# Research conversation: You are a senior ML research advisor synthesizing a literature review into an actionable research strategy. **Today's da

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-2/6725a028-3696-49b3-b2c2-a8f4330dd39d.jsonl`
- **Structured JSON:** [`f93066375ef6244685b1.json`](../../sessions/f9/f93066375ef6244685b1.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-30T06:35:15.818Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-30T06:35:15.818Z",
  "sessionId": "6725a028-3696-49b3-b2c2-a8f4330dd39d",
  "content": "You are a senior ML research advisor synthesizing a literature review into an actionable research strategy.\n\n**Today's date: 2026-05-30 (UTC).**\n\n## Research area: Target: AAAI 2026\nTrack: Information Retrieval and Knowledge Management\n\nDirection: Train a learned reward model that evaluates whether retrieved documents improve multi-step reasoning chain quality (not just final answer correctness), then use this reasoning-utility reward model as a training signal for dense retrievers via RL or contrastive learning. Evaluate on reasoning-intensive retrieval benchmarks (BRIGHT) where existing utility-based retrievers have not been tested.\n\nSeed Papers:\n- BRIGHT (ICLR 2025) — Established the 40.7-point gap for reasoning-intensive retrieval; defines the evaluation target\n- SCARLet (EMNLP 2025) — Demonstrated utility-based retriever training via perturbation attribution, but uses heuristic utility estimation, not a learned reward model\n- Agentic-R (arXiv Jan 2026) — Trained retrievers on downstream answer correctness (binary EM) as utility signal; closest existing work but uses heuristic signal, not learned reasoning quality\n- ReasonIR (arXiv Apr 2025) — SOTA retriever-only baseline on BRIGHT (29.9 nDCG@10); uses synthetic contrastive data, not reward-based training\n\nKnown Gaps:\n- No existing work uses a LEARNED reward model (as opposed to heuristic EM or perturbation) to evaluate document utility for reasoning-intensive retrieval\n- No utility-based retriever training method has been evaluated on BRIGHT; all evaluations are on standard QA benchmarks\n- The distinction between 'document helps answer' vs 'document helps reasoning process' is unformalized — Agentic-R's binary EM conflates documents containing answers with documents that aid reasoning\n\nTheoretical Anchor: Information-theoretic utility: a document's value for reasoning is the mutual information between the document and the reasoning chain conditioned on the query, not the mutual information between the document and the answer. This distinction predicts that utility-based training with reasoning-quality rewards should preferentially retrieve tutorial/explanation documents over answer-containing documents for reasoning-intensive queries.\n\nConstraints:\n- Compute: ≤200 H100-hours\n\nQuality Self-Checks:\n- [ ] Core insight: Documents that help reasoning are different from documents that contain answers, and a learned reward model can distinguish them where binary EM cannot.\n- [ ] Why not obvious: Agentic-R and SCARLet show utility-based training works, but their heuristic signals (EM, perturbation) cannot distinguish reasoning-helpful from answer-containing documents. A learned reward model is needed because reasoning utility is a latent property requiring inference.\n- [ ] Baseline fear test: YES — Agentic-R's simple binary EM baseline achieves strong results on QA benchmarks. The key bet is that learned reasoning-quality rewards provide gains specifically on reasoning-INTENSIVE tasks (BRIGHT) where EM-based utility training would fail because relevant documents don't contain answers.\n- [ ] Information exploited: Reasoning chain quality signals (intermediate step correctness, coherence, faithfulness) that heuristic utility measures ignore.\n\nAvoid:\n- Conflating this with training the LLM/generator (the vast majority of RL-for-RAG work trains the LLM, not the retriever — we must train the retriever)\n- Claiming the utility-vs-relevance insight is novel (SCARLet and Agentic-R have already demonstrated it; our contribution is the LEARNED REWARD MODEL and REASONING-INTENSIVE evaluation)\n\n## Paper analyses (19 papers)\n\n[\n  {\n    \"title\": \"BRIGHT: A Realistic and Challenging Benchmark for Reasoning-Intensive Retrieval\",\n    \"venue\": \"ICLR 2025 (Spotlight)\",\n    \"problem_identification\": \"Existing retrieval benchmarks (BEIR, MTEB) only test surface-level semantic matching, not reasoning-intensive retrieval where query-document connections require multi-step inference. Identified via observing that SOTA retrievers scoring 59.0 nDCG@10 on MTEB collapse to 18.3 on reasoning-intensive queries — a 40.7-point gap.\",\n    \"key_insight\": \"Relevance in many real-world retrieval scenarios is mediated by reasoning chains (deductive, analogical, causal, analytical) invisible to embedding similarity, creating a fundamentally different retrieval problem than what current benchmarks measure.\",\n    \"innovation_type\": \"new_benchmark\",\n    \"method_summary\": \"Constructed 1,398 queries across 12 domains (StackExchange, LeetCode, AoPS, TheoremQA) where relevant documents are linked in accepted answers but share minimal surface overlap with queries. Gold reasoning annotations explain relevance. Evaluated 13 retrievers plus LLM-based query augmentation (CoT prepended to queries, yielding +12.2 nDCG@10) and reranking (+3.1 additional). Continued pre-training on similar domain data fails to improve performance, validating that the benchmark tests reasoning capability, not domain knowledge.\",\n    \"limitations_and_open_questions\": \"Non-unified definition of 'reasoning' across domains (reviewer criticism); small size (1,398 queries); LLM evaluator for downstream QA has 40-48% deviation from human judgment. Open question: what retriever architectures can close the gap without LLM-in-the-loop reranking?\",\n    \"building_blocks\": [\n      \"BRIGHT benchmark (12 datasets, 1.33M short docs, 5.6K long docs)\",\n      \"Three-level retrieval taxonomy (keyword/semantic/reasoning)\",\n      \"CoT query augmentation protocol\",\n      \"Gold reasoning annotations per query\",\n      \"Leaderboard now showing models reaching 66.9 nDCG@10\"\n    ],\n    \"relevance_to_seed\": \"Defines the exact evaluation target — BRIGHT is where our learned reward model approach must demonstrate gains over heuristic utility-based retrievers, specifically on queries where document relevance requires reasoning rather than semantic similarity.\"\n  },\n  {\n    \"title\": \"SCARLet: Training a Utility-based Retriever Through Shared Context Attribution for Retrieval-Augmented Language Models\",\n    \"venue\": \"EMNLP 2025 (Main)\",\n    \"problem_identification\": \"Utility-based retriever training suffers from two unaddressed issues: (1) pooling training data across tasks introduces semantic interference that conflates relevance with utility, and (2) evaluating passages independently misses inter-passage synergies critical for multi-hop reasoning. Identified through systematic analysis of why AAR/RePlug underperform expectations.\",\n    \"key_insight\": \"Single-variable control — training all tasks from a shared context eliminates contextual variation as a confound, ensuring the only differentiating signal between positive/negative passages is their actual downstream utility, not semantic similarity to any particular query.\",\n    \"innovation_type\": \"new_technique\",\n    \"method_summary\": \"Constructs shared context via Wikidata entity expansion, then generates multi-task training data from this shared context using GPT-4o. Estimates passage-level utility via modified LIME perturbation attribution: samples 64 binary perturbation vectors (passage inclusion/exclusion), measures generator logit fluctuations on ground-truth tokens, fits ridge regression surrogate to obtain per-passage utility coefficients. Critically removes LIME's semantic distance weighting since utility ≠ semantic proximity. Uses 1D clustering to partition passages into positive/negative sets for contrastive training.\",\n    \"limitations_and_open_questions\": \"Fails on code domain (up to -11.9 point drops on code retrieval tasks) because Wikipedia-based shared context doesn't transfer. Requires GPT-4o-level synthesizer; GPT-4o-mini fails. 64 perturbation forward passes per instance is computationally expensive. Open question: can the perturbation-based utility estimation be replaced by a learned model that generalizes across domains?\",\n    \"building_blocks\": [\n      \"Perturbation-based utility attribution (modified LIME)\",\n      \"Shared context construction via entity expansion\",\n      \"Utility vs. relevance distinction formalized via logit fluctuation\",\n      \"Contrastive training on utility-labeled passages\"\n    ],\n    \"relevance_to_seed\": \"Directly motivates our work — SCARLet demonstrates utility-based retriever training works but uses heuristic perturbation attribution; replacing this with a learned reward model that evaluates reasoning chain quality is our core contribution.\"\n  },\n  {\n    \"title\": \"Process Reward Models That Think (ThinkPRM)\",\n    \"venue\": \"arXiv 2025 (ICLR 2026 submission, withdrawn)\",\n    \"problem_identification\": \"Discriminative PRMs require massive step-level labels (~800K in PRM800K), use fixed inference compute, and provide no interpretability. Generative verification (GenRM) existed only for outcome-level assessment with short CoTs. No one had combined long chain-of-thought reasoning with step-level process verification. Identified by observing that reasoning models already possess verification capabilities locked behind formatting/steering issues.\",\n    \"key_insight\": \"Verification is itself a reasoning task that benefits from extended thinking — fine-tuning reasoning models on just ~1K filtered synthetic verification chains (covering ~8K step labels) unlocks process-level verification that outperforms discriminative PRMs trained on 100× more data.\",\n    \"innovation_type\": \"combination\",\n    \"method_summary\": \"Prompts QwQ-32B to generate long verification CoTs for problem-solution pairs from PRM800K. Filters chains requiring: correct format (extractable per-step boxed judgments), alignment with gold step labels, and bounded length (≤4096 tokens). ~20% pass filtering, yielding ~1K chains. Fine-tunes R1-Distill models (1.5B–14B) via full fine-tuning or LoRA. At inference, generates verification CoT then force-decodes 'Is the solution correct?' to extract P(yes)/(P(yes)+P(no)) score. Supports parallel scaling (K independent chains) and sequential scaling (budget forcing).\",\n    \"limitations_and_open_questions\": \"Overconfident scores clustering near 0/1; autoregressive error propagation (early incorrect judgments bias subsequent steps); significant inference overhead (1K-5K tokens per verification). Math-centric training — cross-domain generalization demonstrated on GPQA/LiveCodeBench but untested on retrieval. Can this verification paradigm be adapted to evaluate document utility for reasoning chains?\",\n    \"building_blocks\": [\n      \"Generative process verification via long CoT\",\n      \"Data-efficient PRM training recipe (~1K examples)\",\n      \"Process-based filtering of synthetic data\",\n      \"Test-time compute scaling for verification\",\n      \"Force-decode scoring mechanism\"\n    ],\n    \"relevance_to_seed\": \"Provides the architectural template for our reasoning-utility reward model — ThinkPRM shows that generative PRMs with minimal supervision can evaluate reasoning step quality, which we can adapt to evaluate whether retrieved documents improve reasoning chain quality rather than just final answer correctness.\"\n  },\n  {\n    \"title\": \"Process vs. Outcome Reward: Which is Better for Agentic RAG Reinforcement Learning (ReasonRAG)\",\n    \"venue\": \"NeurIPS 2025 (Poster)\",\n    \"problem_identification\": \"Outcome-supervised RL for agentic RAG (e.g., Search-R1) suffers from low exploration efficiency, gradient conflict (correct early steps penalized alongside late errors), and sparse rewards. Nobody had applied process-level rewards to RAG despite their success in math reasoning. Identified by analyzing three failure modes of outcome RL when applied to multi-step retrieve-reason-answer pipelines.\",\n    \"key_insight\": \"The RAG pipeline has natural decomposition points (query generation, evidence extraction, answer generation) where process-level rewards can be meaningfully defined, and MCTS with shortest-path reward estimation can automatically construct process-level preference data without human annotation.\",\n    \"innovation_type\": \"cross_domain\",\n    \"method_summary\": \"Formulates agentic RAG as a three-stage state machine (Reasoning/Grounding/Terminal). Uses MCTS to explore the RAG decision tree, evaluates nodes via Shortest Path Reward Estimation (SPRE: r = F1 × α^steps, rewarding shorter correct paths). Extracts preference pairs at each stage from MCTS children with differing SPRE scores. Trains Qwen2.5-7B via DPO on 13K preference pairs from 5K questions. Achieves 34.4 Avg EM vs. Search-R1's 32.8 with 18× less training data (5K vs. 90K instances).\",\n    \"limitations_and_open_questions\": \"CRITICAL: trains only the LLM, NOT the retriever (BGE is frozen). The 18× efficiency claim counts instances, not compute — MCTS data generation is expensive. Only tested on factoid QA benchmarks with Wikipedia; no reasoning-intensive evaluation. Modest absolute gains (+1.6 EM over Search-R1). Can process rewards be redirected to train the retriever itself rather than the LLM's retrieval usage?\",\n    \"building_blocks\": [\n      \"Three-stage RAG decomposition with per-stage rewards\",\n      \"MCTS-based automatic preference data construction\",\n      \"Shortest Path Reward Estimation (SPRE)\",\n      \"Process vs. outcome reward comparison methodology\",\n      \"RAG-ProGuide dataset (4.6K questions, 13K preference pairs)\"\n    ],\n    \"relevance_to_seed\": \"Provides strong empirical evidence that process-level rewards outperform outcome-level (binary EM) signals for RAG — directly supporting our thesis that learned reasoning-quality rewards should outperform Agentic-R's binary EM. However, ReasonRAG trains the LLM not the retriever; our work must adapt these process reward insights to retriever training.\"\n  },\n  {\n    \"title\": \"Large Reasoning Embedding Models: Towards Next-Generation Dense Retrieval Paradigm (LREM)\",\n    \"venue\": \"arXiv October 2025\",\n    \"problem_identification\": \"Dense retrievers using direct-embedding paradigm capture statistical co-occurrence rather than deep semantics, failing on queries with significant lexical disparity from targets (alternative queries, negation queries, Q&A-style queries). Identified via e-commerce failure analysis: 'drinks more invigorating than tea' retrieves tea products instead of coffee/Red Bull because the model matches surface 'tea' co-occurrence.\",\n    \"key_insight\": \"Reasoning and embedding can be unified in a single model — instead of pipeline query-rewriting then separate embedding, the model generates CoT reasoning tokens that are directly consumed by the same model to produce the final embedding vector, creating an end-to-end semantic bridge.\",\n    \"innovation_type\": \"combination\",\n    \"method_summary\": \"Built on Qwen2.5-3B with special tokens (&lt;think>, &lt;/think>, &lt;emb>). Stage 1 (Cold Start): joint SFT on CoT generation + InfoNCE contrastive loss on embeddings. Stage 2 (RL): GRPO with three reward signals — format compliance (0.5), length constraint (0.2, CoT ≤16 keyword tokens), and retrieval accuracy (1.0, based on rank of target item in cosine similarity). Training data: 75M query-CoT-item triplets constructed via differential retrieval (keep items found ONLY with CoT-augmented query). Deployed on Taobao since August 2025 with +7-16% improvement in online A/B tests across query categories, at cost of +35ms latency.\",\n    \"limitations_and_open_questions\": \"CoT constrained to ≤16 keyword tokens for latency (not full natural language reasoning). No evaluation on academic benchmarks (BEIR/MTEB/BRIGHT). Knowledge-intensive queries show slight precision drop (-2.74%). Causal attention required for generation prevents bidirectional attention for embedding. How would full natural-language CoT perform if latency weren't a constraint?\",\n    \"building_blocks\": [\n      \"Unified reasoning-embedding architecture\",\n      \"Differential retrieval for training data construction\",\n      \"GRPO with retrieval-accuracy reward for embedding models\",\n      \"Two-stage SFT+RL training pipeline\",\n      \"Production deployment methodology with A/B testing\"\n    ],\n    \"relevance_to_seed\": \"Demonstrates the full SFT+RL pipeline for training reasoning-augmented retrievers at scale, validating that RL with retrieval-specific rewards can improve dense retriever quality. The retrieval-accuracy reward (rank-based) is an outcome reward — our learned reasoning-quality reward model would provide richer signal specifically for reasoning-intensive queries where LREM's keyword CoT may be insufficient.\"\n  },\n  {\n    \"title\": \"Q-RAG: Long Context Multi-Step Retrieval via Value-Based Embedder Training\",\n    \"venue\": \"ICLR 2026 (Oral)\",\n    \"problem_identification\": \"Existing multi-step retrievers require expensive LLM fine-tuning or agent orchestration. Q-RAG identifies that retrieval chunk selection can be formulated as a sequential decision problem solvable entirely within the embedding space, avoiding LLM training costs.\",\n    \"key_insight\": \"The retriever embedder itself can serve as the RL policy via factorized Q-values Q(s,a)=⟨E_s(s),E_a(a)⟩, making the inner product between state and action embeddings the value function — no separate policy network or LLM fine-tuning needed.\",\n    \"innovation_type\": \"new_formulation\",\n    \"method_summary\": \"Models multi-step retrieval as a finite-horizon MDP where states are ordered retrieved chunks, actions are remaining chunks, and rewards are sparse terminal signals (all support facts retrieved). Trains state/action embedders via PQN (on-policy value-based RL with λ-returns) to estimate Q-values through their inner product. Uses Boltzmann exploration with annealed temperature and rotary position embeddings for document-position awareness. All training fits on a single A100 GPU.\",\n    \"limitations_and_open_questions\": \"Relies on sparse terminal reward from gold support-fact labels, not learned reward signals; authors explicitly note LLM-based rewards as unexplored future work. Evaluation focuses on long-context needle-retrieval (BabiLong/RULER) rather than reasoning-intensive benchmarks like BRIGHT.\",\n    \"building_blocks\": [\n      \"Factorized Q-value inner-product architecture for retriever\",\n      \"PQN algorithm avoiding replay buffer for embedding-space RL\",\n      \"MDP formulation of multi-step retrieval with chunk-level actions\",\n      \"Rotary position embedding for document-order awareness\"\n    ],\n    \"relevance_to_seed\": \"Closest architectural precedent for our RL-trained retriever — demonstrates the retriever-as-policy paradigm works, but uses heuristic support-fact rewards instead of a learned reasoning-quality reward model, leaving exactly the gap our proposal fills.\"\n  },\n  {\n    \"title\": \"Agentic-R: Learning to Retrieve for Agentic Search\",\n    \"venue\": \"arXiv 2026\",\n    \"problem_identification\": \"Similarity-based retrievers fail in agentic search because similar passages may not help answer generation. Identified that retriever training must account for both local query-passage relevance AND global downstream answer correctness.\",\n    \"key_insight\": \"Retriever and agent quality are coupled — better retrievers yield better agent queries, and better agent queries yield better retriever training data — so bidirectional iterative co-optimization outperforms training either component in isolation.\",\n    \"innovation_type\": \"combination\",\n    \"method_summary\": \"Defines dual utility signals: local relevance (LLM listwise scoring, 0-100) and global answer correctness (binary EM from agent continuation). Ranks passages by GAC then LR to construct contrastive training pairs. Alternates between PPO-based agent training (with retrieved-token masking) and contrastive retriever fine-tuning using evolving agent-generated queries. Converges in ~2 iterations. Retriever input concatenates original question with current-turn query.\",\n    \"limitations_and_open_questions\": \"Global utility is binary EM — cannot distinguish documents that aid reasoning from those containing the answer string. Evaluated only on standard QA benchmarks (HotpotQA, 2WikiMHQA, etc.), not reasoning-intensive retrieval. The iterative loop requires full agent rollouts per retriever training round, raising compute costs.\",\n    \"building_blocks\": [\n      \"Dual local/global utility signal framework\",\n      \"Bidirectional iterative agent-retriever co-optimization loop\",\n      \"LLM listwise relevance scoring for passage ranking\",\n      \"Retrieved-token masking for agent PPO training\"\n    ],\n    \"relevance_to_seed\": \"Primary baseline — demonstrates utility-based retriever training works but uses heuristic EM as global signal. Our learned reward model replaces binary EM with reasoning-chain quality assessment, targeting the exact limitation that EM conflates answer-containing with reasoning-helpful documents.\"\n  },\n  {\n    \"title\": \"Search-R1: Training LLMs to Reason and Leverage Search Engines with Reinforcement Learning\",\n    \"venue\": \"COLM 2025\",\n    \"problem_identification\": \"Prompting LLMs with reasoning capabilities to use search engines is suboptimal because the LLM lacks trained search-interaction skills. Prior work either fine-tunes on curated search trajectories (imitation) or uses no training at all (prompting).\",\n    \"key_insight\": \"Simple outcome-based RL rewards (binary EM) plus retrieved-token masking are sufficient for LLMs to learn complex multi-turn search behaviors emergently — no process supervision, no curated trajectories, no neural reward models needed.\",\n    \"innovation_type\": \"simplification\",\n    \"method_summary\": \"Extends GRPO/PPO with a search-engine environment: the LLM generates &lt;search>query&lt;/search> tokens to trigger retrieval, receiving results in &lt;information> tags. Retrieved token masking zeroes out gradients for all non-LLM-generated tokens, preventing optimization of retrieval content. Uses pure outcome-based EM reward. Observes emergent behaviors: self-verification searches, increasing search frequency during training, and length dynamics (initial decrease, then strategic increase).\",\n    \"limitations_and_open_questions\": \"Trains the LLM generator, not the retriever — the retriever is frozen BM25/dense. Outcome-only rewards cannot provide credit assignment for individual search decisions, limiting performance on complex multi-hop tasks. Authors acknowledge process/format rewards as unexplored future work.\",\n    \"building_blocks\": [\n      \"Retrieved token masking for stable RL with external knowledge\",\n      \"Outcome-based reward sufficiency for search behavior emergence\",\n      \"Multi-turn search-reasoning interleaving framework\",\n      \"GRPO vs PPO comparison for search-augmented training\"\n    ],\n    \"relevance_to_seed\": \"Establishes the RL-for-search paradigm our work extends, but trains the LLM not the retriever. Its retrieved-token masking technique is directly reusable. Its acknowledged limitation — outcome-only rewards lack credit assignment — is precisely what our process-aware reasoning-quality reward model addresses.\"\n  },\n  {\n    \"title\": \"ReSCORE: Label-free Iterative Retriever Training for Multi-hop Question Answering with Relevance-Consistency Supervision\",\n    \"venue\": \"ACL 2025 (Main)\",\n    \"problem_identification\": \"Dense retrievers require labeled query-document pairs, but for multi-hop QA these labels are unavailable because each retrieval iteration generates different queries depending on the LLM. Found that using only P(answer|query,doc) produces false positives from superficial word overlap.\",\n    \"key_insight\": \"Document utility decomposes into relevance P(query|doc) × consistency P(answer|query,doc), and the relevance term is critical for filtering topically unrelated documents that happen to contain answer strings — addressing exactly the answer-containing vs. reasoning-helpful distinction.\",\n    \"innovation_type\": \"new_technique\",\n    \"method_summary\": \"Uses LLM log-probabilities to compute pseudo-ground-truth scores: Q_LM(d|q) ∝ P_LM(q|d) · P_LM(a|q,d). Trains the dense retriever by minimizing KL divergence between the pseudo-GT distribution and retriever softmax scores over top-M candidates. Operates iteratively: retrieve → answer-or-continue → generate thought summary → reformulate query → repeat. Each iteration recomputes pseudo-labels using the improved retriever's candidates.\",\n    \"limitations_and_open_questions\": \"Requires gold answers for consistency computation, so not truly unsupervised. LLM probability computation over candidates is expensive (M=32 per query per iteration). Not evaluated on reasoning-intensive retrieval — only standard multi-hop QA (HotpotQA, 2WikiMHQA, MuSiQue).\",\n    \"building_blocks\": [\n      \"Relevance × consistency decomposition of document utility\",\n      \"LLM log-probability as pseudo-ground-truth supervision for retrievers\",\n      \"KL-divergence training objective between LLM scores and retriever scores\",\n      \"Iterative query reformulation with thought summarization\"\n    ],\n    \"relevance_to_seed\": \"Validates LLM-as-reward-signal for retriever training and introduces the relevance-consistency decomposition that partially captures our reasoning-utility distinction. However, consistency is still measured against the final answer, not reasoning chain quality — our learned reward model goes further by evaluating intermediate reasoning steps.\"\n  },\n  {\n    \"title\": \"ProRAG: Process-Supervised Reinforcement Learning for Retrieval-Augmented Generation\",\n    \"venue\": \"arXiv 2026\",\n    \"problem_identification\": \"Outcome-based RL for RAG suffers from reward sparsity and process hallucinations — models reach correct answers through flawed reasoning. Sparse scalar rewards cannot pinpoint which intermediate retrieval/reasoning step failed in long-horizon trajectories.\",\n    \"key_insight\": \"Step-level credit assignment in multi-hop RAG requires combining MCTS-discovered contrastive reasoning pairs (judged by GPT-4o) with dual-granularity advantages that weight process and outcome signals separately, enabling correction of flawed intermediate steps even when final answers are correct.\",\n    \"innovation_type\": \"combination\",\n    \"method_summary\": \"Four stages: (1) SFT warmup with structured reasoning format; (2) MCTS exploration to find contrastive sibling-node pairs, judged by GPT-4o, yielding ~8K preference pairs to train a PRM via pairwise ranking loss; (3) rejection sampling fine-tuning filtered by both outcome correctness and PRM score threshold (~105K examples); (4) GRPO with dual-granularity advantage A = A_out + β·A_proc (β=0.3), where process advantage comes from frozen PRM and outcome advantage from EM reward.\",\n    \"limitations_and_open_questions\": \"Trains the LLM/generator, not the retriever. MCTS exploration and GPT-4o judging are expensive (unclear if fits within 200 H100-hour budget). PRM is trained on reasoning step quality, not document utility — the reward model evaluates reasoning, not retrieval relevance.\",\n    \"building_blocks\": [\n      \"MCTS-based contrastive pair discovery for PRM training\",\n      \"Dual-granularity advantage combining step-level and outcome-level rewards\",\n      \"GPT-4o as logical judge for step validity in preference pair construction\",\n      \"Four-stage training pipeline: SFT → PRM → RFT → RL\"\n    ],\n    \"relevance_to_seed\": \"Closest architecture for our reasoning-utility reward model construction — the MCTS-based PRM training and dual-granularity advantage mechanism can be adapted from evaluating reasoning steps to evaluating document utility for reasoning. Key difference: ProRAG's PRM judges reasoning quality; our reward model judges whether a document improves reasoning quality.\"\n  },\n  {\n    \"title\": \"ReasonIR: Training Retrievers for Reasoning Tasks\",\n    \"venue\": \"arXiv 2025 (accepted COLM 2025)\",\n    \"problem_identification\": \"Existing retrievers fail on reasoning-intensive queries because training data consists of short factual QA pairs (~20 tokens), while reasoning queries average ~194 tokens and require multi-step inference to match documents. A pilot study showed retrievers plateau or degrade beyond ~256 token queries despite supporting longer contexts.\",\n    \"key_insight\": \"The bottleneck for reasoning-intensive retrieval is training data distribution, not model architecture or context length — retrievers must be trained on long, reasoning-structured query-document pairs where relevance requires inference, not lexical overlap.\",\n    \"innovation_type\": \"new_technique\",\n    \"method_summary\": \"Builds a synthetic data pipeline using Llama-3.1-70B producing two data types: Varied-Length (VL) data with 300–2000 word queries and Hard Query (HQ) data targeting higher-order thinking (analysis, synthesis). Hard negatives are generated via multi-turn prompting conditioned on both query and positive, avoiding false negatives from failed BM25 mining. Trains a bi-encoder (Llama-3.1-8B with bidirectional attention) on ~1.73M samples using InfoNCE loss. A simple score interpolation reranker (0.5*reranker + 0.5*retriever) achieves near-SOTA at 200x less compute than reasoning rerankers.\",\n    \"limitations_and_open_questions\": \"HQ seed documents drawn from BRIGHT corpus raise domain leakage concerns (reviewers flagged this). Coding/theorem domains remain weak (10.5–19.6 nDCG@10). Requires 70B LLM for quality data generation — 8B produces significantly worse negatives. No utility-based or reward-model-based training signal; purely contrastive.\",\n    \"building_blocks\": [\n      \"Synthetic reasoning-intensive query generation pipeline\",\n      \"Multi-turn hard negative generation\",\n      \"Score interpolation reranking\",\n      \"BRIGHT benchmark (29.9 nDCG@10 baseline)\",\n      \"Query rewriting as test-time compute scaling\"\n    ],\n    \"relevance_to_seed\": \"Primary baseline to beat on BRIGHT; demonstrates contrastive training ceiling without reward-based utility signals — our learned reward model targets exactly the gap where synthetic contrastive data cannot distinguish reasoning-helpful from answer-containing documents.\"\n  },\n  {\n    \"title\": \"RaDeR: Reasoning-aware Dense Retrieval Models\",\n    \"venue\": \"EMNLP 2025 (Main)\",\n    \"problem_identification\": \"No first-stage dense retriever performs reasoning for relevance judgment — prior work either uses off-the-shelf retrievers with reasoning-augmented queries (IRCoT, ReAct) or reasoning rerankers (RANK-1) limited by first-stage recall. CoT query augmentation helps BM25 via added terms but fails for dense retrievers lacking reasoning training.\",\n    \"key_insight\": \"MCTS-based math problem solving naturally generates reasoning-intensive retriever training data: partial solution trajectories become queries, retrieved theorems verified by answer correctness become positives, and self-reflection-rejected theorems become hard negatives — all with automatic relevance labels requiring no human annotation.\",\n    \"innovation_type\": \"combination\",\n    \"method_summary\": \"Extends the rStar MCTS framework with Generate-Query and Retrieve-Theorem actions over ProofWiki. High-reward trajectories yield (partial-CoT-query, theorem) training pairs; theorems rejected by LLM self-reflection become hard negatives. Generates three reasoning query types (MCTS-CoT, LLM-reasoning, question) plus lexical queries filtered by round-trip BM25 consistency. Trains bi-encoder retrievers (Qwen2.5 variants) with InfoNCE on only 43K–121K samples.\",\n    \"limitations_and_open_questions\": \"Single-document reasoning only — cannot handle multi-hop where relevance is interdependent. Math-domain data pipeline requires verifiable answers and structured knowledge bases; extension to other domains is non-trivial. MS MARCO MRR drops from 41.2 to 34.4 vs RepLLaMA, suggesting reasoning-standard retrieval tradeoff.\",\n    \"building_blocks\": [\n      \"MCTS-derived retrieval training data\",\n      \"Self-reflective relevance evaluation as automatic labeling\",\n      \"Answer correctness as proxy relevance signal\",\n      \"Sample-efficient training (2.5% of ReasonIR's data, +1.1 nDCG@10)\"\n    ],\n    \"relevance_to_seed\": \"Demonstrates that answer-correctness reward signals from reasoning trajectories can train effective retrievers with extreme sample efficiency — validates the principle that downstream task performance can supervise retriever training, but uses binary answer correctness rather than a learned reasoning-quality reward model.\"\n  },\n  {\n    \"title\": \"CoSearch: Joint Training of Reasoning and Document Ranking via Reinforcement Learning for Agentic Search\",\n    \"venue\": \"arXiv 2026 (in submission)\",\n    \"problem_identification\": \"Existing agentic search systems (Search-R1) treat retrieval as a frozen tool, optimizing only the reasoning agent. An oracle experiment promoting answer-containing documents to top positions showed 26.8% relative F1 improvement for a 3B agent, proving retrieval quality is a major bottleneck.\",\n    \"key_insight\": \"The reasoning agent and document ranker are interdependent and must be co-optimized — the agent's sub-queries shape ranker inputs while ranker outputs shape agent reasoning, creating a feedback loop that fixed-retriever training cannot exploit.\",\n    \"innovation_type\": \"new_formulation\",\n    \"method_summary\": \"Jointly optimizes a reasoning agent and a generative listwise ranker (both Qwen2.5-7B) via GRPO. The ranker reranks 50 E5-retrieved candidates to top-5. A novel semantic query grouping technique (token-F1 threshold δ=0.8) clusters sub-queries across rollouts to satisfy GRPO's identical-input requirement for the ranker — at zero additional sampling cost. Composite rewards combine Hit@k relevance (when answer-containing docs exist) with trajectory-level F1 (always), with a threshold γ=0.5 governing the mixture.\",\n    \"limitations_and_open_questions\": \"First-stage retriever (E5) remains frozen, capping recall. Evaluated only on QA benchmarks with Wikipedia corpus — no reasoning-intensive benchmarks like BRIGHT. Pseudo-relevance labels (string match for answer) conflate answer-containing with reasoning-helpful documents. 3B ranker caused training divergence, suggesting minimum capacity requirements.\",\n    \"building_blocks\": [\n      \"Semantic query grouping for GRPO on rankers\",\n      \"Composite relevance + trajectory rewards\",\n      \"Oracle retrieval experiments to quantify retrieval bottleneck\",\n      \"Joint agent-ranker RL framework\"\n    ],\n    \"relevance_to_seed\": \"Closest architectural parallel to our proposal — applies RL rewards to train a retrieval component — but uses answer-correctness rewards (binary F1) rather than learned reasoning-quality rewards, and trains a reranker rather than the dense retriever itself. Validates that RL-based retrieval training improves agentic search but does not address the reasoning-utility distinction.\"\n  },\n  {\n    \"title\": \"RAG-RewardBench: Benchmarking Reward Models in Retrieval Augmented Generation for Preference Alignment\",\n    \"venue\": \"ACL 2025 (Findings)\",\n    \"problem_identification\": \"Existing RM benchmarks (RewardBench) evaluate only general scenarios with ~47-token prompts, completely missing RAG-specific challenges. Models scoring 90%+ on RewardBench drop to 78.3% on RAG tasks. No benchmark existed to assess RMs on multi-hop reasoning, citation quality, abstention, or conflict robustness in RAG contexts.\",\n    \"key_insight\": \"Trained RALMs (Self-RAG, ChatQA, FgCite) show almost no preference alignment improvement over base models (0.4–2.8%) despite large accuracy gains on RAG tasks — current RALM training optimizes task accuracy but completely fails to align with human preferences for citation, abstention, and robustness.\",\n    \"innovation_type\": \"new_benchmark\",\n    \"method_summary\": \"Constructs 1,485 preference pairs across 18 datasets in 4 RAG-specific scenarios (multi-hop reasoning, fine-grained citation, appropriate abstention, conflict robustness). Uses 24 RALMs for response generation, 6 diverse retrievers, and 4 commercial LLM judges scoring 5 dimensions. Consistency filtering and difficulty calibration (1–2 point score gaps) ensure quality. Evaluates 45 RMs spanning discriminative, generative, and implicit (DPO) types.\",\n    \"limitations_and_open_questions\": \"Evaluates only outcome-level preferences, not process-level reasoning quality. LLM-as-judge dependency may introduce systematic biases. Static benchmark of 1,485 pairs risks saturation. The benchmark identifies the RM gap for RAG but proposes no solution — designing RAG-specialized RMs remains open.\",\n    \"building_blocks\": [\n      \"RAG-specific RM evaluation taxonomy (4 scenarios, 18 subsets)\",\n      \"LLM-as-judge annotation pipeline with consistency filtering\",\n      \"Evidence that implicit RMs (DPO) fail in RAG contexts\",\n      \"Baseline RM performance data for RAG reward modeling\"\n    ],\n    \"relevance_to_seed\": \"Directly validates our premise that existing RMs are inadequate for RAG-specific evaluation and that a specialized learned reward model is needed. The multi-hop reasoning and citation scenarios provide evaluation methodology for our reasoning-utility reward model, and the finding that RALMs fail at preference alignment motivates reward-model-driven training.\"\n  },\n  {\n    \"title\": \"Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection\",\n    \"venue\": \"ICLR 2024 (Oral, top 1%)\",\n    \"problem_identification\": \"Indiscriminate retrieval in RAG systems hurts performance — ChatGPT with retrieval scores worse than without on several tasks. Additionally, no mechanism ensures generated text is faithful to retrieved evidence. The gap is both when-to-retrieve and how-to-verify-grounding.\",\n    \"key_insight\": \"Retrieval decisions and output quality assessment can be distilled into the LM itself as special reflection tokens (Retrieve, IsRel, IsSup, IsUse), trained via standard next-token prediction on critic-augmented data — eliminating the need for separate runtime components or expensive online RL.\",\n    \"innovation_type\": \"new_formulation\",\n    \"method_summary\": \"Trains a critic model (Llama2-7B) on GPT-4-labeled examples to predict 4 reflection token types. Uses this critic offline to augment 150K training examples with inline reflection tokens. Trains the generator on augmented sequences where retrieved passages are masked in loss computation. At inference, segment-level beam search scores candidates using both generation probability and reflection token probabilities, with user-adjustable weights enabling per-task controllability without retraining.\",\n    \"limitations_and_open_questions\": \"Evaluates single-passage selection only — no cross-passage synthesis (reviewer 4MCy). Reflection tokens are post-hoc selectors, not generation guides. Computational overhead of segment-level beam search with multiple passages. Retriever (Contriever) remains frozen and off-the-shelf, bounding recall quality.\",\n    \"building_blocks\": [\n      \"Reflection token paradigm for learned self-evaluation in RAG\",\n      \"Critic-based offline data augmentation (avoiding online RL)\",\n      \"Inference-time controllability via reflection token weights\",\n      \"Segment-level beam search with critique scoring\"\n    ],\n    \"relevance_to_seed\": \"Foundational paradigm for learned evaluation signals in RAG — our reasoning-utility reward model extends the reflection token concept from generation-quality evaluation to document-utility evaluation for retriever training. Self-RAG's IsRel/IsSup tokens evaluate 'does this passage support generation' while our reward model would evaluate 'does this document improve reasoning chain quality' — a complementary but distinct signal.\"\n  },\n  {\n    \"title\": \"ReasonEmbed: Enhanced Text Embeddings for Reasoning-Intensive Document Retrieval\",\n    \"venue\": \"ACL 2026 (Main)\",\n    \"problem_identification\": \"Identified the 'triviality problem' in synthetic retrieval training data: existing datasets (including ReasonIR's) exhibit surface-level query-document overlap that can be solved by lexical matching rather than reasoning, yielding only marginal gains on BRIGHT. Diagnosed empirically by showing high ROUGE overlap correlates with poor nDCG@10 (14.5 vs. 37.1).\",\n    \"key_insight\": \"Source documents used as positives in synthetic data create trivial training signal; excluding them and mining semantically-correlated-but-lexically-distinct positives forces models to learn reasoning-based matching.\",\n    \"innovation_type\": \"combination\",\n    \"method_summary\": \"ReMixer is a 3-stage data synthesis pipeline: (1) conditioned query generation from BRIGHT domains via Qwen2.5-72B with explicit reasoning requirements, (2) source-excluded candidate mining that retrieves positives different in form but correlated in essence, and (3) reasoning-enhanced relevance annotation via a distilled Qwen3-8B annotator trained on Qwen3-235B reasoning traces. Redapter dynamically reweights training via RI-InfoNCE: reasoning intensity RI(s) = min(L_q,D / L_q',D, κ) compares contrastive loss with/without reasoning-augmented queries, upweighting samples where reasoning matters most. Trained with LoRA on Qwen3-8B backbone, single epoch, 82K samples.\",\n    \"limitations_and_open_questions\": \"Relies entirely on synthetic data quality rather than learning utility signals from downstream reasoning performance; Redapter's RI metric requires reasoning-augmented query rewrites at training time. Does not address whether gains transfer beyond embedding-only retrieval to full RAG pipelines.\",\n    \"building_blocks\": [\n      \"ReMixer source-excluded mining pipeline\",\n      \"RI-InfoNCE adaptive weighting by reasoning intensity\",\n      \"Distilled relevance annotator from reasoning traces\",\n      \"82K reasoning-intensive training dataset across 12 domains\"\n    ],\n    \"relevance_to_seed\": \"Sets the BRIGHT SOTA at 38.1 nDCG@10 — our primary evaluation target; its data-centric approach (better training data) is complementary to our reward-model approach (better training signal), and Redapter's reasoning-intensity metric could inform our reward model design.\"\n  },\n  {\n    \"title\": \"RM-R1: Reward Modeling as Reasoning\",\n    \"venue\": \"ICLR 2026\",\n    \"problem_identification\": \"Observed that scalar reward models produce opaque numeric scores and generative RMs produce shallow free-form judgments — neither performs structured reasoning over evaluation criteria. This limits both interpretability and performance on complex preference judgments.\",\n    \"key_insight\": \"Reward modeling should be formulated as a reasoning task: the model first self-generates task-specific evaluation rubrics (for chat) or solves the problem itself (for reasoning), then systematically evaluates against these criteria — making the evaluation process itself a structured reasoning chain.\",\n    \"innovation_type\": \"new_formulation\",\n    \"method_summary\": \"Chain-of-Rubrics (CoR) categorizes inputs as Chat or Reasoning; for Chat, the model generates weighted rubrics in &lt;rubric> tags then evaluates responses against them; for Reasoning, it first solves the problem in &lt;solution> tags then judges correctness. Training is two-phase: (1) distillation from oracle models (Claude-3.7-Sonnet, O3) on ~8.7K samples to bootstrap structured reasoning traces, then (2) GRPO on 64K preference data with a simple binary verifiable reward (correct label = +1, wrong = -1). Evaluated on Qwen-2.5-Instruct and DeepSeek-Distilled-Qwen at 7B-32B scales.\",\n    \"limitations_and_open_questions\": \"Reward is purely binary (correct/incorrect label), missing opportunities for granular quality signals; CoR mechanism adds inference cost from generating rubrics/solutions before scoring. Untested on document-level utility evaluation — only applied to response preference, not retrieval contexts.\",\n    \"b\n... (truncated)\n\n## Your task\n\nSynthesize these paper analyses into a **Field Guide** — a strategic document that would help a researcher generate novel, high-quality ideas in this area. This is NOT a survey — it's an opinionated strategy guide for innovation.\n\nThink about:\n- What PATTERNS OF INNOVATION keep working in this field?\n- What do reviewers consistently reward?\n- Where are the real gaps (not assumed gaps)?\n- What combinations haven't been tried?\n- What mistakes should we avoid?\n\n## Output format\n\nOutput a JSON object with these sections:\n{\n  \"innovation_patterns\": [\n    {\"pattern\": \"name\", \"description\": \"how it works\", \"examples\": [\"paper1\", \"paper2\"], \"success_rate\": \"high/medium/low\"}\n  ],\n  \"reviewer_preferences\": [\n    \"What reviewers in this area consistently care about (based on evidence from paper analyses)\"\n  ],\n  \"field_gaps\": [\n    {\"gap\": \"description of unsolved problem\", \"evidence\": \"which papers mention this limitation\", \"difficulty\": \"high/medium/low\", \"impact_if_solved\": \"high/medium/low\"}\n  ],\n  \"untried_combinations\": [\n    {\"idea_sketch\": \"what could be combined\", \"from_papers\": [\"which papers inspire this\"], \"why_promising\": \"reason\"}\n  ],\n  \"method_building_blocks\": [\n    {\"tool\": \"name\", \"what_it_does\": \"description\", \"used_by\": [\"papers\"], \"could_be_applied_to\": \"new application\"}\n  ],\n  \"common_pitfalls\": [\n    \"Mistakes to avoid when working in this area (based on reviewer feedback and paper limitations)\"\n  ],\n  \"field_trajectory\": \"Where is this field heading? What are the 2-3 most promising macro-directions? (paragraph)\",\n  \"meta_advice\": \"If you were advising a PhD student to write a strong 2026 paper in this area, what would you tell them? (paragraph)\"\n}\n\nBe specific and evidence-based — every claim should reference specific papers from the analyses. Avoid generic advice like 'be novel' — instead say 'Papers that combine X with Y for task Z have been getting accepted (see Paper A, Paper B).'.\n\nIMPORTANT: You MUST end your response with the JSON object."
}
```

---

### Runtime record

_source line 2 · 2026-05-30T06:35:15.822Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-30T06:35:15.822Z",
  "sessionId": "6725a028-3696-49b3-b2c2-a8f4330dd39d"
}
```

---

## Round 1

11 recorded events

### User

_source line 3 · 2026-05-30T06:35:15.836Z_

You are a senior ML research advisor synthesizing a literature review into an actionable research strategy.

**Today's date: 2026-05-30 (UTC).**

## Research area: Target: AAAI 2026
Track: Information Retrieval and Knowledge Management

Direction: Train a learned reward model that evaluates whether retrieved documents improve multi-step reasoning chain quality (not just final answer correctness), then use this reasoning-utility reward model as a training signal for dense retrievers via RL or contrastive learning. Evaluate on reasoning-intensive retrieval benchmarks (BRIGHT) where existing utility-based retrievers have not been tested.

Seed Papers:
- BRIGHT (ICLR 2025) — Established the 40.7-point gap for reasoning-intensive retrieval; defines the evaluation target
- SCARLet (EMNLP 2025) — Demonstrated utility-based retriever training via perturbation attribution, but uses heuristic utility estimation, not a learned reward model
- Agentic-R (arXiv Jan 2026) — Trained retrievers on downstream answer correctness (binary EM) as utility signal; closest existing work but uses heuristic signal, not learned reasoning quality
- ReasonIR (arXiv Apr 2025) — SOTA retriever-only baseline on BRIGHT (29.9 nDCG@10); uses synthetic contrastive data, not reward-based training

Known Gaps:
- No existing work uses a LEARNED reward model (as opposed to heuristic EM or perturbation) to evaluate document utility for reasoning-intensive retrieval
- No utility-based retriever training method has been evaluated on BRIGHT; all evaluations are on standard QA benchmarks
- The distinction between 'document helps answer' vs 'document helps reasoning process' is unformalized — Agentic-R's binary EM conflates documents containing answers with documents that aid reasoning

Theoretical Anchor: Information-theoretic utility: a document's value for reasoning is the mutual information between the document and the reasoning chain conditioned on the query, not the mutual information between the document and the answer. This distinction predicts that utility-based training with reasoning-quality rewards should preferentially retrieve tutorial/explanation documents over answer-containing documents for reasoning-intensive queries.

Constraints:
- Compute: ≤200 H100-hours

Quality Self-Checks:
- [ ] Core insight: Documents that help reasoning are different from documents that contain answers, and a learned reward model can distinguish them where binary EM cannot.
- [ ] Why not obvious: Agentic-R and SCARLet show utility-based training works, but their heuristic signals (EM, perturbation) cannot distinguish reasoning-helpful from answer-containing documents. A learned reward model is needed because reasoning utility is a latent property requiring inference.
- [ ] Baseline fear test: YES — Agentic-R's simple binary EM baseline achieves strong results on QA benchmarks. The key bet is that learned reasoning-quality rewards provide gains specifically on reasoning-INTENSIVE tasks (BRIGHT) where EM-based utility training would fail because relevant documents don't contain answers.
- [ ] Information exploited: Reasoning chain quality signals (intermediate step correctness, coherence, faithfulness) that heuristic utility measures ignore.

Avoid:
- Conflating this with training the LLM/generator (the vast majority of RL-for-RAG work trains the LLM, not the retriever — we must train the retriever)
- Claiming the utility-vs-relevance insight is novel (SCARLet and Agentic-R have already demonstrated it; our contribution is the LEARNED REWARD MODEL and REASONING-INTENSIVE evaluation)

## Paper analyses (19 papers)

[
  {
    "title": "BRIGHT: A Realistic and Challenging Benchmark for Reasoning-Intensive Retrieval",
    "venue": "ICLR 2025 (Spotlight)",
    "problem_identification": "Existing retrieval benchmarks (BEIR, MTEB) only test surface-level semantic matching, not reasoning-intensive retrieval where query-document connections require multi-step inference. Identified via observing that SOTA retrievers scoring 59.0 nDCG@10 on MTEB collapse to 18.3 on reasoning-intensive queries — a 40.7-point gap.",
    "key_insight": "Relevance in many real-world retrieval scenarios is mediated by reasoning chains (deductive, analogical, causal, analytical) invisible to embedding similarity, creating a fundamentally different retrieval problem than what current benchmarks measure.",
    "innovation_type": "new_benchmark",
    "method_summary": "Constructed 1,398 queries across 12 domains (StackExchange, LeetCode, AoPS, TheoremQA) where relevant documents are linked in accepted answers but share minimal surface overlap with queries. Gold reasoning annotations explain relevance. Evaluated 13 retrievers plus LLM-based query augmentation (CoT prepended to queries, yielding +12.2 nDCG@10) and reranking (+3.1 additional). Continued pre-training on similar domain data fails to improve performance, validating that the benchmark tests reasoning capability, not domain knowledge.",
    "limitations_and_open_questions": "Non-unified definition of 'reasoning' across domains (reviewer criticism); small size (1,398 queries); LLM evaluator for downstream QA has 40-48% deviation from human judgment. Open question: what retriever architectures can close the gap without LLM-in-the-loop reranking?",
    "building_blocks": [
      "BRIGHT benchmark (12 datasets, 1.33M short docs, 5.6K long docs)",
      "Three-level retrieval taxonomy (keyword/semantic/reasoning)",
      "CoT query augmentation protocol",
      "Gold reasoning annotations per query",
      "Leaderboard now showing models reaching 66.9 nDCG@10"
    ],
    "relevance_to_seed": "Defines the exact evaluation target — BRIGHT is where our learned reward model approach must demonstrate gains over heuristic utility-based retrievers, specifically on queries where document relevance requires reasoning rather than semantic similarity."
  },
  {
    "title": "SCARLet: Training a Utility-based Retriever Through Shared Context Attribution for Retrieval-Augmented Language Models",
    "venue": "EMNLP 2025 (Main)",
    "problem_identification": "Utility-based retriever training suffers from two unaddressed issues: (1) pooling training data across tasks introduces semantic interference that conflates relevance with utility, and (2) evaluating passages independently misses inter-passage synergies critical for multi-hop reasoning. Identified through systematic analysis of why AAR/RePlug underperform expectations.",
    "key_insight": "Single-variable control — training all tasks from a shared context eliminates contextual variation as a confound, ensuring the only differentiating signal between positive/negative passages is their actual downstream utility, not semantic similarity to any particular query.",
    "innovation_type": "new_technique",
    "method_summary": "Constructs shared context via Wikidata entity expansion, then generates multi-task training data from this shared context using GPT-4o. Estimates passage-level utility via modified LIME perturbation attribution: samples 64 binary perturbation vectors (passage inclusion/exclusion), measures generator logit fluctuations on ground-truth tokens, fits ridge regression surrogate to obtain per-passage utility coefficients. Critically removes LIME's semantic distance weighting since utility ≠ semantic proximity. Uses 1D clustering to partition passages into positive/negative sets for contrastive training.",
    "limitations_and_open_questions": "Fails on code domain (up to -11.9 point drops on code retrieval tasks) because Wikipedia-based shared context doesn't transfer. Requires GPT-4o-level synthesizer; GPT-4o-mini fails. 64 perturbation forward passes per instance is computationally expensive. Open question: can the perturbation-based utility estimation be replaced by a learned model that generalizes across domains?",
    "building_blocks": [
      "Perturbation-based utility attribution (modified LIME)",
      "Shared context construction via entity expansion",
      "Utility vs. relevance distinction formalized via logit fluctuation",
      "Contrastive training on utility-labeled passages"
    ],
    "relevance_to_seed": "Directly motivates our work — SCARLet demonstrates utility-based retriever training works but uses heuristic perturbation attribution; replacing this with a learned reward model that evaluates reasoning chain quality is our core contribution."
  },
  {
    "title": "Process Reward Models That Think (ThinkPRM)",
    "venue": "arXiv 2025 (ICLR 2026 submission, withdrawn)",
    "problem_identification": "Discriminative PRMs require massive step-level labels (~800K in PRM800K), use fixed inference compute, and provide no interpretability. Generative verification (GenRM) existed only for outcome-level assessment with short CoTs. No one had combined long chain-of-thought reasoning with step-level process verification. Identified by observing that reasoning models already possess verification capabilities locked behind formatting/steering issues.",
    "key_insight": "Verification is itself a reasoning task that benefits from extended thinking — fine-tuning reasoning models on just ~1K filtered synthetic verification chains (covering ~8K step labels) unlocks process-level verification that outperforms discriminative PRMs trained on 100× more data.",
    "innovation_type": "combination",
    "method_summary": "Prompts QwQ-32B to generate long verification CoTs for problem-solution pairs from PRM800K. Filters chains requiring: correct format (extractable per-step boxed judgments), alignment with gold step labels, and bounded length (≤4096 tokens). ~20% pass filtering, yielding ~1K chains. Fine-tunes R1-Distill models (1.5B–14B) via full fine-tuning or LoRA. At inference, generates verification CoT then force-decodes 'Is the solution correct?' to extract P(yes)/(P(yes)+P(no)) score. Supports parallel scaling (K independent chains) and sequential scaling (budget forcing).",
    "limitations_and_open_questions": "Overconfident scores clustering near 0/1; autoregressive error propagation (early incorrect judgments bias subsequent steps); significant inference overhead (1K-5K tokens per verification). Math-centric training — cross-domain generalization demonstrated on GPQA/LiveCodeBench but untested on retrieval. Can this verification paradigm be adapted to evaluate document utility for reasoning chains?",
    "building_blocks": [
      "Generative process verification via long CoT",
      "Data-efficient PRM training recipe (~1K examples)",
      "Process-based filtering of synthetic data",
      "Test-time compute scaling for verification",
      "Force-decode scoring mechanism"
    ],
    "relevance_to_seed": "Provides the architectural template for our reasoning-utility reward model — ThinkPRM shows that generative PRMs with minimal supervision can evaluate reasoning step quality, which we can adapt to evaluate whether retrieved documents improve reasoning chain quality rather than just final answer correctness."
  },
  {
    "title": "Process vs. Outcome Reward: Which is Better for Agentic RAG Reinforcement Learning (ReasonRAG)",
    "venue": "NeurIPS 2025 (Poster)",
    "problem_identification": "Outcome-supervised RL for agentic RAG (e.g., Search-R1) suffers from low exploration efficiency, gradient conflict (correct early steps penalized alongside late errors), and sparse rewards. Nobody had applied process-level rewards to RAG despite their success in math reasoning. Identified by analyzing three failure modes of outcome RL when applied to multi-step retrieve-reason-answer pipelines.",
    "key_insight": "The RAG pipeline has natural decomposition points (query generation, evidence extraction, answer generation) where process-level rewards can be meaningfully defined, and MCTS with shortest-path reward estimation can automatically construct process-level preference data without human annotation.",
    "innovation_type": "cross_domain",
    "method_summary": "Formulates agentic RAG as a three-stage state machine (Reasoning/Grounding/Terminal). Uses MCTS to explore the RAG decision tree, evaluates nodes via Shortest Path Reward Estimation (SPRE: r = F1 × α^steps, rewarding shorter correct paths). Extracts preference pairs at each stage from MCTS children with differing SPRE scores. Trains Qwen2.5-7B via DPO on 13K preference pairs from 5K questions. Achieves 34.4 Avg EM vs. Search-R1's 32.8 with 18× less training data (5K vs. 90K instances).",
    "limitations_and_open_questions": "CRITICAL: trains only the LLM, NOT the retriever (BGE is frozen). The 18× efficiency claim counts instances, not compute — MCTS data generation is expensive. Only tested on factoid QA benchmarks with Wikipedia; no reasoning-intensive evaluation. Modest absolute gains (+1.6 EM over Search-R1). Can process rewards be redirected to train the retriever itself rather than the LLM's retrieval usage?",
    "building_blocks": [
      "Three-stage RAG decomposition with per-stage rewards",
      "MCTS-based automatic preference data construction",
      "Shortest Path Reward Estimation (SPRE)",
      "Process vs. outcome reward comparison methodology",
      "RAG-ProGuide dataset (4.6K questions, 13K preference pairs)"
    ],
    "relevance_to_seed": "Provides strong empirical evidence that process-level rewards outperform outcome-level (binary EM) signals for RAG — directly supporting our thesis that learned reasoning-quality rewards should outperform Agentic-R's binary EM. However, ReasonRAG trains the LLM not the retriever; our work must adapt these process reward insights to retriever training."
  },
  {
    "title": "Large Reasoning Embedding Models: Towards Next-Generation Dense Retrieval Paradigm (LREM)",
    "venue": "arXiv October 2025",
    "problem_identification": "Dense retrievers using direct-embedding paradigm capture statistical co-occurrence rather than deep semantics, failing on queries with significant lexical disparity from targets (alternative queries, negation queries, Q&A-style queries). Identified via e-commerce failure analysis: 'drinks more invigorating than tea' retrieves tea products instead of coffee/Red Bull because the model matches surface 'tea' co-occurrence.",
    "key_insight": "Reasoning and embedding can be unified in a single model — instead of pipeline query-rewriting then separate embedding, the model generates CoT reasoning tokens that are directly consumed by the same model to produce the final embedding vector, creating an end-to-end semantic bridge.",
    "innovation_type": "combination",
    "method_summary": "Built on Qwen2.5-3B with special tokens (&lt;think>, &lt;/think>, &lt;emb>). Stage 1 (Cold Start): joint SFT on CoT generation + InfoNCE contrastive loss on embeddings. Stage 2 (RL): GRPO with three reward signals — format compliance (0.5), length constraint (0.2, CoT ≤16 keyword tokens), and retrieval accuracy (1.0, based on rank of target item in cosine similarity). Training data: 75M query-CoT-item triplets constructed via differential retrieval (keep items found ONLY with CoT-augmented query). Deployed on Taobao since August 2025 with +7-16% improvement in online A/B tests across query categories, at cost of +35ms latency.",
    "limitations_and_open_questions": "CoT constrained to ≤16 keyword tokens for latency (not full natural language reasoning). No evaluation on academic benchmarks (BEIR/MTEB/BRIGHT). Knowledge-intensive queries show slight precision drop (-2.74%). Causal attention required for generation prevents bidirectional attention for embedding. How would full natural-language CoT perform if latency weren't a constraint?",
    "building_blocks": [
      "Unified reasoning-embedding architecture",
      "Differential retrieval for training data construction",
      "GRPO with retrieval-accuracy reward for embedding models",
      "Two-stage SFT+RL training pipeline",
      "Production deployment methodology with A/B testing"
    ],
    "relevance_to_seed": "Demonstrates the full SFT+RL pipeline for training reasoning-augmented retrievers at scale, validating that RL with retrieval-specific rewards can improve dense retriever quality. The retrieval-accuracy reward (rank-based) is an outcome reward — our learned reasoning-quality reward model would provide richer signal specifically for reasoning-intensive queries where LREM's keyword CoT may be insufficient."
  },
  {
    "title": "Q-RAG: Long Context Multi-Step Retrieval via Value-Based Embedder Training",
    "venue": "ICLR 2026 (Oral)",
    "problem_identification": "Existing multi-step retrievers require expensive LLM fine-tuning or agent orchestration. Q-RAG identifies that retrieval chunk selection can be formulated as a sequential decision problem solvable entirely within the embedding space, avoiding LLM training costs.",
    "key_insight": "The retriever embedder itself can serve as the RL policy via factorized Q-values Q(s,a)=⟨E_s(s),E_a(a)⟩, making the inner product between state and action embeddings the value function — no separate policy network or LLM fine-tuning needed.",
    "innovation_type": "new_formulation",
    "method_summary": "Models multi-step retrieval as a finite-horizon MDP where states are ordered retrieved chunks, actions are remaining chunks, and rewards are sparse terminal signals (all support facts retrieved). Trains state/action embedders via PQN (on-policy value-based RL with λ-returns) to estimate Q-values through their inner product. Uses Boltzmann exploration with annealed temperature and rotary position embeddings for document-position awareness. All training fits on a single A100 GPU.",
    "limitations_and_open_questions": "Relies on sparse terminal reward from gold support-fact labels, not learned reward signals; authors explicitly note LLM-based rewards as unexplored future work. Evaluation focuses on long-context needle-retrieval (BabiLong/RULER) rather than reasoning-intensive benchmarks like BRIGHT.",
    "building_blocks": [
      "Factorized Q-value inner-product architecture for retriever",
      "PQN algorithm avoiding replay buffer for embedding-space RL",
      "MDP formulation of multi-step retrieval with chunk-level actions",
      "Rotary position embedding for document-order awareness"
    ],
    "relevance_to_seed": "Closest architectural precedent for our RL-trained retriever — demonstrates the retriever-as-policy paradigm works, but uses heuristic support-fact rewards instead of a learned reasoning-quality reward model, leaving exactly the gap our proposal fills."
  },
  {
    "title": "Agentic-R: Learning to Retrieve for Agentic Search",
    "venue": "arXiv 2026",
    "problem_identification": "Similarity-based retrievers fail in agentic search because similar passages may not help answer generation. Identified that retriever training must account for both local query-passage relevance AND global downstream answer correctness.",
    "key_insight": "Retriever and agent quality are coupled — better retrievers yield better agent queries, and better agent queries yield better retriever training data — so bidirectional iterative co-optimization outperforms training either component in isolation.",
    "innovation_type": "combination",
    "method_summary": "Defines dual utility signals: local relevance (LLM listwise scoring, 0-100) and global answer correctness (binary EM from agent continuation). Ranks passages by GAC then LR to construct contrastive training pairs. Alternates between PPO-based agent training (with retrieved-token masking) and contrastive retriever fine-tuning using evolving agent-generated queries. Converges in ~2 iterations. Retriever input concatenates original question with current-turn query.",
    "limitations_and_open_questions": "Global utility is binary EM — cannot distinguish documents that aid reasoning from those containing the answer string. Evaluated only on standard QA benchmarks (HotpotQA, 2WikiMHQA, etc.), not reasoning-intensive retrieval. The iterative loop requires full agent rollouts per retriever training round, raising compute costs.",
    "building_blocks": [
      "Dual local/global utility signal framework",
      "Bidirectional iterative agent-retriever co-optimization loop",
      "LLM listwise relevance scoring for passage ranking",
      "Retrieved-token masking for agent PPO training"
    ],
    "relevance_to_seed": "Primary baseline — demonstrates utility-based retriever training works but uses heuristic EM as global signal. Our learned reward model replaces binary EM with reasoning-chain quality assessment, targeting the exact limitation that EM conflates answer-containing with reasoning-helpful documents."
  },
  {
    "title": "Search-R1: Training LLMs to Reason and Leverage Search Engines with Reinforcement Learning",
    "venue": "COLM 2025",
    "problem_identification": "Prompting LLMs with reasoning capabilities to use search engines is suboptimal because the LLM lacks trained search-interaction skills. Prior work either fine-tunes on curated search trajectories (imitation) or uses no training at all (prompting).",
    "key_insight": "Simple outcome-based RL rewards (binary EM) plus retrieved-token masking are sufficient for LLMs to learn complex multi-turn search behaviors emergently — no process supervision, no curated trajectories, no neural reward models needed.",
    "innovation_type": "simplification",
    "method_summary": "Extends GRPO/PPO with a search-engine environment: the LLM generates &lt;search>query&lt;/search> tokens to trigger retrieval, receiving results in &lt;information> tags. Retrieved token masking zeroes out gradients for all non-LLM-generated tokens, preventing optimization of retrieval content. Uses pure outcome-based EM reward. Observes emergent behaviors: self-verification searches, increasing search frequency during training, and length dynamics (initial decrease, then strategic increase).",
    "limitations_and_open_questions": "Trains the LLM generator, not the retriever — the retriever is frozen BM25/dense. Outcome-only rewards cannot provide credit assignment for individual search decisions, limiting performance on complex multi-hop tasks. Authors acknowledge process/format rewards as unexplored future work.",
    "building_blocks": [
      "Retrieved token masking for stable RL with external knowledge",
      "Outcome-based reward sufficiency for search behavior emergence",
      "Multi-turn search-reasoning interleaving framework",
      "GRPO vs PPO comparison for search-augmented training"
    ],
    "relevance_to_seed": "Establishes the RL-for-search paradigm our work extends, but trains the LLM not the retriever. Its retrieved-token masking technique is directly reusable. Its acknowledged limitation — outcome-only rewards lack credit assignment — is precisely what our process-aware reasoning-quality reward model addresses."
  },
  {
    "title": "ReSCORE: Label-free Iterative Retriever Training for Multi-hop Question Answering with Relevance-Consistency Supervision",
    "venue": "ACL 2025 (Main)",
    "problem_identification": "Dense retrievers require labeled query-document pairs, but for multi-hop QA these labels are unavailable because each retrieval iteration generates different queries depending on the LLM. Found that using only P(answer|query,doc) produces false positives from superficial word overlap.",
    "key_insight": "Document utility decomposes into relevance P(query|doc) × consistency P(answer|query,doc), and the relevance term is critical for filtering topically unrelated documents that happen to contain answer strings — addressing exactly the answer-containing vs. reasoning-helpful distinction.",
    "innovation_type": "new_technique",
    "method_summary": "Uses LLM log-probabilities to compute pseudo-ground-truth scores: Q_LM(d|q) ∝ P_LM(q|d) · P_LM(a|q,d). Trains the dense retriever by minimizing KL divergence between the pseudo-GT distribution and retriever softmax scores over top-M candidates. Operates iteratively: retrieve → answer-or-continue → generate thought summary → reformulate query → repeat. Each iteration recomputes pseudo-labels using the improved retriever's candidates.",
    "limitations_and_open_questions": "Requires gold answers for consistency computation, so not truly unsupervised. LLM probability computation over candidates is expensive (M=32 per query per iteration). Not evaluated on reasoning-intensive retrieval — only standard multi-hop QA (HotpotQA, 2WikiMHQA, MuSiQue).",
    "building_blocks": [
      "Relevance × consistency decomposition of document utility",
      "LLM log-probability as pseudo-ground-truth supervision for retrievers",
      "KL-divergence training objective between LLM scores and retriever scores",
      "Iterative query reformulation with thought summarization"
    ],
    "relevance_to_seed": "Validates LLM-as-reward-signal for retriever training and introduces the relevance-consistency decomposition that partially captures our reasoning-utility distinction. However, consistency is still measured against the final answer, not reasoning chain quality — our learned reward model goes further by evaluating intermediate reasoning steps."
  },
  {
    "title": "ProRAG: Process-Supervised Reinforcement Learning for Retrieval-Augmented Generation",
    "venue": "arXiv 2026",
    "problem_identification": "Outcome-based RL for RAG suffers from reward sparsity and process hallucinations — models reach correct answers through flawed reasoning. Sparse scalar rewards cannot pinpoint which intermediate retrieval/reasoning step failed in long-horizon trajectories.",
    "key_insight": "Step-level credit assignment in multi-hop RAG requires combining MCTS-discovered contrastive reasoning pairs (judged by GPT-4o) with dual-granularity advantages that weight process and outcome signals separately, enabling correction of flawed intermediate steps even when final answers are correct.",
    "innovation_type": "combination",
    "method_summary": "Four stages: (1) SFT warmup with structured reasoning format; (2) MCTS exploration to find contrastive sibling-node pairs, judged by GPT-4o, yielding ~8K preference pairs to train a PRM via pairwise ranking loss; (3) rejection sampling fine-tuning filtered by both outcome correctness and PRM score threshold (~105K examples); (4) GRPO with dual-granularity advantage A = A_out + β·A_proc (β=0.3), where process advantage comes from frozen PRM and outcome advantage from EM reward.",
    "limitations_and_open_questions": "Trains the LLM/generator, not the retriever. MCTS exploration and GPT-4o judging are expensive (unclear if fits within 200 H100-hour budget). PRM is trained on reasoning step quality, not document utility — the reward model evaluates reasoning, not retrieval relevance.",
    "building_blocks": [
      "MCTS-based contrastive pair discovery for PRM training",
      "Dual-granularity advantage combining step-level and outcome-level rewards",
      "GPT-4o as logical judge for step validity in preference pair construction",
      "Four-stage training pipeline: SFT → PRM → RFT → RL"
    ],
    "relevance_to_seed": "Closest architecture for our reasoning-utility reward model construction — the MCTS-based PRM training and dual-granularity advantage mechanism can be adapted from evaluating reasoning steps to evaluating document utility for reasoning. Key difference: ProRAG's PRM judges reasoning quality; our reward model judges whether a document improves reasoning quality."
  },
  {
    "title": "ReasonIR: Training Retrievers for Reasoning Tasks",
    "venue": "arXiv 2025 (accepted COLM 2025)",
    "problem_identification": "Existing retrievers fail on reasoning-intensive queries because training data consists of short factual QA pairs (~20 tokens), while reasoning queries average ~194 tokens and require multi-step inference to match documents. A pilot study showed retrievers plateau or degrade beyond ~256 token queries despite supporting longer contexts.",
    "key_insight": "The bottleneck for reasoning-intensive retrieval is training data distribution, not model architecture or context length — retrievers must be trained on long, reasoning-structured query-document pairs where relevance requires inference, not lexical overlap.",
    "innovation_type": "new_technique",
    "method_summary": "Builds a synthetic data pipeline using Llama-3.1-70B producing two data types: Varied-Length (VL) data with 300–2000 word queries and Hard Query (HQ) data targeting higher-order thinking (analysis, synthesis). Hard negatives are generated via multi-turn prompting conditioned on both query and positive, avoiding false negatives from failed BM25 mining. Trains a bi-encoder (Llama-3.1-8B with bidirectional attention) on ~1.73M samples using InfoNCE loss. A simple score interpolation reranker (0.5*reranker + 0.5*retriever) achieves near-SOTA at 200x less compute than reasoning rerankers.",
    "limitations_and_open_questions": "HQ seed documents drawn from BRIGHT corpus raise domain leakage concerns (reviewers flagged this). Coding/theorem domains remain weak (10.5–19.6 nDCG@10). Requires 70B LLM for quality data generation — 8B produces significantly worse negatives. No utility-based or reward-model-based training signal; purely contrastive.",
    "building_blocks": [
      "Synthetic reasoning-intensive query generation pipeline",
      "Multi-turn hard negative generation",
      "Score interpolation reranking",
      "BRIGHT benchmark (29.9 nDCG@10 baseline)",
      "Query rewriting as test-time compute scaling"
    ],
    "relevance_to_seed": "Primary baseline to beat on BRIGHT; demonstrates contrastive training ceiling without reward-based utility signals — our learned reward model targets exactly the gap where synthetic contrastive data cannot distinguish reasoning-helpful from answer-containing documents."
  },
  {
    "title": "RaDeR: Reasoning-aware Dense Retrieval Models",
    "venue": "EMNLP 2025 (Main)",
    "problem_identification": "No first-stage dense retriever performs reasoning for relevance judgment — prior work either uses off-the-shelf retrievers with reasoning-augmented queries (IRCoT, ReAct) or reasoning rerankers (RANK-1) limited by first-stage recall. CoT query augmentation helps BM25 via added terms but fails for dense retrievers lacking reasoning training.",
    "key_insight": "MCTS-based math problem solving naturally generates reasoning-intensive retriever training data: partial solution trajectories become queries, retrieved theorems verified by answer correctness become positives, and self-reflection-rejected theorems become hard negatives — all with automatic relevance labels requiring no human annotation.",
    "innovation_type": "combination",
    "method_summary": "Extends the rStar MCTS framework with Generate-Query and Retrieve-Theorem actions over ProofWiki. High-reward trajectories yield (partial-CoT-query, theorem) training pairs; theorems rejected by LLM self-reflection become hard negatives. Generates three reasoning query types (MCTS-CoT, LLM-reasoning, question) plus lexical queries filtered by round-trip BM25 consistency. Trains bi-encoder retrievers (Qwen2.5 variants) with InfoNCE on only 43K–121K samples.",
    "limitations_and_open_questions": "Single-document reasoning only — cannot handle multi-hop where relevance is interdependent. Math-domain data pipeline requires verifiable answers and structured knowledge bases; extension to other domains is non-trivial. MS MARCO MRR drops from 41.2 to 34.4 vs RepLLaMA, suggesting reasoning-standard retrieval tradeoff.",
    "building_blocks": [
      "MCTS-derived retrieval training data",
      "Self-reflective relevance evaluation as automatic labeling",
      "Answer correctness as proxy relevance signal",
      "Sample-efficient training (2.5% of ReasonIR's data, +1.1 nDCG@10)"
    ],
    "relevance_to_seed": "Demonstrates that answer-correctness reward signals from reasoning trajectories can train effective retrievers with extreme sample efficiency — validates the principle that downstream task performance can supervise retriever training, but uses binary answer correctness rather than a learned reasoning-quality reward model."
  },
  {
    "title": "CoSearch: Joint Training of Reasoning and Document Ranking via Reinforcement Learning for Agentic Search",
    "venue": "arXiv 2026 (in submission)",
    "problem_identification": "Existing agentic search systems (Search-R1) treat retrieval as a frozen tool, optimizing only the reasoning agent. An oracle experiment promoting answer-containing documents to top positions showed 26.8% relative F1 improvement for a 3B agent, proving retrieval quality is a major bottleneck.",
    "key_insight": "The reasoning agent and document ranker are interdependent and must be co-optimized — the agent's sub-queries shape ranker inputs while ranker outputs shape agent reasoning, creating a feedback loop that fixed-retriever training cannot exploit.",
    "innovation_type": "new_formulation",
    "method_summary": "Jointly optimizes a reasoning agent and a generative listwise ranker (both Qwen2.5-7B) via GRPO. The ranker reranks 50 E5-retrieved candidates to top-5. A novel semantic query grouping technique (token-F1 threshold δ=0.8) clusters sub-queries across rollouts to satisfy GRPO's identical-input requirement for the ranker — at zero additional sampling cost. Composite rewards combine Hit@k relevance (when answer-containing docs exist) with trajectory-level F1 (always), with a threshold γ=0.5 governing the mixture.",
    "limitations_and_open_questions": "First-stage retriever (E5) remains frozen, capping recall. Evaluated only on QA benchmarks with Wikipedia corpus — no reasoning-intensive benchmarks like BRIGHT. Pseudo-relevance labels (string match for answer) conflate answer-containing with reasoning-helpful documents. 3B ranker caused training divergence, suggesting minimum capacity requirements.",
    "building_blocks": [
      "Semantic query grouping for GRPO on rankers",
      "Composite relevance + trajectory rewards",
      "Oracle retrieval experiments to quantify retrieval bottleneck",
      "Joint agent-ranker RL framework"
    ],
    "relevance_to_seed": "Closest architectural parallel to our proposal — applies RL rewards to train a retrieval component — but uses answer-correctness rewards (binary F1) rather than learned reasoning-quality rewards, and trains a reranker rather than the dense retriever itself. Validates that RL-based retrieval training improves agentic search but does not address the reasoning-utility distinction."
  },
  {
    "title": "RAG-RewardBench: Benchmarking Reward Models in Retrieval Augmented Generation for Preference Alignment",
    "venue": "ACL 2025 (Findings)",
    "problem_identification": "Existing RM benchmarks (RewardBench) evaluate only general scenarios with ~47-token prompts, completely missing RAG-specific challenges. Models scoring 90%+ on RewardBench drop to 78.3% on RAG tasks. No benchmark existed to assess RMs on multi-hop reasoning, citation quality, abstention, or conflict robustness in RAG contexts.",
    "key_insight": "Trained RALMs (Self-RAG, ChatQA, FgCite) show almost no preference alignment improvement over base models (0.4–2.8%) despite large accuracy gains on RAG tasks — current RALM training optimizes task accuracy but completely fails to align with human preferences for citation, abstention, and robustness.",
    "innovation_type": "new_benchmark",
    "method_summary": "Constructs 1,485 preference pairs across 18 datasets in 4 RAG-specific scenarios (multi-hop reasoning, fine-grained citation, appropriate abstention, conflict robustness). Uses 24 RALMs for response generation, 6 diverse retrievers, and 4 commercial LLM judges scoring 5 dimensions. Consistency filtering and difficulty calibration (1–2 point score gaps) ensure quality. Evaluates 45 RMs spanning discriminative, generative, and implicit (DPO) types.",
    "limitations_and_open_questions": "Evaluates only outcome-level preferences, not process-level reasoning quality. LLM-as-judge dependency may introduce systematic biases. Static benchmark of 1,485 pairs risks saturation. The benchmark identifies the RM gap for RAG but proposes no solution — designing RAG-specialized RMs remains open.",
    "building_blocks": [
      "RAG-specific RM evaluation taxonomy (4 scenarios, 18 subsets)",
      "LLM-as-judge annotation pipeline with consistency filtering",
      "Evidence that implicit RMs (DPO) fail in RAG contexts",
      "Baseline RM performance data for RAG reward modeling"
    ],
    "relevance_to_seed": "Directly validates our premise that existing RMs are inadequate for RAG-specific evaluation and that a specialized learned reward model is needed. The multi-hop reasoning and citation scenarios provide evaluation methodology for our reasoning-utility reward model, and the finding that RALMs fail at preference alignment motivates reward-model-driven training."
  },
  {
    "title": "Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection",
    "venue": "ICLR 2024 (Oral, top 1%)",
    "problem_identification": "Indiscriminate retrieval in RAG systems hurts performance — ChatGPT with retrieval scores worse than without on several tasks. Additionally, no mechanism ensures generated text is faithful to retrieved evidence. The gap is both when-to-retrieve and how-to-verify-grounding.",
    "key_insight": "Retrieval decisions and output quality assessment can be distilled into the LM itself as special reflection tokens (Retrieve, IsRel, IsSup, IsUse), trained via standard next-token prediction on critic-augmented data — eliminating the need for separate runtime components or expensive online RL.",
    "innovation_type": "new_formulation",
    "method_summary": "Trains a critic model (Llama2-7B) on GPT-4-labeled examples to predict 4 reflection token types. Uses this critic offline to augment 150K training examples with inline reflection tokens. Trains the generator on augmented sequences where retrieved passages are masked in loss computation. At inference, segment-level beam search scores candidates using both generation probability and reflection token probabilities, with user-adjustable weights enabling per-task controllability without retraining.",
    "limitations_and_open_questions": "Evaluates single-passage selection only — no cross-passage synthesis (reviewer 4MCy). Reflection tokens are post-hoc selectors, not generation guides. Computational overhead of segment-level beam search with multiple passages. Retriever (Contriever) remains frozen and off-the-shelf, bounding recall quality.",
    "building_blocks": [
      "Reflection token paradigm for learned self-evaluation in RAG",
      "Critic-based offline data augmentation (avoiding online RL)",
      "Inference-time controllability via reflection token weights",
      "Segment-level beam search with critique scoring"
    ],
    "relevance_to_seed": "Foundational paradigm for learned evaluation signals in RAG — our reasoning-utility reward model extends the reflection token concept from generation-quality evaluation to document-utility evaluation for retriever training. Self-RAG's IsRel/IsSup tokens evaluate 'does this passage support generation' while our reward model would evaluate 'does this document improve reasoning chain quality' — a complementary but distinct signal."
  },
  {
    "title": "ReasonEmbed: Enhanced Text Embeddings for Reasoning-Intensive Document Retrieval",
    "venue": "ACL 2026 (Main)",
    "problem_identification": "Identified the 'triviality problem' in synthetic retrieval training data: existing datasets (including ReasonIR's) exhibit surface-level query-document overlap that can be solved by lexical matching rather than reasoning, yielding only marginal gains on BRIGHT. Diagnosed empirically by showing high ROUGE overlap correlates with poor nDCG@10 (14.5 vs. 37.1).",
    "key_insight": "Source documents used as positives in synthetic data create trivial training signal; excluding them and mining semantically-correlated-but-lexically-distinct positives forces models to learn reasoning-based matching.",
    "innovation_type": "combination",
    "method_summary": "ReMixer is a 3-stage data synthesis pipeline: (1) conditioned query generation from BRIGHT domains via Qwen2.5-72B with explicit reasoning requirements, (2) source-excluded candidate mining that retrieves positives different in form but correlated in essence, and (3) reasoning-enhanced relevance annotation via a distilled Qwen3-8B annotator trained on Qwen3-235B reasoning traces. Redapter dynamically reweights training via RI-InfoNCE: reasoning intensity RI(s) = min(L_q,D / L_q',D, κ) compares contrastive loss with/without reasoning-augmented queries, upweighting samples where reasoning matters most. Trained with LoRA on Qwen3-8B backbone, single epoch, 82K samples.",
    "limitations_and_open_questions": "Relies entirely on synthetic data quality rather than learning utility signals from downstream reasoning performance; Redapter's RI metric requires reasoning-augmented query rewrites at training time. Does not address whether gains transfer beyond embedding-only retrieval to full RAG pipelines.",
    "building_blocks": [
      "ReMixer source-excluded mining pipeline",
      "RI-InfoNCE adaptive weighting by reasoning intensity",
      "Distilled relevance annotator from reasoning traces",
      "82K reasoning-intensive training dataset across 12 domains"
    ],
    "relevance_to_seed": "Sets the BRIGHT SOTA at 38.1 nDCG@10 — our primary evaluation target; its data-centric approach (better training data) is complementary to our reward-model approach (better training signal), and Redapter's reasoning-intensity metric could inform our reward model design."
  },
  {
    "title": "RM-R1: Reward Modeling as Reasoning",
    "venue": "ICLR 2026",
    "problem_identification": "Observed that scalar reward models produce opaque numeric scores and generative RMs produce shallow free-form judgments — neither performs structured reasoning over evaluation criteria. This limits both interpretability and performance on complex preference judgments.",
    "key_insight": "Reward modeling should be formulated as a reasoning task: the model first self-generates task-specific evaluation rubrics (for chat) or solves the problem itself (for reasoning), then systematically evaluates against these criteria — making the evaluation process itself a structured reasoning chain.",
    "innovation_type": "new_formulation",
    "method_summary": "Chain-of-Rubrics (CoR) categorizes inputs as Chat or Reasoning; for Chat, the model generates weighted rubrics in &lt;rubric> tags then evaluates responses against them; for Reasoning, it first solves the problem in &lt;solution> tags then judges correctness. Training is two-phase: (1) distillation from oracle models (Claude-3.7-Sonnet, O3) on ~8.7K samples to bootstrap structured reasoning traces, then (2) GRPO on 64K preference data with a simple binary verifiable reward (correct label = +1, wrong = -1). Evaluated on Qwen-2.5-Instruct and DeepSeek-Distilled-Qwen at 7B-32B scales.",
    "limitations_and_open_questions": "Reward is purely binary (correct/incorrect label), missing opportunities for granular quality signals; CoR mechanism adds inference cost from generating rubrics/solutions before scoring. Untested on document-level utility evaluation — only applied to response preference, not retrieval contexts.",
    "b
... (truncated)

## Your task

Synthesize these paper analyses into a **Field Guide** — a strategic document that would help a researcher generate novel, high-quality ideas in this area. This is NOT a survey — it's an opinionated strategy guide for innovation.

Think about:
- What PATTERNS OF INNOVATION keep working in this field?
- What do reviewers consistently reward?
- Where are the real gaps (not assumed gaps)?
- What combinations haven't been tried?
- What mistakes should we avoid?

## Output format

Output a JSON object with these sections:
{
  "innovation_patterns": [
    {"pattern": "name", "description": "how it works", "examples": ["paper1", "paper2"], "success_rate": "high/medium/low"}
  ],
  "reviewer_preferences": [
    "What reviewers in this area consistently care about (based on evidence from paper analyses)"
  ],
  "field_gaps": [
    {"gap": "description of unsolved problem", "evidence": "which papers mention this limitation", "difficulty": "high/medium/low", "impact_if_solved": "high/medium/low"}
  ],
  "untried_combinations": [
    {"idea_sketch": "what could be combined", "from_papers": ["which papers inspire this"], "why_promising": "reason"}
  ],
  "method_building_blocks": [
    {"tool": "name", "what_it_does": "description", "used_by": ["papers"], "could_be_applied_to": "new application"}
  ],
  "common_pitfalls": [
    "Mistakes to avoid when working in this area (based on reviewer feedback and paper limitations)"
  ],
  "field_trajectory": "Where is this field heading? What are the 2-3 most promising macro-directions? (paragraph)",
  "meta_advice": "If you were advising a PhD student to write a strong 2026 paper in this area, what would you tell them? (paragraph)"
}

Be specific and evidence-based — every claim should reference specific papers from the analyses. Avoid generic advice like 'be novel' — instead say 'Papers that combine X with Y for task Z have been getting accepted (see Paper A, Paper B).'.

IMPORTANT: You MUST end your response with the JSON object.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "ca776cc5-7161-4cab-b90a-0e168cc3e940",
  "type": "user",
  "uuid": "46f0e687-3d71-45bf-917d-1d9c0c135fb5",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "6725a028-3696-49b3-b2c2-a8f4330dd39d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-30T06:35:15.834Z_

```json
{
  "parentUuid": "46f0e687-3d71-45bf-917d-1d9c0c135fb5",
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
  "uuid": "c249411c-6be9-446e-bdd8-8607b24bfa94",
  "timestamp": "2026-05-30T06:35:15.834Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "6725a028-3696-49b3-b2c2-a8f4330dd39d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-30T06:35:15.834Z_

```json
{
  "parentUuid": "c249411c-6be9-446e-bdd8-8607b24bfa94",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "0d665936-4c2e-4f20-91e6-a2dd78bcc336",
  "timestamp": "2026-05-30T06:35:15.834Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "6725a028-3696-49b3-b2c2-a8f4330dd39d",
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
  "lastPrompt": "You are a senior ML research advisor synthesizing a literature review into an actionable research strategy.  **Today's date: 2026-05-30 (UTC).**  ## Research area: Target: AAAI 2026 Track: Information…",
  "leafUuid": "0d665936-4c2e-4f20-91e6-a2dd78bcc336",
  "sessionId": "6725a028-3696-49b3-b2c2-a8f4330dd39d"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Design reasoning-quality reward model for retriever training",
  "sessionId": "6725a028-3696-49b3-b2c2-a8f4330dd39d"
}
```

---

### Assistant

_source line 8 · 2026-05-30T06:35:32.289Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to synthesize 19 paper analyses into a strategic "Field Guide" for generating novel research ideas in the area of reasoning-intensive retrieval with learned reward models. Let me carefully analyze all the papers and produce a comprehensive, evidence-based JSON output.

Let me organize my thinking:

**Innovation Patterns:**
1. Cross-domain transfer of RL/reward techniques (from math reasoning to retrieval)
2. Replacing heuristic signals with learned ones
3. Data-centric approaches (better training data > better architectures)
4. Process-level rewards over outcome-level rewards
5. Unified architectures (combining previously separate components)


6. Elegant simplifications that outperform complexity

**Reviewer Preferences:**
- Strong baselines and ablations
- Evaluation on challenging benchmarks (not just easy ones)
- Compute efficiency
- Novel formulations over incremental improvements
- Clear distinction from prior work

**Field Gaps:**
- No learned reward model for document utility in reasoning
- No utility-based retriever evaluated on BRIGHT
- Reasoning-utility vs answer-utility distinction unformalized
- Cross-domain generalization of utility-based training
- Process rewards for retriever (not LLM) training

**Untried Combinations:**
- ThinkPRM + retriever training
- MCTS-based reward model combined with continuous optimization for retriever training
- Q-RAG's MDP formulation paired with learned reasoning rewards
- ReasonEmbed's data leveraged with reward-model training signals

**Method Building Blocks:**
- Perturbation-based utility attribution (SCARLet)
- MCTS exploration for preference pairs (ProRAG, RaDeR)
- Factorized Q-value architecture (Q-RAG)
- Retrieved-token masking (Search-R1)
- Force-decode scoring (ThinkPRM)
- Dual-granularity advantages (ProRAG)

**Common Pitfalls:**
- Training the LLM instead of the retriever
- Using binary EM as the only signal
- Evaluating only on easy QA benchmarks
- Domain-specific methods that don't transfer
- Compute costs that exceed budgets

Now I'm compiling this into a structured JSON output.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0d665936-4c2e-4f20-91e6-a2dd78bcc336",
  "isSidechain": false,
  "requestId": "req_011CbYHinckqErgjHyZk143n",
  "type": "assistant",
  "uuid": "55936b6b-e1c4-4878-9ba9-4292cd47845b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "6725a028-3696-49b3-b2c2-a8f4330dd39d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Gn9TWkdDa5inJ9moyv7q4p",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12628,
      "cache_read_input_tokens": 11014,
      "output_tokens": 7637,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12628,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 7637,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 12628,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12628
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

_source line 9 · 2026-05-30T06:38:26.907Z_

I'll analyze all 19 papers systematically to produce the Field Guide. Let me first review the remaining paper analyses that were truncated to ensure completeness.

Given the depth of the paper analyses provided, I can now synthesize the strategic Field Guide. Here is my synthesis:

```json
{
  "innovation_patterns": [
    {
      "pattern": "Heuristic-to-Learned Signal Upgrade",
      "description": "Take an existing pipeline that uses a hand-designed or proxy signal (binary EM, BM25 negatives, perturbation attribution) and replace it with a learned model that captures richer structure. The learned model is typically trained on a small amount of high-quality data, often synthetic, and generalizes better than the heuristic it replaces.",
      "examples": ["ThinkPRM (replaces 800K human labels with ~1K filtered synthetic chains)", "RM-R1 (replaces scalar reward with structured chain-of-rubrics reasoning)", "ReSCORE (replaces gold labels with LLM log-probability pseudo-labels)", "Self-RAG (replaces retrieval heuristics with learned reflection tokens)"],
      "success_rate": "high"
    },
    {
      "pattern": "Process-Level Decomposition of Outcome Rewards",
      "description": "Take a task evaluated by a single terminal reward (answer correctness) and decompose it into per-step rewards at natural pipeline boundaries. Train with dual-granularity advantages combining step-level and outcome-level signals. Consistently outperforms pure outcome RL by enabling credit assignment.",
      "examples": ["ReasonRAG (three-stage RAG decomposition with MCTS-based SPRE)", "ProRAG (dual-granularity advantage A_out + β·A_proc with MCTS-trained PRM)", "CoSearch (composite Hit@k + trajectory F1 rewards)"],
      "success_rate": "high"
    },
    {
      "pattern": "Data-Centric Reasoning Gap Closure",
      "description": "Instead of architectural innovation, diagnose that the training data distribution is the bottleneck (e.g., short factoid pairs vs. long reasoning queries) and engineer synthetic data that matches the target distribution. Often achieves SOTA with standard architectures and modest compute.",
      "examples": ["ReasonIR (synthetic VL+HQ data closes reasoning retrieval gap)", "ReasonEmbed (source-excluded mining + RI-InfoNCE achieves 38.1 nDCG@10 on BRIGHT)", "RaDeR (MCTS-derived training data with 2.5% of ReasonIR's volume, +1.1 nDCG@10)"],
      "success_rate": "high"
    },
    {
      "pattern": "RL Formulation of Retrieval as Sequential Decision-Making",
      "description": "Recast retrieval (or multi-step retrieval) as an MDP where document selection actions yield rewards from downstream task performance, enabling policy-gradient or value-based RL training of the retriever itself. Key enablers: factorized Q-values in embedding space, GRPO with retrieval-specific rewards.",
      "examples": ["Q-RAG (factorized Q-value MDP for chunk retrieval, ICLR 2026 Oral)", "LREM (GRPO with retrieval-accuracy reward, deployed on Taobao)", "CoSearch (GRPO for joint agent-ranker optimization)"],
      "success_rate": "medium"
    },
    {
      "pattern": "Unified Reasoning-Embedding Architecture",
      "description": "Merge previously separate reasoning (CoT generation) and embedding (vector representation) stages into a single model with shared parameters, using special tokens to delineate reasoning and embedding phases. Avoids pipeline error propagation and enables end-to-end optimization.",
      "examples": ["LREM (unified &lt;think>CoT&lt;/think>&lt;emb> architecture with GRPO)", "ReasonEmbed (reasoning-enhanced relevance annotation distilled into embeddings)"],
      "success_rate": "medium"
    },
    {
      "pattern": "Iterative Co-Optimization of Coupled Components",
      "description": "When two components are interdependent (retriever/agent, retriever/ranker), alternate training rounds between them so each component improves the training signal for the other. Converges in 2-3 iterations and outperforms training either in isolation.",
      "examples": ["Agentic-R (bidirectional agent-retriever co-optimization, converges in ~2 iterations)", "ReSCORE (iterative pseudo-label refinement as retriever improves)", "CoSearch (joint agent-ranker GRPO)"],
      "success_rate": "medium"
    }
  ],
  "reviewer_preferences": [
    "Strong ablations that isolate the contribution of each component — Q-RAG's oral acceptance at ICLR 2026 featured systematic MDP formulation ablations; ReasonRAG at NeurIPS 2025 directly compared process vs. outcome rewards with controlled experiments.",
    "Evaluation on genuinely challenging benchmarks, not just saturated ones — BRIGHT papers consistently earn higher reviewer scores than those evaluating only on HotpotQA/2WikiMHQA; ReasonEmbed's acceptance at ACL 2026 was driven by BRIGHT SOTA results.",
    "Compute efficiency and reproducibility — RaDeR achieved competitive results with 2.5% of ReasonIR's training data; ThinkPRM used only ~1K training examples vs. PRM800K's 800K; Q-RAG trained on a single A100. Reviewers penalize methods requiring unstated compute budgets (e.g., ProRAG's MCTS + GPT-4o costs were flagged).",
    "Clear formalization of the problem being solved — Q-RAG (ICLR Oral) formalized retrieval as a finite-horizon MDP; RM-R1 (ICLR 2026) formalized reward modeling as reasoning. Papers with novel formalizations consistently outperform papers with only engineering contributions.",
    "Real-world or production validation — LREM's deployment on Taobao with A/B test results (+7-16% online improvement) significantly strengthened an otherwise incremental architecture paper.",
    "Honest limitation analysis — BRIGHT reviewers flagged that ReasonIR's use of BRIGHT corpus documents as seeds created potential data leakage; SCARLet reviewers appreciated the honest reporting of code domain failures (-11.9 points). Hiding weaknesses backfires.",
    "Novel, non-obvious insights validated empirically — ReasonEmbed's 'triviality problem' diagnosis (high ROUGE overlap → poor nDCG@10) was the key differentiator from ReasonIR; ReSCORE's relevance × consistency decomposition was praised for explaining why P(answer|query,doc) alone produces false positives."
  ],
  "field_gaps": [
    {
      "gap": "No learned reward model evaluates document utility for reasoning chain quality (as opposed to binary answer correctness or perturbation-based heuristics)",
      "evidence": "SCARLet uses perturbation attribution (64 forward passes, heuristic); Agentic-R uses binary EM (cannot distinguish reasoning-helpful from answer-containing documents); Q-RAG authors explicitly note 'LLM-based rewards as unexplored future work'; ReSCORE uses LLM log-probabilities as pseudo-labels but still conditions on final answer, not reasoning chain quality",
      "difficulty": "medium",
      "impact_if_solved": "high"
    },
    {
      "gap": "No utility-based retriever training method has been evaluated on BRIGHT (reasoning-intensive retrieval benchmark)",
      "evidence": "Agentic-R evaluated only on HotpotQA/2WikiMHQA; SCARLet evaluated on KILT/ASQA/QAMPARI; ReasonRAG evaluated on factoid QA with Wikipedia; CoSearch evaluated on QA benchmarks; Q-RAG evaluated on BabiLong/RULER. All utility-based methods avoid BRIGHT.",
      "difficulty": "low",
      "impact_if_solved": "high"
    },
    {
      "gap": "Process reward models exist for reasoning step verification but not for document-level utility assessment — no PRM evaluates 'does this document improve reasoning' rather than 'is this reasoning step correct'",
      "evidence": "ThinkPRM evaluates reasoning step correctness; ProRAG's PRM judges step validity; RM-R1 evaluates response quality. RAG-RewardBench explicitly shows existing RMs drop from 90%+ to 78.3% on RAG tasks and identifies 'designing RAG-specialized RMs' as an open problem.",
      "difficulty": "medium",
      "impact_if_solved": "high"
    },
    {
      "gap": "Cross-domain generalization of reasoning-intensive retriever training — current methods fail on code, theorem proving, and specialized domains",
      "evidence": "SCARLet fails on code domain (up to -11.9 point drops); ReasonIR's coding/theorem domains remain weak (10.5–19.6 nDCG@10); RaDeR is math-only with non-trivial domain extension; ReasonEmbed achieves strong average but domain-specific variance is unreported.",
      "difficulty": "high",
      "impact_if_solved": "medium"
    },
    {
      "gap": "RL-based training of the dense retriever itself (not the LLM, not a reranker) using downstream reasoning signals remains nearly unexplored",
      "evidence": "Search-R1 trains LLM (retriever frozen BM25/dense); ReasonRAG trains LLM (BGE frozen); ProRAG trains LLM; CoSearch trains a reranker but freezes the first-stage retriever (E5). Only Q-RAG and LREM train a retriever via RL, but Q-RAG uses heuristic support-fact rewards and LREM uses rank-based outcome rewards, neither using learned reasoning-quality signals.",
      "difficulty": "medium",
      "impact_if_solved": "high"
    },
    {
      "gap": "Formalizing the distinction between 'document that contains the answer' vs. 'document that aids the reasoning process' — current utility signals conflate these",
      "evidence": "Agentic-R's binary EM treats both identically; CoSearch's pseudo-relevance labels use string match for answer presence; ReSCORE's consistency metric P(answer|query,doc) rewards documents containing answer strings. BRIGHT's gold annotations distinguish reasoning-mediated relevance but this distinction hasn't been operationalized as a training signal.",
      "difficulty": "medium",
      "impact_if_solved": "high"
    },
    {
      "gap": "Multi-document reasoning utility — all current methods evaluate documents independently, missing inter-document synergies where two individually low-utility documents combine to enable reasoning",
      "evidence": "SCARLet explicitly identifies inter-passage synergy as a known limitation of independent evaluation; Self-RAG evaluates single-passage selection only (reviewer 4MCy flagged this); RaDeR handles only single-document reasoning.",
      "difficulty": "high",
      "impact_if_solved": "medium"
    }
  ],
  "untried_combinations": [
    {
      "idea_sketch": "ThinkPRM-style generative process verification adapted as a document-utility reward model: instead of verifying 'is this reasoning step correct?', verify 'does adding this document improve reasoning chain quality?' — then use this reward model to train dense retrievers via contrastive learning or RL (à la Q-RAG's MDP formulation)",
      "from_papers": ["ThinkPRM", "Q-RAG", "ProRAG", "SCARLet"],
      "why_promising": "ThinkPRM achieves strong PRM performance with only ~1K training examples, suggesting a document-utility PRM could be similarly data-efficient. Q-RAG proves retriever-as-RL-policy works with heuristic rewards; replacing those with a learned ThinkPRM-style reward model fills the exact gap Q-RAG's authors identified. ProRAG's MCTS-based contrastive pair discovery provides the training data construction method for the reward model."
    },
    {
      "idea_sketch": "ReasonEmbed's source-excluded mining + RI-InfoNCE combined with a learned reasoning-utility reward for hard negative selection: instead of using BM25/dense retrieval to find hard negatives, use a reasoning-utility reward model to identify documents that are semantically similar but reasoning-unhelpful (high relevance, low utility) as maximally informative hard negatives",
      "from_papers": ["ReasonEmbed", "SCARLet", "ReasonIR"],
      "why_promising": "ReasonEmbed achieves BRIGHT SOTA (38.1) through better data; ReasonIR generates hard negatives via multi-turn prompting but these are still based on surface properties. A reward-model-informed hard negative selection would produce negatives that are specifically calibrated against the reasoning-utility distinction, combining the data-centric success pattern with the learned-signal success pattern."
    },
    {
      "idea_sketch": "ReSCORE's relevance × consistency decomposition extended with a third factor: reasoning contribution = P(query|doc) × P(answer|query,doc) × P(reasoning_quality|query,doc,chain), where the third factor is a learned reward model that evaluates how a document changes intermediate reasoning steps, not just the final answer",
      "from_papers": ["ReSCORE", "ThinkPRM", "ReasonRAG"],
      "why_promising": "ReSCORE's two-factor decomposition already shows that relevance filtering improves over consistency-only scoring. Adding reasoning contribution as a third factor captures the signal that neither relevance nor consistency addresses: documents that don't contain the answer but provide explanatory scaffolding for multi-step reasoning. ReasonRAG's empirical evidence that process rewards outperform outcome rewards (+1.6 EM) directly supports this extension."
    },
    {
      "idea_sketch": "Agentic-R's bidirectional agent-retriever co-optimization loop, but replacing the binary EM global utility signal with ProRAG's dual-granularity advantage (process + outcome), and evaluating on BRIGHT instead of standard QA benchmarks",
      "from_papers": ["Agentic-R", "ProRAG", "BRIGHT"],
      "why_promising": "Agentic-R demonstrates the co-optimization framework works but is limited by its binary EM signal on standard QA. ProRAG shows process rewards outperform outcome rewards for RAG. BRIGHT is the unsaturated benchmark where reasoning-utility signals should show the largest differential over heuristic signals. This combination attacks all three identified gaps simultaneously."
    },
    {
      "idea_sketch": "Self-RAG's reflection token paradigm applied to retriever training: train the retriever to produce utility reflection tokens (IsReasoningHelpful, ImprovesChainQuality) alongside embeddings, and use these tokens as self-generated reward signals during contrastive training — a self-supervised reward model that doesn't require a separate RM",
      "from_papers": ["Self-RAG", "LREM", "RM-R1"],
      "why_promising": "Self-RAG shows reflection tokens can be distilled with modest supervision; LREM shows reasoning and embedding can coexist in a single model; RM-R1 shows reward modeling benefits from structured reasoning. A retriever that generates its own reasoning-utility assessments would eliminate the separate reward model training stage, reducing pipeline complexity and compute requirements."
    },
    {
      "idea_sketch": "RaDeR's MCTS-derived training data pipeline generalized beyond math: use MCTS exploration on reasoning-intensive tasks from BRIGHT domains (StackExchange, LeetCode, AoPS) where the LLM reasons with/without candidate documents, and trajectories that reach correct answers identify reasoning-helpful documents while self-reflection-rejected documents become hard negatives. Train a reward model on these MCTS-annotated (document, reasoning_quality_delta) pairs.",
      "from_papers": ["RaDeR", "BRIGHT", "ProRAG"],
      "why_promising": "RaDeR achieves extreme sample efficiency (43K–121K samples, 2.5% of ReasonIR) through MCTS-derived data in math. BRIGHT provides the domains and queries; ProRAG's MCTS framework for contrastive pair discovery scales to RAG. The key insight is that MCTS naturally produces the counterfactual data needed to train a reasoning-utility reward model: the same query with different document subsets yields different reasoning quality, providing direct supervision."
    }
  ],
  "method_building_blocks": [
    {
      "tool": "Perturbation-based utility attribution (modified LIME)",
      "what_it_does": "Samples binary inclusion/exclusion vectors over passage sets, measures generator logit fluctuations, fits ridge regression to obtain per-passage utility coefficients. Removes LIME's semantic distance weighting since utility ≠ proximity.",
      "used_by": ["SCARLet"],
      "could_be_applied_to": "Generating ground-truth utility labels for training a reasoning-utility reward model — instead of manually labeling documents as reasoning-helpful, perturbation attribution over reasoning chain quality (not just answer probability) could automatically generate utility labels at scale."
    },
    {
      "tool": "MCTS-based contrastive pair discovery",
      "what_it_does": "Explores the reasoning/retrieval decision tree via Monte Carlo Tree Search, then extracts preference pairs from sibling nodes with differing outcome quality. Provides automatic process-level supervision without human annotation.",
      "used_by": ["ProRAG", "RaDeR", "ReasonRAG"],
      "could_be_applied_to": "Constructing training data for a document-utility reward model — MCTS over document selection (include/exclude candidates) with reasoning quality as terminal reward would produce (document_set, reasoning_chain, quality_delta) triples that directly train a reward model to predict document utility for reasoning."
    },
    {
      "tool": "Factorized Q-value inner-product architecture",
      "what_it_does": "Decomposes Q(state, action) = ⟨E_s(state), E_a(action)⟩ so the retriever's embedding inner product serves as the RL value function. Enables RL training entirely in embedding space without a separate policy network.",
      "used_by": ["Q-RAG"],
      "could_be_applied_to": "RL-based retriever training with learned reasoning-utility rewards — the factorized architecture makes the retriever trainable via policy gradient methods while keeping inference as a simple inner-product search, maintaining retrieval efficiency."
    },
    {
      "tool": "Retrieved-token masking",
      "what_it_does": "Zeroes out gradients for all non-model-generated tokens (retrieved passages, search results) during RL training, preventing optimization of retrieval content and ensuring the policy learns to use retrieval rather than memorize retrieved text.",
      "used_by": ["Search-R1", "Agentic-R"],
      "could_be_applied_to": "When using LLM-generated reasoning chains as reward signal for retriever training, retrieved-token masking ensures the reward model evaluates the LLM's reasoning quality given the document, not the document content itself — critical for preventing reward hacking."
    },
    {
      "tool": "Generative process verification via long CoT (force-decode scoring)",
      "what_it_does": "Generates a long verification chain-of-thought, then force-decodes a judgment token to extract P(positive)/P(negative) as a calibrated score. Supports parallel scaling (K independent chains) and sequential scaling (budget forcing).",
      "used_by": ["ThinkPRM"],
      "could_be_applied_to": "Document-utility scoring — generate a verification CoT that reasons about whether a document would help answer a query through improved reasoning (not just containing the answer), then force-decode a utility judgment. The test-time compute scaling enables trading off reward model quality vs. cost."
    },
    {
      "tool": "Reasoning-intensity adaptive weighting (RI-InfoNCE)",
      "what_it_does": "Computes a per-sample reasoning intensity score RI(s) = min(L_q,D / L_q',D, κ) comparing contrastive loss with/without reasoning-augmented queries, then upweights training loss for samples where reasoning matters most.",
      "used_by": ["ReasonEmbed"],
      "could_be_applied_to": "Adaptive reward model training — weight reward model training examples by reasoning intensity so the model focuses learning capacity on cases where reasoning-utility distinction matters most, rather than wasting capacity on queries solvable by surface matching."
    },
    {
      "tool": "Dual local/global utility signal framework",
      "what_it_does": "Ranks passages by two complementary signals: local relevance (LLM listwise scoring of query-passage match) and global answer correctness (binary EM from downstream agent). Passages are ranked by global signal first, then local signal as tiebreaker.",
      "used_by": ["Agentic-R"],
      "could_be_applied_to": "Extended to a three-signal framework: local relevance, global answer correctness, and reasoning-chain quality (from learned reward model). The three signals can be combined via learned weights or hierarchical ranking to capture the full spectrum from surface relevance through answer containment to reasoning utility."
    },
    {
      "tool": "Semantic query grouping for GRPO",
      "what_it_does": "Clusters sub-queries across rollouts using token-F1 similarity (threshold δ=0.8) to satisfy GRPO's identical-input requirement for non-LLM components like rankers — enables GRPO training of retrieval components at zero additional sampling cost.",
      "used_by": ["CoSearch"],
      "could_be_applied_to": "GRPO-based training of dense retrievers (not just rankers) — the grouping technique solves the fundamental problem that different reasoning trajectories produce different sub-queries, making standard GRPO inapplicable to retriever training without this clustering step."
    }
  ],
  "common_pitfalls": [
    "Training the LLM/generator when you mean to train the retriever — this is the single most common conflation in the field. Search-R1, ReasonRAG, ProRAG, and Self-RAG all train the LLM while keeping the retriever frozen. Papers claiming to improve 'retrieval-augmented generation' often don't touch retrieval at all. Reviewers will immediately check whether your method actually trains the retriever and will reject if the contribution is misattributed.",
    "Evaluating only on saturated QA benchmarks (HotpotQA, 2WikiMHQA, NQ) where even simple baselines score well — Agentic-R, ReasonRAG, ReSCORE, and CoSearch all avoid BRIGHT. Reviewers increasingly flag this: if your method targets reasoning-intensive retrieval, you must evaluate on BRIGHT or equivalent reasoning-intensive benchmarks, not just multi-hop factoid QA.",
    "Using binary EM/F1 as the sole utility signal while claiming to capture reasoning quality — Agentic-R and CoSearch both use answer-string matching which cannot distinguish documents that contain answers from documents that aid reasoning. If your contribution is about reasoning-quality signals, you must demonstrate that your signal captures information EM cannot (e.g., through ablation showing different document rankings under EM vs. your signal).",
    "Domain-specific methods that don't generalize — SCARLet fails catastrophically on code (-11.9 points) because it relies on Wikipedia-based shared context; RaDeR's MCTS pipeline requires verifiable answers and structured knowledge bases. Reviewers will probe for domain robustness. Either demonstrate cross-domain generalization or explicitly scope your claims.",
    "Underestimating compute costs of MCTS/perturbation-based data generation — SCARLet requires 64 perturbation forward passes per instance; ProRAG's MCTS + GPT-4o judging has unclear compute budget; ReasonRAG's MCTS data generation offsets its 18× training data efficiency claim. Clearly account for data generation compute, not just training compute, in your budget.",
    "Claiming the utility-vs-relevance insight as novel — this distinction was already established by SCARLet (EMNLP 2025) and Agentic-R. Papers that re-introduce this distinction without acknowledging prior work will be rejected for insufficient novelty. The novel contribution must be the METHOD for capturing utility (learned reward model), not the CONCEPT of utility.",
    "Over-relying on synthetic data from BRIGHT-adjacent domains, which creates data leakage concerns — ReasonIR was flagged by reviewers for using BRIGHT corpus documents as seeds. If your training pipeline touches BRIGHT-domain data, you must explicitly address potential contamination with held-out domain evaluation.",
    "Ignoring the relevance-reasoning tradeoff — RaDeR's MS MARCO MRR drops from 41.2 to 34.4 vs. RepLLaMA, suggesting reasoning-focused training hurts standard retrieval. Your method should either demonstrate no degradation on standard benchmarks or explicitly characterize the tradeoff and when to use each approach."
  ],
  "field_trajectory": "The field is converging on three macro-directions that will define the next 12-18 months of retrieval research. First, the RL-ification of retrieval: treating retriever training as a reinforcement learning problem where downstream task performance provides the reward signal is replacing the 20-year paradigm of learning from static relevance labels. Q-RAG's ICLR 2026 Oral acceptance and LREM's production deployment on Taobao validate this direction, but current reward signals (binary EM, rank accuracy, support-fact coverage) are crude proxies for actual retrieval utility. The imminent next step is learned, process-aware reward models that evaluate document utility through the lens of reasoning chain quality — analogous to how ThinkPRM and RM-R1 moved from outcome-level to process-level evaluation in math reasoning. Second, the reasoning-embedding unification: LREM and ReasonEmbed demonstrate that embedding models can be augmented with reasoning capabilities, either through explicit CoT generation (LREM) or reasoning-informed training data (ReasonEmbed). This will continue to push BRIGHT scores upward through increasingly sophisticated ways of injecting reasoning into the embedding process, but the ceiling for data-centric approaches (ReasonEmbed at 38.1 nDCG@10) may be reached soon, creating pressure for reward-based training to provide the next leap. Third, the decomposition of retrieval utility: the field is moving from monolithic relevance scores toward compositional utility signals. ReSCORE's relevance × consistency decomposition, Agentic-R's local/global dual signal, and ProRAG's process/outcome dual advantage all point toward retrieval evaluation as a multi-dimensional assessment where reasoning contribution is the missing dimension. The winning papers of 2026-2027 will be those that formalize reasoning-utility as a first-class training signal and demonstrate that it provides gains specifically on reasoning-intensive benchmarks where simpler utility signals fail.",
  "meta_advice": "If I were advising a PhD student targeting a strong 2026 paper in this area, I would say: your highest-expected-value bet is the intersection of learned reward models and reasoning-intensive retriever training, specifically because this gap sits at the confluence of three validated trends (RL for retrieval, process rewards > outcome rewards, reasoning-intensive evaluation) while remaining genuinely unexplored. Here is the concrete playbook. First, build a reasoning-utility reward model using ThinkPRM's data-efficient recipe (~1K examples): generate reasoning chains with and without candidate documents, use an LLM judge to assess reasoning quality delta, and train a generative reward model that predicts 'does this document improve reasoning chain quality?' — not 'does this document contain the answer?' Second, use this reward model to train a dense retriever via either Q-RAG's factorized Q-value architecture (proven RL-in-embedding-space approach) or contrastive learning with reward-model-scored hard negatives (proven by Agentic-R/ReasonIR). Third, evaluate on BRIGHT — this is non-negotiable, as it is the only benchmark where your reasoning-utility signal should demonstrably outperform binary EM signals, and no utility-based method has been evaluated there. Fourth, include a forensic ablation showing that your reward model ranks documents differently from binary EM on specific BRIGHT queries — find examples where your model prefers tutorial/explanation documents while EM-based methods prefer answer-containing documents. This ablation is what will convince reviewers that the contribution is real, not incremental. Budget your compute carefully: allocate ~50 H100-hours for reward model training (small model, small data following ThinkPRM), ~100 H100-hours for retriever RL training, and ~50 H100-hours for ablations and evaluation. Avoid the temptation to also train the LLM — scope your contribution precisely as 'learned reasoning-utility rewards for retriever training' and let the LLM/generator be frozen. Papers that try to do everything (train retriever + train generator + new reward model + new benchmark) get rejected for insufficient depth. Finally, write your paper around the conceptual distinction: I(Document; ReasoningChain | Query) ≠ I(Document; Answer | Query). This information-theoretic framing gives reviewers a clean mental model, predicts your empirical results, and distinguishes your work from SCARLet and Agentic-R in a way that is immediately clear."
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "55936b6b-e1c4-4878-9ba9-4292cd47845b",
  "isSidechain": false,
  "requestId": "req_011CbYHinckqErgjHyZk143n",
  "type": "assistant",
  "uuid": "6e053b3d-ef6c-4bba-8091-536929e710b0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "6725a028-3696-49b3-b2c2-a8f4330dd39d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Gn9TWkdDa5inJ9moyv7q4p",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12628,
      "cache_read_input_tokens": 11014,
      "output_tokens": 7637,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12628,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 7637,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 12628,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12628
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

_source line 10_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a senior ML research advisor synthesizing a literature review into an actionable research strategy.  **Today's date: 2026-05-30 (UTC).**  ## Research area: Target: AAAI 2026 Track: Information…",
  "leafUuid": "6e053b3d-ef6c-4bba-8091-536929e710b0",
  "sessionId": "6725a028-3696-49b3-b2c2-a8f4330dd39d"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Design reasoning-quality reward model for retriever training",
  "sessionId": "6725a028-3696-49b3-b2c2-a8f4330dd39d"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a senior ML research advisor synthesizing a literature review into an actionable research strategy.  **Today's date: 2026-05-30 (UTC).**  ## Research area: Target: AAAI 2026 Track: Information…",
  "leafUuid": "6e053b3d-ef6c-4bba-8091-536929e710b0",
  "sessionId": "6725a028-3696-49b3-b2c2-a8f4330dd39d"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Design reasoning-quality reward model for retriever training",
  "sessionId": "6725a028-3696-49b3-b2c2-a8f4330dd39d"
}
```

---
