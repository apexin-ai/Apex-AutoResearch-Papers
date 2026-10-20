# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义： 含义：所有 pending 实验确认核心假设；论文叙事成功传达 non-obvious insights；审稿人认为 violation landscape 

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 18
- **Recorded user turns:** 1
- **Tool calls:** 2
- **Original source:** `logs/chats/exported-trajectories/account-1/91d3e0f3-a355-4901-81d3-cef73f6dac5a.jsonl`
- **Structured JSON:** [`f4f4406ecd32db858765.json`](../../sessions/f4/f4f4406ecd32db858765.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-18T16:20:00.248Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-18T16:20:00.248Z",
  "sessionId": "91d3e0f3-a355-4901-81d3-cef73f6dac5a",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：\n\n含义：所有 pending 实验确认核心假设；论文叙事成功传达 non-obvious insights；审稿人认为 violation landscape + enabling dependency + cross-task generalization 三者构成完整且新颖的贡献\n核心假设：['70B DocRED DR baseline ≥15%，证明 scale 不能消除 ontology violations', '70B DocRED OntoCoDec DR reduction ≥80%，F1 neutral-to-positive', 'WikiEvents cross-task story 被接受为 generality 证据（mechanism generalization，非 SOTA performance）', 'Enabling dependency (grammar enables semantic) 被至少 2/3 审稿人识别为 non-trivial architectural insight', 'Tightness × RV baseline dual-factor 和 post-hoc EE 99.6% rejection 被视为 surprising findings', 'CF tradeoff 的 proactive disclosure + root cause analysis + type ambiguity 证据被接受为 honest limitation']\n关键指标范围：{'70b_docred_dr_baseline_pct': [15, 25], '70b_docred_dr_constrained_pct': [1, 5], '70b_docred_dr_reduction_pct': [80, 95], '70b_docred_rf1_delta_pp': [-0.3, 0.5], 'avg_reviewer_score': [3.75, 4.25], 'novelty_score_avg': [3.5, 4.0], 'soundness_score_avg': [4.0, 4.5], 'reviewers_seeing_novelty_ratio': [0.67, 1.0], 'rebuttal_needed': False}\n叙事方向：原始 framing 完全成立：\"universal ontology-constrained structured generation framework\"。 三条 evidence lines 完整落地：(1) 70B 仍有 15%+ violations → scale 不是解法， (2) EE cross-task RoV→0% + post-hoc 99.6% rejection → 框架必要性， (3) 4 models × 3 datasets × 2 tasks → 充分泛化性。 Claims 无需降级。§1 intro 以 \"even 70B models violate at double-digit rates\" 开篇， §5.4 WikiEvents 作为 generality 的 crown jewel， §5.5 tightness × RV interaction 作为 analytical insight 独立贡献。 CF 在 §7 limitations 清晰定位为 \"local enforcement inherent tradeoff, not method defect\"。\n\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: schema_semantic_constrained_ie\nfocus: 目标 4.0 Conference Accept。当前 3.5 的瓶颈是 \"novelty incremental, core conclusion 直觉上显然\"。请重点审查：(1) 论文 story 是否让审稿人感到 \"有我没想到的东西\"；(2) 哪些非显然发现（70B 仍有违规、post-hoc EE 99.6% 删除、enabling dependency、non-rectangularity）的呈现是否足够突出；(3) 实验覆盖面是否有盲点（3 models × 3 datasets × ablation + 70B + beam + sampling + latency）；(4) 从 3.5 到 4.0 的具体可操作建议。\n\n## paper_framing.md\n\n# OntoCoDec — Paper Framing\n\n## Target Venue\nEMNLP 2026 (ARR submission May 25, 2026) — **目标: conference main**（D040, 用户明确指示）\n\n## Title\nOntoCoDec: Type-Valid Information Extraction via Compiled Ontology Constraints\n(D015: \"Near-Complete\" dropped — DocRED residual DR=10.21% (Qwen) 不算 near-complete。论文贡献是方法，不是特定消除率。SciERC 0.93% 和 DocRED 2.55% (Llama) 可在正文中描述为 near-complete，但 title 不宜 overclaim。)\n\n**D040 Story 升级方向**: 从 \"IE-specific constrained decoding\" → \"universal ontology-constrained structured generation framework\"。WikiEvents Event Extraction 验证跨任务泛化。Continuation masking v2 突破（10-doc: RoV 0%, semantic violations ↓95.8%）初步确认跨任务有效性，全量实验进行中。最终 title 待全量结果后调整。\n\n## Core Insight\nLLM-based IE systems produce systematic ontology constraint violations concentrated in specific relation types. Prompt-level intervention (schema-informed prompting) reduces violations by ~62% but cannot eliminate them — certain relation types retain 25-30% violation rates even with explicit constraint descriptions. OntoCoDec provides **near-complete elimination (DR 15.4%→0.93%, ↓94%) at zero or positive F1 impact** through automatic ontology-to-decoder constraint compilation with two complementary layers.\n\n**Phase 2 confirmed (D012 bootstrap CI, v2 fix)**: Grammar+Semantic dual-layer constrained decoding reduces domain/range violations by 94%, eliminates entity-type and relation-vocabulary violations entirely (→0%). F1 impact is **dataset-dependent**:\n- SciERC: Rel F1 neutral (+0.13pp, p=0.58), Ent F1 neutral (-0.03pp, p=0.53)\n- DocRED: Rel F1 **significantly improved** (+0.50pp, p<0.001, 95% CI [+0.23, +0.81]); Ent F1 **significantly improved** (+1.23pp, p<0.001, 95% CI [+0.94, +1.55])\n- Mechanism: grammar 消除 OOV relation names (DocRED RV 29.66%→0.03%) + 非标 entity types (ET 2.48%→0%)。all_set F1 方法下 OOV=FP → fewer FP → higher precision/F1。SciERC baseline RV/ET 已很低，效果不显著。\n- **Grammar 层是 F1 提升的唯一来源**: grammar_only Ent F1=59.38% ≈ full_s1 59.37% (Δ+0.01pp, p=0.66)。Semantic 层对 F1 无额外贡献，专注 DR reduction。\n\n## Core Claims\n\n### Claim 1 (Empirical): Violation Landscape\nLLM-based IE systems violate ontology type constraints at non-trivial rates (15.4% per-triple on SciERC, 18.7% on DocRED). Violations are **not uniformly distributed** — they concentrate on relation types with tight domain/range constraints (Feature-of 33.5%, Compare 42.4%) while loose-constraint relations show near-zero violation (Used-for 0.8%).\n\n**Key insight**: Violation rate is driven by **constraint tightness**, not ontology size. A small ontology with tight constraints can produce more violations than a large ontology with loose constraints.\n\n**D014 修订**: DR reduction ceiling 由 **tightness × model RV baseline** 共同决定，非 tightness 单因素。Llama DocRED DR↓90.2% vs Qwen DR↓44.7%（同一 ontology τ̄=0.842）。机制：Qwen RV=29.66% >> Llama RV=16.03% → grammar 层将 OOV triples 强制匹配有效关系名 → 揭露大量 latent DR violations → 残余 DR 更高。这是比单一 tightness 更深的 insight。\n\n**Evidence**: SciERC (7 relations) 15.4%; DocRED (96 relations) 18.7% — comparable rates despite 14× ontology size difference. Schema-informed prompt on DocRED only achieves DR↓32% (vs SciERC ↓62%), confirming **prompt-level intervention scales poorly with ontology complexity**.\n\n### Claim 2 (Empirical): Prompt Insufficiency\nSchema-informed prompting (explicitly describing domain/range constraints in the prompt) reduces but does not eliminate violations:\n- Overall: 15.4% → 5.78% (-62.4%), still above 5%\n- Per-relation: Compare 42.4% → 27.6%, Evaluate-for 24.1% → 29.9% (**worse**)\n- Prompt intervention is unreliable at the per-relation level — some relations improve, one regresses\n\n**Narrative**: This is NOT about \"5.78% barely above 5%\". The story is: **prompt-level intervention is fundamentally unreliable as a guarantee mechanism**. It works statistically but cannot provide per-instance compliance. Three specific relation types retain >10% violation rates with schema-informed prompts. For safety-critical IE (biomedical, legal, regulatory), statistical reduction is insufficient — guaranteed compliance is required.\n\n### Claim 3 (Methodological): Composable Constraint Framework\nOntoCoDec automatically compiles IE ontology schemas into two composable constraint layers:\n1. **Grammar layer** (XGrammar): JSON structure + type vocabulary constraints (CFG-expressible)\n2. **Semantic layer** (TypeConstraintProcessor): Cross-field domain/range constraints via stateful entity registry + dynamic logit masking\n\nThe two layers are **complementary with enabling dependency**: grammar ensures every generated relation type is in the valid vocabulary, which enables the semantic layer to look up and enforce domain/range rules for that type. Without grammar, the semantic layer encounters unknown relation types and cannot enforce constraints (explaining why semantic_only achieves only ↓24% vs full_s1 ↓94%). This is NOT \"synergistic\" (mutual amplification) — grammar is a prerequisite for semantic, not vice versa.\n\nThe two layers compose via bitwise AND of token masks. Recommended framing: \"Grammar and semantic constraints compose via bitwise AND with an enabling dependency: grammar ensures structural validity, enabling semantic constraints to enforce domain/range rules. When constraint tightness creates empty intersection between layers, the system degrades gracefully to grammar-only constraints, maintaining structural validity as a guaranteed floor.\"\n\n**Graceful degradation + Fallback 频率量化** (D008 + Reviewer 发现):\nWhen $M_{semantic} \\cap M_{grammar} = \\emptyset$, the system falls back to grammar-only control.\n\n**关键量化数据（Reviewer 从日志挖掘）**:\n- Llama DocRED full_s1: **32,921 次 fallback / 577 docs = ~57 次/doc**\n- Llama SciERC full_s1: **5,882 次 fallback / 550 docs = ~10.7 次/doc**\n- DocRED fallback 频率是 SciERC 的 **5.3×**\n- Qwen DocRED fallback 率未知（日志当时无 fallback logging，需估算）\n\n**这直接解释了 DocRED DR 残余 10.19% vs SciERC 0.93%**: 更多 token 位置退化为 grammar-only → grammar-only 的 DR 已知为 26.17% → 高 fallback = 高残余 DR。\n\n**论文建议**: 在 §5 tightness 段报告 fallback 率，定义 \"Constraint Coverage\" 指标（semantic masking 实际生效的 token 比例）。这把 \"10.19% DR 残余\" 从弱点变成可量化分析的 finding。Frame as \"engineering robustness\" in §4; fallback 频率 + tightness 作为 §5 定量分析。\n\n**Decidability taxonomy**: Constraints classified by prefix-decidability:\n- (a) Purely local: entity type ∈ vocabulary (grammar layer)\n- (b) Prefix-decidable with state: relation argument types compatible with domain/range (semantic layer, requires entity registry)\n- (c) Truly non-local: forward coreference — out of scope for forward-only decoding\n\n### Claim 4 (Methodological): S1 vs S2 Decoding Strategies — Architectural Ablation\n- S1 (single-pass): Both layers applied throughout generation. **Recommended primary strategy** — simpler, slightly better metrics across the board.\n- S2 (two-pass): Pass 1 extracts entities (grammar-only), Pass 2 generates relations with input-dependent grammar compiled from Pass 1 entities.\n\n**S2 full results (551/551 SciERC)**: DR 0.97% (vs S1 0.93%), CF 8.03% (vs S1 9.9%), R-F1 8.03% (vs S1 8.36%). S2 does NOT solve CF — the 1.87pp reduction is not significant. S2 also slightly worse on DR and F1. **S2 is an architectural variant demonstrating framework flexibility, not a CF solution.** Position in paper as ablation (Section 5 or Appendix), not as a core contribution.\n\n⚠️ **Do NOT cite pilot50 DR=0% as S2 evidence** — small-sample artifact; full run shows DR=0.97%. Per-relation S2 DR is worse than S1 on Compare (4.6% vs 2.82%), Part-of (1.25% vs 0%), Used-for (0.12% vs 0%).\n\n### Claim 5 (Empirical): Cross-Task Generalization — Event Extraction (D040, NEW)\n**Status**: ✅ All 3 models × 246 docs complete (v3 with collision fix + exact-match fix)\n\nOntoCoDec generalizes beyond Relation Extraction to **Event Extraction** (WikiEvents, Li et al. NAACL 2021), demonstrating that the framework is task-agnostic for any IE task with ontology-defined type constraints.\n\n**Cross-task framing (Reviewer 评估 confirmed)**:\n- **RoV 是 DR 的正确对应物**（不是 RV）：EE 中 per-type violation rate 是 RE 的 3-5×，支持 \"more complex ontology → more critical constraint enforcement\" claim\n- **三层级联 Grammar→RoV→AC**（比 RE 的 Grammar→DR 两层更丰富）：grammar 消除 EV，使 semantic layer 可以 enforce role restriction (RoV→0%)，进而暴露 AC violations。这强化 architecture contribution 论证。\n- **Semantic layer 是 EE 的唯一防线**：grammar 层对 role vocabulary 无能力，只有 semantic layer + continuation masking 能 enforce per-event-type role constraints\n- **\"Practical value\" 防线**：Arg F1 ≈ 0% 不削弱 claim，因为 (a) mechanism generalization 是 contribution 不是 SOTA performance，(b) FT composability 已在 RE 中证明 high-F1 场景有效\n\n**WikiEvents specifics** (DARPA KAIROS ontology):\n- 56 event types × 80 argument roles × 27 entity types（含 5 个补充 Contact 子类型 + CRM entity type）\n- 245 组显式 (event_type, role) → allowed_entity_types 约束\n- Maps directly to OntoCoDec's semantic layer: argument role type constraints ≡ domain/range constraints\n- 27 entity types（比 ACE05 的 7 个更丰富）→ constraint space 更大，更能展示 semantic layer 价值\n- 99.98% 数据满足约束 → 约束定义是真实有效的\n- Hierarchical event names (e.g., Conflict.Attack.DetonateExplode) → 扁平化为 leaf-node 解决 first-token collision（96.1%→3.9%）\n\n**数据集选择理由**（MAVEN/RAMS 排除）：\n- MAVEN (168 types): 无 argument extraction，不适用\n- MAVEN-Arg (162 types): FrameNet-based，无 role→entity_type schema 约束\n- RAMS (139 types): 仅 cardinality 约束，无 entity type binding\n- ACE05 (33 types): LDC 付费，采购周期来不及\n- **WikiEvents 是唯一同时满足 \"免费 + 有显式 role→entity_type 约束\" 的数据集**\n\n**Violation 分类** (5 类，从 RE 的 4 类扩展):\n- ET (Entity Type): entity type 不在 ontology 合法类型列表中\n- EV (Event Vocabulary): event type 不在 ontology 定义中\n- RoV (Role Vocabulary): argument role 不在该 event type 定义中\n- AC (Argument Constraint): argument entity type 不满足 role→entity_type 约束（DR 的自然推广）\n- CF (Cross-Field): 同一 entity 跨 event 被赋予不同 type\n\n**Full results (246 docs, v3 final — collision fix + exact-match fix)**:\n\n| Metric | Qwen3-8B uncon. | Qwen3-8B Full S1 | Llama-3.1-8B uncon. | Llama-3.1-8B Full S1 | Mistral-7B uncon. | Mistral-7B Full S1 |\n|--------|-----------------|-------------------|---------------------|----------------------|-------------------|---------------------|\n| Parse | 88.6% | 83.7% | 91.9% | 84.1% | 88.6% | 88.6% |\n| EV | 24.0% | **0%** | 10.5% | **0%** | 37.3% | **0%** |\n| RoV | 74.9% | **0%** | 88.8% | **0%** | 63.9% | **0%** |\n| AC | 0.3% | 2.1% | 0.1% | 3.8% | 0% | 1.3% |\n| CF | 0% | 21.1% | 0% | 17.2% | 0% | 14.9% |\n| Trigger F1 | 11.8% | 13.4% | 5.7% | 7.5% | 2.4% | 3.9% |\n| Ent F1 | 0% | 14.1% | 0% | 17.6% | 0% | 11.7% |\n\n**Grammar-only ablation (Mistral v3, all 3 models)**:\n- Grammar eliminates EV→0% but RoV remains 64-77%: grammar CFG cannot constrain 80 argument roles conditioned on event context\n- AC rises to 8-14% under grammar-only (latent violation surfacing pattern, same as DocRED RE)\n- Proves semantic layer is essential for EE: two-layer architecture is necessary, not just convenient\n\n**Post-hoc filtering comparison (devastating)**:\n- Qwen: 5,467→23 arguments (99.6% discarded) to reach 0% violation\n- Llama: 5,053→3 arguments (99.9% discarded)\n- Mistral: 6,034→0 arguments (100% discarded)\n- Post-hoc is not viable for EE (contrasts with RE where it's expensive but functional)\n\n**BPE collision diagnostic (confirmed 2026-05-18)**:\n- Qwen (BPE, ~152K vocab): **0 collision groups** — all 27 entity types have unique first tokens\n- Llama (BPE, ~128K vocab): **0 collision groups** — same\n- Mistral (SentencePiece, ~32K vocab): **2 collision groups** (SID/SEN/SIDE→'S', BAL/BOD→'B')\n- **Residual AC narrative**: Mistral AC 1.3% = residual after collision fix (was 16.6%); Qwen/Llama AC 2.1-3.8% = purely model semantic confusion (confuses similar entity types like SID vs SEN), NOT tokenizer collision\n\n**关键 findings**:\n- RoV 是压倒性违规（64-89%），远超 RE 的 RV（1-30%）→ 更强力展示 constraint 需求\n- EV 显著（10-37%）→ grammar 层直接消除\n- **Entity F1 从 0% 恢复到 11.7-17.6%**: 不是语义改进，是 format compliance 恢复——grammar enforcement 产生 schema-valid JSON，parser 才能识别 entity mentions\n- Trigger F1 +1.5 to +1.8pp: elimination of OOV event types counted as FP\n- CF 15-21% 比 RE 更高（EE argument structure 更复杂），沿用 RE 的 CF tradeoff framing\n\n**Story upgrade**: WikiEvents results confirm paper narrative: \"universal ontology-constrained structured generation framework applicable to any IE task with formal type constraints\". Three evidence lines: (1) EV/RoV→0% across all models, (2) grammar-only ablation proves two-layer necessity, (3) post-hoc filtering is non-viable for EE. This is the key differentiator for conference main vs Findings.\n\n**70B scale experiment** (P029-P030, in progress): Qwen3-70B AWQ-INT4 on SciERC + DocRED to demonstrate scale generalization. If successful, adds a 4th model to cross-model evidence, strengthening C5.\n\n**Remaining risk**:\n- CF 15-21% higher than RE → continues CF tradeoff framing\n- 70B experiment timeline tight (need results by May 20 for paper integration)\n\n## Anticipated Reviewer Concerns\n\n### C1: \"5.78% is barely above 5% — threshold is arbitrary\"\n**Response**: Don't argue about the threshold. Argue about per-relation distribution: Compare (27.6%), Evaluate-for (29.9%), Feature-of (11.3%) have double-digit violation rates with schema-informed prompt. The value proposition is per-relation guaranteed compliance, not overall statistical rate.\n\n### C2: \"Why not just post-hoc filter?\"\n**Response (D013, 实验结果已出)**:\n\nPost-hoc filtering 实验结果：post-hoc F1 > OntoCoDec F1（SciERC 8.63 vs 8.36, DocRED 9.61 vs 8.24）——因 low F1 regime 下移除 FP 大幅提升 precision。\n\n**论文 framing（不以 F1 论高低，多维对比）**:\n1. **Recall 维度（核心论点）**: OntoCoDec recall 上升 (SciERC +0.20pp, DocRED +0.56pp) = 概率质量重分配到合法 token 生效。Post-hoc recall 下降 (SciERC -0.72pp, DocRED -1.06pp) = 正确 triple 被误删。\n2. **Information coverage**: DocRED post-hoc 丢弃 **48.1%** triples（近半数信息丢失），SciERC 16.8%。OntoCoDec 保留全部 triple slots。\n3. **Operational**: OntoCoDec 产出即合规、无需后处理、支持流式。Post-hoc 需额外管线、不适用实时场景。\n4. **Precision trade-off（诚实承认）**: \"Post-hoc achieves higher precision by removing a large fraction of triples, many of which are incorrect. This trades information coverage for precision — valid when FP are costly, but inadequate when completeness matters.\"\n\n数据表：SciERC post-hoc rejection 16.8%, OntoCoDec recall 11.60 vs post-hoc 10.68; DocRED post-hoc rejection 48.1%, OntoCoDec recall 10.02 vs post-hoc 8.40。\n\n**Reviewer 补充发现（D013 后）**:\n5. **ET 残余**：post-hoc 只删 triples 不改 entity list，残余 ET=0.4% (SciERC) / 2.47% (DocRED)。OntoCoDec ET=0%。Post-hoc 无法解决 entity type 违规。\n6. **127 个被删 TP (DocRED)**：过滤前 TP=1137，过滤后 TP=1010。丢失的 127 个 TP（11.2%）是正确提取但 entity type 违规的 triple。OntoCoDec 通过生成时强制合法 type 保留这些 TP——\"prevent vs detect\" 核心论据的具体数据。\n7. **OntoCoDec+post-hoc 组合**（future work idea）：先 constrain 再 filter 残余 DR。低优先级，May 19 前不做。\n\n### C3: \"Bitwise AND of two masks is not novel\"\n**Response**: The novelty is not the AND operation — it's (a) the automatic compilation from ontology definitions (zero-code schema compliance), (b) the stateful entity registry enabling cross-field constraints during autoregressive generation, (c) the decidability taxonomy providing theoretical guidance, and (d) the systematic violation landscape measurement motivating the approach.\n\n### C4: \"Evaluate-for violation rate increases with schema-informed prompt\"\n**Response (prior-constraint conflict framework)**: Evaluate-for has 23/36 valid pairs; Method→Task is invalid for Evaluate-for but natural in the LLM's distributional prior (\"Method X evaluates for Task Y\" is semantically plausible). Schema-informed prompting creates a **prior-constraint conflict**: the model learns to avoid Method→Task for Evaluate-for (reducing count 133→87, -34.6%), but the remaining instances are harder boundary cases where the model's type assignment strategy becomes less stable. This is not just \"harder instances\" — it's an active interference between prompt-level constraint signals and the model's learned type associations.\n\n**This strengthens the paper's claim**: prompt-level intervention is not merely insufficient but potentially **counterproductive** for specific constraint configurations. Decoding-time enforcement avoids this issue entirely — it operates on logits, not on the model's reasoning process, so there is no prior-constraint conflict.\n\n### C5: \"Only tested on one model (Qwen3-8B)\"\n**Response**: Cross-model validation DONE (D016 bootstrap verified). Llama-3.1-8B 零代码修改：\n- SciERC: DR 13.34%→0.08% (↓99.4%), R-F1 -0.14pp (p=0.011, negligible), E-F1 NS\n- DocRED: DR 26.07%→2.55% (↓90.2%), R-F1 +0.29pp (p=0.013, significant), E-F1 -0.64pp (p=0.022, modest decline)\n- Parse failures: unconstrained 68 vs full_s1 91 (6.8% vs 9.1%)\n\n**Cross-model claim 指导（Reviewer 专项评估）**:\n- ✅ 可声明：\"OntoCoDec generalizes across model families without code modification\"（程序性事实，铁证）\n- ❌ 不可声明：\"consistently achieves the same reduction rate\"（仅 2 模型，不足以量化声明）\n- **RV↓DR↑ 正交性 finding**: Llama RV baseline 低(16%) 但 DR baseline 高(26%)，反向于 Qwen。证明两层约束解决正交 failure modes——vocabulary compliance ≠ semantic compliance。应作为 §5 cross-model 独立 finding 展开。\n- **Parse failure 偏差**: checker skip parse failures (不计入 F1)，Llama 68/998=6.8% vs Qwen 12/998=1.2%。偏差方向保守（不利于 constrained），不威胁 claim。但需 footnote 披露 + cross-model 表增加 parse failure rate 行。\n- **Llama SciERC CF=6.56%**: 比 Qwen 同量级更高，non-local constraint 问题在 Llama 上更突出，limitations 提及。\n- 等 llama_docred_full_s1 出来后定最终 claim 措辞。\n\n### C6: \"Constrained decoding degrades generation quality (CRANE, Structure Snowballing)\"\n**Response**: OntoCoDec's semantic constraints are narrower than full grammar constraints — only type tokens are masked, free text is unconstrained. **Bootstrap CI (10000×, D012 Qwen + D016 Llama, all registry-aligned)**:\n\n**Qwen3-8B**: SciERC R-F1 +0.13pp (p=0.58, NS), E-F1 -0.03pp (NS). DocRED R-F1 +0.50pp (p<0.001), E-F1 +1.23pp (p<0.001).\n**Llama-3.1-8B**: SciERC R-F1 -0.14pp (p=0.011, negligible), E-F1 NS. DocRED R-F1 +0.29pp (p=0.013), E-F1 -0.64pp (p=0.022).\n\n**Cross-model pattern**: DocRED R-F1 显著提升（两个模型）。E-F1 model-dependent（Qwen +1.23pp, Llama -0.64pp）。\n- 机制：grammar 消除 OOV relation names + 非标 entity types → all_set 方法下减少 FP → precision 提升。Grammar 是 F1 提升的唯一来源（grammar_only Ent F1=59.38% ≈ full_s1 59.37%, Δ=0.01pp, p=0.66）。Semantic 层对 F1 无额外贡献。\n- Frame as: \"On DocRED, R-F1 gains are significant for both models. Entity F1 impact is model-dependent.\"\n- 不升级为 core claim，但如实报告。\n\n### C7: \"Your method trades DR violations for CF violations (cross-field consistency)\"\n**Response**: Both S1 and S2 show elevated CF (per-triple rate ~8-10%). This is an inherent limitation of per-relation independent type enforcement. Must be proactively reported as a limitation. Defense:\n\n**CF 子类型分析（根因已确认）**：\n- **EVR（entity-vs-relation type drift）**: 占 CF 的 >90%。同一 entity 在 entity list 和 relation triple 中被赋予不同 type。S1: 245 entities (7.34%), S2: 178 entities (5.54%, -27%)\n- **Within-rel（同 entity 跨 relation type 不一致）**: S1: 10 (0.36%), S2: 18 (0.72%)\n- S2 减少 EVR 但增加 within-rel——trade-off 更复杂，不是单纯好/差\n\n**Top 冲突模式**: Generic↔OtherScientificTerm (60次), Material↔OtherScientificTerm (28次), Material↔Method (20次)。**这些是 SciERC type system 固有的语义边界模糊区**——同一术语在不同学术语境下确实可以被合理归类为不同 type。CF 在相当程度上是 type system 模糊性的体现，非纯粹的方法缺陷。\n\n**论证层次**：\n1. DR violations = structurally invalid triples（下游系统不可用）→ hard constraint\n2. CF violations = same entity gets different types across relations → individual triples remain type-valid, only cross-triple consistency broken → soft preference\n3. CF 的根因是 type system 语义边界模糊 + per-relation 独立 enforcement，非 bug\n4. Future work: cross-relation global consistency pass (entity-level type consensus before relation-specific enforcement)\n\n**机制归因（口径对账确认）**：grammar_only CF=0.08%（与 unconstrained 持平），full_s1 CF=9.90%，full_s2 CF=8.03%。**CF 100% 由 semantic 层引入，grammar 层无贡献。** 这为 \"CF 是 semantic type enforcement 的系统性副作用\" 提供干净的消融证据。\n\n**论文数字口径**：CF rate 用 violation_checker 口径（denominator=total_entities，与 DR/RV/ET 一致）。分析段落额外给 entity-level EVR 率 + 受影响样本比例。注意：analyze_cf 脚本的 EVR/WR 两维度不是独立的（WR⊂EVR），论文中不要作为两个独立维度报告。\n\n**Do NOT hide this data.** Proactive disclosure + severity distinction + root cause analysis + type ambiguity evidence + 消融归因 = 最强防御策略。\n\n### C8: \"Absolute F1 is too low (~8%) — results are not meaningful\"\n**Response**: This is a zero-shot extraction setting (no training data, no fine-tuning). Low F1 is expected — supervised SOTA on SciERC relation F1 is ~40-50%. Our contribution is the constraint enforcement method, not extraction quality. F1 is a control variable verifying constraints don't degrade quality, not an optimization target. Recommended framing: \"We evaluate in a zero-shot setting to demonstrate that our constraint enforcement method works without task-specific training. F1 is reported to verify that constraint enforcement does not degrade extraction quality, not as a claim of state-of-the-art performance.\"\n\n## Paper Structure (Draft — D040 updated)\n1. Introduction: Ontology constraint violations in LLM-based structured generation + composable framework overview (story: not just RE, general ontology-constrained generation)\n2. Background: Grammar-constrained decoding (XGrammar) + IE ontology structure\n3. Violation Landscape Study (Phase 0 empirics — independent contribution)\n4. OntoCoDec Framework: Compiler + TypeConstraintProcessor + S1/S2 strategies\n5. Experiments:\n   - §5.1-5.3: RE experiments (SciERC + DocRED, 3 models, constrained vs unconstrained vs post-hoc vs prompt-based)\n   - §5.4: **Event Extraction (WikiEvents)** — cross-task generalization (D040)\n   - §5.5: Ablation + analysis (composability, latency, beam search, etc.)\n6. Related Work: 5 constraint paradigms (grammar, vocabulary, structural, type-checking, ontology) + event extraction methods\n7. Conclusion: Framework generality across IE tasks\n\n## Claim Calibration (per Reviewer assessment)\n\n**Safe to claim (sufficient evidence from Phase 2)**:\n- \"First systematic study of ontology constraint violations in LLM-based IE\"\n- \"Violation rate correlates with constraint tightness, not ontology size\" (D014: DR reduction ceiling 由 tightness × model RV baseline 共同决定)\n- \"Grammar+semantic constrained decoding eliminates 94% of DR violations at zero F1 cost\" ✅ Phase 2 confirmed\n- \"Two-layer architecture provides complementary coverage — grammar enables semantic\" ✅ Ablation confirmed\n- \"Prompt-level intervention scales poorly with ontology complexity\" ✅ SciERC ↓62% vs DocRED ↓32%\n\n**Claim with caution**:\n- \"Near-complete type-valid IE\" — S1 0.93%, S2 0.97% residual, not truly 0%. Title updated to \"Near-Complete\"\n- \"Principled framework applicable to arbitrary IE ontologies\" — RE validated on 2 datasets × 2 models; EE (WikiEvents) 10-doc preliminary shows ↓95.8% semantic violations, full results pending\n- \"F1 improvement\" — SciERC: not significant (p=0.58), frame as F1-neutral; DocRED: significant (+0.50pp, p<0.001), 可报告但不升级为 core claim，归因于 OOV elimination 而非约束解码本身的提升\n- \"CF reveals type system ambiguity\" — 可在 §5.3 作为 analysis finding 展开（Generic↔OtherScientificTerm 等模式有独立 insight 价值），但 §7 必须同时保留 CF 作为 limitation + future work。**两处都要有，缺一不可。** 不能暗示\"因为是 type ambiguity 所以 CF 可接受\"\n\n**Do NOT claim**:\n- \"General infrastructure for IE\" — only zero-shot extraction validated\n- \"State-of-the-art\" — F1 is control variable, not optimization target (see C8)\n- \"Synergistic effect\" — mechanism is enabling dependency, not mutual amplification (see Claim 3)\n- \"S2 solves CF\" or \"S2 mitigates Structure Snowballing\" — data shows S2 ≈ S1 on all metrics; position as architectural variant only\n- \"Pilot50 DR=0%\" — small-sample artifact, full S2 has DR=0.97%\n- \"Grammar-first invariant\" 作为独立 claim — 证据不足（仅 1 次崩溃触发，实现是 fallback 非形式化保证）。写入 §4 方法论设计原则（1-2 句），不升级为 claim\n- \"Robust dual-layer composition across schema complexities\" — 等 DocRED 完成。最终如 fallback ≤5/998，可写经验性陈述，不做泛化 claim\n\n## Risk Ranking (ordered by reject probability)\n\n1. **CF violation trade-off under-addressed** (MEDIUM-HIGH): S1 9.9%, S2 8.03% — both elevated. **S2 confirmed: does NOT solve CF.** This is the #1 attack surface. Mitigated by proactive disclosure + severity distinction + root cause analysis (C7). Must be reported as explicit limitation with future work direction (global entity-type consensus).\n2. ~~**Single model limitation**~~ (RESOLVED): Llama-3.1-8B SciERC ✅ (DR↓99.4%) + DocRED ✅ (DR↓90.2%). 2 模型 × 2 数据集全矩阵完成。\n3. **Novelty perception** (MEDIUM): \"PLDI'25 for code → OntoCoDec for IE\" attack line. Must argue IE constraint structure differs fundamentally.\n4. ~~**DocRED Phase 2 weak**~~ (RESOLVED → reframed as D014): Qwen DR↓44.7%, Llama DR↓90.2% — both substantial. Weaker Qwen reduction explained by RV baseline interaction (D014), not method failure.\n5. ~~**Phase 2 F1 drop**~~ (RESOLVED): F1 confirmed neutral (SciERC) or positive (DocRED, p<0.001). Bootstrap CI D012 confirms. No longer a risk.\n\n## Critical Path to EMNLP Submission (May 25)\n\n- **May 13-14**: Phase 0 + Phase 1 + Phase 2 SciERC ✅\n- **May 14**: Phase 2 DocRED 4-way ablation ✅ + Llama SciERC cross-model ✅ + Dream 完成 (3/6)\n- **May 14-15**: Llama DocRED ✅ + Checker 修正 ✅ + post-hoc ✅ + bootstrap CI ✅ + related work ✅\n- **May 15-17**: Prompt sensitivity ✅ + WikiEvents pipeline 开发 + continuation v2 突破\n- **May 17-18**: WikiEvents 3 模型 unconstrained baselines (进行中) + constrained 全量\n- **May 18-19**: WikiEvents 结果分析 + §5.4 Event Extraction 章节撰写\n- **May 19-20**: Intro/Abstract/Conclusion 升级（cross-task story）+ 内部稿 → submit_paper_to_review\n- **May 20-24**: Review 修改 + 最终提交\n\n**当前瓶颈**: WikiEvents 全量实验完成是关键路径。3 模型 unconstrained baselines 并行进行中（Qwen ~68/246, Mistral ~31/246, Llama 重启中），constrained 实验随后立即启动。\n\n## Status\n- Phase 0 SciERC: ✅ Complete (minimal + schema-informed)\n- Phase 0 DocRED: ✅ Complete (minimal 18.7% DR + schema-informed 12.8% DR)\n- Phase 1 Compiler: ✅ Complete (grammar + semantic layers integrated)\n- Phase 2 SciERC (5 configs): ✅ Complete (S1 DR↓94% F1-neutral, S2 降级为 ablation)\n- Phase 2 DocRED (4 configs): ✅ Complete (full_s1 DR↓45%, grammar ET/RV→0%)\n- Llama SciERC cross-model: ✅ Complete (DR↓99.4%, F1-neutral, 零代码修改)\n- Llama DocRED cross-model: ✅ Complete (full_s1 DR↓90.2%, unconstrained DR=26.07%)\n- Checker v2 (D011): ✅ Fixed (ET triple-counting → unique entity dedup)\n- Bootstrap CI (D012): ✅ Fixed + confirmed (entity filter bug resolved)\n- Post-hoc baseline (D013): ✅ Complete (multi-dimensional framing)\n- Related work: ✅ 42 bib entries, 4 additions merged\n- Dream 6/6 actions: ✅ All complete\n- CF violation analysis: ✅ Confirmed inherent limitation (S1 9.9% SciERC / 2.57% DocRED / 12.02% Llama DocRED)\n- D014 tightness revision: ✅ Complete (tightness × RV baseline dual-factor)\n- Llama bootstrap CI (D016): ✅ Fixed + verified (registry-aligned ≤0.05pp, all p-values in paper)\n- Paper compilation: ✅ 8 pages正文 + appendix\n- R5 text fixes (N1/N2/N3/W1-W6): ✅ All complete and verified\n- Prompt sensitivity analysis: ✅ Complete (3 prompts × 2 modes, DR reduction 94.0-94.6%, σ=0.3pp; appendix written)\n- Doc length breakdown: ✅ Complete (appendix written)\n- **WikiEvents Event Extraction (D040)**: 🔄 Continuation v2 突破 (10-doc: RoV 0%, semantic ↓95.8%); 3 模型 unconstrained baselines 进行中; constrained 全量待启动\n\n\n## registry (completed experiments)\n\n- exp_id: mvp_phase0_violation_rate\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_triples: 1724\n    total_entities: 2474\n    json_parse_rate: 1\n    entity_type_violation_rate: 0.004\n    relation_vocabulary_violation_rate: 0.0139\n    domain_range_violation_rate: 0.1537\n    cross_field_consistency_violation_rate: 0.0008\n    go_nogo_metric: 0.1537\n    entity_f1: 0.3101\n    relation_f1: 0.0823\n    per_relation:\n      Used-for:\n        total: 787\n        dr_violations: 6\n        rate: 0.0076\n      Conjunction:\n        total: 32\n        dr_violations: 0\n        rate: 0\n      Hyponym-of:\n        total: 124\n        dr_violations: 18\n        rate: 0.1452\n      Evaluate-for:\n        total: 133\n        dr_violations: 32\n        rate: 0.2406\n      Part-of:\n        total: 72\n        dr_violations: 18\n        rate: 0.25\n      Feature-of:\n        total: 486\n        dr_violations: 163\n        rate: 0.3354\n      Compare:\n        total: 66\n        dr_violations: 28\n        rate: 0.4242\n- exp_id: mvp_phase0_violation_rate_docred\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_docs: 998\n    parsed_docs: 962\n    json_parse_rate: 0.964\n    total_entities: 19099\n    total_triples: 16540\n    entity_type_violation_rate: 0.075\n    relation_vocabulary_violation_rate: 0.289\n    domain_range_violation_rate: 0.187\n    cross_field_consistency_violation_rate: 0.0008\n    go_nogo_metric: 0.187\n    fuzzy_matches: 126\n    top_dr_violations_by_rate:\n      P35_head_of_state: 1\n      P710_participant: 0.919\n      P172_ethnic_group: 0.875\n    top_dr_violations_by_count:\n      P31_instance_of:\n        violations: 322\n        total: 533\n        rate: 0.604\n      P1001_applies_to_jurisdiction:\n        violations: 264\n        total: 594\n        rate: 0.444\n      P1344_participant_in:\n        violations: 194\n        total: 312\n        rate: 0.622\n- exp_id: mvp_phase0_scierc_schema\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    domain_range_violation_rate: 0.0578\n    relation_vocabulary_violation_rate: 0.003\n    entity_type_violation_rate: 0\n    total_violation_rate: 0.0253\n    go_nogo_metric: 0.0578\n    total_triples: 1661\n    vs_minimal_dr_reduction: -0.624\n    per_relation:\n      Used-for:\n        rate: TBD\n      Feature-of:\n        delta_pp: -22.3\n      Part-of:\n        delta_pp: -22.5\n      Compare:\n        delta_pp: -14.8\n      Evaluate-for:\n        delta_pp: 5.8\n    mcnemar_all_significant: true\n- exp_id: mvp_phase0_docred_schema\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_documents: 998\n    documents_checked: 943\n    parse_failures: 55\n    json_parse_rate: 0.9449\n    total_entities: 19524\n    total_triples: 16782\n    entity_type_violations: 119\n    entity_type_violation_rate: 0.0061\n    relation_vocabulary_violations: 3090\n    relation_vocabulary_violation_rate: 0.1841\n    relation_fuzzy_matches: 85\n    domain_range_violations: 2154\n    domain_range_violation_rate: 0.1284\n    cross_field_consistency_violations: 29\n    cross_field_consistency_violation_rate: 0.0015\n    total_violations_any: 5392\n    total_violation_rate: 0.1485\n    go_nogo_metric_dr: 0.1284\n- exp_id: phase2_scierc_grammar_only\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_samples: 551\n    total_triples: 1725\n    total_entities: 2474\n    json_parse_rate: 1\n    entity_type_violation_rate: 0\n    relation_vocabulary_violation_rate: 0\n    domain_range_violation_rate: 0.1484\n    cross_field_consistency_violation_rate: 0.0008\n    entity_f1: 0.3098\n    entity_precision: 0.2598\n    entity_recall: 0.3837\n    relation_f1: 0.0823\n    relation_precision: 0.0643\n    relation_recall: 0.114\n    checker_version: fixed_20260514_v2 (strip + alias + unique_et)\n- exp_id: phase2_scierc_semantic_only\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_samples: 551\n    total_triples: 1726\n    total_entities: 2474\n    json_parse_rate: 1\n    entity_type_violation_rate: 0.004\n    relation_vocabulary_violation_rate: 0.0151\n    domain_range_violation_rate: 0.1165\n    cross_field_consistency_violation_rate: 0.0271\n    entity_f1: 0.3101\n    entity_precision: 0.2605\n    entity_recall: 0.3831\n    relation_f1: 0.0815\n    relation_precision: 0.0637\n    relation_recall: 0.1129\n    checker_version: fixed_20260514_v2 (strip + alias + unique_et)\n- exp_id: phase2_scierc_full_s1\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_samples: 551\n    total_triples: 1729\n    total_entities: 2474\n    json_parse_rate: 1\n    entity_type_violation_rate: 0\n    relation_vocabulary_violation_rate: 0\n    domain_range_violation_rate: 0.0093\n    cross_field_consistency_violation_rate: 0.099\n    entity_f1: 0.3098\n    entity_precision: 0.2598\n    entity_recall: 0.3837\n    relation_f1: 0.0836\n    relation_precision: 0.0654\n    relation_recall: 0.116\n    checker_version: fixed_20260514_v2 (strip + alias + unique_et)\n- exp_id: phase2_scierc_unconstrained\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    json_parse_rate: 1\n    entity_f1: 0.3101\n    entity_precision: 0.2605\n    entity_recall: 0.3831\n    relation_f1: 0.0823\n    relation_precision: 0.0644\n    relation_recall: 0.114\n    entity_type_violation_rate: 0.004\n    relation_vocabulary_violation_rate: 0.0139\n    domain_range_violation_rate: 0.1537\n    cross_field_consistency_violation_rate: 0.0008\n    total_triples: 1724\n    total_entities: 2474\n    total_samples: 551\n    checker_version: fixed_20260514_v2 (strip + alias + unique_et)\n- exp_id: phase2_s2_pilot50\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    domain_range_violation_rate: 0.0205\n    relation_vocabulary_violation_rate: 0\n    relation_f1: 0.1008\n    samples: 50\n    predicted_relations: 146\n    true_positives: 13\n    gold_relations: 112\n    entity_f1_approx: 0.29\n    note: 'DR 修正: 原值 0 来自 dryrun (n=25 triples)。实际 pilot50 DR=3/146=2.05% (来自 violation_report_s2_pilot50.json)。'\n- exp_id: mvp_phase0_docred_schema_r2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: phase2_scierc_full_s2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_samples: 551\n    total_triples: 1644\n    total_entities: 2228\n    json_parse_rate: 1\n    entity_type_violation_rate: 0\n    relation_vocabulary_violation_rate: 0\n    domain_range_violation_rate: 0.0097\n    cross_field_consistency_violation_rate: 0.0803\n    entity_precision: 0.2797\n    entity_recall: 0.3712\n    entity_f1: 0.319\n    relation_precision: 0.064\n    relation_recall: 0.1078\n    relation_f1: 0.0803\n    checker_version: fixed_20260514_v2 (strip + alias + unique_et)\n- exp_id: phase2_docred_grammar_only\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    documents_checked: 985\n    parse_failures: 13\n    total_entities: 20150\n    total_triples: 17341\n    entity_type_violation_rate: 0\n    relation_vocabulary_violation_rate: 0.0003\n    domain_range_violation_rate: 0.2617\n    cross_field_consistency_violation_rate: 0.0007\n    relation_f1: 8.31\n    relation_precision: 7.06\n    relation_recall: 10.12\n    entity_f1: 59.38\n    entity_precision: 58.47\n    entity_recall: 60.32\n    unrecognized_relations: 5\n    f1_method: all_set\n    checker_version: fixed_20260514_v2 (strip + alias + unique_et)\n- exp_id: phase2_docred_full_s1\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    documents_checked: 987\n    parse_failures: 11\n    total_entities: 20187\n    total_triples: 17341\n    entity_type_violation_rate: 0\n    relation_vocabulary_violation_rate: 0.0003\n    domain_range_violation_rate: 0.1021\n    cross_field_consistency_violation_rate: 0.0257\n    entity_f1: 59.37\n    entity_precision: 58.45\n    entity_recall: 59.63\n    relation_f1: 8.23\n    relation_precision: 6.99\n    relation_recall: 10.01\n    unrecognized_relations: 5\n    f1_method: all_set\n    checker_version: fixed_20260514_v2 (strip + alias + unique_et)\n- exp_id: phase2_docred_unconstrained\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    documents_checked: 986\n    parse_failures: 12\n    total_entities: 20171\n    total_triples: 17497\n    entity_type_violation_rate: 0.0248\n    relation_vocabulary_violation_rate: 0.2966\n    domain_range_violation_rate: 0.1846\n    cross_field_consistency_violation_rate: 0.001\n    entity_f1: 58.15\n    entity_precision: 57.26\n    entity_recall: 58.32\n    relation_f1: 7.74\n    relation_precision: 6.55\n    relation_recall: 9.46\n    unrecognized_relations: 5189\n    f1_method: all_set (includes OOV predictions in denominator)\n    checker_version: fixed_20260514_v2 (strip + alias + unique_et)\n    et_v1: 0.0818\n    et_fix_note: v1 triple-counted ET across entity_list + relation head/tail; v2\n      deduplicates by (text, normalized_type)\n- exp_id: phase2_docred_semantic_only\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    documents_checked: 987\n    parse_failures: 11\n    total_entities: 20185\n    total_triples: 17571\n    entity_type_violation_rate: 0.0422\n    relation_vocabulary_violation_rate: 0.2987\n    domain_range_violation_rate: 0.1384\n    cross_field_consistency_violation_rate: 0.0105\n    entity_f1: 57.81\n    entity_precision: 57.27\n    entity_recall: 58.37\n    relation_f1: 7.7\n    relation_precision: 6.54\n    relation_recall: 9.37\n    f1_method: all_set\n    checker_version: fixed_20260514_v2 (strip + alias + unique_et)\n    et_v1: 0.1044\n    et_fix_note: v1 triple-counted ET across entity_list + relation head/tail; v2\n      deduplicates by (text, normalized_type)\n- exp_id: llama_scierc_unconstrained\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    entity_type_violation_rate: 0\n    relation_vocab_violation_rate: 0.0055\n    domain_range_violation_rate: 0.1334\n    cross_field_consistency_violations: 6\n    entity_f1: 0.2356\n    entity_precision: 0.1983\n    entity_recall: 0.2902\n    relation_f1: 0.0268\n    relation_precision: 0.0236\n    relation_recall: 0.031\n    total_entities: 2451\n    total_relations: 1274\n    json_parse_failures: 1\n    samples: 551\n    checker_version: fixed_20260514_v2 (strip + alias + unique_et)\n- exp_id: llama_scierc_full_s1\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    samples: 550\n    entities_extracted: 2469\n    relations_extracted: 1315\n    domain_range_violation_rate: 0.0008\n    relation_vocab_violation_rate: 0\n    entity_type_violation_rate: 0\n    cross_field_consistency_violation_rate: 0.0656\n    total_violation_rate: 0.0431\n    entity_f1: 0.2349\n    entity_precision: 0.1972\n    entity_recall: 0.2902\n    relation_f1: 0.0254\n    relation_precision: 0.0221\n    relation_recall: 0.0298\n    checker_version: fixed_20260514_v2 (strip + alias + unique_et)\n- exp_id: llama_docred_unconstrained\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    checker_version: fixed_20260514_v2\n    f1_method: all_set\n    documents: 998\n    documents_checked: 930\n    parse_failures: 68\n    unique_entities: 11525\n    total_triples: 16437\n    dr_eligible_triples: 13789\n    ET_rate_pct: 0.13\n    RV_rate_pct: 16.03\n    DR_rate_pct: 26.07\n    CF_rate_pct: 0.17\n    entity_precision: 61.22\n    entity_recall: 51.02\n    entity_f1: 55.65\n    relation_precision: 5.22\n    relation_recall: 7\n    relation_f1: 5.98\n    fuzzy_relation_matches: 121\n- exp_id: llama_docred_full_s1\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    checker_version: fixed_20260514_v2 (strip + alias + unique_et)\n    f1_method: all_set\n    violations:\n      ET: 0\n      RV: 0\n      DR: 2.55\n      CF: 12.02\n    f1:\n      entity_f1: 55.01\n      entity_precision: 61.41\n      entity_recall: 49.82\n      relation_f1: 6.27\n      relation_precision: 5.49\n      relation_recall: 7.32\n    counts:\n      documents: 998\n      documents_checked: 907\n      parse_failures: 91\n      unique_entities: 11296\n      triples: 16368\n- exp_id: posthoc_filtering_baseline\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    docred_f1_before: 7.74\n    docred_f1_after: 9.61\n    docred_precision_before: 6.55\n    docred_precision_after: 11.22\n    docred_recall_before: 9.46\n    docred_recall_after: 8.4\n    docred_rejection_rate: 0.481\n    docred_tp_before: 1137\n    docred_tp_after: 1010\n    docred_tp_lost: 127\n    docred_et_residual: 0.0247\n    scierc_f1_before: 8.23\n    scierc_f1_after: 8.63\n    scierc_rejection_rate: 0.168\n    scierc_recall_before: 11.4\n    scierc_recall_after: 10.68\n    scierc_tp_before: 111\n    scierc_tp_after: 104\n- exp_id: llama_docred_unconstrained_mt6144\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ET_rate: 0.13\n    RV_rate: 15.89\n    DR_rate: 26.18\n    DR_rate_eligible: 31.15\n    CF_rate: 0.17\n    entity_precision: 61.19\n    entity_recall: 51.06\n    entity_f1: 55.67\n    relation_precision: 5.18\n    relation_recall: 7\n    relation_f1: 5.95\n    parse_failures: 67\n    documents_checked: 931\n    total_documents: 998\n    unique_entities: 11534\n    total_triples: 16584\n    dr_eligible_triples: 13936\n    fuzzy_relation_matches: 121\n- exp_id: llama_docred_full_s1_mt6144\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    DR_rate_pct: 2.57\n    RV_rate_pct: 0\n    ET_rate_pct: 0\n    CF_rate_pct: 12.13\n    R_F1: 6.25\n    R_precision: 5.45\n    R_recall: 7.32\n    E_F1: 55.04\n    E_precision: 61.41\n    E_recall: 49.87\n    documents_total: 998\n    documents_checked: 908\n    parse_failures: 90\n    triples: 16471\n    unique_entities: 11307\n    fallback_events: 67911\n    wall_clock_seconds: 23926\n    vs_unconstrained_mt6144:\n      DR_delta_pp: -23.61\n      DR_reduction_pct: -90.2\n      R_F1_delta_pp: 0.3\n      E_F1_delta_pp: -0.63\n    vs_full_s1_mt4096:\n      DR_delta_pp: 0.02\n      R_F1_delta_pp: -0.02\n      E_F1_delta_pp: 0.03\n      CF_delta_pp: 0.11\n      parse_fail_delta: -1\n- exp_id: w1_cf_fallback_scierc_pilot\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    ET: 0\n    RV: 0\n    DR: 0.1478\n    CF: 0.0004\n    R_F1: 0.0823\n    R_P: 0.0643\n    R_R: 0.114\n    E_F1: 0.3098\n    E_P: 0.2598\n    E_R: 0.3837\n    entities: 2474\n    relations: 1725\n    samples: 551\n    grammar_first_fallback_rate: 0.3664\n    cf_registry_fallback_rate: 0.0448\n    total_mask_calls: 17024\n    violation_budget_DR_CF: 0.1482\n- exp_id: w1_cf_fallback_docred\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: w1_cf_fallback_llama_scierc\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: w1_cf_fallback_llama_docred\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: w5_lora_scierc_training\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 0.0634\n    eval_loss: 0.0586\n    eval_token_accuracy: 0.9816\n    eval_entropy: 0.9635\n    train_runtime_sec: 688.4\n    epochs: 3\n    checkpoint_path: /root/schema_semantic_constrained_ie/checkpoints/qwen3_8b_lora_scierc\n    merged_model_path: /root/schema_semantic_constrained_ie/checkpoints/qwen3_8b_lora_scierc_merged\n- exp_id: w5_lora_scierc_unconstrained_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    json_parse_rate: 1\n    entity_type_violation_rate: 0\n    relation_vocabulary_violation_rate: 0\n    domain_range_violation_rate: 0.0195\n    cross_field_consistency_violation_rate: 0\n    entity_f1: 0.6705\n    entity_precision: 0.6523\n    entity_recall: 0.6898\n    relation_f1: 0.4386\n    relation_precision: 0.4087\n    relation_recall: 0.4733\n    total_entities: 1784\n    total_relations: 1128\n    domain_range_violations: 22\n    go_nogo_metric: 0.0195\n    dr_gate: FAILED\n- exp_id: w5_lora_scierc_constrained_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    json_parse_rate: 1\n    entity_type_violation_rate: 0\n    relation_vocabulary_violation_rate: 0\n    domain_range_violation_rate: 0\n    cross_field_consistency_violation_rate: 0.0118\n    entity_f1: 0.6705\n    entity_precision: 0.6523\n    entity_recall: 0.6898\n    relation_f1: 0.4377\n    relation_precision: 0.4078\n    relation_recall: 0.4723\n    total_entities: 1784\n    total_relations: 1128\n    total_samples: 551\n    cross_field_consistency_violations: 21\n- exp_id: w5_llama_lora_scierc_training\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    eval_loss: 0.0595\n    eval_mean_token_accuracy: 0.9817\n    eval_entropy: 1.0565\n    train_loss: 0.0501\n    train_runtime_sec: 654.23\n    epochs: 3\n    train_samples_per_second: 8.08\n- exp_id: w5_llama_lora_scierc_unconstrained_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_samples: 551\n    total_entities: 1757\n    total_relations: 1082\n    json_parse_rate: 1\n    entity_type_violation_rate: 0\n    relation_vocabulary_violation_rate: 0\n    domain_range_violation_rate: 0.0111\n    cross_field_consistency_violation_rate: 0\n    total_violation_rate: 0.0042\n    entity_precision: 0.6647\n    entity_recall: 0.691\n    entity_f1: 0.6776\n    relation_precision: 0.432\n    relation_recall: 0.4795\n    relation_f1: 0.4545\n- exp_id: w5_llama_lora_scierc_constrained_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    domain_range_violation_rate: 0.0009\n    relation_vocabulary_violation_rate: 0\n    entity_type_violation_rate: 0\n    cross_field_consistency_violation_rate: 0.0046\n    relation_f1: 0.4547\n    relation_precision: 0.432\n    relation_recall: 0.4795\n    entity_f1: 0.6776\n    entity_precision: 0.6647\n    entity_recall: 0.691\n    total_relations: 1081\n    total_entities: 1757\n    total_samples: 551\n    parse_failures: 0\n- exp_id: w5_qwen_docred_lora_training\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    eval_loss: 0.0614\n    eval_mean_token_accuracy: 0.9804\n    eval_entropy: 0.715\n    train_loss: 0.0682\n    train_runtime_s: 5825.6\n    epochs: 3\n    adapter_path: /root/schema_semantic_constrained_ie/checkpoints/qwen_lora_docred\n    merged_path: /root/autodl-tmp/checkpoints/qwen_lora_docred_merged\n- exp_id: w5_docred_sft_data_gen\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_samples: 3053\n    dev_samples: 998\n    train_entities: 59493\n    train_relations: 38180\n    dev_entities: 19528\n    dev_relations: 12275\n- exp_id: w5_llama_docred_sft_data_gen\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_samples: 3053\n    dev_samples: 998\n    train_size_mb: 19\n    dev_size_mb: 6.1\n- exp_id: w5_llama_docred_lora_training\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 0.0572\n    eval_loss: 0.0624\n    token_acc: 98.06\n- exp_id: w5_llama_docred_lora_unconstrained_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ET_pct: 0\n    RV_pct: 0.15\n    DR_pct: 0.49\n    E_F1: 83.93\n    E_P: 84.93\n    E_R: 82.96\n    R_F1: 43.72\n    R_P: 38.59\n    R_R: 50.41\n    parse_fail_rate: 2.3\n    total_samples: 998\n    total_entities_pred: 19106\n    total_relations_pred: 16171\n- exp_id: w5_llama_docred_lora_constrained_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total: 998\n    parse_failures: 25\n    parse_fail_rate: 2.51\n    entities: 19077\n    relations: 16074\n    entity_f1: 85.23\n    entity_precision: 85.04\n    entity_recall: 85.41\n    relation_f1_all_set: 44.23\n    relation_precision_all_set: 38.82\n    relation_recall_all_set: 51.4\n    et_violations: 0\n    et_violation_rate: 0\n    rv_violations: 0\n    rv_violation_rate: 0\n    dr_violations: 33\n    dr_violation_rate: 0.2\n    cross_field_consistency_violations: 41\n    delta_vs_unconstrained:\n      delta_e_f1: 1.3\n      delta_r_f1: 0.51\n      delta_dr: -0.29\n      delta_rv: -0.15\n      note: Computed as constrained - unconstrained on full-set metrics (not intersection\n        subset). Corrected 2026-05-16 per Reviewer audit.\n- exp_id: w5_qwen_docred_lora_unconstrained_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ET_pct: 0\n    RV_pct: 0.27\n    DR_pct: 0.76\n    CF_pct: 0.12\n    E_F1: 82.15\n    E_P: 85.44\n    E_R: 79.11\n    R_F1: 40.86\n    R_P: 36.41\n    R_R: 46.56\n    parse_fail_rate: 7.11\n    total_samples: 998\n    success_samples: 927\n    fail_samples: 71\n    total_entities_pred: 18091\n    total_relations_pred: 15870\n    ET_pct_excl_fail: 0\n    RV_pct_excl_fail: 0.27\n    DR_pct_excl_fail: 0.76\n    CF_pct_excl_fail: 0.12\n    E_F1_excl_fail: 85.72\n    E_P_excl_fail: 85.44\n    E_R_excl_fail: 86\n    R_F1_excl_fail: 42.2\n    R_P_excl_fail: 36.41\n    R_R_excl_fail: 50.17\n- exp_id: w5_qwen_docred_lora_constrained_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ET_pct: 0\n    RV_pct: 0\n    DR_pct: 0.01\n    CF_pct: 0.41\n    E_F1: 81.43\n    E_P: 85.41\n    E_R: 77.81\n    R_F1: 40.56\n    R_P: 36.35\n    R_R: 45.86\n    parse_fail_rate: 8.52\n    total_samples: 998\n    success_samples: 913\n    fail_samples: 85\n    total_entities_pred: 17799\n    total_relations_pred: 15563\n    E_F1_excl_fail: 85.69\n    R_F1_excl_fail: 42.23\n    delta_vs_unconstrained:\n      delta_DR: -0.75\n      delta_RV: -0.27\n      delta_R_F1: -0.3\n      delta_R_F1_excl_fail: 0.03\n      DR_reduction_pct: 98.7\n      note: 'Constrained - unconstrained. Unconstrained: DR=0.76%, R_F1=40.86, R_F1_excl_fail=42.20'\n- exp_id: w6_mistral_scierc_unconstrained\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    E_P: 0.2402\n    E_R: 0.3156\n    E_F1: 0.2728\n    R_P: 0.0295\n    R_R: 0.0483\n    R_F1: 0.0366\n    ET_pct: 1.5\n    RV_pct: 0\n    DR_pct: 56.94\n    CF_pct: 56.87\n    parse_fail_rate: 0\n    total_samples: 551\n    total_pred_entities: 2202\n    total_pred_relations: 1593\n- exp_id: w6_mistral_scierc_constrained\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    E_P: 0.2437\n    E_R: 0.3144\n    E_F1: 0.2746\n    R_P: 0.0292\n    R_R: 0.0493\n    R_F1: 0.0367\n    ET_pct: 0\n    RV_pct: 0\n    DR_pct: 13.4\n    CF_pct: 1.27\n    CF_count: 21\n    parse_fail_rate: 0\n    total_samples: 551\n    total_pred_entities: 2162\n    total_pred_relations: 1647\n    delta_vs_unconstrained:\n      delta_E_F1: 0.0018\n      delta_R_F1: 0.0001\n      delta_ET: -1.5\n      delta_RV: 0\n      delta_DR: -43.54\n      note: 'Constrained - unconstrained. Baseline: E_F1=0.2728, R_F1=0.0366, DR=56.94%,\n        ET=1.5%, RV=0%'\n- exp_id: w6_mistral_docred_unconstrained\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_samples: 998\n    parse_failures: 7\n    parse_fail_rate: 0.7\n    total_pred_entities: 12580\n    total_pred_relations: 11879\n    ET_pct: 7.58\n    RV_pct: 42.35\n    DR_pct: 57.42\n    CF_pct: 24.78\n    E_P: 0.6221\n    E_R: 0.3975\n    E_F1: 0.4851\n    R_P: 0.0447\n    R_R: 0.0432\n    R_F1: 0.0434\n    f1_method: fuzzy_normalized\n    f1_note: Relation matching uses case-insensitive normalization with token-overlap\n      >80% and edit-distance ≤2 fallback. Strict R_F1=3.50% (delta +0.84pp from 98\n      additional TPs via fuzzy matching of Mistral underscore/abbreviation variants).\n- exp_id: w6_mistral_docred_constrained\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ET_pct: 0\n    RV_pct: 0\n    DR_pct: 33.2\n    CF_pct: 0.19\n    E_P: 65.02\n    E_R: 41.4\n    E_F1: 50.59\n    R_P: 5.67\n    R_R: 5.37\n    R_F1: 5.52\n    parse_fail_rate: 0.8\n    total_samples: 998\n    total_pred_entities: 12535\n    total_pred_relations: 11554\n    delta_vs_unconstrained:\n      ET_pct: -7.58\n      RV_pct: -42.35\n      DR_pct: -24.22\n      CF_pct: -24.59\n      E_F1: 2.08\n      R_F1: 2.02\n- exp_id: w7_qwen_scierc_ft_grammar_only\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ET_pct: 0\n    RV_pct: 0\n    DR_pct: 1.9\n    CF_pct: 0\n    parse_fail_rate: 0\n    total_samples: 551\n    total_entities: 1784\n    total_relations: 1128\n    E_P: 0.6523\n    E_R: 0.6898\n    E_F1: 0.6705\n    R_P: 0.4087\n    R_R: 0.4733\n    R_F1: 0.4386\n    DR_violations: 22\n    tokenizer_warning: false_positive_transformers_4.57.6\n- exp_id: w7_qwen_scierc_ft_semantic_only\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ET_pct: 0\n    RV_pct: 0\n    DR_pct: 0.6\n    CF_count: 15\n    parse_fail_rate: 0\n    total_samples: 551\n    total_entities: 1784\n    total_relations: 1128\n    E_P: 0.6523\n    E_R: 0.6898\n    E_F1: 0.6705\n    R_P: 0.4073\n    R_R: 0.4713\n    R_F1: 0.4369\n    DR_violations: 7\n    delta_vs_grammar_only:\n      DR_delta: -1.3\n      note: semantic_only DR=0.6% vs grammar_only DR=1.9%, semantic layer reduces\n        DR by 68%\n    delta_vs_unconstrained:\n      DR_delta: -1.35\n      note: unconstrained DR=1.95% → semantic_only 0.6%\n- exp_id: w7_llama_scierc_ft_grammar_only\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_samples: 551\n    json_parse_failures: 0\n    total_entities: 1757\n    total_relations: 1082\n    entity_type_violation_rate: 0\n    relation_vocabulary_violation_rate: 0\n    domain_range_violation_rate: 0.0111\n    cross_field_consistency_violation_rate: 0\n    entity_f1:\n      precision: 0.6647\n      recall: 0.691\n      f1: 0.6776\n    relation_f1:\n      precision: 0.432\n      recall: 0.4795\n      f1: 0.4545\n- exp_id: w7_llama_scierc_ft_semantic_only\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ET_pct: 0\n    RV_pct: 0\n    DR_pct: 0.65\n    CF_count: 2\n    E_F1: 67.76\n    E_P: 66.47\n    E_R: 69.1\n    R_F1: 45.47\n    R_P: 43.24\n    R_R: 47.95\n    total_entities: 1757\n    total_relations: 1081\n    json_parse_failures: 0\n- exp_id: w8_ft_posthoc_baseline\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ft_regime:\n      qwen_scierc:\n        R_F1_before: 43.86\n        R_F1_posthoc: 43.94\n        R_F1_constrained: 43.77\n        reject_rate_pct: 1.95\n        TP_lost: 4\n      llama_scierc:\n        R_F1_before: 45.45\n        R_F1_posthoc: 45.23\n        R_F1_constrained: 45.47\n        reject_rate_pct: 1.11\n        TP_lost: 5\n      qwen_docred:\n        R_F1_before: 40.91\n        R_F1_posthoc: 41.11\n        R_F1_constrained: TBD\n        reject_rate_pct: 1.03\n        TP_lost: 1\n      llama_docred:\n        R_F1_before: 43.77\n        R_F1_posthoc: 43.92\n        R_F1_constrained: 44.23\n        reject_rate_pct: 0.64\n        TP_lost: 1\n    zs_regime:\n      mistral_scierc:\n        triples: 1584\n        reject_pct: 20.27\n        R_F1_before: 0.0376\n        R_F1_posthoc: 0.0394\n        R_F1_constrained: 0.0367\n        TP_before: 48\n        TP_after: 44\n        TP_lost: 4\n      qwen_scierc:\n        triples: 1724\n        reject_pct: 16.76\n        R_F1_before: 0.0823\n        R_F1_posthoc: 0.0863\n        R_F1_constrained: 0.0836\n        TP_before: 111\n        TP_after: 104\n        TP_lost: 7\n      llama_scierc:\n        triples: 1274\n        reject_pct: 13.89\n        R_F1_before: 0.0268\n        R_F1_posthoc: 0.0271\n        R_F1_constrained: 0.0254\n        TP_before: 30\n        TP_after: 28\n        TP_lost: 2\n      qwen_docred:\n        triples: 17497\n        reject_pct: 48.12\n        R_F1_before: 0.0774\n        R_F1_posthoc: 0.0961\n        R_F1_constrained: 0.0823\n        TP_before: 1137\n        TP_after: 1010\n        TP_lost: 127\n      llama_docred:\n        triples: 16437\n        reject_pct: 42.18\n        R_F1_before: 0.0598\n        R_F1_posthoc: 0.0744\n        R_F1_constrained: 0.0627\n        TP_before: 850\n        TP_after: 802\n        TP_lost: 48\n      mistral_docred:\n        triples: 11836\n        reject_pct: 73.73\n        R_F1_before: 0.0434\n        R_F1_posthoc: 0.0385\n        R_F1_constrained: 0.0552\n        TP_before: 518\n        TP_after: 292\n        TP_lost: 226\n        removed_RV: 4172\n        removed_ET: 3382\n        removed_DR: 1173\n        note: Only ZS case where posthoc HURTS R_F1 — 73.7% rejection rate loses 43.6%\n          of TPs\n    key_finding: 'ZS: post-hoc R_F1 >= constrained R_F1 in 5/6 groups. Exception:\n      Mistral DocRED where extreme rejection rate (73.7%) causes net F1 loss. Constrained\n      decoding value is in structural guarantee (0% violations) and composability,\n      not F1 preservation.'\n- exp_id: w8_llama_docred_ft_grammar_only\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    E_F1: 84.04\n    R_F1: 43.77\n    entity_precision: 84.99\n    entity_recall: 83.11\n    relation_precision: 38.6\n    relation_recall: 50.53\n    ET_pct: 0\n    RV_pct: 0\n    DR_pct: 0.51\n    CF_pct: 0.12\n    parse_fail_rate: 2.3\n    total_samples: 998\n    total_relations: 16199\n    unique_entities: 13225\n    parse_failures: 23\n- exp_id: w8_qwen_docred_ft_grammar_only\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    E_F1: 82.19\n    E_P: 85.47\n    E_R: 79.16\n    R_F1: 40.85\n    R_P: 36.27\n    R_R: 46.77\n    ET_pct: 0\n    RV_pct: 0\n    DR_pct: 0.61\n    CF_pct: 0.11\n    parse_fail_rate: 7.01\n    total_samples: 998\n    parse_failures: 70\n- exp_id: w8_qwen_docred_ft_semantic_only\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    E_F1: 82.15\n    E_P: 85.58\n    E_R: 78.99\n    R_F1: 40.89\n    R_P: 36.35\n    R_R: 46.73\n    ET_pct: 0\n    RV_pct: 0.23\n    DR_pct: 0.21\n    CF_pct: 0.27\n    parse_fail_rate: 7.52\n    total_samples: 998\n    parse_failures: 75\n    documents_checked: 923\n    total_entities: 18025\n    total_triples: 15909\n    DR_violations: 34\n    RV_violations: 37\n    ET_violations: 0\n    CF_violations: 49\n- exp_id: w8_llama_docred_ft_semantic_only\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    E_F1: 84.02\n    E_P: 85.01\n    E_R: 83.06\n    R_F1: 43.9\n    R_P: 38.89\n    R_R: 50.4\n    ET_pct: 0\n    RV_pct: 0.15\n    DR_pct: 0.3\n    CF_pct: 0.16\n    parse_fail_rate: 2.4\n    total_samples: 998\n    parse_failures: 24\n    documents_checked: 974\n    total_entities: 19099\n    total_relations: 16038\n    DR_violations: 48\n    RV_violations: 24\n    ET_violations: 0\n    CF_violations: 31\n- exp_id: w9_qwen_scierc_zs_sampling\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ET_pct: 0\n    RV_pct: 0\n    DR_pct: 0.75\n    CF_pct: 9.9\n    E_F1: 31.28\n    R_F1: 7.42\n    parse_fail_rate: 0\n    total_samples: 551\n    note: 'F1 computed by v2 checker; greedy baseline with same checker: E_F1=30.98,\n      R_F1=8.36'\n- exp_id: w9_qwen_docred_zs_sampling\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: w9_qwen_docred_zs_sampling_r2\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: beam_search_scierc_full_551\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ET_pct: 0\n    RV_pct: 0\n    DR_pct: 0\n    CF_pct: 0.53\n    E_F1: 32\n    R_F1: 8.56\n    E_P: 26.83\n    E_R: 39.63\n    R_P: 6.69\n    R_R: 11.91\n    parse_fail_rate: 0\n    total_entities: 2476\n    total_relations: 1737\n- exp_id: w9_qwen_scierc_stability_3seeds\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    seed_123:\n      ET_pct: 0\n      RV_pct: 0\n      DR_pct: 0.93\n      CF_pct: 9.9\n      E_F1: 30.98\n      R_F1: 8.36\n    seed_456:\n      ET_pct: 0\n      RV_pct: 0\n      DR_pct: 0.93\n      CF_pct: 9.9\n      E_F1: 30.98\n      R_F1: 8.36\n    seed_789:\n      ET_pct: 0\n      RV_pct: 0\n      DR_pct: 0.93\n      CF_pct: 9.9\n      E_F1: 30.98\n      R_F1: 8.36\n    cross_seed_DR_std: 0\n    cross_seed_DR_range: 0\n    conclusion_note: Greedy decoding is fully deterministic - seed has no effect on\n      output. All metrics identical across 3 seeds.\n- exp_id: w9_llama_scierc_beam_551\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ET_pct: 0\n    RV_pct: 0\n    DR_pct: 0\n    CF_pct: 0.93\n    CF_count: 15\n    E_F1: 25.04\n    E_P: 21.27\n    E_R: 30.42\n    R_F1: 3.33\n    R_P: 2.68\n    R_R: 4.41\n    total_entities: 2398\n    total_relations: 1606\n    parse_fail_rate: 0\n    total_samples: 551\n    vs_greedy_full_s1:\n      DR_delta: -0.08\n      CF_delta: -5.63\n      E_F1_delta: 1.55\n      R_F1_delta: 0.79\n      note: 'Greedy: DR=0.08%, CF=6.56%, E_F1=23.49%, R_F1=2.54%'\n- exp_id: w9_qwen_docred_beam_50\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ET_pct: 0\n    RV_pct: 0\n    DR_pct: 0\n    CF_pct: 0.55\n    E_F1: 58.64\n    R_F1: 9.37\n    total_samples: 50\n    parse_failures: 3\n    parse_fail_rate: 6\n    vs_greedy_full_s1:\n      DR_delta: -10.21\n      CF_delta: -2.02\n      E_F1_delta: -0.73\n      R_F1_delta: 1.14\n      note: 'Greedy full_s1 998 docs: DR=10.21%, CF=2.57%, E_F1=59.37, R_F1=8.23.\n        Beam eliminates ALL DR on DocRED 96-type schema.'\n- exp_id: w10_type_consensus_prototype\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    ET_pct: 0\n    RV_pct: 0\n    DR_pct: 0.93\n    CF_pct: 9.9\n    E_F1: 30.98\n    R_F1: 8.36\n    gtc_skip_total: 672\n    gtc_skip_unique_entities: 258\n    gtc_effective_corrections: 0\n    delta_DR: 0\n    delta_CF: 0\n- exp_id: w10_type_consensus_docred_50\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    ET_pct: 0\n    RV_pct: 0\n    DR_pct: 8.69\n    CF_pct: 2.4\n    E_F1: 59.08\n    R_F1: 8.33\n    gtc_skip_total: 601\n    gtc_skip_unique_entities: 213\n    gtc_effective_corrections: 0\n    delta_DR: 0\n    delta_CF: 0\n- exp_id: w10_llama_docred_beam_50\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ET_pct: 0\n    RV_pct: 0\n    DR_pct: 0\n    CF_pct: 0.94\n    E_F1: 55.62\n    R_F1: 9.47\n    parse_failures: 3\n    parse_fail_rate: 6\n    total_samples: 50\n    vs_greedy_full_s1:\n      DR_delta: -2.57\n      CF_delta: -11.19\n      E_F1_delta: 0.61\n      R_F1_delta: 3.2\n      note: 'Greedy baseline: DR=2.57%, CF=12.13%, E_F1=55.01, R_F1=6.27'\n    checker_note: Must use violation_checker_docred.py for DocRED (not violation_checker.py)\n- exp_id: w10_mistral_scierc_beam_551\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    total_samples: 551\n    parse_failures: 1\n    parse_rate: 0.9982\n    ET_pct: 0\n    RV_pct: 0\n    DR_pct: 13.79\n    CF_pct: 0.57\n    E_P: 23.04\n    E_R: 31.64\n    E_F1: 26.66\n    R_P: 3.13\n    R_R: 7.22\n    R_F1: 4.37\n    total_entities: 2294\n    total_triples: 2241\n    vs_greedy:\n      baseline: w6_mistral_scierc_constrained\n      greedy_DR: 13.4\n      greedy_CF: 1.27\n      greedy_E_F1: 27.46\n      greedy_R_F1: 3.67\n      delta_DR: +0.39pp\n      delta_CF: -0.70pp\n      delta_E_F1: -0.80pp\n      delta_R_F1: +0.70pp\n- exp_id: w10_beam_ablation_k2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ET_pct: 0\n    RV_pct: 0\n    DR_pct: 0.35\n    CF_count: 71\n    CF_pct: 4.12\n    E_F1: 31.54\n    R_F1: 8.75\n    parse_failures: 0\n    total_samples: 551\n    total_triples: 1724\n    vs_greedy:\n      DR_delta: -0.58\n      CF_delta: -5.78\n      E_F1_delta: 0.56\n      R_F1_delta: 0.39\n      note: 'Greedy: DR=0.93%, CF=9.90%, E_F1=30.98, R_F1=8.36'\n    vs_beam_k4:\n      DR_delta: 0.35\n      CF_delta: 3.59\n      E_F1_delta: -0.46\n      R_F1_delta: 0.19\n      note: 'k=4: DR=0%, CF=0.53%, E_F1=32.00, R_F1=8.56'\n- exp_id: w10_beam_ablation_k8\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ET_pct: 0\n    RV_pct: 0\n    DR_pct: 0\n    CF_pct: 0.08\n    CF_count: 2\n    E_F1: 32.18\n    R_F1: 8.39\n    E_P: 26.95\n    E_R: 39.93\n    R_P: 6.54\n    R_R: 11.7\n    parse_failures: 0\n    total_samples: 551\n    total_triples: 1744\n    total_entities: 2483\n    vs_greedy:\n      DR_delta: -0.93\n      CF_delta: -9.82\n      E_F1_delta: 1.2\n      R_F1_delta: 0.03\n    vs_beam_k4:\n      DR_delta: 0\n      CF_delta: -0.45\n      E_F1_delta: 0.18\n      R_F1_delta: -0.17\n- exp_id: w9_mistral_docred_beam_50\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ET_violation_rate: 0\n    RV_violation_rate: 0\n    DR_violation_rate: 21.37\n    CF_violations: 1\n    total_triples: 524\n    total_entities: 597\n    docs_checked: 49\n    parse_failures: 1\n    E_F1: 51.78\n    E_P: 65.2\n    E_R: 42.94\n    R_F1: 5.7\n    R_P: 6.49\n    R_R: 5.08\n    R_tp: 34\n    R_gold: 669\n    R_pred: 524\n- exp_id: w10_qwen_scierc_ft_beam_4\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    DR: 0\n    CF: 0\n    total_violation_rate: 0\n    entity_type_violation_rate: 0\n    relation_vocab_violation_rate: 0\n    domain_range_violation_rate: 0\n    cross_field_consistency_violation_rate: 0\n    E_F1: 66.88\n    E_P: 64.69\n    E_R: 69.22\n    R_F1: 44.23\n    R_P: 39.41\n    R_R: 50.41\n    total_samples: 551\n    json_parse_failures: 0\n    total_entities: 1802\n    total_relations: 1246\n    vs_ft_greedy:\n      baseline: w5_lora_scierc_constrained_eval\n      DR_delta: 0% → 0% (same)\n      CF_delta: 1.18% → 0.0% (eliminated all violations)\n      E_F1_delta: 67.05 → 66.88 (-0.17, negligible)\n      R_F1_delta: 43.77 → 44.23 (+0.46, slight improvement)\n    vs_zs_beam_k4:\n      DR_delta: 0% → 0% (same)\n      CF_delta: 0.53% → 0.0% (eliminated)\n      E_F1_delta: 32.00 → 66.88 (+34.88)\n      R_F1_delta: 8.56 → 44.23 (+35.67)\n- exp_id: r4_prompt_minimal\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    unconstrained:\n      ET_pct: 0.58\n      RV_pct: 1.16\n      DR_pct: 16.91\n      E_F1: 31.98\n      R_F1: 7.91\n    constrained:\n      ET_pct: 0\n      RV_pct: 0\n      DR_pct: 0.92\n      E_F1: 31.99\n      R_F1: 7.85\n    DR_reduction_pct: 94.6\n    delta_R_F1_pp: -0.06\n    delta_E_F1_pp: 0.01\n- exp_id: r4_prompt_detailed\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    unconstrained:\n      ET_pct: 0.22\n      RV_pct: 0.45\n      DR_pct: 11.07\n      E_F1: 33.55\n      R_F1: 10.48\n    constrained:\n      ET_pct: 0\n      RV_pct: 0\n      DR_pct: 0.64\n      E_F1: 33.56\n      R_F1: 10.48\n    DR_reduction_pct: 94.2\n    delta_R_F1_pp: 0\n    delta_E_F1_pp: 0.01\n- exp_id: ee_qwen_wikievents_unconstrained\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    parse_success: 218/246 (88.6%)\n    ET: 0\n    EV: 24\n    RoV: 74.9\n    AC: 0.3\n    CF: 0\n    trigger_f1: 0.1184\n    argument_f1: 0.0009\n    entity_f1: 0\n- exp_id: ee_llama_wikievents_unconstrained\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    parse_success: 226/246 (91.9%)\n    ET: 0\n    EV: 10.5\n    RoV: 88.8\n    AC: 0.1\n    CF: 0\n    trigger_f1: 0.0572\n    argument_f1: 0\n    entity_f1: 0\n- exp_id: ee_qwen_wikievents_constrained\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    parse_success: 206/246 (83.7%)\n    ET: 0\n    EV: 0\n    RoV: 0.3\n    AC: 2.1\n    CF: 21.1\n    trigger_f1: 0.1339\n    argument_f1: 0.0168\n    entity_f1: 0.1409\n    parse_failures: 40\n    go_no_go: 2.4\n    note: after retry with max_new_tokens=8192\n- exp_id: ee_llama_wikievents_constrained\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    parse_success: 215/246 (87.4%)\n    ET: 0\n    EV: 0\n    RoV: 0\n    AC: 3.4\n    CF: 15.5\n    trigger_f1: 0.078\n    argument_f1: 0.011\n    entity_f1: 0.178\n    parse_failures: 31\n    go_no_go: 3.4\n    note: after retry with max_new_tokens=8192\n- exp_id: ee_mistral_wikievents_unconstrained\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    parse_success: 194/246 (78.9%)\n    ET: 0\n    EV: 37.3\n    RoV: 63.9\n    AC: 0\n    CF: 0\n    trigger_f1: 0.0241\n    argument_f1: 0\n    entity_f1: 0\n- exp_id: ee_mistral_wikievents_constrained\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    parse_success: 184/246 (74.8%)\n    ET: 0\n    EV: 0\n    RoV: 54.8\n    AC: 19.2\n    CF: 0.7\n    note: grammar_only baseline (old code without semantic mask fix)\n- exp_id: ee_mistral_wikievents_constrained_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    parse_success: 178/246 (72.4%)\n    ET: 0\n    EV: 0\n    RoV: 0.1\n    AC: 16.6\n    CF: 13.9\n    trigger_f1: 0.0508\n    argument_f1: 0.0047\n    entity_f1: 0.1245\n    parse_failures: 68\n    go_no_go: 16.7\n- exp_id: ee_qwen_wikievents_constrained_v3\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    parse_success: 206/246 (83.7%)\n    parse_failures: 40\n    ET: 0\n    EV: 0\n    RoV: 0\n    AC: 2.1\n    CF: 21.1\n    go_no_go: 2.05\n    entity_f1: 0.1409\n    trigger_f1: 0.1339\n    argument_f1: 0.0168\n    code_version: 938-line (collision+exact-match fix)\n    posthoc_args_removed: 109\n    posthoc_arg_f1: 0.017\n    cf_voting_fix_rate: 15.9%\n    cf_voting_entity_f1: 0.1352\n- exp_id: ee_llama_wikievents_constrained_v3\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    parse_success: 207/246 (84.1%)\n    parse_failures: 39\n    ET: 0\n    EV: 0\n    RoV: 0\n    AC: 3.8\n    CF: 17.2\n    go_no_go: 3.8\n    entity_f1: 0.1763\n    trigger_f1: 0.0748\n    argument_f1: 0.0118\n    code_version: 938-line (collision+exact-match fix)\n    posthoc_args_removed: 173\n    posthoc_arg_f1: 0.0118\n- exp_id: ee_mistral_wikievents_constrained_v3\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    parse_success: 218/246 (88.6%)\n    parse_failures: 28\n    ET: 0\n    EV: 0\n    RoV: 0\n    AC: 1.3\n    CF: 14.9\n    go_no_go: 1.26\n    entity_f1: 0.1171\n    trigger_f1: 0.0387\n    argument_f1: 0.0031\n    code_version: 938-line (collision+exact-match fix)\n    posthoc_args_removed: 86\n    posthoc_ac_after: 0\n- exp_id: ee_mistral_wikievents_grammar_only_v3\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    parse_success: 218/246 (88.6%)\n    parse_failures: 28\n    ET: 0\n    EV: 0\n    RoV: 64\n    AC: 13.8\n    CF: 1.1\n    go_no_go: 77.73\n    entity_f1: 0.1192\n    trigger_f1: 0.0337\n    argument_f1: 0.0027\n    code_version: 938-line (collision+exact-match fix)\n    mode: grammar_only\n- exp_id: 70b_scierc_unconstrained\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ET_pct: 0\n    RV_pct: 0.6\n    DR_pct: 6.5\n    CF_count: 0\n    CF_pct: 0\n    E_F1: 0.3517\n    E_P: 0.3009\n    E_R: 0.4232\n    R_F1: 0.1122\n    R_P: 0.0929\n    R_R: 0.1417\n    total_entities: 2353\n    total_relations: 1485\n    parse_failures: 0\n    samples: 551\n- exp_id: 70b_scierc_constrained\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ET_pct: 0\n    RV_pct: 0\n    DR_pct: 0\n    CF_count: 86\n    CF_pct: 3.66\n    E_F1: 0.3514\n    E_P: 0.3007\n    E_R: 0.4226\n    R_F1: 0.1124\n    R_P: 0.0932\n    R_R: 0.1417\n    total_entities: 2351\n    total_relations: 1481\n    parse_failures: 0\n    samples: 551\n- exp_id: 70b_docred_unconstrained\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n- exp_id: 70b_docred_constrained\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n- exp_id: q1_llama_lora_scierc_beam4\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ET_violation_rate: 0\n    RV_violation_rate: 0\n    DR_violation_rate: 0\n    CF_violation_rate: 0\n    entity_f1: 67.94\n    relation_f1: 46.11\n    samples: 551\n    total_entities: 1853\n    total_relations: 727\n- exp_id: p8_latency_overhead\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    samples: 551\n    unconstrained_mean_s: 4.163\n    unconstrained_median_s: 4.106\n    unconstrained_total_s: 2293.7\n    constrained_mean_s: 4.71\n    constrained_median_s: 4.644\n    constrained_total_s: 2595\n    overhead_ratio_mean: 1.131\n    overhead_ratio_median: 1.131\n    overhead_ratio_p95_perdoc: 1.262\n    overhead_pct: 13.1\n- exp_id: p8b_docred_latency\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: best\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-18T16:20:00.251Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-18T16:20:00.251Z",
  "sessionId": "91d3e0f3-a355-4901-81d3-cef73f6dac5a"
}
```

---

## Round 1

16 recorded events

### User

_source line 3 · 2026-05-18T16:20:00.278Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：

含义：所有 pending 实验确认核心假设；论文叙事成功传达 non-obvious insights；审稿人认为 violation landscape + enabling dependency + cross-task generalization 三者构成完整且新颖的贡献
核心假设：['70B DocRED DR baseline ≥15%，证明 scale 不能消除 ontology violations', '70B DocRED OntoCoDec DR reduction ≥80%，F1 neutral-to-positive', 'WikiEvents cross-task story 被接受为 generality 证据（mechanism generalization，非 SOTA performance）', 'Enabling dependency (grammar enables semantic) 被至少 2/3 审稿人识别为 non-trivial architectural insight', 'Tightness × RV baseline dual-factor 和 post-hoc EE 99.6% rejection 被视为 surprising findings', 'CF tradeoff 的 proactive disclosure + root cause analysis + type ambiguity 证据被接受为 honest limitation']
关键指标范围：{'70b_docred_dr_baseline_pct': [15, 25], '70b_docred_dr_constrained_pct': [1, 5], '70b_docred_dr_reduction_pct': [80, 95], '70b_docred_rf1_delta_pp': [-0.3, 0.5], 'avg_reviewer_score': [3.75, 4.25], 'novelty_score_avg': [3.5, 4.0], 'soundness_score_avg': [4.0, 4.5], 'reviewers_seeing_novelty_ratio': [0.67, 1.0], 'rebuttal_needed': False}
叙事方向：原始 framing 完全成立："universal ontology-constrained structured generation framework"。 三条 evidence lines 完整落地：(1) 70B 仍有 15%+ violations → scale 不是解法， (2) EE cross-task RoV→0% + post-hoc 99.6% rejection → 框架必要性， (3) 4 models × 3 datasets × 2 tasks → 充分泛化性。 Claims 无需降级。§1 intro 以 "even 70B models violate at double-digit rates" 开篇， §5.4 WikiEvents 作为 generality 的 crown jewel， §5.5 tightness × RV interaction 作为 analytical insight 独立贡献。 CF 在 §7 limitations 清晰定位为 "local enforcement inherent tradeoff, not method defect"。


基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。
每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。

# Project context
project: schema_semantic_constrained_ie
focus: 目标 4.0 Conference Accept。当前 3.5 的瓶颈是 "novelty incremental, core conclusion 直觉上显然"。请重点审查：(1) 论文 story 是否让审稿人感到 "有我没想到的东西"；(2) 哪些非显然发现（70B 仍有违规、post-hoc EE 99.6% 删除、enabling dependency、non-rectangularity）的呈现是否足够突出；(3) 实验覆盖面是否有盲点（3 models × 3 datasets × ablation + 70B + beam + sampling + latency）；(4) 从 3.5 到 4.0 的具体可操作建议。

## paper_framing.md

# OntoCoDec — Paper Framing

## Target Venue
EMNLP 2026 (ARR submission May 25, 2026) — **目标: conference main**（D040, 用户明确指示）

## Title
OntoCoDec: Type-Valid Information Extraction via Compiled Ontology Constraints
(D015: "Near-Complete" dropped — DocRED residual DR=10.21% (Qwen) 不算 near-complete。论文贡献是方法，不是特定消除率。SciERC 0.93% 和 DocRED 2.55% (Llama) 可在正文中描述为 near-complete，但 title 不宜 overclaim。)

**D040 Story 升级方向**: 从 "IE-specific constrained decoding" → "universal ontology-constrained structured generation framework"。WikiEvents Event Extraction 验证跨任务泛化。Continuation masking v2 突破（10-doc: RoV 0%, semantic violations ↓95.8%）初步确认跨任务有效性，全量实验进行中。最终 title 待全量结果后调整。

## Core Insight
LLM-based IE systems produce systematic ontology constraint violations concentrated in specific relation types. Prompt-level intervention (schema-informed prompting) reduces violations by ~62% but cannot eliminate them — certain relation types retain 25-30% violation rates even with explicit constraint descriptions. OntoCoDec provides **near-complete elimination (DR 15.4%→0.93%, ↓94%) at zero or positive F1 impact** through automatic ontology-to-decoder constraint compilation with two complementary layers.

**Phase 2 confirmed (D012 bootstrap CI, v2 fix)**: Grammar+Semantic dual-layer constrained decoding reduces domain/range violations by 94%, eliminates entity-type and relation-vocabulary violations entirely (→0%). F1 impact is **dataset-dependent**:
- SciERC: Rel F1 neutral (+0.13pp, p=0.58), Ent F1 neutral (-0.03pp, p=0.53)
- DocRED: Rel F1 **significantly improved** (+0.50pp, p<0.001, 95% CI [+0.23, +0.81]); Ent F1 **significantly improved** (+1.23pp, p<0.001, 95% CI [+0.94, +1.55])
- Mechanism: grammar 消除 OOV relation names (DocRED RV 29.66%→0.03%) + 非标 entity types (ET 2.48%→0%)。all_set F1 方法下 OOV=FP → fewer FP → higher precision/F1。SciERC baseline RV/ET 已很低，效果不显著。
- **Grammar 层是 F1 提升的唯一来源**: grammar_only Ent F1=59.38% ≈ full_s1 59.37% (Δ+0.01pp, p=0.66)。Semantic 层对 F1 无额外贡献，专注 DR reduction。

## Core Claims

### Claim 1 (Empirical): Violation Landscape
LLM-based IE systems violate ontology type constraints at non-trivial rates (15.4% per-triple on SciERC, 18.7% on DocRED). Violations are **not uniformly distributed** — they concentrate on relation types with tight domain/range constraints (Feature-of 33.5%, Compare 42.4%) while loose-constraint relations show near-zero violation (Used-for 0.8%).

**Key insight**: Violation rate is driven by **constraint tightness**, not ontology size. A small ontology with tight constraints can produce more violations than a large ontology with loose constraints.

**D014 修订**: DR reduction ceiling 由 **tightness × model RV baseline** 共同决定，非 tightness 单因素。Llama DocRED DR↓90.2% vs Qwen DR↓44.7%（同一 ontology τ̄=0.842）。机制：Qwen RV=29.66% >> Llama RV=16.03% → grammar 层将 OOV triples 强制匹配有效关系名 → 揭露大量 latent DR violations → 残余 DR 更高。这是比单一 tightness 更深的 insight。

**Evidence**: SciERC (7 relations) 15.4%; DocRED (96 relations) 18.7% — comparable rates despite 14× ontology size difference. Schema-informed prompt on DocRED only achieves DR↓32% (vs SciERC ↓62%), confirming **prompt-level intervention scales poorly with ontology complexity**.

### Claim 2 (Empirical): Prompt Insufficiency
Schema-informed prompting (explicitly describing domain/range constraints in the prompt) reduces but does not eliminate violations:
- Overall: 15.4% → 5.78% (-62.4%), still above 5%
- Per-relation: Compare 42.4% → 27.6%, Evaluate-for 24.1% → 29.9% (**worse**)
- Prompt intervention is unreliable at the per-relation level — some relations improve, one regresses

**Narrative**: This is NOT about "5.78% barely above 5%". The story is: **prompt-level intervention is fundamentally unreliable as a guarantee mechanism**. It works statistically but cannot provide per-instance compliance. Three specific relation types retain >10% violation rates with schema-informed prompts. For safety-critical IE (biomedical, legal, regulatory), statistical reduction is insufficient — guaranteed compliance is required.

### Claim 3 (Methodological): Composable Constraint Framework
OntoCoDec automatically compiles IE ontology schemas into two composable constraint layers:
1. **Grammar layer** (XGrammar): JSON structure + type vocabulary constraints (CFG-expressible)
2. **Semantic layer** (TypeConstraintProcessor): Cross-field domain/range constraints via stateful entity registry + dynamic logit masking

The two layers are **complementary with enabling dependency**: grammar ensures every generated relation type is in the valid vocabulary, which enables the semantic layer to look up and enforce domain/range rules for that type. Without grammar, the semantic layer encounters unknown relation types and cannot enforce constraints (explaining why semantic_only achieves only ↓24% vs full_s1 ↓94%). This is NOT "synergistic" (mutual amplification) — grammar is a prerequisite for semantic, not vice versa.

The two layers compose via bitwise AND of token masks. Recommended framing: "Grammar and semantic constraints compose via bitwise AND with an enabling dependency: grammar ensures structural validity, enabling semantic constraints to enforce domain/range rules. When constraint tightness creates empty intersection between layers, the system degrades gracefully to grammar-only constraints, maintaining structural validity as a guaranteed floor."

**Graceful degradation + Fallback 频率量化** (D008 + Reviewer 发现):
When $M_{semantic} \cap M_{grammar} = \emptyset$, the system falls back to grammar-only control.

**关键量化数据（Reviewer 从日志挖掘）**:
- Llama DocRED full_s1: **32,921 次 fallback / 577 docs = ~57 次/doc**
- Llama SciERC full_s1: **5,882 次 fallback / 550 docs = ~10.7 次/doc**
- DocRED fallback 频率是 SciERC 的 **5.3×**
- Qwen DocRED fallback 率未知（日志当时无 fallback logging，需估算）

**这直接解释了 DocRED DR 残余 10.19% vs SciERC 0.93%**: 更多 token 位置退化为 grammar-only → grammar-only 的 DR 已知为 26.17% → 高 fallback = 高残余 DR。

**论文建议**: 在 §5 tightness 段报告 fallback 率，定义 "Constraint Coverage" 指标（semantic masking 实际生效的 token 比例）。这把 "10.19% DR 残余" 从弱点变成可量化分析的 finding。Frame as "engineering robustness" in §4; fallback 频率 + tightness 作为 §5 定量分析。

**Decidability taxonomy**: Constraints classified by prefix-decidability:
- (a) Purely local: entity type ∈ vocabulary (grammar layer)
- (b) Prefix-decidable with state: relation argument types compatible with domain/range (semantic layer, requires entity registry)
- (c) Truly non-local: forward coreference — out of scope for forward-only decoding

### Claim 4 (Methodological): S1 vs S2 Decoding Strategies — Architectural Ablation
- S1 (single-pass): Both layers applied throughout generation. **Recommended primary strategy** — simpler, slightly better metrics across the board.
- S2 (two-pass): Pass 1 extracts entities (grammar-only), Pass 2 generates relations with input-dependent grammar compiled from Pass 1 entities.

**S2 full results (551/551 SciERC)**: DR 0.97% (vs S1 0.93%), CF 8.03% (vs S1 9.9%), R-F1 8.03% (vs S1 8.36%). S2 does NOT solve CF — the 1.87pp reduction is not significant. S2 also slightly worse on DR and F1. **S2 is an architectural variant demonstrating framework flexibility, not a CF solution.** Position in paper as ablation (Section 5 or Appendix), not as a core contribution.

⚠️ **Do NOT cite pilot50 DR=0% as S2 evidence** — small-sample artifact; full run shows DR=0.97%. Per-relation S2 DR is worse than S1 on Compare (4.6% vs 2.82%), Part-of (1.25% vs 0%), Used-for (0.12% vs 0%).

### Claim 5 (Empirical): Cross-Task Generalization — Event Extraction (D040, NEW)
**Status**: ✅ All 3 models × 246 docs complete (v3 with collision fix + exact-match fix)

OntoCoDec generalizes beyond Relation Extraction to **Event Extraction** (WikiEvents, Li et al. NAACL 2021), demonstrating that the framework is task-agnostic for any IE task with ontology-defined type constraints.

**Cross-task framing (Reviewer 评估 confirmed)**:
- **RoV 是 DR 的正确对应物**（不是 RV）：EE 中 per-type violation rate 是 RE 的 3-5×，支持 "more complex ontology → more critical constraint enforcement" claim
- **三层级联 Grammar→RoV→AC**（比 RE 的 Grammar→DR 两层更丰富）：grammar 消除 EV，使 semantic layer 可以 enforce role restriction (RoV→0%)，进而暴露 AC violations。这强化 architecture contribution 论证。
- **Semantic layer 是 EE 的唯一防线**：grammar 层对 role vocabulary 无能力，只有 semantic layer + continuation masking 能 enforce per-event-type role constraints
- **"Practical value" 防线**：Arg F1 ≈ 0% 不削弱 claim，因为 (a) mechanism generalization 是 contribution 不是 SOTA performance，(b) FT composability 已在 RE 中证明 high-F1 场景有效

**WikiEvents specifics** (DARPA KAIROS ontology):
- 56 event types × 80 argument roles × 27 entity types（含 5 个补充 Contact 子类型 + CRM entity type）
- 245 组显式 (event_type, role) → allowed_entity_types 约束
- Maps directly to OntoCoDec's semantic layer: argument role type constraints ≡ domain/range constraints
- 27 entity types（比 ACE05 的 7 个更丰富）→ constraint space 更大，更能展示 semantic layer 价值
- 99.98% 数据满足约束 → 约束定义是真实有效的
- Hierarchical event names (e.g., Conflict.Attack.DetonateExplode) → 扁平化为 leaf-node 解决 first-token collision（96.1%→3.9%）

**数据集选择理由**（MAVEN/RAMS 排除）：
- MAVEN (168 types): 无 argument extraction，不适用
- MAVEN-Arg (162 types): FrameNet-based，无 role→entity_type schema 约束
- RAMS (139 types): 仅 cardinality 约束，无 entity type binding
- ACE05 (33 types): LDC 付费，采购周期来不及
- **WikiEvents 是唯一同时满足 "免费 + 有显式 role→entity_type 约束" 的数据集**

**Violation 分类** (5 类，从 RE 的 4 类扩展):
- ET (Entity Type): entity type 不在 ontology 合法类型列表中
- EV (Event Vocabulary): event type 不在 ontology 定义中
- RoV (Role Vocabulary): argument role 不在该 event type 定义中
- AC (Argument Constraint): argument entity type 不满足 role→entity_type 约束（DR 的自然推广）
- CF (Cross-Field): 同一 entity 跨 event 被赋予不同 type

**Full results (246 docs, v3 final — collision fix + exact-match fix)**:

| Metric | Qwen3-8B uncon. | Qwen3-8B Full S1 | Llama-3.1-8B uncon. | Llama-3.1-8B Full S1 | Mistral-7B uncon. | Mistral-7B Full S1 |
|--------|-----------------|-------------------|---------------------|----------------------|-------------------|---------------------|
| Parse | 88.6% | 83.7% | 91.9% | 84.1% | 88.6% | 88.6% |
| EV | 24.0% | **0%** | 10.5% | **0%** | 37.3% | **0%** |
| RoV | 74.9% | **0%** | 88.8% | **0%** | 63.9% | **0%** |
| AC | 0.3% | 2.1% | 0.1% | 3.8% | 0% | 1.3% |
| CF | 0% | 21.1% | 0% | 17.2% | 0% | 14.9% |
| Trigger F1 | 11.8% | 13.4% | 5.7% | 7.5% | 2.4% | 3.9% |
| Ent F1 | 0% | 14.1% | 0% | 17.6% | 0% | 11.7% |

**Grammar-only ablation (Mistral v3, all 3 models)**:
- Grammar eliminates EV→0% but RoV remains 64-77%: grammar CFG cannot constrain 80 argument roles conditioned on event context
- AC rises to 8-14% under grammar-only (latent violation surfacing pattern, same as DocRED RE)
- Proves semantic layer is essential for EE: two-layer architecture is necessary, not just convenient

**Post-hoc filtering comparison (devastating)**:
- Qwen: 5,467→23 arguments (99.6% discarded) to reach 0% violation
- Llama: 5,053→3 arguments (99.9% discarded)
- Mistral: 6,034→0 arguments (100% discarded)
- Post-hoc is not viable for EE (contrasts with RE where it's expensive but functional)

**BPE collision diagnostic (confirmed 2026-05-18)**:
- Qwen (BPE, ~152K vocab): **0 collision groups** — all 27 entity types have unique first tokens
- Llama (BPE, ~128K vocab): **0 collision groups** — same
- Mistral (SentencePiece, ~32K vocab): **2 collision groups** (SID/SEN/SIDE→'S', BAL/BOD→'B')
- **Residual AC narrative**: Mistral AC 1.3% = residual after collision fix (was 16.6%); Qwen/Llama AC 2.1-3.8% = purely model semantic confusion (confuses similar entity types like SID vs SEN), NOT tokenizer collision

**关键 findings**:
- RoV 是压倒性违规（64-89%），远超 RE 的 RV（1-30%）→ 更强力展示 constraint 需求
- EV 显著（10-37%）→ grammar 层直接消除
- **Entity F1 从 0% 恢复到 11.7-17.6%**: 不是语义改进，是 format compliance 恢复——grammar enforcement 产生 schema-valid JSON，parser 才能识别 entity mentions
- Trigger F1 +1.5 to +1.8pp: elimination of OOV event types counted as FP
- CF 15-21% 比 RE 更高（EE argument structure 更复杂），沿用 RE 的 CF tradeoff framing

**Story upgrade**: WikiEvents results confirm paper narrative: "universal ontology-constrained structured generation framework applicable to any IE task with formal type constraints". Three evidence lines: (1) EV/RoV→0% across all models, (2) grammar-only ablation proves two-layer necessity, (3) post-hoc filtering is non-viable for EE. This is the key differentiator for conference main vs Findings.

**70B scale experiment** (P029-P030, in progress): Qwen3-70B AWQ-INT4 on SciERC + DocRED to demonstrate scale generalization. If successful, adds a 4th model to cross-model evidence, strengthening C5.

**Remaining risk**:
- CF 15-21% higher than RE → continues CF tradeoff framing
- 70B experiment timeline tight (need results by May 20 for paper integration)

## Anticipated Reviewer Concerns

### C1: "5.78% is barely above 5% — threshold is arbitrary"
**Response**: Don't argue about the threshold. Argue about per-relation distribution: Compare (27.6%), Evaluate-for (29.9%), Feature-of (11.3%) have double-digit violation rates with schema-informed prompt. The value proposition is per-relation guaranteed compliance, not overall statistical rate.

### C2: "Why not just post-hoc filter?"
**Response (D013, 实验结果已出)**:

Post-hoc filtering 实验结果：post-hoc F1 > OntoCoDec F1（SciERC 8.63 vs 8.36, DocRED 9.61 vs 8.24）——因 low F1 regime 下移除 FP 大幅提升 precision。

**论文 framing（不以 F1 论高低，多维对比）**:
1. **Recall 维度（核心论点）**: OntoCoDec recall 上升 (SciERC +0.20pp, DocRED +0.56pp) = 概率质量重分配到合法 token 生效。Post-hoc recall 下降 (SciERC -0.72pp, DocRED -1.06pp) = 正确 triple 被误删。
2. **Information coverage**: DocRED post-hoc 丢弃 **48.1%** triples（近半数信息丢失），SciERC 16.8%。OntoCoDec 保留全部 triple slots。
3. **Operational**: OntoCoDec 产出即合规、无需后处理、支持流式。Post-hoc 需额外管线、不适用实时场景。
4. **Precision trade-off（诚实承认）**: "Post-hoc achieves higher precision by removing a large fraction of triples, many of which are incorrect. This trades information coverage for precision — valid when FP are costly, but inadequate when completeness matters."

数据表：SciERC post-hoc rejection 16.8%, OntoCoDec recall 11.60 vs post-hoc 10.68; DocRED post-hoc rejection 48.1%, OntoCoDec recall 10.02 vs post-hoc 8.40。

**Reviewer 补充发现（D013 后）**:
5. **ET 残余**：post-hoc 只删 triples 不改 entity list，残余 ET=0.4% (SciERC) / 2.47% (DocRED)。OntoCoDec ET=0%。Post-hoc 无法解决 entity type 违规。
6. **127 个被删 TP (DocRED)**：过滤前 TP=1137，过滤后 TP=1010。丢失的 127 个 TP（11.2%）是正确提取但 entity type 违规的 triple。OntoCoDec 通过生成时强制合法 type 保留这些 TP——"prevent vs detect" 核心论据的具体数据。
7. **OntoCoDec+post-hoc 组合**（future work idea）：先 constrain 再 filter 残余 DR。低优先级，May 19 前不做。

### C3: "Bitwise AND of two masks is not novel"
**Response**: The novelty is not the AND operation — it's (a) the automatic compilation from ontology definitions (zero-code schema compliance), (b) the stateful entity registry enabling cross-field constraints during autoregressive generation, (c) the decidability taxonomy providing theoretical guidance, and (d) the systematic violation landscape measurement motivating the approach.

### C4: "Evaluate-for violation rate increases with schema-informed prompt"
**Response (prior-constraint conflict framework)**: Evaluate-for has 23/36 valid pairs; Method→Task is invalid for Evaluate-for but natural in the LLM's distributional prior ("Method X evaluates for Task Y" is semantically plausible). Schema-informed prompting creates a **prior-constraint conflict**: the model learns to avoid Method→Task for Evaluate-for (reducing count 133→87, -34.6%), but the remaining instances are harder boundary cases where the model's type assignment strategy becomes less stable. This is not just "harder instances" — it's an active interference between prompt-level constraint signals and the model's learned type associations.

**This strengthens the paper's claim**: prompt-level intervention is not merely insufficient but potentially **counterproductive** for specific constraint configurations. Decoding-time enforcement avoids this issue entirely — it operates on logits, not on the model's reasoning process, so there is no prior-constraint conflict.

### C5: "Only tested on one model (Qwen3-8B)"
**Response**: Cross-model validation DONE (D016 bootstrap verified). Llama-3.1-8B 零代码修改：
- SciERC: DR 13.34%→0.08% (↓99.4%), R-F1 -0.14pp (p=0.011, negligible), E-F1 NS
- DocRED: DR 26.07%→2.55% (↓90.2%), R-F1 +0.29pp (p=0.013, significant), E-F1 -0.64pp (p=0.022, modest decline)
- Parse failures: unconstrained 68 vs full_s1 91 (6.8% vs 9.1%)

**Cross-model claim 指导（Reviewer 专项评估）**:
- ✅ 可声明："OntoCoDec generalizes across model families without code modification"（程序性事实，铁证）
- ❌ 不可声明："consistently achieves the same reduction rate"（仅 2 模型，不足以量化声明）
- **RV↓DR↑ 正交性 finding**: Llama RV baseline 低(16%) 但 DR baseline 高(26%)，反向于 Qwen。证明两层约束解决正交 failure modes——vocabulary compliance ≠ semantic compliance。应作为 §5 cross-model 独立 finding 展开。
- **Parse failure 偏差**: checker skip parse failures (不计入 F1)，Llama 68/998=6.8% vs Qwen 12/998=1.2%。偏差方向保守（不利于 constrained），不威胁 claim。但需 footnote 披露 + cross-model 表增加 parse failure rate 行。
- **Llama SciERC CF=6.56%**: 比 Qwen 同量级更高，non-local constraint 问题在 Llama 上更突出，limitations 提及。
- 等 llama_docred_full_s1 出来后定最终 claim 措辞。

### C6: "Constrained decoding degrades generation quality (CRANE, Structure Snowballing)"
**Response**: OntoCoDec's semantic constraints are narrower than full grammar constraints — only type tokens are masked, free text is unconstrained. **Bootstrap CI (10000×, D012 Qwen + D016 Llama, all registry-aligned)**:

**Qwen3-8B**: SciERC R-F1 +0.13pp (p=0.58, NS), E-F1 -0.03pp (NS). DocRED R-F1 +0.50pp (p<0.001), E-F1 +1.23pp (p<0.001).
**Llama-3.1-8B**: SciERC R-F1 -0.14pp (p=0.011, negligible), E-F1 NS. DocRED R-F1 +0.29pp (p=0.013), E-F1 -0.64pp (p=0.022).

**Cross-model pattern**: DocRED R-F1 显著提升（两个模型）。E-F1 model-dependent（Qwen +1.23pp, Llama -0.64pp）。
- 机制：grammar 消除 OOV relation names + 非标 entity types → all_set 方法下减少 FP → precision 提升。Grammar 是 F1 提升的唯一来源（grammar_only Ent F1=59.38% ≈ full_s1 59.37%, Δ=0.01pp, p=0.66）。Semantic 层对 F1 无额外贡献。
- Frame as: "On DocRED, R-F1 gains are significant for both models. Entity F1 impact is model-dependent."
- 不升级为 core claim，但如实报告。

### C7: "Your method trades DR violations for CF violations (cross-field consistency)"
**Response**: Both S1 and S2 show elevated CF (per-triple rate ~8-10%). This is an inherent limitation of per-relation independent type enforcement. Must be proactively reported as a limitation. Defense:

**CF 子类型分析（根因已确认）**：
- **EVR（entity-vs-relation type drift）**: 占 CF 的 >90%。同一 entity 在 entity list 和 relation triple 中被赋予不同 type。S1: 245 entities (7.34%), S2: 178 entities (5.54%, -27%)
- **Within-rel（同 entity 跨 relation type 不一致）**: S1: 10 (0.36%), S2: 18 (0.72%)
- S2 减少 EVR 但增加 within-rel——trade-off 更复杂，不是单纯好/差

**Top 冲突模式**: Generic↔OtherScientificTerm (60次), Material↔OtherScientificTerm (28次), Material↔Method (20次)。**这些是 SciERC type system 固有的语义边界模糊区**——同一术语在不同学术语境下确实可以被合理归类为不同 type。CF 在相当程度上是 type system 模糊性的体现，非纯粹的方法缺陷。

**论证层次**：
1. DR violations = structurally invalid triples（下游系统不可用）→ hard constraint
2. CF violations = same entity gets different types across relations → individual triples remain type-valid, only cross-triple consistency broken → soft preference
3. CF 的根因是 type system 语义边界模糊 + per-relation 独立 enforcement，非 bug
4. Future work: cross-relation global consistency pass (entity-level type consensus before relation-specific enforcement)

**机制归因（口径对账确认）**：grammar_only CF=0.08%（与 unconstrained 持平），full_s1 CF=9.90%，full_s2 CF=8.03%。**CF 100% 由 semantic 层引入，grammar 层无贡献。** 这为 "CF 是 semantic type enforcement 的系统性副作用" 提供干净的消融证据。

**论文数字口径**：CF rate 用 violation_checker 口径（denominator=total_entities，与 DR/RV/ET 一致）。分析段落额外给 entity-level EVR 率 + 受影响样本比例。注意：analyze_cf 脚本的 EVR/WR 两维度不是独立的（WR⊂EVR），论文中不要作为两个独立维度报告。

**Do NOT hide this data.** Proactive disclosure + severity distinction + root cause analysis + type ambiguity evidence + 消融归因 = 最强防御策略。

### C8: "Absolute F1 is too low (~8%) — results are not meaningful"
**Response**: This is a zero-shot extraction setting (no training data, no fine-tuning). Low F1 is expected — supervised SOTA on SciERC relation F1 is ~40-50%. Our contribution is the constraint enforcement method, not extraction quality. F1 is a control variable verifying constraints don't degrade quality, not an optimization target. Recommended framing: "We evaluate in a zero-shot setting to demonstrate that our constraint enforcement method works without task-specific training. F1 is reported to verify that constraint enforcement does not degrade extraction quality, not as a claim of state-of-the-art performance."

## Paper Structure (Draft — D040 updated)
1. Introduction: Ontology constraint violations in LLM-based structured generation + composable framework overview (story: not just RE, general ontology-constrained generation)
2. Background: Grammar-constrained decoding (XGrammar) + IE ontology structure
3. Violation Landscape Study (Phase 0 empirics — independent contribution)
4. OntoCoDec Framework: Compiler + TypeConstraintProcessor + S1/S2 strategies
5. Experiments:
   - §5.1-5.3: RE experiments (SciERC + DocRED, 3 models, constrained vs unconstrained vs post-hoc vs prompt-based)
   - §5.4: **Event Extraction (WikiEvents)** — cross-task generalization (D040)
   - §5.5: Ablation + analysis (composability, latency, beam search, etc.)
6. Related Work: 5 constraint paradigms (grammar, vocabulary, structural, type-checking, ontology) + event extraction methods
7. Conclusion: Framework generality across IE tasks

## Claim Calibration (per Reviewer assessment)

**Safe to claim (sufficient evidence from Phase 2)**:
- "First systematic study of ontology constraint violations in LLM-based IE"
- "Violation rate correlates with constraint tightness, not ontology size" (D014: DR reduction ceiling 由 tightness × model RV baseline 共同决定)
- "Grammar+semantic constrained decoding eliminates 94% of DR violations at zero F1 cost" ✅ Phase 2 confirmed
- "Two-layer architecture provides complementary coverage — grammar enables semantic" ✅ Ablation confirmed
- "Prompt-level intervention scales poorly with ontology complexity" ✅ SciERC ↓62% vs DocRED ↓32%

**Claim with caution**:
- "Near-complete type-valid IE" — S1 0.93%, S2 0.97% residual, not truly 0%. Title updated to "Near-Complete"
- "Principled framework applicable to arbitrary IE ontologies" — RE validated on 2 datasets × 2 models; EE (WikiEvents) 10-doc preliminary shows ↓95.8% semantic violations, full results pending
- "F1 improvement" — SciERC: not significant (p=0.58), frame as F1-neutral; DocRED: significant (+0.50pp, p<0.001), 可报告但不升级为 core claim，归因于 OOV elimination 而非约束解码本身的提升
- "CF reveals type system ambiguity" — 可在 §5.3 作为 analysis finding 展开（Generic↔OtherScientificTerm 等模式有独立 insight 价值），但 §7 必须同时保留 CF 作为 limitation + future work。**两处都要有，缺一不可。** 不能暗示"因为是 type ambiguity 所以 CF 可接受"

**Do NOT claim**:
- "General infrastructure for IE" — only zero-shot extraction validated
- "State-of-the-art" — F1 is control variable, not optimization target (see C8)
- "Synergistic effect" — mechanism is enabling dependency, not mutual amplification (see Claim 3)
- "S2 solves CF" or "S2 mitigates Structure Snowballing" — data shows S2 ≈ S1 on all metrics; position as architectural variant only
- "Pilot50 DR=0%" — small-sample artifact, full S2 has DR=0.97%
- "Grammar-first invariant" 作为独立 claim — 证据不足（仅 1 次崩溃触发，实现是 fallback 非形式化保证）。写入 §4 方法论设计原则（1-2 句），不升级为 claim
- "Robust dual-layer composition across schema complexities" — 等 DocRED 完成。最终如 fallback ≤5/998，可写经验性陈述，不做泛化 claim

## Risk Ranking (ordered by reject probability)

1. **CF violation trade-off under-addressed** (MEDIUM-HIGH): S1 9.9%, S2 8.03% — both elevated. **S2 confirmed: does NOT solve CF.** This is the #1 attack surface. Mitigated by proactive disclosure + severity distinction + root cause analysis (C7). Must be reported as explicit limitation with future work direction (global entity-type consensus).
2. ~~**Single model limitation**~~ (RESOLVED): Llama-3.1-8B SciERC ✅ (DR↓99.4%) + DocRED ✅ (DR↓90.2%). 2 模型 × 2 数据集全矩阵完成。
3. **Novelty perception** (MEDIUM): "PLDI'25 for code → OntoCoDec for IE" attack line. Must argue IE constraint structure differs fundamentally.
4. ~~**DocRED Phase 2 weak**~~ (RESOLVED → reframed as D014): Qwen DR↓44.7%, Llama DR↓90.2% — both substantial. Weaker Qwen reduction explained by RV baseline interaction (D014), not method failure.
5. ~~**Phase 2 F1 drop**~~ (RESOLVED): F1 confirmed neutral (SciERC) or positive (DocRED, p<0.001). Bootstrap CI D012 confirms. No longer a risk.

## Critical Path to EMNLP Submission (May 25)

- **May 13-14**: Phase 0 + Phase 1 + Phase 2 SciERC ✅
- **May 14**: Phase 2 DocRED 4-way ablation ✅ + Llama SciERC cross-model ✅ + Dream 完成 (3/6)
- **May 14-15**: Llama DocRED ✅ + Checker 修正 ✅ + post-hoc ✅ + bootstrap CI ✅ + related work ✅
- **May 15-17**: Prompt sensitivity ✅ + WikiEvents pipeline 开发 + continuation v2 突破
- **May 17-18**: WikiEvents 3 模型 unconstrained baselines (进行中) + constrained 全量
- **May 18-19**: WikiEvents 结果分析 + §5.4 Event Extraction 章节撰写
- **May 19-20**: Intro/Abstract/Conclusion 升级（cross-task story）+ 内部稿 → submit_paper_to_review
- **May 20-24**: Review 修改 + 最终提交

**当前瓶颈**: WikiEvents 全量实验完成是关键路径。3 模型 unconstrained baselines 并行进行中（Qwen ~68/246, Mistral ~31/246, Llama 重启中），constrained 实验随后立即启动。

## Status
- Phase 0 SciERC: ✅ Complete (minimal + schema-informed)
- Phase 0 DocRED: ✅ Complete (minimal 18.7% DR + schema-informed 12.8% DR)
- Phase 1 Compiler: ✅ Complete (grammar + semantic layers integrated)
- Phase 2 SciERC (5 configs): ✅ Complete (S1 DR↓94% F1-neutral, S2 降级为 ablation)
- Phase 2 DocRED (4 configs): ✅ Complete (full_s1 DR↓45%, grammar ET/RV→0%)
- Llama SciERC cross-model: ✅ Complete (DR↓99.4%, F1-neutral, 零代码修改)
- Llama DocRED cross-model: ✅ Complete (full_s1 DR↓90.2%, unconstrained DR=26.07%)
- Checker v2 (D011): ✅ Fixed (ET triple-counting → unique entity dedup)
- Bootstrap CI (D012): ✅ Fixed + confirmed (entity filter bug resolved)
- Post-hoc baseline (D013): ✅ Complete (multi-dimensional framing)
- Related work: ✅ 42 bib entries, 4 additions merged
- Dream 6/6 actions: ✅ All complete
- CF violation analysis: ✅ Confirmed inherent limitation (S1 9.9% SciERC / 2.57% DocRED / 12.02% Llama DocRED)
- D014 tightness revision: ✅ Complete (tightness × RV baseline dual-factor)
- Llama bootstrap CI (D016): ✅ Fixed + verified (registry-aligned ≤0.05pp, all p-values in paper)
- Paper compilation: ✅ 8 pages正文 + appendix
- R5 text fixes (N1/N2/N3/W1-W6): ✅ All complete and verified
- Prompt sensitivity analysis: ✅ Complete (3 prompts × 2 modes, DR reduction 94.0-94.6%, σ=0.3pp; appendix written)
- Doc length breakdown: ✅ Complete (appendix written)
- **WikiEvents Event Extraction (D040)**: 🔄 Continuation v2 突破 (10-doc: RoV 0%, semantic ↓95.8%); 3 模型 unconstrained baselines 进行中; constrained 全量待启动


## registry (completed experiments)

- exp_id: mvp_phase0_violation_rate
  name: ''
  status: DONE
  conclusion: success
  metrics:
    total_triples: 1724
    total_entities: 2474
    json_parse_rate: 1
    entity_type_violation_rate: 0.004
    relation_vocabulary_violation_rate: 0.0139
    domain_range_violation_rate: 0.1537
    cross_field_consistency_violation_rate: 0.0008
    go_nogo_metric: 0.1537
    entity_f1: 0.3101
    relation_f1: 0.0823
    per_relation:
      Used-for:
        total: 787
        dr_violations: 6
        rate: 0.0076
      Conjunction:
        total: 32
        dr_violations: 0
        rate: 0
      Hyponym-of:
        total: 124
        dr_violations: 18
        rate: 0.1452
      Evaluate-for:
        total: 133
        dr_violations: 32
        rate: 0.2406
      Part-of:
        total: 72
        dr_violations: 18
        rate: 0.25
      Feature-of:
        total: 486
        dr_violations: 163
        rate: 0.3354
      Compare:
        total: 66
        dr_violations: 28
        rate: 0.4242
- exp_id: mvp_phase0_violation_rate_docred
  name: ''
  status: DONE
  conclusion: success
  metrics:
    total_docs: 998
    parsed_docs: 962
    json_parse_rate: 0.964
    total_entities: 19099
    total_triples: 16540
    entity_type_violation_rate: 0.075
    relation_vocabulary_violation_rate: 0.289
    domain_range_violation_rate: 0.187
    cross_field_consistency_violation_rate: 0.0008
    go_nogo_metric: 0.187
    fuzzy_matches: 126
    top_dr_violations_by_rate:
      P35_head_of_state: 1
      P710_participant: 0.919
      P172_ethnic_group: 0.875
    top_dr_violations_by_count:
      P31_instance_of:
        violations: 322
        total: 533
        rate: 0.604
      P1001_applies_to_jurisdiction:
        violations: 264
        total: 594
        rate: 0.444
      P1344_participant_in:
        violations: 194
        total: 312
        rate: 0.622
- exp_id: mvp_phase0_scierc_schema
  name: ''
  status: DONE
  conclusion: success
  metrics:
    domain_range_violation_rate: 0.0578
    relation_vocabulary_violation_rate: 0.003
    entity_type_violation_rate: 0
    total_violation_rate: 0.0253
    go_nogo_metric: 0.0578
    total_triples: 1661
    vs_minimal_dr_reduction: -0.624
    per_relation:
      Used-for:
        rate: TBD
      Feature-of:
        delta_pp: -22.3
      Part-of:
        delta_pp: -22.5
      Compare:
        delta_pp: -14.8
      Evaluate-for:
        delta_pp: 5.8
    mcnemar_all_significant: true
- exp_id: mvp_phase0_docred_schema
  name: ''
  status: DONE
  conclusion: success
  metrics:
    total_documents: 998
    documents_checked: 943
    parse_failures: 55
    json_parse_rate: 0.9449
    total_entities: 19524
    total_triples: 16782
    entity_type_violations: 119
    entity_type_violation_rate: 0.0061
    relation_vocabulary_violations: 3090
    relation_vocabulary_violation_rate: 0.1841
    relation_fuzzy_matches: 85
    domain_range_violations: 2154
    domain_range_violation_rate: 0.1284
    cross_field_consistency_violations: 29
    cross_field_consistency_violation_rate: 0.0015
    total_violations_any: 5392
    total_violation_rate: 0.1485
    go_nogo_metric_dr: 0.1284
- exp_id: phase2_scierc_grammar_only
  name: ''
  status: DONE
  conclusion: success
  metrics:
    total_samples: 551
    total_triples: 1725
    total_entities: 2474
    json_parse_rate: 1
    entity_type_violation_rate: 0
    relation_vocabulary_violation_rate: 0
    domain_range_violation_rate: 0.1484
    cross_field_consistency_violation_rate: 0.0008
    entity_f1: 0.3098
    entity_precision: 0.2598
    entity_recall: 0.3837
    relation_f1: 0.0823
    relation_precision: 0.0643
    relation_recall: 0.114
    checker_version: fixed_20260514_v2 (strip + alias + unique_et)
- exp_id: phase2_scierc_semantic_only
  name: ''
  status: DONE
  conclusion: success
  metrics:
    total_samples: 551
    total_triples: 1726
    total_entities: 2474
    json_parse_rate: 1
    entity_type_violation_rate: 0.004
    relation_vocabulary_violation_rate: 0.0151
    domain_range_violation_rate: 0.1165
    cross_field_consistency_violation_rate: 0.0271
    entity_f1: 0.3101
    entity_precision: 0.2605
    entity_recall: 0.3831
    relation_f1: 0.0815
    relation_precision: 0.0637
    relation_recall: 0.1129
    checker_version: fixed_20260514_v2 (strip + alias + unique_et)
- exp_id: phase2_scierc_full_s1
  name: ''
  status: DONE
  conclusion: success
  metrics:
    total_samples: 551
    total_triples: 1729
    total_entities: 2474
    json_parse_rate: 1
    entity_type_violation_rate: 0
    relation_vocabulary_violation_rate: 0
    domain_range_violation_rate: 0.0093
    cross_field_consistency_violation_rate: 0.099
    entity_f1: 0.3098
    entity_precision: 0.2598
    entity_recall: 0.3837
    relation_f1: 0.0836
    relation_precision: 0.0654
    relation_recall: 0.116
    checker_version: fixed_20260514_v2 (strip + alias + unique_et)
- exp_id: phase2_scierc_unconstrained
  name: ''
  status: DONE
  conclusion: success
  metrics:
    json_parse_rate: 1
    entity_f1: 0.3101
    entity_precision: 0.2605
    entity_recall: 0.3831
    relation_f1: 0.0823
    relation_precision: 0.0644
    relation_recall: 0.114
    entity_type_violation_rate: 0.004
    relation_vocabulary_violation_rate: 0.0139
    domain_range_violation_rate: 0.1537
    cross_field_consistency_violation_rate: 0.0008
    total_triples: 1724
    total_entities: 2474
    total_samples: 551
    checker_version: fixed_20260514_v2 (strip + alias + unique_et)
- exp_id: phase2_s2_pilot50
  name: ''
  status: DONE
  conclusion: success
  metrics:
    domain_range_violation_rate: 0.0205
    relation_vocabulary_violation_rate: 0
    relation_f1: 0.1008
    samples: 50
    predicted_relations: 146
    true_positives: 13
    gold_relations: 112
    entity_f1_approx: 0.29
    note: 'DR 修正: 原值 0 来自 dryrun (n=25 triples)。实际 pilot50 DR=3/146=2.05% (来自 violation_report_s2_pilot50.json)。'
- exp_id: mvp_phase0_docred_schema_r2
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: phase2_scierc_full_s2
  name: ''
  status: DONE
  conclusion: success
  metrics:
    total_samples: 551
    total_triples: 1644
    total_entities: 2228
    json_parse_rate: 1
    entity_type_violation_rate: 0
    relation_vocabulary_violation_rate: 0
    domain_range_violation_rate: 0.0097
    cross_field_consistency_violation_rate: 0.0803
    entity_precision: 0.2797
    entity_recall: 0.3712
    entity_f1: 0.319
    relation_precision: 0.064
    relation_recall: 0.1078
    relation_f1: 0.0803
    checker_version: fixed_20260514_v2 (strip + alias + unique_et)
- exp_id: phase2_docred_grammar_only
  name: ''
  status: DONE
  conclusion: success
  metrics:
    documents_checked: 985
    parse_failures: 13
    total_entities: 20150
    total_triples: 17341
    entity_type_violation_rate: 0
    relation_vocabulary_violation_rate: 0.0003
    domain_range_violation_rate: 0.2617
    cross_field_consistency_violation_rate: 0.0007
    relation_f1: 8.31
    relation_precision: 7.06
    relation_recall: 10.12
    entity_f1: 59.38
    entity_precision: 58.47
    entity_recall: 60.32
    unrecognized_relations: 5
    f1_method: all_set
    checker_version: fixed_20260514_v2 (strip + alias + unique_et)
- exp_id: phase2_docred_full_s1
  name: ''
  status: DONE
  conclusion: success
  metrics:
    documents_checked: 987
    parse_failures: 11
    total_entities: 20187
    total_triples: 17341
    entity_type_violation_rate: 0
    relation_vocabulary_violation_rate: 0.0003
    domain_range_violation_rate: 0.1021
    cross_field_consistency_violation_rate: 0.0257
    entity_f1: 59.37
    entity_precision: 58.45
    entity_recall: 59.63
    relation_f1: 8.23
    relation_precision: 6.99
    relation_recall: 10.01
    unrecognized_relations: 5
    f1_method: all_set
    checker_version: fixed_20260514_v2 (strip + alias + unique_et)
- exp_id: phase2_docred_unconstrained
  name: ''
  status: DONE
  conclusion: success
  metrics:
    documents_checked: 986
    parse_failures: 12
    total_entities: 20171
    total_triples: 17497
    entity_type_violation_rate: 0.0248
    relation_vocabulary_violation_rate: 0.2966
    domain_range_violation_rate: 0.1846
    cross_field_consistency_violation_rate: 0.001
    entity_f1: 58.15
    entity_precision: 57.26
    entity_recall: 58.32
    relation_f1: 7.74
    relation_precision: 6.55
    relation_recall: 9.46
    unrecognized_relations: 5189
    f1_method: all_set (includes OOV predictions in denominator)
    checker_version: fixed_20260514_v2 (strip + alias + unique_et)
    et_v1: 0.0818
    et_fix_note: v1 triple-counted ET across entity_list + relation head/tail; v2
      deduplicates by (text, normalized_type)
- exp_id: phase2_docred_semantic_only
  name: ''
  status: DONE
  conclusion: success
  metrics:
    documents_checked: 987
    parse_failures: 11
    total_entities: 20185
    total_triples: 17571
    entity_type_violation_rate: 0.0422
    relation_vocabulary_violation_rate: 0.2987
    domain_range_violation_rate: 0.1384
    cross_field_consistency_violation_rate: 0.0105
    entity_f1: 57.81
    entity_precision: 57.27
    entity_recall: 58.37
    relation_f1: 7.7
    relation_precision: 6.54
    relation_recall: 9.37
    f1_method: all_set
    checker_version: fixed_20260514_v2 (strip + alias + unique_et)
    et_v1: 0.1044
    et_fix_note: v1 triple-counted ET across entity_list + relation head/tail; v2
      deduplicates by (text, normalized_type)
- exp_id: llama_scierc_unconstrained
  name: ''
  status: DONE
  conclusion: success
  metrics:
    entity_type_violation_rate: 0
    relation_vocab_violation_rate: 0.0055
    domain_range_violation_rate: 0.1334
    cross_field_consistency_violations: 6
    entity_f1: 0.2356
    entity_precision: 0.1983
    entity_recall: 0.2902
    relation_f1: 0.0268
    relation_precision: 0.0236
    relation_recall: 0.031
    total_entities: 2451
    total_relations: 1274
    json_parse_failures: 1
    samples: 551
    checker_version: fixed_20260514_v2 (strip + alias + unique_et)
- exp_id: llama_scierc_full_s1
  name: ''
  status: DONE
  conclusion: success
  metrics:
    samples: 550
    entities_extracted: 2469
    relations_extracted: 1315
    domain_range_violation_rate: 0.0008
    relation_vocab_violation_rate: 0
    entity_type_violation_rate: 0
    cross_field_consistency_violation_rate: 0.0656
    total_violation_rate: 0.0431
    entity_f1: 0.2349
    entity_precision: 0.1972
    entity_recall: 0.2902
    relation_f1: 0.0254
    relation_precision: 0.0221
    relation_recall: 0.0298
    checker_version: fixed_20260514_v2 (strip + alias + unique_et)
- exp_id: llama_docred_unconstrained
  name: ''
  status: DONE
  conclusion: success
  metrics:
    checker_version: fixed_20260514_v2
    f1_method: all_set
    documents: 998
    documents_checked: 930
    parse_failures: 68
    unique_entities: 11525
    total_triples: 16437
    dr_eligible_triples: 13789
    ET_rate_pct: 0.13
    RV_rate_pct: 16.03
    DR_rate_pct: 26.07
    CF_rate_pct: 0.17
    entity_precision: 61.22
    entity_recall: 51.02
    entity_f1: 55.65
    relation_precision: 5.22
    relation_recall: 7
    relation_f1: 5.98
    fuzzy_relation_matches: 121
- exp_id: llama_docred_full_s1
  name: ''
  status: DONE
  conclusion: success
  metrics:
    checker_version: fixed_20260514_v2 (strip + alias + unique_et)
    f1_method: all_set
    violations:
      ET: 0
      RV: 0
      DR: 2.55
      CF: 12.02
    f1:
      entity_f1: 55.01
      entity_precision: 61.41
      entity_recall: 49.82
      relation_f1: 6.27
      relation_precision: 5.49
      relation_recall: 7.32
    counts:
      documents: 998
      documents_checked: 907
      parse_failures: 91
      unique_entities: 11296
      triples: 16368
- exp_id: posthoc_filtering_baseline
  name: ''
  status: DONE
  conclusion: success
  metrics:
    docred_f1_before: 7.74
    docred_f1_after: 9.61
    docred_precision_before: 6.55
    docred_precision_after: 11.22
    docred_recall_before: 9.46
    docred_recall_after: 8.4
    docred_rejection_rate: 0.481
    docred_tp_before: 1137
    docred_tp_after: 1010
    docred_tp_lost: 127
    docred_et_residual: 0.0247
    scierc_f1_before: 8.23
    scierc_f1_after: 8.63
    scierc_rejection_rate: 0.168
    scierc_recall_before: 11.4
    scierc_recall_after: 10.68
    scierc_tp_before: 111
    scierc_tp_after: 104
- exp_id: llama_docred_unconstrained_mt6144
  name: ''
  status: DONE
  conclusion: success
  metrics:
    ET_rate: 0.13
    RV_rate: 15.89
    DR_rate: 26.18
    DR_rate_eligible: 31.15
    CF_rate: 0.17
    entity_precision: 61.19
    entity_recall: 51.06
    entity_f1: 55.67
    relation_precision: 5.18
    relation_recall: 7
    relation_f1: 5.95
    parse_failures: 67
    documents_checked: 931
    total_documents: 998
    unique_entities: 11534
    total_triples: 16584
    dr_eligible_triples: 13936
    fuzzy_relation_matches: 121
- exp_id: llama_docred_full_s1_mt6144
  name: ''
  status: DONE
  conclusion: success
  metrics:
    DR_rate_pct: 2.57
    RV_rate_pct: 0
    ET_rate_pct: 0
    CF_rate_pct: 12.13
    R_F1: 6.25
    R_precision: 5.45
    R_recall: 7.32
    E_F1: 55.04
    E_precision: 61.41
    E_recall: 49.87
    documents_total: 998
    documents_checked: 908
    parse_failures: 90
    triples: 16471
    unique_entities: 11307
    fallback_events: 67911
    wall_clock_seconds: 23926
    vs_unconstrained_mt6144:
      DR_delta_pp: -23.61
      DR_reduction_pct: -90.2
      R_F1_delta_pp: 0.3
      E_F1_delta_pp: -0.63
    vs_full_s1_mt4096:
      DR_delta_pp: 0.02
      R_F1_delta_pp: -0.02
      E_F1_delta_pp: 0.03
      CF_delta_pp: 0.11
      parse_fail_delta: -1
- exp_id: w1_cf_fallback_scierc_pilot
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    ET: 0
    RV: 0
    DR: 0.1478
    CF: 0.0004
    R_F1: 0.0823
    R_P: 0.0643
    R_R: 0.114
    E_F1: 0.3098
    E_P: 0.2598
    E_R: 0.3837
    entities: 2474
    relations: 1725
    samples: 551
    grammar_first_fallback_rate: 0.3664
    cf_registry_fallback_rate: 0.0448
    total_mask_calls: 17024
    violation_budget_DR_CF: 0.1482
- exp_id: w1_cf_fallback_docred
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: w1_cf_fallback_llama_scierc
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: w1_cf_fallback_llama_docred
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: w5_lora_scierc_training
  name: ''
  status: DONE
  conclusion: success
  metrics:
    train_loss: 0.0634
    eval_loss: 0.0586
    eval_token_accuracy: 0.9816
    eval_entropy: 0.9635
    train_runtime_sec: 688.4
    epochs: 3
    checkpoint_path: /root/schema_semantic_constrained_ie/checkpoints/qwen3_8b_lora_scierc
    merged_model_path: /root/schema_semantic_constrained_ie/checkpoints/qwen3_8b_lora_scierc_merged
- exp_id: w5_lora_scierc_unconstrained_eval
  name: ''
  status: DONE
  conclusion: success
  metrics:
    json_parse_rate: 1
    entity_type_violation_rate: 0
    relation_vocabulary_violation_rate: 0
    domain_range_violation_rate: 0.0195
    cross_field_consistency_violation_rate: 0
    entity_f1: 0.6705
    entity_precision: 0.6523
    entity_recall: 0.6898
    relation_f1: 0.4386
    relation_precision: 0.4087
    relation_recall: 0.4733
    total_entities: 1784
    total_relations: 1128
    domain_range_violations: 22
    go_nogo_metric: 0.0195
    dr_gate: FAILED
- exp_id: w5_lora_scierc_constrained_eval
  name: ''
  status: DONE
  conclusion: success
  metrics:
    json_parse_rate: 1
    entity_type_violation_rate: 0
    relation_vocabulary_violation_rate: 0
    domain_range_violation_rate: 0
    cross_field_consistency_violation_rate: 0.0118
    entity_f1: 0.6705
    entity_precision: 0.6523
    entity_recall: 0.6898
    relation_f1: 0.4377
    relation_precision: 0.4078
    relation_recall: 0.4723
    total_entities: 1784
    total_relations: 1128
    total_samples: 551
    cross_field_consistency_violations: 21
- exp_id: w5_llama_lora_scierc_training
  name: ''
  status: DONE
  conclusion: success
  metrics:
    eval_loss: 0.0595
    eval_mean_token_accuracy: 0.9817
    eval_entropy: 1.0565
    train_loss: 0.0501
    train_runtime_sec: 654.23
    epochs: 3
    train_samples_per_second: 8.08
- exp_id: w5_llama_lora_scierc_unconstrained_eval
  name: ''
  status: DONE
  conclusion: success
  metrics:
    total_samples: 551
    total_entities: 1757
    total_relations: 1082
    json_parse_rate: 1
    entity_type_violation_rate: 0
    relation_vocabulary_violation_rate: 0
    domain_range_violation_rate: 0.0111
    cross_field_consistency_violation_rate: 0
    total_violation_rate: 0.0042
    entity_precision: 0.6647
    entity_recall: 0.691
    entity_f1: 0.6776
    relation_precision: 0.432
    relation_recall: 0.4795
    relation_f1: 0.4545
- exp_id: w5_llama_lora_scierc_constrained_eval
  name: ''
  status: DONE
  conclusion: success
  metrics:
    domain_range_violation_rate: 0.0009
    relation_vocabulary_violation_rate: 0
    entity_type_violation_rate: 0
    cross_field_consistency_violation_rate: 0.0046
    relation_f1: 0.4547
    relation_precision: 0.432
    relation_recall: 0.4795
    entity_f1: 0.6776
    entity_precision: 0.6647
    entity_recall: 0.691
    total_relations: 1081
    total_entities: 1757
    total_samples: 551
    parse_failures: 0
- exp_id: w5_qwen_docred_lora_training
  name: ''
  status: DONE
  conclusion: success
  metrics:
    eval_loss: 0.0614
    eval_mean_token_accuracy: 0.9804
    eval_entropy: 0.715
    train_loss: 0.0682
    train_runtime_s: 5825.6
    epochs: 3
    adapter_path: /root/schema_semantic_constrained_ie/checkpoints/qwen_lora_docred
    merged_path: /root/autodl-tmp/checkpoints/qwen_lora_docred_merged
- exp_id: w5_docred_sft_data_gen
  name: ''
  status: DONE
  conclusion: success
  metrics:
    train_samples: 3053
    dev_samples: 998
    train_entities: 59493
    train_relations: 38180
    dev_entities: 19528
    dev_relations: 12275
- exp_id: w5_llama_docred_sft_data_gen
  name: ''
  status: DONE
  conclusion: success
  metrics:
    train_samples: 3053
    dev_samples: 998
    train_size_mb: 19
    dev_size_mb: 6.1
- exp_id: w5_llama_docred_lora_training
  name: ''
  status: DONE
  conclusion: success
  metrics:
    train_loss: 0.0572
    eval_loss: 0.0624
    token_acc: 98.06
- exp_id: w5_llama_docred_lora_unconstrained_eval
  name: ''
  status: DONE
  conclusion: success
  metrics:
    ET_pct: 0
    RV_pct: 0.15
    DR_pct: 0.49
    E_F1: 83.93
    E_P: 84.93
    E_R: 82.96
    R_F1: 43.72
    R_P: 38.59
    R_R: 50.41
    parse_fail_rate: 2.3
    total_samples: 998
    total_entities_pred: 19106
    total_relations_pred: 16171
- exp_id: w5_llama_docred_lora_constrained_eval
  name: ''
  status: DONE
  conclusion: success
  metrics:
    total: 998
    parse_failures: 25
    parse_fail_rate: 2.51
    entities: 19077
    relations: 16074
    entity_f1: 85.23
    entity_precision: 85.04
    entity_recall: 85.41
    relation_f1_all_set: 44.23
    relation_precision_all_set: 38.82
    relation_recall_all_set: 51.4
    et_violations: 0
    et_violation_rate: 0
    rv_violations: 0
    rv_violation_rate: 0
    dr_violations: 33
    dr_violation_rate: 0.2
    cross_field_consistency_violations: 41
    delta_vs_unconstrained:
      delta_e_f1: 1.3
      delta_r_f1: 0.51
      delta_dr: -0.29
      delta_rv: -0.15
      note: Computed as constrained - unconstrained on full-set metrics (not intersection
        subset). Corrected 2026-05-16 per Reviewer audit.
- exp_id: w5_qwen_docred_lora_unconstrained_eval
  name: ''
  status: DONE
  conclusion: success
  metrics:
    ET_pct: 0
    RV_pct: 0.27
    DR_pct: 0.76
    CF_pct: 0.12
    E_F1: 82.15
    E_P: 85.44
    E_R: 79.11
    R_F1: 40.86
    R_P: 36.41
    R_R: 46.56
    parse_fail_rate: 7.11
    total_samples: 998
    success_samples: 927
    fail_samples: 71
    total_entities_pred: 18091
    total_relations_pred: 15870
    ET_pct_excl_fail: 0
    RV_pct_excl_fail: 0.27
    DR_pct_excl_fail: 0.76
    CF_pct_excl_fail: 0.12
    E_F1_excl_fail: 85.72
    E_P_excl_fail: 85.44
    E_R_excl_fail: 86
    R_F1_excl_fail: 42.2
    R_P_excl_fail: 36.41
    R_R_excl_fail: 50.17
- exp_id: w5_qwen_docred_lora_constrained_eval
  name: ''
  status: DONE
  conclusion: success
  metrics:
    ET_pct: 0
    RV_pct: 0
    DR_pct: 0.01
    CF_pct: 0.41
    E_F1: 81.43
    E_P: 85.41
    E_R: 77.81
    R_F1: 40.56
    R_P: 36.35
    R_R: 45.86
    parse_fail_rate: 8.52
    total_samples: 998
    success_samples: 913
    fail_samples: 85
    total_entities_pred: 17799
    total_relations_pred: 15563
    E_F1_excl_fail: 85.69
    R_F1_excl_fail: 42.23
    delta_vs_unconstrained:
      delta_DR: -0.75
      delta_RV: -0.27
      delta_R_F1: -0.3
      delta_R_F1_excl_fail: 0.03
      DR_reduction_pct: 98.7
      note: 'Constrained - unconstrained. Unconstrained: DR=0.76%, R_F1=40.86, R_F1_excl_fail=42.20'
- exp_id: w6_mistral_scierc_unconstrained
  name: ''
  status: DONE
  conclusion: success
  metrics:
    E_P: 0.2402
    E_R: 0.3156
    E_F1: 0.2728
    R_P: 0.0295
    R_R: 0.0483
    R_F1: 0.0366
    ET_pct: 1.5
    RV_pct: 0
    DR_pct: 56.94
    CF_pct: 56.87
    parse_fail_rate: 0
    total_samples: 551
    total_pred_entities: 2202
    total_pred_relations: 1593
- exp_id: w6_mistral_scierc_constrained
  name: ''
  status: DONE
  conclusion: success
  metrics:
    E_P: 0.2437
    E_R: 0.3144
    E_F1: 0.2746
    R_P: 0.0292
    R_R: 0.0493
    R_F1: 0.0367
    ET_pct: 0
    RV_pct: 0
    DR_pct: 13.4
    CF_pct: 1.27
    CF_count: 21
    parse_fail_rate: 0
    total_samples: 551
    total_pred_entities: 2162
    total_pred_relations: 1647
    delta_vs_unconstrained:
      delta_E_F1: 0.0018
      delta_R_F1: 0.0001
      delta_ET: -1.5
      delta_RV: 0
      delta_DR: -43.54
      note: 'Constrained - unconstrained. Baseline: E_F1=0.2728, R_F1=0.0366, DR=56.94%,
        ET=1.5%, RV=0%'
- exp_id: w6_mistral_docred_unconstrained
  name: ''
  status: DONE
  conclusion: success
  metrics:
    total_samples: 998
    parse_failures: 7
    parse_fail_rate: 0.7
    total_pred_entities: 12580
    total_pred_relations: 11879
    ET_pct: 7.58
    RV_pct: 42.35
    DR_pct: 57.42
    CF_pct: 24.78
    E_P: 0.6221
    E_R: 0.3975
    E_F1: 0.4851
    R_P: 0.0447
    R_R: 0.0432
    R_F1: 0.0434
    f1_method: fuzzy_normalized
    f1_note: Relation matching uses case-insensitive normalization with token-overlap
      >80% and edit-distance ≤2 fallback. Strict R_F1=3.50% (delta +0.84pp from 98
      additional TPs via fuzzy matching of Mistral underscore/abbreviation variants).
- exp_id: w6_mistral_docred_constrained
  name: ''
  status: DONE
  conclusion: success
  metrics:
    ET_pct: 0
    RV_pct: 0
    DR_pct: 33.2
    CF_pct: 0.19
    E_P: 65.02
    E_R: 41.4
    E_F1: 50.59
    R_P: 5.67
    R_R: 5.37
    R_F1: 5.52
    parse_fail_rate: 0.8
    total_samples: 998
    total_pred_entities: 12535
    total_pred_relations: 11554
    delta_vs_unconstrained:
      ET_pct: -7.58
      RV_pct: -42.35
      DR_pct: -24.22
      CF_pct: -24.59
      E_F1: 2.08
      R_F1: 2.02
- exp_id: w7_qwen_scierc_ft_grammar_only
  name: ''
  status: DONE
  conclusion: success
  metrics:
    ET_pct: 0
    RV_pct: 0
    DR_pct: 1.9
    CF_pct: 0
    parse_fail_rate: 0
    total_samples: 551
    total_entities: 1784
    total_relations: 1128
    E_P: 0.6523
    E_R: 0.6898
    E_F1: 0.6705
    R_P: 0.4087
    R_R: 0.4733
    R_F1: 0.4386
    DR_violations: 22
    tokenizer_warning: false_positive_transformers_4.57.6
- exp_id: w7_qwen_scierc_ft_semantic_only
  name: ''
  status: DONE
  conclusion: success
  metrics:
    ET_pct: 0
    RV_pct: 0
    DR_pct: 0.6
    CF_count: 15
    parse_fail_rate: 0
    total_samples: 551
    total_entities: 1784
    total_relations: 1128
    E_P: 0.6523
    E_R: 0.6898
    E_F1: 0.6705
    R_P: 0.4073
    R_R: 0.4713
    R_F1: 0.4369
    DR_violations: 7
    delta_vs_grammar_only:
      DR_delta: -1.3
      note: semantic_only DR=0.6% vs grammar_only DR=1.9%, semantic layer reduces
        DR by 68%
    delta_vs_unconstrained:
      DR_delta: -1.35
      note: unconstrained DR=1.95% → semantic_only 0.6%
- exp_id: w7_llama_scierc_ft_grammar_only
  name: ''
  status: DONE
  conclusion: success
  metrics:
    total_samples: 551
    json_parse_failures: 0
    total_entities: 1757
    total_relations: 1082
    entity_type_violation_rate: 0
    relation_vocabulary_violation_rate: 0
    domain_range_violation_rate: 0.0111
    cross_field_consistency_violation_rate: 0
    entity_f1:
      precision: 0.6647
      recall: 0.691
      f1: 0.6776
    relation_f1:
      precision: 0.432
      recall: 0.4795
      f1: 0.4545
- exp_id: w7_llama_scierc_ft_semantic_only
  name: ''
  status: DONE
  conclusion: success
  metrics:
    ET_pct: 0
    RV_pct: 0
    DR_pct: 0.65
    CF_count: 2
    E_F1: 67.76
    E_P: 66.47
    E_R: 69.1
    R_F1: 45.47
    R_P: 43.24
    R_R: 47.95
    total_entities: 1757
    total_relations: 1081
    json_parse_failures: 0
- exp_id: w8_ft_posthoc_baseline
  name: ''
  status: DONE
  conclusion: success
  metrics:
    ft_regime:
      qwen_scierc:
        R_F1_before: 43.86
        R_F1_posthoc: 43.94
        R_F1_constrained: 43.77
        reject_rate_pct: 1.95
        TP_lost: 4
      llama_scierc:
        R_F1_before: 45.45
        R_F1_posthoc: 45.23
        R_F1_constrained: 45.47
        reject_rate_pct: 1.11
        TP_lost: 5
      qwen_docred:
        R_F1_before: 40.91
        R_F1_posthoc: 41.11
        R_F1_constrained: TBD
        reject_rate_pct: 1.03
        TP_lost: 1
      llama_docred:
        R_F1_before: 43.77
        R_F1_posthoc: 43.92
        R_F1_constrained: 44.23
        reject_rate_pct: 0.64
        TP_lost: 1
    zs_regime:
      mistral_scierc:
        triples: 1584
        reject_pct: 20.27
        R_F1_before: 0.0376
        R_F1_posthoc: 0.0394
        R_F1_constrained: 0.0367
        TP_before: 48
        TP_after: 44
        TP_lost: 4
      qwen_scierc:
        triples: 1724
        reject_pct: 16.76
        R_F1_before: 0.0823
        R_F1_posthoc: 0.0863
        R_F1_constrained: 0.0836
        TP_before: 111
        TP_after: 104
        TP_lost: 7
      llama_scierc:
        triples: 1274
        reject_pct: 13.89
        R_F1_before: 0.0268
        R_F1_posthoc: 0.0271
        R_F1_constrained: 0.0254
        TP_before: 30
        TP_after: 28
        TP_lost: 2
      qwen_docred:
        triples: 17497
        reject_pct: 48.12
        R_F1_before: 0.0774
        R_F1_posthoc: 0.0961
        R_F1_constrained: 0.0823
        TP_before: 1137
        TP_after: 1010
        TP_lost: 127
      llama_docred:
        triples: 16437
        reject_pct: 42.18
        R_F1_before: 0.0598
        R_F1_posthoc: 0.0744
        R_F1_constrained: 0.0627
        TP_before: 850
        TP_after: 802
        TP_lost: 48
      mistral_docred:
        triples: 11836
        reject_pct: 73.73
        R_F1_before: 0.0434
        R_F1_posthoc: 0.0385
        R_F1_constrained: 0.0552
        TP_before: 518
        TP_after: 292
        TP_lost: 226
        removed_RV: 4172
        removed_ET: 3382
        removed_DR: 1173
        note: Only ZS case where posthoc HURTS R_F1 — 73.7% rejection rate loses 43.6%
          of TPs
    key_finding: 'ZS: post-hoc R_F1 >= constrained R_F1 in 5/6 groups. Exception:
      Mistral DocRED where extreme rejection rate (73.7%) causes net F1 loss. Constrained
      decoding value is in structural guarantee (0% violations) and composability,
      not F1 preservation.'
- exp_id: w8_llama_docred_ft_grammar_only
  name: ''
  status: DONE
  conclusion: success
  metrics:
    E_F1: 84.04
    R_F1: 43.77
    entity_precision: 84.99
    entity_recall: 83.11
    relation_precision: 38.6
    relation_recall: 50.53
    ET_pct: 0
    RV_pct: 0
    DR_pct: 0.51
    CF_pct: 0.12
    parse_fail_rate: 2.3
    total_samples: 998
    total_relations: 16199
    unique_entities: 13225
    parse_failures: 23
- exp_id: w8_qwen_docred_ft_grammar_only
  name: ''
  status: DONE
  conclusion: success
  metrics:
    E_F1: 82.19
    E_P: 85.47
    E_R: 79.16
    R_F1: 40.85
    R_P: 36.27
    R_R: 46.77
    ET_pct: 0
    RV_pct: 0
    DR_pct: 0.61
    CF_pct: 0.11
    parse_fail_rate: 7.01
    total_samples: 998
    parse_failures: 70
- exp_id: w8_qwen_docred_ft_semantic_only
  name: ''
  status: DONE
  conclusion: success
  metrics:
    E_F1: 82.15
    E_P: 85.58
    E_R: 78.99
    R_F1: 40.89
    R_P: 36.35
    R_R: 46.73
    ET_pct: 0
    RV_pct: 0.23
    DR_pct: 0.21
    CF_pct: 0.27
    parse_fail_rate: 7.52
    total_samples: 998
    parse_failures: 75
    documents_checked: 923
    total_entities: 18025
    total_triples: 15909
    DR_violations: 34
    RV_violations: 37
    ET_violations: 0
    CF_violations: 49
- exp_id: w8_llama_docred_ft_semantic_only
  name: ''
  status: DONE
  conclusion: success
  metrics:
    E_F1: 84.02
    E_P: 85.01
    E_R: 83.06
    R_F1: 43.9
    R_P: 38.89
    R_R: 50.4
    ET_pct: 0
    RV_pct: 0.15
    DR_pct: 0.3
    CF_pct: 0.16
    parse_fail_rate: 2.4
    total_samples: 998
    parse_failures: 24
    documents_checked: 974
    total_entities: 19099
    total_relations: 16038
    DR_violations: 48
    RV_violations: 24
    ET_violations: 0
    CF_violations: 31
- exp_id: w9_qwen_scierc_zs_sampling
  name: ''
  status: DONE
  conclusion: success
  metrics:
    ET_pct: 0
    RV_pct: 0
    DR_pct: 0.75
    CF_pct: 9.9
    E_F1: 31.28
    R_F1: 7.42
    parse_fail_rate: 0
    total_samples: 551
    note: 'F1 computed by v2 checker; greedy baseline with same checker: E_F1=30.98,
      R_F1=8.36'
- exp_id: w9_qwen_docred_zs_sampling
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: w9_qwen_docred_zs_sampling_r2
  name: ''
  status: PREPARING
  conclusion: killed
  metrics: {}
- exp_id: beam_search_scierc_full_551
  name: ''
  status: DONE
  conclusion: success
  metrics:
    ET_pct: 0
    RV_pct: 0
    DR_pct: 0
    CF_pct: 0.53
    E_F1: 32
    R_F1: 8.56
    E_P: 26.83
    E_R: 39.63
    R_P: 6.69
    R_R: 11.91
    parse_fail_rate: 0
    total_entities: 2476
    total_relations: 1737
- exp_id: w9_qwen_scierc_stability_3seeds
  name: ''
  status: DONE
  conclusion: success
  metrics:
    seed_123:
      ET_pct: 0
      RV_pct: 0
      DR_pct: 0.93
      CF_pct: 9.9
      E_F1: 30.98
      R_F1: 8.36
    seed_456:
      ET_pct: 0
      RV_pct: 0
      DR_pct: 0.93
      CF_pct: 9.9
      E_F1: 30.98
      R_F1: 8.36
    seed_789:
      ET_pct: 0
      RV_pct: 0
      DR_pct: 0.93
      CF_pct: 9.9
      E_F1: 30.98
      R_F1: 8.36
    cross_seed_DR_std: 0
    cross_seed_DR_range: 0
    conclusion_note: Greedy decoding is fully deterministic - seed has no effect on
      output. All metrics identical across 3 seeds.
- exp_id: w9_llama_scierc_beam_551
  name: ''
  status: DONE
  conclusion: success
  metrics:
    ET_pct: 0
    RV_pct: 0
    DR_pct: 0
    CF_pct: 0.93
    CF_count: 15
    E_F1: 25.04
    E_P: 21.27
    E_R: 30.42
    R_F1: 3.33
    R_P: 2.68
    R_R: 4.41
    total_entities: 2398
    total_relations: 1606
    parse_fail_rate: 0
    total_samples: 551
    vs_greedy_full_s1:
      DR_delta: -0.08
      CF_delta: -5.63
      E_F1_delta: 1.55
      R_F1_delta: 0.79
      note: 'Greedy: DR=0.08%, CF=6.56%, E_F1=23.49%, R_F1=2.54%'
- exp_id: w9_qwen_docred_beam_50
  name: ''
  status: DONE
  conclusion: success
  metrics:
    ET_pct: 0
    RV_pct: 0
    DR_pct: 0
    CF_pct: 0.55
    E_F1: 58.64
    R_F1: 9.37
    total_samples: 50
    parse_failures: 3
    parse_fail_rate: 6
    vs_greedy_full_s1:
      DR_delta: -10.21
      CF_delta: -2.02
      E_F1_delta: -0.73
      R_F1_delta: 1.14
      note: 'Greedy full_s1 998 docs: DR=10.21%, CF=2.57%, E_F1=59.37, R_F1=8.23.
        Beam eliminates ALL DR on DocRED 96-type schema.'
- exp_id: w10_type_consensus_prototype
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    ET_pct: 0
    RV_pct: 0
    DR_pct: 0.93
    CF_pct: 9.9
    E_F1: 30.98
    R_F1: 8.36
    gtc_skip_total: 672
    gtc_skip_unique_entities: 258
    gtc_effective_corrections: 0
    delta_DR: 0
    delta_CF: 0
- exp_id: w10_type_consensus_docred_50
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    ET_pct: 0
    RV_pct: 0
    DR_pct: 8.69
    CF_pct: 2.4
    E_F1: 59.08
    R_F1: 8.33
    gtc_skip_total: 601
    gtc_skip_unique_entities: 213
    gtc_effective_corrections: 0
    delta_DR: 0
    delta_CF: 0
- exp_id: w10_llama_docred_beam_50
  name: ''
  status: DONE
  conclusion: success
  metrics:
    ET_pct: 0
    RV_pct: 0
    DR_pct: 0
    CF_pct: 0.94
    E_F1: 55.62
    R_F1: 9.47
    parse_failures: 3
    parse_fail_rate: 6
    total_samples: 50
    vs_greedy_full_s1:
      DR_delta: -2.57
      CF_delta: -11.19
      E_F1_delta: 0.61
      R_F1_delta: 3.2
      note: 'Greedy baseline: DR=2.57%, CF=12.13%, E_F1=55.01, R_F1=6.27'
    checker_note: Must use violation_checker_docred.py for DocRED (not violation_checker.py)
- exp_id: w10_mistral_scierc_beam_551
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    total_samples: 551
    parse_failures: 1
    parse_rate: 0.9982
    ET_pct: 0
    RV_pct: 0
    DR_pct: 13.79
    CF_pct: 0.57
    E_P: 23.04
    E_R: 31.64
    E_F1: 26.66
    R_P: 3.13
    R_R: 7.22
    R_F1: 4.37
    total_entities: 2294
    total_triples: 2241
    vs_greedy:
      baseline: w6_mistral_scierc_constrained
      greedy_DR: 13.4
      greedy_CF: 1.27
      greedy_E_F1: 27.46
      greedy_R_F1: 3.67
      delta_DR: +0.39pp
      delta_CF: -0.70pp
      delta_E_F1: -0.80pp
      delta_R_F1: +0.70pp
- exp_id: w10_beam_ablation_k2
  name: ''
  status: DONE
  conclusion: success
  metrics:
    ET_pct: 0
    RV_pct: 0
    DR_pct: 0.35
    CF_count: 71
    CF_pct: 4.12
    E_F1: 31.54
    R_F1: 8.75
    parse_failures: 0
    total_samples: 551
    total_triples: 1724
    vs_greedy:
      DR_delta: -0.58
      CF_delta: -5.78
      E_F1_delta: 0.56
      R_F1_delta: 0.39
      note: 'Greedy: DR=0.93%, CF=9.90%, E_F1=30.98, R_F1=8.36'
    vs_beam_k4:
      DR_delta: 0.35
      CF_delta: 3.59
      E_F1_delta: -0.46
      R_F1_delta: 0.19
      note: 'k=4: DR=0%, CF=0.53%, E_F1=32.00, R_F1=8.56'
- exp_id: w10_beam_ablation_k8
  name: ''
  status: DONE
  conclusion: success
  metrics:
    ET_pct: 0
    RV_pct: 0
    DR_pct: 0
    CF_pct: 0.08
    CF_count: 2
    E_F1: 32.18
    R_F1: 8.39
    E_P: 26.95
    E_R: 39.93
    R_P: 6.54
    R_R: 11.7
    parse_failures: 0
    total_samples: 551
    total_triples: 1744
    total_entities: 2483
    vs_greedy:
      DR_delta: -0.93
      CF_delta: -9.82
      E_F1_delta: 1.2
      R_F1_delta: 0.03
    vs_beam_k4:
      DR_delta: 0
      CF_delta: -0.45
      E_F1_delta: 0.18
      R_F1_delta: -0.17
- exp_id: w9_mistral_docred_beam_50
  name: ''
  status: DONE
  conclusion: success
  metrics:
    ET_violation_rate: 0
    RV_violation_rate: 0
    DR_violation_rate: 21.37
    CF_violations: 1
    total_triples: 524
    total_entities: 597
    docs_checked: 49
    parse_failures: 1
    E_F1: 51.78
    E_P: 65.2
    E_R: 42.94
    R_F1: 5.7
    R_P: 6.49
    R_R: 5.08
    R_tp: 34
    R_gold: 669
    R_pred: 524
- exp_id: w10_qwen_scierc_ft_beam_4
  name: ''
  status: DONE
  conclusion: success
  metrics:
    DR: 0
    CF: 0
    total_violation_rate: 0
    entity_type_violation_rate: 0
    relation_vocab_violation_rate: 0
    domain_range_violation_rate: 0
    cross_field_consistency_violation_rate: 0
    E_F1: 66.88
    E_P: 64.69
    E_R: 69.22
    R_F1: 44.23
    R_P: 39.41
    R_R: 50.41
    total_samples: 551
    json_parse_failures: 0
    total_entities: 1802
    total_relations: 1246
    vs_ft_greedy:
      baseline: w5_lora_scierc_constrained_eval
      DR_delta: 0% → 0% (same)
      CF_delta: 1.18% → 0.0% (eliminated all violations)
      E_F1_delta: 67.05 → 66.88 (-0.17, negligible)
      R_F1_delta: 43.77 → 44.23 (+0.46, slight improvement)
    vs_zs_beam_k4:
      DR_delta: 0% → 0% (same)
      CF_delta: 0.53% → 0.0% (eliminated)
      E_F1_delta: 32.00 → 66.88 (+34.88)
      R_F1_delta: 8.56 → 44.23 (+35.67)
- exp_id: r4_prompt_minimal
  name: ''
  status: DONE
  conclusion: success
  metrics:
    unconstrained:
      ET_pct: 0.58
      RV_pct: 1.16
      DR_pct: 16.91
      E_F1: 31.98
      R_F1: 7.91
    constrained:
      ET_pct: 0
      RV_pct: 0
      DR_pct: 0.92
      E_F1: 31.99
      R_F1: 7.85
    DR_reduction_pct: 94.6
    delta_R_F1_pp: -0.06
    delta_E_F1_pp: 0.01
- exp_id: r4_prompt_detailed
  name: ''
  status: DONE
  conclusion: success
  metrics:
    unconstrained:
      ET_pct: 0.22
      RV_pct: 0.45
      DR_pct: 11.07
      E_F1: 33.55
      R_F1: 10.48
    constrained:
      ET_pct: 0
      RV_pct: 0
      DR_pct: 0.64
      E_F1: 33.56
      R_F1: 10.48
    DR_reduction_pct: 94.2
    delta_R_F1_pp: 0
    delta_E_F1_pp: 0.01
- exp_id: ee_qwen_wikievents_unconstrained
  name: ''
  status: DONE
  conclusion: success
  metrics:
    parse_success: 218/246 (88.6%)
    ET: 0
    EV: 24
    RoV: 74.9
    AC: 0.3
    CF: 0
    trigger_f1: 0.1184
    argument_f1: 0.0009
    entity_f1: 0
- exp_id: ee_llama_wikievents_unconstrained
  name: ''
  status: DONE
  conclusion: success
  metrics:
    parse_success: 226/246 (91.9%)
    ET: 0
    EV: 10.5
    RoV: 88.8
    AC: 0.1
    CF: 0
    trigger_f1: 0.0572
    argument_f1: 0
    entity_f1: 0
- exp_id: ee_qwen_wikievents_constrained
  name: ''
  status: DONE
  conclusion: success
  metrics:
    parse_success: 206/246 (83.7%)
    ET: 0
    EV: 0
    RoV: 0.3
    AC: 2.1
    CF: 21.1
    trigger_f1: 0.1339
    argument_f1: 0.0168
    entity_f1: 0.1409
    parse_failures: 40
    go_no_go: 2.4
    note: after retry with max_new_tokens=8192
- exp_id: ee_llama_wikievents_constrained
  name: ''
  status: DONE
  conclusion: success
  metrics:
    parse_success: 215/246 (87.4%)
    ET: 0
    EV: 0
    RoV: 0
    AC: 3.4
    CF: 15.5
    trigger_f1: 0.078
    argument_f1: 0.011
    entity_f1: 0.178
    parse_failures: 31
    go_no_go: 3.4
    note: after retry with max_new_tokens=8192
- exp_id: ee_mistral_wikievents_unconstrained
  name: ''
  status: DONE
  conclusion: success
  metrics:
    parse_success: 194/246 (78.9%)
    ET: 0
    EV: 37.3
    RoV: 63.9
    AC: 0
    CF: 0
    trigger_f1: 0.0241
    argument_f1: 0
    entity_f1: 0
- exp_id: ee_mistral_wikievents_constrained
  name: ''
  status: DONE
  conclusion: success
  metrics:
    parse_success: 184/246 (74.8%)
    ET: 0
    EV: 0
    RoV: 54.8
    AC: 19.2
    CF: 0.7
    note: grammar_only baseline (old code without semantic mask fix)
- exp_id: ee_mistral_wikievents_constrained_v2
  name: ''
  status: DONE
  conclusion: success
  metrics:
    parse_success: 178/246 (72.4%)
    ET: 0
    EV: 0
    RoV: 0.1
    AC: 16.6
    CF: 13.9
    trigger_f1: 0.0508
    argument_f1: 0.0047
    entity_f1: 0.1245
    parse_failures: 68
    go_no_go: 16.7
- exp_id: ee_qwen_wikievents_constrained_v3
  name: ''
  status: DONE
  conclusion: success
  metrics:
    parse_success: 206/246 (83.7%)
    parse_failures: 40
    ET: 0
    EV: 0
    RoV: 0
    AC: 2.1
    CF: 21.1
    go_no_go: 2.05
    entity_f1: 0.1409
    trigger_f1: 0.1339
    argument_f1: 0.0168
    code_version: 938-line (collision+exact-match fix)
    posthoc_args_removed: 109
    posthoc_arg_f1: 0.017
    cf_voting_fix_rate: 15.9%
    cf_voting_entity_f1: 0.1352
- exp_id: ee_llama_wikievents_constrained_v3
  name: ''
  status: DONE
  conclusion: success
  metrics:
    parse_success: 207/246 (84.1%)
    parse_failures: 39
    ET: 0
    EV: 0
    RoV: 0
    AC: 3.8
    CF: 17.2
    go_no_go: 3.8
    entity_f1: 0.1763
    trigger_f1: 0.0748
    argument_f1: 0.0118
    code_version: 938-line (collision+exact-match fix)
    posthoc_args_removed: 173
    posthoc_arg_f1: 0.0118
- exp_id: ee_mistral_wikievents_constrained_v3
  name: ''
  status: DONE
  conclusion: success
  metrics:
    parse_success: 218/246 (88.6%)
    parse_failures: 28
    ET: 0
    EV: 0
    RoV: 0
    AC: 1.3
    CF: 14.9
    go_no_go: 1.26
    entity_f1: 0.1171
    trigger_f1: 0.0387
    argument_f1: 0.0031
    code_version: 938-line (collision+exact-match fix)
    posthoc_args_removed: 86
    posthoc_ac_after: 0
- exp_id: ee_mistral_wikievents_grammar_only_v3
  name: ''
  status: DONE
  conclusion: success
  metrics:
    parse_success: 218/246 (88.6%)
    parse_failures: 28
    ET: 0
    EV: 0
    RoV: 64
    AC: 13.8
    CF: 1.1
    go_no_go: 77.73
    entity_f1: 0.1192
    trigger_f1: 0.0337
    argument_f1: 0.0027
    code_version: 938-line (collision+exact-match fix)
    mode: grammar_only
- exp_id: 70b_scierc_unconstrained
  name: ''
  status: DONE
  conclusion: success
  metrics:
    ET_pct: 0
    RV_pct: 0.6
    DR_pct: 6.5
    CF_count: 0
    CF_pct: 0
    E_F1: 0.3517
    E_P: 0.3009
    E_R: 0.4232
    R_F1: 0.1122
    R_P: 0.0929
    R_R: 0.1417
    total_entities: 2353
    total_relations: 1485
    parse_failures: 0
    samples: 551
- exp_id: 70b_scierc_constrained
  name: ''
  status: DONE
  conclusion: success
  metrics:
    ET_pct: 0
    RV_pct: 0
    DR_pct: 0
    CF_count: 86
    CF_pct: 3.66
    E_F1: 0.3514
    E_P: 0.3007
    E_R: 0.4226
    R_F1: 0.1124
    R_P: 0.0932
    R_R: 0.1417
    total_entities: 2351
    total_relations: 1481
    parse_failures: 0
    samples: 551
- exp_id: 70b_docred_unconstrained
  name: ''
  status: RUNNING
  conclusion: ''
  metrics: {}
- exp_id: 70b_docred_constrained
  name: ''
  status: RUNNING
  conclusion: ''
  metrics: {}
- exp_id: q1_llama_lora_scierc_beam4
  name: ''
  status: DONE
  conclusion: success
  metrics:
    ET_violation_rate: 0
    RV_violation_rate: 0
    DR_violation_rate: 0
    CF_violation_rate: 0
    entity_f1: 67.94
    relation_f1: 46.11
    samples: 551
    total_entities: 1853
    total_relations: 727
- exp_id: p8_latency_overhead
  name: ''
  status: DONE
  conclusion: success
  metrics:
    samples: 551
    unconstrained_mean_s: 4.163
    unconstrained_median_s: 4.106
    unconstrained_total_s: 2293.7
    constrained_mean_s: 4.71
    constrained_median_s: 4.644
    constrained_total_s: 2595
    overhead_ratio_mean: 1.131
    overhead_ratio_median: 1.131
    overhead_ratio_p95_perdoc: 1.262
    overhead_pct: 13.1
- exp_id: p8b_docred_latency
  name: ''
  status: RUNNING
  conclusion: ''
  metrics: {}

# 输出格式（YAML，仅输出一个 ```yaml 块）

```yaml
tier: best
narrative_guidance: "..."
imagined_experiments:
  - name: "..."
    plan_id: "..."
    description: "..."
    expected_results: {metric: value, ...}
    result_rationale: "..."
    tables: []
    figures_description: []
    analysis: "..."
```


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "2f4adefe-7616-4627-9e1b-12f6cf4d1828",
  "type": "user",
  "uuid": "5ad56625-c8ef-47b4-9e2c-1dd60d4d82b8",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6",
  "sessionId": "91d3e0f3-a355-4901-81d3-cef73f6dac5a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-18T16:20:00.276Z_

```json
{
  "parentUuid": "5ad56625-c8ef-47b4-9e2c-1dd60d4d82b8",
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
  "uuid": "aa2a45e5-fea6-4cea-9000-fa590d010d6b",
  "timestamp": "2026-05-18T16:20:00.276Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6",
  "sessionId": "91d3e0f3-a355-4901-81d3-cef73f6dac5a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-18T16:20:00.276Z_

```json
{
  "parentUuid": "aa2a45e5-fea6-4cea-9000-fa590d010d6b",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "9790dacb-f3f2-49d3-b991-89246ede2aac",
  "timestamp": "2026-05-18T16:20:00.276Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6",
  "sessionId": "91d3e0f3-a355-4901-81d3-cef73f6dac5a",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：所有 pending 实验确认核心假设；论文叙事成功传达 non-obvious insights；审稿人认为 violation landscape + enabling dependency + cross-task generalization 三者构成完整且新颖的贡献 核心假设：['70B DocRE…",
  "leafUuid": "9790dacb-f3f2-49d3-b991-89246ede2aac",
  "sessionId": "91d3e0f3-a355-4901-81d3-cef73f6dac5a"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Universal ontology-constrained IE via composable grammar and semantic layers",
  "sessionId": "91d3e0f3-a355-4901-81d3-cef73f6dac5a"
}
```

---

### Assistant

_source line 8 · 2026-05-18T16:20:05.091Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed predicted data for all planned experiments in the experiment_plan, under the "best" tier scenario. Let me first find the experiment_plan to understand what experiments are planned.

Let me look at the experiment plan file and the current state of experiments.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9790dacb-f3f2-49d3-b991-89246ede2aac",
  "isSidechain": false,
  "requestId": "req_011CbALc2SHTwM2zwfLyuF76",
  "type": "assistant",
  "uuid": "9e4dd458-d04f-4452-b3d6-2e065a6697c7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6",
  "sessionId": "91d3e0f3-a355-4901-81d3-cef73f6dac5a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015T1Baff9cTY9qPUPBEJR6G",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 35202,
      "cache_read_input_tokens": 11841,
      "output_tokens": 269,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 35202,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 269,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 35202,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 35202
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

_source line 9 · 2026-05-18T16:20:05.556Z_

Let me find the experiment plan to identify all planned experiments.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9e4dd458-d04f-4452-b3d6-2e065a6697c7",
  "isSidechain": false,
  "requestId": "req_011CbALc2SHTwM2zwfLyuF76",
  "type": "assistant",
  "uuid": "f36bdceb-60c0-4051-8f7e-488165c056a2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6",
  "sessionId": "91d3e0f3-a355-4901-81d3-cef73f6dac5a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015T1Baff9cTY9qPUPBEJR6G",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 35202,
      "cache_read_input_tokens": 11841,
      "output_tokens": 269,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 35202,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 269,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 35202,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 35202
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

_source line 10 · 2026-05-18T16:20:08.502Z_

<details open><summary>🔧 Tool call — Agent · `toolu_017MYkBMpDkZeGeMG7irekBL`</summary>

```json
{
  "subagent_type": "Explore",
  "description": "Find experiment plan file",
  "prompt": "Search for the experiment plan file in /home/ubuntu/.agent-ml-research-idea_gen_0509_6/. Look for files named experiment_plan*, plan*, or similar. Also check for any YAML/JSON/MD files that contain \"planned\" experiment entries or \"plan_id\" fields. Search broadly - check the root directory and any subdirectories. Report the full path and contents of any matching files."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f36bdceb-60c0-4051-8f7e-488165c056a2",
  "isSidechain": false,
  "requestId": "req_011CbALc2SHTwM2zwfLyuF76",
  "type": "assistant",
  "uuid": "67786a22-82e3-4cd3-8c55-95f6a5bacbd4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6",
  "sessionId": "91d3e0f3-a355-4901-81d3-cef73f6dac5a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015T1Baff9cTY9qPUPBEJR6G",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 35202,
      "cache_read_input_tokens": 11841,
      "output_tokens": 269,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 35202,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 269,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 35202,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 35202
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

_source line 11 · 2026-05-18T16:20:35.100Z_

<details><summary>↩ Tool result · `toolu_017MYkBMpDkZeGeMG7irekBL`</summary>

```text
Perfect! I found the experiment plan files. Here's a comprehensive report:

## Summary

I found **two experiment plan files** in the directory structure:

### File 1: OntoCoDec Experiment Plan
**Path:** `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/experiment_plan.yaml`

This is the primary experiment plan for the OntoCoDec project targeting EMNLP 2026 ARR (deadline May 25, 2026). It contains:

- **7 Research Claims** (C1-C7): Covering violation landscapes, prompt insufficiency, composable frameworks, cross-model generalization, F1 impact, and cross-task applicability
- **35 Planned Experiments** with `plan_id` fields (P001-P035):
  - Phase 0: Violation Landscape (4 experiments) - ALL COMPLETE
  - Phase 2: SciERC Ablation (4 experiments) - ALL COMPLETE  
  - Phase 2: DocRED Ablation (4 experiments) - ALL COMPLETE
  - Phase 2: Cross-Model (4 experiments) - ALL COMPLETE
  - WikiEvents Event Extraction (6 experiments) - COMPLETE
  - WikiEvents EE Ablation (2 experiments) - COMPLETE
  - Conference Main Supplement Tier 1 (3 experiments) - IN PROGRESS (70B experiments)
  - Conference Main Supplement Tier 2-3 (additional experiments)

- **GPU Budget:** westd-16980 and westd-21461 with 4x RTX PRO 6000 96GB each
- **Status:** ~45 GPU-hours used; 70B experiments next

### File 2: Provenance-Grounded UIE Experiment Plan
**Path:** `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/prov_grounded_uie/experiment_plan.yaml`

This is a secondary project plan with:

- **4 Core Experiments** with `plan_id` fields (exp_sft_baseline, exp_posthoc_nli, exp_grpo_provenance, exp_comparison):
  - SFT Baseline (Qwen3-8B + LoRA on DocRED)
  - Post-hoc NLI Reranking
  - GRPO with Evidence Provenance Reward
  - Three-way Comparison with Degeneration Checks

Both files are structured YAML files with `plan_id` fields, experiment metadata (name, description, hypothesis, priority, dependencies), and results/status information.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "67786a22-82e3-4cd3-8c55-95f6a5bacbd4",
  "isSidechain": false,
  "promptId": "2f4adefe-7616-4627-9e1b-12f6cf4d1828",
  "type": "user",
  "uuid": "28cb7fdd-5479-4bc3-afa3-ce57cf9d1c8b",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Search for the experiment plan file in /home/ubuntu/.agent-ml-research-idea_gen_0509_6/. Look for files named experiment_plan*, plan*, or similar. Also check for any YAML/JSON/MD files that contain \"planned\" experiment entries or \"plan_id\" fields. Search broadly - check the root directory and any subdirectories. Report the full path and contents of any matching files.",
    "agentId": "a8de0f34357dea138",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Perfect! I found the experiment plan files. Here's a comprehensive report:\n\n## Summary\n\nI found **two experiment plan files** in the directory structure:\n\n### File 1: OntoCoDec Experiment Plan\n**Path:** `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/experiment_plan.yaml`\n\nThis is the primary experiment plan for the OntoCoDec project targeting EMNLP 2026 ARR (deadline May 25, 2026). It contains:\n\n- **7 Research Claims** (C1-C7): Covering violation landscapes, prompt insufficiency, composable frameworks, cross-model generalization, F1 impact, and cross-task applicability\n- **35 Planned Experiments** with `plan_id` fields (P001-P035):\n  - Phase 0: Violation Landscape (4 experiments) - ALL COMPLETE\n  - Phase 2: SciERC Ablation (4 experiments) - ALL COMPLETE  \n  - Phase 2: DocRED Ablation (4 experiments) - ALL COMPLETE\n  - Phase 2: Cross-Model (4 experiments) - ALL COMPLETE\n  - WikiEvents Event Extraction (6 experiments) - COMPLETE\n  - WikiEvents EE Ablation (2 experiments) - COMPLETE\n  - Conference Main Supplement Tier 1 (3 experiments) - IN PROGRESS (70B experiments)\n  - Conference Main Supplement Tier 2-3 (additional experiments)\n\n- **GPU Budget:** westd-16980 and westd-21461 with 4x RTX PRO 6000 96GB each\n- **Status:** ~45 GPU-hours used; 70B experiments next\n\n### File 2: Provenance-Grounded UIE Experiment Plan\n**Path:** `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/prov_grounded_uie/experiment_plan.yaml`\n\nThis is a secondary project plan with:\n\n- **4 Core Experiments** with `plan_id` fields (exp_sft_baseline, exp_posthoc_nli, exp_grpo_provenance, exp_comparison):\n  - SFT Baseline (Qwen3-8B + LoRA on DocRED)\n  - Post-hoc NLI Reranking\n  - GRPO with Evidence Provenance Reward\n  - Three-way Comparison with Degeneration Checks\n\nBoth files are structured YAML files with `plan_id` fields, experiment metadata (name, description, hypothesis, priority, dependencies), and results/status information."
      }
    ],
    "totalDurationMs": 26590,
    "totalTokens": 45150,
    "totalToolUseCount": 9,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 17265,
      "cache_read_input_tokens": 27251,
      "output_tokens": 629,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 17265
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 629,
          "cache_read_input_tokens": 27251,
          "cache_creation_input_tokens": 17265,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 17265,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 3,
      "searchCount": 1,
      "bashCount": 5,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 0
    }
  },
  "sourceToolAssistantUUID": "67786a22-82e3-4cd3-8c55-95f6a5bacbd4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6",
  "sessionId": "91d3e0f3-a355-4901-81d3-cef73f6dac5a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-18T16:20:37.757Z_

<details open><summary>🔧 Tool call — Read · `toolu_01YUzjuwWXS9PQQeRqQytoyS`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/experiment_plan.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "28cb7fdd-5479-4bc3-afa3-ce57cf9d1c8b",
  "isSidechain": false,
  "requestId": "req_011CbALebA6KcRELEj7vXY4L",
  "type": "assistant",
  "uuid": "1f473deb-2117-46bb-bdf5-4c3c8cf4a3e1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6",
  "sessionId": "91d3e0f3-a355-4901-81d3-cef73f6dac5a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WMkGXn7FwvfyftvXfmpWyC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 906,
      "cache_read_input_tokens": 47043,
      "output_tokens": 88,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 906,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 88,
          "cache_read_input_tokens": 47043,
          "cache_creation_input_tokens": 906,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 906
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

_source line 13 · 2026-05-18T16:20:37.762Z_

<details><summary>↩ Tool result · `toolu_01YUzjuwWXS9PQQeRqQytoyS`</summary>

```text
1	## OntoCoDec Experiment Plan
2	## Target: EMNLP 2026 ARR (May 25, 2026)
3	## Last updated: 2026-05-17
4	
5	claims:
6	  C1_violation_landscape:
7	    description: "LLM-based IE violates ontology type constraints at non-trivial rates; violation rate driven by constraint tightness × model RV baseline, not ontology size"
8	    status: supported
9	    evidence_strength: strong
10	
11	  C2_prompt_insufficiency:
12	    description: "Schema-informed prompting reduces but cannot eliminate violations; unreliable per-relation"
13	    status: supported
14	    evidence_strength: strong
15	
16	  C3_composable_framework:
17	    description: "OntoCoDec compiles IE ontology schemas into two composable constraint layers (grammar+semantic) with enabling dependency; near-complete DR elimination"
18	    status: supported
19	    evidence_strength: strong
20	
21	  C4_s1_vs_s2:
22	    description: "S2 two-pass offers no advantage over S1 single-pass; S1 adopted as primary"
23	    status: supported_demoted
24	    evidence_strength: moderate
25	    note: "S2 demoted to ablation (D007). S1 simpler + marginally better F1."
26	
27	  C5_cross_model:
28	    description: "OntoCoDec generalizes across models without code modification; DR reduction magnitude varies with model RV baseline"
29	    status: supported
30	    evidence_strength: strong
31	
32	  C6_f1_impact:
33	    description: "Constraint enforcement preserves or improves F1; improvement is model/dataset-dependent (Qwen DocRED significant, SciERC neutral)"
34	    status: supported
35	    evidence_strength: strong
36	
37	  C7_cross_task:
38	    description: "OntoCoDec generalizes beyond RE to Event Extraction (WikiEvents/KAIROS); framework is task-agnostic for any IE with ontology type constraints"
39	    status: supported
40	    evidence_strength: strong
41	    note: "v3 全量完成: 3 models × 246 docs, RoV=0% (all), EV=0% (all), AC 1.3-3.8% (residual semantic confusion). Grammar-only ablation confirms two-layer necessity (RoV=64%). Post-hoc comparison: 99.6-100% argument deletion."
42	
43	experiments:
44	  # --- Phase 0: Violation Landscape (ALL COMPLETE) ---
45	  - plan_id: P001
46	    name: SciERC violation rate (minimal prompt)
47	    claim: C1_violation_landscape
48	    registry_id: mvp_phase0_violation_rate
49	    priority: 1
50	    result: "DR=15.4%, 1724 triples"
51	
52	  - plan_id: P002
53	    name: SciERC violation rate (schema-informed prompt)
54	    claim: C2_prompt_insufficiency
55	    registry_id: mvp_phase0_scierc_schema
56	    priority: 1
57	    result: "DR=5.78%, -62.4% reduction, Evaluate-for regression"
58	
59	  - plan_id: P003
60	    name: DocRED violation rate (minimal prompt)
61	    claim: C1_violation_landscape
62	    registry_id: mvp_phase0_violation_rate_docred
63	    priority: 1
64	    result: "DR=18.7%, RV=28.9%"
65	
66	  - plan_id: P004
67	    name: DocRED violation rate (schema-informed prompt)
68	    claim: C2_prompt_insufficiency
69	    registry_id: mvp_phase0_docred_schema
70	    priority: 1
71	    result: "DR=12.8%, -32% reduction (weaker than SciERC)"
72	
73	  # --- Phase 2: SciERC Ablation (ALL COMPLETE) ---
74	  - plan_id: P005a
75	    name: SciERC unconstrained baseline
76	    claim: C3_composable_framework
77	    registry_id: phase2_scierc_unconstrained
78	    priority: 1
79	    result: "DR=15.37%, RV=1.39%, ET=0.40%, R-F1=8.23%"
80	
81	  - plan_id: P005
82	    name: SciERC grammar-only
83	    claim: C3_composable_framework
84	    registry_id: phase2_scierc_grammar_only
85	    priority: 1
86	    result: "RV→0%, ET→0%, DR=14.84% (grammar alone doesn't reduce DR), E-F1=30.98%"
87	
88	  - plan_id: P006
89	    name: SciERC semantic-only
90	    claim: C3_composable_framework
91	    registry_id: phase2_scierc_semantic_only
92	    priority: 1
93	    result: "DR=11.65% (↓24%), RV/ET unchanged, demonstrates enabling dependency"
94	
95	  - plan_id: P007
96	    name: SciERC full S1
97	    claim: C3_composable_framework
98	    registry_id: phase2_scierc_full_s1
99	    priority: 1
100	    result: "DR=0.93% (↓94%), RV/ET→0%, CF=9.90%, R-F1=8.36% (+0.13pp, p=0.58)"
101	
102	  - plan_id: P008
103	    name: SciERC full S2 (ablation)
104	    claim: C4_s1_vs_s2
105	    registry_id: phase2_scierc_full_s2
106	    priority: 1
107	    result: "DR=0.97%, CF=8.03%, R-F1=8.03% (worse than S1). Demoted."
108	
109	  # --- Phase 2: DocRED Ablation (ALL COMPLETE) ---
110	  - plan_id: P009
111	    name: DocRED unconstrained baseline
112	    claim: C3_composable_framework
113	    registry_id: phase2_docred_unconstrained
114	    priority: 1
115	    result: "DR=18.46%, RV=29.66%, ET=2.48%, R-F1=7.73%"
116	
117	  - plan_id: P010
118	    name: DocRED grammar-only
119	    claim: C3_composable_framework
120	    registry_id: phase2_docred_grammar_only
121	    priority: 1
122	    result: "RV→0.03%, ET→0%, E-F1=59.38% (grammar drives all E-F1 gain)"
123	
124	  - plan_id: P011
125	    name: DocRED semantic-only
126	    claim: C3_composable_framework
127	    registry_id: phase2_docred_semantic_only
128	    priority: 1
129	    result: "DR=13.96%, ET=4.22%"
130	
131	  - plan_id: P012
132	    name: DocRED full S1
133	    claim: C3_composable_framework
134	    registry_id: phase2_docred_full_s1
135	    priority: 1
136	    result: "DR=10.21% (↓45%), RV→0.03%, ET→0%, CF=2.57%, R-F1=8.23% (+0.50pp, p<0.001), E-F1=59.37% (+1.22pp, p<0.001)"
137	
138	  # --- Phase 2: Cross-Model (ALL COMPLETE) ---
139	  - plan_id: P013
140	    name: Llama SciERC unconstrained
141	    claim: C5_cross_model
142	    registry_id: llama_scierc_unconstrained
143	    priority: 2
144	    result: "DR=17.53%, RV=0.23%, ET=0.27%"
145	
146	  - plan_id: P014
147	    name: Llama SciERC full S1
148	    claim: C5_cross_model
149	    registry_id: llama_scierc_full_s1
150	    priority: 2
151	    result: "DR=0.10% (↓99.4%), RV/ET→0%, R-F1 neutral"
152	
153	  - plan_id: P015
154	    name: Llama DocRED unconstrained
155	    claim: C5_cross_model
156	    registry_id: llama_docred_unconstrained
157	    priority: 2
158	    result: "DR=26.07%, RV=16.03%, ET=0.13%, R-F1=5.98%"
159	
160	  - plan_id: P016
161	    name: Llama DocRED full S1
162	    claim: C5_cross_model
163	    registry_id: llama_docred_full_s1
164	    priority: 2
165	    result: "DR=2.55% (↓90.2%), RV/ET→0%, CF=12.02%, R-F1=6.27% (+0.29pp), E-F1=55.01% (-0.64pp), parse_failures=91/998"
166	
167	  # --- Supplementary (ALL COMPLETE) ---
168	  - plan_id: P017
169	    name: S2 pilot (50 docs)
170	    claim: C4_s1_vs_s2
171	    registry_id: phase2_s2_pilot50
172	    priority: 3
173	    result: "Pilot confirmed S2 works, full run in P008"
174	
175	  - plan_id: P018
176	    name: Post-hoc filtering baseline
177	    claim: C6_f1_impact
178	    registry_id: posthoc_filtering_baseline
179	    priority: 2
180	    result: "Post-hoc F1 > OntoCoDec F1 on both datasets. Framing: multi-dimensional (D013)"
181	    note: "Not in registry — computed offline"
182	
183	  - plan_id: P019
184	    name: Bootstrap CI (10000 iterations)
185	    claim: C6_f1_impact
186	    registry_id: d012_bootstrap_ci
187	    priority: 1
188	    result: "SciERC R-F1 +0.13pp p=0.58; DocRED R-F1 +0.50pp p<0.001, E-F1 +1.23pp p<0.001"
189	    note: "Computed offline, not GPU experiment"
190	
191	  - plan_id: P020
192	    name: DocRED schema compilation (Phase 0 R2)
193	    claim: C1_violation_landscape
194	    registry_id: mvp_phase0_docred_schema_r2
195	    priority: 3
196	    result: "killed — superseded by P004"
197	
198	  # --- WikiEvents Event Extraction (D040, conference main 关键路径) ---
199	  - plan_id: P021
200	    name: WikiEvents Qwen3-8B unconstrained
201	    claim: C7_cross_task
202	    priority: 1
203	    depends_on: null
204	    description: "WikiEvents event extraction, Qwen3-8B, unconstrained baseline"
205	
206	  - plan_id: P022
207	    name: WikiEvents Qwen3-8B constrained (full_s1)
208	    claim: C7_cross_task
209	    priority: 1
210	    depends_on: P021
211	    registry_id: ee_qwen_wikievents_constrained_v3
212	    result: "Parse=83.7%, EV=0%, RoV=0%, AC=2.1%, CF=21.1%, Entity-F1=14.1%, Trigger-F1=13.4%"
213	
214	  - plan_id: P023
215	    name: WikiEvents Llama-3.1-8B unconstrained
216	    claim: C7_cross_task
217	    priority: 1
218	    depends_on: null
219	    description: "WikiEvents event extraction, Llama-3.1-8B, unconstrained baseline"
220	
221	  - plan_id: P024
222	    name: WikiEvents Llama-3.1-8B constrained (full_s1)
223	    claim: C7_cross_task
224	    priority: 1
225	    depends_on: P023
226	    registry_id: ee_llama_wikievents_constrained_v3
227	    result: "Parse=84.1%, EV=0%, RoV=0%, AC=3.8%, CF=17.2%, Entity-F1=17.6%, Trigger-F1=7.5%"
228	
229	  - plan_id: P025
230	    name: WikiEvents Mistral-7B unconstrained
231	    claim: C7_cross_task
232	    priority: 1
233	    depends_on: null
234	    description: "WikiEvents event extraction, Mistral-7B-v0.3, unconstrained baseline"
235	
236	  - plan_id: P026
237	    name: WikiEvents Mistral-7B constrained (full_s1)
238	    claim: C7_cross_task
239	    priority: 1
240	    depends_on: P025
241	    registry_id: ee_mistral_wikievents_constrained_v3
242	    result: "Parse=88.6%, EV=0%, RoV=0%, AC=1.3%, CF=14.9%, Entity-F1=11.7%, Trigger-F1=3.9%"
243	
244	  # --- WikiEvents EE Ablation (COMPLETE) ---
245	  - plan_id: P027
246	    name: WikiEvents Mistral grammar_only v3
247	    claim: C3_composable_framework
248	    priority: 1
249	    depends_on: P025
250	    description: "Grammar-only ablation on Mistral WikiEvents — proves semantic layer necessity (RoV remains ~64%)"
251	
252	  - plan_id: P028
253	    name: WikiEvents EE post-hoc filtering (3 models)
254	    claim: C6_f1_impact
255	    priority: 1
256	    description: "Post-hoc filtering baseline for EE — demonstrates 99.6-100% argument deletion to achieve 0% violation"
257	
258	  # --- D049 Conference Main Supplement (P1-P3 Tier 1) ---
259	  - plan_id: P029
260	    name: 70B SciERC unconstrained + constrained
261	    claim: C5_cross_model
262	    priority: 1
263	    depends_on: null
264	    description: "Llama-3.1-70B-Instruct AWQ-INT4 on SciERC — scale dimension (8B→70B within Llama family). westd-21461 cuda:0 unconstrained + cuda:1 constrained. RUNNING."
265	
266	  - plan_id: P030
267	    name: 70B DocRED unconstrained + constrained
268	    claim: C5_cross_model
269	    priority: 1
270	    depends_on: null
271	    description: "Llama-3.1-70B-Instruct AWQ-INT4 on DocRED — scale dimension. westd-16980 cuda:0+1 (pending scp)"
272	
273	  - plan_id: P031
274	    name: Error analysis / case study
275	    claim: C7_cross_task
276	    priority: 1
277	    depends_on: null
278	    description: "10-20 representative cases from v3 EE results — AC residual analysis, CF root causes, qualitative evidence for paper"
279	
280	  # --- D049 Tier 2 ---
281	  - plan_id: P032
282	    name: EE FT composability
283	    claim: C3_composable_framework
284	    priority: 2
285	    depends_on: null
286	    description: "Fine-tuned model + OntoCoDec composability test (~30 GPU-hours). Only if time allows before May 25"
287	
288	  # --- D049 Tier 3 ---
289	  - plan_id: P033
290	    name: Grammar-only cross-model validation (Qwen/Llama EE)
291	    claim: C3_composable_framework
292	    priority: 3
293	    depends_on: null
294	    description: "Grammar-only ablation on Qwen/Llama WikiEvents EE for completeness"
295	
296	  - plan_id: P034
297	    name: Bootstrap CI for EE metrics
298	    claim: C6_f1_impact
299	    priority: 3
300	    depends_on: null
301	    description: "Statistical significance for EE F1 changes"
302	
303	  - plan_id: P035
304	    name: Latency overhead measurement
305	    claim: C3_composable_framework
306	    priority: 3
307	    depends_on: null
308	    description: "Wall-clock comparison: unconstrained vs constrained decoding overhead"
309	
310	gpu_budget:
311	  allocated: "westd-16980 cuda:0,1 + westd-21461 cuda:0,1 (4x RTX PRO 6000 96GB)"
312	  total_used: "~45 GPU-hours (RE + WikiEvents EE complete)"
313	  status: "70B experiments next — 4 GPUs all allocated for 70B SciERC/DocRED parallel runs"
314	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1f473deb-2117-46bb-bdf5-4c3c8cf4a3e1",
  "isSidechain": false,
  "promptId": "2f4adefe-7616-4627-9e1b-12f6cf4d1828",
  "type": "user",
  "uuid": "8b4a7130-efff-4b3c-a397-c101a2c618be",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/experiment_plan.yaml",
      "content": "## OntoCoDec Experiment Plan\n## Target: EMNLP 2026 ARR (May 25, 2026)\n## Last updated: 2026-05-17\n\nclaims:\n  C1_violation_landscape:\n    description: \"LLM-based IE violates ontology type constraints at non-trivial rates; violation rate driven by constraint tightness × model RV baseline, not ontology size\"\n    status: supported\n    evidence_strength: strong\n\n  C2_prompt_insufficiency:\n    description: \"Schema-informed prompting reduces but cannot eliminate violations; unreliable per-relation\"\n    status: supported\n    evidence_strength: strong\n\n  C3_composable_framework:\n    description: \"OntoCoDec compiles IE ontology schemas into two composable constraint layers (grammar+semantic) with enabling dependency; near-complete DR elimination\"\n    status: supported\n    evidence_strength: strong\n\n  C4_s1_vs_s2:\n    description: \"S2 two-pass offers no advantage over S1 single-pass; S1 adopted as primary\"\n    status: supported_demoted\n    evidence_strength: moderate\n    note: \"S2 demoted to ablation (D007). S1 simpler + marginally better F1.\"\n\n  C5_cross_model:\n    description: \"OntoCoDec generalizes across models without code modification; DR reduction magnitude varies with model RV baseline\"\n    status: supported\n    evidence_strength: strong\n\n  C6_f1_impact:\n    description: \"Constraint enforcement preserves or improves F1; improvement is model/dataset-dependent (Qwen DocRED significant, SciERC neutral)\"\n    status: supported\n    evidence_strength: strong\n\n  C7_cross_task:\n    description: \"OntoCoDec generalizes beyond RE to Event Extraction (WikiEvents/KAIROS); framework is task-agnostic for any IE with ontology type constraints\"\n    status: supported\n    evidence_strength: strong\n    note: \"v3 全量完成: 3 models × 246 docs, RoV=0% (all), EV=0% (all), AC 1.3-3.8% (residual semantic confusion). Grammar-only ablation confirms two-layer necessity (RoV=64%). Post-hoc comparison: 99.6-100% argument deletion.\"\n\nexperiments:\n  # --- Phase 0: Violation Landscape (ALL COMPLETE) ---\n  - plan_id: P001\n    name: SciERC violation rate (minimal prompt)\n    claim: C1_violation_landscape\n    registry_id: mvp_phase0_violation_rate\n    priority: 1\n    result: \"DR=15.4%, 1724 triples\"\n\n  - plan_id: P002\n    name: SciERC violation rate (schema-informed prompt)\n    claim: C2_prompt_insufficiency\n    registry_id: mvp_phase0_scierc_schema\n    priority: 1\n    result: \"DR=5.78%, -62.4% reduction, Evaluate-for regression\"\n\n  - plan_id: P003\n    name: DocRED violation rate (minimal prompt)\n    claim: C1_violation_landscape\n    registry_id: mvp_phase0_violation_rate_docred\n    priority: 1\n    result: \"DR=18.7%, RV=28.9%\"\n\n  - plan_id: P004\n    name: DocRED violation rate (schema-informed prompt)\n    claim: C2_prompt_insufficiency\n    registry_id: mvp_phase0_docred_schema\n    priority: 1\n    result: \"DR=12.8%, -32% reduction (weaker than SciERC)\"\n\n  # --- Phase 2: SciERC Ablation (ALL COMPLETE) ---\n  - plan_id: P005a\n    name: SciERC unconstrained baseline\n    claim: C3_composable_framework\n    registry_id: phase2_scierc_unconstrained\n    priority: 1\n    result: \"DR=15.37%, RV=1.39%, ET=0.40%, R-F1=8.23%\"\n\n  - plan_id: P005\n    name: SciERC grammar-only\n    claim: C3_composable_framework\n    registry_id: phase2_scierc_grammar_only\n    priority: 1\n    result: \"RV→0%, ET→0%, DR=14.84% (grammar alone doesn't reduce DR), E-F1=30.98%\"\n\n  - plan_id: P006\n    name: SciERC semantic-only\n    claim: C3_composable_framework\n    registry_id: phase2_scierc_semantic_only\n    priority: 1\n    result: \"DR=11.65% (↓24%), RV/ET unchanged, demonstrates enabling dependency\"\n\n  - plan_id: P007\n    name: SciERC full S1\n    claim: C3_composable_framework\n    registry_id: phase2_scierc_full_s1\n    priority: 1\n    result: \"DR=0.93% (↓94%), RV/ET→0%, CF=9.90%, R-F1=8.36% (+0.13pp, p=0.58)\"\n\n  - plan_id: P008\n    name: SciERC full S2 (ablation)\n    claim: C4_s1_vs_s2\n    registry_id: phase2_scierc_full_s2\n    priority: 1\n    result: \"DR=0.97%, CF=8.03%, R-F1=8.03% (worse than S1). Demoted.\"\n\n  # --- Phase 2: DocRED Ablation (ALL COMPLETE) ---\n  - plan_id: P009\n    name: DocRED unconstrained baseline\n    claim: C3_composable_framework\n    registry_id: phase2_docred_unconstrained\n    priority: 1\n    result: \"DR=18.46%, RV=29.66%, ET=2.48%, R-F1=7.73%\"\n\n  - plan_id: P010\n    name: DocRED grammar-only\n    claim: C3_composable_framework\n    registry_id: phase2_docred_grammar_only\n    priority: 1\n    result: \"RV→0.03%, ET→0%, E-F1=59.38% (grammar drives all E-F1 gain)\"\n\n  - plan_id: P011\n    name: DocRED semantic-only\n    claim: C3_composable_framework\n    registry_id: phase2_docred_semantic_only\n    priority: 1\n    result: \"DR=13.96%, ET=4.22%\"\n\n  - plan_id: P012\n    name: DocRED full S1\n    claim: C3_composable_framework\n    registry_id: phase2_docred_full_s1\n    priority: 1\n    result: \"DR=10.21% (↓45%), RV→0.03%, ET→0%, CF=2.57%, R-F1=8.23% (+0.50pp, p<0.001), E-F1=59.37% (+1.22pp, p<0.001)\"\n\n  # --- Phase 2: Cross-Model (ALL COMPLETE) ---\n  - plan_id: P013\n    name: Llama SciERC unconstrained\n    claim: C5_cross_model\n    registry_id: llama_scierc_unconstrained\n    priority: 2\n    result: \"DR=17.53%, RV=0.23%, ET=0.27%\"\n\n  - plan_id: P014\n    name: Llama SciERC full S1\n    claim: C5_cross_model\n    registry_id: llama_scierc_full_s1\n    priority: 2\n    result: \"DR=0.10% (↓99.4%), RV/ET→0%, R-F1 neutral\"\n\n  - plan_id: P015\n    name: Llama DocRED unconstrained\n    claim: C5_cross_model\n    registry_id: llama_docred_unconstrained\n    priority: 2\n    result: \"DR=26.07%, RV=16.03%, ET=0.13%, R-F1=5.98%\"\n\n  - plan_id: P016\n    name: Llama DocRED full S1\n    claim: C5_cross_model\n    registry_id: llama_docred_full_s1\n    priority: 2\n    result: \"DR=2.55% (↓90.2%), RV/ET→0%, CF=12.02%, R-F1=6.27% (+0.29pp), E-F1=55.01% (-0.64pp), parse_failures=91/998\"\n\n  # --- Supplementary (ALL COMPLETE) ---\n  - plan_id: P017\n    name: S2 pilot (50 docs)\n    claim: C4_s1_vs_s2\n    registry_id: phase2_s2_pilot50\n    priority: 3\n    result: \"Pilot confirmed S2 works, full run in P008\"\n\n  - plan_id: P018\n    name: Post-hoc filtering baseline\n    claim: C6_f1_impact\n    registry_id: posthoc_filtering_baseline\n    priority: 2\n    result: \"Post-hoc F1 > OntoCoDec F1 on both datasets. Framing: multi-dimensional (D013)\"\n    note: \"Not in registry — computed offline\"\n\n  - plan_id: P019\n    name: Bootstrap CI (10000 iterations)\n    claim: C6_f1_impact\n    registry_id: d012_bootstrap_ci\n    priority: 1\n    result: \"SciERC R-F1 +0.13pp p=0.58; DocRED R-F1 +0.50pp p<0.001, E-F1 +1.23pp p<0.001\"\n    note: \"Computed offline, not GPU experiment\"\n\n  - plan_id: P020\n    name: DocRED schema compilation (Phase 0 R2)\n    claim: C1_violation_landscape\n    registry_id: mvp_phase0_docred_schema_r2\n    priority: 3\n    result: \"killed — superseded by P004\"\n\n  # --- WikiEvents Event Extraction (D040, conference main 关键路径) ---\n  - plan_id: P021\n    name: WikiEvents Qwen3-8B unconstrained\n    claim: C7_cross_task\n    priority: 1\n    depends_on: null\n    description: \"WikiEvents event extraction, Qwen3-8B, unconstrained baseline\"\n\n  - plan_id: P022\n    name: WikiEvents Qwen3-8B constrained (full_s1)\n    claim: C7_cross_task\n    priority: 1\n    depends_on: P021\n    registry_id: ee_qwen_wikievents_constrained_v3\n    result: \"Parse=83.7%, EV=0%, RoV=0%, AC=2.1%, CF=21.1%, Entity-F1=14.1%, Trigger-F1=13.4%\"\n\n  - plan_id: P023\n    name: WikiEvents Llama-3.1-8B unconstrained\n    claim: C7_cross_task\n    priority: 1\n    depends_on: null\n    description: \"WikiEvents event extraction, Llama-3.1-8B, unconstrained baseline\"\n\n  - plan_id: P024\n    name: WikiEvents Llama-3.1-8B constrained (full_s1)\n    claim: C7_cross_task\n    priority: 1\n    depends_on: P023\n    registry_id: ee_llama_wikievents_constrained_v3\n    result: \"Parse=84.1%, EV=0%, RoV=0%, AC=3.8%, CF=17.2%, Entity-F1=17.6%, Trigger-F1=7.5%\"\n\n  - plan_id: P025\n    name: WikiEvents Mistral-7B unconstrained\n    claim: C7_cross_task\n    priority: 1\n    depends_on: null\n    description: \"WikiEvents event extraction, Mistral-7B-v0.3, unconstrained baseline\"\n\n  - plan_id: P026\n    name: WikiEvents Mistral-7B constrained (full_s1)\n    claim: C7_cross_task\n    priority: 1\n    depends_on: P025\n    registry_id: ee_mistral_wikievents_constrained_v3\n    result: \"Parse=88.6%, EV=0%, RoV=0%, AC=1.3%, CF=14.9%, Entity-F1=11.7%, Trigger-F1=3.9%\"\n\n  # --- WikiEvents EE Ablation (COMPLETE) ---\n  - plan_id: P027\n    name: WikiEvents Mistral grammar_only v3\n    claim: C3_composable_framework\n    priority: 1\n    depends_on: P025\n    description: \"Grammar-only ablation on Mistral WikiEvents — proves semantic layer necessity (RoV remains ~64%)\"\n\n  - plan_id: P028\n    name: WikiEvents EE post-hoc filtering (3 models)\n    claim: C6_f1_impact\n    priority: 1\n    description: \"Post-hoc filtering baseline for EE — demonstrates 99.6-100% argument deletion to achieve 0% violation\"\n\n  # --- D049 Conference Main Supplement (P1-P3 Tier 1) ---\n  - plan_id: P029\n    name: 70B SciERC unconstrained + constrained\n    claim: C5_cross_model\n    priority: 1\n    depends_on: null\n    description: \"Llama-3.1-70B-Instruct AWQ-INT4 on SciERC — scale dimension (8B→70B within Llama family). westd-21461 cuda:0 unconstrained + cuda:1 constrained. RUNNING.\"\n\n  - plan_id: P030\n    name: 70B DocRED unconstrained + constrained\n    claim: C5_cross_model\n    priority: 1\n    depends_on: null\n    description: \"Llama-3.1-70B-Instruct AWQ-INT4 on DocRED — scale dimension. westd-16980 cuda:0+1 (pending scp)\"\n\n  - plan_id: P031\n    name: Error analysis / case study\n    claim: C7_cross_task\n    priority: 1\n    depends_on: null\n    description: \"10-20 representative cases from v3 EE results — AC residual analysis, CF root causes, qualitative evidence for paper\"\n\n  # --- D049 Tier 2 ---\n  - plan_id: P032\n    name: EE FT composability\n    claim: C3_composable_framework\n    priority: 2\n    depends_on: null\n    description: \"Fine-tuned model + OntoCoDec composability test (~30 GPU-hours). Only if time allows before May 25\"\n\n  # --- D049 Tier 3 ---\n  - plan_id: P033\n    name: Grammar-only cross-model validation (Qwen/Llama EE)\n    claim: C3_composable_framework\n    priority: 3\n    depends_on: null\n    description: \"Grammar-only ablation on Qwen/Llama WikiEvents EE for completeness\"\n\n  - plan_id: P034\n    name: Bootstrap CI for EE metrics\n    claim: C6_f1_impact\n    priority: 3\n    depends_on: null\n    description: \"Statistical significance for EE F1 changes\"\n\n  - plan_id: P035\n    name: Latency overhead measurement\n    claim: C3_composable_framework\n    priority: 3\n    depends_on: null\n    description: \"Wall-clock comparison: unconstrained vs constrained decoding overhead\"\n\ngpu_budget:\n  allocated: \"westd-16980 cuda:0,1 + westd-21461 cuda:0,1 (4x RTX PRO 6000 96GB)\"\n  total_used: \"~45 GPU-hours (RE + WikiEvents EE complete)\"\n  status: \"70B experiments next — 4 GPUs all allocated for 70B SciERC/DocRED parallel runs\"\n",
      "numLines": 314,
      "startLine": 1,
      "totalLines": 314
    }
  },
  "sourceToolAssistantUUID": "1f473deb-2117-46bb-bdf5-4c3c8cf4a3e1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6",
  "sessionId": "91d3e0f3-a355-4901-81d3-cef73f6dac5a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 14 · 2026-05-18T16:20:37.877Z_

````json
{
  "parentUuid": "8b4a7130-efff-4b3c-a397-c101a2c618be",
  "isSidechain": false,
  "attachment": {
    "type": "nested_memory",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/CLAUDE.md",
    "content": {
      "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/CLAUDE.md",
      "type": "Project",
      "content": "## 当前项目\n当前绑定项目：**schema_semantic_constrained_ie**\n\n## 按需查阅\n- 项目配置：`load_project_config(\"schema_semantic_constrained_ie\")` 或 `load_project_config(\"schema_semantic_constrained_ie\", section=\"execution\")`\n- 知识文件：`read_project_file(file=...)` 读取项目文件（ROADMAP.md/memory.md/ideas.md/report.md 等）\n- 路线图：`read_roadmap()` 读取研究方向和短期任务\n- 产出目录：`/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/`（写文件后用 `register_artifact` 注册）\n\n## 用户自定义规则（必须遵守）\n### 审稿规则\n\n- **[EMNLP 2026]** “EMNLP 2026 通过 ARR 统一审稿，Main/Findings 不分开投稿（不是两个Track），Long/Short 也走同一审稿系统，Overall Assessment的评分标准如下：5 = Consider for Award（约前2.5%），4.5 = Borderline Award，4 = Conference（可被主会议接收），3.5 = Borderline Conference，3 = Findings（可被Findings接收），2.5 = Borderline Findings，2 = Resubmit next cycle（需大幅修改，可在下一周期完成），1.5 = Resubmit after next cycle（需大幅修改，无法在下一周期完成），1 = Do not resubmit（需完全重做或与*ACL无关）”\n\n> 以上规则由用户配置，优先级等同于硬约束。违反会被 Reviewer 标记。\n\n## Worker 操作规范\n\n### paper-writing-norms\n\n# 论文写作风格规范\n\n> 核心哲学：**论文是一个有说服力的故事，不是实验报告。** 审稿人在几十秒内判断论文价值——如果 Abstract 和 Introduction 读起来像实验日志，论文就已经失败了。\n\n---\n\n## 一、总体写作哲学\n\n### 1.1 故事驱动，不是数据堆砌\n\n- 论文必须以\"故事线\"为核心展开：问题 → 洞察 → 方法 → 验证\n- 禁止大量实验数据堆砌——每个数字出现必须服务于叙事推进\n- 附录内容必须在正文中有明确引用且融入叙事，禁止简单堆砌\n- 如果附录数据对核心叙事有重大影响，根据附录数据调整论文 framing\n\n### 1.2 主线统一性\n\n- 当 idea 在研究过程中发生变化后，**必须重审全文逻辑**\n- 常见问题：Introduction 讲的故事 A，Method 做的是故事 B，Results 又在讲故事 C\n- 修复方式：从最终实验结论反推，重写 Introduction 的问题定义和动机\n- 每次 idea 调整后检查：Abstract → Introduction → Method → Results → Discussion → Conclusion 是否形成一条连贯主线\n\n### 1.3 专有名词必须有定义\n\n- 首次出现的专有名词/缩写必须给出完整定义和解释\n- Abstract 中使用的缩写也必须在 Abstract 内定义（如 LLM = Large Language Model）\n- 不能假设读者知道你自己定义的术语——论文从来没解释过的概念不能直接使用\n- 通用规则：如果一个非标准术语第一次出现时没有括号定义，就是写作 bug\n\n### 1.4 写作前必读同类优秀论文\n\n- 每个章节动笔前，找 **2-3 篇目标会议近 1-2 年的高分论文**作为风格参考——同类问题或同类方法皆可\n- 重点学：\n  - Abstract 怎么用最少篇幅讲完故事\n  - Introduction 怎么从大问题切入到具体贡献\n  - Related Work 怎么 positioning 自己（不是 survey）\n  - Table/Figure 怎么压缩信息密度\n- **不是抄袭**，是学习同行的故事节奏和审美——不同子领域叙事节奏差异很大\n- 实操：Paper Agent 可以从 `literature_map.yaml` 中挑 `role=foundation` 或 `role=direct-competitor` 的论文，把 `{title, venue, year, abstract}` 附在 Worker 的 task_prompt 中作为概念参考；如需学习写作风格本身，让 Worker 通过 WebSearch 取得论文链接并 fetch 全文\n\n---\n\n## 二、Abstract 写作规范\n\n### 2.1 四个必答问题（150-250 words）\n\nAbstract 必须在很短的篇幅内清楚回答：\n1. **研究什么问题** — 1-2 句话交代背景和痛点\n2. **为什么重要** — 现有方法的不足（不用写太多）\n3. **本文提出什么** — 核心贡献的关键机制（简要，不堆砌细节）\n4. **结果说明什么** — 用具体实验结论支撑贡献\n\n### 2.2 禁忌\n\n- **禁止堆砌数据**：Abstract 不是 Results 的缩写。最多引用 2-3 个关键数字，要服务于 claim\n- **禁止过度宣传**：不说 \"revolutionary\"、\"groundbreaking\"\n- **禁止写成 Introduction 的缩写**：Abstract 是独立阅读单元\n- **禁止术语堆积**：如果审稿人几十秒内判断不出价值，就失败了\n- **缩写必须定义**：Abstract 中首次出现的缩写必须展开\n\n### 2.3 审稿人视角检验\n\n写完后用这个标准自检：审稿人能否在 30 秒内判断——\n- 问题是否重要？\n- 方法是否清楚？\n- 贡献是否可信？\n- 结果是否有说服力？\n\n---\n\n## 三、Introduction 写作规范\n\n### 3.1 完整叙事线（5 段结构）\n\nIntroduction 需要从一个清晰、重要的问题切入，逐步把读者带到核心贡献：\n\n1. **研究背景**（1-2 段）：大模型在某类能力/应用中已取得进展，但仍存在一个关键瓶颈\n2. **问题重要性**（1 段）：结合真实应用、已有方法局限或当前趋势，说明这不是小问题\n3. **现有方法不足**（1 段）：系统梳理为什么不够（依赖更大模型/更多数据/更复杂推理/更高成本，或只在特定 benchmark 有效）\n4. **本文核心想法**（1 段）：我们观察到什么、提出了什么方法、为什么能解决上述问题\n5. **贡献总结**（列表）：清楚列出方法贡献、实验贡献和分析贡献\n\n### 3.2 整体叙事结构\n\n```\n现有进展 → 关键缺口 → 本文洞察 → 方法概述 → 实验证据 → 贡献总结\n```\n\n### 3.3 禁忌\n\n- **禁止泛泛介绍**：不要开头就写 \"LLMs have shown remarkable capabilities...\"，要从具体问题切入\n- **禁止缺少过渡**：每段之间必须有逻辑连接\n- **禁止实验报告风格**：Introduction 不是 \"我们做了 X 实验得到了 Y 结果\" 的罗列\n- 每条 Contribution 必须有对应的 section/table 支撑\n- Contribution 列表中不能出现未在前文铺垫过的概念\n\n---\n\n## 四、Related Work 写作规范\n\n### 4.1 目标\n\n让审稿人相信：作者理解这个领域，知道自己的方法站在什么位置，清楚相对已有工作的真实增量在哪里。\n\n### 4.2 结构要求\n\n- 把已有工作分成几个清晰的主题（如模型训练、推理增强、工具调用、数据构建、评测等）\n- 每类简要说明：已有方法做了什么、解决了哪些问题、和本文的关系\n- 帮助读者理解：哪些是本文直接继承的，哪些方法不同但解决相似问题，哪些留下了本文要解决的缺口\n\n### 4.3 禁忌\n\n- **禁止论文堆砌**：不要写成 \"A proposed X. B proposed Y. C proposed Z.\" 的列表\n- **目标不是展示读了多少论文**，而是做归纳和比较\n- Contribution claim（\"To our knowledge, no prior work...\"）应放在 Introduction，不在 Related Work\n\n### 4.4 引用充足度\n\n- 引用必须覆盖：**直接相关方法、baseline 论文、评测 benchmark 论文、理论基础**\n- 任何一类缺失，审稿人会立刻看出来调研不充分\n- 引用密度参照目标会议近年录用论文的量级——明显偏少意味着 Related Work 调研不足\n\n---\n\n## 五、去 AI 写作风格（硬规则）\n\n以下模式是 AI 生成文本的典型标志，审稿人一眼能看出。**必须全部消除。**\n\n### 5.1 严禁破折号（最显著的 AI 痕迹）\n\n**这是 AI 写作最容易被识别的标志，审稿人最敏感。单列为最高优先级硬规则。**\n\n- 解释性 em-dash（—，U+2014）和 en-dash（–，U+2013）必须**全部删除**\n- 替代方式：用逗号、括号或拆分为两个句子\n- 强制检查命令：\n  ```bash\n  grep -n \"—\" paper/*.tex     # em-dash，每处人工判断是否必要\n  grep -n \" – \" paper/*.tex   # 解释性 en-dash，几乎都应删除\n  ```\n- 例外（允许保留）：表格分隔符、数字范围（`2020–2024`、`pp. 12–18`）、专有名词（`Newton–Raphson`）\n\n### 5.2 段落与句式\n\n- **禁止过度分段**：不需要每 2-3 句就换段，自然段 5-8 句是正常的\n- **减少关系从句**（which, that, who）：能用简洁直接的句子就不用从句\n- **禁止 -ing 短语结尾**：如 \"..., highlighting the applicability of...\" / \"..., demonstrating the effectiveness of...\"。这是 AI 写作最典型的标志之一\n- **禁止连续使用 \"Furthermore\" / \"Moreover\" / \"Additionally\"**：一段内最多用一个过渡词\n- **避免 \"It is worth noting that...\" / \"Notably, ...\"**：直接写要说的内容\n\n### 5.3 用词黑名单\n\n- 避免 \"delve into\" / \"leverage\" / \"utilize\" / \"facilitate\" — 用 \"explore\" / \"use\" / \"enable\"\n- 避免 \"a myriad of\" / \"a plethora of\" — 用 \"many\" / \"various\"\n- 避免 \"in the realm of\" / \"in the context of\" — 直接说\n- 避免 \"paradigm shift\" / \"novel\" 过度使用\n\n### 5.4 校对清单（4 步）\n\n1. 全文 proofread 语法和拼写\n2. 检查所有代词/指示词（this, that, it）是否指代明确\n3. **`grep \"—\"` + `grep \" – \"` 全文清零**（删除所有解释性 dash，§5.1）\n4. `grep \"ing,\"` 模式——大部分 -ing 分词短语需要改写\n\n---\n\n## 六、图表与视觉规范\n\n### 6.1 知识密度原则\n\n- **图表的信息必须紧凑**——不能为了美观而留大量白空间\n- 一张图如果只传达一个简单信息，要么缩小要么合并到其他图中\n- 能用 inline text 说清的不要占一整个 Figure\n\n### 6.2 表格规范\n\n- 表格和正文文字不能视觉重叠（检查 column 宽度和 alignment）\n- 小数精度全表统一\n- 最优加粗、次优下划线\n- Caption 必须自包含\n\n### 6.3 图片规范\n\n- 数值标签不能被线、bar、点遮住——用白色背景或偏移标签\n- 图中字体 >= 7pt（打印后仍可读）\n- 栏宽约束需匹配目标 venue 模板要求\n- 概念图/流程图要有信息量，不要画一个 trivial 的 pipeline 然后占半页\n\n### 6.4 空间效率\n\n- 顶会正文页数严格受限（具体页数查目标会议官网），每 cm² 都是宝贵资源\n- 优先使用 `\\subfigure` 合并相关图\n- Table 能 inline 就不要单独浮动\n- 图表占比与其对叙事的贡献成正比\n\n---\n\n## 七、投稿前通用准备\n\n### 7.1 模板必须官方（硬规则）\n\n- LaTeX 模板**必须从目标会议官网下载**（CallForPapers / Author Instructions 页面）\n- **不要用**：\n  - 网上他人转载的复制版本（可能被改过 margin / 行号设置）\n  - 上一年的模板（参数可能变：字体、margin、行号、anonymous 选项等）\n  - 组里学长留的旧版本（来源不明、无法追溯）\n- 风险：\n  - 样式不符合 → desk reject\n  - margin 不对 → 被审稿人质疑诚信\n  - reference 格式错 → 被认为不规范\n- 流程：先查会议官网 templates → 找不到再 `WebSearch \"{venue} {year} latex template official\"` → 仍找不到汇报 Director（不要用就近年版本顶替）\n- `\\documentclass[]{}` 选项必须与目标 venue + 阶段（review / camera-ready）一致\n\n### 7.2 投稿要求逐项核对\n\n- 目标会议如要求 Checklist / Ethical Statement / Broader Impact Statement / Reproducibility Statement，必须**认真填每一项**，不要全写 N/A\n- 页数限制：查目标会议官网\n- 匿名化要求：review 版 vs camera-ready 版本设置不同\n- 行号开启（review 版常需）\n- 字体大小、margin 不得修改 sty 文件\n\n### 7.3 最终修改 10 项检查流程\n\n提交前必须逐一检查：\n1. 所有最新实验结果已全部录入\n2. 根据实验结果将叙事调至最优状态\n3. 附录所有内容在正文中被引用且融入叙事\n4. 无数据堆砌（每个数字服务于叙事推进）\n5. Abstract 和 Introduction 具有吸引力（不是实验报告风格）\n6. 全文主线统一（idea 变化后各章节逻辑一致）\n7. 所有专有名词有定义\n8. 无 AI 风格标志（dash、-ing phrases、过度分段）\n9. 图表知识密度高、无视觉遮挡\n10. Reference 覆盖直接相关方法、baseline、benchmark、理论基础\n\n## 更多 Skills（按需加载）\n\n执行相关任务前，先 Read 对应 skill 获取环境配置和最佳实践。\n\n- **ssh-env-setup** — 远程服务器 Python/CUDA 环境搭建规范——discovery-first 流程、PEP 668 处理、PyTorch 版本选择。当需要在远程服务器搭建训练环境时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/ssh-env-setup.skill.md`\n- **check-training-status** — 当用户问训练进度/实验状态/查状态时使用。用专用工具查看训练状态，禁止 ssh_execute。  →  `/home/ubuntu/agent-ml-research/skills/global/check-training-status.skill.md`\n- **rebuttal** — 撰写和优化学术 rebuttal——逐条回应审稿意见，生成 response letter。当收到审稿意见、需要写 rebuttal、回复 reviewer 评论时使用。关键词：rebuttal、审稿意见、reviewer response、author response、meta-review、AC 意见。  →  `/home/ubuntu/agent-ml-research/skills/global/rebuttal.skill.md`\n- **review-reviewer-session-start** — Review Reviewer session 启动初始化——检查论文格式、编译状态、材料清单。Review Reviewer 角色 session 启动时自动使用。  →  `/home/ubuntu/agent-ml-research/skills/global/review-reviewer-session-start.skill.md`\n- **reference-audit** — 引用验证与审计——检查 bib 条目完整性、引用真实性、格式一致性。写论文、审查论文、提交前检查引用时使用。关键词：citation verification、引用检查、bib 审计、fake citation、引用格式。  →  `/home/ubuntu/agent-ml-research/skills/global/reference-audit.skill.md`\n- **accelerate-distributed** — HuggingFace Accelerate 分布式训练指南——4行代码实现多GPU/DeepSpeed/FSDP/混合精度。多GPU训练时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/accelerate-distributed.skill.md`\n- **draw-paper-figure** — 生成学术论文级 matplotlib 图表——按 narrative_intent + design_notes 设计，从 pattern 库选用技法，远程 SSH 执行输出 PDF/PNG  →  `/home/ubuntu/agent-ml-research/skills/global/draw-paper-figure.skill.md`\n- **experiment-analysis** — 实验结果分析框架——统计显著性检验、消融分析、baseline 对比、可视化建议。分析实验结果或撰写论文 Results 部分时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/experiment-analysis.skill.md`\n- **hf-hub** — HuggingFace Hub CLI (hf) — 下载/上传模型和数据集、管理缓存、搜索论文和模型。涉及 HuggingFace 资源操作时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/hf-hub.skill.md`\n- **latex-paper** — ML 顶会论文 LaTeX 写作全流程——Claim-Evidence 方法论、引用防幻觉、顶会模板速查、投稿工程链、会议转投。写论文/投稿时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md`\n- **lm-eval-harness** — lm-evaluation-harness 模型评估指南——MMLU/GSM8K/HumanEval 等 60+ 学术基准测试。评估模型质量、对比实验时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/lm-eval-harness.skill.md`\n- **ml-experiment-guide** — 跨项目 ML 实验避坑指南——从多个项目沉淀的通用踩坑经验与最佳实践。当 Worker 准备写实验代码、或排查实验问题时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/ml-experiment-guide.skill.md`\n- **paper-banana** — 用 PaperBanana 生成发表级学术统计图——LLM 写 matplotlib 代码 + Critic 迭代 3 轮，输入 CSV/JSON 数据 + 意图描述即可。需要 GOOGLE_API_KEY。  →  `/home/ubuntu/agent-ml-research/skills/global/paper-banana.skill.md`\n- **paper-image-extractor** — 从论文 PDF 或 arXiv 源码包提取图表——优先 arXiv 原始图片，回退 PDF 解析。用户说\"提取图\"/\"抽图\"/\"extract figures\"时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/paper-image-extractor.skill.md`\n- **peft-lora** — PEFT/LoRA/QLoRA 参数高效微调指南——LoRA 配置选择、QLoRA 量化训练、Adapter 管理与合并。微调大模型时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/peft-lora.skill.md`\n- **research-news** — 每日论文推荐——搜索 arXiv 最新论文，按相关性/新颖性/影响力评分，生成推荐列表。Director 说\"有什么新论文\"/\"最近进展\"/\"research news\"时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/research-news.skill.md`\n- **trl-training** — TRL (Transformer Reinforcement Learning) 训练指南——SFT/DPO/GRPO/KTO 配置与最佳实践。训练或对齐语言模型时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/trl-training.skill.md`\n- **wandb-guide** — W&B 查询最佳实践——如何高效使用 fetch_wandb_metrics / compare_wandb_runs / get_best_wandb_run 分析实验结果。分析实验指标时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/wandb-guide.skill.md`\n",
      "contentDiffersFromDisk": false
    },
    "displayPath": "projects/schema_semantic_constrained_ie/.claude/CLAUDE.md"
  },
  "type": "attachment",
  "uuid": "fed981e0-8348-4041-826e-266e6cdd2491",
  "timestamp": "2026-05-18T16:20:37.877Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6",
  "sessionId": "91d3e0f3-a355-4901-81d3-cef73f6dac5a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
````

---

### Runtime record

_source line 15_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：所有 pending 实验确认核心假设；论文叙事成功传达 non-obvious insights；审稿人认为 violation landscape + enabling dependency + cross-task generalization 三者构成完整且新颖的贡献 核心假设：['70B DocRE…",
  "leafUuid": "fed981e0-8348-4041-826e-266e6cdd2491",
  "sessionId": "91d3e0f3-a355-4901-81d3-cef73f6dac5a"
}
```

---

### Runtime record

_source line 16_

```json
{
  "type": "ai-title",
  "aiTitle": "Universal ontology-constrained IE via composable grammar and semantic layers",
  "sessionId": "91d3e0f3-a355-4901-81d3-cef73f6dac5a"
}
```

---

### Runtime record

_source line 17_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：所有 pending 实验确认核心假设；论文叙事成功传达 non-obvious insights；审稿人认为 violation landscape + enabling dependency + cross-task generalization 三者构成完整且新颖的贡献 核心假设：['70B DocRE…",
  "leafUuid": "fed981e0-8348-4041-826e-266e6cdd2491",
  "sessionId": "91d3e0f3-a355-4901-81d3-cef73f6dac5a"
}
```

---

### Runtime record

_source line 18_

```json
{
  "type": "ai-title",
  "aiTitle": "Universal ontology-constrained IE via composable grammar and semantic layers",
  "sessionId": "91d3e0f3-a355-4901-81d3-cef73f6dac5a"
}
```

---
