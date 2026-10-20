# Research conversation: You are a strict ML research reviewer conducting adversarial review. **Today's date: 2026-05-10 (UTC).** Your job: indep

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 41
- **Recorded user turns:** 1
- **Tool calls:** 7
- **Original source:** `logs/chats/exported-trajectories/account-2/0c886791-a9d9-487c-99a0-b2a7b1d3d99e.jsonl`
- **Structured JSON:** [`d66203f37f0807b404ee.json`](../../sessions/d6/d66203f37f0807b404ee.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-10T22:11:07.615Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-10T22:11:07.615Z",
  "sessionId": "0c886791-a9d9-487c-99a0-b2a7b1d3d99e",
  "content": "You are a strict ML research reviewer conducting adversarial review.\n\n**Today's date: 2026-05-10 (UTC).**\n\nYour job: independently verify this idea's claims via WebSearch, then issue a verdict.\n\n## User requirements\nThe user asked for: **Target: EMNLP 2026, ARR submission deadline 2026-05-25 (16 days from today 2026-05-09). Track: LLM Agents.\n\nDirection: LLM Agents — planning algorithms, memory architectures, tool use, multi-agent coordination, agent training (SFT/RL), self-correction in agentic loops, environment feedback exploitation.\n\nContribution type: METHOD ONLY. Must propose a concrete new algorithm, training procedure, or inference-time mechanism. Reject pure benchmark / dataset / analysis ideas. Method + analysis OK if analysis validates the method.\n\nHARD CONSTRAINTS:\n1. Compute: ≤200 H100-hours total (baselines + method + ablations). Show the math.\n2. Time: ≤16 days. Build on existing OSS agent codebases (AutoGen, LangGraph, OpenManus, etc.) — no from-scratch systems.\n3. Eval: existing benchmarks only — AgentBench, WebArena, SWE-bench Verified, GAIA, ToolBench, ALFWorld, Mind2Web, τ-bench.\n\nAvoid: generic ReAct variants, plain tool retrieval, naive memory summarization. Look for: agent training with minimal RL budget, structured planning beyond flat CoT, multi-agent communication protocols, agent self-verification mechanisms.\n\nTag: direction=agent, contribution_type=method. target_venues=[\"EMNLP 2026 Main\", \"EMNLP 2026 Findings\"].**\nYou MUST evaluate whether this idea actually meets the user's requirements. If the user asked for a top venue, assess whether the idea is truly top-venue quality. If the user asked for low resource cost, verify the resource estimate is realistic and low. An idea that doesn't match what the user asked for should be \"revise\" or \"fail\".\n\n## 核心要求：非常仔细地调研，非常仔细地思考\n\n你是一个严格的审稿人。不要轻信 Generator 的任何 claim——你必须独立验证，深入思考每个维度。\n\n### 调研要求\n\n1. **独立 SOTA 验证**：自己搜索当前 SOTA，不要只检查 Generator 的引用。\n   每个验证维度建议用 2-3 种不同的搜索查询。\n\n2. **可行性深度检查**：\n   - 搜索类似实验的实际成本/周期\n   - 检查 claimed baselines 是否可复现\n   - 验证所需的 datasets/models 是否真的可以获取\n\n3. **新颖性压力测试**：专门搜索 Generator 可能遗漏的工作：\n   - 尝试不同的关键词组合\n   - 同时检查 arXiv 和 conference proceedings\n   - 寻找相邻领域的并行/concurrent 工作\n\n4. **深入阅读**：不要只依赖搜索摘要。用 WebFetch 实际阅读相关论文的 abstract 和关键章节，形成你自己的判断。\n\n### 思考要求\n\n5. **独立判断**：\n   - 不要因为 Generator 说得有道理就轻易 pass——真正好的 idea 经得起严格审查\n   - 思考这个 idea 在实际执行中会遇到什么困难\n   - 考虑这个 idea 对领域的真实贡献（不是自说自话的贡献）\n\n6. **评分诚实**：\n   - 不要给\"看起来还行\"的 idea 高分——4 分意味着\"确实很好\"，5 分意味着\"令人兴奋\"\n   - Agent 评分经常虚高，你的职责就是纠正这种偏差\n\n充分利用你的工具——做真正的调研，不是走过场。\n\n\n## 论文搜索策略\n\n你的搜索质量直接决定了 idea 的质量。不要敷衍搜索——每一次搜索都要有明确的目的。\n\n### 搜索源（推荐每个维度使用 2 个不同来源）\n\n1. **arXiv 预印本**（最新工作）:\n   - `site:arxiv.org {topic} {year}` — 按主题搜索最新论文\n   - `site:arxiv.org {method_name}` — 按具体方法名搜索\n   - `arxiv {topic} {month} {year}` — 精确到月份，找最近 3 个月的工作\n\n2. **Google Scholar**（引用关系 + 综合覆盖）:\n   - `{topic} {year} site:scholar.google.com` — 或直接搜索让 Google 自动包含 Scholar 结果\n   - `\"{exact paper title}\"` — 验证论文是否真实存在\n   - `\"{author name}\" {topic} {year}` — 按活跃作者追踪（找到领域大牛后追踪其最新工作）\n\n3. **Papers With Code**（SOTA 排行 + 代码可用性）:\n   - `site:paperswithcode.com {task_name}` — 查看任务的 SOTA 排行榜\n   - `site:paperswithcode.com {method_name}` — 查看方法是否已被实现\n   - `paperswithcode {dataset} benchmark` — 查看特定 dataset 上的竞争格局\n\n4. **OpenReview**（会议审稿 + 同行评价）:\n   - `site:openreview.net {topic} {year}` — 搜索会议提交的论文\n   - 用 WebFetch 阅读 OpenReview 上的 reviewer comments — 了解领域专家的真实评价\n\n5. **Semantic Scholar**（语义搜索 + 引用图谱）:\n   - `semantic scholar {topic} survey {year}` — 找综述论文\n   - `semanticscholar.org {paper_title}` — 查看 cited by（谁引用了这篇）和 references（它引用了谁）\n\n6. **GitHub**（实现验证）:\n   - `site:github.com {method_name} {task}` — 验证开源实现是否存在\n   - `site:huggingface.co {model_name}` — 验证模型/数据集是否可获取\n\n### 搜索维度（多角度交叉，不要只按 topic 搜）\n\n对每个 idea/方向，尽量覆盖以下维度：\n\n1. **正向搜索**：直接搜索主题相关论文\n   - `{topic} {subtopic} {year}`\n   - `{method_name} for {task_name}`\n\n2. **竞争论文搜索**（最关键！）：\n   - `{core_problem} {year}` — 有没有人在解决同样的问题？\n   - `{approach_keyword} {task} {year}` — 有没有人用类似方法？\n   - `{gap_description} solution` — 你发现的 gap 是否已被解决？\n   - **搜索知名团队的最新工作**：如果你知道哪些团队在做这个方向，搜索他们最近 6 个月的论文\n\n3. **相邻领域搜索**：\n   - `{method_from_other_field} applied to {your_task}`\n   - `{your_problem} in {adjacent_domain}` — 其他领域是否已解决类似问题\n\n4. **反面搜索**（找到反对你 idea 的证据）：\n   - `{your_approach} limitations` / `{your_approach} failure`\n   - `why {assumed_gap} is not a problem`\n   - `{baseline_method} sufficient for {task}` — baseline 是否其实已经够好\n\n5. **引用链追踪**（发现遗漏工作的最有效方法）：\n   - 找到一篇核心相关论文后，用 WebFetch 阅读它的 references 部分\n   - 在 Semantic Scholar 上查看它的 \"cited by\" — 最近引用它的论文很可能是 concurrent work\n   - 对 3 个以上核心相关论文重复此步骤\n\n### 搜索数量建议（理想目标，上下文充裕时尽量达到）\n\n| 角色 | 建议搜索次数 | 说明 |\n|------|-------------|------|\n| Round 1 Generator | 10-15 次 | 每个方向争取 3 次独立搜索 |\n| Round 2 Generator | 5-8 次 | 验证 approach 可行性 + baseline |\n| Review Agent | 8-12 次 | 独立验证 + 竞争论文 + 反面证据 |\n| Revision Agent | 5-10 次 | 针对每个 issue 独立调研 |\n\n### 上下文管理\n\n你的输出 token 有限，必须在上下文耗尽之前完成 JSON 输出。\n\n- 上述搜索次数是理想目标。在上下文充裕时应尽量多搜、深搜，搜得越充分越好。\n- 但必须动态评估剩余上下文：如果已经消耗了大量上下文，应优先完成输出，不要为了凑次数而冒着无法输出的风险。\n- WebFetch 深度阅读很有价值，但每次 fetch 消耗大量 token——优先 fetch 最关键的 2-3 篇，而不是每篇都 fetch。\n- 质量 > 数量：5 次精准搜索 + 深度思考 > 15 次浅层搜索。\n\n\nAs a reviewer, your search focus should be:\n1. **验证 claim**：Generator 声称的 SOTA、gap、novelty 是否属实\n2. **找竞争论文**：是否有 Generator 遗漏的高度相关/相似的工作\n3. **找反面证据**：是否有论文表明 Generator 的 approach 行不通\n4. **引用链检查**：通过核心论文的 cited-by 发现 concurrent work\n\n## 竞争论文专项搜索（Reviewer 独有）\n\n这是你作为 Reviewer 最重要的职责之一——发现 Generator 遗漏的竞争工作：\n\n1. **关键词变体搜索**：用至少 3 种不同的关键词组合搜索同一个问题\n   - 同义词替换（e.g., 'efficient' → 'lightweight/fast/scalable'）\n   - 不同粒度（e.g., 'text classification' → 'sentiment analysis' → 'NLP'）\n   - 方法名 + 任务名的不同组合\n\n2. **知名团队追踪**：如果你知道哪些团队/实验室在做相关方向，\n   搜索他们最近的论文（`\"team_name\" OR \"author_name\" {topic} {year}`）\n\n3. **会议最新录用**：搜索最近一轮 ICML/NeurIPS/ICLR/AAAI/ACL 等会议的 accepted papers\n   - `site:openreview.net {topic} 2026`\n   - `{conference_name} 2026 accepted papers {topic}`\n\n4. **arXiv 近 3 个月密集搜索**：对精确相关的关键词，搜索过去 3 个月的 arXiv 论文\n   这是发现 concurrent work 最有效的窗口\n\n如果你发现了 Generator 遗漏的重要相关工作，必须在 issues 中列出论文标题和链接，\n并在 feedback 中说明这些工作如何影响 idea 的 novelty。\n\n## Review checklist\n1. **SOTA freshness**: Are the models/baselines cited actually current SOTA?\n   If outdated, specify what the current SOTA is and cite your source.\n2. **Reference verification**: Do the cited papers actually exist? (WebSearch to check)\n3. **Gap validity**: Does the claimed research gap still exist, or has recent work addressed it?\n4. **Venue validity**: Are target_venues' submission deadlines after 2026-05-10?\n5. **Feasibility**: Is the resource estimate realistic? Are there hidden dependencies?\n6. **Novelty**: Is this sufficiently different from existing work?\n   When scoring novelty < 4:\n   - You MUST identify the closest existing work(s) via WebSearch\n   - In your feedback, write: \"This idea is too similar to [Paper Title (Venue Year)]. Specifically, [what overlaps]. To differentiate, the generator should [suggestion].\"\n   - This gives the generator targeted guidance to boost novelty, not just \"be more novel\".\n7. **Cost realism across modes**: Are the three mode estimates (manual/human-in-loop/auto) internally consistent?\n   - Auto Research uses more GPU hours (2-5x manual) but GPU idle rate should be near zero\n   - Auto Research timeline should reflect resource availability as bottleneck — days with sufficient GPUs, not weeks\n   - Human-in-Loop should fall between manual and auto on most dimensions\n   - Manual and HIL must NOT include salary/wages — only GPU and API costs\n   - Auto Research must NOT include agent operational overhead\n   - If any mode estimate is clearly unrealistic, flag it\n\n## Idea under review (round 8/10)\n{\n  \"title\": \"Bilateral Intent Grounding: Extending Intra-Group Contrastive Learning from Reasoning Consistency to Multi-Agent Communication Specificity\",\n  \"core_problem\": \"Intra-group contrastive learning within GRPO has been shown to improve single-agent reasoning quality (CLIPO, March 2026; AMIR-GRPO, January 2026), but these methods address individual reasoning consistency — not inter-agent communication. In multi-agent LLM systems, text communication quality remains a bottleneck: latent methods (LatentMAS, ICML 2026; RecursiveMAS; DiffMAS; Interlat, ACL 2026) achieve +8–27% but sacrifice interpretability, while text-based multi-agent GRPO (AT-GRPO/Stronger-MAS, ICLR 2026; MAGRPO, AAAI 2026) and credit assignment approaches (C3, CCPO, CoFi-PGMA) leave message quality to emerge from sparse task reward. CoMAS (ICLR 2026) targets communication quality via LLM-as-judge scalar rewards but provides discussion-level signals without within-message differentiation or contrastive alignment. The Social Deduction LLM (AAMAS 2025) trains receiver-side prediction but is task-specific and non-contrastive. Classical MARL contrastive methods (TACTIC, AAMAS 2025; CACL, 2024) train sender-side encoding with easy negatives at small scale — and critically, TACTIC pre-trains communication modules then freezes them, never jointly training sender and receiver end-to-end. Can the intra-group contrastive mechanism demonstrated by CLIPO for reasoning consistency be adapted to a fundamentally different objective — bilateral communication grounding — where both sender message fidelity AND receiver interpretation accuracy are jointly trained end-to-end via GRPO-group hard negatives?\",\n  \"opportunity\": \"CLIPO (March 2026) and AMIR-GRPO (January 2026) established that GRPO's group sampling structure provides useful contrastive/preference signals for single-agent reasoning. However, their contrastive objectives are fundamentally different from what multi-agent communication requires. CLIPO contrasts based on OUTCOME CORRECTNESS: correct rollouts are positives, incorrect are negatives — enforcing representation consistency across successful reasoning paths. Multi-agent communication requires contrasting based on INTENT IDENTITY: a message should encode its specific sender intent, discriminating against alternative intents the same sender could have had. These are orthogonal objectives from the same structural mechanism. Moreover, CLIPO operates on a single agent — there is no receiver whose interpretation must align with the sender's intent. We identify a genuine open gap: no existing work performs end-to-end bilateral contrastive training of both LLM sender (message generation) and LLM receiver (message comprehension) within GRPO training. TACTIC (AAMAS 2025) trains both sides but pre-trains them offline then freezes during RL. Interlat (ACL 2026) stages training (receiver first, sender second). CoMAS uses scalar rewards without contrastive alignment. MAPoRL (ACL 2025) co-trains generation and comprehension but with no contrastive objective. We propose Bilateral Intent Grounding (BIG), which exploits GRPO-group negatives for a communication-specific bilateral contrastive objective: the sender loss trains messages to encode sender intent specifically; the receiver loss trains the receiver's interpretation to match sender intent accurately. Both losses use the same free GRPO-group negatives but serve different ends — and together create bidirectional grounding pressure that neither alone provides. This is most impactful in the 1.7B regime: AT-GRPO with Qwen3-1.7B achieves only 16.7% on AIME24 (vs. 50–57% with 8B), making inter-agent communication quality the dominant bottleneck. The decisive empirical question is whether BIG's bilateral communication-specific contrastive training provides orthogonal gains to CLIPO's reasoning-consistency training — if so, this demonstrates that GRPO-group contrastive learning has qualitatively different applications for communication versus reasoning, validating the domain extension.\",\n  \"landscape\": \"**Intra-group contrastive/preference learning in GRPO (established technique):** CLIPO (March 2026, arXiv 2603.10101, public code at github.com/Qwen-Applications/CLIPO) applies InfoNCE within GRPO rollout groups: correct rollouts are positives, incorrect are negatives, projected through a learned linear head. The contrastive loss is converted into auxiliary reward augmenting GRPO's standard advantage. Evaluated on math (GSM8K, MATH, AIME) with Qwen2.5-3B/7B, achieving +0.65–5.42 points. AMIR-GRPO (January 2026, arXiv 2601.03661) mines DPO-style pairwise preferences from within-group reward orderings, extracting O(G²) pairs from G completions. Both demonstrate that GRPO's group structure can be exploited for contrastive/preference objectives at zero additional sampling cost — but both target single-agent reasoning consistency, not multi-agent communication. **Latent communication (bypass text):** LatentMAS (ICML 2026 Spotlight, arXiv 2511.20639) enables training-free latent collaboration via shared hidden embeddings, achieving +14.6% accuracy. RecursiveMAS (April 2026, arXiv 2604.25917) trains RecursiveLink modules for cross-agent latent state transfer (+8.3%). DiffMAS (April 2026, arXiv 2604.21794) optimizes KV-cache communication end-to-end (+26.7% on AIME24). Interlat (ACL 2026, arXiv 2511.09149) compresses hidden states with auxiliary separation and alignment losses — notably, Interlat stages sender/receiver training (receiver first then frozen, sender second), not joint bilateral training. All bypass text communication entirely. **Text-based multi-agent GRPO (task reward only):** AT-GRPO/Stronger-MAS/PettingLLMs (ICLR 2026, arXiv 2510.11062, public code) achieves massive multi-agent gains on AIME24 (+31.7–38.7 absolute points over single-agent with Qwen3-8B) via agent-and-turn-wise GRPO in multi-agent discussion. Qwen3-1.7B achieves 16.7% on AIME24, 35.2–39.6% on OlympiadBench — substantial headroom for communication improvement. MAGRPO (AAAI 2026) trains multi-agent writing/coding. Graph-GRPO (March 2026) optimizes topology but not message content. **Communication quality training (scalar reward signals):** CoMAS (ICLR 2026, arXiv 2510.08529) targets communication quality through LLM-as-judge interaction rewards with REINFORCE++, providing discussion-level scalar signals. Evaluated on math/coding with +2–20% gains. Key distinction: CoMAS incentivizes useful communication but cannot differentiate within-message token contributions or provide contrastive alignment between specific intents. **Credit assignment:** C3 (March 2026, arXiv 2603.06859) provides message-level counterfactual credit. CCPO (March 2026, arXiv 2603.21563) estimates marginal contributions. CoFi-PGMA (April 2026, arXiv 2604.22785) derives leave-one-out rewards. Dr. MAS (Feb 2026, arXiv 2602.08847) stabilizes via agent-wise advantage normalization. All provide scalar signals without within-message differentiation or communication-specific auxiliary objectives. **Text communication training in LLM agents:** The Social Deduction LLM (AAMAS 2025, arXiv 2502.06060) trains receiver-side listening loss (task-specific imposter prediction in Among Us) and RL speaking reward. Key distinctions: receiver-side only, task-specific, non-contrastive, PPO on RWKV. MAPoRL (ACL 2025) co-trains generation and comprehension via multi-agent PPO but with no contrastive/alignment loss between agents. MaKTO (NeurIPS 2025) uses KTO for multi-agent Werewolf but no communication-specific contrastive training. **Communication auxiliary losses in classical MARL:** TACTIC (AAMAS 2025) pre-trains both sender (message generator) and receiver (message-observation integrator) via SupCon contrastive objectives — the closest to bilateral contrastive communication training, but (a) pre-trains offline then freezes during RL (not end-to-end joint training), (b) uses random/replay-buffer negatives (not GRPO-group hard negatives), (c) operates on continuous-vector messages at small scale. CACL (2024) provides sender-side only contrastive loss. Lin et al. (NeurIPS 2021) uses autoencoder reconstruction. MASIA (NeurIPS 2022) combines global-state reconstruction with attention aggregation. LangGround (NeurIPS 2024) aligns MARL communication with LLM embeddings. MAIL (IJCAI 2025) uses multi-view contrastive losses for communication graph representations. **Supporting techniques:** CLIPO's projection head architecture (linear, mean pooling). EMA-PG (Feb 2026, arXiv 2602.04417) stability theory. Robinson et al. (ICLR 2021) on hard negatives tightening MI bounds. Attention pooling (Yang et al. NAACL 2016; Lin et al. ICLR 2017). **The gap:** No existing work performs end-to-end bilateral contrastive training of both LLM sender and LLM receiver for multi-agent communication within GRPO training. CLIPO/AMIR-GRPO demonstrated the mechanism for single-agent reasoning; TACTIC demonstrated bilateral contrastive communication but offline/frozen/small-scale; CoMAS targets communication quality but via scalar rewards; Interlat/Social Deduction LLM train one side but not both jointly with contrastive alignment. BIG fills this gap: bilateral, end-to-end, contrastive, GRPO-group hard negatives, at LLM multi-agent scale.\",\n  \"approach\": \"We introduce Bilateral Intent Grounding (BIG), which extends intra-group contrastive learning — demonstrated for single-agent reasoning consistency by CLIPO (March 2026) and AMIR-GRPO (January 2026) — to multi-agent communication, with a fundamentally different contrastive objective (intent specificity rather than outcome consistency) and a novel bilateral formulation training both sender and receiver end-to-end. **Key distinction from CLIPO:** CLIPO's contrastive objective enforces OUTCOME CONSISTENCY — correct rollouts should have similar representations. BIG's contrastive objective enforces INTENT SPECIFICITY — a message should encode its sender's specific intent, and the receiver's interpretation should match that intent. CLIPO has no receiver (single-agent); BIG jointly trains both sides of the communication channel. The positives/negatives have fundamentally different semantics: CLIPO uses correct/incorrect as positive/negative; BIG uses same-intent/different-intent as positive/negative (a message's positive is the sender's intent embedding; negatives are the sender's alternative intents from other GRPO-group completions). **Bilateral formulation (core novelty):** For a given GRPO group with G completions per prompt, in completion k, agent A (sender) develops intent state e_A^k and generates message m^k, which agent B (receiver) reads to form interpretation state r_B^k. *Sender loss* trains messages to encode sender intent: L_sender = -log[exp(sim(pool(m^k), e_A^k)/τ) / Σ_j exp(sim(pool(m^k), e_A^j)/τ)], where j ranges over in-group completions. This uses GRPO-group negatives {e_A^j}_{j≠k} — same-agent, same-prompt, different-intent. *Receiver loss* trains interpretation to match sender intent: L_receiver = -log[exp(sim(r_B^k, e_A^k)/τ) / Σ_j exp(sim(r_B^k, e_A^j)/τ)]. The receiver's interpretation r_B^k is extracted as the pooled hidden state of agent B after processing message m^k. *Bidirectional grounding pressure:* Together, these create complementary training signals — the sender is incentivized to produce intent-specific messages (so the receiver loss can succeed), and the receiver is incentivized to decode intent accurately (even from imperfect messages). Neither alone achieves this: sender-only training (like CLIPO's approach applied to messages) can produce messages that are technically distinguishable but hard for a real receiver to decode; receiver-only training (like Social Deduction LLM's approach) cannot improve message quality. **Intent target extraction:** e_A = sg(EMA_τ(h_A^L)), where sg is stop-gradient and EMA (τ=0.999) provides target stabilization. Stop-gradient prevents auxiliary losses from distorting internal representations. EMA addresses the moving-target problem from continuous LoRA updates, grounded in EMA-PG stability theory (Zhang & Ba, Feb 2026). These adaptations are necessary for the multi-agent setting (multiple LoRA adapters creating cross-agent non-stationarity) but absent from CLIPO's single-agent setup. **Message/interpretation encoding:** Attention-weighted pooling (Yang et al. NAACL 2016; Lin et al. ICLR 2017): α_j = softmax(v^T·tanh(W·h_j + b)), pool = Σ_j α_j·h_j. Applied to message tokens (sender side) and receiver's post-message hidden states (receiver side). **Training:** L = L_GRPO + λ_s·L_sender + λ_r·L_receiver, with λ_s=λ_r annealed linearly from 0.2→0 over training. **Architecture:** Qwen3-1.7B with agent-specific LoRA adapters (rank=64), using PettingLLMs' existing multi-agent discussion infrastructure. The multi-agent discussion format (agents take turns proposing solutions, critiquing, and refining) naturally exposes both sender and receiver roles for each agent. The 1.7B size is deliberate: AT-GRPO with Qwen3-1.7B achieves only 16.7% on AIME24 (vs 50–57% with 8B), providing substantial headroom and ensuring communication quality is genuinely the bottleneck. **EMNLP-scoped evaluation (primary, ARR May 25 2026 — 15 days):** (1) PettingLLMs AIME multi-agent discussion with Qwen3-1.7B, five conditions: (a) AT-GRPO baseline, (b) AT-GRPO + CLIPO per-agent (existing method; improves individual reasoning consistency), (c) AT-GRPO + BIG sender-only (ablation: matches CLIPO's structure but with intent-specificity objective for communication), (d) AT-GRPO + BIG bilateral (full method: sender + receiver losses), (e) AT-GRPO + CLIPO + BIG bilateral (complementarity test). The decisive experiment is (b) vs (d) vs (e): if BIG bilateral provides gains beyond CLIPO, this demonstrates that communication-specific bilateral contrastive training provides orthogonal value to reasoning-consistency training — validating the domain extension. The (c) vs (d) comparison isolates the bilateral component's contribution. (2) Ablation: BIG bilateral with group negatives vs random negatives (tests whether GRPO-group hard negatives matter for communication specifically). (3) Ablation: BIG bilateral without stop-gradient isolation (tests necessity of multi-agent stability mechanism). (4) Qualitative analysis: attention-entropy comparison showing BIG bilateral produces messages with higher intent specificity (concentrated attention on intent-carrying tokens) vs CLIPO (diffuse attention reflecting general reasoning quality). Total EMNLP compute: ~55h H100. **AAAI 2027 extended evaluation (expected ~Aug 2026):** All EMNLP experiments plus: (1) OlympiadBench multi-agent (AT-GRPO 1.7B baseline: 35.2–39.6%, providing additional headroom). (2) BIG-R (Reconstruction) ablation — non-contrastive bilateral variant using MSE reconstruction loss on both sender and receiver sides. (3) Composability: BIG + C3 (complementary within-message bilateral vs between-message counterfactual credit). (4) Analysis of when bilateral > sender-only: hypothesis that bilateral advantage increases with task difficulty (harder problems require more precise communication). (5) λ annealing ablation: constant 0.1 vs linear 0.2→0. Total AAAI compute: ~120h H100.\",\n  \"resource_estimate\": {\n    \"emnlp_scoped\": {\n      \"gpu_hours\": \"~55h H100 (AT-GRPO baseline: ~10h; CLIPO per-agent: ~12h; BIG sender-only: ~10h; BIG bilateral: ~10h; CLIPO + BIG bilateral: ~5h [warm-start from CLIPO]; group-vs-random ablation: ~5h; stop-gradient ablation: ~3h)\",\n      \"gpu_utilization\": \"High (75–90%): uses PettingLLMs existing infrastructure with minimal modification\",\n      \"timeline\": \"15 days (May 10–25, 2026): Days 1–3 implementation (integrate BIG losses into PettingLLMs AT-GRPO training loop — infrastructure already handles multi-agent discussion for AIME, add intent extraction with stop-gradient/EMA, add sender/receiver InfoNCE losses, integrate CLIPO baseline using their public code); Days 4–10 experiments (5 conditions + 2 ablations, parallelizable across 2 GPUs); Days 11–15 analysis + paper writing\",\n      \"team\": \"1 researcher with RL + multi-agent expertise (full-time 15 days)\",\n      \"estimated_gpu_cost\": \"$138–165 (at ~$2.50–3.00/GPU-hr)\",\n      \"execution_risk\": \"Moderate (~35–45% chance of competitive submission). Reduced from original proposal because: (a) PettingLLMs already supports AIME multi-agent discussion natively (no ALFWorld adaptation needed); (b) CLIPO public code provides the projection head baseline directly; (c) BIG implementation adds two InfoNCE losses to existing infrastructure (conceptually straightforward). Primary risks: (a) bilateral loss may not provide gains over sender-only (the bilateral contribution is the core novelty — if sender-only matches bilateral, the contribution weakens to 'CLIPO for communication'); (b) CLIPO + BIG may not stack (if gains are redundant rather than orthogonal, the complementarity argument fails). Mitigations: sender-only vs bilateral ablation is fast to run (same infrastructure, toggle one loss); if bilateral doesn't help, the paper can pivot to analyzing WHY communication-specific contrastive training differs from reasoning-specific (negative result paper).\",\n      \"what_is_preserved\": \"CLIPO direct comparison, bilateral vs sender-only ablation, complementarity test, group-vs-random ablation, stop-gradient necessity test\",\n      \"what_is_sacrificed\": \"OlympiadBench (second benchmark), BIG-R ablation, C3 composability, detailed per-difficulty analysis\"\n    },\n    \"aaai_extended\": {\n      \"gpu_hours\": \"~120h H100 (EMNLP experiments: ~55h; OlympiadBench [all conditions]: ~30h; BIG-R ablation: ~10h; C3 composability: ~10h; per-difficulty analysis: ~5h; λ annealing: ~5h; buffer: ~5h)\",\n      \"gpu_utilization\": \"High (65–80%): parallelizable across multiple GPUs\",\n      \"timeline\": \"10–12 weeks (May–Aug 2026)\",\n      \"team\": \"1–2 researchers\",\n      \"estimated_gpu_cost\": \"$300–360 (at ~$2.50–3.00/GPU-hr)\"\n    }\n  },\n  \"target_venues\": [\n    \"EMNLP 2026 (ARR May 25, 2026) — PRIMARY TARGET: focused on bilateral intent grounding with direct CLIPO comparison. The contribution is clearly scoped: extending intra-group contrastive learning from reasoning to communication via a novel bilateral formulation, with empirical validation of orthogonality. ~55h compute, 15-day execution. Engineering risk is substantially reduced (PettingLLMs native AIME support + CLIPO public code). Scientific risk remains (bilateral must outperform sender-only).\",\n    \"AAAI 2027 (expected abstract ~Jul 25 2026, full paper ~Aug 1 2026) — EXTENDED VERSION: adds OlympiadBench, BIG-R ablation, C3 composability, per-difficulty analysis. If EMNLP is rejected, AAAI provides 12 weeks for the complete program with additional benchmarks.\",\n    \"ICLR 2027 (expected ~Oct 2026) — further fallback with additional time for deeper analysis\"\n  ],\n  \"level\": \"solid\",\n  \"key_references\": [\n    \"CLIPO: Contrastive Learning in Policy Optimization Generalizes RLVR (March 2026, arXiv 2603.10101, public code github.com/Qwen-Applications/CLIPO)\",\n    \"AMIR-GRPO: Inducing Implicit Preference Signals into GRPO (January 2026, arXiv 2601.03661)\",\n    \"Latent Collaboration in Multi-Agent Systems — LatentMAS (ICML 2026 Spotlight, arXiv 2511.20639)\",\n    \"Recursive Multi-Agent Systems — RecursiveMAS (April 2026, arXiv 2604.25917)\",\n    \"Learning to Communicate: Toward End-to-End Optimization — DiffMAS (April 2026, arXiv 2604.21794)\",\n    \"Enabling Agents to Communicate Entirely in Latent Space — Interlat (ACL 2026, arXiv 2511.09149)\",\n    \"CoMAS: Co-Evolving Multi-Agent Systems via Interaction Rewards (ICLR 2026, arXiv 2510.08529)\",\n    \"Training Language Models for Social Deduction with Multi-Agent RL — Social Deduction LLM (AAMAS 2025, arXiv 2502.06060)\",\n    \"Stronger-MAS: Multi-Agent Reinforcement Learning for Collaborative LLMs — AT-GRPO/PettingLLMs (ICLR 2026, arXiv 2510.11062, public code github.com/pettingllms-ai/PettingLLMs)\",\n    \"LLM Collaboration with Multi-Agent RL — MAGRPO (AAAI 2026)\",\n    \"Task-Agnostic Contrastive Pre-Training for Communication — TACTIC (AAMAS 2025)\",\n    \"Learning Multi-Agent Communication with Contrastive Learning — CACL (2024, arXiv 2307.01403)\",\n    \"Multi-Agent Communication with Information Preserving — MAIL (IJCAI 2025)\",\n    \"Contrastive Learning with Hard Negative Samples — Robinson et al. (ICLR 2021, arXiv 2010.04592)\",\n    \"EMA Policy Gradient: Taming RL for LLMs with EMA Anchor — EMA-PG (Feb 2026, arXiv 2602.04417)\",\n    \"Dr. MAS: Stable RL for Multi-Agent LLM Systems (Feb 2026, arXiv 2602.08847)\",\n    \"C3: Contextual Counterfactual Credit Assignment (March 2026, arXiv 2603.06859)\",\n    \"CCPO: Counterfactual Credit Policy Optimization (March 2026, arXiv 2603.21563)\",\n    \"CoFi-PGMA: Counterfactual Policy Gradients for Multi-Agent LLMs (April 2026, arXiv 2604.22785)\",\n    \"Graph-GRPO: Stabilizing Multi-Agent Topology Learning (March 2026, arXiv 2603.02701)\",\n    \"CoDA: Context-Decoupled Hierarchical Agent with RL (WSDM 2026, arXiv 2512.12716, code github.com/liuxuanzhang718/CoDA)\",\n    \"MAPoRL: Multi-Agent Post-Co-Training for Collaborative LLMs (ACL 2025)\",\n    \"MaKTO: Multi-agent Kahneman-Tversky Optimization (NeurIPS 2025)\",\n    \"Learning to Ground Multi-Agent Communication with Autoencoders — Lin et al. (NeurIPS 2021)\",\n    \"Efficient Multi-agent Communication via Self-supervised Information Aggregation — MASIA (NeurIPS 2022)\",\n    \"Language Grounded Multi-agent RL — LangGround (NeurIPS 2024)\",\n    \"Hierarchical Attention Networks — Yang et al. (NAACL 2016)\",\n    \"A Structured Self-Attentive Sentence Embedding — Lin et al. (ICLR 2017)\",\n    \"Reinforcement Learning for LLM-based MAS through Orchestration Traces (May 2026, arXiv 2605.02801)\",\n    \"Beyond Self-Talk: A Communication-Centric Survey of LLM-Based MAS (arXiv 2025)\"\n  ],\n  \"description\": \"We introduce Bilateral Intent Grounding (BIG), which extends intra-group contrastive learning — established for single-agent reasoning consistency by CLIPO (March 2026) and AMIR-GRPO (January 2026) — to multi-agent communication with a fundamentally different objective and a novel bilateral formulation. CLIPO demonstrated that GRPO's group sampling provides useful contrastive signals by contrasting correct vs incorrect rollouts to enforce reasoning trajectory consistency. BIG repurposes the same structural mechanism for a different goal: intent-specific communication. The contrastive semantics differ fundamentally — CLIPO uses outcome correctness (correct/incorrect) as the positive/negative criterion; BIG uses intent identity (same-intent/different-intent) — and BIG introduces bilateral training absent from all prior work. The sender loss trains messages to faithfully encode sender intent (InfoNCE with GRPO in-group alternative intents as hard negatives). The receiver loss — the core novelty — trains the receiver's interpretation to accurately decode sender intent using the same GRPO-group negatives. This bilateral pressure creates a virtuous cycle: senders produce more specific messages because receivers are trained to discriminate, and receivers improve because senders provide more decodable signals. No existing work achieves this: CLIPO has no receiver (single-agent); TACTIC (AAMAS 2025) pre-trains both sides but freezes during RL; Interlat (ACL 2026) stages training sequentially; CoMAS (ICLR 2026) uses scalar rewards without contrastive alignment; MAPoRL (ACL 2025) co-trains but without contrastive objectives. The multi-agent setting also requires domain-specific adaptations absent from CLIPO: stop-gradient isolation and EMA target stabilization (grounded in EMA-PG, Feb 2026) to handle cross-agent LoRA non-stationarity, and cross-agent negative pairs for inter-role discrimination. Architecture: Qwen3-1.7B with agent-specific LoRA (rank=64), built on PettingLLMs' existing multi-agent discussion infrastructure for AIME. The 1.7B regime is deliberate: AT-GRPO achieves only 16.7% on AIME24 at this scale (vs 50–57% with 8B), providing substantial headroom where communication quality is genuinely the bottleneck. **EMNLP-scoped submission (ARR May 25, 15 days):** Five conditions on AIME multi-agent discussion — AT-GRPO baseline, CLIPO per-agent (using their public code), BIG sender-only, BIG bilateral, CLIPO + BIG bilateral. The decisive experiments: (1) BIG bilateral vs CLIPO per-agent tests whether communication-specific contrastive training provides orthogonal value to reasoning-consistency training; (2) BIG bilateral vs BIG sender-only isolates the bilateral contribution; (3) CLIPO + BIG bilateral tests complementarity (if gains stack, the objectives are truly orthogonal). Ablations: group-vs-random negatives, stop-gradient necessity. ~55h H100, substantially reduced engineering risk (PettingLLMs native + CLIPO public code). **AAAI 2027 extended version (~Aug 2026):** Adds OlympiadBench, BIG-R (reconstruction) ablation, C3 composability, per-difficulty bilateral advantage analysis. ~120h H100.\",\n  \"project_name\": \"recon_reg_comm_training\",\n  \"source\": \"web_research\"\n}\n\n\n## Previous review history\n### Round 1 review\nVerdict: revise\nIssues: [\"COMPUTE BUDGET VIOLATION: User's hard constraint is ≤200 H100-hours. The lowest estimate (manual mode, 250h) already exceeds this by 25%. The 120h 'single training run' claim likely underestimates multi-agent GRPO with a decoder, environment rollouts, and cooperative task setup. With ablations and baselines, 200h is unachievable for the proposed scope.\", \"EVAL BENCHMARK VIOLATION: 'Cooperative ALFWorld variants (custom 2-agent role-split tasks)' is NOT an existing benchmark — ALFWorld is single-agent. Creating custom cooperative tasks violates the user's 'existing benchmarks only' constraint. DEPART/HIMPO already uses standard ALFWorld for hierarchical multi-agent evaluation without requiring custom cooperative variants.\", \"CRITICAL MISSING CITATION: Lin et al. (NeurIPS 2021) 'Learning to Ground Multi-Agent Communication with Autoencoders' uses the exact same core mechanism — autoencoder reconstruction of sender state from communication messages to ground multi-agent communication. This is not cited and directly undercuts the novelty claim that reconstruction-regularized communication training is new.\", \"COMPETING WORK NOT ADDRESSED: MAPoRL (ACL 2025) explicitly trains communication quality in multi-agent LLM RL through influence-aware verification rewards that incentivize corrective and persuasive discussions. C3 (arXiv March 2026) provides message-level counterfactual credit assignment. The generator's claim that 'no existing method explicitly trains communication quality' is factually incorrect.\", \"DEPART/HIMPO (OpenReview 2025-2026) trains hierarchical planner-executor multi-agent systems with role-specific rewards on ALFWorld benchmarks, directly overlapping with the proposed evaluation setting and partially with the training approach (role-specific reward shaping).\", \"UNVERIFIABLE REFERENCE: 'Detecting and Repairing Role Drift in Multi-Agent Collaboration with Lightweight Protocols (Preprint 2026)' — I could not independently verify a paper titled 'RoleFix' or with this exact title. Search returns AgentFixer and various drift detection works, but not this specific paper.\", \"TIMELINE INFEASIBILITY: 16 days to design custom cooperative environments, implement the reconstruction decoder, integrate with PettingLLMs/VeRL, train with GRPO, run ablations, implement baselines (AT-GRPO, Graph-GRPO), and write the paper. Even with existing infrastructure, this scope is unrealistic for EMNLP ARR May 25.\", \"TECHNICAL CONCERN: Extracting 'intent embeddings' (last hidden state before message generation) during multi-agent GRPO rollouts with LoRA is non-trivial. The sender's internal representation changes as LoRA adapters are updated, creating a moving-target problem for the decoder. This interaction between the reconstruction loss gradient and the GRPO policy gradient is not analyzed.\"]\nFeedback: The general direction of improving communication quality in multi-agent LLM training is valid and timely, but the current proposal has critical issues that must be addressed:\n\n1. **Novelty repositioning required**: You MUST cite and differentiate from Lin et al. (NeurIPS 2021) 'Learning to Ground Multi-Agent Communication with Autoencoders,' MAPoRL (ACL 2025), and C3 (March 2026). The claim that 'no existing method explicitly trains communication quality' is false. Reposition: what does reconstruction-based regularization offer OVER verifier-based rewards (MAPoRL) and counterfactual credit (C3)? A concrete hypothesis: reconstruction loss provides denser gradient signal per message than outcome-based rewards, especially in early training when task success is rare.\n\n2. **Fix the compute budget**: The user's hard constraint is ≤200 H100-hours. Options: (a) reduce to a 2-3B model (Qwen3.5-2B) with LoRA, which should cut training time by ~3-4x; (b) limit ablations to 2-3 key ones (λ_recon sweep, decoder vs. no-decoder, reconstruction vs. MAPoRL-style reward); (c) use the Stronger-MAS planning benchmarks (Sudoku, Sokoban, Plan-Path) which are already multi-agent and require no custom environment engineering.\n\n3. **Use EXISTING multi-agent benchmarks ONLY**: Drop cooperative ALFWorld variants entirely. Use Stronger-MAS planning tasks (already 2+ agent, role-split compatible, with AT-GRPO baselines for direct comparison). Supplement with MAGRPO's writing/coding collaboration benchmarks. This eliminates environment engineering time AND satisfies the user's constraint.\n\n4. **Sharpen the technical contribution**: The reconstruction decoder training dynamics during GRPO need analysis. Address: (a) how does the reconstruction target (intent embedding) evolve as LoRA weights update? (b) does the decoder need to be periodically re-initialized? (c) what is the gradient interaction between L_recon and L_GRPO? Without this analysis, the method appears ad-hoc.\n\n5. **Target AAAI 2027 or ICLR 2027 instead of EMNLP**: The 16-day timeline is unrealistic for the required scope. With AAAI 2027 (expected ~Aug 2026), you gain 2-3 months for proper experimentation.\n\n### Round 2 review\nVerdict: revise\nIssues: [\"EVAL BENCHMARK CONSTRAINT VIOLATION: The user's hard constraint specifies allowed benchmarks: AgentBench, WebArena, SWE-bench Verified, GAIA, ToolBench, ALFWorld, Mind2Web, τ-bench. The proposal uses Stronger-MAS benchmarks (Sudoku 4x4, Plan-Path 10x10) and CoopHumanEval — NONE of which are in the allowed list. While these are legitimate published benchmarks (ICLR 2026 and AAAI 2026), they do not satisfy the user's explicit constraint.\", \"COOPHUMANEVAL MISMATCH: CoopHumanEval (from MAGRPO) uses role-based code cooperation where agents generate helper functions and main functions without inter-agent message passing. SGIR's core mechanism — reconstruction of sender intent from inter-agent messages — is fundamentally inapplicable to this benchmark. The agents don't send messages to each other; they share code outputs.\", \"MISSING CRITICAL CONCURRENT WORK (5 papers): (1) LatentMAS (ICML 2026 Spotlight, arXiv 2511.20639) — agents communicate through latent hidden-state representations, directly adjacent to SGIR's intent embedding approach. (2) RecursiveMAS (April 2026, arXiv 2604.25917) — RecursiveLink module transfers hidden representations between agents in latent space. (3) CCPO (March 2026, arXiv 2603.21563) — counterfactual credit policy optimization with agent-specific marginal contribution estimation. (4) CoFi-PGMA (April 2026, arXiv 2604.22785) — counterfactual policy gradients for multi-agent LLMs with leave-one-out credit. (5) Dr. MAS (Feb 2026, arXiv 2602.08847) — stable multi-agent GRPO via agent-wise advantage normalization, directly relevant as it addresses GRPO training stability.\", \"OVERSTATED PREMISE — LIN ET AL. GRADIENT CONFLICT: The proposal claims Lin et al. (NeurIPS 2021) found a 'fundamental conflict between reconstruction gradients and RL policy gradients' causing degraded task performance. This mischaracterizes their findings. Lin et al.'s paper shows autoencoding 'is sufficient for arriving at a grounded common language' with 'surprisingly strong task performance,' and their project page confirms the model 'consistently outperforms baselines.' While some tension between losses exists, characterizing it as a 'fundamental conflict' that SGIR uniquely resolves is an overstatement that weakens the core contribution's motivation. Similarly, claiming LangGround 'abandoned reconstruction entirely' due to this conflict is misleading — LangGround chose language embedding alignment primarily for human interpretability in ad-hoc teamwork.\", \"VENUE DEVIATION: The user specifically requested EMNLP 2026 (ARR deadline May 25, 2026). The proposal targets AAAI 2027 and ICLR 2027 instead. While pragmatic (16 days is infeasible for a training-based method paper), this does not match the user's stated requirement. The user's track specification was 'LLM Agents' which aligns with EMNLP, making the venue switch a substantive deviation.\", \"TECHNICAL RISK — DECODER MOVING-TARGET PROBLEM: The reconstruction decoder D_φ must learn to predict hidden states that change as LoRA adapters are updated during GRPO training. With λ annealing from 0.5 to 0, the decoder's target distribution shifts continuously. The proposal does not analyze whether the decoder can track this moving target or whether periodic re-initialization is needed. This is not just a theoretical concern — it directly affects whether the 'dense gradient signal' claim holds in practice.\"]\nFeedback: The revised proposal shows significant improvement over Round 1 (compute budget addressed, custom environments dropped, better landscape coverage), but several critical issues remain:\n\n1. **Fix benchmark compliance**: The user's allowed benchmarks are all primarily single-agent, creating a genuine tension with multi-agent methods. Two options: (a) Use ALFWorld (on the allowed list) with a DEPART/HIMPO-style planner-executor multi-agent setup — this involves message passing and is established in the literature. (b) Acknowledge the tension explicitly and argue that Stronger-MAS benchmarks are the appropriate community-standard multi-agent benchmarks with published baselines, while also providing at least one evaluation on a user-listed benchmark. Drop CoopHumanEval entirely — it uses code-level cooperation without messages, making SGIR inapplicable.\n\n2. **Correct the Lin et al. premise**: Don't overstate the gradient conflict. Instead, reframe: 'Lin et al. showed reconstruction works in small MARL networks. However, scaling reconstruction-based grounding to LLM-scale multi-agent RL introduces new challenges: (a) the LoRA adapter updates create a moving target for the decoder, (b) the high-dimensional hidden states of LLMs make naive reconstruction infeasible, requiring architectural choices. Stop-gradient detachment is one principled approach to manage these scaling challenges.' This is more honest and still provides motivation.\n\n3. **Cite and differentiate from LatentMAS and RecursiveMAS**: These are the closest concurrent works — both pass hidden representations between agents. Key differentiation: LatentMAS/RecursiveMAS REPLACE text communication with latent communication (inference-time mechanism), while SGIR AUGMENTS text communication with reconstruction-based training signal (training-time mechanism). SGIR preserves human-readable inter-agent messages. Also cite Dr. MAS, CCPO, and CoFi-PGMA for completeness.\n\n4. **Address the moving-target problem**: Add a fourth ablation: periodic decoder re-initialization vs. continuous training. Or analyze theoretically why the stop-gradient ensures the target distribution changes slowly enough for the decoder to track. This would strengthen the technical contribution significantly.\n\n5. **Consider meeting the EMNLP deadline**: If EMNLP 2026 is truly the target, scope down radically — 1 benchmark (Stronger-MAS Sudoku), 1 ablation (stop-gradient vs. joint), no CoopHumanEval. But realistically, targeting AAAI 2027 (expected Aug 2026 deadline) with the fuller experimental plan is more appropriate.\n\n### Round 3 review\nVerdict: revise\nIssues: [\"MISLEADING PER-TOKEN CLAIM: The core selling point — 'dense per-token supervision' — is technically inaccurate. With mean-pooling: L_recon = ||D_φ(pool(m)) - e_i||², the gradient ∂L/∂m_j = (1/T) · ∂L/∂pool(m) is identical for all tokens j. Every token receives the same gradient magnitude, making this effectively MESSAGE-LEVEL supervision, not per-token. To achieve genuine per-token differentiation, the proposal would need attention-weighted pooling or per-token reconstruction targets. This claim must be corrected or the pooling mechanism changed.\", \"MISSING CONCURRENT WORK — DiffMAS (arXiv 2604.21794, April 2026): 'Learning to Communicate: Toward End-to-End Optimization of Multi-Agent Language Systems' by Yu et al. (UIUC). DiffMAS optimizes inter-agent communication end-to-end via KV-cache transfer with LoRA adapters, achieving +26.7% on AIME24. While DiffMAS operates in latent space (no text), it directly addresses the same motivation (optimizing multi-agent communication quality) and must be cited and differentiated.\", \"MISSING CITATION — EMA Policy Gradient (arXiv 2602.04417, Feb 2026): Zhang & Ba provide theoretical stability conditions for using EMA anchors in GRPO-like training. Since SGIR's EMA target stabilization (τ=0.999) is a core technical contribution, this paper's stability analysis should be cited to provide theoretical grounding. Without it, the EMA design choice appears under-motivated.\", \"BENCHMARK PARTIAL COMPLIANCE: ALFWorld is on the user's allowed list (good). Stronger-MAS Sudoku 4x4 is NOT on the allowed list (AgentBench, WebArena, SWE-bench Verified, GAIA, ToolBench, ALFWorld, Mind2Web, τ-bench). The proposal acknowledges this implicitly by calling Sudoku a 'community-standard benchmark.' Consider replacing Sudoku with a second allowed-list benchmark or providing explicit justification for the deviation.\", \"THIN EVALUATION FOR TOP VENUE: Two benchmarks — ALFWorld (planner-executor) and Sudoku 4x4 (toy cooperative) — may be insufficient for AAAI 2027. ALFWorld is a good choice, but Sudoku 4x4 is very small-scale (4x4 grid, 2 agents). Reviewers will question generalization. Adding a third benchmark (e.g., from AgentBench or τ-bench multi-agent configurations) or scaling to 6x6 Sokoban (also in Stronger-MAS) would strengthen the experimental section.\", \"VENUE DEVIATION: The user explicitly requested EMNLP 2026 (ARR deadline May 25, 2026). The proposal targets AAAI 2027 (Aug 1, 2026) and ICLR 2027 (~Oct 2026). This follows Round 1-2 reviewer recommendations but still does not satisfy the user's stated constraint. If maintaining AAAI 2027 targeting, the proposal should explicitly acknowledge this deviation and justify why the expanded timeline enables stronger results.\"]\nFeedback: The proposal has improved substantially across Rounds 1-3 — references are now comprehensive and verified, the Lin et al. characterization is honest, benchmark compliance is partially addressed, and the landscape is thorough. Three specific actions to reach pass quality:\n\n1. **Fix the per-token claim or the mechanism**: This is the most important issue. Either (a) replace mean-pooling with attention-weighted pooling where learned attention weights differentiate token contributions, making per-token supervision genuine, or (b) reframe the claim honestly as 'dense message-level supervision' and argue why per-message reconstruction is superior to sparse task reward (which it is — you get a training signal for every message, not just at episode end). Option (a) adds novelty; option (b) sacrifices a selling point but gains integrity.\n\n2. **Cite and differentiate from DiffMAS and EMA-PG**: DiffMAS (arXiv 2604.21794) is the closest concurrent work — differentiate by emphasizing SGIR preserves text (interpretability) while DiffMAS replaces it with KV-cache (performance). EMA-PG (arXiv 2602.04417) provides theoretical grounding for SGIR's EMA choice — cite its stability conditions and connect them to your τ=0.999 design.\n\n3. **Strengthen evaluation scope**: Add at least one more evaluation dimension. Options: (a) scale to Sokoban 6x6 from Stronger-MAS (minimal additional effort, same codebase); (b) add a qualitative analysis of message quality improvement (human evaluation of planner messages in ALFWorld — shows interpretability advantage concretely); (c) compare SGIR message quality against LatentMAS's latent communication on a shared benchmark to directly test the 'close the gap while preserving text' hypothesis. Option (c) would be the strongest contribution but highest effort.\n\nMinor: The DEPART shared-weights architecture means your 'planner' and 'executor' share base model weights with different LoRA adapters. This is fine technically but should be stated explicitly — reviewers familiar with DEPART will notice if you imply separate models.\n\n### Round 4 review\nVerdict: revise\nIssues: [\"MISSING CITATION — MASIA (NeurIPS 2022): 'Efficient Multi-agent Communication via Self-supervised Information Aggregation' (Guan et al.) uses reconstruction loss (reconstructing global state from messages) combined with attention-based message extraction in multi-agent communication. This is a direct precursor combining two of SGIR's core components (reconstruction + attention aggregation) and must be cited and differentiated.\", \"OVERSTATED ATTENTION POOLING NOVELTY: The attention-weighted pooling mechanism (α_j = softmax(v^T·tanh(W·h_j+b))) is the standard Hierarchical Attention Network formula from Yang et al. (NAACL 2016) and Lin et al. (ICLR 2017). Framing it as 'genuine per-token gradient differentiation' obscures that this is a trivially standard architectural choice. The gradient analysis also omits the softmax Jacobian redistribution term (∂α_k/∂h_j contributions), making the mechanism appear cleaner than it actually is.\", \"MISSING CONCURRENT WORK — Interlat (arXiv 2511.09149, revised April 2026): 'Enabling Agents to Communicate Entirely in Latent Space' by Du et al. proposes inter-agent communication via continuous last hidden states with learned compression. This is another latent communication method that should be in the landscape for completeness.\", \"NARROW NOVELTY GAP: The contribution reduces to 'apply stop-gradient + EMA to make reconstruction work at LLM scale' — the attention pooling is standard, the reconstruction idea is from Lin et al. 2021, and the EMA design is borrowed from EMA-PG. Each 'challenge' at LLM scale is addressed by a known technique. This risks the 'engineering combination' critique at top venues where reviewers expect conceptual novelty.\", \"UNCERTAIN EMPIRICAL IMPACT: No preliminary evidence suggests reconstruction can meaningfully close the text-latent performance gap. If LatentMAS achieves +14.6% by bypassing text and SGIR achieves +2-3% while preserving text, the contribution becomes 'we traded most of the performance for interpretability' — which may not be compelling without a strong interpretability analysis showing concrete debugging/safety benefits.\", \"VENUE DEVIATION PERSISTS: User requested EMNLP 2026 (ARR May 25). Proposal targets AAAI 2027 (Aug 1). While acknowledged and justified, this still does not meet the user's stated constraint.\"]\nFeedback: The proposal has improved substantially over 4 rounds — landscape is now comprehensive, references are verified, benchmark compliance is mostly addressed, and the technical mechanism is clarified. Three specific actions to reach pass quality:\n\n1. **Cite MASIA (NeurIPS 2022) and reframe the novelty narrative**: MASIA already combines reconstruction + attention for multi-agent communication messages. Your differentiation: MASIA reconstructs *global state* from messages in small MARL; SGIR reconstructs *sender intent embeddings* from messages at *LLM scale* with *stop-gradient + EMA* to handle LoRA-induced moving targets. The novelty is NOT attention pooling (standard since 2016) — it's the full architectural framework (stop-gradient isolation + EMA stabilization + λ annealing) that makes reconstruction work in the LLM-GRPO setting where naive approaches fail.\n\n2. **Strengthen the impact argument with concrete interpretability value**: The 'preserve text for interpretability' argument is currently abstract. Make it concrete: (a) include a failure-mode analysis showing how SGIR-trained messages help debug agent errors that latent communication cannot, (b) show that SGIR attention weights identify which tokens carry intent (a free interpretability tool), (c) demonstrate human-in-the-loop intervention scenarios where text messages enable real-time correction. This converts the interpretability claim from a philosophical argument into a demonstrated advantage.\n\n3. **Consider a direct text-vs-latent comparison**: On one benchmark (e.g., ALFWorld), run both LatentMAS (training-free, so cheap to evaluate) and SGIR. If SGIR achieves 70-80% of LatentMAS's gains while preserving readable messages, that's a compelling result. If it achieves only 10-20%, you need the interpretability argument to be ironclad. Having this comparison in hand before writing would let you frame the contribution appropriately.\n\nMinor: fix the gradient analysis to acknowledge the softmax Jacobian term, or simply state 'the dominant gradient term is α_j-weighted' without claiming strict proportionality.\n\n### Round 5 review\nVerdict: revise\nIssues: [\"COMPUTE BUDGET VIOLATION (PERSISTENT): User's hard constraint is ≤200 H100-hours. All three modes exceed this: manual 230h (+15%), human-in-loop 250h (+25%), auto 280h (+40%). This was flagged in Round 1 and remains unfixed after 5 rounds. The proposal must either cut scope or demonstrate that the budget math is achievable within 200h.\", \"BENCHMARK NON-COMPLIANCE: Sokoban 6x6 is NOT on the user's allowed benchmark list (AgentBench, WebArena, SWE-bench Verified, GAIA, ToolBench, ALFWorld, Mind2Web, τ-bench). ALFWorld and WebArena-Lite are compliant, but the third benchmark must be replaced with one from the allowed list.\", \"DEPART/HIMPO CODE UNAVAILABILITY: Multiple searches confirm no public code release for DEPART/HIMPO. The proposal depends on 'DEPART-style planner-executor architecture' for ALFWorld and WebArena-Lite evaluation. Without code, this architecture must be reimplemented, adding significant engineering effort within the already-tight timeline. This risk is not acknowledged in the resource estimate.\", \"MISSING CITATION — Social Deduction LLM (arXiv 2502.06060, Feb 2025): 'Training Language Models for Social Deduction with Multi-Agent RL' explicitly trains text message quality in multi-agent LLM RL by decomposing communication into a 'listening' loss (predicting world state from messages — functionally a reconstruction objective on the receiver side) and an RL 'speaking' reward based on how messages shift other agents' beliefs. This is the closest prior work in the LLM-text domain and must be cited and differentiated.\", \"VENUE DEVIATION (PERSISTENT): User explicitly requested EMNLP 2026 (ARR May 25, 2026). Proposal targets AAAI 2027 (Aug 1, 2026). While the timeline justification is sound (16 days is genuinely infeasible for 230+ GPU-hours with human interpretability evaluation), this remains a hard constraint violation. The proposal should either (a) provide a scoped-down EMNLP-feasible variant or (b) explicitly accept that the idea does not meet the user's venue requirement.\", \"ENGINEERING COMBINATION RISK: The novelty narrative has improved substantially, but the core contribution — applying stop-gradient + EMA + attention pooling to make reconstruction/contrastive losses work at LLM-GRPO scale — risks the 'competent engineering' critique at top venues. The GRPO-group hard negatives are genuinely novel but constitute one technique within a larger framework of borrowed components. Reviewers at AAAI/ICLR may ask: 'What is the conceptual insight beyond careful engineering?'\", \"INTERPRETABILITY STUDY COMPLEXITY: The proposed interpretability evaluation (failure diagnosis study, attention-intent correlation with human annotations, human-in-the-loop correction experiments) is ambitious and valuable but adds substantial non-compute costs: annotation protocol design, 20+ person-hours of human annotation, and potential IRB considerations. These are not reflected in the timeline or cost estimates for any mode.\"]\nFeedback: The proposal has improved dramatically over 5 rounds — the landscape is now among the most comprehensive I've seen, references are verified, and the technical framing is mostly honest. Three changes would bring this to pass quality:\n\n1. **FIT WITHIN 200 H100-HOURS (MANDATORY)**: This is the user's hard constraint and has been violated for 5 rounds. Concrete path: (a) Drop Sokoban entirely — it's not on the allowed list anyway, saving ~45h. (b) Reduce ablations to the 3 most critical: IGCT-R vs IGCT-C vs combined, stop-gradient necessity, and λ annealing — saving ~15h. (c) This gives ~170h (70h ALFWorld + 55h WebArena-Lite + 5h LatentMAS baseline + 15h composability + 25h reduced ablations), safely within budget. The Sokoban controlled-comparison is nice-to-have but dispensable — AT-GRPO baselines can be cited without reproduction.\n\n2. **REPLACE SOKOBAN WITH AN ALLOWED-LIST BENCHMARK OR DROP TO TWO**: Options: (a) Drop Sokoban and run ALFWorld + WebArena-Lite (both allowed, sufficient for a methods paper). (b) Replace with τ-bench (from the allowed list) which involves multi-turn agent-human interaction and could showcase IGCT's interpretability advantage. (c) Add an AgentBench subset if a third benchmark is needed for generalization claims.\n\n3. **CITE THE SOCIAL DEDUCTION LLM PAPER AND DIFFERENTIATE**: arXiv 2502.06060 trains text message quality via a prediction loss + RL reward. Key differentiation: Social Deduction uses a receiver-side prediction loss (can the receiver extract world state from the message?) while IGCT uses a sender-side intent reconstruction loss (does the message faithfully convey sender intent?). Social Deduction also lacks contrastive alignment and GRPO-group hard negatives. Add this to the landscape and explain why sender-intent grounding is superior to receiver-side prediction for multi-agent coordination.\n\nMinor improvements: (a) Address DEPART code unavailability — either contact authors for code or describe how planner-executor will be implemented on PettingLLMs without DEPART. (b) Acknowledge that the interpretability study adds ~2 weeks and ~$200-400 in annotation costs beyond compute estimates. (c) Consider strengthening the novelty narrative around GRPO-group hard negatives as the primary conceptual contribution — this is genuinely novel and underemphasized relative to the framework-level engineering.\n\n### Round 6 review\nVerdict: revise\nIssues: [\"TIMELINE CONSTRAINT VIOLATION (PERSISTENT): User's hard constraint is ≤16 days (EMNLP 2026, ARR May 25). The full program requires 10–12 weeks targeting AAAI 2027. The scoped-down EMNLP option (~80h, ALFWorld-only) is honestly flagged at 20–30% success probability but sacrifices the decisive group-vs-random ablation, the Pareto frontier comparison, and the interpretability study — all load-bearing contributions. After 6 rounds, the proposal still does not meet the user's primary venue requirement.\", \"MISSING CONCURRENT WORK — CoMAS (ICLR 2026, arXiv 2510.08529): Co-Evolving Multi-Agent Systems via Interaction Rewards explicitly trains communication quality through LLM-as-judge interaction rewards. While CoMAS uses scalar discussion-level rewards (not contrastive alignment), it addresses the same high-level problem: improving inter-agent communication quality during RL training. Must be cited and differentiated — IGCT provides dense per-token gradient signal via contrastive alignment, while CoMAS provides sparse discussion-level scalar rewards.\", \"REFERENCE ERROR — Robinson et al. hard negatives: The proposal cites 'Robinson et al. (NeurIPS 2021)' but this paper was published at ICLR 2021, not NeurIPS 2021. Minor but should be corrected for accuracy.\", \"ALFWORLD SATURATION RISK: HiPER achieves 97.4% success on ALFWorld with Qwen2.5-7B (single-agent hierarchical RL, no multi-agent communication). With only ~2.6% headroom remaining, demonstrating meaningful gains from communication quality training on ALFWorld is extremely challenging. The planner-executor setup with Qwen3-1.7B (smaller model) may start from a lower baseline, but this raises questions about whether improvements come from better communication or simply from multi-agent cooperation itself.\", \"COMPUTE BUDGET TIGHTNESS: While 155–195h fits within 200h, the margin is thin (5–45h buffer). WebArena-Lite multi-agent setup requires browser automation + planner-executor coordination, which historically runs slower than expected. ALFWorld environment interaction adds latency to GRPO rollouts that pure math/code tasks don't have. The 8h buffer in manual mode leaves little room for debugging or reruns.\", \"PLANNER-EXECUTOR IMPLEMENTATION RISK: Neither DEPART nor CoDA provides a planner-executor architecture specifically for ALFWorld or WebArena-Lite within PettingLLMs. The proposal must: (a) adapt CoDA's context-decoupled architecture to PettingLLMs, (b) implement planner-executor communication for ALFWorld/WebArena-Lite, and (c) modify PettingLLMs for group-level intent access. This is substantial systems work not fully reflected in the timeline.\"]\nFeedback: The proposal has reached strong quality after 6 rounds — the landscape is comprehensive, the core insight is genuinely novel, references are verified, and the compute budget finally fits within 200h. Three changes needed to reach pass quality:\n\n1. **RESOLVE THE TIMELINE/VENUE TENSION**: This is the most persistent issue. Two options: (a) Commit to AAAI 2027 and explicitly acknowledge the EMNLP deviation with a concrete justification (the decisive group-vs-random experiment, Pareto comparison, and interpretability study are essential contributions that cannot be sacrificed for a 15-day deadline). (b) Present a credible EMNLP-scoped version that preserves the decisive experiment: ALFWorld-only, IGCT-C with group vs. random negatives + baseline (~60h compute), no interpretability study, no WebArena-Lite. This preserves the core contribution even if it's a narrower paper. Either way, be definitive rather than hedging.\n\n2. **CITE CoMAS (ICLR 2026) AND ADDRESS ALFWorld SATURATION**: CoMAS trains communication quality via interaction rewards — cite it and differentiate (dense contrastive signal vs. sparse scalar reward). For ALFWorld saturation, consider: (a) report the baseline planner-executor performance WITHOUT IGCT first — if it's already at 90%+, the headroom argument weakens; (b) emphasize WebArena-Lite as the primary benchmark where there's more headroom (current SOTA ~57.58%); (c) frame ALFWorld results as demonstrating that IGCT preserves strong performance while improving message interpretability, not necessarily beating single-agent SOTA.\n\n3. **FIX THE ROBINSON REFERENCE AND TIGHTEN COMPUTE BUFFER**: Correct Robinson et al. to ICLR 2021. For compute: either increase the buffer to 15–20h by slightly reducing ablation scope (e.g., drop λ cosine variant, keep only constant vs. linear annealing), or reduce the WebArena-Lite scope to IGCT-C only (no baseline training — cite published baselines instead).\n\nMinor: The proposal is now strong enough that the 'engineering combination' criticism is largely addressed by the GRPO-group hard negatives insight. The decisive experiment directly tests whether the insight matters. If group negatives significantly outperform random negatives, the conceptual contribution is clear.\n\n### Round 7 review\nVerdict: revise\nIssues: [\"CRITICAL MISSING CITATION — CLIPO (March 2026, arxiv 2603.10101): This paper uses the exact same structural mechanism as IGCT-C — InfoNCE loss applied within GRPO rollout groups via an auxiliary projection head, combined with the GRPO policy gradient via weighted sum. CLIPO projects reasoning trajectories into a contrastive space and uses correct/incorrect rollouts as positives/negatives within each group. The proposal's claimed 'core conceptual contribution' — that GRPO's group sampling can be repurposed for contrastive objectives — is already demonstrated by CLIPO three months earlier, with public code (github.com/Qwen-Applications/CLIPO). This must be cited and the novelty claim substantially reframed.\", \"CRITICAL MISSING CITATION — AMIR-GRPO (January 2026, arxiv 2601.03661): Injects DPO-style contrastive supervision into GRPO by reinterpreting reward orderings within each rollout group as implicit pairwise preferences. Another demonstration that GRPO's group structure can be exploited for contrastive/preference learning, predating the proposal by 4+ months.\", \"CoDA CODE CLAIM UNVERIFIED: The proposal states 'CoDA (WSDM 2026, public code available)' but no public GitHub repository for arxiv 2512.12716 could be found. The similar-named CODA (arxiv 2508.20096) has code at github.com/OpenIXCLab/CODA but is a different paper. This claim should be verified or corrected.\", \"PettingLLMs DOES NOT SUPPORT ALFWorld: PettingLLMs supports Sokoban, Sudoku, Math, and Code benchmarks, but NOT ALFWorld. Adapting PettingLLMs to ALFWorld requires integrating TextWorld API, implementing ALFWorld-specific observation/action parsing, and designing the planner-executor task split — significant systems work not reflected in the 'Days 1-5 implementation' timeline.\", \"NARROWED NOVELTY AFTER CLIPO: With CLIPO and AMIR-GRPO already demonstrating GRPO-group contrastive learning, the proposal's novelty reduces to: (a) applying it to multi-agent communication rather than single-agent reasoning, (b) intent-grounding formulation with stop-gradient + EMA stabilization. This is sufficient for a solid workshop or Findings paper, but the decisive experiment (group vs random negatives) now tests whether GRPO-group negatives are better for communication — not whether the general approach works (CLIPO already shows it does). This lowers the bar for the decisive experiment.\"]\nFeedback: The proposal has reached strong quality in landscape coverage, honest self-assessment, and experimental design after 7 rounds. However, two critical missing citations significantly impact novelty:\n\n1. **CITE CLIPO AND REFRAME NOVELTY (MANDATORY)**: CLIPO (arxiv 2603.10101, March 2026) uses the identical structural mechanism — InfoNCE within GRPO rollout groups via auxiliary head, combined with GRPO loss — for reasoning trajectory consistency. AMIR-GRPO (arxiv 2601.03661, Jan 2026) exploits the same group structure for DPO-style contrastive supervision. Both demonstrate that 'GRPO groups as contrastive negatives' is a known technique. Reframe the contribution from 'discovering that GRPO groups provide contrastive negatives' (already known via CLIPO) to: 'We extend intra-group contrastive learning (CLIPO; AMIR-GRPO) from single-agent reasoning to multi-agent communication, where the contrastive objective serves a fundamentally different purpose — aligning messages with sender intent rather than enforcing trajectory consistency — and requires domain-specific adaptations (stop-gradient isolation, EMA stabilization) to handle LoRA-induced non-stationarity across multiple agents.' This is still a meaningful contribution but must be honestly scoped.\n\n2. **VERIFY OR CORRECT CoDA CODE CLAIM**: No public repository was found for CoDA (arxiv 2512.12716). Either verify the code availability with a direct link or remove the 'public code available' claim. If CoDA code is unavailable, the planner-executor architecture must be implemented from the PettingLLMs Sokoban template, adding engineering effort.\n\n3. **ADDRESS PettingLLMs→ALFWorld GAP**: PettingLLMs does not natively support ALFWorld. The implementation plan should explicitly describe the ALFWorld adaptation steps: TextWorld API integration, observation/action format conversion, planner-executor task decomposition for ALFWorld's 6 task types (pick, clean, heat, cool, examine, put). Consider allocating Days 1-3 exclusively for this adaptation, leaving Days 4-5 for IGCT-C implementation.\n\n4. **STRENGTHEN THE DECISIVE EXPERIMENT'S SIGNIFICANCE**: Given CLIPO, the decisive experiment (group vs random negatives) must now show something CLIPO didn't: that intra-group contrastive learning provides qualitatively different benefits for communication than for reasoning. Consider adding a brief analysis showing that group negatives produce messages with higher intent specificity (measured by intent-token attention entropy) while random negatives produce messages with higher topic distinctiveness but lower intent precision. This would demonstrate that the communication application reveals properties of GRPO-group contrastive learning that CLIPO's reasoning application does not.\n\nMinor: Fix Robinson et al. citation to ICLR 2021 (not NeurIPS 2021, noted in Round 6 but still uncorrected in the description).\n\n\n## Output format\nOutput ONLY a JSON object:\n{\n  \"verdict\": \"pass | revise | fail\",\n  \"scores\": {\n    \"novelty\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"feasibility\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"clarity\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"impact\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"}\n  },\n  \"issues\": [\"specific issue 1\", \"specific issue 2\", ...],\n  \"feedback\": \"Actionable feedback for the generator (if verdict=revise)\",\n  \"reason\": \"One-line summary of verdict rationale\"\n}\n\nRules:\n- \"pass\": idea is sound AND high quality — avg score >= 4.0, no critical issues\n- \"revise\": fixable issues OR scores below threshold — provide specific feedback\n- \"fail\": fundamental flaw (e.g., gap doesn't exist, approach provably wrong, or scores remain low after multiple revisions)\n- Threshold is HIGH (4.0/5.0): agent scores tend to be inflated, so only truly outstanding ideas should pass. An avg of 3.5 is NOT enough.\n- Round 10 only: if still \"revise\", you MUST choose \"pass\" or \"fail\"."
}
```

---

### Runtime record

_source line 2 · 2026-05-10T22:11:07.620Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-10T22:11:07.620Z",
  "sessionId": "0c886791-a9d9-487c-99a0-b2a7b1d3d99e"
}
```

---

## Round 1

39 recorded events

### User

_source line 3 · 2026-05-10T22:11:07.651Z_

You are a strict ML research reviewer conducting adversarial review.

**Today's date: 2026-05-10 (UTC).**

Your job: independently verify this idea's claims via WebSearch, then issue a verdict.

## User requirements
The user asked for: **Target: EMNLP 2026, ARR submission deadline 2026-05-25 (16 days from today 2026-05-09). Track: LLM Agents.

Direction: LLM Agents — planning algorithms, memory architectures, tool use, multi-agent coordination, agent training (SFT/RL), self-correction in agentic loops, environment feedback exploitation.

Contribution type: METHOD ONLY. Must propose a concrete new algorithm, training procedure, or inference-time mechanism. Reject pure benchmark / dataset / analysis ideas. Method + analysis OK if analysis validates the method.

HARD CONSTRAINTS:
1. Compute: ≤200 H100-hours total (baselines + method + ablations). Show the math.
2. Time: ≤16 days. Build on existing OSS agent codebases (AutoGen, LangGraph, OpenManus, etc.) — no from-scratch systems.
3. Eval: existing benchmarks only — AgentBench, WebArena, SWE-bench Verified, GAIA, ToolBench, ALFWorld, Mind2Web, τ-bench.

Avoid: generic ReAct variants, plain tool retrieval, naive memory summarization. Look for: agent training with minimal RL budget, structured planning beyond flat CoT, multi-agent communication protocols, agent self-verification mechanisms.

Tag: direction=agent, contribution_type=method. target_venues=["EMNLP 2026 Main", "EMNLP 2026 Findings"].**
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
4. **Venue validity**: Are target_venues' submission deadlines after 2026-05-10?
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

## Idea under review (round 8/10)
{
  "title": "Bilateral Intent Grounding: Extending Intra-Group Contrastive Learning from Reasoning Consistency to Multi-Agent Communication Specificity",
  "core_problem": "Intra-group contrastive learning within GRPO has been shown to improve single-agent reasoning quality (CLIPO, March 2026; AMIR-GRPO, January 2026), but these methods address individual reasoning consistency — not inter-agent communication. In multi-agent LLM systems, text communication quality remains a bottleneck: latent methods (LatentMAS, ICML 2026; RecursiveMAS; DiffMAS; Interlat, ACL 2026) achieve +8–27% but sacrifice interpretability, while text-based multi-agent GRPO (AT-GRPO/Stronger-MAS, ICLR 2026; MAGRPO, AAAI 2026) and credit assignment approaches (C3, CCPO, CoFi-PGMA) leave message quality to emerge from sparse task reward. CoMAS (ICLR 2026) targets communication quality via LLM-as-judge scalar rewards but provides discussion-level signals without within-message differentiation or contrastive alignment. The Social Deduction LLM (AAMAS 2025) trains receiver-side prediction but is task-specific and non-contrastive. Classical MARL contrastive methods (TACTIC, AAMAS 2025; CACL, 2024) train sender-side encoding with easy negatives at small scale — and critically, TACTIC pre-trains communication modules then freezes them, never jointly training sender and receiver end-to-end. Can the intra-group contrastive mechanism demonstrated by CLIPO for reasoning consistency be adapted to a fundamentally different objective — bilateral communication grounding — where both sender message fidelity AND receiver interpretation accuracy are jointly trained end-to-end via GRPO-group hard negatives?",
  "opportunity": "CLIPO (March 2026) and AMIR-GRPO (January 2026) established that GRPO's group sampling structure provides useful contrastive/preference signals for single-agent reasoning. However, their contrastive objectives are fundamentally different from what multi-agent communication requires. CLIPO contrasts based on OUTCOME CORRECTNESS: correct rollouts are positives, incorrect are negatives — enforcing representation consistency across successful reasoning paths. Multi-agent communication requires contrasting based on INTENT IDENTITY: a message should encode its specific sender intent, discriminating against alternative intents the same sender could have had. These are orthogonal objectives from the same structural mechanism. Moreover, CLIPO operates on a single agent — there is no receiver whose interpretation must align with the sender's intent. We identify a genuine open gap: no existing work performs end-to-end bilateral contrastive training of both LLM sender (message generation) and LLM receiver (message comprehension) within GRPO training. TACTIC (AAMAS 2025) trains both sides but pre-trains them offline then freezes during RL. Interlat (ACL 2026) stages training (receiver first, sender second). CoMAS uses scalar rewards without contrastive alignment. MAPoRL (ACL 2025) co-trains generation and comprehension but with no contrastive objective. We propose Bilateral Intent Grounding (BIG), which exploits GRPO-group negatives for a communication-specific bilateral contrastive objective: the sender loss trains messages to encode sender intent specifically; the receiver loss trains the receiver's interpretation to match sender intent accurately. Both losses use the same free GRPO-group negatives but serve different ends — and together create bidirectional grounding pressure that neither alone provides. This is most impactful in the 1.7B regime: AT-GRPO with Qwen3-1.7B achieves only 16.7% on AIME24 (vs. 50–57% with 8B), making inter-agent communication quality the dominant bottleneck. The decisive empirical question is whether BIG's bilateral communication-specific contrastive training provides orthogonal gains to CLIPO's reasoning-consistency training — if so, this demonstrates that GRPO-group contrastive learning has qualitatively different applications for communication versus reasoning, validating the domain extension.",
  "landscape": "**Intra-group contrastive/preference learning in GRPO (established technique):** CLIPO (March 2026, arXiv 2603.10101, public code at github.com/Qwen-Applications/CLIPO) applies InfoNCE within GRPO rollout groups: correct rollouts are positives, incorrect are negatives, projected through a learned linear head. The contrastive loss is converted into auxiliary reward augmenting GRPO's standard advantage. Evaluated on math (GSM8K, MATH, AIME) with Qwen2.5-3B/7B, achieving +0.65–5.42 points. AMIR-GRPO (January 2026, arXiv 2601.03661) mines DPO-style pairwise preferences from within-group reward orderings, extracting O(G²) pairs from G completions. Both demonstrate that GRPO's group structure can be exploited for contrastive/preference objectives at zero additional sampling cost — but both target single-agent reasoning consistency, not multi-agent communication. **Latent communication (bypass text):** LatentMAS (ICML 2026 Spotlight, arXiv 2511.20639) enables training-free latent collaboration via shared hidden embeddings, achieving +14.6% accuracy. RecursiveMAS (April 2026, arXiv 2604.25917) trains RecursiveLink modules for cross-agent latent state transfer (+8.3%). DiffMAS (April 2026, arXiv 2604.21794) optimizes KV-cache communication end-to-end (+26.7% on AIME24). Interlat (ACL 2026, arXiv 2511.09149) compresses hidden states with auxiliary separation and alignment losses — notably, Interlat stages sender/receiver training (receiver first then frozen, sender second), not joint bilateral training. All bypass text communication entirely. **Text-based multi-agent GRPO (task reward only):** AT-GRPO/Stronger-MAS/PettingLLMs (ICLR 2026, arXiv 2510.11062, public code) achieves massive multi-agent gains on AIME24 (+31.7–38.7 absolute points over single-agent with Qwen3-8B) via agent-and-turn-wise GRPO in multi-agent discussion. Qwen3-1.7B achieves 16.7% on AIME24, 35.2–39.6% on OlympiadBench — substantial headroom for communication improvement. MAGRPO (AAAI 2026) trains multi-agent writing/coding. Graph-GRPO (March 2026) optimizes topology but not message content. **Communication quality training (scalar reward signals):** CoMAS (ICLR 2026, arXiv 2510.08529) targets communication quality through LLM-as-judge interaction rewards with REINFORCE++, providing discussion-level scalar signals. Evaluated on math/coding with +2–20% gains. Key distinction: CoMAS incentivizes useful communication but cannot differentiate within-message token contributions or provide contrastive alignment between specific intents. **Credit assignment:** C3 (March 2026, arXiv 2603.06859) provides message-level counterfactual credit. CCPO (March 2026, arXiv 2603.21563) estimates marginal contributions. CoFi-PGMA (April 2026, arXiv 2604.22785) derives leave-one-out rewards. Dr. MAS (Feb 2026, arXiv 2602.08847) stabilizes via agent-wise advantage normalization. All provide scalar signals without within-message differentiation or communication-specific auxiliary objectives. **Text communication training in LLM agents:** The Social Deduction LLM (AAMAS 2025, arXiv 2502.06060) trains receiver-side listening loss (task-specific imposter prediction in Among Us) and RL speaking reward. Key distinctions: receiver-side only, task-specific, non-contrastive, PPO on RWKV. MAPoRL (ACL 2025) co-trains generation and comprehension via multi-agent PPO but with no contrastive/alignment loss between agents. MaKTO (NeurIPS 2025) uses KTO for multi-agent Werewolf but no communication-specific contrastive training. **Communication auxiliary losses in classical MARL:** TACTIC (AAMAS 2025) pre-trains both sender (message generator) and receiver (message-observation integrator) via SupCon contrastive objectives — the closest to bilateral contrastive communication training, but (a) pre-trains offline then freezes during RL (not end-to-end joint training), (b) uses random/replay-buffer negatives (not GRPO-group hard negatives), (c) operates on continuous-vector messages at small scale. CACL (2024) provides sender-side only contrastive loss. Lin et al. (NeurIPS 2021) uses autoencoder reconstruction. MASIA (NeurIPS 2022) combines global-state reconstruction with attention aggregation. LangGround (NeurIPS 2024) aligns MARL communication with LLM embeddings. MAIL (IJCAI 2025) uses multi-view contrastive losses for communication graph representations. **Supporting techniques:** CLIPO's projection head architecture (linear, mean pooling). EMA-PG (Feb 2026, arXiv 2602.04417) stability theory. Robinson et al. (ICLR 2021) on hard negatives tightening MI bounds. Attention pooling (Yang et al. NAACL 2016; Lin et al. ICLR 2017). **The gap:** No existing work performs end-to-end bilateral contrastive training of both LLM sender and LLM receiver for multi-agent communication within GRPO training. CLIPO/AMIR-GRPO demonstrated the mechanism for single-agent reasoning; TACTIC demonstrated bilateral contrastive communication but offline/frozen/small-scale; CoMAS targets communication quality but via scalar rewards; Interlat/Social Deduction LLM train one side but not both jointly with contrastive alignment. BIG fills this gap: bilateral, end-to-end, contrastive, GRPO-group hard negatives, at LLM multi-agent scale.",
  "approach": "We introduce Bilateral Intent Grounding (BIG), which extends intra-group contrastive learning — demonstrated for single-agent reasoning consistency by CLIPO (March 2026) and AMIR-GRPO (January 2026) — to multi-agent communication, with a fundamentally different contrastive objective (intent specificity rather than outcome consistency) and a novel bilateral formulation training both sender and receiver end-to-end. **Key distinction from CLIPO:** CLIPO's contrastive objective enforces OUTCOME CONSISTENCY — correct rollouts should have similar representations. BIG's contrastive objective enforces INTENT SPECIFICITY — a message should encode its sender's specific intent, and the receiver's interpretation should match that intent. CLIPO has no receiver (single-agent); BIG jointly trains both sides of the communication channel. The positives/negatives have fundamentally different semantics: CLIPO uses correct/incorrect as positive/negative; BIG uses same-intent/different-intent as positive/negative (a message's positive is the sender's intent embedding; negatives are the sender's alternative intents from other GRPO-group completions). **Bilateral formulation (core novelty):** For a given GRPO group with G completions per prompt, in completion k, agent A (sender) develops intent state e_A^k and generates message m^k, which agent B (receiver) reads to form interpretation state r_B^k. *Sender loss* trains messages to encode sender intent: L_sender = -log[exp(sim(pool(m^k), e_A^k)/τ) / Σ_j exp(sim(pool(m^k), e_A^j)/τ)], where j ranges over in-group completions. This uses GRPO-group negatives {e_A^j}_{j≠k} — same-agent, same-prompt, different-intent. *Receiver loss* trains interpretation to match sender intent: L_receiver = -log[exp(sim(r_B^k, e_A^k)/τ) / Σ_j exp(sim(r_B^k, e_A^j)/τ)]. The receiver's interpretation r_B^k is extracted as the pooled hidden state of agent B after processing message m^k. *Bidirectional grounding pressure:* Together, these create complementary training signals — the sender is incentivized to produce intent-specific messages (so the receiver loss can succeed), and the receiver is incentivized to decode intent accurately (even from imperfect messages). Neither alone achieves this: sender-only training (like CLIPO's approach applied to messages) can produce messages that are technically distinguishable but hard for a real receiver to decode; receiver-only training (like Social Deduction LLM's approach) cannot improve message quality. **Intent target extraction:** e_A = sg(EMA_τ(h_A^L)), where sg is stop-gradient and EMA (τ=0.999) provides target stabilization. Stop-gradient prevents auxiliary losses from distorting internal representations. EMA addresses the moving-target problem from continuous LoRA updates, grounded in EMA-PG stability theory (Zhang & Ba, Feb 2026). These adaptations are necessary for the multi-agent setting (multiple LoRA adapters creating cross-agent non-stationarity) but absent from CLIPO's single-agent setup. **Message/interpretation encoding:** Attention-weighted pooling (Yang et al. NAACL 2016; Lin et al. ICLR 2017): α_j = softmax(v^T·tanh(W·h_j + b)), pool = Σ_j α_j·h_j. Applied to message tokens (sender side) and receiver's post-message hidden states (receiver side). **Training:** L = L_GRPO + λ_s·L_sender + λ_r·L_receiver, with λ_s=λ_r annealed linearly from 0.2→0 over training. **Architecture:** Qwen3-1.7B with agent-specific LoRA adapters (rank=64), using PettingLLMs' existing multi-agent discussion infrastructure. The multi-agent discussion format (agents take turns proposing solutions, critiquing, and refining) naturally exposes both sender and receiver roles for each agent. The 1.7B size is deliberate: AT-GRPO with Qwen3-1.7B achieves only 16.7% on AIME24 (vs 50–57% with 8B), providing substantial headroom and ensuring communication quality is genuinely the bottleneck. **EMNLP-scoped evaluation (primary, ARR May 25 2026 — 15 days):** (1) PettingLLMs AIME multi-agent discussion with Qwen3-1.7B, five conditions: (a) AT-GRPO baseline, (b) AT-GRPO + CLIPO per-agent (existing method; improves individual reasoning consistency), (c) AT-GRPO + BIG sender-only (ablation: matches CLIPO's structure but with intent-specificity objective for communication), (d) AT-GRPO + BIG bilateral (full method: sender + receiver losses), (e) AT-GRPO + CLIPO + BIG bilateral (complementarity test). The decisive experiment is (b) vs (d) vs (e): if BIG bilateral provides gains beyond CLIPO, this demonstrates that communication-specific bilateral contrastive training provides orthogonal value to reasoning-consistency training — validating the domain extension. The (c) vs (d) comparison isolates the bilateral component's contribution. (2) Ablation: BIG bilateral with group negatives vs random negatives (tests whether GRPO-group hard negatives matter for communication specifically). (3) Ablation: BIG bilateral without stop-gradient isolation (tests necessity of multi-agent stability mechanism). (4) Qualitative analysis: attention-entropy comparison showing BIG bilateral produces messages with higher intent specificity (concentrated attention on intent-carrying tokens) vs CLIPO (diffuse attention reflecting general reasoning quality). Total EMNLP compute: ~55h H100. **AAAI 2027 extended evaluation (expected ~Aug 2026):** All EMNLP experiments plus: (1) OlympiadBench multi-agent (AT-GRPO 1.7B baseline: 35.2–39.6%, providing additional headroom). (2) BIG-R (Reconstruction) ablation — non-contrastive bilateral variant using MSE reconstruction loss on both sender and receiver sides. (3) Composability: BIG + C3 (complementary within-message bilateral vs between-message counterfactual credit). (4) Analysis of when bilateral > sender-only: hypothesis that bilateral advantage increases with task difficulty (harder problems require more precise communication). (5) λ annealing ablation: constant 0.1 vs linear 0.2→0. Total AAAI compute: ~120h H100.",
  "resource_estimate": {
    "emnlp_scoped": {
      "gpu_hours": "~55h H100 (AT-GRPO baseline: ~10h; CLIPO per-agent: ~12h; BIG sender-only: ~10h; BIG bilateral: ~10h; CLIPO + BIG bilateral: ~5h [warm-start from CLIPO]; group-vs-random ablation: ~5h; stop-gradient ablation: ~3h)",
      "gpu_utilization": "High (75–90%): uses PettingLLMs existing infrastructure with minimal modification",
      "timeline": "15 days (May 10–25, 2026): Days 1–3 implementation (integrate BIG losses into PettingLLMs AT-GRPO training loop — infrastructure already handles multi-agent discussion for AIME, add intent extraction with stop-gradient/EMA, add sender/receiver InfoNCE losses, integrate CLIPO baseline using their public code); Days 4–10 experiments (5 conditions + 2 ablations, parallelizable across 2 GPUs); Days 11–15 analysis + paper writing",
      "team": "1 researcher with RL + multi-agent expertise (full-time 15 days)",
      "estimated_gpu_cost": "$138–165 (at ~$2.50–3.00/GPU-hr)",
      "execution_risk": "Moderate (~35–45% chance of competitive submission). Reduced from original proposal because: (a) PettingLLMs already supports AIME multi-agent discussion natively (no ALFWorld adaptation needed); (b) CLIPO public code provides the projection head baseline directly; (c) BIG implementation adds two InfoNCE losses to existing infrastructure (conceptually straightforward). Primary risks: (a) bilateral loss may not provide gains over sender-only (the bilateral contribution is the core novelty — if sender-only matches bilateral, the contribution weakens to 'CLIPO for communication'); (b) CLIPO + BIG may not stack (if gains are redundant rather than orthogonal, the complementarity argument fails). Mitigations: sender-only vs bilateral ablation is fast to run (same infrastructure, toggle one loss); if bilateral doesn't help, the paper can pivot to analyzing WHY communication-specific contrastive training differs from reasoning-specific (negative result paper).",
      "what_is_preserved": "CLIPO direct comparison, bilateral vs sender-only ablation, complementarity test, group-vs-random ablation, stop-gradient necessity test",
      "what_is_sacrificed": "OlympiadBench (second benchmark), BIG-R ablation, C3 composability, detailed per-difficulty analysis"
    },
    "aaai_extended": {
      "gpu_hours": "~120h H100 (EMNLP experiments: ~55h; OlympiadBench [all conditions]: ~30h; BIG-R ablation: ~10h; C3 composability: ~10h; per-difficulty analysis: ~5h; λ annealing: ~5h; buffer: ~5h)",
      "gpu_utilization": "High (65–80%): parallelizable across multiple GPUs",
      "timeline": "10–12 weeks (May–Aug 2026)",
      "team": "1–2 researchers",
      "estimated_gpu_cost": "$300–360 (at ~$2.50–3.00/GPU-hr)"
    }
  },
  "target_venues": [
    "EMNLP 2026 (ARR May 25, 2026) — PRIMARY TARGET: focused on bilateral intent grounding with direct CLIPO comparison. The contribution is clearly scoped: extending intra-group contrastive learning from reasoning to communication via a novel bilateral formulation, with empirical validation of orthogonality. ~55h compute, 15-day execution. Engineering risk is substantially reduced (PettingLLMs native AIME support + CLIPO public code). Scientific risk remains (bilateral must outperform sender-only).",
    "AAAI 2027 (expected abstract ~Jul 25 2026, full paper ~Aug 1 2026) — EXTENDED VERSION: adds OlympiadBench, BIG-R ablation, C3 composability, per-difficulty analysis. If EMNLP is rejected, AAAI provides 12 weeks for the complete program with additional benchmarks.",
    "ICLR 2027 (expected ~Oct 2026) — further fallback with additional time for deeper analysis"
  ],
  "level": "solid",
  "key_references": [
    "CLIPO: Contrastive Learning in Policy Optimization Generalizes RLVR (March 2026, arXiv 2603.10101, public code github.com/Qwen-Applications/CLIPO)",
    "AMIR-GRPO: Inducing Implicit Preference Signals into GRPO (January 2026, arXiv 2601.03661)",
    "Latent Collaboration in Multi-Agent Systems — LatentMAS (ICML 2026 Spotlight, arXiv 2511.20639)",
    "Recursive Multi-Agent Systems — RecursiveMAS (April 2026, arXiv 2604.25917)",
    "Learning to Communicate: Toward End-to-End Optimization — DiffMAS (April 2026, arXiv 2604.21794)",
    "Enabling Agents to Communicate Entirely in Latent Space — Interlat (ACL 2026, arXiv 2511.09149)",
    "CoMAS: Co-Evolving Multi-Agent Systems via Interaction Rewards (ICLR 2026, arXiv 2510.08529)",
    "Training Language Models for Social Deduction with Multi-Agent RL — Social Deduction LLM (AAMAS 2025, arXiv 2502.06060)",
    "Stronger-MAS: Multi-Agent Reinforcement Learning for Collaborative LLMs — AT-GRPO/PettingLLMs (ICLR 2026, arXiv 2510.11062, public code github.com/pettingllms-ai/PettingLLMs)",
    "LLM Collaboration with Multi-Agent RL — MAGRPO (AAAI 2026)",
    "Task-Agnostic Contrastive Pre-Training for Communication — TACTIC (AAMAS 2025)",
    "Learning Multi-Agent Communication with Contrastive Learning — CACL (2024, arXiv 2307.01403)",
    "Multi-Agent Communication with Information Preserving — MAIL (IJCAI 2025)",
    "Contrastive Learning with Hard Negative Samples — Robinson et al. (ICLR 2021, arXiv 2010.04592)",
    "EMA Policy Gradient: Taming RL for LLMs with EMA Anchor — EMA-PG (Feb 2026, arXiv 2602.04417)",
    "Dr. MAS: Stable RL for Multi-Agent LLM Systems (Feb 2026, arXiv 2602.08847)",
    "C3: Contextual Counterfactual Credit Assignment (March 2026, arXiv 2603.06859)",
    "CCPO: Counterfactual Credit Policy Optimization (March 2026, arXiv 2603.21563)",
    "CoFi-PGMA: Counterfactual Policy Gradients for Multi-Agent LLMs (April 2026, arXiv 2604.22785)",
    "Graph-GRPO: Stabilizing Multi-Agent Topology Learning (March 2026, arXiv 2603.02701)",
    "CoDA: Context-Decoupled Hierarchical Agent with RL (WSDM 2026, arXiv 2512.12716, code github.com/liuxuanzhang718/CoDA)",
    "MAPoRL: Multi-Agent Post-Co-Training for Collaborative LLMs (ACL 2025)",
    "MaKTO: Multi-agent Kahneman-Tversky Optimization (NeurIPS 2025)",
    "Learning to Ground Multi-Agent Communication with Autoencoders — Lin et al. (NeurIPS 2021)",
    "Efficient Multi-agent Communication via Self-supervised Information Aggregation — MASIA (NeurIPS 2022)",
    "Language Grounded Multi-agent RL — LangGround (NeurIPS 2024)",
    "Hierarchical Attention Networks — Yang et al. (NAACL 2016)",
    "A Structured Self-Attentive Sentence Embedding — Lin et al. (ICLR 2017)",
    "Reinforcement Learning for LLM-based MAS through Orchestration Traces (May 2026, arXiv 2605.02801)",
    "Beyond Self-Talk: A Communication-Centric Survey of LLM-Based MAS (arXiv 2025)"
  ],
  "description": "We introduce Bilateral Intent Grounding (BIG), which extends intra-group contrastive learning — established for single-agent reasoning consistency by CLIPO (March 2026) and AMIR-GRPO (January 2026) — to multi-agent communication with a fundamentally different objective and a novel bilateral formulation. CLIPO demonstrated that GRPO's group sampling provides useful contrastive signals by contrasting correct vs incorrect rollouts to enforce reasoning trajectory consistency. BIG repurposes the same structural mechanism for a different goal: intent-specific communication. The contrastive semantics differ fundamentally — CLIPO uses outcome correctness (correct/incorrect) as the positive/negative criterion; BIG uses intent identity (same-intent/different-intent) — and BIG introduces bilateral training absent from all prior work. The sender loss trains messages to faithfully encode sender intent (InfoNCE with GRPO in-group alternative intents as hard negatives). The receiver loss — the core novelty — trains the receiver's interpretation to accurately decode sender intent using the same GRPO-group negatives. This bilateral pressure creates a virtuous cycle: senders produce more specific messages because receivers are trained to discriminate, and receivers improve because senders provide more decodable signals. No existing work achieves this: CLIPO has no receiver (single-agent); TACTIC (AAMAS 2025) pre-trains both sides but freezes during RL; Interlat (ACL 2026) stages training sequentially; CoMAS (ICLR 2026) uses scalar rewards without contrastive alignment; MAPoRL (ACL 2025) co-trains but without contrastive objectives. The multi-agent setting also requires domain-specific adaptations absent from CLIPO: stop-gradient isolation and EMA target stabilization (grounded in EMA-PG, Feb 2026) to handle cross-agent LoRA non-stationarity, and cross-agent negative pairs for inter-role discrimination. Architecture: Qwen3-1.7B with agent-specific LoRA (rank=64), built on PettingLLMs' existing multi-agent discussion infrastructure for AIME. The 1.7B regime is deliberate: AT-GRPO achieves only 16.7% on AIME24 at this scale (vs 50–57% with 8B), providing substantial headroom where communication quality is genuinely the bottleneck. **EMNLP-scoped submission (ARR May 25, 15 days):** Five conditions on AIME multi-agent discussion — AT-GRPO baseline, CLIPO per-agent (using their public code), BIG sender-only, BIG bilateral, CLIPO + BIG bilateral. The decisive experiments: (1) BIG bilateral vs CLIPO per-agent tests whether communication-specific contrastive training provides orthogonal value to reasoning-consistency training; (2) BIG bilateral vs BIG sender-only isolates the bilateral contribution; (3) CLIPO + BIG bilateral tests complementarity (if gains stack, the objectives are truly orthogonal). Ablations: group-vs-random negatives, stop-gradient necessity. ~55h H100, substantially reduced engineering risk (PettingLLMs native + CLIPO public code). **AAAI 2027 extended version (~Aug 2026):** Adds OlympiadBench, BIG-R (reconstruction) ablation, C3 composability, per-difficulty bilateral advantage analysis. ~120h H100.",
  "project_name": "recon_reg_comm_training",
  "source": "web_research"
}


## Previous review history
### Round 1 review
Verdict: revise
Issues: ["COMPUTE BUDGET VIOLATION: User's hard constraint is ≤200 H100-hours. The lowest estimate (manual mode, 250h) already exceeds this by 25%. The 120h 'single training run' claim likely underestimates multi-agent GRPO with a decoder, environment rollouts, and cooperative task setup. With ablations and baselines, 200h is unachievable for the proposed scope.", "EVAL BENCHMARK VIOLATION: 'Cooperative ALFWorld variants (custom 2-agent role-split tasks)' is NOT an existing benchmark — ALFWorld is single-agent. Creating custom cooperative tasks violates the user's 'existing benchmarks only' constraint. DEPART/HIMPO already uses standard ALFWorld for hierarchical multi-agent evaluation without requiring custom cooperative variants.", "CRITICAL MISSING CITATION: Lin et al. (NeurIPS 2021) 'Learning to Ground Multi-Agent Communication with Autoencoders' uses the exact same core mechanism — autoencoder reconstruction of sender state from communication messages to ground multi-agent communication. This is not cited and directly undercuts the novelty claim that reconstruction-regularized communication training is new.", "COMPETING WORK NOT ADDRESSED: MAPoRL (ACL 2025) explicitly trains communication quality in multi-agent LLM RL through influence-aware verification rewards that incentivize corrective and persuasive discussions. C3 (arXiv March 2026) provides message-level counterfactual credit assignment. The generator's claim that 'no existing method explicitly trains communication quality' is factually incorrect.", "DEPART/HIMPO (OpenReview 2025-2026) trains hierarchical planner-executor multi-agent systems with role-specific rewards on ALFWorld benchmarks, directly overlapping with the proposed evaluation setting and partially with the training approach (role-specific reward shaping).", "UNVERIFIABLE REFERENCE: 'Detecting and Repairing Role Drift in Multi-Agent Collaboration with Lightweight Protocols (Preprint 2026)' — I could not independently verify a paper titled 'RoleFix' or with this exact title. Search returns AgentFixer and various drift detection works, but not this specific paper.", "TIMELINE INFEASIBILITY: 16 days to design custom cooperative environments, implement the reconstruction decoder, integrate with PettingLLMs/VeRL, train with GRPO, run ablations, implement baselines (AT-GRPO, Graph-GRPO), and write the paper. Even with existing infrastructure, this scope is unrealistic for EMNLP ARR May 25.", "TECHNICAL CONCERN: Extracting 'intent embeddings' (last hidden state before message generation) during multi-agent GRPO rollouts with LoRA is non-trivial. The sender's internal representation changes as LoRA adapters are updated, creating a moving-target problem for the decoder. This interaction between the reconstruction loss gradient and the GRPO policy gradient is not analyzed."]
Feedback: The general direction of improving communication quality in multi-agent LLM training is valid and timely, but the current proposal has critical issues that must be addressed:

1. **Novelty repositioning required**: You MUST cite and differentiate from Lin et al. (NeurIPS 2021) 'Learning to Ground Multi-Agent Communication with Autoencoders,' MAPoRL (ACL 2025), and C3 (March 2026). The claim that 'no existing method explicitly trains communication quality' is false. Reposition: what does reconstruction-based regularization offer OVER verifier-based rewards (MAPoRL) and counterfactual credit (C3)? A concrete hypothesis: reconstruction loss provides denser gradient signal per message than outcome-based rewards, especially in early training when task success is rare.

2. **Fix the compute budget**: The user's hard constraint is ≤200 H100-hours. Options: (a) reduce to a 2-3B model (Qwen3.5-2B) with LoRA, which should cut training time by ~3-4x; (b) limit ablations to 2-3 key ones (λ_recon sweep, decoder vs. no-decoder, reconstruction vs. MAPoRL-style reward); (c) use the Stronger-MAS planning benchmarks (Sudoku, Sokoban, Plan-Path) which are already multi-agent and require no custom environment engineering.

3. **Use EXISTING multi-agent benchmarks ONLY**: Drop cooperative ALFWorld variants entirely. Use Stronger-MAS planning tasks (already 2+ agent, role-split compatible, with AT-GRPO baselines for direct comparison). Supplement with MAGRPO's writing/coding collaboration benchmarks. This eliminates environment engineering time AND satisfies the user's constraint.

4. **Sharpen the technical contribution**: The reconstruction decoder training dynamics during GRPO need analysis. Address: (a) how does the reconstruction target (intent embedding) evolve as LoRA weights update? (b) does the decoder need to be periodically re-initialized? (c) what is the gradient interaction between L_recon and L_GRPO? Without this analysis, the method appears ad-hoc.

5. **Target AAAI 2027 or ICLR 2027 instead of EMNLP**: The 16-day timeline is unrealistic for the required scope. With AAAI 2027 (expected ~Aug 2026), you gain 2-3 months for proper experimentation.

### Round 2 review
Verdict: revise
Issues: ["EVAL BENCHMARK CONSTRAINT VIOLATION: The user's hard constraint specifies allowed benchmarks: AgentBench, WebArena, SWE-bench Verified, GAIA, ToolBench, ALFWorld, Mind2Web, τ-bench. The proposal uses Stronger-MAS benchmarks (Sudoku 4x4, Plan-Path 10x10) and CoopHumanEval — NONE of which are in the allowed list. While these are legitimate published benchmarks (ICLR 2026 and AAAI 2026), they do not satisfy the user's explicit constraint.", "COOPHUMANEVAL MISMATCH: CoopHumanEval (from MAGRPO) uses role-based code cooperation where agents generate helper functions and main functions without inter-agent message passing. SGIR's core mechanism — reconstruction of sender intent from inter-agent messages — is fundamentally inapplicable to this benchmark. The agents don't send messages to each other; they share code outputs.", "MISSING CRITICAL CONCURRENT WORK (5 papers): (1) LatentMAS (ICML 2026 Spotlight, arXiv 2511.20639) — agents communicate through latent hidden-state representations, directly adjacent to SGIR's intent embedding approach. (2) RecursiveMAS (April 2026, arXiv 2604.25917) — RecursiveLink module transfers hidden representations between agents in latent space. (3) CCPO (March 2026, arXiv 2603.21563) — counterfactual credit policy optimization with agent-specific marginal contribution estimation. (4) CoFi-PGMA (April 2026, arXiv 2604.22785) — counterfactual policy gradients for multi-agent LLMs with leave-one-out credit. (5) Dr. MAS (Feb 2026, arXiv 2602.08847) — stable multi-agent GRPO via agent-wise advantage normalization, directly relevant as it addresses GRPO training stability.", "OVERSTATED PREMISE — LIN ET AL. GRADIENT CONFLICT: The proposal claims Lin et al. (NeurIPS 2021) found a 'fundamental conflict between reconstruction gradients and RL policy gradients' causing degraded task performance. This mischaracterizes their findings. Lin et al.'s paper shows autoencoding 'is sufficient for arriving at a grounded common language' with 'surprisingly strong task performance,' and their project page confirms the model 'consistently outperforms baselines.' While some tension between losses exists, characterizing it as a 'fundamental conflict' that SGIR uniquely resolves is an overstatement that weakens the core contribution's motivation. Similarly, claiming LangGround 'abandoned reconstruction entirely' due to this conflict is misleading — LangGround chose language embedding alignment primarily for human interpretability in ad-hoc teamwork.", "VENUE DEVIATION: The user specifically requested EMNLP 2026 (ARR deadline May 25, 2026). The proposal targets AAAI 2027 and ICLR 2027 instead. While pragmatic (16 days is infeasible for a training-based method paper), this does not match the user's stated requirement. The user's track specification was 'LLM Agents' which aligns with EMNLP, making the venue switch a substantive deviation.", "TECHNICAL RISK — DECODER MOVING-TARGET PROBLEM: The reconstruction decoder D_φ must learn to predict hidden states that change as LoRA adapters are updated during GRPO training. With λ annealing from 0.5 to 0, the decoder's target distribution shifts continuously. The proposal does not analyze whether the decoder can track this moving target or whether periodic re-initialization is needed. This is not just a theoretical concern — it directly affects whether the 'dense gradient signal' claim holds in practice."]
Feedback: The revised proposal shows significant improvement over Round 1 (compute budget addressed, custom environments dropped, better landscape coverage), but several critical issues remain:

1. **Fix benchmark compliance**: The user's allowed benchmarks are all primarily single-agent, creating a genuine tension with multi-agent methods. Two options: (a) Use ALFWorld (on the allowed list) with a DEPART/HIMPO-style planner-executor multi-agent setup — this involves message passing and is established in the literature. (b) Acknowledge the tension explicitly and argue that Stronger-MAS benchmarks are the appropriate community-standard multi-agent benchmarks with published baselines, while also providing at least one evaluation on a user-listed benchmark. Drop CoopHumanEval entirely — it uses code-level cooperation without messages, making SGIR inapplicable.

2. **Correct the Lin et al. premise**: Don't overstate the gradient conflict. Instead, reframe: 'Lin et al. showed reconstruction works in small MARL networks. However, scaling reconstruction-based grounding to LLM-scale multi-agent RL introduces new challenges: (a) the LoRA adapter updates create a moving target for the decoder, (b) the high-dimensional hidden states of LLMs make naive reconstruction infeasible, requiring architectural choices. Stop-gradient detachment is one principled approach to manage these scaling challenges.' This is more honest and still provides motivation.

3. **Cite and differentiate from LatentMAS and RecursiveMAS**: These are the closest concurrent works — both pass hidden representations between agents. Key differentiation: LatentMAS/RecursiveMAS REPLACE text communication with latent communication (inference-time mechanism), while SGIR AUGMENTS text communication with reconstruction-based training signal (training-time mechanism). SGIR preserves human-readable inter-agent messages. Also cite Dr. MAS, CCPO, and CoFi-PGMA for completeness.

4. **Address the moving-target problem**: Add a fourth ablation: periodic decoder re-initialization vs. continuous training. Or analyze theoretically why the stop-gradient ensures the target distribution changes slowly enough for the decoder to track. This would strengthen the technical contribution significantly.

5. **Consider meeting the EMNLP deadline**: If EMNLP 2026 is truly the target, scope down radically — 1 benchmark (Stronger-MAS Sudoku), 1 ablation (stop-gradient vs. joint), no CoopHumanEval. But realistically, targeting AAAI 2027 (expected Aug 2026 deadline) with the fuller experimental plan is more appropriate.

### Round 3 review
Verdict: revise
Issues: ["MISLEADING PER-TOKEN CLAIM: The core selling point — 'dense per-token supervision' — is technically inaccurate. With mean-pooling: L_recon = ||D_φ(pool(m)) - e_i||², the gradient ∂L/∂m_j = (1/T) · ∂L/∂pool(m) is identical for all tokens j. Every token receives the same gradient magnitude, making this effectively MESSAGE-LEVEL supervision, not per-token. To achieve genuine per-token differentiation, the proposal would need attention-weighted pooling or per-token reconstruction targets. This claim must be corrected or the pooling mechanism changed.", "MISSING CONCURRENT WORK — DiffMAS (arXiv 2604.21794, April 2026): 'Learning to Communicate: Toward End-to-End Optimization of Multi-Agent Language Systems' by Yu et al. (UIUC). DiffMAS optimizes inter-agent communication end-to-end via KV-cache transfer with LoRA adapters, achieving +26.7% on AIME24. While DiffMAS operates in latent space (no text), it directly addresses the same motivation (optimizing multi-agent communication quality) and must be cited and differentiated.", "MISSING CITATION — EMA Policy Gradient (arXiv 2602.04417, Feb 2026): Zhang & Ba provide theoretical stability conditions for using EMA anchors in GRPO-like training. Since SGIR's EMA target stabilization (τ=0.999) is a core technical contribution, this paper's stability analysis should be cited to provide theoretical grounding. Without it, the EMA design choice appears under-motivated.", "BENCHMARK PARTIAL COMPLIANCE: ALFWorld is on the user's allowed list (good). Stronger-MAS Sudoku 4x4 is NOT on the allowed list (AgentBench, WebArena, SWE-bench Verified, GAIA, ToolBench, ALFWorld, Mind2Web, τ-bench). The proposal acknowledges this implicitly by calling Sudoku a 'community-standard benchmark.' Consider replacing Sudoku with a second allowed-list benchmark or providing explicit justification for the deviation.", "THIN EVALUATION FOR TOP VENUE: Two benchmarks — ALFWorld (planner-executor) and Sudoku 4x4 (toy cooperative) — may be insufficient for AAAI 2027. ALFWorld is a good choice, but Sudoku 4x4 is very small-scale (4x4 grid, 2 agents). Reviewers will question generalization. Adding a third benchmark (e.g., from AgentBench or τ-bench multi-agent configurations) or scaling to 6x6 Sokoban (also in Stronger-MAS) would strengthen the experimental section.", "VENUE DEVIATION: The user explicitly requested EMNLP 2026 (ARR deadline May 25, 2026). The proposal targets AAAI 2027 (Aug 1, 2026) and ICLR 2027 (~Oct 2026). This follows Round 1-2 reviewer recommendations but still does not satisfy the user's stated constraint. If maintaining AAAI 2027 targeting, the proposal should explicitly acknowledge this deviation and justify why the expanded timeline enables stronger results."]
Feedback: The proposal has improved substantially across Rounds 1-3 — references are now comprehensive and verified, the Lin et al. characterization is honest, benchmark compliance is partially addressed, and the landscape is thorough. Three specific actions to reach pass quality:

1. **Fix the per-token claim or the mechanism**: This is the most important issue. Either (a) replace mean-pooling with attention-weighted pooling where learned attention weights differentiate token contributions, making per-token supervision genuine, or (b) reframe the claim honestly as 'dense message-level supervision' and argue why per-message reconstruction is superior to sparse task reward (which it is — you get a training signal for every message, not just at episode end). Option (a) adds novelty; option (b) sacrifices a selling point but gains integrity.

2. **Cite and differentiate from DiffMAS and EMA-PG**: DiffMAS (arXiv 2604.21794) is the closest concurrent work — differentiate by emphasizing SGIR preserves text (interpretability) while DiffMAS replaces it with KV-cache (performance). EMA-PG (arXiv 2602.04417) provides theoretical grounding for SGIR's EMA choice — cite its stability conditions and connect them to your τ=0.999 design.

3. **Strengthen evaluation scope**: Add at least one more evaluation dimension. Options: (a) scale to Sokoban 6x6 from Stronger-MAS (minimal additional effort, same codebase); (b) add a qualitative analysis of message quality improvement (human evaluation of planner messages in ALFWorld — shows interpretability advantage concretely); (c) compare SGIR message quality against LatentMAS's latent communication on a shared benchmark to directly test the 'close the gap while preserving text' hypothesis. Option (c) would be the strongest contribution but highest effort.

Minor: The DEPART shared-weights architecture means your 'planner' and 'executor' share base model weights with different LoRA adapters. This is fine technically but should be stated explicitly — reviewers familiar with DEPART will notice if you imply separate models.

### Round 4 review
Verdict: revise
Issues: ["MISSING CITATION — MASIA (NeurIPS 2022): 'Efficient Multi-agent Communication via Self-supervised Information Aggregation' (Guan et al.) uses reconstruction loss (reconstructing global state from messages) combined with attention-based message extraction in multi-agent communication. This is a direct precursor combining two of SGIR's core components (reconstruction + attention aggregation) and must be cited and differentiated.", "OVERSTATED ATTENTION POOLING NOVELTY: The attention-weighted pooling mechanism (α_j = softmax(v^T·tanh(W·h_j+b))) is the standard Hierarchical Attention Network formula from Yang et al. (NAACL 2016) and Lin et al. (ICLR 2017). Framing it as 'genuine per-token gradient differentiation' obscures that this is a trivially standard architectural choice. The gradient analysis also omits the softmax Jacobian redistribution term (∂α_k/∂h_j contributions), making the mechanism appear cleaner than it actually is.", "MISSING CONCURRENT WORK — Interlat (arXiv 2511.09149, revised April 2026): 'Enabling Agents to Communicate Entirely in Latent Space' by Du et al. proposes inter-agent communication via continuous last hidden states with learned compression. This is another latent communication method that should be in the landscape for completeness.", "NARROW NOVELTY GAP: The contribution reduces to 'apply stop-gradient + EMA to make reconstruction work at LLM scale' — the attention pooling is standard, the reconstruction idea is from Lin et al. 2021, and the EMA design is borrowed from EMA-PG. Each 'challenge' at LLM scale is addressed by a known technique. This risks the 'engineering combination' critique at top venues where reviewers expect conceptual novelty.", "UNCERTAIN EMPIRICAL IMPACT: No preliminary evidence suggests reconstruction can meaningfully close the text-latent performance gap. If LatentMAS achieves +14.6% by bypassing text and SGIR achieves +2-3% while preserving text, the contribution becomes 'we traded most of the performance for interpretability' — which may not be compelling without a strong interpretability analysis showing concrete debugging/safety benefits.", "VENUE DEVIATION PERSISTS: User requested EMNLP 2026 (ARR May 25). Proposal targets AAAI 2027 (Aug 1). While acknowledged and justified, this still does not meet the user's stated constraint."]
Feedback: The proposal has improved substantially over 4 rounds — landscape is now comprehensive, references are verified, benchmark compliance is mostly addressed, and the technical mechanism is clarified. Three specific actions to reach pass quality:

1. **Cite MASIA (NeurIPS 2022) and reframe the novelty narrative**: MASIA already combines reconstruction + attention for multi-agent communication messages. Your differentiation: MASIA reconstructs *global state* from messages in small MARL; SGIR reconstructs *sender intent embeddings* from messages at *LLM scale* with *stop-gradient + EMA* to handle LoRA-induced moving targets. The novelty is NOT attention pooling (standard since 2016) — it's the full architectural framework (stop-gradient isolation + EMA stabilization + λ annealing) that makes reconstruction work in the LLM-GRPO setting where naive approaches fail.

2. **Strengthen the impact argument with concrete interpretability value**: The 'preserve text for interpretability' argument is currently abstract. Make it concrete: (a) include a failure-mode analysis showing how SGIR-trained messages help debug agent errors that latent communication cannot, (b) show that SGIR attention weights identify which tokens carry intent (a free interpretability tool), (c) demonstrate human-in-the-loop intervention scenarios where text messages enable real-time correction. This converts the interpretability claim from a philosophical argument into a demonstrated advantage.

3. **Consider a direct text-vs-latent comparison**: On one benchmark (e.g., ALFWorld), run both LatentMAS (training-free, so cheap to evaluate) and SGIR. If SGIR achieves 70-80% of LatentMAS's gains while preserving readable messages, that's a compelling result. If it achieves only 10-20%, you need the interpretability argument to be ironclad. Having this comparison in hand before writing would let you frame the contribution appropriately.

Minor: fix the gradient analysis to acknowledge the softmax Jacobian term, or simply state 'the dominant gradient term is α_j-weighted' without claiming strict proportionality.

### Round 5 review
Verdict: revise
Issues: ["COMPUTE BUDGET VIOLATION (PERSISTENT): User's hard constraint is ≤200 H100-hours. All three modes exceed this: manual 230h (+15%), human-in-loop 250h (+25%), auto 280h (+40%). This was flagged in Round 1 and remains unfixed after 5 rounds. The proposal must either cut scope or demonstrate that the budget math is achievable within 200h.", "BENCHMARK NON-COMPLIANCE: Sokoban 6x6 is NOT on the user's allowed benchmark list (AgentBench, WebArena, SWE-bench Verified, GAIA, ToolBench, ALFWorld, Mind2Web, τ-bench). ALFWorld and WebArena-Lite are compliant, but the third benchmark must be replaced with one from the allowed list.", "DEPART/HIMPO CODE UNAVAILABILITY: Multiple searches confirm no public code release for DEPART/HIMPO. The proposal depends on 'DEPART-style planner-executor architecture' for ALFWorld and WebArena-Lite evaluation. Without code, this architecture must be reimplemented, adding significant engineering effort within the already-tight timeline. This risk is not acknowledged in the resource estimate.", "MISSING CITATION — Social Deduction LLM (arXiv 2502.06060, Feb 2025): 'Training Language Models for Social Deduction with Multi-Agent RL' explicitly trains text message quality in multi-agent LLM RL by decomposing communication into a 'listening' loss (predicting world state from messages — functionally a reconstruction objective on the receiver side) and an RL 'speaking' reward based on how messages shift other agents' beliefs. This is the closest prior work in the LLM-text domain and must be cited and differentiated.", "VENUE DEVIATION (PERSISTENT): User explicitly requested EMNLP 2026 (ARR May 25, 2026). Proposal targets AAAI 2027 (Aug 1, 2026). While the timeline justification is sound (16 days is genuinely infeasible for 230+ GPU-hours with human interpretability evaluation), this remains a hard constraint violation. The proposal should either (a) provide a scoped-down EMNLP-feasible variant or (b) explicitly accept that the idea does not meet the user's venue requirement.", "ENGINEERING COMBINATION RISK: The novelty narrative has improved substantially, but the core contribution — applying stop-gradient + EMA + attention pooling to make reconstruction/contrastive losses work at LLM-GRPO scale — risks the 'competent engineering' critique at top venues. The GRPO-group hard negatives are genuinely novel but constitute one technique within a larger framework of borrowed components. Reviewers at AAAI/ICLR may ask: 'What is the conceptual insight beyond careful engineering?'", "INTERPRETABILITY STUDY COMPLEXITY: The proposed interpretability evaluation (failure diagnosis study, attention-intent correlation with human annotations, human-in-the-loop correction experiments) is ambitious and valuable but adds substantial non-compute costs: annotation protocol design, 20+ person-hours of human annotation, and potential IRB considerations. These are not reflected in the timeline or cost estimates for any mode."]
Feedback: The proposal has improved dramatically over 5 rounds — the landscape is now among the most comprehensive I've seen, references are verified, and the technical framing is mostly honest. Three changes would bring this to pass quality:

1. **FIT WITHIN 200 H100-HOURS (MANDATORY)**: This is the user's hard constraint and has been violated for 5 rounds. Concrete path: (a) Drop Sokoban entirely — it's not on the allowed list anyway, saving ~45h. (b) Reduce ablations to the 3 most critical: IGCT-R vs IGCT-C vs combined, stop-gradient necessity, and λ annealing — saving ~15h. (c) This gives ~170h (70h ALFWorld + 55h WebArena-Lite + 5h LatentMAS baseline + 15h composability + 25h reduced ablations), safely within budget. The Sokoban controlled-comparison is nice-to-have but dispensable — AT-GRPO baselines can be cited without reproduction.

2. **REPLACE SOKOBAN WITH AN ALLOWED-LIST BENCHMARK OR DROP TO TWO**: Options: (a) Drop Sokoban and run ALFWorld + WebArena-Lite (both allowed, sufficient for a methods paper). (b) Replace with τ-bench (from the allowed list) which involves multi-turn agent-human interaction and could showcase IGCT's interpretability advantage. (c) Add an AgentBench subset if a third benchmark is needed for generalization claims.

3. **CITE THE SOCIAL DEDUCTION LLM PAPER AND DIFFERENTIATE**: arXiv 2502.06060 trains text message quality via a prediction loss + RL reward. Key differentiation: Social Deduction uses a receiver-side prediction loss (can the receiver extract world state from the message?) while IGCT uses a sender-side intent reconstruction loss (does the message faithfully convey sender intent?). Social Deduction also lacks contrastive alignment and GRPO-group hard negatives. Add this to the landscape and explain why sender-intent grounding is superior to receiver-side prediction for multi-agent coordination.

Minor improvements: (a) Address DEPART code unavailability — either contact authors for code or describe how planner-executor will be implemented on PettingLLMs without DEPART. (b) Acknowledge that the interpretability study adds ~2 weeks and ~$200-400 in annotation costs beyond compute estimates. (c) Consider strengthening the novelty narrative around GRPO-group hard negatives as the primary conceptual contribution — this is genuinely novel and underemphasized relative to the framework-level engineering.

### Round 6 review
Verdict: revise
Issues: ["TIMELINE CONSTRAINT VIOLATION (PERSISTENT): User's hard constraint is ≤16 days (EMNLP 2026, ARR May 25). The full program requires 10–12 weeks targeting AAAI 2027. The scoped-down EMNLP option (~80h, ALFWorld-only) is honestly flagged at 20–30% success probability but sacrifices the decisive group-vs-random ablation, the Pareto frontier comparison, and the interpretability study — all load-bearing contributions. After 6 rounds, the proposal still does not meet the user's primary venue requirement.", "MISSING CONCURRENT WORK — CoMAS (ICLR 2026, arXiv 2510.08529): Co-Evolving Multi-Agent Systems via Interaction Rewards explicitly trains communication quality through LLM-as-judge interaction rewards. While CoMAS uses scalar discussion-level rewards (not contrastive alignment), it addresses the same high-level problem: improving inter-agent communication quality during RL training. Must be cited and differentiated — IGCT provides dense per-token gradient signal via contrastive alignment, while CoMAS provides sparse discussion-level scalar rewards.", "REFERENCE ERROR — Robinson et al. hard negatives: The proposal cites 'Robinson et al. (NeurIPS 2021)' but this paper was published at ICLR 2021, not NeurIPS 2021. Minor but should be corrected for accuracy.", "ALFWORLD SATURATION RISK: HiPER achieves 97.4% success on ALFWorld with Qwen2.5-7B (single-agent hierarchical RL, no multi-agent communication). With only ~2.6% headroom remaining, demonstrating meaningful gains from communication quality training on ALFWorld is extremely challenging. The planner-executor setup with Qwen3-1.7B (smaller model) may start from a lower baseline, but this raises questions about whether improvements come from better communication or simply from multi-agent cooperation itself.", "COMPUTE BUDGET TIGHTNESS: While 155–195h fits within 200h, the margin is thin (5–45h buffer). WebArena-Lite multi-agent setup requires browser automation + planner-executor coordination, which historically runs slower than expected. ALFWorld environment interaction adds latency to GRPO rollouts that pure math/code tasks don't have. The 8h buffer in manual mode leaves little room for debugging or reruns.", "PLANNER-EXECUTOR IMPLEMENTATION RISK: Neither DEPART nor CoDA provides a planner-executor architecture specifically for ALFWorld or WebArena-Lite within PettingLLMs. The proposal must: (a) adapt CoDA's context-decoupled architecture to PettingLLMs, (b) implement planner-executor communication for ALFWorld/WebArena-Lite, and (c) modify PettingLLMs for group-level intent access. This is substantial systems work not fully reflected in the timeline."]
Feedback: The proposal has reached strong quality after 6 rounds — the landscape is comprehensive, the core insight is genuinely novel, references are verified, and the compute budget finally fits within 200h. Three changes needed to reach pass quality:

1. **RESOLVE THE TIMELINE/VENUE TENSION**: This is the most persistent issue. Two options: (a) Commit to AAAI 2027 and explicitly acknowledge the EMNLP deviation with a concrete justification (the decisive group-vs-random experiment, Pareto comparison, and interpretability study are essential contributions that cannot be sacrificed for a 15-day deadline). (b) Present a credible EMNLP-scoped version that preserves the decisive experiment: ALFWorld-only, IGCT-C with group vs. random negatives + baseline (~60h compute), no interpretability study, no WebArena-Lite. This preserves the core contribution even if it's a narrower paper. Either way, be definitive rather than hedging.

2. **CITE CoMAS (ICLR 2026) AND ADDRESS ALFWorld SATURATION**: CoMAS trains communication quality via interaction rewards — cite it and differentiate (dense contrastive signal vs. sparse scalar reward). For ALFWorld saturation, consider: (a) report the baseline planner-executor performance WITHOUT IGCT first — if it's already at 90%+, the headroom argument weakens; (b) emphasize WebArena-Lite as the primary benchmark where there's more headroom (current SOTA ~57.58%); (c) frame ALFWorld results as demonstrating that IGCT preserves strong performance while improving message interpretability, not necessarily beating single-agent SOTA.

3. **FIX THE ROBINSON REFERENCE AND TIGHTEN COMPUTE BUFFER**: Correct Robinson et al. to ICLR 2021. For compute: either increase the buffer to 15–20h by slightly reducing ablation scope (e.g., drop λ cosine variant, keep only constant vs. linear annealing), or reduce the WebArena-Lite scope to IGCT-C only (no baseline training — cite published baselines instead).

Minor: The proposal is now strong enough that the 'engineering combination' criticism is largely addressed by the GRPO-group hard negatives insight. The decisive experiment directly tests whether the insight matters. If group negatives significantly outperform random negatives, the conceptual contribution is clear.

### Round 7 review
Verdict: revise
Issues: ["CRITICAL MISSING CITATION — CLIPO (March 2026, arxiv 2603.10101): This paper uses the exact same structural mechanism as IGCT-C — InfoNCE loss applied within GRPO rollout groups via an auxiliary projection head, combined with the GRPO policy gradient via weighted sum. CLIPO projects reasoning trajectories into a contrastive space and uses correct/incorrect rollouts as positives/negatives within each group. The proposal's claimed 'core conceptual contribution' — that GRPO's group sampling can be repurposed for contrastive objectives — is already demonstrated by CLIPO three months earlier, with public code (github.com/Qwen-Applications/CLIPO). This must be cited and the novelty claim substantially reframed.", "CRITICAL MISSING CITATION — AMIR-GRPO (January 2026, arxiv 2601.03661): Injects DPO-style contrastive supervision into GRPO by reinterpreting reward orderings within each rollout group as implicit pairwise preferences. Another demonstration that GRPO's group structure can be exploited for contrastive/preference learning, predating the proposal by 4+ months.", "CoDA CODE CLAIM UNVERIFIED: The proposal states 'CoDA (WSDM 2026, public code available)' but no public GitHub repository for arxiv 2512.12716 could be found. The similar-named CODA (arxiv 2508.20096) has code at github.com/OpenIXCLab/CODA but is a different paper. This claim should be verified or corrected.", "PettingLLMs DOES NOT SUPPORT ALFWorld: PettingLLMs supports Sokoban, Sudoku, Math, and Code benchmarks, but NOT ALFWorld. Adapting PettingLLMs to ALFWorld requires integrating TextWorld API, implementing ALFWorld-specific observation/action parsing, and designing the planner-executor task split — significant systems work not reflected in the 'Days 1-5 implementation' timeline.", "NARROWED NOVELTY AFTER CLIPO: With CLIPO and AMIR-GRPO already demonstrating GRPO-group contrastive learning, the proposal's novelty reduces to: (a) applying it to multi-agent communication rather than single-agent reasoning, (b) intent-grounding formulation with stop-gradient + EMA stabilization. This is sufficient for a solid workshop or Findings paper, but the decisive experiment (group vs random negatives) now tests whether GRPO-group negatives are better for communication — not whether the general approach works (CLIPO already shows it does). This lowers the bar for the decisive experiment."]
Feedback: The proposal has reached strong quality in landscape coverage, honest self-assessment, and experimental design after 7 rounds. However, two critical missing citations significantly impact novelty:

1. **CITE CLIPO AND REFRAME NOVELTY (MANDATORY)**: CLIPO (arxiv 2603.10101, March 2026) uses the identical structural mechanism — InfoNCE within GRPO rollout groups via auxiliary head, combined with GRPO loss — for reasoning trajectory consistency. AMIR-GRPO (arxiv 2601.03661, Jan 2026) exploits the same group structure for DPO-style contrastive supervision. Both demonstrate that 'GRPO groups as contrastive negatives' is a known technique. Reframe the contribution from 'discovering that GRPO groups provide contrastive negatives' (already known via CLIPO) to: 'We extend intra-group contrastive learning (CLIPO; AMIR-GRPO) from single-agent reasoning to multi-agent communication, where the contrastive objective serves a fundamentally different purpose — aligning messages with sender intent rather than enforcing trajectory consistency — and requires domain-specific adaptations (stop-gradient isolation, EMA stabilization) to handle LoRA-induced non-stationarity across multiple agents.' This is still a meaningful contribution but must be honestly scoped.

2. **VERIFY OR CORRECT CoDA CODE CLAIM**: No public repository was found for CoDA (arxiv 2512.12716). Either verify the code availability with a direct link or remove the 'public code available' claim. If CoDA code is unavailable, the planner-executor architecture must be implemented from the PettingLLMs Sokoban template, adding engineering effort.

3. **ADDRESS PettingLLMs→ALFWorld GAP**: PettingLLMs does not natively support ALFWorld. The implementation plan should explicitly describe the ALFWorld adaptation steps: TextWorld API integration, observation/action format conversion, planner-executor task decomposition for ALFWorld's 6 task types (pick, clean, heat, cool, examine, put). Consider allocating Days 1-3 exclusively for this adaptation, leaving Days 4-5 for IGCT-C implementation.

4. **STRENGTHEN THE DECISIVE EXPERIMENT'S SIGNIFICANCE**: Given CLIPO, the decisive experiment (group vs random negatives) must now show something CLIPO didn't: that intra-group contrastive learning provides qualitatively different benefits for communication than for reasoning. Consider adding a brief analysis showing that group negatives produce messages with higher intent specificity (measured by intent-token attention entropy) while random negatives produce messages with higher topic distinctiveness but lower intent precision. This would demonstrate that the communication application reveals properties of GRPO-group contrastive learning that CLIPO's reasoning application does not.

Minor: Fix Robinson et al. citation to ICLR 2021 (not NeurIPS 2021, noted in Round 6 but still uncorrected in the description).


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
  "promptId": "c4053383-51a2-4c53-bef4-50bbbd8ab467",
  "type": "user",
  "uuid": "74dcf218-2261-44ac-ad40-e2e6fd0e555c",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c886791-a9d9-487c-99a0-b2a7b1d3d99e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-10T22:11:07.647Z_

```json
{
  "parentUuid": "74dcf218-2261-44ac-ad40-e2e6fd0e555c",
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
  "uuid": "1a4db7a1-f0db-464f-8491-4518882255b1",
  "timestamp": "2026-05-10T22:11:07.647Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c886791-a9d9-487c-99a0-b2a7b1d3d99e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-10T22:11:07.647Z_

```json
{
  "parentUuid": "1a4db7a1-f0db-464f-8491-4518882255b1",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "2bac9a80-c934-456b-8422-3c55e6e99697",
  "timestamp": "2026-05-10T22:11:07.647Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c886791-a9d9-487c-99a0-b2a7b1d3d99e",
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
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-10 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "2bac9a80-c934-456b-8422-3c55e6e99697",
  "sessionId": "0c886791-a9d9-487c-99a0-b2a7b1d3d99e"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Bilateral intent grounding for multi-agent LLM communication",
  "sessionId": "0c886791-a9d9-487c-99a0-b2a7b1d3d99e"
}
```

---

### Assistant

_source line 8 · 2026-05-10T22:11:21.317Z_

<details><summary>Logged reasoning block</summary>

```text
This is Round 8 of 10 for reviewing this research idea. Let me carefully analyze the proposal and conduct independent verification searches. The idea has been through 7 rounds of revision already, so I need to assess whether the critical issues from previous rounds have been addressed and whether any new issues exist.

Let me first understand the current state of the proposal:

**Title**: Bilateral Intent Grounding (BIG) - extending intra-group contrastive learning from reasoning consistency to multi-agent communication specificity.

**Key claims**:
1. CLIPO and AMIR-GRPO showed GRPO-group contrastive learning works for single-agent reasoning


2. BIG extends this to multi-agent communication with a different objective (intent specificity vs outcome consistency)
3. Novel bilateral formulation training both sender and receiver end-to-end
4. Uses GRPO-group hard negatives for communication-specific contrastive training
5. Built on PettingLLMs infrastructure with Qwen3-1.7B

**Previous issues that should be resolved**:
- Compute budget (now ~55h H100 for EMNLP scope)
- Missing citations (CLIPO, AMIR-GRPO now cited)
- Benchmark compliance (now using AIME multi-agent discussion)
- Venue targeting (now targeting EMNLP 2026 ARR May 25)

Now I need to check whether these resolutions are actually sound and identify any remaining gaps or new concerns that have emerged.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2bac9a80-c934-456b-8422-3c55e6e99697",
  "isSidechain": false,
  "requestId": "req_011Caueug5iQm3NvAzb6sHWu",
  "type": "assistant",
  "uuid": "d7b7be23-c90e-47de-ab1c-aaeccd6964d0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c886791-a9d9-487c-99a0-b2a7b1d3d99e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VAmvSHdvRtm1WRMckj3AUd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 25410,
      "cache_read_input_tokens": 11804,
      "output_tokens": 1863,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 25410,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1863,
          "cache_read_input_tokens": 11804,
          "cache_creation_input_tokens": 25410,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 25410
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Assistant

_source line 9 · 2026-05-10T22:11:21.360Z_

I'll conduct a thorough independent review of this Round 8 proposal. Let me verify the key claims, check for missing work, and assess feasibility.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d7b7be23-c90e-47de-ab1c-aaeccd6964d0",
  "isSidechain": false,
  "requestId": "req_011Caueug5iQm3NvAzb6sHWu",
  "type": "assistant",
  "uuid": "c91861c4-dee7-41e5-91cc-e8c71c6654c2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c886791-a9d9-487c-99a0-b2a7b1d3d99e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VAmvSHdvRtm1WRMckj3AUd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 25410,
      "cache_read_input_tokens": 11804,
      "output_tokens": 1863,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 25410,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1863,
          "cache_read_input_tokens": 11804,
          "cache_creation_input_tokens": 25410,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 25410
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-10T22:11:27.873Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01SHPBtQhxjXqFXE29bJz8rW`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Verify CLIPO and AMIR-GRPO papers",
  "prompt": "Search the web to verify these two papers and understand exactly what they do:\n\n1. CLIPO (March 2026, arXiv 2603.10101) - \"Contrastive Learning in Policy Optimization Generalizes RLVR\"\n   - Does it use InfoNCE within GRPO rollout groups?\n   - Does it have public code at github.com/Qwen-Applications/CLIPO?\n   - What are its exact results on math benchmarks?\n\n2. AMIR-GRPO (January 2026, arXiv 2601.03661) - \"Inducing Implicit Preference Signals into GRPO\"\n   - Does it mine DPO-style pairwise preferences from GRPO groups?\n   - What are its results?\n\nFor each, use WebSearch and try to WebFetch the arxiv abstract pages. Report exactly what you find — I need to verify these papers exist and do what the proposal claims."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c91861c4-dee7-41e5-91cc-e8c71c6654c2",
  "isSidechain": false,
  "requestId": "req_011Caueug5iQm3NvAzb6sHWu",
  "type": "assistant",
  "uuid": "02bff990-e8d1-4eba-9ccc-845601fb9183",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c886791-a9d9-487c-99a0-b2a7b1d3d99e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VAmvSHdvRtm1WRMckj3AUd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 25410,
      "cache_read_input_tokens": 11804,
      "output_tokens": 1863,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 25410,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1863,
          "cache_read_input_tokens": 11804,
          "cache_creation_input_tokens": 25410,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 25410
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-10T22:11:34.462Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01RRtGjsy7sqTDA1vADGVkiH`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Search for concurrent bilateral/contrastive communication work",
  "prompt": "Search the web for recent papers (2025-2026) that might be concurrent or competing work with the idea of \"bilateral contrastive training for multi-agent LLM communication.\" I need to find papers the proposal might have missed. Search for:\n\n1. \"bilateral communication training LLM agents 2026\" \n2. \"contrastive learning multi-agent communication LLM 2026\"\n3. \"sender receiver alignment multi-agent 2026\"\n4. \"intent grounding multi-agent reinforcement learning 2026\"\n5. \"communication quality training multi-agent LLM GRPO\"\n6. Search arxiv for any papers from March-May 2026 about multi-agent LLM communication training\n\nAlso specifically search for:\n- Any paper that does end-to-end bilateral contrastive training of sender AND receiver in multi-agent LLM systems\n- Any paper applying CLIPO-style contrastive loss to multi-agent communication\n\nReport all relevant papers found with titles, venues, and brief descriptions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "02bff990-e8d1-4eba-9ccc-845601fb9183",
  "isSidechain": false,
  "requestId": "req_011Caueug5iQm3NvAzb6sHWu",
  "type": "assistant",
  "uuid": "65e2940a-fb82-4b0b-8cbc-8bdb466a1d2f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c886791-a9d9-487c-99a0-b2a7b1d3d99e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VAmvSHdvRtm1WRMckj3AUd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 25410,
      "cache_read_input_tokens": 11804,
      "output_tokens": 1863,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 25410,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1863,
          "cache_read_input_tokens": 11804,
          "cache_creation_input_tokens": 25410,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 25410
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-10T22:11:41.222Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01SpMjWNKiVXKxLiHTQXNP7u`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Verify PettingLLMs AIME support and AT-GRPO baselines",
  "prompt": "Search the web to verify:\n\n1. PettingLLMs / AT-GRPO / Stronger-MAS (arXiv 2510.11062):\n   - Does PettingLLMs support AIME multi-agent discussion natively?\n   - What are the exact baselines for Qwen3-1.7B on AIME24? The proposal claims 16.7%.\n   - Does it have public code at github.com/pettingllms-ai/PettingLLMs?\n   - What benchmarks does PettingLLMs actually support?\n\n2. Search for \"AT-GRPO Qwen3 1.7B AIME24\" to verify the 16.7% claim specifically.\n\n3. Check if CLIPO has public code at github.com/Qwen-Applications/CLIPO\n\n4. Verify CoMAS (arXiv 2510.08529) - does it exist and what does it do?\n\n5. Check TACTIC (AAMAS 2025) - does it pre-train sender AND receiver contrastive modules then freeze them during RL?\n\nReport exactly what you find for each."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "65e2940a-fb82-4b0b-8cbc-8bdb466a1d2f",
  "isSidechain": false,
  "requestId": "req_011Caueug5iQm3NvAzb6sHWu",
  "type": "assistant",
  "uuid": "77ed8e3f-cd3f-4eb6-ba69-362c66ecd58e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c886791-a9d9-487c-99a0-b2a7b1d3d99e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VAmvSHdvRtm1WRMckj3AUd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 25410,
      "cache_read_input_tokens": 11804,
      "output_tokens": 1863,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 25410,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1863,
          "cache_read_input_tokens": 11804,
          "cache_creation_input_tokens": 25410,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 25410
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-10T22:11:48.739Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01P2zR2tUdwBuCp5Z8NaT7Uu`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Search for latest multi-agent LLM training papers May 2026",
  "prompt": "Search the web for the very latest papers (April-May 2026) on multi-agent LLM training, especially:\n\n1. Search \"multi-agent LLM reinforcement learning 2026 arxiv\" \n2. Search \"multi-agent GRPO communication 2026\"\n3. Search \"LLM agent communication training contrastive 2026\"\n4. Search for arxiv 2605 papers about multi-agent LLM systems\n5. Search \"site:arxiv.org multi-agent LLM training May 2026\"\n\nAlso verify these specific papers the proposal cites:\n- DiffMAS (arXiv 2604.21794) - does it exist?\n- RecursiveMAS (arXiv 2604.25917) - does it exist?\n- CoFi-PGMA (arXiv 2604.22785) - does it exist?\n- Graph-GRPO (March 2026, arXiv 2603.02701) - does it exist?\n- EMA-PG (arXiv 2602.04417) - does it exist?\n- arXiv 2605.02801 about \"Reinforcement Learning for LLM-based MAS through Orchestration Traces\" - does it exist?\n\nReport all findings including any new papers not cited in the proposal."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "77ed8e3f-cd3f-4eb6-ba69-362c66ecd58e",
  "isSidechain": false,
  "requestId": "req_011Caueug5iQm3NvAzb6sHWu",
  "type": "assistant",
  "uuid": "257aa37c-d8ca-49ae-b3de-d7fd1f830f97",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c886791-a9d9-487c-99a0-b2a7b1d3d99e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VAmvSHdvRtm1WRMckj3AUd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 25410,
      "cache_read_input_tokens": 11804,
      "output_tokens": 1863,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 25410,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1863,
          "cache_read_input_tokens": 11804,
          "cache_creation_input_tokens": 25410,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 25410
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-10T22:12:56.673Z_

<details><summary>↩ Tool result · `toolu_01SHPBtQhxjXqFXE29bJz8rW`</summary>

```text
I now have comprehensive, detailed information on both papers. Here is my full report.

---

## Verification Report

### Paper 1: CLIPO (arXiv 2603.10101)

**Status: CONFIRMED -- the paper exists and matches the claims.**

- **Title:** "CLIPO: Contrastive Learning in Policy Optimization Generalizes RLVR"
- **Authors:** Sijia Cui, Pengyu Cheng, Jiajun Song, Yongbo Gai, Guojun Zhang, Zhechao Yu, Jianhe Lin, Xiaoxi Jiang, Guanjun Jiang
- **Submitted:** March 10, 2026
- **arXiv:** [2603.10101](https://arxiv.org/abs/2603.10101)

**Does it use InfoNCE within GRPO rollout groups?**
Yes, confirmed. The paper explicitly states: "we select the InfoNCE as the lower bound approximation for MI maximization." The contrastive objective operates **within single rollout groups** for each prompt -- for each prompt x, a group of rollouts is generated, and InfoNCE is applied across this group, treating correct responses as positive pairs and incorrect ones as negatives. The contrastive reward is then added to the original verifiable reward. They also experiment with SupCon and SoftNN losses, but InfoNCE achieves the best results (+1.13 average on Track I).

**Does it have public code at github.com/Qwen-Applications/CLIPO?**
Yes, confirmed. The GitHub repository exists and contains:
- Training scripts for GSM8K and MATH datasets
- verl 0.6 + SGLang 0.5.2 implementation
- ContrastiveHead class and loss functions in `verl/trainer/ppo/ray_trainer.py`
- Support for Qwen2.5-3B-Instruct and Qwen2.5-7B-Instruct models

**Exact math benchmark results (from the paper):**
- Track II (competition-level, GRPO+CLIPO): MATH500 77.49%, AMC 49.17%, AIME 18.13%, AIME25 10.63%
- Track I (GSM8K+CLIPO): GSM8K 88.02%, GSM8K-P2 (perturbed) 54.16%
- Average improvements across four RLVR baselines (GRPO, GSPO, DAPO, GMPO): +1.19, +1.26, +1.81, +0.37 on competition-level math datasets

---

### Paper 2: AMIR-GRPO (arXiv 2601.03661)

**Status: CONFIRMED -- the paper exists and matches the claims.**

- **Title:** "AMIR-GRPO: Inducing Implicit Preference Signals into GRPO"
- **Authors:** Amir Hossein Yari, Fajri Koto
- **Submitted:** January 7, 2026
- **arXiv:** [2601.03661](https://arxiv.org/abs/2601.03661)

**Does it mine DPO-style pairwise preferences from GRPO groups?**
Yes, confirmed. The core mechanism works as follows:
- For a rollout group with rewards {r_i}, it constructs pairs (i,j) where r_i > r_j and the reward gap exceeds a margin threshold delta_r
- Higher-reward completions are treated as "preferred" and lower-reward ones as "rejected," exactly as in DPO
- The DPO logit is computed as: z_{i,j}(theta) = beta_DPO * [(log_theta(q,o_i) - log_ref(q,o_i)) - (log_theta(q,o_j) - log_ref(q,o_j))]
- The final objective combines GRPO loss with the preference regularizer: J_AMIR-GRPO = J_GRPO + lambda_reg * J_pref
- The regularization weight lambda_reg adapts dynamically

**Exact results:**

| Benchmark | Model | GRPO Pass@1 | AMIR-GRPO Pass@1 | GRPO Pass@4 | AMIR-GRPO Pass@4 |
|-----------|-------|------------|-------------------|------------|-------------------|
| AIME2025 | Qwen-7B | 4.2% | 5.8% | 12.1% | 13.8% |
| AMC23 | Qwen-7B | 45.0% | 47.8% | 63.7% | 73.1% |
| LiveMathBench | Qwen-7B | 27.4% | 30.2% | 41.7% | 45.1% |

Models tested: Qwen2.5-Instruct (3B, 7B), Gemma3-it (4B). All trained with LoRA (rank 16), group size 8, LR 5e-6.

---

### Summary

Both papers are **real, published on arXiv at the claimed IDs and dates, and do what the proposal claims**:
- CLIPO genuinely uses InfoNCE within GRPO rollout groups and has public code at the claimed GitHub URL
- AMIR-GRPO genuinely mines DPO-style pairwise preferences from within-group reward rankings in GRPO

Sources:
- [CLIPO on arXiv](https://arxiv.org/abs/2603.10101)
- [CLIPO full paper](https://arxiv.org/html/2603.10101v1)
- [CLIPO GitHub repository](https://github.com/Qwen-Applications/CLIPO)
- [CLIPO on HuggingFace Papers](https://huggingface.co/papers/2603.10101)
- [AMIR-GRPO on arXiv](https://arxiv.org/abs/2601.03661)
- [AMIR-GRPO full paper](https://arxiv.org/html/2601.03661v1)

agentId: afc1765bd1688391e (use SendMessage with to: 'afc1765bd1688391e' to continue this agent)
&lt;usage>total_tokens: 20112
tool_uses: 11
duration_ms: 88795&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "02bff990-e8d1-4eba-9ccc-845601fb9183",
  "isSidechain": false,
  "promptId": "c4053383-51a2-4c53-bef4-50bbbd8ab467",
  "type": "user",
  "uuid": "0b41ceff-8dea-495b-b32a-2e20fd5d74ba",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Search the web to verify these two papers and understand exactly what they do:\n\n1. CLIPO (March 2026, arXiv 2603.10101) - \"Contrastive Learning in Policy Optimization Generalizes RLVR\"\n   - Does it use InfoNCE within GRPO rollout groups?\n   - Does it have public code at github.com/Qwen-Applications/CLIPO?\n   - What are its exact results on math benchmarks?\n\n2. AMIR-GRPO (January 2026, arXiv 2601.03661) - \"Inducing Implicit Preference Signals into GRPO\"\n   - Does it mine DPO-style pairwise preferences from GRPO groups?\n   - What are its results?\n\nFor each, use WebSearch and try to WebFetch the arxiv abstract pages. Report exactly what you find — I need to verify these papers exist and do what the proposal claims.",
    "agentId": "afc1765bd1688391e",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "I now have comprehensive, detailed information on both papers. Here is my full report.\n\n---\n\n## Verification Report\n\n### Paper 1: CLIPO (arXiv 2603.10101)\n\n**Status: CONFIRMED -- the paper exists and matches the claims.**\n\n- **Title:** \"CLIPO: Contrastive Learning in Policy Optimization Generalizes RLVR\"\n- **Authors:** Sijia Cui, Pengyu Cheng, Jiajun Song, Yongbo Gai, Guojun Zhang, Zhechao Yu, Jianhe Lin, Xiaoxi Jiang, Guanjun Jiang\n- **Submitted:** March 10, 2026\n- **arXiv:** [2603.10101](https://arxiv.org/abs/2603.10101)\n\n**Does it use InfoNCE within GRPO rollout groups?**\nYes, confirmed. The paper explicitly states: \"we select the InfoNCE as the lower bound approximation for MI maximization.\" The contrastive objective operates **within single rollout groups** for each prompt -- for each prompt x, a group of rollouts is generated, and InfoNCE is applied across this group, treating correct responses as positive pairs and incorrect ones as negatives. The contrastive reward is then added to the original verifiable reward. They also experiment with SupCon and SoftNN losses, but InfoNCE achieves the best results (+1.13 average on Track I).\n\n**Does it have public code at github.com/Qwen-Applications/CLIPO?**\nYes, confirmed. The GitHub repository exists and contains:\n- Training scripts for GSM8K and MATH datasets\n- verl 0.6 + SGLang 0.5.2 implementation\n- ContrastiveHead class and loss functions in `verl/trainer/ppo/ray_trainer.py`\n- Support for Qwen2.5-3B-Instruct and Qwen2.5-7B-Instruct models\n\n**Exact math benchmark results (from the paper):**\n- Track II (competition-level, GRPO+CLIPO): MATH500 77.49%, AMC 49.17%, AIME 18.13%, AIME25 10.63%\n- Track I (GSM8K+CLIPO): GSM8K 88.02%, GSM8K-P2 (perturbed) 54.16%\n- Average improvements across four RLVR baselines (GRPO, GSPO, DAPO, GMPO): +1.19, +1.26, +1.81, +0.37 on competition-level math datasets\n\n---\n\n### Paper 2: AMIR-GRPO (arXiv 2601.03661)\n\n**Status: CONFIRMED -- the paper exists and matches the claims.**\n\n- **Title:** \"AMIR-GRPO: Inducing Implicit Preference Signals into GRPO\"\n- **Authors:** Amir Hossein Yari, Fajri Koto\n- **Submitted:** January 7, 2026\n- **arXiv:** [2601.03661](https://arxiv.org/abs/2601.03661)\n\n**Does it mine DPO-style pairwise preferences from GRPO groups?**\nYes, confirmed. The core mechanism works as follows:\n- For a rollout group with rewards {r_i}, it constructs pairs (i,j) where r_i > r_j and the reward gap exceeds a margin threshold delta_r\n- Higher-reward completions are treated as \"preferred\" and lower-reward ones as \"rejected,\" exactly as in DPO\n- The DPO logit is computed as: z_{i,j}(theta) = beta_DPO * [(log_theta(q,o_i) - log_ref(q,o_i)) - (log_theta(q,o_j) - log_ref(q,o_j))]\n- The final objective combines GRPO loss with the preference regularizer: J_AMIR-GRPO = J_GRPO + lambda_reg * J_pref\n- The regularization weight lambda_reg adapts dynamically\n\n**Exact results:**\n\n| Benchmark | Model | GRPO Pass@1 | AMIR-GRPO Pass@1 | GRPO Pass@4 | AMIR-GRPO Pass@4 |\n|-----------|-------|------------|-------------------|------------|-------------------|\n| AIME2025 | Qwen-7B | 4.2% | 5.8% | 12.1% | 13.8% |\n| AMC23 | Qwen-7B | 45.0% | 47.8% | 63.7% | 73.1% |\n| LiveMathBench | Qwen-7B | 27.4% | 30.2% | 41.7% | 45.1% |\n\nModels tested: Qwen2.5-Instruct (3B, 7B), Gemma3-it (4B). All trained with LoRA (rank 16), group size 8, LR 5e-6.\n\n---\n\n### Summary\n\nBoth papers are **real, published on arXiv at the claimed IDs and dates, and do what the proposal claims**:\n- CLIPO genuinely uses InfoNCE within GRPO rollout groups and has public code at the claimed GitHub URL\n- AMIR-GRPO genuinely mines DPO-style pairwise preferences from within-group reward rankings in GRPO\n\nSources:\n- [CLIPO on arXiv](https://arxiv.org/abs/2603.10101)\n- [CLIPO full paper](https://arxiv.org/html/2603.10101v1)\n- [CLIPO GitHub repository](https://github.com/Qwen-Applications/CLIPO)\n- [CLIPO on HuggingFace Papers](https://huggingface.co/papers/2603.10101)\n- [AMIR-GRPO on arXiv](https://arxiv.org/abs/2601.03661)\n- [AMIR-GRPO full paper](https://arxiv.org/html/2601.03661v1)"
      }
    ],
    "totalDurationMs": 88795,
    "totalTokens": 20112,
    "totalToolUseCount": 11,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1541,
      "cache_read_input_tokens": 17073,
      "output_tokens": 1497,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1541
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1497,
          "cache_read_input_tokens": 17073,
          "cache_creation_input_tokens": 1541,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1541,
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
  "sourceToolAssistantUUID": "02bff990-e8d1-4eba-9ccc-845601fb9183",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c886791-a9d9-487c-99a0-b2a7b1d3d99e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-10T22:13:38.740Z_

<details><summary>↩ Tool result · `toolu_01SpMjWNKiVXKxLiHTQXNP7u`</summary>

```text
Now I have all the data I need. Here is the complete report:

---

## Verification Report

### 1. PettingLLMs / AT-GRPO / Stronger-MAS (arXiv 2510.11062)

**Does PettingLLMs support AIME multi-agent discussion natively?**
Not as "multi-agent discussion" in the way that term usually implies. AIME is listed as a supported math benchmark, but during training the multi-agent setup uses a structured **Tool-User + Reasoner** role pairing (one agent uses code interpreters, the other does direct reasoning). Evaluation on AIME is single-agent style. It is not an open multi-agent discussion format.

**Exact baselines for Qwen3-1.7B on AIME24 -- does the proposal's claim of 16.7% hold?**
The 16.7% figure is **NOT a baseline**. According to Table 1 of the paper:
- Single agent baseline: **13.40%**
- Single agent + GRPO: **10.00%** (actually worse)
- MAS (no RL): **13.30%**
- MAS + GRPO: **13.30%**
- MAS + AT-GRPO w/ shared policy: **16.70%** (this is the *trained result*, not a baseline)
- MAS + AT-GRPO w/ per-role policies: **13.30%**

So 16.7% is the AT-GRPO trained result with shared policy, not any kind of baseline. If someone claimed "the baseline is 16.7%," that is incorrect.

**Does it have public code at github.com/pettingllms-ai/PettingLLMs?**
**Yes.** The repository exists and is tagged as "[ICLR'26] Stronger-MAS: A RL Framework for multi LLM agent system."

**What benchmarks does PettingLLMs actually support?**
- Code: APPS, CodeContests, LiveCodeBench
- Math: AIME, OlympiadBench
- Games/Planning: Sudoku, Sokoban
- Planned/upcoming: Verilog design, web search, robotics, database query, scientific discovery

### 2. AT-GRPO Qwen3 1.7B AIME24 16.7% claim

**Verdict: The 16.7% is the trained AT-GRPO result (shared policy), not a baseline.** The actual single-agent baseline is 13.40%, and single-agent + GRPO actually degrades to 10.00% on AIME24. If a proposal states "16.7%" as a baseline to beat, that is a misrepresentation of the Stronger-MAS paper's numbers.

For independent reference, the Qwen3 technical report lists Qwen3-1.7B at ~23.33% AveragePass@1 on AIME24, though evaluation methodology differs (thinking mode, generation length, etc.).

### 3. CLIPO at github.com/Qwen-Applications/CLIPO

**Yes, it exists and has real code.** The repository is titled "CLIPO: Contrastive Learning in Policy Optimization Generalizes RLVR." It contains:
- Core implementation built on the verl framework (verl 0.6, sglang 0.5.2)
- Training scripts for GSM8K and MATH tracks
- Supports Qwen2.5-3B-Instruct and Qwen2.5-7B-Instruct
- Evaluates on: GSM8K, GSM variants, TheoremQA, MMLU, TruthfulQA, CommonsenseQA (Track I); MATH, AIME, AIME 2025, AMC, MATH perturbation variants (Track II)
- 19 stars, 2 forks -- appears to be an active, real project from Alibaba's Qwen Applications team

### 4. CoMAS (arXiv 2510.08529)

**Yes, it exists.** The paper is titled "CoMAS: Co-Evolving Multi-Agent Systems via Interaction Rewards." Key facts:
- Enables LLM-based agents to improve autonomously through multi-agent interactions
- Generates intrinsic rewards from inter-agent discussion dynamics
- Uses an LLM-as-a-judge mechanism to formulate rewards
- Optimizes each agent's policy through RL in a decentralized, scalable manner
- Claims state-of-the-art performance; ablation studies confirm necessity of interaction-based reward signals
- Has a GitHub implementation at [github.com/xxyQwQ/CoMAS](https://github.com/xxyQwQ/CoMAS)
- Submitted October 2025, updated February 2026; has an OpenReview page

### 5. TACTIC (AAMAS 2025) -- does it pre-train sender AND receiver, then freeze both during RL?

**Yes, that is exactly correct.** TACTIC pre-trains **both** modules and freezes **both** during RL:

**Stage 1 (Offline contrastive pre-training):**
- **Message Generator (sender):** takes partial observations and generates outgoing messages
- **Message-Observation Integrator (receiver):** combines incoming messages with local observations into integrated representations
- Two contrastive objectives are used: Global Information Alignment (GIA) across all agents/timesteps, and Feature Integration Alignment (FIA) per agent
- Additional auxiliary losses: a deconstruction loss and a dynamic loss

**Stage 2 (Online RL policy learning):**
- The paper explicitly states: "the parameters of the pre-trained adaptive message generator and message-observation integrator remain fixed during this online training phase"
- Only the action-selection policy (GRU-based Q-network via QMIX) is trained
- The frozen communication modules provide representations that inform the policy network

So the claim that TACTIC pre-trains sender AND receiver contrastive modules then freezes them during RL is **confirmed as accurate**.

---

Sources:
- [Stronger-MAS arXiv page](https://arxiv.org/abs/2510.11062)
- [Stronger-MAS full paper HTML](https://arxiv.org/html/2510.11062)
- [PettingLLMs GitHub](https://github.com/pettingllms-ai/PettingLLMs)
- [CLIPO GitHub](https://github.com/Qwen-Applications/CLIPO)
- [CoMAS arXiv page](https://arxiv.org/abs/2510.08529)
- [CoMAS GitHub](https://github.com/xxyQwQ/CoMAS)
- [TACTIC arXiv HTML](https://arxiv.org/html/2501.02174)
- [TACTIC AAMAS 2025 proceedings PDF](https://www.ifaamas.org/Proceedings/aamas2025/pdfs/p2262.pdf)
- [Qwen3 Technical Report](https://arxiv.org/pdf/2505.09388)
- [AIME 2024 Benchmark Leaderboard](https://llm-stats.com/benchmarks/aime-2024)

agentId: a414f8376339a4870 (use SendMessage with to: 'a414f8376339a4870' to continue this agent)
&lt;usage>total_tokens: 23560
tool_uses: 16
duration_ms: 117514&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "77ed8e3f-cd3f-4eb6-ba69-362c66ecd58e",
  "isSidechain": false,
  "promptId": "c4053383-51a2-4c53-bef4-50bbbd8ab467",
  "type": "user",
  "uuid": "e81d34a1-cba5-42c0-818b-4f48c2c7cd32",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Search the web to verify:\n\n1. PettingLLMs / AT-GRPO / Stronger-MAS (arXiv 2510.11062):\n   - Does PettingLLMs support AIME multi-agent discussion natively?\n   - What are the exact baselines for Qwen3-1.7B on AIME24? The proposal claims 16.7%.\n   - Does it have public code at github.com/pettingllms-ai/PettingLLMs?\n   - What benchmarks does PettingLLMs actually support?\n\n2. Search for \"AT-GRPO Qwen3 1.7B AIME24\" to verify the 16.7% claim specifically.\n\n3. Check if CLIPO has public code at github.com/Qwen-Applications/CLIPO\n\n4. Verify CoMAS (arXiv 2510.08529) - does it exist and what does it do?\n\n5. Check TACTIC (AAMAS 2025) - does it pre-train sender AND receiver contrastive modules then freeze them during RL?\n\nReport exactly what you find for each.",
    "agentId": "a414f8376339a4870",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have all the data I need. Here is the complete report:\n\n---\n\n## Verification Report\n\n### 1. PettingLLMs / AT-GRPO / Stronger-MAS (arXiv 2510.11062)\n\n**Does PettingLLMs support AIME multi-agent discussion natively?**\nNot as \"multi-agent discussion\" in the way that term usually implies. AIME is listed as a supported math benchmark, but during training the multi-agent setup uses a structured **Tool-User + Reasoner** role pairing (one agent uses code interpreters, the other does direct reasoning). Evaluation on AIME is single-agent style. It is not an open multi-agent discussion format.\n\n**Exact baselines for Qwen3-1.7B on AIME24 -- does the proposal's claim of 16.7% hold?**\nThe 16.7% figure is **NOT a baseline**. According to Table 1 of the paper:\n- Single agent baseline: **13.40%**\n- Single agent + GRPO: **10.00%** (actually worse)\n- MAS (no RL): **13.30%**\n- MAS + GRPO: **13.30%**\n- MAS + AT-GRPO w/ shared policy: **16.70%** (this is the *trained result*, not a baseline)\n- MAS + AT-GRPO w/ per-role policies: **13.30%**\n\nSo 16.7% is the AT-GRPO trained result with shared policy, not any kind of baseline. If someone claimed \"the baseline is 16.7%,\" that is incorrect.\n\n**Does it have public code at github.com/pettingllms-ai/PettingLLMs?**\n**Yes.** The repository exists and is tagged as \"[ICLR'26] Stronger-MAS: A RL Framework for multi LLM agent system.\"\n\n**What benchmarks does PettingLLMs actually support?**\n- Code: APPS, CodeContests, LiveCodeBench\n- Math: AIME, OlympiadBench\n- Games/Planning: Sudoku, Sokoban\n- Planned/upcoming: Verilog design, web search, robotics, database query, scientific discovery\n\n### 2. AT-GRPO Qwen3 1.7B AIME24 16.7% claim\n\n**Verdict: The 16.7% is the trained AT-GRPO result (shared policy), not a baseline.** The actual single-agent baseline is 13.40%, and single-agent + GRPO actually degrades to 10.00% on AIME24. If a proposal states \"16.7%\" as a baseline to beat, that is a misrepresentation of the Stronger-MAS paper's numbers.\n\nFor independent reference, the Qwen3 technical report lists Qwen3-1.7B at ~23.33% AveragePass@1 on AIME24, though evaluation methodology differs (thinking mode, generation length, etc.).\n\n### 3. CLIPO at github.com/Qwen-Applications/CLIPO\n\n**Yes, it exists and has real code.** The repository is titled \"CLIPO: Contrastive Learning in Policy Optimization Generalizes RLVR.\" It contains:\n- Core implementation built on the verl framework (verl 0.6, sglang 0.5.2)\n- Training scripts for GSM8K and MATH tracks\n- Supports Qwen2.5-3B-Instruct and Qwen2.5-7B-Instruct\n- Evaluates on: GSM8K, GSM variants, TheoremQA, MMLU, TruthfulQA, CommonsenseQA (Track I); MATH, AIME, AIME 2025, AMC, MATH perturbation variants (Track II)\n- 19 stars, 2 forks -- appears to be an active, real project from Alibaba's Qwen Applications team\n\n### 4. CoMAS (arXiv 2510.08529)\n\n**Yes, it exists.** The paper is titled \"CoMAS: Co-Evolving Multi-Agent Systems via Interaction Rewards.\" Key facts:\n- Enables LLM-based agents to improve autonomously through multi-agent interactions\n- Generates intrinsic rewards from inter-agent discussion dynamics\n- Uses an LLM-as-a-judge mechanism to formulate rewards\n- Optimizes each agent's policy through RL in a decentralized, scalable manner\n- Claims state-of-the-art performance; ablation studies confirm necessity of interaction-based reward signals\n- Has a GitHub implementation at [github.com/xxyQwQ/CoMAS](https://github.com/xxyQwQ/CoMAS)\n- Submitted October 2025, updated February 2026; has an OpenReview page\n\n### 5. TACTIC (AAMAS 2025) -- does it pre-train sender AND receiver, then freeze both during RL?\n\n**Yes, that is exactly correct.** TACTIC pre-trains **both** modules and freezes **both** during RL:\n\n**Stage 1 (Offline contrastive pre-training):**\n- **Message Generator (sender):** takes partial observations and generates outgoing messages\n- **Message-Observation Integrator (receiver):** combines incoming messages with local observations into integrated representations\n- Two contrastive objectives are used: Global Information Alignment (GIA) across all agents/timesteps, and Feature Integration Alignment (FIA) per agent\n- Additional auxiliary losses: a deconstruction loss and a dynamic loss\n\n**Stage 2 (Online RL policy learning):**\n- The paper explicitly states: \"the parameters of the pre-trained adaptive message generator and message-observation integrator remain fixed during this online training phase\"\n- Only the action-selection policy (GRU-based Q-network via QMIX) is trained\n- The frozen communication modules provide representations that inform the policy network\n\nSo the claim that TACTIC pre-trains sender AND receiver contrastive modules then freezes them during RL is **confirmed as accurate**.\n\n---\n\nSources:\n- [Stronger-MAS arXiv page](https://arxiv.org/abs/2510.11062)\n- [Stronger-MAS full paper HTML](https://arxiv.org/html/2510.11062)\n- [PettingLLMs GitHub](https://github.com/pettingllms-ai/PettingLLMs)\n- [CLIPO GitHub](https://github.com/Qwen-Applications/CLIPO)\n- [CoMAS arXiv page](https://arxiv.org/abs/2510.08529)\n- [CoMAS GitHub](https://github.com/xxyQwQ/CoMAS)\n- [TACTIC arXiv HTML](https://arxiv.org/html/2501.02174)\n- [TACTIC AAMAS 2025 proceedings PDF](https://www.ifaamas.org/Proceedings/aamas2025/pdfs/p2262.pdf)\n- [Qwen3 Technical Report](https://arxiv.org/pdf/2505.09388)\n- [AIME 2024 Benchmark Leaderboard](https://llm-stats.com/benchmarks/aime-2024)"
      }
    ],
    "totalDurationMs": 117514,
    "totalTokens": 23560,
    "totalToolUseCount": 16,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1801,
      "cache_read_input_tokens": 20012,
      "output_tokens": 1746,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1801
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1746,
          "cache_read_input_tokens": 20012,
          "cache_creation_input_tokens": 1801,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1801,
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
      "otherToolCount": 16
    }
  },
  "sourceToolAssistantUUID": "77ed8e3f-cd3f-4eb6-ba69-362c66ecd58e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c886791-a9d9-487c-99a0-b2a7b1d3d99e",
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
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-10 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "e81d34a1-cba5-42c0-818b-4f48c2c7cd32",
  "sessionId": "0c886791-a9d9-487c-99a0-b2a7b1d3d99e"
}
```

---

### Runtime record

_source line 17_

```json
{
  "type": "ai-title",
  "aiTitle": "Bilateral intent grounding for multi-agent LLM communication",
  "sessionId": "0c886791-a9d9-487c-99a0-b2a7b1d3d99e"
}
```

---

### Tool result

_source line 18 · 2026-05-10T22:14:04.868Z_

<details><summary>↩ Tool result · `toolu_01RRtGjsy7sqTDA1vADGVkiH`</summary>

```text
Here is the comprehensive report of all relevant papers found that could be concurrent or competing work with "bilateral contrastive training for multi-agent LLM communication."

---

## HIGHLY RELEVANT PAPERS (Directly Overlapping Ideas)

### 1. CACL: Learning Multi-Agent Communication with Contrastive Learning
- **Venue:** ICLR 2024 (conference paper, building on ICLR 2022 workshop paper)
- **arXiv:** 2307.01403
- **Description:** Proposes Communication Alignment Contrastive Learning (CACL), which treats messages sent between agents as different incomplete views of the same environment state and uses contrastive learning to maximize mutual information between messages within a trajectory. Messages from the same trajectory are pulled closer; messages from different trajectories are pushed apart. This is the closest existing work to bilateral contrastive training -- it applies a CLIP-style contrastive objective directly to inter-agent messages. However, it operates in the traditional MARL (small-model) setting, not with LLMs.
- [Paper PDF](https://proceedings.iclr.cc/paper_files/paper/2024/file/de2ad3ed44ee4e675b3be42aa0b615d0-Paper-Conference.pdf)

### 2. Learning to Ground Decentralized Multi-Agent Communication with Contrastive Learning
- **Venue:** ICLR 2022 Workshop (EmeCom)
- **Description:** The precursor workshop paper introducing CACL, grounding decentralized multi-agent communication via contrastive learning to maximize mutual information between agent messages. Demonstrates that contrastive grounding induces more symmetric communication and captures global state information.
- [OpenReview](https://openreview.net/forum?id=rLceWXWCmZc)

### 3. MAIL: Multi-Agent Communication with Information Preserving Graph Contrastive Learning
- **Venue:** IJCAI 2025
- **Description:** Proposes a graph contrastive learning approach for multi-agent communication that minimizes feature contrastive loss, cross-module loss, and topological contrastive loss to learn expressive message representations. Extends contrastive communication to graph-structured agent topologies.
- [IJCAI 2025 Proceedings PDF](https://www.ijcai.org/proceedings/2025/0008.pdf)

### 4. MAGE: Learning Multi-Agent Communication via Graph Contrastive Learning
- **Venue:** Pattern Recognition (2025)
- **Description:** Uses graph contrastive learning for multi-agent communication by generating correlated graph views through stochastic corruption, then training with contrastive loss to enhance consistency of agent features. First work to extend graph contrastive learning to MARL communication.
- [ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0031320325007538)

---

## STRONGLY RELEVANT PAPERS (Multi-Agent LLM Training / GRPO Extensions)

### 5. M-GRPO: Multi-Agent Deep Research -- Training Multi-Agent Systems with M-GRPO
- **arXiv:** 2511.13288 (November 2025)
- **Description:** Extends GRPO to vertical (hierarchical) multi-agent LLM systems. Computes group-relative advantages for both main and sub-agents, introduces trajectory-alignment for variable sub-agent invocations, and uses a decoupled training pipeline where agents on separate servers exchange minimal statistics. Directly relevant as it applies GRPO to multi-agent LLM training.
- [arXiv](https://arxiv.org/abs/2511.13288)

### 6. MAGRPO: LLM Collaboration with Multi-Agent Reinforcement Learning
- **Venue:** AAAI 2026
- **Description:** Formalizes LLM dialogue as a Dec-POMDP and introduces Multi-Agent Group Relative Policy Optimization. Uses centralized group-relative advantages for joint optimization while preserving decentralized execution. Directly trains multiple LLMs to collaborate via shared reward signals. Open-source library CoMLRL released.
- [arXiv](https://arxiv.org/abs/2508.04652) | [AAAI 2026 Proceedings](https://ojs.aaai.org/index.php/AAAI/article/view/40487)

### 7. MARFT: Multi-Agent Reinforcement Fine-Tuning
- **arXiv:** 2504.16129 (April 2025, updated November 2025)
- **Description:** Introduces the MARFT paradigm for fine-tuning LLM-based multi-agent systems with RL. Proposes Flex-MG mechanism and a universal algorithmic framework specifically tailored for LLM-based MAS. Addresses the gap between traditional MARL and LLM-based multi-agent systems.
- [arXiv](https://arxiv.org/abs/2504.16129)

### 8. MARTI: A Framework for Multi-Agent LLM Systems Reinforced Training and Inference
- **Venue:** ICLR 2026
- **Institution:** Tsinghua University
- **Description:** Open-source framework for training LLM-based multi-agent systems with RL. Supports centralized multi-agent interactions with distributed policy training, multi-turn asynchronous rollouts, dynamic workflows, and both verifiable and generative rewards. MARTI-v2 adds tree search-augmented RL.
- [OpenReview](https://openreview.net/forum?id=E7jZqo0A50) | [GitHub](https://github.com/TsinghuaC3I/MARTI)

### 9. MARS: Co-evolving Dual-System Deep Research via Multi-Agent Reinforcement Learning
- **arXiv:** 2510.04935 (October 2025, updated February 2026)
- **Description:** Co-evolution framework jointly optimizing dual cognitive systems (System 1 fast processing + System 2 deliberate reasoning) through multi-agent RL. Extends GRPO to simultaneously optimize both systems with multi-turn tool interactions. Relevant as it trains bilateral agent roles with shared trajectory rewards.
- [arXiv](https://arxiv.org/abs/2510.04935)

---

## RELEVANT PAPERS (Communication Optimization / Latent Communication)

### 10. LatentMAS: Latent Collaboration in Multi-Agent Systems
- **Venue:** ICML 2026 Spotlight
- **arXiv:** 2511.20639 (November 2025)
- **Description:** Moves agent collaboration from token space into latent space. Agents communicate by passing latent thoughts (last-layer hidden embeddings) through shared working memory. Achieves up to 14.6% accuracy improvement with 70-84% token reduction and 4x faster inference. Training-free latent-space alignment.
- [arXiv](https://arxiv.org/abs/2511.20639) | [GitHub](https://github.com/Gen-Verse/LatentMAS)

### 11. The Vision Wormhole: Latent-Space Communication in Heterogeneous Multi-Agent Systems
- **arXiv:** 2602.15382 (February 2026)
- **Description:** Maps heterogeneous reasoning traces into a shared continuous latent space via a Universal Visual Codec and injects them into the receiver's visual pathway. Uses self-supervised distillation (teacher-student) to align high-speed visual channel with text-based reasoning. Reduces sender-receiver alignment complexity from O(N^2) to O(N) with hub-and-spoke topology.
- [arXiv](https://arxiv.org/abs/2602.15382)

### 12. Adapting LLM Agents Through Communication (LTC)
- **Venue:** Under review / OpenReview
- **arXiv:** 2310.01444
- **Description:** Proposes Learning Through Communication (LTC), enabling LLM agents to improve through interactions with environments and other agents. Defines three communication patterns: single-agent monologue, multi-agent dialogue, and teacher-student dialogue. Uses universal buffer for linguistic and reward feedback with iterative policy updates.
- [OpenReview](https://openreview.net/forum?id=wOelVq8fwL)

### 13. Cut the Crap: An Economical Communication Pipeline for LLM-based Multi-Agent Systems (AgentPrune)
- **Venue:** ICLR 2025
- **arXiv:** 2410.02506
- **Description:** Identifies and formalizes communication redundancy in LLM-based multi-agent pipelines. Proposes AgentPrune for one-shot pruning of the spatial-temporal message-passing graph. Achieves comparable results with ~87% cost reduction.
- [arXiv](https://arxiv.org/abs/2410.02506)

### 14. Language Grounded Multi-Agent Reinforcement Learning with Human-Interpretable Communication
- **arXiv:** 2409.17348 (September 2024, updated 2025)
- **Description:** Grounds MARL agent communication in natural language using synthetic data from embodied LLMs. Demonstrates zero-shot generalization in ad-hoc teamwork with unseen teammates. Combines RL loss with supervised learning loss for end-to-end training.
- [arXiv](https://arxiv.org/abs/2409.17348)

---

## CONTEXTUAL / SURVEY PAPERS

### 15. Beyond Self-Talk: A Communication-Centric Survey of LLM-Based Multi-Agent Systems
- **arXiv:** 2502.14321 (February 2025, updated June 2025)
- **Description:** Comprehensive survey examining LLM-based MAS from a communication perspective. Proposes a framework integrating system-level communication (architecture, goals, protocols) with internal communication (strategies, paradigms, content). Highlights challenges in communication efficiency, security, and scalability.
- [arXiv](https://arxiv.org/abs/2502.14321)

### 16. Reinforcement Learning for LLM-based Multi-Agent Systems through Orchestration Traces
- **arXiv:** 2605.02801 (May 2026)
- **Description:** Surveys and systematizes RL methods for LLM-based MAS through orchestration traces. Documents the recent emergence of hierarchical GRPO decompositions, message-level counterfactual credit assignment, and Shapley-based agent-level credit methods from 2025-Q2 through May 2026.
- [arXiv](https://arxiv.org/abs/2605.02801)

### 17. Active Learning for Communication Structure Optimization in LLM-Based Multi-Agent Systems
- **arXiv:** 2605.05703 (May 2026)
- **Authors:** Huchen Yang, Xinghao Dong, Dan Negrut, Jin-Long Wu
- **Description:** Optimizes communication topology in LLM-based MAS using active learning. Directly relevant to the structural aspects of multi-agent communication design.

---

## KEY GAP ANALYSIS

Based on this extensive search, the specific niche of **bilateral contrastive training applied to sender AND receiver in multi-agent LLM systems** does not appear to have been published. The closest works are:

- **CACL (ICLR 2024)** does bilateral contrastive alignment of agent messages, but in small MARL models, not LLMs.
- **MAGRPO / M-GRPO / MARFT** apply GRPO-based RL to multi-agent LLM training, but do not use contrastive objectives on the communication channel itself.
- **LatentMAS and Vision Wormhole** address sender-receiver alignment in LLM agents, but through latent-space distillation rather than contrastive losses.
- **No paper found** applies a CLIP/CLIPO-style contrastive loss specifically to bilateral sender-receiver LLM communication in multi-agent systems.

The proposal's combination of (a) contrastive loss on the communication channel + (b) applied to LLM-scale agents + (c) bilateral training of both sender and receiver appears to be a novel intersection as of May 2026. The most threatening concurrent work would be CACL's potential extension to LLMs, and the GRPO-family papers (MAGRPO, M-GRPO, MARTI, MARFT) which could be combined with contrastive communication objectives.

agentId: a6e82473bf7a9063b (use SendMessage with to: 'a6e82473bf7a9063b' to continue this agent)
&lt;usage>total_tokens: 36335
tool_uses: 25
duration_ms: 150403&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "65e2940a-fb82-4b0b-8cbc-8bdb466a1d2f",
  "isSidechain": false,
  "promptId": "c4053383-51a2-4c53-bef4-50bbbd8ab467",
  "type": "user",
  "uuid": "c7dc38e0-a3ae-4262-b39b-3e08db620429",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Search the web for recent papers (2025-2026) that might be concurrent or competing work with the idea of \"bilateral contrastive training for multi-agent LLM communication.\" I need to find papers the proposal might have missed. Search for:\n\n1. \"bilateral communication training LLM agents 2026\" \n2. \"contrastive learning multi-agent communication LLM 2026\"\n3. \"sender receiver alignment multi-agent 2026\"\n4. \"intent grounding multi-agent reinforcement learning 2026\"\n5. \"communication quality training multi-agent LLM GRPO\"\n6. Search arxiv for any papers from March-May 2026 about multi-agent LLM communication training\n\nAlso specifically search for:\n- Any paper that does end-to-end bilateral contrastive training of sender AND receiver in multi-agent LLM systems\n- Any paper applying CLIPO-style contrastive loss to multi-agent communication\n\nReport all relevant papers found with titles, venues, and brief descriptions.",
    "agentId": "a6e82473bf7a9063b",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here is the comprehensive report of all relevant papers found that could be concurrent or competing work with \"bilateral contrastive training for multi-agent LLM communication.\"\n\n---\n\n## HIGHLY RELEVANT PAPERS (Directly Overlapping Ideas)\n\n### 1. CACL: Learning Multi-Agent Communication with Contrastive Learning\n- **Venue:** ICLR 2024 (conference paper, building on ICLR 2022 workshop paper)\n- **arXiv:** 2307.01403\n- **Description:** Proposes Communication Alignment Contrastive Learning (CACL), which treats messages sent between agents as different incomplete views of the same environment state and uses contrastive learning to maximize mutual information between messages within a trajectory. Messages from the same trajectory are pulled closer; messages from different trajectories are pushed apart. This is the closest existing work to bilateral contrastive training -- it applies a CLIP-style contrastive objective directly to inter-agent messages. However, it operates in the traditional MARL (small-model) setting, not with LLMs.\n- [Paper PDF](https://proceedings.iclr.cc/paper_files/paper/2024/file/de2ad3ed44ee4e675b3be42aa0b615d0-Paper-Conference.pdf)\n\n### 2. Learning to Ground Decentralized Multi-Agent Communication with Contrastive Learning\n- **Venue:** ICLR 2022 Workshop (EmeCom)\n- **Description:** The precursor workshop paper introducing CACL, grounding decentralized multi-agent communication via contrastive learning to maximize mutual information between agent messages. Demonstrates that contrastive grounding induces more symmetric communication and captures global state information.\n- [OpenReview](https://openreview.net/forum?id=rLceWXWCmZc)\n\n### 3. MAIL: Multi-Agent Communication with Information Preserving Graph Contrastive Learning\n- **Venue:** IJCAI 2025\n- **Description:** Proposes a graph contrastive learning approach for multi-agent communication that minimizes feature contrastive loss, cross-module loss, and topological contrastive loss to learn expressive message representations. Extends contrastive communication to graph-structured agent topologies.\n- [IJCAI 2025 Proceedings PDF](https://www.ijcai.org/proceedings/2025/0008.pdf)\n\n### 4. MAGE: Learning Multi-Agent Communication via Graph Contrastive Learning\n- **Venue:** Pattern Recognition (2025)\n- **Description:** Uses graph contrastive learning for multi-agent communication by generating correlated graph views through stochastic corruption, then training with contrastive loss to enhance consistency of agent features. First work to extend graph contrastive learning to MARL communication.\n- [ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0031320325007538)\n\n---\n\n## STRONGLY RELEVANT PAPERS (Multi-Agent LLM Training / GRPO Extensions)\n\n### 5. M-GRPO: Multi-Agent Deep Research -- Training Multi-Agent Systems with M-GRPO\n- **arXiv:** 2511.13288 (November 2025)\n- **Description:** Extends GRPO to vertical (hierarchical) multi-agent LLM systems. Computes group-relative advantages for both main and sub-agents, introduces trajectory-alignment for variable sub-agent invocations, and uses a decoupled training pipeline where agents on separate servers exchange minimal statistics. Directly relevant as it applies GRPO to multi-agent LLM training.\n- [arXiv](https://arxiv.org/abs/2511.13288)\n\n### 6. MAGRPO: LLM Collaboration with Multi-Agent Reinforcement Learning\n- **Venue:** AAAI 2026\n- **Description:** Formalizes LLM dialogue as a Dec-POMDP and introduces Multi-Agent Group Relative Policy Optimization. Uses centralized group-relative advantages for joint optimization while preserving decentralized execution. Directly trains multiple LLMs to collaborate via shared reward signals. Open-source library CoMLRL released.\n- [arXiv](https://arxiv.org/abs/2508.04652) | [AAAI 2026 Proceedings](https://ojs.aaai.org/index.php/AAAI/article/view/40487)\n\n### 7. MARFT: Multi-Agent Reinforcement Fine-Tuning\n- **arXiv:** 2504.16129 (April 2025, updated November 2025)\n- **Description:** Introduces the MARFT paradigm for fine-tuning LLM-based multi-agent systems with RL. Proposes Flex-MG mechanism and a universal algorithmic framework specifically tailored for LLM-based MAS. Addresses the gap between traditional MARL and LLM-based multi-agent systems.\n- [arXiv](https://arxiv.org/abs/2504.16129)\n\n### 8. MARTI: A Framework for Multi-Agent LLM Systems Reinforced Training and Inference\n- **Venue:** ICLR 2026\n- **Institution:** Tsinghua University\n- **Description:** Open-source framework for training LLM-based multi-agent systems with RL. Supports centralized multi-agent interactions with distributed policy training, multi-turn asynchronous rollouts, dynamic workflows, and both verifiable and generative rewards. MARTI-v2 adds tree search-augmented RL.\n- [OpenReview](https://openreview.net/forum?id=E7jZqo0A50) | [GitHub](https://github.com/TsinghuaC3I/MARTI)\n\n### 9. MARS: Co-evolving Dual-System Deep Research via Multi-Agent Reinforcement Learning\n- **arXiv:** 2510.04935 (October 2025, updated February 2026)\n- **Description:** Co-evolution framework jointly optimizing dual cognitive systems (System 1 fast processing + System 2 deliberate reasoning) through multi-agent RL. Extends GRPO to simultaneously optimize both systems with multi-turn tool interactions. Relevant as it trains bilateral agent roles with shared trajectory rewards.\n- [arXiv](https://arxiv.org/abs/2510.04935)\n\n---\n\n## RELEVANT PAPERS (Communication Optimization / Latent Communication)\n\n### 10. LatentMAS: Latent Collaboration in Multi-Agent Systems\n- **Venue:** ICML 2026 Spotlight\n- **arXiv:** 2511.20639 (November 2025)\n- **Description:** Moves agent collaboration from token space into latent space. Agents communicate by passing latent thoughts (last-layer hidden embeddings) through shared working memory. Achieves up to 14.6% accuracy improvement with 70-84% token reduction and 4x faster inference. Training-free latent-space alignment.\n- [arXiv](https://arxiv.org/abs/2511.20639) | [GitHub](https://github.com/Gen-Verse/LatentMAS)\n\n### 11. The Vision Wormhole: Latent-Space Communication in Heterogeneous Multi-Agent Systems\n- **arXiv:** 2602.15382 (February 2026)\n- **Description:** Maps heterogeneous reasoning traces into a shared continuous latent space via a Universal Visual Codec and injects them into the receiver's visual pathway. Uses self-supervised distillation (teacher-student) to align high-speed visual channel with text-based reasoning. Reduces sender-receiver alignment complexity from O(N^2) to O(N) with hub-and-spoke topology.\n- [arXiv](https://arxiv.org/abs/2602.15382)\n\n### 12. Adapting LLM Agents Through Communication (LTC)\n- **Venue:** Under review / OpenReview\n- **arXiv:** 2310.01444\n- **Description:** Proposes Learning Through Communication (LTC), enabling LLM agents to improve through interactions with environments and other agents. Defines three communication patterns: single-agent monologue, multi-agent dialogue, and teacher-student dialogue. Uses universal buffer for linguistic and reward feedback with iterative policy updates.\n- [OpenReview](https://openreview.net/forum?id=wOelVq8fwL)\n\n### 13. Cut the Crap: An Economical Communication Pipeline for LLM-based Multi-Agent Systems (AgentPrune)\n- **Venue:** ICLR 2025\n- **arXiv:** 2410.02506\n- **Description:** Identifies and formalizes communication redundancy in LLM-based multi-agent pipelines. Proposes AgentPrune for one-shot pruning of the spatial-temporal message-passing graph. Achieves comparable results with ~87% cost reduction.\n- [arXiv](https://arxiv.org/abs/2410.02506)\n\n### 14. Language Grounded Multi-Agent Reinforcement Learning with Human-Interpretable Communication\n- **arXiv:** 2409.17348 (September 2024, updated 2025)\n- **Description:** Grounds MARL agent communication in natural language using synthetic data from embodied LLMs. Demonstrates zero-shot generalization in ad-hoc teamwork with unseen teammates. Combines RL loss with supervised learning loss for end-to-end training.\n- [arXiv](https://arxiv.org/abs/2409.17348)\n\n---\n\n## CONTEXTUAL / SURVEY PAPERS\n\n### 15. Beyond Self-Talk: A Communication-Centric Survey of LLM-Based Multi-Agent Systems\n- **arXiv:** 2502.14321 (February 2025, updated June 2025)\n- **Description:** Comprehensive survey examining LLM-based MAS from a communication perspective. Proposes a framework integrating system-level communication (architecture, goals, protocols) with internal communication (strategies, paradigms, content). Highlights challenges in communication efficiency, security, and scalability.\n- [arXiv](https://arxiv.org/abs/2502.14321)\n\n### 16. Reinforcement Learning for LLM-based Multi-Agent Systems through Orchestration Traces\n- **arXiv:** 2605.02801 (May 2026)\n- **Description:** Surveys and systematizes RL methods for LLM-based MAS through orchestration traces. Documents the recent emergence of hierarchical GRPO decompositions, message-level counterfactual credit assignment, and Shapley-based agent-level credit methods from 2025-Q2 through May 2026.\n- [arXiv](https://arxiv.org/abs/2605.02801)\n\n### 17. Active Learning for Communication Structure Optimization in LLM-Based Multi-Agent Systems\n- **arXiv:** 2605.05703 (May 2026)\n- **Authors:** Huchen Yang, Xinghao Dong, Dan Negrut, Jin-Long Wu\n- **Description:** Optimizes communication topology in LLM-based MAS using active learning. Directly relevant to the structural aspects of multi-agent communication design.\n\n---\n\n## KEY GAP ANALYSIS\n\nBased on this extensive search, the specific niche of **bilateral contrastive training applied to sender AND receiver in multi-agent LLM systems** does not appear to have been published. The closest works are:\n\n- **CACL (ICLR 2024)** does bilateral contrastive alignment of agent messages, but in small MARL models, not LLMs.\n- **MAGRPO / M-GRPO / MARFT** apply GRPO-based RL to multi-agent LLM training, but do not use contrastive objectives on the communication channel itself.\n- **LatentMAS and Vision Wormhole** address sender-receiver alignment in LLM agents, but through latent-space distillation rather than contrastive losses.\n- **No paper found** applies a CLIP/CLIPO-style contrastive loss specifically to bilateral sender-receiver LLM communication in multi-agent systems.\n\nThe proposal's combination of (a) contrastive loss on the communication channel + (b) applied to LLM-scale agents + (c) bilateral training of both sender and receiver appears to be a novel intersection as of May 2026. The most threatening concurrent work would be CACL's potential extension to LLMs, and the GRPO-family papers (MAGRPO, M-GRPO, MARTI, MARFT) which could be combined with contrastive communication objectives."
      }
    ],
    "totalDurationMs": 150403,
    "totalTokens": 36335,
    "totalToolUseCount": 25,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1348,
      "cache_read_input_tokens": 31996,
      "output_tokens": 2990,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1348
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2990,
          "cache_read_input_tokens": 31996,
          "cache_creation_input_tokens": 1348,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1348,
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
  "sourceToolAssistantUUID": "65e2940a-fb82-4b0b-8cbc-8bdb466a1d2f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c886791-a9d9-487c-99a0-b2a7b1d3d99e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-10T22:14:17.660Z_

<details><summary>↩ Tool result · `toolu_01P2zR2tUdwBuCp5Z8NaT7Uu`</summary>

```text
Now I have comprehensive findings. Here is my full report:

---

## Verification of Cited Papers

### 1. DiffMAS (arXiv 2604.21794) -- EXISTS
**Title:** "Learning to Communicate: Toward End-to-End Optimization of Multi-Agent Language Systems"
- Submitted April 23, 2026; under review at COLM 2026
- Proposes DiffMAS, a training framework that treats latent communication (via KV caches) as a differentiable, learnable component of multi-agent systems
- Reports up to +26.7% improvement on AIME24 and consistent gains across reasoning benchmarks

### 2. RecursiveMAS (arXiv 2604.25917) -- EXISTS
**Title:** "Recursive Multi-Agent Systems"
- Submitted April 28, 2026
- Framework treats the entire multi-agent system as a unified latent-space recursive computation
- Reports 8.3% average accuracy gains and significant speedup across benchmarks in math, science, medicine, and code generation
- The entire loop is differentiable, enabling backpropagation through all rounds and agents simultaneously

### 3. CoFi-PGMA (arXiv 2604.22785) -- EXISTS
**Title:** "CoFi-PGMA: Counterfactual Policy Gradients under Filtered Feedback for Multi-Agent LLMs"
- Submitted April 3, 2026
- Derives a counterfactual per-agent training objective based on marginal contribution
- Corrects learning signals under both routing and collaborative mechanisms
- Addresses credit assignment problems when standard RLHF objectives become misspecified in multi-agent contexts

### 4. Graph-GRPO (arXiv 2603.02701) -- EXISTS
**Title:** "Graph-GRPO: Stabilizing Multi-Agent Topology Learning via Group Relative Policy Optimization"
- Submitted March 3, 2026
- Integrates GRPO to improve how agents learn to construct task-specific communication graphs
- Samples diverse topologies and computes edge advantages through relative performance comparison
- Addresses gradient variance and credit assignment challenges

### 5. EMA-PG (arXiv 2602.04417) -- EXISTS
**Title:** "EMA Policy Gradient: Taming Reinforcement Learning for LLMs with EMA Anchor and Top-k KL"
- Submitted February 4, 2026
- Replaces fixed anchor policies with exponential moving average mechanism (analogous to target networks in Q-learning)
- Introduces Top-k KL estimator for flexible KL divergence calculations
- Code publicly available on GitHub

### 6. arXiv 2605.02801 -- EXISTS
**Title:** "Reinforcement Learning for LLM-based Multi-Agent Systems through Orchestration Traces"
- Submitted May 4, 2026
- Documents Moonshot's Kimi K2.5 introducing Agent Swarm trained with Parallel-Agent Reinforcement Learning (PARL), scaling to 4,000 coordinated steps
- Studies orchestration traces as temporal interaction graphs (sub-agent spawning, delegation, communication, tool use, return, aggregation, stopping)
- Identifies reward design spanning eight families including orchestration rewards

**All six cited papers exist and are verified on arXiv.**

---

## Additional Relevant Papers NOT Cited in the Proposal

The following recent papers were found through the searches and may be relevant to the proposal:

### Training Stability and Credit Assignment

1. **Dr. MAS** (arXiv 2602.08847, Feb 2026) -- Identifies that GRPO-style global normalization baselines deviate from diverse agents' reward distributions, causing gradient-norm instability. Proposes agent-wise advantage normalization. End-to-end RL training framework supporting heterogeneous LLMs. Open-sourced at [github.com/langfengQ/DrMAS](https://github.com/langfengQ/DrMAS).

2. **Stronger-MAS / AT-GRPO** (arXiv 2510.11062, ICLR 2026) -- Proposes Agent- and Turn-wise GRPO (AT-GRPO), noting standard GRPO grouping assumptions break down when prompts vary by role and turn. Boosts long-horizon planning accuracy from 14-47% to 96-99.5%. Open-sourced as PettingLLMs framework.

3. **CCPO: Counterfactual Credit Policy Optimization** (arXiv 2603.21563, March 2026) -- Builds dynamic counterfactual baselines simulating outcomes with an agent's contribution removed, yielding role-sensitive advantages. Addresses free-riding in collaborative LLM training.

4. **MHGPO: Multi-Agent Heterogeneous Group Policy Optimization** (arXiv 2506.02718) -- Critic-free algorithm that guides policy updates by estimating relative reward advantages across heterogeneous groups of rollouts.

5. **ProxMO** (arXiv 2602.19225, Feb 2026) -- Proximity-Based Multi-Turn Optimization for practical credit assignment in LLM agent training. Plug-and-play compatible with standard GRPO frameworks.

6. **RTMC** (arXiv 2604.11037, April 2026) -- Step-level credit assignment via rollout trees. Aggregates return statistics across rollouts sharing common state to produce per-step advantages without a learned critic.

### Latent Communication

7. **LatentMAS** (arXiv 2511.20639, ICML 2026 Spotlight) -- Training-free framework for pure latent collaboration among LLM agents. Agents communicate via last-layer hidden embeddings through shared latent working memory. Up to 14.6% higher accuracy, 70-84% fewer tokens, 4x faster inference.

8. **When Less Latent Leads to Better Relay** (arXiv 2604.13349, April 2026) -- Information-preserving compression for latent multi-agent LLM collaboration. Introduces Orthogonal Backfill (OBF) to reduce memory/communication cost of full KV relay while mitigating information loss.

9. **LMNet: Dense Communication between Language Models** (arXiv 2505.12741, May 2025) -- Proposes dense vector communication between LLMs using stripped LLMs as vertices and optimizable seq2seq modules as edges. Fully differentiable. LMNet-1B achieves competitive performance with <0.1% training cost.

10. **Interlat** (arXiv 2511.09149) -- Paradigm for direct inter-agent communication entirely in latent space by transmitting last-layer hidden states.

### Meta-Reasoning and Architecture

11. **ReMA** (arXiv 2503.09501, March 2025) -- Decouples reasoning into a high-level meta-thinking agent and low-level reasoning agent, trained via multi-agent RL. Outperforms single-agent RL baselines on competitive math and LLM-as-Judge benchmarks.

12. **Coordination as an Architectural Layer for LLM-Based Multi-Agent Systems** (arXiv 2605.03310, May 2026) -- Argues coordination should be a configurable architectural layer separable from agent logic. Notes multi-agent LLM systems fail in production at 41-87% rates, mostly from coordination defects.

13. **A Brief Overview: Agentic Reinforcement Learning In Large Language Models** (arXiv 2604.27859, April 2026) -- Comprehensive survey of agentic RL paradigms.

14. **From Reasoning to Agentic: Credit Assignment in Reinforcement Learning for Large Language Models** (arXiv 2604.09459, April 2026) -- Survey covering credit assignment methods for LLM RL published January 2024 through April 2026.

15. **Governed Collaborative Memory as Artificial Selection in LLM-Based Multi-Agent Systems** (arXiv 2605.04264, May 2026) -- Addresses persistent memory turning LLM agents from stateless participants into state-bearing components.

---

## Summary

All six papers cited in the proposal are verified as real and existing on arXiv with the stated IDs and topics. The searches uncovered at least 15 additional highly relevant papers from 2025-2026 that are not cited, with the most significant being:

- **Dr. MAS** and **Stronger-MAS/AT-GRPO** directly address GRPO instability in multi-agent settings (the core problem space)
- **CCPO** provides counterfactual credit assignment for multi-agent collaboration
- **LatentMAS** (ICML 2026 Spotlight) and its compression follow-up are directly relevant to latent communication
- **LMNet** proposes end-to-end differentiable dense communication between LLMs
- Two comprehensive surveys (arXiv 2604.09459 and 2604.27859) cover the field broadly

Sources:
- [DiffMAS - arXiv 2604.21794](https://arxiv.org/abs/2604.21794)
- [RecursiveMAS - arXiv 2604.25917](https://arxiv.org/abs/2604.25917)
- [CoFi-PGMA - arXiv 2604.22785](https://arxiv.org/abs/2604.22785)
- [Graph-GRPO - arXiv 2603.02701](https://arxiv.org/abs/2603.02701)
- [EMA-PG - arXiv 2602.04417](https://arxiv.org/abs/2602.04417)
- [RL for LLM-based MAS through Orchestration Traces - arXiv 2605.02801](https://arxiv.org/abs/2605.02801)
- [Dr. MAS - arXiv 2602.08847](https://arxiv.org/abs/2602.08847)
- [Stronger-MAS - arXiv 2510.11062](https://arxiv.org/abs/2510.11062)
- [CCPO - arXiv 2603.21563](https://arxiv.org/abs/2603.21563)
- [MHGPO - arXiv 2506.02718](https://arxiv.org/abs/2506.02718)
- [ProxMO - arXiv 2602.19225](https://arxiv.org/abs/2602.19225)
- [RTMC - arXiv 2604.11037](https://arxiv.org/abs/2604.11037)
- [LatentMAS - arXiv 2511.20639](https://arxiv.org/abs/2511.20639)
- [Latent Compression - arXiv 2604.13349](https://arxiv.org/abs/2604.13349)
- [LMNet - arXiv 2505.12741](https://arxiv.org/abs/2505.12741)
- [Interlat - arXiv 2511.09149](https://arxiv.org/abs/2511.09149)
- [ReMA - arXiv 2503.09501](https://arxiv.org/abs/2503.09501)
- [Coordination as Architectural Layer - arXiv 2605.03310](https://arxiv.org/abs/2605.03310)
- [Agentic RL Overview - arXiv 2604.27859](https://arxiv.org/abs/2604.27859)
- [Credit Assignment Survey - arXiv 2604.09459](https://arxiv.org/abs/2604.09459)
- [Governed Collaborative Memory - arXiv 2605.04264](https://arxiv.org/abs/2605.04264)

agentId: ae1b4400f09425013 (use SendMessage with to: 'ae1b4400f09425013' to continue this agent)
&lt;usage>total_tokens: 30988
tool_uses: 22
duration_ms: 148919&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "257aa37c-d8ca-49ae-b3de-d7fd1f830f97",
  "isSidechain": false,
  "promptId": "c4053383-51a2-4c53-bef4-50bbbd8ab467",
  "type": "user",
  "uuid": "a1337155-cd10-4cdb-a237-8e85cb65e541",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Search the web for the very latest papers (April-May 2026) on multi-agent LLM training, especially:\n\n1. Search \"multi-agent LLM reinforcement learning 2026 arxiv\" \n2. Search \"multi-agent GRPO communication 2026\"\n3. Search \"LLM agent communication training contrastive 2026\"\n4. Search for arxiv 2605 papers about multi-agent LLM systems\n5. Search \"site:arxiv.org multi-agent LLM training May 2026\"\n\nAlso verify these specific papers the proposal cites:\n- DiffMAS (arXiv 2604.21794) - does it exist?\n- RecursiveMAS (arXiv 2604.25917) - does it exist?\n- CoFi-PGMA (arXiv 2604.22785) - does it exist?\n- Graph-GRPO (March 2026, arXiv 2603.02701) - does it exist?\n- EMA-PG (arXiv 2602.04417) - does it exist?\n- arXiv 2605.02801 about \"Reinforcement Learning for LLM-based MAS through Orchestration Traces\" - does it exist?\n\nReport all findings including any new papers not cited in the proposal.",
    "agentId": "ae1b4400f09425013",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have comprehensive findings. Here is my full report:\n\n---\n\n## Verification of Cited Papers\n\n### 1. DiffMAS (arXiv 2604.21794) -- EXISTS\n**Title:** \"Learning to Communicate: Toward End-to-End Optimization of Multi-Agent Language Systems\"\n- Submitted April 23, 2026; under review at COLM 2026\n- Proposes DiffMAS, a training framework that treats latent communication (via KV caches) as a differentiable, learnable component of multi-agent systems\n- Reports up to +26.7% improvement on AIME24 and consistent gains across reasoning benchmarks\n\n### 2. RecursiveMAS (arXiv 2604.25917) -- EXISTS\n**Title:** \"Recursive Multi-Agent Systems\"\n- Submitted April 28, 2026\n- Framework treats the entire multi-agent system as a unified latent-space recursive computation\n- Reports 8.3% average accuracy gains and significant speedup across benchmarks in math, science, medicine, and code generation\n- The entire loop is differentiable, enabling backpropagation through all rounds and agents simultaneously\n\n### 3. CoFi-PGMA (arXiv 2604.22785) -- EXISTS\n**Title:** \"CoFi-PGMA: Counterfactual Policy Gradients under Filtered Feedback for Multi-Agent LLMs\"\n- Submitted April 3, 2026\n- Derives a counterfactual per-agent training objective based on marginal contribution\n- Corrects learning signals under both routing and collaborative mechanisms\n- Addresses credit assignment problems when standard RLHF objectives become misspecified in multi-agent contexts\n\n### 4. Graph-GRPO (arXiv 2603.02701) -- EXISTS\n**Title:** \"Graph-GRPO: Stabilizing Multi-Agent Topology Learning via Group Relative Policy Optimization\"\n- Submitted March 3, 2026\n- Integrates GRPO to improve how agents learn to construct task-specific communication graphs\n- Samples diverse topologies and computes edge advantages through relative performance comparison\n- Addresses gradient variance and credit assignment challenges\n\n### 5. EMA-PG (arXiv 2602.04417) -- EXISTS\n**Title:** \"EMA Policy Gradient: Taming Reinforcement Learning for LLMs with EMA Anchor and Top-k KL\"\n- Submitted February 4, 2026\n- Replaces fixed anchor policies with exponential moving average mechanism (analogous to target networks in Q-learning)\n- Introduces Top-k KL estimator for flexible KL divergence calculations\n- Code publicly available on GitHub\n\n### 6. arXiv 2605.02801 -- EXISTS\n**Title:** \"Reinforcement Learning for LLM-based Multi-Agent Systems through Orchestration Traces\"\n- Submitted May 4, 2026\n- Documents Moonshot's Kimi K2.5 introducing Agent Swarm trained with Parallel-Agent Reinforcement Learning (PARL), scaling to 4,000 coordinated steps\n- Studies orchestration traces as temporal interaction graphs (sub-agent spawning, delegation, communication, tool use, return, aggregation, stopping)\n- Identifies reward design spanning eight families including orchestration rewards\n\n**All six cited papers exist and are verified on arXiv.**\n\n---\n\n## Additional Relevant Papers NOT Cited in the Proposal\n\nThe following recent papers were found through the searches and may be relevant to the proposal:\n\n### Training Stability and Credit Assignment\n\n1. **Dr. MAS** (arXiv 2602.08847, Feb 2026) -- Identifies that GRPO-style global normalization baselines deviate from diverse agents' reward distributions, causing gradient-norm instability. Proposes agent-wise advantage normalization. End-to-end RL training framework supporting heterogeneous LLMs. Open-sourced at [github.com/langfengQ/DrMAS](https://github.com/langfengQ/DrMAS).\n\n2. **Stronger-MAS / AT-GRPO** (arXiv 2510.11062, ICLR 2026) -- Proposes Agent- and Turn-wise GRPO (AT-GRPO), noting standard GRPO grouping assumptions break down when prompts vary by role and turn. Boosts long-horizon planning accuracy from 14-47% to 96-99.5%. Open-sourced as PettingLLMs framework.\n\n3. **CCPO: Counterfactual Credit Policy Optimization** (arXiv 2603.21563, March 2026) -- Builds dynamic counterfactual baselines simulating outcomes with an agent's contribution removed, yielding role-sensitive advantages. Addresses free-riding in collaborative LLM training.\n\n4. **MHGPO: Multi-Agent Heterogeneous Group Policy Optimization** (arXiv 2506.02718) -- Critic-free algorithm that guides policy updates by estimating relative reward advantages across heterogeneous groups of rollouts.\n\n5. **ProxMO** (arXiv 2602.19225, Feb 2026) -- Proximity-Based Multi-Turn Optimization for practical credit assignment in LLM agent training. Plug-and-play compatible with standard GRPO frameworks.\n\n6. **RTMC** (arXiv 2604.11037, April 2026) -- Step-level credit assignment via rollout trees. Aggregates return statistics across rollouts sharing common state to produce per-step advantages without a learned critic.\n\n### Latent Communication\n\n7. **LatentMAS** (arXiv 2511.20639, ICML 2026 Spotlight) -- Training-free framework for pure latent collaboration among LLM agents. Agents communicate via last-layer hidden embeddings through shared latent working memory. Up to 14.6% higher accuracy, 70-84% fewer tokens, 4x faster inference.\n\n8. **When Less Latent Leads to Better Relay** (arXiv 2604.13349, April 2026) -- Information-preserving compression for latent multi-agent LLM collaboration. Introduces Orthogonal Backfill (OBF) to reduce memory/communication cost of full KV relay while mitigating information loss.\n\n9. **LMNet: Dense Communication between Language Models** (arXiv 2505.12741, May 2025) -- Proposes dense vector communication between LLMs using stripped LLMs as vertices and optimizable seq2seq modules as edges. Fully differentiable. LMNet-1B achieves competitive performance with <0.1% training cost.\n\n10. **Interlat** (arXiv 2511.09149) -- Paradigm for direct inter-agent communication entirely in latent space by transmitting last-layer hidden states.\n\n### Meta-Reasoning and Architecture\n\n11. **ReMA** (arXiv 2503.09501, March 2025) -- Decouples reasoning into a high-level meta-thinking agent and low-level reasoning agent, trained via multi-agent RL. Outperforms single-agent RL baselines on competitive math and LLM-as-Judge benchmarks.\n\n12. **Coordination as an Architectural Layer for LLM-Based Multi-Agent Systems** (arXiv 2605.03310, May 2026) -- Argues coordination should be a configurable architectural layer separable from agent logic. Notes multi-agent LLM systems fail in production at 41-87% rates, mostly from coordination defects.\n\n13. **A Brief Overview: Agentic Reinforcement Learning In Large Language Models** (arXiv 2604.27859, April 2026) -- Comprehensive survey of agentic RL paradigms.\n\n14. **From Reasoning to Agentic: Credit Assignment in Reinforcement Learning for Large Language Models** (arXiv 2604.09459, April 2026) -- Survey covering credit assignment methods for LLM RL published January 2024 through April 2026.\n\n15. **Governed Collaborative Memory as Artificial Selection in LLM-Based Multi-Agent Systems** (arXiv 2605.04264, May 2026) -- Addresses persistent memory turning LLM agents from stateless participants into state-bearing components.\n\n---\n\n## Summary\n\nAll six papers cited in the proposal are verified as real and existing on arXiv with the stated IDs and topics. The searches uncovered at least 15 additional highly relevant papers from 2025-2026 that are not cited, with the most significant being:\n\n- **Dr. MAS** and **Stronger-MAS/AT-GRPO** directly address GRPO instability in multi-agent settings (the core problem space)\n- **CCPO** provides counterfactual credit assignment for multi-agent collaboration\n- **LatentMAS** (ICML 2026 Spotlight) and its compression follow-up are directly relevant to latent communication\n- **LMNet** proposes end-to-end differentiable dense communication between LLMs\n- Two comprehensive surveys (arXiv 2604.09459 and 2604.27859) cover the field broadly\n\nSources:\n- [DiffMAS - arXiv 2604.21794](https://arxiv.org/abs/2604.21794)\n- [RecursiveMAS - arXiv 2604.25917](https://arxiv.org/abs/2604.25917)\n- [CoFi-PGMA - arXiv 2604.22785](https://arxiv.org/abs/2604.22785)\n- [Graph-GRPO - arXiv 2603.02701](https://arxiv.org/abs/2603.02701)\n- [EMA-PG - arXiv 2602.04417](https://arxiv.org/abs/2602.04417)\n- [RL for LLM-based MAS through Orchestration Traces - arXiv 2605.02801](https://arxiv.org/abs/2605.02801)\n- [Dr. MAS - arXiv 2602.08847](https://arxiv.org/abs/2602.08847)\n- [Stronger-MAS - arXiv 2510.11062](https://arxiv.org/abs/2510.11062)\n- [CCPO - arXiv 2603.21563](https://arxiv.org/abs/2603.21563)\n- [MHGPO - arXiv 2506.02718](https://arxiv.org/abs/2506.02718)\n- [ProxMO - arXiv 2602.19225](https://arxiv.org/abs/2602.19225)\n- [RTMC - arXiv 2604.11037](https://arxiv.org/abs/2604.11037)\n- [LatentMAS - arXiv 2511.20639](https://arxiv.org/abs/2511.20639)\n- [Latent Compression - arXiv 2604.13349](https://arxiv.org/abs/2604.13349)\n- [LMNet - arXiv 2505.12741](https://arxiv.org/abs/2505.12741)\n- [Interlat - arXiv 2511.09149](https://arxiv.org/abs/2511.09149)\n- [ReMA - arXiv 2503.09501](https://arxiv.org/abs/2503.09501)\n- [Coordination as Architectural Layer - arXiv 2605.03310](https://arxiv.org/abs/2605.03310)\n- [Agentic RL Overview - arXiv 2604.27859](https://arxiv.org/abs/2604.27859)\n- [Credit Assignment Survey - arXiv 2604.09459](https://arxiv.org/abs/2604.09459)\n- [Governed Collaborative Memory - arXiv 2605.04264](https://arxiv.org/abs/2605.04264)"
      }
    ],
    "totalDurationMs": 148919,
    "totalTokens": 30988,
    "totalToolUseCount": 22,
    "usage": {
      "input_tokens": 809,
      "cache_creation_input_tokens": 2034,
      "cache_read_input_tokens": 25280,
      "output_tokens": 2865,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2034
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 809,
          "output_tokens": 2865,
          "cache_read_input_tokens": 25280,
          "cache_creation_input_tokens": 2034,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2034,
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
      "otherToolCount": 22
    }
  },
  "sourceToolAssistantUUID": "257aa37c-d8ca-49ae-b3de-d7fd1f830f97",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c886791-a9d9-487c-99a0-b2a7b1d3d99e",
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
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-10 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "a1337155-cd10-4cdb-a237-8e85cb65e541",
  "sessionId": "0c886791-a9d9-487c-99a0-b2a7b1d3d99e"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "Bilateral intent grounding for multi-agent LLM communication",
  "sessionId": "0c886791-a9d9-487c-99a0-b2a7b1d3d99e"
}
```

---

### Assistant

_source line 22 · 2026-05-10T22:14:23.406Z_

Good, I have extensive verification data. Let me now do targeted searches on the most critical remaining concerns.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a1337155-cd10-4cdb-a237-8e85cb65e541",
  "isSidechain": false,
  "requestId": "req_011Cauf9fuSPRxWPVBxvLDgw",
  "type": "assistant",
  "uuid": "cffa9610-365c-483a-b915-01a9b7e3e50d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c886791-a9d9-487c-99a0-b2a7b1d3d99e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CgeUYp448NzLv3uTBVVZ66",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11317,
      "cache_read_input_tokens": 37214,
      "output_tokens": 786,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11317,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 786,
          "cache_read_input_tokens": 37214,
          "cache_creation_input_tokens": 11317,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11317
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-10T22:14:32.701Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01VGH83ZswZtHNFCEzivQJXc`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Verify AIME benchmark and PettingLLMs multi-agent discussion format",
  "prompt": "I need to verify a specific claim about a research proposal. The proposal says it will use \"PettingLLMs AIME multi-agent discussion\" as its evaluation benchmark for a multi-agent communication training paper targeting EMNLP 2026.\n\nThe user's hard constraint says benchmarks must be from this list: AgentBench, WebArena, SWE-bench Verified, GAIA, ToolBench, ALFWorld, Mind2Web, τ-bench.\n\nAIME is NOT on this list. \n\nHowever, I need to understand:\n1. Is AIME (American Invitational Mathematics Examination) a standard benchmark used in LLM agent research?\n2. Does PettingLLMs actually implement a multi-agent DISCUSSION format for AIME where agents exchange text messages? Search for specifics about how PettingLLMs structures multi-agent math problem solving.\n3. Is AIME24 a commonly used evaluation benchmark in the multi-agent LLM literature?\n\nAlso search:\n4. \"AT-GRPO multi-agent discussion format AIME\" to understand what the multi-agent setup looks like\n5. Whether there's a mismatch between AIME (a math exam) and the user's allowed benchmarks (which are all agent/tool-use benchmarks)\n\nReport your findings carefully."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cffa9610-365c-483a-b915-01a9b7e3e50d",
  "isSidechain": false,
  "requestId": "req_011Cauf9fuSPRxWPVBxvLDgw",
  "type": "assistant",
  "uuid": "3fde3df9-ba74-4cfc-a27d-6a4950a5686d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c886791-a9d9-487c-99a0-b2a7b1d3d99e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CgeUYp448NzLv3uTBVVZ66",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11317,
      "cache_read_input_tokens": 37214,
      "output_tokens": 786,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11317,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 786,
          "cache_read_input_tokens": 37214,
          "cache_creation_input_tokens": 11317,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11317
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-10T22:14:41.841Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01NscAgcNjNExYgosnuEjFMy`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Search for MAPoRL and Social Deduction LLM verification",
  "prompt": "Search the web to verify these papers and understand what they do:\n\n1. MAPoRL (ACL 2025) - \"Multi-Agent Post-Co-Training for Collaborative LLMs\" \n   - Search for this paper on arxiv and Google Scholar\n   - Does it co-train generation and comprehension?\n   - Does it use contrastive objectives?\n\n2. Social Deduction LLM (AAMAS 2025, arXiv 2502.06060) - \"Training Language Models for Social Deduction with Multi-Agent RL\"\n   - Does it train receiver-side listening loss?\n   - Is it task-specific (Among Us)?\n   - Is it non-contrastive?\n\n3. Also search for any paper that does \"bilateral\" or \"bidirectional\" contrastive training of both sender and receiver communication in LLM agents, specifically from 2025-2026.\n\n4. Search for \"MAGE contrastive multi-agent communication 2025\" - there was a mention of MAGE (Pattern Recognition 2025) doing graph contrastive learning for multi-agent communication. Is this relevant as a missing citation?\n\nReport exactly what you find."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3fde3df9-ba74-4cfc-a27d-6a4950a5686d",
  "isSidechain": false,
  "requestId": "req_011Cauf9fuSPRxWPVBxvLDgw",
  "type": "assistant",
  "uuid": "67d6ec1a-4cc1-4b66-ae51-0e3804f02d4e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c886791-a9d9-487c-99a0-b2a7b1d3d99e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CgeUYp448NzLv3uTBVVZ66",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11317,
      "cache_read_input_tokens": 37214,
      "output_tokens": 786,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11317,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 786,
          "cache_read_input_tokens": 37214,
          "cache_creation_input_tokens": 11317,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11317
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-10T22:16:05.905Z_

<details><summary>↩ Tool result · `toolu_01VGH83ZswZtHNFCEzivQJXc`</summary>

```text
I now have comprehensive findings. Here is my report:

---

## Findings

### 1. Is AIME a standard benchmark used in LLM agent research?

**No -- AIME is a standard benchmark for LLM *mathematical reasoning*, not for LLM *agent* research.** AIME (American Invitational Mathematics Examination) is a well-established evaluation for testing whether an LLM can solve competition-level math problems. It consists of 15 problems per session (30 total across AIME I and II), each requiring an integer answer between 0-999. It is a **static, single-turn reasoning benchmark** -- there is no environment interaction, no tool use, no grounding, and no multi-step task execution in a dynamic setting. Major leaderboards track AIME 2024, 2025, and 2026 scores as a measure of mathematical reasoning capability.

This is categorically different from the benchmarks on the user's allowed list (AgentBench, WebArena, SWE-bench Verified, GAIA, ToolBench, ALFWorld, Mind2Web, tau-bench), which all evaluate **agentic capabilities**: planning, tool use, environment interaction, multi-step task completion, web navigation, code editing, etc.

### 2. Does PettingLLMs implement a multi-agent DISCUSSION format for AIME?

**PettingLLMs is a real framework** (ICLR 2026 paper titled "Stronger-MAS"), available at `https://github.com/pettingllms-ai/PettingLLMs`. It implements AT-GRPO (Agent- and Turn-wise Group Relative Policy Optimization) for training collaborative multi-agent LLM systems. It does support AIME as one of its math environments (alongside OlympiadBench).

However, the specifics of the "discussion" format are important to understand:
- PettingLLMs enables multi-turn interactions where agents revise outputs using environment feedback. For code tasks, this is explicit (Coder + Unit-Tester exchanging artifacts). For math tasks like AIME, the multi-agent setup involves agents collaborating on reasoning, but **the core task remains solving a math problem with an integer answer** -- not navigating an environment, using tools, or completing agentic tasks.
- The "discussion" is a **training methodology** (agents exchanging reasoning steps to arrive at a math answer), not an **agent benchmark** in the sense of the user's allowed list. It is closer to "multi-agent debate for reasoning" than to "agent evaluation in an interactive environment."

### 3. Is AIME24 a commonly used evaluation benchmark in multi-agent LLM literature?

AIME24 is commonly used in LLM evaluation literature broadly, particularly for mathematical reasoning and RL-based post-training. It is used in some multi-agent work (e.g., M-GRPO papers), but primarily as a **downstream task to measure reasoning quality**, not as a benchmark for evaluating agent communication, tool use, or environmental interaction. It is not a "multi-agent benchmark" in the way that MultiAgentBench or the user's allowed benchmarks are.

### 4. AT-GRPO multi-agent discussion format for AIME

AT-GRPO (Agent- and Turn-wise Group Relative Policy Optimization) provides fine-grained credit assignment at both the agent and turn level. In a multi-agent AIME setup, multiple agents exchange reasoning about a math problem across turns. The "one-round discussion" baseline involves agents receiving the same prompt, generating responses, and then having their prompts augmented with each other's first-turn responses in a second turn. This is a **reasoning refinement protocol**, not an interactive agent task.

### 5. The fundamental mismatch

There is a clear categorical mismatch between AIME and the user's allowed benchmarks:

| Property | User's Allowed Benchmarks | AIME |
|---|---|---|
| Environment interaction | Yes (web, code repos, household, APIs) | No |
| Tool use | Yes | No |
| Multi-step task execution | Yes (dynamic, stateful) | No (single answer) |
| What it measures | Agentic capability | Mathematical reasoning |
| Answer format | Task completion in environment | Integer 0-999 |

**The user's allowed list consists entirely of agent/tool-use benchmarks.** AIME is a math reasoning benchmark. Even when wrapped in a PettingLLMs multi-agent discussion format, the underlying evaluation is still "did the agents produce the correct integer answer to a math competition problem" -- not "did the agents successfully navigate an environment, use tools, and complete a multi-step task."

### Bottom Line

The proposal's use of "PettingLLMs AIME multi-agent discussion" as an evaluation benchmark does not satisfy the user's constraint. While PettingLLMs is a legitimate framework and AIME is a legitimate benchmark, AIME is fundamentally a math reasoning evaluation, not an agent/tool-use benchmark. It is not on the allowed list, and it is not a substitute for any benchmark on the allowed list. The benchmarks on the allowed list all evaluate interactive, environment-grounded, tool-using agent behavior -- a completely different evaluation paradigm from competition math problem solving.

agentId: ae1786ce142949517 (use SendMessage with to: 'ae1786ce142949517' to continue this agent)
&lt;usage>total_tokens: 21964
tool_uses: 11
duration_ms: 93201&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3fde3df9-ba74-4cfc-a27d-6a4950a5686d",
  "isSidechain": false,
  "promptId": "c4053383-51a2-4c53-bef4-50bbbd8ab467",
  "type": "user",
  "uuid": "ec4ab065-7486-43e8-bbeb-0d90f39bbaf3",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to verify a specific claim about a research proposal. The proposal says it will use \"PettingLLMs AIME multi-agent discussion\" as its evaluation benchmark for a multi-agent communication training paper targeting EMNLP 2026.\n\nThe user's hard constraint says benchmarks must be from this list: AgentBench, WebArena, SWE-bench Verified, GAIA, ToolBench, ALFWorld, Mind2Web, τ-bench.\n\nAIME is NOT on this list. \n\nHowever, I need to understand:\n1. Is AIME (American Invitational Mathematics Examination) a standard benchmark used in LLM agent research?\n2. Does PettingLLMs actually implement a multi-agent DISCUSSION format for AIME where agents exchange text messages? Search for specifics about how PettingLLMs structures multi-agent math problem solving.\n3. Is AIME24 a commonly used evaluation benchmark in the multi-agent LLM literature?\n\nAlso search:\n4. \"AT-GRPO multi-agent discussion format AIME\" to understand what the multi-agent setup looks like\n5. Whether there's a mismatch between AIME (a math exam) and the user's allowed benchmarks (which are all agent/tool-use benchmarks)\n\nReport your findings carefully.",
    "agentId": "ae1786ce142949517",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "I now have comprehensive findings. Here is my report:\n\n---\n\n## Findings\n\n### 1. Is AIME a standard benchmark used in LLM agent research?\n\n**No -- AIME is a standard benchmark for LLM *mathematical reasoning*, not for LLM *agent* research.** AIME (American Invitational Mathematics Examination) is a well-established evaluation for testing whether an LLM can solve competition-level math problems. It consists of 15 problems per session (30 total across AIME I and II), each requiring an integer answer between 0-999. It is a **static, single-turn reasoning benchmark** -- there is no environment interaction, no tool use, no grounding, and no multi-step task execution in a dynamic setting. Major leaderboards track AIME 2024, 2025, and 2026 scores as a measure of mathematical reasoning capability.\n\nThis is categorically different from the benchmarks on the user's allowed list (AgentBench, WebArena, SWE-bench Verified, GAIA, ToolBench, ALFWorld, Mind2Web, tau-bench), which all evaluate **agentic capabilities**: planning, tool use, environment interaction, multi-step task completion, web navigation, code editing, etc.\n\n### 2. Does PettingLLMs implement a multi-agent DISCUSSION format for AIME?\n\n**PettingLLMs is a real framework** (ICLR 2026 paper titled \"Stronger-MAS\"), available at `https://github.com/pettingllms-ai/PettingLLMs`. It implements AT-GRPO (Agent- and Turn-wise Group Relative Policy Optimization) for training collaborative multi-agent LLM systems. It does support AIME as one of its math environments (alongside OlympiadBench).\n\nHowever, the specifics of the \"discussion\" format are important to understand:\n- PettingLLMs enables multi-turn interactions where agents revise outputs using environment feedback. For code tasks, this is explicit (Coder + Unit-Tester exchanging artifacts). For math tasks like AIME, the multi-agent setup involves agents collaborating on reasoning, but **the core task remains solving a math problem with an integer answer** -- not navigating an environment, using tools, or completing agentic tasks.\n- The \"discussion\" is a **training methodology** (agents exchanging reasoning steps to arrive at a math answer), not an **agent benchmark** in the sense of the user's allowed list. It is closer to \"multi-agent debate for reasoning\" than to \"agent evaluation in an interactive environment.\"\n\n### 3. Is AIME24 a commonly used evaluation benchmark in multi-agent LLM literature?\n\nAIME24 is commonly used in LLM evaluation literature broadly, particularly for mathematical reasoning and RL-based post-training. It is used in some multi-agent work (e.g., M-GRPO papers), but primarily as a **downstream task to measure reasoning quality**, not as a benchmark for evaluating agent communication, tool use, or environmental interaction. It is not a \"multi-agent benchmark\" in the way that MultiAgentBench or the user's allowed benchmarks are.\n\n### 4. AT-GRPO multi-agent discussion format for AIME\n\nAT-GRPO (Agent- and Turn-wise Group Relative Policy Optimization) provides fine-grained credit assignment at both the agent and turn level. In a multi-agent AIME setup, multiple agents exchange reasoning about a math problem across turns. The \"one-round discussion\" baseline involves agents receiving the same prompt, generating responses, and then having their prompts augmented with each other's first-turn responses in a second turn. This is a **reasoning refinement protocol**, not an interactive agent task.\n\n### 5. The fundamental mismatch\n\nThere is a clear categorical mismatch between AIME and the user's allowed benchmarks:\n\n| Property | User's Allowed Benchmarks | AIME |\n|---|---|---|\n| Environment interaction | Yes (web, code repos, household, APIs) | No |\n| Tool use | Yes | No |\n| Multi-step task execution | Yes (dynamic, stateful) | No (single answer) |\n| What it measures | Agentic capability | Mathematical reasoning |\n| Answer format | Task completion in environment | Integer 0-999 |\n\n**The user's allowed list consists entirely of agent/tool-use benchmarks.** AIME is a math reasoning benchmark. Even when wrapped in a PettingLLMs multi-agent discussion format, the underlying evaluation is still \"did the agents produce the correct integer answer to a math competition problem\" -- not \"did the agents successfully navigate an environment, use tools, and complete a multi-step task.\"\n\n### Bottom Line\n\nThe proposal's use of \"PettingLLMs AIME multi-agent discussion\" as an evaluation benchmark does not satisfy the user's constraint. While PettingLLMs is a legitimate framework and AIME is a legitimate benchmark, AIME is fundamentally a math reasoning evaluation, not an agent/tool-use benchmark. It is not on the allowed list, and it is not a substitute for any benchmark on the allowed list. The benchmarks on the allowed list all evaluate interactive, environment-grounded, tool-using agent behavior -- a completely different evaluation paradigm from competition math problem solving."
      }
    ],
    "totalDurationMs": 93201,
    "totalTokens": 21964,
    "totalToolUseCount": 11,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2216,
      "cache_read_input_tokens": 18532,
      "output_tokens": 1215,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2216
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1215,
          "cache_read_input_tokens": 18532,
          "cache_creation_input_tokens": 2216,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2216,
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
  "sourceToolAssistantUUID": "3fde3df9-ba74-4cfc-a27d-6a4950a5686d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c886791-a9d9-487c-99a0-b2a7b1d3d99e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-10T22:17:38.938Z_

<details><summary>↩ Tool result · `toolu_01NscAgcNjNExYgosnuEjFMy`</summary>

```text
Now I have comprehensive information on all four questions. Here is my complete report.

---

## 1. MAPoRL (ACL 2025) -- arXiv 2502.18439

**Title:** "Multi-Agent Post-Co-Training for Collaborative Large Language Models with Reinforcement Learning"
**Authors:** Chanwoo Park, Seungju Han, Xingzhi Guo, Asuman E. Ozdaglar, Kaiqing Zhang, Joo-Kyung Kim
**Venue:** ACL 2025, Vienna, Austria (pages 30215-30248)

**Does it co-train generation and comprehension?**
No. The "co-training" in MAPoRL refers to training **multiple LLM agents together simultaneously**, not co-training generation and comprehension as separate skills. Multiple LLMs generate their own responses independently, then engage in multi-turn discussion to collaboratively improve a final answer. The focus is on collaborative debate behavior, not on separating generation from comprehension.

**Does it use contrastive objectives?**
No. MAPoRL uses **no contrastive objectives whatsoever**. Its training signal comes from a verifier that assigns a score evaluating both the final answer's correctness and the quality of the discussion (rewarding corrective and persuasive exchanges). This score is maximized via multi-agent RL using PPO with a KL regularization term against reference models and a value function loss. There are no contrastive or comparative losses between agents.

---

## 2. Social Deduction LLM (AAMAS 2025) -- arXiv 2502.06060

**Title:** "Training Language Models for Social Deduction with Multi-Agent Reinforcement Learning"
**Authors:** Bidipta Sarkar, Warren Xia, C. Karen Liu, Dorsa Sadigh
**Venue:** AAMAS 2025, Detroit, Michigan

**Does it train receiver-side listening loss?**
Yes. The paper explicitly decomposes communication into **listening** and **speaking** skills and trains both. The listening loss is a standard supervised **cross-entropy/negative log-likelihood loss**: `L_L(pi, tau) = -log pi(q | tau)`, where the agent predicts the identity of the imposter `q` given its action-observation history including discussion messages. This serves as a dense reward signal to guide communication learning.

**Is it task-specific (Among Us)?**
Yes. The paper studies an embodied social deduction game **based on Among Us**, where agents must identify an adversarial imposter through natural language discussion. It is task-specific to this Among Us-inspired setting.

**Is it non-contrastive?**
Yes, it is entirely **non-contrastive**. The listening component uses supervised prediction (cross-entropy), and the speaking component uses reinforcement learning with a reward based on belief change (`r_s = B_t - B_t'`, measuring how much a message increases crewmates' confidence in voting out the true imposter). Both are trained jointly in a single combined loss. No contrastive objectives appear anywhere in the paper.

---

## 3. Bilateral/Bidirectional Contrastive Training of Both Sender and Receiver in LLM Agents (2025-2026)

After extensive searching, **I did not find any paper from 2025-2026 that performs bilateral or bidirectional contrastive training of both sender and receiver communication specifically in LLM agents.** Here is what the closest related work looks like:

- **CACL (Communication Alignment Contrastive Learning)** from "Learning Multi-Agent Communication with Contrastive Learning" (Lo et al., ICLR 2024, arXiv 2307.01403): This uses contrastive learning for multi-agent communication, treating different agents' messages about the same state as positive pairs. However, it operates on **traditional MARL agents** (not LLMs), uses continuous message vectors (not natural language), and applies a **unilateral** contrastive objective -- each agent independently applies contrastive learning to its own messages, not a bilateral sender-receiver contrastive objective.

- **TACTIC** (arXiv 2501.02174, 2025): Task-Agnostic Contrastive pre-Training for Inter-Agent Communication. Uses offline contrastive pretraining for communication modules, but again operates on traditional MARL, not LLM agents.

- **SA-LLM** (arXiv 2503.08842, March 2025): "Contrastive Speaker-Aware Learning for Multi-party Dialogue Generation with LLMs" -- uses contrastive learning to learn speaker roles in multi-party dialogue, but this is about dialogue generation quality, not multi-agent communication protocol training between sender and receiver.

- The Social Deduction paper (2502.06060) trains both speaker and listener but is **non-contrastive**.

**Bottom line:** No paper was found that does bilateral contrastive training of both sender and receiver communication in LLM-based multi-agent systems from 2025-2026. This appears to be a gap in the literature.

---

## 4. MAGE (Pattern Recognition 2025) -- Graph Contrastive Learning for Multi-Agent Communication

**Title:** "Learning multi-agent communication via graph contrastive learning"
**Journal:** Pattern Recognition (Elsevier/ScienceDirect), published July 2025
**ScienceDirect:** [S0031320325007538](https://www.sciencedirect.com/science/article/abs/pii/S0031320325007538)

**What MAGE does:** MAGE is a multi-agent communication protocol that uses graph contrastive learning to learn high-quality message representations. It generates two correlated graph views by applying stochastic corruption to a communication graph, then trains with a contrastive loss to enhance consistency of agent feature representations across these views. It operates at two levels:
- **Topological level:** Dynamically removes edges (higher removal probability for less significant edges)
- **Feature level:** Introduces noise to less critical dimensions of agent features

**Is it relevant as a missing citation?** This depends on what paper you are comparing it to, but here are the key limitations of its relevance:

1. **MAGE operates on traditional MARL agents, NOT LLM agents.** It works with continuous observation/action spaces and learned message vectors in cooperative control environments (e.g., StarCraft-style tasks), not with natural language communication between language models.

2. **MAGE's contrastive objective is about learning better message representations through graph augmentation**, not about bilateral sender-receiver contrastive training. It contrasts different augmented views of the same communication graph, not sender vs. receiver perspectives.

3. **It does not train both sender and receiver with contrastive objectives bilaterally.** The contrastive loss operates on graph-level representations.

If your paper concerns contrastive training of LLM agents' communication (both generation and comprehension of natural language messages), MAGE operates in a fundamentally different domain (traditional MARL with continuous messages, graph-based representation learning). It would be relevant primarily as a "contrastive learning has been used in multi-agent communication" background citation, but not as a directly comparable or competing approach for LLM-based bilateral contrastive communication training.

---

Sources:
- [MAPoRL -- ACL Anthology](https://aclanthology.org/2025.acl-long.1459/)
- [MAPoRL -- arXiv 2502.18439](https://arxiv.org/abs/2502.18439)
- [Social Deduction LLM -- arXiv 2502.06060](https://arxiv.org/abs/2502.06060)
- [MAGE -- ScienceDirect (Pattern Recognition 2025)](https://www.sciencedirect.com/science/article/abs/pii/S0031320325007538)
- [CACL -- arXiv 2307.01403 (ICLR 2024)](https://arxiv.org/abs/2307.01403)
- [TACTIC -- arXiv 2501.02174](https://arxiv.org/html/2501.02174)
- [SA-LLM -- arXiv 2503.08842](https://arxiv.org/abs/2503.08842)
- [Adapting LLM Agents Through Communication -- ICLR 2024](https://openreview.net/forum?id=wOelVq8fwL)

agentId: ad679632efe395930 (use SendMessage with to: 'ad679632efe395930' to continue this agent)
&lt;usage>total_tokens: 31495
tool_uses: 25
duration_ms: 177094&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "67d6ec1a-4cc1-4b66-ae51-0e3804f02d4e",
  "isSidechain": false,
  "promptId": "c4053383-51a2-4c53-bef4-50bbbd8ab467",
  "type": "user",
  "uuid": "78b57ea2-4764-4abb-afdf-a896bc8b5fab",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Search the web to verify these papers and understand what they do:\n\n1. MAPoRL (ACL 2025) - \"Multi-Agent Post-Co-Training for Collaborative LLMs\" \n   - Search for this paper on arxiv and Google Scholar\n   - Does it co-train generation and comprehension?\n   - Does it use contrastive objectives?\n\n2. Social Deduction LLM (AAMAS 2025, arXiv 2502.06060) - \"Training Language Models for Social Deduction with Multi-Agent RL\"\n   - Does it train receiver-side listening loss?\n   - Is it task-specific (Among Us)?\n   - Is it non-contrastive?\n\n3. Also search for any paper that does \"bilateral\" or \"bidirectional\" contrastive training of both sender and receiver communication in LLM agents, specifically from 2025-2026.\n\n4. Search for \"MAGE contrastive multi-agent communication 2025\" - there was a mention of MAGE (Pattern Recognition 2025) doing graph contrastive learning for multi-agent communication. Is this relevant as a missing citation?\n\nReport exactly what you find.",
    "agentId": "ad679632efe395930",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have comprehensive information on all four questions. Here is my complete report.\n\n---\n\n## 1. MAPoRL (ACL 2025) -- arXiv 2502.18439\n\n**Title:** \"Multi-Agent Post-Co-Training for Collaborative Large Language Models with Reinforcement Learning\"\n**Authors:** Chanwoo Park, Seungju Han, Xingzhi Guo, Asuman E. Ozdaglar, Kaiqing Zhang, Joo-Kyung Kim\n**Venue:** ACL 2025, Vienna, Austria (pages 30215-30248)\n\n**Does it co-train generation and comprehension?**\nNo. The \"co-training\" in MAPoRL refers to training **multiple LLM agents together simultaneously**, not co-training generation and comprehension as separate skills. Multiple LLMs generate their own responses independently, then engage in multi-turn discussion to collaboratively improve a final answer. The focus is on collaborative debate behavior, not on separating generation from comprehension.\n\n**Does it use contrastive objectives?**\nNo. MAPoRL uses **no contrastive objectives whatsoever**. Its training signal comes from a verifier that assigns a score evaluating both the final answer's correctness and the quality of the discussion (rewarding corrective and persuasive exchanges). This score is maximized via multi-agent RL using PPO with a KL regularization term against reference models and a value function loss. There are no contrastive or comparative losses between agents.\n\n---\n\n## 2. Social Deduction LLM (AAMAS 2025) -- arXiv 2502.06060\n\n**Title:** \"Training Language Models for Social Deduction with Multi-Agent Reinforcement Learning\"\n**Authors:** Bidipta Sarkar, Warren Xia, C. Karen Liu, Dorsa Sadigh\n**Venue:** AAMAS 2025, Detroit, Michigan\n\n**Does it train receiver-side listening loss?**\nYes. The paper explicitly decomposes communication into **listening** and **speaking** skills and trains both. The listening loss is a standard supervised **cross-entropy/negative log-likelihood loss**: `L_L(pi, tau) = -log pi(q | tau)`, where the agent predicts the identity of the imposter `q` given its action-observation history including discussion messages. This serves as a dense reward signal to guide communication learning.\n\n**Is it task-specific (Among Us)?**\nYes. The paper studies an embodied social deduction game **based on Among Us**, where agents must identify an adversarial imposter through natural language discussion. It is task-specific to this Among Us-inspired setting.\n\n**Is it non-contrastive?**\nYes, it is entirely **non-contrastive**. The listening component uses supervised prediction (cross-entropy), and the speaking component uses reinforcement learning with a reward based on belief change (`r_s = B_t - B_t'`, measuring how much a message increases crewmates' confidence in voting out the true imposter). Both are trained jointly in a single combined loss. No contrastive objectives appear anywhere in the paper.\n\n---\n\n## 3. Bilateral/Bidirectional Contrastive Training of Both Sender and Receiver in LLM Agents (2025-2026)\n\nAfter extensive searching, **I did not find any paper from 2025-2026 that performs bilateral or bidirectional contrastive training of both sender and receiver communication specifically in LLM agents.** Here is what the closest related work looks like:\n\n- **CACL (Communication Alignment Contrastive Learning)** from \"Learning Multi-Agent Communication with Contrastive Learning\" (Lo et al., ICLR 2024, arXiv 2307.01403): This uses contrastive learning for multi-agent communication, treating different agents' messages about the same state as positive pairs. However, it operates on **traditional MARL agents** (not LLMs), uses continuous message vectors (not natural language), and applies a **unilateral** contrastive objective -- each agent independently applies contrastive learning to its own messages, not a bilateral sender-receiver contrastive objective.\n\n- **TACTIC** (arXiv 2501.02174, 2025): Task-Agnostic Contrastive pre-Training for Inter-Agent Communication. Uses offline contrastive pretraining for communication modules, but again operates on traditional MARL, not LLM agents.\n\n- **SA-LLM** (arXiv 2503.08842, March 2025): \"Contrastive Speaker-Aware Learning for Multi-party Dialogue Generation with LLMs\" -- uses contrastive learning to learn speaker roles in multi-party dialogue, but this is about dialogue generation quality, not multi-agent communication protocol training between sender and receiver.\n\n- The Social Deduction paper (2502.06060) trains both speaker and listener but is **non-contrastive**.\n\n**Bottom line:** No paper was found that does bilateral contrastive training of both sender and receiver communication in LLM-based multi-agent systems from 2025-2026. This appears to be a gap in the literature.\n\n---\n\n## 4. MAGE (Pattern Recognition 2025) -- Graph Contrastive Learning for Multi-Agent Communication\n\n**Title:** \"Learning multi-agent communication via graph contrastive learning\"\n**Journal:** Pattern Recognition (Elsevier/ScienceDirect), published July 2025\n**ScienceDirect:** [S0031320325007538](https://www.sciencedirect.com/science/article/abs/pii/S0031320325007538)\n\n**What MAGE does:** MAGE is a multi-agent communication protocol that uses graph contrastive learning to learn high-quality message representations. It generates two correlated graph views by applying stochastic corruption to a communication graph, then trains with a contrastive loss to enhance consistency of agent feature representations across these views. It operates at two levels:\n- **Topological level:** Dynamically removes edges (higher removal probability for less significant edges)\n- **Feature level:** Introduces noise to less critical dimensions of agent features\n\n**Is it relevant as a missing citation?** This depends on what paper you are comparing it to, but here are the key limitations of its relevance:\n\n1. **MAGE operates on traditional MARL agents, NOT LLM agents.** It works with continuous observation/action spaces and learned message vectors in cooperative control environments (e.g., StarCraft-style tasks), not with natural language communication between language models.\n\n2. **MAGE's contrastive objective is about learning better message representations through graph augmentation**, not about bilateral sender-receiver contrastive training. It contrasts different augmented views of the same communication graph, not sender vs. receiver perspectives.\n\n3. **It does not train both sender and receiver with contrastive objectives bilaterally.** The contrastive loss operates on graph-level representations.\n\nIf your paper concerns contrastive training of LLM agents' communication (both generation and comprehension of natural language messages), MAGE operates in a fundamentally different domain (traditional MARL with continuous messages, graph-based representation learning). It would be relevant primarily as a \"contrastive learning has been used in multi-agent communication\" background citation, but not as a directly comparable or competing approach for LLM-based bilateral contrastive communication training.\n\n---\n\nSources:\n- [MAPoRL -- ACL Anthology](https://aclanthology.org/2025.acl-long.1459/)\n- [MAPoRL -- arXiv 2502.18439](https://arxiv.org/abs/2502.18439)\n- [Social Deduction LLM -- arXiv 2502.06060](https://arxiv.org/abs/2502.06060)\n- [MAGE -- ScienceDirect (Pattern Recognition 2025)](https://www.sciencedirect.com/science/article/abs/pii/S0031320325007538)\n- [CACL -- arXiv 2307.01403 (ICLR 2024)](https://arxiv.org/abs/2307.01403)\n- [TACTIC -- arXiv 2501.02174](https://arxiv.org/html/2501.02174)\n- [SA-LLM -- arXiv 2503.08842](https://arxiv.org/abs/2503.08842)\n- [Adapting LLM Agents Through Communication -- ICLR 2024](https://openreview.net/forum?id=wOelVq8fwL)"
      }
    ],
    "totalDurationMs": 177094,
    "totalTokens": 31495,
    "totalToolUseCount": 25,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 593,
      "cache_read_input_tokens": 28911,
      "output_tokens": 1990,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 593
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1990,
          "cache_read_input_tokens": 28911,
          "cache_creation_input_tokens": 593,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 593,
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
  "sourceToolAssistantUUID": "67d6ec1a-4cc1-4b66-ae51-0e3804f02d4e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c886791-a9d9-487c-99a0-b2a7b1d3d99e",
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
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-10 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "78b57ea2-4764-4abb-afdf-a896bc8b5fab",
  "sessionId": "0c886791-a9d9-487c-99a0-b2a7b1d3d99e"
}
```

---

### Runtime record

_source line 28_

```json
{
  "type": "ai-title",
  "aiTitle": "Bilateral intent grounding for multi-agent LLM communication",
  "sessionId": "0c886791-a9d9-487c-99a0-b2a7b1d3d99e"
}
```

---

### Assistant

_source line 29 · 2026-05-10T22:19:43.771Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have comprehensive verification data. Let me synthesize my findings and assess the proposal systematically.

## Key Findings from My Research

### 1. CLIPO and AMIR-GRPO (Verified)
- CLIPO (March 2026, arXiv 2603.10101) - CONFIRMED. Uses InfoNCE within GRPO rollout groups. Public code at github.com/Qwen-Applications/CLIPO. Results: +0.65–5.42 points on math benchmarks.


- AMIR-GRPO (January 2026, arXiv 2601.03661) - CONFIRMED. Mines DPO-style pairwise preferences from GRPO groups.
- Both are now properly cited in the proposal (this was the critical issue from Round 7).

### 2. PettingLLMs and AIME Claims
- PettingLLMs does support AIME natively.
- The 16.7% result for Qwen3-1.7B on AIME24 is from AT-GRPO training with a shared policy, not a baseline—the single-agent baseline sits at 13.40%.
- The proposal's framing is actually sound: it's showing that even with AT-GRPO training, 1.7B models plateau at 16.7%, which justifies exploring communication improvements.

### 3. BENCHMARK COMPLIANCE
This is a critical constraint violation. The hard requirements specify only these benchmarks: AgentBench, WebArena, SWE-bench Verified, GAIA, ToolBench, ALFWorld, Mind2Web, τ-bench. AIME24 isn't on this list, yet the proposal uses it as the primary evaluation metric—this needs immediate correction.

The fundamental issue is that AIME is a math reasoning benchmark, while all the allowed benchmarks are designed for agent-environment interaction. The multi-agent discussion format for solving AIME problems doesn't align with what these benchmarks measure, and there's a categorical mismatch between the proposed evaluation approach and the user's specified constraints.

Actually, ALFWorld was already discussed in previous rounds as a planner-executor setup and is on the allowed list—abandoning that for AIME represents a step backward in compliance.

Looking at the novelty more carefully, the proposal extends intra-group contrastive learning from reasoning to communication by introducing bilateral training where both sender and receiver losses use GRPO-group negatives. This differs from CLIPO's single-agent outcome consistency approach and AMIR-GRPO's framework. The bilateral formulation—training both communicating agents simultaneously with shared negative samples—appears to be the core novel contribution, and my searches haven't found existing work doing this in multi-agent LLM systems.

TACTIC comes closest by training both agents contrastively, but it pre-trains offline then freezes during RL, uses random negatives, and operates at smaller scale. The novelty here is real but incremental—it's applying a known contrastive mechanism to multi-agent communication with domain-specific adaptations like the bilateral setup, stop-gradient, and EMA. The landscape is now comprehensive with citations covering latent methods, communication approaches, and GRPO variants.

I found several uncited papers during my search: MAGE does graph contrastive learning for MARL but isn't LLM-focused, M-GRPO extends GRPO to hierarchical systems, MARFT provides a multi-agent RL fine-tuning framework, MARTI is another multi-agent training framework, and LMNet enables dense vector communication. Most have limited relevance to the core contribution, though M-GRPO and MARFT might warrant brief mentions as related MARL frameworks.

Now looking at the technical soundness—the method combines InfoNCE losses for both sender and receiver with GRPO-group alternatives as negatives, uses stop-gradient and EMA for stability, and pools messages via attention weighting. The combined loss balances GRPO with weighted sender and receiver components. One issue I'm noticing: the intent state comes from the sender's hidden representation before message generation, stabilized through stop-gradient and EMA, but there's no explicit validation that this embedding actually captures meaningful intent.

For compute, the budget sits around 55 hours on H100s, well under the 200-hour limit—baseline takes roughly 10 hours, per-agent CLIPO about 12, and the bilateral variants another 10-20 combined with ablations filling out the rest. This scales reasonably for 1.7B models with LoRA.

The timeline is compressed into 15 days with implementation in the first few days, experiments taking up the bulk of the middle period, and the final stretch dedicated to analysis and writing. It's aggressive but workable since the infrastructure already supports the necessary components.

Now I'm noticing a critical mismatch: AIME isn't on the allowed benchmark list at all. The user was explicit about which evaluations are permitted, and AIME doesn't appear there. I'm realizing the constraint is pretty explicit—that dash and list strongly suggests AIME isn't an allowed evaluation benchmark, even though the multi-agent discussion format itself is from published work. The question is whether "existing benchmarks only" means "don't create new ones" or "only use these eight specific benchmarks," and the formatting really points to the latter interpretation.

There's a real tension here: the user wants multi-agent coordination, but most of the allowed benchmarks are single-agent focused. The proposal chose AIME because multi-agent communication naturally fits there, but that's a genuine violation of the stated constraints.

On the 16.7% framing, I need to check what the actual comparison point is—the proposal mentions AT-GRPO with Qwen3-1.7B at 16.7% on AIME24, and there's a reference to 50% somewhere, but the thought cuts off before I can see the full context.

Looking at the claim that "inter-agent communication quality is the dominant bottleneck"—that's a big assertion without real evidence. The performance gap between 1.7B and 8B models could stem from capacity, reasoning ability, or knowledge, not necessarily communication quality. The proposal is making an assumption that isn't backed up.

And then there's the evaluation scope: just AIME24 for EMNLP is pretty thin. They mention OlympiadBench for an extended AAAI version, but a single benchmark doesn't give much confidence in the approach.

Now stepping back at what's actually improved—the citations are fixed, the contribution is clearer as extending contrastive learning to communication, the compute is reasonable, and the bilateral formulation is genuinely novel. But there's a critical problem: AIME isn't on the allowed benchmark list. And the core empirical bet—that communication is actually the bottleneck rather than just model capacity—still lacks evidence.

The benchmark issue is solvable by switching to ALFWorld with a planner-executor setup, though that's a significant revision. The communication bottleneck assumption is more of an execution risk than a fatal flaw. Adding a second benchmark would address the evaluation thinness. The novelty is incremental—applying CLIPO's mechanism to multi-agent communication—but that's reasonable for a Findings paper.

Scoring this: novelty lands at 3/5 because the bilateral contrastive formulation with sender and receiver losses using GRPO-group negatives is genuinely novel, but each component is borrowed and the contribution is really domain transfer of an existing approach. Feasibility is also 3/5—the compute budget works and the timeline is tight but doable with existing code, though AIME isn't on the allowed benchmark list and the communication bottleneck assumption at 1.7B scale remains unvalidated.

The proposal is well-structured and clearly articulated with a solid experimental design, earning 4/5 for clarity, but impact is limited to 3/5 since it's only evaluated on math rather than agent benchmarks and the bilateral advantage over sender-only is still uncertain. Overall this averages to 3.25, which falls below the target threshold.

The persistent issue across all eight rounds is benchmark compliance—the proposal keeps shifting to different benchmarks outside the allowed list, and this round's switch to AIME represents a regression from the previous ALFWorld approach. The core idea is technically sound and the landscape is now comprehensive, but the novelty and impact remain moderate at 3/5 each, and the benchmark violation has been consistent across every iteration. Given this is round 8 of 10, I need to push back with specific feedback on the benchmark constraint and demand stronger novelty and impact arguments for the final rounds rather than approve another revision.

Wait, I'm reconsidering the benchmark issue more carefully. The user explicitly listed "multi-agent coordination" and "agent training (SFT/RL)" as valid research directions, and the BIG method directly addresses multi-agent coordination training via RL—so the direction itself is valid. The constraint specifies using existing benchmarks from the approved list, and AIME isn't on it, but there's a real tension here: none of those benchmarks have established multi-agent setups with inter-agent communication, and ALFWorld, while the closest option, doesn't naturally support the kind of bilateral communication the method requires.

The proposal could defend itself by pointing to PettingLLMs' AIME multi-agent discussion setup from the ICLR 2026 paper as an existing benchmark, but that still doesn't resolve the fact that AIME itself isn't on the specified list. This feels like a genuine constraint violation that should be flagged—the proposal needs to either incorporate at least one benchmark from the allowed list (like ALFWorld configured as planner-executor) or make a compelling case for why AIME is necessary despite being off-list.

Now I need to assess whether this clears the bar for EMNLP 2026 Main in terms of venue quality.

The core issue is that the contribution feels incremental—extending CLIPO to handle communication—with evaluation limited to a single benchmark in a narrow model size regime, and the bilateral advantage itself remains uncertain. For a Main conference paper, I'd expect stronger empirical validation across multiple benchmarks and clearer evidence that the bilateral approach genuinely outperforms sender-only alternatives. This reads more like Findings material, which actually fits within what the user is willing to accept.

For Findings, the bar is lower: a novel method with focused evaluation and solid ablations would be sufficient, and the scope here seems reasonable for that tier.

I should also verify whether the 16.7% figure needs clarification—the proposal attributes this to AT-GRPO with Qwen3-1.7B on AIME24, but I need to check if that's actually the shared-policy result or if there's a framing issue there.

Looking at the per-agent breakdown from Stronger-MAS, the shared AT-GRPO policy achieves 16.7% compared to 13.4% for a single agent, which is a +3.3 point gain. The per-role variant drops back to 13.3%, suggesting the shared policy is what's driving that improvement. The proposal's framing seems accurate—they're using 16.7% as their starting point and arguing that communication quality is the limiting factor. But that claim about communication being the dominant bottleneck at 1.7B scale is still speculative; the model might simply lack the raw reasoning capacity to go much higher.

What's more concerning is that if multi-agent collaboration only yields +3.3 points at 1.7B, then improving communication through BIG training might only add another 1-2 points at best. The 8B results show dramatically larger gains from multi-agent discussion—31.7 to 38.7 points—which suggests the model needs sufficient capacity to actually generate and understand useful messages. At 1.7B, the bottleneck might not be communication quality at all, but rather the model's fundamental inability to benefit from collaboration regardless of how well-trained the communication is. The proposal doesn't really grapple with this possibility.

Now I'm scoring this across the key dimensions: novelty is moderate since it's applying bilateral contrastive learning to LLM communication but borrowing heavily from existing techniques, feasibility is constrained by the tight timeline and the fact that AIME isn't on the allowed benchmark list, clarity is strong with good experimental design, but impact is limited given the small model regime and uncertain gains from bilateral training over simpler approaches. That puts me at 3.25 overall, below the 4.0 threshold. This needs revision—the core ideas are sound but the execution and scope need tightening.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "78b57ea2-4764-4abb-afdf-a896bc8b5fab",
  "isSidechain": false,
  "requestId": "req_011CaufQWWJknXZLEB5zsNKz",
  "type": "assistant",
  "uuid": "2bb6bf66-eb6f-4dcd-a1eb-464707b99d4d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c886791-a9d9-487c-99a0-b2a7b1d3d99e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015jxVqMF3JHytKFJAXzPfc6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4180,
      "cache_read_input_tokens": 48531,
      "output_tokens": 5669,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4180,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5669,
          "cache_read_input_tokens": 48531,
          "cache_creation_input_tokens": 4180,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4180
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Assistant

_source line 30 · 2026-05-10T22:19:43.773Z_

Now let me do one more targeted verification on the key empirical claim about 1.7B communication bottleneck.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2bb6bf66-eb6f-4dcd-a1eb-464707b99d4d",
  "isSidechain": false,
  "requestId": "req_011CaufQWWJknXZLEB5zsNKz",
  "type": "assistant",
  "uuid": "3061efbf-249c-431e-90d8-1df064c857b4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c886791-a9d9-487c-99a0-b2a7b1d3d99e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015jxVqMF3JHytKFJAXzPfc6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4180,
      "cache_read_input_tokens": 48531,
      "output_tokens": 5669,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4180,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5669,
          "cache_read_input_tokens": 48531,
          "cache_creation_input_tokens": 4180,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4180
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-10T22:19:49.757Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01Ef2feQCavTBKn76cf33GE3`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Verify 1.7B communication bottleneck claim",
  "prompt": "Search the web to verify this specific claim from a research proposal:\n\n\"AT-GRPO with Qwen3-1.7B achieves only 16.7% on AIME24 (vs. 50–57% with 8B), making inter-agent communication quality the dominant bottleneck.\"\n\nSpecifically, I need to understand:\n1. What are the exact AT-GRPO results from the Stronger-MAS paper (arXiv 2510.11062) for different model sizes on AIME24? What is the single-agent baseline at 1.7B?\n2. At 1.7B scale, how much does multi-agent discussion help over single-agent? (i.e., is the multi-agent gain only a few points?)\n3. Is there evidence that communication quality (vs. model capacity/reasoning ability) is actually the bottleneck at 1.7B scale?\n4. Search for \"small language model multi-agent discussion diminishing returns\" or similar to see if there's evidence that small models don't benefit much from multi-agent collaboration.\n5. What does the Qwen3-1.7B model achieve on AIME24 in single-agent mode?\n\nThe concern: if the 1.7B model only gains ~3 points from multi-agent setup (13.4% → 16.7%), improving communication quality may yield minimal additional gains because the model lacks fundamental reasoning capacity, not communication quality.\n\nReport your findings."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3061efbf-249c-431e-90d8-1df064c857b4",
  "isSidechain": false,
  "requestId": "req_011CaufQWWJknXZLEB5zsNKz",
  "type": "assistant",
  "uuid": "3373a925-a200-4f2f-a861-19bc52eacf4f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c886791-a9d9-487c-99a0-b2a7b1d3d99e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015jxVqMF3JHytKFJAXzPfc6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4180,
      "cache_read_input_tokens": 48531,
      "output_tokens": 5669,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4180,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5669,
          "cache_read_input_tokens": 48531,
          "cache_creation_input_tokens": 4180,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4180
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Runtime record

_source line 32_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-10 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "3373a925-a200-4f2f-a861-19bc52eacf4f",
  "sessionId": "0c886791-a9d9-487c-99a0-b2a7b1d3d99e"
}
```

---

### Runtime record

_source line 33_

```json
{
  "type": "ai-title",
  "aiTitle": "Bilateral intent grounding for multi-agent LLM communication",
  "sessionId": "0c886791-a9d9-487c-99a0-b2a7b1d3d99e"
}
```

---

### Tool result

_source line 34 · 2026-05-10T22:23:28.621Z_

<details><summary>↩ Tool result · `toolu_01Ef2feQCavTBKn76cf33GE3`</summary>

```text
I have gathered extensive information. Here is my comprehensive report.

---

## Findings Report: AT-GRPO Claims Analysis for AIME24

### 1. Exact AT-GRPO Results from the Stronger-MAS Paper (arXiv 2510.11062)

The numbers from the paper (Tables 1 and 2) are confirmed:

**Qwen3-1.7B on AIME24:**
| Configuration | Accuracy |
|---|---|
| Single Agent (baseline) | 13.40% |
| Single Agent + GRPO | 10.00% |
| MAS (prompt-only, no training) | 13.30% |
| MAS + GRPO | 13.30% |
| MAS + AT-GRPO (shared policy) | **16.70%** |
| MAS + AT-GRPO (per-role policies) | 13.30% |

**Qwen3-8B on AIME24:**
| Configuration | Accuracy |
|---|---|
| Single Agent (baseline) | 18.30% |
| Single Agent + GRPO | 18.30% |
| MAS (prompt-only, no training) | 36.60% |
| MAS + GRPO | 33.30% |
| MAS + AT-GRPO (shared policy) | **50.00%** |
| MAS + AT-GRPO (per-role policies) | **57.00%** |

The single-agent baseline for Qwen3-1.7B on AIME24 is **13.40%**.

### 2. Multi-Agent Gain at 1.7B Scale

The concern raised in the research proposal is well-founded. At 1.7B:

- **Single agent baseline**: 13.40%
- **Best multi-agent (AT-GRPO shared)**: 16.70%
- **Net gain**: +3.30 percentage points

Notably, even the untrained MAS (prompt-only) at 1.7B shows **no gain** over single agent (13.30% vs 13.40% -- essentially equivalent or slightly worse). Standard GRPO training actually *hurts* performance (dropping single-agent to 10.00%).

Compare this to 8B, where:
- **Single agent baseline**: 18.30%
- **Best multi-agent (AT-GRPO per-role)**: 57.00%
- **Net gain**: +38.70 percentage points
- Even untrained MAS doubles performance: 36.60% vs 18.30%

The contrast is stark. At 8B, simply putting models into a multi-agent discussion without any training already doubles performance (18.3% to 36.6%). At 1.7B, the same untrained multi-agent setup provides zero benefit (13.4% to 13.3%).

### 3. Is Communication Quality Actually the Bottleneck at 1.7B?

**The evidence is mixed and the claim in the proposal is likely too simplistic.** Here is what the evidence suggests:

**Evidence AGAINST "communication quality is the dominant bottleneck":**

- The SLM-MUX paper (arXiv 2510.05077) directly demonstrates that **discussion-based orchestration methods designed for large models actively harm small models**, causing accuracy drops of up to 5.5%. The root cause: "SLMs tend to exhibit groupthink, reinforcing incorrect reasoning during discussions rather than correcting mistakes." 59.5% of failures were attributed to groupthink. The paper explicitly states the bottleneck is that "SLMs lack sufficient reasoning capacity for this interaction model, making the communication channel irrelevant."

- The comprehensive LLM reasoning evaluation paper (arXiv 2601.13243) found that "additional multi-agent interactions provide limited and inconsistent benefits" and that "failed cases are heavily concentrated in the high-cost regime," indicating model capacity (ability to solve problems) rather than communication quality is the limiting factor.

**Evidence FOR "communication quality matters":**

- The "Can Small Agents Collaborate" paper (arXiv 2601.11327) found that communication/orchestration IS the bottleneck when using tool-augmented multi-agent setups with a strong orchestrator. With an 8B orchestrator, sub-agent size barely matters (1.7B sub-agents: 23.0% vs 32B sub-agents: 23.6% on GAIA). However, this involves a heterogeneous architecture with a capable orchestrator, not homogeneous small agents discussing with each other.

- The paper "Large Language Models Miss the Multi-Agent Mark" (arXiv 2505.21298) argues natural language communication itself is "inefficient and ambiguous" and advocates structured communication protocols, suggesting communication infrastructure matters.

### 4. Small Language Models and Multi-Agent Diminishing Returns

Multiple papers converge on a critical finding: **discussion-based multi-agent methods that work for frontier models fail or backfire for small models.**

Key evidence:
- **SLM-MUX**: Discussion methods (Mixture-of-Agents, LLM-Debate, Multi-Agent Verification) caused accuracy drops of 2-5.5% for SLMs while improving frontier LLMs by up to 2%. The solution that works: **no inter-model communication at all** -- instead, confidence-based selection where each model generates independently and the most consistent answer wins.
- **Groupthink**: Small models reinforce each other's errors rather than correcting them. They lack the capacity to critically evaluate another agent's reasoning and identify flaws.
- **One counterpoint**: The "Diversity of Thought" paper (arXiv 2410.12853) found multi-agent debate can help at any scale when using *diverse* models (different architectures), not copies of the same model. This suggests the homogeneous setup in Stronger-MAS (all Qwen3-1.7B agents) is particularly prone to failure.

### 5. Qwen3-1.7B Standalone AIME24 Performance

I was unable to find an official Qwen3-1.7B AIME24 score from the Qwen technical report (the relevant Table 19 is not accessible in the HTML/search-extractable versions). However, the Stronger-MAS paper uses Qwen3-1.7B and reports its single-agent baseline as **13.40%** on AIME24. For reference, Qwen3-32B achieves ~23.3% in non-thinking mode and ~70% in thinking mode on AIME24. The 13.40% figure for 1.7B is consistent with what one would expect for a model of that size.

### Critical Assessment of the Proposal's Claim

The claim that "inter-agent communication quality is the dominant bottleneck" at 1.7B scale is **likely incorrect or at best misleading**. The evidence strongly suggests:

1. **The fundamental bottleneck is reasoning capacity, not communication quality.** At 1.7B, the model cannot reliably solve AIME problems individually (13.4%). Even with perfect communication, multiple copies of a model that cannot solve a problem individually will not solve it collectively -- they will simply reinforce each other's errors (groupthink).

2. **The 3.3-point gain (13.4% to 16.7%) from AT-GRPO at 1.7B likely represents the ceiling of what multi-agent collaboration can extract from this model size on this task.** Improving communication quality further is unlikely to yield meaningful additional gains because the individual agents lack the underlying mathematical reasoning ability.

3. **The 8B results are not simply "better communication" -- they reflect an emergent capability threshold.** At 8B, even untrained MAS doubles performance (18.3% to 36.6%), suggesting the 8B model has latent reasoning ability that can be surfaced through discussion. The 1.7B model does not exhibit this property at all (13.4% to 13.3% with untrained MAS).

4. **The most effective approach for small models avoids inter-model communication entirely** (SLM-MUX), suggesting that communication itself is counterproductive, not merely low-quality, at small model scales.

**Bottom line**: If you are proposing to improve inter-agent communication quality as a way to boost 1.7B performance on AIME24, the literature suggests this is unlikely to work. The model lacks the individual reasoning capacity needed to benefit from discussion. The correct framing is not "communication quality is the bottleneck" but rather "the model is below the capability threshold where multi-agent collaboration provides meaningful benefits on hard math tasks."

Sources:
- [Stronger-MAS: Multi-Agent Reinforcement Learning for Collaborative LLMs (arXiv 2510.11062)](https://arxiv.org/abs/2510.11062)
- [SLM-MUX: Orchestrating Small Language Models for Reasoning (arXiv 2510.05077)](https://arxiv.org/html/2510.05077)
- [Can Small Agents Collaborate to Beat a Single Large Language Model? (arXiv 2601.11327)](https://arxiv.org/html/2601.11327)
- [A Comprehensive Evaluation of LLM Reasoning: From Single-Model to Multi-Agent Paradigms (arXiv 2601.13243)](https://arxiv.org/html/2601.13243)
- [Large Language Models Miss the Multi-Agent Mark (arXiv 2505.21298)](https://arxiv.org/html/2505.21298)
- [Diversity of Thought Elicits Stronger Reasoning in Multi-Agent Debate (arXiv 2410.12853)](https://arxiv.org/abs/2410.12853)
- [PettingLLMs GitHub Repository](https://github.com/pettingllms-ai/PettingLLMs)
- [Qwen3 Technical Report (arXiv 2505.09388)](https://arxiv.org/abs/2505.09388)

agentId: aa219ab732b86947d (use SendMessage with to: 'aa219ab732b86947d' to continue this agent)
&lt;usage>total_tokens: 31810
tool_uses: 26
duration_ms: 218858&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3373a925-a200-4f2f-a861-19bc52eacf4f",
  "isSidechain": false,
  "promptId": "c4053383-51a2-4c53-bef4-50bbbd8ab467",
  "type": "user",
  "uuid": "7ca23970-887d-4112-a19c-ba042e33f526",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Search the web to verify this specific claim from a research proposal:\n\n\"AT-GRPO with Qwen3-1.7B achieves only 16.7% on AIME24 (vs. 50–57% with 8B), making inter-agent communication quality the dominant bottleneck.\"\n\nSpecifically, I need to understand:\n1. What are the exact AT-GRPO results from the Stronger-MAS paper (arXiv 2510.11062) for different model sizes on AIME24? What is the single-agent baseline at 1.7B?\n2. At 1.7B scale, how much does multi-agent discussion help over single-agent? (i.e., is the multi-agent gain only a few points?)\n3. Is there evidence that communication quality (vs. model capacity/reasoning ability) is actually the bottleneck at 1.7B scale?\n4. Search for \"small language model multi-agent discussion diminishing returns\" or similar to see if there's evidence that small models don't benefit much from multi-agent collaboration.\n5. What does the Qwen3-1.7B model achieve on AIME24 in single-agent mode?\n\nThe concern: if the 1.7B model only gains ~3 points from multi-agent setup (13.4% → 16.7%), improving communication quality may yield minimal additional gains because the model lacks fundamental reasoning capacity, not communication quality.\n\nReport your findings.",
    "agentId": "aa219ab732b86947d",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "I have gathered extensive information. Here is my comprehensive report.\n\n---\n\n## Findings Report: AT-GRPO Claims Analysis for AIME24\n\n### 1. Exact AT-GRPO Results from the Stronger-MAS Paper (arXiv 2510.11062)\n\nThe numbers from the paper (Tables 1 and 2) are confirmed:\n\n**Qwen3-1.7B on AIME24:**\n| Configuration | Accuracy |\n|---|---|\n| Single Agent (baseline) | 13.40% |\n| Single Agent + GRPO | 10.00% |\n| MAS (prompt-only, no training) | 13.30% |\n| MAS + GRPO | 13.30% |\n| MAS + AT-GRPO (shared policy) | **16.70%** |\n| MAS + AT-GRPO (per-role policies) | 13.30% |\n\n**Qwen3-8B on AIME24:**\n| Configuration | Accuracy |\n|---|---|\n| Single Agent (baseline) | 18.30% |\n| Single Agent + GRPO | 18.30% |\n| MAS (prompt-only, no training) | 36.60% |\n| MAS + GRPO | 33.30% |\n| MAS + AT-GRPO (shared policy) | **50.00%** |\n| MAS + AT-GRPO (per-role policies) | **57.00%** |\n\nThe single-agent baseline for Qwen3-1.7B on AIME24 is **13.40%**.\n\n### 2. Multi-Agent Gain at 1.7B Scale\n\nThe concern raised in the research proposal is well-founded. At 1.7B:\n\n- **Single agent baseline**: 13.40%\n- **Best multi-agent (AT-GRPO shared)**: 16.70%\n- **Net gain**: +3.30 percentage points\n\nNotably, even the untrained MAS (prompt-only) at 1.7B shows **no gain** over single agent (13.30% vs 13.40% -- essentially equivalent or slightly worse). Standard GRPO training actually *hurts* performance (dropping single-agent to 10.00%).\n\nCompare this to 8B, where:\n- **Single agent baseline**: 18.30%\n- **Best multi-agent (AT-GRPO per-role)**: 57.00%\n- **Net gain**: +38.70 percentage points\n- Even untrained MAS doubles performance: 36.60% vs 18.30%\n\nThe contrast is stark. At 8B, simply putting models into a multi-agent discussion without any training already doubles performance (18.3% to 36.6%). At 1.7B, the same untrained multi-agent setup provides zero benefit (13.4% to 13.3%).\n\n### 3. Is Communication Quality Actually the Bottleneck at 1.7B?\n\n**The evidence is mixed and the claim in the proposal is likely too simplistic.** Here is what the evidence suggests:\n\n**Evidence AGAINST \"communication quality is the dominant bottleneck\":**\n\n- The SLM-MUX paper (arXiv 2510.05077) directly demonstrates that **discussion-based orchestration methods designed for large models actively harm small models**, causing accuracy drops of up to 5.5%. The root cause: \"SLMs tend to exhibit groupthink, reinforcing incorrect reasoning during discussions rather than correcting mistakes.\" 59.5% of failures were attributed to groupthink. The paper explicitly states the bottleneck is that \"SLMs lack sufficient reasoning capacity for this interaction model, making the communication channel irrelevant.\"\n\n- The comprehensive LLM reasoning evaluation paper (arXiv 2601.13243) found that \"additional multi-agent interactions provide limited and inconsistent benefits\" and that \"failed cases are heavily concentrated in the high-cost regime,\" indicating model capacity (ability to solve problems) rather than communication quality is the limiting factor.\n\n**Evidence FOR \"communication quality matters\":**\n\n- The \"Can Small Agents Collaborate\" paper (arXiv 2601.11327) found that communication/orchestration IS the bottleneck when using tool-augmented multi-agent setups with a strong orchestrator. With an 8B orchestrator, sub-agent size barely matters (1.7B sub-agents: 23.0% vs 32B sub-agents: 23.6% on GAIA). However, this involves a heterogeneous architecture with a capable orchestrator, not homogeneous small agents discussing with each other.\n\n- The paper \"Large Language Models Miss the Multi-Agent Mark\" (arXiv 2505.21298) argues natural language communication itself is \"inefficient and ambiguous\" and advocates structured communication protocols, suggesting communication infrastructure matters.\n\n### 4. Small Language Models and Multi-Agent Diminishing Returns\n\nMultiple papers converge on a critical finding: **discussion-based multi-agent methods that work for frontier models fail or backfire for small models.**\n\nKey evidence:\n- **SLM-MUX**: Discussion methods (Mixture-of-Agents, LLM-Debate, Multi-Agent Verification) caused accuracy drops of 2-5.5% for SLMs while improving frontier LLMs by up to 2%. The solution that works: **no inter-model communication at all** -- instead, confidence-based selection where each model generates independently and the most consistent answer wins.\n- **Groupthink**: Small models reinforce each other's errors rather than correcting them. They lack the capacity to critically evaluate another agent's reasoning and identify flaws.\n- **One counterpoint**: The \"Diversity of Thought\" paper (arXiv 2410.12853) found multi-agent debate can help at any scale when using *diverse* models (different architectures), not copies of the same model. This suggests the homogeneous setup in Stronger-MAS (all Qwen3-1.7B agents) is particularly prone to failure.\n\n### 5. Qwen3-1.7B Standalone AIME24 Performance\n\nI was unable to find an official Qwen3-1.7B AIME24 score from the Qwen technical report (the relevant Table 19 is not accessible in the HTML/search-extractable versions). However, the Stronger-MAS paper uses Qwen3-1.7B and reports its single-agent baseline as **13.40%** on AIME24. For reference, Qwen3-32B achieves ~23.3% in non-thinking mode and ~70% in thinking mode on AIME24. The 13.40% figure for 1.7B is consistent with what one would expect for a model of that size.\n\n### Critical Assessment of the Proposal's Claim\n\nThe claim that \"inter-agent communication quality is the dominant bottleneck\" at 1.7B scale is **likely incorrect or at best misleading**. The evidence strongly suggests:\n\n1. **The fundamental bottleneck is reasoning capacity, not communication quality.** At 1.7B, the model cannot reliably solve AIME problems individually (13.4%). Even with perfect communication, multiple copies of a model that cannot solve a problem individually will not solve it collectively -- they will simply reinforce each other's errors (groupthink).\n\n2. **The 3.3-point gain (13.4% to 16.7%) from AT-GRPO at 1.7B likely represents the ceiling of what multi-agent collaboration can extract from this model size on this task.** Improving communication quality further is unlikely to yield meaningful additional gains because the individual agents lack the underlying mathematical reasoning ability.\n\n3. **The 8B results are not simply \"better communication\" -- they reflect an emergent capability threshold.** At 8B, even untrained MAS doubles performance (18.3% to 36.6%), suggesting the 8B model has latent reasoning ability that can be surfaced through discussion. The 1.7B model does not exhibit this property at all (13.4% to 13.3% with untrained MAS).\n\n4. **The most effective approach for small models avoids inter-model communication entirely** (SLM-MUX), suggesting that communication itself is counterproductive, not merely low-quality, at small model scales.\n\n**Bottom line**: If you are proposing to improve inter-agent communication quality as a way to boost 1.7B performance on AIME24, the literature suggests this is unlikely to work. The model lacks the individual reasoning capacity needed to benefit from discussion. The correct framing is not \"communication quality is the bottleneck\" but rather \"the model is below the capability threshold where multi-agent collaboration provides meaningful benefits on hard math tasks.\"\n\nSources:\n- [Stronger-MAS: Multi-Agent Reinforcement Learning for Collaborative LLMs (arXiv 2510.11062)](https://arxiv.org/abs/2510.11062)\n- [SLM-MUX: Orchestrating Small Language Models for Reasoning (arXiv 2510.05077)](https://arxiv.org/html/2510.05077)\n- [Can Small Agents Collaborate to Beat a Single Large Language Model? (arXiv 2601.11327)](https://arxiv.org/html/2601.11327)\n- [A Comprehensive Evaluation of LLM Reasoning: From Single-Model to Multi-Agent Paradigms (arXiv 2601.13243)](https://arxiv.org/html/2601.13243)\n- [Large Language Models Miss the Multi-Agent Mark (arXiv 2505.21298)](https://arxiv.org/html/2505.21298)\n- [Diversity of Thought Elicits Stronger Reasoning in Multi-Agent Debate (arXiv 2410.12853)](https://arxiv.org/abs/2410.12853)\n- [PettingLLMs GitHub Repository](https://github.com/pettingllms-ai/PettingLLMs)\n- [Qwen3 Technical Report (arXiv 2505.09388)](https://arxiv.org/abs/2505.09388)"
      }
    ],
    "totalDurationMs": 218858,
    "totalTokens": 31810,
    "totalToolUseCount": 26,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 395,
      "cache_read_input_tokens": 29054,
      "output_tokens": 2360,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 395
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2360,
          "cache_read_input_tokens": 29054,
          "cache_creation_input_tokens": 395,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 395,
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
  "sourceToolAssistantUUID": "3373a925-a200-4f2f-a861-19bc52eacf4f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c886791-a9d9-487c-99a0-b2a7b1d3d99e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 35 · 2026-05-10T22:23:28.629Z_

```json
{
  "parentUuid": "7ca23970-887d-4112-a19c-ba042e33f526",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "afdfe46e-1df1-425d-89d1-2e10182b4c9f",
  "timestamp": "2026-05-10T22:23:28.629Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c886791-a9d9-487c-99a0-b2a7b1d3d99e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 36 · 2026-05-10T22:24:26.902Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the data I need to write a comprehensive review. Let me synthesize everything.

## Summary of Findings

### What's Improved (from Round 7):
1. **CLIPO and AMIR-GRPO properly cited** ✓ - The novelty is reframed as extending intra-group contrastive learning from reasoning to communication
2. **Compute budget** ✓ - ~55h H100, well within 200h constraint
3. **Venue targeting** ✓ - Now targets EMNLP 2026 ARR May 25 (matches user's requirement)


4. **Landscape comprehensiveness** ✓ - Very thorough, most relevant work cited
5. **Bilateral formulation novelty confirmed** ✓ - No existing paper does bilateral contrastive training of both sender and receiver in LLM multi-agent systems

### Critical Issues Remaining:

There's a persistent benchmark compliance problem—AIME isn't on the allowed list (AgentBench, WebArena, SWE-bench Verified, GAIA, ToolBench, ALFWorld, Mind2Web, τ-bench), and this constraint violation has carried through every round of revisions.

The core assumption about communication bottlenecks at 1.7B parameters appears empirically shaky. Recent work shows small models actually suffer from groupthink in multi-agent setups, with untrained systems providing negligible gains and even trained approaches only yielding modest improvements—suggesting the real constraint is reasoning capacity rather than communication quality.

Using only AIME24 as a single evaluation benchmark feels thin for an EMNLP submission, and the novelty claim is starting to feel incremental.

I'm also noticing several citation gaps that undermine the framing. SLM-MUX directly contradicts the proposal's premise by showing discussion-based methods harm small models, and there are missing references to MAGE on graph contrastive learning for multi-agent systems and M-GRPO on hierarchical multi-agent GRPO extensions that should be in the landscape.

Looking at the scores now: the bilateral contrastive formulation with sender and receiver losses is genuinely novel, but it's fundamentally a domain transfer of CLIPO's mechanism where each component—stop-gradient, EMA, attention pooling, InfoNCE—is borrowed from existing work, so the conceptual contribution feels incremental. On feasibility, the compute budget works and the infrastructure is there, but AIME isn't on the allowed benchmark list which is a hard constraint violation, and the empirical premise that communication quality is the bottleneck at 1.7B seems contradicted by the SLM-MUX findings.

The proposal is well-structured with excellent landscape coverage and clear differentiation from CLIPO, but the impact is fundamentally limited—the evidence suggests small models don't actually benefit from multi-agent discussion, the 3.3-point AT-GRPO baseline gain leaves minimal headroom for improvement, and even if the approach works technically, it's only tested on AIME math rather than agent benchmarks and specific to a scale where multi-agent gains are already minimal.

This puts the average score well below the 4.0 threshold, so revision is needed, though I'm increasingly concerned the core premise itself might be unfixable after eight rounds of iteration. The persistent benchmark feasibility issues combined with the SLM-MUX evidence undermining the fundamental assumption is pushing this toward failure territory. That said, there might be a path forward if the proposal shifts to 8B models where multi-agent gains are substantial, since communication quality training could plausibly matter more at that scale—though the compute constraints would need to be addressed.

Alternatively, I could restructure around an allowed benchmark like ALFWorld with a planner-executor setup, pair it with 8B models using LoRA for efficiency, and that would tackle both the benchmark and premise problems. The core idea is salvageable but only with significant restructuring and very specific guidance on which direction to take.

Let me think through the benchmark constraint more carefully though. The user's list is explicit—AgentBench, WebArena, SWE-bench Verified, GAIA, ToolBench, ALFWorld, Mind2Web, τ-bench—but the proposal uses AIME with multi-agent discussion from PettingLLMs, which is published but not on that list. There's an argument that the list was designed for general agent tasks rather than multi-agent communication specifically, but the constraint is clear enough that the proposal should at least acknowledge this deviation and provide justification.

If I reframe the impact differently—using smaller 3-4B models where multi-agent collaboration might hit a sweet spot, showing that BIG improves communication quality at scales where coordination actually works, and demonstrating it on ALFWorld instead—that becomes much stronger. But it's essentially a different paper.

I'll recommend a revise with specific guidance on these tradeoffs.

For Round 8, I need to be honest about whether two more revisions can realistically address the core issues. The benchmark compliance is fixable by switching to ALFWorld or adding a second allowed benchmark. The communication bottleneck premise is fixable by moving to 7B or 8B models, or by directly addressing the SLM-MUX evidence. The incremental novelty is inherent to the approach but can be strengthened with better empirical results. The single-benchmark limitation is also fixable. The most fragile piece is the underlying premise—if the proposal stays at 1.7B, it has to contend with existing evidence that smaller models struggle with multi-agent communication. If it scales up, compute requirements increase, though LoRA might keep it within the 200-hour budget.

All of these are addressable in principle, so I'll give a revise verdict with clear feedback on each issue.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "afdfe46e-1df1-425d-89d1-2e10182b4c9f",
  "isSidechain": false,
  "requestId": "req_011CaufrHVSophaKgUiNuf9A",
  "type": "assistant",
  "uuid": "e6e85c6f-b46c-4ab6-9188-f3102fe9fa32",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c886791-a9d9-487c-99a0-b2a7b1d3d99e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016ARt6c2Ah2Mn8TpYQFNjvK",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8205,
      "cache_read_input_tokens": 52711,
      "output_tokens": 4586,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8205,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 4586,
          "cache_read_input_tokens": 52711,
          "cache_creation_input_tokens": 8205,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8205
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Assistant

_source line 37 · 2026-05-10T22:25:17.129Z_

I now have comprehensive data from my independent verification. Let me synthesize my findings into the review.

## Key Findings from Independent Verification

**Verified claims:**
- CLIPO (arXiv 2603.10101) and AMIR-GRPO (arXiv 2601.03661) confirmed real with correct descriptions
- CLIPO public code verified at github.com/Qwen-Applications/CLIPO
- PettingLLMs public code verified, supports AIME natively
- All 6 additionally cited papers (DiffMAS, RecursiveMAS, CoFi-PGMA, Graph-GRPO, EMA-PG, arXiv 2605.02801) verified
- TACTIC confirmed to pre-train both sender AND receiver then freeze during RL
- No existing paper found performing bilateral contrastive training of sender+receiver in LLM multi-agent systems — the gap is real

**Critical discoveries:**
- AIME is NOT on the user's allowed benchmark list
- AT-GRPO 16.7% at 1.7B is only +3.3 points over single-agent baseline (13.4%)
- SLM-MUX (arXiv 2510.05077) shows discussion-based multi-agent methods actively HARM small models due to groupthink
- At 1.7B, untrained MAS provides ZERO gain (13.3% vs 13.4% single-agent)

```json
{
  "verdict": "revise",
  "scores": {
    "novelty": {"score": 3, "rationale": "The bilateral contrastive formulation (sender + receiver losses using GRPO-group negatives with intent-specificity objective) is genuinely novel — no existing paper does this. However, the contribution is fundamentally a domain transfer of CLIPO's mechanism to communication, with each adaptation component borrowed from prior work (stop-gradient, EMA from EMA-PG, attention pooling from Yang 2016/Lin 2017). Incremental but real."},
    "feasibility": {"score": 2, "rationale": "Compute (55h) fits within budget, and PettingLLMs + CLIPO code reduce engineering effort. However: (a) AIME is NOT on the user's allowed benchmark list — a hard constraint violation persisting across ALL 8 rounds; (b) the core empirical premise (communication quality is the 1.7B bottleneck) is directly contradicted by SLM-MUX (arXiv 2510.05077) showing small models suffer from groupthink, not poor communication quality; (c) only +3.3 points from AT-GRPO at 1.7B leaves minimal headroom for further communication improvement."},
    "clarity": {"score": 4, "rationale": "Excellent landscape coverage — the most comprehensive of all 8 rounds. Clear differentiation from CLIPO (outcome consistency vs intent specificity), well-designed 5-condition experiment isolating bilateral contribution. The reframing as 'extending GRPO-group contrastive learning from reasoning to communication' is honest and well-articulated."},
    "impact": {"score": 2, "rationale": "The core premise is empirically undermined: at 1.7B, multi-agent discussion provides only +3.3 points on AIME24, and SLM-MUX shows discussion-based methods actively harm small models via groupthink. Even if BIG works technically, a +1-2 point improvement on AIME24 at 1.7B is not compelling for EMNLP. Evaluated on a single non-allowed benchmark in a regime where the literature predicts failure."}
  },
  "issues": [
    "BENCHMARK NON-COMPLIANCE (CRITICAL, PERSISTENT ACROSS ALL 8 ROUNDS): AIME is NOT on the user's allowed benchmark list (AgentBench, WebArena, SWE-bench Verified, GAIA, ToolBench, ALFWorld, Mind2Web, τ-bench). Previous rounds used ALFWorld (on the list) and WebArena-Lite (partially compliant); this round regressed to AIME-only, which is fully non-compliant. AIME is a math reasoning benchmark, not an agent benchmark — categorically different from the allowed list which evaluates planning, tool use, and environment interaction.",
    "CORE PREMISE EMPIRICALLY UNDERMINED — SLM-MUX (arXiv 2510.05077, ICLR 2026 under review): This paper directly contradicts the proposal's core assumption. SLM-MUX demonstrates that discussion-based multi-agent methods (including debate and verification) cause accuracy DROPS of 2-5.5% for small language models due to groupthink — 59.5% of failures attributed to models reinforcing each other's errors. At 1.7B, the bottleneck is reasoning capacity, not communication quality. The SLM-MUX finding that the best approach for small models avoids inter-model communication entirely is devastating to BIG's premise.",
    "MINIMAL HEADROOM AT 1.7B: Stronger-MAS data shows untrained MAS at 1.7B provides ZERO gain (13.3% vs 13.4% single-agent). AT-GRPO provides only +3.3 points (13.4% → 16.7%). Compare to 8B where untrained MAS nearly doubles performance (18.3% → 36.6%) and AT-GRPO adds +38.7 points. This strongly suggests 1.7B models are below the capability threshold where multi-agent collaboration provides meaningful benefits on hard math — improving communication quality cannot compensate for insufficient individual reasoning capacity.",
    "SINGLE NON-ALLOWED BENCHMARK: EMNLP-scoped evaluation uses only AIME24 — a math reasoning benchmark not on the allowed list. For any top venue, a single benchmark is thin. For a methods paper claiming to improve multi-agent communication, evaluation should include at least one benchmark where communication genuinely matters (e.g., ALFWorld planner-executor where high-level plans must be communicated to executors).",
    "MISSING CRITICAL CITATION — SLM-MUX (arXiv 2510.05077): Directly relevant paper showing small-model multi-agent discussion fails. Must be cited and the proposal must either (a) switch to a model scale where multi-agent collaboration works, or (b) provide a convincing argument for why contrastive communication training overcomes the groupthink problem that SLM-MUX identifies.",
    "MISSING CITATION — M-GRPO (arXiv 2511.13288, Nov 2025): Extends GRPO to vertical/hierarchical multi-agent LLM systems with trajectory-alignment for variable sub-agent invocations. Directly relevant as another GRPO extension for multi-agent settings.",
    "UNSUBSTANTIATED CAUSAL CLAIM: 'inter-agent communication quality the dominant bottleneck' at 1.7B is stated as fact without evidence. The 1.7B→8B performance gap (16.7% vs 50-57%) could be due to reasoning capacity, world knowledge, instruction following, or many other factors beyond communication quality. This claim requires supporting evidence, not assertion."
  ],
  "feedback": "The proposal has reached strong quality in landscape coverage, reference verification, and structural clarity after 8 rounds — the reframing around CLIPO is honest and the bilateral formulation is genuinely novel. However, two fundamental problems must be resolved for the final rounds:\n\n1. **FIX THE MODEL SCALE OR DEFEND AGAINST SLM-MUX (CRITICAL)**: The proposal's entire premise — that communication quality is the bottleneck at 1.7B — is contradicted by SLM-MUX (arXiv 2510.05077), which shows small models suffer from groupthink in multi-agent discussion. Three options: (a) Switch to Qwen3-4B or 8B with LoRA (rank=32 to manage memory), where multi-agent discussion demonstrably helps (+20-38 points on AIME24 at 8B). Compute increases but may still fit within 200h with aggressive LoRA. (b) Keep 1.7B but explicitly hypothesize that BIG's bilateral contrastive training MITIGATES groupthink by forcing message-intent specificity — and frame the experiment as testing this hypothesis (with SLM-MUX as the null hypothesis). (c) Switch to a task where small models DO benefit from communication (e.g., code collaboration in PettingLLMs, where Tool-User + Reasoner roles have clearer communication needs). Option (b) is riskiest but most interesting; option (a) is safest.\n\n2. **USE AT LEAST ONE BENCHMARK FROM THE ALLOWED LIST (MANDATORY)**: This constraint has been violated in every round. Concrete path: Add ALFWorld with a planner-executor setup (as in Rounds 3-6). PettingLLMs doesn't support ALFWorld natively, but Round 6 already explored this — use CoDA's architecture or implement a simple planner-executor split. Alternatively, use τ-bench (multi-turn agent-user interaction) which could showcase communication quality. Even if AIME remains the PRIMARY benchmark, having one allowed-list benchmark demonstrates generalization and satisfies the constraint.\n\n3. **Cite SLM-MUX and address head-on**: Don't ignore the evidence against your premise. Frame it: 'SLM-MUX shows naive multi-agent discussion hurts small models via groupthink. We hypothesize that this failure stems from undifferentiated, non-specific messages that reinforce dominant (often incorrect) reasoning patterns. BIG's intent-specificity training should produce messages that convey specific, distinguishable intents rather than generic agreement, potentially mitigating groupthink.' This turns a weakness into a testable hypothesis.\n\n4. **Minor**: Cite M-GRPO (arXiv 2511.13288) for landscape completeness. Consider adding a groupthink analysis metric — e.g., measure message diversity/entropy across agents before and after BIG training to test whether BIG reduces groupthink.\n\nBottom line: The bilateral contrastive formulation is novel and the landscape is excellent, but the empirical setting (1.7B on AIME) is the weakest possible choice — both off the allowed benchmark list AND in a regime where the literature predicts failure. Fix the setting, and this becomes a viable Findings paper.",
  "reason": "Benchmark non-compliance persists (AIME not on allowed list), and the core premise (communication quality bottleneck at 1.7B) is empirically undermined by SLM-MUX showing small models suffer from groupthink, not poor communication quality — the experimental setting must be fixed."
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e6e85c6f-b46c-4ab6-9188-f3102fe9fa32",
  "isSidechain": false,
  "requestId": "req_011CaufrHVSophaKgUiNuf9A",
  "type": "assistant",
  "uuid": "514d49dc-61d2-40e2-94bf-cb1495880d2b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c886791-a9d9-487c-99a0-b2a7b1d3d99e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016ARt6c2Ah2Mn8TpYQFNjvK",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8205,
      "cache_read_input_tokens": 52711,
      "output_tokens": 4586,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8205,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 4586,
          "cache_read_input_tokens": 52711,
          "cache_creation_input_tokens": 8205,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8205
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
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
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-10 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "514d49dc-61d2-40e2-94bf-cb1495880d2b",
  "sessionId": "0c886791-a9d9-487c-99a0-b2a7b1d3d99e"
}
```

---

### Runtime record

_source line 39_

```json
{
  "type": "ai-title",
  "aiTitle": "Bilateral intent grounding for multi-agent LLM communication",
  "sessionId": "0c886791-a9d9-487c-99a0-b2a7b1d3d99e"
}
```

---

### Runtime record

_source line 40_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-10 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "514d49dc-61d2-40e2-94bf-cb1495880d2b",
  "sessionId": "0c886791-a9d9-487c-99a0-b2a7b1d3d99e"
}
```

---

### Runtime record

_source line 41_

```json
{
  "type": "ai-title",
  "aiTitle": "Bilateral intent grounding for multi-agent LLM communication",
  "sessionId": "0c886791-a9d9-487c-99a0-b2a7b1d3d99e"
}
```

---
