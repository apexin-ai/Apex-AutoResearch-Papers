# Research conversation: You are a strict ML research reviewer conducting adversarial review. **Today's date: 2026-05-13 (UTC).** Your job: indep

**When Does Detect-and-Reweight Work for Synthetic Contamination? (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 58
- **Recorded user turns:** 1
- **Tool calls:** 14
- **Original source:** `logs/chats/exported-trajectories/account-3/38eec20f-28d6-4706-b24b-8f0ea53acfb9.jsonl`
- **Structured JSON:** [`76f914090191ccd0ebe2.json`](../../sessions/76/76f914090191ccd0ebe2.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-13T04:42:06.512Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-13T04:42:06.512Z",
  "sessionId": "38eec20f-28d6-4706-b24b-8f0ea53acfb9",
  "content": "You are a strict ML research reviewer conducting adversarial review.\n\n**Today's date: 2026-05-13 (UTC).**\n\nYour job: independently verify this idea's claims via WebSearch, then issue a verdict.\n\n## User requirements\nThe user asked for: **VLA中的token裁剪/增强能否提升VLA模型的泛化性（多从理论角度分析为何能增强）**\nYou MUST evaluate whether this idea actually meets the user's requirements. If the user asked for a top venue, assess whether the idea is truly top-venue quality. If the user asked for low resource cost, verify the resource estimate is realistic and low. An idea that doesn't match what the user asked for should be \"revise\" or \"fail\".\n\n## 核心要求：非常仔细地调研，非常仔细地思考\n\n你是一个严格的审稿人。不要轻信 Generator 的任何 claim——你必须独立验证，深入思考每个维度。\n\n### 调研要求\n\n1. **独立 SOTA 验证**：自己搜索当前 SOTA，不要只检查 Generator 的引用。\n   每个验证维度建议用 2-3 种不同的搜索查询。\n\n2. **可行性深度检查**：\n   - 搜索类似实验的实际成本/周期\n   - 检查 claimed baselines 是否可复现\n   - 验证所需的 datasets/models 是否真的可以获取\n\n3. **新颖性压力测试**：专门搜索 Generator 可能遗漏的工作：\n   - 尝试不同的关键词组合\n   - 同时检查 arXiv 和 conference proceedings\n   - 寻找相邻领域的并行/concurrent 工作\n\n4. **深入阅读**：不要只依赖搜索摘要。用 WebFetch 实际阅读相关论文的 abstract 和关键章节，形成你自己的判断。\n\n### 思考要求\n\n5. **独立判断**：\n   - 不要因为 Generator 说得有道理就轻易 pass——真正好的 idea 经得起严格审查\n   - 思考这个 idea 在实际执行中会遇到什么困难\n   - 考虑这个 idea 对领域的真实贡献（不是自说自话的贡献）\n\n6. **评分诚实**：\n   - 不要给\"看起来还行\"的 idea 高分——4 分意味着\"确实很好\"，5 分意味着\"令人兴奋\"\n   - Agent 评分经常虚高，你的职责就是纠正这种偏差\n\n充分利用你的工具——做真正的调研，不是走过场。\n\n\n## 论文搜索策略\n\n你的搜索质量直接决定了 idea 的质量。不要敷衍搜索——每一次搜索都要有明确的目的。\n\n### 搜索源（推荐每个维度使用 2 个不同来源）\n\n1. **arXiv 预印本**（最新工作）:\n   - `site:arxiv.org {topic} {year}` — 按主题搜索最新论文\n   - `site:arxiv.org {method_name}` — 按具体方法名搜索\n   - `arxiv {topic} {month} {year}` — 精确到月份，找最近 3 个月的工作\n\n2. **Google Scholar**（引用关系 + 综合覆盖）:\n   - `{topic} {year} site:scholar.google.com` — 或直接搜索让 Google 自动包含 Scholar 结果\n   - `\"{exact paper title}\"` — 验证论文是否真实存在\n   - `\"{author name}\" {topic} {year}` — 按活跃作者追踪（找到领域大牛后追踪其最新工作）\n\n3. **Papers With Code**（SOTA 排行 + 代码可用性）:\n   - `site:paperswithcode.com {task_name}` — 查看任务的 SOTA 排行榜\n   - `site:paperswithcode.com {method_name}` — 查看方法是否已被实现\n   - `paperswithcode {dataset} benchmark` — 查看特定 dataset 上的竞争格局\n\n4. **OpenReview**（会议审稿 + 同行评价）:\n   - `site:openreview.net {topic} {year}` — 搜索会议提交的论文\n   - 用 WebFetch 阅读 OpenReview 上的 reviewer comments — 了解领域专家的真实评价\n\n5. **Semantic Scholar**（语义搜索 + 引用图谱）:\n   - `semantic scholar {topic} survey {year}` — 找综述论文\n   - `semanticscholar.org {paper_title}` — 查看 cited by（谁引用了这篇）和 references（它引用了谁）\n\n6. **GitHub**（实现验证）:\n   - `site:github.com {method_name} {task}` — 验证开源实现是否存在\n   - `site:huggingface.co {model_name}` — 验证模型/数据集是否可获取\n\n### 搜索维度（多角度交叉，不要只按 topic 搜）\n\n对每个 idea/方向，尽量覆盖以下维度：\n\n1. **正向搜索**：直接搜索主题相关论文\n   - `{topic} {subtopic} {year}`\n   - `{method_name} for {task_name}`\n\n2. **竞争论文搜索**（最关键！）：\n   - `{core_problem} {year}` — 有没有人在解决同样的问题？\n   - `{approach_keyword} {task} {year}` — 有没有人用类似方法？\n   - `{gap_description} solution` — 你发现的 gap 是否已被解决？\n   - **搜索知名团队的最新工作**：如果你知道哪些团队在做这个方向，搜索他们最近 6 个月的论文\n\n3. **相邻领域搜索**：\n   - `{method_from_other_field} applied to {your_task}`\n   - `{your_problem} in {adjacent_domain}` — 其他领域是否已解决类似问题\n\n4. **反面搜索**（找到反对你 idea 的证据）：\n   - `{your_approach} limitations` / `{your_approach} failure`\n   - `why {assumed_gap} is not a problem`\n   - `{baseline_method} sufficient for {task}` — baseline 是否其实已经够好\n\n5. **引用链追踪**（发现遗漏工作的最有效方法）：\n   - 找到一篇核心相关论文后，用 WebFetch 阅读它的 references 部分\n   - 在 Semantic Scholar 上查看它的 \"cited by\" — 最近引用它的论文很可能是 concurrent work\n   - 对 3 个以上核心相关论文重复此步骤\n\n### 搜索数量建议（理想目标，上下文充裕时尽量达到）\n\n| 角色 | 建议搜索次数 | 说明 |\n|------|-------------|------|\n| Round 1 Generator | 10-15 次 | 每个方向争取 3 次独立搜索 |\n| Round 2 Generator | 5-8 次 | 验证 approach 可行性 + baseline |\n| Review Agent | 8-12 次 | 独立验证 + 竞争论文 + 反面证据 |\n| Revision Agent | 5-10 次 | 针对每个 issue 独立调研 |\n\n### 上下文管理\n\n你的输出 token 有限，必须在上下文耗尽之前完成 JSON 输出。\n\n- 上述搜索次数是理想目标。在上下文充裕时应尽量多搜、深搜，搜得越充分越好。\n- 但必须动态评估剩余上下文：如果已经消耗了大量上下文，应优先完成输出，不要为了凑次数而冒着无法输出的风险。\n- WebFetch 深度阅读很有价值，但每次 fetch 消耗大量 token——优先 fetch 最关键的 2-3 篇，而不是每篇都 fetch。\n- 质量 > 数量：5 次精准搜索 + 深度思考 > 15 次浅层搜索。\n\n\nAs a reviewer, your search focus should be:\n1. **验证 claim**：Generator 声称的 SOTA、gap、novelty 是否属实\n2. **找竞争论文**：是否有 Generator 遗漏的高度相关/相似的工作\n3. **找反面证据**：是否有论文表明 Generator 的 approach 行不通\n4. **引用链检查**：通过核心论文的 cited-by 发现 concurrent work\n\n## 竞争论文专项搜索（Reviewer 独有）\n\n这是你作为 Reviewer 最重要的职责之一——发现 Generator 遗漏的竞争工作：\n\n1. **关键词变体搜索**：用至少 3 种不同的关键词组合搜索同一个问题\n   - 同义词替换（e.g., 'efficient' → 'lightweight/fast/scalable'）\n   - 不同粒度（e.g., 'text classification' → 'sentiment analysis' → 'NLP'）\n   - 方法名 + 任务名的不同组合\n\n2. **知名团队追踪**：如果你知道哪些团队/实验室在做相关方向，\n   搜索他们最近的论文（`\"team_name\" OR \"author_name\" {topic} {year}`）\n\n3. **会议最新录用**：搜索最近一轮 ICML/NeurIPS/ICLR/AAAI/ACL 等会议的 accepted papers\n   - `site:openreview.net {topic} 2026`\n   - `{conference_name} 2026 accepted papers {topic}`\n\n4. **arXiv 近 3 个月密集搜索**：对精确相关的关键词，搜索过去 3 个月的 arXiv 论文\n   这是发现 concurrent work 最有效的窗口\n\n如果你发现了 Generator 遗漏的重要相关工作，必须在 issues 中列出论文标题和链接，\n并在 feedback 中说明这些工作如何影响 idea 的 novelty。\n\n## Review checklist\n1. **SOTA freshness**: Are the models/baselines cited actually current SOTA?\n   If outdated, specify what the current SOTA is and cite your source.\n2. **Reference verification**: Do the cited papers actually exist? (WebSearch to check)\n3. **Gap validity**: Does the claimed research gap still exist, or has recent work addressed it?\n4. **Venue validity**: Are target_venues' submission deadlines after 2026-05-13?\n5. **Feasibility**: Is the resource estimate realistic? Are there hidden dependencies?\n6. **Novelty**: Is this sufficiently different from existing work?\n   When scoring novelty < 4:\n   - You MUST identify the closest existing work(s) via WebSearch\n   - In your feedback, write: \"This idea is too similar to [Paper Title (Venue Year)]. Specifically, [what overlaps]. To differentiate, the generator should [suggestion].\"\n   - This gives the generator targeted guidance to boost novelty, not just \"be more novel\".\n7. **Cost realism across modes**: Are the three mode estimates (manual/human-in-loop/auto) internally consistent?\n   - Auto Research uses more GPU hours (2-5x manual) but GPU idle rate should be near zero\n   - Auto Research timeline should reflect resource availability as bottleneck — days with sufficient GPUs, not weeks\n   - Human-in-Loop should fall between manual and auto on most dimensions\n   - Manual and HIL must NOT include salary/wages — only GPU and API costs\n   - Auto Research must NOT include agent operational overhead\n   - If any mode estimate is clearly unrealistic, flag it\n\n## Idea under review (round 2/10)\n{\n  \"title\": \"Counterfactual Token Masking: A Theoretically Grounded Framework for Robust VLA Finetuning via Implicit Causal Data Augmentation\",\n  \"core_problem\": \"VLA finetuning on robotic demonstration data suffers from representation degradation (attention migration to background tokens, representation collapse, domain-specific forgetting) primarily because demonstration data is inherently low-diversity — the same table, background, lighting, and camera pose repeat across thousands of episodes. Existing mitigation approaches (frozen-encoder alignment, dual encoders, contrastive state regularization, spectral expert decomposition, action-as-language reformulation) each address specific symptoms but none exploit the fundamental causal structure of the problem: spurious visual correlations in low-diversity robot data drive representation collapse, and these correlations can be broken through principled counterfactual interventions on visual tokens during training.\",\n  \"opportunity\": \"The convergence of three independent research lines creates a unique theoretical opportunity: (1) 'Masked Images Are Counterfactual Samples' (Xiao et al., CVPR 2023) established that masking image patches and refilling them constitutes a counterfactual intervention that breaks spurious correlations in finetuning, but applied this only to classification with CAM-guided masking; (2) Information Dropout (Achille & Soatto, TPAMI 2018) proved that multiplicative noise on representations is equivalent to IB regularization, learning representations invariant to nuisance factors; (3) 'Don't Blind Your VLA' (arXiv 2510.25616) and RS-CL (ICLR 2026) independently documented that VLA finetuning destroys pretrained visual representations, with the former showing attention migration from task-relevant to background tokens and the latter showing that representation-level regularization (view cutoff, contrastive loss) yields large gains. The gap is that no existing work synthesizes these insights: applying counterfactual token-level masking specifically to the VLA finetuning setting, with formal IB-theoretic and causal justification for why this prevents the documented pathologies. PatchDropout (WACV 2023) showed random patch dropout improves ViT training, but in standard training — not the unique frozen-ViT → projector → LLM pipeline of VLAs where the regularization target and gradient dynamics differ fundamentally. LightVLA (ICRA 2026) showed training-time differentiable token selection improves VLA performance (+2.6%), providing empirical evidence that training-time token manipulation benefits VLAs — but framed as efficiency, without theoretical analysis of the regularization effect.\",\n  \"landscape\": \"The VLA representation preservation space now contains at least six concurrent approaches: (1) Frozen-encoder alignment: 'Don't Blind Your VLA' (arXiv 2510.25616) pulls VLA hidden states toward a frozen teacher's features via cosine similarity loss, directly mitigating attention sink. (2) Dual-encoder co-training: Gen-VLA (arXiv 2509.11417) uses separate encoders for action prediction and VL understanding with co-training to prevent forgetting. (3) Contrastive state regularization: RS-CL (ICLR 2026) shapes representations via InfoNCE weighted by robot proprioceptive state distances, with 'view cutoff' augmentation that masks entire camera view features (representation-level, not token-level). (4) Spectral expert decomposition: VLA-GSE (arXiv 2605.06175) initializes generalized/specialized experts from SVD of frozen backbone, addressing overfitting via parameter-efficient adaptation. (5) Action-as-language: VLM2VLA (ICLR 2026) represents actions in natural language to avoid distribution mismatch. (6) Asymmetric dual-critic regularization: CRL-VLA (arXiv 2602.03445) uses frozen/trainable critic pair for continual learning. In the broader token masking/dropout literature: PatchDropout (WACV 2023) randomly drops input patches during ViT training for efficiency and implicit regularization. DropKey (CVPR 2023) applies dropout to attention keys before softmax in ViTs. EntroDrop (arXiv 2512.23422) uses entropy-guided token dropout for LLM training. 'Masked Images Are Counterfactual Samples' (CVPR 2023) uses CAM-guided masked patches with feature distillation for robust classification finetuning. 'To Sink or Not to Sink' (ICLR 2026) shows that ViT attention sinks in VLMs actually encode high-level semantic concepts, challenging the view that sinks are purely pathological — the nuance being that sinks become harmful specifically when VLA finetuning causes attention to MIGRATE from task-relevant to background tokens, not because sinks themselves are inherently bad. The Token Reduction Survey (arXiv 2505.18227) argues token reduction should go beyond efficiency in generative models. CRAFT (arXiv 2602.12532) applies VIB for force modality integration. Gaze-Regularized VLA (arXiv 2603.23202) regularizes attention via KL to human gaze maps (requires external data). TraceVLA (ICLR 2025) uses visual trace prompt dropout but only drops/retains the trace overlay. The specific gap we target: no existing work provides a formal theoretical framework connecting token-level masking during VLA finetuning to (a) information-bottleneck regularization adapted to the frozen-ViT → projector → LLM architecture, (b) counterfactual data augmentation that breaks the spurious visual correlations inherent in low-diversity robot demonstration data, and (c) attention entropy preservation guarantees.\",\n  \"approach\": \"We propose Counterfactual Token Masking (CTM), a theoretically grounded framework for robust VLA finetuning that operates by stochastically masking visual patch tokens after the ViT projector and before the LLM backbone. The framework has three components:\\n\\n**Component 1: Uniform CTM (baseline).** At each training step, independently mask each projected visual token with probability p (cosine-annealed from 0.25→0.05 over training), replacing masked tokens with a learned [MASK] embedding. This forces the LLM backbone to predict actions even when 'easy' background tokens (which dominate low-diversity robot data) are absent, creating implicit counterfactual training samples. Placement after the projector is critical: pre-projector masking would save compute but cannot regularize the projector→LLM interface where representation collapse concentrates; post-LLM-embedding masking would disrupt the LLM's pretrained token interactions.\\n\\n**Component 2: Adaptive CTM (main contribution).** Replace uniform masking with learned per-token masking rates via the Information Dropout formulation. A lightweight module (single-layer MLP, ~0.1M parameters) takes each projected visual token and outputs a per-token log-variance α_i. Token i is masked with probability σ(α_i), where σ is the sigmoid function. A KL penalty term β·Σ_i KL(Bernoulli(σ(α_i)) || Bernoulli(p_prior)) is added to the action prediction loss, where p_prior is the base masking rate (0.15). β is warmed up from 0→1 over the first 20% of training to allow the model to first learn action prediction before the IB constraint tightens. This module operates entirely on the projector's output and is compatible with LoRA finetuning of the LLM backbone — it does not modify the frozen ViT.\\n\\n**Component 3: Theoretical Analysis.** We provide: (a) A formal derivation of the IB bound for VLA finetuning with token masking: following Achille & Soatto (2018), we show that stochastic token masking minimizes an upper bound on I(Z_v; X_v | A), where Z_v is the visual representation entering the LLM, X_v is the raw visual input, and A is the target action. This bound decomposes into the action prediction loss plus a complexity term penalizing representation dependence on individual input tokens. (b) A proof that token masking with probability p > 0 lower-bounds the attention entropy of the LLM's first layer over visual tokens by H ≥ -log(1-p) - ε under mild conditions on the attention temperature, preventing the degenerate attention collapse documented in 'Don't Blind Your VLA'. This reconciles with 'To Sink or Not to Sink' (ICLR 2026): attention sinks are beneficial for encoding visual summaries, but finetuning-induced migration of attention mass to background sinks is harmful — CTM prevents migration without eliminating sinks. (c) A PAC-Bayes generalization bound adapted from Gal & Ghahramani (2016): treating token masking as a stochastic posterior over sub-networks, we derive a tighter generalization bound for the VLA that decreases with the masking rate, formally justifying why CTM improves OOD transfer. (d) A causal analysis connecting to the counterfactual framework of Xiao et al. (CVPR 2023): masking tokens from low-diversity background regions constitutes a do-calculus intervention do(X_bg = ∅) that identifies the causal effect of task-relevant visual features on action prediction, breaking spurious correlations between background appearance and action labels.\\n\\n**Base model:** OpenVLA-OFT with LoRA.\\n\\n**Primary evaluation (OOD generalization):** SimplerEnv Visual Variant Aggregation (randomized backgrounds, textures, lighting, distractors, camera poses) as the PRIMARY metric. LIBERO-Plus (VLA-GSE's robustness benchmark with 7 perturbation dimensions) for systematic robustness analysis.\\n\\n**Secondary evaluation (in-distribution):** LIBERO 4-suite average (note: saturated at ~97% for OpenVLA-OFT; we expect marginal ID gains and focus on OOD).\\n\\n**Diagnostic metrics:** CKA similarity between VLA visual representations and frozen VLM teacher at each finetuning epoch (representation preservation). Attention entropy dynamics over training trajectory (attention collapse prevention). Learned masking rate heatmaps for Adaptive CTM (interpretability: which tokens does the model learn to mask?).\\n\\n**Baselines (comprehensive):** (1) OpenVLA-OFT (no regularization), (2) Don't Blind Your VLA (frozen teacher alignment), (3) Gen-VLA (dual encoder), (4) RS-CL (contrastive state regularization + view cutoff), (5) VLA-GSE (spectral expert decomposition), (6) VLM2VLA (action-as-language), (7) CRL-VLA (asymmetric dual-critic), (8) PatchDropout applied to VLA pipeline (methodological ablation), (9) Standard dropout on visual tokens (ablation).\\n\\n**Key ablations:** (a) Masking placement: pre-projector vs. post-projector vs. post-LLM-embedding; (b) Uniform vs. adaptive masking; (c) Masking schedule: constant vs. cosine annealing vs. linear decay; (d) CTM combined with Don't Blind Your VLA's alignment loss (complementarity test); (e) CTM combined with RS-CL (complementarity test).\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"~250h A100-80GB\",\n      \"gpu_utilization\": \"Low (~30-40%); researcher must integrate CTM into OpenVLA-OFT codebase, implement adaptive masking module, derive and verify theoretical bounds, debug gradient flow through masked tokens, write evaluation pipelines for SimplerEnv and LIBERO-Plus\",\n      \"timeline\": \"3-4 months\",\n      \"team\": \"1-2 researchers (ideally one with theory background for IB/PAC-Bayes derivations)\",\n      \"estimated_gpu_cost\": \"$375-500\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"~350h A100-80GB\",\n      \"gpu_utilization\": \"Moderate (~60-70%); agent queues masking schedule sweeps, placement ablations, and baseline comparisons automatically; human reviews theoretical derivations and approves experimental direction daily\",\n      \"timeline\": \"6-10 weeks\",\n      \"team\": \"1 researcher, ~45min/day for theory review and direction-setting\",\n      \"claude_api_cost\": \"$150-300 (1000-2000 Opus turns for code generation, experiment design, proof-checking, result analysis)\",\n      \"estimated_gpu_cost\": \"$525-600\",\n      \"risk_note\": \"Theoretical derivations (IB bound, PAC-Bayes bound, attention entropy proof) require human verification; agent-generated proofs may contain subtle errors in the VLA-specific adaptation. Integration of adaptive masking module into OpenVLA-OFT's gradient flow requires careful engineering — wrong placement or initialization may cause training instability.\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"~700h A100-80GB (comprehensive ablations: 3 placements × 4 schedules × 3 masking types × 5 baselines × 2 benchmarks, plus complementarity experiments)\",\n      \"gpu_utilization\": \"High (~90%+); agent runs experiments 24/7, immediately queues next configuration based on results\",\n      \"timeline\": \"12-16 days with 8 A100s available\",\n      \"team\": \"0 for experiments (theoretical derivations must be human-verified before submission)\",\n      \"claude_api_cost\": \"$500-800 (4000-6000 Opus turns for full pipeline: code, debug, hyperparameter search, analysis, draft writing)\",\n      \"estimated_gpu_cost\": \"$1050-1200\",\n      \"speed_bottleneck\": \"GPU count; each LIBERO finetuning run takes ~8-12h on 1 A100 with LoRA; SimplerEnv evaluation adds ~2h per configuration. 9 baselines × 2 benchmarks = minimum 18 evaluation runs.\",\n      \"risk_note\": \"Agent may over-explore uniform masking hyperparameters without recognizing that adaptive masking is the key differentiator requiring deeper architectural investigation. Theoretical contributions cannot be fully automated — proofs need human review. Reproducibility of some baselines (RS-CL, VLA-GSE, VLM2VLA) depends on code availability.\"\n    }\n  },\n  \"target_venues\": [\n    \"ICLR 2027 (expected deadline ~September 2026, primary target)\",\n    \"ICRA 2027 (expected deadline ~September 2026, secondary target)\",\n    \"CoRL 2027 (expected deadline ~May 2027, backup)\"\n  ],\n  \"level\": \"solid\",\n  \"key_references\": [\n    \"Information Dropout: Learning Optimal Representations Through Noisy Computation (Achille & Soatto, TPAMI 2018)\",\n    \"Don't Blind Your VLA: Aligning Visual Representations for OOD Generalization (arXiv 2510.25616, 2025)\",\n    \"Contrastive Representation Regularization for Vision-Language-Action Models [RS-CL] (ICLR 2026)\",\n    \"PatchDropout: Economizing Vision Transformers Using Patch Dropout (WACV 2023)\",\n    \"Masked Images Are Counterfactual Samples for Robust Fine-tuning (Xiao et al., CVPR 2023)\",\n    \"DropKey for Vision Transformer (CVPR 2023)\",\n    \"Entropy-Guided Token Dropout [EntroDrop] (arXiv 2512.23422, 2025)\",\n    \"To Sink or Not to Sink: Visual Information Pathways in Large Vision-Language Models (ICLR 2026)\",\n    \"VLA-GSE: Boosting Parameter-Efficient Fine-Tuning in VLA with Generalized and Specialized Experts (arXiv 2605.06175, 2026)\",\n    \"Actions as Language: Fine-Tuning VLMs into VLAs Without Catastrophic Forgetting [VLM2VLA] (ICLR 2026)\",\n    \"CRL-VLA: Continual Vision-Language-Action Learning (arXiv 2602.03445, 2026)\",\n    \"Enhancing Generalization in Vision-Language-Action Models by Preserving Pretrained Representations [Gen-VLA] (arXiv 2509.11417, 2025)\",\n    \"OpenVLA: An Open-Source Vision-Language-Action Model (CoRL 2024)\",\n    \"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success [OpenVLA-OFT] (arXiv 2025)\",\n    \"The Better You Learn The Smarter You Prune [LightVLA] (ICRA 2026)\",\n    \"TraceVLA: Visual Trace Prompting Enhances Spatial-Temporal Awareness (ICLR 2025)\",\n    \"Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning (Gal & Ghahramani, ICML 2016)\",\n    \"Deep Variational Information Bottleneck (Alemi et al., ICLR 2017)\",\n    \"Token Reduction Should Go Beyond Efficiency in Generative Models (arXiv 2505.18227, 2025)\",\n    \"CRAFT: Adapting VLA Models to Contact-rich Manipulation via Force-aware Curriculum Fine-tuning (arXiv 2602.12532, 2026)\",\n    \"Gaze-Regularized Vision-Language-Action Models for Robotic Manipulation (arXiv 2603.23202, 2026)\",\n    \"VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning (arXiv 2025)\",\n    \"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models (2025)\"\n  ],\n  \"description\": \"We propose Counterfactual Token Masking (CTM), a theoretically grounded framework for robust VLA finetuning that addresses representation degradation through implicit causal data augmentation. Our key insight is that robotic demonstration data is inherently low-diversity (same environments repeat across episodes), creating spurious visual correlations that drive the attention migration and representation collapse documented in recent work. CTM stochastically masks projected visual tokens before they enter the LLM backbone, creating implicit counterfactual training samples where background/distractor tokens are absent, forcing the model to ground action predictions in causally relevant visual features. We develop two variants: Uniform CTM with cosine-annealed masking, and Adaptive CTM where a lightweight learned module outputs per-token masking probabilities regularized via an information bottleneck KL penalty. We provide four theoretical contributions: (a) an IB bound showing CTM minimizes representation dependence on spurious input tokens during VLA finetuning; (b) an attention entropy lower bound proving CTM prevents degenerate attention collapse; (c) a PAC-Bayes generalization bound adapted to token-level masking; (d) a causal analysis connecting token masking to counterfactual interventions that break background-action spurious correlations. Our approach is architecture-agnostic, requires minimal additional parameters (~0.1M for adaptive variant), and is complementary to existing methods (frozen-encoder alignment, contrastive regularization). We differentiate from PatchDropout (standard ViT training, not VLA pipeline), RS-CL (representation-level view cutoff, not token-level masking), and the counterfactual samples framework (CAM-guided classification finetuning, not VLA-specific). Using OpenVLA-OFT as the base, we evaluate primarily on SimplerEnv OOD Visual Variant Aggregation and LIBERO-Plus robustness benchmarks, comparing against six concurrent VLA regularization approaches: Don't Blind Your VLA, Gen-VLA, RS-CL, VLA-GSE, VLM2VLA, and CRL-VLA.\",\n  \"project_name\": \"vla_token_mask_reg\",\n  \"source\": \"web_research\"\n}\n\n\n## Previous review history\n### Round 1 review\nVerdict: revise\nIssues: [\"CRITICAL MISSING REFERENCES: (1) RS-CL (ICLR 2026) — directly regularizes VLA representations during training via contrastive loss with robot state supervision, includes 'view cutoff' augmentation that masks entire view features; (2) PatchDropout (WACV 2023) — the direct methodological precedent for random patch dropout during ViT training; (3) 'Masked Images Are Counterfactual Samples' (CVPR 2023) — uses masked patches + feature distillation for robust finetuning, extremely close in spirit; (4) EntroDrop (arXiv 2512.23422) — entropy-guided token dropout during training as regularization; (5) DropKey (CVPR 2023) — attention-level dropout regularization for ViTs; (6) VLA-GSE (arXiv 2605.06175, May 2026) — addresses VLA overfitting via spectral expert decomposition + backbone reversal; (7) VLM2VLA / Actions as Language (ICLR 2026) — prevents catastrophic forgetting in VLA finetuning; (8) CRL-VLA (arXiv 2602.03445) — asymmetric regularization framework for VLA; (9) 'To Sink or Not to Sink' (ICLR 2026) — analyzes attention sinks in VLMs with training-based mitigation; (10) Token Reduction Survey (arXiv 2505.18227) — argues token reduction should go beyond efficiency.\", \"NOVELTY OVERSTATEMENT: The claim 'The connection between Information Dropout and structured token masking during VLA finetuning is entirely unexplored' is too strong. PatchDropout (2023) already showed random patch dropout during ViT training improves performance. LightVLA (ICRA 2026) showed that differentiable token selection during VLA training yields +2.6% success rate, demonstrating implicit regularization from training-time token manipulation. The actual novelty is narrower than claimed.\", \"INSUFFICIENT THEORETICAL DEPTH: The user specifically requested theoretical analysis of WHY token pruning/augmentation enhances VLA generalization. The idea merely references Information Dropout (2017) without: (a) formally deriving the IB bound for the VLA setting with token masking; (b) proving why token masking prevents attention sink under specific conditions; (c) connecting to PAC-Bayes generalization bounds for dropout-regularized models; (d) analyzing the invariance properties induced by masking (e.g., occlusion robustness, background invariance) via group theory or causal reasoning; (e) the CVPR 2023 'Masked Images as Counterfactual Samples' paper provides a causal/counterfactual framework that is directly applicable but not cited.\", \"BASELINE SATURATION: LIBERO in-distribution success rate is already 97.1% with OpenVLA-OFT. Demonstrating statistically significant improvement on in-distribution tasks is nearly impossible. The evaluation plan should focus almost entirely on OOD generalization (SimplerEnv variants, unseen objects/backgrounds) rather than in-distribution metrics.\", \"VENUE TIMING: CoRL 2026 abstract deadline is May 26, 2026 (13 days away) with paper deadline May 28. Starting a new project to meet this deadline is infeasible. This should be removed as a target venue or the timeline must be substantially revised.\", \"COMPETITIVE POSITIONING INADEQUATE: The VLA representation preservation space now has at least 6 concurrent approaches: (1) frozen-encoder alignment (Don't Blind Your VLA), (2) dual-encoder co-training (Gen-VLA), (3) contrastive state regularization (RS-CL), (4) spectral expert decomposition + backbone reversal (VLA-GSE), (5) action-as-language representation (VLM2VLA), (6) asymmetric dual-critic regularization (CRL-VLA). The proposed method must demonstrate clear advantages over ALL of these, not just Don't Blind Your VLA and Gen-VLA.\", \"ADAPTIVE VARIANT UNDERSPECIFIED: The 'learned per-token log-variance' adaptive masking variant is the most theoretically interesting component but is insufficiently detailed. How does the per-token variance interact with LoRA fine-tuning? Does it add trainable parameters to the frozen ViT? How is the KL penalty weighted against the action prediction loss? Without these details, the theoretical contribution remains vague.\"]\nFeedback: The core direction — training-time token masking as VLA regularization — has merit, but the idea needs substantial revision in three areas:\n\n**1. NOVELTY RESCUE (highest priority):** You must acknowledge and differentiate from PatchDropout (WACV 2023), RS-CL (ICLR 2026), and 'Masked Images Are Counterfactual Samples' (CVPR 2023). PatchDropout is random patch dropout during ViT training — your method applied to VLAs needs to show what is fundamentally different about the VLA setting. RS-CL already regularizes VLA representations at ICLR 2026 — position your approach as complementary or superior. The 'counterfactual samples' paper provides a causal framework for masked-image finetuning that you should either adopt or differentiate from. Consider: what makes token masking *in VLAs specifically* different from token masking in standard ViTs?\n\n**2. THEORETICAL DEPTH (user requirement):** The user explicitly requested theoretical analysis of WHY token masking enhances VLA generalization. Currently you cite Information Dropout without derivation. You need: (a) A formal IB bound showing that stochastic token masking during VLA finetuning minimizes I(Z;X|Y) where Z is the representation, X is the input, Y is the action — derive this for the specific VLA architecture with frozen ViT + projector + LLM; (b) A formal connection between token masking and attention entropy — prove that masking prevents attention collapse to sink tokens under certain conditions on the masking probability; (c) Analysis of the invariance properties: token masking creates implicit data augmentation equivalent to partial occlusion — connect this to the OOD scenarios (background change, distractor objects) via causal invariance principles; (d) Consider the PAC-Bayes perspective: dropout-regularized models have tighter generalization bounds (Gal & Ghahramani 2016) — adapt this analysis to token-level masking.\n\n**3. EXPERIMENTAL REPOSITIONING:** Drop LIBERO in-distribution as a primary metric (it's saturated at 97.1%). Focus on: (a) SimplerEnv OOD visual variants as the primary evaluation; (b) CKA degradation curves comparing masking vs. no-masking during finetuning trajectory; (c) Attention entropy dynamics visualization; (d) Add RS-CL, VLA-GSE, and VLM2VLA as baselines beyond Don't Blind Your VLA and Gen-VLA; (e) Consider real-robot transfer experiments if feasible.\n\n**4. VENUE:** Remove CoRL 2026 (deadline in 13 days). ICLR 2027 (~September 2026) is realistic. Also consider RSS 2026 or ICRA 2027.\n\n**5. MISSING KEY INSIGHT:** The most interesting theoretical angle you're not exploiting: VLA finetuning suffers from attention sink specifically because robotic demonstration data is low-diversity (same backgrounds, same table, same lighting). Token masking forces the model to solve the task even when 'easy' background tokens are absent, creating implicit counterfactual training samples. This connects directly to the CVPR 2023 counterfactual framework and gives a much stronger theoretical story than generic IB regularization.\n\n\n## Output format\nOutput ONLY a JSON object:\n{\n  \"verdict\": \"pass | revise | fail\",\n  \"scores\": {\n    \"novelty\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"feasibility\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"clarity\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"impact\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"}\n  },\n  \"issues\": [\"specific issue 1\", \"specific issue 2\", ...],\n  \"feedback\": \"Actionable feedback for the generator (if verdict=revise)\",\n  \"reason\": \"One-line summary of verdict rationale\"\n}\n\nRules:\n- \"pass\": idea is sound AND high quality — avg score >= 4.0, no critical issues\n- \"revise\": fixable issues OR scores below threshold — provide specific feedback\n- \"fail\": fundamental flaw (e.g., gap doesn't exist, approach provably wrong, or scores remain low after multiple revisions)\n- Threshold is HIGH (4.0/5.0): agent scores tend to be inflated, so only truly outstanding ideas should pass. An avg of 3.5 is NOT enough.\n- Round 10 only: if still \"revise\", you MUST choose \"pass\" or \"fail\"."
}
```

---

### Runtime record

_source line 2 · 2026-05-13T04:42:06.517Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-13T04:42:06.517Z",
  "sessionId": "38eec20f-28d6-4706-b24b-8f0ea53acfb9"
}
```

---

## Round 1

56 recorded events

### User

_source line 3 · 2026-05-13T04:42:06.555Z_

You are a strict ML research reviewer conducting adversarial review.

**Today's date: 2026-05-13 (UTC).**

Your job: independently verify this idea's claims via WebSearch, then issue a verdict.

## User requirements
The user asked for: **VLA中的token裁剪/增强能否提升VLA模型的泛化性（多从理论角度分析为何能增强）**
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
4. **Venue validity**: Are target_venues' submission deadlines after 2026-05-13?
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
  "title": "Counterfactual Token Masking: A Theoretically Grounded Framework for Robust VLA Finetuning via Implicit Causal Data Augmentation",
  "core_problem": "VLA finetuning on robotic demonstration data suffers from representation degradation (attention migration to background tokens, representation collapse, domain-specific forgetting) primarily because demonstration data is inherently low-diversity — the same table, background, lighting, and camera pose repeat across thousands of episodes. Existing mitigation approaches (frozen-encoder alignment, dual encoders, contrastive state regularization, spectral expert decomposition, action-as-language reformulation) each address specific symptoms but none exploit the fundamental causal structure of the problem: spurious visual correlations in low-diversity robot data drive representation collapse, and these correlations can be broken through principled counterfactual interventions on visual tokens during training.",
  "opportunity": "The convergence of three independent research lines creates a unique theoretical opportunity: (1) 'Masked Images Are Counterfactual Samples' (Xiao et al., CVPR 2023) established that masking image patches and refilling them constitutes a counterfactual intervention that breaks spurious correlations in finetuning, but applied this only to classification with CAM-guided masking; (2) Information Dropout (Achille & Soatto, TPAMI 2018) proved that multiplicative noise on representations is equivalent to IB regularization, learning representations invariant to nuisance factors; (3) 'Don't Blind Your VLA' (arXiv 2510.25616) and RS-CL (ICLR 2026) independently documented that VLA finetuning destroys pretrained visual representations, with the former showing attention migration from task-relevant to background tokens and the latter showing that representation-level regularization (view cutoff, contrastive loss) yields large gains. The gap is that no existing work synthesizes these insights: applying counterfactual token-level masking specifically to the VLA finetuning setting, with formal IB-theoretic and causal justification for why this prevents the documented pathologies. PatchDropout (WACV 2023) showed random patch dropout improves ViT training, but in standard training — not the unique frozen-ViT → projector → LLM pipeline of VLAs where the regularization target and gradient dynamics differ fundamentally. LightVLA (ICRA 2026) showed training-time differentiable token selection improves VLA performance (+2.6%), providing empirical evidence that training-time token manipulation benefits VLAs — but framed as efficiency, without theoretical analysis of the regularization effect.",
  "landscape": "The VLA representation preservation space now contains at least six concurrent approaches: (1) Frozen-encoder alignment: 'Don't Blind Your VLA' (arXiv 2510.25616) pulls VLA hidden states toward a frozen teacher's features via cosine similarity loss, directly mitigating attention sink. (2) Dual-encoder co-training: Gen-VLA (arXiv 2509.11417) uses separate encoders for action prediction and VL understanding with co-training to prevent forgetting. (3) Contrastive state regularization: RS-CL (ICLR 2026) shapes representations via InfoNCE weighted by robot proprioceptive state distances, with 'view cutoff' augmentation that masks entire camera view features (representation-level, not token-level). (4) Spectral expert decomposition: VLA-GSE (arXiv 2605.06175) initializes generalized/specialized experts from SVD of frozen backbone, addressing overfitting via parameter-efficient adaptation. (5) Action-as-language: VLM2VLA (ICLR 2026) represents actions in natural language to avoid distribution mismatch. (6) Asymmetric dual-critic regularization: CRL-VLA (arXiv 2602.03445) uses frozen/trainable critic pair for continual learning. In the broader token masking/dropout literature: PatchDropout (WACV 2023) randomly drops input patches during ViT training for efficiency and implicit regularization. DropKey (CVPR 2023) applies dropout to attention keys before softmax in ViTs. EntroDrop (arXiv 2512.23422) uses entropy-guided token dropout for LLM training. 'Masked Images Are Counterfactual Samples' (CVPR 2023) uses CAM-guided masked patches with feature distillation for robust classification finetuning. 'To Sink or Not to Sink' (ICLR 2026) shows that ViT attention sinks in VLMs actually encode high-level semantic concepts, challenging the view that sinks are purely pathological — the nuance being that sinks become harmful specifically when VLA finetuning causes attention to MIGRATE from task-relevant to background tokens, not because sinks themselves are inherently bad. The Token Reduction Survey (arXiv 2505.18227) argues token reduction should go beyond efficiency in generative models. CRAFT (arXiv 2602.12532) applies VIB for force modality integration. Gaze-Regularized VLA (arXiv 2603.23202) regularizes attention via KL to human gaze maps (requires external data). TraceVLA (ICLR 2025) uses visual trace prompt dropout but only drops/retains the trace overlay. The specific gap we target: no existing work provides a formal theoretical framework connecting token-level masking during VLA finetuning to (a) information-bottleneck regularization adapted to the frozen-ViT → projector → LLM architecture, (b) counterfactual data augmentation that breaks the spurious visual correlations inherent in low-diversity robot demonstration data, and (c) attention entropy preservation guarantees.",
  "approach": "We propose Counterfactual Token Masking (CTM), a theoretically grounded framework for robust VLA finetuning that operates by stochastically masking visual patch tokens after the ViT projector and before the LLM backbone. The framework has three components:\n\n**Component 1: Uniform CTM (baseline).** At each training step, independently mask each projected visual token with probability p (cosine-annealed from 0.25→0.05 over training), replacing masked tokens with a learned [MASK] embedding. This forces the LLM backbone to predict actions even when 'easy' background tokens (which dominate low-diversity robot data) are absent, creating implicit counterfactual training samples. Placement after the projector is critical: pre-projector masking would save compute but cannot regularize the projector→LLM interface where representation collapse concentrates; post-LLM-embedding masking would disrupt the LLM's pretrained token interactions.\n\n**Component 2: Adaptive CTM (main contribution).** Replace uniform masking with learned per-token masking rates via the Information Dropout formulation. A lightweight module (single-layer MLP, ~0.1M parameters) takes each projected visual token and outputs a per-token log-variance α_i. Token i is masked with probability σ(α_i), where σ is the sigmoid function. A KL penalty term β·Σ_i KL(Bernoulli(σ(α_i)) || Bernoulli(p_prior)) is added to the action prediction loss, where p_prior is the base masking rate (0.15). β is warmed up from 0→1 over the first 20% of training to allow the model to first learn action prediction before the IB constraint tightens. This module operates entirely on the projector's output and is compatible with LoRA finetuning of the LLM backbone — it does not modify the frozen ViT.\n\n**Component 3: Theoretical Analysis.** We provide: (a) A formal derivation of the IB bound for VLA finetuning with token masking: following Achille & Soatto (2018), we show that stochastic token masking minimizes an upper bound on I(Z_v; X_v | A), where Z_v is the visual representation entering the LLM, X_v is the raw visual input, and A is the target action. This bound decomposes into the action prediction loss plus a complexity term penalizing representation dependence on individual input tokens. (b) A proof that token masking with probability p > 0 lower-bounds the attention entropy of the LLM's first layer over visual tokens by H ≥ -log(1-p) - ε under mild conditions on the attention temperature, preventing the degenerate attention collapse documented in 'Don't Blind Your VLA'. This reconciles with 'To Sink or Not to Sink' (ICLR 2026): attention sinks are beneficial for encoding visual summaries, but finetuning-induced migration of attention mass to background sinks is harmful — CTM prevents migration without eliminating sinks. (c) A PAC-Bayes generalization bound adapted from Gal & Ghahramani (2016): treating token masking as a stochastic posterior over sub-networks, we derive a tighter generalization bound for the VLA that decreases with the masking rate, formally justifying why CTM improves OOD transfer. (d) A causal analysis connecting to the counterfactual framework of Xiao et al. (CVPR 2023): masking tokens from low-diversity background regions constitutes a do-calculus intervention do(X_bg = ∅) that identifies the causal effect of task-relevant visual features on action prediction, breaking spurious correlations between background appearance and action labels.\n\n**Base model:** OpenVLA-OFT with LoRA.\n\n**Primary evaluation (OOD generalization):** SimplerEnv Visual Variant Aggregation (randomized backgrounds, textures, lighting, distractors, camera poses) as the PRIMARY metric. LIBERO-Plus (VLA-GSE's robustness benchmark with 7 perturbation dimensions) for systematic robustness analysis.\n\n**Secondary evaluation (in-distribution):** LIBERO 4-suite average (note: saturated at ~97% for OpenVLA-OFT; we expect marginal ID gains and focus on OOD).\n\n**Diagnostic metrics:** CKA similarity between VLA visual representations and frozen VLM teacher at each finetuning epoch (representation preservation). Attention entropy dynamics over training trajectory (attention collapse prevention). Learned masking rate heatmaps for Adaptive CTM (interpretability: which tokens does the model learn to mask?).\n\n**Baselines (comprehensive):** (1) OpenVLA-OFT (no regularization), (2) Don't Blind Your VLA (frozen teacher alignment), (3) Gen-VLA (dual encoder), (4) RS-CL (contrastive state regularization + view cutoff), (5) VLA-GSE (spectral expert decomposition), (6) VLM2VLA (action-as-language), (7) CRL-VLA (asymmetric dual-critic), (8) PatchDropout applied to VLA pipeline (methodological ablation), (9) Standard dropout on visual tokens (ablation).\n\n**Key ablations:** (a) Masking placement: pre-projector vs. post-projector vs. post-LLM-embedding; (b) Uniform vs. adaptive masking; (c) Masking schedule: constant vs. cosine annealing vs. linear decay; (d) CTM combined with Don't Blind Your VLA's alignment loss (complementarity test); (e) CTM combined with RS-CL (complementarity test).",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "~250h A100-80GB",
      "gpu_utilization": "Low (~30-40%); researcher must integrate CTM into OpenVLA-OFT codebase, implement adaptive masking module, derive and verify theoretical bounds, debug gradient flow through masked tokens, write evaluation pipelines for SimplerEnv and LIBERO-Plus",
      "timeline": "3-4 months",
      "team": "1-2 researchers (ideally one with theory background for IB/PAC-Bayes derivations)",
      "estimated_gpu_cost": "$375-500"
    },
    "human_in_loop": {
      "gpu_hours": "~350h A100-80GB",
      "gpu_utilization": "Moderate (~60-70%); agent queues masking schedule sweeps, placement ablations, and baseline comparisons automatically; human reviews theoretical derivations and approves experimental direction daily",
      "timeline": "6-10 weeks",
      "team": "1 researcher, ~45min/day for theory review and direction-setting",
      "claude_api_cost": "$150-300 (1000-2000 Opus turns for code generation, experiment design, proof-checking, result analysis)",
      "estimated_gpu_cost": "$525-600",
      "risk_note": "Theoretical derivations (IB bound, PAC-Bayes bound, attention entropy proof) require human verification; agent-generated proofs may contain subtle errors in the VLA-specific adaptation. Integration of adaptive masking module into OpenVLA-OFT's gradient flow requires careful engineering — wrong placement or initialization may cause training instability."
    },
    "auto_research": {
      "gpu_hours": "~700h A100-80GB (comprehensive ablations: 3 placements × 4 schedules × 3 masking types × 5 baselines × 2 benchmarks, plus complementarity experiments)",
      "gpu_utilization": "High (~90%+); agent runs experiments 24/7, immediately queues next configuration based on results",
      "timeline": "12-16 days with 8 A100s available",
      "team": "0 for experiments (theoretical derivations must be human-verified before submission)",
      "claude_api_cost": "$500-800 (4000-6000 Opus turns for full pipeline: code, debug, hyperparameter search, analysis, draft writing)",
      "estimated_gpu_cost": "$1050-1200",
      "speed_bottleneck": "GPU count; each LIBERO finetuning run takes ~8-12h on 1 A100 with LoRA; SimplerEnv evaluation adds ~2h per configuration. 9 baselines × 2 benchmarks = minimum 18 evaluation runs.",
      "risk_note": "Agent may over-explore uniform masking hyperparameters without recognizing that adaptive masking is the key differentiator requiring deeper architectural investigation. Theoretical contributions cannot be fully automated — proofs need human review. Reproducibility of some baselines (RS-CL, VLA-GSE, VLM2VLA) depends on code availability."
    }
  },
  "target_venues": [
    "ICLR 2027 (expected deadline ~September 2026, primary target)",
    "ICRA 2027 (expected deadline ~September 2026, secondary target)",
    "CoRL 2027 (expected deadline ~May 2027, backup)"
  ],
  "level": "solid",
  "key_references": [
    "Information Dropout: Learning Optimal Representations Through Noisy Computation (Achille & Soatto, TPAMI 2018)",
    "Don't Blind Your VLA: Aligning Visual Representations for OOD Generalization (arXiv 2510.25616, 2025)",
    "Contrastive Representation Regularization for Vision-Language-Action Models [RS-CL] (ICLR 2026)",
    "PatchDropout: Economizing Vision Transformers Using Patch Dropout (WACV 2023)",
    "Masked Images Are Counterfactual Samples for Robust Fine-tuning (Xiao et al., CVPR 2023)",
    "DropKey for Vision Transformer (CVPR 2023)",
    "Entropy-Guided Token Dropout [EntroDrop] (arXiv 2512.23422, 2025)",
    "To Sink or Not to Sink: Visual Information Pathways in Large Vision-Language Models (ICLR 2026)",
    "VLA-GSE: Boosting Parameter-Efficient Fine-Tuning in VLA with Generalized and Specialized Experts (arXiv 2605.06175, 2026)",
    "Actions as Language: Fine-Tuning VLMs into VLAs Without Catastrophic Forgetting [VLM2VLA] (ICLR 2026)",
    "CRL-VLA: Continual Vision-Language-Action Learning (arXiv 2602.03445, 2026)",
    "Enhancing Generalization in Vision-Language-Action Models by Preserving Pretrained Representations [Gen-VLA] (arXiv 2509.11417, 2025)",
    "OpenVLA: An Open-Source Vision-Language-Action Model (CoRL 2024)",
    "Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success [OpenVLA-OFT] (arXiv 2025)",
    "The Better You Learn The Smarter You Prune [LightVLA] (ICRA 2026)",
    "TraceVLA: Visual Trace Prompting Enhances Spatial-Temporal Awareness (ICLR 2025)",
    "Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning (Gal & Ghahramani, ICML 2016)",
    "Deep Variational Information Bottleneck (Alemi et al., ICLR 2017)",
    "Token Reduction Should Go Beyond Efficiency in Generative Models (arXiv 2505.18227, 2025)",
    "CRAFT: Adapting VLA Models to Contact-rich Manipulation via Force-aware Curriculum Fine-tuning (arXiv 2602.12532, 2026)",
    "Gaze-Regularized Vision-Language-Action Models for Robotic Manipulation (arXiv 2603.23202, 2026)",
    "VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning (arXiv 2025)",
    "LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models (2025)"
  ],
  "description": "We propose Counterfactual Token Masking (CTM), a theoretically grounded framework for robust VLA finetuning that addresses representation degradation through implicit causal data augmentation. Our key insight is that robotic demonstration data is inherently low-diversity (same environments repeat across episodes), creating spurious visual correlations that drive the attention migration and representation collapse documented in recent work. CTM stochastically masks projected visual tokens before they enter the LLM backbone, creating implicit counterfactual training samples where background/distractor tokens are absent, forcing the model to ground action predictions in causally relevant visual features. We develop two variants: Uniform CTM with cosine-annealed masking, and Adaptive CTM where a lightweight learned module outputs per-token masking probabilities regularized via an information bottleneck KL penalty. We provide four theoretical contributions: (a) an IB bound showing CTM minimizes representation dependence on spurious input tokens during VLA finetuning; (b) an attention entropy lower bound proving CTM prevents degenerate attention collapse; (c) a PAC-Bayes generalization bound adapted to token-level masking; (d) a causal analysis connecting token masking to counterfactual interventions that break background-action spurious correlations. Our approach is architecture-agnostic, requires minimal additional parameters (~0.1M for adaptive variant), and is complementary to existing methods (frozen-encoder alignment, contrastive regularization). We differentiate from PatchDropout (standard ViT training, not VLA pipeline), RS-CL (representation-level view cutoff, not token-level masking), and the counterfactual samples framework (CAM-guided classification finetuning, not VLA-specific). Using OpenVLA-OFT as the base, we evaluate primarily on SimplerEnv OOD Visual Variant Aggregation and LIBERO-Plus robustness benchmarks, comparing against six concurrent VLA regularization approaches: Don't Blind Your VLA, Gen-VLA, RS-CL, VLA-GSE, VLM2VLA, and CRL-VLA.",
  "project_name": "vla_token_mask_reg",
  "source": "web_research"
}


## Previous review history
### Round 1 review
Verdict: revise
Issues: ["CRITICAL MISSING REFERENCES: (1) RS-CL (ICLR 2026) — directly regularizes VLA representations during training via contrastive loss with robot state supervision, includes 'view cutoff' augmentation that masks entire view features; (2) PatchDropout (WACV 2023) — the direct methodological precedent for random patch dropout during ViT training; (3) 'Masked Images Are Counterfactual Samples' (CVPR 2023) — uses masked patches + feature distillation for robust finetuning, extremely close in spirit; (4) EntroDrop (arXiv 2512.23422) — entropy-guided token dropout during training as regularization; (5) DropKey (CVPR 2023) — attention-level dropout regularization for ViTs; (6) VLA-GSE (arXiv 2605.06175, May 2026) — addresses VLA overfitting via spectral expert decomposition + backbone reversal; (7) VLM2VLA / Actions as Language (ICLR 2026) — prevents catastrophic forgetting in VLA finetuning; (8) CRL-VLA (arXiv 2602.03445) — asymmetric regularization framework for VLA; (9) 'To Sink or Not to Sink' (ICLR 2026) — analyzes attention sinks in VLMs with training-based mitigation; (10) Token Reduction Survey (arXiv 2505.18227) — argues token reduction should go beyond efficiency.", "NOVELTY OVERSTATEMENT: The claim 'The connection between Information Dropout and structured token masking during VLA finetuning is entirely unexplored' is too strong. PatchDropout (2023) already showed random patch dropout during ViT training improves performance. LightVLA (ICRA 2026) showed that differentiable token selection during VLA training yields +2.6% success rate, demonstrating implicit regularization from training-time token manipulation. The actual novelty is narrower than claimed.", "INSUFFICIENT THEORETICAL DEPTH: The user specifically requested theoretical analysis of WHY token pruning/augmentation enhances VLA generalization. The idea merely references Information Dropout (2017) without: (a) formally deriving the IB bound for the VLA setting with token masking; (b) proving why token masking prevents attention sink under specific conditions; (c) connecting to PAC-Bayes generalization bounds for dropout-regularized models; (d) analyzing the invariance properties induced by masking (e.g., occlusion robustness, background invariance) via group theory or causal reasoning; (e) the CVPR 2023 'Masked Images as Counterfactual Samples' paper provides a causal/counterfactual framework that is directly applicable but not cited.", "BASELINE SATURATION: LIBERO in-distribution success rate is already 97.1% with OpenVLA-OFT. Demonstrating statistically significant improvement on in-distribution tasks is nearly impossible. The evaluation plan should focus almost entirely on OOD generalization (SimplerEnv variants, unseen objects/backgrounds) rather than in-distribution metrics.", "VENUE TIMING: CoRL 2026 abstract deadline is May 26, 2026 (13 days away) with paper deadline May 28. Starting a new project to meet this deadline is infeasible. This should be removed as a target venue or the timeline must be substantially revised.", "COMPETITIVE POSITIONING INADEQUATE: The VLA representation preservation space now has at least 6 concurrent approaches: (1) frozen-encoder alignment (Don't Blind Your VLA), (2) dual-encoder co-training (Gen-VLA), (3) contrastive state regularization (RS-CL), (4) spectral expert decomposition + backbone reversal (VLA-GSE), (5) action-as-language representation (VLM2VLA), (6) asymmetric dual-critic regularization (CRL-VLA). The proposed method must demonstrate clear advantages over ALL of these, not just Don't Blind Your VLA and Gen-VLA.", "ADAPTIVE VARIANT UNDERSPECIFIED: The 'learned per-token log-variance' adaptive masking variant is the most theoretically interesting component but is insufficiently detailed. How does the per-token variance interact with LoRA fine-tuning? Does it add trainable parameters to the frozen ViT? How is the KL penalty weighted against the action prediction loss? Without these details, the theoretical contribution remains vague."]
Feedback: The core direction — training-time token masking as VLA regularization — has merit, but the idea needs substantial revision in three areas:

**1. NOVELTY RESCUE (highest priority):** You must acknowledge and differentiate from PatchDropout (WACV 2023), RS-CL (ICLR 2026), and 'Masked Images Are Counterfactual Samples' (CVPR 2023). PatchDropout is random patch dropout during ViT training — your method applied to VLAs needs to show what is fundamentally different about the VLA setting. RS-CL already regularizes VLA representations at ICLR 2026 — position your approach as complementary or superior. The 'counterfactual samples' paper provides a causal framework for masked-image finetuning that you should either adopt or differentiate from. Consider: what makes token masking *in VLAs specifically* different from token masking in standard ViTs?

**2. THEORETICAL DEPTH (user requirement):** The user explicitly requested theoretical analysis of WHY token masking enhances VLA generalization. Currently you cite Information Dropout without derivation. You need: (a) A formal IB bound showing that stochastic token masking during VLA finetuning minimizes I(Z;X|Y) where Z is the representation, X is the input, Y is the action — derive this for the specific VLA architecture with frozen ViT + projector + LLM; (b) A formal connection between token masking and attention entropy — prove that masking prevents attention collapse to sink tokens under certain conditions on the masking probability; (c) Analysis of the invariance properties: token masking creates implicit data augmentation equivalent to partial occlusion — connect this to the OOD scenarios (background change, distractor objects) via causal invariance principles; (d) Consider the PAC-Bayes perspective: dropout-regularized models have tighter generalization bounds (Gal & Ghahramani 2016) — adapt this analysis to token-level masking.

**3. EXPERIMENTAL REPOSITIONING:** Drop LIBERO in-distribution as a primary metric (it's saturated at 97.1%). Focus on: (a) SimplerEnv OOD visual variants as the primary evaluation; (b) CKA degradation curves comparing masking vs. no-masking during finetuning trajectory; (c) Attention entropy dynamics visualization; (d) Add RS-CL, VLA-GSE, and VLM2VLA as baselines beyond Don't Blind Your VLA and Gen-VLA; (e) Consider real-robot transfer experiments if feasible.

**4. VENUE:** Remove CoRL 2026 (deadline in 13 days). ICLR 2027 (~September 2026) is realistic. Also consider RSS 2026 or ICRA 2027.

**5. MISSING KEY INSIGHT:** The most interesting theoretical angle you're not exploiting: VLA finetuning suffers from attention sink specifically because robotic demonstration data is low-diversity (same backgrounds, same table, same lighting). Token masking forces the model to solve the task even when 'easy' background tokens are absent, creating implicit counterfactual training samples. This connects directly to the CVPR 2023 counterfactual framework and gives a much stronger theoretical story than generic IB regularization.


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
  "promptId": "251a69dd-0148-46cf-91d6-c922d95174a8",
  "type": "user",
  "uuid": "a62cc102-4cb1-4812-a34e-dfae52188c53",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "38eec20f-28d6-4706-b24b-8f0ea53acfb9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-13T04:42:06.552Z_

```json
{
  "parentUuid": "a62cc102-4cb1-4812-a34e-dfae52188c53",
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
  "uuid": "babbe5c6-fc14-4f21-b01c-894f18f12a99",
  "timestamp": "2026-05-13T04:42:06.552Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "38eec20f-28d6-4706-b24b-8f0ea53acfb9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-13T04:42:06.553Z_

```json
{
  "parentUuid": "babbe5c6-fc14-4f21-b01c-894f18f12a99",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "ba665a84-2efd-4a18-aaca-ea1be5e6238f",
  "timestamp": "2026-05-13T04:42:06.553Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "38eec20f-28d6-4706-b24b-8f0ea53acfb9",
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
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-13 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "ba665a84-2efd-4a18-aaca-ea1be5e6238f",
  "sessionId": "38eec20f-28d6-4706-b24b-8f0ea53acfb9"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Review VLA token masking robustness via theory",
  "sessionId": "38eec20f-28d6-4706-b24b-8f0ea53acfb9"
}
```

---

### Assistant

_source line 8 · 2026-05-13T04:42:11.566Z_

<details><summary>Logged reasoning block</summary>

```text
Let me carefully review this idea about Counterfactual Token Masking (CTM) for VLA finetuning. This is round 2/10, so the generator has had a chance to revise based on round 1 feedback. Let me independently verify the claims and assess the quality.

Let me start by searching for the key references and competitive landscape.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ba665a84-2efd-4a18-aaca-ea1be5e6238f",
  "isSidechain": false,
  "requestId": "req_011CayxLmWqE7agU8DiXKZGQ",
  "type": "assistant",
  "uuid": "0e09d08c-5b9b-4613-9775-67c7e6eb8ed7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "38eec20f-28d6-4706-b24b-8f0ea53acfb9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015JFpBe6UQkgR1SAb8wDJbk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15543,
      "cache_read_input_tokens": 11841,
      "output_tokens": 1966,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15543,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1966,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 15543,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15543
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

_source line 9 · 2026-05-13T04:42:12.588Z_

I'll conduct a thorough independent review of this revised idea. Let me start by verifying key claims, checking references, and searching for competitive/concurrent work.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0e09d08c-5b9b-4613-9775-67c7e6eb8ed7",
  "isSidechain": false,
  "requestId": "req_011CayxLmWqE7agU8DiXKZGQ",
  "type": "assistant",
  "uuid": "9e03bc95-fadb-4d3c-afa0-294820c699e0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "38eec20f-28d6-4706-b24b-8f0ea53acfb9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015JFpBe6UQkgR1SAb8wDJbk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15543,
      "cache_read_input_tokens": 11841,
      "output_tokens": 1966,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15543,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1966,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 15543,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15543
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

_source line 10 · 2026-05-13T04:42:22.008Z_

<details open><summary>🔧 Tool call — Agent · `toolu_014E9AZhur474ywR1JzdYTYh`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Verify VLA SOTA and key references",
  "prompt": "You are helping me review an ML research idea. I need you to search for and verify the following claims and references. For each search, use WebSearch and then WebFetch on the most relevant results.\n\n1. **Verify \"Don't Blind Your VLA\" (arXiv 2510.25616)**: Search for this paper, confirm it exists, and check its main claims about attention migration and representation collapse during VLA finetuning.\n\n2. **Verify RS-CL (ICLR 2026)**: Search for \"Contrastive Representation Regularization Vision-Language-Action ICLR 2026\" and confirm this paper exists at ICLR 2026 with the claimed \"view cutoff\" augmentation.\n\n3. **Verify VLA-GSE (arXiv 2605.06175)**: Search for this paper about spectral expert decomposition for VLA. Note: arXiv 2605 means May 2026 — verify if this actually exists.\n\n4. **Verify \"Masked Images Are Counterfactual Samples\" (CVPR 2023)**: Search for this paper by Xiao et al. and confirm its claims about masked patches as counterfactual interventions.\n\n5. **Verify PatchDropout (WACV 2023)**: Search for \"PatchDropout Economizing Vision Transformers\" and confirm it exists.\n\n6. **Verify LightVLA (ICRA 2026)**: Search for \"LightVLA token pruning ICRA 2026\" and confirm the claimed +2.6% success rate from differentiable token selection.\n\n7. **Search for OpenVLA-OFT**: Verify the claimed 97% LIBERO success rate and current SOTA status.\n\n8. **Verify \"To Sink or Not to Sink\" (ICLR 2026)**: Search for this paper about attention sinks in VLMs.\n\nFor each paper, report: (a) whether it exists, (b) its actual venue/year, (c) whether the claims made about it in the idea are accurate. Use WebSearch first, then WebFetch on key results."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9e03bc95-fadb-4d3c-afa0-294820c699e0",
  "isSidechain": false,
  "requestId": "req_011CayxLmWqE7agU8DiXKZGQ",
  "type": "assistant",
  "uuid": "33d9e667-7ba1-4a44-8a09-b37dae818479",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "38eec20f-28d6-4706-b24b-8f0ea53acfb9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015JFpBe6UQkgR1SAb8wDJbk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15543,
      "cache_read_input_tokens": 11841,
      "output_tokens": 1966,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15543,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1966,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 15543,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15543
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

_source line 11 · 2026-05-13T04:42:32.380Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01Hgt3XVkc6ht4zBtXCXYEm3`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Search for competitive/concurrent VLA work",
  "prompt": "You are helping me review an ML research idea about \"token masking as regularization during VLA (Vision-Language-Action) finetuning.\" I need you to search for competitive and concurrent work that the idea may have missed. Use WebSearch extensively.\n\nSearch for the following:\n\n1. **Token masking/dropout in VLAs**: Search \"token masking VLA 2025 2026\", \"visual token dropout robot learning\", \"token pruning VLA generalization\"\n\n2. **VLA robustness/generalization recent work**: Search \"VLA generalization out-of-distribution 2026\", \"vision language action robust finetuning 2026\"\n\n3. **Information bottleneck in robotics/VLA**: Search \"information bottleneck robot learning\", \"information bottleneck VLA\", \"IB regularization vision language action\"\n\n4. **VLA-Pruner**: Search for \"VLA-Pruner temporal visual token pruning\" — the idea mentions this but doesn't detail it. Check if it's a close competitor.\n\n5. **LIBERO-Plus benchmark**: Search \"LIBERO-Plus robustness benchmark VLA\" to verify this exists.\n\n6. **SimplerEnv visual variants**: Search \"SimplerEnv visual variant aggregation VLA evaluation\" to verify this benchmark exists and is standard.\n\n7. **CRL-VLA (arXiv 2602.03445)**: Search for this continual learning VLA paper.\n\n8. **VLM2VLA / Actions as Language (ICLR 2026)**: Verify this exists.\n\n9. **Gen-VLA (arXiv 2509.11417)**: Verify this exists.\n\n10. **Recent arXiv (Feb-May 2026) on VLA regularization**: Search \"VLA regularization arXiv 2026\", \"vision language action model finetuning 2026\" to find any very recent concurrent work.\n\nFor each search, report what you found, whether the papers exist, and whether any of them are close competitors to the proposed \"Counterfactual Token Masking\" idea. Use WebSearch and WebFetch on the most important results."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "33d9e667-7ba1-4a44-8a09-b37dae818479",
  "isSidechain": false,
  "requestId": "req_011CayxLmWqE7agU8DiXKZGQ",
  "type": "assistant",
  "uuid": "c5537a78-4abc-4e7f-94f0-b2ba1d274af4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "38eec20f-28d6-4706-b24b-8f0ea53acfb9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015JFpBe6UQkgR1SAb8wDJbk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15543,
      "cache_read_input_tokens": 11841,
      "output_tokens": 1966,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15543,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1966,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 15543,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15543
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

_source line 12 · 2026-05-13T04:42:43.016Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01DKP7jci1dqWvDj7bMyirYb`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Verify theoretical claims and IB framework",
  "prompt": "You are helping me review an ML research idea that proposes using token masking during VLA (Vision-Language-Action) finetuning, with theoretical justification from Information Bottleneck theory. I need you to verify several theoretical claims.\n\n1. **Information Dropout (Achille & Soatto, TPAMI 2018)**: Search for this paper and verify the claim that \"multiplicative noise on representations is equivalent to IB regularization.\" Use WebSearch and WebFetch to read the abstract and key results.\n\n2. **Gal & Ghahramani (ICML 2016) \"Dropout as a Bayesian Approximation\"**: Verify this paper exists and its relevance to PAC-Bayes bounds for dropout. The idea claims to adapt PAC-Bayes bounds from this work to token-level masking.\n\n3. **Deep Variational Information Bottleneck (Alemi et al., ICLR 2017)**: Verify this paper and its connection to the proposed IB framework.\n\n4. **Search for \"information bottleneck token masking\" or \"information bottleneck patch dropout\"**: Are there existing works that already connect IB theory to token/patch-level masking? This would undermine the novelty claim.\n\n5. **Search for \"PAC-Bayes generalization bound token dropout\" or \"PAC-Bayes patch masking\"**: Has anyone already derived PAC-Bayes bounds for token-level masking?\n\n6. **Search for \"attention entropy regularization\" or \"attention entropy preservation\"**: The idea claims to prove an attention entropy lower bound from masking. Is this already known?\n\n7. **Search for \"counterfactual data augmentation causal invariance\" or \"counterfactual masking causal\"**: Beyond Xiao et al. (CVPR 2023), are there other works connecting masking to causal/counterfactual frameworks?\n\n8. **CRAFT (arXiv 2602.12532)**: Verify this paper about VIB for force modality integration in VLA. How close is it to the proposed approach?\n\n9. **Search \"Gaze-Regularized VLA\" (arXiv 2603.23202)**: Verify this paper about using human gaze to regularize VLA attention.\n\nFor each, report whether the paper exists, its actual claims, and whether they support or undermine the novelty of the proposed idea. Use WebSearch first, then WebFetch on the most important 2-3 papers."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c5537a78-4abc-4e7f-94f0-b2ba1d274af4",
  "isSidechain": false,
  "requestId": "req_011CayxLmWqE7agU8DiXKZGQ",
  "type": "assistant",
  "uuid": "4d0f653b-9879-4d35-811c-9b4de286aa9b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "38eec20f-28d6-4706-b24b-8f0ea53acfb9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015JFpBe6UQkgR1SAb8wDJbk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15543,
      "cache_read_input_tokens": 11841,
      "output_tokens": 1966,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15543,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1966,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 15543,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15543
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

_source line 13 · 2026-05-13T04:46:09.386Z_

<details><summary>↩ Tool result · `toolu_014E9AZhur474ywR1JzdYTYh`</summary>

```text
Now I have all the information needed. Here is my comprehensive verification report.

---

## Verification Report: ML Research Idea References

### 1. "Don't Blind Your VLA" (arXiv 2510.25616)

- **(a) Exists:** YES. Confirmed on arXiv at [2510.25616](https://arxiv.org/abs/2510.25616).
- **(b) Venue/Year:** arXiv preprint, October 2025. No conference venue listed -- it is a preprint.
- **(c) Claims accuracy:** The claims about **attention migration** (attention maps become diffuse and leak into irrelevant background regions after fine-tuning), **representation collapse** (t-SNE shows blurred/overlapping clusters vs. well-separated in the base VLM), and **attention sinks** (attention becomes noisy and weakly correlated with target objects) are all **accurate** and directly stated in the paper. The paper also documents "domain forgetting" -- VLAs lose knowledge of abstract domains absent from robotics data. Their proposed solution is Visual Representation Alignment using a frozen vision teacher during fine-tuning, yielding up to 10% relative OOD improvement.

### 2. RS-CL (ICLR 2026)

- **(a) Exists:** YES. Full title: "Contrastive Representation Regularization for Vision-Language-Action Models." Available on [OpenReview](https://openreview.net/forum?id=hm2EcwFm2Q) and [arXiv 2510.01711](https://arxiv.org/abs/2510.01711).
- **(b) Venue/Year:** **ICLR 2026** -- confirmed on OpenReview.
- **(c) Claims accuracy:** The claim about **RS-CL** (Robot State-aware Contrastive Loss) is **accurate** -- it assigns pairwise weights based on distances between robot proprioceptive states. The **"view cutoff" augmentation** claim is also **accurate** -- it randomly masks out the embedding slice of one observation view from the VLM representation at the feature level (not the data level), making it computationally efficient since only the lightweight adapter needs to process augmented variants.

### 3. VLA-GSE (arXiv 2605.06175)

- **(a) Exists:** YES, surprisingly. It was posted to arXiv on **May 7, 2026**, which is only 6 days ago from today's date (May 13, 2026). Available at [arXiv 2605.06175](https://arxiv.org/html/2605.06175v1).
- **(b) Venue/Year:** arXiv preprint, May 2026. No conference venue yet.
- **(c) Claims accuracy:** The claim about **spectral expert decomposition** is **accurate**. The paper uses SVD to decompose frozen backbone weights: leading singular components initialize **generalized experts** (shared/always-on), while remaining components are partitioned to initialize **specialized experts** (routed). The paper also addresses gradient scale balancing due to singular-value imbalance across experts. The characterization as "spectral expert decomposition for VLA" is correct.

### 4. "Masked Images Are Counterfactual Samples" (CVPR 2023)

- **(a) Exists:** YES. Full title: "Masked Images Are Counterfactual Samples for Robust Fine-Tuning." Available on [CVPR 2023 Open Access](https://openaccess.thecvf.com/content/CVPR2023/html/Xiao_Masked_Images_Are_Counterfactual_Samples_for_Robust_Fine-Tuning_CVPR_2023_paper.html) and [arXiv 2303.03052](https://arxiv.org/abs/2303.03052).
- **(b) Venue/Year:** **CVPR 2023** -- confirmed.
- **(c) Claims accuracy:** **Accurate.** First author is Yao Xiao. The paper proposes using masked images as counterfactual samples by masking semantics-related or semantics-unrelated patches (identified via class activation maps) and refilling them with patches from other images. These serve as counterfactual interventions in feature-based distillation for robust fine-tuning, achieving better ID/OOD trade-offs.

### 5. PatchDropout (WACV 2023)

- **(a) Exists:** YES. Full title: "PatchDropout: Economizing Vision Transformers Using Patch Dropout." Available on [WACV 2023 Open Access](https://openaccess.thecvf.com/content/WACV2023/papers/Liu_PatchDropout_Economizing_Vision_Transformers_Using_Patch_Dropout_WACV_2023_paper.pdf) and [arXiv 2208.07220](https://arxiv.org/abs/2208.07220).
- **(b) Venue/Year:** **WACV 2023** -- confirmed.
- **(c) Claims accuracy:** **Accurate.** The paper proposes randomly dropping input patches during ViT training/inference, reducing FLOPs and memory by at least 50% on standard datasets like ImageNet, with up to 5x savings on high-resolution medical images. Implementation is straightforward (a single `PatchDropout(keep_rate)` call before transformer blocks).

### 6. LightVLA (ICRA 2026)

- **(a) Exists:** YES. Full title: "The Better You Learn, The Smarter You Prune: Towards Efficient Vision-language-action Models via Differentiable Token Pruning." Available on [GitHub](https://github.com/LiAutoAD/LightVLA) and [arXiv 2509.12594](https://arxiv.org/abs/2509.12594).
- **(b) Venue/Year:** **ICRA 2026** -- confirmed (accepted January 31, 2026).
- **(c) Claims accuracy:** The **+2.6% success rate** claim is **accurate** -- LightVLA achieves a 2.6% improvement in task success rate on the LIBERO benchmark. The **differentiable token selection** claim is **accurate** -- it uses dynamic queries (generated via cross-attention between visual tokens and task instruction tokens) and Gumbel softmax for differentiable token selection. Additionally confirmed: 59.1% FLOPs reduction, 38.2% latency reduction, no additional trainable parameters, and no heuristic magic numbers.

### 7. OpenVLA-OFT

- **(a) Exists:** YES. Available at [openvla-oft.github.io](https://openvla-oft.github.io/) and [arXiv 2502.19645](https://arxiv.org/abs/2502.19645).
- **(b) Venue/Year:** arXiv preprint, February 2025.
- **(c) Claims accuracy:** The **97% LIBERO success rate** is **accurate** -- specifically 97.1% average across 4 LIBERO task suites. The **SOTA claim** is **accurate** -- it outperforms pi0, MDT, Seer, DiT Policy, Octo, and Diffusion Policy. Key improvements come from parallel decoding, action chunking, continuous action representation, and L1 regression-based learning, achieving a 26x speedup in action generation.

### 8. "To Sink or Not to Sink" (ICLR 2026)

- **(a) Exists:** YES. Full title: "To Sink or Not to Sink: Visual Information Pathways in Large Vision-Language Models." Available on [OpenReview](https://openreview.net/forum?id=sQGlhjKUC0) and [arXiv 2510.08510](https://arxiv.org/abs/2510.08510).
- **(b) Venue/Year:** **ICLR 2026** -- confirmed (published January 26, 2026).
- **(c) Claims accuracy:** **Accurate** that it is about attention sinks in VLMs. However, the paper's specific focus is on **ViT attention sinks** (high-norm visual tokens from the Vision Transformer), rather than attention sinks in the LLM component. The key finding is that these ViT sink tokens encapsulate high-level semantic concepts but are often overlooked in existing LVLM architectures. The authors propose both training-free and training-based methods to better leverage these tokens, demonstrating improvements across mathematical problem solving, logical inference, and geometric understanding tasks.

---

### Summary Table

| # | Paper | Exists? | Venue Correct? | Claims Accurate? |
|---|-------|---------|----------------|-----------------|
| 1 | Don't Blind Your VLA | YES | YES (arXiv 2510) | YES |
| 2 | RS-CL | YES | YES (ICLR 2026) | YES |
| 3 | VLA-GSE | YES | YES (arXiv May 2026) | YES |
| 4 | Masked Images Are Counterfactual | YES | YES (CVPR 2023) | YES |
| 5 | PatchDropout | YES | YES (WACV 2023) | YES |
| 6 | LightVLA | YES | YES (ICRA 2026) | YES |
| 7 | OpenVLA-OFT | YES | arXiv preprint | YES (97.1%, SOTA) |
| 8 | To Sink or Not to Sink | YES | YES (ICLR 2026) | YES (note: focus is ViT sinks specifically) |

**All 8 papers verified as real and existing. All major claims about them appear accurate.** The only nuance worth noting is paper #8 -- while it is indeed about attention sinks in VLMs as claimed, its specific contribution is about *ViT-side* attention sinks (high-norm visual tokens from the vision encoder) rather than attention sinks in the language model component. If the research idea cites it in the context of LLM-side attention sinks, that would be a slight mischaracterization.

Sources:
- [Don't Blind Your VLA - arXiv](https://arxiv.org/abs/2510.25616)
- [Don't Blind Your VLA - HTML](https://arxiv.org/html/2510.25616)
- [RS-CL - OpenReview](https://openreview.net/forum?id=hm2EcwFm2Q)
- [RS-CL - arXiv](https://arxiv.org/abs/2510.01711)
- [RS-CL - arXiv HTML](https://arxiv.org/html/2510.01711v1)
- [VLA-GSE - arXiv HTML](https://arxiv.org/html/2605.06175v1)
- [Masked Images Are Counterfactual Samples - CVPR 2023](https://openaccess.thecvf.com/content/CVPR2023/html/Xiao_Masked_Images_Are_Counterfactual_Samples_for_Robust_Fine-Tuning_CVPR_2023_paper.html)
- [Masked Images Are Counterfactual Samples - arXiv](https://arxiv.org/abs/2303.03052)
- [PatchDropout - WACV 2023](https://openaccess.thecvf.com/content/WACV2023/papers/Liu_PatchDropout_Economizing_Vision_Transformers_Using_Patch_Dropout_WACV_2023_paper.pdf)
- [PatchDropout - arXiv](https://arxiv.org/abs/2208.07220)
- [LightVLA - GitHub](https://github.com/LiAutoAD/LightVLA)
- [LightVLA - arXiv](https://arxiv.org/abs/2509.12594)
- [OpenVLA-OFT](https://openvla-oft.github.io/)
- [OpenVLA-OFT - arXiv](https://arxiv.org/abs/2502.19645)
- [To Sink or Not to Sink - OpenReview](https://openreview.net/forum?id=sQGlhjKUC0)
- [To Sink or Not to Sink - arXiv](https://arxiv.org/abs/2510.08510)

agentId: aaaf10396fbe9b422 (use SendMessage with to: 'aaaf10396fbe9b422' to continue this agent)
&lt;usage>total_tokens: 27023
tool_uses: 21
duration_ms: 227371&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "33d9e667-7ba1-4a44-8a09-b37dae818479",
  "isSidechain": false,
  "promptId": "251a69dd-0148-46cf-91d6-c922d95174a8",
  "type": "user",
  "uuid": "c8ad357d-ba18-4f50-9b94-19c3452bf011",
  "toolUseResult": {
    "status": "completed",
    "prompt": "You are helping me review an ML research idea. I need you to search for and verify the following claims and references. For each search, use WebSearch and then WebFetch on the most relevant results.\n\n1. **Verify \"Don't Blind Your VLA\" (arXiv 2510.25616)**: Search for this paper, confirm it exists, and check its main claims about attention migration and representation collapse during VLA finetuning.\n\n2. **Verify RS-CL (ICLR 2026)**: Search for \"Contrastive Representation Regularization Vision-Language-Action ICLR 2026\" and confirm this paper exists at ICLR 2026 with the claimed \"view cutoff\" augmentation.\n\n3. **Verify VLA-GSE (arXiv 2605.06175)**: Search for this paper about spectral expert decomposition for VLA. Note: arXiv 2605 means May 2026 — verify if this actually exists.\n\n4. **Verify \"Masked Images Are Counterfactual Samples\" (CVPR 2023)**: Search for this paper by Xiao et al. and confirm its claims about masked patches as counterfactual interventions.\n\n5. **Verify PatchDropout (WACV 2023)**: Search for \"PatchDropout Economizing Vision Transformers\" and confirm it exists.\n\n6. **Verify LightVLA (ICRA 2026)**: Search for \"LightVLA token pruning ICRA 2026\" and confirm the claimed +2.6% success rate from differentiable token selection.\n\n7. **Search for OpenVLA-OFT**: Verify the claimed 97% LIBERO success rate and current SOTA status.\n\n8. **Verify \"To Sink or Not to Sink\" (ICLR 2026)**: Search for this paper about attention sinks in VLMs.\n\nFor each paper, report: (a) whether it exists, (b) its actual venue/year, (c) whether the claims made about it in the idea are accurate. Use WebSearch first, then WebFetch on key results.",
    "agentId": "aaaf10396fbe9b422",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have all the information needed. Here is my comprehensive verification report.\n\n---\n\n## Verification Report: ML Research Idea References\n\n### 1. \"Don't Blind Your VLA\" (arXiv 2510.25616)\n\n- **(a) Exists:** YES. Confirmed on arXiv at [2510.25616](https://arxiv.org/abs/2510.25616).\n- **(b) Venue/Year:** arXiv preprint, October 2025. No conference venue listed -- it is a preprint.\n- **(c) Claims accuracy:** The claims about **attention migration** (attention maps become diffuse and leak into irrelevant background regions after fine-tuning), **representation collapse** (t-SNE shows blurred/overlapping clusters vs. well-separated in the base VLM), and **attention sinks** (attention becomes noisy and weakly correlated with target objects) are all **accurate** and directly stated in the paper. The paper also documents \"domain forgetting\" -- VLAs lose knowledge of abstract domains absent from robotics data. Their proposed solution is Visual Representation Alignment using a frozen vision teacher during fine-tuning, yielding up to 10% relative OOD improvement.\n\n### 2. RS-CL (ICLR 2026)\n\n- **(a) Exists:** YES. Full title: \"Contrastive Representation Regularization for Vision-Language-Action Models.\" Available on [OpenReview](https://openreview.net/forum?id=hm2EcwFm2Q) and [arXiv 2510.01711](https://arxiv.org/abs/2510.01711).\n- **(b) Venue/Year:** **ICLR 2026** -- confirmed on OpenReview.\n- **(c) Claims accuracy:** The claim about **RS-CL** (Robot State-aware Contrastive Loss) is **accurate** -- it assigns pairwise weights based on distances between robot proprioceptive states. The **\"view cutoff\" augmentation** claim is also **accurate** -- it randomly masks out the embedding slice of one observation view from the VLM representation at the feature level (not the data level), making it computationally efficient since only the lightweight adapter needs to process augmented variants.\n\n### 3. VLA-GSE (arXiv 2605.06175)\n\n- **(a) Exists:** YES, surprisingly. It was posted to arXiv on **May 7, 2026**, which is only 6 days ago from today's date (May 13, 2026). Available at [arXiv 2605.06175](https://arxiv.org/html/2605.06175v1).\n- **(b) Venue/Year:** arXiv preprint, May 2026. No conference venue yet.\n- **(c) Claims accuracy:** The claim about **spectral expert decomposition** is **accurate**. The paper uses SVD to decompose frozen backbone weights: leading singular components initialize **generalized experts** (shared/always-on), while remaining components are partitioned to initialize **specialized experts** (routed). The paper also addresses gradient scale balancing due to singular-value imbalance across experts. The characterization as \"spectral expert decomposition for VLA\" is correct.\n\n### 4. \"Masked Images Are Counterfactual Samples\" (CVPR 2023)\n\n- **(a) Exists:** YES. Full title: \"Masked Images Are Counterfactual Samples for Robust Fine-Tuning.\" Available on [CVPR 2023 Open Access](https://openaccess.thecvf.com/content/CVPR2023/html/Xiao_Masked_Images_Are_Counterfactual_Samples_for_Robust_Fine-Tuning_CVPR_2023_paper.html) and [arXiv 2303.03052](https://arxiv.org/abs/2303.03052).\n- **(b) Venue/Year:** **CVPR 2023** -- confirmed.\n- **(c) Claims accuracy:** **Accurate.** First author is Yao Xiao. The paper proposes using masked images as counterfactual samples by masking semantics-related or semantics-unrelated patches (identified via class activation maps) and refilling them with patches from other images. These serve as counterfactual interventions in feature-based distillation for robust fine-tuning, achieving better ID/OOD trade-offs.\n\n### 5. PatchDropout (WACV 2023)\n\n- **(a) Exists:** YES. Full title: \"PatchDropout: Economizing Vision Transformers Using Patch Dropout.\" Available on [WACV 2023 Open Access](https://openaccess.thecvf.com/content/WACV2023/papers/Liu_PatchDropout_Economizing_Vision_Transformers_Using_Patch_Dropout_WACV_2023_paper.pdf) and [arXiv 2208.07220](https://arxiv.org/abs/2208.07220).\n- **(b) Venue/Year:** **WACV 2023** -- confirmed.\n- **(c) Claims accuracy:** **Accurate.** The paper proposes randomly dropping input patches during ViT training/inference, reducing FLOPs and memory by at least 50% on standard datasets like ImageNet, with up to 5x savings on high-resolution medical images. Implementation is straightforward (a single `PatchDropout(keep_rate)` call before transformer blocks).\n\n### 6. LightVLA (ICRA 2026)\n\n- **(a) Exists:** YES. Full title: \"The Better You Learn, The Smarter You Prune: Towards Efficient Vision-language-action Models via Differentiable Token Pruning.\" Available on [GitHub](https://github.com/LiAutoAD/LightVLA) and [arXiv 2509.12594](https://arxiv.org/abs/2509.12594).\n- **(b) Venue/Year:** **ICRA 2026** -- confirmed (accepted January 31, 2026).\n- **(c) Claims accuracy:** The **+2.6% success rate** claim is **accurate** -- LightVLA achieves a 2.6% improvement in task success rate on the LIBERO benchmark. The **differentiable token selection** claim is **accurate** -- it uses dynamic queries (generated via cross-attention between visual tokens and task instruction tokens) and Gumbel softmax for differentiable token selection. Additionally confirmed: 59.1% FLOPs reduction, 38.2% latency reduction, no additional trainable parameters, and no heuristic magic numbers.\n\n### 7. OpenVLA-OFT\n\n- **(a) Exists:** YES. Available at [openvla-oft.github.io](https://openvla-oft.github.io/) and [arXiv 2502.19645](https://arxiv.org/abs/2502.19645).\n- **(b) Venue/Year:** arXiv preprint, February 2025.\n- **(c) Claims accuracy:** The **97% LIBERO success rate** is **accurate** -- specifically 97.1% average across 4 LIBERO task suites. The **SOTA claim** is **accurate** -- it outperforms pi0, MDT, Seer, DiT Policy, Octo, and Diffusion Policy. Key improvements come from parallel decoding, action chunking, continuous action representation, and L1 regression-based learning, achieving a 26x speedup in action generation.\n\n### 8. \"To Sink or Not to Sink\" (ICLR 2026)\n\n- **(a) Exists:** YES. Full title: \"To Sink or Not to Sink: Visual Information Pathways in Large Vision-Language Models.\" Available on [OpenReview](https://openreview.net/forum?id=sQGlhjKUC0) and [arXiv 2510.08510](https://arxiv.org/abs/2510.08510).\n- **(b) Venue/Year:** **ICLR 2026** -- confirmed (published January 26, 2026).\n- **(c) Claims accuracy:** **Accurate** that it is about attention sinks in VLMs. However, the paper's specific focus is on **ViT attention sinks** (high-norm visual tokens from the Vision Transformer), rather than attention sinks in the LLM component. The key finding is that these ViT sink tokens encapsulate high-level semantic concepts but are often overlooked in existing LVLM architectures. The authors propose both training-free and training-based methods to better leverage these tokens, demonstrating improvements across mathematical problem solving, logical inference, and geometric understanding tasks.\n\n---\n\n### Summary Table\n\n| # | Paper | Exists? | Venue Correct? | Claims Accurate? |\n|---|-------|---------|----------------|-----------------|\n| 1 | Don't Blind Your VLA | YES | YES (arXiv 2510) | YES |\n| 2 | RS-CL | YES | YES (ICLR 2026) | YES |\n| 3 | VLA-GSE | YES | YES (arXiv May 2026) | YES |\n| 4 | Masked Images Are Counterfactual | YES | YES (CVPR 2023) | YES |\n| 5 | PatchDropout | YES | YES (WACV 2023) | YES |\n| 6 | LightVLA | YES | YES (ICRA 2026) | YES |\n| 7 | OpenVLA-OFT | YES | arXiv preprint | YES (97.1%, SOTA) |\n| 8 | To Sink or Not to Sink | YES | YES (ICLR 2026) | YES (note: focus is ViT sinks specifically) |\n\n**All 8 papers verified as real and existing. All major claims about them appear accurate.** The only nuance worth noting is paper #8 -- while it is indeed about attention sinks in VLMs as claimed, its specific contribution is about *ViT-side* attention sinks (high-norm visual tokens from the vision encoder) rather than attention sinks in the language model component. If the research idea cites it in the context of LLM-side attention sinks, that would be a slight mischaracterization.\n\nSources:\n- [Don't Blind Your VLA - arXiv](https://arxiv.org/abs/2510.25616)\n- [Don't Blind Your VLA - HTML](https://arxiv.org/html/2510.25616)\n- [RS-CL - OpenReview](https://openreview.net/forum?id=hm2EcwFm2Q)\n- [RS-CL - arXiv](https://arxiv.org/abs/2510.01711)\n- [RS-CL - arXiv HTML](https://arxiv.org/html/2510.01711v1)\n- [VLA-GSE - arXiv HTML](https://arxiv.org/html/2605.06175v1)\n- [Masked Images Are Counterfactual Samples - CVPR 2023](https://openaccess.thecvf.com/content/CVPR2023/html/Xiao_Masked_Images_Are_Counterfactual_Samples_for_Robust_Fine-Tuning_CVPR_2023_paper.html)\n- [Masked Images Are Counterfactual Samples - arXiv](https://arxiv.org/abs/2303.03052)\n- [PatchDropout - WACV 2023](https://openaccess.thecvf.com/content/WACV2023/papers/Liu_PatchDropout_Economizing_Vision_Transformers_Using_Patch_Dropout_WACV_2023_paper.pdf)\n- [PatchDropout - arXiv](https://arxiv.org/abs/2208.07220)\n- [LightVLA - GitHub](https://github.com/LiAutoAD/LightVLA)\n- [LightVLA - arXiv](https://arxiv.org/abs/2509.12594)\n- [OpenVLA-OFT](https://openvla-oft.github.io/)\n- [OpenVLA-OFT - arXiv](https://arxiv.org/abs/2502.19645)\n- [To Sink or Not to Sink - OpenReview](https://openreview.net/forum?id=sQGlhjKUC0)\n- [To Sink or Not to Sink - arXiv](https://arxiv.org/abs/2510.08510)"
      }
    ],
    "totalDurationMs": 227371,
    "totalTokens": 27023,
    "totalToolUseCount": 21,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 368,
      "cache_read_input_tokens": 23591,
      "output_tokens": 3063,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 368
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3063,
          "cache_read_input_tokens": 23591,
          "cache_creation_input_tokens": 368,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 368,
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
      "otherToolCount": 21
    }
  },
  "sourceToolAssistantUUID": "33d9e667-7ba1-4a44-8a09-b37dae818479",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "38eec20f-28d6-4706-b24b-8f0ea53acfb9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 14_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-13 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "c8ad357d-ba18-4f50-9b94-19c3452bf011",
  "sessionId": "38eec20f-28d6-4706-b24b-8f0ea53acfb9"
}
```

---

### Runtime record

_source line 15_

```json
{
  "type": "ai-title",
  "aiTitle": "Review VLA token masking robustness via theory",
  "sessionId": "38eec20f-28d6-4706-b24b-8f0ea53acfb9"
}
```

---

### Tool result

_source line 16 · 2026-05-13T04:46:17.169Z_

<details><summary>↩ Tool result · `toolu_01DKP7jci1dqWvDj7bMyirYb`</summary>

```text
I now have comprehensive information for all 9 items. Here is my full analysis:

---

## Verification Report: Theoretical Claims in the Proposed Token-Masking VLA Finetuning Idea

### 1. Information Dropout (Achille & Soatto, TPAMI 2018)

**Status: Paper exists. Claim is slightly overstated.**

The paper "Information Dropout: Learning Optimal Representations Through Noisy Computation" is real and published in IEEE TPAMI 2018 (also available as arXiv:1611.01353). However, the claim that "multiplicative noise on representations is **equivalent** to IB regularization" is an overstatement. The actual result is weaker: when restricted to the family of distributions obtained by injecting noise to one layer of a neural network, one can **efficiently approximate and minimize** the IB Lagrangian. The authors explicitly acknowledge: *"Since we restrict the family of distributions, there is no guarantee that the resulting representation will be optimal."* The representation uses z = epsilon . f(x) where epsilon is multiplicative noise with unit mean, and standard dropout is shown to be a special case (Bernoulli noise rescaled to mean 1). So the relationship is an **approximation under restricted distribution families**, not an equivalence. The proposed idea should be careful not to overclaim this link.

**Source**: [Information Dropout - IEEE TPAMI](https://dl.acm.org/doi/10.1109/TPAMI.2017.2784440) | [arXiv](https://ar5iv.labs.arxiv.org/html/1611.01353)

---

### 2. Gal & Ghahramani (ICML 2016) "Dropout as a Bayesian Approximation"

**Status: Paper exists. PAC-Bayes connection requires clarification.**

The paper "Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning" was published at ICML 2016 (Proceedings of the 33rd ICML, pp. 1050-1059). It is a highly influential paper. However, its primary contribution is casting dropout as approximate **Bayesian inference in deep Gaussian processes** -- not PAC-Bayes bounds. The paper is about uncertainty estimation, not generalization bounds.

The PAC-Bayes connection to dropout actually comes from a different source: **McAllester (2013), "A PAC-Bayesian Tutorial with a Dropout Bound"** (arXiv:1307.2118), which explicitly derives PAC-Bayesian bounds for dropout training. If the proposed idea claims to adapt PAC-Bayes bounds "from Gal & Ghahramani," that is a misattribution. The correct citation chain should go through McAllester (2013) for PAC-Bayes dropout bounds, not Gal & Ghahramani (2016).

**Source**: [Gal & Ghahramani ICML 2016](https://proceedings.mlr.press/v48/gal16.html) | [McAllester 2013](https://arxiv.org/abs/1307.2118)

---

### 3. Deep Variational Information Bottleneck (Alemi et al., ICLR 2017)

**Status: Paper exists. Claims are accurate.**

"Deep Variational Information Bottleneck" by Alemi, Fischer, Dillon, and Murphy was published at ICLR 2017 (arXiv:1612.00410). It presents a variational approximation to the IB framework of Tishby et al. (1999), using neural network parameterization and the reparameterization trick. The paper shows VIB-trained models outperform other regularization methods in generalization and adversarial robustness. This is a foundational and legitimate building block for any IB-based deep learning approach. Its connection to the proposed framework is well-grounded.

**Source**: [arXiv:1612.00410](https://arxiv.org/abs/1612.00410) | [OpenReview](https://openreview.net/forum?id=HyxQzBceg)

---

### 4. Existing Works Connecting IB Theory to Token/Patch-Level Masking

**Status: SIGNIFICANT PRIOR WORK EXISTS. This undermines the novelty claim.**

The search revealed a directly relevant paper: **"Efficient Visual Transformer by Information Bottleneck Inspired Token Merging" (IBTM)** by Wang & Yang (OpenReview). This paper:
- Derives a **novel separable variational upper bound for the IB loss**
- Designs a **mask module architecture** explicitly to reduce this IB bound
- Applies this at the **token level** in vision transformers
- Demonstrates FLOPs and inference time reduction while maintaining/improving accuracy

This is essentially the same theoretical connection the proposed idea claims: IB theory justifying token-level operations in transformers. While IBTM focuses on token *merging* (for efficiency) rather than token *masking* (for regularization during finetuning), the theoretical bridge between IB and token-level operations is already established.

Additionally, **PatchDropout (WACV 2023)** randomly drops input patch tokens for efficiency, though without explicit IB justification. **TLM: Token-Level Masking for Transformers (EMNLP 2023)** proposes token-level masking in multi-head attention as regularization.

**Source**: [IBTM - OpenReview](https://openreview.net/forum?id=Jwgw3znxT3) | [TLM - ACL Anthology](https://aclanthology.org/2023.emnlp-main.871/) | [PatchDropout - WACV 2023](https://openaccess.thecvf.com/content/WACV2023/papers/Liu_PatchDropout_Economizing_Vision_Transformers_Using_Patch_Dropout_WACV_2023_paper.pdf)

---

### 5. PAC-Bayes Bounds for Token-Level Masking

**Status: Very close prior work exists in AttentionDrop (2025).**

No paper was found that derives PAC-Bayes bounds specifically for **token dropout/masking**. However, a very recent and highly relevant paper exists: **"AttentionDrop: A Novel Regularization Method for Transformer Models" (arXiv:2504.12088, April 2025)** by Baig et al. This paper:
- Derives **PAC-Bayes generalization bounds** for attention-level stochastic perturbation
- Proves that attention-level noise increases posterior entropy and tightens risk bounds (Theorem 1)
- Introduces Hard Attention Masking (zeroing top-k logits), Blurred Smoothing, and Consistency Regularization
- Shows the KL divergence simplifies to KL(Q||P) = Hn^2(-ln sigma + C_0)

This operates on **attention distributions** rather than dropping entire tokens, but the PAC-Bayes framework for attention-level masking in transformers is already established. Extending McAllester's (2013) dropout PAC-Bayes bound to token-level masking would be an incremental step, not a fundamental new contribution, given that AttentionDrop already bridges this gap for attention-level operations.

**Source**: [AttentionDrop](https://arxiv.org/html/2504.12088) | [McAllester PAC-Bayes Dropout](https://arxiv.org/abs/1307.2118)

---

### 6. Attention Entropy Regularization / Attention Entropy Preservation

**Status: Well-studied area. Entropy bounds from masking are partially known.**

This is a well-explored research area:

- **Zhai et al. (ICML 2023), "Stabilizing Transformer Training by Preventing Attention Entropy Collapse"** (Apple Research): Proves a **tight lower bound** on attention entropy that decreases exponentially with the spectral norm of attention logits. They introduce sigmaReparam to prevent entropy collapse.
- **AttentionDrop (2025)**: Shows that masking/blurring attention distributions increases posterior entropy and derives formal bounds connecting this to generalization.
- **Entropy-based Attention Regularization (EAR)**: Used for bias mitigation.
- **Entropy-Invariant Scaling**: Adjusts softmax temperature to preserve entropy as sequence length grows.

The claim that the proposed idea "proves an attention entropy lower bound from masking" would need to be carefully differentiated from the Zhai et al. (2023) lower bound and the AttentionDrop entropy analysis. The general connection between masking/dropout and attention entropy is already known.

**Source**: [Zhai et al. ICML 2023](https://arxiv.org/abs/2303.06296) | [AttentionDrop](https://arxiv.org/html/2504.12088)

---

### 7. Counterfactual Data Augmentation and Causal Invariance via Masking

**Status: Multiple prior works exist, including in robotics.**

- **Xiao et al. (CVPR 2023), "Masked Images Are Counterfactual Samples for Robust Fine-tuning"**: This paper explicitly frames masked images as counterfactual samples based on causal analysis. It masks semantically relevant or irrelevant patches using class activation maps. However, this is for **image classification**, not VLA/robotics.
- **RoCoDA (arXiv:2411.16959)**: "Counterfactual Data Augmentation for Data-Efficient Robot Learning from Demonstrations" -- directly applies counterfactual data augmentation in **robotics imitation learning**. Uses causal graphs to identify task-irrelevant state subsets and resamples them while preserving causal dependencies.
- **C2L**: Generates factual and counterfactual samples by masking non-causal and causal tokens, applying contrastive learning.
- **Causal Action Influence Aware Counterfactual Data Augmentation (arXiv:2405.18917)**: Explicitly connects causal action influence with counterfactual augmentation.

The counterfactual/causal framing of masking is not novel. RoCoDA in particular already connects counterfactual augmentation to robotics learning, which is close to the VLA domain.

**Source**: [Xiao et al. CVPR 2023](https://openaccess.thecvf.com/content/CVPR2023/html/Xiao_Masked_Images_Are_Counterfactual_Samples_for_Robust_Fine-Tuning_CVPR_2023_paper.html) | [RoCoDA](https://arxiv.org/abs/2411.16959)

---

### 8. CRAFT (arXiv:2602.12532)

**Status: Paper exists and is VERY close to the proposed approach.**

CRAFT ("Adapting VLA Models to Contact-rich Manipulation via Force-aware Curriculum Fine-tuning") is a real paper that:
- Uses a **Variational Information Bottleneck (VIB) module** applied directly to VLA models
- Compresses **vision and language embeddings** (not individual tokens) through a Gaussian posterior: p(F^c|F) = N(mu, sigma^2), with standard normal prior
- Uses the VIB loss: L_VIB = 1/2 * sum(-log sigma_i^2 + mu_i^2 + sigma_i^2 - 1)
- Employs a curriculum: lambda_VIB(t) = lambda_init * exp(-t/T_decay), gradually relaxing the bottleneck

**How close is it to the proposed approach?** CRAFT already applies IB theory (via VIB) to VLA finetuning. The key differences are: (1) CRAFT operates on **fused embeddings** rather than individual tokens, (2) CRAFT's purpose is to prioritize force modality, not general regularization, and (3) CRAFT uses Gaussian noise injection rather than discrete token masking. But the core idea -- "use VIB during VLA finetuning to control information flow" -- is already claimed by CRAFT. Any proposed approach applying IB to VLA token masking would need to clearly differentiate from CRAFT.

**Source**: [CRAFT arXiv](https://arxiv.org/abs/2602.12532) | [CRAFT HTML](https://arxiv.org/html/2602.12532)

---

### 9. Gaze-Regularized VLA (arXiv:2603.23202)

**Status: Paper exists and is relevant to attention regularization in VLAs.**

"Gaze-Regularized Vision-Language-Action Models for Robotic Manipulation" by Pani & Yang (University of Hong Kong, March 2026):
- Uses **KL divergence** to align VLA transformer attention with human gaze heatmaps converted to patch-level distributions
- Achieves 4-12% improvement on manipulation benchmarks
- Requires no architectural modifications or inference-time overhead
- Produces interpretable attention patterns

This paper is relevant because it demonstrates that **regularizing VLA attention distributions** (in this case toward human gaze priors) improves performance. If the proposed idea claims that token masking creates beneficial attention entropy properties, the Gaze-VLA paper provides an alternative mechanism for achieving similar attention regularization goals. It does not use IB theory or token masking directly, but it occupies similar conceptual territory (controlling what VLA attention focuses on during finetuning).

**Source**: [arXiv:2603.23202](https://arxiv.org/abs/2603.23202)

---

## Overall Assessment

The proposed idea of using token masking during VLA finetuning with IB-theoretic justification faces **significant novelty concerns**:

1. **The IB-to-token-masking bridge already exists** (IBTM paper), though applied to token merging for efficiency rather than regularization.
2. **VIB applied to VLA finetuning already exists** (CRAFT), though at the embedding level rather than token level.
3. **PAC-Bayes bounds for attention-level masking already exist** (AttentionDrop 2025), making extension to token-level masking incremental.
4. **Attention entropy bounds from masking/dropout are already known** (Zhai et al. 2023, AttentionDrop 2025).
5. **Counterfactual framing of masking** is established (Xiao et al. CVPR 2023), and **counterfactual augmentation in robotics** is established (RoCoDA).
6. **The Gal & Ghahramani citation for PAC-Bayes is a misattribution** -- the correct source is McAllester (2013).
7. **The Achille & Soatto claim should be weakened** from "equivalence" to "approximation under restricted distribution families."

The strongest potential novelty angle would be the **specific combination** of IB-theoretic token masking applied to VLA finetuning with formal generalization bounds -- but each individual component has clear precedent, and CRAFT already occupies the "IB + VLA finetuning" space.

agentId: a5c79868542b0b237 (use SendMessage with to: 'a5c79868542b0b237' to continue this agent)
&lt;usage>total_tokens: 36004
tool_uses: 28
duration_ms: 214147&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4d0f653b-9879-4d35-811c-9b4de286aa9b",
  "isSidechain": false,
  "promptId": "251a69dd-0148-46cf-91d6-c922d95174a8",
  "type": "user",
  "uuid": "4dc8c650-b2ab-4217-9224-753e93327f59",
  "toolUseResult": {
    "status": "completed",
    "prompt": "You are helping me review an ML research idea that proposes using token masking during VLA (Vision-Language-Action) finetuning, with theoretical justification from Information Bottleneck theory. I need you to verify several theoretical claims.\n\n1. **Information Dropout (Achille & Soatto, TPAMI 2018)**: Search for this paper and verify the claim that \"multiplicative noise on representations is equivalent to IB regularization.\" Use WebSearch and WebFetch to read the abstract and key results.\n\n2. **Gal & Ghahramani (ICML 2016) \"Dropout as a Bayesian Approximation\"**: Verify this paper exists and its relevance to PAC-Bayes bounds for dropout. The idea claims to adapt PAC-Bayes bounds from this work to token-level masking.\n\n3. **Deep Variational Information Bottleneck (Alemi et al., ICLR 2017)**: Verify this paper and its connection to the proposed IB framework.\n\n4. **Search for \"information bottleneck token masking\" or \"information bottleneck patch dropout\"**: Are there existing works that already connect IB theory to token/patch-level masking? This would undermine the novelty claim.\n\n5. **Search for \"PAC-Bayes generalization bound token dropout\" or \"PAC-Bayes patch masking\"**: Has anyone already derived PAC-Bayes bounds for token-level masking?\n\n6. **Search for \"attention entropy regularization\" or \"attention entropy preservation\"**: The idea claims to prove an attention entropy lower bound from masking. Is this already known?\n\n7. **Search for \"counterfactual data augmentation causal invariance\" or \"counterfactual masking causal\"**: Beyond Xiao et al. (CVPR 2023), are there other works connecting masking to causal/counterfactual frameworks?\n\n8. **CRAFT (arXiv 2602.12532)**: Verify this paper about VIB for force modality integration in VLA. How close is it to the proposed approach?\n\n9. **Search \"Gaze-Regularized VLA\" (arXiv 2603.23202)**: Verify this paper about using human gaze to regularize VLA attention.\n\nFor each, report whether the paper exists, its actual claims, and whether they support or undermine the novelty of the proposed idea. Use WebSearch first, then WebFetch on the most important 2-3 papers.",
    "agentId": "a5c79868542b0b237",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "I now have comprehensive information for all 9 items. Here is my full analysis:\n\n---\n\n## Verification Report: Theoretical Claims in the Proposed Token-Masking VLA Finetuning Idea\n\n### 1. Information Dropout (Achille & Soatto, TPAMI 2018)\n\n**Status: Paper exists. Claim is slightly overstated.**\n\nThe paper \"Information Dropout: Learning Optimal Representations Through Noisy Computation\" is real and published in IEEE TPAMI 2018 (also available as arXiv:1611.01353). However, the claim that \"multiplicative noise on representations is **equivalent** to IB regularization\" is an overstatement. The actual result is weaker: when restricted to the family of distributions obtained by injecting noise to one layer of a neural network, one can **efficiently approximate and minimize** the IB Lagrangian. The authors explicitly acknowledge: *\"Since we restrict the family of distributions, there is no guarantee that the resulting representation will be optimal.\"* The representation uses z = epsilon . f(x) where epsilon is multiplicative noise with unit mean, and standard dropout is shown to be a special case (Bernoulli noise rescaled to mean 1). So the relationship is an **approximation under restricted distribution families**, not an equivalence. The proposed idea should be careful not to overclaim this link.\n\n**Source**: [Information Dropout - IEEE TPAMI](https://dl.acm.org/doi/10.1109/TPAMI.2017.2784440) | [arXiv](https://ar5iv.labs.arxiv.org/html/1611.01353)\n\n---\n\n### 2. Gal & Ghahramani (ICML 2016) \"Dropout as a Bayesian Approximation\"\n\n**Status: Paper exists. PAC-Bayes connection requires clarification.**\n\nThe paper \"Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning\" was published at ICML 2016 (Proceedings of the 33rd ICML, pp. 1050-1059). It is a highly influential paper. However, its primary contribution is casting dropout as approximate **Bayesian inference in deep Gaussian processes** -- not PAC-Bayes bounds. The paper is about uncertainty estimation, not generalization bounds.\n\nThe PAC-Bayes connection to dropout actually comes from a different source: **McAllester (2013), \"A PAC-Bayesian Tutorial with a Dropout Bound\"** (arXiv:1307.2118), which explicitly derives PAC-Bayesian bounds for dropout training. If the proposed idea claims to adapt PAC-Bayes bounds \"from Gal & Ghahramani,\" that is a misattribution. The correct citation chain should go through McAllester (2013) for PAC-Bayes dropout bounds, not Gal & Ghahramani (2016).\n\n**Source**: [Gal & Ghahramani ICML 2016](https://proceedings.mlr.press/v48/gal16.html) | [McAllester 2013](https://arxiv.org/abs/1307.2118)\n\n---\n\n### 3. Deep Variational Information Bottleneck (Alemi et al., ICLR 2017)\n\n**Status: Paper exists. Claims are accurate.**\n\n\"Deep Variational Information Bottleneck\" by Alemi, Fischer, Dillon, and Murphy was published at ICLR 2017 (arXiv:1612.00410). It presents a variational approximation to the IB framework of Tishby et al. (1999), using neural network parameterization and the reparameterization trick. The paper shows VIB-trained models outperform other regularization methods in generalization and adversarial robustness. This is a foundational and legitimate building block for any IB-based deep learning approach. Its connection to the proposed framework is well-grounded.\n\n**Source**: [arXiv:1612.00410](https://arxiv.org/abs/1612.00410) | [OpenReview](https://openreview.net/forum?id=HyxQzBceg)\n\n---\n\n### 4. Existing Works Connecting IB Theory to Token/Patch-Level Masking\n\n**Status: SIGNIFICANT PRIOR WORK EXISTS. This undermines the novelty claim.**\n\nThe search revealed a directly relevant paper: **\"Efficient Visual Transformer by Information Bottleneck Inspired Token Merging\" (IBTM)** by Wang & Yang (OpenReview). This paper:\n- Derives a **novel separable variational upper bound for the IB loss**\n- Designs a **mask module architecture** explicitly to reduce this IB bound\n- Applies this at the **token level** in vision transformers\n- Demonstrates FLOPs and inference time reduction while maintaining/improving accuracy\n\nThis is essentially the same theoretical connection the proposed idea claims: IB theory justifying token-level operations in transformers. While IBTM focuses on token *merging* (for efficiency) rather than token *masking* (for regularization during finetuning), the theoretical bridge between IB and token-level operations is already established.\n\nAdditionally, **PatchDropout (WACV 2023)** randomly drops input patch tokens for efficiency, though without explicit IB justification. **TLM: Token-Level Masking for Transformers (EMNLP 2023)** proposes token-level masking in multi-head attention as regularization.\n\n**Source**: [IBTM - OpenReview](https://openreview.net/forum?id=Jwgw3znxT3) | [TLM - ACL Anthology](https://aclanthology.org/2023.emnlp-main.871/) | [PatchDropout - WACV 2023](https://openaccess.thecvf.com/content/WACV2023/papers/Liu_PatchDropout_Economizing_Vision_Transformers_Using_Patch_Dropout_WACV_2023_paper.pdf)\n\n---\n\n### 5. PAC-Bayes Bounds for Token-Level Masking\n\n**Status: Very close prior work exists in AttentionDrop (2025).**\n\nNo paper was found that derives PAC-Bayes bounds specifically for **token dropout/masking**. However, a very recent and highly relevant paper exists: **\"AttentionDrop: A Novel Regularization Method for Transformer Models\" (arXiv:2504.12088, April 2025)** by Baig et al. This paper:\n- Derives **PAC-Bayes generalization bounds** for attention-level stochastic perturbation\n- Proves that attention-level noise increases posterior entropy and tightens risk bounds (Theorem 1)\n- Introduces Hard Attention Masking (zeroing top-k logits), Blurred Smoothing, and Consistency Regularization\n- Shows the KL divergence simplifies to KL(Q||P) = Hn^2(-ln sigma + C_0)\n\nThis operates on **attention distributions** rather than dropping entire tokens, but the PAC-Bayes framework for attention-level masking in transformers is already established. Extending McAllester's (2013) dropout PAC-Bayes bound to token-level masking would be an incremental step, not a fundamental new contribution, given that AttentionDrop already bridges this gap for attention-level operations.\n\n**Source**: [AttentionDrop](https://arxiv.org/html/2504.12088) | [McAllester PAC-Bayes Dropout](https://arxiv.org/abs/1307.2118)\n\n---\n\n### 6. Attention Entropy Regularization / Attention Entropy Preservation\n\n**Status: Well-studied area. Entropy bounds from masking are partially known.**\n\nThis is a well-explored research area:\n\n- **Zhai et al. (ICML 2023), \"Stabilizing Transformer Training by Preventing Attention Entropy Collapse\"** (Apple Research): Proves a **tight lower bound** on attention entropy that decreases exponentially with the spectral norm of attention logits. They introduce sigmaReparam to prevent entropy collapse.\n- **AttentionDrop (2025)**: Shows that masking/blurring attention distributions increases posterior entropy and derives formal bounds connecting this to generalization.\n- **Entropy-based Attention Regularization (EAR)**: Used for bias mitigation.\n- **Entropy-Invariant Scaling**: Adjusts softmax temperature to preserve entropy as sequence length grows.\n\nThe claim that the proposed idea \"proves an attention entropy lower bound from masking\" would need to be carefully differentiated from the Zhai et al. (2023) lower bound and the AttentionDrop entropy analysis. The general connection between masking/dropout and attention entropy is already known.\n\n**Source**: [Zhai et al. ICML 2023](https://arxiv.org/abs/2303.06296) | [AttentionDrop](https://arxiv.org/html/2504.12088)\n\n---\n\n### 7. Counterfactual Data Augmentation and Causal Invariance via Masking\n\n**Status: Multiple prior works exist, including in robotics.**\n\n- **Xiao et al. (CVPR 2023), \"Masked Images Are Counterfactual Samples for Robust Fine-tuning\"**: This paper explicitly frames masked images as counterfactual samples based on causal analysis. It masks semantically relevant or irrelevant patches using class activation maps. However, this is for **image classification**, not VLA/robotics.\n- **RoCoDA (arXiv:2411.16959)**: \"Counterfactual Data Augmentation for Data-Efficient Robot Learning from Demonstrations\" -- directly applies counterfactual data augmentation in **robotics imitation learning**. Uses causal graphs to identify task-irrelevant state subsets and resamples them while preserving causal dependencies.\n- **C2L**: Generates factual and counterfactual samples by masking non-causal and causal tokens, applying contrastive learning.\n- **Causal Action Influence Aware Counterfactual Data Augmentation (arXiv:2405.18917)**: Explicitly connects causal action influence with counterfactual augmentation.\n\nThe counterfactual/causal framing of masking is not novel. RoCoDA in particular already connects counterfactual augmentation to robotics learning, which is close to the VLA domain.\n\n**Source**: [Xiao et al. CVPR 2023](https://openaccess.thecvf.com/content/CVPR2023/html/Xiao_Masked_Images_Are_Counterfactual_Samples_for_Robust_Fine-Tuning_CVPR_2023_paper.html) | [RoCoDA](https://arxiv.org/abs/2411.16959)\n\n---\n\n### 8. CRAFT (arXiv:2602.12532)\n\n**Status: Paper exists and is VERY close to the proposed approach.**\n\nCRAFT (\"Adapting VLA Models to Contact-rich Manipulation via Force-aware Curriculum Fine-tuning\") is a real paper that:\n- Uses a **Variational Information Bottleneck (VIB) module** applied directly to VLA models\n- Compresses **vision and language embeddings** (not individual tokens) through a Gaussian posterior: p(F^c|F) = N(mu, sigma^2), with standard normal prior\n- Uses the VIB loss: L_VIB = 1/2 * sum(-log sigma_i^2 + mu_i^2 + sigma_i^2 - 1)\n- Employs a curriculum: lambda_VIB(t) = lambda_init * exp(-t/T_decay), gradually relaxing the bottleneck\n\n**How close is it to the proposed approach?** CRAFT already applies IB theory (via VIB) to VLA finetuning. The key differences are: (1) CRAFT operates on **fused embeddings** rather than individual tokens, (2) CRAFT's purpose is to prioritize force modality, not general regularization, and (3) CRAFT uses Gaussian noise injection rather than discrete token masking. But the core idea -- \"use VIB during VLA finetuning to control information flow\" -- is already claimed by CRAFT. Any proposed approach applying IB to VLA token masking would need to clearly differentiate from CRAFT.\n\n**Source**: [CRAFT arXiv](https://arxiv.org/abs/2602.12532) | [CRAFT HTML](https://arxiv.org/html/2602.12532)\n\n---\n\n### 9. Gaze-Regularized VLA (arXiv:2603.23202)\n\n**Status: Paper exists and is relevant to attention regularization in VLAs.**\n\n\"Gaze-Regularized Vision-Language-Action Models for Robotic Manipulation\" by Pani & Yang (University of Hong Kong, March 2026):\n- Uses **KL divergence** to align VLA transformer attention with human gaze heatmaps converted to patch-level distributions\n- Achieves 4-12% improvement on manipulation benchmarks\n- Requires no architectural modifications or inference-time overhead\n- Produces interpretable attention patterns\n\nThis paper is relevant because it demonstrates that **regularizing VLA attention distributions** (in this case toward human gaze priors) improves performance. If the proposed idea claims that token masking creates beneficial attention entropy properties, the Gaze-VLA paper provides an alternative mechanism for achieving similar attention regularization goals. It does not use IB theory or token masking directly, but it occupies similar conceptual territory (controlling what VLA attention focuses on during finetuning).\n\n**Source**: [arXiv:2603.23202](https://arxiv.org/abs/2603.23202)\n\n---\n\n## Overall Assessment\n\nThe proposed idea of using token masking during VLA finetuning with IB-theoretic justification faces **significant novelty concerns**:\n\n1. **The IB-to-token-masking bridge already exists** (IBTM paper), though applied to token merging for efficiency rather than regularization.\n2. **VIB applied to VLA finetuning already exists** (CRAFT), though at the embedding level rather than token level.\n3. **PAC-Bayes bounds for attention-level masking already exist** (AttentionDrop 2025), making extension to token-level masking incremental.\n4. **Attention entropy bounds from masking/dropout are already known** (Zhai et al. 2023, AttentionDrop 2025).\n5. **Counterfactual framing of masking** is established (Xiao et al. CVPR 2023), and **counterfactual augmentation in robotics** is established (RoCoDA).\n6. **The Gal & Ghahramani citation for PAC-Bayes is a misattribution** -- the correct source is McAllester (2013).\n7. **The Achille & Soatto claim should be weakened** from \"equivalence\" to \"approximation under restricted distribution families.\"\n\nThe strongest potential novelty angle would be the **specific combination** of IB-theoretic token masking applied to VLA finetuning with formal generalization bounds -- but each individual component has clear precedent, and CRAFT already occupies the \"IB + VLA finetuning\" space."
      }
    ],
    "totalDurationMs": 214147,
    "totalTokens": 36004,
    "totalToolUseCount": 28,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 512,
      "cache_read_input_tokens": 31821,
      "output_tokens": 3670,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 512
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3670,
          "cache_read_input_tokens": 31821,
          "cache_creation_input_tokens": 512,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 512,
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
      "otherToolCount": 28
    }
  },
  "sourceToolAssistantUUID": "4d0f653b-9879-4d35-811c-9b4de286aa9b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "38eec20f-28d6-4706-b24b-8f0ea53acfb9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-13T04:46:37.312Z_

<details><summary>↩ Tool result · `toolu_01Hgt3XVkc6ht4zBtXCXYEm3`</summary>

```text
Now I have comprehensive data. Let me compile the final analysis.

---

Here is my comprehensive review of competitive and concurrent work for the "Counterfactual Token Masking" (CTM) idea for VLA finetuning, organized by search area.

---

## 1. Token Masking / Dropout in VLAs

**This is the most crowded competitive space.** There is a large and rapidly growing body of work on visual token pruning/masking in VLAs, though most focus on **inference efficiency** rather than **regularization for generalization**:

- **VLA-Pruner** (arXiv:2511.16449, Nov 2025, updated Feb 2026): Temporal-aware dual-level visual token pruning. Uses prefill attention + temporal smoothing of action-decode attention as a plug-and-play **inference-time** method. Focus is efficiency, not regularization. **Not a direct competitor** to CTM's training-time regularization framing.

- **LightVLA** (arXiv:2509.12594, ICRA 2026): Differentiable token pruning using Gumbel softmax for adaptive token selection during **training**. Reduces FLOPs by 59% with 2.9% improvement in success rate. This is closer to CTM since it modifies training, though framed as efficiency rather than regularization.

- **VLA-IAP** (arXiv:2603.22991, Mar 2026): Training-free visual token pruning via interaction alignment. Inference-time only. Not a competitor.

- **"See What Matters" / GridS** (ICML 2026): Differentiable grid sample pruning for "generalizable" VLA. This paper explicitly connects token pruning to **generalization**, not just efficiency. Uses continuous resampling of visual tokens. Published at a top venue. **Potentially a close competitor** if CTM's story is that token reduction improves generalization.

- **ETA-VLA** (arXiv:2603.25766): Temporal fusion + intra-LLM sparsification. Focused on autonomous driving VLAs. Efficiency-focused.

- **SP-VLA** (arXiv:2506.12723): Joint model scheduling and token pruning. Efficiency-focused.

- **SpecPrune-VLA** (OpenReview): Action-aware self-speculative pruning. Efficiency-focused.

**Key gap CTM could exploit:** Most of these papers frame token reduction as an **efficiency** problem. CTM's framing of token masking as an explicit **regularization** strategy grounded in the information bottleneck principle is relatively novel in the VLA space.

---

## 2. VLA Robustness / Generalization Recent Work

**CRITICAL FINDING -- "Rethinking VLA Model Scaling" (arXiv:2602.09722, Feb 2026):** This paper by Wang et al. **directly tested sensory dropout** (stochastically masking visual inputs and proprioception during training with p=0.2) as a regularization technique for VLA scaling. Their finding: **sensory dropout HURT performance**. Disabling visual dropout increased success rates from 84.5% to 85.6%. They conclude "the natural diversity of the pre-training corpus already serves as an effective regularizer." **This is a direct challenge to the CTM premise** and must be addressed in the paper. The CTM paper needs to explain why its approach differs (e.g., counterfactual design, targeted rather than random masking, different training regime, finetuning vs. pretraining context).

Other relevant generalization work:
- **"What Can RL Bring to VLA Generalization?"** (arXiv:2505.19789): RL finetuning (PPO) enhances VLA generalization, especially in execution and semantics.
- **VLA-RFT** (ICLR 2026): Reinforcement finetuning with world model simulators.
- **"Robust Finetuning via Parameter Merging"** (arXiv:2512.08333, Yadav et al., Berkeley): Weight interpolation between pretrained and finetuned checkpoints. No token masking -- purely weight-space. Uses LIBERO and real-world. **Close competitor** in the "robust finetuning" framing.
- **"Boosting VLA Finetuning with Feasible Action Neighborhood Prior"** (arXiv:2604.01570, Apr 2026): KL-divergence regularizer on action distributions using Gaussian priors. Tested on LIBERO and ManiSkill. **Close competitor** in the "regularization during finetuning" framing.

---

## 3. Information Bottleneck in Robotics / VLA

- **CRAFT** (arXiv:2602.12532, Feb 2026): This paper uses a **variational information bottleneck (VIB)** after the vision-language encoder in a VLA, with KL regularization that initially suppresses vision/language signals to force reliance on force modality, then gradually anneals the bottleneck. **This is the closest IB-based competitor** -- it literally applies an information bottleneck to VLA finetuning, though for a different purpose (contact-rich manipulation, not generalization per se).

- **RL Token (RLT)** (arXiv:2604.23073, Physical Intelligence, Apr 2026): Creates an explicit information bottleneck by compressing VLA embeddings into a single "RL token" via an encoder-decoder transformer. The bottleneck forces the token to retain all task-relevant information. Different goal (enabling efficient online RL) but uses the same theoretical motivation.

- **Variational IB for Meta-RL** (Sensors 2023): Older work applying IB to meta-reinforcement learning for robot skill transfer. Improves sample efficiency 200-5000x.

- **IBTM** (OpenReview): Information Bottleneck inspired Token Merging for vision transformers. Not VLA-specific but theoretically adjacent.

**Assessment:** CRAFT is the paper CTM needs to cite and differentiate from most carefully in the IB space. CRAFT uses IB to modulate modality influence; CTM (presumably) uses masking to create an IB that improves visual generalization.

---

## 4. VLA-Pruner (Detailed)

Confirmed: VLA-Pruner (arXiv:2511.16449) is a **plug-and-play inference-time** token pruning method. It does NOT modify training. Its dual-level criterion (semantic + action importance) is designed for computational efficiency during deployment. **It is NOT a close competitor** to CTM's training-time regularization approach, though CTM should cite it in the related work section on token reduction in VLAs.

---

## 5. LIBERO-Plus Benchmark

**Confirmed to exist.** LIBERO-Plus (arXiv:2510.13626) is a robustness benchmark with 10,030 tasks spanning 7 perturbation dimensions (object layout, camera viewpoints, robot initial states, language instructions, light conditions, background textures, sensor noise) with 5 difficulty levels. It appeared as a **CVPR 2026 poster**. GitHub: `github.com/sylvestf/LIBERO-plus`. It is integrated into HuggingFace LeRobot. This is a legitimate and increasingly standard benchmark for VLA robustness evaluation.

---

## 6. SimplerEnv Visual Variants

**Confirmed to exist and is standard.** SimplerEnv (CoRL 2024) provides two evaluation setups:
- **Visual Matching**: sim visuals closely match real training data (in-distribution)
- **Variant Aggregation**: averages across OOD backgrounds, lightings, distractors, table textures, camera poses (out-of-distribution generalization test)

It evaluates on Google Robot and WidowX+Bridge setups. This is widely used in VLA papers (Gen-VLA, TraceVLA, OpenVLA, etc.) and is considered a standard benchmark.

---

## 7. CRL-VLA (arXiv:2602.03445)

**Confirmed to exist.** CRL-VLA: "Continual Vision-Language-Action Learning" by Zeng et al., submitted Feb 3, 2026. It addresses the stability-plasticity tradeoff in continual RL finetuning of VLAs using Goal-Conditioned Value Formulation with a dual-critic architecture. This is about continual learning, not regularization per se, so it is tangentially related but not a direct competitor.

---

## 8. VLM2VLA / Actions as Language

**Confirmed to exist at ICLR 2026.** "Actions as Language: Fine-Tuning VLMs into VLAs Without Catastrophic Forgetting" by Hancock, Wu, Zha, Russakovsky, and Majumdar (Princeton). The method represents robot actions as natural language strings and uses LoRA to minimize backbone modification. It preserves VLM capabilities (85%+ retention on 12 multimodal benchmarks) and enables zero-shot generalization. Available on OpenReview (`openreview.net/forum?id=sFO9d6XSlf`).

---

## 9. Gen-VLA (arXiv:2509.11417)

**Confirmed to exist.** "Enhancing Generalization in Vision-Language-Action Models by Preserving Pretrained Representations" by Grover, Gopalkrishnan, Ai, Christensen, Su, and Li (UC San Diego / Hillbot). Uses: (1) dual-encoder with one frozen encoder, (2) string-based action tokenizer, (3) co-training with VL datasets. Evaluates on **SimplerEnv** (both Visual Matching and Variant Aggregation). Does NOT use token masking. **Close competitor** in the generalization-through-representation-preservation space.

---

## 10. Recent Concurrent Work (Feb-May 2026)

Several important papers the CTM idea should be aware of:

- **Gaze-Regularized VLA** (arXiv:2603.23202, Mar 2026): Uses KL divergence to align transformer attention with human gaze distributions. 4-12% improvements on LIBERO. A different regularization approach but in the same "regularize VLA attention" space.

- **RS-CL / Contrastive Representation Regularization** (arXiv:2510.01711): Robot State-aware Contrastive Loss that aligns VLM representations with proprioceptive states. Uses "view cutoff" (randomly masking feature slices for observation views) -- this is somewhat related to token masking. Evaluated on LIBERO and RoboCasa.

- **"Don't Blind Your VLA"** (arXiv:2510.25616): Identifies attention sink, representation collapse, and domain forgetting during VLA SFT. Proposes Visual Representation Alignment using a frozen teacher with cosine similarity. Evaluated on SimplerEnv. Diagnoses the same problem (VLA representations degrade during finetuning) but proposes a different solution.

- **Knowledge Insulation** (arXiv:2505.23705, Physical Intelligence, NeurIPS 2025): Insulates VLM backbone by not propagating action expert gradients. Trains with discrete FAST tokens for representation quality while using flow matching for continuous actions. Addresses the same root problem of representation degradation during finetuning.

- **VLA-GSE** (arXiv:2605.06175, May 2026): Parameter-efficient finetuning with generalized and specialized expert modules. Very recent.

---

## Summary of Competitive Threats

**Highest threat (must address explicitly):**

1. **"Rethinking VLA Model Scaling" (arXiv:2602.09722)** -- Directly tested sensory dropout in VLA training and found it **hurts performance**. The CTM paper must explain why its approach is different (counterfactual design, finetuning vs. pretraining, targeted vs. random, etc.).

2. **CRAFT (arXiv:2602.12532)** -- Already uses a variational information bottleneck in VLA finetuning. Different application (force-modality focus) but same theoretical framework.

3. **"See What Matters" / GridS (ICML 2026)** -- Connects token pruning to VLA generalization, not just efficiency.

**Medium threat (should cite and differentiate):**

4. **LightVLA** -- Differentiable token pruning during training.
5. **Gen-VLA** -- Preservation-based generalization approach.
6. **"Don't Blind Your VLA"** -- Same problem diagnosis (representation degradation during SFT).
7. **Parameter Merging (arXiv:2512.08333)** -- Competing robust finetuning approach.
8. **FAN Prior (arXiv:2604.01570)** -- Competing regularization-during-finetuning approach.
9. **RS-CL (arXiv:2510.01711)** -- View masking + contrastive regularization.
10. **Knowledge Insulation (NeurIPS 2025)** -- Competing approach to preventing representation degradation.

**Lower threat (cite in related work):**
- VLA-Pruner, VLA-IAP, ETA-VLA, SP-VLA (all inference-time efficiency)
- VLM2VLA, CRL-VLA (different problems: forgetting, continual learning)
- Gaze-Regularized VLA (different regularization signal)

Sources:
- [VLA-Pruner](https://arxiv.org/abs/2511.16449)
- [LightVLA](https://arxiv.org/abs/2509.12594)
- [VLA-IAP](https://arxiv.org/abs/2603.22991)
- [See What Matters / GridS (ICML 2026)](https://icml.cc/virtual/2026/poster/65010)
- [Rethinking VLA Model Scaling](https://arxiv.org/html/2602.09722)
- [Robust Finetuning via Parameter Merging](https://arxiv.org/abs/2512.08333)
- [FAN Prior for VLA Finetuning](https://arxiv.org/html/2604.01570v1)
- [CRAFT: Force-Aware Curriculum Fine-tuning](https://arxiv.org/abs/2602.12532)
- [RL Token](https://arxiv.org/abs/2604.23073)
- [LIBERO-Plus](https://arxiv.org/abs/2510.13626)
- [LIBERO-Plus CVPR 2026](https://cvpr.thecvf.com/virtual/2026/poster/38735)
- [SimplerEnv GitHub](https://github.com/simpler-env/SimplerEnv)
- [CRL-VLA](https://arxiv.org/abs/2602.03445)
- [VLM2VLA / Actions as Language](https://arxiv.org/abs/2509.22195)
- [VLM2VLA OpenReview (ICLR 2026)](https://openreview.net/forum?id=sFO9d6XSlf)
- [Gen-VLA](https://arxiv.org/abs/2509.11417)
- [Gen-VLA Project Page](https://gen-vla.github.io/)
- [Gaze-Regularized VLA](https://arxiv.org/html/2603.23202v1)
- [RS-CL / Contrastive Representation Regularization](https://arxiv.org/html/2510.01711v1)
- [Don't Blind Your VLA](https://arxiv.org/abs/2510.25616)
- [Knowledge Insulation (Physical Intelligence)](https://arxiv.org/abs/2505.23705)
- [VLA-GSE](https://arxiv.org/html/2605.06175v1)
- [ETA-VLA](https://arxiv.org/abs/2603.25766)
- [What Can RL Bring to VLA Generalization](https://arxiv.org/abs/2505.19789)
- [VLA-RFT (ICLR 2026)](https://openreview.net/forum?id=Jaut99EHeu)
- [ICLR 2026 VLA Survey Blog](https://mbreuss.github.io/blog_post_iclr_26_vla.html)
- [VLA-Cache](https://arxiv.org/html/2502.02175v2)

agentId: a6466d84670312cd2 (use SendMessage with to: 'a6466d84670312cd2' to continue this agent)
&lt;usage>total_tokens: 49165
tool_uses: 41
duration_ms: 244929&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c5537a78-4abc-4e7f-94f0-b2ba1d274af4",
  "isSidechain": false,
  "promptId": "251a69dd-0148-46cf-91d6-c922d95174a8",
  "type": "user",
  "uuid": "412eeda4-621c-4d5e-b9da-e6ca6399d999",
  "toolUseResult": {
    "status": "completed",
    "prompt": "You are helping me review an ML research idea about \"token masking as regularization during VLA (Vision-Language-Action) finetuning.\" I need you to search for competitive and concurrent work that the idea may have missed. Use WebSearch extensively.\n\nSearch for the following:\n\n1. **Token masking/dropout in VLAs**: Search \"token masking VLA 2025 2026\", \"visual token dropout robot learning\", \"token pruning VLA generalization\"\n\n2. **VLA robustness/generalization recent work**: Search \"VLA generalization out-of-distribution 2026\", \"vision language action robust finetuning 2026\"\n\n3. **Information bottleneck in robotics/VLA**: Search \"information bottleneck robot learning\", \"information bottleneck VLA\", \"IB regularization vision language action\"\n\n4. **VLA-Pruner**: Search for \"VLA-Pruner temporal visual token pruning\" — the idea mentions this but doesn't detail it. Check if it's a close competitor.\n\n5. **LIBERO-Plus benchmark**: Search \"LIBERO-Plus robustness benchmark VLA\" to verify this exists.\n\n6. **SimplerEnv visual variants**: Search \"SimplerEnv visual variant aggregation VLA evaluation\" to verify this benchmark exists and is standard.\n\n7. **CRL-VLA (arXiv 2602.03445)**: Search for this continual learning VLA paper.\n\n8. **VLM2VLA / Actions as Language (ICLR 2026)**: Verify this exists.\n\n9. **Gen-VLA (arXiv 2509.11417)**: Verify this exists.\n\n10. **Recent arXiv (Feb-May 2026) on VLA regularization**: Search \"VLA regularization arXiv 2026\", \"vision language action model finetuning 2026\" to find any very recent concurrent work.\n\nFor each search, report what you found, whether the papers exist, and whether any of them are close competitors to the proposed \"Counterfactual Token Masking\" idea. Use WebSearch and WebFetch on the most important results.",
    "agentId": "a6466d84670312cd2",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have comprehensive data. Let me compile the final analysis.\n\n---\n\nHere is my comprehensive review of competitive and concurrent work for the \"Counterfactual Token Masking\" (CTM) idea for VLA finetuning, organized by search area.\n\n---\n\n## 1. Token Masking / Dropout in VLAs\n\n**This is the most crowded competitive space.** There is a large and rapidly growing body of work on visual token pruning/masking in VLAs, though most focus on **inference efficiency** rather than **regularization for generalization**:\n\n- **VLA-Pruner** (arXiv:2511.16449, Nov 2025, updated Feb 2026): Temporal-aware dual-level visual token pruning. Uses prefill attention + temporal smoothing of action-decode attention as a plug-and-play **inference-time** method. Focus is efficiency, not regularization. **Not a direct competitor** to CTM's training-time regularization framing.\n\n- **LightVLA** (arXiv:2509.12594, ICRA 2026): Differentiable token pruning using Gumbel softmax for adaptive token selection during **training**. Reduces FLOPs by 59% with 2.9% improvement in success rate. This is closer to CTM since it modifies training, though framed as efficiency rather than regularization.\n\n- **VLA-IAP** (arXiv:2603.22991, Mar 2026): Training-free visual token pruning via interaction alignment. Inference-time only. Not a competitor.\n\n- **\"See What Matters\" / GridS** (ICML 2026): Differentiable grid sample pruning for \"generalizable\" VLA. This paper explicitly connects token pruning to **generalization**, not just efficiency. Uses continuous resampling of visual tokens. Published at a top venue. **Potentially a close competitor** if CTM's story is that token reduction improves generalization.\n\n- **ETA-VLA** (arXiv:2603.25766): Temporal fusion + intra-LLM sparsification. Focused on autonomous driving VLAs. Efficiency-focused.\n\n- **SP-VLA** (arXiv:2506.12723): Joint model scheduling and token pruning. Efficiency-focused.\n\n- **SpecPrune-VLA** (OpenReview): Action-aware self-speculative pruning. Efficiency-focused.\n\n**Key gap CTM could exploit:** Most of these papers frame token reduction as an **efficiency** problem. CTM's framing of token masking as an explicit **regularization** strategy grounded in the information bottleneck principle is relatively novel in the VLA space.\n\n---\n\n## 2. VLA Robustness / Generalization Recent Work\n\n**CRITICAL FINDING -- \"Rethinking VLA Model Scaling\" (arXiv:2602.09722, Feb 2026):** This paper by Wang et al. **directly tested sensory dropout** (stochastically masking visual inputs and proprioception during training with p=0.2) as a regularization technique for VLA scaling. Their finding: **sensory dropout HURT performance**. Disabling visual dropout increased success rates from 84.5% to 85.6%. They conclude \"the natural diversity of the pre-training corpus already serves as an effective regularizer.\" **This is a direct challenge to the CTM premise** and must be addressed in the paper. The CTM paper needs to explain why its approach differs (e.g., counterfactual design, targeted rather than random masking, different training regime, finetuning vs. pretraining context).\n\nOther relevant generalization work:\n- **\"What Can RL Bring to VLA Generalization?\"** (arXiv:2505.19789): RL finetuning (PPO) enhances VLA generalization, especially in execution and semantics.\n- **VLA-RFT** (ICLR 2026): Reinforcement finetuning with world model simulators.\n- **\"Robust Finetuning via Parameter Merging\"** (arXiv:2512.08333, Yadav et al., Berkeley): Weight interpolation between pretrained and finetuned checkpoints. No token masking -- purely weight-space. Uses LIBERO and real-world. **Close competitor** in the \"robust finetuning\" framing.\n- **\"Boosting VLA Finetuning with Feasible Action Neighborhood Prior\"** (arXiv:2604.01570, Apr 2026): KL-divergence regularizer on action distributions using Gaussian priors. Tested on LIBERO and ManiSkill. **Close competitor** in the \"regularization during finetuning\" framing.\n\n---\n\n## 3. Information Bottleneck in Robotics / VLA\n\n- **CRAFT** (arXiv:2602.12532, Feb 2026): This paper uses a **variational information bottleneck (VIB)** after the vision-language encoder in a VLA, with KL regularization that initially suppresses vision/language signals to force reliance on force modality, then gradually anneals the bottleneck. **This is the closest IB-based competitor** -- it literally applies an information bottleneck to VLA finetuning, though for a different purpose (contact-rich manipulation, not generalization per se).\n\n- **RL Token (RLT)** (arXiv:2604.23073, Physical Intelligence, Apr 2026): Creates an explicit information bottleneck by compressing VLA embeddings into a single \"RL token\" via an encoder-decoder transformer. The bottleneck forces the token to retain all task-relevant information. Different goal (enabling efficient online RL) but uses the same theoretical motivation.\n\n- **Variational IB for Meta-RL** (Sensors 2023): Older work applying IB to meta-reinforcement learning for robot skill transfer. Improves sample efficiency 200-5000x.\n\n- **IBTM** (OpenReview): Information Bottleneck inspired Token Merging for vision transformers. Not VLA-specific but theoretically adjacent.\n\n**Assessment:** CRAFT is the paper CTM needs to cite and differentiate from most carefully in the IB space. CRAFT uses IB to modulate modality influence; CTM (presumably) uses masking to create an IB that improves visual generalization.\n\n---\n\n## 4. VLA-Pruner (Detailed)\n\nConfirmed: VLA-Pruner (arXiv:2511.16449) is a **plug-and-play inference-time** token pruning method. It does NOT modify training. Its dual-level criterion (semantic + action importance) is designed for computational efficiency during deployment. **It is NOT a close competitor** to CTM's training-time regularization approach, though CTM should cite it in the related work section on token reduction in VLAs.\n\n---\n\n## 5. LIBERO-Plus Benchmark\n\n**Confirmed to exist.** LIBERO-Plus (arXiv:2510.13626) is a robustness benchmark with 10,030 tasks spanning 7 perturbation dimensions (object layout, camera viewpoints, robot initial states, language instructions, light conditions, background textures, sensor noise) with 5 difficulty levels. It appeared as a **CVPR 2026 poster**. GitHub: `github.com/sylvestf/LIBERO-plus`. It is integrated into HuggingFace LeRobot. This is a legitimate and increasingly standard benchmark for VLA robustness evaluation.\n\n---\n\n## 6. SimplerEnv Visual Variants\n\n**Confirmed to exist and is standard.** SimplerEnv (CoRL 2024) provides two evaluation setups:\n- **Visual Matching**: sim visuals closely match real training data (in-distribution)\n- **Variant Aggregation**: averages across OOD backgrounds, lightings, distractors, table textures, camera poses (out-of-distribution generalization test)\n\nIt evaluates on Google Robot and WidowX+Bridge setups. This is widely used in VLA papers (Gen-VLA, TraceVLA, OpenVLA, etc.) and is considered a standard benchmark.\n\n---\n\n## 7. CRL-VLA (arXiv:2602.03445)\n\n**Confirmed to exist.** CRL-VLA: \"Continual Vision-Language-Action Learning\" by Zeng et al., submitted Feb 3, 2026. It addresses the stability-plasticity tradeoff in continual RL finetuning of VLAs using Goal-Conditioned Value Formulation with a dual-critic architecture. This is about continual learning, not regularization per se, so it is tangentially related but not a direct competitor.\n\n---\n\n## 8. VLM2VLA / Actions as Language\n\n**Confirmed to exist at ICLR 2026.** \"Actions as Language: Fine-Tuning VLMs into VLAs Without Catastrophic Forgetting\" by Hancock, Wu, Zha, Russakovsky, and Majumdar (Princeton). The method represents robot actions as natural language strings and uses LoRA to minimize backbone modification. It preserves VLM capabilities (85%+ retention on 12 multimodal benchmarks) and enables zero-shot generalization. Available on OpenReview (`openreview.net/forum?id=sFO9d6XSlf`).\n\n---\n\n## 9. Gen-VLA (arXiv:2509.11417)\n\n**Confirmed to exist.** \"Enhancing Generalization in Vision-Language-Action Models by Preserving Pretrained Representations\" by Grover, Gopalkrishnan, Ai, Christensen, Su, and Li (UC San Diego / Hillbot). Uses: (1) dual-encoder with one frozen encoder, (2) string-based action tokenizer, (3) co-training with VL datasets. Evaluates on **SimplerEnv** (both Visual Matching and Variant Aggregation). Does NOT use token masking. **Close competitor** in the generalization-through-representation-preservation space.\n\n---\n\n## 10. Recent Concurrent Work (Feb-May 2026)\n\nSeveral important papers the CTM idea should be aware of:\n\n- **Gaze-Regularized VLA** (arXiv:2603.23202, Mar 2026): Uses KL divergence to align transformer attention with human gaze distributions. 4-12% improvements on LIBERO. A different regularization approach but in the same \"regularize VLA attention\" space.\n\n- **RS-CL / Contrastive Representation Regularization** (arXiv:2510.01711): Robot State-aware Contrastive Loss that aligns VLM representations with proprioceptive states. Uses \"view cutoff\" (randomly masking feature slices for observation views) -- this is somewhat related to token masking. Evaluated on LIBERO and RoboCasa.\n\n- **\"Don't Blind Your VLA\"** (arXiv:2510.25616): Identifies attention sink, representation collapse, and domain forgetting during VLA SFT. Proposes Visual Representation Alignment using a frozen teacher with cosine similarity. Evaluated on SimplerEnv. Diagnoses the same problem (VLA representations degrade during finetuning) but proposes a different solution.\n\n- **Knowledge Insulation** (arXiv:2505.23705, Physical Intelligence, NeurIPS 2025): Insulates VLM backbone by not propagating action expert gradients. Trains with discrete FAST tokens for representation quality while using flow matching for continuous actions. Addresses the same root problem of representation degradation during finetuning.\n\n- **VLA-GSE** (arXiv:2605.06175, May 2026): Parameter-efficient finetuning with generalized and specialized expert modules. Very recent.\n\n---\n\n## Summary of Competitive Threats\n\n**Highest threat (must address explicitly):**\n\n1. **\"Rethinking VLA Model Scaling\" (arXiv:2602.09722)** -- Directly tested sensory dropout in VLA training and found it **hurts performance**. The CTM paper must explain why its approach is different (counterfactual design, finetuning vs. pretraining, targeted vs. random, etc.).\n\n2. **CRAFT (arXiv:2602.12532)** -- Already uses a variational information bottleneck in VLA finetuning. Different application (force-modality focus) but same theoretical framework.\n\n3. **\"See What Matters\" / GridS (ICML 2026)** -- Connects token pruning to VLA generalization, not just efficiency.\n\n**Medium threat (should cite and differentiate):**\n\n4. **LightVLA** -- Differentiable token pruning during training.\n5. **Gen-VLA** -- Preservation-based generalization approach.\n6. **\"Don't Blind Your VLA\"** -- Same problem diagnosis (representation degradation during SFT).\n7. **Parameter Merging (arXiv:2512.08333)** -- Competing robust finetuning approach.\n8. **FAN Prior (arXiv:2604.01570)** -- Competing regularization-during-finetuning approach.\n9. **RS-CL (arXiv:2510.01711)** -- View masking + contrastive regularization.\n10. **Knowledge Insulation (NeurIPS 2025)** -- Competing approach to preventing representation degradation.\n\n**Lower threat (cite in related work):**\n- VLA-Pruner, VLA-IAP, ETA-VLA, SP-VLA (all inference-time efficiency)\n- VLM2VLA, CRL-VLA (different problems: forgetting, continual learning)\n- Gaze-Regularized VLA (different regularization signal)\n\nSources:\n- [VLA-Pruner](https://arxiv.org/abs/2511.16449)\n- [LightVLA](https://arxiv.org/abs/2509.12594)\n- [VLA-IAP](https://arxiv.org/abs/2603.22991)\n- [See What Matters / GridS (ICML 2026)](https://icml.cc/virtual/2026/poster/65010)\n- [Rethinking VLA Model Scaling](https://arxiv.org/html/2602.09722)\n- [Robust Finetuning via Parameter Merging](https://arxiv.org/abs/2512.08333)\n- [FAN Prior for VLA Finetuning](https://arxiv.org/html/2604.01570v1)\n- [CRAFT: Force-Aware Curriculum Fine-tuning](https://arxiv.org/abs/2602.12532)\n- [RL Token](https://arxiv.org/abs/2604.23073)\n- [LIBERO-Plus](https://arxiv.org/abs/2510.13626)\n- [LIBERO-Plus CVPR 2026](https://cvpr.thecvf.com/virtual/2026/poster/38735)\n- [SimplerEnv GitHub](https://github.com/simpler-env/SimplerEnv)\n- [CRL-VLA](https://arxiv.org/abs/2602.03445)\n- [VLM2VLA / Actions as Language](https://arxiv.org/abs/2509.22195)\n- [VLM2VLA OpenReview (ICLR 2026)](https://openreview.net/forum?id=sFO9d6XSlf)\n- [Gen-VLA](https://arxiv.org/abs/2509.11417)\n- [Gen-VLA Project Page](https://gen-vla.github.io/)\n- [Gaze-Regularized VLA](https://arxiv.org/html/2603.23202v1)\n- [RS-CL / Contrastive Representation Regularization](https://arxiv.org/html/2510.01711v1)\n- [Don't Blind Your VLA](https://arxiv.org/abs/2510.25616)\n- [Knowledge Insulation (Physical Intelligence)](https://arxiv.org/abs/2505.23705)\n- [VLA-GSE](https://arxiv.org/html/2605.06175v1)\n- [ETA-VLA](https://arxiv.org/abs/2603.25766)\n- [What Can RL Bring to VLA Generalization](https://arxiv.org/abs/2505.19789)\n- [VLA-RFT (ICLR 2026)](https://openreview.net/forum?id=Jaut99EHeu)\n- [ICLR 2026 VLA Survey Blog](https://mbreuss.github.io/blog_post_iclr_26_vla.html)\n- [VLA-Cache](https://arxiv.org/html/2502.02175v2)"
      }
    ],
    "totalDurationMs": 244929,
    "totalTokens": 49165,
    "totalToolUseCount": 41,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3148,
      "cache_read_input_tokens": 41984,
      "output_tokens": 4032,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3148
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4032,
          "cache_read_input_tokens": 41984,
          "cache_creation_input_tokens": 3148,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3148,
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
      "otherToolCount": 41
    }
  },
  "sourceToolAssistantUUID": "c5537a78-4abc-4e7f-94f0-b2ba1d274af4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "38eec20f-28d6-4706-b24b-8f0ea53acfb9",
  "version": "2.1.126",
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
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-13 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "412eeda4-621c-4d5e-b9da-e6ca6399d999",
  "sessionId": "38eec20f-28d6-4706-b24b-8f0ea53acfb9"
}
```

---

### Runtime record

_source line 19_

```json
{
  "type": "ai-title",
  "aiTitle": "Review VLA token masking robustness via theory",
  "sessionId": "38eec20f-28d6-4706-b24b-8f0ea53acfb9"
}
```

---

### Assistant

_source line 20 · 2026-05-13T04:47:13.738Z_

<details><summary>Logged reasoning block</summary>

```text
Excellent. Now I have comprehensive research from all three agents. Let me synthesize the findings and form my independent assessment.

## Key Findings

### Reference Verification
All 8 major papers checked exist and their claims are accurate. Good.

### Critical Competitive Threats

1. **"Rethinking VLA Model Scaling" (arXiv:2602.09722)** — DIRECTLY tested sensory dropout (stochastic masking of visual inputs during training with p=0.2) in VLAs and found it HURT performance. This is a CRITICAL challenge to CTM's premise that the idea does NOT mention at all.


2. **"See What Matters" / GridS (ICML 2026)** — Connects token pruning to VLA generalization beyond just efficiency, published at a top venue, which the idea doesn't address.
3. **CRAFT (arXiv:2602.12532)** — Already applies VIB in VLA finetuning, so the idea's differentiation here is insufficient.
4. **IBTM, AttentionDrop (arXiv:2504.12088), and RoCoDA (arXiv:2411.16)** — These establish that information bottleneck principles, PAC-Bayes bounds for stochastic perturbation, and token-level operations are already well-explored in the literature.
5. **Knowledge Insulation (NeurIPS 2025, Physical Intelligence)** — Yet another existing approach to preventing representation degradation.

Looking at the theoretical foundations, I'm seeing significant overlap with prior work: the information bottleneck-to-token-masking connection isn't novel, VIB applied to VLA finetuning is already done, PAC-Bayes bounds for attention-level masking exist, and counterfactual framing of masking has been established. There's also a citation issue—the PAC-Bayes attribution to Gal & Ghahramani appears incorrect, with McAllester (2013) being the proper source.

The Achille & Soatto claim needs to be reframed from equivalence to approximation, and there's a critical empirical problem: Wang et al.'s February 2026 paper on VLA model scaling directly tested sensory dropout during training and found it degraded performance, suggesting the natural diversity in pre-training data was already sufficient. This contradicts the core premise, and the proposal doesn't even acknowledge this work.

Evaluating novelty across dimensions, the approach combines known techniques—token masking, information bottleneck regularization, and counterfactual framing—applied to VLAs, but each theoretical component already has established precedent in the literature.  The specific combination for VLAs shows some novelty, though it's largely a straightforward adaptation of existing theory to a new domain, similar to what "See What Matters" and GridS already accomplished at ICML 2026. I'm settling on a novelty score of 2.

For feasibility, the resource requirements look plausible, but the empirical evidence from "Rethinking VLA Model Scaling" raises serious concerns about whether the approach would actually work in practice, and the adaptive masking module introduces additional implementation complexity.

The theoretical foundations have some issues too—there's a misattribution with the PAC-Bayes framework and an overstatement about information bottleneck equivalence—which suggests the proofs may not be as solid as presented. Reproducing nine baselines is ambitious given these risks, so I'm scoring feasibility at 3.

The writing itself is clear and well-organized with comprehensive baselines and evaluation plans, though those theoretical missteps do undermine the rigor. That puts clarity at 4. Now I'm considering the potential impact if the approach actually works.

The core contribution—using token masking as a regularization technique for vision-language models—could be valuable, but the theoretical advances are mostly incremental adaptations of existing ideas. The field is crowded with at least six competing approaches already, so even a working method might offer only marginal gains over what's already out there. More concerning is that "Rethinking VLA Model Scaling" directly tested sensory dropout in these models and found it actually hurts performance, which is direct counter-evidence the proposal doesn't address. There's also "See What Matters" and GridS from ICML 2026 that already connect token operations to VLA generalization at a top venue. Given all this, I'm scoring impact at 2-3.

Looking at the specific theoretical claims, each of the four contributions has substantial precedent—RoCoDA uses counterfactual augmentation in robotics, AttentionDrop provides PAC-Bayes bounds for attention masking, and Knowledge Insulation from NeurIPS 2025 tackles representation degradation. The novelty feels overstated when these connections aren't properly differentiated. There are also some attribution issues: the PAC-Bayes bounds should reference McAllester (2013) rather than Gal & Ghahramani (2016), and the information bottleneck claim should be framed as an approximation rather than an equivalence. The work has improved significantly from the first round with better literature coverage and a clearer theoretical framework, but these critical gaps need to be addressed before it's ready. Averaging the scores across reviewers gives around 2.9.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "412eeda4-621c-4d5e-b9da-e6ca6399d999",
  "isSidechain": false,
  "requestId": "req_011CayxgiFwB7YZdwvavb1ma",
  "type": "assistant",
  "uuid": "62ded681-6c7d-4080-9448-d2fd5931356a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "38eec20f-28d6-4706-b24b-8f0ea53acfb9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PwSPNGDWRBqCguGxtwe4E4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3771,
      "cache_creation_input_tokens": 9233,
      "cache_read_input_tokens": 27384,
      "output_tokens": 1801,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9233,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3771,
          "output_tokens": 1801,
          "cache_read_input_tokens": 27384,
          "cache_creation_input_tokens": 9233,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9233
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

_source line 21 · 2026-05-13T04:47:13.847Z_

Now let me search for a few more critical items that emerged from the research — particularly the counter-evidence paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "62ded681-6c7d-4080-9448-d2fd5931356a",
  "isSidechain": false,
  "requestId": "req_011CayxgiFwB7YZdwvavb1ma",
  "type": "assistant",
  "uuid": "968c5585-8402-4415-b2b5-49a754c54938",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "38eec20f-28d6-4706-b24b-8f0ea53acfb9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PwSPNGDWRBqCguGxtwe4E4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3771,
      "cache_creation_input_tokens": 9233,
      "cache_read_input_tokens": 27384,
      "output_tokens": 1801,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9233,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3771,
          "output_tokens": 1801,
          "cache_read_input_tokens": 27384,
          "cache_creation_input_tokens": 9233,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9233
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

_source line 22 · 2026-05-13T04:47:13.848Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_0177iCWHC1SzSRatp6TTtc45`</summary>

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
  "parentUuid": "968c5585-8402-4415-b2b5-49a754c54938",
  "isSidechain": false,
  "requestId": "req_011CayxgiFwB7YZdwvavb1ma",
  "type": "assistant",
  "uuid": "a745c008-9224-4208-bac5-8c27c913a0b3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "38eec20f-28d6-4706-b24b-8f0ea53acfb9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PwSPNGDWRBqCguGxtwe4E4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3771,
      "cache_creation_input_tokens": 9233,
      "cache_read_input_tokens": 27384,
      "output_tokens": 1801,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9233,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3771,
          "output_tokens": 1801,
          "cache_read_input_tokens": 27384,
          "cache_creation_input_tokens": 9233,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9233
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

_source line 23 · 2026-05-13T04:47:13.855Z_

<details><summary>↩ Tool result · `toolu_0177iCWHC1SzSRatp6TTtc45`</summary>

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
  "parentUuid": "a745c008-9224-4208-bac5-8c27c913a0b3",
  "isSidechain": false,
  "promptId": "251a69dd-0148-46cf-91d6-c922d95174a8",
  "type": "user",
  "uuid": "9351d6ff-ca74-4fd4-aec8-4fb9a3f045b6",
  "toolUseResult": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 17
  },
  "sourceToolAssistantUUID": "a745c008-9224-4208-bac5-8c27c913a0b3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "38eec20f-28d6-4706-b24b-8f0ea53acfb9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-13T04:47:17.083Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WDwcoyGn7YwfSGXK8pHybo`</summary>

```json
{
  "query": "\"Rethinking VLA Model Scaling\" sensory dropout visual dropout arXiv 2602"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9351d6ff-ca74-4fd4-aec8-4fb9a3f045b6",
  "isSidechain": false,
  "requestId": "req_011CayxjQds3a6q28EUas29A",
  "type": "assistant",
  "uuid": "5d869f81-b491-4bb1-98a7-5870c9608116",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "38eec20f-28d6-4706-b24b-8f0ea53acfb9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QpZpwtWNeW2kBBzXHriYgq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6093,
      "cache_read_input_tokens": 36617,
      "output_tokens": 183,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6093,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 183,
          "cache_read_input_tokens": 36617,
          "cache_creation_input_tokens": 6093,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6093
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

_source line 25 · 2026-05-13T04:47:17.617Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017gUa67g1bPYWn86yvmibsN`</summary>

```json
{
  "query": "\"See What Matters\" GridS token pruning VLA generalization ICML 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5d869f81-b491-4bb1-98a7-5870c9608116",
  "isSidechain": false,
  "requestId": "req_011CayxjQds3a6q28EUas29A",
  "type": "assistant",
  "uuid": "a052cd2b-4d0b-43ed-915c-3affacd1cd2a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "38eec20f-28d6-4706-b24b-8f0ea53acfb9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QpZpwtWNeW2kBBzXHriYgq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6093,
      "cache_read_input_tokens": 36617,
      "output_tokens": 183,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6093,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 183,
          "cache_read_input_tokens": 36617,
          "cache_creation_input_tokens": 6093,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6093
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

_source line 26 · 2026-05-13T04:47:17.827Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JaL98eKVjv837Pp8HQtAUr`</summary>

```json
{
  "query": "RoCoDA counterfactual data augmentation robot learning demonstrations arXiv 2411"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a052cd2b-4d0b-43ed-915c-3affacd1cd2a",
  "isSidechain": false,
  "requestId": "req_011CayxjQds3a6q28EUas29A",
  "type": "assistant",
  "uuid": "3dab006b-9de2-46c7-bcd1-428e10d515d9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "38eec20f-28d6-4706-b24b-8f0ea53acfb9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QpZpwtWNeW2kBBzXHriYgq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6093,
      "cache_read_input_tokens": 36617,
      "output_tokens": 183,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6093,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 183,
          "cache_read_input_tokens": 36617,
          "cache_creation_input_tokens": 6093,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6093
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

_source line 27 · 2026-05-13T04:47:20.931Z_

<details><summary>↩ Tool result · `toolu_017gUa67g1bPYWn86yvmibsN`</summary>

```text
Web search results for query: ""See What Matters" GridS token pruning VLA generalization ICML 2026"

Links: [{"title":"ICML Poster See What Matters: Differentiable Grid Sample Pruning for Generalizable Vision-Language-Action Model","url":"https://icml.cc/virtual/2026/poster/65010"}]

Great! I found the research paper. Here's what I found:

"See What Matters" addresses Vision-Language-Action (VLA) models that have shown remarkable promise in robotics manipulation, yet their high computational cost hinders real-time deployment.

The research identifies that existing token pruning methods suffer from a fundamental trade-off: aggressive compression using pruning inevitably discards critical geometric details like contact points, leading to severe performance degradation.

To address this, the authors propose the Differentiable Grid Sampler (GridS), a plug-and-play module that performs task-aware, continuous resampling of visual tokens in VLA by adaptively predicting a minimal set of salient coordinates and extracting features via differentiable interpolation, achieving drastic compression.

The paper was presented as a poster at ICML 2026 and focuses on improving the generalization of Vision-Language-Action models through geometry-aware token pruning rather than traditional discrete pruning approaches.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a052cd2b-4d0b-43ed-915c-3affacd1cd2a",
  "isSidechain": false,
  "promptId": "251a69dd-0148-46cf-91d6-c922d95174a8",
  "type": "user",
  "uuid": "16971b36-1bae-4cd9-9edf-e59139f65daa",
  "toolUseResult": {
    "query": "\"See What Matters\" GridS token pruning VLA generalization ICML 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01WEhfW5uV6MAHJrw5zoCkqF",
        "content": [
          {
            "title": "ICML Poster See What Matters: Differentiable Grid Sample Pruning for Generalizable Vision-Language-Action Model",
            "url": "https://icml.cc/virtual/2026/poster/65010"
          }
        ]
      },
      "Great! I found the research paper. Here's what I found:\n\n\"See What Matters\" addresses Vision-Language-Action (VLA) models that have shown remarkable promise in robotics manipulation, yet their high computational cost hinders real-time deployment.\n\nThe research identifies that existing token pruning methods suffer from a fundamental trade-off: aggressive compression using pruning inevitably discards critical geometric details like contact points, leading to severe performance degradation.\n\nTo address this, the authors propose the Differentiable Grid Sampler (GridS), a plug-and-play module that performs task-aware, continuous resampling of visual tokens in VLA by adaptively predicting a minimal set of salient coordinates and extracting features via differentiable interpolation, achieving drastic compression.\n\nThe paper was presented as a poster at ICML 2026 and focuses on improving the generalization of Vision-Language-Action models through geometry-aware token pruning rather than traditional discrete pruning approaches."
    ],
    "durationSeconds": 3.3098282460000483
  },
  "sourceToolAssistantUUID": "a052cd2b-4d0b-43ed-915c-3affacd1cd2a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "38eec20f-28d6-4706-b24b-8f0ea53acfb9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-13T04:47:23.006Z_

<details><summary>↩ Tool result · `toolu_01WDwcoyGn7YwfSGXK8pHybo`</summary>

```text
Web search results for query: ""Rethinking VLA Model Scaling" sensory dropout visual dropout arXiv 2602"

Links: [{"title":"Rethinking Visual-Language-Action Model Scaling: Alignment, Mixture, and Regularization","url":"https://arxiv.org/html/2602.09722"},{"title":"[2602.09722] Rethinking Visual-Language-Action Model Scaling: Alignment, Mixture, and Regularization","url":"https://arxiv.org/abs/2602.09722"},{"title":"Rethinking Visual-Language-Action Model Scaling:","url":"https://arxiv.org/pdf/2602.09722"},{"title":"Recurrent-Depth VLA: Implicit Test-Time Compute Scaling of Vision–Language–Action Models via Latent Iterative Reasoning","url":"https://arxiv.org/html/2602.07845"},{"title":"Rethinking the Practicality of Vision-language-action Model: A Comprehensive Benchmark and An Improved Baseline","url":"https://arxiv.org/html/2602.22663"},{"title":"GigaBrain-0.5M*: a VLA That Learns From World Model-Based Reinforcement Learning","url":"https://arxiv.org/html/2602.12099"},{"title":"[2602.22663] Rethinking the Practicality of Vision-language-action Model: A Comprehensive Benchmark and An Improved Baseline","url":"https://arxiv.org/abs/2602.22663"},{"title":"[2602.12281v2] Scaling Verification Can Be More Effective than Scaling Policy Learning for Vision-Language-Action Alignment","url":"https://arxiv.org/abs/2602.12281v2"},{"title":"[2602.07845] Recurrent-Depth VLA: Implicit Test-Time Compute Scaling of Vision-Language-Action Models via Latent Iterative Reasoning","url":"https://arxiv.org/abs/2602.07845"},{"title":"VLANeXt: Recipes for Building Strong VLA Models","url":"https://arxiv.org/html/2602.18532"}]

I found the paper! Here are the key findings from the search results:

The paper presents a systematic study that disentangles the scaling recipe for VLAs (Vision-Language-Action models) trained on heterogeneous robot data.

The analysis centers on three key design dimensions: Physical Alignment, Embodiment Mixture, and Training Regularization.

**Key Findings:**

1. **Physical Alignment**: A unified end-effector (EEF)-relative action representation is critical for robust cross-embodiment transfer.

2. **Embodiment Mixture**: Naively pooling heterogeneous robot datasets often induces negative transfer rather than gains, underscoring the fragility of indiscriminate data scaling.

3. **Training Regularization**: Intuitive strategies, such as sensory dropout and multi-stage fine-tuning, do not consistently improve performance at scale.

The paper also introduces a Grouped Blind Ensemble protocol that blinds operators to model identity and separates policy execution from outcome judgment, reducing experimenter bias.

The paper is titled "Rethinking Visual-Language-Action Model Scaling: Alignment, Mixture, and Regularization" and was published on arXiv on February 10, 2026 (arXiv:2602.09722).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5d869f81-b491-4bb1-98a7-5870c9608116",
  "isSidechain": false,
  "promptId": "251a69dd-0148-46cf-91d6-c922d95174a8",
  "type": "user",
  "uuid": "ccbef060-3468-49bf-831d-9d082cf9c542",
  "toolUseResult": {
    "query": "\"Rethinking VLA Model Scaling\" sensory dropout visual dropout arXiv 2602",
    "results": [
      {
        "tool_use_id": "srvtoolu_01VmHNwPgcVWozJAMFCao7kC",
        "content": [
          {
            "title": "Rethinking Visual-Language-Action Model Scaling: Alignment, Mixture, and Regularization",
            "url": "https://arxiv.org/html/2602.09722"
          },
          {
            "title": "[2602.09722] Rethinking Visual-Language-Action Model Scaling: Alignment, Mixture, and Regularization",
            "url": "https://arxiv.org/abs/2602.09722"
          },
          {
            "title": "Rethinking Visual-Language-Action Model Scaling:",
            "url": "https://arxiv.org/pdf/2602.09722"
          },
          {
            "title": "Recurrent-Depth VLA: Implicit Test-Time Compute Scaling of Vision–Language–Action Models via Latent Iterative Reasoning",
            "url": "https://arxiv.org/html/2602.07845"
          },
          {
            "title": "Rethinking the Practicality of Vision-language-action Model: A Comprehensive Benchmark and An Improved Baseline",
            "url": "https://arxiv.org/html/2602.22663"
          },
          {
            "title": "GigaBrain-0.5M*: a VLA That Learns From World Model-Based Reinforcement Learning",
            "url": "https://arxiv.org/html/2602.12099"
          },
          {
            "title": "[2602.22663] Rethinking the Practicality of Vision-language-action Model: A Comprehensive Benchmark and An Improved Baseline",
            "url": "https://arxiv.org/abs/2602.22663"
          },
          {
            "title": "[2602.12281v2] Scaling Verification Can Be More Effective than Scaling Policy Learning for Vision-Language-Action Alignment",
            "url": "https://arxiv.org/abs/2602.12281v2"
          },
          {
            "title": "[2602.07845] Recurrent-Depth VLA: Implicit Test-Time Compute Scaling of Vision-Language-Action Models via Latent Iterative Reasoning",
            "url": "https://arxiv.org/abs/2602.07845"
          },
          {
            "title": "VLANeXt: Recipes for Building Strong VLA Models",
            "url": "https://arxiv.org/html/2602.18532"
          }
        ]
      },
      "I found the paper! Here are the key findings from the search results:\n\nThe paper presents a systematic study that disentangles the scaling recipe for VLAs (Vision-Language-Action models) trained on heterogeneous robot data.\n\nThe analysis centers on three key design dimensions: Physical Alignment, Embodiment Mixture, and Training Regularization.\n\n**Key Findings:**\n\n1. **Physical Alignment**: A unified end-effector (EEF)-relative action representation is critical for robust cross-embodiment transfer.\n\n2. **Embodiment Mixture**: Naively pooling heterogeneous robot datasets often induces negative transfer rather than gains, underscoring the fragility of indiscriminate data scaling.\n\n3. **Training Regularization**: Intuitive strategies, such as sensory dropout and multi-stage fine-tuning, do not consistently improve performance at scale.\n\nThe paper also introduces a Grouped Blind Ensemble protocol that blinds operators to model identity and separates policy execution from outcome judgment, reducing experimenter bias.\n\nThe paper is titled \"Rethinking Visual-Language-Action Model Scaling: Alignment, Mixture, and Regularization\" and was published on arXiv on February 10, 2026 (arXiv:2602.09722)."
    ],
    "durationSeconds": 5.919803459000017
  },
  "sourceToolAssistantUUID": "5d869f81-b491-4bb1-98a7-5870c9608116",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "38eec20f-28d6-4706-b24b-8f0ea53acfb9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-13T04:47:25.726Z_

<details><summary>↩ Tool result · `toolu_01JaL98eKVjv837Pp8HQtAUr`</summary>

```text
Web search results for query: "RoCoDA counterfactual data augmentation robot learning demonstrations arXiv 2411"

Links: [{"title":"RoCoDA: Counterfactual Data Augmentation for Data-Efficient Robot Learning from Demonstrations","url":"https://arxiv.org/html/2411.16959v1"},{"title":"[2411.16959] RoCoDA: Counterfactual Data Augmentation for Data-Efficient Robot Learning from Demonstrations","url":"https://arxiv.org/abs/2411.16959"},{"title":"RoCoDA: Counterfactual Data Augmentation for Data-Efficient Robot Learning from Demonstrations | alphaXiv","url":"https://www.alphaxiv.org/resources/2411.16959v2"},{"title":"RoCoDA: Counterfactual Data Augmentation","url":"https://rocoda.github.io/"},{"title":"RoCoDA: Counterfactual Data Augmentation for Data-Efficient Robot Learning from Demonstrations","url":"https://www.researchgate.net/publication/386143974_RoCoDA_Counterfactual_Data_Augmentation_for_Data-Efficient_Robot_Learning_from_Demonstrations"},{"title":"[Literature Review] RoCoDA: Counterfactual Data Augmentation for Data-Efficient Robot Learning from Demonstrations","url":"https://www.themoonlight.io/en/review/rocoda-counterfactual-data-augmentation-for-data-efficient-robot-learning-from-demonstrations"},{"title":"RoCoDA: Counterfactual Data Augmentation for Data-Efficient Robot Learning from Demonstrations | Request PDF","url":"https://www.researchgate.net/publication/395230290_RoCoDA_Counterfactual_Data_Augmentation_for_Data-Efficient_Robot_Learning_from_Demonstrations"},{"title":"RoCoDA: Counterfactual Data Augmentation for Data-Efficient Robot Learning from Demonstrations","url":"https://powerdrill.ai/discover/discover-RoCoDA-Counterfactual-Data-cm40dg4qudokh01dm12k9bh5v"},{"title":"Computer Science Nov 2024","url":"https://arxiv.org/list/cs/2024-11?skip=7400&show=1000"},{"title":"[2304.13431v3] Implicit Counterfactual Data Augmentation for Robust Learning","url":"https://arxiv.org/abs/2304.13431v3"}]

I found comprehensive information about the RoCoDA paper. Here's what the search revealed:

## RoCoDA: Counterfactual Data Augmentation for Robot Learning

RoCoDA is a novel method that unifies the concepts of invariance, equivariance, and causality within a single framework to enhance data augmentation for imitation learning.

### Key Features

RoCoDA leverages causal invariance by modifying task-irrelevant subsets of the environment state without affecting the policy's output, and simultaneously exploits SE(3) equivariance by applying rigid body transformations to object poses and adjusting corresponding actions to generate synthetic demonstrations.

The pipeline consists of 5 augmentations applied in tandem – causally invariant counterfactual data augmentation, SE(3) equivariant object state and trajectory augmentation, translation and scale invariance (resize and crop), hue invariance (color jitter), and observation noise invariance (proprioception noise).

### Results

The research validates RoCoDA through extensive experiments on five robotic manipulation tasks, demonstrating improvements in policy performance, generalization, and sample efficiency compared to state-of-the-art data augmentation methods, with policies exhibiting robust generalization to unseen object poses, textures, and the presence of distractors.

Notably, policies trained with RoCoDA exhibit emergent behavior such as re-grasping, indicating policies possess a deeper understanding of task dynamics.

### Publication

The paper (arXiv:2411.16959) was accepted to the 2025 IEEE International Conference on Robotics and Automation (ICRA), with authors Ezra Ameperosa, Jeremy A. Collins, Mrinal Jain, and Animesh Garg.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3dab006b-9de2-46c7-bcd1-428e10d515d9",
  "isSidechain": false,
  "promptId": "251a69dd-0148-46cf-91d6-c922d95174a8",
  "type": "user",
  "uuid": "edf0fc50-e05d-4d0a-8af3-13860441d94a",
  "toolUseResult": {
    "query": "RoCoDA counterfactual data augmentation robot learning demonstrations arXiv 2411",
    "results": [
      {
        "tool_use_id": "srvtoolu_01ShbSZQRGKTGVY3zDztrGsX",
        "content": [
          {
            "title": "RoCoDA: Counterfactual Data Augmentation for Data-Efficient Robot Learning from Demonstrations",
            "url": "https://arxiv.org/html/2411.16959v1"
          },
          {
            "title": "[2411.16959] RoCoDA: Counterfactual Data Augmentation for Data-Efficient Robot Learning from Demonstrations",
            "url": "https://arxiv.org/abs/2411.16959"
          },
          {
            "title": "RoCoDA: Counterfactual Data Augmentation for Data-Efficient Robot Learning from Demonstrations | alphaXiv",
            "url": "https://www.alphaxiv.org/resources/2411.16959v2"
          },
          {
            "title": "RoCoDA: Counterfactual Data Augmentation",
            "url": "https://rocoda.github.io/"
          },
          {
            "title": "RoCoDA: Counterfactual Data Augmentation for Data-Efficient Robot Learning from Demonstrations",
            "url": "https://www.researchgate.net/publication/386143974_RoCoDA_Counterfactual_Data_Augmentation_for_Data-Efficient_Robot_Learning_from_Demonstrations"
          },
          {
            "title": "[Literature Review] RoCoDA: Counterfactual Data Augmentation for Data-Efficient Robot Learning from Demonstrations",
            "url": "https://www.themoonlight.io/en/review/rocoda-counterfactual-data-augmentation-for-data-efficient-robot-learning-from-demonstrations"
          },
          {
            "title": "RoCoDA: Counterfactual Data Augmentation for Data-Efficient Robot Learning from Demonstrations | Request PDF",
            "url": "https://www.researchgate.net/publication/395230290_RoCoDA_Counterfactual_Data_Augmentation_for_Data-Efficient_Robot_Learning_from_Demonstrations"
          },
          {
            "title": "RoCoDA: Counterfactual Data Augmentation for Data-Efficient Robot Learning from Demonstrations",
            "url": "https://powerdrill.ai/discover/discover-RoCoDA-Counterfactual-Data-cm40dg4qudokh01dm12k9bh5v"
          },
          {
            "title": "Computer Science Nov 2024",
            "url": "https://arxiv.org/list/cs/2024-11?skip=7400&show=1000"
          },
          {
            "title": "[2304.13431v3] Implicit Counterfactual Data Augmentation for Robust Learning",
            "url": "https://arxiv.org/abs/2304.13431v3"
          }
        ]
      },
      "I found comprehensive information about the RoCoDA paper. Here's what the search revealed:\n\n## RoCoDA: Counterfactual Data Augmentation for Robot Learning\n\nRoCoDA is a novel method that unifies the concepts of invariance, equivariance, and causality within a single framework to enhance data augmentation for imitation learning.\n\n### Key Features\n\nRoCoDA leverages causal invariance by modifying task-irrelevant subsets of the environment state without affecting the policy's output, and simultaneously exploits SE(3) equivariance by applying rigid body transformations to object poses and adjusting corresponding actions to generate synthetic demonstrations.\n\nThe pipeline consists of 5 augmentations applied in tandem – causally invariant counterfactual data augmentation, SE(3) equivariant object state and trajectory augmentation, translation and scale invariance (resize and crop), hue invariance (color jitter), and observation noise invariance (proprioception noise).\n\n### Results\n\nThe research validates RoCoDA through extensive experiments on five robotic manipulation tasks, demonstrating improvements in policy performance, generalization, and sample efficiency compared to state-of-the-art data augmentation methods, with policies exhibiting robust generalization to unseen object poses, textures, and the presence of distractors.\n\nNotably, policies trained with RoCoDA exhibit emergent behavior such as re-grasping, indicating policies possess a deeper understanding of task dynamics.\n\n### Publication\n\nThe paper (arXiv:2411.16959) was accepted to the 2025 IEEE International Conference on Robotics and Automation (ICRA), with authors Ezra Ameperosa, Jeremy A. Collins, Mrinal Jain, and Animesh Garg."
    ],
    "durationSeconds": 7.8964010329999725
  },
  "sourceToolAssistantUUID": "3dab006b-9de2-46c7-bcd1-428e10d515d9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "38eec20f-28d6-4706-b24b-8f0ea53acfb9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 30_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-13 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "edf0fc50-e05d-4d0a-8af3-13860441d94a",
  "sessionId": "38eec20f-28d6-4706-b24b-8f0ea53acfb9"
}
```

---

### Runtime record

_source line 31_

```json
{
  "type": "ai-title",
  "aiTitle": "Review VLA token masking robustness via theory",
  "sessionId": "38eec20f-28d6-4706-b24b-8f0ea53acfb9"
}
```

---

### Assistant

_source line 32 · 2026-05-13T04:47:29.766Z_

<details><summary>Logged reasoning block</summary>

```text
Let me now fetch the key paper "Rethinking VLA Model Scaling" to understand exactly what they found about sensory dropout, as this is critical counter-evidence.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "edf0fc50-e05d-4d0a-8af3-13860441d94a",
  "isSidechain": false,
  "requestId": "req_011CayxkHDABs1KczrT8uR3a",
  "type": "assistant",
  "uuid": "6ce9089c-b4b9-49cd-a07c-fd0b23b6c85c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "38eec20f-28d6-4706-b24b-8f0ea53acfb9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J8pCuPJukkXZTP4dq6i7tc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2445,
      "cache_read_input_tokens": 42710,
      "output_tokens": 148,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2445,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 148,
          "cache_read_input_tokens": 42710,
          "cache_creation_input_tokens": 2445,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2445
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

_source line 33 · 2026-05-13T04:47:30.320Z_

Let me read the critical counter-evidence paper in detail, plus verify a few more items.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6ce9089c-b4b9-49cd-a07c-fd0b23b6c85c",
  "isSidechain": false,
  "requestId": "req_011CayxkHDABs1KczrT8uR3a",
  "type": "assistant",
  "uuid": "5a66522c-d507-4fa1-8d94-0fd3a4a36f32",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "38eec20f-28d6-4706-b24b-8f0ea53acfb9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J8pCuPJukkXZTP4dq6i7tc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2445,
      "cache_read_input_tokens": 42710,
      "output_tokens": 148,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2445,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 148,
          "cache_read_input_tokens": 42710,
          "cache_creation_input_tokens": 2445,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2445
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

_source line 34 · 2026-05-13T04:47:30.508Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_017HFV2LCyNWUeg9HhvJzeE4`</summary>

```json
{
  "query": "select:WebFetch",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5a66522c-d507-4fa1-8d94-0fd3a4a36f32",
  "isSidechain": false,
  "requestId": "req_011CayxkHDABs1KczrT8uR3a",
  "type": "assistant",
  "uuid": "6c3d792e-ec41-4618-95e0-930ed0bbd08e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "38eec20f-28d6-4706-b24b-8f0ea53acfb9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J8pCuPJukkXZTP4dq6i7tc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2445,
      "cache_read_input_tokens": 42710,
      "output_tokens": 148,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2445,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 148,
          "cache_read_input_tokens": 42710,
          "cache_creation_input_tokens": 2445,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2445
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

_source line 35 · 2026-05-13T04:47:30.510Z_

<details><summary>↩ Tool result · `toolu_017HFV2LCyNWUeg9HhvJzeE4`</summary>

````text
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
  "parentUuid": "6c3d792e-ec41-4618-95e0-930ed0bbd08e",
  "isSidechain": false,
  "promptId": "251a69dd-0148-46cf-91d6-c922d95174a8",
  "type": "user",
  "uuid": "2e7ee4a6-839c-458e-bfc6-a134c60e13f4",
  "toolUseResult": {
    "matches": [
      "WebFetch"
    ],
    "query": "select:WebFetch",
    "total_deferred_tools": 17
  },
  "sourceToolAssistantUUID": "6c3d792e-ec41-4618-95e0-930ed0bbd08e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "38eec20f-28d6-4706-b24b-8f0ea53acfb9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 36 · 2026-05-13T04:47:30.569Z_

```json
{
  "parentUuid": "2e7ee4a6-839c-458e-bfc6-a134c60e13f4",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "2521bcd1-6baa-4671-9686-e652778c88bb",
  "timestamp": "2026-05-13T04:47:30.569Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "38eec20f-28d6-4706-b24b-8f0ea53acfb9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 37 · 2026-05-13T04:47:35.331Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Aux8NQcZJ6DpitfBY4ZkjX`</summary>

```json
{
  "url": "https://arxiv.org/html/2602.09722",
  "prompt": "Find the specific section about \"sensory dropout\" or \"visual dropout\" as a training regularization technique. What exactly did they test? What masking probability did they use? What was the result — did it help or hurt VLA performance? Provide exact numbers if available. Also describe any other regularization techniques they tested and their results. Quote the relevant passages."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2521bcd1-6baa-4671-9686-e652778c88bb",
  "isSidechain": false,
  "requestId": "req_011CayxkdvbkwxsNGpzntJk9",
  "type": "assistant",
  "uuid": "e69dfc30-c0cf-4265-83c3-6f792e3d2ad1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "38eec20f-28d6-4706-b24b-8f0ea53acfb9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PMDpTtm7t66bAEUT1EnTNF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 769,
      "cache_read_input_tokens": 45155,
      "output_tokens": 335,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 769,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 335,
          "cache_read_input_tokens": 45155,
          "cache_creation_input_tokens": 769,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 769
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

_source line 38 · 2026-05-13T04:47:37.285Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_0133LX4eNtsXm3xotAp55qiB`</summary>

```json
{
  "url": "https://icml.cc/virtual/2026/poster/65010",
  "prompt": "Extract all details about the \"See What Matters\" / GridS paper: authors, exact contribution, how it connects token pruning to VLA generalization, key results, and whether it provides theoretical analysis. What benchmarks does it evaluate on?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e69dfc30-c0cf-4265-83c3-6f792e3d2ad1",
  "isSidechain": false,
  "requestId": "req_011CayxkdvbkwxsNGpzntJk9",
  "type": "assistant",
  "uuid": "90030f0e-074b-4479-b3ae-da57e7672060",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "38eec20f-28d6-4706-b24b-8f0ea53acfb9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PMDpTtm7t66bAEUT1EnTNF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 769,
      "cache_read_input_tokens": 45155,
      "output_tokens": 335,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 769,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 335,
          "cache_read_input_tokens": 45155,
          "cache_creation_input_tokens": 769,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 769
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

_source line 39 · 2026-05-13T04:47:37.908Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QsRThbNw7p2aimTE3e3VGT`</summary>

```json
{
  "query": "AttentionDrop PAC-Bayes generalization bound transformer attention masking regularization arXiv 2504"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "90030f0e-074b-4479-b3ae-da57e7672060",
  "isSidechain": false,
  "requestId": "req_011CayxkdvbkwxsNGpzntJk9",
  "type": "assistant",
  "uuid": "016f3690-f93c-48b1-8354-a102665a8ef2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "38eec20f-28d6-4706-b24b-8f0ea53acfb9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PMDpTtm7t66bAEUT1EnTNF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 769,
      "cache_read_input_tokens": 45155,
      "output_tokens": 335,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 769,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 335,
          "cache_read_input_tokens": 45155,
          "cache_creation_input_tokens": 769,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 769
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

_source line 40 · 2026-05-13T04:47:40.019Z_

<details><summary>↩ Tool result · `toolu_0133LX4eNtsXm3xotAp55qiB`</summary>

```text
# GridS Paper Summary

**Authors:** Yixu Feng, Zinan Zhao, Yanxiang Ma, Chenghao Xia, Chengbin Du, Yunke Wang, Chang Xu

**Core Contribution:**
The paper introduces Differentiable Grid Sampler (GridS), described as "a plug-and-play module that performs task-aware, continuous resampling of visual tokens in VLA." Rather than treating compression as simple token removal, the approach recasts it as geometry-aware resampling in the vision encoder.

**Connection to VLA Generalization:**
The authors identify a key limitation in existing methods: aggressive pruning removes critical geometric details like contact points, degrading performance. GridS addresses this by adaptively selecting salient spatial coordinates and using differentiable interpolation to preserve essential spatial information needed for robotic manipulation.

**Key Results:**
- Achieves 76% FLOP reduction with no success rate degradation
- Uses fewer than 10% of original visual tokens
- Demonstrates "the lowest feasible visual token count reported to date"

**Benchmarks Evaluated:**
- LIBERO benchmark
- Real robotic platform experiments

**Theoretical Analysis:**
The document excerpt does not indicate whether theoretical analysis is provided beyond the methodology description.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "90030f0e-074b-4479-b3ae-da57e7672060",
  "isSidechain": false,
  "promptId": "251a69dd-0148-46cf-91d6-c922d95174a8",
  "type": "user",
  "uuid": "24673e71-a44d-44d3-b5aa-c692d4d4259e",
  "toolUseResult": {
    "bytes": 86857,
    "code": 200,
    "codeText": "OK",
    "result": "# GridS Paper Summary\n\n**Authors:** Yixu Feng, Zinan Zhao, Yanxiang Ma, Chenghao Xia, Chengbin Du, Yunke Wang, Chang Xu\n\n**Core Contribution:**\nThe paper introduces Differentiable Grid Sampler (GridS), described as \"a plug-and-play module that performs task-aware, continuous resampling of visual tokens in VLA.\" Rather than treating compression as simple token removal, the approach recasts it as geometry-aware resampling in the vision encoder.\n\n**Connection to VLA Generalization:**\nThe authors identify a key limitation in existing methods: aggressive pruning removes critical geometric details like contact points, degrading performance. GridS addresses this by adaptively selecting salient spatial coordinates and using differentiable interpolation to preserve essential spatial information needed for robotic manipulation.\n\n**Key Results:**\n- Achieves 76% FLOP reduction with no success rate degradation\n- Uses fewer than 10% of original visual tokens\n- Demonstrates \"the lowest feasible visual token count reported to date\"\n\n**Benchmarks Evaluated:**\n- LIBERO benchmark\n- Real robotic platform experiments\n\n**Theoretical Analysis:**\nThe document excerpt does not indicate whether theoretical analysis is provided beyond the methodology description.",
    "durationMs": 2729,
    "url": "https://icml.cc/virtual/2026/poster/65010"
  },
  "sourceToolAssistantUUID": "90030f0e-074b-4479-b3ae-da57e7672060",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "38eec20f-28d6-4706-b24b-8f0ea53acfb9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-13T04:47:40.892Z_

<details><summary>↩ Tool result · `toolu_01Aux8NQcZJ6DpitfBY4ZkjX`</summary>

```text
# Sensory Dropout and Training Regularization Results

## Dropout Testing

The researchers tested sensory dropout with specific masking probabilities:

**Visual Dropout:** They evaluated "dropping of each camera view with p=0.2" during pretraining.

**Proprioceptive Dropout:** They tested "mask proprioception by zeroing the input proprioceptive vector with probability p=0.2."

## Results: Dropout Did NOT Help

Contrary to expectations, the findings were striking. The paper states: "Stochastic modality dropout does not provide a consistent improvement. Disabling visual dropout (pview=0) increases success to 85.6% versus the balanced baseline (84.5%)."

They also found that "heavy proprioceptive masking reduces performance." Testing showed removing state masking entirely (p=0) yielded 85.6% success compared to 84.5% with both modalities masked.

**Conclusion:** The researchers concluded that "the natural diversity of the pre-training corpus already serves as an effective regularizer, making additional noise injection unnecessary, or even harmful."

## Curriculum Learning: Also Unnecessary

They tested two-stage training but found it unhelpful. Direct end-to-end training achieved 85.8% success, outperforming the multi-stage curriculum approach. They noted: "Directly fine-tuning the full model end-to-end...attains the best average success."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e69dfc30-c0cf-4265-83c3-6f792e3d2ad1",
  "isSidechain": false,
  "promptId": "251a69dd-0148-46cf-91d6-c922d95174a8",
  "type": "user",
  "uuid": "b4b2e134-6ad8-4eae-8aac-4c13ef527a58",
  "toolUseResult": {
    "bytes": 285514,
    "code": 200,
    "codeText": "OK",
    "result": "# Sensory Dropout and Training Regularization Results\n\n## Dropout Testing\n\nThe researchers tested sensory dropout with specific masking probabilities:\n\n**Visual Dropout:** They evaluated \"dropping of each camera view with p=0.2\" during pretraining.\n\n**Proprioceptive Dropout:** They tested \"mask proprioception by zeroing the input proprioceptive vector with probability p=0.2.\"\n\n## Results: Dropout Did NOT Help\n\nContrary to expectations, the findings were striking. The paper states: \"Stochastic modality dropout does not provide a consistent improvement. Disabling visual dropout (pview=0) increases success to 85.6% versus the balanced baseline (84.5%).\"\n\nThey also found that \"heavy proprioceptive masking reduces performance.\" Testing showed removing state masking entirely (p=0) yielded 85.6% success compared to 84.5% with both modalities masked.\n\n**Conclusion:** The researchers concluded that \"the natural diversity of the pre-training corpus already serves as an effective regularizer, making additional noise injection unnecessary, or even harmful.\"\n\n## Curriculum Learning: Also Unnecessary\n\nThey tested two-stage training but found it unhelpful. Direct end-to-end training achieved 85.8% success, outperforming the multi-stage curriculum approach. They noted: \"Directly fine-tuning the full model end-to-end...attains the best average success.\"",
    "durationMs": 5560,
    "url": "https://arxiv.org/html/2602.09722"
  },
  "sourceToolAssistantUUID": "e69dfc30-c0cf-4265-83c3-6f792e3d2ad1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "38eec20f-28d6-4706-b24b-8f0ea53acfb9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-13T04:47:45.266Z_

<details><summary>↩ Tool result · `toolu_01QsRThbNw7p2aimTE3e3VGT`</summary>

```text
Web search results for query: "AttentionDrop PAC-Bayes generalization bound transformer attention masking regularization arXiv 2504"

Links: [{"title":"AttentionDrop: A Novel Regularization Method for Transformer Models","url":"https://arxiv.org/html/2504.12088v2"},{"title":"A Novel Regularization Method for Transformer Models","url":"https://arxiv.org/pdf/2504.12088"},{"title":"[2504.12088] AttentionDrop: A Novel Regularization Method for Transformer Models","url":"https://arxiv.org/abs/2504.12088"},{"title":"A Regularization Method for Fully-Connected Self-Attention ...","url":"https://arxiv.org/pdf/1907.11065"},{"title":"Pay Attention to Attention Distribution: A New Local Lipschitz Bound for Transformers","url":"https://arxiv.org/html/2507.07814v1"},{"title":"Learning Linear Attention in Polynomial Time","url":"https://arxiv.org/html/2410.10101v2"},{"title":"On the Role of Attention Masks and LayerNorm in Transformers","url":"https://arxiv.org/html/2405.18781v1"},{"title":"Crisp Attention: Regularizing Transformers via Structured Sparsity","url":"https://arxiv.org/html/2508.06016v1"},{"title":"[PDF] DropAttention: A Regularization Method for Fully-Connected Self-Attention Networks | Semantic Scholar","url":"https://www.semanticscholar.org/paper/DropAttention:-A-Regularization-Method-for-Networks-Lin-Liu/910aea4a020c329afb8b8a948abaafdf9ebcab3f"},{"title":"Dissecting the Interplay of Attention Paths in a Statistical Mechanics Theory of Transformers","url":"https://arxiv.org/html/2405.15926v2"}]

I found the paper you were looking for! Here are the key findings:

## AttentionDrop: A Novel Regularization Method for Transformer Models

AttentionDrop is the first regularization framework that directly perturbs self-attention distributions. It features three different variants that operate directly on self-attention distributions: Hard Attention Masking randomly zeroes out top-k attention logits per query to encourage diverse context utilization, Blurred Attention Smoothing applies a dynamic Gaussian convolution over attention logits to diffuse overly peaked distributions, and Consistency-Regularized AttentionDrop enforces output stability under multiple independent AttentionDrop perturbations via a KL-based consistency loss.

### Theoretical Contributions

The paper derives PAC-Bayes generalization bounds to show how attention-level noise increases posterior entropy and tightens risk bounds, by analyzing the effect on gradient variance. Injecting noise into attention distributions serves not only as a regularizer but also theoretically reduces generalization error bounds via PAC-Bayes.

### Empirical Results

Through theoretical analysis and extensive experiments, the paper demonstrated consistent improvements in generalization, calibration, and robustness across vision and translation benchmarks.

The paper is available on arXiv at 2504.12088 (April 2025).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "016f3690-f93c-48b1-8354-a102665a8ef2",
  "isSidechain": false,
  "promptId": "251a69dd-0148-46cf-91d6-c922d95174a8",
  "type": "user",
  "uuid": "00f5cd8d-a181-4734-aa68-d62a8119d7f2",
  "toolUseResult": {
    "query": "AttentionDrop PAC-Bayes generalization bound transformer attention masking regularization arXiv 2504",
    "results": [
      {
        "tool_use_id": "srvtoolu_01PmgYP2G9LJqsyQCSdDy5VL",
        "content": [
          {
            "title": "AttentionDrop: A Novel Regularization Method for Transformer Models",
            "url": "https://arxiv.org/html/2504.12088v2"
          },
          {
            "title": "A Novel Regularization Method for Transformer Models",
            "url": "https://arxiv.org/pdf/2504.12088"
          },
          {
            "title": "[2504.12088] AttentionDrop: A Novel Regularization Method for Transformer Models",
            "url": "https://arxiv.org/abs/2504.12088"
          },
          {
            "title": "A Regularization Method for Fully-Connected Self-Attention ...",
            "url": "https://arxiv.org/pdf/1907.11065"
          },
          {
            "title": "Pay Attention to Attention Distribution: A New Local Lipschitz Bound for Transformers",
            "url": "https://arxiv.org/html/2507.07814v1"
          },
          {
            "title": "Learning Linear Attention in Polynomial Time",
            "url": "https://arxiv.org/html/2410.10101v2"
          },
          {
            "title": "On the Role of Attention Masks and LayerNorm in Transformers",
            "url": "https://arxiv.org/html/2405.18781v1"
          },
          {
            "title": "Crisp Attention: Regularizing Transformers via Structured Sparsity",
            "url": "https://arxiv.org/html/2508.06016v1"
          },
          {
            "title": "[PDF] DropAttention: A Regularization Method for Fully-Connected Self-Attention Networks | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/DropAttention:-A-Regularization-Method-for-Networks-Lin-Liu/910aea4a020c329afb8b8a948abaafdf9ebcab3f"
          },
          {
            "title": "Dissecting the Interplay of Attention Paths in a Statistical Mechanics Theory of Transformers",
            "url": "https://arxiv.org/html/2405.15926v2"
          }
        ]
      },
      "I found the paper you were looking for! Here are the key findings:\n\n## AttentionDrop: A Novel Regularization Method for Transformer Models\n\nAttentionDrop is the first regularization framework that directly perturbs self-attention distributions. It features three different variants that operate directly on self-attention distributions: Hard Attention Masking randomly zeroes out top-k attention logits per query to encourage diverse context utilization, Blurred Attention Smoothing applies a dynamic Gaussian convolution over attention logits to diffuse overly peaked distributions, and Consistency-Regularized AttentionDrop enforces output stability under multiple independent AttentionDrop perturbations via a KL-based consistency loss.\n\n### Theoretical Contributions\n\nThe paper derives PAC-Bayes generalization bounds to show how attention-level noise increases posterior entropy and tightens risk bounds, by analyzing the effect on gradient variance. Injecting noise into attention distributions serves not only as a regularizer but also theoretically reduces generalization error bounds via PAC-Bayes.\n\n### Empirical Results\n\nThrough theoretical analysis and extensive experiments, the paper demonstrated consistent improvements in generalization, calibration, and robustness across vision and translation benchmarks.\n\nThe paper is available on arXiv at 2504.12088 (April 2025)."
    ],
    "durationSeconds": 7.356310278999969
  },
  "sourceToolAssistantUUID": "016f3690-f93c-48b1-8354-a102665a8ef2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "38eec20f-28d6-4706-b24b-8f0ea53acfb9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 43 · 2026-05-13T04:47:48.321Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have very strong evidence. Let me also check the "Knowledge Insulation" paper from Physical Intelligence and search for any other very recent works I might be missing.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "00f5cd8d-a181-4734-aa68-d62a8119d7f2",
  "isSidechain": false,
  "requestId": "req_011CayxmioKKFdcXVNWSxUzP",
  "type": "assistant",
  "uuid": "0431c4a0-4a52-441f-8226-c2b8b8aaf654",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "38eec20f-28d6-4706-b24b-8f0ea53acfb9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VBATYkyHv2EHbVk7K23PMX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1826,
      "cache_read_input_tokens": 45924,
      "output_tokens": 244,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1826,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 244,
          "cache_read_input_tokens": 45924,
          "cache_creation_input_tokens": 1826,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1826
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

_source line 44 · 2026-05-13T04:47:48.824Z_

Let me do a few more targeted searches to verify key missing references and check venue deadlines.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0431c4a0-4a52-441f-8226-c2b8b8aaf654",
  "isSidechain": false,
  "requestId": "req_011CayxmioKKFdcXVNWSxUzP",
  "type": "assistant",
  "uuid": "c893f510-51c7-45bd-9fe0-9692a57a9042",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "38eec20f-28d6-4706-b24b-8f0ea53acfb9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VBATYkyHv2EHbVk7K23PMX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1826,
      "cache_read_input_tokens": 45924,
      "output_tokens": 244,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1826,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 244,
          "cache_read_input_tokens": 45924,
          "cache_creation_input_tokens": 1826,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1826
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

_source line 45 · 2026-05-13T04:47:49.930Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013pJ2gwBXLqJPHqLuchH4Q4`</summary>

```json
{
  "query": "Knowledge Insulation VLA representation degradation Physical Intelligence NeurIPS 2025 arXiv 2505"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c893f510-51c7-45bd-9fe0-9692a57a9042",
  "isSidechain": false,
  "requestId": "req_011CayxmioKKFdcXVNWSxUzP",
  "type": "assistant",
  "uuid": "bf83b94c-20a5-45ff-ab69-a4c5ffceee1c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "38eec20f-28d6-4706-b24b-8f0ea53acfb9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VBATYkyHv2EHbVk7K23PMX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1826,
      "cache_read_input_tokens": 45924,
      "output_tokens": 244,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1826,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 244,
          "cache_read_input_tokens": 45924,
          "cache_creation_input_tokens": 1826,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1826
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

_source line 46 · 2026-05-13T04:47:50.340Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012KvuE2Hb1xdc3yZeCipX3c`</summary>

```json
{
  "query": "ICLR 2027 submission deadline September 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bf83b94c-20a5-45ff-ab69-a4c5ffceee1c",
  "isSidechain": false,
  "requestId": "req_011CayxmioKKFdcXVNWSxUzP",
  "type": "assistant",
  "uuid": "40a47816-b729-4fcb-96ab-2abac3988028",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "38eec20f-28d6-4706-b24b-8f0ea53acfb9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VBATYkyHv2EHbVk7K23PMX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1826,
      "cache_read_input_tokens": 45924,
      "output_tokens": 244,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1826,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 244,
          "cache_read_input_tokens": 45924,
          "cache_creation_input_tokens": 1826,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1826
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

_source line 47 · 2026-05-13T04:47:51.094Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UspfX5VnMmsnh7Y79rgE2d`</summary>

```json
{
  "query": "IBTM information bottleneck token merging vision transformer OpenReview"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "40a47816-b729-4fcb-96ab-2abac3988028",
  "isSidechain": false,
  "requestId": "req_011CayxmioKKFdcXVNWSxUzP",
  "type": "assistant",
  "uuid": "0f04687a-610c-48df-b1b3-488da9c64d8c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "38eec20f-28d6-4706-b24b-8f0ea53acfb9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VBATYkyHv2EHbVk7K23PMX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1826,
      "cache_read_input_tokens": 45924,
      "output_tokens": 244,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1826,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 244,
          "cache_read_input_tokens": 45924,
          "cache_creation_input_tokens": 1826,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1826
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

_source line 48 · 2026-05-13T04:47:55.703Z_

<details><summary>↩ Tool result · `toolu_012KvuE2Hb1xdc3yZeCipX3c`</summary>

```text
Web search results for query: "ICLR 2027 submission deadline September 2026"

Links: [{"title":"ICLR 2026","url":"https://iclr.cc/"},{"title":"International Conference on Learning Representations ICLR in August 2027 in Sydney","url":"https://waset.org/learning-representations-conference-in-august-2027-in-sydney"},{"title":"2026 Dates and Deadlines","url":"https://iclr.cc/Conferences/2026/Dates"},{"title":"Key deadlines in AI and ML conferences","url":"https://scouts.yutori.com/inbox/53e01f0f-2f7a-4f63-9b38-22358e5386ac"},{"title":"AI & ML Conference Deadlines 2026–2027","url":"https://trybibby.com/conference-deadlines"},{"title":"International Conference on Learning Representations - Wikipedia","url":"https://en.wikipedia.org/wiki/International_Conference_on_Learning_Representations"},{"title":"ICLR 2026 Author Guide","url":"https://iclr.cc/Conferences/2026/AuthorGuide"},{"title":"Call for Papers","url":"https://iclr.cc/Conferences/2025/CallForPapers"},{"title":"Year-Round Deadlines - Imranur Rahman","url":"https://imranur-rahman.github.io/deadlines/"},{"title":"2025 Dates and Deadlines","url":"https://iclr.cc/Conferences/2025/Dates"}]

The search results show information about ICLR 2026, but not specifically about ICLR 2027's submission deadline. Let me search more specifically for ICLR 2027 dates.

Links: [{"title":"International Conference on Learning Representations ICLR in August 2027 in Sydney","url":"https://waset.org/learning-representations-conference-in-august-2027-in-sydney"},{"title":"2026 Dates and Deadlines","url":"https://iclr.cc/Conferences/2026/Dates"},{"title":"ICLR 2026 Call for Papers","url":"https://iclr.cc/Conferences/2026/CallForPapers"},{"title":"Key deadlines in AI and ML conferences","url":"https://scouts.yutori.com/inbox/53e01f0f-2f7a-4f63-9b38-22358e5386ac"},{"title":"ICLR 2026","url":"https://iclr.cc/"},{"title":"Call for Papers","url":"https://iclr.cc/Conferences/2025/CallForPapers"},{"title":"2025 Dates and Deadlines","url":"https://iclr.cc/Conferences/2025/Dates"},{"title":"AI & ML Conference Deadlines 2026–2027","url":"https://trybibby.com/conference-deadlines"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"Year-Round Deadlines - Imranur Rahman","url":"https://imranur-rahman.github.io/deadlines/"}]

Based on my search results, I was unable to find specific information about ICLR 2027's submission deadline in September 2026. The search results show information about ICLR 2026 (which had a September 24 submission deadline) and general information about ICLR's typical schedule, but official details for ICLR 2027 don't appear to be published yet.

ICLR 2027 is predicted to occur around April 24-28, 2027, based on previous year schedules, but the specific submission deadline has not been officially announced. Some 2026/2027 conference calls for papers are not yet posted, which may include ICLR 2027's official dates and deadlines.

For the most accurate and current information about ICLR 2027 submission deadlines, I recommend checking the official ICLR website directly at iclr.cc when the call for papers is announced.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "40a47816-b729-4fcb-96ab-2abac3988028",
  "isSidechain": false,
  "promptId": "251a69dd-0148-46cf-91d6-c922d95174a8",
  "type": "user",
  "uuid": "ae4736c2-c438-46e8-8b52-c97932bc7e18",
  "toolUseResult": {
    "query": "ICLR 2027 submission deadline September 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_017JicBcr6QdQeBMNbJwkp1L",
        "content": [
          {
            "title": "ICLR 2026",
            "url": "https://iclr.cc/"
          },
          {
            "title": "International Conference on Learning Representations ICLR in August 2027 in Sydney",
            "url": "https://waset.org/learning-representations-conference-in-august-2027-in-sydney"
          },
          {
            "title": "2026 Dates and Deadlines",
            "url": "https://iclr.cc/Conferences/2026/Dates"
          },
          {
            "title": "Key deadlines in AI and ML conferences",
            "url": "https://scouts.yutori.com/inbox/53e01f0f-2f7a-4f63-9b38-22358e5386ac"
          },
          {
            "title": "AI & ML Conference Deadlines 2026–2027",
            "url": "https://trybibby.com/conference-deadlines"
          },
          {
            "title": "International Conference on Learning Representations - Wikipedia",
            "url": "https://en.wikipedia.org/wiki/International_Conference_on_Learning_Representations"
          },
          {
            "title": "ICLR 2026 Author Guide",
            "url": "https://iclr.cc/Conferences/2026/AuthorGuide"
          },
          {
            "title": "Call for Papers",
            "url": "https://iclr.cc/Conferences/2025/CallForPapers"
          },
          {
            "title": "Year-Round Deadlines - Imranur Rahman",
            "url": "https://imranur-rahman.github.io/deadlines/"
          },
          {
            "title": "2025 Dates and Deadlines",
            "url": "https://iclr.cc/Conferences/2025/Dates"
          }
        ]
      },
      "The search results show information about ICLR 2026, but not specifically about ICLR 2027's submission deadline. Let me search more specifically for ICLR 2027 dates.",
      {
        "tool_use_id": "srvtoolu_01RaeHX1CdFwxWcx8BiZYEU1",
        "content": [
          {
            "title": "International Conference on Learning Representations ICLR in August 2027 in Sydney",
            "url": "https://waset.org/learning-representations-conference-in-august-2027-in-sydney"
          },
          {
            "title": "2026 Dates and Deadlines",
            "url": "https://iclr.cc/Conferences/2026/Dates"
          },
          {
            "title": "ICLR 2026 Call for Papers",
            "url": "https://iclr.cc/Conferences/2026/CallForPapers"
          },
          {
            "title": "Key deadlines in AI and ML conferences",
            "url": "https://scouts.yutori.com/inbox/53e01f0f-2f7a-4f63-9b38-22358e5386ac"
          },
          {
            "title": "ICLR 2026",
            "url": "https://iclr.cc/"
          },
          {
            "title": "Call for Papers",
            "url": "https://iclr.cc/Conferences/2025/CallForPapers"
          },
          {
            "title": "2025 Dates and Deadlines",
            "url": "https://iclr.cc/Conferences/2025/Dates"
          },
          {
            "title": "AI & ML Conference Deadlines 2026–2027",
            "url": "https://trybibby.com/conference-deadlines"
          },
          {
            "title": "AI Conference Deadlines",
            "url": "https://mlciv.com/ai-deadlines/"
          },
          {
            "title": "Year-Round Deadlines - Imranur Rahman",
            "url": "https://imranur-rahman.github.io/deadlines/"
          }
        ]
      },
      "Based on my search results, I was unable to find specific information about ICLR 2027's submission deadline in September 2026. The search results show information about ICLR 2026 (which had a September 24 submission deadline) and general information about ICLR's typical schedule, but official details for ICLR 2027 don't appear to be published yet.\n\nICLR 2027 is predicted to occur around April 24-28, 2027, based on previous year schedules, but the specific submission deadline has not been officially announced. Some 2026/2027 conference calls for papers are not yet posted, which may include ICLR 2027's official dates and deadlines.\n\nFor the most accurate and current information about ICLR 2027 submission deadlines, I recommend checking the official ICLR website directly at iclr.cc when the call for papers is announced."
    ],
    "durationSeconds": 5.36095165100001
  },
  "sourceToolAssistantUUID": "40a47816-b729-4fcb-96ab-2abac3988028",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "38eec20f-28d6-4706-b24b-8f0ea53acfb9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 49_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-13 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "ae4736c2-c438-46e8-8b52-c97932bc7e18",
  "sessionId": "38eec20f-28d6-4706-b24b-8f0ea53acfb9"
}
```

---

### Runtime record

_source line 50_

```json
{
  "type": "ai-title",
  "aiTitle": "Review VLA token masking robustness via theory",
  "sessionId": "38eec20f-28d6-4706-b24b-8f0ea53acfb9"
}
```

---

### Tool result

_source line 51 · 2026-05-13T04:47:55.880Z_

<details><summary>↩ Tool result · `toolu_013pJ2gwBXLqJPHqLuchH4Q4`</summary>

```text
Web search results for query: "Knowledge Insulation VLA representation degradation Physical Intelligence NeurIPS 2025 arXiv 2505"

Links: [{"title":"[2505.23705] Knowledge Insulating Vision-Language-Action Models: Train Fast, Run Fast, Generalize Better","url":"https://arxiv.org/abs/2505.23705"},{"title":"GitHub - keon/awesome-physical-ai: A curated list of academic papers and resources on Physical AI — focusing on Vision-Language-Action (VLA) models, world models, embodied ai, and robotic foundation models.","url":"https://github.com/keon/awesome-physical-ai"},{"title":"arXiv:2506.13045v2 [cs.LG] 18 Jun 2025 1","url":"https://www.arxiv.org/pdf/2506.13045v2"},{"title":"Artificial Intelligence May 2025","url":"https://www.arxiv.org/list/cs.AI/2025-05?skip=1575&show=1000"},{"title":"Pure Vision Language Action (VLA) Models: A Comprehensive Survey","url":"https://arxiv.org/html/2509.19012v1"},{"title":"[2505.21906] ChatVLA-2: Vision-Language-Action Model with Open-World Embodied Reasoning from Pretrained Knowledge","url":"https://arxiv.org/abs/2505.21906"},{"title":"NeurIPS 2025 Papers","url":"https://neurips.cc/virtual/2025/papers.html"},{"title":"Computer Science May 2025","url":"https://arxiv.org/list/cs/2025-05?skip=12075&show=2000"},{"title":"awesome-physical-ai/README.md at main · keon/awesome-physical-ai","url":"https://github.com/keon/awesome-physical-ai/blob/main/README.md"},{"title":"π∗ 0.6: a VLA That Learns From Experience Physical Intelligence","url":"https://www.pi.website/download/pistar06.pdf"}]

I found the paper you're looking for! Here are the key results:

## Knowledge Insulating Vision-Language-Action Models

Vision-language-action (VLA) models provide a powerful approach to training control policies for physical systems, such as robots, by combining end-to-end learning with transfer of semantic knowledge from web-scale vision-language model (VLM) training.

A key open question is whether specialized modules for continuous control preserve or degrade the semantic knowledge contained in the pretrained VLM, and what effect they have on the VLA training dynamics.

Research has shown that naively including continuous diffusion or flow matching action experts significantly harms both training speed and knowledge transfer, and proposes a technique for insulating the VLM backbone during VLA training that mitigates this issue.

**Paper Details:**
- **arXiv ID:** 2505.23705
- **Title:** "Knowledge Insulating Vision-Language-Action Models: Train Fast, Run Fast, Generalize Better"
- **Posted:** May 29, 2025
- **URL:** https://arxiv.org/abs/2505.23705

This paper appears to be part of Physical Intelligence's work presented around NeurIPS 2025, addressing the important challenge of preventing representation degradation when adapting pretrained vision-language models for robotic control tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bf83b94c-20a5-45ff-ab69-a4c5ffceee1c",
  "isSidechain": false,
  "promptId": "251a69dd-0148-46cf-91d6-c922d95174a8",
  "type": "user",
  "uuid": "71f4c047-f231-40f9-b7c0-f2b801cfdb78",
  "toolUseResult": {
    "query": "Knowledge Insulation VLA representation degradation Physical Intelligence NeurIPS 2025 arXiv 2505",
    "results": [
      {
        "tool_use_id": "srvtoolu_01JoEiwgEsbDy6yC44PLHzE1",
        "content": [
          {
            "title": "[2505.23705] Knowledge Insulating Vision-Language-Action Models: Train Fast, Run Fast, Generalize Better",
            "url": "https://arxiv.org/abs/2505.23705"
          },
          {
            "title": "GitHub - keon/awesome-physical-ai: A curated list of academic papers and resources on Physical AI — focusing on Vision-Language-Action (VLA) models, world models, embodied ai, and robotic foundation models.",
            "url": "https://github.com/keon/awesome-physical-ai"
          },
          {
            "title": "arXiv:2506.13045v2 [cs.LG] 18 Jun 2025 1",
            "url": "https://www.arxiv.org/pdf/2506.13045v2"
          },
          {
            "title": "Artificial Intelligence May 2025",
            "url": "https://www.arxiv.org/list/cs.AI/2025-05?skip=1575&show=1000"
          },
          {
            "title": "Pure Vision Language Action (VLA) Models: A Comprehensive Survey",
            "url": "https://arxiv.org/html/2509.19012v1"
          },
          {
            "title": "[2505.21906] ChatVLA-2: Vision-Language-Action Model with Open-World Embodied Reasoning from Pretrained Knowledge",
            "url": "https://arxiv.org/abs/2505.21906"
          },
          {
            "title": "NeurIPS 2025 Papers",
            "url": "https://neurips.cc/virtual/2025/papers.html"
          },
          {
            "title": "Computer Science May 2025",
            "url": "https://arxiv.org/list/cs/2025-05?skip=12075&show=2000"
          },
          {
            "title": "awesome-physical-ai/README.md at main · keon/awesome-physical-ai",
            "url": "https://github.com/keon/awesome-physical-ai/blob/main/README.md"
          },
          {
            "title": "π∗ 0.6: a VLA That Learns From Experience Physical Intelligence",
            "url": "https://www.pi.website/download/pistar06.pdf"
          }
        ]
      },
      "I found the paper you're looking for! Here are the key results:\n\n## Knowledge Insulating Vision-Language-Action Models\n\nVision-language-action (VLA) models provide a powerful approach to training control policies for physical systems, such as robots, by combining end-to-end learning with transfer of semantic knowledge from web-scale vision-language model (VLM) training.\n\nA key open question is whether specialized modules for continuous control preserve or degrade the semantic knowledge contained in the pretrained VLM, and what effect they have on the VLA training dynamics.\n\nResearch has shown that naively including continuous diffusion or flow matching action experts significantly harms both training speed and knowledge transfer, and proposes a technique for insulating the VLM backbone during VLA training that mitigates this issue.\n\n**Paper Details:**\n- **arXiv ID:** 2505.23705\n- **Title:** \"Knowledge Insulating Vision-Language-Action Models: Train Fast, Run Fast, Generalize Better\"\n- **Posted:** May 29, 2025\n- **URL:** https://arxiv.org/abs/2505.23705\n\nThis paper appears to be part of Physical Intelligence's work presented around NeurIPS 2025, addressing the important challenge of preventing representation degradation when adapting pretrained vision-language models for robotic control tasks."
    ],
    "durationSeconds": 5.945122766999994
  },
  "sourceToolAssistantUUID": "bf83b94c-20a5-45ff-ab69-a4c5ffceee1c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "38eec20f-28d6-4706-b24b-8f0ea53acfb9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-13T04:47:56.717Z_

<details><summary>↩ Tool result · `toolu_01UspfX5VnMmsnh7Y79rgE2d`</summary>

```text
Web search results for query: "IBTM information bottleneck token merging vision transformer OpenReview"

Links: [{"title":"Efficient Visual Transformer by Information Bottleneck Inspired Token Merging | OpenReview","url":"https://openreview.net/forum?id=Jwgw3znxT3"},{"title":"EFFICIENT VISION TRANSFORMER BY INFORMATION ...","url":"https://openreview.net/pdf?id=Jwgw3znxT3"},{"title":"Efficient Visual Transformer by Learnable Token Merging","url":"https://arxiv.org/html/2407.15219v1"},{"title":"Bottlenecked Transformers: Periodic KV Cache Abstraction for Generalised Reasoning","url":"https://arxiv.org/html/2505.16950v1"},{"title":"Efficient Vision Transformer via Token Merger","url":"https://www.researchgate.net/publication/372343417_Efficient_Vision_Transformer_via_Token_Merger"},{"title":"1 Efficient Visual Transformer by Learnable Token Merging","url":"https://arxiv.org/pdf/2407.15219"},{"title":"Connectivity-based Token Condensation for Efficient Vision Transformer | OpenReview","url":"https://openreview.net/forum?id=8vGXHjuCiq"},{"title":"Token Merging: Your ViT But Faster | OpenReview","url":"https://openreview.net/forum?id=JroZRaRw7Eu"},{"title":"Attention Bottlenecks for Multimodal Fusion | OpenReview","url":"https://openreview.net/forum?id=KJ5h-yfUHa"},{"title":"Training-Free Visual Token Compression via Delayed Spatial Merging | OpenReview","url":"https://openreview.net/forum?id=4JXo4wOUfQ"}]

I found the research on IBTM. Here's what the search results reveal:

## IBTM: Information Bottleneck Token Merging for Vision Transformers

IBTM is a novel and compact transformer block called "Transformer with Information Bottleneck inspired Token Merging." 

**Core Functionality:**
IBTM performs token merging in a learnable scheme. The IBTM is motivated by the reduction of the Information Bottleneck (IB), and a novel and separable variational upper bound for the IB loss is derived.

**Performance Benefits:**
IBTM is compatible with many popular and compact transformer networks, such as MobileViT and EfficientViT, and it reduces the FLOPs and the inference time of the vision transformers while maintaining or even improving the prediction accuracy.

**Experimental Scope:**
In the experiments, IBTM blocks are used to replace all the transformer blocks in popular vision transformers, including MobileViT, EfficientViT, ViT, and Swin. Extensive results on image classification and object detection evidence that IBTM renders compact and efficient vision transformers with comparable or much better prediction accuracy than the original vision transformers.

The paper is available on OpenReview at https://openreview.net/forum?id=Jwgw3znxT3, with the publication date noted as October 4, 2024.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0f04687a-610c-48df-b1b3-488da9c64d8c",
  "isSidechain": false,
  "promptId": "251a69dd-0148-46cf-91d6-c922d95174a8",
  "type": "user",
  "uuid": "50c52227-ff3e-434f-8f7a-f5fb1695a575",
  "toolUseResult": {
    "query": "IBTM information bottleneck token merging vision transformer OpenReview",
    "results": [
      {
        "tool_use_id": "srvtoolu_01HV8MYKeYoEPTeiT3jMAfsM",
        "content": [
          {
            "title": "Efficient Visual Transformer by Information Bottleneck Inspired Token Merging | OpenReview",
            "url": "https://openreview.net/forum?id=Jwgw3znxT3"
          },
          {
            "title": "EFFICIENT VISION TRANSFORMER BY INFORMATION ...",
            "url": "https://openreview.net/pdf?id=Jwgw3znxT3"
          },
          {
            "title": "Efficient Visual Transformer by Learnable Token Merging",
            "url": "https://arxiv.org/html/2407.15219v1"
          },
          {
            "title": "Bottlenecked Transformers: Periodic KV Cache Abstraction for Generalised Reasoning",
            "url": "https://arxiv.org/html/2505.16950v1"
          },
          {
            "title": "Efficient Vision Transformer via Token Merger",
            "url": "https://www.researchgate.net/publication/372343417_Efficient_Vision_Transformer_via_Token_Merger"
          },
          {
            "title": "1 Efficient Visual Transformer by Learnable Token Merging",
            "url": "https://arxiv.org/pdf/2407.15219"
          },
          {
            "title": "Connectivity-based Token Condensation for Efficient Vision Transformer | OpenReview",
            "url": "https://openreview.net/forum?id=8vGXHjuCiq"
          },
          {
            "title": "Token Merging: Your ViT But Faster | OpenReview",
            "url": "https://openreview.net/forum?id=JroZRaRw7Eu"
          },
          {
            "title": "Attention Bottlenecks for Multimodal Fusion | OpenReview",
            "url": "https://openreview.net/forum?id=KJ5h-yfUHa"
          },
          {
            "title": "Training-Free Visual Token Compression via Delayed Spatial Merging | OpenReview",
            "url": "https://openreview.net/forum?id=4JXo4wOUfQ"
          }
        ]
      },
      "I found the research on IBTM. Here's what the search results reveal:\n\n## IBTM: Information Bottleneck Token Merging for Vision Transformers\n\nIBTM is a novel and compact transformer block called \"Transformer with Information Bottleneck inspired Token Merging.\" \n\n**Core Functionality:**\nIBTM performs token merging in a learnable scheme. The IBTM is motivated by the reduction of the Information Bottleneck (IB), and a novel and separable variational upper bound for the IB loss is derived.\n\n**Performance Benefits:**\nIBTM is compatible with many popular and compact transformer networks, such as MobileViT and EfficientViT, and it reduces the FLOPs and the inference time of the vision transformers while maintaining or even improving the prediction accuracy.\n\n**Experimental Scope:**\nIn the experiments, IBTM blocks are used to replace all the transformer blocks in popular vision transformers, including MobileViT, EfficientViT, ViT, and Swin. Extensive results on image classification and object detection evidence that IBTM renders compact and efficient vision transformers with comparable or much better prediction accuracy than the original vision transformers.\n\nThe paper is available on OpenReview at https://openreview.net/forum?id=Jwgw3znxT3, with the publication date noted as October 4, 2024."
    ],
    "durationSeconds": 5.620879168000014
  },
  "sourceToolAssistantUUID": "0f04687a-610c-48df-b1b3-488da9c64d8c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "38eec20f-28d6-4706-b24b-8f0ea53acfb9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 53 · 2026-05-13T04:48:35.353Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a very comprehensive picture. Let me synthesize all findings and produce the review JSON.

## Critical Issues Summary

### 1. DEVASTATING COUNTER-EVIDENCE NOT ADDRESSED
"Rethinking VLA Model Scaling" (arXiv:2602.09722, Feb 2026) directly tested visual dropout (p=0.2) during VLA training and found it **HURTS** performance (84.5% with dropout → 85.6% without). They concluded: "the natural diversity of the pre-training corpus already serves as an effective regularizer, making additional noise injection unnecessary, or even harmful." 

The CTM idea does NOT mention this paper at all. 

This is a critical gap because the paper's findings directly undermine the core assumption that token masking helps VLA training. There's a potential defense here—the paper tested dropout on diverse pretraining data while CTM targets low-diversity robot finetuning, where regularization might actually be beneficial—but the idea would need to explicitly acknowledge this paper and make that argument rather than ignoring it entirely.

### 2. MISSING COMPETITIVE WORK
- **"See What Matters" / GridS (ICML 2026)**: Differentiable token resampling for VLA generalization. Published at a top venue. Not mentioned.
- **Knowledge Insulation (arXiv:2505.23705, Physical Intelligence)**: Addresses representation degradation during VLA training by insulating VLM backbone. Not mentioned.
- **RoCoDA (ICRA 2025)**: Counterfactual data augmentation for robot learning. Directly applies causal/counterfactual augmentation in robotics. Not mentioned.
- **AttentionDrop (arXiv:2504.12088)**: PAC-Bayes bounds for attention-level masking in transformers. Not mentioned.
- **IBTM**: IB-inspired token merging with formal IB bound derivation. Partially undermines the theoretical novelty.

### 3. THEORETICAL NOVELTY CONCERNS
Looking at the four claimed theoretical contributions, each one has substantial prior work that weakens the novelty claims. The IB bound for token masking, for instance, is already covered by IBTM.

The attention entropy lower bound, PAC-Bayes bound, and causal analysis all have existing precedents—Zhai et al. derived attention entropy bounds, AttentionDrop and McAllester's work already established PAC-Bayes frameworks for masking and dropout, and Xiao et al. plus RoCoDA already applied counterfactual frameworks to vision and robotics respectively.

The real contribution is combining these established pieces specifically for VLAs, though each component individually is well-known. There are some attribution issues—the PAC-Bayes bounds should trace back to McAllester rather than Gal & Ghahramani, and the IB "equivalence" in Achille & Soatto is more of an approximation under specific conditions. That said, the work does offer a comprehensive landscape analysis across six concurrent approaches, maintains clear differentiation from most cited works, and presents a solid three-component framework with detailed evaluation and ablation plans. The shift away from LIBERO saturation toward OOD evaluation is a reasonable adjustment. Overall, the novelty feels limited since it's primarily repackaging known techniques, landing around 2/5.

The implementation itself is straightforward, but there's a fundamental feasibility problem: prior work like "Rethinking VLA Model Scaling" shows that visual dropout actually hurts VLA performance, which directly contradicts what this approach assumes will work. The paper needs to make a convincing case for why token-level masking with adaptive rates would succeed where simpler sensory dropout failed. Each theoretical component also carries risk—they need to demonstrate meaningful differences from existing work rather than just minor variations.

The writeup is well-structured and comprehensive with clearly defined components and a solid evaluation plan, though there are some minor issues with how PAC-Bayes and information bottleneck are framed. Even if the approach works, the impact would be limited given the crowded landscape of competing methods and the fact that the theoretical contributions are largely adaptations of known techniques rather than novel insights.

Scoring this out, the novelty and feasibility concerns combined with moderate impact puts the overall assessment below the publication threshold. The core issue is that the approach needs to convincingly overcome the evidence that visual dropout hurts VLA performance, and the theoretical contributions need to be substantively different from existing work to be publishable at a top venue.

Now I need to identify the specific revisions required: the counter-evidence against the main hypothesis needs direct engagement, the related work section must properly position this against GridS and the other concurrent approaches, the theoretical claims need tightening to reflect what's genuinely novel, and the PAC-Bayes attribution error needs correction.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "50c52227-ff3e-434f-8f7a-f5fb1695a575",
  "isSidechain": false,
  "requestId": "req_011CayxnZh9rbJo8enRQbXX6",
  "type": "assistant",
  "uuid": "98877189-8504-4608-896d-fdc5f4302052",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "38eec20f-28d6-4706-b24b-8f0ea53acfb9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V7PARU8dMYggaGxdBsLNvj",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2966,
      "cache_read_input_tokens": 47750,
      "output_tokens": 4121,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2966,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4121,
          "cache_read_input_tokens": 47750,
          "cache_creation_input_tokens": 2966,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2966
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

_source line 54 · 2026-05-13T04:49:23.320Z_

Now I have comprehensive evidence from all angles. Let me compile my final assessment.

```json
{
  "verdict": "revise",
  "scores": {
    "novelty": {
      "score": 2,
      "rationale": "Each of the four claimed theoretical contributions has significant prior art: IBTM (OpenReview 2024) already derives IB bounds for token-level operations in ViTs; CRAFT (arXiv 2602.12532) already applies VIB to VLA finetuning; AttentionDrop (arXiv 2504.12088) already provides PAC-Bayes bounds for attention-level perturbation; Zhai et al. (ICML 2023) already derived attention entropy bounds; RoCoDA (ICRA 2025) already applies counterfactual augmentation to robotics. 'See What Matters'/GridS (ICML 2026) already connects differentiable token operations to VLA generalization at a top venue. The remaining novelty — the specific combination of adaptive token masking with IB regularization in the frozen-ViT → projector → LLM pipeline — is incremental."
    },
    "feasibility": {
      "score": 2,
      "rationale": "'Rethinking VLA Model Scaling' (arXiv 2602.09722, Feb 2026) directly tested visual dropout (p=0.2) during VLA training and found it HURTS performance (84.5% → 85.6% without dropout), concluding 'natural diversity of the pre-training corpus already serves as an effective regularizer.' This is devastating counter-evidence that the idea completely ignores. While one could argue finetuning-on-low-diversity-data differs from pretraining, this must be explicitly addressed with a convincing argument, and may indicate the fundamental approach is flawed."
    },
    "clarity": {
      "score": 4,
      "rationale": "The writeup is well-structured with three clearly defined components, comprehensive baselines (9 methods), appropriate evaluation focus on OOD metrics, and detailed ablation plans. Minor issues: PAC-Bayes bounds are misattributed to Gal & Ghahramani (2016) when the correct source is McAllester (2013); Achille & Soatto's result is an approximation under restricted distribution families, not an equivalence."
    },
    "impact": {
      "score": 2,
      "rationale": "The VLA representation preservation space is extremely crowded with 6+ concurrent approaches (frozen-encoder alignment, dual-encoder, contrastive regularization, spectral experts, action-as-language, dual-critic) plus GridS at ICML 2026 for token-level operations. Even if CTM works, the marginal contribution over this dense field would likely be viewed as incremental by top-venue reviewers. The theoretical contributions are adaptations of known results to a new domain, not fundamentally new insights."
    }
  },
  "issues": [
    "CRITICAL COUNTER-EVIDENCE IGNORED: 'Rethinking VLA Model Scaling' (arXiv 2602.09722, Wang et al., Feb 2026) directly tested sensory dropout (visual dropout p=0.2) during VLA training and found it HURTS performance — 84.5% with dropout vs 85.6% without. They concluded 'the natural diversity of the pre-training corpus already serves as an effective regularizer, making additional noise injection unnecessary, or even harmful.' This paper is not cited anywhere in the idea and directly challenges the CTM premise. The idea MUST address why CTM would succeed where simple sensory dropout failed.",
    "CRITICAL MISSING REFERENCE — 'See What Matters'/GridS (ICML 2026, Feng et al.): Differentiable grid sample pruning for 'generalizable VLA' — explicitly connects token-level operations to VLA generalization (not just efficiency). Published at ICML 2026. Achieves 76% FLOP reduction with no success rate degradation. This is a direct competitor in the 'token operations improve VLA generalization' space and is not cited.",
    "CRITICAL MISSING REFERENCE — RoCoDA (ICRA 2025, Ameperosa et al., arXiv 2411.16959): Counterfactual data augmentation for robot learning that leverages causal graphs to identify task-irrelevant state subsets and resample them. Directly applies the counterfactual/causal augmentation framework to robotics imitation learning — extremely close to CTM's causal story. Not cited.",
    "CRITICAL MISSING REFERENCE — Knowledge Insulation (arXiv 2505.23705, Physical Intelligence): Addresses the exact same problem (representation degradation during VLA finetuning) by insulating the VLM backbone from action expert gradients. Demonstrated to 'Train Fast, Run Fast, Generalize Better.' Not cited.",
    "MISSING REFERENCE — AttentionDrop (arXiv 2504.12088, Apr 2025): Already derives PAC-Bayes generalization bounds for attention-level stochastic perturbation in transformers, proving that attention-level noise increases posterior entropy and tightens risk bounds. This significantly undermines the claimed novelty of theoretical contribution (c), the PAC-Bayes bound.",
    "MISSING REFERENCE — IBTM (OpenReview 2024): 'Efficient Visual Transformer by Information Bottleneck Inspired Token Merging' already derives a separable variational upper bound for the IB loss applied to token-level operations in ViTs. This undermines the claimed novelty of theoretical contribution (a), the IB bound for token masking.",
    "MISATTRIBUTION: The PAC-Bayes generalization bound is attributed to Gal & Ghahramani (ICML 2016), but that paper is about Bayesian approximation via dropout for uncertainty estimation, NOT PAC-Bayes bounds. The correct citation for PAC-Bayes dropout bounds is McAllester (2013), 'A PAC-Bayesian Tutorial with a Dropout Bound' (arXiv 1307.2118).",
    "THEORETICAL OVERSTATEMENT: The idea states Achille & Soatto (2018) proved multiplicative noise 'is equivalent to IB regularization.' The actual result is weaker: it is an approximation under restricted distribution families. The authors explicitly state 'there is no guarantee that the resulting representation will be optimal.' This distinction matters for the formal derivation claimed in Component 3(a).",
    "THEORETICAL NOVELTY INFLATION: All four theoretical contributions have significant predecessors — (a) IB bound: IBTM + CRAFT, (b) attention entropy: Zhai et al. ICML 2023 + AttentionDrop, (c) PAC-Bayes: McAllester 2013 + AttentionDrop, (d) causal: Xiao et al. CVPR 2023 + RoCoDA. Adapting each to the VLA setting is useful but does not constitute a 'theoretical contribution' at a top venue — it is application of existing theory to a new domain.",
    "RESOURCE ESTIMATE INCONSISTENCY: The manual mode estimates ~250h A100 at 30-40% utilization. With 9 baselines to reproduce (many without released code — RS-CL, VLA-GSE, VLM2VLA), just baseline reproduction could consume 100+ hours. The 250h estimate is likely undercount for a paper with this many comparisons."
  ],
  "feedback": "The idea has improved significantly from round 1 in landscape coverage and evaluation design, but three critical gaps remain:\n\n**1. ADDRESS THE COUNTER-EVIDENCE (highest priority).** 'Rethinking VLA Model Scaling' (arXiv 2602.09722) found visual dropout HURTS VLA training. You MUST cite this paper and explain why CTM differs. The key argument should be: they tested dropout during *pretraining on diverse multi-embodiment data* where natural diversity already regularizes, whereas CTM targets *finetuning on low-diversity single-task demonstrations* where spurious correlations form. Additionally, their dropout was uniform random on entire camera views, whereas CTM's adaptive variant learns to mask specifically the tokens that cause spurious correlations. This distinction (pretraining-diverse vs. finetuning-low-diversity) should become a central motivation, not an afterthought.\n\n**2. CITE AND POSITION AGAINST NEW COMPETITORS.** You must add: (a) GridS/'See What Matters' (ICML 2026) — differentiate by noting GridS focuses on geometry-aware resampling for efficiency with generalization as side benefit, while CTM explicitly optimizes for OOD generalization via IB regularization; (b) RoCoDA (ICRA 2025) — differentiate by noting RoCoDA operates on state-space augmentation with explicit causal graphs, while CTM operates on visual token space with implicit IB-based causal identification; (c) Knowledge Insulation (Physical Intelligence) — differentiate by noting it insulates via gradient blocking, while CTM regularizes via information-theoretic token masking; (d) AttentionDrop — acknowledge as theoretical precedent for attention-level PAC-Bayes bounds.\n\n**3. NARROW AND SHARPEN THEORETICAL CLAIMS.** Given IBTM (IB for tokens), AttentionDrop (PAC-Bayes for attention masking), CRAFT (VIB for VLA), and Zhai et al. (attention entropy bounds), claiming four independent theoretical contributions is overclaiming. Instead, frame a single unified theoretical contribution: 'We derive the first VLA-specific information-theoretic analysis showing that token masking after the projector creates an implicit variational information bottleneck that simultaneously (a) upper-bounds representation dependence on spurious tokens AND (b) lower-bounds attention diversity, with the key insight that this dual effect is uniquely important in the frozen-ViT→projector→LLM architecture where gradient flow is constrained.' This unified framing is more honest and potentially stronger than four incremental adaptations.\n\n**4. FIX MISATTRIBUTIONS.** Replace 'Gal & Ghahramani (2016)' with 'McAllester (2013)' for PAC-Bayes dropout bounds. Weaken 'equivalent to IB regularization' to 'approximates IB regularization under restricted distribution families' for Achille & Soatto.\n\n**5. ADD MISSING BASELINES.** Add GridS (ICML 2026) and Knowledge Insulation to the baseline comparisons — they are direct competitors. Consider adding RoCoDA-style counterfactual augmentation as an ablation to isolate CTM's contribution beyond standard counterfactual augmentation.",
  "reason": "Critical counter-evidence (visual dropout hurts VLA performance) is unaddressed, multiple important competitors are missing (GridS ICML 2026, RoCoDA, Knowledge Insulation, AttentionDrop), and all four theoretical contributions have significant prior art — the novelty is narrower than claimed."
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "98877189-8504-4608-896d-fdc5f4302052",
  "isSidechain": false,
  "requestId": "req_011CayxnZh9rbJo8enRQbXX6",
  "type": "assistant",
  "uuid": "d925703e-c6a8-4583-9253-635611214bf5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "38eec20f-28d6-4706-b24b-8f0ea53acfb9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V7PARU8dMYggaGxdBsLNvj",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2966,
      "cache_read_input_tokens": 47750,
      "output_tokens": 4121,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2966,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4121,
          "cache_read_input_tokens": 47750,
          "cache_creation_input_tokens": 2966,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2966
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

_source line 55_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-13 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "d925703e-c6a8-4583-9253-635611214bf5",
  "sessionId": "38eec20f-28d6-4706-b24b-8f0ea53acfb9"
}
```

---

### Runtime record

_source line 56_

```json
{
  "type": "ai-title",
  "aiTitle": "Review VLA token masking robustness via theory",
  "sessionId": "38eec20f-28d6-4706-b24b-8f0ea53acfb9"
}
```

---

### Runtime record

_source line 57_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-13 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "d925703e-c6a8-4583-9253-635611214bf5",
  "sessionId": "38eec20f-28d6-4706-b24b-8f0ea53acfb9"
}
```

---

### Runtime record

_source line 58_

```json
{
  "type": "ai-title",
  "aiTitle": "Review VLA token masking robustness via theory",
  "sessionId": "38eec20f-28d6-4706-b24b-8f0ea53acfb9"
}
```

---
