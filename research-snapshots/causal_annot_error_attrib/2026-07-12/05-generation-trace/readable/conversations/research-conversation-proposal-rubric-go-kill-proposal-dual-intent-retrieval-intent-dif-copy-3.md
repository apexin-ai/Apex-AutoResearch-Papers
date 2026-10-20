# Research conversation: 【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。 【proposal】: # Dual-Intent Retrieval: Intent-Dif

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 39
- **Recorded user turns:** 1
- **Tool calls:** 9
- **Original source:** `logs/chats/exported-trajectories/account-3/6959a7ca-d39c-4100-bbdf-21ac425702af.jsonl`
- **Structured JSON:** [`40edd87912f1b23e98f4.json`](../../sessions/40/40edd87912f1b23e98f4.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-16T01:48:41.483Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-16T01:48:41.483Z",
  "sessionId": "6959a7ca-d39c-4100-bbdf-21ac425702af",
  "content": "【任务】: 请评估以下 proposal 的客观中稿概率。\n必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。\n\n【proposal】:\n# Dual-Intent Retrieval: Intent-Differentiated Query Formulation for Reasoning-Augmented RAG\n\n**状态**: 待审阅  \n**级别**: top-tier  \n**创建时间**: 2026-05-15T16:06:37.791174+00:00\n\n## 描述\nWe propose Dual-Intent Retrieval, a method that explicitly classifies each retrieval call within a reasoning model's chain-of-thought as either discovery-intent (seeking new evidence to advance reasoning) or verification-intent (seeking evidence to confirm or refute an intermediate claim), then applies structurally different query construction and retrieval strategies for each. Discovery queries use standard BM25 retrieval, matching its strength at keyword-rich information-seeking queries. Verification queries use a hybrid BM25+dense retrieval pipeline with NLI-based contrastive reranking: given an intermediate claim, the model generates contrastive queries (seeded by templates during SFT, refined through RL), retrieves via both BM25 and E5-base-v2 dense retrieval, and re-ranks by evidential discriminativeness using DeBERTa-v3-base NLI scoring, surfacing documents that most clearly support or refute the claim.\n\nThis operationalizes an insight that ReaLM-Retrieve empirically observed but did not act upon: its behavioral analysis (Section 6.9) identifies 'verification retrievals' as a distinct pattern in 31% of cases that reduces backtracking by 18%, while its failure analysis finds that over-retrieval during exploration accounts for 31% of failures. Despite observing that retrieval intent varies structurally, ReaLM-Retrieve's QueryGen maps all retrieval calls through the same learned embedding space without differentiating strategy. Even Veri-R1 (Oct 2025), which trains verification-specific RL policies via GRPO with a multi-component reward (label + evidence IoU + format + validity), uses uniform query construction across all search turns. We make this insight actionable.\n\nThe approach addresses a broader gap: ReaLM-Retrieve adapts queries implicitly without distinguishing purpose; CoRAG (NeurIPS 2025) reformulates queries iteratively but uniformly; DeepControl (ICLR 2026 Workshop) controls retrieval volume, not query strategy; AutoRefine (NeurIPS 2025) refines evidence post-retrieval; RAG-Star (NAACL 2025) verifies answers in MCTS with uniform retrieval; Veri-R1 (Oct 2025) trains verification-specific RL but uses uniform query construction; RAFTS (ACL 2024) demonstrates contrastive argument synthesis for fact-checking but operates standalone; Reason and Verify (Mar 2026) structures verification taxonomies for biomedical RAG but applies uniform retrieval. None classify intent and differentiate query construction within RL-trained sequential reasoning.\n\nThe contribution is dual: (1) explicit intent classification with structurally differentiated retrieval pipelines, and (2) RL-discovered verification query strategies that emerge from the &lt;verify>claim ||| query&lt;/verify> format. The latter is a co-equal contribution: the structured format creates a rich action space for GRPO to discover sophisticated verification strategies (e.g., negation patterns, contrastive framing, claim-type-specific formulations) that humans might not manually design — and the query evolution analysis in Phase 3 is positioned as a key expected finding.\n\nBuilt atop Search-R1's open-source RL framework using Qwen2.5-7B (chosen over Qwen3-8B to avoid a known 10-20× GRPO training speed regression in veRL), we introduce intent tokens (&lt;discover>/&lt;verify>) and train via GRPO with a composite reward combining answer correctness and faithfulness. A critical design choice: we use different NLI model families for verification reranking (DeBERTa-v3-base, 184M params) vs. faithfulness reward (RoBERTa-large-NLI, 355M params) to prevent circular optimization where the policy learns to game its own reward signal. Intent labels are bootstrapped via heuristic rules for SFT cold start, then refined through RL. The &lt;verify>claim ||| query&lt;/verify> format allows RL to learn sophisticated query formulations beyond initial templates, following RAFTS's insight that LLM-generated contrastive formulations outperform fixed templates. We evaluate on six benchmarks — MuSiQue, HotpotQA, 2WikiMultiHopQA, StrategyQA, FEVER, and HOVER — against Search-R1, IRCoT, AutoRefine, RAG-Star, and Veri-R1 baselines (with model-scale caveats for Veri-R1's 3B models and ReaLM-Retrieve's 32B). StrategyQA tests implicit multi-hop reasoning where the model must infer what type of evidence to seek; FEVER is the canonical claim verification benchmark directly comparable with Veri-R1's evaluation; HOVER tests multi-hop verification — together providing comprehensive coverage of both the discovery and verification aspects of our contribution. A mandatory pilot validates that discovery/verification intent is distinguishable — well-motivated given ReaLM-Retrieve's 31% verification rate.\n\n**Compute budget with verified arithmetic:** The entire pipeline fits within ~202 H100-hours (hard cap ≤210). Phase 2 (the dominant cost) runs 2 GRPO training configurations × 500 steps each on 8×H100. Per-step time is ~75 sec (range: 65-90 sec; calibrated from veRL benchmarks showing 60-70 sec/step for Qwen2.5-7B on 8×A800, ms-swift issue #3302, with Search-R1 retrieval overhead partially offset by H100 throughput). Per run: 500 steps × 75 sec = 10.4 wall-hours × 8 GPUs = ~83 H100-hours. Two runs = ~166 H100-hours. Plus overhead (pilot 5h, SFT 5h, NLI 8h, eval 18h) = ~202 H100-hours. 500 steps matches Search-R1's own protocol and exceeds AutoRefine's 300-step convergence; GRPO risks reward collapse beyond 500 steps, making this a well-calibrated choice. Contingency: reduce to 400 steps if per-step exceeds 90 sec, giving ~196h total.\n\nPrimary target: AAAI 2027 (abstract ~July 21, full paper ~July 28, 2026), providing a comfortable ~10-week window. The May 25, 2026 ARR cycle — the last eligible for EMNLP 2026 (commitment deadline August 2, 2026; note: there is no June ARR cycle, as ARR switched to 10-week review cycles) — is a stretch goal only. ICLR 2027 (~October 2026) serves as a fallback for extended experiments.\n\n## 核心问题\nCurrent reasoning-augmented retrieval systems optimize various aspects of the retrieval-reasoning interface — when to retrieve (ReaLM-Retrieve), how much to retrieve (DeepControl), how to refine retrieved evidence (AutoRefine), and how to coordinate retrieval with reasoning structure (DualRAG, HARIS) — yet all treat query construction as a single undifferentiated process. ReaLM-Retrieve's learned QueryGen module generates context-adaptive query representations via cross-attention to reasoning step embeddings, adapting queries implicitly through learned representations. Critically, ReaLM-Retrieve's own behavioral analysis (Section 6.9) empirically identifies 'verification retrievals' as a distinct pattern in 31% of cases — reducing backtracking by 18% — and its failure analysis finds that 'over-retrieval during exploration' accounts for 31% of failures (Section 7.3). These observations directly evidence that retrieval intent varies structurally within reasoning chains and that intent-mismatched retrieval actively degrades performance. Yet ReaLM-Retrieve does not operationalize this insight: its QueryGen maps all retrieval calls through the same continuous embedding space, conflating exploratory and confirmatory information needs. No system explicitly classifies the purpose of each retrieval call within a reasoning chain and applies structurally different query construction strategies accordingly. Even Veri-R1 (Oct 2025), which specifically trains models for claim verification via GRPO with iterative retrieval across up to 3 search turns, applies the same uniform query construction strategy across all retrieval calls — further evidencing that the discovery/verification distinction is not operationalized even in verification-specialized systems. Within a reasoning chain, a retrieval call seeking new evidence to explore an unknown sub-question (discovery) requires broad, recall-oriented queries, while one checking whether a specific intermediate claim holds (verification) requires targeted, claim-contrastive queries that seek both supporting and refuting evidence. Implicit query adaptation via learned representations cannot capture this structural distinction because a verification query should actively seek disconfirming evidence, which is anti-correlated with the topical relevance signal that learned query generators optimize for. This intent-blind retrieval means verification-stage retrievals return topically relevant but evidentially uninformative documents, degrading reasoning faithfulness. The problem is compounded by evidence that retrieval can actively hurt reasoning when poorly matched to reasoning needs — Shakya et al. (2026) show that traces including retrieval perform slightly worse than CoT without retrieval, but that adaptive retrieval (choosing when to retrieve) improves overall performance, suggesting that retrieval quality and intent matching — not just retrieval timing or volume — is a critical bottleneck.\n\n## 机遇 / Why Now\nReaLM-Retrieve empirically observed that retrieval intent varies within reasoning chains — identifying verification retrievals (31% of cases) as a distinct beneficial pattern and over-retrieval during exploration (31% of failures) as a primary failure mode — but did not operationalize this insight. We make it actionable via explicit intent classification and structurally differentiated query construction.\n\nReasoning models now produce long CoT traces with explicit intermediate claims that create a structurally exploitable retrieval signal: 'retrieve evidence to check claim X' is functionally distinct from 'retrieve evidence to answer question Y,' and these two modes demand different query construction strategies — yet no existing system makes this distinction explicit and operationalizes it at query construction time.\n\nRecent work has advanced adjacent aspects of this space without addressing this core gap. On implicit query adaptation: ReaLM-Retrieve (Apr 2026) uses a learned single-layer transformer decoder QueryGen that generates context-adaptive 768-dim query embeddings via cross-attention to reasoning step representations, achieving 71.2% F1 on MuSiQue (+11.8% over standard RAG) with only 1.8 retrieval calls — but its learned representations adapt queries implicitly without distinguishing retrieval purpose, and its own error analysis reveals this as a limitation. On retrieval-verification in tree search: RAG-Star (NAACL 2025) uses retrieval-augmented verification within MCTS, scoring answer-document consistency to guide tree search backpropagation, but applies uniform retrieval for every sub-query and operates in tree-structured (not sequential) reasoning. On iterative query reformulation: CoRAG (NeurIPS 2025) dynamically reformulates queries based on evolving reasoning state via rejection sampling, achieving SOTA on KILT, but applies the same reformulation strategy regardless of whether the model needs exploration or confirmation. On retrieval control: DeepControl (ICLR 2026 Workshop) measures marginal information utility to control retrieval continuation and granularity (+9.4% over Search-R1 on Qwen2.5-7B), but controls how much to retrieve, not how to construct purpose-differentiated queries. On evidence refinement: AutoRefine (NeurIPS 2025) introduces a &lt;refine> step between search calls with retrieval-specific rewards via GRPO, dramatically improving multi-hop QA, but refines evidence post-retrieval without differentiating query construction. On reasoning-aware retrieval embeddings: AgentIR (Mar 2026) encodes reasoning traces into retrieval embeddings for intent-aware retrieval but treats all retrieval calls uniformly without intent classification. On RL-trained claim verification: Veri-R1 (Oct 2025) trains Qwen2.5-3B-Instruct via GRPO for iterative claim verification on FEVEROUS/FEVER/HOVER/SciFACT, improving joint accuracy by 30% and doubling evidence scores — but applies the same query strategy across all search turns despite being verification-specialized. On domain-specific structured verification: Reason and Verify (Mar 2026) integrates explicit sub-claim grounding with an eight-category verification taxonomy for biomedical RAG, achieving 89.1% on BioASQ-Y/N — but applies uniform retrieval without intent classification and is not RL-trained.\n\nThe precise gap: existing systems adapt query representations implicitly through learned embeddings (ReaLM-Retrieve, CoRAG, AgentIR), reformulate queries iteratively (CoRAG), control retrieval volume (DeepControl), refine evidence post-retrieval (AutoRefine, SURE-RAG, Entropic Claim Resolution), verify answers in tree search (RAG-Star), train verification-specific RL policies with uniform retrieval (Veri-R1), or structure verification taxonomies in domain-specific settings (Reason and Verify) — but none explicitly classifies retrieval intent as discovery vs. verification and applies structurally different query construction strategies for each, particularly claim-contrastive retrieval that actively seeks disconfirming evidence for verification-intent calls. ReaLM-Retrieve's own analysis shows this distinction exists and matters; Veri-R1's uniform approach to verification-specific retrieval confirms it remains unaddressed even in the most targeted systems. We operationalize it.\n\n## 方法思路\nWe build a dual-intent retrieval module on top of the open-source Search-R1 framework that introduces explicit intent-differentiated query formulation into reasoning-augmented retrieval. The approach has four phases designed to fit within ~200 H100-hours and ~11 days.\n\n**Model choice: Qwen2.5-7B.** We use Qwen2.5-7B as the primary model, not Qwen3-8B. This is a deliberate choice motivated by a known, unresolved training speed regression: Qwen3-8B exhibits 10-20× slower generation during veRL GRPO training compared to Qwen2.5-7B (veRL GitHub issues #1580, #3816), with each step taking ~1 hour instead of minutes. The root cause appears to be Qwen3's thinking mode generating excessively long outputs (~7000 tokens vs ~1000 tokens), and this affects even non-thinking configurations due to architectural differences in how vLLM handles Qwen3. Qwen2.5-7B is the backbone Search-R1 was originally validated on, with proven GRPO training efficiency and 24% average relative improvement on QA benchmarks. We use Qwen2.5-7B-Base for the primary experiments, consistent with Search-R1's original evaluation.\n\n**Phase 0 — Pilot Feasibility (Day 1, ~5 H100-hours):** Generate reasoning traces on 500 MuSiQue training examples using standard Search-R1 with Qwen2.5-7B. Apply heuristic rules to classify each &lt;search> call: if the preceding reasoning contains an explicit claim or assertion ('X is Y', 'therefore', 'this means') followed by retrieval, label it VERIFY; if it contains a question decomposition or information-seeking pattern ('I need to find', 'what is', sub-question form), label it DISCOVER. Manually inspect 100 labeled examples and compute distribution statistics. Go/no-go: proceed only if both categories appear with ≥15% frequency and heuristic accuracy ≥75%. This threshold is well-motivated: ReaLM-Retrieve's analysis found verification retrievals comprise 31% of cases, suggesting ≥15% is easily achievable.\n\n**Phase 1 — Implementation (Days 2-4):** Extend the Search-R1 token format: replace the single &lt;search>query&lt;/search> with two intent-tagged variants: &lt;discover>query&lt;/discover> and &lt;verify>claim ||| query&lt;/verify>. The verify format includes both the claim and an optional model-generated query, enabling RL to learn sophisticated query formulations beyond templates. This dual-format design serves a deeper purpose beyond mere classification: by structuring verification retrieval as explicit claim ||| query pairs, we give the RL optimization a rich action space in which to develop intent-specific query patterns. The model must learn not just what to search for, but how to construct queries that surface evidence specifically relevant to confirming or refuting its tentative claim — a fundamentally different skill from exploratory information-seeking. Implement differentiated query processing in the search environment:\n\n(a) Discovery mode — pass the query to BM25, return top-3 results (same as baseline). BM25 is appropriate for discovery queries because they tend to be keyword-rich and information-seeking, matching BM25's lexical matching strength.\n\n(b) Verification mode — uses a hybrid retrieval pipeline to address the limitation that BM25 performs poorly on semantically-oriented contrastive queries. Extract the claim and the model-generated query (or, during SFT cold-start, generate a contrastive query pair via templates: 'evidence supporting [claim]' / 'evidence contradicting [claim]'). Retrieve top-3 via BM25 (lexical match on claim content) and top-3 via dense retrieval (E5-base-v2, which Search-R1 already supports as a retrieval backend) using the contrastive queries. Pool the 6 results, re-rank by evidential discriminativeness using an NLI cross-encoder (cross-encoder/nli-deberta-v3-base, 184M params) to score entailment and contradiction, returning the top-3 documents ranked by |entailment − contradiction| score (most discriminative first). The hybrid BM25+dense approach is motivated by evidence that hybrid retrieval improves recall by 15-30% over either method alone, and dense retrieval is critical for semantic matching on contrastive queries where keywords like 'supporting'/'contradicting' are uninformative for BM25. Note: Search-R1 provides pre-built E5-base-v2 FAISS indexes for its Wikipedia corpus, eliminating index-building overhead.\n\n**Template limitation and RL-learned query refinement (co-equal contribution):** We acknowledge that template-based contrastive queries ('evidence supporting/contradicting [claim]') are simplistic — real verification needs are more nuanced (causal claims require different evidence patterns than factual or temporal claims). The &lt;verify>claim ||| query&lt;/verify> format is specifically designed to allow the model to learn more sophisticated query formulations through RL. During SFT cold-start, templates provide the initial format. During GRPO training, the model is free to generate arbitrary text in the query field, learning from outcome rewards which query formulations yield the most useful evidence. This follows RAFTS's (ACL 2024) insight that LLM-generated contrastive arguments outperform fixed templates, but integrates the learning directly into the RL loop rather than requiring a separate generation step. We position the RL-discovered verification query strategies as a co-equal contribution alongside the intent taxonomy itself: if the model learns to use negation patterns, hedge framing, contrastive structures, or claim-type-specific formulations that humans would not manually design, this constitutes a compelling finding about how structured action spaces enable emergent strategy discovery through reward optimization.\n\nSFT cold start: relabel heuristically-classified Search-R1 traces with intent tokens and fine-tune Qwen2.5-7B-Base for ~100 steps to learn the new format.\n\nNote on Search-R1 RL algorithm: Search-R1 supports both PPO and GRPO via separate training scripts (train_ppo.sh and train_grpo.sh) built on the veRL framework. We use the GRPO configuration for training efficiency and stability, consistent with recent work (AutoRefine, DeepControl, Veri-R1) that also builds on Search-R1 with GRPO.\n\n**NLI model separation to avoid reward circularity:** A critical design decision is using different NLI models for verification reranking vs. faithfulness reward computation, to prevent a circular optimization where the model learns to game its own reward signal. During verification-intent retrieval, documents are reranked by |entailment − contradiction| via cross-encoder/nli-deberta-v3-base (DeBERTa architecture, 184M params). The faithfulness reward component uses a different model family: ynie/roberta-large-snli_mnli_fever_anli_R1_R2_R3-nli (RoBERTa-large architecture, 355M params, trained on SNLI+MNLI+FEVER+ANLI). Using different architectures (DeBERTa disentangled attention vs. RoBERTa standard attention) and different training data distributions ensures the models have different decision boundaries, preventing the policy from learning to select documents that trivially satisfy the reward without genuinely improving evidential quality. The circularity concern is real: if the same model ranks documents and scores faithfulness, the optimization target reduces to 'retrieve documents that this specific model scores highly on' rather than 'retrieve genuinely informative evidence.' Different models with different inductive biases prevent this collapse.\n\n**NLI reranking cost analysis:** DeBERTa-v3-base (184M params) processes ~800-1200 sentence pairs/sec on a single H100. During GRPO training with global batch size B=256, average R=2.5 retrieval calls per sample, and estimated verification fraction V=0.4, total NLI pairs per step = B × R × V × 6 = 256 × 2.5 × 0.4 × 6 ≈ 1,536 pairs. At 1,000 pairs/sec, this adds ~1.5 seconds per step. The RoBERTa-large reward model (355M params) processes ~400-600 pairs/sec; with ~3 claims per trace × 256 samples = ~768 pairs, adding ~1.5 seconds per step. Combined NLI overhead is ~3 seconds per step. Compared to the LLM forward/backward pass on 8×H100 with Qwen2.5-7B, total NLI overhead is ~5-10% — manageable without dedicated hardware. To minimize memory contention, we run NLI inference on CPU (adding ~10-15 sec per step, still <25% overhead) or allocate a fraction of one GPU's memory. We budget an additional ~8 H100-hours for NLI overhead across all training runs.\n\n**Phase 2 — RL Training (Days 5-8, ~166 H100-hours on 8×H100):** Train with GRPO using a composite reward: R = α·EM(answer) + (1−α)·faithfulness, where faithfulness is the fraction of intermediate claims in the reasoning trace that are supported (entailment > 0.5) by at least one retrieved document, scored by the RoBERTa-large NLI model (distinct from the DeBERTa reranker). Set α = 0.7 (tunable). Run two configurations: (1) full dual-intent with hybrid contrastive verification retrieval (primary), (2) standard Search-R1 baseline with GRPO (ablation: no intent). The BM25-only ablation (dual-intent tokens with standard retrieval for both modes) is deferred to save compute; it can be added as a reduced-scale 250-step run (~28 H100-hours) if the primary runs finish under budget.\n\n**Per-run compute arithmetic:** Each run uses 500 training steps on 8×H100, matching Search-R1's own training protocol (the original Search-R1 paper trains for exactly 500 steps with checkpoints every 100 steps). Per-step time estimate: the veRL GRPO benchmark shows 60-70 sec/step for Qwen2.5-7B full-parameter GRPO on 8×A800 with NuminaMath-TIR (ms-swift issue #3302). Search-R1's multi-turn retrieval adds overhead from search engine calls during rollout generation (~2-4 search calls per trajectory with BM25 latency <50ms each) and longer context sequences (max_prompt_length=4096 vs ~2048 for math). H100's ~1.3× throughput advantage over A800 partially offsets this overhead. We estimate ~75 sec/step (range: 65-90 sec), yielding: 500 steps × 75 sec = 37,500 sec ≈ 10.4 wall-hours per run. Per-run GPU-hours: 10.4 wall-hours × 8 GPUs = **~83 H100-hours**. Two runs total: **~166 H100-hours**. **Contingency:** if per-step time exceeds 90 sec, reduce to 400 steps per run — still above AutoRefine's 300-step convergence point — giving 400 × 90 sec ≈ 10.0 wall-hours × 8 GPUs ≈ 80 H100-hours per run, ~160 H100-hours total for Phase 2.\n\n**Convergence justification for 500 steps:** 500 steps matches Search-R1's own training protocol, where the original paper uses exactly 500 steps for both Qwen2.5-3B and Qwen2.5-7B with GRPO. AutoRefine (NeurIPS 2025), built on the same Search-R1/veRL/GRPO stack, trains for only 300 steps and achieves its reported gains (HotpotQA: 0.405 F1, MuSiQue: 0.157 F1). GRPO-LEAD converges in ~200 steps with top-performing checkpoints selected via validation. Empirical GRPO training dynamics show gradient norms stabilize by step 40, with most accuracy gains in the first 200-300 steps. Additionally, GRPO is known to risk reward collapse when trained for too many steps, further motivating 500 steps as a well-calibrated choice rather than a compromise.\n\n**Phase 3 — Evaluation & Analysis (Days 9-11, ~18 H100-hours):** Evaluate on MuSiQue, HotpotQA, 2WikiMultiHopQA, StrategyQA, FEVER, and HOVER (6 benchmarks). MuSiQue, HotpotQA, and 2WikiMultiHopQA are standard multi-hop QA benchmarks requiring compositional reasoning with explicit decomposition. StrategyQA requires implicit multi-hop reasoning where the decomposition strategy is not given — the model must infer what type of evidence to seek, making it an ideal showcase for intent-differentiated retrieval since the discovery/verification transition is not signaled by the question structure but must emerge from the model's reasoning process. FEVER is the canonical fact verification benchmark (185K claims, supported/refuted/NEI) — essential for a method whose core contribution involves verification-intent retrieval, and directly comparable with Veri-R1's evaluation on the same benchmark. HOVER is a multi-hop claim verification benchmark requiring evidence from 2-4 Wikipedia articles, testing both discovery (finding relevant articles across hops) and verification (confirming multi-hop claims against aggregated evidence). Metrics: answer F1/EM, faithfulness (claim-support rate), retrieval precision/recall on supporting evidence. Baselines: Search-R1 (reproduced with GRPO), IRCoT, and ReaLM-Retrieve (reported numbers with model-scale caveats, as their best results use DeepSeek-R1-Distill-Qwen-32B). Additional comparisons: AutoRefine (reported numbers, NeurIPS 2025), RAG-Star (reported numbers from Llama-3.1-8B-Instruct), Veri-R1 (reported numbers on HOVER and FEVER, with model-scale caveats since Veri-R1 uses Qwen2.5-3B-Instruct and Llama3.2-3B-Instruct while we use 7B; we will report per-parameter efficiency where feasible to enable fair comparison). Analysis: (a) intent distribution — what fraction of retrievals are classified as discovery vs. verification across all six benchmarks, and how this compares to ReaLM-Retrieve's observed 31% verification rate, (b) per-intent retrieval quality — does verification mode retrieve more evidentially discriminative documents (measured by |entailment − contradiction| spread), (c) comparison with implicit adaptation — does explicit intent classification outperform ReaLM-Retrieve's learned QueryGen on verification-heavy reasoning chains, (d) NLI model separation analysis — compare performance with same-model vs. different-model reranking/reward to quantify circularity effects, (e) **query evolution analysis (key expected finding)** — do RL-learned verification queries diverge from initial templates, and what patterns emerge (claim-type-specific formulations, negation patterns, contrastive framing, hedge structures, etc.)? This analysis is positioned as a key finding, not merely a diagnostic: if RL discovers intent-specific query patterns that humans wouldn't write — e.g., systematically different query structures for causal vs. factual vs. temporal claims — that constitutes a compelling result in its own right, demonstrating that the structured &lt;verify>claim ||| query&lt;/verify> format enables emergent strategy discovery through reward optimization, (f) error analysis — when does intent misclassification degrade performance, (g) case studies showing how contrastive verification queries surface disconfirming evidence that standard and implicitly-adapted queries miss, (h) StrategyQA-specific analysis — does intent-differentiated retrieval show disproportionate gains on implicit decomposition tasks where the model must infer retrieval intent without explicit question structure?\n\n**Design justifications:** The binary discovery/verification taxonomy is the minimal distinction that captures the most variance in retrieval intent within reasoning chains. This choice is now directly grounded in ReaLM-Retrieve's empirical findings: their three behavioral patterns (early resolution 42%, verification 31%, failed retrieval 12%) naturally collapse into our binary taxonomy — early resolution and failed retrieval are both discovery-intent (information-seeking), while verification retrievals map directly to our verification-intent. The choice is further motivated by Shakya et al.'s (2026) finding that retrieval during exploration can hurt reasoning while adaptive retrieval helps — suggesting that the exploration/confirmation axis is the primary dimension along which retrieval intent varies. Finer categories (clarification, disambiguation, quantitative validation) are subsumed: clarification and disambiguation are discovery subtypes, quantitative/causal verification are verification subtypes. Binary classification is also more robust with limited RL training budget and avoids the need for multi-class intent supervision. The framework is extensible to additional intent types via new tokens.\n\nThe key distinction from related approaches: ReaLM-Retrieve's QueryGen learns a continuous mapping from reasoning states to query embeddings, and its own analysis reveals that verification retrievals are a distinct beneficial pattern — but it does not operationalize this insight by applying different retrieval pipelines. Veri-R1 trains verification-specific RL policies with a multi-component reward (label + evidence IoU + format + validity) but uses the same uniform query strategy across all search turns — even its emergent 'fine-grained subclaim-level decomposition' is not structurally supported by differentiated retrieval. Our approach makes intent classification explicit and applies structurally different retrieval pipelines — critically, verification queries use hybrid BM25+dense retrieval with NLI-based contrastive reranking to actively seek disconfirming evidence, which is anti-correlated with topical relevance maximization. RAG-Star uses retrieval for verification within MCTS but verifies candidate answers at tree nodes with uniform relevance-based retrieval, not intermediate claims with contrastive queries. AutoRefine's &lt;refine> step distills evidence post-retrieval but doesn't change how queries are constructed. CoRAG reformulates queries iteratively but applies the same reformulation strategy regardless of intent. DeepControl controls retrieval volume and timing but not query construction strategy. RAFTS (ACL 2024) demonstrates that contrastive argument synthesis improves fact verification, but operates as a standalone pipeline — we integrate contrastive retrieval directly into the RL-trained reasoning loop. Reason and Verify (Mar 2026) structures verification with an eight-category taxonomy for biomedical RAG but applies uniform retrieval — we address a different dimension (retrieval pipeline differentiation) in a domain-general RL-trained setting.\n\nThe contribution is dual: (1) explicit intent classification with structurally differentiated retrieval pipelines, and (2) RL-discovered verification query strategies that emerge from the &lt;verify>claim ||| query&lt;/verify> format — the latter being a co-equal contribution that may yield insights about how structured action spaces enable emergent retrieval strategies.\n\nFallback: if claim extraction quality is poor in the reasoning trace (e.g., no clear propositional claim before a retrieval call), default to discovery mode — this is safe because discovery mode is equivalent to the baseline.\n\n## 研究现状\nThe reasoning-augmented retrieval landscape in 2025-2026 has advanced along five axes — implicit query adaptation, retrieval timing/volume control, retrieval-reasoning coordination, post-retrieval evidence quality, and reasoning-stage verification — creating a rich but precisely gapped design space.\n\n**Implicit query adaptation.** ReaLM-Retrieve achieves 71.2% F1 on MuSiQue with 1.8 retrieval calls by combining step-level uncertainty-based retrieval timing with a learned QueryGen module (single-layer transformer decoder, 512 hidden dim, 8 attention heads) that cross-attends to current reasoning step embeddings, producing context-adaptive 768-dim query representations for ColBERTv2 dense retrieval. The +11.8% F1 improvement on MuSiQue (+10.1% average across three benchmarks) demonstrates that adaptive query generation substantially outperforms static queries. Crucially, ReaLM-Retrieve's own behavioral analysis (Section 6.9) identifies three dominant retrieval patterns: 'early resolution' (42% of cases, yielding 23% shorter reasoning chains), 'verification retrievals' (31%, reducing backtracking by 18%), and 'failed retrievals' (12%, extending chains by 8%). Its failure analysis (Section 7.3) finds that over-retrieval during exploratory reasoning phases accounts for 31% of failures by 'disrupting productive chains by prematurely committing to hypotheses.' These observations directly evidence that retrieval intent varies structurally and that intent-mismatched retrieval degrades performance — yet QueryGen's cross-attention mechanism learns a single continuous mapping from reasoning states to query embeddings, conflating exploratory and confirmatory needs into the same representation space. CoRAG (NeurIPS 2025) dynamically reformulates queries based on evolving reasoning state via rejection sampling training, establishing SOTA on KILT with >10-point EM improvements on multi-hop QA, but applies uniform reformulation strategy regardless of retrieval purpose. AgentIR (Mar 2026) encodes reasoning traces into retrieval embeddings for intent-aware retrieval but treats all retrieval calls uniformly without intent classification.\n\n**Retrieval timing and volume control.** DeepControl (ICLR 2026 Workshop) formalizes information utility as U(e) = ρ·Novelty + (1−ρ)·Effectiveness, using an annealed control-forcing curriculum to train retrieval continuation and granularity control, achieving +9.4% on Qwen2.5-7B over RL baselines across seven benchmarks. R1-Searcher++ trains models to decide whether to use internal knowledge or external search. Shakya et al. (Feb 2026) find that 'traces including retrieval actually perform worse compared to CoT' while the model's decision to adaptively avoid retrieval improves overall performance — suggesting that retrieval quality and intent matching matters more than retrieval quantity.\n\n**Retrieval-reasoning coordination.** Search-R1 trains LLMs via RL (supporting both PPO and GRPO) to issue search queries within reasoning, achieving +41%/+20% on QA benchmarks for 7B/3B models, with Qwen2.5-7B as the primary validated backbone. AutoRefine (NeurIPS 2025) introduces a &lt;refine> step between search calls that distills evidence from ~600 to ~100-200 tokens, trained with GRPO using dual rewards (answer correctness + retrieval quality), achieving major gains on multi-hop QA (HotpotQA: 0.405 vs 0.297 Search-R1; MuSiQue: 0.157 vs 0.066). DualRAG (ACL 2025) coordinates reasoning-augmented querying with progressive knowledge aggregation. HARIS (arXiv 2506.07528, Jun 2025) uses a hierarchical two-agent architecture (reasoning + search) with GRPO training on Qwen3-4B, evaluating on EX-FEVER (80.12% F1 on 2-hop) and HOVER (61.00% accuracy on 4-hop) for claim verification — but with uniform search strategy across all retrieval calls. IRCoT interleaves retrieval at fixed intervals.\n\n**Post-retrieval evidence quality.** SURE-RAG (May 2026) scores claim-evidence pairs for sufficiency. Entropic Claim Resolution (Mar 2026) selects discriminative evidence via entropy minimization. RAFTS (ACL 2024) synthesizes contrastive supporting/refuting arguments from retrieved passages via LLM-based generation with a two-stage BM25+dense retrieval pipeline for standalone fact verification — demonstrating that contrastive evidence framing improves verification accuracy, but operating as a standalone fact-checking system rather than integrated in reasoning RL loops. Reason and Verify (arXiv 2603.10143, Mar 2026) integrates explicit sub-claim grounding with an eight-category verification taxonomy for biomedical RAG, achieving 89.1% on BioASQ-Y/N with Llama-3-8B-Instruct. Though domain-specific (biomedical) and not RL-trained, it demonstrates concurrent interest in structured verification within RAG, using BGE cross-encoder reranking and rationale grounding — but applies uniform retrieval without intent classification. REPAIR (Jan 2026) uses reasoning plans for mid-course correction during reranking. All operate downstream of query construction.\n\n**Reasoning-stage verification.** RAG-Star (NAACL 2025) uses MCTS for deliberative reasoning with retrieval-augmented verification: for each MCTS node, retrieval checks answer-document consistency (scoring 1=unverifiable, 2=conflict, 3=aligned) with query- and answer-aware reward modeling. However, RAG-Star verifies candidate answers at MCTS tree nodes using uniform retrieval, not intermediate claims within sequential reasoning chains, and does not use contrastive queries to actively seek disconfirming evidence. Veri-R1 (arXiv 2510.01932, Oct 2025) is the most directly comparable RL-based verification system: it trains Qwen2.5-3B-Instruct and Llama3.2-3B-Instruct via GRPO for iterative claim verification with up to 3 search turns, using a 4-component reward (label correctness +2, evidence IoU, format compliance, validity weight). Evaluated on FEVEROUS, EX-FEVER, FEVER, SciFACT, and HOVER, Veri-R1 improves joint accuracy by up to 30% and doubles evidence scores vs baselines. Open-source and built on Search-R1/veRL. Critically, despite being designed specifically for claim verification, Veri-R1 does NOT differentiate retrieval intent — all search queries use the same uniform strategy, whether the model is exploring for initial evidence or confirming a tentative conclusion. Its case analysis shows Online RL naturally develops 'fine-grained subclaim-level decomposition,' but this emergent behavior is not structurally supported by differentiated retrieval pipelines. FIRE (NAACL Findings 2025) uses confidence-based iterative retrieval for fact-checking with 7.6× cost reduction but applies the same query strategy per iteration. 'Don't Let It Hallucinate' (NeurIPS 2025) transforms queries into logical premises for pre-generation verification, operating before reasoning chains begin. VERITAS rewards faithful reasoning but doesn't modify retrieval.\n\n**The gap.** All existing systems either (a) adapt query representations implicitly through learned embeddings without distinguishing retrieval purpose — even when their own analysis shows the distinction exists and matters (ReaLM-Retrieve, CoRAG, AgentIR), (b) control retrieval timing/volume without differentiating query construction (DeepControl, R1-Searcher++), (c) refine evidence post-retrieval without improving the upstream query (AutoRefine, SURE-RAG, ECR, RAFTS), (d) verify answers in tree search or pre-generation without contrastive query construction within sequential reasoning (RAG-Star, FIRE, Don't Let It Hallucinate), (e) train verification-specific RL policies but still use uniform query construction across all search turns (Veri-R1), or (f) structure verification taxonomies in domain-specific settings without intent-differentiated retrieval (Reason and Verify). No system explicitly classifies retrieval intent as discovery vs. verification within sequential reasoning chains and applies structurally different query construction strategies for each — particularly claim-contrastive retrieval that actively seeks disconfirming evidence during verification.\n\n## 目标 Venue\n- AAAI 2027 (abstract ~July 21, 2026; full paper ~July 28, 2026 — primary target with comfortable ~10-week window for experiments, analysis, and paper writing)\n- ARR May 25, 2026 → EMNLP 2026 (commitment deadline August 2, 2026) — stretch goal only, requires aggressive 10-day execution with pre-existing Search-R1/veRL familiarity; note: this is the last eligible ARR cycle for EMNLP 2026, as the next ARR cycle (August 3, 2026) falls after the EMNLP commitment deadline; no June ARR cycle exists due to ARR's switch to 10-week review cycles\n- ICLR 2027 (expected ~October 2026 — fallback allowing additional model scales, extended ablations, or supplementary benchmarks)\n\n## 关键参考\n- Search-R1: Training LLMs to Reason and Leverage Search Engines with Reinforcement Learning (arXiv 2503.09516, Mar 2025) — base framework; supports PPO and GRPO via veRL, &lt;search> token format; validated on Qwen2.5-7B with 24% average relative improvement; trains for 500 GRPO steps with checkpoints every 100 steps; provides pre-built BM25 and E5 FAISS indexes for Wikipedia corpus\n- When to Retrieve During Reasoning: Adaptive Retrieval for Large Reasoning Models [ReaLM-Retrieve] (arXiv 2604.26649, Apr 2026) — learned QueryGen module (single-layer transformer decoder, cross-attention to reasoning step embeddings, 768-dim adaptive query representations); +11.8% F1 on MuSiQue (71.2%), +10.1% average across 3 benchmarks; Section 6.9 identifies verification retrievals (31% of cases) as a distinct pattern reducing backtracking by 18%; Section 7.3 identifies over-retrieval during exploration as 31% of failures; implicitly adaptive but not intent-differentiated despite observing the need\n- RAG-Star: Enhancing Deliberative Reasoning with Retrieval Augmented Verification and Refinement (NAACL 2025, Jiang et al.) — MCTS-based reasoning with retrieval-augmented verification at tree nodes (answer-document consistency scoring), query- and answer-aware reward modeling; verifies candidate answers in tree search with uniform retrieval, not intermediate claims with contrastive queries\n- Chain-of-Retrieval Augmented Generation [CoRAG] (NeurIPS 2025, arXiv 2501.14342) — dynamic query reformulation via rejection sampling training, SOTA on KILT, >10-point EM on multi-hop QA; reformulates queries based on evolving state but without intent differentiation\n- Scaling Search-Augmented LLM Reasoning via Adaptive Information Control [DeepControl] (arXiv 2602.01672, ICLR 2026 Workshop SPOT) — information utility = ρ·Novelty + (1−ρ)·Effectiveness, retrieval continuation and granularity control with annealed curriculum; +9.4% on Qwen2.5-7B over RL baselines; controls retrieval volume, not query construction strategy\n- Search and Refine During Think [AutoRefine] (NeurIPS 2025, arXiv 2505.11277) — &lt;refine> step distilling evidence between search calls, GRPO with dual rewards (answer + retrieval quality); trains for 300 steps on Search-R1/veRL/GRPO stack and achieves convergence; HotpotQA: 0.405 vs 0.297 Search-R1, MuSiQue: 0.157 vs 0.066; refines evidence post-retrieval without intent-differentiated query construction\n- Retrieval Augmented Fact Verification by Synthesizing Contrastive Arguments [RAFTS] (ACL 2024) — LLM-based contrastive supporting/refuting argument synthesis with two-stage BM25+dense retrieval pipeline; demonstrates contrastive evidence framing improves verification; standalone system, not integrated in reasoning RL\n- Veri-R1: Toward Precise and Faithful Claim Verification via Online Reinforcement Learning (arXiv 2510.01932, Oct 2025) — GRPO-trained iterative claim verification with Qwen2.5-3B-Instruct and Llama3.2-3B-Instruct on FEVEROUS/EX-FEVER/FEVER/SciFACT/HOVER; 4-component reward (label correctness + evidence IoU + format compliance + validity weight); improves joint accuracy by 30%, doubles evidence scores; does NOT differentiate retrieval intent despite being verification-focused; open-source on Search-R1/veRL; most directly comparable RL-based verification baseline\n- HARIS: Coordinating Search-Informed Reasoning and Reasoning-Guided Search in Claim Verification (arXiv 2506.07528, Jun 2025) — hierarchical two-agent architecture (reasoning + search) with GRPO training on Qwen3-4B; evaluates on EX-FEVER (80.12% F1 on 2-hop) and HOVER (61.00% accuracy on 4-hop); uniform search strategy without intent differentiation\n- Reason and Verify: A Framework for Faithful Retrieval-Augmented Generation (arXiv 2603.10143, Mar 2026) — biomedical RAG with eight-category verification taxonomy, explicit sub-claim grounding, BGE cross-encoder reranking; 89.1% on BioASQ-Y/N with Llama-3-8B-Instruct; domain-specific but demonstrates concurrent interest in structured verification within RAG; uniform retrieval without intent classification\n- R1-Searcher++: Incentivizing Dynamic Knowledge Acquisition of LLMs via RL (arXiv 2505.17005, May 2025) — internal vs. external knowledge distinction, not intent within external retrieval\n- REPAIR: Adaptive Retrieval for Reasoning-Intensive Retrieval (arXiv 2601.04618, Jan 2026) — reasoning plans for reranking; operates post-retrieval, not at query construction\n- FIRE: Fact-checking with Iterative Retrieval and Verification (NAACL Findings 2025) — confidence-based iterative retrieval; 7.6× cost reduction but same query strategy per iteration\n- Don't Let It Hallucinate: Premise Verification via Retrieval-Augmented Logical Reasoning (NeurIPS 2025) — pre-generation premise verification, not during reasoning chain\n- Adaptive Retrieval helps Reasoning in LLMs — but mostly if it's not used (arXiv 2602.07213, Shakya et al., Feb 2026) — traces with retrieval perform slightly worse than CoT; adaptive retrieval (choosing when to retrieve) improves overall performance; directly motivates that retrieval quality and intent matching matters more than retrieval volume\n- DualRAG: A Dual-Process Approach to Integrate Reasoning and Retrieval for Multi-Hop QA (ACL 2025) — dual reasoning-retrieval processes but uniform retrieval strategy\n- AgentIR: Reasoning-Aware Retrieval for Deep Research Agents (arXiv 2603.04384, Mar 2026) — encodes reasoning traces in embeddings but uniform intent across all retrieval calls\n- SURE-RAG: Sufficiency and Uncertainty-Aware Evidence Verification for Selective RAG (arXiv, May 2026) — post-retrieval claim-evidence scoring\n- Entropic Claim Resolution: Uncertainty-Driven Evidence Selection for RAG (arXiv, Mar 2026) — post-retrieval evidence selection via entropy minimization\n- Beyond Correctness: Rewarding Faithful Reasoning in RAG [VERITAS] (arXiv, Oct 2025) — faithfulness reward for generators, not retrieval modification\n- Interleaving Retrieval with Chain-of-Thought Reasoning [IRCoT] (ACL 2023) — fixed-interval retrieval baseline\n- Adaptive-RAG: Learning to Adapt Retrieval-Augmented LLMs through Question Complexity (NAACL 2024)\n- veRL GitHub issues #1580, #3816 — Qwen3-8B GRPO training 10-20× slower than Qwen2.5-7B due to generation speed regression; motivates our model choice\n- ms-swift GitHub issue #3302 — GRPO training speed benchmark: 60-70 sec/step for Qwen2.5-7B full-parameter GRPO on 8×A800 with veRL; calibrates our per-step compute estimate\n\n## 资源估算\n### auto_research\n- **claude_api_cost**: $200-400 (est. 2000-4000 turns for autonomous experiment design and paper drafting)\n- **estimated_gpu_cost**: ~$630 (210h × ~$3.00/hr)\n- **gpu_hours**: ≤210 H100-hours (hard budget cap). Agent must track cumulative GPU-hours (wall-time × GPUs, not wall-time alone) and prioritize: primary dual-intent run (~83h) and baseline run (~83h) are mandatory; BM25-only ablation at 250 steps (~42h) is included only if cumulative spend remains ≤168h after the two primary runs. If approaching cap, agent reduces ablation steps or skips lowest-priority analysis.\n- **gpu_utilization**: ~85-95% utilization; agent pipelines experiments continuously\n- **risk_note**: Agent should implement early stopping on reward plateau detection (GRPO risks reward collapse beyond ~500 steps); if pilot feasibility fails (intent categories not distinguishable), agent should pivot to testing contrastive verification queries without intent classification\n- **speed_bottleneck**: Primary bottleneck is sequential GRPO runs on 8 GPUs (~10.4 wall-hours each at 75 sec/step); BM25 index pre-built, E5 FAISS index downloadable from Search-R1; NLI inference adds ~5-10% per-step overhead\n- **team**: 0 (initial setup and final review only)\n- **timeline**: 6-9 days with 8×H100 available\n\n### human_in_loop\n- **claude_api_cost**: $100-200 (est. 1000-2000 turns for code generation and experiment analysis)\n- **estimated_gpu_cost**: ~$606-630 (202-210h × ~$3.00/hr)\n- **gpu_hours**: ~202-210 H100-hours. Base plan (~202h) plus agent-proposed extensions with human approval: reduced-scale BM25-only ablation (250 steps on 8×H100 = 250 × 75 sec ≈ 5.2 wall-hours × 8 GPUs ≈ ~42h), reward weighting variants, or heuristic threshold tuning. Extensions prioritized by expected information value within remaining budget.\n- **gpu_utilization**: ~55-70% utilization; agent queues experiments while human reviews\n- **risk_note**: Composite faithfulness+correctness reward may need human judgment on α weighting if RL training shows reward hacking on the faithfulness component; if per-step time exceeds 90 sec, human approves step-count reduction to 400\n- **team**: 1 researcher, ~20-30min/day reviewing proposals and results\n- **timeline**: 2-3 weeks\n\n### manual\n- **estimated_gpu_cost**: ~$606 (202h × ~$3.00/hr H100 spot pricing)\n- **gpu_hours**: ~202 H100-hours total (range: 183-215 depending on per-step training speed). Breakdown with explicit wall-time × GPU arithmetic: Phase 0 pilot: ~5h (generation only, 1-2 GPUs); Phase 1 SFT cold start: ~5h (100 SFT steps); Phase 2 GRPO training: 2 runs × 500 steps × ~75 sec/step = 2 × (10.4 wall-hours × 8 GPUs) = ~166h; NLI overhead during training: ~8h; Phase 3 evaluation on 6 benchmarks: ~18h. Dense index building: ~0h (Search-R1 provides pre-built E5-base-v2 FAISS indexes). Per-step calibration: veRL GRPO benchmarks show 60-70 sec/step for Qwen2.5-7B on 8×A800 (ms-swift issue #3302); we estimate ~75 sec/step for Search-R1 on 8×H100, accounting for retrieval overhead partially offset by H100 throughput advantage. Contingency: if per-step exceeds 90 sec, reduce to 400 steps/run (above AutoRefine's 300-step convergence), giving 2 × (10.0 wall-hours × 8 GPUs) = ~160h for Phase 2, ~196h total.\n- **gpu_utilization**: ~40-50% effective utilization; GPUs idle during implementation, debugging, and analysis phases\n- **team**: 1 researcher with RL and retrieval experience\n- **timeline**: 10-12 days (10 days with 8×H100 and familiarity with Search-R1/veRL codebase; 12 days otherwise)\n\n"
}
```

---

### Runtime record

_source line 2 · 2026-05-16T01:48:41.500Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-16T01:48:41.500Z",
  "sessionId": "6959a7ca-d39c-4100-bbdf-21ac425702af"
}
```

---

## Round 1

37 recorded events

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
  "promptId": "04e8bf86-cce7-4413-9784-9f3d6381232b",
  "type": "user",
  "uuid": "7ccd1096-0eef-4dad-9aa7-ec09c15c5aa5",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6959a7ca-d39c-4100-bbdf-21ac425702af",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-16T01:48:41.515Z_

```json
{
  "parentUuid": "7ccd1096-0eef-4dad-9aa7-ec09c15c5aa5",
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
  "uuid": "760b99c6-873a-4ede-a6e8-2d23d0dedc54",
  "timestamp": "2026-05-16T01:48:41.515Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6959a7ca-d39c-4100-bbdf-21ac425702af",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-16T01:48:41.515Z_

```json
{
  "parentUuid": "760b99c6-873a-4ede-a6e8-2d23d0dedc54",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "5cd08f54-f122-429d-9fc7-93f8636f1ed9",
  "timestamp": "2026-05-16T01:48:41.515Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6959a7ca-d39c-4100-bbdf-21ac425702af",
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
  "leafUuid": "5cd08f54-f122-429d-9fc7-93f8636f1ed9",
  "sessionId": "6959a7ca-d39c-4100-bbdf-21ac425702af"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate dual-intent retrieval proposal",
  "sessionId": "6959a7ca-d39c-4100-bbdf-21ac425702af"
}
```

---

### Assistant

_source line 8 · 2026-05-16T01:49:17.276Z_

<details><summary>Logged reasoning block</summary>

```text
Let me carefully evaluate this proposal for EMNLP 2026 main conference. I need to assess the idea quality across Novelty, Significance, and Related Work, and provide a probability estimate.

Let me first understand the core idea:

The proposal suggests "Dual-Intent Retrieval" — classifying each retrieval call within a reasoning model's chain-of-thought as either "discovery-intent" (seeking new evidence) or "verification-intent" (seeking to confirm/refute a claim), then applying structurally different query construction and retrieval strategies for each type.

- Discovery queries → standard BM25


- Verification queries → hybrid BM25 + dense retrieval with NLI-based contrastive reranking

The key motivation comes from ReaLM-Retrieve's observation that 31% of retrieval calls are verification-type, but no existing system operationalizes this distinction. Now I'm considering whether a simpler baseline could work just as well — specifically, whether applying the hybrid retrieval pipeline uniformly across all queries would eliminate the need for intent classification altogether, since it's unclear that hybrid retrieval would actually hurt discovery performance.

I'm also thinking through whether the RL model could implicitly learn to formulate different queries for verification without explicit tokens, or whether AutoRefine's post-retrieval refinement step might achieve similar benefits more simply. The core assumptions here feel worth scrutinizing: the binary discovery/verification taxonomy might be too coarse, heuristic classification could introduce noise that undermines the differentiated pipelines, and the NLI reranking objective isn't obviously the right one. There's also the question of whether a well-trained RL model would naturally learn to seek disconfirming evidence when needed, rather than requiring explicit guidance.

The actual novelty seems to be in the explicit classification plus differentiated pipelines, but the individual components — varying retrieval intent, contrastive retrieval for verification, RL-based query learning — are all established ideas. I need to look at what specifically combines these in a new way.

On the "surprising finding" test, I suspect most reviewers would find this intuitive rather than surprising — differentiating query strategy by intent makes sense, but the real question is whether the complexity pays off empirically. The more compelling angle would be if the RL actually discovers interesting verification query patterns, though that's speculative.

Now I'm checking the recent literature to ground the novelty claims.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5cd08f54-f122-429d-9fc7-93f8636f1ed9",
  "isSidechain": false,
  "requestId": "req_011Cb5QYWdGCiMshGkohFX3J",
  "type": "assistant",
  "uuid": "340da0f8-de03-4bd3-a836-edd564f2b2a1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6959a7ca-d39c-4100-bbdf-21ac425702af",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NcxbsfSFBu1BBKrKdcQjbw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 28111,
      "cache_read_input_tokens": 0,
      "output_tokens": 1207,
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
          "output_tokens": 1207,
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

_source line 9 · 2026-05-16T01:49:17.381Z_

Let me first search for recent related work to verify the novelty claims before making my assessment.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "340da0f8-de03-4bd3-a836-edd564f2b2a1",
  "isSidechain": false,
  "requestId": "req_011Cb5QYWdGCiMshGkohFX3J",
  "type": "assistant",
  "uuid": "e6b83d6f-7723-460f-bb78-d6f4126c6cfc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6959a7ca-d39c-4100-bbdf-21ac425702af",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NcxbsfSFBu1BBKrKdcQjbw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 28111,
      "cache_read_input_tokens": 0,
      "output_tokens": 1207,
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
          "output_tokens": 1207,
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

_source line 10 · 2026-05-16T01:49:17.384Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01EpCbKwrrZL4oFPhqyDNhQD`</summary>

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
  "parentUuid": "e6b83d6f-7723-460f-bb78-d6f4126c6cfc",
  "isSidechain": false,
  "requestId": "req_011Cb5QYWdGCiMshGkohFX3J",
  "type": "assistant",
  "uuid": "dffd2801-7bd5-4ced-8331-1c8aba374542",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6959a7ca-d39c-4100-bbdf-21ac425702af",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NcxbsfSFBu1BBKrKdcQjbw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 28111,
      "cache_read_input_tokens": 0,
      "output_tokens": 1207,
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
          "output_tokens": 1207,
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

_source line 11 · 2026-05-16T01:49:17.395Z_

<details><summary>↩ Tool result · `toolu_01EpCbKwrrZL4oFPhqyDNhQD`</summary>

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
  "parentUuid": "dffd2801-7bd5-4ced-8331-1c8aba374542",
  "isSidechain": false,
  "promptId": "04e8bf86-cce7-4413-9784-9f3d6381232b",
  "type": "user",
  "uuid": "b222886f-6ab5-4caa-bf8f-89bc961b4cd1",
  "toolUseResult": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "dffd2801-7bd5-4ced-8331-1c8aba374542",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6959a7ca-d39c-4100-bbdf-21ac425702af",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-16T01:49:19.627Z_

Now let me search for the key related works to verify novelty claims.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b222886f-6ab5-4caa-bf8f-89bc961b4cd1",
  "isSidechain": false,
  "requestId": "req_011Cb5Qb9Nv1CHNtqe99vTuB",
  "type": "assistant",
  "uuid": "80c549eb-8e8e-4e08-85f6-bc18c4d32e5c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6959a7ca-d39c-4100-bbdf-21ac425702af",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019f1vHxZTmoqs8RCN9phozK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1733,
      "cache_read_input_tokens": 28111,
      "output_tokens": 192,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1733,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 192,
          "cache_read_input_tokens": 28111,
          "cache_creation_input_tokens": 1733,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1733
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

_source line 13 · 2026-05-16T01:49:20.165Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GeT5QbpAtaVPx9EZ2qk11C`</summary>

```json
{
  "query": "intent-differentiated retrieval reasoning RAG discovery verification 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "80c549eb-8e8e-4e08-85f6-bc18c4d32e5c",
  "isSidechain": false,
  "requestId": "req_011Cb5Qb9Nv1CHNtqe99vTuB",
  "type": "assistant",
  "uuid": "53a7fc7e-eaac-4f00-9bb9-c63b701b7783",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6959a7ca-d39c-4100-bbdf-21ac425702af",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019f1vHxZTmoqs8RCN9phozK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1733,
      "cache_read_input_tokens": 28111,
      "output_tokens": 192,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1733,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 192,
          "cache_read_input_tokens": 28111,
          "cache_creation_input_tokens": 1733,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1733
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

_source line 14 · 2026-05-16T01:49:21.103Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012AZ4LdZLqFfo9cLjG3m3En`</summary>

```json
{
  "query": "ReaLM-Retrieve adaptive retrieval reasoning models QueryGen verification retrievals 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "53a7fc7e-eaac-4f00-9bb9-c63b701b7783",
  "isSidechain": false,
  "requestId": "req_011Cb5Qb9Nv1CHNtqe99vTuB",
  "type": "assistant",
  "uuid": "75e9e2c5-f406-48a8-92cd-19182c80b4a7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6959a7ca-d39c-4100-bbdf-21ac425702af",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019f1vHxZTmoqs8RCN9phozK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1733,
      "cache_read_input_tokens": 28111,
      "output_tokens": 192,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1733,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 192,
          "cache_read_input_tokens": 28111,
          "cache_creation_input_tokens": 1733,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1733
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

_source line 15 · 2026-05-16T01:49:21.617Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01YQxYQ3vFwQcpy8EL6Am34U`</summary>

```json
{
  "query": "Veri-R1 GRPO claim verification iterative retrieval 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "75e9e2c5-f406-48a8-92cd-19182c80b4a7",
  "isSidechain": false,
  "requestId": "req_011Cb5Qb9Nv1CHNtqe99vTuB",
  "type": "assistant",
  "uuid": "b65dbefb-6bc0-4706-9a91-71221cac7575",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6959a7ca-d39c-4100-bbdf-21ac425702af",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019f1vHxZTmoqs8RCN9phozK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1733,
      "cache_read_input_tokens": 28111,
      "output_tokens": 192,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1733,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 192,
          "cache_read_input_tokens": 28111,
          "cache_creation_input_tokens": 1733,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1733
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

_source line 16 · 2026-05-16T01:49:28.389Z_

<details><summary>↩ Tool result · `toolu_01GeT5QbpAtaVPx9EZ2qk11C`</summary>

```text
Web search results for query: "intent-differentiated retrieval reasoning RAG discovery verification 2025 2026"

Links: [{"title":"[2505.09339] RAG-Enabled Intent Reasoning for Application-Network Interaction","url":"https://arxiv.org/abs/2505.09339"},{"title":"MIND-RAG: Multimodal Context-Aware and Intent-Aware ...","url":"https://openaccess.thecvf.com/content/ICCV2025W/MRR%202025/papers/Yu_MIND-RAG_Multimodal_Context-Aware_and_Intent-Aware_Retrieval-Augmented_Generation_for_Educational_Publications_ICCVW_2025_paper.pdf"},{"title":"Agentic RAG: a comprehensive guide to intelligent retrieval and reasoning","url":"https://www.kore.ai/blog/what-is-agentic-rag"},{"title":"RAG in 2026: Smarter Retrieval and Real-Time Responses","url":"https://dataforest.ai/blog/rag-in-2025-smarter-retrieval-and-real-time-responses"},{"title":"(PDF) The Evolution of Retrieval-Augmented Generation (RAG) in AI","url":"https://www.researchgate.net/publication/399423892_The_Evolution_of_Retrieval-Augmented_Generation_RAG_in_AI"},{"title":"Agentic Workflow for Reliable RAG: Reducing Hallucinations with Coordinated Reasoning | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-3-032-21625-0_8"},{"title":"[2603.09891] Overview of the TREC 2025 Retrieval Augmented Generation (RAG) Track","url":"https://arxiv.org/abs/2603.09891"},{"title":"From RAG to Context - A 2025 year-end review of RAG | RAGFlow","url":"https://ragflow.io/blog/rag-review-2025-from-rag-to-context"},{"title":"RAG in 2026: How Retrieval-Augmented Generation Works for Enterprise AI","url":"https://www.techment.com/blogs/rag-in-2026/"},{"title":"awesome-generative-ai-guide/research_updates/rag_research_table.md at main · aishwaryanr/awesome-generative-ai-guide","url":"https://github.com/aishwaryanr/awesome-generative-ai-guide/blob/main/research_updates/rag_research_table.md"}]

I found several relevant research papers and articles about RAG (Retrieval-Augmented Generation) systems with focus on intent, reasoning, discovery, and verification. Here are the key findings:

## Intent-Differentiated RAG Systems

Recent research proposes context-aware AI frameworks utilizing machine reasoning, retrieval augmented generation, and generative AI technologies to interpret intents from different applications. Intent predictions guide the selection of modality-specific retrieval databases, demonstrating how intent detection differentiates retrieval strategies.

## Agentic RAG and Reasoning

Unlike traditional RAG, which performs a single retrieval followed by generation, Agentic RAG uses autonomous AI agents to interpret the query, plan the workflow, retrieve information iteratively, refine context, validate results, and ensure the final answer is grounded, accurate, and enterprise-ready. The AI agent evaluates the intent behind the request, determines the complexity of the task, and identifies whether it requires a straightforward factual response or a multi-step reasoning operation.

## Verification and Fact-Checking

An enhanced Agentic RAG framework comes with a built-in Fact-Verification Feedback Loop where a dedicated agent checks each statement generated by the model against the retrieved evidence, and whenever the agent finds something inconsistent or lacking support, it automatically starts a correction cycle—refining the query and running the retrieval-generation process again until the answer reaches the required level of factual accuracy.

## 2025-2026 Evolution

As of 2025–2026, RAG has moved into a Modular and Agentic phase. By 2025–2026, systems have evolved far beyond simple text lookup to support multimodal RAG, which seamlessly searches and references images, structured code, audio transcripts, and even technical schematics.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "53a7fc7e-eaac-4f00-9bb9-c63b701b7783",
  "isSidechain": false,
  "promptId": "04e8bf86-cce7-4413-9784-9f3d6381232b",
  "type": "user",
  "uuid": "948d45c3-3c36-4b49-811f-042a542715b8",
  "toolUseResult": {
    "query": "intent-differentiated retrieval reasoning RAG discovery verification 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01XVhdoxy5ERqnnbtDEpocm9",
        "content": [
          {
            "title": "[2505.09339] RAG-Enabled Intent Reasoning for Application-Network Interaction",
            "url": "https://arxiv.org/abs/2505.09339"
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
            "title": "RAG in 2026: Smarter Retrieval and Real-Time Responses",
            "url": "https://dataforest.ai/blog/rag-in-2025-smarter-retrieval-and-real-time-responses"
          },
          {
            "title": "(PDF) The Evolution of Retrieval-Augmented Generation (RAG) in AI",
            "url": "https://www.researchgate.net/publication/399423892_The_Evolution_of_Retrieval-Augmented_Generation_RAG_in_AI"
          },
          {
            "title": "Agentic Workflow for Reliable RAG: Reducing Hallucinations with Coordinated Reasoning | Springer Nature Link",
            "url": "https://link.springer.com/chapter/10.1007/978-3-032-21625-0_8"
          },
          {
            "title": "[2603.09891] Overview of the TREC 2025 Retrieval Augmented Generation (RAG) Track",
            "url": "https://arxiv.org/abs/2603.09891"
          },
          {
            "title": "From RAG to Context - A 2025 year-end review of RAG | RAGFlow",
            "url": "https://ragflow.io/blog/rag-review-2025-from-rag-to-context"
          },
          {
            "title": "RAG in 2026: How Retrieval-Augmented Generation Works for Enterprise AI",
            "url": "https://www.techment.com/blogs/rag-in-2026/"
          },
          {
            "title": "awesome-generative-ai-guide/research_updates/rag_research_table.md at main · aishwaryanr/awesome-generative-ai-guide",
            "url": "https://github.com/aishwaryanr/awesome-generative-ai-guide/blob/main/research_updates/rag_research_table.md"
          }
        ]
      },
      "I found several relevant research papers and articles about RAG (Retrieval-Augmented Generation) systems with focus on intent, reasoning, discovery, and verification. Here are the key findings:\n\n## Intent-Differentiated RAG Systems\n\nRecent research proposes context-aware AI frameworks utilizing machine reasoning, retrieval augmented generation, and generative AI technologies to interpret intents from different applications. Intent predictions guide the selection of modality-specific retrieval databases, demonstrating how intent detection differentiates retrieval strategies.\n\n## Agentic RAG and Reasoning\n\nUnlike traditional RAG, which performs a single retrieval followed by generation, Agentic RAG uses autonomous AI agents to interpret the query, plan the workflow, retrieve information iteratively, refine context, validate results, and ensure the final answer is grounded, accurate, and enterprise-ready. The AI agent evaluates the intent behind the request, determines the complexity of the task, and identifies whether it requires a straightforward factual response or a multi-step reasoning operation.\n\n## Verification and Fact-Checking\n\nAn enhanced Agentic RAG framework comes with a built-in Fact-Verification Feedback Loop where a dedicated agent checks each statement generated by the model against the retrieved evidence, and whenever the agent finds something inconsistent or lacking support, it automatically starts a correction cycle—refining the query and running the retrieval-generation process again until the answer reaches the required level of factual accuracy.\n\n## 2025-2026 Evolution\n\nAs of 2025–2026, RAG has moved into a Modular and Agentic phase. By 2025–2026, systems have evolved far beyond simple text lookup to support multimodal RAG, which seamlessly searches and references images, structured code, audio transcripts, and even technical schematics."
    ],
    "durationSeconds": 8.219103401,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "53a7fc7e-eaac-4f00-9bb9-c63b701b7783",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6959a7ca-d39c-4100-bbdf-21ac425702af",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-16T01:49:28.435Z_

<details><summary>↩ Tool result · `toolu_01YQxYQ3vFwQcpy8EL6Am34U`</summary>

```text
Web search results for query: "Veri-R1 GRPO claim verification iterative retrieval 2025"

Links: [{"title":"Veri-R1: Toward Precise and Faithful Claim Verification via Online Reinforcement Learning","url":"https://arxiv.org/html/2510.01932v2"},{"title":"[2510.01932] Veri-R1: Toward Precise and Faithful Claim Verification via Online Reinforcement Learning","url":"https://arxiv.org/abs/2510.01932"},{"title":"Coordinating Search-Informed Reasoning and Reasoning-Guided Search in Claim Verification","url":"https://arxiv.org/html/2506.07528v1"},{"title":"GitHub - PeterGriffinJin/Search-R1: Search-R1: An Efficient, Scalable RL Training Framework for Reasoning & Search Engine Calling interleaved LLM based on veRL · GitHub","url":"https://github.com/PeterGriffinJin/Search-R1"},{"title":"FIRE: Fact-checking with Iterative Retrieval and Verification - ACL Anthology","url":"https://aclanthology.org/2025.findings-naacl.158/"},{"title":"ΥΥΥΥΥΥΥΥΥΥΥΥΥΥΥΥΥ VeriFastScore: Speeding up long-form factuality evaluation","url":"https://arxiv.org/html/2505.16973"},{"title":"VERI-SURE: A Contract-Aware Multi-Agent Framework with Temporal","url":"https://arxiv.org/pdf/2601.19747v1"},{"title":"GitHub - JiazhengZhang/AgentV-RL · GitHub","url":"https://github.com/JiazhengZhang/AgentV-RL"},{"title":"FIRE: Fact-checking with Iterative Retrieval and Verification | Request PDF","url":"https://www.researchgate.net/publication/392499024_FIRE_Fact-checking_with_Iterative_Retrieval_and_Verification"},{"title":"[2411.00784] FIRE: Fact-checking with Iterative Retrieval and Verification","url":"https://arxiv.org/abs/2411.00784"}]

Based on the search results, here's what I found about Veri-R1, GRPO, and claim verification with iterative retrieval:

## Veri-R1: Online Reinforcement Learning for Claim Verification

Veri-R1 is a novel training framework designed to enhance the online claim verification capability of LLMs within a unified pipeline. It is an online reinforcement learning (RL) framework that enables an LLM to interact with a search engine and to receive reward signals that explicitly shape its planning, retrieval, and reasoning behaviors.

## Key Technical Approach

During RL training, Veri-R1 employs the GRPO algorithm to preferentially learn from high-quality trajectories. During training rollouts, LLMs are required to iteratively search and reason across multiple turns before producing final answers. The model caps the number of search turns at three and requires the model to produce its answer once this budget is exhausted.

## Performance Results

Empirical results show that Veri-R1 improves joint accuracy by up to 30% and doubles the evidence score, often surpassing its larger-scale model counterparts. The results highlight the effectiveness of online RL for precise and faithful claim verification, providing an important foundation for future research.

## Related Context

The approach aligns with broader trends in using GRPO and reinforcement learning for search-augmented LLMs, as evidenced by related work on systems that combine iterative retrieval with verification for fact-checking tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b65dbefb-6bc0-4706-9a91-71221cac7575",
  "isSidechain": false,
  "promptId": "04e8bf86-cce7-4413-9784-9f3d6381232b",
  "type": "user",
  "uuid": "3d58b7a1-f435-449d-b191-9d0304527627",
  "toolUseResult": {
    "query": "Veri-R1 GRPO claim verification iterative retrieval 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_015g3gDiJv1RinovWxH4p6fB",
        "content": [
          {
            "title": "Veri-R1: Toward Precise and Faithful Claim Verification via Online Reinforcement Learning",
            "url": "https://arxiv.org/html/2510.01932v2"
          },
          {
            "title": "[2510.01932] Veri-R1: Toward Precise and Faithful Claim Verification via Online Reinforcement Learning",
            "url": "https://arxiv.org/abs/2510.01932"
          },
          {
            "title": "Coordinating Search-Informed Reasoning and Reasoning-Guided Search in Claim Verification",
            "url": "https://arxiv.org/html/2506.07528v1"
          },
          {
            "title": "GitHub - PeterGriffinJin/Search-R1: Search-R1: An Efficient, Scalable RL Training Framework for Reasoning & Search Engine Calling interleaved LLM based on veRL · GitHub",
            "url": "https://github.com/PeterGriffinJin/Search-R1"
          },
          {
            "title": "FIRE: Fact-checking with Iterative Retrieval and Verification - ACL Anthology",
            "url": "https://aclanthology.org/2025.findings-naacl.158/"
          },
          {
            "title": "ΥΥΥΥΥΥΥΥΥΥΥΥΥΥΥΥΥ VeriFastScore: Speeding up long-form factuality evaluation",
            "url": "https://arxiv.org/html/2505.16973"
          },
          {
            "title": "VERI-SURE: A Contract-Aware Multi-Agent Framework with Temporal",
            "url": "https://arxiv.org/pdf/2601.19747v1"
          },
          {
            "title": "GitHub - JiazhengZhang/AgentV-RL · GitHub",
            "url": "https://github.com/JiazhengZhang/AgentV-RL"
          },
          {
            "title": "FIRE: Fact-checking with Iterative Retrieval and Verification | Request PDF",
            "url": "https://www.researchgate.net/publication/392499024_FIRE_Fact-checking_with_Iterative_Retrieval_and_Verification"
          },
          {
            "title": "[2411.00784] FIRE: Fact-checking with Iterative Retrieval and Verification",
            "url": "https://arxiv.org/abs/2411.00784"
          }
        ]
      },
      "Based on the search results, here's what I found about Veri-R1, GRPO, and claim verification with iterative retrieval:\n\n## Veri-R1: Online Reinforcement Learning for Claim Verification\n\nVeri-R1 is a novel training framework designed to enhance the online claim verification capability of LLMs within a unified pipeline. It is an online reinforcement learning (RL) framework that enables an LLM to interact with a search engine and to receive reward signals that explicitly shape its planning, retrieval, and reasoning behaviors.\n\n## Key Technical Approach\n\nDuring RL training, Veri-R1 employs the GRPO algorithm to preferentially learn from high-quality trajectories. During training rollouts, LLMs are required to iteratively search and reason across multiple turns before producing final answers. The model caps the number of search turns at three and requires the model to produce its answer once this budget is exhausted.\n\n## Performance Results\n\nEmpirical results show that Veri-R1 improves joint accuracy by up to 30% and doubles the evidence score, often surpassing its larger-scale model counterparts. The results highlight the effectiveness of online RL for precise and faithful claim verification, providing an important foundation for future research.\n\n## Related Context\n\nThe approach aligns with broader trends in using GRPO and reinforcement learning for search-augmented LLMs, as evidenced by related work on systems that combine iterative retrieval with verification for fact-checking tasks."
    ],
    "durationSeconds": 6.81529666,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "b65dbefb-6bc0-4706-9a91-71221cac7575",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6959a7ca-d39c-4100-bbdf-21ac425702af",
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
  "leafUuid": "3d58b7a1-f435-449d-b191-9d0304527627",
  "sessionId": "6959a7ca-d39c-4100-bbdf-21ac425702af"
}
```

---

### Runtime record

_source line 19_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate dual-intent retrieval proposal",
  "sessionId": "6959a7ca-d39c-4100-bbdf-21ac425702af"
}
```

---

### Tool result

_source line 20 · 2026-05-16T01:49:29.085Z_

<details><summary>↩ Tool result · `toolu_012AZ4LdZLqFfo9cLjG3m3En`</summary>

```text
Web search results for query: "ReaLM-Retrieve adaptive retrieval reasoning models QueryGen verification retrievals 2026"

Links: [{"title":"When to Retrieve During Reasoning: Adaptive Retrieval for Large Reasoning Models","url":"https://arxiv.org/html/2604.26649"},{"title":"[2604.26649] When to Retrieve During Reasoning: Adaptive Retrieval for Large Reasoning Models","url":"https://arxiv.org/abs/2604.26649"},{"title":"REALM: retrieval-augmented language model pre-training","url":"https://dl.acm.org/doi/abs/10.5555/3524938.3525306"},{"title":"[2002.08909] REALM: Retrieval-Augmented Language Model Pre-Training","url":"https://arxiv.org/abs/2002.08909"},{"title":"[PDF] REALM: Retrieval-Augmented Language Model Pre-Training | Semantic Scholar","url":"https://www.semanticscholar.org/paper/REALM:-Retrieval-Augmented-Language-Model-Guu-Lee/832fff14d2ed50eb7969c4c4b976c35776548f56"},{"title":"REALM: Retrieval-Augmented Language Model Pre-Training","url":"https://github.com/google-research/language/blob/master/language/realm/README.md"},{"title":"REALM: Retrieval-Augmented Language Model Pre-Training | Request PDF","url":"https://www.researchgate.net/publication/339398913_REALM_Retrieval-Augmented_Language_Model_Pre-Training"},{"title":"REALM: Integrating Retrieval into Language Representation Models","url":"https://research.google/blog/realm-integrating-retrieval-into-language-representation-models/"},{"title":"[PDF] Improving Retrieval Augmented Language Model with Self-Reasoning | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Improving-Retrieval-Augmented-Language-Model-with-Xia-Zhou/d8cbe0bfcc9c2eb1714c0e5be18a6ecaf50ea7a5"},{"title":"What is Retrieval-Augmented Language Model pre-training? | Definition from TechTarget","url":"https://www.techtarget.com/searchenterpriseai/definition/Retrieval-Augmented-Language-Model-pre-training"}]

Based on the search results, I found information about ReaLM-Retrieve and related topics from 2026:

## ReaLM-Retrieve: Adaptive Retrieval for Large Reasoning Models

ReaLM-Retrieve achieves on average 10.1% absolute improvement in answer F1 over standard RAG while reducing retrieval calls by 47% compared to fixed-interval approaches like IRCoT. On the challenging MuSiQue benchmark requiring 2-4 hop reasoning, the method achieves 71.2% F1 with an average of only 1.8 retrieval calls per question.

## Key Performance Metrics

ReaLM-Retrieve improves retrieval quality itself, achieving 81.3% Recall@5 with consistently higher precision and MRR than fixed-interval baselines on supporting evidence, establishing new state-of-the-art efficiency-accuracy trade-offs for reasoning-intensive retrieval tasks.

## Identified Failure Modes

The research identified three primary failure modes in the system: QueryGen produces queries retrieving tangentially related content, often due to entity ambiguity (e.g., "Washington" as person vs. state). Additionally, required information is absent in the retrieval corpus, causing noise injection, particularly for recent events (post-2023) and specialized domains, and RSUS occasionally triggers retrieval during exploratory reasoning phases, disrupting productive chains by prematurely committing to hypotheses.

## Comparative Analysis

Compared to ReARTeR (Sun et al., 2025), step-level uncertainty detection provides finer-grained timing signals, yielding 4.6% higher F1 with 28% fewer calls.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "75e9e2c5-f406-48a8-92cd-19182c80b4a7",
  "isSidechain": false,
  "promptId": "04e8bf86-cce7-4413-9784-9f3d6381232b",
  "type": "user",
  "uuid": "546d7e80-9ab0-4600-af75-fb6ac6390852",
  "toolUseResult": {
    "query": "ReaLM-Retrieve adaptive retrieval reasoning models QueryGen verification retrievals 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01W3qs2pYCtBT77JknSvEF9u",
        "content": [
          {
            "title": "When to Retrieve During Reasoning: Adaptive Retrieval for Large Reasoning Models",
            "url": "https://arxiv.org/html/2604.26649"
          },
          {
            "title": "[2604.26649] When to Retrieve During Reasoning: Adaptive Retrieval for Large Reasoning Models",
            "url": "https://arxiv.org/abs/2604.26649"
          },
          {
            "title": "REALM: retrieval-augmented language model pre-training",
            "url": "https://dl.acm.org/doi/abs/10.5555/3524938.3525306"
          },
          {
            "title": "[2002.08909] REALM: Retrieval-Augmented Language Model Pre-Training",
            "url": "https://arxiv.org/abs/2002.08909"
          },
          {
            "title": "[PDF] REALM: Retrieval-Augmented Language Model Pre-Training | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/REALM:-Retrieval-Augmented-Language-Model-Guu-Lee/832fff14d2ed50eb7969c4c4b976c35776548f56"
          },
          {
            "title": "REALM: Retrieval-Augmented Language Model Pre-Training",
            "url": "https://github.com/google-research/language/blob/master/language/realm/README.md"
          },
          {
            "title": "REALM: Retrieval-Augmented Language Model Pre-Training | Request PDF",
            "url": "https://www.researchgate.net/publication/339398913_REALM_Retrieval-Augmented_Language_Model_Pre-Training"
          },
          {
            "title": "REALM: Integrating Retrieval into Language Representation Models",
            "url": "https://research.google/blog/realm-integrating-retrieval-into-language-representation-models/"
          },
          {
            "title": "[PDF] Improving Retrieval Augmented Language Model with Self-Reasoning | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/Improving-Retrieval-Augmented-Language-Model-with-Xia-Zhou/d8cbe0bfcc9c2eb1714c0e5be18a6ecaf50ea7a5"
          },
          {
            "title": "What is Retrieval-Augmented Language Model pre-training? | Definition from TechTarget",
            "url": "https://www.techtarget.com/searchenterpriseai/definition/Retrieval-Augmented-Language-Model-pre-training"
          }
        ]
      },
      "Based on the search results, I found information about ReaLM-Retrieve and related topics from 2026:\n\n## ReaLM-Retrieve: Adaptive Retrieval for Large Reasoning Models\n\nReaLM-Retrieve achieves on average 10.1% absolute improvement in answer F1 over standard RAG while reducing retrieval calls by 47% compared to fixed-interval approaches like IRCoT. On the challenging MuSiQue benchmark requiring 2-4 hop reasoning, the method achieves 71.2% F1 with an average of only 1.8 retrieval calls per question.\n\n## Key Performance Metrics\n\nReaLM-Retrieve improves retrieval quality itself, achieving 81.3% Recall@5 with consistently higher precision and MRR than fixed-interval baselines on supporting evidence, establishing new state-of-the-art efficiency-accuracy trade-offs for reasoning-intensive retrieval tasks.\n\n## Identified Failure Modes\n\nThe research identified three primary failure modes in the system: QueryGen produces queries retrieving tangentially related content, often due to entity ambiguity (e.g., \"Washington\" as person vs. state). Additionally, required information is absent in the retrieval corpus, causing noise injection, particularly for recent events (post-2023) and specialized domains, and RSUS occasionally triggers retrieval during exploratory reasoning phases, disrupting productive chains by prematurely committing to hypotheses.\n\n## Comparative Analysis\n\nCompared to ReARTeR (Sun et al., 2025), step-level uncertainty detection provides finer-grained timing signals, yielding 4.6% higher F1 with 28% fewer calls."
    ],
    "durationSeconds": 7.978580619000001,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "75e9e2c5-f406-48a8-92cd-19182c80b4a7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6959a7ca-d39c-4100-bbdf-21ac425702af",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-16T01:49:31.832Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GqzQDppqwDmH4tttNwWZN3`</summary>

```json
{
  "query": "contrastive query retrieval verification claim NLI reranking RAG 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "546d7e80-9ab0-4600-af75-fb6ac6390852",
  "isSidechain": false,
  "requestId": "req_011Cb5Qc1L13my7He8esaWWK",
  "type": "assistant",
  "uuid": "403d0ae0-0cc6-453a-bb85-56c2d9e82ef0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6959a7ca-d39c-4100-bbdf-21ac425702af",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013FKUJqbATVV9PcTQjKF7km",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 929,
      "cache_creation_input_tokens": 2306,
      "cache_read_input_tokens": 29844,
      "output_tokens": 180,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2306,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 929,
          "output_tokens": 180,
          "cache_read_input_tokens": 29844,
          "cache_creation_input_tokens": 2306,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2306
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

_source line 22 · 2026-05-16T01:49:32.371Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JttcZmtjCswZ3Zi3TerUwx`</summary>

```json
{
  "query": "AutoRefine Search-R1 refine step GRPO NeurIPS 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "403d0ae0-0cc6-453a-bb85-56c2d9e82ef0",
  "isSidechain": false,
  "requestId": "req_011Cb5Qc1L13my7He8esaWWK",
  "type": "assistant",
  "uuid": "9230e575-68e9-4e4e-9f41-1039834d445e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6959a7ca-d39c-4100-bbdf-21ac425702af",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013FKUJqbATVV9PcTQjKF7km",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 929,
      "cache_creation_input_tokens": 2306,
      "cache_read_input_tokens": 29844,
      "output_tokens": 180,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2306,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 929,
          "output_tokens": 180,
          "cache_read_input_tokens": 29844,
          "cache_creation_input_tokens": 2306,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2306
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

_source line 23 · 2026-05-16T01:49:33.099Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MuwEYGbpJbciT5nDmeTZcw`</summary>

```json
{
  "query": "retrieval intent classification query differentiation reasoning chain 2025 2026 NLP"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9230e575-68e9-4e4e-9f41-1039834d445e",
  "isSidechain": false,
  "requestId": "req_011Cb5Qc1L13my7He8esaWWK",
  "type": "assistant",
  "uuid": "9af37d0d-d337-446f-9d1d-ad04df1241ec",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6959a7ca-d39c-4100-bbdf-21ac425702af",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013FKUJqbATVV9PcTQjKF7km",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 929,
      "cache_creation_input_tokens": 2306,
      "cache_read_input_tokens": 29844,
      "output_tokens": 180,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2306,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 929,
          "output_tokens": 180,
          "cache_read_input_tokens": 29844,
          "cache_creation_input_tokens": 2306,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2306
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

_source line 24 · 2026-05-16T01:49:38.614Z_

<details><summary>↩ Tool result · `toolu_01GqzQDppqwDmH4tttNwWZN3`</summary>

```text
Web search results for query: "contrastive query retrieval verification claim NLI reranking RAG 2025 2026"

Links: [{"title":"DS@GT at CheckThat! 2025: Evaluating Context and Tokenization Strategies for Numerical Fact Verification","url":"https://arxiv.org/html/2507.06195"},{"title":"RankRAG: Unifying Context Ranking with Retrieval-Augmented Generation in LLMs","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/db93ccb6cf392f352570dd5af0a223d3-Paper-Conference.pdf"},{"title":"Contrastive Retrieval-Augmented Generation on Experience","url":"https://aclanthology.org/2025.findings-acl.1224.pdf"},{"title":"The Next Frontier of RAG: How Enterprise Knowledge Systems Will Evolve (2026-2030) - NStarX Inc.","url":"https://nstarxinc.com/blog/the-next-frontier-of-rag-how-enterprise-knowledge-systems-will-evolve-2026-2030/"},{"title":"Top 7 Rerankers for RAG","url":"https://www.analyticsvidhya.com/blog/2025/06/top-rerankers-for-rag/"},{"title":"A Review on Fact Extraction and Verification","url":"https://dl.acm.org/doi/fullHtml/10.1145/3485127"},{"title":"How Good are LLM-based Rerankers? An Empirical Analysis of","url":"https://arxiv.org/pdf/2508.16757"},{"title":"GitHub - liunian-Jay/Awesome-RAG: 💡 Awesome RAG: A resource of Retrieval-Augmented Generation (RAG) for LLMs, focusing on the development of technology.","url":"https://github.com/liunian-Jay/Awesome-RAG"},{"title":"Optimizing Retrieval for RAG via Reinforcement Learning Jiawei Zhou Lei Chen","url":"https://openreview.net/pdf/74b57081a9a2db071d310000acfd1692aa247047.pdf"},{"title":"RankRAG: Unifying Context Ranking with Retrieval-Augmented Generation in LLMs","url":"https://www.researchgate.net/publication/397197372_RankRAG_Unifying_Context_Ranking_with_Retrieval-Augmented_Generation_in_LLMs"}]

Based on the search results, here are relevant findings related to your query about contrastive query retrieval, verification, claim, NLI, reranking, and RAG in 2025-2026:

## Recent Research on These Topics

**Fact Verification and NLI Pipelines:**
A hybrid BM25 + transformer evidence retrieval-reranking pipeline has been plugged into a ModernBERT Natural Language Inference (NLI) core for numerical fact verification. Claim decomposition is also being employed to split the claim into separate parts and improve the retrieval stage, similar to query expansion.

**Contrastive Learning in RAG:**
Recent reranking models like Mixedbread's mxbai-rerank incorporate a three-stage reinforcement learning approach (GRPO, Contrastive Learning, Preference Learning). Additionally, reinforced contrastive learning training consists of on-policy retrieval, approximated LLM generation based on retrieved documents, and reinforced contrastive learning to optimize the retriever.

**RAG Evolution (2025-2026):**
Retrieval precision has improved by 15–30% through hybrid search and reranking, and there is a framework called RaCoT (Retrieval-aware Contrastive-of-Thought) that shifts contrastive thinking to the pre-retrieval stage.

The research landscape shows active development in combining contrastive learning, query reranking, NLI-based verification, and RAG systems through 2025-2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "403d0ae0-0cc6-453a-bb85-56c2d9e82ef0",
  "isSidechain": false,
  "promptId": "04e8bf86-cce7-4413-9784-9f3d6381232b",
  "type": "user",
  "uuid": "559fc6c1-98a9-43a9-a016-272833255426",
  "toolUseResult": {
    "query": "contrastive query retrieval verification claim NLI reranking RAG 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01URSyjGLC8m4oaWT5Zy9QN1",
        "content": [
          {
            "title": "DS@GT at CheckThat! 2025: Evaluating Context and Tokenization Strategies for Numerical Fact Verification",
            "url": "https://arxiv.org/html/2507.06195"
          },
          {
            "title": "RankRAG: Unifying Context Ranking with Retrieval-Augmented Generation in LLMs",
            "url": "https://proceedings.neurips.cc/paper_files/paper/2024/file/db93ccb6cf392f352570dd5af0a223d3-Paper-Conference.pdf"
          },
          {
            "title": "Contrastive Retrieval-Augmented Generation on Experience",
            "url": "https://aclanthology.org/2025.findings-acl.1224.pdf"
          },
          {
            "title": "The Next Frontier of RAG: How Enterprise Knowledge Systems Will Evolve (2026-2030) - NStarX Inc.",
            "url": "https://nstarxinc.com/blog/the-next-frontier-of-rag-how-enterprise-knowledge-systems-will-evolve-2026-2030/"
          },
          {
            "title": "Top 7 Rerankers for RAG",
            "url": "https://www.analyticsvidhya.com/blog/2025/06/top-rerankers-for-rag/"
          },
          {
            "title": "A Review on Fact Extraction and Verification",
            "url": "https://dl.acm.org/doi/fullHtml/10.1145/3485127"
          },
          {
            "title": "How Good are LLM-based Rerankers? An Empirical Analysis of",
            "url": "https://arxiv.org/pdf/2508.16757"
          },
          {
            "title": "GitHub - liunian-Jay/Awesome-RAG: 💡 Awesome RAG: A resource of Retrieval-Augmented Generation (RAG) for LLMs, focusing on the development of technology.",
            "url": "https://github.com/liunian-Jay/Awesome-RAG"
          },
          {
            "title": "Optimizing Retrieval for RAG via Reinforcement Learning Jiawei Zhou Lei Chen",
            "url": "https://openreview.net/pdf/74b57081a9a2db071d310000acfd1692aa247047.pdf"
          },
          {
            "title": "RankRAG: Unifying Context Ranking with Retrieval-Augmented Generation in LLMs",
            "url": "https://www.researchgate.net/publication/397197372_RankRAG_Unifying_Context_Ranking_with_Retrieval-Augmented_Generation_in_LLMs"
          }
        ]
      },
      "Based on the search results, here are relevant findings related to your query about contrastive query retrieval, verification, claim, NLI, reranking, and RAG in 2025-2026:\n\n## Recent Research on These Topics\n\n**Fact Verification and NLI Pipelines:**\nA hybrid BM25 + transformer evidence retrieval-reranking pipeline has been plugged into a ModernBERT Natural Language Inference (NLI) core for numerical fact verification. Claim decomposition is also being employed to split the claim into separate parts and improve the retrieval stage, similar to query expansion.\n\n**Contrastive Learning in RAG:**\nRecent reranking models like Mixedbread's mxbai-rerank incorporate a three-stage reinforcement learning approach (GRPO, Contrastive Learning, Preference Learning). Additionally, reinforced contrastive learning training consists of on-policy retrieval, approximated LLM generation based on retrieved documents, and reinforced contrastive learning to optimize the retriever.\n\n**RAG Evolution (2025-2026):**\nRetrieval precision has improved by 15–30% through hybrid search and reranking, and there is a framework called RaCoT (Retrieval-aware Contrastive-of-Thought) that shifts contrastive thinking to the pre-retrieval stage.\n\nThe research landscape shows active development in combining contrastive learning, query reranking, NLI-based verification, and RAG systems through 2025-2026."
    ],
    "durationSeconds": 6.775322263000001,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "403d0ae0-0cc6-453a-bb85-56c2d9e82ef0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6959a7ca-d39c-4100-bbdf-21ac425702af",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-16T01:49:39.978Z_

<details><summary>↩ Tool result · `toolu_01JttcZmtjCswZ3Zi3TerUwx`</summary>

```text
Web search results for query: "AutoRefine Search-R1 refine step GRPO NeurIPS 2025"

Links: [{"title":"GitHub - syr-cn/AutoRefine: [NeurIPS 2025 Poster] Search and Refine During Think: Facilitating Knowledge Refinement for Improved Retrieval-Augmented Reasoning","url":"https://github.com/syr-cn/AutoRefine"},{"title":"GitHub - PeterGriffinJin/Search-R1: Search-R1: An Efficient, Scalable RL Training Framework for Reasoning & Search Engine Calling interleaved LLM based on veRL · GitHub","url":"https://github.com/PeterGriffinJin/Search-R1"},{"title":"Search and Refine During Think: Autonomous Retrieval-Augmented Reasoning of LLMs","url":"https://arxiv.org/html/2505.11277v1"},{"title":"[2505.11277] Search and Refine During Think: Facilitating Knowledge Refinement for Improved Retrieval-Augmented Reasoning","url":"https://arxiv.org/abs/2505.11277"},{"title":"[2503.09516] Search-R1: Training LLMs to Reason and Leverage Search Engines with Reinforcement Learning","url":"https://arxiv.org/abs/2503.09516"},{"title":"Search-R1: Training LLMs to Reason and Leverage ...","url":"https://arxiv.org/pdf/2503.09516"},{"title":"NeurIPS Poster S-GRPO: Early Exit via Reinforcement Learning in Reasoning Models","url":"https://neurips.cc/virtual/2025/poster/115333"},{"title":"Group-in-Group Policy Optimization for LLM Agent Training Lang Feng1","url":"https://personal.ntu.edu.sg/boan/papers/NeurIPS25_GiGPO.pdf"},{"title":"Tree Search for LLM Agent Reinforcement Learning","url":"https://arxiv.org/pdf/2509.21240"},{"title":"GitHub - junfanz1/GRPO: Search-R1 fine-tunes LLMs to decide when to search and when to answer using reinforcement learning over multi-step trajectories. It employs Group Relative Policy Optimization (GRPO) for stable token-level updates without a critic. The model learns adaptive retrieval policies, dynamically integrating search results to construct context and improve r · GitHub","url":"https://github.com/junfanz1/GRPO"}]

Based on the search results, here's what I found about AutoRefine, Search-R1, the refine step, GRPO, and NeurIPS 2025:

## AutoRefine Overview

AutoRefine introduces explicit knowledge refinement steps between successive search calls, enabling the model to iteratively filter, distill, and organize evidence before generating an answer. An actor model generates diverse reasoning trajectories for a given question, including think, search, refine, and answer.

## The Refine Step

The refine step is a key innovation in AutoRefine. To investigate the effectiveness of knowledge refinement, the work specifically analyzes whether the refinement steps successfully distill critical information from retrieved documents by comparing the success rate of different actions: search, refine, and answer.

## GRPO Training

These trajectories are optimized using the GRPO algorithm, where the loss on retrieved documents is masked out. More specifically, tailored retrieval-specific rewards are incorporated alongside answer correctness rewards using group relative policy optimization.

## Performance Results

Experiments on single-hop and multi-hop QA benchmarks demonstrate that AutoRefine significantly outperforms existing approaches, particularly in complex, multi-hop reasoning scenarios, and detailed analysis shows that AutoRefine issues frequent, higher-quality searches and synthesizes evidence effectively.

## NeurIPS 2025 Status

AutoRefine is an NeurIPS 2025 contribution, with the arXiv paper titled "Search and Refine During Think: Autonomous Retrieval-Augmented Reasoning of LLMs" published on May 16, 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9230e575-68e9-4e4e-9f41-1039834d445e",
  "isSidechain": false,
  "promptId": "04e8bf86-cce7-4413-9784-9f3d6381232b",
  "type": "user",
  "uuid": "ddb49613-4e34-4955-a9f4-a3ad70411113",
  "toolUseResult": {
    "query": "AutoRefine Search-R1 refine step GRPO NeurIPS 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_0154z6hVpSoKdFrn8kNYV9yZ",
        "content": [
          {
            "title": "GitHub - syr-cn/AutoRefine: [NeurIPS 2025 Poster] Search and Refine During Think: Facilitating Knowledge Refinement for Improved Retrieval-Augmented Reasoning",
            "url": "https://github.com/syr-cn/AutoRefine"
          },
          {
            "title": "GitHub - PeterGriffinJin/Search-R1: Search-R1: An Efficient, Scalable RL Training Framework for Reasoning & Search Engine Calling interleaved LLM based on veRL · GitHub",
            "url": "https://github.com/PeterGriffinJin/Search-R1"
          },
          {
            "title": "Search and Refine During Think: Autonomous Retrieval-Augmented Reasoning of LLMs",
            "url": "https://arxiv.org/html/2505.11277v1"
          },
          {
            "title": "[2505.11277] Search and Refine During Think: Facilitating Knowledge Refinement for Improved Retrieval-Augmented Reasoning",
            "url": "https://arxiv.org/abs/2505.11277"
          },
          {
            "title": "[2503.09516] Search-R1: Training LLMs to Reason and Leverage Search Engines with Reinforcement Learning",
            "url": "https://arxiv.org/abs/2503.09516"
          },
          {
            "title": "Search-R1: Training LLMs to Reason and Leverage ...",
            "url": "https://arxiv.org/pdf/2503.09516"
          },
          {
            "title": "NeurIPS Poster S-GRPO: Early Exit via Reinforcement Learning in Reasoning Models",
            "url": "https://neurips.cc/virtual/2025/poster/115333"
          },
          {
            "title": "Group-in-Group Policy Optimization for LLM Agent Training Lang Feng1",
            "url": "https://personal.ntu.edu.sg/boan/papers/NeurIPS25_GiGPO.pdf"
          },
          {
            "title": "Tree Search for LLM Agent Reinforcement Learning",
            "url": "https://arxiv.org/pdf/2509.21240"
          },
          {
            "title": "GitHub - junfanz1/GRPO: Search-R1 fine-tunes LLMs to decide when to search and when to answer using reinforcement learning over multi-step trajectories. It employs Group Relative Policy Optimization (GRPO) for stable token-level updates without a critic. The model learns adaptive retrieval policies, dynamically integrating search results to construct context and improve r · GitHub",
            "url": "https://github.com/junfanz1/GRPO"
          }
        ]
      },
      "Based on the search results, here's what I found about AutoRefine, Search-R1, the refine step, GRPO, and NeurIPS 2025:\n\n## AutoRefine Overview\n\nAutoRefine introduces explicit knowledge refinement steps between successive search calls, enabling the model to iteratively filter, distill, and organize evidence before generating an answer. An actor model generates diverse reasoning trajectories for a given question, including think, search, refine, and answer.\n\n## The Refine Step\n\nThe refine step is a key innovation in AutoRefine. To investigate the effectiveness of knowledge refinement, the work specifically analyzes whether the refinement steps successfully distill critical information from retrieved documents by comparing the success rate of different actions: search, refine, and answer.\n\n## GRPO Training\n\nThese trajectories are optimized using the GRPO algorithm, where the loss on retrieved documents is masked out. More specifically, tailored retrieval-specific rewards are incorporated alongside answer correctness rewards using group relative policy optimization.\n\n## Performance Results\n\nExperiments on single-hop and multi-hop QA benchmarks demonstrate that AutoRefine significantly outperforms existing approaches, particularly in complex, multi-hop reasoning scenarios, and detailed analysis shows that AutoRefine issues frequent, higher-quality searches and synthesizes evidence effectively.\n\n## NeurIPS 2025 Status\n\nAutoRefine is an NeurIPS 2025 contribution, with the arXiv paper titled \"Search and Refine During Think: Autonomous Retrieval-Augmented Reasoning of LLMs\" published on May 16, 2025."
    ],
    "durationSeconds": 7.603151394,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "9230e575-68e9-4e4e-9f41-1039834d445e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6959a7ca-d39c-4100-bbdf-21ac425702af",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-16T01:49:40.390Z_

<details><summary>↩ Tool result · `toolu_01MuwEYGbpJbciT5nDmeTZcw`</summary>

```text
Web search results for query: "retrieval intent classification query differentiation reasoning chain 2025 2026 NLP"

Links: [{"title":"Intent Classification: 2026 Techniques for NLP Models | Label Your Data","url":"https://labelyourdata.com/articles/machine-learning/intent-classification"},{"title":"CoT-RAG: Integrating Chain of Thought and Retrieval- ...","url":"https://aclanthology.org/2025.findings-emnlp.168.pdf"},{"title":"In a Few Words: Comparing Weak Supervision and LLMs for Short Query Intent Classification","url":"https://arxiv.org/html/2504.21398v1"},{"title":"Query Expansion in Enhancing Retrieval-Augmented Generation (RAG) | by Sahin Ahmed(Data Scientist/MLE) | Medium","url":"https://medium.com/@sahin.samia/query-expansion-in-enhancing-retrieval-augmented-generation-rag-d41153317383"},{"title":"Accepted Findings Papers - EMNLP 2025","url":"https://2025.emnlp.org/program/find_papers/"},{"title":"Query rewriting strategies for LLMs & search engines - Elasticsearch Labs","url":"https://www.elastic.co/search-labs/blog/query-rewriting-llm-search-improve"},{"title":"1 Large Language Models for Information Retrieval: A Survey","url":"http://playbigdata.ruc.edu.cn/dou/publication/2025_Survey_LLM4IR.pdf"},{"title":"Day 9 - Query Expansion and Rewriting: Making User Intent Crystal Clear","url":"https://www.linkedin.com/pulse/day-9-query-expansion-rewriting-making-user-intent-crystal-marques-ytixe"},{"title":"Retrieval Augmented Generation (RAG) for LLMs | Prompt Engineering Guide&lt;!-- -->","url":"https://www.promptingguide.ai/research/rag"},{"title":"dblp: NLPCC 2025 - Part I","url":"https://dblp.org/db/conf/nlpcc/nlpcc2025-1.html"}]

I found several relevant results on retrieval, intent classification, query differentiation, reasoning chains, and NLP for 2025-2026. Here's a summary of what the search uncovered:

## Intent Classification Approaches (2025-2026)

There are four main approaches to intent classification: rule-based systems relying on predefined patterns or keyword matching, classical machine learning models such as SVMs or Random Forests using engineered features like n-grams or TF-IDF, fine-tuned transformers including BERT and RoBERTa leveraging deep contextual embeddings, and LLM-based prompting using models like GPT or Claude to classify intents with zero- or few-shot examples without fine-tuning.

## Reasoning Chains and Query Differentiation

CoT-RAG integrates Chain of Thought and Retrieval-Augmented Generation to enhance reasoning in Large Language Models. A strategy proposed by Sun et al. involves getting clues first (such as keywords, semantic clues), then perform reasoning and then make a decision about the correct class.

## Retrieval-Augmented Generation (RAG) with Intent

Retrieval-Augmented Generation (RAG) combines a retriever (to fetch relevant data) and a generator (to answer), and can help improve classification when intent depends on external context (e.g., past interactions). Query expansion addresses retrieval challenges by enhancing user queries with additional relevant terms, improving retrieval precision and recall, and ultimately boosting the quality of generated outputs.

The search results reveal active ongoing research in NLP during 2025-2026 combining these areas, particularly through frameworks like CoT-RAG and various query expansion techniques.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9af37d0d-d337-446f-9d1d-ad04df1241ec",
  "isSidechain": false,
  "promptId": "04e8bf86-cce7-4413-9784-9f3d6381232b",
  "type": "user",
  "uuid": "e373fa3c-0ee7-439d-b122-2364274b0f3b",
  "toolUseResult": {
    "query": "retrieval intent classification query differentiation reasoning chain 2025 2026 NLP",
    "results": [
      {
        "tool_use_id": "srvtoolu_01G55PLVY8k78JGuPJoD5srC",
        "content": [
          {
            "title": "Intent Classification: 2026 Techniques for NLP Models | Label Your Data",
            "url": "https://labelyourdata.com/articles/machine-learning/intent-classification"
          },
          {
            "title": "CoT-RAG: Integrating Chain of Thought and Retrieval- ...",
            "url": "https://aclanthology.org/2025.findings-emnlp.168.pdf"
          },
          {
            "title": "In a Few Words: Comparing Weak Supervision and LLMs for Short Query Intent Classification",
            "url": "https://arxiv.org/html/2504.21398v1"
          },
          {
            "title": "Query Expansion in Enhancing Retrieval-Augmented Generation (RAG) | by Sahin Ahmed(Data Scientist/MLE) | Medium",
            "url": "https://medium.com/@sahin.samia/query-expansion-in-enhancing-retrieval-augmented-generation-rag-d41153317383"
          },
          {
            "title": "Accepted Findings Papers - EMNLP 2025",
            "url": "https://2025.emnlp.org/program/find_papers/"
          },
          {
            "title": "Query rewriting strategies for LLMs & search engines - Elasticsearch Labs",
            "url": "https://www.elastic.co/search-labs/blog/query-rewriting-llm-search-improve"
          },
          {
            "title": "1 Large Language Models for Information Retrieval: A Survey",
            "url": "http://playbigdata.ruc.edu.cn/dou/publication/2025_Survey_LLM4IR.pdf"
          },
          {
            "title": "Day 9 - Query Expansion and Rewriting: Making User Intent Crystal Clear",
            "url": "https://www.linkedin.com/pulse/day-9-query-expansion-rewriting-making-user-intent-crystal-marques-ytixe"
          },
          {
            "title": "Retrieval Augmented Generation (RAG) for LLMs | Prompt Engineering Guide&lt;!-- -->",
            "url": "https://www.promptingguide.ai/research/rag"
          },
          {
            "title": "dblp: NLPCC 2025 - Part I",
            "url": "https://dblp.org/db/conf/nlpcc/nlpcc2025-1.html"
          }
        ]
      },
      "I found several relevant results on retrieval, intent classification, query differentiation, reasoning chains, and NLP for 2025-2026. Here's a summary of what the search uncovered:\n\n## Intent Classification Approaches (2025-2026)\n\nThere are four main approaches to intent classification: rule-based systems relying on predefined patterns or keyword matching, classical machine learning models such as SVMs or Random Forests using engineered features like n-grams or TF-IDF, fine-tuned transformers including BERT and RoBERTa leveraging deep contextual embeddings, and LLM-based prompting using models like GPT or Claude to classify intents with zero- or few-shot examples without fine-tuning.\n\n## Reasoning Chains and Query Differentiation\n\nCoT-RAG integrates Chain of Thought and Retrieval-Augmented Generation to enhance reasoning in Large Language Models. A strategy proposed by Sun et al. involves getting clues first (such as keywords, semantic clues), then perform reasoning and then make a decision about the correct class.\n\n## Retrieval-Augmented Generation (RAG) with Intent\n\nRetrieval-Augmented Generation (RAG) combines a retriever (to fetch relevant data) and a generator (to answer), and can help improve classification when intent depends on external context (e.g., past interactions). Query expansion addresses retrieval challenges by enhancing user queries with additional relevant terms, improving retrieval precision and recall, and ultimately boosting the quality of generated outputs.\n\nThe search results reveal active ongoing research in NLP during 2025-2026 combining these areas, particularly through frameworks like CoT-RAG and various query expansion techniques."
    ],
    "durationSeconds": 7.2884298400000045,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "9af37d0d-d337-446f-9d1d-ad04df1241ec",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6959a7ca-d39c-4100-bbdf-21ac425702af",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 27_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Dual-Intent Retrieval: Intent-Differentiated Query Formulation for Reasoning-Augmented RAG  **状态**: 待审阅   **级别**…",
  "leafUuid": "e373fa3c-0ee7-439d-b122-2364274b0f3b",
  "sessionId": "6959a7ca-d39c-4100-bbdf-21ac425702af"
}
```

---

### Runtime record

_source line 28_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate dual-intent retrieval proposal",
  "sessionId": "6959a7ca-d39c-4100-bbdf-21ac425702af"
}
```

---

### Tool call

_source line 29 · 2026-05-16T01:49:43.867Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01S9kPb991hu7dtrHHYaxgxo`</summary>

```json
{
  "query": "\"dual intent\" OR \"intent-aware\" retrieval query formulation reasoning augmented generation differentiated 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e373fa3c-0ee7-439d-b122-2364274b0f3b",
  "isSidechain": false,
  "requestId": "req_011Cb5QcqfrXguKeCQ6ZBbjN",
  "type": "assistant",
  "uuid": "11503758-7189-4bb0-af9e-cd24019cfcb2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6959a7ca-d39c-4100-bbdf-21ac425702af",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01REArwbW9pKMkCaggUfwEs3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4092,
      "cache_read_input_tokens": 32150,
      "output_tokens": 128,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4092,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 128,
          "cache_read_input_tokens": 32150,
          "cache_creation_input_tokens": 4092,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4092
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

_source line 30 · 2026-05-16T01:49:44.754Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011uyyJGZWnzKie1my3kUzsc`</summary>

```json
{
  "query": "HARIS claim verification hierarchical agent search reasoning GRPO 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "11503758-7189-4bb0-af9e-cd24019cfcb2",
  "isSidechain": false,
  "requestId": "req_011Cb5QcqfrXguKeCQ6ZBbjN",
  "type": "assistant",
  "uuid": "26a0b080-316e-43c5-a1ee-ecf4df2e56e0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6959a7ca-d39c-4100-bbdf-21ac425702af",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01REArwbW9pKMkCaggUfwEs3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4092,
      "cache_read_input_tokens": 32150,
      "output_tokens": 128,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4092,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 128,
          "cache_read_input_tokens": 32150,
          "cache_creation_input_tokens": 4092,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4092
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

_source line 31 · 2026-05-16T01:49:51.029Z_

<details><summary>↩ Tool result · `toolu_011uyyJGZWnzKie1my3kUzsc`</summary>

```text
Web search results for query: "HARIS claim verification hierarchical agent search reasoning GRPO 2025"

Links: [{"title":"Coordinating Search-Informed Reasoning and Reasoning-Guided Search in Claim Verification","url":"https://arxiv.org/html/2506.07528v1"},{"title":"[2506.07528] Coordinating Search-Informed Reasoning and Reasoning-Guided Search in Claim Verification","url":"https://arxiv.org/abs/2506.07528"},{"title":"(PDF) Coordinating Search-Informed Reasoning and Reasoning-Guided Search in Claim Verification","url":"https://www.researchgate.net/publication/392529941_Coordinating_Search-Informed_Reasoning_and_Reasoning-Guided_Search_in_Claim_Verification"},{"title":"Example of HARIS's reasoning agent rollout. The reasoning and search... | Download Scientific Diagram","url":"https://www.researchgate.net/figure/Example-of-HARISs-reasoning-agent-rollout-The-reasoning-and-search-agents-coordinate_fig2_392529941"},{"title":"HiPRAG: Hierarchical Process Rewards for Efficient Agentic Retrieval Augmented Generation","url":"https://arxiv.org/html/2510.07794"},{"title":"Hierarchical Agentic RAG","url":"https://www.emergentmind.com/topics/hierarchical-agentic-rag"},{"title":"How to Train a Leader: Hierarchical Reasoning in Multi-Agent LLMs","url":"https://arxiv.org/pdf/2507.08960"},{"title":"ARISE: Agent Reasoning with Intrinsic Skill Evolution in Hierarchical Reinforcement Learning","url":"https://arxiv.org/html/2603.16060"},{"title":"Multi-Agent Deep Research: Training Multi-Agent Systems with M-GRPO","url":"https://arxiv.org/html/2511.13288v2"},{"title":"GitHub - blacksnail789521/Agentic-RL-Training-Recipes: Training Recipes for Agentic Reinforcement Learning in LLMs: A Survey · GitHub","url":"https://github.com/blacksnail789521/Agentic-RL-Training-Recipes"}]

Based on the search results, I found comprehensive information about HARIS and its approach to claim verification. Here's what I found:

## HARIS: Hierarchical Agent Reasoning and Information Search

HARIS is a hierarchical agent framework designed for complex multi-hop claim verification, explicitly modeling the coordinated process of reasoning-driven searching and search-informed reasoning.

### Architecture

HARIS consists of a high-level reasoning agent that focuses on constructing the main verification chain, generating factual questions when more information is needed, and a low-level search agent that iteratively retrieves more information, refining its search based on intermediate findings.

Specifically, the high-level reasoning agent in HARIS constructs the main claim verification chain, coordinating multi-step reasoning and generating factual questions for the search agent when additional information is needed.

### Training Approach

HARIS is trained end-to-end via Group Relative Policy Optimization (GRPO) using outcome-based rewards, directly optimizing task performance without intermediate supervision.

### Performance

HARIS demonstrates strong performance on two challenging benchmarks, EX-FEVER and HOVER, validating its effectiveness in tackling multi-hop claim verification.

The paper, published in June 2025, addresses the challenge that conventional approaches often overlook the dynamic interplay between reasoning and information retrieval, which can be critical for accurate multi-hop verification.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "26a0b080-316e-43c5-a1ee-ecf4df2e56e0",
  "isSidechain": false,
  "promptId": "04e8bf86-cce7-4413-9784-9f3d6381232b",
  "type": "user",
  "uuid": "92021075-3896-4151-968e-0787fd86c705",
  "toolUseResult": {
    "query": "HARIS claim verification hierarchical agent search reasoning GRPO 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01YUsqyHaTi9HTkqsP1y5BGN",
        "content": [
          {
            "title": "Coordinating Search-Informed Reasoning and Reasoning-Guided Search in Claim Verification",
            "url": "https://arxiv.org/html/2506.07528v1"
          },
          {
            "title": "[2506.07528] Coordinating Search-Informed Reasoning and Reasoning-Guided Search in Claim Verification",
            "url": "https://arxiv.org/abs/2506.07528"
          },
          {
            "title": "(PDF) Coordinating Search-Informed Reasoning and Reasoning-Guided Search in Claim Verification",
            "url": "https://www.researchgate.net/publication/392529941_Coordinating_Search-Informed_Reasoning_and_Reasoning-Guided_Search_in_Claim_Verification"
          },
          {
            "title": "Example of HARIS's reasoning agent rollout. The reasoning and search... | Download Scientific Diagram",
            "url": "https://www.researchgate.net/figure/Example-of-HARISs-reasoning-agent-rollout-The-reasoning-and-search-agents-coordinate_fig2_392529941"
          },
          {
            "title": "HiPRAG: Hierarchical Process Rewards for Efficient Agentic Retrieval Augmented Generation",
            "url": "https://arxiv.org/html/2510.07794"
          },
          {
            "title": "Hierarchical Agentic RAG",
            "url": "https://www.emergentmind.com/topics/hierarchical-agentic-rag"
          },
          {
            "title": "How to Train a Leader: Hierarchical Reasoning in Multi-Agent LLMs",
            "url": "https://arxiv.org/pdf/2507.08960"
          },
          {
            "title": "ARISE: Agent Reasoning with Intrinsic Skill Evolution in Hierarchical Reinforcement Learning",
            "url": "https://arxiv.org/html/2603.16060"
          },
          {
            "title": "Multi-Agent Deep Research: Training Multi-Agent Systems with M-GRPO",
            "url": "https://arxiv.org/html/2511.13288v2"
          },
          {
            "title": "GitHub - blacksnail789521/Agentic-RL-Training-Recipes: Training Recipes for Agentic Reinforcement Learning in LLMs: A Survey · GitHub",
            "url": "https://github.com/blacksnail789521/Agentic-RL-Training-Recipes"
          }
        ]
      },
      "Based on the search results, I found comprehensive information about HARIS and its approach to claim verification. Here's what I found:\n\n## HARIS: Hierarchical Agent Reasoning and Information Search\n\nHARIS is a hierarchical agent framework designed for complex multi-hop claim verification, explicitly modeling the coordinated process of reasoning-driven searching and search-informed reasoning.\n\n### Architecture\n\nHARIS consists of a high-level reasoning agent that focuses on constructing the main verification chain, generating factual questions when more information is needed, and a low-level search agent that iteratively retrieves more information, refining its search based on intermediate findings.\n\nSpecifically, the high-level reasoning agent in HARIS constructs the main claim verification chain, coordinating multi-step reasoning and generating factual questions for the search agent when additional information is needed.\n\n### Training Approach\n\nHARIS is trained end-to-end via Group Relative Policy Optimization (GRPO) using outcome-based rewards, directly optimizing task performance without intermediate supervision.\n\n### Performance\n\nHARIS demonstrates strong performance on two challenging benchmarks, EX-FEVER and HOVER, validating its effectiveness in tackling multi-hop claim verification.\n\nThe paper, published in June 2025, addresses the challenge that conventional approaches often overlook the dynamic interplay between reasoning and information retrieval, which can be critical for accurate multi-hop verification."
    ],
    "durationSeconds": 6.26989400700001,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "26a0b080-316e-43c5-a1ee-ecf4df2e56e0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6959a7ca-d39c-4100-bbdf-21ac425702af",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-16T01:49:51.812Z_

<details><summary>↩ Tool result · `toolu_01S9kPb991hu7dtrHHYaxgxo`</summary>

```text
Web search results for query: ""dual intent" OR "intent-aware" retrieval query formulation reasoning augmented generation differentiated 2025 2026"

Links: [{"title":"Retrieval-Augmented Generation: A Comprehensive Survey of Architectures, Enhancements, and Robustness Frontiers","url":"https://arxiv.org/html/2506.00054v1"},{"title":"MIND-RAG: Multimodal Context-Aware and Intent-Aware ...","url":"https://openaccess.thecvf.com/content/ICCV2025W/MRR%202025/papers/Yu_MIND-RAG_Multimodal_Context-Aware_and_Intent-Aware_Retrieval-Augmented_Generation_for_Educational_Publications_ICCVW_2025_paper.pdf"},{"title":"RAG+: Enhancing Retrieval-Augmented Generation with Application-Aware Reasoning","url":"https://arxiv.org/html/2506.11555v4"},{"title":"KA-RAG: Integrating Knowledge Graphs and Agentic Retrieval-Augmented Generation for an Intelligent Educational Question-Answering Model","url":"https://www.mdpi.com/2076-3417/15/23/12547"},{"title":"CRP-RAG: A Retrieval-Augmented Generation Framework for Supporting Complex Logical Reasoning and Knowledge Planning","url":"https://www.mdpi.com/2079-9292/14/1/47"},{"title":"Retrieval Augmented Generation (RAG) for Fintech: Agentic Design and Evaluation","url":"https://arxiv.org/html/2510.25518v1"},{"title":"A Survey on Retrieval And Structuring Augmented Generation","url":"https://arxiv.org/pdf/2509.10697"},{"title":"Uncertainty Quantification for Retrieval-Augmented Reasoning","url":"https://arxiv.org/html/2510.11483v1"},{"title":"1 Retrieval-Augmented Generation for Large Language Models: A Survey","url":"https://www.rivista.ai/wp-content/uploads/2025/09/2312.10997v5.pdf"},{"title":"Reasoning in Large Language Models: A Survey[v1] | Preprints.org","url":"https://www.preprints.org/manuscript/202510.1024/v1/download"}]

Based on the search results, here are the key findings related to dual intent, intent-aware retrieval, query formulation, reasoning-augmented generation, and differentiated approaches in 2025-2026:

## Intent-Aware Retrieval Systems

Limited retrieval performance stems from the system's inability to fully model user intent, particularly in queries that implicitly demand multimodal information or domain-specific knowledge. To address this, intent predictions guide the selection of modality-specific retrieval databases in systems like MIND-RAG (2025).

## Query Formulation and Reasoning

Recent approaches distinguish between knowledge retrieval and knowledge application. Existing RAG methods often focus on lexical or semantic similarity when retrieving knowledge, paying little attention to how the retrieved content should be applied in downstream tasks. The RAG+ framework (2025) addresses this gap by decomposing reasoning tasks into smaller steps and retrieving relevant knowledge for each substep.

## Differentiated Approaches (2025-2026)

Several differentiated methodologies have emerged:

1. **Intent Classification**: Intent Classifier determines whether the user input requires retrieval, which involves fetching new context from the knowledge base, or summary, which compresses existing conversational history.

2. **Reasoning-Guided Knowledge Planning**: CRP-RAG guides knowledge retrieval, evaluation, and reasoning strategy formulation based on reasoning logic, aligning relevant knowledge with the reasoning process to ensure the effective support of the reasoning process.

3. **Dual-Pathway Retrieval**: The Dual-Pathway KG-RAG framework combines structured retrieval from knowledge graphs with unstructured corpus retrieval in parallel, enhancing factual consistency and reducing hallucinations by 18% in biomedical QA tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "11503758-7189-4bb0-af9e-cd24019cfcb2",
  "isSidechain": false,
  "promptId": "04e8bf86-cce7-4413-9784-9f3d6381232b",
  "type": "user",
  "uuid": "7d04e40f-e3f6-4deb-be32-53e64a7b4cb1",
  "toolUseResult": {
    "query": "\"dual intent\" OR \"intent-aware\" retrieval query formulation reasoning augmented generation differentiated 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_016CqJfBfKbfuHJ3pr14HxXe",
        "content": [
          {
            "title": "Retrieval-Augmented Generation: A Comprehensive Survey of Architectures, Enhancements, and Robustness Frontiers",
            "url": "https://arxiv.org/html/2506.00054v1"
          },
          {
            "title": "MIND-RAG: Multimodal Context-Aware and Intent-Aware ...",
            "url": "https://openaccess.thecvf.com/content/ICCV2025W/MRR%202025/papers/Yu_MIND-RAG_Multimodal_Context-Aware_and_Intent-Aware_Retrieval-Augmented_Generation_for_Educational_Publications_ICCVW_2025_paper.pdf"
          },
          {
            "title": "RAG+: Enhancing Retrieval-Augmented Generation with Application-Aware Reasoning",
            "url": "https://arxiv.org/html/2506.11555v4"
          },
          {
            "title": "KA-RAG: Integrating Knowledge Graphs and Agentic Retrieval-Augmented Generation for an Intelligent Educational Question-Answering Model",
            "url": "https://www.mdpi.com/2076-3417/15/23/12547"
          },
          {
            "title": "CRP-RAG: A Retrieval-Augmented Generation Framework for Supporting Complex Logical Reasoning and Knowledge Planning",
            "url": "https://www.mdpi.com/2079-9292/14/1/47"
          },
          {
            "title": "Retrieval Augmented Generation (RAG) for Fintech: Agentic Design and Evaluation",
            "url": "https://arxiv.org/html/2510.25518v1"
          },
          {
            "title": "A Survey on Retrieval And Structuring Augmented Generation",
            "url": "https://arxiv.org/pdf/2509.10697"
          },
          {
            "title": "Uncertainty Quantification for Retrieval-Augmented Reasoning",
            "url": "https://arxiv.org/html/2510.11483v1"
          },
          {
            "title": "1 Retrieval-Augmented Generation for Large Language Models: A Survey",
            "url": "https://www.rivista.ai/wp-content/uploads/2025/09/2312.10997v5.pdf"
          },
          {
            "title": "Reasoning in Large Language Models: A Survey[v1] | Preprints.org",
            "url": "https://www.preprints.org/manuscript/202510.1024/v1/download"
          }
        ]
      },
      "Based on the search results, here are the key findings related to dual intent, intent-aware retrieval, query formulation, reasoning-augmented generation, and differentiated approaches in 2025-2026:\n\n## Intent-Aware Retrieval Systems\n\nLimited retrieval performance stems from the system's inability to fully model user intent, particularly in queries that implicitly demand multimodal information or domain-specific knowledge. To address this, intent predictions guide the selection of modality-specific retrieval databases in systems like MIND-RAG (2025).\n\n## Query Formulation and Reasoning\n\nRecent approaches distinguish between knowledge retrieval and knowledge application. Existing RAG methods often focus on lexical or semantic similarity when retrieving knowledge, paying little attention to how the retrieved content should be applied in downstream tasks. The RAG+ framework (2025) addresses this gap by decomposing reasoning tasks into smaller steps and retrieving relevant knowledge for each substep.\n\n## Differentiated Approaches (2025-2026)\n\nSeveral differentiated methodologies have emerged:\n\n1. **Intent Classification**: Intent Classifier determines whether the user input requires retrieval, which involves fetching new context from the knowledge base, or summary, which compresses existing conversational history.\n\n2. **Reasoning-Guided Knowledge Planning**: CRP-RAG guides knowledge retrieval, evaluation, and reasoning strategy formulation based on reasoning logic, aligning relevant knowledge with the reasoning process to ensure the effective support of the reasoning process.\n\n3. **Dual-Pathway Retrieval**: The Dual-Pathway KG-RAG framework combines structured retrieval from knowledge graphs with unstructured corpus retrieval in parallel, enhancing factual consistency and reducing hallucinations by 18% in biomedical QA tasks."
    ],
    "durationSeconds": 7.940528586,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "11503758-7189-4bb0-af9e-cd24019cfcb2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6959a7ca-d39c-4100-bbdf-21ac425702af",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 33 · 2026-05-16T01:49:51.818Z_

```json
{
  "parentUuid": "7d04e40f-e3f6-4deb-be32-53e64a7b4cb1",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "b6d414d8-b993-4d95-a219-63af503937d0",
  "timestamp": "2026-05-16T01:49:51.818Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6959a7ca-d39c-4100-bbdf-21ac425702af",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 34 · 2026-05-16T01:50:39.993Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me synthesize my findings and assess this proposal carefully.

## Core Idea Assessment

The core idea is: "Explicitly classify each retrieval call within a reasoning chain as discovery-intent or verification-intent, then apply structurally different query construction and retrieval strategies for each."

### Trivial Alternative Check

The most threatening trivial alternative is: **Just use hybrid BM25+dense retrieval with NLI reranking for ALL queries, without intent classification.** If hybrid retrieval with NLI reranking is better than BM25 alone, why not use it for everything? The proposal argues BM25 is "appropriate" for discovery queries because they're "keyword-rich," but this doesn't mean hybrid would be worse. 

This is a critical trivial baseline that the proposal needs to address. A second concern: **the RL model might learn query differentiation implicitly.** During RL training, the model already has freedom to write any query it wants, so if the reward signal is clear, it should naturally learn to construct contrastive queries for verification without explicit intent tokens—the tokens might actually constrain rather than help. There's also **AutoRefine's refinement step**, which could capture similar benefits through post-retrieval evidence refinement rather than upstream query construction.

### Premise Assumption Check

1. **Implicit query adaptation**

—The weakest assumption here. The paper claims verification queries need disconfirming evidence, which diverges from topical relevance, but RL-trained models optimize for downstream task performance, not relevance. A well-trained model should learn whatever query patterns maximize the reward, including disconfirming evidence if it helps.

2. **Binary discovery/verification taxonomy**—Plausible but thinly evidenced. ReaLM-Retrieve identified three patterns (early resolution, verification, failed retrieval) that the proposal maps to binary categories, but these were descriptive error analysis categories, not validated intent types. The mapping is convenient rather than grounded.

3. **Heuristic intent classification**—The proposal acknowledges this risk with a pilot study, but the reliability of classifying intent from queries remains uncertain.

4. **NLI-based contrastive reranking**—This assumes that high discriminativeness (strong entailment or contradiction) equals usefulness for verification, but a highly discriminative document could still be irrelevant or unreliable. The metric might not actually correlate with utility.

The novelty comes from combining intent classification within reasoning chains with differentiated retrieval pipelines and RL-discovered verification strategies, but the core contribution is really just operationalizing an existing observation from prior work.

The RL-discovered query strategies feel speculative and depend on empirical results rather than representing a genuine methodological advance. Meanwhile, the research problem itself—constructing better queries in reasoning chains—is important and timely, though the binary discovery/verification distinction may be too simplistic to drive substantial improvements, and any gains will likely be modest percentage-point increases that need to be quite significant for a systems paper at a top venue.

If the results show 3-5% F1 improvements, reviewers probably won't find it surprising—differentiating retrieval intent is an intuitive next step—and while the RL-discovered patterns might be interesting, the overall contribution won't feel game-changing. The related work is thorough and well-positioned against prior work, though there's a risk of over-relying on that positioning rather than standing on independent merit.

The core issue is that this is a competent engineering contribution built on an obvious-in-hindsight observation from ReaLM-Retrieve, with speculative empirical gains from RL-discovered patterns. It's well-executed and clearly written, but the idea itself lacks depth or novelty—the kind of paper that needs strong empirical results to justify acceptance, since the conceptual contribution alone isn't compelling enough.

For EMNLP main conference, I'm looking at medium novelty and significance, with excellent related work coverage. The trivial alternative threat—just using hybrid retrieval everywhere or letting RL learn implicitly—isn't adequately addressed, and the idea fails the "I would have guessed this" test. Given the problem's genuine importance but the engineering-focused nature of the contribution, I'd estimate around 20-28% acceptance probability, with a median of about 24%.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b6d414d8-b993-4d95-a219-63af503937d0",
  "isSidechain": false,
  "requestId": "req_011Cb5QdgVyZmjfJvPHgY2hw",
  "type": "assistant",
  "uuid": "720a096f-fc7e-41a3-a33e-1ed37d849857",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6959a7ca-d39c-4100-bbdf-21ac425702af",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KwBNcKyHNei9Sr7B7z439g",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 908,
      "cache_creation_input_tokens": 1251,
      "cache_read_input_tokens": 36242,
      "output_tokens": 4503,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1251,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 908,
          "output_tokens": 4503,
          "cache_read_input_tokens": 36242,
          "cache_creation_input_tokens": 1251,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1251
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

_source line 35 · 2026-05-16T01:51:47.557Z_

Now I have sufficient information to make my assessment. Let me compile the evaluation.

---

```
【阶段】: Triage

【Trivial Alternative 检验】:

存在两个严重的 trivial alternative 威胁：

1. **统一使用 hybrid BM25+dense+NLI reranking 处理所有 query（无需 intent 分类）**：
   如果 hybrid retrieval + NLI reranking 对 verification query 有效，为什么不对所有 query 都使用它？Proposal 声称 BM25 对 discovery query "更合适"因为它们是 keyword-rich 的，但这只能论证 BM25 不差，不能论证 hybrid 会更差。一个 reviewer 完全可以要求一个 "uniform hybrid for all queries" baseline——如果它表现接近，则 intent classification 的增量价值趋近于零。Proposal 没有讨论这个 trivial alternative。

2. **让 RL 隐式学习 query 差异化（无需显式 intent token）**：
   在 Search-R1 的 RL 训练中，模型已经可以自由生成任意 query 文本。如果 reward signal 足够清晰（EM + faithfulness），模型应该自然学会在需要验证时写出 contrastive query，无需 &lt;discover>/&lt;verify> 的显式约束。显式 intent token 可能反而限制了模型的灵活性。这个 alternative 的增量成本几乎为零（只是调整 reward），却可能达到类似效果。Proposal 的反论（"implicit adaptation cannot capture the distinction because verification is anti-correlated with topical relevance"）存在逻辑跳跃——RL 优化的是下游 EM/F1，不是 topical relevance。

增量价值在于：如果可以证明 (a) uniform hybrid 显著不如 differentiated pipeline，且 (b) 显式 intent token 显著优于让 RL 隐式学习差异化，则 intent classification + differentiated pipeline 的组合有真实增量。但这两个条件目前都是未验证假设。

【前提假设检验】:

核心逻辑链条中存在以下未验证假设：

1. **"隐式 query adaptation 无法捕捉 discovery/verification 区分"**（最关键假设）：
   论证基于 "verification 需要 disconfirming evidence，而 learned query generator 优化 topical relevance"。但 RL-trained query generator（如 Search-R1）优化的是下游任务表现（EM/F1），不是 topical relevance。如果 disconfirming evidence 有助于提高 EM，RL 应当能隐式学会检索它。这个论证把 dense retriever 的训练目标与 RL policy 的训练目标混为一谈。

2. **"ReaLM-Retrieve Section 6.9 的 31% verification rate 可推广到 Search-R1 + Qwen2.5-7B 设置"**：
   ReaLM-Retrieve 使用 DeepSeek-R1-Distill-Qwen-32B 且有自己的 QueryGen 架构，其观察到的 verification pattern 可能与模型规模和架构高度相关。在 7B 模型 + 不同 RL 框架下，verification retrieval 是否仍然是一个 distinct 且 beneficial 的 pattern 是未知的。

3. **"|entailment - contradiction| 是 verification retrieval 的正确 reranking 信号"**：
   一个文档可以与 claim 有强 entailment/contradiction 关系但事实上不相关或不可靠。这个指标衡量的是 NLI 模型的判断置信度，不一定等于 "evidentially informative"。

4. **"二元分类（discovery/verification）是最优粒度"**：
   这个假设虽有合理论证（minimal distinction capturing most variance），但本质上是便利性选择而非有理论支撑的设计。实际 reasoning chain 中的 retrieval intent 可能有更丰富的结构（clarification, comparison, quantification 等）。

【3 维度打分】:

  1. Novelty: 【弱-中】 — 核心贡献是 "operationalize an observation from ReaLM-Retrieve"——将 ReaLM-Retrieve 自己观察到但未利用的 discovery/verification 区分变为显式机制。这是一个合理但 obvious-in-hindsight 的 next step：任何读过 ReaLM-Retrieve Section 6.9 的研究者都会想到"既然 verification retrieval 有不同 pattern，为什么不做不同处理"。Intent classification + differentiated pipeline 的组合在 reasoning-augmented RAG 中是新的，但各组件（BM25/dense hybrid、NLI reranking、contrastive query、RL token format）都来自已有工作的直接拼装。"RL-discovered query strategies" 作为 co-equal contribution 是投机性的——它依赖于一个尚不确定的实验发现，不构成方法论创新。与最相关 5-10 篇近期工作比较后，剥离 surface differences 剩余的 novelty delta 是：显式 intent token + pipeline routing。这是一个 engineering-level 的差异，而非 conceptual-level 的。

  2. Significance: 【中】 — 研究问题本身是重要的：reasoning-augmented retrieval 中 query construction 的质量确实是瓶颈，这一点被 Shakya et al. (2026) 和 ReaLM-Retrieve 的 failure analysis 共同证实。但这个 specific proposal 的影响力受限于：(a) binary intent taxonomy 可能过于粗糙，预期改进幅度有限；(b) 即使 positive，结果大概率是 "moderate improvement on benchmarks"（~2-5% F1），reviewer 会说 "I would have guessed this would help a bit"，不会说 "surprising"；(c) 方法的可推广性受限于需要 NLI reranker 和 dense retriever 的额外基础设施，增加了 deployment 复杂度。不过，如果 RL-discovered query patterns 分析做得好，有一定的 analytical insight 价值。

  3. Related Work: 【强】 — 这是 proposal 最突出的优点。对 2024-2026 年的 reasoning-augmented retrieval 领域做了非常系统的梳理，沿 5 个维度（implicit adaptation, timing/volume control, reasoning-retrieval coordination, post-retrieval quality, verification）清晰分类，差异化定位明确。ReaLM-Retrieve、Veri-R1、AutoRefine、CoRAG、DeepControl、RAFTS、HARIS、Reason and Verify 等均有准确描述和定位。Gap identification 是 genuine 的——确实没有现有系统在 sequential reasoning chain 中做 explicit intent classification + differentiated query construction。唯一的小瑕疵是对 ReaLM-Retrieve Section 6.9 的数据过度依赖作为动机的全部基础。

【概率估计】: [18% - 28%] 中位 22%

【估计理由】:
Related Work 的覆盖和 gap identification 是 strong 的，证明了作者对领域的深入理解，这为论文的 "positioning" 质量提供了保底。但 Novelty 是核心限制因素：idea 的本质是 "operationalize an obvious next step from ReaLM-Retrieve's observation"，属于 incremental engineering contribution 而非 conceptual breakthrough。更严重的是，两个 trivial alternative（uniform hybrid for all, implicit RL learning）构成真实威胁，且 proposal 中未充分讨论。Significance 受限于预期结果的 "I would have guessed this" 性质——即使 positive results，审稿人不太可能认为 surprising。综合来看，这是一个 "方向正确、positioning 优秀但 idea 内核偏薄" 的 proposal，典型的 25% 区间。但 trivial alternative 威胁和核心假设的逻辑跳跃将上界压到 ~28%，中位值降至 22%。

【主要风险】:
1. **Trivial alternative 致命威胁**：Reviewer 几乎必然要求 "uniform hybrid retrieval for all queries" baseline，如果该 baseline 接近 dual-intent 的表现，则 intent classification 的增量价值被否定，论文核心贡献坍塌。
2. **核心前提的逻辑跳跃**："implicit adaptation cannot capture discovery/verification distinction because verification is anti-correlated with topical relevance" 的论证将 dense retriever 的训练目标与 RL policy 的训练目标混淆——RL 优化下游 EM/F1，不是 topical relevance。如果 RL 本身就能隐式学会差异化 query construction，显式 intent token 可能是多余的 inductive bias。
```

**补充说明**：

这个 proposal 在**形式完善度**上是顶级的——compute budget 精确到小时、NLI model separation 的 circularity 论证、per-step training calibration、contingency plan 等都显示了极高的工程规划能力。但正如评估原则所强调的，形式完善度 ≠ idea 好。透过这些精心设计的细节看本质，核心 claim 是："显式区分 retrieval intent 并用不同 pipeline 处理比让 RL 隐式学习更好"——这个 claim 的说服力取决于是否能排除 trivial alternatives，而这恰恰是 proposal 目前最薄弱的环节。

Sources:
- [ReaLM-Retrieve: When to Retrieve During Reasoning](https://arxiv.org/abs/2604.26649)
- [Veri-R1: Claim Verification via Online RL](https://arxiv.org/abs/2510.01932)
- [AutoRefine: Search and Refine During Think](https://arxiv.org/abs/2505.11277)
- [Search-R1: Training LLMs to Reason and Leverage Search Engines](https://arxiv.org/abs/2503.09516)
- [HARIS: Coordinating Search-Informed Reasoning](https://arxiv.org/abs/2506.07528)
- [Contrastive Retrieval-Augmented Generation on Experience](https://aclanthology.org/2025.findings-acl.1224.pdf)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "720a096f-fc7e-41a3-a33e-1ed37d849857",
  "isSidechain": false,
  "requestId": "req_011Cb5QdgVyZmjfJvPHgY2hw",
  "type": "assistant",
  "uuid": "36e10de9-02a8-45e7-9f01-464c0890ee6f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6959a7ca-d39c-4100-bbdf-21ac425702af",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KwBNcKyHNei9Sr7B7z439g",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 908,
      "cache_creation_input_tokens": 1251,
      "cache_read_input_tokens": 36242,
      "output_tokens": 4503,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1251,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 908,
          "output_tokens": 4503,
          "cache_read_input_tokens": 36242,
          "cache_creation_input_tokens": 1251,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1251
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

_source line 36_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Dual-Intent Retrieval: Intent-Differentiated Query Formulation for Reasoning-Augmented RAG  **状态**: 待审阅   **级别**…",
  "leafUuid": "36e10de9-02a8-45e7-9f01-464c0890ee6f",
  "sessionId": "6959a7ca-d39c-4100-bbdf-21ac425702af"
}
```

---

### Runtime record

_source line 37_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate dual-intent retrieval proposal",
  "sessionId": "6959a7ca-d39c-4100-bbdf-21ac425702af"
}
```

---

### Runtime record

_source line 38_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Dual-Intent Retrieval: Intent-Differentiated Query Formulation for Reasoning-Augmented RAG  **状态**: 待审阅   **级别**…",
  "leafUuid": "36e10de9-02a8-45e7-9f01-464c0890ee6f",
  "sessionId": "6959a7ca-d39c-4100-bbdf-21ac425702af"
}
```

---

### Runtime record

_source line 39_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate dual-intent retrieval proposal",
  "sessionId": "6959a7ca-d39c-4100-bbdf-21ac425702af"
}
```

---
