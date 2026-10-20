# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义： 含义：≥2 reviewers 认为 novelty 不足以支撑 main conference；核心 'guaranteed compliance' cl

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 33
- **Recorded user turns:** 1
- **Tool calls:** 5
- **Original source:** `logs/chats/exported-trajectories/account-1/8b60bbb7-357b-4091-8cce-e13fa8ccd284.jsonl`
- **Structured JSON:** [`a941ab7c6be136e57127.json`](../../sessions/a9/a941ab7c6be136e57127.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-22T05:50:11.271Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-22T05:50:11.271Z",
  "sessionId": "8b60bbb7-357b-4091-8cce-e13fa8ccd284",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：\n\n含义：≥2 reviewers 认为 novelty 不足以支撑 main conference；核心 'guaranteed compliance' claim 被 CF 数据和 post-hoc 比较削弱；需要 reframe 切入角度\n核心假设：[\"Novelty 被拒：'constrained decoding for IE is a straightforward application of XGrammar; the semantic layer is a lookup table with logit masking'\", \"CF 被视为 fundamental flaw：'you claim type-valid IE but introduce 10-21% cross-field violations — the cure is worse than the disease in some configs'\", \"Post-hoc 在 ZS regime 下 R_F1 全面优于 constrained decoding（5/6 configs），reviewer 直接问 'what's the point?'\", \"EE 完全被 dismiss：'Arg F1≈0, Entity F1 from 0→14% is just format compliance, not extraction improvement'\", '70B LoRA eval 出问题：DR>1% 或 R-F1 下降 >2pp 或 parse failure rate 过高（>10%），削弱 scale 泛化 claim', \"ZS 8% F1 被两位 reviewer 视为 'toy evaluation'\", 'GCD/BoostCD 被 reviewer 认为已 subsume 本文贡献']\n关键指标范围：{'emnlp_overall_assessment': [2.5, 3.5], 'review_novelty': [2.0, 3.0], 'review_soundness': [3.0, 3.5], 'review_significance': [2.0, 3.0], '70b_lora_scierc_DR_pct': [0.5, 3.0], '70b_lora_scierc_R_F1_delta_pp': [-3.0, -0.5], '70b_lora_docred_DR_pct': [0.5, 5.0], '70b_lora_docred_R_F1_delta_pp': [-4.0, -1.0], 'hostile_reviewer_count': [2, 3]}\n叙事方向：核心 \"type-valid IE\" framing 不成立，需要完全 reframe。仍冲 EMNLP 2026（October ARR cycle），不降级 venue。 Reframe 方向：从 \"constrained decoding method paper\" → \"empirical study paper with a tool\"。 新 title 方向：\"How Do LLMs Violate Ontology Constraints? A Systematic Study with Mitigation\"。 新 story：(1) 主贡献是 violation landscape 的系统性实证研究（tightness × RV baseline 交互、constraint-type taxonomy、cross-model/cross-task violation pattern），这本身是 ACL/EMNLP 近年接受的 empirical analysis 范式； (2) OntoCoDec 降级为 \"mitigation tool\" 而非核心贡献，证明 violation 可被系统性处理但存在 tradeoff（DR↓ vs CF↑）； (3) 重心转向 analysis findings——为什么 prompt 不够（prior-constraint conflict）、为什么 post-hoc 不够（information loss）、为什么 grammar-only 不够（enabling dependency）、为什么 CF 必然存在（prefix-decidability 的理论限制）。 这个 reframe 把 novelty 锚点从 method → empirical findings + theoretical analysis，避开 \"incremental over XGrammar\" 攻击线。 补充工作：(a) 更深的 violation pattern 分析（per-relation type、per-document length、per-entity ambiguity）；(b) 与 GoLLIE 等 code-generation IE 的 violation 对比（d063 已有初步数据）；(c) 理论部分扩展 decidability taxonomy 为 formal framework。\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: schema_semantic_constrained_ie\nvenue: emnlp-2026\nfocus: 评估当前论文（含 70B ZS 跨两个数据集 + 即将到手的 70B LoRA 结果）能否达到 EMNLP 2026 Overall Assessment 4.0（Conference）。重点关注：novelty 感知（semantic constraint layer 是否被视为足够新颖）、evaluation scope（RE 为主 + preliminary EE 是否足够）、与 GCD/BoostCD/XGrammar 的差异化。\n\n## paper_framing.md\n\n# OntoCoDec — Paper Framing\n\n## Target Venue\nEMNLP 2026 (ARR submission May 25, 2026) — **目标: conference main**（D040, 用户明确指示）\n\n## Title\nOntoCoDec: Type-Valid Information Extraction via Compiled Ontology Constraints\n(D015: \"Near-Complete\" dropped — DocRED residual DR=10.21% (Qwen) 不算 near-complete。论文贡献是方法，不是特定消除率。SciERC 0.93% 和 DocRED 2.55% (Llama) 可在正文中描述为 near-complete，但 title 不宜 overclaim。)\n\n**D040 Story 升级方向**: 从 \"IE-specific constrained decoding\" → \"universal ontology-constrained structured generation framework\"。WikiEvents Event Extraction 验证跨任务泛化。Continuation masking v2 突破（10-doc: RoV 0%, semantic violations ↓95.8%）初步确认跨任务有效性，全量实验进行中。最终 title 待全量结果后调整。\n\n## Core Insight\nLLM-based IE systems produce systematic ontology constraint violations concentrated in specific relation types. Prompt-level intervention (schema-informed prompting) reduces violations by ~62% but cannot eliminate them — certain relation types retain 25-30% violation rates even with explicit constraint descriptions. OntoCoDec provides **near-complete elimination (DR 15.4%→0.93%, ↓94%) at zero or positive F1 impact** through automatic ontology-to-decoder constraint compilation with two complementary layers.\n\n**Phase 2 confirmed (D012 bootstrap CI, v2 fix)**: Grammar+Semantic dual-layer constrained decoding reduces domain/range violations by 94%, eliminates entity-type and relation-vocabulary violations entirely (→0%). F1 impact is **dataset-dependent**:\n- SciERC: Rel F1 neutral (+0.13pp, p=0.58), Ent F1 neutral (-0.03pp, p=0.53)\n- DocRED: Rel F1 **significantly improved** (+0.50pp, p<0.001, 95% CI [+0.23, +0.81]); Ent F1 **significantly improved** (+1.23pp, p<0.001, 95% CI [+0.94, +1.55])\n- Mechanism: grammar 消除 OOV relation names (DocRED RV 29.66%→0.03%) + 非标 entity types (ET 2.48%→0%)。all_set F1 方法下 OOV=FP → fewer FP → higher precision/F1。SciERC baseline RV/ET 已很低，效果不显著。\n- **Grammar 层是 F1 提升的唯一来源**: grammar_only Ent F1=59.38% ≈ full_s1 59.37% (Δ+0.01pp, p=0.66)。Semantic 层对 F1 无额外贡献，专注 DR reduction。\n\n## Core Claims\n\n### Claim 1 (Empirical): Violation Landscape\nLLM-based IE systems violate ontology type constraints at non-trivial rates (15.4% per-triple on SciERC, 18.7% on DocRED). Violations are **not uniformly distributed** — they concentrate on relation types with tight domain/range constraints (Feature-of 33.5%, Compare 42.4%) while loose-constraint relations show near-zero violation (Used-for 0.8%).\n\n**Key insight**: Violation rate is driven by **constraint tightness**, not ontology size. A small ontology with tight constraints can produce more violations than a large ontology with loose constraints.\n\n**D014 修订**: DR reduction ceiling 由 **tightness × model RV baseline** 共同决定，非 tightness 单因素。Llama DocRED DR↓90.2% vs Qwen DR↓44.7%（同一 ontology τ̄=0.842）。机制：Qwen RV=29.66% >> Llama RV=16.03% → grammar 层将 OOV triples 强制匹配有效关系名 → 揭露大量 latent DR violations → 残余 DR 更高。这是比单一 tightness 更深的 insight。\n\n**Evidence**: SciERC (7 relations) 15.4%; DocRED (96 relations) 18.7% — comparable rates despite 14× ontology size difference. Schema-informed prompt on DocRED only achieves DR↓32% (vs SciERC ↓62%), confirming **prompt-level intervention scales poorly with ontology complexity**.\n\n### Claim 2 (Empirical): Prompt Insufficiency\nSchema-informed prompting (explicitly describing domain/range constraints in the prompt) reduces but does not eliminate violations:\n- Overall: 15.4% → 5.78% (-62.4%), still above 5%\n- Per-relation: Compare 42.4% → 27.6%, Evaluate-for 24.1% → 29.9% (**worse**)\n- Prompt intervention is unreliable at the per-relation level — some relations improve, one regresses\n\n**Narrative**: This is NOT about \"5.78% barely above 5%\". The story is: **prompt-level intervention is fundamentally unreliable as a guarantee mechanism**. It works statistically but cannot provide per-instance compliance. Three specific relation types retain >10% violation rates with schema-informed prompts. For safety-critical IE (biomedical, legal, regulatory), statistical reduction is insufficient — guaranteed compliance is required.\n\n### Claim 3 (Methodological): Composable Constraint Framework\nOntoCoDec automatically compiles IE ontology schemas into two composable constraint layers:\n1. **Grammar layer** (XGrammar): JSON structure + type vocabulary constraints (CFG-expressible)\n2. **Semantic layer** (TypeConstraintProcessor): Cross-field domain/range constraints via stateful entity registry + dynamic logit masking\n\nThe two layers are **complementary with enabling dependency**: grammar ensures every generated relation type is in the valid vocabulary, which enables the semantic layer to look up and enforce domain/range rules for that type. Without grammar, the semantic layer encounters unknown relation types and cannot enforce constraints (explaining why semantic_only achieves only ↓24% vs full_s1 ↓94%). This is NOT \"synergistic\" (mutual amplification) — grammar is a prerequisite for semantic, not vice versa.\n\nThe two layers compose via bitwise AND of token masks. Recommended framing: \"Grammar and semantic constraints compose via bitwise AND with an enabling dependency: grammar ensures structural validity, enabling semantic constraints to enforce domain/range rules. When constraint tightness creates empty intersection between layers, the system degrades gracefully to grammar-only constraints, maintaining structural validity as a guaranteed floor.\"\n\n**Graceful degradation + Fallback 频率量化** (D008 + Reviewer 发现):\nWhen $M_{semantic} \\cap M_{grammar} = \\emptyset$, the system falls back to grammar-only control.\n\n**关键量化数据（Reviewer 从日志挖掘）**:\n- Llama DocRED full_s1: **32,921 次 fallback / 577 docs = ~57 次/doc**\n- Llama SciERC full_s1: **5,882 次 fallback / 550 docs = ~10.7 次/doc**\n- DocRED fallback 频率是 SciERC 的 **5.3×**\n- Qwen DocRED fallback 率未知（日志当时无 fallback logging，需估算）\n\n**这直接解释了 DocRED DR 残余 10.19% vs SciERC 0.93%**: 更多 token 位置退化为 grammar-only → grammar-only 的 DR 已知为 26.17% → 高 fallback = 高残余 DR。\n\n**论文建议**: 在 §5 tightness 段报告 fallback 率，定义 \"Constraint Coverage\" 指标（semantic masking 实际生效的 token 比例）。这把 \"10.19% DR 残余\" 从弱点变成可量化分析的 finding。Frame as \"engineering robustness\" in §4; fallback 频率 + tightness 作为 §5 定量分析。\n\n**Decidability taxonomy**: Constraints classified by prefix-decidability:\n- (a) Purely local: entity type ∈ vocabulary (grammar layer)\n- (b) Prefix-decidable with state: relation argument types compatible with domain/range (semantic layer, requires entity registry)\n- (c) Truly non-local: forward coreference — out of scope for forward-only decoding\n\n### Claim 4 (Methodological): S1 vs S2 Decoding Strategies — Architectural Ablation\n- S1 (single-pass): Both layers applied throughout generation. **Recommended primary strategy** — simpler, slightly better metrics across the board.\n- S2 (two-pass): Pass 1 extracts entities (grammar-only), Pass 2 generates relations with input-dependent grammar compiled from Pass 1 entities.\n\n**S2 full results (551/551 SciERC)**: DR 0.97% (vs S1 0.93%), CF 8.03% (vs S1 9.9%), R-F1 8.03% (vs S1 8.36%). S2 does NOT solve CF — the 1.87pp reduction is not significant. S2 also slightly worse on DR and F1. **S2 is an architectural variant demonstrating framework flexibility, not a CF solution.** Position in paper as ablation (Section 5 or Appendix), not as a core contribution.\n\n⚠️ **Do NOT cite pilot50 DR=0% as S2 evidence** — small-sample artifact; full run shows DR=0.97%. Per-relation S2 DR is worse than S1 on Compare (4.6% vs 2.82%), Part-of (1.25% vs 0%), Used-for (0.12% vs 0%).\n\n### Claim 5 (Empirical): Cross-Task Generalization — Event Extraction (D040, NEW)\n**Status**: ✅ All 3 models × 246 docs complete (v3 with collision fix + exact-match fix)\n\nOntoCoDec generalizes beyond Relation Extraction to **Event Extraction** (WikiEvents, Li et al. NAACL 2021), demonstrating that the framework is task-agnostic for any IE task with ontology-defined type constraints.\n\n**Cross-task framing (Reviewer 评估 confirmed)**:\n- **RoV 是 DR 的正确对应物**（不是 RV）：EE 中 per-type violation rate 是 RE 的 3-5×，支持 \"more complex ontology → more critical constraint enforcement\" claim\n- **三层级联 Grammar→RoV→AC**（比 RE 的 Grammar→DR 两层更丰富）：grammar 消除 EV，使 semantic layer 可以 enforce role restriction (RoV→0%)，进而暴露 AC violations。这强化 architecture contribution 论证。\n- **Semantic layer 是 EE 的唯一防线**：grammar 层对 role vocabulary 无能力，只有 semantic layer + continuation masking 能 enforce per-event-type role constraints\n- **\"Practical value\" 防线**：Arg F1 ≈ 0% 不削弱 claim，因为 (a) mechanism generalization 是 contribution 不是 SOTA performance，(b) FT composability 已在 RE 中证明 high-F1 场景有效\n\n**WikiEvents specifics** (DARPA KAIROS ontology):\n- 56 event types × 80 argument roles × 27 entity types（含 5 个补充 Contact 子类型 + CRM entity type）\n- 245 组显式 (event_type, role) → allowed_entity_types 约束\n- Maps directly to OntoCoDec's semantic layer: argument role type constraints ≡ domain/range constraints\n- 27 entity types（比 ACE05 的 7 个更丰富）→ constraint space 更大，更能展示 semantic layer 价值\n- 99.98% 数据满足约束 → 约束定义是真实有效的\n- Hierarchical event names (e.g., Conflict.Attack.DetonateExplode) → 扁平化为 leaf-node 解决 first-token collision（96.1%→3.9%）\n\n**数据集选择理由**（MAVEN/RAMS 排除）：\n- MAVEN (168 types): 无 argument extraction，不适用\n- MAVEN-Arg (162 types): FrameNet-based，无 role→entity_type schema 约束\n- RAMS (139 types): 仅 cardinality 约束，无 entity type binding\n- ACE05 (33 types): LDC 付费，采购周期来不及\n- **WikiEvents 是唯一同时满足 \"免费 + 有显式 role→entity_type 约束\" 的数据集**\n\n**Violation 分类** (5 类，从 RE 的 4 类扩展):\n- ET (Entity Type): entity type 不在 ontology 合法类型列表中\n- EV (Event Vocabulary): event type 不在 ontology 定义中\n- RoV (Role Vocabulary): argument role 不在该 event type 定义中\n- AC (Argument Constraint): argument entity type 不满足 role→entity_type 约束（DR 的自然推广）\n- CF (Cross-Field): 同一 entity 跨 event 被赋予不同 type\n\n**Full results (246 docs, v3 final — collision fix + exact-match fix)**:\n\n| Metric | Qwen3-8B uncon. | Qwen3-8B Full S1 | Llama-3.1-8B uncon. | Llama-3.1-8B Full S1 | Mistral-7B uncon. | Mistral-7B Full S1 |\n|--------|-----------------|-------------------|---------------------|----------------------|-------------------|---------------------|\n| Parse | 88.6% | 83.7% | 91.9% | 84.1% | 88.6% | 88.6% |\n| EV | 24.0% | **0%** | 10.5% | **0%** | 37.3% | **0%** |\n| RoV | 74.9% | **0%** | 88.8% | **0%** | 63.9% | **0%** |\n| AC | 0.3% | 2.1% | 0.1% | 3.8% | 0% | 1.3% |\n| CF | 0% | 21.1% | 0% | 17.2% | 0% | 14.9% |\n| Trigger F1 | 11.8% | 13.4% | 5.7% | 7.5% | 2.4% | 3.9% |\n| Ent F1 | 0% | 14.1% | 0% | 17.6% | 0% | 11.7% |\n\n**Grammar-only ablation (Mistral v3, all 3 models)**:\n- Grammar eliminates EV→0% but RoV remains 64-77%: grammar CFG cannot constrain 80 argument roles conditioned on event context\n- AC rises to 8-14% under grammar-only (latent violation surfacing pattern, same as DocRED RE)\n- Proves semantic layer is essential for EE: two-layer architecture is necessary, not just convenient\n\n**Post-hoc filtering comparison (devastating)**:\n- Qwen: 5,467→23 arguments (99.6% discarded) to reach 0% violation\n- Llama: 5,053→3 arguments (99.9% discarded)\n- Mistral: 6,034→0 arguments (100% discarded)\n- Post-hoc is not viable for EE (contrasts with RE where it's expensive but functional)\n\n**BPE collision diagnostic (confirmed 2026-05-18)**:\n- Qwen (BPE, ~152K vocab): **0 collision groups** — all 27 entity types have unique first tokens\n- Llama (BPE, ~128K vocab): **0 collision groups** — same\n- Mistral (SentencePiece, ~32K vocab): **2 collision groups** (SID/SEN/SIDE→'S', BAL/BOD→'B')\n- **Residual AC narrative**: Mistral AC 1.3% = residual after collision fix (was 16.6%); Qwen/Llama AC 2.1-3.8% = purely model semantic confusion (confuses similar entity types like SID vs SEN), NOT tokenizer collision\n\n**关键 findings**:\n- RoV 是压倒性违规（64-89%），远超 RE 的 RV（1-30%）→ 更强力展示 constraint 需求\n- EV 显著（10-37%）→ grammar 层直接消除\n- **Entity F1 从 0% 恢复到 11.7-17.6%**: 不是语义改进，是 format compliance 恢复——grammar enforcement 产生 schema-valid JSON，parser 才能识别 entity mentions\n- Trigger F1 +1.5 to +1.8pp: elimination of OOV event types counted as FP\n- CF 15-21% 比 RE 更高（EE argument structure 更复杂），沿用 RE 的 CF tradeoff framing\n\n**Story upgrade**: WikiEvents results confirm paper narrative: \"universal ontology-constrained structured generation framework applicable to any IE task with formal type constraints\". Three evidence lines: (1) EV/RoV→0% across all models, (2) grammar-only ablation proves two-layer necessity, (3) post-hoc filtering is non-viable for EE. This is the key differentiator for conference main vs Findings.\n\n**70B scale experiment** (P029-P030, in progress): Qwen3-70B AWQ-INT4 on SciERC + DocRED to demonstrate scale generalization. If successful, adds a 4th model to cross-model evidence, strengthening C5.\n\n**Remaining risk**:\n- CF 15-21% higher than RE → continues CF tradeoff framing\n- 70B experiment timeline tight (need results by May 20 for paper integration)\n\n## Anticipated Reviewer Concerns\n\n### C1: \"5.78% is barely above 5% — threshold is arbitrary\"\n**Response**: Don't argue about the threshold. Argue about per-relation distribution: Compare (27.6%), Evaluate-for (29.9%), Feature-of (11.3%) have double-digit violation rates with schema-informed prompt. The value proposition is per-relation guaranteed compliance, not overall statistical rate.\n\n### C2: \"Why not just post-hoc filter?\"\n**Response (D013, 实验结果已出)**:\n\nPost-hoc filtering 实验结果：post-hoc F1 > OntoCoDec F1（SciERC 8.63 vs 8.36, DocRED 9.61 vs 8.24）——因 low F1 regime 下移除 FP 大幅提升 precision。\n\n**论文 framing（不以 F1 论高低，多维对比）**:\n1. **Recall 维度（核心论点）**: OntoCoDec recall 上升 (SciERC +0.20pp, DocRED +0.56pp) = 概率质量重分配到合法 token 生效。Post-hoc recall 下降 (SciERC -0.72pp, DocRED -1.06pp) = 正确 triple 被误删。\n2. **Information coverage**: DocRED post-hoc 丢弃 **48.1%** triples（近半数信息丢失），SciERC 16.8%。OntoCoDec 保留全部 triple slots。\n3. **Operational**: OntoCoDec 产出即合规、无需后处理、支持流式。Post-hoc 需额外管线、不适用实时场景。\n4. **Precision trade-off（诚实承认）**: \"Post-hoc achieves higher precision by removing a large fraction of triples, many of which are incorrect. This trades information coverage for precision — valid when FP are costly, but inadequate when completeness matters.\"\n\n数据表：SciERC post-hoc rejection 16.8%, OntoCoDec recall 11.60 vs post-hoc 10.68; DocRED post-hoc rejection 48.1%, OntoCoDec recall 10.02 vs post-hoc 8.40。\n\n**Reviewer 补充发现（D013 后）**:\n5. **ET 残余**：post-hoc 只删 triples 不改 entity list，残余 ET=0.4% (SciERC) / 2.47% (DocRED)。OntoCoDec ET=0%。Post-hoc 无法解决 entity type 违规。\n6. **127 个被删 TP (DocRED)**：过滤前 TP=1137，过滤后 TP=1010。丢失的 127 个 TP（11.2%）是正确提取但 entity type 违规的 triple。OntoCoDec 通过生成时强制合法 type 保留这些 TP——\"prevent vs detect\" 核心论据的具体数据。\n7. **OntoCoDec+post-hoc 组合**（future work idea）：先 constrain 再 filter 残余 DR。低优先级，May 19 前不做。\n\n### C3: \"Bitwise AND of two masks is not novel\"\n**Response**: The novelty is not the AND operation — it's (a) the automatic compilation from ontology definitions (zero-code schema compliance), (b) the stateful entity registry enabling cross-field constraints during autoregressive generation, (c) the decidability taxonomy providing theoretical guidance, and (d) the systematic violation landscape measurement motivating the approach.\n\n### C4: \"Evaluate-for violation rate increases with schema-informed prompt\"\n**Response (prior-constraint conflict framework)**: Evaluate-for has 23/36 valid pairs; Method→Task is invalid for Evaluate-for but natural in the LLM's distributional prior (\"Method X evaluates for Task Y\" is semantically plausible). Schema-informed prompting creates a **prior-constraint conflict**: the model learns to avoid Method→Task for Evaluate-for (reducing count 133→87, -34.6%), but the remaining instances are harder boundary cases where the model's type assignment strategy becomes less stable. This is not just \"harder instances\" — it's an active interference between prompt-level constraint signals and the model's learned type associations.\n\n**This strengthens the paper's claim**: prompt-level intervention is not merely insufficient but potentially **counterproductive** for specific constraint configurations. Decoding-time enforcement avoids this issue entirely — it operates on logits, not on the model's reasoning process, so there is no prior-constraint conflict.\n\n### C5: \"Only tested on one model (Qwen3-8B)\"\n**Response**: Cross-model validation DONE (D016 bootstrap verified). Llama-3.1-8B 零代码修改：\n- SciERC: DR 13.34%→0.08% (↓99.4%), R-F1 -0.14pp (p=0.011, negligible), E-F1 NS\n- DocRED: DR 26.07%→2.55% (↓90.2%), R-F1 +0.29pp (p=0.013, significant), E-F1 -0.64pp (p=0.022, modest decline)\n- Parse failures: unconstrained 68 vs full_s1 91 (6.8% vs 9.1%)\n\n**Cross-model claim 指导（Reviewer 专项评估）**:\n- ✅ 可声明：\"OntoCoDec generalizes across model families without code modification\"（程序性事实，铁证）\n- ❌ 不可声明：\"consistently achieves the same reduction rate\"（仅 2 模型，不足以量化声明）\n- **RV↓DR↑ 正交性 finding**: Llama RV baseline 低(16%) 但 DR baseline 高(26%)，反向于 Qwen。证明两层约束解决正交 failure modes——vocabulary compliance ≠ semantic compliance。应作为 §5 cross-model 独立 finding 展开。\n- **Parse failure 偏差**: checker skip parse failures (不计入 F1)，Llama 68/998=6.8% vs Qwen 12/998=1.2%。偏差方向保守（不利于 constrained），不威胁 claim。但需 footnote 披露 + cross-model 表增加 parse failure rate 行。\n- **Llama SciERC CF=6.56%**: 比 Qwen 同量级更高，non-local constraint 问题在 Llama 上更突出，limitations 提及。\n- 等 llama_docred_full_s1 出来后定最终 claim 措辞。\n\n### C6: \"Constrained decoding degrades generation quality (CRANE, Structure Snowballing)\"\n**Response**: OntoCoDec's semantic constraints are narrower than full grammar constraints — only type tokens are masked, free text is unconstrained. **Bootstrap CI (10000×, D012 Qwen + D016 Llama, all registry-aligned)**:\n\n**Qwen3-8B**: SciERC R-F1 +0.13pp (p=0.58, NS), E-F1 -0.03pp (NS). DocRED R-F1 +0.50pp (p<0.001), E-F1 +1.23pp (p<0.001).\n**Llama-3.1-8B**: SciERC R-F1 -0.14pp (p=0.011, negligible), E-F1 NS. DocRED R-F1 +0.29pp (p=0.013), E-F1 -0.64pp (p=0.022).\n\n**Cross-model pattern**: DocRED R-F1 显著提升（两个模型）。E-F1 model-dependent（Qwen +1.23pp, Llama -0.64pp）。\n- 机制：grammar 消除 OOV relation names + 非标 entity types → all_set 方法下减少 FP → precision 提升。Grammar 是 F1 提升的唯一来源（grammar_only Ent F1=59.38% ≈ full_s1 59.37%, Δ=0.01pp, p=0.66）。Semantic 层对 F1 无额外贡献。\n- Frame as: \"On DocRED, R-F1 gains are significant for both models. Entity F1 impact is model-dependent.\"\n- 不升级为 core claim，但如实报告。\n\n### C7: \"Your method trades DR violations for CF violations (cross-field consistency)\"\n**Response**: Both S1 and S2 show elevated CF (per-triple rate ~8-10%). This is an inherent limitation of per-relation independent type enforcement. Must be proactively reported as a limitation. Defense:\n\n**CF 子类型分析（根因已确认）**：\n- **EVR（entity-vs-relation type drift）**: 占 CF 的 >90%。同一 entity 在 entity list 和 relation triple 中被赋予不同 type。S1: 245 entities (7.34%), S2: 178 entities (5.54%, -27%)\n- **Within-rel（同 entity 跨 relation type 不一致）**: S1: 10 (0.36%), S2: 18 (0.72%)\n- S2 减少 EVR 但增加 within-rel——trade-off 更复杂，不是单纯好/差\n\n**Top 冲突模式**: Generic↔OtherScientificTerm (60次), Material↔OtherScientificTerm (28次), Material↔Method (20次)。**这些是 SciERC type system 固有的语义边界模糊区**——同一术语在不同学术语境下确实可以被合理归类为不同 type。CF 在相当程度上是 type system 模糊性的体现，非纯粹的方法缺陷。\n\n**论证层次**：\n1. DR violations = structurally invalid triples（下游系统不可用）→ hard constraint\n2. CF violations = same entity gets different types across relations → individual triples remain type-valid, only cross-triple consistency broken → soft preference\n3. CF 的根因是 type system 语义边界模糊 + per-relation 独立 enforcement，非 bug\n4. Future work: cross-relation global consistency pass (entity-level type consensus before relation-specific enforcement)\n\n**机制归因（口径对账确认）**：grammar_only CF=0.08%（与 unconstrained 持平），full_s1 CF=9.90%，full_s2 CF=8.03%。**CF 100% 由 semantic 层引入，grammar 层无贡献。** 这为 \"CF 是 semantic type enforcement 的系统性副作用\" 提供干净的消融证据。\n\n**论文数字口径**：CF rate 用 violation_checker 口径（denominator=total_entities，与 DR/RV/ET 一致）。分析段落额外给 entity-level EVR 率 + 受影响样本比例。注意：analyze_cf 脚本的 EVR/WR 两维度不是独立的（WR⊂EVR），论文中不要作为两个独立维度报告。\n\n**Do NOT hide this data.** Proactive disclosure + severity distinction + root cause analysis + type ambiguity evidence + 消融归因 = 最强防御策略。\n\n### C8: \"Absolute F1 is too low (~8%) — results are not meaningful\"\n**Response**: This is a zero-shot extraction setting (no training data, no fine-tuning). Low F1 is expected — supervised SOTA on SciERC relation F1 is ~40-50%. Our contribution is the constraint enforcement method, not extraction quality. F1 is a control variable verifying constraints don't degrade quality, not an optimization target. Recommended framing: \"We evaluate in a zero-shot setting to demonstrate that our constraint enforcement method works without task-specific training. F1 is reported to verify that constraint enforcement does not degrade extraction quality, not as a claim of state-of-the-art performance.\"\n\n## Paper Structure (Draft — D040 updated)\n1. Introduction: Ontology constraint violations in LLM-based structured generation + composable framework overview (story: not just RE, general ontology-constrained generation)\n2. Background: Grammar-constrained decoding (XGrammar) + IE ontology structure\n3. Violation Landscape Study (Phase 0 empirics — independent contribution)\n4. OntoCoDec Framework: Compiler + TypeConstraintProcessor + S1/S2 strategies\n5. Experiments:\n   - §5.1-5.3: RE experiments (SciERC + DocRED, 3 models, constrained vs unconstrained vs post-hoc vs prompt-based)\n   - §5.4: **Event Extraction (WikiEvents)** — cross-task generalization (D040)\n   - §5.5: Ablation + analysis (composability, latency, beam search, etc.)\n6. Related Work: 5 constraint paradigms (grammar, vocabulary, structural, type-checking, ontology) + event extraction methods\n7. Conclusion: Framework generality across IE tasks\n\n## Claim Calibration (per Reviewer assessment)\n\n**Safe to claim (sufficient evidence from Phase 2)**:\n- \"First systematic study of ontology constraint violations in LLM-based IE\"\n- \"Violation rate correlates with constraint tightness, not ontology size\" (D014: DR reduction ceiling 由 tightness × model RV baseline 共同决定)\n- \"Grammar+semantic constrained decoding eliminates 94% of DR violations at zero F1 cost\" ✅ Phase 2 confirmed\n- \"Two-layer architecture provides complementary coverage — grammar enables semantic\" ✅ Ablation confirmed\n- \"Prompt-level intervention scales poorly with ontology complexity\" ✅ SciERC ↓62% vs DocRED ↓32%\n\n**Claim with caution**:\n- \"Near-complete type-valid IE\" — S1 0.93%, S2 0.97% residual, not truly 0%. Title updated to \"Near-Complete\"\n- \"Principled framework applicable to arbitrary IE ontologies\" — RE validated on 2 datasets × 2 models; EE (WikiEvents) 10-doc preliminary shows ↓95.8% semantic violations, full results pending\n- \"F1 improvement\" — SciERC: not significant (p=0.58), frame as F1-neutral; DocRED: significant (+0.50pp, p<0.001), 可报告但不升级为 core claim，归因于 OOV elimination 而非约束解码本身的提升\n- \"CF reveals type system ambiguity\" — 可在 §5.3 作为 analysis finding 展开（Generic↔OtherScientificTerm 等模式有独立 insight 价值），但 §7 必须同时保留 CF 作为 limitation + future work。**两处都要有，缺一不可。** 不能暗示\"因为是 type ambiguity 所以 CF 可接受\"\n\n**Do NOT claim**:\n- \"General infrastructure for IE\" — only zero-shot extraction validated\n- \"State-of-the-art\" — F1 is control variable, not optimization target (see C8)\n- \"Synergistic effect\" — mechanism is enabling dependency, not mutual amplification (see Claim 3)\n- \"S2 solves CF\" or \"S2 mitigates Structure Snowballing\" — data shows S2 ≈ S1 on all metrics; position as architectural variant only\n- \"Pilot50 DR=0%\" — small-sample artifact, full S2 has DR=0.97%\n- \"Grammar-first invariant\" 作为独立 claim — 证据不足（仅 1 次崩溃触发，实现是 fallback 非形式化保证）。写入 §4 方法论设计原则（1-2 句），不升级为 claim\n- \"Robust dual-layer composition across schema complexities\" — 等 DocRED 完成。最终如 fallback ≤5/998，可写经验性陈述，不做泛化 claim\n\n## Risk Ranking (ordered by reject probability)\n\n1. **CF violation trade-off under-addressed** (MEDIUM-HIGH): S1 9.9%, S2 8.03% — both elevated. **S2 confirmed: does NOT solve CF.** This is the #1 attack surface. Mitigated by proactive disclosure + severity distinction + root cause analysis (C7). Must be reported as explicit limitation with future work direction (global entity-type consensus).\n2. ~~**Single model limitation**~~ (RESOLVED): Llama-3.1-8B SciERC ✅ (DR↓99.4%) + DocRED ✅ (DR↓90.2%). 2 模型 × 2 数据集全矩阵完成。\n3. **Novelty perception** (MEDIUM): \"PLDI'25 for code → OntoCoDec for IE\" attack line. Must argue IE constraint structure differs fundamentally.\n4. ~~**DocRED Phase 2 weak**~~ (RESOLVED → reframed as D014): Qwen DR↓44.7%, Llama DR↓90.2% — both substantial. Weaker Qwen reduction explained by RV baseline interaction (D014), not method failure.\n5. ~~**Phase 2 F1 drop**~~ (RESOLVED): F1 confirmed neutral (SciERC) or positive (DocRED, p<0.001). Bootstrap CI D012 confirms. No longer a risk.\n\n## Critical Path to EMNLP Submission (May 25)\n\n- **May 13-14**: Phase 0 + Phase 1 + Phase 2 SciERC ✅\n- **May 14**: Phase 2 DocRED 4-way ablation ✅ + Llama SciERC cross-model ✅ + Dream 完成 (3/6)\n- **May 14-15**: Llama DocRED ✅ + Checker 修正 ✅ + post-hoc ✅ + bootstrap CI ✅ + related work ✅\n- **May 15-17**: Prompt sensitivity ✅ + WikiEvents pipeline 开发 + continuation v2 突破\n- **May 17-18**: WikiEvents 3 模型 unconstrained baselines (进行中) + constrained 全量\n- **May 18-19**: WikiEvents 结果分析 + §5.4 Event Extraction 章节撰写\n- **May 19-20**: Intro/Abstract/Conclusion 升级（cross-task story）+ 内部稿 → submit_paper_to_review\n- **May 20-24**: Review 修改 + 最终提交\n\n**当前瓶颈**: WikiEvents 全量实验完成是关键路径。3 模型 unconstrained baselines 并行进行中（Qwen ~68/246, Mistral ~31/246, Llama 重启中），constrained 实验随后立即启动。\n\n## Status\n- Phase 0 SciERC: ✅ Complete (minimal + schema-informed)\n- Phase 0 DocRED: ✅ Complete (minimal 18.7% DR + schema-informed 12.8% DR)\n- Phase 1 Compiler: ✅ Complete (grammar + semantic layers integrated)\n- Phase 2 SciERC (5 configs): ✅ Complete (S1 DR↓94% F1-neutral, S2 降级为 ablation)\n- Phase 2 DocRED (4 configs): ✅ Complete (full_s1 DR↓45%, grammar ET/RV→0%)\n- Llama SciERC cross-model: ✅ Complete (DR↓99.4%, F1-neutral, 零代码修改)\n- Llama DocRED cross-model: ✅ Complete (full_s1 DR↓90.2%, unconstrained DR=26.07%)\n- Checker v2 (D011): ✅ Fixed (ET triple-counting → unique entity dedup)\n- Bootstrap CI (D012): ✅ Fixed + confirmed (entity filter bug resolved)\n- Post-hoc baseline (D013): ✅ Complete (multi-dimensional framing)\n- Related work: ✅ 42 bib entries, 4 additions merged\n- Dream 6/6 actions: ✅ All complete\n- CF violation analysis: ✅ Confirmed inherent limitation (S1 9.9% SciERC / 2.57% DocRED / 12.02% Llama DocRED)\n- D014 tightness revision: ✅ Complete (tightness × RV baseline dual-factor)\n- Llama bootstrap CI (D016): ✅ Fixed + verified (registry-aligned ≤0.05pp, all p-values in paper)\n- Paper compilation: ✅ 8 pages正文 + appendix\n- R5 text fixes (N1/N2/N3/W1-W6): ✅ All complete and verified\n- Prompt sensitivity analysis: ✅ Complete (3 prompts × 2 modes, DR reduction 94.0-94.6%, σ=0.3pp; appendix written)\n- Doc length breakdown: ✅ Complete (appendix written)\n- **WikiEvents Event Extraction (D040)**: 🔄 Continuation v2 突破 (10-doc: RoV 0%, semantic ↓95.8%); 3 模型 unconstrained baselines 进行中; constrained 全量待启动\n\n\n## registry (completed experiments)\n\n- exp_id: mvp_phase0_violation_rate\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_triples: 1724\n    total_entities: 2474\n    json_parse_rate: 1\n    entity_type_violation_rate: 0.004\n    relation_vocabulary_violation_rate: 0.0139\n    domain_range_violation_rate: 0.1537\n    cross_field_consistency_violation_rate: 0.0008\n    go_nogo_metric: 0.1537\n    entity_f1: 0.3101\n    relation_f1: 0.0823\n    per_relation:\n      Used-for:\n        total: 787\n        dr_violations: 6\n        rate: 0.0076\n      Conjunction:\n        total: 32\n        dr_violations: 0\n        rate: 0\n      Hyponym-of:\n        total: 124\n        dr_violations: 18\n        rate: 0.1452\n      Evaluate-for:\n        total: 133\n        dr_violations: 32\n        rate: 0.2406\n      Part-of:\n        total: 72\n        dr_violations: 18\n        rate: 0.25\n      Feature-of:\n        total: 486\n        dr_violations: 163\n        rate: 0.3354\n      Compare:\n        total: 66\n        dr_violations: 28\n        rate: 0.4242\n- exp_id: mvp_phase0_violation_rate_docred\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_docs: 998\n    parsed_docs: 962\n    json_parse_rate: 0.964\n    total_entities: 19099\n    total_triples: 16540\n    entity_type_violation_rate: 0.075\n    relation_vocabulary_violation_rate: 0.289\n    domain_range_violation_rate: 0.187\n    cross_field_consistency_violation_rate: 0.0008\n    go_nogo_metric: 0.187\n    fuzzy_matches: 126\n    top_dr_violations_by_rate:\n      P35_head_of_state: 1\n      P710_participant: 0.919\n      P172_ethnic_group: 0.875\n    top_dr_violations_by_count:\n      P31_instance_of:\n        violations: 322\n        total: 533\n        rate: 0.604\n      P1001_applies_to_jurisdiction:\n        violations: 264\n        total: 594\n        rate: 0.444\n      P1344_participant_in:\n        violations: 194\n        total: 312\n        rate: 0.622\n- exp_id: mvp_phase0_scierc_schema\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    domain_range_violation_rate: 0.0578\n    relation_vocabulary_violation_rate: 0.003\n    entity_type_violation_rate: 0\n    total_violation_rate: 0.0253\n    go_nogo_metric: 0.0578\n    total_triples: 1661\n    vs_minimal_dr_reduction: -0.624\n    per_relation:\n      Used-for:\n        rate: TBD\n      Feature-of:\n        delta_pp: -22.3\n      Part-of:\n        delta_pp: -22.5\n      Compare:\n        delta_pp: -14.8\n      Evaluate-for:\n        delta_pp: 5.8\n    mcnemar_all_significant: true\n- exp_id: mvp_phase0_docred_schema\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_documents: 998\n    documents_checked: 943\n    parse_failures: 55\n    json_parse_rate: 0.9449\n    total_entities: 19524\n    total_triples: 16782\n    entity_type_violations: 119\n    entity_type_violation_rate: 0.0061\n    relation_vocabulary_violations: 3090\n    relation_vocabulary_violation_rate: 0.1841\n    relation_fuzzy_matches: 85\n    domain_range_violations: 2154\n    domain_range_violation_rate: 0.1284\n    cross_field_consistency_violations: 29\n    cross_field_consistency_violation_rate: 0.0015\n    total_violations_any: 5392\n    total_violation_rate: 0.1485\n    go_nogo_metric_dr: 0.1284\n- exp_id: phase2_scierc_grammar_only\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_samples: 551\n    total_triples: 1725\n    total_entities: 2474\n    json_parse_rate: 1\n    entity_type_violation_rate: 0\n    relation_vocabulary_violation_rate: 0\n    domain_range_violation_rate: 0.1484\n    cross_field_consistency_violation_rate: 0.0008\n    entity_f1: 0.3098\n    entity_precision: 0.2598\n    entity_recall: 0.3837\n    relation_f1: 0.0823\n    relation_precision: 0.0643\n    relation_recall: 0.114\n    checker_version: fixed_20260514_v2 (strip + alias + unique_et)\n- exp_id: phase2_scierc_semantic_only\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_samples: 551\n    total_triples: 1726\n    total_entities: 2474\n    json_parse_rate: 1\n    entity_type_violation_rate: 0.004\n    relation_vocabulary_violation_rate: 0.0151\n    domain_range_violation_rate: 0.1165\n    cross_field_consistency_violation_rate: 0.0271\n    entity_f1: 0.3101\n    entity_precision: 0.2605\n    entity_recall: 0.3831\n    relation_f1: 0.0815\n    relation_precision: 0.0637\n    relation_recall: 0.1129\n    checker_version: fixed_20260514_v2 (strip + alias + unique_et)\n- exp_id: phase2_scierc_full_s1\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_samples: 551\n    total_triples: 1729\n    total_entities: 2474\n    json_parse_rate: 1\n    entity_type_violation_rate: 0\n    relation_vocabulary_violation_rate: 0\n    domain_range_violation_rate: 0.0093\n    cross_field_consistency_violation_rate: 0.099\n    entity_f1: 0.3098\n    entity_precision: 0.2598\n    entity_recall: 0.3837\n    relation_f1: 0.0836\n    relation_precision: 0.0654\n    relation_recall: 0.116\n    checker_version: fixed_20260514_v2 (strip + alias + unique_et)\n- exp_id: phase2_scierc_unconstrained\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    json_parse_rate: 1\n    entity_f1: 0.3101\n    entity_precision: 0.2605\n    entity_recall: 0.3831\n    relation_f1: 0.0823\n    relation_precision: 0.0644\n    relation_recall: 0.114\n    entity_type_violation_rate: 0.004\n    relation_vocabulary_violation_rate: 0.0139\n    domain_range_violation_rate: 0.1537\n    cross_field_consistency_violation_rate: 0.0008\n    total_triples: 1724\n    total_entities: 2474\n    total_samples: 551\n    checker_version: fixed_20260514_v2 (strip + alias + unique_et)\n- exp_id: phase2_s2_pilot50\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    domain_range_violation_rate: 0.0205\n    relation_vocabulary_violation_rate: 0\n    relation_f1: 0.1008\n    samples: 50\n    predicted_relations: 146\n    true_positives: 13\n    gold_relations: 112\n    entity_f1_approx: 0.29\n    note: 'DR 修正: 原值 0 来自 dryrun (n=25 triples)。实际 pilot50 DR=3/146=2.05% (来自 violation_report_s2_pilot50.json)。'\n- exp_id: mvp_phase0_docred_schema_r2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: phase2_scierc_full_s2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_samples: 551\n    total_triples: 1644\n    total_entities: 2228\n    json_parse_rate: 1\n    entity_type_violation_rate: 0\n    relation_vocabulary_violation_rate: 0\n    domain_range_violation_rate: 0.0097\n    cross_field_consistency_violation_rate: 0.0803\n    entity_precision: 0.2797\n    entity_recall: 0.3712\n    entity_f1: 0.319\n    relation_precision: 0.064\n    relation_recall: 0.1078\n    relation_f1: 0.0803\n    checker_version: fixed_20260514_v2 (strip + alias + unique_et)\n- exp_id: phase2_docred_grammar_only\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    documents_checked: 985\n    parse_failures: 13\n    total_entities: 20150\n    total_triples: 17341\n    entity_type_violation_rate: 0\n    relation_vocabulary_violation_rate: 0.0003\n    domain_range_violation_rate: 0.2617\n    cross_field_consistency_violation_rate: 0.0007\n    relation_f1: 8.31\n    relation_precision: 7.06\n    relation_recall: 10.12\n    entity_f1: 59.38\n    entity_precision: 58.47\n    entity_recall: 60.32\n    unrecognized_relations: 5\n    f1_method: all_set\n    checker_version: fixed_20260514_v2 (strip + alias + unique_et)\n- exp_id: phase2_docred_full_s1\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    documents_checked: 987\n    parse_failures: 11\n    total_entities: 20187\n    total_triples: 17341\n    entity_type_violation_rate: 0\n    relation_vocabulary_violation_rate: 0.0003\n    domain_range_violation_rate: 0.1021\n    cross_field_consistency_violation_rate: 0.0257\n    entity_f1: 59.37\n    entity_precision: 58.45\n    entity_recall: 59.63\n    relation_f1: 8.23\n    relation_precision: 6.99\n    relation_recall: 10.01\n    unrecognized_relations: 5\n    f1_method: all_set\n    checker_version: fixed_20260514_v2 (strip + alias + unique_et)\n- exp_id: phase2_docred_unconstrained\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    documents_checked: 986\n    parse_failures: 12\n    total_entities: 20171\n    total_triples: 17497\n    entity_type_violation_rate: 0.0248\n    relation_vocabulary_violation_rate: 0.2966\n    domain_range_violation_rate: 0.1846\n    cross_field_consistency_violation_rate: 0.001\n    entity_f1: 58.15\n    entity_precision: 57.26\n    entity_recall: 58.32\n    relation_f1: 7.74\n    relation_precision: 6.55\n    relation_recall: 9.46\n    unrecognized_relations: 5189\n    f1_method: all_set (includes OOV predictions in denominator)\n    checker_version: fixed_20260514_v2 (strip + alias + unique_et)\n    et_v1: 0.0818\n    et_fix_note: v1 triple-counted ET across entity_list + relation head/tail; v2\n      deduplicates by (text, normalized_type)\n- exp_id: phase2_docred_semantic_only\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    documents_checked: 987\n    parse_failures: 11\n    total_entities: 20185\n    total_triples: 17571\n    entity_type_violation_rate: 0.0422\n    relation_vocabulary_violation_rate: 0.2987\n    domain_range_violation_rate: 0.1384\n    cross_field_consistency_violation_rate: 0.0105\n    entity_f1: 57.81\n    entity_precision: 57.27\n    entity_recall: 58.37\n    relation_f1: 7.7\n    relation_precision: 6.54\n    relation_recall: 9.37\n    f1_method: all_set\n    checker_version: fixed_20260514_v2 (strip + alias + unique_et)\n    et_v1: 0.1044\n    et_fix_note: v1 triple-counted ET across entity_list + relation head/tail; v2\n      deduplicates by (text, normalized_type)\n- exp_id: llama_scierc_unconstrained\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    entity_type_violation_rate: 0\n    relation_vocab_violation_rate: 0.0055\n    domain_range_violation_rate: 0.1334\n    cross_field_consistency_violations: 6\n    entity_f1: 0.2356\n    entity_precision: 0.1983\n    entity_recall: 0.2902\n    relation_f1: 0.0268\n    relation_precision: 0.0236\n    relation_recall: 0.031\n    total_entities: 2451\n    total_relations: 1274\n    json_parse_failures: 1\n    samples: 551\n    checker_version: fixed_20260514_v2 (strip + alias + unique_et)\n- exp_id: llama_scierc_full_s1\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    samples: 550\n    entities_extracted: 2469\n    relations_extracted: 1315\n    domain_range_violation_rate: 0.0008\n    relation_vocab_violation_rate: 0\n    entity_type_violation_rate: 0\n    cross_field_consistency_violation_rate: 0.0656\n    total_violation_rate: 0.0431\n    entity_f1: 0.2349\n    entity_precision: 0.1972\n    entity_recall: 0.2902\n    relation_f1: 0.0254\n    relation_precision: 0.0221\n    relation_recall: 0.0298\n    checker_version: fixed_20260514_v2 (strip + alias + unique_et)\n- exp_id: llama_docred_unconstrained\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    checker_version: fixed_20260514_v2\n    f1_method: all_set\n    documents: 998\n    documents_checked: 930\n    parse_failures: 68\n    unique_entities: 11525\n    total_triples: 16437\n    dr_eligible_triples: 13789\n    ET_rate_pct: 0.13\n    RV_rate_pct: 16.03\n    DR_rate_pct: 26.07\n    CF_rate_pct: 0.17\n    entity_precision: 61.22\n    entity_recall: 51.02\n    entity_f1: 55.65\n    relation_precision: 5.22\n    relation_recall: 7\n    relation_f1: 5.98\n    fuzzy_relation_matches: 121\n- exp_id: llama_docred_full_s1\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    checker_version: fixed_20260514_v2 (strip + alias + unique_et)\n    f1_method: all_set\n    violations:\n      ET: 0\n      RV: 0\n      DR: 2.55\n      CF: 12.02\n    f1:\n      entity_f1: 55.01\n      entity_precision: 61.41\n      entity_recall: 49.82\n      relation_f1: 6.27\n      relation_precision: 5.49\n      relation_recall: 7.32\n    counts:\n      documents: 998\n      documents_checked: 907\n      parse_failures: 91\n      unique_entities: 11296\n      triples: 16368\n- exp_id: posthoc_filtering_baseline\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    docred_f1_before: 7.74\n    docred_f1_after: 9.61\n    docred_precision_before: 6.55\n    docred_precision_after: 11.22\n    docred_recall_before: 9.46\n    docred_recall_after: 8.4\n    docred_rejection_rate: 0.481\n    docred_tp_before: 1137\n    docred_tp_after: 1010\n    docred_tp_lost: 127\n    docred_et_residual: 0.0247\n    scierc_f1_before: 8.23\n    scierc_f1_after: 8.63\n    scierc_rejection_rate: 0.168\n    scierc_recall_before: 11.4\n    scierc_recall_after: 10.68\n    scierc_tp_before: 111\n    scierc_tp_after: 104\n- exp_id: llama_docred_unconstrained_mt6144\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ET_rate: 0.13\n    RV_rate: 15.89\n    DR_rate: 26.18\n    DR_rate_eligible: 31.15\n    CF_rate: 0.17\n    entity_precision: 61.19\n    entity_recall: 51.06\n    entity_f1: 55.67\n    relation_precision: 5.18\n    relation_recall: 7\n    relation_f1: 5.95\n    parse_failures: 67\n    documents_checked: 931\n    total_documents: 998\n    unique_entities: 11534\n    total_triples: 16584\n    dr_eligible_triples: 13936\n    fuzzy_relation_matches: 121\n- exp_id: llama_docred_full_s1_mt6144\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    DR_rate_pct: 2.57\n    RV_rate_pct: 0\n    ET_rate_pct: 0\n    CF_rate_pct: 12.13\n    R_F1: 6.25\n    R_precision: 5.45\n    R_recall: 7.32\n    E_F1: 55.04\n    E_precision: 61.41\n    E_recall: 49.87\n    documents_total: 998\n    documents_checked: 908\n    parse_failures: 90\n    triples: 16471\n    unique_entities: 11307\n    fallback_events: 67911\n    wall_clock_seconds: 23926\n    vs_unconstrained_mt6144:\n      DR_delta_pp: -23.61\n      DR_reduction_pct: -90.2\n      R_F1_delta_pp: 0.3\n      E_F1_delta_pp: -0.63\n    vs_full_s1_mt4096:\n      DR_delta_pp: 0.02\n      R_F1_delta_pp: -0.02\n      E_F1_delta_pp: 0.03\n      CF_delta_pp: 0.11\n      parse_fail_delta: -1\n- exp_id: w1_cf_fallback_scierc_pilot\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    ET: 0\n    RV: 0\n    DR: 0.1478\n    CF: 0.0004\n    R_F1: 0.0823\n    R_P: 0.0643\n    R_R: 0.114\n    E_F1: 0.3098\n    E_P: 0.2598\n    E_R: 0.3837\n    entities: 2474\n    relations: 1725\n    samples: 551\n    grammar_first_fallback_rate: 0.3664\n    cf_registry_fallback_rate: 0.0448\n    total_mask_calls: 17024\n    violation_budget_DR_CF: 0.1482\n- exp_id: w1_cf_fallback_docred\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: w1_cf_fallback_llama_scierc\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: w1_cf_fallback_llama_docred\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: w5_lora_scierc_training\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 0.0634\n    eval_loss: 0.0586\n    eval_token_accuracy: 0.9816\n    eval_entropy: 0.9635\n    train_runtime_sec: 688.4\n    epochs: 3\n    checkpoint_path: /root/schema_semantic_constrained_ie/checkpoints/qwen3_8b_lora_scierc\n    merged_model_path: /root/schema_semantic_constrained_ie/checkpoints/qwen3_8b_lora_scierc_merged\n- exp_id: w5_lora_scierc_unconstrained_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    json_parse_rate: 1\n    entity_type_violation_rate: 0\n    relation_vocabulary_violation_rate: 0\n    domain_range_violation_rate: 0.0195\n    cross_field_consistency_violation_rate: 0\n    entity_f1: 0.6705\n    entity_precision: 0.6523\n    entity_recall: 0.6898\n    relation_f1: 0.4386\n    relation_precision: 0.4087\n    relation_recall: 0.4733\n    total_entities: 1784\n    total_relations: 1128\n    domain_range_violations: 22\n    go_nogo_metric: 0.0195\n    dr_gate: FAILED\n- exp_id: w5_lora_scierc_constrained_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    json_parse_rate: 1\n    entity_type_violation_rate: 0\n    relation_vocabulary_violation_rate: 0\n    domain_range_violation_rate: 0\n    cross_field_consistency_violation_rate: 0.0118\n    entity_f1: 0.6705\n    entity_precision: 0.6523\n    entity_recall: 0.6898\n    relation_f1: 0.4377\n    relation_precision: 0.4078\n    relation_recall: 0.4723\n    total_entities: 1784\n    total_relations: 1128\n    total_samples: 551\n    cross_field_consistency_violations: 21\n- exp_id: w5_llama_lora_scierc_training\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    eval_loss: 0.0595\n    eval_mean_token_accuracy: 0.9817\n    eval_entropy: 1.0565\n    train_loss: 0.0501\n    train_runtime_sec: 654.23\n    epochs: 3\n    train_samples_per_second: 8.08\n- exp_id: w5_llama_lora_scierc_unconstrained_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_samples: 551\n    total_entities: 1757\n    total_relations: 1082\n    json_parse_rate: 1\n    entity_type_violation_rate: 0\n    relation_vocabulary_violation_rate: 0\n    domain_range_violation_rate: 0.0111\n    cross_field_consistency_violation_rate: 0\n    total_violation_rate: 0.0042\n    entity_precision: 0.6647\n    entity_recall: 0.691\n    entity_f1: 0.6776\n    relation_precision: 0.432\n    relation_recall: 0.4795\n    relation_f1: 0.4545\n- exp_id: w5_llama_lora_scierc_constrained_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    domain_range_violation_rate: 0.0009\n    relation_vocabulary_violation_rate: 0\n    entity_type_violation_rate: 0\n    cross_field_consistency_violation_rate: 0.0046\n    relation_f1: 0.4547\n    relation_precision: 0.432\n    relation_recall: 0.4795\n    entity_f1: 0.6776\n    entity_precision: 0.6647\n    entity_recall: 0.691\n    total_relations: 1081\n    total_entities: 1757\n    total_samples: 551\n    parse_failures: 0\n- exp_id: w5_qwen_docred_lora_training\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    eval_loss: 0.0614\n    eval_mean_token_accuracy: 0.9804\n    eval_entropy: 0.715\n    train_loss: 0.0682\n    train_runtime_s: 5825.6\n    epochs: 3\n    adapter_path: /root/schema_semantic_constrained_ie/checkpoints/qwen_lora_docred\n    merged_path: /root/autodl-tmp/checkpoints/qwen_lora_docred_merged\n- exp_id: w5_docred_sft_data_gen\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_samples: 3053\n    dev_samples: 998\n    train_entities: 59493\n    train_relations: 38180\n    dev_entities: 19528\n    dev_relations: 12275\n- exp_id: w5_llama_docred_sft_data_gen\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_samples: 3053\n    dev_samples: 998\n    train_size_mb: 19\n    dev_size_mb: 6.1\n- exp_id: w5_llama_docred_lora_training\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 0.0572\n    eval_loss: 0.0624\n    token_acc: 98.06\n- exp_id: w5_llama_docred_lora_unconstrained_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ET_pct: 0\n    RV_pct: 0.15\n    DR_pct: 0.49\n    E_F1: 83.93\n    E_P: 84.93\n    E_R: 82.96\n    R_F1: 43.72\n    R_P: 38.59\n    R_R: 50.41\n    parse_fail_rate: 2.3\n    total_samples: 998\n    total_entities_pred: 19106\n    total_relations_pred: 16171\n- exp_id: w5_llama_docred_lora_constrained_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total: 998\n    parse_failures: 25\n    parse_fail_rate: 2.51\n    entities: 19077\n    relations: 16074\n    entity_f1: 83.94\n    entity_precision: 85\n    entity_recall: 84.13\n    relation_f1_all_set: 43.78\n    relation_precision_all_set: 38.79\n    relation_recall_all_set: 50.81\n    et_violations: 0\n    et_violation_rate: 0\n    rv_violations: 0\n    rv_violation_rate: 0\n    dr_violations: 33\n    dr_violation_rate: 0.21\n    CF_pct: 0.21\n    delta_vs_unconstrained:\n      delta_e_f1: 0.01\n      delta_r_f1: 0.06\n      delta_dr: -0.28\n      note: Authoritative values from eval_d064.py on w5_llama_docred_lora_constrained_eval.jsonl\n        (998 lines). Updated 2026-05-20.\n    provenance: eval_d064.py on westd-16980:/root/schema_semantic_constrained_ie/outputs/w5_llama_docred_lora_constrained_eval.jsonl,\n      2026-05-20. P/R corrected 2026-05-20 per Director.\n- exp_id: w5_qwen_docred_lora_unconstrained_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ET_pct: 0\n    RV_pct: 0.27\n    DR_pct: 0.76\n    CF_pct: 0.12\n    E_F1: 82.15\n    E_P: 85.44\n    E_R: 79.11\n    R_F1: 40.86\n    R_P: 36.41\n    R_R: 46.56\n    parse_fail_rate: 7.11\n    total_samples: 998\n    success_samples: 927\n    fail_samples: 71\n    total_entities_pred: 18091\n    total_relations_pred: 15870\n    ET_pct_excl_fail: 0\n    RV_pct_excl_fail: 0.27\n    DR_pct_excl_fail: 0.76\n    CF_pct_excl_fail: 0.12\n    E_F1_excl_fail: 85.72\n    E_P_excl_fail: 85.44\n    E_R_excl_fail: 86\n    R_F1_excl_fail: 42.2\n    R_P_excl_fail: 36.41\n    R_R_excl_fail: 50.17\n- exp_id: w5_qwen_docred_lora_constrained_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ET_pct: 0\n    RV_pct: 0\n    DR_pct: 0.01\n    CF_pct: 0.41\n    E_F1: 81.43\n    E_P: 85.41\n    E_R: 77.81\n    R_F1: 40.56\n    R_P: 36.35\n    R_R: 45.86\n    parse_fail_rate: 8.52\n    total_samples: 998\n    success_samples: 913\n    fail_samples: 85\n    total_entities_pred: 17799\n    total_relations_pred: 15563\n    E_F1_excl_fail: 85.69\n    R_F1_excl_fail: 42.23\n    delta_vs_unconstrained:\n      delta_DR: -0.75\n      delta_RV: -0.27\n      delta_R_F1: -0.3\n      delta_R_F1_excl_fail: 0.03\n      DR_reduction_pct: 98.7\n      note: 'Constrained - unconstrained. Unconstrained: DR=0.76%, R_F1=40.86, R_F1_excl_fail=42.20'\n- exp_id: w6_mistral_scierc_unconstrained\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    E_P: 0.2402\n    E_R: 0.3156\n    E_F1: 0.2728\n    R_P: 0.0295\n    R_R: 0.0483\n    R_F1: 0.0366\n    ET_pct: 1.5\n    RV_pct: 0\n    DR_pct: 56.94\n    CF_pct: 56.87\n    parse_fail_rate: 0\n    total_samples: 551\n    total_pred_entities: 2202\n    total_pred_relations: 1593\n- exp_id: w6_mistral_scierc_constrained\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    E_P: 0.2437\n    E_R: 0.3144\n    E_F1: 0.2746\n    R_P: 0.0292\n    R_R: 0.0493\n    R_F1: 0.0367\n    ET_pct: 0\n    RV_pct: 0\n    DR_pct: 13.4\n    CF_pct: 1.27\n    CF_count: 21\n    parse_fail_rate: 0\n    total_samples: 551\n    total_pred_entities: 2162\n    total_pred_relations: 1647\n    delta_vs_unconstrained:\n      delta_E_F1: 0.0018\n      delta_R_F1: 0.0001\n      delta_ET: -1.5\n      delta_RV: 0\n      delta_DR: -43.54\n      note: 'Constrained - unconstrained. Baseline: E_F1=0.2728, R_F1=0.0366, DR=56.94%,\n        ET=1.5%, RV=0%'\n- exp_id: w6_mistral_docred_unconstrained\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_samples: 998\n    parse_failures: 7\n    parse_fail_rate: 0.7\n    total_pred_entities: 12580\n    total_pred_relations: 11879\n    ET_pct: 7.58\n    RV_pct: 42.35\n    DR_pct: 57.42\n    CF_pct: 24.78\n    E_P: 0.6221\n    E_R: 0.3975\n    E_F1: 0.4851\n    R_P: 0.0447\n    R_R: 0.0432\n    R_F1: 0.0434\n    f1_method: fuzzy_normalized\n    f1_note: Relation matching uses case-insensitive normalization with token-overlap\n      >80% and edit-distance ≤2 fallback. Strict R_F1=3.50% (delta +0.84pp from 98\n      additional TPs via fuzzy matching of Mistral underscore/abbreviation variants).\n- exp_id: w6_mistral_docred_constrained\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ET_pct: 0\n    RV_pct: 0\n    DR_pct: 33.2\n    CF_pct: 0.19\n    E_P: 65.02\n    E_R: 41.4\n    E_F1: 50.59\n    R_P: 5.67\n    R_R: 5.37\n    R_F1: 5.52\n    parse_fail_rate: 0.8\n    total_samples: 998\n    total_pred_entities: 12535\n    total_pred_relations: 11554\n    delta_vs_unconstrained:\n      ET_pct: -7.58\n      RV_pct: -42.35\n      DR_pct: -24.22\n      CF_pct: -24.59\n      E_F1: 2.08\n      R_F1: 2.02\n- exp_id: w7_qwen_scierc_ft_grammar_only\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ET_pct: 0\n    RV_pct: 0\n    DR_pct: 1.9\n    CF_pct: 0\n    parse_fail_rate: 0\n    total_samples: 551\n    total_entities: 1784\n    total_relations: 1128\n    E_P: 0.6523\n    E_R: 0.6898\n    E_F1: 0.6705\n    R_P: 0.4087\n    R_R: 0.4733\n    R_F1: 0.4386\n    DR_violations: 22\n    tokenizer_warning: false_positive_transformers_4.57.6\n- exp_id: w7_qwen_scierc_ft_semantic_only\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ET_pct: 0\n    RV_pct: 0\n    DR_pct: 0.6\n    CF_count: 15\n    parse_fail_rate: 0\n    total_samples: 551\n    total_entities: 1784\n    total_relations: 1128\n    E_P: 0.6523\n    E_R: 0.6898\n    E_F1: 0.6705\n    R_P: 0.4073\n    R_R: 0.4713\n    R_F1: 0.4369\n    DR_violations: 7\n    delta_vs_grammar_only:\n      DR_delta: -1.3\n      note: semantic_only DR=0.6% vs grammar_only DR=1.9%, semantic layer reduces\n        DR by 68%\n    delta_vs_unconstrained:\n      DR_delta: -1.35\n      note: unconstrained DR=1.95% → semantic_only 0.6%\n- exp_id: w7_llama_scierc_ft_grammar_only\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_samples: 551\n    json_parse_failures: 0\n    total_entities: 1757\n    total_relations: 1082\n    entity_type_violation_rate: 0\n    relation_vocabulary_violation_rate: 0\n    domain_range_violation_rate: 0.0111\n    cross_field_consistency_violation_rate: 0\n    entity_f1:\n      precision: 0.6647\n      recall: 0.691\n      f1: 0.6776\n    relation_f1:\n      precision: 0.432\n      recall: 0.4795\n      f1: 0.4545\n- exp_id: w7_llama_scierc_ft_semantic_only\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ET_pct: 0\n    RV_pct: 0\n    DR_pct: 0.65\n    CF_count: 2\n    E_F1: 67.76\n    E_P: 66.47\n    E_R: 69.1\n    R_F1: 45.47\n    R_P: 43.24\n    R_R: 47.95\n    total_entities: 1757\n    total_relations: 1081\n    json_parse_failures: 0\n- exp_id: w8_ft_posthoc_baseline\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ft_regime:\n      qwen_scierc:\n        R_F1_before: 43.86\n        R_F1_posthoc: 43.94\n        R_F1_constrained: 43.77\n        reject_rate_pct: 1.95\n        TP_lost: 4\n      llama_scierc:\n        R_F1_before: 45.45\n        R_F1_posthoc: 45.23\n        R_F1_constrained: 45.47\n        reject_rate_pct: 1.11\n        TP_lost: 5\n      qwen_docred:\n        R_F1_before: 40.91\n        R_F1_posthoc: 41.11\n        R_F1_constrained: TBD\n        reject_rate_pct: 1.03\n        TP_lost: 1\n      llama_docred:\n        R_F1_before: 43.77\n        R_F1_posthoc: 43.92\n        R_F1_constrained: 44.23\n        reject_rate_pct: 0.64\n        TP_lost: 1\n    zs_regime:\n      mistral_scierc:\n        triples: 1584\n        reject_pct: 20.27\n        R_F1_before: 0.0376\n        R_F1_posthoc: 0.0394\n        R_F1_constrained: 0.0367\n        TP_before: 48\n        TP_after: 44\n        TP_lost: 4\n      qwen_scierc:\n        triples: 1724\n        reject_pct: 16.76\n        R_F1_before: 0.0823\n        R_F1_posthoc: 0.0863\n        R_F1_constrained: 0.0836\n        TP_before: 111\n        TP_after: 104\n        TP_lost: 7\n      llama_scierc:\n        triples: 1274\n        reject_pct: 13.89\n        R_F1_before: 0.0268\n        R_F1_posthoc: 0.0271\n        R_F1_constrained: 0.0254\n        TP_before: 30\n        TP_after: 28\n        TP_lost: 2\n      qwen_docred:\n        triples: 17497\n        reject_pct: 48.12\n        R_F1_before: 0.0774\n        R_F1_posthoc: 0.0961\n        R_F1_constrained: 0.0823\n        TP_before: 1137\n        TP_after: 1010\n        TP_lost: 127\n      llama_docred:\n        triples: 16437\n        reject_pct: 42.18\n        R_F1_before: 0.0598\n        R_F1_posthoc: 0.0744\n        R_F1_constrained: 0.0627\n        TP_before: 850\n        TP_after: 802\n        TP_lost: 48\n      mistral_docred:\n        triples: 11836\n        reject_pct: 73.73\n        R_F1_before: 0.0434\n        R_F1_posthoc: 0.0385\n        R_F1_constrained: 0.0552\n        TP_before: 518\n        TP_after: 292\n        TP_lost: 226\n        removed_RV: 4172\n        removed_ET: 3382\n        removed_DR: 1173\n        note: Only ZS case where posthoc HURTS R_F1 — 73.7% rejection rate loses 43.6%\n          of TPs\n    key_finding: 'ZS: post-hoc R_F1 >= constrained R_F1 in 5/6 groups. Exception:\n      Mistral DocRED where extreme rejection rate (73.7%) causes net F1 loss. Constrained\n      decoding value is in structural guarantee (0% violations) and composability,\n      not F1 preservation.'\n- exp_id: w8_llama_docred_ft_grammar_only\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    E_F1: 84.04\n    R_F1: 43.77\n    entity_precision: 84.99\n    entity_recall: 83.11\n    relation_precision: 38.6\n    relation_recall: 50.53\n    ET_pct: 0\n    RV_pct: 0\n    DR_pct: 0.51\n    CF_pct: 0.12\n    parse_fail_rate: 2.3\n    total_samples: 998\n    total_relations: 16199\n    unique_entities: 13225\n    parse_failures: 23\n- exp_id: w8_qwen_docred_ft_grammar_only\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    E_F1: 82.19\n    E_P: 85.47\n    E_R: 79.16\n    R_F1: 40.85\n    R_P: 36.27\n    R_R: 46.77\n    ET_pct: 0\n    RV_pct: 0\n    DR_pct: 0.61\n    CF_pct: 0.11\n    parse_fail_rate: 7.01\n    total_samples: 998\n    parse_failures: 70\n- exp_id: w8_qwen_docred_ft_semantic_only\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    E_F1: 82.15\n    E_P: 85.58\n    E_R: 78.99\n    R_F1: 40.89\n    R_P: 36.35\n    R_R: 46.73\n    ET_pct: 0\n    RV_pct: 0.23\n    DR_pct: 0.21\n    CF_pct: 0.27\n    parse_fail_rate: 7.52\n    total_samples: 998\n    parse_failures: 75\n    documents_checked: 923\n    total_entities: 18025\n    total_triples: 15909\n    DR_violations: 34\n    RV_violations: 37\n    ET_violations: 0\n    CF_violations: 49\n- exp_id: w8_llama_docred_ft_semantic_only\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    E_F1: 84.02\n    E_P: 85.01\n    E_R: 83.06\n    R_F1: 43.9\n    R_P: 38.89\n    R_R: 50.4\n    ET_pct: 0\n    RV_pct: 0.15\n    DR_pct: 0.3\n    CF_pct: 0.16\n    parse_fail_rate: 2.4\n    total_samples: 998\n    parse_failures: 24\n    documents_checked: 974\n    total_entities: 19099\n    total_relations: 16038\n    DR_violations: 48\n    RV_violations: 24\n    ET_violations: 0\n    CF_violations: 31\n- exp_id: w9_qwen_scierc_zs_sampling\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ET_pct: 0\n    RV_pct: 0\n    DR_pct: 0.75\n    CF_pct: 9.9\n    E_F1: 31.28\n    R_F1: 7.42\n    parse_fail_rate: 0\n    total_samples: 551\n    note: 'F1 computed by v2 checker; greedy baseline with same checker: E_F1=30.98,\n      R_F1=8.36'\n- exp_id: w9_qwen_docred_zs_sampling\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: w9_qwen_docred_zs_sampling_r2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: beam_search_scierc_full_551\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ET_pct: 0\n    RV_pct: 0\n    DR_pct: 0\n    CF_pct: 0.53\n    E_F1: 32\n    R_F1: 8.56\n    E_P: 26.83\n    E_R: 39.63\n    R_P: 6.69\n    R_R: 11.91\n    parse_fail_rate: 0\n    total_entities: 2476\n    total_relations: 1737\n- exp_id: w9_qwen_scierc_stability_3seeds\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    seed_123:\n      ET_pct: 0\n      RV_pct: 0\n      DR_pct: 0.93\n      CF_pct: 9.9\n      E_F1: 30.98\n      R_F1: 8.36\n    seed_456:\n      ET_pct: 0\n      RV_pct: 0\n      DR_pct: 0.93\n      CF_pct: 9.9\n      E_F1: 30.98\n      R_F1: 8.36\n    seed_789:\n      ET_pct: 0\n      RV_pct: 0\n      DR_pct: 0.93\n      CF_pct: 9.9\n      E_F1: 30.98\n      R_F1: 8.36\n    cross_seed_DR_std: 0\n    cross_seed_DR_range: 0\n    conclusion_note: Greedy decoding is fully deterministic - seed has no effect on\n      output. All metrics identical across 3 seeds.\n- exp_id: w9_llama_scierc_beam_551\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ET_pct: 0\n    RV_pct: 0\n    DR_pct: 0\n    CF_pct: 0.93\n    CF_count: 15\n    E_F1: 25.04\n    E_P: 21.27\n    E_R: 30.42\n    R_F1: 3.33\n    R_P: 2.68\n    R_R: 4.41\n    total_entities: 2398\n    total_relations: 1606\n    parse_fail_rate: 0\n    total_samples: 551\n    vs_greedy_full_s1:\n      DR_delta: -0.08\n      CF_delta: -5.63\n      E_F1_delta: 1.55\n      R_F1_delta: 0.79\n      note: 'Greedy: DR=0.08%, CF=6.56%, E_F1=23.49%, R_F1=2.54%'\n- exp_id: w9_qwen_docred_beam_50\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ET_pct: 0\n    RV_pct: 0\n    DR_pct: 0\n    CF_pct: 0.55\n    E_F1: 58.64\n    R_F1: 9.37\n    total_samples: 50\n    parse_failures: 3\n    parse_fail_rate: 6\n    vs_greedy_full_s1:\n      DR_delta: -10.21\n      CF_delta: -2.02\n      E_F1_delta: -0.73\n      R_F1_delta: 1.14\n      note: 'Greedy full_s1 998 docs: DR=10.21%, CF=2.57%, E_F1=59.37, R_F1=8.23.\n        Beam eliminates ALL DR on DocRED 96-type schema.'\n- exp_id: w10_type_consensus_prototype\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    ET_pct: 0\n    RV_pct: 0\n    DR_pct: 0.93\n    CF_pct: 9.9\n    E_F1: 30.98\n    R_F1: 8.36\n    gtc_skip_total: 672\n    gtc_skip_unique_entities: 258\n    gtc_effective_corrections: 0\n    delta_DR: 0\n    delta_CF: 0\n- exp_id: w10_type_consensus_docred_50\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    ET_pct: 0\n    RV_pct: 0\n    DR_pct: 8.69\n    CF_pct: 2.4\n    E_F1: 59.08\n    R_F1: 8.33\n    gtc_skip_total: 601\n    gtc_skip_unique_entities: 213\n    gtc_effective_corrections: 0\n    delta_DR: 0\n    delta_CF: 0\n- exp_id: w10_llama_docred_beam_50\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ET_pct: 0\n    RV_pct: 0\n    DR_pct: 0\n    CF_pct: 0.94\n    E_F1: 55.62\n    R_F1: 9.47\n    parse_failures: 3\n    parse_fail_rate: 6\n    total_samples: 50\n    vs_greedy_full_s1:\n      DR_delta: -2.57\n      CF_delta: -11.19\n      E_F1_delta: 0.61\n      R_F1_delta: 3.2\n      note: 'Greedy baseline: DR=2.57%, CF=12.13%, E_F1=55.01, R_F1=6.27'\n    checker_note: Must use violation_checker_docred.py for DocRED (not violation_checker.py)\n- exp_id: w10_mistral_scierc_beam_551\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    total_samples: 551\n    parse_failures: 1\n    parse_rate: 0.9982\n    ET_pct: 0\n    RV_pct: 0\n    DR_pct: 13.79\n    CF_pct: 0.57\n    E_P: 23.04\n    E_R: 31.64\n    E_F1: 26.66\n    R_P: 3.13\n    R_R: 7.22\n    R_F1: 4.37\n    total_entities: 2294\n    total_triples: 2241\n    vs_greedy:\n      baseline: w6_mistral_scierc_constrained\n      greedy_DR: 13.4\n      greedy_CF: 1.27\n      greedy_E_F1: 27.46\n      greedy_R_F1: 3.67\n      delta_DR: +0.39pp\n      delta_CF: -0.70pp\n      delta_E_F1: -0.80pp\n      delta_R_F1: +0.70pp\n- exp_id: w10_beam_ablation_k2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ET_pct: 0\n    RV_pct: 0\n    DR_pct: 0.35\n    CF_count: 71\n    CF_pct: 4.12\n    E_F1: 31.54\n    R_F1: 8.75\n    parse_failures: 0\n    total_samples: 551\n    total_triples: 1724\n    vs_greedy:\n      DR_delta: -0.58\n      CF_delta: -5.78\n      E_F1_delta: 0.56\n      R_F1_delta: 0.39\n      note: 'Greedy: DR=0.93%, CF=9.90%, E_F1=30.98, R_F1=8.36'\n    vs_beam_k4:\n      DR_delta: 0.35\n      CF_delta: 3.59\n      E_F1_delta: -0.46\n      R_F1_delta: 0.19\n      note: 'k=4: DR=0%, CF=0.53%, E_F1=32.00, R_F1=8.56'\n- exp_id: w10_beam_ablation_k8\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ET_pct: 0\n    RV_pct: 0\n    DR_pct: 0\n    CF_pct: 0.08\n    CF_count: 2\n    E_F1: 32.18\n    R_F1: 8.39\n    E_P: 26.95\n    E_R: 39.93\n    R_P: 6.54\n    R_R: 11.7\n    parse_failures: 0\n    total_samples: 551\n    total_triples: 1744\n    total_entities: 2483\n    vs_greedy:\n      DR_delta: -0.93\n      CF_delta: -9.82\n      E_F1_delta: 1.2\n      R_F1_delta: 0.03\n    vs_beam_k4:\n      DR_delta: 0\n      CF_delta: -0.45\n      E_F1_delta: 0.18\n      R_F1_delta: -0.17\n- exp_id: w9_mistral_docred_beam_50\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ET_violation_rate: 0\n    RV_violation_rate: 0\n    DR_violation_rate: 21.37\n    CF_violations: 1\n    total_triples: 524\n    total_entities: 597\n    docs_checked: 49\n    parse_failures: 1\n    E_F1: 51.78\n    E_P: 65.2\n    E_R: 42.94\n    R_F1: 5.7\n    R_P: 6.49\n    R_R: 5.08\n    R_tp: 34\n    R_gold: 669\n    R_pred: 524\n- exp_id: w10_qwen_scierc_ft_beam_4\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    DR: 0\n    CF: 0\n    total_violation_rate: 0\n    entity_type_violation_rate: 0\n    relation_vocab_violation_rate: 0\n    domain_range_violation_rate: 0\n    cross_field_consistency_violation_rate: 0\n    E_F1: 66.88\n    E_P: 64.69\n    E_R: 69.22\n    R_F1: 44.23\n    R_P: 39.41\n    R_R: 50.41\n    total_samples: 551\n    json_parse_failures: 0\n    total_entities: 1802\n    total_relations: 1246\n    vs_ft_greedy:\n      baseline: w5_lora_scierc_constrained_eval\n      DR_delta: 0% → 0% (same)\n      CF_delta: 1.18% → 0.0% (eliminated all violations)\n      E_F1_delta: 67.05 → 66.88 (-0.17, negligible)\n      R_F1_delta: 43.77 → 44.23 (+0.46, slight improvement)\n    vs_zs_beam_k4:\n      DR_delta: 0% → 0% (same)\n      CF_delta: 0.53% → 0.0% (eliminated)\n      E_F1_delta: 32.00 → 66.88 (+34.88)\n      R_F1_delta: 8.56 → 44.23 (+35.67)\n- exp_id: r4_prompt_minimal\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    unconstrained:\n      ET_pct: 0.58\n      RV_pct: 1.16\n      DR_pct: 16.91\n      E_F1: 31.98\n      R_F1: 7.91\n    constrained:\n      ET_pct: 0\n      RV_pct: 0\n      DR_pct: 0.92\n      E_F1: 31.99\n      R_F1: 7.85\n    DR_reduction_pct: 94.6\n    delta_R_F1_pp: -0.06\n    delta_E_F1_pp: 0.01\n- exp_id: r4_prompt_detailed\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    unconstrained:\n      ET_pct: 0.22\n      RV_pct: 0.45\n      DR_pct: 11.07\n      E_F1: 33.55\n      R_F1: 10.48\n    constrained:\n      ET_pct: 0\n      RV_pct: 0\n      DR_pct: 0.64\n      E_F1: 33.56\n      R_F1: 10.48\n    DR_reduction_pct: 94.2\n    delta_R_F1_pp: 0\n    delta_E_F1_pp: 0.01\n- exp_id: ee_qwen_wikievents_unconstrained\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    parse_success: 218/246 (88.6%)\n    ET: 0\n    EV: 24\n    RoV: 74.9\n    AC: 0.3\n    CF: 0\n    trigger_f1: 0.1184\n    argument_f1: 0.0009\n    entity_f1: 0\n- exp_id: ee_llama_wikievents_unconstrained\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    parse_success: 226/246 (91.9%)\n    ET: 0\n    EV: 10.5\n    RoV: 88.8\n    AC: 0.1\n    CF: 0\n    trigger_f1: 0.0572\n    argument_f1: 0\n    entity_f1: 0\n- exp_id: ee_qwen_wikievents_constrained\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    parse_success: 206/246 (83.7%)\n    ET: 0\n    EV: 0\n    RoV: 0.3\n    AC: 2.1\n    CF: 21.1\n    trigger_f1: 0.1339\n    argument_f1: 0.0168\n    entity_f1: 0.1409\n    parse_failures: 40\n    go_no_go: 2.4\n    note: after retry with max_new_tokens=8192\n- exp_id: ee_llama_wikievents_constrained\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    parse_success: 215/246 (87.4%)\n    ET: 0\n    EV: 0\n    RoV: 0\n    AC: 3.4\n    CF: 15.5\n    trigger_f1: 0.078\n    argument_f1: 0.011\n    entity_f1: 0.178\n    parse_failures: 31\n    go_no_go: 3.4\n    note: after retry with max_new_tokens=8192\n- exp_id: ee_mistral_wikievents_unconstrained\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    parse_success: 194/246 (78.9%)\n    ET: 0\n    EV: 37.3\n    RoV: 63.9\n    AC: 0\n    CF: 0\n    trigger_f1: 0.0241\n    argument_f1: 0\n    entity_f1: 0\n- exp_id: ee_mistral_wikievents_constrained\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    parse_success: 184/246 (74.8%)\n    ET: 0\n    EV: 0\n    RoV: 54.8\n    AC: 19.2\n    CF: 0.7\n    note: grammar_only baseline (old code without semantic mask fix)\n- exp_id: ee_mistral_wikievents_constrained_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    parse_success: 178/246 (72.4%)\n    ET: 0\n    EV: 0\n    RoV: 0.1\n    AC: 16.6\n    CF: 13.9\n    trigger_f1: 0.0508\n    argument_f1: 0.0047\n    entity_f1: 0.1245\n    parse_failures: 68\n    go_no_go: 16.7\n- exp_id: ee_qwen_wikievents_constrained_v3\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    parse_success: 206/246 (83.7%)\n    parse_failures: 40\n    ET: 0\n    EV: 0\n    RoV: 0\n    AC: 2.1\n    CF: 21.1\n    go_no_go: 2.05\n    entity_f1: 0.1409\n    trigger_f1: 0.1339\n    argument_f1: 0.0168\n    code_version: 938-line (collision+exact-match fix)\n    posthoc_args_removed: 109\n    posthoc_arg_f1: 0.017\n    cf_voting_fix_rate: 15.9%\n    cf_voting_entity_f1: 0.1352\n- exp_id: ee_llama_wikievents_constrained_v3\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    parse_success: 207/246 (84.1%)\n    parse_failures: 39\n    ET: 0\n    EV: 0\n    RoV: 0\n    AC: 3.8\n    CF: 17.2\n    go_no_go: 3.8\n    entity_f1: 0.1763\n    trigger_f1: 0.0748\n    argument_f1: 0.0118\n    code_version: 938-line (collision+exact-match fix)\n    posthoc_args_removed: 173\n    posthoc_arg_f1: 0.0118\n- exp_id: ee_mistral_wikievents_constrained_v3\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    parse_success: 218/246 (88.6%)\n    parse_failures: 28\n    ET: 0\n    EV: 0\n    RoV: 0\n    AC: 1.3\n    CF: 14.9\n    go_no_go: 1.26\n    entity_f1: 0.1171\n    trigger_f1: 0.0387\n    argument_f1: 0.0031\n    code_version: 938-line (collision+exact-match fix)\n    posthoc_args_removed: 86\n    posthoc_ac_after: 0\n- exp_id: ee_mistral_wikievents_grammar_only_v3\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    parse_success: 218/246 (88.6%)\n    parse_failures: 28\n    ET: 0\n    EV: 0\n    RoV: 64\n    AC: 13.8\n    CF: 1.1\n    go_no_go: 77.73\n    entity_f1: 0.1192\n    trigger_f1: 0.0337\n    argument_f1: 0.0027\n    code_version: 938-line (collision+exact-match fix)\n    mode: grammar_only\n- exp_id: 70b_scierc_unconstrained\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ET_pct: 0\n    RV_pct: 0.6\n    DR_pct: 6.5\n    CF_count: 0\n    CF_pct: 0\n    E_F1: 0.3517\n    E_P: 0.3009\n    E_R: 0.4232\n    R_F1: 0.1122\n    R_P: 0.0929\n    R_R: 0.1417\n    total_entities: 2353\n    total_relations: 1485\n    parse_failures: 0\n    samples: 551\n- exp_id: 70b_scierc_constrained\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ET_pct: 0\n    RV_pct: 0\n    DR_pct: 0\n    CF_count: 86\n    CF_pct: 3.66\n    E_F1: 0.3514\n    E_P: 0.3007\n    E_R: 0.4226\n    R_F1: 0.1124\n    R_P: 0.0932\n    R_R: 0.1417\n    total_entities: 2351\n    total_relations: 1481\n    parse_failures: 0\n    samples: 551\n- exp_id: 70b_docred_unconstrained\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    entity_f1: 69.03\n    entity_precision: 75.03\n    entity_recall: 63.92\n    relation_f1: 13.03\n    relation_precision: 12.43\n    relation_recall: 13.69\n    ET_violation: 0.02\n    RV_violation: 7.8\n    DR_violation: 15\n    CF_violation: 0.07\n    parse_failures: 0\n    docs_processed: 998\n- exp_id: 70b_docred_constrained\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ET_violation: 0\n    RV_violation: 0\n    DR_violation: 0\n    CF_violation: 7.01\n    entity_f1: 69.05\n    entity_precision: 75.03\n    entity_recall: 63.95\n    relation_f1: 13.07\n    relation_precision: 12.54\n    relation_recall: 13.64\n    parse_failures: 1\n    docs_processed: 997\n    total_docs: 998\n    unique_entities: 12207\n    total_triples: 13249\n- exp_id: q1_llama_lora_scierc_beam4\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ET_violation_rate: 0\n    RV_violation_rate: 0\n    DR_violation_rate: 0\n    CF_violation_rate: 0\n    entity_f1: 67.94\n    relation_f1: 46.11\n    samples: 551\n    total_entities: 1853\n    total_relations: 727\n- exp_id: p8_latency_overhead\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    samples: 551\n    unconstrained_mean_s: 4.163\n    unconstrained_median_s: 4.106\n    unconstrained_total_s: 2293.7\n    constrained_mean_s: 4.71\n    constrained_median_s: 4.644\n    constrained_total_s: 2595\n    overhead_ratio_mean: 1.131\n    overhead_ratio_median: 1.131\n    overhead_ratio_p95_perdoc: 1.262\n    overhead_pct: 13.1\n- exp_id: p8b_docred_latency\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: p8c_ft_scierc_latency\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    unconstrained_mean_s: 2.612\n    constrained_mean_s: 2.873\n    unconstrained_median_s: 2.355\n    constrained_median_s: 2.624\n    overhead_mean_pct: 10\n    overhead_median_pct: 11.42\n    per_doc_ratio_mean: 1.205\n    per_doc_ratio_median: 1.117\n    num_docs: 551\n    unconstrained_total_s: 1439\n    constrained_total_s: 1582.9\n- exp_id: p1_ee_ft_composability\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: p1_ee_ft_composability_r2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: p1_ee_ft_composability_r3\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: p1_ee_ft_composability_r4\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    unconstrained:\n      entity_f1: 0\n      trigger_f1: 0.4598\n      argument_f1: 0.1581\n      rov: 0.251\n      ac: 0.06\n      cf: 0\n      parse_rate: 0.25\n    full_s1:\n      entity_f1: 0.5823\n      trigger_f1: 0.6\n      argument_f1: 0.4667\n      rov: 0\n      ac: 0\n      cf: 0.03\n      parse_rate: 0.1\n- exp_id: p1_ee_ft_llama\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: p1_llama_ee_ft\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: p1_ee_ft_composability_r5\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    unconstrained:\n      parse_rate: 0.85\n      trigger_f1: 0.3208\n      argument_f1: 0.0785\n      rov_rate: 0.3831\n      ac_rate: 0.0268\n      go_nogo: 0.41\n    full_s1:\n      parse_rate: 0.95\n      trigger_f1: 0.2672\n      argument_f1: 0.0818\n      rov_rate: 0\n      ac_rate: 0\n      go_nogo: 0\n- exp_id: p1_ee_ft_llama_r2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    parse_rate_unconstrained: 1\n    parse_rate_constrained: 1\n    trigger_f1_unconstrained: 0.2752\n    trigger_f1_constrained: 0.2691\n    argument_f1_unconstrained: 0.0998\n    argument_f1_constrained: 0.0891\n    entity_f1: 0\n    rov_rate_unconstrained: 0.088\n    rov_rate_constrained: 0\n    ac_rate_unconstrained: 0.035\n    ac_rate_constrained: 0.008\n    go_nogo_unconstrained: 0.122\n    go_nogo_constrained: 0.0078\n- exp_id: d062_full_ft_scierc\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    unconstrained:\n      entity_f1: 0.6478\n      relation_f1: 0.3789\n      DR_pct: 2.74\n      RV_pct: 0.18\n      ET_pct: 0\n      CF_pct: 0\n    constrained:\n      entity_f1: 0.6478\n      relation_f1: 0.3789\n      DR_pct: 0\n      RV_pct: 0\n      ET_pct: 0\n      CF_pct: 1.31\n    training:\n      eval_loss_final: 0.09459\n      epochs: 3\n      total_steps: 333\n      training_time: 21m49s\n- exp_id: d062_cf_majority_voting\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    qwen_scierc_zs:\n      cf_before: 245\n      cf_after: 201\n      dr_rate_before: 0.0093\n      dr_rate_after: 0.0324\n    llama_scierc_zs:\n      cf_before: 162\n      cf_after: 123\n      dr_rate_before: 0.0008\n      dr_rate_after: 0.0236\n    qwen_docred_zs:\n      cf_before: 518\n      cf_after: 21\n      dr_rate_before: 0.1021\n      dr_rate_after: 0.1466\n    llama_docred_zs:\n      cf_before: 1358\n      cf_after: 107\n      dr_rate_before: 0.0255\n      dr_rate_after: 0.1665\n    qwen_scierc_ft:\n      cf_before: 21\n      cf_after: 12\n      dr_rate_before: 0\n      dr_rate_after: 0.0071\n    llama_scierc_ft:\n      cf_before: 8\n      cf_after: 4\n      dr_rate_before: 0.0009\n      dr_rate_after: 0.0037\n    qwen_docred_ft:\n      cf_before: 48\n      cf_after: 3\n      dr_rate_before: 0.0001\n      dr_rate_after: 0.0044\n    llama_docred_ft:\n      cf_before: 41\n      cf_after: 2\n      dr_rate_before: 0.0021\n      dr_rate_after: 0.005\n- exp_id: d062_beam_latency\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    beam4_unconstrained_s_per_doc: 3.446\n    beam4_constrained_s_per_doc: 4.013\n    beam4_unconstrained_total_s: 1898.7\n    beam4_constrained_total_s: 2211\n    beam_greedy_ratio_unconstrained: 1.319\n    beam_greedy_ratio_constrained: 1.397\n    constraint_overhead_beam: 1.165\n    constraint_overhead_greedy: 1.1\n    greedy_unconstrained_s_per_doc: 2.612\n    greedy_constrained_s_per_doc: 2.873\n- exp_id: d062_ontology_scalability\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    compile_small_total_s: 0.334\n    compile_medium_total_s: 0.322\n    compile_large_total_s: 0.345\n    compile_xlarge_total_s: 0.42\n    grammar_small_s: 0.333\n    grammar_xlarge_s: 0.365\n    semantic_small_s: 0.0004\n    semantic_xlarge_s: 0.017\n    overhead_small: 1.02\n    overhead_medium: 1.03\n    overhead_large: 1.03\n    overhead_xlarge: 1.03\n    failures: 0\n- exp_id: d063_gollie_violation_rate\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    gollie_DR: 0\n    gollie_RV: 0\n    gollie_ET: 0\n    gollie_CF: 0.67\n    gollie_entities: 300\n    gollie_relations: 7\n    gollie_empty_docs_pct: 45\n    docs_tested: 100\n- exp_id: d064_docred_full_beam\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: d065_tcr_pilot\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    scierc_zs_qwen:\n      cf_before: 9.75\n      cf_after: 0\n      dr_before: 0.93\n      dr_after: 1.21\n      ef1_delta: -0.0129\n      fund_pct: 2.04\n    scierc_zs_llama:\n      cf_before: 6.4\n      cf_after: 0\n      dr_before: 0.08\n      dr_after: 0.3\n      ef1_delta: -0.0178\n      fund_pct: 1.85\n    scierc_lora_qwen:\n      cf_before: 1.19\n      cf_after: 0\n      dr_before: 0\n      dr_after: 0\n      ef1_delta: -0.0075\n      fund_pct: 0\n    scierc_lora_llama:\n      cf_before: 0.46\n      cf_after: 0\n      dr_before: 0.09\n      dr_after: 0.09\n      ef1_delta: -0.0018\n      fund_pct: 0\n    scierc_zs_mistral:\n      cf_before: 0.67\n      cf_after: 0\n      dr_before: 13.36\n      dr_after: 12.87\n      ef1_delta: 0.0005\n      fund_pct: 0\n    docred_zs_qwen:\n      cf_before: 13.11\n      cf_after: 0\n      dr_before: 10.21\n      dr_after: 11.74\n      ef1_delta: -0.0344\n      fund_pct: 13.52\n    docred_zs_llama:\n      cf_before: 23.71\n      cf_after: 0\n      dr_before: 2.55\n      dr_after: 11.93\n      ef1_delta: -0.0521\n      fund_pct: 22.78\n    docred_zs_70b:\n      cf_before: 11.61\n      cf_after: 0\n      dr_before: 0\n      dr_after: 4.2\n      ef1_delta: -0.0598\n      fund_pct: 18.26\n    docred_lora_qwen:\n      cf_before: 0.42\n      cf_after: 0\n      dr_before: 0.01\n      dr_after: 0.14\n      ef1_delta: -0.0016\n      fund_pct: 12.16\n    docred_lora_llama:\n      cf_before: 0.36\n      cf_after: 0\n      dr_before: 0.21\n      dr_after: 0.2\n      ef1_delta: -0.0017\n      fund_pct: 11.59\n    total_configs: 10\n    all_cf_eliminated: true\n- exp_id: d065_tcr_full\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    configs_tested: 10\n    all_cf_eliminated: true\n    scierc_all_dr_delta_max: 0.28\n    docred_lora_dr_delta_max: 0.14\n    docred_zs_llama_dr_delta: 9.38\n    docred_zs_70b_dr_delta: 4.2\n    docred_zs_qwen_dr_delta: 1.53\n    fund_conflict_scierc_max: 2.04\n    fund_conflict_docred_zs_max: 22.78\n    fund_conflict_docred_lora_max: 12.16\n    lora_ef1_cost_max: 0.0075\n    zs_docred_ef1_cost_max: 0.0598\n- exp_id: d068_constraint_guided_beam_pilot\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics: {}\n- exp_id: d066_beam_sweep\n  name: ''\n  status: ANALYZING\n  conclusion: ''\n  metrics:\n    scierc_qwen3_8b:\n      k1_unc:\n        E_F1: 66.88\n        R_F1: 42.95\n        DR_pct: 2.11\n        CF_pct: 0\n        avg_time: 2.494\n      k1_con:\n        E_F1: 66.88\n        R_F1: 42.95\n        DR_pct: 0\n        CF_pct: 0.5\n        avg_time: 2.932\n      k2_unc:\n        E_F1: 67.79\n        R_F1: 44.75\n        DR_pct: 1.54\n        CF_pct: 0\n        avg_time: 2.954\n      k2_con:\n        E_F1: 67.71\n        R_F1: 44.6\n        DR_pct: 0\n        CF_pct: 0.11\n        avg_time: 3.463\n      k4_unc:\n        E_F1: 67.49\n        R_F1: 43.72\n        DR_pct: 1.89\n        CF_pct: 0\n        avg_time: 3.485\n      k4_con:\n        E_F1: 67.22\n        R_F1: 43.6\n        DR_pct: 0\n        CF_pct: 0\n        avg_time: 4.069\n      k8_unc:\n        E_F1: 66.4\n        R_F1: 43.17\n        DR_pct: 1.77\n        CF_pct: 0\n        avg_time: 4.194\n      k8_con:\n        E_F1: 66.36\n        R_F1: 43.65\n        DR_pct: 0\n        CF_pct: 0\n        avg_time: 5.058\n    pareto_optimal: k=2 con\n    best_E_F1:\n      config: k=2 unc\n      value: 67.79\n    best_R_F1:\n      config: k=2 unc\n      value: 44.75\n- exp_id: d067_seed_variance\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    qwen_scierc_unc:\n      E_F1: 66.94 ± 0.08\n      R_F1: 43.25 ± 0.43\n      DR: 2.06 ± 0.08\n      CF: 0.00 ± 0.00\n    qwen_scierc_con:\n      E_F1: 66.94 ± 0.08\n      R_F1: 43.22 ± 0.39\n      DR: 0.00 ± 0.00\n      CF: 0.48 ± 0.02\n    llama_scierc_unc:\n      E_F1: 67.99 ± 0.16\n      R_F1: 45.38 ± 0.05\n      DR: 1.04 ± 0.05\n      CF: 0.00 ± 0.00\n    llama_scierc_con:\n      E_F1: 67.99 ± 0.16\n      R_F1: 45.40 ± 0.05\n      DR: 0.03 ± 0.04\n      CF: 0.26 ± 0.02\n    max_sigma_pp: 0.43\n    greedy_deterministic: true\n    snr_dr_improvement: '>12x'\n    qwen_docred_status: pending (not started)\n    llama_scierc_seed456_con_status: running (407/551)\n- exp_id: d066_docred_beam_sweep\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: d065_qwen_greedy_4096\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: d065_qwen_greedy_4096_r2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    E-F1: 81.87\n    R-F1: 40.79\n    DR_pct: 0\n    CF_pct: 0.22\n    ET_pct: 0\n    RV_pct: 0\n    PF_pct: 8.52\n    samples: 998\n- exp_id: d066_sweep_16980_gpu1\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: d066_sweep_21461_gpu1\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total: 551\n    E_F1: 66.36\n    R_F1: 43.65\n    DR_pct: 0\n    CF_pct: 0\n    ET_pct: 0\n    RV_pct: 0\n    avg_time_s: 5.058\n    output_file: qwen_scierc_beam8_full_s1.jsonl\n    note: Actually ran on SciERC 551 docs (not DocRED 200 as originally recorded in\n      hypothesis)\n- exp_id: d066_sweep_llama_beam2_s1\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    E_F1: 85.6\n    E_P: 85.29\n    E_R: 85.92\n    R_F1: 51.17\n    R_P: 48.51\n    R_R: 54.14\n    DR_pct: 0\n    CF_pct: 0\n    ET_pct: 0\n    RV_pct: 0\n    parse_fail_pct: 0.5\n    total_samples: 200\n    total_entities_pred: 3814\n    total_relations_pred: 2839\n- exp_id: d066_sweep_llama_beam8_unc\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    E_F1: 85.77\n    E_P: 85.7\n    E_R: 85.84\n    R_F1: 51.97\n    R_P: 49.76\n    R_R: 54.38\n    DR_pct: 0\n    CF_pct: 0.05\n    ET_pct: 0\n    RV_pct: 0.07\n    parse_fail_pct: 0.5\n    total_samples: 200\n    total_entities_pred: 3788\n    total_relations_pred: 2779\n- exp_id: d066_sweep_llama_scierc_beam1_unc\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    total: 275\n    success: 275\n    fail: 0\n    output_file: llama_scierc_beam1_unconstrained.jsonl\n    note: 'INVALIDATED: Used dev set (275 docs) instead of test set (551 docs). Not\n      comparable with other beam sweep results. Llama SciERC beam sweep deprioritized\n      — must use scripts/d066_beam_sweep_scierc.sh with --data_path data/processed_data/test.json\n      if rerun.'\n- exp_id: d066_sweep_llama_beam8_s1\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    E-F1: 85.76\n    R-F1: 51.74\n    DR_pct: 0\n    CF_pct: 0\n    PF_pct: 0.5\n    samples: 200\n- exp_id: d066_sweep_llama_docred_beam1_unc\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total: 200\n    success: 196\n    fail: 4\n    output_file: llama_docred_200_beam1_unconstrained.jsonl\n- exp_id: d066_sweep_llama_docred_beam1_s1\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    E-F1: 85.43\n    R-F1: 47.35\n    DR_pct: 0\n    CF_pct: 0.19\n    PF_pct: 2\n    samples: 200\n- exp_id: d066_sweep_llama_docred_beam4_unc\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    E-F1: 85.67\n    R-F1: 52.65\n    DR_pct: 0.04\n    CF_pct: 0.08\n    PF_pct: 0.5\n    samples: 200\n- exp_id: d066_sweep_llama_docred_beam4_s1\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    E-F1: 85.61\n    E-P: 85.48\n    E-R: 85.73\n    R-F1: 51.89\n    R-P: 51.59\n    R-R: 52.2\n    DR_pct: 0\n    CF_pct: 0\n    PF_pct: 0.5\n    ET_pct: 0\n    RV_pct: 0\n    samples: 200\n    parse_fail: 1\n- exp_id: d066_sweep_llama_scierc_beam4_s1_551\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    E-F1: 68.06\n    E-P: 65.96\n    E-R: 70.29\n    R-F1: 46.18\n    R-P: 42.1\n    R-R: 51.13\n    ET_pct: 0\n    RV_pct: 0\n    DR_pct: 0\n    CF_pct: 0\n    parse_fail: 0\n    samples: 551\n    note: 'ET/RV corrected from 100→0: original eval used hardcoded DocRED ontology,\n      re-evaled with --dataset scierc'\n- exp_id: d066_sweep_llama_scierc_beam2_s1_551\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    entity_f1: 68.34\n    entity_p: 66.59\n    entity_r: 70.17\n    relation_f1: 46.12\n    relation_p: 42.73\n    relation_r: 50.1\n    parse_fail_pct: 0\n    ET_pct: 0\n    RV_pct: 0\n    DR_pct: 0\n    CF_pct: 0.17\n    note: 'ET/RV corrected from 100→0: original eval used hardcoded DocRED ontology,\n      re-evaled with --dataset scierc'\n- exp_id: d066_sweep_llama_scierc_beam8_s1_551\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    E-F1: 67.51\n    E-P: 64.99\n    E-R: 70.23\n    R-F1: 44.95\n    R-P: 40.1\n    R-R: 51.13\n    ET_pct: 0\n    RV_pct: 0\n    DR_pct: 0\n    CF_pct: 0\n    PF_pct: 0\n    samples: 551\n    note: Reconcile false positive corrected. Eval with --dataset scierc confirmed.\n- exp_id: r14_qwen_docred_beam4_998\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    E_F1: 58.19\n    R_F1: 8.72\n    DR_pct: 0\n    RV_pct: 0\n    ET_pct: 0\n    CF_pct: 4.94\n    parse_fail_pct: 3.51\n    samples: 998\n    success: 963\n    fail: 35\n- exp_id: r14_llama_docred_beam4_998\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    R_F1: 8.83\n    E_F1: 57.81\n    DR_pct: 0\n    CF_pct: 1\n    ET_pct: 0\n    RV_pct: 0\n    parse_fail_pct: 3.91\n    samples: 998\n    success: 959\n    fail: 39\n    baseline_ZS_greedy_R_F1: 6.27\n    baseline_ZS_greedy_E_F1: 54.93\n    baseline_ZS_greedy_DR_pct: 2.55\n    baseline_ZS_greedy_CF_pct: 8.54\n- exp_id: r16_trie_qwen_ft_scierc\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    E_F1: 66.73\n    R_F1: 42.57\n    ET_pct: 0\n    RV_pct: 0\n    DR_pct: 95.5\n    CF_pct: 0.09\n    parse_fail_pct: 9.1\n    samples: 551\n- exp_id: r16_trie_qwen_zs_scierc\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    E_F1: 30.97\n    R_F1: 8.64\n    ET_pct: 0\n    RV_pct: 0\n    DR_pct: 29.3\n    CF_pct: 0\n    parse_fail_pct: 0\n    samples: 551\n- exp_id: r16_trie_llama_ft_scierc\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    E_F1: 65.37\n    R_F1: 41.42\n    ET_pct: 0\n    RV_pct: 0\n    DR_pct: 15.2\n    CF_pct: 0\n    parse_fail_pct: 50.8\n    samples: 551\n- exp_id: r16_trie_llama_zs_scierc\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    E_F1: 23.23\n    R_F1: 2.9\n    ET_pct: 0\n    RV_pct: 0\n    DR_pct: 84.4\n    CF_pct: 0.36\n    parse_fail_pct: 0\n    samples: 551\n- exp_id: r16_70b_scierc_zs_s1\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    E_F1: 35.19\n    R_F1: 11.24\n    DR_pct: 0\n    RV_pct: 0\n    ET_pct: 0\n    CF_pct: 3.5\n    parse_fail_pct: 0\n    samples: 551\n    baseline_unc_E_F1: 35.21\n    baseline_unc_R_F1: 11.15\n    baseline_unc_DR_pct: 6.41\n    baseline_unc_RV_pct: 0.61\n    baseline_unc_CF_pct: 0\n- exp_id: r16_70b_docred_zs_s1\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    E_F1: 69.11\n    R_F1: 13.05\n    DR_pct: 0\n    RV_pct: 0\n    ET_pct: 0\n    CF_pct: 0.04\n    parse_fail_pct: 0.1\n    samples: 998\n    total_entities: 16599\n    total_triples: 13239\n    baseline_unc_DR_pct: 14.98\n    baseline_unc_R_F1: 13.01\n    note: Metrics corrected via eval_d064.py with DocRED schema mapping. Original\n      violation_checker.py gave R-F1=0 due to SciERC schema mismatch.\n- exp_id: r16_70b_lora_scierc\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    eval_loss: 0.0611\n    token_acc: 97.78\n    steps_completed: 663\n    epochs: 3\n    train_loss_start: 0.183\n    train_loss_end: 0.041\n- exp_id: r16_70b_lora_docred\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    eval_loss: 0.0635\n    token_acc: 97.94\n    steps_completed: 1146\n    epochs: 3\n    train_loss_start: 0.147\n    train_loss_end: 0.056\n- exp_id: eval_70b_lora_scierc_unconstrained\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: r16_70b_lora_scierc_eval\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: eval_70b_lora_docred_200_unconstrained\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: worst\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n\n重要：tables 中使用 YAML flow sequence 时，所有字符串必须加双引号（如 `columns: [\"Judge\", \"Biased?\"]`），否则 `?` `:` 等字符会导致解析失败。\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-22T05:50:11.275Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-22T05:50:11.275Z",
  "sessionId": "8b60bbb7-357b-4091-8cce-e13fa8ccd284"
}
```

---

## Round 1

31 recorded events

### User

_source line 3 · 2026-05-22T05:50:11.301Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：

含义：≥2 reviewers 认为 novelty 不足以支撑 main conference；核心 'guaranteed compliance' claim 被 CF 数据和 post-hoc 比较削弱；需要 reframe 切入角度
核心假设：["Novelty 被拒：'constrained decoding for IE is a straightforward application of XGrammar; the semantic layer is a lookup table with logit masking'", "CF 被视为 fundamental flaw：'you claim type-valid IE but introduce 10-21% cross-field violations — the cure is worse than the disease in some configs'", "Post-hoc 在 ZS regime 下 R_F1 全面优于 constrained decoding（5/6 configs），reviewer 直接问 'what's the point?'", "EE 完全被 dismiss：'Arg F1≈0, Entity F1 from 0→14% is just format compliance, not extraction improvement'", '70B LoRA eval 出问题：DR>1% 或 R-F1 下降 >2pp 或 parse failure rate 过高（>10%），削弱 scale 泛化 claim', "ZS 8% F1 被两位 reviewer 视为 'toy evaluation'", 'GCD/BoostCD 被 reviewer 认为已 subsume 本文贡献']
关键指标范围：{'emnlp_overall_assessment': [2.5, 3.5], 'review_novelty': [2.0, 3.0], 'review_soundness': [3.0, 3.5], 'review_significance': [2.0, 3.0], '70b_lora_scierc_DR_pct': [0.5, 3.0], '70b_lora_scierc_R_F1_delta_pp': [-3.0, -0.5], '70b_lora_docred_DR_pct': [0.5, 5.0], '70b_lora_docred_R_F1_delta_pp': [-4.0, -1.0], 'hostile_reviewer_count': [2, 3]}
叙事方向：核心 "type-valid IE" framing 不成立，需要完全 reframe。仍冲 EMNLP 2026（October ARR cycle），不降级 venue。 Reframe 方向：从 "constrained decoding method paper" → "empirical study paper with a tool"。 新 title 方向："How Do LLMs Violate Ontology Constraints? A Systematic Study with Mitigation"。 新 story：(1) 主贡献是 violation landscape 的系统性实证研究（tightness × RV baseline 交互、constraint-type taxonomy、cross-model/cross-task violation pattern），这本身是 ACL/EMNLP 近年接受的 empirical analysis 范式； (2) OntoCoDec 降级为 "mitigation tool" 而非核心贡献，证明 violation 可被系统性处理但存在 tradeoff（DR↓ vs CF↑）； (3) 重心转向 analysis findings——为什么 prompt 不够（prior-constraint conflict）、为什么 post-hoc 不够（information loss）、为什么 grammar-only 不够（enabling dependency）、为什么 CF 必然存在（prefix-decidability 的理论限制）。 这个 reframe 把 novelty 锚点从 method → empirical findings + theoretical analysis，避开 "incremental over XGrammar" 攻击线。 补充工作：(a) 更深的 violation pattern 分析（per-relation type、per-document length、per-entity ambiguity）；(b) 与 GoLLIE 等 code-generation IE 的 violation 对比（d063 已有初步数据）；(c) 理论部分扩展 decidability taxonomy 为 formal framework。

基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。
每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。

# Project context
project: schema_semantic_constrained_ie
venue: emnlp-2026
focus: 评估当前论文（含 70B ZS 跨两个数据集 + 即将到手的 70B LoRA 结果）能否达到 EMNLP 2026 Overall Assessment 4.0（Conference）。重点关注：novelty 感知（semantic constraint layer 是否被视为足够新颖）、evaluation scope（RE 为主 + preliminary EE 是否足够）、与 GCD/BoostCD/XGrammar 的差异化。

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
    entity_f1: 83.94
    entity_precision: 85
    entity_recall: 84.13
    relation_f1_all_set: 43.78
    relation_precision_all_set: 38.79
    relation_recall_all_set: 50.81
    et_violations: 0
    et_violation_rate: 0
    rv_violations: 0
    rv_violation_rate: 0
    dr_violations: 33
    dr_violation_rate: 0.21
    CF_pct: 0.21
    delta_vs_unconstrained:
      delta_e_f1: 0.01
      delta_r_f1: 0.06
      delta_dr: -0.28
      note: Authoritative values from eval_d064.py on w5_llama_docred_lora_constrained_eval.jsonl
        (998 lines). Updated 2026-05-20.
    provenance: eval_d064.py on westd-16980:/root/schema_semantic_constrained_ie/outputs/w5_llama_docred_lora_constrained_eval.jsonl,
      2026-05-20. P/R corrected 2026-05-20 per Director.
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
  status: DONE
  conclusion: success
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
  status: DONE
  conclusion: success
  metrics:
    entity_f1: 69.03
    entity_precision: 75.03
    entity_recall: 63.92
    relation_f1: 13.03
    relation_precision: 12.43
    relation_recall: 13.69
    ET_violation: 0.02
    RV_violation: 7.8
    DR_violation: 15
    CF_violation: 0.07
    parse_failures: 0
    docs_processed: 998
- exp_id: 70b_docred_constrained
  name: ''
  status: DONE
  conclusion: success
  metrics:
    ET_violation: 0
    RV_violation: 0
    DR_violation: 0
    CF_violation: 7.01
    entity_f1: 69.05
    entity_precision: 75.03
    entity_recall: 63.95
    relation_f1: 13.07
    relation_precision: 12.54
    relation_recall: 13.64
    parse_failures: 1
    docs_processed: 997
    total_docs: 998
    unique_entities: 12207
    total_triples: 13249
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
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: p8c_ft_scierc_latency
  name: ''
  status: DONE
  conclusion: success
  metrics:
    unconstrained_mean_s: 2.612
    constrained_mean_s: 2.873
    unconstrained_median_s: 2.355
    constrained_median_s: 2.624
    overhead_mean_pct: 10
    overhead_median_pct: 11.42
    per_doc_ratio_mean: 1.205
    per_doc_ratio_median: 1.117
    num_docs: 551
    unconstrained_total_s: 1439
    constrained_total_s: 1582.9
- exp_id: p1_ee_ft_composability
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: p1_ee_ft_composability_r2
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: p1_ee_ft_composability_r3
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: p1_ee_ft_composability_r4
  name: ''
  status: DONE
  conclusion: failed
  metrics:
    unconstrained:
      entity_f1: 0
      trigger_f1: 0.4598
      argument_f1: 0.1581
      rov: 0.251
      ac: 0.06
      cf: 0
      parse_rate: 0.25
    full_s1:
      entity_f1: 0.5823
      trigger_f1: 0.6
      argument_f1: 0.4667
      rov: 0
      ac: 0
      cf: 0.03
      parse_rate: 0.1
- exp_id: p1_ee_ft_llama
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: p1_llama_ee_ft
  name: ''
  status: PREPARING
  conclusion: ''
  metrics: {}
- exp_id: p1_ee_ft_composability_r5
  name: ''
  status: DONE
  conclusion: success
  metrics:
    unconstrained:
      parse_rate: 0.85
      trigger_f1: 0.3208
      argument_f1: 0.0785
      rov_rate: 0.3831
      ac_rate: 0.0268
      go_nogo: 0.41
    full_s1:
      parse_rate: 0.95
      trigger_f1: 0.2672
      argument_f1: 0.0818
      rov_rate: 0
      ac_rate: 0
      go_nogo: 0
- exp_id: p1_ee_ft_llama_r2
  name: ''
  status: DONE
  conclusion: success
  metrics:
    parse_rate_unconstrained: 1
    parse_rate_constrained: 1
    trigger_f1_unconstrained: 0.2752
    trigger_f1_constrained: 0.2691
    argument_f1_unconstrained: 0.0998
    argument_f1_constrained: 0.0891
    entity_f1: 0
    rov_rate_unconstrained: 0.088
    rov_rate_constrained: 0
    ac_rate_unconstrained: 0.035
    ac_rate_constrained: 0.008
    go_nogo_unconstrained: 0.122
    go_nogo_constrained: 0.0078
- exp_id: d062_full_ft_scierc
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    unconstrained:
      entity_f1: 0.6478
      relation_f1: 0.3789
      DR_pct: 2.74
      RV_pct: 0.18
      ET_pct: 0
      CF_pct: 0
    constrained:
      entity_f1: 0.6478
      relation_f1: 0.3789
      DR_pct: 0
      RV_pct: 0
      ET_pct: 0
      CF_pct: 1.31
    training:
      eval_loss_final: 0.09459
      epochs: 3
      total_steps: 333
      training_time: 21m49s
- exp_id: d062_cf_majority_voting
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    qwen_scierc_zs:
      cf_before: 245
      cf_after: 201
      dr_rate_before: 0.0093
      dr_rate_after: 0.0324
    llama_scierc_zs:
      cf_before: 162
      cf_after: 123
      dr_rate_before: 0.0008
      dr_rate_after: 0.0236
    qwen_docred_zs:
      cf_before: 518
      cf_after: 21
      dr_rate_before: 0.1021
      dr_rate_after: 0.1466
    llama_docred_zs:
      cf_before: 1358
      cf_after: 107
      dr_rate_before: 0.0255
      dr_rate_after: 0.1665
    qwen_scierc_ft:
      cf_before: 21
      cf_after: 12
      dr_rate_before: 0
      dr_rate_after: 0.0071
    llama_scierc_ft:
      cf_before: 8
      cf_after: 4
      dr_rate_before: 0.0009
      dr_rate_after: 0.0037
    qwen_docred_ft:
      cf_before: 48
      cf_after: 3
      dr_rate_before: 0.0001
      dr_rate_after: 0.0044
    llama_docred_ft:
      cf_before: 41
      cf_after: 2
      dr_rate_before: 0.0021
      dr_rate_after: 0.005
- exp_id: d062_beam_latency
  name: ''
  status: DONE
  conclusion: success
  metrics:
    beam4_unconstrained_s_per_doc: 3.446
    beam4_constrained_s_per_doc: 4.013
    beam4_unconstrained_total_s: 1898.7
    beam4_constrained_total_s: 2211
    beam_greedy_ratio_unconstrained: 1.319
    beam_greedy_ratio_constrained: 1.397
    constraint_overhead_beam: 1.165
    constraint_overhead_greedy: 1.1
    greedy_unconstrained_s_per_doc: 2.612
    greedy_constrained_s_per_doc: 2.873
- exp_id: d062_ontology_scalability
  name: ''
  status: DONE
  conclusion: success
  metrics:
    compile_small_total_s: 0.334
    compile_medium_total_s: 0.322
    compile_large_total_s: 0.345
    compile_xlarge_total_s: 0.42
    grammar_small_s: 0.333
    grammar_xlarge_s: 0.365
    semantic_small_s: 0.0004
    semantic_xlarge_s: 0.017
    overhead_small: 1.02
    overhead_medium: 1.03
    overhead_large: 1.03
    overhead_xlarge: 1.03
    failures: 0
- exp_id: d063_gollie_violation_rate
  name: ''
  status: DONE
  conclusion: success
  metrics:
    gollie_DR: 0
    gollie_RV: 0
    gollie_ET: 0
    gollie_CF: 0.67
    gollie_entities: 300
    gollie_relations: 7
    gollie_empty_docs_pct: 45
    docs_tested: 100
- exp_id: d064_docred_full_beam
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: d065_tcr_pilot
  name: ''
  status: DONE
  conclusion: success
  metrics:
    scierc_zs_qwen:
      cf_before: 9.75
      cf_after: 0
      dr_before: 0.93
      dr_after: 1.21
      ef1_delta: -0.0129
      fund_pct: 2.04
    scierc_zs_llama:
      cf_before: 6.4
      cf_after: 0
      dr_before: 0.08
      dr_after: 0.3
      ef1_delta: -0.0178
      fund_pct: 1.85
    scierc_lora_qwen:
      cf_before: 1.19
      cf_after: 0
      dr_before: 0
      dr_after: 0
      ef1_delta: -0.0075
      fund_pct: 0
    scierc_lora_llama:
      cf_before: 0.46
      cf_after: 0
      dr_before: 0.09
      dr_after: 0.09
      ef1_delta: -0.0018
      fund_pct: 0
    scierc_zs_mistral:
      cf_before: 0.67
      cf_after: 0
      dr_before: 13.36
      dr_after: 12.87
      ef1_delta: 0.0005
      fund_pct: 0
    docred_zs_qwen:
      cf_before: 13.11
      cf_after: 0
      dr_before: 10.21
      dr_after: 11.74
      ef1_delta: -0.0344
      fund_pct: 13.52
    docred_zs_llama:
      cf_before: 23.71
      cf_after: 0
      dr_before: 2.55
      dr_after: 11.93
      ef1_delta: -0.0521
      fund_pct: 22.78
    docred_zs_70b:
      cf_before: 11.61
      cf_after: 0
      dr_before: 0
      dr_after: 4.2
      ef1_delta: -0.0598
      fund_pct: 18.26
    docred_lora_qwen:
      cf_before: 0.42
      cf_after: 0
      dr_before: 0.01
      dr_after: 0.14
      ef1_delta: -0.0016
      fund_pct: 12.16
    docred_lora_llama:
      cf_before: 0.36
      cf_after: 0
      dr_before: 0.21
      dr_after: 0.2
      ef1_delta: -0.0017
      fund_pct: 11.59
    total_configs: 10
    all_cf_eliminated: true
- exp_id: d065_tcr_full
  name: ''
  status: DONE
  conclusion: success
  metrics:
    configs_tested: 10
    all_cf_eliminated: true
    scierc_all_dr_delta_max: 0.28
    docred_lora_dr_delta_max: 0.14
    docred_zs_llama_dr_delta: 9.38
    docred_zs_70b_dr_delta: 4.2
    docred_zs_qwen_dr_delta: 1.53
    fund_conflict_scierc_max: 2.04
    fund_conflict_docred_zs_max: 22.78
    fund_conflict_docred_lora_max: 12.16
    lora_ef1_cost_max: 0.0075
    zs_docred_ef1_cost_max: 0.0598
- exp_id: d068_constraint_guided_beam_pilot
  name: ''
  status: DONE
  conclusion: negative
  metrics: {}
- exp_id: d066_beam_sweep
  name: ''
  status: ANALYZING
  conclusion: ''
  metrics:
    scierc_qwen3_8b:
      k1_unc:
        E_F1: 66.88
        R_F1: 42.95
        DR_pct: 2.11
        CF_pct: 0
        avg_time: 2.494
      k1_con:
        E_F1: 66.88
        R_F1: 42.95
        DR_pct: 0
        CF_pct: 0.5
        avg_time: 2.932
      k2_unc:
        E_F1: 67.79
        R_F1: 44.75
        DR_pct: 1.54
        CF_pct: 0
        avg_time: 2.954
      k2_con:
        E_F1: 67.71
        R_F1: 44.6
        DR_pct: 0
        CF_pct: 0.11
        avg_time: 3.463
      k4_unc:
        E_F1: 67.49
        R_F1: 43.72
        DR_pct: 1.89
        CF_pct: 0
        avg_time: 3.485
      k4_con:
        E_F1: 67.22
        R_F1: 43.6
        DR_pct: 0
        CF_pct: 0
        avg_time: 4.069
      k8_unc:
        E_F1: 66.4
        R_F1: 43.17
        DR_pct: 1.77
        CF_pct: 0
        avg_time: 4.194
      k8_con:
        E_F1: 66.36
        R_F1: 43.65
        DR_pct: 0
        CF_pct: 0
        avg_time: 5.058
    pareto_optimal: k=2 con
    best_E_F1:
      config: k=2 unc
      value: 67.79
    best_R_F1:
      config: k=2 unc
      value: 44.75
- exp_id: d067_seed_variance
  name: ''
  status: DONE
  conclusion: success
  metrics:
    qwen_scierc_unc:
      E_F1: 66.94 ± 0.08
      R_F1: 43.25 ± 0.43
      DR: 2.06 ± 0.08
      CF: 0.00 ± 0.00
    qwen_scierc_con:
      E_F1: 66.94 ± 0.08
      R_F1: 43.22 ± 0.39
      DR: 0.00 ± 0.00
      CF: 0.48 ± 0.02
    llama_scierc_unc:
      E_F1: 67.99 ± 0.16
      R_F1: 45.38 ± 0.05
      DR: 1.04 ± 0.05
      CF: 0.00 ± 0.00
    llama_scierc_con:
      E_F1: 67.99 ± 0.16
      R_F1: 45.40 ± 0.05
      DR: 0.03 ± 0.04
      CF: 0.26 ± 0.02
    max_sigma_pp: 0.43
    greedy_deterministic: true
    snr_dr_improvement: '>12x'
    qwen_docred_status: pending (not started)
    llama_scierc_seed456_con_status: running (407/551)
- exp_id: d066_docred_beam_sweep
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: d065_qwen_greedy_4096
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: d065_qwen_greedy_4096_r2
  name: ''
  status: DONE
  conclusion: success
  metrics:
    E-F1: 81.87
    R-F1: 40.79
    DR_pct: 0
    CF_pct: 0.22
    ET_pct: 0
    RV_pct: 0
    PF_pct: 8.52
    samples: 998
- exp_id: d066_sweep_16980_gpu1
  name: ''
  status: DONE
  conclusion: success
  metrics: {}
- exp_id: d066_sweep_21461_gpu1
  name: ''
  status: DONE
  conclusion: success
  metrics:
    total: 551
    E_F1: 66.36
    R_F1: 43.65
    DR_pct: 0
    CF_pct: 0
    ET_pct: 0
    RV_pct: 0
    avg_time_s: 5.058
    output_file: qwen_scierc_beam8_full_s1.jsonl
    note: Actually ran on SciERC 551 docs (not DocRED 200 as originally recorded in
      hypothesis)
- exp_id: d066_sweep_llama_beam2_s1
  name: ''
  status: DONE
  conclusion: success
  metrics:
    E_F1: 85.6
    E_P: 85.29
    E_R: 85.92
    R_F1: 51.17
    R_P: 48.51
    R_R: 54.14
    DR_pct: 0
    CF_pct: 0
    ET_pct: 0
    RV_pct: 0
    parse_fail_pct: 0.5
    total_samples: 200
    total_entities_pred: 3814
    total_relations_pred: 2839
- exp_id: d066_sweep_llama_beam8_unc
  name: ''
  status: DONE
  conclusion: success
  metrics:
    E_F1: 85.77
    E_P: 85.7
    E_R: 85.84
    R_F1: 51.97
    R_P: 49.76
    R_R: 54.38
    DR_pct: 0
    CF_pct: 0.05
    ET_pct: 0
    RV_pct: 0.07
    parse_fail_pct: 0.5
    total_samples: 200
    total_entities_pred: 3788
    total_relations_pred: 2779
- exp_id: d066_sweep_llama_scierc_beam1_unc
  name: ''
  status: DONE
  conclusion: failed
  metrics:
    total: 275
    success: 275
    fail: 0
    output_file: llama_scierc_beam1_unconstrained.jsonl
    note: 'INVALIDATED: Used dev set (275 docs) instead of test set (551 docs). Not
      comparable with other beam sweep results. Llama SciERC beam sweep deprioritized
      — must use scripts/d066_beam_sweep_scierc.sh with --data_path data/processed_data/test.json
      if rerun.'
- exp_id: d066_sweep_llama_beam8_s1
  name: ''
  status: DONE
  conclusion: success
  metrics:
    E-F1: 85.76
    R-F1: 51.74
    DR_pct: 0
    CF_pct: 0
    PF_pct: 0.5
    samples: 200
- exp_id: d066_sweep_llama_docred_beam1_unc
  name: ''
  status: DONE
  conclusion: success
  metrics:
    total: 200
    success: 196
    fail: 4
    output_file: llama_docred_200_beam1_unconstrained.jsonl
- exp_id: d066_sweep_llama_docred_beam1_s1
  name: ''
  status: DONE
  conclusion: success
  metrics:
    E-F1: 85.43
    R-F1: 47.35
    DR_pct: 0
    CF_pct: 0.19
    PF_pct: 2
    samples: 200
- exp_id: d066_sweep_llama_docred_beam4_unc
  name: ''
  status: DONE
  conclusion: success
  metrics:
    E-F1: 85.67
    R-F1: 52.65
    DR_pct: 0.04
    CF_pct: 0.08
    PF_pct: 0.5
    samples: 200
- exp_id: d066_sweep_llama_docred_beam4_s1
  name: ''
  status: DONE
  conclusion: success
  metrics:
    E-F1: 85.61
    E-P: 85.48
    E-R: 85.73
    R-F1: 51.89
    R-P: 51.59
    R-R: 52.2
    DR_pct: 0
    CF_pct: 0
    PF_pct: 0.5
    ET_pct: 0
    RV_pct: 0
    samples: 200
    parse_fail: 1
- exp_id: d066_sweep_llama_scierc_beam4_s1_551
  name: ''
  status: DONE
  conclusion: success
  metrics:
    E-F1: 68.06
    E-P: 65.96
    E-R: 70.29
    R-F1: 46.18
    R-P: 42.1
    R-R: 51.13
    ET_pct: 0
    RV_pct: 0
    DR_pct: 0
    CF_pct: 0
    parse_fail: 0
    samples: 551
    note: 'ET/RV corrected from 100→0: original eval used hardcoded DocRED ontology,
      re-evaled with --dataset scierc'
- exp_id: d066_sweep_llama_scierc_beam2_s1_551
  name: ''
  status: DONE
  conclusion: success
  metrics:
    entity_f1: 68.34
    entity_p: 66.59
    entity_r: 70.17
    relation_f1: 46.12
    relation_p: 42.73
    relation_r: 50.1
    parse_fail_pct: 0
    ET_pct: 0
    RV_pct: 0
    DR_pct: 0
    CF_pct: 0.17
    note: 'ET/RV corrected from 100→0: original eval used hardcoded DocRED ontology,
      re-evaled with --dataset scierc'
- exp_id: d066_sweep_llama_scierc_beam8_s1_551
  name: ''
  status: DONE
  conclusion: success
  metrics:
    E-F1: 67.51
    E-P: 64.99
    E-R: 70.23
    R-F1: 44.95
    R-P: 40.1
    R-R: 51.13
    ET_pct: 0
    RV_pct: 0
    DR_pct: 0
    CF_pct: 0
    PF_pct: 0
    samples: 551
    note: Reconcile false positive corrected. Eval with --dataset scierc confirmed.
- exp_id: r14_qwen_docred_beam4_998
  name: ''
  status: DONE
  conclusion: success
  metrics:
    E_F1: 58.19
    R_F1: 8.72
    DR_pct: 0
    RV_pct: 0
    ET_pct: 0
    CF_pct: 4.94
    parse_fail_pct: 3.51
    samples: 998
    success: 963
    fail: 35
- exp_id: r14_llama_docred_beam4_998
  name: ''
  status: DONE
  conclusion: success
  metrics:
    R_F1: 8.83
    E_F1: 57.81
    DR_pct: 0
    CF_pct: 1
    ET_pct: 0
    RV_pct: 0
    parse_fail_pct: 3.91
    samples: 998
    success: 959
    fail: 39
    baseline_ZS_greedy_R_F1: 6.27
    baseline_ZS_greedy_E_F1: 54.93
    baseline_ZS_greedy_DR_pct: 2.55
    baseline_ZS_greedy_CF_pct: 8.54
- exp_id: r16_trie_qwen_ft_scierc
  name: ''
  status: DONE
  conclusion: success
  metrics:
    E_F1: 66.73
    R_F1: 42.57
    ET_pct: 0
    RV_pct: 0
    DR_pct: 95.5
    CF_pct: 0.09
    parse_fail_pct: 9.1
    samples: 551
- exp_id: r16_trie_qwen_zs_scierc
  name: ''
  status: DONE
  conclusion: success
  metrics:
    E_F1: 30.97
    R_F1: 8.64
    ET_pct: 0
    RV_pct: 0
    DR_pct: 29.3
    CF_pct: 0
    parse_fail_pct: 0
    samples: 551
- exp_id: r16_trie_llama_ft_scierc
  name: ''
  status: DONE
  conclusion: success
  metrics:
    E_F1: 65.37
    R_F1: 41.42
    ET_pct: 0
    RV_pct: 0
    DR_pct: 15.2
    CF_pct: 0
    parse_fail_pct: 50.8
    samples: 551
- exp_id: r16_trie_llama_zs_scierc
  name: ''
  status: DONE
  conclusion: success
  metrics:
    E_F1: 23.23
    R_F1: 2.9
    ET_pct: 0
    RV_pct: 0
    DR_pct: 84.4
    CF_pct: 0.36
    parse_fail_pct: 0
    samples: 551
- exp_id: r16_70b_scierc_zs_s1
  name: ''
  status: DONE
  conclusion: success
  metrics:
    E_F1: 35.19
    R_F1: 11.24
    DR_pct: 0
    RV_pct: 0
    ET_pct: 0
    CF_pct: 3.5
    parse_fail_pct: 0
    samples: 551
    baseline_unc_E_F1: 35.21
    baseline_unc_R_F1: 11.15
    baseline_unc_DR_pct: 6.41
    baseline_unc_RV_pct: 0.61
    baseline_unc_CF_pct: 0
- exp_id: r16_70b_docred_zs_s1
  name: ''
  status: DONE
  conclusion: success
  metrics:
    E_F1: 69.11
    R_F1: 13.05
    DR_pct: 0
    RV_pct: 0
    ET_pct: 0
    CF_pct: 0.04
    parse_fail_pct: 0.1
    samples: 998
    total_entities: 16599
    total_triples: 13239
    baseline_unc_DR_pct: 14.98
    baseline_unc_R_F1: 13.01
    note: Metrics corrected via eval_d064.py with DocRED schema mapping. Original
      violation_checker.py gave R-F1=0 due to SciERC schema mismatch.
- exp_id: r16_70b_lora_scierc
  name: ''
  status: DONE
  conclusion: success
  metrics:
    eval_loss: 0.0611
    token_acc: 97.78
    steps_completed: 663
    epochs: 3
    train_loss_start: 0.183
    train_loss_end: 0.041
- exp_id: r16_70b_lora_docred
  name: ''
  status: DONE
  conclusion: success
  metrics:
    eval_loss: 0.0635
    token_acc: 97.94
    steps_completed: 1146
    epochs: 3
    train_loss_start: 0.147
    train_loss_end: 0.056
- exp_id: eval_70b_lora_scierc_unconstrained
  name: ''
  status: DONE
  conclusion: success
  metrics: {}
- exp_id: r16_70b_lora_scierc_eval
  name: ''
  status: PREPARING
  conclusion: ''
  metrics: {}
- exp_id: eval_70b_lora_docred_200_unconstrained
  name: ''
  status: RUNNING
  conclusion: ''
  metrics: {}

# 输出格式（YAML，仅输出一个 ```yaml 块）

```yaml
tier: worst
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

重要：tables 中使用 YAML flow sequence 时，所有字符串必须加双引号（如 `columns: ["Judge", "Biased?"]`），否则 `?` `:` 等字符会导致解析失败。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "4dbb97d9-fc82-4efe-b694-2a73482dbb33",
  "type": "user",
  "uuid": "a3fd081d-d0f7-4b69-b154-9659a167d4d2",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6",
  "sessionId": "8b60bbb7-357b-4091-8cce-e13fa8ccd284",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-22T05:50:11.297Z_

```json
{
  "parentUuid": "a3fd081d-d0f7-4b69-b154-9659a167d4d2",
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
  "uuid": "cd170e7a-a646-4951-aa86-939a1d73be49",
  "timestamp": "2026-05-22T05:50:11.297Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6",
  "sessionId": "8b60bbb7-357b-4091-8cce-e13fa8ccd284",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-22T05:50:11.297Z_

```json
{
  "parentUuid": "cd170e7a-a646-4951-aa86-939a1d73be49",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "9c046120-f144-4fc2-ba93-c6bf96489cf4",
  "timestamp": "2026-05-22T05:50:11.297Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6",
  "sessionId": "8b60bbb7-357b-4091-8cce-e13fa8ccd284",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：≥2 reviewers 认为 novelty 不足以支撑 main conference；核心 'guaranteed compliance' claim 被 CF 数据和 post-hoc 比较削弱；需要 reframe 切入角度 核心假设：[\"Novelty 被拒：'constrained decod…",
  "leafUuid": "9c046120-f144-4fc2-ba93-c6bf96489cf4",
  "sessionId": "8b60bbb7-357b-4091-8cce-e13fa8ccd284"
}
```

---

### Assistant

_source line 7 · 2026-05-22T05:50:15.454Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed predicted results for each planned experiment in the experiment_plan, under the "worst" tier scenario they've defined. Let me first find the experiment_plan file to see what experiments are planned.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9c046120-f144-4fc2-ba93-c6bf96489cf4",
  "isSidechain": false,
  "requestId": "req_011CbH5p6k7FSsVgomKiuFGs",
  "type": "assistant",
  "uuid": "7c09748d-d528-4fdb-88da-6f89a2e741c0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6",
  "sessionId": "8b60bbb7-357b-4091-8cce-e13fa8ccd284",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014du4NejzDvxdk1Zxhva1ue",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 43688,
      "cache_read_input_tokens": 11841,
      "output_tokens": 171,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 43688,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 171,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 43688,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 43688
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

_source line 8 · 2026-05-22T05:50:15.953Z_

Let me find the experiment plan to see what experiments are planned.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7c09748d-d528-4fdb-88da-6f89a2e741c0",
  "isSidechain": false,
  "requestId": "req_011CbH5p6k7FSsVgomKiuFGs",
  "type": "assistant",
  "uuid": "9ceb0ea2-aafc-411d-b35a-682933d6c433",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6",
  "sessionId": "8b60bbb7-357b-4091-8cce-e13fa8ccd284",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014du4NejzDvxdk1Zxhva1ue",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 43688,
      "cache_read_input_tokens": 11841,
      "output_tokens": 171,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 43688,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 171,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 43688,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 43688
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

_source line 9 · 2026-05-22T05:50:16.451Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01LDCLn4UjBFoiriVNuDdhSw`</summary>

```json
{
  "pattern": "**/experiment_plan*"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9ceb0ea2-aafc-411d-b35a-682933d6c433",
  "isSidechain": false,
  "requestId": "req_011CbH5p6k7FSsVgomKiuFGs",
  "type": "assistant",
  "uuid": "7983bd34-734f-4adf-93b4-660914b3e43f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6",
  "sessionId": "8b60bbb7-357b-4091-8cce-e13fa8ccd284",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014du4NejzDvxdk1Zxhva1ue",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 43688,
      "cache_read_input_tokens": 11841,
      "output_tokens": 171,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 43688,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 171,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 43688,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 43688
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

_source line 10 · 2026-05-22T05:50:16.572Z_

<details><summary>↩ Tool result · `toolu_01LDCLn4UjBFoiriVNuDdhSw`</summary>

```text
projects/prov_grounded_uie/experiment_plan.yaml
projects/schema_semantic_constrained_ie/experiment_plan.lock
projects/schema_semantic_constrained_ie/artifacts/llama_docred_maxtoken/experiment_plan.md
projects/schema_semantic_constrained_ie/experiment_plan.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1d0bc3f8-2403-4d7d-ac7c-01c1c274dbca",
  "isSidechain": false,
  "promptId": "4dbb97d9-fc82-4efe-b694-2a73482dbb33",
  "type": "user",
  "uuid": "29390f98-e8a4-4533-aecf-200962464fc5",
  "toolUseResult": {
    "filenames": [
      "projects/prov_grounded_uie/experiment_plan.yaml",
      "projects/schema_semantic_constrained_ie/experiment_plan.lock",
      "projects/schema_semantic_constrained_ie/artifacts/llama_docred_maxtoken/experiment_plan.md",
      "projects/schema_semantic_constrained_ie/experiment_plan.yaml"
    ],
    "durationMs": 111,
    "numFiles": 4,
    "truncated": false
  },
  "sourceToolAssistantUUID": "7983bd34-734f-4adf-93b4-660914b3e43f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6",
  "sessionId": "8b60bbb7-357b-4091-8cce-e13fa8ccd284",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-22T05:50:16.555Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01GpqZ1nwZ5r6YkApgamjAoG`</summary>

```json
{
  "pattern": "**/*plan*"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7983bd34-734f-4adf-93b4-660914b3e43f",
  "isSidechain": false,
  "requestId": "req_011CbH5p6k7FSsVgomKiuFGs",
  "type": "assistant",
  "uuid": "1d0bc3f8-2403-4d7d-ac7c-01c1c274dbca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6",
  "sessionId": "8b60bbb7-357b-4091-8cce-e13fa8ccd284",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014du4NejzDvxdk1Zxhva1ue",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 43688,
      "cache_read_input_tokens": 11841,
      "output_tokens": 171,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 43688,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 171,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 43688,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 43688
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

_source line 12 · 2026-05-22T05:50:16.699Z_

<details><summary>↩ Tool result · `toolu_01GpqZ1nwZ5r6YkApgamjAoG`</summary>

```text
projects/prov_grounded_uie/artifacts/.venv/lib/python3.14/site-packages/pyarrow/include/arrow/acero/exec_plan.h
projects/prov_grounded_uie/artifacts/.venv/lib/python3.14/site-packages/pyarrow/include/arrow/dataset/plan.h
projects/prov_grounded_uie/artifacts/.venv/lib/python3.14/site-packages/pyarrow/include/arrow/engine/substrait/test_plan_builder.h
projects/prov_grounded_uie/artifacts/.venv/lib/python3.14/site-packages/pyarrow/tests/test_exec_plan.py
projects/prov_grounded_uie/artifacts/.venv/lib/python3.14/site-packages/pyarrow/tests/__pycache__/test_exec_plan.cpython-314.pyc
projects/prov_grounded_uie/artifacts/.venv/lib/python3.14/site-packages/sympy/geometry/plane.py
projects/prov_grounded_uie/artifacts/.venv/lib/python3.14/site-packages/sympy/geometry/tests/test_plane.py
projects/prov_grounded_uie/artifacts/.venv/lib/python3.14/site-packages/sympy/geometry/__pycache__/plane.cpython-314.pyc
projects/prov_grounded_uie/artifacts/.venv/lib/python3.14/site-packages/sympy/geometry/tests/__pycache__/test_plane.cpython-314.pyc
projects/prov_grounded_uie/artifacts/.venv/lib/python3.14/site-packages/networkx/algorithms/planar_drawing.py
projects/prov_grounded_uie/artifacts/.venv/lib/python3.14/site-packages/networkx/algorithms/planarity.py
projects/prov_grounded_uie/artifacts/.venv/lib/python3.14/site-packages/networkx/algorithms/tests/test_planar_drawing.py
projects/prov_grounded_uie/artifacts/.venv/lib/python3.14/site-packages/networkx/algorithms/tests/test_planarity.py
projects/prov_grounded_uie/artifacts/.venv/lib/python3.14/site-packages/networkx/algorithms/__pycache__/planar_drawing.cpython-314.pyc
projects/prov_grounded_uie/artifacts/.venv/lib/python3.14/site-packages/networkx/algorithms/__pycache__/planarity.cpython-314.pyc
projects/prov_grounded_uie/artifacts/.venv/lib/python3.14/site-packages/networkx/algorithms/tests/__pycache__/test_planar_drawing.cpython-314.pyc
projects/prov_grounded_uie/artifacts/.venv/lib/python3.14/site-packages/networkx/algorithms/tests/__pycache__/test_planarity.cpython-314.pyc
projects/prov_grounded_uie/artifacts/.venv/lib/python3.14/site-packages/torch/_inductor/codegen/memory_planning.py
projects/prov_grounded_uie/artifacts/.venv/lib/python3.14/site-packages/torch/distributed/checkpoint/_dedup_save_plans.py
projects/prov_grounded_uie/artifacts/.venv/lib/python3.14/site-packages/torch/distributed/checkpoint/default_planner.py
projects/prov_grounded_uie/artifacts/.venv/lib/python3.14/site-packages/torch/distributed/checkpoint/planner.py
projects/prov_grounded_uie/artifacts/.venv/lib/python3.14/site-packages/torch/distributed/checkpoint/planner_helpers.py
projects/prov_grounded_uie/artifacts/.venv/lib/python3.14/site-packages/torch/distributed/elastic/control_plane.py
projects/prov_grounded_uie/artifacts/.venv/lib/python3.14/site-packages/torch/include/ATen/ops/_cufft_clear_plan_cache.h
projects/prov_grounded_uie/artifacts/.venv/lib/python3.14/site-packages/torch/include/ATen/ops/_cufft_clear_plan_cache_compositeimplicitautograd_dispatch.h
projects/prov_grounded_uie/artifacts/.venv/lib/python3.14/site-packages/torch/include/ATen/ops/_cufft_clear_plan_cache_native.h
projects/prov_grounded_uie/artifacts/.venv/lib/python3.14/site-packages/torch/include/ATen/ops/_cufft_clear_plan_cache_ops.h
projects/prov_grounded_uie/artifacts/.venv/lib/python3.14/site-packages/torch/include/ATen/ops/_cufft_get_plan_cache_max_size.h
projects/prov_grounded_uie/artifacts/.venv/lib/python3.14/site-packages/torch/include/ATen/ops/_cufft_get_plan_cache_max_size_compositeimplicitautograd_dispatch.h
projects/prov_grounded_uie/artifacts/.venv/lib/python3.14/site-packages/torch/include/ATen/ops/_cufft_get_plan_cache_max_size_native.h
projects/prov_grounded_uie/artifacts/.venv/lib/python3.14/site-packages/torch/include/ATen/ops/_cufft_get_plan_cache_max_size_ops.h
projects/prov_grounded_uie/artifacts/.venv/lib/python3.14/site-packages/torch/include/ATen/ops/_cufft_get_plan_cache_size.h
projects/prov_grounded_uie/artifacts/.venv/lib/python3.14/site-packages/torch/include/ATen/ops/_cufft_get_plan_cache_size_compositeimplicitautograd_dispatch.h
projects/prov_grounded_uie/artifacts/.venv/lib/python3.14/site-packages/torch/include/ATen/ops/_cufft_get_plan_cache_size_native.h
projects/prov_grounded_uie/artifacts/.venv/lib/python3.14/site-packages/torch/include/ATen/ops/_cufft_get_plan_cache_size_ops.h
projects/prov_grounded_uie/artifacts/.venv/lib/python3.14/site-packages/torch/include/ATen/ops/_cufft_set_plan_cache_max_size.h
projects/prov_grounded_uie/artifacts/.venv/lib/python3.14/site-packages/torch/include/ATen/ops/_cufft_set_plan_cache_max_size_compositeimplicitautograd_dispatch.h
projects/prov_grounded_uie/artifacts/.venv/lib/python3.14/site-packages/torch/include/ATen/ops/_cufft_set_plan_cache_max_size_native.h
projects/prov_grounded_uie/artifacts/.venv/lib/python3.14/site-packages/torch/include/ATen/ops/_cufft_set_plan_cache_max_size_ops.h
projects/prov_grounded_uie/artifacts/.venv/lib/python3.14/site-packages/torch/include/torch/csrc/jit/runtime/static/memory_planner.h
projects/prov_grounded_uie/artifacts/.venv/lib/python3.14/site-packages/torch/_inductor/codegen/__pycache__/memory_planning.cpython-314.pyc
projects/prov_grounded_uie/artifacts/.venv/lib/python3.14/site-packages/torch/distributed/checkpoint/__pycache__/_dedup_save_plans.cpython-314.pyc
projects/prov_grounded_uie/artifacts/.venv/lib/python3.14/site-packages/torch/distributed/checkpoint/__pycache__/default_planner.cpython-314.pyc
projects/prov_grounded_uie/artifacts/.venv/lib/python3.14/site-packages/torch/distributed/checkpoint/__pycache__/planner.cpython-314.pyc
projects/prov_grounded_uie/artifacts/.venv/lib/python3.14/site-packages/torch/distributed/checkpoint/__pycache__/planner_helpers.cpython-314.pyc
projects/prov_grounded_uie/artifacts/.venv/lib/python3.14/site-packages/torch/distributed/elastic/__pycache__/control_plane.cpython-314.pyc
projects/prov_grounded_uie/logs/workers/worker_code_experiment-plan_20260512T114557.log
projects/prov_grounded_uie/logs/workers/worker_code_experiment-plan_20260512T114557_result.json
projects/prov_grounded_uie/experiment_plan.yaml
projects/schema_semantic_constrained_ie/experiment_plan.lock
projects/schema_semantic_constrained_ie/writing_plan.yaml
projects/schema_semantic_constrained_ie/artifacts/llama_docred_maxtoken/experiment_plan.md
projects/schema_semantic_constrained_ie/logs/workers/worker_research_pair_based_impl_plan_20260515T141200.log
projects/schema_semantic_constrained_ie/logs/chats/worker_research_pair_based_impl_plan_20260515T141200.lock
projects/schema_semantic_constrained_ie/logs/chats/worker_research_pair_based_impl_plan_20260515T141200.jsonl
projects/schema_semantic_constrained_ie/logs/workers/worker_research_pair_based_impl_plan_20260515T141200_retry1.log
projects/schema_semantic_constrained_ie/artifacts/pair_based_enforcement_plan.md
projects/schema_semantic_constrained_ie/logs/workers/worker_research_pair_based_impl_plan_20260515T141200_retry2.log
projects/schema_semantic_constrained_ie/logs/workers/worker_research_pair_based_impl_plan_20260515T141200_result.json
projects/schema_semantic_constrained_ie/experiment_plan.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1d0bc3f8-2403-4d7d-ac7c-01c1c274dbca",
  "isSidechain": false,
  "promptId": "4dbb97d9-fc82-4efe-b694-2a73482dbb33",
  "type": "user",
  "uuid": "1e550fde-3405-4ac8-83bb-aa8347a0e956",
  "toolUseResult": {
    "filenames": [
      "projects/prov_grounded_uie/artifacts/.venv/lib/python3.14/site-packages/pyarrow/include/arrow/acero/exec_plan.h",
      "projects/prov_grounded_uie/artifacts/.venv/lib/python3.14/site-packages/pyarrow/include/arrow/dataset/plan.h",
      "projects/prov_grounded_uie/artifacts/.venv/lib/python3.14/site-packages/pyarrow/include/arrow/engine/substrait/test_plan_builder.h",
      "projects/prov_grounded_uie/artifacts/.venv/lib/python3.14/site-packages/pyarrow/tests/test_exec_plan.py",
      "projects/prov_grounded_uie/artifacts/.venv/lib/python3.14/site-packages/pyarrow/tests/__pycache__/test_exec_plan.cpython-314.pyc",
      "projects/prov_grounded_uie/artifacts/.venv/lib/python3.14/site-packages/sympy/geometry/plane.py",
      "projects/prov_grounded_uie/artifacts/.venv/lib/python3.14/site-packages/sympy/geometry/tests/test_plane.py",
      "projects/prov_grounded_uie/artifacts/.venv/lib/python3.14/site-packages/sympy/geometry/__pycache__/plane.cpython-314.pyc",
      "projects/prov_grounded_uie/artifacts/.venv/lib/python3.14/site-packages/sympy/geometry/tests/__pycache__/test_plane.cpython-314.pyc",
      "projects/prov_grounded_uie/artifacts/.venv/lib/python3.14/site-packages/networkx/algorithms/planar_drawing.py",
      "projects/prov_grounded_uie/artifacts/.venv/lib/python3.14/site-packages/networkx/algorithms/planarity.py",
      "projects/prov_grounded_uie/artifacts/.venv/lib/python3.14/site-packages/networkx/algorithms/tests/test_planar_drawing.py",
      "projects/prov_grounded_uie/artifacts/.venv/lib/python3.14/site-packages/networkx/algorithms/tests/test_planarity.py",
      "projects/prov_grounded_uie/artifacts/.venv/lib/python3.14/site-packages/networkx/algorithms/__pycache__/planar_drawing.cpython-314.pyc",
      "projects/prov_grounded_uie/artifacts/.venv/lib/python3.14/site-packages/networkx/algorithms/__pycache__/planarity.cpython-314.pyc",
      "projects/prov_grounded_uie/artifacts/.venv/lib/python3.14/site-packages/networkx/algorithms/tests/__pycache__/test_planar_drawing.cpython-314.pyc",
      "projects/prov_grounded_uie/artifacts/.venv/lib/python3.14/site-packages/networkx/algorithms/tests/__pycache__/test_planarity.cpython-314.pyc",
      "projects/prov_grounded_uie/artifacts/.venv/lib/python3.14/site-packages/torch/_inductor/codegen/memory_planning.py",
      "projects/prov_grounded_uie/artifacts/.venv/lib/python3.14/site-packages/torch/distributed/checkpoint/_dedup_save_plans.py",
      "projects/prov_grounded_uie/artifacts/.venv/lib/python3.14/site-packages/torch/distributed/checkpoint/default_planner.py",
      "projects/prov_grounded_uie/artifacts/.venv/lib/python3.14/site-packages/torch/distributed/checkpoint/planner.py",
      "projects/prov_grounded_uie/artifacts/.venv/lib/python3.14/site-packages/torch/distributed/checkpoint/planner_helpers.py",
      "projects/prov_grounded_uie/artifacts/.venv/lib/python3.14/site-packages/torch/distributed/elastic/control_plane.py",
      "projects/prov_grounded_uie/artifacts/.venv/lib/python3.14/site-packages/torch/include/ATen/ops/_cufft_clear_plan_cache.h",
      "projects/prov_grounded_uie/artifacts/.venv/lib/python3.14/site-packages/torch/include/ATen/ops/_cufft_clear_plan_cache_compositeimplicitautograd_dispatch.h",
      "projects/prov_grounded_uie/artifacts/.venv/lib/python3.14/site-packages/torch/include/ATen/ops/_cufft_clear_plan_cache_native.h",
      "projects/prov_grounded_uie/artifacts/.venv/lib/python3.14/site-packages/torch/include/ATen/ops/_cufft_clear_plan_cache_ops.h",
      "projects/prov_grounded_uie/artifacts/.venv/lib/python3.14/site-packages/torch/include/ATen/ops/_cufft_get_plan_cache_max_size.h",
      "projects/prov_grounded_uie/artifacts/.venv/lib/python3.14/site-packages/torch/include/ATen/ops/_cufft_get_plan_cache_max_size_compositeimplicitautograd_dispatch.h",
      "projects/prov_grounded_uie/artifacts/.venv/lib/python3.14/site-packages/torch/include/ATen/ops/_cufft_get_plan_cache_max_size_native.h",
      "projects/prov_grounded_uie/artifacts/.venv/lib/python3.14/site-packages/torch/include/ATen/ops/_cufft_get_plan_cache_max_size_ops.h",
      "projects/prov_grounded_uie/artifacts/.venv/lib/python3.14/site-packages/torch/include/ATen/ops/_cufft_get_plan_cache_size.h",
      "projects/prov_grounded_uie/artifacts/.venv/lib/python3.14/site-packages/torch/include/ATen/ops/_cufft_get_plan_cache_size_compositeimplicitautograd_dispatch.h",
      "projects/prov_grounded_uie/artifacts/.venv/lib/python3.14/site-packages/torch/include/ATen/ops/_cufft_get_plan_cache_size_native.h",
      "projects/prov_grounded_uie/artifacts/.venv/lib/python3.14/site-packages/torch/include/ATen/ops/_cufft_get_plan_cache_size_ops.h",
      "projects/prov_grounded_uie/artifacts/.venv/lib/python3.14/site-packages/torch/include/ATen/ops/_cufft_set_plan_cache_max_size.h",
      "projects/prov_grounded_uie/artifacts/.venv/lib/python3.14/site-packages/torch/include/ATen/ops/_cufft_set_plan_cache_max_size_compositeimplicitautograd_dispatch.h",
      "projects/prov_grounded_uie/artifacts/.venv/lib/python3.14/site-packages/torch/include/ATen/ops/_cufft_set_plan_cache_max_size_native.h",
      "projects/prov_grounded_uie/artifacts/.venv/lib/python3.14/site-packages/torch/include/ATen/ops/_cufft_set_plan_cache_max_size_ops.h",
      "projects/prov_grounded_uie/artifacts/.venv/lib/python3.14/site-packages/torch/include/torch/csrc/jit/runtime/static/memory_planner.h",
      "projects/prov_grounded_uie/artifacts/.venv/lib/python3.14/site-packages/torch/_inductor/codegen/__pycache__/memory_planning.cpython-314.pyc",
      "projects/prov_grounded_uie/artifacts/.venv/lib/python3.14/site-packages/torch/distributed/checkpoint/__pycache__/_dedup_save_plans.cpython-314.pyc",
      "projects/prov_grounded_uie/artifacts/.venv/lib/python3.14/site-packages/torch/distributed/checkpoint/__pycache__/default_planner.cpython-314.pyc",
      "projects/prov_grounded_uie/artifacts/.venv/lib/python3.14/site-packages/torch/distributed/checkpoint/__pycache__/planner.cpython-314.pyc",
      "projects/prov_grounded_uie/artifacts/.venv/lib/python3.14/site-packages/torch/distributed/checkpoint/__pycache__/planner_helpers.cpython-314.pyc",
      "projects/prov_grounded_uie/artifacts/.venv/lib/python3.14/site-packages/torch/distributed/elastic/__pycache__/control_plane.cpython-314.pyc",
      "projects/prov_grounded_uie/logs/workers/worker_code_experiment-plan_20260512T114557.log",
      "projects/prov_grounded_uie/logs/workers/worker_code_experiment-plan_20260512T114557_result.json",
      "projects/prov_grounded_uie/experiment_plan.yaml",
      "projects/schema_semantic_constrained_ie/experiment_plan.lock",
      "projects/schema_semantic_constrained_ie/writing_plan.yaml",
      "projects/schema_semantic_constrained_ie/artifacts/llama_docred_maxtoken/experiment_plan.md",
      "projects/schema_semantic_constrained_ie/logs/workers/worker_research_pair_based_impl_plan_20260515T141200.log",
      "projects/schema_semantic_constrained_ie/logs/chats/worker_research_pair_based_impl_plan_20260515T141200.lock",
      "projects/schema_semantic_constrained_ie/logs/chats/worker_research_pair_based_impl_plan_20260515T141200.jsonl",
      "projects/schema_semantic_constrained_ie/logs/workers/worker_research_pair_based_impl_plan_20260515T141200_retry1.log",
      "projects/schema_semantic_constrained_ie/artifacts/pair_based_enforcement_plan.md",
      "projects/schema_semantic_constrained_ie/logs/workers/worker_research_pair_based_impl_plan_20260515T141200_retry2.log",
      "projects/schema_semantic_constrained_ie/logs/workers/worker_research_pair_based_impl_plan_20260515T141200_result.json",
      "projects/schema_semantic_constrained_ie/experiment_plan.yaml"
    ],
    "durationMs": 140,
    "numFiles": 60,
    "truncated": false
  },
  "sourceToolAssistantUUID": "1d0bc3f8-2403-4d7d-ac7c-01c1c274dbca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6",
  "sessionId": "8b60bbb7-357b-4091-8cce-e13fa8ccd284",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Ontology constraint violations in LLM-based IE—worst case analysis",
  "sessionId": "8b60bbb7-357b-4091-8cce-e13fa8ccd284"
}
```

---

### Tool call

_source line 14 · 2026-05-22T05:50:20.935Z_

<details open><summary>🔧 Tool call — Read · `toolu_01EeZqnsthUDSaeeLVAQsi6T`</summary>

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
  "parentUuid": "1e550fde-3405-4ac8-83bb-aa8347a0e956",
  "isSidechain": false,
  "requestId": "req_011CbH5pW3ZowEXHi1DWEnr6",
  "type": "assistant",
  "uuid": "78622efa-0c44-40bd-b4ef-7fc26c17ff90",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6",
  "sessionId": "8b60bbb7-357b-4091-8cce-e13fa8ccd284",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YPaRNu7QjACTte42zKU1bU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2949,
      "cache_read_input_tokens": 55529,
      "output_tokens": 88,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2949,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 88,
          "cache_read_input_tokens": 55529,
          "cache_creation_input_tokens": 2949,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2949
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

_source line 15 · 2026-05-22T05:50:20.944Z_

<details><summary>↩ Tool result · `toolu_01EeZqnsthUDSaeeLVAQsi6T`</summary>

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
  "parentUuid": "78622efa-0c44-40bd-b4ef-7fc26c17ff90",
  "isSidechain": false,
  "promptId": "4dbb97d9-fc82-4efe-b694-2a73482dbb33",
  "type": "user",
  "uuid": "2f39f069-a090-42dc-b194-5707502c1d53",
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
  "sourceToolAssistantUUID": "78622efa-0c44-40bd-b4ef-7fc26c17ff90",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6",
  "sessionId": "8b60bbb7-357b-4091-8cce-e13fa8ccd284",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 16 · 2026-05-22T05:50:21.031Z_

````json
{
  "parentUuid": "2f39f069-a090-42dc-b194-5707502c1d53",
  "isSidechain": false,
  "attachment": {
    "type": "nested_memory",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/CLAUDE.md",
    "content": {
      "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/CLAUDE.md",
      "type": "Project",
      "content": "## 当前项目\n当前绑定项目：**schema_semantic_constrained_ie**\n\n## 按需查阅\n- 项目配置：`load_project_config(\"schema_semantic_constrained_ie\")` 或 `load_project_config(\"schema_semantic_constrained_ie\", section=\"execution\")`\n- 知识文件：`read_project_file(file=...)` 读取项目文件（ROADMAP.md/memory.md/ideas.md/report.md 等）\n- 路线图：`read_roadmap()` 读取研究方向和短期任务\n- 产出目录：`/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/`（写文件后用 `register_artifact` 注册）\n\n## 用户自定义规则（必须遵守）\n### 审稿规则\n\n- **[EMNLP 2026]** “EMNLP 2026 通过 ARR 统一审稿，Main/Findings 不分开投稿（不是两个Track），Long/Short 也走同一审稿系统，Overall Assessment的评分标准如下：5 = Consider for Award（约前2.5%），4.5 = Borderline Award，4 = Conference（可被主会议接收），3.5 = Borderline Conference，3 = Findings（可被Findings接收），2.5 = Borderline Findings，2 = Resubmit next cycle（需大幅修改，可在下一周期完成），1.5 = Resubmit after next cycle（需大幅修改，无法在下一周期完成），1 = Do not resubmit（需完全重做或与*ACL无关）”\n- **[EMNLP 2026]** EMNLP 2026 restricts long paper submissions to a strict 8-page limit for main text, with unlimited space for references. Mandatory limitations and optional ethical considerations do not count towards this page limit, provided they do not contain excessive additional content.\n\n### 写作规则\n\n- **[EMNLP 2026]** Limitations 章节只需要写一小段，覆盖 3 个点左右就可以了，不需要写得很长\n- **[EMNLP 2026]** ARR Responsible NLP Checklist在OpenReview的submission form里面（由用户手动填写），而不是在论文pdf里面\n\n> 以上规则由用户配置，优先级等同于硬约束。违反会被 Reviewer 标记。\n\n## Worker 操作规范\n\n### ssh-env-setup\n\n# 远程服务器环境搭建规范\n\n## 核心原则\n\n**先探测，再安装。** 不要假设服务器上什么都没有——很多包已经装好了。安装前必须走 discovery 流程。\n\n**镜像快速路径**：连接服务器后，先用 `detect_image` 检测是否为预置镜像。如果是已知镜像且版本匹配，跳过基础环境搭建（Phase 1-4），直接安装项目特有依赖。未检测到镜像时走传统流程。\n\n**aml-train 镜像使用 conda 环境**（不是 venv）。环境激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`。pip/python 在 `/root/miniconda3/bin/` 下。**不要假设 .venv 存在，不要创建 venv。**\n\n## Phase 1: 环境探测（用 ssh_read_only）\n\n连接到服务器后，第一步永远是收集信息，不要直接装东西：\n\n```bash\n# 1. Python 环境\nwhich python3 && python3 --version\npip3 --version 2>/dev/null || echo \"NO_PIP\"\n\n# 2. CUDA 环境\nnvidia-smi --query-gpu=name,memory.total,driver_version --format=csv,noheader 2>/dev/null || echo \"NO_GPU\"\nnvcc --version 2>/dev/null | grep \"release\" || echo \"NO_NVCC\"\n\n# 3. 包管理器\nls -d /opt/miniconda3 ~/miniconda3 ~/.conda 2>/dev/null || echo \"NO_CONDA\"\nls -d .venv venv env 2>/dev/null || echo \"NO_VENV\"\npip3 list --format=freeze 2>/dev/null | grep -iE \"torch|transformers|flash\" || echo \"NO_ML_PKGS\"\n\n# 4. PEP 668 检查\npython3 -c \"import sysconfig; print(sysconfig.get_path('stdlib'))\" 2>/dev/null\nls /usr/lib/python*/EXTERNALLY-MANAGED 2>/dev/null && echo \"PEP668_MANAGED\" || echo \"PEP668_OK\"\n```\n\n根据探测结果决定安装策略，不要猜。\n\n## Phase 2: 环境策略选择\n\n根据 Phase 1 结果选择**一个**策略，不要混用：\n\n| 探测结果 | 策略 | 说明 |\n|----------|------|------|\n| 项目目录有 `.venv/` | 用它：`source .venv/bin/activate` | 最优先 |\n| 有 conda 且有写权限 | `conda activate base` 或创建专属 env | 次优先 |\n| PEP668_MANAGED + 无 venv | 创建 venv：`python3 -m venv .venv && source .venv/bin/activate` | 不要用 --break-system-packages |\n| PEP668_OK（无保护） | 直接 `pip install`（旧系统） | 仍建议 venv |\n\n**决不混用 conda install + pip install 到同一环境。** 选了 pip 就全用 pip。\n\n## Phase 3: PyTorch 安装\n\n### CUDA 版本映射（2025-2026 常用）\n\n先从 `nvcc --version` 或 `nvidia-smi` 获取 CUDA 版本，然后匹配：\n\n| CUDA 版本 | PyTorch pip index URL | 推荐 torch 版本 |\n|-----------|----------------------|-----------------|\n| 11.8 | `https://download.pytorch.org/whl/cu118` | ≥ 2.0 |\n| 12.1 | `https://download.pytorch.org/whl/cu121` | ≥ 2.1 |\n| 12.4 | `https://download.pytorch.org/whl/cu124` | ≥ 2.4 |\n| 12.6 | `https://download.pytorch.org/whl/cu126` | ≥ 2.6 |\n\n**不要猜版本号。** 如果不确定可用版本：\n```bash\npip index versions torch --index-url https://download.pytorch.org/whl/cu121 2>/dev/null | head -3\n```\n\n安装命令：\n```bash\npip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu{CUDA_SHORT}\n```\n\n### 大包超时处理\n\nPyTorch wheel 约 500MB-2GB，默认 SSH 超时可能不够。策略：\n\n```bash\n# 方法 1: nohup + 轮询（推荐）\nnohup pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121 > /tmp/pip_install.log 2>&1 &\necho $!  # 记录 PID\n\n# 后续用 ssh_read_only 轮询\ncat /tmp/pip_install.log | tail -5\nps -p &lt;PID> -o pid= 2>/dev/null && echo \"STILL_RUNNING\" || echo \"DONE\"\n```\n\n```bash\n# 方法 2: 加大 pip 超时\npip install --timeout 300 torch ...\n```\n\n## Phase 4: 验证（必须执行）\n\n安装后必须验证，不要假设成功：\n\n```bash\npython3 -c \"\nimport torch\nprint(f'torch={torch.__version__}, cuda={torch.cuda.is_available()}, gpus={torch.cuda.device_count()}')\nif torch.cuda.is_available():\n    for i in range(torch.cuda.device_count()):\n        print(f'  GPU {i}: {torch.cuda.get_device_name(i)} ({torch.cuda.get_device_properties(i).total_mem // 1024**3}GB)')\n\"\n```\n\n验证失败的常见原因：\n- `torch.cuda.is_available()` 返回 False → CUDA 版本和 torch 不匹配，重装正确版本\n- `ImportError: libcudnn` → 缺 cuDNN，装 `nvidia-cudnn-cu1x`\n- GPU 数量不对 → 检查 `CUDA_VISIBLE_DEVICES` 环境变量\n\n## Phase 5: 项目依赖\n\n基础环境就绪后，安装项目依赖：\n\n```bash\n# 优先用 requirements.txt / pyproject.toml\npip install -r requirements.txt  # 或 pip install -e .\n\n# 常用 ML 依赖补装\npip install transformers datasets einops accelerate wandb\n```\n\nflash-attention 特殊处理（编译型包）：\n```bash\n# 需要匹配的 CUDA toolkit，编译耗时 5-15 分钟\npip install flash-attn --no-build-isolation\n# 如果编译失败，试预编译版本\npip install flash-attn --no-build-isolation 2>/dev/null || pip install flash-attn-wheels\n```\n\n## ssh_read_only vs ssh_execute 使用规则\n\n| 操作 | 用哪个工具 |\n|------|-----------|\n| 检查环境（python --version, nvidia-smi, pip list） | `ssh_read_only` |\n| 读文件内容、查日志 | `ssh_read_only` |\n| 安装包（pip install, conda install） | `ssh_execute` |\n| 创建/修改文件、启动进程 | `ssh_execute` |\n| 运行实验脚本 | `ssh_execute` |\n\n**原则：能用 read_only 就用 read_only，只有要改变服务器状态时才用 execute。**\n\n## AutoDL 专项注意事项\n\nAutoDL 实例有一系列特殊约束，5 个项目反复踩坑，必须遵守：\n\n### 磁盘\n- **根分区只有 ~30GB，严禁存大文件。** 模型、数据集、HF cache 全部放数据盘 `/root/autodl-tmp/`\n- 设置 `HF_HOME=/root/autodl-tmp/.hf_cache`，否则 HF 默认缓存到根分区导致磁盘满\n- 下载模型时用 `--local-dir /root/autodl-tmp/models/&lt;name>`，不要用默认路径\n\n### 网络\n- pip install / git clone 前必须 `source /etc/network_turbo` 启用代理加速，否则 pypi.nvidia.com 504 超时、GitHub TLS 断连\n- HF 下载设 `HF_HUB_DISABLE_XET=1`，xet_get 在 AutoDL 上返回 401\n- **SSL 证书**：`network_turbo` 的代理使用自签名证书，Python 默认 SSL 验证会失败。必须设置 `REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt` 和 `SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt`，否则 HF 下载、datasets 加载等全部报 SSL 错误\n- **大模型下载优先用 ModelScope**：AutoDL 代理下载 HuggingFace 大文件极慢（~200KB/s），改用 ModelScope 国内 CDN 速度快很多。`pip install modelscope && python -c \"from modelscope import snapshot_download; snapshot_download('Qwen/Qwen2.5-7B-Instruct', cache_dir='/root/autodl-tmp/.hf_cache')\"`\n\n### SSH\n- **AutoDL 实例重启后 SSH 端口会变。** 连接失败时不要反复重试，应提示用户去控制台查新端口并更新 `~/.ssh/config`\n\n## 经验沉淀\n\n- [2026-04-05] Worker 首次连接服务器时，先用一条 ssh_read_only 组合命令完成全部探测，减少 SSH 往返次数\n- [2026-04-05] 遇到 PEP 668 时创建 venv 而非 --break-system-packages，避免污染系统 Python\n- [2026-04-05] PyTorch 大包安装用 nohup 后台执行 + 轮询方式，避免 SSH 超时导致安装中断\n- [2026-04-05] conda 环境和 pip 不要混用——如果项目用 pip，就全部用 pip\n- [2026-04-09] sync_code 前确保本地 commit 已 push 到 remote，否则服务器 git pull 拉不到最新代码\n- [2026-04-09] venv 创建后用 `which python` 验证路径指向正确的 venv python，不要假设系统 PATH 正确\n\n## 更多 Skills（按需加载）\n\n执行相关任务前，先 Read 对应 skill 获取环境配置和最佳实践。\n\n- **paper-writing-norms** — 顶会级别论文写作风格规范——章节写法（Abstract/Intro/Related Work）、去 AI 风格、视觉密度、叙事哲学。Paper Agent 和 Worker 写论文章节时必须加载。  →  `/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md`\n- **check-training-status** — 当用户问训练进度/实验状态/查状态时使用。用专用工具查看训练状态，禁止 ssh_execute。  →  `/home/ubuntu/agent-ml-research/skills/global/check-training-status.skill.md`\n- **rebuttal** — 撰写和优化学术 rebuttal——逐条回应审稿意见，生成 response letter。当收到审稿意见、需要写 rebuttal、回复 reviewer 评论时使用。关键词：rebuttal、审稿意见、reviewer response、author response、meta-review、AC 意见。  →  `/home/ubuntu/agent-ml-research/skills/global/rebuttal.skill.md`\n- **review-reviewer-session-start** — Review Reviewer session 启动初始化——检查论文格式、编译状态、材料清单。Review Reviewer 角色 session 启动时自动使用。  →  `/home/ubuntu/agent-ml-research/skills/global/review-reviewer-session-start.skill.md`\n- **reference-audit** — 引用验证与审计——检查 bib 条目完整性、引用真实性、格式一致性。写论文、审查论文、提交前检查引用时使用。关键词：citation verification、引用检查、bib 审计、fake citation、引用格式。  →  `/home/ubuntu/agent-ml-research/skills/global/reference-audit.skill.md`\n- **accelerate-distributed** — HuggingFace Accelerate 分布式训练指南——4行代码实现多GPU/DeepSpeed/FSDP/混合精度。多GPU训练时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/accelerate-distributed.skill.md`\n- **draw-paper-figure** — 生成学术论文级 matplotlib 图表——按 narrative_intent + design_notes 设计，从 pattern 库选用技法，远程 SSH 执行输出 PDF/PNG  →  `/home/ubuntu/agent-ml-research/skills/global/draw-paper-figure.skill.md`\n- **experiment-analysis** — 实验结果分析框架——统计显著性检验、消融分析、baseline 对比、可视化建议。分析实验结果或撰写论文 Results 部分时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/experiment-analysis.skill.md`\n- **hf-hub** — HuggingFace Hub CLI (hf) — 下载/上传模型和数据集、管理缓存、搜索论文和模型。涉及 HuggingFace 资源操作时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/hf-hub.skill.md`\n- **latex-paper** — ML 顶会论文 LaTeX 写作全流程——Claim-Evidence 方法论、引用防幻觉、顶会模板速查、投稿工程链、会议转投。写论文/投稿时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md`\n- **lm-eval-harness** — lm-evaluation-harness 模型评估指南——MMLU/GSM8K/HumanEval 等 60+ 学术基准测试。评估模型质量、对比实验时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/lm-eval-harness.skill.md`\n- **ml-experiment-guide** — 跨项目 ML 实验避坑指南——从多个项目沉淀的通用踩坑经验与最佳实践。当 Worker 准备写实验代码、或排查实验问题时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/ml-experiment-guide.skill.md`\n- **paper-banana** — 用 PaperBanana 生成学术图表——概念图（架构/流程/framework）首选，探索性统计图也可。LLM 写 matplotlib 代码 + VLM Critic 闭环迭代。需要 GOOGLE_API_KEY。  →  `/home/ubuntu/agent-ml-research/skills/global/paper-banana.skill.md`\n- **paper-image-extractor** — 从论文 PDF 或 arXiv 源码包提取图表——优先 arXiv 原始图片，回退 PDF 解析。用户说\"提取图\"/\"抽图\"/\"extract figures\"时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/paper-image-extractor.skill.md`\n- **peft-lora** — PEFT/LoRA/QLoRA 参数高效微调指南——LoRA 配置选择、QLoRA 量化训练、Adapter 管理与合并。微调大模型时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/peft-lora.skill.md`\n- **research-news** — 每日论文推荐——搜索 arXiv 最新论文，按相关性/新颖性/影响力评分，生成推荐列表。Director 说\"有什么新论文\"/\"最近进展\"/\"research news\"时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/research-news.skill.md`\n- **trl-training** — TRL (Transformer Reinforcement Learning) 训练指南——SFT/DPO/GRPO/KTO 配置与最佳实践。训练或对齐语言模型时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/trl-training.skill.md`\n- **wandb-guide** — W&B 查询最佳实践——如何高效使用 fetch_wandb_metrics / compare_wandb_runs / get_best_wandb_run 分析实验结果。分析实验指标时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/wandb-guide.skill.md`\n- **Schema-Semantic Constrained IE Research Patterns** — 从10篇论文蒸馏的约束解码+结构化IE领域研究共识——实验设计、baseline选择、评估规范、方法论趋势  →  `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/skills/projects/schema_semantic_constrained_ie/distilled-research.skill.md`\n- **Schema-Semantic Constrained IE Writing Patterns** — 从8篇深度精读论文蒸馏的约束解码+结构化IE领域写作规范——叙事结构、图表编排、论证策略  →  `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/skills/projects/schema_semantic_constrained_ie/distilled-writing.skill.md`\n",
      "contentDiffersFromDisk": false
    },
    "displayPath": "projects/schema_semantic_constrained_ie/.claude/CLAUDE.md"
  },
  "type": "attachment",
  "uuid": "fe97d269-cb6c-48cf-8fd4-2c3c73a299b6",
  "timestamp": "2026-05-22T05:50:21.031Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6",
  "sessionId": "8b60bbb7-357b-4091-8cce-e13fa8ccd284",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
````

---

### Runtime record

_source line 17_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：≥2 reviewers 认为 novelty 不足以支撑 main conference；核心 'guaranteed compliance' claim 被 CF 数据和 post-hoc 比较削弱；需要 reframe 切入角度 核心假设：[\"Novelty 被拒：'constrained decod…",
  "leafUuid": "fe97d269-cb6c-48cf-8fd4-2c3c73a299b6",
  "sessionId": "8b60bbb7-357b-4091-8cce-e13fa8ccd284"
}
```

---

### Runtime record

_source line 18_

```json
{
  "type": "ai-title",
  "aiTitle": "Ontology constraint violations in LLM-based IE—worst case analysis",
  "sessionId": "8b60bbb7-357b-4091-8cce-e13fa8ccd284"
}
```

---

### Assistant

_source line 19 · 2026-05-22T05:51:03.671Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have the experiment plan. Let me identify which experiments are still in "planned" status (not yet completed). Looking at the registry and experiment_plan, I need to find experiments that are:
1. Still planned (not completed)
2. Or recently completed but need predictions under the "worst" tier

Looking at the experiment_plan, the experiments with results already noted are complete. Let me look for planned/running ones:

From the registry:
- `r16_70b_lora_scierc_eval` - PREPARING
- `eval_70b_lora_docred_200_unconstrained` - RUNNING


- `p1_llama_ee_ft` - PREPARING
- `d066_beam_sweep` - ANALYZING

So the key planned experiments that might still need predictions are P031 through P033 (error analysis, EE FT composability, and grammar), while P029 and P030 already have their results in the registry.

Looking at the registry more carefully, the 70B LoRA experiments are actually the critical ones still in progress—the training is done for both SciERC and DocRED, but the evaluation runs are either preparing or actively running. The "worst" tier criteria flags issues if the 70B LoRA eval shows a DocRED F1 drop over 2 percentage points or parse failure rates exceeding 10%, which would undermine the scaling generalization claim. I should check the experiment_plan.lock file for more specifics on what's planned.

Re-reading the request, I need to predict results for each planned experiment in the plan. Looking at which ones have actual results versus those still pending, the completed experiments have `result:` fields filled in, while the ones without results or with PREPARING/RUNNING status are what I need to forecast. Scanning through P001-P035, most have results already, but P031 (error analysis and case studies) and P032 (EE fine-tuning) don't have results yet, and those are the ones I should focus predictions on. I need to focus on the worst-case scenario predictions for the experiments still in progress or planned. Looking at what's actively running or preparing—the 70B LoRA evaluations on SciERC and DocRED, the Llama EE fine-tuning, and the beam sweep analysis—I should generate predictions for how these would perform if things went poorly, rather than optimistically.

But I'm realizing the user's request is actually asking me to examine every experiment in the plan that's marked as "planned" status and provide detailed worst-case results for each one. The challenge is that the experiment plan doesn't have explicit status fields, so I need to identify which experiments are still planned by looking for ones without result entries, then cross-reference against the registry to see what's actually been completed versus what's still pending. Looking at which experiments are still in progress versus completed, I see the 70B LoRA evaluations are the critical ones—particularly the SciERC and DocRED runs that are either preparing or actively running. But I think the user actually wants me to project what the entire experimental plan would look like if everything fell into the "worst" tier scenario, not just the pending ones.

Let me check the lock file to clarify which experiments are truly "planned" versus already executed.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fe97d269-cb6c-48cf-8fd4-2c3c73a299b6",
  "isSidechain": false,
  "requestId": "req_011CbH5ppGC1MrtsPBU3Nm4X",
  "type": "assistant",
  "uuid": "c4d58909-76fe-4264-abff-54368ab29280",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6",
  "sessionId": "8b60bbb7-357b-4091-8cce-e13fa8ccd284",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U9cZtdUDRvnEDCeEbXR5bp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10606,
      "cache_read_input_tokens": 58478,
      "output_tokens": 2036,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10606,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2036,
          "cache_read_input_tokens": 58478,
          "cache_creation_input_tokens": 10606,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10606
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

_source line 20 · 2026-05-22T05:51:03.702Z_

<details open><summary>🔧 Tool call — Read · `toolu_013v7R4ExnMAsjXwnD5GEPZP`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/experiment_plan.lock"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c4d58909-76fe-4264-abff-54368ab29280",
  "isSidechain": false,
  "requestId": "req_011CbH5ppGC1MrtsPBU3Nm4X",
  "type": "assistant",
  "uuid": "5b401e30-851b-4fbf-ba66-c2a569c9b4cd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6",
  "sessionId": "8b60bbb7-357b-4091-8cce-e13fa8ccd284",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U9cZtdUDRvnEDCeEbXR5bp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10606,
      "cache_read_input_tokens": 58478,
      "output_tokens": 2036,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10606,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2036,
          "cache_read_input_tokens": 58478,
          "cache_creation_input_tokens": 10606,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10606
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

_source line 21 · 2026-05-22T05:51:03.713Z_

<details><summary>↩ Tool result · `toolu_013v7R4ExnMAsjXwnD5GEPZP`</summary>

```text
&lt;system-reminder>Warning: the file exists but is shorter than the provided offset (1). The file has 1 lines.&lt;/system-reminder>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5b401e30-851b-4fbf-ba66-c2a569c9b4cd",
  "isSidechain": false,
  "promptId": "4dbb97d9-fc82-4efe-b694-2a73482dbb33",
  "type": "user",
  "uuid": "d9f7b9c9-c598-4b50-9d6b-58a6f71cc0fa",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/experiment_plan.lock",
      "content": "",
      "numLines": 1,
      "startLine": 1,
      "totalLines": 1
    }
  },
  "sourceToolAssistantUUID": "5b401e30-851b-4fbf-ba66-c2a569c9b4cd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6",
  "sessionId": "8b60bbb7-357b-4091-8cce-e13fa8ccd284",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 22 · 2026-05-22T05:57:30.252Z_

<details><summary>Logged reasoning block</summary>

```text
The lock file is essentially empty. Let me look at the experiment plan more carefully. The experiments without `result:` fields are the "planned" ones. Let me also check if there's a dream/scenario file or a tier definition file that has more details.

Let me identify all experiments in the plan that don't have a `result:` field:
- P021: WikiEvents Qwen3-8B unconstrained
- P023: WikiEvents Llama-3.1-8B unconstrained
- P025: WikiEvents Mistral-7B unconstrained


- P027: WikiEvents Mistral grammar_only v3
- P028: WikiEvents EE post-hoc filtering
- P029: 70B SciERC unconstrained + constrained
- P030: 70B DocRED unconstrained + constrained
- P031: Error analysis / case study
- P032: EE FT composability
- P033: Grammar-only cross-model validation
- P034: Bootstrap CI for EE metrics
- P035: Latency overhead measurement

Now I need to cross-check against the registry to see which ones actually have results already recorded.

Most of these are already done—P021 through P032 all have corresponding registry entries except for P031, P033, and P034. P035 has partial results with the latency overhead and fine-tuned SciERC measurements.

There are also many experiments in the registry that aren't part of the formal plan—LoRA variants, beam search sweeps, TCR experiments, and various seed variance tests. But looking back at what the user actually asked for, I think they want me to analyze every experiment in the plan itself, treating even completed ones as if I need to describe the worst-case interpretation of those results—how a critical reviewer would view them.

For the experiments still marked as planned without results yet, I should predict what the worst-tier outcomes would look like. The ones without result fields are P021, P023, P025, P027 through P035. For those, I'll construct pessimistic predictions. For the ones that already have results, I'll reframe those results in the most unfavorable light possible to build out the complete worst-case narrative. I'm realizing the "worst" tier scenario isn't just about predicting experimental outcomes—it's about simulating how a hostile reviewer would interpret all the results. The core dismissals would be that novelty gets rejected, counterfactuals are seen as fundamentally flawed, post-hoc analysis fails in zero-shot settings, entity extraction gets completely dismissed, the 70B LoRA evaluations fail, the 8% F1 on zero-shot is treated as trivial, and existing methods like GCD and BoostCD are claimed to already subsume the contributions. So I need to generate the imagined_experiments array by predicting worst-case outcomes for all planned experiments without results, covering the full range from P021-P035 plus any critical pending runs from the registry. Looking at the registry entries that are already marked DONE, I can use their actual results rather than predicting worst-case outcomes. For the experiments still pending—particularly the 70B LoRA evaluations—I'll generate conservative predictions based on worst-case assumptions, then compile everything into a comprehensive YAML output with results for each planned experiment. For the pending 70B LoRA experiments, I'll use worst-case predictions within the defined ranges. Now I'm going through the planned experiments systematically—starting with the WikiEvents experiments already in the registry, I'll pull their actual results and reframe them through a worst-case lens, then fill in predictions for the ones still pending evaluation. Finishing up the DocRED results, then I see several experiments already tracked in the registry while a few others like the grammar-only cross-model evaluation and bootstrap confidence intervals are still pending, along with the latency overhead studies. There are also some 70B LoRA evaluations on SciERC that haven't been completed yet.

Looking at the worst-case tier definitions for these models, I'm checking the expected performance degradation ranges—DocRED and SciERC LoRA variants could see detection rates between 0.5-5% and R-F1 drops of 1-4 percentage points depending on the dataset. Looking at the 70B LoRA results, the unconstrained SciERC eval is done but I don't have the metrics yet, while DocRED unconstrained is still running. For the constrained predictions under worst-case tier, I'm estimating the SciERC model would show DR around 0.5-3% with R-F1 dropping by that same range compared to unconstrained, which if baseline is similar to the 8B LoRA results around 43-44%, would put constrained performance in the 40-43% range.

Now I'm realizing I should construct the full YAML configuration more systematically. Looking through the registry, there are many more experiments beyond the original plan—d062 through d068 series covering full fine-tuning, voting strategies, beam search variants, and seed variance studies, plus r14, r16, and various w-series ablations—so I need to make sure I'm capturing everything comprehensively.

But the user specifically asked about planned experiments, which means I should focus on P021-P035. However, re-reading the worst-tier definition, it references specific findings across the entire paper—like post-hoc results outperforming constrained decoding in zero-shot settings, the 8% F1 gap being dismissed as toy evaluation, and issues with 70B LoRA evaluation. This suggests the worst tier is actually a full paper simulation, not just isolated experiments.

So I think what I need to do is generate predicted results for all experiments in the plan (P001-P035), using actual data where available and filling in predictions for pending ones, to construct the complete worst-tier picture.

Looking at the plan structure, P001-P020 all have result fields already, while P021-P035 are the ones without results yet. But some of these have registry entries with actual results. For those, I should interpret the actual results through the worst-tier lens. For the 70B LoRA evaluations still in progress, I'll need to predict worst-case outcomes.

Let me generate the full output now, checking one more time what the 70B LoRA SciERC unconstrained eval actually produced, since it's marked as done but appears to have empty results.

Now I'll construct the worst-tier prediction YAML carefully. For planned experiments that already have registry data, I'll use those results. For pending ones, I'll predict worst-case numbers. And for all of them, I'll add result_rationale explaining how these results support the worst-tier narrative. I need to clarify the distinction between the zero-shot 70B experiments in the plan versus the separate LoRA fine-tuning experiments. Looking at the performance thresholds for the LoRA variants, I'm seeing some concerning metrics—the DocRED LoRA is showing larger drops in relation F1 and higher data requirements than the SciERC version.

Now I'm checking which experiments actually have results versus which are still pending. Going through P021 to P035, I can see that P022, P024, and P026 already have result fields populated, meaning those are done. That leaves 12 experiments still planned that need worst-tier predictions generated.

I should also include the 70B LoRA experiments since they're specifically called out in the worst-tier definition, even though they're not in the main plan. For the output structure, I'll organize this as a YAML with the tier designation, narrative guidance, and then imagined experiments that each include the plan ID, description, expected metrics, rationale, and any relevant tables or figures.

Let me verify the status of the existing experiments first—P029 and P030 (the 70B zero-shot runs) are already complete with strong results, so those should use actual data rather than being treated as worst-case scenarios. The real concern for the worst tier is around the 70B LoRA experiments that aren't yet in the plan.

Now I'll work through each experiment systematically, starting with P021 on WikiEvents with Qwen unconstrained. Looking at the Mistral results with grammar constraints, I see the RoV metric stays around 64% even with the grammar-only approach, which aligns with expectations since grammar alone doesn't address the dominant violation type. For the post-hoc filtering experiment, I'm examining how aggressively the different models discard arguments—Qwen, Llama, and Mistral all show extreme filtering rates above 99%, suggesting the post-hoc constraints are overly restrictive.

Moving to the 70B model experiments, the SciERC results look promising with zero detection rate on constrained decoding and reasonable F1 scores, though a reviewer might push back on the absolute performance level. For DocRED, I'm seeing similar patterns with the constrained version achieving zero detection rate while maintaining comparable relation F1 performance.

The error analysis is qualitative, showing that most remaining violations stem from fundamental model limitations rather than issues that constrained decoding could address. Now looking at the composability experiments across different model families—Qwen and Llama both show trigger detection in the 26-32% range with argument F1 around 8-9%, and the constrained versions are zeroing out some metrics while maintaining or slightly improving others.

The key finding is that constrained decoding actually degrades trigger extraction performance (dropping 5 percentage points for Qwen) while providing minimal argument F1 gains, which suggests the approach is trading off extraction quality for constraint satisfaction. The grammar-only variant hasn't been tested yet, but I expect it'll follow the pattern from Mistral where it eliminates violations entirely but leaves the core extraction metrics unchanged. The bootstrap confidence interval work for event extraction is still pending.

Looking at latency, the registry shows about 13% overhead on SciERC zero-shot and 10% on the fine-tuned version, which the reviewer acknowledged but didn't flag as problematic. Now shifting to the 70B LoRA experiments—based on the 8B results where Qwen achieved 43.86% and Llama hit 45.45%, I'm estimating the larger model should land somewhere in that 42-46% range for relation F1, with a baseline DR improvement of 1-3 points.

For the constrained variant on SciERC, I'm expecting the worst case to show about 2% DR with a 2-point F1 drop down to around 42%, plus parse failures exceeding 10%. The DocRED experiments follow a similar pattern—8B models hit 40-43% F1, so 70B should be comparable, but the constrained version could see 3% DR and a 3-point F1 drop with similar parsing issues.

Now I'm assembling the full YAML output...

I need to include all the planned experiments from the original plan plus these 70B LoRA evaluations. For the reviewer simulation, I'm thinking worst-case scenario: 2-3 hostile reviewers, overall assessment around 2.5-3.5, with novelty and significance both in the 2-3 range but soundness holding at 3-3.5. The key reframe is shifting from "constrained decoding method paper" to "empirical study paper with a tool."

Let me structure this systematically and generate the comprehensive YAML output.

Now I'm working through the worst-case metric predictions for the pending experiments. For the 70B LoRA results, I'm looking at the existing LoRA data from smaller models to calibrate my estimates—the 8B variants show pretty modest effects, so I'm predicting similarly conservative numbers for the 70B version.

The quantized 70B model might actually perform worse due to how AWQ-INT4 artifacts interact with constrained decoding, potentially pushing violation rates higher and introducing more parse failures around 12-15%. I'm settling on mid-range predictions: SciERC at 1.5% DR with a 1.5pp R-F1 drop, and DocRED at 2.5% DR with a 2pp drop.

Now I need to check what the unconstrained 70B LoRA eval already shows in the registry so I can properly anchor these worst-case estimates. _70b_lora_scierc_unconstrained` is DONE but has empty metrics. Let me see if there's data elsewhere.

I don't have access to the actual numbers. Under worst tier, let me predict:

70B LoRA SciERC unconstrained:
- Since 8B LoRA Qwen got R-F1=43.86 and 8B LoRA Llama got R-F1=45.45
- 70B should be at least as good or better: maybe R-F1≈47-50%
- DR baseline: maybe 0.5-2%
- ET/RV: ~0%

70B LoRA SciERC constrained (worst tier):
- DR: 1.5% (fails the "near-complete" claim)
- R-F1: 45-48% (drops 2pp from unconstrained ~48%)
- Parse failures: 12%
- CF: 2-5%

70B LoRA DocRED unconstrained:
- R-F1: maybe 45-48%
- DR: 0.5-2%

70B LoRA DocRED constrained (worst tier):
- DR: 2.5%
- R-F1: 43-46% (drops 2pp)
- Parse failures: 15%

I'm overthinking the specific numbers here. Let me just generate the YAML with coherent worst-case estimates. I need to include all planned experiments from P021-P035, the critical 70B LoRA eval experiments, and detailed metrics with rationale for each.

Generating YAML output... Writing experiment specifications... 有实际数据。RoV=74.9% 是 EE 中压倒性违规类型，远超 RE 的 RV（1-30%）。
      Entity-F1=0% 和 Arg-F1≈0% 是 ZS EE 的固有困难——模型甚至无法输出 schema-valid 的 entity 格式。
      但在 worst 档，reviewer 会直接抓住这一点：baseline 几乎不工作，任何在此基础上的"改进"都是 
      format compliance 恢复，不是语义能力提升。"Entity F1 from 0 to 14% is just format compliance, 
      not extraction improvement" 正是来自于 unconstrained baseline 的 0%。现在看三个模型的无约束基线表现，Qwen3-8B 的 Parse% 最高（88.6%），但 RoV 仍然达到 74.9%；Llama-3.1-8B 虽然 Parse% 更好（91.9%），却有最严重的 RoV（88.8%）；Mistral-7B 的 Parse% 最低（78.9%），三个模型的 Entity-F1 和 Arg-F1 都基本为 0，这进一步证实了格式合规性的根本问题。 Looking at the actual results for Llama on WikiEvents, the RoV percentage of 88.8% is notably the highest among the three models, indicating that most argument roles fall outside the event type definitions. The trigger F1 score of 5.7% trails behind Qwen's 11.8%, suggesting Llama performs worse on this extraction task overall. The zero argument F1 score reinforces the reviewer's concern about the meaningfulness of the evaluation at this difficulty level. Looking at the Mistral baseline results, the parse rate of 78.9% is the lowest among models tested, while the event extraction rate of 37.3% is notably high—indicating that over a third of predicted event types don't exist in the ontology. This fundamental mismatch between model outputs and task requirements becomes a critical issue when reviewers assess whether the task setup itself is viable.

The trigger F1 score of 2.4% is essentially negligible, which reinforces concerns about whether this is a meaningful evaluation. Mistral clearly underperforms on event extraction compared to the other models tested, raising legitimate questions about model selection for this particular task. Now I'm looking at the grammar-only ablation experiment on WikiEvents with Mistral to demonstrate why the semantic layer is essential. Generating comparison table...

The grammar-only ablation shows what reviewers consider an obvious result—that semantic constraints matter—but the real issue is how the semantic layer introduces a spike in constraint violations, jumping from 1.1% to 14.9%. This actually strengthens the argument that constraint violations are a fundamental problem with the approach. Now looking at the post-hoc filtering baseline for WikiEvents across multiple models...

the data shows these models need to discard 99.6-100% of arguments to achieve zero violations, which is drastically different from the 16-48% discard rates needed in the relation extraction task. Generating comparison table...

A reviewer pushes back on the narrative, suggesting the zero-shot EE results just expose fundamental issues with the approach rather than validating the constrained decoding solution. Now I'm looking at the 70B model scaling experiment on SciERC, comparing unconstrained versus constrained performance metrics to see how the larger model generalizes. Generating comparison table... earing." The core tension here is that while constrained decoding achieves zero violation rate on the 70B model, the baseline violation rate is already so low that it undermines the argument for needing the method in the first place. Now I'm setting up the 70B DocRED experiment to test whether this scaling effect holds across different datasets, with expected results showing near-zero violation rates for both constrained and unconstrained approaches.

Looking at the actual results, we have one parse failure, and the data confirms that the 70B model achieves the best zero-shot violation rate across all configurations at 0%, significantly outperforming the 8B variants. However, the constrained violation rate of 7.01% is still substantial—roughly one in fourteen entities showing inconsistent typing across the 96 relations in DocRED. This pattern of systematic inconsistency appears across the 8B results too, suggesting it's a fundamental limitation rather than an isolated issue. The unconstrained violation rate of 15% on the 70B model also raises questions about how the scaling compares to the smaller models. Looking at the cross-scale results, the CF percentages don't decrease with model size—70B actually shows 7.01% compared to Qwen-8B's 2.57%—which strengthens the argument that this is a fundamental issue with the method rather than a model-specific artifact. Now I'm planning the error analysis phase to examine 10-20 representative cases, focusing on identifying the root causes behind the remaining accuracy issues and categorizing the CF failures by whether they stem from entity ambiguity, model confusion, or ontology gaps.

The qualitative analysis reveals that accuracy residuals primarily come from models confusing semantically similar entity types like SID versus SEN, which constrained decoding can't resolve since it's fundamentally a semantic understanding problem. For the CF cases, about 45% trace back to fuzzy semantic boundaries in the ontology system itself, 40% stem from the model assigning different types to the same entity depending on relational context, and the remaining 15% point to inherent design flaws in the ontology.

Now I'm anticipating how reviewers will push back—they'll argue that nearly half the CF errors are actually dataset problems and another 40% are model capability issues, neither of which my method addresses. The error analysis becomes a liability here because each case study example demonstrates that constrained decoding only enforces local constraints and can't handle cross-relation consistency or improve the model's semantic reasoning. Reviewers will likely use these case studies to argue that the method's limitations are more revealing than its actual contributions.

For the composability test on WikiEvents, I'm checking how well the fine-tuned models work with OntoCoDec across different configurations—comparing unconstrained versus constrained decoding for both Qwen and Llama, tracking trigger F1, argument F1, and other metrics.

The actual results show a significant performance drop when applying constrained decoding: Qwen's trigger F1 falls from 32.08% to 26.72%, which reviewers have flagged as the classic constraint-quality tradeoff that's already been documented in prior work. The argument F1 scores are also affected by the constraint enforcement. 现在我看到了具体的性能数据对比——Qwen 在受约束解码下触发器F1从32.08下降到26.72，而Llama的论证F1实际上从9.98下降到8.91，这正是审稿人认为不可接受的质量退化。审稿人的核心批评是这5个百分点的下降幅度太大，而论证F1的改善微乎其微，这使得整个可组合性的改进在最差档被完全否定了。

这个观点直接攻击了我们方法的新颖性——如果约束解码只是XGrammar的直接应用加上一个查找表和logit掩蔽，那么语义层的贡献就很有限。接下来我需要看跨模型的纯语法消融实验，这会验证语法约束在Qwen和Llama上的独立效果。

根据Mistral的模式推断，纯语法应该会完全消除EV（因为语法无法处理语义），保持RoV在70-80%范围（因为语法无法约束事件类型条件下的角色），而AC会上升到10-14%（潜在违规浮现）。最坏的情况是审稿人认为这个实验是冗余的——Mistral的消融已经展示了这一点，结论也很显而易见。

现在我在整理三个模型的语法消融对比表，展示Mistral的实际结果和Qwen、Llama的预测结果，都遵循相同的模式：EV降至0%，RoV保持在64-77%，AC在9.5-14.2%之间波动。这些一致的模式在方法论上提供了完整的消融证据，但我意识到最严苛的审稿人可能会质疑这个实验的必要性。

接下来我需要为EE指标建立自助法置信区间，计算Qwen和Llama在触发器和实体F1上的显著性检验，预期结果显示Qwen的触发器F1变化不显著（p=0.18），但实体F1有显著提升（p=0.001），Llama也呈现类似的模式。

现在补充Mistral模型的结果，同样显示实体F1的显著改善（p=0.001）而触发器F1不显著（p=0.31），这表明改善主要来自格式合规性恢复——语法约束强制输出有效JSON，使解析器能够识别实体，但对触发器识别的影响有限。

论文审稿人最坏情况下会指出，唯一统计显著的改善是实体F1，而这完全归因于格式修复而非真正的信息抽取能力提升。

现在看着引导程序置信区间的结果，Entity-F1在所有三个模型上都显示出显著改善（Qwen +14.09%, Llama +17.63%, Mistral +11.71%），但Trigger-F1和Argument-F1的提升都不显著，这强化了那个批评——改善主要来自格式合规性而非实际的抽取性能。

接下来我需要检查延迟开销的测量数据，看约束解码在不同场景下的性能成本。

虽然13%的开销在绝对值上可以接受，但审阅者可能会将其与交叉字段违规问题结合考虑，认为为了一个引入10-21%违规的方法付出13%的延迟代价不划算。我正在整理延迟开销汇总表来展示各种设置下的具体数据。 Looking at the 70B LoRA experiments that weren't in the original plan, I'm setting up the SciERC unconstrained evaluation with Qwen3-70B using LoRA fine-tuning, expecting around 47% relation F1 and 70% entity F1 with minimal constraint violations and parse failures. The unconstrained baseline itself isn't the issue—it's really about establishing the comparison point for the constrained evaluation. For the constrained version with the 70B model, I'm expecting the relation F1 to drop slightly to around 45.5%, entity F1 around 70.3%, with a decoding rate of about 1.8% and parse failures at 11%.

Looking at the performance breakdown, the 1.7 percentage point drop in relation F1 comes from the AWQ-INT4 quantization shifting the logit distribution, which makes the semantic mask's fallback mechanism trigger more often, leaving some residual decoding rate even with constrained decoding—unlike the 8B LoRA version which achieved nearly zero. Generating performance metrics table...

The 70B LoRA results on DocRED without constraints show the model performing better, with R-F1 at 45.8 and E-F1 at 84.2, though parse failures remain minimal. This contrasts sharply with the constrained version's degradation, suggesting the constraints themselves are problematic for larger quantized models rather than the underlying approach. Generating metrics table... 在最坏情况下，70B 量化模型加上约束解码在 DocRED 上的表现甚至不如 8B 全精度模型，解析失败率高达 13%，这反映了长文档、量化和约束解码三重因素叠加导致的严重性能退化。现在我在查看具体的对比数据，包括 8B 和 70B 模型在各项指标上的差异。 The 13% parse failure rate means roughly 130 documents couldn't be evaluated, which combined with the increased domain-range violations and R-F1 drop creates a compelling case that the method doesn't scale to practical deployment with quantized large models. But I'm second-guessing my prediction for the 70B LoRA SciERC constrained case—if constrained decoding is supposed to reduce violations, why would I predict 1.8% when unconstrained is only 1.2%? That suggests quantization noise is creating unexpected interactions with the masking mechanism. The quantization effects are compounding the problem—Q quantization shifts the logit distributions in ways that break the constraint mask's effectiveness, forcing more frequent fallbacks to grammar-only generation, which leaves residual DR violations that the semantic layer can't correct. Looking at the actual 8B LoRA results, the constrained approach achieved near-perfect DR reduction (92-100%), so having constrained DR exceed unconstrained for 70B would be a catastrophic failure that contradicts the pattern, suggesting I should recalibrate the unconstrained baseline to 0.8-1.5% instead. I'm realizing the latent violation pattern from Qwen could apply here too—the grammar constraint might expose hidden DR violations in the LoRA model. But with 70B's already minimal baseline violations, the real problem is probably the interaction between quantization and the constraint mask causing more type-incorrect entity generation. Let me settle on a concrete worst-case scenario for 70B LoRA across both datasets. I'm verifying my analysis across the different model configurations—the pattern holds where grammar-only constraints surface latent violations in base models, but LoRA fine-tuning eliminates those issues by producing correct relation names naturally. For the 70B quantized model, constrained decoding might be forcing slightly off-vocabulary relation names that the model wouldn't naturally generate, which could explain the DR increase.

Actually, I'm overcomplicating this. The simpler explanation works: quantization degrades logit quality, the constraint mask interacts poorly with those degraded logits, and the result is higher residual DR than expected along with R-F1 degradation. That's plausible enough without needing to trace every mechanism.

Let me lock in my predictions and make sure the overall narrative is consistent across all three experiment tiers.

Now I need to finalize the YAML and verify the experiment plan—checking which of P021-P026 have results and registry IDs, since some are missing those details. Looking at the remaining experiments, I see a mix of completed work with actual data and predictions. P027 through P032 have concrete results or are derived from them, while P033 and P034 are still predictions. P035 has actual latency measurements, and then there are several LoRA evaluation experiments that are still pending.

That brings me to 16 total experiments to document. I need to clarify whether the user wants me to include only the truly pending ones or all planned experiments regardless of status. Re-reading their request, they're asking for detailed data on every planned experiment in the plan—so I'll pull actual numbers from the registry where available and generate predictions for the rest.

For the reviewer simulation, I'm thinking about how a critical reviewer would assess this work. The overall score would likely land around 2.5-3.5, aiming for 3.0 which represents solid findings, with particular attention to novelty and methodological rigor.

Writing the YAML output now...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d9f7b9c9-c598-4b50-9d6b-58a6f71cc0fa",
  "isSidechain": false,
  "requestId": "req_011CbH5sxvftoY24R8P1RWhX",
  "type": "assistant",
  "uuid": "81420f12-8c8a-4c7c-9f9b-880719b2ef69",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6",
  "sessionId": "8b60bbb7-357b-4091-8cce-e13fa8ccd284",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015xxgdz4USXc71RJohcNQbR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2075,
      "cache_read_input_tokens": 69084,
      "output_tokens": 22225,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2075,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 22225,
          "cache_read_input_tokens": 69084,
          "cache_creation_input_tokens": 2075,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2075
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

_source line 23 · 2026-05-22T05:57:30.255Z_

Now I have all the data needed. Let me cross-reference the registry to identify which planned experiments have actual data vs need predictions.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "81420f12-8c8a-4c7c-9f9b-880719b2ef69",
  "isSidechain": false,
  "requestId": "req_011CbH5sxvftoY24R8P1RWhX",
  "type": "assistant",
  "uuid": "1658be12-d0c1-4735-aaf9-7b77bf58a4ea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6",
  "sessionId": "8b60bbb7-357b-4091-8cce-e13fa8ccd284",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015xxgdz4USXc71RJohcNQbR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2075,
      "cache_read_input_tokens": 69084,
      "output_tokens": 22225,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2075,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 22225,
          "cache_read_input_tokens": 69084,
          "cache_creation_input_tokens": 2075,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2075
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

_source line 24 · 2026-05-22T05:57:30.292Z_

<details open><summary>🔧 Tool call — Agent · `toolu_015StsWzJeSh5yZe142y2pzS`</summary>

```json
{
  "subagent_type": "Explore",
  "description": "Find 70B LoRA eval results",
  "prompt": "In /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/, search for any files containing results from 70B LoRA evaluation experiments. Look for:\n1. Files matching *70b*lora*eval* or *r16*eval*\n2. Any JSONL files with 70b LoRA results\n3. Check the artifacts/ directory for any 70B LoRA outputs\n\nI need to find if there are actual metric results for:\n- eval_70b_lora_scierc_unconstrained\n- r16_70b_lora_scierc_eval\n- eval_70b_lora_docred_200_unconstrained\n\nSearch breadth: medium"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1658be12-d0c1-4735-aaf9-7b77bf58a4ea",
  "isSidechain": false,
  "requestId": "req_011CbH5sxvftoY24R8P1RWhX",
  "type": "assistant",
  "uuid": "45287a44-fe50-48e3-a424-4f2841addb8a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6",
  "sessionId": "8b60bbb7-357b-4091-8cce-e13fa8ccd284",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015xxgdz4USXc71RJohcNQbR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2075,
      "cache_read_input_tokens": 69084,
      "output_tokens": 22225,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2075,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 22225,
          "cache_read_input_tokens": 69084,
          "cache_creation_input_tokens": 2075,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2075
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

_source line 25_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：≥2 reviewers 认为 novelty 不足以支撑 main conference；核心 'guaranteed compliance' claim 被 CF 数据和 post-hoc 比较削弱；需要 reframe 切入角度 核心假设：[\"Novelty 被拒：'constrained decod…",
  "leafUuid": "45287a44-fe50-48e3-a424-4f2841addb8a",
  "sessionId": "8b60bbb7-357b-4091-8cce-e13fa8ccd284"
}
```

---

### Runtime record

_source line 26_

```json
{
  "type": "ai-title",
  "aiTitle": "Ontology constraint violations in LLM-based IE—worst case analysis",
  "sessionId": "8b60bbb7-357b-4091-8cce-e13fa8ccd284"
}
```

---

### Tool result

_source line 27 · 2026-05-22T05:58:30.867Z_

<details><summary>↩ Tool result · `toolu_015StsWzJeSh5yZe142y2pzS`</summary>

```text
Excellent! I've found detailed information about the 70B LoRA evaluation experiments. Let me compile my findings:

## Search Results Summary

I've found the 70B LoRA evaluation experiment results in your project directory. Here's what exists:

### Files Found:

**1. Training Checkpoints (Completed):**
- `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/checkpoints/r16_70b_lora_scierc_DONE_20260522T021045.json`
  - Status: DONE
  - Metrics: eval_loss=0.0611, token_acc=97.78%, steps_completed=663
  
- `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/checkpoints/r16_70b_lora_docred_DONE_20260522T020801.json`
  - Status: DONE (but marked as "failed" with "process dead, no active cron monitor")
  - Note: Training completed, but metrics not fully captured

**2. Evaluation Experiments (Results Exist):**

#### eval_70b_lora_scierc_unconstrained (COMPLETED)
- Checkpoint: `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/checkpoints/eval_70b_lora_scierc_unconstrained_DONE_20260522T052450.json`
- **Metrics Found** (from worker_eval_70b_lora_scierc_unconstrained_violations_20260522T052510_result.json):
  - Entity P: 62.74%, R: 67.12%, **F1: 64.86**
  - Relation P: 41.61%, R: 48.36%, **R-F1: 44.73**
  - Violations: ET=0%, RV=0%, DR=1.50%, CF=0%
  - Parse success: 100% (551 samples)

#### r16_70b_lora_scierc (Training + parent for eval)
- Completed with R16 LoRA training (checkpoint-663)
- Used for the eval_70b_lora_scierc_unconstrained experiments

#### eval_70b_lora_docred_200_unconstrained (IN PROGRESS)
- Checkpoint: `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/checkpoints/eval_70b_lora_docred_200_unconstrained_RUNNING_20260522T040649.json`
- Status: Still running (as of 2026-05-22 04:06 UTC)
- Note: Expected to complete in ~12 hours from the worker log

#### r16_70b_lora_docred (Training parent)
- Training completed with checkpoint-1146
- Status: Marked "failed" due to process death, but training steps completed (1146/1146)

**3. Related Evaluation Results:**

#### r16_70b_scierc_zs_s1 (Zero-shot baseline comparison)
- File: `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/r16_70b_scierc_zs_s1/report/70b_scierc_zs_results.json`
- **Metrics**:
  - Unconstrained: E-F1=35.21, R-F1=11.15
  - S1 Constrained: E-F1=35.19, R-F1=11.24
  - DR reduction: 6.41% → 0%

#### 70B DocRED Unconstrained Analysis
- File: `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/70b_docred_unconstrained_analysis.md`
- **Metrics**: Entity F1=69.03%, Relation F1=13.03%, DR violation=15.0%

### Summary of Findings:

**Files with actual metric results:**
1. `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/logs/workers/worker_eval_70b_lora_scierc_unconstrained_violations_20260522T052510_result.json` - **HAS R-F1=44.73 for SciERC**
2. `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/r16_70b_scierc_zs_s1/report/70b_scierc_zs_results.json` - **HAS metrics for zero-shot 70B baseline**
3. `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/logs/workers/worker_eval_70b_lora_docred_inference_20260522T023202_result.json` - Status update (still running/recent)

**Status of requested experiments:**
- ✅ `eval_70b_lora_scierc_unconstrained` - **COMPLETED with results** (R-F1=44.73)
- ⏳ `r16_70b_lora_scierc_eval` - Training complete, unconstrained eval complete, constrained eval status unclear
- ⏳ `eval_70b_lora_docred_200_unconstrained` - Still running as of last checkpoint

**Important Note:** The constrained (S1) evaluation results for the LoRA 70B models appear to still be in progress. The unconstrained baseline for SciERC LoRA shows strong performance (R-F1=44.73) compared to the zero-shot baseline (R-F1=11.15).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "45287a44-fe50-48e3-a424-4f2841addb8a",
  "isSidechain": false,
  "promptId": "4dbb97d9-fc82-4efe-b694-2a73482dbb33",
  "type": "user",
  "uuid": "534c990a-a8e6-4c78-bb27-59382d1e0473",
  "toolUseResult": {
    "status": "completed",
    "prompt": "In /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/, search for any files containing results from 70B LoRA evaluation experiments. Look for:\n1. Files matching *70b*lora*eval* or *r16*eval*\n2. Any JSONL files with 70b LoRA results\n3. Check the artifacts/ directory for any 70B LoRA outputs\n\nI need to find if there are actual metric results for:\n- eval_70b_lora_scierc_unconstrained\n- r16_70b_lora_scierc_eval\n- eval_70b_lora_docred_200_unconstrained\n\nSearch breadth: medium",
    "agentId": "a5771b2a84fa8e3d0",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Excellent! I've found detailed information about the 70B LoRA evaluation experiments. Let me compile my findings:\n\n## Search Results Summary\n\nI've found the 70B LoRA evaluation experiment results in your project directory. Here's what exists:\n\n### Files Found:\n\n**1. Training Checkpoints (Completed):**\n- `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/checkpoints/r16_70b_lora_scierc_DONE_20260522T021045.json`\n  - Status: DONE\n  - Metrics: eval_loss=0.0611, token_acc=97.78%, steps_completed=663\n  \n- `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/checkpoints/r16_70b_lora_docred_DONE_20260522T020801.json`\n  - Status: DONE (but marked as \"failed\" with \"process dead, no active cron monitor\")\n  - Note: Training completed, but metrics not fully captured\n\n**2. Evaluation Experiments (Results Exist):**\n\n#### eval_70b_lora_scierc_unconstrained (COMPLETED)\n- Checkpoint: `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/checkpoints/eval_70b_lora_scierc_unconstrained_DONE_20260522T052450.json`\n- **Metrics Found** (from worker_eval_70b_lora_scierc_unconstrained_violations_20260522T052510_result.json):\n  - Entity P: 62.74%, R: 67.12%, **F1: 64.86**\n  - Relation P: 41.61%, R: 48.36%, **R-F1: 44.73**\n  - Violations: ET=0%, RV=0%, DR=1.50%, CF=0%\n  - Parse success: 100% (551 samples)\n\n#### r16_70b_lora_scierc (Training + parent for eval)\n- Completed with R16 LoRA training (checkpoint-663)\n- Used for the eval_70b_lora_scierc_unconstrained experiments\n\n#### eval_70b_lora_docred_200_unconstrained (IN PROGRESS)\n- Checkpoint: `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/checkpoints/eval_70b_lora_docred_200_unconstrained_RUNNING_20260522T040649.json`\n- Status: Still running (as of 2026-05-22 04:06 UTC)\n- Note: Expected to complete in ~12 hours from the worker log\n\n#### r16_70b_lora_docred (Training parent)\n- Training completed with checkpoint-1146\n- Status: Marked \"failed\" due to process death, but training steps completed (1146/1146)\n\n**3. Related Evaluation Results:**\n\n#### r16_70b_scierc_zs_s1 (Zero-shot baseline comparison)\n- File: `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/r16_70b_scierc_zs_s1/report/70b_scierc_zs_results.json`\n- **Metrics**:\n  - Unconstrained: E-F1=35.21, R-F1=11.15\n  - S1 Constrained: E-F1=35.19, R-F1=11.24\n  - DR reduction: 6.41% → 0%\n\n#### 70B DocRED Unconstrained Analysis\n- File: `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/70b_docred_unconstrained_analysis.md`\n- **Metrics**: Entity F1=69.03%, Relation F1=13.03%, DR violation=15.0%\n\n### Summary of Findings:\n\n**Files with actual metric results:**\n1. `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/logs/workers/worker_eval_70b_lora_scierc_unconstrained_violations_20260522T052510_result.json` - **HAS R-F1=44.73 for SciERC**\n2. `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/r16_70b_scierc_zs_s1/report/70b_scierc_zs_results.json` - **HAS metrics for zero-shot 70B baseline**\n3. `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/logs/workers/worker_eval_70b_lora_docred_inference_20260522T023202_result.json` - Status update (still running/recent)\n\n**Status of requested experiments:**\n- ✅ `eval_70b_lora_scierc_unconstrained` - **COMPLETED with results** (R-F1=44.73)\n- ⏳ `r16_70b_lora_scierc_eval` - Training complete, unconstrained eval complete, constrained eval status unclear\n- ⏳ `eval_70b_lora_docred_200_unconstrained` - Still running as of last checkpoint\n\n**Important Note:** The constrained (S1) evaluation results for the LoRA 70B models appear to still be in progress. The unconstrained baseline for SciERC LoRA shows strong performance (R-F1=44.73) compared to the zero-shot baseline (R-F1=11.15)."
      }
    ],
    "totalDurationMs": 60568,
    "totalTokens": 74996,
    "totalToolUseCount": 45,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 11180,
      "cache_read_input_tokens": 62341,
      "output_tokens": 1468,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 11180
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 1468,
          "cache_read_input_tokens": 62341,
          "cache_creation_input_tokens": 11180,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 11180,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 10,
      "searchCount": 4,
      "bashCount": 31,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 0
    }
  },
  "sourceToolAssistantUUID": "45287a44-fe50-48e3-a424-4f2841addb8a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6",
  "sessionId": "8b60bbb7-357b-4091-8cce-e13fa8ccd284",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 28 · 2026-05-22T05:59:13.352Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have the actual data for 70B LoRA SciERC unconstrained:
- E-F1: 64.86
- R-F1: 44.73
- DR: 1.50%
- ET/RV/CF: 0%
- Parse: 100%

This is important context. The unconstrained 70B LoRA SciERC has DR=1.50%, which is between the 8B Qwen LoRA (1.95%) and Llama LoRA (1.11%).


For the constrained version, I'd expect the DR to drop to around 0.5-3% with R-F1 declining by 0.5-3 percentage points to somewhere between 41.73-44.23. The 70B LoRA DocRED unconstrained is still running, but based on the 8B models—Llama hitting 43.72 R-F1 with 0.49% DR and Qwen at 40 R-F1—I can make an educated guess about where the 70B will land.

Now I'm looking at the actual results for the unconstrained SciERC run: 44.73 R-F1, 64.86 E-F1, and 1.50% DR with no other error types. For the constrained version, I'm predicting DR around 1.8% (within my 0.5-3% range) and R-F1 dropping to roughly 43.0, since even with constraints the quantization effects still introduce some degradation.

I'm reconsidering the parse failure rates though—the worst-case tier suggests >10% is possible, but that seems too high for SciERC given that even the 8B models hit 0% there. I'm adjusting my estimate to 5% for SciERC constrained and 12% for DocRED constrained, since longer documents are more vulnerable to parsing issues.

Actually, I realize the worst tier uses OR logic—any single failure mode crossing the threshold is enough, not all three simultaneously. So for SciERC I can lean on the 1.8% DR and ~1.7pp R-F1 drop with a modest 3% PF, while DocRED hits the >2pp R-F1 threshold at ~2.5pp with 2.5% DR and 8% PF. These feel more grounded than forcing 10%+ parse failures on both datasets.

Now looking at the actual range definitions for the worst tier, I should pick values closer to the middle of those ranges rather than the extremes—so for SciERC around 1.5% DR and -1.5pp R-F1 delta, and for DocRED around 2.5% DR and -2.5pp R-F1 delta, which aligns better with realistic degradation patterns. .5 = 43.5

For the parse failure rates, I'm estimating around 3% for SciERC and 10% for DocRED, since longer documents tend to cause more generation issues. Now I need to finalize the predictions, but I should check the worst-tier criteria first—the user specified that at least one of these conditions must hold: DR exceeding 1%, R-F1 dropping more than 2 percentage points, or parse failure rate above 10%. I'll make sure at least one metric clearly fails on each dataset to properly reflect the worst tier.

For SciERC, I'll set DR at 1.5% and PF at 3%, which hits the DR threshold. For DocRED, DR at 2.5% and R-F1 dropping 2.5 percentage points covers both the DR and R-F1 conditions, with PF borderline at 10%. This gives me a plausible worst case where both datasets degrade through different failure modes. Now I'm ready to construct the final YAML output, and I should also incorporate the actual 70B LoRA unconstrained SciERC data where available, noting which predictions are based on actual results versus estimates.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "534c990a-a8e6-4c78-bb27-59382d1e0473",
  "isSidechain": false,
  "requestId": "req_011CbH6SvVF58GEZC7RQj3tn",
  "type": "assistant",
  "uuid": "96ac166d-f985-4de0-b3f8-92018d96b3ba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6",
  "sessionId": "8b60bbb7-357b-4091-8cce-e13fa8ccd284",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PtxzT58eueTWRyZ9Lbr7qd",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 23663,
      "cache_read_input_tokens": 71159,
      "output_tokens": 14162,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 23663,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 14162,
          "cache_read_input_tokens": 71159,
          "cache_creation_input_tokens": 23663,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 23663
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

_source line 29 · 2026-05-22T06:03:06.028Z_

Good — the 70B LoRA SciERC unconstrained eval is complete with R-F1=44.73, DR=1.50%. DocRED eval still running. Now I have all the data needed to construct the worst-tier predictions.

```yaml
tier: worst
narrative_guidance: >
  核心 "type-valid IE" framing 不成立，需完全 reframe。仍冲 EMNLP 2026（October ARR cycle），不降级 venue。
  Reframe: "constrained decoding method paper" → "empirical study paper with a tool"。
  新 title: "How Do LLMs Violate Ontology Constraints? A Systematic Study with Mitigation"。
  新 story: (1) violation landscape 系统性实证研究为主贡献；(2) OntoCoDec 降级为 mitigation tool；
  (3) 重心转向 analysis findings — why prompt 不够、why post-hoc 不够、why grammar-only 不够、why CF 必然存在。
  Novelty 锚点从 method → empirical findings + theoretical analysis，回避 "incremental over XGrammar"。
  补充: (a) per-relation-type violation pattern 深度分析；(b) GoLLIE code-generation IE violation 对比；
  (c) decidability taxonomy 扩展为 formal framework。
  预估 reviewer 评分: Overall 2.5–3.5, Novelty 2–3, Soundness 3–3.5, Significance 2–3, hostile_reviewer_count 2–3。

imagined_experiments:
  - name: "WikiEvents Qwen3-8B unconstrained"
    plan_id: "P021"
    description: "WikiEvents EE unconstrained baseline, Qwen3-8B, 246 docs"
    expected_results:
      parse_rate_pct: 88.6
      EV_pct: 24.0
      RoV_pct: 74.9
      AC_pct: 0.3
      CF_pct: 0
      trigger_f1_pct: 11.84
      argument_f1_pct: 0.09
      entity_f1_pct: 0
    result_rationale: >
      已有实际数据。Entity-F1=0%、Arg-F1≈0% 是 ZS EE 固有困难——模型无法输出 schema-valid
      entity 格式。Worst 档 reviewer 抓住 baseline 几乎不工作这一点："Even the baseline shows
      EE is barely functional; any 'improvement' on near-zero is format compliance recovery,
      not semantic extraction." RoV=74.9% 虽然展示了 constraint 需求，但 reviewer 反转叙事：
      "This proves ZS EE is fundamentally broken, not that your method fixes it."
    tables:
      - name: "WikiEvents ZS Unconstrained Baselines (3 Models)"
        columns: ["Model", "Parse%", "EV%", "RoV%", "AC%", "Trig-F1", "Arg-F1", "Ent-F1"]
        rows:
          - ["Qwen3-8B", "88.6", "24.0", "74.9", "0.3", "11.8", "0.09", "0"]
          - ["Llama-3.1-8B", "91.9", "10.5", "88.8", "0.1", "5.7", "0", "0"]
          - ["Mistral-7B", "78.9", "37.3", "63.9", "0", "2.4", "0", "0"]
    figures_description:
      - "Per-model violation type stacked bar chart (EV/RoV/AC)"
    analysis: >
      三模型 Entity-F1=0% / Arg-F1≈0% 成为 "EE completely dismissed" 的核心证据。
      Reviewer: "Arg F1≈0, Entity F1 from 0→14% is just format compliance, not extraction
      improvement." 不视为 constraint enforcement 机会，而视为 task 选择失败。

  - name: "WikiEvents Llama-3.1-8B unconstrained"
    plan_id: "P023"
    description: "WikiEvents EE unconstrained baseline, Llama-3.1-8B, 246 docs"
    expected_results:
      parse_rate_pct: 91.9
      EV_pct: 10.5
      RoV_pct: 88.8
      AC_pct: 0.1
      CF_pct: 0
      trigger_f1_pct: 5.72
      argument_f1_pct: 0
      entity_f1_pct: 0
    result_rationale: >
      已有实际数据。Llama RoV=88.8% 是三模型最高——近 9/10 argument role 不在 event type
      定义中。Trigger-F1=5.7% 低于 Qwen。Worst 档 reviewer: "This model is completely
      non-functional for EE. Constrained decoding on non-functional extraction is
      a constraint compliance demo, not an IE contribution."
    tables: []
    figures_description: []
    analysis: >
      Llama RoV=88.8% 超过 Qwen 74.9%，模型间 violation pattern 差异巨大，但 worst-tier
      reviewer 不关心差异，只关心 Arg-F1=0%。

  - name: "WikiEvents Mistral-7B unconstrained"
    plan_id: "P025"
    description: "WikiEvents EE unconstrained baseline, Mistral-7B-v0.3, 246 docs"
    expected_results:
      parse_rate_pct: 78.9
      EV_pct: 37.3
      RoV_pct: 63.9
      AC_pct: 0
      CF_pct: 0
      trigger_f1_pct: 2.41
      argument_f1_pct: 0
      entity_f1_pct: 0
    result_rationale: >
      已有实际数据。Parse rate 最低 (78.9%)，EV 最高 (37.3%)——超 1/3 event type 是 OOV。
      Trigger-F1=2.4% 几乎为零。Worst 档 reviewer: "If your chosen model can't even produce
      valid event type names 37% of the time, the task setup itself is problematic." 选择明显
      不适合此 task 的模型被质疑为 cherry-pick 不利 baseline 以夸大改善。
    tables: []
    figures_description: []
    analysis: >
      Mistral 是 EE 最差模型。Worst-tier reviewer 质疑为何选择它——如果用来展示"更差模型更需要
      constraint"，那 Arg-F1=0% 的 baseline 使任何 improvement 都无意义。

  - name: "WikiEvents Mistral grammar-only v3"
    plan_id: "P027"
    description: "Grammar-only ablation on Mistral WikiEvents, proves semantic layer necessity for EE"
    expected_results:
      parse_rate_pct: 88.6
      EV_pct: 0
      RoV_pct: 64.0
      AC_pct: 13.8
      CF_pct: 1.1
      entity_f1_pct: 11.92
      trigger_f1_pct: 3.37
      argument_f1_pct: 0.27
    result_rationale: >
      已有实际数据。Grammar-only 消除 EV→0% 但 RoV 仍 64%——grammar CFG 无法约束 80 个
      event-type-conditioned argument roles。AC 上升至 13.8%（latent violation surfacing，
      与 DocRED RE 模式一致）。本应是 two-layer necessity 有力证据。但 worst 档 reviewer:
      "Of course grammar can't do semantic constraints — this is not an insight, it's an
      expected outcome. Your ablation confirms the obvious." 被视为 trivially expected，
      不构成 contribution。更关键: CF 从 1.1%(grammar-only) 升到 14.9%(full_s1)——
      semantic 层引入大量 CF。
    tables:
      - name: "WikiEvents Grammar-Only vs Full S1 (Mistral)"
        columns: ["Config", "EV%", "RoV%", "AC%", "CF%", "Ent-F1"]
        rows:
          - ["unconstrained", "37.3", "63.9", "0", "0", "0"]
          - ["grammar_only", "0", "64.0", "13.8", "1.1", "11.9"]
          - ["full_s1", "0", "0", "1.3", "14.9", "11.7"]
    figures_description:
      - "Three-bar violation distribution comparison: unconstrained / grammar_only / full_s1"
    analysis: >
      Ablation 结论正确但被视为 trivial。更致命的是数据暴露了 CF trade-off: grammar_only
      CF=1.1% → full_s1 CF=14.9%。Reviewer: "Adding your semantic layer increases
      cross-field violations by 14× while providing no extraction quality improvement.
      The cure is worse than the disease."

  - name: "WikiEvents EE post-hoc filtering (3 models)"
    plan_id: "P028"
    description: "Post-hoc filtering baseline for EE, quantifies argument deletion rate"
    expected_results:
      qwen_args_before: 5467
      qwen_args_after: 23
      qwen_discard_pct: 99.6
      llama_args_before: 5053
      llama_args_after: 3
      llama_discard_pct: 99.9
      mistral_args_before: 6034
      mistral_args_after: 0
      mistral_discard_pct: 100.0
    result_rationale: >
      已有实际数据（从 v3 constrained 结果的 posthoc 字段计算）。Post-hoc 需删除 99.6-100%
      arguments 才能达 0% violation——RE 中仅 16-48%。本应是 paper 强力卖点（"post-hoc non-viable
      for EE, constrained decoding is the only option"）。但 worst 档 reviewer 翻转叙事:
      "This confirms ZS EE is fundamentally broken, not that your method solves it. When
      99.6% of generated arguments are violations, the model has no understanding of the
      task — your grammar is just producing well-formatted noise."
    tables:
      - name: "Post-hoc Filtering: RE vs EE Discard Rate"
        columns: ["Task", "Model", "Discard%", "Remaining"]
        rows:
          - ["RE SciERC", "Qwen", "16.8%", "1435 triples"]
          - ["RE DocRED", "Qwen", "48.1%", "9076 triples"]
          - ["EE WikiEvents", "Qwen", "99.6%", "23 args"]
          - ["EE WikiEvents", "Llama", "99.9%", "3 args"]
          - ["EE WikiEvents", "Mistral", "100%", "0 args"]
    figures_description:
      - "Bar chart comparing post-hoc discard rates across RE and EE tasks"
    analysis: >
      Post-hoc 毁灭性结果在 worst 档被用来否定整个 EE evaluation 的价值。Reviewer 不接受
      "constrained decoding is the only option" 论点，而认为 "no option works for ZS EE,
      so why evaluate it."

  - name: "70B SciERC unconstrained + constrained (ZS)"
    plan_id: "P029"
    description: "Qwen3-70B AWQ-INT4 on SciERC ZS, scale generalization 8B→70B"
    expected_results:
      unconstrained_DR_pct: 6.5
      unconstrained_RV_pct: 0.6
      unconstrained_R_F1: 11.22
      unconstrained_E_F1: 35.17
      constrained_DR_pct: 0
      constrained_CF_pct: 3.66
      constrained_R_F1: 11.24
      constrained_E_F1: 35.14
      parse_failures: 0
    result_rationale: >
      已有实际数据。DR=0% 是完美消除，CF=3.66% 低于 8B 的 9.9%。但 worst 档关注两点:
      (1) R-F1=11.24% 仍是 "toy evaluation" — "A 70B model achieving 11% relation F1 in
      ZS is not a serious evaluation setting."
      (2) 70B unconstrained DR=6.5% 远低于 8B 的 15.4% — "Larger models are already more
      constraint-compliant; the marginal value of your method diminishes with scale."
      即 DR=0% 被视为 expected（大模型本来就更合规），不是 method contribution。
    tables:
      - name: "Scale Comparison: 8B vs 70B ZS SciERC"
        columns: ["Model", "DR-unc%", "DR-con%", "CF-con%", "R-F1"]
        rows:
          - ["Qwen3-8B", "15.37", "0.93", "9.90", "8.36"]
          - ["Llama-3.1-8B", "13.34", "0.08", "6.56", "2.54"]
          - ["Qwen3-70B", "6.50", "0.00", "3.66", "11.24"]
    figures_description:
      - "Model scale vs baseline violation rate, showing diminishing marginal constraint value"
    analysis: >
      70B 创造两难: (a) DR=0% 证明方法完美工作; (b) 大模型 baseline violation 更低，削弱
      "需要 constrained decoding" 论点。Reviewer: "As models scale, they naturally become
      more compliant. Your method solves a problem that is disappearing."

  - name: "70B DocRED unconstrained + constrained (ZS)"
    plan_id: "P030"
    description: "Qwen3-70B AWQ-INT4 on DocRED ZS, scale generalization"
    expected_results:
      unconstrained_DR_pct: 15.0
      unconstrained_RV_pct: 7.8
      unconstrained_ET_pct: 0.02
      unconstrained_R_F1: 13.03
      unconstrained_E_F1: 69.03
      constrained_DR_pct: 0
      constrained_CF_pct: 7.01
      constrained_R_F1: 13.07
      constrained_E_F1: 69.05
      parse_failures: 1
    result_rationale: >
      已有实际数据。DR=0% 是 DocRED 上的最佳结果（优于 Qwen-8B 10.21%、Llama-8B 2.55%）。
      但 CF=7.01%。Worst 档: "On DocRED (96 relations), CF=7.01% means roughly 1 in 14
      entities has inconsistent typing. Combined with 8B CF=10-12%, this is systematic,
      not a corner case." 70B unc DR=15% 与 8B Qwen DR=18.46% 差距不大——
      "70B doesn't help much on DocRED, yet your method introduces 7% CF."
      CF 没有随模型规模减少（70B CF=7.01% > Qwen-8B CF=2.57%），支持 "CF is inherent to
      the method" 攻击线。
    tables:
      - name: "DocRED Cross-Scale CF Comparison"
        columns: ["Model", "DR-unc%", "DR-con%", "CF-con%", "R-F1-delta"]
        rows:
          - ["Qwen3-8B", "18.46", "10.21", "2.57", "+0.50"]
          - ["Llama-3.1-8B", "26.07", "2.55", "12.02", "+0.29"]
          - ["Qwen3-70B", "15.00", "0.00", "7.01", "+0.04"]
    figures_description: []
    analysis: >
      DocRED 70B CF=7.01% 介于 Qwen-8B (2.57%) 和 Llama-8B (12.02%) 之间，没有 scale
      改善趋势。Reviewer 判定 CF 是方法固有缺陷，非模型 artifact。

  - name: "Error analysis / case study"
    plan_id: "P031"
    description: "10-20 representative cases: AC residual 根因、CF root cause、qualitative evidence"
    expected_results:
      ac_residual_cases_examined: 15
      cf_root_cause_type_ambiguity_pct: 45
      cf_root_cause_model_confusion_pct: 40
      cf_root_cause_ontology_gap_pct: 15
      actionable_insight_count: 2
    result_rationale: >
      预测数据（定性分析）。AC 残余案例显示模型在语义相近 entity types（SID vs SEN, PER vs SID）
      上持续混淆——constrained decoding 无法解决语义理解问题。CF 根因: ~45% 来自 ontology type
      system 语义边界模糊（Generic↔OtherScientificTerm），40% 来自模型在不同 relation context
      下对同一 entity 的 type assignment 不一致，15% 来自 ontology 设计缺陷。
      Worst 档 reviewer 引用 case study: "Nearly half of CF is a dataset artifact and 40%
      is a model capability problem — neither is addressable by constrained decoding. The
      error analysis reveals that the method's limitations are more interesting than its
      contributions."
    tables: []
    figures_description:
      - "Entity type confusion matrix for CF violations"
      - "Case study examples with annotated violation chains"
    analysis: >
      Error analysis 在 worst 档反而成为攻击弹药。每个 case 指向 constrained decoding 根本
      局限: 只能 enforce 局部约束，无法解决跨 relation 一致性和模型语义理解。Reviewer 直接
      引用 case study 论证 limitations > contributions。

  - name: "EE FT composability"
    plan_id: "P032"
    description: "Fine-tuned model + OntoCoDec composability on WikiEvents EE"
    expected_results:
      qwen_ft_unc_trigger_f1: 32.08
      qwen_ft_unc_arg_f1: 7.85
      qwen_ft_unc_rov_pct: 38.3
      qwen_ft_con_trigger_f1: 26.72
      qwen_ft_con_arg_f1: 8.18
      qwen_ft_con_rov_pct: 0
      qwen_ft_con_ac_pct: 0
      llama_ft_unc_trigger_f1: 27.52
      llama_ft_unc_arg_f1: 9.98
      llama_ft_unc_rov_pct: 8.8
      llama_ft_con_trigger_f1: 26.91
      llama_ft_con_arg_f1: 8.91
      llama_ft_con_rov_pct: 0
      llama_ft_con_ac_pct: 0.8
    result_rationale: >
      已有实际数据（p1_ee_ft_composability_r5 + p1_ee_ft_llama_r2）。关键问题:
      (1) Qwen Trigger-F1 从 32.08%→26.72%（-5.36pp），constrained decoding 明显损害
      trigger extraction 质量。Reviewer: "Your method trades extraction quality for constraint
      compliance — Structure Snowballing (Tam et al. 2024) already documented this trade-off."
      (2) Arg-F1 改善微乎其微（Qwen +0.33pp, Llama -1.07pp 实际下降）。
      (3) Llama constrained AC=0.8% 表明 FT regime 下仍无法完全消除 argument constraint violations。
      Reviewer 总结: "The only outcome is constraint compliance at the cost of extraction
      performance. This is a net negative contribution."
    tables:
      - name: "EE FT Composability Impact"
        columns: ["Model", "Config", "Trig-F1", "Arg-F1", "RoV%", "AC%"]
        rows:
          - ["Qwen", "unconstrained", "32.08", "7.85", "38.3", "2.7"]
          - ["Qwen", "constrained", "26.72", "8.18", "0", "0"]
          - ["Llama", "unconstrained", "27.52", "9.98", "8.8", "3.5"]
          - ["Llama", "constrained", "26.91", "8.91", "0", "0.8"]
    figures_description:
      - "Paired bar chart: Trigger-F1 degradation under constrained decoding in FT EE"
    analysis: >
      EE FT composability 在 worst 档被完全 dismiss。核心攻击:
      (a) Trigger-F1 降 5pp 是 unacceptable quality degradation;
      (b) Arg-F1 改善不显著且 Llama 实际下降;
      (c) "This confirms constrained decoding for IE is a straightforward application of
      XGrammar with a lookup table."

  - name: "Grammar-only cross-model validation (Qwen/Llama EE)"
    plan_id: "P033"
    description: "Grammar-only ablation on Qwen 和 Llama WikiEvents EE for completeness"
    expected_results:
      qwen_grammar_only_EV_pct: 0
      qwen_grammar_only_RoV_pct: 71.5
      qwen_grammar_only_AC_pct: 10.2
      qwen_grammar_only_CF_pct: 0.7
      qwen_grammar_only_entity_f1: 13.8
      llama_grammar_only_EV_pct: 0
      llama_grammar_only_RoV_pct: 76.4
      llama_grammar_only_AC_pct: 14.5
      llama_grammar_only_CF_pct: 0.5
      llama_grammar_only_entity_f1: 17.2
    result_rationale: >
      预测数据。基于 Mistral grammar-only 模式（RoV=64%, AC=13.8%），Qwen/Llama 预计:
      EV→0%（grammar 消除）, RoV 保持 70-77%（grammar 无法约束 event-conditioned roles）,
      AC 上升至 10-15%（latent violation surfacing）。Worst 档 reviewer: "Redundant — the
      Mistral ablation already shows this, and the conclusion is trivially expected." 三模型
      一致性虽是完整消融证据，但被视为不增加 insight。
    tables:
      - name: "EE Grammar-Only Ablation (3 Models)"
        columns: ["Model", "EV%", "RoV%", "AC%", "CF%", "Ent-F1"]
        rows:
          - ["Mistral (actual)", "0", "64.0", "13.8", "1.1", "11.9"]
          - ["Qwen (predicted)", "0", "71.5", "10.2", "0.7", "13.8"]
          - ["Llama (predicted)", "0", "76.4", "14.5", "0.5", "17.2"]
    figures_description: []
    analysis: >
      三模型 grammar-only 一致模式（EV→0%, RoV≫0%, AC↑）在方法论上完整，但 reviewer 认为
      不增加任何 insight: "it's obvious that grammar constraints can only handle vocabulary-level
      violations, not semantic ones."

  - name: "Bootstrap CI for EE metrics"
    plan_id: "P034"
    description: "Statistical significance testing for EE F1 changes (10000× bootstrap)"
    expected_results:
      qwen_trigger_f1_delta_pp: 1.55
      qwen_trigger_f1_p: 0.18
      qwen_entity_f1_delta_pp: 14.09
      qwen_entity_f1_p: 0.001
      qwen_arg_f1_delta_pp: 1.59
      qwen_arg_f1_p: 0.42
      llama_trigger_f1_delta_pp: 1.76
      llama_trigger_f1_p: 0.22
      llama_entity_f1_delta_pp: 17.63
      llama_entity_f1_p: 0.001
      llama_arg_f1_delta_pp: 1.18
      llama_arg_f1_p: 0.38
      mistral_trigger_f1_delta_pp: 1.46
      mistral_trigger_f1_p: 0.31
      mistral_entity_f1_delta_pp: 11.71
      mistral_entity_f1_p: 0.001
      mistral_arg_f1_delta_pp: 0.31
      mistral_arg_f1_p: 0.61
    result_rationale: >
      预测数据。Bootstrap CI 预计显示:
      (a) Entity-F1 改善（0%→11-17%）统计显著（p<0.01），但完全来自 format compliance 恢复
      （grammar 强制 valid JSON → parser 识别 entity）——不是语义提升。
      (b) Trigger-F1 改善（+1.5-1.8pp）全部不显著（p>0.15），绝对值太低（3-13%）variance 太大。
      (c) Arg-F1 改善全部不显著——绝对值接近零。
      Worst 档 reviewer: "The only statistically significant improvement is entity F1, which is
      entirely attributable to format compliance, not extraction improvement. No significant
      improvement on any semantically meaningful metric."
    tables:
      - name: "EE Bootstrap CI Summary"
        columns: ["Model", "Metric", "Delta-pp", "p-value", "Sig?"]
        rows:
          - ["Qwen", "Trigger-F1", "+1.55", "0.18", "No"]
          - ["Qwen", "Entity-F1", "+14.09", "<0.001", "Yes*"]
          - ["Qwen", "Arg-F1", "+1.59", "0.42", "No"]
          - ["Llama", "Trigger-F1", "+1.76", "0.22", "No"]
          - ["Llama", "Entity-F1", "+17.63", "<0.001", "Yes*"]
          - ["Llama", "Arg-F1", "+1.18", "0.38", "No"]
          - ["Mistral", "Trigger-F1", "+1.46", "0.31", "No"]
          - ["Mistral", "Entity-F1", "+11.71", "<0.001", "Yes*"]
          - ["Mistral", "Arg-F1", "+0.31", "0.61", "No"]
    figures_description:
      - "Forest plot of EE F1 deltas with 95% CI, *=format compliance only"
    analysis: >
      Bootstrap CI 成为双刃剑: Entity-F1 显著但仅是 format compliance（*标注），
      Trigger-F1 和 Arg-F1 均不显著。Reviewer: "No significant improvement on any
      semantically meaningful metric." 这与 RE 结果（DocRED R-F1 +0.50pp p<0.001）形成
      对比，强化 "EE 实验是 toy" 的攻击。

  - name: "Latency overhead measurement"
    plan_id: "P035"
    description: "Wall-clock comparison: unconstrained vs constrained decoding overhead"
    expected_results:
      zs_scierc_overhead_pct: 13.1
      zs_scierc_mean_unc_s: 4.163
      zs_scierc_mean_con_s: 4.71
      ft_scierc_overhead_pct: 10.0
      ft_scierc_mean_unc_s: 2.612
      ft_scierc_mean_con_s: 2.873
      beam4_constraint_overhead_pct: 16.5
    result_rationale: >
      已有实际数据（p8_latency_overhead: 13.1%, p8c_ft_scierc_latency: 10%）。Latency
      本身不是主要攻击面——13% 可接受。但 worst 档 reviewer 将其嵌入 cost-benefit: "13% latency
      for a method that introduces 10-21% cross-field violations and achieves no significant
      F1 improvement in ZS — the trade-off is unfavorable." 在综合评估中作为 additional cost。
    tables:
      - name: "Latency Overhead Summary"
        columns: ["Setting", "Overhead%", "unc s/doc", "con s/doc"]
        rows:
          - ["ZS SciERC", "13.1", "4.16", "4.71"]
          - ["FT SciERC", "10.0", "2.61", "2.87"]
          - ["FT Beam-4", "16.5", "3.45", "4.01"]
    figures_description: []
    analysis: >
      Latency 单独不构成 reject 理由，但 reviewer 在综合评估中使用: "Your method adds 13%
      latency, introduces CF violations, and provides no significant F1 gain in ZS."

  # --- 70B LoRA Experiments (worst tier 核心假设，不在原始 plan 中) ---

  - name: "70B LoRA SciERC unconstrained eval"
    plan_id: "R16_70B_LORA_SCIERC_UNC"
    description: "Qwen3-70B AWQ-INT4 LoRA fine-tuned, SciERC unconstrained evaluation"
    expected_results:
      R_F1: 44.73
      E_F1: 64.86
      DR_pct: 1.50
      RV_pct: 0
      ET_pct: 0
      CF_pct: 0
      parse_fail_pct: 0
      total_samples: 551
    result_rationale: >
      已有实际数据（eval_70b_lora_scierc_unconstrained DONE）。R-F1=44.73% 与 8B LoRA
      Qwen (43.86%) 和 Llama (45.45%) 在同一水平——70B+AWQ-INT4 量化并未带来显著优势。
      DR baseline=1.50% 高于 Llama-8B LoRA (1.11%) 但低于 Qwen-8B LoRA (1.95%)。
      关键: 这个 baseline 设定了 constrained eval 的对比基准。如果 constrained 版本 DR
      不能显著降低，或 R-F1 明显下降，70B LoRA 实验就变成负面证据。
    tables: []
    figures_description: []
    analysis: >
      Unconstrained baseline 本身不是问题，R-F1=44.73% 是合理的。关键是 constrained
      eval 会如何表现。

  - name: "70B LoRA SciERC constrained eval"
    plan_id: "R16_70B_LORA_SCIERC_CON"
    description: "Qwen3-70B AWQ-INT4 LoRA, SciERC constrained (full_s1) — worst tier 核心预测"
    expected_results:
      R_F1: 43.2
      E_F1: 64.5
      DR_pct: 1.5
      RV_pct: 0
      ET_pct: 0
      CF_pct: 2.2
      parse_fail_pct: 5.0
      total_samples: 551
      delta_R_F1_pp: -1.53
      delta_E_F1_pp: -0.36
    result_rationale: >
      预测数据（worst tier 核心假设: DR>1% 或 R-F1 下降 >2pp 或 PF>10%）。
      DR=1.5%（范围 [0.5, 3.0]）: constrained decoding 未能消除 DR，与 8B LoRA 的 DR=0-0.09%
      形成鲜明对比。机制: AWQ-INT4 量化导致 logit distribution 偏移，semantic mask 的 top-k
      fallback 更频繁触发，残余 DR 更高。quantized logits 的 precision 不够导致 mask 边界
      附近的 token 概率计算不精确。
      R-F1 下降 1.53pp（范围 [-3.0, -0.5]）: 从 44.73→43.2%，虽未超过 -2pp threshold，但
      方向与 8B LoRA 的 near-zero/positive delta 完全相反。
      PF=5%: 量化模型在 constrained decoding 下偶尔产生重复或 truncation，但 SciERC 文档短，
      PF 不至于超过 10%。
      综合: DR>1% 已触发 worst tier 条件。Reviewer: "Your method fails to eliminate domain-range
      violations on a quantized 70B model — the deployment scenario where guarantees matter most."
    tables:
      - name: "LoRA SciERC: 8B vs 70B Constrained Impact"
        columns: ["Model", "unc DR%", "con DR%", "DR-reduction%", "R-F1 delta", "PF%"]
        rows:
          - ["Qwen-8B LoRA", "1.95", "0", "100", "-0.09", "0"]
          - ["Llama-8B LoRA", "1.11", "0.09", "92", "+0.02", "0"]
          - ["Qwen-70B LoRA (pred)", "1.50", "1.50", "0", "-1.53", "5.0"]
    figures_description:
      - "Model size vs DR reduction rate: 8B achieves 92-100%, 70B achieves 0%"
    analysis: >
      70B LoRA SciERC constrained 在 worst 档是关键打击: DR reduction=0%（constrained DR
      等于 unconstrained DR），意味着 semantic mask 在量化模型上完全失效。R-F1 同时下降 1.5pp。
      Reviewer: "At 70B scale with INT4 quantization, your semantic constraints provide
      zero DR reduction while degrading extraction quality by 1.5pp. This undermines the
      entire scale generalization claim."

  - name: "70B LoRA DocRED unconstrained eval"
    plan_id: "R16_70B_LORA_DOCRED_UNC"
    description: "Qwen3-70B AWQ-INT4 LoRA, DocRED unconstrained — 实验 RUNNING"
    expected_results:
      R_F1: 46.2
      E_F1: 85.0
      DR_pct: 0.65
      RV_pct: 0.05
      ET_pct: 0
      CF_pct: 0.04
      parse_fail_pct: 3.5
      total_samples: 200
    result_rationale: >
      预测数据（实验 RUNNING，200 docs 子集）。基于 8B LoRA DocRED 结果推断:
      Qwen-8B LoRA R-F1=40.86, Llama-8B LoRA R-F1=43.72, 70B 预计 +3-5pp 提升至 ~46%。
      E-F1 预计 ~85%（8B 范围 82-84%，70B 更强）。DR baseline 0.65%（8B 范围 0.49-0.76%）。
      200 docs 子集使得结果统计 power 较弱，增加 reviewer 质疑空间。
    tables: []
    figures_description: []
    analysis: >
      200 docs 子集（而非 998 全量）在 worst 档被 reviewer 质疑: "Why only 200 documents
      for your most important scale experiment? This looks like a convenience sample, not
      a rigorous evaluation."

  - name: "70B LoRA DocRED constrained eval"
    plan_id: "R16_70B_LORA_DOCRED_CON"
    description: "Qwen3-70B AWQ-INT4 LoRA, DocRED constrained (full_s1) — worst tier 核心预测"
    expected_results:
      R_F1: 43.7
      E_F1: 84.5
      DR_pct: 2.8
      RV_pct: 0
      ET_pct: 0
      CF_pct: 1.8
      parse_fail_pct: 11.0
      total_samples: 200
      delta_R_F1_pp: -2.5
      delta_E_F1_pp: -0.5
    result_rationale: >
      预测数据（worst tier 核心假设: DR>1% 或 R-F1 下降 >2pp 或 PF>10%）。
      DR=2.8%（范围 [0.5, 5.0]）: DocRED 96-relation ontology 下量化模型的 semantic mask
      fallback 更频繁。8B LoRA DocRED constrained DR=0.01-0.21%，70B 的 2.8% 是数量级恶化。
      机制: 量化后 logit space 的 probability mass 在 96-relation ontology 下分布更不均匀，
      semantic mask 与 grammar mask 的 intersection 更常为空→更多 fallback→更高残余 DR。
      R-F1 下降 2.5pp（范围 [-4.0, -1.0]）: 从 46.2%→43.7%。这甚至低于 8B Llama LoRA
      constrained (43.78%)——70B+量化+constrained 组合效果不如 8B full-precision。
      PF=11%（>10% threshold）: DocRED 长文档 + 量化 + constrained 三重因素叠加导致生成
      退化（重复序列、early truncation、malformed JSON）。22 docs/200 无法评估。
      综合: 全部三个 threshold 都被触发（DR>1% ✓, R-F1 drop >2pp ✓, PF>10% ✓）。
    tables:
      - name: "LoRA DocRED: 8B vs 70B Constrained Full Comparison"
        columns: ["Model", "DR-con%", "CF%", "R-F1", "R-F1-delta", "PF%"]
        rows:
          - ["Qwen-8B LoRA", "0.01", "0.41", "40.56", "-0.30", "8.5"]
          - ["Llama-8B LoRA", "0.21", "0.21", "43.78", "+0.06", "2.5"]
          - ["Qwen-70B LoRA (pred)", "2.80", "1.80", "43.70", "-2.50", "11.0"]
    figures_description:
      - "Scatter: model size vs constrained decoding effectiveness (DR reduction %)"
      - "Bar: R-F1 delta under constrained decoding, 8B vs 70B"
    analysis: >
      70B LoRA DocRED 在 worst 档是 scale generalization claim 终结。三重失败:
      (a) DR 2.8%——constrained 仍有显著残余 violations;
      (b) R-F1 下降 2.5pp 至 43.7%——低于 8B Llama LoRA constrained 43.78%;
      (c) 11% parse failures——22/200 docs 不可评估。
      Reviewer: "On DocRED, the 70B quantized model with constraints performs WORSE than
      the 8B full-precision model, while being far more expensive to run. The method does
      not scale to practical deployment scenarios with quantized large models."
      这与 70B ZS 的 DR=0% 形成对比: "Your method works at 70B only in zero-shot where F1
      is 13% (toy); in the fine-tuned regime where F1 is meaningful (~46%), it fails."

  # --- Post-hoc vs Constrained (ZS regime, 已有数据但 worst tier 解读关键) ---

  - name: "Post-hoc vs Constrained ZS Regime (6 configs)"
    plan_id: "W8_POSTHOC_ZS"
    description: "Post-hoc filtering R-F1 全面优于 constrained decoding in 5/6 ZS configs — worst tier 核心假设"
    expected_results:
      qwen_scierc_posthoc_R_F1: 8.63
      qwen_scierc_constrained_R_F1: 8.36
      qwen_scierc_posthoc_wins: true
      llama_scierc_posthoc_R_F1: 2.71
      llama_scierc_constrained_R_F1: 2.54
      llama_scierc_posthoc_wins: true
      mistral_scierc_posthoc_R_F1: 3.94
      mistral_scierc_constrained_R_F1: 3.67
      mistral_scierc_posthoc_wins: true
      qwen_docred_posthoc_R_F1: 9.61
      qwen_docred_constrained_R_F1: 8.23
      qwen_docred_posthoc_wins: true
      llama_docred_posthoc_R_F1: 7.44
      llama_docred_constrained_R_F1: 6.27
      llama_docred_posthoc_wins: true
      mistral_docred_posthoc_R_F1: 3.85
      mistral_docred_constrained_R_F1: 5.52
      mistral_docred_posthoc_wins: false
      posthoc_win_count: 5
      posthoc_total_configs: 6
    result_rationale: >
      已有实际数据（w8_ft_posthoc_baseline）。Post-hoc R-F1 >= constrained R-F1 in 5/6 ZS
      configs。仅 Mistral DocRED（极端 73.7% rejection rate 导致 TP 大量丢失）例外。
      机制: low F1 regime 下（R-F1 < 13%），most predicted triples are FP。Post-hoc 通过删除
      violating triples 移除大量 FP，precision 大幅提升。Constrained decoding 虽保留更多 triples
      （包括 TP），但 FP 也更多。当 FP/TP ratio >> 1 时，post-hoc 的 precision gain 超过 recall loss。
      Worst 档 reviewer: "In the zero-shot regime that constitutes 60% of your evaluation,
      a simple post-hoc filter consistently outperforms your constrained decoding on the
      metric that matters (F1). What's the point of engineering a complex constrained
      decoding pipeline when removing bad triples after generation works better?"
    tables:
      - name: "ZS Post-hoc vs Constrained R-F1"
        columns: ["Dataset", "Model", "Post-hoc R-F1", "Constrained R-F1", "Winner"]
        rows:
          - ["SciERC", "Qwen", "8.63", "8.36", "Post-hoc"]
          - ["SciERC", "Llama", "2.71", "2.54", "Post-hoc"]
          - ["SciERC", "Mistral", "3.94", "3.67", "Post-hoc"]
          - ["DocRED", "Qwen", "9.61", "8.23", "Post-hoc"]
          - ["DocRED", "Llama", "7.44", "6.27", "Post-hoc"]
          - ["DocRED", "Mistral", "3.85", "5.52", "Constrained"]
    figures_description:
      - "Paired dot plot: post-hoc vs constrained R-F1 for 6 ZS configs with winner highlighted"
    analysis: >
      5/6 ZS configs post-hoc wins on R-F1。这是 worst 档最致命的 finding。Reviewer 直接问:
      "What's the point?" Paper 的 counter-arguments（recall preservation, operational
      properties, information coverage）在 ZS regime 的 sub-10% F1 下不具说服力。
      Reframe 方向: 将 constrained decoding 的价值锚定在 (a) FT regime（post-hoc wins 消失），
      (b) EE task（post-hoc 删除 99.6-100%），(c) structural guarantee（per-instance
      compliance vs statistical compliance），避开 ZS F1 比较。
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "96ac166d-f985-4de0-b3f8-92018d96b3ba",
  "isSidechain": false,
  "requestId": "req_011CbH6SvVF58GEZC7RQj3tn",
  "type": "assistant",
  "uuid": "fac9ac75-5aef-4758-a42e-8902e650fd63",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6",
  "sessionId": "8b60bbb7-357b-4091-8cce-e13fa8ccd284",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PtxzT58eueTWRyZ9Lbr7qd",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 23663,
      "cache_read_input_tokens": 71159,
      "output_tokens": 14162,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 23663,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 14162,
          "cache_read_input_tokens": 71159,
          "cache_creation_input_tokens": 23663,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 23663
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

_source line 30_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：≥2 reviewers 认为 novelty 不足以支撑 main conference；核心 'guaranteed compliance' claim 被 CF 数据和 post-hoc 比较削弱；需要 reframe 切入角度 核心假设：[\"Novelty 被拒：'constrained decod…",
  "leafUuid": "fac9ac75-5aef-4758-a42e-8902e650fd63",
  "sessionId": "8b60bbb7-357b-4091-8cce-e13fa8ccd284"
}
```

---

### Runtime record

_source line 31_

```json
{
  "type": "ai-title",
  "aiTitle": "Ontology constraint violations in LLM-based IE—worst case analysis",
  "sessionId": "8b60bbb7-357b-4091-8cce-e13fa8ccd284"
}
```

---

### Runtime record

_source line 32_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：≥2 reviewers 认为 novelty 不足以支撑 main conference；核心 'guaranteed compliance' claim 被 CF 数据和 post-hoc 比较削弱；需要 reframe 切入角度 核心假设：[\"Novelty 被拒：'constrained decod…",
  "leafUuid": "fac9ac75-5aef-4758-a42e-8902e650fd63",
  "sessionId": "8b60bbb7-357b-4091-8cce-e13fa8ccd284"
}
```

---

### Runtime record

_source line 33_

```json
{
  "type": "ai-title",
  "aiTitle": "Ontology constraint violations in LLM-based IE—worst case analysis",
  "sessionId": "8b60bbb7-357b-4091-8cce-e13fa8ccd284"
}
```

---
