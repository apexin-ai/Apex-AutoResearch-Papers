# Research conversation: You are a strict ML research reviewer conducting adversarial review. **Today's date: 2026-05-16 (UTC).** Your job: indep

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 44
- **Recorded user turns:** 1
- **Tool calls:** 10
- **Original source:** `logs/chats/exported-trajectories/account-2/73813be2-f916-4121-a2d7-450b728cd138.jsonl`
- **Structured JSON:** [`468ae47cbad65099c475.json`](../../sessions/46/468ae47cbad65099c475.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-16T08:45:01.533Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-16T08:45:01.533Z",
  "sessionId": "73813be2-f916-4121-a2d7-450b728cd138",
  "content": "You are a strict ML research reviewer conducting adversarial review.\n\n**Today's date: 2026-05-16 (UTC).**\n\nYour job: independently verify this idea's claims via WebSearch, then issue a verdict.\n\n## User requirements\nThe user asked for: **Target: EMNLP 2026, ARR submission deadline 2026-05-25 (11 days from today 2026-05-14). Track: Generation.\n\nDirection: Faithfulness, hallucination reduction, and calibrated uncertainty in LLM generation. In-scope: hallucination detection via internal representations (linear probes on hidden states, attention patterns, logit signatures), decoding-time interventions that suppress hallucinated content, calibration of verbalized confidence so model uncertainty matches actual accuracy, faithful chain-of-thought (CoT reflects actual computation, not post-hoc rationalization), attribution-aware generation with provenance to source spans, fine-grained atomic-claim verification during or after generation. Cross-cutting with Interpretability and Language Modeling tracks — the contribution must improve GENERATION quality, not just analyze model internals.\n\nContribution type: METHOD ONLY. Must propose a concrete detection algorithm, decoding-time intervention, training recipe, or calibration method. Pure analysis (\"we found models hallucinate when X\") is out of scope. Method + faithfulness analysis OK if analysis validates the method.\n\nHARD CONSTRAINTS:\n1. Compute: ≤200 H100-hours total. Hallucination work is mostly inference + lightweight probe training — budget for forward passes across many prompts + small classifier heads (linear probes, MLPs on hidden states). Avoid full SFT of large models.\n2. Time: ≤11 days. Use existing open models (Llama-3, Qwen3, DeepSeek-R1 distills, Mistral) + existing hallucination/faithfulness benchmarks. Build on interpretability toolkits (TransformerLens, nnsight) for hidden-state extraction if needed.\n3. Eval: TruthfulQA, HaluEval, FaithBench, FActScore, FELM, SimpleQA, LongFact for hallucination detection/reduction; ECE / Brier score / selective accuracy for calibration; faithfulness metrics on CoT (causal interventions, unlearning probes); attribution precision/recall on ELI5-attributed, ExpertQA. Must report both hallucination reduction AND utility preservation (MT-Bench, MMLU) — don't kill helpfulness while suppressing hallucinations.\n\nWhy this matters now: EMNLP 2025 awarded TWO Outstanding Papers in this space (\"Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations\", \"Measuring Chain of Thought Faithfulness by Unlearning Reasoning Steps\"), and the second annual Uncertainty Quantification workshop was held alongside. Hallucination is THE blocking issue for LLM deployment in high-stakes domains, and methods that exploit internal representations (rather than external retrieval or RLHF) are an emerging frontier. Look for: representation-level hallucination detectors that generalize across model families, decoding-time refusal/abstention mechanisms triggered by uncertainty features, calibration methods that work without holdout data, faithful-by-construction reasoning architectures (vs. post-hoc rationalization), atomic-fact-level verification integrated into generation. Avoid: yet another hallucination benchmark, RLHF-from-scratch calibration training, prompt-only \"say I don't know\" tricks, retrieval-augmented faithfulness (covered by Seed 2). Distinguish from existing Interpretability seed: that seed focuses on interpretability METHODS (circuits, probes as tools); this seed uses interpretability TECHNIQUES as means to improve generation faithfulness — output-quality contribution must be primary.**\nYou MUST evaluate whether this idea actually meets the user's requirements. If the user asked for a top venue, assess whether the idea is truly top-venue quality. If the user asked for low resource cost, verify the resource estimate is realistic and low. An idea that doesn't match what the user asked for should be \"revise\" or \"fail\".\n\n## 核心要求：非常仔细地调研，非常仔细地思考\n\n你是一个严格的审稿人。不要轻信 Generator 的任何 claim——你必须独立验证，深入思考每个维度。\n\n### 调研要求\n\n1. **独立 SOTA 验证**：自己搜索当前 SOTA，不要只检查 Generator 的引用。\n   每个验证维度建议用 2-3 种不同的搜索查询。\n\n2. **可行性深度检查**：\n   - 搜索类似实验的实际成本/周期\n   - 检查 claimed baselines 是否可复现\n   - 验证所需的 datasets/models 是否真的可以获取\n\n3. **新颖性压力测试**：专门搜索 Generator 可能遗漏的工作：\n   - 尝试不同的关键词组合\n   - 同时检查 arXiv 和 conference proceedings\n   - 寻找相邻领域的并行/concurrent 工作\n\n4. **深入阅读**：不要只依赖搜索摘要。用 WebFetch 实际阅读相关论文的 abstract 和关键章节，形成你自己的判断。\n\n### 思考要求\n\n5. **独立判断**：\n   - 不要因为 Generator 说得有道理就轻易 pass——真正好的 idea 经得起严格审查\n   - 思考这个 idea 在实际执行中会遇到什么困难\n   - 考虑这个 idea 对领域的真实贡献（不是自说自话的贡献）\n\n6. **评分诚实**：\n   - 不要给\"看起来还行\"的 idea 高分——4 分意味着\"确实很好\"，5 分意味着\"令人兴奋\"\n   - Agent 评分经常虚高，你的职责就是纠正这种偏差\n\n充分利用你的工具——做真正的调研，不是走过场。\n\n\n## 论文搜索策略\n\n你的搜索质量直接决定了 idea 的质量。不要敷衍搜索——每一次搜索都要有明确的目的。\n\n### 搜索源（推荐每个维度使用 2 个不同来源）\n\n1. **arXiv 预印本**（最新工作）:\n   - `site:arxiv.org {topic} {year}` — 按主题搜索最新论文\n   - `site:arxiv.org {method_name}` — 按具体方法名搜索\n   - `arxiv {topic} {month} {year}` — 精确到月份，找最近 3 个月的工作\n\n2. **Google Scholar**（引用关系 + 综合覆盖）:\n   - `{topic} {year} site:scholar.google.com` — 或直接搜索让 Google 自动包含 Scholar 结果\n   - `\"{exact paper title}\"` — 验证论文是否真实存在\n   - `\"{author name}\" {topic} {year}` — 按活跃作者追踪（找到领域大牛后追踪其最新工作）\n\n3. **Papers With Code**（SOTA 排行 + 代码可用性）:\n   - `site:paperswithcode.com {task_name}` — 查看任务的 SOTA 排行榜\n   - `site:paperswithcode.com {method_name}` — 查看方法是否已被实现\n   - `paperswithcode {dataset} benchmark` — 查看特定 dataset 上的竞争格局\n\n4. **OpenReview**（会议审稿 + 同行评价）:\n   - `site:openreview.net {topic} {year}` — 搜索会议提交的论文\n   - 用 WebFetch 阅读 OpenReview 上的 reviewer comments — 了解领域专家的真实评价\n\n5. **Semantic Scholar**（语义搜索 + 引用图谱）:\n   - `semantic scholar {topic} survey {year}` — 找综述论文\n   - `semanticscholar.org {paper_title}` — 查看 cited by（谁引用了这篇）和 references（它引用了谁）\n\n6. **GitHub**（实现验证）:\n   - `site:github.com {method_name} {task}` — 验证开源实现是否存在\n   - `site:huggingface.co {model_name}` — 验证模型/数据集是否可获取\n\n### 搜索维度（多角度交叉，不要只按 topic 搜）\n\n对每个 idea/方向，尽量覆盖以下维度：\n\n1. **正向搜索**：直接搜索主题相关论文\n   - `{topic} {subtopic} {year}`\n   - `{method_name} for {task_name}`\n\n2. **竞争论文搜索**（最关键！）：\n   - `{core_problem} {year}` — 有没有人在解决同样的问题？\n   - `{approach_keyword} {task} {year}` — 有没有人用类似方法？\n   - `{gap_description} solution` — 你发现的 gap 是否已被解决？\n   - **搜索知名团队的最新工作**：如果你知道哪些团队在做这个方向，搜索他们最近 6 个月的论文\n\n3. **相邻领域搜索**：\n   - `{method_from_other_field} applied to {your_task}`\n   - `{your_problem} in {adjacent_domain}` — 其他领域是否已解决类似问题\n\n4. **反面搜索**（找到反对你 idea 的证据）：\n   - `{your_approach} limitations` / `{your_approach} failure`\n   - `why {assumed_gap} is not a problem`\n   - `{baseline_method} sufficient for {task}` — baseline 是否其实已经够好\n\n5. **引用链追踪**（发现遗漏工作的最有效方法）：\n   - 找到一篇核心相关论文后，用 WebFetch 阅读它的 references 部分\n   - 在 Semantic Scholar 上查看它的 \"cited by\" — 最近引用它的论文很可能是 concurrent work\n   - 对 3 个以上核心相关论文重复此步骤\n\n### 搜索数量建议（理想目标，上下文充裕时尽量达到）\n\n| 角色 | 建议搜索次数 | 说明 |\n|------|-------------|------|\n| Round 1 Generator | 10-15 次 | 每个方向争取 3 次独立搜索 |\n| Round 2 Generator | 5-8 次 | 验证 approach 可行性 + baseline |\n| Review Agent | 8-12 次 | 独立验证 + 竞争论文 + 反面证据 |\n| Revision Agent | 5-10 次 | 针对每个 issue 独立调研 |\n\n### 上下文管理\n\n你的输出 token 有限，必须在上下文耗尽之前完成 JSON 输出。\n\n- 上述搜索次数是理想目标。在上下文充裕时应尽量多搜、深搜，搜得越充分越好。\n- 但必须动态评估剩余上下文：如果已经消耗了大量上下文，应优先完成输出，不要为了凑次数而冒着无法输出的风险。\n- WebFetch 深度阅读很有价值，但每次 fetch 消耗大量 token——优先 fetch 最关键的 2-3 篇，而不是每篇都 fetch。\n- 质量 > 数量：5 次精准搜索 + 深度思考 > 15 次浅层搜索。\n\n\nAs a reviewer, your search focus should be:\n1. **验证 claim**：Generator 声称的 SOTA、gap、novelty 是否属实\n2. **找竞争论文**：是否有 Generator 遗漏的高度相关/相似的工作\n3. **找反面证据**：是否有论文表明 Generator 的 approach 行不通\n4. **引用链检查**：通过核心论文的 cited-by 发现 concurrent work\n\n## 竞争论文专项搜索（Reviewer 独有）\n\n这是你作为 Reviewer 最重要的职责之一——发现 Generator 遗漏的竞争工作：\n\n1. **关键词变体搜索**：用至少 3 种不同的关键词组合搜索同一个问题\n   - 同义词替换（e.g., 'efficient' → 'lightweight/fast/scalable'）\n   - 不同粒度（e.g., 'text classification' → 'sentiment analysis' → 'NLP'）\n   - 方法名 + 任务名的不同组合\n\n2. **知名团队追踪**：如果你知道哪些团队/实验室在做相关方向，\n   搜索他们最近的论文（`\"team_name\" OR \"author_name\" {topic} {year}`）\n\n3. **会议最新录用**：搜索最近一轮 ICML/NeurIPS/ICLR/AAAI/ACL 等会议的 accepted papers\n   - `site:openreview.net {topic} 2026`\n   - `{conference_name} 2026 accepted papers {topic}`\n\n4. **arXiv 近 3 个月密集搜索**：对精确相关的关键词，搜索过去 3 个月的 arXiv 论文\n   这是发现 concurrent work 最有效的窗口\n\n如果你发现了 Generator 遗漏的重要相关工作，必须在 issues 中列出论文标题和链接，\n并在 feedback 中说明这些工作如何影响 idea 的 novelty。\n\n## Review checklist\n1. **SOTA freshness**: Are the models/baselines cited actually current SOTA?\n   If outdated, specify what the current SOTA is and cite your source.\n2. **Reference verification**: Do the cited papers actually exist? (WebSearch to check)\n3. **Gap validity**: Does the claimed research gap still exist, or has recent work addressed it?\n4. **Venue validity**: Are target_venues' submission deadlines after 2026-05-16?\n5. **Feasibility**: Is the resource estimate realistic? Are there hidden dependencies?\n6. **Novelty**: Is this sufficiently different from existing work?\n   When scoring novelty < 4:\n   - You MUST identify the closest existing work(s) via WebSearch\n   - In your feedback, write: \"This idea is too similar to [Paper Title (Venue Year)]. Specifically, [what overlaps]. To differentiate, the generator should [suggestion].\"\n   - This gives the generator targeted guidance to boost novelty, not just \"be more novel\".\n7. **Cost realism across modes**: Are the three mode estimates (manual/human-in-loop/auto) internally consistent?\n   - Auto Research uses more GPU hours (2-5x manual) but GPU idle rate should be near zero\n   - Auto Research timeline should reflect resource availability as bottleneck — days with sufficient GPUs, not weeks\n   - Human-in-Loop should fall between manual and auto on most dimensions\n   - Manual and HIL must NOT include salary/wages — only GPU and API costs\n   - Auto Research must NOT include agent operational overhead\n   - If any mode estimate is clearly unrealistic, flag it\n\n## Idea under review (round 4/10)\n{\n  \"title\": \"Geometry-Triggered Sentence-Level Activation Steering for Factual Hallucination Suppression\",\n  \"core_problem\": \"Recent work (Attractor Geometry of Transformer Memory, May 2026) demonstrates that factual hallucination corresponds to 'basin absence'—the hidden state drifts freely when no memorized attractor basin exists—and that geometric margin separates correct recall from hallucination substantially better than entropy (AUROC 0.858 vs. 0.656 on TruthfulQA; up to 0.993 on controlled factoid tasks). Yet translating geometric margin into targeted activation interventions remains unsolved at the right granularity. Hallucination Basins (April 2026) proposes geometry-aware steering but operates at per-sequence granularity—applying uniform corrections across all claims in a response. Spherical Steering (ICML 2026) introduces geometry-aware rotation with an input-adaptive vMF confidence gate, achieving strong TruthfulQA gains, but applies steering per-token without claim-level selectivity: every token gets steered with some intensity, even in correct sub-claims, causing subtle quality degradation on already-accurate content. COAST (May 2026) addresses utility preservation via constrained optimization of the steering vector itself but does not address when to steer. Existing methods either steer everything (Spherical Steering, FLAS, ODESteer), steer the whole sequence (Hallucination Basins), or refine how to steer (COAST)—none selectively gate intervention at the natural unit of factual claims.\",\n  \"opportunity\": \"The critical gap is between detection granularity and intervention granularity. Current geometry-aware steering methods couple 'where to steer' with 'how to steer' at mismatched granularities: Spherical Steering's per-token vMF gate modulates intensity continuously but cannot make a binary 'this claim needs correction / this claim is fine' decision; Hallucination Basins' per-sequence decision cannot distinguish correct from incorrect claims within a response; COAST optimizes the steering vector but applies it uniformly. The unexploited sweet spot is sentence-level gating: sentences are the natural unit of factual claims (the granularity FActScore evaluates, the granularity humans judge, and the granularity at which LLMs perform context integration before next-sentence planning). The combination of (1) Mahalanobis-distance-based basin absence detection as a binary trigger at sentence boundaries, (2) sentence-level gating enabling within-sequence selectivity (steer only flagged claims), and (3) per-layer MLP controller provides a principled 'when + where + how much' framework that is complementary to advances in 'how to steer' (rotation, flow, constrained optimization). Importantly, the trigger mechanism uses basin distance (measuring knowledge absence) rather than directional alignment to a pre-computed truthfulness axis (as in Spherical Steering's vMF gate), providing a more principled signal for detecting hallucination-prone states.\",\n  \"landscape\": \"**Geometry-aware steering (closest competitors):** Spherical Steering (arXiv 2602.08169, ICML 2026) uses geodesic rotation with a von Mises-Fisher confidence gate that dynamically modulates per-token steering strength based on cosine alignment to truthful/hallucinated directions. Achieves MC1 +15.80% on TruthfulQA (Llama-3.1-8B) while preserving generation quality. Operates per-token with a single-layer intervention (layer 24). GTS differs in three ways: (a) sentence-level binary gating vs. per-token continuous modulation—enabling selective skip of entire correct claims rather than low-intensity steering through them; (b) Mahalanobis basin-distance trigger (measuring knowledge absence from attractor geometry) vs. vMF directional alignment to a fixed truthfulness axis (measuring surface-level direction); (c) per-layer MLP controller vs. single-layer intervention. Hallucination Basins (arXiv 2604.04743, April 2026) proposes Adaptive Geometry-Aware Steering using centroid-difference vectors, Euclidean distance trigger, and scalar logistic-regression controller at per-sequence granularity on 1B–3B models. GTS advances beyond it via sentence-level gating, Mahalanobis distance, and per-layer controller.\\n\\n**Utility-preservation approaches:** Minimizing Collateral Damage / COAST (arXiv 2605.01167, May 2026) formalizes collateral damage as unintended feature-direction shifts and solves steering as constrained optimization weighted by the empirical second-moment matrix. Achieves 30% ASR improvement over Angular Steering with preserved benchmarks. COAST is complementary to GTS: it optimizes the steering vector, while GTS optimizes when to apply it. These could be combined (sentence-gated COAST steering). FLAS (arXiv 2605.05892, May 2026) learns a concept-conditioned velocity field for multi-step token-level activation transport, first learned method to outperform prompting on AxBench. Operates per-token with 97.6M–255M trainable parameters. Not hallucination-specific and does not use geometric triggers.\\n\\n**Hallucination detection (analysis-only):** Attractor Geometry of Transformer Memory (arXiv 2605.05686, May 2026) demonstrates hallucination = basin absence with geometric margin achieving AUROC 0.858 on TruthfulQA (vs. entropy 0.656), and AUROC 0.993 on controlled factoid tasks. Authors note 'transfer to open-domain settings requires further study' and margin 'degrades on adversarial reasoning probes.' PCNet (arXiv 2605.05953, May 2026) detects hallucinations as geometric anomalies and applies contrastive decoding at token level. Where Does Reasoning Break? (arXiv 2605.13772, May 2026) detects step-level hallucination via transport geometry but proposes no intervention. DRIFT (arXiv 2601.14210, Jan 2026) detects representational instability at <0.1% overhead.\\n\\n**Calibration/expression approaches:** Calibrating Verbal Uncertainty as a Linear Feature (Ji et al., EMNLP 2025 Outstanding Paper, arXiv 2503.14477) achieves ~31.9% reduction in confident hallucinations via linear-feature intervention on Llama3.1-8B/Mistral-7B/Qwen2.5-7B. Calibrates uncertainty expression without correcting underlying generation—complementary to GTS which detects knowledge absence and redirects toward factual representations.\\n\\n**Other steering methods:** ACT (WWW 2025) uses K-means clustered corpus-averaged vectors. ODESteer (ICLR 2026) achieves 5.7% over ACT via ODE-based multi-step steering but remains input-oblivious. Guiding Giants/WAS (arXiv 2505.20309, May 2025) trains lightweight controllers for layer-aware weighted activation steering. SADI (arXiv 2410.12299, 2024) constructs input-specific dynamic steering vectors. HELIX/Tethered Reasoning (arXiv 2602.17691, Feb 2026) uses Mahalanobis distance + graduated steering for structural coherence in quantized models.\\n\\n**Supporting evidence:** Hallucination as Trajectory Commitment (arXiv 2604.15400, April 2026) provides causal evidence for early commitment with asymmetric attractor dynamics, supporting timely intervention at sentence boundaries before commitment propagates. Think in Sentences (arXiv 2604.10135, April 2026) demonstrates that sentence boundary tokens show attention concentration patterns consistent with context integration cycles, motivating the sentence-as-planning-unit hypothesis (though it does not analyze hidden-state geometry directly).\",\n  \"approach\": \"We propose Geometry-Triggered Steering (GTS), a method that bridges the detection-to-intervention gap by introducing sentence-level selective gating to geometry-aware activation steering. The key insight is that the 'when to steer' decision should operate at claim granularity (sentences), even if the 'how to steer' step operates at token/layer granularity.\\n\\n**Stage 1: TRIGGER (PCA-Regularized Geometric Margin at Sentence Boundaries)**\\nDuring generation, at each sentence boundary (detected via period/newline tokens), extract hidden-state activations at the boundary token across layers using nnsight intervention hooks. Compute geometric margin using class-conditional PCA-regularized Mahalanobis distance:\\n(a) Offline: From a calibration set (~2K examples from TruthfulQA + FELM correct-answer forward passes), collect hidden states at factual completion positions. Apply PCA to project from full hidden dimension (d=4096) to top-k principal components (k=256), reducing covariance estimation to a well-conditioned 256×256 matrix.\\n(b) Online: Project the boundary token's activation into the PCA subspace, compute Mahalanobis distance to nearest factual cluster centroid: δ(x) = √((h_pca - μ_pca)ᵀ Σ_pca⁻¹ (h_pca - μ_pca)).\\n(c) When δ exceeds a calibrated threshold (set via precision-recall analysis on validation split targeting high precision to minimize false interventions), flag the upcoming sentence for intervention.\\n\\n**Trigger reliability note:** Geometric margin achieves AUROC 0.858 on TruthfulQA (vs. entropy 0.656)—sufficient for selective intervention with appropriate thresholding, though far from the 0.993 achieved on synthetic factoid tasks. This motivates operating at high-precision thresholds (accepting lower recall) so that when GTS intervenes, it is likely correct. The precision-recall tradeoff is explicitly studied in ablations.\\n\\n**Stage 2: DIRECTION (Centroid-Directed Steering Vector)**\\nCompute the steering direction as the unit vector from the current activation toward the factual cluster centroid at each layer in the PCA subspace, then project back to full space: v_steer = (μ_pca - h_pca) / ||μ_pca - h_pca||, lifted back to full dimensionality via PCA inverse transform. This yields an input-specific correction direction toward regions of successful fact recall. We additionally experiment with a COAST-style constrained refinement of this vector to minimize collateral damage.\\n\\n**Stage 3: INTENSITY (Per-Layer MLP Controller)**\\nA lightweight 2-layer MLP controller (hidden dim 64, inspired by Guiding Giants/WAS) takes [geometric_margin, layer_index/L, margin_velocity] as input (3D feature vector) and predicts per-layer steering weight λ_ℓ. The controller is trained on a calibration set (~2K examples) via a combined objective: maximize FActScore on steered outputs while minimizing perplexity increase on outputs where margin is below threshold. Steering is applied: h_steered(ℓ) = h(ℓ) + λ_ℓ · v_steer(ℓ) at the residual stream of layers where λ_ℓ > ε.\\n\\n**Timing Hypothesis Validation:**\\nWe explicitly frame the following as a testable hypothesis: geometric margin at sentence boundary N is predictive of factual accuracy in sentence N+1. This is a non-trivial extrapolation from the Attractor Geometry results (which validated margin on first-token factoid completion only). Validation protocol: (1) Generate 500 multi-sentence responses on LongFact/FActScore prompts. (2) Compute margin at every sentence boundary. (3) Annotate each subsequent sentence with FActScore. (4) Measure Spearman correlation between boundary margin and next-sentence factuality. If correlation ρ < 0.3, we fall back to a look-ahead variant: extract margin from the first 3 generated tokens of the new sentence (before committing via speculative-style buffering). The look-ahead variant adds ~15% latency overhead (3 extra forward passes per sentence boundary with rollback capability), which is accounted for in the resource estimate.\\n\\n**Ablation Design (isolating each contribution):**\\n- GTS-full vs. GTS-sequence (ablate sentence gating: single decision per sequence, matching Hallucination Basins)\\n- GTS-full vs. GTS-Euclidean (replace Mahalanobis with Euclidean, matching Hallucination Basins and Attractor Geometry)\\n- GTS-full vs. GTS-scalar (replace per-layer MLP with single scalar, matching Hallucination Basins' controller)\\n- GTS-full vs. GTS-pertoken (apply continuous steering every token, matching Spherical Steering's granularity but with our trigger signal)\\n- GTS-full vs. Spherical Steering (direct comparison using their released code)\\n- GTS-full vs. Verbal-Uncertainty-Feature (Ji et al. baseline)\\n- GTS-full + COAST refinement (combining selective gating with constrained optimization)\\n\\n**Novelty acknowledgment:** If Mahalanobis does not significantly outperform Euclidean in ablations (a known risk given that both Attractor Geometry and Hallucination Basins succeed with Euclidean), the primary novelty contribution shifts to sentence-level gating + per-layer controller as the mechanism enabling within-sequence selectivity—which remains differentiated from all baselines.\\n\\nImplementation uses nnsight 0.6 on Qwen3-8B and Llama-3.1-8B-Instruct. Evaluation on TruthfulQA, HaluEval, FaithBench, FActScore, FELM, SimpleQA, LongFact, MT-Bench, MMLU, plus ECE/Brier calibration metrics. Spherical Steering (released code) serves as primary baseline on identical benchmarks.\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"~200h H100 80GB\",\n      \"gpu_utilization\": \"Low (~15-20%). GPU idles during code/debug/analysis cycles.\",\n      \"timeline\": \"3-4 months\",\n      \"team\": \"1-2 researchers with mechanistic interpretability + geometric ML experience\",\n      \"estimated_gpu_cost\": \"$600-700 (H100 at ~$3/hr spot)\",\n      \"factScore_api_cost\": \"$200-400 (GPT-4 entailment checks: ~150 checks/biography × 2 models × ~8 conditions × 200 examples)\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"~230h H100 80GB\",\n      \"gpu_utilization\": \"Moderate (45-55%). Agent queues batches but blocks on geometric design decisions and timing validation analysis.\",\n      \"timeline\": \"3-4 weeks\",\n      \"team\": \"1 researcher, ~30min/day reviewing agent proposals\",\n      \"claude_api_cost\": \"$200-350\",\n      \"estimated_gpu_cost\": \"$690-800\",\n      \"factScore_api_cost\": \"$200-400\",\n      \"risk_note\": \"Timing hypothesis validation and precision-recall threshold calibration benefit from human intuition. If timing hypothesis fails (ρ < 0.3), implementing look-ahead fallback adds ~1 week.\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"~240-270h H100 80GB (expanded: PCA-k ablations, Mahalanobis vs. Euclidean, timing validation, Spherical Steering comparison, Hallucination Basins ablations, per-token vs sentence-level ablation, COAST combination, layer weight ablations, two-model validation, 10 benchmarks)\",\n      \"gpu_utilization\": \"High (~85-90%). Well-defined pipeline with clear ablation structure.\",\n      \"timeline\": \"10-14 days with 2-4 H100 GPUs running in parallel\",\n      \"team\": \"0 (initial setup: provision GPUs, configure nnsight, define eval harness, clone Spherical Steering repo)\",\n      \"claude_api_cost\": \"$350-550 (est. 5000-7000 turns)\",\n      \"estimated_gpu_cost\": \"$720-810\",\n      \"factScore_api_cost\": \"$300-500 (higher due to more ablation conditions)\",\n      \"speed_bottleneck\": \"GPU count for parallel ablation sweeps. Secondary: FActScore GPT-4 API calls (~100s per response). Spherical Steering baseline reproduction requires their codebase setup.\",\n      \"risk_note\": \"Primary risk: timing hypothesis may fail for multi-sentence generation (Attractor Geometry validated only on factoid completion, authors note 'transfer to open-domain settings requires further study'). Mitigation: look-ahead variant. Secondary risk: Mahalanobis may not beat Euclidean—novelty then rests on sentence-level gating + per-layer controller. Tertiary risk: Spherical Steering's per-token vMF gate may approximate sentence-level selectivity well enough that the explicit gating advantage is marginal.\"\n    }\n  },\n  \"target_venues\": [\n    \"EMNLP 2026 (ARR submission deadline May 25, 2026; commitment deadline August 2, 2026)\"\n  ],\n  \"level\": \"top-tier\",\n  \"key_references\": [\n    \"Spherical Steering: Geometry-Aware Activation Rotation for Language Models (arXiv 2602.08169, ICML 2026)\",\n    \"Attractor Geometry of Transformer Memory: From Conflict Arbitration to Confident Hallucination (arXiv 2605.05686, May 2026)\",\n    \"Hallucination Basins: A Dynamic Framework for Understanding and Controlling LLM Hallucinations (arXiv 2604.04743, April 2026)\",\n    \"Minimizing Collateral Damage in Activation Steering (arXiv 2605.01167, May 2026)\",\n    \"Beyond Steering Vector: Flow-based Activation Steering for Inference-Time Intervention (FLAS, arXiv 2605.05892, May 2026)\",\n    \"Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations (Ji et al., EMNLP 2025 Outstanding Paper, arXiv 2503.14477)\",\n    \"Tethered Reasoning (HELIX): Decoupling Entropy from Hallucination in Quantized LLMs via Manifold Steering (arXiv 2602.17691, Feb 2026)\",\n    \"Adaptive Activation Steering: A Tuning-Free LLM Truthfulness Improvement Method (ACT, WWW 2025)\",\n    \"ODESteer: A Unified ODE-Based Steering Framework for LLM Alignment (ICLR 2026, arXiv 2602.17560)\",\n    \"Where Does Reasoning Break? Step-Level Hallucination Detection via Hidden-State Transport Geometry (arXiv 2605.13772, May 2026)\",\n    \"DRIFT: Detecting Representational Inconsistencies for Factual Truthfulness (arXiv 2601.14210, Jan 2026)\",\n    \"Guiding Giants: Lightweight Controllers for Weighted Activation Steering in LLMs (arXiv 2505.20309, May 2025)\",\n    \"Hallucination as an Anomaly: Dynamic Intervention via Probabilistic Circuits (PCNet, arXiv 2605.05953, May 2026)\",\n    \"Hallucination as Trajectory Commitment: Causal Evidence for Asymmetric Attractor Dynamics (arXiv 2604.15400, April 2026)\",\n    \"Think in Sentences: Explicit Sentence Boundaries Enhance Language Model's Capabilities (arXiv 2604.10135, April 2026)\",\n    \"A Simple Unified Framework for Detecting Out-of-Distribution Samples and Adversarial Attacks (Lee et al., NeurIPS 2018)\",\n    \"Semantics-Adaptive Activation Intervention for LLMs via Dynamic Steering Vectors (SADI, arXiv 2410.12299, 2024)\",\n    \"Dynamic Multimodal Activation Steering for Hallucination Mitigation in Large Vision-Language Models (ICLR 2026)\",\n    \"Monitoring Decoding: Mitigating Hallucination via Evaluating the Factuality of Partial Response during Generation (ACL Findings 2025)\"\n  ],\n  \"description\": \"We propose Geometry-Triggered Steering (GTS), a method that introduces sentence-level selective gating to geometry-aware activation steering for factual hallucination suppression. The key insight is that the 'when to steer' decision should operate at claim granularity (sentences), even when 'how to steer' operates at token/layer granularity.\\n\\nBuilding on the finding that geometric margin separates correct recall from hallucination (AUROC 0.858 on TruthfulQA vs. entropy's 0.656; Liang et al., May 2026), GTS monitors PCA-regularized Mahalanobis distance from residual stream activations to factual cluster centroids at sentence boundaries during generation. When geometric margin indicates basin absence—suggesting the model lacks a memorized attractor for the upcoming content—GTS computes an input-specific steering vector directed toward the factual centroid and applies it with per-layer weights predicted by a lightweight MLP controller. Crucially, sentences where the model is within a factual basin are left untouched.\\n\\nGTS addresses the granularity mismatch in prior work: (1) vs. Spherical Steering (ICML 2026), which applies per-token rotation with continuous vMF-gated intensity (achieving +15% TruthfulQA MC1), GTS makes binary claim-level steer/skip decisions—enabling complete preservation of correct sub-claims within multi-sentence responses, rather than applying low-intensity steering through all tokens including correct ones. The trigger signals also differ fundamentally: Spherical Steering's vMF gate measures alignment to a fixed truthfulness axis, while GTS's Mahalanobis trigger measures distance from factual attractor basins (knowledge absence vs. directional alignment). (2) vs. Hallucination Basins (April 2026), which uses per-sequence Euclidean distance with a scalar controller on 1B–3B models, GTS introduces within-sequence selectivity, directional covariance, and per-layer control. (3) vs. COAST (May 2026), which optimizes the steering vector via constrained optimization to minimize collateral damage, GTS is complementary—it optimizes when to steer rather than how to steer, and we include a GTS+COAST combination experiment.\\n\\nWe explicitly validate the timing hypothesis (margin at boundary N predicts factuality of sentence N+1)—a non-trivial extrapolation from factoid completion settings—with a correlation study and provide a look-ahead fallback if the hypothesis fails. Ablations isolate each design choice against matched baselines (sentence-gating ablated, Euclidean substituted, scalar controller substituted, per-token granularity substituted, direct Spherical Steering comparison). We acknowledge that if Mahalanobis does not significantly outperform Euclidean, the primary novelty shifts to sentence-level gating + per-layer controller.\\n\\nImplementation uses nnsight 0.6 on Qwen3-8B and Llama-3.1-8B-Instruct with Spherical Steering's released code as primary baseline. Evaluation on TruthfulQA, HaluEval, FaithBench, FActScore, FELM, SimpleQA, LongFact, MT-Bench, MMLU, plus ECE/Brier calibration metrics.\",\n  \"project_name\": \"geometry_triggered_steering\",\n  \"source\": \"web_research\"\n}\n\n\n## Previous review history\n### Round 1 review\nVerdict: revise\nIssues: [\"CRITICAL VENUE MISMATCH: User explicitly requested EMNLP 2026 (ARR deadline May 25, 2026), but the idea targets ICLR 2027 and AAAI 2027. The target venues must be changed to EMNLP 2026.\", \"MISSED MAJOR COMPETITOR: HELIX/Tethered Reasoning (arxiv 2602.17691, Feb 2026) already tethers hidden-state trajectories to a pre-computed truthfulness manifold using Mahalanobis distance, applying graduated steering vectors when divergence is detected—directly overlapping with LTS's core contribution. This paper is not cited or discussed.\", \"MISSED CONCURRENT WORK: (a) 'Where Does Reasoning Break?' (arxiv 2605.13772, May 2026)—step-level hallucination detection via hidden-state transport geometry; (b) 'Attractor Geometry of Transformer Memory' (arxiv 2605.05686, May 2026)—basin absence characterization explaining hallucination as free drift; (c) 'Guiding Giants' (arxiv 2505.20309)—lightweight controllers for instance-specific, layer-aware weighted activation steering; (d) DRIFT (arxiv 2601.14210, Jan 2026)—representational inconsistency detection from intermediate layers.\", \"UNSOLVED PREREQUISITE: Claim boundary detection during autoregressive generation has no established method. All cited claim decomposition approaches (FActScore, Claimify, DecMetrics) work post-hoc on complete text. The proposal assumes this exists but provides no solution. This is a fundamental gap in the method pipeline.\", \"TOOLING RISK: TransformerLens has confirmed support for Qwen3-0.6B-Base only. Qwen3-8B/14B compatibility is unverified. nnsight may be a more reliable alternative but the proposal specifically relies on TransformerLens hooks.\", \"ORTHOGONAL PROJECTION UNDERSPECIFIED: The 'factual basin boundary' is not a well-defined geometric object in 4096+ dimensional space. The Hallucination Basins paper (which LTS builds on) explicitly warns that separability is 'strongly task-dependent' and factoid/summarization tasks show different basin structures. How the boundary is estimated, whether it's convex, and what approximation is used for projection are all unspecified.\", \"EVALUATION COVERAGE: User requires TruthfulQA, HaluEval, FaithBench, FActScore, FELM, SimpleQA, LongFact, ECE/Brier, MT-Bench, MMLU. The proposal only evaluates on TruthfulQA, FELM, and FActScore—missing 7 required benchmarks.\", \"RESOURCE ESTIMATES IN WRONG UNITS: User specified ≤200 H100-hours; the proposal estimates in A100 hours. While roughly equivalent after conversion, this shows lack of attention to the user's specifications.\", \"TIMELINE UNREALISTIC: Even the auto-research estimate (10-18 days) exceeds the 11-day constraint before accounting for the unsolved claim-boundary problem, potential TransformerLens incompatibility, and basin boundary estimation challenges.\"]\nFeedback: This idea has a sound motivation—bridging trajectory-based detection and activation steering—but needs major revisions across multiple dimensions:\n\n1. **Fix venue**: Target EMNLP 2026 (ARR May 25) as the user specified, not ICLR/AAAI 2027.\n\n2. **Differentiate from HELIX**: The most urgent novelty threat is HELIX (Tethered Reasoning, arxiv 2602.17691). HELIX already does Mahalanobis-distance-based trajectory monitoring + graduated steering. LTS must clearly articulate what claim-level granularity + orthogonal projection adds beyond HELIX's token-level manifold tethering. Consider: (a) showing claim-level steering preserves utility better than token-level (less over-correction), (b) orthogonal projection yields smaller-norm corrections than HELIX's graduated vectors, (c) ablating claim-level vs token-level on FActScore where per-claim faithfulness matters.\n\n3. **Solve the claim boundary problem**: Either (a) use a simple heuristic (sentence boundaries as claim proxies, which FActScore itself uses), (b) run a lightweight claim decomposition model in parallel during generation, or (c) switch to sentence-level granularity and call it such honestly. Don't assume a solved problem that isn't.\n\n4. **Use nnsight instead of TransformerLens**: nnsight has confirmed Qwen3-VL support and operates on any HuggingFace model. It's a more robust choice for Qwen3-8B/14B.\n\n5. **Simplify basin boundary estimation**: Instead of orthogonal projection onto a manifold boundary (which is ill-defined), consider: (a) use the centroid of the factual cluster and steer toward it (like ACT but trajectory-conditioned), or (b) use the estimated direction from current activation toward the nearest factual centroid, scaled by divergence magnitude. This is more implementable and testable in 11 days.\n\n6. **Add all required benchmarks**: Include HaluEval, FaithBench, SimpleQA, LongFact, ECE/Brier, MT-Bench, MMLU as the user specified.\n\n7. **Also cite and compare against**: HELIX, DRIFT, 'Where Does Reasoning Break?', 'Attractor Geometry of Transformer Memory', and 'Guiding Giants' (WAS).\n\n### Round 2 review\nVerdict: revise\nIssues: [\"CRITICAL COMPETITOR UNDISCUSSED: 'Hallucination Basins' (arXiv 2604.04743, April 2026) already proposes 'Adaptive Geometry-Aware Steering' using centroid-difference vectors (μ_fact−μ_hall), Euclidean distance to basin center as trigger, and a learned scalar controller from geometric features Φ(x)∈ℝ². This is the most direct competitor to GTS—operating at per-sequence granularity on 1B-3B models. The proposal cites it in key_references but does NOT discuss it in the landscape narrative or differentiate against its steering method. This must be fixed.\", \"MISSING CITATION: 'Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations' (Ji et al., EMNLP 2025 Outstanding Paper) achieves ~30% hallucination reduction via inference-time linear-feature intervention in the same paradigm (representation-space signal → inference-time intervention → hallucination reduction). This paper is mentioned in the user's requirements but NOT cited in key_references. GTS must compare against this baseline.\", \"MAHALANOBIS COMPUTATION UNDERSPECIFIED: With ~2K calibration examples (TruthfulQA has ~800 questions) in 4096-dimensional hidden-state space, the sample covariance matrix will be rank-deficient (rank ≤ 2K, dimension 4096). The proposal must specify its regularization strategy: PCA projection to lower dimensions, Ledoit-Wolf shrinkage, diagonal approximation, or class-conditional dimensionality reduction. Note that Hallucination Basins sidesteps this entirely by using Euclidean distance.\", \"TIMING ASSUMPTION UNVERIFIED: The Attractor Geometry paper demonstrates geometric margin on factoid completion tasks (single-token prediction: 'The capital of France is ___'). The proposal assumes margin at sentence boundary N predicts hallucination in sentence N+1 during multi-sentence generation—an untested extrapolation. This should be framed as a testable hypothesis with a fallback (e.g., steer the current sentence in a second-pass or steer at the generating token itself).\", \"NOVELTY FRAMING INSUFFICIENT: The proposal claims the 'specific combination' is novel but does not make a compelling case for WHY sentence-level granularity is better than token-level (PCNet) or sequence-level (Hallucination Basins). The argument 'matching FActScore's evaluation unit' is weak—FActScore evaluates post-hoc, it doesn't constrain intervention granularity. Need a principled argument: e.g., sentence-level avoids PCNet's per-token overhead while enabling within-sequence selectivity that per-sequence methods lack.\"]\nFeedback: The idea has a solid technical foundation but needs to address a critical novelty gap and several methodological underspecifications:\n\n1. **Explicitly compare against Hallucination Basins' steering method**: Add to the landscape: 'Hallucination Basins (2604.04743) proposes Adaptive Geometry-Aware Steering using centroid-difference vectors with a learned scalar controller at per-sequence granularity on 1B-3B models. GTS advances beyond this in three ways: (a) sentence-level gating enables within-sequence selectivity—flagging uncertain claims while preserving confident ones, avoiding the all-or-nothing sequence-level decision; (b) Mahalanobis distance accounts for directional covariance in representation space, providing a tighter decision boundary than isotropic Euclidean distance; (c) per-layer MLP controller learns which layers matter for different types of factual errors, vs. a single scalar that applies uniform intensity.' Then plan ablations: GTS vs. sequence-level baseline (ablate sentence gating) and GTS vs. Euclidean variant.\n\n2. **Cite and position against EMNLP 2025 Outstanding Paper**: 'Calibrating Verbal Uncertainty' (Ji et al., EMNLP 2025) uses a single linear direction for verbal uncertainty. GTS uses geometric margin (distance-based, multi-dimensional) which captures knowledge absence rather than just verbal hedging. Argue: geometric margin detects cases where the model LACKS knowledge (basin absence), while verbal uncertainty detects cases where the model EXPRESSES uncertainty—these are complementary signals, and GTS catches confident hallucinations that verbal uncertainty misses.\n\n3. **Specify Mahalanobis regularization**: 'We compute geometric margin using class-conditional PCA, projecting hidden states to the top-k principal components (k=256) of the factual cluster before computing Mahalanobis distance. This reduces the covariance estimation to a well-conditioned 256×256 matrix from ~2K samples. We ablate k∈{64, 128, 256, 512} and include a diagonal-covariance baseline.'\n\n4. **Frame the timing hypothesis explicitly**: 'We hypothesize that geometric margin at sentence boundaries is predictive of the next sentence's factual accuracy because the residual stream at a period token encodes the model's internal plan for continuation. We validate this with a controlled experiment: compute margin at each sentence boundary and measure correlation with FActScore-annotated factuality of the subsequent sentence. If correlation is weak, we fall back to a look-ahead variant that extracts margin from the first 3 tokens of the new sentence before committing the full sentence.'\n\n5. **Strengthen the novelty argument**: The contribution should be framed not as 'first to combine X+Y+Z' but as 'sentence-level gating solves a specific failure mode of existing methods.' Show: Hallucination Basins over-steers correct sentences (utility loss) because it can't distinguish within a sequence; PCNet under-steers at token level because hallucination is a sentence-level phenomenon (one bad token = one bad claim). GTS hits the sweet spot.\n\n### Round 3 review\nVerdict: revise\nIssues: [\"MISSING CRITICAL COMPETITOR: Spherical Steering (arXiv 2602.08169, ICML 2026) proposes geometry-aware activation rotation with a 'confidence gate that dynamically modulates steering strength based on input uncertainty' — this is conceptually very close to GTS's trigger-then-steer paradigm but uses rotation instead of addition, achieving +10% on TruthfulQA while preserving generation quality. This paper is NOT cited and must be discussed as a baseline.\", \"MISSING COMPETITOR: 'Minimizing Collateral Damage in Activation Steering' (arXiv 2605.01167, May 2026) directly addresses the utility-preservation problem that GTS claims sentence-level gating solves, but via a constrained optimization framework. This is an alternative solution to the same problem that should be compared.\", \"MISSING COMPETITOR: FLAS (Flow-based Activation Steering, arXiv 2605.05892, May 2026) learns a concept-conditioned velocity field that transports activations, claiming to outperform existing steering methods including those on TruthfulQA. This represents another geometry-aware steering approach not discussed.\", \"CHERRY-PICKED AUROC CLAIM: The description implies geometric margin achieves 'AUROC 0.993–1.000' but this is on synthetic factoid tasks. On TruthfulQA, the actual AUROC is 0.858 — a 14-point gap that significantly weakens the trigger reliability argument. The proposal must report the TruthfulQA AUROC and discuss implications for trigger precision/recall.\", \"TIMING HYPOTHESIS REMAINS HIGH-RISK: The Attractor Geometry paper tests ONLY first-token factoid completion on synthetic and controlled tasks. Extrapolating to 'margin at sentence boundary N predicts sentence N+1 factuality' during multi-sentence open-ended generation is a substantial leap. The look-ahead fallback (extracting margin from first 3 tokens) is reasonable but introduces latency and complexity not accounted for in the resource estimate.\", \"OVER-INTERPRETATION OF 'Think in Sentences': The proposal claims this paper provides 'theoretical support for why geometric margin at these positions may be predictive of subsequent sentence quality.' However, the paper is a prompting strategy paper that shows attention concentration at delimiters — it does NOT analyze hidden-state geometry at sentence boundaries and provides no evidence about geometric margin predictiveness.\", \"MAHALANOBIS vs EUCLIDEAN: The proposal positions PCA-regularized Mahalanobis as an advantage over Hallucination Basins' Euclidean, citing OOD detection literature (Lee et al. 2018). However, (1) Hallucination Basins works successfully with Euclidean, (2) the Attractor Geometry paper also uses Euclidean and achieves strong results, and (3) the benefit of Mahalanobis in THIS setting (high-dim LLM residual streams with limited calibration data) is undemonstrated. The ablation is planned but this is a risk to the primary novelty claim if Mahalanobis doesn't significantly outperform Euclidean.\", \"RESOURCE ESTIMATE CONCERN: Running FActScore evaluation on multi-model outputs requires significant GPT-4 API costs (not included in the estimate). FActScore evaluates ~130-205 entailment checks per biography and takes ~100 seconds per response. With 2 models × multiple conditions × hundreds of examples, API costs could be $200-500+ on top of GPU costs.\", \"SCALE COMPARISON WEAKNESS: GTS claims to operate at '8B scale, vs. Hallucination Basins' 1B-3B' as an advance. But the Attractor Geometry paper also tested on models up to 14B and Hallucination Basins tested basin detection on Llama-3.1-8B. Scale alone is not a contribution.\"]\nFeedback: The idea has improved substantially from rounds 1-2 and now has a clear, well-articulated pipeline. The core concept of sentence-level selective steering is sound. However, three critical issues remain:\n\n1. **Cite and compare against Spherical Steering (ICML 2026, arXiv 2602.08169)**: This paper's confidence gate + geometry-aware rotation is the closest competitor to GTS's trigger + steer paradigm. You MUST position against it. Key differentiation: Spherical Steering uses rotation (preserving norm) with a general confidence gate, while GTS uses centroid-directed addition with a geometry-specific Mahalanobis trigger. Argue that GTS's trigger is more principled (basin-distance-based) and its sentence-level granularity enables within-sequence selectivity that Spherical Steering lacks (it applies uniformly). Also cite 'Minimizing Collateral Damage' (2605.01167) as an alternative approach to utility preservation.\n\n2. **Fix the AUROC reporting**: Currently the 0.993-1.000 AUROC is prominently featured but comes from synthetic factoid tasks. The TruthfulQA AUROC is 0.858 — still useful as a trigger but with much higher false-positive/negative rates. Be honest about this: 'Geometric margin achieves AUROC 0.858 on TruthfulQA (vs. entropy's 0.622), sufficient for selective intervention with appropriate thresholding, though precision-recall tradeoffs require careful calibration.' This honesty actually strengthens the paper because it motivates the ablation study.\n\n3. **De-emphasize 'Think in Sentences' as geometric evidence**: This paper shows attention concentration, not hidden-state geometry. Cite it as motivating the sentence-as-unit-of-planning hypothesis, not as providing geometric evidence. The timing hypothesis must stand on its own empirical validation (which the proposal already plans).\n\nMinor improvements: (a) Add FActScore API costs to the resource estimate (~$200-400). (b) Acknowledge that if Mahalanobis doesn't significantly outperform Euclidean, the novelty shifts primarily to sentence-level gating + per-layer controller. (c) Drop the 'AUROC 0.993-1.000' framing and lead with the TruthfulQA number instead.\n\n\n## Output format\nOutput ONLY a JSON object:\n{\n  \"verdict\": \"pass | revise | fail\",\n  \"scores\": {\n    \"novelty\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"feasibility\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"clarity\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"impact\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"}\n  },\n  \"issues\": [\"specific issue 1\", \"specific issue 2\", ...],\n  \"feedback\": \"Actionable feedback for the generator (if verdict=revise)\",\n  \"reason\": \"One-line summary of verdict rationale\"\n}\n\nRules:\n- \"pass\": idea is sound AND high quality — avg score >= 4.0, no critical issues\n- \"revise\": fixable issues OR scores below threshold — provide specific feedback\n- \"fail\": fundamental flaw (e.g., gap doesn't exist, approach provably wrong, or scores remain low after multiple revisions)\n- Threshold is HIGH (4.0/5.0): agent scores tend to be inflated, so only truly outstanding ideas should pass. An avg of 3.5 is NOT enough.\n- Round 10 only: if still \"revise\", you MUST choose \"pass\" or \"fail\"."
}
```

---

### Runtime record

_source line 2 · 2026-05-16T08:45:01.537Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-16T08:45:01.537Z",
  "sessionId": "73813be2-f916-4121-a2d7-450b728cd138"
}
```

---

## Round 1

42 recorded events

### User

_source line 3 · 2026-05-16T08:45:01.560Z_

You are a strict ML research reviewer conducting adversarial review.

**Today's date: 2026-05-16 (UTC).**

Your job: independently verify this idea's claims via WebSearch, then issue a verdict.

## User requirements
The user asked for: **Target: EMNLP 2026, ARR submission deadline 2026-05-25 (11 days from today 2026-05-14). Track: Generation.

Direction: Faithfulness, hallucination reduction, and calibrated uncertainty in LLM generation. In-scope: hallucination detection via internal representations (linear probes on hidden states, attention patterns, logit signatures), decoding-time interventions that suppress hallucinated content, calibration of verbalized confidence so model uncertainty matches actual accuracy, faithful chain-of-thought (CoT reflects actual computation, not post-hoc rationalization), attribution-aware generation with provenance to source spans, fine-grained atomic-claim verification during or after generation. Cross-cutting with Interpretability and Language Modeling tracks — the contribution must improve GENERATION quality, not just analyze model internals.

Contribution type: METHOD ONLY. Must propose a concrete detection algorithm, decoding-time intervention, training recipe, or calibration method. Pure analysis ("we found models hallucinate when X") is out of scope. Method + faithfulness analysis OK if analysis validates the method.

HARD CONSTRAINTS:
1. Compute: ≤200 H100-hours total. Hallucination work is mostly inference + lightweight probe training — budget for forward passes across many prompts + small classifier heads (linear probes, MLPs on hidden states). Avoid full SFT of large models.
2. Time: ≤11 days. Use existing open models (Llama-3, Qwen3, DeepSeek-R1 distills, Mistral) + existing hallucination/faithfulness benchmarks. Build on interpretability toolkits (TransformerLens, nnsight) for hidden-state extraction if needed.
3. Eval: TruthfulQA, HaluEval, FaithBench, FActScore, FELM, SimpleQA, LongFact for hallucination detection/reduction; ECE / Brier score / selective accuracy for calibration; faithfulness metrics on CoT (causal interventions, unlearning probes); attribution precision/recall on ELI5-attributed, ExpertQA. Must report both hallucination reduction AND utility preservation (MT-Bench, MMLU) — don't kill helpfulness while suppressing hallucinations.

Why this matters now: EMNLP 2025 awarded TWO Outstanding Papers in this space ("Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations", "Measuring Chain of Thought Faithfulness by Unlearning Reasoning Steps"), and the second annual Uncertainty Quantification workshop was held alongside. Hallucination is THE blocking issue for LLM deployment in high-stakes domains, and methods that exploit internal representations (rather than external retrieval or RLHF) are an emerging frontier. Look for: representation-level hallucination detectors that generalize across model families, decoding-time refusal/abstention mechanisms triggered by uncertainty features, calibration methods that work without holdout data, faithful-by-construction reasoning architectures (vs. post-hoc rationalization), atomic-fact-level verification integrated into generation. Avoid: yet another hallucination benchmark, RLHF-from-scratch calibration training, prompt-only "say I don't know" tricks, retrieval-augmented faithfulness (covered by Seed 2). Distinguish from existing Interpretability seed: that seed focuses on interpretability METHODS (circuits, probes as tools); this seed uses interpretability TECHNIQUES as means to improve generation faithfulness — output-quality contribution must be primary.**
You MUST evaluate whether this idea actually meets the user's requirements. If the user asked for a top venue, assess whether the idea is truly top-venue quality. If the user asked for low resource cost, verify the resource estimate is realistic and low. An idea that doesn't match what the user asked for should be "revise" or "fail".

## 核心要求：非常仔细地调研，非常仔细地思考

你是一个严格的审稿人。不要轻信 Generator 的任何 claim——你必须独立验证，深入思考每个维度。

### 调研要求

1. **独立 SOTA 验证**：自己搜索当前 SOTA，不要只检查 Generator 的引用。
   每个验证维度建议用 2-3 种不同的搜索查询。

2. **可行性深度检查**：
   - 搜索类似实验的实际成本/周期
   - 检查 claimed baselines 是否可复现
   - 验证所需的 datasets/models 是否真的可以获取

3. **新颖性压力测试**：专门搜索 Generator 可能遗漏的工作：
   - 尝试不同的关键词组合
   - 同时检查 arXiv 和 conference proceedings
   - 寻找相邻领域的并行/concurrent 工作

4. **深入阅读**：不要只依赖搜索摘要。用 WebFetch 实际阅读相关论文的 abstract 和关键章节，形成你自己的判断。

### 思考要求

5. **独立判断**：
   - 不要因为 Generator 说得有道理就轻易 pass——真正好的 idea 经得起严格审查
   - 思考这个 idea 在实际执行中会遇到什么困难
   - 考虑这个 idea 对领域的真实贡献（不是自说自话的贡献）

6. **评分诚实**：
   - 不要给"看起来还行"的 idea 高分——4 分意味着"确实很好"，5 分意味着"令人兴奋"
   - Agent 评分经常虚高，你的职责就是纠正这种偏差

充分利用你的工具——做真正的调研，不是走过场。


## 论文搜索策略

你的搜索质量直接决定了 idea 的质量。不要敷衍搜索——每一次搜索都要有明确的目的。

### 搜索源（推荐每个维度使用 2 个不同来源）

1. **arXiv 预印本**（最新工作）:
   - `site:arxiv.org {topic} {year}` — 按主题搜索最新论文
   - `site:arxiv.org {method_name}` — 按具体方法名搜索
   - `arxiv {topic} {month} {year}` — 精确到月份，找最近 3 个月的工作

2. **Google Scholar**（引用关系 + 综合覆盖）:
   - `{topic} {year} site:scholar.google.com` — 或直接搜索让 Google 自动包含 Scholar 结果
   - `"{exact paper title}"` — 验证论文是否真实存在
   - `"{author name}" {topic} {year}` — 按活跃作者追踪（找到领域大牛后追踪其最新工作）

3. **Papers With Code**（SOTA 排行 + 代码可用性）:
   - `site:paperswithcode.com {task_name}` — 查看任务的 SOTA 排行榜
   - `site:paperswithcode.com {method_name}` — 查看方法是否已被实现
   - `paperswithcode {dataset} benchmark` — 查看特定 dataset 上的竞争格局

4. **OpenReview**（会议审稿 + 同行评价）:
   - `site:openreview.net {topic} {year}` — 搜索会议提交的论文
   - 用 WebFetch 阅读 OpenReview 上的 reviewer comments — 了解领域专家的真实评价

5. **Semantic Scholar**（语义搜索 + 引用图谱）:
   - `semantic scholar {topic} survey {year}` — 找综述论文
   - `semanticscholar.org {paper_title}` — 查看 cited by（谁引用了这篇）和 references（它引用了谁）

6. **GitHub**（实现验证）:
   - `site:github.com {method_name} {task}` — 验证开源实现是否存在
   - `site:huggingface.co {model_name}` — 验证模型/数据集是否可获取

### 搜索维度（多角度交叉，不要只按 topic 搜）

对每个 idea/方向，尽量覆盖以下维度：

1. **正向搜索**：直接搜索主题相关论文
   - `{topic} {subtopic} {year}`
   - `{method_name} for {task_name}`

2. **竞争论文搜索**（最关键！）：
   - `{core_problem} {year}` — 有没有人在解决同样的问题？
   - `{approach_keyword} {task} {year}` — 有没有人用类似方法？
   - `{gap_description} solution` — 你发现的 gap 是否已被解决？
   - **搜索知名团队的最新工作**：如果你知道哪些团队在做这个方向，搜索他们最近 6 个月的论文

3. **相邻领域搜索**：
   - `{method_from_other_field} applied to {your_task}`
   - `{your_problem} in {adjacent_domain}` — 其他领域是否已解决类似问题

4. **反面搜索**（找到反对你 idea 的证据）：
   - `{your_approach} limitations` / `{your_approach} failure`
   - `why {assumed_gap} is not a problem`
   - `{baseline_method} sufficient for {task}` — baseline 是否其实已经够好

5. **引用链追踪**（发现遗漏工作的最有效方法）：
   - 找到一篇核心相关论文后，用 WebFetch 阅读它的 references 部分
   - 在 Semantic Scholar 上查看它的 "cited by" — 最近引用它的论文很可能是 concurrent work
   - 对 3 个以上核心相关论文重复此步骤

### 搜索数量建议（理想目标，上下文充裕时尽量达到）

| 角色 | 建议搜索次数 | 说明 |
|------|-------------|------|
| Round 1 Generator | 10-15 次 | 每个方向争取 3 次独立搜索 |
| Round 2 Generator | 5-8 次 | 验证 approach 可行性 + baseline |
| Review Agent | 8-12 次 | 独立验证 + 竞争论文 + 反面证据 |
| Revision Agent | 5-10 次 | 针对每个 issue 独立调研 |

### 上下文管理

你的输出 token 有限，必须在上下文耗尽之前完成 JSON 输出。

- 上述搜索次数是理想目标。在上下文充裕时应尽量多搜、深搜，搜得越充分越好。
- 但必须动态评估剩余上下文：如果已经消耗了大量上下文，应优先完成输出，不要为了凑次数而冒着无法输出的风险。
- WebFetch 深度阅读很有价值，但每次 fetch 消耗大量 token——优先 fetch 最关键的 2-3 篇，而不是每篇都 fetch。
- 质量 > 数量：5 次精准搜索 + 深度思考 > 15 次浅层搜索。


As a reviewer, your search focus should be:
1. **验证 claim**：Generator 声称的 SOTA、gap、novelty 是否属实
2. **找竞争论文**：是否有 Generator 遗漏的高度相关/相似的工作
3. **找反面证据**：是否有论文表明 Generator 的 approach 行不通
4. **引用链检查**：通过核心论文的 cited-by 发现 concurrent work

## 竞争论文专项搜索（Reviewer 独有）

这是你作为 Reviewer 最重要的职责之一——发现 Generator 遗漏的竞争工作：

1. **关键词变体搜索**：用至少 3 种不同的关键词组合搜索同一个问题
   - 同义词替换（e.g., 'efficient' → 'lightweight/fast/scalable'）
   - 不同粒度（e.g., 'text classification' → 'sentiment analysis' → 'NLP'）
   - 方法名 + 任务名的不同组合

2. **知名团队追踪**：如果你知道哪些团队/实验室在做相关方向，
   搜索他们最近的论文（`"team_name" OR "author_name" {topic} {year}`）

3. **会议最新录用**：搜索最近一轮 ICML/NeurIPS/ICLR/AAAI/ACL 等会议的 accepted papers
   - `site:openreview.net {topic} 2026`
   - `{conference_name} 2026 accepted papers {topic}`

4. **arXiv 近 3 个月密集搜索**：对精确相关的关键词，搜索过去 3 个月的 arXiv 论文
   这是发现 concurrent work 最有效的窗口

如果你发现了 Generator 遗漏的重要相关工作，必须在 issues 中列出论文标题和链接，
并在 feedback 中说明这些工作如何影响 idea 的 novelty。

## Review checklist
1. **SOTA freshness**: Are the models/baselines cited actually current SOTA?
   If outdated, specify what the current SOTA is and cite your source.
2. **Reference verification**: Do the cited papers actually exist? (WebSearch to check)
3. **Gap validity**: Does the claimed research gap still exist, or has recent work addressed it?
4. **Venue validity**: Are target_venues' submission deadlines after 2026-05-16?
5. **Feasibility**: Is the resource estimate realistic? Are there hidden dependencies?
6. **Novelty**: Is this sufficiently different from existing work?
   When scoring novelty < 4:
   - You MUST identify the closest existing work(s) via WebSearch
   - In your feedback, write: "This idea is too similar to [Paper Title (Venue Year)]. Specifically, [what overlaps]. To differentiate, the generator should [suggestion]."
   - This gives the generator targeted guidance to boost novelty, not just "be more novel".
7. **Cost realism across modes**: Are the three mode estimates (manual/human-in-loop/auto) internally consistent?
   - Auto Research uses more GPU hours (2-5x manual) but GPU idle rate should be near zero
   - Auto Research timeline should reflect resource availability as bottleneck — days with sufficient GPUs, not weeks
   - Human-in-Loop should fall between manual and auto on most dimensions
   - Manual and HIL must NOT include salary/wages — only GPU and API costs
   - Auto Research must NOT include agent operational overhead
   - If any mode estimate is clearly unrealistic, flag it

## Idea under review (round 4/10)
{
  "title": "Geometry-Triggered Sentence-Level Activation Steering for Factual Hallucination Suppression",
  "core_problem": "Recent work (Attractor Geometry of Transformer Memory, May 2026) demonstrates that factual hallucination corresponds to 'basin absence'—the hidden state drifts freely when no memorized attractor basin exists—and that geometric margin separates correct recall from hallucination substantially better than entropy (AUROC 0.858 vs. 0.656 on TruthfulQA; up to 0.993 on controlled factoid tasks). Yet translating geometric margin into targeted activation interventions remains unsolved at the right granularity. Hallucination Basins (April 2026) proposes geometry-aware steering but operates at per-sequence granularity—applying uniform corrections across all claims in a response. Spherical Steering (ICML 2026) introduces geometry-aware rotation with an input-adaptive vMF confidence gate, achieving strong TruthfulQA gains, but applies steering per-token without claim-level selectivity: every token gets steered with some intensity, even in correct sub-claims, causing subtle quality degradation on already-accurate content. COAST (May 2026) addresses utility preservation via constrained optimization of the steering vector itself but does not address when to steer. Existing methods either steer everything (Spherical Steering, FLAS, ODESteer), steer the whole sequence (Hallucination Basins), or refine how to steer (COAST)—none selectively gate intervention at the natural unit of factual claims.",
  "opportunity": "The critical gap is between detection granularity and intervention granularity. Current geometry-aware steering methods couple 'where to steer' with 'how to steer' at mismatched granularities: Spherical Steering's per-token vMF gate modulates intensity continuously but cannot make a binary 'this claim needs correction / this claim is fine' decision; Hallucination Basins' per-sequence decision cannot distinguish correct from incorrect claims within a response; COAST optimizes the steering vector but applies it uniformly. The unexploited sweet spot is sentence-level gating: sentences are the natural unit of factual claims (the granularity FActScore evaluates, the granularity humans judge, and the granularity at which LLMs perform context integration before next-sentence planning). The combination of (1) Mahalanobis-distance-based basin absence detection as a binary trigger at sentence boundaries, (2) sentence-level gating enabling within-sequence selectivity (steer only flagged claims), and (3) per-layer MLP controller provides a principled 'when + where + how much' framework that is complementary to advances in 'how to steer' (rotation, flow, constrained optimization). Importantly, the trigger mechanism uses basin distance (measuring knowledge absence) rather than directional alignment to a pre-computed truthfulness axis (as in Spherical Steering's vMF gate), providing a more principled signal for detecting hallucination-prone states.",
  "landscape": "**Geometry-aware steering (closest competitors):** Spherical Steering (arXiv 2602.08169, ICML 2026) uses geodesic rotation with a von Mises-Fisher confidence gate that dynamically modulates per-token steering strength based on cosine alignment to truthful/hallucinated directions. Achieves MC1 +15.80% on TruthfulQA (Llama-3.1-8B) while preserving generation quality. Operates per-token with a single-layer intervention (layer 24). GTS differs in three ways: (a) sentence-level binary gating vs. per-token continuous modulation—enabling selective skip of entire correct claims rather than low-intensity steering through them; (b) Mahalanobis basin-distance trigger (measuring knowledge absence from attractor geometry) vs. vMF directional alignment to a fixed truthfulness axis (measuring surface-level direction); (c) per-layer MLP controller vs. single-layer intervention. Hallucination Basins (arXiv 2604.04743, April 2026) proposes Adaptive Geometry-Aware Steering using centroid-difference vectors, Euclidean distance trigger, and scalar logistic-regression controller at per-sequence granularity on 1B–3B models. GTS advances beyond it via sentence-level gating, Mahalanobis distance, and per-layer controller.\n\n**Utility-preservation approaches:** Minimizing Collateral Damage / COAST (arXiv 2605.01167, May 2026) formalizes collateral damage as unintended feature-direction shifts and solves steering as constrained optimization weighted by the empirical second-moment matrix. Achieves 30% ASR improvement over Angular Steering with preserved benchmarks. COAST is complementary to GTS: it optimizes the steering vector, while GTS optimizes when to apply it. These could be combined (sentence-gated COAST steering). FLAS (arXiv 2605.05892, May 2026) learns a concept-conditioned velocity field for multi-step token-level activation transport, first learned method to outperform prompting on AxBench. Operates per-token with 97.6M–255M trainable parameters. Not hallucination-specific and does not use geometric triggers.\n\n**Hallucination detection (analysis-only):** Attractor Geometry of Transformer Memory (arXiv 2605.05686, May 2026) demonstrates hallucination = basin absence with geometric margin achieving AUROC 0.858 on TruthfulQA (vs. entropy 0.656), and AUROC 0.993 on controlled factoid tasks. Authors note 'transfer to open-domain settings requires further study' and margin 'degrades on adversarial reasoning probes.' PCNet (arXiv 2605.05953, May 2026) detects hallucinations as geometric anomalies and applies contrastive decoding at token level. Where Does Reasoning Break? (arXiv 2605.13772, May 2026) detects step-level hallucination via transport geometry but proposes no intervention. DRIFT (arXiv 2601.14210, Jan 2026) detects representational instability at <0.1% overhead.\n\n**Calibration/expression approaches:** Calibrating Verbal Uncertainty as a Linear Feature (Ji et al., EMNLP 2025 Outstanding Paper, arXiv 2503.14477) achieves ~31.9% reduction in confident hallucinations via linear-feature intervention on Llama3.1-8B/Mistral-7B/Qwen2.5-7B. Calibrates uncertainty expression without correcting underlying generation—complementary to GTS which detects knowledge absence and redirects toward factual representations.\n\n**Other steering methods:** ACT (WWW 2025) uses K-means clustered corpus-averaged vectors. ODESteer (ICLR 2026) achieves 5.7% over ACT via ODE-based multi-step steering but remains input-oblivious. Guiding Giants/WAS (arXiv 2505.20309, May 2025) trains lightweight controllers for layer-aware weighted activation steering. SADI (arXiv 2410.12299, 2024) constructs input-specific dynamic steering vectors. HELIX/Tethered Reasoning (arXiv 2602.17691, Feb 2026) uses Mahalanobis distance + graduated steering for structural coherence in quantized models.\n\n**Supporting evidence:** Hallucination as Trajectory Commitment (arXiv 2604.15400, April 2026) provides causal evidence for early commitment with asymmetric attractor dynamics, supporting timely intervention at sentence boundaries before commitment propagates. Think in Sentences (arXiv 2604.10135, April 2026) demonstrates that sentence boundary tokens show attention concentration patterns consistent with context integration cycles, motivating the sentence-as-planning-unit hypothesis (though it does not analyze hidden-state geometry directly).",
  "approach": "We propose Geometry-Triggered Steering (GTS), a method that bridges the detection-to-intervention gap by introducing sentence-level selective gating to geometry-aware activation steering. The key insight is that the 'when to steer' decision should operate at claim granularity (sentences), even if the 'how to steer' step operates at token/layer granularity.\n\n**Stage 1: TRIGGER (PCA-Regularized Geometric Margin at Sentence Boundaries)**\nDuring generation, at each sentence boundary (detected via period/newline tokens), extract hidden-state activations at the boundary token across layers using nnsight intervention hooks. Compute geometric margin using class-conditional PCA-regularized Mahalanobis distance:\n(a) Offline: From a calibration set (~2K examples from TruthfulQA + FELM correct-answer forward passes), collect hidden states at factual completion positions. Apply PCA to project from full hidden dimension (d=4096) to top-k principal components (k=256), reducing covariance estimation to a well-conditioned 256×256 matrix.\n(b) Online: Project the boundary token's activation into the PCA subspace, compute Mahalanobis distance to nearest factual cluster centroid: δ(x) = √((h_pca - μ_pca)ᵀ Σ_pca⁻¹ (h_pca - μ_pca)).\n(c) When δ exceeds a calibrated threshold (set via precision-recall analysis on validation split targeting high precision to minimize false interventions), flag the upcoming sentence for intervention.\n\n**Trigger reliability note:** Geometric margin achieves AUROC 0.858 on TruthfulQA (vs. entropy 0.656)—sufficient for selective intervention with appropriate thresholding, though far from the 0.993 achieved on synthetic factoid tasks. This motivates operating at high-precision thresholds (accepting lower recall) so that when GTS intervenes, it is likely correct. The precision-recall tradeoff is explicitly studied in ablations.\n\n**Stage 2: DIRECTION (Centroid-Directed Steering Vector)**\nCompute the steering direction as the unit vector from the current activation toward the factual cluster centroid at each layer in the PCA subspace, then project back to full space: v_steer = (μ_pca - h_pca) / ||μ_pca - h_pca||, lifted back to full dimensionality via PCA inverse transform. This yields an input-specific correction direction toward regions of successful fact recall. We additionally experiment with a COAST-style constrained refinement of this vector to minimize collateral damage.\n\n**Stage 3: INTENSITY (Per-Layer MLP Controller)**\nA lightweight 2-layer MLP controller (hidden dim 64, inspired by Guiding Giants/WAS) takes [geometric_margin, layer_index/L, margin_velocity] as input (3D feature vector) and predicts per-layer steering weight λ_ℓ. The controller is trained on a calibration set (~2K examples) via a combined objective: maximize FActScore on steered outputs while minimizing perplexity increase on outputs where margin is below threshold. Steering is applied: h_steered(ℓ) = h(ℓ) + λ_ℓ · v_steer(ℓ) at the residual stream of layers where λ_ℓ > ε.\n\n**Timing Hypothesis Validation:**\nWe explicitly frame the following as a testable hypothesis: geometric margin at sentence boundary N is predictive of factual accuracy in sentence N+1. This is a non-trivial extrapolation from the Attractor Geometry results (which validated margin on first-token factoid completion only). Validation protocol: (1) Generate 500 multi-sentence responses on LongFact/FActScore prompts. (2) Compute margin at every sentence boundary. (3) Annotate each subsequent sentence with FActScore. (4) Measure Spearman correlation between boundary margin and next-sentence factuality. If correlation ρ < 0.3, we fall back to a look-ahead variant: extract margin from the first 3 generated tokens of the new sentence (before committing via speculative-style buffering). The look-ahead variant adds ~15% latency overhead (3 extra forward passes per sentence boundary with rollback capability), which is accounted for in the resource estimate.\n\n**Ablation Design (isolating each contribution):**\n- GTS-full vs. GTS-sequence (ablate sentence gating: single decision per sequence, matching Hallucination Basins)\n- GTS-full vs. GTS-Euclidean (replace Mahalanobis with Euclidean, matching Hallucination Basins and Attractor Geometry)\n- GTS-full vs. GTS-scalar (replace per-layer MLP with single scalar, matching Hallucination Basins' controller)\n- GTS-full vs. GTS-pertoken (apply continuous steering every token, matching Spherical Steering's granularity but with our trigger signal)\n- GTS-full vs. Spherical Steering (direct comparison using their released code)\n- GTS-full vs. Verbal-Uncertainty-Feature (Ji et al. baseline)\n- GTS-full + COAST refinement (combining selective gating with constrained optimization)\n\n**Novelty acknowledgment:** If Mahalanobis does not significantly outperform Euclidean in ablations (a known risk given that both Attractor Geometry and Hallucination Basins succeed with Euclidean), the primary novelty contribution shifts to sentence-level gating + per-layer controller as the mechanism enabling within-sequence selectivity—which remains differentiated from all baselines.\n\nImplementation uses nnsight 0.6 on Qwen3-8B and Llama-3.1-8B-Instruct. Evaluation on TruthfulQA, HaluEval, FaithBench, FActScore, FELM, SimpleQA, LongFact, MT-Bench, MMLU, plus ECE/Brier calibration metrics. Spherical Steering (released code) serves as primary baseline on identical benchmarks.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "~200h H100 80GB",
      "gpu_utilization": "Low (~15-20%). GPU idles during code/debug/analysis cycles.",
      "timeline": "3-4 months",
      "team": "1-2 researchers with mechanistic interpretability + geometric ML experience",
      "estimated_gpu_cost": "$600-700 (H100 at ~$3/hr spot)",
      "factScore_api_cost": "$200-400 (GPT-4 entailment checks: ~150 checks/biography × 2 models × ~8 conditions × 200 examples)"
    },
    "human_in_loop": {
      "gpu_hours": "~230h H100 80GB",
      "gpu_utilization": "Moderate (45-55%). Agent queues batches but blocks on geometric design decisions and timing validation analysis.",
      "timeline": "3-4 weeks",
      "team": "1 researcher, ~30min/day reviewing agent proposals",
      "claude_api_cost": "$200-350",
      "estimated_gpu_cost": "$690-800",
      "factScore_api_cost": "$200-400",
      "risk_note": "Timing hypothesis validation and precision-recall threshold calibration benefit from human intuition. If timing hypothesis fails (ρ < 0.3), implementing look-ahead fallback adds ~1 week."
    },
    "auto_research": {
      "gpu_hours": "~240-270h H100 80GB (expanded: PCA-k ablations, Mahalanobis vs. Euclidean, timing validation, Spherical Steering comparison, Hallucination Basins ablations, per-token vs sentence-level ablation, COAST combination, layer weight ablations, two-model validation, 10 benchmarks)",
      "gpu_utilization": "High (~85-90%). Well-defined pipeline with clear ablation structure.",
      "timeline": "10-14 days with 2-4 H100 GPUs running in parallel",
      "team": "0 (initial setup: provision GPUs, configure nnsight, define eval harness, clone Spherical Steering repo)",
      "claude_api_cost": "$350-550 (est. 5000-7000 turns)",
      "estimated_gpu_cost": "$720-810",
      "factScore_api_cost": "$300-500 (higher due to more ablation conditions)",
      "speed_bottleneck": "GPU count for parallel ablation sweeps. Secondary: FActScore GPT-4 API calls (~100s per response). Spherical Steering baseline reproduction requires their codebase setup.",
      "risk_note": "Primary risk: timing hypothesis may fail for multi-sentence generation (Attractor Geometry validated only on factoid completion, authors note 'transfer to open-domain settings requires further study'). Mitigation: look-ahead variant. Secondary risk: Mahalanobis may not beat Euclidean—novelty then rests on sentence-level gating + per-layer controller. Tertiary risk: Spherical Steering's per-token vMF gate may approximate sentence-level selectivity well enough that the explicit gating advantage is marginal."
    }
  },
  "target_venues": [
    "EMNLP 2026 (ARR submission deadline May 25, 2026; commitment deadline August 2, 2026)"
  ],
  "level": "top-tier",
  "key_references": [
    "Spherical Steering: Geometry-Aware Activation Rotation for Language Models (arXiv 2602.08169, ICML 2026)",
    "Attractor Geometry of Transformer Memory: From Conflict Arbitration to Confident Hallucination (arXiv 2605.05686, May 2026)",
    "Hallucination Basins: A Dynamic Framework for Understanding and Controlling LLM Hallucinations (arXiv 2604.04743, April 2026)",
    "Minimizing Collateral Damage in Activation Steering (arXiv 2605.01167, May 2026)",
    "Beyond Steering Vector: Flow-based Activation Steering for Inference-Time Intervention (FLAS, arXiv 2605.05892, May 2026)",
    "Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations (Ji et al., EMNLP 2025 Outstanding Paper, arXiv 2503.14477)",
    "Tethered Reasoning (HELIX): Decoupling Entropy from Hallucination in Quantized LLMs via Manifold Steering (arXiv 2602.17691, Feb 2026)",
    "Adaptive Activation Steering: A Tuning-Free LLM Truthfulness Improvement Method (ACT, WWW 2025)",
    "ODESteer: A Unified ODE-Based Steering Framework for LLM Alignment (ICLR 2026, arXiv 2602.17560)",
    "Where Does Reasoning Break? Step-Level Hallucination Detection via Hidden-State Transport Geometry (arXiv 2605.13772, May 2026)",
    "DRIFT: Detecting Representational Inconsistencies for Factual Truthfulness (arXiv 2601.14210, Jan 2026)",
    "Guiding Giants: Lightweight Controllers for Weighted Activation Steering in LLMs (arXiv 2505.20309, May 2025)",
    "Hallucination as an Anomaly: Dynamic Intervention via Probabilistic Circuits (PCNet, arXiv 2605.05953, May 2026)",
    "Hallucination as Trajectory Commitment: Causal Evidence for Asymmetric Attractor Dynamics (arXiv 2604.15400, April 2026)",
    "Think in Sentences: Explicit Sentence Boundaries Enhance Language Model's Capabilities (arXiv 2604.10135, April 2026)",
    "A Simple Unified Framework for Detecting Out-of-Distribution Samples and Adversarial Attacks (Lee et al., NeurIPS 2018)",
    "Semantics-Adaptive Activation Intervention for LLMs via Dynamic Steering Vectors (SADI, arXiv 2410.12299, 2024)",
    "Dynamic Multimodal Activation Steering for Hallucination Mitigation in Large Vision-Language Models (ICLR 2026)",
    "Monitoring Decoding: Mitigating Hallucination via Evaluating the Factuality of Partial Response during Generation (ACL Findings 2025)"
  ],
  "description": "We propose Geometry-Triggered Steering (GTS), a method that introduces sentence-level selective gating to geometry-aware activation steering for factual hallucination suppression. The key insight is that the 'when to steer' decision should operate at claim granularity (sentences), even when 'how to steer' operates at token/layer granularity.\n\nBuilding on the finding that geometric margin separates correct recall from hallucination (AUROC 0.858 on TruthfulQA vs. entropy's 0.656; Liang et al., May 2026), GTS monitors PCA-regularized Mahalanobis distance from residual stream activations to factual cluster centroids at sentence boundaries during generation. When geometric margin indicates basin absence—suggesting the model lacks a memorized attractor for the upcoming content—GTS computes an input-specific steering vector directed toward the factual centroid and applies it with per-layer weights predicted by a lightweight MLP controller. Crucially, sentences where the model is within a factual basin are left untouched.\n\nGTS addresses the granularity mismatch in prior work: (1) vs. Spherical Steering (ICML 2026), which applies per-token rotation with continuous vMF-gated intensity (achieving +15% TruthfulQA MC1), GTS makes binary claim-level steer/skip decisions—enabling complete preservation of correct sub-claims within multi-sentence responses, rather than applying low-intensity steering through all tokens including correct ones. The trigger signals also differ fundamentally: Spherical Steering's vMF gate measures alignment to a fixed truthfulness axis, while GTS's Mahalanobis trigger measures distance from factual attractor basins (knowledge absence vs. directional alignment). (2) vs. Hallucination Basins (April 2026), which uses per-sequence Euclidean distance with a scalar controller on 1B–3B models, GTS introduces within-sequence selectivity, directional covariance, and per-layer control. (3) vs. COAST (May 2026), which optimizes the steering vector via constrained optimization to minimize collateral damage, GTS is complementary—it optimizes when to steer rather than how to steer, and we include a GTS+COAST combination experiment.\n\nWe explicitly validate the timing hypothesis (margin at boundary N predicts factuality of sentence N+1)—a non-trivial extrapolation from factoid completion settings—with a correlation study and provide a look-ahead fallback if the hypothesis fails. Ablations isolate each design choice against matched baselines (sentence-gating ablated, Euclidean substituted, scalar controller substituted, per-token granularity substituted, direct Spherical Steering comparison). We acknowledge that if Mahalanobis does not significantly outperform Euclidean, the primary novelty shifts to sentence-level gating + per-layer controller.\n\nImplementation uses nnsight 0.6 on Qwen3-8B and Llama-3.1-8B-Instruct with Spherical Steering's released code as primary baseline. Evaluation on TruthfulQA, HaluEval, FaithBench, FActScore, FELM, SimpleQA, LongFact, MT-Bench, MMLU, plus ECE/Brier calibration metrics.",
  "project_name": "geometry_triggered_steering",
  "source": "web_research"
}


## Previous review history
### Round 1 review
Verdict: revise
Issues: ["CRITICAL VENUE MISMATCH: User explicitly requested EMNLP 2026 (ARR deadline May 25, 2026), but the idea targets ICLR 2027 and AAAI 2027. The target venues must be changed to EMNLP 2026.", "MISSED MAJOR COMPETITOR: HELIX/Tethered Reasoning (arxiv 2602.17691, Feb 2026) already tethers hidden-state trajectories to a pre-computed truthfulness manifold using Mahalanobis distance, applying graduated steering vectors when divergence is detected—directly overlapping with LTS's core contribution. This paper is not cited or discussed.", "MISSED CONCURRENT WORK: (a) 'Where Does Reasoning Break?' (arxiv 2605.13772, May 2026)—step-level hallucination detection via hidden-state transport geometry; (b) 'Attractor Geometry of Transformer Memory' (arxiv 2605.05686, May 2026)—basin absence characterization explaining hallucination as free drift; (c) 'Guiding Giants' (arxiv 2505.20309)—lightweight controllers for instance-specific, layer-aware weighted activation steering; (d) DRIFT (arxiv 2601.14210, Jan 2026)—representational inconsistency detection from intermediate layers.", "UNSOLVED PREREQUISITE: Claim boundary detection during autoregressive generation has no established method. All cited claim decomposition approaches (FActScore, Claimify, DecMetrics) work post-hoc on complete text. The proposal assumes this exists but provides no solution. This is a fundamental gap in the method pipeline.", "TOOLING RISK: TransformerLens has confirmed support for Qwen3-0.6B-Base only. Qwen3-8B/14B compatibility is unverified. nnsight may be a more reliable alternative but the proposal specifically relies on TransformerLens hooks.", "ORTHOGONAL PROJECTION UNDERSPECIFIED: The 'factual basin boundary' is not a well-defined geometric object in 4096+ dimensional space. The Hallucination Basins paper (which LTS builds on) explicitly warns that separability is 'strongly task-dependent' and factoid/summarization tasks show different basin structures. How the boundary is estimated, whether it's convex, and what approximation is used for projection are all unspecified.", "EVALUATION COVERAGE: User requires TruthfulQA, HaluEval, FaithBench, FActScore, FELM, SimpleQA, LongFact, ECE/Brier, MT-Bench, MMLU. The proposal only evaluates on TruthfulQA, FELM, and FActScore—missing 7 required benchmarks.", "RESOURCE ESTIMATES IN WRONG UNITS: User specified ≤200 H100-hours; the proposal estimates in A100 hours. While roughly equivalent after conversion, this shows lack of attention to the user's specifications.", "TIMELINE UNREALISTIC: Even the auto-research estimate (10-18 days) exceeds the 11-day constraint before accounting for the unsolved claim-boundary problem, potential TransformerLens incompatibility, and basin boundary estimation challenges."]
Feedback: This idea has a sound motivation—bridging trajectory-based detection and activation steering—but needs major revisions across multiple dimensions:

1. **Fix venue**: Target EMNLP 2026 (ARR May 25) as the user specified, not ICLR/AAAI 2027.

2. **Differentiate from HELIX**: The most urgent novelty threat is HELIX (Tethered Reasoning, arxiv 2602.17691). HELIX already does Mahalanobis-distance-based trajectory monitoring + graduated steering. LTS must clearly articulate what claim-level granularity + orthogonal projection adds beyond HELIX's token-level manifold tethering. Consider: (a) showing claim-level steering preserves utility better than token-level (less over-correction), (b) orthogonal projection yields smaller-norm corrections than HELIX's graduated vectors, (c) ablating claim-level vs token-level on FActScore where per-claim faithfulness matters.

3. **Solve the claim boundary problem**: Either (a) use a simple heuristic (sentence boundaries as claim proxies, which FActScore itself uses), (b) run a lightweight claim decomposition model in parallel during generation, or (c) switch to sentence-level granularity and call it such honestly. Don't assume a solved problem that isn't.

4. **Use nnsight instead of TransformerLens**: nnsight has confirmed Qwen3-VL support and operates on any HuggingFace model. It's a more robust choice for Qwen3-8B/14B.

5. **Simplify basin boundary estimation**: Instead of orthogonal projection onto a manifold boundary (which is ill-defined), consider: (a) use the centroid of the factual cluster and steer toward it (like ACT but trajectory-conditioned), or (b) use the estimated direction from current activation toward the nearest factual centroid, scaled by divergence magnitude. This is more implementable and testable in 11 days.

6. **Add all required benchmarks**: Include HaluEval, FaithBench, SimpleQA, LongFact, ECE/Brier, MT-Bench, MMLU as the user specified.

7. **Also cite and compare against**: HELIX, DRIFT, 'Where Does Reasoning Break?', 'Attractor Geometry of Transformer Memory', and 'Guiding Giants' (WAS).

### Round 2 review
Verdict: revise
Issues: ["CRITICAL COMPETITOR UNDISCUSSED: 'Hallucination Basins' (arXiv 2604.04743, April 2026) already proposes 'Adaptive Geometry-Aware Steering' using centroid-difference vectors (μ_fact−μ_hall), Euclidean distance to basin center as trigger, and a learned scalar controller from geometric features Φ(x)∈ℝ². This is the most direct competitor to GTS—operating at per-sequence granularity on 1B-3B models. The proposal cites it in key_references but does NOT discuss it in the landscape narrative or differentiate against its steering method. This must be fixed.", "MISSING CITATION: 'Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations' (Ji et al., EMNLP 2025 Outstanding Paper) achieves ~30% hallucination reduction via inference-time linear-feature intervention in the same paradigm (representation-space signal → inference-time intervention → hallucination reduction). This paper is mentioned in the user's requirements but NOT cited in key_references. GTS must compare against this baseline.", "MAHALANOBIS COMPUTATION UNDERSPECIFIED: With ~2K calibration examples (TruthfulQA has ~800 questions) in 4096-dimensional hidden-state space, the sample covariance matrix will be rank-deficient (rank ≤ 2K, dimension 4096). The proposal must specify its regularization strategy: PCA projection to lower dimensions, Ledoit-Wolf shrinkage, diagonal approximation, or class-conditional dimensionality reduction. Note that Hallucination Basins sidesteps this entirely by using Euclidean distance.", "TIMING ASSUMPTION UNVERIFIED: The Attractor Geometry paper demonstrates geometric margin on factoid completion tasks (single-token prediction: 'The capital of France is ___'). The proposal assumes margin at sentence boundary N predicts hallucination in sentence N+1 during multi-sentence generation—an untested extrapolation. This should be framed as a testable hypothesis with a fallback (e.g., steer the current sentence in a second-pass or steer at the generating token itself).", "NOVELTY FRAMING INSUFFICIENT: The proposal claims the 'specific combination' is novel but does not make a compelling case for WHY sentence-level granularity is better than token-level (PCNet) or sequence-level (Hallucination Basins). The argument 'matching FActScore's evaluation unit' is weak—FActScore evaluates post-hoc, it doesn't constrain intervention granularity. Need a principled argument: e.g., sentence-level avoids PCNet's per-token overhead while enabling within-sequence selectivity that per-sequence methods lack."]
Feedback: The idea has a solid technical foundation but needs to address a critical novelty gap and several methodological underspecifications:

1. **Explicitly compare against Hallucination Basins' steering method**: Add to the landscape: 'Hallucination Basins (2604.04743) proposes Adaptive Geometry-Aware Steering using centroid-difference vectors with a learned scalar controller at per-sequence granularity on 1B-3B models. GTS advances beyond this in three ways: (a) sentence-level gating enables within-sequence selectivity—flagging uncertain claims while preserving confident ones, avoiding the all-or-nothing sequence-level decision; (b) Mahalanobis distance accounts for directional covariance in representation space, providing a tighter decision boundary than isotropic Euclidean distance; (c) per-layer MLP controller learns which layers matter for different types of factual errors, vs. a single scalar that applies uniform intensity.' Then plan ablations: GTS vs. sequence-level baseline (ablate sentence gating) and GTS vs. Euclidean variant.

2. **Cite and position against EMNLP 2025 Outstanding Paper**: 'Calibrating Verbal Uncertainty' (Ji et al., EMNLP 2025) uses a single linear direction for verbal uncertainty. GTS uses geometric margin (distance-based, multi-dimensional) which captures knowledge absence rather than just verbal hedging. Argue: geometric margin detects cases where the model LACKS knowledge (basin absence), while verbal uncertainty detects cases where the model EXPRESSES uncertainty—these are complementary signals, and GTS catches confident hallucinations that verbal uncertainty misses.

3. **Specify Mahalanobis regularization**: 'We compute geometric margin using class-conditional PCA, projecting hidden states to the top-k principal components (k=256) of the factual cluster before computing Mahalanobis distance. This reduces the covariance estimation to a well-conditioned 256×256 matrix from ~2K samples. We ablate k∈{64, 128, 256, 512} and include a diagonal-covariance baseline.'

4. **Frame the timing hypothesis explicitly**: 'We hypothesize that geometric margin at sentence boundaries is predictive of the next sentence's factual accuracy because the residual stream at a period token encodes the model's internal plan for continuation. We validate this with a controlled experiment: compute margin at each sentence boundary and measure correlation with FActScore-annotated factuality of the subsequent sentence. If correlation is weak, we fall back to a look-ahead variant that extracts margin from the first 3 tokens of the new sentence before committing the full sentence.'

5. **Strengthen the novelty argument**: The contribution should be framed not as 'first to combine X+Y+Z' but as 'sentence-level gating solves a specific failure mode of existing methods.' Show: Hallucination Basins over-steers correct sentences (utility loss) because it can't distinguish within a sequence; PCNet under-steers at token level because hallucination is a sentence-level phenomenon (one bad token = one bad claim). GTS hits the sweet spot.

### Round 3 review
Verdict: revise
Issues: ["MISSING CRITICAL COMPETITOR: Spherical Steering (arXiv 2602.08169, ICML 2026) proposes geometry-aware activation rotation with a 'confidence gate that dynamically modulates steering strength based on input uncertainty' — this is conceptually very close to GTS's trigger-then-steer paradigm but uses rotation instead of addition, achieving +10% on TruthfulQA while preserving generation quality. This paper is NOT cited and must be discussed as a baseline.", "MISSING COMPETITOR: 'Minimizing Collateral Damage in Activation Steering' (arXiv 2605.01167, May 2026) directly addresses the utility-preservation problem that GTS claims sentence-level gating solves, but via a constrained optimization framework. This is an alternative solution to the same problem that should be compared.", "MISSING COMPETITOR: FLAS (Flow-based Activation Steering, arXiv 2605.05892, May 2026) learns a concept-conditioned velocity field that transports activations, claiming to outperform existing steering methods including those on TruthfulQA. This represents another geometry-aware steering approach not discussed.", "CHERRY-PICKED AUROC CLAIM: The description implies geometric margin achieves 'AUROC 0.993–1.000' but this is on synthetic factoid tasks. On TruthfulQA, the actual AUROC is 0.858 — a 14-point gap that significantly weakens the trigger reliability argument. The proposal must report the TruthfulQA AUROC and discuss implications for trigger precision/recall.", "TIMING HYPOTHESIS REMAINS HIGH-RISK: The Attractor Geometry paper tests ONLY first-token factoid completion on synthetic and controlled tasks. Extrapolating to 'margin at sentence boundary N predicts sentence N+1 factuality' during multi-sentence open-ended generation is a substantial leap. The look-ahead fallback (extracting margin from first 3 tokens) is reasonable but introduces latency and complexity not accounted for in the resource estimate.", "OVER-INTERPRETATION OF 'Think in Sentences': The proposal claims this paper provides 'theoretical support for why geometric margin at these positions may be predictive of subsequent sentence quality.' However, the paper is a prompting strategy paper that shows attention concentration at delimiters — it does NOT analyze hidden-state geometry at sentence boundaries and provides no evidence about geometric margin predictiveness.", "MAHALANOBIS vs EUCLIDEAN: The proposal positions PCA-regularized Mahalanobis as an advantage over Hallucination Basins' Euclidean, citing OOD detection literature (Lee et al. 2018). However, (1) Hallucination Basins works successfully with Euclidean, (2) the Attractor Geometry paper also uses Euclidean and achieves strong results, and (3) the benefit of Mahalanobis in THIS setting (high-dim LLM residual streams with limited calibration data) is undemonstrated. The ablation is planned but this is a risk to the primary novelty claim if Mahalanobis doesn't significantly outperform Euclidean.", "RESOURCE ESTIMATE CONCERN: Running FActScore evaluation on multi-model outputs requires significant GPT-4 API costs (not included in the estimate). FActScore evaluates ~130-205 entailment checks per biography and takes ~100 seconds per response. With 2 models × multiple conditions × hundreds of examples, API costs could be $200-500+ on top of GPU costs.", "SCALE COMPARISON WEAKNESS: GTS claims to operate at '8B scale, vs. Hallucination Basins' 1B-3B' as an advance. But the Attractor Geometry paper also tested on models up to 14B and Hallucination Basins tested basin detection on Llama-3.1-8B. Scale alone is not a contribution."]
Feedback: The idea has improved substantially from rounds 1-2 and now has a clear, well-articulated pipeline. The core concept of sentence-level selective steering is sound. However, three critical issues remain:

1. **Cite and compare against Spherical Steering (ICML 2026, arXiv 2602.08169)**: This paper's confidence gate + geometry-aware rotation is the closest competitor to GTS's trigger + steer paradigm. You MUST position against it. Key differentiation: Spherical Steering uses rotation (preserving norm) with a general confidence gate, while GTS uses centroid-directed addition with a geometry-specific Mahalanobis trigger. Argue that GTS's trigger is more principled (basin-distance-based) and its sentence-level granularity enables within-sequence selectivity that Spherical Steering lacks (it applies uniformly). Also cite 'Minimizing Collateral Damage' (2605.01167) as an alternative approach to utility preservation.

2. **Fix the AUROC reporting**: Currently the 0.993-1.000 AUROC is prominently featured but comes from synthetic factoid tasks. The TruthfulQA AUROC is 0.858 — still useful as a trigger but with much higher false-positive/negative rates. Be honest about this: 'Geometric margin achieves AUROC 0.858 on TruthfulQA (vs. entropy's 0.622), sufficient for selective intervention with appropriate thresholding, though precision-recall tradeoffs require careful calibration.' This honesty actually strengthens the paper because it motivates the ablation study.

3. **De-emphasize 'Think in Sentences' as geometric evidence**: This paper shows attention concentration, not hidden-state geometry. Cite it as motivating the sentence-as-unit-of-planning hypothesis, not as providing geometric evidence. The timing hypothesis must stand on its own empirical validation (which the proposal already plans).

Minor improvements: (a) Add FActScore API costs to the resource estimate (~$200-400). (b) Acknowledge that if Mahalanobis doesn't significantly outperform Euclidean, the novelty shifts primarily to sentence-level gating + per-layer controller. (c) Drop the 'AUROC 0.993-1.000' framing and lead with the TruthfulQA number instead.


## Output format
Output ONLY a JSON object:
{
  "verdict": "pass | revise | fail",
  "scores": {
    "novelty": {"score": 0-5, "rationale": "1-2 sentence justification"},
    "feasibility": {"score": 0-5, "rationale": "1-2 sentence justification"},
    "clarity": {"score": 0-5, "rationale": "1-2 sentence justification"},
    "impact": {"score": 0-5, "rationale": "1-2 sentence justification"}
  },
  "issues": ["specific issue 1", "specific issue 2", ...],
  "feedback": "Actionable feedback for the generator (if verdict=revise)",
  "reason": "One-line summary of verdict rationale"
}

Rules:
- "pass": idea is sound AND high quality — avg score >= 4.0, no critical issues
- "revise": fixable issues OR scores below threshold — provide specific feedback
- "fail": fundamental flaw (e.g., gap doesn't exist, approach provably wrong, or scores remain low after multiple revisions)
- Threshold is HIGH (4.0/5.0): agent scores tend to be inflated, so only truly outstanding ideas should pass. An avg of 3.5 is NOT enough.
- Round 10 only: if still "revise", you MUST choose "pass" or "fail".

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "fa61ad10-397c-4783-9490-82353cc0b8e8",
  "type": "user",
  "uuid": "87e78c91-1dc3-4450-8a6d-e9fe674aa252",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73813be2-f916-4121-a2d7-450b728cd138",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-16T08:45:01.558Z_

```json
{
  "parentUuid": "87e78c91-1dc3-4450-8a6d-e9fe674aa252",
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
  "uuid": "f74d346f-f3c2-47ab-af69-1ca899792b0f",
  "timestamp": "2026-05-16T08:45:01.558Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73813be2-f916-4121-a2d7-450b728cd138",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-16T08:45:01.558Z_

```json
{
  "parentUuid": "f74d346f-f3c2-47ab-af69-1ca899792b0f",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "edf739fb-cb7e-4485-b370-1e68e2153d5b",
  "timestamp": "2026-05-16T08:45:01.558Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73813be2-f916-4121-a2d7-450b728cd138",
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
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-16 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "edf739fb-cb7e-4485-b370-1e68e2153d5b",
  "sessionId": "73813be2-f916-4121-a2d7-450b728cd138"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Geometry-triggered sentence-level hallucination steering",
  "sessionId": "73813be2-f916-4121-a2d7-450b728cd138"
}
```

---

### Assistant

_source line 8 · 2026-05-16T08:45:21.506Z_

<details><summary>Logged reasoning block</summary>

```text
This is round 4 of 10 for reviewing a research idea about "Geometry-Triggered Sentence-Level Activation Steering for Factual Hallucination Suppression" (GTS). The idea has been through 3 rounds of revision already. Let me conduct a thorough independent review.

Let me identify the key claims and elements I need to verify:

1. **Spherical Steering (arXiv 2602.08169, ICML 2026)** - The proposal now cites this. I need to verify it exists and check its actual contributions.


2. **Attractor Geometry of Transformer Memory (arXiv 2605.05686, May 2026)** - Claims AUROC 0.858 on TruthfulQA for geometric margin.
3. **Hallucination Basins (arXiv 2604.04743, April 2026)** - Per-sequence steering with Euclidean distance.
4. **COAST (arXiv 2605.01167, May 2026)** - Constrained optimization for activation steering.
5. **FLAS (arXiv 2605.05892, May 2026)** - Flow-based activation steering.

Now I'm checking the remaining references and methodological claims to assess the novelty and validity of the GTS approach. I'm starting to search for additional competing approaches and verify the core claims around sentence-level gating and the timing hypothesis.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "edf739fb-cb7e-4485-b370-1e68e2153d5b",
  "isSidechain": false,
  "requestId": "req_011Cb5xHtrJBneof5zR3ZQNg",
  "type": "assistant",
  "uuid": "58c831a6-558d-4dcc-8414-48c2697f1622",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73813be2-f916-4121-a2d7-450b728cd138",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J5jEHLYt7ir1iPdVnTzmgs",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 19587,
      "cache_read_input_tokens": 11841,
      "output_tokens": 1717,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19587,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1717,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 19587,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19587
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

_source line 9 · 2026-05-16T08:45:21.706Z_

I'll conduct an independent verification of this idea's claims, focusing on novelty threats, feasibility, and the key technical assumptions. Let me search for the most critical competitors and verify the core claims.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "58c831a6-558d-4dcc-8414-48c2697f1622",
  "isSidechain": false,
  "requestId": "req_011Cb5xHtrJBneof5zR3ZQNg",
  "type": "assistant",
  "uuid": "bcddffcd-22b6-4b69-9f7d-366823bccc0d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73813be2-f916-4121-a2d7-450b728cd138",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J5jEHLYt7ir1iPdVnTzmgs",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 19587,
      "cache_read_input_tokens": 11841,
      "output_tokens": 1717,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19587,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1717,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 19587,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19587
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

_source line 10 · 2026-05-16T08:45:27.268Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01QRYW1B1NmBmYk4F9jSuvzR`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Verify Spherical Steering paper",
  "prompt": "Use WebSearch to find and verify the paper \"Spherical Steering: Geometry-Aware Activation Rotation for Language Models\" (arXiv 2602.08169). I need to know:\n1. Does it actually exist? What are its exact claims?\n2. Does it use a \"von Mises-Fisher confidence gate\" that \"dynamically modulates steering strength based on input uncertainty\"?\n3. What TruthfulQA results does it achieve (specifically MC1 percentage improvement)?\n4. Does it operate per-token or per-sequence?\n5. Is it actually accepted at ICML 2026?\n6. Does it have released code?\n\nSearch for: \"Spherical Steering geometry-aware activation rotation\" and \"arxiv 2602.08169\". Also try fetching the arxiv page if possible."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bcddffcd-22b6-4b69-9f7d-366823bccc0d",
  "isSidechain": false,
  "requestId": "req_011Cb5xHtrJBneof5zR3ZQNg",
  "type": "assistant",
  "uuid": "ac3ed160-7d06-4cdc-8035-6417ddd23714",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73813be2-f916-4121-a2d7-450b728cd138",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J5jEHLYt7ir1iPdVnTzmgs",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 19587,
      "cache_read_input_tokens": 11841,
      "output_tokens": 1717,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19587,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1717,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 19587,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19587
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

_source line 11 · 2026-05-16T08:45:30.503Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01AVGh5Er3wWkjFCe62QDN7b`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Verify Attractor Geometry paper",
  "prompt": "Use WebSearch to find and verify the paper \"Attractor Geometry of Transformer Memory: From Conflict Arbitration to Confident Hallucination\" (arXiv 2605.05686, May 2026). I need to know:\n1. Does it actually exist?\n2. Does it claim geometric margin achieves AUROC 0.858 on TruthfulQA (vs. entropy 0.656)?\n3. Does it characterize hallucination as \"basin absence\"?\n4. Does it note that \"transfer to open-domain settings requires further study\"?\n5. What models/scales does it test on?\n\nSearch for \"Attractor Geometry Transformer Memory\" and \"arxiv 2605.05686\" and \"hallucination basin absence attractor geometry 2026\"."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ac3ed160-7d06-4cdc-8035-6417ddd23714",
  "isSidechain": false,
  "requestId": "req_011Cb5xHtrJBneof5zR3ZQNg",
  "type": "assistant",
  "uuid": "3f23fd55-8726-4661-a55e-3e04f34924b8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73813be2-f916-4121-a2d7-450b728cd138",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J5jEHLYt7ir1iPdVnTzmgs",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 19587,
      "cache_read_input_tokens": 11841,
      "output_tokens": 1717,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19587,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1717,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 19587,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19587
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

_source line 12 · 2026-05-16T08:45:36.607Z_

<details open><summary>🔧 Tool call — Agent · `toolu_016Yw5XdgpT8Fu7YLv8JhQhC`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Search for sentence-level steering competitors",
  "prompt": "Use WebSearch to find ANY papers that propose sentence-level or claim-level activation steering or intervention for hallucination reduction in LLMs. I need to check if the \"sentence-level gating\" contribution claimed by this idea already exists in prior work.\n\nSearch for:\n1. \"sentence-level activation steering hallucination\" 2025 2026\n2. \"claim-level intervention hallucination LLM\" 2025 2026\n3. \"selective activation steering\" OR \"selective steering\" hallucination 2025 2026\n4. \"sentence-level gating\" LLM generation 2025 2026\n5. \"granularity hallucination intervention\" OR \"claim-level hallucination suppression\"\n\nAlso search for \"Monitoring Decoding hallucination factuality partial response\" since this is cited in the key_references and may do something similar (intervening during generation at sub-sequence granularity)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3f23fd55-8726-4661-a55e-3e04f34924b8",
  "isSidechain": false,
  "requestId": "req_011Cb5xHtrJBneof5zR3ZQNg",
  "type": "assistant",
  "uuid": "149a2b8e-bf6d-46ec-91de-221f7f9553f3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73813be2-f916-4121-a2d7-450b728cd138",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J5jEHLYt7ir1iPdVnTzmgs",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 19587,
      "cache_read_input_tokens": 11841,
      "output_tokens": 1717,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19587,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1717,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 19587,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19587
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

_source line 13 · 2026-05-16T08:45:41.001Z_

<details open><summary>🔧 Tool call — Agent · `toolu_014JP1Fmv6oJKEMhNRz6Dtu6`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Verify COAST and Hallucination Basins",
  "prompt": "Use WebSearch to find and verify these two papers:\n\n1. \"Minimizing Collateral Damage in Activation Steering\" (arXiv 2605.01167, May 2026) - also called COAST. Does it exist? What does it actually do? Does it claim 30% ASR improvement?\n\n2. \"Hallucination Basins: A Dynamic Framework for Understanding and Controlling LLM Hallucinations\" (arXiv 2604.04743, April 2026). Does it exist? Does it propose \"Adaptive Geometry-Aware Steering\"? Does it use centroid-difference vectors and Euclidean distance trigger with a scalar logistic-regression controller? What scale models (1B-3B)?\n\nSearch for:\n- \"Minimizing Collateral Damage activation steering\" OR \"arxiv 2605.01167\"\n- \"COAST activation steering constrained optimization\"\n- \"Hallucination Basins\" OR \"arxiv 2604.04743\"\n- \"geometry-aware steering hallucination basins\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "149a2b8e-bf6d-46ec-91de-221f7f9553f3",
  "isSidechain": false,
  "requestId": "req_011Cb5xHtrJBneof5zR3ZQNg",
  "type": "assistant",
  "uuid": "cb462a7f-7f26-4342-8c62-0fde5c9c6cb2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73813be2-f916-4121-a2d7-450b728cd138",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J5jEHLYt7ir1iPdVnTzmgs",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 19587,
      "cache_read_input_tokens": 11841,
      "output_tokens": 1717,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19587,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1717,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 19587,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19587
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

_source line 14 · 2026-05-16T08:46:36.082Z_

<details><summary>↩ Tool result · `toolu_01QRYW1B1NmBmYk4F9jSuvzR`</summary>

```text
Now I have comprehensive information. Let me compile the findings.

Based on my research, here is a detailed verification of each claim about "Spherical Steering: Geometry-Aware Activation Rotation for Language Models" (arXiv 2602.08169):

---

## 1. Does the paper exist?

**Yes, it exists.** It is a real paper on arXiv (2602.08169), submitted February 9, 2026, by Zejia You, Chunyuan Deng, and Hanjie Chen. The paper proposes a training-free inference-time steering method that rotates activations along a geodesic toward a target direction (rather than using standard activation addition), preserving representation magnitude while steering model behavior.

---

## 2. Does it use a "von Mises-Fisher confidence gate" that "dynamically modulates steering strength based on input uncertainty"?

**Yes, confirmed.** The paper employs a vMF-based confidence gate. The mechanism computes alignment scores between the current activation direction and both truthful/hallucinated prototype directions using cosine similarity. These scores are fed into vMF-induced exponential terms (f(u;m,kappa) proportional to exp(kappa * m^T * u)), normalized via softmax to produce probabilities pT and pH. The difference delta = pH - pT maps to intervention strength t in [0,1] through a thresholded rule controlled by hyperparameters alpha, beta, and kappa. So the claim about "dynamically modulating steering strength based on input uncertainty" is accurate.

---

## 3. TruthfulQA MC1 results?

The paper reports specific MC1 improvements:
- **LLaMA-3.1-8B-Instruct**: 34.15% (baseline) to 49.95% (Spherical Steering) = **+15.8 percentage points**
- **Qwen-2.5-7B-Instruct**: 35.87% (baseline) to 48.71% (Spherical Steering) = **+12.84 percentage points**

The general claim of "+10% on TruthfulQA" in the abstract appears to be a rounded/conservative figure; actual improvements are larger (12-16 percentage points on MC1). The average improvement across all six benchmarks tested is +8.06 points.

---

## 4. Per-token or per-sequence?

**Per-token during generation.** Prototypes are constructed using last-token activations extracted offline, but at inference time, the steering rotation is applied at each decoding step (token-by-token) based on the current activations. So it operates per-token.

---

## 5. Is it accepted at ICML 2026?

**Evidence is mixed but leans toward yes.** The arXiv paper itself does not explicitly state ICML 2026 acceptance (it is posted as a preprint). However, the GitHub repository (github.com/chili-lab/Spherical-Steering) has "[ICML 2026]" in its title/description, and search results consistently reference it as an ICML 2026 paper. This is consistent with papers that receive acceptance after the preprint is posted and update their repo but not the arXiv abstract immediately.

---

## 6. Does it have released code?

**Yes.** Code is available at: https://github.com/chili-lab/Spherical-Steering

The repository contains:
- `spherical_steering.py` - Core steering logic with geometric intervention hooks
- `get_activations.py` - Extracts last-token hidden states from answer pairs
- `get_prototypes.py` - Computes steering targets with question-level splits
- `evaluate_mc.py` - Multiple-choice evaluation (MC1/MC2/MC3 metrics)
- `evaluate_llm_judge.py` - Open-ended generation with truth/information scoring
- `utils.py` - Data loading and activation extraction utilities
- Quickstart scripts for Llama3.1-8B-Instruct and Qwen2.5-7B-Instruct

License: CC-BY-NC-SA 4.0, Python 3.10, dependencies in environment.yml.

---

## Summary

All major claims check out as real. The paper exists, uses a vMF confidence gate, achieves substantial TruthfulQA MC1 improvements (+12-16 percentage points), operates per-token at inference, appears accepted at ICML 2026 (per GitHub repo tagging), and has publicly released code.

Sources:
- [arXiv:2602.08169 Abstract](https://arxiv.org/abs/2602.08169)
- [arXiv:2602.08169 HTML](https://arxiv.org/html/2602.08169v1)
- [GitHub: chili-lab/Spherical-Steering](https://github.com/chili-lab/Spherical-Steering)
- [ResearchGate Publication](https://www.researchgate.net/publication/400605038_Spherical_Steering_Geometry-Aware_Activation_Rotation_for_Language_Models)

agentId: add766dc6f6f2b147 (use SendMessage with to: 'add766dc6f6f2b147' to continue this agent)
&lt;usage>total_tokens: 18245
tool_uses: 9
duration_ms: 68807&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ac3ed160-7d06-4cdc-8035-6417ddd23714",
  "isSidechain": false,
  "promptId": "fa61ad10-397c-4783-9490-82353cc0b8e8",
  "type": "user",
  "uuid": "ca0b38dd-fb95-436c-ba07-2a4cd1052e0d",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Use WebSearch to find and verify the paper \"Spherical Steering: Geometry-Aware Activation Rotation for Language Models\" (arXiv 2602.08169). I need to know:\n1. Does it actually exist? What are its exact claims?\n2. Does it use a \"von Mises-Fisher confidence gate\" that \"dynamically modulates steering strength based on input uncertainty\"?\n3. What TruthfulQA results does it achieve (specifically MC1 percentage improvement)?\n4. Does it operate per-token or per-sequence?\n5. Is it actually accepted at ICML 2026?\n6. Does it have released code?\n\nSearch for: \"Spherical Steering geometry-aware activation rotation\" and \"arxiv 2602.08169\". Also try fetching the arxiv page if possible.",
    "agentId": "add766dc6f6f2b147",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have comprehensive information. Let me compile the findings.\n\nBased on my research, here is a detailed verification of each claim about \"Spherical Steering: Geometry-Aware Activation Rotation for Language Models\" (arXiv 2602.08169):\n\n---\n\n## 1. Does the paper exist?\n\n**Yes, it exists.** It is a real paper on arXiv (2602.08169), submitted February 9, 2026, by Zejia You, Chunyuan Deng, and Hanjie Chen. The paper proposes a training-free inference-time steering method that rotates activations along a geodesic toward a target direction (rather than using standard activation addition), preserving representation magnitude while steering model behavior.\n\n---\n\n## 2. Does it use a \"von Mises-Fisher confidence gate\" that \"dynamically modulates steering strength based on input uncertainty\"?\n\n**Yes, confirmed.** The paper employs a vMF-based confidence gate. The mechanism computes alignment scores between the current activation direction and both truthful/hallucinated prototype directions using cosine similarity. These scores are fed into vMF-induced exponential terms (f(u;m,kappa) proportional to exp(kappa * m^T * u)), normalized via softmax to produce probabilities pT and pH. The difference delta = pH - pT maps to intervention strength t in [0,1] through a thresholded rule controlled by hyperparameters alpha, beta, and kappa. So the claim about \"dynamically modulating steering strength based on input uncertainty\" is accurate.\n\n---\n\n## 3. TruthfulQA MC1 results?\n\nThe paper reports specific MC1 improvements:\n- **LLaMA-3.1-8B-Instruct**: 34.15% (baseline) to 49.95% (Spherical Steering) = **+15.8 percentage points**\n- **Qwen-2.5-7B-Instruct**: 35.87% (baseline) to 48.71% (Spherical Steering) = **+12.84 percentage points**\n\nThe general claim of \"+10% on TruthfulQA\" in the abstract appears to be a rounded/conservative figure; actual improvements are larger (12-16 percentage points on MC1). The average improvement across all six benchmarks tested is +8.06 points.\n\n---\n\n## 4. Per-token or per-sequence?\n\n**Per-token during generation.** Prototypes are constructed using last-token activations extracted offline, but at inference time, the steering rotation is applied at each decoding step (token-by-token) based on the current activations. So it operates per-token.\n\n---\n\n## 5. Is it accepted at ICML 2026?\n\n**Evidence is mixed but leans toward yes.** The arXiv paper itself does not explicitly state ICML 2026 acceptance (it is posted as a preprint). However, the GitHub repository (github.com/chili-lab/Spherical-Steering) has \"[ICML 2026]\" in its title/description, and search results consistently reference it as an ICML 2026 paper. This is consistent with papers that receive acceptance after the preprint is posted and update their repo but not the arXiv abstract immediately.\n\n---\n\n## 6. Does it have released code?\n\n**Yes.** Code is available at: https://github.com/chili-lab/Spherical-Steering\n\nThe repository contains:\n- `spherical_steering.py` - Core steering logic with geometric intervention hooks\n- `get_activations.py` - Extracts last-token hidden states from answer pairs\n- `get_prototypes.py` - Computes steering targets with question-level splits\n- `evaluate_mc.py` - Multiple-choice evaluation (MC1/MC2/MC3 metrics)\n- `evaluate_llm_judge.py` - Open-ended generation with truth/information scoring\n- `utils.py` - Data loading and activation extraction utilities\n- Quickstart scripts for Llama3.1-8B-Instruct and Qwen2.5-7B-Instruct\n\nLicense: CC-BY-NC-SA 4.0, Python 3.10, dependencies in environment.yml.\n\n---\n\n## Summary\n\nAll major claims check out as real. The paper exists, uses a vMF confidence gate, achieves substantial TruthfulQA MC1 improvements (+12-16 percentage points), operates per-token at inference, appears accepted at ICML 2026 (per GitHub repo tagging), and has publicly released code.\n\nSources:\n- [arXiv:2602.08169 Abstract](https://arxiv.org/abs/2602.08169)\n- [arXiv:2602.08169 HTML](https://arxiv.org/html/2602.08169v1)\n- [GitHub: chili-lab/Spherical-Steering](https://github.com/chili-lab/Spherical-Steering)\n- [ResearchGate Publication](https://www.researchgate.net/publication/400605038_Spherical_Steering_Geometry-Aware_Activation_Rotation_for_Language_Models)"
      }
    ],
    "totalDurationMs": 68807,
    "totalTokens": 18245,
    "totalToolUseCount": 9,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2429,
      "cache_read_input_tokens": 14598,
      "output_tokens": 1217,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2429
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1217,
          "cache_read_input_tokens": 14598,
          "cache_creation_input_tokens": 2429,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2429,
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
      "otherToolCount": 9
    }
  },
  "sourceToolAssistantUUID": "ac3ed160-7d06-4cdc-8035-6417ddd23714",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73813be2-f916-4121-a2d7-450b728cd138",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-16T08:47:14.323Z_

<details><summary>↩ Tool result · `toolu_014JP1Fmv6oJKEMhNRz6Dtu6`</summary>

```text
Now I have enough information to provide a comprehensive answer. Here is my findings report:

---

## Paper 1: "Minimizing Collateral Damage in Activation Steering" (arXiv 2605.01167)

**Does it exist?** YES. It is a real paper on arXiv at https://arxiv.org/abs/2605.01167, submitted May 1, 2026, by Tam Nguyen, Tu Anh Nguyen, Sina Alemohammad, and Richard G. Baraniuk.

**What does it actually do?** The paper introduces COAST (COllateral-damage Minimizing Activation STeering). It formalizes "collateral damage" in activation steering -- the unintended changes along non-target feature directions when you steer along a target direction. It models steering as a constrained optimization problem and finds a new activation that minimizes the expected squared collateral change weighted by the empirical second-moment matrix of activations. COAST uses differential geometry to traverse the solution space. It strictly generalizes SLERP (the norm-preserving version of ActAdd).

**Does it claim 30% ASR improvement?** YES, this claim is substantiated. The paper reports that COAST achieves up to a 30% improvement in Attack Success Rate (ASR) over Angular Steering and improves up to 20% in accuracy compared to ActAdd at the same ASR. Specifically for Gemma-2-9B and Llama-3.2-3B, COAST improves both ASR and task accuracy simultaneously. Models tested include: Llama-3.2-3B-Instruct, Llama-3.1-8B-Instruct, Qwen2.5-14B-Instruct, and Gemma-2-9B-IT.

---

## Paper 2: "Hallucination Basins: A Dynamic Framework for Understanding and Controlling LLM Hallucinations" (arXiv 2604.04743)

**Does it exist?** YES. It is a real paper on arXiv at https://arxiv.org/abs/2604.04743, published April 6, 2026, by Kalyan Cherukuri and Lav R. Varshney.

**Does it propose "Adaptive Geometry-Aware Steering"?** YES. The paper introduces geometry-aware steering that can reduce hallucination probability without retraining. Search results confirm it introduces an "Adaptive Geometry-Aware Steering" method as part of their framework.

**Does it use centroid-difference vectors?** YES. The steering vector is computed as the difference between class centroids (factual vs. hallucinated response representations). The paper shows 3D PCA projections of middle-layer hidden activations with factual and hallucination samples, along with the interpolation trajectory between their centroids.

**Does it use Euclidean distance trigger with a scalar logistic-regression controller?** PARTIALLY CONFIRMED / UNCERTAIN. The paper defines a steering policy that intervenes proportionally based on proximity to the nearest hallucination basin. However, my searches could NOT confirm the specific claims about a "Euclidean distance trigger" or a "scalar logistic-regression controller." The site-specific search for terms like "logistic," "scalar," "trigger," and "Euclidean distance" within the paper returned no results. The paper may use these mechanisms internally, but I cannot verify these specific technical details from web search alone -- you would need to read the full paper to confirm.

**What scale models (1B-3B)?** YES, confirmed. The paper was evaluated on: Llama 3.2-1B, Llama 3.2-3B, Gemma-2-2B, and Qwen2-1.5B -- all in the 1B-3B range. Benchmarks used: HaluEval, MuSiQue, FEVER, and TruthfulQA.

---

## Summary

| Claim | Verified? |
|-------|-----------|
| Paper 1 exists at arXiv 2605.01167 | YES |
| Paper 1 is called COAST | YES |
| Paper 1 uses constrained optimization for steering | YES |
| Paper 1 claims 30% ASR improvement | YES (up to 30% over Angular Steering) |
| Paper 2 exists at arXiv 2604.04743 | YES |
| Paper 2 proposes Adaptive Geometry-Aware Steering | YES |
| Paper 2 uses centroid-difference vectors | YES |
| Paper 2 uses Euclidean distance trigger | UNCONFIRMED (proximity-based intervention is confirmed, but "Euclidean" specifically not verified) |
| Paper 2 uses scalar logistic-regression controller | UNCONFIRMED (not found in search results) |
| Paper 2 uses 1B-3B scale models | YES (Llama 3.2-1B/3B, Gemma-2-2B, Qwen2-1.5B) |

Sources:
- [Minimizing Collateral Damage in Activation Steering - arXiv](https://arxiv.org/abs/2605.01167)
- [Minimizing Collateral Damage in Activation Steering - HTML](https://arxiv.org/html/2605.01167v1)
- [Hallucination Basins - arXiv](https://arxiv.org/abs/2604.04743)
- [Hallucination Basins - HTML](https://arxiv.org/html/2604.04743v1)
- [Activation Steering in 2026: A Practitioner's Field Guide](https://subhadipmitra.com/blog/2026/activation-steering-field-guide/)

agentId: a76d532389c051c6c (use SendMessage with to: 'a76d532389c051c6c' to continue this agent)
&lt;usage>total_tokens: 23227
tool_uses: 14
duration_ms: 93319&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cb462a7f-7f26-4342-8c62-0fde5c9c6cb2",
  "isSidechain": false,
  "promptId": "fa61ad10-397c-4783-9490-82353cc0b8e8",
  "type": "user",
  "uuid": "a5c8b13b-cf23-4d69-bcf2-4126b24d009d",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Use WebSearch to find and verify these two papers:\n\n1. \"Minimizing Collateral Damage in Activation Steering\" (arXiv 2605.01167, May 2026) - also called COAST. Does it exist? What does it actually do? Does it claim 30% ASR improvement?\n\n2. \"Hallucination Basins: A Dynamic Framework for Understanding and Controlling LLM Hallucinations\" (arXiv 2604.04743, April 2026). Does it exist? Does it propose \"Adaptive Geometry-Aware Steering\"? Does it use centroid-difference vectors and Euclidean distance trigger with a scalar logistic-regression controller? What scale models (1B-3B)?\n\nSearch for:\n- \"Minimizing Collateral Damage activation steering\" OR \"arxiv 2605.01167\"\n- \"COAST activation steering constrained optimization\"\n- \"Hallucination Basins\" OR \"arxiv 2604.04743\"\n- \"geometry-aware steering hallucination basins\"",
    "agentId": "a76d532389c051c6c",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have enough information to provide a comprehensive answer. Here is my findings report:\n\n---\n\n## Paper 1: \"Minimizing Collateral Damage in Activation Steering\" (arXiv 2605.01167)\n\n**Does it exist?** YES. It is a real paper on arXiv at https://arxiv.org/abs/2605.01167, submitted May 1, 2026, by Tam Nguyen, Tu Anh Nguyen, Sina Alemohammad, and Richard G. Baraniuk.\n\n**What does it actually do?** The paper introduces COAST (COllateral-damage Minimizing Activation STeering). It formalizes \"collateral damage\" in activation steering -- the unintended changes along non-target feature directions when you steer along a target direction. It models steering as a constrained optimization problem and finds a new activation that minimizes the expected squared collateral change weighted by the empirical second-moment matrix of activations. COAST uses differential geometry to traverse the solution space. It strictly generalizes SLERP (the norm-preserving version of ActAdd).\n\n**Does it claim 30% ASR improvement?** YES, this claim is substantiated. The paper reports that COAST achieves up to a 30% improvement in Attack Success Rate (ASR) over Angular Steering and improves up to 20% in accuracy compared to ActAdd at the same ASR. Specifically for Gemma-2-9B and Llama-3.2-3B, COAST improves both ASR and task accuracy simultaneously. Models tested include: Llama-3.2-3B-Instruct, Llama-3.1-8B-Instruct, Qwen2.5-14B-Instruct, and Gemma-2-9B-IT.\n\n---\n\n## Paper 2: \"Hallucination Basins: A Dynamic Framework for Understanding and Controlling LLM Hallucinations\" (arXiv 2604.04743)\n\n**Does it exist?** YES. It is a real paper on arXiv at https://arxiv.org/abs/2604.04743, published April 6, 2026, by Kalyan Cherukuri and Lav R. Varshney.\n\n**Does it propose \"Adaptive Geometry-Aware Steering\"?** YES. The paper introduces geometry-aware steering that can reduce hallucination probability without retraining. Search results confirm it introduces an \"Adaptive Geometry-Aware Steering\" method as part of their framework.\n\n**Does it use centroid-difference vectors?** YES. The steering vector is computed as the difference between class centroids (factual vs. hallucinated response representations). The paper shows 3D PCA projections of middle-layer hidden activations with factual and hallucination samples, along with the interpolation trajectory between their centroids.\n\n**Does it use Euclidean distance trigger with a scalar logistic-regression controller?** PARTIALLY CONFIRMED / UNCERTAIN. The paper defines a steering policy that intervenes proportionally based on proximity to the nearest hallucination basin. However, my searches could NOT confirm the specific claims about a \"Euclidean distance trigger\" or a \"scalar logistic-regression controller.\" The site-specific search for terms like \"logistic,\" \"scalar,\" \"trigger,\" and \"Euclidean distance\" within the paper returned no results. The paper may use these mechanisms internally, but I cannot verify these specific technical details from web search alone -- you would need to read the full paper to confirm.\n\n**What scale models (1B-3B)?** YES, confirmed. The paper was evaluated on: Llama 3.2-1B, Llama 3.2-3B, Gemma-2-2B, and Qwen2-1.5B -- all in the 1B-3B range. Benchmarks used: HaluEval, MuSiQue, FEVER, and TruthfulQA.\n\n---\n\n## Summary\n\n| Claim | Verified? |\n|-------|-----------|\n| Paper 1 exists at arXiv 2605.01167 | YES |\n| Paper 1 is called COAST | YES |\n| Paper 1 uses constrained optimization for steering | YES |\n| Paper 1 claims 30% ASR improvement | YES (up to 30% over Angular Steering) |\n| Paper 2 exists at arXiv 2604.04743 | YES |\n| Paper 2 proposes Adaptive Geometry-Aware Steering | YES |\n| Paper 2 uses centroid-difference vectors | YES |\n| Paper 2 uses Euclidean distance trigger | UNCONFIRMED (proximity-based intervention is confirmed, but \"Euclidean\" specifically not verified) |\n| Paper 2 uses scalar logistic-regression controller | UNCONFIRMED (not found in search results) |\n| Paper 2 uses 1B-3B scale models | YES (Llama 3.2-1B/3B, Gemma-2-2B, Qwen2-1.5B) |\n\nSources:\n- [Minimizing Collateral Damage in Activation Steering - arXiv](https://arxiv.org/abs/2605.01167)\n- [Minimizing Collateral Damage in Activation Steering - HTML](https://arxiv.org/html/2605.01167v1)\n- [Hallucination Basins - arXiv](https://arxiv.org/abs/2604.04743)\n- [Hallucination Basins - HTML](https://arxiv.org/html/2604.04743v1)\n- [Activation Steering in 2026: A Practitioner's Field Guide](https://subhadipmitra.com/blog/2026/activation-steering-field-guide/)"
      }
    ],
    "totalDurationMs": 93319,
    "totalTokens": 23227,
    "totalToolUseCount": 14,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2055,
      "cache_read_input_tokens": 19810,
      "output_tokens": 1361,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2055
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1361,
          "cache_read_input_tokens": 19810,
          "cache_creation_input_tokens": 2055,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2055,
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
      "otherToolCount": 14
    }
  },
  "sourceToolAssistantUUID": "cb462a7f-7f26-4342-8c62-0fde5c9c6cb2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73813be2-f916-4121-a2d7-450b728cd138",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 16_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-16 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "a5c8b13b-cf23-4d69-bcf2-4126b24d009d",
  "sessionId": "73813be2-f916-4121-a2d7-450b728cd138"
}
```

---

### Runtime record

_source line 17_

```json
{
  "type": "ai-title",
  "aiTitle": "Geometry-triggered sentence-level hallucination steering",
  "sessionId": "73813be2-f916-4121-a2d7-450b728cd138"
}
```

---

### Tool result

_source line 18 · 2026-05-16T08:47:33.742Z_

<details><summary>↩ Tool result · `toolu_016Yw5XdgpT8Fu7YLv8JhQhC`</summary>

```text
Here is a comprehensive summary of my findings on whether "sentence-level gating" or claim-level activation steering/intervention for hallucination reduction already exists in prior work.

---

## Verdict: The core idea of sentence-level or claim-level selective intervention during generation DOES exist in multiple prior works (2025-2026).

There is a rich and rapidly growing body of work that performs sub-sequence-level (sentence, claim, or token) selective intervention during generation to reduce hallucinations. The exact phrase "sentence-level gating" is not used as a named method, but the underlying concept is well-covered by several papers. Here are the most relevant:

---

## Directly Relevant Prior Work

### 1. SENTINEL: "Mitigating Object Hallucinations via Sentence-Level Early Intervention" (July 2025)
- **arxiv**: [2507.12455](https://arxiv.org/abs/2507.12455)
- **What it does**: Explicitly performs sentence-level intervention. It identifies that hallucinations emerge at early stages of generation and propagate, then applies preference learning (C-DPO) that emphasizes discriminative learning *at the sentence level* where hallucinations initially manifest.
- **Relevance**: This is the closest match to "sentence-level gating" -- it literally uses the phrase "sentence-level early intervention" in its title.

### 2. Monitoring Decoding (MD): "Mitigating Hallucination via Evaluating the Factuality of Partial Response during Generation" (March 2025, ACL 2025 Findings)
- **arxiv**: [2503.03106](https://arxiv.org/abs/2503.03106)
- **What it does**: Monitors the factuality of partial responses *during generation* in real-time. When it detects hallucination-prone tokens, it applies targeted intervention via a tree-based decoding strategy -- intervening only on crucial tokens rather than resampling entire responses.
- **Relevance**: This is sub-sequence granularity intervention during generation, which is the core mechanic of "sentence-level gating."

### 3. FASB: "Steering When Necessary: Flexible Steering Large Language Models with Backtracking" (NeurIPS 2025)
- **arxiv**: [2508.17621](https://arxiv.org/abs/2508.17621)
- **What it does**: Dynamically determines *both the necessity and strength* of activation steering intervention during generation by probing activation states. Only intervenes when needed (conditional/selective steering). Includes a backtracking mechanism to correct tokens after deviation is detected.
- **Relevance**: This is exactly "selective activation steering" -- it gates whether to apply steering on a per-token/per-step basis during generation.

### 4. Dynamic Multimodal Activation Steering (DMAS) (Feb 2026)
- **arxiv**: [2602.21704](https://arxiv.org/abs/2602.21704)
- **What it does**: Dynamically selects the most relevant steering vector based on the semantic content of the input. Constructs a semantic-based truthfulness steering vector database and applies context-aware interventions to specific attention heads during inference.
- **Relevance**: Dynamic/selective steering vector application -- the steering is not uniform but adapted to semantic context, similar in spirit to sentence-level gating.

### 5. Adaptive Activation Steering (ACT) (ACM Web Conference 2025)
- **arxiv**: [2406.00034](https://arxiv.org/abs/2406.00034)
- **What it does**: Uses unsupervised clustering to generate diverse steering vectors for different hallucination categories, and *adaptively adjusts steering intensity* based on the truthfulness content of activations.
- **Relevance**: Adaptive/conditional steering intensity -- another form of selective gating of the intervention.

### 6. PCNet: "Hallucination as an Anomaly: Dynamic Intervention via Probabilistic Circuits" (May 2026)
- **arxiv**: [2605.05953](https://arxiv.org/abs/2605.05953)
- **What it does**: Uses a Probabilistic Circuit as a *dynamic gate* that distinguishes hallucinated from factual hidden states at each decoding step, only triggering correction (contrastive decoding) when the latent geometry deviates from factual regions.
- **Relevance**: Per-token dynamic gating -- only applies correction when anomaly is detected. Explicitly addresses the problem that indiscriminate correction corrupts correct generations.

### 7. HaluGate (vLLM, Dec 2025)
- **Blog**: [vLLM Blog](https://blog.vllm.ai/2025/12/14/halugate.html)
- **What it does**: A production pipeline for token-level hallucination detection that gates whether verification is needed (Sentinel classifier) and then performs token-level detection of unsupported claims.
- **Relevance**: Production-grade "gating" for hallucination detection at token/span level.

---

## Summary Assessment

The "sentence-level gating" contribution is **not novel** as a concept. Multiple papers from 2025-2026 already implement:

1. **Selective/conditional intervention** -- only steering when the model is about to hallucinate (FASB, PCNet, Monitoring Decoding)
2. **Sentence-level granularity** -- explicitly operating at sentence boundaries (SENTINEL)
3. **Dynamic steering vector selection** -- adapting what steering to apply based on generation context (DMAS, ACT)
4. **Gating mechanisms** -- binary or soft gates that decide whether to intervene at each step (PCNet, HaluGate)

The specific *combination* of (a) activation steering (not just contrastive decoding) with (b) sentence-level granularity (not token-level) and (c) a learned gating mechanism might still be a novel specific instantiation, but the individual components and the general paradigm of "selectively intervening at sub-sequence granularity during generation to reduce hallucination" is well-established in the 2025-2026 literature.

---

Sources:
- [SENTINEL: Mitigating Object Hallucinations via Sentence-Level Early Intervention](https://arxiv.org/abs/2507.12455)
- [Monitoring Decoding: Mitigating Hallucination via Evaluating the Factuality of Partial Response during Generation](https://arxiv.org/abs/2503.03106)
- [Steering When Necessary: Flexible Steering Large Language Models with Backtracking (NeurIPS 2025)](https://arxiv.org/abs/2508.17621)
- [Dynamic Multimodal Activation Steering for Hallucination Mitigation in LVLMs](https://arxiv.org/abs/2602.21704)
- [Adaptive Activation Steering: A Tuning-Free LLM Truthfulness Improvement Method](https://arxiv.org/abs/2406.00034)
- [Hallucination as an Anomaly: Dynamic Intervention via Probabilistic Circuits](https://arxiv.org/abs/2605.05953)
- [HaluGate: Token-Level Truth (vLLM Blog)](https://blog.vllm.ai/2025/12/14/halugate.html)
- [Activation Steering Decoding (ACL 2025)](https://aclanthology.org/2025.acl-long.634/)
- [DMAS (OpenReview)](https://openreview.net/forum?id=YtWZdwEG5K)

agentId: a86501407b1f40153 (use SendMessage with to: 'a86501407b1f40153' to continue this agent)
&lt;usage>total_tokens: 28906
tool_uses: 17
duration_ms: 117129&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "149a2b8e-bf6d-46ec-91de-221f7f9553f3",
  "isSidechain": false,
  "promptId": "fa61ad10-397c-4783-9490-82353cc0b8e8",
  "type": "user",
  "uuid": "97e48ab8-2ff9-4c3e-8488-d8f81d42fdea",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Use WebSearch to find ANY papers that propose sentence-level or claim-level activation steering or intervention for hallucination reduction in LLMs. I need to check if the \"sentence-level gating\" contribution claimed by this idea already exists in prior work.\n\nSearch for:\n1. \"sentence-level activation steering hallucination\" 2025 2026\n2. \"claim-level intervention hallucination LLM\" 2025 2026\n3. \"selective activation steering\" OR \"selective steering\" hallucination 2025 2026\n4. \"sentence-level gating\" LLM generation 2025 2026\n5. \"granularity hallucination intervention\" OR \"claim-level hallucination suppression\"\n\nAlso search for \"Monitoring Decoding hallucination factuality partial response\" since this is cited in the key_references and may do something similar (intervening during generation at sub-sequence granularity).",
    "agentId": "a86501407b1f40153",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here is a comprehensive summary of my findings on whether \"sentence-level gating\" or claim-level activation steering/intervention for hallucination reduction already exists in prior work.\n\n---\n\n## Verdict: The core idea of sentence-level or claim-level selective intervention during generation DOES exist in multiple prior works (2025-2026).\n\nThere is a rich and rapidly growing body of work that performs sub-sequence-level (sentence, claim, or token) selective intervention during generation to reduce hallucinations. The exact phrase \"sentence-level gating\" is not used as a named method, but the underlying concept is well-covered by several papers. Here are the most relevant:\n\n---\n\n## Directly Relevant Prior Work\n\n### 1. SENTINEL: \"Mitigating Object Hallucinations via Sentence-Level Early Intervention\" (July 2025)\n- **arxiv**: [2507.12455](https://arxiv.org/abs/2507.12455)\n- **What it does**: Explicitly performs sentence-level intervention. It identifies that hallucinations emerge at early stages of generation and propagate, then applies preference learning (C-DPO) that emphasizes discriminative learning *at the sentence level* where hallucinations initially manifest.\n- **Relevance**: This is the closest match to \"sentence-level gating\" -- it literally uses the phrase \"sentence-level early intervention\" in its title.\n\n### 2. Monitoring Decoding (MD): \"Mitigating Hallucination via Evaluating the Factuality of Partial Response during Generation\" (March 2025, ACL 2025 Findings)\n- **arxiv**: [2503.03106](https://arxiv.org/abs/2503.03106)\n- **What it does**: Monitors the factuality of partial responses *during generation* in real-time. When it detects hallucination-prone tokens, it applies targeted intervention via a tree-based decoding strategy -- intervening only on crucial tokens rather than resampling entire responses.\n- **Relevance**: This is sub-sequence granularity intervention during generation, which is the core mechanic of \"sentence-level gating.\"\n\n### 3. FASB: \"Steering When Necessary: Flexible Steering Large Language Models with Backtracking\" (NeurIPS 2025)\n- **arxiv**: [2508.17621](https://arxiv.org/abs/2508.17621)\n- **What it does**: Dynamically determines *both the necessity and strength* of activation steering intervention during generation by probing activation states. Only intervenes when needed (conditional/selective steering). Includes a backtracking mechanism to correct tokens after deviation is detected.\n- **Relevance**: This is exactly \"selective activation steering\" -- it gates whether to apply steering on a per-token/per-step basis during generation.\n\n### 4. Dynamic Multimodal Activation Steering (DMAS) (Feb 2026)\n- **arxiv**: [2602.21704](https://arxiv.org/abs/2602.21704)\n- **What it does**: Dynamically selects the most relevant steering vector based on the semantic content of the input. Constructs a semantic-based truthfulness steering vector database and applies context-aware interventions to specific attention heads during inference.\n- **Relevance**: Dynamic/selective steering vector application -- the steering is not uniform but adapted to semantic context, similar in spirit to sentence-level gating.\n\n### 5. Adaptive Activation Steering (ACT) (ACM Web Conference 2025)\n- **arxiv**: [2406.00034](https://arxiv.org/abs/2406.00034)\n- **What it does**: Uses unsupervised clustering to generate diverse steering vectors for different hallucination categories, and *adaptively adjusts steering intensity* based on the truthfulness content of activations.\n- **Relevance**: Adaptive/conditional steering intensity -- another form of selective gating of the intervention.\n\n### 6. PCNet: \"Hallucination as an Anomaly: Dynamic Intervention via Probabilistic Circuits\" (May 2026)\n- **arxiv**: [2605.05953](https://arxiv.org/abs/2605.05953)\n- **What it does**: Uses a Probabilistic Circuit as a *dynamic gate* that distinguishes hallucinated from factual hidden states at each decoding step, only triggering correction (contrastive decoding) when the latent geometry deviates from factual regions.\n- **Relevance**: Per-token dynamic gating -- only applies correction when anomaly is detected. Explicitly addresses the problem that indiscriminate correction corrupts correct generations.\n\n### 7. HaluGate (vLLM, Dec 2025)\n- **Blog**: [vLLM Blog](https://blog.vllm.ai/2025/12/14/halugate.html)\n- **What it does**: A production pipeline for token-level hallucination detection that gates whether verification is needed (Sentinel classifier) and then performs token-level detection of unsupported claims.\n- **Relevance**: Production-grade \"gating\" for hallucination detection at token/span level.\n\n---\n\n## Summary Assessment\n\nThe \"sentence-level gating\" contribution is **not novel** as a concept. Multiple papers from 2025-2026 already implement:\n\n1. **Selective/conditional intervention** -- only steering when the model is about to hallucinate (FASB, PCNet, Monitoring Decoding)\n2. **Sentence-level granularity** -- explicitly operating at sentence boundaries (SENTINEL)\n3. **Dynamic steering vector selection** -- adapting what steering to apply based on generation context (DMAS, ACT)\n4. **Gating mechanisms** -- binary or soft gates that decide whether to intervene at each step (PCNet, HaluGate)\n\nThe specific *combination* of (a) activation steering (not just contrastive decoding) with (b) sentence-level granularity (not token-level) and (c) a learned gating mechanism might still be a novel specific instantiation, but the individual components and the general paradigm of \"selectively intervening at sub-sequence granularity during generation to reduce hallucination\" is well-established in the 2025-2026 literature.\n\n---\n\nSources:\n- [SENTINEL: Mitigating Object Hallucinations via Sentence-Level Early Intervention](https://arxiv.org/abs/2507.12455)\n- [Monitoring Decoding: Mitigating Hallucination via Evaluating the Factuality of Partial Response during Generation](https://arxiv.org/abs/2503.03106)\n- [Steering When Necessary: Flexible Steering Large Language Models with Backtracking (NeurIPS 2025)](https://arxiv.org/abs/2508.17621)\n- [Dynamic Multimodal Activation Steering for Hallucination Mitigation in LVLMs](https://arxiv.org/abs/2602.21704)\n- [Adaptive Activation Steering: A Tuning-Free LLM Truthfulness Improvement Method](https://arxiv.org/abs/2406.00034)\n- [Hallucination as an Anomaly: Dynamic Intervention via Probabilistic Circuits](https://arxiv.org/abs/2605.05953)\n- [HaluGate: Token-Level Truth (vLLM Blog)](https://blog.vllm.ai/2025/12/14/halugate.html)\n- [Activation Steering Decoding (ACL 2025)](https://aclanthology.org/2025.acl-long.634/)\n- [DMAS (OpenReview)](https://openreview.net/forum?id=YtWZdwEG5K)"
      }
    ],
    "totalDurationMs": 117129,
    "totalTokens": 28906,
    "totalToolUseCount": 17,
    "usage": {
      "input_tokens": 965,
      "cache_creation_input_tokens": 1182,
      "cache_read_input_tokens": 24940,
      "output_tokens": 1819,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1182
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 965,
          "output_tokens": 1819,
          "cache_read_input_tokens": 24940,
          "cache_creation_input_tokens": 1182,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1182,
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
      "otherToolCount": 17
    }
  },
  "sourceToolAssistantUUID": "149a2b8e-bf6d-46ec-91de-221f7f9553f3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73813be2-f916-4121-a2d7-450b728cd138",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-16T08:47:51.950Z_

<details><summary>↩ Tool result · `toolu_01AVGh5Er3wWkjFCe62QDN7b`</summary>

```text
Based on my research, here is a comprehensive answer to your five questions:

---

## Findings on arXiv 2605.05686

**1. Does it actually exist?**

Yes. The paper "Attractor Geometry of Transformer Memory: From Conflict Arbitration to Confident Hallucination" (arXiv:2605.05686) exists and is publicly available. It was submitted on May 7, 2026, authored by Qiyao Liang (MIT), Risto Miikkulainen (UT Austin / Cognizant), and Ila Fiete (MIT).

**2. Does it claim geometric margin achieves AUROC 0.858 on TruthfulQA (vs. entropy 0.656)?**

Yes, confirmed. The paper reports exactly those numbers:
- Geometric margin AUROC on TruthfulQA: **0.858**
- Entropy AUROC on TruthfulQA: **0.656**

They also report even stronger separation in other settings: margin AUROC = 1.000 vs. entropy 0.622 on pretrained knowledge (no adapter), and margin AUROC = 0.993 vs. entropy 0.968 on the synthetic LoRA task.

**3. Does it characterize hallucination as "basin absence"?**

Yes. The abstract explicitly states: "hallucination is basin absence: the hidden state drifts freely when no memorized basin exists." This is a core claim of the paper -- that hallucination occurs when the entity has no memorized attractor basin at all, as opposed to conflict which is "basin competition" between parametric and working memory.

**4. Does it note that "transfer to open-domain settings requires further study"?**

Yes. The paper acknowledges that while margin reaches TruthfulQA AUROC = 0.858, it "degrades on adversarial reasoning probes where no memorized basin exists," and explicitly states that "transfer to open-domain settings requires further study." They also note that "The scaling analyses cover 0.36B-14B parameters; RLHF behavior remains open."

**5. What models/scales does it test on?**

- Primary experiments: **Qwen2.5-3B-Instruct** (d=2,048, 36 layers)
- Scaling analysis: **12 instruction-tuned models spanning 0.36B to 14B parameters** across **four model families** (the specific family names beyond Qwen are not fully enumerated in the accessible portions of the paper)
- Two benchmarks used for the scaling evaluation
- The scaling law C = exp(-c/delta-bar) (with c approximately 5.9) is reported to collapse 21 (model, benchmark) data points across these 12 models

---

## Summary

All five claims you asked about are verified as accurate. The paper exists, reports the exact AUROC figures you cited, characterizes hallucination as "basin absence," acknowledges that open-domain transfer needs further study, and tests across 12 models from 0.36B to 14B parameters (with Qwen2.5-3B-Instruct as the primary model).

Sources:
- [arXiv:2605.05686 Abstract](https://arxiv.org/abs/2605.05686)
- [arXiv:2605.05686 Full HTML](https://arxiv.org/html/2605.05686)
- [The Fiete Lab @ MIT - Publications](https://fietelab.mit.edu/publications/)

agentId: a3045c8291cb930f7 (use SendMessage with to: 'a3045c8291cb930f7' to continue this agent)
&lt;usage>total_tokens: 24469
tool_uses: 19
duration_ms: 141442&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3f23fd55-8726-4661-a55e-3e04f34924b8",
  "isSidechain": false,
  "promptId": "fa61ad10-397c-4783-9490-82353cc0b8e8",
  "type": "user",
  "uuid": "aa51ffb6-592e-41ca-914f-98673940f8eb",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Use WebSearch to find and verify the paper \"Attractor Geometry of Transformer Memory: From Conflict Arbitration to Confident Hallucination\" (arXiv 2605.05686, May 2026). I need to know:\n1. Does it actually exist?\n2. Does it claim geometric margin achieves AUROC 0.858 on TruthfulQA (vs. entropy 0.656)?\n3. Does it characterize hallucination as \"basin absence\"?\n4. Does it note that \"transfer to open-domain settings requires further study\"?\n5. What models/scales does it test on?\n\nSearch for \"Attractor Geometry Transformer Memory\" and \"arxiv 2605.05686\" and \"hallucination basin absence attractor geometry 2026\".",
    "agentId": "a3045c8291cb930f7",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Based on my research, here is a comprehensive answer to your five questions:\n\n---\n\n## Findings on arXiv 2605.05686\n\n**1. Does it actually exist?**\n\nYes. The paper \"Attractor Geometry of Transformer Memory: From Conflict Arbitration to Confident Hallucination\" (arXiv:2605.05686) exists and is publicly available. It was submitted on May 7, 2026, authored by Qiyao Liang (MIT), Risto Miikkulainen (UT Austin / Cognizant), and Ila Fiete (MIT).\n\n**2. Does it claim geometric margin achieves AUROC 0.858 on TruthfulQA (vs. entropy 0.656)?**\n\nYes, confirmed. The paper reports exactly those numbers:\n- Geometric margin AUROC on TruthfulQA: **0.858**\n- Entropy AUROC on TruthfulQA: **0.656**\n\nThey also report even stronger separation in other settings: margin AUROC = 1.000 vs. entropy 0.622 on pretrained knowledge (no adapter), and margin AUROC = 0.993 vs. entropy 0.968 on the synthetic LoRA task.\n\n**3. Does it characterize hallucination as \"basin absence\"?**\n\nYes. The abstract explicitly states: \"hallucination is basin absence: the hidden state drifts freely when no memorized basin exists.\" This is a core claim of the paper -- that hallucination occurs when the entity has no memorized attractor basin at all, as opposed to conflict which is \"basin competition\" between parametric and working memory.\n\n**4. Does it note that \"transfer to open-domain settings requires further study\"?**\n\nYes. The paper acknowledges that while margin reaches TruthfulQA AUROC = 0.858, it \"degrades on adversarial reasoning probes where no memorized basin exists,\" and explicitly states that \"transfer to open-domain settings requires further study.\" They also note that \"The scaling analyses cover 0.36B-14B parameters; RLHF behavior remains open.\"\n\n**5. What models/scales does it test on?**\n\n- Primary experiments: **Qwen2.5-3B-Instruct** (d=2,048, 36 layers)\n- Scaling analysis: **12 instruction-tuned models spanning 0.36B to 14B parameters** across **four model families** (the specific family names beyond Qwen are not fully enumerated in the accessible portions of the paper)\n- Two benchmarks used for the scaling evaluation\n- The scaling law C = exp(-c/delta-bar) (with c approximately 5.9) is reported to collapse 21 (model, benchmark) data points across these 12 models\n\n---\n\n## Summary\n\nAll five claims you asked about are verified as accurate. The paper exists, reports the exact AUROC figures you cited, characterizes hallucination as \"basin absence,\" acknowledges that open-domain transfer needs further study, and tests across 12 models from 0.36B to 14B parameters (with Qwen2.5-3B-Instruct as the primary model).\n\nSources:\n- [arXiv:2605.05686 Abstract](https://arxiv.org/abs/2605.05686)\n- [arXiv:2605.05686 Full HTML](https://arxiv.org/html/2605.05686)\n- [The Fiete Lab @ MIT - Publications](https://fietelab.mit.edu/publications/)"
      }
    ],
    "totalDurationMs": 141442,
    "totalTokens": 24469,
    "totalToolUseCount": 19,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 500,
      "cache_read_input_tokens": 23138,
      "output_tokens": 830,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 500
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 830,
          "cache_read_input_tokens": 23138,
          "cache_creation_input_tokens": 500,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 500,
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
      "otherToolCount": 19
    }
  },
  "sourceToolAssistantUUID": "3f23fd55-8726-4661-a55e-3e04f34924b8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73813be2-f916-4121-a2d7-450b728cd138",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 20 · 2026-05-16T08:47:56.976Z_

Critical finding: there are multiple papers implementing selective/conditional steering that were NOT adequately discussed. Let me dig deeper into two of the most threatening competitors.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aa51ffb6-592e-41ca-914f-98673940f8eb",
  "isSidechain": false,
  "requestId": "req_011Cb5xWSsiG7kDR79vmCP3d",
  "type": "assistant",
  "uuid": "cc5894ec-a07c-42d6-a4b6-fd910fb275b3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73813be2-f916-4121-a2d7-450b728cd138",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EGNY2FUTCHZVep7KgHjKZG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3373,
      "cache_creation_input_tokens": 3959,
      "cache_read_input_tokens": 31428,
      "output_tokens": 925,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3959,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3373,
          "output_tokens": 925,
          "cache_read_input_tokens": 31428,
          "cache_creation_input_tokens": 3959,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3959
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

_source line 21 · 2026-05-16T08:48:02.514Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01VQPW4USPCaeGraLJ2i7E6c`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Verify FASB NeurIPS 2025 paper",
  "prompt": "Use WebSearch to find and verify the paper \"Steering When Necessary: Flexible Steering Large Language Models with Backtracking\" which is claimed to be at NeurIPS 2025 (arxiv 2508.17621). I need to know:\n1. Does it exist? (Note: arXiv 2508 means August 2025 submission)\n2. Does it use activation-space probing to decide WHEN to apply steering?\n3. Does it include a backtracking mechanism?\n4. What is its actual intervention granularity (token-level, sentence-level, or something else)?\n5. What benchmarks does it evaluate on?\n6. Is it actually accepted at NeurIPS 2025?\n\nSearch for \"Steering When Necessary Flexible Steering Backtracking\" and \"arxiv 2508.17621\" and \"FASB activation steering selective\". Also search for \"flexible activation steering backtracking NeurIPS 2025\"."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cc5894ec-a07c-42d6-a4b6-fd910fb275b3",
  "isSidechain": false,
  "requestId": "req_011Cb5xWSsiG7kDR79vmCP3d",
  "type": "assistant",
  "uuid": "02c5a297-9acc-47d4-badc-dac0ffdc3770",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73813be2-f916-4121-a2d7-450b728cd138",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EGNY2FUTCHZVep7KgHjKZG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3373,
      "cache_creation_input_tokens": 3959,
      "cache_read_input_tokens": 31428,
      "output_tokens": 925,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3959,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3373,
          "output_tokens": 925,
          "cache_read_input_tokens": 31428,
          "cache_creation_input_tokens": 3959,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3959
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

_source line 22 · 2026-05-16T08:48:06.147Z_

<details open><summary>🔧 Tool call — Agent · `toolu_016v2YUVxRC3NaGQ1cWbFrLX`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Verify SENTINEL paper",
  "prompt": "Use WebSearch to find and verify the paper \"SENTINEL: Mitigating Object Hallucinations via Sentence-Level Early Intervention\" (arxiv 2507.12455, July 2025). I need to know:\n1. Does it exist?\n2. Is it about text LLMs or vision-language models (VLMs)?\n3. Does it apply activation steering at sentence level, or does it use a different mechanism (like preference learning)?\n4. What is its actual method for \"sentence-level intervention\"?\n5. Is it about factual hallucination in text generation, or object hallucination in image captioning?\n\nSearch for \"SENTINEL sentence-level early intervention hallucination\" and \"arxiv 2507.12455\". Also search for \"sentence level hallucination mitigation 2025\"."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "02c5a297-9acc-47d4-badc-dac0ffdc3770",
  "isSidechain": false,
  "requestId": "req_011Cb5xWSsiG7kDR79vmCP3d",
  "type": "assistant",
  "uuid": "98d9786d-489a-47b3-ba3e-8a31fdb0a145",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73813be2-f916-4121-a2d7-450b728cd138",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EGNY2FUTCHZVep7KgHjKZG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3373,
      "cache_creation_input_tokens": 3959,
      "cache_read_input_tokens": 31428,
      "output_tokens": 925,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3959,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3373,
          "output_tokens": 925,
          "cache_read_input_tokens": 31428,
          "cache_creation_input_tokens": 3959,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3959
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

_source line 23 · 2026-05-16T08:48:11.826Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01H9CWFwhGp22VDEKvYrKQwb`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Search recent concurrent work May 2026",
  "prompt": "Use WebSearch to find the MOST RECENT papers (March-May 2026) on activation steering for hallucination reduction that might compete with a \"geometry-triggered sentence-level steering\" approach. I need to check if there are concurrent submissions the generator may have missed.\n\nSearch for:\n1. \"activation steering hallucination 2026\" site:arxiv.org\n2. \"geometry-aware steering hallucination\" 2026\n3. \"selective steering hallucination detection\" 2026\n4. \"claim-level hallucination intervention decoding\" 2026\n5. \"Mahalanobis distance hallucination steering\" 2026\n6. \"sentence boundary steering LLM\" 2026\n\nAlso search for:\n7. \"PCNet hallucination probabilistic circuits\" to verify this paper (arxiv 2605.05953)\n8. \"HELIX tethered reasoning Mahalanobis\" OR \"arxiv 2602.17691\" to verify this paper's actual mechanism"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "98d9786d-489a-47b3-ba3e-8a31fdb0a145",
  "isSidechain": false,
  "requestId": "req_011Cb5xWSsiG7kDR79vmCP3d",
  "type": "assistant",
  "uuid": "5dc037e5-b2e3-4a18-9d3d-323b68a358f5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73813be2-f916-4121-a2d7-450b728cd138",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EGNY2FUTCHZVep7KgHjKZG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3373,
      "cache_creation_input_tokens": 3959,
      "cache_read_input_tokens": 31428,
      "output_tokens": 925,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3959,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3373,
          "output_tokens": 925,
          "cache_read_input_tokens": 31428,
          "cache_creation_input_tokens": 3959,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3959
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

_source line 24 · 2026-05-16T08:48:49.642Z_

<details><summary>↩ Tool result · `toolu_016v2YUVxRC3NaGQ1cWbFrLX`</summary>

```text
I now have comprehensive information to answer all your questions. Here are my findings:

---

## Answers to Your Questions About SENTINEL (arXiv 2507.12455)

### 1. Does it exist?

Yes, confirmed. The paper "Mitigating Object Hallucinations via Sentence-Level Early Intervention" exists at arXiv 2507.12455, submitted July 16, 2025. It was also accepted at ICCV 2025 (published in OpenAccess proceedings).

### 2. Is it about text LLMs or vision-language models (VLMs)?

It is about **multimodal large language models (MLLMs) / vision-language models**. It addresses hallucinations where models fabricate content that contradicts visual inputs. This is squarely in the VLM domain, not text-only LLMs.

### 3. Does it apply activation steering at sentence level, or a different mechanism?

It does **NOT** use activation steering. It uses **preference learning** -- specifically a novel variant called **C-DPO (Context-aware Direct Preference Optimization)**. The "sentence-level" aspect refers to constructing preference pairs and applying the DPO loss at the sentence granularity, not to any inference-time activation manipulation.

### 4. What is its actual method for "sentence-level intervention"?

The full name is SENTINEL = "Sentence-level Early iNtervention Through IN-domain prEference Learning." The method works in six steps:

1. Generate multiple in-domain responses conditioned on input image, prompt, and context.
2. Extract all mentioned objects from each generated sentence.
3. Validate object existence using two open-vocabulary object detectors via cross-referencing.
4. Classify sentences as hallucinated or non-hallucinated based on detector results.
5. Extend generation context with verified non-hallucinated sentences to guide subsequent outputs (iterative bootstrapping of preference data).
6. Fine-tune the model using C-DPO loss that emphasizes discriminative learning at the sentence level where hallucinations first manifest.

The key insight is that hallucinations emerge early in generation and propagate -- so building sentence-level preference pairs and training with C-DPO targets the root cause.

### 5. Is it about factual hallucination in text generation, or object hallucination in image captioning?

It is about **object hallucination in image captioning/description tasks** for VLMs. The hallucinations it targets are fabricated objects that are not present in the input image. It evaluates on Object HalBench and AMBER -- both are benchmarks for object hallucination in vision-language tasks.

---

## Summary

SENTINEL is a VLM paper (not text LLM), targeting object hallucination (not factual/knowledge hallucination), using preference learning via C-DPO (not activation steering). The "sentence-level early intervention" refers to constructing training signal at sentence granularity during preference optimization, motivated by the finding that hallucinations propagate from early sentences.

Sources:
- [arXiv 2507.12455 - Mitigating Object Hallucinations via Sentence-Level Early Intervention](https://arxiv.org/abs/2507.12455)
- [ICCV 2025 Paper PDF](https://openaccess.thecvf.com/content/ICCV2025/papers/Peng_Mitigating_Object_Hallucinations_via_Sentence-Level_Early_Intervention_ICCV_2025_paper.pdf)
- [SENTINEL Framework Reduces Hallucinations In Multimodal Large Language Models - QuantumZeitgeist](https://quantumzeitgeist.com/sentinel-framework-reduces-hallucinations-in-multimodal-large-language-models/)
- [ResearchGate - PDF](https://www.researchgate.net/publication/393771584_Mitigating_Object_Hallucinations_via_Sentence-Level_Early_Intervention)

agentId: a603bc451514e7c86 (use SendMessage with to: 'a603bc451514e7c86' to continue this agent)
&lt;usage>total_tokens: 15502
tool_uses: 5
duration_ms: 43492&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "98d9786d-489a-47b3-ba3e-8a31fdb0a145",
  "isSidechain": false,
  "promptId": "fa61ad10-397c-4783-9490-82353cc0b8e8",
  "type": "user",
  "uuid": "904324e5-9125-4b2d-9028-28d14b643694",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Use WebSearch to find and verify the paper \"SENTINEL: Mitigating Object Hallucinations via Sentence-Level Early Intervention\" (arxiv 2507.12455, July 2025). I need to know:\n1. Does it exist?\n2. Is it about text LLMs or vision-language models (VLMs)?\n3. Does it apply activation steering at sentence level, or does it use a different mechanism (like preference learning)?\n4. What is its actual method for \"sentence-level intervention\"?\n5. Is it about factual hallucination in text generation, or object hallucination in image captioning?\n\nSearch for \"SENTINEL sentence-level early intervention hallucination\" and \"arxiv 2507.12455\". Also search for \"sentence level hallucination mitigation 2025\".",
    "agentId": "a603bc451514e7c86",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "I now have comprehensive information to answer all your questions. Here are my findings:\n\n---\n\n## Answers to Your Questions About SENTINEL (arXiv 2507.12455)\n\n### 1. Does it exist?\n\nYes, confirmed. The paper \"Mitigating Object Hallucinations via Sentence-Level Early Intervention\" exists at arXiv 2507.12455, submitted July 16, 2025. It was also accepted at ICCV 2025 (published in OpenAccess proceedings).\n\n### 2. Is it about text LLMs or vision-language models (VLMs)?\n\nIt is about **multimodal large language models (MLLMs) / vision-language models**. It addresses hallucinations where models fabricate content that contradicts visual inputs. This is squarely in the VLM domain, not text-only LLMs.\n\n### 3. Does it apply activation steering at sentence level, or a different mechanism?\n\nIt does **NOT** use activation steering. It uses **preference learning** -- specifically a novel variant called **C-DPO (Context-aware Direct Preference Optimization)**. The \"sentence-level\" aspect refers to constructing preference pairs and applying the DPO loss at the sentence granularity, not to any inference-time activation manipulation.\n\n### 4. What is its actual method for \"sentence-level intervention\"?\n\nThe full name is SENTINEL = \"Sentence-level Early iNtervention Through IN-domain prEference Learning.\" The method works in six steps:\n\n1. Generate multiple in-domain responses conditioned on input image, prompt, and context.\n2. Extract all mentioned objects from each generated sentence.\n3. Validate object existence using two open-vocabulary object detectors via cross-referencing.\n4. Classify sentences as hallucinated or non-hallucinated based on detector results.\n5. Extend generation context with verified non-hallucinated sentences to guide subsequent outputs (iterative bootstrapping of preference data).\n6. Fine-tune the model using C-DPO loss that emphasizes discriminative learning at the sentence level where hallucinations first manifest.\n\nThe key insight is that hallucinations emerge early in generation and propagate -- so building sentence-level preference pairs and training with C-DPO targets the root cause.\n\n### 5. Is it about factual hallucination in text generation, or object hallucination in image captioning?\n\nIt is about **object hallucination in image captioning/description tasks** for VLMs. The hallucinations it targets are fabricated objects that are not present in the input image. It evaluates on Object HalBench and AMBER -- both are benchmarks for object hallucination in vision-language tasks.\n\n---\n\n## Summary\n\nSENTINEL is a VLM paper (not text LLM), targeting object hallucination (not factual/knowledge hallucination), using preference learning via C-DPO (not activation steering). The \"sentence-level early intervention\" refers to constructing training signal at sentence granularity during preference optimization, motivated by the finding that hallucinations propagate from early sentences.\n\nSources:\n- [arXiv 2507.12455 - Mitigating Object Hallucinations via Sentence-Level Early Intervention](https://arxiv.org/abs/2507.12455)\n- [ICCV 2025 Paper PDF](https://openaccess.thecvf.com/content/ICCV2025/papers/Peng_Mitigating_Object_Hallucinations_via_Sentence-Level_Early_Intervention_ICCV_2025_paper.pdf)\n- [SENTINEL Framework Reduces Hallucinations In Multimodal Large Language Models - QuantumZeitgeist](https://quantumzeitgeist.com/sentinel-framework-reduces-hallucinations-in-multimodal-large-language-models/)\n- [ResearchGate - PDF](https://www.researchgate.net/publication/393771584_Mitigating_Object_Hallucinations_via_Sentence-Level_Early_Intervention)"
      }
    ],
    "totalDurationMs": 43492,
    "totalTokens": 15502,
    "totalToolUseCount": 5,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1091,
      "cache_read_input_tokens": 13469,
      "output_tokens": 941,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1091
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 941,
          "cache_read_input_tokens": 13469,
          "cache_creation_input_tokens": 1091,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1091,
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
      "otherToolCount": 5
    }
  },
  "sourceToolAssistantUUID": "98d9786d-489a-47b3-ba3e-8a31fdb0a145",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73813be2-f916-4121-a2d7-450b728cd138",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 25_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-16 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "904324e5-9125-4b2d-9028-28d14b643694",
  "sessionId": "73813be2-f916-4121-a2d7-450b728cd138"
}
```

---

### Runtime record

_source line 26_

```json
{
  "type": "ai-title",
  "aiTitle": "Geometry-triggered sentence-level hallucination steering",
  "sessionId": "73813be2-f916-4121-a2d7-450b728cd138"
}
```

---

### Tool result

_source line 27 · 2026-05-16T08:49:11.025Z_

<details><summary>↩ Tool result · `toolu_01VQPW4USPCaeGraLJ2i7E6c`</summary>

```text
Based on my comprehensive search, here are the findings for each of your questions:

---

## Results for "Steering When Necessary: Flexible Steering Large Language Models with Backtracking" (arXiv 2508.17621)

### 1. Does it exist?

**Yes.** The paper exists at arXiv 2508.17621, submitted August 25, 2025, with a revised version on October 1, 2025. The authors are Zifeng Cheng, Jinwei Gan, Zhiwei Jiang, Cong Wang, Yafeng Yin, Xiang Luo, Yuchen Fu, and Qing Gu. Since arXiv 2508 corresponds to August 2025 submissions, the timeline is consistent.

### 2. Does it use activation-space probing to decide WHEN to apply steering?

**Yes.** FASB uses a probe-based classifier trained on internal activation states (specifically attention heads) to dynamically determine whether intervention is necessary at any given point in generation. The classifier tracks the internal states of the LLM during generation, considering both the question and the generated content so far, to assess whether the model is deviating from desired behavior. This is explicitly called the "Probe method" in the paper.

### 3. Does it include a backtracking mechanism?

**Yes.** The paper explicitly proposes a backtracking mechanism. The key insight is that intervening *after* detecting a deviation is often too late. So when deviation is detected, the mechanism "steps back a few tokens" and then performs activation steering to regenerate those tokens, steering generation toward the desired direction.

### 4. What is its actual intervention granularity?

**Token-level.** The intervention operates at the token level. The classifier monitors internal states during token-by-token generation and determines both *whether* to intervene and the *strength* of intervention. The backtracking mechanism steps back a specific number of tokens to regenerate them with steering applied. The intervention strength is adaptively set based on the degree of deviation detected by the classifier.

### 5. What benchmarks does it evaluate on?

The paper evaluates on **7 benchmarks total**:
- **TruthfulQA** (the primary evaluation dataset)
- **Six multiple-choice datasets**: COPA, StoryCloze, NLI (SNLI/Bowman et al.), MMLU, SST2, and Winogrande

### 6. Is it actually accepted at NeurIPS 2025?

**Yes.** The paper was accepted as a poster at NeurIPS 2025 in San Diego. It has:
- A NeurIPS virtual poster page at `neurips.cc/virtual/2025/poster/116311`
- An OpenReview page at `openreview.net/forum?id=l75RyRcevf`

This is confirmed -- it is a legitimate NeurIPS 2025 poster paper.

---

Sources:
- [arXiv paper page](https://arxiv.org/abs/2508.17621)
- [arXiv HTML version](https://arxiv.org/html/2508.17621)
- [OpenReview page](https://openreview.net/forum?id=l75RyRcevf)
- [NeurIPS 2025 Poster](https://neurips.cc/virtual/2025/loc/san-diego/poster/116311)

agentId: a15bddadf98884943 (use SendMessage with to: 'a15bddadf98884943' to continue this agent)
&lt;usage>total_tokens: 18083
tool_uses: 11
duration_ms: 68507&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "02c5a297-9acc-47d4-badc-dac0ffdc3770",
  "isSidechain": false,
  "promptId": "fa61ad10-397c-4783-9490-82353cc0b8e8",
  "type": "user",
  "uuid": "8854c9a7-6124-40cf-8e7c-26e58b5e44a9",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Use WebSearch to find and verify the paper \"Steering When Necessary: Flexible Steering Large Language Models with Backtracking\" which is claimed to be at NeurIPS 2025 (arxiv 2508.17621). I need to know:\n1. Does it exist? (Note: arXiv 2508 means August 2025 submission)\n2. Does it use activation-space probing to decide WHEN to apply steering?\n3. Does it include a backtracking mechanism?\n4. What is its actual intervention granularity (token-level, sentence-level, or something else)?\n5. What benchmarks does it evaluate on?\n6. Is it actually accepted at NeurIPS 2025?\n\nSearch for \"Steering When Necessary Flexible Steering Backtracking\" and \"arxiv 2508.17621\" and \"FASB activation steering selective\". Also search for \"flexible activation steering backtracking NeurIPS 2025\".",
    "agentId": "a15bddadf98884943",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Based on my comprehensive search, here are the findings for each of your questions:\n\n---\n\n## Results for \"Steering When Necessary: Flexible Steering Large Language Models with Backtracking\" (arXiv 2508.17621)\n\n### 1. Does it exist?\n\n**Yes.** The paper exists at arXiv 2508.17621, submitted August 25, 2025, with a revised version on October 1, 2025. The authors are Zifeng Cheng, Jinwei Gan, Zhiwei Jiang, Cong Wang, Yafeng Yin, Xiang Luo, Yuchen Fu, and Qing Gu. Since arXiv 2508 corresponds to August 2025 submissions, the timeline is consistent.\n\n### 2. Does it use activation-space probing to decide WHEN to apply steering?\n\n**Yes.** FASB uses a probe-based classifier trained on internal activation states (specifically attention heads) to dynamically determine whether intervention is necessary at any given point in generation. The classifier tracks the internal states of the LLM during generation, considering both the question and the generated content so far, to assess whether the model is deviating from desired behavior. This is explicitly called the \"Probe method\" in the paper.\n\n### 3. Does it include a backtracking mechanism?\n\n**Yes.** The paper explicitly proposes a backtracking mechanism. The key insight is that intervening *after* detecting a deviation is often too late. So when deviation is detected, the mechanism \"steps back a few tokens\" and then performs activation steering to regenerate those tokens, steering generation toward the desired direction.\n\n### 4. What is its actual intervention granularity?\n\n**Token-level.** The intervention operates at the token level. The classifier monitors internal states during token-by-token generation and determines both *whether* to intervene and the *strength* of intervention. The backtracking mechanism steps back a specific number of tokens to regenerate them with steering applied. The intervention strength is adaptively set based on the degree of deviation detected by the classifier.\n\n### 5. What benchmarks does it evaluate on?\n\nThe paper evaluates on **7 benchmarks total**:\n- **TruthfulQA** (the primary evaluation dataset)\n- **Six multiple-choice datasets**: COPA, StoryCloze, NLI (SNLI/Bowman et al.), MMLU, SST2, and Winogrande\n\n### 6. Is it actually accepted at NeurIPS 2025?\n\n**Yes.** The paper was accepted as a poster at NeurIPS 2025 in San Diego. It has:\n- A NeurIPS virtual poster page at `neurips.cc/virtual/2025/poster/116311`\n- An OpenReview page at `openreview.net/forum?id=l75RyRcevf`\n\nThis is confirmed -- it is a legitimate NeurIPS 2025 poster paper.\n\n---\n\nSources:\n- [arXiv paper page](https://arxiv.org/abs/2508.17621)\n- [arXiv HTML version](https://arxiv.org/html/2508.17621)\n- [OpenReview page](https://openreview.net/forum?id=l75RyRcevf)\n- [NeurIPS 2025 Poster](https://neurips.cc/virtual/2025/loc/san-diego/poster/116311)"
      }
    ],
    "totalDurationMs": 68507,
    "totalTokens": 18083,
    "totalToolUseCount": 11,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1170,
      "cache_read_input_tokens": 16109,
      "output_tokens": 803,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1170
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 803,
          "cache_read_input_tokens": 16109,
          "cache_creation_input_tokens": 1170,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1170,
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
      "otherToolCount": 11
    }
  },
  "sourceToolAssistantUUID": "02c5a297-9acc-47d4-badc-dac0ffdc3770",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73813be2-f916-4121-a2d7-450b728cd138",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-16T08:50:18.691Z_

<details><summary>↩ Tool result · `toolu_01H9CWFwhGp22VDEKvYrKQwb`</summary>

```text
Here is my comprehensive report on recent competing papers (March-May 2026) on activation steering for hallucination reduction that could compete with a "geometry-triggered sentence-level steering" approach:

---

## Highly Relevant Concurrent Competitors (Feb-May 2026)

### 1. Steering Vector Fields (SVF) -- arXiv 2602.01654 (Feb 2026)
- **Mechanism**: Learns a differentiable concept scoring function whose local gradient defines the steering direction at each context. Unlike static steering vectors, SVF refreshes steering directions from evolving hidden states throughout decoding.
- **Why it competes**: This is context-aware, geometry-sensitive steering that adapts per-token -- directly overlapping with "geometry-triggered" approaches. Evaluates on hallucination control and outperforms BiPO and other baselines on long-form generation.
- [Paper](https://arxiv.org/abs/2602.01654)

### 2. Spherical Steering -- arXiv 2602.08169 (Feb 2026, ICML 2026)
- **Mechanism**: Rotates activations along a geodesic toward a target direction (preserving norm/magnitude), rather than adding steering vectors. Training-free.
- **Why it competes**: Explicitly "geometry-aware" -- uses hypersphere geometry to avoid representation collapse. +10% on TruthfulQA over addition-based baselines. The "geometry-aware" framing directly overlaps with your paper's positioning.
- [Paper](https://arxiv.org/abs/2602.08169) | [Code](https://github.com/chili-lab/Spherical-Steering)

### 3. Curveball Steering -- arXiv 2603.09313 (March 2026)
- **Mechanism**: Nonlinear steering via polynomial kernel PCA that respects learned activation geometry. Demonstrates that LLM activation spaces have substantial concept-dependent geometric distortions, making linear interventions suboptimal.
- **Why it competes**: Another "geometry-aware" steering method that addresses the same core insight -- that activation space geometry matters for effective steering. Outperforms linear PCA-based steering in distorted regimes.
- [Paper](https://arxiv.org/abs/2603.09313)

### 4. HELIX / Tethered Reasoning -- arXiv 2602.17691 (Feb 2026)
- **Mechanism**: Computes a Unified Truth Score (UTS) combining token-level semantic entropy with **Mahalanobis distance** from a pre-computed truthfulness manifold. When UTS indicates trajectory divergence, graduated steering vectors redirect activations. Only affects 0.2-2.5% of tokens.
- **Why it competes**: Uses Mahalanobis distance as a geometric trigger for selective steering -- very close to "geometry-triggered" steering. Focused on quantized LLMs but the mechanism generalizes. GSM8K: 88.84% at T=3.0.
- [Paper](https://arxiv.org/abs/2602.17691)

### 5. PCNet / Hallucination as an Anomaly -- arXiv 2605.05953 (May 7, 2026)
- **Mechanism**: Probabilistic Circuit (PCNet) trained as a tractable density estimator over the LLM residual stream. Detects hallucinations as geometric anomalies via exact NLL computation (no sampling). Gates PC-LDCD (latent density contrastive decoding) only when latent geometry deviates from factual regions.
- **Why it competes**: Geometric anomaly detection triggering selective intervention at decoding time. AUROC up to 99% for hallucination detection. Very recent (May 2026) and directly models the "factual manifold" concept.
- Authors: Erik Nielsen, Elia Cunegatti, Marcus Vukojevic, Giovanni Iacca (University of Trento)
- [Paper](https://arxiv.org/abs/2605.05953)

### 6. Where Does Reasoning Break? -- arXiv 2605.13772 (May 13, 2026)
- **Mechanism**: Frames hallucination as excursions in transport cost away from a stable manifold of coherent hidden-state transitions. Uses step-level geometric transition features (7 features) to detect the first error in multi-step reasoning.
- **Why it competes**: Step-level (granular) hallucination detection via hidden-state geometry. Directly relevant to "sentence-level" detection. Uses contrastive PCA lens and BiLSTM student. Outperforms entropy/probing/attention baselines on ProcessBench, PRM800K, HaluEval, TruthfulQA.
- [Paper](https://arxiv.org/abs/2605.13772)

### 7. MESA (Mitigating Entangled Steering) -- arXiv 2604.07914 (April 2026)
- **Mechanism**: Plug-and-play framework that performs controlled and selective latent intervention. Addresses "entangled steering signals" where suppressing hallucinations disrupts generation behavior. Targets hallucination-relevant responses while preserving token distribution.
- **Why it competes**: Selective steering (only intervening when needed) while preserving generation quality -- similar to sentence-level selective intervention.
- [Paper](https://arxiv.org/abs/2604.07914)

### 8. SENTINEL (Sentence-Level Early Intervention) -- arXiv 2507.12455 (July 2025, published ICCV 2025)
- **Mechanism**: Identifies that hallucinations predominantly emerge at early stages of generation and propagate. Uses sentence-level preference learning with bootstrapped in-domain preference pairs.
- **Why it competes**: Explicitly "sentence-level" intervention for hallucination. Though older (2025) and preference-learning-based rather than activation-steering, the sentence-level framing is identical. Published at ICCV 2025 -- you should cite this.
- [Paper](https://arxiv.org/abs/2507.12455)

---

## Moderately Relevant Papers

### 9. Dynamic Multimodal Activation Steering (DMAS) -- arXiv 2602.21704 (Feb 2026)
- Context-aware dynamic selection of steering vectors based on semantic similarity + attention head targeting. Training-free. Focused on Vision-Language Models. 20.2% reduction in sentence-level hallucination (CHAIRS).
- [Paper](https://arxiv.org/abs/2602.21704)

### 10. REVIS -- arXiv 2602.11824 (Feb 2026)
- Sparse latent steering using orthogonal projection to extract pure visual vectors + calibration-based layer selection + inference-time dynamic risk-aware steering. 19% hallucination reduction. Vision-Language focused.
- [Paper](https://arxiv.org/abs/2602.11824)

### 11. Steer Like the LLM (PSR) -- arXiv 2605.03907 (May 5, 2026)
- Shows that effective steering should apply token-specific coefficients (strong on some tokens, weak on others), mimicking how prompts actually work. Introduces Prompt Steering Replacement models.
- [Paper](https://arxiv.org/abs/2605.03907)

### 12. Prompt-Activation Duality -- arXiv 2605.10664 (May 2026)
- Attention-level interventions for activation steering.
- [Paper](https://arxiv.org/html/2605.10664)

---

## Verification of Specific Papers

**PCNet (arXiv 2605.05953)**: CONFIRMED. "Hallucination as an Anomaly: Dynamic Intervention via Probabilistic Circuits" by Nielsen, Cunegatti, Vukojevic, Iacca (U. Trento). May 7, 2026. Uses PCNet as density estimator on residual stream, gates PC-LDCD intervention when NLL indicates anomaly.

**HELIX (arXiv 2602.17691)**: CONFIRMED. "Tethered Reasoning: Decoupling Entropy from Hallucination in Quantized LLMs via Manifold Steering" by Craig Atkinson. Feb 2026. Uses Mahalanobis distance from truthfulness manifold + semantic entropy to compute UTS, triggers graduated steering vectors. Note: The paper name is "Tethered Reasoning" and the framework is called "HELIX" -- not "HELIX tethered reasoning" as a single unit.

---

## Key Threat Assessment for "Geometry-Triggered Sentence-Level Steering"

**Highest overlap papers** (most likely to be flagged by reviewers as concurrent work):
1. **Steering Vector Fields** (2602.01654) -- context-aware geometry-driven steering
2. **Spherical Steering** (2602.08169) -- geometry-aware steering (ICML 2026 accepted)
3. **HELIX** (2602.17691) -- Mahalanobis-triggered selective steering
4. **PCNet** (2605.05953) -- geometric anomaly-triggered selective intervention
5. **Step-Level Transport Geometry** (2605.13772) -- step-level geometric hallucination detection

The combination of "geometric trigger + sentence-level granularity + text LLM hallucination" appears to be a gap -- most geometric approaches operate token-level or step-level, and most sentence-level approaches (SENTINEL) use preference learning rather than activation geometry. However, PCNet and the Transport Geometry paper are very close in spirit and extremely recent (May 2026).

Sources:
- [Steering Vector Fields](https://arxiv.org/abs/2602.01654)
- [Spherical Steering](https://arxiv.org/abs/2602.08169)
- [Curveball Steering](https://arxiv.org/abs/2603.09313)
- [HELIX / Tethered Reasoning](https://arxiv.org/abs/2602.17691)
- [PCNet / Hallucination as an Anomaly](https://arxiv.org/abs/2605.05953)
- [Step-Level Hallucination via Transport Geometry](https://arxiv.org/abs/2605.13772)
- [MESA](https://arxiv.org/abs/2604.07914)
- [SENTINEL](https://arxiv.org/abs/2507.12455)
- [DMAS](https://arxiv.org/abs/2602.21704)
- [REVIS](https://arxiv.org/abs/2602.11824)
- [Steer Like the LLM](https://arxiv.org/abs/2605.03907)
- [Prompt-Activation Duality](https://arxiv.org/html/2605.10664)

agentId: a1993c84ad2495b66 (use SendMessage with to: 'a1993c84ad2495b66' to continue this agent)
&lt;usage>total_tokens: 29340
tool_uses: 18
duration_ms: 126862&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5dc037e5-b2e3-4a18-9d3d-323b68a358f5",
  "isSidechain": false,
  "promptId": "fa61ad10-397c-4783-9490-82353cc0b8e8",
  "type": "user",
  "uuid": "ac1ae4b6-f2a1-4418-8095-ca6240eab769",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Use WebSearch to find the MOST RECENT papers (March-May 2026) on activation steering for hallucination reduction that might compete with a \"geometry-triggered sentence-level steering\" approach. I need to check if there are concurrent submissions the generator may have missed.\n\nSearch for:\n1. \"activation steering hallucination 2026\" site:arxiv.org\n2. \"geometry-aware steering hallucination\" 2026\n3. \"selective steering hallucination detection\" 2026\n4. \"claim-level hallucination intervention decoding\" 2026\n5. \"Mahalanobis distance hallucination steering\" 2026\n6. \"sentence boundary steering LLM\" 2026\n\nAlso search for:\n7. \"PCNet hallucination probabilistic circuits\" to verify this paper (arxiv 2605.05953)\n8. \"HELIX tethered reasoning Mahalanobis\" OR \"arxiv 2602.17691\" to verify this paper's actual mechanism",
    "agentId": "a1993c84ad2495b66",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here is my comprehensive report on recent competing papers (March-May 2026) on activation steering for hallucination reduction that could compete with a \"geometry-triggered sentence-level steering\" approach:\n\n---\n\n## Highly Relevant Concurrent Competitors (Feb-May 2026)\n\n### 1. Steering Vector Fields (SVF) -- arXiv 2602.01654 (Feb 2026)\n- **Mechanism**: Learns a differentiable concept scoring function whose local gradient defines the steering direction at each context. Unlike static steering vectors, SVF refreshes steering directions from evolving hidden states throughout decoding.\n- **Why it competes**: This is context-aware, geometry-sensitive steering that adapts per-token -- directly overlapping with \"geometry-triggered\" approaches. Evaluates on hallucination control and outperforms BiPO and other baselines on long-form generation.\n- [Paper](https://arxiv.org/abs/2602.01654)\n\n### 2. Spherical Steering -- arXiv 2602.08169 (Feb 2026, ICML 2026)\n- **Mechanism**: Rotates activations along a geodesic toward a target direction (preserving norm/magnitude), rather than adding steering vectors. Training-free.\n- **Why it competes**: Explicitly \"geometry-aware\" -- uses hypersphere geometry to avoid representation collapse. +10% on TruthfulQA over addition-based baselines. The \"geometry-aware\" framing directly overlaps with your paper's positioning.\n- [Paper](https://arxiv.org/abs/2602.08169) | [Code](https://github.com/chili-lab/Spherical-Steering)\n\n### 3. Curveball Steering -- arXiv 2603.09313 (March 2026)\n- **Mechanism**: Nonlinear steering via polynomial kernel PCA that respects learned activation geometry. Demonstrates that LLM activation spaces have substantial concept-dependent geometric distortions, making linear interventions suboptimal.\n- **Why it competes**: Another \"geometry-aware\" steering method that addresses the same core insight -- that activation space geometry matters for effective steering. Outperforms linear PCA-based steering in distorted regimes.\n- [Paper](https://arxiv.org/abs/2603.09313)\n\n### 4. HELIX / Tethered Reasoning -- arXiv 2602.17691 (Feb 2026)\n- **Mechanism**: Computes a Unified Truth Score (UTS) combining token-level semantic entropy with **Mahalanobis distance** from a pre-computed truthfulness manifold. When UTS indicates trajectory divergence, graduated steering vectors redirect activations. Only affects 0.2-2.5% of tokens.\n- **Why it competes**: Uses Mahalanobis distance as a geometric trigger for selective steering -- very close to \"geometry-triggered\" steering. Focused on quantized LLMs but the mechanism generalizes. GSM8K: 88.84% at T=3.0.\n- [Paper](https://arxiv.org/abs/2602.17691)\n\n### 5. PCNet / Hallucination as an Anomaly -- arXiv 2605.05953 (May 7, 2026)\n- **Mechanism**: Probabilistic Circuit (PCNet) trained as a tractable density estimator over the LLM residual stream. Detects hallucinations as geometric anomalies via exact NLL computation (no sampling). Gates PC-LDCD (latent density contrastive decoding) only when latent geometry deviates from factual regions.\n- **Why it competes**: Geometric anomaly detection triggering selective intervention at decoding time. AUROC up to 99% for hallucination detection. Very recent (May 2026) and directly models the \"factual manifold\" concept.\n- Authors: Erik Nielsen, Elia Cunegatti, Marcus Vukojevic, Giovanni Iacca (University of Trento)\n- [Paper](https://arxiv.org/abs/2605.05953)\n\n### 6. Where Does Reasoning Break? -- arXiv 2605.13772 (May 13, 2026)\n- **Mechanism**: Frames hallucination as excursions in transport cost away from a stable manifold of coherent hidden-state transitions. Uses step-level geometric transition features (7 features) to detect the first error in multi-step reasoning.\n- **Why it competes**: Step-level (granular) hallucination detection via hidden-state geometry. Directly relevant to \"sentence-level\" detection. Uses contrastive PCA lens and BiLSTM student. Outperforms entropy/probing/attention baselines on ProcessBench, PRM800K, HaluEval, TruthfulQA.\n- [Paper](https://arxiv.org/abs/2605.13772)\n\n### 7. MESA (Mitigating Entangled Steering) -- arXiv 2604.07914 (April 2026)\n- **Mechanism**: Plug-and-play framework that performs controlled and selective latent intervention. Addresses \"entangled steering signals\" where suppressing hallucinations disrupts generation behavior. Targets hallucination-relevant responses while preserving token distribution.\n- **Why it competes**: Selective steering (only intervening when needed) while preserving generation quality -- similar to sentence-level selective intervention.\n- [Paper](https://arxiv.org/abs/2604.07914)\n\n### 8. SENTINEL (Sentence-Level Early Intervention) -- arXiv 2507.12455 (July 2025, published ICCV 2025)\n- **Mechanism**: Identifies that hallucinations predominantly emerge at early stages of generation and propagate. Uses sentence-level preference learning with bootstrapped in-domain preference pairs.\n- **Why it competes**: Explicitly \"sentence-level\" intervention for hallucination. Though older (2025) and preference-learning-based rather than activation-steering, the sentence-level framing is identical. Published at ICCV 2025 -- you should cite this.\n- [Paper](https://arxiv.org/abs/2507.12455)\n\n---\n\n## Moderately Relevant Papers\n\n### 9. Dynamic Multimodal Activation Steering (DMAS) -- arXiv 2602.21704 (Feb 2026)\n- Context-aware dynamic selection of steering vectors based on semantic similarity + attention head targeting. Training-free. Focused on Vision-Language Models. 20.2% reduction in sentence-level hallucination (CHAIRS).\n- [Paper](https://arxiv.org/abs/2602.21704)\n\n### 10. REVIS -- arXiv 2602.11824 (Feb 2026)\n- Sparse latent steering using orthogonal projection to extract pure visual vectors + calibration-based layer selection + inference-time dynamic risk-aware steering. 19% hallucination reduction. Vision-Language focused.\n- [Paper](https://arxiv.org/abs/2602.11824)\n\n### 11. Steer Like the LLM (PSR) -- arXiv 2605.03907 (May 5, 2026)\n- Shows that effective steering should apply token-specific coefficients (strong on some tokens, weak on others), mimicking how prompts actually work. Introduces Prompt Steering Replacement models.\n- [Paper](https://arxiv.org/abs/2605.03907)\n\n### 12. Prompt-Activation Duality -- arXiv 2605.10664 (May 2026)\n- Attention-level interventions for activation steering.\n- [Paper](https://arxiv.org/html/2605.10664)\n\n---\n\n## Verification of Specific Papers\n\n**PCNet (arXiv 2605.05953)**: CONFIRMED. \"Hallucination as an Anomaly: Dynamic Intervention via Probabilistic Circuits\" by Nielsen, Cunegatti, Vukojevic, Iacca (U. Trento). May 7, 2026. Uses PCNet as density estimator on residual stream, gates PC-LDCD intervention when NLL indicates anomaly.\n\n**HELIX (arXiv 2602.17691)**: CONFIRMED. \"Tethered Reasoning: Decoupling Entropy from Hallucination in Quantized LLMs via Manifold Steering\" by Craig Atkinson. Feb 2026. Uses Mahalanobis distance from truthfulness manifold + semantic entropy to compute UTS, triggers graduated steering vectors. Note: The paper name is \"Tethered Reasoning\" and the framework is called \"HELIX\" -- not \"HELIX tethered reasoning\" as a single unit.\n\n---\n\n## Key Threat Assessment for \"Geometry-Triggered Sentence-Level Steering\"\n\n**Highest overlap papers** (most likely to be flagged by reviewers as concurrent work):\n1. **Steering Vector Fields** (2602.01654) -- context-aware geometry-driven steering\n2. **Spherical Steering** (2602.08169) -- geometry-aware steering (ICML 2026 accepted)\n3. **HELIX** (2602.17691) -- Mahalanobis-triggered selective steering\n4. **PCNet** (2605.05953) -- geometric anomaly-triggered selective intervention\n5. **Step-Level Transport Geometry** (2605.13772) -- step-level geometric hallucination detection\n\nThe combination of \"geometric trigger + sentence-level granularity + text LLM hallucination\" appears to be a gap -- most geometric approaches operate token-level or step-level, and most sentence-level approaches (SENTINEL) use preference learning rather than activation geometry. However, PCNet and the Transport Geometry paper are very close in spirit and extremely recent (May 2026).\n\nSources:\n- [Steering Vector Fields](https://arxiv.org/abs/2602.01654)\n- [Spherical Steering](https://arxiv.org/abs/2602.08169)\n- [Curveball Steering](https://arxiv.org/abs/2603.09313)\n- [HELIX / Tethered Reasoning](https://arxiv.org/abs/2602.17691)\n- [PCNet / Hallucination as an Anomaly](https://arxiv.org/abs/2605.05953)\n- [Step-Level Hallucination via Transport Geometry](https://arxiv.org/abs/2605.13772)\n- [MESA](https://arxiv.org/abs/2604.07914)\n- [SENTINEL](https://arxiv.org/abs/2507.12455)\n- [DMAS](https://arxiv.org/abs/2602.21704)\n- [REVIS](https://arxiv.org/abs/2602.11824)\n- [Steer Like the LLM](https://arxiv.org/abs/2605.03907)\n- [Prompt-Activation Duality](https://arxiv.org/html/2605.10664)"
      }
    ],
    "totalDurationMs": 126862,
    "totalTokens": 29340,
    "totalToolUseCount": 18,
    "usage": {
      "input_tokens": 837,
      "cache_creation_input_tokens": 1008,
      "cache_read_input_tokens": 24873,
      "output_tokens": 2622,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1008
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 837,
          "output_tokens": 2622,
          "cache_read_input_tokens": 24873,
          "cache_creation_input_tokens": 1008,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1008,
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
      "otherToolCount": 18
    }
  },
  "sourceToolAssistantUUID": "5dc037e5-b2e3-4a18-9d3d-323b68a358f5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73813be2-f916-4121-a2d7-450b728cd138",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 29 · 2026-05-16T08:50:25.989Z_

Now I have critical findings. Let me verify a few more things — particularly FASB (the most direct threat as a selective steering method at NeurIPS 2025) and search for any papers that directly undermine the timing hypothesis.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ac1ae4b6-f2a1-4418-8095-ca6240eab769",
  "isSidechain": false,
  "requestId": "req_011Cb5xhGPV1urGsSZ2Bj6X9",
  "type": "assistant",
  "uuid": "ffbed317-4c03-43dc-b249-b082ffb648f8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73813be2-f916-4121-a2d7-450b728cd138",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018MVUqF9yVeX7gzmF8uQr3B",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8954,
      "cache_read_input_tokens": 35387,
      "output_tokens": 880,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8954,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 880,
          "cache_read_input_tokens": 35387,
          "cache_creation_input_tokens": 8954,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8954
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

_source line 30 · 2026-05-16T08:50:29.163Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01XjwSsCC9hrNbkRTWtG19Yg`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Verify Steering Vector Fields paper",
  "prompt": "Use WebSearch to find and verify \"Steering Vector Fields\" (arXiv 2602.01654, Feb 2026). I need:\n1. Does it exist?\n2. What is its core mechanism — does it learn per-context steering directions from a differentiable scoring function?\n3. Does it operate per-token during decoding?\n4. Does it evaluate on TruthfulQA or hallucination benchmarks?\n5. Does it use geometric features of the activation space?\n\nSearch for \"Steering Vector Fields\" arxiv 2602.01654 and \"differentiable concept scoring steering direction\". Also try \"SVF steering vector fields language model 2026\"."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ffbed317-4c03-43dc-b249-b082ffb648f8",
  "isSidechain": false,
  "requestId": "req_011Cb5xhGPV1urGsSZ2Bj6X9",
  "type": "assistant",
  "uuid": "9447036b-d255-4dbc-bf43-84455998f2a1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73813be2-f916-4121-a2d7-450b728cd138",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018MVUqF9yVeX7gzmF8uQr3B",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8954,
      "cache_read_input_tokens": 35387,
      "output_tokens": 880,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8954,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 880,
          "cache_read_input_tokens": 35387,
          "cache_creation_input_tokens": 8954,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8954
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

_source line 31 · 2026-05-16T08:50:33.685Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01Vnycb98B3ShA9SDaBf3C9T`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Check FASB mechanism vs GTS",
  "prompt": "Use WebSearch and WebFetch to get more details about FASB \"Steering When Necessary: Flexible Steering Large Language Models with Backtracking\" (arXiv 2508.17621, NeurIPS 2025). I specifically need to understand:\n\n1. How does FASB decide WHEN to steer? What is the probe architecture?\n2. Does it use geometric features (distances, margins) or a trained binary classifier?\n3. At what granularity does it make the steer/no-steer decision? (Every token? Every few tokens? Sentence level?)\n4. What TruthfulQA results does it achieve?\n5. Does it compare to any geometry-based detection methods?\n\nTry fetching the arxiv abstract page: https://arxiv.org/abs/2508.17621\nAlso search for \"FASB steering when necessary TruthfulQA results\" and \"flexible activation steering probe backtracking\"."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9447036b-d255-4dbc-bf43-84455998f2a1",
  "isSidechain": false,
  "requestId": "req_011Cb5xhGPV1urGsSZ2Bj6X9",
  "type": "assistant",
  "uuid": "7e593084-7dd8-489d-b0eb-c8b206b74408",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73813be2-f916-4121-a2d7-450b728cd138",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018MVUqF9yVeX7gzmF8uQr3B",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8954,
      "cache_read_input_tokens": 35387,
      "output_tokens": 880,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8954,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 880,
          "cache_read_input_tokens": 35387,
          "cache_creation_input_tokens": 8954,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8954
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

_source line 32 · 2026-05-16T08:50:38.959Z_

<details open><summary>🔧 Tool call — Agent · `toolu_0126cABYA2U27ArnB8ywzZRH`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Search for timing hypothesis evidence",
  "prompt": "Use WebSearch to find any evidence FOR or AGAINST the hypothesis that \"hidden state geometry at sentence boundaries is predictive of factuality in the next sentence.\" This is a critical assumption of the paper I'm reviewing.\n\nSearch for:\n1. \"sentence boundary\" \"hidden state\" prediction hallucination OR factuality\n2. \"sentence planning\" transformer hidden states generation\n3. \"hallucination early detection\" \"before generation\" OR \"predictive\"\n4. \"Hallucination as Trajectory Commitment\" arxiv 2604.15400 — this paper claims \"early commitment\" in hallucination. Does it support detecting hallucination at sentence boundaries?\n5. \"hidden state\" predictive \"next sentence\" factuality OR accuracy OR hallucination\n\nAlso search for evidence AGAINST this hypothesis:\n6. \"hallucination unpredictable\" OR \"hallucination cannot be detected in advance\"\n7. \"activation steering timing\" when to intervene"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7e593084-7dd8-489d-b0eb-c8b206b74408",
  "isSidechain": false,
  "requestId": "req_011Cb5xhGPV1urGsSZ2Bj6X9",
  "type": "assistant",
  "uuid": "d237932e-8cc2-4dde-a2b6-1695cc790e36",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73813be2-f916-4121-a2d7-450b728cd138",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018MVUqF9yVeX7gzmF8uQr3B",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8954,
      "cache_read_input_tokens": 35387,
      "output_tokens": 880,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8954,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 880,
          "cache_read_input_tokens": 35387,
          "cache_creation_input_tokens": 8954,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8954
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

_source line 33_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-16 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "d237932e-8cc2-4dde-a2b6-1695cc790e36",
  "sessionId": "73813be2-f916-4121-a2d7-450b728cd138"
}
```

---

### Runtime record

_source line 34_

```json
{
  "type": "ai-title",
  "aiTitle": "Geometry-triggered sentence-level hallucination steering",
  "sessionId": "73813be2-f916-4121-a2d7-450b728cd138"
}
```

---

### Tool result

_source line 35 · 2026-05-16T08:51:30.901Z_

<details><summary>↩ Tool result · `toolu_01XjwSsCC9hrNbkRTWtG19Yg`</summary>

```text
I now have comprehensive information to answer all five of your questions. Here is my analysis:

---

## Verification of "Steering Vector Fields" (arXiv:2602.01654)

### 1. Does it exist?

**Yes.** The paper is confirmed to exist at [arXiv:2602.01654](https://arxiv.org/abs/2602.01654), titled "Steering Vector Fields for Context-Aware Inference-Time Control in Large Language Models." It was submitted on February 2, 2026, by Jiaqian Li and co-authors.

---

### 2. Core mechanism -- does it learn per-context steering directions from a differentiable scoring function?

**Yes, confirmed.** SVF learns a **differentiable concept scoring function** whose **local gradient** defines the steering direction at each point in activation space. This makes the intervention explicitly context-dependent -- the steering direction is a function of the current hidden state, rather than a single static vector applied uniformly. The concept boundary is modeled by a nonlinear MLP, and the local normal to that boundary determines the steering direction at any given activation.

---

### 3. Does it operate per-token during decoding?

**Not strictly per-token, but per-K-steps.** During long-form generation, SVF **refreshes the representation-conditioned steering direction every K steps**, allowing interventions to remain aligned with the evolving trajectory of the generation. So it is not a one-shot static intervention, but it also does not necessarily recompute at every single token -- it recomputes periodically. In any case, the steering direction is inherently token-position-aware because it depends on the current activation at that position.

---

### 4. Does it evaluate on TruthfulQA or hallucination benchmarks?

**Yes, both.** The paper evaluates on:
- **TruthfulQA** (Lin et al., 2022): 817 questions across 38 categories, each paired with correct and incorrect answers, used to evaluate truthfulness steering.
- **A hallucination dataset**: containing 1,000 examples with two types of hallucination (unprompted hallucination and context-triggered hallucination), each with a prompt and two candidate continuations (hallucinated vs. correct).

---

### 5. Does it use geometric features of the activation space?

**Yes, centrally.** The entire framework is described as a "geometric paradigm." Key geometric elements include:
- A learned **concept boundary** (nonlinear surface in activation space) whose **local normal direction** serves as the steering vector at any point.
- A **shared projection matrix** and **layer-conditioned calibration** that place multi-layer activations into a shared, aligned concept space.
- The method is explicitly motivated by the observation that the concept-improving direction varies geometrically across the activation manifold, and a static (flat) vector is an inadequate approximation of this curved structure.

Ablation studies confirm the criticality of the MLP's nonlinearity for capturing complex concept geometries in activation space.

---

Sources:
- [Steering Vector Fields for Context-Aware Inference-Time Control in Large Language Models (arXiv abstract)](https://arxiv.org/abs/2602.01654)
- [Steering Vector Fields (HTML version)](https://arxiv.org/html/2602.01654)
- [Literature Review on themoonlight.io](https://www.themoonlight.io/en/review/steering-vector-fields-for-context-aware-inference-time-control-in-large-language-models)
- [Activation Steering in 2026: A Practitioner's Field Guide](https://subhadipmitra.com/blog/2026/activation-steering-field-guide/)

agentId: a56c77bfdcc52d6e6 (use SendMessage with to: 'a56c77bfdcc52d6e6' to continue this agent)
&lt;usage>total_tokens: 17803
tool_uses: 8
duration_ms: 61734&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9447036b-d255-4dbc-bf43-84455998f2a1",
  "isSidechain": false,
  "promptId": "fa61ad10-397c-4783-9490-82353cc0b8e8",
  "type": "user",
  "uuid": "06e8a8d0-cc2b-42e3-8643-6e6e42faee7d",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Use WebSearch to find and verify \"Steering Vector Fields\" (arXiv 2602.01654, Feb 2026). I need:\n1. Does it exist?\n2. What is its core mechanism — does it learn per-context steering directions from a differentiable scoring function?\n3. Does it operate per-token during decoding?\n4. Does it evaluate on TruthfulQA or hallucination benchmarks?\n5. Does it use geometric features of the activation space?\n\nSearch for \"Steering Vector Fields\" arxiv 2602.01654 and \"differentiable concept scoring steering direction\". Also try \"SVF steering vector fields language model 2026\".",
    "agentId": "a56c77bfdcc52d6e6",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "I now have comprehensive information to answer all five of your questions. Here is my analysis:\n\n---\n\n## Verification of \"Steering Vector Fields\" (arXiv:2602.01654)\n\n### 1. Does it exist?\n\n**Yes.** The paper is confirmed to exist at [arXiv:2602.01654](https://arxiv.org/abs/2602.01654), titled \"Steering Vector Fields for Context-Aware Inference-Time Control in Large Language Models.\" It was submitted on February 2, 2026, by Jiaqian Li and co-authors.\n\n---\n\n### 2. Core mechanism -- does it learn per-context steering directions from a differentiable scoring function?\n\n**Yes, confirmed.** SVF learns a **differentiable concept scoring function** whose **local gradient** defines the steering direction at each point in activation space. This makes the intervention explicitly context-dependent -- the steering direction is a function of the current hidden state, rather than a single static vector applied uniformly. The concept boundary is modeled by a nonlinear MLP, and the local normal to that boundary determines the steering direction at any given activation.\n\n---\n\n### 3. Does it operate per-token during decoding?\n\n**Not strictly per-token, but per-K-steps.** During long-form generation, SVF **refreshes the representation-conditioned steering direction every K steps**, allowing interventions to remain aligned with the evolving trajectory of the generation. So it is not a one-shot static intervention, but it also does not necessarily recompute at every single token -- it recomputes periodically. In any case, the steering direction is inherently token-position-aware because it depends on the current activation at that position.\n\n---\n\n### 4. Does it evaluate on TruthfulQA or hallucination benchmarks?\n\n**Yes, both.** The paper evaluates on:\n- **TruthfulQA** (Lin et al., 2022): 817 questions across 38 categories, each paired with correct and incorrect answers, used to evaluate truthfulness steering.\n- **A hallucination dataset**: containing 1,000 examples with two types of hallucination (unprompted hallucination and context-triggered hallucination), each with a prompt and two candidate continuations (hallucinated vs. correct).\n\n---\n\n### 5. Does it use geometric features of the activation space?\n\n**Yes, centrally.** The entire framework is described as a \"geometric paradigm.\" Key geometric elements include:\n- A learned **concept boundary** (nonlinear surface in activation space) whose **local normal direction** serves as the steering vector at any point.\n- A **shared projection matrix** and **layer-conditioned calibration** that place multi-layer activations into a shared, aligned concept space.\n- The method is explicitly motivated by the observation that the concept-improving direction varies geometrically across the activation manifold, and a static (flat) vector is an inadequate approximation of this curved structure.\n\nAblation studies confirm the criticality of the MLP's nonlinearity for capturing complex concept geometries in activation space.\n\n---\n\nSources:\n- [Steering Vector Fields for Context-Aware Inference-Time Control in Large Language Models (arXiv abstract)](https://arxiv.org/abs/2602.01654)\n- [Steering Vector Fields (HTML version)](https://arxiv.org/html/2602.01654)\n- [Literature Review on themoonlight.io](https://www.themoonlight.io/en/review/steering-vector-fields-for-context-aware-inference-time-control-in-large-language-models)\n- [Activation Steering in 2026: A Practitioner's Field Guide](https://subhadipmitra.com/blog/2026/activation-steering-field-guide/)"
      }
    ],
    "totalDurationMs": 61734,
    "totalTokens": 17803,
    "totalToolUseCount": 8,
    "usage": {
      "input_tokens": 1025,
      "cache_creation_input_tokens": 1918,
      "cache_read_input_tokens": 13993,
      "output_tokens": 867,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1918
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1025,
          "output_tokens": 867,
          "cache_read_input_tokens": 13993,
          "cache_creation_input_tokens": 1918,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1918,
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
      "otherToolCount": 8
    }
  },
  "sourceToolAssistantUUID": "9447036b-d255-4dbc-bf43-84455998f2a1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73813be2-f916-4121-a2d7-450b728cd138",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-16T08:52:33.349Z_

<details><summary>↩ Tool result · `toolu_01Vnycb98B3ShA9SDaBf3C9T`</summary>

````text
Now I have comprehensive information to provide a detailed answer.

---

Here is a detailed synthesis of the FASB paper ("Steering When Necessary: Flexible Steering Large Language Models with Backtracking", arXiv 2508.17621, NeurIPS 2025):

---

## 1. How FASB Decides WHEN to Steer -- Probe Architecture

The probe is a **simple linear classifier** (dot product + sigmoid) applied to attention head activations:

```
p_{theta}^{l,h}(x) = sigmoid(&lt;theta_{l,h}, x_{i,-1}^{l,h}>)
```

**Inputs:** The activation of the h-th attention head in layer l, extracted at the **last token position** of the generated sequence so far.

**Training:** Binary classification on concatenated question-answer pairs from a labeled dataset (e.g., TruthfulQA). Positive examples are truthful/aligned answers; negative examples are untruthful/misaligned ones.

**Head Selection:** After training a probe per head, the **top-k heads with highest validation accuracy** are selected (k=24 for TruthfulQA).

**Aggregation across heads:** The deviation probability at each generation step is the average prediction across the top-k heads:

```
p(x_{i,j}) = (1/k) * sum_{(l,h) in top-k} (1 - p_{theta}^{l,h}(x_{i,j}^{l,h}))
```

**Threshold:** Intervention is triggered when `p(x_{i,j}) > beta` (typically beta = 0.4-0.5).

**The probe parameters theta_{l,h} double as the steering vector** -- the same learned linear direction that classifies truthfulness is directly added to activations during intervention.

---

## 2. Geometric Features vs. Trained Binary Classifier

FASB's **main method uses a trained binary classifier** (the linear probe), NOT geometric features like distances or margins.

However, the paper includes an alternative **"Prototype" method** (Appendix A) that IS geometric:
- It computes class prototypes by averaging positive and negative activations
- Uses cosine similarity with temperature-scaled softmax: `exp(cos(x, theta_pos)/tau) / [exp(cos(x, theta_pos)/tau) + exp(cos(x, theta_neg)/tau)]`
- The steering vector becomes the mean difference: `theta = theta_pos - theta_neg`
- This is training-free (only averaging required)

The main reported results use the **Probe method** (trained classifier), which outperforms the Prototype method.

---

## 3. Granularity of the Steer/No-Steer Decision

The decision is made at **per-token granularity**. After generating each token, the system:

1. Extracts attention head activations for the newly generated token
2. Runs the linear probe across top-k heads
3. Averages the deviation scores
4. If the average exceeds threshold beta, triggers backtracking

**Backtracking mechanism:** When deviation is detected at token j, the system discards the last s tokens (default s=10) and regenerates them WITH activation steering applied. The intervention strength is adaptive:

```
r = I(p(x_{i,j}) > beta) * p(x_{i,j}) * alpha
```

where alpha controls overall magnitude. So stronger detected deviation leads to stronger steering.

---

## 4. TruthfulQA Results

**Model:** LLaMA2-7B-CHAT

| Method | True% | Info% | True x Info% | MC1% | MC2% | MC3% |
|--------|-------|-------|--------------|------|------|------|
| Baseline (no steering) | 66.83 | 99.51 | 66.50 | 33.41 | 51.07 | 24.76 |
| ITI | 94.49 | 80.55 | 76.11 | 38.31 | 57.15 | 30.53 |
| CAA | 71.60 | 83.84 | 60.03 | 34.03 | 52.76 | 25.62 |
| ORTHO | 67.94 | 90.09 | 61.21 | 36.23 | 52.88 | 26.12 |
| SADI-HEAD | 77.72 | 98.53 | 76.58 | 35.90 | 54.65 | 26.99 |
| **FASB (Probe)** | **93.88** | **85.81** | **80.56** | **48.71** | **66.58** | **41.95** |

FASB achieves the best True x Info (80.56%), MC1 (48.71%), MC2 (66.58%), and MC3 (41.95%), substantially outperforming all baselines. The MC1 improvement over ITI is +10.4 points.

**On other models:** Qwen2.5-7B saw improvements of +24.61 MC1 and +20.03 MC2. Qwen2.5-32B-Instruct improved MC1 from ~50% to ~69%.

**Six multiple-choice benchmarks** (COPA, StoryCloze, NLI, MMLU, SST2, Winogrande): FASB averaged **78.8%** vs. 65.1% baseline and 66.1% for SADI.

---

## 5. Comparison to Geometry-Based Detection Methods

**FASB does NOT compare to:**
- CCS (Contrast-Consistent Search)
- LEACE
- DRO (Distributionally Robust Optimization)
- Mass-mean probing
- Any purely geometric/unsupervised detection methods

**Baselines included are all activation steering methods:**
- ITI (Inference-Time Intervention)
- CAA (Contrastive Activation Addition)
- ORTHO (orthogonal projection-based)
- CAST
- ACT
- SADI / SADI-HEAD

The connection to geometry is implicit: the Prototype method (Appendix A) uses mean differences and cosine similarity, which is geometrically equivalent to mass-mean separation, but the paper does not frame it this way or cite geometric detection literature.

---

Sources:
- [arXiv Abstract - 2508.17621](https://arxiv.org/abs/2508.17621)
- [Full HTML Paper](https://arxiv.org/html/2508.17621v2)
- [OpenReview - NeurIPS 2025](https://openreview.net/forum?id=l75RyRcevf)
- [NeurIPS 2025 Poster](https://neurips.cc/virtual/2025/poster/116311)
- [ResearchGate Figure - Probing Accuracy per Head](https://www.researchgate.net/figure/Probing-accuracy-for-each-attention-head-of-the-LLM-on-TruthfulQA-dataset-for-linear_fig2_383654038)

agentId: a14e27dda29ff8451 (use SendMessage with to: 'a14e27dda29ff8451' to continue this agent)
&lt;usage>total_tokens: 21245
tool_uses: 11
duration_ms: 119661&lt;/usage>
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "parentUuid": "7e593084-7dd8-489d-b0eb-c8b206b74408",
  "isSidechain": false,
  "promptId": "fa61ad10-397c-4783-9490-82353cc0b8e8",
  "type": "user",
  "uuid": "f7592783-ba99-40ac-9ec9-6c5d873f3b79",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Use WebSearch and WebFetch to get more details about FASB \"Steering When Necessary: Flexible Steering Large Language Models with Backtracking\" (arXiv 2508.17621, NeurIPS 2025). I specifically need to understand:\n\n1. How does FASB decide WHEN to steer? What is the probe architecture?\n2. Does it use geometric features (distances, margins) or a trained binary classifier?\n3. At what granularity does it make the steer/no-steer decision? (Every token? Every few tokens? Sentence level?)\n4. What TruthfulQA results does it achieve?\n5. Does it compare to any geometry-based detection methods?\n\nTry fetching the arxiv abstract page: https://arxiv.org/abs/2508.17621\nAlso search for \"FASB steering when necessary TruthfulQA results\" and \"flexible activation steering probe backtracking\".",
    "agentId": "a14e27dda29ff8451",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have comprehensive information to provide a detailed answer.\n\n---\n\nHere is a detailed synthesis of the FASB paper (\"Steering When Necessary: Flexible Steering Large Language Models with Backtracking\", arXiv 2508.17621, NeurIPS 2025):\n\n---\n\n## 1. How FASB Decides WHEN to Steer -- Probe Architecture\n\nThe probe is a **simple linear classifier** (dot product + sigmoid) applied to attention head activations:\n\n```\np_{theta}^{l,h}(x) = sigmoid(&lt;theta_{l,h}, x_{i,-1}^{l,h}>)\n```\n\n**Inputs:** The activation of the h-th attention head in layer l, extracted at the **last token position** of the generated sequence so far.\n\n**Training:** Binary classification on concatenated question-answer pairs from a labeled dataset (e.g., TruthfulQA). Positive examples are truthful/aligned answers; negative examples are untruthful/misaligned ones.\n\n**Head Selection:** After training a probe per head, the **top-k heads with highest validation accuracy** are selected (k=24 for TruthfulQA).\n\n**Aggregation across heads:** The deviation probability at each generation step is the average prediction across the top-k heads:\n\n```\np(x_{i,j}) = (1/k) * sum_{(l,h) in top-k} (1 - p_{theta}^{l,h}(x_{i,j}^{l,h}))\n```\n\n**Threshold:** Intervention is triggered when `p(x_{i,j}) > beta` (typically beta = 0.4-0.5).\n\n**The probe parameters theta_{l,h} double as the steering vector** -- the same learned linear direction that classifies truthfulness is directly added to activations during intervention.\n\n---\n\n## 2. Geometric Features vs. Trained Binary Classifier\n\nFASB's **main method uses a trained binary classifier** (the linear probe), NOT geometric features like distances or margins.\n\nHowever, the paper includes an alternative **\"Prototype\" method** (Appendix A) that IS geometric:\n- It computes class prototypes by averaging positive and negative activations\n- Uses cosine similarity with temperature-scaled softmax: `exp(cos(x, theta_pos)/tau) / [exp(cos(x, theta_pos)/tau) + exp(cos(x, theta_neg)/tau)]`\n- The steering vector becomes the mean difference: `theta = theta_pos - theta_neg`\n- This is training-free (only averaging required)\n\nThe main reported results use the **Probe method** (trained classifier), which outperforms the Prototype method.\n\n---\n\n## 3. Granularity of the Steer/No-Steer Decision\n\nThe decision is made at **per-token granularity**. After generating each token, the system:\n\n1. Extracts attention head activations for the newly generated token\n2. Runs the linear probe across top-k heads\n3. Averages the deviation scores\n4. If the average exceeds threshold beta, triggers backtracking\n\n**Backtracking mechanism:** When deviation is detected at token j, the system discards the last s tokens (default s=10) and regenerates them WITH activation steering applied. The intervention strength is adaptive:\n\n```\nr = I(p(x_{i,j}) > beta) * p(x_{i,j}) * alpha\n```\n\nwhere alpha controls overall magnitude. So stronger detected deviation leads to stronger steering.\n\n---\n\n## 4. TruthfulQA Results\n\n**Model:** LLaMA2-7B-CHAT\n\n| Method | True% | Info% | True x Info% | MC1% | MC2% | MC3% |\n|--------|-------|-------|--------------|------|------|------|\n| Baseline (no steering) | 66.83 | 99.51 | 66.50 | 33.41 | 51.07 | 24.76 |\n| ITI | 94.49 | 80.55 | 76.11 | 38.31 | 57.15 | 30.53 |\n| CAA | 71.60 | 83.84 | 60.03 | 34.03 | 52.76 | 25.62 |\n| ORTHO | 67.94 | 90.09 | 61.21 | 36.23 | 52.88 | 26.12 |\n| SADI-HEAD | 77.72 | 98.53 | 76.58 | 35.90 | 54.65 | 26.99 |\n| **FASB (Probe)** | **93.88** | **85.81** | **80.56** | **48.71** | **66.58** | **41.95** |\n\nFASB achieves the best True x Info (80.56%), MC1 (48.71%), MC2 (66.58%), and MC3 (41.95%), substantially outperforming all baselines. The MC1 improvement over ITI is +10.4 points.\n\n**On other models:** Qwen2.5-7B saw improvements of +24.61 MC1 and +20.03 MC2. Qwen2.5-32B-Instruct improved MC1 from ~50% to ~69%.\n\n**Six multiple-choice benchmarks** (COPA, StoryCloze, NLI, MMLU, SST2, Winogrande): FASB averaged **78.8%** vs. 65.1% baseline and 66.1% for SADI.\n\n---\n\n## 5. Comparison to Geometry-Based Detection Methods\n\n**FASB does NOT compare to:**\n- CCS (Contrast-Consistent Search)\n- LEACE\n- DRO (Distributionally Robust Optimization)\n- Mass-mean probing\n- Any purely geometric/unsupervised detection methods\n\n**Baselines included are all activation steering methods:**\n- ITI (Inference-Time Intervention)\n- CAA (Contrastive Activation Addition)\n- ORTHO (orthogonal projection-based)\n- CAST\n- ACT\n- SADI / SADI-HEAD\n\nThe connection to geometry is implicit: the Prototype method (Appendix A) uses mean differences and cosine similarity, which is geometrically equivalent to mass-mean separation, but the paper does not frame it this way or cite geometric detection literature.\n\n---\n\nSources:\n- [arXiv Abstract - 2508.17621](https://arxiv.org/abs/2508.17621)\n- [Full HTML Paper](https://arxiv.org/html/2508.17621v2)\n- [OpenReview - NeurIPS 2025](https://openreview.net/forum?id=l75RyRcevf)\n- [NeurIPS 2025 Poster](https://neurips.cc/virtual/2025/poster/116311)\n- [ResearchGate Figure - Probing Accuracy per Head](https://www.researchgate.net/figure/Probing-accuracy-for-each-attention-head-of-the-LLM-on-TruthfulQA-dataset-for-linear_fig2_383654038)"
      }
    ],
    "totalDurationMs": 119661,
    "totalTokens": 21245,
    "totalToolUseCount": 11,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 998,
      "cache_read_input_tokens": 18506,
      "output_tokens": 1740,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 998
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1740,
          "cache_read_input_tokens": 18506,
          "cache_creation_input_tokens": 998,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 998,
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
      "otherToolCount": 11
    }
  },
  "sourceToolAssistantUUID": "7e593084-7dd8-489d-b0eb-c8b206b74408",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73813be2-f916-4121-a2d7-450b728cd138",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
````

</details>

---

### Tool result

_source line 37 · 2026-05-16T08:52:44.759Z_

<details><summary>↩ Tool result · `toolu_0126cABYA2U27ArnB8ywzZRH`</summary>

```text
I now have comprehensive evidence on all dimensions of your hypothesis. Here is my synthesis:

---

## Evidence Assessment: "Hidden state geometry at sentence boundaries is predictive of factuality in the next sentence"

### STRONG EVIDENCE FOR the hypothesis

**1. Hidden states encode factuality before generation occurs**

- **FactCheckmate** (arXiv 2410.02899) directly demonstrates that a classifier trained on hidden states produced over inputs -- *before decoding begins* -- achieves >70% preemptive hallucination detection accuracy, and intervention on those states yields 34.4% more factual outputs. This is the closest direct evidence that pre-generation hidden state geometry predicts factuality of upcoming content.

- **HALP** (arXiv 2603.05465, EACL 2026) shows hallucination risk is detectable from internal representations in a single forward pass *without generating a single token*, achieving up to 0.93 AUROC. Late query-token states (which are analogous to "boundary" representations) are most predictive for most architectures.

- **Simple Factuality Probes** (EMNLP 2025 Findings) demonstrates that lightweight linear probes on hidden states are "highly predictive of factuality in long-form natural language generation," achieving competitive performance with 100x fewer FLOPs than multi-sample methods. The probes work at the sentence/claim level.

- **On Early Detection of Hallucinations in Factual QA** (arXiv 2312.14183, KDD 2024) shows tokens *preceding* a hallucination can already predict the hallucination before it occurs (0.80 AUROC), including from "uninformative" formatting tokens -- suggesting boundary-adjacent positions carry the signal.

**2. Sentence-level structure in hidden states is real and exploitable**

- **"Let's Predict Sentence by Sentence"** (arXiv 2505.22202) directly shows that pretrained token-level LMs can be adapted to operate in a sentence-level embedding space, autoregressively predicting continuous embeddings of *next sentences*. This demonstrates that sentence-level planning information exists in the hidden state manifold and is extractable.

**3. Hallucination commits early -- at the very first tokens of a new segment**

- **"Hallucination as Trajectory Commitment"** (arXiv 2604.15400, April 2026) provides *causal* evidence that hallucination is an early trajectory commitment: in 44.3% of bifurcating prompts, factual vs. hallucinated trajectories diverge at the **first generated token**. Crucially, injecting a hallucinated activation corrupts output 87.5% of the time with a *single* perturbation, while correction requires sustained multi-step intervention. This strongly supports the idea that hidden state geometry at the boundary (transition point) is where the "decision" toward hallucination is made.

**4. Hidden state geometry specifically, not just activations, is informative**

- **"Where Does Reasoning Break?"** (arXiv 2605.13772, May 2026) frames hallucination detection as a *geometric* property of hidden-state trajectories -- correct reasoning moves through a stable manifold of locally coherent transitions, and errors appear as "localized excursions in transport cost." This directly validates the geometric framing.

- **ICR Probe** (arXiv 2507.16488, ACL 2025) captures the *cross-layer evolution* (dynamics) of hidden states rather than static representations, showing that the dynamic geometric structure of hidden states is more informative for hallucination detection than static snapshots.

**5. Activation steering at generation boundaries works**

- **Activation Steering Decoding** (ACL 2025) and **Dynamic Multimodal Activation Steering** (arXiv 2602.21704) show that intervening on hidden states during generation can reduce hallucination, with methods like FASB (Flexible Activation Steering with Backtracking) using classifiers on activation states to determine *when* to intervene -- implicitly confirming that boundary states carry predictive information.

---

### EVIDENCE AGAINST / CAVEATS

**1. Generalization challenges are real**

- **"Are the Hidden States Hiding Something?"** (arXiv 2505.16520, ACL 2025) is the strongest cautionary note. While partially validating that hidden states encode truthfulness, it shows that prior findings rely on *synthetic* datasets and **generalization to LLM-generated datasets remains challenging**. The paper's authors specifically warn that what works on controlled factoid statements may not transfer to realistic generation scenarios.

**2. Fundamental impossibility results**

- **"Hallucination is Inevitable"** (arXiv 2401.11817) proves LLMs cannot avoid hallucination in the general case. 
- **"On the Fundamental Impossibility of Hallucination Control"** (arXiv 2506.06382) shows no inference mechanism can simultaneously satisfy four properties needed for perfect hallucination control.
- **"(Im)possibility of Automated Hallucination Detection"** (arXiv 2504.17004) establishes that hallucination detection is equivalent to language identification -- theoretically hard in general. Reliable detection requires *both* correct and explicitly labeled incorrect examples.

These don't negate the hypothesis outright, but they bound its applicability: hidden state probes may work for *some* hallucination types but cannot be a universal solution.

**3. Hallucinations from distributional pressures, not "planning"**

- OpenAI's **"Why Language Models Hallucinate"** (arXiv 2509.04664) argues hallucinations arise from training/evaluation incentives that reward guessing over uncertainty acknowledgment. If hallucinations arise from stochastic distributional pressures at decoding time rather than from "plans" encoded in hidden states, then boundary-based prediction may have a ceiling.

**4. The "first token" commitment finding has limitations**

- The Trajectory Commitment paper (2604.15400) was conducted only on Qwen2.5-1.5B (a relatively small model) and only 44.3% of prompts showed clear bifurcation. The remaining 55.7% may involve more gradual drift where sentence-boundary geometry is less predictive.

---

### OVERALL ASSESSMENT

The hypothesis is **well-supported but with important caveats**:

- **Strongly supported**: Hidden states encode factuality information that is extractable via probes; this information exists before/at generation boundaries; the geometry (not just magnitude) of hidden states is informative; early commitment at transition points is causally demonstrated.
- **Partially challenged**: Generalization from synthetic to realistic LLM-generated text is an open problem; the approach cannot be universal due to fundamental impossibility results; effectiveness may vary substantially by model architecture and scale.

The hypothesis is a reasonable and empirically grounded assumption for a paper, but reviewers should note the generalization concerns from the ACL 2025 paper by Servedio et al. and the theoretical impossibility bounds.

---

Sources:
- [Are the Hidden States Hiding Something? (ACL 2025)](https://arxiv.org/abs/2505.16520)
- [FactCheckmate: Preemptively Detecting and Mitigating Hallucinations](https://arxiv.org/abs/2410.02899)
- [HALP: Detecting Hallucinations Without Generating a Single Token (EACL 2026)](https://arxiv.org/abs/2603.05465)
- [On Early Detection of Hallucinations in Factual QA (KDD 2024)](https://arxiv.org/abs/2312.14183)
- [Simple Factuality Probes Detect Hallucinations in Long-Form NLG (EMNLP 2025)](https://aclanthology.org/2025.findings-emnlp.880/)
- [Let's Predict Sentence by Sentence (arXiv 2505.22202)](https://arxiv.org/abs/2505.22202)
- [Hallucination as Trajectory Commitment (arXiv 2604.15400)](https://arxiv.org/abs/2604.15400)
- [Where Does Reasoning Break? Step-Level Hallucination Detection via Hidden-State Transport Geometry (arXiv 2605.13772)](https://arxiv.org/abs/2605.13772)
- [ICR Probe: Tracking Hidden State Dynamics (ACL 2025)](https://arxiv.org/abs/2507.16488)
- [Activation Steering Decoding (ACL 2025)](https://aclanthology.org/2025.acl-long.634/)
- [Dynamic Multimodal Activation Steering (arXiv 2602.21704)](https://arxiv.org/html/2602.21704v1)
- [Hallucination is Inevitable: An Innate Limitation of LLMs](https://arxiv.org/abs/2401.11817)
- [On the Fundamental Impossibility of Hallucination Control](https://arxiv.org/html/2506.06382v1)
- [(Im)possibility of Automated Hallucination Detection](https://arxiv.org/html/2504.17004v1)
- [Why Language Models Hallucinate (OpenAI)](https://arxiv.org/abs/2509.04664)
- [Adaptive Activation Steering (WWW 2025)](https://dl.acm.org/doi/10.1145/3696410.3714640)

agentId: aec4f1f23427c8feb (use SendMessage with to: 'aec4f1f23427c8feb' to continue this agent)
&lt;usage>total_tokens: 28849
tool_uses: 18
duration_ms: 125797&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d237932e-8cc2-4dde-a2b6-1695cc790e36",
  "isSidechain": false,
  "promptId": "fa61ad10-397c-4783-9490-82353cc0b8e8",
  "type": "user",
  "uuid": "81fb76fb-08b7-4f3d-b571-8260a8ae3bfc",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Use WebSearch to find any evidence FOR or AGAINST the hypothesis that \"hidden state geometry at sentence boundaries is predictive of factuality in the next sentence.\" This is a critical assumption of the paper I'm reviewing.\n\nSearch for:\n1. \"sentence boundary\" \"hidden state\" prediction hallucination OR factuality\n2. \"sentence planning\" transformer hidden states generation\n3. \"hallucination early detection\" \"before generation\" OR \"predictive\"\n4. \"Hallucination as Trajectory Commitment\" arxiv 2604.15400 — this paper claims \"early commitment\" in hallucination. Does it support detecting hallucination at sentence boundaries?\n5. \"hidden state\" predictive \"next sentence\" factuality OR accuracy OR hallucination\n\nAlso search for evidence AGAINST this hypothesis:\n6. \"hallucination unpredictable\" OR \"hallucination cannot be detected in advance\"\n7. \"activation steering timing\" when to intervene",
    "agentId": "aec4f1f23427c8feb",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "I now have comprehensive evidence on all dimensions of your hypothesis. Here is my synthesis:\n\n---\n\n## Evidence Assessment: \"Hidden state geometry at sentence boundaries is predictive of factuality in the next sentence\"\n\n### STRONG EVIDENCE FOR the hypothesis\n\n**1. Hidden states encode factuality before generation occurs**\n\n- **FactCheckmate** (arXiv 2410.02899) directly demonstrates that a classifier trained on hidden states produced over inputs -- *before decoding begins* -- achieves >70% preemptive hallucination detection accuracy, and intervention on those states yields 34.4% more factual outputs. This is the closest direct evidence that pre-generation hidden state geometry predicts factuality of upcoming content.\n\n- **HALP** (arXiv 2603.05465, EACL 2026) shows hallucination risk is detectable from internal representations in a single forward pass *without generating a single token*, achieving up to 0.93 AUROC. Late query-token states (which are analogous to \"boundary\" representations) are most predictive for most architectures.\n\n- **Simple Factuality Probes** (EMNLP 2025 Findings) demonstrates that lightweight linear probes on hidden states are \"highly predictive of factuality in long-form natural language generation,\" achieving competitive performance with 100x fewer FLOPs than multi-sample methods. The probes work at the sentence/claim level.\n\n- **On Early Detection of Hallucinations in Factual QA** (arXiv 2312.14183, KDD 2024) shows tokens *preceding* a hallucination can already predict the hallucination before it occurs (0.80 AUROC), including from \"uninformative\" formatting tokens -- suggesting boundary-adjacent positions carry the signal.\n\n**2. Sentence-level structure in hidden states is real and exploitable**\n\n- **\"Let's Predict Sentence by Sentence\"** (arXiv 2505.22202) directly shows that pretrained token-level LMs can be adapted to operate in a sentence-level embedding space, autoregressively predicting continuous embeddings of *next sentences*. This demonstrates that sentence-level planning information exists in the hidden state manifold and is extractable.\n\n**3. Hallucination commits early -- at the very first tokens of a new segment**\n\n- **\"Hallucination as Trajectory Commitment\"** (arXiv 2604.15400, April 2026) provides *causal* evidence that hallucination is an early trajectory commitment: in 44.3% of bifurcating prompts, factual vs. hallucinated trajectories diverge at the **first generated token**. Crucially, injecting a hallucinated activation corrupts output 87.5% of the time with a *single* perturbation, while correction requires sustained multi-step intervention. This strongly supports the idea that hidden state geometry at the boundary (transition point) is where the \"decision\" toward hallucination is made.\n\n**4. Hidden state geometry specifically, not just activations, is informative**\n\n- **\"Where Does Reasoning Break?\"** (arXiv 2605.13772, May 2026) frames hallucination detection as a *geometric* property of hidden-state trajectories -- correct reasoning moves through a stable manifold of locally coherent transitions, and errors appear as \"localized excursions in transport cost.\" This directly validates the geometric framing.\n\n- **ICR Probe** (arXiv 2507.16488, ACL 2025) captures the *cross-layer evolution* (dynamics) of hidden states rather than static representations, showing that the dynamic geometric structure of hidden states is more informative for hallucination detection than static snapshots.\n\n**5. Activation steering at generation boundaries works**\n\n- **Activation Steering Decoding** (ACL 2025) and **Dynamic Multimodal Activation Steering** (arXiv 2602.21704) show that intervening on hidden states during generation can reduce hallucination, with methods like FASB (Flexible Activation Steering with Backtracking) using classifiers on activation states to determine *when* to intervene -- implicitly confirming that boundary states carry predictive information.\n\n---\n\n### EVIDENCE AGAINST / CAVEATS\n\n**1. Generalization challenges are real**\n\n- **\"Are the Hidden States Hiding Something?\"** (arXiv 2505.16520, ACL 2025) is the strongest cautionary note. While partially validating that hidden states encode truthfulness, it shows that prior findings rely on *synthetic* datasets and **generalization to LLM-generated datasets remains challenging**. The paper's authors specifically warn that what works on controlled factoid statements may not transfer to realistic generation scenarios.\n\n**2. Fundamental impossibility results**\n\n- **\"Hallucination is Inevitable\"** (arXiv 2401.11817) proves LLMs cannot avoid hallucination in the general case. \n- **\"On the Fundamental Impossibility of Hallucination Control\"** (arXiv 2506.06382) shows no inference mechanism can simultaneously satisfy four properties needed for perfect hallucination control.\n- **\"(Im)possibility of Automated Hallucination Detection\"** (arXiv 2504.17004) establishes that hallucination detection is equivalent to language identification -- theoretically hard in general. Reliable detection requires *both* correct and explicitly labeled incorrect examples.\n\nThese don't negate the hypothesis outright, but they bound its applicability: hidden state probes may work for *some* hallucination types but cannot be a universal solution.\n\n**3. Hallucinations from distributional pressures, not \"planning\"**\n\n- OpenAI's **\"Why Language Models Hallucinate\"** (arXiv 2509.04664) argues hallucinations arise from training/evaluation incentives that reward guessing over uncertainty acknowledgment. If hallucinations arise from stochastic distributional pressures at decoding time rather than from \"plans\" encoded in hidden states, then boundary-based prediction may have a ceiling.\n\n**4. The \"first token\" commitment finding has limitations**\n\n- The Trajectory Commitment paper (2604.15400) was conducted only on Qwen2.5-1.5B (a relatively small model) and only 44.3% of prompts showed clear bifurcation. The remaining 55.7% may involve more gradual drift where sentence-boundary geometry is less predictive.\n\n---\n\n### OVERALL ASSESSMENT\n\nThe hypothesis is **well-supported but with important caveats**:\n\n- **Strongly supported**: Hidden states encode factuality information that is extractable via probes; this information exists before/at generation boundaries; the geometry (not just magnitude) of hidden states is informative; early commitment at transition points is causally demonstrated.\n- **Partially challenged**: Generalization from synthetic to realistic LLM-generated text is an open problem; the approach cannot be universal due to fundamental impossibility results; effectiveness may vary substantially by model architecture and scale.\n\nThe hypothesis is a reasonable and empirically grounded assumption for a paper, but reviewers should note the generalization concerns from the ACL 2025 paper by Servedio et al. and the theoretical impossibility bounds.\n\n---\n\nSources:\n- [Are the Hidden States Hiding Something? (ACL 2025)](https://arxiv.org/abs/2505.16520)\n- [FactCheckmate: Preemptively Detecting and Mitigating Hallucinations](https://arxiv.org/abs/2410.02899)\n- [HALP: Detecting Hallucinations Without Generating a Single Token (EACL 2026)](https://arxiv.org/abs/2603.05465)\n- [On Early Detection of Hallucinations in Factual QA (KDD 2024)](https://arxiv.org/abs/2312.14183)\n- [Simple Factuality Probes Detect Hallucinations in Long-Form NLG (EMNLP 2025)](https://aclanthology.org/2025.findings-emnlp.880/)\n- [Let's Predict Sentence by Sentence (arXiv 2505.22202)](https://arxiv.org/abs/2505.22202)\n- [Hallucination as Trajectory Commitment (arXiv 2604.15400)](https://arxiv.org/abs/2604.15400)\n- [Where Does Reasoning Break? Step-Level Hallucination Detection via Hidden-State Transport Geometry (arXiv 2605.13772)](https://arxiv.org/abs/2605.13772)\n- [ICR Probe: Tracking Hidden State Dynamics (ACL 2025)](https://arxiv.org/abs/2507.16488)\n- [Activation Steering Decoding (ACL 2025)](https://aclanthology.org/2025.acl-long.634/)\n- [Dynamic Multimodal Activation Steering (arXiv 2602.21704)](https://arxiv.org/html/2602.21704v1)\n- [Hallucination is Inevitable: An Innate Limitation of LLMs](https://arxiv.org/abs/2401.11817)\n- [On the Fundamental Impossibility of Hallucination Control](https://arxiv.org/html/2506.06382v1)\n- [(Im)possibility of Automated Hallucination Detection](https://arxiv.org/html/2504.17004v1)\n- [Why Language Models Hallucinate (OpenAI)](https://arxiv.org/abs/2509.04664)\n- [Adaptive Activation Steering (WWW 2025)](https://dl.acm.org/doi/10.1145/3696410.3714640)"
      }
    ],
    "totalDurationMs": 125797,
    "totalTokens": 28849,
    "totalToolUseCount": 18,
    "usage": {
      "input_tokens": 921,
      "cache_creation_input_tokens": 1151,
      "cache_read_input_tokens": 24511,
      "output_tokens": 2266,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1151
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 921,
          "output_tokens": 2266,
          "cache_read_input_tokens": 24511,
          "cache_creation_input_tokens": 1151,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1151,
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
      "otherToolCount": 18
    }
  },
  "sourceToolAssistantUUID": "d237932e-8cc2-4dde-a2b6-1695cc790e36",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73813be2-f916-4121-a2d7-450b728cd138",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 38 · 2026-05-16T08:52:44.768Z_

```json
{
  "parentUuid": "81fb76fb-08b7-4f3d-b571-8260a8ae3bfc",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "49c32690-6746-47b0-9bf4-f85195fa147b",
  "timestamp": "2026-05-16T08:52:44.768Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73813be2-f916-4121-a2d7-450b728cd138",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 39_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-16 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "49c32690-6746-47b0-9bf4-f85195fa147b",
  "sessionId": "73813be2-f916-4121-a2d7-450b728cd138"
}
```

---

### Runtime record

_source line 40_

```json
{
  "type": "ai-title",
  "aiTitle": "Geometry-triggered sentence-level hallucination steering",
  "sessionId": "73813be2-f916-4121-a2d7-450b728cd138"
}
```

---

### Assistant

_source line 41 · 2026-05-16T08:53:50.478Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have comprehensive research to form my review. Let me synthesize what I've found:

## Key Findings:

### 1. Reference Verification
- **Spherical Steering (2602.08169)**: VERIFIED. Exists, ICML 2026, vMF confidence gate, per-token, +15.8% MC1 on TruthfulQA (Llama-3.1-8B). Has released code.
- **Attractor Geometry (2605.05686)**: VERIFIED. Exists, AUROC 0.858 on TruthfulQA, basin absence characterization.


- **Hallucination Basins (2604.04743)**: VERIFIED. Exists, geometry-aware steering for 1B-3B models, though the specific implementation details around Euclidean distance triggers and scalar logistic-regression controllers aren't independently confirmed.
- **COAST (2605.01167)**: VERIFIED. Exists, constrained optimization approach achieving 30% ASR improvement.
- **FLAS (2605.05892)**: Referenced consistently but not independently verified.

### 2. Critical Missing Competitors

I'm noticing a significant gap—FASB from NeurIPS 2025 (arXiv 2508.17621) appears to be a major competitor that should be discussed, particularly given its probe-based approach.

FASB uses a learned classifier to determine when steering should be applied, which directly addresses the same "when to steer" problem that GTS is positioning as novel. It operates per-token with backtracking and achieves 48.71% MC1 on TruthfulQA with Llama2-7B-CHAT, using the probe's learned direction as the steering vector itself. This was published at a top venue, making it a critical reference point.

Beyond that, there are two other recent approaches that also aren't cited: Steering Vector Fields (SVF, arXiv 2602.01654) takes a context-aware, geometry-driven approach that refreshes steering directions dynamically during generation using concept boundary normals, and Curveball Steering (arXiv 2603.09313) explores nonlinear steering through polynomial methods. Both evaluate on similar benchmarks but represent different technical directions that should be acknowledged.

MESA (arXiv 2604.07914) tackles hallucination through selective latent intervention, addressing the entanglement problem in steering signals—another angle that's relevant but missing from the proposal.

Regarding the sentence-level gating claim, SENTINEL isn't really a competitor since it focuses on VLMs and preference learning rather than activation steering. But FASB is the real threat: it does exactly what GTS claims to do with sentence-level decisions, though it operates per-token with backtracking instead and uses a linear probe on attention heads rather than Mahalanobis distance on the residual stream.

The proposal doesn't cite FASB, which is a notable gap.

Looking at the timing hypothesis, the evidence is actually fairly encouraging—FactCheckmate shows hidden states predict factuality before decoding with over 70% accuracy, HALP achieves 0.93 AUROC for hallucination detection from a single forward pass, and multiple papers demonstrate early commitment signals in the first tokens. However, there are real limitations: generalization from synthetic to realistic text is harder than expected, only about 44% of prompts show clear bifurcation in the trajectory commitment work, and the theoretical foundations still need strengthening.

Now examining the novelty claims: sentence-level gating is genuinely differentiated from prior work like FASB (per-token) and Hallucination Basins (per-sequence), and the Mahalanobis distance trigger with per-layer MLP control does offer some technical distinction. But FASB's backtracking mechanism effectively achieves similar sub-sequence selectivity in practice, so the practical advantage isn't as clear-cut as claimed.

The real contribution is the combination of sentence-level gating with basin-distance triggering and the argument that sentences are the right intervention granularity for hallucinations—a reasonable incremental advance rather than a fundamental breakthrough.

For feasibility, the 240-270 hour estimate runs slightly over the 200-hour budget, and the 10-14 day timeline is tight but achievable. The timing hypothesis poses the biggest risk; if it doesn't work, the fallback approach adds complexity. I have the tools I need—nnsight 0.6 supports both target models, Spherical Steering has released code for comparison, and FActScore evaluation costs ($200-500 for GPT-4 API) are already factored in. I'm also noticing some critical citations I should address: FASB uses probe-based triggers with backtracking, Steering Vector Fields applies context-aware geometry with periodic updates, and Curveball Steering appears to be another recent approach I need to review.

The proposal handles several things well—it reports the honest AUROC number rather than inflating results, frames the timing hypothesis as testable with a fallback plan, acknowledges that Mahalanobis might not outperform Euclidean distance, and includes ablations to isolate each contribution. The main gap is FASB, a NeurIPS 2025 paper that directly tackles the "when to steer" question, which is surprisingly absent given how central that problem is to the work.

Looking at the overall assessment, the novelty is incremental—sentence-level gating is a reasonable idea but not particularly distinctive in a crowded field. Feasibility looks tight but achievable if the timing hypothesis pans out, though the resource estimates are slightly over budget. The writing is clear with a well-structured pipeline and thoughtful risk acknowledgments. Impact-wise, if successful it would be a useful contribution, but it's still incremental relative to existing work like Spherical Steering and FASB.

Averaging these scores gives 3.5, which falls short of the 4.0 threshold. The verdict is to revise—the proposal needs to better address FASB as the most direct competitor for the "when to steer" question, incorporate SVF's geometry-aware approach, more carefully argue the novelty over FASB, and tighten the resource estimate to stay within the 200 H100-hour budget. The novelty score of 3/5 reflects that while sentence-level gating is solid, the broader landscape already includes multiple geometry-aware selective steering approaches, making this contribution feel incremental rather than groundbreaking.

Feasibility sits at 3/5 due to the timing hypothesis being risky—only 44% of prompts show clear bifurcation patterns—and the resource estimate pushing past budget constraints, all within an 11-day window. The pipeline itself is well-defined with a reasonable fallback plan. Clarity scores 4/5 for the exceptionally structured proposal with honest risk assessment and explicit fallback mechanisms, though the missing FASB comparison weakens the positioning. Impact is 3/5 because while sentence-level gating could outperform token-level selective steering and continuous vMF gating, the expected improvement margin remains unclear.

That puts me at 3.25 overall, which normally suggests revision. But this is round 4 with substantial prior feedback incorporated, and the clarity is genuinely strong. The real blocker is FASB. If I can add those citations, compare against SVF, make a clear case for why sentence-level binary gating beats token-level probing with backtracking, and keep the resource estimate under 200 H100-hours, this becomes passable. These are all fixable.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "49c32690-6746-47b0-9bf4-f85195fa147b",
  "isSidechain": false,
  "requestId": "req_011Cb5xt2y9kcLuGbmu2X9yh",
  "type": "assistant",
  "uuid": "ccdb94cf-21cd-4fc8-941b-bd62d2a6cea9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73813be2-f916-4121-a2d7-450b728cd138",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RGp4SDPsVQEj5WwHdiatvK",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6160,
      "cache_read_input_tokens": 44341,
      "output_tokens": 4312,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6160,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 4312,
          "cache_read_input_tokens": 44341,
          "cache_creation_input_tokens": 6160,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6160
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

_source line 42 · 2026-05-16T08:54:24.303Z_

Now I have comprehensive evidence to form my review. Let me summarize the critical findings:

**Key discoveries:**
1. **FASB (NeurIPS 2025)** — a direct "when to steer" competitor using probe-based trigger + backtracking — is NOT cited
2. **Steering Vector Fields (Feb 2026)** — context-aware geometry-driven steering with periodic refresh — is NOT cited
3. **SENTINEL** is a VLM paper (not a text LLM competitor), so it's not threatening
4. The timing hypothesis has reasonable supporting evidence but with known generalization concerns
5. All major cited papers are verified as real

```json
{
  "verdict": "revise",
  "scores": {
    "novelty": {"score": 3, "rationale": "The sentence-level gating contribution is real but narrow. FASB (NeurIPS 2025) already solves 'when to steer' via probe-based triggering with backtracking, and Steering Vector Fields (Feb 2026) provides context-aware geometry-driven steering that refreshes periodically. The landscape is extremely crowded with 5+ geometry-aware selective steering methods from early 2026 alone."},
    "feasibility": {"score": 3, "rationale": "The timing hypothesis carries substantial risk—Trajectory Commitment (2604.15400) shows only 44.3% of prompts exhibit clear bifurcation, and 'Are the Hidden States Hiding Something?' (ACL 2025) warns synthetic-to-real generalization is hard. Auto estimate of 240-270 H100-hours exceeds the 200h budget. Pipeline is well-defined but tight."},
    "clarity": {"score": 4, "rationale": "Exceptionally well-structured proposal with clear stages, honest risk acknowledgments, planned ablations with matched baselines, and explicit fallback mechanisms. The positioning against Spherical Steering and Hallucination Basins is thorough. Only gap: missing FASB comparison leaves the 'when to steer' positioning incomplete."},
    "impact": {"score": 3, "rationale": "If sentence-level gating meaningfully outperforms FASB's token-level selective steering and Spherical Steering's continuous vMF gating, this would be useful. But the expected marginal improvement over these strong baselines (FASB achieves MC1 48.71% on TruthfulQA via selective steering) is uncertain and potentially small."}
  },
  "issues": [
    "CRITICAL MISSING COMPETITOR: FASB ('Steering When Necessary: Flexible Steering Large Language Models with Backtracking', arXiv 2508.17621, NeurIPS 2025) directly addresses the 'when to steer' problem using a probe-based trigger on attention heads with token-level adaptive steering + backtracking. It achieves MC1 48.71% on TruthfulQA (LLaMA2-7B-CHAT) and is published at a top venue. This is the most direct competitor to GTS's core contribution and is NOT cited.",
    "MISSING COMPETITOR: Steering Vector Fields (arXiv 2602.01654, Feb 2026) learns a differentiable concept scoring function whose local gradient defines context-aware steering directions, refreshing every K steps during generation. It uses geometric features (concept boundary normals via MLP) and evaluates on TruthfulQA + hallucination benchmarks. This is geometry-aware context-dependent steering — directly relevant and NOT cited.",
    "NOVELTY ARGUMENT INCOMPLETE: The proposal argues 'no existing method selectively gates at claim granularity' but FASB effectively achieves sub-sequence selectivity via token-level probe + backtracking (undo last 10 tokens and regenerate with steering). The proposal must argue why sentence-level binary gating is BETTER than FASB's mechanism — e.g., lower computational overhead (no rollback), cleaner intervention boundaries, better FActScore because claims are preserved/rejected atomically rather than partially regenerated.",
    "RESOURCE ESTIMATE EXCEEDS BUDGET: Auto estimate is 240-270 H100-hours, exceeding the user's hard constraint of ≤200 H100-hours. The ablation matrix (8+ conditions × 2 models × 10 benchmarks) needs trimming or the estimate needs to explain how it fits within budget.",
    "HALLUCINATION BASINS TECHNICAL CLAIMS UNVERIFIED: The proposal claims Hallucination Basins uses 'Euclidean distance trigger' and 'scalar logistic-regression controller' but my independent search could not confirm these specific technical details from the paper. The proposal should only claim what can be verified from the paper's content.",
    "CURVEBALL STEERING UNCITED: Curveball Steering (arXiv 2603.09313, March 2026) uses nonlinear steering via polynomial kernel PCA that explicitly addresses geometric distortions in activation space — relevant as a geometry-aware steering baseline not discussed."
  ],
  "feedback": "The proposal has matured significantly over four rounds and the core pipeline is well-designed. Three targeted fixes would bring it to passing quality:\n\n1. **Cite and position against FASB (NeurIPS 2025)**: FASB's probe-based trigger + backtracking is the most direct competitor for 'when to steer.' Position GTS's advantage as: (a) sentence-level binary decisions are computationally cheaper than FASB's per-token monitoring + rollback (no speculative computation wasted); (b) GTS preserves entire correct sentences untouched rather than partially regenerating them; (c) GTS's Mahalanobis trigger detects knowledge absence (a geometric property) while FASB's linear probe detects directional alignment (a surface-level feature that may not generalize). Add FASB as an ablation baseline: GTS-full vs. FASB-style per-token probe trigger (matching their mechanism but with your steering vector).\n\n2. **Cite Steering Vector Fields (2602.01654)**: Position as: SVF learns input-dependent steering DIRECTIONS (the 'how to steer' varies), while GTS learns input-dependent steering DECISIONS (the 'whether to steer' varies). SVF still steers at every K-step; GTS can skip entire sentences. These are complementary insights.\n\n3. **Trim resource estimate to ≤200 H100-hours**: Either reduce ablation conditions (e.g., combine Euclidean vs. Mahalanobis ablation with the scalar-vs-MLP ablation rather than running them separately) or reduce evaluation benchmarks for non-primary ablations (full 10-benchmark evaluation on GTS-full and top-2 baselines only, 4-benchmark subset for ablation variants). The user's hard constraint is 200h — present a plan that respects it.\n\nMinor: (a) Remove or soften the specific 'scalar logistic-regression controller' claim about Hallucination Basins unless you can verify it from the paper text. (b) Cite Curveball Steering as another geometry-aware approach in the broader landscape.",
  "reason": "Strong technical pipeline but missing FASB (NeurIPS 2025) — the most direct 'when to steer' competitor — and resource estimate exceeds the 200 H100-hour budget."
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ccdb94cf-21cd-4fc8-941b-bd62d2a6cea9",
  "isSidechain": false,
  "requestId": "req_011Cb5xt2y9kcLuGbmu2X9yh",
  "type": "assistant",
  "uuid": "a0ebba53-2c3f-4a36-91aa-12f853f790fb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73813be2-f916-4121-a2d7-450b728cd138",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RGp4SDPsVQEj5WwHdiatvK",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6160,
      "cache_read_input_tokens": 44341,
      "output_tokens": 4312,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6160,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 4312,
          "cache_read_input_tokens": 44341,
          "cache_creation_input_tokens": 6160,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6160
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

_source line 43_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-16 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "a0ebba53-2c3f-4a36-91aa-12f853f790fb",
  "sessionId": "73813be2-f916-4121-a2d7-450b728cd138"
}
```

---

### Runtime record

_source line 44_

```json
{
  "type": "ai-title",
  "aiTitle": "Geometry-triggered sentence-level hallucination steering",
  "sessionId": "73813be2-f916-4121-a2d7-450b728cd138"
}
```

---
