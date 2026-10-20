# Research conversation: You are a strict ML research reviewer conducting adversarial review. **Today's date: 2026-05-15 (UTC).** Your job: indep

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 59
- **Recorded user turns:** 1
- **Tool calls:** 13
- **Original source:** `logs/chats/exported-trajectories/account-2/5e709fca-c93a-4e70-85b1-fd9313a35a19.jsonl`
- **Structured JSON:** [`ad9bed5f214a0b64c82f.json`](../../sessions/ad/ad9bed5f214a0b64c82f.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-15T14:10:13.137Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-15T14:10:13.137Z",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19",
  "content": "You are a strict ML research reviewer conducting adversarial review.\n\n**Today's date: 2026-05-15 (UTC).**\n\nYour job: independently verify this idea's claims via WebSearch, then issue a verdict.\n\n## User requirements\nThe user asked for: **Target: EMNLP 2026, ARR submission deadline 2026-05-25 (11 days from today 2026-05-14). Track: Generation.\n\nDirection: Faithfulness, hallucination reduction, and calibrated uncertainty in LLM generation. In-scope: hallucination detection via internal representations (linear probes on hidden states, attention patterns, logit signatures), decoding-time interventions that suppress hallucinated content, calibration of verbalized confidence so model uncertainty matches actual accuracy, faithful chain-of-thought (CoT reflects actual computation, not post-hoc rationalization), attribution-aware generation with provenance to source spans, fine-grained atomic-claim verification during or after generation. Cross-cutting with Interpretability and Language Modeling tracks — the contribution must improve GENERATION quality, not just analyze model internals.\n\nContribution type: METHOD ONLY. Must propose a concrete detection algorithm, decoding-time intervention, training recipe, or calibration method. Pure analysis (\"we found models hallucinate when X\") is out of scope. Method + faithfulness analysis OK if analysis validates the method.\n\nHARD CONSTRAINTS:\n1. Compute: ≤200 H100-hours total. Hallucination work is mostly inference + lightweight probe training — budget for forward passes across many prompts + small classifier heads (linear probes, MLPs on hidden states). Avoid full SFT of large models.\n2. Time: ≤11 days. Use existing open models (Llama-3, Qwen3, DeepSeek-R1 distills, Mistral) + existing hallucination/faithfulness benchmarks. Build on interpretability toolkits (TransformerLens, nnsight) for hidden-state extraction if needed.\n3. Eval: TruthfulQA, HaluEval, FaithBench, FActScore, FELM, SimpleQA, LongFact for hallucination detection/reduction; ECE / Brier score / selective accuracy for calibration; faithfulness metrics on CoT (causal interventions, unlearning probes); attribution precision/recall on ELI5-attributed, ExpertQA. Must report both hallucination reduction AND utility preservation (MT-Bench, MMLU) — don't kill helpfulness while suppressing hallucinations.\n\nWhy this matters now: EMNLP 2025 awarded TWO Outstanding Papers in this space (\"Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations\", \"Measuring Chain of Thought Faithfulness by Unlearning Reasoning Steps\"), and the second annual Uncertainty Quantification workshop was held alongside. Hallucination is THE blocking issue for LLM deployment in high-stakes domains, and methods that exploit internal representations (rather than external retrieval or RLHF) are an emerging frontier. Look for: representation-level hallucination detectors that generalize across model families, decoding-time refusal/abstention mechanisms triggered by uncertainty features, calibration methods that work without holdout data, faithful-by-construction reasoning architectures (vs. post-hoc rationalization), atomic-fact-level verification integrated into generation. Avoid: yet another hallucination benchmark, RLHF-from-scratch calibration training, prompt-only \"say I don't know\" tricks, retrieval-augmented faithfulness (covered by Seed 2). Distinguish from existing Interpretability seed: that seed focuses on interpretability METHODS (circuits, probes as tools); this seed uses interpretability TECHNIQUES as means to improve generation faithfulness — output-quality contribution must be primary.**\nYou MUST evaluate whether this idea actually meets the user's requirements. If the user asked for a top venue, assess whether the idea is truly top-venue quality. If the user asked for low resource cost, verify the resource estimate is realistic and low. An idea that doesn't match what the user asked for should be \"revise\" or \"fail\".\n\n## 核心要求：非常仔细地调研，非常仔细地思考\n\n你是一个严格的审稿人。不要轻信 Generator 的任何 claim——你必须独立验证，深入思考每个维度。\n\n### 调研要求\n\n1. **独立 SOTA 验证**：自己搜索当前 SOTA，不要只检查 Generator 的引用。\n   每个验证维度建议用 2-3 种不同的搜索查询。\n\n2. **可行性深度检查**：\n   - 搜索类似实验的实际成本/周期\n   - 检查 claimed baselines 是否可复现\n   - 验证所需的 datasets/models 是否真的可以获取\n\n3. **新颖性压力测试**：专门搜索 Generator 可能遗漏的工作：\n   - 尝试不同的关键词组合\n   - 同时检查 arXiv 和 conference proceedings\n   - 寻找相邻领域的并行/concurrent 工作\n\n4. **深入阅读**：不要只依赖搜索摘要。用 WebFetch 实际阅读相关论文的 abstract 和关键章节，形成你自己的判断。\n\n### 思考要求\n\n5. **独立判断**：\n   - 不要因为 Generator 说得有道理就轻易 pass——真正好的 idea 经得起严格审查\n   - 思考这个 idea 在实际执行中会遇到什么困难\n   - 考虑这个 idea 对领域的真实贡献（不是自说自话的贡献）\n\n6. **评分诚实**：\n   - 不要给\"看起来还行\"的 idea 高分——4 分意味着\"确实很好\"，5 分意味着\"令人兴奋\"\n   - Agent 评分经常虚高，你的职责就是纠正这种偏差\n\n充分利用你的工具——做真正的调研，不是走过场。\n\n\n## 论文搜索策略\n\n你的搜索质量直接决定了 idea 的质量。不要敷衍搜索——每一次搜索都要有明确的目的。\n\n### 搜索源（推荐每个维度使用 2 个不同来源）\n\n1. **arXiv 预印本**（最新工作）:\n   - `site:arxiv.org {topic} {year}` — 按主题搜索最新论文\n   - `site:arxiv.org {method_name}` — 按具体方法名搜索\n   - `arxiv {topic} {month} {year}` — 精确到月份，找最近 3 个月的工作\n\n2. **Google Scholar**（引用关系 + 综合覆盖）:\n   - `{topic} {year} site:scholar.google.com` — 或直接搜索让 Google 自动包含 Scholar 结果\n   - `\"{exact paper title}\"` — 验证论文是否真实存在\n   - `\"{author name}\" {topic} {year}` — 按活跃作者追踪（找到领域大牛后追踪其最新工作）\n\n3. **Papers With Code**（SOTA 排行 + 代码可用性）:\n   - `site:paperswithcode.com {task_name}` — 查看任务的 SOTA 排行榜\n   - `site:paperswithcode.com {method_name}` — 查看方法是否已被实现\n   - `paperswithcode {dataset} benchmark` — 查看特定 dataset 上的竞争格局\n\n4. **OpenReview**（会议审稿 + 同行评价）:\n   - `site:openreview.net {topic} {year}` — 搜索会议提交的论文\n   - 用 WebFetch 阅读 OpenReview 上的 reviewer comments — 了解领域专家的真实评价\n\n5. **Semantic Scholar**（语义搜索 + 引用图谱）:\n   - `semantic scholar {topic} survey {year}` — 找综述论文\n   - `semanticscholar.org {paper_title}` — 查看 cited by（谁引用了这篇）和 references（它引用了谁）\n\n6. **GitHub**（实现验证）:\n   - `site:github.com {method_name} {task}` — 验证开源实现是否存在\n   - `site:huggingface.co {model_name}` — 验证模型/数据集是否可获取\n\n### 搜索维度（多角度交叉，不要只按 topic 搜）\n\n对每个 idea/方向，尽量覆盖以下维度：\n\n1. **正向搜索**：直接搜索主题相关论文\n   - `{topic} {subtopic} {year}`\n   - `{method_name} for {task_name}`\n\n2. **竞争论文搜索**（最关键！）：\n   - `{core_problem} {year}` — 有没有人在解决同样的问题？\n   - `{approach_keyword} {task} {year}` — 有没有人用类似方法？\n   - `{gap_description} solution` — 你发现的 gap 是否已被解决？\n   - **搜索知名团队的最新工作**：如果你知道哪些团队在做这个方向，搜索他们最近 6 个月的论文\n\n3. **相邻领域搜索**：\n   - `{method_from_other_field} applied to {your_task}`\n   - `{your_problem} in {adjacent_domain}` — 其他领域是否已解决类似问题\n\n4. **反面搜索**（找到反对你 idea 的证据）：\n   - `{your_approach} limitations` / `{your_approach} failure`\n   - `why {assumed_gap} is not a problem`\n   - `{baseline_method} sufficient for {task}` — baseline 是否其实已经够好\n\n5. **引用链追踪**（发现遗漏工作的最有效方法）：\n   - 找到一篇核心相关论文后，用 WebFetch 阅读它的 references 部分\n   - 在 Semantic Scholar 上查看它的 \"cited by\" — 最近引用它的论文很可能是 concurrent work\n   - 对 3 个以上核心相关论文重复此步骤\n\n### 搜索数量建议（理想目标，上下文充裕时尽量达到）\n\n| 角色 | 建议搜索次数 | 说明 |\n|------|-------------|------|\n| Round 1 Generator | 10-15 次 | 每个方向争取 3 次独立搜索 |\n| Round 2 Generator | 5-8 次 | 验证 approach 可行性 + baseline |\n| Review Agent | 8-12 次 | 独立验证 + 竞争论文 + 反面证据 |\n| Revision Agent | 5-10 次 | 针对每个 issue 独立调研 |\n\n### 上下文管理\n\n你的输出 token 有限，必须在上下文耗尽之前完成 JSON 输出。\n\n- 上述搜索次数是理想目标。在上下文充裕时应尽量多搜、深搜，搜得越充分越好。\n- 但必须动态评估剩余上下文：如果已经消耗了大量上下文，应优先完成输出，不要为了凑次数而冒着无法输出的风险。\n- WebFetch 深度阅读很有价值，但每次 fetch 消耗大量 token——优先 fetch 最关键的 2-3 篇，而不是每篇都 fetch。\n- 质量 > 数量：5 次精准搜索 + 深度思考 > 15 次浅层搜索。\n\n\nAs a reviewer, your search focus should be:\n1. **验证 claim**：Generator 声称的 SOTA、gap、novelty 是否属实\n2. **找竞争论文**：是否有 Generator 遗漏的高度相关/相似的工作\n3. **找反面证据**：是否有论文表明 Generator 的 approach 行不通\n4. **引用链检查**：通过核心论文的 cited-by 发现 concurrent work\n\n## 竞争论文专项搜索（Reviewer 独有）\n\n这是你作为 Reviewer 最重要的职责之一——发现 Generator 遗漏的竞争工作：\n\n1. **关键词变体搜索**：用至少 3 种不同的关键词组合搜索同一个问题\n   - 同义词替换（e.g., 'efficient' → 'lightweight/fast/scalable'）\n   - 不同粒度（e.g., 'text classification' → 'sentiment analysis' → 'NLP'）\n   - 方法名 + 任务名的不同组合\n\n2. **知名团队追踪**：如果你知道哪些团队/实验室在做相关方向，\n   搜索他们最近的论文（`\"team_name\" OR \"author_name\" {topic} {year}`）\n\n3. **会议最新录用**：搜索最近一轮 ICML/NeurIPS/ICLR/AAAI/ACL 等会议的 accepted papers\n   - `site:openreview.net {topic} 2026`\n   - `{conference_name} 2026 accepted papers {topic}`\n\n4. **arXiv 近 3 个月密集搜索**：对精确相关的关键词，搜索过去 3 个月的 arXiv 论文\n   这是发现 concurrent work 最有效的窗口\n\n如果你发现了 Generator 遗漏的重要相关工作，必须在 issues 中列出论文标题和链接，\n并在 feedback 中说明这些工作如何影响 idea 的 novelty。\n\n## Review checklist\n1. **SOTA freshness**: Are the models/baselines cited actually current SOTA?\n   If outdated, specify what the current SOTA is and cite your source.\n2. **Reference verification**: Do the cited papers actually exist? (WebSearch to check)\n3. **Gap validity**: Does the claimed research gap still exist, or has recent work addressed it?\n4. **Venue validity**: Are target_venues' submission deadlines after 2026-05-15?\n5. **Feasibility**: Is the resource estimate realistic? Are there hidden dependencies?\n6. **Novelty**: Is this sufficiently different from existing work?\n   When scoring novelty < 4:\n   - You MUST identify the closest existing work(s) via WebSearch\n   - In your feedback, write: \"This idea is too similar to [Paper Title (Venue Year)]. Specifically, [what overlaps]. To differentiate, the generator should [suggestion].\"\n   - This gives the generator targeted guidance to boost novelty, not just \"be more novel\".\n7. **Cost realism across modes**: Are the three mode estimates (manual/human-in-loop/auto) internally consistent?\n   - Auto Research uses more GPU hours (2-5x manual) but GPU idle rate should be near zero\n   - Auto Research timeline should reflect resource availability as bottleneck — days with sufficient GPUs, not weeks\n   - Human-in-Loop should fall between manual and auto on most dimensions\n   - Manual and HIL must NOT include salary/wages — only GPU and API costs\n   - Auto Research must NOT include agent operational overhead\n   - If any mode estimate is clearly unrealistic, flag it\n\n## Idea under review (round 3/10)\n{\n  \"title\": \"Read and Steer: Probe-Guided Claim-Level Confidence Calibration for Long-Form Generation\",\n  \"core_problem\": \"LLMs generate long-form outputs where hallucinated claims are expressed with the same high confidence as factual ones. Existing approaches either detect hallucinations at claim level without calibrating expressed confidence (Han et al., EMNLP 2025 — binary probes + neuron clamping), calibrate confidence only at response level for short-form QA (Ji et al., EMNLP 2025; Miao & Ungar, 2026; CORAL, 2026), use probe-guided steering without claim-level granularity or long-form scope (ITI, NeurIPS 2023; CLAS, 2026; ActCab/CoDec, EMNLP 2024), or require multi-stage training of the base model (CURE, April 2026; CAG, May 2026; LoVeC, May 2025). No existing method performs claim-level calibrated uncertainty expression in long-form generation without base model training. Furthermore, the accuracy-confidence orthogonality that enables clean steering (Miao & Ungar, 2026) has only been validated on 7–8B models for short-form QA — whether it holds at 70B scale in long-form generation is an open question with practical implications for the entire probe-guided steering paradigm.\",\n  \"opportunity\": \"Four recent results create a convergent opportunity: (1) Han et al. (EMNLP Findings 2025) showed lightweight linear probes on hidden states detect claim-level factuality in long-form generation, matching expensive multi-sample methods at up to 100× fewer FLOPs — but their neuron clamping intervention is binary (suppress/allow), not calibrated; (2) Miao & Ungar (March 2026) discovered that internal accuracy and verbalized confidence are nearly orthogonal linear features (cosine similarity < 0.04), meaning models internally know when they're wrong but fail to express this — and that adaptive CAA steering along these directions achieves major calibration improvement (ECE 14.9→3.7 on Llama-3.1-8B, 35.1→3.3 on Mistral-7B), but only for response-level QA on 7–8B models; (3) Kumaran et al. (March 2026) demonstrated that confidence representations are cached at answer-adjacent positions before verbalization, enabling real-time detection during generation; (4) CLAS (April 2026) demonstrated that probe-derived adaptive steering works on models up to Llama 3.1-70B across 11 benchmarks, providing evidence that the steering mechanism scales — though not specifically for confidence calibration. Combining these — reading claim-level accuracy signals via probes during long-form generation, then steering verbalized confidence to match — is unexplored and fills a specific gap. Critically, testing whether the accuracy-confidence orthogonality extends to 70B scale and long-form generation is itself a contribution that informs the feasibility of the entire probe-guided confidence steering paradigm.\",\n  \"landscape\": \"**Foundational probe→steer paradigm:** ITI (Li et al., NeurIPS 2023) introduced inference-time intervention: linear probes identify truthful directions in attention heads, and activations are shifted along these directions during generation. Foundational work, but targets truthfulness (content change) rather than calibrated confidence expression, and only on TruthfulQA.\\n\\n**Closest prior work — claim-level probing in long-form generation:** Han et al. (EMNLP Findings 2025) trained simple linear probes on LLM hidden states that detect claim-level hallucinations in long-form generation with performance matching expensive multi-sample methods (up to 100× fewer FLOPs), testing on models up to Llama 3.1-405B. Their neuron clamping causally reduces hallucinations by fixing activations of factuality-correlated neurons — but this is a binary intervention (suppress or allow) that does not produce calibrated verbal uncertainty expression. Obeso et al. (arXiv 2509.03531, 2025) trains entity-level probes for real-time streaming hallucination detection in long-form generation (AUC 0.90 on Llama-3.3-70B) — detection only, no calibrated steering.\\n\\n**Closest prior work — calibrated confidence steering:** Miao & Ungar (arXiv 2603.25052, March 2026) discovered that calibration accuracy and verbalized confidence are orthogonal linear features (cosine similarity < 0.04), and proposed two-stage adaptive CAA steering that reads internal accuracy and steers verbalized output to match, achieving ECE improvements from 14.9→3.7 (Llama-3.1-8B) and 35.1→3.3 (Mistral-7B) — but only for response-level short-form QA on 7–8B models. They explicitly acknowledge: 'Whether the linear encoding findings hold at larger scales remains open. Evaluation is restricted to question-answering tasks; extending to open-ended generation would require rethinking how the probe target is constructed.' Ji et al. (EMNLP 2025) discovered the Verbal Uncertainty Feature (VUF) and proposed MUC with ~30% reduction in confident hallucinations — also response-level, short-form, on ≤8B models.\\n\\n**Same-group prior work — CORAL:** CORAL (Miao, Cho & Ungar, arXiv 2602.06022, February 2026) uses regularized MLP probes on residual activations to predict correctness and steers at inference time, achieving 10% accuracy and 50% ECE improvements. However, CORAL targets MCQA on 7B models with response-level steering — no claim-level decomposition or long-form generation. RaS differs in (a) claim-level granularity via factuality probes, (b) long-form generation scope, and (c) confidence expression calibration rather than answer correctness steering.\\n\\n**Activation calibration + guided decoding:** ActCab/CoDec (EMNLP 2024) trains a linear layer on LM last-layer activations for confidence calibration, then uses confidence-guided decoding to elicit truthful answers. Same conceptual pipeline (activation-based calibration → guided generation) but operates at response level on QA, and modifies decoding probabilities rather than verbalized confidence expression.\\n\\n**Adaptive steering strength:** CLAS (Hsu et al., arXiv 2604.24693, April 2026) introduces context-dependent linear activation steering where steering strength adapts via learned sensing vectors: α_ℓ,t = (c_ℓ · [h_ℓ,t, 1]). Tested on Llama-3.1-70B across 11 benchmarks, demonstrating that probe-derived adaptive steering scales to 70B. RaS's α = β × max(0, threshold − probe_score) adapts similarly but is driven by factuality probe scores per-claim rather than a general context sensing vector, and targets confidence calibration specifically.\\n\\n**Mechanistic understanding:** 'How do LLMs Compute Verbal Confidence?' (Kumaran et al., arXiv 2603.17839, March 2026) provides convergent evidence that confidence representations emerge at answer-adjacent positions via cached retrieval, supporting the feasibility of online detection during generation.\\n\\n**Training-free steering baselines:** SteerConf (NeurIPS 2025) does prompt-based training-free confidence steering via multi-prompt aggregation. ACT (WWW 2025) applies tuning-free diverse steering vectors with adaptive intensity for truthfulness, scaling to 65B.\\n\\n**Claim-level long-form calibration (training-based):** CURE (arXiv 2604.12046, April 2026) uses multi-stage training to teach claim-level confidence reasoning, improving accuracy by up to 39.9%. CAG (arXiv 2605.01749, May 2026) achieves up to 13% factuality gain via training-based calibration-aware generation. LoVeC (arXiv 2505.23912, May 2025) uses RL to train LLMs to append on-the-fly confidence scores per statement in long-form generation, achieving 20× speedup over self-consistency methods. All three require base model fine-tuning or RL.\\n\\n**Post-generation claim-level approaches:** CSS (arXiv 2604.17487, April 2026) decomposes answers into claims and backs off uncertain ones using external verifiers. Selective Abstraction (arXiv 2602.11908, February 2026) replaces low-confidence atoms with confident abstractions.\\n\\n**Residual-stream anomaly detection:** PCNET (arXiv 2605.05953, May 2026) uses probabilistic circuits on residual streams for hallucination detection + contrastive decoding, reaching up to 99% AUROC — but targets short-form QA and changes content (different token selection) rather than expressing calibrated uncertainty.\\n\\n**Scaling concerns for activation steering:** Scaling laws for activation steering (ICML 2025) show that CAA effectiveness diminishes with model size on Llama 2 (7B→13B→70B) for behavioral steering (refusal). Endogenous steering resistance (arXiv 2602.06941, February 2026) shows Llama-3.3-70B has 3.8% ESR rate (vs <1% for smaller models). However, CLAS demonstrates successful probe-derived steering on Llama-3.1-70B, suggesting that adaptive, probe-guided steering may be more robust at scale than uniform CAA.\\n\\n**Gap:** No existing work combines claim-level factuality probing (à la Han et al.) with calibrated activation steering along the verbalized-confidence direction (à la Miao & Ungar) in a single-pass, online framework for long-form generation. This intersection — reading internal accuracy per-claim and steering verbalized confidence to match during generation — is the contribution space. Additionally, no work has tested whether the accuracy-confidence orthogonality discovered at 7–8B scale holds at 70B or in long-form generation contexts, making this verification itself a contribution to the mechanistic understanding of confidence representations.\",\n  \"approach\": \"We propose Read-and-Steer (RaS), a single-pass framework for claim-level calibrated uncertainty expression in long-form generation. The system reads internal accuracy signals per-claim via lightweight probes and steers verbalized confidence to match via targeted activation intervention, producing naturally hedged language for uncertain claims while leaving confident-and-correct claims untouched.\\n\\n**Pilot Experiment — Orthogonality Verification at Scale (~8h, 2× H100, first week):** Before committing the full experimental budget, we replicate Miao & Ungar's orthogonality analysis on Llama 3.1-70B in a long-form generation setting. We extract accuracy and confidence directions from biography-generation hidden states (not QA), measure their cosine similarity, and compare against the < 0.04 value found at 7–8B scale. This pilot has three outcomes: (a) orthogonality holds (cosine < 0.1) — proceed as planned, report the scaling result as a contribution; (b) orthogonality partially holds (cosine 0.1–0.3) — adapt steering to project out the accuracy component from the confidence direction before steering, proceed with modified approach; (c) orthogonality fails (cosine > 0.3) — report as an important negative finding about the limits of linear feature geometry at scale, fall back to the 8B-only configuration. All three outcomes produce publishable results.\\n\\n**Offline Stage 1 — Factuality Probe Training (~12h wall, 2× H100 for 70B; ~4h, 1× H100 for 8B; one-time per model):** Generate long-form outputs (biographies, factual descriptions) from the target model, decompose into atomic claims using FActScore/OpenFActScore decomposition, verify claim factuality against knowledge sources. Extract hidden states at each claim's token span across multiple layers (following Han et al.'s layer-group methodology). Train lightweight linear probes (logistic regression on span-aggregated hidden states) to predict continuous factuality confidence scores. Unlike Han et al.'s binary factuality labels, we train on soft labels derived from verification confidence, enabling graded uncertainty estimation.\\n\\n**Offline Stage 2 — Verbalized-Confidence Direction Extraction (~5h wall, 2× H100 for 70B; ~2h, 1× H100 for 8B; one-time per model):** Extract a verbalized-confidence steering direction via contrastive activation pairs: generate matched claim pairs where the same factual content is expressed with high confidence ('X was born in Y') vs. hedged uncertainty ('X was reportedly born in Y, though I am not certain'). The mean activation difference yields the steering direction, following the contrastive methodology from Ji et al. (VUF) and Miao & Ungar (CAA). For the 70B model, if the pilot reveals partial orthogonality degradation, we apply Gram-Schmidt orthogonalization to project the confidence direction away from the accuracy direction before use.\\n\\n**Online Stage — Probe-Guided Steering During Generation:** During autoregressive generation: (1) At each generated token, run the factuality probe on its hidden states — this is a single matrix-vector multiplication with negligible overhead. (2) Maintain a running mean probe score over the current sentence span using a sliding window. (3) At sentence boundaries (detected from generated punctuation — periods, newlines — which are trivially available during generation), evaluate the accumulated probe score against a calibrated threshold. (4) If the probe indicates internal uncertainty (score below threshold) while the generation shows no hedging markers, apply a steering offset along the extracted verbalized-confidence direction on subsequent tokens, with steering magnitude α proportional to the miscalibration gap: α = β × max(0, threshold − probe_score), where β is calibrated on a held-out validation set. This adaptive formula is conceptually related to CLAS's context-dependent steering, but driven by per-claim factuality probe scores rather than general input-context sensing vectors. (5) Deactivate steering when the probe score recovers above threshold.\\n\\n**Key design choices addressing known limitations:** (a) Span-aggregated probe scores over the full claim token range avoid the single-token prefix-contamination problem — the signal reflects the entire claim, not just the cumulative prefix. (b) Single-pass online monitoring eliminates the two-pass chicken-and-egg problem identified for the original CL-MUC approach — no position-aligned regeneration needed. (c) Continuous calibrated steering (not binary neuron clamping) produces graded hedging proportional to internal uncertainty, distinguishing this from Han et al.'s binary intervention. (d) Operating on the verbalized-confidence direction (orthogonal to accuracy per Miao & Ungar, verified at 70B scale in our pilot) means steering affects expression style without corrupting the model's factual knowledge. (e) Adaptive steering magnitude based on probe-detected need may mitigate the diminishing effectiveness of uniform CAA at larger scales (ICML 2025 scaling laws), since steering is only applied where needed and at probe-calibrated intensity.\\n\\n**Models:** Llama 3.1-70B-Instruct as primary (standard dense transformer architecture, well-studied for probing and steering, large enough to test scaling of the orthogonality finding, with CLAS confirming probe-derived steering viability at this scale). Llama 3.1-8B-Instruct as validation (enables direct comparison with Miao & Ungar and Ji et al. baselines on the same model family, validates the pipeline in well-charted territory before scaling). Both models use standard transformer attention across all layers, avoiding the untested territory of hybrid DeltaNet architectures (e.g., Qwen 3.5) where linear probe and steering techniques lack validation.\\n\\n**Benchmarks:** FActScore (biography generation, primary) and LongFact (diverse long-form factuality). Metrics: claim-level ECE, Brier score (calibration quality), AUROC (uncertainty detection), FActScore/factual precision (to verify steering does not degrade content quality), and MT-Bench fluency subset (to verify generation quality preservation). We also report the cosine similarity between accuracy and confidence directions at 70B scale as a standalone mechanistic finding.\\n\\n**Quantitative targets:** We expect RaS to achieve: (1) claim-level ECE reduction of ≥40% relative to unsteered baselines on both FActScore and LongFact; (2) FActScore preservation within 2% of unsteered baseline (steering affects verbal expression, not factual content); (3) uncertainty detection AUROC ≥0.80 (probe-based); (4) superior calibration (lower ECE) compared to Han et al.'s binary neuron clamping at comparable or better FActScore. These targets are informed by Miao & Ungar's response-level results (ECE reductions of 70–90% on QA), discounted for the harder claim-level long-form setting.\\n\\n**Comparisons:** (1) Unsteered baseline, (2) Han et al.'s probes + neuron clamping (closest representation-based method for long-form), (3) CURE (closest training-based method, if reproducible), (4) LoVeC (RL-based long-form verbalized confidence, if reproducible), (5) Ablations: probe-only detection without steering, uniform steering without probe guidance, VUF-only steering (Ji et al.'s original method applied per-claim), CORAL-style MLP probes vs. linear probes, varying layers for probe extraction, steering strength sensitivity, CLAS-style sensing vector vs. probe-score-driven adaptation.\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"~250h H100 80GB (orthogonality pilot ~8h [2×H100], probe training + direction extraction ~34h [20h 70B on 2×H100, 6h 8B], Llama 3.1-70B generation + evaluation on FActScore + LongFact ~100h [2×H100], Llama 3.1-8B validation ~25h, baseline comparisons ~45h, ablations ~38h)\",\n      \"gpu_utilization\": \"~20-30% effective — GPU idles during code development, pipeline debugging, and results analysis\",\n      \"timeline\": \"5-7 weeks (1 researcher full-time)\",\n      \"team\": \"1-2 researchers with mechanistic interpretability and activation steering experience\",\n      \"estimated_gpu_cost\": \"$625-875 (at ~$2.50-3.50/hr H100 80GB spot)\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"~200h H100 80GB (agent handles pipeline code, probe training iteration, evaluation scripting; human approves pilot results, probe design, steering threshold calibration, and ablation priorities)\",\n      \"gpu_utilization\": \"~45-60% — agent queues experiments between human check-ins\",\n      \"timeline\": \"3-4 weeks\",\n      \"team\": \"1 researcher, ~30min/day for methodology decisions, pilot outcome assessment, and qualitative hedging evaluation\",\n      \"claude_api_cost\": \"$100-200 (~1500-3000 Opus turns)\",\n      \"estimated_gpu_cost\": \"$500-700\",\n      \"risk_note\": \"Primary risk: whether accuracy-confidence orthogonality holds at 70B scale in long-form generation — the ~8h pilot experiment validates this before committing the full budget. If orthogonality breaks (outcome c), we fall back to an 8B-only paper with the negative scaling result as a contribution, reducing total compute to ~80h H100. Secondary risk: whether probe-guided steering produces natural hedging at 70B or degrades fluency — qualitative human assessment is essential. Tertiary risk: CAA effectiveness diminishing at 70B scale (per ICML 2025 scaling laws), though our adaptive probe-guided approach may be more robust than uniform steering.\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"~280h H100 80GB (agent explores probe architectures, layer selections, steering schedules across both models, plus comprehensive evaluation)\",\n      \"gpu_utilization\": \"~80-90% — continuous experiment pipeline with minimal idle\",\n      \"timeline\": \"7-10 days with 2× H100 80GB\",\n      \"team\": \"0 researchers (initial setup + final review only)\",\n      \"claude_api_cost\": \"$200-400 (~3000-6000 Opus turns)\",\n      \"estimated_gpu_cost\": \"$700-980\",\n      \"speed_bottleneck\": \"Long-form generation throughput on Llama 3.1-70B with 2× H100 tensor parallelism (~20-30 tok/s) — generating and evaluating hundreds of long-form responses per configuration is the computational bottleneck\",\n      \"risk_note\": \"Without human judgment, agent may over-optimize probe thresholds on validation set rather than ensuring robustness, may miss qualitative assessment of hedging naturalness, and critically may not correctly interpret the orthogonality pilot results (the decision to proceed vs. pivot requires understanding of the mechanistic implications)\"\n    }\n  },\n  \"target_venues\": [\n    \"AAAI 2027 (abstract Jul 21, full paper Jul 28, 2026 — ~10 weeks; conference Feb 16-23, Montréal) — PRIMARY\",\n    \"ARR August 2026 (submission Aug 3, 2026 — ~11 weeks; committable to EMNLP 2026 Oct 24-29 or later *ACL venues)\",\n    \"ICLR 2027 (expected submission ~Oct 2026, ~20 weeks; comfortable timeline)\"\n  ],\n  \"level\": \"solid\",\n  \"key_references\": [\n    \"Simple Factuality Probes Detect Hallucinations in Long-Form Natural Language Generation (Han et al., Findings of EMNLP 2025) — closest prior work: claim-level probes + neuron clamping in long-form generation\",\n    \"Closing the Confidence-Faithfulness Gap in LLMs (Miao & Ungar, arXiv 2603.25052, March 2026) — accuracy-confidence orthogonality discovery + adaptive CAA steering; explicitly notes scaling and long-form extension as open questions\",\n    \"Correctness-Optimized Residual Activation Lens [CORAL] (Miao, Cho & Ungar, arXiv 2602.06022, February 2026) — same group; MLP probes → correctness steering on MCQA at 7B scale; must differentiate as response-level, short-form only\",\n    \"Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations (Ji et al., EMNLP 2025) — VUF discovery and MUC for response-level short-form QA\",\n    \"Inference-Time Intervention: Eliciting Truthful Answers from a Language Model [ITI] (Li et al., NeurIPS 2023) — foundational probe→steer paradigm using linear probes on attention heads for truthfulness\",\n    \"Enhancing Language Model Factuality via Activation-Based Confidence Calibration and Guided Decoding [ActCab/CoDec] (EMNLP 2024) — activation calibration + confidence-guided decoding for QA factuality\",\n    \"Contextual Linear Activation Steering [CLAS] (Hsu et al., arXiv 2604.24693, April 2026) — probe-derived adaptive steering with context-dependent strength; tested on Llama-3.1-70B, confirming steering viability at 70B scale\",\n    \"How do LLMs Compute Verbal Confidence? (Kumaran et al., arXiv 2603.17839, March 2026) — mechanistic evidence for cached confidence retrieval at answer-adjacent positions\",\n    \"Reinforcement Learning for Better Verbalized Confidence in Long-Form Generation [LoVeC] (arXiv 2505.23912, May 2025) — RL-based on-the-fly confidence scoring per statement in long-form generation; training-based\",\n    \"Scaling Laws for Activation Steering with Llama 2 Models and Refusal Mechanisms (ICML 2025) — demonstrates CAA effectiveness diminishes with model size (7B→70B); informs our adaptive steering design\",\n    \"Endogenous Resistance to Activation Steering in Language Models (arXiv 2602.06941, February 2026) — Llama-3.3-70B shows 3.8% endogenous steering resistance; relevant scaling concern\",\n    \"Does Transformer Interpretability Transfer to RNNs? (2024) — probing and CAA partially transfer to recurrent architectures with reduced effectiveness; motivates our choice of standard transformer models\",\n    \"SteerConf: Steering LLMs for Confidence Elicitation (Zhou et al., NeurIPS 2025) — prompt-based training-free confidence calibration\",\n    \"Adaptive Activation Steering: A Tuning-Free LLM Truthfulness Improvement Method (ACT, WWW 2025) — diverse steering vectors with adaptive intensity control\",\n    \"Real-Time Detection of Hallucinated Entities in Long-Form Generation (Obeso et al., arXiv 2509.03531, 2025) — entity-level streaming probes for long-form generation\",\n    \"Hallucination as an Anomaly: Dynamic Intervention via Probabilistic Circuits [PCNET] (arXiv 2605.05953, May 2026) — residual stream anomaly detection + contrastive decoding intervention\",\n    \"Streaming Hallucination Detection in Long Chain-of-Thought Reasoning (arXiv 2601.02170, January 2026) — online hallucination detection as evolving latent state\",\n    \"Think Through Uncertainty: Improving Long-Form Generation Factuality via Reasoning Calibration [CURE] (arXiv 2604.12046, April 2026) — multi-stage training for claim-level confidence reasoning\",\n    \"Only Say What You Know: Calibration-Aware Generation for Long-Form Factuality [CAG] (arXiv 2605.01749, May 2026) — training-based calibration-aware generation\",\n    \"Atomic Calibration of LLMs in Long-Form Generations (Findings of AACL-IJCNLP 2025) — showed poor claim-level calibration in long-form outputs\",\n    \"Answer Only as Precisely as Justified: Calibrated Claim-Level Specificity Control [CSS] (arXiv 2604.17487, April 2026) — post-generation specificity control via external verifiers\",\n    \"When Should LLMs Be Less Specific? Selective Abstraction for Reliable Long-Form Text Generation (arXiv 2602.11908, February 2026)\",\n    \"Semantic Entropy Probes: Robust and Cheap Hallucination Detection in LLMs (ICML 2024) — linear probes approximate semantic entropy at response level\",\n    \"FActScore: Fine-grained Atomic Evaluation of Factual Precision in Long Form Text Generation (EMNLP 2023)\",\n    \"Long-form Factuality in Large Language Models [LongFact/SAFE] (NeurIPS 2024)\",\n    \"Steering Language Models With Activation Engineering (Turner et al., arXiv 2308.10248, 2023)\"\n  ],\n  \"description\": \"We propose Read-and-Steer (RaS), a single-pass framework for claim-level calibrated uncertainty expression in long-form generation. Motivated by two key findings — Han et al. (EMNLP 2025) showed lightweight probes detect claim-level factuality in long-form hidden states, and Miao & Ungar (2026) discovered that internal accuracy and verbalized confidence are nearly orthogonal linear features — RaS combines both insights in a novel way: it reads claim-level accuracy signals via factuality probes during autoregressive generation and steers verbalized confidence to match via targeted activation intervention along the orthogonal confidence direction, all within a single forward pass. Unlike Han et al.'s neuron clamping (binary suppression of hallucinations), RaS produces calibrated verbal hedging proportional to the model's internal uncertainty. Unlike CURE, CAG, and LoVeC, it requires no base model training — only lightweight linear probe fitting and contrastive direction extraction. The probe-guided adaptive steering formula (α = β × max(0, threshold − probe_score)) relates to CLAS's context-dependent steering but is driven by per-claim factuality signals rather than general context sensing, and targets confidence expression rather than content correctness (as in ITI, CORAL, and ActCab/CoDec). The framework includes a dedicated pilot experiment verifying the accuracy-confidence orthogonality at 70B scale in long-form generation — extending Miao & Ungar's finding beyond the 7–8B QA setting where it was established. We evaluate on Llama 3.1-70B (primary, testing scaling) and Llama 3.1-8B (validation, direct comparison with prior work) using FActScore and LongFact, measuring claim-level ECE, Brier score, AUROC, and factual precision. We expect ≥40% claim-level ECE reduction over unsteered baselines while preserving FActScore within 2%. Both models use standard transformer architectures, avoiding the untested hybrid DeltaNet territory (e.g., Qwen 3.5) where linear probing and activation steering techniques lack validation. All experiments fit within ~250 H100-hours.\",\n  \"project_name\": \"probe_guided_claim_calibration\",\n  \"source\": \"web_research\"\n}\n\n\n## Previous review history\n### Round 1 review\nVerdict: revise\nIssues: [\"CRITICAL MISSING COMPETITOR: Han et al. 'Simple Factuality Probes Detect Hallucinations in Long-Form Natural Language Generation' (EMNLP Findings 2025) — same Oxford group as Semantic Entropy Probes — already does claim-level hidden-state probing + neuron clamping for causal hallucination reduction in long-form generation. This is the closest existing work and was completely missed.\", \"MISSING COMPETITOR: Miao & Ungar 'Closing the Confidence-Faithfulness Gap in LLMs' (arXiv 2603.25052, March 2026) uses CAA steering for confidence calibration, finding calibration and verbalized confidence are orthogonal linear features. Their two-stage adaptive steering pipeline is closely related.\", \"MISSING WORK: 'How do LLMs Compute Verbal Confidence?' (arXiv 2603.17839, March 2026) provides mechanistic analysis of verbal confidence computation; SteerConf (NeurIPS 2025) does training-free steering for confidence calibration; Adaptive Activation Steering (ACT, WWW 2025) does tuning-free diverse steering vectors for truthfulness; 'Real-Time Detection of Hallucinated Entities' (Obeso et al., 2025) does entity-level probes in long-form. None cited.\", \"VUF was validated ONLY on 7-8B dense models (Llama3.1-8B, Mistral-7B, Qwen2.5-7B). The paper itself notes Qwen2.5 shows 'significantly less sensitivity' to VUF steering. Transfer to Qwen3.5-27B is unverified, and transfer to Llama 4 Scout (109B MoE, 16 experts) is extremely unlikely to work cleanly — MoE architectures route different tokens through different experts, making linear feature identification fundamentally harder.\", \"Two-pass generation has a chicken-and-egg problem: pass 1 identifies claims and their token positions; steering in pass 2 changes the generation, so claims will appear at different positions or be entirely different. The approach assumes regeneration reproduces the same claims in the same positions, which activation steering specifically disrupts.\", \"Resource estimate (300h A100 manual, 200h A100 HIL, 500h auto) exceeds the user's hard constraint of ≤200 H100-hours total. Even the HIL estimate at 200h A100 ≈ 130-150h H100 equivalent is optimistic given the need for two-pass generation across multiple benchmarks with 27B+ models.\", \"Semantic Entropy Probes were designed for response-level uncertainty approximation. Adapting them to claim-level semantic uncertainty in long-form contexts requires new training data and potentially different probe architectures — this is not a trivial adaptation and the '~30h' SEP training estimate is likely too low.\", \"The 'claim's final token position' VUF projection assumes clean per-claim signals, but in autoregressive generation, hidden states at position i are conditioned on ALL preceding tokens. The VUF signal at a claim's last token reflects the entire prefix, not just that claim — extraction may not give meaningful per-claim uncertainty.\"]\nFeedback: The idea has a clear and appealing structure, but faces critical novelty and feasibility problems that must be addressed:\n\n**Novelty — differentiate from Han et al. (2025):** This is the single most important fix. Han et al. already showed that simple linear probes on hidden states detect hallucinations at claim level in long-form generation AND that neuron clamping causally reduces hallucinations. You MUST: (1) cite this paper prominently as the closest prior work, (2) articulate what VUF+SEP dual-signal scoring adds over simple factuality probes (e.g., better calibration vs. binary factuality, verbal hedging rather than deletion/clamping), (3) run head-to-head comparisons. Also cite Miao & Ungar (2026) on CAA steering for calibration.\n\n**Feasibility — drop Llama 4 Scout, fix the two-pass problem:**\n- Replace Llama 4 Scout with a dense model (Llama 3.1-70B, Qwen2.5-72B, or stick with Qwen3.5-27B only). MoE models are too risky for VUF extraction in 11 days.\n- Rethink the two-pass approach: consider single-pass with streaming claim detection (detect uncertainty signals during generation and intervene in real-time using a sliding window), or adopt a post-hoc rewriting/hedging approach that doesn't require position-aligned regeneration.\n- Reduce scope to 1 model with ablations rather than 2 models × 4 benchmarks.\n\n**Compute — stay within budget:**\n- The ≤200 H100-hour constraint means roughly 1 model, 2-3 benchmarks max with focused experiments.\n- Drop extensive ablation sweeps in favor of one clean comparison: CL-MUC vs. Han et al.'s probes vs. CURE/CAG.\n\n**Technical — address the claim-level VUF signal problem:**\n- Provide evidence or pilot results that VUF projection at claim-final tokens gives meaningful per-claim uncertainty, or pivot to a different extraction strategy (e.g., aggregate VUF across all tokens in a claim span).\n\n### Round 2 review\nVerdict: revise\nIssues: [\"CRITICAL — Qwen3.5-27B architecture mismatch: Qwen3.5-27B uses a hybrid Gated DeltaNet + attention architecture (3:1 ratio). 75% of layers are DeltaNet (linear attention), fundamentally different from standard transformer attention. Linear probes, contrastive activation directions, and steering techniques were developed and validated ONLY on standard transformer architectures. TransformerLens does not support DeltaNet layers. The proposal claims Qwen3.5-27B is 'confirmed viable for activation steering' — this is false and unverified. The entire primary experimental setup may fail on day 1.\", \"CRITICAL — Unverified scaling assumption: Miao & Ungar's accuracy-confidence orthogonality (cosine similarity < 0.04) was demonstrated ONLY on 7-8B standard transformers (Llama-3.1-8B, Mistral-7B, Qwen2.5-7B) on short-form QA. They explicitly state: 'Whether the linear encoding findings hold at larger scales remains open. Evaluation is restricted to question-answering tasks; extending to open-ended generation would require rethinking how the probe target is constructed.' RaS critically depends on this orthogonality holding at 27B scale in long-form generation — this is an assumption, not a validated property.\", \"MISSING COMPETITOR — CORAL (arXiv 2602.06022, Feb 2026): From the SAME Miao & Ungar group. Trains MLP probes on residual stream activations to predict correctness, then steers model behavior at inference time — essentially the same probe→steer pipeline concept. Evaluates on MCQA with 7B models. Must be cited and differentiated as same-group prior work.\", \"MISSING COMPETITOR — CLAS (arXiv 2604.24693, April 2026): Contextual Linear Activation Steering uses probe-derived steering vectors with dynamic, context-dependent strength. RaS's α = β × max(0, threshold − probe_score) is conceptually similar to CLAS's adaptive steering strength. Must be cited.\", \"MISSING COMPETITOR — ITI (NeurIPS 2023, Li et al.): Inference-Time Intervention — the foundational work that uses linear probes to identify truthful directions in attention heads and steers during generation. The probe→steer-during-generation paradigm originates here. Not cited.\", \"MISSING COMPETITOR — ActCab/CoDec (EMNLP 2024): Trains a linear layer on LM last-layer activations for confidence calibration, then uses confidence-guided decoding to elicit truthful answers. Same conceptual pipeline (activation-based calibration → guided generation). Not cited.\", \"Timeline risk: EMNLP 2026 ARR deadline is May 25, 2026 — 10 days away. With the DeltaNet architecture risk likely requiring a pivot to Llama 3.1-8B only (reducing the paper to a direct comparison with Miao & Ungar on the same 8B model), this is not enough time to produce competitive results. AAAI 2027 (July 28) is more realistic.\", \"Qwen2.5 sensitivity acknowledged but not addressed: Miao & Ungar note that Qwen2.5-7B shows 'significantly less sensitivity' to VUF steering compared to Llama and Mistral. If Qwen models are inherently less responsive to this type of steering, the Qwen3.5-27B results may be disappointing even if the architecture challenge is resolved.\"]\nFeedback: The core idea — combining Han et al.'s claim-level probes with Miao & Ungar's calibrated confidence steering in single-pass long-form generation — addresses a genuine gap. But there are critical issues that must be resolved:\n\n**1. Replace Qwen3.5-27B as primary model (HIGHEST PRIORITY):**\nQwen3.5-27B's hybrid DeltaNet architecture (75% linear attention layers) is untested territory for linear probes and activation steering. All prior work validated these techniques on standard transformer architectures. Options:\n- **Best option**: Use Llama 3.1-70B (standard transformer, well-studied, large enough to be compelling) as primary, with Llama 3.1-8B as validation for direct comparison to Miao & Ungar. This requires ~2× the compute of 8B but fits within 200 H100-hours if you drop Qwen entirely.\n- **Alternative**: Use Qwen2.5-32B (standard transformer architecture, unlike Qwen3.5). But note Qwen2.5 shows reduced sensitivity to confidence steering per Miao & Ungar.\n- **Risky fallback**: Keep Qwen3.5-27B but acknowledge it as an architectural exploration, not 'confirmed viable.' Run a 5h pilot on DeltaNet-layer probing before committing.\n\n**2. Cite all missing competitors and sharpen differentiation:**\nAdd CORAL (same group as Miao & Ungar — probe→steer on MCQA), CLAS (dynamic steering strength from probes), ITI (foundational probe→steer work, NeurIPS 2023), and ActCab/CoDec (activation calibration + guided decoding, EMNLP 2024). Your differentiation should be: all prior probe→steer work operates at response level on short-form QA; RaS is the first to operate at claim level during long-form generation with calibrated (not binary) confidence expression.\n\n**3. Address the orthogonality scaling gap explicitly:**\nDon't claim orthogonality transfers — frame it as a hypothesis to test. Add a dedicated experiment: replicate Miao & Ungar's orthogonality analysis on your primary model (measuring cosine similarity between accuracy and confidence directions at 27B+ scale on long-form generation). This is both a contribution (extending the finding to new settings) and a risk-mitigation step.\n\n**4. Target AAAI 2027 (July 28) instead of EMNLP (May 25):**\n10 days is too tight for a paper with this many unvalidated assumptions. AAAI gives 10+ weeks, which allows: 1-week pilot on architecture/orthogonality, 3-week implementation, 2-week evaluation, 4-week writing. Still ambitious but feasible.\n\n**5. Strengthen the impact argument:**\nThe crowded landscape (CURE, CAG, CSS, PCNET, LoVeC, Rewarding Doubt) means you need clear quantitative expectations. State upfront: 'We expect RaS to achieve claim-level ECE below X (vs. Y for unsteered and Z for binary clamping) while maintaining FActScore above W.' Without specific targets, the paper risks being 'we tried the obvious combination and it kind of worked.'\n\n\n## Output format\nOutput ONLY a JSON object:\n{\n  \"verdict\": \"pass | revise | fail\",\n  \"scores\": {\n    \"novelty\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"feasibility\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"clarity\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"impact\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"}\n  },\n  \"issues\": [\"specific issue 1\", \"specific issue 2\", ...],\n  \"feedback\": \"Actionable feedback for the generator (if verdict=revise)\",\n  \"reason\": \"One-line summary of verdict rationale\"\n}\n\nRules:\n- \"pass\": idea is sound AND high quality — avg score >= 4.0, no critical issues\n- \"revise\": fixable issues OR scores below threshold — provide specific feedback\n- \"fail\": fundamental flaw (e.g., gap doesn't exist, approach provably wrong, or scores remain low after multiple revisions)\n- Threshold is HIGH (4.0/5.0): agent scores tend to be inflated, so only truly outstanding ideas should pass. An avg of 3.5 is NOT enough.\n- Round 10 only: if still \"revise\", you MUST choose \"pass\" or \"fail\"."
}
```

---

### Runtime record

_source line 2 · 2026-05-15T14:10:13.142Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-15T14:10:13.142Z",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19"
}
```

---

## Round 1

57 recorded events

### User

_source line 3 · 2026-05-15T14:10:13.176Z_

You are a strict ML research reviewer conducting adversarial review.

**Today's date: 2026-05-15 (UTC).**

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
4. **Venue validity**: Are target_venues' submission deadlines after 2026-05-15?
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

## Idea under review (round 3/10)
{
  "title": "Read and Steer: Probe-Guided Claim-Level Confidence Calibration for Long-Form Generation",
  "core_problem": "LLMs generate long-form outputs where hallucinated claims are expressed with the same high confidence as factual ones. Existing approaches either detect hallucinations at claim level without calibrating expressed confidence (Han et al., EMNLP 2025 — binary probes + neuron clamping), calibrate confidence only at response level for short-form QA (Ji et al., EMNLP 2025; Miao & Ungar, 2026; CORAL, 2026), use probe-guided steering without claim-level granularity or long-form scope (ITI, NeurIPS 2023; CLAS, 2026; ActCab/CoDec, EMNLP 2024), or require multi-stage training of the base model (CURE, April 2026; CAG, May 2026; LoVeC, May 2025). No existing method performs claim-level calibrated uncertainty expression in long-form generation without base model training. Furthermore, the accuracy-confidence orthogonality that enables clean steering (Miao & Ungar, 2026) has only been validated on 7–8B models for short-form QA — whether it holds at 70B scale in long-form generation is an open question with practical implications for the entire probe-guided steering paradigm.",
  "opportunity": "Four recent results create a convergent opportunity: (1) Han et al. (EMNLP Findings 2025) showed lightweight linear probes on hidden states detect claim-level factuality in long-form generation, matching expensive multi-sample methods at up to 100× fewer FLOPs — but their neuron clamping intervention is binary (suppress/allow), not calibrated; (2) Miao & Ungar (March 2026) discovered that internal accuracy and verbalized confidence are nearly orthogonal linear features (cosine similarity < 0.04), meaning models internally know when they're wrong but fail to express this — and that adaptive CAA steering along these directions achieves major calibration improvement (ECE 14.9→3.7 on Llama-3.1-8B, 35.1→3.3 on Mistral-7B), but only for response-level QA on 7–8B models; (3) Kumaran et al. (March 2026) demonstrated that confidence representations are cached at answer-adjacent positions before verbalization, enabling real-time detection during generation; (4) CLAS (April 2026) demonstrated that probe-derived adaptive steering works on models up to Llama 3.1-70B across 11 benchmarks, providing evidence that the steering mechanism scales — though not specifically for confidence calibration. Combining these — reading claim-level accuracy signals via probes during long-form generation, then steering verbalized confidence to match — is unexplored and fills a specific gap. Critically, testing whether the accuracy-confidence orthogonality extends to 70B scale and long-form generation is itself a contribution that informs the feasibility of the entire probe-guided confidence steering paradigm.",
  "landscape": "**Foundational probe→steer paradigm:** ITI (Li et al., NeurIPS 2023) introduced inference-time intervention: linear probes identify truthful directions in attention heads, and activations are shifted along these directions during generation. Foundational work, but targets truthfulness (content change) rather than calibrated confidence expression, and only on TruthfulQA.\n\n**Closest prior work — claim-level probing in long-form generation:** Han et al. (EMNLP Findings 2025) trained simple linear probes on LLM hidden states that detect claim-level hallucinations in long-form generation with performance matching expensive multi-sample methods (up to 100× fewer FLOPs), testing on models up to Llama 3.1-405B. Their neuron clamping causally reduces hallucinations by fixing activations of factuality-correlated neurons — but this is a binary intervention (suppress or allow) that does not produce calibrated verbal uncertainty expression. Obeso et al. (arXiv 2509.03531, 2025) trains entity-level probes for real-time streaming hallucination detection in long-form generation (AUC 0.90 on Llama-3.3-70B) — detection only, no calibrated steering.\n\n**Closest prior work — calibrated confidence steering:** Miao & Ungar (arXiv 2603.25052, March 2026) discovered that calibration accuracy and verbalized confidence are orthogonal linear features (cosine similarity < 0.04), and proposed two-stage adaptive CAA steering that reads internal accuracy and steers verbalized output to match, achieving ECE improvements from 14.9→3.7 (Llama-3.1-8B) and 35.1→3.3 (Mistral-7B) — but only for response-level short-form QA on 7–8B models. They explicitly acknowledge: 'Whether the linear encoding findings hold at larger scales remains open. Evaluation is restricted to question-answering tasks; extending to open-ended generation would require rethinking how the probe target is constructed.' Ji et al. (EMNLP 2025) discovered the Verbal Uncertainty Feature (VUF) and proposed MUC with ~30% reduction in confident hallucinations — also response-level, short-form, on ≤8B models.\n\n**Same-group prior work — CORAL:** CORAL (Miao, Cho & Ungar, arXiv 2602.06022, February 2026) uses regularized MLP probes on residual activations to predict correctness and steers at inference time, achieving 10% accuracy and 50% ECE improvements. However, CORAL targets MCQA on 7B models with response-level steering — no claim-level decomposition or long-form generation. RaS differs in (a) claim-level granularity via factuality probes, (b) long-form generation scope, and (c) confidence expression calibration rather than answer correctness steering.\n\n**Activation calibration + guided decoding:** ActCab/CoDec (EMNLP 2024) trains a linear layer on LM last-layer activations for confidence calibration, then uses confidence-guided decoding to elicit truthful answers. Same conceptual pipeline (activation-based calibration → guided generation) but operates at response level on QA, and modifies decoding probabilities rather than verbalized confidence expression.\n\n**Adaptive steering strength:** CLAS (Hsu et al., arXiv 2604.24693, April 2026) introduces context-dependent linear activation steering where steering strength adapts via learned sensing vectors: α_ℓ,t = (c_ℓ · [h_ℓ,t, 1]). Tested on Llama-3.1-70B across 11 benchmarks, demonstrating that probe-derived adaptive steering scales to 70B. RaS's α = β × max(0, threshold − probe_score) adapts similarly but is driven by factuality probe scores per-claim rather than a general context sensing vector, and targets confidence calibration specifically.\n\n**Mechanistic understanding:** 'How do LLMs Compute Verbal Confidence?' (Kumaran et al., arXiv 2603.17839, March 2026) provides convergent evidence that confidence representations emerge at answer-adjacent positions via cached retrieval, supporting the feasibility of online detection during generation.\n\n**Training-free steering baselines:** SteerConf (NeurIPS 2025) does prompt-based training-free confidence steering via multi-prompt aggregation. ACT (WWW 2025) applies tuning-free diverse steering vectors with adaptive intensity for truthfulness, scaling to 65B.\n\n**Claim-level long-form calibration (training-based):** CURE (arXiv 2604.12046, April 2026) uses multi-stage training to teach claim-level confidence reasoning, improving accuracy by up to 39.9%. CAG (arXiv 2605.01749, May 2026) achieves up to 13% factuality gain via training-based calibration-aware generation. LoVeC (arXiv 2505.23912, May 2025) uses RL to train LLMs to append on-the-fly confidence scores per statement in long-form generation, achieving 20× speedup over self-consistency methods. All three require base model fine-tuning or RL.\n\n**Post-generation claim-level approaches:** CSS (arXiv 2604.17487, April 2026) decomposes answers into claims and backs off uncertain ones using external verifiers. Selective Abstraction (arXiv 2602.11908, February 2026) replaces low-confidence atoms with confident abstractions.\n\n**Residual-stream anomaly detection:** PCNET (arXiv 2605.05953, May 2026) uses probabilistic circuits on residual streams for hallucination detection + contrastive decoding, reaching up to 99% AUROC — but targets short-form QA and changes content (different token selection) rather than expressing calibrated uncertainty.\n\n**Scaling concerns for activation steering:** Scaling laws for activation steering (ICML 2025) show that CAA effectiveness diminishes with model size on Llama 2 (7B→13B→70B) for behavioral steering (refusal). Endogenous steering resistance (arXiv 2602.06941, February 2026) shows Llama-3.3-70B has 3.8% ESR rate (vs <1% for smaller models). However, CLAS demonstrates successful probe-derived steering on Llama-3.1-70B, suggesting that adaptive, probe-guided steering may be more robust at scale than uniform CAA.\n\n**Gap:** No existing work combines claim-level factuality probing (à la Han et al.) with calibrated activation steering along the verbalized-confidence direction (à la Miao & Ungar) in a single-pass, online framework for long-form generation. This intersection — reading internal accuracy per-claim and steering verbalized confidence to match during generation — is the contribution space. Additionally, no work has tested whether the accuracy-confidence orthogonality discovered at 7–8B scale holds at 70B or in long-form generation contexts, making this verification itself a contribution to the mechanistic understanding of confidence representations.",
  "approach": "We propose Read-and-Steer (RaS), a single-pass framework for claim-level calibrated uncertainty expression in long-form generation. The system reads internal accuracy signals per-claim via lightweight probes and steers verbalized confidence to match via targeted activation intervention, producing naturally hedged language for uncertain claims while leaving confident-and-correct claims untouched.\n\n**Pilot Experiment — Orthogonality Verification at Scale (~8h, 2× H100, first week):** Before committing the full experimental budget, we replicate Miao & Ungar's orthogonality analysis on Llama 3.1-70B in a long-form generation setting. We extract accuracy and confidence directions from biography-generation hidden states (not QA), measure their cosine similarity, and compare against the < 0.04 value found at 7–8B scale. This pilot has three outcomes: (a) orthogonality holds (cosine < 0.1) — proceed as planned, report the scaling result as a contribution; (b) orthogonality partially holds (cosine 0.1–0.3) — adapt steering to project out the accuracy component from the confidence direction before steering, proceed with modified approach; (c) orthogonality fails (cosine > 0.3) — report as an important negative finding about the limits of linear feature geometry at scale, fall back to the 8B-only configuration. All three outcomes produce publishable results.\n\n**Offline Stage 1 — Factuality Probe Training (~12h wall, 2× H100 for 70B; ~4h, 1× H100 for 8B; one-time per model):** Generate long-form outputs (biographies, factual descriptions) from the target model, decompose into atomic claims using FActScore/OpenFActScore decomposition, verify claim factuality against knowledge sources. Extract hidden states at each claim's token span across multiple layers (following Han et al.'s layer-group methodology). Train lightweight linear probes (logistic regression on span-aggregated hidden states) to predict continuous factuality confidence scores. Unlike Han et al.'s binary factuality labels, we train on soft labels derived from verification confidence, enabling graded uncertainty estimation.\n\n**Offline Stage 2 — Verbalized-Confidence Direction Extraction (~5h wall, 2× H100 for 70B; ~2h, 1× H100 for 8B; one-time per model):** Extract a verbalized-confidence steering direction via contrastive activation pairs: generate matched claim pairs where the same factual content is expressed with high confidence ('X was born in Y') vs. hedged uncertainty ('X was reportedly born in Y, though I am not certain'). The mean activation difference yields the steering direction, following the contrastive methodology from Ji et al. (VUF) and Miao & Ungar (CAA). For the 70B model, if the pilot reveals partial orthogonality degradation, we apply Gram-Schmidt orthogonalization to project the confidence direction away from the accuracy direction before use.\n\n**Online Stage — Probe-Guided Steering During Generation:** During autoregressive generation: (1) At each generated token, run the factuality probe on its hidden states — this is a single matrix-vector multiplication with negligible overhead. (2) Maintain a running mean probe score over the current sentence span using a sliding window. (3) At sentence boundaries (detected from generated punctuation — periods, newlines — which are trivially available during generation), evaluate the accumulated probe score against a calibrated threshold. (4) If the probe indicates internal uncertainty (score below threshold) while the generation shows no hedging markers, apply a steering offset along the extracted verbalized-confidence direction on subsequent tokens, with steering magnitude α proportional to the miscalibration gap: α = β × max(0, threshold − probe_score), where β is calibrated on a held-out validation set. This adaptive formula is conceptually related to CLAS's context-dependent steering, but driven by per-claim factuality probe scores rather than general input-context sensing vectors. (5) Deactivate steering when the probe score recovers above threshold.\n\n**Key design choices addressing known limitations:** (a) Span-aggregated probe scores over the full claim token range avoid the single-token prefix-contamination problem — the signal reflects the entire claim, not just the cumulative prefix. (b) Single-pass online monitoring eliminates the two-pass chicken-and-egg problem identified for the original CL-MUC approach — no position-aligned regeneration needed. (c) Continuous calibrated steering (not binary neuron clamping) produces graded hedging proportional to internal uncertainty, distinguishing this from Han et al.'s binary intervention. (d) Operating on the verbalized-confidence direction (orthogonal to accuracy per Miao & Ungar, verified at 70B scale in our pilot) means steering affects expression style without corrupting the model's factual knowledge. (e) Adaptive steering magnitude based on probe-detected need may mitigate the diminishing effectiveness of uniform CAA at larger scales (ICML 2025 scaling laws), since steering is only applied where needed and at probe-calibrated intensity.\n\n**Models:** Llama 3.1-70B-Instruct as primary (standard dense transformer architecture, well-studied for probing and steering, large enough to test scaling of the orthogonality finding, with CLAS confirming probe-derived steering viability at this scale). Llama 3.1-8B-Instruct as validation (enables direct comparison with Miao & Ungar and Ji et al. baselines on the same model family, validates the pipeline in well-charted territory before scaling). Both models use standard transformer attention across all layers, avoiding the untested territory of hybrid DeltaNet architectures (e.g., Qwen 3.5) where linear probe and steering techniques lack validation.\n\n**Benchmarks:** FActScore (biography generation, primary) and LongFact (diverse long-form factuality). Metrics: claim-level ECE, Brier score (calibration quality), AUROC (uncertainty detection), FActScore/factual precision (to verify steering does not degrade content quality), and MT-Bench fluency subset (to verify generation quality preservation). We also report the cosine similarity between accuracy and confidence directions at 70B scale as a standalone mechanistic finding.\n\n**Quantitative targets:** We expect RaS to achieve: (1) claim-level ECE reduction of ≥40% relative to unsteered baselines on both FActScore and LongFact; (2) FActScore preservation within 2% of unsteered baseline (steering affects verbal expression, not factual content); (3) uncertainty detection AUROC ≥0.80 (probe-based); (4) superior calibration (lower ECE) compared to Han et al.'s binary neuron clamping at comparable or better FActScore. These targets are informed by Miao & Ungar's response-level results (ECE reductions of 70–90% on QA), discounted for the harder claim-level long-form setting.\n\n**Comparisons:** (1) Unsteered baseline, (2) Han et al.'s probes + neuron clamping (closest representation-based method for long-form), (3) CURE (closest training-based method, if reproducible), (4) LoVeC (RL-based long-form verbalized confidence, if reproducible), (5) Ablations: probe-only detection without steering, uniform steering without probe guidance, VUF-only steering (Ji et al.'s original method applied per-claim), CORAL-style MLP probes vs. linear probes, varying layers for probe extraction, steering strength sensitivity, CLAS-style sensing vector vs. probe-score-driven adaptation.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "~250h H100 80GB (orthogonality pilot ~8h [2×H100], probe training + direction extraction ~34h [20h 70B on 2×H100, 6h 8B], Llama 3.1-70B generation + evaluation on FActScore + LongFact ~100h [2×H100], Llama 3.1-8B validation ~25h, baseline comparisons ~45h, ablations ~38h)",
      "gpu_utilization": "~20-30% effective — GPU idles during code development, pipeline debugging, and results analysis",
      "timeline": "5-7 weeks (1 researcher full-time)",
      "team": "1-2 researchers with mechanistic interpretability and activation steering experience",
      "estimated_gpu_cost": "$625-875 (at ~$2.50-3.50/hr H100 80GB spot)"
    },
    "human_in_loop": {
      "gpu_hours": "~200h H100 80GB (agent handles pipeline code, probe training iteration, evaluation scripting; human approves pilot results, probe design, steering threshold calibration, and ablation priorities)",
      "gpu_utilization": "~45-60% — agent queues experiments between human check-ins",
      "timeline": "3-4 weeks",
      "team": "1 researcher, ~30min/day for methodology decisions, pilot outcome assessment, and qualitative hedging evaluation",
      "claude_api_cost": "$100-200 (~1500-3000 Opus turns)",
      "estimated_gpu_cost": "$500-700",
      "risk_note": "Primary risk: whether accuracy-confidence orthogonality holds at 70B scale in long-form generation — the ~8h pilot experiment validates this before committing the full budget. If orthogonality breaks (outcome c), we fall back to an 8B-only paper with the negative scaling result as a contribution, reducing total compute to ~80h H100. Secondary risk: whether probe-guided steering produces natural hedging at 70B or degrades fluency — qualitative human assessment is essential. Tertiary risk: CAA effectiveness diminishing at 70B scale (per ICML 2025 scaling laws), though our adaptive probe-guided approach may be more robust than uniform steering."
    },
    "auto_research": {
      "gpu_hours": "~280h H100 80GB (agent explores probe architectures, layer selections, steering schedules across both models, plus comprehensive evaluation)",
      "gpu_utilization": "~80-90% — continuous experiment pipeline with minimal idle",
      "timeline": "7-10 days with 2× H100 80GB",
      "team": "0 researchers (initial setup + final review only)",
      "claude_api_cost": "$200-400 (~3000-6000 Opus turns)",
      "estimated_gpu_cost": "$700-980",
      "speed_bottleneck": "Long-form generation throughput on Llama 3.1-70B with 2× H100 tensor parallelism (~20-30 tok/s) — generating and evaluating hundreds of long-form responses per configuration is the computational bottleneck",
      "risk_note": "Without human judgment, agent may over-optimize probe thresholds on validation set rather than ensuring robustness, may miss qualitative assessment of hedging naturalness, and critically may not correctly interpret the orthogonality pilot results (the decision to proceed vs. pivot requires understanding of the mechanistic implications)"
    }
  },
  "target_venues": [
    "AAAI 2027 (abstract Jul 21, full paper Jul 28, 2026 — ~10 weeks; conference Feb 16-23, Montréal) — PRIMARY",
    "ARR August 2026 (submission Aug 3, 2026 — ~11 weeks; committable to EMNLP 2026 Oct 24-29 or later *ACL venues)",
    "ICLR 2027 (expected submission ~Oct 2026, ~20 weeks; comfortable timeline)"
  ],
  "level": "solid",
  "key_references": [
    "Simple Factuality Probes Detect Hallucinations in Long-Form Natural Language Generation (Han et al., Findings of EMNLP 2025) — closest prior work: claim-level probes + neuron clamping in long-form generation",
    "Closing the Confidence-Faithfulness Gap in LLMs (Miao & Ungar, arXiv 2603.25052, March 2026) — accuracy-confidence orthogonality discovery + adaptive CAA steering; explicitly notes scaling and long-form extension as open questions",
    "Correctness-Optimized Residual Activation Lens [CORAL] (Miao, Cho & Ungar, arXiv 2602.06022, February 2026) — same group; MLP probes → correctness steering on MCQA at 7B scale; must differentiate as response-level, short-form only",
    "Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations (Ji et al., EMNLP 2025) — VUF discovery and MUC for response-level short-form QA",
    "Inference-Time Intervention: Eliciting Truthful Answers from a Language Model [ITI] (Li et al., NeurIPS 2023) — foundational probe→steer paradigm using linear probes on attention heads for truthfulness",
    "Enhancing Language Model Factuality via Activation-Based Confidence Calibration and Guided Decoding [ActCab/CoDec] (EMNLP 2024) — activation calibration + confidence-guided decoding for QA factuality",
    "Contextual Linear Activation Steering [CLAS] (Hsu et al., arXiv 2604.24693, April 2026) — probe-derived adaptive steering with context-dependent strength; tested on Llama-3.1-70B, confirming steering viability at 70B scale",
    "How do LLMs Compute Verbal Confidence? (Kumaran et al., arXiv 2603.17839, March 2026) — mechanistic evidence for cached confidence retrieval at answer-adjacent positions",
    "Reinforcement Learning for Better Verbalized Confidence in Long-Form Generation [LoVeC] (arXiv 2505.23912, May 2025) — RL-based on-the-fly confidence scoring per statement in long-form generation; training-based",
    "Scaling Laws for Activation Steering with Llama 2 Models and Refusal Mechanisms (ICML 2025) — demonstrates CAA effectiveness diminishes with model size (7B→70B); informs our adaptive steering design",
    "Endogenous Resistance to Activation Steering in Language Models (arXiv 2602.06941, February 2026) — Llama-3.3-70B shows 3.8% endogenous steering resistance; relevant scaling concern",
    "Does Transformer Interpretability Transfer to RNNs? (2024) — probing and CAA partially transfer to recurrent architectures with reduced effectiveness; motivates our choice of standard transformer models",
    "SteerConf: Steering LLMs for Confidence Elicitation (Zhou et al., NeurIPS 2025) — prompt-based training-free confidence calibration",
    "Adaptive Activation Steering: A Tuning-Free LLM Truthfulness Improvement Method (ACT, WWW 2025) — diverse steering vectors with adaptive intensity control",
    "Real-Time Detection of Hallucinated Entities in Long-Form Generation (Obeso et al., arXiv 2509.03531, 2025) — entity-level streaming probes for long-form generation",
    "Hallucination as an Anomaly: Dynamic Intervention via Probabilistic Circuits [PCNET] (arXiv 2605.05953, May 2026) — residual stream anomaly detection + contrastive decoding intervention",
    "Streaming Hallucination Detection in Long Chain-of-Thought Reasoning (arXiv 2601.02170, January 2026) — online hallucination detection as evolving latent state",
    "Think Through Uncertainty: Improving Long-Form Generation Factuality via Reasoning Calibration [CURE] (arXiv 2604.12046, April 2026) — multi-stage training for claim-level confidence reasoning",
    "Only Say What You Know: Calibration-Aware Generation for Long-Form Factuality [CAG] (arXiv 2605.01749, May 2026) — training-based calibration-aware generation",
    "Atomic Calibration of LLMs in Long-Form Generations (Findings of AACL-IJCNLP 2025) — showed poor claim-level calibration in long-form outputs",
    "Answer Only as Precisely as Justified: Calibrated Claim-Level Specificity Control [CSS] (arXiv 2604.17487, April 2026) — post-generation specificity control via external verifiers",
    "When Should LLMs Be Less Specific? Selective Abstraction for Reliable Long-Form Text Generation (arXiv 2602.11908, February 2026)",
    "Semantic Entropy Probes: Robust and Cheap Hallucination Detection in LLMs (ICML 2024) — linear probes approximate semantic entropy at response level",
    "FActScore: Fine-grained Atomic Evaluation of Factual Precision in Long Form Text Generation (EMNLP 2023)",
    "Long-form Factuality in Large Language Models [LongFact/SAFE] (NeurIPS 2024)",
    "Steering Language Models With Activation Engineering (Turner et al., arXiv 2308.10248, 2023)"
  ],
  "description": "We propose Read-and-Steer (RaS), a single-pass framework for claim-level calibrated uncertainty expression in long-form generation. Motivated by two key findings — Han et al. (EMNLP 2025) showed lightweight probes detect claim-level factuality in long-form hidden states, and Miao & Ungar (2026) discovered that internal accuracy and verbalized confidence are nearly orthogonal linear features — RaS combines both insights in a novel way: it reads claim-level accuracy signals via factuality probes during autoregressive generation and steers verbalized confidence to match via targeted activation intervention along the orthogonal confidence direction, all within a single forward pass. Unlike Han et al.'s neuron clamping (binary suppression of hallucinations), RaS produces calibrated verbal hedging proportional to the model's internal uncertainty. Unlike CURE, CAG, and LoVeC, it requires no base model training — only lightweight linear probe fitting and contrastive direction extraction. The probe-guided adaptive steering formula (α = β × max(0, threshold − probe_score)) relates to CLAS's context-dependent steering but is driven by per-claim factuality signals rather than general context sensing, and targets confidence expression rather than content correctness (as in ITI, CORAL, and ActCab/CoDec). The framework includes a dedicated pilot experiment verifying the accuracy-confidence orthogonality at 70B scale in long-form generation — extending Miao & Ungar's finding beyond the 7–8B QA setting where it was established. We evaluate on Llama 3.1-70B (primary, testing scaling) and Llama 3.1-8B (validation, direct comparison with prior work) using FActScore and LongFact, measuring claim-level ECE, Brier score, AUROC, and factual precision. We expect ≥40% claim-level ECE reduction over unsteered baselines while preserving FActScore within 2%. Both models use standard transformer architectures, avoiding the untested hybrid DeltaNet territory (e.g., Qwen 3.5) where linear probing and activation steering techniques lack validation. All experiments fit within ~250 H100-hours.",
  "project_name": "probe_guided_claim_calibration",
  "source": "web_research"
}


## Previous review history
### Round 1 review
Verdict: revise
Issues: ["CRITICAL MISSING COMPETITOR: Han et al. 'Simple Factuality Probes Detect Hallucinations in Long-Form Natural Language Generation' (EMNLP Findings 2025) — same Oxford group as Semantic Entropy Probes — already does claim-level hidden-state probing + neuron clamping for causal hallucination reduction in long-form generation. This is the closest existing work and was completely missed.", "MISSING COMPETITOR: Miao & Ungar 'Closing the Confidence-Faithfulness Gap in LLMs' (arXiv 2603.25052, March 2026) uses CAA steering for confidence calibration, finding calibration and verbalized confidence are orthogonal linear features. Their two-stage adaptive steering pipeline is closely related.", "MISSING WORK: 'How do LLMs Compute Verbal Confidence?' (arXiv 2603.17839, March 2026) provides mechanistic analysis of verbal confidence computation; SteerConf (NeurIPS 2025) does training-free steering for confidence calibration; Adaptive Activation Steering (ACT, WWW 2025) does tuning-free diverse steering vectors for truthfulness; 'Real-Time Detection of Hallucinated Entities' (Obeso et al., 2025) does entity-level probes in long-form. None cited.", "VUF was validated ONLY on 7-8B dense models (Llama3.1-8B, Mistral-7B, Qwen2.5-7B). The paper itself notes Qwen2.5 shows 'significantly less sensitivity' to VUF steering. Transfer to Qwen3.5-27B is unverified, and transfer to Llama 4 Scout (109B MoE, 16 experts) is extremely unlikely to work cleanly — MoE architectures route different tokens through different experts, making linear feature identification fundamentally harder.", "Two-pass generation has a chicken-and-egg problem: pass 1 identifies claims and their token positions; steering in pass 2 changes the generation, so claims will appear at different positions or be entirely different. The approach assumes regeneration reproduces the same claims in the same positions, which activation steering specifically disrupts.", "Resource estimate (300h A100 manual, 200h A100 HIL, 500h auto) exceeds the user's hard constraint of ≤200 H100-hours total. Even the HIL estimate at 200h A100 ≈ 130-150h H100 equivalent is optimistic given the need for two-pass generation across multiple benchmarks with 27B+ models.", "Semantic Entropy Probes were designed for response-level uncertainty approximation. Adapting them to claim-level semantic uncertainty in long-form contexts requires new training data and potentially different probe architectures — this is not a trivial adaptation and the '~30h' SEP training estimate is likely too low.", "The 'claim's final token position' VUF projection assumes clean per-claim signals, but in autoregressive generation, hidden states at position i are conditioned on ALL preceding tokens. The VUF signal at a claim's last token reflects the entire prefix, not just that claim — extraction may not give meaningful per-claim uncertainty."]
Feedback: The idea has a clear and appealing structure, but faces critical novelty and feasibility problems that must be addressed:

**Novelty — differentiate from Han et al. (2025):** This is the single most important fix. Han et al. already showed that simple linear probes on hidden states detect hallucinations at claim level in long-form generation AND that neuron clamping causally reduces hallucinations. You MUST: (1) cite this paper prominently as the closest prior work, (2) articulate what VUF+SEP dual-signal scoring adds over simple factuality probes (e.g., better calibration vs. binary factuality, verbal hedging rather than deletion/clamping), (3) run head-to-head comparisons. Also cite Miao & Ungar (2026) on CAA steering for calibration.

**Feasibility — drop Llama 4 Scout, fix the two-pass problem:**
- Replace Llama 4 Scout with a dense model (Llama 3.1-70B, Qwen2.5-72B, or stick with Qwen3.5-27B only). MoE models are too risky for VUF extraction in 11 days.
- Rethink the two-pass approach: consider single-pass with streaming claim detection (detect uncertainty signals during generation and intervene in real-time using a sliding window), or adopt a post-hoc rewriting/hedging approach that doesn't require position-aligned regeneration.
- Reduce scope to 1 model with ablations rather than 2 models × 4 benchmarks.

**Compute — stay within budget:**
- The ≤200 H100-hour constraint means roughly 1 model, 2-3 benchmarks max with focused experiments.
- Drop extensive ablation sweeps in favor of one clean comparison: CL-MUC vs. Han et al.'s probes vs. CURE/CAG.

**Technical — address the claim-level VUF signal problem:**
- Provide evidence or pilot results that VUF projection at claim-final tokens gives meaningful per-claim uncertainty, or pivot to a different extraction strategy (e.g., aggregate VUF across all tokens in a claim span).

### Round 2 review
Verdict: revise
Issues: ["CRITICAL — Qwen3.5-27B architecture mismatch: Qwen3.5-27B uses a hybrid Gated DeltaNet + attention architecture (3:1 ratio). 75% of layers are DeltaNet (linear attention), fundamentally different from standard transformer attention. Linear probes, contrastive activation directions, and steering techniques were developed and validated ONLY on standard transformer architectures. TransformerLens does not support DeltaNet layers. The proposal claims Qwen3.5-27B is 'confirmed viable for activation steering' — this is false and unverified. The entire primary experimental setup may fail on day 1.", "CRITICAL — Unverified scaling assumption: Miao & Ungar's accuracy-confidence orthogonality (cosine similarity < 0.04) was demonstrated ONLY on 7-8B standard transformers (Llama-3.1-8B, Mistral-7B, Qwen2.5-7B) on short-form QA. They explicitly state: 'Whether the linear encoding findings hold at larger scales remains open. Evaluation is restricted to question-answering tasks; extending to open-ended generation would require rethinking how the probe target is constructed.' RaS critically depends on this orthogonality holding at 27B scale in long-form generation — this is an assumption, not a validated property.", "MISSING COMPETITOR — CORAL (arXiv 2602.06022, Feb 2026): From the SAME Miao & Ungar group. Trains MLP probes on residual stream activations to predict correctness, then steers model behavior at inference time — essentially the same probe→steer pipeline concept. Evaluates on MCQA with 7B models. Must be cited and differentiated as same-group prior work.", "MISSING COMPETITOR — CLAS (arXiv 2604.24693, April 2026): Contextual Linear Activation Steering uses probe-derived steering vectors with dynamic, context-dependent strength. RaS's α = β × max(0, threshold − probe_score) is conceptually similar to CLAS's adaptive steering strength. Must be cited.", "MISSING COMPETITOR — ITI (NeurIPS 2023, Li et al.): Inference-Time Intervention — the foundational work that uses linear probes to identify truthful directions in attention heads and steers during generation. The probe→steer-during-generation paradigm originates here. Not cited.", "MISSING COMPETITOR — ActCab/CoDec (EMNLP 2024): Trains a linear layer on LM last-layer activations for confidence calibration, then uses confidence-guided decoding to elicit truthful answers. Same conceptual pipeline (activation-based calibration → guided generation). Not cited.", "Timeline risk: EMNLP 2026 ARR deadline is May 25, 2026 — 10 days away. With the DeltaNet architecture risk likely requiring a pivot to Llama 3.1-8B only (reducing the paper to a direct comparison with Miao & Ungar on the same 8B model), this is not enough time to produce competitive results. AAAI 2027 (July 28) is more realistic.", "Qwen2.5 sensitivity acknowledged but not addressed: Miao & Ungar note that Qwen2.5-7B shows 'significantly less sensitivity' to VUF steering compared to Llama and Mistral. If Qwen models are inherently less responsive to this type of steering, the Qwen3.5-27B results may be disappointing even if the architecture challenge is resolved."]
Feedback: The core idea — combining Han et al.'s claim-level probes with Miao & Ungar's calibrated confidence steering in single-pass long-form generation — addresses a genuine gap. But there are critical issues that must be resolved:

**1. Replace Qwen3.5-27B as primary model (HIGHEST PRIORITY):**
Qwen3.5-27B's hybrid DeltaNet architecture (75% linear attention layers) is untested territory for linear probes and activation steering. All prior work validated these techniques on standard transformer architectures. Options:
- **Best option**: Use Llama 3.1-70B (standard transformer, well-studied, large enough to be compelling) as primary, with Llama 3.1-8B as validation for direct comparison to Miao & Ungar. This requires ~2× the compute of 8B but fits within 200 H100-hours if you drop Qwen entirely.
- **Alternative**: Use Qwen2.5-32B (standard transformer architecture, unlike Qwen3.5). But note Qwen2.5 shows reduced sensitivity to confidence steering per Miao & Ungar.
- **Risky fallback**: Keep Qwen3.5-27B but acknowledge it as an architectural exploration, not 'confirmed viable.' Run a 5h pilot on DeltaNet-layer probing before committing.

**2. Cite all missing competitors and sharpen differentiation:**
Add CORAL (same group as Miao & Ungar — probe→steer on MCQA), CLAS (dynamic steering strength from probes), ITI (foundational probe→steer work, NeurIPS 2023), and ActCab/CoDec (activation calibration + guided decoding, EMNLP 2024). Your differentiation should be: all prior probe→steer work operates at response level on short-form QA; RaS is the first to operate at claim level during long-form generation with calibrated (not binary) confidence expression.

**3. Address the orthogonality scaling gap explicitly:**
Don't claim orthogonality transfers — frame it as a hypothesis to test. Add a dedicated experiment: replicate Miao & Ungar's orthogonality analysis on your primary model (measuring cosine similarity between accuracy and confidence directions at 27B+ scale on long-form generation). This is both a contribution (extending the finding to new settings) and a risk-mitigation step.

**4. Target AAAI 2027 (July 28) instead of EMNLP (May 25):**
10 days is too tight for a paper with this many unvalidated assumptions. AAAI gives 10+ weeks, which allows: 1-week pilot on architecture/orthogonality, 3-week implementation, 2-week evaluation, 4-week writing. Still ambitious but feasible.

**5. Strengthen the impact argument:**
The crowded landscape (CURE, CAG, CSS, PCNET, LoVeC, Rewarding Doubt) means you need clear quantitative expectations. State upfront: 'We expect RaS to achieve claim-level ECE below X (vs. Y for unsteered and Z for binary clamping) while maintaining FActScore above W.' Without specific targets, the paper risks being 'we tried the obvious combination and it kind of worked.'


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
  "promptId": "d0af2fce-b877-4a83-b1a2-3e65f7ded303",
  "type": "user",
  "uuid": "507d5900-80ca-4123-a082-283f0e66f8a4",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-15T14:10:13.173Z_

```json
{
  "parentUuid": "507d5900-80ca-4123-a082-283f0e66f8a4",
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
  "uuid": "672a3d86-3aac-4d33-9f38-aca21030fde0",
  "timestamp": "2026-05-15T14:10:13.173Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-15T14:10:13.174Z_

```json
{
  "parentUuid": "672a3d86-3aac-4d33-9f38-aca21030fde0",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "de817de6-839a-43a5-855a-4fb17e850efd",
  "timestamp": "2026-05-15T14:10:13.174Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19",
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
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-15 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "de817de6-839a-43a5-855a-4fb17e850efd",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Claim-level confidence calibration for long-form LLM generation",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19"
}
```

---

### Assistant

_source line 8 · 2026-05-15T14:10:18.641Z_

<details><summary>Logged reasoning block</summary>

```text
Let me carefully review this idea - "Read and Steer (RaS): Probe-Guided Claim-Level Confidence Calibration for Long-Form Generation" - now in its third round of revision. I need to independently verify the claims, check for missing competitors, assess feasibility, and determine if the revisions adequately addressed prior review concerns.

Let me start by searching for the key papers and competitors mentioned, and look for any additional work that might have been missed.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "de817de6-839a-43a5-855a-4fb17e850efd",
  "isSidechain": false,
  "requestId": "req_011Cb4VHG16uMbDADVBqj1Hd",
  "type": "assistant",
  "uuid": "35fefc0f-83cc-41f4-a4a1-64a57f77f7ac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PZczvW5E8uagjeQzsi3wRw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 19707,
      "cache_read_input_tokens": 11841,
      "output_tokens": 886,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19707,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 886,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 19707,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19707
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

_source line 9 · 2026-05-15T14:10:19.117Z_

I'll conduct a thorough independent review of this revised idea. Let me start by verifying key claims and searching for competitors across multiple dimensions.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "35fefc0f-83cc-41f4-a4a1-64a57f77f7ac",
  "isSidechain": false,
  "requestId": "req_011Cb4VHG16uMbDADVBqj1Hd",
  "type": "assistant",
  "uuid": "1d8949c2-67c2-4f12-98fd-eaa72045f239",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PZczvW5E8uagjeQzsi3wRw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 19707,
      "cache_read_input_tokens": 11841,
      "output_tokens": 886,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19707,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 886,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 19707,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19707
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

_source line 10 · 2026-05-15T14:10:32.988Z_

<details open><summary>🔧 Tool call — Agent · `toolu_017EZRcMX3Pzpebckn13fDka`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Verify key papers and orthogonality claims",
  "prompt": "You are helping me verify claims in a machine learning paper proposal. I need you to search for and verify the following papers and their claims. For each, use WebSearch and WebFetch to find the actual paper and confirm the claims.\n\n1. **Han et al. \"Simple Factuality Probes Detect Hallucinations in Long-Form Natural Language Generation\" (EMNLP Findings 2025)** — Claimed: lightweight linear probes on hidden states detect claim-level hallucinations in long-form generation, matching multi-sample methods at 100× fewer FLOPs. Also claimed: \"neuron clamping\" causally reduces hallucinations. Verify this paper exists, confirm these claims, and check what models they tested on.\n\n2. **Miao & Ungar \"Closing the Confidence-Faithfulness Gap in LLMs\" (arXiv 2603.25052, March 2026)** — Claimed: accuracy and verbalized confidence are nearly orthogonal linear features (cosine similarity < 0.04), adaptive CAA steering achieves ECE 14.9→3.7 on Llama-3.1-8B and 35.1→3.3 on Mistral-7B. Also claimed they explicitly note scaling and long-form extension as open questions. Verify existence and claims.\n\n3. **CORAL (Miao, Cho & Ungar, arXiv 2602.06022, February 2026)** — Claimed: MLP probes on residual activations, correctness steering on MCQA at 7B scale, response-level only. Verify existence.\n\n4. **CLAS (Hsu et al., arXiv 2604.24693, April 2026)** — Claimed: context-dependent linear activation steering, tested on Llama-3.1-70B across 11 benchmarks. Verify existence and whether it really works at 70B scale.\n\n5. **Scaling Laws for Activation Steering (ICML 2025)** — Claimed: CAA effectiveness diminishes with model size (7B→13B→70B) for behavioral steering. Verify.\n\n6. **Endogenous Resistance to Activation Steering (arXiv 2602.06941, Feb 2026)** — Claimed: Llama-3.3-70B has 3.8% ESR rate. Verify.\n\nFor each paper, report: (a) whether it exists, (b) whether the specific claims are accurate, (c) any important details the proposal might have missed or misrepresented. Use WebSearch with queries like \"site:arxiv.org\" or direct paper title searches. Try to fetch at least the abstracts of the most critical papers (#1, #2, #4)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1d8949c2-67c2-4f12-98fd-eaa72045f239",
  "isSidechain": false,
  "requestId": "req_011Cb4VHG16uMbDADVBqj1Hd",
  "type": "assistant",
  "uuid": "5ac96ffd-82cf-4ba9-8aa6-cca5462d231c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PZczvW5E8uagjeQzsi3wRw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 19707,
      "cache_read_input_tokens": 11841,
      "output_tokens": 886,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19707,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 886,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 19707,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19707
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

_source line 11 · 2026-05-15T14:16:02.424Z_

<details><summary>↩ Tool result · `toolu_017EZRcMX3Pzpebckn13fDka`</summary>

```text
Now I have all the information needed. Let me compile the comprehensive verification report.

---

Here is the verification report for all six papers:

---

## Paper 1: Han et al. "Simple Factuality Probes Detect Hallucinations in Long-Form Natural Language Generation" (EMNLP Findings 2025)

**(a) Existence: CONFIRMED.** Published as Findings of EMNLP 2025, pages 16209-16226. Available at [ACL Anthology](https://aclanthology.org/2025.findings-emnlp.880/). Authors: Jiatong Han, Neil Band, Muhammed Razzak, Jannik Kossen, Tim G. J. Rudner, and Yarin Gal.

**(b) Claims verification:**

- **Lightweight linear probes on hidden states detect claim-level hallucinations:** PARTIALLY CONFIRMED. The paper does use lightweight probes on hidden states for hallucination detection. The abstract states: "LLM hidden states are highly predictive of factuality in long-form natural language generation and...this information can be efficiently extracted at inference time using a lightweight probe." The term "claim-level" is used in secondary sources describing the paper but was not explicitly prominent in the abstract itself -- the paper does operate on factual claims within long-form text, so calling it "claim-level" appears reasonable.

- **Matching multi-sample methods at 100x fewer FLOPs:** CONFIRMED. The abstract explicitly states: "our approach achieves competitive performance with up to 100x fewer FLOPs."

- **"Neuron clamping" causally reduces hallucinations:** CONFIRMED. Multiple sources indicate the paper includes a neuron clamping analysis where neuron activations are clamped to the tail range of their "supported" class activation values, causally reducing hallucinations. This is described in the body of the paper (Table 6), not in the abstract.

- **Models tested:** The abstract says "open-weight models up to 405B parameters." The 405B figure strongly suggests Llama-3.1-405B was included, but I could not extract the complete list of model names from the abstract alone.

**(c) Potential issues for proposal:** The proposal's characterization appears accurate. The main caveat is that the 405B models were used for evaluation/benchmarking -- the probes themselves are trained on and generalize from smaller models' hidden states.

---

## Paper 2: Miao & Ungar "Closing the Confidence-Faithfulness Gap in LLMs" (arXiv 2603.25052, March 2026)

**(a) Existence: CONFIRMED.** Available at [arXiv:2603.25052](https://arxiv.org/abs/2603.25052). Authors: Miranda Muqing Miao, Lyle Ungar (University of Pennsylvania). Submitted March 26, 2026.

**(b) Claims verification:**

- **Accuracy and verbalized confidence are nearly orthogonal linear features (cosine similarity < 0.04):** CONFIRMED. The paper states the "cosine similarity between the two ridge probe weight vectors (pure verbal vs. gold calibration)" remains "below 0.04 across all layers" (Figure 3(c)).

- **Adaptive CAA steering achieves ECE 14.9 -> 3.7 on Llama-3.1-8B and 35.1 -> 3.3 on Mistral-7B:** CONFIRMED. Table 4 shows exactly these numbers. Additionally, Qwen2.5-7B-Inst. goes from 36.0 -> 10.7 (a result the proposal omits).

- **Explicitly note scaling and long-form extension as open questions:** CONFIRMED. The Limitations section explicitly states: (1) "Our experiments use 7-8B parameter models, and whether the linear encoding and orthogonality findings hold at larger scales...remains open." (2) "Our evaluation is restricted to question-answering tasks with verifiable answers, extending to open-ended generation would require rethinking how the probe target is constructed."

- **Three models tested:** Llama-3.1-8B, Mistral-7B-v0.3, and Qwen2.5-7B (both base and instruction-tuned variants). Four datasets used.

**(c) Potential issues for proposal:** The paper does NOT use the exact term "adaptive CAA steering" -- it describes a "two-stage adaptive steering pipeline" that uses CAA. The proposal should also note that the Qwen2.5-7B result (36.0 -> 10.7) is notably weaker than the other two models, suggesting the method's effectiveness varies. The paper also identifies a novel "Reasoning Contamination Effect" where reasoning disrupts verbalized confidence -- this is a significant finding the proposal may want to acknowledge. Also, the paper explicitly notes the limitation of requiring a separate generation pass for confidence assessment.

---

## Paper 3: CORAL (Miao, Cho & Ungar, arXiv 2602.06022, February 2026)

**(a) Existence: CONFIRMED.** Full title: "Correctness-Optimized Residual Activation Lens (CORAL): Transferrable and Calibration-Aware Inference-Time Steering." Available at [arXiv:2602.06022](https://arxiv.org/abs/2602.06022). Authors: Miranda Muqing Miao, Young-Min Cho, Lyle Ungar. Submitted February 5, 2026.

**(b) Claims verification:**

- **MLP probes on residual activations:** CONFIRMED. The paper uses "weight-decay MLP probes" on model internal activations.

- **Correctness steering on MCQA at 7B scale:** CONFIRMED. Evaluated "across three 7B-parameter models," improving accuracy by 10% and ECE by 50% on average. Transfers to four held-out benchmarks (ARC-Challenge, HellaSwag, Math-MC, OpenBookQA) with 14% accuracy and 49% ECE improvements.

- **Response-level only:** CONFIRMED. The abstract explicitly says it improves "MCQA performance during inference" -- there is no mention of claim-level or token-level granularity.

**(c) Potential issues for proposal:** The characterization appears accurate. The proposal could note that CORAL's transfer results are a significant strength -- gains generalize without retraining to held-out benchmarks.

---

## Paper 4: CLAS (Hsu et al., arXiv 2604.24693, April 2026)

**(a) Existence: CONFIRMED.** Full title: "Contextual Linear Activation Steering of Language Models." Available at [arXiv:2604.24693](https://arxiv.org/abs/2604.24693). Authors: Brandon Hsu, Daniel Beaglehole, Adityanarayanan Radhakrishnan, Mikhail Belkin (UC San Diego, MIT, Broad Institute). GitHub implementation available at [bhdsc/CLAS](https://github.com/bhdsc/CLAS).

**(b) Claims verification:**

- **Context-dependent linear activation steering:** CONFIRMED. The method "dynamically adapts linear activation steering to context-dependent steering strengths."

- **Tested on Llama-3.1-70B:** CONFIRMED. The four model families tested are Qwen2.5-7B, Llama-3.1-8B, Llama-3.1-70B, and Llama-3.2-1B. Llama-3.1-70B achieved an average accuracy of 88.40% across 10 tasks.

- **11 benchmarks:** CONFIRMED. The benchmarks are: Alpaca, Grandiloquent, GSM8K, IMDb, JailbreakBench, LeetCode, MMLU, MNMT, Repetition, TLDR, ToxicChat.

- **Works at 70B scale:** CONFIRMED. Results explicitly include Llama-3.1-70B.

**(c) Potential issues for proposal:** The proposal's characterization appears accurate. Note that CLAS also tests at 1B scale (Llama-3.2-1B), showing breadth across scales. The method "matches or exceeds the performance of ReFT and LoRA in settings with limited labeled data," which is a strong competitive claim. The proposal calling this "context-dependent" is accurate -- the paper's key innovation is adapting steering strength per-token based on context rather than using a fixed strength.

---

## Paper 5: "Scaling Laws for Activation Steering" (ICML 2025)

**(a) Existence: CONFIRMED.** Full title: "Scaling laws for activation steering with Llama 2 models and refusal mechanisms." Published at ICML 2025. Available at [arXiv:2507.11771](https://arxiv.org/abs/2507.11771). Authors: Sheikh Abdur Raheem Ali, Justin Xu, Ivory Yang, Jasmine Xinze Li, Ayse Arslan, Clark Benham.

**(b) Claims verification:**

- **CAA effectiveness diminishes with model size (7B -> 13B -> 70B):** CONFIRMED. The paper explicitly finds "the effectiveness of CAA diminishes with model size," explaining that larger models "drown out" the steering vector due to more downstream computation.

- **For behavioral steering:** CONFIRMED but note: the paper specifically studies refusal behavior using Llama 2 models (7B, 13B, 70B), not generic "behavioral steering." It uses contrastive pairs (e.g., hate to love) and focuses on refusal mechanisms.

**(c) Potential issues for proposal:** The proposal should note this paper uses **Llama 2** models specifically, not Llama 3 or other families. The finding about diminishing effectiveness is specific to these models and refusal-type behavioral steering -- it may not generalize to all steering tasks or architectures. The paper also finds that negative steering has more pronounced effects than positive steering, and that early-mid layers are most effective, which are additional nuances.

---

## Paper 6: "Endogenous Resistance to Activation Steering" (arXiv 2602.06941, Feb 2026)

**(a) Existence: CONFIRMED.** Available at [arXiv:2602.06941](https://arxiv.org/abs/2602.06941). Authors: Alex McKenzie, Keenan Pepper, Stijn Servaes, Martin Leitgab, Murat Cubuktepe, Mike Vaiana, Diogo de Lucena, Judd Rosenblatt, Michael S. A. Graziano.

**(b) Claims verification:**

- **Llama-3.3-70B has 3.8% ESR rate:** CONFIRMED. The paper states exactly: "Llama-3.3-70B shows an ESR rate of 3.8%, substantially higher than all other models tested (all below 1%)."

- **Additional details:** Multi-attempt rate for Llama-3.3-70B is 7.4% (vs. <=1.2% for others). Improvement rate when attempting correction is 83% at optimal boost levels. Smaller models (Llama-3.1-8B, Gemma-2-27B/9B/2B) all show ESR below 1%.

**(c) Potential issues for proposal:** The paper identifies 26 SAE latents causally linked to ESR in Llama-3.3-70B, and zero-ablating these latents reduced multi-attempt rates by 25%. ESR can be enhanced through prompting (4x increase) and fine-tuning, which has implications for both adversarial protection and safety intervention interference. This dual-use nature (ESR could either help or hurt alignment efforts) is worth noting.

---

## Summary

All six papers **exist and are real**. The specific numerical claims in the proposal are **largely accurate**. Key corrections and caveats:

1. **Paper #1 (Han et al.):** "Neuron clamping" is confirmed but is a secondary contribution, not the main focus. The paper is primarily about detection probes. Models go up to 405B.
2. **Paper #2 (Miao & Ungar):** All numbers confirmed exactly. The proposal omits the weaker Qwen2.5 result and the "Reasoning Contamination Effect." The long-form limitation is explicitly stated but the paper says "open-ended generation" rather than "long-form."
3. **Paper #3 (CORAL):** Accurately described as MCQA-only, 7B-scale, response-level.
4. **Paper #4 (CLAS):** Confirmed at 70B scale across 11 benchmarks. Also tests 1B and 7-8B scales.
5. **Paper #5 (Scaling Laws):** Confirmed, but uses **Llama 2** models and focuses on **refusal** steering specifically.
6. **Paper #6 (ESR):** 3.8% ESR rate confirmed exactly.

Sources:
- [Han et al. EMNLP Findings 2025](https://aclanthology.org/2025.findings-emnlp.880/)
- [Miao & Ungar arXiv:2603.25052](https://arxiv.org/abs/2603.25052)
- [CORAL arXiv:2602.06022](https://arxiv.org/abs/2602.06022)
- [CLAS arXiv:2604.24693](https://arxiv.org/abs/2604.24693)
- [Scaling Laws arXiv:2507.11771](https://arxiv.org/abs/2507.11771)
- [ESR arXiv:2602.06941](https://arxiv.org/abs/2602.06941)
- [CLAS GitHub Repository](https://github.com/bhdsc/CLAS)
- [ICML 2025 Virtual Page](https://icml.cc/virtual/2025/50642)

agentId: a871c0eb886219af8 (use SendMessage with to: 'a871c0eb886219af8' to continue this agent)
&lt;usage>total_tokens: 31152
tool_uses: 26
duration_ms: 329429&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5ac96ffd-82cf-4ba9-8aa6-cca5462d231c",
  "isSidechain": false,
  "promptId": "d0af2fce-b877-4a83-b1a2-3e65f7ded303",
  "type": "user",
  "uuid": "238b1140-a1db-41d5-8745-d311821aef1e",
  "toolUseResult": {
    "status": "completed",
    "prompt": "You are helping me verify claims in a machine learning paper proposal. I need you to search for and verify the following papers and their claims. For each, use WebSearch and WebFetch to find the actual paper and confirm the claims.\n\n1. **Han et al. \"Simple Factuality Probes Detect Hallucinations in Long-Form Natural Language Generation\" (EMNLP Findings 2025)** — Claimed: lightweight linear probes on hidden states detect claim-level hallucinations in long-form generation, matching multi-sample methods at 100× fewer FLOPs. Also claimed: \"neuron clamping\" causally reduces hallucinations. Verify this paper exists, confirm these claims, and check what models they tested on.\n\n2. **Miao & Ungar \"Closing the Confidence-Faithfulness Gap in LLMs\" (arXiv 2603.25052, March 2026)** — Claimed: accuracy and verbalized confidence are nearly orthogonal linear features (cosine similarity < 0.04), adaptive CAA steering achieves ECE 14.9→3.7 on Llama-3.1-8B and 35.1→3.3 on Mistral-7B. Also claimed they explicitly note scaling and long-form extension as open questions. Verify existence and claims.\n\n3. **CORAL (Miao, Cho & Ungar, arXiv 2602.06022, February 2026)** — Claimed: MLP probes on residual activations, correctness steering on MCQA at 7B scale, response-level only. Verify existence.\n\n4. **CLAS (Hsu et al., arXiv 2604.24693, April 2026)** — Claimed: context-dependent linear activation steering, tested on Llama-3.1-70B across 11 benchmarks. Verify existence and whether it really works at 70B scale.\n\n5. **Scaling Laws for Activation Steering (ICML 2025)** — Claimed: CAA effectiveness diminishes with model size (7B→13B→70B) for behavioral steering. Verify.\n\n6. **Endogenous Resistance to Activation Steering (arXiv 2602.06941, Feb 2026)** — Claimed: Llama-3.3-70B has 3.8% ESR rate. Verify.\n\nFor each paper, report: (a) whether it exists, (b) whether the specific claims are accurate, (c) any important details the proposal might have missed or misrepresented. Use WebSearch with queries like \"site:arxiv.org\" or direct paper title searches. Try to fetch at least the abstracts of the most critical papers (#1, #2, #4).",
    "agentId": "a871c0eb886219af8",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have all the information needed. Let me compile the comprehensive verification report.\n\n---\n\nHere is the verification report for all six papers:\n\n---\n\n## Paper 1: Han et al. \"Simple Factuality Probes Detect Hallucinations in Long-Form Natural Language Generation\" (EMNLP Findings 2025)\n\n**(a) Existence: CONFIRMED.** Published as Findings of EMNLP 2025, pages 16209-16226. Available at [ACL Anthology](https://aclanthology.org/2025.findings-emnlp.880/). Authors: Jiatong Han, Neil Band, Muhammed Razzak, Jannik Kossen, Tim G. J. Rudner, and Yarin Gal.\n\n**(b) Claims verification:**\n\n- **Lightweight linear probes on hidden states detect claim-level hallucinations:** PARTIALLY CONFIRMED. The paper does use lightweight probes on hidden states for hallucination detection. The abstract states: \"LLM hidden states are highly predictive of factuality in long-form natural language generation and...this information can be efficiently extracted at inference time using a lightweight probe.\" The term \"claim-level\" is used in secondary sources describing the paper but was not explicitly prominent in the abstract itself -- the paper does operate on factual claims within long-form text, so calling it \"claim-level\" appears reasonable.\n\n- **Matching multi-sample methods at 100x fewer FLOPs:** CONFIRMED. The abstract explicitly states: \"our approach achieves competitive performance with up to 100x fewer FLOPs.\"\n\n- **\"Neuron clamping\" causally reduces hallucinations:** CONFIRMED. Multiple sources indicate the paper includes a neuron clamping analysis where neuron activations are clamped to the tail range of their \"supported\" class activation values, causally reducing hallucinations. This is described in the body of the paper (Table 6), not in the abstract.\n\n- **Models tested:** The abstract says \"open-weight models up to 405B parameters.\" The 405B figure strongly suggests Llama-3.1-405B was included, but I could not extract the complete list of model names from the abstract alone.\n\n**(c) Potential issues for proposal:** The proposal's characterization appears accurate. The main caveat is that the 405B models were used for evaluation/benchmarking -- the probes themselves are trained on and generalize from smaller models' hidden states.\n\n---\n\n## Paper 2: Miao & Ungar \"Closing the Confidence-Faithfulness Gap in LLMs\" (arXiv 2603.25052, March 2026)\n\n**(a) Existence: CONFIRMED.** Available at [arXiv:2603.25052](https://arxiv.org/abs/2603.25052). Authors: Miranda Muqing Miao, Lyle Ungar (University of Pennsylvania). Submitted March 26, 2026.\n\n**(b) Claims verification:**\n\n- **Accuracy and verbalized confidence are nearly orthogonal linear features (cosine similarity < 0.04):** CONFIRMED. The paper states the \"cosine similarity between the two ridge probe weight vectors (pure verbal vs. gold calibration)\" remains \"below 0.04 across all layers\" (Figure 3(c)).\n\n- **Adaptive CAA steering achieves ECE 14.9 -> 3.7 on Llama-3.1-8B and 35.1 -> 3.3 on Mistral-7B:** CONFIRMED. Table 4 shows exactly these numbers. Additionally, Qwen2.5-7B-Inst. goes from 36.0 -> 10.7 (a result the proposal omits).\n\n- **Explicitly note scaling and long-form extension as open questions:** CONFIRMED. The Limitations section explicitly states: (1) \"Our experiments use 7-8B parameter models, and whether the linear encoding and orthogonality findings hold at larger scales...remains open.\" (2) \"Our evaluation is restricted to question-answering tasks with verifiable answers, extending to open-ended generation would require rethinking how the probe target is constructed.\"\n\n- **Three models tested:** Llama-3.1-8B, Mistral-7B-v0.3, and Qwen2.5-7B (both base and instruction-tuned variants). Four datasets used.\n\n**(c) Potential issues for proposal:** The paper does NOT use the exact term \"adaptive CAA steering\" -- it describes a \"two-stage adaptive steering pipeline\" that uses CAA. The proposal should also note that the Qwen2.5-7B result (36.0 -> 10.7) is notably weaker than the other two models, suggesting the method's effectiveness varies. The paper also identifies a novel \"Reasoning Contamination Effect\" where reasoning disrupts verbalized confidence -- this is a significant finding the proposal may want to acknowledge. Also, the paper explicitly notes the limitation of requiring a separate generation pass for confidence assessment.\n\n---\n\n## Paper 3: CORAL (Miao, Cho & Ungar, arXiv 2602.06022, February 2026)\n\n**(a) Existence: CONFIRMED.** Full title: \"Correctness-Optimized Residual Activation Lens (CORAL): Transferrable and Calibration-Aware Inference-Time Steering.\" Available at [arXiv:2602.06022](https://arxiv.org/abs/2602.06022). Authors: Miranda Muqing Miao, Young-Min Cho, Lyle Ungar. Submitted February 5, 2026.\n\n**(b) Claims verification:**\n\n- **MLP probes on residual activations:** CONFIRMED. The paper uses \"weight-decay MLP probes\" on model internal activations.\n\n- **Correctness steering on MCQA at 7B scale:** CONFIRMED. Evaluated \"across three 7B-parameter models,\" improving accuracy by 10% and ECE by 50% on average. Transfers to four held-out benchmarks (ARC-Challenge, HellaSwag, Math-MC, OpenBookQA) with 14% accuracy and 49% ECE improvements.\n\n- **Response-level only:** CONFIRMED. The abstract explicitly says it improves \"MCQA performance during inference\" -- there is no mention of claim-level or token-level granularity.\n\n**(c) Potential issues for proposal:** The characterization appears accurate. The proposal could note that CORAL's transfer results are a significant strength -- gains generalize without retraining to held-out benchmarks.\n\n---\n\n## Paper 4: CLAS (Hsu et al., arXiv 2604.24693, April 2026)\n\n**(a) Existence: CONFIRMED.** Full title: \"Contextual Linear Activation Steering of Language Models.\" Available at [arXiv:2604.24693](https://arxiv.org/abs/2604.24693). Authors: Brandon Hsu, Daniel Beaglehole, Adityanarayanan Radhakrishnan, Mikhail Belkin (UC San Diego, MIT, Broad Institute). GitHub implementation available at [bhdsc/CLAS](https://github.com/bhdsc/CLAS).\n\n**(b) Claims verification:**\n\n- **Context-dependent linear activation steering:** CONFIRMED. The method \"dynamically adapts linear activation steering to context-dependent steering strengths.\"\n\n- **Tested on Llama-3.1-70B:** CONFIRMED. The four model families tested are Qwen2.5-7B, Llama-3.1-8B, Llama-3.1-70B, and Llama-3.2-1B. Llama-3.1-70B achieved an average accuracy of 88.40% across 10 tasks.\n\n- **11 benchmarks:** CONFIRMED. The benchmarks are: Alpaca, Grandiloquent, GSM8K, IMDb, JailbreakBench, LeetCode, MMLU, MNMT, Repetition, TLDR, ToxicChat.\n\n- **Works at 70B scale:** CONFIRMED. Results explicitly include Llama-3.1-70B.\n\n**(c) Potential issues for proposal:** The proposal's characterization appears accurate. Note that CLAS also tests at 1B scale (Llama-3.2-1B), showing breadth across scales. The method \"matches or exceeds the performance of ReFT and LoRA in settings with limited labeled data,\" which is a strong competitive claim. The proposal calling this \"context-dependent\" is accurate -- the paper's key innovation is adapting steering strength per-token based on context rather than using a fixed strength.\n\n---\n\n## Paper 5: \"Scaling Laws for Activation Steering\" (ICML 2025)\n\n**(a) Existence: CONFIRMED.** Full title: \"Scaling laws for activation steering with Llama 2 models and refusal mechanisms.\" Published at ICML 2025. Available at [arXiv:2507.11771](https://arxiv.org/abs/2507.11771). Authors: Sheikh Abdur Raheem Ali, Justin Xu, Ivory Yang, Jasmine Xinze Li, Ayse Arslan, Clark Benham.\n\n**(b) Claims verification:**\n\n- **CAA effectiveness diminishes with model size (7B -> 13B -> 70B):** CONFIRMED. The paper explicitly finds \"the effectiveness of CAA diminishes with model size,\" explaining that larger models \"drown out\" the steering vector due to more downstream computation.\n\n- **For behavioral steering:** CONFIRMED but note: the paper specifically studies refusal behavior using Llama 2 models (7B, 13B, 70B), not generic \"behavioral steering.\" It uses contrastive pairs (e.g., hate to love) and focuses on refusal mechanisms.\n\n**(c) Potential issues for proposal:** The proposal should note this paper uses **Llama 2** models specifically, not Llama 3 or other families. The finding about diminishing effectiveness is specific to these models and refusal-type behavioral steering -- it may not generalize to all steering tasks or architectures. The paper also finds that negative steering has more pronounced effects than positive steering, and that early-mid layers are most effective, which are additional nuances.\n\n---\n\n## Paper 6: \"Endogenous Resistance to Activation Steering\" (arXiv 2602.06941, Feb 2026)\n\n**(a) Existence: CONFIRMED.** Available at [arXiv:2602.06941](https://arxiv.org/abs/2602.06941). Authors: Alex McKenzie, Keenan Pepper, Stijn Servaes, Martin Leitgab, Murat Cubuktepe, Mike Vaiana, Diogo de Lucena, Judd Rosenblatt, Michael S. A. Graziano.\n\n**(b) Claims verification:**\n\n- **Llama-3.3-70B has 3.8% ESR rate:** CONFIRMED. The paper states exactly: \"Llama-3.3-70B shows an ESR rate of 3.8%, substantially higher than all other models tested (all below 1%).\"\n\n- **Additional details:** Multi-attempt rate for Llama-3.3-70B is 7.4% (vs. <=1.2% for others). Improvement rate when attempting correction is 83% at optimal boost levels. Smaller models (Llama-3.1-8B, Gemma-2-27B/9B/2B) all show ESR below 1%.\n\n**(c) Potential issues for proposal:** The paper identifies 26 SAE latents causally linked to ESR in Llama-3.3-70B, and zero-ablating these latents reduced multi-attempt rates by 25%. ESR can be enhanced through prompting (4x increase) and fine-tuning, which has implications for both adversarial protection and safety intervention interference. This dual-use nature (ESR could either help or hurt alignment efforts) is worth noting.\n\n---\n\n## Summary\n\nAll six papers **exist and are real**. The specific numerical claims in the proposal are **largely accurate**. Key corrections and caveats:\n\n1. **Paper #1 (Han et al.):** \"Neuron clamping\" is confirmed but is a secondary contribution, not the main focus. The paper is primarily about detection probes. Models go up to 405B.\n2. **Paper #2 (Miao & Ungar):** All numbers confirmed exactly. The proposal omits the weaker Qwen2.5 result and the \"Reasoning Contamination Effect.\" The long-form limitation is explicitly stated but the paper says \"open-ended generation\" rather than \"long-form.\"\n3. **Paper #3 (CORAL):** Accurately described as MCQA-only, 7B-scale, response-level.\n4. **Paper #4 (CLAS):** Confirmed at 70B scale across 11 benchmarks. Also tests 1B and 7-8B scales.\n5. **Paper #5 (Scaling Laws):** Confirmed, but uses **Llama 2** models and focuses on **refusal** steering specifically.\n6. **Paper #6 (ESR):** 3.8% ESR rate confirmed exactly.\n\nSources:\n- [Han et al. EMNLP Findings 2025](https://aclanthology.org/2025.findings-emnlp.880/)\n- [Miao & Ungar arXiv:2603.25052](https://arxiv.org/abs/2603.25052)\n- [CORAL arXiv:2602.06022](https://arxiv.org/abs/2602.06022)\n- [CLAS arXiv:2604.24693](https://arxiv.org/abs/2604.24693)\n- [Scaling Laws arXiv:2507.11771](https://arxiv.org/abs/2507.11771)\n- [ESR arXiv:2602.06941](https://arxiv.org/abs/2602.06941)\n- [CLAS GitHub Repository](https://github.com/bhdsc/CLAS)\n- [ICML 2025 Virtual Page](https://icml.cc/virtual/2025/50642)"
      }
    ],
    "totalDurationMs": 329429,
    "totalTokens": 31152,
    "totalToolUseCount": 26,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 462,
      "cache_read_input_tokens": 27315,
      "output_tokens": 3374,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 462
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3374,
          "cache_read_input_tokens": 27315,
          "cache_creation_input_tokens": 462,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 462,
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
      "otherToolCount": 26
    }
  },
  "sourceToolAssistantUUID": "5ac96ffd-82cf-4ba9-8aa6-cca5462d231c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-15 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "238b1140-a1db-41d5-8745-d311821aef1e",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Claim-level confidence calibration for long-form LLM generation",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19"
}
```

---

### Assistant

_source line 14 · 2026-05-15T14:16:05.467Z_

Good — all six key papers verified. Now let me search for missing competitors and concurrent work that the proposal might have overlooked.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "238b1140-a1db-41d5-8745-d311821aef1e",
  "isSidechain": false,
  "requestId": "req_011Cb4Vj11gFmfpHMJUG5kk5",
  "type": "assistant",
  "uuid": "33feac60-48b2-43e6-886f-932dc5e6c9b6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N64WvjnkJSFUFbeDAe2jPy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4336,
      "cache_read_input_tokens": 31548,
      "output_tokens": 744,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4336,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 744,
          "cache_read_input_tokens": 31548,
          "cache_creation_input_tokens": 4336,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4336
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

_source line 15 · 2026-05-15T14:16:20.186Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01XkzBWXSeo5wXVpAfYmVcjr`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Search for missing competitors and concurrent work",
  "prompt": "You are helping me review an ML paper proposal about \"probe-guided claim-level confidence calibration for long-form generation.\" The idea combines claim-level factuality probes with activation steering to calibrate verbalized confidence during long-form text generation. I need you to search for MISSING competitors or concurrent work that the proposal may have overlooked.\n\nThe proposal already cites: Han et al. (EMNLP 2025), Miao & Ungar (2026), CORAL (2026), CLAS (2026), ITI (NeurIPS 2023), ActCab/CoDec (EMNLP 2024), CURE (2026), CAG (2026), LoVeC (2025), PCNET (2026), SteerConf (NeurIPS 2025), ACT (WWW 2025), CSS (2026), Selective Abstraction (2026), Kumaran et al. (2026), Obeso et al. (2025), Scaling Laws for Activation Steering (ICML 2025), ESR (2026).\n\nPlease search for work the proposal may have MISSED using the following queries (use WebSearch):\n\n1. \"claim-level calibration long-form generation 2025 2026\" — any claim-level calibration work for long-form text\n2. \"activation steering confidence calibration 2026\" — concurrent steering-for-calibration work  \n3. \"probe guided decoding hallucination 2026\" — probe-guided generation approaches\n4. \"verbalized uncertainty long-form 2025 2026\" — verbalized uncertainty in long-form settings\n5. \"inference time intervention hallucination reduction 2026\" — ITI-style approaches for hallucinations\n6. \"linear probes hallucination detection steering 2026\" — probe+steering combinations\n7. \"site:arxiv.org claim level uncertainty calibration LLM 2026\" — arxiv-specific search\n8. \"faithfulness calibration generation ACL EMNLP 2026\" — venue-specific recent work\n9. \"activation engineering confidence LLM 2025 2026\" — activation engineering for confidence\n10. \"Rewarding Doubt hallucination 2026\" OR \"self-aware generation LLM 2026\" — alternative approaches\n\nFor each search, report: (a) the query used, (b) any papers found that are NOT in the cited list above, (c) how relevant they are to the proposal (high/medium/low), and (d) whether they threaten the novelty claim.\n\nFocus especially on papers from January-May 2026 that might be concurrent work. If you find something highly relevant, use WebFetch to read more details."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "33feac60-48b2-43e6-886f-932dc5e6c9b6",
  "isSidechain": false,
  "requestId": "req_011Cb4Vj11gFmfpHMJUG5kk5",
  "type": "assistant",
  "uuid": "64d38cd0-3f08-4896-ac2f-fa0adfef4faf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N64WvjnkJSFUFbeDAe2jPy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4336,
      "cache_read_input_tokens": 31548,
      "output_tokens": 744,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4336,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 744,
          "cache_read_input_tokens": 31548,
          "cache_creation_input_tokens": 4336,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4336
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

_source line 16 · 2026-05-15T14:20:31.643Z_

<details><summary>↩ Tool result · `toolu_01XkzBWXSeo5wXVpAfYmVcjr`</summary>

```text
Now I have comprehensive results. Let me compile the final report.

---

Here is a systematic analysis of potentially missing competitors and concurrent work, organized by search query. I focus on papers **not already cited** in the proposal.

---

## QUERY 1: "claim-level calibration long-form generation 2025 2026"

### Papers Found (NOT in cited list):

**1. "Atomic Calibration of LLMs in Long-Form Generations"** -- Zhang et al., Findings of IJCNLP-AACL 2025 ([arXiv:2410.13246](https://arxiv.org/abs/2410.13246))
- Systematically studies atomic (claim-level) calibration by decomposing long responses into atomic claims. Categorizes confidence elicitation methods into discriminative vs. generative types and proposes confidence fusion strategies.
- **Relevance: HIGH.** This is a direct predecessor to the proposal's claim-level approach. It provides the empirical foundation showing LLMs are poorly calibrated at the atomic level in long-form generation.
- **Novelty threat: MEDIUM.** It diagnoses the problem your proposal solves but does not use probes or activation steering as a remedy.

**2. CARE: "Fact-Level Calibration and Correction for Long-Form Generations"** -- Yuan et al., SIGIR 2025 ([ACM](https://dl.acm.org/doi/10.1145/3726302.3730195))
- Proposes a fact-level confidence calibration framework incorporating both relevance and correctness, plus CARE (Confidence-Aware Fact Correction) that uses high-confidence facts to iteratively refine low-confidence ones.
- **Relevance: HIGH.** Operates at the same granularity (fact/claim-level) in long-form generation with calibration + correction.
- **Novelty threat: MEDIUM.** Uses iterative correction rather than activation steering, so the mechanism differs, but the problem formulation overlaps substantially.

**3. "Only Say What You Know: Calibration-Aware Generation for Long-Form Factuality" (CAG)** -- Luo et al., May 2026 ([arXiv:2605.01749](https://arxiv.org/abs/2605.01749))
- Proposes "Exploration-Commitment Decoupling" separating knowledge exploration from final output commitment, with calibrated reliability estimates. Up to 13% factuality improvement.
- **Relevance: HIGH.** Note: The proposal already cites "CAG (2026)" -- verify this is the same paper. If so, no issue.
- **Novelty threat: LOW if already cited.**

**4. "Conformal Linguistic Calibration: Trading-off between Factuality and Specificity"** -- Jiang et al., Feb 2025 ([arXiv:2502.19110](https://arxiv.org/abs/2502.19110))
- Reinterprets linguistic calibration as answer set prediction with conformal guarantees. Enables uncertainty-aware adaptive claim rewriting.
- **Relevance: MEDIUM-HIGH.** Addresses calibration at the claim level via semantic "backoff" rather than abstention.
- **Novelty threat: LOW.** Different mechanism (conformal prediction / linguistic hedging) vs. activation steering.

---

## QUERY 2: "activation steering confidence calibration 2026"

### Papers Found (NOT in cited list):

**5. "Spherical Steering: Geometry-Aware Activation Rotation for Language Models"** -- You et al., Feb 2026 ([arXiv:2602.08169](https://arxiv.org/abs/2602.08169))
- Proposes rotation-based (rather than addition-based) steering using spherical linear interpolation, with adaptive von Mises-Fisher confidence gating. Up to +15% accuracy.
- **Relevance: MEDIUM-HIGH.** Directly relevant as a better steering mechanism that could be applied to confidence calibration. The confidence-gated aspect is particularly relevant.
- **Novelty threat: MEDIUM.** If someone combines Spherical Steering with factuality probes, it subsumes part of the proposal's contribution.

**6. ODESteer: "A Unified ODE-Based Steering Framework for LLM Alignment"** -- Zhao et al., ICLR 2026 ([arXiv:2602.17560](https://arxiv.org/abs/2602.17560))
- Interprets activation addition as first-order approximation of an ODE; uses barrier functions from control theory for multi-step adaptive steering. +5.7% on TruthfulQA.
- **Relevance: MEDIUM.** General steering framework that could be applied to confidence/factuality steering. Provides theoretical grounding.
- **Novelty threat: LOW-MEDIUM.** Different theoretical framework but potentially applicable to the proposal's setting.

**7. AUSteer: "Fine-Grained Activation Steering: Steering Less, Achieving More"** -- ICLR 2026 ([arXiv:2602.04428](https://arxiv.org/abs/2602.04428))
- Decomposes block activations into atomic units, selects discriminative ones via activation momenta, applies adaptive per-input steering strengths.
- **Relevance: MEDIUM.** Fine-grained steering method that could be combined with probe-guided approaches. Relevant as a baseline/alternative steering mechanism.
- **Novelty threat: LOW-MEDIUM.** Different target (general alignment, not confidence calibration specifically).

**8. "Steering Vector Fields for Context-Aware Inference-Time Control in LLMs"** -- Li et al., Feb 2026 ([arXiv:2602.01654](https://arxiv.org/abs/2602.01654))
- Learns a differentiable concept scoring function whose gradient defines context-dependent steering direction (rather than a fixed vector). Supports multi-layer coordinated intervention.
- **Relevance: MEDIUM.** Addresses the limitation that static steering vectors fail in long-form generation -- directly relevant to the proposal's setting.
- **Novelty threat: LOW-MEDIUM.** General steering methodology, not specifically applied to confidence calibration.

**9. FLAS: "Beyond Steering Vector: Flow-based Activation Steering for Inference-Time Intervention"** -- Jin et al., May 2026 ([arXiv:2605.05892](https://arxiv.org/abs/2605.05892))
- Learns concept-conditioned velocity field for multi-step, token-varying activation transformations. First learned method to consistently surpass prompting baselines.
- **Relevance: MEDIUM.** Another advanced steering mechanism that supersedes static vector approaches.
- **Novelty threat: LOW.** General framework, not applied to confidence.

---

## QUERY 3: "probe guided decoding hallucination 2026"

### Papers Found (NOT in cited list):

**10. "A Single Direction of Truth: An Observer Model's Linear Residual Probe Exposes and Steers Contextual Hallucinations"** -- O'Neill et al., July 2025 ([arXiv:2507.23221](https://arxiv.org/abs/2507.23221))
- **THIS IS THE MOST IMPORTANT FIND.** Uses a linear probe on an observer model's residual stream to detect hallucinations (>0.95 F1), then uses the probe weight vector as a steering vector injected into a generator to reduce/amplify hallucination prevalence.
- **Relevance: VERY HIGH.** This is extremely close to the proposal's approach -- it combines linear probes with activation steering for hallucination control. The key difference is it uses an external observer model and targets contextual hallucination, while the proposal targets confidence calibration.
- **Novelty threat: HIGH.** The core probe-to-steering pipeline is very similar. The proposal must differentiate clearly (e.g., claim-level granularity, confidence calibration vs. binary hallucination, self-probing vs. observer model).

**11. HaloProbe: "Bayesian Detection and Mitigation of Object Hallucinations in Vision-Language Models"** -- Zohrabi et al., April 2026 ([arXiv:2604.06165](https://arxiv.org/abs/2604.06165))
- Bayesian framework combining external description statistics with internal decoding signals for token-level hallucination probability estimation, used for guided decoding.
- **Relevance: MEDIUM.** Probe-guided decoding for hallucination mitigation, but in the vision-language setting.
- **Novelty threat: LOW.** Different modality (VLMs) and approach (Bayesian, not linear probe + steering).

**12. "Neural Probe-Based Hallucination Detection for Large Language Models"** -- Liang & Wang, Dec 2025 ([arXiv:2512.20949](https://arxiv.org/abs/2512.20949))
- Uses lightweight MLP probes (not just linear) with Bayesian-optimized layer selection and multi-objective loss for token-level hallucination detection.
- **Relevance: MEDIUM.** Probe-based detection, but detection-only (no steering or calibration component).
- **Novelty threat: LOW.** Detection only, no intervention.

**13. HALP: "Detecting Hallucinations in Vision-Language Models without Generating a Single Token"** -- EACL 2026 ([arXiv:2603.05465](https://arxiv.org/abs/2603.05465))
- Probes internal representations pre-generation to predict hallucination risk (up to 0.93 AUROC), enabling early abstention or adaptive decoding.
- **Relevance: MEDIUM.** Pre-generation probing for hallucination detection, though in VLMs.
- **Novelty threat: LOW.** Different modality and no steering mechanism.

---

## QUERY 4: "verbalized uncertainty long-form 2025 2026"

### Papers Found (NOT in cited list):

**14. "LLMs Should Express Uncertainty Explicitly"** -- Guo et al., April 2026 ([arXiv:2604.05306](https://arxiv.org/abs/2604.05306))
- Compares end-of-reasoning self-assessment (confidence scores) with during-reasoning `&lt;uncertain>` markers. Finds both reduce overconfident errors and improve RAG integration.
- **Relevance: MEDIUM-HIGH.** Directly addresses verbalized uncertainty with mechanistic insights (changes concentrate in later layers, sharpening existing structures).
- **Novelty threat: LOW.** Training-based approach without probes or steering.

**15. CSFT: "Verbalized Confidence Triggers Self-Verification: Emergent Behavior Without Explicit Reasoning Supervision"** -- 2026 ([OpenReview](https://openreview.net/forum?id=P2o8wOzZMX))
- Confidence-supervised fine-tuning triggers emergent self-verification (from <1.5% to ~20% rates) without explicit reasoning supervision.
- **Relevance: MEDIUM.** Shows that confidence training alone can elicit sophisticated calibration behavior.
- **Novelty threat: LOW.** SFT-based, not inference-time intervention.

**16. DINCO: "Calibrating Verbalized Confidence with Self-Generated Distractors"** -- Wang et al., 2025 ([arXiv:2509.25532](https://arxiv.org/abs/2509.25532))
- Normalizes verbalized confidence across self-generated distractors to correct for suggestibility bias. DINCO at 10 runs outperforms self-consistency at 100.
- **Relevance: MEDIUM.** Alternative calibration approach for verbalized confidence.
- **Novelty threat: LOW.** Purely sampling-based, orthogonal to probe+steering approach.

---

## QUERY 5: "inference time intervention hallucination reduction 2026"

### Papers Found (NOT in cited list):

**17. AFTER: "Mitigating the Object Hallucination of LVLM via Adaptive Factual-Guided Activation Editing"** -- Wang et al., ICLR 2026 ([arXiv:2601.01957](https://arxiv.org/abs/2601.01957))
- Combines Factual-Augmented Activation Steering (FAS) with Query-Adaptive Offset Optimization (QAO) for input-specific steering from a general factual steering vector. Up to 16.3% hallucination reduction.
- **Relevance: MEDIUM-HIGH.** Adaptive, query-aware steering for factuality -- conceptually related to probe-guided steering for confidence.
- **Novelty threat: MEDIUM.** Different domain (VLMs), but the adaptive factual-guided steering mechanism has significant conceptual overlap.

---

## QUERY 6: "linear probes hallucination detection steering 2026"

**Key finding already covered above (#10, "A Single Direction of Truth").** Also:

**18. "Simple Factuality Probes Detect Hallucinations in Long-Form Natural Language Generation"** -- Han et al., Findings of EMNLP 2025 ([ACL Anthology](https://aclanthology.org/2025.findings-emnlp.880/))
- LLM hidden states are highly predictive of factuality; lightweight probes achieve competitive performance with up to 100x fewer FLOPs.
- **Relevance: HIGH.** Note: The proposal already cites "Han et al. (EMNLP 2025)" -- likely this paper. Confirm.
- **Novelty threat: N/A if cited.**

---

## QUERY 7: "site:arxiv.org claim level uncertainty calibration LLM 2026"

### Papers Found (NOT in cited list):

**19. CoCA: "Confidence Before Answering: A Paradigm Shift for Efficient LLM Uncertainty Estimation"** -- Li et al., March 2026 ([arXiv:2603.05881](https://arxiv.org/abs/2603.05881))
- GRPO-based RL that jointly optimizes confidence calibration and answer accuracy via confidence-first generation with segmented credit assignment.
- **Relevance: MEDIUM-HIGH.** Addresses confidence calibration through RL training rather than inference-time intervention.
- **Novelty threat: LOW.** Different mechanism (RL training vs. probe+steering).

**20. DCPO: "Decoupling Reasoning and Confidence: Resurrecting Calibration in Reinforcement Learning from Verifiable Rewards"** -- Ma et al., March 2026 ([arXiv:2603.09117](https://arxiv.org/abs/2603.09117))
- Identifies that RLVR training makes models overconfident on incorrect answers; proposes decoupling reasoning and calibration objectives.
- **Relevance: MEDIUM.** Addresses the overconfidence problem through training rather than inference-time.
- **Novelty threat: LOW.** Complementary approach.

**21. "Calibrating LLM Judges: Linear Probes for Fast and Reliable Uncertainty Estimation"** -- Dec 2025 ([arXiv:2512.22245](https://arxiv.org/abs/2512.22245))
- Uses linear probes on LLM-as-judge hidden states for uncertainty estimation.
- **Relevance: MEDIUM.** Probes for calibration, but in the LLM-as-judge setting.
- **Novelty threat: LOW.** Different application context.

---

## QUERY 8: "faithfulness calibration generation ACL EMNLP 2026"

### Papers Found (NOT in cited list):

**22. CSS: "Answer Only as Precisely as Justified: Calibrated Claim-Level Specificity Control for Agentic Systems"** -- Huang et al., April 2026 ([arXiv:2604.17487](https://arxiv.org/abs/2604.17487))
- Decomposes answers into claims, uses Clopper-Pearson confidence bounds for calibrated specificity selection (fine-grained, coarse, or omit). Improves utility from 0.846 to 0.913 on LongFact.
- **Relevance: HIGH.** Note: The proposal already cites "CSS (2026)" -- likely this paper. Confirm it is the same.
- **Novelty threat: N/A if cited.**

---

## QUERY 9: "activation engineering confidence LLM 2025 2026"

### Papers Found (NOT in cited list):

**23. CAST: "Programming Refusal with Conditional Activation Steering"** -- IBM, ICLR 2025 (Spotlight) ([arXiv:2409.05907](https://arxiv.org/abs/2409.05907))
- Conditional steering that applies behavior vectors only when activation patterns match a condition vector. Adds controllability without extra compute.
- **Relevance: MEDIUM.** The conditional application mechanism (steer only when condition is met) is relevant -- analogous to "steer only when probe detects low confidence."
- **Novelty threat: LOW-MEDIUM.** General mechanism, but the conditional steering paradigm is conceptually close.

---

## QUERY 10: "Rewarding Doubt hallucination 2026" / "self-aware generation LLM 2026"

### Papers Found (NOT in cited list):

**24. "Mitigating LLM Hallucination via Behaviorally Calibrated Reinforcement Learning"** -- Wu et al., Dec 2025/Jan 2026 ([arXiv:2512.19920](https://arxiv.org/abs/2512.19920))
- Uses behavioral calibration in RL with strictly proper scoring rules so models learn to abstain when not confident. A 4B model matches frontier models in calibration error.
- **Relevance: MEDIUM.** RL-based approach to calibrated uncertainty expression.
- **Novelty threat: LOW.** Training-based, not inference-time.

---

## SUMMARY OF MOST CRITICAL MISSING CITATIONS

Ranked by urgency:

| Priority | Paper | Why It Matters |
|----------|-------|---------------|
| **CRITICAL** | "A Single Direction of Truth" (O'Neill et al., 2025) | **Combines linear probes with activation steering for hallucination control** -- the closest existing work to the proposal's core mechanism |
| **HIGH** | "Atomic Calibration of LLMs in Long-Form Generations" (Zhang et al., IJCNLP 2025) | Foundational work on claim-level calibration in long-form generation |
| **HIGH** | CARE / "Fact-Level Calibration and Correction" (Yuan et al., SIGIR 2025) | Fact-level calibration + correction for long-form, same problem formulation |
| **HIGH** | Spherical Steering (You et al., Feb 2026) | Better steering mechanism with confidence-gated application |
| **HIGH** | AFTER (Wang et al., ICLR 2026) | Adaptive factual-guided activation steering with query-aware offsets |
| **MEDIUM-HIGH** | "LLMs Should Express Uncertainty Explicitly" (Guo et al., Apr 2026) | Explicit uncertainty expression with mechanistic insights |
| **MEDIUM-HIGH** | CoCA (Li et al., Mar 2026) | Confidence-first RL framework for calibration |
| **MEDIUM-HIGH** | Conformal Linguistic Calibration (Jiang et al., 2025) | Claim-level rewriting with conformal guarantees |
| **MEDIUM** | ODESteer (ICLR 2026), AUSteer (ICLR 2026), SVF (Feb 2026), FLAS (May 2026) | Advanced steering methods that could serve as baselines |
| **MEDIUM** | CAST (IBM, ICLR 2025) | Conditional steering paradigm |
| **MEDIUM** | DCPO (Ma et al., Mar 2026) | Decoupled calibration in RL training |

## KEY NOVELTY ASSESSMENT

The **most threatening** paper to novelty is **"A Single Direction of Truth"** (O'Neill et al., 2025). It already demonstrates the probe-to-steering pipeline for hallucination control. The proposal must clearly differentiate on:
1. **Claim-level granularity** (vs. span-level binary hallucination detection)
2. **Confidence calibration** (continuous scores, not binary factual/hallucinated)
3. **Self-probing** within the generating model (vs. external observer model)
4. **Verbalized confidence alignment** (steering to calibrate expressed confidence, not just reduce hallucinations)

The other critical gap is the **"Atomic Calibration"** and **CARE** papers which establish the problem space the proposal operates in and should be cited as motivating work.

Sources:
- [Atomic Calibration of LLMs in Long-Form Generations](https://arxiv.org/abs/2410.13246)
- [Fact-Level Calibration and Correction for Long-Form Generations (CARE)](https://dl.acm.org/doi/10.1145/3726302.3730195)
- [Only Say What You Know: Calibration-Aware Generation](https://arxiv.org/abs/2605.01749)
- [Conformal Linguistic Calibration](https://arxiv.org/abs/2502.19110)
- [Spherical Steering](https://arxiv.org/abs/2602.08169)
- [ODESteer](https://arxiv.org/abs/2602.17560)
- [AUSteer](https://arxiv.org/abs/2602.04428)
- [Steering Vector Fields](https://arxiv.org/abs/2602.01654)
- [FLAS: Flow-based Activation Steering](https://arxiv.org/abs/2605.05892)
- [A Single Direction of Truth](https://arxiv.org/abs/2507.23221)
- [HaloProbe](https://arxiv.org/abs/2604.06165)
- [Neural Probe-Based Hallucination Detection](https://arxiv.org/abs/2512.20949)
- [HALP](https://arxiv.org/abs/2603.05465)
- [LLMs Should Express Uncertainty Explicitly](https://arxiv.org/abs/2604.05306)
- [CSFT: Verbalized Confidence Triggers Self-Verification](https://openreview.net/forum?id=P2o8wOzZMX)
- [DINCO](https://arxiv.org/abs/2509.25532)
- [AFTER](https://arxiv.org/abs/2601.01957)
- [Simple Factuality Probes](https://aclanthology.org/2025.findings-emnlp.880/)
- [CoCA: Confidence Before Answering](https://arxiv.org/abs/2603.05881)
- [DCPO: Decoupling Reasoning and Confidence](https://arxiv.org/abs/2603.09117)
- [CSS: Calibrated Claim-Level Specificity Control](https://arxiv.org/abs/2604.17487)
- [CAST: Conditional Activation Steering](https://arxiv.org/abs/2409.05907)
- [Behaviorally Calibrated RL](https://arxiv.org/abs/2512.19920)
- [Calibrating LLM Judges with Linear Probes](https://arxiv.org/abs/2512.22245)
- [Geometry-Calibrated Conformal Abstention](https://arxiv.org/abs/2604.27914)
- [Activation Steering Field Guide (blog)](https://subhadipmitra.com/blog/2026/activation-steering-field-guide/)

agentId: aea0f367b90d6b2a7 (use SendMessage with to: 'aea0f367b90d6b2a7' to continue this agent)
&lt;usage>total_tokens: 52548
tool_uses: 46
duration_ms: 251453&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "64d38cd0-3f08-4896-ac2f-fa0adfef4faf",
  "isSidechain": false,
  "promptId": "d0af2fce-b877-4a83-b1a2-3e65f7ded303",
  "type": "user",
  "uuid": "fdd71abd-0458-4b11-a19f-774c2f2fcec9",
  "toolUseResult": {
    "status": "completed",
    "prompt": "You are helping me review an ML paper proposal about \"probe-guided claim-level confidence calibration for long-form generation.\" The idea combines claim-level factuality probes with activation steering to calibrate verbalized confidence during long-form text generation. I need you to search for MISSING competitors or concurrent work that the proposal may have overlooked.\n\nThe proposal already cites: Han et al. (EMNLP 2025), Miao & Ungar (2026), CORAL (2026), CLAS (2026), ITI (NeurIPS 2023), ActCab/CoDec (EMNLP 2024), CURE (2026), CAG (2026), LoVeC (2025), PCNET (2026), SteerConf (NeurIPS 2025), ACT (WWW 2025), CSS (2026), Selective Abstraction (2026), Kumaran et al. (2026), Obeso et al. (2025), Scaling Laws for Activation Steering (ICML 2025), ESR (2026).\n\nPlease search for work the proposal may have MISSED using the following queries (use WebSearch):\n\n1. \"claim-level calibration long-form generation 2025 2026\" — any claim-level calibration work for long-form text\n2. \"activation steering confidence calibration 2026\" — concurrent steering-for-calibration work  \n3. \"probe guided decoding hallucination 2026\" — probe-guided generation approaches\n4. \"verbalized uncertainty long-form 2025 2026\" — verbalized uncertainty in long-form settings\n5. \"inference time intervention hallucination reduction 2026\" — ITI-style approaches for hallucinations\n6. \"linear probes hallucination detection steering 2026\" — probe+steering combinations\n7. \"site:arxiv.org claim level uncertainty calibration LLM 2026\" — arxiv-specific search\n8. \"faithfulness calibration generation ACL EMNLP 2026\" — venue-specific recent work\n9. \"activation engineering confidence LLM 2025 2026\" — activation engineering for confidence\n10. \"Rewarding Doubt hallucination 2026\" OR \"self-aware generation LLM 2026\" — alternative approaches\n\nFor each search, report: (a) the query used, (b) any papers found that are NOT in the cited list above, (c) how relevant they are to the proposal (high/medium/low), and (d) whether they threaten the novelty claim.\n\nFocus especially on papers from January-May 2026 that might be concurrent work. If you find something highly relevant, use WebFetch to read more details.",
    "agentId": "aea0f367b90d6b2a7",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have comprehensive results. Let me compile the final report.\n\n---\n\nHere is a systematic analysis of potentially missing competitors and concurrent work, organized by search query. I focus on papers **not already cited** in the proposal.\n\n---\n\n## QUERY 1: \"claim-level calibration long-form generation 2025 2026\"\n\n### Papers Found (NOT in cited list):\n\n**1. \"Atomic Calibration of LLMs in Long-Form Generations\"** -- Zhang et al., Findings of IJCNLP-AACL 2025 ([arXiv:2410.13246](https://arxiv.org/abs/2410.13246))\n- Systematically studies atomic (claim-level) calibration by decomposing long responses into atomic claims. Categorizes confidence elicitation methods into discriminative vs. generative types and proposes confidence fusion strategies.\n- **Relevance: HIGH.** This is a direct predecessor to the proposal's claim-level approach. It provides the empirical foundation showing LLMs are poorly calibrated at the atomic level in long-form generation.\n- **Novelty threat: MEDIUM.** It diagnoses the problem your proposal solves but does not use probes or activation steering as a remedy.\n\n**2. CARE: \"Fact-Level Calibration and Correction for Long-Form Generations\"** -- Yuan et al., SIGIR 2025 ([ACM](https://dl.acm.org/doi/10.1145/3726302.3730195))\n- Proposes a fact-level confidence calibration framework incorporating both relevance and correctness, plus CARE (Confidence-Aware Fact Correction) that uses high-confidence facts to iteratively refine low-confidence ones.\n- **Relevance: HIGH.** Operates at the same granularity (fact/claim-level) in long-form generation with calibration + correction.\n- **Novelty threat: MEDIUM.** Uses iterative correction rather than activation steering, so the mechanism differs, but the problem formulation overlaps substantially.\n\n**3. \"Only Say What You Know: Calibration-Aware Generation for Long-Form Factuality\" (CAG)** -- Luo et al., May 2026 ([arXiv:2605.01749](https://arxiv.org/abs/2605.01749))\n- Proposes \"Exploration-Commitment Decoupling\" separating knowledge exploration from final output commitment, with calibrated reliability estimates. Up to 13% factuality improvement.\n- **Relevance: HIGH.** Note: The proposal already cites \"CAG (2026)\" -- verify this is the same paper. If so, no issue.\n- **Novelty threat: LOW if already cited.**\n\n**4. \"Conformal Linguistic Calibration: Trading-off between Factuality and Specificity\"** -- Jiang et al., Feb 2025 ([arXiv:2502.19110](https://arxiv.org/abs/2502.19110))\n- Reinterprets linguistic calibration as answer set prediction with conformal guarantees. Enables uncertainty-aware adaptive claim rewriting.\n- **Relevance: MEDIUM-HIGH.** Addresses calibration at the claim level via semantic \"backoff\" rather than abstention.\n- **Novelty threat: LOW.** Different mechanism (conformal prediction / linguistic hedging) vs. activation steering.\n\n---\n\n## QUERY 2: \"activation steering confidence calibration 2026\"\n\n### Papers Found (NOT in cited list):\n\n**5. \"Spherical Steering: Geometry-Aware Activation Rotation for Language Models\"** -- You et al., Feb 2026 ([arXiv:2602.08169](https://arxiv.org/abs/2602.08169))\n- Proposes rotation-based (rather than addition-based) steering using spherical linear interpolation, with adaptive von Mises-Fisher confidence gating. Up to +15% accuracy.\n- **Relevance: MEDIUM-HIGH.** Directly relevant as a better steering mechanism that could be applied to confidence calibration. The confidence-gated aspect is particularly relevant.\n- **Novelty threat: MEDIUM.** If someone combines Spherical Steering with factuality probes, it subsumes part of the proposal's contribution.\n\n**6. ODESteer: \"A Unified ODE-Based Steering Framework for LLM Alignment\"** -- Zhao et al., ICLR 2026 ([arXiv:2602.17560](https://arxiv.org/abs/2602.17560))\n- Interprets activation addition as first-order approximation of an ODE; uses barrier functions from control theory for multi-step adaptive steering. +5.7% on TruthfulQA.\n- **Relevance: MEDIUM.** General steering framework that could be applied to confidence/factuality steering. Provides theoretical grounding.\n- **Novelty threat: LOW-MEDIUM.** Different theoretical framework but potentially applicable to the proposal's setting.\n\n**7. AUSteer: \"Fine-Grained Activation Steering: Steering Less, Achieving More\"** -- ICLR 2026 ([arXiv:2602.04428](https://arxiv.org/abs/2602.04428))\n- Decomposes block activations into atomic units, selects discriminative ones via activation momenta, applies adaptive per-input steering strengths.\n- **Relevance: MEDIUM.** Fine-grained steering method that could be combined with probe-guided approaches. Relevant as a baseline/alternative steering mechanism.\n- **Novelty threat: LOW-MEDIUM.** Different target (general alignment, not confidence calibration specifically).\n\n**8. \"Steering Vector Fields for Context-Aware Inference-Time Control in LLMs\"** -- Li et al., Feb 2026 ([arXiv:2602.01654](https://arxiv.org/abs/2602.01654))\n- Learns a differentiable concept scoring function whose gradient defines context-dependent steering direction (rather than a fixed vector). Supports multi-layer coordinated intervention.\n- **Relevance: MEDIUM.** Addresses the limitation that static steering vectors fail in long-form generation -- directly relevant to the proposal's setting.\n- **Novelty threat: LOW-MEDIUM.** General steering methodology, not specifically applied to confidence calibration.\n\n**9. FLAS: \"Beyond Steering Vector: Flow-based Activation Steering for Inference-Time Intervention\"** -- Jin et al., May 2026 ([arXiv:2605.05892](https://arxiv.org/abs/2605.05892))\n- Learns concept-conditioned velocity field for multi-step, token-varying activation transformations. First learned method to consistently surpass prompting baselines.\n- **Relevance: MEDIUM.** Another advanced steering mechanism that supersedes static vector approaches.\n- **Novelty threat: LOW.** General framework, not applied to confidence.\n\n---\n\n## QUERY 3: \"probe guided decoding hallucination 2026\"\n\n### Papers Found (NOT in cited list):\n\n**10. \"A Single Direction of Truth: An Observer Model's Linear Residual Probe Exposes and Steers Contextual Hallucinations\"** -- O'Neill et al., July 2025 ([arXiv:2507.23221](https://arxiv.org/abs/2507.23221))\n- **THIS IS THE MOST IMPORTANT FIND.** Uses a linear probe on an observer model's residual stream to detect hallucinations (>0.95 F1), then uses the probe weight vector as a steering vector injected into a generator to reduce/amplify hallucination prevalence.\n- **Relevance: VERY HIGH.** This is extremely close to the proposal's approach -- it combines linear probes with activation steering for hallucination control. The key difference is it uses an external observer model and targets contextual hallucination, while the proposal targets confidence calibration.\n- **Novelty threat: HIGH.** The core probe-to-steering pipeline is very similar. The proposal must differentiate clearly (e.g., claim-level granularity, confidence calibration vs. binary hallucination, self-probing vs. observer model).\n\n**11. HaloProbe: \"Bayesian Detection and Mitigation of Object Hallucinations in Vision-Language Models\"** -- Zohrabi et al., April 2026 ([arXiv:2604.06165](https://arxiv.org/abs/2604.06165))\n- Bayesian framework combining external description statistics with internal decoding signals for token-level hallucination probability estimation, used for guided decoding.\n- **Relevance: MEDIUM.** Probe-guided decoding for hallucination mitigation, but in the vision-language setting.\n- **Novelty threat: LOW.** Different modality (VLMs) and approach (Bayesian, not linear probe + steering).\n\n**12. \"Neural Probe-Based Hallucination Detection for Large Language Models\"** -- Liang & Wang, Dec 2025 ([arXiv:2512.20949](https://arxiv.org/abs/2512.20949))\n- Uses lightweight MLP probes (not just linear) with Bayesian-optimized layer selection and multi-objective loss for token-level hallucination detection.\n- **Relevance: MEDIUM.** Probe-based detection, but detection-only (no steering or calibration component).\n- **Novelty threat: LOW.** Detection only, no intervention.\n\n**13. HALP: \"Detecting Hallucinations in Vision-Language Models without Generating a Single Token\"** -- EACL 2026 ([arXiv:2603.05465](https://arxiv.org/abs/2603.05465))\n- Probes internal representations pre-generation to predict hallucination risk (up to 0.93 AUROC), enabling early abstention or adaptive decoding.\n- **Relevance: MEDIUM.** Pre-generation probing for hallucination detection, though in VLMs.\n- **Novelty threat: LOW.** Different modality and no steering mechanism.\n\n---\n\n## QUERY 4: \"verbalized uncertainty long-form 2025 2026\"\n\n### Papers Found (NOT in cited list):\n\n**14. \"LLMs Should Express Uncertainty Explicitly\"** -- Guo et al., April 2026 ([arXiv:2604.05306](https://arxiv.org/abs/2604.05306))\n- Compares end-of-reasoning self-assessment (confidence scores) with during-reasoning `&lt;uncertain>` markers. Finds both reduce overconfident errors and improve RAG integration.\n- **Relevance: MEDIUM-HIGH.** Directly addresses verbalized uncertainty with mechanistic insights (changes concentrate in later layers, sharpening existing structures).\n- **Novelty threat: LOW.** Training-based approach without probes or steering.\n\n**15. CSFT: \"Verbalized Confidence Triggers Self-Verification: Emergent Behavior Without Explicit Reasoning Supervision\"** -- 2026 ([OpenReview](https://openreview.net/forum?id=P2o8wOzZMX))\n- Confidence-supervised fine-tuning triggers emergent self-verification (from <1.5% to ~20% rates) without explicit reasoning supervision.\n- **Relevance: MEDIUM.** Shows that confidence training alone can elicit sophisticated calibration behavior.\n- **Novelty threat: LOW.** SFT-based, not inference-time intervention.\n\n**16. DINCO: \"Calibrating Verbalized Confidence with Self-Generated Distractors\"** -- Wang et al., 2025 ([arXiv:2509.25532](https://arxiv.org/abs/2509.25532))\n- Normalizes verbalized confidence across self-generated distractors to correct for suggestibility bias. DINCO at 10 runs outperforms self-consistency at 100.\n- **Relevance: MEDIUM.** Alternative calibration approach for verbalized confidence.\n- **Novelty threat: LOW.** Purely sampling-based, orthogonal to probe+steering approach.\n\n---\n\n## QUERY 5: \"inference time intervention hallucination reduction 2026\"\n\n### Papers Found (NOT in cited list):\n\n**17. AFTER: \"Mitigating the Object Hallucination of LVLM via Adaptive Factual-Guided Activation Editing\"** -- Wang et al., ICLR 2026 ([arXiv:2601.01957](https://arxiv.org/abs/2601.01957))\n- Combines Factual-Augmented Activation Steering (FAS) with Query-Adaptive Offset Optimization (QAO) for input-specific steering from a general factual steering vector. Up to 16.3% hallucination reduction.\n- **Relevance: MEDIUM-HIGH.** Adaptive, query-aware steering for factuality -- conceptually related to probe-guided steering for confidence.\n- **Novelty threat: MEDIUM.** Different domain (VLMs), but the adaptive factual-guided steering mechanism has significant conceptual overlap.\n\n---\n\n## QUERY 6: \"linear probes hallucination detection steering 2026\"\n\n**Key finding already covered above (#10, \"A Single Direction of Truth\").** Also:\n\n**18. \"Simple Factuality Probes Detect Hallucinations in Long-Form Natural Language Generation\"** -- Han et al., Findings of EMNLP 2025 ([ACL Anthology](https://aclanthology.org/2025.findings-emnlp.880/))\n- LLM hidden states are highly predictive of factuality; lightweight probes achieve competitive performance with up to 100x fewer FLOPs.\n- **Relevance: HIGH.** Note: The proposal already cites \"Han et al. (EMNLP 2025)\" -- likely this paper. Confirm.\n- **Novelty threat: N/A if cited.**\n\n---\n\n## QUERY 7: \"site:arxiv.org claim level uncertainty calibration LLM 2026\"\n\n### Papers Found (NOT in cited list):\n\n**19. CoCA: \"Confidence Before Answering: A Paradigm Shift for Efficient LLM Uncertainty Estimation\"** -- Li et al., March 2026 ([arXiv:2603.05881](https://arxiv.org/abs/2603.05881))\n- GRPO-based RL that jointly optimizes confidence calibration and answer accuracy via confidence-first generation with segmented credit assignment.\n- **Relevance: MEDIUM-HIGH.** Addresses confidence calibration through RL training rather than inference-time intervention.\n- **Novelty threat: LOW.** Different mechanism (RL training vs. probe+steering).\n\n**20. DCPO: \"Decoupling Reasoning and Confidence: Resurrecting Calibration in Reinforcement Learning from Verifiable Rewards\"** -- Ma et al., March 2026 ([arXiv:2603.09117](https://arxiv.org/abs/2603.09117))\n- Identifies that RLVR training makes models overconfident on incorrect answers; proposes decoupling reasoning and calibration objectives.\n- **Relevance: MEDIUM.** Addresses the overconfidence problem through training rather than inference-time.\n- **Novelty threat: LOW.** Complementary approach.\n\n**21. \"Calibrating LLM Judges: Linear Probes for Fast and Reliable Uncertainty Estimation\"** -- Dec 2025 ([arXiv:2512.22245](https://arxiv.org/abs/2512.22245))\n- Uses linear probes on LLM-as-judge hidden states for uncertainty estimation.\n- **Relevance: MEDIUM.** Probes for calibration, but in the LLM-as-judge setting.\n- **Novelty threat: LOW.** Different application context.\n\n---\n\n## QUERY 8: \"faithfulness calibration generation ACL EMNLP 2026\"\n\n### Papers Found (NOT in cited list):\n\n**22. CSS: \"Answer Only as Precisely as Justified: Calibrated Claim-Level Specificity Control for Agentic Systems\"** -- Huang et al., April 2026 ([arXiv:2604.17487](https://arxiv.org/abs/2604.17487))\n- Decomposes answers into claims, uses Clopper-Pearson confidence bounds for calibrated specificity selection (fine-grained, coarse, or omit). Improves utility from 0.846 to 0.913 on LongFact.\n- **Relevance: HIGH.** Note: The proposal already cites \"CSS (2026)\" -- likely this paper. Confirm it is the same.\n- **Novelty threat: N/A if cited.**\n\n---\n\n## QUERY 9: \"activation engineering confidence LLM 2025 2026\"\n\n### Papers Found (NOT in cited list):\n\n**23. CAST: \"Programming Refusal with Conditional Activation Steering\"** -- IBM, ICLR 2025 (Spotlight) ([arXiv:2409.05907](https://arxiv.org/abs/2409.05907))\n- Conditional steering that applies behavior vectors only when activation patterns match a condition vector. Adds controllability without extra compute.\n- **Relevance: MEDIUM.** The conditional application mechanism (steer only when condition is met) is relevant -- analogous to \"steer only when probe detects low confidence.\"\n- **Novelty threat: LOW-MEDIUM.** General mechanism, but the conditional steering paradigm is conceptually close.\n\n---\n\n## QUERY 10: \"Rewarding Doubt hallucination 2026\" / \"self-aware generation LLM 2026\"\n\n### Papers Found (NOT in cited list):\n\n**24. \"Mitigating LLM Hallucination via Behaviorally Calibrated Reinforcement Learning\"** -- Wu et al., Dec 2025/Jan 2026 ([arXiv:2512.19920](https://arxiv.org/abs/2512.19920))\n- Uses behavioral calibration in RL with strictly proper scoring rules so models learn to abstain when not confident. A 4B model matches frontier models in calibration error.\n- **Relevance: MEDIUM.** RL-based approach to calibrated uncertainty expression.\n- **Novelty threat: LOW.** Training-based, not inference-time.\n\n---\n\n## SUMMARY OF MOST CRITICAL MISSING CITATIONS\n\nRanked by urgency:\n\n| Priority | Paper | Why It Matters |\n|----------|-------|---------------|\n| **CRITICAL** | \"A Single Direction of Truth\" (O'Neill et al., 2025) | **Combines linear probes with activation steering for hallucination control** -- the closest existing work to the proposal's core mechanism |\n| **HIGH** | \"Atomic Calibration of LLMs in Long-Form Generations\" (Zhang et al., IJCNLP 2025) | Foundational work on claim-level calibration in long-form generation |\n| **HIGH** | CARE / \"Fact-Level Calibration and Correction\" (Yuan et al., SIGIR 2025) | Fact-level calibration + correction for long-form, same problem formulation |\n| **HIGH** | Spherical Steering (You et al., Feb 2026) | Better steering mechanism with confidence-gated application |\n| **HIGH** | AFTER (Wang et al., ICLR 2026) | Adaptive factual-guided activation steering with query-aware offsets |\n| **MEDIUM-HIGH** | \"LLMs Should Express Uncertainty Explicitly\" (Guo et al., Apr 2026) | Explicit uncertainty expression with mechanistic insights |\n| **MEDIUM-HIGH** | CoCA (Li et al., Mar 2026) | Confidence-first RL framework for calibration |\n| **MEDIUM-HIGH** | Conformal Linguistic Calibration (Jiang et al., 2025) | Claim-level rewriting with conformal guarantees |\n| **MEDIUM** | ODESteer (ICLR 2026), AUSteer (ICLR 2026), SVF (Feb 2026), FLAS (May 2026) | Advanced steering methods that could serve as baselines |\n| **MEDIUM** | CAST (IBM, ICLR 2025) | Conditional steering paradigm |\n| **MEDIUM** | DCPO (Ma et al., Mar 2026) | Decoupled calibration in RL training |\n\n## KEY NOVELTY ASSESSMENT\n\nThe **most threatening** paper to novelty is **\"A Single Direction of Truth\"** (O'Neill et al., 2025). It already demonstrates the probe-to-steering pipeline for hallucination control. The proposal must clearly differentiate on:\n1. **Claim-level granularity** (vs. span-level binary hallucination detection)\n2. **Confidence calibration** (continuous scores, not binary factual/hallucinated)\n3. **Self-probing** within the generating model (vs. external observer model)\n4. **Verbalized confidence alignment** (steering to calibrate expressed confidence, not just reduce hallucinations)\n\nThe other critical gap is the **\"Atomic Calibration\"** and **CARE** papers which establish the problem space the proposal operates in and should be cited as motivating work.\n\nSources:\n- [Atomic Calibration of LLMs in Long-Form Generations](https://arxiv.org/abs/2410.13246)\n- [Fact-Level Calibration and Correction for Long-Form Generations (CARE)](https://dl.acm.org/doi/10.1145/3726302.3730195)\n- [Only Say What You Know: Calibration-Aware Generation](https://arxiv.org/abs/2605.01749)\n- [Conformal Linguistic Calibration](https://arxiv.org/abs/2502.19110)\n- [Spherical Steering](https://arxiv.org/abs/2602.08169)\n- [ODESteer](https://arxiv.org/abs/2602.17560)\n- [AUSteer](https://arxiv.org/abs/2602.04428)\n- [Steering Vector Fields](https://arxiv.org/abs/2602.01654)\n- [FLAS: Flow-based Activation Steering](https://arxiv.org/abs/2605.05892)\n- [A Single Direction of Truth](https://arxiv.org/abs/2507.23221)\n- [HaloProbe](https://arxiv.org/abs/2604.06165)\n- [Neural Probe-Based Hallucination Detection](https://arxiv.org/abs/2512.20949)\n- [HALP](https://arxiv.org/abs/2603.05465)\n- [LLMs Should Express Uncertainty Explicitly](https://arxiv.org/abs/2604.05306)\n- [CSFT: Verbalized Confidence Triggers Self-Verification](https://openreview.net/forum?id=P2o8wOzZMX)\n- [DINCO](https://arxiv.org/abs/2509.25532)\n- [AFTER](https://arxiv.org/abs/2601.01957)\n- [Simple Factuality Probes](https://aclanthology.org/2025.findings-emnlp.880/)\n- [CoCA: Confidence Before Answering](https://arxiv.org/abs/2603.05881)\n- [DCPO: Decoupling Reasoning and Confidence](https://arxiv.org/abs/2603.09117)\n- [CSS: Calibrated Claim-Level Specificity Control](https://arxiv.org/abs/2604.17487)\n- [CAST: Conditional Activation Steering](https://arxiv.org/abs/2409.05907)\n- [Behaviorally Calibrated RL](https://arxiv.org/abs/2512.19920)\n- [Calibrating LLM Judges with Linear Probes](https://arxiv.org/abs/2512.22245)\n- [Geometry-Calibrated Conformal Abstention](https://arxiv.org/abs/2604.27914)\n- [Activation Steering Field Guide (blog)](https://subhadipmitra.com/blog/2026/activation-steering-field-guide/)"
      }
    ],
    "totalDurationMs": 251453,
    "totalTokens": 52548,
    "totalToolUseCount": 46,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3895,
      "cache_read_input_tokens": 42842,
      "output_tokens": 5810,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3895
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5810,
          "cache_read_input_tokens": 42842,
          "cache_creation_input_tokens": 3895,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3895,
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
      "otherToolCount": 46
    }
  },
  "sourceToolAssistantUUID": "64d38cd0-3f08-4896-ac2f-fa0adfef4faf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 17_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-15 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "fdd71abd-0458-4b11-a19f-774c2f2fcec9",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19"
}
```

---

### Runtime record

_source line 18_

```json
{
  "type": "ai-title",
  "aiTitle": "Claim-level confidence calibration for long-form LLM generation",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19"
}
```

---

### Assistant

_source line 19 · 2026-05-15T14:20:36.102Z_

Critical finding: "A Single Direction of Truth" (O'Neill et al., 2025) — probe-to-steering for hallucination control — is highly relevant and not cited. Let me now verify the feasibility claims and check for the most critical missing paper more carefully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fdd71abd-0458-4b11-a19f-774c2f2fcec9",
  "isSidechain": false,
  "requestId": "req_011Cb4W4qzkfLvLzgeyae9a1",
  "type": "assistant",
  "uuid": "dbecdc0c-803b-4c3d-a645-f5a62520852b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KqxjhbHEBgMBrspbxsduWA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6637,
      "cache_read_input_tokens": 35884,
      "output_tokens": 139,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6637,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 139,
          "cache_read_input_tokens": 35884,
          "cache_creation_input_tokens": 6637,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6637
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

_source line 20 · 2026-05-15T14:20:36.214Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01DPF2NQtNwVrAQcLafxStEU`</summary>

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
  "parentUuid": "dbecdc0c-803b-4c3d-a645-f5a62520852b",
  "isSidechain": false,
  "requestId": "req_011Cb4W4qzkfLvLzgeyae9a1",
  "type": "assistant",
  "uuid": "aeafd275-94f6-4da8-b91d-3c08635da021",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KqxjhbHEBgMBrspbxsduWA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6637,
      "cache_read_input_tokens": 35884,
      "output_tokens": 139,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6637,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 139,
          "cache_read_input_tokens": 35884,
          "cache_creation_input_tokens": 6637,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6637
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

_source line 21 · 2026-05-15T14:20:36.220Z_

<details><summary>↩ Tool result · `toolu_01DPF2NQtNwVrAQcLafxStEU`</summary>

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
  "parentUuid": "aeafd275-94f6-4da8-b91d-3c08635da021",
  "isSidechain": false,
  "promptId": "d0af2fce-b877-4a83-b1a2-3e65f7ded303",
  "type": "user",
  "uuid": "7a5948d1-b1f2-46ce-973e-0b6497dff652",
  "toolUseResult": {
    "matches": [
      "WebSearch",
      "WebFetch"
    ],
    "query": "select:WebSearch,WebFetch",
    "total_deferred_tools": 17
  },
  "sourceToolAssistantUUID": "aeafd275-94f6-4da8-b91d-3c08635da021",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 22 · 2026-05-15T14:20:45.544Z_

<details><summary>Logged reasoning block</summary>

```text
Let me now do my own independent verification of the most critical aspects:

1. Verify "A Single Direction of Truth" (O'Neill et al., 2025) - this is the most threatening competitor
2. Check whether the proposal's compute budget (250 H100-hours) fits the user's constraint of ≤200 H100-hours
3. Verify the Atomic Calibration paper (already cited in the proposal, I see it in key_references)
4. Check CARE (SIGIR 2025) which seems to be a missing competitor
5. Check venue deadlines

Let me look more carefully at the proposal. I notice:


- Atomic Calibration is already cited, so that's covered
- "A Single Direction of Truth" is missing from the references entirely
- CARE (SIGIR 2025) is also not cited
- The compute budget lists ~250h H100 80GB for manual mode, which exceeds the user's hard constraint of ≤200 H100-hours total

These are the key issues I need to verify.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7a5948d1-b1f2-46ce-973e-0b6497dff652",
  "isSidechain": false,
  "requestId": "req_011Cb4W5BqMbraG6obknBck4",
  "type": "assistant",
  "uuid": "25f80265-737d-4356-8cbc-156d40f90987",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EBFxoEJuczMvy8JY4x5vy7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1158,
      "cache_read_input_tokens": 42521,
      "output_tokens": 553,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1158,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 553,
          "cache_read_input_tokens": 42521,
          "cache_creation_input_tokens": 1158,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1158
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

_source line 23 · 2026-05-15T14:20:45.567Z_

Let me verify the most threatening missing competitor and check compute constraints.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "25f80265-737d-4356-8cbc-156d40f90987",
  "isSidechain": false,
  "requestId": "req_011Cb4W5BqMbraG6obknBck4",
  "type": "assistant",
  "uuid": "700acd96-13c0-4046-be54-3e09eb690550",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EBFxoEJuczMvy8JY4x5vy7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1158,
      "cache_read_input_tokens": 42521,
      "output_tokens": 553,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1158,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 553,
          "cache_read_input_tokens": 42521,
          "cache_creation_input_tokens": 1158,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1158
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

_source line 24 · 2026-05-15T14:20:47.240Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01QZkC5sELjtNPi4cdCgZBQv`</summary>

```json
{
  "url": "https://arxiv.org/abs/2507.23221",
  "prompt": "Extract the full abstract, authors, title, and submission date. What exactly does this paper do? Does it: (1) use linear probes on hidden states, (2) use the probe direction as a steering vector, (3) reduce hallucinations via activation steering? What models and tasks does it test on? What are the key results?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "700acd96-13c0-4046-be54-3e09eb690550",
  "isSidechain": false,
  "requestId": "req_011Cb4W5BqMbraG6obknBck4",
  "type": "assistant",
  "uuid": "40c6e6fb-bb5a-4862-a08d-33935f5bbb06",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EBFxoEJuczMvy8JY4x5vy7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1158,
      "cache_read_input_tokens": 42521,
      "output_tokens": 553,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1158,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 553,
          "cache_read_input_tokens": 42521,
          "cache_creation_input_tokens": 1158,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1158
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

_source line 25 · 2026-05-15T14:20:47.711Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015ebpSAAsCAyqzBoACD2eDT`</summary>

```json
{
  "query": "CARE fact-level calibration correction long-form generation SIGIR 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "40c6e6fb-bb5a-4862-a08d-33935f5bbb06",
  "isSidechain": false,
  "requestId": "req_011Cb4W5BqMbraG6obknBck4",
  "type": "assistant",
  "uuid": "c7a8ae6d-1633-49c1-9ddb-0cd66e573e7b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EBFxoEJuczMvy8JY4x5vy7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1158,
      "cache_read_input_tokens": 42521,
      "output_tokens": 553,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1158,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 553,
          "cache_read_input_tokens": 42521,
          "cache_creation_input_tokens": 1158,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1158
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

_source line 26 · 2026-05-15T14:20:48.342Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UR9aKSdtv1AQ3n53T4mc1c`</summary>

```json
{
  "query": "AAAI 2027 submission deadline July 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c7a8ae6d-1633-49c1-9ddb-0cd66e573e7b",
  "isSidechain": false,
  "requestId": "req_011Cb4W5BqMbraG6obknBck4",
  "type": "assistant",
  "uuid": "8b4051c7-288b-41b0-a98d-88562e49e915",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EBFxoEJuczMvy8JY4x5vy7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1158,
      "cache_read_input_tokens": 42521,
      "output_tokens": 553,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1158,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 553,
          "cache_read_input_tokens": 42521,
          "cache_creation_input_tokens": 1158,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1158
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

_source line 27 · 2026-05-15T14:20:51.955Z_

<details><summary>↩ Tool result · `toolu_01UR9aKSdtv1AQ3n53T4mc1c`</summary>

```text
Web search results for query: "AAAI 2027 submission deadline July 2026"

Links: [{"title":"AI Deadlines – AI Conference Call For Paper Deadlines","url":"http://aideadlines.org/"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"AI & ML Conference Deadlines 2026–2027","url":"https://trybibby.com/conference-deadlines"},{"title":"AAAI Conference on Artificial Intelligence - AAAI","url":"https://aaai.org/conference/aaai/"},{"title":"AAAI-27 - AAAI","url":"https://aaai.org/conference/aaai/aaai-27/"},{"title":"AAAI: National Conference on Artificial Intelligence 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=3"},{"title":"Update aaai conference deadlines · huggingface/ai-deadlines at 8e14540","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/8e145403081be22360311ec9ad9565e14b1f2d32"},{"title":"AAAI Conference on Artificial Intelligence","url":"http://aideadlines.org/conference/?id=aaai27"},{"title":"AAAI 2027 LaTeX Template | Author Kit & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/aaai"},{"title":"AI/ML Conference Timeline | NIU AI","url":"https://www.niuai.org/resources/conference-timeline/"}]

Based on the search results, I found the AAAI 2027 submission deadline information:

The abstracts are due on July 21, 2026 at 11:59 PM UTC-12, and full papers are due on July 28, 2026 at 11:59 PM UTC-12. Supplementary material and code are due by July 31, 2026 at 11:59 PM UTC-12.

The Forty-first Conference on Artificial Intelligence (AAAI-27) will be held in Montréal, Québec, Canada from February 16-23, 2027.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8b4051c7-288b-41b0-a98d-88562e49e915",
  "isSidechain": false,
  "promptId": "d0af2fce-b877-4a83-b1a2-3e65f7ded303",
  "type": "user",
  "uuid": "5137e190-2e66-4735-9138-6141686c9efc",
  "toolUseResult": {
    "query": "AAAI 2027 submission deadline July 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01YKZEZkm1zRgh1mMRbcZBVo",
        "content": [
          {
            "title": "AI Deadlines – AI Conference Call For Paper Deadlines",
            "url": "http://aideadlines.org/"
          },
          {
            "title": "AI Conference Deadlines",
            "url": "https://mlciv.com/ai-deadlines/"
          },
          {
            "title": "AI & ML Conference Deadlines 2026–2027",
            "url": "https://trybibby.com/conference-deadlines"
          },
          {
            "title": "AAAI Conference on Artificial Intelligence - AAAI",
            "url": "https://aaai.org/conference/aaai/"
          },
          {
            "title": "AAAI-27 - AAAI",
            "url": "https://aaai.org/conference/aaai/aaai-27/"
          },
          {
            "title": "AAAI: National Conference on Artificial Intelligence 2027 2026 2025 ...",
            "url": "http://www.wikicfp.com/cfp/program?id=3"
          },
          {
            "title": "Update aaai conference deadlines · huggingface/ai-deadlines at 8e14540",
            "url": "https://huggingface.co/spaces/huggingface/ai-deadlines/commit/8e145403081be22360311ec9ad9565e14b1f2d32"
          },
          {
            "title": "AAAI Conference on Artificial Intelligence",
            "url": "http://aideadlines.org/conference/?id=aaai27"
          },
          {
            "title": "AAAI 2027 LaTeX Template | Author Kit & Overleaf | Underleaf",
            "url": "https://www.underleaf.ai/templates/aaai"
          },
          {
            "title": "AI/ML Conference Timeline | NIU AI",
            "url": "https://www.niuai.org/resources/conference-timeline/"
          }
        ]
      },
      "Based on the search results, I found the AAAI 2027 submission deadline information:\n\nThe abstracts are due on July 21, 2026 at 11:59 PM UTC-12, and full papers are due on July 28, 2026 at 11:59 PM UTC-12. Supplementary material and code are due by July 31, 2026 at 11:59 PM UTC-12.\n\nThe Forty-first Conference on Artificial Intelligence (AAAI-27) will be held in Montréal, Québec, Canada from February 16-23, 2027."
    ],
    "durationSeconds": 3.6090118510000173
  },
  "sourceToolAssistantUUID": "8b4051c7-288b-41b0-a98d-88562e49e915",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-15T14:20:52.887Z_

<details><summary>↩ Tool result · `toolu_01QZkC5sELjtNPi4cdCgZBQv`</summary>

```text
# Paper Summary

**Title:** "A Single Direction of Truth: An Observer Model's Linear Residual Probe Exposes and Steers Contextual Hallucinations"

**Authors:** Charles O'Neill, Slava Chalnev, Chi Chi Zhao, Max Kirkby, Mudith Jayasekara

**Submission Date:** July 31, 2025

**Abstract:** The authors address contextual hallucinations using an interpretability approach where "a generator-agnostic observer model detects hallucinations via a single forward pass and a linear probe on its residual stream." They identify one transferable linear direction distinguishing hallucinated from faithful outputs.

## What the Paper Does

The research accomplishes all three objectives you mentioned:

1. **Linear probes on hidden states:** Uses linear probes applied to the residual stream to detect hallucinations
2. **Probe direction as steering vector:** The identified linear direction proves actionable for manipulation
3. **Reduction via activation steering:** Demonstrates that "manipulating this direction causally steers generator hallucination rates"

## Models and Tasks

The work evaluates performance across Gemma-2 models (2B to 27B parameters). They also introduce the ContraTales benchmark—a 2000-example dataset for assessing hallucination detection solutions in realistic contexts.

## Key Results

- Linear probe outperforms baselines by 5-27 percentage points
- Demonstrates robust mid-layer performance across model sizes
- Gradient-times-activation analysis localizes the signal to specific late-layer MLP sub-circuits
- Proves the direction's causal effectiveness in reducing hallucinations
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "40c6e6fb-bb5a-4862-a08d-33935f5bbb06",
  "isSidechain": false,
  "promptId": "d0af2fce-b877-4a83-b1a2-3e65f7ded303",
  "type": "user",
  "uuid": "d0133548-c2e0-430f-9eea-fa36eaefc99d",
  "toolUseResult": {
    "bytes": 46658,
    "code": 200,
    "codeText": "OK",
    "result": "# Paper Summary\n\n**Title:** \"A Single Direction of Truth: An Observer Model's Linear Residual Probe Exposes and Steers Contextual Hallucinations\"\n\n**Authors:** Charles O'Neill, Slava Chalnev, Chi Chi Zhao, Max Kirkby, Mudith Jayasekara\n\n**Submission Date:** July 31, 2025\n\n**Abstract:** The authors address contextual hallucinations using an interpretability approach where \"a generator-agnostic observer model detects hallucinations via a single forward pass and a linear probe on its residual stream.\" They identify one transferable linear direction distinguishing hallucinated from faithful outputs.\n\n## What the Paper Does\n\nThe research accomplishes all three objectives you mentioned:\n\n1. **Linear probes on hidden states:** Uses linear probes applied to the residual stream to detect hallucinations\n2. **Probe direction as steering vector:** The identified linear direction proves actionable for manipulation\n3. **Reduction via activation steering:** Demonstrates that \"manipulating this direction causally steers generator hallucination rates\"\n\n## Models and Tasks\n\nThe work evaluates performance across Gemma-2 models (2B to 27B parameters). They also introduce the ContraTales benchmark—a 2000-example dataset for assessing hallucination detection solutions in realistic contexts.\n\n## Key Results\n\n- Linear probe outperforms baselines by 5-27 percentage points\n- Demonstrates robust mid-layer performance across model sizes\n- Gradient-times-activation analysis localizes the signal to specific late-layer MLP sub-circuits\n- Proves the direction's causal effectiveness in reducing hallucinations",
    "durationMs": 5645,
    "url": "https://arxiv.org/abs/2507.23221"
  },
  "sourceToolAssistantUUID": "40c6e6fb-bb5a-4862-a08d-33935f5bbb06",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-15T14:20:54.770Z_

<details><summary>↩ Tool result · `toolu_015ebpSAAsCAyqzBoACD2eDT`</summary>

```text
Web search results for query: "CARE fact-level calibration correction long-form generation SIGIR 2025"

Links: [{"title":"Fact-Level Calibration and Correction for Long-Form Generations | Proceedings of the 48th International ACM SIGIR Conference on Research and Development in Information Retrieval","url":"https://dl.acm.org/doi/10.1145/3726302.3730195"},{"title":"Fact-Level Calibration and Correction for Long-Form Generations | Request PDF","url":"https://www.researchgate.net/publication/393657638_Fact-Level_Calibration_and_Correction_for_Long-Form_Generations"},{"title":"SIGIR 2025, Padua, 13-18 July | Accepted Papers - Unipd","url":"https://sigir2025.dei.unipd.it/accepted-papers.html"},{"title":"Fact-Level Calibration and Correction for Long-Form ...","url":"https://dl.acm.org/doi/pdf/10.1145/3726302.3730195"},{"title":"Fact Verification in Knowledge Graphs Using LLMs","url":"https://www.dei.unipd.it/~silvello/papers/2025-SIGIR_Demo_LLM.pdf"},{"title":"SIGIR-AP 2025 Tutorial Proposal:","url":"https://www.researchgate.net/profile/Su_Weihang/publication/396210825_SIGIR-AP_2025_Tutorial_Proposal_Dynamic_and_Parametric_Retrieval-Augmented_Generation/links/68e2347ef3032e2b4be6b800/SIGIR-AP-2025-Tutorial-Proposal-Dynamic-and-Parametric-Retrieval-Augmented-Generation.pdf"},{"title":"SIGIR-AP 2025","url":"https://www.sigir-ap.org/sigir-ap-2025/accepted-papers/index.html"},{"title":"(PDF) SIGIR 2025 -- LiveRAG Challenge Report","url":"https://www.researchgate.net/publication/393477229_SIGIR_2025_--_LiveRAG_Challenge_Report"},{"title":"The Great Nugget Recall: Automating Fact Extraction and RAG Evaluation with Large Language Models | Request PDF","url":"https://www.researchgate.net/publication/393658928_The_Great_Nugget_Recall_Automating_Fact_Extraction_and_RAG_Evaluation_with_Large_Language_Models"},{"title":"Fact-Level Confidence Calibration and Self-Correction","url":"https://arxiv.org/html/2411.13343v1"}]

Based on the search results, I found information about the paper you're looking for:

## Fact-Level Calibration and Correction for Long-Form Generations (SIGIR 2025)

CARE (Confidence-Aware Fact Correction) is a method that leverages high-confidence facts to iteratively refine and correct low-confidence ones.

**Paper Details:**
- Authors: Yige Yuan, Bingbing Xu, Hexiang Tan, Fei Sun, Teng Xiao, Wei Li, Huawei Shen, Xueqi Cheng
- Conference: SIGIR '25: The 48th International ACM SIGIR Conference on Research and Development in Information Retrieval

**Research Focus:**

Large language models have achieved remarkable progress across various domains, yet their tendency to generate hallucinations remains a critical barrier to their practical reliability. Confidence calibration addresses this challenge by aligning a model's confidence with its actual accuracy, improving self-evaluation and trustworthiness.

The paper proposes a fact-level confidence calibration framework that evaluates and adjusts confidence at the granularity of individual facts, incorporating both relevance and correctness. This framework identifies finer-grained calibration discrepancies, reduces overconfidence, and reveals confidence variance.

Experimental results demonstrate that CARE effectively improves the quality of generated content. The code is available at https://github.com/yuanyige/fact-calibration.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c7a8ae6d-1633-49c1-9ddb-0cd66e573e7b",
  "isSidechain": false,
  "promptId": "d0af2fce-b877-4a83-b1a2-3e65f7ded303",
  "type": "user",
  "uuid": "8651cc72-e6a1-4f22-abf4-462f73f4ca66",
  "toolUseResult": {
    "query": "CARE fact-level calibration correction long-form generation SIGIR 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01FAVCwsr271rLTL3HwfQVN8",
        "content": [
          {
            "title": "Fact-Level Calibration and Correction for Long-Form Generations | Proceedings of the 48th International ACM SIGIR Conference on Research and Development in Information Retrieval",
            "url": "https://dl.acm.org/doi/10.1145/3726302.3730195"
          },
          {
            "title": "Fact-Level Calibration and Correction for Long-Form Generations | Request PDF",
            "url": "https://www.researchgate.net/publication/393657638_Fact-Level_Calibration_and_Correction_for_Long-Form_Generations"
          },
          {
            "title": "SIGIR 2025, Padua, 13-18 July | Accepted Papers - Unipd",
            "url": "https://sigir2025.dei.unipd.it/accepted-papers.html"
          },
          {
            "title": "Fact-Level Calibration and Correction for Long-Form ...",
            "url": "https://dl.acm.org/doi/pdf/10.1145/3726302.3730195"
          },
          {
            "title": "Fact Verification in Knowledge Graphs Using LLMs",
            "url": "https://www.dei.unipd.it/~silvello/papers/2025-SIGIR_Demo_LLM.pdf"
          },
          {
            "title": "SIGIR-AP 2025 Tutorial Proposal:",
            "url": "https://www.researchgate.net/profile/Su_Weihang/publication/396210825_SIGIR-AP_2025_Tutorial_Proposal_Dynamic_and_Parametric_Retrieval-Augmented_Generation/links/68e2347ef3032e2b4be6b800/SIGIR-AP-2025-Tutorial-Proposal-Dynamic-and-Parametric-Retrieval-Augmented-Generation.pdf"
          },
          {
            "title": "SIGIR-AP 2025",
            "url": "https://www.sigir-ap.org/sigir-ap-2025/accepted-papers/index.html"
          },
          {
            "title": "(PDF) SIGIR 2025 -- LiveRAG Challenge Report",
            "url": "https://www.researchgate.net/publication/393477229_SIGIR_2025_--_LiveRAG_Challenge_Report"
          },
          {
            "title": "The Great Nugget Recall: Automating Fact Extraction and RAG Evaluation with Large Language Models | Request PDF",
            "url": "https://www.researchgate.net/publication/393658928_The_Great_Nugget_Recall_Automating_Fact_Extraction_and_RAG_Evaluation_with_Large_Language_Models"
          },
          {
            "title": "Fact-Level Confidence Calibration and Self-Correction",
            "url": "https://arxiv.org/html/2411.13343v1"
          }
        ]
      },
      "Based on the search results, I found information about the paper you're looking for:\n\n## Fact-Level Calibration and Correction for Long-Form Generations (SIGIR 2025)\n\nCARE (Confidence-Aware Fact Correction) is a method that leverages high-confidence facts to iteratively refine and correct low-confidence ones.\n\n**Paper Details:**\n- Authors: Yige Yuan, Bingbing Xu, Hexiang Tan, Fei Sun, Teng Xiao, Wei Li, Huawei Shen, Xueqi Cheng\n- Conference: SIGIR '25: The 48th International ACM SIGIR Conference on Research and Development in Information Retrieval\n\n**Research Focus:**\n\nLarge language models have achieved remarkable progress across various domains, yet their tendency to generate hallucinations remains a critical barrier to their practical reliability. Confidence calibration addresses this challenge by aligning a model's confidence with its actual accuracy, improving self-evaluation and trustworthiness.\n\nThe paper proposes a fact-level confidence calibration framework that evaluates and adjusts confidence at the granularity of individual facts, incorporating both relevance and correctness. This framework identifies finer-grained calibration discrepancies, reduces overconfidence, and reveals confidence variance.\n\nExperimental results demonstrate that CARE effectively improves the quality of generated content. The code is available at https://github.com/yuanyige/fact-calibration."
    ],
    "durationSeconds": 7.056490228000097
  },
  "sourceToolAssistantUUID": "c7a8ae6d-1633-49c1-9ddb-0cd66e573e7b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 30 · 2026-05-15T14:20:54.773Z_

```json
{
  "parentUuid": "8651cc72-e6a1-4f22-abf4-462f73f4ca66",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "fafc4917-2642-4580-ad3f-43e001b1e82b",
  "timestamp": "2026-05-15T14:20:54.773Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 31 · 2026-05-15T14:21:04.971Z_

<details><summary>Logged reasoning block</summary>

```text
Good. Let me now gather more information. Key findings so far:

1. "A Single Direction of Truth" (O'Neill et al., July 2025) — uses linear probes + steering for hallucination control, but critically uses an *external observer model* (not self-probing) and tests on Gemma-2 models. The proposal is about self-probing within the generating model for calibrated confidence (not binary hallucination), at claim-level granularity in long-form generation. This is a relevant competitor but the differentiation is clear.


2. CARE (SIGIR 2025) — another fact-level calibration approach for long-form generation, though it operates through a different mechanism without probing or steering.

I also need to flag a resource constraint: the compute budget for manual mode runs to about 250 H100-hours, which exceeds the hard limit of 200 H100-hours. The AAAI 2027 deadline is confirmed for July 21 (abstract) and July 28 (full paper), and I should verify the ARR August 2026 submission window as well.

On the model selection front, the Qwen 3.5-27B issue from the previous round was already addressed by switching to Llama 3.1-70B, so that's resolved. Let me do a final sweep for any other critical papers I might have missed.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fafc4917-2642-4580-ad3f-43e001b1e82b",
  "isSidechain": false,
  "requestId": "req_011Cb4W6Yqgptr6h29ZYmd8C",
  "type": "assistant",
  "uuid": "626d6e04-5479-4637-ad76-ae78a516b199",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PkoyYze9UkeJHVVFs2hkvL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 619,
      "cache_creation_input_tokens": 2092,
      "cache_read_input_tokens": 43679,
      "output_tokens": 523,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2092,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 619,
          "output_tokens": 523,
          "cache_read_input_tokens": 43679,
          "cache_creation_input_tokens": 2092,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2092
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

_source line 32 · 2026-05-15T14:21:04.988Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01H7tvaPVsoLa5ESkkJTeXtb`</summary>

```json
{
  "query": "ARR August 2026 submission deadline ACL rolling review"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "626d6e04-5479-4637-ad76-ae78a516b199",
  "isSidechain": false,
  "requestId": "req_011Cb4W6Yqgptr6h29ZYmd8C",
  "type": "assistant",
  "uuid": "d702d262-e271-4a10-bef6-cc4b5591025a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PkoyYze9UkeJHVVFs2hkvL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 619,
      "cache_creation_input_tokens": 2092,
      "cache_read_input_tokens": 43679,
      "output_tokens": 523,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2092,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 619,
          "output_tokens": 523,
          "cache_read_input_tokens": 43679,
          "cache_creation_input_tokens": 2092,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2092
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

_source line 33 · 2026-05-15T14:21:05.473Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VyDqZXssPEz4GuMZTZmGqW`</summary>

```json
{
  "query": "\"probe guided\" \"long-form generation\" calibration steering 2026 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d702d262-e271-4a10-bef6-cc4b5591025a",
  "isSidechain": false,
  "requestId": "req_011Cb4W6Yqgptr6h29ZYmd8C",
  "type": "assistant",
  "uuid": "012ae15c-a59e-4816-a23e-864995597f3a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PkoyYze9UkeJHVVFs2hkvL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 619,
      "cache_creation_input_tokens": 2092,
      "cache_read_input_tokens": 43679,
      "output_tokens": 523,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2092,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 619,
          "output_tokens": 523,
          "cache_read_input_tokens": 43679,
          "cache_creation_input_tokens": 2092,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2092
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

_source line 34 · 2026-05-15T14:21:05.786Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01982SLUbGfD6WH6i8ECShjT`</summary>

```json
{
  "query": "Llama 3.1 70B activation steering linear probes factuality 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "012ae15c-a59e-4816-a23e-864995597f3a",
  "isSidechain": false,
  "requestId": "req_011Cb4W6Yqgptr6h29ZYmd8C",
  "type": "assistant",
  "uuid": "63f9e43d-7801-4d7a-a8fb-d393bfde450d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PkoyYze9UkeJHVVFs2hkvL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 619,
      "cache_creation_input_tokens": 2092,
      "cache_read_input_tokens": 43679,
      "output_tokens": 523,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2092,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 619,
          "output_tokens": 523,
          "cache_read_input_tokens": 43679,
          "cache_creation_input_tokens": 2092,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2092
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

_source line 35_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-15 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "63f9e43d-7801-4d7a-a8fb-d393bfde450d",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19"
}
```

---

### Runtime record

_source line 36_

```json
{
  "type": "ai-title",
  "aiTitle": "Claim-level confidence calibration for long-form LLM generation",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19"
}
```

---

### Tool result

_source line 37 · 2026-05-15T14:21:09.352Z_

<details><summary>↩ Tool result · `toolu_01H7tvaPVsoLa5ESkkJTeXtb`</summary>

```text
Web search results for query: "ARR August 2026 submission deadline ACL rolling review"

Links: [{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"aclrollingreview/dates.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/dates.md"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ACL ARR | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"ACL ARR 2026 March | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR%2F2026%2FMarch"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"}]

Based on the search results, here's what I found regarding ARR August 2026 submission deadline for ACL Rolling Review:

The August 2026 ARR cycle has an August 3 submission deadline. According to the official ARR dates and venues information, for EACL 2027, the final ARR submission date is August 3, 2026, with a commitment date of October 11, 2026.

ARR switched to 10-week review cycles starting in May 2025, which changed the review timeline compared to the previous 8-week cycles that ran earlier.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d702d262-e271-4a10-bef6-cc4b5591025a",
  "isSidechain": false,
  "promptId": "d0af2fce-b877-4a83-b1a2-3e65f7ded303",
  "type": "user",
  "uuid": "a467188a-e7aa-4f47-be48-5d9e8318e7b3",
  "toolUseResult": {
    "query": "ARR August 2026 submission deadline ACL rolling review",
    "results": [
      {
        "tool_use_id": "srvtoolu_014Gh77y3ss7iUvweKitEr7V",
        "content": [
          {
            "title": "Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/dates"
          },
          {
            "title": "CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/cfp"
          },
          {
            "title": "aclrollingreview/dates.md at main · acl-org/aclrollingreview",
            "url": "https://github.com/acl-org/aclrollingreview/blob/main/dates.md"
          },
          {
            "title": "ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/"
          },
          {
            "title": "ACL ARR | OpenReview",
            "url": "https://openreview.net/group?id=aclweb.org%2FACL%2FARR"
          },
          {
            "title": "Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/authors"
          },
          {
            "title": "Main Conference - ACL 2026",
            "url": "https://2026.aclweb.org/calls/main_conference_papers/"
          },
          {
            "title": "ACL ARR 2026 March | OpenReview",
            "url": "https://openreview.net/group?id=aclweb.org%2FACL%2FARR%2F2026%2FMarch"
          },
          {
            "title": "Call for Main Conference Papers -",
            "url": "https://2026.eacl.org/calls/papers/"
          },
          {
            "title": "Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/incentives2026"
          }
        ]
      },
      "Based on the search results, here's what I found regarding ARR August 2026 submission deadline for ACL Rolling Review:\n\nThe August 2026 ARR cycle has an August 3 submission deadline. According to the official ARR dates and venues information, for EACL 2027, the final ARR submission date is August 3, 2026, with a commitment date of October 11, 2026.\n\nARR switched to 10-week review cycles starting in May 2025, which changed the review timeline compared to the previous 8-week cycles that ran earlier."
    ],
    "durationSeconds": 4.360789430000004
  },
  "sourceToolAssistantUUID": "d702d262-e271-4a10-bef6-cc4b5591025a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-15T14:21:13.208Z_

<details><summary>↩ Tool result · `toolu_01982SLUbGfD6WH6i8ECShjT`</summary>

```text
Web search results for query: "Llama 3.1 70B activation steering linear probes factuality 2026"

Links: [{"title":"Mapping the Latent Space of Llama 3.3 70B","url":"https://www.goodfire.ai/research/mapping-latent-spaces-llama"},{"title":"[2512.17639] Linear Personality Probing and Steering in LLMs: A Big Five Study","url":"https://arxiv.org/abs/2512.17639"},{"title":"Simple Factuality Probes Detect Hallucinations in Long- ...","url":"https://aclanthology.org/2025.findings-emnlp.880.pdf"},{"title":"Probing and Steering Evaluation Awareness of Language Models","url":"https://arxiv.org/html/2507.01786v2"},{"title":"meta-llama/Llama-3.3-70B-Instruct · Hugging Face","url":"https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct"},{"title":"llama3.3:70b","url":"https://ollama.com/library/llama3.3:70b"},{"title":"meta-llama/Llama-3.1-70B · Hugging Face","url":"https://huggingface.co/meta-llama/Llama-3.1-70B"},{"title":"Llama 3.1 - 405B, 70B & 8B with multilinguality and long context","url":"https://huggingface.co/blog/llama31"},{"title":"meta-llama/Llama-3.1-70B-Instruct · Hugging Face","url":"https://huggingface.co/meta-llama/Llama-3.1-70B-Instruct"},{"title":"Steering Llama 2 via Contrastive Activation Addition","url":"https://www.researchgate.net/publication/384215189_Steering_Llama_2_via_Contrastive_Activation_Addition"}]

Based on the search results, here's what I found regarding activation steering, linear probes, and factuality research related to Llama models in 2026:

## Key Research on Activation Steering and Linear Probes

Research using Llama 3.3 70B has employed linear regression to learn per-layer directions in activation space for probing and steering model behavior. Linear directions aligned with trait-scores are effective probes for personality detection, while their steering capabilities strongly depend on context, producing reliable effects in forced-choice tasks but limited influence in open-ended generation or when additional context is present in the prompt.

## Factuality and Steering Trade-offs

When applying activation steering, models show that factuality slowly begins to degrade—for instance, at steering strength 0.6 most facts are correct, whereas at strength 1 many facts are incorrect. The mechanism by which factual recall is damaged by latent steering is unknown, but would be very interesting to understand.

## SAE-Based Steering and Evaluation Awareness

Steering with SAE features demonstrated partial capability recovery, but it remains unclear whether SAE steering genuinely modified model beliefs and behaviours or merely introduced more targeted noise. Recent research from 2026 also explores linear probes on Llama-3.3-70B-Instruct's activations, finding that evaluation awareness is internally represented and can be extracted through linear probes.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "63f9e43d-7801-4d7a-a8fb-d393bfde450d",
  "isSidechain": false,
  "promptId": "d0af2fce-b877-4a83-b1a2-3e65f7ded303",
  "type": "user",
  "uuid": "3e91254e-ff0f-42aa-9e05-8ce26d8d013c",
  "toolUseResult": {
    "query": "Llama 3.1 70B activation steering linear probes factuality 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01LxEXTDint1pkcvu6xw7NuG",
        "content": [
          {
            "title": "Mapping the Latent Space of Llama 3.3 70B",
            "url": "https://www.goodfire.ai/research/mapping-latent-spaces-llama"
          },
          {
            "title": "[2512.17639] Linear Personality Probing and Steering in LLMs: A Big Five Study",
            "url": "https://arxiv.org/abs/2512.17639"
          },
          {
            "title": "Simple Factuality Probes Detect Hallucinations in Long- ...",
            "url": "https://aclanthology.org/2025.findings-emnlp.880.pdf"
          },
          {
            "title": "Probing and Steering Evaluation Awareness of Language Models",
            "url": "https://arxiv.org/html/2507.01786v2"
          },
          {
            "title": "meta-llama/Llama-3.3-70B-Instruct · Hugging Face",
            "url": "https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct"
          },
          {
            "title": "llama3.3:70b",
            "url": "https://ollama.com/library/llama3.3:70b"
          },
          {
            "title": "meta-llama/Llama-3.1-70B · Hugging Face",
            "url": "https://huggingface.co/meta-llama/Llama-3.1-70B"
          },
          {
            "title": "Llama 3.1 - 405B, 70B & 8B with multilinguality and long context",
            "url": "https://huggingface.co/blog/llama31"
          },
          {
            "title": "meta-llama/Llama-3.1-70B-Instruct · Hugging Face",
            "url": "https://huggingface.co/meta-llama/Llama-3.1-70B-Instruct"
          },
          {
            "title": "Steering Llama 2 via Contrastive Activation Addition",
            "url": "https://www.researchgate.net/publication/384215189_Steering_Llama_2_via_Contrastive_Activation_Addition"
          }
        ]
      },
      "Based on the search results, here's what I found regarding activation steering, linear probes, and factuality research related to Llama models in 2026:\n\n## Key Research on Activation Steering and Linear Probes\n\nResearch using Llama 3.3 70B has employed linear regression to learn per-layer directions in activation space for probing and steering model behavior. Linear directions aligned with trait-scores are effective probes for personality detection, while their steering capabilities strongly depend on context, producing reliable effects in forced-choice tasks but limited influence in open-ended generation or when additional context is present in the prompt.\n\n## Factuality and Steering Trade-offs\n\nWhen applying activation steering, models show that factuality slowly begins to degrade—for instance, at steering strength 0.6 most facts are correct, whereas at strength 1 many facts are incorrect. The mechanism by which factual recall is damaged by latent steering is unknown, but would be very interesting to understand.\n\n## SAE-Based Steering and Evaluation Awareness\n\nSteering with SAE features demonstrated partial capability recovery, but it remains unclear whether SAE steering genuinely modified model beliefs and behaviours or merely introduced more targeted noise. Recent research from 2026 also explores linear probes on Llama-3.3-70B-Instruct's activations, finding that evaluation awareness is internally represented and can be extracted through linear probes."
    ],
    "durationSeconds": 7.418162847999949
  },
  "sourceToolAssistantUUID": "63f9e43d-7801-4d7a-a8fb-d393bfde450d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-15T14:21:13.441Z_

<details><summary>↩ Tool result · `toolu_01VyDqZXssPEz4GuMZTZmGqW`</summary>

```text
Web search results for query: ""probe guided" "long-form generation" calibration steering 2026 arxiv"

Links: [{"title":"Only Say What You Know: Calibration-Aware Generation for Long-Form Factuality","url":"https://arxiv.org/html/2605.01749"},{"title":"On Stable Long-Form Generation: Benchmarking and Mitigating Length Volatility","url":"https://arxiv.org/html/2605.01357"},{"title":"[2605.01749] Only Say What You Know: Calibration-Aware Generation for Long-Form Factuality","url":"https://arxiv.org/abs/2605.01749"},{"title":"CorrSteer: Generation-Time LLM Steering via Correlated Sparse Autoencoder Features","url":"https://arxiv.org/html/2508.12535v3"},{"title":"Reliable Control-Point Selection for Steering Reasoning in ...","url":"https://arxiv.org/pdf/2604.02113"},{"title":"A Course Correction in Steerability Evaluation: Revealing Miscalibration and Side Effects in LLMs","url":"https://arxiv.org/html/2505.23816"},{"title":"[2402.06544] Calibrating Long-form Generations from Large Language Models","url":"https://arxiv.org/abs/2402.06544"},{"title":"Predicting Where Steering Vectors Succeed","url":"https://arxiv.org/html/2604.15557v1"},{"title":"Steering Pretrained Drafters during Speculative Decoding","url":"https://arxiv.org/html/2511.09844"},{"title":"Published as a conference paper at ICLR 2026","url":"https://arxiv.org/pdf/2506.18841"}]

I found several relevant papers from the 2026 arXiv results. Here's what the search returned:

## Key Results

**Most Relevant: "Only Say What You Know: Calibration-Aware Generation for Long-Form Factuality" (2605.01749)**

This paper introduces Calibration-Aware Generation (CAG), a framework that enables end-to-end, calibration-aware generation by explicitly separating exploration from commitment, proposing an Exploration-Commitment Decoupling paradigm that disentangles knowledge exploration from final commitment. The approach is characterized by two mechanisms: calibrated exploration, where the model generates well-calibrated intermediate steps accompanied by explicit reliability estimates learned from fine-grained factuality annotations, and selective commitment for constructing final answers.

**Other Relevant Papers:**

1. "On Stable Long-Form Generation: Benchmarking and Mitigating Length Volatility" unfolds in three stages: benchmarking, probing, and mitigation, proposing VOLTBench, a novel heterogeneous-task benchmark designed to systematically quantify the length volatility of long-form generation.

2. "Reliable Control-Point Selection for Steering Reasoning" applies a stability probing methodology related to consistency-based filtering, where only boundaries where the model exhibits stable behavior are used for steering vector construction.

3. "Predicting Where Steering Vectors Succeed" validates linear steering at frontier scale with emotion concepts in Claude Sonnet 4.5 representable as linear directions with causal behavioral effects.

These papers collectively address probe-guided approaches, long-form generation, calibration, and steering mechanisms in 2026 arXiv research.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "012ae15c-a59e-4816-a23e-864995597f3a",
  "isSidechain": false,
  "promptId": "d0af2fce-b877-4a83-b1a2-3e65f7ded303",
  "type": "user",
  "uuid": "09a0c03e-a0b4-41f2-a780-a31399a8e2b6",
  "toolUseResult": {
    "query": "\"probe guided\" \"long-form generation\" calibration steering 2026 arxiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_01VKkoVxTQnB6YdunbedV5S9",
        "content": [
          {
            "title": "Only Say What You Know: Calibration-Aware Generation for Long-Form Factuality",
            "url": "https://arxiv.org/html/2605.01749"
          },
          {
            "title": "On Stable Long-Form Generation: Benchmarking and Mitigating Length Volatility",
            "url": "https://arxiv.org/html/2605.01357"
          },
          {
            "title": "[2605.01749] Only Say What You Know: Calibration-Aware Generation for Long-Form Factuality",
            "url": "https://arxiv.org/abs/2605.01749"
          },
          {
            "title": "CorrSteer: Generation-Time LLM Steering via Correlated Sparse Autoencoder Features",
            "url": "https://arxiv.org/html/2508.12535v3"
          },
          {
            "title": "Reliable Control-Point Selection for Steering Reasoning in ...",
            "url": "https://arxiv.org/pdf/2604.02113"
          },
          {
            "title": "A Course Correction in Steerability Evaluation: Revealing Miscalibration and Side Effects in LLMs",
            "url": "https://arxiv.org/html/2505.23816"
          },
          {
            "title": "[2402.06544] Calibrating Long-form Generations from Large Language Models",
            "url": "https://arxiv.org/abs/2402.06544"
          },
          {
            "title": "Predicting Where Steering Vectors Succeed",
            "url": "https://arxiv.org/html/2604.15557v1"
          },
          {
            "title": "Steering Pretrained Drafters during Speculative Decoding",
            "url": "https://arxiv.org/html/2511.09844"
          },
          {
            "title": "Published as a conference paper at ICLR 2026",
            "url": "https://arxiv.org/pdf/2506.18841"
          }
        ]
      },
      "I found several relevant papers from the 2026 arXiv results. Here's what the search returned:\n\n## Key Results\n\n**Most Relevant: \"Only Say What You Know: Calibration-Aware Generation for Long-Form Factuality\" (2605.01749)**\n\nThis paper introduces Calibration-Aware Generation (CAG), a framework that enables end-to-end, calibration-aware generation by explicitly separating exploration from commitment, proposing an Exploration-Commitment Decoupling paradigm that disentangles knowledge exploration from final commitment. The approach is characterized by two mechanisms: calibrated exploration, where the model generates well-calibrated intermediate steps accompanied by explicit reliability estimates learned from fine-grained factuality annotations, and selective commitment for constructing final answers.\n\n**Other Relevant Papers:**\n\n1. \"On Stable Long-Form Generation: Benchmarking and Mitigating Length Volatility\" unfolds in three stages: benchmarking, probing, and mitigation, proposing VOLTBench, a novel heterogeneous-task benchmark designed to systematically quantify the length volatility of long-form generation.\n\n2. \"Reliable Control-Point Selection for Steering Reasoning\" applies a stability probing methodology related to consistency-based filtering, where only boundaries where the model exhibits stable behavior are used for steering vector construction.\n\n3. \"Predicting Where Steering Vectors Succeed\" validates linear steering at frontier scale with emotion concepts in Claude Sonnet 4.5 representable as linear directions with causal behavioral effects.\n\nThese papers collectively address probe-guided approaches, long-form generation, calibration, and steering mechanisms in 2026 arXiv research."
    ],
    "durationSeconds": 7.965213446000009
  },
  "sourceToolAssistantUUID": "012ae15c-a59e-4816-a23e-864995597f3a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 40 · 2026-05-15T14:22:32.888Z_

<details><summary>Logged reasoning block</summary>

```text
Let me now check a few more things:

1. "A Single Direction of Truth" paper more carefully - I need to understand the key differences from the proposal
2. The compute budget issue (250 H100-hours exceeds the user's 200 H100-hour constraint)
3. Whether the venue deadlines are correct

Key facts I've gathered:
- AAAI 2027: abstract Jul 21, full Jul 28 — confirmed
- ARR August 2026: submission Aug 3 — confirmed
- "A Single Direction of Truth" uses an OBSERVER model's probes to detect and steer a GENERATOR model's hallucinations. This is different from self-probing.


- CARE does fact-level calibration, and while the proposal cites the related "Atomic Calibration" work, I should note whether CARE itself is referenced.

Now I'm assessing the novelty dimension. The core contribution appears to be combining claim-level factuality detection from prior work with calibrated confidence steering, which represents a specific integration of existing techniques rather than entirely new methods.

Looking at feasibility, there's a critical constraint issue: the proposal estimates around 250 H100-hours for manual mode, but the hard limit is 200 H100-hours, which creates a violation. The pilot experiment design itself looks solid though.

The timeline works for AAAI 2027 with over 10 weeks available, and using Llama 3.1-70B is sensible as a well-established baseline. The single-pass approach is also more practical than the earlier two-pass variant.

But there's a subtle technical problem I'm noticing with the steering mechanism. The span-aggregated probe scores use a sliding window over claim tokens, which introduces latency. By the time the model detects uncertainty in a claim, it's already generated confident-sounding text. The proposal mentions steering happens "at sentence boundaries," which means it kicks in after the uncertain sentence is already produced. So the hedging only applies to follow-up tokens, not retroactively to the uncertain claim itself. That's a meaningful limitation on what the approach can actually fix.

The paper would need to address this either through a look-ahead mechanism where you generate a few tokens, check for uncertainty, then back up and regenerate with steering applied, or find another way to hedge the original uncertain claim rather than just subsequent sentences.

But actually, re-reading the approach more carefully — the probe runs at every token and maintains a running mean score across the sentence. The real problem is timing: by the time you've generated "Barack Obama was born in Kenya," the hallucination is already complete in the output, even though the probe might only become confident about the error after seeing "Kenya." So you're stuck hedging forward-looking claims rather than fixing the problematic statement itself.

The steering mechanism's appeal is that it targets the confidence direction orthogonally to factual content, which in theory lets you express uncertainty without changing what's actually said. But that's also its limitation — if the model is confidently wrong, hedging doesn't fix the underlying error. The probe's real utility is calibration: making the model's expressed confidence match its actual accuracy, which only helps when the model has some internal signal of doubt to begin with.

The critical assumption here is whether the uncertainty signal emerges token-by-token during generation or only after the full claim is formed. If it's dynamic, per-token steering could gradually intensify hedging as the claim develops. The proposal leans on this but doesn't validate it.

There's also a practical constraint I need to flag: the manual mode requires 250 H100-hours, which breaks the user's 200-hour budget. The HIL approach stays within bounds at around 200 hours.

I'm also noticing some citation gaps — "A Single Direction of Truth" and CARE are both recent papers that should be referenced here, and there are several advanced steering methods that could strengthen the related work section.

Looking at the actual scores now: the novelty sits at 3.5 out of 5 because while the specific combination is original, it's essentially building on Han et al.'s probes and Miao & Ungar's steering framework. "A Single Direction of Truth" already explores probe-to-steer pipelines for hallucinations, so the gap is real but not huge. The empirical validation of orthogonality at scale does add something genuine though.

Feasibility is also 3.5 — the compute budget problem is real, but the pilot design is solid and Llama 3.1-70B is the right choice. Single-pass generation is more tractable than two-pass, though there's a timing issue: the sentence-boundary steering means uncertain claims are already generated before the uncertainty signal can influence them.

The writing itself is strong at 4 out of 5 — comprehensive, clear differentiation from prior work, good experimental design. But impact lands at 3.5 because while hallucination reduction matters, users probably want correct answers rather than hedged wrong ones, and the forward-looking nature of the steering (hedging after the claim instead of during generation) limits how much this actually helps in practice.

That averages to 3.625, which falls short of the 4.0 threshold.

Now I'm weighing whether this deserves a pass or revise. The proposal has gone through three rounds of revision and the core idea is solid — it addresses a real gap with a well-designed pilot. But there are concrete issues: the compute requirements exceed the user's constraint in most configurations, there are missing competitors like "A Single Direction of Truth" and CARE, and the sentence-boundary steering problem is a legitimate technical concern. The average score being below 4.0 tips it toward revise, even though these problems are fixable.

Actually, let me look at the compute numbers more carefully — the manual mode is 250 H100-hours against a ≤200 constraint, auto mode is 280, but the HIL mode hits exactly 200.

I should also check whether the proposal has abandoned the EMNLP 2026 deadline the user originally requested. Looking at the target venues, it's pivoted to AAAI 2027 as primary with ARR August 2026 as a backup option. That's a reasonable shift given the timeline — ARR August gives about 11 weeks from now, which is more feasible than the original May 25 ARR deadline for EMNLP 2026. EMNLP 2026 via ARR is also workable as a backup. Let me consolidate the main concerns: the compute budget exceeds the stated limit, there are two key missing baselines in the related work, the steering mechanism activates too late in generation, and the timeline doesn't align with what the user requested. All of these are addressable, so a revision recommendation makes sense. Now I'm reconsidering the novelty assessment—the core idea combines existing factuality probing with calibrated steering along a confidence direction, which is somewhat incremental but has merit depending on how the execution differentiates it.

Looking at the landscape more carefully: Han et al. uses probes with binary clamping rather than calibrated steering, Miao & Ungar applies calibrated steering but not at the claim level or for long-form text, and the other approaches either focus on hallucination detection without confidence calibration, fact-level calibration without steering, or require training. The proposed combination of claim-level probing with online calibrated steering in a single pass appears to occupy a genuine gap in the literature.

The novelty feels like a 3.5 — it's a well-motivated synthesis of existing techniques rather than a fundamentally new approach, though the orthogonality-at-scale finding does add some value. For impact, the problem itself is critical, and a training-free method would be practical, but the sentence-boundary limitation means confidence signals come after potentially problematic claims. That's useful for readers but less transformative than actually preventing hallucinations, so I'm settling on 3.5 for impact as well.

With clarity at 4.0, my average lands at 3.625, which points to a revise verdict. Now I need to identify the specific weaknesses and frame constructive feedback.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "09a0c03e-a0b4-41f2-a780-a31399a8e2b6",
  "isSidechain": false,
  "requestId": "req_011Cb4W7vi7JDGrxgcxp6Qww",
  "type": "assistant",
  "uuid": "77f41999-d6a2-4eca-b2f2-246c8bfd2f48",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AKZccagYmeyRPDJnDN6M44",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 873,
      "cache_creation_input_tokens": 2629,
      "cache_read_input_tokens": 45771,
      "output_tokens": 3563,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2629,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 873,
          "output_tokens": 3563,
          "cache_read_input_tokens": 45771,
          "cache_creation_input_tokens": 2629,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2629
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

_source line 41 · 2026-05-15T14:22:32.890Z_

Now let me check the critical technical concern about real-time probe signal timing during generation.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "77f41999-d6a2-4eca-b2f2-246c8bfd2f48",
  "isSidechain": false,
  "requestId": "req_011Cb4W7vi7JDGrxgcxp6Qww",
  "type": "assistant",
  "uuid": "49f5310f-495c-40fb-99bd-f3d9d52ccbcd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AKZccagYmeyRPDJnDN6M44",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 873,
      "cache_creation_input_tokens": 2629,
      "cache_read_input_tokens": 45771,
      "output_tokens": 3563,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2629,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 873,
          "output_tokens": 3563,
          "cache_read_input_tokens": 45771,
          "cache_creation_input_tokens": 2629,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2629
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

_source line 42 · 2026-05-15T14:22:35.131Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01G1E6YjSTPhmLbM8QwDsoT7`</summary>

```json
{
  "url": "https://arxiv.org/abs/2603.25052",
  "prompt": "I need to understand: (1) How exactly does the two-stage adaptive CAA steering work? Does it require generating the full response first, then steering in a second pass? Or is it single-pass? (2) What are the exact limitations stated in the paper? (3) Does the paper discuss how probe signals change during token-by-token generation vs. after full generation? (4) What specific models and tasks were tested?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "49f5310f-495c-40fb-99bd-f3d9d52ccbcd",
  "isSidechain": false,
  "requestId": "req_011Cb4W7vi7JDGrxgcxp6Qww",
  "type": "assistant",
  "uuid": "46bce618-ba1f-462d-b28b-4195c56c2a11",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AKZccagYmeyRPDJnDN6M44",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 873,
      "cache_creation_input_tokens": 2629,
      "cache_read_input_tokens": 45771,
      "output_tokens": 3563,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2629,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 873,
          "output_tokens": 3563,
          "cache_read_input_tokens": 45771,
          "cache_creation_input_tokens": 2629,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2629
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

_source line 43 · 2026-05-15T14:22:35.871Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01828rAkHBSmAKK7ZvqYZpdK`</summary>

```json
{
  "query": "\"hidden state\" probe signal \"during generation\" hallucination detection token-level real-time 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "46bce618-ba1f-462d-b28b-4195c56c2a11",
  "isSidechain": false,
  "requestId": "req_011Cb4W7vi7JDGrxgcxp6Qww",
  "type": "assistant",
  "uuid": "8c834813-3a48-4ba3-bc87-531dc3e1eb33",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AKZccagYmeyRPDJnDN6M44",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 873,
      "cache_creation_input_tokens": 2629,
      "cache_read_input_tokens": 45771,
      "output_tokens": 3563,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2629,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 873,
          "output_tokens": 3563,
          "cache_read_input_tokens": 45771,
          "cache_creation_input_tokens": 2629,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2629
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

_source line 44_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-15 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "8c834813-3a48-4ba3-bc87-531dc3e1eb33",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19"
}
```

---

### Runtime record

_source line 45_

```json
{
  "type": "ai-title",
  "aiTitle": "Claim-level confidence calibration for long-form LLM generation",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19"
}
```

---

### Tool result

_source line 46 · 2026-05-15T14:22:39.374Z_

<details><summary>↩ Tool result · `toolu_01G1E6YjSTPhmLbM8QwDsoT7`</summary>

```text
Based on the provided arXiv page content, I can only offer limited answers, as the abstract provides minimal technical detail:

**1. Two-stage adaptive steering mechanism:**
The abstract states they "introduce a two-stage adaptive steering pipeline that reads the model's internal accuracy estimate and steers verbalized output to match it," but the page doesn't specify whether this requires full response generation first or operates in single-pass mode.

**2. Stated limitations:**
No explicit limitations are mentioned in the abstract or metadata provided.

**3. Token-by-token generation dynamics:**
The abstract doesn't address how probe signals evolve during incremental token generation versus post-hoc analysis.

**4. Models and datasets tested:**
The abstract confirms testing "across three open-weight models and four datasets" but doesn't name them specifically on this page.

**Key finding described:** The paper identifies orthogonal encoding of calibration versus verbalized confidence signals, and introduces the "Reasoning Contamination Effect," where reasoning processes disrupt confidence verbalization and worsen miscalibration.

To obtain answers to questions 1-3 and the specific model/dataset names, you'd need to access the full PDF or HTML version linked on this page.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "46bce618-ba1f-462d-b28b-4195c56c2a11",
  "isSidechain": false,
  "promptId": "d0af2fce-b877-4a83-b1a2-3e65f7ded303",
  "type": "user",
  "uuid": "9cacdcb7-5137-43ba-9f75-f64c39d8f7bf",
  "toolUseResult": {
    "bytes": 45525,
    "code": 200,
    "codeText": "OK",
    "result": "Based on the provided arXiv page content, I can only offer limited answers, as the abstract provides minimal technical detail:\n\n**1. Two-stage adaptive steering mechanism:**\nThe abstract states they \"introduce a two-stage adaptive steering pipeline that reads the model's internal accuracy estimate and steers verbalized output to match it,\" but the page doesn't specify whether this requires full response generation first or operates in single-pass mode.\n\n**2. Stated limitations:**\nNo explicit limitations are mentioned in the abstract or metadata provided.\n\n**3. Token-by-token generation dynamics:**\nThe abstract doesn't address how probe signals evolve during incremental token generation versus post-hoc analysis.\n\n**4. Models and datasets tested:**\nThe abstract confirms testing \"across three open-weight models and four datasets\" but doesn't name them specifically on this page.\n\n**Key finding described:** The paper identifies orthogonal encoding of calibration versus verbalized confidence signals, and introduces the \"Reasoning Contamination Effect,\" where reasoning processes disrupt confidence verbalization and worsen miscalibration.\n\nTo obtain answers to questions 1-3 and the specific model/dataset names, you'd need to access the full PDF or HTML version linked on this page.",
    "durationMs": 4236,
    "url": "https://arxiv.org/abs/2603.25052"
  },
  "sourceToolAssistantUUID": "46bce618-ba1f-462d-b28b-4195c56c2a11",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-15T14:22:44.343Z_

<details><summary>↩ Tool result · `toolu_01828rAkHBSmAKK7ZvqYZpdK`</summary>

```text
Web search results for query: ""hidden state" probe signal "during generation" hallucination detection token-level real-time 2025 2026"

Links: [{"title":"Real-Time Detection of Hallucinated Entities in Long-Form Generation","url":"https://www.hallucination-probes.com/"},{"title":"Real-Time Detection of Hallucinated Entities in Long-Form Generation","url":"https://arxiv.org/html/2509.03531v1"},{"title":"HALT: Hallucination Assessment via Latent Testing","url":"https://arxiv.org/html/2601.14210v1"},{"title":"GitHub - EdinburghNLP/awesome-hallucination-detection: List of papers on hallucination detection in LLMs. · GitHub","url":"https://github.com/EdinburghNLP/awesome-hallucination-detection"},{"title":"Token-Level Truth: Real-Time Hallucination Detection for Production LLMs | vLLM Blog","url":"https://blog.vllm.ai/2025/12/14/halugate.html"},{"title":"HALP: Detecting Hallucinations in Vision-Language Models without Generating a Single Token","url":"https://arxiv.org/html/2603.05465v1"},{"title":"🚨 AI Hallucinations Are Getting Smarter — Here’s How to Catch Them in Real-Time (Even in Agentic AI Systems, 2026) | by Yash Mishra | Feb, 2026 | Medium","url":"https://medium.com/@yash.mishra0501/ai-hallucinations-are-getting-smarter-heres-how-to-catch-them-in-real-time-even-in-agentic-3d75a9fc1ab3"},{"title":"Token-Level Hallucination Detection","url":"https://www.emergentmind.com/topics/token-level-hallucination-detection"},{"title":"HALT: Hallucination Assessment via Log-probs as Time series","url":"https://arxiv.org/html/2602.02888v1"},{"title":"ICR Probe: Tracking Hidden State Dynamics for Reliable ...","url":"https://aclanthology.org/2025.acl-long.880.pdf"}]

Based on my search results, I found several relevant papers and resources on using hidden state probes for real-time, token-level hallucination detection during generation in 2025-2026:

## Key Research Areas

**Core Approach - Hidden State Probes:**

Linear probes that read hidden states from an intermediate layer of the model output hallucination probabilities for each token. For enhanced performance, LoRA adapters are also trained jointly with the probe.

**Real-Time Detection During Generation:**

Token-level hallucination detection approaches enable cheap, real-time streaming monitoring during generation. Streaming token-level detection approaches suggest a concrete path toward real-time hallucination monitoring at scale.

**Performance Results:**

Simple linear probes consistently achieve AUCs above 0.85, and LoRA probes improve even further, pushing AUCs above 0.89. LoRA probes consistently achieve greater than 0.96 AUC in short-form QA settings.

**Recent Methodologies (2025-2026):**

- Lightweight residual probes read hallucination risk directly from intermediate hidden states, with computation orders of magnitude cheaper than token generation and enabling near-instantaneous hallucination risk estimation.

- Some approaches probe each layer's residual stream to obtain scores, then aggregate across all layers to capture global information, with this aggregated signal serving as input to the probe for final hallucination detection.

**Practical Applications:**

Linear probes (or LoRA-enhanced heads) are trained on hidden activations at a late transformer layer to predict the hallucination label for each token in real time.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8c834813-3a48-4ba3-bc87-531dc3e1eb33",
  "isSidechain": false,
  "promptId": "d0af2fce-b877-4a83-b1a2-3e65f7ded303",
  "type": "user",
  "uuid": "a19e76cc-88ef-45a1-9608-a10efdb27051",
  "toolUseResult": {
    "query": "\"hidden state\" probe signal \"during generation\" hallucination detection token-level real-time 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Trb2PFsXsD4RDURZ89D3XE",
        "content": [
          {
            "title": "Real-Time Detection of Hallucinated Entities in Long-Form Generation",
            "url": "https://www.hallucination-probes.com/"
          },
          {
            "title": "Real-Time Detection of Hallucinated Entities in Long-Form Generation",
            "url": "https://arxiv.org/html/2509.03531v1"
          },
          {
            "title": "HALT: Hallucination Assessment via Latent Testing",
            "url": "https://arxiv.org/html/2601.14210v1"
          },
          {
            "title": "GitHub - EdinburghNLP/awesome-hallucination-detection: List of papers on hallucination detection in LLMs. · GitHub",
            "url": "https://github.com/EdinburghNLP/awesome-hallucination-detection"
          },
          {
            "title": "Token-Level Truth: Real-Time Hallucination Detection for Production LLMs | vLLM Blog",
            "url": "https://blog.vllm.ai/2025/12/14/halugate.html"
          },
          {
            "title": "HALP: Detecting Hallucinations in Vision-Language Models without Generating a Single Token",
            "url": "https://arxiv.org/html/2603.05465v1"
          },
          {
            "title": "🚨 AI Hallucinations Are Getting Smarter — Here’s How to Catch Them in Real-Time (Even in Agentic AI Systems, 2026) | by Yash Mishra | Feb, 2026 | Medium",
            "url": "https://medium.com/@yash.mishra0501/ai-hallucinations-are-getting-smarter-heres-how-to-catch-them-in-real-time-even-in-agentic-3d75a9fc1ab3"
          },
          {
            "title": "Token-Level Hallucination Detection",
            "url": "https://www.emergentmind.com/topics/token-level-hallucination-detection"
          },
          {
            "title": "HALT: Hallucination Assessment via Log-probs as Time series",
            "url": "https://arxiv.org/html/2602.02888v1"
          },
          {
            "title": "ICR Probe: Tracking Hidden State Dynamics for Reliable ...",
            "url": "https://aclanthology.org/2025.acl-long.880.pdf"
          }
        ]
      },
      "Based on my search results, I found several relevant papers and resources on using hidden state probes for real-time, token-level hallucination detection during generation in 2025-2026:\n\n## Key Research Areas\n\n**Core Approach - Hidden State Probes:**\n\nLinear probes that read hidden states from an intermediate layer of the model output hallucination probabilities for each token. For enhanced performance, LoRA adapters are also trained jointly with the probe.\n\n**Real-Time Detection During Generation:**\n\nToken-level hallucination detection approaches enable cheap, real-time streaming monitoring during generation. Streaming token-level detection approaches suggest a concrete path toward real-time hallucination monitoring at scale.\n\n**Performance Results:**\n\nSimple linear probes consistently achieve AUCs above 0.85, and LoRA probes improve even further, pushing AUCs above 0.89. LoRA probes consistently achieve greater than 0.96 AUC in short-form QA settings.\n\n**Recent Methodologies (2025-2026):**\n\n- Lightweight residual probes read hallucination risk directly from intermediate hidden states, with computation orders of magnitude cheaper than token generation and enabling near-instantaneous hallucination risk estimation.\n\n- Some approaches probe each layer's residual stream to obtain scores, then aggregate across all layers to capture global information, with this aggregated signal serving as input to the probe for final hallucination detection.\n\n**Practical Applications:**\n\nLinear probes (or LoRA-enhanced heads) are trained on hidden activations at a late transformer layer to predict the hallucination label for each token in real time."
    ],
    "durationSeconds": 8.469282353000017
  },
  "sourceToolAssistantUUID": "8c834813-3a48-4ba3-bc87-531dc3e1eb33",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 48 · 2026-05-15T14:23:20.934Z_

<details><summary>Logged reasoning block</summary>

```text
Good, so real-time token-level probing during generation is established as feasible. The key question for the proposal is whether you can detect that a claim is uncertain BEFORE or DURING the generation of that claim, rather than only after it's fully generated.

Let me also check: the proposal says "At sentence boundaries, evaluate the accumulated probe score against a calibrated threshold. If the probe indicates internal uncertainty...apply a steering offset along the extracted verbalized-confidence direction on subsequent tokens."

This means:
1. Generate Sentence 1 token by token (running probe at each token)


2. At the end of Sentence 1, check accumulated probe score
3. If uncertain → steer Sentence 2

But here's the issue: Sentence 1 is already fully generated with confident language by the time I evaluate it. The hedging only kicks in for Sentence 2 and beyond, which means I'm detecting uncertainty too late—after the uncertain claim has already been stated confidently. The proposal only checks at sentence boundaries, not mid-sentence, so even if the probe score drops halfway through generating Sentence 1, I wouldn't start steering until the next sentence begins.

Though there's an intriguing possibility: if the probe is picking up on prospective uncertainty—the model's internal representation of what it's about to generate, not just what it's already produced—then low probe scores during the prefix of a claim might signal an impending hallucination before it actually happens. Research suggests confidence representations are cached at answer-adjacent positions before the model verbalizes them, so the uncertainty signal could theoretically be available before the problematic content is generated. The question is whether Han et al.'s probes, which were trained on completed claims rather than prefixes, would actually be informative enough for this kind of prospective detection in long-form generation.

The technical concern seems real but manageable. The proposal could strengthen its approach by training probes on claim prefixes in addition to completed claims, using a more aggressive sliding window that triggers mid-sentence, or simply acknowledging the latency limitation and demonstrating it's acceptable in practice.

Now I'm checking the compute budget against the stated constraints. The user specified a maximum of 200 H100-hours, but the proposal's estimates exceed this across most configurations—manual at roughly 250 hours, human-in-the-loop at 200 hours right at the limit, and automated at around 280 hours. This is a significant constraint violation that needs addressing. Looking at where the compute is being allocated, the orthogonality pilot appears to be a major component.

Breaking down the costs further, I can see the probe training and direction extraction consuming significant resources, the 70B generation and evaluation taking the largest chunk, plus validation and comparison work. To fit within budget, the proposal could trim ablations substantially, reduce baseline comparisons, or potentially drop the 8B validation phase entirely. With some strategic scope reduction—cutting ablations and comparisons while keeping the core experiments—this could actually come in under 200 hours, so it's a fixable issue rather than a fundamental problem.

Now assessing novelty and feasibility: the approach combines claim-level probing with calibrated confidence steering in a single-pass, training-free setup, which is a genuine integration of existing techniques. While Han et al.'s probes and Miao & Ungar's steering are well-established, and prior work like "A Single Direction of Truth" and CARE have tackled related problems, the orthogonality verification at scale does add something. The novelty sits at a moderate level—it's a solid combination but not groundbreaking methodologically, so strong empirical results would be needed to justify publication at a top venue. On feasibility, the compute budget does exceed the 200-hour constraint at around 250-280 hours, though the pilot experiment is well-designed and mitigates the main technical risks. Llama 3.1-70B is a reasonable choice, and the single-pass approach is achievable, though there are some remaining constraints to work through.

The main concern is that sentence-boundary steering introduces latency between detection and response, which could affect output naturalness. The timeline for AAAI 2027 is workable with 10+ weeks available, but the scaling laws paper suggests CAA effectiveness diminishes at 70B—the adaptive approach might help but hasn't been validated yet. The proposal is well-organized and clearly differentiates from prior work with explicit quantitative targets, though the sentence-boundary latency issue could be explained more thoroughly. The core impact is solid—hallucination reduction in long-form generation is important and the training-free approach is deployable—but there's a fundamental tension: hedging happens after uncertain claims are made, which limits how natural the calibrated output feels and leaves a gap between confident-sounding wrong statements and their follow-up corrections.

The average score comes to 3.625, so this needs revision. We're in round 3 of 10, which gives room to address the main problems: the compute budget violation, the missing "A Single Direction of Truth" competitor, the sentence-boundary steering latency, and acknowledging CARE.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a19e76cc-88ef-45a1-9608-a10efdb27051",
  "isSidechain": false,
  "requestId": "req_011Cb4WEdKYAJQsmcRZ5qVcT",
  "type": "assistant",
  "uuid": "02e853a8-1b92-487e-8307-069f096378a7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018GEpbnZ3rLPawUCh7JUZ1W",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5679,
      "cache_read_input_tokens": 48400,
      "output_tokens": 1824,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5679,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1824,
          "cache_read_input_tokens": 48400,
          "cache_creation_input_tokens": 5679,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5679
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

_source line 49 · 2026-05-15T14:23:20.941Z_

Now let me verify one more critical issue — whether the proposal's sentence-boundary steering approach has a fundamental detection latency problem.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "02e853a8-1b92-487e-8307-069f096378a7",
  "isSidechain": false,
  "requestId": "req_011Cb4WEdKYAJQsmcRZ5qVcT",
  "type": "assistant",
  "uuid": "710174a2-e3f6-40b5-b675-e0272b52ef3b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018GEpbnZ3rLPawUCh7JUZ1W",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5679,
      "cache_read_input_tokens": 48400,
      "output_tokens": 1824,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5679,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1824,
          "cache_read_input_tokens": 48400,
          "cache_creation_input_tokens": 5679,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5679
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

_source line 50 · 2026-05-15T14:23:23.974Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Ka9ucivuj7bjUhcrrhZ1aY`</summary>

```json
{
  "url": "https://arxiv.org/abs/2509.03531",
  "prompt": "This is the Obeso et al. paper on real-time detection of hallucinated entities in long-form generation. I need to know: (1) Do the probes detect hallucinations DURING generation (before the claim is complete) or only AFTER the claim token is generated? (2) How early in the generation of a claim can the probe detect that it will be a hallucination? (3) What is the detection latency — can probes detect uncertainty from prefix tokens before the hallucinated content appears?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "710174a2-e3f6-40b5-b675-e0272b52ef3b",
  "isSidechain": false,
  "requestId": "req_011Cb4WEdKYAJQsmcRZ5qVcT",
  "type": "assistant",
  "uuid": "bf2fd1bd-2f8e-4e34-b34e-ecf6c0aaf36b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018GEpbnZ3rLPawUCh7JUZ1W",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5679,
      "cache_read_input_tokens": 48400,
      "output_tokens": 1824,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5679,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1824,
          "cache_read_input_tokens": 48400,
          "cache_creation_input_tokens": 5679,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5679
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

_source line 51 · 2026-05-15T14:23:24.603Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01J8aCmeZTCXD9AUTXKjR3jB`</summary>

```json
{
  "query": "\"A Single Direction of Truth\" \"observer model\" probe steering hallucination O'Neill 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bf2fd1bd-2f8e-4e34-b34e-ecf6c0aaf36b",
  "isSidechain": false,
  "requestId": "req_011Cb4WEdKYAJQsmcRZ5qVcT",
  "type": "assistant",
  "uuid": "3dc10019-1293-4c80-be1b-5d41939933de",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018GEpbnZ3rLPawUCh7JUZ1W",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5679,
      "cache_read_input_tokens": 48400,
      "output_tokens": 1824,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5679,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1824,
          "cache_read_input_tokens": 48400,
          "cache_creation_input_tokens": 5679,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5679
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

_source line 52 · 2026-05-15T14:23:27.148Z_

<details><summary>↩ Tool result · `toolu_01Ka9ucivuj7bjUhcrrhZ1aY`</summary>

```text
Based on the provided arXiv page content, I cannot answer your specific questions about detection timing and latency.

The abstract describes the method as enabling "streaming detection" and targeting "token-level labels," but it does not specify whether detection occurs during generation (before completion) or after token generation, nor does it provide information about detection latency or how early hallucinations can be identified within a claim.

The page content states: "Our approach targets entity-level hallucinations...thereby naturally mapping to token-level labels and enabling streaming detection." However, this indicates the capability for streaming, not the precise temporal mechanics you're asking about.

To answer your three specific questions about detection timing, early warning capability, and latency, you would need to consult the full paper PDF rather than this abstract summary.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bf2fd1bd-2f8e-4e34-b34e-ecf6c0aaf36b",
  "isSidechain": false,
  "promptId": "d0af2fce-b877-4a83-b1a2-3e65f7ded303",
  "type": "user",
  "uuid": "d5031e04-1c26-47e7-8e8b-aef20e883ee0",
  "toolUseResult": {
    "bytes": 48009,
    "code": 200,
    "codeText": "OK",
    "result": "Based on the provided arXiv page content, I cannot answer your specific questions about detection timing and latency.\n\nThe abstract describes the method as enabling \"streaming detection\" and targeting \"token-level labels,\" but it does not specify whether detection occurs during generation (before completion) or after token generation, nor does it provide information about detection latency or how early hallucinations can be identified within a claim.\n\nThe page content states: \"Our approach targets entity-level hallucinations...thereby naturally mapping to token-level labels and enabling streaming detection.\" However, this indicates the capability for streaming, not the precise temporal mechanics you're asking about.\n\nTo answer your three specific questions about detection timing, early warning capability, and latency, you would need to consult the full paper PDF rather than this abstract summary.",
    "durationMs": 3168,
    "url": "https://arxiv.org/abs/2509.03531"
  },
  "sourceToolAssistantUUID": "bf2fd1bd-2f8e-4e34-b34e-ecf6c0aaf36b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 53 · 2026-05-15T14:23:31.928Z_

<details><summary>↩ Tool result · `toolu_01J8aCmeZTCXD9AUTXKjR3jB`</summary>

```text
Web search results for query: ""A Single Direction of Truth" "observer model" probe steering hallucination O'Neill 2025"

Links: [{"title":"[2507.23221] A Single Direction of Truth: An Observer Model's Linear Residual Probe Exposes and Steers Contextual Hallucinations","url":"https://arxiv.org/abs/2507.23221"},{"title":"A Single Direction of Truth: An Observer Model’s Linear Residual Probe Exposes and Steers Contextual Hallucinations","url":"https://arxiv.org/html/2507.23221v1"},{"title":"A Single Direction of Truth: An Observer Model’s Linear Residual Probe","url":"https://arxiv.org/pdf/2507.23221"},{"title":"Computer Science Jul 2025","url":"https://arxiv.org/list/cs/2025-07?skip=10600&show=25"},{"title":"Published as a conference paper at ICLR 2025","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/c1c44e46358e0fb94dc94ec495a7fb1a-Paper-Conference.pdf"},{"title":"Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations","url":"https://arxiv.org/html/2503.14477v1"},{"title":"Steering Hallucination in LVLMs via Representation ...","url":"https://aclanthology.org/2025.emnlp-main.725.pdf"},{"title":"Dynamic Multimodal Activation Steering for Hallucination ...","url":"https://arxiv.org/pdf/2602.21704"},{"title":"Adaptive Activation Steering: A Tuning-Free LLM Truthfulness Improvement Method for Diverse Hallucinations Categories","url":"https://arxiv.org/html/2406.00034v2"},{"title":"Simple Factuality Probes Detect Hallucinations in Long- ...","url":"https://aclanthology.org/2025.findings-emnlp.880.pdf"}]

Based on the search results, I found the paper you're looking for:

**"A Single Direction of Truth: An Observer Model's Linear Residual Probe Exposes and Steers Contextual Hallucinations"** is an arXiv paper authored by Charles O'Neill and colleagues, posted on July 31, 2025.

## Key Findings

The research demonstrates a practical interpretability insight: a generator-agnostic observer model detects hallucinations via a single forward pass and a linear probe on its residual stream.

The probe isolates a single, transferable linear direction separating hallucinated from faithful text, outperforming baselines by 5-27 points and showing robust mid-layer performance across Gemma-2 models (2B to 27B).

## Actionability

Manipulating this direction causally steers generator hallucination rates, proving its actionability. Gradient-times-activation localises this signal to sparse, late-layer MLP activity.

## Contribution

The results offer novel evidence of internal, low-dimensional hallucination tracking linked to specific MLP sub-circuits, exploitable for detection and mitigation. The authors release the 2000-example ContraTales benchmark for realistic assessment of such solutions.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3dc10019-1293-4c80-be1b-5d41939933de",
  "isSidechain": false,
  "promptId": "d0af2fce-b877-4a83-b1a2-3e65f7ded303",
  "type": "user",
  "uuid": "6d1b38b5-d382-478d-a683-0bfaa116f6a3",
  "toolUseResult": {
    "query": "\"A Single Direction of Truth\" \"observer model\" probe steering hallucination O'Neill 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01GWqAmdrctDj7hopDZy68N5",
        "content": [
          {
            "title": "[2507.23221] A Single Direction of Truth: An Observer Model's Linear Residual Probe Exposes and Steers Contextual Hallucinations",
            "url": "https://arxiv.org/abs/2507.23221"
          },
          {
            "title": "A Single Direction of Truth: An Observer Model’s Linear Residual Probe Exposes and Steers Contextual Hallucinations",
            "url": "https://arxiv.org/html/2507.23221v1"
          },
          {
            "title": "A Single Direction of Truth: An Observer Model’s Linear Residual Probe",
            "url": "https://arxiv.org/pdf/2507.23221"
          },
          {
            "title": "Computer Science Jul 2025",
            "url": "https://arxiv.org/list/cs/2025-07?skip=10600&show=25"
          },
          {
            "title": "Published as a conference paper at ICLR 2025",
            "url": "https://proceedings.iclr.cc/paper_files/paper/2025/file/c1c44e46358e0fb94dc94ec495a7fb1a-Paper-Conference.pdf"
          },
          {
            "title": "Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations",
            "url": "https://arxiv.org/html/2503.14477v1"
          },
          {
            "title": "Steering Hallucination in LVLMs via Representation ...",
            "url": "https://aclanthology.org/2025.emnlp-main.725.pdf"
          },
          {
            "title": "Dynamic Multimodal Activation Steering for Hallucination ...",
            "url": "https://arxiv.org/pdf/2602.21704"
          },
          {
            "title": "Adaptive Activation Steering: A Tuning-Free LLM Truthfulness Improvement Method for Diverse Hallucinations Categories",
            "url": "https://arxiv.org/html/2406.00034v2"
          },
          {
            "title": "Simple Factuality Probes Detect Hallucinations in Long- ...",
            "url": "https://aclanthology.org/2025.findings-emnlp.880.pdf"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for:\n\n**\"A Single Direction of Truth: An Observer Model's Linear Residual Probe Exposes and Steers Contextual Hallucinations\"** is an arXiv paper authored by Charles O'Neill and colleagues, posted on July 31, 2025.\n\n## Key Findings\n\nThe research demonstrates a practical interpretability insight: a generator-agnostic observer model detects hallucinations via a single forward pass and a linear probe on its residual stream.\n\nThe probe isolates a single, transferable linear direction separating hallucinated from faithful text, outperforming baselines by 5-27 points and showing robust mid-layer performance across Gemma-2 models (2B to 27B).\n\n## Actionability\n\nManipulating this direction causally steers generator hallucination rates, proving its actionability. Gradient-times-activation localises this signal to sparse, late-layer MLP activity.\n\n## Contribution\n\nThe results offer novel evidence of internal, low-dimensional hallucination tracking linked to specific MLP sub-circuits, exploitable for detection and mitigation. The authors release the 2000-example ContraTales benchmark for realistic assessment of such solutions."
    ],
    "durationSeconds": 7.321699976000003
  },
  "sourceToolAssistantUUID": "3dc10019-1293-4c80-be1b-5d41939933de",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 54_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-15 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "6d1b38b5-d382-478d-a683-0bfaa116f6a3",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19"
}
```

---

### Runtime record

_source line 55_

```json
{
  "type": "ai-title",
  "aiTitle": "Claim-level confidence calibration for long-form LLM generation",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19"
}
```

---

### Assistant

_source line 56 · 2026-05-15T14:24:03.933Z_

<details><summary>Logged reasoning block</summary>

```text
OK, I now have a clear picture. Let me also note that "A Single Direction of Truth" uses an OBSERVER model (separate from the generator), which is fundamentally different from the proposal's self-probing approach. The observer reads the generator's output text, probes its own hidden states, and identifies a hallucination direction. Then that direction can be injected into the generator to steer it. This is a different paradigm from self-probing.

The proposal's approach probes the GENERATING model's own hidden states during generation — no observer needed. This is a meaningful difference.

However, it's still a significant related work that should be cited.


I see the Atomic Calibration paper is already in the references, which is good. But the CARE paper from SIGIR 2025 — a fact-level calibration and correction framework for long-form generation — isn't cited and seems directly relevant to this work. Now I'm ready to write my final review, though I'm noticing a critical issue: the compute requirements across all modes exceed the stated constraint, with manual at 250 hours, auto at 280 hours, and human-in-the-loop at 200 hours, when the user's limit is ≤200 H100-hours.

There are also two key missing competitors I need to flag. "A Single Direction of Truth" (O'Neill et al., arXiv 2507.23221) uses linear probes on an observer model's residual stream to detect hallucinations and then steers the generator via that direction — it's the closest existing probe-to-steer pipeline for hallucination control, even though it relies on an external observer rather than self-probing. And there's a latency concern with the sentence-boundary steering approach: since the method evaluates probe scores at sentence boundaries and applies steering to subsequent tokens, uncertain claims within a sentence are already generated before correction can happen.

The quantitative targets also seem potentially overoptimistic — the ≥40% claim-level ECE reduction is extrapolated from Miao & Ungar's response-level results (70-90% reduction), but claim-level ECE in long-form generation faces distinct challenges like claim boundary detection noise and probe signal dilution that could make a 40% target aggressive. There's also a venue mismatch to consider since the user requested EMNLP 2026.

Looking at the novelty score, the specific combination of claim-level probing with calibrated confidence steering in a single-pass, training-free setting for long-form generation is genuinely novel — no prior work combines these elements exactly. However, it's fundamentally built on Han et al.'s probes and Miao & Ungar's steering approach, and "A Single Direction of Truth" already demonstrated the probe-to-steer pipeline for hallucinations. The orthogonality-at-scale verification adds something empirically, but it's a modest contribution. For a top venue, the methodological novelty feels thin, so the proposal's success will hinge almost entirely on strong empirical results.

On feasibility, the compute budget is a concern — 250 hours exceeds the 200-hour constraint — and while the pilot is well-designed with Llama 3.1-70B as a sensible choice, the sentence-boundary steering latency is a genuine practical limitation. Scaling laws suggest diminishing returns for calibrated attention at 70B, though the adaptive approach might help if it works. The AAAI 2027 timeline is realistic.

The proposal is well-organized with clear differentiation from prior work and addresses previous review feedback, though the steering latency issue deserves better explanation. The training-free, single-pass approach is genuinely practical for the important problem of hallucination, but the impact is somewhat limited by these practical constraints.

The core issue is that adding hedging after uncertain claims doesn't solve the fundamental problem — there's a real gap between "the model outputs hedging text" and "the model actually knows when to be uncertain." Training-based methods might achieve better calibration, and this approach remains unproven at scale. The verdict is to revise: reduce compute to 200 hours, cite the relevant prior work on steering and calibration, either fix the latency issue or reframe it, and explore sub-sentence steering triggers as a potential improvement.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6d1b38b5-d382-478d-a683-0bfaa116f6a3",
  "isSidechain": false,
  "requestId": "req_011Cb4WJ8mvHgMwD9Db7hYYK",
  "type": "assistant",
  "uuid": "c57a8fc9-20ad-4e85-9339-31fd4bc353f2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013nCSnCXoPT5tVMneWfV5vH",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2855,
      "cache_read_input_tokens": 54079,
      "output_tokens": 3644,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2855,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3644,
          "cache_read_input_tokens": 54079,
          "cache_creation_input_tokens": 2855,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2855
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

_source line 57 · 2026-05-15T14:24:49.184Z_

I've now completed my independent verification. Let me synthesize the findings.

**Key verification results:**
- All 6 core cited papers exist and claims are accurate
- Compute budget (250h manual) exceeds user's hard ≤200 H100-hour constraint
- Critical missing competitor: "A Single Direction of Truth" (probe→steer for hallucinations)
- CARE (SIGIR 2025) — fact-level calibration in long-form — not cited
- AAAI 2027 deadlines confirmed (Jul 21 abstract, Jul 28 full)
- Sentence-boundary steering creates a fundamental detection-to-intervention latency problem

```json
{
  "verdict": "revise",
  "scores": {
    "novelty": {"score": 3.5, "rationale": "The claim-level × calibrated-confidence × long-form × single-pass × training-free combination is genuinely unexplored. However, it remains fundamentally a combination paper (Han et al.'s probes + Miao & Ungar's steering), and 'A Single Direction of Truth' (O'Neill et al., 2025) already demonstrates the probe→steer pipeline for hallucination control. The orthogonality-at-scale verification adds empirical novelty but is modest."},
    "feasibility": {"score": 3.5, "rationale": "The pilot experiment is well-designed and the Llama 3.1-70B choice is sound. However, the manual compute estimate (~250h H100) exceeds the user's hard ≤200 H100-hour constraint. The sentence-boundary steering evaluation creates a latency gap where uncertain claims are already generated with confident language before hedging activates. ICML 2025 scaling laws showing CAA diminishes at 70B remain a risk despite the adaptive formulation."},
    "clarity": {"score": 4, "rationale": "Excellent organization with comprehensive landscape coverage citing 25+ papers, clear differentiation from prior work, explicit quantitative targets, and a well-designed pilot experiment. Addresses all prior review concerns (replaced Qwen3.5, fixed two-pass, added missing citations). The strongest dimension of this proposal."},
    "impact": {"score": 3.5, "rationale": "Addresses the critical problem of hallucination in long-form generation with a practical training-free approach. However, sentence-boundary steering means hedging appears AFTER uncertain claims, not during them — producing 'confident wrong claim + follow-up hedge' rather than 'hedged claim from the start.' Competition from CURE, CAG, and LoVeC (training-based) may achieve more natural calibration."}
  },
  "issues": [
    "COMPUTE EXCEEDS CONSTRAINT: Manual mode estimates ~250h H100-hours, auto mode ~280h, and even HIL mode is at the exact 200h limit. The user's hard constraint is ≤200 H100-hours total. The breakdown shows ~38h for ablations and ~45h for baselines — both need trimming, and dropping the 8B validation track (~25h) or reducing 70B evaluation scope would help.",
    "MISSING COMPETITOR — 'A Single Direction of Truth' (O'Neill et al., arXiv 2507.23221, July 2025): Uses a linear probe on an observer model's residual stream to detect hallucinations (outperforming baselines by 5–27 points on Gemma-2 2B–27B), then uses the probe direction as a steering vector to causally reduce hallucination rates. While it uses an external observer model (vs. RaS's self-probing) and targets binary hallucination (vs. calibrated confidence), the probe→steer pipeline is very close. Must be cited with clear differentiation: RaS self-probes claim-level factuality for graded confidence calibration; O'Neill et al. use an observer model for binary hallucination detection/reduction.",
    "MISSING COMPETITOR — CARE (Yuan et al., SIGIR 2025): Fact-level calibration and correction framework for long-form generation using confidence-aware fact correction where high-confidence facts iteratively refine low-confidence ones. Directly addresses the same problem (fact-level calibration in long-form) with a different mechanism (iterative correction vs. activation steering). Must be cited.",
    "SENTENCE-BOUNDARY STEERING LATENCY: The approach evaluates accumulated probe scores 'at sentence boundaries' and applies steering to 'subsequent tokens.' This means an uncertain claim within Sentence N is generated with confident language, and hedging only appears in Sentence N+1 onward. The output reads as 'Barack Obama was born in Kenya. However, I am not fully certain about the above.' — the hallucinated claim itself remains confidently expressed. This is a fundamental design limitation that either (a) should be acknowledged as a known tradeoff, (b) mitigated with sub-sentence evaluation triggers (e.g., every K tokens or at clause boundaries), or (c) reframed as 'forward-looking uncertainty conditioning' rather than 'per-claim calibrated hedging.'",
    "QUANTITATIVE TARGETS MAY BE OVEROPTIMISTIC: The ≥40% claim-level ECE reduction target is derived by 'discounting' Miao & Ungar's response-level QA results (70–90% ECE reduction). But claim-level ECE in long-form generation faces additional challenges: noisy claim boundary detection, probe signal dilution from long-context hidden states, and the sentence-boundary steering latency. A more conservative target (e.g., ≥25% ECE reduction) would be more defensible.",
    "MISSING ADVANCED STEERING BASELINES: The proposal compares against static VUF steering but not against recent adaptive steering methods that could serve as stronger baselines: Spherical Steering (You et al., Feb 2026 — rotation-based with confidence gating), CAST (IBM, ICLR 2025 — conditional activation steering), and FLAS (Jin et al., May 2026 — flow-based activation steering). At minimum, CAST's conditional steering paradigm (apply steering only when a condition is met) is conceptually close to probe-triggered steering and should be discussed."
  ],
  "feedback": "The proposal has improved substantially since Round 1 — replacing Qwen3.5, fixing the two-pass problem, citing CORAL/CLAS/ITI/ActCab, and adding the orthogonality pilot are all strong revisions. The core gap remains real. Here are the remaining fixes:\n\n**1. Reduce compute to ≤200 H100-hours (REQUIRED):**\nThe most straightforward path: drop the 8B validation track (~25h saved), reduce ablations from 5 to 3 (~15h saved), and tighten baseline comparisons to the 2 most relevant (Han et al. neuron clamping + CURE) (~15h saved). This brings the total to ~195h. Alternatively, reduce the 70B evaluation corpus size by 30% and keep the 8B track as a lighter sanity check (~10h instead of 25h).\n\n**2. Cite 'A Single Direction of Truth' and CARE:**\nO'Neill et al. (2025) is the closest probe→steer work for hallucinations. Differentiate on three axes: (a) self-probing vs. external observer, (b) calibrated confidence vs. binary hallucination, (c) claim-level granularity in long-form vs. span-level in short contexts. CARE (SIGIR 2025) should be cited as a parallel approach to fact-level calibration that uses iterative correction rather than activation steering.\n\n**3. Address the steering latency problem (CRITICAL for technical credibility):**\nThree options, in order of preference:\n(a) **Best: Sub-sentence triggers.** Evaluate probe scores every K tokens (e.g., K=8) with a running exponential average, and trigger steering mid-sentence when the score drops below threshold. This hedges the CURRENT claim by steering later tokens in the same sentence (e.g., steering mid-generation produces 'Obama was born in — well, I believe it may have been — Kenya, though I'm not fully certain'). The cost is slightly more frequent threshold checks, which is negligible.\n(b) **Acceptable: Acknowledge and empirically measure the latency.** Report what fraction of uncertain claims get hedged within the same sentence vs. in subsequent sentences. If the probe signal rises early in claims (as Kumaran et al.'s cached-retrieval finding suggests), mid-claim steering may be feasible even with sentence-boundary triggers.\n(c) **Minimum: Reframe as 'forward-looking uncertainty conditioning.'** Acknowledge that RaS conditions subsequent generation on detected uncertainty, producing uncertainty-aware continuation rather than per-claim hedging.\n\n**4. Temper quantitative targets:**\nSet the primary ECE reduction target at ≥25% (vs. ≥40%), noting that Miao & Ungar's 70–90% reductions were on response-level QA with 7–8B models, and claim-level long-form calibration at 70B is substantially harder. Keep ≥40% as a stretch goal. This protects the paper from appearing to underperform its own targets.\n\n**5. Discuss CAST (ICLR 2025) as conceptual relative:**\nCAST's conditional activation steering (apply steering only when activation patterns match a condition) is conceptually close to probe-triggered steering. One sentence in the landscape distinguishing RaS's data-driven probe threshold from CAST's learned condition vector is sufficient.",
  "reason": "Well-constructed combination paper with genuine gap, but compute exceeds user constraint, a critical competitor is uncited, and the sentence-boundary steering latency creates a gap between claimed and actual per-claim calibration."
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c57a8fc9-20ad-4e85-9339-31fd4bc353f2",
  "isSidechain": false,
  "requestId": "req_011Cb4WJ8mvHgMwD9Db7hYYK",
  "type": "assistant",
  "uuid": "f05102f7-ad8d-4c69-93dc-519eb13e53b4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013nCSnCXoPT5tVMneWfV5vH",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2855,
      "cache_read_input_tokens": 54079,
      "output_tokens": 3644,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2855,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3644,
          "cache_read_input_tokens": 54079,
          "cache_creation_input_tokens": 2855,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2855
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

_source line 58_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-15 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "f05102f7-ad8d-4c69-93dc-519eb13e53b4",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19"
}
```

---

### Runtime record

_source line 59_

```json
{
  "type": "ai-title",
  "aiTitle": "Claim-level confidence calibration for long-form LLM generation",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19"
}
```

---
