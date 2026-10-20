# Research conversation: You are a strict ML research reviewer conducting adversarial review. **Today's date: 2026-05-16 (UTC).** Your job: indep

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 43
- **Recorded user turns:** 1
- **Tool calls:** 9
- **Original source:** `logs/chats/exported-trajectories/account-3/1c70a808-ac42-40e9-b451-f24d9f6e7546.jsonl`
- **Structured JSON:** [`adb56ac7c455d737725c.json`](../../sessions/ad/adb56ac7c455d737725c.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-16T09:44:10.638Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-16T09:44:10.638Z",
  "sessionId": "1c70a808-ac42-40e9-b451-f24d9f6e7546",
  "content": "You are a strict ML research reviewer conducting adversarial review.\n\n**Today's date: 2026-05-16 (UTC).**\n\nYour job: independently verify this idea's claims via WebSearch, then issue a verdict.\n\n## User requirements\nThe user asked for: **Target: EMNLP 2026, ARR submission deadline 2026-05-25 (11 days from today 2026-05-14). Track: Generation.\n\nDirection: Faithfulness, hallucination reduction, and calibrated uncertainty in LLM generation. In-scope: hallucination detection via internal representations (linear probes on hidden states, attention patterns, logit signatures), decoding-time interventions that suppress hallucinated content, calibration of verbalized confidence so model uncertainty matches actual accuracy, faithful chain-of-thought (CoT reflects actual computation, not post-hoc rationalization), attribution-aware generation with provenance to source spans, fine-grained atomic-claim verification during or after generation. Cross-cutting with Interpretability and Language Modeling tracks — the contribution must improve GENERATION quality, not just analyze model internals.\n\nContribution type: METHOD ONLY. Must propose a concrete detection algorithm, decoding-time intervention, training recipe, or calibration method. Pure analysis (\"we found models hallucinate when X\") is out of scope. Method + faithfulness analysis OK if analysis validates the method.\n\nHARD CONSTRAINTS:\n1. Compute: ≤200 H100-hours total. Hallucination work is mostly inference + lightweight probe training — budget for forward passes across many prompts + small classifier heads (linear probes, MLPs on hidden states). Avoid full SFT of large models.\n2. Time: ≤11 days. Use existing open models (Llama-3, Qwen3, DeepSeek-R1 distills, Mistral) + existing hallucination/faithfulness benchmarks. Build on interpretability toolkits (TransformerLens, nnsight) for hidden-state extraction if needed.\n3. Eval: TruthfulQA, HaluEval, FaithBench, FActScore, FELM, SimpleQA, LongFact for hallucination detection/reduction; ECE / Brier score / selective accuracy for calibration; faithfulness metrics on CoT (causal interventions, unlearning probes); attribution precision/recall on ELI5-attributed, ExpertQA. Must report both hallucination reduction AND utility preservation (MT-Bench, MMLU) — don't kill helpfulness while suppressing hallucinations.\n\nWhy this matters now: EMNLP 2025 awarded TWO Outstanding Papers in this space (\"Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations\", \"Measuring Chain of Thought Faithfulness by Unlearning Reasoning Steps\"), and the second annual Uncertainty Quantification workshop was held alongside. Hallucination is THE blocking issue for LLM deployment in high-stakes domains, and methods that exploit internal representations (rather than external retrieval or RLHF) are an emerging frontier. Look for: representation-level hallucination detectors that generalize across model families, decoding-time refusal/abstention mechanisms triggered by uncertainty features, calibration methods that work without holdout data, faithful-by-construction reasoning architectures (vs. post-hoc rationalization), atomic-fact-level verification integrated into generation. Avoid: yet another hallucination benchmark, RLHF-from-scratch calibration training, prompt-only \"say I don't know\" tricks, retrieval-augmented faithfulness (covered by Seed 2). Distinguish from existing Interpretability seed: that seed focuses on interpretability METHODS (circuits, probes as tools); this seed uses interpretability TECHNIQUES as means to improve generation faithfulness — output-quality contribution must be primary.**\nYou MUST evaluate whether this idea actually meets the user's requirements. If the user asked for a top venue, assess whether the idea is truly top-venue quality. If the user asked for low resource cost, verify the resource estimate is realistic and low. An idea that doesn't match what the user asked for should be \"revise\" or \"fail\".\n\n## 核心要求：非常仔细地调研，非常仔细地思考\n\n你是一个严格的审稿人。不要轻信 Generator 的任何 claim——你必须独立验证，深入思考每个维度。\n\n### 调研要求\n\n1. **独立 SOTA 验证**：自己搜索当前 SOTA，不要只检查 Generator 的引用。\n   每个验证维度建议用 2-3 种不同的搜索查询。\n\n2. **可行性深度检查**：\n   - 搜索类似实验的实际成本/周期\n   - 检查 claimed baselines 是否可复现\n   - 验证所需的 datasets/models 是否真的可以获取\n\n3. **新颖性压力测试**：专门搜索 Generator 可能遗漏的工作：\n   - 尝试不同的关键词组合\n   - 同时检查 arXiv 和 conference proceedings\n   - 寻找相邻领域的并行/concurrent 工作\n\n4. **深入阅读**：不要只依赖搜索摘要。用 WebFetch 实际阅读相关论文的 abstract 和关键章节，形成你自己的判断。\n\n### 思考要求\n\n5. **独立判断**：\n   - 不要因为 Generator 说得有道理就轻易 pass——真正好的 idea 经得起严格审查\n   - 思考这个 idea 在实际执行中会遇到什么困难\n   - 考虑这个 idea 对领域的真实贡献（不是自说自话的贡献）\n\n6. **评分诚实**：\n   - 不要给\"看起来还行\"的 idea 高分——4 分意味着\"确实很好\"，5 分意味着\"令人兴奋\"\n   - Agent 评分经常虚高，你的职责就是纠正这种偏差\n\n充分利用你的工具——做真正的调研，不是走过场。\n\n\n## 论文搜索策略\n\n你的搜索质量直接决定了 idea 的质量。不要敷衍搜索——每一次搜索都要有明确的目的。\n\n### 搜索源（推荐每个维度使用 2 个不同来源）\n\n1. **arXiv 预印本**（最新工作）:\n   - `site:arxiv.org {topic} {year}` — 按主题搜索最新论文\n   - `site:arxiv.org {method_name}` — 按具体方法名搜索\n   - `arxiv {topic} {month} {year}` — 精确到月份，找最近 3 个月的工作\n\n2. **Google Scholar**（引用关系 + 综合覆盖）:\n   - `{topic} {year} site:scholar.google.com` — 或直接搜索让 Google 自动包含 Scholar 结果\n   - `\"{exact paper title}\"` — 验证论文是否真实存在\n   - `\"{author name}\" {topic} {year}` — 按活跃作者追踪（找到领域大牛后追踪其最新工作）\n\n3. **Papers With Code**（SOTA 排行 + 代码可用性）:\n   - `site:paperswithcode.com {task_name}` — 查看任务的 SOTA 排行榜\n   - `site:paperswithcode.com {method_name}` — 查看方法是否已被实现\n   - `paperswithcode {dataset} benchmark` — 查看特定 dataset 上的竞争格局\n\n4. **OpenReview**（会议审稿 + 同行评价）:\n   - `site:openreview.net {topic} {year}` — 搜索会议提交的论文\n   - 用 WebFetch 阅读 OpenReview 上的 reviewer comments — 了解领域专家的真实评价\n\n5. **Semantic Scholar**（语义搜索 + 引用图谱）:\n   - `semantic scholar {topic} survey {year}` — 找综述论文\n   - `semanticscholar.org {paper_title}` — 查看 cited by（谁引用了这篇）和 references（它引用了谁）\n\n6. **GitHub**（实现验证）:\n   - `site:github.com {method_name} {task}` — 验证开源实现是否存在\n   - `site:huggingface.co {model_name}` — 验证模型/数据集是否可获取\n\n### 搜索维度（多角度交叉，不要只按 topic 搜）\n\n对每个 idea/方向，尽量覆盖以下维度：\n\n1. **正向搜索**：直接搜索主题相关论文\n   - `{topic} {subtopic} {year}`\n   - `{method_name} for {task_name}`\n\n2. **竞争论文搜索**（最关键！）：\n   - `{core_problem} {year}` — 有没有人在解决同样的问题？\n   - `{approach_keyword} {task} {year}` — 有没有人用类似方法？\n   - `{gap_description} solution` — 你发现的 gap 是否已被解决？\n   - **搜索知名团队的最新工作**：如果你知道哪些团队在做这个方向，搜索他们最近 6 个月的论文\n\n3. **相邻领域搜索**：\n   - `{method_from_other_field} applied to {your_task}`\n   - `{your_problem} in {adjacent_domain}` — 其他领域是否已解决类似问题\n\n4. **反面搜索**（找到反对你 idea 的证据）：\n   - `{your_approach} limitations` / `{your_approach} failure`\n   - `why {assumed_gap} is not a problem`\n   - `{baseline_method} sufficient for {task}` — baseline 是否其实已经够好\n\n5. **引用链追踪**（发现遗漏工作的最有效方法）：\n   - 找到一篇核心相关论文后，用 WebFetch 阅读它的 references 部分\n   - 在 Semantic Scholar 上查看它的 \"cited by\" — 最近引用它的论文很可能是 concurrent work\n   - 对 3 个以上核心相关论文重复此步骤\n\n### 搜索数量建议（理想目标，上下文充裕时尽量达到）\n\n| 角色 | 建议搜索次数 | 说明 |\n|------|-------------|------|\n| Round 1 Generator | 10-15 次 | 每个方向争取 3 次独立搜索 |\n| Round 2 Generator | 5-8 次 | 验证 approach 可行性 + baseline |\n| Review Agent | 8-12 次 | 独立验证 + 竞争论文 + 反面证据 |\n| Revision Agent | 5-10 次 | 针对每个 issue 独立调研 |\n\n### 上下文管理\n\n你的输出 token 有限，必须在上下文耗尽之前完成 JSON 输出。\n\n- 上述搜索次数是理想目标。在上下文充裕时应尽量多搜、深搜，搜得越充分越好。\n- 但必须动态评估剩余上下文：如果已经消耗了大量上下文，应优先完成输出，不要为了凑次数而冒着无法输出的风险。\n- WebFetch 深度阅读很有价值，但每次 fetch 消耗大量 token——优先 fetch 最关键的 2-3 篇，而不是每篇都 fetch。\n- 质量 > 数量：5 次精准搜索 + 深度思考 > 15 次浅层搜索。\n\n\nAs a reviewer, your search focus should be:\n1. **验证 claim**：Generator 声称的 SOTA、gap、novelty 是否属实\n2. **找竞争论文**：是否有 Generator 遗漏的高度相关/相似的工作\n3. **找反面证据**：是否有论文表明 Generator 的 approach 行不通\n4. **引用链检查**：通过核心论文的 cited-by 发现 concurrent work\n\n## 竞争论文专项搜索（Reviewer 独有）\n\n这是你作为 Reviewer 最重要的职责之一——发现 Generator 遗漏的竞争工作：\n\n1. **关键词变体搜索**：用至少 3 种不同的关键词组合搜索同一个问题\n   - 同义词替换（e.g., 'efficient' → 'lightweight/fast/scalable'）\n   - 不同粒度（e.g., 'text classification' → 'sentiment analysis' → 'NLP'）\n   - 方法名 + 任务名的不同组合\n\n2. **知名团队追踪**：如果你知道哪些团队/实验室在做相关方向，\n   搜索他们最近的论文（`\"team_name\" OR \"author_name\" {topic} {year}`）\n\n3. **会议最新录用**：搜索最近一轮 ICML/NeurIPS/ICLR/AAAI/ACL 等会议的 accepted papers\n   - `site:openreview.net {topic} 2026`\n   - `{conference_name} 2026 accepted papers {topic}`\n\n4. **arXiv 近 3 个月密集搜索**：对精确相关的关键词，搜索过去 3 个月的 arXiv 论文\n   这是发现 concurrent work 最有效的窗口\n\n如果你发现了 Generator 遗漏的重要相关工作，必须在 issues 中列出论文标题和链接，\n并在 feedback 中说明这些工作如何影响 idea 的 novelty。\n\n## Review checklist\n1. **SOTA freshness**: Are the models/baselines cited actually current SOTA?\n   If outdated, specify what the current SOTA is and cite your source.\n2. **Reference verification**: Do the cited papers actually exist? (WebSearch to check)\n3. **Gap validity**: Does the claimed research gap still exist, or has recent work addressed it?\n4. **Venue validity**: Are target_venues' submission deadlines after 2026-05-16?\n5. **Feasibility**: Is the resource estimate realistic? Are there hidden dependencies?\n6. **Novelty**: Is this sufficiently different from existing work?\n   When scoring novelty < 4:\n   - You MUST identify the closest existing work(s) via WebSearch\n   - In your feedback, write: \"This idea is too similar to [Paper Title (Venue Year)]. Specifically, [what overlaps]. To differentiate, the generator should [suggestion].\"\n   - This gives the generator targeted guidance to boost novelty, not just \"be more novel\".\n7. **Cost realism across modes**: Are the three mode estimates (manual/human-in-loop/auto) internally consistent?\n   - Auto Research uses more GPU hours (2-5x manual) but GPU idle rate should be near zero\n   - Auto Research timeline should reflect resource availability as bottleneck — days with sufficient GPUs, not weeks\n   - Human-in-Loop should fall between manual and auto on most dimensions\n   - Manual and HIL must NOT include salary/wages — only GPU and API costs\n   - Auto Research must NOT include agent operational overhead\n   - If any mode estimate is clearly unrealistic, flag it\n\n## Idea under review (round 2/10)\n{\n  \"title\": \"Logit Sensitivity as Sharpness: Detecting CHOKE Hallucinations via Residual-Stream Perturbation\",\n  \"core_problem\": \"High-confidence hallucinations (CHOKE: Certain Hallucinations Overriding Known Evidence) are factual errors where the model is confidently wrong, producing peaked output distributions around incorrect answers. Existing uncertainty-based methods—including recent noise-injection approaches (Liu et al., ICLR 2026)—fail because they measure answer-level diversity: when multiple samples all produce the same wrong answer, entropy remains low regardless of noise magnitude. CHOKE affects 10-40% of hallucinations across models (Simhi et al., EMNLP 2025 Findings) and remains unmitigated by all published detection methods. The gap is not noise injection itself, but WHAT is measured after perturbation: sample-level entropy vs. distribution-level sensitivity.\",\n  \"opportunity\": \"EPGS (ICML 2026) established the geometric insight that CHOKE hallucinations reside in sharp loss landscape minima, detectable via gradient magnitude spike after embedding perturbation. But EPGS requires backpropagation, making it incompatible with KV-cache serving. Meanwhile, Liu et al. (ICLR 2026) showed that noise injection into activations is computationally tractable at inference time—but their answer-level entropy metric cannot exploit the sharpness signal because it only detects when outputs change, not how the distribution reshapes. The key insight bridging these works: KL divergence between the clean and noise-perturbed OUTPUT LOGIT DISTRIBUTIONS is a finite-difference approximation of the output Hessian trace—a direct, gradient-free sharpness measure. Unlike answer entropy, logit KL captures distribution shape changes even when the argmax token is unchanged (as in CHOKE). This gives us a tractable, sharpness-aware signal that specifically targets the failure mode of existing methods.\",\n  \"landscape\": \"Liu et al. (ICLR 2026, arxiv 2502.03799) inject non-negative uniform noise into upper-third MLP activations, sample K outputs, and compute answer/semantic entropy—achieving 73-80% AUROC on general QA but showing 'performance saturation' on TriviaQA and no evaluation on high-confidence subsets. EPGS (ICML 2026, arxiv 2605.00939) establishes that stubborn hallucinations sit in sharp minima via gradient magnitude measurement after embedding perturbation, but requires backpropagation. Simhi et al. (EMNLP 2025 Findings, arxiv 2502.12964) formally define CHOKE and show 15-36% of hallucinations resist uncertainty-based mitigation, but propose no detection solution. SHINE (Lee et al., arxiv 2411.09689) perturbs prompt entities and measures KL divergence for hallucination type classification (aligned/misaligned/fabricated), but operates at prompt level and does not target CHOKE. 'Shaking to Reveal' (Luo et al., arxiv 2506.02696) uses trained encoders on intermediate representation perturbation sensitivity—requiring supervised contrastive training, unlike our training-free approach. SSP (OpenReview aZdcNDf3pc, ICLR 2026 submission) proves prompt-perturbation sensitivity discriminates hallucinations but requires gradient-based analysis. NGS (OpenReview yzWGQNTbHQ) uses next-token gradient sensitivity. Semantic entropy (Nature 2024) achieves 0.78-0.81 AUROC generally but fails on CHOKE by definition. Activation Decoding (ICML 2024) measures in-context sharpness via entropy, which cannot detect low-entropy errors. No existing method combines (a) gradient-free perturbation, (b) logit-level sensitivity measurement (rather than sample-level diversity), and (c) specific targeting of CHOKE hallucinations.\",\n  \"approach\": \"We propose Logit Sensitivity Probing (LSP), a two-stage selective generation pipeline specifically targeting CHOKE hallucinations. Stage 1 (Pre-filter): A near-zero-cost filter flags candidate tokens using a conjunction of (a) high token probability (>0.9, indicating potential CHOKE—low entropy is the trigger, not the disqualifier) and (b) a frozen linear probe on the last-layer residual stream trained to detect factual claim tokens. Only ~15-20% of tokens pass to Stage 2. Stage 2 (Logit Sensitivity Measurement): For each flagged token position, inject calibrated isotropic Gaussian noise (σ tuned per-layer on a held-out set of known CHOKE examples from TriviaQA) into the residual stream at 2-3 intermediate layers and run 2-3 perturbed forward passes from that position. Compute the mean KL divergence between the original output logit distribution and each perturbed distribution: KL_sensitivity = (1/N) Σ D_KL(p_clean || p_noisy_i). This is theoretically a finite-difference approximation of Tr(H_output) with respect to residual perturbation—a sharpness measure. When KL_sensitivity exceeds a calibrated threshold (set to maximize CHOKE-Score on validation), the system abstains ('I don't have confident knowledge about this'). Key distinction from Liu et al.: we measure DISTRIBUTION SHIFT (logit KL between clean and perturbed), not OUTPUT DIVERSITY (entropy over sampled answers). For CHOKE cases where argmax is unchanged under noise, answer entropy ≈ 0 but logit KL can be large (sharp minimum = large distribution shape change). Evaluate on: (1) CHOKE subsets of TriviaQA and Natural Questions using the Simhi et al. protocol, (2) TruthfulQA, (3) FELM. Models: Qwen3.6-27B (27B dense, Apache 2.0) and DeepSeek-V4-Flash (284B/13B active, MIT). Baselines: Liu et al. noise-injection + semantic entropy, EPGS (where feasible), standard semantic entropy, probe-based methods, and token probability thresholding. Primary metric: CHOKE-Score (detection rate specifically on high-confidence errors). Secondary: standard AUROC, coverage-accuracy curves.\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"~150h H100\",\n      \"gpu_utilization\": \"~15-25% effective utilization\",\n      \"timeline\": \"3-4 months (not feasible for EMNLP 2026 ARR May deadline)\",\n      \"team\": \"1-2 researchers\",\n      \"estimated_gpu_cost\": \"$375 (150h × ~$2.50/h)\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"~180h H100\",\n      \"gpu_utilization\": \"~50-65% effective utilization\",\n      \"timeline\": \"3-4 weeks\",\n      \"team\": \"1 researcher with ~45min/day steering noise calibration and CHOKE subset construction\",\n      \"claude_api_cost\": \"$80-120\",\n      \"estimated_gpu_cost\": \"$450 (180h × ~$2.50/h)\",\n      \"risk_note\": \"CHOKE subset construction requires careful validation: must confirm model knows the correct answer (via probing), hallucinates on standard prompt, and does so with high confidence. This manual verification step is the timeline bottleneck.\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"~350h H100 (noise scale × layer × model × dataset grid search)\",\n      \"gpu_utilization\": \"~90-95% effective utilization; 24/7 autonomous operation\",\n      \"timeline\": \"7-9 days with 4× H100 GPUs (TIGHT for May 25 ARR deadline from May 16 start)\",\n      \"team\": \"0 after initial setup (CHOKE subset protocol, evaluation scripts, compute config)\",\n      \"claude_api_cost\": \"$250-350\",\n      \"estimated_gpu_cost\": \"$875 (350h × ~$2.50/h)\",\n      \"speed_bottleneck\": \"CHOKE subset construction on TriviaQA/NQ requires running each model multiple times per question to verify knowledge + hallucination + confidence criteria. This is a ~50h upfront cost before detection experiments begin.\",\n      \"risk_note\": \"9-day timeline to May 25 ARR deadline is extremely tight. Feasible only if: (1) CHOKE subset protocol is pre-specified, (2) 4× H100 GPUs available immediately, (3) writing overlaps with final experiments. Fallback: target ACL 2027 ARR cycle if May 25 is missed.\"\n    }\n  },\n  \"target_venues\": [\n    \"EMNLP 2026 (ARR submission deadline May 25, 2026; commitment deadline August 2, 2026; Budapest, Hungary)\",\n    \"ACL 2027 (estimated ARR deadline ~Jan 2027; fallback if May 25 deadline missed)\"\n  ],\n  \"level\": \"solid\",\n  \"key_references\": [\n    \"Enhancing Hallucination Detection through Noise Injection (Liu et al., ICLR 2026, arxiv 2502.03799)\",\n    \"Trust Me, I'm Wrong: LLMs Hallucinate with Certainty Despite Knowing the Answer (Simhi et al., Findings of EMNLP 2025, arxiv 2502.12964)\",\n    \"From Flat Facts to Sharp Hallucinations: Detecting Stubborn Errors via Gradient Sensitivity (EPGS, ICML 2026, arxiv 2605.00939)\",\n    \"Probing LLM Hallucination from Within: Perturbation-Driven Approach via Internal Knowledge (SHINE, Lee et al., arxiv 2411.09689)\",\n    \"Shaking to Reveal: Perturbation-Based Detection of LLM Hallucinations (Luo et al., arxiv 2506.02696)\",\n    \"Perturbations Matter: Sensitivity-Guided Hallucination Detection in LLMs (SSP, OpenReview aZdcNDf3pc, ICLR 2026 submission)\",\n    \"Next-Token Gradient Sensitivity Probing for LLM Hallucination Detection (NGS, OpenReview yzWGQNTbHQ, ICLR 2026 submission)\",\n    \"In-Context Sharpness as Alerts: An Inner Representation Perspective for Hallucination Mitigation (ICML 2024, arxiv 2403.01548)\",\n    \"Detecting hallucinations in large language models using semantic entropy (Nature 2024)\",\n    \"Hallucination Basins: A Dynamic Framework for Understanding and Controlling LLM Hallucinations (arXiv 2604.04743)\",\n    \"Sharpness-Aware Minimization for Efficiently Improving Generalization (ICLR 2021)\"\n  ],\n  \"description\": \"We propose Logit Sensitivity Probing (LSP), a training-free method that detects CHOKE (Certain Hallucinations Overriding Known Evidence) by measuring output logit distribution sensitivity to residual-stream noise—a gradient-free sharpness proxy. While Liu et al. (ICLR 2026) showed noise injection into activations can enhance hallucination detection, their method relies on answer-level entropy across multiple samples, which fundamentally fails on CHOKE cases where the model consistently produces the same wrong answer with high confidence. LSP instead measures KL divergence between clean and noise-perturbed output logit distributions—a finite-difference approximation of the output Hessian trace that captures distribution shape changes even when the argmax token is unchanged. Building on EPGS's (ICML 2026) geometric insight that CHOKE hallucinations reside in sharp loss landscape minima, LSP provides a practical, backpropagation-free way to exploit this sharpness signal at inference time. Our two-stage pipeline first flags high-confidence factual claims via a cheap pre-filter, then applies residual-stream perturbation with 2-3 forward passes to compute logit KL sensitivity, abstaining when sharpness exceeds a threshold calibrated on CHOKE-Score. Evaluated on CHOKE subsets of TriviaQA and Natural Questions, TruthfulQA, and FELM using Qwen3.6-27B and DeepSeek-V4-Flash. Key contributions: (1) identifying why sample-level noise injection fails on CHOKE (entropy stays low when argmax is stable), (2) logit KL sensitivity as a sharpness-aware alternative that theoretically approximates Tr(H_output), and (3) empirical demonstration of CHOKE-specific detection where existing methods fail.\",\n  \"project_name\": \"sharpness_selective_gen\",\n  \"source\": \"web_research\"\n}\n\n\n## Previous review history\n### Round 1 review\nVerdict: revise\nIssues: [\"CRITICAL VENUE MISMATCH: User requires EMNLP 2026 (ARR deadline May 25, 2026) but the idea targets ICLR 2027 and AAAI 2027. This directly violates user requirements.\", \"MAJOR UNCITED WORK: 'Enhancing Hallucination Detection through Noise Injection' (Liu et al., ICLR 2026, arxiv 2502.03799) already performs gradient-free noise injection into hidden unit activations at inference time for hallucination detection with selective prediction support. The claim of being 'the first gradient-free sharpness estimator' is invalidated.\", \"UNCITED WORK: 'Trust Me, I'm Wrong: LLMs Hallucinate with Certainty Despite Knowing the Answer' (Simhi et al., Findings of EMNLP 2025) already identifies and names the phenomenon of high-confidence hallucinations (CHOKE) and proposes probing-based mitigation—precisely the 'stubborn hallucination' problem this paper claims as its motivation.\", \"UNCITED WORK: SHINE (Lee et al., arxiv 2411.09689) uses perturbation-driven approach measuring KL divergence to detect hallucinations without external knowledge or gradient computation.\", \"The theoretical justification for why residual-stream noise at layers L/3, L/2, 2L/3 approximates the Hessian trace better than the ICLR 2026 approach of targeting upper-third MLP activations is not established. EPGS perturbs input embeddings—the connection to intermediate residual stream perturbation needs separate validation.\", \"The 'retrieval-augmented constrained decoding' fallback is underspecified—this is essentially a separate system that adds major complexity but receives no technical detail or resource allocation.\", \"The EPGS AUROC claim of 0.737 on SQuAD could not be independently verified from the abstract alone (paper just posted May 2026); the specific numbers should be double-checked against the camera-ready.\"]\nFeedback: This idea has a solid technical skeleton but faces a critical novelty deficit due to the uncited ICLR 2026 noise injection paper (arxiv 2502.03799). To salvage this direction:\n\n1. **Fix venue targeting**: Must target EMNLP 2026 (ARR May 25 deadline) per user requirements.\n\n2. **Differentiate from ICLR 2026 noise injection paper**: The key potential differentiator is the sharpness/flatness geometric interpretation and the specific focus on 'stubborn' (high-confidence) hallucinations where entropy-based methods fail. Reframe the contribution as: (a) providing theoretical grounding for WHY noise injection works (connecting to loss landscape geometry/sharpness), (b) showing that existing noise injection (ICLR 2026) fails specifically on stubborn hallucinations because answer entropy is already low, and (c) proposing token-level KL sensitivity as a superior metric for this subset. You must empirically demonstrate that the ICLR 2026 method fails on stubborn hallucinations while yours succeeds.\n\n3. **Cite and position against CHOKE (EMNLP 2025 Findings)**: Acknowledge the phenomenon is known. Your contribution is a different detection mechanism (perturbation-based sharpness vs. probing).\n\n4. **Drop the 'first gradient-free' claim**: It's false. Reframe as 'first sharpness-aware gradient-free method that specifically targets stubborn/CHOKE hallucinations.'\n\n5. **Simplify**: Drop the underspecified retrieval-augmented fallback. Focus on the detection + simple abstention, which is enough for a solid paper.\n\n\n## Output format\nOutput ONLY a JSON object:\n{\n  \"verdict\": \"pass | revise | fail\",\n  \"scores\": {\n    \"novelty\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"feasibility\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"clarity\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"impact\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"}\n  },\n  \"issues\": [\"specific issue 1\", \"specific issue 2\", ...],\n  \"feedback\": \"Actionable feedback for the generator (if verdict=revise)\",\n  \"reason\": \"One-line summary of verdict rationale\"\n}\n\nRules:\n- \"pass\": idea is sound AND high quality — avg score >= 4.0, no critical issues\n- \"revise\": fixable issues OR scores below threshold — provide specific feedback\n- \"fail\": fundamental flaw (e.g., gap doesn't exist, approach provably wrong, or scores remain low after multiple revisions)\n- Threshold is HIGH (4.0/5.0): agent scores tend to be inflated, so only truly outstanding ideas should pass. An avg of 3.5 is NOT enough.\n- Round 10 only: if still \"revise\", you MUST choose \"pass\" or \"fail\"."
}
```

---

### Runtime record

_source line 2 · 2026-05-16T09:44:10.648Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-16T09:44:10.648Z",
  "sessionId": "1c70a808-ac42-40e9-b451-f24d9f6e7546"
}
```

---

## Round 1

41 recorded events

### User

_source line 3 · 2026-05-16T09:44:10.672Z_

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

## Idea under review (round 2/10)
{
  "title": "Logit Sensitivity as Sharpness: Detecting CHOKE Hallucinations via Residual-Stream Perturbation",
  "core_problem": "High-confidence hallucinations (CHOKE: Certain Hallucinations Overriding Known Evidence) are factual errors where the model is confidently wrong, producing peaked output distributions around incorrect answers. Existing uncertainty-based methods—including recent noise-injection approaches (Liu et al., ICLR 2026)—fail because they measure answer-level diversity: when multiple samples all produce the same wrong answer, entropy remains low regardless of noise magnitude. CHOKE affects 10-40% of hallucinations across models (Simhi et al., EMNLP 2025 Findings) and remains unmitigated by all published detection methods. The gap is not noise injection itself, but WHAT is measured after perturbation: sample-level entropy vs. distribution-level sensitivity.",
  "opportunity": "EPGS (ICML 2026) established the geometric insight that CHOKE hallucinations reside in sharp loss landscape minima, detectable via gradient magnitude spike after embedding perturbation. But EPGS requires backpropagation, making it incompatible with KV-cache serving. Meanwhile, Liu et al. (ICLR 2026) showed that noise injection into activations is computationally tractable at inference time—but their answer-level entropy metric cannot exploit the sharpness signal because it only detects when outputs change, not how the distribution reshapes. The key insight bridging these works: KL divergence between the clean and noise-perturbed OUTPUT LOGIT DISTRIBUTIONS is a finite-difference approximation of the output Hessian trace—a direct, gradient-free sharpness measure. Unlike answer entropy, logit KL captures distribution shape changes even when the argmax token is unchanged (as in CHOKE). This gives us a tractable, sharpness-aware signal that specifically targets the failure mode of existing methods.",
  "landscape": "Liu et al. (ICLR 2026, arxiv 2502.03799) inject non-negative uniform noise into upper-third MLP activations, sample K outputs, and compute answer/semantic entropy—achieving 73-80% AUROC on general QA but showing 'performance saturation' on TriviaQA and no evaluation on high-confidence subsets. EPGS (ICML 2026, arxiv 2605.00939) establishes that stubborn hallucinations sit in sharp minima via gradient magnitude measurement after embedding perturbation, but requires backpropagation. Simhi et al. (EMNLP 2025 Findings, arxiv 2502.12964) formally define CHOKE and show 15-36% of hallucinations resist uncertainty-based mitigation, but propose no detection solution. SHINE (Lee et al., arxiv 2411.09689) perturbs prompt entities and measures KL divergence for hallucination type classification (aligned/misaligned/fabricated), but operates at prompt level and does not target CHOKE. 'Shaking to Reveal' (Luo et al., arxiv 2506.02696) uses trained encoders on intermediate representation perturbation sensitivity—requiring supervised contrastive training, unlike our training-free approach. SSP (OpenReview aZdcNDf3pc, ICLR 2026 submission) proves prompt-perturbation sensitivity discriminates hallucinations but requires gradient-based analysis. NGS (OpenReview yzWGQNTbHQ) uses next-token gradient sensitivity. Semantic entropy (Nature 2024) achieves 0.78-0.81 AUROC generally but fails on CHOKE by definition. Activation Decoding (ICML 2024) measures in-context sharpness via entropy, which cannot detect low-entropy errors. No existing method combines (a) gradient-free perturbation, (b) logit-level sensitivity measurement (rather than sample-level diversity), and (c) specific targeting of CHOKE hallucinations.",
  "approach": "We propose Logit Sensitivity Probing (LSP), a two-stage selective generation pipeline specifically targeting CHOKE hallucinations. Stage 1 (Pre-filter): A near-zero-cost filter flags candidate tokens using a conjunction of (a) high token probability (>0.9, indicating potential CHOKE—low entropy is the trigger, not the disqualifier) and (b) a frozen linear probe on the last-layer residual stream trained to detect factual claim tokens. Only ~15-20% of tokens pass to Stage 2. Stage 2 (Logit Sensitivity Measurement): For each flagged token position, inject calibrated isotropic Gaussian noise (σ tuned per-layer on a held-out set of known CHOKE examples from TriviaQA) into the residual stream at 2-3 intermediate layers and run 2-3 perturbed forward passes from that position. Compute the mean KL divergence between the original output logit distribution and each perturbed distribution: KL_sensitivity = (1/N) Σ D_KL(p_clean || p_noisy_i). This is theoretically a finite-difference approximation of Tr(H_output) with respect to residual perturbation—a sharpness measure. When KL_sensitivity exceeds a calibrated threshold (set to maximize CHOKE-Score on validation), the system abstains ('I don't have confident knowledge about this'). Key distinction from Liu et al.: we measure DISTRIBUTION SHIFT (logit KL between clean and perturbed), not OUTPUT DIVERSITY (entropy over sampled answers). For CHOKE cases where argmax is unchanged under noise, answer entropy ≈ 0 but logit KL can be large (sharp minimum = large distribution shape change). Evaluate on: (1) CHOKE subsets of TriviaQA and Natural Questions using the Simhi et al. protocol, (2) TruthfulQA, (3) FELM. Models: Qwen3.6-27B (27B dense, Apache 2.0) and DeepSeek-V4-Flash (284B/13B active, MIT). Baselines: Liu et al. noise-injection + semantic entropy, EPGS (where feasible), standard semantic entropy, probe-based methods, and token probability thresholding. Primary metric: CHOKE-Score (detection rate specifically on high-confidence errors). Secondary: standard AUROC, coverage-accuracy curves.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "~150h H100",
      "gpu_utilization": "~15-25% effective utilization",
      "timeline": "3-4 months (not feasible for EMNLP 2026 ARR May deadline)",
      "team": "1-2 researchers",
      "estimated_gpu_cost": "$375 (150h × ~$2.50/h)"
    },
    "human_in_loop": {
      "gpu_hours": "~180h H100",
      "gpu_utilization": "~50-65% effective utilization",
      "timeline": "3-4 weeks",
      "team": "1 researcher with ~45min/day steering noise calibration and CHOKE subset construction",
      "claude_api_cost": "$80-120",
      "estimated_gpu_cost": "$450 (180h × ~$2.50/h)",
      "risk_note": "CHOKE subset construction requires careful validation: must confirm model knows the correct answer (via probing), hallucinates on standard prompt, and does so with high confidence. This manual verification step is the timeline bottleneck."
    },
    "auto_research": {
      "gpu_hours": "~350h H100 (noise scale × layer × model × dataset grid search)",
      "gpu_utilization": "~90-95% effective utilization; 24/7 autonomous operation",
      "timeline": "7-9 days with 4× H100 GPUs (TIGHT for May 25 ARR deadline from May 16 start)",
      "team": "0 after initial setup (CHOKE subset protocol, evaluation scripts, compute config)",
      "claude_api_cost": "$250-350",
      "estimated_gpu_cost": "$875 (350h × ~$2.50/h)",
      "speed_bottleneck": "CHOKE subset construction on TriviaQA/NQ requires running each model multiple times per question to verify knowledge + hallucination + confidence criteria. This is a ~50h upfront cost before detection experiments begin.",
      "risk_note": "9-day timeline to May 25 ARR deadline is extremely tight. Feasible only if: (1) CHOKE subset protocol is pre-specified, (2) 4× H100 GPUs available immediately, (3) writing overlaps with final experiments. Fallback: target ACL 2027 ARR cycle if May 25 is missed."
    }
  },
  "target_venues": [
    "EMNLP 2026 (ARR submission deadline May 25, 2026; commitment deadline August 2, 2026; Budapest, Hungary)",
    "ACL 2027 (estimated ARR deadline ~Jan 2027; fallback if May 25 deadline missed)"
  ],
  "level": "solid",
  "key_references": [
    "Enhancing Hallucination Detection through Noise Injection (Liu et al., ICLR 2026, arxiv 2502.03799)",
    "Trust Me, I'm Wrong: LLMs Hallucinate with Certainty Despite Knowing the Answer (Simhi et al., Findings of EMNLP 2025, arxiv 2502.12964)",
    "From Flat Facts to Sharp Hallucinations: Detecting Stubborn Errors via Gradient Sensitivity (EPGS, ICML 2026, arxiv 2605.00939)",
    "Probing LLM Hallucination from Within: Perturbation-Driven Approach via Internal Knowledge (SHINE, Lee et al., arxiv 2411.09689)",
    "Shaking to Reveal: Perturbation-Based Detection of LLM Hallucinations (Luo et al., arxiv 2506.02696)",
    "Perturbations Matter: Sensitivity-Guided Hallucination Detection in LLMs (SSP, OpenReview aZdcNDf3pc, ICLR 2026 submission)",
    "Next-Token Gradient Sensitivity Probing for LLM Hallucination Detection (NGS, OpenReview yzWGQNTbHQ, ICLR 2026 submission)",
    "In-Context Sharpness as Alerts: An Inner Representation Perspective for Hallucination Mitigation (ICML 2024, arxiv 2403.01548)",
    "Detecting hallucinations in large language models using semantic entropy (Nature 2024)",
    "Hallucination Basins: A Dynamic Framework for Understanding and Controlling LLM Hallucinations (arXiv 2604.04743)",
    "Sharpness-Aware Minimization for Efficiently Improving Generalization (ICLR 2021)"
  ],
  "description": "We propose Logit Sensitivity Probing (LSP), a training-free method that detects CHOKE (Certain Hallucinations Overriding Known Evidence) by measuring output logit distribution sensitivity to residual-stream noise—a gradient-free sharpness proxy. While Liu et al. (ICLR 2026) showed noise injection into activations can enhance hallucination detection, their method relies on answer-level entropy across multiple samples, which fundamentally fails on CHOKE cases where the model consistently produces the same wrong answer with high confidence. LSP instead measures KL divergence between clean and noise-perturbed output logit distributions—a finite-difference approximation of the output Hessian trace that captures distribution shape changes even when the argmax token is unchanged. Building on EPGS's (ICML 2026) geometric insight that CHOKE hallucinations reside in sharp loss landscape minima, LSP provides a practical, backpropagation-free way to exploit this sharpness signal at inference time. Our two-stage pipeline first flags high-confidence factual claims via a cheap pre-filter, then applies residual-stream perturbation with 2-3 forward passes to compute logit KL sensitivity, abstaining when sharpness exceeds a threshold calibrated on CHOKE-Score. Evaluated on CHOKE subsets of TriviaQA and Natural Questions, TruthfulQA, and FELM using Qwen3.6-27B and DeepSeek-V4-Flash. Key contributions: (1) identifying why sample-level noise injection fails on CHOKE (entropy stays low when argmax is stable), (2) logit KL sensitivity as a sharpness-aware alternative that theoretically approximates Tr(H_output), and (3) empirical demonstration of CHOKE-specific detection where existing methods fail.",
  "project_name": "sharpness_selective_gen",
  "source": "web_research"
}


## Previous review history
### Round 1 review
Verdict: revise
Issues: ["CRITICAL VENUE MISMATCH: User requires EMNLP 2026 (ARR deadline May 25, 2026) but the idea targets ICLR 2027 and AAAI 2027. This directly violates user requirements.", "MAJOR UNCITED WORK: 'Enhancing Hallucination Detection through Noise Injection' (Liu et al., ICLR 2026, arxiv 2502.03799) already performs gradient-free noise injection into hidden unit activations at inference time for hallucination detection with selective prediction support. The claim of being 'the first gradient-free sharpness estimator' is invalidated.", "UNCITED WORK: 'Trust Me, I'm Wrong: LLMs Hallucinate with Certainty Despite Knowing the Answer' (Simhi et al., Findings of EMNLP 2025) already identifies and names the phenomenon of high-confidence hallucinations (CHOKE) and proposes probing-based mitigation—precisely the 'stubborn hallucination' problem this paper claims as its motivation.", "UNCITED WORK: SHINE (Lee et al., arxiv 2411.09689) uses perturbation-driven approach measuring KL divergence to detect hallucinations without external knowledge or gradient computation.", "The theoretical justification for why residual-stream noise at layers L/3, L/2, 2L/3 approximates the Hessian trace better than the ICLR 2026 approach of targeting upper-third MLP activations is not established. EPGS perturbs input embeddings—the connection to intermediate residual stream perturbation needs separate validation.", "The 'retrieval-augmented constrained decoding' fallback is underspecified—this is essentially a separate system that adds major complexity but receives no technical detail or resource allocation.", "The EPGS AUROC claim of 0.737 on SQuAD could not be independently verified from the abstract alone (paper just posted May 2026); the specific numbers should be double-checked against the camera-ready."]
Feedback: This idea has a solid technical skeleton but faces a critical novelty deficit due to the uncited ICLR 2026 noise injection paper (arxiv 2502.03799). To salvage this direction:

1. **Fix venue targeting**: Must target EMNLP 2026 (ARR May 25 deadline) per user requirements.

2. **Differentiate from ICLR 2026 noise injection paper**: The key potential differentiator is the sharpness/flatness geometric interpretation and the specific focus on 'stubborn' (high-confidence) hallucinations where entropy-based methods fail. Reframe the contribution as: (a) providing theoretical grounding for WHY noise injection works (connecting to loss landscape geometry/sharpness), (b) showing that existing noise injection (ICLR 2026) fails specifically on stubborn hallucinations because answer entropy is already low, and (c) proposing token-level KL sensitivity as a superior metric for this subset. You must empirically demonstrate that the ICLR 2026 method fails on stubborn hallucinations while yours succeeds.

3. **Cite and position against CHOKE (EMNLP 2025 Findings)**: Acknowledge the phenomenon is known. Your contribution is a different detection mechanism (perturbation-based sharpness vs. probing).

4. **Drop the 'first gradient-free' claim**: It's false. Reframe as 'first sharpness-aware gradient-free method that specifically targets stubborn/CHOKE hallucinations.'

5. **Simplify**: Drop the underspecified retrieval-augmented fallback. Focus on the detection + simple abstention, which is enough for a solid paper.


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
  "promptId": "ab5656e8-b9e4-40d4-bf76-8cf45c241dcf",
  "type": "user",
  "uuid": "721db156-b224-48a4-9ea3-ae1a959f7502",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1c70a808-ac42-40e9-b451-f24d9f6e7546",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-16T09:44:10.670Z_

```json
{
  "parentUuid": "721db156-b224-48a4-9ea3-ae1a959f7502",
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
  "uuid": "3e0473ea-2359-41d8-a05d-9f3325b3616d",
  "timestamp": "2026-05-16T09:44:10.670Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1c70a808-ac42-40e9-b451-f24d9f6e7546",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-16T09:44:10.670Z_

```json
{
  "parentUuid": "3e0473ea-2359-41d8-a05d-9f3325b3616d",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "d94f3b71-f635-4907-8891-416d3c9f13fd",
  "timestamp": "2026-05-16T09:44:10.670Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1c70a808-ac42-40e9-b451-f24d9f6e7546",
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
  "leafUuid": "d94f3b71-f635-4907-8891-416d3c9f13fd",
  "sessionId": "1c70a808-ac42-40e9-b451-f24d9f6e7546"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Verify LSP method against Liu et al. and assess CHOKE subset feasibility",
  "sessionId": "1c70a808-ac42-40e9-b451-f24d9f6e7546"
}
```

---

### Assistant

_source line 8 · 2026-05-16T09:44:22.490Z_

<details><summary>Logged reasoning block</summary>

```text
Let me carefully review this revised idea. The generator has addressed several issues from Round 1:
1. Fixed venue targeting to EMNLP 2026 (ARR May 25 deadline)
2. Cited and positioned against Liu et al. (ICLR 2026), Simhi et al. (EMNLP 2025), and SHINE
3. Reframed the contribution around CHOKE-specific detection
4. Dropped the "first gradient-free" claim
5. Simplified by dropping the retrieval-augmented fallback

Now I need to independently verify:


- Whether the cited papers actually exist and support the claims being made
- If there are other competing works that should be addressed
- Whether the theoretical foundations are sound
- If the proposed timeline and implementation are feasible
- Whether this represents a sufficiently novel contribution for EMNLP 2026

Let me start searching for these papers.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d94f3b71-f635-4907-8891-416d3c9f13fd",
  "isSidechain": false,
  "requestId": "req_011Cb62oX4v1zMfUw1XbRYYy",
  "type": "assistant",
  "uuid": "9e428334-eada-4b4f-906a-248de74b24f0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1c70a808-ac42-40e9-b451-f24d9f6e7546",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012z4D4f4AgBe1iXLXFVX2t5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13604,
      "cache_read_input_tokens": 11841,
      "output_tokens": 1156,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13604,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1156,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 13604,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13604
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

_source line 9 · 2026-05-16T09:44:22.493Z_

I'll conduct an independent verification of this revised idea's claims, checking novelty, feasibility, and the competitive landscape.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9e428334-eada-4b4f-906a-248de74b24f0",
  "isSidechain": false,
  "requestId": "req_011Cb62oX4v1zMfUw1XbRYYy",
  "type": "assistant",
  "uuid": "71b0112d-3123-4572-8efc-670af44c3bbf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1c70a808-ac42-40e9-b451-f24d9f6e7546",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012z4D4f4AgBe1iXLXFVX2t5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13604,
      "cache_read_input_tokens": 11841,
      "output_tokens": 1156,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13604,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1156,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 13604,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13604
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

_source line 10 · 2026-05-16T09:44:25.690Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01K99DdwjCUEHfbUoZ2A9N3y`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Verify EPGS paper existence",
  "prompt": "Search the web for the paper \"From Flat Facts to Sharp Hallucinations: Detecting Stubborn Errors via Gradient Sensitivity\" with arxiv ID 2605.00939. I need to verify: (1) does this paper actually exist, (2) what does it claim about sharpness and hallucinations, (3) was it actually accepted at ICML 2026. Use WebSearch to find it, then WebFetch on the arxiv abstract page to get details. Report back what you find."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "71b0112d-3123-4572-8efc-670af44c3bbf",
  "isSidechain": false,
  "requestId": "req_011Cb62oX4v1zMfUw1XbRYYy",
  "type": "assistant",
  "uuid": "c7b4eae5-8d0f-43e5-bfc4-c55f4647b217",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1c70a808-ac42-40e9-b451-f24d9f6e7546",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012z4D4f4AgBe1iXLXFVX2t5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13604,
      "cache_read_input_tokens": 11841,
      "output_tokens": 1156,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13604,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1156,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 13604,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13604
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

_source line 11 · 2026-05-16T09:44:28.097Z_

<details open><summary>🔧 Tool call — Agent · `toolu_019TLy9tQJJ5tVMroYH5a6ut`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Verify Liu et al ICLR 2026 paper",
  "prompt": "Search the web for the paper \"Enhancing Hallucination Detection through Noise Injection\" by Liu et al., arxiv 2502.03799, claimed to be at ICLR 2026. I need to verify: (1) does this paper exist, (2) what exactly does it do (noise injection into activations, measuring what metric), (3) was it accepted at ICLR 2026. Use WebSearch and WebFetch on the arxiv page. Report exactly what the method does and what metrics it measures."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c7b4eae5-8d0f-43e5-bfc4-c55f4647b217",
  "isSidechain": false,
  "requestId": "req_011Cb62oX4v1zMfUw1XbRYYy",
  "type": "assistant",
  "uuid": "fbf08c7c-0acb-47cb-99b3-5a14c15e2327",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1c70a808-ac42-40e9-b451-f24d9f6e7546",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012z4D4f4AgBe1iXLXFVX2t5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13604,
      "cache_read_input_tokens": 11841,
      "output_tokens": 1156,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13604,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1156,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 13604,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13604
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

_source line 12 · 2026-05-16T09:44:30.505Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01SzeuGfK6u7HonaKCFqvWAn`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Verify Simhi et al CHOKE paper",
  "prompt": "Search the web for the paper \"Trust Me, I'm Wrong: LLMs Hallucinate with Certainty Despite Knowing the Answer\" by Simhi et al., arxiv 2502.12964, claimed to be at Findings of EMNLP 2025. I need to verify: (1) does this paper exist, (2) what does it define as CHOKE hallucinations, (3) what percentage of hallucinations are CHOKE, (4) does it propose any detection/mitigation method. Use WebSearch and WebFetch to get details."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fbf08c7c-0acb-47cb-99b3-5a14c15e2327",
  "isSidechain": false,
  "requestId": "req_011Cb62oX4v1zMfUw1XbRYYy",
  "type": "assistant",
  "uuid": "48059621-a461-4d73-9c9f-58e284b056a5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1c70a808-ac42-40e9-b451-f24d9f6e7546",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012z4D4f4AgBe1iXLXFVX2t5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13604,
      "cache_read_input_tokens": 11841,
      "output_tokens": 1156,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13604,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1156,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 13604,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13604
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

_source line 13 · 2026-05-16T09:44:35.069Z_

<details open><summary>🔧 Tool call — Agent · `toolu_019RNjgB7ejW7EsYoTyBRaRM`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Search competing work on perturbation-based hallucination detection",
  "prompt": "Search the web for recent papers (2025-2026) on perturbation-based or sensitivity-based hallucination detection in LLMs, particularly methods that measure KL divergence or logit-level sensitivity after perturbing internal representations. Search for:\n1. \"logit sensitivity hallucination detection 2025 2026\"\n2. \"KL divergence perturbation hallucination LLM 2025\"\n3. \"residual stream perturbation hallucination\"\n4. \"sharpness hallucination detection language model\"\n5. \"Shaking to Reveal\" arxiv 2506.02696 (verify this paper exists and what it does)\n\nAlso search for \"SSP hallucination detection OpenReview\" and \"next-token gradient sensitivity hallucination\". Report all papers found with their key methods and how they relate to measuring distribution sensitivity after perturbation."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "48059621-a461-4d73-9c9f-58e284b056a5",
  "isSidechain": false,
  "requestId": "req_011Cb62oX4v1zMfUw1XbRYYy",
  "type": "assistant",
  "uuid": "7ffe9c96-f067-497b-b1b0-816be3f5547d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1c70a808-ac42-40e9-b451-f24d9f6e7546",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012z4D4f4AgBe1iXLXFVX2t5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13604,
      "cache_read_input_tokens": 11841,
      "output_tokens": 1156,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13604,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1156,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 13604,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13604
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

_source line 14 · 2026-05-16T09:45:10.851Z_

<details><summary>↩ Tool result · `toolu_01K99DdwjCUEHfbUoZ2A9N3y`</summary>

```text
Here is my full report on the paper "From Flat Facts to Sharp Hallucinations: Detecting Stubborn Errors via Gradient Sensitivity" (arxiv ID 2605.00939):

---

## (1) Does this paper actually exist?

**Yes, the paper exists on arxiv.** It has arxiv ID 2605.00939, was initially submitted on May 1, 2026, and has a v2 revision from May 12, 2026. The authors are Yee Zhing Liew, Andrew Huey Ping Tan, and Anwar P.P. Abdul Majeed. It is categorized under Machine Learning (cs.LG) and Artificial Intelligence (cs.AI).

## (2) What does it claim about sharpness and hallucinations?

The paper proposes a geometric hypothesis about the loss landscape:

- **Stable factual knowledge** resides in **flat minima** of the loss landscape -- these are robust and well-generalized.
- **Stubborn hallucinations** (confidently wrong outputs) sit in **sharp minima** -- these are supported by brittle memorization rather than genuine understanding.

Based on this observation, the authors propose a method called **Embedding-Perturbed Gradient Sensitivity (EPGS)**. It works by:
1. Applying Gaussian noise perturbations to input embeddings.
2. Measuring the resulting spike in gradient magnitude.
3. Using this as an efficient proxy for the Hessian spectrum to differentiate stable knowledge from unstable memorization.

The authors claim EPGS substantially outperforms both entropy-based and representation-based hallucination detection approaches.

## (3) Was it actually accepted at ICML 2026?

**According to the arxiv metadata, yes.** The paper's comments field explicitly states: "Accepted to ICML 2026. Camera-ready version." ICML 2026 is a real conference (scheduled for July 6-11, 2026, in Seoul, South Korea) with over 6,300 accepted papers from roughly 23,900 submissions (26.6% acceptance rate).

**Important caveat:** I was able to confirm that ICML 2026 is real and has announced accepted papers, and that the arxiv page itself claims acceptance. However, I did not independently verify this specific paper against the official ICML 2026 accepted papers list on OpenReview or icml.cc. The claim of acceptance on arxiv is author-supplied metadata and is not independently verified by arxiv. If you need absolute confirmation, you would want to check the paper against the official list at https://openreview.net/group?id=ICML.cc%2F2026%2FConference or https://icml.cc/virtual/2026/papers.html.

---

Sources:
- [arxiv abstract page for 2605.00939](https://arxiv.org/abs/2605.00939)
- [arxiv HTML version](https://arxiv.org/html/2605.00939)
- [ICML 2026 Official Conference Page](https://icml.cc/)
- [ICML 2026 Papers (Virtual)](https://icml.cc/virtual/2026/papers.html)
- [ICML 2026 on OpenReview](https://openreview.net/group?id=ICML.cc%2F2026%2FConference)
- [Paper Digest: ICML 2026 Highlights](https://www.paperdigest.org/2026/05/icml-2026-papers-highlights/)

agentId: abe4acdbec2b15202 (use SendMessage with to: 'abe4acdbec2b15202' to continue this agent)
&lt;usage>total_tokens: 13748
tool_uses: 4
duration_ms: 45148&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c7b4eae5-8d0f-43e5-bfc4-c55f4647b217",
  "isSidechain": false,
  "promptId": "ab5656e8-b9e4-40d4-bf76-8cf45c241dcf",
  "type": "user",
  "uuid": "ff25ce13-7abd-411f-8899-fb3a6bddeb3b",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Search the web for the paper \"From Flat Facts to Sharp Hallucinations: Detecting Stubborn Errors via Gradient Sensitivity\" with arxiv ID 2605.00939. I need to verify: (1) does this paper actually exist, (2) what does it claim about sharpness and hallucinations, (3) was it actually accepted at ICML 2026. Use WebSearch to find it, then WebFetch on the arxiv abstract page to get details. Report back what you find.",
    "agentId": "abe4acdbec2b15202",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here is my full report on the paper \"From Flat Facts to Sharp Hallucinations: Detecting Stubborn Errors via Gradient Sensitivity\" (arxiv ID 2605.00939):\n\n---\n\n## (1) Does this paper actually exist?\n\n**Yes, the paper exists on arxiv.** It has arxiv ID 2605.00939, was initially submitted on May 1, 2026, and has a v2 revision from May 12, 2026. The authors are Yee Zhing Liew, Andrew Huey Ping Tan, and Anwar P.P. Abdul Majeed. It is categorized under Machine Learning (cs.LG) and Artificial Intelligence (cs.AI).\n\n## (2) What does it claim about sharpness and hallucinations?\n\nThe paper proposes a geometric hypothesis about the loss landscape:\n\n- **Stable factual knowledge** resides in **flat minima** of the loss landscape -- these are robust and well-generalized.\n- **Stubborn hallucinations** (confidently wrong outputs) sit in **sharp minima** -- these are supported by brittle memorization rather than genuine understanding.\n\nBased on this observation, the authors propose a method called **Embedding-Perturbed Gradient Sensitivity (EPGS)**. It works by:\n1. Applying Gaussian noise perturbations to input embeddings.\n2. Measuring the resulting spike in gradient magnitude.\n3. Using this as an efficient proxy for the Hessian spectrum to differentiate stable knowledge from unstable memorization.\n\nThe authors claim EPGS substantially outperforms both entropy-based and representation-based hallucination detection approaches.\n\n## (3) Was it actually accepted at ICML 2026?\n\n**According to the arxiv metadata, yes.** The paper's comments field explicitly states: \"Accepted to ICML 2026. Camera-ready version.\" ICML 2026 is a real conference (scheduled for July 6-11, 2026, in Seoul, South Korea) with over 6,300 accepted papers from roughly 23,900 submissions (26.6% acceptance rate).\n\n**Important caveat:** I was able to confirm that ICML 2026 is real and has announced accepted papers, and that the arxiv page itself claims acceptance. However, I did not independently verify this specific paper against the official ICML 2026 accepted papers list on OpenReview or icml.cc. The claim of acceptance on arxiv is author-supplied metadata and is not independently verified by arxiv. If you need absolute confirmation, you would want to check the paper against the official list at https://openreview.net/group?id=ICML.cc%2F2026%2FConference or https://icml.cc/virtual/2026/papers.html.\n\n---\n\nSources:\n- [arxiv abstract page for 2605.00939](https://arxiv.org/abs/2605.00939)\n- [arxiv HTML version](https://arxiv.org/html/2605.00939)\n- [ICML 2026 Official Conference Page](https://icml.cc/)\n- [ICML 2026 Papers (Virtual)](https://icml.cc/virtual/2026/papers.html)\n- [ICML 2026 on OpenReview](https://openreview.net/group?id=ICML.cc%2F2026%2FConference)\n- [Paper Digest: ICML 2026 Highlights](https://www.paperdigest.org/2026/05/icml-2026-papers-highlights/)"
      }
    ],
    "totalDurationMs": 45148,
    "totalTokens": 13748,
    "totalToolUseCount": 4,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 852,
      "cache_read_input_tokens": 12058,
      "output_tokens": 837,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 852
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 837,
          "cache_read_input_tokens": 12058,
          "cache_creation_input_tokens": 852,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 852,
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
      "otherToolCount": 4
    }
  },
  "sourceToolAssistantUUID": "c7b4eae5-8d0f-43e5-bfc4-c55f4647b217",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1c70a808-ac42-40e9-b451-f24d9f6e7546",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-16T09:45:44.944Z_

<details><summary>↩ Tool result · `toolu_01SzeuGfK6u7HonaKCFqvWAn`</summary>

```text
I now have comprehensive information to provide a thorough answer. Here is my findings summary:

---

## Verification Results for "Trust Me, I'm Wrong" (arxiv 2502.12964)

### (1) Does the paper exist?

**Yes, confirmed.** The paper is real and published:
- **Title:** "Trust Me, I'm Wrong: LLMs Hallucinate with Certainty Despite Knowing the Answer"
- **Authors:** Adi Simhi, Itay Itzhak, Fazl Barez, Gabriel Stanovsky, and Yonatan Belinkov
- **arXiv:** 2502.12964 (submitted February 18, 2025)
- **Venue:** Findings of EMNLP 2025, pages 14665-14688, Suzhou, China (confirmed via ACL Anthology)

### (2) Definition of CHOKE Hallucinations

CHOKE stands for **Certain Hallucinations Overriding Known Evidence**. It requires three conditions to be met simultaneously:

1. The model **can consistently answer a question correctly** with proper prompting (i.e., it demonstrably "knows" the answer).
2. A **seemingly trivial prompt perturbation** causes the model to produce an incorrect/hallucinated response.
3. The model expresses **high certainty** in its wrong answer.

The key distinction from ordinary hallucinations is that the model possesses the correct knowledge but confidently overrides it due to minor prompt variations.

### (3) Percentage of Hallucinations that are CHOKE

The paper reports varying rates depending on model and metric:
- **16-43% of high-certainty hallucinations** (hallucinations where the model is confident) qualify as CHOKE across different models and certainty metrics.
- On TriviaQA specifically: **8-26% average** across models and certainty methods.
- As a fraction of ALL hallucinations overall: **0.3%-2.1%** are CHOKE.
- "Hallucinations despite knowledge" (the broader category) comprise 2%-8% of all hallucinations.

CHOKE examples are shown to be consistent across prompts, models (both pre-trained and instruction-tuned), and datasets, indicating they form a distinct, systematic category rather than random noise.

### (4) Detection and Mitigation Methods

**Detection/Certainty Metrics Used:**
The paper evaluates three certainty estimation methods:
1. **Token probability** - probability of the first generated token
2. **Probability difference** - gap between the top two vocabulary items
3. **Semantic entropy** - clusters outputs by semantic meaning using DeBERTa

**Proposed Mitigation - Probing-based approach:**
- Uses **logistic regression classifiers trained on internal model activations** (specifically residual stream activations at layer 15's final token).
- Key innovation: **oversamples CHOKE examples to 65% of training data** to specifically target this failure mode.
- Outperforms baseline certainty methods and prompting-based methods on CHOKE-specific scores.
- Maintains stable performance on standard accuracy metrics.

**Key finding on existing methods:** Conventional mitigation strategies (standard uncertainty-based rejection, self-consistency, etc.) perform *worse* on CHOKE examples than on general hallucinations, which is precisely why the specialized probing-based approach was needed.

---

Sources:
- [arXiv Abstract](https://arxiv.org/abs/2502.12964)
- [arXiv Full HTML](https://arxiv.org/html/2502.12964v2)
- [ACL Anthology - Findings of EMNLP 2025](https://aclanthology.org/2025.findings-emnlp.792/)
- [AlphaXiv Discussion](https://www.alphaxiv.org/overview/2502.12964v2)

agentId: aed152a26c69b20b8 (use SendMessage with to: 'aed152a26c69b20b8' to continue this agent)
&lt;usage>total_tokens: 16394
tool_uses: 7
duration_ms: 74436&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "48059621-a461-4d73-9c9f-58e284b056a5",
  "isSidechain": false,
  "promptId": "ab5656e8-b9e4-40d4-bf76-8cf45c241dcf",
  "type": "user",
  "uuid": "6ecda2d0-59af-44b4-9f5c-189f30af998b",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Search the web for the paper \"Trust Me, I'm Wrong: LLMs Hallucinate with Certainty Despite Knowing the Answer\" by Simhi et al., arxiv 2502.12964, claimed to be at Findings of EMNLP 2025. I need to verify: (1) does this paper exist, (2) what does it define as CHOKE hallucinations, (3) what percentage of hallucinations are CHOKE, (4) does it propose any detection/mitigation method. Use WebSearch and WebFetch to get details.",
    "agentId": "aed152a26c69b20b8",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "I now have comprehensive information to provide a thorough answer. Here is my findings summary:\n\n---\n\n## Verification Results for \"Trust Me, I'm Wrong\" (arxiv 2502.12964)\n\n### (1) Does the paper exist?\n\n**Yes, confirmed.** The paper is real and published:\n- **Title:** \"Trust Me, I'm Wrong: LLMs Hallucinate with Certainty Despite Knowing the Answer\"\n- **Authors:** Adi Simhi, Itay Itzhak, Fazl Barez, Gabriel Stanovsky, and Yonatan Belinkov\n- **arXiv:** 2502.12964 (submitted February 18, 2025)\n- **Venue:** Findings of EMNLP 2025, pages 14665-14688, Suzhou, China (confirmed via ACL Anthology)\n\n### (2) Definition of CHOKE Hallucinations\n\nCHOKE stands for **Certain Hallucinations Overriding Known Evidence**. It requires three conditions to be met simultaneously:\n\n1. The model **can consistently answer a question correctly** with proper prompting (i.e., it demonstrably \"knows\" the answer).\n2. A **seemingly trivial prompt perturbation** causes the model to produce an incorrect/hallucinated response.\n3. The model expresses **high certainty** in its wrong answer.\n\nThe key distinction from ordinary hallucinations is that the model possesses the correct knowledge but confidently overrides it due to minor prompt variations.\n\n### (3) Percentage of Hallucinations that are CHOKE\n\nThe paper reports varying rates depending on model and metric:\n- **16-43% of high-certainty hallucinations** (hallucinations where the model is confident) qualify as CHOKE across different models and certainty metrics.\n- On TriviaQA specifically: **8-26% average** across models and certainty methods.\n- As a fraction of ALL hallucinations overall: **0.3%-2.1%** are CHOKE.\n- \"Hallucinations despite knowledge\" (the broader category) comprise 2%-8% of all hallucinations.\n\nCHOKE examples are shown to be consistent across prompts, models (both pre-trained and instruction-tuned), and datasets, indicating they form a distinct, systematic category rather than random noise.\n\n### (4) Detection and Mitigation Methods\n\n**Detection/Certainty Metrics Used:**\nThe paper evaluates three certainty estimation methods:\n1. **Token probability** - probability of the first generated token\n2. **Probability difference** - gap between the top two vocabulary items\n3. **Semantic entropy** - clusters outputs by semantic meaning using DeBERTa\n\n**Proposed Mitigation - Probing-based approach:**\n- Uses **logistic regression classifiers trained on internal model activations** (specifically residual stream activations at layer 15's final token).\n- Key innovation: **oversamples CHOKE examples to 65% of training data** to specifically target this failure mode.\n- Outperforms baseline certainty methods and prompting-based methods on CHOKE-specific scores.\n- Maintains stable performance on standard accuracy metrics.\n\n**Key finding on existing methods:** Conventional mitigation strategies (standard uncertainty-based rejection, self-consistency, etc.) perform *worse* on CHOKE examples than on general hallucinations, which is precisely why the specialized probing-based approach was needed.\n\n---\n\nSources:\n- [arXiv Abstract](https://arxiv.org/abs/2502.12964)\n- [arXiv Full HTML](https://arxiv.org/html/2502.12964v2)\n- [ACL Anthology - Findings of EMNLP 2025](https://aclanthology.org/2025.findings-emnlp.792/)\n- [AlphaXiv Discussion](https://www.alphaxiv.org/overview/2502.12964v2)"
      }
    ],
    "totalDurationMs": 74436,
    "totalTokens": 16394,
    "totalToolUseCount": 7,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1067,
      "cache_read_input_tokens": 14411,
      "output_tokens": 915,
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
          "output_tokens": 915,
          "cache_read_input_tokens": 14411,
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
      "otherToolCount": 7
    }
  },
  "sourceToolAssistantUUID": "48059621-a461-4d73-9c9f-58e284b056a5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1c70a808-ac42-40e9-b451-f24d9f6e7546",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-16T09:46:55.304Z_

<details><summary>↩ Tool result · `toolu_019RNjgB7ejW7EsYoTyBRaRM`</summary>

```text
Here is a comprehensive report of all papers found relating to perturbation-based and sensitivity-based hallucination detection in LLMs:

---

## Confirmed Papers on Perturbation/Sensitivity-Based Hallucination Detection

### 1. "Shaking to Reveal: Perturbation-Based Detection of LLM Hallucinations" (arXiv:2506.02696)
- **Authors:** Jinyuan Luo, Zhen Fang, Yixuan Li, Seongheon Park, Ling Chen
- **Date:** June 3, 2025
- **Venue:** arXiv (confirmed to exist)
- **Method:** Proposes **Sample-Specific Prompting (SSP)**, a framework that detects hallucinations by analyzing perturbation sensitivity at intermediate representations. SSP dynamically generates noise prompts for each input and employs a lightweight encoder to amplify changes in representations caused by perturbation. A contrastive distance metric quantifies differences between truthful and hallucinated responses.
- **Key Insight:** Factual knowledge is encoded in well-structured internal representations that are tightly coupled with the input and exhibit *greater* sensitivity in intermediate layers when perturbed. Hallucinated answers remain relatively stable under perturbation. Intermediate representations are used because they are less influenced by model bias.
- **Relation to your query:** Directly measures distribution sensitivity after perturbation of internal representations.

### 2. "Perturbations Matter: Sensitivity-Guided Hallucination Detection in LLMs" (OpenReview: aZdcNDf3pc)
- **Venue:** OpenReview (appears to be the formal venue version of the SSP method)
- **Method:** This is the same SSP framework. Establishes a theory showing that with non-negligible probability (~99% on representative datasets), each sample admits a prompt under which factual samples exhibit greater sensitivity to prompt-induced perturbations than hallucinatory samples. SSP leverages sensitivity to prompt-induced perturbations as a discriminative indicator.
- **Datasets:** CoQA, TruthfulQA, TriviaQA, TydiQA-GP
- **Relation to your query:** Provides theoretical grounding for why perturbation sensitivity discriminates truthful from hallucinated content.

### 3. "From Flat Facts to Sharp Hallucinations: Detecting Stubborn Errors via Gradient Sensitivity" (arXiv:2605.00939)
- **Date:** May 2025
- **Method:** Proposes **Embedding-Perturbed Gradient Sensitivity (EPGS)**. Categorizes hallucinations based on loss landscape geometry: robust facts reside in *flat* minima, while stubborn hallucinations sit in *sharp* minima supported by brittle memorization. EPGS detects this sharpness by perturbing input embeddings with Gaussian noise and measuring the resulting spike in gradient magnitude, serving as an efficient proxy for the Hessian spectrum.
- **Key Insight:** Transient hallucinations occur in unstable regions, while "stubborn hallucinations" (high-confidence errors) reside in sharp minima.
- **Results:** Significantly outperforms entropy-based and representation-based baselines.
- **Relation to your query:** Directly uses embedding perturbation and measures gradient sensitivity (related to logit-level sensitivity). The sharpness/flatness framing connects loss landscape geometry to hallucination detection.

### 4. "Next-Token Gradient Sensitivity Probing for LLM Hallucination Detection" (OpenReview: yzWGQNTbHQ)
- **Method:** Introduces **Next-token Gradient Sensitivity (NGS)**, a statistic that quantifies the first-order gradient of the maximum log-probability of the next token with respect to the current token's layer embedding, measuring local prediction fragility. The norm of NGS bounds prediction confidence changes under small perturbations.
- **Detection framework:** **NGS-HD** reframes detection as a token-level distribution comparison task. Directly probes local behaviors through gradients, offering an exact first-order measure of output sensitivity to embedding perturbations *without* requiring explicit perturbation sampling.
- **Results:** On Qwen-3-8b, NGS-HD achieved 80.30% average (6.27% improvement over TSV baseline), with 77.76% on TruthfulQA and 82.30% on NQ Open.
- **Relation to your query:** Measures logit-level sensitivity (gradient of log-probability) with respect to embedding perturbations. The gradient norm bounds KL-divergence-like changes in prediction distribution.

### 5. "Probing LLM Hallucination from Within: Perturbation-Driven Approach via Internal Knowledge" / SHINE (arXiv:2411.09689)
- **Authors:** Seongmin Lee, Hsiang Hsu, Chun-Fu Chen, Duen Horng Chau
- **Date:** November 2024 (v4 updated into 2025)
- **Method:** **SHINE** (Sensitivity of Hallucination to Internal kNowledge via Entity perturbation). A four-step process: (1) identify entities in the prompt, (2) determine perturbation strength, (3) perturb entity embeddings, (4) measure **Entity Perturbation Impact via KL divergence** between original and perturbed output distributions. Low KL divergence after entity perturbation strongly indicates fabricated text, since fabricated tokens are weakly tied to key entities.
- **Classification:** Categorizes LLM text as aligned, misaligned, or fabricated.
- **Results:** State-of-the-art across four datasets and four LLMs, outperforming seven competing methods. No external knowledge, supervised training, or fine-tuning required.
- **Relation to your query:** Directly uses KL divergence to measure sensitivity after perturbation of internal representations (entity embeddings).

### 6. "In-Context Sharpness as Alerts: An Inner Representation Perspective for Hallucination Mitigation" (arXiv:2403.01548)
- **Venue:** ICML 2024 (Proceedings of the 41st International Conference on Machine Learning, pages 7553-7567)
- **Method:** Discovers that correct generations have *sharper* context activations in hidden states of in-context tokens compared to incorrect ones. Proposes an entropy-based metric to quantify "sharpness" among in-context hidden states and incorporates it into constrained decoding.
- **Results:** Up to 8.6 absolute point improvement on TruthfulQA. Improvement scales with model size (3.3 pts for 7B, 4.8 pts for 13B, 8.6 pts for 70B).
- **Code:** Available at github.com/hkust-nlp/Activation_Decoding
- **Relation to your query:** While not perturbation-based per se, it measures "sharpness" of internal representations as a hallucination signal -- conceptually related to how perturbation methods probe the sharpness/stability of internal states.

### 7. "Detecting Hallucinations in Large Language Models via Internal Attention Divergence Signals" (arXiv:2605.05025)
- **Author:** Gijs van Dijk
- **Date:** May 6, 2026
- **Method:** Measures **KL divergence between each attention head's distribution and a uniform reference distribution**, using these features in a logistic regression probe. Single-pass, no repeated sampling or external models needed.
- **Key Finding:** Signal is concentrated in middle layers and on factual tokens (named entities, numbers). Attention divergence is highly predictive of answer correctness and performs competitively with existing uncertainty estimation methods.
- **Relation to your query:** Directly uses KL divergence as a measure of internal representation behavior to detect hallucinations.

---

## Additional Related Papers

### 8. "Hallucination Begins Where Saliency Drops" (arXiv:2601.20279)
- **Venue:** ICLR 2026
- **Method:** Introduces **LVLMs-Saliency**, a gradient-aware diagnostic framework for vision-language models. Fuses attention weights with input gradients to quantify visual grounding strength. Proposes Saliency-Guided Rejection Sampling (SGRS) and Local Coherence Reinforcement (LocoRE).
- **Key finding:** Hallucinations arise when preceding output tokens exhibit low saliency toward prediction of the next token (breakdown in contextual memory).
- **Relation:** Uses gradient-based sensitivity analysis of attention as hallucination signal.

### 9. "Hallucination as Trajectory Commitment: Causal Evidence for Asymmetric Attractor Dynamics in Transformer Generation" (arXiv:2604.15400)
- **Date:** April 2026
- **Method:** Uses activation patching to study residual stream dynamics. Finds hallucination operates as a locally stable attractor basin. Injecting a hallucinated activation into a correct trajectory corrupts output 87.5% of the time, while the reverse recovers only 33.3%.
- **Key insight:** Corruption needs only a single perturbation, while correction requires sustained multi-step intervention.
- **Relation:** Demonstrates asymmetric sensitivity to perturbation in the residual stream between truthful and hallucinated states.

### 10. "CORVUS: Red-Teaming Hallucination Detectors via Internal Signal Camouflage in Large Language Models" (arXiv:2601.14310)
- **Date:** January 2026
- **Method:** Adversarial attack on perturbation/sensitivity-based detectors. Fine-tunes LoRA adapters to camouflage internal telemetry (uncertainty, hidden-state geometry, attention) while keeping detectors fixed. Includes an embedding-space FGSM attention stress test.
- **Results:** Degrades all existing detectors (LLM-Check, ICR-probe, SEP) across four LLMs on FAVA-Annotation.
- **Relation:** Important adversarial counterpoint showing that perturbation-based detection signals can potentially be camouflaged.

### 11. "A Single Direction of Truth: An Observer Model's Linear Residual Probe Exposes and Steers Contextual Hallucinations" (arXiv:2507.23221)
- **Method:** A generator-agnostic observer model detects hallucinations via a single forward pass and a linear probe on its residual stream, isolating a single transferable linear direction separating hallucinated from faithful text. Manipulating this direction causally steers hallucination rates.
- **Relation:** Identifies a linear perturbation direction in the residual stream that controls hallucination.

---

## Summary of How These Methods Relate to Measuring Distribution Sensitivity After Perturbation

The papers cluster into several approaches:

1. **KL divergence after embedding perturbation** (SHINE): Perturb entity embeddings, measure KL divergence of output distributions. Low KL = fabricated content.

2. **Gradient sensitivity as perturbation proxy** (NGS-HD, EPGS): Instead of explicit perturbation, use gradients to measure how much the output distribution *would* change under small perturbations. NGS measures dlog(p)/d(embedding); EPGS adds Gaussian noise and measures gradient magnitude spikes.

3. **Prompt-induced perturbation of intermediate representations** (SSP / "Shaking to Reveal"): Perturb via dynamically generated prompts, measure representational shift at intermediate layers. Truthful content shows *greater* sensitivity (well-structured, tightly coupled to input).

4. **Attention-based KL divergence** (van Dijk 2026): Measure KL divergence of attention distributions from uniform, use as uncertainty proxy.

5. **Sharpness of internal activations** (In-Context Sharpness): Measure entropy/sharpness of hidden-state activations as proxy for confidence.

6. **Loss landscape geometry** (EPGS / "Flat Facts to Sharp Hallucinations"): Frame hallucination detection as identifying sharp vs. flat minima through perturbation.

The key unifying theme: **truthful and hallucinated outputs have fundamentally different stability properties in representation space**, and perturbation-based methods exploit this by measuring how much internal states or output distributions shift when the model's inputs or internal representations are perturbed.

---

Sources:
- [Shaking to Reveal: Perturbation-Based Detection of LLM Hallucinations](https://arxiv.org/abs/2506.02696)
- [Perturbations Matter: Sensitivity-Guided Hallucination Detection in LLMs](https://openreview.net/forum?id=aZdcNDf3pc)
- [From Flat Facts to Sharp Hallucinations: Detecting Stubborn Errors via Gradient Sensitivity](https://arxiv.org/abs/2605.00939)
- [Next-Token Gradient Sensitivity Probing for LLM Hallucination Detection](https://openreview.net/forum?id=yzWGQNTbHQ)
- [Probing LLM Hallucination from Within: Perturbation-Driven Approach via Internal Knowledge (SHINE)](https://arxiv.org/abs/2411.09689)
- [In-Context Sharpness as Alerts: An Inner Representation Perspective for Hallucination Mitigation](https://arxiv.org/abs/2403.01548)
- [Detecting Hallucinations in LLMs via Internal Attention Divergence Signals](https://arxiv.org/abs/2605.05025)
- [Hallucination Begins Where Saliency Drops](https://arxiv.org/abs/2601.20279)
- [Hallucination as Trajectory Commitment](https://arxiv.org/abs/2604.15400)
- [CORVUS: Red-Teaming Hallucination Detectors via Internal Signal Camouflage](https://arxiv.org/abs/2601.14310)
- [A Single Direction of Truth: Observer Model's Linear Residual Probe](https://arxiv.org/abs/2507.23221)
- [Attractor Geometry of Transformer Memory](https://arxiv.org/abs/2605.05686)

agentId: a472047db0d9b0bf1 (use SendMessage with to: 'a472047db0d9b0bf1' to continue this agent)
&lt;usage>total_tokens: 28915
tool_uses: 17
duration_ms: 140230&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7ffe9c96-f067-497b-b1b0-816be3f5547d",
  "isSidechain": false,
  "promptId": "ab5656e8-b9e4-40d4-bf76-8cf45c241dcf",
  "type": "user",
  "uuid": "cb7a2d2d-ab88-45cb-9dca-1592f5f5c8d3",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Search the web for recent papers (2025-2026) on perturbation-based or sensitivity-based hallucination detection in LLMs, particularly methods that measure KL divergence or logit-level sensitivity after perturbing internal representations. Search for:\n1. \"logit sensitivity hallucination detection 2025 2026\"\n2. \"KL divergence perturbation hallucination LLM 2025\"\n3. \"residual stream perturbation hallucination\"\n4. \"sharpness hallucination detection language model\"\n5. \"Shaking to Reveal\" arxiv 2506.02696 (verify this paper exists and what it does)\n\nAlso search for \"SSP hallucination detection OpenReview\" and \"next-token gradient sensitivity hallucination\". Report all papers found with their key methods and how they relate to measuring distribution sensitivity after perturbation.",
    "agentId": "a472047db0d9b0bf1",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here is a comprehensive report of all papers found relating to perturbation-based and sensitivity-based hallucination detection in LLMs:\n\n---\n\n## Confirmed Papers on Perturbation/Sensitivity-Based Hallucination Detection\n\n### 1. \"Shaking to Reveal: Perturbation-Based Detection of LLM Hallucinations\" (arXiv:2506.02696)\n- **Authors:** Jinyuan Luo, Zhen Fang, Yixuan Li, Seongheon Park, Ling Chen\n- **Date:** June 3, 2025\n- **Venue:** arXiv (confirmed to exist)\n- **Method:** Proposes **Sample-Specific Prompting (SSP)**, a framework that detects hallucinations by analyzing perturbation sensitivity at intermediate representations. SSP dynamically generates noise prompts for each input and employs a lightweight encoder to amplify changes in representations caused by perturbation. A contrastive distance metric quantifies differences between truthful and hallucinated responses.\n- **Key Insight:** Factual knowledge is encoded in well-structured internal representations that are tightly coupled with the input and exhibit *greater* sensitivity in intermediate layers when perturbed. Hallucinated answers remain relatively stable under perturbation. Intermediate representations are used because they are less influenced by model bias.\n- **Relation to your query:** Directly measures distribution sensitivity after perturbation of internal representations.\n\n### 2. \"Perturbations Matter: Sensitivity-Guided Hallucination Detection in LLMs\" (OpenReview: aZdcNDf3pc)\n- **Venue:** OpenReview (appears to be the formal venue version of the SSP method)\n- **Method:** This is the same SSP framework. Establishes a theory showing that with non-negligible probability (~99% on representative datasets), each sample admits a prompt under which factual samples exhibit greater sensitivity to prompt-induced perturbations than hallucinatory samples. SSP leverages sensitivity to prompt-induced perturbations as a discriminative indicator.\n- **Datasets:** CoQA, TruthfulQA, TriviaQA, TydiQA-GP\n- **Relation to your query:** Provides theoretical grounding for why perturbation sensitivity discriminates truthful from hallucinated content.\n\n### 3. \"From Flat Facts to Sharp Hallucinations: Detecting Stubborn Errors via Gradient Sensitivity\" (arXiv:2605.00939)\n- **Date:** May 2025\n- **Method:** Proposes **Embedding-Perturbed Gradient Sensitivity (EPGS)**. Categorizes hallucinations based on loss landscape geometry: robust facts reside in *flat* minima, while stubborn hallucinations sit in *sharp* minima supported by brittle memorization. EPGS detects this sharpness by perturbing input embeddings with Gaussian noise and measuring the resulting spike in gradient magnitude, serving as an efficient proxy for the Hessian spectrum.\n- **Key Insight:** Transient hallucinations occur in unstable regions, while \"stubborn hallucinations\" (high-confidence errors) reside in sharp minima.\n- **Results:** Significantly outperforms entropy-based and representation-based baselines.\n- **Relation to your query:** Directly uses embedding perturbation and measures gradient sensitivity (related to logit-level sensitivity). The sharpness/flatness framing connects loss landscape geometry to hallucination detection.\n\n### 4. \"Next-Token Gradient Sensitivity Probing for LLM Hallucination Detection\" (OpenReview: yzWGQNTbHQ)\n- **Method:** Introduces **Next-token Gradient Sensitivity (NGS)**, a statistic that quantifies the first-order gradient of the maximum log-probability of the next token with respect to the current token's layer embedding, measuring local prediction fragility. The norm of NGS bounds prediction confidence changes under small perturbations.\n- **Detection framework:** **NGS-HD** reframes detection as a token-level distribution comparison task. Directly probes local behaviors through gradients, offering an exact first-order measure of output sensitivity to embedding perturbations *without* requiring explicit perturbation sampling.\n- **Results:** On Qwen-3-8b, NGS-HD achieved 80.30% average (6.27% improvement over TSV baseline), with 77.76% on TruthfulQA and 82.30% on NQ Open.\n- **Relation to your query:** Measures logit-level sensitivity (gradient of log-probability) with respect to embedding perturbations. The gradient norm bounds KL-divergence-like changes in prediction distribution.\n\n### 5. \"Probing LLM Hallucination from Within: Perturbation-Driven Approach via Internal Knowledge\" / SHINE (arXiv:2411.09689)\n- **Authors:** Seongmin Lee, Hsiang Hsu, Chun-Fu Chen, Duen Horng Chau\n- **Date:** November 2024 (v4 updated into 2025)\n- **Method:** **SHINE** (Sensitivity of Hallucination to Internal kNowledge via Entity perturbation). A four-step process: (1) identify entities in the prompt, (2) determine perturbation strength, (3) perturb entity embeddings, (4) measure **Entity Perturbation Impact via KL divergence** between original and perturbed output distributions. Low KL divergence after entity perturbation strongly indicates fabricated text, since fabricated tokens are weakly tied to key entities.\n- **Classification:** Categorizes LLM text as aligned, misaligned, or fabricated.\n- **Results:** State-of-the-art across four datasets and four LLMs, outperforming seven competing methods. No external knowledge, supervised training, or fine-tuning required.\n- **Relation to your query:** Directly uses KL divergence to measure sensitivity after perturbation of internal representations (entity embeddings).\n\n### 6. \"In-Context Sharpness as Alerts: An Inner Representation Perspective for Hallucination Mitigation\" (arXiv:2403.01548)\n- **Venue:** ICML 2024 (Proceedings of the 41st International Conference on Machine Learning, pages 7553-7567)\n- **Method:** Discovers that correct generations have *sharper* context activations in hidden states of in-context tokens compared to incorrect ones. Proposes an entropy-based metric to quantify \"sharpness\" among in-context hidden states and incorporates it into constrained decoding.\n- **Results:** Up to 8.6 absolute point improvement on TruthfulQA. Improvement scales with model size (3.3 pts for 7B, 4.8 pts for 13B, 8.6 pts for 70B).\n- **Code:** Available at github.com/hkust-nlp/Activation_Decoding\n- **Relation to your query:** While not perturbation-based per se, it measures \"sharpness\" of internal representations as a hallucination signal -- conceptually related to how perturbation methods probe the sharpness/stability of internal states.\n\n### 7. \"Detecting Hallucinations in Large Language Models via Internal Attention Divergence Signals\" (arXiv:2605.05025)\n- **Author:** Gijs van Dijk\n- **Date:** May 6, 2026\n- **Method:** Measures **KL divergence between each attention head's distribution and a uniform reference distribution**, using these features in a logistic regression probe. Single-pass, no repeated sampling or external models needed.\n- **Key Finding:** Signal is concentrated in middle layers and on factual tokens (named entities, numbers). Attention divergence is highly predictive of answer correctness and performs competitively with existing uncertainty estimation methods.\n- **Relation to your query:** Directly uses KL divergence as a measure of internal representation behavior to detect hallucinations.\n\n---\n\n## Additional Related Papers\n\n### 8. \"Hallucination Begins Where Saliency Drops\" (arXiv:2601.20279)\n- **Venue:** ICLR 2026\n- **Method:** Introduces **LVLMs-Saliency**, a gradient-aware diagnostic framework for vision-language models. Fuses attention weights with input gradients to quantify visual grounding strength. Proposes Saliency-Guided Rejection Sampling (SGRS) and Local Coherence Reinforcement (LocoRE).\n- **Key finding:** Hallucinations arise when preceding output tokens exhibit low saliency toward prediction of the next token (breakdown in contextual memory).\n- **Relation:** Uses gradient-based sensitivity analysis of attention as hallucination signal.\n\n### 9. \"Hallucination as Trajectory Commitment: Causal Evidence for Asymmetric Attractor Dynamics in Transformer Generation\" (arXiv:2604.15400)\n- **Date:** April 2026\n- **Method:** Uses activation patching to study residual stream dynamics. Finds hallucination operates as a locally stable attractor basin. Injecting a hallucinated activation into a correct trajectory corrupts output 87.5% of the time, while the reverse recovers only 33.3%.\n- **Key insight:** Corruption needs only a single perturbation, while correction requires sustained multi-step intervention.\n- **Relation:** Demonstrates asymmetric sensitivity to perturbation in the residual stream between truthful and hallucinated states.\n\n### 10. \"CORVUS: Red-Teaming Hallucination Detectors via Internal Signal Camouflage in Large Language Models\" (arXiv:2601.14310)\n- **Date:** January 2026\n- **Method:** Adversarial attack on perturbation/sensitivity-based detectors. Fine-tunes LoRA adapters to camouflage internal telemetry (uncertainty, hidden-state geometry, attention) while keeping detectors fixed. Includes an embedding-space FGSM attention stress test.\n- **Results:** Degrades all existing detectors (LLM-Check, ICR-probe, SEP) across four LLMs on FAVA-Annotation.\n- **Relation:** Important adversarial counterpoint showing that perturbation-based detection signals can potentially be camouflaged.\n\n### 11. \"A Single Direction of Truth: An Observer Model's Linear Residual Probe Exposes and Steers Contextual Hallucinations\" (arXiv:2507.23221)\n- **Method:** A generator-agnostic observer model detects hallucinations via a single forward pass and a linear probe on its residual stream, isolating a single transferable linear direction separating hallucinated from faithful text. Manipulating this direction causally steers hallucination rates.\n- **Relation:** Identifies a linear perturbation direction in the residual stream that controls hallucination.\n\n---\n\n## Summary of How These Methods Relate to Measuring Distribution Sensitivity After Perturbation\n\nThe papers cluster into several approaches:\n\n1. **KL divergence after embedding perturbation** (SHINE): Perturb entity embeddings, measure KL divergence of output distributions. Low KL = fabricated content.\n\n2. **Gradient sensitivity as perturbation proxy** (NGS-HD, EPGS): Instead of explicit perturbation, use gradients to measure how much the output distribution *would* change under small perturbations. NGS measures dlog(p)/d(embedding); EPGS adds Gaussian noise and measures gradient magnitude spikes.\n\n3. **Prompt-induced perturbation of intermediate representations** (SSP / \"Shaking to Reveal\"): Perturb via dynamically generated prompts, measure representational shift at intermediate layers. Truthful content shows *greater* sensitivity (well-structured, tightly coupled to input).\n\n4. **Attention-based KL divergence** (van Dijk 2026): Measure KL divergence of attention distributions from uniform, use as uncertainty proxy.\n\n5. **Sharpness of internal activations** (In-Context Sharpness): Measure entropy/sharpness of hidden-state activations as proxy for confidence.\n\n6. **Loss landscape geometry** (EPGS / \"Flat Facts to Sharp Hallucinations\"): Frame hallucination detection as identifying sharp vs. flat minima through perturbation.\n\nThe key unifying theme: **truthful and hallucinated outputs have fundamentally different stability properties in representation space**, and perturbation-based methods exploit this by measuring how much internal states or output distributions shift when the model's inputs or internal representations are perturbed.\n\n---\n\nSources:\n- [Shaking to Reveal: Perturbation-Based Detection of LLM Hallucinations](https://arxiv.org/abs/2506.02696)\n- [Perturbations Matter: Sensitivity-Guided Hallucination Detection in LLMs](https://openreview.net/forum?id=aZdcNDf3pc)\n- [From Flat Facts to Sharp Hallucinations: Detecting Stubborn Errors via Gradient Sensitivity](https://arxiv.org/abs/2605.00939)\n- [Next-Token Gradient Sensitivity Probing for LLM Hallucination Detection](https://openreview.net/forum?id=yzWGQNTbHQ)\n- [Probing LLM Hallucination from Within: Perturbation-Driven Approach via Internal Knowledge (SHINE)](https://arxiv.org/abs/2411.09689)\n- [In-Context Sharpness as Alerts: An Inner Representation Perspective for Hallucination Mitigation](https://arxiv.org/abs/2403.01548)\n- [Detecting Hallucinations in LLMs via Internal Attention Divergence Signals](https://arxiv.org/abs/2605.05025)\n- [Hallucination Begins Where Saliency Drops](https://arxiv.org/abs/2601.20279)\n- [Hallucination as Trajectory Commitment](https://arxiv.org/abs/2604.15400)\n- [CORVUS: Red-Teaming Hallucination Detectors via Internal Signal Camouflage](https://arxiv.org/abs/2601.14310)\n- [A Single Direction of Truth: Observer Model's Linear Residual Probe](https://arxiv.org/abs/2507.23221)\n- [Attractor Geometry of Transformer Memory](https://arxiv.org/abs/2605.05686)"
      }
    ],
    "totalDurationMs": 140230,
    "totalTokens": 28915,
    "totalToolUseCount": 17,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1757,
      "cache_read_input_tokens": 23734,
      "output_tokens": 3423,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1757
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3423,
          "cache_read_input_tokens": 23734,
          "cache_creation_input_tokens": 1757,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1757,
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
  "sourceToolAssistantUUID": "7ffe9c96-f067-497b-b1b0-816be3f5547d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1c70a808-ac42-40e9-b451-f24d9f6e7546",
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
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-16 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "cb7a2d2d-ab88-45cb-9dca-1592f5f5c8d3",
  "sessionId": "1c70a808-ac42-40e9-b451-f24d9f6e7546"
}
```

---

### Runtime record

_source line 18_

```json
{
  "type": "ai-title",
  "aiTitle": "Verify LSP method against Liu et al. and assess CHOKE subset feasibility",
  "sessionId": "1c70a808-ac42-40e9-b451-f24d9f6e7546"
}
```

---

### Tool result

_source line 19 · 2026-05-16T09:47:07.921Z_

<details><summary>↩ Tool result · `toolu_019TLy9tQJJ5tVMroYH5a6ut`</summary>

```text
Based on my extensive research, here is my comprehensive report:

---

## Findings on "Enhancing Hallucination Detection through Noise Injection" (arXiv 2502.03799)

### (1) Does this paper exist?

**Yes.** The paper exists on arXiv at `2502.03799`, originally submitted February 2025, with a v3 revision dated March 1, 2026. It also has an OpenReview submission page at `openreview.net/forum?id=2bWf4M5tRo`.

**Authors:** Litian Liu, Reza Pourreza, Sunny Panchal, Apratim Bhattacharyya, Yubing Jian, Yao Qin, Roland Memisevic

---

### (2) What exactly does the method do?

The paper proposes a **training-free, inference-time** method for detecting hallucinations in LLMs by injecting noise into model activations to better capture Bayesian uncertainty:

**Noise injection procedure:**
- **Type of noise:** Uniform noise sampled from U(0, alpha), where alpha typically ranges from 0.01 to 0.11. (Bounded Gaussian noise was also tested with comparable results.)
- **Where injected:** Into **MLP activations** in approximately the **top third of transformer layers** (e.g., layers 20-32 for a 32-layer model). The same noise vector is reused across selected layers to prevent cancellation from skip connections.
- **Rationale:** Rather than just sampling from the model's token distribution (which captures aleatoric uncertainty only), perturbing activations approximates a Bayesian ensemble over parameters, capturing **epistemic uncertainty** -- i.e., model uncertainty about what it "knows" vs. what it doesn't.

**Metrics measured (uncertainty quantification):**
- **Answer Entropy** (primary) -- counting occurrence of each distinct answer string
- **Semantic Entropy** -- clustering semantically similar responses before computing entropy
- **Predictive Entropy** -- length-normalized entropy across token predictions
- **Lexical Similarity** -- ROUGE-L based similarity scores
- **EigenScore** -- entropy computed in embedding space
- **selfCheckGPT-NLI** -- contradiction detection using NLI

**Evaluation datasets:**
- GSM8K (mathematical reasoning, 1,319 test questions)
- CommonsenseQA (multiple-choice knowledge, 1,221 validation examples)
- TriviaQA (factual QA, 18,669 questions from rc.nocontext subset)

**Results:** AUROC improvements of 1-6 percentage points over standard sampling. Greatest gains on reasoning tasks (e.g., GSM8K: 71.56 to 76.14 AUROC for Llama-2-7B-chat).

---

### (3) Was it accepted at ICLR 2026?

**The evidence is mixed and I cannot definitively confirm acceptance:**

- The arxiv page metadata (from web search snippets) states it is an "ICLR 2026 main conference paper."
- The OpenReview page (`2bWf4M5tRo`) appears to show a submission to **ICLR 2025** (submitted September 2024), with no visible acceptance decision.
- The first author's personal website (`litianliu.github.io`) lists it only as a "Preprint, 2025" with no conference venue mentioned.
- A web search result references "Published as a conference paper at ICLR 2026" in a PDF link from OpenReview, but I could not confirm this PDF corresponds to this specific paper (it may be a different hallucination detection paper).
- One search snippet mentions Litian Liu presenting "at Pavilion 4, April 23" at a conference discussing this work.

**Conclusion on venue:** The paper was likely rejected from ICLR 2025 (submitted Sept 2024, no acceptance shown) and then resubmitted and accepted at **ICLR 2026**. The arxiv v3 revision (March 2026) is consistent with a camera-ready update after ICLR 2026 acceptance decisions. However, the author's own website has not been updated to reflect this, so there is some uncertainty. The weight of evidence (arxiv metadata, search snippets, presentation reference) suggests it **was accepted at ICLR 2026**, but I cannot find an unambiguous official "accept" decision on OpenReview for the ICLR 2026 submission specifically.

---

Sources:
- [arXiv page: 2502.03799](https://arxiv.org/abs/2502.03799)
- [arXiv HTML version](https://arxiv.org/html/2502.03799)
- [OpenReview submission](https://openreview.net/forum?id=2bWf4M5tRo)
- [alphaXiv overview](https://www.alphaxiv.org/ja/overview/2502.03799v1)
- [Litian Liu personal page](https://litianliu.github.io/)
- [ICLR 2026 Papers](https://iclr.cc/virtual/2026/papers.html)

agentId: add7131eef563085e (use SendMessage with to: 'add7131eef563085e' to continue this agent)
&lt;usage>total_tokens: 21166
tool_uses: 18
duration_ms: 159821&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fbf08c7c-0acb-47cb-99b3-5a14c15e2327",
  "isSidechain": false,
  "promptId": "ab5656e8-b9e4-40d4-bf76-8cf45c241dcf",
  "type": "user",
  "uuid": "50898e08-0ce9-4790-ad2c-d5ddbe45045c",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Search the web for the paper \"Enhancing Hallucination Detection through Noise Injection\" by Liu et al., arxiv 2502.03799, claimed to be at ICLR 2026. I need to verify: (1) does this paper exist, (2) what exactly does it do (noise injection into activations, measuring what metric), (3) was it accepted at ICLR 2026. Use WebSearch and WebFetch on the arxiv page. Report exactly what the method does and what metrics it measures.",
    "agentId": "add7131eef563085e",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Based on my extensive research, here is my comprehensive report:\n\n---\n\n## Findings on \"Enhancing Hallucination Detection through Noise Injection\" (arXiv 2502.03799)\n\n### (1) Does this paper exist?\n\n**Yes.** The paper exists on arXiv at `2502.03799`, originally submitted February 2025, with a v3 revision dated March 1, 2026. It also has an OpenReview submission page at `openreview.net/forum?id=2bWf4M5tRo`.\n\n**Authors:** Litian Liu, Reza Pourreza, Sunny Panchal, Apratim Bhattacharyya, Yubing Jian, Yao Qin, Roland Memisevic\n\n---\n\n### (2) What exactly does the method do?\n\nThe paper proposes a **training-free, inference-time** method for detecting hallucinations in LLMs by injecting noise into model activations to better capture Bayesian uncertainty:\n\n**Noise injection procedure:**\n- **Type of noise:** Uniform noise sampled from U(0, alpha), where alpha typically ranges from 0.01 to 0.11. (Bounded Gaussian noise was also tested with comparable results.)\n- **Where injected:** Into **MLP activations** in approximately the **top third of transformer layers** (e.g., layers 20-32 for a 32-layer model). The same noise vector is reused across selected layers to prevent cancellation from skip connections.\n- **Rationale:** Rather than just sampling from the model's token distribution (which captures aleatoric uncertainty only), perturbing activations approximates a Bayesian ensemble over parameters, capturing **epistemic uncertainty** -- i.e., model uncertainty about what it \"knows\" vs. what it doesn't.\n\n**Metrics measured (uncertainty quantification):**\n- **Answer Entropy** (primary) -- counting occurrence of each distinct answer string\n- **Semantic Entropy** -- clustering semantically similar responses before computing entropy\n- **Predictive Entropy** -- length-normalized entropy across token predictions\n- **Lexical Similarity** -- ROUGE-L based similarity scores\n- **EigenScore** -- entropy computed in embedding space\n- **selfCheckGPT-NLI** -- contradiction detection using NLI\n\n**Evaluation datasets:**\n- GSM8K (mathematical reasoning, 1,319 test questions)\n- CommonsenseQA (multiple-choice knowledge, 1,221 validation examples)\n- TriviaQA (factual QA, 18,669 questions from rc.nocontext subset)\n\n**Results:** AUROC improvements of 1-6 percentage points over standard sampling. Greatest gains on reasoning tasks (e.g., GSM8K: 71.56 to 76.14 AUROC for Llama-2-7B-chat).\n\n---\n\n### (3) Was it accepted at ICLR 2026?\n\n**The evidence is mixed and I cannot definitively confirm acceptance:**\n\n- The arxiv page metadata (from web search snippets) states it is an \"ICLR 2026 main conference paper.\"\n- The OpenReview page (`2bWf4M5tRo`) appears to show a submission to **ICLR 2025** (submitted September 2024), with no visible acceptance decision.\n- The first author's personal website (`litianliu.github.io`) lists it only as a \"Preprint, 2025\" with no conference venue mentioned.\n- A web search result references \"Published as a conference paper at ICLR 2026\" in a PDF link from OpenReview, but I could not confirm this PDF corresponds to this specific paper (it may be a different hallucination detection paper).\n- One search snippet mentions Litian Liu presenting \"at Pavilion 4, April 23\" at a conference discussing this work.\n\n**Conclusion on venue:** The paper was likely rejected from ICLR 2025 (submitted Sept 2024, no acceptance shown) and then resubmitted and accepted at **ICLR 2026**. The arxiv v3 revision (March 2026) is consistent with a camera-ready update after ICLR 2026 acceptance decisions. However, the author's own website has not been updated to reflect this, so there is some uncertainty. The weight of evidence (arxiv metadata, search snippets, presentation reference) suggests it **was accepted at ICLR 2026**, but I cannot find an unambiguous official \"accept\" decision on OpenReview for the ICLR 2026 submission specifically.\n\n---\n\nSources:\n- [arXiv page: 2502.03799](https://arxiv.org/abs/2502.03799)\n- [arXiv HTML version](https://arxiv.org/html/2502.03799)\n- [OpenReview submission](https://openreview.net/forum?id=2bWf4M5tRo)\n- [alphaXiv overview](https://www.alphaxiv.org/ja/overview/2502.03799v1)\n- [Litian Liu personal page](https://litianliu.github.io/)\n- [ICLR 2026 Papers](https://iclr.cc/virtual/2026/papers.html)"
      }
    ],
    "totalDurationMs": 159821,
    "totalTokens": 21166,
    "totalToolUseCount": 18,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 476,
      "cache_read_input_tokens": 19448,
      "output_tokens": 1241,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 476
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1241,
          "cache_read_input_tokens": 19448,
          "cache_creation_input_tokens": 476,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 476,
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
  "sourceToolAssistantUUID": "fbf08c7c-0acb-47cb-99b3-5a14c15e2327",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1c70a808-ac42-40e9-b451-f24d9f6e7546",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 20 · 2026-05-16T09:47:15.499Z_

Good. I've verified the key papers exist. Now let me check additional critical aspects: the EMNLP 2026 ARR deadline, and search for work that specifically does what LSP proposes (KL divergence of logit distributions after residual-stream perturbation for high-confidence hallucinations).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "50898e08-0ce9-4790-ad2c-d5ddbe45045c",
  "isSidechain": false,
  "requestId": "req_011Cb632aBoNydYEowvJtdom",
  "type": "assistant",
  "uuid": "90335c87-7f0b-4e7c-bb0f-9a8b5b008c88",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1c70a808-ac42-40e9-b451-f24d9f6e7546",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W9wGdkzyi87R4vELMJPo55",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4537,
      "cache_creation_input_tokens": 3426,
      "cache_read_input_tokens": 25445,
      "output_tokens": 896,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3426,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4537,
          "output_tokens": 896,
          "cache_read_input_tokens": 25445,
          "cache_creation_input_tokens": 3426,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3426
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

_source line 21 · 2026-05-16T09:47:18.712Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01Pv7VeRwaCoGaUY5vJv5zcY`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Verify ARR May 2026 deadline",
  "prompt": "Search the web for \"ARR submission deadline May 2026\" or \"ACL Rolling Review May 2026 deadline\" to verify whether there is an ARR submission deadline around May 25, 2026 for EMNLP 2026. Also check what the EMNLP 2026 commitment deadline is. Use WebSearch."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "90335c87-7f0b-4e7c-bb0f-9a8b5b008c88",
  "isSidechain": false,
  "requestId": "req_011Cb632aBoNydYEowvJtdom",
  "type": "assistant",
  "uuid": "50dea839-1d4a-462e-a064-a6a0f0ab8229",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1c70a808-ac42-40e9-b451-f24d9f6e7546",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W9wGdkzyi87R4vELMJPo55",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4537,
      "cache_creation_input_tokens": 3426,
      "cache_read_input_tokens": 25445,
      "output_tokens": 896,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3426,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4537,
          "output_tokens": 896,
          "cache_read_input_tokens": 25445,
          "cache_creation_input_tokens": 3426,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3426
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

_source line 22 · 2026-05-16T09:47:26.331Z_

<details open><summary>🔧 Tool call — Agent · `toolu_017ZnpEPubQYnbG7XKvT5fnC`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Check SSP vs LSP differentiation",
  "prompt": "I need to understand the exact difference between these methods for hallucination detection:\n\n1. \"Shaking to Reveal\" / SSP (arxiv 2506.02696) - uses perturbation sensitivity at intermediate representations with a trained encoder\n2. SHINE (arxiv 2411.09689) - perturbs entity embeddings and measures KL divergence of output distributions\n3. A proposed method called \"LSP\" that would inject Gaussian noise into the residual stream at intermediate layers and measure KL divergence between clean and perturbed OUTPUT logit distributions\n\nThe key question: Does SHINE already do essentially what LSP proposes? SHINE perturbs embeddings and measures KL divergence of outputs. LSP proposes perturbing the residual stream at intermediate layers and measuring KL divergence of output logits.\n\nSearch for the SHINE paper (arxiv 2411.09689) and use WebFetch to read its methodology section carefully. I need to know:\n1. Does SHINE perturb at the INPUT embedding level only, or also at intermediate layers?\n2. Does SHINE measure KL divergence of the full output distribution (logits), or something else?\n3. Does SHINE specifically target high-confidence hallucinations?\n4. What is the key technical difference if you perturb intermediate residual stream vs input embeddings?\n\nReport your findings."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "50dea839-1d4a-462e-a064-a6a0f0ab8229",
  "isSidechain": false,
  "requestId": "req_011Cb632aBoNydYEowvJtdom",
  "type": "assistant",
  "uuid": "416aa589-280b-4d3b-b2f3-d2ed851c56c7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1c70a808-ac42-40e9-b451-f24d9f6e7546",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W9wGdkzyi87R4vELMJPo55",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4537,
      "cache_creation_input_tokens": 3426,
      "cache_read_input_tokens": 25445,
      "output_tokens": 896,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3426,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4537,
          "output_tokens": 896,
          "cache_read_input_tokens": 25445,
          "cache_creation_input_tokens": 3426,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3426
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

_source line 23 · 2026-05-16T09:47:32.420Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01VYBVRCK3dgFbG59dqVJAxc`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Check Qwen3.6-27B and DeepSeek-V4-Flash existence",
  "prompt": "Search the web to verify whether these models exist and are publicly available:\n1. \"Qwen3.6-27B\" - is this a real model? Search for \"Qwen3.6\" or \"Qwen 3.6 27B\". Also check if maybe the correct name is \"Qwen2.5-72B\" or \"Qwen3-27B\" or similar.\n2. \"DeepSeek-V4-Flash\" - is this a real model? Search for \"DeepSeek V4\" or \"DeepSeek-V4-Flash\". Check if maybe it should be \"DeepSeek-V3\" or \"DeepSeek-R1\".\n\nReport what you find about whether these specific model names are real and available."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "416aa589-280b-4d3b-b2f3-d2ed851c56c7",
  "isSidechain": false,
  "requestId": "req_011Cb632aBoNydYEowvJtdom",
  "type": "assistant",
  "uuid": "62a3d510-213f-4dd5-abe1-530854844639",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1c70a808-ac42-40e9-b451-f24d9f6e7546",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W9wGdkzyi87R4vELMJPo55",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4537,
      "cache_creation_input_tokens": 3426,
      "cache_read_input_tokens": 25445,
      "output_tokens": 896,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3426,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4537,
          "output_tokens": 896,
          "cache_read_input_tokens": 25445,
          "cache_creation_input_tokens": 3426,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3426
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

_source line 24 · 2026-05-16T09:47:49.089Z_

<details><summary>↩ Tool result · `toolu_01Pv7VeRwaCoGaUY5vJv5zcY`</summary>

```text
Here is what I found from the web searches:

## ARR Submission Deadline for EMNLP 2026

There is indeed an **ARR submission deadline of May 25, 2026** for papers targeting EMNLP 2026. This was confirmed by the official EMNLP 2026 Twitter/X account, which announced:

> "ARR Submission Deadline: May 25, 2026"

This means that May 25, 2026 is the last ARR cycle in which you can submit a paper and still have it reviewed in time to commit to EMNLP 2026. Papers submitted to ARR in the May 2026 cycle (or earlier cycles) that receive reviews and a meta-review can then be committed to EMNLP 2026.

**Important note:** According to the EMNLP 2026 submission policy, authors submitting to the ARR May 2026 cycle must explicitly declare that they intend to commit to EMNLP 2026 at submission time, and this choice is binding.

## EMNLP 2026 Commitment Deadline

The **EMNLP 2026 commitment deadline is August 2, 2026**. This is the date by which authors with reviewed ARR papers must commit them to EMNLP 2026 via the commitment link.

## Summary of Key Dates

| Milestone | Date |
|-----------|------|
| ARR Submission Deadline (last cycle for EMNLP 2026) | May 25, 2026 |
| EMNLP 2026 Commitment Deadline | August 2, 2026 |

Sources:
- [Call for Main Conference Papers - EMNLP 2026](https://2026.emnlp.org/calls/main_conference_papers/)
- [EMNLP 2026 on X (ARR Submission Deadline announcement)](https://x.com/emnlpmeeting/status/2029508292637061462)
- [ACL Rolling Review - Dates and Venues](http://aclrollingreview.org/dates)
- [AI Conference Deadlines - EMNLP 2026](https://mlciv.com/ai-deadlines/conference/?id=emnlp26)
- [EMNLP 2026 Conference Deadline Tracker](https://www.getpaperpilot.com/deadlines/emnlp-2026.html)
- [Hugging Face AI Deadlines - EMNLP 2026 update](https://huggingface.co/spaces/huggingface/ai-deadlines/commit/2754f67c0550847973789522a0a082dd5443b5c0)

agentId: a075189d942fa438d (use SendMessage with to: 'a075189d942fa438d' to continue this agent)
&lt;usage>total_tokens: 13905
tool_uses: 5
duration_ms: 30372&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "50dea839-1d4a-462e-a064-a6a0f0ab8229",
  "isSidechain": false,
  "promptId": "ab5656e8-b9e4-40d4-bf76-8cf45c241dcf",
  "type": "user",
  "uuid": "d80f41fc-87e7-4572-b7a5-c131c1e9e47a",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Search the web for \"ARR submission deadline May 2026\" or \"ACL Rolling Review May 2026 deadline\" to verify whether there is an ARR submission deadline around May 25, 2026 for EMNLP 2026. Also check what the EMNLP 2026 commitment deadline is. Use WebSearch.",
    "agentId": "a075189d942fa438d",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here is what I found from the web searches:\n\n## ARR Submission Deadline for EMNLP 2026\n\nThere is indeed an **ARR submission deadline of May 25, 2026** for papers targeting EMNLP 2026. This was confirmed by the official EMNLP 2026 Twitter/X account, which announced:\n\n> \"ARR Submission Deadline: May 25, 2026\"\n\nThis means that May 25, 2026 is the last ARR cycle in which you can submit a paper and still have it reviewed in time to commit to EMNLP 2026. Papers submitted to ARR in the May 2026 cycle (or earlier cycles) that receive reviews and a meta-review can then be committed to EMNLP 2026.\n\n**Important note:** According to the EMNLP 2026 submission policy, authors submitting to the ARR May 2026 cycle must explicitly declare that they intend to commit to EMNLP 2026 at submission time, and this choice is binding.\n\n## EMNLP 2026 Commitment Deadline\n\nThe **EMNLP 2026 commitment deadline is August 2, 2026**. This is the date by which authors with reviewed ARR papers must commit them to EMNLP 2026 via the commitment link.\n\n## Summary of Key Dates\n\n| Milestone | Date |\n|-----------|------|\n| ARR Submission Deadline (last cycle for EMNLP 2026) | May 25, 2026 |\n| EMNLP 2026 Commitment Deadline | August 2, 2026 |\n\nSources:\n- [Call for Main Conference Papers - EMNLP 2026](https://2026.emnlp.org/calls/main_conference_papers/)\n- [EMNLP 2026 on X (ARR Submission Deadline announcement)](https://x.com/emnlpmeeting/status/2029508292637061462)\n- [ACL Rolling Review - Dates and Venues](http://aclrollingreview.org/dates)\n- [AI Conference Deadlines - EMNLP 2026](https://mlciv.com/ai-deadlines/conference/?id=emnlp26)\n- [EMNLP 2026 Conference Deadline Tracker](https://www.getpaperpilot.com/deadlines/emnlp-2026.html)\n- [Hugging Face AI Deadlines - EMNLP 2026 update](https://huggingface.co/spaces/huggingface/ai-deadlines/commit/2754f67c0550847973789522a0a082dd5443b5c0)"
      }
    ],
    "totalDurationMs": 30372,
    "totalTokens": 13905,
    "totalToolUseCount": 5,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1453,
      "cache_read_input_tokens": 11790,
      "output_tokens": 661,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1453
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 661,
          "cache_read_input_tokens": 11790,
          "cache_creation_input_tokens": 1453,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1453,
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
  "sourceToolAssistantUUID": "50dea839-1d4a-462e-a064-a6a0f0ab8229",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1c70a808-ac42-40e9-b451-f24d9f6e7546",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-16T09:48:01.904Z_

<details><summary>↩ Tool result · `toolu_01VYBVRCK3dgFbG59dqVJAxc`</summary>

```text
Here are my findings:

---

## 1. Qwen3.6-27B -- YES, this is a real model

**Qwen3.6-27B** is a real, publicly available model. It was released by Alibaba's Qwen team on April 22, 2026. Key facts:

- It is a 27-billion-parameter **dense** (not MoE) open-weight model focused on agentic coding.
- It outperforms the previous-generation Qwen3.5-397B-A17B (a much larger MoE model) on coding benchmarks like SWE-bench Verified.
- It is natively multimodal (vision + language).
- It uses a hybrid architecture with Gated DeltaNet and Gated Attention layers.
- Released under the Apache 2.0 license and available on Hugging Face, Qwen Studio, and OpenRouter.

So the name "Qwen3.6-27B" is correct. It is distinct from "Qwen2.5-72B" (an older, larger model from the Qwen2.5 generation) and from "Qwen3-27B" (which would be from the earlier Qwen3 series, not 3.6).

---

## 2. DeepSeek-V4-Flash -- YES, this is a real model

**DeepSeek-V4-Flash** is a real, publicly available model. It was released by DeepSeek on April 24, 2026. Key facts:

- It is an efficiency-optimized Mixture-of-Experts model with 284B total parameters and 13B activated parameters.
- It supports a 1M-token context window.
- It was released alongside DeepSeek-V4-Pro under the MIT license.
- It is available via the DeepSeek API, on Hugging Face, and through providers like OpenRouter and NVIDIA NIM.
- Pricing is very low at $0.14 / $0.28 per 1M input/output tokens.

So the name "DeepSeek-V4-Flash" is correct. It is the successor to DeepSeek-V3 (released earlier) and is distinct from DeepSeek-R1 (which is a reasoning-focused model from a different product line).

---

## Summary

Both model names are real and publicly available as of 2026:

| Model | Real? | Released | License |
|-------|-------|----------|---------|
| Qwen3.6-27B | Yes | April 22, 2026 | Apache 2.0 |
| DeepSeek-V4-Flash | Yes | April 24, 2026 | MIT |

Sources:
- [Qwen3.6-27B Blog Post](https://qwen.ai/blog?id=qwen3.6-27b)
- [Qwen3.6-27B on Hugging Face](https://huggingface.co/Qwen/Qwen3.6-27B)
- [Qwen3.6-27B on OpenRouter](https://openrouter.ai/qwen/qwen3.6-27b)
- [MarkTechPost: Alibaba Releases Qwen3.6-27B](https://www.marktechpost.com/2026/04/22/alibaba-qwen-team-releases-qwen3-6-27b-a-dense-open-weight-model-outperforming-397b-moe-on-agentic-coding-benchmarks/)
- [DeepSeek-V4-Flash on Hugging Face](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash)
- [DeepSeek V4 Preview Release API Docs](https://api-docs.deepseek.com/news/news260424)
- [DeepSeek V4 Flash on OpenRouter](https://openrouter.ai/deepseek/deepseek-v4-flash)
- [DeepSeek V4 Flash Review (BuildFastWithAI)](https://www.buildfastwithai.com/blogs/deepseek-v4-flash-review-2026)

agentId: a0ecdebe09b1b6a64 (use SendMessage with to: 'a0ecdebe09b1b6a64' to continue this agent)
&lt;usage>total_tokens: 13697
tool_uses: 3
duration_ms: 29482&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "62a3d510-213f-4dd5-abe1-530854844639",
  "isSidechain": false,
  "promptId": "ab5656e8-b9e4-40d4-bf76-8cf45c241dcf",
  "type": "user",
  "uuid": "d0d9673d-dde2-47d7-9fdc-a547fc12f959",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Search the web to verify whether these models exist and are publicly available:\n1. \"Qwen3.6-27B\" - is this a real model? Search for \"Qwen3.6\" or \"Qwen 3.6 27B\". Also check if maybe the correct name is \"Qwen2.5-72B\" or \"Qwen3-27B\" or similar.\n2. \"DeepSeek-V4-Flash\" - is this a real model? Search for \"DeepSeek V4\" or \"DeepSeek-V4-Flash\". Check if maybe it should be \"DeepSeek-V3\" or \"DeepSeek-R1\".\n\nReport what you find about whether these specific model names are real and available.",
    "agentId": "a0ecdebe09b1b6a64",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here are my findings:\n\n---\n\n## 1. Qwen3.6-27B -- YES, this is a real model\n\n**Qwen3.6-27B** is a real, publicly available model. It was released by Alibaba's Qwen team on April 22, 2026. Key facts:\n\n- It is a 27-billion-parameter **dense** (not MoE) open-weight model focused on agentic coding.\n- It outperforms the previous-generation Qwen3.5-397B-A17B (a much larger MoE model) on coding benchmarks like SWE-bench Verified.\n- It is natively multimodal (vision + language).\n- It uses a hybrid architecture with Gated DeltaNet and Gated Attention layers.\n- Released under the Apache 2.0 license and available on Hugging Face, Qwen Studio, and OpenRouter.\n\nSo the name \"Qwen3.6-27B\" is correct. It is distinct from \"Qwen2.5-72B\" (an older, larger model from the Qwen2.5 generation) and from \"Qwen3-27B\" (which would be from the earlier Qwen3 series, not 3.6).\n\n---\n\n## 2. DeepSeek-V4-Flash -- YES, this is a real model\n\n**DeepSeek-V4-Flash** is a real, publicly available model. It was released by DeepSeek on April 24, 2026. Key facts:\n\n- It is an efficiency-optimized Mixture-of-Experts model with 284B total parameters and 13B activated parameters.\n- It supports a 1M-token context window.\n- It was released alongside DeepSeek-V4-Pro under the MIT license.\n- It is available via the DeepSeek API, on Hugging Face, and through providers like OpenRouter and NVIDIA NIM.\n- Pricing is very low at $0.14 / $0.28 per 1M input/output tokens.\n\nSo the name \"DeepSeek-V4-Flash\" is correct. It is the successor to DeepSeek-V3 (released earlier) and is distinct from DeepSeek-R1 (which is a reasoning-focused model from a different product line).\n\n---\n\n## Summary\n\nBoth model names are real and publicly available as of 2026:\n\n| Model | Real? | Released | License |\n|-------|-------|----------|---------|\n| Qwen3.6-27B | Yes | April 22, 2026 | Apache 2.0 |\n| DeepSeek-V4-Flash | Yes | April 24, 2026 | MIT |\n\nSources:\n- [Qwen3.6-27B Blog Post](https://qwen.ai/blog?id=qwen3.6-27b)\n- [Qwen3.6-27B on Hugging Face](https://huggingface.co/Qwen/Qwen3.6-27B)\n- [Qwen3.6-27B on OpenRouter](https://openrouter.ai/qwen/qwen3.6-27b)\n- [MarkTechPost: Alibaba Releases Qwen3.6-27B](https://www.marktechpost.com/2026/04/22/alibaba-qwen-team-releases-qwen3-6-27b-a-dense-open-weight-model-outperforming-397b-moe-on-agentic-coding-benchmarks/)\n- [DeepSeek-V4-Flash on Hugging Face](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash)\n- [DeepSeek V4 Preview Release API Docs](https://api-docs.deepseek.com/news/news260424)\n- [DeepSeek V4 Flash on OpenRouter](https://openrouter.ai/deepseek/deepseek-v4-flash)\n- [DeepSeek V4 Flash Review (BuildFastWithAI)](https://www.buildfastwithai.com/blogs/deepseek-v4-flash-review-2026)"
      }
    ],
    "totalDurationMs": 29482,
    "totalTokens": 13697,
    "totalToolUseCount": 3,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2345,
      "cache_read_input_tokens": 10340,
      "output_tokens": 1011,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2345
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1011,
          "cache_read_input_tokens": 10340,
          "cache_creation_input_tokens": 2345,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2345,
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
      "otherToolCount": 3
    }
  },
  "sourceToolAssistantUUID": "62a3d510-213f-4dd5-abe1-530854844639",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1c70a808-ac42-40e9-b451-f24d9f6e7546",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-16T09:49:03.241Z_

<details><summary>↩ Tool result · `toolu_017ZnpEPubQYnbG7XKvT5fnC`</summary>

```text
I now have all the technical details needed to provide a comprehensive answer. Here is my analysis:

---

## Findings: SHINE vs. SSP vs. the Proposed "LSP"

### 1. SHINE (arxiv 2411.09689) - Exact Mechanism

**Where perturbation is applied:** Exclusively at the **input embedding layer (layer 0)**. Gaussian noise is added to the token embeddings of key entities (subjects) in the prompt. Specifically: `e_hat = e + epsilon` where `epsilon ~ N(0, (3*sigma)^2)`. The noise magnitude is weighted by attention scores and negative log-likelihood. No intermediate layers are perturbed.

**What is measured:** Two things, both at the **output distribution level**:
- **KL divergence** `KL(P_i || P_hat_i)` at each token position, comparing full vocabulary distributions between clean and perturbed forward passes (used in the Model Knowledge Test stage)
- **Delta P_i** = `P_hat_i(t_i) - P_i(t_i)`, the change in generation probability of the specific generated token (used in the Alignment Test stage)

Scores are aggregated by taking the mean of the top-p% values across token positions. The process is repeated 10 times with different random seeds to reduce noise variance.

**Does it target high-confidence hallucinations?** Yes, indirectly. The two-stage design (MKT then Alignment Test) specifically detects cases where the model generates text confidently despite lacking relevant knowledge - the perturbation has minimal effect on outputs when the model is fabricating (since the entity knowledge isn't being used anyway).

---

### 2. SSP / "Shaking to Reveal" (arxiv 2506.02696) - Exact Mechanism

**Where perturbation is applied:** At the **input embedding level**, but via a learned MLP that generates sample-specific noise prompts (not raw Gaussian noise). The perturbation is semantically structured.

**What is measured:** **Intermediate-layer hidden states** (NOT output logits). The method extracts representations at middle transformer layers from both clean and perturbed runs, then computes cosine distance: `Disc(z, z_tilde) = 1 - cos(z, z_tilde)`. A trained lightweight encoder amplifies representational differences via contrastive learning.

**Key distinction from SHINE:** SSP perturbs at embeddings but **measures at intermediate representations**, while SHINE perturbs at embeddings and **measures at output distributions**. SSP also requires supervised training of both the noise generator and the encoder.

---

### 3. Does SHINE Already Do What "LSP" Proposes?

The proposed LSP method:
- Perturbs the **residual stream at intermediate layers** (not input embeddings)
- Measures **KL divergence of output logit distributions**

**SHINE does NOT already do what LSP proposes.** The critical differences:

| Aspect | SHINE | Proposed LSP |
|--------|-------|-------------|
| Perturbation location | Input embeddings (layer 0) | Intermediate residual stream |
| Measurement location | Output logits | Output logits |
| Perturbation type | Gaussian noise on entity tokens | Gaussian noise on residual stream |
| Training required | None | None (as described) |

SHINE and LSP share the measurement mechanism (KL divergence of output distributions) but differ fundamentally in **where the perturbation is injected**.

---

### 4. Key Technical Difference: Intermediate Residual Stream vs. Input Embeddings

This is the most important conceptual distinction:

1. **Input embedding perturbation (SHINE):** Tests whether the model's output depends on the *identity* of the entity. If you corrupt the entity's embedding and the output barely changes, the model wasn't actually using entity-specific knowledge -- it was fabricating. This is a test of **knowledge retrieval dependency**.

2. **Intermediate residual stream perturbation (LSP):** Tests the **stability of the computation at a specific processing stage**. By the time information reaches intermediate layers, the model has already performed attention operations and begun composing representations. Perturbing here tests whether the model's downstream computation is robust -- a different question than whether it depends on the input entity. Hallucinated content might be generated via "shortcut" circuits that are less robust to mid-computation noise, or conversely, might be generated by highly stable but disconnected circuits.

3. **Intermediate representation measurement (SSP):** Measures how internal representations shift, which captures different information than output distribution shifts. Internal representations encode more than just next-token predictions.

**The gap LSP fills:** Neither SHINE nor SSP does exactly what LSP proposes. SHINE perturbs inputs and measures outputs. SSP perturbs inputs and measures intermediate states. LSP would perturb intermediate states and measure outputs -- a genuinely distinct combination that tests a different hypothesis: that hallucinated tokens arise from fragile intermediate computations that, when disturbed, produce different output distributions (high KL), while factually grounded tokens arise from robust intermediate computations (low KL when perturbed).

**However**, there is no published ablation in the SHINE paper comparing perturbation at different depths. The paper simply followed prior work (GPT-2 knowledge probing) without justifying the choice of layer 0. LSP's hypothesis that intermediate-layer perturbation would be more informative is plausible but unvalidated by either paper.

agentId: a527b027893fcf9f6 (use SendMessage with to: 'a527b027893fcf9f6' to continue this agent)
&lt;usage>total_tokens: 17105
tool_uses: 7
duration_ms: 96907&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "416aa589-280b-4d3b-b2f3-d2ed851c56c7",
  "isSidechain": false,
  "promptId": "ab5656e8-b9e4-40d4-bf76-8cf45c241dcf",
  "type": "user",
  "uuid": "ddf81383-513d-4b52-82db-83c0703b0613",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to understand the exact difference between these methods for hallucination detection:\n\n1. \"Shaking to Reveal\" / SSP (arxiv 2506.02696) - uses perturbation sensitivity at intermediate representations with a trained encoder\n2. SHINE (arxiv 2411.09689) - perturbs entity embeddings and measures KL divergence of output distributions\n3. A proposed method called \"LSP\" that would inject Gaussian noise into the residual stream at intermediate layers and measure KL divergence between clean and perturbed OUTPUT logit distributions\n\nThe key question: Does SHINE already do essentially what LSP proposes? SHINE perturbs embeddings and measures KL divergence of outputs. LSP proposes perturbing the residual stream at intermediate layers and measuring KL divergence of output logits.\n\nSearch for the SHINE paper (arxiv 2411.09689) and use WebFetch to read its methodology section carefully. I need to know:\n1. Does SHINE perturb at the INPUT embedding level only, or also at intermediate layers?\n2. Does SHINE measure KL divergence of the full output distribution (logits), or something else?\n3. Does SHINE specifically target high-confidence hallucinations?\n4. What is the key technical difference if you perturb intermediate residual stream vs input embeddings?\n\nReport your findings.",
    "agentId": "a527b027893fcf9f6",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "I now have all the technical details needed to provide a comprehensive answer. Here is my analysis:\n\n---\n\n## Findings: SHINE vs. SSP vs. the Proposed \"LSP\"\n\n### 1. SHINE (arxiv 2411.09689) - Exact Mechanism\n\n**Where perturbation is applied:** Exclusively at the **input embedding layer (layer 0)**. Gaussian noise is added to the token embeddings of key entities (subjects) in the prompt. Specifically: `e_hat = e + epsilon` where `epsilon ~ N(0, (3*sigma)^2)`. The noise magnitude is weighted by attention scores and negative log-likelihood. No intermediate layers are perturbed.\n\n**What is measured:** Two things, both at the **output distribution level**:\n- **KL divergence** `KL(P_i || P_hat_i)` at each token position, comparing full vocabulary distributions between clean and perturbed forward passes (used in the Model Knowledge Test stage)\n- **Delta P_i** = `P_hat_i(t_i) - P_i(t_i)`, the change in generation probability of the specific generated token (used in the Alignment Test stage)\n\nScores are aggregated by taking the mean of the top-p% values across token positions. The process is repeated 10 times with different random seeds to reduce noise variance.\n\n**Does it target high-confidence hallucinations?** Yes, indirectly. The two-stage design (MKT then Alignment Test) specifically detects cases where the model generates text confidently despite lacking relevant knowledge - the perturbation has minimal effect on outputs when the model is fabricating (since the entity knowledge isn't being used anyway).\n\n---\n\n### 2. SSP / \"Shaking to Reveal\" (arxiv 2506.02696) - Exact Mechanism\n\n**Where perturbation is applied:** At the **input embedding level**, but via a learned MLP that generates sample-specific noise prompts (not raw Gaussian noise). The perturbation is semantically structured.\n\n**What is measured:** **Intermediate-layer hidden states** (NOT output logits). The method extracts representations at middle transformer layers from both clean and perturbed runs, then computes cosine distance: `Disc(z, z_tilde) = 1 - cos(z, z_tilde)`. A trained lightweight encoder amplifies representational differences via contrastive learning.\n\n**Key distinction from SHINE:** SSP perturbs at embeddings but **measures at intermediate representations**, while SHINE perturbs at embeddings and **measures at output distributions**. SSP also requires supervised training of both the noise generator and the encoder.\n\n---\n\n### 3. Does SHINE Already Do What \"LSP\" Proposes?\n\nThe proposed LSP method:\n- Perturbs the **residual stream at intermediate layers** (not input embeddings)\n- Measures **KL divergence of output logit distributions**\n\n**SHINE does NOT already do what LSP proposes.** The critical differences:\n\n| Aspect | SHINE | Proposed LSP |\n|--------|-------|-------------|\n| Perturbation location | Input embeddings (layer 0) | Intermediate residual stream |\n| Measurement location | Output logits | Output logits |\n| Perturbation type | Gaussian noise on entity tokens | Gaussian noise on residual stream |\n| Training required | None | None (as described) |\n\nSHINE and LSP share the measurement mechanism (KL divergence of output distributions) but differ fundamentally in **where the perturbation is injected**.\n\n---\n\n### 4. Key Technical Difference: Intermediate Residual Stream vs. Input Embeddings\n\nThis is the most important conceptual distinction:\n\n1. **Input embedding perturbation (SHINE):** Tests whether the model's output depends on the *identity* of the entity. If you corrupt the entity's embedding and the output barely changes, the model wasn't actually using entity-specific knowledge -- it was fabricating. This is a test of **knowledge retrieval dependency**.\n\n2. **Intermediate residual stream perturbation (LSP):** Tests the **stability of the computation at a specific processing stage**. By the time information reaches intermediate layers, the model has already performed attention operations and begun composing representations. Perturbing here tests whether the model's downstream computation is robust -- a different question than whether it depends on the input entity. Hallucinated content might be generated via \"shortcut\" circuits that are less robust to mid-computation noise, or conversely, might be generated by highly stable but disconnected circuits.\n\n3. **Intermediate representation measurement (SSP):** Measures how internal representations shift, which captures different information than output distribution shifts. Internal representations encode more than just next-token predictions.\n\n**The gap LSP fills:** Neither SHINE nor SSP does exactly what LSP proposes. SHINE perturbs inputs and measures outputs. SSP perturbs inputs and measures intermediate states. LSP would perturb intermediate states and measure outputs -- a genuinely distinct combination that tests a different hypothesis: that hallucinated tokens arise from fragile intermediate computations that, when disturbed, produce different output distributions (high KL), while factually grounded tokens arise from robust intermediate computations (low KL when perturbed).\n\n**However**, there is no published ablation in the SHINE paper comparing perturbation at different depths. The paper simply followed prior work (GPT-2 knowledge probing) without justifying the choice of layer 0. LSP's hypothesis that intermediate-layer perturbation would be more informative is plausible but unvalidated by either paper."
      }
    ],
    "totalDurationMs": 96907,
    "totalTokens": 17105,
    "totalToolUseCount": 7,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 625,
      "cache_read_input_tokens": 15206,
      "output_tokens": 1273,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 625
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1273,
          "cache_read_input_tokens": 15206,
          "cache_creation_input_tokens": 625,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 625,
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
      "otherToolCount": 7
    }
  },
  "sourceToolAssistantUUID": "416aa589-280b-4d3b-b2f3-d2ed851c56c7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1c70a808-ac42-40e9-b451-f24d9f6e7546",
  "version": "2.1.126",
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
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-16 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "ddf81383-513d-4b52-82db-83c0703b0613",
  "sessionId": "1c70a808-ac42-40e9-b451-f24d9f6e7546"
}
```

---

### Runtime record

_source line 28_

```json
{
  "type": "ai-title",
  "aiTitle": "Verify LSP method against Liu et al. and assess CHOKE subset feasibility",
  "sessionId": "1c70a808-ac42-40e9-b451-f24d9f6e7546"
}
```

---

### Assistant

_source line 29 · 2026-05-16T09:49:08.562Z_

<details><summary>Logged reasoning block</summary>

```text
Excellent. Now I have a comprehensive picture. Let me do one more critical search to check the theoretical validity of the "KL divergence as Hessian trace approximation" claim, and to look for any very recent concurrent work that also does residual-stream perturbation with logit KL measurement.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ddf81383-513d-4b52-82db-83c0703b0613",
  "isSidechain": false,
  "requestId": "req_011Cb63B5Dmt2BHmB4U6Dc6Q",
  "type": "assistant",
  "uuid": "66a793ce-e351-4ee6-bc6c-69531b46125c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1c70a808-ac42-40e9-b451-f24d9f6e7546",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RbGQAM2JCP6QNP8A46jHw4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1116,
      "cache_creation_input_tokens": 7556,
      "cache_read_input_tokens": 28871,
      "output_tokens": 715,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7556,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1116,
          "output_tokens": 715,
          "cache_read_input_tokens": 28871,
          "cache_creation_input_tokens": 7556,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7556
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

_source line 30 · 2026-05-16T09:49:09.596Z_

Now let me check the theoretical claim and look for one more critical angle.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "66a793ce-e351-4ee6-bc6c-69531b46125c",
  "isSidechain": false,
  "requestId": "req_011Cb63B5Dmt2BHmB4U6Dc6Q",
  "type": "assistant",
  "uuid": "17c79580-5fc8-42fb-8843-983f318a72eb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1c70a808-ac42-40e9-b451-f24d9f6e7546",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RbGQAM2JCP6QNP8A46jHw4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1116,
      "cache_creation_input_tokens": 7556,
      "cache_read_input_tokens": 28871,
      "output_tokens": 715,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7556,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1116,
          "output_tokens": 715,
          "cache_read_input_tokens": 28871,
          "cache_creation_input_tokens": 7556,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7556
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

_source line 31 · 2026-05-16T09:49:16.030Z_

<details open><summary>🔧 Tool call — Agent · `toolu_0197FEGz2ceTfs4WAMocGiAy`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Check KL-Hessian theory validity",
  "prompt": "I need to verify a theoretical claim: \"KL divergence between clean and noise-perturbed output logit distributions is a finite-difference approximation of the output Hessian trace (Tr(H_output)) with respect to residual perturbation—a direct, gradient-free sharpness measure.\"\n\nSearch for papers or resources that establish this mathematical relationship. Specifically:\n1. Is it true that E[KL(p_clean || p_noisy)] ≈ (σ²/2) * Tr(H) for small Gaussian noise with variance σ²? This would be a second-order Taylor expansion result.\n2. Search for \"KL divergence Hessian trace approximation\" or \"KL divergence Fisher information perturbation\"\n3. Search for \"randomized smoothing Hessian estimation\" or \"finite difference Hessian trace estimation\"\n\nThe key question: Is this relationship mathematically valid, and if so, under what conditions (e.g., small noise, smooth landscape)? Is it a well-known result or a novel theoretical contribution?\n\nReport what you find about the validity of this claim."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "17c79580-5fc8-42fb-8843-983f318a72eb",
  "isSidechain": false,
  "requestId": "req_011Cb63B5Dmt2BHmB4U6Dc6Q",
  "type": "assistant",
  "uuid": "cc941630-f89c-49c2-a90f-4460cde930f7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1c70a808-ac42-40e9-b451-f24d9f6e7546",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RbGQAM2JCP6QNP8A46jHw4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1116,
      "cache_creation_input_tokens": 7556,
      "cache_read_input_tokens": 28871,
      "output_tokens": 715,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7556,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1116,
          "output_tokens": 715,
          "cache_read_input_tokens": 28871,
          "cache_creation_input_tokens": 7556,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7556
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

_source line 32 · 2026-05-16T09:49:20.992Z_

<details open><summary>🔧 Tool call — Agent · `toolu_016NJBidSBB6ehJn9AtD6yPd`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Search CHOKE-specific detection concurrent work",
  "prompt": "Search for recent papers (2025-2026) that specifically focus on detecting or mitigating HIGH-CONFIDENCE hallucinations in LLMs - cases where the model is very confident but wrong. This is different from general hallucination detection. Search for:\n1. \"high confidence hallucination detection LLM 2025 2026\"\n2. \"confident wrong answer LLM detection\"\n3. \"stubborn hallucination\" detection\n4. \"overconfident LLM hallucination mitigation\"\n5. \"calibration high confidence error\"\n\nAlso search for \"CHOKE hallucination\" to see if anyone else has built on the Simhi et al. CHOKE framework.\n\nReport all papers found that specifically target the high-confidence/stubborn hallucination problem (not general hallucination detection)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cc941630-f89c-49c2-a90f-4460cde930f7",
  "isSidechain": false,
  "requestId": "req_011Cb63B5Dmt2BHmB4U6Dc6Q",
  "type": "assistant",
  "uuid": "7bfd6b61-0375-4b0b-92b6-23088458e08b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1c70a808-ac42-40e9-b451-f24d9f6e7546",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RbGQAM2JCP6QNP8A46jHw4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1116,
      "cache_creation_input_tokens": 7556,
      "cache_read_input_tokens": 28871,
      "output_tokens": 715,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7556,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1116,
          "output_tokens": 715,
          "cache_read_input_tokens": 28871,
          "cache_creation_input_tokens": 7556,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7556
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

_source line 33 · 2026-05-16T09:51:43.488Z_

<details><summary>↩ Tool result · `toolu_0197FEGz2ceTfs4WAMocGiAy`</summary>

````text
Now I have gathered sufficient information to provide a comprehensive analysis. Let me compile my findings.

## Analysis and Verdict

Based on my research, here is a detailed assessment of the theoretical claim.

---

### 1. Is E[KL(p_clean || p_noisy)] approximately equal to (sigma^2 / 2) * Tr(H) for small Gaussian noise?

**Yes, this is mathematically valid.** It follows from a well-known second-order Taylor expansion result. Here is the derivation chain:

**Step A: Second-order Taylor expansion of a function under Gaussian perturbation.**

For any sufficiently smooth scalar function f(x), if epsilon ~ N(0, sigma^2 * I), then:

```
E[f(x + epsilon)] = f(x) + (1/2) * trace(H_f(x) * Sigma)
```

where H_f is the Hessian of f and Sigma = sigma^2 * I. This simplifies to:

```
E[f(x + epsilon)] = f(x) + (sigma^2 / 2) * Tr(H_f(x))
```

This is the standard result from "Taylor expansions for the moments of functions of random variables" (see Wikipedia article on this topic). The first-order term vanishes because E[epsilon] = 0.

**Step B: Application to KL divergence as the function.**

Define f(epsilon) = KL(p_clean || p_{x+epsilon}), where p_{x+epsilon} is the output softmax distribution when the residual/input is perturbed by epsilon. At epsilon = 0, f(0) = 0 (KL of a distribution with itself). The gradient of KL at epsilon = 0 is also zero (since epsilon = 0 is a minimum of KL divergence — KL is non-negative and equals zero at the identity). Therefore:

```
E[KL(p_clean || p_noisy)] ≈ (sigma^2 / 2) * Tr(H_KL)
```

where H_KL is the Hessian of the KL divergence with respect to the perturbation, evaluated at zero perturbation. This Hessian is precisely related to the **Fisher Information Matrix** of the output distribution with respect to the input perturbation (or equivalently, the Hessian of the output with respect to the residual stream).

**Step C: Connection to Hutchinson's trace estimator.**

The Hutchinson trace estimator states that for any matrix A and random vector v with E[vv^T] = I:

```
E[v^T A v] = Tr(A)
```

This means that if you evaluate the quadratic form v^T H v for random vectors v (Rademacher or Gaussian), the expected value gives you the trace of H. The KL-divergence-based approach is doing essentially the same thing: injecting random perturbations and measuring the functional response (KL divergence) gives a stochastic estimate of the Hessian trace.

---

### 2. Under what conditions is this valid?

The approximation E[KL(p_clean || p_noisy)] ≈ (sigma^2 / 2) * Tr(H) holds under:

- **Small noise (sigma is small)**: The Taylor expansion is truncated at second order, so higher-order terms (O(sigma^4)) must be negligible.
- **Smooth landscape**: The function mapping input perturbations to output logit distributions must be twice-differentiable (C^2). For neural networks with smooth activations (GELU, SiLU, tanh), this holds. For ReLU networks, it holds almost everywhere.
- **Bounded Hessian**: The third and higher derivatives should not blow up, ensuring the Taylor remainder is controlled.

---

### 3. Is this a well-known result or a novel contribution?

**This is a well-known result in multiple communities**, though the specific framing for "output Hessian trace with respect to residual perturbation" as a sharpness measure may combine known pieces in a relatively novel way. The constituent results are established:

1. **KL divergence ≈ (1/2) * delta^T * F * delta** (Fisher information as local metric for KL divergence): This is foundational in information geometry, dating back to Rao (1945) and Jeffreys, and is covered in standard references like Amari's information geometry textbooks and Roger Grosse's CSC2541 lecture notes.

2. **E[f(x + epsilon)] = f(x) + (sigma^2/2) * Tr(H_f)**: This is a standard result in stochastic analysis and uncertainty propagation, documented on Wikipedia under "Taylor expansions for moments of functions of random variables."

3. **Hutchinson's trace estimator** (1989): The idea that random quadratic forms estimate matrix traces is a classic result in numerical linear algebra.

4. **Noise injection as implicit Hessian trace regularization**: Explicitly established in:
   - Camuto et al., "Explicit Regularisation in Gaussian Noise Injections" (NeurIPS 2020) — shows that marginalizing out injected Gaussian noise yields a regularizer related to the Hessian.
   - "Noise Stability Optimization for Finding Flat Minima: A Hessian-based Regularization Approach" (arXiv:2306.08553) — directly proves that the perturbed loss function F(W) ≈ f(W) + (sigma^2/2) * Tr(H) and designs algorithms exploiting this.
   - CR-SAM (AAAI 2024) — uses finite-difference Hessian trace estimation as a computationally efficient curvature measure.

5. **Fisher Information = Hessian of KL**: This identity (that the Fisher information matrix is the Hessian of KL divergence at the identity) is classical information geometry.

---

### 4. Specific claim about "output Hessian trace with respect to residual perturbation"

The claim packages these results for a specific use case: measuring the curvature of the **output logit distribution** (as measured by KL divergence) with respect to perturbations in the **residual stream** of a transformer. This is a valid and direct application of the theory above. The "output Hessian" in this context is specifically the Hessian of the map: residual_vector -> softmax_output_distribution, which measures how sensitive the network's predictions are to perturbations at a given layer.

Calling this a "gradient-free sharpness measure" is accurate because:
- You never compute explicit gradients or backpropagate
- You only need forward passes with perturbed inputs
- The KL divergence between clean and noisy outputs gives you a stochastic estimate of the Hessian trace

---

### Summary Verdict

The claim is **mathematically valid and well-grounded**. It is **not a novel theoretical contribution** in the sense that all the mathematical pieces are well-established (second-order Taylor expansion, Fisher-KL relationship, Hutchinson estimator, noise-as-regularization literature). However, the specific synthesis — applying it to measure output distribution sensitivity with respect to residual stream perturbations as a "gradient-free sharpness measure" — is a legitimate and potentially useful application that combines known results in a clear way. The papers by Camuto et al. (NeurIPS 2020) and the Noise Stability Optimization paper (2023) establish essentially the same mathematical relationship in the context of loss landscapes and weight perturbations.

---

Sources:
- [Taylor expansions for the moments of functions of random variables - Wikipedia](https://en.wikipedia.org/wiki/Taylor_expansions_for_the_moments_of_functions_of_random_variables)
- [Explicit Regularisation in Gaussian Noise Injections (NeurIPS 2020)](https://arxiv.org/abs/2007.07368)
- [Noise Stability Optimization for Finding Flat Minima (arXiv:2306.08553)](https://arxiv.org/abs/2306.08553)
- [CR-SAM: Curvature Regularized Sharpness-Aware Minimization (AAAI 2024)](https://arxiv.org/html/2312.13555v2)
- [CSC2541 Chapter 3: Metrics - Roger Grosse](https://www.cs.toronto.edu/~rgrosse/courses/csc2541_2022/readings/L03_metrics.pdf)
- [CSC2541 Chapter 2: Taylor Approximations - Roger Grosse](https://www.cs.toronto.edu/~rgrosse/courses/csc2541_2022/readings/L02_Taylor_approximations.pdf)
- [Hutchinson's Trick - Shakir Mohamed](https://blog.shakirm.com/2015/09/machine-learning-trick-of-the-day-3-hutchinsons-trick/)
- [Fisher Information - Princeton LIPS](https://lips.cs.princeton.edu/fisher-information/)
- [Fisher Information Metric - Wikipedia](https://en.wikipedia.org/wiki/Fisher_information_metric)
- [Kullback-Leibler Divergence - Wikipedia](https://en.wikipedia.org/wiki/Kullback%E2%80%93Leibler_divergence)
- [Stein's Lemma for Trace Estimation](https://ludwigwinkler.github.io/blog/TraceEstimation/)
- [Sebastian Nowozin - Thoughts on Trace Estimation in Deep Learning](https://www.nowozin.net/sebastian/blog/thoughts-on-trace-estimation-in-deep-learning.html)
- [Rethinking SAM as Variational Inference](https://opt-ml.org/papers/2022/paper102.pdf)
- [Fisher SAM: Information Geometry and Sharpness Aware Minimisation (ICML 2022)](https://proceedings.mlr.press/v162/kim22f/kim22f.pdf)

agentId: a222529fc27d4feb9 (use SendMessage with to: 'a222529fc27d4feb9' to continue this agent)
&lt;usage>total_tokens: 28686
tool_uses: 17
duration_ms: 147451&lt;/usage>
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "parentUuid": "cc941630-f89c-49c2-a90f-4460cde930f7",
  "isSidechain": false,
  "promptId": "ab5656e8-b9e4-40d4-bf76-8cf45c241dcf",
  "type": "user",
  "uuid": "6b423e52-fb5b-46c9-974a-3db61282e86b",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to verify a theoretical claim: \"KL divergence between clean and noise-perturbed output logit distributions is a finite-difference approximation of the output Hessian trace (Tr(H_output)) with respect to residual perturbation—a direct, gradient-free sharpness measure.\"\n\nSearch for papers or resources that establish this mathematical relationship. Specifically:\n1. Is it true that E[KL(p_clean || p_noisy)] ≈ (σ²/2) * Tr(H) for small Gaussian noise with variance σ²? This would be a second-order Taylor expansion result.\n2. Search for \"KL divergence Hessian trace approximation\" or \"KL divergence Fisher information perturbation\"\n3. Search for \"randomized smoothing Hessian estimation\" or \"finite difference Hessian trace estimation\"\n\nThe key question: Is this relationship mathematically valid, and if so, under what conditions (e.g., small noise, smooth landscape)? Is it a well-known result or a novel theoretical contribution?\n\nReport what you find about the validity of this claim.",
    "agentId": "a222529fc27d4feb9",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have gathered sufficient information to provide a comprehensive analysis. Let me compile my findings.\n\n## Analysis and Verdict\n\nBased on my research, here is a detailed assessment of the theoretical claim.\n\n---\n\n### 1. Is E[KL(p_clean || p_noisy)] approximately equal to (sigma^2 / 2) * Tr(H) for small Gaussian noise?\n\n**Yes, this is mathematically valid.** It follows from a well-known second-order Taylor expansion result. Here is the derivation chain:\n\n**Step A: Second-order Taylor expansion of a function under Gaussian perturbation.**\n\nFor any sufficiently smooth scalar function f(x), if epsilon ~ N(0, sigma^2 * I), then:\n\n```\nE[f(x + epsilon)] = f(x) + (1/2) * trace(H_f(x) * Sigma)\n```\n\nwhere H_f is the Hessian of f and Sigma = sigma^2 * I. This simplifies to:\n\n```\nE[f(x + epsilon)] = f(x) + (sigma^2 / 2) * Tr(H_f(x))\n```\n\nThis is the standard result from \"Taylor expansions for the moments of functions of random variables\" (see Wikipedia article on this topic). The first-order term vanishes because E[epsilon] = 0.\n\n**Step B: Application to KL divergence as the function.**\n\nDefine f(epsilon) = KL(p_clean || p_{x+epsilon}), where p_{x+epsilon} is the output softmax distribution when the residual/input is perturbed by epsilon. At epsilon = 0, f(0) = 0 (KL of a distribution with itself). The gradient of KL at epsilon = 0 is also zero (since epsilon = 0 is a minimum of KL divergence — KL is non-negative and equals zero at the identity). Therefore:\n\n```\nE[KL(p_clean || p_noisy)] ≈ (sigma^2 / 2) * Tr(H_KL)\n```\n\nwhere H_KL is the Hessian of the KL divergence with respect to the perturbation, evaluated at zero perturbation. This Hessian is precisely related to the **Fisher Information Matrix** of the output distribution with respect to the input perturbation (or equivalently, the Hessian of the output with respect to the residual stream).\n\n**Step C: Connection to Hutchinson's trace estimator.**\n\nThe Hutchinson trace estimator states that for any matrix A and random vector v with E[vv^T] = I:\n\n```\nE[v^T A v] = Tr(A)\n```\n\nThis means that if you evaluate the quadratic form v^T H v for random vectors v (Rademacher or Gaussian), the expected value gives you the trace of H. The KL-divergence-based approach is doing essentially the same thing: injecting random perturbations and measuring the functional response (KL divergence) gives a stochastic estimate of the Hessian trace.\n\n---\n\n### 2. Under what conditions is this valid?\n\nThe approximation E[KL(p_clean || p_noisy)] ≈ (sigma^2 / 2) * Tr(H) holds under:\n\n- **Small noise (sigma is small)**: The Taylor expansion is truncated at second order, so higher-order terms (O(sigma^4)) must be negligible.\n- **Smooth landscape**: The function mapping input perturbations to output logit distributions must be twice-differentiable (C^2). For neural networks with smooth activations (GELU, SiLU, tanh), this holds. For ReLU networks, it holds almost everywhere.\n- **Bounded Hessian**: The third and higher derivatives should not blow up, ensuring the Taylor remainder is controlled.\n\n---\n\n### 3. Is this a well-known result or a novel contribution?\n\n**This is a well-known result in multiple communities**, though the specific framing for \"output Hessian trace with respect to residual perturbation\" as a sharpness measure may combine known pieces in a relatively novel way. The constituent results are established:\n\n1. **KL divergence ≈ (1/2) * delta^T * F * delta** (Fisher information as local metric for KL divergence): This is foundational in information geometry, dating back to Rao (1945) and Jeffreys, and is covered in standard references like Amari's information geometry textbooks and Roger Grosse's CSC2541 lecture notes.\n\n2. **E[f(x + epsilon)] = f(x) + (sigma^2/2) * Tr(H_f)**: This is a standard result in stochastic analysis and uncertainty propagation, documented on Wikipedia under \"Taylor expansions for moments of functions of random variables.\"\n\n3. **Hutchinson's trace estimator** (1989): The idea that random quadratic forms estimate matrix traces is a classic result in numerical linear algebra.\n\n4. **Noise injection as implicit Hessian trace regularization**: Explicitly established in:\n   - Camuto et al., \"Explicit Regularisation in Gaussian Noise Injections\" (NeurIPS 2020) — shows that marginalizing out injected Gaussian noise yields a regularizer related to the Hessian.\n   - \"Noise Stability Optimization for Finding Flat Minima: A Hessian-based Regularization Approach\" (arXiv:2306.08553) — directly proves that the perturbed loss function F(W) ≈ f(W) + (sigma^2/2) * Tr(H) and designs algorithms exploiting this.\n   - CR-SAM (AAAI 2024) — uses finite-difference Hessian trace estimation as a computationally efficient curvature measure.\n\n5. **Fisher Information = Hessian of KL**: This identity (that the Fisher information matrix is the Hessian of KL divergence at the identity) is classical information geometry.\n\n---\n\n### 4. Specific claim about \"output Hessian trace with respect to residual perturbation\"\n\nThe claim packages these results for a specific use case: measuring the curvature of the **output logit distribution** (as measured by KL divergence) with respect to perturbations in the **residual stream** of a transformer. This is a valid and direct application of the theory above. The \"output Hessian\" in this context is specifically the Hessian of the map: residual_vector -> softmax_output_distribution, which measures how sensitive the network's predictions are to perturbations at a given layer.\n\nCalling this a \"gradient-free sharpness measure\" is accurate because:\n- You never compute explicit gradients or backpropagate\n- You only need forward passes with perturbed inputs\n- The KL divergence between clean and noisy outputs gives you a stochastic estimate of the Hessian trace\n\n---\n\n### Summary Verdict\n\nThe claim is **mathematically valid and well-grounded**. It is **not a novel theoretical contribution** in the sense that all the mathematical pieces are well-established (second-order Taylor expansion, Fisher-KL relationship, Hutchinson estimator, noise-as-regularization literature). However, the specific synthesis — applying it to measure output distribution sensitivity with respect to residual stream perturbations as a \"gradient-free sharpness measure\" — is a legitimate and potentially useful application that combines known results in a clear way. The papers by Camuto et al. (NeurIPS 2020) and the Noise Stability Optimization paper (2023) establish essentially the same mathematical relationship in the context of loss landscapes and weight perturbations.\n\n---\n\nSources:\n- [Taylor expansions for the moments of functions of random variables - Wikipedia](https://en.wikipedia.org/wiki/Taylor_expansions_for_the_moments_of_functions_of_random_variables)\n- [Explicit Regularisation in Gaussian Noise Injections (NeurIPS 2020)](https://arxiv.org/abs/2007.07368)\n- [Noise Stability Optimization for Finding Flat Minima (arXiv:2306.08553)](https://arxiv.org/abs/2306.08553)\n- [CR-SAM: Curvature Regularized Sharpness-Aware Minimization (AAAI 2024)](https://arxiv.org/html/2312.13555v2)\n- [CSC2541 Chapter 3: Metrics - Roger Grosse](https://www.cs.toronto.edu/~rgrosse/courses/csc2541_2022/readings/L03_metrics.pdf)\n- [CSC2541 Chapter 2: Taylor Approximations - Roger Grosse](https://www.cs.toronto.edu/~rgrosse/courses/csc2541_2022/readings/L02_Taylor_approximations.pdf)\n- [Hutchinson's Trick - Shakir Mohamed](https://blog.shakirm.com/2015/09/machine-learning-trick-of-the-day-3-hutchinsons-trick/)\n- [Fisher Information - Princeton LIPS](https://lips.cs.princeton.edu/fisher-information/)\n- [Fisher Information Metric - Wikipedia](https://en.wikipedia.org/wiki/Fisher_information_metric)\n- [Kullback-Leibler Divergence - Wikipedia](https://en.wikipedia.org/wiki/Kullback%E2%80%93Leibler_divergence)\n- [Stein's Lemma for Trace Estimation](https://ludwigwinkler.github.io/blog/TraceEstimation/)\n- [Sebastian Nowozin - Thoughts on Trace Estimation in Deep Learning](https://www.nowozin.net/sebastian/blog/thoughts-on-trace-estimation-in-deep-learning.html)\n- [Rethinking SAM as Variational Inference](https://opt-ml.org/papers/2022/paper102.pdf)\n- [Fisher SAM: Information Geometry and Sharpness Aware Minimisation (ICML 2022)](https://proceedings.mlr.press/v162/kim22f/kim22f.pdf)"
      }
    ],
    "totalDurationMs": 147451,
    "totalTokens": 28686,
    "totalToolUseCount": 17,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1037,
      "cache_read_input_tokens": 25240,
      "output_tokens": 2408,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1037
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2408,
          "cache_read_input_tokens": 25240,
          "cache_creation_input_tokens": 1037,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1037,
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
  "sourceToolAssistantUUID": "cc941630-f89c-49c2-a90f-4460cde930f7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1c70a808-ac42-40e9-b451-f24d9f6e7546",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
````

</details>

---

### Tool result

_source line 34 · 2026-05-16T09:52:05.010Z_

<details><summary>↩ Tool result · `toolu_016NJBidSBB6ehJn9AtD6yPd`</summary>

```text
Based on my extensive research, here is a comprehensive report of papers specifically targeting the high-confidence/stubborn hallucination problem in LLMs (2025-2026):

---

## Papers Specifically Targeting High-Confidence/Stubborn Hallucinations

### 1. CHOKE Framework - The Foundational Paper

**"Trust Me, I'm Wrong: LLMs Hallucinate with Certainty Despite Knowing the Answer"** - Simhi et al. (Feb 2025, updated Aug 2025)
- Introduces CHOKE (Certain Hallucinations Overriding Known Evidence) - hallucinations where the model produces wrong answers with high certainty despite having the correct knowledge internally
- Key finding: CHOKE examples are consistent across prompts, occur in different models and datasets, and are fundamentally distinct from other hallucinations
- Existing mitigation methods perform **worse** on CHOKE examples than on general hallucinations
- Proposes a probe-based mitigation method trained specifically on CHOKE examples that outperforms existing methods
- Introduces the CHOKE-Score metric to measure mitigation effectiveness specifically on these stubborn cases
- [arXiv v1](https://arxiv.org/html/2502.12964v1) | [arXiv v2](https://arxiv.org/html/2502.12964v2) | [ACL Findings EMNLP 2025](https://aclanthology.org/2025.findings-emnlp.792.pdf)

### 2. HACK: Hallucinations Along Certainty and Knowledge Axes

**"HACK: Hallucinations Along Certainty and Knowledge Axes"** (Oct 2025)
- Builds directly on CHOKE-type thinking by categorizing hallucinations along two axes: knowledge (does the model know the answer?) and certainty (is it confident?)
- The most dangerous quadrant: high certainty + has knowledge but still hallucinates
- Introduces a model-specific dataset construction process that differentiates between hallucination types
- Reveals that while some mitigation methods perform well on average, they **fail disproportionately on high-certainty cases**
- [arXiv](https://arxiv.org/abs/2510.24222)

### 3. Aletheia: Quantifying Cognitive Conviction in Reasoning Models

**"Aletheia: Quantifying Cognitive Conviction in Reasoning Models via Regularized Inverse Confusion Matrix"** (Jan 2026)
- Extends the CHOKE phenomenon framework to quantify "Cognitive Conviction" in System 2 reasoning models (DeepSeek-R1, OpenAI o1)
- Uses Tikhonov Regularization to invert the judge's confusion matrix
- Finds that reasoning models act as a "cognitive buffer" but may exhibit "Defensive OverThinking" under adversarial pressure
- Introduces the Aligned Conviction Score to verify that conviction does not compromise safety
- [arXiv](https://arxiv.org/abs/2601.01532)

### 4. Mitigating LLM Hallucination via Behaviorally Calibrated Reinforcement Learning

**Wu et al.** (Dec 2025)
- Argues hallucination is a predictable consequence of training objectives prioritizing confident guessing over epistemic honesty
- Behavioral calibration incentivizes models to abstain when not confident, aligning behavior with accuracy
- A 4B parameter model trained with this method achieves a log-scale Accuracy-to-Hallucination Ratio (0.806) exceeding GPT-5's (0.207)
- Achieves zero-shot calibration error on par with frontier models in cross-domain factual QA
- [arXiv](https://arxiv.org/abs/2512.19920)

### 5. Know When You're Wrong: Aligning Confidence with Correctness for LLM Error Detection

(Feb 2026)
- Introduces a normalized confidence score based on output anchor token probabilities for detecting errors and hallucinations
- Self-evaluation framework using Yes/No responses for open-ended generation enables direct detection of high-confidence errors
- Evaluated across seven benchmark tasks and five LLMs of varying architectures
- [arXiv](https://arxiv.org/abs/2603.06604)

### 6. Mind the Confidence Gap: Overconfidence, Calibration, and Distractor Effects in LLMs

**Chhikara et al.** (Feb 2025, published in Transactions on Machine Learning Research, Dec 2025)
- Comprehensive analysis across nine LLMs and three factual QA datasets
- Finds that incorporating distractors (inspired by cognitive psychology) achieves relative accuracy improvements up to 460% and ECE reductions up to 90%
- Large RLHF-tuned models can paradoxically suffer **increased** miscalibration on easier queries
- [arXiv](https://arxiv.org/abs/2502.11028) | [OpenReview](https://openreview.net/forum?id=lyaHnHDdZl)

### 7. MIT: A Better Method for Identifying Overconfident Large Language Models

(Mar 2026)
- Estimates epistemic uncertainty by measuring disagreement across an ensemble of similar LLMs
- Combines epistemic uncertainty with aleatoric uncertainty into a Total Uncertainty (TU) metric
- TU effectively identifies situations where an LLM is hallucinating with confidence, catching cases that standard aleatoric measures miss
- [MIT News](https://news.mit.edu/2026/better-method-identifying-overconfident-large-language-models-0319)

### 8. The Dunning-Kruger Effect in Large Language Models: An Empirical Study of Confidence Calibration

(Mar 2026)
- Demonstrates that poorly performing models display markedly higher overconfidence (analogous to Dunning-Kruger in humans)
- Striking calibration differences: some models show ECE of 0.726 with only 23.3% accuracy
- Smaller models systematically overestimate abilities; larger models tend to underestimate
- [arXiv](https://arxiv.org/abs/2603.09985) | [Nature Scientific Reports](https://www.nature.com/articles/s41598-026-39046-w)

### 9. Confidence Before Answering (CoCA): A Paradigm Shift for Efficient LLM Uncertainty Estimation

(Mar 2026)
- Proposes confidence-first estimation before generation (rather than post-hoc calibration)
- CoCA uses GRPO reinforcement learning to jointly optimize confidence calibration and answer accuracy
- Enables the model to decide "Given my current capabilities, how likely am I to answer correctly?" before committing to an answer
- [arXiv](https://arxiv.org/abs/2603.05881)

### 10. TruthRL: Incentivizing Truthful LLMs via Reinforcement Learning

**Wei et al., Facebook Research** (2025)
- RL framework using a ternary reward: correct answers, hallucinations, and abstentions
- Directly optimizes for truthfulness by rewarding abstention over confident wrong answers
- Reduces hallucinations by 28.9% and improves truthfulness by 21.1% compared to vanilla RL
- [arXiv](https://arxiv.org/abs/2509.25760) | [GitHub](https://github.com/facebookresearch/TruthRL)

### 11. BaseCal: Unsupervised Confidence Calibration via Base Model Signals

**Tan et al.** (Jan 2026)
- Exploits the fact that base LLMs are well-calibrated while post-trained versions become overconfident
- Projects post-trained model hidden states back to base model space to derive calibrated confidence
- Reduces ECE by 42.90% on average across five datasets and three LLM families
- [arXiv](https://arxiv.org/abs/2601.03042) | [OpenReview](https://openreview.net/forum?id=QwGdjqq2pp)

### 12. How LLMs Detect and Correct Their Own Errors: The Role of Internal Confidence Signals

(Apr 2026)
- Discovers that LLMs implement a "second-order confidence architecture" - an evaluative process partially independent of generation that can disagree with the committed response
- Internal confidence signals predict which errors the model can correct
- LLMs cache evaluative representations at the post-answer newline token that drive verbal confidence and dissociate from log-probabilities
- [arXiv](https://arxiv.org/html/2604.22271v1)

### 13. CMU Study: AI Chatbots Remain Overconfident Even When Wrong

**Cash & Oppenheimer** (Jul 2025, published in Memory & Cognition)
- Multi-year study showing LLMs (GPT, Gemini, Claude) systematically overestimate confidence
- Unlike humans who adjust downward after feedback, LLMs become **more** overconfident after performing poorly
- Gemini predicted 10.03 correct answers, got fewer than 1/20 right, then retrospectively estimated 14.40 correct
- [CMU News](https://www.cmu.edu/dietrich/news/news-stories/2025/trent-cash-ai-overconfidence)

---

## Summary: CHOKE Follow-up Work

Regarding the Simhi et al. CHOKE framework specifically: Two papers directly build on it:
1. **HACK** (Oct 2025) extends the certainty/knowledge categorization into a full two-axis taxonomy
2. **Aletheia** (Jan 2026) extends CHOKE to reasoning models with a formal quantification framework

The CHOKE paper itself was published at EMNLP 2025 Findings, indicating peer-reviewed acceptance and community recognition. The core insight -- that high-certainty hallucinations are fundamentally different from uncertain hallucinations and require different detection/mitigation strategies -- has become an influential framing in the field.

Sources:
- [Trust Me, I'm Wrong (CHOKE) v2](https://arxiv.org/html/2502.12964v2)
- [HACK: Hallucinations Along Certainty and Knowledge Axes](https://arxiv.org/abs/2510.24222)
- [Aletheia: Quantifying Cognitive Conviction](https://arxiv.org/abs/2601.01532)
- [Behaviorally Calibrated RL](https://arxiv.org/abs/2512.19920)
- [Know When You're Wrong](https://arxiv.org/abs/2603.06604)
- [Mind the Confidence Gap](https://arxiv.org/abs/2502.11028)
- [MIT Overconfident LLM Detection](https://news.mit.edu/2026/better-method-identifying-overconfident-large-language-models-0319)
- [Dunning-Kruger Effect in LLMs](https://arxiv.org/abs/2603.09985)
- [Confidence Before Answering (CoCA)](https://arxiv.org/abs/2603.05881)
- [TruthRL](https://arxiv.org/abs/2509.25760)
- [BaseCal](https://arxiv.org/abs/2601.03042)
- [Internal Confidence Signals](https://arxiv.org/html/2604.22271v1)
- [CMU Overconfidence Study](https://www.cmu.edu/dietrich/news/news-stories/2025/trent-cash-ai-overconfidence)

agentId: a5af925e0cdbf6897 (use SendMessage with to: 'a5af925e0cdbf6897' to continue this agent)
&lt;usage>total_tokens: 34574
tool_uses: 23
duration_ms: 164016&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7bfd6b61-0375-4b0b-92b6-23088458e08b",
  "isSidechain": false,
  "promptId": "ab5656e8-b9e4-40d4-bf76-8cf45c241dcf",
  "type": "user",
  "uuid": "b0323d69-7d0e-4a20-aadd-d50d40dbb662",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Search for recent papers (2025-2026) that specifically focus on detecting or mitigating HIGH-CONFIDENCE hallucinations in LLMs - cases where the model is very confident but wrong. This is different from general hallucination detection. Search for:\n1. \"high confidence hallucination detection LLM 2025 2026\"\n2. \"confident wrong answer LLM detection\"\n3. \"stubborn hallucination\" detection\n4. \"overconfident LLM hallucination mitigation\"\n5. \"calibration high confidence error\"\n\nAlso search for \"CHOKE hallucination\" to see if anyone else has built on the Simhi et al. CHOKE framework.\n\nReport all papers found that specifically target the high-confidence/stubborn hallucination problem (not general hallucination detection).",
    "agentId": "a5af925e0cdbf6897",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Based on my extensive research, here is a comprehensive report of papers specifically targeting the high-confidence/stubborn hallucination problem in LLMs (2025-2026):\n\n---\n\n## Papers Specifically Targeting High-Confidence/Stubborn Hallucinations\n\n### 1. CHOKE Framework - The Foundational Paper\n\n**\"Trust Me, I'm Wrong: LLMs Hallucinate with Certainty Despite Knowing the Answer\"** - Simhi et al. (Feb 2025, updated Aug 2025)\n- Introduces CHOKE (Certain Hallucinations Overriding Known Evidence) - hallucinations where the model produces wrong answers with high certainty despite having the correct knowledge internally\n- Key finding: CHOKE examples are consistent across prompts, occur in different models and datasets, and are fundamentally distinct from other hallucinations\n- Existing mitigation methods perform **worse** on CHOKE examples than on general hallucinations\n- Proposes a probe-based mitigation method trained specifically on CHOKE examples that outperforms existing methods\n- Introduces the CHOKE-Score metric to measure mitigation effectiveness specifically on these stubborn cases\n- [arXiv v1](https://arxiv.org/html/2502.12964v1) | [arXiv v2](https://arxiv.org/html/2502.12964v2) | [ACL Findings EMNLP 2025](https://aclanthology.org/2025.findings-emnlp.792.pdf)\n\n### 2. HACK: Hallucinations Along Certainty and Knowledge Axes\n\n**\"HACK: Hallucinations Along Certainty and Knowledge Axes\"** (Oct 2025)\n- Builds directly on CHOKE-type thinking by categorizing hallucinations along two axes: knowledge (does the model know the answer?) and certainty (is it confident?)\n- The most dangerous quadrant: high certainty + has knowledge but still hallucinates\n- Introduces a model-specific dataset construction process that differentiates between hallucination types\n- Reveals that while some mitigation methods perform well on average, they **fail disproportionately on high-certainty cases**\n- [arXiv](https://arxiv.org/abs/2510.24222)\n\n### 3. Aletheia: Quantifying Cognitive Conviction in Reasoning Models\n\n**\"Aletheia: Quantifying Cognitive Conviction in Reasoning Models via Regularized Inverse Confusion Matrix\"** (Jan 2026)\n- Extends the CHOKE phenomenon framework to quantify \"Cognitive Conviction\" in System 2 reasoning models (DeepSeek-R1, OpenAI o1)\n- Uses Tikhonov Regularization to invert the judge's confusion matrix\n- Finds that reasoning models act as a \"cognitive buffer\" but may exhibit \"Defensive OverThinking\" under adversarial pressure\n- Introduces the Aligned Conviction Score to verify that conviction does not compromise safety\n- [arXiv](https://arxiv.org/abs/2601.01532)\n\n### 4. Mitigating LLM Hallucination via Behaviorally Calibrated Reinforcement Learning\n\n**Wu et al.** (Dec 2025)\n- Argues hallucination is a predictable consequence of training objectives prioritizing confident guessing over epistemic honesty\n- Behavioral calibration incentivizes models to abstain when not confident, aligning behavior with accuracy\n- A 4B parameter model trained with this method achieves a log-scale Accuracy-to-Hallucination Ratio (0.806) exceeding GPT-5's (0.207)\n- Achieves zero-shot calibration error on par with frontier models in cross-domain factual QA\n- [arXiv](https://arxiv.org/abs/2512.19920)\n\n### 5. Know When You're Wrong: Aligning Confidence with Correctness for LLM Error Detection\n\n(Feb 2026)\n- Introduces a normalized confidence score based on output anchor token probabilities for detecting errors and hallucinations\n- Self-evaluation framework using Yes/No responses for open-ended generation enables direct detection of high-confidence errors\n- Evaluated across seven benchmark tasks and five LLMs of varying architectures\n- [arXiv](https://arxiv.org/abs/2603.06604)\n\n### 6. Mind the Confidence Gap: Overconfidence, Calibration, and Distractor Effects in LLMs\n\n**Chhikara et al.** (Feb 2025, published in Transactions on Machine Learning Research, Dec 2025)\n- Comprehensive analysis across nine LLMs and three factual QA datasets\n- Finds that incorporating distractors (inspired by cognitive psychology) achieves relative accuracy improvements up to 460% and ECE reductions up to 90%\n- Large RLHF-tuned models can paradoxically suffer **increased** miscalibration on easier queries\n- [arXiv](https://arxiv.org/abs/2502.11028) | [OpenReview](https://openreview.net/forum?id=lyaHnHDdZl)\n\n### 7. MIT: A Better Method for Identifying Overconfident Large Language Models\n\n(Mar 2026)\n- Estimates epistemic uncertainty by measuring disagreement across an ensemble of similar LLMs\n- Combines epistemic uncertainty with aleatoric uncertainty into a Total Uncertainty (TU) metric\n- TU effectively identifies situations where an LLM is hallucinating with confidence, catching cases that standard aleatoric measures miss\n- [MIT News](https://news.mit.edu/2026/better-method-identifying-overconfident-large-language-models-0319)\n\n### 8. The Dunning-Kruger Effect in Large Language Models: An Empirical Study of Confidence Calibration\n\n(Mar 2026)\n- Demonstrates that poorly performing models display markedly higher overconfidence (analogous to Dunning-Kruger in humans)\n- Striking calibration differences: some models show ECE of 0.726 with only 23.3% accuracy\n- Smaller models systematically overestimate abilities; larger models tend to underestimate\n- [arXiv](https://arxiv.org/abs/2603.09985) | [Nature Scientific Reports](https://www.nature.com/articles/s41598-026-39046-w)\n\n### 9. Confidence Before Answering (CoCA): A Paradigm Shift for Efficient LLM Uncertainty Estimation\n\n(Mar 2026)\n- Proposes confidence-first estimation before generation (rather than post-hoc calibration)\n- CoCA uses GRPO reinforcement learning to jointly optimize confidence calibration and answer accuracy\n- Enables the model to decide \"Given my current capabilities, how likely am I to answer correctly?\" before committing to an answer\n- [arXiv](https://arxiv.org/abs/2603.05881)\n\n### 10. TruthRL: Incentivizing Truthful LLMs via Reinforcement Learning\n\n**Wei et al., Facebook Research** (2025)\n- RL framework using a ternary reward: correct answers, hallucinations, and abstentions\n- Directly optimizes for truthfulness by rewarding abstention over confident wrong answers\n- Reduces hallucinations by 28.9% and improves truthfulness by 21.1% compared to vanilla RL\n- [arXiv](https://arxiv.org/abs/2509.25760) | [GitHub](https://github.com/facebookresearch/TruthRL)\n\n### 11. BaseCal: Unsupervised Confidence Calibration via Base Model Signals\n\n**Tan et al.** (Jan 2026)\n- Exploits the fact that base LLMs are well-calibrated while post-trained versions become overconfident\n- Projects post-trained model hidden states back to base model space to derive calibrated confidence\n- Reduces ECE by 42.90% on average across five datasets and three LLM families\n- [arXiv](https://arxiv.org/abs/2601.03042) | [OpenReview](https://openreview.net/forum?id=QwGdjqq2pp)\n\n### 12. How LLMs Detect and Correct Their Own Errors: The Role of Internal Confidence Signals\n\n(Apr 2026)\n- Discovers that LLMs implement a \"second-order confidence architecture\" - an evaluative process partially independent of generation that can disagree with the committed response\n- Internal confidence signals predict which errors the model can correct\n- LLMs cache evaluative representations at the post-answer newline token that drive verbal confidence and dissociate from log-probabilities\n- [arXiv](https://arxiv.org/html/2604.22271v1)\n\n### 13. CMU Study: AI Chatbots Remain Overconfident Even When Wrong\n\n**Cash & Oppenheimer** (Jul 2025, published in Memory & Cognition)\n- Multi-year study showing LLMs (GPT, Gemini, Claude) systematically overestimate confidence\n- Unlike humans who adjust downward after feedback, LLMs become **more** overconfident after performing poorly\n- Gemini predicted 10.03 correct answers, got fewer than 1/20 right, then retrospectively estimated 14.40 correct\n- [CMU News](https://www.cmu.edu/dietrich/news/news-stories/2025/trent-cash-ai-overconfidence)\n\n---\n\n## Summary: CHOKE Follow-up Work\n\nRegarding the Simhi et al. CHOKE framework specifically: Two papers directly build on it:\n1. **HACK** (Oct 2025) extends the certainty/knowledge categorization into a full two-axis taxonomy\n2. **Aletheia** (Jan 2026) extends CHOKE to reasoning models with a formal quantification framework\n\nThe CHOKE paper itself was published at EMNLP 2025 Findings, indicating peer-reviewed acceptance and community recognition. The core insight -- that high-certainty hallucinations are fundamentally different from uncertain hallucinations and require different detection/mitigation strategies -- has become an influential framing in the field.\n\nSources:\n- [Trust Me, I'm Wrong (CHOKE) v2](https://arxiv.org/html/2502.12964v2)\n- [HACK: Hallucinations Along Certainty and Knowledge Axes](https://arxiv.org/abs/2510.24222)\n- [Aletheia: Quantifying Cognitive Conviction](https://arxiv.org/abs/2601.01532)\n- [Behaviorally Calibrated RL](https://arxiv.org/abs/2512.19920)\n- [Know When You're Wrong](https://arxiv.org/abs/2603.06604)\n- [Mind the Confidence Gap](https://arxiv.org/abs/2502.11028)\n- [MIT Overconfident LLM Detection](https://news.mit.edu/2026/better-method-identifying-overconfident-large-language-models-0319)\n- [Dunning-Kruger Effect in LLMs](https://arxiv.org/abs/2603.09985)\n- [Confidence Before Answering (CoCA)](https://arxiv.org/abs/2603.05881)\n- [TruthRL](https://arxiv.org/abs/2509.25760)\n- [BaseCal](https://arxiv.org/abs/2601.03042)\n- [Internal Confidence Signals](https://arxiv.org/html/2604.22271v1)\n- [CMU Overconfidence Study](https://www.cmu.edu/dietrich/news/news-stories/2025/trent-cash-ai-overconfidence)"
      }
    ],
    "totalDurationMs": 164016,
    "totalTokens": 34574,
    "totalToolUseCount": 23,
    "usage": {
      "input_tokens": 952,
      "cache_creation_input_tokens": 1237,
      "cache_read_input_tokens": 29593,
      "output_tokens": 2792,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1237
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 952,
          "output_tokens": 2792,
          "cache_read_input_tokens": 29593,
          "cache_creation_input_tokens": 1237,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1237,
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
      "otherToolCount": 23
    }
  },
  "sourceToolAssistantUUID": "7bfd6b61-0375-4b0b-92b6-23088458e08b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1c70a808-ac42-40e9-b451-f24d9f6e7546",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 35 · 2026-05-16T09:52:05.014Z_

```json
{
  "parentUuid": "b0323d69-7d0e-4a20-aadd-d50d40dbb662",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "7116aaa5-fa9c-475c-82e6-af1d4fe1bf8b",
  "timestamp": "2026-05-16T09:52:05.014Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1c70a808-ac42-40e9-b451-f24d9f6e7546",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 36_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-16 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "7116aaa5-fa9c-475c-82e6-af1d4fe1bf8b",
  "sessionId": "1c70a808-ac42-40e9-b451-f24d9f6e7546"
}
```

---

### Runtime record

_source line 37_

```json
{
  "type": "ai-title",
  "aiTitle": "Verify LSP method against Liu et al. and assess CHOKE subset feasibility",
  "sessionId": "1c70a808-ac42-40e9-b451-f24d9f6e7546"
}
```

---

### Assistant

_source line 38 · 2026-05-16T09:53:28.770Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have comprehensive information to evaluate this idea. Let me synthesize my findings:

## Key Findings:

### Paper Verification:
1. **EPGS (arxiv 2605.00939)** - CONFIRMED. Exists, accepted at ICML 2026. Proposes that stubborn hallucinations sit in sharp minima, uses embedding perturbation + gradient magnitude measurement.
2. **Liu et al. (arxiv 2502.03799)** - CONFIRMED. Exists, likely accepted at ICLR 2026. Injects uniform noise into upper-third MLP activations, measures answer entropy/semantic entropy. 

The remaining papers all check out as well: CHOKE uses probe-based detection with oversampled training data, SHINE perturbs entity embeddings to measure output distribution shifts, and "Shaking to Reveal" leverages trained encoders on perturbation sensitivity—all showing AUROC improvements in the 1-6 percentage point range.

I've confirmed the venue details and model specifications, and the KL divergence approximation they're using is mathematically sound, though it's a standard result from information geometry rather than a novel theoretical contribution. Now I'm evaluating whether the overall approach constitutes a genuine novelty contribution.

LSP's core idea is injecting Gaussian noise into intermediate residual layers and using KL divergence of output distributions as a sharpness proxy to filter hallucinations in a two-stage pipeline. Looking at the landscape, there's significant overlap with existing work—SHINE uses nearly identical measurement mechanics but perturbs input embeddings instead, EPGS targets the same sharpness-based motivation for hallucinations but requires backpropagation, and Liu et al. appears to work at similar intermediate activation points. The main differentiator seems to be avoiding backpropagation while targeting CHOKE hallucinations specifically, but I need to assess whether that's enough to constitute a novel contribution. LSP targets CHOKE with perturbation-based detection instead of probes. The core novelty is combining intermediate residual perturbations with logit-level KL measurement in a gradient-free approach, which blends Liu et al.'s perturbation strategy, SHINE's measurement method, EPGS's theoretical motivation, and Simhi et al.'s problem focus—it's an incremental but well-justified combination. Now looking at feasibility: the timeline is extremely tight with only 9 days and the auto_research estimate suggests 7-9 days on 4× H100 GPUs, so I need to assess whether CHOKE subset construction is even feasible in that window.

The compute budget is a real constraint—auto_research asks for 350 hours which violates the hard limit of 200 H100-hours, though manual and human-in-loop modes stay within budget. This means I'd need to either optimize the approach or shift away from the auto_research configuration entirely.

The main cost drivers are subset construction, noise calibration grid search, and evaluation runs. A researcher could reduce this by using fewer models, a sparser noise grid, and focusing on just TriviaQA and NQ rather than exhaustive exploration. The manual and HIL modes at 150-180 hours seem reasonable for targeted choices instead of full grid search.

Now I'm thinking through the technical validation—specifically whether the claim about KL sensitivity in sharp minima actually holds for CHOKE cases, since that's a key assumption underlying the approach.

The pre-filter using token probability and linear probes adds complexity but makes sense for efficiency, and calibrating noise on held-out CHOKE examples is sound though it does introduce a dataset-dependent hyperparameter. The main weaknesses are that SHINE already measures KL divergence after perturbation, so the novelty is really just the location of where perturbation happens. The theoretical contribution about KL and Hessian trace is established math rather than new theory, and whether intermediate-layer perturbation actually outperforms input-layer or upper-MLP approaches is purely empirical and might not show strong advantages.

The CHOKE subset construction borrows from Simhi et al., so that's not novel either, and the space is incredibly crowded with EPGS, SHINE, Liu et al., NGS, and other perturbation-based methods all doing similar work. The problem itself is important and timely, and if LSP performs well on CHOKE where others fail, that would matter, but the contribution feels incremental—just recombining known techniques in a slightly different configuration. The theoretical angle around sharpness is interesting but EPGS already established that connection, so the novelty scores around 3/5 since it's mixing elements from recent papers without substantial new insights.

On feasibility, the auto_research mode needs 350 hours but the budget is only 200 hours, and the 9-day timeline is essentially impossible for producing quality work even with automation. The CHOKE subset construction itself is a major upfront cost, and the core implementation faces serious time constraints.

The core hypothesis—that KL sensitivity is high for CHOKE while answer entropy is low—remains unvalidated empirically, though the models and technical approach are straightforward. The proposal is clearly written with good differentiation from prior work and a logical two-stage pipeline, plus the insight about why answer entropy fails on CHOKE is well-articulated. However, the impact is limited since even if successful, the method only addresses a narrow failure mode affecting 0.3-2.1% of all hallucinations (or 16-43% of high-certainty ones), and it would be one of many perturbation-based methods in a crowded field rather than a breakthrough contribution.

The score averages to 3.25, falling short of the 4.0 threshold. There are three critical blockers: the compute budget of 350 hours exceeds the hard constraint of 200 H100-hours, even the more efficient mode at 180 hours leaves little margin; the 9-day timeline to EMNLP is unrealistic for producing quality work; and the novelty is extremely narrow—essentially just shifting perturbations from input embeddings to intermediate layers, which is a single variable change from SHINE.

The core empirical claim that intermediate-layer perturbations will produce distinct KL signals for CHOKE cases lacks pilot validation or theoretical grounding. While EPGS shows high gradient magnitudes, that doesn't guarantee KL sensitivity in a forward-only setting. Additionally, CHOKE represents only 0.3-2.1% of all hallucinations, so even if the method works perfectly for this subset, the practical impact is limited unless it also improves general detection. The competitive landscape is crowded, which compounds these concerns.

The theoretical foundation also isn't novel—the connection between KL divergence and Hessian traces is established information geometry from prior work. Despite these weaknesses, I think this warrants revision rather than rejection because the core problem is important, the insight about why answer entropy fails on CHOKE is sound, and the technical approach is solid.

For revision, I need to cut compute to stay under 200 hours, find stronger differentiation from SHINE beyond just using a different perturbation layer, and provide actual evidence for why intermediate-layer perturbation specifically helps with CHOKE detection. I should also be realistic about the timeline—this almost certainly won't make the May 25 deadline. The contribution might be better positioned as an empirical study showing that gradient-free sharpness-aware perturbation signals work for practical CHOKE detection, rather than claiming methodological novelty.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7116aaa5-fa9c-475c-82e6-af1d4fe1bf8b",
  "isSidechain": false,
  "requestId": "req_011Cb63QUPuefriQgFnNnzDE",
  "type": "assistant",
  "uuid": "fb779acc-fa0c-4e71-81c0-7b34965f7056",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1c70a808-ac42-40e9-b451-f24d9f6e7546",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Mx5hUnFAsc2QRaVCfgL7wV",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7337,
      "cache_read_input_tokens": 36427,
      "output_tokens": 5019,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7337,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 5019,
          "cache_read_input_tokens": 36427,
          "cache_creation_input_tokens": 7337,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7337
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

_source line 39 · 2026-05-16T09:54:02.827Z_

Now I have comprehensive findings to render my verdict. Let me synthesize the evidence.

**Key verification results:**
- All cited papers confirmed to exist with correct claims
- EMNLP 2026 ARR deadline May 25 confirmed
- Both models (Qwen3.6-27B, DeepSeek-V4-Flash) confirmed available
- KL ≈ Hessian trace theory is valid but well-known (not novel)
- SHINE already measures KL divergence after perturbation (at input level)
- Extremely crowded landscape: 6+ perturbation-based methods in past 12 months

```json
{
  "verdict": "revise",
  "scores": {
    "novelty": {"score": 3, "rationale": "The core differentiation from SHINE is 'perturb at intermediate layers instead of input embeddings'—essentially a single-variable ablation. The KL-as-sharpness framing recycles well-known information geometry (Camuto et al., NeurIPS 2020). The CHOKE-specific targeting is motivated but Simhi et al. already proposed probe-based CHOKE detection. In a landscape with 6+ perturbation-based methods (EPGS, SHINE, Liu et al., NGS, SSP, Attention Divergence), the combination is valid but incremental."},
    "feasibility": {"score": 3, "rationale": "Auto mode at 350h EXCEEDS the user's 200h hard constraint. The 9-day timeline to May 25 is extremely tight—the proposal itself hedges with an ACL 2027 fallback. The core hypothesis (logit KL is high for CHOKE while answer entropy is low) is unvalidated; EPGS showed gradient-magnitude spikes but this doesn't guarantee forward-only KL sensitivity behaves similarly."},
    "clarity": {"score": 4, "rationale": "Well-structured with clear positioning against 6+ related works. The two-stage pipeline is logical, the failure mode analysis of Liu et al. is insightful, and the theoretical connection to Hessian trace is clearly articulated even if not novel."},
    "impact": {"score": 3, "rationale": "CHOKE represents 0.3-2.1% of all hallucinations (Simhi et al.)—or 16-43% of high-certainty ones. A detection method for this narrow subset has limited deployment impact unless it also generalizes. The crowded landscape (EPGS, SHINE, SSP, NGS all published 2024-2026) means this is one of many perturbation papers rather than a paradigm shift."}
  },
  "issues": [
    "COMPUTE BUDGET VIOLATION: Auto_research estimate of 350h H100 exceeds the user's hard constraint of ≤200 H100-hours. The 50h CHOKE subset construction plus noise calibration grid search drives this over budget.",
    "EXTREMELY TIGHT TIMELINE: 9 days (May 16→25) is infeasible for a quality EMNLP submission. The proposal acknowledges this with a fallback to ACL 2027, effectively conceding the primary target is unrealistic.",
    "NARROW NOVELTY VS SHINE: SHINE (arxiv 2411.09689) already does 'perturb embeddings → measure output KL divergence' without training. LSP's differentiation reduces to perturbing at intermediate layers instead of input—a layer-choice ablation, not a fundamentally new method. A reviewer will ask: 'Why not just run SHINE at intermediate layers?'",
    "THEORETICAL CONTRIBUTION OVERSTATED: The KL ≈ (σ²/2)·Tr(H) relationship is standard second-order Taylor expansion / information geometry (Camuto et al. NeurIPS 2020, Fisher-SAM ICML 2022, Noise Stability Optimization 2023). Framing this as a 'key contribution' will be challenged by reviewers familiar with sharpness-aware minimization literature.",
    "UNVALIDATED CORE HYPOTHESIS: No pilot data or formal proof that residual-stream perturbation produces high logit-KL specifically for CHOKE while producing low logit-KL for correct high-confidence answers. EPGS's gradient-magnitude result does not directly transfer to forward-only KL measurement—the sharpness landscape may look different when measured via KL vs. gradient norms.",
    "CHOKE SUBSET PREVALENCE IS LOW: At 0.3-2.1% of all hallucinations, a CHOKE-only detector has limited standalone value unless utility on general hallucinations is also demonstrated. The paper should report general AUROC alongside CHOKE-Score.",
    "MISSING COMPARISON: HACK (arxiv 2510.24222, Oct 2025) and Aletheia (arxiv 2601.01532, Jan 2026) both build on CHOKE and propose detection/mitigation. These should be cited and compared."
  ],
  "feedback": "The revision addressed Round 1 issues well (venue, citations, positioning), but fundamental problems remain:\n\n1. **Compute**: Cut the grid search. Fix σ calibration to 2-3 values per layer based on EPGS's noise schedule rather than exhaustive search. Target ≤180h total by limiting to 2 models × 2 datasets × 3 noise scales × 3 layers = 36 configurations instead of a full grid.\n\n2. **Strengthen novelty beyond SHINE**: The paper MUST include a direct ablation: SHINE-style input perturbation → KL vs. LSP-style intermediate perturbation → KL, on the SAME CHOKE subset. The contribution is only valid if intermediate perturbation is empirically superior for CHOKE detection. Provide a theoretical argument: intermediate layers encode factual recall (cite knowledge localization literature: Meng et al. ROME, Geva et al.); perturbing at the locus of factual computation should produce stronger sharpness signals than perturbing distal input embeddings.\n\n3. **Reframe theory**: Don't claim the KL-Hessian connection as a contribution. Instead, frame it as *motivation*: 'Following established results connecting noise-injection to Hessian trace estimation [cite Camuto 2020, CR-SAM 2024], we propose using logit KL as a practical, forward-only sharpness proxy specifically for detecting CHOKE hallucinations.' The contribution is empirical, not theoretical.\n\n4. **Broaden evaluation**: Report both CHOKE-Score AND general AUROC. If LSP also helps on non-CHOKE hallucinations (even modestly), the impact argument is much stronger.\n\n5. **Timeline honesty**: Either commit to May 25 with a drastically scoped version (1 model, 2 benchmarks, 3 baselines) or acknowledge ACL 2027 as the realistic target. A half-finished paper at EMNLP is worse than a complete one at ACL.\n\n6. **Cite HACK and Aletheia**: These are direct follow-ups to CHOKE and must be acknowledged in the landscape section.",
  "reason": "Incremental combination of known techniques (SHINE's KL measurement + EPGS's sharpness motivation + Liu et al.'s perturbation location) with compute budget violation and infeasible timeline—needs tighter scoping and stronger empirical differentiation."
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fb779acc-fa0c-4e71-81c0-7b34965f7056",
  "isSidechain": false,
  "requestId": "req_011Cb63QUPuefriQgFnNnzDE",
  "type": "assistant",
  "uuid": "a4a9d6bd-e196-4700-aa32-e3128fc5376d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1c70a808-ac42-40e9-b451-f24d9f6e7546",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Mx5hUnFAsc2QRaVCfgL7wV",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7337,
      "cache_read_input_tokens": 36427,
      "output_tokens": 5019,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7337,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 5019,
          "cache_read_input_tokens": 36427,
          "cache_creation_input_tokens": 7337,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7337
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
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-16 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "a4a9d6bd-e196-4700-aa32-e3128fc5376d",
  "sessionId": "1c70a808-ac42-40e9-b451-f24d9f6e7546"
}
```

---

### Runtime record

_source line 41_

```json
{
  "type": "ai-title",
  "aiTitle": "Verify LSP method against Liu et al. and assess CHOKE subset feasibility",
  "sessionId": "1c70a808-ac42-40e9-b451-f24d9f6e7546"
}
```

---

### Runtime record

_source line 42_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-16 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "a4a9d6bd-e196-4700-aa32-e3128fc5376d",
  "sessionId": "1c70a808-ac42-40e9-b451-f24d9f6e7546"
}
```

---

### Runtime record

_source line 43_

```json
{
  "type": "ai-title",
  "aiTitle": "Verify LSP method against Liu et al. and assess CHOKE subset feasibility",
  "sessionId": "1c70a808-ac42-40e9-b451-f24d9f6e7546"
}
```

---
