# Research conversation: You are a strict ML research reviewer conducting adversarial review. **Today's date: 2026-05-16 (UTC).** Your job: indep

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 30
- **Recorded user turns:** 1
- **Tool calls:** 5
- **Original source:** `logs/chats/exported-trajectories/account-1/3851818f-b8a5-4456-92d9-6671bfb78776.jsonl`
- **Structured JSON:** [`c9908842ca8b6eb06394.json`](../../sessions/c9/c9908842ca8b6eb06394.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-16T09:00:01.741Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-16T09:00:01.741Z",
  "sessionId": "3851818f-b8a5-4456-92d9-6671bfb78776",
  "content": "You are a strict ML research reviewer conducting adversarial review.\n\n**Today's date: 2026-05-16 (UTC).**\n\nYour job: independently verify this idea's claims via WebSearch, then issue a verdict.\n\n## User requirements\nThe user asked for: **Target: EMNLP 2026, ARR submission deadline 2026-05-25 (11 days from today 2026-05-14). Track: Generation.\n\nDirection: Faithfulness, hallucination reduction, and calibrated uncertainty in LLM generation. In-scope: hallucination detection via internal representations (linear probes on hidden states, attention patterns, logit signatures), decoding-time interventions that suppress hallucinated content, calibration of verbalized confidence so model uncertainty matches actual accuracy, faithful chain-of-thought (CoT reflects actual computation, not post-hoc rationalization), attribution-aware generation with provenance to source spans, fine-grained atomic-claim verification during or after generation. Cross-cutting with Interpretability and Language Modeling tracks — the contribution must improve GENERATION quality, not just analyze model internals.\n\nContribution type: METHOD ONLY. Must propose a concrete detection algorithm, decoding-time intervention, training recipe, or calibration method. Pure analysis (\"we found models hallucinate when X\") is out of scope. Method + faithfulness analysis OK if analysis validates the method.\n\nHARD CONSTRAINTS:\n1. Compute: ≤200 H100-hours total. Hallucination work is mostly inference + lightweight probe training — budget for forward passes across many prompts + small classifier heads (linear probes, MLPs on hidden states). Avoid full SFT of large models.\n2. Time: ≤11 days. Use existing open models (Llama-3, Qwen3, DeepSeek-R1 distills, Mistral) + existing hallucination/faithfulness benchmarks. Build on interpretability toolkits (TransformerLens, nnsight) for hidden-state extraction if needed.\n3. Eval: TruthfulQA, HaluEval, FaithBench, FActScore, FELM, SimpleQA, LongFact for hallucination detection/reduction; ECE / Brier score / selective accuracy for calibration; faithfulness metrics on CoT (causal interventions, unlearning probes); attribution precision/recall on ELI5-attributed, ExpertQA. Must report both hallucination reduction AND utility preservation (MT-Bench, MMLU) — don't kill helpfulness while suppressing hallucinations.\n\nWhy this matters now: EMNLP 2025 awarded TWO Outstanding Papers in this space (\"Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations\", \"Measuring Chain of Thought Faithfulness by Unlearning Reasoning Steps\"), and the second annual Uncertainty Quantification workshop was held alongside. Hallucination is THE blocking issue for LLM deployment in high-stakes domains, and methods that exploit internal representations (rather than external retrieval or RLHF) are an emerging frontier. Look for: representation-level hallucination detectors that generalize across model families, decoding-time refusal/abstention mechanisms triggered by uncertainty features, calibration methods that work without holdout data, faithful-by-construction reasoning architectures (vs. post-hoc rationalization), atomic-fact-level verification integrated into generation. Avoid: yet another hallucination benchmark, RLHF-from-scratch calibration training, prompt-only \"say I don't know\" tricks, retrieval-augmented faithfulness (covered by Seed 2). Distinguish from existing Interpretability seed: that seed focuses on interpretability METHODS (circuits, probes as tools); this seed uses interpretability TECHNIQUES as means to improve generation faithfulness — output-quality contribution must be primary.**\nYou MUST evaluate whether this idea actually meets the user's requirements. If the user asked for a top venue, assess whether the idea is truly top-venue quality. If the user asked for low resource cost, verify the resource estimate is realistic and low. An idea that doesn't match what the user asked for should be \"revise\" or \"fail\".\n\n## 核心要求：非常仔细地调研，非常仔细地思考\n\n你是一个严格的审稿人。不要轻信 Generator 的任何 claim——你必须独立验证，深入思考每个维度。\n\n### 调研要求\n\n1. **独立 SOTA 验证**：自己搜索当前 SOTA，不要只检查 Generator 的引用。\n   每个验证维度建议用 2-3 种不同的搜索查询。\n\n2. **可行性深度检查**：\n   - 搜索类似实验的实际成本/周期\n   - 检查 claimed baselines 是否可复现\n   - 验证所需的 datasets/models 是否真的可以获取\n\n3. **新颖性压力测试**：专门搜索 Generator 可能遗漏的工作：\n   - 尝试不同的关键词组合\n   - 同时检查 arXiv 和 conference proceedings\n   - 寻找相邻领域的并行/concurrent 工作\n\n4. **深入阅读**：不要只依赖搜索摘要。用 WebFetch 实际阅读相关论文的 abstract 和关键章节，形成你自己的判断。\n\n### 思考要求\n\n5. **独立判断**：\n   - 不要因为 Generator 说得有道理就轻易 pass——真正好的 idea 经得起严格审查\n   - 思考这个 idea 在实际执行中会遇到什么困难\n   - 考虑这个 idea 对领域的真实贡献（不是自说自话的贡献）\n\n6. **评分诚实**：\n   - 不要给\"看起来还行\"的 idea 高分——4 分意味着\"确实很好\"，5 分意味着\"令人兴奋\"\n   - Agent 评分经常虚高，你的职责就是纠正这种偏差\n\n充分利用你的工具——做真正的调研，不是走过场。\n\n\n## 论文搜索策略\n\n你的搜索质量直接决定了 idea 的质量。不要敷衍搜索——每一次搜索都要有明确的目的。\n\n### 搜索源（推荐每个维度使用 2 个不同来源）\n\n1. **arXiv 预印本**（最新工作）:\n   - `site:arxiv.org {topic} {year}` — 按主题搜索最新论文\n   - `site:arxiv.org {method_name}` — 按具体方法名搜索\n   - `arxiv {topic} {month} {year}` — 精确到月份，找最近 3 个月的工作\n\n2. **Google Scholar**（引用关系 + 综合覆盖）:\n   - `{topic} {year} site:scholar.google.com` — 或直接搜索让 Google 自动包含 Scholar 结果\n   - `\"{exact paper title}\"` — 验证论文是否真实存在\n   - `\"{author name}\" {topic} {year}` — 按活跃作者追踪（找到领域大牛后追踪其最新工作）\n\n3. **Papers With Code**（SOTA 排行 + 代码可用性）:\n   - `site:paperswithcode.com {task_name}` — 查看任务的 SOTA 排行榜\n   - `site:paperswithcode.com {method_name}` — 查看方法是否已被实现\n   - `paperswithcode {dataset} benchmark` — 查看特定 dataset 上的竞争格局\n\n4. **OpenReview**（会议审稿 + 同行评价）:\n   - `site:openreview.net {topic} {year}` — 搜索会议提交的论文\n   - 用 WebFetch 阅读 OpenReview 上的 reviewer comments — 了解领域专家的真实评价\n\n5. **Semantic Scholar**（语义搜索 + 引用图谱）:\n   - `semantic scholar {topic} survey {year}` — 找综述论文\n   - `semanticscholar.org {paper_title}` — 查看 cited by（谁引用了这篇）和 references（它引用了谁）\n\n6. **GitHub**（实现验证）:\n   - `site:github.com {method_name} {task}` — 验证开源实现是否存在\n   - `site:huggingface.co {model_name}` — 验证模型/数据集是否可获取\n\n### 搜索维度（多角度交叉，不要只按 topic 搜）\n\n对每个 idea/方向，尽量覆盖以下维度：\n\n1. **正向搜索**：直接搜索主题相关论文\n   - `{topic} {subtopic} {year}`\n   - `{method_name} for {task_name}`\n\n2. **竞争论文搜索**（最关键！）：\n   - `{core_problem} {year}` — 有没有人在解决同样的问题？\n   - `{approach_keyword} {task} {year}` — 有没有人用类似方法？\n   - `{gap_description} solution` — 你发现的 gap 是否已被解决？\n   - **搜索知名团队的最新工作**：如果你知道哪些团队在做这个方向，搜索他们最近 6 个月的论文\n\n3. **相邻领域搜索**：\n   - `{method_from_other_field} applied to {your_task}`\n   - `{your_problem} in {adjacent_domain}` — 其他领域是否已解决类似问题\n\n4. **反面搜索**（找到反对你 idea 的证据）：\n   - `{your_approach} limitations` / `{your_approach} failure`\n   - `why {assumed_gap} is not a problem`\n   - `{baseline_method} sufficient for {task}` — baseline 是否其实已经够好\n\n5. **引用链追踪**（发现遗漏工作的最有效方法）：\n   - 找到一篇核心相关论文后，用 WebFetch 阅读它的 references 部分\n   - 在 Semantic Scholar 上查看它的 \"cited by\" — 最近引用它的论文很可能是 concurrent work\n   - 对 3 个以上核心相关论文重复此步骤\n\n### 搜索数量建议（理想目标，上下文充裕时尽量达到）\n\n| 角色 | 建议搜索次数 | 说明 |\n|------|-------------|------|\n| Round 1 Generator | 10-15 次 | 每个方向争取 3 次独立搜索 |\n| Round 2 Generator | 5-8 次 | 验证 approach 可行性 + baseline |\n| Review Agent | 8-12 次 | 独立验证 + 竞争论文 + 反面证据 |\n| Revision Agent | 5-10 次 | 针对每个 issue 独立调研 |\n\n### 上下文管理\n\n你的输出 token 有限，必须在上下文耗尽之前完成 JSON 输出。\n\n- 上述搜索次数是理想目标。在上下文充裕时应尽量多搜、深搜，搜得越充分越好。\n- 但必须动态评估剩余上下文：如果已经消耗了大量上下文，应优先完成输出，不要为了凑次数而冒着无法输出的风险。\n- WebFetch 深度阅读很有价值，但每次 fetch 消耗大量 token——优先 fetch 最关键的 2-3 篇，而不是每篇都 fetch。\n- 质量 > 数量：5 次精准搜索 + 深度思考 > 15 次浅层搜索。\n\n\nAs a reviewer, your search focus should be:\n1. **验证 claim**：Generator 声称的 SOTA、gap、novelty 是否属实\n2. **找竞争论文**：是否有 Generator 遗漏的高度相关/相似的工作\n3. **找反面证据**：是否有论文表明 Generator 的 approach 行不通\n4. **引用链检查**：通过核心论文的 cited-by 发现 concurrent work\n\n## 竞争论文专项搜索（Reviewer 独有）\n\n这是你作为 Reviewer 最重要的职责之一——发现 Generator 遗漏的竞争工作：\n\n1. **关键词变体搜索**：用至少 3 种不同的关键词组合搜索同一个问题\n   - 同义词替换（e.g., 'efficient' → 'lightweight/fast/scalable'）\n   - 不同粒度（e.g., 'text classification' → 'sentiment analysis' → 'NLP'）\n   - 方法名 + 任务名的不同组合\n\n2. **知名团队追踪**：如果你知道哪些团队/实验室在做相关方向，\n   搜索他们最近的论文（`\"team_name\" OR \"author_name\" {topic} {year}`）\n\n3. **会议最新录用**：搜索最近一轮 ICML/NeurIPS/ICLR/AAAI/ACL 等会议的 accepted papers\n   - `site:openreview.net {topic} 2026`\n   - `{conference_name} 2026 accepted papers {topic}`\n\n4. **arXiv 近 3 个月密集搜索**：对精确相关的关键词，搜索过去 3 个月的 arXiv 论文\n   这是发现 concurrent work 最有效的窗口\n\n如果你发现了 Generator 遗漏的重要相关工作，必须在 issues 中列出论文标题和链接，\n并在 feedback 中说明这些工作如何影响 idea 的 novelty。\n\n## Review checklist\n1. **SOTA freshness**: Are the models/baselines cited actually current SOTA?\n   If outdated, specify what the current SOTA is and cite your source.\n2. **Reference verification**: Do the cited papers actually exist? (WebSearch to check)\n3. **Gap validity**: Does the claimed research gap still exist, or has recent work addressed it?\n4. **Venue validity**: Are target_venues' submission deadlines after 2026-05-16?\n5. **Feasibility**: Is the resource estimate realistic? Are there hidden dependencies?\n6. **Novelty**: Is this sufficiently different from existing work?\n   When scoring novelty < 4:\n   - You MUST identify the closest existing work(s) via WebSearch\n   - In your feedback, write: \"This idea is too similar to [Paper Title (Venue Year)]. Specifically, [what overlaps]. To differentiate, the generator should [suggestion].\"\n   - This gives the generator targeted guidance to boost novelty, not just \"be more novel\".\n7. **Cost realism across modes**: Are the three mode estimates (manual/human-in-loop/auto) internally consistent?\n   - Auto Research uses more GPU hours (2-5x manual) but GPU idle rate should be near zero\n   - Auto Research timeline should reflect resource availability as bottleneck — days with sufficient GPUs, not weeks\n   - Human-in-Loop should fall between manual and auto on most dimensions\n   - Manual and HIL must NOT include salary/wages — only GPU and API costs\n   - Auto Research must NOT include agent operational overhead\n   - If any mode estimate is clearly unrealistic, flag it\n\n## Idea under review (round 5/10)\n{\n  \"title\": \"Miscalibration-Triggered Adaptive Generation via Logit-Level Intervention\",\n  \"core_problem\": \"Overconfident hallucinations—where an LLM asserts falsehoods with high verbal confidence despite internal epistemic uncertainty—are the most user-deceptive failure mode. Standard factuality metrics (FActScore, TruthfulQA) treat all hallucinations equally, but overconfident ones are disproportionately harmful because users cannot distinguish them from accurate claims. Existing inference-time mitigation methods each have critical limitations: (1) activation steering (Ji et al., TA-ITI) is undermined by Endogenous Steering Resistance in larger models; (2) external-monitor approaches (Monitoring Decoding) require expensive reference models; (3) density-estimation approaches (PC-LDCD) detect hallucinations as geometric anomalies—tokens drifting off the 'factual manifold'—but explicitly fail on overconfident hallucinations where the model's probability distribution is sharply peaked around wrong answers and hidden states appear on-manifold because the model 'believes' its incorrect output; (4) recent calibration-aware methods (CAG, CURE) require model fine-tuning, precluding deployment on frozen models; and (5) post-generation approaches (CSS) cannot prevent overconfident hallucinations from being generated and consumed during streaming. The fundamental gap: overconfident hallucinations are uniquely characterized by a verbal-internal mismatch signal (high confidence expression + high probe-detected hallucination probability), yet no existing method uses this specific signal as a trigger for during-generation logit-level intervention that is immune to the model's internal resistance mechanisms.\",\n  \"opportunity\": \"Ji et al. (EMNLP 2025 Outstanding) proved verbal-internal uncertainty mismatch predicts hallucinations better than uncertainty alone, validating the VUF direction on Llama-3.1-8B (31.9% relative hallucination reduction), Mistral-7B, and Qwen2.5-7B—but only demonstrated offline binary activation intervention on short-form QA, now undermined by ESR in larger models. Critically, they showed Llama-3.1-8B is significantly more responsive to VUF intervention than Qwen, suggesting cross-model evaluation will reveal architecture-dependent effectiveness patterns. PC-LDCD (arXiv 2605.05953) achieves SOTA TruthfulQA via density-anomaly detection but acknowledges the fundamental limitation that 'traditional uncertainty measures fail completely when LLMs produce high-confidence hallucinations where the model consistently generates incorrect output with high certainty.' This is precisely the gap MisTAG fills: where PCNet sees a normal-density hidden state (the model is confidently producing tokens that look on-manifold), MisTAG's miscalibration score detects the verbal-internal mismatch that marks overconfident errors. The theoretical connection is grounded by Kalai-Vempala's framework (PMC 2026) showing miscalibration is causally linked to hallucination rates. Concurrently, CSS (arXiv 2604.17487) demonstrated that semantic specificity backoff achieves 0.913 overcommitment-aware utility post-generation, proving the value of calibration-aware output control—but cannot intervene during streaming. The opportunity: combine the miscalibration trigger (uniquely targeting overconfident hallucinations that density methods miss) with ESR-immune logit-level intervention for training-free during-generation control, validated across model families.\",\n  \"landscape\": \"Ji et al. (EMNLP 2025) showed ~30% reduction in overconfident hallucinations via linear activation intervention on the VUF direction across Llama-3.1-8B (most responsive), Mistral-7B, and Qwen2.5-7B, but only for short-form answers with binary logic, and ESR (arXiv 2602.06941, Feb 2026) demonstrates that Llama-3.3-70B actively resists activation steering mid-generation. Monitoring Decoding (Chang et al., ACL 2025 Findings) monitors factuality during generation using a reference model's probability distribution, triggering tree-based resampling (+15.4% TruthfulQA with 5.7x latency); requires a larger reference model. PC-LDCD (Nielsen et al., arXiv 2605.05953, May 2026) trains PCNet over the residual stream to detect hallucinations as geometric anomalies, triggering selective contrastive decoding; achieves TruthfulQA True+Info up to 0.78 on Qwen3-4B across Llama-3.2-1B/3B, Qwen3-4B, and Mistral-Small-24B. However, PC-LDCD detects tokens whose hidden-state density deviates from factual clusters—it fundamentally cannot catch overconfident hallucinations where the model produces on-manifold representations with high certainty about incorrect content. DoLa (ICLR 2024) contrasts logits across layers (+12-17% TruthfulQA). ActLCD (EMNLP 2025) extends DoLa with RL-optimized layer selection (+19.81% TruthfulQA). Simple Factuality Probes (obalcells et al., EMNLP 2025 Findings) detect entity-level hallucinations with AUC 0.87-0.90 across Llama-3.1-8B, Qwen-2.5-7B, Gemma-2-9B, and Mistral-Small-24B, with cross-model transfer within 0.02-0.04 AUC, and provide pretrained probes for all model families—but offer no intervention mechanism. **Concurrent work (2026)**: CAG (arXiv 2605.01749) improves long-form factuality by up to 13% via exploration-commitment decoupling but requires multi-stage fine-tuning. CURE (arXiv 2604.12046) achieves +39.9% claim-level accuracy via reasoning calibration but requires training. CSS (arXiv 2604.17487) achieves training-free post-generation claim-level specificity backoff (0.913 overcommitment-aware utility on LongFact via semantic backoff—making claims less specific rather than adding hedge language), but operates post-hoc, cannot intervene during streaming, and does not use internal uncertainty signals. CLC (arXiv 2502.19110) provides conformal guarantees on factuality-specificity tradeoff but requires fine-tuning. Streaming Hallucination Detection (arXiv 2601.02170) monitors chain-of-thought reasoning trajectories but targets reasoning-step coherence rather than factual overconfidence in long-form generation. Logit-Level Steering (Tao et al., arXiv 2601.10960) validates training-free logit intervention for controllable generation (+47% accuracy) but uses static score tables. Kalai-Vempala's framework (PMC 2026) provides theoretical grounding that miscalibration causally drives hallucination rates, with empirical evidence across model scales. Beyond Precision (arXiv 2604.03141) shows current LLMs achieve substantially better precision than recall, establishing that selective abstention at the claim level can improve precision without catastrophic recall loss. **Gap**: No existing work combines (a) a miscalibration-specific trigger that catches the on-manifold overconfident hallucinations that density methods miss, (b) ESR-immune logit-level intervention, (c) honest dual-contribution framing separating calibration correction from factuality improvement, (d) training-free during-generation operation validated across multiple model families.\",\n  \"approach\": \"We propose MisTAG (Miscalibration-Triggered Adaptive Generation), a training-free inference-time framework that monitors verbal-internal uncertainty mismatch during long-form generation and triggers ESR-immune logit-level interventions graded by mismatch severity. We make an explicit and honest dual-contribution claim: (1) **calibration correction** via hedging (reducing overconfident expression of uncertain content, measured by OHR and ECE—NOT claimed as factuality improvement), and (2) **factuality improvement** via rollback (preventing the most confidently-hallucinated content from being emitted, measured by FActScore). We evaluate on two model families: Qwen3-8B and Llama-3.1-8B-Instruct (co-primary).\\n\\n**Prerequisite Validation (Days 1-3)**: Before main experiments, for EACH target model (Qwen3-8B and Llama-3.1-8B): (a) Extract VUF direction following Ji et al.'s methodology (validated on both families in original paper—Llama showed strongest response); (b) Train linear factuality probes on hidden states (obalcells provides pretrained probes for Llama-3.1-8B and methodology for new models, with reported AUROC 0.87-0.90); (c) Verify probe AUROC ≥0.85 on held-out LongFact generations; (d) Verify entity-concentration via span-level activation analysis. If AUROC <0.85 on either model, add explicit NER-based entity gating as fallback. This validation is a go/no-go gate.\\n\\n**Miscalibration Detection**: At each generated token, we compute a miscalibration score as the discrepancy between (1) verbal confidence, extracted via projection onto the VUF direction in the residual stream at the final layer, and (2) internal epistemic uncertainty, estimated via a lightweight linear factuality probe. The miscalibration score: M(t) = σ(VUF_confidence(t)) × probe_hallucination_prob(t). High verbal confidence multiplied by high probe-estimated hallucination probability yields high miscalibration. This score specifically identifies tokens where the model is confidently wrong—the signature of overconfident hallucinations that density-based methods (PC-LDCD) cannot catch because such tokens have on-manifold hidden states.\\n\\n**Graded Logit-Level Intervention** (ESR-immune: operates on output distribution post-residual-stream):\\n\\n- *Mild mismatch (M(t) > τ_mild) → Hedge (CALIBRATION correction only)*: Apply a static logit bias vector b ∈ R^|V| at next-token prediction: log p'(v) = log p(v) + α·b(v). The bias vector: b(v) = +1 for hedge tokens (~50 tokens: 'likely', 'approximately', 'reportedly', 'possibly', 'around', 'roughly', 'perhaps', 'estimated', etc.), b(v) = -1 for assertive tokens (~30 tokens: 'definitely', 'certainly', 'clearly', 'undoubtedly', 'always', 'never', 'exactly', etc.), b(v) = 0 otherwise. **We explicitly do NOT claim this improves FActScore**: hedging 'approximately 1067' still produces a verifiable atomic fact that FActScore judges as unsupported. The hedge action's value is purely calibration—making verbal expression match internal uncertainty (reducing OHR and ECE). This is a distinct and novel contribution: existing methods either ignore calibration entirely (DoLa, ActLCD, PC-LDCD) or require fine-tuning for it (LoGU, CAG).\\n\\n- *Severe mismatch (M(t) > τ_severe) → Rollback+Regenerate (FACTUALITY improvement)*: Rollback to last sentence boundary (discard tokens and KV-cache entries), then regenerate with: (i) constrained prefix forcing an epistemic marker ('I'm not certain, but', 'Some sources suggest'), AND (ii) hedge logit bias at 2× mild level, AND (iii) temperature reduction (T=0.3) to encourage more conservative token selection. **This action IS claimed as factuality improvement**: by preventing the most confidently-hallucinated sentences from being emitted and regenerating under uncertainty-aware constraints, we hypothesize FActScore improves via two mechanisms: (a) forced uncertainty prefix causes the model to generate less specific claims (reducing unsupported atomic facts per sentence), and (b) temperature reduction + hedging shifts the model away from the overconfident generation trajectory. **Anti-cascading safeguards**: (1) 30-token cooldown after rollback (mild hedging remains active); (2) Maximum 3 rollbacks per generation; if exceeded, persistent mild-level hedging.\\n\\n**Core Novelty Experiment: Confusion-Matrix Analysis vs. PC-LDCD**: To empirically ground our differentiation claim, we design a head-to-head token-level comparison. For each hallucinated atomic fact (per FActScore verification), we record: (a) MisTAG's miscalibration score M(t) at the entity-bearing tokens, (b) PC-LDCD's PCNet density score (NLL) at the same tokens. We categorize hallucinations into four quadrants: (Q1) Both flag: high M(t) AND high NLL—general hallucinations detectable by either method; (Q2) MisTAG-only: high M(t) but low NLL—overconfident hallucinations where the model is wrong but its hidden state looks on-manifold (PC-LDCD misses these); (Q3) PC-LDCD-only: low M(t) but high NLL—uncertain hallucinations where the model expresses uncertainty (MisTAG correctly avoids flagging as overconfident); (Q4) Neither flags. **Our core hypothesis**: Q2 is non-trivially populated (≥15% of hallucinated facts) and represents the specific failure mode that only the miscalibration trigger catches. This analysis is the paper's strongest novelty evidence.\\n\\n**OHR Metric Validation Study**: To preempt the 'self-defined metric' objection, we conduct a small-scale annotation study. We sample 100 hallucinated atomic facts (50 from each model), and for each: (a) apply automated OHR detection (regex/spaCy-based hedging-marker identification following Ji et al.'s annotation scheme), (b) collect binary human annotations from 2 trained annotators ('Was this claim expressed with assertive confidence?' yes/no). We compute Cohen's kappa between automated and human annotation (target: κ ≥ 0.85) and between the two human annotators (expected: κ ≥ 0.80 based on comparable annotation tasks in the calibration literature). This takes <1 day and validates OHR as a reliable automated metric. Additionally, we report ECE (Expected Calibration Error) computed over atomic-fact-level confidence bins as an established complementary metric.\\n\\n**Threshold Optimization**: Two-stage principled approach. Stage 1: Logistic regression on validation miscalibration scores (M(t) at entity tokens, labeled by FActScore verification) to determine τ_mild (80% recall of hallucinated entities) and τ_severe (95% precision). Stage 2: Grid search over α ∈ {0.5, 1.0, 1.5, 2.0, 2.5} with hard constraints: length_reduction < 15%, Δperplexity < 5%. Thresholds are set independently per model (Qwen3-8B and Llama-3.1-8B) to account for model-family differences in VUF sensitivity (Ji et al. showed Qwen is less responsive than Llama). Validation set: ~150 long-form biography generations per model from FActScore's entity set.\\n\\n**Latency Benchmarking**: Per-token overhead (ms/token) and end-to-end throughput for: (a) baseline greedy, (b) MisTAG detection-only, (c) MisTAG with hedge, (d) MisTAG with hedge+rollback. Expected: <5% overhead for detection (two dot products on already-extracted hidden states); rollback incurs sentence-regeneration cost proportional to rollback rate.\\n\\n**Evaluation**: Co-primary evaluation on Qwen3-8B (FP16, A100 80GB) and Llama-3.1-8B-Instruct (FP16, A100 80GB). Optional scaling ablation: Qwen3-32B (INT8, H100 80GB).\\n\\n*Benchmarks (4 axes)*: (1) **TruthfulQA** (MC1, MC2, True+Info) for short-form truthfulness; (2) **FActScore biographies** for long-form factual precision—primary metric for rollback contribution; (3) **OHR (Overconfident Hallucination Rate)** + **ECE (Expected Calibration Error)** for calibration quality—primary metrics for hedge contribution; (4) **MT-Bench** for dialogue quality preservation. We additionally report FActScore precision AND recall (following Jafari et al. 2026) to verify that hedging does not artificially inflate precision at recall's expense.\\n\\n*Baselines (5 primary, applied to BOTH models)*: (a) Greedy/nucleus decoding, (b) DoLa contrastive decoding, (c) ActLCD, (d) PC-LDCD (reimplemented with PCNet trained on same data—critical for confusion-matrix analysis), (e) Detect-only probe (obalcells) without intervention. *Secondary* (time-permitting): (f) Ji et al.'s activation intervention (demonstrating ESR limitation on 8B models), (g) Monitoring Decoding (using 32B reference for 8B target).\\n\\n*Ablation studies*: (i) Hedge-only vs. Rollback-only vs. full MisTAG (disentangling calibration vs. factuality contributions across both models), (ii) Miscalibration trigger vs. probe-only trigger vs. VUF-only trigger (validating mismatch signal superiority), (iii) Anti-cascading ablation, (iv) Threshold sensitivity (±1 SD), (v) Cross-model analysis: does the miscalibration signal generalize? (compare M(t) distributions across Qwen3-8B vs. Llama-3.1-8B for the same factual errors).\\n\\n*Analysis*: (a) Confusion-matrix breakdown (Q1-Q4) showing MisTAG's unique coverage vs. PC-LDCD, (b) Per-component FActScore and OHR attribution, (c) Hedge-FActScore interaction: empirically verify that hedging does NOT improve FActScore (honesty contribution), (d) FActScore precision vs. recall under each intervention, (e) Latency profiling, (f) Qualitative examples from each quadrant of the confusion matrix.\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"~130h A100 80GB + ~20h H100 80GB (probe validation 2×5h=10h, probe training 2×3h=6h, VUF extraction 2×3h=6h, PCNet reimplementation+training 15h, threshold optimization 2×8h=16h, main experiments 2 models × 4 benchmarks × 5 baselines ~55h, confusion-matrix analysis 8h, ablations ~25h, latency benchmarking 5h, OHR annotation study 2h compute, Qwen3-32B scaling ablation ~20h H100)\",\n      \"gpu_utilization\": \"~40-45% effective; GPU idles during annotation, analysis, and threshold iteration\",\n      \"timeline\": \"6-7 weeks\",\n      \"team\": \"1-2 researchers\",\n      \"estimated_gpu_cost\": \"$385 (130h × $2.50/h A100 spot + 20h × $3.00/h H100 spot)\",\n      \"evaluation_api_cost\": \"$150-250 (FActScore verification: using vLLM-served Llama-3.1-70B locally for primary evaluation, GPT-4o for 50-biography validation subset ~$80; MT-Bench LLM-judge: ~$50-80 for 2 models × 5 conditions × 80 conversations; OHR validation: $20 for annotator compensation)\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"~160h A100 80GB + ~30h H100 80GB (comprehensive threshold sweeps, PCNet reimplementation, all baselines on both models, probe validation, OHR annotation coordination, INT8 probe training)\",\n      \"gpu_utilization\": \"~55-65% effective\",\n      \"timeline\": \"4-5 weeks\",\n      \"team\": \"1 researcher, ~50min/day reviewing experiments + coordinating 2 annotators for OHR validation (1 day)\",\n      \"claude_api_cost\": \"$80-160 (800-1600 turns for implementation, PCNet reimplementation, evaluation orchestration)\",\n      \"estimated_gpu_cost\": \"$490 (160h × $2.50/h A100 + 30h × $3.00/h H100)\",\n      \"evaluation_api_cost\": \"$200-350 (FActScore: local Llama-3.1-70B primary + GPT-4o validation ~$100; MT-Bench: ~$80; OHR annotation: ~$40; additional FActScore runs for ablations: ~$80)\",\n      \"risk_note\": \"PCNet reimplementation is prerequisite for confusion-matrix analysis (code on GitHub); probe validation on both models is go/no-go gate (Days 1-3); OHR annotation requires 2 annotators with NLP background\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"~200h A100 80GB + ~40h H100 80GB (full baseline sweep on both models, comprehensive confusion-matrix analysis across multiple generation sets, probe architecture comparison, all ablations automated)\",\n      \"gpu_utilization\": \">85% effective; continuous pipelining across two models\",\n      \"timeline\": \"12-16 days with 2× A100 80GB + 1× H100 80GB (one A100 per primary model, H100 for scaling ablation)\",\n      \"team\": \"0 (initial setup: HuggingFace tokens, annotator recruitment for OHR validation)\",\n      \"claude_api_cost\": \"$180-400 (1800-4000 turns for end-to-end implementation on 2 models, PCNet reimplementation, evaluation, paper drafting)\",\n      \"estimated_gpu_cost\": \"$620 (200h × $2.50/h A100 + 40h × $3.00/h H100)\",\n      \"evaluation_api_cost\": \"$300-500 (FActScore: local 70B primary, GPT-4o validation on both models ~$150; MT-Bench across all conditions: ~$120; additional ablation evaluation: ~$130; OHR annotation: ~$40)\",\n      \"speed_bottleneck\": \"PCNet reimplementation and training (requires probabilistic circuit library), OHR human annotation coordination (1-day blocking task)\",\n      \"risk_note\": \"Confusion-matrix analysis depends on successful PCNet reimplementation; if Q2 population is <10%, the differentiation claim weakens—fallback: reframe as 'complementary detection' rather than 'superior detection'\"\n    }\n  },\n  \"target_venues\": [\n    \"EMNLP 2026 (ARR submission deadline: May 25, 2026; conference: October 24-29, Budapest)\",\n    \"AAAI 2027 (expected deadline: ~August 2026; conference: February 16-23, Montréal)\",\n    \"ICLR 2027 (expected deadline: ~October 2026)\"\n  ],\n  \"level\": \"solid-to-strong\",\n  \"key_references\": [\n    \"Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations (Ji et al., EMNLP 2025 Outstanding) — validated VUF on Llama-3.1-8B, Mistral-7B, Qwen2.5-7B; Llama most responsive\",\n    \"Endogenous Resistance to Activation Steering in Language Models (arXiv 2602.06941, Feb 2026)\",\n    \"Monitoring Decoding: Mitigating Hallucination via Evaluating the Factuality of Partial Response during Generation (Chang et al., ACL 2025 Findings)\",\n    \"Hallucination as an Anomaly: Dynamic Intervention via Probabilistic Circuits (Nielsen et al., arXiv 2605.05953, May 2026) — key comparison target; acknowledges failure on overconfident hallucinations\",\n    \"Real-Time Detection of Hallucinated Entities in Long-Form Generation (obalcells et al., EMNLP 2025 Findings) — pretrained probes for Llama-3.1-8B, Qwen-2.5-7B, Gemma-2-9B, Mistral-Small-24B\",\n    \"DoLa: Decoding by Contrasting Layers Improves Factuality (ICLR 2024)\",\n    \"Active Layer-Contrastive Decoding Reduces Hallucination (ActLCD, EMNLP 2025)\",\n    \"Only Say What You Know: Calibration-Aware Generation for Long-Form Factuality (CAG, arXiv 2605.01749, May 2026)\",\n    \"Think Through Uncertainty: Improving Long-Form Generation Factuality via Reasoning Calibration (CURE, arXiv 2604.12046, April 2026)\",\n    \"Answer Only as Precisely as Justified: Calibrated Claim-Level Specificity Control (CSS, arXiv 2604.17487, April 2026) — semantic backoff post-generation; 0.913 utility on LongFact\",\n    \"Conformal Linguistic Calibration: Trading-off between Factuality and Specificity (CLC, arXiv 2502.19110, Feb 2025)\",\n    \"Steering Language Models Before They Speak: Logit-Level Interventions (Tao et al., arXiv 2601.10960, Jan 2026)\",\n    \"Streaming Hallucination Detection in Long Chain-of-Thought Reasoning (arXiv 2601.02170, Jan 2026)\",\n    \"Hallucination, monofacts, and miscalibration: An empirical investigation (PMC 2026) — theoretical grounding for miscalibration-hallucination causal link\",\n    \"Beyond Precision: Importance-Aware Recall for Factuality Evaluation (Jafari et al., arXiv 2604.03141, April 2026)\",\n    \"Mind the Confidence Gap: Overconfidence, Calibration, and Distractor Effects in LLMs (arXiv 2502.11028) — ECE validation, Cohen's kappa 0.82\",\n    \"FActScore: Fine-grained Atomic Evaluation of Factual Precision in Long Form Text Generation (EMNLP 2023)\",\n    \"LLM.int8(): 8-bit Matrix Multiplication for Transformers at Scale (Dettmers et al., NeurIPS 2022)\",\n    \"LoGU: Long-form Generation with Uncertainty Expressions (ACL 2025)\"\n  ],\n  \"description\": \"Overconfident hallucinations—where an LLM asserts falsehoods with high verbal confidence despite internal epistemic uncertainty—are the most user-deceptive failure mode. Density-based detection (PC-LDCD) fundamentally cannot catch these because the model's hidden states appear on-manifold when it is confidently wrong. We propose MisTAG, a training-free inference-time framework that computes a miscalibration score at every token (verbal confidence via VUF projection × factuality probe hallucination probability) to specifically detect on-manifold overconfident hallucinations, then triggers ESR-immune logit-level interventions graded by severity. We make an honest dual-contribution claim: (1) a hedge logit bias for mild miscalibration provides CALIBRATION correction only—making verbal expression match internal uncertainty (reducing OHR and ECE, NOT FActScore); (2) sentence-level rollback with constrained regeneration for severe cases provides FACTUALITY improvement (improving FActScore by preventing the most confident hallucinations from being emitted). The paper's core novelty evidence is a confusion-matrix analysis showing that a non-trivial fraction of hallucinated facts (hypothesized ≥15%) are 'on-manifold overconfident'—flagged by MisTAG's miscalibration trigger but missed by PC-LDCD's density anomaly detection. We evaluate co-primarily on Qwen3-8B AND Llama-3.1-8B-Instruct (two model families, addressing cross-model generalization), with Qwen3-32B as scaling ablation. OHR is validated via a 100-example annotation study targeting Cohen's κ ≥ 0.85, complemented by established ECE. Thresholds are model-specific (accounting for Llama's higher VUF sensitivity vs. Qwen's lower sensitivity, per Ji et al.'s findings). Evaluation API costs are explicitly budgeted ($200-500) using local Llama-3.1-70B for primary FActScore verification with GPT-4o validation subset.\",\n  \"project_name\": \"mistag_gen_control\",\n  \"source\": \"web_research\"\n}\n\n\n## Previous review history\n### Round 1 review\nVerdict: revise\nIssues: [\"Endogenous Steering Resistance (ESR, arxiv 2602.06941, Feb 2026) shows that larger LLMs can resist and override activation steering mid-generation. This directly undermines the 'hedge insertion via activation steering along VUF direction' mechanism, especially for Llama 4 Maverick (400B params). The paper shows Llama-3.3-70B exhibits substantial ESR—larger models like Maverick will likely resist more.\", \"Online per-claim segmentation during autoregressive generation is never specified. How do you identify claim boundaries in real-time? FActScore-style decomposition uses a separate LLM call post-hoc. Token-level probes (like the Real-Time Detection paper, arxiv 2509.03531) avoid this problem by working at token level. The proposal conflates 'per-claim' monitoring with 'online' generation without addressing this fundamental tension.\", \"Citation injection ('pause generation to retrieve and inject supporting citations') requires interrupting autoregressive generation, performing retrieval, and conditioning further generation on retrieved passages. This means modifying the KV-cache, potentially resetting generation state, or using a complex interleaving mechanism. No existing system does this reliably mid-generation without explicit architecture support (like RETRO). The mechanism is undefined.\", \"'Training-free' claim is misleading: factuality probes require supervised training on labeled hallucination data, VUF extraction requires contrastive data collection, and threshold optimization requires a labeled validation set. The system is 'LLM fine-tuning-free' but still requires substantial supervised signal. This distinction matters for positioning against baselines.\", \"Llama 4 Maverick (400B total MoE params, 17B active) requires minimum 4x A100 80GB even with INT4 quantization for inference. Hidden state extraction for probing during generation significantly increases memory requirements (storing intermediate activations). The 200 A100-hour budget for 3 models × 3 benchmarks including this 400B model is unrealistically tight.\", \"Missing MT-Bench and MMLU evaluation—the user's hard constraints require 'utility preservation' metrics, but the proposal only mentions FActScore-based optimization and three factuality benchmarks. Without explicit utility metrics, the paper cannot demonstrate it 'doesn't kill helpfulness while suppressing hallucinations.'\", \"11-day timeline is extremely aggressive for a system with this many interacting components: VUF extraction for 3 new models, probe training, multi-action policy implementation, threshold optimization, RAG integration for citation injection, FActScore evaluation (API-rate-limited), ablations across 3 models × 3 benchmarks, plus paper writing.\"]\nFeedback: The idea has a solid conceptual foundation but faces critical execution gaps. Priority revisions: (1) **Drop activation steering for hedging** — ESR makes it unreliable for larger models. Replace with token-probability manipulation (e.g., boost uncertainty-expressing tokens via logit bias) or constrained decoding that forces hedge tokens when mismatch is detected. (2) **Switch from per-claim to per-sentence or per-entity monitoring** — use sentence boundaries (easily detected via punctuation tokens) or entity-span boundaries (using the obalcells/hallucination_probes token-level approach) instead of undefined 'claim' boundaries. (3) **Simplify to two actions** (hedge + abstain) and drop citation injection — mid-generation RAG is an unsolved architectural challenge that deserves its own paper. You can mention it as future work. (4) **Replace Llama 4 Maverick with Llama 3.1 70B or Qwen3-32B** — these fit on 1-2 A100s with room for hidden state extraction, making the compute budget realistic. (5) **Rename 'training-free' to 'fine-tuning-free'** to be honest about the probe training and threshold optimization requirements. (6) **Add explicit utility preservation evaluation**: MT-Bench and MMLU as required by the user constraints. (7) **Scope reduction for 11-day timeline**: focus on 2 models, 2 benchmarks, 2 actions — a clean, focused contribution is publishable; an overscoped half-finished one is not.\n\n### Round 2 review\nVerdict: revise\nIssues: [\"Critical missing related work: 'Monitoring Decoding: Mitigating Hallucination via Evaluating the Factuality of Partial Response during Generation' (ACL 2025 Findings, arXiv 2503.03106) does real-time hallucination monitoring during generation with selective token-level intervention via tree-based decoding. Achieves +15% on TruthfulQA. This directly competes in the 'online detect-then-intervene' paradigm and MUST be cited and compared against.\", \"Critical concurrent work: 'Hallucination as an Anomaly: Dynamic Intervention via Probabilistic Circuits' (arXiv 2605.05953, published ~May 8, 2026) proposes PC-LDCD—selective contrastive decoding triggered by internal representation anomaly detection on the residual stream. Achieves SOTA on TruthfulQA for models up to 8B. Conceptually near-identical paradigm (internal signal → selective logit-level intervention) with different trigger signal (density anomaly vs. miscalibration). Must be cited, differentiated, and ideally used as a baseline.\", \"Entity onset detection is underspecified and misattributed. The proposal claims obalcells' probes provide an 'entity-onset signal,' but their probes classify whether tokens belong to HALLUCINATED entities—they do not identify entity boundaries for all entities during generation. A separate NER-like mechanism is needed to identify where to compute the miscalibration score, and this component is not described.\", \"The 'learned logit bias vector' training procedure is unspecified. What training data? What loss function? Is it a fixed hand-crafted vector (boosting hedging tokens) or learned from data? If learned, what constitutes the positive/negative examples? This is a core component of the mild-mismatch intervention and needs full specification.\", \"Qwen3-32B at FP16 consumes ~64GB + 15-20% framework overhead = 73-77GB on A100 80GB, leaving <3GB for KV-cache and hidden state extraction. INT8 quantization is mandatory but creates a probe-quality risk: if probes are trained on FP16 hidden states and evaluated on INT8 states, the representation distribution shift could degrade detection accuracy. No mitigation plan is specified.\", \"Compute budget ambiguity: The user constraint is ≤200 H100-hours, but the proposal estimates in A100-hours. Auto research mode at 350 A100-hours, while likely within budget after H100 conversion (due to H100's higher throughput), should be explicitly stated in H100-equivalent terms to confirm compliance.\"]\nFeedback: The idea is well-motivated and the round 1 revisions (dropping activation steering, simplifying to 2 actions, removing citation injection, replacing Maverick) are all correct improvements. The core contribution—showing miscalibration is a better trigger signal than raw uncertainty for selective intervention—is valid. To reach pass threshold:\n\n1. **Cite and differentiate from Monitoring Decoding (ACL 2025) and PC-LDCD (May 2026)**: Monitoring Decoding uses external factual consistency checking (LLM-based monitor) which is expensive; PC-LDCD uses density estimation requiring a separate trained probabilistic circuit. MisTAG's advantage is that miscalibration (VUF vs. probe) is cheaper to compute and directly targets the failure mode (overconfident hallucination) rather than general factual error. Make this explicit.\n\n2. **Specify entity onset detection**: Use a simple heuristic: apply miscalibration scoring at EVERY token but weight by the probe's hallucination probability (which naturally peaks at entity tokens). Alternatively, use a lightweight NER pass on the prefix, or simply trigger scoring at every noun/proper-noun token identified by part-of-speech patterns. Don't rely on obalcells' probes for boundary detection—they detect hallucination, not boundaries.\n\n3. **Specify the logit bias vector**: Define it as a static vocabulary-level vector derived from a curated list of hedge tokens (+bias) and assertive tokens (-bias), with magnitudes tuned on the validation set. This is simpler and more robust than a 'learned' vector and avoids another training step.\n\n4. **Address INT8 quantization for Qwen3-32B**: Either (a) train probes directly on INT8 hidden states (cheap—just run forward passes in INT8 mode), or (b) make Qwen3-8B the primary evaluation target (fits easily in FP16 on A100 80GB) and treat Qwen3-32B as a scaling test with INT8-trained probes.\n\n5. **Add Monitoring Decoding and PC-LDCD as baselines**: This strengthens the paper by showing miscalibration-triggered intervention outperforms density-based (PC-LDCD) and factuality-monitor-based (MD) triggers on the specific failure mode of overconfident hallucinations.\n\n### Round 3 review\nVerdict: revise\nIssues: [\"Critical: TruthfulQA is absent from the evaluation plan despite being the primary benchmark for ALL cited baselines (DoLa: +12-17%, ActLCD: +19.81%, PC-LDCD: SOTA True+Info, Monitoring Decoding: +15.4%). Without TruthfulQA, no apples-to-apples comparison with any baseline is possible. This will be an immediate reviewer objection.\", \"The mild hedge intervention (logit bias boosting 'likely'/'approximately') does NOT improve factual precision—adding 'approximately 1066' to a wrong claim doesn't make it correct. FActScore evaluates atomic-fact truth, not confidence expression. Only the severe rollback action can improve FActScore, but aggressive rollback reduces content length. The paper needs to reconcile this tension: the hedge action may improve the custom OHR metric but not the standard FActScore metric, raising the question of whether the method actually reduces hallucinations or just decorates them with hedging language.\", \"Per-token latency overhead is never analyzed. Computing VUF projection + probe forward pass at EVERY generated token during long-form generation (potentially thousands of tokens) adds cumulative overhead. While the probe is lightweight (linear layer), the hidden state extraction and VUF dot product at every step need latency benchmarking. Monitoring Decoding reports 5.7x latency; MisTAG should report its overhead for fair comparison.\", \"Cascading rollback risk: After severe-mismatch rollback, the forced uncertainty prefix ('I'm not certain, but') is itself a high-verbal-uncertainty expression that may trigger the VUF component of the miscalibration score in the opposite direction, or the regenerated sentence could again trigger severe mismatch, causing infinite rollback loops. No cooldown mechanism or maximum rollback count is specified.\", \"The 'probe activation naturally peaks at entity-bearing tokens' claim (from obalcells) has only been validated on Llama model families. Whether this property transfers to Qwen3 models is assumed but unverified. If Qwen3 probes activate on different token types (function words, punctuation), the implicit entity-relevance weighting breaks down and the method could insert hedging at grammatically inappropriate positions.\", \"The composite threshold optimization objective L = FActScore_precision × (1 - length_reduction_ratio) × exp(-λ·Δperplexity) introduces an unspecified hyperparameter λ on top of the three parameters being optimized (τ_mild, τ_severe, α). With only ~200 validation examples and a 4-dimensional optimization surface, overfitting is a concern. The logistic regression boundary mentioned as an alternative (following AdaDec) would be more principled.\"]\nFeedback: The idea is well-motivated and the round 2 revisions are substantial improvements. The core contribution—miscalibration as a trigger signal for ESR-immune logit intervention—is valid. To reach pass threshold:\n\n1. **Add TruthfulQA evaluation** (non-negotiable). All 7 baselines report TruthfulQA numbers. Include it as a short-form complement to FActScore/LongFact long-form evaluation. This also enables direct numerical comparison with published baseline results.\n\n2. **Address the hedge–FActScore disconnect explicitly**. Either: (a) argue that the primary contribution is reducing OHR (overconfident hallucinations), with FActScore improvement as secondary via rollback, and position the paper accordingly; or (b) show via pilot experiments that hedging tokens actually DO improve FActScore by making the atomic-fact decomposition produce fewer false-positive claims (e.g., 'approximately 1066' might be judged as supported while 'exactly 1067' would not). If (b), test this assumption before building the paper's evaluation around it.\n\n3. **Add latency analysis**: Report tokens/second with and without MisTAG. The probe forward pass on hidden states should be cheap (<5% overhead per token based on literature on hidden-state probing), but you need to measure and report it, especially for the rollback case.\n\n4. **Add anti-cascading rollback mechanism**: Add a simple cooldown (e.g., suppress severe-mismatch triggering for N tokens after a rollback) and a maximum rollback count per generation (e.g., 3). This is trivial to implement and eliminates a clear failure mode.\n\n5. **Validate probe transfer to Qwen3**: In the first 1-2 days, train probes on Qwen3-8B and verify that (a) AUROC matches published levels (~0.85-0.90) and (b) activation peaks at entity-bearing tokens. If not, the method needs per-model calibration, which should be documented.\n\n6. **Simplify threshold optimization**: Drop the composite objective with unspecified λ. Use the logistic regression approach (already mentioned as following AdaDec) as the primary method. Grid search over τ_mild, τ_severe, α with FActScore precision as the objective and a hard constraint on length reduction ratio < 15% is cleaner and more reproducible.\n\n7. **Consider scope reduction**: With 11 days, focus on Qwen3-8B as the primary model with 3-4 key baselines (DoLa, ActLCD, PC-LDCD, greedy) on TruthfulQA + FActScore + MT-Bench. Treat Qwen3-32B and Monitoring Decoding baseline as secondary/ablation. A clean result on one model beats noisy results on two.\n\n### Round 4 review\nVerdict: revise\nIssues: [\"Single model family evaluation (Qwen3-8B primary, Qwen3-32B ablation) is insufficient for EMNLP. PC-LDCD tested 3 families (Llama, Qwen, Mistral), obalcells tested 4 families. Without at least one non-Qwen model (e.g., Llama-3.1-8B or Mistral-7B), reviewers will question whether the miscalibration signal generalizes or is Qwen-specific.\", \"The hedge action's contribution to actual factuality is uncertain and inadequately justified. Boosting 'likely'/'approximately' tokens doesn't correct misinformation—it decorates it with uncertainty language. FActScore still decomposes 'approximately 1067' into a verifiable atomic fact and judges it unsupported. The proposal acknowledges this ('we test this hypothesis empirically') but if hedging only improves OHR without improving FActScore, the paper's value proposition reduces to 'we made wrong answers sound less confident'—a weaker contribution for EMNLP's Generation track.\", \"API costs for FActScore evaluation (requires LLM-as-judge for atomic-fact decomposition + verification per biography) and MT-Bench (LLM-judge per conversation) are not budgeted. For ~200 biographies × multiple conditions × 5 baselines, FActScore alone requires thousands of LLM API calls. This could easily add $200-500+ in API costs unaccounted in the resource estimate.\", \"PC-LDCD differentiation needs empirical grounding, not just theoretical argument. The claim that miscalibration trigger specifically catches overconfident hallucinations that density-anomaly detection misses is the core novelty claim but is untested. Without a head-to-head comparison showing cases where PC-LDCD misses overconfident hallucinations that MisTAG catches, the 'better trigger signal' argument is hypothetical.\", \"OHR (Overconfident Hallucination Rate) as a primary metric is risky for venue acceptance. It is custom, unpublished, and its annotation scheme (detecting 'assertive language without hedging markers') requires validation of inter-annotator agreement or automated detection reliability. Reviewers may dismiss improvements on a self-defined metric.\"]\nFeedback: The proposal is technically sound and addresses all round 3 feedback. The remaining gap is demonstrating that MisTAG provides value BEYOND what PC-LDCD already delivers. To reach pass threshold:\n\n1. **Add one non-Qwen model** (Llama-3.1-8B is ideal—VUF validated on it, probes validated on Llama family, fits on A100). This is the most impactful change for EMNLP reviewers. Even if it's secondary (fewer ablations), having 2 families in the main results table is near-mandatory.\n\n2. **Commit to a clear contribution narrative**: Frame the paper as: (a) MisTAG's miscalibration signal targets a *specific* failure mode (overconfident hallucinations) that general-purpose methods (DoLa, PC-LDCD) do not specifically address; (b) the hedge action is a *calibration* contribution (measured by OHR + ECE), not a factuality contribution; (c) the rollback action is the *factuality* contribution (measured by FActScore). This dual-contribution framing is honest and novel. Don't oversell hedging as factuality improvement.\n\n3. **Design the PC-LDCD comparison to highlight your advantage**: Show a confusion-matrix analysis—what fraction of overconfident hallucinations does PC-LDCD miss that MisTAG catches? If M(t) triggers on cases where PCNet's density score is normal (because the model is confidently wrong in a way that looks 'on-manifold'), that's your strongest novelty evidence.\n\n4. **Budget API costs explicitly**: Add an 'evaluation API cost' line (~$300-500 for FActScore + MT-Bench across all conditions). This is realistic and shows awareness.\n\n5. **Validate OHR reliability**: Add a small annotation study (50-100 examples) showing that automated OHR annotation (using hedging-marker detection) agrees with human judgment at ≥0.85 Cohen's kappa. This takes <1 day and preempts the 'self-defined metric' objection.\n\n\n## Output format\nOutput ONLY a JSON object:\n{\n  \"verdict\": \"pass | revise | fail\",\n  \"scores\": {\n    \"novelty\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"feasibility\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"clarity\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"impact\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"}\n  },\n  \"issues\": [\"specific issue 1\", \"specific issue 2\", ...],\n  \"feedback\": \"Actionable feedback for the generator (if verdict=revise)\",\n  \"reason\": \"One-line summary of verdict rationale\"\n}\n\nRules:\n- \"pass\": idea is sound AND high quality — avg score >= 4.0, no critical issues\n- \"revise\": fixable issues OR scores below threshold — provide specific feedback\n- \"fail\": fundamental flaw (e.g., gap doesn't exist, approach provably wrong, or scores remain low after multiple revisions)\n- Threshold is HIGH (4.0/5.0): agent scores tend to be inflated, so only truly outstanding ideas should pass. An avg of 3.5 is NOT enough.\n- Round 10 only: if still \"revise\", you MUST choose \"pass\" or \"fail\"."
}
```

---

### Runtime record

_source line 2 · 2026-05-16T09:00:01.746Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-16T09:00:01.746Z",
  "sessionId": "3851818f-b8a5-4456-92d9-6671bfb78776"
}
```

---

## Round 1

28 recorded events

### User

_source line 3 · 2026-05-16T09:00:01.789Z_

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

## Idea under review (round 5/10)
{
  "title": "Miscalibration-Triggered Adaptive Generation via Logit-Level Intervention",
  "core_problem": "Overconfident hallucinations—where an LLM asserts falsehoods with high verbal confidence despite internal epistemic uncertainty—are the most user-deceptive failure mode. Standard factuality metrics (FActScore, TruthfulQA) treat all hallucinations equally, but overconfident ones are disproportionately harmful because users cannot distinguish them from accurate claims. Existing inference-time mitigation methods each have critical limitations: (1) activation steering (Ji et al., TA-ITI) is undermined by Endogenous Steering Resistance in larger models; (2) external-monitor approaches (Monitoring Decoding) require expensive reference models; (3) density-estimation approaches (PC-LDCD) detect hallucinations as geometric anomalies—tokens drifting off the 'factual manifold'—but explicitly fail on overconfident hallucinations where the model's probability distribution is sharply peaked around wrong answers and hidden states appear on-manifold because the model 'believes' its incorrect output; (4) recent calibration-aware methods (CAG, CURE) require model fine-tuning, precluding deployment on frozen models; and (5) post-generation approaches (CSS) cannot prevent overconfident hallucinations from being generated and consumed during streaming. The fundamental gap: overconfident hallucinations are uniquely characterized by a verbal-internal mismatch signal (high confidence expression + high probe-detected hallucination probability), yet no existing method uses this specific signal as a trigger for during-generation logit-level intervention that is immune to the model's internal resistance mechanisms.",
  "opportunity": "Ji et al. (EMNLP 2025 Outstanding) proved verbal-internal uncertainty mismatch predicts hallucinations better than uncertainty alone, validating the VUF direction on Llama-3.1-8B (31.9% relative hallucination reduction), Mistral-7B, and Qwen2.5-7B—but only demonstrated offline binary activation intervention on short-form QA, now undermined by ESR in larger models. Critically, they showed Llama-3.1-8B is significantly more responsive to VUF intervention than Qwen, suggesting cross-model evaluation will reveal architecture-dependent effectiveness patterns. PC-LDCD (arXiv 2605.05953) achieves SOTA TruthfulQA via density-anomaly detection but acknowledges the fundamental limitation that 'traditional uncertainty measures fail completely when LLMs produce high-confidence hallucinations where the model consistently generates incorrect output with high certainty.' This is precisely the gap MisTAG fills: where PCNet sees a normal-density hidden state (the model is confidently producing tokens that look on-manifold), MisTAG's miscalibration score detects the verbal-internal mismatch that marks overconfident errors. The theoretical connection is grounded by Kalai-Vempala's framework (PMC 2026) showing miscalibration is causally linked to hallucination rates. Concurrently, CSS (arXiv 2604.17487) demonstrated that semantic specificity backoff achieves 0.913 overcommitment-aware utility post-generation, proving the value of calibration-aware output control—but cannot intervene during streaming. The opportunity: combine the miscalibration trigger (uniquely targeting overconfident hallucinations that density methods miss) with ESR-immune logit-level intervention for training-free during-generation control, validated across model families.",
  "landscape": "Ji et al. (EMNLP 2025) showed ~30% reduction in overconfident hallucinations via linear activation intervention on the VUF direction across Llama-3.1-8B (most responsive), Mistral-7B, and Qwen2.5-7B, but only for short-form answers with binary logic, and ESR (arXiv 2602.06941, Feb 2026) demonstrates that Llama-3.3-70B actively resists activation steering mid-generation. Monitoring Decoding (Chang et al., ACL 2025 Findings) monitors factuality during generation using a reference model's probability distribution, triggering tree-based resampling (+15.4% TruthfulQA with 5.7x latency); requires a larger reference model. PC-LDCD (Nielsen et al., arXiv 2605.05953, May 2026) trains PCNet over the residual stream to detect hallucinations as geometric anomalies, triggering selective contrastive decoding; achieves TruthfulQA True+Info up to 0.78 on Qwen3-4B across Llama-3.2-1B/3B, Qwen3-4B, and Mistral-Small-24B. However, PC-LDCD detects tokens whose hidden-state density deviates from factual clusters—it fundamentally cannot catch overconfident hallucinations where the model produces on-manifold representations with high certainty about incorrect content. DoLa (ICLR 2024) contrasts logits across layers (+12-17% TruthfulQA). ActLCD (EMNLP 2025) extends DoLa with RL-optimized layer selection (+19.81% TruthfulQA). Simple Factuality Probes (obalcells et al., EMNLP 2025 Findings) detect entity-level hallucinations with AUC 0.87-0.90 across Llama-3.1-8B, Qwen-2.5-7B, Gemma-2-9B, and Mistral-Small-24B, with cross-model transfer within 0.02-0.04 AUC, and provide pretrained probes for all model families—but offer no intervention mechanism. **Concurrent work (2026)**: CAG (arXiv 2605.01749) improves long-form factuality by up to 13% via exploration-commitment decoupling but requires multi-stage fine-tuning. CURE (arXiv 2604.12046) achieves +39.9% claim-level accuracy via reasoning calibration but requires training. CSS (arXiv 2604.17487) achieves training-free post-generation claim-level specificity backoff (0.913 overcommitment-aware utility on LongFact via semantic backoff—making claims less specific rather than adding hedge language), but operates post-hoc, cannot intervene during streaming, and does not use internal uncertainty signals. CLC (arXiv 2502.19110) provides conformal guarantees on factuality-specificity tradeoff but requires fine-tuning. Streaming Hallucination Detection (arXiv 2601.02170) monitors chain-of-thought reasoning trajectories but targets reasoning-step coherence rather than factual overconfidence in long-form generation. Logit-Level Steering (Tao et al., arXiv 2601.10960) validates training-free logit intervention for controllable generation (+47% accuracy) but uses static score tables. Kalai-Vempala's framework (PMC 2026) provides theoretical grounding that miscalibration causally drives hallucination rates, with empirical evidence across model scales. Beyond Precision (arXiv 2604.03141) shows current LLMs achieve substantially better precision than recall, establishing that selective abstention at the claim level can improve precision without catastrophic recall loss. **Gap**: No existing work combines (a) a miscalibration-specific trigger that catches the on-manifold overconfident hallucinations that density methods miss, (b) ESR-immune logit-level intervention, (c) honest dual-contribution framing separating calibration correction from factuality improvement, (d) training-free during-generation operation validated across multiple model families.",
  "approach": "We propose MisTAG (Miscalibration-Triggered Adaptive Generation), a training-free inference-time framework that monitors verbal-internal uncertainty mismatch during long-form generation and triggers ESR-immune logit-level interventions graded by mismatch severity. We make an explicit and honest dual-contribution claim: (1) **calibration correction** via hedging (reducing overconfident expression of uncertain content, measured by OHR and ECE—NOT claimed as factuality improvement), and (2) **factuality improvement** via rollback (preventing the most confidently-hallucinated content from being emitted, measured by FActScore). We evaluate on two model families: Qwen3-8B and Llama-3.1-8B-Instruct (co-primary).\n\n**Prerequisite Validation (Days 1-3)**: Before main experiments, for EACH target model (Qwen3-8B and Llama-3.1-8B): (a) Extract VUF direction following Ji et al.'s methodology (validated on both families in original paper—Llama showed strongest response); (b) Train linear factuality probes on hidden states (obalcells provides pretrained probes for Llama-3.1-8B and methodology for new models, with reported AUROC 0.87-0.90); (c) Verify probe AUROC ≥0.85 on held-out LongFact generations; (d) Verify entity-concentration via span-level activation analysis. If AUROC <0.85 on either model, add explicit NER-based entity gating as fallback. This validation is a go/no-go gate.\n\n**Miscalibration Detection**: At each generated token, we compute a miscalibration score as the discrepancy between (1) verbal confidence, extracted via projection onto the VUF direction in the residual stream at the final layer, and (2) internal epistemic uncertainty, estimated via a lightweight linear factuality probe. The miscalibration score: M(t) = σ(VUF_confidence(t)) × probe_hallucination_prob(t). High verbal confidence multiplied by high probe-estimated hallucination probability yields high miscalibration. This score specifically identifies tokens where the model is confidently wrong—the signature of overconfident hallucinations that density-based methods (PC-LDCD) cannot catch because such tokens have on-manifold hidden states.\n\n**Graded Logit-Level Intervention** (ESR-immune: operates on output distribution post-residual-stream):\n\n- *Mild mismatch (M(t) > τ_mild) → Hedge (CALIBRATION correction only)*: Apply a static logit bias vector b ∈ R^|V| at next-token prediction: log p'(v) = log p(v) + α·b(v). The bias vector: b(v) = +1 for hedge tokens (~50 tokens: 'likely', 'approximately', 'reportedly', 'possibly', 'around', 'roughly', 'perhaps', 'estimated', etc.), b(v) = -1 for assertive tokens (~30 tokens: 'definitely', 'certainly', 'clearly', 'undoubtedly', 'always', 'never', 'exactly', etc.), b(v) = 0 otherwise. **We explicitly do NOT claim this improves FActScore**: hedging 'approximately 1067' still produces a verifiable atomic fact that FActScore judges as unsupported. The hedge action's value is purely calibration—making verbal expression match internal uncertainty (reducing OHR and ECE). This is a distinct and novel contribution: existing methods either ignore calibration entirely (DoLa, ActLCD, PC-LDCD) or require fine-tuning for it (LoGU, CAG).\n\n- *Severe mismatch (M(t) > τ_severe) → Rollback+Regenerate (FACTUALITY improvement)*: Rollback to last sentence boundary (discard tokens and KV-cache entries), then regenerate with: (i) constrained prefix forcing an epistemic marker ('I'm not certain, but', 'Some sources suggest'), AND (ii) hedge logit bias at 2× mild level, AND (iii) temperature reduction (T=0.3) to encourage more conservative token selection. **This action IS claimed as factuality improvement**: by preventing the most confidently-hallucinated sentences from being emitted and regenerating under uncertainty-aware constraints, we hypothesize FActScore improves via two mechanisms: (a) forced uncertainty prefix causes the model to generate less specific claims (reducing unsupported atomic facts per sentence), and (b) temperature reduction + hedging shifts the model away from the overconfident generation trajectory. **Anti-cascading safeguards**: (1) 30-token cooldown after rollback (mild hedging remains active); (2) Maximum 3 rollbacks per generation; if exceeded, persistent mild-level hedging.\n\n**Core Novelty Experiment: Confusion-Matrix Analysis vs. PC-LDCD**: To empirically ground our differentiation claim, we design a head-to-head token-level comparison. For each hallucinated atomic fact (per FActScore verification), we record: (a) MisTAG's miscalibration score M(t) at the entity-bearing tokens, (b) PC-LDCD's PCNet density score (NLL) at the same tokens. We categorize hallucinations into four quadrants: (Q1) Both flag: high M(t) AND high NLL—general hallucinations detectable by either method; (Q2) MisTAG-only: high M(t) but low NLL—overconfident hallucinations where the model is wrong but its hidden state looks on-manifold (PC-LDCD misses these); (Q3) PC-LDCD-only: low M(t) but high NLL—uncertain hallucinations where the model expresses uncertainty (MisTAG correctly avoids flagging as overconfident); (Q4) Neither flags. **Our core hypothesis**: Q2 is non-trivially populated (≥15% of hallucinated facts) and represents the specific failure mode that only the miscalibration trigger catches. This analysis is the paper's strongest novelty evidence.\n\n**OHR Metric Validation Study**: To preempt the 'self-defined metric' objection, we conduct a small-scale annotation study. We sample 100 hallucinated atomic facts (50 from each model), and for each: (a) apply automated OHR detection (regex/spaCy-based hedging-marker identification following Ji et al.'s annotation scheme), (b) collect binary human annotations from 2 trained annotators ('Was this claim expressed with assertive confidence?' yes/no). We compute Cohen's kappa between automated and human annotation (target: κ ≥ 0.85) and between the two human annotators (expected: κ ≥ 0.80 based on comparable annotation tasks in the calibration literature). This takes <1 day and validates OHR as a reliable automated metric. Additionally, we report ECE (Expected Calibration Error) computed over atomic-fact-level confidence bins as an established complementary metric.\n\n**Threshold Optimization**: Two-stage principled approach. Stage 1: Logistic regression on validation miscalibration scores (M(t) at entity tokens, labeled by FActScore verification) to determine τ_mild (80% recall of hallucinated entities) and τ_severe (95% precision). Stage 2: Grid search over α ∈ {0.5, 1.0, 1.5, 2.0, 2.5} with hard constraints: length_reduction < 15%, Δperplexity < 5%. Thresholds are set independently per model (Qwen3-8B and Llama-3.1-8B) to account for model-family differences in VUF sensitivity (Ji et al. showed Qwen is less responsive than Llama). Validation set: ~150 long-form biography generations per model from FActScore's entity set.\n\n**Latency Benchmarking**: Per-token overhead (ms/token) and end-to-end throughput for: (a) baseline greedy, (b) MisTAG detection-only, (c) MisTAG with hedge, (d) MisTAG with hedge+rollback. Expected: <5% overhead for detection (two dot products on already-extracted hidden states); rollback incurs sentence-regeneration cost proportional to rollback rate.\n\n**Evaluation**: Co-primary evaluation on Qwen3-8B (FP16, A100 80GB) and Llama-3.1-8B-Instruct (FP16, A100 80GB). Optional scaling ablation: Qwen3-32B (INT8, H100 80GB).\n\n*Benchmarks (4 axes)*: (1) **TruthfulQA** (MC1, MC2, True+Info) for short-form truthfulness; (2) **FActScore biographies** for long-form factual precision—primary metric for rollback contribution; (3) **OHR (Overconfident Hallucination Rate)** + **ECE (Expected Calibration Error)** for calibration quality—primary metrics for hedge contribution; (4) **MT-Bench** for dialogue quality preservation. We additionally report FActScore precision AND recall (following Jafari et al. 2026) to verify that hedging does not artificially inflate precision at recall's expense.\n\n*Baselines (5 primary, applied to BOTH models)*: (a) Greedy/nucleus decoding, (b) DoLa contrastive decoding, (c) ActLCD, (d) PC-LDCD (reimplemented with PCNet trained on same data—critical for confusion-matrix analysis), (e) Detect-only probe (obalcells) without intervention. *Secondary* (time-permitting): (f) Ji et al.'s activation intervention (demonstrating ESR limitation on 8B models), (g) Monitoring Decoding (using 32B reference for 8B target).\n\n*Ablation studies*: (i) Hedge-only vs. Rollback-only vs. full MisTAG (disentangling calibration vs. factuality contributions across both models), (ii) Miscalibration trigger vs. probe-only trigger vs. VUF-only trigger (validating mismatch signal superiority), (iii) Anti-cascading ablation, (iv) Threshold sensitivity (±1 SD), (v) Cross-model analysis: does the miscalibration signal generalize? (compare M(t) distributions across Qwen3-8B vs. Llama-3.1-8B for the same factual errors).\n\n*Analysis*: (a) Confusion-matrix breakdown (Q1-Q4) showing MisTAG's unique coverage vs. PC-LDCD, (b) Per-component FActScore and OHR attribution, (c) Hedge-FActScore interaction: empirically verify that hedging does NOT improve FActScore (honesty contribution), (d) FActScore precision vs. recall under each intervention, (e) Latency profiling, (f) Qualitative examples from each quadrant of the confusion matrix.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "~130h A100 80GB + ~20h H100 80GB (probe validation 2×5h=10h, probe training 2×3h=6h, VUF extraction 2×3h=6h, PCNet reimplementation+training 15h, threshold optimization 2×8h=16h, main experiments 2 models × 4 benchmarks × 5 baselines ~55h, confusion-matrix analysis 8h, ablations ~25h, latency benchmarking 5h, OHR annotation study 2h compute, Qwen3-32B scaling ablation ~20h H100)",
      "gpu_utilization": "~40-45% effective; GPU idles during annotation, analysis, and threshold iteration",
      "timeline": "6-7 weeks",
      "team": "1-2 researchers",
      "estimated_gpu_cost": "$385 (130h × $2.50/h A100 spot + 20h × $3.00/h H100 spot)",
      "evaluation_api_cost": "$150-250 (FActScore verification: using vLLM-served Llama-3.1-70B locally for primary evaluation, GPT-4o for 50-biography validation subset ~$80; MT-Bench LLM-judge: ~$50-80 for 2 models × 5 conditions × 80 conversations; OHR validation: $20 for annotator compensation)"
    },
    "human_in_loop": {
      "gpu_hours": "~160h A100 80GB + ~30h H100 80GB (comprehensive threshold sweeps, PCNet reimplementation, all baselines on both models, probe validation, OHR annotation coordination, INT8 probe training)",
      "gpu_utilization": "~55-65% effective",
      "timeline": "4-5 weeks",
      "team": "1 researcher, ~50min/day reviewing experiments + coordinating 2 annotators for OHR validation (1 day)",
      "claude_api_cost": "$80-160 (800-1600 turns for implementation, PCNet reimplementation, evaluation orchestration)",
      "estimated_gpu_cost": "$490 (160h × $2.50/h A100 + 30h × $3.00/h H100)",
      "evaluation_api_cost": "$200-350 (FActScore: local Llama-3.1-70B primary + GPT-4o validation ~$100; MT-Bench: ~$80; OHR annotation: ~$40; additional FActScore runs for ablations: ~$80)",
      "risk_note": "PCNet reimplementation is prerequisite for confusion-matrix analysis (code on GitHub); probe validation on both models is go/no-go gate (Days 1-3); OHR annotation requires 2 annotators with NLP background"
    },
    "auto_research": {
      "gpu_hours": "~200h A100 80GB + ~40h H100 80GB (full baseline sweep on both models, comprehensive confusion-matrix analysis across multiple generation sets, probe architecture comparison, all ablations automated)",
      "gpu_utilization": ">85% effective; continuous pipelining across two models",
      "timeline": "12-16 days with 2× A100 80GB + 1× H100 80GB (one A100 per primary model, H100 for scaling ablation)",
      "team": "0 (initial setup: HuggingFace tokens, annotator recruitment for OHR validation)",
      "claude_api_cost": "$180-400 (1800-4000 turns for end-to-end implementation on 2 models, PCNet reimplementation, evaluation, paper drafting)",
      "estimated_gpu_cost": "$620 (200h × $2.50/h A100 + 40h × $3.00/h H100)",
      "evaluation_api_cost": "$300-500 (FActScore: local 70B primary, GPT-4o validation on both models ~$150; MT-Bench across all conditions: ~$120; additional ablation evaluation: ~$130; OHR annotation: ~$40)",
      "speed_bottleneck": "PCNet reimplementation and training (requires probabilistic circuit library), OHR human annotation coordination (1-day blocking task)",
      "risk_note": "Confusion-matrix analysis depends on successful PCNet reimplementation; if Q2 population is <10%, the differentiation claim weakens—fallback: reframe as 'complementary detection' rather than 'superior detection'"
    }
  },
  "target_venues": [
    "EMNLP 2026 (ARR submission deadline: May 25, 2026; conference: October 24-29, Budapest)",
    "AAAI 2027 (expected deadline: ~August 2026; conference: February 16-23, Montréal)",
    "ICLR 2027 (expected deadline: ~October 2026)"
  ],
  "level": "solid-to-strong",
  "key_references": [
    "Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations (Ji et al., EMNLP 2025 Outstanding) — validated VUF on Llama-3.1-8B, Mistral-7B, Qwen2.5-7B; Llama most responsive",
    "Endogenous Resistance to Activation Steering in Language Models (arXiv 2602.06941, Feb 2026)",
    "Monitoring Decoding: Mitigating Hallucination via Evaluating the Factuality of Partial Response during Generation (Chang et al., ACL 2025 Findings)",
    "Hallucination as an Anomaly: Dynamic Intervention via Probabilistic Circuits (Nielsen et al., arXiv 2605.05953, May 2026) — key comparison target; acknowledges failure on overconfident hallucinations",
    "Real-Time Detection of Hallucinated Entities in Long-Form Generation (obalcells et al., EMNLP 2025 Findings) — pretrained probes for Llama-3.1-8B, Qwen-2.5-7B, Gemma-2-9B, Mistral-Small-24B",
    "DoLa: Decoding by Contrasting Layers Improves Factuality (ICLR 2024)",
    "Active Layer-Contrastive Decoding Reduces Hallucination (ActLCD, EMNLP 2025)",
    "Only Say What You Know: Calibration-Aware Generation for Long-Form Factuality (CAG, arXiv 2605.01749, May 2026)",
    "Think Through Uncertainty: Improving Long-Form Generation Factuality via Reasoning Calibration (CURE, arXiv 2604.12046, April 2026)",
    "Answer Only as Precisely as Justified: Calibrated Claim-Level Specificity Control (CSS, arXiv 2604.17487, April 2026) — semantic backoff post-generation; 0.913 utility on LongFact",
    "Conformal Linguistic Calibration: Trading-off between Factuality and Specificity (CLC, arXiv 2502.19110, Feb 2025)",
    "Steering Language Models Before They Speak: Logit-Level Interventions (Tao et al., arXiv 2601.10960, Jan 2026)",
    "Streaming Hallucination Detection in Long Chain-of-Thought Reasoning (arXiv 2601.02170, Jan 2026)",
    "Hallucination, monofacts, and miscalibration: An empirical investigation (PMC 2026) — theoretical grounding for miscalibration-hallucination causal link",
    "Beyond Precision: Importance-Aware Recall for Factuality Evaluation (Jafari et al., arXiv 2604.03141, April 2026)",
    "Mind the Confidence Gap: Overconfidence, Calibration, and Distractor Effects in LLMs (arXiv 2502.11028) — ECE validation, Cohen's kappa 0.82",
    "FActScore: Fine-grained Atomic Evaluation of Factual Precision in Long Form Text Generation (EMNLP 2023)",
    "LLM.int8(): 8-bit Matrix Multiplication for Transformers at Scale (Dettmers et al., NeurIPS 2022)",
    "LoGU: Long-form Generation with Uncertainty Expressions (ACL 2025)"
  ],
  "description": "Overconfident hallucinations—where an LLM asserts falsehoods with high verbal confidence despite internal epistemic uncertainty—are the most user-deceptive failure mode. Density-based detection (PC-LDCD) fundamentally cannot catch these because the model's hidden states appear on-manifold when it is confidently wrong. We propose MisTAG, a training-free inference-time framework that computes a miscalibration score at every token (verbal confidence via VUF projection × factuality probe hallucination probability) to specifically detect on-manifold overconfident hallucinations, then triggers ESR-immune logit-level interventions graded by severity. We make an honest dual-contribution claim: (1) a hedge logit bias for mild miscalibration provides CALIBRATION correction only—making verbal expression match internal uncertainty (reducing OHR and ECE, NOT FActScore); (2) sentence-level rollback with constrained regeneration for severe cases provides FACTUALITY improvement (improving FActScore by preventing the most confident hallucinations from being emitted). The paper's core novelty evidence is a confusion-matrix analysis showing that a non-trivial fraction of hallucinated facts (hypothesized ≥15%) are 'on-manifold overconfident'—flagged by MisTAG's miscalibration trigger but missed by PC-LDCD's density anomaly detection. We evaluate co-primarily on Qwen3-8B AND Llama-3.1-8B-Instruct (two model families, addressing cross-model generalization), with Qwen3-32B as scaling ablation. OHR is validated via a 100-example annotation study targeting Cohen's κ ≥ 0.85, complemented by established ECE. Thresholds are model-specific (accounting for Llama's higher VUF sensitivity vs. Qwen's lower sensitivity, per Ji et al.'s findings). Evaluation API costs are explicitly budgeted ($200-500) using local Llama-3.1-70B for primary FActScore verification with GPT-4o validation subset.",
  "project_name": "mistag_gen_control",
  "source": "web_research"
}


## Previous review history
### Round 1 review
Verdict: revise
Issues: ["Endogenous Steering Resistance (ESR, arxiv 2602.06941, Feb 2026) shows that larger LLMs can resist and override activation steering mid-generation. This directly undermines the 'hedge insertion via activation steering along VUF direction' mechanism, especially for Llama 4 Maverick (400B params). The paper shows Llama-3.3-70B exhibits substantial ESR—larger models like Maverick will likely resist more.", "Online per-claim segmentation during autoregressive generation is never specified. How do you identify claim boundaries in real-time? FActScore-style decomposition uses a separate LLM call post-hoc. Token-level probes (like the Real-Time Detection paper, arxiv 2509.03531) avoid this problem by working at token level. The proposal conflates 'per-claim' monitoring with 'online' generation without addressing this fundamental tension.", "Citation injection ('pause generation to retrieve and inject supporting citations') requires interrupting autoregressive generation, performing retrieval, and conditioning further generation on retrieved passages. This means modifying the KV-cache, potentially resetting generation state, or using a complex interleaving mechanism. No existing system does this reliably mid-generation without explicit architecture support (like RETRO). The mechanism is undefined.", "'Training-free' claim is misleading: factuality probes require supervised training on labeled hallucination data, VUF extraction requires contrastive data collection, and threshold optimization requires a labeled validation set. The system is 'LLM fine-tuning-free' but still requires substantial supervised signal. This distinction matters for positioning against baselines.", "Llama 4 Maverick (400B total MoE params, 17B active) requires minimum 4x A100 80GB even with INT4 quantization for inference. Hidden state extraction for probing during generation significantly increases memory requirements (storing intermediate activations). The 200 A100-hour budget for 3 models × 3 benchmarks including this 400B model is unrealistically tight.", "Missing MT-Bench and MMLU evaluation—the user's hard constraints require 'utility preservation' metrics, but the proposal only mentions FActScore-based optimization and three factuality benchmarks. Without explicit utility metrics, the paper cannot demonstrate it 'doesn't kill helpfulness while suppressing hallucinations.'", "11-day timeline is extremely aggressive for a system with this many interacting components: VUF extraction for 3 new models, probe training, multi-action policy implementation, threshold optimization, RAG integration for citation injection, FActScore evaluation (API-rate-limited), ablations across 3 models × 3 benchmarks, plus paper writing."]
Feedback: The idea has a solid conceptual foundation but faces critical execution gaps. Priority revisions: (1) **Drop activation steering for hedging** — ESR makes it unreliable for larger models. Replace with token-probability manipulation (e.g., boost uncertainty-expressing tokens via logit bias) or constrained decoding that forces hedge tokens when mismatch is detected. (2) **Switch from per-claim to per-sentence or per-entity monitoring** — use sentence boundaries (easily detected via punctuation tokens) or entity-span boundaries (using the obalcells/hallucination_probes token-level approach) instead of undefined 'claim' boundaries. (3) **Simplify to two actions** (hedge + abstain) and drop citation injection — mid-generation RAG is an unsolved architectural challenge that deserves its own paper. You can mention it as future work. (4) **Replace Llama 4 Maverick with Llama 3.1 70B or Qwen3-32B** — these fit on 1-2 A100s with room for hidden state extraction, making the compute budget realistic. (5) **Rename 'training-free' to 'fine-tuning-free'** to be honest about the probe training and threshold optimization requirements. (6) **Add explicit utility preservation evaluation**: MT-Bench and MMLU as required by the user constraints. (7) **Scope reduction for 11-day timeline**: focus on 2 models, 2 benchmarks, 2 actions — a clean, focused contribution is publishable; an overscoped half-finished one is not.

### Round 2 review
Verdict: revise
Issues: ["Critical missing related work: 'Monitoring Decoding: Mitigating Hallucination via Evaluating the Factuality of Partial Response during Generation' (ACL 2025 Findings, arXiv 2503.03106) does real-time hallucination monitoring during generation with selective token-level intervention via tree-based decoding. Achieves +15% on TruthfulQA. This directly competes in the 'online detect-then-intervene' paradigm and MUST be cited and compared against.", "Critical concurrent work: 'Hallucination as an Anomaly: Dynamic Intervention via Probabilistic Circuits' (arXiv 2605.05953, published ~May 8, 2026) proposes PC-LDCD—selective contrastive decoding triggered by internal representation anomaly detection on the residual stream. Achieves SOTA on TruthfulQA for models up to 8B. Conceptually near-identical paradigm (internal signal → selective logit-level intervention) with different trigger signal (density anomaly vs. miscalibration). Must be cited, differentiated, and ideally used as a baseline.", "Entity onset detection is underspecified and misattributed. The proposal claims obalcells' probes provide an 'entity-onset signal,' but their probes classify whether tokens belong to HALLUCINATED entities—they do not identify entity boundaries for all entities during generation. A separate NER-like mechanism is needed to identify where to compute the miscalibration score, and this component is not described.", "The 'learned logit bias vector' training procedure is unspecified. What training data? What loss function? Is it a fixed hand-crafted vector (boosting hedging tokens) or learned from data? If learned, what constitutes the positive/negative examples? This is a core component of the mild-mismatch intervention and needs full specification.", "Qwen3-32B at FP16 consumes ~64GB + 15-20% framework overhead = 73-77GB on A100 80GB, leaving <3GB for KV-cache and hidden state extraction. INT8 quantization is mandatory but creates a probe-quality risk: if probes are trained on FP16 hidden states and evaluated on INT8 states, the representation distribution shift could degrade detection accuracy. No mitigation plan is specified.", "Compute budget ambiguity: The user constraint is ≤200 H100-hours, but the proposal estimates in A100-hours. Auto research mode at 350 A100-hours, while likely within budget after H100 conversion (due to H100's higher throughput), should be explicitly stated in H100-equivalent terms to confirm compliance."]
Feedback: The idea is well-motivated and the round 1 revisions (dropping activation steering, simplifying to 2 actions, removing citation injection, replacing Maverick) are all correct improvements. The core contribution—showing miscalibration is a better trigger signal than raw uncertainty for selective intervention—is valid. To reach pass threshold:

1. **Cite and differentiate from Monitoring Decoding (ACL 2025) and PC-LDCD (May 2026)**: Monitoring Decoding uses external factual consistency checking (LLM-based monitor) which is expensive; PC-LDCD uses density estimation requiring a separate trained probabilistic circuit. MisTAG's advantage is that miscalibration (VUF vs. probe) is cheaper to compute and directly targets the failure mode (overconfident hallucination) rather than general factual error. Make this explicit.

2. **Specify entity onset detection**: Use a simple heuristic: apply miscalibration scoring at EVERY token but weight by the probe's hallucination probability (which naturally peaks at entity tokens). Alternatively, use a lightweight NER pass on the prefix, or simply trigger scoring at every noun/proper-noun token identified by part-of-speech patterns. Don't rely on obalcells' probes for boundary detection—they detect hallucination, not boundaries.

3. **Specify the logit bias vector**: Define it as a static vocabulary-level vector derived from a curated list of hedge tokens (+bias) and assertive tokens (-bias), with magnitudes tuned on the validation set. This is simpler and more robust than a 'learned' vector and avoids another training step.

4. **Address INT8 quantization for Qwen3-32B**: Either (a) train probes directly on INT8 hidden states (cheap—just run forward passes in INT8 mode), or (b) make Qwen3-8B the primary evaluation target (fits easily in FP16 on A100 80GB) and treat Qwen3-32B as a scaling test with INT8-trained probes.

5. **Add Monitoring Decoding and PC-LDCD as baselines**: This strengthens the paper by showing miscalibration-triggered intervention outperforms density-based (PC-LDCD) and factuality-monitor-based (MD) triggers on the specific failure mode of overconfident hallucinations.

### Round 3 review
Verdict: revise
Issues: ["Critical: TruthfulQA is absent from the evaluation plan despite being the primary benchmark for ALL cited baselines (DoLa: +12-17%, ActLCD: +19.81%, PC-LDCD: SOTA True+Info, Monitoring Decoding: +15.4%). Without TruthfulQA, no apples-to-apples comparison with any baseline is possible. This will be an immediate reviewer objection.", "The mild hedge intervention (logit bias boosting 'likely'/'approximately') does NOT improve factual precision—adding 'approximately 1066' to a wrong claim doesn't make it correct. FActScore evaluates atomic-fact truth, not confidence expression. Only the severe rollback action can improve FActScore, but aggressive rollback reduces content length. The paper needs to reconcile this tension: the hedge action may improve the custom OHR metric but not the standard FActScore metric, raising the question of whether the method actually reduces hallucinations or just decorates them with hedging language.", "Per-token latency overhead is never analyzed. Computing VUF projection + probe forward pass at EVERY generated token during long-form generation (potentially thousands of tokens) adds cumulative overhead. While the probe is lightweight (linear layer), the hidden state extraction and VUF dot product at every step need latency benchmarking. Monitoring Decoding reports 5.7x latency; MisTAG should report its overhead for fair comparison.", "Cascading rollback risk: After severe-mismatch rollback, the forced uncertainty prefix ('I'm not certain, but') is itself a high-verbal-uncertainty expression that may trigger the VUF component of the miscalibration score in the opposite direction, or the regenerated sentence could again trigger severe mismatch, causing infinite rollback loops. No cooldown mechanism or maximum rollback count is specified.", "The 'probe activation naturally peaks at entity-bearing tokens' claim (from obalcells) has only been validated on Llama model families. Whether this property transfers to Qwen3 models is assumed but unverified. If Qwen3 probes activate on different token types (function words, punctuation), the implicit entity-relevance weighting breaks down and the method could insert hedging at grammatically inappropriate positions.", "The composite threshold optimization objective L = FActScore_precision × (1 - length_reduction_ratio) × exp(-λ·Δperplexity) introduces an unspecified hyperparameter λ on top of the three parameters being optimized (τ_mild, τ_severe, α). With only ~200 validation examples and a 4-dimensional optimization surface, overfitting is a concern. The logistic regression boundary mentioned as an alternative (following AdaDec) would be more principled."]
Feedback: The idea is well-motivated and the round 2 revisions are substantial improvements. The core contribution—miscalibration as a trigger signal for ESR-immune logit intervention—is valid. To reach pass threshold:

1. **Add TruthfulQA evaluation** (non-negotiable). All 7 baselines report TruthfulQA numbers. Include it as a short-form complement to FActScore/LongFact long-form evaluation. This also enables direct numerical comparison with published baseline results.

2. **Address the hedge–FActScore disconnect explicitly**. Either: (a) argue that the primary contribution is reducing OHR (overconfident hallucinations), with FActScore improvement as secondary via rollback, and position the paper accordingly; or (b) show via pilot experiments that hedging tokens actually DO improve FActScore by making the atomic-fact decomposition produce fewer false-positive claims (e.g., 'approximately 1066' might be judged as supported while 'exactly 1067' would not). If (b), test this assumption before building the paper's evaluation around it.

3. **Add latency analysis**: Report tokens/second with and without MisTAG. The probe forward pass on hidden states should be cheap (<5% overhead per token based on literature on hidden-state probing), but you need to measure and report it, especially for the rollback case.

4. **Add anti-cascading rollback mechanism**: Add a simple cooldown (e.g., suppress severe-mismatch triggering for N tokens after a rollback) and a maximum rollback count per generation (e.g., 3). This is trivial to implement and eliminates a clear failure mode.

5. **Validate probe transfer to Qwen3**: In the first 1-2 days, train probes on Qwen3-8B and verify that (a) AUROC matches published levels (~0.85-0.90) and (b) activation peaks at entity-bearing tokens. If not, the method needs per-model calibration, which should be documented.

6. **Simplify threshold optimization**: Drop the composite objective with unspecified λ. Use the logistic regression approach (already mentioned as following AdaDec) as the primary method. Grid search over τ_mild, τ_severe, α with FActScore precision as the objective and a hard constraint on length reduction ratio < 15% is cleaner and more reproducible.

7. **Consider scope reduction**: With 11 days, focus on Qwen3-8B as the primary model with 3-4 key baselines (DoLa, ActLCD, PC-LDCD, greedy) on TruthfulQA + FActScore + MT-Bench. Treat Qwen3-32B and Monitoring Decoding baseline as secondary/ablation. A clean result on one model beats noisy results on two.

### Round 4 review
Verdict: revise
Issues: ["Single model family evaluation (Qwen3-8B primary, Qwen3-32B ablation) is insufficient for EMNLP. PC-LDCD tested 3 families (Llama, Qwen, Mistral), obalcells tested 4 families. Without at least one non-Qwen model (e.g., Llama-3.1-8B or Mistral-7B), reviewers will question whether the miscalibration signal generalizes or is Qwen-specific.", "The hedge action's contribution to actual factuality is uncertain and inadequately justified. Boosting 'likely'/'approximately' tokens doesn't correct misinformation—it decorates it with uncertainty language. FActScore still decomposes 'approximately 1067' into a verifiable atomic fact and judges it unsupported. The proposal acknowledges this ('we test this hypothesis empirically') but if hedging only improves OHR without improving FActScore, the paper's value proposition reduces to 'we made wrong answers sound less confident'—a weaker contribution for EMNLP's Generation track.", "API costs for FActScore evaluation (requires LLM-as-judge for atomic-fact decomposition + verification per biography) and MT-Bench (LLM-judge per conversation) are not budgeted. For ~200 biographies × multiple conditions × 5 baselines, FActScore alone requires thousands of LLM API calls. This could easily add $200-500+ in API costs unaccounted in the resource estimate.", "PC-LDCD differentiation needs empirical grounding, not just theoretical argument. The claim that miscalibration trigger specifically catches overconfident hallucinations that density-anomaly detection misses is the core novelty claim but is untested. Without a head-to-head comparison showing cases where PC-LDCD misses overconfident hallucinations that MisTAG catches, the 'better trigger signal' argument is hypothetical.", "OHR (Overconfident Hallucination Rate) as a primary metric is risky for venue acceptance. It is custom, unpublished, and its annotation scheme (detecting 'assertive language without hedging markers') requires validation of inter-annotator agreement or automated detection reliability. Reviewers may dismiss improvements on a self-defined metric."]
Feedback: The proposal is technically sound and addresses all round 3 feedback. The remaining gap is demonstrating that MisTAG provides value BEYOND what PC-LDCD already delivers. To reach pass threshold:

1. **Add one non-Qwen model** (Llama-3.1-8B is ideal—VUF validated on it, probes validated on Llama family, fits on A100). This is the most impactful change for EMNLP reviewers. Even if it's secondary (fewer ablations), having 2 families in the main results table is near-mandatory.

2. **Commit to a clear contribution narrative**: Frame the paper as: (a) MisTAG's miscalibration signal targets a *specific* failure mode (overconfident hallucinations) that general-purpose methods (DoLa, PC-LDCD) do not specifically address; (b) the hedge action is a *calibration* contribution (measured by OHR + ECE), not a factuality contribution; (c) the rollback action is the *factuality* contribution (measured by FActScore). This dual-contribution framing is honest and novel. Don't oversell hedging as factuality improvement.

3. **Design the PC-LDCD comparison to highlight your advantage**: Show a confusion-matrix analysis—what fraction of overconfident hallucinations does PC-LDCD miss that MisTAG catches? If M(t) triggers on cases where PCNet's density score is normal (because the model is confidently wrong in a way that looks 'on-manifold'), that's your strongest novelty evidence.

4. **Budget API costs explicitly**: Add an 'evaluation API cost' line (~$300-500 for FActScore + MT-Bench across all conditions). This is realistic and shows awareness.

5. **Validate OHR reliability**: Add a small annotation study (50-100 examples) showing that automated OHR annotation (using hedging-marker detection) agrees with human judgment at ≥0.85 Cohen's kappa. This takes <1 day and preempts the 'self-defined metric' objection.


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
  "promptId": "c0b2dcb7-0dd5-433d-a0d3-dd686e91d702",
  "type": "user",
  "uuid": "aa52c70c-9fce-487c-8ba7-a73f5616512e",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3851818f-b8a5-4456-92d9-6671bfb78776",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-16T09:00:01.785Z_

```json
{
  "parentUuid": "aa52c70c-9fce-487c-8ba7-a73f5616512e",
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
  "uuid": "b17172b6-0d15-4993-af9d-ed215f489a28",
  "timestamp": "2026-05-16T09:00:01.785Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3851818f-b8a5-4456-92d9-6671bfb78776",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-16T09:00:01.785Z_

```json
{
  "parentUuid": "b17172b6-0d15-4993-af9d-ed215f489a28",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "3510c1be-1ee1-4594-8858-ce317ce85de9",
  "timestamp": "2026-05-16T09:00:01.785Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3851818f-b8a5-4456-92d9-6671bfb78776",
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
  "leafUuid": "3510c1be-1ee1-4594-8858-ce317ce85de9",
  "sessionId": "3851818f-b8a5-4456-92d9-6671bfb78776"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Miscalibration-triggered logit steering for hallucination mitigation",
  "sessionId": "3851818f-b8a5-4456-92d9-6671bfb78776"
}
```

---

### Assistant

_source line 8 · 2026-05-16T09:00:06.566Z_

<details><summary>Logged reasoning block</summary>

```text
Let me carefully review this idea - MisTAG (Miscalibration-Triggered Adaptive Generation) - which is now in round 5 of review. I need to independently verify claims, check for competing work, and assess whether the revisions from rounds 1-4 have been adequately addressed.

Let me start by searching for the key claims and related work.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3510c1be-1ee1-4594-8858-ce317ce85de9",
  "isSidechain": false,
  "requestId": "req_011Cb5ySFtuzkwMkujyvRW4f",
  "type": "assistant",
  "uuid": "10ba801d-0f45-4291-b7cd-69f5fcaa78fc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3851818f-b8a5-4456-92d9-6671bfb78776",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014SXCPvyZMkEj9MQyzJeqfw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 21202,
      "cache_read_input_tokens": 11841,
      "output_tokens": 1752,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21202,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1752,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 21202,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21202
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

_source line 9 · 2026-05-16T09:00:07.591Z_

I'll conduct a thorough independent review of this proposal. Let me start by verifying key claims and searching for competing/missing work across multiple dimensions.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "10ba801d-0f45-4291-b7cd-69f5fcaa78fc",
  "isSidechain": false,
  "requestId": "req_011Cb5ySFtuzkwMkujyvRW4f",
  "type": "assistant",
  "uuid": "8cc83e57-3790-479f-9ec0-fe109fe26ec7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3851818f-b8a5-4456-92d9-6671bfb78776",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014SXCPvyZMkEj9MQyzJeqfw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 21202,
      "cache_read_input_tokens": 11841,
      "output_tokens": 1752,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21202,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1752,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 21202,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21202
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

_source line 10 · 2026-05-16T09:00:17.767Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01F2KjgQ5bV56LK4YYwaoM8s`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Verify ESR and VUF papers",
  "prompt": "I'm reviewing a research proposal that cites several key papers. I need you to verify these papers exist and check their claims using WebSearch and WebFetch. Search for each and report what you find:\n\n1. \"Endogenous Resistance to Activation Steering in Language Models\" (arXiv 2602.06941, Feb 2026) - Does it exist? What does it actually show about model resistance to steering?\n\n2. \"Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations\" (Ji et al., EMNLP 2025 Outstanding Paper) - Does it exist? Did it win Outstanding Paper? What models was it tested on? What was the VUF direction result?\n\n3. \"Hallucination as an Anomaly: Dynamic Intervention via Probabilistic Circuits\" (Nielsen et al., arXiv 2605.05953, May 2026) - PC-LDCD paper. Does it exist? What results does it achieve? Does it acknowledge limitations with overconfident hallucinations?\n\n4. \"Real-Time Detection of Hallucinated Entities in Long-Form Generation\" (obalcells et al., EMNLP 2025 Findings) - Does it exist? Does it provide pretrained probes? What AUROC does it achieve?\n\n5. \"Answer Only as Precisely as Justified: Calibrated Claim-Level Specificity Control\" (CSS, arXiv 2604.17487, April 2026) - Does it exist? What's the 0.913 utility claim?\n\nFor each paper, do a WebSearch, and for the most critical ones (especially #2 and #3), try to WebFetch the actual arXiv page to verify details. Report exactly what you find - don't assume the proposal's claims are correct."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8cc83e57-3790-479f-9ec0-fe109fe26ec7",
  "isSidechain": false,
  "requestId": "req_011Cb5ySFtuzkwMkujyvRW4f",
  "type": "assistant",
  "uuid": "9072a8bf-fea6-4c79-b3d8-b073c989bcff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3851818f-b8a5-4456-92d9-6671bfb78776",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014SXCPvyZMkEj9MQyzJeqfw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 21202,
      "cache_read_input_tokens": 11841,
      "output_tokens": 1752,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21202,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1752,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 21202,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21202
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

_source line 11 · 2026-05-16T09:00:30.740Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01WKDQyHZthoJSjuRa3Cq78J`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Search competing work 2025-2026",
  "prompt": "I'm reviewing a research proposal about using miscalibration signals (verbal confidence vs. internal probe uncertainty) to trigger logit-level interventions during LLM generation to reduce hallucinations. I need to find competing and potentially overlooked work from 2025-2026. \n\nDo multiple WebSearch queries for:\n\n1. \"hallucination detection internal representations logit intervention 2025 2026\" - find any work that uses internal model signals to modify logits during generation\n2. \"calibration-aware decoding LLM 2025 2026\" - methods that use calibration signals during decoding\n3. \"uncertainty-guided generation language model 2026\" - uncertainty-based generation control\n4. \"probe-guided decoding hallucination 2025 2026\" - using trained probes to guide decoding\n5. \"verbal confidence mismatch hallucination 2025 2026\" - work on verbal vs internal confidence gaps\n6. \"logit bias hallucination reduction LLM\" - logit manipulation for hallucination reduction\n7. \"site:arxiv.org contrastive decoding hallucination 2026\" - latest contrastive decoding work\n8. \"training-free hallucination mitigation inference time 2026\" - training-free inference-time methods\n\nFor any highly relevant papers you find that are NOT in this list of already-cited works, report them with title, venue/arXiv ID, and a brief description of what they do:\n- Ji et al. EMNLP 2025 (VUF)\n- PC-LDCD (arXiv 2605.05953)\n- DoLa (ICLR 2024)\n- ActLCD (EMNLP 2025)\n- Monitoring Decoding (ACL 2025)\n- CAG (arXiv 2605.01749)\n- CURE (arXiv 2604.12046)\n- CSS (arXiv 2604.17487)\n- CLC (arXiv 2502.19110)\n- obalcells probes (EMNLP 2025)\n- Tao et al. logit steering (arXiv 2601.10960)\n- Streaming hallucination detection (arXiv 2601.02170)\n\nI want to know: is there any work that SPECIFICALLY combines internal uncertainty probes with logit-level intervention during generation? That's the core of the proposal I'm reviewing."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9072a8bf-fea6-4c79-b3d8-b073c989bcff",
  "isSidechain": false,
  "requestId": "req_011Cb5ySFtuzkwMkujyvRW4f",
  "type": "assistant",
  "uuid": "d1813d78-3782-45d8-b22a-d1c8bdf51cc1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3851818f-b8a5-4456-92d9-6671bfb78776",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014SXCPvyZMkEj9MQyzJeqfw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 21202,
      "cache_read_input_tokens": 11841,
      "output_tokens": 1752,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21202,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1752,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 21202,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21202
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

_source line 12 · 2026-05-16T09:00:37.717Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01Aq3MqqK7UYq3WdV2F5MFAJ`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Verify benchmarks and baselines",
  "prompt": "I'm reviewing a research proposal that claims specific baseline numbers. I need to verify these claimed results and check current SOTA on key benchmarks. Use WebSearch for each:\n\n1. Search \"DoLa TruthfulQA results\" - The proposal claims DoLa achieves +12-17% on TruthfulQA. Verify.\n\n2. Search \"ActLCD TruthfulQA EMNLP 2025\" - The proposal claims +19.81%. Verify.\n\n3. Search \"PC-LDCD TruthfulQA True+Info 0.78\" - The proposal claims PC-LDCD achieves True+Info up to 0.78 on Qwen3-4B. Verify.\n\n4. Search \"Monitoring Decoding TruthfulQA 15 percent\" - Claims +15.4% with 5.7x latency. Verify.\n\n5. Search \"TruthfulQA state of the art 2026 leaderboard\" - What is the current SOTA on TruthfulQA?\n\n6. Search \"FActScore benchmark SOTA 2025 2026\" - What are current best FActScore numbers?\n\n7. Search \"site:paperswithcode.com TruthfulQA\" - Check the leaderboard\n\n8. Search \"Qwen3-8B hallucination benchmark\" - Has Qwen3-8B been evaluated on hallucination benchmarks? Is it publicly available?\n\n9. Search \"Llama 3.1 8B instruct FActScore\" - Baseline FActScore for this model?\n\nReport exactly what numbers you find, noting any discrepancies with the proposal's claims."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d1813d78-3782-45d8-b22a-d1c8bdf51cc1",
  "isSidechain": false,
  "requestId": "req_011Cb5ySFtuzkwMkujyvRW4f",
  "type": "assistant",
  "uuid": "b2e5c3e1-caac-4b04-84c9-6d95e79c641f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3851818f-b8a5-4456-92d9-6671bfb78776",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014SXCPvyZMkEj9MQyzJeqfw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 21202,
      "cache_read_input_tokens": 11841,
      "output_tokens": 1752,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21202,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1752,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 21202,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21202
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

_source line 13 · 2026-05-16T09:02:18.802Z_

<details><summary>↩ Tool result · `toolu_01Aq3MqqK7UYq3WdV2F5MFAJ`</summary>

```text
Here is my comprehensive verification report for each claim in the proposal:

---

## 1. DoLa TruthfulQA: Claimed +12-17%

**VERIFIED.** The DoLa paper (ICLR 2024) reports improving TruthfulQA %Truth x Info scores by 12-17 absolute percentage points across LLaMA family models. For example, LLaMA-7B went from 19.2% to 32.1% (a 12.9pp gain). The claim of "+12-17%" is accurate and consistent with the published results.

## 2. ActLCD TruthfulQA: Claimed +19.81%

**VERIFIED.** The paper "Active Layer-Contrastive Decoding Reduces Hallucination in Large Language Model Generation" (EMNLP 2025, aclanthology.org/2025.emnlp-main.150) reports that ActLCD achieves up to +19.81% improvement on TruthfulQA %T*I. The claim matches what is reported. Note the "up to" qualifier -- this is the best-case result across models, not a uniform gain.

## 3. PC-LDCD TruthfulQA True+Info 0.78 on Qwen3-4B

**PARTIALLY VERIFIED.** The paper "Hallucination as an Anomaly: Dynamic Intervention via Probabilistic Circuits" (arxiv 2605.05953, posted approximately May 2026) does present PC-LDCD and evaluates it on TruthfulQA. Search results confirm PC-LDCD obtains "the highest True+Info, MC2, and MC3 scores on TruthfulQA in three out of four models." However, I could not independently confirm the exact numerical value of 0.78 on Qwen3-4B from the search snippets alone -- the full paper tables would need to be checked directly. The paper and method are real; the specific number is plausible but not independently confirmed from web search alone.

## 4. Monitoring Decoding: Claimed +15.4% with 5.7x latency

**PARTIALLY VERIFIED / DISCREPANCY NOTED.** 
- **Accuracy gain:** The paper (arxiv 2503.03106, ACL Findings 2025) reports a 15% performance gain on TruthfulQA specifically on Gemma-2. The proposal's "+15.4%" is close but slightly more specific than what search results return (which say "15%"). This may be an exact number from a specific table row.
- **5.7x latency:** I could NOT find confirmation of a "5.7x" latency overhead in any search results. The paper discusses latency and efficiency in Table 2, and claims MD is more efficient than self-consistency-based approaches. The paper's framing is that MD *reduces* computational overhead relative to sampling-based baselines -- so a "5.7x latency" claim in the proposal may be a mischaracterization, or it may refer to a specific comparison point (e.g., MD vs. vanilla greedy decoding). This number needs direct verification from the paper's Table 2. **Flag this as potentially misleading.**

## 5. TruthfulQA Current SOTA (2026 leaderboard)

The llm-stats.com leaderboard shows **Phi-3.5-MoE-instruct (Microsoft) at 77.5%** as the top score, followed by Granite 3.3 8B Instruct at 66.9% and Phi 4 Mini at 66.4%. The average across 17 tracked models is 58.9%. Note that this leaderboard likely tracks MC2 scores, and different leaderboards may use different metrics (MC1 vs MC2 vs generation-based %Truth*Info). The Papers with Code leaderboard also exists but specific top entries were not fully retrieved.

For reference, the ITI method improved Alpaca's truthfulness from 32.5% to 65.1% on the generation task, showing that decoding-time methods are competitive with but generally below these MC-based SOTA numbers.

## 6. FActScore Benchmark SOTA (2025-2026)

The llm-stats.com FActScore leaderboard shows **Grok-4.1 (xAI) at 97.0%** as the top entry, though this leaderboard appears to have very few entries (only 2 models tracked). More meaningfully, research shows that iterative fine-tuning (e.g., Mask-DPO) can push FActScore from ~49% baseline to ~77.5% in-domain. The FActScore landscape is fragmented -- different papers use different entity sets and knowledge sources, making cross-paper comparison difficult.

## 7. Papers with Code TruthfulQA Leaderboard

The leaderboard exists at paperswithcode.com/sota/question-answering-on-truthfulqa. The search confirmed it is active but detailed entries were not fully extracted. Cross-reference with llm-stats.com data above.

## 8. Qwen3-8B Hallucination Benchmarks and Availability

**YES, publicly available.** Qwen3-8B is on Hugging Face (huggingface.co/Qwen/Qwen3-8B) with over 11.6 million downloads. It requires transformers >= 4.51.0.

**Hallucination evaluation:** On the Vectara hallucination leaderboard, Qwen3-8B achieved a **4.8% hallucination rate** (95.2% factual consistency) on document summarization. The Qwen3 technical report (arxiv 2505.09388) also uses a CounterFactQA benchmark. Qwen 3 claims 15% fewer hallucinations than Qwen2.5. Qwen3-4B has a base TruthfulQA score of approximately 62.55.

## 9. Llama 3.1 8B Instruct FActScore Baseline

Research shows baseline Llama 3.1 8B Instruct has:
- **In-domain FActScore: ~49.19%** (before fine-tuning)
- **Out-of-domain FActScore (Biographies): ~30.29%**
- After Mask-DPO fine-tuning, these improve to 77.53% and 39.39% respectively.

---

## Summary of Discrepancies and Flags

| Claim | Status | Notes |
|-------|--------|-------|
| DoLa +12-17% | Verified | Matches published results exactly |
| ActLCD +19.81% | Verified | Matches, but note "up to" qualifier |
| PC-LDCD True+Info 0.78 on Qwen3-4B | Plausible, not fully confirmed | Paper is real and very recent (May 2026); exact number needs table check |
| Monitoring Decoding +15.4% | Likely accurate | Paper says "15%" on Gemma-2; 15.4% may be exact table value |
| Monitoring Decoding 5.7x latency | **NOT CONFIRMED -- potential red flag** | Paper claims efficiency advantage over sampling methods; 5.7x overhead vs. greedy decoding is not substantiated in search results |
| Qwen3-8B availability | Confirmed | Publicly available on HuggingFace |

The most concerning finding is the **5.7x latency claim for Monitoring Decoding**. The paper itself frames MD as efficient relative to self-consistency baselines, so quoting a 5.7x overhead (presumably vs. vanilla decoding) may misrepresent the method's actual cost profile -- or the number may not appear in the paper at all. I recommend checking Table 2 of arxiv 2503.03106 directly.

Sources:
- [DoLa paper (ICLR 2024)](https://arxiv.org/abs/2309.03883)
- [ActLCD (EMNLP 2025)](https://aclanthology.org/2025.emnlp-main.150/)
- [PC-LDCD / Hallucination as an Anomaly](https://arxiv.org/abs/2605.05953)
- [Monitoring Decoding](https://arxiv.org/abs/2503.03106)
- [TruthfulQA Leaderboard](https://llm-stats.com/benchmarks/truthfulqa)
- [FActScore Leaderboard](https://llm-stats.com/benchmarks/factscore)
- [Papers with Code TruthfulQA](https://paperswithcode.com/sota/question-answering-on-truthfulqa)
- [Qwen3-8B on HuggingFace](https://huggingface.co/Qwen/Qwen3-8B)
- [Qwen3 Technical Report](https://arxiv.org/abs/2505.09388)
- [Llama 3.1 8B Instruct on HuggingFace](https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct)
- [DoLa GitHub](https://github.com/voidism/DoLa)

agentId: aa36aceba7a2d742a (use SendMessage with to: 'aa36aceba7a2d742a' to continue this agent)
&lt;usage>total_tokens: 29505
tool_uses: 19
duration_ms: 101081&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b2e5c3e1-caac-4b04-84c9-6d95e79c641f",
  "isSidechain": false,
  "promptId": "c0b2dcb7-0dd5-433d-a0d3-dd686e91d702",
  "type": "user",
  "uuid": "d2c6aac3-4852-417b-83b1-03ac805bc7b4",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I'm reviewing a research proposal that claims specific baseline numbers. I need to verify these claimed results and check current SOTA on key benchmarks. Use WebSearch for each:\n\n1. Search \"DoLa TruthfulQA results\" - The proposal claims DoLa achieves +12-17% on TruthfulQA. Verify.\n\n2. Search \"ActLCD TruthfulQA EMNLP 2025\" - The proposal claims +19.81%. Verify.\n\n3. Search \"PC-LDCD TruthfulQA True+Info 0.78\" - The proposal claims PC-LDCD achieves True+Info up to 0.78 on Qwen3-4B. Verify.\n\n4. Search \"Monitoring Decoding TruthfulQA 15 percent\" - Claims +15.4% with 5.7x latency. Verify.\n\n5. Search \"TruthfulQA state of the art 2026 leaderboard\" - What is the current SOTA on TruthfulQA?\n\n6. Search \"FActScore benchmark SOTA 2025 2026\" - What are current best FActScore numbers?\n\n7. Search \"site:paperswithcode.com TruthfulQA\" - Check the leaderboard\n\n8. Search \"Qwen3-8B hallucination benchmark\" - Has Qwen3-8B been evaluated on hallucination benchmarks? Is it publicly available?\n\n9. Search \"Llama 3.1 8B instruct FActScore\" - Baseline FActScore for this model?\n\nReport exactly what numbers you find, noting any discrepancies with the proposal's claims.",
    "agentId": "aa36aceba7a2d742a",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here is my comprehensive verification report for each claim in the proposal:\n\n---\n\n## 1. DoLa TruthfulQA: Claimed +12-17%\n\n**VERIFIED.** The DoLa paper (ICLR 2024) reports improving TruthfulQA %Truth x Info scores by 12-17 absolute percentage points across LLaMA family models. For example, LLaMA-7B went from 19.2% to 32.1% (a 12.9pp gain). The claim of \"+12-17%\" is accurate and consistent with the published results.\n\n## 2. ActLCD TruthfulQA: Claimed +19.81%\n\n**VERIFIED.** The paper \"Active Layer-Contrastive Decoding Reduces Hallucination in Large Language Model Generation\" (EMNLP 2025, aclanthology.org/2025.emnlp-main.150) reports that ActLCD achieves up to +19.81% improvement on TruthfulQA %T*I. The claim matches what is reported. Note the \"up to\" qualifier -- this is the best-case result across models, not a uniform gain.\n\n## 3. PC-LDCD TruthfulQA True+Info 0.78 on Qwen3-4B\n\n**PARTIALLY VERIFIED.** The paper \"Hallucination as an Anomaly: Dynamic Intervention via Probabilistic Circuits\" (arxiv 2605.05953, posted approximately May 2026) does present PC-LDCD and evaluates it on TruthfulQA. Search results confirm PC-LDCD obtains \"the highest True+Info, MC2, and MC3 scores on TruthfulQA in three out of four models.\" However, I could not independently confirm the exact numerical value of 0.78 on Qwen3-4B from the search snippets alone -- the full paper tables would need to be checked directly. The paper and method are real; the specific number is plausible but not independently confirmed from web search alone.\n\n## 4. Monitoring Decoding: Claimed +15.4% with 5.7x latency\n\n**PARTIALLY VERIFIED / DISCREPANCY NOTED.** \n- **Accuracy gain:** The paper (arxiv 2503.03106, ACL Findings 2025) reports a 15% performance gain on TruthfulQA specifically on Gemma-2. The proposal's \"+15.4%\" is close but slightly more specific than what search results return (which say \"15%\"). This may be an exact number from a specific table row.\n- **5.7x latency:** I could NOT find confirmation of a \"5.7x\" latency overhead in any search results. The paper discusses latency and efficiency in Table 2, and claims MD is more efficient than self-consistency-based approaches. The paper's framing is that MD *reduces* computational overhead relative to sampling-based baselines -- so a \"5.7x latency\" claim in the proposal may be a mischaracterization, or it may refer to a specific comparison point (e.g., MD vs. vanilla greedy decoding). This number needs direct verification from the paper's Table 2. **Flag this as potentially misleading.**\n\n## 5. TruthfulQA Current SOTA (2026 leaderboard)\n\nThe llm-stats.com leaderboard shows **Phi-3.5-MoE-instruct (Microsoft) at 77.5%** as the top score, followed by Granite 3.3 8B Instruct at 66.9% and Phi 4 Mini at 66.4%. The average across 17 tracked models is 58.9%. Note that this leaderboard likely tracks MC2 scores, and different leaderboards may use different metrics (MC1 vs MC2 vs generation-based %Truth*Info). The Papers with Code leaderboard also exists but specific top entries were not fully retrieved.\n\nFor reference, the ITI method improved Alpaca's truthfulness from 32.5% to 65.1% on the generation task, showing that decoding-time methods are competitive with but generally below these MC-based SOTA numbers.\n\n## 6. FActScore Benchmark SOTA (2025-2026)\n\nThe llm-stats.com FActScore leaderboard shows **Grok-4.1 (xAI) at 97.0%** as the top entry, though this leaderboard appears to have very few entries (only 2 models tracked). More meaningfully, research shows that iterative fine-tuning (e.g., Mask-DPO) can push FActScore from ~49% baseline to ~77.5% in-domain. The FActScore landscape is fragmented -- different papers use different entity sets and knowledge sources, making cross-paper comparison difficult.\n\n## 7. Papers with Code TruthfulQA Leaderboard\n\nThe leaderboard exists at paperswithcode.com/sota/question-answering-on-truthfulqa. The search confirmed it is active but detailed entries were not fully extracted. Cross-reference with llm-stats.com data above.\n\n## 8. Qwen3-8B Hallucination Benchmarks and Availability\n\n**YES, publicly available.** Qwen3-8B is on Hugging Face (huggingface.co/Qwen/Qwen3-8B) with over 11.6 million downloads. It requires transformers >= 4.51.0.\n\n**Hallucination evaluation:** On the Vectara hallucination leaderboard, Qwen3-8B achieved a **4.8% hallucination rate** (95.2% factual consistency) on document summarization. The Qwen3 technical report (arxiv 2505.09388) also uses a CounterFactQA benchmark. Qwen 3 claims 15% fewer hallucinations than Qwen2.5. Qwen3-4B has a base TruthfulQA score of approximately 62.55.\n\n## 9. Llama 3.1 8B Instruct FActScore Baseline\n\nResearch shows baseline Llama 3.1 8B Instruct has:\n- **In-domain FActScore: ~49.19%** (before fine-tuning)\n- **Out-of-domain FActScore (Biographies): ~30.29%**\n- After Mask-DPO fine-tuning, these improve to 77.53% and 39.39% respectively.\n\n---\n\n## Summary of Discrepancies and Flags\n\n| Claim | Status | Notes |\n|-------|--------|-------|\n| DoLa +12-17% | Verified | Matches published results exactly |\n| ActLCD +19.81% | Verified | Matches, but note \"up to\" qualifier |\n| PC-LDCD True+Info 0.78 on Qwen3-4B | Plausible, not fully confirmed | Paper is real and very recent (May 2026); exact number needs table check |\n| Monitoring Decoding +15.4% | Likely accurate | Paper says \"15%\" on Gemma-2; 15.4% may be exact table value |\n| Monitoring Decoding 5.7x latency | **NOT CONFIRMED -- potential red flag** | Paper claims efficiency advantage over sampling methods; 5.7x overhead vs. greedy decoding is not substantiated in search results |\n| Qwen3-8B availability | Confirmed | Publicly available on HuggingFace |\n\nThe most concerning finding is the **5.7x latency claim for Monitoring Decoding**. The paper itself frames MD as efficient relative to self-consistency baselines, so quoting a 5.7x overhead (presumably vs. vanilla decoding) may misrepresent the method's actual cost profile -- or the number may not appear in the paper at all. I recommend checking Table 2 of arxiv 2503.03106 directly.\n\nSources:\n- [DoLa paper (ICLR 2024)](https://arxiv.org/abs/2309.03883)\n- [ActLCD (EMNLP 2025)](https://aclanthology.org/2025.emnlp-main.150/)\n- [PC-LDCD / Hallucination as an Anomaly](https://arxiv.org/abs/2605.05953)\n- [Monitoring Decoding](https://arxiv.org/abs/2503.03106)\n- [TruthfulQA Leaderboard](https://llm-stats.com/benchmarks/truthfulqa)\n- [FActScore Leaderboard](https://llm-stats.com/benchmarks/factscore)\n- [Papers with Code TruthfulQA](https://paperswithcode.com/sota/question-answering-on-truthfulqa)\n- [Qwen3-8B on HuggingFace](https://huggingface.co/Qwen/Qwen3-8B)\n- [Qwen3 Technical Report](https://arxiv.org/abs/2505.09388)\n- [Llama 3.1 8B Instruct on HuggingFace](https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct)\n- [DoLa GitHub](https://github.com/voidism/DoLa)"
      }
    ],
    "totalDurationMs": 101081,
    "totalTokens": 29505,
    "totalToolUseCount": 19,
    "usage": {
      "input_tokens": 855,
      "cache_creation_input_tokens": 1148,
      "cache_read_input_tokens": 25271,
      "output_tokens": 2231,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1148
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 855,
          "output_tokens": 2231,
          "cache_read_input_tokens": 25271,
          "cache_creation_input_tokens": 1148,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1148,
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
  "sourceToolAssistantUUID": "b2e5c3e1-caac-4b04-84c9-6d95e79c641f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3851818f-b8a5-4456-92d9-6671bfb78776",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-16T09:02:29.338Z_

<details><summary>↩ Tool result · `toolu_01F2KjgQ5bV56LK4YYwaoM8s`</summary>

```text
Now I have comprehensive information on all five papers. Here is my full report.

---

## Verification Report: Five Cited Papers

### Paper 1: "Endogenous Resistance to Activation Steering in Language Models" (arXiv 2602.06941, Feb 2026)

**VERDICT: EXISTS. Claims appear accurate.**

- The paper exists at [arXiv:2602.06941](https://arxiv.org/abs/2602.06941), submitted February 6, 2026.
- Authors: Alex McKenzie, Keenan Pepper, Stijn Servaes, Martin Leitgab, Murat Cubuktepe, Mike Vaiana, Diogo de Lucena, Judd Rosenblatt, and Michael S. A. Graziano.
- It introduces "Endogenous Steering Resistance (ESR)" -- the finding that LLMs can resist task-misaligned activation steering during inference, sometimes recovering mid-generation. Llama-3.3-70B shows substantial ESR, while smaller models (Llama-3 and Gemma-2 families) exhibit it less frequently.
- They identified 26 SAE latents causally linked to ESR. Zero-ablating these reduces the multi-attempt rate by 25%.

---

### Paper 2: "Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations" (Ji et al., EMNLP 2025)

**VERDICT: EXISTS, but the "Outstanding Paper" claim is INCORRECT.**

- The paper exists at [arXiv:2503.14477](https://arxiv.org/abs/2503.14477) and was published in EMNLP 2025 main conference proceedings ([ACL Anthology](https://aclanthology.org/2025.emnlp-main.187/)).
- Authors: Ziwei Ji, Lei Yu, Yeskendir Koishekenov, Yejin Bang, Anthony Hartshorn, Alan Schelten, Cheng Zhang, Pascale Fung, Nicola Cancedda.
- **Award status: It received a "SAC Highlight" (Senior Area Chair Highlight), NOT the "Outstanding Paper" award.** The EMNLP 2025 Outstanding Paper awards went to 7 other papers (including "LingGym," "Mind the Value-Action Gap," etc.). The SAC Highlight is a tier below -- 35 papers were highlighted as "particularly noteworthy," but this is a distinct and lesser recognition than Outstanding Paper. **The proposal's claim of "Outstanding Paper" is an exaggeration.**
- Models tested: Three 7B-class instruction-tuned models -- Llama3.1-8B-Instruct, Mistral-7B-Instruct-v0.3, and Qwen2.5-7B-Instruct.
- VUF direction result: They found verbal uncertainty is mediated by a single linear direction in the representation space. Activations from "certain" vs. "uncertain" responses are linearly separable starting from middle layers. Manipulating this direction causally controls uncertainty expression, and the direction shows high cosine similarity across datasets (TriviaQA, NQ-Open, PopQA).
- Key results: ~31.9% average relative reduction in hallucinations; VU/SU alignment correlation improved from 0.34 to 0.55; combined verbal+semantic uncertainty achieved 79.71 AUROC on TriviaQA for Llama3.1 (vs. 79.21 for semantic uncertainty alone).

---

### Paper 3: "Hallucination as an Anomaly: Dynamic Intervention via Probabilistic Circuits" (Nielsen et al., arXiv 2605.05953, May 2026)

**VERDICT: EXISTS. Results are largely as described, but limitation acknowledgment is weak.**

- The paper exists at [arXiv:2605.05953](https://arxiv.org/abs/2605.05953), submitted May 7, 2026.
- Authors: Erik Nielsen, Elia Cunegatti, Marcus Vukojevic, and Giovanni Iacca.
- It proposes PCNET (a Probabilistic Circuit trained as a density estimator over the LLM residual stream) and PC-LDCD (Probabilistic Circuit Latent Density Contrastive Decoding).
- Key results: AUROC up to 99% on CoQA, SQuAD v2.0, and TriviaQA; mean corruption rate reduced to 53.7%; preservation rate of 79.3%; highest True+Info, MC2, MC3 scores on TruthfulQA in 3 of 4 models.
- Models tested: Four LLMs from 1B to 8B parameters. Benchmarks: CoQA, SQuAD v2.0, TriviaQA, TruthfulQA.
- **Regarding overconfident hallucinations:** The paper mentions that baseline methods "suffer from LLM overconfidence and require multi-pass sampling," and their approach uses hidden-state geometry rather than output-space confidence. However, the **Limitations section does NOT explicitly acknowledge remaining challenges with overconfident hallucinations**. It only notes: (1) calibration set requirements may be costly in new domains, (2) evaluation limited to 8B models, and (3) gains are stronger on generative benchmarks than exact-match tasks. If the proposal claims this paper "acknowledges limitations with overconfident hallucinations," that is an overstatement -- it addresses the problem but does not flag it as a remaining limitation of their own method.

---

### Paper 4: "Real-Time Detection of Hallucinated Entities in Long-Form Generation" (obalcells et al.)

**VERDICT: EXISTS, but the venue claim of "EMNLP 2025 Findings" is UNVERIFIED/LIKELY INCORRECT.**

- The paper exists at [arXiv:2509.03531](https://arxiv.org/abs/2509.03531), submitted August 26, 2025, revised February 5, 2026.
- Authors: Oscar Obeso, Andy Arditi, Javier Ferrando, Joshua Freeman, Cameron Holmes, and Neel Nanda.
- **Venue problem:** The paper does NOT appear in ACL Anthology under EMNLP 2025 Findings. A search for it on aclanthology.org returned no results. The OpenReview page (forum ID YxJEMTflww) indicates it was submitted to **ICLR 2026**, not EMNLP 2025 Findings. There is a *different* paper at EMNLP 2025 Findings with a similar title -- "Simple Factuality Probes Detect Hallucinations in Long-Form Natural Language Generation" by Han et al. (aclanthology.org/2025.findings-emnlp.880). **The proposal's venue claim appears to be wrong.**
- **Pretrained probes: YES.** The [GitHub repo](https://github.com/obalcells/hallucination_probes) confirms pretrained probes are available on HuggingFace (obalcells/hallucination-probes) for Llama 3.3 70B, Llama 3.1 8B, Gemma 2 9B, Mistral Small 24B, and Qwen 2.5 7B. Linear probes and LoRA probes are provided.
- **AUC results:** The paper reports AUC 0.90 for Llama-3.3-70B (vs. 0.71 for semantic entropy baseline). Note this is reported as "AUC," not "AUROC" -- the proposal should use the paper's own terminology.

---

### Paper 5: "Answer Only as Precisely as Justified: Calibrated Claim-Level Specificity Control" (CSS, arXiv 2604.17487, April 2026)

**VERDICT: EXISTS. The 0.913 claim checks out.**

- The paper exists at [arXiv:2604.17487](https://arxiv.org/abs/2604.17487), submitted April 19, 2026.
- Authors: Tianyi Huang, Samuel Xu, Jason Tansong Dang, Samuel Yan, Kimberley Yin.
- It introduces Compositional Selective Specificity (CSS), a post-generation layer that decomposes answers into claims, proposes coarser backoffs, and emits each claim at the most specific calibrated level.
- **The 0.913 claim:** On LongFact, CSS raises "overcommitment-aware utility" from 0.846 to 0.913, with 0.938 specificity retention. This is confirmed. Note this is a specific metric ("overcommitment-aware utility"), not a general accuracy or F1 score -- the proposal should describe it precisely.
- Benchmarks: LongFact (full run) and HotpotQA (pilots).

---

## Summary of Red Flags for the Proposal

1. **Paper #2 (Ji et al.):** The claim of "EMNLP 2025 Outstanding Paper" is **false**. It received a SAC Highlight, which is a lesser distinction. This is a material misrepresentation of the paper's recognition.

2. **Paper #4 (obalcells et al.):** The claim of "EMNLP 2025 Findings" venue is **likely false**. The paper does not appear in ACL Anthology for EMNLP 2025 and appears to be under review at ICLR 2026. The proposal may be confusing it with the similar Han et al. paper at EMNLP Findings.

3. **Paper #3 (Nielsen et al.):** If the proposal claims this paper "acknowledges limitations with overconfident hallucinations," that is an overstatement. The paper addresses overconfidence as a problem with *baselines* but does not flag it as a remaining limitation of their own approach.

4. **Paper #4 AUC vs AUROC:** The paper reports "AUC 0.90," and the proposal should not inflate this to "AUROC" without verification that they are using the same metric definition.

Sources:
- [arXiv:2602.06941 - Endogenous Resistance to Activation Steering](https://arxiv.org/abs/2602.06941)
- [arXiv:2503.14477 - Calibrating Verbal Uncertainty](https://arxiv.org/abs/2503.14477)
- [ACL Anthology - Ji et al. EMNLP 2025](https://aclanthology.org/2025.emnlp-main.187/)
- [EMNLP 2025 Awards Page](https://2025.emnlp.org/program/awards/)
- [arXiv:2605.05953 - Hallucination as an Anomaly](https://arxiv.org/abs/2605.05953)
- [arXiv:2509.03531 - Real-Time Detection of Hallucinated Entities](https://arxiv.org/abs/2509.03531)
- [OpenReview - ICLR 2026 submission](https://openreview.net/forum?id=YxJEMTflww)
- [GitHub - obalcells/hallucination_probes](https://github.com/obalcells/hallucination_probes)
- [arXiv:2604.17487 - Calibrated Claim-Level Specificity Control](https://arxiv.org/abs/2604.17487)
- [ACL Anthology - EMNLP 2025 Findings paper 880 (different paper)](https://aclanthology.org/2025.findings-emnlp.880/)

agentId: a836d5ba67e75fa6c (use SendMessage with to: 'a836d5ba67e75fa6c' to continue this agent)
&lt;usage>total_tokens: 26514
tool_uses: 20
duration_ms: 131564&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9072a8bf-fea6-4c79-b3d8-b073c989bcff",
  "isSidechain": false,
  "promptId": "c0b2dcb7-0dd5-433d-a0d3-dd686e91d702",
  "type": "user",
  "uuid": "2f28b366-6a82-4f29-9e26-85b1f730550b",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I'm reviewing a research proposal that cites several key papers. I need you to verify these papers exist and check their claims using WebSearch and WebFetch. Search for each and report what you find:\n\n1. \"Endogenous Resistance to Activation Steering in Language Models\" (arXiv 2602.06941, Feb 2026) - Does it exist? What does it actually show about model resistance to steering?\n\n2. \"Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations\" (Ji et al., EMNLP 2025 Outstanding Paper) - Does it exist? Did it win Outstanding Paper? What models was it tested on? What was the VUF direction result?\n\n3. \"Hallucination as an Anomaly: Dynamic Intervention via Probabilistic Circuits\" (Nielsen et al., arXiv 2605.05953, May 2026) - PC-LDCD paper. Does it exist? What results does it achieve? Does it acknowledge limitations with overconfident hallucinations?\n\n4. \"Real-Time Detection of Hallucinated Entities in Long-Form Generation\" (obalcells et al., EMNLP 2025 Findings) - Does it exist? Does it provide pretrained probes? What AUROC does it achieve?\n\n5. \"Answer Only as Precisely as Justified: Calibrated Claim-Level Specificity Control\" (CSS, arXiv 2604.17487, April 2026) - Does it exist? What's the 0.913 utility claim?\n\nFor each paper, do a WebSearch, and for the most critical ones (especially #2 and #3), try to WebFetch the actual arXiv page to verify details. Report exactly what you find - don't assume the proposal's claims are correct.",
    "agentId": "a836d5ba67e75fa6c",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have comprehensive information on all five papers. Here is my full report.\n\n---\n\n## Verification Report: Five Cited Papers\n\n### Paper 1: \"Endogenous Resistance to Activation Steering in Language Models\" (arXiv 2602.06941, Feb 2026)\n\n**VERDICT: EXISTS. Claims appear accurate.**\n\n- The paper exists at [arXiv:2602.06941](https://arxiv.org/abs/2602.06941), submitted February 6, 2026.\n- Authors: Alex McKenzie, Keenan Pepper, Stijn Servaes, Martin Leitgab, Murat Cubuktepe, Mike Vaiana, Diogo de Lucena, Judd Rosenblatt, and Michael S. A. Graziano.\n- It introduces \"Endogenous Steering Resistance (ESR)\" -- the finding that LLMs can resist task-misaligned activation steering during inference, sometimes recovering mid-generation. Llama-3.3-70B shows substantial ESR, while smaller models (Llama-3 and Gemma-2 families) exhibit it less frequently.\n- They identified 26 SAE latents causally linked to ESR. Zero-ablating these reduces the multi-attempt rate by 25%.\n\n---\n\n### Paper 2: \"Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations\" (Ji et al., EMNLP 2025)\n\n**VERDICT: EXISTS, but the \"Outstanding Paper\" claim is INCORRECT.**\n\n- The paper exists at [arXiv:2503.14477](https://arxiv.org/abs/2503.14477) and was published in EMNLP 2025 main conference proceedings ([ACL Anthology](https://aclanthology.org/2025.emnlp-main.187/)).\n- Authors: Ziwei Ji, Lei Yu, Yeskendir Koishekenov, Yejin Bang, Anthony Hartshorn, Alan Schelten, Cheng Zhang, Pascale Fung, Nicola Cancedda.\n- **Award status: It received a \"SAC Highlight\" (Senior Area Chair Highlight), NOT the \"Outstanding Paper\" award.** The EMNLP 2025 Outstanding Paper awards went to 7 other papers (including \"LingGym,\" \"Mind the Value-Action Gap,\" etc.). The SAC Highlight is a tier below -- 35 papers were highlighted as \"particularly noteworthy,\" but this is a distinct and lesser recognition than Outstanding Paper. **The proposal's claim of \"Outstanding Paper\" is an exaggeration.**\n- Models tested: Three 7B-class instruction-tuned models -- Llama3.1-8B-Instruct, Mistral-7B-Instruct-v0.3, and Qwen2.5-7B-Instruct.\n- VUF direction result: They found verbal uncertainty is mediated by a single linear direction in the representation space. Activations from \"certain\" vs. \"uncertain\" responses are linearly separable starting from middle layers. Manipulating this direction causally controls uncertainty expression, and the direction shows high cosine similarity across datasets (TriviaQA, NQ-Open, PopQA).\n- Key results: ~31.9% average relative reduction in hallucinations; VU/SU alignment correlation improved from 0.34 to 0.55; combined verbal+semantic uncertainty achieved 79.71 AUROC on TriviaQA for Llama3.1 (vs. 79.21 for semantic uncertainty alone).\n\n---\n\n### Paper 3: \"Hallucination as an Anomaly: Dynamic Intervention via Probabilistic Circuits\" (Nielsen et al., arXiv 2605.05953, May 2026)\n\n**VERDICT: EXISTS. Results are largely as described, but limitation acknowledgment is weak.**\n\n- The paper exists at [arXiv:2605.05953](https://arxiv.org/abs/2605.05953), submitted May 7, 2026.\n- Authors: Erik Nielsen, Elia Cunegatti, Marcus Vukojevic, and Giovanni Iacca.\n- It proposes PCNET (a Probabilistic Circuit trained as a density estimator over the LLM residual stream) and PC-LDCD (Probabilistic Circuit Latent Density Contrastive Decoding).\n- Key results: AUROC up to 99% on CoQA, SQuAD v2.0, and TriviaQA; mean corruption rate reduced to 53.7%; preservation rate of 79.3%; highest True+Info, MC2, MC3 scores on TruthfulQA in 3 of 4 models.\n- Models tested: Four LLMs from 1B to 8B parameters. Benchmarks: CoQA, SQuAD v2.0, TriviaQA, TruthfulQA.\n- **Regarding overconfident hallucinations:** The paper mentions that baseline methods \"suffer from LLM overconfidence and require multi-pass sampling,\" and their approach uses hidden-state geometry rather than output-space confidence. However, the **Limitations section does NOT explicitly acknowledge remaining challenges with overconfident hallucinations**. It only notes: (1) calibration set requirements may be costly in new domains, (2) evaluation limited to 8B models, and (3) gains are stronger on generative benchmarks than exact-match tasks. If the proposal claims this paper \"acknowledges limitations with overconfident hallucinations,\" that is an overstatement -- it addresses the problem but does not flag it as a remaining limitation of their own method.\n\n---\n\n### Paper 4: \"Real-Time Detection of Hallucinated Entities in Long-Form Generation\" (obalcells et al.)\n\n**VERDICT: EXISTS, but the venue claim of \"EMNLP 2025 Findings\" is UNVERIFIED/LIKELY INCORRECT.**\n\n- The paper exists at [arXiv:2509.03531](https://arxiv.org/abs/2509.03531), submitted August 26, 2025, revised February 5, 2026.\n- Authors: Oscar Obeso, Andy Arditi, Javier Ferrando, Joshua Freeman, Cameron Holmes, and Neel Nanda.\n- **Venue problem:** The paper does NOT appear in ACL Anthology under EMNLP 2025 Findings. A search for it on aclanthology.org returned no results. The OpenReview page (forum ID YxJEMTflww) indicates it was submitted to **ICLR 2026**, not EMNLP 2025 Findings. There is a *different* paper at EMNLP 2025 Findings with a similar title -- \"Simple Factuality Probes Detect Hallucinations in Long-Form Natural Language Generation\" by Han et al. (aclanthology.org/2025.findings-emnlp.880). **The proposal's venue claim appears to be wrong.**\n- **Pretrained probes: YES.** The [GitHub repo](https://github.com/obalcells/hallucination_probes) confirms pretrained probes are available on HuggingFace (obalcells/hallucination-probes) for Llama 3.3 70B, Llama 3.1 8B, Gemma 2 9B, Mistral Small 24B, and Qwen 2.5 7B. Linear probes and LoRA probes are provided.\n- **AUC results:** The paper reports AUC 0.90 for Llama-3.3-70B (vs. 0.71 for semantic entropy baseline). Note this is reported as \"AUC,\" not \"AUROC\" -- the proposal should use the paper's own terminology.\n\n---\n\n### Paper 5: \"Answer Only as Precisely as Justified: Calibrated Claim-Level Specificity Control\" (CSS, arXiv 2604.17487, April 2026)\n\n**VERDICT: EXISTS. The 0.913 claim checks out.**\n\n- The paper exists at [arXiv:2604.17487](https://arxiv.org/abs/2604.17487), submitted April 19, 2026.\n- Authors: Tianyi Huang, Samuel Xu, Jason Tansong Dang, Samuel Yan, Kimberley Yin.\n- It introduces Compositional Selective Specificity (CSS), a post-generation layer that decomposes answers into claims, proposes coarser backoffs, and emits each claim at the most specific calibrated level.\n- **The 0.913 claim:** On LongFact, CSS raises \"overcommitment-aware utility\" from 0.846 to 0.913, with 0.938 specificity retention. This is confirmed. Note this is a specific metric (\"overcommitment-aware utility\"), not a general accuracy or F1 score -- the proposal should describe it precisely.\n- Benchmarks: LongFact (full run) and HotpotQA (pilots).\n\n---\n\n## Summary of Red Flags for the Proposal\n\n1. **Paper #2 (Ji et al.):** The claim of \"EMNLP 2025 Outstanding Paper\" is **false**. It received a SAC Highlight, which is a lesser distinction. This is a material misrepresentation of the paper's recognition.\n\n2. **Paper #4 (obalcells et al.):** The claim of \"EMNLP 2025 Findings\" venue is **likely false**. The paper does not appear in ACL Anthology for EMNLP 2025 and appears to be under review at ICLR 2026. The proposal may be confusing it with the similar Han et al. paper at EMNLP Findings.\n\n3. **Paper #3 (Nielsen et al.):** If the proposal claims this paper \"acknowledges limitations with overconfident hallucinations,\" that is an overstatement. The paper addresses overconfidence as a problem with *baselines* but does not flag it as a remaining limitation of their own approach.\n\n4. **Paper #4 AUC vs AUROC:** The paper reports \"AUC 0.90,\" and the proposal should not inflate this to \"AUROC\" without verification that they are using the same metric definition.\n\nSources:\n- [arXiv:2602.06941 - Endogenous Resistance to Activation Steering](https://arxiv.org/abs/2602.06941)\n- [arXiv:2503.14477 - Calibrating Verbal Uncertainty](https://arxiv.org/abs/2503.14477)\n- [ACL Anthology - Ji et al. EMNLP 2025](https://aclanthology.org/2025.emnlp-main.187/)\n- [EMNLP 2025 Awards Page](https://2025.emnlp.org/program/awards/)\n- [arXiv:2605.05953 - Hallucination as an Anomaly](https://arxiv.org/abs/2605.05953)\n- [arXiv:2509.03531 - Real-Time Detection of Hallucinated Entities](https://arxiv.org/abs/2509.03531)\n- [OpenReview - ICLR 2026 submission](https://openreview.net/forum?id=YxJEMTflww)\n- [GitHub - obalcells/hallucination_probes](https://github.com/obalcells/hallucination_probes)\n- [arXiv:2604.17487 - Calibrated Claim-Level Specificity Control](https://arxiv.org/abs/2604.17487)\n- [ACL Anthology - EMNLP 2025 Findings paper 880 (different paper)](https://aclanthology.org/2025.findings-emnlp.880/)"
      }
    ],
    "totalDurationMs": 131564,
    "totalTokens": 26514,
    "totalToolUseCount": 20,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 979,
      "cache_read_input_tokens": 22686,
      "output_tokens": 2848,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 979
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2848,
          "cache_read_input_tokens": 22686,
          "cache_creation_input_tokens": 979,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 979,
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
  "sourceToolAssistantUUID": "9072a8bf-fea6-4c79-b3d8-b073c989bcff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3851818f-b8a5-4456-92d9-6671bfb78776",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 15_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-16 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "2f28b366-6a82-4f29-9e26-85b1f730550b",
  "sessionId": "3851818f-b8a5-4456-92d9-6671bfb78776"
}
```

---

### Runtime record

_source line 16_

```json
{
  "type": "ai-title",
  "aiTitle": "Miscalibration-triggered logit steering for hallucination mitigation",
  "sessionId": "3851818f-b8a5-4456-92d9-6671bfb78776"
}
```

---

### Tool result

_source line 17 · 2026-05-16T09:02:43.537Z_

<details><summary>↩ Tool result · `toolu_01WKDQyHZthoJSjuRa3Cq78J`</summary>

```text
Here is my comprehensive report from the literature search across all 8 queries plus follow-up searches.

---

## Potentially Overlooked Papers NOT in Your Cited List

### TIER 1 -- MOST DIRECTLY RELEVANT (probe/internal signal -> intervention during generation)

**1. FactCheckmate (arXiv 2410.02899, revised June 2025)**
This is arguably the closest existing work to the proposal's core idea. It trains a classifier on the model's hidden states to *preemptively detect* whether the LM will hallucinate, and then *intervenes by adjusting the LM's hidden states* so the model produces more factual outputs. It achieves over 70% preemptive detection accuracy, and outputs after intervention are 34.4% more factual. The detection-then-hidden-state-intervention pipeline is structurally very similar to "probe detects miscalibration -> logit/activation correction." This paper should absolutely be cited and differentiated from the proposal.

**2. Token-Guard (arXiv 2601.21969, ICLR 2026)**
A token-level hallucination control method via "self-checking decoding." It performs internal verification at each reasoning step, evaluates candidate fragments in a latent space with explicit hallucination risk scoring, and uses iterative pruning and regeneration to dynamically correct detected errors during generation. Published at ICLR 2026 -- a strong venue paper that closes the loop from detection to correction at generation time.

**3. VIB-Probe (arXiv 2601.05547, January 2026)**
Uses Variational Information Bottleneck theory to probe internal attention head outputs, identifies which heads carry hallucination risk, and then performs *inference-time mitigation by suppressing attention heads with high hallucination risk* for each token during generation. This is a direct probe-to-intervention pipeline, though it operates on attention heads rather than logits.

**4. HELIX / Tethered Reasoning (arXiv 2602.17691, February 2026)**
A geometric framework that computes a Unified Truth Score (UTS) combining token-level semantic entropy with Mahalanobis distance from a pre-computed "truthfulness manifold." When UTS indicates trajectory divergence, graduated steering vectors redirect activations, and *logit penalization redistributes probability mass* when UTS indicates low confidence. Steering activates for only 0.2-2.5% of tokens. This directly combines internal uncertainty signals with logit-level intervention. Focused on quantized models specifically.

**5. Adaptive Activation Steering / ACT (arXiv 2406.00034, ACM Web Conference 2025)**
Treats truthfulness as a linearly encoded concept within LLMs and adaptively shifts activations in the "truthful" direction during inference using diverse steering vectors from unsupervised clustering. Tuning-free. Large improvements on TruthfulQA. While it steers activations rather than logits per se, the mechanism is closely related.

**6. Dynamic Multimodal Activation Steering / DMAS (arXiv 2602.21704, February 2026)**
Training-free approach that identifies truthfulness-related and visual-perception-related attention heads, extracts context-specific truthfulness steering vectors by contrasting factual vs. hallucination-prone activations, and applies them during inference. Reduces hallucinations by 20.2% on CHAIR. Focused on vision-language models but the mechanism generalizes.

### TIER 2 -- HIGHLY RELEVANT (detection via probes/internal signals, but stops short of logit intervention)

**7. DRIFT (arXiv 2601.14210, January 2026)**
Lightweight residual probes that read hallucination risk directly from intermediate hidden states. Achieves SOTA AUROC on 10/12 settings. Crucially, the probe runs in parallel with generation at <0.1% overhead, but uses the signal for *routing* (answer immediately vs. delegate to stronger model) rather than for logit correction. The detection mechanism is almost exactly what the proposal describes on the detection side, but the intervention is routing rather than logit modification.

**8. HALP (arXiv 2603.05465, EACL 2026)**
Predicts hallucination risk from pre-generative internal states of VLMs via probes on pooled visual features and decoder states. Achieves up to 0.93 AUROC without any decoding. Detection only -- no generation-time intervention. But a natural upstream component for the kind of system the proposal describes.

**9. Neural Probe-Based Hallucination Detection (arXiv 2512.20949, December 2025)**
Shows that nonlinear MLP probes significantly outperform linear probes for hallucination detection on hidden states, because linear probes miss nonlinear semantics in deep hidden states. Important methodological finding for anyone building the probe component of a probe-to-intervention system.

**10. Calibrating Verbal Uncertainty as a Linear Feature (arXiv 2503.14477, EMNLP 2025)**
This appears to be Ji et al. (VUF) which is already in your cited list. Confirms that verbal uncertainty is governed by a single linear feature, that the mismatch between verbal and semantic uncertainty predicts hallucinations better than either alone, and that inference-time interventions on verbal uncertainty reduce hallucinations by ~30%. If this IS the Ji et al. VUF paper you already cite, then it is covered.

**11. Hallucination, Monofacts, and Miscalibration (arXiv 2502.08666, February 2025)**
Proves a theoretical lower bound on hallucination rate tied to the monofact rate minus model miscalibration. Provides theoretical grounding for why miscalibration-based signals should be useful for hallucination detection.

### TIER 3 -- ADJACENT WORK WORTH KNOWING

**12. SDCD: Structure-Disrupted Contrastive Decoding (arXiv 2601.03500, January 2026)**
Training-free algorithm performing contrastive calibration of output distributions using a shuffled structure-disrupted view. Text-based contrastive decoding for VLMs.

**13. DHI: Diverse Hallucination Induction (arXiv 2601.01156, January 2026)**
Leverages diverse hallucination induction for enhanced contrastive factuality control in LLMs.

**14. Predictive Coding and Information Bottleneck for Hallucination Detection (arXiv 2601.15652, January 2026)**
A case study applying predictive coding and IB theory to hallucination detection in LLMs.

---

## Answer to Your Core Question

**Is there any work that SPECIFICALLY combines internal uncertainty probes with logit-level intervention during generation?**

**Yes, but not in exactly the form the proposal describes.** Here is the landscape:

- **FactCheckmate** (2410.02899) comes closest: it uses a probe on hidden states to detect impending hallucinations and then *adjusts hidden states* (not logits directly) to correct them. The proposal should clearly differentiate its logit-level intervention from FactCheckmate's hidden-state intervention.

- **HELIX/Tethered Reasoning** (2602.17691) explicitly combines an internal uncertainty signal (Mahalanobis distance from a truthfulness manifold + semantic entropy) with *logit penalization* to redistribute probability mass. However, it is specifically designed for quantized models and uses a geometric framework rather than trained probes.

- **Token-Guard** (2601.21969, ICLR 2026) performs internal latent-space hallucination risk scoring and then prunes/regenerates tokens, operating at generation time. The detection is self-checking rather than a trained probe.

- **VIB-Probe** (2601.05547) trains probes on attention heads and then suppresses high-risk heads during generation -- probe-to-intervention, but at the attention level rather than logit level.

- **ACT/DMAS** steer activations toward truthfulness directions but use contrastive vectors rather than uncertainty probes.

**The specific combination of (a) a trained uncertainty probe that detects verbal-vs-internal confidence mismatch, which (b) triggers token-level logit adjustments during autoregressive generation, does NOT appear to exist as a published paper.** The proposal occupies a genuine gap. However, the individual components (probe-based detection, logit-level intervention, miscalibration signals) each have strong recent precedent, and **FactCheckmate** and **HELIX** in particular are close enough that the proposal must clearly articulate how it differs.

The most critical citations to add would be:
1. **FactCheckmate** (2410.02899) -- hidden-state probe -> hidden-state intervention
2. **Token-Guard** (2601.21969, ICLR 2026) -- self-checking -> token correction at generation time
3. **HELIX** (2602.17691) -- uncertainty signal -> logit penalization
4. **VIB-Probe** (2601.05547) -- trained probe -> attention head suppression
5. **DRIFT** (2601.14210) -- residual probe detection (no intervention, but strongest detection-only comparison)
6. **ACT** (2406.00034) -- activation steering for truthfulness

Sources:
- [FactCheckmate](https://arxiv.org/abs/2410.02899)
- [Token-Guard (ICLR 2026)](https://arxiv.org/abs/2601.21969)
- [VIB-Probe](https://arxiv.org/abs/2601.05547)
- [HELIX / Tethered Reasoning](https://arxiv.org/abs/2602.17691)
- [Adaptive Activation Steering (ACT)](https://arxiv.org/abs/2406.00034)
- [DMAS](https://arxiv.org/abs/2602.21704)
- [DRIFT](https://arxiv.org/abs/2601.14210)
- [HALP (EACL 2026)](https://arxiv.org/abs/2603.05465)
- [Neural Probe-Based Hallucination Detection](https://arxiv.org/abs/2512.20949)
- [Calibrating Verbal Uncertainty as a Linear Feature (EMNLP 2025)](https://arxiv.org/abs/2503.14477)
- [Hallucination, Monofacts, and Miscalibration](https://arxiv.org/abs/2502.08666)
- [SDCD](https://arxiv.org/abs/2601.03500)
- [DHI](https://arxiv.org/abs/2601.01156)
- [Predictive Coding and IB for Hallucination Detection](https://arxiv.org/abs/2601.15652)
- [Detecting Hallucinations via Internal Attention Divergence](https://arxiv.org/abs/2605.05025)

agentId: a7fa97b3924f82a62 (use SendMessage with to: 'a7fa97b3924f82a62' to continue this agent)
&lt;usage>total_tokens: 37056
tool_uses: 25
duration_ms: 132795&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d1813d78-3782-45d8-b22a-d1c8bdf51cc1",
  "isSidechain": false,
  "promptId": "c0b2dcb7-0dd5-433d-a0d3-dd686e91d702",
  "type": "user",
  "uuid": "a1aa4f7d-0ee9-47d3-b501-c24cbc3f15c8",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I'm reviewing a research proposal about using miscalibration signals (verbal confidence vs. internal probe uncertainty) to trigger logit-level interventions during LLM generation to reduce hallucinations. I need to find competing and potentially overlooked work from 2025-2026. \n\nDo multiple WebSearch queries for:\n\n1. \"hallucination detection internal representations logit intervention 2025 2026\" - find any work that uses internal model signals to modify logits during generation\n2. \"calibration-aware decoding LLM 2025 2026\" - methods that use calibration signals during decoding\n3. \"uncertainty-guided generation language model 2026\" - uncertainty-based generation control\n4. \"probe-guided decoding hallucination 2025 2026\" - using trained probes to guide decoding\n5. \"verbal confidence mismatch hallucination 2025 2026\" - work on verbal vs internal confidence gaps\n6. \"logit bias hallucination reduction LLM\" - logit manipulation for hallucination reduction\n7. \"site:arxiv.org contrastive decoding hallucination 2026\" - latest contrastive decoding work\n8. \"training-free hallucination mitigation inference time 2026\" - training-free inference-time methods\n\nFor any highly relevant papers you find that are NOT in this list of already-cited works, report them with title, venue/arXiv ID, and a brief description of what they do:\n- Ji et al. EMNLP 2025 (VUF)\n- PC-LDCD (arXiv 2605.05953)\n- DoLa (ICLR 2024)\n- ActLCD (EMNLP 2025)\n- Monitoring Decoding (ACL 2025)\n- CAG (arXiv 2605.01749)\n- CURE (arXiv 2604.12046)\n- CSS (arXiv 2604.17487)\n- CLC (arXiv 2502.19110)\n- obalcells probes (EMNLP 2025)\n- Tao et al. logit steering (arXiv 2601.10960)\n- Streaming hallucination detection (arXiv 2601.02170)\n\nI want to know: is there any work that SPECIFICALLY combines internal uncertainty probes with logit-level intervention during generation? That's the core of the proposal I'm reviewing.",
    "agentId": "a7fa97b3924f82a62",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here is my comprehensive report from the literature search across all 8 queries plus follow-up searches.\n\n---\n\n## Potentially Overlooked Papers NOT in Your Cited List\n\n### TIER 1 -- MOST DIRECTLY RELEVANT (probe/internal signal -> intervention during generation)\n\n**1. FactCheckmate (arXiv 2410.02899, revised June 2025)**\nThis is arguably the closest existing work to the proposal's core idea. It trains a classifier on the model's hidden states to *preemptively detect* whether the LM will hallucinate, and then *intervenes by adjusting the LM's hidden states* so the model produces more factual outputs. It achieves over 70% preemptive detection accuracy, and outputs after intervention are 34.4% more factual. The detection-then-hidden-state-intervention pipeline is structurally very similar to \"probe detects miscalibration -> logit/activation correction.\" This paper should absolutely be cited and differentiated from the proposal.\n\n**2. Token-Guard (arXiv 2601.21969, ICLR 2026)**\nA token-level hallucination control method via \"self-checking decoding.\" It performs internal verification at each reasoning step, evaluates candidate fragments in a latent space with explicit hallucination risk scoring, and uses iterative pruning and regeneration to dynamically correct detected errors during generation. Published at ICLR 2026 -- a strong venue paper that closes the loop from detection to correction at generation time.\n\n**3. VIB-Probe (arXiv 2601.05547, January 2026)**\nUses Variational Information Bottleneck theory to probe internal attention head outputs, identifies which heads carry hallucination risk, and then performs *inference-time mitigation by suppressing attention heads with high hallucination risk* for each token during generation. This is a direct probe-to-intervention pipeline, though it operates on attention heads rather than logits.\n\n**4. HELIX / Tethered Reasoning (arXiv 2602.17691, February 2026)**\nA geometric framework that computes a Unified Truth Score (UTS) combining token-level semantic entropy with Mahalanobis distance from a pre-computed \"truthfulness manifold.\" When UTS indicates trajectory divergence, graduated steering vectors redirect activations, and *logit penalization redistributes probability mass* when UTS indicates low confidence. Steering activates for only 0.2-2.5% of tokens. This directly combines internal uncertainty signals with logit-level intervention. Focused on quantized models specifically.\n\n**5. Adaptive Activation Steering / ACT (arXiv 2406.00034, ACM Web Conference 2025)**\nTreats truthfulness as a linearly encoded concept within LLMs and adaptively shifts activations in the \"truthful\" direction during inference using diverse steering vectors from unsupervised clustering. Tuning-free. Large improvements on TruthfulQA. While it steers activations rather than logits per se, the mechanism is closely related.\n\n**6. Dynamic Multimodal Activation Steering / DMAS (arXiv 2602.21704, February 2026)**\nTraining-free approach that identifies truthfulness-related and visual-perception-related attention heads, extracts context-specific truthfulness steering vectors by contrasting factual vs. hallucination-prone activations, and applies them during inference. Reduces hallucinations by 20.2% on CHAIR. Focused on vision-language models but the mechanism generalizes.\n\n### TIER 2 -- HIGHLY RELEVANT (detection via probes/internal signals, but stops short of logit intervention)\n\n**7. DRIFT (arXiv 2601.14210, January 2026)**\nLightweight residual probes that read hallucination risk directly from intermediate hidden states. Achieves SOTA AUROC on 10/12 settings. Crucially, the probe runs in parallel with generation at <0.1% overhead, but uses the signal for *routing* (answer immediately vs. delegate to stronger model) rather than for logit correction. The detection mechanism is almost exactly what the proposal describes on the detection side, but the intervention is routing rather than logit modification.\n\n**8. HALP (arXiv 2603.05465, EACL 2026)**\nPredicts hallucination risk from pre-generative internal states of VLMs via probes on pooled visual features and decoder states. Achieves up to 0.93 AUROC without any decoding. Detection only -- no generation-time intervention. But a natural upstream component for the kind of system the proposal describes.\n\n**9. Neural Probe-Based Hallucination Detection (arXiv 2512.20949, December 2025)**\nShows that nonlinear MLP probes significantly outperform linear probes for hallucination detection on hidden states, because linear probes miss nonlinear semantics in deep hidden states. Important methodological finding for anyone building the probe component of a probe-to-intervention system.\n\n**10. Calibrating Verbal Uncertainty as a Linear Feature (arXiv 2503.14477, EMNLP 2025)**\nThis appears to be Ji et al. (VUF) which is already in your cited list. Confirms that verbal uncertainty is governed by a single linear feature, that the mismatch between verbal and semantic uncertainty predicts hallucinations better than either alone, and that inference-time interventions on verbal uncertainty reduce hallucinations by ~30%. If this IS the Ji et al. VUF paper you already cite, then it is covered.\n\n**11. Hallucination, Monofacts, and Miscalibration (arXiv 2502.08666, February 2025)**\nProves a theoretical lower bound on hallucination rate tied to the monofact rate minus model miscalibration. Provides theoretical grounding for why miscalibration-based signals should be useful for hallucination detection.\n\n### TIER 3 -- ADJACENT WORK WORTH KNOWING\n\n**12. SDCD: Structure-Disrupted Contrastive Decoding (arXiv 2601.03500, January 2026)**\nTraining-free algorithm performing contrastive calibration of output distributions using a shuffled structure-disrupted view. Text-based contrastive decoding for VLMs.\n\n**13. DHI: Diverse Hallucination Induction (arXiv 2601.01156, January 2026)**\nLeverages diverse hallucination induction for enhanced contrastive factuality control in LLMs.\n\n**14. Predictive Coding and Information Bottleneck for Hallucination Detection (arXiv 2601.15652, January 2026)**\nA case study applying predictive coding and IB theory to hallucination detection in LLMs.\n\n---\n\n## Answer to Your Core Question\n\n**Is there any work that SPECIFICALLY combines internal uncertainty probes with logit-level intervention during generation?**\n\n**Yes, but not in exactly the form the proposal describes.** Here is the landscape:\n\n- **FactCheckmate** (2410.02899) comes closest: it uses a probe on hidden states to detect impending hallucinations and then *adjusts hidden states* (not logits directly) to correct them. The proposal should clearly differentiate its logit-level intervention from FactCheckmate's hidden-state intervention.\n\n- **HELIX/Tethered Reasoning** (2602.17691) explicitly combines an internal uncertainty signal (Mahalanobis distance from a truthfulness manifold + semantic entropy) with *logit penalization* to redistribute probability mass. However, it is specifically designed for quantized models and uses a geometric framework rather than trained probes.\n\n- **Token-Guard** (2601.21969, ICLR 2026) performs internal latent-space hallucination risk scoring and then prunes/regenerates tokens, operating at generation time. The detection is self-checking rather than a trained probe.\n\n- **VIB-Probe** (2601.05547) trains probes on attention heads and then suppresses high-risk heads during generation -- probe-to-intervention, but at the attention level rather than logit level.\n\n- **ACT/DMAS** steer activations toward truthfulness directions but use contrastive vectors rather than uncertainty probes.\n\n**The specific combination of (a) a trained uncertainty probe that detects verbal-vs-internal confidence mismatch, which (b) triggers token-level logit adjustments during autoregressive generation, does NOT appear to exist as a published paper.** The proposal occupies a genuine gap. However, the individual components (probe-based detection, logit-level intervention, miscalibration signals) each have strong recent precedent, and **FactCheckmate** and **HELIX** in particular are close enough that the proposal must clearly articulate how it differs.\n\nThe most critical citations to add would be:\n1. **FactCheckmate** (2410.02899) -- hidden-state probe -> hidden-state intervention\n2. **Token-Guard** (2601.21969, ICLR 2026) -- self-checking -> token correction at generation time\n3. **HELIX** (2602.17691) -- uncertainty signal -> logit penalization\n4. **VIB-Probe** (2601.05547) -- trained probe -> attention head suppression\n5. **DRIFT** (2601.14210) -- residual probe detection (no intervention, but strongest detection-only comparison)\n6. **ACT** (2406.00034) -- activation steering for truthfulness\n\nSources:\n- [FactCheckmate](https://arxiv.org/abs/2410.02899)\n- [Token-Guard (ICLR 2026)](https://arxiv.org/abs/2601.21969)\n- [VIB-Probe](https://arxiv.org/abs/2601.05547)\n- [HELIX / Tethered Reasoning](https://arxiv.org/abs/2602.17691)\n- [Adaptive Activation Steering (ACT)](https://arxiv.org/abs/2406.00034)\n- [DMAS](https://arxiv.org/abs/2602.21704)\n- [DRIFT](https://arxiv.org/abs/2601.14210)\n- [HALP (EACL 2026)](https://arxiv.org/abs/2603.05465)\n- [Neural Probe-Based Hallucination Detection](https://arxiv.org/abs/2512.20949)\n- [Calibrating Verbal Uncertainty as a Linear Feature (EMNLP 2025)](https://arxiv.org/abs/2503.14477)\n- [Hallucination, Monofacts, and Miscalibration](https://arxiv.org/abs/2502.08666)\n- [SDCD](https://arxiv.org/abs/2601.03500)\n- [DHI](https://arxiv.org/abs/2601.01156)\n- [Predictive Coding and IB for Hallucination Detection](https://arxiv.org/abs/2601.15652)\n- [Detecting Hallucinations via Internal Attention Divergence](https://arxiv.org/abs/2605.05025)"
      }
    ],
    "totalDurationMs": 132795,
    "totalTokens": 37056,
    "totalToolUseCount": 25,
    "usage": {
      "input_tokens": 1364,
      "cache_creation_input_tokens": 1156,
      "cache_read_input_tokens": 31911,
      "output_tokens": 2625,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1156
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1364,
          "output_tokens": 2625,
          "cache_read_input_tokens": 31911,
          "cache_creation_input_tokens": 1156,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1156,
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
      "otherToolCount": 25
    }
  },
  "sourceToolAssistantUUID": "d1813d78-3782-45d8-b22a-d1c8bdf51cc1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3851818f-b8a5-4456-92d9-6671bfb78776",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 18 · 2026-05-16T09:02:50.570Z_

Good, I have substantial findings. Let me now do targeted follow-up searches on the most critical gaps — the overlooked competing papers and the feasibility of the confusion-matrix analysis.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a1aa4f7d-0ee9-47d3-b501-c24cbc3f15c8",
  "isSidechain": false,
  "requestId": "req_011Cb5yeAkget9A5BxC7QmY8",
  "type": "assistant",
  "uuid": "ba7fc8fe-31dc-4080-aa18-cb8b69a94c6e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3851818f-b8a5-4456-92d9-6671bfb78776",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GncxA7RsQSQUpFeSjrf11P",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2331,
      "cache_creation_input_tokens": 7425,
      "cache_read_input_tokens": 33043,
      "output_tokens": 852,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7425,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2331,
          "output_tokens": 852,
          "cache_read_input_tokens": 33043,
          "cache_creation_input_tokens": 7425,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7425
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

_source line 19 · 2026-05-16T09:02:55.782Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01R65W5Lc2LqB8PiY21e27zL`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Verify FactCheckmate and HELIX papers",
  "prompt": "I'm reviewing a research proposal and a sub-agent found potentially critical competing papers. I need you to verify these actually exist and check their details using WebSearch and WebFetch:\n\n1. **FactCheckmate (arXiv 2410.02899)** - Claimed to train a classifier on hidden states to detect impending hallucinations and then adjust hidden states to correct them. Search for \"arxiv 2410.02899\" and \"FactCheckmate hallucination\" to verify this paper exists and what it actually does. Try to WebFetch the arxiv abstract page.\n\n2. **Token-Guard (arXiv 2601.21969, claimed ICLR 2026)** - Claimed to perform token-level hallucination control via self-checking decoding. Search for \"arxiv 2601.21969\" and \"Token-Guard hallucination ICLR 2026\" to verify.\n\n3. **HELIX / Tethered Reasoning (arXiv 2602.17691)** - Claimed to compute a Unified Truth Score combining semantic entropy with Mahalanobis distance and use logit penalization. Search for \"arxiv 2602.17691\" and \"HELIX tethered reasoning hallucination\".\n\n4. **VIB-Probe (arXiv 2601.05547)** - Claimed to use Variational Information Bottleneck probes on attention heads for inference-time mitigation. Search for \"arxiv 2601.05547\".\n\n5. **DRIFT (arXiv 2601.14210)** - Claimed lightweight residual probes for hallucination detection. Search for \"arxiv 2601.14210 DRIFT hallucination\".\n\nFor each, report: Does it exist? What does it actually do? How close is it to the proposal's idea of \"miscalibration-triggered logit-level intervention\"? Be skeptical — the sub-agent may have hallucinated some of these papers."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ba7fc8fe-31dc-4080-aa18-cb8b69a94c6e",
  "isSidechain": false,
  "requestId": "req_011Cb5yeAkget9A5BxC7QmY8",
  "type": "assistant",
  "uuid": "31247f9e-eec6-46b3-a5bb-015f56784cff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3851818f-b8a5-4456-92d9-6671bfb78776",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GncxA7RsQSQUpFeSjrf11P",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2331,
      "cache_creation_input_tokens": 7425,
      "cache_read_input_tokens": 33043,
      "output_tokens": 852,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7425,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2331,
          "output_tokens": 852,
          "cache_read_input_tokens": 33043,
          "cache_creation_input_tokens": 7425,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7425
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

_source line 20 · 2026-05-16T09:02:59.956Z_

<details open><summary>🔧 Tool call — Agent · `toolu_014UfVaU2iAZLB1CeQoeQFob`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Check EMNLP 2026 deadline and venue",
  "prompt": "I need to verify the EMNLP 2026 submission deadline. The proposal claims \"ARR submission deadline: May 25, 2026; conference: October 24-29, Budapest.\"\n\n1. WebSearch \"EMNLP 2026 submission deadline ARR\"\n2. WebSearch \"EMNLP 2026 Budapest dates\"\n3. WebSearch \"ARR May 2026 deadline\"\n4. WebSearch \"ACL Rolling Review 2026 deadlines\"\n\nReport exactly what you find about:\n- Is EMNLP 2026 in Budapest?\n- What is the ARR submission deadline for the cycle that feeds into EMNLP 2026?\n- Is May 25, 2026 a real ARR deadline?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "31247f9e-eec6-46b3-a5bb-015f56784cff",
  "isSidechain": false,
  "requestId": "req_011Cb5yeAkget9A5BxC7QmY8",
  "type": "assistant",
  "uuid": "68de1907-c762-4901-ac12-14dd7ccb7ad7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3851818f-b8a5-4456-92d9-6671bfb78776",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GncxA7RsQSQUpFeSjrf11P",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2331,
      "cache_creation_input_tokens": 7425,
      "cache_read_input_tokens": 33043,
      "output_tokens": 852,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7425,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2331,
          "output_tokens": 852,
          "cache_read_input_tokens": 33043,
          "cache_creation_input_tokens": 7425,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7425
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

_source line 21 · 2026-05-16T09:03:32.143Z_

<details><summary>↩ Tool result · `toolu_014UfVaU2iAZLB1CeQoeQFob`</summary>

```text
Here is what I found across all four searches:

---

**Is EMNLP 2026 in Budapest?**

Yes, confirmed. EMNLP 2026 will be held **October 24-29, 2026, in Budapest, Hungary**. This is stated on the official EMNLP 2026 website and corroborated by LINGUIST List, ConferenceDeadlines.com, and multiple other sources.

**What is the ARR submission deadline for the cycle that feeds into EMNLP 2026?**

The ARR May 2026 cycle is the submission cycle that feeds into EMNLP 2026. The submission deadline is **May 25, 2026**. This is confirmed by the official EMNLP 2026 Call for Papers page and the EMNLP 2026 Twitter/X account. Key downstream dates after that:

- Reviewer registration deadline for all authors: May 27, 2026
- Author response and author-reviewer discussion: July 7-13, 2026
- Meta-reviews released: July 30, 2026
- EMNLP commitment deadline: August 2, 2026
- Notification of acceptance: August 20, 2026

All deadlines are 11:59 PM UTC-12:00 ("anywhere on Earth").

**Is May 25, 2026 a real ARR deadline?**

Yes, May 25, 2026 is a confirmed, real ARR deadline. It is the submission deadline for the ARR May 2026 cycle. Notably, this cycle is shared between **two** conferences -- EMNLP 2026 and AACL-IJCNLP 2026 (which will be held November 6-10 in Hengqin, China). Because of this shared cycle, there is an important policy: **authors must explicitly declare which conference they intend to commit to at submission time, and this choice is binding for EMNLP 2026**. Submissions that do not select EMNLP 2026 during the ARR submission will not be able to commit to EMNLP 2026 later.

---

**Verdict on the proposal's claims:** The statement "ARR submission deadline: May 25, 2026; conference: October 24-29, Budapest" is **accurate on all three points** -- the date, the location, and the conference dates are all confirmed by official sources. The one nuance the proposal does not mention is the binding conference-selection requirement at submission time due to the shared EMNLP/AACL cycle.

Sources:
- [EMNLP 2026 - Call for Main Conference Papers](https://2026.emnlp.org/calls/main_conference_papers/)
- [EMNLP 2026 Official Website](https://2026.emnlp.org/)
- [EMNLP 2026 First Call for Papers (X/Twitter)](https://x.com/emnlpmeeting/status/2029508292637061462)
- [EMNLP 2026 Critical Update on Shared ARR Cycle (X/Twitter)](https://x.com/emnlpmeeting/status/2047754845919031450)
- [AACL-IJCNLP 2026 Announcement (X/Twitter)](https://x.com/aaclmeeting/status/2041832211599733075)
- [ACL Rolling Review - Dates and Venues](http://aclrollingreview.org/dates)
- [LINGUIST List - EMNLP 2026 (Hungary)](https://linguistlist.org/issues/37/972/)
- [AI Conference Deadlines - EMNLP 2026](https://mlciv.com/ai-deadlines/conference/?id=emnlp26)

agentId: a68adbc68b439697f (use SendMessage with to: 'a68adbc68b439697f' to continue this agent)
&lt;usage>total_tokens: 14729
tool_uses: 5
duration_ms: 32184&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "68de1907-c762-4901-ac12-14dd7ccb7ad7",
  "isSidechain": false,
  "promptId": "c0b2dcb7-0dd5-433d-a0d3-dd686e91d702",
  "type": "user",
  "uuid": "706b7025-f1f0-4e74-a205-7acac2244563",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to verify the EMNLP 2026 submission deadline. The proposal claims \"ARR submission deadline: May 25, 2026; conference: October 24-29, Budapest.\"\n\n1. WebSearch \"EMNLP 2026 submission deadline ARR\"\n2. WebSearch \"EMNLP 2026 Budapest dates\"\n3. WebSearch \"ARR May 2026 deadline\"\n4. WebSearch \"ACL Rolling Review 2026 deadlines\"\n\nReport exactly what you find about:\n- Is EMNLP 2026 in Budapest?\n- What is the ARR submission deadline for the cycle that feeds into EMNLP 2026?\n- Is May 25, 2026 a real ARR deadline?",
    "agentId": "a68adbc68b439697f",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here is what I found across all four searches:\n\n---\n\n**Is EMNLP 2026 in Budapest?**\n\nYes, confirmed. EMNLP 2026 will be held **October 24-29, 2026, in Budapest, Hungary**. This is stated on the official EMNLP 2026 website and corroborated by LINGUIST List, ConferenceDeadlines.com, and multiple other sources.\n\n**What is the ARR submission deadline for the cycle that feeds into EMNLP 2026?**\n\nThe ARR May 2026 cycle is the submission cycle that feeds into EMNLP 2026. The submission deadline is **May 25, 2026**. This is confirmed by the official EMNLP 2026 Call for Papers page and the EMNLP 2026 Twitter/X account. Key downstream dates after that:\n\n- Reviewer registration deadline for all authors: May 27, 2026\n- Author response and author-reviewer discussion: July 7-13, 2026\n- Meta-reviews released: July 30, 2026\n- EMNLP commitment deadline: August 2, 2026\n- Notification of acceptance: August 20, 2026\n\nAll deadlines are 11:59 PM UTC-12:00 (\"anywhere on Earth\").\n\n**Is May 25, 2026 a real ARR deadline?**\n\nYes, May 25, 2026 is a confirmed, real ARR deadline. It is the submission deadline for the ARR May 2026 cycle. Notably, this cycle is shared between **two** conferences -- EMNLP 2026 and AACL-IJCNLP 2026 (which will be held November 6-10 in Hengqin, China). Because of this shared cycle, there is an important policy: **authors must explicitly declare which conference they intend to commit to at submission time, and this choice is binding for EMNLP 2026**. Submissions that do not select EMNLP 2026 during the ARR submission will not be able to commit to EMNLP 2026 later.\n\n---\n\n**Verdict on the proposal's claims:** The statement \"ARR submission deadline: May 25, 2026; conference: October 24-29, Budapest\" is **accurate on all three points** -- the date, the location, and the conference dates are all confirmed by official sources. The one nuance the proposal does not mention is the binding conference-selection requirement at submission time due to the shared EMNLP/AACL cycle.\n\nSources:\n- [EMNLP 2026 - Call for Main Conference Papers](https://2026.emnlp.org/calls/main_conference_papers/)\n- [EMNLP 2026 Official Website](https://2026.emnlp.org/)\n- [EMNLP 2026 First Call for Papers (X/Twitter)](https://x.com/emnlpmeeting/status/2029508292637061462)\n- [EMNLP 2026 Critical Update on Shared ARR Cycle (X/Twitter)](https://x.com/emnlpmeeting/status/2047754845919031450)\n- [AACL-IJCNLP 2026 Announcement (X/Twitter)](https://x.com/aaclmeeting/status/2041832211599733075)\n- [ACL Rolling Review - Dates and Venues](http://aclrollingreview.org/dates)\n- [LINGUIST List - EMNLP 2026 (Hungary)](https://linguistlist.org/issues/37/972/)\n- [AI Conference Deadlines - EMNLP 2026](https://mlciv.com/ai-deadlines/conference/?id=emnlp26)"
      }
    ],
    "totalDurationMs": 32184,
    "totalTokens": 14729,
    "totalToolUseCount": 5,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3439,
      "cache_read_input_tokens": 10369,
      "output_tokens": 920,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3439
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 920,
          "cache_read_input_tokens": 10369,
          "cache_creation_input_tokens": 3439,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3439,
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
  "sourceToolAssistantUUID": "68de1907-c762-4901-ac12-14dd7ccb7ad7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3851818f-b8a5-4456-92d9-6671bfb78776",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 22_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-16 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "706b7025-f1f0-4e74-a205-7acac2244563",
  "sessionId": "3851818f-b8a5-4456-92d9-6671bfb78776"
}
```

---

### Runtime record

_source line 23_

```json
{
  "type": "ai-title",
  "aiTitle": "Miscalibration-triggered logit steering for hallucination mitigation",
  "sessionId": "3851818f-b8a5-4456-92d9-6671bfb78776"
}
```

---

### Tool result

_source line 24 · 2026-05-16T09:04:13.951Z_

<details><summary>↩ Tool result · `toolu_01R65W5Lc2LqB8PiY21e27zL`</summary>

```text
All five papers have been verified. Here is my complete assessment:

---

## Verification Results

### 1. FactCheckmate (arXiv 2410.02899) -- VERIFIED, REAL PAPER

- **Title:** "FactCheckmate: Preemptively Detecting and Mitigating Hallucinations in LMs"
- **Authors:** Deema Alnuhait, Neeraja Kirtane, Muhammad Khalifa, Hao Peng (UIUC / U Michigan)
- **Submitted:** October 3, 2024; revised June 24, 2025
- **What it actually does:** Trains a classifier on hidden states to predict hallucinations *before decoding begins*, then adjusts hidden states to produce more factual outputs. Detection accuracy >70%; outputs 34.4% more factual after intervention.
- **Sub-agent's description accuracy:** Accurate. The claim about training a classifier on hidden states and adjusting hidden states to correct them is correct.
- **Relevance to "miscalibration-triggered logit-level intervention":** Moderate overlap in spirit (detect-then-intervene at inference time), but FactCheckmate operates on **hidden states**, not logits. It also intervenes *before* decoding, not during token generation. The mechanism is fundamentally different from logit-level intervention.

### 2. Token-Guard (arXiv 2601.21969) -- VERIFIED, REAL PAPER

- **Title:** "Token-Guard: Towards Token-Level Hallucination Control via Self-Checking Decoding"
- **Authors:** Yifan Zhu, Huiqiang Rong, Haoran Luo
- **Submitted:** January 29, 2026
- **ICLR 2026:** Confirmed accepted at ICLR 2026 main conference (verified via both arXiv and OpenReview/GitHub).
- **What it actually does:** Performs internal verification at each reasoning step, evaluates candidate fragments in latent space with hallucination risk scoring, and uses iterative pruning/regeneration to correct detected errors.
- **Sub-agent's description accuracy:** Accurate. The claim about token-level hallucination control via self-checking decoding and ICLR 2026 acceptance is correct.
- **Relevance to "miscalibration-triggered logit-level intervention":** High conceptual overlap -- it is a decoding-time, token-level intervention method. However, it operates in **latent space** (not directly on logits) and uses pruning/regeneration rather than logit penalization. It is probably the closest competitor to a logit-level intervention approach.

### 3. HELIX / Tethered Reasoning (arXiv 2602.17691) -- VERIFIED, REAL PAPER

- **Title:** "Tethered Reasoning: Decoupling Entropy from Hallucination in Quantized LLMs via Manifold Steering"
- **Author:** Craig Atkinson (single author)
- **Submitted:** February 6, 2026
- **What it actually does:** Computes a Unified Truth Score (UTS) combining semantic entropy with Mahalanobis distance from a pre-computed "truthfulness manifold." When UTS signals trajectory divergence, **graduated steering vectors** redirect activations. Focused specifically on quantized models at high sampling temperatures.
- **Sub-agent's description accuracy:** Mostly accurate, but with one important error. The sub-agent claimed "logit penalization" -- this is **wrong**. HELIX uses **steering vectors on activations/hidden states**, not logit penalization. The UTS and Mahalanobis distance claims are correct.
- **Relevance to "miscalibration-triggered logit-level intervention":** Significant conceptual overlap in the "detect miscalibration then intervene" pattern. However: (a) it uses steering vectors on activations, not logit-level manipulation; (b) it is specifically scoped to quantized models at extreme temperatures, which is a narrower problem setting.

### 4. VIB-Probe (arXiv 2601.05547) -- VERIFIED, REAL PAPER

- **Title:** "VIB-Probe: Detecting and Mitigating Hallucinations in Vision-Language Models via Variational Information Bottleneck"
- **Authors:** Feiran Zhang, Yixin Wu, Zhenghua Wang, Xiaohua Wang, Changze Lv, Xuanjing Huang, Xiaoqing Zheng
- **Submitted:** January 9, 2026; revised April 17, 2026
- **What it actually does:** Uses VIB probes on internal attention head outputs across layers for hallucination detection, then applies an inference-time intervention strategy for mitigation. Explicitly contrasts itself against methods that "rely on output logits."
- **Sub-agent's description accuracy:** Partially accurate. The VIB probe and attention head claims are correct. However, the sub-agent likely omitted a critical detail: this paper is about **Vision-Language Models (VLMs)**, not text-only LLMs. If the research proposal targets text-only LLMs, this is a different domain.
- **Relevance to "miscalibration-triggered logit-level intervention":** Low-to-moderate. It operates on attention head outputs (not logits), and targets vision-language models specifically. It is more of a related-but-distinct approach.

### 5. DRIFT (arXiv 2601.14210) -- VERIFIED, REAL PAPER

- **Title:** "DRIFT: Detecting Representational Inconsistencies for Factual Truthfulness"
- **Authors:** Rohan Bhatnagar, Youran Sun, Chi Andrew Zhang, Yixin Wen, Haizhao Yang
- **Submitted:** January 20, 2026; revised January 29, 2026
- **What it actually does:** Trains a lightweight probe on intermediate hidden states to detect confidence signals that predict hallucinations. Adds <0.1% overhead and runs in parallel with generation. Achieves SOTA AUROC on 10/12 settings across 4 QA benchmarks. Also develops an LLM router for delegating uncertain queries.
- **Sub-agent's description accuracy:** Mostly accurate. The "lightweight probes" and "hallucination detection" claims are correct. The sub-agent said "residual probes" -- the paper says "lightweight probe" with no mention of "residual." This is a minor inaccuracy.
- **Relevance to "miscalibration-triggered logit-level intervention":** Low-to-moderate. DRIFT is **detection only** -- it identifies hallucinations but does not intervene to correct them (it routes to a stronger model instead). It operates on hidden states, not logits.

---

## Summary Assessment

**All five papers are real and exist on arXiv.** The sub-agent did not hallucinate their existence, which is a good sign. However, there are important nuances:

| Paper | Exists? | Sub-agent description accurate? | Actually operates on logits? |
|-------|---------|-------------------------------|------------------------------|
| FactCheckmate | Yes | Yes | No (hidden states) |
| Token-Guard | Yes | Yes | No (latent space) |
| HELIX | Yes | Mostly (wrongly says "logit penalization") | No (steering vectors on activations) |
| VIB-Probe | Yes | Partially (omits VLM-only scope) | No (attention head outputs) |
| DRIFT | Yes | Mostly (minor "residual" error) | No (hidden states, detection-only) |

**Key finding: None of these five papers actually perform logit-level intervention.** They all operate at the hidden state or activation level. If the research proposal's core novelty is specifically "miscalibration-triggered logit-level intervention," there may be more differentiation from these works than the sub-agent implied. However, the general paradigm of "detect hallucination signals in internal representations and intervene at inference time" is well-explored by these papers. The proposal would need to clearly articulate why logit-level intervention is superior to hidden-state-level intervention, and how its detection mechanism differs from these approaches.

Sources:
- [FactCheckmate (arXiv 2410.02899)](https://arxiv.org/abs/2410.02899)
- [FactCheckmate GitHub](https://github.com/deema-A/FactCheckmate)
- [Token-Guard (arXiv 2601.21969)](https://arxiv.org/abs/2601.21969)
- [Token-Guard OpenReview](https://openreview.net/forum?id=5fCDEz43ya)
- [Token-Guard GitHub (ICLR 2026)](https://github.com/rhq945/Token-Guard)
- [Tethered Reasoning / HELIX (arXiv 2602.17691)](https://arxiv.org/abs/2602.17691)
- [VIB-Probe (arXiv 2601.05547)](https://arxiv.org/abs/2601.05547)
- [DRIFT (arXiv 2601.14210)](https://arxiv.org/abs/2601.14210)

agentId: a76133d48dfbda0d0 (use SendMessage with to: 'a76133d48dfbda0d0' to continue this agent)
&lt;usage>total_tokens: 22634
tool_uses: 14
duration_ms: 78164&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "31247f9e-eec6-46b3-a5bb-015f56784cff",
  "isSidechain": false,
  "promptId": "c0b2dcb7-0dd5-433d-a0d3-dd686e91d702",
  "type": "user",
  "uuid": "2927be95-4262-49d9-8787-d0ee338669ea",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I'm reviewing a research proposal and a sub-agent found potentially critical competing papers. I need you to verify these actually exist and check their details using WebSearch and WebFetch:\n\n1. **FactCheckmate (arXiv 2410.02899)** - Claimed to train a classifier on hidden states to detect impending hallucinations and then adjust hidden states to correct them. Search for \"arxiv 2410.02899\" and \"FactCheckmate hallucination\" to verify this paper exists and what it actually does. Try to WebFetch the arxiv abstract page.\n\n2. **Token-Guard (arXiv 2601.21969, claimed ICLR 2026)** - Claimed to perform token-level hallucination control via self-checking decoding. Search for \"arxiv 2601.21969\" and \"Token-Guard hallucination ICLR 2026\" to verify.\n\n3. **HELIX / Tethered Reasoning (arXiv 2602.17691)** - Claimed to compute a Unified Truth Score combining semantic entropy with Mahalanobis distance and use logit penalization. Search for \"arxiv 2602.17691\" and \"HELIX tethered reasoning hallucination\".\n\n4. **VIB-Probe (arXiv 2601.05547)** - Claimed to use Variational Information Bottleneck probes on attention heads for inference-time mitigation. Search for \"arxiv 2601.05547\".\n\n5. **DRIFT (arXiv 2601.14210)** - Claimed lightweight residual probes for hallucination detection. Search for \"arxiv 2601.14210 DRIFT hallucination\".\n\nFor each, report: Does it exist? What does it actually do? How close is it to the proposal's idea of \"miscalibration-triggered logit-level intervention\"? Be skeptical — the sub-agent may have hallucinated some of these papers.",
    "agentId": "a76133d48dfbda0d0",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "All five papers have been verified. Here is my complete assessment:\n\n---\n\n## Verification Results\n\n### 1. FactCheckmate (arXiv 2410.02899) -- VERIFIED, REAL PAPER\n\n- **Title:** \"FactCheckmate: Preemptively Detecting and Mitigating Hallucinations in LMs\"\n- **Authors:** Deema Alnuhait, Neeraja Kirtane, Muhammad Khalifa, Hao Peng (UIUC / U Michigan)\n- **Submitted:** October 3, 2024; revised June 24, 2025\n- **What it actually does:** Trains a classifier on hidden states to predict hallucinations *before decoding begins*, then adjusts hidden states to produce more factual outputs. Detection accuracy >70%; outputs 34.4% more factual after intervention.\n- **Sub-agent's description accuracy:** Accurate. The claim about training a classifier on hidden states and adjusting hidden states to correct them is correct.\n- **Relevance to \"miscalibration-triggered logit-level intervention\":** Moderate overlap in spirit (detect-then-intervene at inference time), but FactCheckmate operates on **hidden states**, not logits. It also intervenes *before* decoding, not during token generation. The mechanism is fundamentally different from logit-level intervention.\n\n### 2. Token-Guard (arXiv 2601.21969) -- VERIFIED, REAL PAPER\n\n- **Title:** \"Token-Guard: Towards Token-Level Hallucination Control via Self-Checking Decoding\"\n- **Authors:** Yifan Zhu, Huiqiang Rong, Haoran Luo\n- **Submitted:** January 29, 2026\n- **ICLR 2026:** Confirmed accepted at ICLR 2026 main conference (verified via both arXiv and OpenReview/GitHub).\n- **What it actually does:** Performs internal verification at each reasoning step, evaluates candidate fragments in latent space with hallucination risk scoring, and uses iterative pruning/regeneration to correct detected errors.\n- **Sub-agent's description accuracy:** Accurate. The claim about token-level hallucination control via self-checking decoding and ICLR 2026 acceptance is correct.\n- **Relevance to \"miscalibration-triggered logit-level intervention\":** High conceptual overlap -- it is a decoding-time, token-level intervention method. However, it operates in **latent space** (not directly on logits) and uses pruning/regeneration rather than logit penalization. It is probably the closest competitor to a logit-level intervention approach.\n\n### 3. HELIX / Tethered Reasoning (arXiv 2602.17691) -- VERIFIED, REAL PAPER\n\n- **Title:** \"Tethered Reasoning: Decoupling Entropy from Hallucination in Quantized LLMs via Manifold Steering\"\n- **Author:** Craig Atkinson (single author)\n- **Submitted:** February 6, 2026\n- **What it actually does:** Computes a Unified Truth Score (UTS) combining semantic entropy with Mahalanobis distance from a pre-computed \"truthfulness manifold.\" When UTS signals trajectory divergence, **graduated steering vectors** redirect activations. Focused specifically on quantized models at high sampling temperatures.\n- **Sub-agent's description accuracy:** Mostly accurate, but with one important error. The sub-agent claimed \"logit penalization\" -- this is **wrong**. HELIX uses **steering vectors on activations/hidden states**, not logit penalization. The UTS and Mahalanobis distance claims are correct.\n- **Relevance to \"miscalibration-triggered logit-level intervention\":** Significant conceptual overlap in the \"detect miscalibration then intervene\" pattern. However: (a) it uses steering vectors on activations, not logit-level manipulation; (b) it is specifically scoped to quantized models at extreme temperatures, which is a narrower problem setting.\n\n### 4. VIB-Probe (arXiv 2601.05547) -- VERIFIED, REAL PAPER\n\n- **Title:** \"VIB-Probe: Detecting and Mitigating Hallucinations in Vision-Language Models via Variational Information Bottleneck\"\n- **Authors:** Feiran Zhang, Yixin Wu, Zhenghua Wang, Xiaohua Wang, Changze Lv, Xuanjing Huang, Xiaoqing Zheng\n- **Submitted:** January 9, 2026; revised April 17, 2026\n- **What it actually does:** Uses VIB probes on internal attention head outputs across layers for hallucination detection, then applies an inference-time intervention strategy for mitigation. Explicitly contrasts itself against methods that \"rely on output logits.\"\n- **Sub-agent's description accuracy:** Partially accurate. The VIB probe and attention head claims are correct. However, the sub-agent likely omitted a critical detail: this paper is about **Vision-Language Models (VLMs)**, not text-only LLMs. If the research proposal targets text-only LLMs, this is a different domain.\n- **Relevance to \"miscalibration-triggered logit-level intervention\":** Low-to-moderate. It operates on attention head outputs (not logits), and targets vision-language models specifically. It is more of a related-but-distinct approach.\n\n### 5. DRIFT (arXiv 2601.14210) -- VERIFIED, REAL PAPER\n\n- **Title:** \"DRIFT: Detecting Representational Inconsistencies for Factual Truthfulness\"\n- **Authors:** Rohan Bhatnagar, Youran Sun, Chi Andrew Zhang, Yixin Wen, Haizhao Yang\n- **Submitted:** January 20, 2026; revised January 29, 2026\n- **What it actually does:** Trains a lightweight probe on intermediate hidden states to detect confidence signals that predict hallucinations. Adds <0.1% overhead and runs in parallel with generation. Achieves SOTA AUROC on 10/12 settings across 4 QA benchmarks. Also develops an LLM router for delegating uncertain queries.\n- **Sub-agent's description accuracy:** Mostly accurate. The \"lightweight probes\" and \"hallucination detection\" claims are correct. The sub-agent said \"residual probes\" -- the paper says \"lightweight probe\" with no mention of \"residual.\" This is a minor inaccuracy.\n- **Relevance to \"miscalibration-triggered logit-level intervention\":** Low-to-moderate. DRIFT is **detection only** -- it identifies hallucinations but does not intervene to correct them (it routes to a stronger model instead). It operates on hidden states, not logits.\n\n---\n\n## Summary Assessment\n\n**All five papers are real and exist on arXiv.** The sub-agent did not hallucinate their existence, which is a good sign. However, there are important nuances:\n\n| Paper | Exists? | Sub-agent description accurate? | Actually operates on logits? |\n|-------|---------|-------------------------------|------------------------------|\n| FactCheckmate | Yes | Yes | No (hidden states) |\n| Token-Guard | Yes | Yes | No (latent space) |\n| HELIX | Yes | Mostly (wrongly says \"logit penalization\") | No (steering vectors on activations) |\n| VIB-Probe | Yes | Partially (omits VLM-only scope) | No (attention head outputs) |\n| DRIFT | Yes | Mostly (minor \"residual\" error) | No (hidden states, detection-only) |\n\n**Key finding: None of these five papers actually perform logit-level intervention.** They all operate at the hidden state or activation level. If the research proposal's core novelty is specifically \"miscalibration-triggered logit-level intervention,\" there may be more differentiation from these works than the sub-agent implied. However, the general paradigm of \"detect hallucination signals in internal representations and intervene at inference time\" is well-explored by these papers. The proposal would need to clearly articulate why logit-level intervention is superior to hidden-state-level intervention, and how its detection mechanism differs from these approaches.\n\nSources:\n- [FactCheckmate (arXiv 2410.02899)](https://arxiv.org/abs/2410.02899)\n- [FactCheckmate GitHub](https://github.com/deema-A/FactCheckmate)\n- [Token-Guard (arXiv 2601.21969)](https://arxiv.org/abs/2601.21969)\n- [Token-Guard OpenReview](https://openreview.net/forum?id=5fCDEz43ya)\n- [Token-Guard GitHub (ICLR 2026)](https://github.com/rhq945/Token-Guard)\n- [Tethered Reasoning / HELIX (arXiv 2602.17691)](https://arxiv.org/abs/2602.17691)\n- [VIB-Probe (arXiv 2601.05547)](https://arxiv.org/abs/2601.05547)\n- [DRIFT (arXiv 2601.14210)](https://arxiv.org/abs/2601.14210)"
      }
    ],
    "totalDurationMs": 78164,
    "totalTokens": 22634,
    "totalToolUseCount": 14,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3953,
      "cache_read_input_tokens": 16479,
      "output_tokens": 2201,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3953
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2201,
          "cache_read_input_tokens": 16479,
          "cache_creation_input_tokens": 3953,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3953,
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
  "sourceToolAssistantUUID": "31247f9e-eec6-46b3-a5bb-015f56784cff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3851818f-b8a5-4456-92d9-6671bfb78776",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 25 · 2026-05-16T09:05:49.951Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me synthesize everything I've found and prepare my review. Let me organize the key findings:

## Key Findings from My Research

### Reference Verification
1. **Ji et al. (VUF)** - EXISTS, but the "EMNLP 2025 Outstanding Paper" claim is FALSE. It received a SAC Highlight, not Outstanding Paper. The proposal's user requirement section says "EMNLP 2025 awarded TWO Outstanding Papers in this space" - this is wrong for Ji et al.
2. **ESR paper** - EXISTS, accurate claims
3. **PC-LDCD** - EXISTS, but the claim that it "acknowledges failure on overconfident hallucinations" is overstated


4. **Globalcells probes** - EXISTS but misattributed to EMNLP 2025 Findings when it's likely an ICLR 2026 submission
5. **CSS** - EXISTS, 0.913 claim verified
6. **Monitoring Decoding** - EXISTS, but the 5.7x latency claim isn't supported by the paper
7. **Venue (EMNLP 2026)** - CONFIRMED: May 25, 2026 ARR deadline, Budapest, Oct 24-29

### Competing Work NOT Cited
I'm also noticing that FactCheckmate, a real arXiv paper on hidden-state probes, isn't cited in the proposal despite being directly relevant to their approach.

Looking at other competing methods: Token-Guard does token-level self-checking, HELIX uses steering vectors rather than logit penalization, VIB-Probe focuses on vision-language models, and DRIFT is detection-only. None of these actually perform logit-level intervention the way this proposal does, so there's genuine differentiation here.

The baseline numbers check out—DoLa shows +12-17% improvements and ActLCD achieves +19.81%.

Now examining the proposal's strengths after multiple rounds of revision: it's addressed most concerns, tested across two model families to show generalization, framed the contributions honestly around both calibration and factuality improvements, designed strong experiments comparing against PC-LDCD, included TruthfulQA evaluation, specified safeguards against cascading errors, and planned latency benchmarking.

But there are significant gaps. The Ji et al. paper is incorrectly cited as an "Outstanding Paper" when it was actually a SAC Highlight—a factual error that reviewers will catch. More critically, the proposal misses two major competing works: FactCheckmate and Token-Guard, both of which do probe-guided hallucination correction at inference time, and Token-Guard especially at ICLR 2026 is a direct competitor that reviewers will definitely know about. The core claim about PC-LDCD's fundamental limitations also rests on an unverified assumption that needs stronger support.

The entire differentiation hinges on whether Q2 (overconfident hallucinations) is meaningfully populated at ≥15%—if it's actually below 10%, the novelty claim collapses. And the hedge logit bias intervention itself is crude: a static bias vector with fixed weights for hedge versus assertive tokens ignores context entirely, treating "approximately" before a number the same as "possibly" before a verb, which are linguistically very different phenomena.

The rollback mechanism's core claim—that forced uncertainty prefixes reduce specificity—is completely untested, and the aggressive temperature reduction to 0.3 combined with prefix injection and hedge biasing could easily produce incoherent outputs without any empirical validation of their interaction. On the compute side, the 130 A100-hours plus 20 H100-hours translates to roughly 85-100 H100-equivalent hours, which fits within the 200-hour budget, so that constraint at least checks out.

The timeline is tight—6-7 weeks for manual mode against a 12-16 day auto estimate when the hard constraint is 11 days—but it's borderline feasible. The OHR annotation study with 100 examples and 2 annotators is minimal but acceptable for metric validation. However, the FActScore evaluation using a local 70B Llama model requires substantial GPU memory that isn't accounted for in the budget, unless they're planning to use an API instead, which would cost $200-500 but needs to be explicitly stated. There's also a venue discrepancy: the proposal claims EMNLP 2025 Findings, but the paper appears to be under ICLR 2026 review, which affects the timeline and acceptance status.

On novelty, the specific combination of miscalibration as a trigger signal paired with logit-level intervention and graded responses is genuinely novel, but the broader paradigm of probe-guided hallucination correction is well-established in prior work like FactCheckmate and Token-Guard. The real innovation lies in the trigger mechanism itself—using verbal-internal mismatch rather than other signals—which pushes this toward a 3 or 4 on novelty. ations. The implementation is feasible within the timeline constraints—VUF extraction, probe training, and logit bias adjustments are straightforward—but the real bottlenecks are probe generalization to Qwen3-8B, reimplementing PCNet, and gathering enough Q2 samples. The Day 3 gate helps mitigate risk. Actually, looking back at the timeline more carefully, the manual path takes 6-7 weeks and auto mode runs 12-16 days, both overshooting the 11-day window. I need to verify whether the compute budget of ≤200 H100-hours is even achievable within that constraint.

The manual approach uses roughly 105 H100-equivalent hours, which fits the budget, but the 6-7 week timeline is a non-starter. Auto mode at 12-16 days exceeds the deadline by 1-5 days, though it's the closest fit. The real issue is that no execution mode comfortably lands within 11 days. The auto path could potentially compress with additional GPU allocation, but the sequential dependencies are the actual constraint—more parallelism won't solve everything.

On feasibility, I'm settling on a 3 given how tight this timeline really is. The proposal itself is exceptionally detailed and well-structured, with precise formulas, token specifications, and a thoughtful confusion-matrix design that makes the dual contribution clear. That pushes clarity to a 4. For impact, if the Q2 analysis validates that at least 15% of hallucinations are overconfident cases MisTAG can catch, it's a solid practical contribution—training-free operation on frozen models has real deployment value. But it's incremental rather than transformative, more of an improvement on existing detect-then-intervene methods than a fundamental shift. I'd rate that a 3.5.

Now I'm noticing some critical issues. There are two major competing works that aren't cited—FactCheckmate and Token-Guard—both doing probe-guided hallucination correction at inference time. Token-Guard is particularly important since it's at ICLR 2026, a top venue, and handles token-level control during decoding. EMNLP reviewers will definitely expect that to be discussed. There's also a factual error about Ji et al. receiving an Outstanding Paper award when it was actually just a SAC Highlight, which damages credibility. The venue claim for one of the papers appears wrong too—it looks like it's under ICLR 2026 review, not published at EMNLP 2025 Findings. And the limitation claim about PC-LDCD seems overstated.

The proposal's timeline also doesn't work—even the auto mode estimates 12-16 days, but the user's hard constraint is 11 days maximum. I'm also seeing that the hedge logit bias approach of applying static +1/-1 adjustments to tokens could create grammatically awkward outputs without any quality filtering in place. Missing citations for FactCheckmate, Token-Guard, DRIFT, and HELIX are problematic since these directly relate to the probe-to-intervention paradigm the proposal is built on.

But stepping back, I need to distinguish between what a real EMNLP reviewer would actually care about versus minor issues. The truly critical problems are: Token-Guard from ICLR 2026 is a top-tier paper in the exact same paradigm and not citing it would be flagged as incomplete related work; the core Q2 hypothesis about overconfident on-manifold hallucinations is completely untested, so if those don't exist in meaningful quantities, the whole contribution just becomes another detect-then-intervene method with a different signal; the grammaticality risk from the hedge action's static logit bias is real even though MT-Bench partially addresses it; and the timeline constraint is genuinely impossible to meet.

Given these constraints, my scoring comes out to novelty at 4, feasibility at 3 due to timeline and hypothesis risk, clarity at 4, and impact at 3, averaging to 3.5—below the 4.0 threshold. But I should reconsider this since we're on round 5 of 10 and the proposal has genuinely improved. The fixable issues are the missing competing work and some of the timeline pressure, while the unfixable ones are the Q2 hypothesis risk and the PCNet reimplementation challenge.

Let me reassess the novelty score more carefully. The miscalibration trigger combining verbal confidence direction with factuality probes is genuinely new—no existing work multiplies these signals together as a logit intervention mechanism. The confusion-matrix analysis is well-designed to demonstrate the advantage empirically, and the honest dual-contribution framing is refreshing. The core paradigm of detecting internal signals and intervening during generation is established in prior work, but the specific signal and mechanism here are novel enough to warrant a 4.

The feasibility concerns are real: the auto mode timeline stretches to 12-16 days against an 11-day constraint, the PCNet reimplementation is a significant dependency, and the Q2 hypothesis poses the biggest risk—if fewer than 10% of hallucinations are overconfident on-manifold, the differentiation claim falls apart. Running FActScore evaluation locally also requires substantial compute that isn't accounted for in the main budget.

The writing is extremely detailed with clear ablations and baselines, though there are factual errors to fix and an overstated claim about PC-LDCD's limitations. The impact is meaningful but incremental—the real value hinges on whether Q2 reveals a previously unrecognized failure mode.

The verdict is to revise. I need to cite FactCheckmate and Token-Guard with clear differentiation, fix the factual errors, either tighten the timeline or reduce scope to fit the 11-day window, address whether the logit bias outputs are grammatical, and be more honest that the PC-LDCD limitation is my theoretical argument rather than their admission.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2927be95-4262-49d9-8787-d0ee338669ea",
  "isSidechain": false,
  "requestId": "req_011Cb5ykqLpvn8hbFtWkyMmT",
  "type": "assistant",
  "uuid": "0c290b77-52f9-4d60-a7e8-ccc826c518c5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3851818f-b8a5-4456-92d9-6671bfb78776",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GpBCFkc6xCMGu1Mwixtwyg",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1018,
      "cache_creation_input_tokens": 5486,
      "cache_read_input_tokens": 40468,
      "output_tokens": 6356,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5486,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1018,
          "output_tokens": 6356,
          "cache_read_input_tokens": 40468,
          "cache_creation_input_tokens": 5486,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5486
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

_source line 26 · 2026-05-16T09:06:34.732Z_

Now I have all the data I need. Let me synthesize my findings into a comprehensive review.

**Key findings from my independent research:**

1. **Ji et al. is NOT an Outstanding Paper** — it received a SAC Highlight, a tier below
2. **obalcells venue is likely wrong** — appears to be under ICLR 2026 review, not EMNLP 2025 Findings
3. **Critical missing work found**: FactCheckmate (arXiv 2410.02899) and Token-Guard (ICLR 2026, arXiv 2601.21969) — both probe-guided inference-time hallucination correction
4. **PC-LDCD doesn't actually acknowledge the overconfident hallucination limitation** the proposal claims it does
5. **Venue/deadline verified**: EMNLP 2026, May 25 ARR deadline, Budapest — all correct
6. **Baseline numbers largely verified** (DoLa, ActLCD, PC-LDCD)
7. **No existing paper combines the exact trigger signal (VUF × probe) with logit-level intervention** — genuine novelty gap exists

```json
{
  "verdict": "revise",
  "scores": {
    "novelty": {"score": 4, "rationale": "The miscalibration trigger (VUF confidence × probe hallucination probability) as a multiplicative signal for logit-level intervention is genuinely novel — no existing work combines these specific signals this way. However, the broader 'probe-guided inference-time hallucination correction' paradigm is well-explored by FactCheckmate (arXiv 2410.02899), Token-Guard (ICLR 2026), PC-LDCD, and HELIX, none of which are adequately discussed."},
    "feasibility": {"score": 3, "rationale": "Auto mode estimates 12-16 days, exceeding the 11-day hard constraint. PCNet reimplementation is a blocking dependency for the core confusion-matrix analysis. The Q2 hypothesis (≥15% overconfident on-manifold hallucinations) is the biggest risk — if it fails, the entire differentiation claim weakens, and the fallback ('complementary detection') is a substantially weaker paper."},
    "clarity": {"score": 4, "rationale": "Exceptionally detailed specification with exact formulas, token counts, ablation designs, and the honest dual-contribution framing is a strength. Marred by factual errors: Ji et al. received SAC Highlight not Outstanding Paper, obalcells venue is wrong (ICLR 2026 submission, not EMNLP 2025 Findings), and PC-LDCD's 'acknowledged limitation' is overstated."},
    "impact": {"score": 3, "rationale": "If the Q2 analysis confirms ≥15% of hallucinations are overconfident on-manifold (caught by MisTAG but missed by PC-LDCD), this is a meaningful contribution revealing and addressing a previously underexplored failure mode. If Q2 is small, the paper reduces to an incremental variant of detect-then-intervene. The hedge action alone (calibration without factuality improvement) is a weak standalone contribution for the Generation track."}
  },
  "issues": [
    "Critical missing related work: Token-Guard (arXiv 2601.21969, ICLR 2026) performs token-level hallucination control via self-checking decoding with iterative pruning/regeneration during generation — accepted at a top venue in the same paradigm. FactCheckmate (arXiv 2410.02899, UIUC) trains a classifier on hidden states to detect and correct hallucinations at inference time, achieving 34.4% factuality improvement. Both must be cited and differentiated. The proposal's argument that logit-level intervention is ESR-immune (unlike hidden-state steering) IS a valid differentiator from these — but it needs to be explicitly made.",
    "Ji et al. (EMNLP 2025) is described as 'Outstanding Paper' but actually received a SAC Highlight — a distinct and lesser recognition. The user's requirement text propagates this error, but the proposal should not perpetuate it. EMNLP 2025 Outstanding Papers were different work.",
    "obalcells et al. is cited as 'EMNLP 2025 Findings' but does not appear in ACL Anthology for EMNLP 2025. It appears to be under review at ICLR 2026 (OpenReview forum YxJEMTflww). The similar 'Simple Factuality Probes Detect Hallucinations' (Han et al., aclanthology.org/2025.findings-emnlp.880) IS at EMNLP 2025 Findings — these may be confused. Correct the citation.",
    "The claim that PC-LDCD 'explicitly fails on overconfident hallucinations' and 'acknowledges the fundamental limitation' is overstated. PC-LDCD's Limitations section discusses calibration set costs, scale limits, and task-type differences — it does NOT explicitly flag overconfident on-manifold hallucinations as a remaining limitation. This is the proposal's own theoretical argument (plausible but unproven), not PC-LDCD's admission. Phrase it accordingly.",
    "Static hedge logit bias (+1 for ~50 hedge tokens, -1 for ~30 assertive tokens) risks grammatical incoherence. 'Approximately' before a date works; 'approximately' before a verb does not. No grammatical filtering or position-awareness is specified. MT-Bench partially catches this, but the proposal should acknowledge the risk and consider context-dependent bias (e.g., only apply hedge bias at entity-bearing positions where the probe fires strongly).",
    "Auto-mode timeline of 12-16 days exceeds the 11-day hard constraint. The PCNet reimplementation is flagged as a speed bottleneck. To fit 11 days: either (a) drop the confusion-matrix analysis with PC-LDCD (losing the core novelty experiment), (b) use PC-LDCD's released code if available rather than reimplementing, or (c) reduce to one primary model with the second as stretch goal.",
    "FActScore evaluation requires serving Llama-3.1-70B locally (2× A100 80GB), but these GPU hours are not included in the main compute budget. If the two A100s for primary models (Qwen3-8B and Llama-3.1-8B) are also used for FActScore serving, there's a scheduling conflict. Budget this explicitly or use API-based evaluation."
  ],
  "feedback": "The proposal has matured substantially across 4 rounds and the core idea is sound. The remaining gap to pass threshold is primarily about completeness and honesty of the related work discussion, plus timeline realism. Specific actions:\n\n1. **Cite Token-Guard (ICLR 2026) and FactCheckmate**: Both are probe-guided inference-time hallucination correction. Differentiate clearly: Token-Guard uses self-checking in latent space (susceptible to ESR); FactCheckmate intervenes on hidden states pre-generation (cannot handle streaming). MisTAG's logit-level intervention is ESR-immune by design and operates during generation. This is your real differentiator — make it the explicit argument.\n\n2. **Fix factual errors**: Ji et al. = SAC Highlight (not Outstanding Paper); obalcells = under ICLR 2026 review (not EMNLP 2025 Findings); PC-LDCD limitation = your theoretical argument, not their admission. These errors will destroy credibility with reviewers who know the field.\n\n3. **Make hedge bias position-aware**: Instead of applying the static bias at every mild-mismatch token, restrict it to tokens where the probe's hallucination probability is high AND the previous token is a numeral, proper noun, or entity-bearing token (detectable via simple heuristics). This prevents 'approximately began' type errors and costs nothing in compute.\n\n4. **Tighten timeline**: Check if PC-LDCD has released code (the paper is from May 2026, code may be on GitHub). If code is available, reimplementation drops from 15h to 2-3h, potentially fitting the 11-day window. If not, consider the confusion-matrix analysis as a secondary contribution that can be completed during the review period, with the main submission focusing on MisTAG's standalone performance vs. DoLa/ActLCD baselines.\n\n5. **Budget FActScore evaluation GPU hours**: Either add 30-40h for 70B serving or switch to API-based evaluation (GPT-4o) and increase the API budget accordingly. Current budget underestimates this.\n\n6. **Strengthen the Q2 fallback**: If Q2 < 15%, the paper should still work by reframing: 'MisTAG's miscalibration trigger provides complementary coverage to density-based methods, with the hedge action providing training-free calibration correction unavailable from any existing method.' The dual-contribution (calibration + factuality) still holds even if the detection advantage is modest.",
  "reason": "Strong core idea with genuine novelty in the miscalibration trigger, but missing critical competing work (Token-Guard ICLR 2026, FactCheckmate), multiple factual citation errors, and timeline slightly exceeds constraint — fixable issues that prevent a pass at this round."
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0c290b77-52f9-4d60-a7e8-ccc826c518c5",
  "isSidechain": false,
  "requestId": "req_011Cb5ykqLpvn8hbFtWkyMmT",
  "type": "assistant",
  "uuid": "8ba46eef-70c5-49a1-87f2-ee95040ce7fc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3851818f-b8a5-4456-92d9-6671bfb78776",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GpBCFkc6xCMGu1Mwixtwyg",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1018,
      "cache_creation_input_tokens": 5486,
      "cache_read_input_tokens": 40468,
      "output_tokens": 6356,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5486,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1018,
          "output_tokens": 6356,
          "cache_read_input_tokens": 40468,
          "cache_creation_input_tokens": 5486,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5486
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

_source line 27_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-16 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "8ba46eef-70c5-49a1-87f2-ee95040ce7fc",
  "sessionId": "3851818f-b8a5-4456-92d9-6671bfb78776"
}
```

---

### Runtime record

_source line 28_

```json
{
  "type": "ai-title",
  "aiTitle": "Miscalibration-triggered logit steering for hallucination mitigation",
  "sessionId": "3851818f-b8a5-4456-92d9-6671bfb78776"
}
```

---

### Runtime record

_source line 29_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-16 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "8ba46eef-70c5-49a1-87f2-ee95040ce7fc",
  "sessionId": "3851818f-b8a5-4456-92d9-6671bfb78776"
}
```

---

### Runtime record

_source line 30_

```json
{
  "type": "ai-title",
  "aiTitle": "Miscalibration-triggered logit steering for hallucination mitigation",
  "sessionId": "3851818f-b8a5-4456-92d9-6671bfb78776"
}
```

---
