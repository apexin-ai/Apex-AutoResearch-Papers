# Research conversation: You are a strict ML research reviewer conducting adversarial review. **Today's date: 2026-05-10 (UTC).** Your job: indep

**When Does Detect-and-Reweight Work for Synthetic Contamination? (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 46
- **Recorded user turns:** 1
- **Tool calls:** 11
- **Original source:** `logs/chats/exported-trajectories/account-3/c9f1e88d-7547-445a-bdb2-8a60925de079.jsonl`
- **Structured JSON:** [`fb95e9f0def5aacb0083.json`](../../sessions/fb/fb95e9f0def5aacb0083.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-10T19:20:26.394Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-10T19:20:26.394Z",
  "sessionId": "c9f1e88d-7547-445a-bdb2-8a60925de079",
  "content": "You are a strict ML research reviewer conducting adversarial review.\n\n**Today's date: 2026-05-10 (UTC).**\n\nYour job: independently verify this idea's claims via WebSearch, then issue a verdict.\n\n## User requirements\nThe user asked for: **Target: CoRL 2026 (Austin, Nov 9-12, 2026). Abstract deadline 2026-05-26 (17 days); paper deadline 2026-05-29 (20 days).\n\nDirection: Generative models specifically targeting HUMANOID robot training data — addressing the high-DoF, whole-body, loco-manipulation data scarcity that bottlenecks humanoid VLA / WM training. SCOPE LIMITED TO TWO CONTRIBUTION TYPES:\n  (a) Generation ALGORITHMS — e.g., video diffusion conditioned on humanoid action streams, action-conditioned generative models, latent humanoid trajectory generators, physics-aware whole-body video generation.\n  (b) Procedural data-generation PIPELINES — e.g., MimicGen-style automated demo multiplication for humanoids, procedural whole-body task/scene generation, automated quality filtering pipelines for synthetic humanoid trajectories.\n\nOUT OF SCOPE: action retargeting innovations (human-video → humanoid-action retargeting). Treat existing retargeters (HumanPlus, OmniH2O) as black-box upstream tools if needed; do NOT propose new retargeting methods.\n\nRecent landscape (do not duplicate): NVIDIA GR00T-Dreams, DexMimicGen, MimicGen extensions for humanoid, Helix self-supervised humanoid pipelines, Cosmos for synthetic humanoid video. Humanoid data scarcity is the #1 bottleneck cited in 2026 humanoid papers — high impact area.\n\nContribution type: METHOD ONLY. New generation algorithm OR new procedural pipeline. Not a new released humanoid dataset alone.\n\nSIM-ONLY MITIGATION: Validate generated data by training a downstream humanoid policy/VLA in sim and comparing against models trained on baseline data. Frame contribution as method, not dataset.\n\nHARD CONSTRAINTS:\n1. Compute: ≤200 H100-hours total. Strategies: (a) fine-tune existing video diffusion (CogVideoX, OpenSora, Cosmos) with humanoid-action conditioning, (b) procedural pipeline that requires negligible training compute, (c) small efficient humanoid-specific generator that beats general baselines.\n2. Time: ≤20 days. Build on HF Diffusers, OpenSora, NVIDIA Cosmos repos, Isaac Lab humanoid suite (G1, H1), MimicGen, RoboCasa with humanoid embodiments if available.\n3. Eval: train humanoid policy/VLA on generated vs baseline data. Test on Isaac Lab humanoid manipulation/locomanipulation tasks, RoboCasa kitchen with humanoid embodiment, HumanoidBench. Report success rate + data efficiency curves.\n\nLook for: physics-aware whole-body video generation with kinematic consistency, action-conditioned generators that exploit humanoid kinematic structure, procedural pipelines that produce diverse loco-manipulation (not just static manipulation) data, automatic quality filtering for synthetic humanoid trajectories. Avoid: any retargeting-based contribution, arm-only generation rebadged as humanoid, naive fine-tuning of video diffusion on humanoid clips without method.\n\nTag: direction=humanoid_data_gen, contribution_type=method. target_venues=[\"CoRL 2026\"].**\nYou MUST evaluate whether this idea actually meets the user's requirements. If the user asked for a top venue, assess whether the idea is truly top-venue quality. If the user asked for low resource cost, verify the resource estimate is realistic and low. An idea that doesn't match what the user asked for should be \"revise\" or \"fail\".\n\n## 核心要求：非常仔细地调研，非常仔细地思考\n\n你是一个严格的审稿人。不要轻信 Generator 的任何 claim——你必须独立验证，深入思考每个维度。\n\n### 调研要求\n\n1. **独立 SOTA 验证**：自己搜索当前 SOTA，不要只检查 Generator 的引用。\n   每个验证维度建议用 2-3 种不同的搜索查询。\n\n2. **可行性深度检查**：\n   - 搜索类似实验的实际成本/周期\n   - 检查 claimed baselines 是否可复现\n   - 验证所需的 datasets/models 是否真的可以获取\n\n3. **新颖性压力测试**：专门搜索 Generator 可能遗漏的工作：\n   - 尝试不同的关键词组合\n   - 同时检查 arXiv 和 conference proceedings\n   - 寻找相邻领域的并行/concurrent 工作\n\n4. **深入阅读**：不要只依赖搜索摘要。用 WebFetch 实际阅读相关论文的 abstract 和关键章节，形成你自己的判断。\n\n### 思考要求\n\n5. **独立判断**：\n   - 不要因为 Generator 说得有道理就轻易 pass——真正好的 idea 经得起严格审查\n   - 思考这个 idea 在实际执行中会遇到什么困难\n   - 考虑这个 idea 对领域的真实贡献（不是自说自话的贡献）\n\n6. **评分诚实**：\n   - 不要给\"看起来还行\"的 idea 高分——4 分意味着\"确实很好\"，5 分意味着\"令人兴奋\"\n   - Agent 评分经常虚高，你的职责就是纠正这种偏差\n\n充分利用你的工具——做真正的调研，不是走过场。\n\n\n## 论文搜索策略\n\n你的搜索质量直接决定了 idea 的质量。不要敷衍搜索——每一次搜索都要有明确的目的。\n\n### 搜索源（推荐每个维度使用 2 个不同来源）\n\n1. **arXiv 预印本**（最新工作）:\n   - `site:arxiv.org {topic} {year}` — 按主题搜索最新论文\n   - `site:arxiv.org {method_name}` — 按具体方法名搜索\n   - `arxiv {topic} {month} {year}` — 精确到月份，找最近 3 个月的工作\n\n2. **Google Scholar**（引用关系 + 综合覆盖）:\n   - `{topic} {year} site:scholar.google.com` — 或直接搜索让 Google 自动包含 Scholar 结果\n   - `\"{exact paper title}\"` — 验证论文是否真实存在\n   - `\"{author name}\" {topic} {year}` — 按活跃作者追踪（找到领域大牛后追踪其最新工作）\n\n3. **Papers With Code**（SOTA 排行 + 代码可用性）:\n   - `site:paperswithcode.com {task_name}` — 查看任务的 SOTA 排行榜\n   - `site:paperswithcode.com {method_name}` — 查看方法是否已被实现\n   - `paperswithcode {dataset} benchmark` — 查看特定 dataset 上的竞争格局\n\n4. **OpenReview**（会议审稿 + 同行评价）:\n   - `site:openreview.net {topic} {year}` — 搜索会议提交的论文\n   - 用 WebFetch 阅读 OpenReview 上的 reviewer comments — 了解领域专家的真实评价\n\n5. **Semantic Scholar**（语义搜索 + 引用图谱）:\n   - `semantic scholar {topic} survey {year}` — 找综述论文\n   - `semanticscholar.org {paper_title}` — 查看 cited by（谁引用了这篇）和 references（它引用了谁）\n\n6. **GitHub**（实现验证）:\n   - `site:github.com {method_name} {task}` — 验证开源实现是否存在\n   - `site:huggingface.co {model_name}` — 验证模型/数据集是否可获取\n\n### 搜索维度（多角度交叉，不要只按 topic 搜）\n\n对每个 idea/方向，尽量覆盖以下维度：\n\n1. **正向搜索**：直接搜索主题相关论文\n   - `{topic} {subtopic} {year}`\n   - `{method_name} for {task_name}`\n\n2. **竞争论文搜索**（最关键！）：\n   - `{core_problem} {year}` — 有没有人在解决同样的问题？\n   - `{approach_keyword} {task} {year}` — 有没有人用类似方法？\n   - `{gap_description} solution` — 你发现的 gap 是否已被解决？\n   - **搜索知名团队的最新工作**：如果你知道哪些团队在做这个方向，搜索他们最近 6 个月的论文\n\n3. **相邻领域搜索**：\n   - `{method_from_other_field} applied to {your_task}`\n   - `{your_problem} in {adjacent_domain}` — 其他领域是否已解决类似问题\n\n4. **反面搜索**（找到反对你 idea 的证据）：\n   - `{your_approach} limitations` / `{your_approach} failure`\n   - `why {assumed_gap} is not a problem`\n   - `{baseline_method} sufficient for {task}` — baseline 是否其实已经够好\n\n5. **引用链追踪**（发现遗漏工作的最有效方法）：\n   - 找到一篇核心相关论文后，用 WebFetch 阅读它的 references 部分\n   - 在 Semantic Scholar 上查看它的 \"cited by\" — 最近引用它的论文很可能是 concurrent work\n   - 对 3 个以上核心相关论文重复此步骤\n\n### 搜索数量建议（理想目标，上下文充裕时尽量达到）\n\n| 角色 | 建议搜索次数 | 说明 |\n|------|-------------|------|\n| Round 1 Generator | 10-15 次 | 每个方向争取 3 次独立搜索 |\n| Round 2 Generator | 5-8 次 | 验证 approach 可行性 + baseline |\n| Review Agent | 8-12 次 | 独立验证 + 竞争论文 + 反面证据 |\n| Revision Agent | 5-10 次 | 针对每个 issue 独立调研 |\n\n### 上下文管理\n\n你的输出 token 有限，必须在上下文耗尽之前完成 JSON 输出。\n\n- 上述搜索次数是理想目标。在上下文充裕时应尽量多搜、深搜，搜得越充分越好。\n- 但必须动态评估剩余上下文：如果已经消耗了大量上下文，应优先完成输出，不要为了凑次数而冒着无法输出的风险。\n- WebFetch 深度阅读很有价值，但每次 fetch 消耗大量 token——优先 fetch 最关键的 2-3 篇，而不是每篇都 fetch。\n- 质量 > 数量：5 次精准搜索 + 深度思考 > 15 次浅层搜索。\n\n\nAs a reviewer, your search focus should be:\n1. **验证 claim**：Generator 声称的 SOTA、gap、novelty 是否属实\n2. **找竞争论文**：是否有 Generator 遗漏的高度相关/相似的工作\n3. **找反面证据**：是否有论文表明 Generator 的 approach 行不通\n4. **引用链检查**：通过核心论文的 cited-by 发现 concurrent work\n\n## 竞争论文专项搜索（Reviewer 独有）\n\n这是你作为 Reviewer 最重要的职责之一——发现 Generator 遗漏的竞争工作：\n\n1. **关键词变体搜索**：用至少 3 种不同的关键词组合搜索同一个问题\n   - 同义词替换（e.g., 'efficient' → 'lightweight/fast/scalable'）\n   - 不同粒度（e.g., 'text classification' → 'sentiment analysis' → 'NLP'）\n   - 方法名 + 任务名的不同组合\n\n2. **知名团队追踪**：如果你知道哪些团队/实验室在做相关方向，\n   搜索他们最近的论文（`\"team_name\" OR \"author_name\" {topic} {year}`）\n\n3. **会议最新录用**：搜索最近一轮 ICML/NeurIPS/ICLR/AAAI/ACL 等会议的 accepted papers\n   - `site:openreview.net {topic} 2026`\n   - `{conference_name} 2026 accepted papers {topic}`\n\n4. **arXiv 近 3 个月密集搜索**：对精确相关的关键词，搜索过去 3 个月的 arXiv 论文\n   这是发现 concurrent work 最有效的窗口\n\n如果你发现了 Generator 遗漏的重要相关工作，必须在 issues 中列出论文标题和链接，\n并在 feedback 中说明这些工作如何影响 idea 的 novelty。\n\n## Review checklist\n1. **SOTA freshness**: Are the models/baselines cited actually current SOTA?\n   If outdated, specify what the current SOTA is and cite your source.\n2. **Reference verification**: Do the cited papers actually exist? (WebSearch to check)\n3. **Gap validity**: Does the claimed research gap still exist, or has recent work addressed it?\n4. **Venue validity**: Are target_venues' submission deadlines after 2026-05-10?\n5. **Feasibility**: Is the resource estimate realistic? Are there hidden dependencies?\n6. **Novelty**: Is this sufficiently different from existing work?\n   When scoring novelty < 4:\n   - You MUST identify the closest existing work(s) via WebSearch\n   - In your feedback, write: \"This idea is too similar to [Paper Title (Venue Year)]. Specifically, [what overlaps]. To differentiate, the generator should [suggestion].\"\n   - This gives the generator targeted guidance to boost novelty, not just \"be more novel\".\n7. **Cost realism across modes**: Are the three mode estimates (manual/human-in-loop/auto) internally consistent?\n   - Auto Research uses more GPU hours (2-5x manual) but GPU idle rate should be near zero\n   - Auto Research timeline should reflect resource availability as bottleneck — days with sufficient GPUs, not weeks\n   - Human-in-Loop should fall between manual and auto on most dimensions\n   - Manual and HIL must NOT include salary/wages — only GPU and API costs\n   - Auto Research must NOT include agent operational overhead\n   - If any mode estimate is clearly unrealistic, flag it\n\n## Idea under review (round 5/10)\n{\n  \"title\": \"CompLocoGen: Grammar-Structured Transition Feasibility Learning for Compositional Humanoid Loco-Manipulation Task Generation\",\n  \"core_problem\": \"Scaling humanoid loco-manipulation to diverse real-world tasks requires diverse training environments, but every loco-manipulation task in NVIDIA's AGILE/GR00T-WBC ecosystem must be manually specified as a self-contained Isaac Lab configuration file. VIRAL (CVPR 2026) demonstrates composite tasks work but identifies reward engineering as a scaling bottleneck. Eurekaverse (CoRL 2024) pioneered LLM-driven environment curriculum generation but only for single-skill training (quadruped parkour), generating environment variations rather than compositionally coupled multi-stage tasks. LLM-based reward methods (STRIDE, FORGE/EUREKA) automate reward optimization for single predefined tasks but cannot generate compositionally coupled tasks where inter-primitive dynamics (balance during walk-to-pick transitions, gait adaptation for carry, CoM shifts at primitive boundaries) create emergent failure modes absent from any individual primitive. The fundamental challenge is twofold: (1) composing novel multi-stage loco-manipulation tasks from a primitive grammar, and (2) efficiently predicting which compositions are dynamically feasible without exhaustive simulation—requiring a learned transition feasibility model that generalizes across primitive types and parameters. How can we combine a physics-informed skill grammar with a learned Transition Feasibility Network to automatically generate diverse, dynamically feasible loco-manipulation task configurations for Isaac Lab?\",\n  \"opportunity\": \"VIRAL (CVPR 2026) achieves 54 consecutive real-world loco-manipulation cycles on G1 but relies entirely on hand-designed stage-weighted rewards—the authors state that 'scaling to the open-ended diversity of daily life remains intractable' via manual reward engineering. Eurekaverse (CoRL 2024) automates environment curriculum generation via LLM code generation with agent-environment co-evolution, achieving superhuman parkour curricula—but operates on single-skill locomotion over terrain, with no manipulation, no inter-primitive coupling, and no compositional task structure. STRIDE (arXiv:2502.04692) and FORGE (OpenReview 2025) automate reward design for single tasks. DemoHLM (arXiv:2510.11258) generates diverse humanoid loco-manipulation trajectories from a single demonstration via object-centric replay—producing spatial variations of one task template but not compositionally novel tasks. LHM-Humanoid (arXiv:2508.16943) achieves impressive long-horizon loco-manipulation across 350 scenes but relies on manually designed configurations. Genie Sim 3.0 (arXiv:2601.02078) uses LLM-powered scene generation with 200+ tasks and 5140 assets but lacks formal compositional task specification and degrades on multi-step tasks (~52% vs ~80% for atomic tasks). In the learned composition space, Generative Skill Chaining (arXiv:2401.03360) uses diffusion models for skill precondition/effect chaining, and GSC (Robotics & Autonomous Systems, 2024) models skill sets as GNN graphs—but both target fixed-base manipulation without dynamics-aware feasibility for whole-body locomotion+manipulation coupling. SuperDyno (ICLR 2025 Workshop) learns neural dynamics for humanoid control but not for composition feasibility prediction. The gap is precise: no system combines (1) a grammar for compositional loco-manipulation task generation with (2) a learned transition feasibility predictor that efficiently determines which compositions are dynamically viable, enabling (3) active generation of training data for the AGILE/GR00T-WBC ecosystem.\",\n  \"landscape\": \"**LLM-based environment/curriculum generation**: Eurekaverse (arXiv:2411.01775, CoRL 2024) uses LLM code generation to produce increasingly challenging terrain environments for quadruped parkour, with agent-environment co-evolution over 5 generations. Key paradigm: LLM generates Python terrain functions → train policy → evaluate → feedback to LLM. However, it generates monolithic terrain programs for single-skill locomotion—no manipulation, no inter-primitive dynamics, no compositional task structure. CompLocoGen extends this paradigm to compositional multi-stage loco-manipulation: instead of varying a single environment, we compose multi-primitive task sequences and learn which compositions are dynamically feasible. Genie Sim 3.0 (arXiv:2601.02078, AgiBot, Jan 2026) uses LLM-powered scene generation with RAG-based asset retrieval and DSL code generation to create thousands of diverse environments for humanoid manipulation across 200+ tasks—but lacks formal compositional grammar and shows performance degradation on multi-step tasks. **LLM-based reward design (per-task optimization)**: STRIDE (arXiv:2502.04692, Feb 2025) automates humanoid locomotion reward design via LLMs, 250% over EUREKA—single-task locomotion only. FORGE (OpenReview 2025) uses multi-agent LLMs for evolutionary reward refinement, 38.5% over EUREKA—single-task. EUREKA (ICLR 2024) established the LLM-to-reward-code paradigm. These solve per-task reward engineering; CompLocoGen solves the orthogonal problem of generating novel task compositions with learned feasibility prediction. **Demonstration-based data generation**: DemoHLM (arXiv:2510.11258) generates diverse humanoid loco-manipulation trajectories from a single teleoperated demonstration by converting to object-centric representations and replaying under varied initial conditions with a 3-stage pipeline (locomotion → pre-manipulation → manipulation) on Unitree G1. It produces spatial diversity within a fixed task template—not compositional novelty across task structures. CompLocoGen generates qualitatively different training data: novel task compositions (e.g., walk-pick-carry-climb_stairs-place) that no single demonstration could cover. **Learned skill composition approaches**: Generative Skill Chaining (arXiv:2401.03360, CoRL 2024) trains skill-level diffusion models capturing (precondition, parameters, effect) distributions for chaining—fixed-base manipulation only. SCaR (NeurIPS 2024) refines skill chaining with learned success predictors for sub-task transitions. GSC (Robotics & Autonomous Systems, 2024) models skill sets as GNN graphs with transformer-style architecture for skill embeddings. SuperDyno (ICLR 2025 Workshop) learns differentiable neural dynamics for humanoid whole-body control. None of these address composition feasibility for coupled loco-manipulation where locomotion dynamics (balance, gait) interact with manipulation state (load, grasp). CompLocoGen's Transition Feasibility Network operates specifically on the boundary states between loco-manipulation primitives, learning to predict whether locomotion-manipulation coupling will cause failure at transitions. **Sim-to-real composite tasks**: VIRAL/GR00T-VisualSim2Real (CVPR 2026, NVlabs) demonstrates composite loco-manipulation with 54 consecutive real-world cycles—hand-designed tasks. LHM-Humanoid (arXiv:2508.16943, March 2026) learns unified policies across 350 manually designed scenes via RL teacher distillation. FALCON (arXiv:2505.06776, L4DC 2026) demonstrates force-adaptive dual-agent RL for loco-manipulation on real humanoids—hand-designed tasks. WholeBodyVLA (ICLR 2026, arXiv:2512.11047) learns unified latent VLA—policy architecture orthogonal to task generation. **Scene graph and compositional approaches**: Scene Graph Atomic Skills (ICRA 2026) uses GNN + diffusion for compositional skill execution addressing distribution shifts from scene composition—tabletop manipulation focus. GenManip (CVPR 2025) provides LLM-to-simulation-to-filter for tabletop manipulation. Humanoid Hanoi (arXiv:2602.13850, Feb 2026) demonstrates distribution shift during skill composition requiring data aggregation—directly informs our transition modeling. **The specific gap**: No system combines grammar-structured compositional task generation with a learned transition feasibility predictor for humanoid loco-manipulation. Eurekaverse generates single-skill environments; DemoHLM augments single demonstrations; Generative Skill Chaining/GSC learn feasibility for fixed-base manipulation; VIRAL/LHM-Humanoid use manually designed compositions. CompLocoGen uniquely combines: (a) a 7-primitive grammar generating exponentially many task compositions, (b) a GNN-based Transition Feasibility Network that learns loco-manipulation coupling dynamics from few-shot simulation rollouts, and (c) active generation targeting the uncertainty frontier of the feasibility predictor.\",\n  \"approach\": \"We build CompLocoGen as a grammar-structured system that learns transition feasibility for compositional loco-manipulation task generation, producing Isaac Lab-compatible configurations within 200 H100-hours.\\n\\n**Expanded Physics-Informed Skill Grammar (7 Primitives)**: We define a context-free grammar over seven coupled loco-manipulation primitives: walk(target_pos, speed, gait_style), pick(object_id, grasp_type, approach_vector), place(target_pos, placement_constraint), carry(object_id, carry_pose, stability_mode), push(object_id, direction, force_profile), open_door(door_id, handle_type, opening_angle), and squat(target_height, duration, stability_mode). Each primitive has typed spatial parameters, structural preconditions/postconditions, and a boundary state specification (the distribution of robot states—CoM position/velocity, joint configurations, contact states, grasp forces—at primitive entry/exit). The 7-primitive grammar produces 7^L valid structural sequences of length L (before feasibility filtering). For L=3-5 (typical loco-manipulation tasks), this yields 343-16,807 structural compositions. With parameter variation (3-5 settings per typed parameter), the effective task space is 10^4-10^6 unique configurations. Structural filtering (precondition/postcondition satisfaction) reduces this by ~60%; dynamic feasibility filtering further reduces by an experimentally measured factor—quantifying this reduction IS the key experimental result.\\n\\n**Transition Feasibility Network (TFN) — Core Algorithmic Contribution**: Instead of relying solely on analytical physics predicates (ZMP, centroidal dynamics), we introduce a GNN-based Transition Feasibility Network that learns to predict composition success probability from primitive boundary states. Architecture: Each primitive instance is a node with features encoding (primitive type, spatial parameters, expected boundary state statistics). Edges connect consecutive primitives in the composition. A message-passing GNN (3 layers, 128-dim) processes the composition graph and outputs per-edge transition feasibility scores ∈ [0,1] plus an overall composition feasibility score. Training proceeds in three phases: (1) Bootstrap: Seed the TFN with ~200 simulation rollouts (50 per transition type for the 4 most common transitions: walk→pick, pick→carry, carry→walk, walk→place) using analytical predicates to stratify sampling across feasible/infeasible boundary. (2) Active Learning: Use TFN uncertainty (MC-dropout variance) to identify which transition types and parameter regions have highest prediction uncertainty. Allocate simulation budget preferentially to these uncertain regions. After each batch of 50 rollouts, retrain TFN. (3) Generalization: Evaluate TFN's ability to predict feasibility for novel primitive types (push, open_door, squat) from only 20-30 rollouts per new transition type—testing whether the learned dynamics representations transfer across primitive types that share physical structure (e.g., all primitives involving load shifts share centroidal coupling features). The TFN's advantage over analytical predicates: (a) it captures non-obvious interaction effects that simplified analytical models miss (e.g., arm momentum during open_door affecting walking balance), (b) it improves with data rather than requiring manual engineering of new physics equations for each primitive type, (c) it provides calibrated uncertainty estimates enabling active generation. The TFN's advantage over monolithic learned feasibility models (e.g., training a classifier on full-task rollouts): the grammar structure means it only needs to learn local transition dynamics (O(P^2) transition types for P primitives = 49 for 7 primitives), not global task success from all possible sequences (exponential in length).\\n\\n**LLM-Guided Task Program Generation with Grammar Constraints**: The LLM (Qwen 3.6-35B-A3B) generates task programs as grammar-valid primitive sequences with spatial parameter bindings. The LLM reasons about task semantics (delivery routes, obstacle navigation, sequential manipulation schedules) while the grammar enforces structural validity and the TFN provides differentiable feasibility scores for soft-constraining the LLM's parameter choices. Generated programs are compiled into Isaac Lab Python @configclass environment configurations using AGILE's configuration-driven architecture: each becomes a self-contained file specifying scene setup, observation space, action space, staged reward functions (auto-generated from primitive sequence structure following VIRAL's stage-weighted approach), termination conditions, and curriculum parameters.\\n\\n**Active Composition Generation Loop**: Inspired by Eurekaverse's co-evolution but targeting compositional diversity rather than single-skill difficulty: (1) Generate batch of grammar-valid compositions via LLM. (2) TFN scores each composition; compositions above threshold proceed to simulation, compositions below threshold are rejected, compositions in the uncertain band are prioritized for simulation (active learning). (3) Simulate accepted compositions in Isaac Lab (4096 parallel environments). (4) Update TFN with new rollout data. (5) LLM receives feedback on which compositions succeeded/failed and why (structured failure mode analysis: balance failure, grasp loss, collision, timeout). This loop iterates for ~10 generations, progressively expanding the frontier of achievable compositions.\\n\\n**Pre-trained GR00T-WBC Execution**: Pre-trained SONIC locomotion checkpoint + PinkKinematics IK for upper-body manipulation. State-machine coordinator sequences SONIC commands and IK targets based on primitive transitions. For primitives requiring novel coordination (push, open_door), fine-tune with <5 H100-hours per primitive type using AGILE's training pipeline.\\n\\n**Downstream Evaluation with Compositional Generalization**: Train diffusion policy (ACT architecture) on generated datasets. Evaluate: (a) held-out compositions (novel primitive sequences), (b) held-out spatial configurations, (c) held-out dynamic parameters, (d) novel primitive types added post-training. Baselines: (1) Eurekaverse-style single-skill environment co-evolution (adapted to loco-manipulation: generate environment variations for individual primitives, then manually compose), (2) DemoHLM-style demo augmentation (single demo per task → spatial variations), (3) STRIDE-style per-task reward optimization for composed tasks, (4) Grammar-only composition with analytical predicates (no TFN), (5) Grammar + TFN without active learning (random composition sampling), (6) LLM-only generation without grammar constraints, (7) LHM-Humanoid-style manually designed task set (5-8 hand-designed compositions). Key ablations: TFN vs. analytical predicates (measures value of learning), active vs. random sampling (measures value of uncertainty-guided generation), grammar structure vs. unstructured composition (measures value of grammatical scaffold for learning).\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"~180-200h H100\",\n      \"gpu_utilization\": \"25-35% effective; researcher idles GPU while designing grammar, implementing TFN architecture, debugging SONIC+IK integration, and iterating active learning loop\",\n      \"timeline\": \"7-8 weeks (1.5 weeks grammar design + TFN architecture + SONIC integration, 2 weeks TFN training + active generation loop, 2 weeks downstream training + evaluation, 1.5 weeks ablations + paper)\",\n      \"team\": \"1 researcher (requires familiarity with Isaac Lab, GNN training, and AGILE/GR00T-WBC)\",\n      \"estimated_gpu_cost\": \"$450-500 at ~$2.50/hr H100 spot pricing\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"~170-200h H100\",\n      \"gpu_utilization\": \"55-70%; agent automates configclass generation, TFN training loops, experiment scheduling; idles during human review of TFN architecture decisions and generated task quality\",\n      \"timeline\": \"6-7 weeks (targeting Humanoids 2026 June 30 deadline, 51 days)\",\n      \"team\": \"1 researcher, ~25-35min/day reviewing TFN training curves, generated compositions, and demonstration quality\",\n      \"claude_api_cost\": \"$200-400 (2000-4000 agentic turns for Isaac Lab compilation, TFN training orchestration, and experiment analysis)\",\n      \"estimated_gpu_cost\": \"$425-500 at ~$2.50/hr H100 spot pricing\",\n      \"budget_breakdown\": \"~10h TFN bootstrap data collection (200 rollouts × 4096 envs), ~5h TFN training (GNN, fast on single GPU), ~5h SONIC fine-tuning for push/open_door/squat, ~60h active generation loop (10 generations × ~6h per generation: LLM generation + simulation verification + TFN update), ~60h downstream diffusion policy training, ~40h ablations (7 baselines + 3 key ablations), ~20h buffer/iteration\",\n      \"risk_note\": \"Primary risk: TFN may overfit to bootstrap distribution and fail to generalize to novel transition types with only 20-30 rollouts. Mitigation: architecture uses primitive-type-agnostic physical features (CoM velocity, contact forces, joint torques at boundaries) rather than type-specific embeddings. Secondary risk: SONIC checkpoint may need more than 5h fine-tuning for push/open_door primitives.\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"~190-200h H100 (budget-constrained)\",\n      \"gpu_utilization\": \"80-90%; agent operates continuously, prioritizing TFN active learning loop\",\n      \"timeline\": \"3-4 weeks with 4 H100 GPUs concurrently\",\n      \"team\": \"0 (initial 3-hour setup: configure AGILE, verify SONIC checkpoint, set LLM API keys, define TFN architecture)\",\n      \"claude_api_cost\": \"$350-750 (3500-7500 turns for autonomous pipeline development, TFN training, active generation, and paper drafting)\",\n      \"estimated_gpu_cost\": \"$475-500 at ~$2.50/hr H100 spot pricing\",\n      \"speed_bottleneck\": \"Active learning loop requires sequential TFN updates between generation batches; physics verification throughput (4096 envs per H100, ~15 wall-clock hours for 1000 valid demonstrations)\",\n      \"risk_note\": \"Agent may over-explore TFN architecture variants vs. downstream evaluation; strict budget requires early stopping\"\n    }\n  },\n  \"target_venues\": [\n    \"Humanoids 2026 (paper deadline June 30, 2026 — 51 days, primary target. Ideal venue: humanoid-specific systems+algorithmic contribution, values both the grammar engineering and TFN learning contribution; conference Dec 6-9, Santa Clara CA)\",\n    \"ICRA 2027 (expected deadline ~September 2026 — allows extended ablations, potential real-robot transfer via AGILE's sim-to-real pipeline, and TFN generalization to more primitive types)\",\n    \"CoRL 2027 (expected deadline ~June 2027 — full learning-theoretic analysis of grammar-structured active feasibility learning, formal sample complexity bounds)\"\n  ],\n  \"level\": \"solid-to-strong\",\n  \"key_references\": [\n    \"Eurekaverse: Environment Curriculum Generation via Large Language Models (CoRL 2024, arXiv:2411.01775, NVIDIA Research) — LLM-driven environment co-evolution for single-skill locomotion training; generates terrain programs for quadruped parkour. Key paradigm ancestor. Differentiation: single-skill environment variation vs. our compositional multi-stage task generation with learned transition dynamics\",\n    \"VIRAL: Visual Sim-to-Real at Scale for Humanoid Loco-Manipulation (CVPR 2026, arXiv:2511.15200, NVlabs) — hand-designed composite tasks on G1 with 54 consecutive real-world cycles; identifies reward engineering as scaling bottleneck. Primary comparison\",\n    \"DemoHLM: From One Demonstration to Generalizable Humanoid Loco-Manipulation (arXiv:2510.11258) — generates diverse trajectories from single demo via object-centric representation replay on Unitree G1. Produces spatial variations within fixed task template. Key data-generation baseline: demonstrates demo-augmentation cannot produce compositional novelty\",\n    \"AGILE: A Comprehensive Workflow for Humanoid Loco-Manipulation Learning (arXiv:2603.20147, March 2026, github.com/nvidia-isaac/WBC-AGILE, Apache 2.0) — target substrate; configuration-driven Isaac Lab workflow. CompLocoGen generates upstream training task configurations\",\n    \"Generative Skill Chaining: Long-Horizon Skill Planning with Diffusion Models (arXiv:2401.03360, CoRL 2024) — trains skill-level diffusion models for precondition/effect-based chaining in fixed-base manipulation. Informs our TFN's per-edge feasibility prediction but does not address loco-manipulation coupling\",\n    \"GSC: A Graph-based Skill Composition Framework for Robot Learning (Robotics & Autonomous Systems, 2024) — GNN over skill graphs with transformer-style architecture. Architectural inspiration for our Transition Feasibility Network\",\n    \"SCaR: Refining Skill Chaining for Long-Horizon Robotic Manipulation (NeurIPS 2024) — learned success predictors for sub-task transitions; validates that transition feasibility can be learned from few-shot rollouts\",\n    \"SuperDyno: Scalable Humanoid Whole-Body Control via Differentiable Neural Network Dynamics (ICLR 2025 Workshop) — learns neural dynamics for humanoid control replacing analytical simulators. Validates that humanoid dynamics can be captured by neural networks\",\n    \"Genie Sim 3.0 (arXiv:2601.02078, AgiBot, Jan 2026) — LLM-powered scene generation with 200+ tasks, 5140 assets. Large-scale generation without compositional grammar; performance degrades on multi-step tasks\",\n    \"STRIDE: Automating Reward Design for Humanoid Robotics Locomotion (arXiv:2502.04692, Feb 2025) — automates single-task locomotion reward design via LLMs, 250% over EUREKA. Cannot compose multi-stage tasks\",\n    \"FORGE: Forging Better Rewards via Multi-Agent LLM Framework (OpenReview 2025) — multi-agent LLM reward evolution, 38.5% over EUREKA. Single-task; does not address task composition\",\n    \"EUREKA: Human-Level Reward Design via Coding LLMs (ICLR 2024, arXiv:2310.12931) — established LLM reward optimization paradigm\",\n    \"LHM-Humanoid: Learning a Unified Policy for Long-Horizon Humanoid Whole-Body Loco-Manipulation (arXiv:2508.16943, March 2026) — 350 diverse scenes, RL teacher + DAgger. Manually designed scenes; CompLocoGen could serve as automated task generator\",\n    \"WholeBodyVLA: Towards Unified Latent VLA for Whole-Body Loco-Manipulation Control (ICLR 2026, arXiv:2512.11047) — policy architecture orthogonal to task generation\",\n    \"FALCON: Learning Force-Adaptive Humanoid Loco-Manipulation (arXiv:2505.06776, L4DC 2026) — force-adaptive dual-agent RL on real humanoids; validates deployability, hand-designed tasks\",\n    \"Scene Graph Atomic Skills (ICRA 2026, Harvard) — GNN + diffusion for compositional skill execution addressing distribution shifts from scene composition; tabletop focus\",\n    \"Humanoid Hanoi (arXiv:2602.13850, Feb 2026) — distribution shift during skill composition; directly informs our transition feasibility learning\",\n    \"GR00T-WholeBodyControl/SONIC (NVlabs, open-source Apache 2.0) — pre-trained G1 locomotion checkpoints (142K+ motions), decoupled WBC\",\n    \"GenManip: LLM-driven Simulation for Generalizable Manipulation (CVPR 2025) — LLM-to-simulation-to-filter paradigm for tabletop manipulation\",\n    \"GR00T-Gen (NVIDIA, 2025) — generates 100+ individual tasks, not compositionally coupled\",\n    \"Isaac Lab (arXiv:2511.04831) — Python @configclass manager-based workflow for environment specification\",\n    \"SkillBlender (arXiv:2506.09366) — compositional skill blending on G1, manual specification\"\n  ],\n  \"description\": \"We propose CompLocoGen, a system that combines a physics-informed skill grammar with a learned Transition Feasibility Network (TFN) to automatically generate diverse humanoid loco-manipulation training environments for NVIDIA's AGILE/Isaac Lab ecosystem—within 200 H100-hours. The core algorithmic contribution is the TFN: a GNN-based model that learns to predict whether primitive transitions in a composed task sequence will succeed, trained via active learning from targeted simulation rollouts at primitive boundaries. This addresses a limitation of both analytical approaches (which require manual engineering per primitive type and miss non-obvious coupling effects) and monolithic learned models (which face exponential sample complexity in composition length). The grammar provides structure that makes transition feasibility learnable from O(100) rollouts per transition type: instead of learning global task success (exponential), the TFN learns local boundary dynamics (quadratic in primitive count). We define a 7-primitive grammar (walk, pick, place, carry, push, open_door, squat) producing 10^4-10^6 parametrized compositions, and quantify how structural filtering, analytical predicates, and learned TFN filtering progressively reduce this space to dynamically feasible tasks. An active generation loop (inspired by Eurekaverse's co-evolution but targeting compositional diversity) iteratively expands the frontier of achievable compositions by allocating simulation budget to high-uncertainty transition regions. Generated task programs compile to Isaac Lab @configclass configurations. Execution leverages GR00T-WBC's pre-trained SONIC locomotion and PinkKinematics IK. Evaluation compares against 7 baselines including Eurekaverse-style single-skill co-evolution, DemoHLM-style demo augmentation, STRIDE-style per-task reward optimization, and grammar-only analytical filtering—with key ablations isolating the value of learned feasibility, active sampling, and grammar structure. Primary target: Humanoids 2026 (June 30, 51 days).\",\n  \"project_name\": \"llm_locomanip_factory\",\n  \"source\": \"web_research\"\n}\n\n\n## Previous review history\n### Round 1 review\nVerdict: revise\nIssues: [\"CRITICAL OMISSION: NVIDIA GR00T-Gen (2025-2026) already uses LLMs and generative AI to create diverse tasks and simulation-ready environments for humanoid robots, with 100+ tasks spanning manipulation/locomotion/navigation, 2500+ 3D assets, and cross-embodiment humanoid support. This is not cited or discussed in the landscape. The claimed gap ('no system automatically composes and generates diverse humanoid loco-manipulation demonstrations') is overstated.\", \"FRAMEWORK INCOMPATIBILITY: SkillBlender is built on legged_gym/humanoid-gym/unitree_rl_gym, NOT Isaac Lab. The proposal assumes SkillBlender pretrained primitives (walk/reach/squat/step) can be bootstrapped into Isaac Lab G1 environments, but these have fundamentally different APIs, observation spaces, action conventions, and reward structures. Porting is a multi-week engineering effort alone.\", \"MISSING REFERENCE: EgoHumanoid (arXiv:2602.10106, Feb 2026) from OpenDriveLab addresses humanoid loco-manipulation data generation through robot-free egocentric demonstrations, achieving 51% improvement over robot-only baselines on G1. This concurrent work in the same problem space is not discussed.\", \"CONTROLLER INTEGRATION COMPLEXITY UNDERESTIMATED: Combining RL-locomotion from SkillBlender (different framework), IK-manipulation from Isaac Lab PR#3150's PinkKinematics, and MCTS refinement adapted from HumanoidGen (designed for fixed-base bimanual manipulation) requires integrating three unrelated codebases. Physics coupling between locomotion and manipulation (balance during lifting, force propagation during walking-while-carrying) makes this significantly harder than sequential composition.\", \"TIMELINE MISMATCH: The manual estimate is 3-5 months, yet the auto-research timeline claims 1-3 weeks. The 20-day CoRL deadline is incompatible with the acknowledged complexity. Physics simulation debugging for coupled loco-manipulation (contact instabilities, IK solver divergence) requires human intuition the generator's own risk note acknowledges.\", \"DreamControl-v2 (arXiv:2604.00202, March 2026) generates diverse humanoid motion trajectories via trainable guided diffusion priors, validated on Unitree G1. While the approach differs (diffusion vs. compositional programming), the paper addresses the same goal of scalable humanoid trajectory generation and should be more carefully contrasted.\", \"COMPUTE BUDGET CONCERN: Training multiple diffusion policies across varying dataset sizes for scaling law analysis, plus running thousands of Isaac Lab simulations for compositional data generation (including failed MCTS rollouts), will likely exceed the 200 H100-hour budget. HumanoidGen reports scaling experiments at smaller scope; this proposal's combinatorial approach generates many more candidate trajectories.\", \"COMBINATORIAL DIVERSITY OVERCLAIMED: Physics simulation failure rates for coupled loco-manipulation will be high—maintaining balance while performing diverse manipulation actions (carrying trays while navigating obstacles, squatting to pick up items while maintaining stability) is notoriously fragile in sim. The effective yield of 'thousands' of valid demonstrations from compositional generation is likely much lower than claimed.\"]\nFeedback: The core direction (automated compositional data generation for humanoid loco-manipulation) addresses a real need, but the proposal has significant gaps requiring revision:\n\n1. **Address GR00T-Gen directly**: NVIDIA GR00T-Gen already does LLM-based task/environment generation for humanoid robots. You must explicitly differentiate—GR00T-Gen appears to generate individual tasks (manipulation, locomotion, navigation) separately, not compositionally coupled loco-manipulation. Make this distinction the centerpiece of your novelty claim, but verify it first.\n\n2. **Fix the SkillBlender/Isaac Lab incompatibility**: Either (a) commit to porting SkillBlender primitives to Isaac Lab and budget 5-7 days for this alone, or (b) build the entire pipeline on legged_gym/humanoid-gym where SkillBlender already works, or (c) abandon SkillBlender and train locomotion primitives from scratch in Isaac Lab using existing reward functions. Option (b) is fastest but loses PinkKinematics IK from PR#3150.\n\n3. **Reduce scope for CoRL deadline**: Given 20 days, consider: (a) dropping MCTS refinement and using simpler rejection sampling, (b) supporting only 2-3 skill primitives (walk+pick+place) rather than 7, (c) using a single downstream policy architecture rather than scaling law analysis. A narrow but solid contribution beats an ambitious but incomplete one.\n\n4. **Target Humanoids 2026 instead**: With a June 30 deadline (50 days), the timeline becomes more realistic. This also better matches the venue focus.\n\n5. **Add EgoHumanoid and GR00T-Gen to landscape analysis**: Both are highly relevant concurrent/competing work that reviewers will notice if omitted.\n\n6. **Be honest about diversity yield**: Report expected success rate of compositional task generation (what fraction of LLM-generated task programs produce physically valid demonstrations) as a metric, not just total generated count.\n\n### Round 2 review\nVerdict: revise\nIssues: [\"CRITICAL: COMPUTE BUDGET VIOLATES USER'S HARD CONSTRAINT. User specifies ≤200 H100-hours total. Proposal estimates 300-400h (manual), 350-500h (HIL), 600-900h (auto). Even the absolute minimum (300h) is 50% over budget. The proposal must be redesigned to fit within 200 H100-hours.\", \"TIMELINE MISMATCH: User specifically targets CoRL 2026 (20 days). Proposal honestly says CoRL is 'only feasible if pipeline is substantially complete by submission' and targets Humanoids 2026 (50 days) as primary venue. This doesn't match the user's requirement.\", \"MISSING COMPETING WORK: GR00T-VisualSim2Real (NVIDIA, open-source Apache 2.0) implements VIRAL composite loco-manipulation tasks (Walk-Stand-Drop-Grasp-Turn) on G1 with sim-to-real transfer. While tasks are hand-designed, this is a relevant baseline and evaluation comparison that should be discussed.\", \"MISSING RELEVANT WORK: Humanoid Hanoi (arXiv:2602.13850, Feb 2026) demonstrates skill composition through shared whole-body controller with important finding about distribution shift during composition. Their data aggregation procedure for maintaining controller robustness across novel skill compositions is directly relevant to CompLocoGen's approach.\", \"LOCOMOTION RL FROM SCRATCH IS UNNECESSARY: Isaac Lab already has pre-trained G1 locomotion policies (demonstrated in PRs #3150/#3259 and AGILE). Training from scratch wastes 50-100 H100-hours that could be saved by using existing checkpoints, which is critical given the budget constraint.\", \"NOVELTY CONCERN: The methodology (LLM generates task programs → execute in simulation → filter by physics verification) is well-established by RoboGen (ICML 2024), GenManip (CVPR 2025), and HumanoidGen (NeurIPS 2025). The specific application to coupled loco-manipulation is novel, but reviewers may view this as straightforward domain transfer of an existing paradigm rather than a new method.\", \"AGILE (NVIDIA, March 2026) provides a configuration-driven Isaac Lab workflow for G1 loco-manipulation with YAML task descriptors. CompLocoGen could be positioned as an automated task composer sitting on top of AGILE's descriptor system—this would strengthen the contribution by building on official NVIDIA infrastructure rather than reimplementing.\", \"EVALUATION SCOPE TOO NARROW: Training a single diffusion policy on generated vs baseline data tests only one downstream consumer. The user's eval requirement mentions VLA training as well. With the tight compute budget, the proposal should either commit to a single strong evaluation or explain why one architecture suffices.\"]\nFeedback: The core idea is solid and the gap is real, but two critical constraint violations must be fixed:\n\n1. **FIT WITHIN 200 H100-HOURS**: The most effective cuts: (a) Use Isaac Lab's existing pre-trained G1 locomotion policy from PR #3150 instead of training from scratch (-50-100h); (b) Reduce the number of generated demonstrations and ablation experiments; (c) Use a single downstream policy evaluation (skip scaling curves); (d) Run rejection sampling with fewer parallel environments. A realistic 200h budget: ~5h locomotion policy fine-tuning, ~50h LLM-driven task generation + rejection sampling (4096 envs), ~50h downstream diffusion policy training, ~50h ablations, ~45h buffer. This requires aggressive scope reduction but the core contribution (compositional grammar + LLM generation + physics filtering) can still be demonstrated.\n\n2. **ADDRESS CoRL 2026 TIMELINE (20 days)**: Either (a) commit to a minimal-viable submission: 4 primitives, pre-trained locomotion (no RL training), 5-10 task compositions, single downstream evaluation—this is tight but possible if Isaac Lab infrastructure works immediately; OR (b) explicitly argue why Humanoids 2026 (50 days) better serves the contribution and accept that CoRL 2026 cannot be met.\n\n3. **STRENGTHEN NOVELTY**: Position the contribution not just as 'LLM generates tasks' (done before) but emphasize: (a) the formal grammar with typed spatial parameters and precondition/postcondition logic for ensuring physical validity of compositions, (b) the physics-aware feedback loop (structured error messages back to LLM), (c) demonstrate that compositional generation produces qualitatively different training data than augmenting existing demos (compare against OmniRetarget/GR00T-Mimic baselines).\n\n4. **ADD AGILE as build substrate**: Frame CompLocoGen as an automated task composer that plugs into AGILE's descriptor architecture. This (a) reduces engineering effort, (b) inherits AGILE's evaluation pipeline, (c) makes the contribution clearly complementary to NVIDIA's ecosystem rather than competing with it.\n\n5. **Add GR00T-VisualSim2Real VIRAL and Humanoid Hanoi to landscape**—both are directly relevant to the compositional loco-manipulation setting.\n\n### Round 3 review\nVerdict: revise\nIssues: [\"MISSING COMPETING WORK: STRIDE (arXiv:2502.04692, Feb 2025) automates reward design for humanoid locomotion via LLMs, outperforming EUREKA by 250%. FORGE (OpenReview 2025) uses multi-agent LLMs for reward evolution with 38.5% gains on Humanoid. These directly address the 'reward engineering bottleneck' that CompLocoGen claims to solve. A reviewer familiar with these would ask: why not use STRIDE-like iterative reward generation for each composed task, bypassing the need for grammar-constrained reward templates?\", \"AGILE YAML DESCRIPTOR MISCHARACTERIZATION: AGILE's YAML descriptors are deployment I/O contracts (joint names, observation ordering, action scaling, history buffers) for sim2sim/sim2real transfer—NOT training task specifications. Isaac Lab defines environments via Python @configclass in the manager-based workflow. The proposal needs to either (a) generate Python environment configs (not YAML), or (b) clarify exactly which AGILE configuration format it targets. This affects the core 'AGILE-native' claim.\", \"CoRL 2026 TIMELINE REMAINS UNREALISTIC: 20 days to abstract, including SONIC+PinkKinematics integration, LLM grammar+prompt engineering, data generation, downstream policy training, ablations, and paper writing. Even with 'minimal-viable scope' (4 primitives, 5-8 compositions), the engineering integration risk alone (SONIC locomotion coordinated with IK manipulation via state machine) requires debugging cycles incompatible with this timeline.\", \"MISSING REFERENCE: 'Physically Consistent Humanoid Loco-Manipulation using Latent Diffusion Models' (arXiv:2504.16843, Humanoids 2025) generates physically consistent humanoid loco-manipulation trajectories via latent diffusion models + whole-body trajectory optimization. Different approach but same problem domain—should be discussed as an alternative generation paradigm.\", \"NOVELTY CONCERN FOR CoRL: The technical contribution reduces to (1) a context-free grammar over 4 primitives with typed preconditions, (2) LLM compilation to execution format, (3) standard rejection sampling with feedback. None of these components individually are novel. The combination applied to loco-manipulation is a valid systems contribution for Humanoids 2026 but may not clear CoRL's novelty bar, where reviewers expect algorithmic depth.\", \"40-60% YIELD RATE UNSUBSTANTIATED: No empirical or cited basis for this estimate. Coupled loco-manipulation transitions (balance during pick, grasp stability during walk, CoM shift during carry initiation) are notoriously failure-prone in simulation. The grammar prevents structurally invalid sequences but cannot predict dynamic failures. Without a pilot study, this number is speculative.\", \"EVALUATION BASELINE CONCERN: Comparing against 'Isaac Lab pick-navigate-place single-template (PR #3150)' is weak—it's a single task, not a method. The more meaningful comparison would be against STRIDE/FORGE-style automated reward generation applied per-task, or against GR00T-Gen's task diversity within NVIDIA's ecosystem. The current baselines don't adequately test whether the grammar-based composition approach adds value over simpler alternatives.\"]\nFeedback: The proposal has improved significantly from rounds 1-2 (compute budget fixed, pre-trained checkpoints used, landscape expanded), but three issues remain before passing:\n\n1. **BOOST NOVELTY BEYOND DOMAIN TRANSFER**: The grammar+LLM→execute→filter pipeline is well-known. To reach CoRL novelty, consider: (a) a physics-informed grammar that encodes dynamic constraints (not just precondition/postcondition logic but actual force/torque feasibility predictions from the grammar parameters—e.g., predicting whether carry(5kg) + walk(1.5m/s) is dynamically feasible BEFORE simulation, using learned dynamics models); (b) contrast explicitly with STRIDE/FORGE reward generation—argue that compositional task generation is fundamentally different from per-task reward generation (STRIDE generates one reward at a time; you generate coupled multi-stage tasks where inter-stage dynamics matter); (c) demonstrate emergent compositional generalization not achievable by any per-task method.\n\n2. **FIX AGILE DESCRIPTOR CLAIM**: Verify whether AGILE actually uses YAML for full task definition or only for deployment I/O. If the latter, either (a) reframe as generating Isaac Lab Python @configclass environments (which is what the LLM would actually need to output), or (b) define your own YAML task specification schema that compiles to Isaac Lab environments—and acknowledge this is your contribution, not AGILE's existing format.\n\n3. **TARGET Humanoids 2026 AS PRIMARY AND HONESTLY SCOPE FOR IT**: CoRL in 20 days is not feasible for a contribution requiring SONIC+IK integration, grammar design, generation pipeline, AND downstream evaluation. Commit to Humanoids 2026 (51 days) with full scope, and only mention CoRL if you can demonstrate the pipeline works in the first week. The user's requirement targets CoRL, but an honest 'minimal-viable CoRL submission is high-risk; Humanoids 2026 is the reliable path' is better than pretending 20 days suffices.\n\n4. **ADD STRIDE/FORGE TO LANDSCAPE AND DIFFERENTIATE**: These papers automate reward design via LLMs—the same bottleneck you claim to address. Your differentiation should be: STRIDE generates single-task rewards iteratively; CompLocoGen generates compositionally coupled multi-stage tasks where the grammar ensures inter-primitive physical consistency that per-task reward generation cannot guarantee.\n\n5. **SUBSTANTIATE YIELD RATE**: Either cite empirical data from related work (GenManip/HumanoidGen success rates) or commit to reporting this as an experimental metric rather than a prior estimate.\n\n### Round 4 review\nVerdict: revise\nIssues: [\"MISSING COMPETING WORK: Eurekaverse (CoRL 2024, NVIDIA Research) establishes LLM-driven environment curriculum generation with agent-environment co-evolution for RL training. While it targets quadrupedal parkour (not humanoid loco-manipulation), the paradigm—LLM generates diverse training environments, train policies, evaluate, feed back to LLM for next iteration—is essentially identical to CompLocoGen's pipeline. This must be cited and explicitly differentiated: Eurekaverse generates environment variations for single-skill training; CompLocoGen generates compositionally coupled multi-stage task configurations with inter-primitive dynamics constraints.\", \"MISSING BASELINE: DemoHLM (arXiv:2510.11258) generates diverse humanoid loco-manipulation trajectories from a single teleoperated demonstration by converting to object-centric representations and replaying under varied initial conditions. It uses a 3-stage pipeline (locomotion → pre-manipulation → manipulation) with a hierarchical controller on Unitree G1. While DemoHLM generates spatial variations of one task template rather than compositionally novel tasks, it should be added as a data-generation baseline to demonstrate that grammar-based composition produces qualitatively different (not just more) training data than demo-augmentation approaches.\", \"VENUE MISMATCH: The user explicitly targets CoRL 2026 (paper deadline May 29, 19 days away). The proposal honestly pivots to Humanoids 2026 (July 24, 75 days) as primary target. While this honesty is appreciated, the proposal must either: (a) commit to a minimal CoRL submission (2-3 task compositions, pre-trained everything, single downstream eval, no ablation depth) with Humanoids as the full version, or (b) clearly justify why CoRL is infeasible and Humanoids is the right venue. Currently the proposal lists Humanoids as primary but doesn't address how to satisfy the user's CoRL requirement.\", \"LIMITED COMPOSITIONAL SPACE: The grammar defines only 4 primitives (walk, pick, place, carry). The number of meaningfully distinct task compositions from 4 primitives is inherently limited. With structural and dynamic feasibility filtering, the effective compositional space may be quite small. The proposal should either (a) expand primitives (push, pull, open_door, climb_stairs, squat) to demonstrate the grammar's extensibility, or (b) provide analysis of how many compositionally distinct and dynamically feasible tasks the 4-primitive grammar can produce.\", \"NOVELTY DEPTH FOR CoRL: The technical contribution reduces to (1) a context-free grammar over 4 primitives with typed parameters and analytical physics predicates, (2) LLM-guided constrained generation with Qwen 3.6, (3) compilation to Isaac Lab @configclass, (4) rejection sampling with online predicate calibration. Each component individually uses standard techniques. The combination is novel for loco-manipulation, but CoRL reviewers may expect deeper algorithmic contribution—e.g., learning the dynamics predicates from data rather than hand-coding ZMP/centroidal analysis, or providing formal guarantees about compositional coverage/completeness. For Humanoids 2026, this systems contribution would be appropriately valued.\", \"GENIE SIM 3.0 (arXiv:2601.02078, AgiBot, Jan 2026) is a comprehensive simulation platform with LLM-powered scene generation that generates thousands of diverse environments for humanoid robots across 200+ tasks. While it focuses on scene construction rather than compositional task specification with physics constraints, it represents a relevant large-scale automated generation approach and should be briefly acknowledged in the landscape.\"]\nFeedback: The proposal has improved substantially across rounds 1-3 (compute budget fixed, AGILE configclass corrected, STRIDE/FORGE differentiated, yield rate as experimental metric). The core idea—dynamics-aware compositional grammar for humanoid loco-manipulation task generation—is genuinely valuable and addresses a real bottleneck. Three targeted changes would bring this to pass quality:\n\n1. **ADD EUREKAVERSE AND DemoHLM**: Eurekaverse (CoRL 2024) is the most important missing citation—it pioneered LLM-driven environment curriculum generation. Your differentiation is clear (single-skill environment variation vs. compositional multi-stage task generation with inter-primitive dynamics constraints) but must be explicitly stated. DemoHLM should be added as a data-generation baseline to show that compositional generation produces qualitatively different training data than demo augmentation.\n\n2. **RESOLVE VENUE STRATEGY**: Either (a) commit to a minimal CoRL abstract (May 26, 16 days): 4 primitives, 3-5 task compositions using pre-trained SONIC+IK, single downstream eval, no ablations—essentially a proof-of-concept showing the grammar works—with full paper at Humanoids 2026; OR (b) drop CoRL and commit fully to Humanoids 2026 with full scope. A split strategy (CoRL abstract as teaser, Humanoids as full paper) is viable if the pipeline can produce initial results in ~14 days.\n\n3. **EXPAND GRAMMAR OR JUSTIFY SCOPE**: Either add 2-3 more primitives (push, open_door, squat) to demonstrate extensibility, or provide explicit analysis of compositional diversity: how many unique task programs does the 4-primitive grammar produce? What fraction survive structural filtering? Dynamic filtering? This strengthens the contribution by quantifying the grammar's generative power.\n\nMinor: Add Genie Sim 3.0 to landscape (LLM-driven scene generation, different scope but related). Consider whether learning dynamics predicates (small MLP trained on simulation rollouts) rather than purely analytical models could provide an additional novelty dimension for CoRL framing.\n\n\n## Output format\nOutput ONLY a JSON object:\n{\n  \"verdict\": \"pass | revise | fail\",\n  \"scores\": {\n    \"novelty\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"feasibility\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"clarity\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"impact\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"}\n  },\n  \"issues\": [\"specific issue 1\", \"specific issue 2\", ...],\n  \"feedback\": \"Actionable feedback for the generator (if verdict=revise)\",\n  \"reason\": \"One-line summary of verdict rationale\"\n}\n\nRules:\n- \"pass\": idea is sound AND high quality — avg score >= 4.0, no critical issues\n- \"revise\": fixable issues OR scores below threshold — provide specific feedback\n- \"fail\": fundamental flaw (e.g., gap doesn't exist, approach provably wrong, or scores remain low after multiple revisions)\n- Threshold is HIGH (4.0/5.0): agent scores tend to be inflated, so only truly outstanding ideas should pass. An avg of 3.5 is NOT enough.\n- Round 10 only: if still \"revise\", you MUST choose \"pass\" or \"fail\"."
}
```

---

### Runtime record

_source line 2 · 2026-05-10T19:20:26.399Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-10T19:20:26.399Z",
  "sessionId": "c9f1e88d-7547-445a-bdb2-8a60925de079"
}
```

---

## Round 1

44 recorded events

### User

_source line 3 · 2026-05-10T19:20:26.675Z_

You are a strict ML research reviewer conducting adversarial review.

**Today's date: 2026-05-10 (UTC).**

Your job: independently verify this idea's claims via WebSearch, then issue a verdict.

## User requirements
The user asked for: **Target: CoRL 2026 (Austin, Nov 9-12, 2026). Abstract deadline 2026-05-26 (17 days); paper deadline 2026-05-29 (20 days).

Direction: Generative models specifically targeting HUMANOID robot training data — addressing the high-DoF, whole-body, loco-manipulation data scarcity that bottlenecks humanoid VLA / WM training. SCOPE LIMITED TO TWO CONTRIBUTION TYPES:
  (a) Generation ALGORITHMS — e.g., video diffusion conditioned on humanoid action streams, action-conditioned generative models, latent humanoid trajectory generators, physics-aware whole-body video generation.
  (b) Procedural data-generation PIPELINES — e.g., MimicGen-style automated demo multiplication for humanoids, procedural whole-body task/scene generation, automated quality filtering pipelines for synthetic humanoid trajectories.

OUT OF SCOPE: action retargeting innovations (human-video → humanoid-action retargeting). Treat existing retargeters (HumanPlus, OmniH2O) as black-box upstream tools if needed; do NOT propose new retargeting methods.

Recent landscape (do not duplicate): NVIDIA GR00T-Dreams, DexMimicGen, MimicGen extensions for humanoid, Helix self-supervised humanoid pipelines, Cosmos for synthetic humanoid video. Humanoid data scarcity is the #1 bottleneck cited in 2026 humanoid papers — high impact area.

Contribution type: METHOD ONLY. New generation algorithm OR new procedural pipeline. Not a new released humanoid dataset alone.

SIM-ONLY MITIGATION: Validate generated data by training a downstream humanoid policy/VLA in sim and comparing against models trained on baseline data. Frame contribution as method, not dataset.

HARD CONSTRAINTS:
1. Compute: ≤200 H100-hours total. Strategies: (a) fine-tune existing video diffusion (CogVideoX, OpenSora, Cosmos) with humanoid-action conditioning, (b) procedural pipeline that requires negligible training compute, (c) small efficient humanoid-specific generator that beats general baselines.
2. Time: ≤20 days. Build on HF Diffusers, OpenSora, NVIDIA Cosmos repos, Isaac Lab humanoid suite (G1, H1), MimicGen, RoboCasa with humanoid embodiments if available.
3. Eval: train humanoid policy/VLA on generated vs baseline data. Test on Isaac Lab humanoid manipulation/locomanipulation tasks, RoboCasa kitchen with humanoid embodiment, HumanoidBench. Report success rate + data efficiency curves.

Look for: physics-aware whole-body video generation with kinematic consistency, action-conditioned generators that exploit humanoid kinematic structure, procedural pipelines that produce diverse loco-manipulation (not just static manipulation) data, automatic quality filtering for synthetic humanoid trajectories. Avoid: any retargeting-based contribution, arm-only generation rebadged as humanoid, naive fine-tuning of video diffusion on humanoid clips without method.

Tag: direction=humanoid_data_gen, contribution_type=method. target_venues=["CoRL 2026"].**
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

## Idea under review (round 5/10)
{
  "title": "CompLocoGen: Grammar-Structured Transition Feasibility Learning for Compositional Humanoid Loco-Manipulation Task Generation",
  "core_problem": "Scaling humanoid loco-manipulation to diverse real-world tasks requires diverse training environments, but every loco-manipulation task in NVIDIA's AGILE/GR00T-WBC ecosystem must be manually specified as a self-contained Isaac Lab configuration file. VIRAL (CVPR 2026) demonstrates composite tasks work but identifies reward engineering as a scaling bottleneck. Eurekaverse (CoRL 2024) pioneered LLM-driven environment curriculum generation but only for single-skill training (quadruped parkour), generating environment variations rather than compositionally coupled multi-stage tasks. LLM-based reward methods (STRIDE, FORGE/EUREKA) automate reward optimization for single predefined tasks but cannot generate compositionally coupled tasks where inter-primitive dynamics (balance during walk-to-pick transitions, gait adaptation for carry, CoM shifts at primitive boundaries) create emergent failure modes absent from any individual primitive. The fundamental challenge is twofold: (1) composing novel multi-stage loco-manipulation tasks from a primitive grammar, and (2) efficiently predicting which compositions are dynamically feasible without exhaustive simulation—requiring a learned transition feasibility model that generalizes across primitive types and parameters. How can we combine a physics-informed skill grammar with a learned Transition Feasibility Network to automatically generate diverse, dynamically feasible loco-manipulation task configurations for Isaac Lab?",
  "opportunity": "VIRAL (CVPR 2026) achieves 54 consecutive real-world loco-manipulation cycles on G1 but relies entirely on hand-designed stage-weighted rewards—the authors state that 'scaling to the open-ended diversity of daily life remains intractable' via manual reward engineering. Eurekaverse (CoRL 2024) automates environment curriculum generation via LLM code generation with agent-environment co-evolution, achieving superhuman parkour curricula—but operates on single-skill locomotion over terrain, with no manipulation, no inter-primitive coupling, and no compositional task structure. STRIDE (arXiv:2502.04692) and FORGE (OpenReview 2025) automate reward design for single tasks. DemoHLM (arXiv:2510.11258) generates diverse humanoid loco-manipulation trajectories from a single demonstration via object-centric replay—producing spatial variations of one task template but not compositionally novel tasks. LHM-Humanoid (arXiv:2508.16943) achieves impressive long-horizon loco-manipulation across 350 scenes but relies on manually designed configurations. Genie Sim 3.0 (arXiv:2601.02078) uses LLM-powered scene generation with 200+ tasks and 5140 assets but lacks formal compositional task specification and degrades on multi-step tasks (~52% vs ~80% for atomic tasks). In the learned composition space, Generative Skill Chaining (arXiv:2401.03360) uses diffusion models for skill precondition/effect chaining, and GSC (Robotics & Autonomous Systems, 2024) models skill sets as GNN graphs—but both target fixed-base manipulation without dynamics-aware feasibility for whole-body locomotion+manipulation coupling. SuperDyno (ICLR 2025 Workshop) learns neural dynamics for humanoid control but not for composition feasibility prediction. The gap is precise: no system combines (1) a grammar for compositional loco-manipulation task generation with (2) a learned transition feasibility predictor that efficiently determines which compositions are dynamically viable, enabling (3) active generation of training data for the AGILE/GR00T-WBC ecosystem.",
  "landscape": "**LLM-based environment/curriculum generation**: Eurekaverse (arXiv:2411.01775, CoRL 2024) uses LLM code generation to produce increasingly challenging terrain environments for quadruped parkour, with agent-environment co-evolution over 5 generations. Key paradigm: LLM generates Python terrain functions → train policy → evaluate → feedback to LLM. However, it generates monolithic terrain programs for single-skill locomotion—no manipulation, no inter-primitive dynamics, no compositional task structure. CompLocoGen extends this paradigm to compositional multi-stage loco-manipulation: instead of varying a single environment, we compose multi-primitive task sequences and learn which compositions are dynamically feasible. Genie Sim 3.0 (arXiv:2601.02078, AgiBot, Jan 2026) uses LLM-powered scene generation with RAG-based asset retrieval and DSL code generation to create thousands of diverse environments for humanoid manipulation across 200+ tasks—but lacks formal compositional grammar and shows performance degradation on multi-step tasks. **LLM-based reward design (per-task optimization)**: STRIDE (arXiv:2502.04692, Feb 2025) automates humanoid locomotion reward design via LLMs, 250% over EUREKA—single-task locomotion only. FORGE (OpenReview 2025) uses multi-agent LLMs for evolutionary reward refinement, 38.5% over EUREKA—single-task. EUREKA (ICLR 2024) established the LLM-to-reward-code paradigm. These solve per-task reward engineering; CompLocoGen solves the orthogonal problem of generating novel task compositions with learned feasibility prediction. **Demonstration-based data generation**: DemoHLM (arXiv:2510.11258) generates diverse humanoid loco-manipulation trajectories from a single teleoperated demonstration by converting to object-centric representations and replaying under varied initial conditions with a 3-stage pipeline (locomotion → pre-manipulation → manipulation) on Unitree G1. It produces spatial diversity within a fixed task template—not compositional novelty across task structures. CompLocoGen generates qualitatively different training data: novel task compositions (e.g., walk-pick-carry-climb_stairs-place) that no single demonstration could cover. **Learned skill composition approaches**: Generative Skill Chaining (arXiv:2401.03360, CoRL 2024) trains skill-level diffusion models capturing (precondition, parameters, effect) distributions for chaining—fixed-base manipulation only. SCaR (NeurIPS 2024) refines skill chaining with learned success predictors for sub-task transitions. GSC (Robotics & Autonomous Systems, 2024) models skill sets as GNN graphs with transformer-style architecture for skill embeddings. SuperDyno (ICLR 2025 Workshop) learns differentiable neural dynamics for humanoid whole-body control. None of these address composition feasibility for coupled loco-manipulation where locomotion dynamics (balance, gait) interact with manipulation state (load, grasp). CompLocoGen's Transition Feasibility Network operates specifically on the boundary states between loco-manipulation primitives, learning to predict whether locomotion-manipulation coupling will cause failure at transitions. **Sim-to-real composite tasks**: VIRAL/GR00T-VisualSim2Real (CVPR 2026, NVlabs) demonstrates composite loco-manipulation with 54 consecutive real-world cycles—hand-designed tasks. LHM-Humanoid (arXiv:2508.16943, March 2026) learns unified policies across 350 manually designed scenes via RL teacher distillation. FALCON (arXiv:2505.06776, L4DC 2026) demonstrates force-adaptive dual-agent RL for loco-manipulation on real humanoids—hand-designed tasks. WholeBodyVLA (ICLR 2026, arXiv:2512.11047) learns unified latent VLA—policy architecture orthogonal to task generation. **Scene graph and compositional approaches**: Scene Graph Atomic Skills (ICRA 2026) uses GNN + diffusion for compositional skill execution addressing distribution shifts from scene composition—tabletop manipulation focus. GenManip (CVPR 2025) provides LLM-to-simulation-to-filter for tabletop manipulation. Humanoid Hanoi (arXiv:2602.13850, Feb 2026) demonstrates distribution shift during skill composition requiring data aggregation—directly informs our transition modeling. **The specific gap**: No system combines grammar-structured compositional task generation with a learned transition feasibility predictor for humanoid loco-manipulation. Eurekaverse generates single-skill environments; DemoHLM augments single demonstrations; Generative Skill Chaining/GSC learn feasibility for fixed-base manipulation; VIRAL/LHM-Humanoid use manually designed compositions. CompLocoGen uniquely combines: (a) a 7-primitive grammar generating exponentially many task compositions, (b) a GNN-based Transition Feasibility Network that learns loco-manipulation coupling dynamics from few-shot simulation rollouts, and (c) active generation targeting the uncertainty frontier of the feasibility predictor.",
  "approach": "We build CompLocoGen as a grammar-structured system that learns transition feasibility for compositional loco-manipulation task generation, producing Isaac Lab-compatible configurations within 200 H100-hours.\n\n**Expanded Physics-Informed Skill Grammar (7 Primitives)**: We define a context-free grammar over seven coupled loco-manipulation primitives: walk(target_pos, speed, gait_style), pick(object_id, grasp_type, approach_vector), place(target_pos, placement_constraint), carry(object_id, carry_pose, stability_mode), push(object_id, direction, force_profile), open_door(door_id, handle_type, opening_angle), and squat(target_height, duration, stability_mode). Each primitive has typed spatial parameters, structural preconditions/postconditions, and a boundary state specification (the distribution of robot states—CoM position/velocity, joint configurations, contact states, grasp forces—at primitive entry/exit). The 7-primitive grammar produces 7^L valid structural sequences of length L (before feasibility filtering). For L=3-5 (typical loco-manipulation tasks), this yields 343-16,807 structural compositions. With parameter variation (3-5 settings per typed parameter), the effective task space is 10^4-10^6 unique configurations. Structural filtering (precondition/postcondition satisfaction) reduces this by ~60%; dynamic feasibility filtering further reduces by an experimentally measured factor—quantifying this reduction IS the key experimental result.\n\n**Transition Feasibility Network (TFN) — Core Algorithmic Contribution**: Instead of relying solely on analytical physics predicates (ZMP, centroidal dynamics), we introduce a GNN-based Transition Feasibility Network that learns to predict composition success probability from primitive boundary states. Architecture: Each primitive instance is a node with features encoding (primitive type, spatial parameters, expected boundary state statistics). Edges connect consecutive primitives in the composition. A message-passing GNN (3 layers, 128-dim) processes the composition graph and outputs per-edge transition feasibility scores ∈ [0,1] plus an overall composition feasibility score. Training proceeds in three phases: (1) Bootstrap: Seed the TFN with ~200 simulation rollouts (50 per transition type for the 4 most common transitions: walk→pick, pick→carry, carry→walk, walk→place) using analytical predicates to stratify sampling across feasible/infeasible boundary. (2) Active Learning: Use TFN uncertainty (MC-dropout variance) to identify which transition types and parameter regions have highest prediction uncertainty. Allocate simulation budget preferentially to these uncertain regions. After each batch of 50 rollouts, retrain TFN. (3) Generalization: Evaluate TFN's ability to predict feasibility for novel primitive types (push, open_door, squat) from only 20-30 rollouts per new transition type—testing whether the learned dynamics representations transfer across primitive types that share physical structure (e.g., all primitives involving load shifts share centroidal coupling features). The TFN's advantage over analytical predicates: (a) it captures non-obvious interaction effects that simplified analytical models miss (e.g., arm momentum during open_door affecting walking balance), (b) it improves with data rather than requiring manual engineering of new physics equations for each primitive type, (c) it provides calibrated uncertainty estimates enabling active generation. The TFN's advantage over monolithic learned feasibility models (e.g., training a classifier on full-task rollouts): the grammar structure means it only needs to learn local transition dynamics (O(P^2) transition types for P primitives = 49 for 7 primitives), not global task success from all possible sequences (exponential in length).\n\n**LLM-Guided Task Program Generation with Grammar Constraints**: The LLM (Qwen 3.6-35B-A3B) generates task programs as grammar-valid primitive sequences with spatial parameter bindings. The LLM reasons about task semantics (delivery routes, obstacle navigation, sequential manipulation schedules) while the grammar enforces structural validity and the TFN provides differentiable feasibility scores for soft-constraining the LLM's parameter choices. Generated programs are compiled into Isaac Lab Python @configclass environment configurations using AGILE's configuration-driven architecture: each becomes a self-contained file specifying scene setup, observation space, action space, staged reward functions (auto-generated from primitive sequence structure following VIRAL's stage-weighted approach), termination conditions, and curriculum parameters.\n\n**Active Composition Generation Loop**: Inspired by Eurekaverse's co-evolution but targeting compositional diversity rather than single-skill difficulty: (1) Generate batch of grammar-valid compositions via LLM. (2) TFN scores each composition; compositions above threshold proceed to simulation, compositions below threshold are rejected, compositions in the uncertain band are prioritized for simulation (active learning). (3) Simulate accepted compositions in Isaac Lab (4096 parallel environments). (4) Update TFN with new rollout data. (5) LLM receives feedback on which compositions succeeded/failed and why (structured failure mode analysis: balance failure, grasp loss, collision, timeout). This loop iterates for ~10 generations, progressively expanding the frontier of achievable compositions.\n\n**Pre-trained GR00T-WBC Execution**: Pre-trained SONIC locomotion checkpoint + PinkKinematics IK for upper-body manipulation. State-machine coordinator sequences SONIC commands and IK targets based on primitive transitions. For primitives requiring novel coordination (push, open_door), fine-tune with <5 H100-hours per primitive type using AGILE's training pipeline.\n\n**Downstream Evaluation with Compositional Generalization**: Train diffusion policy (ACT architecture) on generated datasets. Evaluate: (a) held-out compositions (novel primitive sequences), (b) held-out spatial configurations, (c) held-out dynamic parameters, (d) novel primitive types added post-training. Baselines: (1) Eurekaverse-style single-skill environment co-evolution (adapted to loco-manipulation: generate environment variations for individual primitives, then manually compose), (2) DemoHLM-style demo augmentation (single demo per task → spatial variations), (3) STRIDE-style per-task reward optimization for composed tasks, (4) Grammar-only composition with analytical predicates (no TFN), (5) Grammar + TFN without active learning (random composition sampling), (6) LLM-only generation without grammar constraints, (7) LHM-Humanoid-style manually designed task set (5-8 hand-designed compositions). Key ablations: TFN vs. analytical predicates (measures value of learning), active vs. random sampling (measures value of uncertainty-guided generation), grammar structure vs. unstructured composition (measures value of grammatical scaffold for learning).",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "~180-200h H100",
      "gpu_utilization": "25-35% effective; researcher idles GPU while designing grammar, implementing TFN architecture, debugging SONIC+IK integration, and iterating active learning loop",
      "timeline": "7-8 weeks (1.5 weeks grammar design + TFN architecture + SONIC integration, 2 weeks TFN training + active generation loop, 2 weeks downstream training + evaluation, 1.5 weeks ablations + paper)",
      "team": "1 researcher (requires familiarity with Isaac Lab, GNN training, and AGILE/GR00T-WBC)",
      "estimated_gpu_cost": "$450-500 at ~$2.50/hr H100 spot pricing"
    },
    "human_in_loop": {
      "gpu_hours": "~170-200h H100",
      "gpu_utilization": "55-70%; agent automates configclass generation, TFN training loops, experiment scheduling; idles during human review of TFN architecture decisions and generated task quality",
      "timeline": "6-7 weeks (targeting Humanoids 2026 June 30 deadline, 51 days)",
      "team": "1 researcher, ~25-35min/day reviewing TFN training curves, generated compositions, and demonstration quality",
      "claude_api_cost": "$200-400 (2000-4000 agentic turns for Isaac Lab compilation, TFN training orchestration, and experiment analysis)",
      "estimated_gpu_cost": "$425-500 at ~$2.50/hr H100 spot pricing",
      "budget_breakdown": "~10h TFN bootstrap data collection (200 rollouts × 4096 envs), ~5h TFN training (GNN, fast on single GPU), ~5h SONIC fine-tuning for push/open_door/squat, ~60h active generation loop (10 generations × ~6h per generation: LLM generation + simulation verification + TFN update), ~60h downstream diffusion policy training, ~40h ablations (7 baselines + 3 key ablations), ~20h buffer/iteration",
      "risk_note": "Primary risk: TFN may overfit to bootstrap distribution and fail to generalize to novel transition types with only 20-30 rollouts. Mitigation: architecture uses primitive-type-agnostic physical features (CoM velocity, contact forces, joint torques at boundaries) rather than type-specific embeddings. Secondary risk: SONIC checkpoint may need more than 5h fine-tuning for push/open_door primitives."
    },
    "auto_research": {
      "gpu_hours": "~190-200h H100 (budget-constrained)",
      "gpu_utilization": "80-90%; agent operates continuously, prioritizing TFN active learning loop",
      "timeline": "3-4 weeks with 4 H100 GPUs concurrently",
      "team": "0 (initial 3-hour setup: configure AGILE, verify SONIC checkpoint, set LLM API keys, define TFN architecture)",
      "claude_api_cost": "$350-750 (3500-7500 turns for autonomous pipeline development, TFN training, active generation, and paper drafting)",
      "estimated_gpu_cost": "$475-500 at ~$2.50/hr H100 spot pricing",
      "speed_bottleneck": "Active learning loop requires sequential TFN updates between generation batches; physics verification throughput (4096 envs per H100, ~15 wall-clock hours for 1000 valid demonstrations)",
      "risk_note": "Agent may over-explore TFN architecture variants vs. downstream evaluation; strict budget requires early stopping"
    }
  },
  "target_venues": [
    "Humanoids 2026 (paper deadline June 30, 2026 — 51 days, primary target. Ideal venue: humanoid-specific systems+algorithmic contribution, values both the grammar engineering and TFN learning contribution; conference Dec 6-9, Santa Clara CA)",
    "ICRA 2027 (expected deadline ~September 2026 — allows extended ablations, potential real-robot transfer via AGILE's sim-to-real pipeline, and TFN generalization to more primitive types)",
    "CoRL 2027 (expected deadline ~June 2027 — full learning-theoretic analysis of grammar-structured active feasibility learning, formal sample complexity bounds)"
  ],
  "level": "solid-to-strong",
  "key_references": [
    "Eurekaverse: Environment Curriculum Generation via Large Language Models (CoRL 2024, arXiv:2411.01775, NVIDIA Research) — LLM-driven environment co-evolution for single-skill locomotion training; generates terrain programs for quadruped parkour. Key paradigm ancestor. Differentiation: single-skill environment variation vs. our compositional multi-stage task generation with learned transition dynamics",
    "VIRAL: Visual Sim-to-Real at Scale for Humanoid Loco-Manipulation (CVPR 2026, arXiv:2511.15200, NVlabs) — hand-designed composite tasks on G1 with 54 consecutive real-world cycles; identifies reward engineering as scaling bottleneck. Primary comparison",
    "DemoHLM: From One Demonstration to Generalizable Humanoid Loco-Manipulation (arXiv:2510.11258) — generates diverse trajectories from single demo via object-centric representation replay on Unitree G1. Produces spatial variations within fixed task template. Key data-generation baseline: demonstrates demo-augmentation cannot produce compositional novelty",
    "AGILE: A Comprehensive Workflow for Humanoid Loco-Manipulation Learning (arXiv:2603.20147, March 2026, github.com/nvidia-isaac/WBC-AGILE, Apache 2.0) — target substrate; configuration-driven Isaac Lab workflow. CompLocoGen generates upstream training task configurations",
    "Generative Skill Chaining: Long-Horizon Skill Planning with Diffusion Models (arXiv:2401.03360, CoRL 2024) — trains skill-level diffusion models for precondition/effect-based chaining in fixed-base manipulation. Informs our TFN's per-edge feasibility prediction but does not address loco-manipulation coupling",
    "GSC: A Graph-based Skill Composition Framework for Robot Learning (Robotics & Autonomous Systems, 2024) — GNN over skill graphs with transformer-style architecture. Architectural inspiration for our Transition Feasibility Network",
    "SCaR: Refining Skill Chaining for Long-Horizon Robotic Manipulation (NeurIPS 2024) — learned success predictors for sub-task transitions; validates that transition feasibility can be learned from few-shot rollouts",
    "SuperDyno: Scalable Humanoid Whole-Body Control via Differentiable Neural Network Dynamics (ICLR 2025 Workshop) — learns neural dynamics for humanoid control replacing analytical simulators. Validates that humanoid dynamics can be captured by neural networks",
    "Genie Sim 3.0 (arXiv:2601.02078, AgiBot, Jan 2026) — LLM-powered scene generation with 200+ tasks, 5140 assets. Large-scale generation without compositional grammar; performance degrades on multi-step tasks",
    "STRIDE: Automating Reward Design for Humanoid Robotics Locomotion (arXiv:2502.04692, Feb 2025) — automates single-task locomotion reward design via LLMs, 250% over EUREKA. Cannot compose multi-stage tasks",
    "FORGE: Forging Better Rewards via Multi-Agent LLM Framework (OpenReview 2025) — multi-agent LLM reward evolution, 38.5% over EUREKA. Single-task; does not address task composition",
    "EUREKA: Human-Level Reward Design via Coding LLMs (ICLR 2024, arXiv:2310.12931) — established LLM reward optimization paradigm",
    "LHM-Humanoid: Learning a Unified Policy for Long-Horizon Humanoid Whole-Body Loco-Manipulation (arXiv:2508.16943, March 2026) — 350 diverse scenes, RL teacher + DAgger. Manually designed scenes; CompLocoGen could serve as automated task generator",
    "WholeBodyVLA: Towards Unified Latent VLA for Whole-Body Loco-Manipulation Control (ICLR 2026, arXiv:2512.11047) — policy architecture orthogonal to task generation",
    "FALCON: Learning Force-Adaptive Humanoid Loco-Manipulation (arXiv:2505.06776, L4DC 2026) — force-adaptive dual-agent RL on real humanoids; validates deployability, hand-designed tasks",
    "Scene Graph Atomic Skills (ICRA 2026, Harvard) — GNN + diffusion for compositional skill execution addressing distribution shifts from scene composition; tabletop focus",
    "Humanoid Hanoi (arXiv:2602.13850, Feb 2026) — distribution shift during skill composition; directly informs our transition feasibility learning",
    "GR00T-WholeBodyControl/SONIC (NVlabs, open-source Apache 2.0) — pre-trained G1 locomotion checkpoints (142K+ motions), decoupled WBC",
    "GenManip: LLM-driven Simulation for Generalizable Manipulation (CVPR 2025) — LLM-to-simulation-to-filter paradigm for tabletop manipulation",
    "GR00T-Gen (NVIDIA, 2025) — generates 100+ individual tasks, not compositionally coupled",
    "Isaac Lab (arXiv:2511.04831) — Python @configclass manager-based workflow for environment specification",
    "SkillBlender (arXiv:2506.09366) — compositional skill blending on G1, manual specification"
  ],
  "description": "We propose CompLocoGen, a system that combines a physics-informed skill grammar with a learned Transition Feasibility Network (TFN) to automatically generate diverse humanoid loco-manipulation training environments for NVIDIA's AGILE/Isaac Lab ecosystem—within 200 H100-hours. The core algorithmic contribution is the TFN: a GNN-based model that learns to predict whether primitive transitions in a composed task sequence will succeed, trained via active learning from targeted simulation rollouts at primitive boundaries. This addresses a limitation of both analytical approaches (which require manual engineering per primitive type and miss non-obvious coupling effects) and monolithic learned models (which face exponential sample complexity in composition length). The grammar provides structure that makes transition feasibility learnable from O(100) rollouts per transition type: instead of learning global task success (exponential), the TFN learns local boundary dynamics (quadratic in primitive count). We define a 7-primitive grammar (walk, pick, place, carry, push, open_door, squat) producing 10^4-10^6 parametrized compositions, and quantify how structural filtering, analytical predicates, and learned TFN filtering progressively reduce this space to dynamically feasible tasks. An active generation loop (inspired by Eurekaverse's co-evolution but targeting compositional diversity) iteratively expands the frontier of achievable compositions by allocating simulation budget to high-uncertainty transition regions. Generated task programs compile to Isaac Lab @configclass configurations. Execution leverages GR00T-WBC's pre-trained SONIC locomotion and PinkKinematics IK. Evaluation compares against 7 baselines including Eurekaverse-style single-skill co-evolution, DemoHLM-style demo augmentation, STRIDE-style per-task reward optimization, and grammar-only analytical filtering—with key ablations isolating the value of learned feasibility, active sampling, and grammar structure. Primary target: Humanoids 2026 (June 30, 51 days).",
  "project_name": "llm_locomanip_factory",
  "source": "web_research"
}


## Previous review history
### Round 1 review
Verdict: revise
Issues: ["CRITICAL OMISSION: NVIDIA GR00T-Gen (2025-2026) already uses LLMs and generative AI to create diverse tasks and simulation-ready environments for humanoid robots, with 100+ tasks spanning manipulation/locomotion/navigation, 2500+ 3D assets, and cross-embodiment humanoid support. This is not cited or discussed in the landscape. The claimed gap ('no system automatically composes and generates diverse humanoid loco-manipulation demonstrations') is overstated.", "FRAMEWORK INCOMPATIBILITY: SkillBlender is built on legged_gym/humanoid-gym/unitree_rl_gym, NOT Isaac Lab. The proposal assumes SkillBlender pretrained primitives (walk/reach/squat/step) can be bootstrapped into Isaac Lab G1 environments, but these have fundamentally different APIs, observation spaces, action conventions, and reward structures. Porting is a multi-week engineering effort alone.", "MISSING REFERENCE: EgoHumanoid (arXiv:2602.10106, Feb 2026) from OpenDriveLab addresses humanoid loco-manipulation data generation through robot-free egocentric demonstrations, achieving 51% improvement over robot-only baselines on G1. This concurrent work in the same problem space is not discussed.", "CONTROLLER INTEGRATION COMPLEXITY UNDERESTIMATED: Combining RL-locomotion from SkillBlender (different framework), IK-manipulation from Isaac Lab PR#3150's PinkKinematics, and MCTS refinement adapted from HumanoidGen (designed for fixed-base bimanual manipulation) requires integrating three unrelated codebases. Physics coupling between locomotion and manipulation (balance during lifting, force propagation during walking-while-carrying) makes this significantly harder than sequential composition.", "TIMELINE MISMATCH: The manual estimate is 3-5 months, yet the auto-research timeline claims 1-3 weeks. The 20-day CoRL deadline is incompatible with the acknowledged complexity. Physics simulation debugging for coupled loco-manipulation (contact instabilities, IK solver divergence) requires human intuition the generator's own risk note acknowledges.", "DreamControl-v2 (arXiv:2604.00202, March 2026) generates diverse humanoid motion trajectories via trainable guided diffusion priors, validated on Unitree G1. While the approach differs (diffusion vs. compositional programming), the paper addresses the same goal of scalable humanoid trajectory generation and should be more carefully contrasted.", "COMPUTE BUDGET CONCERN: Training multiple diffusion policies across varying dataset sizes for scaling law analysis, plus running thousands of Isaac Lab simulations for compositional data generation (including failed MCTS rollouts), will likely exceed the 200 H100-hour budget. HumanoidGen reports scaling experiments at smaller scope; this proposal's combinatorial approach generates many more candidate trajectories.", "COMBINATORIAL DIVERSITY OVERCLAIMED: Physics simulation failure rates for coupled loco-manipulation will be high—maintaining balance while performing diverse manipulation actions (carrying trays while navigating obstacles, squatting to pick up items while maintaining stability) is notoriously fragile in sim. The effective yield of 'thousands' of valid demonstrations from compositional generation is likely much lower than claimed."]
Feedback: The core direction (automated compositional data generation for humanoid loco-manipulation) addresses a real need, but the proposal has significant gaps requiring revision:

1. **Address GR00T-Gen directly**: NVIDIA GR00T-Gen already does LLM-based task/environment generation for humanoid robots. You must explicitly differentiate—GR00T-Gen appears to generate individual tasks (manipulation, locomotion, navigation) separately, not compositionally coupled loco-manipulation. Make this distinction the centerpiece of your novelty claim, but verify it first.

2. **Fix the SkillBlender/Isaac Lab incompatibility**: Either (a) commit to porting SkillBlender primitives to Isaac Lab and budget 5-7 days for this alone, or (b) build the entire pipeline on legged_gym/humanoid-gym where SkillBlender already works, or (c) abandon SkillBlender and train locomotion primitives from scratch in Isaac Lab using existing reward functions. Option (b) is fastest but loses PinkKinematics IK from PR#3150.

3. **Reduce scope for CoRL deadline**: Given 20 days, consider: (a) dropping MCTS refinement and using simpler rejection sampling, (b) supporting only 2-3 skill primitives (walk+pick+place) rather than 7, (c) using a single downstream policy architecture rather than scaling law analysis. A narrow but solid contribution beats an ambitious but incomplete one.

4. **Target Humanoids 2026 instead**: With a June 30 deadline (50 days), the timeline becomes more realistic. This also better matches the venue focus.

5. **Add EgoHumanoid and GR00T-Gen to landscape analysis**: Both are highly relevant concurrent/competing work that reviewers will notice if omitted.

6. **Be honest about diversity yield**: Report expected success rate of compositional task generation (what fraction of LLM-generated task programs produce physically valid demonstrations) as a metric, not just total generated count.

### Round 2 review
Verdict: revise
Issues: ["CRITICAL: COMPUTE BUDGET VIOLATES USER'S HARD CONSTRAINT. User specifies ≤200 H100-hours total. Proposal estimates 300-400h (manual), 350-500h (HIL), 600-900h (auto). Even the absolute minimum (300h) is 50% over budget. The proposal must be redesigned to fit within 200 H100-hours.", "TIMELINE MISMATCH: User specifically targets CoRL 2026 (20 days). Proposal honestly says CoRL is 'only feasible if pipeline is substantially complete by submission' and targets Humanoids 2026 (50 days) as primary venue. This doesn't match the user's requirement.", "MISSING COMPETING WORK: GR00T-VisualSim2Real (NVIDIA, open-source Apache 2.0) implements VIRAL composite loco-manipulation tasks (Walk-Stand-Drop-Grasp-Turn) on G1 with sim-to-real transfer. While tasks are hand-designed, this is a relevant baseline and evaluation comparison that should be discussed.", "MISSING RELEVANT WORK: Humanoid Hanoi (arXiv:2602.13850, Feb 2026) demonstrates skill composition through shared whole-body controller with important finding about distribution shift during composition. Their data aggregation procedure for maintaining controller robustness across novel skill compositions is directly relevant to CompLocoGen's approach.", "LOCOMOTION RL FROM SCRATCH IS UNNECESSARY: Isaac Lab already has pre-trained G1 locomotion policies (demonstrated in PRs #3150/#3259 and AGILE). Training from scratch wastes 50-100 H100-hours that could be saved by using existing checkpoints, which is critical given the budget constraint.", "NOVELTY CONCERN: The methodology (LLM generates task programs → execute in simulation → filter by physics verification) is well-established by RoboGen (ICML 2024), GenManip (CVPR 2025), and HumanoidGen (NeurIPS 2025). The specific application to coupled loco-manipulation is novel, but reviewers may view this as straightforward domain transfer of an existing paradigm rather than a new method.", "AGILE (NVIDIA, March 2026) provides a configuration-driven Isaac Lab workflow for G1 loco-manipulation with YAML task descriptors. CompLocoGen could be positioned as an automated task composer sitting on top of AGILE's descriptor system—this would strengthen the contribution by building on official NVIDIA infrastructure rather than reimplementing.", "EVALUATION SCOPE TOO NARROW: Training a single diffusion policy on generated vs baseline data tests only one downstream consumer. The user's eval requirement mentions VLA training as well. With the tight compute budget, the proposal should either commit to a single strong evaluation or explain why one architecture suffices."]
Feedback: The core idea is solid and the gap is real, but two critical constraint violations must be fixed:

1. **FIT WITHIN 200 H100-HOURS**: The most effective cuts: (a) Use Isaac Lab's existing pre-trained G1 locomotion policy from PR #3150 instead of training from scratch (-50-100h); (b) Reduce the number of generated demonstrations and ablation experiments; (c) Use a single downstream policy evaluation (skip scaling curves); (d) Run rejection sampling with fewer parallel environments. A realistic 200h budget: ~5h locomotion policy fine-tuning, ~50h LLM-driven task generation + rejection sampling (4096 envs), ~50h downstream diffusion policy training, ~50h ablations, ~45h buffer. This requires aggressive scope reduction but the core contribution (compositional grammar + LLM generation + physics filtering) can still be demonstrated.

2. **ADDRESS CoRL 2026 TIMELINE (20 days)**: Either (a) commit to a minimal-viable submission: 4 primitives, pre-trained locomotion (no RL training), 5-10 task compositions, single downstream evaluation—this is tight but possible if Isaac Lab infrastructure works immediately; OR (b) explicitly argue why Humanoids 2026 (50 days) better serves the contribution and accept that CoRL 2026 cannot be met.

3. **STRENGTHEN NOVELTY**: Position the contribution not just as 'LLM generates tasks' (done before) but emphasize: (a) the formal grammar with typed spatial parameters and precondition/postcondition logic for ensuring physical validity of compositions, (b) the physics-aware feedback loop (structured error messages back to LLM), (c) demonstrate that compositional generation produces qualitatively different training data than augmenting existing demos (compare against OmniRetarget/GR00T-Mimic baselines).

4. **ADD AGILE as build substrate**: Frame CompLocoGen as an automated task composer that plugs into AGILE's descriptor architecture. This (a) reduces engineering effort, (b) inherits AGILE's evaluation pipeline, (c) makes the contribution clearly complementary to NVIDIA's ecosystem rather than competing with it.

5. **Add GR00T-VisualSim2Real VIRAL and Humanoid Hanoi to landscape**—both are directly relevant to the compositional loco-manipulation setting.

### Round 3 review
Verdict: revise
Issues: ["MISSING COMPETING WORK: STRIDE (arXiv:2502.04692, Feb 2025) automates reward design for humanoid locomotion via LLMs, outperforming EUREKA by 250%. FORGE (OpenReview 2025) uses multi-agent LLMs for reward evolution with 38.5% gains on Humanoid. These directly address the 'reward engineering bottleneck' that CompLocoGen claims to solve. A reviewer familiar with these would ask: why not use STRIDE-like iterative reward generation for each composed task, bypassing the need for grammar-constrained reward templates?", "AGILE YAML DESCRIPTOR MISCHARACTERIZATION: AGILE's YAML descriptors are deployment I/O contracts (joint names, observation ordering, action scaling, history buffers) for sim2sim/sim2real transfer—NOT training task specifications. Isaac Lab defines environments via Python @configclass in the manager-based workflow. The proposal needs to either (a) generate Python environment configs (not YAML), or (b) clarify exactly which AGILE configuration format it targets. This affects the core 'AGILE-native' claim.", "CoRL 2026 TIMELINE REMAINS UNREALISTIC: 20 days to abstract, including SONIC+PinkKinematics integration, LLM grammar+prompt engineering, data generation, downstream policy training, ablations, and paper writing. Even with 'minimal-viable scope' (4 primitives, 5-8 compositions), the engineering integration risk alone (SONIC locomotion coordinated with IK manipulation via state machine) requires debugging cycles incompatible with this timeline.", "MISSING REFERENCE: 'Physically Consistent Humanoid Loco-Manipulation using Latent Diffusion Models' (arXiv:2504.16843, Humanoids 2025) generates physically consistent humanoid loco-manipulation trajectories via latent diffusion models + whole-body trajectory optimization. Different approach but same problem domain—should be discussed as an alternative generation paradigm.", "NOVELTY CONCERN FOR CoRL: The technical contribution reduces to (1) a context-free grammar over 4 primitives with typed preconditions, (2) LLM compilation to execution format, (3) standard rejection sampling with feedback. None of these components individually are novel. The combination applied to loco-manipulation is a valid systems contribution for Humanoids 2026 but may not clear CoRL's novelty bar, where reviewers expect algorithmic depth.", "40-60% YIELD RATE UNSUBSTANTIATED: No empirical or cited basis for this estimate. Coupled loco-manipulation transitions (balance during pick, grasp stability during walk, CoM shift during carry initiation) are notoriously failure-prone in simulation. The grammar prevents structurally invalid sequences but cannot predict dynamic failures. Without a pilot study, this number is speculative.", "EVALUATION BASELINE CONCERN: Comparing against 'Isaac Lab pick-navigate-place single-template (PR #3150)' is weak—it's a single task, not a method. The more meaningful comparison would be against STRIDE/FORGE-style automated reward generation applied per-task, or against GR00T-Gen's task diversity within NVIDIA's ecosystem. The current baselines don't adequately test whether the grammar-based composition approach adds value over simpler alternatives."]
Feedback: The proposal has improved significantly from rounds 1-2 (compute budget fixed, pre-trained checkpoints used, landscape expanded), but three issues remain before passing:

1. **BOOST NOVELTY BEYOND DOMAIN TRANSFER**: The grammar+LLM→execute→filter pipeline is well-known. To reach CoRL novelty, consider: (a) a physics-informed grammar that encodes dynamic constraints (not just precondition/postcondition logic but actual force/torque feasibility predictions from the grammar parameters—e.g., predicting whether carry(5kg) + walk(1.5m/s) is dynamically feasible BEFORE simulation, using learned dynamics models); (b) contrast explicitly with STRIDE/FORGE reward generation—argue that compositional task generation is fundamentally different from per-task reward generation (STRIDE generates one reward at a time; you generate coupled multi-stage tasks where inter-stage dynamics matter); (c) demonstrate emergent compositional generalization not achievable by any per-task method.

2. **FIX AGILE DESCRIPTOR CLAIM**: Verify whether AGILE actually uses YAML for full task definition or only for deployment I/O. If the latter, either (a) reframe as generating Isaac Lab Python @configclass environments (which is what the LLM would actually need to output), or (b) define your own YAML task specification schema that compiles to Isaac Lab environments—and acknowledge this is your contribution, not AGILE's existing format.

3. **TARGET Humanoids 2026 AS PRIMARY AND HONESTLY SCOPE FOR IT**: CoRL in 20 days is not feasible for a contribution requiring SONIC+IK integration, grammar design, generation pipeline, AND downstream evaluation. Commit to Humanoids 2026 (51 days) with full scope, and only mention CoRL if you can demonstrate the pipeline works in the first week. The user's requirement targets CoRL, but an honest 'minimal-viable CoRL submission is high-risk; Humanoids 2026 is the reliable path' is better than pretending 20 days suffices.

4. **ADD STRIDE/FORGE TO LANDSCAPE AND DIFFERENTIATE**: These papers automate reward design via LLMs—the same bottleneck you claim to address. Your differentiation should be: STRIDE generates single-task rewards iteratively; CompLocoGen generates compositionally coupled multi-stage tasks where the grammar ensures inter-primitive physical consistency that per-task reward generation cannot guarantee.

5. **SUBSTANTIATE YIELD RATE**: Either cite empirical data from related work (GenManip/HumanoidGen success rates) or commit to reporting this as an experimental metric rather than a prior estimate.

### Round 4 review
Verdict: revise
Issues: ["MISSING COMPETING WORK: Eurekaverse (CoRL 2024, NVIDIA Research) establishes LLM-driven environment curriculum generation with agent-environment co-evolution for RL training. While it targets quadrupedal parkour (not humanoid loco-manipulation), the paradigm—LLM generates diverse training environments, train policies, evaluate, feed back to LLM for next iteration—is essentially identical to CompLocoGen's pipeline. This must be cited and explicitly differentiated: Eurekaverse generates environment variations for single-skill training; CompLocoGen generates compositionally coupled multi-stage task configurations with inter-primitive dynamics constraints.", "MISSING BASELINE: DemoHLM (arXiv:2510.11258) generates diverse humanoid loco-manipulation trajectories from a single teleoperated demonstration by converting to object-centric representations and replaying under varied initial conditions. It uses a 3-stage pipeline (locomotion → pre-manipulation → manipulation) with a hierarchical controller on Unitree G1. While DemoHLM generates spatial variations of one task template rather than compositionally novel tasks, it should be added as a data-generation baseline to demonstrate that grammar-based composition produces qualitatively different (not just more) training data than demo-augmentation approaches.", "VENUE MISMATCH: The user explicitly targets CoRL 2026 (paper deadline May 29, 19 days away). The proposal honestly pivots to Humanoids 2026 (July 24, 75 days) as primary target. While this honesty is appreciated, the proposal must either: (a) commit to a minimal CoRL submission (2-3 task compositions, pre-trained everything, single downstream eval, no ablation depth) with Humanoids as the full version, or (b) clearly justify why CoRL is infeasible and Humanoids is the right venue. Currently the proposal lists Humanoids as primary but doesn't address how to satisfy the user's CoRL requirement.", "LIMITED COMPOSITIONAL SPACE: The grammar defines only 4 primitives (walk, pick, place, carry). The number of meaningfully distinct task compositions from 4 primitives is inherently limited. With structural and dynamic feasibility filtering, the effective compositional space may be quite small. The proposal should either (a) expand primitives (push, pull, open_door, climb_stairs, squat) to demonstrate the grammar's extensibility, or (b) provide analysis of how many compositionally distinct and dynamically feasible tasks the 4-primitive grammar can produce.", "NOVELTY DEPTH FOR CoRL: The technical contribution reduces to (1) a context-free grammar over 4 primitives with typed parameters and analytical physics predicates, (2) LLM-guided constrained generation with Qwen 3.6, (3) compilation to Isaac Lab @configclass, (4) rejection sampling with online predicate calibration. Each component individually uses standard techniques. The combination is novel for loco-manipulation, but CoRL reviewers may expect deeper algorithmic contribution—e.g., learning the dynamics predicates from data rather than hand-coding ZMP/centroidal analysis, or providing formal guarantees about compositional coverage/completeness. For Humanoids 2026, this systems contribution would be appropriately valued.", "GENIE SIM 3.0 (arXiv:2601.02078, AgiBot, Jan 2026) is a comprehensive simulation platform with LLM-powered scene generation that generates thousands of diverse environments for humanoid robots across 200+ tasks. While it focuses on scene construction rather than compositional task specification with physics constraints, it represents a relevant large-scale automated generation approach and should be briefly acknowledged in the landscape."]
Feedback: The proposal has improved substantially across rounds 1-3 (compute budget fixed, AGILE configclass corrected, STRIDE/FORGE differentiated, yield rate as experimental metric). The core idea—dynamics-aware compositional grammar for humanoid loco-manipulation task generation—is genuinely valuable and addresses a real bottleneck. Three targeted changes would bring this to pass quality:

1. **ADD EUREKAVERSE AND DemoHLM**: Eurekaverse (CoRL 2024) is the most important missing citation—it pioneered LLM-driven environment curriculum generation. Your differentiation is clear (single-skill environment variation vs. compositional multi-stage task generation with inter-primitive dynamics constraints) but must be explicitly stated. DemoHLM should be added as a data-generation baseline to show that compositional generation produces qualitatively different training data than demo augmentation.

2. **RESOLVE VENUE STRATEGY**: Either (a) commit to a minimal CoRL abstract (May 26, 16 days): 4 primitives, 3-5 task compositions using pre-trained SONIC+IK, single downstream eval, no ablations—essentially a proof-of-concept showing the grammar works—with full paper at Humanoids 2026; OR (b) drop CoRL and commit fully to Humanoids 2026 with full scope. A split strategy (CoRL abstract as teaser, Humanoids as full paper) is viable if the pipeline can produce initial results in ~14 days.

3. **EXPAND GRAMMAR OR JUSTIFY SCOPE**: Either add 2-3 more primitives (push, open_door, squat) to demonstrate extensibility, or provide explicit analysis of compositional diversity: how many unique task programs does the 4-primitive grammar produce? What fraction survive structural filtering? Dynamic filtering? This strengthens the contribution by quantifying the grammar's generative power.

Minor: Add Genie Sim 3.0 to landscape (LLM-driven scene generation, different scope but related). Consider whether learning dynamics predicates (small MLP trained on simulation rollouts) rather than purely analytical models could provide an additional novelty dimension for CoRL framing.


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
  "promptId": "9b9ebae5-ea89-443c-82ad-9f786b68d79f",
  "type": "user",
  "uuid": "6b7d4a54-7d69-485b-930d-7df0805efa4e",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c9f1e88d-7547-445a-bdb2-8a60925de079",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-10T19:20:26.671Z_

```json
{
  "parentUuid": "6b7d4a54-7d69-485b-930d-7df0805efa4e",
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
  "uuid": "812daa07-1b51-424e-8f54-762fdeb144cc",
  "timestamp": "2026-05-10T19:20:26.671Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c9f1e88d-7547-445a-bdb2-8a60925de079",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-10T19:20:26.671Z_

```json
{
  "parentUuid": "812daa07-1b51-424e-8f54-762fdeb144cc",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "5bd1d396-f976-4872-b5de-c8483c8875cf",
  "timestamp": "2026-05-10T19:20:26.671Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c9f1e88d-7547-445a-bdb2-8a60925de079",
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
  "leafUuid": "5bd1d396-f976-4872-b5de-c8483c8875cf",
  "sessionId": "c9f1e88d-7547-445a-bdb2-8a60925de079"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Verify CompLocoGen novelty and feasibility for humanoid loco-manipulation task generation",
  "sessionId": "c9f1e88d-7547-445a-bdb2-8a60925de079"
}
```

---

### Assistant

_source line 8 · 2026-05-10T19:20:48.363Z_

<details><summary>Logged reasoning block</summary>

```text
This is round 5 of 10 for reviewing a research idea called "CompLocoGen." Let me carefully analyze this proposal and conduct independent verification via web searches. The idea proposes a grammar-structured system with a learned Transition Feasibility Network (TFN) for compositional humanoid loco-manipulation task generation.

Let me first understand what has changed since previous rounds:
1. Round 1: Issues with GR00T-Gen omission, SkillBlender/Isaac Lab incompatibility, missing EgoHumanoid, timeline concerns → revise
2. Round 2: Compute budget violation (300-400h vs 200h limit), timeline mismatch, missing works → revise


3. Round 3: STRIDE/FORGE missing, AGILE YAML mischaracterization, novelty concerns, yield rate unsubstantiated → revise
4. Round 4: Missing Eurekaverse and DemoHLM, venue mismatch, limited compositional space, novelty depth → revise

Now in round 5, the proposal has been revised to address many of these issues: Eurekaverse, DemoHLM, Genie Sim 3.0, STRIDE, and FORGE have been added to the related work section, the primitive action set has expanded to seven skills including walk, pick, place, carry, push, open_door, and squat, and there are additional improvements being made.

The Transition Feasibility Network is now positioned as the core algorithmic contribution, which should meaningfully strengthen the novelty argument. The compute budget has been pinned to approximately 180-200 H100-hours, the primary submission target shifted to Humanoids 2026 with a June 30 deadline, AGILE is now correctly integrated as the build substrate with proper configuration class generation, and multiple baselines and ablations have been incorporated.

Now I need to validate several critical aspects: whether the TFN represents genuine novelty or overlaps with existing work, confirm the venue deadlines are accurate, verify that the cited baselines and references actually exist, assess whether the compute budget is feasible, identify any remaining gaps in the competitive landscape, and determine whether this work aligns better with CoRL or Humanoids standards.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5bd1d396-f976-4872-b5de-c8483c8875cf",
  "isSidechain": false,
  "requestId": "req_011CauRtmB1nCUoHUNHPgxCr",
  "type": "assistant",
  "uuid": "eaef3342-4287-405e-8ee0-5e941f6a2cb3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c9f1e88d-7547-445a-bdb2-8a60925de079",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XehoEcXkM3NoXuhyPtw5rD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 21226,
      "cache_read_input_tokens": 11664,
      "output_tokens": 1589,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21226,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1589,
          "cache_read_input_tokens": 11664,
          "cache_creation_input_tokens": 21226,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21226
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

_source line 9 · 2026-05-10T19:20:48.365Z_

I'll conduct independent verification of this revised proposal's claims, focusing on the new TFN contribution, competing work, and feasibility. Let me search across multiple dimensions.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eaef3342-4287-405e-8ee0-5e941f6a2cb3",
  "isSidechain": false,
  "requestId": "req_011CauRtmB1nCUoHUNHPgxCr",
  "type": "assistant",
  "uuid": "aec7e3b1-e1ee-4a86-915b-c005cad41890",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c9f1e88d-7547-445a-bdb2-8a60925de079",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XehoEcXkM3NoXuhyPtw5rD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 21226,
      "cache_read_input_tokens": 11664,
      "output_tokens": 1589,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21226,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1589,
          "cache_read_input_tokens": 11664,
          "cache_creation_input_tokens": 21226,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21226
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

_source line 10 · 2026-05-10T19:20:53.527Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01AVidU5ibbGxyrr9qsHhBEe`</summary>

```json
{
  "subagent_type": "Explore",
  "description": "Search Eurekaverse and TFN",
  "prompt": "I'm reviewing a research proposal about compositional humanoid loco-manipulation task generation. I need to verify several claims via web search. Please search for:\n\n1. \"Eurekaverse\" CoRL 2024 - verify this paper exists and what it does (LLM-driven environment curriculum generation)\n2. \"transition feasibility\" OR \"transition feasibility network\" robot skill composition - check if anyone has already proposed learning transition feasibility for skill chaining\n3. \"SCaR\" NeurIPS 2024 skill chaining - verify this paper and what it does with learned success predictors\n4. \"Generative Skill Chaining\" CoRL 2024 diffusion - verify this paper\n\nUse WebSearch for each query. Report what you find, especially whether anyone has already proposed a GNN-based transition feasibility predictor for robot skill composition."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aec7e3b1-e1ee-4a86-915b-c005cad41890",
  "isSidechain": false,
  "requestId": "req_011CauRtmB1nCUoHUNHPgxCr",
  "type": "assistant",
  "uuid": "fe4769df-962a-4361-86f6-710f1a5c604e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c9f1e88d-7547-445a-bdb2-8a60925de079",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XehoEcXkM3NoXuhyPtw5rD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 21226,
      "cache_read_input_tokens": 11664,
      "output_tokens": 1589,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21226,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1589,
          "cache_read_input_tokens": 11664,
          "cache_creation_input_tokens": 21226,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21226
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

_source line 11 · 2026-05-10T19:20:58.384Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01ACKhoisqpFtLk2sVgFvAd5`</summary>

```json
{
  "subagent_type": "Explore",
  "description": "Search AGILE and Humanoids 2026",
  "prompt": "I need to verify several claims for a research proposal review. Please use WebSearch to find:\n\n1. \"AGILE\" NVIDIA humanoid loco-manipulation Isaac Lab 2026 - verify this paper/framework exists (arXiv:2603.20147)\n2. \"Humanoids 2026\" conference deadline - verify the paper deadline (claimed June 30, 2026)\n3. \"CoRL 2026\" Austin deadline - verify abstract deadline May 26 and paper deadline May 29, 2026\n4. \"GR00T-WBC\" OR \"SONIC\" NVIDIA humanoid locomotion checkpoint - verify pre-trained locomotion checkpoints exist\n5. \"LHM-Humanoid\" arXiv:2508.16943 - verify this paper exists\n\nReport what you find for each query."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fe4769df-962a-4361-86f6-710f1a5c604e",
  "isSidechain": false,
  "requestId": "req_011CauRtmB1nCUoHUNHPgxCr",
  "type": "assistant",
  "uuid": "2f152227-9641-4fcf-aef8-90b4e2d7da02",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c9f1e88d-7547-445a-bdb2-8a60925de079",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XehoEcXkM3NoXuhyPtw5rD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 21226,
      "cache_read_input_tokens": 11664,
      "output_tokens": 1589,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21226,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1589,
          "cache_read_input_tokens": 11664,
          "cache_creation_input_tokens": 21226,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21226
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

_source line 12 · 2026-05-10T19:21:03.158Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01FfQLV1D7N6M1f8uvNiDcmi`</summary>

```json
{
  "subagent_type": "Explore",
  "description": "Search competing TFN works",
  "prompt": "I'm reviewing a paper proposing a \"Transition Feasibility Network\" (GNN-based) that learns to predict whether transitions between robot skill primitives will succeed in humanoid loco-manipulation. I need to find competing/similar work. Please use WebSearch for:\n\n1. \"learned feasibility\" OR \"feasibility prediction\" robot skill composition 2024 2025 2026\n2. \"graph neural network\" skill chaining robot manipulation\n3. \"compositional task generation\" humanoid robot 2025 2026\n4. \"active learning\" robot task generation feasibility\n5. site:arxiv.org \"humanoid loco-manipulation\" data generation 2026\n\nReport any papers that propose learning transition feasibility or skill composition feasibility, especially using GNNs or similar architectures."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2f152227-9641-4fcf-aef8-90b4e2d7da02",
  "isSidechain": false,
  "requestId": "req_011CauRtmB1nCUoHUNHPgxCr",
  "type": "assistant",
  "uuid": "d7d8182d-41eb-47a3-8e2f-c838f301eef2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c9f1e88d-7547-445a-bdb2-8a60925de079",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XehoEcXkM3NoXuhyPtw5rD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 21226,
      "cache_read_input_tokens": 11664,
      "output_tokens": 1589,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21226,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1589,
          "cache_read_input_tokens": 11664,
          "cache_creation_input_tokens": 21226,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21226
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

_source line 13 · 2026-05-10T19:21:06.817Z_

<details open><summary>🔧 Tool call — Agent · `toolu_011WkErdb77uYpp31p6uVLpZ`</summary>

```json
{
  "subagent_type": "Explore",
  "description": "Search recent humanoid works 2026",
  "prompt": "I need to find the latest competing work in humanoid robot data generation and task composition from 2026. Please use WebSearch for:\n\n1. \"humanoid\" \"task generation\" OR \"environment generation\" simulation 2026\n2. site:arxiv.org humanoid whole-body loco-manipulation 2026\n3. \"GR00T-Dreams\" NVIDIA humanoid synthetic data 2026\n4. \"DexMimicGen\" humanoid 2026\n5. \"Cosmos\" humanoid video generation training data 2026\n6. \"procedural generation\" humanoid robot tasks 2026\n\nReport all relevant papers you find, especially anything that generates diverse humanoid training tasks or environments automatically."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d7d8182d-41eb-47a3-8e2f-c838f301eef2",
  "isSidechain": false,
  "requestId": "req_011CauRtmB1nCUoHUNHPgxCr",
  "type": "assistant",
  "uuid": "3e0e7c8e-0a8b-4846-9ee8-146ccf6aa28f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c9f1e88d-7547-445a-bdb2-8a60925de079",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XehoEcXkM3NoXuhyPtw5rD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 21226,
      "cache_read_input_tokens": 11664,
      "output_tokens": 1589,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21226,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1589,
          "cache_read_input_tokens": 11664,
          "cache_creation_input_tokens": 21226,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21226
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

_source line 14 · 2026-05-10T19:21:13.259Z_

<details><summary>↩ Tool result · `toolu_01AVidU5ibbGxyrr9qsHhBEe`</summary>

```text
## Summary of Findings

I've verified the claims from your research proposal. Here's what I found:

### 1. **Eurekaverse (CoRL 2024)** - VERIFIED
The paper exists and is correctly described. Eurekaverse uses LLMs to generate environment curricula by instructing an LLM to iteratively sample progressively more challenging environments. It was successfully applied to quadrupedal parkour learning with real-world transfer.

**Authors:** William Liang, Sam Wang, Hungju Wang, Osbert Bastani, Dinesh Jayaraman, Jason Ma

### 2. **Transition Feasibility Networks for Skill Composition** - PARTIALLY FOUND
Multiple papers address transition feasibility between skills, but the framing varies:
- **Generative Skill Chaining (GSC)** implicitly considers "transition feasibility" and subsequent skill affordability
- **SCaR (NeurIPS 2024)** uses bi-directional regularization to align terminal/initial states between consecutive skills
- **Graph-Based Skill Composition (GSC)** creates skill graphs with transformer-style graph architectures for skill representation

However, I did not find evidence of a specific **GNN-based transition feasibility predictor** paper. The closest work is the graph-based approaches mentioned above, but these appear to be for skill graph representation rather than learning transition feasibility as a separate learned module.

### 3. **SCaR (NeurIPS 2024)** - VERIFIED
SCaR applies dual regularization to skill chaining, with bi-directional alignment between consecutive skills. **Important note:** It focuses on regularization and alignment rather than learning explicit success predictors. The framework was evaluated on furniture assembly, kitchen organization, and real-world pick-and-place tasks.

### 4. **Generative Skill Chaining with Diffusion** - PARTIALLY VERIFIED
The paper exists but was published at **CoRL 2023, not CoRL 2024**. It uses skill-centric diffusion models and composes their distributions for long-horizon planning. A related work called **Generative Factor Chaining** extended this to CoRL 2024 for multi-manipulator coordination.

## Key Finding on GNN-based Transition Feasibility

Your proposal may be novel on this front: I found no evidence of a published paper proposing a **GNN-based transition feasibility predictor specifically for robot skill composition**. The existing literature addresses transition feasibility through regularization (SCaR), implicit consideration in diffusion models (GSC), or graph representations (GSC graph-based), but not through explicit learned transition feasibility networks using GNNs.

---

Sources:
- [Eurekaverse GitHub](https://github.com/eureka-research/eurekaverse)
- [Eurekaverse ArXiv](https://arxiv.org/abs/2411.01775)
- [Eurekaverse OpenReview](https://openreview.net/forum?id=F0rWEID2gb)
- [Generative Skill Chaining](https://generative-skill-chaining.github.io/)
- [Generative Skill Chaining Paper](https://generative-skill-chaining.github.io/assets/2023_Generative_Skill_Chaining.pdf)
- [SCaR NeurIPS 2024 Proceedings](https://proceedings.neurips.cc/paper_files/paper/2024/file/ca92ff06d973ece92cecc561757d500e-Paper-Conference.pdf)
- [SCaR OpenReview](https://openreview.net/forum?id=RnxJc4vTVi)
- [Graph-Based Skill Composition](https://www.sciencedirect.com/science/article/abs/pii/S0921889024001714)
- [Generative Factor Chaining](https://generative-fc.github.io/)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fe4769df-962a-4361-86f6-710f1a5c604e",
  "isSidechain": false,
  "promptId": "9b9ebae5-ea89-443c-82ad-9f786b68d79f",
  "type": "user",
  "uuid": "cbb27337-2f38-4e6f-82eb-19b8825cf135",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I'm reviewing a research proposal about compositional humanoid loco-manipulation task generation. I need to verify several claims via web search. Please search for:\n\n1. \"Eurekaverse\" CoRL 2024 - verify this paper exists and what it does (LLM-driven environment curriculum generation)\n2. \"transition feasibility\" OR \"transition feasibility network\" robot skill composition - check if anyone has already proposed learning transition feasibility for skill chaining\n3. \"SCaR\" NeurIPS 2024 skill chaining - verify this paper and what it does with learned success predictors\n4. \"Generative Skill Chaining\" CoRL 2024 diffusion - verify this paper\n\nUse WebSearch for each query. Report what you find, especially whether anyone has already proposed a GNN-based transition feasibility predictor for robot skill composition.",
    "agentId": "a0d34475159340417",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "## Summary of Findings\n\nI've verified the claims from your research proposal. Here's what I found:\n\n### 1. **Eurekaverse (CoRL 2024)** - VERIFIED\nThe paper exists and is correctly described. Eurekaverse uses LLMs to generate environment curricula by instructing an LLM to iteratively sample progressively more challenging environments. It was successfully applied to quadrupedal parkour learning with real-world transfer.\n\n**Authors:** William Liang, Sam Wang, Hungju Wang, Osbert Bastani, Dinesh Jayaraman, Jason Ma\n\n### 2. **Transition Feasibility Networks for Skill Composition** - PARTIALLY FOUND\nMultiple papers address transition feasibility between skills, but the framing varies:\n- **Generative Skill Chaining (GSC)** implicitly considers \"transition feasibility\" and subsequent skill affordability\n- **SCaR (NeurIPS 2024)** uses bi-directional regularization to align terminal/initial states between consecutive skills\n- **Graph-Based Skill Composition (GSC)** creates skill graphs with transformer-style graph architectures for skill representation\n\nHowever, I did not find evidence of a specific **GNN-based transition feasibility predictor** paper. The closest work is the graph-based approaches mentioned above, but these appear to be for skill graph representation rather than learning transition feasibility as a separate learned module.\n\n### 3. **SCaR (NeurIPS 2024)** - VERIFIED\nSCaR applies dual regularization to skill chaining, with bi-directional alignment between consecutive skills. **Important note:** It focuses on regularization and alignment rather than learning explicit success predictors. The framework was evaluated on furniture assembly, kitchen organization, and real-world pick-and-place tasks.\n\n### 4. **Generative Skill Chaining with Diffusion** - PARTIALLY VERIFIED\nThe paper exists but was published at **CoRL 2023, not CoRL 2024**. It uses skill-centric diffusion models and composes their distributions for long-horizon planning. A related work called **Generative Factor Chaining** extended this to CoRL 2024 for multi-manipulator coordination.\n\n## Key Finding on GNN-based Transition Feasibility\n\nYour proposal may be novel on this front: I found no evidence of a published paper proposing a **GNN-based transition feasibility predictor specifically for robot skill composition**. The existing literature addresses transition feasibility through regularization (SCaR), implicit consideration in diffusion models (GSC), or graph representations (GSC graph-based), but not through explicit learned transition feasibility networks using GNNs.\n\n---\n\nSources:\n- [Eurekaverse GitHub](https://github.com/eureka-research/eurekaverse)\n- [Eurekaverse ArXiv](https://arxiv.org/abs/2411.01775)\n- [Eurekaverse OpenReview](https://openreview.net/forum?id=F0rWEID2gb)\n- [Generative Skill Chaining](https://generative-skill-chaining.github.io/)\n- [Generative Skill Chaining Paper](https://generative-skill-chaining.github.io/assets/2023_Generative_Skill_Chaining.pdf)\n- [SCaR NeurIPS 2024 Proceedings](https://proceedings.neurips.cc/paper_files/paper/2024/file/ca92ff06d973ece92cecc561757d500e-Paper-Conference.pdf)\n- [SCaR OpenReview](https://openreview.net/forum?id=RnxJc4vTVi)\n- [Graph-Based Skill Composition](https://www.sciencedirect.com/science/article/abs/pii/S0921889024001714)\n- [Generative Factor Chaining](https://generative-fc.github.io/)"
      }
    ],
    "totalDurationMs": 19726,
    "totalTokens": 19971,
    "totalToolUseCount": 4,
    "usage": {
      "input_tokens": 1962,
      "cache_creation_input_tokens": 2823,
      "cache_read_input_tokens": 14262,
      "output_tokens": 924,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2823
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1962,
          "output_tokens": 924,
          "cache_read_input_tokens": 14262,
          "cache_creation_input_tokens": 2823,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2823,
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
  "sourceToolAssistantUUID": "fe4769df-962a-4361-86f6-710f1a5c604e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c9f1e88d-7547-445a-bdb2-8a60925de079",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-10T19:21:16.882Z_

<details><summary>↩ Tool result · `toolu_01ACKhoisqpFtLk2sVgFvAd5`</summary>

```text
## Research Proposal Verification Report

Here's what I found for each of your claims:

### 1. AGILE NVIDIA Humanoid Loco-Manipulation (arXiv:2603.20147)
**VERIFIED** - The paper exists and is confirmed. "AGILE: A Comprehensive Workflow for Humanoid Loco-Manipulation Learning" is a real paper published March 20, 2026. It's an open-source workflow built on Isaac Lab and RSL-RL that provides a four-stage pipeline for humanoid learning: interactive environment verification, reproducible training, unified evaluation, and descriptor-driven deployment.

### 2. Humanoids 2026 Conference Deadline (June 30, 2026)
**PARTIALLY VERIFIED** - The conference exists (IEEE-RAS 25th International Conference on Humanoid Robots, December 6-9, 2026 in Santa Clara, CA). However, the search results do not explicitly confirm the June 30, 2026 paper deadline. The official conference website at https://2026.ieee-humanoids.org/ should have the exact deadline, but it wasn't displayed in the search results.

### 3. CoRL 2026 Austin Deadlines
**VERIFIED** - The deadlines are confirmed as accurate:
- Abstract submission deadline: May 26, 2026 11:59 UTC
- Paper submission deadline: May 29, 2026 11:59 UTC
- Conference location: JW Marriott Austin, November 9-12, 2026
- Papers submitted via OpenReview

### 4. GR00T-WBC and SONIC Pre-trained Locomotion Checkpoints
**VERIFIED** - Both systems exist with pre-trained checkpoints:
- **GR00T Whole-Body Control (WBC)** is a unified platform for humanoid controllers hosted on GitHub (NVlabs/GR00T-WholeBodyControl)
- **SONIC** is a humanoid behavior foundation model trained on the Bones-SEED motion capture dataset (142K+ motions, 288+ hours)
- **GEAR-SONIC** with pre-trained checkpoints was released February 19, 2026 and is available on Hugging Face
- Both support locomotion, whole-body control, and real-time deployment

### 5. LHM-Humanoid (arXiv:2508.16943)
**VERIFIED** - The paper exists. "LHM-Humanoid: Learning a Unified Policy for Long-Horizon Humanoid Whole-Body Loco-Manipulation in Diverse Messy Environments" is a real paper last revised March 5, 2026. It presents a framework for learning unified policies for humanoid loco-manipulation across diverse cluttered scenes using RL teacher policies, DAgger distillation, and vision-language-action models.

---

**Summary**: 4 of 5 claims fully verified, and 1 partially verified (Humanoids 2026 deadline exists but specific June 30 date not confirmed in search results).

Sources:
- [AGILE: A Comprehensive Workflow for Humanoid Loco-Manipulation Learning](https://arxiv.org/html/2603.20147v1)
- [Humanoids 2026 Conference](https://2026.ieee-humanoids.org/)
- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)
- [GR00T-WholeBodyControl GitHub](https://github.com/NVlabs/GR00T-WholeBodyControl)
- [GEAR-SONIC on Hugging Face](https://huggingface.co/nvidia/GEAR-SONIC)
- [LHM-Humanoid arXiv:2508.16943](https://arxiv.org/abs/2508.16943)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2f152227-9641-4fcf-aef8-90b4e2d7da02",
  "isSidechain": false,
  "promptId": "9b9ebae5-ea89-443c-82ad-9f786b68d79f",
  "type": "user",
  "uuid": "c391767d-7019-44c5-9ea3-a8cce95576f6",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to verify several claims for a research proposal review. Please use WebSearch to find:\n\n1. \"AGILE\" NVIDIA humanoid loco-manipulation Isaac Lab 2026 - verify this paper/framework exists (arXiv:2603.20147)\n2. \"Humanoids 2026\" conference deadline - verify the paper deadline (claimed June 30, 2026)\n3. \"CoRL 2026\" Austin deadline - verify abstract deadline May 26 and paper deadline May 29, 2026\n4. \"GR00T-WBC\" OR \"SONIC\" NVIDIA humanoid locomotion checkpoint - verify pre-trained locomotion checkpoints exist\n5. \"LHM-Humanoid\" arXiv:2508.16943 - verify this paper exists\n\nReport what you find for each query.",
    "agentId": "af1d5343193f8d545",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "## Research Proposal Verification Report\n\nHere's what I found for each of your claims:\n\n### 1. AGILE NVIDIA Humanoid Loco-Manipulation (arXiv:2603.20147)\n**VERIFIED** - The paper exists and is confirmed. \"AGILE: A Comprehensive Workflow for Humanoid Loco-Manipulation Learning\" is a real paper published March 20, 2026. It's an open-source workflow built on Isaac Lab and RSL-RL that provides a four-stage pipeline for humanoid learning: interactive environment verification, reproducible training, unified evaluation, and descriptor-driven deployment.\n\n### 2. Humanoids 2026 Conference Deadline (June 30, 2026)\n**PARTIALLY VERIFIED** - The conference exists (IEEE-RAS 25th International Conference on Humanoid Robots, December 6-9, 2026 in Santa Clara, CA). However, the search results do not explicitly confirm the June 30, 2026 paper deadline. The official conference website at https://2026.ieee-humanoids.org/ should have the exact deadline, but it wasn't displayed in the search results.\n\n### 3. CoRL 2026 Austin Deadlines\n**VERIFIED** - The deadlines are confirmed as accurate:\n- Abstract submission deadline: May 26, 2026 11:59 UTC\n- Paper submission deadline: May 29, 2026 11:59 UTC\n- Conference location: JW Marriott Austin, November 9-12, 2026\n- Papers submitted via OpenReview\n\n### 4. GR00T-WBC and SONIC Pre-trained Locomotion Checkpoints\n**VERIFIED** - Both systems exist with pre-trained checkpoints:\n- **GR00T Whole-Body Control (WBC)** is a unified platform for humanoid controllers hosted on GitHub (NVlabs/GR00T-WholeBodyControl)\n- **SONIC** is a humanoid behavior foundation model trained on the Bones-SEED motion capture dataset (142K+ motions, 288+ hours)\n- **GEAR-SONIC** with pre-trained checkpoints was released February 19, 2026 and is available on Hugging Face\n- Both support locomotion, whole-body control, and real-time deployment\n\n### 5. LHM-Humanoid (arXiv:2508.16943)\n**VERIFIED** - The paper exists. \"LHM-Humanoid: Learning a Unified Policy for Long-Horizon Humanoid Whole-Body Loco-Manipulation in Diverse Messy Environments\" is a real paper last revised March 5, 2026. It presents a framework for learning unified policies for humanoid loco-manipulation across diverse cluttered scenes using RL teacher policies, DAgger distillation, and vision-language-action models.\n\n---\n\n**Summary**: 4 of 5 claims fully verified, and 1 partially verified (Humanoids 2026 deadline exists but specific June 30 date not confirmed in search results).\n\nSources:\n- [AGILE: A Comprehensive Workflow for Humanoid Loco-Manipulation Learning](https://arxiv.org/html/2603.20147v1)\n- [Humanoids 2026 Conference](https://2026.ieee-humanoids.org/)\n- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)\n- [GR00T-WholeBodyControl GitHub](https://github.com/NVlabs/GR00T-WholeBodyControl)\n- [GEAR-SONIC on Hugging Face](https://huggingface.co/nvidia/GEAR-SONIC)\n- [LHM-Humanoid arXiv:2508.16943](https://arxiv.org/abs/2508.16943)"
      }
    ],
    "totalDurationMs": 18494,
    "totalTokens": 20681,
    "totalToolUseCount": 5,
    "usage": {
      "input_tokens": 908,
      "cache_creation_input_tokens": 4607,
      "cache_read_input_tokens": 14258,
      "output_tokens": 908,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4607
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 908,
          "output_tokens": 908,
          "cache_read_input_tokens": 14258,
          "cache_creation_input_tokens": 4607,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4607,
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
  "sourceToolAssistantUUID": "2f152227-9641-4fcf-aef8-90b4e2d7da02",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c9f1e88d-7547-445a-bdb2-8a60925de079",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-10T19:21:24.843Z_

<details><summary>↩ Tool result · `toolu_01FfQLV1D7N6M1f8uvNiDcmi`</summary>

```text
## Summary of Competing and Related Work

I found several highly relevant papers and research directions that relate to your Transition Feasibility Network proposal. Here are the key findings organized by theme:

### Direct Relevance: Feasibility Prediction and Active Learning

**FATE: Closed-Loop Feasibility-Aware Task Generation with Active Repair for Physically Grounded Robotic Curricula**
- Directly addresses feasibility-aware task generation
- Closes the loop between language-driven task proposal and embodied feasibility verification
- Uses active learning to refine curricula

**Active Learning of Abstract Plan Feasibility**
- Learns models of whether plans will succeed when executed
- Integrates feasibility learning into active learning loops for data efficiency
- Directly comparable to your transition feasibility approach

**RoboGene: Boosting VLA Pre-training via Diversity-Driven Agentic Framework for Real-World Task Generation**
- Automates generation of diverse, physically plausible manipulation tasks
- Integrates self-reflection mechanisms to enforce physical constraints
- Addresses task hallucination problems in foundation models

### Graph Neural Networks for Skill Learning and Manipulation

**Efficient and Interpretable Robot Manipulation with Graph Neural Networks**
- Uses GNNs to solve robot manipulation by representing task-relevant entities as graph nodes
- Learns policies over graph representations using imitation learning
- Generalizes to new object configurations (highly relevant architecture choice)

**Generative Factor Chaining (GFC)**
- Learning-to-plan method for complex coordinated manipulation
- Uses factor graphs with diffusion models for multi-arm coordination
- Demonstrates compositional approaches to skill sequencing

**WAGNN: A Weighted Aggregation Graph Neural Network for robot skill learning**
- Learns structured policies through graph aggregation
- Incorporates robot structure priors similar to what your GNN approach likely does

**SCaR: Refining Skill Chaining for Long-Horizon Robotic Manipulation via Dual Regularization**
- Recent work on skill chaining with regularization techniques
- Addresses the skill composition problem you're tackling

### Humanoid Loco-Manipulation (2025-2026)

**Ψ₀: An Open Foundation Model Towards Universal Humanoid Loco-Manipulation** (March 2026)
- Latest foundation model for humanoid loco-manipulation
- Pre-trains on human demonstration data then fine-tunes on robot data
- Most recent comparable work in the exact domain

**OmniRetarget: Interaction-Preserving Data Generation for Humanoid Whole-Body Loco-Manipulation and Scene Interaction** (October 2025)
- Addresses data generation for complex loco-manipulation
- Preserves spatial and contact relationships between agent, terrain, and objects
- Tackles similar data generation challenges

**EgoHumanoid: Unlocking In-the-Wild Loco-Manipulation with Robot-Free Egocentric Demonstration** (February 2026)
- Co-trains vision-language-action policies using human and robot data
- Achieves 51% improvement over robot-only baselines
- Demonstrates efficacy of human demonstration data for robot learning

**AGILE: A Comprehensive Workflow for Humanoid Loco-Manipulation Learning** (March 2026)
- End-to-end workflow for humanoid learning including synthetic data generation
- Covers evaluation using motion metrics and VLA training

### Sources:

- [FATE: Closed-Loop Feasibility-Aware Task Generation](https://arxiv.org/html/2603.01505)
- [Active Learning of Abstract Plan Feasibility](https://deepai.org/publication/active-learning-of-abstract-plan-feasibility)
- [RoboGene: Diversity-Driven Agentic Framework](https://arxiv.org/html/2602.16444)
- [Efficient and Interpretable Robot Manipulation with GNNs](https://arxiv.org/abs/2102.13177)
- [Generative Factor Chaining](https://arxiv.org/html/2409.16275)
- [Ψ₀: Universal Humanoid Loco-Manipulation](https://arxiv.org/abs/2603.12263)
- [OmniRetarget: Interaction-Preserving Data Generation](https://arxiv.org/abs/2509.26633)
- [EgoHumanoid: In-the-Wild Loco-Manipulation](https://arxiv.org/abs/2602.10106)
- [AGILE: Comprehensive Workflow for Humanoid Learning](https://arxiv.org/html/2603.20147v1)
- [ULC: Unified Fine-Grained Controller for Loco-Manipulation](https://arxiv.org/pdf/2507.06905)
- [Physically Consistent Loco-Manipulation using Latent Diffusion](https://arxiv.org/html/2504.16843v1)

Your Transition Feasibility Network using GNNs appears to fill a specific gap in learning transition compatibility between primitives for humanoid loco-manipulation, with most recent work (2025-2026) focusing on data generation, foundation models, and end-to-end learning rather than explicitly modeling feasibility of primitive transitions.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d7d8182d-41eb-47a3-8e2f-c838f301eef2",
  "isSidechain": false,
  "promptId": "9b9ebae5-ea89-443c-82ad-9f786b68d79f",
  "type": "user",
  "uuid": "780f53ac-35fd-4fa3-a216-99c9a4c8394c",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I'm reviewing a paper proposing a \"Transition Feasibility Network\" (GNN-based) that learns to predict whether transitions between robot skill primitives will succeed in humanoid loco-manipulation. I need to find competing/similar work. Please use WebSearch for:\n\n1. \"learned feasibility\" OR \"feasibility prediction\" robot skill composition 2024 2025 2026\n2. \"graph neural network\" skill chaining robot manipulation\n3. \"compositional task generation\" humanoid robot 2025 2026\n4. \"active learning\" robot task generation feasibility\n5. site:arxiv.org \"humanoid loco-manipulation\" data generation 2026\n\nReport any papers that propose learning transition feasibility or skill composition feasibility, especially using GNNs or similar architectures.",
    "agentId": "a1ce7b1fd4b81beb9",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "## Summary of Competing and Related Work\n\nI found several highly relevant papers and research directions that relate to your Transition Feasibility Network proposal. Here are the key findings organized by theme:\n\n### Direct Relevance: Feasibility Prediction and Active Learning\n\n**FATE: Closed-Loop Feasibility-Aware Task Generation with Active Repair for Physically Grounded Robotic Curricula**\n- Directly addresses feasibility-aware task generation\n- Closes the loop between language-driven task proposal and embodied feasibility verification\n- Uses active learning to refine curricula\n\n**Active Learning of Abstract Plan Feasibility**\n- Learns models of whether plans will succeed when executed\n- Integrates feasibility learning into active learning loops for data efficiency\n- Directly comparable to your transition feasibility approach\n\n**RoboGene: Boosting VLA Pre-training via Diversity-Driven Agentic Framework for Real-World Task Generation**\n- Automates generation of diverse, physically plausible manipulation tasks\n- Integrates self-reflection mechanisms to enforce physical constraints\n- Addresses task hallucination problems in foundation models\n\n### Graph Neural Networks for Skill Learning and Manipulation\n\n**Efficient and Interpretable Robot Manipulation with Graph Neural Networks**\n- Uses GNNs to solve robot manipulation by representing task-relevant entities as graph nodes\n- Learns policies over graph representations using imitation learning\n- Generalizes to new object configurations (highly relevant architecture choice)\n\n**Generative Factor Chaining (GFC)**\n- Learning-to-plan method for complex coordinated manipulation\n- Uses factor graphs with diffusion models for multi-arm coordination\n- Demonstrates compositional approaches to skill sequencing\n\n**WAGNN: A Weighted Aggregation Graph Neural Network for robot skill learning**\n- Learns structured policies through graph aggregation\n- Incorporates robot structure priors similar to what your GNN approach likely does\n\n**SCaR: Refining Skill Chaining for Long-Horizon Robotic Manipulation via Dual Regularization**\n- Recent work on skill chaining with regularization techniques\n- Addresses the skill composition problem you're tackling\n\n### Humanoid Loco-Manipulation (2025-2026)\n\n**Ψ₀: An Open Foundation Model Towards Universal Humanoid Loco-Manipulation** (March 2026)\n- Latest foundation model for humanoid loco-manipulation\n- Pre-trains on human demonstration data then fine-tunes on robot data\n- Most recent comparable work in the exact domain\n\n**OmniRetarget: Interaction-Preserving Data Generation for Humanoid Whole-Body Loco-Manipulation and Scene Interaction** (October 2025)\n- Addresses data generation for complex loco-manipulation\n- Preserves spatial and contact relationships between agent, terrain, and objects\n- Tackles similar data generation challenges\n\n**EgoHumanoid: Unlocking In-the-Wild Loco-Manipulation with Robot-Free Egocentric Demonstration** (February 2026)\n- Co-trains vision-language-action policies using human and robot data\n- Achieves 51% improvement over robot-only baselines\n- Demonstrates efficacy of human demonstration data for robot learning\n\n**AGILE: A Comprehensive Workflow for Humanoid Loco-Manipulation Learning** (March 2026)\n- End-to-end workflow for humanoid learning including synthetic data generation\n- Covers evaluation using motion metrics and VLA training\n\n### Sources:\n\n- [FATE: Closed-Loop Feasibility-Aware Task Generation](https://arxiv.org/html/2603.01505)\n- [Active Learning of Abstract Plan Feasibility](https://deepai.org/publication/active-learning-of-abstract-plan-feasibility)\n- [RoboGene: Diversity-Driven Agentic Framework](https://arxiv.org/html/2602.16444)\n- [Efficient and Interpretable Robot Manipulation with GNNs](https://arxiv.org/abs/2102.13177)\n- [Generative Factor Chaining](https://arxiv.org/html/2409.16275)\n- [Ψ₀: Universal Humanoid Loco-Manipulation](https://arxiv.org/abs/2603.12263)\n- [OmniRetarget: Interaction-Preserving Data Generation](https://arxiv.org/abs/2509.26633)\n- [EgoHumanoid: In-the-Wild Loco-Manipulation](https://arxiv.org/abs/2602.10106)\n- [AGILE: Comprehensive Workflow for Humanoid Learning](https://arxiv.org/html/2603.20147v1)\n- [ULC: Unified Fine-Grained Controller for Loco-Manipulation](https://arxiv.org/pdf/2507.06905)\n- [Physically Consistent Loco-Manipulation using Latent Diffusion](https://arxiv.org/html/2504.16843v1)\n\nYour Transition Feasibility Network using GNNs appears to fill a specific gap in learning transition compatibility between primitives for humanoid loco-manipulation, with most recent work (2025-2026) focusing on data generation, foundation models, and end-to-end learning rather than explicitly modeling feasibility of primitive transitions."
      }
    ],
    "totalDurationMs": 21681,
    "totalTokens": 21405,
    "totalToolUseCount": 5,
    "usage": {
      "input_tokens": 3833,
      "cache_creation_input_tokens": 2083,
      "cache_read_input_tokens": 14247,
      "output_tokens": 1242,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2083
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3833,
          "output_tokens": 1242,
          "cache_read_input_tokens": 14247,
          "cache_creation_input_tokens": 2083,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2083,
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
  "sourceToolAssistantUUID": "d7d8182d-41eb-47a3-8e2f-c838f301eef2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c9f1e88d-7547-445a-bdb2-8a60925de079",
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
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-10 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "780f53ac-35fd-4fa3-a216-99c9a4c8394c",
  "sessionId": "c9f1e88d-7547-445a-bdb2-8a60925de079"
}
```

---

### Runtime record

_source line 18_

```json
{
  "type": "ai-title",
  "aiTitle": "Verify CompLocoGen novelty and feasibility for humanoid loco-manipulation task generation",
  "sessionId": "c9f1e88d-7547-445a-bdb2-8a60925de079"
}
```

---

### Tool result

_source line 19 · 2026-05-10T19:21:30.811Z_

<details><summary>↩ Tool result · `toolu_011WkErdb77uYpp31p6uVLpZ`</summary>

```text
## Summary of Latest Competing Work in Humanoid Robot Data Generation and Task Composition (2026)

Based on comprehensive web searches, I've identified the major research directions and systems in this space:

### **1. Simulation and Task Generation Platforms**

**Genie Sim 3.0** - A unified simulation platform for robotic manipulation that uses LLM-powered tools to construct high-fidelity scenes from natural language instructions. It enables scene generation in minutes (vs. hours in traditional pipelines) and introduces the first benchmark using LLMs for automated evaluation and mass-generation of evaluation scenarios, with five core task suites (instruction understanding, spatial reasoning, atomic skill operation, disturbance adaptation, and training-to-deployment generalization).

### **2. Synthetic Data Generation Systems**

**GR00T-Dreams (NVIDIA)** - A blueprint using NVIDIA Cosmos world foundation models to generate vast amounts of synthetic trajectory data from a single image and language instructions. Uses Cosmos Predict-2 physical AI models combined with Cosmos-Reason1 for converting real robot data into synthetic trajectories. GR00T N1.5 was developed in 36 hours (vs. 3 months manual collection).

**DexMimicGen** - An automated data generation system for bimanual dexterous manipulation that scales from ~5 human demonstrations to 20,000+ synthetic demonstrations across 9 tasks. Achieved 90% real-world success on can sorting with just 40 synthetic rollouts from 4 real demos.

### **3. Whole-Body Loco-Manipulation Learning (Recent arxiv papers)**

- **LHM-Humanoid** (March 2026) - Long-horizon humanoid whole-body loco-manipulation in diverse environments using RL with teacher-student policy distillation into VLA models
- **Sumo** (April 2026) - Sim-to-real whole-body dynamic manipulation using test-time steering of pre-trained policies
- **WholeBodyVLA** (December 2025) - Unified latent VLA framework for learning from action-free egocentric videos
- **ResMimic** (October 2025) - Two-stage residual learning framework combining general motion tracking with task-specific residual policies
- **SkillBlender** (June 2025) - Hierarchical RL framework with pretraining of goal-conditioned primitive skills

### **4. World Foundation Models for Physical AI**

**NVIDIA Cosmos** - Trained on 9,000 trillion tokens from 20 million hours of real-world data (human interactions, robotics, driving). Cosmos Transfer 2.5 enables photorealistic synthetic video generation with faster data augmentation. Used by 1X (NEO Gamma humanoid) and Skild AI.

### **Key Trend**

The convergence is clear: **synthetic data generation from foundation models + task composition from LLMs + simulation environments** enable rapid scaling without manual teleoperation or scene construction. All major systems emphasize sim-to-real transfer, procedural-like task generation from language prompts, and training on mixtures of real and synthetic data.

Sources:
- [Genie Sim 3.0 - AGIBOT](https://arxiv.org/html/2601.02078v1)
- [NVIDIA GR00T-Dreams Technical Blog](https://developer.nvidia.com/blog/enhance-robot-learning-with-synthetic-trajectory-data-generated-by-world-foundation-models/)
- [DexMimicGen arxiv](https://arxiv.org/abs/2410.24185)
- [LHM-Humanoid arxiv](https://arxiv.org/html/2508.16943)
- [Sumo arxiv](https://arxiv.org/abs/2604.08508)
- [NVIDIA Cosmos World Foundation Models](https://developer.nvidia.com/blog/scale-synthetic-data-and-physical-ai-reasoning-with-nvidia-cosmos-world-foundation-models/)
- [WholeBodyVLA arxiv](https://arxiv.org/abs/2512.11047)
- [ResMimic arxiv](https://arxiv.org/abs/2510.05070v1)
- [SkillBlender arxiv](https://arxiv.org/html/2506.09366v1)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3e0e7c8e-0a8b-4846-9ee8-146ccf6aa28f",
  "isSidechain": false,
  "promptId": "9b9ebae5-ea89-443c-82ad-9f786b68d79f",
  "type": "user",
  "uuid": "97f43aff-5b5e-4de8-a369-02842192f65a",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to find the latest competing work in humanoid robot data generation and task composition from 2026. Please use WebSearch for:\n\n1. \"humanoid\" \"task generation\" OR \"environment generation\" simulation 2026\n2. site:arxiv.org humanoid whole-body loco-manipulation 2026\n3. \"GR00T-Dreams\" NVIDIA humanoid synthetic data 2026\n4. \"DexMimicGen\" humanoid 2026\n5. \"Cosmos\" humanoid video generation training data 2026\n6. \"procedural generation\" humanoid robot tasks 2026\n\nReport all relevant papers you find, especially anything that generates diverse humanoid training tasks or environments automatically.",
    "agentId": "ae310ba66c7250626",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "## Summary of Latest Competing Work in Humanoid Robot Data Generation and Task Composition (2026)\n\nBased on comprehensive web searches, I've identified the major research directions and systems in this space:\n\n### **1. Simulation and Task Generation Platforms**\n\n**Genie Sim 3.0** - A unified simulation platform for robotic manipulation that uses LLM-powered tools to construct high-fidelity scenes from natural language instructions. It enables scene generation in minutes (vs. hours in traditional pipelines) and introduces the first benchmark using LLMs for automated evaluation and mass-generation of evaluation scenarios, with five core task suites (instruction understanding, spatial reasoning, atomic skill operation, disturbance adaptation, and training-to-deployment generalization).\n\n### **2. Synthetic Data Generation Systems**\n\n**GR00T-Dreams (NVIDIA)** - A blueprint using NVIDIA Cosmos world foundation models to generate vast amounts of synthetic trajectory data from a single image and language instructions. Uses Cosmos Predict-2 physical AI models combined with Cosmos-Reason1 for converting real robot data into synthetic trajectories. GR00T N1.5 was developed in 36 hours (vs. 3 months manual collection).\n\n**DexMimicGen** - An automated data generation system for bimanual dexterous manipulation that scales from ~5 human demonstrations to 20,000+ synthetic demonstrations across 9 tasks. Achieved 90% real-world success on can sorting with just 40 synthetic rollouts from 4 real demos.\n\n### **3. Whole-Body Loco-Manipulation Learning (Recent arxiv papers)**\n\n- **LHM-Humanoid** (March 2026) - Long-horizon humanoid whole-body loco-manipulation in diverse environments using RL with teacher-student policy distillation into VLA models\n- **Sumo** (April 2026) - Sim-to-real whole-body dynamic manipulation using test-time steering of pre-trained policies\n- **WholeBodyVLA** (December 2025) - Unified latent VLA framework for learning from action-free egocentric videos\n- **ResMimic** (October 2025) - Two-stage residual learning framework combining general motion tracking with task-specific residual policies\n- **SkillBlender** (June 2025) - Hierarchical RL framework with pretraining of goal-conditioned primitive skills\n\n### **4. World Foundation Models for Physical AI**\n\n**NVIDIA Cosmos** - Trained on 9,000 trillion tokens from 20 million hours of real-world data (human interactions, robotics, driving). Cosmos Transfer 2.5 enables photorealistic synthetic video generation with faster data augmentation. Used by 1X (NEO Gamma humanoid) and Skild AI.\n\n### **Key Trend**\n\nThe convergence is clear: **synthetic data generation from foundation models + task composition from LLMs + simulation environments** enable rapid scaling without manual teleoperation or scene construction. All major systems emphasize sim-to-real transfer, procedural-like task generation from language prompts, and training on mixtures of real and synthetic data.\n\nSources:\n- [Genie Sim 3.0 - AGIBOT](https://arxiv.org/html/2601.02078v1)\n- [NVIDIA GR00T-Dreams Technical Blog](https://developer.nvidia.com/blog/enhance-robot-learning-with-synthetic-trajectory-data-generated-by-world-foundation-models/)\n- [DexMimicGen arxiv](https://arxiv.org/abs/2410.24185)\n- [LHM-Humanoid arxiv](https://arxiv.org/html/2508.16943)\n- [Sumo arxiv](https://arxiv.org/abs/2604.08508)\n- [NVIDIA Cosmos World Foundation Models](https://developer.nvidia.com/blog/scale-synthetic-data-and-physical-ai-reasoning-with-nvidia-cosmos-world-foundation-models/)\n- [WholeBodyVLA arxiv](https://arxiv.org/abs/2512.11047)\n- [ResMimic arxiv](https://arxiv.org/abs/2510.05070v1)\n- [SkillBlender arxiv](https://arxiv.org/html/2506.09366v1)"
      }
    ],
    "totalDurationMs": 23992,
    "totalTokens": 22019,
    "totalToolUseCount": 6,
    "usage": {
      "input_tokens": 4703,
      "cache_creation_input_tokens": 2077,
      "cache_read_input_tokens": 14228,
      "output_tokens": 1011,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2077
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4703,
          "output_tokens": 1011,
          "cache_read_input_tokens": 14228,
          "cache_creation_input_tokens": 2077,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2077,
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
      "otherToolCount": 6
    }
  },
  "sourceToolAssistantUUID": "3e0e7c8e-0a8b-4846-9ee8-146ccf6aa28f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c9f1e88d-7547-445a-bdb2-8a60925de079",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 20 · 2026-05-10T19:21:35.146Z_

Good initial findings. Let me now deep-dive into the most critical competing works — especially FATE (feasibility-aware task generation) and Ψ₀ — and verify the Humanoids 2026 deadline.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "97f43aff-5b5e-4de8-a369-02842192f65a",
  "isSidechain": false,
  "requestId": "req_011CauRyV7FwvX4pfcgCwoJb",
  "type": "assistant",
  "uuid": "a2a61c88-cfee-4e58-ab7a-25a26ab36941",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c9f1e88d-7547-445a-bdb2-8a60925de079",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013wbyRowTJ6SKFYuuVGhgcL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5763,
      "cache_read_input_tokens": 32890,
      "output_tokens": 1119,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5763,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1119,
          "cache_read_input_tokens": 32890,
          "cache_creation_input_tokens": 5763,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5763
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

_source line 21 · 2026-05-10T19:21:41.937Z_

<details open><summary>🔧 Tool call — Agent · `toolu_011CqYPJnbvgShdJN3Dq6w2w`</summary>

```json
{
  "subagent_type": "Explore",
  "description": "Deep dive FATE paper",
  "prompt": "I found a paper called \"FATE: Closed-Loop Feasibility-Aware Task Generation with Active Repair for Physically Grounded Robotic Curricula\" (arXiv:2603.01505). This is potentially a very important competing work for a proposal about learning transition feasibility for compositional task generation.\n\nPlease use WebSearch to find more details about this paper, then use WebFetch to read the arxiv abstract page (https://arxiv.org/abs/2603.01505). I need to know:\n1. What exactly does FATE do?\n2. Does it use feasibility prediction/learning?\n3. Does it generate compositional tasks?\n4. Is it for humanoid robots or general manipulation?\n5. How does it relate to a grammar-based compositional task generation approach with a GNN-based transition feasibility network?\n\nBe thorough — this could be the most important competing work."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a2a61c88-cfee-4e58-ab7a-25a26ab36941",
  "isSidechain": false,
  "requestId": "req_011CauRyV7FwvX4pfcgCwoJb",
  "type": "assistant",
  "uuid": "3f508934-aeef-4734-835c-3e10b444304d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c9f1e88d-7547-445a-bdb2-8a60925de079",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013wbyRowTJ6SKFYuuVGhgcL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5763,
      "cache_read_input_tokens": 32890,
      "output_tokens": 1119,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5763,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1119,
          "cache_read_input_tokens": 32890,
          "cache_creation_input_tokens": 5763,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5763
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

_source line 22 · 2026-05-10T19:21:48.197Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01K1uwsF8khvUJyzwrwVgsM2`</summary>

```json
{
  "subagent_type": "Explore",
  "description": "Search Psi0 and OmniRetarget",
  "prompt": "I need to check two important papers for a research proposal review:\n\n1. \"Ψ₀\" OR \"Psi-0\" humanoid loco-manipulation foundation model 2026 (arXiv:2603.12263) - Is this a foundation model that could make compositional task generation less necessary?\n\n2. \"OmniRetarget\" humanoid data generation 2025 (arXiv:2509.26633) - Does this generate diverse loco-manipulation data that overlaps with compositional task generation?\n\n3. Also search for: \"RoboGene\" task generation 2026 - another potentially competing automated task generation system\n\nPlease use WebSearch for each, and if possible WebFetch the arxiv abstracts. I need to understand whether these papers make a \"compositional grammar + transition feasibility network\" approach redundant or complementary."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3f508934-aeef-4734-835c-3e10b444304d",
  "isSidechain": false,
  "requestId": "req_011CauRyV7FwvX4pfcgCwoJb",
  "type": "assistant",
  "uuid": "6f957f87-82b9-43fd-9acd-3ad839453768",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c9f1e88d-7547-445a-bdb2-8a60925de079",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013wbyRowTJ6SKFYuuVGhgcL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5763,
      "cache_read_input_tokens": 32890,
      "output_tokens": 1119,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5763,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1119,
          "cache_read_input_tokens": 32890,
          "cache_creation_input_tokens": 5763,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5763
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

_source line 23 · 2026-05-10T19:21:52.964Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01VzhfdXR4EVpppvVJgqzedn`</summary>

```json
{
  "subagent_type": "Explore",
  "description": "Verify Humanoids 2026 deadline",
  "prompt": "I need to verify the exact paper submission deadline for the IEEE-RAS Humanoids 2026 conference (December 6-9, 2026, Santa Clara CA). The proposal claims June 30, 2026 but earlier it was claimed as July 24, 2026.\n\nPlease use WebSearch to find:\n1. \"Humanoids 2026\" paper deadline OR submission deadline\n2. \"IEEE-RAS 2026 humanoid robots\" call for papers\n3. Try WebFetch on https://2026.ieee-humanoids.org/ to check the actual deadline\n\nAlso search for: \"Humanoids 2025\" deadline to see what typical deadlines are for this conference (the 2025 edition would have had deadlines in 2025).\n\nReport the exact dates you find."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6f957f87-82b9-43fd-9acd-3ad839453768",
  "isSidechain": false,
  "requestId": "req_011CauRyV7FwvX4pfcgCwoJb",
  "type": "assistant",
  "uuid": "6db2c0db-434e-46a0-8635-159ff1d53f55",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c9f1e88d-7547-445a-bdb2-8a60925de079",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013wbyRowTJ6SKFYuuVGhgcL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5763,
      "cache_read_input_tokens": 32890,
      "output_tokens": 1119,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5763,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1119,
          "cache_read_input_tokens": 32890,
          "cache_creation_input_tokens": 5763,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5763
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

_source line 24 · 2026-05-10T19:21:57.851Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01S9zj3pSHkt5D8s4Kyoj68D`</summary>

```json
{
  "subagent_type": "Explore",
  "description": "Search SuperDyno and physics predicates",
  "prompt": "For a research proposal review, I need to verify:\n\n1. \"SuperDyno\" ICLR 2025 humanoid neural dynamics - verify this paper exists and what it does\n2. \"Humanoid Hanoi\" arXiv:2602.13850 skill composition distribution shift - verify this paper\n3. \"FALCON\" arXiv:2505.06776 force-adaptive humanoid loco-manipulation - verify this paper\n4. Search for: \"learned dynamics\" OR \"neural dynamics\" humanoid skill composition feasibility 2025 2026 - are there papers that learn dynamics models specifically for predicting skill composition success?\n\nUse WebSearch for each query. Report what you find."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6db2c0db-434e-46a0-8635-159ff1d53f55",
  "isSidechain": false,
  "requestId": "req_011CauRyV7FwvX4pfcgCwoJb",
  "type": "assistant",
  "uuid": "ac1a70a8-99a7-477c-b10a-f89070568f20",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c9f1e88d-7547-445a-bdb2-8a60925de079",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013wbyRowTJ6SKFYuuVGhgcL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5763,
      "cache_read_input_tokens": 32890,
      "output_tokens": 1119,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5763,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1119,
          "cache_read_input_tokens": 32890,
          "cache_creation_input_tokens": 5763,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5763
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

_source line 25 · 2026-05-10T19:22:05.707Z_

<details><summary>↩ Tool result · `toolu_01VzhfdXR4EVpppvVJgqzedn`</summary>

```text
Based on my search results, I've found conflicting information about the Humanoids 2026 paper submission deadline. Here's what I discovered:

## Key Findings:

**Humanoids 2026 Deadline - CONFLICTING REPORTS:**

1. **WebFetch from the official conference website (2026.ieee-humanoids.org)** states:
   - **Paper submission deadline: July 24, 2026**
   - Supplementary video materials deadline: July 27, 2026

2. **WebSearch results** indicate:
   - **Call for papers submission window: October 1, 2025 to June 30, 2026**
   - This suggests June 30, 2026 as the deadline

The official conference website (fetched directly) appears to be the most authoritative source and indicates **July 24, 2026** as the paper submission deadline, not June 30, 2026.

## Historical Context (Humanoids 2025):

For comparison, Humanoids 2025 had:
- Regular papers deadline: May 1-15, 2025
- Late Breaking Results: July 31, 2025
- Final manuscript: August 15, 2025
- Conference dates: September 30 - October 2, 2025

## Conclusion:

The proposal's claim of **June 30, 2026** appears to be incorrect. According to the official Humanoids 2026 website, the correct deadline is **July 24, 2026**. This aligns better with the earlier claim of July 24, 2026 that was mentioned in your question.

I recommend verifying this directly on the official Humanoids 2026 website at https://2026.ieee-humanoids.org/ for the most current information.

Sources:
- [Humanoids 2026 Official Website](https://2026.ieee-humanoids.org/)
- [Humanoids 2025 Conference](https://2025humanoids.org/)
- [WikiCFP - IEEE-RAS Humanoids Conference](http://www.wikicfp.com/cfp/program?id=1239)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6db2c0db-434e-46a0-8635-159ff1d53f55",
  "isSidechain": false,
  "promptId": "9b9ebae5-ea89-443c-82ad-9f786b68d79f",
  "type": "user",
  "uuid": "f4f3ac09-0d0c-414e-b41b-d4ed78f53aa1",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to verify the exact paper submission deadline for the IEEE-RAS Humanoids 2026 conference (December 6-9, 2026, Santa Clara CA). The proposal claims June 30, 2026 but earlier it was claimed as July 24, 2026.\n\nPlease use WebSearch to find:\n1. \"Humanoids 2026\" paper deadline OR submission deadline\n2. \"IEEE-RAS 2026 humanoid robots\" call for papers\n3. Try WebFetch on https://2026.ieee-humanoids.org/ to check the actual deadline\n\nAlso search for: \"Humanoids 2025\" deadline to see what typical deadlines are for this conference (the 2025 edition would have had deadlines in 2025).\n\nReport the exact dates you find.",
    "agentId": "a5f39603dbb2f6d7e",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Based on my search results, I've found conflicting information about the Humanoids 2026 paper submission deadline. Here's what I discovered:\n\n## Key Findings:\n\n**Humanoids 2026 Deadline - CONFLICTING REPORTS:**\n\n1. **WebFetch from the official conference website (2026.ieee-humanoids.org)** states:\n   - **Paper submission deadline: July 24, 2026**\n   - Supplementary video materials deadline: July 27, 2026\n\n2. **WebSearch results** indicate:\n   - **Call for papers submission window: October 1, 2025 to June 30, 2026**\n   - This suggests June 30, 2026 as the deadline\n\nThe official conference website (fetched directly) appears to be the most authoritative source and indicates **July 24, 2026** as the paper submission deadline, not June 30, 2026.\n\n## Historical Context (Humanoids 2025):\n\nFor comparison, Humanoids 2025 had:\n- Regular papers deadline: May 1-15, 2025\n- Late Breaking Results: July 31, 2025\n- Final manuscript: August 15, 2025\n- Conference dates: September 30 - October 2, 2025\n\n## Conclusion:\n\nThe proposal's claim of **June 30, 2026** appears to be incorrect. According to the official Humanoids 2026 website, the correct deadline is **July 24, 2026**. This aligns better with the earlier claim of July 24, 2026 that was mentioned in your question.\n\nI recommend verifying this directly on the official Humanoids 2026 website at https://2026.ieee-humanoids.org/ for the most current information.\n\nSources:\n- [Humanoids 2026 Official Website](https://2026.ieee-humanoids.org/)\n- [Humanoids 2025 Conference](https://2025humanoids.org/)\n- [WikiCFP - IEEE-RAS Humanoids Conference](http://www.wikicfp.com/cfp/program?id=1239)"
      }
    ],
    "totalDurationMs": 12740,
    "totalTokens": 17820,
    "totalToolUseCount": 4,
    "usage": {
      "input_tokens": 686,
      "cache_creation_input_tokens": 2387,
      "cache_read_input_tokens": 14251,
      "output_tokens": 496,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2387
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 686,
          "output_tokens": 496,
          "cache_read_input_tokens": 14251,
          "cache_creation_input_tokens": 2387,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2387,
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
  "sourceToolAssistantUUID": "6db2c0db-434e-46a0-8635-159ff1d53f55",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c9f1e88d-7547-445a-bdb2-8a60925de079",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-10T19:22:14.556Z_

<details><summary>↩ Tool result · `toolu_011CqYPJnbvgShdJN3Dq6w2w`</summary>

```text
Excellent! I now have comprehensive information about this paper. Let me compile the detailed findings:

## FATE: Detailed Analysis

Based on the arxiv abstract and full paper, here's what you need to know about this competing work:

### 1. **What FATE Does**
FATE (Feasibility-Aware Task Generation with Active Repair) is a **closed-loop, self-correcting framework** that reimagines robotic task generation as an iterative validation-and-refinement process. It solves a critical problem: LLM-generated tasks are often "linguistically coherent but physically infeasible." Rather than decoupling generation and verification into discrete stages, FATE embeds a generalist embodied agent directly into the generation loop to guarantee physical groundedness.

### 2. **Feasibility Prediction/Learning**
**This is a key difference from a GNN-based transition feasibility network approach.** FATE does NOT use learned feasibility prediction. Instead, it uses:
- A **Vision-Language Model auditor** (RoboBrain 2.0, 7B parameters) for logical feasibility checks
- A **two-phase validation pipeline**:
  - **Static Phase**: Perceptual validation detecting geometric violations and affordance mismatches through an "Ante-Auditor"
  - **Dynamic Phase**: Runtime execution monitoring via an "In-step Auditor"
- **Four consistency conditions** for feasibility assessment: reachability, affordance matching, physical plausibility, and morphological compatibility
- Active **repair mechanisms** when infeasible tasks are detected (Ante-Repair, Primitive-Repair, RL-Repair)

### 3. **Compositional Tasks**
**No.** FATE generates **individual task instances**, not compositional task sequences. While tasks are hierarchically decomposed into execution primitives, the framework targets single long-horizon objectives rather than compositional combinations.

### 4. **Robot Platform**
**Not humanoid.** FATE uses a **RidgebackFranka** embodiment—a **7-DoF arm on a holonomic base** for coordinated navigation and manipulation tasks. This is a general manipulation platform, not specifically humanoid.

### 5. **Comparison to Grammar-Based + GNN Feasibility Network Approach**
This is fundamentally different from your proposal:
- **FATE**: Uses VLM-based validation + active repair (iterative refinement in the loop)
- **Your approach**: Uses grammar-based composition + learned GNN feasibility prediction (upfront prediction before execution)

FATE's strength is its closed-loop active repair mechanism that catches and fixes physical infeasibility through simulation/execution. Your approach would differentiate by:
- Using **compositional task generation** (FATE doesn't do this)
- Deploying a **learned neural network predictor** (GNN for transition feasibility) rather than VLM auditing
- Potentially being more efficient by predicting feasibility before generation rather than iteratively repairing

**Bottom line:** FATE is orthogonal work focused on individual task feasibility validation through active repair. Your paper should emphasize that you're addressing **compositional task generation** with **learned feasibility prediction**, which are distinct problems that FATE doesn't tackle.

Sources:
- [FATE arxiv abstract](https://arxiv.org/abs/2603.01505)
- [FATE arxiv HTML](https://arxiv.org/html/2603.01505)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3f508934-aeef-4734-835c-3e10b444304d",
  "isSidechain": false,
  "promptId": "9b9ebae5-ea89-443c-82ad-9f786b68d79f",
  "type": "user",
  "uuid": "1da02f4f-793b-4fa7-9a6d-329d2af0c9bf",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I found a paper called \"FATE: Closed-Loop Feasibility-Aware Task Generation with Active Repair for Physically Grounded Robotic Curricula\" (arXiv:2603.01505). This is potentially a very important competing work for a proposal about learning transition feasibility for compositional task generation.\n\nPlease use WebSearch to find more details about this paper, then use WebFetch to read the arxiv abstract page (https://arxiv.org/abs/2603.01505). I need to know:\n1. What exactly does FATE do?\n2. Does it use feasibility prediction/learning?\n3. Does it generate compositional tasks?\n4. Is it for humanoid robots or general manipulation?\n5. How does it relate to a grammar-based compositional task generation approach with a GNN-based transition feasibility network?\n\nBe thorough — this could be the most important competing work.",
    "agentId": "a6f87b661e55a9b25",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Excellent! I now have comprehensive information about this paper. Let me compile the detailed findings:\n\n## FATE: Detailed Analysis\n\nBased on the arxiv abstract and full paper, here's what you need to know about this competing work:\n\n### 1. **What FATE Does**\nFATE (Feasibility-Aware Task Generation with Active Repair) is a **closed-loop, self-correcting framework** that reimagines robotic task generation as an iterative validation-and-refinement process. It solves a critical problem: LLM-generated tasks are often \"linguistically coherent but physically infeasible.\" Rather than decoupling generation and verification into discrete stages, FATE embeds a generalist embodied agent directly into the generation loop to guarantee physical groundedness.\n\n### 2. **Feasibility Prediction/Learning**\n**This is a key difference from a GNN-based transition feasibility network approach.** FATE does NOT use learned feasibility prediction. Instead, it uses:\n- A **Vision-Language Model auditor** (RoboBrain 2.0, 7B parameters) for logical feasibility checks\n- A **two-phase validation pipeline**:\n  - **Static Phase**: Perceptual validation detecting geometric violations and affordance mismatches through an \"Ante-Auditor\"\n  - **Dynamic Phase**: Runtime execution monitoring via an \"In-step Auditor\"\n- **Four consistency conditions** for feasibility assessment: reachability, affordance matching, physical plausibility, and morphological compatibility\n- Active **repair mechanisms** when infeasible tasks are detected (Ante-Repair, Primitive-Repair, RL-Repair)\n\n### 3. **Compositional Tasks**\n**No.** FATE generates **individual task instances**, not compositional task sequences. While tasks are hierarchically decomposed into execution primitives, the framework targets single long-horizon objectives rather than compositional combinations.\n\n### 4. **Robot Platform**\n**Not humanoid.** FATE uses a **RidgebackFranka** embodiment—a **7-DoF arm on a holonomic base** for coordinated navigation and manipulation tasks. This is a general manipulation platform, not specifically humanoid.\n\n### 5. **Comparison to Grammar-Based + GNN Feasibility Network Approach**\nThis is fundamentally different from your proposal:\n- **FATE**: Uses VLM-based validation + active repair (iterative refinement in the loop)\n- **Your approach**: Uses grammar-based composition + learned GNN feasibility prediction (upfront prediction before execution)\n\nFATE's strength is its closed-loop active repair mechanism that catches and fixes physical infeasibility through simulation/execution. Your approach would differentiate by:\n- Using **compositional task generation** (FATE doesn't do this)\n- Deploying a **learned neural network predictor** (GNN for transition feasibility) rather than VLM auditing\n- Potentially being more efficient by predicting feasibility before generation rather than iteratively repairing\n\n**Bottom line:** FATE is orthogonal work focused on individual task feasibility validation through active repair. Your paper should emphasize that you're addressing **compositional task generation** with **learned feasibility prediction**, which are distinct problems that FATE doesn't tackle.\n\nSources:\n- [FATE arxiv abstract](https://arxiv.org/abs/2603.01505)\n- [FATE arxiv HTML](https://arxiv.org/html/2603.01505)"
      }
    ],
    "totalDurationMs": 32613,
    "totalTokens": 17849,
    "totalToolUseCount": 3,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 579,
      "cache_read_input_tokens": 16478,
      "output_tokens": 787,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 579
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 787,
          "cache_read_input_tokens": 16478,
          "cache_creation_input_tokens": 579,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 579,
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
  "sourceToolAssistantUUID": "3f508934-aeef-4734-835c-3e10b444304d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c9f1e88d-7547-445a-bdb2-8a60925de079",
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
  "leafUuid": "1da02f4f-793b-4fa7-9a6d-329d2af0c9bf",
  "sessionId": "c9f1e88d-7547-445a-bdb2-8a60925de079"
}
```

---

### Runtime record

_source line 28_

```json
{
  "type": "ai-title",
  "aiTitle": "Verify CompLocoGen novelty and feasibility for humanoid loco-manipulation task generation",
  "sessionId": "c9f1e88d-7547-445a-bdb2-8a60925de079"
}
```

---

### Tool result

_source line 29 · 2026-05-10T19:22:15.204Z_

<details><summary>↩ Tool result · `toolu_01K1uwsF8khvUJyzwrwVgsM2`</summary>

```text
## Analysis Summary

Based on my research, here's how these three systems relate to a "compositional grammar + transition feasibility network" approach:

### 1. **Ψ₀ (Psi-Zero) Foundation Model** - COMPLEMENTARY
- **Focus**: Visual-language foundation model using staged training (VLM pre-training on human video + post-training on robot data)
- **Strength**: Learns generalizable visual-action representations with high data efficiency
- **Relationship**: This is a **policy learning model**, not a task generation system. It doesn't address *how* to generate diverse task specifications or trajectories. Your compositional grammar could actually be a **complementary pre-processing layer** to generate the diverse tasks that feed into Ψ₀'s training pipeline.
- **Overlap**: Minimal - Ψ₀ focuses on learning from existing data, not generating it

### 2. **OmniRetarget** - PARTIALLY OVERLAPPING
- **Focus**: Data generation through motion retargeting that preserves human-object-environment interactions
- **Strength**: Generates kinematically feasible, diverse trajectories (8+ hours) from human motion capture
- **Relationship**: This is a **data generation system** like your approach, but it's **human-centric**. It generates diverse trajectories by retargeting human motions while preserving interaction constraints.
- **Key Difference**: OmniRetarget relies on existing human motion capture data; your compositional grammar + feasibility network could be more flexible for generating novel task combinations not present in human data
- **Complementarity**: OmniRetarget excels at realistic manipulation constraints; your compositional approach excels at task diversity beyond human experience

### 3. **RoboGene** - DIRECTLY COMPETITIVE
- **Focus**: Automated task generation for VLA pre-training using diversity-driven sampling + self-reflection
- **Strength**: Generates diverse task specifications (18k trajectories) with feasibility checking; integrates diversity sampling + constraint validation
- **Relationship**: This is your **most direct competitor**. RoboGene uses:
  - Diversity-driven sampling (similar goal to compositional grammar)
  - Self-reflection/feasibility checking (similar to your transition feasibility network)
  - Human-in-the-loop refinement
- **Critical Overlap**: Both aim to generate diverse, feasible task specifications for robotic learning

### Strategic Positioning

**Your approach is NOT redundant:**

1. **RoboGene is an LLM-based approach** (uses GPT-4o, Gemini as backbone agents). Your grammar-based + network-based approach is **structurally different and could be more efficient** (no LLM inference needed, more interpretable)

2. **OmniRetarget + Your Grammar**: You could integrate OmniRetarget's trajectory generation with your compositional grammar to handle the "real-world constraint" problem that OmniRetarget solves better than RoboGene

3. **Ψ₀ + Your System**: Your compositional task generation is a **perfect upstream task provider** for Ψ₀'s training pipeline

### Recommendation
Position your work as:
- **Complementary to Ψ₀**: "Our compositional grammar efficiently generates the diverse task specifications needed for VLA foundation model pre-training"
- **Alternative to RoboGene**: "Unlike LLM-based task generation, our grammar + feasibility network approach is more efficient, interpretable, and doesn't require foundation model inference"
- **Potential integration with OmniRetarget**: "Our grammar could specify high-level task compositions; OmniRetarget handles constraint-preserving trajectory generation"

Sources:
- [Ψ₀: An Open Foundation Model Towards Universal Humanoid Loco-Manipulation](https://arxiv.org/abs/2603.12263)
- [OmniRetarget: Interaction-Preserving Data Generation](https://arxiv.org/abs/2509.26633)
- [RoboGene: Boosting VLA Pre-training via Diversity-Driven Agentic Framework](https://arxiv.org/abs/2602.16444)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6f957f87-82b9-43fd-9acd-3ad839453768",
  "isSidechain": false,
  "promptId": "9b9ebae5-ea89-443c-82ad-9f786b68d79f",
  "type": "user",
  "uuid": "d5259ead-2b17-41bb-84ff-8b4fccbe46fc",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to check two important papers for a research proposal review:\n\n1. \"Ψ₀\" OR \"Psi-0\" humanoid loco-manipulation foundation model 2026 (arXiv:2603.12263) - Is this a foundation model that could make compositional task generation less necessary?\n\n2. \"OmniRetarget\" humanoid data generation 2025 (arXiv:2509.26633) - Does this generate diverse loco-manipulation data that overlaps with compositional task generation?\n\n3. Also search for: \"RoboGene\" task generation 2026 - another potentially competing automated task generation system\n\nPlease use WebSearch for each, and if possible WebFetch the arxiv abstracts. I need to understand whether these papers make a \"compositional grammar + transition feasibility network\" approach redundant or complementary.",
    "agentId": "a84559ebb60edf065",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "## Analysis Summary\n\nBased on my research, here's how these three systems relate to a \"compositional grammar + transition feasibility network\" approach:\n\n### 1. **Ψ₀ (Psi-Zero) Foundation Model** - COMPLEMENTARY\n- **Focus**: Visual-language foundation model using staged training (VLM pre-training on human video + post-training on robot data)\n- **Strength**: Learns generalizable visual-action representations with high data efficiency\n- **Relationship**: This is a **policy learning model**, not a task generation system. It doesn't address *how* to generate diverse task specifications or trajectories. Your compositional grammar could actually be a **complementary pre-processing layer** to generate the diverse tasks that feed into Ψ₀'s training pipeline.\n- **Overlap**: Minimal - Ψ₀ focuses on learning from existing data, not generating it\n\n### 2. **OmniRetarget** - PARTIALLY OVERLAPPING\n- **Focus**: Data generation through motion retargeting that preserves human-object-environment interactions\n- **Strength**: Generates kinematically feasible, diverse trajectories (8+ hours) from human motion capture\n- **Relationship**: This is a **data generation system** like your approach, but it's **human-centric**. It generates diverse trajectories by retargeting human motions while preserving interaction constraints.\n- **Key Difference**: OmniRetarget relies on existing human motion capture data; your compositional grammar + feasibility network could be more flexible for generating novel task combinations not present in human data\n- **Complementarity**: OmniRetarget excels at realistic manipulation constraints; your compositional approach excels at task diversity beyond human experience\n\n### 3. **RoboGene** - DIRECTLY COMPETITIVE\n- **Focus**: Automated task generation for VLA pre-training using diversity-driven sampling + self-reflection\n- **Strength**: Generates diverse task specifications (18k trajectories) with feasibility checking; integrates diversity sampling + constraint validation\n- **Relationship**: This is your **most direct competitor**. RoboGene uses:\n  - Diversity-driven sampling (similar goal to compositional grammar)\n  - Self-reflection/feasibility checking (similar to your transition feasibility network)\n  - Human-in-the-loop refinement\n- **Critical Overlap**: Both aim to generate diverse, feasible task specifications for robotic learning\n\n### Strategic Positioning\n\n**Your approach is NOT redundant:**\n\n1. **RoboGene is an LLM-based approach** (uses GPT-4o, Gemini as backbone agents). Your grammar-based + network-based approach is **structurally different and could be more efficient** (no LLM inference needed, more interpretable)\n\n2. **OmniRetarget + Your Grammar**: You could integrate OmniRetarget's trajectory generation with your compositional grammar to handle the \"real-world constraint\" problem that OmniRetarget solves better than RoboGene\n\n3. **Ψ₀ + Your System**: Your compositional task generation is a **perfect upstream task provider** for Ψ₀'s training pipeline\n\n### Recommendation\nPosition your work as:\n- **Complementary to Ψ₀**: \"Our compositional grammar efficiently generates the diverse task specifications needed for VLA foundation model pre-training\"\n- **Alternative to RoboGene**: \"Unlike LLM-based task generation, our grammar + feasibility network approach is more efficient, interpretable, and doesn't require foundation model inference\"\n- **Potential integration with OmniRetarget**: \"Our grammar could specify high-level task compositions; OmniRetarget handles constraint-preserving trajectory generation\"\n\nSources:\n- [Ψ₀: An Open Foundation Model Towards Universal Humanoid Loco-Manipulation](https://arxiv.org/abs/2603.12263)\n- [OmniRetarget: Interaction-Preserving Data Generation](https://arxiv.org/abs/2509.26633)\n- [RoboGene: Boosting VLA Pre-training via Diversity-Driven Agentic Framework](https://arxiv.org/abs/2602.16444)"
      }
    ],
    "totalDurationMs": 27005,
    "totalTokens": 20497,
    "totalToolUseCount": 6,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1195,
      "cache_read_input_tokens": 18316,
      "output_tokens": 979,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1195
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 979,
          "cache_read_input_tokens": 18316,
          "cache_creation_input_tokens": 1195,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1195,
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
      "otherToolCount": 6
    }
  },
  "sourceToolAssistantUUID": "6f957f87-82b9-43fd-9acd-3ad839453768",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c9f1e88d-7547-445a-bdb2-8a60925de079",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-10T19:22:17.827Z_

<details><summary>↩ Tool result · `toolu_01S9zj3pSHkt5D8s4Kyoj68D`</summary>

```text
## Research Verification Results

### 1. SuperDyno - ICLR 2025 ✓ VERIFIED
**Status:** Paper exists and is confirmed
- **Full Title:** "Scalable Humanoid Whole-Body Control via Differentiable Neural Network Dynamics"
- **Publication:** Workshop paper at ICLR 2025
- **What it does:** Proposes a framework combining supervised and reinforcement learning for scalable humanoid controller learning using learned neural dynamics models. The key innovation is using differentiable neural network dynamics as a simulator for accurate prediction and effective policy optimization.
- **Key benefit:** Achieves higher sample efficiency, lower tracking error, and scales to datasets with tens of thousands of motion clips.
- **Project:** https://dynamics-humanoid.github.io/dynamics-humanoid/

### 2. Humanoid Hanoi - arXiv:2602.13850 ✓ VERIFIED
**Status:** Paper exists and is confirmed
- **Full Title:** "Humanoid Hanoi: Investigating Shared Whole-Body Control for Skill-Based Box Rearrangement"
- **Focus:** Addresses distribution shift in skill composition by using a shared whole-body controller (WBC) for executing multiple skills
- **What it does:** Implements a long-horizon Tower-of-Hanoi box rearrangement benchmark and tackles the problem that skill composition causes state and command distribution shifts that reduce robustness
- **Solution:** Uses data aggregation with domain randomization to augment shared-WBC training with closed-loop skill execution rollouts
- **Validation:** Tested in simulation and on Digit V3 humanoid robot

### 3. FALCON - arXiv:2505.06776 ✓ VERIFIED
**Status:** Paper exists and is confirmed
- **Full Title:** "FALCON: Learning Force-Adaptive Humanoid Loco-Manipulation"
- **What it does:** Dual-agent RL framework for robust force-adaptive humanoid loco-manipulation that decomposes control into lower-body (stable locomotion) and upper-body (end-effector tracking with implicit force compensation) agents
- **Key results:** 2x more accurate upper-body tracking vs baselines while maintaining robust locomotion; tested on real-world tasks including payload transport (0-20N), cart-pulling (0-100N), and door-opening (0-40N)
- **Venue:** L4DC 2026
- **Authors:** CMU, Field AI, Nissan USA

### 4. Learned/Neural Dynamics for Skill Composition - LIMITED FINDINGS
**Status:** Related work exists, but limited specific papers on this exact topic
- **Found:** SuperDyno (above) uses learned neural dynamics for control, and "Neural Robot Dynamics" (NeRD) is a learned dynamics model for predicting articulated rigid-body states
- **General trend:** The research community is exploring skill composition and learned dynamics models, but there appear to be few papers specifically focused on using learned dynamics to predict skill composition feasibility
- **Related research:** "Compose Your Policies! Improving Diffusion-based or Flow-based Robot Policies via Test-time Distribution-level Composition" addresses policy composition methods (2025-2026)

---

Sources:
- [SuperDyno on OpenReview](https://openreview.net/forum?id=FPgKt7bA8w)
- [SuperDyno Project Website](https://dynamics-humanoid.github.io/dynamics-humanoid/)
- [Humanoid Hanoi on arXiv](https://arxiv.org/abs/2602.13850)
- [FALCON on arXiv](https://arxiv.org/abs/2505.06776)
- [FALCON Project Website](https://lecar-lab.github.io/falcon-humanoid/)
- [Neural Robot Dynamics on arXiv](https://arxiv.org/pdf/2508.15755)
- [Learning-based Dynamics Models Review](https://www.science.org/doi/10.1126/scirobotics.adt1497)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ac1a70a8-99a7-477c-b10a-f89070568f20",
  "isSidechain": false,
  "promptId": "9b9ebae5-ea89-443c-82ad-9f786b68d79f",
  "type": "user",
  "uuid": "c6199577-36d8-46cd-a350-1c5778a95be0",
  "toolUseResult": {
    "status": "completed",
    "prompt": "For a research proposal review, I need to verify:\n\n1. \"SuperDyno\" ICLR 2025 humanoid neural dynamics - verify this paper exists and what it does\n2. \"Humanoid Hanoi\" arXiv:2602.13850 skill composition distribution shift - verify this paper\n3. \"FALCON\" arXiv:2505.06776 force-adaptive humanoid loco-manipulation - verify this paper\n4. Search for: \"learned dynamics\" OR \"neural dynamics\" humanoid skill composition feasibility 2025 2026 - are there papers that learn dynamics models specifically for predicting skill composition success?\n\nUse WebSearch for each query. Report what you find.",
    "agentId": "a6cf77a0047a23b0c",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "## Research Verification Results\n\n### 1. SuperDyno - ICLR 2025 ✓ VERIFIED\n**Status:** Paper exists and is confirmed\n- **Full Title:** \"Scalable Humanoid Whole-Body Control via Differentiable Neural Network Dynamics\"\n- **Publication:** Workshop paper at ICLR 2025\n- **What it does:** Proposes a framework combining supervised and reinforcement learning for scalable humanoid controller learning using learned neural dynamics models. The key innovation is using differentiable neural network dynamics as a simulator for accurate prediction and effective policy optimization.\n- **Key benefit:** Achieves higher sample efficiency, lower tracking error, and scales to datasets with tens of thousands of motion clips.\n- **Project:** https://dynamics-humanoid.github.io/dynamics-humanoid/\n\n### 2. Humanoid Hanoi - arXiv:2602.13850 ✓ VERIFIED\n**Status:** Paper exists and is confirmed\n- **Full Title:** \"Humanoid Hanoi: Investigating Shared Whole-Body Control for Skill-Based Box Rearrangement\"\n- **Focus:** Addresses distribution shift in skill composition by using a shared whole-body controller (WBC) for executing multiple skills\n- **What it does:** Implements a long-horizon Tower-of-Hanoi box rearrangement benchmark and tackles the problem that skill composition causes state and command distribution shifts that reduce robustness\n- **Solution:** Uses data aggregation with domain randomization to augment shared-WBC training with closed-loop skill execution rollouts\n- **Validation:** Tested in simulation and on Digit V3 humanoid robot\n\n### 3. FALCON - arXiv:2505.06776 ✓ VERIFIED\n**Status:** Paper exists and is confirmed\n- **Full Title:** \"FALCON: Learning Force-Adaptive Humanoid Loco-Manipulation\"\n- **What it does:** Dual-agent RL framework for robust force-adaptive humanoid loco-manipulation that decomposes control into lower-body (stable locomotion) and upper-body (end-effector tracking with implicit force compensation) agents\n- **Key results:** 2x more accurate upper-body tracking vs baselines while maintaining robust locomotion; tested on real-world tasks including payload transport (0-20N), cart-pulling (0-100N), and door-opening (0-40N)\n- **Venue:** L4DC 2026\n- **Authors:** CMU, Field AI, Nissan USA\n\n### 4. Learned/Neural Dynamics for Skill Composition - LIMITED FINDINGS\n**Status:** Related work exists, but limited specific papers on this exact topic\n- **Found:** SuperDyno (above) uses learned neural dynamics for control, and \"Neural Robot Dynamics\" (NeRD) is a learned dynamics model for predicting articulated rigid-body states\n- **General trend:** The research community is exploring skill composition and learned dynamics models, but there appear to be few papers specifically focused on using learned dynamics to predict skill composition feasibility\n- **Related research:** \"Compose Your Policies! Improving Diffusion-based or Flow-based Robot Policies via Test-time Distribution-level Composition\" addresses policy composition methods (2025-2026)\n\n---\n\nSources:\n- [SuperDyno on OpenReview](https://openreview.net/forum?id=FPgKt7bA8w)\n- [SuperDyno Project Website](https://dynamics-humanoid.github.io/dynamics-humanoid/)\n- [Humanoid Hanoi on arXiv](https://arxiv.org/abs/2602.13850)\n- [FALCON on arXiv](https://arxiv.org/abs/2505.06776)\n- [FALCON Project Website](https://lecar-lab.github.io/falcon-humanoid/)\n- [Neural Robot Dynamics on arXiv](https://arxiv.org/pdf/2508.15755)\n- [Learning-based Dynamics Models Review](https://www.science.org/doi/10.1126/scirobotics.adt1497)"
      }
    ],
    "totalDurationMs": 19974,
    "totalTokens": 19727,
    "totalToolUseCount": 4,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 4540,
      "cache_read_input_tokens": 14228,
      "output_tokens": 952,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4540
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 952,
          "cache_read_input_tokens": 14228,
          "cache_creation_input_tokens": 4540,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4540,
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
  "sourceToolAssistantUUID": "ac1a70a8-99a7-477c-b10a-f89070568f20",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c9f1e88d-7547-445a-bdb2-8a60925de079",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 31 · 2026-05-10T19:22:17.831Z_

```json
{
  "parentUuid": "c6199577-36d8-46cd-a350-1c5778a95be0",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "3eea9177-41b4-4da7-a066-87c6b398c1ac",
  "timestamp": "2026-05-10T19:22:17.831Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c9f1e88d-7547-445a-bdb2-8a60925de079",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 32 · 2026-05-10T19:22:22.442Z_

Now let me do a final round of targeted searches on the most critical gaps I've identified — particularly RoboGene's overlap, the compute budget realism, and whether the TFN's active learning framing has precedent.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3eea9177-41b4-4da7-a066-87c6b398c1ac",
  "isSidechain": false,
  "requestId": "req_011CauS2x83ew6tCmwW1MH6n",
  "type": "assistant",
  "uuid": "2a5d2a0c-e217-40aa-901e-6801f4a95084",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c9f1e88d-7547-445a-bdb2-8a60925de079",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Rpo5if3EZAWgbYTxGXDkP8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4528,
      "cache_read_input_tokens": 38653,
      "output_tokens": 866,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4528,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 866,
          "cache_read_input_tokens": 38653,
          "cache_creation_input_tokens": 4528,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4528
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

_source line 33 · 2026-05-10T19:22:29.435Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01DTsF3kGMo7xuP2H2Vke3qB`</summary>

```json
{
  "subagent_type": "Explore",
  "description": "Deep dive RoboGene overlap",
  "prompt": "I need to deeply understand \"RoboGene: Boosting VLA Pre-training via Diversity-Driven Agentic Framework for Real-World Task Generation\" (arXiv:2602.16444, Feb 2026). This may be a critical competing work for a proposal about grammar-based compositional task generation with learned feasibility.\n\nPlease use WebFetch to read the abstract and details at https://arxiv.org/abs/2602.16444\n\nI need to understand:\n1. Does RoboGene generate compositional multi-stage tasks or single tasks?\n2. Does it have any feasibility prediction mechanism?\n3. Does it target humanoid robots specifically?\n4. What's its scale of generation (number of tasks, trajectories)?\n5. How does it handle physical feasibility?\n\nThis is crucial for assessing whether a \"grammar + GNN transition feasibility network\" approach offers genuine novelty over RoboGene."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2a5d2a0c-e217-40aa-901e-6801f4a95084",
  "isSidechain": false,
  "requestId": "req_011CauS2x83ew6tCmwW1MH6n",
  "type": "assistant",
  "uuid": "b33608ab-60a0-49c0-ae4a-6ab41a60c9bc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c9f1e88d-7547-445a-bdb2-8a60925de079",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Rpo5if3EZAWgbYTxGXDkP8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4528,
      "cache_read_input_tokens": 38653,
      "output_tokens": 866,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4528,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 866,
          "cache_read_input_tokens": 38653,
          "cache_creation_input_tokens": 4528,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4528
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

_source line 34 · 2026-05-10T19:22:33.966Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01Rfi49KCKts3jjjwKrATiNz`</summary>

```json
{
  "subagent_type": "Explore",
  "description": "Search active learning feasibility",
  "prompt": "I need to search for work that combines active learning with feasibility prediction for robot task/skill composition. Please use WebSearch for:\n\n1. \"active learning\" \"feasibility\" robot task generation 2024 2025 2026\n2. \"active learning\" skill composition robot \"sample efficiency\" \n3. \"uncertainty-guided\" task generation robot simulation\n4. \"GNN\" \"feasibility\" robot skill 2024 2025\n\nAlso search for: \"context-free grammar\" robot task specification 2024 2025 2026 - has anyone used formal grammars for robot task generation before?\n\nReport all relevant findings."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b33608ab-60a0-49c0-ae4a-6ab41a60c9bc",
  "isSidechain": false,
  "requestId": "req_011CauS2x83ew6tCmwW1MH6n",
  "type": "assistant",
  "uuid": "ce528d0e-334e-4e64-a119-266a88cda6ee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c9f1e88d-7547-445a-bdb2-8a60925de079",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Rpo5if3EZAWgbYTxGXDkP8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4528,
      "cache_read_input_tokens": 38653,
      "output_tokens": 866,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4528,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 866,
          "cache_read_input_tokens": 38653,
          "cache_creation_input_tokens": 4528,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4528
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

_source line 35 · 2026-05-10T19:22:40.437Z_

<details open><summary>🔧 Tool call — Agent · `toolu_016bdo5xsVfKTKQYnGSn61Hx`</summary>

```json
{
  "subagent_type": "Explore",
  "description": "Verify compute budget realism",
  "prompt": "I need to verify whether 200 H100-hours is realistic for a project that involves:\n- Running ~1000 Isaac Lab simulation rollouts with 4096 parallel environments on Unitree G1\n- Training a small GNN (3 layers, 128-dim) with active learning (~10 iterations)\n- Training a diffusion policy (ACT architecture) on generated humanoid data\n- Running 7 baseline comparisons + 3 ablation studies\n\nPlease use WebSearch to find:\n1. \"Isaac Lab\" humanoid training GPU hours H100 - how many GPU hours do typical Isaac Lab humanoid RL experiments take?\n2. \"diffusion policy\" training compute hours GPU - how long does training ACT/diffusion policy take?\n3. \"AGILE\" Isaac Lab training time GPU - what compute does the AGILE pipeline require?\n4. \"4096 parallel environments\" Isaac Lab H100 throughput\n\nReport typical compute requirements for these components."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ce528d0e-334e-4e64-a119-266a88cda6ee",
  "isSidechain": false,
  "requestId": "req_011CauS2x83ew6tCmwW1MH6n",
  "type": "assistant",
  "uuid": "e9b29d47-3795-4e30-b2fc-80f444e35496",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c9f1e88d-7547-445a-bdb2-8a60925de079",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Rpo5if3EZAWgbYTxGXDkP8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4528,
      "cache_read_input_tokens": 38653,
      "output_tokens": 866,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4528,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 866,
          "cache_read_input_tokens": 38653,
          "cache_creation_input_tokens": 4528,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4528
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

_source line 36 · 2026-05-10T19:23:03.523Z_

<details><summary>↩ Tool result · `toolu_016bdo5xsVfKTKQYnGSn61Hx`</summary>

```text
## Summary of GPU Compute Requirements

Based on the search results, here's an assessment of your 200 H100-hour budget:

### Component Breakdowns:

**1. Isaac Lab Simulation Rollouts (1000 rollouts, 4096 parallel envs)**
- Isaac Lab achieves "orders-of-magnitude higher throughput than CPU-based simulators" on a single H100
- A policy requiring 10 million environment steps can train "overnight rather than over months"
- 4096 environments is a standard configuration for GPU saturation on high-end GPUs
- **Estimate**: 1000 rollouts with 4096 parallel environments on H100 is likely **5-20 H100-hours** (depending on episode length and simulator complexity for Unitree G1)

**2. GNN Training (3 layers, 128-dim, ~10 iterations)**
- This is a small neural network with active learning
- **Estimate**: **1-5 H100-hours** (small models train very quickly; active learning loops add modest overhead)

**3. Diffusion Policy / ACT Training**
- ACT policy training takes "a few hours on one GPU" for ~100k steps
- RTX 3090/4090 can train on 200-episode datasets in 4-12 hours
- H100 is significantly more capable than 3090/4090
- **Estimate**: **2-8 H100-hours** per training run

**4. Baseline Comparisons (7) + Ablations (3)**
- 10 total experimental configurations
- Each likely requires similar compute to the main diffusion policy training
- **Estimate**: **20-80 H100-hours** (2-8 hours × 10 configurations)

### Total Budget Assessment:

**Conservative estimate: 28-113 H100-hours**
**200 H100-hours provides: 1.8-7x safety margin**

**Verdict: 200 H100-hours appears REALISTIC and provides comfortable headroom** for:
- Re-runs if experiments fail
- Hyperparameter tuning iterations
- Extended ablation studies
- Policy refinement iterations
- Unexpected longer training times

The main uncertainty is the exact scale of your simulation rollouts (episode length, environment complexity for Unitree G1), but even with pessimistic assumptions, you should have sufficient budget.

---

Sources:
- [Isaac Lab: A GPU-Accelerated Simulation Framework for Multi-Modal Robot Learning](https://arxiv.org/html/2511.04831v1)
- [Performance Benchmarks — Isaac Lab Documentation](https://isaac-sim.github.io/IsaacLab/main/source/overview/reinforcement-learning/performance_benchmarks.html)
- [Diffusion Policy for Robot Learning: What It Is and How to Use It](https://www.roboticscenter.ai/blog/diffusion-policy-robots)
- [3D Diffusion Policy](https://arxiv.org/html/2403.03954v1)
- [GPU-Accelerated Robotic Simulation Training with NVIDIA Isaac Lab in VAMS](https://aws.amazon.com/blogs/spatial/gpu-accelerated-robotic-simulation-training-with-nvidia-isaac-lab-in-vams/)
- [Multi-GPU and Multi-Node Training — Isaac Lab Documentation](https://isaac-sim.github.io/IsaacLab/main/source/features/multi_gpu.html)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e9b29d47-3795-4e30-b2fc-80f444e35496",
  "isSidechain": false,
  "promptId": "9b9ebae5-ea89-443c-82ad-9f786b68d79f",
  "type": "user",
  "uuid": "bc398148-2e57-4365-9c34-70e09fa0a5c1",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to verify whether 200 H100-hours is realistic for a project that involves:\n- Running ~1000 Isaac Lab simulation rollouts with 4096 parallel environments on Unitree G1\n- Training a small GNN (3 layers, 128-dim) with active learning (~10 iterations)\n- Training a diffusion policy (ACT architecture) on generated humanoid data\n- Running 7 baseline comparisons + 3 ablation studies\n\nPlease use WebSearch to find:\n1. \"Isaac Lab\" humanoid training GPU hours H100 - how many GPU hours do typical Isaac Lab humanoid RL experiments take?\n2. \"diffusion policy\" training compute hours GPU - how long does training ACT/diffusion policy take?\n3. \"AGILE\" Isaac Lab training time GPU - what compute does the AGILE pipeline require?\n4. \"4096 parallel environments\" Isaac Lab H100 throughput\n\nReport typical compute requirements for these components.",
    "agentId": "a623de3082dab6d05",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "## Summary of GPU Compute Requirements\n\nBased on the search results, here's an assessment of your 200 H100-hour budget:\n\n### Component Breakdowns:\n\n**1. Isaac Lab Simulation Rollouts (1000 rollouts, 4096 parallel envs)**\n- Isaac Lab achieves \"orders-of-magnitude higher throughput than CPU-based simulators\" on a single H100\n- A policy requiring 10 million environment steps can train \"overnight rather than over months\"\n- 4096 environments is a standard configuration for GPU saturation on high-end GPUs\n- **Estimate**: 1000 rollouts with 4096 parallel environments on H100 is likely **5-20 H100-hours** (depending on episode length and simulator complexity for Unitree G1)\n\n**2. GNN Training (3 layers, 128-dim, ~10 iterations)**\n- This is a small neural network with active learning\n- **Estimate**: **1-5 H100-hours** (small models train very quickly; active learning loops add modest overhead)\n\n**3. Diffusion Policy / ACT Training**\n- ACT policy training takes \"a few hours on one GPU\" for ~100k steps\n- RTX 3090/4090 can train on 200-episode datasets in 4-12 hours\n- H100 is significantly more capable than 3090/4090\n- **Estimate**: **2-8 H100-hours** per training run\n\n**4. Baseline Comparisons (7) + Ablations (3)**\n- 10 total experimental configurations\n- Each likely requires similar compute to the main diffusion policy training\n- **Estimate**: **20-80 H100-hours** (2-8 hours × 10 configurations)\n\n### Total Budget Assessment:\n\n**Conservative estimate: 28-113 H100-hours**\n**200 H100-hours provides: 1.8-7x safety margin**\n\n**Verdict: 200 H100-hours appears REALISTIC and provides comfortable headroom** for:\n- Re-runs if experiments fail\n- Hyperparameter tuning iterations\n- Extended ablation studies\n- Policy refinement iterations\n- Unexpected longer training times\n\nThe main uncertainty is the exact scale of your simulation rollouts (episode length, environment complexity for Unitree G1), but even with pessimistic assumptions, you should have sufficient budget.\n\n---\n\nSources:\n- [Isaac Lab: A GPU-Accelerated Simulation Framework for Multi-Modal Robot Learning](https://arxiv.org/html/2511.04831v1)\n- [Performance Benchmarks — Isaac Lab Documentation](https://isaac-sim.github.io/IsaacLab/main/source/overview/reinforcement-learning/performance_benchmarks.html)\n- [Diffusion Policy for Robot Learning: What It Is and How to Use It](https://www.roboticscenter.ai/blog/diffusion-policy-robots)\n- [3D Diffusion Policy](https://arxiv.org/html/2403.03954v1)\n- [GPU-Accelerated Robotic Simulation Training with NVIDIA Isaac Lab in VAMS](https://aws.amazon.com/blogs/spatial/gpu-accelerated-robotic-simulation-training-with-nvidia-isaac-lab-in-vams/)\n- [Multi-GPU and Multi-Node Training — Isaac Lab Documentation](https://isaac-sim.github.io/IsaacLab/main/source/features/multi_gpu.html)"
      }
    ],
    "totalDurationMs": 23083,
    "totalTokens": 19586,
    "totalToolUseCount": 4,
    "usage": {
      "input_tokens": 2579,
      "cache_creation_input_tokens": 1908,
      "cache_read_input_tokens": 14288,
      "output_tokens": 811,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1908
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2579,
          "output_tokens": 811,
          "cache_read_input_tokens": 14288,
          "cache_creation_input_tokens": 1908,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1908,
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
  "sourceToolAssistantUUID": "e9b29d47-3795-4e30-b2fc-80f444e35496",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c9f1e88d-7547-445a-bdb2-8a60925de079",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 37_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-10 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "bc398148-2e57-4365-9c34-70e09fa0a5c1",
  "sessionId": "c9f1e88d-7547-445a-bdb2-8a60925de079"
}
```

---

### Runtime record

_source line 38_

```json
{
  "type": "ai-title",
  "aiTitle": "Verify CompLocoGen novelty and feasibility for humanoid loco-manipulation task generation",
  "sessionId": "c9f1e88d-7547-445a-bdb2-8a60925de079"
}
```

---

### Tool result

_source line 39 · 2026-05-10T19:23:05.709Z_

<details><summary>↩ Tool result · `toolu_01Rfi49KCKts3jjjwKrATiNz`</summary>

```text
## Summary of Search Findings

Based on my comprehensive web search, here are the key findings organized by topic:

### 1. Active Learning + Feasibility for Robot Task Generation (2024-2026)

**Major Advances:**
- **Sample-Efficient Learning**: A robotic arm successfully learned 1,000 manipulation tasks in under 24 hours using only a single demonstration per task, combining trajectory decomposition and retrieval-based generalization
- **Embodied LLM Approach (ELLMER)**: Framework utilizing GPT-4 and retrieval-augmented generation enables robots to complete long-horizon tasks in unpredictable environments by extracting contextually relevant examples and producing action plans with force and visual feedback
- **Interactive Task Learning**: Research assesses system feasibility for novice users to intuitively personalize robot skills without technical knowledge in domestic environments

### 2. Active Learning + Skill Composition + Sample Efficiency

**Key Research:**
- **MUSEL (Model Uncertainty for Sample-Efficient Learning)**: Novel active learning framework that combines total predictive uncertainty, learning progress, and input diversity to guide data acquisition for self-supervised robot learning
- **Autonomous Robotic Playing with Active Learning**: Robots use environment models learned during autonomous play for active learning and compositional generation of novel preparatory behaviors
- **Graph-Based Skill Composition (GSC)**: First framework to model a whole skill set as a graph and learn skill embeddings with GNNs, enabling more efficient integration of previously learned knowledge
- **Hierarchical RL for Construction Tasks**: Benchmarking of hierarchical reinforcement learning and vision-language-action models for sample-efficient task learning

### 3. Uncertainty-Guided Task Generation

**Relevant Approaches:**
- **Uncertainty-Aware Robotic World Model (RWM-U)**: Extends autoregressive world models with epistemic uncertainty estimation, enabling temporally consistent multi-step rollouts with uncertainty propagated over long horizons. Uses ensemble-based uncertainty to quantify epistemic uncertainty from limited offline data, penalizing high-risk imagined transitions during policy learning
- **Task-Specific Uncertainty Management (GUIDE)**: Creates Task-Specific Uncertainty Maps (TSUMs) that represent acceptable uncertainty levels across regions, enabling policies to adapt behavior based on specific uncertainty requirements

### 4. GNN + Feasibility for Robot Skills (2024-2025)

**GNN Applications:**
- GNNs widely used for modeling particle interactions where particles are nodes and features include physical parameters, motion, and displacement
- Lightweight architectures (MLPs, graph-based models) capture keypoint dynamics with generalization across object instances
- Enabling fast inference, real-time planning, and feedback control

**2025 Context:**
- Breakthroughs in 3D perception, control, skill planning enabled by generative AI
- 2025 International Humanoid Robot Skills Competition showcases transition from lab to real-life applications

### 5. Context-Free Grammar for Robot Task Specification

**Findings:**
- **ProgPrompt**: Program generation for situated robot task planning using large language models (published in Autonomous Robots, Springer Nature)
- **SELP (Safe and Efficient Task Plans)**: Published at ICRA 2025, focuses on generating safe and efficient task plans for robot agents
- **Grammar Learning in LLMs**: Research shows transformers can learn context-free grammars, with comprehensive understanding of how GPT-like models capture CFG structure and rules
- **LLM-Based Planning at RoboCup 2024**: System deployed in Eindhoven secured second place in GPSR (General Purpose Service Robot) task using formal planning approaches

**Formal Grammar Use Cases**: While direct formal grammar specification for robot tasks exists (ProgPrompt framework), the research more commonly employs LLMs to generate task programs rather than hand-crafted formal grammars. However, the grammar learning research suggests these models understand and can work with formal specifications.

---

### Primary Sources:
- [Task cognition and planning for service robots](https://www.oaepublish.com/articles/ir.2025.08)
- [Sample-Efficient Robot Skill Learning for Construction Tasks](https://arxiv.org/pdf/2512.14031)
- [Skill Learning by Autonomous Robotic Playing Using Active Learning](https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2020.00042/full)
- [GSC: Graph-based Skill Composition Framework](https://www.sciencedirect.com/science/article/abs/pii/S0921889024001714)
- [Uncertainty-Aware Robotic World Model](https://arxiv.org/abs/2504.16680)
- [Enhancing Robot Navigation Policies with Task-Specific Uncertainty Management](https://arxiv.org/html/2410.15178v2)
- [ProgPrompt: Program generation for robot task planning](https://link.springer.com/article/10.1007/s10514-023-10135-3)
- [SELP: Safe and Efficient Task Plans for Robot Agents](https://cs.purdue.edu/homes/lintan/publications/selp-icra25.pdf)
- [How Language Models Learn Context-Free Grammars](https://openreview.net/forum?id=qnbLGV9oFL)
- [Embodied LLMs for Robot Tasks](https://www.nature.com/articles/s42256-025-01005-x)
- [Robot Learning in the Era of Foundation Models](https://www.sciencedirect.com/science/article/abs/pii/S0925231225006356)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ce528d0e-334e-4e64-a119-266a88cda6ee",
  "isSidechain": false,
  "promptId": "9b9ebae5-ea89-443c-82ad-9f786b68d79f",
  "type": "user",
  "uuid": "6d27ba87-e4b8-4a6e-9b29-7450eb46f5e0",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to search for work that combines active learning with feasibility prediction for robot task/skill composition. Please use WebSearch for:\n\n1. \"active learning\" \"feasibility\" robot task generation 2024 2025 2026\n2. \"active learning\" skill composition robot \"sample efficiency\" \n3. \"uncertainty-guided\" task generation robot simulation\n4. \"GNN\" \"feasibility\" robot skill 2024 2025\n\nAlso search for: \"context-free grammar\" robot task specification 2024 2025 2026 - has anyone used formal grammars for robot task generation before?\n\nReport all relevant findings.",
    "agentId": "a4c0e896cd5d7e090",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "## Summary of Search Findings\n\nBased on my comprehensive web search, here are the key findings organized by topic:\n\n### 1. Active Learning + Feasibility for Robot Task Generation (2024-2026)\n\n**Major Advances:**\n- **Sample-Efficient Learning**: A robotic arm successfully learned 1,000 manipulation tasks in under 24 hours using only a single demonstration per task, combining trajectory decomposition and retrieval-based generalization\n- **Embodied LLM Approach (ELLMER)**: Framework utilizing GPT-4 and retrieval-augmented generation enables robots to complete long-horizon tasks in unpredictable environments by extracting contextually relevant examples and producing action plans with force and visual feedback\n- **Interactive Task Learning**: Research assesses system feasibility for novice users to intuitively personalize robot skills without technical knowledge in domestic environments\n\n### 2. Active Learning + Skill Composition + Sample Efficiency\n\n**Key Research:**\n- **MUSEL (Model Uncertainty for Sample-Efficient Learning)**: Novel active learning framework that combines total predictive uncertainty, learning progress, and input diversity to guide data acquisition for self-supervised robot learning\n- **Autonomous Robotic Playing with Active Learning**: Robots use environment models learned during autonomous play for active learning and compositional generation of novel preparatory behaviors\n- **Graph-Based Skill Composition (GSC)**: First framework to model a whole skill set as a graph and learn skill embeddings with GNNs, enabling more efficient integration of previously learned knowledge\n- **Hierarchical RL for Construction Tasks**: Benchmarking of hierarchical reinforcement learning and vision-language-action models for sample-efficient task learning\n\n### 3. Uncertainty-Guided Task Generation\n\n**Relevant Approaches:**\n- **Uncertainty-Aware Robotic World Model (RWM-U)**: Extends autoregressive world models with epistemic uncertainty estimation, enabling temporally consistent multi-step rollouts with uncertainty propagated over long horizons. Uses ensemble-based uncertainty to quantify epistemic uncertainty from limited offline data, penalizing high-risk imagined transitions during policy learning\n- **Task-Specific Uncertainty Management (GUIDE)**: Creates Task-Specific Uncertainty Maps (TSUMs) that represent acceptable uncertainty levels across regions, enabling policies to adapt behavior based on specific uncertainty requirements\n\n### 4. GNN + Feasibility for Robot Skills (2024-2025)\n\n**GNN Applications:**\n- GNNs widely used for modeling particle interactions where particles are nodes and features include physical parameters, motion, and displacement\n- Lightweight architectures (MLPs, graph-based models) capture keypoint dynamics with generalization across object instances\n- Enabling fast inference, real-time planning, and feedback control\n\n**2025 Context:**\n- Breakthroughs in 3D perception, control, skill planning enabled by generative AI\n- 2025 International Humanoid Robot Skills Competition showcases transition from lab to real-life applications\n\n### 5. Context-Free Grammar for Robot Task Specification\n\n**Findings:**\n- **ProgPrompt**: Program generation for situated robot task planning using large language models (published in Autonomous Robots, Springer Nature)\n- **SELP (Safe and Efficient Task Plans)**: Published at ICRA 2025, focuses on generating safe and efficient task plans for robot agents\n- **Grammar Learning in LLMs**: Research shows transformers can learn context-free grammars, with comprehensive understanding of how GPT-like models capture CFG structure and rules\n- **LLM-Based Planning at RoboCup 2024**: System deployed in Eindhoven secured second place in GPSR (General Purpose Service Robot) task using formal planning approaches\n\n**Formal Grammar Use Cases**: While direct formal grammar specification for robot tasks exists (ProgPrompt framework), the research more commonly employs LLMs to generate task programs rather than hand-crafted formal grammars. However, the grammar learning research suggests these models understand and can work with formal specifications.\n\n---\n\n### Primary Sources:\n- [Task cognition and planning for service robots](https://www.oaepublish.com/articles/ir.2025.08)\n- [Sample-Efficient Robot Skill Learning for Construction Tasks](https://arxiv.org/pdf/2512.14031)\n- [Skill Learning by Autonomous Robotic Playing Using Active Learning](https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2020.00042/full)\n- [GSC: Graph-based Skill Composition Framework](https://www.sciencedirect.com/science/article/abs/pii/S0921889024001714)\n- [Uncertainty-Aware Robotic World Model](https://arxiv.org/abs/2504.16680)\n- [Enhancing Robot Navigation Policies with Task-Specific Uncertainty Management](https://arxiv.org/html/2410.15178v2)\n- [ProgPrompt: Program generation for robot task planning](https://link.springer.com/article/10.1007/s10514-023-10135-3)\n- [SELP: Safe and Efficient Task Plans for Robot Agents](https://cs.purdue.edu/homes/lintan/publications/selp-icra25.pdf)\n- [How Language Models Learn Context-Free Grammars](https://openreview.net/forum?id=qnbLGV9oFL)\n- [Embodied LLMs for Robot Tasks](https://www.nature.com/articles/s42256-025-01005-x)\n- [Robot Learning in the Era of Foundation Models](https://www.sciencedirect.com/science/article/abs/pii/S0925231225006356)"
      }
    ],
    "totalDurationMs": 31741,
    "totalTokens": 21199,
    "totalToolUseCount": 5,
    "usage": {
      "input_tokens": 907,
      "cache_creation_input_tokens": 4759,
      "cache_read_input_tokens": 14211,
      "output_tokens": 1322,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4759
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 907,
          "output_tokens": 1322,
          "cache_read_input_tokens": 14211,
          "cache_creation_input_tokens": 4759,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4759,
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
  "sourceToolAssistantUUID": "ce528d0e-334e-4e64-a119-266a88cda6ee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c9f1e88d-7547-445a-bdb2-8a60925de079",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-10T19:23:19.343Z_

<details><summary>↩ Tool result · `toolu_01DTsF3kGMo7xuP2H2Vke3qB`</summary>

```text
Perfect! Now I have comprehensive information. Let me provide you with a detailed analysis structured around your critical questions.

## RoboGene Deep Dive Summary

Based on the arXiv paper and HTML version, here are the answers to your five critical questions:

### 1. **Compositional vs. Single Tasks**
RoboGene generates **multi-stage compositional tasks** with hierarchical structure. The paper explicitly demonstrates this with mobile manipulation tasks showing four sequential steps (pick, identify, navigate, place)—not single primitives. This is significant for your work.

### 2. **Feasibility Prediction Mechanism**
RoboGene uses **LLM-based self-reflection with three independent evaluators**:
- **Physical Feasibility Evaluator**: Analyzes kinematic feasibility, workspace overlap, physics compliance
- **Novelty Evaluator**: Four-dimensional complexity assessment
- **Constraint Adherence Evaluator**: Prevents hallucination of non-existent objects/skills

Crucially, feasibility is **not a learned predictor model** but rather **rule-based + LLM reasoning**. The evaluators produce natural language critiques fed to a "Self-Reflection Refiner" that synthesizes feedback into refined tasks. This is a critical difference from your proposed GNN transition feasibility network approach.

### 3. **Robot Specificity**
RoboGene is **NOT humanoid-specific**—it targets **single-arm, dual-arm, and mobile robots**. More general than your potential humanoid focus.

### 4. **Scale of Generation**
- **18,000 trajectories** collected in large-scale real-world experiments
- **900 tasks** were evaluated for quality metrics
- **719 unique objects** covered
- **118 distinct skills** with balanced distribution
This is substantial real-world validation, not just synthetic generation.

### 5. **Physical Feasibility Handling**
Three complementary mechanisms:
1. **Diversity-Driven Sampling (LFU Strategy)**: Least Frequently Used counters for scenarios, objects, skills—actively guides generation toward underexplored task space
2. **Self-Reflection Refinement**: LLM evaluators iteratively improve tasks based on feasibility critiques
3. **Human-in-the-Loop (HITL) Continuous Learning**: RAG-based memory consolidating real-world execution feedback, storing heuristic guidelines as semantic key-value pairs, retrieved via cosine similarity

---

## Novelty Assessment: Grammar + GNN vs. RoboGene

Your approach offers **genuine and substantial novelty**:

| Aspect | RoboGene | Your Proposal |
|--------|----------|---------------|
| **Feasibility Mechanism** | LLM evaluators + rule-based reasoning | Learned GNN transition model |
| **Task Structure** | Free-form LLM generation guided by diversity sampling | Grammar-based compositional generation |
| **Scalability** | LLM-dependent (cost, latency) | Grammar + learned model (scalable) |
| **Generalization** | Limited to observed task distributions | Grammar enables structural generalization |
| **Physics Modeling** | Heuristic + LLM judgment | Explicit transition feasibility network |

The key distinction: RoboGene is **diversity-driven LLM synthesis with post-hoc feasibility fixing**, while your approach is **grammar-constrained generation with learned feasibility prediction**. These are fundamentally different paradigms, not just incremental improvements.

---

Sources:
- [RoboGene arXiv Abstract](https://arxiv.org/abs/2602.16444)
- [RoboGene HTML Version](https://arxiv.org/html/2602.16444)
- [RoboGene Abstract v2](https://arxiv.org/abs/2602.16444v2)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b33608ab-60a0-49c0-ae4a-6ab41a60c9bc",
  "isSidechain": false,
  "promptId": "9b9ebae5-ea89-443c-82ad-9f786b68d79f",
  "type": "user",
  "uuid": "5a455b67-636e-481b-8340-5a6f837e6414",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to deeply understand \"RoboGene: Boosting VLA Pre-training via Diversity-Driven Agentic Framework for Real-World Task Generation\" (arXiv:2602.16444, Feb 2026). This may be a critical competing work for a proposal about grammar-based compositional task generation with learned feasibility.\n\nPlease use WebFetch to read the abstract and details at https://arxiv.org/abs/2602.16444\n\nI need to understand:\n1. Does RoboGene generate compositional multi-stage tasks or single tasks?\n2. Does it have any feasibility prediction mechanism?\n3. Does it target humanoid robots specifically?\n4. What's its scale of generation (number of tasks, trajectories)?\n5. How does it handle physical feasibility?\n\nThis is crucial for assessing whether a \"grammar + GNN transition feasibility network\" approach offers genuine novelty over RoboGene.",
    "agentId": "af1f1fd1e2927832d",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Perfect! Now I have comprehensive information. Let me provide you with a detailed analysis structured around your critical questions.\n\n## RoboGene Deep Dive Summary\n\nBased on the arXiv paper and HTML version, here are the answers to your five critical questions:\n\n### 1. **Compositional vs. Single Tasks**\nRoboGene generates **multi-stage compositional tasks** with hierarchical structure. The paper explicitly demonstrates this with mobile manipulation tasks showing four sequential steps (pick, identify, navigate, place)—not single primitives. This is significant for your work.\n\n### 2. **Feasibility Prediction Mechanism**\nRoboGene uses **LLM-based self-reflection with three independent evaluators**:\n- **Physical Feasibility Evaluator**: Analyzes kinematic feasibility, workspace overlap, physics compliance\n- **Novelty Evaluator**: Four-dimensional complexity assessment\n- **Constraint Adherence Evaluator**: Prevents hallucination of non-existent objects/skills\n\nCrucially, feasibility is **not a learned predictor model** but rather **rule-based + LLM reasoning**. The evaluators produce natural language critiques fed to a \"Self-Reflection Refiner\" that synthesizes feedback into refined tasks. This is a critical difference from your proposed GNN transition feasibility network approach.\n\n### 3. **Robot Specificity**\nRoboGene is **NOT humanoid-specific**—it targets **single-arm, dual-arm, and mobile robots**. More general than your potential humanoid focus.\n\n### 4. **Scale of Generation**\n- **18,000 trajectories** collected in large-scale real-world experiments\n- **900 tasks** were evaluated for quality metrics\n- **719 unique objects** covered\n- **118 distinct skills** with balanced distribution\nThis is substantial real-world validation, not just synthetic generation.\n\n### 5. **Physical Feasibility Handling**\nThree complementary mechanisms:\n1. **Diversity-Driven Sampling (LFU Strategy)**: Least Frequently Used counters for scenarios, objects, skills—actively guides generation toward underexplored task space\n2. **Self-Reflection Refinement**: LLM evaluators iteratively improve tasks based on feasibility critiques\n3. **Human-in-the-Loop (HITL) Continuous Learning**: RAG-based memory consolidating real-world execution feedback, storing heuristic guidelines as semantic key-value pairs, retrieved via cosine similarity\n\n---\n\n## Novelty Assessment: Grammar + GNN vs. RoboGene\n\nYour approach offers **genuine and substantial novelty**:\n\n| Aspect | RoboGene | Your Proposal |\n|--------|----------|---------------|\n| **Feasibility Mechanism** | LLM evaluators + rule-based reasoning | Learned GNN transition model |\n| **Task Structure** | Free-form LLM generation guided by diversity sampling | Grammar-based compositional generation |\n| **Scalability** | LLM-dependent (cost, latency) | Grammar + learned model (scalable) |\n| **Generalization** | Limited to observed task distributions | Grammar enables structural generalization |\n| **Physics Modeling** | Heuristic + LLM judgment | Explicit transition feasibility network |\n\nThe key distinction: RoboGene is **diversity-driven LLM synthesis with post-hoc feasibility fixing**, while your approach is **grammar-constrained generation with learned feasibility prediction**. These are fundamentally different paradigms, not just incremental improvements.\n\n---\n\nSources:\n- [RoboGene arXiv Abstract](https://arxiv.org/abs/2602.16444)\n- [RoboGene HTML Version](https://arxiv.org/html/2602.16444)\n- [RoboGene Abstract v2](https://arxiv.org/abs/2602.16444v2)"
      }
    ],
    "totalDurationMs": 49900,
    "totalTokens": 19985,
    "totalToolUseCount": 6,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 792,
      "cache_read_input_tokens": 18295,
      "output_tokens": 895,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 792
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 895,
          "cache_read_input_tokens": 18295,
          "cache_creation_input_tokens": 792,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 792,
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
      "otherToolCount": 6
    }
  },
  "sourceToolAssistantUUID": "b33608ab-60a0-49c0-ae4a-6ab41a60c9bc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c9f1e88d-7547-445a-bdb2-8a60925de079",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 41 · 2026-05-10T19:25:05.893Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me synthesize all my findings and form a judgment. Let me go through the review checklist carefully:

## 1. SOTA Freshness
The proposal cites current work well: Eurekaverse (CoRL 2024), VIRAL (CVPR 2026), DemoHLM, AGILE (March 2026), STRIDE, FORGE, Genie Sim 3.0, LHM-Humanoid, etc. These are all verified as real and correctly described.

## 2. Reference Verification
All key references I checked exist:


- Eurekaverse ✓ (CoRL 2024)
- VIRAL ✓ (CVPR 2026)
- DemoHLM ✓
- AGILE ✓ (arXiv:2603.20147)
- SCaR ✓ (NeurIPS 2024)
- Generative Skill Chaining ✓ (though it's CoRL 2023, not 2024 as cited—a minor discrepancy)
- SuperDyno ✓ (ICLR 2025 Workshop)
- Humanoid Hanoi ✓
- FALCON ✓
- LHM-Humanoid ✓
- GR00T-WBC/SONIC ✓

Now I'm checking the gap claim about combining grammar-structured compositional task generation with learned transition feasibility prediction for humanoid loco-manipulation. Looking at related work, FATE handles feasibility-aware generation but relies on VLM validation rather than learned predictors and doesn't target humanoid compositional tasks, while RoboGene uses LLM-based feasibility evaluation without the GNN predictor component and isn't humanoid-specific. Generative Skill Chaining and GSC both work with learned skill composition and GNN-based skill graphs, but they're limited to fixed-base manipulation, and SCaR learns transition success predictors only in that same fixed-base setting.

The specific combination of grammar-based generation, learned GNN feasibility prediction, and humanoid loco-manipulation does appear to be novel.

For venue deadlines, CoRL 2026 checks out with the abstract due May 26 and paper May 29. But there's a timing issue with Humanoids 2026—the proposal claims June 30 as the deadline, though my search indicates it's actually July 24, which actually gives more runway than stated, making the timeline more feasible than originally presented.

On feasibility, the compute requirements look solid with 200 H100-hours being conservative relative to the 28-113 hour estimate, and the 51-75 day window is workable for this scope. All the key dependencies—SONIC/GR00T-WBC checkpoints, AGILE framework, and Isaac Lab—are already available.

The main novelty hinges on the Transition Feasibility Network: a GNN architecture specifically designed to predict whether skill transitions will succeed, paired with an active learning loop that targets high-uncertainty transitions for generation. This combination of feasibility learning with uncertainty-guided generation appears to be the distinguishing contribution.

Compared to related work like RoboGene (which uses LLM-based feasibility evaluation), Generative Skill Chaining (which focuses on fixed-base trajectory generation), and FATE (which handles single tasks with VLMs), the approach of applying learned feasibility prediction to humanoid loco-manipulation with coupled dynamics fills a meaningful gap.

The key algorithmic contribution is using a GNN to learn transition boundary dynamics, which exploits compositional structure to bring sample complexity down from exponential to quadratic — that's a solid insight.

Looking at the cost breakdown across the three modes, the numbers are internally consistent: manual and HIL both run around 180-200 GPU hours over 6-8 weeks, while the automated approach compresses that to 3-4 weeks with higher utilization. The budget allocations make sense relative to the computational demands of each approach.

But there's a critical mismatch with the user's timeline — they're targeting CoRL 2026 with a May 29 paper deadline, which is only 17-20 days away, yet the proposal is built around Humanoids 2026 in July as the primary venue. There's also a citation error where Generative Skill Chaining is attributed to CoRL 2024 when it's actually from 2023. More importantly, the proposal misses two directly relevant competing works: RoboGene, which uses LLMs for diverse task generation with feasibility checking, and FATE, which appears to address similar automated task generation problems. The proposal references "Qwen 3.6-35B-A3B" as the LLM backbone, but I'm uncertain whether this model actually exists. Qwen released version 3 around April/May 2025, so a 3.6 variant might plausibly exist by May 2026, and the "35B-A3B" notation could indicate a Mixture of Experts architecture with 35B total parameters and 3B active—which aligns with Qwen's actual model releases. I should verify whether this is a real model or a hallucination before flagging it as an error.

Looking at the overall assessment, the proposal has genuine strengths: the TFN is a novel contribution that addresses prior reviewer feedback, the gap analysis is thorough with solid landscape coverage, the compute budget is realistic and well-justified, and the quadratic-versus-exponential sample complexity argument is compelling. The active learning loop is well-motivated, the baseline set is strong with seven baselines plus three ablations, and building on existing AGILE/SONIC infrastructure reduces engineering risk. However, there's a primary venue mismatch issue that needs addressing.

The main weakness is that the user wants CoRL 2026 with only 20 days remaining, but the proposal targets Humanoids 2026 which has 75 days—this is a fundamental requirement violation. Additionally, the work is missing citations to RoboGene, FATE, and Ψ₀ as competing or related approaches, and some claims about TFN generalization from 20-30 rollouts lack substantiation.

For novelty, I'm rating this around 3.5 out of 5. The TFN combined with grammar-based generation is novel, but the overall pipeline—LLM to grammar to execution to filtering—follows established patterns from RoboGen, GenManip, and Eurekaverse. The core novelty of learning transition feasibility with a GNN that exploits compositional structure is a solid incremental contribution rather than a fundamental paradigm shift, and the missing citations further weaken the novelty positioning.

Actually, reconsidering this: the TFN's specific insight about how compositional structure lets you learn O(P²) transition types instead of exponential task-level feasibility is genuinely clever and novel. The active learning approach on transition uncertainty is also original. For a systems and algorithms paper targeting Humanoids, this is strong work, though it might be borderline for CoRL.

The feasibility rating is also 3.5 out of 5. The compute budget checks out and the infrastructure exists through SONIC, AGILE, and Isaac Lab, but the timeline is the critical issue—20 days for CoRL is infeasible for this scope even with pre-trained components, whereas the 75-day Humanoids timeline is more realistic.

On clarity, I'd rate this 4 out of 5. The proposal is well-structured with a clearly articulated TFN contribution, comprehensive baselines, and thoughtfully designed ablations. The grammar specification is detailed, though the overall description could be more concise in places.

For impact, it's 3.5 out of 5. This addresses a real bottleneck in humanoid loco-manipulation task diversity, and if the TFN performs as intended, it could enable automatic scaling of training environments. But the practical impact hinges on whether the generated tasks actually improve downstream policy performance—that's an open experimental question. The contribution is also somewhat narrow, tied to the Isaac Lab and AGILE ecosystem.

Averaging these scores gives 3.625, which falls short of the acceptance threshold.

The core issues holding this back are the venue mismatch—the user is targeting CoRL but the proposal is oriented toward humanoids—plus missing citations for competing work like RoboGene and FATE, and some claims that lack sufficient support. My verdict is to revise. The novelty is solid at 3.5 since TFN is novel but the pipeline itself is established, and those competing works should be cited. Feasibility is also 3.5 due to compute being manageable but the venue and timeline not aligning with what the user needs. Clarity holds at 4.0, and impact stays at 3.5. This is fixable work—the proposal has come a long way but needs these adjustments to cross the bar.

Actually, I'm noticing something important here: the user explicitly wants CoRL 2026, but the proposal targets Humanoids 2026 instead, citing that CoRL's timeline is infeasible. The previous reviewer even suggested committing to Humanoids as primary. So there's a real tension between what the user asked for and what the proposal is doing. The proposal is probably right that CoRL 2026 isn't realistic for this scope, but I should flag this conflict clearly rather than just penalizing it—the user needs to know their stated target doesn't align with what's actually achievable.

Looking at the hard constraints more carefully, the 20-day timeline is pretty binding when combined with the CoRL 2026 target. The proposal uses compute efficiently (180-200 H100-hours is within budget), but the timeline is the real problem—even the optimistic auto-research path is 3-4 weeks, and the manual approach stretches to 7-8 weeks. That's a critical mismatch. The proposal needs to either compress the scope to fit 20 days or explicitly justify why that's impossible and propose a phased approach instead.

Beyond the timeline issue, there are some significant gaps in the related work. RoboGene and FATE are both recent papers on automated task generation with feasibility checking that should be discussed. There's also Ψ₀, a humanoid foundation model for loco-manipulation that's relevant as a potential downstream application. And the claim about TFN generalization needs more substantiation—it's presented without enough evidence backing it up.

I'm also noticing some factual errors: the Humanoids deadline appears to be July 24, not June 30, and the Generative Skill Chaining citation looks like it should be CoRL 2023, not 2024.

Looking at the overall assessment, TFN is genuinely novel in how it applies GNNs to transition feasibility with better sample complexity, but the pipeline itself follows established patterns from RoboGen and Eurekaverse. The feasibility score has to reflect that the timeline fundamentally breaks the user's constraint, even though the compute budget itself is realistic.

The proposal is well-written and clearly structured, and it does tackle a real bottleneck in humanoid data scaling. The insight about compositional structure enabling efficient feasibility learning is solid. But the impact remains limited by the narrow scope within the Isaac Lab ecosystem and the unproven generalization claims.

Averaging everything out, I'm landing at 3.5/5, which falls below the 4.0 threshold. The verdict is to revise. Though I should double-check whether I'm being fair here—the proposal has actually improved substantially across multiple rounds, with the compute budget fixed and the framework refined.

Looking at what's been addressed: the compute estimates are now realistic, the framework issue is resolved, TFN is positioned as a core contribution, the related work landscape is much more comprehensive, and the baselines have expanded significantly. The grammar primitives have grown from 4 to 7, and the AGILE descriptor characterization is corrected.

The remaining gaps are concrete though: it doesn't satisfy the CoRL/20-day constraint, and there are some missing references and unsubstantiated claims. These are fixable issues, so "revise" with specific actionable feedback is the right call.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5a455b67-636e-481b-8340-5a6f837e6414",
  "isSidechain": false,
  "requestId": "req_011CauS7VBSrJBRYE5MqMegk",
  "type": "assistant",
  "uuid": "e1baec04-65bf-463f-8348-4e17b4c1104d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c9f1e88d-7547-445a-bdb2-8a60925de079",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014ZSqHN1xGMctpU2KjpoYpy",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2178,
      "cache_creation_input_tokens": 1788,
      "cache_read_input_tokens": 43181,
      "output_tokens": 6697,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1788,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2178,
          "output_tokens": 6697,
          "cache_read_input_tokens": 43181,
          "cache_creation_input_tokens": 1788,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1788
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

_source line 42 · 2026-05-10T19:25:54.404Z_

Now I have enough evidence to render a thorough judgment. Let me synthesize all findings.

**Key findings from my independent research:**

1. **TFN novelty holds up**: No existing work proposes a GNN-based transition feasibility predictor specifically for humanoid loco-manipulation skill composition. Closest are SCaR (learned success predictors, fixed-base), GSC (GNN skill graphs, no feasibility prediction), and Generative Skill Chaining (diffusion-based, fixed-base). The quadratic-vs-exponential sample complexity argument is clean.

2. **Critical missing competitors found**: RoboGene (arXiv:2602.16444, Feb 2026) and FATE (arXiv:2603.01505, March 2026) are directly relevant uncited works in automated feasibility-aware task generation.

3. **Compute budget verified as realistic**: Conservative estimates suggest 28-113 H100-hours for all components, giving 2-7x headroom within 200h.

4. **Venue deadline discrepancy**: Humanoids 2026 deadline appears to be July 24 (not June 30 as claimed), giving even more time.

5. **All key references verified as real**, with one minor citation error (Generative Skill Chaining is CoRL 2023, not 2024).

```json
{
  "verdict": "revise",
  "scores": {
    "novelty": {"score": 3.5, "rationale": "The TFN's insight—exploiting compositional structure for O(P²) transition learning instead of exponential task-level feasibility—is genuinely novel and no prior work does this for humanoid loco-manipulation. However, the overall pipeline (LLM→grammar→simulate→filter) follows established patterns (RoboGen, Eurekaverse, GenManip). Two directly relevant uncited works weaken the novelty positioning: RoboGene (arXiv:2602.16444) does automated diverse task generation with LLM-based feasibility evaluation, and FATE (arXiv:2603.01505) does feasibility-aware task generation with active repair."},
    "feasibility": {"score": 3, "rationale": "Compute budget (180-200 H100-hours) is verified realistic with comfortable headroom. SONIC/AGILE/Isaac Lab infrastructure exists and is accessible. However, the proposal fundamentally violates the user's requirements: the user targets CoRL 2026 with a 20-day hard constraint, but the proposal targets Humanoids 2026 (75 days) with a 7-8 week manual timeline. No CoRL-feasible minimal scope is presented. TFN generalization from 20-30 rollouts per novel primitive is an unsubstantiated claim."},
    "clarity": {"score": 4, "rationale": "Excellent technical clarity. The TFN architecture, training procedure (bootstrap→active learning→generalization), and the grammar specification with 7 typed primitives are well-articulated. Landscape analysis is now comprehensive with clear differentiation against 20+ related works. Baselines and ablations are well-designed and motivated."},
    "impact": {"score": 3.5, "rationale": "Addresses a genuine bottleneck—manual task specification limits diversity in humanoid loco-manipulation training. The TFN's ability to efficiently predict composition feasibility could meaningfully accelerate humanoid policy research. However, impact is somewhat ecosystem-specific (Isaac Lab/AGILE) and depends on unproven TFN generalization. The practical question—whether generated compositional tasks actually improve downstream policy performance more than simpler augmentation—remains experimental."}
  },
  "issues": [
    "CRITICAL: VENUE/TIMELINE MISMATCH WITH USER REQUIREMENTS. The user explicitly targets CoRL 2026 (abstract May 26, paper May 29, ≤20 days). The proposal abandons CoRL entirely, targeting Humanoids 2026 (July 24, 75 days) as primary with ICRA 2027 and CoRL 2027 as secondary. The manual timeline (7-8 weeks) and even auto-research timeline (3-4 weeks) exceed the user's 20-day hard constraint. The proposal must either present a CoRL-feasible minimal scope or explicitly justify why CoRL 2026 cannot be met while proposing a concrete alternative the user can accept.",
    "MISSING COMPETING WORK: RoboGene (arXiv:2602.16444, Feb 2026) generates diverse robot tasks with three LLM-based feasibility evaluators (physical, novelty, constraint adherence), diversity-driven LFU sampling, and self-reflection refinement. It produces 18K trajectories across 900 tasks. While its mechanism differs (LLM-based evaluation vs. learned GNN prediction), it directly addresses the same problem of automated diverse feasibility-aware task generation. The proposal must cite and differentiate: RoboGene uses post-hoc LLM feasibility fixing; CompLocoGen uses learned upfront prediction with compositional structure. RoboGene targets general manipulation; CompLocoGen targets humanoid loco-manipulation with coupled dynamics.",
    "MISSING COMPETING WORK: FATE (arXiv:2603.01505, March 2026) proposes closed-loop feasibility-aware task generation with active repair using VLM auditors (static + dynamic phases). While FATE targets individual tasks on mobile manipulators (not compositional humanoid tasks), it directly occupies the 'feasibility-aware task generation' space. The TFN's advantage over FATE—learned boundary dynamics vs. VLM-based auditing, compositional structure vs. single tasks—should be articulated.",
    "MISSING REFERENCE: Ψ₀ (arXiv:2603.12263, March 2026) is a foundation model for universal humanoid loco-manipulation using staged VLM pre-training on human video + robot data fine-tuning. While it's a policy model (not task generation), it represents a key potential downstream consumer of CompLocoGen's generated tasks and should be mentioned to strengthen the impact argument.",
    "TFN GENERALIZATION CLAIM UNSUBSTANTIATED: The proposal claims the TFN can generalize to novel primitive types (push, open_door, squat) from only 20-30 rollouts per new transition type, arguing that 'primitive-type-agnostic physical features (CoM velocity, contact forces, joint torques)' enable transfer. This is a strong empirical claim with no supporting evidence. While architecturally plausible, it should be framed as a key experimental hypothesis, not a design assumption. If generalization fails, the active learning budget for 7 primitives grows substantially.",
    "HUMANOIDS 2026 DEADLINE ERROR: The proposal claims 'paper deadline June 30, 2026 — 51 days' but the official Humanoids 2026 website (2026.ieee-humanoids.org) indicates the paper submission deadline is July 24, 2026 (75 days from today). This is favorable (more time) but suggests the deadline wasn't verified against the official source.",
    "MINOR: Generative Skill Chaining is cited as 'CoRL 2024' but appears to be CoRL 2023 (arXiv:2401.03360 submitted Jan 2024 but the paper was at CoRL 2023). Verify and correct."
  ],
  "feedback": "The proposal has improved substantially over 5 rounds — the TFN is a genuine novelty contribution and the compute/infrastructure are now realistic. Three targeted changes would bring this to pass quality:\n\n1. **ADDRESS CoRL 2026 OR JUSTIFY ALTERNATIVE**: The user's requirement is CoRL 2026 (20 days). You must either: (a) Present a CoRL-minimal scope: 3 primitives (walk/pick/place), pre-trained SONIC+IK, TFN with bootstrap-only training (no full active learning loop), 3 compositions, single downstream eval, no ablations — essentially demonstrating TFN feasibility prediction works. Use the Humanoids deadline for the full 7-primitive + active learning + ablation paper. OR (b) Make a compelling case that the TFN contribution requires the full evaluation to be convincing and that a stripped-down CoRL submission would be rejected anyway — then commit to Humanoids 2026 (actual deadline July 24 = 75 days, plenty of time).\n\n2. **ADD RoboGene AND FATE TO LANDSCAPE**: Both are 2026 works in automated feasibility-aware task generation. Your differentiation is clear and strong: (a) vs. RoboGene: learned GNN prediction vs. LLM-based evaluation; compositional grammar structure vs. free-form LLM generation; humanoid-specific coupled dynamics vs. general manipulation. (b) vs. FATE: upfront composition-level prediction vs. per-task post-hoc VLM auditing; compositional multi-stage tasks vs. single tasks; humanoid loco-manipulation vs. mobile manipulation. Frame RoboGene as a baseline comparison if possible.\n\n3. **REFRAME TFN GENERALIZATION AS HYPOTHESIS**: Change the 20-30 rollout generalization claim from a design assumption to a key experimental question. State: 'We hypothesize that primitive-type-agnostic physical features enable few-shot transfer; quantifying the number of rollouts needed per novel primitive type IS a key experimental result.' Budget contingency compute (10-20h) in case generalization requires more rollouts than expected.\n\nMinor: Fix Humanoids 2026 deadline to July 24 (more favorable). Verify Generative Skill Chaining venue (CoRL 2023 vs 2024). Add Ψ₀ as a downstream consumer in the impact discussion.",
  "reason": "Strong algorithmic contribution (TFN) with verified compute feasibility, but critically fails to address user's CoRL 2026/20-day requirement and misses two directly competing 2026 works (RoboGene, FATE) in feasibility-aware task generation."
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e1baec04-65bf-463f-8348-4e17b4c1104d",
  "isSidechain": false,
  "requestId": "req_011CauS7VBSrJBRYE5MqMegk",
  "type": "assistant",
  "uuid": "e4fac64d-b2b9-43cb-a953-1a52dce61738",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c9f1e88d-7547-445a-bdb2-8a60925de079",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014ZSqHN1xGMctpU2KjpoYpy",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2178,
      "cache_creation_input_tokens": 1788,
      "cache_read_input_tokens": 43181,
      "output_tokens": 6697,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1788,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2178,
          "output_tokens": 6697,
          "cache_read_input_tokens": 43181,
          "cache_creation_input_tokens": 1788,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1788
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

_source line 43_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-10 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "e4fac64d-b2b9-43cb-a953-1a52dce61738",
  "sessionId": "c9f1e88d-7547-445a-bdb2-8a60925de079"
}
```

---

### Runtime record

_source line 44_

```json
{
  "type": "ai-title",
  "aiTitle": "Verify CompLocoGen novelty and feasibility for humanoid loco-manipulation task generation",
  "sessionId": "c9f1e88d-7547-445a-bdb2-8a60925de079"
}
```

---

### Runtime record

_source line 45_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-10 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "e4fac64d-b2b9-43cb-a953-1a52dce61738",
  "sessionId": "c9f1e88d-7547-445a-bdb2-8a60925de079"
}
```

---

### Runtime record

_source line 46_

```json
{
  "type": "ai-title",
  "aiTitle": "Verify CompLocoGen novelty and feasibility for humanoid loco-manipulation task generation",
  "sessionId": "c9f1e88d-7547-445a-bdb2-8a60925de079"
}
```

---
