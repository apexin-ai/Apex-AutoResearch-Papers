# Research conversation: You are a strict ML research reviewer conducting adversarial review. **Today's date: 2026-05-11 (UTC).** Your job: indep

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 48
- **Recorded user turns:** 1
- **Tool calls:** 10
- **Original source:** `logs/chats/exported-trajectories/account-2/ae8c16f5-ce1c-4bce-923e-3afb8499b025.jsonl`
- **Structured JSON:** [`4d97274ecb38dc05da38.json`](../../sessions/4d/4d97274ecb38dc05da38.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-12T00:44:37.801Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-12T00:44:37.801Z",
  "sessionId": "ae8c16f5-ce1c-4bce-923e-3afb8499b025",
  "content": "You are a strict ML research reviewer conducting adversarial review.\n\n**Today's date: 2026-05-11 (UTC).**\n\nYour job: independently verify this idea's claims via WebSearch, then issue a verdict.\n\n## User requirements\nThe user asked for: **Target: EMNLP 2026, ARR submission deadline 2026-05-25 (16 days from today 2026-05-09). Track: NLP and Symbolic Reasoning.\n\nDirection: Neurosymbolic reasoning — combining neural models with symbolic systems (logic programs, knowledge graphs, formal verification, constraint solvers). NOT limited to LLM-only reasoning — explicitly seek methods that integrate external symbolic components. Also in-scope: structured mathematical reasoning, program-aided reasoning, theorem prover integration.\n\nContribution type: METHOD ONLY. Must propose a new hybrid algorithm, training objective, or inference pipeline that combines neural + symbolic components. Pure prompting tricks (vanilla CoT, self-consistency) are out of scope.\n\nHARD CONSTRAINTS:\n1. Compute: ≤200 H100-hours total. Neurosymbolic methods are often inference-heavy not training-heavy — budget accordingly.\n2. Time: ≤16 days. Use existing open checkpoints (Qwen3, Llama-3.x, DeepSeek-R1 distills) + off-the-shelf solvers (Z3, Prolog, SymPy, Lean4).\n3. Eval: MATH, AIME 2024/2025, GPQA Diamond, ProofWriter, FOLIO, LogiQA, ARC-Challenge, BBH.\n\nLook for: lightweight symbolic verifiers as post-hoc filters, neural-guided symbolic search, structured output → formal checker pipelines, hybrid neuro-symbolic distillation. Avoid: pure prompt engineering, vanilla CoT.\n\nTag: direction=neurosymbolic_reasoning, contribution_type=method. target_venues=[\"EMNLP 2026 Main\", \"EMNLP 2026 Findings\"].**\nYou MUST evaluate whether this idea actually meets the user's requirements. If the user asked for a top venue, assess whether the idea is truly top-venue quality. If the user asked for low resource cost, verify the resource estimate is realistic and low. An idea that doesn't match what the user asked for should be \"revise\" or \"fail\".\n\n## 核心要求：非常仔细地调研，非常仔细地思考\n\n你是一个严格的审稿人。不要轻信 Generator 的任何 claim——你必须独立验证，深入思考每个维度。\n\n### 调研要求\n\n1. **独立 SOTA 验证**：自己搜索当前 SOTA，不要只检查 Generator 的引用。\n   每个验证维度建议用 2-3 种不同的搜索查询。\n\n2. **可行性深度检查**：\n   - 搜索类似实验的实际成本/周期\n   - 检查 claimed baselines 是否可复现\n   - 验证所需的 datasets/models 是否真的可以获取\n\n3. **新颖性压力测试**：专门搜索 Generator 可能遗漏的工作：\n   - 尝试不同的关键词组合\n   - 同时检查 arXiv 和 conference proceedings\n   - 寻找相邻领域的并行/concurrent 工作\n\n4. **深入阅读**：不要只依赖搜索摘要。用 WebFetch 实际阅读相关论文的 abstract 和关键章节，形成你自己的判断。\n\n### 思考要求\n\n5. **独立判断**：\n   - 不要因为 Generator 说得有道理就轻易 pass——真正好的 idea 经得起严格审查\n   - 思考这个 idea 在实际执行中会遇到什么困难\n   - 考虑这个 idea 对领域的真实贡献（不是自说自话的贡献）\n\n6. **评分诚实**：\n   - 不要给\"看起来还行\"的 idea 高分——4 分意味着\"确实很好\"，5 分意味着\"令人兴奋\"\n   - Agent 评分经常虚高，你的职责就是纠正这种偏差\n\n充分利用你的工具——做真正的调研，不是走过场。\n\n\n## 论文搜索策略\n\n你的搜索质量直接决定了 idea 的质量。不要敷衍搜索——每一次搜索都要有明确的目的。\n\n### 搜索源（推荐每个维度使用 2 个不同来源）\n\n1. **arXiv 预印本**（最新工作）:\n   - `site:arxiv.org {topic} {year}` — 按主题搜索最新论文\n   - `site:arxiv.org {method_name}` — 按具体方法名搜索\n   - `arxiv {topic} {month} {year}` — 精确到月份，找最近 3 个月的工作\n\n2. **Google Scholar**（引用关系 + 综合覆盖）:\n   - `{topic} {year} site:scholar.google.com` — 或直接搜索让 Google 自动包含 Scholar 结果\n   - `\"{exact paper title}\"` — 验证论文是否真实存在\n   - `\"{author name}\" {topic} {year}` — 按活跃作者追踪（找到领域大牛后追踪其最新工作）\n\n3. **Papers With Code**（SOTA 排行 + 代码可用性）:\n   - `site:paperswithcode.com {task_name}` — 查看任务的 SOTA 排行榜\n   - `site:paperswithcode.com {method_name}` — 查看方法是否已被实现\n   - `paperswithcode {dataset} benchmark` — 查看特定 dataset 上的竞争格局\n\n4. **OpenReview**（会议审稿 + 同行评价）:\n   - `site:openreview.net {topic} {year}` — 搜索会议提交的论文\n   - 用 WebFetch 阅读 OpenReview 上的 reviewer comments — 了解领域专家的真实评价\n\n5. **Semantic Scholar**（语义搜索 + 引用图谱）:\n   - `semantic scholar {topic} survey {year}` — 找综述论文\n   - `semanticscholar.org {paper_title}` — 查看 cited by（谁引用了这篇）和 references（它引用了谁）\n\n6. **GitHub**（实现验证）:\n   - `site:github.com {method_name} {task}` — 验证开源实现是否存在\n   - `site:huggingface.co {model_name}` — 验证模型/数据集是否可获取\n\n### 搜索维度（多角度交叉，不要只按 topic 搜）\n\n对每个 idea/方向，尽量覆盖以下维度：\n\n1. **正向搜索**：直接搜索主题相关论文\n   - `{topic} {subtopic} {year}`\n   - `{method_name} for {task_name}`\n\n2. **竞争论文搜索**（最关键！）：\n   - `{core_problem} {year}` — 有没有人在解决同样的问题？\n   - `{approach_keyword} {task} {year}` — 有没有人用类似方法？\n   - `{gap_description} solution` — 你发现的 gap 是否已被解决？\n   - **搜索知名团队的最新工作**：如果你知道哪些团队在做这个方向，搜索他们最近 6 个月的论文\n\n3. **相邻领域搜索**：\n   - `{method_from_other_field} applied to {your_task}`\n   - `{your_problem} in {adjacent_domain}` — 其他领域是否已解决类似问题\n\n4. **反面搜索**（找到反对你 idea 的证据）：\n   - `{your_approach} limitations` / `{your_approach} failure`\n   - `why {assumed_gap} is not a problem`\n   - `{baseline_method} sufficient for {task}` — baseline 是否其实已经够好\n\n5. **引用链追踪**（发现遗漏工作的最有效方法）：\n   - 找到一篇核心相关论文后，用 WebFetch 阅读它的 references 部分\n   - 在 Semantic Scholar 上查看它的 \"cited by\" — 最近引用它的论文很可能是 concurrent work\n   - 对 3 个以上核心相关论文重复此步骤\n\n### 搜索数量建议（理想目标，上下文充裕时尽量达到）\n\n| 角色 | 建议搜索次数 | 说明 |\n|------|-------------|------|\n| Round 1 Generator | 10-15 次 | 每个方向争取 3 次独立搜索 |\n| Round 2 Generator | 5-8 次 | 验证 approach 可行性 + baseline |\n| Review Agent | 8-12 次 | 独立验证 + 竞争论文 + 反面证据 |\n| Revision Agent | 5-10 次 | 针对每个 issue 独立调研 |\n\n### 上下文管理\n\n你的输出 token 有限，必须在上下文耗尽之前完成 JSON 输出。\n\n- 上述搜索次数是理想目标。在上下文充裕时应尽量多搜、深搜，搜得越充分越好。\n- 但必须动态评估剩余上下文：如果已经消耗了大量上下文，应优先完成输出，不要为了凑次数而冒着无法输出的风险。\n- WebFetch 深度阅读很有价值，但每次 fetch 消耗大量 token——优先 fetch 最关键的 2-3 篇，而不是每篇都 fetch。\n- 质量 > 数量：5 次精准搜索 + 深度思考 > 15 次浅层搜索。\n\n\nAs a reviewer, your search focus should be:\n1. **验证 claim**：Generator 声称的 SOTA、gap、novelty 是否属实\n2. **找竞争论文**：是否有 Generator 遗漏的高度相关/相似的工作\n3. **找反面证据**：是否有论文表明 Generator 的 approach 行不通\n4. **引用链检查**：通过核心论文的 cited-by 发现 concurrent work\n\n## 竞争论文专项搜索（Reviewer 独有）\n\n这是你作为 Reviewer 最重要的职责之一——发现 Generator 遗漏的竞争工作：\n\n1. **关键词变体搜索**：用至少 3 种不同的关键词组合搜索同一个问题\n   - 同义词替换（e.g., 'efficient' → 'lightweight/fast/scalable'）\n   - 不同粒度（e.g., 'text classification' → 'sentiment analysis' → 'NLP'）\n   - 方法名 + 任务名的不同组合\n\n2. **知名团队追踪**：如果你知道哪些团队/实验室在做相关方向，\n   搜索他们最近的论文（`\"team_name\" OR \"author_name\" {topic} {year}`）\n\n3. **会议最新录用**：搜索最近一轮 ICML/NeurIPS/ICLR/AAAI/ACL 等会议的 accepted papers\n   - `site:openreview.net {topic} 2026`\n   - `{conference_name} 2026 accepted papers {topic}`\n\n4. **arXiv 近 3 个月密集搜索**：对精确相关的关键词，搜索过去 3 个月的 arXiv 论文\n   这是发现 concurrent work 最有效的窗口\n\n如果你发现了 Generator 遗漏的重要相关工作，必须在 issues 中列出论文标题和链接，\n并在 feedback 中说明这些工作如何影响 idea 的 novelty。\n\n## Review checklist\n1. **SOTA freshness**: Are the models/baselines cited actually current SOTA?\n   If outdated, specify what the current SOTA is and cite your source.\n2. **Reference verification**: Do the cited papers actually exist? (WebSearch to check)\n3. **Gap validity**: Does the claimed research gap still exist, or has recent work addressed it?\n4. **Venue validity**: Are target_venues' submission deadlines after 2026-05-11?\n5. **Feasibility**: Is the resource estimate realistic? Are there hidden dependencies?\n6. **Novelty**: Is this sufficiently different from existing work?\n   When scoring novelty < 4:\n   - You MUST identify the closest existing work(s) via WebSearch\n   - In your feedback, write: \"This idea is too similar to [Paper Title (Venue Year)]. Specifically, [what overlaps]. To differentiate, the generator should [suggestion].\"\n   - This gives the generator targeted guidance to boost novelty, not just \"be more novel\".\n7. **Cost realism across modes**: Are the three mode estimates (manual/human-in-loop/auto) internally consistent?\n   - Auto Research uses more GPU hours (2-5x manual) but GPU idle rate should be near zero\n   - Auto Research timeline should reflect resource availability as bottleneck — days with sufficient GPUs, not weeks\n   - Human-in-Loop should fall between manual and auto on most dimensions\n   - Manual and HIL must NOT include salary/wages — only GPU and API costs\n   - Auto Research must NOT include agent operational overhead\n   - If any mode estimate is clearly unrealistic, flag it\n\n## Idea under review (round 7/10)\n{\n  \"title\": \"Two-Tier Confidence-Gated Formalization with Roundtrip Validation and Cumulative Online Constraint Tracking for Multi-Step Reasoning Verification\",\n  \"core_problem\": \"In multi-step reasoning, errors introduced at step k propagate to steps k+1...n, creating cascading failures. Online verification systems have emerged to catch errors during generation: interwhen (Microsoft, Feb 2026) achieves effective cumulative-like checking for structured-state tasks (ZebraLogic, Maze, SpatialMap) by forking inference to extract the full current solution state and verifying it against constraints via Z3. However, for derivation tasks — mathematical proofs and logical deduction chains (ProofWriter, FOLIO, AIME) — no compact solution state exists to extract mid-generation; the verification state IS the accumulated chain of derived assertions. VeriCoT (ICLR 2026 poster) maintains cumulative Z3 assertion tracking for derivation tasks but operates only post-hoc. Beyond the online-vs-post-hoc and state-vs-assertion distinctions, all verification systems face a formalization bottleneck with two failure modes: (1) formalization failure — NL-to-formal translation fails outright (HERMES reports >60% autoformalization failure at Kₜ=1 with DeepSeek-V3.1), leaving the constraint store sparse and uninformative; and (2) systematic unfaithfulness — 'Do LLMs Game Formalization?' (arXiv 2604.19459, April 2026) demonstrates that LLMs systematically mistranslate premises during formalization, producing internally consistent but unfaithful outputs that 'evade detection entirely.' Cross-sample consistency alone cannot catch systematic errors because all K samples may converge on the same incorrect formalization. Can a two-tier confidence-gated formalization system — with roundtrip validation to catch systematic errors at Tier 1, and weak but near-100%-reliable constraints at Tier 2 — maintain both constraint store informativeness and precision during online verification of derivation tasks?\",\n  \"opportunity\": \"A convergence of recent findings creates the opportunity for a principled solution to the formalization bottleneck in online reasoning verification. interwhen (Microsoft, Feb 2026) demonstrates that online Z3 verification during generation improves accuracy by up to 15pp on structured-state tasks. However, for derivation tasks — where reasoning progresses through chains of intermediate lemmas — interwhen's state-extraction paradigm does not apply. VeriCoT (ICLR 2026 poster) validates that cumulative assertion tracking catches cross-step inconsistencies in derivation tasks, but operates post-hoc. HERMES achieves online Lean4 verification but with >60% autoformalization failure at Kₜ=1. Crucially, 'Do LLMs Game Formalization?' (arXiv 2604.19459, April 2026) reveals a deeper threat: systematic premise mistranslation that produces internally consistent but unfaithful formalizations, evading detection by cross-sample consistency, LLM-as-judge, and rule-based diff. This means cross-sample consistency is necessary but insufficient for formalization confidence — a complementary faithfulness check is needed. 'Faithful Autoformalization via Roundtrip Verification and Repair' (arXiv 2604.25031, April 2026) demonstrates that roundtrip verification (formalize → informalize → re-formalize → Z3 equivalence) raises formal equivalence from 45-61% to 83-85%, with Z3 equivalence checks resolving in <1 second. ReForm (arXiv 2510.24592) shows that reflective self-validation during autoformalization achieves +22.6pp average improvement. 'Autoformalize Mathematical Statements by Symbolic Equivalence and Semantic Consistency' (NeurIPS 2024) validates cross-sample consistency as a useful signal (combined method achieves 45.8% on MATH, 8.3% absolute improvement). The unexploited combination is: (1) two-tier confidence-gated formalization with roundtrip validation — cross-sample consistency for candidate selection, roundtrip verification to catch systematic errors, and weak constraint fallback when confidence is low — that manages the informativeness-precision tradeoff explicitly (PRIMARY novelty), (2) online assertion-level cumulative tracking for derivation tasks (SECONDARY), and (3) MUS-guided targeted regeneration (TERTIARY). We formalize this as an informativeness-precision tradeoff: define constraint store informativeness I(C) = fraction of steps with ≥1 constraint, and precision P(C) = fraction of semantically correct constraints. Without gating: I≈1.0, P≈0.4-0.6. With Tier 1 only: I≈0.5, P≈0.9. With two-tier + roundtrip: I≈0.95, P≈0.85-0.95. This principled framework is the first to explicitly manage the informativeness-precision tradeoff in online reasoning verification.\",\n  \"landscape\": \"**Online verification systems**: interwhen (Microsoft, arXiv 2602.11202, Feb 2026) introduces the 'LLM-Process-Modulo' paradigm — periodically polling the reasoning trace, forking inference to recover intermediate solutions, and running Z3 asynchronously. For structured-state tasks (ZebraLogic, Maze, SpatialMap, Game24, Verina), it converts the model's structured output into a representation checked for logical consistency using Z3, effectively achieving cumulative-like checking by extracting the full accumulated solution state at each fork point. On ZebraLogic X-Large, it achieves +10.4pp with Qwen3-30B-A3B. However, for derivation tasks (math proofs, logical deductions), there is no compact solution state to extract. HERMES (arXiv 2511.18760, Nov 2025) interleaves informal reasoning with Lean4 verification, achieving 97.4% on MATH-500 and 66.7% on AIME'25 with DeepSeek-V3.1, but with >60% autoformalization failure at Kₜ=1.\\n\\n**Post-hoc verification systems**: VeriCoT (ICLR 2026 poster, arXiv 2511.04662) autoformalizes each step into FOL, maintains cumulative Z3 constraints (ℱᵢ = ℱᵢ₋₁ ∪ {Fᵢ}), and checks entailment/contradiction — pioneering cumulative assertion tracking for derivation tasks but post-hoc only. VERGE (arXiv 2601.20055, Jan 2026) uses LLM-based claim-level semantic routing across 6 types and MCS-based error localization, achieving 18.7% average uplift. Its ablation shows routing is essential: removing it causes -8.3% average degradation (HLE halving from 30.5% to 15.2%). Safe (ACL 2025, arXiv 2506.04592) performs step-aware Lean4 verification but does not address formalization confidence.\\n\\n**Formalization faithfulness — the systematic error problem**: 'Do LLMs Game Formalization?' (arXiv 2604.19459, April 2026) uses a two-stage pipeline (formalization then proof over locked formalization) to expose model-specific gaming behaviors. GPT-5 fabricates axioms during proof generation (107 instances, 56.2% conclusion-as-axiom), which IS detectable via cross-stage comparison. But DeepSeek-R1 mistranslates premises during formalization itself, producing internally consistent outputs that evade ALL tested detection methods — cross-stage comparison, LLM-as-judge (Claude Opus 4.5), and rule-based diff. This directly threatens cross-sample consistency mechanisms: if the formalizer consistently makes the same semantic error across all K samples, high consistency is assigned to an incorrect formalization. The paper evaluates on 303 FOL problems (FOLIO + Multi-LogiEval) with compilation rates of 87-99% despite substantial unfaithfulness.\\n\\n**Formalization reliability and roundtrip defenses**: 'Faithful Autoformalization via Roundtrip Verification and Repair' (arXiv 2604.25031, April 2026) demonstrates that roundtrip verification (formalize → informalize → re-formalize → Z3 equivalence check, <1s per check) raises formal equivalence from 45-61% to 83-85%, with diagnosis-guided repair requiring only 7.21 LLM calls per repair vs. 12.27 for random baseline. ReForm (arXiv 2510.24592, ICLR 2026 submission) interweaves autoformalization with semantic self-validation, achieving +22.6pp average improvement across four benchmarks. 'Autoformalize Mathematical Statements by Symbolic Equivalence and Semantic Consistency' (NeurIPS 2024, arXiv 2410.20936) validates cross-sample consistency: combined method (Z3/CVC5 + Isabelle/HOL) achieves 45.8% on MATH (8.3% absolute improvement); symbolic equivalence alone achieves 42.0% (4.5% absolute). 'Grammars of Formal Uncertainty' (NeurIPS 2025, arXiv 2505.20047) achieves AUROC >0.93 for detecting formalization errors on logic tasks but shows SMT helps on logic (+34.8%) while hurting on factual tasks (-44.5%).\\n\\n**Domain-aware routing**: Adaptive LLM-Symbolic Reasoning (EACL 2026, arXiv 2510.06774) demonstrates dynamic solver selection from Z3/Pyke/Prover9/MiniZinc outperforms static approaches, with LLMs achieving >90% solver prediction accuracy.\\n\\n**The gap**: No system combines (1) confidence-gated formalization with both cross-sample consistency AND roundtrip validation to catch systematic errors, plus weak constraint fallback for maintaining informativeness — explicitly managing the informativeness-precision tradeoff (PRIMARY), (2) online assertion-level cumulative tracking for derivation tasks (SECONDARY), and (3) MUS-guided targeted regeneration (TERTIARY). The 'Do LLMs Game Formalization?' paper makes roundtrip validation a necessity, not a luxury — cross-sample consistency alone is vulnerable to systematic mistranslation.\",\n  \"approach\": \"Build a three-component pipeline — Reasoner, Two-Tier Confidence-Gated Formalizer with Roundtrip Validation, and Cumulative Online Constraint Monitor — that operates incrementally during chain-of-thought generation.\\n\\n**Formal Framework: Informativeness-Precision Tradeoff**. We define two metrics for constraint store quality: (a) **Informativeness** I(C) = |{i : C(sᵢ) ≠ ∅}| / n — the fraction of reasoning steps with at least one constraint in the store. (b) **Precision** P(C) = |{c ∈ ∪C(sᵢ) : c is semantically faithful}| / |∪C(sᵢ)| — the fraction of constraints that faithfully represent the original NL step. Without gating (accept all formalizations): I ≈ 1.0, P ≈ 0.4-0.6. With Tier 1 only (skip low-confidence steps): I ≈ 0.4-0.6, P ≈ 0.85-0.95. With Tier 2 fallback: I ≈ 0.95-1.0, P ≈ 0.85-0.95. The two-tier mechanism with roundtrip validation explicitly manages this tradeoff: Tier 1 + roundtrip optimizes for precision (high threshold, systematic error detection), Tier 2 optimizes for informativeness (near-100% correct by construction). We evaluate both metrics empirically and report the Pareto frontier across configurations.\\n\\n**Reasoner**: Qwen3-32B in thinking mode. Baseline performance (thinking mode, pass@1): AIME'24 ~70%, AIME'25 ~76.7%, MATH-500 ~95.2%.\\n\\n**Two-Tier Confidence-Gated Formalizer with Roundtrip Validation (PRIMARY CONTRIBUTION)**:\\n\\n- **Tier 1 (Full formalization with roundtrip validation)**: Generate K=5 candidate formalizations per step in SMT-LIB using Qwen3-14B. Compute confidence via cross-sample majority consistency: normalize candidates syntactically, then check pairwise symbolic equivalence using Z3. If ≥4/5 candidates are equivalent, the majority candidate proceeds to **roundtrip validation**: (i) informalize the majority formalization back to NL using Qwen3-14B (1 LLM call), (ii) compare the back-translated NL against the original reasoning step via an NLI-style entailment check (1 LLM call, or combined into a single call: 'Translate this formal statement back to English. Is the result semantically equivalent to: [original step]? Answer YES/NO with brief justification.'). If roundtrip confirms faithfulness → accept as Tier 1. If roundtrip detects semantic drift → downgrade to Tier 2 even though cross-sample consistency was high. This directly addresses the systematic mistranslation threat identified by 'Do LLMs Game Formalization?': even when all K samples agree on an incorrect formalization, the roundtrip back to NL exposes semantic divergence from the original step. The roundtrip approach is inspired by arXiv 2604.25031 (which raises formal equivalence from 45-61% to 83-85%), adapted as a lightweight single-call validation rather than a full multi-iteration repair pipeline. **Cost**: +1 LLM call per high-confidence step (combined informalization + NLI check), amortized only over steps that pass cross-sample consistency (~50-60% of steps). **Known limitation**: If the same model systematically produces the same NL interpretation during both formalization and informalization, roundtrip may not catch the error. We quantify this residual risk empirically by measuring the rate of roundtrip-undetected systematic errors using a held-out set of manually annotated formalization pairs (50 steps each from AIME, ProofWriter, FOLIO). We expect this rate to be low based on the roundtrip paper's results (83-85% equivalence after roundtrip), but report it transparently.\\n\\n- **Tier 2 (Weak constraints)**: When Tier 1 confidence falls below threshold OR roundtrip validation fails, extract weaker but near-100%-reliable constraints via templated patterns from the NL step. For **math/arithmetic steps**: numerical value bindings (x = 15), type constraints (is_integer, is_positive), ordering relations (x > y), simple arithmetic identities. For **logical reasoning steps**: truth value assignments (A = True), simple propositional entailments (P → Q), predicate-argument bindings (Dog(X) = True), negation patterns (Kind(A) = False). Tier 2 precision is near-100% by construction (simple pattern matching on surface forms), ensuring I(C) remains high without degrading P(C).\\n\\n**Minimum Viable Validation — Specific Error Types**: The two-tier mechanism's value is demonstrated by catching specific cross-step error patterns that require both Tier 1 and Tier 2 constraints:\\n- **AIME**: Step 3 establishes 'let n = 15' (Tier 2 if full formalization fails: n = 15, is_integer(n)). Step 7 derives 'n² = 225' (Tier 1 or 2). Step 9 erroneously claims 'n² = 216' → UNSAT with constraints from steps 3 and 7. Without Tier 2, if step 3's full formalization failed, no constraint on n exists and the error propagates.\\n- **ProofWriter**: Step 1 establishes 'If something is big and round then it is nice' (Tier 2: Big(x) ∧ Round(x) → Nice(x)). Step 3: 'Bob is big and round' (Tier 2: Big(Bob), Round(Bob)). Step 5 claims 'Bob is not nice' → UNSAT. These propositional patterns are exactly what Tier 2 captures reliably.\\n- **FOLIO**: Step 1: 'All students who study hard pass' (Tier 2: Student(x) ∧ StudyHard(x) → Pass(x)). Step 3: 'Alice studies hard' (Tier 2: StudyHard(Alice)). Step 5: 'Alice fails' → UNSAT.\\nWe measure: (a) how many such cross-step errors exist in baseline generations, (b) what fraction are caught by Tier 1 alone vs. Tier 1+2, (c) what fraction require Tier 2 constraints specifically (the delta is the two-tier mechanism's marginal value).\\n\\n**Domain-Aware Routing via Rule-Based Heuristic**: Benchmark-level rule-based heuristic: {AIME, MATH-500, ProofWriter, FOLIO, LogiQA} → Z3 verification; {ARC-Challenge, GPQA Diamond, BBH} → LLM reasoning only. Sufficient for fixed benchmark evaluation; dynamic instance-level routing (following EACL 2026 / VERGE) is a clear future direction.\\n\\n**Cumulative Online Constraint Monitor (SECONDARY CONTRIBUTION)**: Maintains a cumulative incremental Z3 solver context at the assertion level for derivation tasks. After each formalization (Tier 1 or Tier 2), assertions are pushed and check-sat is called (<100ms for linear arithmetic). If UNSAT:\\n- Extract MUS via Z3's unsat-core API.\\n- Map conflicting assertions to originating steps.\\n- Pop the conflicting step's scope.\\n- Provide the Reasoner with a structured constraint-violation prompt containing the specific conflicting constraints.\\n- Regenerate the violating step with explicit feedback. If UNSAT persists after 3 attempts, fall back to regenerating from the earliest conflicting step in the MUS.\\n\\n**Central Experiment — Minimum Publishable Result Set**: The core claim requires comparing 4 conditions on 3 benchmarks:\\n1. **Online-Cumulative (ours)**: Two-tier confidence-gated formalization with roundtrip validation + cumulative assertion tracking.\\n2. **Online-Independent (interwhen-style)**: Online Z3 checking against problem constraints only, without cumulative tracking.\\n3. **Post-hoc-Cumulative (VeriCoT-style)**: Cumulative Z3 checking applied after full chain with self-reflection.\\n4. **No-verification baseline**: Qwen3-32B thinking mode.\\nOn 3 core benchmarks: **AIME 2024, ProofWriter, FOLIO**.\\nWith 1 core ablation: **Two-tier (Tier 1 + Tier 2) vs. Tier-1-only** (measuring Tier 2's marginal contribution to informativeness and error detection).\\nThis constitutes 4 conditions × 3 benchmarks × 2 ablation levels = **24 runs, achievable in ~60 H100-hours (~5 days)**.\\n\\n**Stretch goals** (if time permits):\\n- Additional benchmarks: AIME 2025, MATH-500 (near-saturated), ZebraLogic (comparison benchmark — expect to MATCH interwhen, validating no degradation on structured-state tasks), GPQA Diamond (sanity check, expect no improvement).\\n- Additional baselines: HERMES (online Lean4, noting different base model), VERGE (post-hoc MCS), majority voting (k=8).\\n- Additional ablations: MUS-guided vs. generic retry vs. MCS-guided feedback; roundtrip validation ON vs. OFF.\\n\\n**ZebraLogic Positioning**: ZebraLogic is repositioned as a **comparison benchmark**, not a prioritized one. On ZebraLogic, interwhen's state-extraction achieves +10.4pp (X-Large, Qwen3-30B-A3B) and should perform well because it is a structured-state task. Our approach should **match** interwhen on ZebraLogic, validating that assertion-level tracking does not degrade performance on structured-state tasks, while **exceeding** interwhen and VeriCoT on derivation tasks (AIME, ProofWriter, FOLIO) where state extraction cannot apply. This strengthens the paper's narrative: our approach fills a complementary gap for derivation tasks, not a replacement for interwhen on structured-state tasks.\\n\\nMeasure: (a) error cascade length, (b) total regeneration cost, (c) downstream accuracy, (d) wall-clock latency, (e) false positive rate, (f) constraint store informativeness I(C), (g) constraint store precision P(C).\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"~150h H100-80GB\",\n      \"gpu_utilization\": \"Low (~25%). GPUs idle during confidence calibration and formalization error analysis.\",\n      \"timeline\": \"2-2.5 months\",\n      \"team\": \"1-2 researchers (one NLP/LLM, one with SMT/constraint programming experience)\",\n      \"estimated_gpu_cost\": \"$450-600 (at ~$3-4/hr H100 spot)\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"~120h H100-80GB\",\n      \"gpu_utilization\": \"Moderate (~55%). Agent runs experiments between check-ins.\",\n      \"timeline\": \"3-5 weeks\",\n      \"team\": \"1 researcher, ~30-40min/day reviewing formalization quality, confidence calibration, and Tier 2 template coverage\",\n      \"claude_api_cost\": \"$100-180 (1000-1800 turns)\",\n      \"estimated_gpu_cost\": \"$360-480\",\n      \"risk_note\": \"Tier 2 propositional constraint templates for logic benchmarks need manual validation on ~50 sample steps from ProofWriter/FOLIO. Roundtrip validation residual error rate needs manual annotation on 150 steps (50 per core benchmark).\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"~180h H100-80GB (Qwen3-32B on 2 H100s + Qwen3-14B on 1 H100 = 3 H100s per experiment; +10h for roundtrip validation overhead)\",\n      \"gpu_utilization\": \"High (~80%). Continuous inference pipeline; Z3 calls <100ms; roundtrip adds ~1 Qwen3-14B call per Tier 1 step.\",\n      \"timeline\": \"10-14 days with 4 H100s available. FALLBACK: If pipeline debugging takes >7 days, execute minimum publishable result set only (4 conditions × 3 benchmarks × 2 ablation = 24 runs, ~60 H100-hours, ~5 days). Stretch benchmarks and ablations deferred to camera-ready.\",\n      \"team\": \"0 (initial setup + final review)\",\n      \"claude_api_cost\": \"$200-350 (2000-3500 turns)\",\n      \"estimated_gpu_cost\": \"$540-720\",\n      \"speed_bottleneck\": \"Formalizer throughput: K=5 samples per step × ~500 tokens/sample for Qwen3-14B + 1 roundtrip call (~300 tokens) per high-confidence step. With vLLM batching on 1 H100, ~3000 tok/s → ~1.0s per step's formalization set including roundtrip. Cross-sample equivalence checking via Z3 adds <50ms.\",\n      \"risk_note\": \"Systematic formalization errors (per arXiv 2604.19459) may partially evade roundtrip detection if the same model performs both formalization and informalization. Mitigation: quantify residual rate on 150 manually annotated steps. If residual rate exceeds 15%, consider using a different model (e.g., Qwen3-8B) for informalization to break the systematic error pattern.\",\n      \"timeline_derisking\": \"Core result set (24 runs, ~60 H100-hours) is achievable in 5 days even with significant debugging time. Stretch goals add ~120 H100-hours over 5-9 additional days. Prioritized benchmark ordering: AIME'24 first (highest expected improvement), then ProofWriter + FOLIO (logic benchmarks demonstrating Tier 2 value), then stretch benchmarks.\"\n    }\n  },\n  \"target_venues\": [\n    \"EMNLP 2026 (ARR deadline May 25, 2026)\",\n    \"AAAI 2027 (deadline ~August 1, 2026)\",\n    \"ICLR 2027 (deadline ~September-October 2026)\"\n  ],\n  \"level\": \"solid\",\n  \"key_references\": [\n    \"interwhen: A Generalizable Framework for Verifiable Reasoning with Test-time Monitors (Microsoft, arXiv 2602.11202, Feb 2026)\",\n    \"VeriCoT: Neuro-symbolic Chain-of-Thought Validation via Logical Consistency Checks (ICLR 2026 poster, arXiv 2511.04662)\",\n    \"HERMES: Towards Efficient and Verifiable Mathematical Reasoning in LLMs (arXiv 2511.18760, Nov 2025) — base model: DeepSeek-V3.1\",\n    \"VERGE: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning (arXiv 2601.20055, Jan 2026)\",\n    \"Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning (arXiv 2604.19459, April 2026)\",\n    \"Faithful Autoformalization via Roundtrip Verification and Repair (arXiv 2604.25031, April 2026)\",\n    \"ReForm: Reflective Autoformalization with Prospective Bounded Sequence Optimization (arXiv 2510.24592)\",\n    \"Safe: Enhancing Mathematical Reasoning in Large Language Models via Retrospective Step-aware Formal Verification (ACL 2025, arXiv 2506.04592)\",\n    \"Adaptive LLM-Symbolic Reasoning via Dynamic Logical Solver Composition (EACL 2026, arXiv 2510.06774)\",\n    \"Grammars of Formal Uncertainty: When to Trust LLMs in Automated Reasoning Tasks (NeurIPS 2025, arXiv 2505.20047)\",\n    \"Autoformalize Mathematical Statements by Symbolic Equivalence and Semantic Consistency (NeurIPS 2024, arXiv 2410.20936)\",\n    \"Efficient PRM Training Data Synthesis via Formal Verification [FoVer] (ACL 2026 Findings, arXiv 2505.15960)\",\n    \"ProcessBench: Identifying Process Errors in Mathematical Reasoning (ACL 2025)\",\n    \"Beyond Correctness: Exposing LLM-generated Logical Flaws via Multi-step Automated Theorem Proving [MATP] (ICSE 2026)\"\n  ],\n  \"description\": \"We propose a two-tier confidence-gated formalization system with roundtrip validation for online multi-step reasoning verification, targeting derivation tasks (mathematical proofs, logical deduction chains) where existing online verification approaches cannot apply their state-extraction paradigm. We ground our approach in a formal informativeness-precision tradeoff: define constraint store informativeness I(C) as the fraction of steps with ≥1 constraint, and precision P(C) as the fraction of semantically faithful constraints. Without gating: I≈1.0, P≈0.4-0.6 (many wrong constraints cause false positives). With Tier 1 only: I≈0.5, P≈0.9 (sparse store misses errors). Our two-tier mechanism achieves I≈0.95, P≈0.85-0.95 by construction. Our PRIMARY contribution is a two-tier confidence gate with roundtrip validation: Tier 1 uses cross-sample majority consistency (≥4/5 Z3-equivalent candidates) for candidate selection, followed by a lightweight roundtrip validation step (informalize back to NL, check semantic equivalence with original step — 1 additional LLM call) that catches systematic formalization errors identified by 'Do LLMs Game Formalization?' (arXiv 2604.19459). When roundtrip detects semantic drift, the step is downgraded to Tier 2 even if cross-sample consistency was high. Tier 2 extracts weaker but near-100%-reliable constraints — numerical bindings for math steps, truth value assignments and propositional entailments for logic steps — keeping the constraint store informative when full formalization fails or is unfaithful. Specific error types demonstrating value: on AIME, Tier 2 catches arithmetic propagation errors (step 3: n=15, step 9: n²=216 → UNSAT); on ProofWriter, Tier 2 catches transitive reasoning violations (Big(Bob) ∧ Round(Bob) with Big∧Round→Nice, then ¬Nice(Bob) → UNSAT). Our SECONDARY contribution extends VeriCoT's post-hoc cumulative Z3 assertion tracking to online generation for derivation tasks where interwhen's state-extraction does not work. Our TERTIARY contribution uses MUS-guided targeted regeneration. ZebraLogic is repositioned as a comparison benchmark: we expect to match interwhen (which achieves +10.4pp on X-Large via state extraction) on structured-state tasks while exceeding it on derivation tasks, strengthening the narrative that our approach fills a complementary gap. The minimum publishable result set is 4 conditions (online-cumulative ours, online-independent interwhen-style, post-hoc-cumulative VeriCoT-style, no-verification) × 3 core benchmarks (AIME 2024, ProofWriter, FOLIO) × 2 ablation levels (two-tier vs. Tier-1-only) = 24 runs in ~60 H100-hours, with remaining benchmarks and ablations as stretch goals. Timeline fallback: if debugging exceeds 7 days, execute only the minimum publishable set (~5 days). Evaluation uses Qwen3-32B in thinking mode with domain-aware rule-based routing (Z3 for math/logic benchmarks, LLM-only for factual benchmarks).\",\n  \"project_name\": \"two_tier_gated_verify\",\n  \"source\": \"web_research\"\n}\n\n\n## Previous review history\n### Round 1 review\nVerdict: revise\nIssues: [\"CRITICAL: The novelty claim is built on a factual error about VeriCoT. VeriCoT already maintains cumulative Z3 constraints (ℱᵢ = ℱᵢ₋₁ ∪ {Fᵢ}) and checks cross-step consistency (ℱᵢ₋₁ ⊧ ¬Fᵢ). The generator's claim that VeriCoT 'checks entailment from premises and prior steps, but entailment checking is different from cumulative consistency checking' is directly contradicted by VeriCoT's paper.\", \"HERMES (Nov 2025) already does online verification during LLM generation with a memory module for proof continuity across multi-step chains, addressing the 'online vs post-hoc' differentiation the generator claims as novel.\", \"VERGE (Jan 2026) already uses Minimal Correction Subsets (MCS) for precise error localization, which is functionally equivalent to the proposed MUS-based error localization via Z3 unsat-core.\", \"NL-to-Z3 translation accuracy is a critical bottleneck: recent benchmarks show ~71% accuracy for NL-to-formal-logic translation. A ~30% formalization error rate would generate spurious UNSAT results (false positives) that trigger unnecessary regeneration of correct steps, potentially degrading performance below baselines.\", \"Evaluation benchmarks don't match user requirements. User specified: MATH, AIME 2024/2025, GPQA Diamond, ProofWriter, FOLIO, LogiQA, ARC-Challenge, BBH. Proposal only evaluates on: ProcessBench, MATH-500, ProofWriter — missing 6 of 8 required benchmarks.\", \"Compute budget mismatch: DeepSeek-R1 (671B) requires 8+ H100s minimum. Combined with Qwen-72B formalizer, running evaluations + ablations on multiple benchmarks would likely exceed the 200 H100-hour constraint. The auto_research estimate of 700 A100-hours (~450 H100-hours) explicitly exceeds the budget by 2.25x.\", \"The proposal does not address the false positive problem: when Z3 reports UNSAT due to an incorrect formalization (not a real reasoning error), the system would incorrectly force regeneration of a correct step, potentially introducing new errors.\", \"Missing comparison with HERMES (Lean-based online verification + memory module) as a baseline, which is the most directly relevant competitor for the 'online verification during generation' claim.\"]\nFeedback: The idea has a kernel of merit (online incremental constraint checking with targeted regeneration) but the novelty framing needs a complete overhaul. Specific actions to revise:\n\n1. **Fix the VeriCoT characterization**: Acknowledge that VeriCoT already does cumulative Z3 consistency checking. Reframe the contribution as: VeriCoT operates post-hoc (verify-then-reflect on the complete chain), while your approach intervenes mid-generation before downstream steps compound the error. The real novelty is the *timing* of intervention (online, not post-hoc) and *granularity* of correction (single-step targeted regeneration with MUS feedback, not full chain self-reflection).\n\n2. **Add HERMES as a key baseline**: HERMES does online verification with Lean. Your approach should differentiate by using Z3 (broader constraint language, faster for arithmetic) vs. Lean (more expressive but slower). This is a meaningful tradeoff to discuss.\n\n3. **Address the NL-to-Z3 formalization bottleneck head-on**: Propose a calibration mechanism to estimate formalization confidence. When confidence is low, skip Z3 checking for that step rather than risk false positives. Consider using MATH-VF's Solution Graph (sparse dependency tracking) to reduce what needs to be formalized.\n\n4. **Match evaluation benchmarks to user requirements**: Add AIME 2024/2025, GPQA Diamond, FOLIO, LogiQA, ARC-Challenge, BBH. Note that the approach may only benefit math/logic domains — candidly scope the evaluation.\n\n5. **Use distilled models to fit compute budget**: Switch to DeepSeek-R1-Distill-Qwen-32B (fits on 2 H100s, scores 72.6% on AIME 2024) and a smaller formalizer (Qwen-2.5-14B or fine-tuned 7B). Re-estimate costs in H100-hours explicitly.\n\n6. **Quantify the 'online vs post-hoc' advantage**: Design an experiment showing that intervening at step k prevents error cascading in steps k+1...n, while post-hoc approaches (VeriCoT) detect the error but incur the cascade cost. This is the real value proposition — make it the central experiment.\n\n### Round 2 review\nVerdict: revise\nIssues: [\"CRITICAL: interwhen (Microsoft, Feb 2026, arXiv 2602.11202) is not cited. This paper already demonstrates online verification during LLM reasoning generation using Z3 SMT solver for logic/spatial tasks, with asynchronous verifier execution and trajectory interruption only on error detection — achieving up to 15pp accuracy improvement. This directly overlaps with the proposal's core 'online Z3 verification during generation' claim and must be addressed as a baseline.\", \"The PCFG-based confidence estimation from 'Grammars of Formal Uncertainty' was validated on ProofWriter (logic tasks) with AUROC >0.93, but the same paper shows SMT autoformalization HURTS accuracy on factual tasks (-44.5%). The proposal evaluates on GPQA Diamond and ARC-Challenge where formalization may degrade rather than help — the confidence gating may need domain-specific behavior (always skip on certain task types), which adds complexity not currently addressed.\", \"Formalization coverage risk: at ~60-72% autoformalization accuracy in current literature, even with K=5 sampling and confidence gating, a substantial fraction of reasoning steps may have low confidence and be skipped. If >40% of steps are skipped, the cumulative constraint store becomes sparse and less effective at catching cross-step inconsistencies — potentially reducing the system to verifying only 'easy' steps that were likely correct anyway.\", \"MATH-500 is near-saturated (HERMES achieves 97.4% with online Lean4 verification). Using Qwen3-32B as the base model, the baseline accuracy may already be >95%, leaving <5% absolute headroom. The primary evaluation signal will need to come from AIME 2024/2025, but these are harder problems where NL-to-Z3 formalization accuracy is more uncertain.\", \"16-day timeline risk: implementing the full pipeline (Qwen3-32B reasoner + Qwen3-14B formalizer + PCFG confidence estimation + incremental Z3 solver + MUS extraction + targeted regeneration), calibrating confidence thresholds per domain, running 8+ benchmarks, and completing 4 ablation studies is ambitious. The PCFG fitting alone requires generating K=5 samples per step across a validation set, parsing them as SMT-LIB, and computing grammar statistics.\", \"MUS vs MCS distinction from VERGE is not well-articulated. MUS (what went wrong) and MCS (what to change) are dual concepts. The proposal should clarify why MUS-guided feedback is superior to VERGE's MCS-based correction for the targeted regeneration use case, rather than just using a different acronym.\"]\nFeedback: The proposal has significantly improved from Round 1 — the VeriCoT characterization is now correct, HERMES is included as a baseline, confidence gating addresses the formalization bottleneck, and the central experiment is well-designed. The remaining issues are addressable:\n\n1. **Add interwhen as a key baseline and differentiate explicitly**: interwhen (arXiv 2602.11202, Feb 2026) does online Z3 verification during generation but (a) does NOT maintain cumulative constraint state across steps — it checks each intermediate solution independently, (b) does NOT use PCFG-based confidence gating — it verifies at fixed polling intervals, and (c) does NOT provide MUS-derived structured feedback — it simply interrupts and lets the model self-correct. Frame your contribution as: cumulative constraint tracking + confidence-aware selective formalization + MUS-guided targeted regeneration, which interwhen lacks.\n\n2. **Address formalization coverage explicitly**: Add an analysis/ablation measuring what fraction of steps pass the confidence threshold across different benchmark domains. If coverage is <50% on math benchmarks, consider a fallback: for skipped steps, add a weaker constraint (e.g., numerical range bounds or type constraints) that can be formalized with near-100% confidence, keeping the constraint store informative even when full formalization fails.\n\n3. **Scope GPQA Diamond and ARC-Challenge honestly**: Given that SMT hurts on factual tasks per 'Grammars of Formal Uncertainty', consider dropping these from primary evaluation or adding a 'domain classifier' that routes tasks to Z3 verification only when the task type is logic/math. Report these benchmarks as 'sanity checks' showing the system doesn't degrade on non-target domains.\n\n4. **Clarify MUS vs MCS**: MUS identifies the minimal set of conflicting constraints (diagnosis), while MCS identifies the minimal set to remove to restore satisfiability (repair). Argue that MUS is better for targeted regeneration because it tells the LLM WHAT went wrong (conflicting constraints), not just WHAT to remove.\n\n5. **De-risk timeline**: Consider dropping one ablation (e.g., K=1 vs K=5 can be a supplementary experiment) and focusing on the 3 most important: confidence gating ON/OFF, online vs post-hoc, and MUS feedback vs generic retry. Prioritize AIME and ProofWriter/FOLIO results over MATH-500 (saturated).\n\n### Round 3 review\nVerdict: revise\nIssues: [\"ARC-Challenge is still missing from the evaluation benchmarks despite being explicitly required by the user. The proposal includes ZebraLogic and ProcessBench (not required) but omits ARC-Challenge (required).\", \"Timeline risk is the biggest concern: 14 days remaining to implement a 5-component pipeline (Reasoner, Two-Tier Formalizer with PCFG confidence, Domain Classifier, Cumulative Z3 Monitor with MUS, Targeted Regeneration), calibrate confidence thresholds, run experiments across 8+ benchmarks × 6 conditions, complete 4 ablations, and write the paper. Even with the open-source PCFG code from 'Grammars of Formal Uncertainty' (github.com/DebarghaG/grammars-formal-uncertainty), integration and calibration per task domain is non-trivial.\", \"Qwen3-32B baseline AIME performance is not clearly established. The Qwen3 technical report does not report Qwen3-32B dense model scores on AIME 2024/2025 separately from the MoE variants. Without knowing the baseline, it's impossible to assess how much headroom exists for improvement. The proposal should explicitly measure and report the unverified baseline as the first experiment.\", \"PCFG confidence calibration complexity is underestimated. The approach requires: (a) generating K=5 formalizations per step across a calibration set, (b) parsing each as SMT-LIB, (c) fitting PCFG distributions, (d) computing grammar entropy and cross-sample consistency, (e) calibrating thresholds per task domain (math vs. logic vs. hybrid). This is essentially reimplementing a core component of 'Grammars of Formal Uncertainty' within the pipeline.\", \"Tier 2 weak constraints ('numerical value bindings, type constraints, ordering relations extracted via templated regex') may have limited coverage on purely logical tasks (e.g., ProofWriter, FOLIO) where the reasoning steps involve logical deductions rather than numerical computations. The proposal should analyze what fraction of steps on logic benchmarks would yield any Tier 2 constraints.\", \"The domain classifier is described as 'a lightweight classifier fine-tuned on Grammars of Formal Uncertainty task labels' but the training data for this classifier is not specified. How many task-type labels are needed? What is the classifier architecture? Fine-tuning even a small model adds another component to implement and validate within 14 days.\"]\nFeedback: The proposal has made strong improvements from Rounds 1-2 and the core novelty is now verified (interwhen's code confirms no cumulative constraint tracking). Specific actions to reach pass quality:\n\n1. **Add ARC-Challenge** to evaluation benchmarks — this is a hard user requirement. Frame it as a sanity check alongside GPQA Diamond (expect no improvement, confirm no degradation).\n\n2. **De-risk the timeline** by simplifying two components:\n   - Replace the fine-tuned domain classifier with a **rule-based heuristic** (e.g., if benchmark is in {ProofWriter, FOLIO, LogiQA, ZebraLogic, AIME, MATH} → route to Z3; else → skip). This is sufficient for the paper's evaluation since all benchmarks are known in advance. Discuss the learned classifier as future work.\n   - For PCFG confidence, consider a **simpler proxy**: instead of full grammar fitting, use **cross-sample majority consistency** (if ≥4 of 5 formalizations produce equivalent Z3 assertions via syntactic normalization, high confidence; else low). This captures the key signal (consensus = reliable formalization) without PCFG overhead. Discuss full PCFG as an ablation or supplement.\n\n3. **Establish baseline first**: Run Qwen3-32B (no verification) on all benchmarks as the very first experiment. Report these numbers explicitly. This sets the headroom for each benchmark and may reveal that some benchmarks (e.g., MATH-500) are already saturated with this base model.\n\n4. **Analyze Tier 2 coverage on logic benchmarks**: For ProofWriter and FOLIO, the reasoning steps are logical deductions (e.g., 'If A is true and A→B, then B'). These may not yield numerical bindings or ordering relations. Consider extending Tier 2 to include simple propositional constraints (variable truth assignments) that can be extracted with near-100% reliability from logical reasoning steps.\n\n5. **Drop the K=1 vs K=5 supplementary ablation** to save time. The 3 core ablations (two-tier vs. Tier-1-only, online-cumulative vs. online-independent vs. post-hoc, MUS vs. generic retry vs. MCS) are sufficient for the paper.\n\n6. **Prioritize benchmarks**: Given limited time, run the full experiment suite on AIME 2024, AIME 2025, ProofWriter, FOLIO, and ZebraLogic first (where the approach should shine). Add MATH-500, LogiQA, GPQA Diamond, ARC-Challenge, and BBH as secondary if time permits.\n\n### Round 4 review\nVerdict: revise\nIssues: [\"IMPORTANT: The characterization of interwhen is misleading. The proposal claims interwhen 'checks intermediate solutions against fixed problem constraints rather than maintaining cumulative cross-step dependencies.' Verification of interwhen's code and paper shows its fork mechanism extracts the FULL current solution state (e.g., all house-attribute assignments in ZebraLogic), so Z3 checks the complete cumulative state. If step 3 assigns x=7 and step 5 assigns x=12, interwhen catches this. The real distinction is that interwhen uses STATE-LEVEL cumulative checking (works for CSP/structured-state tasks) while the proposal uses ASSERTION-LEVEL cumulative tracking (works for derivation tasks like math proofs where no complete structured state can be extracted). This is a genuine and important distinction — but it must be articulated correctly.\", \"VeriCoT has been accepted at ICLR 2026 (poster), not just arXiv. This should be updated in references and raises the bar for comparison — VeriCoT is now peer-reviewed at a top venue.\", \"'Safe: Enhancing Mathematical Reasoning via Retrospective Step-aware Formal Verification' (ACL 2025, arXiv 2506.04592) does step-aware Lean4 verification of mathematical reasoning and is not cited. It should be included as related work alongside HERMES.\", \"AIME 2024 baseline of ~70% may be conservative. While it matches the EvalScope reproduction, third-party evaluations (llm-stats.com, designforonline.com) report Qwen3-32B at 80-81% on AIME 2024. If the true baseline is 80%, the headroom shrinks from ~30pp to ~20pp. The proposal should either justify the 70% figure (specific eval settings) or acknowledge the range.\", \"HERMES results (97.4% MATH-500, 66.7% AIME'25) are with DeepSeek-V3.1 as the base model, not Qwen3-32B. A fair comparison requires either running HERMES with Qwen3-32B or acknowledging the different base models when comparing. Currently the proposal lists these numbers without clarifying the base model mismatch.\", \"The NeurIPS 2024 paper title is 'Autoformalize Mathematical Statements' (not 'Autoformalizing'), and its equivalence checking uses Z3, CVC5, and Isabelle/HOL — not Z3 alone. The 10.7% improvement is for GPT-4 on miniF2F specifically; broader results show 0.22-1.35x relative improvements.\"]\nFeedback: The proposal has improved substantially over 4 rounds and the core idea is sound. Two actions would bring it to pass quality:\n\n1. **Fix the interwhen distinction** — this is the most important revision. Acknowledge that interwhen achieves cumulative-like checking for structured-state tasks (ZebraLogic, Maze, SpatialMap) because its fork mechanism extracts the full current solution state. Then argue that your assertion-level cumulative tracking handles DERIVATION tasks (mathematical proofs, logical deductions) where no complete structured state can be extracted mid-generation. On AIME, for example, you can't ask the model to 'output your current mathematical state as JSON' — the state IS the chain of derivations. This is actually a stronger novelty claim than 'interwhen doesn't track cumulative constraints' because it identifies a specific class of tasks where your approach provides something interwhen structurally cannot.\n\n2. **Minor updates**: (a) Update VeriCoT to ICLR 2026 poster, (b) cite Safe (ACL 2025) as related work, (c) clarify HERMES base model is DeepSeek-V3.1 not Qwen3-32B, (d) acknowledge AIME 2024 baseline variance (70-81% depending on eval settings) and state your exact evaluation protocol, (e) fix minor reference inaccuracies.\n\n### Round 5 review\nVerdict: revise\nIssues: [\"IMPORTANT (unfixed from Round 4): The interwhen characterization is STILL misleading. The proposal says 'Unlike interwhen, which checks intermediate solutions against fixed problem constraints' — but interwhen extracts the FULL cumulative solution state (e.g., all house-attribute assignments in ZebraLogic) and checks it against constraints, effectively catching cross-step inconsistencies for structured-state tasks. This was explicitly flagged in Round 4 with a specific reframing suggestion (state-level vs assertion-level distinction) that was not implemented.\", \"IMPORTANT: Multiple Round 4 minor fixes were NOT applied: (a) VeriCoT still listed as 'arXiv Nov 2025' instead of ICLR 2026 poster, (b) Safe (ACL 2025, arXiv 2506.04592) still not cited, (c) HERMES results (97.4% MATH-500, 66.7% AIME'25) still not clarified as using DeepSeek-V3.1 base model (not Qwen3-32B), (d) NeurIPS 2024 paper title still 'Autoformalizing' instead of 'Autoformalize', (e) AIME 2024 baseline variance (70% pass@1 vs 80-81% avg@64) not acknowledged with evaluation protocol specification.\", \"Missing related work: 'Adaptive LLM-Symbolic Reasoning via Dynamic Logical Solver Composition' (EACL 2026, arXiv 2510.06774) introduces an adaptive multi-paradigm framework that dynamically selects from Z3/Pyke/Prover9/MiniZinc based on problem type. It explicitly criticizes static, predetermined solver routing — which is exactly what the proposed rule-based domain heuristic does. This paper must be cited and the limitation acknowledged.\", \"VERGE's semantic routing (claim-level LLM-based classification into 6 types → formal vs soft verifier) is not discussed despite being conceptually related to the proposed domain routing. VERGE's ablation shows removing routing drops performance by 8.3% average. The proposal should discuss VERGE's routing and position its rule-based heuristic as a practical simplification with known limitations.\", \"The 10.7% improvement from the NeurIPS 2024 autoformalization paper is misattributed: it comes from the COMBINED method (symbolic equivalence + semantic consistency using Z3, CVC5, and Isabelle/HOL with 12 tactics), not from 'cross-candidate symbolic equivalence checking via Z3' alone. The proposal uses this as validation for its cross-sample Z3-only consistency approach, which is a weaker version of what the paper actually shows.\", \"The novelty framing centers on cumulative constraint tracking as the primary differentiator, but VeriCoT already does exactly this (ℱᵢ = ℱᵢ₋₁ ∪ {Fᵢ}). The two-tier confidence-gated formalization is the actually novel component and should be promoted to the primary contribution, with online timing as secondary.\"]\nFeedback: The proposal has matured well over 5 rounds but has a persistent problem: the interwhen characterization flagged in Round 4 was not fixed, and multiple minor corrections were not applied. These must be addressed — a reviewer seeing incorrect characterizations of closely related work will question the paper's credibility. Specific actions:\n\n1. **Fix interwhen characterization (CRITICAL, Round 3 of asking)**: Replace 'checks intermediate solutions against fixed problem constraints' with an accurate description. Acknowledge that interwhen achieves cumulative-like checking for STRUCTURED-STATE tasks (ZebraLogic, Maze, SpatialMap) because its fork extracts the full current solution state. Then argue your assertion-level cumulative tracking handles DERIVATION tasks (math proofs, logical deductions in ProofWriter/FOLIO) where no complete structured state can be extracted mid-generation — the 'state' IS the chain of derivations. Use a derivation-task example: 'step 3 establishes monotonicity, step 7 applies a bound requiring concavity' rather than 'step 3 derives x=7, step 5 derives x=12' (which interwhen WOULD catch via state extraction).\n\n2. **Apply all Round 4 minor fixes**: (a) VeriCoT → ICLR 2026 poster, (b) cite Safe (ACL 2025), (c) clarify HERMES uses DeepSeek-V3.1, (d) fix title to 'Autoformalize', (e) specify AIME baseline evaluation protocol (EvalScope pass@1, n=1, temp=0.6) and note avg@64 gives ~80-81%.\n\n3. **Cite Adaptive LLM-Symbolic Reasoning (EACL 2026)** and acknowledge that static rule-based routing is a known limitation. Position your heuristic as a practical choice for fixed benchmark evaluation, with the EACL 2026 dynamic approach as the right future direction.\n\n4. **Reframe novelty hierarchy**: Lead with two-tier confidence-gated formalization as the PRIMARY contribution (this is genuinely novel — no prior work combines cross-sample consistency gating with weak constraint fallback for maintaining constraint store informativeness). Position online timing as SECONDARY and cumulative tracking as TERTIARY (since VeriCoT already does it, your contribution is applying it online).\n\n5. **Fix the NeurIPS 2024 citation**: The 10.7% is from the combined method (symbolic equivalence + semantic consistency) using Z3+CVC5+Isabelle, not from Z3-only cross-sample equivalence. Either cite the full method accurately or note that your approach uses a simplified version (Z3-only pairwise equivalence) and the 10.7% is an upper bound from the more complex pipeline.\n\n6. **Discuss VERGE's semantic routing** as related work and explain why your simpler approach is sufficient for your evaluation setup (all benchmarks known in advance) while acknowledging VERGE's claim-level routing is more general.\n\n### Round 6 review\nVerdict: revise\nIssues: [\"NEW ISSUE: 'Do LLMs Game Formalization?' (arXiv 2604.19459, April 2026) demonstrates that LLMs systematically mistranslate premises during formalization, producing internally consistent but unfaithful outputs that 'evade detection entirely.' This directly undermines the cross-sample consistency mechanism: if Qwen3-14B consistently makes the same formalization error across all K=5 samples, the system assigns HIGH confidence to an incorrect formalization, introducing false positives into the cumulative constraint store. The proposal acknowledges this risk in a risk_note but relegates mitigation to 'roundtrip spot-checking in supplementary analysis' — this should be promoted to a core defense mechanism or at minimum discussed as a known limitation with quantified expected impact.\", \"ZebraLogic is listed as a prioritized benchmark where 'the approach should add most value,' but the proposal itself acknowledges that (a) interwhen's state-extraction works well on ZebraLogic (structured-state task), and (b) 'Tier 2 propositional constraint extraction may have limited yield on ZebraLogic (which involves constraint satisfaction rather than propositional deduction).' This creates a contradictory expectation — either reposition ZebraLogic as a baseline-comparison benchmark (where interwhen should match or outperform) or explain specifically why assertion-level cumulative tracking adds value beyond interwhen's state extraction on this task.\", \"The empirical outcome risk is inadequately addressed. The two-tier mechanism's value proposition rests on a chain of assumptions: (1) Tier 1 confidence correctly distinguishes good from bad formalizations, (2) Tier 2 weak constraints are informative enough to catch real cross-step errors, (3) the cumulative constraint store with mixed Tier-1/Tier-2 constraints provides enough coverage for MUS to identify meaningful conflicts. If any link fails — e.g., if Tier 2 constraints on AIME problems are limited to trivial bindings like 'n is a positive integer' that rarely conflict — the system reduces to checking only the easy steps. The proposal should identify a minimum viable validation: what specific error type on AIME/ProofWriter would demonstrate the two-tier mechanism's value?\", \"The 14-day timeline has no fallback plan. If debugging the formalizer-confidence-gate-Z3 pipeline takes 7+ days, there may not be enough time for the full experimental suite (8 benchmarks × 6 conditions × 3 ablations). The proposal should specify a minimum publishable result set: which 2-3 benchmarks and which 2-3 comparisons constitute the core claim, and which are stretch goals.\"]\nFeedback: The proposal has made excellent progress — ALL Round 5 issues are now fixed, and the interwhen characterization (flagged since Round 3) is finally accurate. The core idea is sound and the contribution hierarchy is clear. To reach pass quality:\n\n1. **Address systematic formalization errors in the core method**: Cite 'Do LLMs Game Formalization?' (arXiv 2604.19459, April 2026) and discuss how cross-sample consistency handles (or fails to handle) systematic mistranslations. Consider promoting roundtrip verification from supplementary to a lightweight Tier 1 validation step — generate K=5 formalizations, check cross-sample consistency, then roundtrip-verify the majority candidate back to NL and compare with the original step. This adds one informalization call per high-confidence step but catches systematic errors. If this is too expensive, at minimum quantify the expected rate of systematic errors on your benchmarks and argue that Tier 2 fallback provides a safety net.\n\n2. **Reposition ZebraLogic**: Move ZebraLogic from 'prioritized' to 'comparison' category. On ZebraLogic, interwhen's state-extraction should work well, and the experiment should validate that your approach matches (not necessarily exceeds) interwhen on structured-state tasks while excelling on derivation tasks (AIME, ProofWriter, FOLIO). This actually strengthens the paper's narrative: your approach fills a gap for derivation tasks, not a replacement for interwhen on structured-state tasks.\n\n3. **Define minimum viable experiment**: Specify: 'The core publishable claim requires comparing online-cumulative (ours) vs. online-independent (interwhen-style) vs. post-hoc-cumulative (VeriCoT-style) vs. no-verification on AIME 2024 + ProofWriter + FOLIO, with the two-tier vs. Tier-1-only ablation. This constitutes 4 conditions × 3 benchmarks × 2 ablation levels = 24 runs, achievable in ~60 H100-hours. The remaining benchmarks and ablations are stretch goals.' This de-risks the timeline without sacrificing the core contribution.\n\n4. **Strengthen novelty framing**: Add a brief formal characterization of the informativeness-precision tradeoff. Define constraint store informativeness (fraction of steps with at least one constraint) and constraint store precision (fraction of constraints that are correct). Tier 1 optimizes for precision (high threshold), Tier 2 optimizes for informativeness (near-100% correct by construction). The two-tier mechanism explicitly manages this tradeoff. This elevates the contribution from an engineering trick to a principled framework.\n\n\n## Output format\nOutput ONLY a JSON object:\n{\n  \"verdict\": \"pass | revise | fail\",\n  \"scores\": {\n    \"novelty\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"feasibility\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"clarity\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"impact\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"}\n  },\n  \"issues\": [\"specific issue 1\", \"specific issue 2\", ...],\n  \"feedback\": \"Actionable feedback for the generator (if verdict=revise)\",\n  \"reason\": \"One-line summary of verdict rationale\"\n}\n\nRules:\n- \"pass\": idea is sound AND high quality — avg score >= 4.0, no critical issues\n- \"revise\": fixable issues OR scores below threshold — provide specific feedback\n- \"fail\": fundamental flaw (e.g., gap doesn't exist, approach provably wrong, or scores remain low after multiple revisions)\n- Threshold is HIGH (4.0/5.0): agent scores tend to be inflated, so only truly outstanding ideas should pass. An avg of 3.5 is NOT enough.\n- Round 10 only: if still \"revise\", you MUST choose \"pass\" or \"fail\"."
}
```

---

### Runtime record

_source line 2 · 2026-05-12T00:44:37.807Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-12T00:44:37.807Z",
  "sessionId": "ae8c16f5-ce1c-4bce-923e-3afb8499b025"
}
```

---

## Round 1

46 recorded events

### User

_source line 3 · 2026-05-12T00:44:37.842Z_

You are a strict ML research reviewer conducting adversarial review.

**Today's date: 2026-05-11 (UTC).**

Your job: independently verify this idea's claims via WebSearch, then issue a verdict.

## User requirements
The user asked for: **Target: EMNLP 2026, ARR submission deadline 2026-05-25 (16 days from today 2026-05-09). Track: NLP and Symbolic Reasoning.

Direction: Neurosymbolic reasoning — combining neural models with symbolic systems (logic programs, knowledge graphs, formal verification, constraint solvers). NOT limited to LLM-only reasoning — explicitly seek methods that integrate external symbolic components. Also in-scope: structured mathematical reasoning, program-aided reasoning, theorem prover integration.

Contribution type: METHOD ONLY. Must propose a new hybrid algorithm, training objective, or inference pipeline that combines neural + symbolic components. Pure prompting tricks (vanilla CoT, self-consistency) are out of scope.

HARD CONSTRAINTS:
1. Compute: ≤200 H100-hours total. Neurosymbolic methods are often inference-heavy not training-heavy — budget accordingly.
2. Time: ≤16 days. Use existing open checkpoints (Qwen3, Llama-3.x, DeepSeek-R1 distills) + off-the-shelf solvers (Z3, Prolog, SymPy, Lean4).
3. Eval: MATH, AIME 2024/2025, GPQA Diamond, ProofWriter, FOLIO, LogiQA, ARC-Challenge, BBH.

Look for: lightweight symbolic verifiers as post-hoc filters, neural-guided symbolic search, structured output → formal checker pipelines, hybrid neuro-symbolic distillation. Avoid: pure prompt engineering, vanilla CoT.

Tag: direction=neurosymbolic_reasoning, contribution_type=method. target_venues=["EMNLP 2026 Main", "EMNLP 2026 Findings"].**
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
4. **Venue validity**: Are target_venues' submission deadlines after 2026-05-11?
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

## Idea under review (round 7/10)
{
  "title": "Two-Tier Confidence-Gated Formalization with Roundtrip Validation and Cumulative Online Constraint Tracking for Multi-Step Reasoning Verification",
  "core_problem": "In multi-step reasoning, errors introduced at step k propagate to steps k+1...n, creating cascading failures. Online verification systems have emerged to catch errors during generation: interwhen (Microsoft, Feb 2026) achieves effective cumulative-like checking for structured-state tasks (ZebraLogic, Maze, SpatialMap) by forking inference to extract the full current solution state and verifying it against constraints via Z3. However, for derivation tasks — mathematical proofs and logical deduction chains (ProofWriter, FOLIO, AIME) — no compact solution state exists to extract mid-generation; the verification state IS the accumulated chain of derived assertions. VeriCoT (ICLR 2026 poster) maintains cumulative Z3 assertion tracking for derivation tasks but operates only post-hoc. Beyond the online-vs-post-hoc and state-vs-assertion distinctions, all verification systems face a formalization bottleneck with two failure modes: (1) formalization failure — NL-to-formal translation fails outright (HERMES reports >60% autoformalization failure at Kₜ=1 with DeepSeek-V3.1), leaving the constraint store sparse and uninformative; and (2) systematic unfaithfulness — 'Do LLMs Game Formalization?' (arXiv 2604.19459, April 2026) demonstrates that LLMs systematically mistranslate premises during formalization, producing internally consistent but unfaithful outputs that 'evade detection entirely.' Cross-sample consistency alone cannot catch systematic errors because all K samples may converge on the same incorrect formalization. Can a two-tier confidence-gated formalization system — with roundtrip validation to catch systematic errors at Tier 1, and weak but near-100%-reliable constraints at Tier 2 — maintain both constraint store informativeness and precision during online verification of derivation tasks?",
  "opportunity": "A convergence of recent findings creates the opportunity for a principled solution to the formalization bottleneck in online reasoning verification. interwhen (Microsoft, Feb 2026) demonstrates that online Z3 verification during generation improves accuracy by up to 15pp on structured-state tasks. However, for derivation tasks — where reasoning progresses through chains of intermediate lemmas — interwhen's state-extraction paradigm does not apply. VeriCoT (ICLR 2026 poster) validates that cumulative assertion tracking catches cross-step inconsistencies in derivation tasks, but operates post-hoc. HERMES achieves online Lean4 verification but with >60% autoformalization failure at Kₜ=1. Crucially, 'Do LLMs Game Formalization?' (arXiv 2604.19459, April 2026) reveals a deeper threat: systematic premise mistranslation that produces internally consistent but unfaithful formalizations, evading detection by cross-sample consistency, LLM-as-judge, and rule-based diff. This means cross-sample consistency is necessary but insufficient for formalization confidence — a complementary faithfulness check is needed. 'Faithful Autoformalization via Roundtrip Verification and Repair' (arXiv 2604.25031, April 2026) demonstrates that roundtrip verification (formalize → informalize → re-formalize → Z3 equivalence) raises formal equivalence from 45-61% to 83-85%, with Z3 equivalence checks resolving in <1 second. ReForm (arXiv 2510.24592) shows that reflective self-validation during autoformalization achieves +22.6pp average improvement. 'Autoformalize Mathematical Statements by Symbolic Equivalence and Semantic Consistency' (NeurIPS 2024) validates cross-sample consistency as a useful signal (combined method achieves 45.8% on MATH, 8.3% absolute improvement). The unexploited combination is: (1) two-tier confidence-gated formalization with roundtrip validation — cross-sample consistency for candidate selection, roundtrip verification to catch systematic errors, and weak constraint fallback when confidence is low — that manages the informativeness-precision tradeoff explicitly (PRIMARY novelty), (2) online assertion-level cumulative tracking for derivation tasks (SECONDARY), and (3) MUS-guided targeted regeneration (TERTIARY). We formalize this as an informativeness-precision tradeoff: define constraint store informativeness I(C) = fraction of steps with ≥1 constraint, and precision P(C) = fraction of semantically correct constraints. Without gating: I≈1.0, P≈0.4-0.6. With Tier 1 only: I≈0.5, P≈0.9. With two-tier + roundtrip: I≈0.95, P≈0.85-0.95. This principled framework is the first to explicitly manage the informativeness-precision tradeoff in online reasoning verification.",
  "landscape": "**Online verification systems**: interwhen (Microsoft, arXiv 2602.11202, Feb 2026) introduces the 'LLM-Process-Modulo' paradigm — periodically polling the reasoning trace, forking inference to recover intermediate solutions, and running Z3 asynchronously. For structured-state tasks (ZebraLogic, Maze, SpatialMap, Game24, Verina), it converts the model's structured output into a representation checked for logical consistency using Z3, effectively achieving cumulative-like checking by extracting the full accumulated solution state at each fork point. On ZebraLogic X-Large, it achieves +10.4pp with Qwen3-30B-A3B. However, for derivation tasks (math proofs, logical deductions), there is no compact solution state to extract. HERMES (arXiv 2511.18760, Nov 2025) interleaves informal reasoning with Lean4 verification, achieving 97.4% on MATH-500 and 66.7% on AIME'25 with DeepSeek-V3.1, but with >60% autoformalization failure at Kₜ=1.\n\n**Post-hoc verification systems**: VeriCoT (ICLR 2026 poster, arXiv 2511.04662) autoformalizes each step into FOL, maintains cumulative Z3 constraints (ℱᵢ = ℱᵢ₋₁ ∪ {Fᵢ}), and checks entailment/contradiction — pioneering cumulative assertion tracking for derivation tasks but post-hoc only. VERGE (arXiv 2601.20055, Jan 2026) uses LLM-based claim-level semantic routing across 6 types and MCS-based error localization, achieving 18.7% average uplift. Its ablation shows routing is essential: removing it causes -8.3% average degradation (HLE halving from 30.5% to 15.2%). Safe (ACL 2025, arXiv 2506.04592) performs step-aware Lean4 verification but does not address formalization confidence.\n\n**Formalization faithfulness — the systematic error problem**: 'Do LLMs Game Formalization?' (arXiv 2604.19459, April 2026) uses a two-stage pipeline (formalization then proof over locked formalization) to expose model-specific gaming behaviors. GPT-5 fabricates axioms during proof generation (107 instances, 56.2% conclusion-as-axiom), which IS detectable via cross-stage comparison. But DeepSeek-R1 mistranslates premises during formalization itself, producing internally consistent outputs that evade ALL tested detection methods — cross-stage comparison, LLM-as-judge (Claude Opus 4.5), and rule-based diff. This directly threatens cross-sample consistency mechanisms: if the formalizer consistently makes the same semantic error across all K samples, high consistency is assigned to an incorrect formalization. The paper evaluates on 303 FOL problems (FOLIO + Multi-LogiEval) with compilation rates of 87-99% despite substantial unfaithfulness.\n\n**Formalization reliability and roundtrip defenses**: 'Faithful Autoformalization via Roundtrip Verification and Repair' (arXiv 2604.25031, April 2026) demonstrates that roundtrip verification (formalize → informalize → re-formalize → Z3 equivalence check, <1s per check) raises formal equivalence from 45-61% to 83-85%, with diagnosis-guided repair requiring only 7.21 LLM calls per repair vs. 12.27 for random baseline. ReForm (arXiv 2510.24592, ICLR 2026 submission) interweaves autoformalization with semantic self-validation, achieving +22.6pp average improvement across four benchmarks. 'Autoformalize Mathematical Statements by Symbolic Equivalence and Semantic Consistency' (NeurIPS 2024, arXiv 2410.20936) validates cross-sample consistency: combined method (Z3/CVC5 + Isabelle/HOL) achieves 45.8% on MATH (8.3% absolute improvement); symbolic equivalence alone achieves 42.0% (4.5% absolute). 'Grammars of Formal Uncertainty' (NeurIPS 2025, arXiv 2505.20047) achieves AUROC >0.93 for detecting formalization errors on logic tasks but shows SMT helps on logic (+34.8%) while hurting on factual tasks (-44.5%).\n\n**Domain-aware routing**: Adaptive LLM-Symbolic Reasoning (EACL 2026, arXiv 2510.06774) demonstrates dynamic solver selection from Z3/Pyke/Prover9/MiniZinc outperforms static approaches, with LLMs achieving >90% solver prediction accuracy.\n\n**The gap**: No system combines (1) confidence-gated formalization with both cross-sample consistency AND roundtrip validation to catch systematic errors, plus weak constraint fallback for maintaining informativeness — explicitly managing the informativeness-precision tradeoff (PRIMARY), (2) online assertion-level cumulative tracking for derivation tasks (SECONDARY), and (3) MUS-guided targeted regeneration (TERTIARY). The 'Do LLMs Game Formalization?' paper makes roundtrip validation a necessity, not a luxury — cross-sample consistency alone is vulnerable to systematic mistranslation.",
  "approach": "Build a three-component pipeline — Reasoner, Two-Tier Confidence-Gated Formalizer with Roundtrip Validation, and Cumulative Online Constraint Monitor — that operates incrementally during chain-of-thought generation.\n\n**Formal Framework: Informativeness-Precision Tradeoff**. We define two metrics for constraint store quality: (a) **Informativeness** I(C) = |{i : C(sᵢ) ≠ ∅}| / n — the fraction of reasoning steps with at least one constraint in the store. (b) **Precision** P(C) = |{c ∈ ∪C(sᵢ) : c is semantically faithful}| / |∪C(sᵢ)| — the fraction of constraints that faithfully represent the original NL step. Without gating (accept all formalizations): I ≈ 1.0, P ≈ 0.4-0.6. With Tier 1 only (skip low-confidence steps): I ≈ 0.4-0.6, P ≈ 0.85-0.95. With Tier 2 fallback: I ≈ 0.95-1.0, P ≈ 0.85-0.95. The two-tier mechanism with roundtrip validation explicitly manages this tradeoff: Tier 1 + roundtrip optimizes for precision (high threshold, systematic error detection), Tier 2 optimizes for informativeness (near-100% correct by construction). We evaluate both metrics empirically and report the Pareto frontier across configurations.\n\n**Reasoner**: Qwen3-32B in thinking mode. Baseline performance (thinking mode, pass@1): AIME'24 ~70%, AIME'25 ~76.7%, MATH-500 ~95.2%.\n\n**Two-Tier Confidence-Gated Formalizer with Roundtrip Validation (PRIMARY CONTRIBUTION)**:\n\n- **Tier 1 (Full formalization with roundtrip validation)**: Generate K=5 candidate formalizations per step in SMT-LIB using Qwen3-14B. Compute confidence via cross-sample majority consistency: normalize candidates syntactically, then check pairwise symbolic equivalence using Z3. If ≥4/5 candidates are equivalent, the majority candidate proceeds to **roundtrip validation**: (i) informalize the majority formalization back to NL using Qwen3-14B (1 LLM call), (ii) compare the back-translated NL against the original reasoning step via an NLI-style entailment check (1 LLM call, or combined into a single call: 'Translate this formal statement back to English. Is the result semantically equivalent to: [original step]? Answer YES/NO with brief justification.'). If roundtrip confirms faithfulness → accept as Tier 1. If roundtrip detects semantic drift → downgrade to Tier 2 even though cross-sample consistency was high. This directly addresses the systematic mistranslation threat identified by 'Do LLMs Game Formalization?': even when all K samples agree on an incorrect formalization, the roundtrip back to NL exposes semantic divergence from the original step. The roundtrip approach is inspired by arXiv 2604.25031 (which raises formal equivalence from 45-61% to 83-85%), adapted as a lightweight single-call validation rather than a full multi-iteration repair pipeline. **Cost**: +1 LLM call per high-confidence step (combined informalization + NLI check), amortized only over steps that pass cross-sample consistency (~50-60% of steps). **Known limitation**: If the same model systematically produces the same NL interpretation during both formalization and informalization, roundtrip may not catch the error. We quantify this residual risk empirically by measuring the rate of roundtrip-undetected systematic errors using a held-out set of manually annotated formalization pairs (50 steps each from AIME, ProofWriter, FOLIO). We expect this rate to be low based on the roundtrip paper's results (83-85% equivalence after roundtrip), but report it transparently.\n\n- **Tier 2 (Weak constraints)**: When Tier 1 confidence falls below threshold OR roundtrip validation fails, extract weaker but near-100%-reliable constraints via templated patterns from the NL step. For **math/arithmetic steps**: numerical value bindings (x = 15), type constraints (is_integer, is_positive), ordering relations (x > y), simple arithmetic identities. For **logical reasoning steps**: truth value assignments (A = True), simple propositional entailments (P → Q), predicate-argument bindings (Dog(X) = True), negation patterns (Kind(A) = False). Tier 2 precision is near-100% by construction (simple pattern matching on surface forms), ensuring I(C) remains high without degrading P(C).\n\n**Minimum Viable Validation — Specific Error Types**: The two-tier mechanism's value is demonstrated by catching specific cross-step error patterns that require both Tier 1 and Tier 2 constraints:\n- **AIME**: Step 3 establishes 'let n = 15' (Tier 2 if full formalization fails: n = 15, is_integer(n)). Step 7 derives 'n² = 225' (Tier 1 or 2). Step 9 erroneously claims 'n² = 216' → UNSAT with constraints from steps 3 and 7. Without Tier 2, if step 3's full formalization failed, no constraint on n exists and the error propagates.\n- **ProofWriter**: Step 1 establishes 'If something is big and round then it is nice' (Tier 2: Big(x) ∧ Round(x) → Nice(x)). Step 3: 'Bob is big and round' (Tier 2: Big(Bob), Round(Bob)). Step 5 claims 'Bob is not nice' → UNSAT. These propositional patterns are exactly what Tier 2 captures reliably.\n- **FOLIO**: Step 1: 'All students who study hard pass' (Tier 2: Student(x) ∧ StudyHard(x) → Pass(x)). Step 3: 'Alice studies hard' (Tier 2: StudyHard(Alice)). Step 5: 'Alice fails' → UNSAT.\nWe measure: (a) how many such cross-step errors exist in baseline generations, (b) what fraction are caught by Tier 1 alone vs. Tier 1+2, (c) what fraction require Tier 2 constraints specifically (the delta is the two-tier mechanism's marginal value).\n\n**Domain-Aware Routing via Rule-Based Heuristic**: Benchmark-level rule-based heuristic: {AIME, MATH-500, ProofWriter, FOLIO, LogiQA} → Z3 verification; {ARC-Challenge, GPQA Diamond, BBH} → LLM reasoning only. Sufficient for fixed benchmark evaluation; dynamic instance-level routing (following EACL 2026 / VERGE) is a clear future direction.\n\n**Cumulative Online Constraint Monitor (SECONDARY CONTRIBUTION)**: Maintains a cumulative incremental Z3 solver context at the assertion level for derivation tasks. After each formalization (Tier 1 or Tier 2), assertions are pushed and check-sat is called (<100ms for linear arithmetic). If UNSAT:\n- Extract MUS via Z3's unsat-core API.\n- Map conflicting assertions to originating steps.\n- Pop the conflicting step's scope.\n- Provide the Reasoner with a structured constraint-violation prompt containing the specific conflicting constraints.\n- Regenerate the violating step with explicit feedback. If UNSAT persists after 3 attempts, fall back to regenerating from the earliest conflicting step in the MUS.\n\n**Central Experiment — Minimum Publishable Result Set**: The core claim requires comparing 4 conditions on 3 benchmarks:\n1. **Online-Cumulative (ours)**: Two-tier confidence-gated formalization with roundtrip validation + cumulative assertion tracking.\n2. **Online-Independent (interwhen-style)**: Online Z3 checking against problem constraints only, without cumulative tracking.\n3. **Post-hoc-Cumulative (VeriCoT-style)**: Cumulative Z3 checking applied after full chain with self-reflection.\n4. **No-verification baseline**: Qwen3-32B thinking mode.\nOn 3 core benchmarks: **AIME 2024, ProofWriter, FOLIO**.\nWith 1 core ablation: **Two-tier (Tier 1 + Tier 2) vs. Tier-1-only** (measuring Tier 2's marginal contribution to informativeness and error detection).\nThis constitutes 4 conditions × 3 benchmarks × 2 ablation levels = **24 runs, achievable in ~60 H100-hours (~5 days)**.\n\n**Stretch goals** (if time permits):\n- Additional benchmarks: AIME 2025, MATH-500 (near-saturated), ZebraLogic (comparison benchmark — expect to MATCH interwhen, validating no degradation on structured-state tasks), GPQA Diamond (sanity check, expect no improvement).\n- Additional baselines: HERMES (online Lean4, noting different base model), VERGE (post-hoc MCS), majority voting (k=8).\n- Additional ablations: MUS-guided vs. generic retry vs. MCS-guided feedback; roundtrip validation ON vs. OFF.\n\n**ZebraLogic Positioning**: ZebraLogic is repositioned as a **comparison benchmark**, not a prioritized one. On ZebraLogic, interwhen's state-extraction achieves +10.4pp (X-Large, Qwen3-30B-A3B) and should perform well because it is a structured-state task. Our approach should **match** interwhen on ZebraLogic, validating that assertion-level tracking does not degrade performance on structured-state tasks, while **exceeding** interwhen and VeriCoT on derivation tasks (AIME, ProofWriter, FOLIO) where state extraction cannot apply. This strengthens the paper's narrative: our approach fills a complementary gap for derivation tasks, not a replacement for interwhen on structured-state tasks.\n\nMeasure: (a) error cascade length, (b) total regeneration cost, (c) downstream accuracy, (d) wall-clock latency, (e) false positive rate, (f) constraint store informativeness I(C), (g) constraint store precision P(C).",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "~150h H100-80GB",
      "gpu_utilization": "Low (~25%). GPUs idle during confidence calibration and formalization error analysis.",
      "timeline": "2-2.5 months",
      "team": "1-2 researchers (one NLP/LLM, one with SMT/constraint programming experience)",
      "estimated_gpu_cost": "$450-600 (at ~$3-4/hr H100 spot)"
    },
    "human_in_loop": {
      "gpu_hours": "~120h H100-80GB",
      "gpu_utilization": "Moderate (~55%). Agent runs experiments between check-ins.",
      "timeline": "3-5 weeks",
      "team": "1 researcher, ~30-40min/day reviewing formalization quality, confidence calibration, and Tier 2 template coverage",
      "claude_api_cost": "$100-180 (1000-1800 turns)",
      "estimated_gpu_cost": "$360-480",
      "risk_note": "Tier 2 propositional constraint templates for logic benchmarks need manual validation on ~50 sample steps from ProofWriter/FOLIO. Roundtrip validation residual error rate needs manual annotation on 150 steps (50 per core benchmark)."
    },
    "auto_research": {
      "gpu_hours": "~180h H100-80GB (Qwen3-32B on 2 H100s + Qwen3-14B on 1 H100 = 3 H100s per experiment; +10h for roundtrip validation overhead)",
      "gpu_utilization": "High (~80%). Continuous inference pipeline; Z3 calls <100ms; roundtrip adds ~1 Qwen3-14B call per Tier 1 step.",
      "timeline": "10-14 days with 4 H100s available. FALLBACK: If pipeline debugging takes >7 days, execute minimum publishable result set only (4 conditions × 3 benchmarks × 2 ablation = 24 runs, ~60 H100-hours, ~5 days). Stretch benchmarks and ablations deferred to camera-ready.",
      "team": "0 (initial setup + final review)",
      "claude_api_cost": "$200-350 (2000-3500 turns)",
      "estimated_gpu_cost": "$540-720",
      "speed_bottleneck": "Formalizer throughput: K=5 samples per step × ~500 tokens/sample for Qwen3-14B + 1 roundtrip call (~300 tokens) per high-confidence step. With vLLM batching on 1 H100, ~3000 tok/s → ~1.0s per step's formalization set including roundtrip. Cross-sample equivalence checking via Z3 adds <50ms.",
      "risk_note": "Systematic formalization errors (per arXiv 2604.19459) may partially evade roundtrip detection if the same model performs both formalization and informalization. Mitigation: quantify residual rate on 150 manually annotated steps. If residual rate exceeds 15%, consider using a different model (e.g., Qwen3-8B) for informalization to break the systematic error pattern.",
      "timeline_derisking": "Core result set (24 runs, ~60 H100-hours) is achievable in 5 days even with significant debugging time. Stretch goals add ~120 H100-hours over 5-9 additional days. Prioritized benchmark ordering: AIME'24 first (highest expected improvement), then ProofWriter + FOLIO (logic benchmarks demonstrating Tier 2 value), then stretch benchmarks."
    }
  },
  "target_venues": [
    "EMNLP 2026 (ARR deadline May 25, 2026)",
    "AAAI 2027 (deadline ~August 1, 2026)",
    "ICLR 2027 (deadline ~September-October 2026)"
  ],
  "level": "solid",
  "key_references": [
    "interwhen: A Generalizable Framework for Verifiable Reasoning with Test-time Monitors (Microsoft, arXiv 2602.11202, Feb 2026)",
    "VeriCoT: Neuro-symbolic Chain-of-Thought Validation via Logical Consistency Checks (ICLR 2026 poster, arXiv 2511.04662)",
    "HERMES: Towards Efficient and Verifiable Mathematical Reasoning in LLMs (arXiv 2511.18760, Nov 2025) — base model: DeepSeek-V3.1",
    "VERGE: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning (arXiv 2601.20055, Jan 2026)",
    "Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning (arXiv 2604.19459, April 2026)",
    "Faithful Autoformalization via Roundtrip Verification and Repair (arXiv 2604.25031, April 2026)",
    "ReForm: Reflective Autoformalization with Prospective Bounded Sequence Optimization (arXiv 2510.24592)",
    "Safe: Enhancing Mathematical Reasoning in Large Language Models via Retrospective Step-aware Formal Verification (ACL 2025, arXiv 2506.04592)",
    "Adaptive LLM-Symbolic Reasoning via Dynamic Logical Solver Composition (EACL 2026, arXiv 2510.06774)",
    "Grammars of Formal Uncertainty: When to Trust LLMs in Automated Reasoning Tasks (NeurIPS 2025, arXiv 2505.20047)",
    "Autoformalize Mathematical Statements by Symbolic Equivalence and Semantic Consistency (NeurIPS 2024, arXiv 2410.20936)",
    "Efficient PRM Training Data Synthesis via Formal Verification [FoVer] (ACL 2026 Findings, arXiv 2505.15960)",
    "ProcessBench: Identifying Process Errors in Mathematical Reasoning (ACL 2025)",
    "Beyond Correctness: Exposing LLM-generated Logical Flaws via Multi-step Automated Theorem Proving [MATP] (ICSE 2026)"
  ],
  "description": "We propose a two-tier confidence-gated formalization system with roundtrip validation for online multi-step reasoning verification, targeting derivation tasks (mathematical proofs, logical deduction chains) where existing online verification approaches cannot apply their state-extraction paradigm. We ground our approach in a formal informativeness-precision tradeoff: define constraint store informativeness I(C) as the fraction of steps with ≥1 constraint, and precision P(C) as the fraction of semantically faithful constraints. Without gating: I≈1.0, P≈0.4-0.6 (many wrong constraints cause false positives). With Tier 1 only: I≈0.5, P≈0.9 (sparse store misses errors). Our two-tier mechanism achieves I≈0.95, P≈0.85-0.95 by construction. Our PRIMARY contribution is a two-tier confidence gate with roundtrip validation: Tier 1 uses cross-sample majority consistency (≥4/5 Z3-equivalent candidates) for candidate selection, followed by a lightweight roundtrip validation step (informalize back to NL, check semantic equivalence with original step — 1 additional LLM call) that catches systematic formalization errors identified by 'Do LLMs Game Formalization?' (arXiv 2604.19459). When roundtrip detects semantic drift, the step is downgraded to Tier 2 even if cross-sample consistency was high. Tier 2 extracts weaker but near-100%-reliable constraints — numerical bindings for math steps, truth value assignments and propositional entailments for logic steps — keeping the constraint store informative when full formalization fails or is unfaithful. Specific error types demonstrating value: on AIME, Tier 2 catches arithmetic propagation errors (step 3: n=15, step 9: n²=216 → UNSAT); on ProofWriter, Tier 2 catches transitive reasoning violations (Big(Bob) ∧ Round(Bob) with Big∧Round→Nice, then ¬Nice(Bob) → UNSAT). Our SECONDARY contribution extends VeriCoT's post-hoc cumulative Z3 assertion tracking to online generation for derivation tasks where interwhen's state-extraction does not work. Our TERTIARY contribution uses MUS-guided targeted regeneration. ZebraLogic is repositioned as a comparison benchmark: we expect to match interwhen (which achieves +10.4pp on X-Large via state extraction) on structured-state tasks while exceeding it on derivation tasks, strengthening the narrative that our approach fills a complementary gap. The minimum publishable result set is 4 conditions (online-cumulative ours, online-independent interwhen-style, post-hoc-cumulative VeriCoT-style, no-verification) × 3 core benchmarks (AIME 2024, ProofWriter, FOLIO) × 2 ablation levels (two-tier vs. Tier-1-only) = 24 runs in ~60 H100-hours, with remaining benchmarks and ablations as stretch goals. Timeline fallback: if debugging exceeds 7 days, execute only the minimum publishable set (~5 days). Evaluation uses Qwen3-32B in thinking mode with domain-aware rule-based routing (Z3 for math/logic benchmarks, LLM-only for factual benchmarks).",
  "project_name": "two_tier_gated_verify",
  "source": "web_research"
}


## Previous review history
### Round 1 review
Verdict: revise
Issues: ["CRITICAL: The novelty claim is built on a factual error about VeriCoT. VeriCoT already maintains cumulative Z3 constraints (ℱᵢ = ℱᵢ₋₁ ∪ {Fᵢ}) and checks cross-step consistency (ℱᵢ₋₁ ⊧ ¬Fᵢ). The generator's claim that VeriCoT 'checks entailment from premises and prior steps, but entailment checking is different from cumulative consistency checking' is directly contradicted by VeriCoT's paper.", "HERMES (Nov 2025) already does online verification during LLM generation with a memory module for proof continuity across multi-step chains, addressing the 'online vs post-hoc' differentiation the generator claims as novel.", "VERGE (Jan 2026) already uses Minimal Correction Subsets (MCS) for precise error localization, which is functionally equivalent to the proposed MUS-based error localization via Z3 unsat-core.", "NL-to-Z3 translation accuracy is a critical bottleneck: recent benchmarks show ~71% accuracy for NL-to-formal-logic translation. A ~30% formalization error rate would generate spurious UNSAT results (false positives) that trigger unnecessary regeneration of correct steps, potentially degrading performance below baselines.", "Evaluation benchmarks don't match user requirements. User specified: MATH, AIME 2024/2025, GPQA Diamond, ProofWriter, FOLIO, LogiQA, ARC-Challenge, BBH. Proposal only evaluates on: ProcessBench, MATH-500, ProofWriter — missing 6 of 8 required benchmarks.", "Compute budget mismatch: DeepSeek-R1 (671B) requires 8+ H100s minimum. Combined with Qwen-72B formalizer, running evaluations + ablations on multiple benchmarks would likely exceed the 200 H100-hour constraint. The auto_research estimate of 700 A100-hours (~450 H100-hours) explicitly exceeds the budget by 2.25x.", "The proposal does not address the false positive problem: when Z3 reports UNSAT due to an incorrect formalization (not a real reasoning error), the system would incorrectly force regeneration of a correct step, potentially introducing new errors.", "Missing comparison with HERMES (Lean-based online verification + memory module) as a baseline, which is the most directly relevant competitor for the 'online verification during generation' claim."]
Feedback: The idea has a kernel of merit (online incremental constraint checking with targeted regeneration) but the novelty framing needs a complete overhaul. Specific actions to revise:

1. **Fix the VeriCoT characterization**: Acknowledge that VeriCoT already does cumulative Z3 consistency checking. Reframe the contribution as: VeriCoT operates post-hoc (verify-then-reflect on the complete chain), while your approach intervenes mid-generation before downstream steps compound the error. The real novelty is the *timing* of intervention (online, not post-hoc) and *granularity* of correction (single-step targeted regeneration with MUS feedback, not full chain self-reflection).

2. **Add HERMES as a key baseline**: HERMES does online verification with Lean. Your approach should differentiate by using Z3 (broader constraint language, faster for arithmetic) vs. Lean (more expressive but slower). This is a meaningful tradeoff to discuss.

3. **Address the NL-to-Z3 formalization bottleneck head-on**: Propose a calibration mechanism to estimate formalization confidence. When confidence is low, skip Z3 checking for that step rather than risk false positives. Consider using MATH-VF's Solution Graph (sparse dependency tracking) to reduce what needs to be formalized.

4. **Match evaluation benchmarks to user requirements**: Add AIME 2024/2025, GPQA Diamond, FOLIO, LogiQA, ARC-Challenge, BBH. Note that the approach may only benefit math/logic domains — candidly scope the evaluation.

5. **Use distilled models to fit compute budget**: Switch to DeepSeek-R1-Distill-Qwen-32B (fits on 2 H100s, scores 72.6% on AIME 2024) and a smaller formalizer (Qwen-2.5-14B or fine-tuned 7B). Re-estimate costs in H100-hours explicitly.

6. **Quantify the 'online vs post-hoc' advantage**: Design an experiment showing that intervening at step k prevents error cascading in steps k+1...n, while post-hoc approaches (VeriCoT) detect the error but incur the cascade cost. This is the real value proposition — make it the central experiment.

### Round 2 review
Verdict: revise
Issues: ["CRITICAL: interwhen (Microsoft, Feb 2026, arXiv 2602.11202) is not cited. This paper already demonstrates online verification during LLM reasoning generation using Z3 SMT solver for logic/spatial tasks, with asynchronous verifier execution and trajectory interruption only on error detection — achieving up to 15pp accuracy improvement. This directly overlaps with the proposal's core 'online Z3 verification during generation' claim and must be addressed as a baseline.", "The PCFG-based confidence estimation from 'Grammars of Formal Uncertainty' was validated on ProofWriter (logic tasks) with AUROC >0.93, but the same paper shows SMT autoformalization HURTS accuracy on factual tasks (-44.5%). The proposal evaluates on GPQA Diamond and ARC-Challenge where formalization may degrade rather than help — the confidence gating may need domain-specific behavior (always skip on certain task types), which adds complexity not currently addressed.", "Formalization coverage risk: at ~60-72% autoformalization accuracy in current literature, even with K=5 sampling and confidence gating, a substantial fraction of reasoning steps may have low confidence and be skipped. If >40% of steps are skipped, the cumulative constraint store becomes sparse and less effective at catching cross-step inconsistencies — potentially reducing the system to verifying only 'easy' steps that were likely correct anyway.", "MATH-500 is near-saturated (HERMES achieves 97.4% with online Lean4 verification). Using Qwen3-32B as the base model, the baseline accuracy may already be >95%, leaving <5% absolute headroom. The primary evaluation signal will need to come from AIME 2024/2025, but these are harder problems where NL-to-Z3 formalization accuracy is more uncertain.", "16-day timeline risk: implementing the full pipeline (Qwen3-32B reasoner + Qwen3-14B formalizer + PCFG confidence estimation + incremental Z3 solver + MUS extraction + targeted regeneration), calibrating confidence thresholds per domain, running 8+ benchmarks, and completing 4 ablation studies is ambitious. The PCFG fitting alone requires generating K=5 samples per step across a validation set, parsing them as SMT-LIB, and computing grammar statistics.", "MUS vs MCS distinction from VERGE is not well-articulated. MUS (what went wrong) and MCS (what to change) are dual concepts. The proposal should clarify why MUS-guided feedback is superior to VERGE's MCS-based correction for the targeted regeneration use case, rather than just using a different acronym."]
Feedback: The proposal has significantly improved from Round 1 — the VeriCoT characterization is now correct, HERMES is included as a baseline, confidence gating addresses the formalization bottleneck, and the central experiment is well-designed. The remaining issues are addressable:

1. **Add interwhen as a key baseline and differentiate explicitly**: interwhen (arXiv 2602.11202, Feb 2026) does online Z3 verification during generation but (a) does NOT maintain cumulative constraint state across steps — it checks each intermediate solution independently, (b) does NOT use PCFG-based confidence gating — it verifies at fixed polling intervals, and (c) does NOT provide MUS-derived structured feedback — it simply interrupts and lets the model self-correct. Frame your contribution as: cumulative constraint tracking + confidence-aware selective formalization + MUS-guided targeted regeneration, which interwhen lacks.

2. **Address formalization coverage explicitly**: Add an analysis/ablation measuring what fraction of steps pass the confidence threshold across different benchmark domains. If coverage is <50% on math benchmarks, consider a fallback: for skipped steps, add a weaker constraint (e.g., numerical range bounds or type constraints) that can be formalized with near-100% confidence, keeping the constraint store informative even when full formalization fails.

3. **Scope GPQA Diamond and ARC-Challenge honestly**: Given that SMT hurts on factual tasks per 'Grammars of Formal Uncertainty', consider dropping these from primary evaluation or adding a 'domain classifier' that routes tasks to Z3 verification only when the task type is logic/math. Report these benchmarks as 'sanity checks' showing the system doesn't degrade on non-target domains.

4. **Clarify MUS vs MCS**: MUS identifies the minimal set of conflicting constraints (diagnosis), while MCS identifies the minimal set to remove to restore satisfiability (repair). Argue that MUS is better for targeted regeneration because it tells the LLM WHAT went wrong (conflicting constraints), not just WHAT to remove.

5. **De-risk timeline**: Consider dropping one ablation (e.g., K=1 vs K=5 can be a supplementary experiment) and focusing on the 3 most important: confidence gating ON/OFF, online vs post-hoc, and MUS feedback vs generic retry. Prioritize AIME and ProofWriter/FOLIO results over MATH-500 (saturated).

### Round 3 review
Verdict: revise
Issues: ["ARC-Challenge is still missing from the evaluation benchmarks despite being explicitly required by the user. The proposal includes ZebraLogic and ProcessBench (not required) but omits ARC-Challenge (required).", "Timeline risk is the biggest concern: 14 days remaining to implement a 5-component pipeline (Reasoner, Two-Tier Formalizer with PCFG confidence, Domain Classifier, Cumulative Z3 Monitor with MUS, Targeted Regeneration), calibrate confidence thresholds, run experiments across 8+ benchmarks × 6 conditions, complete 4 ablations, and write the paper. Even with the open-source PCFG code from 'Grammars of Formal Uncertainty' (github.com/DebarghaG/grammars-formal-uncertainty), integration and calibration per task domain is non-trivial.", "Qwen3-32B baseline AIME performance is not clearly established. The Qwen3 technical report does not report Qwen3-32B dense model scores on AIME 2024/2025 separately from the MoE variants. Without knowing the baseline, it's impossible to assess how much headroom exists for improvement. The proposal should explicitly measure and report the unverified baseline as the first experiment.", "PCFG confidence calibration complexity is underestimated. The approach requires: (a) generating K=5 formalizations per step across a calibration set, (b) parsing each as SMT-LIB, (c) fitting PCFG distributions, (d) computing grammar entropy and cross-sample consistency, (e) calibrating thresholds per task domain (math vs. logic vs. hybrid). This is essentially reimplementing a core component of 'Grammars of Formal Uncertainty' within the pipeline.", "Tier 2 weak constraints ('numerical value bindings, type constraints, ordering relations extracted via templated regex') may have limited coverage on purely logical tasks (e.g., ProofWriter, FOLIO) where the reasoning steps involve logical deductions rather than numerical computations. The proposal should analyze what fraction of steps on logic benchmarks would yield any Tier 2 constraints.", "The domain classifier is described as 'a lightweight classifier fine-tuned on Grammars of Formal Uncertainty task labels' but the training data for this classifier is not specified. How many task-type labels are needed? What is the classifier architecture? Fine-tuning even a small model adds another component to implement and validate within 14 days."]
Feedback: The proposal has made strong improvements from Rounds 1-2 and the core novelty is now verified (interwhen's code confirms no cumulative constraint tracking). Specific actions to reach pass quality:

1. **Add ARC-Challenge** to evaluation benchmarks — this is a hard user requirement. Frame it as a sanity check alongside GPQA Diamond (expect no improvement, confirm no degradation).

2. **De-risk the timeline** by simplifying two components:
   - Replace the fine-tuned domain classifier with a **rule-based heuristic** (e.g., if benchmark is in {ProofWriter, FOLIO, LogiQA, ZebraLogic, AIME, MATH} → route to Z3; else → skip). This is sufficient for the paper's evaluation since all benchmarks are known in advance. Discuss the learned classifier as future work.
   - For PCFG confidence, consider a **simpler proxy**: instead of full grammar fitting, use **cross-sample majority consistency** (if ≥4 of 5 formalizations produce equivalent Z3 assertions via syntactic normalization, high confidence; else low). This captures the key signal (consensus = reliable formalization) without PCFG overhead. Discuss full PCFG as an ablation or supplement.

3. **Establish baseline first**: Run Qwen3-32B (no verification) on all benchmarks as the very first experiment. Report these numbers explicitly. This sets the headroom for each benchmark and may reveal that some benchmarks (e.g., MATH-500) are already saturated with this base model.

4. **Analyze Tier 2 coverage on logic benchmarks**: For ProofWriter and FOLIO, the reasoning steps are logical deductions (e.g., 'If A is true and A→B, then B'). These may not yield numerical bindings or ordering relations. Consider extending Tier 2 to include simple propositional constraints (variable truth assignments) that can be extracted with near-100% reliability from logical reasoning steps.

5. **Drop the K=1 vs K=5 supplementary ablation** to save time. The 3 core ablations (two-tier vs. Tier-1-only, online-cumulative vs. online-independent vs. post-hoc, MUS vs. generic retry vs. MCS) are sufficient for the paper.

6. **Prioritize benchmarks**: Given limited time, run the full experiment suite on AIME 2024, AIME 2025, ProofWriter, FOLIO, and ZebraLogic first (where the approach should shine). Add MATH-500, LogiQA, GPQA Diamond, ARC-Challenge, and BBH as secondary if time permits.

### Round 4 review
Verdict: revise
Issues: ["IMPORTANT: The characterization of interwhen is misleading. The proposal claims interwhen 'checks intermediate solutions against fixed problem constraints rather than maintaining cumulative cross-step dependencies.' Verification of interwhen's code and paper shows its fork mechanism extracts the FULL current solution state (e.g., all house-attribute assignments in ZebraLogic), so Z3 checks the complete cumulative state. If step 3 assigns x=7 and step 5 assigns x=12, interwhen catches this. The real distinction is that interwhen uses STATE-LEVEL cumulative checking (works for CSP/structured-state tasks) while the proposal uses ASSERTION-LEVEL cumulative tracking (works for derivation tasks like math proofs where no complete structured state can be extracted). This is a genuine and important distinction — but it must be articulated correctly.", "VeriCoT has been accepted at ICLR 2026 (poster), not just arXiv. This should be updated in references and raises the bar for comparison — VeriCoT is now peer-reviewed at a top venue.", "'Safe: Enhancing Mathematical Reasoning via Retrospective Step-aware Formal Verification' (ACL 2025, arXiv 2506.04592) does step-aware Lean4 verification of mathematical reasoning and is not cited. It should be included as related work alongside HERMES.", "AIME 2024 baseline of ~70% may be conservative. While it matches the EvalScope reproduction, third-party evaluations (llm-stats.com, designforonline.com) report Qwen3-32B at 80-81% on AIME 2024. If the true baseline is 80%, the headroom shrinks from ~30pp to ~20pp. The proposal should either justify the 70% figure (specific eval settings) or acknowledge the range.", "HERMES results (97.4% MATH-500, 66.7% AIME'25) are with DeepSeek-V3.1 as the base model, not Qwen3-32B. A fair comparison requires either running HERMES with Qwen3-32B or acknowledging the different base models when comparing. Currently the proposal lists these numbers without clarifying the base model mismatch.", "The NeurIPS 2024 paper title is 'Autoformalize Mathematical Statements' (not 'Autoformalizing'), and its equivalence checking uses Z3, CVC5, and Isabelle/HOL — not Z3 alone. The 10.7% improvement is for GPT-4 on miniF2F specifically; broader results show 0.22-1.35x relative improvements."]
Feedback: The proposal has improved substantially over 4 rounds and the core idea is sound. Two actions would bring it to pass quality:

1. **Fix the interwhen distinction** — this is the most important revision. Acknowledge that interwhen achieves cumulative-like checking for structured-state tasks (ZebraLogic, Maze, SpatialMap) because its fork mechanism extracts the full current solution state. Then argue that your assertion-level cumulative tracking handles DERIVATION tasks (mathematical proofs, logical deductions) where no complete structured state can be extracted mid-generation. On AIME, for example, you can't ask the model to 'output your current mathematical state as JSON' — the state IS the chain of derivations. This is actually a stronger novelty claim than 'interwhen doesn't track cumulative constraints' because it identifies a specific class of tasks where your approach provides something interwhen structurally cannot.

2. **Minor updates**: (a) Update VeriCoT to ICLR 2026 poster, (b) cite Safe (ACL 2025) as related work, (c) clarify HERMES base model is DeepSeek-V3.1 not Qwen3-32B, (d) acknowledge AIME 2024 baseline variance (70-81% depending on eval settings) and state your exact evaluation protocol, (e) fix minor reference inaccuracies.

### Round 5 review
Verdict: revise
Issues: ["IMPORTANT (unfixed from Round 4): The interwhen characterization is STILL misleading. The proposal says 'Unlike interwhen, which checks intermediate solutions against fixed problem constraints' — but interwhen extracts the FULL cumulative solution state (e.g., all house-attribute assignments in ZebraLogic) and checks it against constraints, effectively catching cross-step inconsistencies for structured-state tasks. This was explicitly flagged in Round 4 with a specific reframing suggestion (state-level vs assertion-level distinction) that was not implemented.", "IMPORTANT: Multiple Round 4 minor fixes were NOT applied: (a) VeriCoT still listed as 'arXiv Nov 2025' instead of ICLR 2026 poster, (b) Safe (ACL 2025, arXiv 2506.04592) still not cited, (c) HERMES results (97.4% MATH-500, 66.7% AIME'25) still not clarified as using DeepSeek-V3.1 base model (not Qwen3-32B), (d) NeurIPS 2024 paper title still 'Autoformalizing' instead of 'Autoformalize', (e) AIME 2024 baseline variance (70% pass@1 vs 80-81% avg@64) not acknowledged with evaluation protocol specification.", "Missing related work: 'Adaptive LLM-Symbolic Reasoning via Dynamic Logical Solver Composition' (EACL 2026, arXiv 2510.06774) introduces an adaptive multi-paradigm framework that dynamically selects from Z3/Pyke/Prover9/MiniZinc based on problem type. It explicitly criticizes static, predetermined solver routing — which is exactly what the proposed rule-based domain heuristic does. This paper must be cited and the limitation acknowledged.", "VERGE's semantic routing (claim-level LLM-based classification into 6 types → formal vs soft verifier) is not discussed despite being conceptually related to the proposed domain routing. VERGE's ablation shows removing routing drops performance by 8.3% average. The proposal should discuss VERGE's routing and position its rule-based heuristic as a practical simplification with known limitations.", "The 10.7% improvement from the NeurIPS 2024 autoformalization paper is misattributed: it comes from the COMBINED method (symbolic equivalence + semantic consistency using Z3, CVC5, and Isabelle/HOL with 12 tactics), not from 'cross-candidate symbolic equivalence checking via Z3' alone. The proposal uses this as validation for its cross-sample Z3-only consistency approach, which is a weaker version of what the paper actually shows.", "The novelty framing centers on cumulative constraint tracking as the primary differentiator, but VeriCoT already does exactly this (ℱᵢ = ℱᵢ₋₁ ∪ {Fᵢ}). The two-tier confidence-gated formalization is the actually novel component and should be promoted to the primary contribution, with online timing as secondary."]
Feedback: The proposal has matured well over 5 rounds but has a persistent problem: the interwhen characterization flagged in Round 4 was not fixed, and multiple minor corrections were not applied. These must be addressed — a reviewer seeing incorrect characterizations of closely related work will question the paper's credibility. Specific actions:

1. **Fix interwhen characterization (CRITICAL, Round 3 of asking)**: Replace 'checks intermediate solutions against fixed problem constraints' with an accurate description. Acknowledge that interwhen achieves cumulative-like checking for STRUCTURED-STATE tasks (ZebraLogic, Maze, SpatialMap) because its fork extracts the full current solution state. Then argue your assertion-level cumulative tracking handles DERIVATION tasks (math proofs, logical deductions in ProofWriter/FOLIO) where no complete structured state can be extracted mid-generation — the 'state' IS the chain of derivations. Use a derivation-task example: 'step 3 establishes monotonicity, step 7 applies a bound requiring concavity' rather than 'step 3 derives x=7, step 5 derives x=12' (which interwhen WOULD catch via state extraction).

2. **Apply all Round 4 minor fixes**: (a) VeriCoT → ICLR 2026 poster, (b) cite Safe (ACL 2025), (c) clarify HERMES uses DeepSeek-V3.1, (d) fix title to 'Autoformalize', (e) specify AIME baseline evaluation protocol (EvalScope pass@1, n=1, temp=0.6) and note avg@64 gives ~80-81%.

3. **Cite Adaptive LLM-Symbolic Reasoning (EACL 2026)** and acknowledge that static rule-based routing is a known limitation. Position your heuristic as a practical choice for fixed benchmark evaluation, with the EACL 2026 dynamic approach as the right future direction.

4. **Reframe novelty hierarchy**: Lead with two-tier confidence-gated formalization as the PRIMARY contribution (this is genuinely novel — no prior work combines cross-sample consistency gating with weak constraint fallback for maintaining constraint store informativeness). Position online timing as SECONDARY and cumulative tracking as TERTIARY (since VeriCoT already does it, your contribution is applying it online).

5. **Fix the NeurIPS 2024 citation**: The 10.7% is from the combined method (symbolic equivalence + semantic consistency) using Z3+CVC5+Isabelle, not from Z3-only cross-sample equivalence. Either cite the full method accurately or note that your approach uses a simplified version (Z3-only pairwise equivalence) and the 10.7% is an upper bound from the more complex pipeline.

6. **Discuss VERGE's semantic routing** as related work and explain why your simpler approach is sufficient for your evaluation setup (all benchmarks known in advance) while acknowledging VERGE's claim-level routing is more general.

### Round 6 review
Verdict: revise
Issues: ["NEW ISSUE: 'Do LLMs Game Formalization?' (arXiv 2604.19459, April 2026) demonstrates that LLMs systematically mistranslate premises during formalization, producing internally consistent but unfaithful outputs that 'evade detection entirely.' This directly undermines the cross-sample consistency mechanism: if Qwen3-14B consistently makes the same formalization error across all K=5 samples, the system assigns HIGH confidence to an incorrect formalization, introducing false positives into the cumulative constraint store. The proposal acknowledges this risk in a risk_note but relegates mitigation to 'roundtrip spot-checking in supplementary analysis' — this should be promoted to a core defense mechanism or at minimum discussed as a known limitation with quantified expected impact.", "ZebraLogic is listed as a prioritized benchmark where 'the approach should add most value,' but the proposal itself acknowledges that (a) interwhen's state-extraction works well on ZebraLogic (structured-state task), and (b) 'Tier 2 propositional constraint extraction may have limited yield on ZebraLogic (which involves constraint satisfaction rather than propositional deduction).' This creates a contradictory expectation — either reposition ZebraLogic as a baseline-comparison benchmark (where interwhen should match or outperform) or explain specifically why assertion-level cumulative tracking adds value beyond interwhen's state extraction on this task.", "The empirical outcome risk is inadequately addressed. The two-tier mechanism's value proposition rests on a chain of assumptions: (1) Tier 1 confidence correctly distinguishes good from bad formalizations, (2) Tier 2 weak constraints are informative enough to catch real cross-step errors, (3) the cumulative constraint store with mixed Tier-1/Tier-2 constraints provides enough coverage for MUS to identify meaningful conflicts. If any link fails — e.g., if Tier 2 constraints on AIME problems are limited to trivial bindings like 'n is a positive integer' that rarely conflict — the system reduces to checking only the easy steps. The proposal should identify a minimum viable validation: what specific error type on AIME/ProofWriter would demonstrate the two-tier mechanism's value?", "The 14-day timeline has no fallback plan. If debugging the formalizer-confidence-gate-Z3 pipeline takes 7+ days, there may not be enough time for the full experimental suite (8 benchmarks × 6 conditions × 3 ablations). The proposal should specify a minimum publishable result set: which 2-3 benchmarks and which 2-3 comparisons constitute the core claim, and which are stretch goals."]
Feedback: The proposal has made excellent progress — ALL Round 5 issues are now fixed, and the interwhen characterization (flagged since Round 3) is finally accurate. The core idea is sound and the contribution hierarchy is clear. To reach pass quality:

1. **Address systematic formalization errors in the core method**: Cite 'Do LLMs Game Formalization?' (arXiv 2604.19459, April 2026) and discuss how cross-sample consistency handles (or fails to handle) systematic mistranslations. Consider promoting roundtrip verification from supplementary to a lightweight Tier 1 validation step — generate K=5 formalizations, check cross-sample consistency, then roundtrip-verify the majority candidate back to NL and compare with the original step. This adds one informalization call per high-confidence step but catches systematic errors. If this is too expensive, at minimum quantify the expected rate of systematic errors on your benchmarks and argue that Tier 2 fallback provides a safety net.

2. **Reposition ZebraLogic**: Move ZebraLogic from 'prioritized' to 'comparison' category. On ZebraLogic, interwhen's state-extraction should work well, and the experiment should validate that your approach matches (not necessarily exceeds) interwhen on structured-state tasks while excelling on derivation tasks (AIME, ProofWriter, FOLIO). This actually strengthens the paper's narrative: your approach fills a gap for derivation tasks, not a replacement for interwhen on structured-state tasks.

3. **Define minimum viable experiment**: Specify: 'The core publishable claim requires comparing online-cumulative (ours) vs. online-independent (interwhen-style) vs. post-hoc-cumulative (VeriCoT-style) vs. no-verification on AIME 2024 + ProofWriter + FOLIO, with the two-tier vs. Tier-1-only ablation. This constitutes 4 conditions × 3 benchmarks × 2 ablation levels = 24 runs, achievable in ~60 H100-hours. The remaining benchmarks and ablations are stretch goals.' This de-risks the timeline without sacrificing the core contribution.

4. **Strengthen novelty framing**: Add a brief formal characterization of the informativeness-precision tradeoff. Define constraint store informativeness (fraction of steps with at least one constraint) and constraint store precision (fraction of constraints that are correct). Tier 1 optimizes for precision (high threshold), Tier 2 optimizes for informativeness (near-100% correct by construction). The two-tier mechanism explicitly manages this tradeoff. This elevates the contribution from an engineering trick to a principled framework.


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
  "promptId": "9f058579-330c-423c-b0cd-eef715c67283",
  "type": "user",
  "uuid": "0239d34e-9ccf-4899-ba06-15862134be86",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ae8c16f5-ce1c-4bce-923e-3afb8499b025",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-12T00:44:37.838Z_

```json
{
  "parentUuid": "0239d34e-9ccf-4899-ba06-15862134be86",
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
  "uuid": "6b77de11-dcfc-4758-b91c-4bed24dc1c61",
  "timestamp": "2026-05-12T00:44:37.838Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ae8c16f5-ce1c-4bce-923e-3afb8499b025",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-12T00:44:37.838Z_

```json
{
  "parentUuid": "6b77de11-dcfc-4758-b91c-4bed24dc1c61",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "8ec62a49-5739-4bf8-be43-965c75831016",
  "timestamp": "2026-05-12T00:44:37.838Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ae8c16f5-ce1c-4bce-923e-3afb8499b025",
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
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-11 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "8ec62a49-5739-4bf8-be43-965c75831016",
  "sessionId": "ae8c16f5-ce1c-4bce-923e-3afb8499b025"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Two-tier confidence-gated formalization for online derivation verification",
  "sessionId": "ae8c16f5-ce1c-4bce-923e-3afb8499b025"
}
```

---

### Assistant

_source line 8 · 2026-05-12T00:44:47.471Z_

<details><summary>Logged reasoning block</summary>

```text
This is a complex ML research review task. I need to independently verify the claims made in this proposal, which is now in round 7 of 10. Let me carefully analyze the idea and conduct thorough research to verify its claims.

The proposal is about "Two-Tier Confidence-Gated Formalization with Roundtrip Validation and Cumulative Online Constraint Tracking for Multi-Step Reasoning Verification."

Key claims to verify:
1. interwhen characterization (state-level vs assertion-level distinction)
2. VeriCoT as ICLR 2026 poster
3. "Do LLMs Game Formalization?" paper and its findings


4. Roundtrip verification paper claims
5. HERMES results and base model
6. Safe (ACL 2025) citation
7. Adaptive LLM-Symbolic Reasoning (EACL 2026)
8. Current SOTA on benchmarks
9. Novelty of the two-tier approach
10. Feasibility within constraints

Let me start by searching for the most critical pieces.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8ec62a49-5739-4bf8-be43-965c75831016",
  "isSidechain": false,
  "requestId": "req_011CawkRWLWGAtmxDZJHrFAC",
  "type": "assistant",
  "uuid": "0f33fb7a-a40f-4f7d-a2f5-e5305489824e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ae8c16f5-ce1c-4bce-923e-3afb8499b025",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T5nJ7KSTuP11hx6X1LsFUF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 23877,
      "cache_read_input_tokens": 11841,
      "output_tokens": 2550,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 23877,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2550,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 23877,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 23877
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

_source line 9 · 2026-05-12T00:44:47.985Z_

I'll conduct an independent adversarial review of this proposal. Let me start by verifying the key claims and searching for competing work.

Starting with parallel searches on the most critical verification dimensions.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0f33fb7a-a40f-4f7d-a2f5-e5305489824e",
  "isSidechain": false,
  "requestId": "req_011CawkRWLWGAtmxDZJHrFAC",
  "type": "assistant",
  "uuid": "e264b129-4f8b-4347-95f2-febf7aedb0d1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ae8c16f5-ce1c-4bce-923e-3afb8499b025",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T5nJ7KSTuP11hx6X1LsFUF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 23877,
      "cache_read_input_tokens": 11841,
      "output_tokens": 2550,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 23877,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2550,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 23877,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 23877
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

_source line 10 · 2026-05-12T00:45:01.083Z_

<details open><summary>🔧 Tool call — Agent · `toolu_011LrExfDsiUpjrKqCzWhqjK`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Verify interwhen and VeriCoT claims",
  "prompt": "You are helping me verify claims about two papers cited in an ML research proposal. Use WebSearch and WebFetch to find and read these papers. Report back with specific findings.\n\n1. **interwhen** (arXiv 2602.11202, Feb 2026): \n   - Search for this paper. Verify it exists.\n   - Does it do online Z3 verification during LLM generation?\n   - Does it use \"state extraction\" (forking inference to recover intermediate solutions)?\n   - Does it achieve cumulative-like checking by extracting the FULL current solution state?\n   - What tasks does it work on? (ZebraLogic, Maze, SpatialMap, etc.)\n   - What results does it achieve? (specifically the +10.4pp on ZebraLogic X-Large with Qwen3-30B-A3B)\n   - Does it work on \"derivation tasks\" (math proofs, logical deductions)?\n\n2. **VeriCoT** (arXiv 2511.04662):\n   - Verify it exists and check if it's accepted at ICLR 2026 as a poster.\n   - Does it maintain cumulative Z3 constraints (ℱᵢ = ℱᵢ₋₁ ∪ {Fᵢ})?\n   - Is it post-hoc only?\n   - What benchmarks does it evaluate on?\n\nSearch using queries like:\n- \"interwhen LLM-Process-Modulo Z3 verification arXiv 2602.11202\"\n- \"VeriCoT neuro-symbolic chain-of-thought ICLR 2026\"\n- site:arxiv.org for both papers\n- site:openreview.net for VeriCoT ICLR 2026\n\nReport specific details from the actual papers, not just search snippet summaries. Use WebFetch on the arxiv abstract pages."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e264b129-4f8b-4347-95f2-febf7aedb0d1",
  "isSidechain": false,
  "requestId": "req_011CawkRWLWGAtmxDZJHrFAC",
  "type": "assistant",
  "uuid": "6f3ed4cb-b5f8-4a58-b0c1-9f41cd7b2336",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ae8c16f5-ce1c-4bce-923e-3afb8499b025",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T5nJ7KSTuP11hx6X1LsFUF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 23877,
      "cache_read_input_tokens": 11841,
      "output_tokens": 2550,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 23877,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2550,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 23877,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 23877
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

_source line 11 · 2026-05-12T00:45:11.618Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01DX1mR2jPaWw4j2ohBjvERm`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Verify formalization gaming paper",
  "prompt": "You are helping me verify claims about papers on formalization faithfulness cited in an ML research proposal. Use WebSearch and WebFetch to find and verify these papers.\n\n1. **\"Do LLMs Game Formalization?\"** (claimed arXiv 2604.19459, April 2026):\n   - Search for this paper. Verify it exists.\n   - Does it demonstrate that LLMs systematically mistranslate premises during formalization?\n   - Does it show internally consistent but unfaithful outputs that \"evade detection entirely\"?\n   - Does it evaluate on 303 FOL problems (FOLIO + Multi-LogiEval)?\n   - What detection methods does it test? (cross-stage comparison, LLM-as-judge, rule-based diff)\n   - Does GPT-5 fabricate axioms? Does DeepSeek-R1 mistranslate premises?\n\n2. **\"Faithful Autoformalization via Roundtrip Verification and Repair\"** (claimed arXiv 2604.25031, April 2026):\n   - Search for this paper. Verify it exists.\n   - Does roundtrip verification raise formal equivalence from 45-61% to 83-85%?\n   - Is the Z3 equivalence check <1 second?\n   - How many LLM calls does diagnosis-guided repair require (claimed 7.21 vs 12.27 for random)?\n\n3. **ReForm** (claimed arXiv 2510.24592):\n   - Search for this paper. Verify it exists and its claims (+22.6pp average improvement).\n\nSearch queries:\n- \"Do LLMs Game Formalization arXiv 2604.19459\"\n- \"Faithful Autoformalization Roundtrip Verification arXiv 2604.25031\"\n- \"ReForm reflective autoformalization arXiv 2510.24592\"\n- \"LLM formalization faithfulness systematic errors 2026\"\n\nUse WebFetch to read the actual abstracts and key claims."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6f3ed4cb-b5f8-4a58-b0c1-9f41cd7b2336",
  "isSidechain": false,
  "requestId": "req_011CawkRWLWGAtmxDZJHrFAC",
  "type": "assistant",
  "uuid": "ece1a144-7c84-4a37-ac1c-6ae464398b91",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ae8c16f5-ce1c-4bce-923e-3afb8499b025",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T5nJ7KSTuP11hx6X1LsFUF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 23877,
      "cache_read_input_tokens": 11841,
      "output_tokens": 2550,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 23877,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2550,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 23877,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 23877
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

_source line 12 · 2026-05-12T00:45:21.206Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01LA5fpbX23kxUozAf9HjEy9`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Search for competing/concurrent work",
  "prompt": "You are helping me find competing and concurrent work that may overlap with a research proposal about \"two-tier confidence-gated formalization for online multi-step reasoning verification using Z3.\" \n\nSearch for recent work (2025-2026) on:\n\n1. **Online/streaming verification of LLM reasoning with formal methods**:\n   - \"online verification LLM reasoning Z3 2026\"\n   - \"streaming formal verification chain-of-thought 2025 2026\"\n   - \"real-time constraint checking LLM generation\"\n\n2. **Confidence-gated or selective formalization**:\n   - \"confidence gating formalization LLM\"\n   - \"selective autoformalization reasoning\"\n   - \"when to formalize LLM reasoning\"\n\n3. **Roundtrip verification for formalization faithfulness**:\n   - \"roundtrip verification autoformalization\"\n   - \"back-translation verification formal logic\"\n   - \"formalization faithfulness verification\"\n\n4. **Neurosymbolic reasoning verification recent work**:\n   - \"neurosymbolic reasoning verification 2026 arXiv\"\n   - \"hybrid neural symbolic reasoning verification EMNLP ICLR 2026\"\n   - \"Z3 SMT solver LLM reasoning 2026\"\n\n5. **Specifically check for any work combining these elements**:\n   - \"two-tier formalization constraint reasoning\"\n   - \"weak constraint fallback verification LLM\"\n   - \"informativeness precision tradeoff verification\"\n\n6. **Check recent EMNLP/ACL/ICLR 2026 accepted papers on reasoning verification**:\n   - \"ICLR 2026 accepted papers reasoning verification\"\n   - \"ACL 2026 reasoning verification formal methods\"\n\nFor each relevant paper found, report: title, venue/arXiv ID, date, and how it relates to the proposal. Use WebFetch to read abstracts of the most relevant papers."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ece1a144-7c84-4a37-ac1c-6ae464398b91",
  "isSidechain": false,
  "requestId": "req_011CawkRWLWGAtmxDZJHrFAC",
  "type": "assistant",
  "uuid": "6c674d3f-a74b-4af9-91d1-42fd5eaf4d79",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ae8c16f5-ce1c-4bce-923e-3afb8499b025",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T5nJ7KSTuP11hx6X1LsFUF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 23877,
      "cache_read_input_tokens": 11841,
      "output_tokens": 2550,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 23877,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2550,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 23877,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 23877
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

_source line 13 · 2026-05-12T00:45:33.103Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01YUK9K6fo4MXpA4fRNUfjmr`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Verify SOTA baselines and benchmarks",
  "prompt": "You are helping me verify current SOTA results on benchmarks relevant to an ML research proposal. Use WebSearch and WebFetch.\n\n1. **Qwen3-32B performance** (the proposed base model):\n   - Search for Qwen3-32B results on AIME 2024, AIME 2025, MATH-500\n   - \"Qwen3-32B AIME 2024 benchmark results\"\n   - \"Qwen3 32B thinking mode performance\"\n   - Check if pass@1 ~70% on AIME 2024 is accurate, or if it's higher (80-81%)\n   - Check MATH-500 baseline (claimed ~95.2%)\n\n2. **HERMES results verification**:\n   - \"HERMES mathematical reasoning verification arXiv 2511.18760\"\n   - Verify: 97.4% on MATH-500, 66.7% on AIME'25\n   - Confirm base model is DeepSeek-V3.1\n   - Check the >60% autoformalization failure at Kₜ=1 claim\n\n3. **Current SOTA on ProofWriter, FOLIO, LogiQA**:\n   - \"ProofWriter SOTA 2025 2026\"\n   - \"FOLIO benchmark SOTA results\"\n   - \"LogiQA benchmark results 2025 2026\"\n\n4. **VERGE results**:\n   - \"VERGE formal refinement LLM reasoning arXiv 2601.20055\"\n   - Verify the 18.7% average uplift claim\n   - Verify the routing ablation (-8.3% without routing)\n\n5. **Safe (ACL 2025) paper**:\n   - \"Safe step-aware formal verification ACL 2025 arXiv 2506.04592\"\n   - Verify it exists and does step-aware Lean4 verification\n\n6. **FoVer paper**:\n   - \"FoVer efficient PRM training formal verification arXiv 2505.15960\"\n   - Verify it's ACL 2026 Findings\n\nReport specific numbers and sources for each."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6c674d3f-a74b-4af9-91d1-42fd5eaf4d79",
  "isSidechain": false,
  "requestId": "req_011CawkRWLWGAtmxDZJHrFAC",
  "type": "assistant",
  "uuid": "c2e179a9-7e77-44d1-80f3-0f0db9a6d24f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ae8c16f5-ce1c-4bce-923e-3afb8499b025",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T5nJ7KSTuP11hx6X1LsFUF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 23877,
      "cache_read_input_tokens": 11841,
      "output_tokens": 2550,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 23877,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2550,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 23877,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 23877
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

_source line 14 · 2026-05-12T00:46:58.251Z_

<details><summary>↩ Tool result · `toolu_01DX1mR2jPaWw4j2ohBjvERm`</summary>

```text
Excellent. Now I have comprehensive data on all three papers. Let me compile the verification results.

---

## Verification Results

### Paper 1: "Do LLMs Game Formalization?" (arXiv 2604.19459, April 2026)

**Existence: CONFIRMED.** The paper exists at arXiv 2604.19459, submitted April 21, 2026, by Kyuhee Kim, Auguste Poiroux, and Antoine Bosselut. Published at the VerifAI-2 Workshop, ICLR 2026.

Claim-by-claim verification:

- **"LLMs systematically mistranslate premises during formalization"** -- PARTIALLY ACCURATE / NUANCED. The paper finds **no evidence of systematic gaming in unified generation**. However, in a two-stage pipeline, DeepSeek-R1 does mistranslate premises during formalization. The word "systematically" is an overstatement of the paper's findings -- the paper describes two distinct *modes* of unfaithfulness, not a single systematic pattern across all LLMs.

- **"Internally consistent but unfaithful outputs that evade detection entirely"** -- CONFIRMED. The paper uses this exact language about DeepSeek-R1's behavior: it "mistranslates premises during formalization, producing internally consistent outputs that evade detection entirely."

- **303 FOL problems (FOLIO + Multi-LogiEval)** -- CONFIRMED. 203 from FOLIO, 100 from Multi-LogiEval.

- **Detection methods (cross-stage comparison, LLM-as-judge, rule-based diff)** -- CONFIRMED. All three methods are explicitly tested. Cross-stage comparison detects GPT-5's axiom fabrication; LLM-as-judge (using Claude Opus 4.5) produces false negatives/positives; rule-based diff detects Stage 2 modifications to Stage 1 formalizations.

- **GPT-5 fabricates axioms** -- CONFIRMED. "GPT-5 fabricates axioms during proof generation, a reactive fallback detectable via cross-stage comparison."

- **DeepSeek-R1 mistranslates premises** -- CONFIRMED. DeepSeek-R1 mistranslates premises during formalization (e.g., translating place-based premises as event-based to make theorems trivial).

---

### Paper 2: "Faithful Autoformalization via Roundtrip Verification and Repair" (arXiv 2604.25031, April 2026)

**Existence: CONFIRMED.** Submitted April 27, 2026 (v1), revised May 9, 2026 (v2), by Daneshvar Amrollahi, Jerry Lopez, and Clark Barrett.

Claim-by-claim verification:

- **"Roundtrip verification raises formal equivalence from 45-61% to 83-85%"** -- PARTIALLY ACCURATE but simplified. The actual baseline equivalence ranges from ~44.7% to ~66.2% (depending on model and domain). Post-repair equivalence reaches 85.3%-94.7%. The "45-61% to 83-85%" framing is a reasonable approximation of the Traffic domain results with Claude (44.7% to 85.3%), but it understates the GPT results (which reach 90.7% on Traffic) and omits the Wildlife domain. The range is selectively cited.

- **"Z3 equivalence check <1 second"** -- CONFIRMED. The paper states "all queries resolve in under one second" using Z3 SMT solver v4.15.3.

- **"Diagnosis-guided repair requires 7.21 vs 12.27 LLM calls for random"** -- PARTIALLY CONFIRMED. These exact numbers (7.21 vs 12.27) appear for the **Traffic domain with Claude only**. For Traffic domain with GPT, the relationship is actually **reversed** (14.56 for full/diagnosis-guided vs 9.77 for random). The paper itself notes the cost advantage is "model-dependent." Citing only the Claude numbers without this caveat is cherry-picking.

- **150 traffic rules** -- CONFIRMED for the Traffic corpus (150 rules from Texas Transportation Code), though there is also a second Wildlife corpus of 77 rules.

---

### Paper 3: ReForm (arXiv 2510.24592)

**Existence: CONFIRMED.** Submitted October 28, 2025 (v1), revised February 10, 2026 (v3), by Guoxin Chen, Jing Wu, Xinjie Chen, Wayne Xin Zhao, Ruihua Song, Chengxi Li, Kai Fan, Dayiheng Liu, and Minpeng Liao.

- **"+22.6pp average improvement"** -- CONFIRMED. The abstract states "an average improvement of 22.6 percentage points over the strongest baselines" across four autoformalization benchmarks.

---

### Summary of Concerns

All three papers are **real and verified** at the claimed arXiv IDs. Most specific claims are accurate. However, two issues stand out:

1. **Paper 1**: The proposal's framing that LLMs "systematically mistranslate premises" overstates the paper's nuanced finding. The paper explicitly finds *no systematic gaming* in unified generation. The unfaithfulness modes are pipeline-specific and model-specific, not a universal systematic behavior.

2. **Paper 2**: The LLM call cost claim (7.21 vs 12.27) cherry-picks one model's results. For GPT, the diagnosis-guided approach is actually *more expensive* than random repair (14.56 vs 9.77). The equivalence improvement range is also selectively cited from one domain/model combination.

Sources:
- [Do LLMs Game Formalization? (arXiv 2604.19459)](https://arxiv.org/abs/2604.19459)
- [Do LLMs Game Formalization? (HTML)](https://arxiv.org/html/2604.19459)
- [Faithful Autoformalization via Roundtrip Verification and Repair (arXiv 2604.25031)](https://arxiv.org/abs/2604.25031)
- [Faithful Autoformalization via Roundtrip Verification and Repair (HTML)](https://arxiv.org/html/2604.25031)
- [ReForm: Reflective Autoformalization (arXiv 2510.24592)](https://arxiv.org/abs/2510.24592)

agentId: add5a9d73de00a963 (use SendMessage with to: 'add5a9d73de00a963' to continue this agent)
&lt;usage>total_tokens: 19887
tool_uses: 10
duration_ms: 106629&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ece1a144-7c84-4a37-ac1c-6ae464398b91",
  "isSidechain": false,
  "promptId": "9f058579-330c-423c-b0cd-eef715c67283",
  "type": "user",
  "uuid": "145d41b6-fa78-4934-a211-dad9f17a8544",
  "toolUseResult": {
    "status": "completed",
    "prompt": "You are helping me verify claims about papers on formalization faithfulness cited in an ML research proposal. Use WebSearch and WebFetch to find and verify these papers.\n\n1. **\"Do LLMs Game Formalization?\"** (claimed arXiv 2604.19459, April 2026):\n   - Search for this paper. Verify it exists.\n   - Does it demonstrate that LLMs systematically mistranslate premises during formalization?\n   - Does it show internally consistent but unfaithful outputs that \"evade detection entirely\"?\n   - Does it evaluate on 303 FOL problems (FOLIO + Multi-LogiEval)?\n   - What detection methods does it test? (cross-stage comparison, LLM-as-judge, rule-based diff)\n   - Does GPT-5 fabricate axioms? Does DeepSeek-R1 mistranslate premises?\n\n2. **\"Faithful Autoformalization via Roundtrip Verification and Repair\"** (claimed arXiv 2604.25031, April 2026):\n   - Search for this paper. Verify it exists.\n   - Does roundtrip verification raise formal equivalence from 45-61% to 83-85%?\n   - Is the Z3 equivalence check <1 second?\n   - How many LLM calls does diagnosis-guided repair require (claimed 7.21 vs 12.27 for random)?\n\n3. **ReForm** (claimed arXiv 2510.24592):\n   - Search for this paper. Verify it exists and its claims (+22.6pp average improvement).\n\nSearch queries:\n- \"Do LLMs Game Formalization arXiv 2604.19459\"\n- \"Faithful Autoformalization Roundtrip Verification arXiv 2604.25031\"\n- \"ReForm reflective autoformalization arXiv 2510.24592\"\n- \"LLM formalization faithfulness systematic errors 2026\"\n\nUse WebFetch to read the actual abstracts and key claims.",
    "agentId": "add5a9d73de00a963",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Excellent. Now I have comprehensive data on all three papers. Let me compile the verification results.\n\n---\n\n## Verification Results\n\n### Paper 1: \"Do LLMs Game Formalization?\" (arXiv 2604.19459, April 2026)\n\n**Existence: CONFIRMED.** The paper exists at arXiv 2604.19459, submitted April 21, 2026, by Kyuhee Kim, Auguste Poiroux, and Antoine Bosselut. Published at the VerifAI-2 Workshop, ICLR 2026.\n\nClaim-by-claim verification:\n\n- **\"LLMs systematically mistranslate premises during formalization\"** -- PARTIALLY ACCURATE / NUANCED. The paper finds **no evidence of systematic gaming in unified generation**. However, in a two-stage pipeline, DeepSeek-R1 does mistranslate premises during formalization. The word \"systematically\" is an overstatement of the paper's findings -- the paper describes two distinct *modes* of unfaithfulness, not a single systematic pattern across all LLMs.\n\n- **\"Internally consistent but unfaithful outputs that evade detection entirely\"** -- CONFIRMED. The paper uses this exact language about DeepSeek-R1's behavior: it \"mistranslates premises during formalization, producing internally consistent outputs that evade detection entirely.\"\n\n- **303 FOL problems (FOLIO + Multi-LogiEval)** -- CONFIRMED. 203 from FOLIO, 100 from Multi-LogiEval.\n\n- **Detection methods (cross-stage comparison, LLM-as-judge, rule-based diff)** -- CONFIRMED. All three methods are explicitly tested. Cross-stage comparison detects GPT-5's axiom fabrication; LLM-as-judge (using Claude Opus 4.5) produces false negatives/positives; rule-based diff detects Stage 2 modifications to Stage 1 formalizations.\n\n- **GPT-5 fabricates axioms** -- CONFIRMED. \"GPT-5 fabricates axioms during proof generation, a reactive fallback detectable via cross-stage comparison.\"\n\n- **DeepSeek-R1 mistranslates premises** -- CONFIRMED. DeepSeek-R1 mistranslates premises during formalization (e.g., translating place-based premises as event-based to make theorems trivial).\n\n---\n\n### Paper 2: \"Faithful Autoformalization via Roundtrip Verification and Repair\" (arXiv 2604.25031, April 2026)\n\n**Existence: CONFIRMED.** Submitted April 27, 2026 (v1), revised May 9, 2026 (v2), by Daneshvar Amrollahi, Jerry Lopez, and Clark Barrett.\n\nClaim-by-claim verification:\n\n- **\"Roundtrip verification raises formal equivalence from 45-61% to 83-85%\"** -- PARTIALLY ACCURATE but simplified. The actual baseline equivalence ranges from ~44.7% to ~66.2% (depending on model and domain). Post-repair equivalence reaches 85.3%-94.7%. The \"45-61% to 83-85%\" framing is a reasonable approximation of the Traffic domain results with Claude (44.7% to 85.3%), but it understates the GPT results (which reach 90.7% on Traffic) and omits the Wildlife domain. The range is selectively cited.\n\n- **\"Z3 equivalence check <1 second\"** -- CONFIRMED. The paper states \"all queries resolve in under one second\" using Z3 SMT solver v4.15.3.\n\n- **\"Diagnosis-guided repair requires 7.21 vs 12.27 LLM calls for random\"** -- PARTIALLY CONFIRMED. These exact numbers (7.21 vs 12.27) appear for the **Traffic domain with Claude only**. For Traffic domain with GPT, the relationship is actually **reversed** (14.56 for full/diagnosis-guided vs 9.77 for random). The paper itself notes the cost advantage is \"model-dependent.\" Citing only the Claude numbers without this caveat is cherry-picking.\n\n- **150 traffic rules** -- CONFIRMED for the Traffic corpus (150 rules from Texas Transportation Code), though there is also a second Wildlife corpus of 77 rules.\n\n---\n\n### Paper 3: ReForm (arXiv 2510.24592)\n\n**Existence: CONFIRMED.** Submitted October 28, 2025 (v1), revised February 10, 2026 (v3), by Guoxin Chen, Jing Wu, Xinjie Chen, Wayne Xin Zhao, Ruihua Song, Chengxi Li, Kai Fan, Dayiheng Liu, and Minpeng Liao.\n\n- **\"+22.6pp average improvement\"** -- CONFIRMED. The abstract states \"an average improvement of 22.6 percentage points over the strongest baselines\" across four autoformalization benchmarks.\n\n---\n\n### Summary of Concerns\n\nAll three papers are **real and verified** at the claimed arXiv IDs. Most specific claims are accurate. However, two issues stand out:\n\n1. **Paper 1**: The proposal's framing that LLMs \"systematically mistranslate premises\" overstates the paper's nuanced finding. The paper explicitly finds *no systematic gaming* in unified generation. The unfaithfulness modes are pipeline-specific and model-specific, not a universal systematic behavior.\n\n2. **Paper 2**: The LLM call cost claim (7.21 vs 12.27) cherry-picks one model's results. For GPT, the diagnosis-guided approach is actually *more expensive* than random repair (14.56 vs 9.77). The equivalence improvement range is also selectively cited from one domain/model combination.\n\nSources:\n- [Do LLMs Game Formalization? (arXiv 2604.19459)](https://arxiv.org/abs/2604.19459)\n- [Do LLMs Game Formalization? (HTML)](https://arxiv.org/html/2604.19459)\n- [Faithful Autoformalization via Roundtrip Verification and Repair (arXiv 2604.25031)](https://arxiv.org/abs/2604.25031)\n- [Faithful Autoformalization via Roundtrip Verification and Repair (HTML)](https://arxiv.org/html/2604.25031)\n- [ReForm: Reflective Autoformalization (arXiv 2510.24592)](https://arxiv.org/abs/2510.24592)"
      }
    ],
    "totalDurationMs": 106629,
    "totalTokens": 19887,
    "totalToolUseCount": 10,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1319,
      "cache_read_input_tokens": 17011,
      "output_tokens": 1556,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1319
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1556,
          "cache_read_input_tokens": 17011,
          "cache_creation_input_tokens": 1319,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1319,
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
      "otherToolCount": 10
    }
  },
  "sourceToolAssistantUUID": "ece1a144-7c84-4a37-ac1c-6ae464398b91",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ae8c16f5-ce1c-4bce-923e-3afb8499b025",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-12T00:47:53.347Z_

<details><summary>↩ Tool result · `toolu_011LrExfDsiUpjrKqCzWhqjK`</summary>

```text
Excellent. Now I have comprehensive information on both papers. Let me compile the findings.

---

## Findings Report

### Paper 1: interwhen (arXiv 2602.11202, Feb 2026)

**Exists:** YES. "interwhen: A Generalizable Framework for Verifiable Reasoning with Test-time Monitors" by Vishak K Bhat, Prateek Chanda, et al. Submitted February 5, 2026.

**Does it do online Z3 verification during LLM generation?**
YES, but with nuance. The Z3 verification is **asynchronous and interleaved** with generation, not purely post-hoc. The workflow: at periodic intervals (e.g., every k newlines), the framework forks the generation into a side-stream to extract state, runs Z3 on that extracted state, and only interrupts the main generation stream if the verifier finds an error. So Z3 runs *during* the generation process, but asynchronously -- the main generation continues unless an error is detected. Z3 is specifically used for the **SpatialMap** and **ZebraLogic** tasks.

**Does it use "state extraction" via forking inference?**
YES. The paper explicitly uses "forking inference." The mechanism works by forking the model's execution at periodic intervals, appending a `&lt;/think>` marker plus a format instruction, and generating a structured intermediate answer in a side-stream. This recovers the model's current solution state without modifying the main generation trace.

**Does it achieve cumulative-like checking by extracting the FULL current solution state?**
YES. For ZebraLogic specifically, the paper states the model is asked to generate "a JSON representation of the current assignments of attributes to houses during the reasoning process." This captures **all accumulated assignments so far** -- the full current solution state, not just the latest step. The Z3 verifier then checks this full state against the puzzle constraints. However, the paper does NOT explicitly maintain a formal cumulative constraint set (like F_i = F_{i-1} union {F_i}) -- instead it extracts the full current state and checks it against the original problem constraints.

**What tasks does it work on?**
Five benchmarks:
- **Maze** (1,500 instances) -- grid navigation with turn counting
- **SpatialMap** (1,500 instances) -- spatial reasoning about object locations
- **GameOf24** (1,362 instances) -- arithmetic expression construction
- **ZebraLogic** (1,000 instances + X-Large subset) -- constraint satisfaction puzzles
- **Verina** (189 instances) -- Lean4 code/specification generation (split into VerinaCode and VerinaSpec)

**Does it achieve +10.4pp on ZebraLogic X-Large with Qwen3-30B-A3B?**
YES, confirmed. ZebraLogic X-Large with Qwen3-30B-A3B: interwhen achieves **89.6% accuracy** vs. baseline CoT of 79.2%, a gain of **+10.4 percentage points** at 103.4% relative token usage. The paper also reports a **+15.5pp improvement** on Verina-Code with Qwen3-30B (71.6% vs. 56.1% CoT).

**Does it work on "derivation tasks" (math proofs, logical deductions)?**
NO -- not evaluated on derivation tasks. The paper does not explicitly use the terminology "derivation tasks" vs. "construction tasks," but all five benchmarks are construction/verification tasks (building solutions, navigating state spaces, generating code). No math proofs or formal logical deductions are evaluated. The paper notes: "interwhen benefits tasks where intermediate checks differ from the final check" and acknowledges that "building verifiers for general reasoning tasks is an important future challenge."

---

### Paper 2: VeriCoT (arXiv 2511.04662)

**Exists:** YES. "VeriCoT: Neuro-symbolic Chain-of-Thought Validation via Logical Consistency Checks" by Yu Feng, Nathaniel Weir, Kaj Bostrom, Sam Bayless, et al. Submitted November 6, 2025.

**Accepted at ICLR 2026 as a poster?**
YES, confirmed. The OpenReview page (ID: zHuV3Vatov) shows it is **published as a conference paper at ICLR 2026** with **poster** status.

**Does it maintain cumulative Z3 constraints (F_i = F_{i-1} union {F_i})?**
YES. The paper explicitly uses the formulation **F_i = F_{i-1} ∪ {F_i}** for accumulating formulas across reasoning steps, and similarly **P_i = P_{i-1} ∪ {P_i}** for premises. It "maintains a growing set of first-order-logic (FOL) premises inferred from NL context." The solver used is specifically **Z3** (SMT solver), with formulas encoded in SMT-LIB format.

**Is it post-hoc only?**
YES. VeriCoT operates **post-hoc** -- it is applied after the full Chain-of-Thought generation is complete. The algorithm processes each completed reasoning step sequentially rather than intervening during generation. (Though it can be used for inference-time self-reflection as a secondary application, the verification itself is post-hoc.)

**What benchmarks does it evaluate on?**
Three datasets:
- **ProofWriter** (5,000 training / 400 test)
- **LegalBench-SARA** (272 entailment + 95 numeric instances)
- **BioASQ Task 12b** (5,049 training / 340 test)

Key results: ProofWriter 45.2% pass rate / 94.1% precision; self-reflection yields ~46% relative improvement in verification pass rates; DPO fine-tuning achieves 18.4% relative improvement.

---

### Summary of Claim Verification

| Claim | Verdict |
|-------|---------|
| interwhen exists at 2602.11202 | CONFIRMED |
| interwhen does online Z3 verification during generation | CONFIRMED (asynchronous, interleaved) |
| interwhen uses "state extraction" via forking inference | CONFIRMED |
| interwhen extracts FULL current solution state | CONFIRMED (for ZebraLogic: full JSON of all current assignments) |
| interwhen works on ZebraLogic, Maze, SpatialMap | CONFIRMED (plus GameOf24, Verina) |
| interwhen achieves +10.4pp on ZebraLogic X-Large with Qwen3-30B-A3B | CONFIRMED (79.2% -> 89.6%) |
| interwhen works on derivation tasks | NOT SUPPORTED (only construction/verification tasks evaluated) |
| VeriCoT exists at 2511.04662 | CONFIRMED |
| VeriCoT accepted at ICLR 2026 as poster | CONFIRMED |
| VeriCoT maintains cumulative constraints F_i = F_{i-1} ∪ {F_i} | CONFIRMED |
| VeriCoT is post-hoc only | CONFIRMED |
| VeriCoT benchmarks: ProofWriter, LegalBench-SARA, BioASQ | CONFIRMED |

Sources:
- [interwhen arXiv abstract](https://arxiv.org/abs/2602.11202)
- [interwhen full HTML paper](https://arxiv.org/html/2602.11202)
- [VeriCoT arXiv abstract](https://arxiv.org/abs/2511.04662)
- [VeriCoT full HTML paper](https://arxiv.org/html/2511.04662v1)
- [VeriCoT OpenReview (ICLR 2026)](https://openreview.net/forum?id=zHuV3Vatov)

agentId: a60b8b53e7c936364 (use SendMessage with to: 'a60b8b53e7c936364' to continue this agent)
&lt;usage>total_tokens: 23572
tool_uses: 13
duration_ms: 172257&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6f3ed4cb-b5f8-4a58-b0c1-9f41cd7b2336",
  "isSidechain": false,
  "promptId": "9f058579-330c-423c-b0cd-eef715c67283",
  "type": "user",
  "uuid": "be316499-20fb-42f5-a9c7-2d53b0eb421a",
  "toolUseResult": {
    "status": "completed",
    "prompt": "You are helping me verify claims about two papers cited in an ML research proposal. Use WebSearch and WebFetch to find and read these papers. Report back with specific findings.\n\n1. **interwhen** (arXiv 2602.11202, Feb 2026): \n   - Search for this paper. Verify it exists.\n   - Does it do online Z3 verification during LLM generation?\n   - Does it use \"state extraction\" (forking inference to recover intermediate solutions)?\n   - Does it achieve cumulative-like checking by extracting the FULL current solution state?\n   - What tasks does it work on? (ZebraLogic, Maze, SpatialMap, etc.)\n   - What results does it achieve? (specifically the +10.4pp on ZebraLogic X-Large with Qwen3-30B-A3B)\n   - Does it work on \"derivation tasks\" (math proofs, logical deductions)?\n\n2. **VeriCoT** (arXiv 2511.04662):\n   - Verify it exists and check if it's accepted at ICLR 2026 as a poster.\n   - Does it maintain cumulative Z3 constraints (ℱᵢ = ℱᵢ₋₁ ∪ {Fᵢ})?\n   - Is it post-hoc only?\n   - What benchmarks does it evaluate on?\n\nSearch using queries like:\n- \"interwhen LLM-Process-Modulo Z3 verification arXiv 2602.11202\"\n- \"VeriCoT neuro-symbolic chain-of-thought ICLR 2026\"\n- site:arxiv.org for both papers\n- site:openreview.net for VeriCoT ICLR 2026\n\nReport specific details from the actual papers, not just search snippet summaries. Use WebFetch on the arxiv abstract pages.",
    "agentId": "a60b8b53e7c936364",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Excellent. Now I have comprehensive information on both papers. Let me compile the findings.\n\n---\n\n## Findings Report\n\n### Paper 1: interwhen (arXiv 2602.11202, Feb 2026)\n\n**Exists:** YES. \"interwhen: A Generalizable Framework for Verifiable Reasoning with Test-time Monitors\" by Vishak K Bhat, Prateek Chanda, et al. Submitted February 5, 2026.\n\n**Does it do online Z3 verification during LLM generation?**\nYES, but with nuance. The Z3 verification is **asynchronous and interleaved** with generation, not purely post-hoc. The workflow: at periodic intervals (e.g., every k newlines), the framework forks the generation into a side-stream to extract state, runs Z3 on that extracted state, and only interrupts the main generation stream if the verifier finds an error. So Z3 runs *during* the generation process, but asynchronously -- the main generation continues unless an error is detected. Z3 is specifically used for the **SpatialMap** and **ZebraLogic** tasks.\n\n**Does it use \"state extraction\" via forking inference?**\nYES. The paper explicitly uses \"forking inference.\" The mechanism works by forking the model's execution at periodic intervals, appending a `&lt;/think>` marker plus a format instruction, and generating a structured intermediate answer in a side-stream. This recovers the model's current solution state without modifying the main generation trace.\n\n**Does it achieve cumulative-like checking by extracting the FULL current solution state?**\nYES. For ZebraLogic specifically, the paper states the model is asked to generate \"a JSON representation of the current assignments of attributes to houses during the reasoning process.\" This captures **all accumulated assignments so far** -- the full current solution state, not just the latest step. The Z3 verifier then checks this full state against the puzzle constraints. However, the paper does NOT explicitly maintain a formal cumulative constraint set (like F_i = F_{i-1} union {F_i}) -- instead it extracts the full current state and checks it against the original problem constraints.\n\n**What tasks does it work on?**\nFive benchmarks:\n- **Maze** (1,500 instances) -- grid navigation with turn counting\n- **SpatialMap** (1,500 instances) -- spatial reasoning about object locations\n- **GameOf24** (1,362 instances) -- arithmetic expression construction\n- **ZebraLogic** (1,000 instances + X-Large subset) -- constraint satisfaction puzzles\n- **Verina** (189 instances) -- Lean4 code/specification generation (split into VerinaCode and VerinaSpec)\n\n**Does it achieve +10.4pp on ZebraLogic X-Large with Qwen3-30B-A3B?**\nYES, confirmed. ZebraLogic X-Large with Qwen3-30B-A3B: interwhen achieves **89.6% accuracy** vs. baseline CoT of 79.2%, a gain of **+10.4 percentage points** at 103.4% relative token usage. The paper also reports a **+15.5pp improvement** on Verina-Code with Qwen3-30B (71.6% vs. 56.1% CoT).\n\n**Does it work on \"derivation tasks\" (math proofs, logical deductions)?**\nNO -- not evaluated on derivation tasks. The paper does not explicitly use the terminology \"derivation tasks\" vs. \"construction tasks,\" but all five benchmarks are construction/verification tasks (building solutions, navigating state spaces, generating code). No math proofs or formal logical deductions are evaluated. The paper notes: \"interwhen benefits tasks where intermediate checks differ from the final check\" and acknowledges that \"building verifiers for general reasoning tasks is an important future challenge.\"\n\n---\n\n### Paper 2: VeriCoT (arXiv 2511.04662)\n\n**Exists:** YES. \"VeriCoT: Neuro-symbolic Chain-of-Thought Validation via Logical Consistency Checks\" by Yu Feng, Nathaniel Weir, Kaj Bostrom, Sam Bayless, et al. Submitted November 6, 2025.\n\n**Accepted at ICLR 2026 as a poster?**\nYES, confirmed. The OpenReview page (ID: zHuV3Vatov) shows it is **published as a conference paper at ICLR 2026** with **poster** status.\n\n**Does it maintain cumulative Z3 constraints (F_i = F_{i-1} union {F_i})?**\nYES. The paper explicitly uses the formulation **F_i = F_{i-1} ∪ {F_i}** for accumulating formulas across reasoning steps, and similarly **P_i = P_{i-1} ∪ {P_i}** for premises. It \"maintains a growing set of first-order-logic (FOL) premises inferred from NL context.\" The solver used is specifically **Z3** (SMT solver), with formulas encoded in SMT-LIB format.\n\n**Is it post-hoc only?**\nYES. VeriCoT operates **post-hoc** -- it is applied after the full Chain-of-Thought generation is complete. The algorithm processes each completed reasoning step sequentially rather than intervening during generation. (Though it can be used for inference-time self-reflection as a secondary application, the verification itself is post-hoc.)\n\n**What benchmarks does it evaluate on?**\nThree datasets:\n- **ProofWriter** (5,000 training / 400 test)\n- **LegalBench-SARA** (272 entailment + 95 numeric instances)\n- **BioASQ Task 12b** (5,049 training / 340 test)\n\nKey results: ProofWriter 45.2% pass rate / 94.1% precision; self-reflection yields ~46% relative improvement in verification pass rates; DPO fine-tuning achieves 18.4% relative improvement.\n\n---\n\n### Summary of Claim Verification\n\n| Claim | Verdict |\n|-------|---------|\n| interwhen exists at 2602.11202 | CONFIRMED |\n| interwhen does online Z3 verification during generation | CONFIRMED (asynchronous, interleaved) |\n| interwhen uses \"state extraction\" via forking inference | CONFIRMED |\n| interwhen extracts FULL current solution state | CONFIRMED (for ZebraLogic: full JSON of all current assignments) |\n| interwhen works on ZebraLogic, Maze, SpatialMap | CONFIRMED (plus GameOf24, Verina) |\n| interwhen achieves +10.4pp on ZebraLogic X-Large with Qwen3-30B-A3B | CONFIRMED (79.2% -> 89.6%) |\n| interwhen works on derivation tasks | NOT SUPPORTED (only construction/verification tasks evaluated) |\n| VeriCoT exists at 2511.04662 | CONFIRMED |\n| VeriCoT accepted at ICLR 2026 as poster | CONFIRMED |\n| VeriCoT maintains cumulative constraints F_i = F_{i-1} ∪ {F_i} | CONFIRMED |\n| VeriCoT is post-hoc only | CONFIRMED |\n| VeriCoT benchmarks: ProofWriter, LegalBench-SARA, BioASQ | CONFIRMED |\n\nSources:\n- [interwhen arXiv abstract](https://arxiv.org/abs/2602.11202)\n- [interwhen full HTML paper](https://arxiv.org/html/2602.11202)\n- [VeriCoT arXiv abstract](https://arxiv.org/abs/2511.04662)\n- [VeriCoT full HTML paper](https://arxiv.org/html/2511.04662v1)\n- [VeriCoT OpenReview (ICLR 2026)](https://openreview.net/forum?id=zHuV3Vatov)"
      }
    ],
    "totalDurationMs": 172257,
    "totalTokens": 23572,
    "totalToolUseCount": 13,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1938,
      "cache_read_input_tokens": 19718,
      "output_tokens": 1915,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1938
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1915,
          "cache_read_input_tokens": 19718,
          "cache_creation_input_tokens": 1938,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1938,
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
      "otherToolCount": 13
    }
  },
  "sourceToolAssistantUUID": "6f3ed4cb-b5f8-4a58-b0c1-9f41cd7b2336",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ae8c16f5-ce1c-4bce-923e-3afb8499b025",
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
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-11 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "be316499-20fb-42f5-a9c7-2d53b0eb421a",
  "sessionId": "ae8c16f5-ce1c-4bce-923e-3afb8499b025"
}
```

---

### Runtime record

_source line 17_

```json
{
  "type": "ai-title",
  "aiTitle": "Two-tier confidence-gated formalization for online derivation verification",
  "sessionId": "ae8c16f5-ce1c-4bce-923e-3afb8499b025"
}
```

---

### Tool result

_source line 18 · 2026-05-12T00:50:11.298Z_

<details><summary>↩ Tool result · `toolu_01LA5fpbX23kxUozAf9HjEy9`</summary>

```text
I now have comprehensive coverage. Here is my full report of competing and concurrent work.

---

## Competing and Concurrent Work Report

Below is a comprehensive landscape of recent (2025--2026) work that overlaps with a proposal on "two-tier confidence-gated formalization for online multi-step reasoning verification using Z3." I have organized findings by relevance tier.

---

### TIER 1: MOST DIRECTLY COMPETING -- Papers combining multiple core elements of the proposal

#### 1. VERGE: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning
- **arXiv:** [2601.20055](https://arxiv.org/abs/2601.20055) | January 27, 2026 (revised May 2, 2026)
- **Authors:** Vikash Singh, Darion Cassel, Nathaniel Weir, Nick Feng, Sam Bayless
- **Overlap:** **This is the single most threatening competitor.** VERGE implements a neurosymbolic framework combining LLMs with SMT solvers for iterative verification-guided reasoning. Its three key innovations directly parallel the proposal: (1) **semantic routing** that directs logical claims to symbolic solvers (including SMT) while routing commonsense claims to LLM ensembles -- this is functionally equivalent to a two-tier formalization approach; (2) multi-model consensus via formal semantic equivalence checking; (3) Minimal Correction Subsets (MCS) for precise error localization. The "soft verifier" for commonsense claims is capped at a lower maximum score than SMT-verified claims, directly implementing an informativeness-precision tradeoff.
- **Key distinction from proposal:** VERGE focuses on post-hoc iterative refinement rather than online/streaming verification during generation. It also does not explicitly use confidence scores as a gating mechanism -- the routing is based on claim type (logical vs. commonsense) rather than model confidence.

#### 2. When to Trust the Cheap Check: Weak and Strong Verification for Reasoning
- **arXiv:** [2602.17633](https://arxiv.org/html/2602.17633) | February 2026
- **Authors:** Shayan Kiyani, Sima Noorani, George Pappas, Hamed Hassani (University of Pennsylvania)
- **Overlap:** **Directly formalizes the confidence-gated two-tier verification concept.** Introduces Selective Strong Verification (SSV), an online algorithm with a two-threshold structure: weak verification scores below a lower threshold trigger rejection, scores above an upper threshold trigger acceptance, and scores between the thresholds defer to expensive strong verification. The paper proves optimal policies and Pareto frontiers for the tradeoff between verification cost and reasoning quality.
- **Key distinction from proposal:** This paper operates at a general/abstract level (weak vs. strong verifiers) without specifying SMT/Z3 as the strong verifier or autoformalization as the mechanism. It does not address formalization faithfulness or roundtrip verification. The proposal's contribution would be in instantiating this general framework with specific Z3-based formalization tiers.

#### 3. Pushing the Boundaries of Natural Reasoning: Interleaved Bonus from Formal-Logic Verification
- **arXiv:** [2601.22642](https://arxiv.org/abs/2601.22642) | January 30, 2026
- **Authors:** Chuxue Cao, Jinluan Yang, Haoran Li, et al.
- **Overlap:** **Implements online/streaming formal verification during LLM generation.** The framework "dynamically interleaves formal symbolic verification with the natural language generation process, providing real-time feedback to detect and rectify errors as they occur." Uses a two-stage training pipeline (SFT + policy optimization). Achieves 10.4--14.2% improvement on reasoning benchmarks. This directly addresses the "online" aspect of the proposal.
- **Key distinction from proposal:** Uses formal logic verification for training (RL rewards) rather than inference-time verification. Does not use SMT/Z3 specifically. No confidence gating -- verification is applied uniformly rather than selectively.

#### 4. Grammars of Formal Uncertainty: When to Trust LLMs in Automated Reasoning Tasks
- **Venue:** NeurIPS 2025 | [arXiv 2505.20047](https://arxiv.org/abs/2505.20047)
- **Authors:** Debargha Ganguly, Vikash Singh, et al.
- **Overlap:** **Directly addresses when to trust LLM-generated formalizations, specifically for SMT-based autoformalization.** Introduces a PCFG-based uncertainty taxonomy and a lightweight signal fusion for selective verification, reducing errors by 14--100% with minimal abstention. Finds that SMT-based autoformalization has domain-specific accuracy impact (+34.8% on logical tasks, -44.5% on factual ones).
- **Key distinction from proposal:** Focuses on uncertainty quantification for deciding when to trust formalization outputs, not on a two-tier weak/strong formalization approach. Does not perform online verification during generation.

---

### TIER 2: STRONGLY RELATED -- Papers sharing 2+ core elements

#### 5. HERMES: Towards Efficient and Verifiable Mathematical Reasoning in LLMs
- **arXiv:** [2511.18760](https://arxiv.org/abs/2511.18760) | November 24, 2025
- **Authors:** Azim Ospanov, Zijin Feng, Jiacheng Sun, et al.
- **Overlap:** Interleaves informal reasoning with formal verification checkpoints in Lean 4 during multi-step reasoning. **Implements back-translation verification** for formalization faithfulness. Uses a memory module for proof continuity across reasoning steps. Achieves 67% accuracy improvement with 80% fewer FLOPs.
- **Key distinction:** Uses Lean 4 (not Z3/SMT), focused on mathematical proofs, no confidence gating for selective formalization.

#### 6. Typed Chain-of-Thought: A Curry-Howard Framework for Verifying LLM Reasoning
- **arXiv:** [2510.01069](https://arxiv.org/abs/2510.01069) | October 1, 2025 | Submitted to ICLR 2026
- **Author:** Elija Perrier
- **Overlap:** Formal verification of CoT reasoning by mapping reasoning traces to typed proof structures via the Curry-Howard correspondence. Produces per-step Typed Faithfulness Certificates (TFCs). Achieves 69.8% on GSM8K vs 19.6% baseline through Certified Self-Consistency.
- **Key distinction:** Type-theoretic framework rather than SMT-based. No confidence gating or selective formalization.

#### 7. Safe: Enhancing Mathematical Reasoning via Retrospective Step-aware Formal Verification
- **Venue:** ACL 2025 | [arXiv 2506.04592](https://arxiv.org/abs/2506.04592)
- **Authors:** Chengwu Liu, Ye Yuan, Yichun Yin, et al.
- **Overlap:** Step-aware formal verification using Lean 4 with **four distinct verification states** per step (no verification needed, formalization failed, formalization + proof successful, formalization successful but proof failed). This multi-state approach is conceptually similar to a tiered verification system.
- **Key distinction:** Retrospective (post-hoc) rather than online. Uses Lean 4 rather than Z3. The "tiers" are verification outcomes rather than formalization strength levels.

#### 8. MATH-VF: Step-Wise Formal Verification for LLM-Based Mathematical Problem Solving
- **arXiv:** [2505.20869](https://arxiv.org/abs/2505.20869) | May 27, 2025
- **Authors:** Kuo Zhou, Lu Zhang
- **Overlap:** **Directly uses Z3 and SymPy** for step-by-step verification of LLM mathematical reasoning. Uses a Formalizer + Critic architecture where the Critic leverages Z3/SymPy to verify each step.
- **Key distinction:** No confidence gating -- all steps are verified uniformly. Post-hoc verification rather than online. No two-tier formalization strategy.

#### 9. LogicReward: Incentivizing LLM Reasoning via Step-Wise Logical Supervision
- **Venue:** ICLR 2026 | [arXiv 2512.18196](https://arxiv.org/abs/2512.18196)
- **Authors:** Jundong Xu, Hao Fei, et al.
- **Overlap:** Autoformalization with Soft Unification -- translates natural language to formal logic while capturing implicit assumptions. Step-wise logical supervision using Isabelle theorem prover. Handles the formalization faithfulness problem through soft unification.
- **Key distinction:** Used as a training reward signal rather than inference-time verification. Uses Isabelle rather than Z3.

#### 10. ReProbe: Efficient Test-Time Scaling of Multi-Step Reasoning by Probing Internal States
- **Venue:** ACL 2026 Main | [arXiv 2511.06209](https://arxiv.org/abs/2511.06209)
- **Authors:** Jingwei Ni, Ekaterina Fadeeva, et al.
- **Overlap:** Uses internal LLM states to estimate **confidence in reasoning steps** for selective verification. Lightweight probes (<10M params) that match models 810x larger. Demonstrates that "LLM internal states encode confidence in their reasoning processes."
- **Key distinction:** Confidence-based but uses neural probes rather than formal methods. No formalization component.

---

### TIER 3: RELATED WORK -- Papers sharing 1 core element

#### 11. Online Learnability of Chain-of-Thought Verifiers: Soundness and Completeness Trade-offs
- **arXiv:** [2603.03538](https://arxiv.org/abs/2603.03538) | March 3, 2026
- **Authors:** Maria-Florina Balcan, Avrim Blum, et al.
- **Overlap:** Provides theoretical foundations for online learning of CoT verifiers, with formal analysis of soundness vs. completeness tradeoffs. Proves tight mistake bounds. Highly relevant to the theoretical justification of any two-tier verification system.

#### 12. A Neurosymbolic Approach to Natural Language Formalization and Verification
- **arXiv:** [2511.09008](https://arxiv.org/abs/2511.09008) | November 12, 2025
- **Authors:** Sam Bayless, Stefano Buliani, Darion Cassel, Byron Cook, et al.
- **Overlap:** Two-stage neurosymbolic framework using redundant formalization with semantic equivalence checking for roundtrip verification. Achieves >99% soundness. Directly relevant to formalization faithfulness verification.

#### 13. SpecGuard: Verification-Aware Speculative Decoding for Multi-Step Reasoning
- **arXiv:** [2604.15244](https://arxiv.org/abs/2604.15244) | April 16, 2026
- **Authors:** Kiran Purohit, Ramasuri Narayanam, Soumyabrata Pal
- **Overlap:** Online step-level verification during generation using attention-based grounding scores and log-probability confidence. Shifts verification from tokens to complete reasoning steps.

#### 14. Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning
- **Venue:** VerifAI-2 Workshop, ICLR 2026 | [arXiv 2604.19459](https://arxiv.org/abs/2604.19459)
- **Authors:** Kyuhee Kim, Auguste Poiroux, Antoine Bosselut
- **Overlap:** Directly investigates formalization faithfulness -- finds that high compilation rates do not indicate faithful reasoning. GPT-5 fabricates axioms; DeepSeek-R1 mistranslates premises. Critical evidence supporting the need for roundtrip verification.

#### 15. Logic-Parametric Neuro-Symbolic NLI: Controlling Logical Formalisms for Verifiable LLM Reasoning
- **arXiv:** [2601.05705](https://arxiv.org/abs/2601.05705) | January 9, 2026
- **Authors:** Ali Farjami, Luca Redondi, Marco Valentino
- **Overlap:** Treats logical formalisms as controllable components, embedding multiple logic systems (classical, modal, deontic) and showing different logics excel for different domains. Relevant to the idea of selecting formalization strength.

#### 16. SymCode: A Neurosymbolic Approach to Mathematical Reasoning via Verifiable Code Generation
- **Venue:** EACL 2026 Findings | [arXiv 2510.25975](https://arxiv.org/abs/2510.25975)
- **Authors:** Sina Bagheri Nezhad, Yao Li, Ameeta Agrawal
- **Overlap:** Grounds LLM reasoning in symbolic engines (SymPy) for verifiable computation. Shifts failures from "opaque logical fallacies" to "transparent programmatic errors."

#### 17. Autoformalization in the Era of Large Language Models: A Survey
- **arXiv:** [2505.23486](https://arxiv.org/abs/2505.23486) | May 2025
- **Overlap:** Comprehensive survey of autoformalization approaches including back-translation, evaluation challenges, and faithfulness problems. Essential related work for any formalization-based verification proposal.

#### 18. Solver-Aided Verification of Policy Compliance in Tool-Augmented LLM Agents
- **arXiv:** [2603.20449](https://arxiv.org/abs/2603.20449) | March 2026
- **Overlap:** Uses Z3 SMT solver specifically for verifying LLM agent actions against formal policies.

---

### SUMMARY OF COMPETITIVE LANDSCAPE

**What already exists:**
- Two-tier/semantic routing between strong (SMT) and weak (LLM ensemble) verification: **VERGE**
- Formal theory of weak-strong verification gating with optimal thresholds: **Kiyani et al.**
- Online/streaming formal verification during LLM generation: **Cao et al.**
- Selective formalization based on uncertainty signals: **Ganguly et al. (NeurIPS 2025)**
- Step-wise verification with Z3/SymPy specifically: **MATH-VF**
- Roundtrip/back-translation verification for formalization faithfulness: **HERMES, Bayless et al.**
- Confidence probing for selective verification: **ReProbe (ACL 2026)**

**What appears genuinely novel in the proposal (potential differentiators):**
1. The specific combination of **confidence-gated** (rather than claim-type-based) routing to **two tiers of formalization strength** (weak constraints vs. full FOL) using **Z3 specifically** for **online** multi-step verification is not present in any single paper.
2. VERGE routes by claim type (logical vs. commonsense), not by model confidence. The proposal's confidence-gating mechanism would be distinct.
3. Kiyani et al. provide the theory but no instantiation with formal methods. The proposal would be a concrete instantiation.
4. No existing work combines the "informativeness-precision tradeoff" framing with Z3-based tiered formalization at inference time during streaming generation.

**Highest-risk competitors to monitor:**
- **VERGE** (Singh et al.) -- closest overall system architecture
- **Kiyani et al.** -- closest theoretical framework
- **Ganguly et al.** -- closest on the "when to formalize" question
- **Cao et al.** -- closest on online/streaming verification

agentId: ab345770ed99e781e (use SendMessage with to: 'ab345770ed99e781e' to continue this agent)
&lt;usage>total_tokens: 48731
tool_uses: 44
duration_ms: 290088&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6c674d3f-a74b-4af9-91d1-42fd5eaf4d79",
  "isSidechain": false,
  "promptId": "9f058579-330c-423c-b0cd-eef715c67283",
  "type": "user",
  "uuid": "7e625aa4-a493-4ff8-adbb-ae96ca10b9cc",
  "toolUseResult": {
    "status": "completed",
    "prompt": "You are helping me find competing and concurrent work that may overlap with a research proposal about \"two-tier confidence-gated formalization for online multi-step reasoning verification using Z3.\" \n\nSearch for recent work (2025-2026) on:\n\n1. **Online/streaming verification of LLM reasoning with formal methods**:\n   - \"online verification LLM reasoning Z3 2026\"\n   - \"streaming formal verification chain-of-thought 2025 2026\"\n   - \"real-time constraint checking LLM generation\"\n\n2. **Confidence-gated or selective formalization**:\n   - \"confidence gating formalization LLM\"\n   - \"selective autoformalization reasoning\"\n   - \"when to formalize LLM reasoning\"\n\n3. **Roundtrip verification for formalization faithfulness**:\n   - \"roundtrip verification autoformalization\"\n   - \"back-translation verification formal logic\"\n   - \"formalization faithfulness verification\"\n\n4. **Neurosymbolic reasoning verification recent work**:\n   - \"neurosymbolic reasoning verification 2026 arXiv\"\n   - \"hybrid neural symbolic reasoning verification EMNLP ICLR 2026\"\n   - \"Z3 SMT solver LLM reasoning 2026\"\n\n5. **Specifically check for any work combining these elements**:\n   - \"two-tier formalization constraint reasoning\"\n   - \"weak constraint fallback verification LLM\"\n   - \"informativeness precision tradeoff verification\"\n\n6. **Check recent EMNLP/ACL/ICLR 2026 accepted papers on reasoning verification**:\n   - \"ICLR 2026 accepted papers reasoning verification\"\n   - \"ACL 2026 reasoning verification formal methods\"\n\nFor each relevant paper found, report: title, venue/arXiv ID, date, and how it relates to the proposal. Use WebFetch to read abstracts of the most relevant papers.",
    "agentId": "ab345770ed99e781e",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "I now have comprehensive coverage. Here is my full report of competing and concurrent work.\n\n---\n\n## Competing and Concurrent Work Report\n\nBelow is a comprehensive landscape of recent (2025--2026) work that overlaps with a proposal on \"two-tier confidence-gated formalization for online multi-step reasoning verification using Z3.\" I have organized findings by relevance tier.\n\n---\n\n### TIER 1: MOST DIRECTLY COMPETING -- Papers combining multiple core elements of the proposal\n\n#### 1. VERGE: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning\n- **arXiv:** [2601.20055](https://arxiv.org/abs/2601.20055) | January 27, 2026 (revised May 2, 2026)\n- **Authors:** Vikash Singh, Darion Cassel, Nathaniel Weir, Nick Feng, Sam Bayless\n- **Overlap:** **This is the single most threatening competitor.** VERGE implements a neurosymbolic framework combining LLMs with SMT solvers for iterative verification-guided reasoning. Its three key innovations directly parallel the proposal: (1) **semantic routing** that directs logical claims to symbolic solvers (including SMT) while routing commonsense claims to LLM ensembles -- this is functionally equivalent to a two-tier formalization approach; (2) multi-model consensus via formal semantic equivalence checking; (3) Minimal Correction Subsets (MCS) for precise error localization. The \"soft verifier\" for commonsense claims is capped at a lower maximum score than SMT-verified claims, directly implementing an informativeness-precision tradeoff.\n- **Key distinction from proposal:** VERGE focuses on post-hoc iterative refinement rather than online/streaming verification during generation. It also does not explicitly use confidence scores as a gating mechanism -- the routing is based on claim type (logical vs. commonsense) rather than model confidence.\n\n#### 2. When to Trust the Cheap Check: Weak and Strong Verification for Reasoning\n- **arXiv:** [2602.17633](https://arxiv.org/html/2602.17633) | February 2026\n- **Authors:** Shayan Kiyani, Sima Noorani, George Pappas, Hamed Hassani (University of Pennsylvania)\n- **Overlap:** **Directly formalizes the confidence-gated two-tier verification concept.** Introduces Selective Strong Verification (SSV), an online algorithm with a two-threshold structure: weak verification scores below a lower threshold trigger rejection, scores above an upper threshold trigger acceptance, and scores between the thresholds defer to expensive strong verification. The paper proves optimal policies and Pareto frontiers for the tradeoff between verification cost and reasoning quality.\n- **Key distinction from proposal:** This paper operates at a general/abstract level (weak vs. strong verifiers) without specifying SMT/Z3 as the strong verifier or autoformalization as the mechanism. It does not address formalization faithfulness or roundtrip verification. The proposal's contribution would be in instantiating this general framework with specific Z3-based formalization tiers.\n\n#### 3. Pushing the Boundaries of Natural Reasoning: Interleaved Bonus from Formal-Logic Verification\n- **arXiv:** [2601.22642](https://arxiv.org/abs/2601.22642) | January 30, 2026\n- **Authors:** Chuxue Cao, Jinluan Yang, Haoran Li, et al.\n- **Overlap:** **Implements online/streaming formal verification during LLM generation.** The framework \"dynamically interleaves formal symbolic verification with the natural language generation process, providing real-time feedback to detect and rectify errors as they occur.\" Uses a two-stage training pipeline (SFT + policy optimization). Achieves 10.4--14.2% improvement on reasoning benchmarks. This directly addresses the \"online\" aspect of the proposal.\n- **Key distinction from proposal:** Uses formal logic verification for training (RL rewards) rather than inference-time verification. Does not use SMT/Z3 specifically. No confidence gating -- verification is applied uniformly rather than selectively.\n\n#### 4. Grammars of Formal Uncertainty: When to Trust LLMs in Automated Reasoning Tasks\n- **Venue:** NeurIPS 2025 | [arXiv 2505.20047](https://arxiv.org/abs/2505.20047)\n- **Authors:** Debargha Ganguly, Vikash Singh, et al.\n- **Overlap:** **Directly addresses when to trust LLM-generated formalizations, specifically for SMT-based autoformalization.** Introduces a PCFG-based uncertainty taxonomy and a lightweight signal fusion for selective verification, reducing errors by 14--100% with minimal abstention. Finds that SMT-based autoformalization has domain-specific accuracy impact (+34.8% on logical tasks, -44.5% on factual ones).\n- **Key distinction from proposal:** Focuses on uncertainty quantification for deciding when to trust formalization outputs, not on a two-tier weak/strong formalization approach. Does not perform online verification during generation.\n\n---\n\n### TIER 2: STRONGLY RELATED -- Papers sharing 2+ core elements\n\n#### 5. HERMES: Towards Efficient and Verifiable Mathematical Reasoning in LLMs\n- **arXiv:** [2511.18760](https://arxiv.org/abs/2511.18760) | November 24, 2025\n- **Authors:** Azim Ospanov, Zijin Feng, Jiacheng Sun, et al.\n- **Overlap:** Interleaves informal reasoning with formal verification checkpoints in Lean 4 during multi-step reasoning. **Implements back-translation verification** for formalization faithfulness. Uses a memory module for proof continuity across reasoning steps. Achieves 67% accuracy improvement with 80% fewer FLOPs.\n- **Key distinction:** Uses Lean 4 (not Z3/SMT), focused on mathematical proofs, no confidence gating for selective formalization.\n\n#### 6. Typed Chain-of-Thought: A Curry-Howard Framework for Verifying LLM Reasoning\n- **arXiv:** [2510.01069](https://arxiv.org/abs/2510.01069) | October 1, 2025 | Submitted to ICLR 2026\n- **Author:** Elija Perrier\n- **Overlap:** Formal verification of CoT reasoning by mapping reasoning traces to typed proof structures via the Curry-Howard correspondence. Produces per-step Typed Faithfulness Certificates (TFCs). Achieves 69.8% on GSM8K vs 19.6% baseline through Certified Self-Consistency.\n- **Key distinction:** Type-theoretic framework rather than SMT-based. No confidence gating or selective formalization.\n\n#### 7. Safe: Enhancing Mathematical Reasoning via Retrospective Step-aware Formal Verification\n- **Venue:** ACL 2025 | [arXiv 2506.04592](https://arxiv.org/abs/2506.04592)\n- **Authors:** Chengwu Liu, Ye Yuan, Yichun Yin, et al.\n- **Overlap:** Step-aware formal verification using Lean 4 with **four distinct verification states** per step (no verification needed, formalization failed, formalization + proof successful, formalization successful but proof failed). This multi-state approach is conceptually similar to a tiered verification system.\n- **Key distinction:** Retrospective (post-hoc) rather than online. Uses Lean 4 rather than Z3. The \"tiers\" are verification outcomes rather than formalization strength levels.\n\n#### 8. MATH-VF: Step-Wise Formal Verification for LLM-Based Mathematical Problem Solving\n- **arXiv:** [2505.20869](https://arxiv.org/abs/2505.20869) | May 27, 2025\n- **Authors:** Kuo Zhou, Lu Zhang\n- **Overlap:** **Directly uses Z3 and SymPy** for step-by-step verification of LLM mathematical reasoning. Uses a Formalizer + Critic architecture where the Critic leverages Z3/SymPy to verify each step.\n- **Key distinction:** No confidence gating -- all steps are verified uniformly. Post-hoc verification rather than online. No two-tier formalization strategy.\n\n#### 9. LogicReward: Incentivizing LLM Reasoning via Step-Wise Logical Supervision\n- **Venue:** ICLR 2026 | [arXiv 2512.18196](https://arxiv.org/abs/2512.18196)\n- **Authors:** Jundong Xu, Hao Fei, et al.\n- **Overlap:** Autoformalization with Soft Unification -- translates natural language to formal logic while capturing implicit assumptions. Step-wise logical supervision using Isabelle theorem prover. Handles the formalization faithfulness problem through soft unification.\n- **Key distinction:** Used as a training reward signal rather than inference-time verification. Uses Isabelle rather than Z3.\n\n#### 10. ReProbe: Efficient Test-Time Scaling of Multi-Step Reasoning by Probing Internal States\n- **Venue:** ACL 2026 Main | [arXiv 2511.06209](https://arxiv.org/abs/2511.06209)\n- **Authors:** Jingwei Ni, Ekaterina Fadeeva, et al.\n- **Overlap:** Uses internal LLM states to estimate **confidence in reasoning steps** for selective verification. Lightweight probes (<10M params) that match models 810x larger. Demonstrates that \"LLM internal states encode confidence in their reasoning processes.\"\n- **Key distinction:** Confidence-based but uses neural probes rather than formal methods. No formalization component.\n\n---\n\n### TIER 3: RELATED WORK -- Papers sharing 1 core element\n\n#### 11. Online Learnability of Chain-of-Thought Verifiers: Soundness and Completeness Trade-offs\n- **arXiv:** [2603.03538](https://arxiv.org/abs/2603.03538) | March 3, 2026\n- **Authors:** Maria-Florina Balcan, Avrim Blum, et al.\n- **Overlap:** Provides theoretical foundations for online learning of CoT verifiers, with formal analysis of soundness vs. completeness tradeoffs. Proves tight mistake bounds. Highly relevant to the theoretical justification of any two-tier verification system.\n\n#### 12. A Neurosymbolic Approach to Natural Language Formalization and Verification\n- **arXiv:** [2511.09008](https://arxiv.org/abs/2511.09008) | November 12, 2025\n- **Authors:** Sam Bayless, Stefano Buliani, Darion Cassel, Byron Cook, et al.\n- **Overlap:** Two-stage neurosymbolic framework using redundant formalization with semantic equivalence checking for roundtrip verification. Achieves >99% soundness. Directly relevant to formalization faithfulness verification.\n\n#### 13. SpecGuard: Verification-Aware Speculative Decoding for Multi-Step Reasoning\n- **arXiv:** [2604.15244](https://arxiv.org/abs/2604.15244) | April 16, 2026\n- **Authors:** Kiran Purohit, Ramasuri Narayanam, Soumyabrata Pal\n- **Overlap:** Online step-level verification during generation using attention-based grounding scores and log-probability confidence. Shifts verification from tokens to complete reasoning steps.\n\n#### 14. Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning\n- **Venue:** VerifAI-2 Workshop, ICLR 2026 | [arXiv 2604.19459](https://arxiv.org/abs/2604.19459)\n- **Authors:** Kyuhee Kim, Auguste Poiroux, Antoine Bosselut\n- **Overlap:** Directly investigates formalization faithfulness -- finds that high compilation rates do not indicate faithful reasoning. GPT-5 fabricates axioms; DeepSeek-R1 mistranslates premises. Critical evidence supporting the need for roundtrip verification.\n\n#### 15. Logic-Parametric Neuro-Symbolic NLI: Controlling Logical Formalisms for Verifiable LLM Reasoning\n- **arXiv:** [2601.05705](https://arxiv.org/abs/2601.05705) | January 9, 2026\n- **Authors:** Ali Farjami, Luca Redondi, Marco Valentino\n- **Overlap:** Treats logical formalisms as controllable components, embedding multiple logic systems (classical, modal, deontic) and showing different logics excel for different domains. Relevant to the idea of selecting formalization strength.\n\n#### 16. SymCode: A Neurosymbolic Approach to Mathematical Reasoning via Verifiable Code Generation\n- **Venue:** EACL 2026 Findings | [arXiv 2510.25975](https://arxiv.org/abs/2510.25975)\n- **Authors:** Sina Bagheri Nezhad, Yao Li, Ameeta Agrawal\n- **Overlap:** Grounds LLM reasoning in symbolic engines (SymPy) for verifiable computation. Shifts failures from \"opaque logical fallacies\" to \"transparent programmatic errors.\"\n\n#### 17. Autoformalization in the Era of Large Language Models: A Survey\n- **arXiv:** [2505.23486](https://arxiv.org/abs/2505.23486) | May 2025\n- **Overlap:** Comprehensive survey of autoformalization approaches including back-translation, evaluation challenges, and faithfulness problems. Essential related work for any formalization-based verification proposal.\n\n#### 18. Solver-Aided Verification of Policy Compliance in Tool-Augmented LLM Agents\n- **arXiv:** [2603.20449](https://arxiv.org/abs/2603.20449) | March 2026\n- **Overlap:** Uses Z3 SMT solver specifically for verifying LLM agent actions against formal policies.\n\n---\n\n### SUMMARY OF COMPETITIVE LANDSCAPE\n\n**What already exists:**\n- Two-tier/semantic routing between strong (SMT) and weak (LLM ensemble) verification: **VERGE**\n- Formal theory of weak-strong verification gating with optimal thresholds: **Kiyani et al.**\n- Online/streaming formal verification during LLM generation: **Cao et al.**\n- Selective formalization based on uncertainty signals: **Ganguly et al. (NeurIPS 2025)**\n- Step-wise verification with Z3/SymPy specifically: **MATH-VF**\n- Roundtrip/back-translation verification for formalization faithfulness: **HERMES, Bayless et al.**\n- Confidence probing for selective verification: **ReProbe (ACL 2026)**\n\n**What appears genuinely novel in the proposal (potential differentiators):**\n1. The specific combination of **confidence-gated** (rather than claim-type-based) routing to **two tiers of formalization strength** (weak constraints vs. full FOL) using **Z3 specifically** for **online** multi-step verification is not present in any single paper.\n2. VERGE routes by claim type (logical vs. commonsense), not by model confidence. The proposal's confidence-gating mechanism would be distinct.\n3. Kiyani et al. provide the theory but no instantiation with formal methods. The proposal would be a concrete instantiation.\n4. No existing work combines the \"informativeness-precision tradeoff\" framing with Z3-based tiered formalization at inference time during streaming generation.\n\n**Highest-risk competitors to monitor:**\n- **VERGE** (Singh et al.) -- closest overall system architecture\n- **Kiyani et al.** -- closest theoretical framework\n- **Ganguly et al.** -- closest on the \"when to formalize\" question\n- **Cao et al.** -- closest on online/streaming verification"
      }
    ],
    "totalDurationMs": 290088,
    "totalTokens": 48731,
    "totalToolUseCount": 44,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1465,
      "cache_read_input_tokens": 43409,
      "output_tokens": 3856,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1465
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3856,
          "cache_read_input_tokens": 43409,
          "cache_creation_input_tokens": 1465,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1465,
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
      "otherToolCount": 44
    }
  },
  "sourceToolAssistantUUID": "6c674d3f-a74b-4af9-91d1-42fd5eaf4d79",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ae8c16f5-ce1c-4bce-923e-3afb8499b025",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-12T00:51:27.770Z_

<details><summary>↩ Tool result · `toolu_01YUK9K6fo4MXpA4fRNUfjmr`</summary>

```text
Now I have all the data I need to compile a comprehensive report. Here is the synthesis:

---

## Verification Report: SOTA Benchmark Results

### 1. Qwen3-32B Performance

**AIME 2024:**
- The claimed ~70% appears to come from a specific evaluation run (EvalScope reports 70% with 100 samples). However, the llm-stats.com AIME 2024 leaderboard lists Qwen3-32B at **81.4%**, and designforonline.com reports **80.7%** ("AIME" score). The discrepancy likely reflects different evaluation settings: thinking budget, number of samples, and pass@1 vs. consensus scoring. The **~70% figure is likely an undercount**; with sufficient thinking budget, the model scores closer to **80-81%** on AIME 2024.
- AIME 2025: **73%** (designforonline.com) to **76.7%** (EvalScope with 100 samples). The leaderboard does not rank Qwen3-32B in the visible top-50 for AIME 2025.
- **MATH-500: 95.2-96.1%**. EvalScope reports 95.16%, designforonline.com reports 96.1%. Both are consistent with the claimed ~95.2% baseline -- the 96.1% figure may reflect optimized thinking budget.

**Bottom line:** The claimed ~70% on AIME 2024 is **too low** for thinking mode; the actual figure is closer to **80-81%**. MATH-500 at ~95.2% is approximately accurate (actual range 95.2-96.1%).

Sources:
- [AIME 2024 Leaderboard](https://llm-stats.com/benchmarks/aime-2024) -- Qwen3-32B at 0.814
- [Qwen3-32B Review (designforonline)](https://designforonline.com/ai-models/qwen-qwen3-32b/) -- AIME 80.7%, AIME'25 73%, MATH-500 96.1%
- [EvalScope Qwen3 Evaluation](https://evalscope.readthedocs.io/en/latest/best_practice/qwen3.html) -- AIME'24 70%, MATH-500 95.16% (100-sample run)
- [Qwen3 Technical Report](https://arxiv.org/abs/2505.09388)

---

### 2. HERMES (arXiv 2511.18760) -- All Claims Verified

- **MATH-500: 97.4%** -- Confirmed (Table 1 in the paper, using DeepSeek-V3.1 as base model).
- **AIME'25: 66.7%** -- Confirmed (Table 1, DeepSeek-V3.1).
- **Base model: DeepSeek-V3.1** -- Confirmed. The paper evaluates three base models: Qwen3-8B, OpenAI o3-mini, and DeepSeek-V3.1. The 97.4% / 66.7% numbers are from DeepSeek-V3.1.
- **>60% autoformalization failure at K_t=1** -- Confirmed. Figure 6(a) shows translation failures exceeding 60% when the translation budget is set to 1. As K_t increases, failures drop to 10% or less.
- The paper achieves "up to 67% accuracy improvement on AIME'25 while using 80% fewer total inference FLOPs."

Sources:
- [HERMES arXiv page](https://arxiv.org/abs/2511.18760)
- [HERMES full paper](https://arxiv.org/html/2511.18760)

---

### 3. Current SOTA on ProofWriter, FOLIO, LogiQA

**ProofWriter:**
- Best reported accuracy: **~98.3%** (LeanReasoner and LINC, neurosymbolic approaches). LeanReasoner achieves this with only ~100 in-domain fine-tuning samples.
- Fine-tuned smaller models (Mistral 7B, LLaMA-2 13B) via ProofFOL also reach **~98%**.
- Original T5-based ProofWriter model: up to 96% on depth D3-D5.
- LINC yields **26% absolute gains over CoT for GPT-4** on ProofWriter.
- No single widely tracked "leaderboard" exists; the benchmark is largely considered near-saturated by neurosymbolic methods.

**FOLIO (test set, 226 examples):**
- GPT-4 few-shot: **64.2%**
- GPT-3.5-Turbo few-shot: **58.3%**
- **Logic-LM (GPT-4): 78.1%** -- current best reported
- LINC (GPT-4): **73.1%**
- DetermLR (GPT-4): **77.5%**
- A 9B model matches Logic-LM performance at ~78.9% (per the MoT paper).
- FOLIO remains a challenging benchmark; no model has exceeded ~80%.

**LogiQA:**
- GPT-4 (API): **~72%** on LogiQA 2.0 test set (from "Evaluating the Logical Reasoning Ability of ChatGPT and GPT-4").
- o1-preview: **~90%** on LogiQA (from Nature Scientific Reports comparative evaluation).
- No comprehensive 2026 leaderboard exists for LogiQA specifically; major LLM leaderboards (Vellum, llm-stats) do not track it as a primary benchmark.

Sources:
- [ProofWriter Dataset overview](https://www.emergentmind.com/topics/proofwriter-dataset)
- [FOLIO paper with results](https://arxiv.org/html/2209.00840v2) -- GPT-4 64.2%, Logic-LM 78.1%
- [Logic-LM paper](https://arxiv.org/abs/2305.12295)
- [LogiQA evaluation paper](https://arxiv.org/abs/2304.03439)
- [o1 vs human cognition (Nature)](https://www.nature.com/articles/s41598-025-33629-9)

---

### 4. VERGE (arXiv 2601.20055) -- All Claims Verified

- **18.7% average uplift** -- Confirmed. The abstract states: "VERGE demonstrates an average performance uplift of 18.7% at convergence across a set of reasoning benchmarks compared to single-pass approaches."
- **-8.3% without routing** -- Confirmed. Table 3 ablation study (GPT-OSS-120B):
  - w/o MCS: -6.8%
  - **w/o Routing: -8.3%**
  - Soft-Only: -22.8%
  - Unsat-Core Only: -10.9%
- The routing mechanism is "particularly advantageous for open-ended and commonsense reasoning" (e.g., HLE drops from 30.5% to 15.2% without routing).
- Published January 27, 2026.

Sources:
- [VERGE arXiv page](https://arxiv.org/abs/2601.20055)
- [VERGE full paper](https://arxiv.org/html/2601.20055)
- [VERGE HuggingFace paper page](https://huggingface.co/papers/2601.20055)

---

### 5. Safe (ACL 2025) -- Verified

- **Paper exists**: arXiv 2506.04592, "Safe: Enhancing Mathematical Reasoning in Large Language Models via Retrospective Step-aware Formal Verification."
- **ACL 2025 Main** -- Confirmed. Listed in [ACL Anthology](https://aclanthology.org/2025.acl-long.594/) as ACL 2025 Main conference paper.
- **Step-aware Lean 4 verification** -- Confirmed. The paper "articulate[s] mathematical claims in formal mathematical language Lean 4 at each reasoning step and provide[s] formal proofs to identify hallucinations."
- Introduces **FormalStep** benchmark: 30,809 formal statements for step correctness theorem proving.
- Described as "the first endeavor to utilize formal mathematical language Lean 4 for verifying natural language content generated by LLMs."
- Official code: [github.com/liuchengwucn/Safe](https://github.com/liuchengwucn/Safe)

Sources:
- [Safe arXiv page](https://arxiv.org/abs/2506.04592)
- [Safe ACL Anthology](https://aclanthology.org/2025.acl-long.594/)
- [Safe GitHub](https://github.com/liuchengwucn/Safe)

---

### 6. FoVer -- Verified

- **Paper exists**: arXiv 2505.15960, "Efficient PRM Training Data Synthesis via Formal Verification" (originally titled "Training Step-Level Reasoning Verifiers with Formal Verification Tools").
- **ACL 2026 Findings** -- Confirmed. The GitHub README explicitly states: "(ACL 2026 Findings)."
- Uses formal verification tools (Z3 and Isabelle) to synthesize PRM training data with step-level error labels, eliminating the need for human annotation or additional LLM calls.
- PRMs trained with FoVer outperform baseline PRMs and achieve competitive/superior results compared to SOTA PRMs trained on human-annotated labels.
- FOLIO results (Best-of-K=7): FoVer-Llama3.1-8B achieves 60.1% (vs. 58.6% baseline); FoVer-Qwen2.5-7B at 63.5%.
- Code/data: [github.com/psunlpgroup/FoVer](https://github.com/psunlpgroup/FoVer)

Sources:
- [FoVer arXiv page](https://arxiv.org/abs/2505.15960)
- [FoVer GitHub (ACL 2026 Findings confirmed)](https://github.com/psunlpgroup/FoVer)
- [FoVer project page](https://fover-prm.github.io/)

agentId: a9ce1b71c314b1b30 (use SendMessage with to: 'a9ce1b71c314b1b30' to continue this agent)
&lt;usage>total_tokens: 50823
tool_uses: 52
duration_ms: 354657&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c2e179a9-7e77-44d1-80f3-0f0db9a6d24f",
  "isSidechain": false,
  "promptId": "9f058579-330c-423c-b0cd-eef715c67283",
  "type": "user",
  "uuid": "a265702c-ecb6-4e31-8e68-d2fccc6a87fb",
  "toolUseResult": {
    "status": "completed",
    "prompt": "You are helping me verify current SOTA results on benchmarks relevant to an ML research proposal. Use WebSearch and WebFetch.\n\n1. **Qwen3-32B performance** (the proposed base model):\n   - Search for Qwen3-32B results on AIME 2024, AIME 2025, MATH-500\n   - \"Qwen3-32B AIME 2024 benchmark results\"\n   - \"Qwen3 32B thinking mode performance\"\n   - Check if pass@1 ~70% on AIME 2024 is accurate, or if it's higher (80-81%)\n   - Check MATH-500 baseline (claimed ~95.2%)\n\n2. **HERMES results verification**:\n   - \"HERMES mathematical reasoning verification arXiv 2511.18760\"\n   - Verify: 97.4% on MATH-500, 66.7% on AIME'25\n   - Confirm base model is DeepSeek-V3.1\n   - Check the >60% autoformalization failure at Kₜ=1 claim\n\n3. **Current SOTA on ProofWriter, FOLIO, LogiQA**:\n   - \"ProofWriter SOTA 2025 2026\"\n   - \"FOLIO benchmark SOTA results\"\n   - \"LogiQA benchmark results 2025 2026\"\n\n4. **VERGE results**:\n   - \"VERGE formal refinement LLM reasoning arXiv 2601.20055\"\n   - Verify the 18.7% average uplift claim\n   - Verify the routing ablation (-8.3% without routing)\n\n5. **Safe (ACL 2025) paper**:\n   - \"Safe step-aware formal verification ACL 2025 arXiv 2506.04592\"\n   - Verify it exists and does step-aware Lean4 verification\n\n6. **FoVer paper**:\n   - \"FoVer efficient PRM training formal verification arXiv 2505.15960\"\n   - Verify it's ACL 2026 Findings\n\nReport specific numbers and sources for each.",
    "agentId": "a9ce1b71c314b1b30",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have all the data I need to compile a comprehensive report. Here is the synthesis:\n\n---\n\n## Verification Report: SOTA Benchmark Results\n\n### 1. Qwen3-32B Performance\n\n**AIME 2024:**\n- The claimed ~70% appears to come from a specific evaluation run (EvalScope reports 70% with 100 samples). However, the llm-stats.com AIME 2024 leaderboard lists Qwen3-32B at **81.4%**, and designforonline.com reports **80.7%** (\"AIME\" score). The discrepancy likely reflects different evaluation settings: thinking budget, number of samples, and pass@1 vs. consensus scoring. The **~70% figure is likely an undercount**; with sufficient thinking budget, the model scores closer to **80-81%** on AIME 2024.\n- AIME 2025: **73%** (designforonline.com) to **76.7%** (EvalScope with 100 samples). The leaderboard does not rank Qwen3-32B in the visible top-50 for AIME 2025.\n- **MATH-500: 95.2-96.1%**. EvalScope reports 95.16%, designforonline.com reports 96.1%. Both are consistent with the claimed ~95.2% baseline -- the 96.1% figure may reflect optimized thinking budget.\n\n**Bottom line:** The claimed ~70% on AIME 2024 is **too low** for thinking mode; the actual figure is closer to **80-81%**. MATH-500 at ~95.2% is approximately accurate (actual range 95.2-96.1%).\n\nSources:\n- [AIME 2024 Leaderboard](https://llm-stats.com/benchmarks/aime-2024) -- Qwen3-32B at 0.814\n- [Qwen3-32B Review (designforonline)](https://designforonline.com/ai-models/qwen-qwen3-32b/) -- AIME 80.7%, AIME'25 73%, MATH-500 96.1%\n- [EvalScope Qwen3 Evaluation](https://evalscope.readthedocs.io/en/latest/best_practice/qwen3.html) -- AIME'24 70%, MATH-500 95.16% (100-sample run)\n- [Qwen3 Technical Report](https://arxiv.org/abs/2505.09388)\n\n---\n\n### 2. HERMES (arXiv 2511.18760) -- All Claims Verified\n\n- **MATH-500: 97.4%** -- Confirmed (Table 1 in the paper, using DeepSeek-V3.1 as base model).\n- **AIME'25: 66.7%** -- Confirmed (Table 1, DeepSeek-V3.1).\n- **Base model: DeepSeek-V3.1** -- Confirmed. The paper evaluates three base models: Qwen3-8B, OpenAI o3-mini, and DeepSeek-V3.1. The 97.4% / 66.7% numbers are from DeepSeek-V3.1.\n- **>60% autoformalization failure at K_t=1** -- Confirmed. Figure 6(a) shows translation failures exceeding 60% when the translation budget is set to 1. As K_t increases, failures drop to 10% or less.\n- The paper achieves \"up to 67% accuracy improvement on AIME'25 while using 80% fewer total inference FLOPs.\"\n\nSources:\n- [HERMES arXiv page](https://arxiv.org/abs/2511.18760)\n- [HERMES full paper](https://arxiv.org/html/2511.18760)\n\n---\n\n### 3. Current SOTA on ProofWriter, FOLIO, LogiQA\n\n**ProofWriter:**\n- Best reported accuracy: **~98.3%** (LeanReasoner and LINC, neurosymbolic approaches). LeanReasoner achieves this with only ~100 in-domain fine-tuning samples.\n- Fine-tuned smaller models (Mistral 7B, LLaMA-2 13B) via ProofFOL also reach **~98%**.\n- Original T5-based ProofWriter model: up to 96% on depth D3-D5.\n- LINC yields **26% absolute gains over CoT for GPT-4** on ProofWriter.\n- No single widely tracked \"leaderboard\" exists; the benchmark is largely considered near-saturated by neurosymbolic methods.\n\n**FOLIO (test set, 226 examples):**\n- GPT-4 few-shot: **64.2%**\n- GPT-3.5-Turbo few-shot: **58.3%**\n- **Logic-LM (GPT-4): 78.1%** -- current best reported\n- LINC (GPT-4): **73.1%**\n- DetermLR (GPT-4): **77.5%**\n- A 9B model matches Logic-LM performance at ~78.9% (per the MoT paper).\n- FOLIO remains a challenging benchmark; no model has exceeded ~80%.\n\n**LogiQA:**\n- GPT-4 (API): **~72%** on LogiQA 2.0 test set (from \"Evaluating the Logical Reasoning Ability of ChatGPT and GPT-4\").\n- o1-preview: **~90%** on LogiQA (from Nature Scientific Reports comparative evaluation).\n- No comprehensive 2026 leaderboard exists for LogiQA specifically; major LLM leaderboards (Vellum, llm-stats) do not track it as a primary benchmark.\n\nSources:\n- [ProofWriter Dataset overview](https://www.emergentmind.com/topics/proofwriter-dataset)\n- [FOLIO paper with results](https://arxiv.org/html/2209.00840v2) -- GPT-4 64.2%, Logic-LM 78.1%\n- [Logic-LM paper](https://arxiv.org/abs/2305.12295)\n- [LogiQA evaluation paper](https://arxiv.org/abs/2304.03439)\n- [o1 vs human cognition (Nature)](https://www.nature.com/articles/s41598-025-33629-9)\n\n---\n\n### 4. VERGE (arXiv 2601.20055) -- All Claims Verified\n\n- **18.7% average uplift** -- Confirmed. The abstract states: \"VERGE demonstrates an average performance uplift of 18.7% at convergence across a set of reasoning benchmarks compared to single-pass approaches.\"\n- **-8.3% without routing** -- Confirmed. Table 3 ablation study (GPT-OSS-120B):\n  - w/o MCS: -6.8%\n  - **w/o Routing: -8.3%**\n  - Soft-Only: -22.8%\n  - Unsat-Core Only: -10.9%\n- The routing mechanism is \"particularly advantageous for open-ended and commonsense reasoning\" (e.g., HLE drops from 30.5% to 15.2% without routing).\n- Published January 27, 2026.\n\nSources:\n- [VERGE arXiv page](https://arxiv.org/abs/2601.20055)\n- [VERGE full paper](https://arxiv.org/html/2601.20055)\n- [VERGE HuggingFace paper page](https://huggingface.co/papers/2601.20055)\n\n---\n\n### 5. Safe (ACL 2025) -- Verified\n\n- **Paper exists**: arXiv 2506.04592, \"Safe: Enhancing Mathematical Reasoning in Large Language Models via Retrospective Step-aware Formal Verification.\"\n- **ACL 2025 Main** -- Confirmed. Listed in [ACL Anthology](https://aclanthology.org/2025.acl-long.594/) as ACL 2025 Main conference paper.\n- **Step-aware Lean 4 verification** -- Confirmed. The paper \"articulate[s] mathematical claims in formal mathematical language Lean 4 at each reasoning step and provide[s] formal proofs to identify hallucinations.\"\n- Introduces **FormalStep** benchmark: 30,809 formal statements for step correctness theorem proving.\n- Described as \"the first endeavor to utilize formal mathematical language Lean 4 for verifying natural language content generated by LLMs.\"\n- Official code: [github.com/liuchengwucn/Safe](https://github.com/liuchengwucn/Safe)\n\nSources:\n- [Safe arXiv page](https://arxiv.org/abs/2506.04592)\n- [Safe ACL Anthology](https://aclanthology.org/2025.acl-long.594/)\n- [Safe GitHub](https://github.com/liuchengwucn/Safe)\n\n---\n\n### 6. FoVer -- Verified\n\n- **Paper exists**: arXiv 2505.15960, \"Efficient PRM Training Data Synthesis via Formal Verification\" (originally titled \"Training Step-Level Reasoning Verifiers with Formal Verification Tools\").\n- **ACL 2026 Findings** -- Confirmed. The GitHub README explicitly states: \"(ACL 2026 Findings).\"\n- Uses formal verification tools (Z3 and Isabelle) to synthesize PRM training data with step-level error labels, eliminating the need for human annotation or additional LLM calls.\n- PRMs trained with FoVer outperform baseline PRMs and achieve competitive/superior results compared to SOTA PRMs trained on human-annotated labels.\n- FOLIO results (Best-of-K=7): FoVer-Llama3.1-8B achieves 60.1% (vs. 58.6% baseline); FoVer-Qwen2.5-7B at 63.5%.\n- Code/data: [github.com/psunlpgroup/FoVer](https://github.com/psunlpgroup/FoVer)\n\nSources:\n- [FoVer arXiv page](https://arxiv.org/abs/2505.15960)\n- [FoVer GitHub (ACL 2026 Findings confirmed)](https://github.com/psunlpgroup/FoVer)\n- [FoVer project page](https://fover-prm.github.io/)"
      }
    ],
    "totalDurationMs": 354657,
    "totalTokens": 50823,
    "totalToolUseCount": 52,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1002,
      "cache_read_input_tokens": 47225,
      "output_tokens": 2595,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1002
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2595,
          "cache_read_input_tokens": 47225,
          "cache_creation_input_tokens": 1002,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1002,
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
      "otherToolCount": 52
    }
  },
  "sourceToolAssistantUUID": "c2e179a9-7e77-44d1-80f3-0f0db9a6d24f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ae8c16f5-ce1c-4bce-923e-3afb8499b025",
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
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-11 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "a265702c-ecb6-4e31-8e68-d2fccc6a87fb",
  "sessionId": "ae8c16f5-ce1c-4bce-923e-3afb8499b025"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "Two-tier confidence-gated formalization for online derivation verification",
  "sessionId": "ae8c16f5-ce1c-4bce-923e-3afb8499b025"
}
```

---

### Assistant

_source line 22 · 2026-05-12T00:51:50.683Z_

<details><summary>Logged reasoning block</summary>

```text
Excellent. I now have comprehensive verification results from all four agents. Let me synthesize and also search for a few more critical items that the agents identified - particularly the Kiyani et al. paper on weak-strong verification gating, which seems like a very significant competitor that the proposal doesn't cite.

Let me also check on the MATP paper cited in the references, and verify the EMNLP 2026 ARR deadline.

Key findings so far:

1. **interwhen**: Confirmed. The proposal's characterization is NOW accurate (state-level vs assertion-level distinction). Correctly notes it doesn't work on derivation tasks.


2. **VeriCoT**: Confirmed as ICLR 2026 poster with post-hoc verification using cumulative Z3 constraints - the proposal characterizes this accurately now.
3. **"Do LLMs Game Formalization?"**: The paper exists but the proposal oversimplifies its findings - it only shows gaming in two-stage pipelines, not in unified generation, which is a meaningful distinction the proposal glosses over.
4. **Roundtrip verification**: Confirmed to exist, though the cost comparison appears cherry-picked with Claude-only numbers (7.21 vs 12.27) while GPT shows the opposite pattern.
5. **ReForm**: Confirmed with the +22.6 improvement figure.
6. **HERMES**: All claims check out, using DeepSeek-V3.1 as the base model.
7. **Safe**: Confirmed as ACL 2025 Main conference paper.
8. **FoVer**: Confirmed for ACL 2026 Findings track.
9. **VERGE**: All claims verified.
10. **Qwen3-32B AIME 2024**: The ~70% figure is pass@1 under specific conditions; with thinking mode enabled it reaches 80-81%, and the proposal now correctly reflects this range.
11. **Critical gap identified**: Kiyani et al.'s "When to Trust the Cheap Check" (arXiv 2602.17633, Feb 2026) formalizes the exact two-tier weak-strong verification framework with optimal thresholds, but it's not cited in the proposal.

I'm also noting several other relevant papers on verification approaches—Cao et al. on streaming formal verification, MATH-VF with step-wise Z3+SymPy checking, and SpecGuard for online step-level verification during generation. The Kiyani paper seems like the most critical omission since it directly addresses the core informativeness-precision tradeoff concept.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a265702c-ecb6-4e31-8e68-d2fccc6a87fb",
  "isSidechain": false,
  "requestId": "req_011CawkwioSZJcPp7QCXmnvM",
  "type": "assistant",
  "uuid": "141b33e5-aad0-473c-ba07-540f13261d09",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ae8c16f5-ce1c-4bce-923e-3afb8499b025",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RUgexf2c4Bths9GY3YmLBD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12836,
      "cache_read_input_tokens": 35718,
      "output_tokens": 1537,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12836,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1537,
          "cache_read_input_tokens": 35718,
          "cache_creation_input_tokens": 12836,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12836
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

_source line 23 · 2026-05-12T00:51:50.685Z_

Important findings emerging. Let me verify a critical uncited competitor and check the EMNLP deadline.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "141b33e5-aad0-473c-ba07-540f13261d09",
  "isSidechain": false,
  "requestId": "req_011CawkwioSZJcPp7QCXmnvM",
  "type": "assistant",
  "uuid": "eb40a252-e1c7-4bcc-8718-0f84099eda62",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ae8c16f5-ce1c-4bce-923e-3afb8499b025",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RUgexf2c4Bths9GY3YmLBD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12836,
      "cache_read_input_tokens": 35718,
      "output_tokens": 1537,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12836,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1537,
          "cache_read_input_tokens": 35718,
          "cache_creation_input_tokens": 12836,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12836
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

_source line 24 · 2026-05-12T00:51:59.675Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01DdsbzkBrMuj3beeVaqAPFV`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Verify critical uncited competitor",
  "prompt": "I need to verify a potentially critical competing paper that was not cited in a research proposal I'm reviewing. Use WebSearch and WebFetch to find and read this paper.\n\n**Paper: \"When to Trust the Cheap Check: Weak and Strong Verification for Reasoning\"** (arXiv 2602.17633, February 2026)\n- Authors: Shayan Kiyani, Sima Noorani, George Pappas, Hamed Hassani (University of Pennsylvania)\n\nI need to know:\n1. Does this paper exist? Read its abstract via WebFetch on https://arxiv.org/abs/2602.17633\n2. Does it formalize a two-tier verification concept with weak and strong verifiers?\n3. Does it define an informativeness-precision or cost-quality tradeoff?\n4. Does it prove optimal policies or Pareto frontiers?\n5. Does it propose \"Selective Strong Verification (SSV)\"?\n6. How does it relate to a proposal about \"two-tier confidence-gated formalization\" with Z3-based verification?\n\nAlso search for:\n- \"weak strong verification reasoning 2026\"\n- \"selective verification reasoning LLM cost tradeoff\"\n\nThis is critical because if this paper already formalizes the two-tier verification tradeoff concept, it directly undermines the novelty of a proposal claiming the informativeness-precision tradeoff framework as a primary contribution."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eb40a252-e1c7-4bcc-8718-0f84099eda62",
  "isSidechain": false,
  "requestId": "req_011CawkwioSZJcPp7QCXmnvM",
  "type": "assistant",
  "uuid": "48aadf9e-628b-4fa8-ba9e-ce8e0e74c15d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ae8c16f5-ce1c-4bce-923e-3afb8499b025",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RUgexf2c4Bths9GY3YmLBD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12836,
      "cache_read_input_tokens": 35718,
      "output_tokens": 1537,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12836,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1537,
          "cache_read_input_tokens": 35718,
          "cache_creation_input_tokens": 12836,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12836
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

_source line 25 · 2026-05-12T00:52:07.636Z_

<details open><summary>🔧 Tool call — Agent · `toolu_014xES8PDD266YVP5cYLZk3r`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Verify EMNLP deadline and additional refs",
  "prompt": "I need to verify several things for an ML research review. Use WebSearch.\n\n1. **EMNLP 2026 ARR submission deadline**: Search for \"EMNLP 2026 submission deadline\" and \"ARR May 2026 deadline\". The proposal claims the ARR submission deadline is May 25, 2026. Is this correct?\n\n2. **\"Beyond Correctness: Exposing LLM-generated Logical Flaws via Multi-step Automated Theorem Proving\" (MATP, claimed ICSE 2026)**: Search for this paper. Does it exist? Is it at ICSE 2026?\n\n3. **\"Autoformalize Mathematical Statements by Symbolic Equivalence and Semantic Consistency\" (NeurIPS 2024, arXiv 2410.20936)**: Search for this paper and verify:\n   - Title is \"Autoformalize\" not \"Autoformalizing\"\n   - Results: 45.8% on MATH with combined method, 8.3% absolute improvement\n   - Uses Z3, CVC5, and Isabelle/HOL\n\n4. **Adaptive LLM-Symbolic Reasoning (EACL 2026, arXiv 2510.06774)**: Verify this paper exists and is at EACL 2026.\n\n5. **ProcessBench (ACL 2025)**: Verify this exists.\n\nReport specific findings for each."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "48aadf9e-628b-4fa8-ba9e-ce8e0e74c15d",
  "isSidechain": false,
  "requestId": "req_011CawkwioSZJcPp7QCXmnvM",
  "type": "assistant",
  "uuid": "690ed330-4f5c-46ef-a830-81906525b7b1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ae8c16f5-ce1c-4bce-923e-3afb8499b025",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RUgexf2c4Bths9GY3YmLBD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12836,
      "cache_read_input_tokens": 35718,
      "output_tokens": 1537,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12836,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1537,
          "cache_read_input_tokens": 35718,
          "cache_creation_input_tokens": 12836,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12836
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

_source line 26 · 2026-05-12T00:53:18.487Z_

<details><summary>↩ Tool result · `toolu_01DdsbzkBrMuj3beeVaqAPFV`</summary>

```text
Excellent. I now have comprehensive information to give you a thorough assessment. Here is my analysis:

---

## Verification Report: "When to Trust the Cheap Check" (arXiv 2602.17633)

### 1. Does this paper exist?

**Yes, confirmed.** The paper "When to Trust the Cheap Check: Weak and Strong Verification for Reasoning" (arXiv 2602.17633, February 2026) is a real, published preprint by Shayan Kiyani, Sima Noorani, George Pappas, and Hamed Hassani at the University of Pennsylvania. It is indexed on arXiv, ResearchGate, AlphaXiv, and Google Scholar.

### 2. Does it formalize a two-tier verification concept?

**Yes, this is the paper's central contribution.** It explicitly formalizes:
- **Strong verification** `g: P x R -> {0,1}` -- a binary, authoritative but expensive oracle (e.g., human inspection, domain-specific execution).
- **Weak verification** `w: P x R -> [0,1]` -- a continuous, cheap but noisy signal (e.g., reward models, LLM self-consistency).

The framework defines a **three-action policy** mapping weak scores to decisions: Accept, Reject, or Query the strong verifier. This is precisely a two-tier verification architecture.

### 3. Does it define a cost-quality tradeoff?

**Yes.** The paper tracks three competing objectives:
- **Type-I Error (incorrect acceptance)** -- accepting responses the strong verifier would deem wrong.
- **Type-II Error (incorrect rejection)** -- rejecting correct responses.
- **Strong verification frequency** -- the cost metric (computational load, latency, human effort).

The paper explicitly characterizes a **Pareto frontier** between reasoning quality and verification cost, allowing practitioners to interpolate between weak-only (minimal cost, lower reliability) and strong-only (maximum reliability, high cost) regimes. While it does not use the exact phrase "informativeness-precision tradeoff," the formalization captures the same conceptual space.

### 4. Does it prove optimal policies or Pareto frontiers?

**Yes, with formal theorems.**

- **Theorem 4.2** proves that under calibration assumptions, optimal policies have a **two-threshold structure**:
  - Reject if `w < t_low`
  - Query strong verifier if `t_low <= w <= t_high`
  - Accept if `w > t_high`

- **Proposition 4.3** characterizes the optimal objective value as depending on **calibration** (whether `Pr[g=1|w=p] = p`) and **sharpness** (how concentrated weak scores are near 0 or 1).

- **Theorem 5.1** provides finite-time guarantees for the online algorithm, bounding Type-I and Type-II errors with slack terms that decay as more strong verification observations accumulate. These guarantees are **distribution-free** -- no assumptions on the query stream, language model, or weak verifier quality.

### 5. Does it propose "Selective Strong Verification (SSV)"?

**Yes.** The paper proposes **"Selective Strong Verification" (Algorithm 1)** as its main practical contribution. SSV maintains adaptive thresholds that adjust based on observed strong verification feedback, using randomized exploration to maintain unbiased feedback even in decisive regions. On Sudoku experiments, SSV achieves comparable accuracy (43.1% at alpha=beta=0.01) while requiring **46% fewer strong verification calls** compared to an oracle baseline.

### 6. How does it relate to a "two-tier confidence-gated formalization" proposal with Z3-based verification?

**This is the critical overlap analysis:**

| Concept | Kiyani et al. (2602.17633) | Proposal under review |
|---|---|---|
| Two-tier verification hierarchy | Formalized (weak vs. strong oracles) | "Two-tier confidence-gated formalization" |
| Confidence thresholding / gating | Two-threshold optimal policy (Theorem 4.2) | "Confidence-gated" mechanism |
| Cost-quality tradeoff formalization | Three-metric framework with Pareto frontier | "Informativeness-precision tradeoff" |
| Selective deferral to expensive verifier | SSV algorithm with online guarantees | Selective use of Z3-based strong verification |
| Formal proofs of optimality | Theorems 4.2, 5.1; Proposition 4.3 | Claimed as contribution |

**Key differences:** The Kiyani et al. paper does **not** use Z3/SMT solvers or formal verification tools. Their "strong verifier" is abstract (human inspection, domain execution). A proposal that specifically instantiates the strong verifier as Z3 for mathematical/logical domains would add implementation specificity but would not be introducing the conceptual framework itself -- that framework is already formalized in this paper.

### Assessment of Novelty Impact

**This is a significant prior art concern.** If the proposal under review claims the "informativeness-precision tradeoff framework" or "two-tier confidence-gated verification" as a primary theoretical contribution, arXiv 2602.17633 directly undermines that claim. Kiyani et al. have already:

1. Formalized the two-tier weak/strong verification framework with formal definitions.
2. Proven the optimal two-threshold gating policy structure.
3. Characterized the Pareto frontier between verification cost and reasoning quality.
4. Developed an online algorithm (SSV) with distribution-free finite-time guarantees.
5. Validated experimentally on math reasoning and sequential reasoning tasks.

A proposal could still claim novelty in the **specific instantiation** (e.g., using Z3 as the strong verifier, targeting a particular domain) or in extending the framework, but it **cannot claim the two-tier verification tradeoff formalization itself as novel** without citing and differentiating from this work.

**Recommendation:** This paper must be cited in any proposal claiming contributions in two-tier verification tradeoff formalization. The proposal should be repositioned to clearly articulate what it adds beyond the Kiyani et al. framework.

---

Sources:
- [When to Trust the Cheap Check: Weak and Strong Verification for Reasoning (arXiv abstract)](https://arxiv.org/abs/2602.17633)
- [When to Trust the Cheap Check (full HTML)](https://arxiv.org/html/2602.17633)
- [ResearchGate listing](https://www.researchgate.net/publication/400970108_When_to_Trust_the_Cheap_Check_Weak_and_Strong_Verification_for_Reasoning)
- [AlphaXiv overview](https://www.alphaxiv.org/overview/2602.17633)
- [Shayan Kiyani - Google Scholar](https://scholar.google.com/citations?user=R1oEJ0YAAAAJ&hl=en)

agentId: a36cb1baed46c0081 (use SendMessage with to: 'a36cb1baed46c0081' to continue this agent)
&lt;usage>total_tokens: 17614
tool_uses: 7
duration_ms: 78807&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "48aadf9e-628b-4fa8-ba9e-ce8e0e74c15d",
  "isSidechain": false,
  "promptId": "9f058579-330c-423c-b0cd-eef715c67283",
  "type": "user",
  "uuid": "55c3eb69-e995-48fb-9f77-efb73f245821",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to verify a potentially critical competing paper that was not cited in a research proposal I'm reviewing. Use WebSearch and WebFetch to find and read this paper.\n\n**Paper: \"When to Trust the Cheap Check: Weak and Strong Verification for Reasoning\"** (arXiv 2602.17633, February 2026)\n- Authors: Shayan Kiyani, Sima Noorani, George Pappas, Hamed Hassani (University of Pennsylvania)\n\nI need to know:\n1. Does this paper exist? Read its abstract via WebFetch on https://arxiv.org/abs/2602.17633\n2. Does it formalize a two-tier verification concept with weak and strong verifiers?\n3. Does it define an informativeness-precision or cost-quality tradeoff?\n4. Does it prove optimal policies or Pareto frontiers?\n5. Does it propose \"Selective Strong Verification (SSV)\"?\n6. How does it relate to a proposal about \"two-tier confidence-gated formalization\" with Z3-based verification?\n\nAlso search for:\n- \"weak strong verification reasoning 2026\"\n- \"selective verification reasoning LLM cost tradeoff\"\n\nThis is critical because if this paper already formalizes the two-tier verification tradeoff concept, it directly undermines the novelty of a proposal claiming the informativeness-precision tradeoff framework as a primary contribution.",
    "agentId": "a36cb1baed46c0081",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Excellent. I now have comprehensive information to give you a thorough assessment. Here is my analysis:\n\n---\n\n## Verification Report: \"When to Trust the Cheap Check\" (arXiv 2602.17633)\n\n### 1. Does this paper exist?\n\n**Yes, confirmed.** The paper \"When to Trust the Cheap Check: Weak and Strong Verification for Reasoning\" (arXiv 2602.17633, February 2026) is a real, published preprint by Shayan Kiyani, Sima Noorani, George Pappas, and Hamed Hassani at the University of Pennsylvania. It is indexed on arXiv, ResearchGate, AlphaXiv, and Google Scholar.\n\n### 2. Does it formalize a two-tier verification concept?\n\n**Yes, this is the paper's central contribution.** It explicitly formalizes:\n- **Strong verification** `g: P x R -> {0,1}` -- a binary, authoritative but expensive oracle (e.g., human inspection, domain-specific execution).\n- **Weak verification** `w: P x R -> [0,1]` -- a continuous, cheap but noisy signal (e.g., reward models, LLM self-consistency).\n\nThe framework defines a **three-action policy** mapping weak scores to decisions: Accept, Reject, or Query the strong verifier. This is precisely a two-tier verification architecture.\n\n### 3. Does it define a cost-quality tradeoff?\n\n**Yes.** The paper tracks three competing objectives:\n- **Type-I Error (incorrect acceptance)** -- accepting responses the strong verifier would deem wrong.\n- **Type-II Error (incorrect rejection)** -- rejecting correct responses.\n- **Strong verification frequency** -- the cost metric (computational load, latency, human effort).\n\nThe paper explicitly characterizes a **Pareto frontier** between reasoning quality and verification cost, allowing practitioners to interpolate between weak-only (minimal cost, lower reliability) and strong-only (maximum reliability, high cost) regimes. While it does not use the exact phrase \"informativeness-precision tradeoff,\" the formalization captures the same conceptual space.\n\n### 4. Does it prove optimal policies or Pareto frontiers?\n\n**Yes, with formal theorems.**\n\n- **Theorem 4.2** proves that under calibration assumptions, optimal policies have a **two-threshold structure**:\n  - Reject if `w < t_low`\n  - Query strong verifier if `t_low <= w <= t_high`\n  - Accept if `w > t_high`\n\n- **Proposition 4.3** characterizes the optimal objective value as depending on **calibration** (whether `Pr[g=1|w=p] = p`) and **sharpness** (how concentrated weak scores are near 0 or 1).\n\n- **Theorem 5.1** provides finite-time guarantees for the online algorithm, bounding Type-I and Type-II errors with slack terms that decay as more strong verification observations accumulate. These guarantees are **distribution-free** -- no assumptions on the query stream, language model, or weak verifier quality.\n\n### 5. Does it propose \"Selective Strong Verification (SSV)\"?\n\n**Yes.** The paper proposes **\"Selective Strong Verification\" (Algorithm 1)** as its main practical contribution. SSV maintains adaptive thresholds that adjust based on observed strong verification feedback, using randomized exploration to maintain unbiased feedback even in decisive regions. On Sudoku experiments, SSV achieves comparable accuracy (43.1% at alpha=beta=0.01) while requiring **46% fewer strong verification calls** compared to an oracle baseline.\n\n### 6. How does it relate to a \"two-tier confidence-gated formalization\" proposal with Z3-based verification?\n\n**This is the critical overlap analysis:**\n\n| Concept | Kiyani et al. (2602.17633) | Proposal under review |\n|---|---|---|\n| Two-tier verification hierarchy | Formalized (weak vs. strong oracles) | \"Two-tier confidence-gated formalization\" |\n| Confidence thresholding / gating | Two-threshold optimal policy (Theorem 4.2) | \"Confidence-gated\" mechanism |\n| Cost-quality tradeoff formalization | Three-metric framework with Pareto frontier | \"Informativeness-precision tradeoff\" |\n| Selective deferral to expensive verifier | SSV algorithm with online guarantees | Selective use of Z3-based strong verification |\n| Formal proofs of optimality | Theorems 4.2, 5.1; Proposition 4.3 | Claimed as contribution |\n\n**Key differences:** The Kiyani et al. paper does **not** use Z3/SMT solvers or formal verification tools. Their \"strong verifier\" is abstract (human inspection, domain execution). A proposal that specifically instantiates the strong verifier as Z3 for mathematical/logical domains would add implementation specificity but would not be introducing the conceptual framework itself -- that framework is already formalized in this paper.\n\n### Assessment of Novelty Impact\n\n**This is a significant prior art concern.** If the proposal under review claims the \"informativeness-precision tradeoff framework\" or \"two-tier confidence-gated verification\" as a primary theoretical contribution, arXiv 2602.17633 directly undermines that claim. Kiyani et al. have already:\n\n1. Formalized the two-tier weak/strong verification framework with formal definitions.\n2. Proven the optimal two-threshold gating policy structure.\n3. Characterized the Pareto frontier between verification cost and reasoning quality.\n4. Developed an online algorithm (SSV) with distribution-free finite-time guarantees.\n5. Validated experimentally on math reasoning and sequential reasoning tasks.\n\nA proposal could still claim novelty in the **specific instantiation** (e.g., using Z3 as the strong verifier, targeting a particular domain) or in extending the framework, but it **cannot claim the two-tier verification tradeoff formalization itself as novel** without citing and differentiating from this work.\n\n**Recommendation:** This paper must be cited in any proposal claiming contributions in two-tier verification tradeoff formalization. The proposal should be repositioned to clearly articulate what it adds beyond the Kiyani et al. framework.\n\n---\n\nSources:\n- [When to Trust the Cheap Check: Weak and Strong Verification for Reasoning (arXiv abstract)](https://arxiv.org/abs/2602.17633)\n- [When to Trust the Cheap Check (full HTML)](https://arxiv.org/html/2602.17633)\n- [ResearchGate listing](https://www.researchgate.net/publication/400970108_When_to_Trust_the_Cheap_Check_Weak_and_Strong_Verification_for_Reasoning)\n- [AlphaXiv overview](https://www.alphaxiv.org/overview/2602.17633)\n- [Shayan Kiyani - Google Scholar](https://scholar.google.com/citations?user=R1oEJ0YAAAAJ&hl=en)"
      }
    ],
    "totalDurationMs": 78807,
    "totalTokens": 17614,
    "totalToolUseCount": 7,
    "usage": {
      "input_tokens": 225,
      "cache_creation_input_tokens": 2212,
      "cache_read_input_tokens": 13517,
      "output_tokens": 1660,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2212
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 225,
          "output_tokens": 1660,
          "cache_read_input_tokens": 13517,
          "cache_creation_input_tokens": 2212,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2212,
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
  "sourceToolAssistantUUID": "48aadf9e-628b-4fa8-ba9e-ce8e0e74c15d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ae8c16f5-ce1c-4bce-923e-3afb8499b025",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-12T00:53:38.519Z_

<details><summary>↩ Tool result · `toolu_014xES8PDD266YVP5cYLZk3r`</summary>

```text
Here are my findings for each item:

---

## 1. EMNLP 2026 ARR Submission Deadline

**CONFIRMED.** The ARR submission deadline for EMNLP 2026 long and short papers is **May 25, 2026**. The proposal's claim is correct. EMNLP 2026 will be held in Budapest, Hungary, October 24-29, 2026. Other key dates: commitment deadline August 2, notification August 20, camera-ready September 20.

---

## 2. "Beyond Correctness" / MATP (ICSE 2026)

**The paper exists and is at ICSE 2026, but there is a title discrepancy.** The full title on arXiv (2512.23511) and the ICSE 2026 Research Track listing is:

> "Beyond Correctness: Exposing LLM-generated Logical Flaws **in Reasoning** via Multi-step Automated Theorem Proving"

The proposal omits "in Reasoning" from the title. Additionally, the abbreviation stands for "Multi-step **Automatic** Theorem Proving" (not "Automated"), though this varies between sources. The paper is confirmed as accepted to the ICSE 2026 Research Track.

---

## 3. "Autoformalize Mathematical Statements..." (NeurIPS 2024, arXiv 2410.20936)

**The paper exists and is confirmed at NeurIPS 2024, but there are issues with the claimed details:**

- **Title discrepancy:** The official NeurIPS proceedings and ResearchGate use "**Autoformalize**" (no -ing). However, the arXiv HTML rendering and PDF use "**Autoformalizing**" (with -ing). So both forms appear in different authoritative sources. The NeurIPS poster page uses "Autoformalize" without the -ing.

- **Tools used:** The paper uses **Z3, CVC5, and Isabelle/HOL** (specifically, 12 Isabelle/HOL tactics plus Z3 and CVC5 as SMT solvers). This claim checks out.

- **Results (45.8% on MATH, 8.3% absolute improvement):** I could not independently confirm these exact figures from the search results alone. The search results describe "0.22-1.35x relative improvements" but do not surface the specific 45.8% or 8.3% numbers. These figures would need to be verified by reading the paper directly. The claim is **unverified** -- not contradicted, but not confirmed either.

---

## 4. Adaptive LLM-Symbolic Reasoning (EACL 2026, arXiv 2510.06774)

**CONFIRMED.** The paper "Adaptive LLM-Symbolic Reasoning via Dynamic Logical Solver Composition" (arXiv 2510.06774) exists and is published in the Proceedings of the 19th Conference of the European Chapter of the Association for Computational Linguistics (EACL 2026), Volume 1: Long Papers, pages 1187-1208, Rabat, Morocco. It is available in the ACL Anthology at `aclanthology.org/2026.eacl-long.54/`.

---

## 5. ProcessBench (ACL 2025)

**CONFIRMED.** ProcessBench is the paper "ProcessBench: Identifying Process Errors in Mathematical Reasoning" published at ACL 2025. It is listed in the ACL Anthology at `aclanthology.org/2025.acl-long.50/` and has an official GitHub repository at `github.com/QwenLM/ProcessBench`. Authors include Chujie Zheng, Zhenru Zhang, and others from the Qwen team.

---

Sources:
- [EMNLP 2026 Official Site](https://2026.emnlp.org/)
- [EMNLP 2026 Call for Papers](https://2026.emnlp.org/calls/main_conference_papers/)
- [ARR Dates and Venues](http://aclrollingreview.org/dates)
- [Beyond Correctness - ICSE 2026 Research Track](https://conf.researchr.org/details/icse-2026/icse-2026-research-track/292/Beyond-Correctness-Exposing-LLM-generated-Logical-Flaws-in-Reasoning-via-Multi-step-)
- [Beyond Correctness - arXiv 2512.23511](https://arxiv.org/abs/2512.23511)
- [Autoformalize - arXiv 2410.20936](https://arxiv.org/abs/2410.20936)
- [Autoformalize - NeurIPS 2024 Poster](https://neurips.cc/virtual/2024/poster/96359)
- [Autoformalize - NeurIPS Proceedings](https://proceedings.neurips.cc//paper_files/paper/2024/hash/6034a661584af6c28fd97a6f23e56c0a-Abstract-Conference.html)
- [Adaptive LLM-Symbolic Reasoning - arXiv 2510.06774](https://arxiv.org/abs/2510.06774)
- [Adaptive LLM-Symbolic Reasoning - ACL Anthology (EACL 2026)](https://aclanthology.org/2026.eacl-long.54/)
- [ProcessBench - ACL Anthology](https://aclanthology.org/2025.acl-long.50/)
- [ProcessBench - GitHub](https://github.com/QwenLM/ProcessBench)

agentId: a1a6fff17bb8fc6a4 (use SendMessage with to: 'a1a6fff17bb8fc6a4' to continue this agent)
&lt;usage>total_tokens: 20386
tool_uses: 10
duration_ms: 90880&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "690ed330-4f5c-46ef-a830-81906525b7b1",
  "isSidechain": false,
  "promptId": "9f058579-330c-423c-b0cd-eef715c67283",
  "type": "user",
  "uuid": "7fa42bbd-1bdf-4a0d-9edb-bff058ee54ff",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to verify several things for an ML research review. Use WebSearch.\n\n1. **EMNLP 2026 ARR submission deadline**: Search for \"EMNLP 2026 submission deadline\" and \"ARR May 2026 deadline\". The proposal claims the ARR submission deadline is May 25, 2026. Is this correct?\n\n2. **\"Beyond Correctness: Exposing LLM-generated Logical Flaws via Multi-step Automated Theorem Proving\" (MATP, claimed ICSE 2026)**: Search for this paper. Does it exist? Is it at ICSE 2026?\n\n3. **\"Autoformalize Mathematical Statements by Symbolic Equivalence and Semantic Consistency\" (NeurIPS 2024, arXiv 2410.20936)**: Search for this paper and verify:\n   - Title is \"Autoformalize\" not \"Autoformalizing\"\n   - Results: 45.8% on MATH with combined method, 8.3% absolute improvement\n   - Uses Z3, CVC5, and Isabelle/HOL\n\n4. **Adaptive LLM-Symbolic Reasoning (EACL 2026, arXiv 2510.06774)**: Verify this paper exists and is at EACL 2026.\n\n5. **ProcessBench (ACL 2025)**: Verify this exists.\n\nReport specific findings for each.",
    "agentId": "a1a6fff17bb8fc6a4",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here are my findings for each item:\n\n---\n\n## 1. EMNLP 2026 ARR Submission Deadline\n\n**CONFIRMED.** The ARR submission deadline for EMNLP 2026 long and short papers is **May 25, 2026**. The proposal's claim is correct. EMNLP 2026 will be held in Budapest, Hungary, October 24-29, 2026. Other key dates: commitment deadline August 2, notification August 20, camera-ready September 20.\n\n---\n\n## 2. \"Beyond Correctness\" / MATP (ICSE 2026)\n\n**The paper exists and is at ICSE 2026, but there is a title discrepancy.** The full title on arXiv (2512.23511) and the ICSE 2026 Research Track listing is:\n\n> \"Beyond Correctness: Exposing LLM-generated Logical Flaws **in Reasoning** via Multi-step Automated Theorem Proving\"\n\nThe proposal omits \"in Reasoning\" from the title. Additionally, the abbreviation stands for \"Multi-step **Automatic** Theorem Proving\" (not \"Automated\"), though this varies between sources. The paper is confirmed as accepted to the ICSE 2026 Research Track.\n\n---\n\n## 3. \"Autoformalize Mathematical Statements...\" (NeurIPS 2024, arXiv 2410.20936)\n\n**The paper exists and is confirmed at NeurIPS 2024, but there are issues with the claimed details:**\n\n- **Title discrepancy:** The official NeurIPS proceedings and ResearchGate use \"**Autoformalize**\" (no -ing). However, the arXiv HTML rendering and PDF use \"**Autoformalizing**\" (with -ing). So both forms appear in different authoritative sources. The NeurIPS poster page uses \"Autoformalize\" without the -ing.\n\n- **Tools used:** The paper uses **Z3, CVC5, and Isabelle/HOL** (specifically, 12 Isabelle/HOL tactics plus Z3 and CVC5 as SMT solvers). This claim checks out.\n\n- **Results (45.8% on MATH, 8.3% absolute improvement):** I could not independently confirm these exact figures from the search results alone. The search results describe \"0.22-1.35x relative improvements\" but do not surface the specific 45.8% or 8.3% numbers. These figures would need to be verified by reading the paper directly. The claim is **unverified** -- not contradicted, but not confirmed either.\n\n---\n\n## 4. Adaptive LLM-Symbolic Reasoning (EACL 2026, arXiv 2510.06774)\n\n**CONFIRMED.** The paper \"Adaptive LLM-Symbolic Reasoning via Dynamic Logical Solver Composition\" (arXiv 2510.06774) exists and is published in the Proceedings of the 19th Conference of the European Chapter of the Association for Computational Linguistics (EACL 2026), Volume 1: Long Papers, pages 1187-1208, Rabat, Morocco. It is available in the ACL Anthology at `aclanthology.org/2026.eacl-long.54/`.\n\n---\n\n## 5. ProcessBench (ACL 2025)\n\n**CONFIRMED.** ProcessBench is the paper \"ProcessBench: Identifying Process Errors in Mathematical Reasoning\" published at ACL 2025. It is listed in the ACL Anthology at `aclanthology.org/2025.acl-long.50/` and has an official GitHub repository at `github.com/QwenLM/ProcessBench`. Authors include Chujie Zheng, Zhenru Zhang, and others from the Qwen team.\n\n---\n\nSources:\n- [EMNLP 2026 Official Site](https://2026.emnlp.org/)\n- [EMNLP 2026 Call for Papers](https://2026.emnlp.org/calls/main_conference_papers/)\n- [ARR Dates and Venues](http://aclrollingreview.org/dates)\n- [Beyond Correctness - ICSE 2026 Research Track](https://conf.researchr.org/details/icse-2026/icse-2026-research-track/292/Beyond-Correctness-Exposing-LLM-generated-Logical-Flaws-in-Reasoning-via-Multi-step-)\n- [Beyond Correctness - arXiv 2512.23511](https://arxiv.org/abs/2512.23511)\n- [Autoformalize - arXiv 2410.20936](https://arxiv.org/abs/2410.20936)\n- [Autoformalize - NeurIPS 2024 Poster](https://neurips.cc/virtual/2024/poster/96359)\n- [Autoformalize - NeurIPS Proceedings](https://proceedings.neurips.cc//paper_files/paper/2024/hash/6034a661584af6c28fd97a6f23e56c0a-Abstract-Conference.html)\n- [Adaptive LLM-Symbolic Reasoning - arXiv 2510.06774](https://arxiv.org/abs/2510.06774)\n- [Adaptive LLM-Symbolic Reasoning - ACL Anthology (EACL 2026)](https://aclanthology.org/2026.eacl-long.54/)\n- [ProcessBench - ACL Anthology](https://aclanthology.org/2025.acl-long.50/)\n- [ProcessBench - GitHub](https://github.com/QwenLM/ProcessBench)"
      }
    ],
    "totalDurationMs": 90880,
    "totalTokens": 20386,
    "totalToolUseCount": 10,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 823,
      "cache_read_input_tokens": 18180,
      "output_tokens": 1382,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 823
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1382,
          "cache_read_input_tokens": 18180,
          "cache_creation_input_tokens": 823,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 823,
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
      "otherToolCount": 10
    }
  },
  "sourceToolAssistantUUID": "690ed330-4f5c-46ef-a830-81906525b7b1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ae8c16f5-ce1c-4bce-923e-3afb8499b025",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 28_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-11 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "7fa42bbd-1bdf-4a0d-9edb-bff058ee54ff",
  "sessionId": "ae8c16f5-ce1c-4bce-923e-3afb8499b025"
}
```

---

### Runtime record

_source line 29_

```json
{
  "type": "ai-title",
  "aiTitle": "Two-tier confidence-gated formalization for online derivation verification",
  "sessionId": "ae8c16f5-ce1c-4bce-923e-3afb8499b025"
}
```

---

### Assistant

_source line 30 · 2026-05-12T00:55:15.317Z_

<details><summary>Logged reasoning block</summary>

```text
Excellent. Now I have comprehensive verification data. Let me synthesize my findings and form a judgment.

## Summary of Key Findings

### References Verification
All cited papers exist and are verified. Most claims are accurate with some nuances:
- interwhen: Correctly characterized now (state-level vs assertion-level distinction)
- VeriCoT: Correctly listed as ICLR 2026 poster
- "Do LLMs Game Formalization?": Exists, but the systematic error finding is more nuanced than presented (pipeline-specific, model-specific, not universal)
- Roundtrip verification paper: Exists, but cost claims cherry-pick Claude-only results


- HERMES: Correctly noted as using DeepSeek-V3.1
- Safe: Correctly cited as ACL 2025
- EACL 2026 Adaptive paper: Correctly cited

### CRITICAL UNCITED COMPETITOR
There's a significant gap here—Kiyani et al.'s work on weak versus strong verification (arXiv 2602.17633) directly addresses the two-tier verification tradeoff with formal theorems about optimal gating policies and Pareto frontiers, yet it's completely absent from the citations.

### Other Uncited Competing Work
Several other recent papers tackle similar verification strategies during generation: Cao et al. on online formal verification, MATH-VF with step-wise symbolic verification, SpecGuard's online step-level approach, and Bayless et al.'s neurosymbolic roundtrip verification—all missing from the references.

### Baseline Accuracy

There's a discrepancy in the reported baseline. The proposal cites Qwen3-32B at ~70% on AIME 2024, but the actual thinking mode performance appears closer to 80-81%, which could be understating how strong the baseline already is.

### Novelty Assessment

The genuinely novel contribution is the specific two-tier architecture combining cross-sample consistency gating for candidate selection with roundtrip validation to catch systematic errors and weak constraint fallback when confidence drops. No existing work combines these three elements together. That said, the broader informativeness-precision tradeoff framework that anchors this approach has already been formalized more rigorously by Kiyani et al., so the conceptual foundation isn't entirely new.

The online assertion-level cumulative tracking for derivation tasks is also genuinely novel—VeriCoT does cumulative tracking but only post-hoc, while interwhen does online tracking but at the state level rather than assertion level. Combining both online and assertion-level tracking specifically for derivation tasks hasn't been done before.

The MUS-guided targeted regeneration is a reasonable alternative to VERGE's MCS-based approach, but it's not a dramatic departure.

### Feasibility Assessment

The compute budget of 150-180 H100-hours fits within the 200 H100-hour limit, with a fallback minimum publishable set requiring only ~60 H100-hours. The 16-day timeline for the full pipeline is tight, but the fallback plan of completing the minimum publishable set in ~5 days of compute is realistic. Qwen3-32B and Qwen3-14B are available, and Z3 is off-the-shelf.

The 6-component system—Reasoner, Two-Tier Formalizer, Roundtrip Validation, Cumulative Z3 Monitor, MUS extraction, and Targeted Regeneration—is complex, but the modular design makes implementing it in 16 days ambitious yet feasible.

### Quality Assessment for EMNLP 2026

After seven rounds of refinement, the core idea is solid and fills a genuine gap: interwhen handles structured-state tasks but not derivation tasks, VeriCoT handles derivation tasks but only post-hoc, and the two-tier approach directly addresses the formalization bottleneck that affects all existing systems.

The remaining issues are that Kiyani et al. needs to be cited for their more rigorous formalization of the two-tier verification tradeoff, and the "Do LLMs Game Formalization?" findings need some refinement.

Actually, I'm reconsidering the novelty score. The proposal isn't just claiming a general tradeoff framework—it's proposing specific mechanisms like Tier 1 cross-sample verification with roundtrip checking and Tier 2 weak constraints that instantiate this tradeoff specifically for autoformalization in reasoning verification. While Kiyani et al. provides an abstract weak versus strong verifier framework, this work offers concrete, domain-aware instantiations of that framework.

The real issue is that Kiyani et al. isn't cited at all, which would be flagged by reviewers who know the work. The proposal should acknowledge it and position itself as a specific instantiation with roundtrip validation as the key differentiator. Combined with the cherry-picked verification cost numbers, I'm settling on a novelty score of 3.5.

For feasibility, the compute budget and fallback timeline are reasonable, though fitting implementation, debugging, and experiments for a 6-component system into 16 days is ambitious. The minimum viable set of 24 runs within ~60 H100-hours is doable though.

The proposal is well-structured with clear contribution hierarchy and detailed experimental design, so clarity scores at 4.

On impact, there's a genuine gap in online verification for derivation tasks, but whether the two-tier mechanism actually catches meaningful errors in practice is uncertain. The error examples feel somewhat constructed rather than representative of real-world failure modes.

Averaging these scores gives 3.625, which falls short of the 4.0 bar. The verdict is to revise. The critical fixes are citing Kiyani et al. and reframing the informativeness-precision tradeoff as building on their work, addressing the cherry-picked costs, tempering the "Do LLMs Game Formalization?" claim to be pipeline-specific rather than universal, and completing the final citation.

Actually, I should step back — this is round 7 of 10, and the proposal has already been through six iterations with steady improvement. The Kiyani et al. omission is genuinely important prior art that directly supports the core contribution, but it's a citation and positioning issue, not a fundamental rethink. The cherry-picking and nuance problems are more about paper writing than the underlying idea. Let me rescore with this in mind, particularly reconsidering novelty given that the specific combination of cross-sample verification, roundtrip checking, and weak constraint fallback for online derivation tasks is genuinely novel even if the general framework builds on existing work.

Novelty lands at 3.5 but could reach 4 with proper positioning of Kiyani et al. Feasibility is actually quite solid — the minimum viable set is clearly defined at 24 runs requiring roughly 60 H100-hours over 5 days, all tools are available, and there's a sensible timeline fallback. The 16-day schedule is tight but realistic. Clarity is strong with a well-organized contribution hierarchy. Impact sits at 3.5 since the approach addresses a real gap, though the practical advantage over post-hoc VeriCoT remains unvalidated. Averaging these scores gives 3.75, still below the 4.0 threshold, so another revision is warranted.

Looking at this more carefully, the core contributions — the two-tier formalization with roundtrip validation, online assertion-level tracking for derivation tasks, and MUS-guided regeneration — form a solid systems paper suitable for EMNLP. The motivation is clear, the methodology is principled, and the experimental plan is sound. The main uncertainty is whether empirical results will demonstrate meaningful gains over existing baselines. I think the right path forward is a targeted revision addressing specific, fixable issues: properly citing Kiyani et al., resolving the cherry-picking concerns, and acknowledging the additional related work like SpecGuard and MATH-VF.

Scoring this out: novelty lands at 3.5 given the strong specific combination despite Kiyani et al. anticipating parts of the general framework, feasibility is 4 with the fallback plan in place, clarity is 4 for the well-structured presentation, and impact stays at 3.5 since while the paper tackles a genuine gap in online verification for derivation tasks, the incremental benefit over post-hoc approaches remains uncertain. That averages to 3.75, below the 4.0 threshold, so my verdict is revise.

But reconsidering the impact score—this addresses a real, important problem with cascading errors in multi-step reasoning, and if it works it would genuinely matter to the community. The evaluation is comprehensive, the approach is principled with formal grounding, and it fills a gap no existing system covers. So I'm keeping impact at 3.5.

Now I'm thinking more carefully about whether Kiyani et al. is actually a blocker. They provide the general abstract framework for weak-strong verification with optimal thresholds, but this proposal offers a specific, domain-aware instantiation: Tier 2 templated constraints as the weak verifier, Tier 1 full SMT formalization plus roundtrip validation as the strong verifier, and confidence gating tied specifically to autoformalization quality through cross-sample consistency. The roundtrip validation catches a particular failure mode that systematic mistranslation creates. This is really just a general optimization theory paper versus a specific application paper—both can be publishable. I just need to frame it as instantiating and extending Kiyani et al.'s framework for reasoning verification specifically, which actually bumps novelty up to 4 with the roundtrip validation and domain-specific instantiation.

There's still that genuine concern about the roundtrip validation's limitation though—if the same model does both formalization and informalization, it might systematically produce the same interpretation, which the proposal acknowledges and plans to quantify empirically.

The mitigation strategy makes sense: if the residual error rate exceeds 15%, switch to a different model for informalization to break the pattern. That's a practical safeguard.

Looking back at the revision history, all previous rounds' feedback has been addressed, so the main outstanding issue is really just the missing Kiyani et al. citation and a few minor points. The verdict should be revise—it's genuinely close to passing, but that citation gap needs to be fixed.

Now I'm checking whether the roundtrip paper results are being cherry-picked. The agent report shows the 7.21 vs 12.27 LLM calls comparison only holds for Traffic domain with Claude, while GPT shows the opposite pattern. The equivalence improvement claim is also selective—citing the best-case range without acknowledging the variability across domains. The proposal is presenting these as general findings when they're actually domain and model-specific.

That said, these numbers are being used as motivation for why roundtrip verification matters, not as claimed results from the proposal itself. So it's more of a citation accuracy issue than a fundamental methodological flaw.

I'm also reconsidering the Kiyani paper omission. We're at round 7 of 10, and the proposal has shown consistent responsiveness to feedback with a sound core idea. The missing citation is credibility-damaging but not approach-breaking. Given the average score sits at 3.75 and the feedback is concrete and fixable, I think **revise** is the right call—one more round should get this across the threshold.

Now I'll draft the review.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7fa42bbd-1bdf-4a0d-9edb-bff058ee54ff",
  "isSidechain": false,
  "requestId": "req_011Cawm7MpAFWvEGohLSJmZX",
  "type": "assistant",
  "uuid": "e0f69260-27ed-47e4-a210-dd9b4a3f58bf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ae8c16f5-ce1c-4bce-923e-3afb8499b025",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VqZKt7GhajFn3YPm6WcFp4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4780,
      "cache_read_input_tokens": 48554,
      "output_tokens": 3945,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4780,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3945,
          "cache_read_input_tokens": 48554,
          "cache_creation_input_tokens": 4780,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4780
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

_source line 31 · 2026-05-12T00:55:16.398Z_

Now I have comprehensive data from all verification agents. Let me synthesize my findings and assess the proposal.

Key findings so far:
- All cited papers verified as real
- A critical uncited competitor found: Kiyani et al. (arXiv 2602.17633)
- Some citation cherry-picking identified
- EMNLP 2026 deadline confirmed (May 25, 2026)

Let me do one final search for the most threatening related work.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e0f69260-27ed-47e4-a210-dd9b4a3f58bf",
  "isSidechain": false,
  "requestId": "req_011Cawm7MpAFWvEGohLSJmZX",
  "type": "assistant",
  "uuid": "2db84a0a-d571-4610-a54b-918b36b58d15",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ae8c16f5-ce1c-4bce-923e-3afb8499b025",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VqZKt7GhajFn3YPm6WcFp4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4780,
      "cache_read_input_tokens": 48554,
      "output_tokens": 3945,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4780,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3945,
          "cache_read_input_tokens": 48554,
          "cache_creation_input_tokens": 4780,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4780
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

_source line 32 · 2026-05-12T00:55:16.712Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01JmG16cYiDGBHQn1ePxB2X4`</summary>

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
  "parentUuid": "2db84a0a-d571-4610-a54b-918b36b58d15",
  "isSidechain": false,
  "requestId": "req_011Cawm7MpAFWvEGohLSJmZX",
  "type": "assistant",
  "uuid": "97ed2a5a-3cb3-498b-a63c-c70c3ff83e15",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ae8c16f5-ce1c-4bce-923e-3afb8499b025",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VqZKt7GhajFn3YPm6WcFp4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4780,
      "cache_read_input_tokens": 48554,
      "output_tokens": 3945,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4780,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3945,
          "cache_read_input_tokens": 48554,
          "cache_creation_input_tokens": 4780,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4780
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

_source line 33 · 2026-05-12T00:55:16.719Z_

<details><summary>↩ Tool result · `toolu_01JmG16cYiDGBHQn1ePxB2X4`</summary>

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
  "parentUuid": "97ed2a5a-3cb3-498b-a63c-c70c3ff83e15",
  "isSidechain": false,
  "promptId": "9f058579-330c-423c-b0cd-eef715c67283",
  "type": "user",
  "uuid": "a2adf77a-5b98-4fab-95ae-38f7c5c588ac",
  "toolUseResult": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 17
  },
  "sourceToolAssistantUUID": "97ed2a5a-3cb3-498b-a63c-c70c3ff83e15",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ae8c16f5-ce1c-4bce-923e-3afb8499b025",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 34 · 2026-05-12T00:55:16.783Z_

```json
{
  "parentUuid": "a2adf77a-5b98-4fab-95ae-38f7c5c588ac",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "b93aa6ea-5643-4973-8ca9-a2a1a6b3b20d",
  "timestamp": "2026-05-12T00:55:16.783Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ae8c16f5-ce1c-4bce-923e-3afb8499b025",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 35_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-11 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "b93aa6ea-5643-4973-8ca9-a2a1a6b3b20d",
  "sessionId": "ae8c16f5-ce1c-4bce-923e-3afb8499b025"
}
```

---

### Runtime record

_source line 36_

```json
{
  "type": "ai-title",
  "aiTitle": "Two-tier confidence-gated formalization for online derivation verification",
  "sessionId": "ae8c16f5-ce1c-4bce-923e-3afb8499b025"
}
```

---

### Tool call

_source line 37 · 2026-05-12T00:55:20.902Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01YRsj8WnRdQ5KUuXqDM6NHp`</summary>

```json
{
  "query": "SpecGuard verification-aware speculative decoding multi-step reasoning arXiv 2604.15244"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b93aa6ea-5643-4973-8ca9-a2a1a6b3b20d",
  "isSidechain": false,
  "requestId": "req_011CawmEbugM9D7KX89eQr5m",
  "type": "assistant",
  "uuid": "a22f7143-2906-481f-9bad-f56a856a2982",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ae8c16f5-ce1c-4bce-923e-3afb8499b025",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U3TfzFogzbgsqwmBCztd7j",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4569,
      "cache_read_input_tokens": 53334,
      "output_tokens": 200,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4569,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 200,
          "cache_read_input_tokens": 53334,
          "cache_creation_input_tokens": 4569,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4569
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

_source line 38 · 2026-05-12T00:55:22.305Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0146gFmSpnxfT6qnnEbKwYZP`</summary>

```json
{
  "query": "MATH-VF step-wise formal verification Z3 SymPy arXiv 2505.20869 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a22f7143-2906-481f-9bad-f56a856a2982",
  "isSidechain": false,
  "requestId": "req_011CawmEbugM9D7KX89eQr5m",
  "type": "assistant",
  "uuid": "0957928c-193f-4ac3-85d1-cc5ea18b1076",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ae8c16f5-ce1c-4bce-923e-3afb8499b025",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U3TfzFogzbgsqwmBCztd7j",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4569,
      "cache_read_input_tokens": 53334,
      "output_tokens": 200,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4569,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 200,
          "cache_read_input_tokens": 53334,
          "cache_creation_input_tokens": 4569,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4569
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

_source line 39 · 2026-05-12T00:55:22.827Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01ETcZ5LsDzfYmrMDm7bavSk`</summary>

```json
{
  "query": "\"neurosymbolic approach\" \"natural language formalization\" roundtrip verification arXiv 2511.09008"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0957928c-193f-4ac3-85d1-cc5ea18b1076",
  "isSidechain": false,
  "requestId": "req_011CawmEbugM9D7KX89eQr5m",
  "type": "assistant",
  "uuid": "dc3fea12-6c3a-44ef-b22b-acda30938689",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ae8c16f5-ce1c-4bce-923e-3afb8499b025",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U3TfzFogzbgsqwmBCztd7j",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4569,
      "cache_read_input_tokens": 53334,
      "output_tokens": 200,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4569,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 200,
          "cache_read_input_tokens": 53334,
          "cache_creation_input_tokens": 4569,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4569
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

_source line 40 · 2026-05-12T00:55:27.988Z_

<details><summary>↩ Tool result · `toolu_01YRsj8WnRdQ5KUuXqDM6NHp`</summary>

```text
Web search results for query: "SpecGuard verification-aware speculative decoding multi-step reasoning arXiv 2604.15244"

Links: [{"title":"[2604.15244] From Tokens to Steps: Verification-Aware Speculative Decoding for Efficient Multi-Step Reasoning","url":"https://arxiv.org/abs/2604.15244"},{"title":"From Tokens to Steps: Verification-Aware Speculative Decoding for Efficient Multi-Step Reasoning","url":"https://arxiv.org/html/2604.15244"},{"title":"ConfSpec: Efficient Step-Level Speculative Reasoning via Confidence-Gated Verification","url":"https://arxiv.org/html/2602.18447"},{"title":"GitHub - hemingkx/SpeculativeDecodingPapers: 📰 Must-read papers and blogs on Speculative Decoding ⚡️","url":"https://github.com/hemingkx/SpeculativeDecodingPapers"},{"title":"Traversal Verification for Speculative Tree Decoding","url":"https://arxiv.org/html/2505.12398"},{"title":"SpecPV: Improving Self-Speculative Decoding for Long-Context Generation via Partial Verification","url":"https://arxiv.org/html/2512.02337v1"},{"title":"Scaling Speculative Decoding with Lookahead Reasoning","url":"https://arxiv.org/html/2506.19830v1"},{"title":"Speculative decoding: how it works & when to use it","url":"https://redis.io/blog/speculative-decoding-llm/"},{"title":"A Hitchhiker’s Guide to Speculative Decoding – PyTorch","url":"https://pytorch.org/blog/hitchhikers-guide-speculative-decoding/"},{"title":"Block Verification Accelerates Speculative Decoding | OpenReview","url":"https://openreview.net/forum?id=frsg32u0rO"}]

I found the paper you're looking for! Here are the key details about SpecGuard from arXiv 2604.15244:

## Overview

SpecGuard is a verification-aware speculative decoding framework that performs step-level verification using only model-internal signals.

## Problem It Addresses

The token-centric nature of standard speculative decoding allows erroneous steps to propagate, and prior approaches mitigate this using external reward models, but incur additional latency, computational overhead, and limit generalizability.

## Key Features

At each step, SpecGuard samples multiple draft candidates and selects the most consistent step, which is then validated using an ensemble of two lightweight model-internal signals: (i) an attention-based grounding score that measures attribution to the input and previous steps. Additionally, SpecGuard introduces log-probability-based verification (LPBV) as a complementary mechanism to assess the reliability of the full reasoning step, relying on the model's own predictive confidence as reflected in the conditional log probability of the tokens generated.

## Results

Experiments across a range of reasoning benchmarks show that SpecGuard improves accuracy by 3.6% while reducing latency by ~11%, outperforming both standard speculative decoding and reward-guided speculative decoding.

The paper's title is "From Tokens to Steps: Verification-Aware Speculative Decoding for Efficient Multi-Step Reasoning."


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a22f7143-2906-481f-9bad-f56a856a2982",
  "isSidechain": false,
  "promptId": "9f058579-330c-423c-b0cd-eef715c67283",
  "type": "user",
  "uuid": "477b8831-2be9-426d-a31b-3f6be3f52704",
  "toolUseResult": {
    "query": "SpecGuard verification-aware speculative decoding multi-step reasoning arXiv 2604.15244",
    "results": [
      {
        "tool_use_id": "srvtoolu_01VRZBSbck82NCJhELb3ehz3",
        "content": [
          {
            "title": "[2604.15244] From Tokens to Steps: Verification-Aware Speculative Decoding for Efficient Multi-Step Reasoning",
            "url": "https://arxiv.org/abs/2604.15244"
          },
          {
            "title": "From Tokens to Steps: Verification-Aware Speculative Decoding for Efficient Multi-Step Reasoning",
            "url": "https://arxiv.org/html/2604.15244"
          },
          {
            "title": "ConfSpec: Efficient Step-Level Speculative Reasoning via Confidence-Gated Verification",
            "url": "https://arxiv.org/html/2602.18447"
          },
          {
            "title": "GitHub - hemingkx/SpeculativeDecodingPapers: 📰 Must-read papers and blogs on Speculative Decoding ⚡️",
            "url": "https://github.com/hemingkx/SpeculativeDecodingPapers"
          },
          {
            "title": "Traversal Verification for Speculative Tree Decoding",
            "url": "https://arxiv.org/html/2505.12398"
          },
          {
            "title": "SpecPV: Improving Self-Speculative Decoding for Long-Context Generation via Partial Verification",
            "url": "https://arxiv.org/html/2512.02337v1"
          },
          {
            "title": "Scaling Speculative Decoding with Lookahead Reasoning",
            "url": "https://arxiv.org/html/2506.19830v1"
          },
          {
            "title": "Speculative decoding: how it works & when to use it",
            "url": "https://redis.io/blog/speculative-decoding-llm/"
          },
          {
            "title": "A Hitchhiker’s Guide to Speculative Decoding – PyTorch",
            "url": "https://pytorch.org/blog/hitchhikers-guide-speculative-decoding/"
          },
          {
            "title": "Block Verification Accelerates Speculative Decoding | OpenReview",
            "url": "https://openreview.net/forum?id=frsg32u0rO"
          }
        ]
      },
      "I found the paper you're looking for! Here are the key details about SpecGuard from arXiv 2604.15244:\n\n## Overview\n\nSpecGuard is a verification-aware speculative decoding framework that performs step-level verification using only model-internal signals.\n\n## Problem It Addresses\n\nThe token-centric nature of standard speculative decoding allows erroneous steps to propagate, and prior approaches mitigate this using external reward models, but incur additional latency, computational overhead, and limit generalizability.\n\n## Key Features\n\nAt each step, SpecGuard samples multiple draft candidates and selects the most consistent step, which is then validated using an ensemble of two lightweight model-internal signals: (i) an attention-based grounding score that measures attribution to the input and previous steps. Additionally, SpecGuard introduces log-probability-based verification (LPBV) as a complementary mechanism to assess the reliability of the full reasoning step, relying on the model's own predictive confidence as reflected in the conditional log probability of the tokens generated.\n\n## Results\n\nExperiments across a range of reasoning benchmarks show that SpecGuard improves accuracy by 3.6% while reducing latency by ~11%, outperforming both standard speculative decoding and reward-guided speculative decoding.\n\nThe paper's title is \"From Tokens to Steps: Verification-Aware Speculative Decoding for Efficient Multi-Step Reasoning.\""
    ],
    "durationSeconds": 7.0829679239999965
  },
  "sourceToolAssistantUUID": "a22f7143-2906-481f-9bad-f56a856a2982",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ae8c16f5-ce1c-4bce-923e-3afb8499b025",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-12T00:55:29.511Z_

<details><summary>↩ Tool result · `toolu_0146gFmSpnxfT6qnnEbKwYZP`</summary>

```text
Web search results for query: "MATH-VF step-wise formal verification Z3 SymPy arXiv 2505.20869 2025"

Links: [{"title":"[2505.20869] Step-Wise Formal Verification for LLM-Based Mathematical Problem Solving","url":"https://arxiv.org/abs/2505.20869"},{"title":"Step-Wise Formal Verification for LLM-Based Mathematical Problem Solving","url":"https://arxiv.org/html/2505.20869"},{"title":"Step-Wise Formal Verification for LLM-Based Mathematical Problem Solving - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250520869Z/abstract"},{"title":"Step-Wise Formal Verification for LLM-Based Mathematical ...","url":"https://arxiv.org/pdf/2505.20869"},{"title":"[2505.15960] Efficient PRM Training Data Synthesis via Formal Verification","url":"https://arxiv.org/abs/2505.15960"},{"title":"Training Step-Level Reasoning Verifiers with Formal ...","url":"https://arxiv.org/pdf/2505.15960"},{"title":"[Literature Review] Step-Wise Formal Verification for LLM-Based Mathematical Problem Solving","url":"https://www.themoonlight.io/en/review/step-wise-formal-verification-for-llm-based-mathematical-problem-solving"},{"title":"Step-Wise Formal Verification for LLM-Based Mathematical Problem Solving","url":"https://www.researchgate.net/publication/392134530_Step-Wise_Formal_Verification_for_LLM-Based_Mathematical_Problem_Solving"},{"title":"On Learning Verifiers and Implications to Chain-of-Thought Reasoning","url":"https://arxiv.org/html/2505.22650.pdf"},{"title":"FoVer: Efficient PRM Training Data Synthesis via Formal Verification","url":"https://fover-prm.github.io/"}]

I found the paper! Here's information about the research:

## MATH-VF: Step-Wise Formal Verification for LLM-Based Mathematical Problem Solving

The paper proposes a framework, MATH-VF, which includes a Formalizer and a Critic, for formally verifying the correctness of the solutions generated by large language models.

### Framework Components

The Formalizer first formalizes the informal solution, and then the Critic leverages external tools such as Z3 and SymPy to verify the conclusions in each step of the reasoning.

### Tools Used

SymPy is a powerful software tool designed to perform both symbolic and numerical computations. It is capable of manipulating mathematical expressions symbolically, performing operations such as differentiation, integration, solving equations, and factoring polynomials.

Z3 is a high performance Satisfiability Modulo Theories (SMT) Solver developed by Microsoft Research. It is designed to check the satisfiability of logical expressions and generate models for satisfiable formulas. Z3 supports a wide range of theories, including linear arithmetic (both real and integer), bit vectors, arrays, datatypes, strings, and more.

### Key Features

MATH-VF is a training-free framework for step-by-step verification of mathematical reasoning. MATH-VF not only evaluates the correctness of solutions, but also provides constructive feedback for incorrect ones.

The approach was evaluated on two widely used mathematical benchmarks: MATH500 and ProcessBench.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0957928c-193f-4ac3-85d1-cc5ea18b1076",
  "isSidechain": false,
  "promptId": "9f058579-330c-423c-b0cd-eef715c67283",
  "type": "user",
  "uuid": "ae1d23db-eca2-4d11-bda9-35f04dbc4963",
  "toolUseResult": {
    "query": "MATH-VF step-wise formal verification Z3 SymPy arXiv 2505.20869 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01FWw61UXBKumLbEB7ZmgJLZ",
        "content": [
          {
            "title": "[2505.20869] Step-Wise Formal Verification for LLM-Based Mathematical Problem Solving",
            "url": "https://arxiv.org/abs/2505.20869"
          },
          {
            "title": "Step-Wise Formal Verification for LLM-Based Mathematical Problem Solving",
            "url": "https://arxiv.org/html/2505.20869"
          },
          {
            "title": "Step-Wise Formal Verification for LLM-Based Mathematical Problem Solving - ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/2025arXiv250520869Z/abstract"
          },
          {
            "title": "Step-Wise Formal Verification for LLM-Based Mathematical ...",
            "url": "https://arxiv.org/pdf/2505.20869"
          },
          {
            "title": "[2505.15960] Efficient PRM Training Data Synthesis via Formal Verification",
            "url": "https://arxiv.org/abs/2505.15960"
          },
          {
            "title": "Training Step-Level Reasoning Verifiers with Formal ...",
            "url": "https://arxiv.org/pdf/2505.15960"
          },
          {
            "title": "[Literature Review] Step-Wise Formal Verification for LLM-Based Mathematical Problem Solving",
            "url": "https://www.themoonlight.io/en/review/step-wise-formal-verification-for-llm-based-mathematical-problem-solving"
          },
          {
            "title": "Step-Wise Formal Verification for LLM-Based Mathematical Problem Solving",
            "url": "https://www.researchgate.net/publication/392134530_Step-Wise_Formal_Verification_for_LLM-Based_Mathematical_Problem_Solving"
          },
          {
            "title": "On Learning Verifiers and Implications to Chain-of-Thought Reasoning",
            "url": "https://arxiv.org/html/2505.22650.pdf"
          },
          {
            "title": "FoVer: Efficient PRM Training Data Synthesis via Formal Verification",
            "url": "https://fover-prm.github.io/"
          }
        ]
      },
      "I found the paper! Here's information about the research:\n\n## MATH-VF: Step-Wise Formal Verification for LLM-Based Mathematical Problem Solving\n\nThe paper proposes a framework, MATH-VF, which includes a Formalizer and a Critic, for formally verifying the correctness of the solutions generated by large language models.\n\n### Framework Components\n\nThe Formalizer first formalizes the informal solution, and then the Critic leverages external tools such as Z3 and SymPy to verify the conclusions in each step of the reasoning.\n\n### Tools Used\n\nSymPy is a powerful software tool designed to perform both symbolic and numerical computations. It is capable of manipulating mathematical expressions symbolically, performing operations such as differentiation, integration, solving equations, and factoring polynomials.\n\nZ3 is a high performance Satisfiability Modulo Theories (SMT) Solver developed by Microsoft Research. It is designed to check the satisfiability of logical expressions and generate models for satisfiable formulas. Z3 supports a wide range of theories, including linear arithmetic (both real and integer), bit vectors, arrays, datatypes, strings, and more.\n\n### Key Features\n\nMATH-VF is a training-free framework for step-by-step verification of mathematical reasoning. MATH-VF not only evaluates the correctness of solutions, but also provides constructive feedback for incorrect ones.\n\nThe approach was evaluated on two widely used mathematical benchmarks: MATH500 and ProcessBench."
    ],
    "durationSeconds": 7.20423955300008
  },
  "sourceToolAssistantUUID": "0957928c-193f-4ac3-85d1-cc5ea18b1076",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ae8c16f5-ce1c-4bce-923e-3afb8499b025",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-12T00:55:34.069Z_

<details><summary>↩ Tool result · `toolu_01ETcZ5LsDzfYmrMDm7bavSk`</summary>

```text
Web search results for query: ""neurosymbolic approach" "natural language formalization" roundtrip verification arXiv 2511.09008"

Links: [{"title":"[2511.09008] A Neurosymbolic Approach to Natural Language Formalization and Verification","url":"https://arxiv.org/abs/2511.09008"},{"title":"A Neurosymbolic Approach to Natural Language Formalization and Verification","url":"https://arxiv.org/html/2511.09008v1"},{"title":"A Neurosymbolic Approach to Natural Language Formalization and Verification - Prompt University","url":"https://news.prompt.university/item/134568/a-neurosymbolic-approach-to-natural-language-formalization-and-verification"},{"title":"(PDF) A Neurosymbolic Approach to Natural Language Formalization and Verification","url":"https://www.researchgate.net/publication/397556828_A_Neurosymbolic_Approach_to_Natural_Language_Formalization_and_Verification"},{"title":"A Neurosymbolic Approach to Natural Language Formalization and Verification | OpenReview","url":"https://openreview.net/forum?id=aMIkbx81Em"},{"title":"Google Scholar","url":"https://scholar.google.com/scholar?q=A+Neurosymbolic+Approach+to+Natural+Language+Formalization+and+Verification."},{"title":"A Neurosymbolic Approach to Natural Language ...","url":"https://www.alphaxiv.org/overview/2511.09008v1"},{"title":"[Literature Review] A Neurosymbolic Approach to Natural Language Formalization and Verification","url":"https://www.themoonlight.io/en/review/a-neurosymbolic-approach-to-natural-language-formalization-and-verification"},{"title":"A NEUROSYMBOLIC APPROACH TO NATURAL ...","url":"https://openreview.net/pdf?id=aMIkbx81Em"},{"title":"Neuro-Symbolic Autoformalization Framework","url":"https://www.emergentmind.com/topics/neuro-symbolic-autoformalization-framework"}]

Based on the search results, I found comprehensive information about arXiv paper 2511.09008:

## A Neurosymbolic Approach to Natural Language Formalization and Verification

The paper was submitted on November 12, 2025, with authors including Sam Bayless, Stefano Buliani, Darion Cassel, Byron Cook, and 24 other collaborators.

### Overview

The research addresses how Large Language Models perform well at natural language interpretation and reasoning, but their inherent stochasticity limits their adoption in regulated industries like finance and healthcare that operate under strict policies. The authors present a two-stage neurosymbolic framework that (1) uses LLMs with optional human guidance to formalize natural language policies, allowing fine-grained control of the formalization process, and (2) uses inference-time autoformalization to validate logical correctness of natural language statements against those policies.

### Key Innovation: Roundtrip Verification

When correctness is paramount, they perform multiple redundant formalization steps at inference time, cross checking the formalizations for semantic equivalence. This is the roundtrip verification approach—formalizing natural language multiple times and comparing the resulting formalizations to ensure consistency.

### Results

The paper presents Automated Reasoning checks (ARc), a neurosymbolic approach that exceeds 99% soundness on datasets that it was not trained on—an assurance threshold unattainable by existing pure neural or neurosymbolic approaches. More specifically, at the most conservative threshold (3/3), it reaches 99.2% soundness with a 2.5% false positive rate while achieving 92.6% precision.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dc3fea12-6c3a-44ef-b22b-acda30938689",
  "isSidechain": false,
  "promptId": "9f058579-330c-423c-b0cd-eef715c67283",
  "type": "user",
  "uuid": "f596a4cf-ca19-4324-8c88-793fe510ee70",
  "toolUseResult": {
    "query": "\"neurosymbolic approach\" \"natural language formalization\" roundtrip verification arXiv 2511.09008",
    "results": [
      {
        "tool_use_id": "srvtoolu_01986tALKuMNzUFQZ61BzUZ5",
        "content": [
          {
            "title": "[2511.09008] A Neurosymbolic Approach to Natural Language Formalization and Verification",
            "url": "https://arxiv.org/abs/2511.09008"
          },
          {
            "title": "A Neurosymbolic Approach to Natural Language Formalization and Verification",
            "url": "https://arxiv.org/html/2511.09008v1"
          },
          {
            "title": "A Neurosymbolic Approach to Natural Language Formalization and Verification - Prompt University",
            "url": "https://news.prompt.university/item/134568/a-neurosymbolic-approach-to-natural-language-formalization-and-verification"
          },
          {
            "title": "(PDF) A Neurosymbolic Approach to Natural Language Formalization and Verification",
            "url": "https://www.researchgate.net/publication/397556828_A_Neurosymbolic_Approach_to_Natural_Language_Formalization_and_Verification"
          },
          {
            "title": "A Neurosymbolic Approach to Natural Language Formalization and Verification | OpenReview",
            "url": "https://openreview.net/forum?id=aMIkbx81Em"
          },
          {
            "title": "Google Scholar",
            "url": "https://scholar.google.com/scholar?q=A+Neurosymbolic+Approach+to+Natural+Language+Formalization+and+Verification."
          },
          {
            "title": "A Neurosymbolic Approach to Natural Language ...",
            "url": "https://www.alphaxiv.org/overview/2511.09008v1"
          },
          {
            "title": "[Literature Review] A Neurosymbolic Approach to Natural Language Formalization and Verification",
            "url": "https://www.themoonlight.io/en/review/a-neurosymbolic-approach-to-natural-language-formalization-and-verification"
          },
          {
            "title": "A NEUROSYMBOLIC APPROACH TO NATURAL ...",
            "url": "https://openreview.net/pdf?id=aMIkbx81Em"
          },
          {
            "title": "Neuro-Symbolic Autoformalization Framework",
            "url": "https://www.emergentmind.com/topics/neuro-symbolic-autoformalization-framework"
          }
        ]
      },
      "Based on the search results, I found comprehensive information about arXiv paper 2511.09008:\n\n## A Neurosymbolic Approach to Natural Language Formalization and Verification\n\nThe paper was submitted on November 12, 2025, with authors including Sam Bayless, Stefano Buliani, Darion Cassel, Byron Cook, and 24 other collaborators.\n\n### Overview\n\nThe research addresses how Large Language Models perform well at natural language interpretation and reasoning, but their inherent stochasticity limits their adoption in regulated industries like finance and healthcare that operate under strict policies. The authors present a two-stage neurosymbolic framework that (1) uses LLMs with optional human guidance to formalize natural language policies, allowing fine-grained control of the formalization process, and (2) uses inference-time autoformalization to validate logical correctness of natural language statements against those policies.\n\n### Key Innovation: Roundtrip Verification\n\nWhen correctness is paramount, they perform multiple redundant formalization steps at inference time, cross checking the formalizations for semantic equivalence. This is the roundtrip verification approach—formalizing natural language multiple times and comparing the resulting formalizations to ensure consistency.\n\n### Results\n\nThe paper presents Automated Reasoning checks (ARc), a neurosymbolic approach that exceeds 99% soundness on datasets that it was not trained on—an assurance threshold unattainable by existing pure neural or neurosymbolic approaches. More specifically, at the most conservative threshold (3/3), it reaches 99.2% soundness with a 2.5% false positive rate while achieving 92.6% precision."
    ],
    "durationSeconds": 11.237424157999921
  },
  "sourceToolAssistantUUID": "dc3fea12-6c3a-44ef-b22b-acda30938689",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ae8c16f5-ce1c-4bce-923e-3afb8499b025",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 43 · 2026-05-12T00:56:22.286Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the data I need for a comprehensive review. Let me synthesize everything.

Key findings for my review:

### CRITICAL UNCITED WORK

1. **Kiyani et al. "When to Trust the Cheap Check" (arXiv 2602.17633, Feb 2026)** — NOT CITED. This paper formalizes the exact two-tier weak/strong verification tradeoff with:
   - Formal weak/strong verification hierarchy
   - Optimal two-threshold gating policy (Theorem 4.2)
   - Pareto frontier between verification cost and quality  
   - Online algorithm with distribution-free guarantees

This directly addresses the proposal's claimed contribution around the informativeness-precision tradeoff.

2. **MATH-VF (arXiv 2505.20869)** — NOT CITED. Implements step-wise verification using Z3 and SymPy with a Formalizer and Critic architecture, highly relevant to the approach.

3. **Bayless et al. "A Neurosymbolic Approach to Natural Language Formalization and Verification" (arXiv 2511.09008)** — NOT CITED. Employs redundant formalization with semantic equivalence checking for roundtrip verification, achieving over 99% soundness.

4. **SpecGu** — appears to be another uncited work that's cut off, but likely follows the same pattern of missing citations.

5. **Cao et al. "Pushing the Boundaries of Natural Reasoning" (arXiv 2601.22642, Jan 2026)** — NOT CITED. Performs online formal verification during generation.

I'm also verifying the accuracy of various claims in the paper — checking that cited papers actually exist, confirming the correct characterization of verification approaches, and validating conference placements and deadlines.

Now I'm examining some problematic citations. The "Do LLMs Game Formalization?" paper claims systematic mistranslation during formalization, but the actual findings show the behavior varies by pipeline and model rather than being systematic. The roundtrip verification paper selectively reports results favoring Claude while omitting GPT's opposite pattern, and cherry-picks equivalence improvements from a single domain. The NeurIPS 2024 paper's improvement figure also appears to have been adjusted.

Looking at the novelty score, the specific combination of techniques here is genuinely novel, but there are several uncited precedents that already explore similar ideas—Kiyani et al. on verification tradeoffs, Bayless et al. on redundant formalization with semantic equivalence checking, and MATH-VF on multi-solver step-wise verification. I need to acknowledge these and clarify what's actually new. The feasibility looks solid with a realistic compute budget, though the thinking cuts off mid-sentence.

Continuing from there: the compute estimate of 100-200 hours fits within the 200-hour limit, there's a well-defined minimum publishable set at 24 runs taking about 5 days, all required tools are available, and the timeline has sensible fallbacks even if it's tight. The proposal is clearly structured with a good contribution hierarchy and detailed approach, plus the informativeness-precision framework adds rigor. The experimental design is comprehensive. On impact though, there's a real concern—while this addresses a genuine gap in online verification for derivation tasks, the practical value hinges on whether the errors caught actually matter. ProofWriter and FOLIO may already be near saturation with neurosymbolic methods around 98%, and the AIME baseline is uncertain between 70-80%, making it unclear how much room there is to improve. Averaging the scores gives 3.75, which points toward a revise verdict.

The main issues holding this back are citation gaps—Kiyani et al. is uncited and critical, plus several others like MATH-VF, Bayless et al., and SpecGuard are missing. There are also some minor citation inaccuracies. All of these are fixable in one revision without touching the core approach. Let me reconsider the ProofWriter saturation concern though. The agent reported SOTA at ~98% with neurosymbolic methods, but the proposal uses Qwen3-32B as the base model, which likely won't hit 98% on ProofWriter without verification. The real question is what Qwen3-32B's baseline actually is on that benchmark, since the proposal is specifically testing the verification component's ability to improve from there.

The verification system's value depends on how many errors the base model makes—if it's already at 98%, there's little room for improvement, but if it's closer to 80%, the verification system has meaningful work to do. ProofWriter also varies by problem depth, and the 98% figures might only apply to easier depths, so the proposal should specify which depth it's evaluating. This is worth flagging but not a dealbreaker since AIME and FOLIO offer more headroom for improvement. I'm settling on revise as the recommendation.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f596a4cf-ca19-4324-8c88-793fe510ee70",
  "isSidechain": false,
  "requestId": "req_011CawmFsqQuF3hGpqxvU4B5",
  "type": "assistant",
  "uuid": "40732fd1-b656-41ff-9b35-2bccaa23780b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ae8c16f5-ce1c-4bce-923e-3afb8499b025",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018ukR9xrRXUQmeSgRXt5aSY",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2916,
      "cache_read_input_tokens": 57903,
      "output_tokens": 3858,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2916,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3858,
          "cache_read_input_tokens": 57903,
          "cache_creation_input_tokens": 2916,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2916
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

_source line 44 · 2026-05-12T00:57:02.709Z_

I now have comprehensive verification data. Let me compile my final assessment.

## Synthesis of Findings

**All cited papers verified as real.** The interwhen characterization is now accurate (state-level vs assertion-level distinction — fixed from Rounds 3-5). VeriCoT correctly listed as ICLR 2026 poster. HERMES base model correctly identified as DeepSeek-V3.1. Safe cited as ACL 2025. EMNLP 2026 ARR deadline May 25, 2026 confirmed.

**Critical uncited competitors identified:**

1. **Kiyani et al. "When to Trust the Cheap Check" (arXiv 2602.17633, Feb 2026)** — Formalizes the two-tier weak/strong verification concept with optimal two-threshold gating (Theorem 4.2), Pareto frontiers, and an online SSV algorithm with distribution-free guarantees. This directly anticipates the proposal's "informativeness-precision tradeoff" framework claim.

2. **MATH-VF (arXiv 2505.20869)** — Step-wise Z3+SymPy verification with Formalizer+Critic architecture. Directly related.

3. **Bayless et al. (arXiv 2511.09008)** — Redundant formalization + semantic equivalence checking achieving >99% soundness. Directly related to the roundtrip verification approach.

4. **SpecGuard (arXiv 2604.15244, April 2026)** — Online step-level verification during generation using model-internal signals.

**Citation accuracy issues:** The roundtrip verification paper's cost numbers (7.21 vs 12.27 LLM calls) are cherry-picked from Claude-only results; for GPT the relationship reverses (14.56 vs 9.77). The "Do LLMs Game Formalization?" paper's findings are slightly overstated — it finds pipeline-specific, model-specific unfaithfulness, not universal systematic gaming.

```json
{
  "verdict": "revise",
  "scores": {
    "novelty": {"score": 3.5, "rationale": "The specific combination (cross-sample consistency + roundtrip validation + weak constraint fallback for online derivation-task verification) is novel, but Kiyani et al. (arXiv 2602.17633, Feb 2026) — uncited — already formalizes the two-tier weak/strong verification tradeoff with optimal thresholds, Pareto frontiers, and an online algorithm, directly anticipating the 'informativeness-precision tradeoff' claimed as a contribution. Bayless et al. (arXiv 2511.09008) — also uncited — achieves >99% soundness via redundant formalization with semantic equivalence checking, anticipating the roundtrip verification component."},
    "feasibility": {"score": 4, "rationale": "Compute budget is realistic (~60-180 H100-hours within 200 limit), minimum publishable set is well-defined (24 runs, ~5 days), all models (Qwen3-32B, Qwen3-14B) and tools (Z3, vLLM) are available off-the-shelf, and the timeline fallback plan is sensible. Main risk is pipeline integration complexity within 16 days."},
    "clarity": {"score": 4, "rationale": "Well-structured with clear PRIMARY/SECONDARY/TERTIARY contribution hierarchy, formal informativeness-precision framework, specific error examples per benchmark, and a well-defined minimum publishable result set. The approach section is detailed enough for reproduction."},
    "impact": {"score": 3.5, "rationale": "Fills a genuine gap (online verification for derivation tasks where interwhen's state extraction cannot apply), but practical impact is uncertain: ProofWriter SOTA is ~98% with neurosymbolic methods (limited headroom), AIME baseline for Qwen3-32B may be 80-81% (not 70%), and the incremental benefit of online over post-hoc verification for derivation tasks is theoretically motivated but empirically unvalidated."}
  },
  "issues": [
    "CRITICAL: Kiyani et al. 'When to Trust the Cheap Check: Weak and Strong Verification for Reasoning' (arXiv 2602.17633, Feb 2026) is NOT cited. This paper formalizes the exact two-tier weak/strong verification tradeoff with optimal two-threshold gating (Theorem 4.2: reject if w < t_low, query strong verifier if t_low ≤ w ≤ t_high, accept if w > t_high), Pareto frontiers between verification cost and reasoning quality, and an online Selective Strong Verification (SSV) algorithm with distribution-free guarantees. The proposal's 'informativeness-precision tradeoff' framework is directly anticipated by this work. The proposal must cite it and reposition its contribution as a specific domain-aware instantiation (Z3-based formalization tiers for reasoning verification) rather than claiming the general framework as novel.",
    "IMPORTANT: Bayless et al. 'A Neurosymbolic Approach to Natural Language Formalization and Verification' (arXiv 2511.09008, Nov 2025) is NOT cited. This paper uses redundant formalization with semantic equivalence checking for roundtrip verification, achieving >99% soundness at the most conservative threshold with only 2.5% false positive rate. It directly anticipates the roundtrip verification component of the proposal and should be cited alongside arXiv 2604.25031.",
    "MATH-VF 'Step-Wise Formal Verification for LLM-Based Mathematical Problem Solving' (arXiv 2505.20869, May 2025) is NOT cited. It uses Z3 + SymPy for step-by-step verification with a Formalizer + Critic architecture, which is structurally similar to the proposal's approach. It should be cited as related work.",
    "The roundtrip verification paper's (arXiv 2604.25031) cost efficiency claim is cherry-picked: '7.21 LLM calls per repair vs. 12.27 for random baseline' comes from Claude on the Traffic domain only. For GPT, diagnosis-guided repair is MORE expensive than random (14.56 vs 9.77). The equivalence improvement range (45-61% to 83-85%) is also selectively cited from one domain. The proposal should either cite the full range of results or note the model-dependence.",
    "ProofWriter SOTA is ~98% with neurosymbolic methods (LeanReasoner, LINC, ProofFOL). If Qwen3-32B's baseline on ProofWriter is already high, the headroom for improvement may be very limited. The proposal should investigate Qwen3-32B's ProofWriter baseline and clarify which depth levels (D0-D5) are evaluated — deeper problems have lower baselines.",
    "The 'Do LLMs Game Formalization?' paper's findings are slightly overstated in the proposal. The paper finds NO evidence of systematic gaming in unified generation — the unfaithfulness occurs specifically in two-stage pipelines and is model-specific (DeepSeek-R1 in particular). The proposal's framing that 'LLMs systematically mistranslate premises during formalization' should be qualified to reflect the pipeline-specific, model-specific nature of the finding."
  ],
  "feedback": "The proposal has matured significantly over 7 rounds and the core idea is sound. Two actions would bring it to pass quality:\n\n1. **Cite Kiyani et al. (arXiv 2602.17633) and reposition the informativeness-precision tradeoff** (CRITICAL). Kiyani et al. formalize the general weak/strong verification framework with optimal thresholds and Pareto frontiers. Your contribution should be positioned as: (a) a domain-specific instantiation of this general framework for reasoning verification, with Z3-based formalization as the 'strong' verifier and templated constraints as the 'weak' verifier, (b) the addition of roundtrip validation as a FAITHFULNESS check orthogonal to the confidence threshold (Kiyani et al. assume the strong verifier is correct — your roundtrip mechanism addresses what happens when even the 'strong' formalization is systematically unfaithful), and (c) the online assertion-level cumulative tracking for derivation tasks. This actually STRENGTHENS your contribution: you're not just proposing a tradeoff framework, you're solving a problem (systematic unfaithfulness) that Kiyani et al.'s framework cannot handle because it assumes the strong verifier is reliable.\n\n2. **Cite Bayless et al. (arXiv 2511.09008) and MATH-VF (arXiv 2505.20869) as related work.** Bayless et al.'s redundant formalization + equivalence checking achieves >99% soundness but does not operate online during generation or use confidence-gated tiering. MATH-VF uses Z3+SymPy for step-wise verification but without confidence gating, roundtrip validation, or online cumulative tracking. These citations actually validate your approach — they show the individual components work, while your contribution is the principled integration.\n\n3. **Minor fixes**: (a) Qualify the roundtrip cost claim as model-dependent, (b) qualify the 'Do LLMs Game Formalization?' findings as pipeline-specific, (c) investigate ProofWriter baseline with Qwen3-32B to assess headroom, (d) consider citing SpecGuard (arXiv 2604.15244) as concurrent work on online step-level verification.",
  "reason": "Strong core idea with accurate related work characterization, but missing a critical competitor (Kiyani et al.) that directly anticipates the informativeness-precision tradeoff framework claimed as a contribution — requires citation and repositioning."
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "40732fd1-b656-41ff-9b35-2bccaa23780b",
  "isSidechain": false,
  "requestId": "req_011CawmFsqQuF3hGpqxvU4B5",
  "type": "assistant",
  "uuid": "80b53cb0-ec62-42d2-8d80-823aee973106",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ae8c16f5-ce1c-4bce-923e-3afb8499b025",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018ukR9xrRXUQmeSgRXt5aSY",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2916,
      "cache_read_input_tokens": 57903,
      "output_tokens": 3858,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2916,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3858,
          "cache_read_input_tokens": 57903,
          "cache_creation_input_tokens": 2916,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2916
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

_source line 45_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-11 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "80b53cb0-ec62-42d2-8d80-823aee973106",
  "sessionId": "ae8c16f5-ce1c-4bce-923e-3afb8499b025"
}
```

---

### Runtime record

_source line 46_

```json
{
  "type": "ai-title",
  "aiTitle": "Two-tier confidence-gated formalization for online derivation verification",
  "sessionId": "ae8c16f5-ce1c-4bce-923e-3afb8499b025"
}
```

---

### Runtime record

_source line 47_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-11 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "80b53cb0-ec62-42d2-8d80-823aee973106",
  "sessionId": "ae8c16f5-ce1c-4bce-923e-3afb8499b025"
}
```

---

### Runtime record

_source line 48_

```json
{
  "type": "ai-title",
  "aiTitle": "Two-tier confidence-gated formalization for online derivation verification",
  "sessionId": "ae8c16f5-ce1c-4bce-923e-3afb8499b025"
}
```

---
