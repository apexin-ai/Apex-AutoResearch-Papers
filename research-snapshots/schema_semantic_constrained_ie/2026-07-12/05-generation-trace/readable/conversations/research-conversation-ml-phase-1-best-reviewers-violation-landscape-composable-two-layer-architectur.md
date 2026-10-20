# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义： 含义：Reviewers 认可 violation landscape + composable two-layer architecture 为双重贡献；c

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 43
- **Recorded user turns:** 1
- **Tool calls:** 9
- **Original source:** `logs/chats/exported-trajectories/account-3/b82a3282-ed21-4676-9e91-4d9b245dd612.jsonl`
- **Structured JSON:** [`df668574f415e677f759.json`](../../sessions/df/df668574f415e677f759.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-22T05:28:55.005Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-22T05:28:55.005Z",
  "sessionId": "b82a3282-ed21-4676-9e91-4d9b245dd612",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：\n\n含义：Reviewers 认可 violation landscape + composable two-layer architecture 为双重贡献；cross-task (RE+EE) 证据链完整；70B LoRA 结果干净\n核心假设：['Violation landscape study 被视为独立 empirical contribution（非仅 motivation section）', \"Stateful entity registry + decidability taxonomy + automatic ontology compilation 的组合被视为超越 'XGrammar for IE' 的方法论创新\", 'WikiEvents EE 的 EV/RoV→0% + grammar-only ablation 被接受为 cross-task generalization 的充分证据，Arg F1≈0 不被视为致命缺陷', 'CF tradeoff 的 proactive disclosure + root cause analysis + beam search mitigation 被接受为诚实且充分的处理', '70B LoRA eval: DR≤0.1%, |ΔR-F1|≤0.3pp（复现 8B LoRA 的 scale-neutral 模式）', '至少 2/3 reviewers 认可 novelty 不仅是 engineering 而是 methodological advance']\n关键指标范围：{'emnlp_overall_assessment': [4.0, 4.5], 'review_novelty': [3.5, 4.0], 'review_soundness': [4.0, 4.5], 'review_significance': [3.5, 4.0], '70b_lora_scierc_DR_pct': [0, 0.1], '70b_lora_scierc_R_F1_delta_pp': [-0.3, 0.3], '70b_lora_docred_DR_pct': [0, 0.2], '70b_lora_docred_R_F1_delta_pp': [-0.5, 0.5], 'hostile_reviewer_count': [0, 1]}\n叙事方向：原始 framing 完全成立——\"universal ontology-constrained structured generation framework\"。 Paper story: violation landscape (empirical contribution #1) → composable constraint compilation (methodological contribution #2) → RE 验证 (3 models × 2 datasets × ZS+FT) + EE 跨任务泛化 + 70B scale generalization。 Claims 无需降级。Title 保留 \"Type-Valid IE via Compiled Ontology Constraints\"。 CF 写入 §7 limitation + beam search mitigation 写入 §5.5，不影响 core claim。 Conference main 稳过。\n\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: schema_semantic_constrained_ie\nvenue: emnlp-2026\nfocus: 评估当前论文（含 70B ZS 跨两个数据集 + 即将到手的 70B LoRA 结果）能否达到 EMNLP 2026 Overall Assessment 4.0（Conference）。重点关注：novelty 感知（semantic constraint layer 是否被视为足够新颖）、evaluation scope（RE 为主 + preliminary EE 是否足够）、与 GCD/BoostCD/XGrammar 的差异化。\n\n## paper_framing.md\n\n# OntoCoDec — Paper Framing\n\n## Target Venue\nEMNLP 2026 (ARR submission May 25, 2026) — **目标: conference main**（D040, 用户明确指示）\n\n## Title\nOntoCoDec: Type-Valid Information Extraction via Compiled Ontology Constraints\n(D015: \"Near-Complete\" dropped — DocRED residual DR=10.21% (Qwen) 不算 near-complete。论文贡献是方法，不是特定消除率。SciERC 0.93% 和 DocRED 2.55% (Llama) 可在正文中描述为 near-complete，但 title 不宜 overclaim。)\n\n**D040 Story 升级方向**: 从 \"IE-specific constrained decoding\" → \"universal ontology-constrained structured generation framework\"。WikiEvents Event Extraction 验证跨任务泛化。Continuation masking v2 突破（10-doc: RoV 0%, semantic violations ↓95.8%）初步确认跨任务有效性，全量实验进行中。最终 title 待全量结果后调整。\n\n## Core Insight\nLLM-based IE systems produce systematic ontology constraint violations concentrated in specific relation types. Prompt-level intervention (schema-informed prompting) reduces violations by ~62% but cannot eliminate them — certain relation types retain 25-30% violation rates even with explicit constraint descriptions. OntoCoDec provides **near-complete elimination (DR 15.4%→0.93%, ↓94%) at zero or positive F1 impact** through automatic ontology-to-decoder constraint compilation with two complementary layers.\n\n**Phase 2 confirmed (D012 bootstrap CI, v2 fix)**: Grammar+Semantic dual-layer constrained decoding reduces domain/range violations by 94%, eliminates entity-type and relation-vocabulary violations entirely (→0%). F1 impact is **dataset-dependent**:\n- SciERC: Rel F1 neutral (+0.13pp, p=0.58), Ent F1 neutral (-0.03pp, p=0.53)\n- DocRED: Rel F1 **significantly improved** (+0.50pp, p<0.001, 95% CI [+0.23, +0.81]); Ent F1 **significantly improved** (+1.23pp, p<0.001, 95% CI [+0.94, +1.55])\n- Mechanism: grammar 消除 OOV relation names (DocRED RV 29.66%→0.03%) + 非标 entity types (ET 2.48%→0%)。all_set F1 方法下 OOV=FP → fewer FP → higher precision/F1。SciERC baseline RV/ET 已很低，效果不显著。\n- **Grammar 层是 F1 提升的唯一来源**: grammar_only Ent F1=59.38% ≈ full_s1 59.37% (Δ+0.01pp, p=0.66)。Semantic 层对 F1 无额外贡献，专注 DR reduction。\n\n## Core Claims\n\n### Claim 1 (Empirical): Violation Landscape\nLLM-based IE systems violate ontology type constraints at non-trivial rates (15.4% per-triple on SciERC, 18.7% on DocRED). Violations are **not uniformly distributed** — they concentrate on relation types with tight domain/range constraints (Feature-of 33.5%, Compare 42.4%) while loose-constraint relations show near-zero violation (Used-for 0.8%).\n\n**Key insight**: Violation rate is driven by **constraint tightness**, not ontology size. A small ontology with tight constraints can produce more violations than a large ontology with loose constraints.\n\n**D014 修订**: DR reduction ceiling 由 **tightness × model RV baseline** 共同决定，非 tightness 单因素。Llama DocRED DR↓90.2% vs Qwen DR↓44.7%（同一 ontology τ̄=0.842）。机制：Qwen RV=29.66% >> Llama RV=16.03% → grammar 层将 OOV triples 强制匹配有效关系名 → 揭露大量 latent DR violations → 残余 DR 更高。这是比单一 tightness 更深的 insight。\n\n**Evidence**: SciERC (7 relations) 15.4%; DocRED (96 relations) 18.7% — comparable rates despite 14× ontology size difference. Schema-informed prompt on DocRED only achieves DR↓32% (vs SciERC ↓62%), confirming **prompt-level intervention scales poorly with ontology complexity**.\n\n### Claim 2 (Empirical): Prompt Insufficiency\nSchema-informed prompting (explicitly describing domain/range constraints in the prompt) reduces but does not eliminate violations:\n- Overall: 15.4% → 5.78% (-62.4%), still above 5%\n- Per-relation: Compare 42.4% → 27.6%, Evaluate-for 24.1% → 29.9% (**worse**)\n- Prompt intervention is unreliable at the per-relation level — some relations improve, one regresses\n\n**Narrative**: This is NOT about \"5.78% barely above 5%\". The story is: **prompt-level intervention is fundamentally unreliable as a guarantee mechanism**. It works statistically but cannot provide per-instance compliance. Three specific relation types retain >10% violation rates with schema-informed prompts. For safety-critical IE (biomedical, legal, regulatory), statistical reduction is insufficient — guaranteed compliance is required.\n\n### Claim 3 (Methodological): Composable Constraint Framework\nOntoCoDec automatically compiles IE ontology schemas into two composable constraint layers:\n1. **Grammar layer** (XGrammar): JSON structure + type vocabulary constraints (CFG-expressible)\n2. **Semantic layer** (TypeConstraintProcessor): Cross-field domain/range constraints via stateful entity registry + dynamic logit masking\n\nThe two layers are **complementary with enabling dependency**: grammar ensures every generated relation type is in the valid vocabulary, which enables the semantic layer to look up and enforce domain/range rules for that type. Without grammar, the semantic layer encounters unknown relation types and cannot enforce constraints (explaining why semantic_only achieves only ↓24% vs full_s1 ↓94%). This is NOT \"synergistic\" (mutual amplification) — grammar is a prerequisite for semantic, not vice versa.\n\nThe two layers compose via bitwise AND of token masks. Recommended framing: \"Grammar and semantic constraints compose via bitwise AND with an enabling dependency: grammar ensures structural validity, enabling semantic constraints to enforce domain/range rules. When constraint tightness creates empty intersection between layers, the system degrades gracefully to grammar-only constraints, maintaining structural validity as a guaranteed floor.\"\n\n**Graceful degradation + Fallback 频率量化** (D008 + Reviewer 发现):\nWhen $M_{semantic} \\cap M_{grammar} = \\emptyset$, the system falls back to grammar-only control.\n\n**关键量化数据（Reviewer 从日志挖掘）**:\n- Llama DocRED full_s1: **32,921 次 fallback / 577 docs = ~57 次/doc**\n- Llama SciERC full_s1: **5,882 次 fallback / 550 docs = ~10.7 次/doc**\n- DocRED fallback 频率是 SciERC 的 **5.3×**\n- Qwen DocRED fallback 率未知（日志当时无 fallback logging，需估算）\n\n**这直接解释了 DocRED DR 残余 10.19% vs SciERC 0.93%**: 更多 token 位置退化为 grammar-only → grammar-only 的 DR 已知为 26.17% → 高 fallback = 高残余 DR。\n\n**论文建议**: 在 §5 tightness 段报告 fallback 率，定义 \"Constraint Coverage\" 指标（semantic masking 实际生效的 token 比例）。这把 \"10.19% DR 残余\" 从弱点变成可量化分析的 finding。Frame as \"engineering robustness\" in §4; fallback 频率 + tightness 作为 §5 定量分析。\n\n**Decidability taxonomy**: Constraints classified by prefix-decidability:\n- (a) Purely local: entity type ∈ vocabulary (grammar layer)\n- (b) Prefix-decidable with state: relation argument types compatible with domain/range (semantic layer, requires entity registry)\n- (c) Truly non-local: forward coreference — out of scope for forward-only decoding\n\n### Claim 4 (Methodological): S1 vs S2 Decoding Strategies — Architectural Ablation\n- S1 (single-pass): Both layers applied throughout generation. **Recommended primary strategy** — simpler, slightly better metrics across the board.\n- S2 (two-pass): Pass 1 extracts entities (grammar-only), Pass 2 generates relations with input-dependent grammar compiled from Pass 1 entities.\n\n**S2 full results (551/551 SciERC)**: DR 0.97% (vs S1 0.93%), CF 8.03% (vs S1 9.9%), R-F1 8.03% (vs S1 8.36%). S2 does NOT solve CF — the 1.87pp reduction is not significant. S2 also slightly worse on DR and F1. **S2 is an architectural variant demonstrating framework flexibility, not a CF solution.** Position in paper as ablation (Section 5 or Appendix), not as a core contribution.\n\n⚠️ **Do NOT cite pilot50 DR=0% as S2 evidence** — small-sample artifact; full run shows DR=0.97%. Per-relation S2 DR is worse than S1 on Compare (4.6% vs 2.82%), Part-of (1.25% vs 0%), Used-for (0.12% vs 0%).\n\n### Claim 5 (Empirical): Cross-Task Generalization — Event Extraction (D040, NEW)\n**Status**: ✅ All 3 models × 246 docs complete (v3 with collision fix + exact-match fix)\n\nOntoCoDec generalizes beyond Relation Extraction to **Event Extraction** (WikiEvents, Li et al. NAACL 2021), demonstrating that the framework is task-agnostic for any IE task with ontology-defined type constraints.\n\n**Cross-task framing (Reviewer 评估 confirmed)**:\n- **RoV 是 DR 的正确对应物**（不是 RV）：EE 中 per-type violation rate 是 RE 的 3-5×，支持 \"more complex ontology → more critical constraint enforcement\" claim\n- **三层级联 Grammar→RoV→AC**（比 RE 的 Grammar→DR 两层更丰富）：grammar 消除 EV，使 semantic layer 可以 enforce role restriction (RoV→0%)，进而暴露 AC violations。这强化 architecture contribution 论证。\n- **Semantic layer 是 EE 的唯一防线**：grammar 层对 role vocabulary 无能力，只有 semantic layer + continuation masking 能 enforce per-event-type role constraints\n- **\"Practical value\" 防线**：Arg F1 ≈ 0% 不削弱 claim，因为 (a) mechanism generalization 是 contribution 不是 SOTA performance，(b) FT composability 已在 RE 中证明 high-F1 场景有效\n\n**WikiEvents specifics** (DARPA KAIROS ontology):\n- 56 event types × 80 argument roles × 27 entity types（含 5 个补充 Contact 子类型 + CRM entity type）\n- 245 组显式 (event_type, role) → allowed_entity_types 约束\n- Maps directly to OntoCoDec's semantic layer: argument role type constraints ≡ domain/range constraints\n- 27 entity types（比 ACE05 的 7 个更丰富）→ constraint space 更大，更能展示 semantic layer 价值\n- 99.98% 数据满足约束 → 约束定义是真实有效的\n- Hierarchical event names (e.g., Conflict.Attack.DetonateExplode) → 扁平化为 leaf-node 解决 first-token collision（96.1%→3.9%）\n\n**数据集选择理由**（MAVEN/RAMS 排除）：\n- MAVEN (168 types): 无 argument extraction，不适用\n- MAVEN-Arg (162 types): FrameNet-based，无 role→entity_type schema 约束\n- RAMS (139 types): 仅 cardinality 约束，无 entity type binding\n- ACE05 (33 types): LDC 付费，采购周期来不及\n- **WikiEvents 是唯一同时满足 \"免费 + 有显式 role→entity_type 约束\" 的数据集**\n\n**Violation 分类** (5 类，从 RE 的 4 类扩展):\n- ET (Entity Type): entity type 不在 ontology 合法类型列表中\n- EV (Event Vocabulary): event type 不在 ontology 定义中\n- RoV (Role Vocabulary): argument role 不在该 event type 定义中\n- AC (Argument Constraint): argument entity type 不满足 role→entity_type 约束（DR 的自然推广）\n- CF (Cross-Field): 同一 entity 跨 event 被赋予不同 type\n\n**Full results (246 docs, v3 final — collision fix + exact-match fix)**:\n\n| Metric | Qwen3-8B uncon. | Qwen3-8B Full S1 | Llama-3.1-8B uncon. | Llama-3.1-8B Full S1 | Mistral-7B uncon. | Mistral-7B Full S1 |\n|--------|-----------------|-------------------|---------------------|----------------------|-------------------|---------------------|\n| Parse | 88.6% | 83.7% | 91.9% | 84.1% | 88.6% | 88.6% |\n| EV | 24.0% | **0%** | 10.5% | **0%** | 37.3% | **0%** |\n| RoV | 74.9% | **0%** | 88.8% | **0%** | 63.9% | **0%** |\n| AC | 0.3% | 2.1% | 0.1% | 3.8% | 0% | 1.3% |\n| CF | 0% | 21.1% | 0% | 17.2% | 0% | 14.9% |\n| Trigger F1 | 11.8% | 13.4% | 5.7% | 7.5% | 2.4% | 3.9% |\n| Ent F1 | 0% | 14.1% | 0% | 17.6% | 0% | 11.7% |\n\n**Grammar-only ablation (Mistral v3, all 3 models)**:\n- Grammar eliminates EV→0% but RoV remains 64-77%: grammar CFG cannot constrain 80 argument roles conditioned on event context\n- AC rises to 8-14% under grammar-only (latent violation surfacing pattern, same as DocRED RE)\n- Proves semantic layer is essential for EE: two-layer architecture is necessary, not just convenient\n\n**Post-hoc filtering comparison (devastating)**:\n- Qwen: 5,467→23 arguments (99.6% discarded) to reach 0% violation\n- Llama: 5,053→3 arguments (99.9% discarded)\n- Mistral: 6,034→0 arguments (100% discarded)\n- Post-hoc is not viable for EE (contrasts with RE where it's expensive but functional)\n\n**BPE collision diagnostic (confirmed 2026-05-18)**:\n- Qwen (BPE, ~152K vocab): **0 collision groups** — all 27 entity types have unique first tokens\n- Llama (BPE, ~128K vocab): **0 collision groups** — same\n- Mistral (SentencePiece, ~32K vocab): **2 collision groups** (SID/SEN/SIDE→'S', BAL/BOD→'B')\n- **Residual AC narrative**: Mistral AC 1.3% = residual after collision fix (was 16.6%); Qwen/Llama AC 2.1-3.8% = purely model semantic confusion (confuses similar entity types like SID vs SEN), NOT tokenizer collision\n\n**关键 findings**:\n- RoV 是压倒性违规（64-89%），远超 RE 的 RV（1-30%）→ 更强力展示 constraint 需求\n- EV 显著（10-37%）→ grammar 层直接消除\n- **Entity F1 从 0% 恢复到 11.7-17.6%**: 不是语义改进，是 format compliance 恢复——grammar enforcement 产生 schema-valid JSON，parser 才能识别 entity mentions\n- Trigger F1 +1.5 to +1.8pp: elimination of OOV event types counted as FP\n- CF 15-21% 比 RE 更高（EE argument structure 更复杂），沿用 RE 的 CF tradeoff framing\n\n**Story upgrade**: WikiEvents results confirm paper narrative: \"universal ontology-constrained structured generation framework applicable to any IE task with formal type constraints\". Three evidence lines: (1) EV/RoV→0% across all models, (2) grammar-only ablation proves two-layer necessity, (3) post-hoc filtering is non-viable for EE. This is the key differentiator for conference main vs Findings.\n\n**70B scale experiment** (P029-P030, in progress): Qwen3-70B AWQ-INT4 on SciERC + DocRED to demonstrate scale generalization. If successful, adds a 4th model to cross-model evidence, strengthening C5.\n\n**Remaining risk**:\n- CF 15-21% higher than RE → continues CF tradeoff framing\n- 70B experiment timeline tight (need results by May 20 for paper integration)\n\n## Anticipated Reviewer Concerns\n\n### C1: \"5.78% is barely above 5% — threshold is arbitrary\"\n**Response**: Don't argue about the threshold. Argue about per-relation distribution: Compare (27.6%), Evaluate-for (29.9%), Feature-of (11.3%) have double-digit violation rates with schema-informed prompt. The value proposition is per-relation guaranteed compliance, not overall statistical rate.\n\n### C2: \"Why not just post-hoc filter?\"\n**Response (D013, 实验结果已出)**:\n\nPost-hoc filtering 实验结果：post-hoc F1 > OntoCoDec F1（SciERC 8.63 vs 8.36, DocRED 9.61 vs 8.24）——因 low F1 regime 下移除 FP 大幅提升 precision。\n\n**论文 framing（不以 F1 论高低，多维对比）**:\n1. **Recall 维度（核心论点）**: OntoCoDec recall 上升 (SciERC +0.20pp, DocRED +0.56pp) = 概率质量重分配到合法 token 生效。Post-hoc recall 下降 (SciERC -0.72pp, DocRED -1.06pp) = 正确 triple 被误删。\n2. **Information coverage**: DocRED post-hoc 丢弃 **48.1%** triples（近半数信息丢失），SciERC 16.8%。OntoCoDec 保留全部 triple slots。\n3. **Operational**: OntoCoDec 产出即合规、无需后处理、支持流式。Post-hoc 需额外管线、不适用实时场景。\n4. **Precision trade-off（诚实承认）**: \"Post-hoc achieves higher precision by removing a large fraction of triples, many of which are incorrect. This trades information coverage for precision — valid when FP are costly, but inadequate when completeness matters.\"\n\n数据表：SciERC post-hoc rejection 16.8%, OntoCoDec recall 11.60 vs post-hoc 10.68; DocRED post-hoc rejection 48.1%, OntoCoDec recall 10.02 vs post-hoc 8.40。\n\n**Reviewer 补充发现（D013 后）**:\n5. **ET 残余**：post-hoc 只删 triples 不改 entity list，残余 ET=0.4% (SciERC) / 2.47% (DocRED)。OntoCoDec ET=0%。Post-hoc 无法解决 entity type 违规。\n6. **127 个被删 TP (DocRED)**：过滤前 TP=1137，过滤后 TP=1010。丢失的 127 个 TP（11.2%）是正确提取但 entity type 违规的 triple。OntoCoDec 通过生成时强制合法 type 保留这些 TP——\"prevent vs detect\" 核心论据的具体数据。\n7. **OntoCoDec+post-hoc 组合**（future work idea）：先 constrain 再 filter 残余 DR。低优先级，May 19 前不做。\n\n### C3: \"Bitwise AND of two masks is not novel\"\n**Response**: The novelty is not the AND operation — it's (a) the automatic compilation from ontology definitions (zero-code schema compliance), (b) the stateful entity registry enabling cross-field constraints during autoregressive generation, (c) the decidability taxonomy providing theoretical guidance, and (d) the systematic violation landscape measurement motivating the approach.\n\n### C4: \"Evaluate-for violation rate increases with schema-informed prompt\"\n**Response (prior-constraint conflict framework)**: Evaluate-for has 23/36 valid pairs; Method→Task is invalid for Evaluate-for but natural in the LLM's distributional prior (\"Method X evaluates for Task Y\" is semantically plausible). Schema-informed prompting creates a **prior-constraint conflict**: the model learns to avoid Method→Task for Evaluate-for (reducing count 133→87, -34.6%), but the remaining instances are harder boundary cases where the model's type assignment strategy becomes less stable. This is not just \"harder instances\" — it's an active interference between prompt-level constraint signals and the model's learned type associations.\n\n**This strengthens the paper's claim**: prompt-level intervention is not merely insufficient but potentially **counterproductive** for specific constraint configurations. Decoding-time enforcement avoids this issue entirely — it operates on logits, not on the model's reasoning process, so there is no prior-constraint conflict.\n\n### C5: \"Only tested on one model (Qwen3-8B)\"\n**Response**: Cross-model validation DONE (D016 bootstrap verified). Llama-3.1-8B 零代码修改：\n- SciERC: DR 13.34%→0.08% (↓99.4%), R-F1 -0.14pp (p=0.011, negligible), E-F1 NS\n- DocRED: DR 26.07%→2.55% (↓90.2%), R-F1 +0.29pp (p=0.013, significant), E-F1 -0.64pp (p=0.022, modest decline)\n- Parse failures: unconstrained 68 vs full_s1 91 (6.8% vs 9.1%)\n\n**Cross-model claim 指导（Reviewer 专项评估）**:\n- ✅ 可声明：\"OntoCoDec generalizes across model families without code modification\"（程序性事实，铁证）\n- ❌ 不可声明：\"consistently achieves the same reduction rate\"（仅 2 模型，不足以量化声明）\n- **RV↓DR↑ 正交性 finding**: Llama RV baseline 低(16%) 但 DR baseline 高(26%)，反向于 Qwen。证明两层约束解决正交 failure modes——vocabulary compliance ≠ semantic compliance。应作为 §5 cross-model 独立 finding 展开。\n- **Parse failure 偏差**: checker skip parse failures (不计入 F1)，Llama 68/998=6.8% vs Qwen 12/998=1.2%。偏差方向保守（不利于 constrained），不威胁 claim。但需 footnote 披露 + cross-model 表增加 parse failure rate 行。\n- **Llama SciERC CF=6.56%**: 比 Qwen 同量级更高，non-local constraint 问题在 Llama 上更突出，limitations 提及。\n- 等 llama_docred_full_s1 出来后定最终 claim 措辞。\n\n### C6: \"Constrained decoding degrades generation quality (CRANE, Structure Snowballing)\"\n**Response**: OntoCoDec's semantic constraints are narrower than full grammar constraints — only type tokens are masked, free text is unconstrained. **Bootstrap CI (10000×, D012 Qwen + D016 Llama, all registry-aligned)**:\n\n**Qwen3-8B**: SciERC R-F1 +0.13pp (p=0.58, NS), E-F1 -0.03pp (NS). DocRED R-F1 +0.50pp (p<0.001), E-F1 +1.23pp (p<0.001).\n**Llama-3.1-8B**: SciERC R-F1 -0.14pp (p=0.011, negligible), E-F1 NS. DocRED R-F1 +0.29pp (p=0.013), E-F1 -0.64pp (p=0.022).\n\n**Cross-model pattern**: DocRED R-F1 显著提升（两个模型）。E-F1 model-dependent（Qwen +1.23pp, Llama -0.64pp）。\n- 机制：grammar 消除 OOV relation names + 非标 entity types → all_set 方法下减少 FP → precision 提升。Grammar 是 F1 提升的唯一来源（grammar_only Ent F1=59.38% ≈ full_s1 59.37%, Δ=0.01pp, p=0.66）。Semantic 层对 F1 无额外贡献。\n- Frame as: \"On DocRED, R-F1 gains are significant for both models. Entity F1 impact is model-dependent.\"\n- 不升级为 core claim，但如实报告。\n\n### C7: \"Your method trades DR violations for CF violations (cross-field consistency)\"\n**Response**: Both S1 and S2 show elevated CF (per-triple rate ~8-10%). This is an inherent limitation of per-relation independent type enforcement. Must be proactively reported as a limitation. Defense:\n\n**CF 子类型分析（根因已确认）**：\n- **EVR（entity-vs-relation type drift）**: 占 CF 的 >90%。同一 entity 在 entity list 和 relation triple 中被赋予不同 type。S1: 245 entities (7.34%), S2: 178 entities (5.54%, -27%)\n- **Within-rel（同 entity 跨 relation type 不一致）**: S1: 10 (0.36%), S2: 18 (0.72%)\n- S2 减少 EVR 但增加 within-rel——trade-off 更复杂，不是单纯好/差\n\n**Top 冲突模式**: Generic↔OtherScientificTerm (60次), Material↔OtherScientificTerm (28次), Material↔Method (20次)。**这些是 SciERC type system 固有的语义边界模糊区**——同一术语在不同学术语境下确实可以被合理归类为不同 type。CF 在相当程度上是 type system 模糊性的体现，非纯粹的方法缺陷。\n\n**论证层次**：\n1. DR violations = structurally invalid triples（下游系统不可用）→ hard constraint\n2. CF violations = same entity gets different types across relations → individual triples remain type-valid, only cross-triple consistency broken → soft preference\n3. CF 的根因是 type system 语义边界模糊 + per-relation 独立 enforcement，非 bug\n4. Future work: cross-relation global consistency pass (entity-level type consensus before relation-specific enforcement)\n\n**机制归因（口径对账确认）**：grammar_only CF=0.08%（与 unconstrained 持平），full_s1 CF=9.90%，full_s2 CF=8.03%。**CF 100% 由 semantic 层引入，grammar 层无贡献。** 这为 \"CF 是 semantic type enforcement 的系统性副作用\" 提供干净的消融证据。\n\n**论文数字口径**：CF rate 用 violation_checker 口径（denominator=total_entities，与 DR/RV/ET 一致）。分析段落额外给 entity-level EVR 率 + 受影响样本比例。注意：analyze_cf 脚本的 EVR/WR 两维度不是独立的（WR⊂EVR），论文中不要作为两个独立维度报告。\n\n**Do NOT hide this data.** Proactive disclosure + severity distinction + root cause analysis + type ambiguity evidence + 消融归因 = 最强防御策略。\n\n### C8: \"Absolute F1 is too low (~8%) — results are not meaningful\"\n**Response**: This is a zero-shot extraction setting (no training data, no fine-tuning). Low F1 is expected — supervised SOTA on SciERC relation F1 is ~40-50%. Our contribution is the constraint enforcement method, not extraction quality. F1 is a control variable verifying constraints don't degrade quality, not an optimization target. Recommended framing: \"We evaluate in a zero-shot setting to demonstrate that our constraint enforcement method works without task-specific training. F1 is reported to verify that constraint enforcement does not degrade extraction quality, not as a claim of state-of-the-art performance.\"\n\n## Paper Structure (Draft — D040 updated)\n1. Introduction: Ontology constraint violations in LLM-based structured generation + composable framework overview (story: not just RE, general ontology-constrained generation)\n2. Background: Grammar-constrained decoding (XGrammar) + IE ontology structure\n3. Violation Landscape Study (Phase 0 empirics — independent contribution)\n4. OntoCoDec Framework: Compiler + TypeConstraintProcessor + S1/S2 strategies\n5. Experiments:\n   - §5.1-5.3: RE experiments (SciERC + DocRED, 3 models, constrained vs unconstrained vs post-hoc vs prompt-based)\n   - §5.4: **Event Extraction (WikiEvents)** — cross-task generalization (D040)\n   - §5.5: Ablation + analysis (composability, latency, beam search, etc.)\n6. Related Work: 5 constraint paradigms (grammar, vocabulary, structural, type-checking, ontology) + event extraction methods\n7. Conclusion: Framework generality across IE tasks\n\n## Claim Calibration (per Reviewer assessment)\n\n**Safe to claim (sufficient evidence from Phase 2)**:\n- \"First systematic study of ontology constraint violations in LLM-based IE\"\n- \"Violation rate correlates with constraint tightness, not ontology size\" (D014: DR reduction ceiling 由 tightness × model RV baseline 共同决定)\n- \"Grammar+semantic constrained decoding eliminates 94% of DR violations at zero F1 cost\" ✅ Phase 2 confirmed\n- \"Two-layer architecture provides complementary coverage — grammar enables semantic\" ✅ Ablation confirmed\n- \"Prompt-level intervention scales poorly with ontology complexity\" ✅ SciERC ↓62% vs DocRED ↓32%\n\n**Claim with caution**:\n- \"Near-complete type-valid IE\" — S1 0.93%, S2 0.97% residual, not truly 0%. Title updated to \"Near-Complete\"\n- \"Principled framework applicable to arbitrary IE ontologies\" — RE validated on 2 datasets × 2 models; EE (WikiEvents) 10-doc preliminary shows ↓95.8% semantic violations, full results pending\n- \"F1 improvement\" — SciERC: not significant (p=0.58), frame as F1-neutral; DocRED: significant (+0.50pp, p<0.001), 可报告但不升级为 core claim，归因于 OOV elimination 而非约束解码本身的提升\n- \"CF reveals type system ambiguity\" — 可在 §5.3 作为 analysis finding 展开（Generic↔OtherScientificTerm 等模式有独立 insight 价值），但 §7 必须同时保留 CF 作为 limitation + future work。**两处都要有，缺一不可。** 不能暗示\"因为是 type ambiguity 所以 CF 可接受\"\n\n**Do NOT claim**:\n- \"General infrastructure for IE\" — only zero-shot extraction validated\n- \"State-of-the-art\" — F1 is control variable, not optimization target (see C8)\n- \"Synergistic effect\" — mechanism is enabling dependency, not mutual amplification (see Claim 3)\n- \"S2 solves CF\" or \"S2 mitigates Structure Snowballing\" — data shows S2 ≈ S1 on all metrics; position as architectural variant only\n- \"Pilot50 DR=0%\" — small-sample artifact, full S2 has DR=0.97%\n- \"Grammar-first invariant\" 作为独立 claim — 证据不足（仅 1 次崩溃触发，实现是 fallback 非形式化保证）。写入 §4 方法论设计原则（1-2 句），不升级为 claim\n- \"Robust dual-layer composition across schema complexities\" — 等 DocRED 完成。最终如 fallback ≤5/998，可写经验性陈述，不做泛化 claim\n\n## Risk Ranking (ordered by reject probability)\n\n1. **CF violation trade-off under-addressed** (MEDIUM-HIGH): S1 9.9%, S2 8.03% — both elevated. **S2 confirmed: does NOT solve CF.** This is the #1 attack surface. Mitigated by proactive disclosure + severity distinction + root cause analysis (C7). Must be reported as explicit limitation with future work direction (global entity-type consensus).\n2. ~~**Single model limitation**~~ (RESOLVED): Llama-3.1-8B SciERC ✅ (DR↓99.4%) + DocRED ✅ (DR↓90.2%). 2 模型 × 2 数据集全矩阵完成。\n3. **Novelty perception** (MEDIUM): \"PLDI'25 for code → OntoCoDec for IE\" attack line. Must argue IE constraint structure differs fundamentally.\n4. ~~**DocRED Phase 2 weak**~~ (RESOLVED → reframed as D014): Qwen DR↓44.7%, Llama DR↓90.2% — both substantial. Weaker Qwen reduction explained by RV baseline interaction (D014), not method failure.\n5. ~~**Phase 2 F1 drop**~~ (RESOLVED): F1 confirmed neutral (SciERC) or positive (DocRED, p<0.001). Bootstrap CI D012 confirms. No longer a risk.\n\n## Critical Path to EMNLP Submission (May 25)\n\n- **May 13-14**: Phase 0 + Phase 1 + Phase 2 SciERC ✅\n- **May 14**: Phase 2 DocRED 4-way ablation ✅ + Llama SciERC cross-model ✅ + Dream 完成 (3/6)\n- **May 14-15**: Llama DocRED ✅ + Checker 修正 ✅ + post-hoc ✅ + bootstrap CI ✅ + related work ✅\n- **May 15-17**: Prompt sensitivity ✅ + WikiEvents pipeline 开发 + continuation v2 突破\n- **May 17-18**: WikiEvents 3 模型 unconstrained baselines (进行中) + constrained 全量\n- **May 18-19**: WikiEvents 结果分析 + §5.4 Event Extraction 章节撰写\n- **May 19-20**: Intro/Abstract/Conclusion 升级（cross-task story）+ 内部稿 → submit_paper_to_review\n- **May 20-24**: Review 修改 + 最终提交\n\n**当前瓶颈**: WikiEvents 全量实验完成是关键路径。3 模型 unconstrained baselines 并行进行中（Qwen ~68/246, Mistral ~31/246, Llama 重启中），constrained 实验随后立即启动。\n\n## Status\n- Phase 0 SciERC: ✅ Complete (minimal + schema-informed)\n- Phase 0 DocRED: ✅ Complete (minimal 18.7% DR + schema-informed 12.8% DR)\n- Phase 1 Compiler: ✅ Complete (grammar + semantic layers integrated)\n- Phase 2 SciERC (5 configs): ✅ Complete (S1 DR↓94% F1-neutral, S2 降级为 ablation)\n- Phase 2 DocRED (4 configs): ✅ Complete (full_s1 DR↓45%, grammar ET/RV→0%)\n- Llama SciERC cross-model: ✅ Complete (DR↓99.4%, F1-neutral, 零代码修改)\n- Llama DocRED cross-model: ✅ Complete (full_s1 DR↓90.2%, unconstrained DR=26.07%)\n- Checker v2 (D011): ✅ Fixed (ET triple-counting → unique entity dedup)\n- Bootstrap CI (D012): ✅ Fixed + confirmed (entity filter bug resolved)\n- Post-hoc baseline (D013): ✅ Complete (multi-dimensional framing)\n- Related work: ✅ 42 bib entries, 4 additions merged\n- Dream 6/6 actions: ✅ All complete\n- CF violation analysis: ✅ Confirmed inherent limitation (S1 9.9% SciERC / 2.57% DocRED / 12.02% Llama DocRED)\n- D014 tightness revision: ✅ Complete (tightness × RV baseline dual-factor)\n- Llama bootstrap CI (D016): ✅ Fixed + verified (registry-aligned ≤0.05pp, all p-values in paper)\n- Paper compilation: ✅ 8 pages正文 + appendix\n- R5 text fixes (N1/N2/N3/W1-W6): ✅ All complete and verified\n- Prompt sensitivity analysis: ✅ Complete (3 prompts × 2 modes, DR reduction 94.0-94.6%, σ=0.3pp; appendix written)\n- Doc length breakdown: ✅ Complete (appendix written)\n- **WikiEvents Event Extraction (D040)**: 🔄 Continuation v2 突破 (10-doc: RoV 0%, semantic ↓95.8%); 3 模型 unconstrained baselines 进行中; constrained 全量待启动\n\n\n## registry (completed experiments)\n\n- exp_id: mvp_phase0_violation_rate\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_triples: 1724\n    total_entities: 2474\n    json_parse_rate: 1\n    entity_type_violation_rate: 0.004\n    relation_vocabulary_violation_rate: 0.0139\n    domain_range_violation_rate: 0.1537\n    cross_field_consistency_violation_rate: 0.0008\n    go_nogo_metric: 0.1537\n    entity_f1: 0.3101\n    relation_f1: 0.0823\n    per_relation:\n      Used-for:\n        total: 787\n        dr_violations: 6\n        rate: 0.0076\n      Conjunction:\n        total: 32\n        dr_violations: 0\n        rate: 0\n      Hyponym-of:\n        total: 124\n        dr_violations: 18\n        rate: 0.1452\n      Evaluate-for:\n        total: 133\n        dr_violations: 32\n        rate: 0.2406\n      Part-of:\n        total: 72\n        dr_violations: 18\n        rate: 0.25\n      Feature-of:\n        total: 486\n        dr_violations: 163\n        rate: 0.3354\n      Compare:\n        total: 66\n        dr_violations: 28\n        rate: 0.4242\n- exp_id: mvp_phase0_violation_rate_docred\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_docs: 998\n    parsed_docs: 962\n    json_parse_rate: 0.964\n    total_entities: 19099\n    total_triples: 16540\n    entity_type_violation_rate: 0.075\n    relation_vocabulary_violation_rate: 0.289\n    domain_range_violation_rate: 0.187\n    cross_field_consistency_violation_rate: 0.0008\n    go_nogo_metric: 0.187\n    fuzzy_matches: 126\n    top_dr_violations_by_rate:\n      P35_head_of_state: 1\n      P710_participant: 0.919\n      P172_ethnic_group: 0.875\n    top_dr_violations_by_count:\n      P31_instance_of:\n        violations: 322\n        total: 533\n        rate: 0.604\n      P1001_applies_to_jurisdiction:\n        violations: 264\n        total: 594\n        rate: 0.444\n      P1344_participant_in:\n        violations: 194\n        total: 312\n        rate: 0.622\n- exp_id: mvp_phase0_scierc_schema\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    domain_range_violation_rate: 0.0578\n    relation_vocabulary_violation_rate: 0.003\n    entity_type_violation_rate: 0\n    total_violation_rate: 0.0253\n    go_nogo_metric: 0.0578\n    total_triples: 1661\n    vs_minimal_dr_reduction: -0.624\n    per_relation:\n      Used-for:\n        rate: TBD\n      Feature-of:\n        delta_pp: -22.3\n      Part-of:\n        delta_pp: -22.5\n      Compare:\n        delta_pp: -14.8\n      Evaluate-for:\n        delta_pp: 5.8\n    mcnemar_all_significant: true\n- exp_id: mvp_phase0_docred_schema\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_documents: 998\n    documents_checked: 943\n    parse_failures: 55\n    json_parse_rate: 0.9449\n    total_entities: 19524\n    total_triples: 16782\n    entity_type_violations: 119\n    entity_type_violation_rate: 0.0061\n    relation_vocabulary_violations: 3090\n    relation_vocabulary_violation_rate: 0.1841\n    relation_fuzzy_matches: 85\n    domain_range_violations: 2154\n    domain_range_violation_rate: 0.1284\n    cross_field_consistency_violations: 29\n    cross_field_consistency_violation_rate: 0.0015\n    total_violations_any: 5392\n    total_violation_rate: 0.1485\n    go_nogo_metric_dr: 0.1284\n- exp_id: phase2_scierc_grammar_only\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_samples: 551\n    total_triples: 1725\n    total_entities: 2474\n    json_parse_rate: 1\n    entity_type_violation_rate: 0\n    relation_vocabulary_violation_rate: 0\n    domain_range_violation_rate: 0.1484\n    cross_field_consistency_violation_rate: 0.0008\n    entity_f1: 0.3098\n    entity_precision: 0.2598\n    entity_recall: 0.3837\n    relation_f1: 0.0823\n    relation_precision: 0.0643\n    relation_recall: 0.114\n    checker_version: fixed_20260514_v2 (strip + alias + unique_et)\n- exp_id: phase2_scierc_semantic_only\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_samples: 551\n    total_triples: 1726\n    total_entities: 2474\n    json_parse_rate: 1\n    entity_type_violation_rate: 0.004\n    relation_vocabulary_violation_rate: 0.0151\n    domain_range_violation_rate: 0.1165\n    cross_field_consistency_violation_rate: 0.0271\n    entity_f1: 0.3101\n    entity_precision: 0.2605\n    entity_recall: 0.3831\n    relation_f1: 0.0815\n    relation_precision: 0.0637\n    relation_recall: 0.1129\n    checker_version: fixed_20260514_v2 (strip + alias + unique_et)\n- exp_id: phase2_scierc_full_s1\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_samples: 551\n    total_triples: 1729\n    total_entities: 2474\n    json_parse_rate: 1\n    entity_type_violation_rate: 0\n    relation_vocabulary_violation_rate: 0\n    domain_range_violation_rate: 0.0093\n    cross_field_consistency_violation_rate: 0.099\n    entity_f1: 0.3098\n    entity_precision: 0.2598\n    entity_recall: 0.3837\n    relation_f1: 0.0836\n    relation_precision: 0.0654\n    relation_recall: 0.116\n    checker_version: fixed_20260514_v2 (strip + alias + unique_et)\n- exp_id: phase2_scierc_unconstrained\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    json_parse_rate: 1\n    entity_f1: 0.3101\n    entity_precision: 0.2605\n    entity_recall: 0.3831\n    relation_f1: 0.0823\n    relation_precision: 0.0644\n    relation_recall: 0.114\n    entity_type_violation_rate: 0.004\n    relation_vocabulary_violation_rate: 0.0139\n    domain_range_violation_rate: 0.1537\n    cross_field_consistency_violation_rate: 0.0008\n    total_triples: 1724\n    total_entities: 2474\n    total_samples: 551\n    checker_version: fixed_20260514_v2 (strip + alias + unique_et)\n- exp_id: phase2_s2_pilot50\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    domain_range_violation_rate: 0.0205\n    relation_vocabulary_violation_rate: 0\n    relation_f1: 0.1008\n    samples: 50\n    predicted_relations: 146\n    true_positives: 13\n    gold_relations: 112\n    entity_f1_approx: 0.29\n    note: 'DR 修正: 原值 0 来自 dryrun (n=25 triples)。实际 pilot50 DR=3/146=2.05% (来自 violation_report_s2_pilot50.json)。'\n- exp_id: mvp_phase0_docred_schema_r2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: phase2_scierc_full_s2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_samples: 551\n    total_triples: 1644\n    total_entities: 2228\n    json_parse_rate: 1\n    entity_type_violation_rate: 0\n    relation_vocabulary_violation_rate: 0\n    domain_range_violation_rate: 0.0097\n    cross_field_consistency_violation_rate: 0.0803\n    entity_precision: 0.2797\n    entity_recall: 0.3712\n    entity_f1: 0.319\n    relation_precision: 0.064\n    relation_recall: 0.1078\n    relation_f1: 0.0803\n    checker_version: fixed_20260514_v2 (strip + alias + unique_et)\n- exp_id: phase2_docred_grammar_only\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    documents_checked: 985\n    parse_failures: 13\n    total_entities: 20150\n    total_triples: 17341\n    entity_type_violation_rate: 0\n    relation_vocabulary_violation_rate: 0.0003\n    domain_range_violation_rate: 0.2617\n    cross_field_consistency_violation_rate: 0.0007\n    relation_f1: 8.31\n    relation_precision: 7.06\n    relation_recall: 10.12\n    entity_f1: 59.38\n    entity_precision: 58.47\n    entity_recall: 60.32\n    unrecognized_relations: 5\n    f1_method: all_set\n    checker_version: fixed_20260514_v2 (strip + alias + unique_et)\n- exp_id: phase2_docred_full_s1\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    documents_checked: 987\n    parse_failures: 11\n    total_entities: 20187\n    total_triples: 17341\n    entity_type_violation_rate: 0\n    relation_vocabulary_violation_rate: 0.0003\n    domain_range_violation_rate: 0.1021\n    cross_field_consistency_violation_rate: 0.0257\n    entity_f1: 59.37\n    entity_precision: 58.45\n    entity_recall: 59.63\n    relation_f1: 8.23\n    relation_precision: 6.99\n    relation_recall: 10.01\n    unrecognized_relations: 5\n    f1_method: all_set\n    checker_version: fixed_20260514_v2 (strip + alias + unique_et)\n- exp_id: phase2_docred_unconstrained\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    documents_checked: 986\n    parse_failures: 12\n    total_entities: 20171\n    total_triples: 17497\n    entity_type_violation_rate: 0.0248\n    relation_vocabulary_violation_rate: 0.2966\n    domain_range_violation_rate: 0.1846\n    cross_field_consistency_violation_rate: 0.001\n    entity_f1: 58.15\n    entity_precision: 57.26\n    entity_recall: 58.32\n    relation_f1: 7.74\n    relation_precision: 6.55\n    relation_recall: 9.46\n    unrecognized_relations: 5189\n    f1_method: all_set (includes OOV predictions in denominator)\n    checker_version: fixed_20260514_v2 (strip + alias + unique_et)\n    et_v1: 0.0818\n    et_fix_note: v1 triple-counted ET across entity_list + relation head/tail; v2\n      deduplicates by (text, normalized_type)\n- exp_id: phase2_docred_semantic_only\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    documents_checked: 987\n    parse_failures: 11\n    total_entities: 20185\n    total_triples: 17571\n    entity_type_violation_rate: 0.0422\n    relation_vocabulary_violation_rate: 0.2987\n    domain_range_violation_rate: 0.1384\n    cross_field_consistency_violation_rate: 0.0105\n    entity_f1: 57.81\n    entity_precision: 57.27\n    entity_recall: 58.37\n    relation_f1: 7.7\n    relation_precision: 6.54\n    relation_recall: 9.37\n    f1_method: all_set\n    checker_version: fixed_20260514_v2 (strip + alias + unique_et)\n    et_v1: 0.1044\n    et_fix_note: v1 triple-counted ET across entity_list + relation head/tail; v2\n      deduplicates by (text, normalized_type)\n- exp_id: llama_scierc_unconstrained\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    entity_type_violation_rate: 0\n    relation_vocab_violation_rate: 0.0055\n    domain_range_violation_rate: 0.1334\n    cross_field_consistency_violations: 6\n    entity_f1: 0.2356\n    entity_precision: 0.1983\n    entity_recall: 0.2902\n    relation_f1: 0.0268\n    relation_precision: 0.0236\n    relation_recall: 0.031\n    total_entities: 2451\n    total_relations: 1274\n    json_parse_failures: 1\n    samples: 551\n    checker_version: fixed_20260514_v2 (strip + alias + unique_et)\n- exp_id: llama_scierc_full_s1\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    samples: 550\n    entities_extracted: 2469\n    relations_extracted: 1315\n    domain_range_violation_rate: 0.0008\n    relation_vocab_violation_rate: 0\n    entity_type_violation_rate: 0\n    cross_field_consistency_violation_rate: 0.0656\n    total_violation_rate: 0.0431\n    entity_f1: 0.2349\n    entity_precision: 0.1972\n    entity_recall: 0.2902\n    relation_f1: 0.0254\n    relation_precision: 0.0221\n    relation_recall: 0.0298\n    checker_version: fixed_20260514_v2 (strip + alias + unique_et)\n- exp_id: llama_docred_unconstrained\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    checker_version: fixed_20260514_v2\n    f1_method: all_set\n    documents: 998\n    documents_checked: 930\n    parse_failures: 68\n    unique_entities: 11525\n    total_triples: 16437\n    dr_eligible_triples: 13789\n    ET_rate_pct: 0.13\n    RV_rate_pct: 16.03\n    DR_rate_pct: 26.07\n    CF_rate_pct: 0.17\n    entity_precision: 61.22\n    entity_recall: 51.02\n    entity_f1: 55.65\n    relation_precision: 5.22\n    relation_recall: 7\n    relation_f1: 5.98\n    fuzzy_relation_matches: 121\n- exp_id: llama_docred_full_s1\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    checker_version: fixed_20260514_v2 (strip + alias + unique_et)\n    f1_method: all_set\n    violations:\n      ET: 0\n      RV: 0\n      DR: 2.55\n      CF: 12.02\n    f1:\n      entity_f1: 55.01\n      entity_precision: 61.41\n      entity_recall: 49.82\n      relation_f1: 6.27\n      relation_precision: 5.49\n      relation_recall: 7.32\n    counts:\n      documents: 998\n      documents_checked: 907\n      parse_failures: 91\n      unique_entities: 11296\n      triples: 16368\n- exp_id: posthoc_filtering_baseline\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    docred_f1_before: 7.74\n    docred_f1_after: 9.61\n    docred_precision_before: 6.55\n    docred_precision_after: 11.22\n    docred_recall_before: 9.46\n    docred_recall_after: 8.4\n    docred_rejection_rate: 0.481\n    docred_tp_before: 1137\n    docred_tp_after: 1010\n    docred_tp_lost: 127\n    docred_et_residual: 0.0247\n    scierc_f1_before: 8.23\n    scierc_f1_after: 8.63\n    scierc_rejection_rate: 0.168\n    scierc_recall_before: 11.4\n    scierc_recall_after: 10.68\n    scierc_tp_before: 111\n    scierc_tp_after: 104\n- exp_id: llama_docred_unconstrained_mt6144\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ET_rate: 0.13\n    RV_rate: 15.89\n    DR_rate: 26.18\n    DR_rate_eligible: 31.15\n    CF_rate: 0.17\n    entity_precision: 61.19\n    entity_recall: 51.06\n    entity_f1: 55.67\n    relation_precision: 5.18\n    relation_recall: 7\n    relation_f1: 5.95\n    parse_failures: 67\n    documents_checked: 931\n    total_documents: 998\n    unique_entities: 11534\n    total_triples: 16584\n    dr_eligible_triples: 13936\n    fuzzy_relation_matches: 121\n- exp_id: llama_docred_full_s1_mt6144\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    DR_rate_pct: 2.57\n    RV_rate_pct: 0\n    ET_rate_pct: 0\n    CF_rate_pct: 12.13\n    R_F1: 6.25\n    R_precision: 5.45\n    R_recall: 7.32\n    E_F1: 55.04\n    E_precision: 61.41\n    E_recall: 49.87\n    documents_total: 998\n    documents_checked: 908\n    parse_failures: 90\n    triples: 16471\n    unique_entities: 11307\n    fallback_events: 67911\n    wall_clock_seconds: 23926\n    vs_unconstrained_mt6144:\n      DR_delta_pp: -23.61\n      DR_reduction_pct: -90.2\n      R_F1_delta_pp: 0.3\n      E_F1_delta_pp: -0.63\n    vs_full_s1_mt4096:\n      DR_delta_pp: 0.02\n      R_F1_delta_pp: -0.02\n      E_F1_delta_pp: 0.03\n      CF_delta_pp: 0.11\n      parse_fail_delta: -1\n- exp_id: w1_cf_fallback_scierc_pilot\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    ET: 0\n    RV: 0\n    DR: 0.1478\n    CF: 0.0004\n    R_F1: 0.0823\n    R_P: 0.0643\n    R_R: 0.114\n    E_F1: 0.3098\n    E_P: 0.2598\n    E_R: 0.3837\n    entities: 2474\n    relations: 1725\n    samples: 551\n    grammar_first_fallback_rate: 0.3664\n    cf_registry_fallback_rate: 0.0448\n    total_mask_calls: 17024\n    violation_budget_DR_CF: 0.1482\n- exp_id: w1_cf_fallback_docred\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: w1_cf_fallback_llama_scierc\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: w1_cf_fallback_llama_docred\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: w5_lora_scierc_training\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 0.0634\n    eval_loss: 0.0586\n    eval_token_accuracy: 0.9816\n    eval_entropy: 0.9635\n    train_runtime_sec: 688.4\n    epochs: 3\n    checkpoint_path: /root/schema_semantic_constrained_ie/checkpoints/qwen3_8b_lora_scierc\n    merged_model_path: /root/schema_semantic_constrained_ie/checkpoints/qwen3_8b_lora_scierc_merged\n- exp_id: w5_lora_scierc_unconstrained_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    json_parse_rate: 1\n    entity_type_violation_rate: 0\n    relation_vocabulary_violation_rate: 0\n    domain_range_violation_rate: 0.0195\n    cross_field_consistency_violation_rate: 0\n    entity_f1: 0.6705\n    entity_precision: 0.6523\n    entity_recall: 0.6898\n    relation_f1: 0.4386\n    relation_precision: 0.4087\n    relation_recall: 0.4733\n    total_entities: 1784\n    total_relations: 1128\n    domain_range_violations: 22\n    go_nogo_metric: 0.0195\n    dr_gate: FAILED\n- exp_id: w5_lora_scierc_constrained_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    json_parse_rate: 1\n    entity_type_violation_rate: 0\n    relation_vocabulary_violation_rate: 0\n    domain_range_violation_rate: 0\n    cross_field_consistency_violation_rate: 0.0118\n    entity_f1: 0.6705\n    entity_precision: 0.6523\n    entity_recall: 0.6898\n    relation_f1: 0.4377\n    relation_precision: 0.4078\n    relation_recall: 0.4723\n    total_entities: 1784\n    total_relations: 1128\n    total_samples: 551\n    cross_field_consistency_violations: 21\n- exp_id: w5_llama_lora_scierc_training\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    eval_loss: 0.0595\n    eval_mean_token_accuracy: 0.9817\n    eval_entropy: 1.0565\n    train_loss: 0.0501\n    train_runtime_sec: 654.23\n    epochs: 3\n    train_samples_per_second: 8.08\n- exp_id: w5_llama_lora_scierc_unconstrained_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_samples: 551\n    total_entities: 1757\n    total_relations: 1082\n    json_parse_rate: 1\n    entity_type_violation_rate: 0\n    relation_vocabulary_violation_rate: 0\n    domain_range_violation_rate: 0.0111\n    cross_field_consistency_violation_rate: 0\n    total_violation_rate: 0.0042\n    entity_precision: 0.6647\n    entity_recall: 0.691\n    entity_f1: 0.6776\n    relation_precision: 0.432\n    relation_recall: 0.4795\n    relation_f1: 0.4545\n- exp_id: w5_llama_lora_scierc_constrained_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    domain_range_violation_rate: 0.0009\n    relation_vocabulary_violation_rate: 0\n    entity_type_violation_rate: 0\n    cross_field_consistency_violation_rate: 0.0046\n    relation_f1: 0.4547\n    relation_precision: 0.432\n    relation_recall: 0.4795\n    entity_f1: 0.6776\n    entity_precision: 0.6647\n    entity_recall: 0.691\n    total_relations: 1081\n    total_entities: 1757\n    total_samples: 551\n    parse_failures: 0\n- exp_id: w5_qwen_docred_lora_training\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    eval_loss: 0.0614\n    eval_mean_token_accuracy: 0.9804\n    eval_entropy: 0.715\n    train_loss: 0.0682\n    train_runtime_s: 5825.6\n    epochs: 3\n    adapter_path: /root/schema_semantic_constrained_ie/checkpoints/qwen_lora_docred\n    merged_path: /root/autodl-tmp/checkpoints/qwen_lora_docred_merged\n- exp_id: w5_docred_sft_data_gen\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_samples: 3053\n    dev_samples: 998\n    train_entities: 59493\n    train_relations: 38180\n    dev_entities: 19528\n    dev_relations: 12275\n- exp_id: w5_llama_docred_sft_data_gen\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_samples: 3053\n    dev_samples: 998\n    train_size_mb: 19\n    dev_size_mb: 6.1\n- exp_id: w5_llama_docred_lora_training\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 0.0572\n    eval_loss: 0.0624\n    token_acc: 98.06\n- exp_id: w5_llama_docred_lora_unconstrained_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ET_pct: 0\n    RV_pct: 0.15\n    DR_pct: 0.49\n    E_F1: 83.93\n    E_P: 84.93\n    E_R: 82.96\n    R_F1: 43.72\n    R_P: 38.59\n    R_R: 50.41\n    parse_fail_rate: 2.3\n    total_samples: 998\n    total_entities_pred: 19106\n    total_relations_pred: 16171\n- exp_id: w5_llama_docred_lora_constrained_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total: 998\n    parse_failures: 25\n    parse_fail_rate: 2.51\n    entities: 19077\n    relations: 16074\n    entity_f1: 83.94\n    entity_precision: 85\n    entity_recall: 84.13\n    relation_f1_all_set: 43.78\n    relation_precision_all_set: 38.79\n    relation_recall_all_set: 50.81\n    et_violations: 0\n    et_violation_rate: 0\n    rv_violations: 0\n    rv_violation_rate: 0\n    dr_violations: 33\n    dr_violation_rate: 0.21\n    CF_pct: 0.21\n    delta_vs_unconstrained:\n      delta_e_f1: 0.01\n      delta_r_f1: 0.06\n      delta_dr: -0.28\n      note: Authoritative values from eval_d064.py on w5_llama_docred_lora_constrained_eval.jsonl\n        (998 lines). Updated 2026-05-20.\n    provenance: eval_d064.py on westd-16980:/root/schema_semantic_constrained_ie/outputs/w5_llama_docred_lora_constrained_eval.jsonl,\n      2026-05-20. P/R corrected 2026-05-20 per Director.\n- exp_id: w5_qwen_docred_lora_unconstrained_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ET_pct: 0\n    RV_pct: 0.27\n    DR_pct: 0.76\n    CF_pct: 0.12\n    E_F1: 82.15\n    E_P: 85.44\n    E_R: 79.11\n    R_F1: 40.86\n    R_P: 36.41\n    R_R: 46.56\n    parse_fail_rate: 7.11\n    total_samples: 998\n    success_samples: 927\n    fail_samples: 71\n    total_entities_pred: 18091\n    total_relations_pred: 15870\n    ET_pct_excl_fail: 0\n    RV_pct_excl_fail: 0.27\n    DR_pct_excl_fail: 0.76\n    CF_pct_excl_fail: 0.12\n    E_F1_excl_fail: 85.72\n    E_P_excl_fail: 85.44\n    E_R_excl_fail: 86\n    R_F1_excl_fail: 42.2\n    R_P_excl_fail: 36.41\n    R_R_excl_fail: 50.17\n- exp_id: w5_qwen_docred_lora_constrained_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ET_pct: 0\n    RV_pct: 0\n    DR_pct: 0.01\n    CF_pct: 0.41\n    E_F1: 81.43\n    E_P: 85.41\n    E_R: 77.81\n    R_F1: 40.56\n    R_P: 36.35\n    R_R: 45.86\n    parse_fail_rate: 8.52\n    total_samples: 998\n    success_samples: 913\n    fail_samples: 85\n    total_entities_pred: 17799\n    total_relations_pred: 15563\n    E_F1_excl_fail: 85.69\n    R_F1_excl_fail: 42.23\n    delta_vs_unconstrained:\n      delta_DR: -0.75\n      delta_RV: -0.27\n      delta_R_F1: -0.3\n      delta_R_F1_excl_fail: 0.03\n      DR_reduction_pct: 98.7\n      note: 'Constrained - unconstrained. Unconstrained: DR=0.76%, R_F1=40.86, R_F1_excl_fail=42.20'\n- exp_id: w6_mistral_scierc_unconstrained\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    E_P: 0.2402\n    E_R: 0.3156\n    E_F1: 0.2728\n    R_P: 0.0295\n    R_R: 0.0483\n    R_F1: 0.0366\n    ET_pct: 1.5\n    RV_pct: 0\n    DR_pct: 56.94\n    CF_pct: 56.87\n    parse_fail_rate: 0\n    total_samples: 551\n    total_pred_entities: 2202\n    total_pred_relations: 1593\n- exp_id: w6_mistral_scierc_constrained\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    E_P: 0.2437\n    E_R: 0.3144\n    E_F1: 0.2746\n    R_P: 0.0292\n    R_R: 0.0493\n    R_F1: 0.0367\n    ET_pct: 0\n    RV_pct: 0\n    DR_pct: 13.4\n    CF_pct: 1.27\n    CF_count: 21\n    parse_fail_rate: 0\n    total_samples: 551\n    total_pred_entities: 2162\n    total_pred_relations: 1647\n    delta_vs_unconstrained:\n      delta_E_F1: 0.0018\n      delta_R_F1: 0.0001\n      delta_ET: -1.5\n      delta_RV: 0\n      delta_DR: -43.54\n      note: 'Constrained - unconstrained. Baseline: E_F1=0.2728, R_F1=0.0366, DR=56.94%,\n        ET=1.5%, RV=0%'\n- exp_id: w6_mistral_docred_unconstrained\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_samples: 998\n    parse_failures: 7\n    parse_fail_rate: 0.7\n    total_pred_entities: 12580\n    total_pred_relations: 11879\n    ET_pct: 7.58\n    RV_pct: 42.35\n    DR_pct: 57.42\n    CF_pct: 24.78\n    E_P: 0.6221\n    E_R: 0.3975\n    E_F1: 0.4851\n    R_P: 0.0447\n    R_R: 0.0432\n    R_F1: 0.0434\n    f1_method: fuzzy_normalized\n    f1_note: Relation matching uses case-insensitive normalization with token-overlap\n      >80% and edit-distance ≤2 fallback. Strict R_F1=3.50% (delta +0.84pp from 98\n      additional TPs via fuzzy matching of Mistral underscore/abbreviation variants).\n- exp_id: w6_mistral_docred_constrained\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ET_pct: 0\n    RV_pct: 0\n    DR_pct: 33.2\n    CF_pct: 0.19\n    E_P: 65.02\n    E_R: 41.4\n    E_F1: 50.59\n    R_P: 5.67\n    R_R: 5.37\n    R_F1: 5.52\n    parse_fail_rate: 0.8\n    total_samples: 998\n    total_pred_entities: 12535\n    total_pred_relations: 11554\n    delta_vs_unconstrained:\n      ET_pct: -7.58\n      RV_pct: -42.35\n      DR_pct: -24.22\n      CF_pct: -24.59\n      E_F1: 2.08\n      R_F1: 2.02\n- exp_id: w7_qwen_scierc_ft_grammar_only\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ET_pct: 0\n    RV_pct: 0\n    DR_pct: 1.9\n    CF_pct: 0\n    parse_fail_rate: 0\n    total_samples: 551\n    total_entities: 1784\n    total_relations: 1128\n    E_P: 0.6523\n    E_R: 0.6898\n    E_F1: 0.6705\n    R_P: 0.4087\n    R_R: 0.4733\n    R_F1: 0.4386\n    DR_violations: 22\n    tokenizer_warning: false_positive_transformers_4.57.6\n- exp_id: w7_qwen_scierc_ft_semantic_only\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ET_pct: 0\n    RV_pct: 0\n    DR_pct: 0.6\n    CF_count: 15\n    parse_fail_rate: 0\n    total_samples: 551\n    total_entities: 1784\n    total_relations: 1128\n    E_P: 0.6523\n    E_R: 0.6898\n    E_F1: 0.6705\n    R_P: 0.4073\n    R_R: 0.4713\n    R_F1: 0.4369\n    DR_violations: 7\n    delta_vs_grammar_only:\n      DR_delta: -1.3\n      note: semantic_only DR=0.6% vs grammar_only DR=1.9%, semantic layer reduces\n        DR by 68%\n    delta_vs_unconstrained:\n      DR_delta: -1.35\n      note: unconstrained DR=1.95% → semantic_only 0.6%\n- exp_id: w7_llama_scierc_ft_grammar_only\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_samples: 551\n    json_parse_failures: 0\n    total_entities: 1757\n    total_relations: 1082\n    entity_type_violation_rate: 0\n    relation_vocabulary_violation_rate: 0\n    domain_range_violation_rate: 0.0111\n    cross_field_consistency_violation_rate: 0\n    entity_f1:\n      precision: 0.6647\n      recall: 0.691\n      f1: 0.6776\n    relation_f1:\n      precision: 0.432\n      recall: 0.4795\n      f1: 0.4545\n- exp_id: w7_llama_scierc_ft_semantic_only\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ET_pct: 0\n    RV_pct: 0\n    DR_pct: 0.65\n    CF_count: 2\n    E_F1: 67.76\n    E_P: 66.47\n    E_R: 69.1\n    R_F1: 45.47\n    R_P: 43.24\n    R_R: 47.95\n    total_entities: 1757\n    total_relations: 1081\n    json_parse_failures: 0\n- exp_id: w8_ft_posthoc_baseline\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ft_regime:\n      qwen_scierc:\n        R_F1_before: 43.86\n        R_F1_posthoc: 43.94\n        R_F1_constrained: 43.77\n        reject_rate_pct: 1.95\n        TP_lost: 4\n      llama_scierc:\n        R_F1_before: 45.45\n        R_F1_posthoc: 45.23\n        R_F1_constrained: 45.47\n        reject_rate_pct: 1.11\n        TP_lost: 5\n      qwen_docred:\n        R_F1_before: 40.91\n        R_F1_posthoc: 41.11\n        R_F1_constrained: TBD\n        reject_rate_pct: 1.03\n        TP_lost: 1\n      llama_docred:\n        R_F1_before: 43.77\n        R_F1_posthoc: 43.92\n        R_F1_constrained: 44.23\n        reject_rate_pct: 0.64\n        TP_lost: 1\n    zs_regime:\n      mistral_scierc:\n        triples: 1584\n        reject_pct: 20.27\n        R_F1_before: 0.0376\n        R_F1_posthoc: 0.0394\n        R_F1_constrained: 0.0367\n        TP_before: 48\n        TP_after: 44\n        TP_lost: 4\n      qwen_scierc:\n        triples: 1724\n        reject_pct: 16.76\n        R_F1_before: 0.0823\n        R_F1_posthoc: 0.0863\n        R_F1_constrained: 0.0836\n        TP_before: 111\n        TP_after: 104\n        TP_lost: 7\n      llama_scierc:\n        triples: 1274\n        reject_pct: 13.89\n        R_F1_before: 0.0268\n        R_F1_posthoc: 0.0271\n        R_F1_constrained: 0.0254\n        TP_before: 30\n        TP_after: 28\n        TP_lost: 2\n      qwen_docred:\n        triples: 17497\n        reject_pct: 48.12\n        R_F1_before: 0.0774\n        R_F1_posthoc: 0.0961\n        R_F1_constrained: 0.0823\n        TP_before: 1137\n        TP_after: 1010\n        TP_lost: 127\n      llama_docred:\n        triples: 16437\n        reject_pct: 42.18\n        R_F1_before: 0.0598\n        R_F1_posthoc: 0.0744\n        R_F1_constrained: 0.0627\n        TP_before: 850\n        TP_after: 802\n        TP_lost: 48\n      mistral_docred:\n        triples: 11836\n        reject_pct: 73.73\n        R_F1_before: 0.0434\n        R_F1_posthoc: 0.0385\n        R_F1_constrained: 0.0552\n        TP_before: 518\n        TP_after: 292\n        TP_lost: 226\n        removed_RV: 4172\n        removed_ET: 3382\n        removed_DR: 1173\n        note: Only ZS case where posthoc HURTS R_F1 — 73.7% rejection rate loses 43.6%\n          of TPs\n    key_finding: 'ZS: post-hoc R_F1 >= constrained R_F1 in 5/6 groups. Exception:\n      Mistral DocRED where extreme rejection rate (73.7%) causes net F1 loss. Constrained\n      decoding value is in structural guarantee (0% violations) and composability,\n      not F1 preservation.'\n- exp_id: w8_llama_docred_ft_grammar_only\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    E_F1: 84.04\n    R_F1: 43.77\n    entity_precision: 84.99\n    entity_recall: 83.11\n    relation_precision: 38.6\n    relation_recall: 50.53\n    ET_pct: 0\n    RV_pct: 0\n    DR_pct: 0.51\n    CF_pct: 0.12\n    parse_fail_rate: 2.3\n    total_samples: 998\n    total_relations: 16199\n    unique_entities: 13225\n    parse_failures: 23\n- exp_id: w8_qwen_docred_ft_grammar_only\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    E_F1: 82.19\n    E_P: 85.47\n    E_R: 79.16\n    R_F1: 40.85\n    R_P: 36.27\n    R_R: 46.77\n    ET_pct: 0\n    RV_pct: 0\n    DR_pct: 0.61\n    CF_pct: 0.11\n    parse_fail_rate: 7.01\n    total_samples: 998\n    parse_failures: 70\n- exp_id: w8_qwen_docred_ft_semantic_only\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    E_F1: 82.15\n    E_P: 85.58\n    E_R: 78.99\n    R_F1: 40.89\n    R_P: 36.35\n    R_R: 46.73\n    ET_pct: 0\n    RV_pct: 0.23\n    DR_pct: 0.21\n    CF_pct: 0.27\n    parse_fail_rate: 7.52\n    total_samples: 998\n    parse_failures: 75\n    documents_checked: 923\n    total_entities: 18025\n    total_triples: 15909\n    DR_violations: 34\n    RV_violations: 37\n    ET_violations: 0\n    CF_violations: 49\n- exp_id: w8_llama_docred_ft_semantic_only\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    E_F1: 84.02\n    E_P: 85.01\n    E_R: 83.06\n    R_F1: 43.9\n    R_P: 38.89\n    R_R: 50.4\n    ET_pct: 0\n    RV_pct: 0.15\n    DR_pct: 0.3\n    CF_pct: 0.16\n    parse_fail_rate: 2.4\n    total_samples: 998\n    parse_failures: 24\n    documents_checked: 974\n    total_entities: 19099\n    total_relations: 16038\n    DR_violations: 48\n    RV_violations: 24\n    ET_violations: 0\n    CF_violations: 31\n- exp_id: w9_qwen_scierc_zs_sampling\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ET_pct: 0\n    RV_pct: 0\n    DR_pct: 0.75\n    CF_pct: 9.9\n    E_F1: 31.28\n    R_F1: 7.42\n    parse_fail_rate: 0\n    total_samples: 551\n    note: 'F1 computed by v2 checker; greedy baseline with same checker: E_F1=30.98,\n      R_F1=8.36'\n- exp_id: w9_qwen_docred_zs_sampling\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: w9_qwen_docred_zs_sampling_r2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: beam_search_scierc_full_551\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ET_pct: 0\n    RV_pct: 0\n    DR_pct: 0\n    CF_pct: 0.53\n    E_F1: 32\n    R_F1: 8.56\n    E_P: 26.83\n    E_R: 39.63\n    R_P: 6.69\n    R_R: 11.91\n    parse_fail_rate: 0\n    total_entities: 2476\n    total_relations: 1737\n- exp_id: w9_qwen_scierc_stability_3seeds\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    seed_123:\n      ET_pct: 0\n      RV_pct: 0\n      DR_pct: 0.93\n      CF_pct: 9.9\n      E_F1: 30.98\n      R_F1: 8.36\n    seed_456:\n      ET_pct: 0\n      RV_pct: 0\n      DR_pct: 0.93\n      CF_pct: 9.9\n      E_F1: 30.98\n      R_F1: 8.36\n    seed_789:\n      ET_pct: 0\n      RV_pct: 0\n      DR_pct: 0.93\n      CF_pct: 9.9\n      E_F1: 30.98\n      R_F1: 8.36\n    cross_seed_DR_std: 0\n    cross_seed_DR_range: 0\n    conclusion_note: Greedy decoding is fully deterministic - seed has no effect on\n      output. All metrics identical across 3 seeds.\n- exp_id: w9_llama_scierc_beam_551\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ET_pct: 0\n    RV_pct: 0\n    DR_pct: 0\n    CF_pct: 0.93\n    CF_count: 15\n    E_F1: 25.04\n    E_P: 21.27\n    E_R: 30.42\n    R_F1: 3.33\n    R_P: 2.68\n    R_R: 4.41\n    total_entities: 2398\n    total_relations: 1606\n    parse_fail_rate: 0\n    total_samples: 551\n    vs_greedy_full_s1:\n      DR_delta: -0.08\n      CF_delta: -5.63\n      E_F1_delta: 1.55\n      R_F1_delta: 0.79\n      note: 'Greedy: DR=0.08%, CF=6.56%, E_F1=23.49%, R_F1=2.54%'\n- exp_id: w9_qwen_docred_beam_50\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ET_pct: 0\n    RV_pct: 0\n    DR_pct: 0\n    CF_pct: 0.55\n    E_F1: 58.64\n    R_F1: 9.37\n    total_samples: 50\n    parse_failures: 3\n    parse_fail_rate: 6\n    vs_greedy_full_s1:\n      DR_delta: -10.21\n      CF_delta: -2.02\n      E_F1_delta: -0.73\n      R_F1_delta: 1.14\n      note: 'Greedy full_s1 998 docs: DR=10.21%, CF=2.57%, E_F1=59.37, R_F1=8.23.\n        Beam eliminates ALL DR on DocRED 96-type schema.'\n- exp_id: w10_type_consensus_prototype\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    ET_pct: 0\n    RV_pct: 0\n    DR_pct: 0.93\n    CF_pct: 9.9\n    E_F1: 30.98\n    R_F1: 8.36\n    gtc_skip_total: 672\n    gtc_skip_unique_entities: 258\n    gtc_effective_corrections: 0\n    delta_DR: 0\n    delta_CF: 0\n- exp_id: w10_type_consensus_docred_50\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    ET_pct: 0\n    RV_pct: 0\n    DR_pct: 8.69\n    CF_pct: 2.4\n    E_F1: 59.08\n    R_F1: 8.33\n    gtc_skip_total: 601\n    gtc_skip_unique_entities: 213\n    gtc_effective_corrections: 0\n    delta_DR: 0\n    delta_CF: 0\n- exp_id: w10_llama_docred_beam_50\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ET_pct: 0\n    RV_pct: 0\n    DR_pct: 0\n    CF_pct: 0.94\n    E_F1: 55.62\n    R_F1: 9.47\n    parse_failures: 3\n    parse_fail_rate: 6\n    total_samples: 50\n    vs_greedy_full_s1:\n      DR_delta: -2.57\n      CF_delta: -11.19\n      E_F1_delta: 0.61\n      R_F1_delta: 3.2\n      note: 'Greedy baseline: DR=2.57%, CF=12.13%, E_F1=55.01, R_F1=6.27'\n    checker_note: Must use violation_checker_docred.py for DocRED (not violation_checker.py)\n- exp_id: w10_mistral_scierc_beam_551\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    total_samples: 551\n    parse_failures: 1\n    parse_rate: 0.9982\n    ET_pct: 0\n    RV_pct: 0\n    DR_pct: 13.79\n    CF_pct: 0.57\n    E_P: 23.04\n    E_R: 31.64\n    E_F1: 26.66\n    R_P: 3.13\n    R_R: 7.22\n    R_F1: 4.37\n    total_entities: 2294\n    total_triples: 2241\n    vs_greedy:\n      baseline: w6_mistral_scierc_constrained\n      greedy_DR: 13.4\n      greedy_CF: 1.27\n      greedy_E_F1: 27.46\n      greedy_R_F1: 3.67\n      delta_DR: +0.39pp\n      delta_CF: -0.70pp\n      delta_E_F1: -0.80pp\n      delta_R_F1: +0.70pp\n- exp_id: w10_beam_ablation_k2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ET_pct: 0\n    RV_pct: 0\n    DR_pct: 0.35\n    CF_count: 71\n    CF_pct: 4.12\n    E_F1: 31.54\n    R_F1: 8.75\n    parse_failures: 0\n    total_samples: 551\n    total_triples: 1724\n    vs_greedy:\n      DR_delta: -0.58\n      CF_delta: -5.78\n      E_F1_delta: 0.56\n      R_F1_delta: 0.39\n      note: 'Greedy: DR=0.93%, CF=9.90%, E_F1=30.98, R_F1=8.36'\n    vs_beam_k4:\n      DR_delta: 0.35\n      CF_delta: 3.59\n      E_F1_delta: -0.46\n      R_F1_delta: 0.19\n      note: 'k=4: DR=0%, CF=0.53%, E_F1=32.00, R_F1=8.56'\n- exp_id: w10_beam_ablation_k8\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ET_pct: 0\n    RV_pct: 0\n    DR_pct: 0\n    CF_pct: 0.08\n    CF_count: 2\n    E_F1: 32.18\n    R_F1: 8.39\n    E_P: 26.95\n    E_R: 39.93\n    R_P: 6.54\n    R_R: 11.7\n    parse_failures: 0\n    total_samples: 551\n    total_triples: 1744\n    total_entities: 2483\n    vs_greedy:\n      DR_delta: -0.93\n      CF_delta: -9.82\n      E_F1_delta: 1.2\n      R_F1_delta: 0.03\n    vs_beam_k4:\n      DR_delta: 0\n      CF_delta: -0.45\n      E_F1_delta: 0.18\n      R_F1_delta: -0.17\n- exp_id: w9_mistral_docred_beam_50\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ET_violation_rate: 0\n    RV_violation_rate: 0\n    DR_violation_rate: 21.37\n    CF_violations: 1\n    total_triples: 524\n    total_entities: 597\n    docs_checked: 49\n    parse_failures: 1\n    E_F1: 51.78\n    E_P: 65.2\n    E_R: 42.94\n    R_F1: 5.7\n    R_P: 6.49\n    R_R: 5.08\n    R_tp: 34\n    R_gold: 669\n    R_pred: 524\n- exp_id: w10_qwen_scierc_ft_beam_4\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    DR: 0\n    CF: 0\n    total_violation_rate: 0\n    entity_type_violation_rate: 0\n    relation_vocab_violation_rate: 0\n    domain_range_violation_rate: 0\n    cross_field_consistency_violation_rate: 0\n    E_F1: 66.88\n    E_P: 64.69\n    E_R: 69.22\n    R_F1: 44.23\n    R_P: 39.41\n    R_R: 50.41\n    total_samples: 551\n    json_parse_failures: 0\n    total_entities: 1802\n    total_relations: 1246\n    vs_ft_greedy:\n      baseline: w5_lora_scierc_constrained_eval\n      DR_delta: 0% → 0% (same)\n      CF_delta: 1.18% → 0.0% (eliminated all violations)\n      E_F1_delta: 67.05 → 66.88 (-0.17, negligible)\n      R_F1_delta: 43.77 → 44.23 (+0.46, slight improvement)\n    vs_zs_beam_k4:\n      DR_delta: 0% → 0% (same)\n      CF_delta: 0.53% → 0.0% (eliminated)\n      E_F1_delta: 32.00 → 66.88 (+34.88)\n      R_F1_delta: 8.56 → 44.23 (+35.67)\n- exp_id: r4_prompt_minimal\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    unconstrained:\n      ET_pct: 0.58\n      RV_pct: 1.16\n      DR_pct: 16.91\n      E_F1: 31.98\n      R_F1: 7.91\n    constrained:\n      ET_pct: 0\n      RV_pct: 0\n      DR_pct: 0.92\n      E_F1: 31.99\n      R_F1: 7.85\n    DR_reduction_pct: 94.6\n    delta_R_F1_pp: -0.06\n    delta_E_F1_pp: 0.01\n- exp_id: r4_prompt_detailed\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    unconstrained:\n      ET_pct: 0.22\n      RV_pct: 0.45\n      DR_pct: 11.07\n      E_F1: 33.55\n      R_F1: 10.48\n    constrained:\n      ET_pct: 0\n      RV_pct: 0\n      DR_pct: 0.64\n      E_F1: 33.56\n      R_F1: 10.48\n    DR_reduction_pct: 94.2\n    delta_R_F1_pp: 0\n    delta_E_F1_pp: 0.01\n- exp_id: ee_qwen_wikievents_unconstrained\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    parse_success: 218/246 (88.6%)\n    ET: 0\n    EV: 24\n    RoV: 74.9\n    AC: 0.3\n    CF: 0\n    trigger_f1: 0.1184\n    argument_f1: 0.0009\n    entity_f1: 0\n- exp_id: ee_llama_wikievents_unconstrained\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    parse_success: 226/246 (91.9%)\n    ET: 0\n    EV: 10.5\n    RoV: 88.8\n    AC: 0.1\n    CF: 0\n    trigger_f1: 0.0572\n    argument_f1: 0\n    entity_f1: 0\n- exp_id: ee_qwen_wikievents_constrained\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    parse_success: 206/246 (83.7%)\n    ET: 0\n    EV: 0\n    RoV: 0.3\n    AC: 2.1\n    CF: 21.1\n    trigger_f1: 0.1339\n    argument_f1: 0.0168\n    entity_f1: 0.1409\n    parse_failures: 40\n    go_no_go: 2.4\n    note: after retry with max_new_tokens=8192\n- exp_id: ee_llama_wikievents_constrained\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    parse_success: 215/246 (87.4%)\n    ET: 0\n    EV: 0\n    RoV: 0\n    AC: 3.4\n    CF: 15.5\n    trigger_f1: 0.078\n    argument_f1: 0.011\n    entity_f1: 0.178\n    parse_failures: 31\n    go_no_go: 3.4\n    note: after retry with max_new_tokens=8192\n- exp_id: ee_mistral_wikievents_unconstrained\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    parse_success: 194/246 (78.9%)\n    ET: 0\n    EV: 37.3\n    RoV: 63.9\n    AC: 0\n    CF: 0\n    trigger_f1: 0.0241\n    argument_f1: 0\n    entity_f1: 0\n- exp_id: ee_mistral_wikievents_constrained\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    parse_success: 184/246 (74.8%)\n    ET: 0\n    EV: 0\n    RoV: 54.8\n    AC: 19.2\n    CF: 0.7\n    note: grammar_only baseline (old code without semantic mask fix)\n- exp_id: ee_mistral_wikievents_constrained_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    parse_success: 178/246 (72.4%)\n    ET: 0\n    EV: 0\n    RoV: 0.1\n    AC: 16.6\n    CF: 13.9\n    trigger_f1: 0.0508\n    argument_f1: 0.0047\n    entity_f1: 0.1245\n    parse_failures: 68\n    go_no_go: 16.7\n- exp_id: ee_qwen_wikievents_constrained_v3\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    parse_success: 206/246 (83.7%)\n    parse_failures: 40\n    ET: 0\n    EV: 0\n    RoV: 0\n    AC: 2.1\n    CF: 21.1\n    go_no_go: 2.05\n    entity_f1: 0.1409\n    trigger_f1: 0.1339\n    argument_f1: 0.0168\n    code_version: 938-line (collision+exact-match fix)\n    posthoc_args_removed: 109\n    posthoc_arg_f1: 0.017\n    cf_voting_fix_rate: 15.9%\n    cf_voting_entity_f1: 0.1352\n- exp_id: ee_llama_wikievents_constrained_v3\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    parse_success: 207/246 (84.1%)\n    parse_failures: 39\n    ET: 0\n    EV: 0\n    RoV: 0\n    AC: 3.8\n    CF: 17.2\n    go_no_go: 3.8\n    entity_f1: 0.1763\n    trigger_f1: 0.0748\n    argument_f1: 0.0118\n    code_version: 938-line (collision+exact-match fix)\n    posthoc_args_removed: 173\n    posthoc_arg_f1: 0.0118\n- exp_id: ee_mistral_wikievents_constrained_v3\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    parse_success: 218/246 (88.6%)\n    parse_failures: 28\n    ET: 0\n    EV: 0\n    RoV: 0\n    AC: 1.3\n    CF: 14.9\n    go_no_go: 1.26\n    entity_f1: 0.1171\n    trigger_f1: 0.0387\n    argument_f1: 0.0031\n    code_version: 938-line (collision+exact-match fix)\n    posthoc_args_removed: 86\n    posthoc_ac_after: 0\n- exp_id: ee_mistral_wikievents_grammar_only_v3\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    parse_success: 218/246 (88.6%)\n    parse_failures: 28\n    ET: 0\n    EV: 0\n    RoV: 64\n    AC: 13.8\n    CF: 1.1\n    go_no_go: 77.73\n    entity_f1: 0.1192\n    trigger_f1: 0.0337\n    argument_f1: 0.0027\n    code_version: 938-line (collision+exact-match fix)\n    mode: grammar_only\n- exp_id: 70b_scierc_unconstrained\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ET_pct: 0\n    RV_pct: 0.6\n    DR_pct: 6.5\n    CF_count: 0\n    CF_pct: 0\n    E_F1: 0.3517\n    E_P: 0.3009\n    E_R: 0.4232\n    R_F1: 0.1122\n    R_P: 0.0929\n    R_R: 0.1417\n    total_entities: 2353\n    total_relations: 1485\n    parse_failures: 0\n    samples: 551\n- exp_id: 70b_scierc_constrained\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ET_pct: 0\n    RV_pct: 0\n    DR_pct: 0\n    CF_count: 86\n    CF_pct: 3.66\n    E_F1: 0.3514\n    E_P: 0.3007\n    E_R: 0.4226\n    R_F1: 0.1124\n    R_P: 0.0932\n    R_R: 0.1417\n    total_entities: 2351\n    total_relations: 1481\n    parse_failures: 0\n    samples: 551\n- exp_id: 70b_docred_unconstrained\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    entity_f1: 69.03\n    entity_precision: 75.03\n    entity_recall: 63.92\n    relation_f1: 13.03\n    relation_precision: 12.43\n    relation_recall: 13.69\n    ET_violation: 0.02\n    RV_violation: 7.8\n    DR_violation: 15\n    CF_violation: 0.07\n    parse_failures: 0\n    docs_processed: 998\n- exp_id: 70b_docred_constrained\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ET_violation: 0\n    RV_violation: 0\n    DR_violation: 0\n    CF_violation: 7.01\n    entity_f1: 69.05\n    entity_precision: 75.03\n    entity_recall: 63.95\n    relation_f1: 13.07\n    relation_precision: 12.54\n    relation_recall: 13.64\n    parse_failures: 1\n    docs_processed: 997\n    total_docs: 998\n    unique_entities: 12207\n    total_triples: 13249\n- exp_id: q1_llama_lora_scierc_beam4\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ET_violation_rate: 0\n    RV_violation_rate: 0\n    DR_violation_rate: 0\n    CF_violation_rate: 0\n    entity_f1: 67.94\n    relation_f1: 46.11\n    samples: 551\n    total_entities: 1853\n    total_relations: 727\n- exp_id: p8_latency_overhead\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    samples: 551\n    unconstrained_mean_s: 4.163\n    unconstrained_median_s: 4.106\n    unconstrained_total_s: 2293.7\n    constrained_mean_s: 4.71\n    constrained_median_s: 4.644\n    constrained_total_s: 2595\n    overhead_ratio_mean: 1.131\n    overhead_ratio_median: 1.131\n    overhead_ratio_p95_perdoc: 1.262\n    overhead_pct: 13.1\n- exp_id: p8b_docred_latency\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: p8c_ft_scierc_latency\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    unconstrained_mean_s: 2.612\n    constrained_mean_s: 2.873\n    unconstrained_median_s: 2.355\n    constrained_median_s: 2.624\n    overhead_mean_pct: 10\n    overhead_median_pct: 11.42\n    per_doc_ratio_mean: 1.205\n    per_doc_ratio_median: 1.117\n    num_docs: 551\n    unconstrained_total_s: 1439\n    constrained_total_s: 1582.9\n- exp_id: p1_ee_ft_composability\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: p1_ee_ft_composability_r2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: p1_ee_ft_composability_r3\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: p1_ee_ft_composability_r4\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    unconstrained:\n      entity_f1: 0\n      trigger_f1: 0.4598\n      argument_f1: 0.1581\n      rov: 0.251\n      ac: 0.06\n      cf: 0\n      parse_rate: 0.25\n    full_s1:\n      entity_f1: 0.5823\n      trigger_f1: 0.6\n      argument_f1: 0.4667\n      rov: 0\n      ac: 0\n      cf: 0.03\n      parse_rate: 0.1\n- exp_id: p1_ee_ft_llama\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: p1_llama_ee_ft\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: p1_ee_ft_composability_r5\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    unconstrained:\n      parse_rate: 0.85\n      trigger_f1: 0.3208\n      argument_f1: 0.0785\n      rov_rate: 0.3831\n      ac_rate: 0.0268\n      go_nogo: 0.41\n    full_s1:\n      parse_rate: 0.95\n      trigger_f1: 0.2672\n      argument_f1: 0.0818\n      rov_rate: 0\n      ac_rate: 0\n      go_nogo: 0\n- exp_id: p1_ee_ft_llama_r2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    parse_rate_unconstrained: 1\n    parse_rate_constrained: 1\n    trigger_f1_unconstrained: 0.2752\n    trigger_f1_constrained: 0.2691\n    argument_f1_unconstrained: 0.0998\n    argument_f1_constrained: 0.0891\n    entity_f1: 0\n    rov_rate_unconstrained: 0.088\n    rov_rate_constrained: 0\n    ac_rate_unconstrained: 0.035\n    ac_rate_constrained: 0.008\n    go_nogo_unconstrained: 0.122\n    go_nogo_constrained: 0.0078\n- exp_id: d062_full_ft_scierc\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    unconstrained:\n      entity_f1: 0.6478\n      relation_f1: 0.3789\n      DR_pct: 2.74\n      RV_pct: 0.18\n      ET_pct: 0\n      CF_pct: 0\n    constrained:\n      entity_f1: 0.6478\n      relation_f1: 0.3789\n      DR_pct: 0\n      RV_pct: 0\n      ET_pct: 0\n      CF_pct: 1.31\n    training:\n      eval_loss_final: 0.09459\n      epochs: 3\n      total_steps: 333\n      training_time: 21m49s\n- exp_id: d062_cf_majority_voting\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    qwen_scierc_zs:\n      cf_before: 245\n      cf_after: 201\n      dr_rate_before: 0.0093\n      dr_rate_after: 0.0324\n    llama_scierc_zs:\n      cf_before: 162\n      cf_after: 123\n      dr_rate_before: 0.0008\n      dr_rate_after: 0.0236\n    qwen_docred_zs:\n      cf_before: 518\n      cf_after: 21\n      dr_rate_before: 0.1021\n      dr_rate_after: 0.1466\n    llama_docred_zs:\n      cf_before: 1358\n      cf_after: 107\n      dr_rate_before: 0.0255\n      dr_rate_after: 0.1665\n    qwen_scierc_ft:\n      cf_before: 21\n      cf_after: 12\n      dr_rate_before: 0\n      dr_rate_after: 0.0071\n    llama_scierc_ft:\n      cf_before: 8\n      cf_after: 4\n      dr_rate_before: 0.0009\n      dr_rate_after: 0.0037\n    qwen_docred_ft:\n      cf_before: 48\n      cf_after: 3\n      dr_rate_before: 0.0001\n      dr_rate_after: 0.0044\n    llama_docred_ft:\n      cf_before: 41\n      cf_after: 2\n      dr_rate_before: 0.0021\n      dr_rate_after: 0.005\n- exp_id: d062_beam_latency\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    beam4_unconstrained_s_per_doc: 3.446\n    beam4_constrained_s_per_doc: 4.013\n    beam4_unconstrained_total_s: 1898.7\n    beam4_constrained_total_s: 2211\n    beam_greedy_ratio_unconstrained: 1.319\n    beam_greedy_ratio_constrained: 1.397\n    constraint_overhead_beam: 1.165\n    constraint_overhead_greedy: 1.1\n    greedy_unconstrained_s_per_doc: 2.612\n    greedy_constrained_s_per_doc: 2.873\n- exp_id: d062_ontology_scalability\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    compile_small_total_s: 0.334\n    compile_medium_total_s: 0.322\n    compile_large_total_s: 0.345\n    compile_xlarge_total_s: 0.42\n    grammar_small_s: 0.333\n    grammar_xlarge_s: 0.365\n    semantic_small_s: 0.0004\n    semantic_xlarge_s: 0.017\n    overhead_small: 1.02\n    overhead_medium: 1.03\n    overhead_large: 1.03\n    overhead_xlarge: 1.03\n    failures: 0\n- exp_id: d063_gollie_violation_rate\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    gollie_DR: 0\n    gollie_RV: 0\n    gollie_ET: 0\n    gollie_CF: 0.67\n    gollie_entities: 300\n    gollie_relations: 7\n    gollie_empty_docs_pct: 45\n    docs_tested: 100\n- exp_id: d064_docred_full_beam\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: d065_tcr_pilot\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    scierc_zs_qwen:\n      cf_before: 9.75\n      cf_after: 0\n      dr_before: 0.93\n      dr_after: 1.21\n      ef1_delta: -0.0129\n      fund_pct: 2.04\n    scierc_zs_llama:\n      cf_before: 6.4\n      cf_after: 0\n      dr_before: 0.08\n      dr_after: 0.3\n      ef1_delta: -0.0178\n      fund_pct: 1.85\n    scierc_lora_qwen:\n      cf_before: 1.19\n      cf_after: 0\n      dr_before: 0\n      dr_after: 0\n      ef1_delta: -0.0075\n      fund_pct: 0\n    scierc_lora_llama:\n      cf_before: 0.46\n      cf_after: 0\n      dr_before: 0.09\n      dr_after: 0.09\n      ef1_delta: -0.0018\n      fund_pct: 0\n    scierc_zs_mistral:\n      cf_before: 0.67\n      cf_after: 0\n      dr_before: 13.36\n      dr_after: 12.87\n      ef1_delta: 0.0005\n      fund_pct: 0\n    docred_zs_qwen:\n      cf_before: 13.11\n      cf_after: 0\n      dr_before: 10.21\n      dr_after: 11.74\n      ef1_delta: -0.0344\n      fund_pct: 13.52\n    docred_zs_llama:\n      cf_before: 23.71\n      cf_after: 0\n      dr_before: 2.55\n      dr_after: 11.93\n      ef1_delta: -0.0521\n      fund_pct: 22.78\n    docred_zs_70b:\n      cf_before: 11.61\n      cf_after: 0\n      dr_before: 0\n      dr_after: 4.2\n      ef1_delta: -0.0598\n      fund_pct: 18.26\n    docred_lora_qwen:\n      cf_before: 0.42\n      cf_after: 0\n      dr_before: 0.01\n      dr_after: 0.14\n      ef1_delta: -0.0016\n      fund_pct: 12.16\n    docred_lora_llama:\n      cf_before: 0.36\n      cf_after: 0\n      dr_before: 0.21\n      dr_after: 0.2\n      ef1_delta: -0.0017\n      fund_pct: 11.59\n    total_configs: 10\n    all_cf_eliminated: true\n- exp_id: d065_tcr_full\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    configs_tested: 10\n    all_cf_eliminated: true\n    scierc_all_dr_delta_max: 0.28\n    docred_lora_dr_delta_max: 0.14\n    docred_zs_llama_dr_delta: 9.38\n    docred_zs_70b_dr_delta: 4.2\n    docred_zs_qwen_dr_delta: 1.53\n    fund_conflict_scierc_max: 2.04\n    fund_conflict_docred_zs_max: 22.78\n    fund_conflict_docred_lora_max: 12.16\n    lora_ef1_cost_max: 0.0075\n    zs_docred_ef1_cost_max: 0.0598\n- exp_id: d068_constraint_guided_beam_pilot\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics: {}\n- exp_id: d066_beam_sweep\n  name: ''\n  status: ANALYZING\n  conclusion: ''\n  metrics:\n    scierc_qwen3_8b:\n      k1_unc:\n        E_F1: 66.88\n        R_F1: 42.95\n        DR_pct: 2.11\n        CF_pct: 0\n        avg_time: 2.494\n      k1_con:\n        E_F1: 66.88\n        R_F1: 42.95\n        DR_pct: 0\n        CF_pct: 0.5\n        avg_time: 2.932\n      k2_unc:\n        E_F1: 67.79\n        R_F1: 44.75\n        DR_pct: 1.54\n        CF_pct: 0\n        avg_time: 2.954\n      k2_con:\n        E_F1: 67.71\n        R_F1: 44.6\n        DR_pct: 0\n        CF_pct: 0.11\n        avg_time: 3.463\n      k4_unc:\n        E_F1: 67.49\n        R_F1: 43.72\n        DR_pct: 1.89\n        CF_pct: 0\n        avg_time: 3.485\n      k4_con:\n        E_F1: 67.22\n        R_F1: 43.6\n        DR_pct: 0\n        CF_pct: 0\n        avg_time: 4.069\n      k8_unc:\n        E_F1: 66.4\n        R_F1: 43.17\n        DR_pct: 1.77\n        CF_pct: 0\n        avg_time: 4.194\n      k8_con:\n        E_F1: 66.36\n        R_F1: 43.65\n        DR_pct: 0\n        CF_pct: 0\n        avg_time: 5.058\n    pareto_optimal: k=2 con\n    best_E_F1:\n      config: k=2 unc\n      value: 67.79\n    best_R_F1:\n      config: k=2 unc\n      value: 44.75\n- exp_id: d067_seed_variance\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    qwen_scierc_unc:\n      E_F1: 66.94 ± 0.08\n      R_F1: 43.25 ± 0.43\n      DR: 2.06 ± 0.08\n      CF: 0.00 ± 0.00\n    qwen_scierc_con:\n      E_F1: 66.94 ± 0.08\n      R_F1: 43.22 ± 0.39\n      DR: 0.00 ± 0.00\n      CF: 0.48 ± 0.02\n    llama_scierc_unc:\n      E_F1: 67.99 ± 0.16\n      R_F1: 45.38 ± 0.05\n      DR: 1.04 ± 0.05\n      CF: 0.00 ± 0.00\n    llama_scierc_con:\n      E_F1: 67.99 ± 0.16\n      R_F1: 45.40 ± 0.05\n      DR: 0.03 ± 0.04\n      CF: 0.26 ± 0.02\n    max_sigma_pp: 0.43\n    greedy_deterministic: true\n    snr_dr_improvement: '>12x'\n    qwen_docred_status: pending (not started)\n    llama_scierc_seed456_con_status: running (407/551)\n- exp_id: d066_docred_beam_sweep\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: d065_qwen_greedy_4096\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: d065_qwen_greedy_4096_r2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    E-F1: 81.87\n    R-F1: 40.79\n    DR_pct: 0\n    CF_pct: 0.22\n    ET_pct: 0\n    RV_pct: 0\n    PF_pct: 8.52\n    samples: 998\n- exp_id: d066_sweep_16980_gpu1\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: d066_sweep_21461_gpu1\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total: 551\n    E_F1: 66.36\n    R_F1: 43.65\n    DR_pct: 0\n    CF_pct: 0\n    ET_pct: 0\n    RV_pct: 0\n    avg_time_s: 5.058\n    output_file: qwen_scierc_beam8_full_s1.jsonl\n    note: Actually ran on SciERC 551 docs (not DocRED 200 as originally recorded in\n      hypothesis)\n- exp_id: d066_sweep_llama_beam2_s1\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    E_F1: 85.6\n    E_P: 85.29\n    E_R: 85.92\n    R_F1: 51.17\n    R_P: 48.51\n    R_R: 54.14\n    DR_pct: 0\n    CF_pct: 0\n    ET_pct: 0\n    RV_pct: 0\n    parse_fail_pct: 0.5\n    total_samples: 200\n    total_entities_pred: 3814\n    total_relations_pred: 2839\n- exp_id: d066_sweep_llama_beam8_unc\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    E_F1: 85.77\n    E_P: 85.7\n    E_R: 85.84\n    R_F1: 51.97\n    R_P: 49.76\n    R_R: 54.38\n    DR_pct: 0\n    CF_pct: 0.05\n    ET_pct: 0\n    RV_pct: 0.07\n    parse_fail_pct: 0.5\n    total_samples: 200\n    total_entities_pred: 3788\n    total_relations_pred: 2779\n- exp_id: d066_sweep_llama_scierc_beam1_unc\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    total: 275\n    success: 275\n    fail: 0\n    output_file: llama_scierc_beam1_unconstrained.jsonl\n    note: 'INVALIDATED: Used dev set (275 docs) instead of test set (551 docs). Not\n      comparable with other beam sweep results. Llama SciERC beam sweep deprioritized\n      — must use scripts/d066_beam_sweep_scierc.sh with --data_path data/processed_data/test.json\n      if rerun.'\n- exp_id: d066_sweep_llama_beam8_s1\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    E-F1: 85.76\n    R-F1: 51.74\n    DR_pct: 0\n    CF_pct: 0\n    PF_pct: 0.5\n    samples: 200\n- exp_id: d066_sweep_llama_docred_beam1_unc\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total: 200\n    success: 196\n    fail: 4\n    output_file: llama_docred_200_beam1_unconstrained.jsonl\n- exp_id: d066_sweep_llama_docred_beam1_s1\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    E-F1: 85.43\n    R-F1: 47.35\n    DR_pct: 0\n    CF_pct: 0.19\n    PF_pct: 2\n    samples: 200\n- exp_id: d066_sweep_llama_docred_beam4_unc\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    E-F1: 85.67\n    R-F1: 52.65\n    DR_pct: 0.04\n    CF_pct: 0.08\n    PF_pct: 0.5\n    samples: 200\n- exp_id: d066_sweep_llama_docred_beam4_s1\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    E-F1: 85.61\n    E-P: 85.48\n    E-R: 85.73\n    R-F1: 51.89\n    R-P: 51.59\n    R-R: 52.2\n    DR_pct: 0\n    CF_pct: 0\n    PF_pct: 0.5\n    ET_pct: 0\n    RV_pct: 0\n    samples: 200\n    parse_fail: 1\n- exp_id: d066_sweep_llama_scierc_beam4_s1_551\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    E-F1: 68.06\n    E-P: 65.96\n    E-R: 70.29\n    R-F1: 46.18\n    R-P: 42.1\n    R-R: 51.13\n    ET_pct: 0\n    RV_pct: 0\n    DR_pct: 0\n    CF_pct: 0\n    parse_fail: 0\n    samples: 551\n    note: 'ET/RV corrected from 100→0: original eval used hardcoded DocRED ontology,\n      re-evaled with --dataset scierc'\n- exp_id: d066_sweep_llama_scierc_beam2_s1_551\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    entity_f1: 68.34\n    entity_p: 66.59\n    entity_r: 70.17\n    relation_f1: 46.12\n    relation_p: 42.73\n    relation_r: 50.1\n    parse_fail_pct: 0\n    ET_pct: 0\n    RV_pct: 0\n    DR_pct: 0\n    CF_pct: 0.17\n    note: 'ET/RV corrected from 100→0: original eval used hardcoded DocRED ontology,\n      re-evaled with --dataset scierc'\n- exp_id: d066_sweep_llama_scierc_beam8_s1_551\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    E-F1: 67.51\n    E-P: 64.99\n    E-R: 70.23\n    R-F1: 44.95\n    R-P: 40.1\n    R-R: 51.13\n    ET_pct: 0\n    RV_pct: 0\n    DR_pct: 0\n    CF_pct: 0\n    PF_pct: 0\n    samples: 551\n    note: Reconcile false positive corrected. Eval with --dataset scierc confirmed.\n- exp_id: r14_qwen_docred_beam4_998\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    E_F1: 58.19\n    R_F1: 8.72\n    DR_pct: 0\n    RV_pct: 0\n    ET_pct: 0\n    CF_pct: 4.94\n    parse_fail_pct: 3.51\n    samples: 998\n    success: 963\n    fail: 35\n- exp_id: r14_llama_docred_beam4_998\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    R_F1: 8.83\n    E_F1: 57.81\n    DR_pct: 0\n    CF_pct: 1\n    ET_pct: 0\n    RV_pct: 0\n    parse_fail_pct: 3.91\n    samples: 998\n    success: 959\n    fail: 39\n    baseline_ZS_greedy_R_F1: 6.27\n    baseline_ZS_greedy_E_F1: 54.93\n    baseline_ZS_greedy_DR_pct: 2.55\n    baseline_ZS_greedy_CF_pct: 8.54\n- exp_id: r16_trie_qwen_ft_scierc\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    E_F1: 66.73\n    R_F1: 42.57\n    ET_pct: 0\n    RV_pct: 0\n    DR_pct: 95.5\n    CF_pct: 0.09\n    parse_fail_pct: 9.1\n    samples: 551\n- exp_id: r16_trie_qwen_zs_scierc\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    E_F1: 30.97\n    R_F1: 8.64\n    ET_pct: 0\n    RV_pct: 0\n    DR_pct: 29.3\n    CF_pct: 0\n    parse_fail_pct: 0\n    samples: 551\n- exp_id: r16_trie_llama_ft_scierc\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    E_F1: 65.37\n    R_F1: 41.42\n    ET_pct: 0\n    RV_pct: 0\n    DR_pct: 15.2\n    CF_pct: 0\n    parse_fail_pct: 50.8\n    samples: 551\n- exp_id: r16_trie_llama_zs_scierc\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    E_F1: 23.23\n    R_F1: 2.9\n    ET_pct: 0\n    RV_pct: 0\n    DR_pct: 84.4\n    CF_pct: 0.36\n    parse_fail_pct: 0\n    samples: 551\n- exp_id: r16_70b_scierc_zs_s1\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    E_F1: 35.19\n    R_F1: 11.24\n    DR_pct: 0\n    RV_pct: 0\n    ET_pct: 0\n    CF_pct: 3.5\n    parse_fail_pct: 0\n    samples: 551\n    baseline_unc_E_F1: 35.21\n    baseline_unc_R_F1: 11.15\n    baseline_unc_DR_pct: 6.41\n    baseline_unc_RV_pct: 0.61\n    baseline_unc_CF_pct: 0\n- exp_id: r16_70b_docred_zs_s1\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    E_F1: 69.11\n    R_F1: 13.05\n    DR_pct: 0\n    RV_pct: 0\n    ET_pct: 0\n    CF_pct: 0.04\n    parse_fail_pct: 0.1\n    samples: 998\n    total_entities: 16599\n    total_triples: 13239\n    baseline_unc_DR_pct: 14.98\n    baseline_unc_R_F1: 13.01\n    note: Metrics corrected via eval_d064.py with DocRED schema mapping. Original\n      violation_checker.py gave R-F1=0 due to SciERC schema mismatch.\n- exp_id: r16_70b_lora_scierc\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    eval_loss: 0.0611\n    token_acc: 97.78\n    steps_completed: 663\n    epochs: 3\n    train_loss_start: 0.183\n    train_loss_end: 0.041\n- exp_id: r16_70b_lora_docred\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    eval_loss: 0.0635\n    token_acc: 97.94\n    steps_completed: 1146\n    epochs: 3\n    train_loss_start: 0.147\n    train_loss_end: 0.056\n- exp_id: eval_70b_lora_scierc_unconstrained\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: r16_70b_lora_scierc_eval\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: eval_70b_lora_docred_200_unconstrained\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: best\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n\n重要：tables 中使用 YAML flow sequence 时，所有字符串必须加双引号（如 `columns: [\"Judge\", \"Biased?\"]`），否则 `?` `:` 等字符会导致解析失败。\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-22T05:28:55.009Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-22T05:28:55.009Z",
  "sessionId": "b82a3282-ed21-4676-9e91-4d9b245dd612"
}
```

---

## Round 1

41 recorded events

### User

_source line 3 · 2026-05-22T05:28:55.033Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：

含义：Reviewers 认可 violation landscape + composable two-layer architecture 为双重贡献；cross-task (RE+EE) 证据链完整；70B LoRA 结果干净
核心假设：['Violation landscape study 被视为独立 empirical contribution（非仅 motivation section）', "Stateful entity registry + decidability taxonomy + automatic ontology compilation 的组合被视为超越 'XGrammar for IE' 的方法论创新", 'WikiEvents EE 的 EV/RoV→0% + grammar-only ablation 被接受为 cross-task generalization 的充分证据，Arg F1≈0 不被视为致命缺陷', 'CF tradeoff 的 proactive disclosure + root cause analysis + beam search mitigation 被接受为诚实且充分的处理', '70B LoRA eval: DR≤0.1%, |ΔR-F1|≤0.3pp（复现 8B LoRA 的 scale-neutral 模式）', '至少 2/3 reviewers 认可 novelty 不仅是 engineering 而是 methodological advance']
关键指标范围：{'emnlp_overall_assessment': [4.0, 4.5], 'review_novelty': [3.5, 4.0], 'review_soundness': [4.0, 4.5], 'review_significance': [3.5, 4.0], '70b_lora_scierc_DR_pct': [0, 0.1], '70b_lora_scierc_R_F1_delta_pp': [-0.3, 0.3], '70b_lora_docred_DR_pct': [0, 0.2], '70b_lora_docred_R_F1_delta_pp': [-0.5, 0.5], 'hostile_reviewer_count': [0, 1]}
叙事方向：原始 framing 完全成立——"universal ontology-constrained structured generation framework"。 Paper story: violation landscape (empirical contribution #1) → composable constraint compilation (methodological contribution #2) → RE 验证 (3 models × 2 datasets × ZS+FT) + EE 跨任务泛化 + 70B scale generalization。 Claims 无需降级。Title 保留 "Type-Valid IE via Compiled Ontology Constraints"。 CF 写入 §7 limitation + beam search mitigation 写入 §5.5，不影响 core claim。 Conference main 稳过。


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

重要：tables 中使用 YAML flow sequence 时，所有字符串必须加双引号（如 `columns: ["Judge", "Biased?"]`），否则 `?` `:` 等字符会导致解析失败。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "786f7088-ac23-479c-aa7e-7dfebc108fef",
  "type": "user",
  "uuid": "8c124532-d408-4ed7-ad10-51cd91751bc2",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6",
  "sessionId": "b82a3282-ed21-4676-9e91-4d9b245dd612",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-22T05:28:55.031Z_

```json
{
  "parentUuid": "8c124532-d408-4ed7-ad10-51cd91751bc2",
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
  "uuid": "8d7ba68d-72c2-4738-86f1-76d675760534",
  "timestamp": "2026-05-22T05:28:55.031Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6",
  "sessionId": "b82a3282-ed21-4676-9e91-4d9b245dd612",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-22T05:28:55.031Z_

```json
{
  "parentUuid": "8d7ba68d-72c2-4738-86f1-76d675760534",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "84660c40-fd8d-4842-9f82-5a18943c54de",
  "timestamp": "2026-05-22T05:28:55.031Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6",
  "sessionId": "b82a3282-ed21-4676-9e91-4d9b245dd612",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：Reviewers 认可 violation landscape + composable two-layer architecture 为双重贡献；cross-task (RE+EE) 证据链完整；70B LoRA 结果干净 核心假设：['Violation landscape study 被视为独立 em…",
  "leafUuid": "84660c40-fd8d-4842-9f82-5a18943c54de",
  "sessionId": "b82a3282-ed21-4676-9e91-4d9b245dd612"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "EMNLP 2026 Conference Main Submission Evaluation",
  "sessionId": "b82a3282-ed21-4676-9e91-4d9b245dd612"
}
```

---

### Assistant

_source line 8 · 2026-05-22T05:28:59.241Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed predicted experimental results for all planned experiments in the experiment_plan, based on the "best" tier definition provided. Let me first find and read the experiment_plan to understand what experiments are planned.

Let me search for the experiment plan file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "84660c40-fd8d-4842-9f82-5a18943c54de",
  "isSidechain": false,
  "requestId": "req_011CbH4C2CPTyTDPA8rFQ1sv",
  "type": "assistant",
  "uuid": "8ced1cec-4d2e-4915-af23-26b912b7a959",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6",
  "sessionId": "b82a3282-ed21-4676-9e91-4d9b245dd612",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C157KyyG9Z65BPHkZFjdVi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 43321,
      "cache_read_input_tokens": 11841,
      "output_tokens": 179,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 43321,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 179,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 43321,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 43321
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

_source line 9 · 2026-05-22T05:28:59.696Z_

Let me find the experiment plan first.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8ced1cec-4d2e-4915-af23-26b912b7a959",
  "isSidechain": false,
  "requestId": "req_011CbH4C2CPTyTDPA8rFQ1sv",
  "type": "assistant",
  "uuid": "3d8c95ce-31ea-4e9f-a287-d477986f8205",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6",
  "sessionId": "b82a3282-ed21-4676-9e91-4d9b245dd612",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C157KyyG9Z65BPHkZFjdVi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 43321,
      "cache_read_input_tokens": 11841,
      "output_tokens": 179,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 43321,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 179,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 43321,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 43321
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

_source line 10 · 2026-05-22T05:29:00.291Z_

<details open><summary>🔧 Tool call — Glob · `toolu_016wNVsNZrisqmADCBb1Ffa2`</summary>

```json
{
  "pattern": "**/*experiment_plan*"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3d8c95ce-31ea-4e9f-a287-d477986f8205",
  "isSidechain": false,
  "requestId": "req_011CbH4C2CPTyTDPA8rFQ1sv",
  "type": "assistant",
  "uuid": "a9897e56-dd1c-47d5-b258-85b6e9621d2a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6",
  "sessionId": "b82a3282-ed21-4676-9e91-4d9b245dd612",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C157KyyG9Z65BPHkZFjdVi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 43321,
      "cache_read_input_tokens": 11841,
      "output_tokens": 179,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 43321,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 179,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 43321,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 43321
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

_source line 11 · 2026-05-22T05:29:00.438Z_

<details><summary>↩ Tool result · `toolu_016wNVsNZrisqmADCBb1Ffa2`</summary>

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
  "parentUuid": "a9897e56-dd1c-47d5-b258-85b6e9621d2a",
  "isSidechain": false,
  "promptId": "786f7088-ac23-479c-aa7e-7dfebc108fef",
  "type": "user",
  "uuid": "91efea7c-4d3c-4003-bd96-b8d693f946b3",
  "toolUseResult": {
    "filenames": [
      "projects/prov_grounded_uie/experiment_plan.yaml",
      "projects/schema_semantic_constrained_ie/experiment_plan.lock",
      "projects/schema_semantic_constrained_ie/artifacts/llama_docred_maxtoken/experiment_plan.md",
      "projects/schema_semantic_constrained_ie/experiment_plan.yaml"
    ],
    "durationMs": 136,
    "numFiles": 4,
    "truncated": false
  },
  "sourceToolAssistantUUID": "a9897e56-dd1c-47d5-b258-85b6e9621d2a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6",
  "sessionId": "b82a3282-ed21-4676-9e91-4d9b245dd612",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-22T05:29:00.449Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01Gg5g6KeBowgnF4AYNcBCLp`</summary>

```json
{
  "pattern": "**/*exp*plan*"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "91efea7c-4d3c-4003-bd96-b8d693f946b3",
  "isSidechain": false,
  "requestId": "req_011CbH4C2CPTyTDPA8rFQ1sv",
  "type": "assistant",
  "uuid": "4de236d9-a65c-4475-ad88-5c80611b2da8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6",
  "sessionId": "b82a3282-ed21-4676-9e91-4d9b245dd612",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C157KyyG9Z65BPHkZFjdVi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 43321,
      "cache_read_input_tokens": 11841,
      "output_tokens": 179,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 43321,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 179,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 43321,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 43321
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

_source line 13 · 2026-05-22T05:29:00.590Z_

<details><summary>↩ Tool result · `toolu_01Gg5g6KeBowgnF4AYNcBCLp`</summary>

```text
projects/prov_grounded_uie/logs/workers/worker_code_experiment-plan_20260512T114557.log
projects/prov_grounded_uie/logs/workers/worker_code_experiment-plan_20260512T114557_result.json
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
  "parentUuid": "4de236d9-a65c-4475-ad88-5c80611b2da8",
  "isSidechain": false,
  "promptId": "786f7088-ac23-479c-aa7e-7dfebc108fef",
  "type": "user",
  "uuid": "c0268f15-7942-4cbc-9cfe-c8ff69a65874",
  "toolUseResult": {
    "filenames": [
      "projects/prov_grounded_uie/logs/workers/worker_code_experiment-plan_20260512T114557.log",
      "projects/prov_grounded_uie/logs/workers/worker_code_experiment-plan_20260512T114557_result.json",
      "projects/prov_grounded_uie/experiment_plan.yaml",
      "projects/schema_semantic_constrained_ie/experiment_plan.lock",
      "projects/schema_semantic_constrained_ie/artifacts/llama_docred_maxtoken/experiment_plan.md",
      "projects/schema_semantic_constrained_ie/experiment_plan.yaml"
    ],
    "durationMs": 110,
    "numFiles": 6,
    "truncated": false
  },
  "sourceToolAssistantUUID": "4de236d9-a65c-4475-ad88-5c80611b2da8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6",
  "sessionId": "b82a3282-ed21-4676-9e91-4d9b245dd612",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-22T05:29:03.981Z_

<details open><summary>🔧 Tool call — Read · `toolu_01DyMFdfcEJTzg2z5GXt8NW1`</summary>

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
  "parentUuid": "c0268f15-7942-4cbc-9cfe-c8ff69a65874",
  "isSidechain": false,
  "requestId": "req_011CbH4CSFza9t98KuvcYUh5",
  "type": "assistant",
  "uuid": "e4b3e5a8-fd1f-435d-81d3-7c7a88ec5ed5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6",
  "sessionId": "b82a3282-ed21-4676-9e91-4d9b245dd612",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VcE3jLVFYxMReh5oKM9ADE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 462,
      "cache_read_input_tokens": 55162,
      "output_tokens": 88,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 462,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 88,
          "cache_read_input_tokens": 55162,
          "cache_creation_input_tokens": 462,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 462
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

_source line 15 · 2026-05-22T05:29:03.994Z_

<details><summary>↩ Tool result · `toolu_01DyMFdfcEJTzg2z5GXt8NW1`</summary>

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
  "parentUuid": "e4b3e5a8-fd1f-435d-81d3-7c7a88ec5ed5",
  "isSidechain": false,
  "promptId": "786f7088-ac23-479c-aa7e-7dfebc108fef",
  "type": "user",
  "uuid": "9c929862-6fe7-4984-aa59-ab457c1c8686",
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
  "sourceToolAssistantUUID": "e4b3e5a8-fd1f-435d-81d3-7c7a88ec5ed5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6",
  "sessionId": "b82a3282-ed21-4676-9e91-4d9b245dd612",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 16 · 2026-05-22T05:29:04.034Z_

````json
{
  "parentUuid": "9c929862-6fe7-4984-aa59-ab457c1c8686",
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
  "uuid": "31eed5fa-535c-465c-bbe5-f10123c8a9c8",
  "timestamp": "2026-05-22T05:29:04.034Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6",
  "sessionId": "b82a3282-ed21-4676-9e91-4d9b245dd612",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：Reviewers 认可 violation landscape + composable two-layer architecture 为双重贡献；cross-task (RE+EE) 证据链完整；70B LoRA 结果干净 核心假设：['Violation landscape study 被视为独立 em…",
  "leafUuid": "31eed5fa-535c-465c-bbe5-f10123c8a9c8",
  "sessionId": "b82a3282-ed21-4676-9e91-4d9b245dd612"
}
```

---

### Runtime record

_source line 18_

```json
{
  "type": "ai-title",
  "aiTitle": "EMNLP 2026 Conference Main Submission Evaluation",
  "sessionId": "b82a3282-ed21-4676-9e91-4d9b245dd612"
}
```

---

### Assistant

_source line 19 · 2026-05-22T05:32:42.429Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have the full experiment plan. Let me identify all the experiments that have status "planned" (i.e., not yet completed). Looking at the experiment plan, most experiments are already DONE in the registry. Let me find the ones that are still planned/pending.

Looking at the experiment plan, the experiments with results already filled in are completed. The ones without `result:` fields or with status like PREPARING/RUNNING in the registry are the planned ones.

Let me cross-reference with the registry to identify which experiments are still planned:

From the experiment plan:
- P001-P020: All DONE (results filled in)


- P021-P026: All DONE (WikiEvents experiments across Qwen, Llama, and Mistral with both unconstrained and constrained variants)
- P027: WikiEvents Mistral grammar is still pending completion
- P028-P033: Checking status on remaining experiments including post-hoc filtering, 70B models on SciERC and DocRED, error analysis, fine-tuning composability, and cross-model validation
- P034-P035: Bootstrap CI and latency overhead measurement need registry IDs, though latency overhead is already tracked
- Looking at the registry, I see several 70B LoRA experiments in various stages—training is done for SciERC and DocRED, evaluation is either complete with empty metrics or still running, which suggests there's active work on LoRA-based approaches for these tasks

Now I'm re-reading what the user actually wants—they're asking for detailed predicted data for all planned experiments in the experiment_plan, using the "best" tier definitions from Phase 1. Most experiments already have results, so I think they want me to generate imagined results for the remaining pending ones. The "best" tier has specific ranges like 70b_lora_scierc_DR_pct between 0-0.1% and 70b_lora_scierc_R_F1_delta_pp between -0.3 to 0.3 percentage points, with similar bounds for DocRED metrics.

Looking at the registry status, the 70B LoRA eval experiments are still in progress—some are preparing or running—so those are the ones that need predictions based on the "best" tier criteria. Looking at the registry entries, most of these planned experiments actually have results already recorded—P021 through P030 all show completion status. The truly pending work is the 70B LoRA experiments: the SciERC evaluation is still preparing while the DocRED evaluation is currently running, along with their constrained variants.

For the remaining planned experiments without registry data—P031 through P035—I need to generate predicted results with detailed rationales explaining what outcomes I'd expect based on the patterns from completed experiments. The constrained DocRED eval hasn't been registered yet either. Looking at the best tier metrics, I need the 70B LoRA results across both SciERC and DocRED datasets in both constrained and unconstrained modes to populate those key performance indicators. Since the user is asking for detailed data on every planned experiment, I should map out all the experiments from the experiment_plan, not just focus on the 70B LoRA ones.

Scanning through the planned experiments, most of them don't have results registered yet — these include the WikiEvents experiments across different model sizes, the grammar-only validation work, the error analysis, and the latency measurements. Some of these likely already have results available in the registry that I should check, but the ones without registered results are what I need to focus on predicting or retrieving. me identify which experiments are actually planned versus completed by checking the experiment plan file — those with a `result:` field are done, while the ones with just descriptions are still planned. Looking through the list, I can see P021, P023, P025, P027, P028, P029, P030, P032 all have some registry data already, while P031, P033, P034, and P035 don't have data yet.

But I'm noticing something important: there are 70B LoRA experiments in the registry that aren't even in the experiment_plan.yaml file at all. These were added later and include training runs and evaluations for SciERC and DocRED. The best tier definition specifically references these 70B LoRA results, so even though they're outside the original plan, they're clearly part of what needs predicted results.

I should generate predictions for both the planned experiments that are still missing results and these additional 70B LoRA evaluations. To calibrate my predictions, I'm looking at the existing 70B zero-shot results and 8B LoRA performance to estimate what the 70B LoRA numbers should be. Continuing with the LoRA results for both Llama and Qwen models across SciERC and DocRED datasets, showing similar patterns where constrained versions maintain performance while reducing hallucinations.

Now looking at the 70B model's LoRA training metrics, which show strong token accuracy around 97-98% with low evaluation losses, and I'm defining the performance thresholds for the "best" tier across both datasets to establish acceptable ranges for hallucination rates and relation F1 deltas. tier expects:
- 70B LoRA SciERC constrained: DR ≤ 0.1%, |ΔR-F1| ≤ 0.3pp
- 70B LoRA DocRED constrained: DR ≤ 0.2%, |ΔR-F1| ≤ 0.5pp

Based on:
- 8B LoRA patterns: LoRA training dramatically reduces violations even without constraints (DR drops to 0.5-2% from 6-26%)
- 70B ZS already shows lower DR than 8B ZS (6.5% vs 15.4% on SciERC; 15% vs 18.7% on DocRED)
- 70B constrained already achieves DR=0% on both datasets in ZS mode
- LoRA further reduces baseline violations → constrained DR should be very near 0%, with minimal F1 impact since LoRA models already produce mostly valid outputs

For unconstrained 70B LoRA, I'm expecting SciERC DR around 0.5-1.5% and DocRED around 0.3-0.8%, with R_F1 likely in the 45-50% range given the larger model capacity. With constraints applied, both datasets should see DR near 0% with negligible F1 degradation and minimal constraint violations.

Now I need to structure the output covering all planned experiments systematically, organizing them by dataset and configuration type. I'm realizing the user wants predictions for all planned experiments regardless of whether results already exist—they're asking me to generate the "imagined" best-tier data with detailed rationales for each one, treating this as a Phase 1 exercise before final results are in. Let me re-examine the instructions to make sure I'm interpreting this correctly.

Looking at the experiment_plan, I need to identify which experiments are truly planned (have a description but no result field) versus completed ones. That gives me a clear list of about ten experiments I need to generate predictions for, each with a detailed explanation of why those results would occur at the best tier. I'm noticing that some experiments in the registry are already running or preparing, like the 70B LoRA evaluations for SciERC and DocRED, so I need to distinguish between truly planned experiments (those without results yet) and ones that have actual data. For the YAML output, I'll use existing registry data as realized predictions where available, and generate predictions for the remaining planned experiments that are critical to the best tier assumptions. I'm working through the key narrative for the "best" tier results—the violation landscape combined with our composable architecture represents a dual contribution, and we have a complete evidence chain across relation extraction and entity extraction tasks. The 70B LoRA results look clean with minimal degradation rates, so I'm now generating the detailed YAML output. I need to pull actual registry data for completed experiments, make informed predictions for the 70B LoRA based on patterns from the 8B models, and ensure all metrics align with the "best" tier ranges. Looking at the 8B LoRA results, I see degradation rates of 1-2% unconstrained that drop to near-zero when constrained, and the 70B zero-shot shows 6.5% unconstrained degradation, so I'm extrapolating from there. Looking at the DocRED results, the 70B LoRA model shows similar patterns to the smaller variants—very low constrained DR around 0.1% or less, with modest R_F1 improvements in the 45-48% range and E_F1 around 84-86%. The eval loss metrics for 70B LoRA are comparable across both datasets, suggesting consistent training quality.

Now I'm generating specific predictions for the 70B LoRA configurations on SciERC, estimating slightly lower DR than the 8B Qwen baseline given the similar eval loss, while keeping other metrics relatively stable. Now I'm checking that all the metrics fall within acceptable ranges for the constrained models, and they do. I need to generate the full YAML output for the experiment plan, but first I should clarify what "planned" means in this context—looking back at the experiment definitions, some entries have both results and registry IDs indicating completion, while others only have descriptions.

I'm realizing that several of the "planned" experiments actually have registry data available, so I should use the actual results where they exist and only generate predictions for experiments still in progress. Let me sort through which ones have real data versus which ones need forecasting. Looking at the 70B LoRA experiments — they're referenced in the best tier metrics even though they're not formally listed in the experiment plan, so I should include predictions for those alongside the other planned experiments that still need data.

Now I'm examining the WikiEvents post-hoc filtering results more carefully. The v3 metrics show relatively small numbers of arguments removed (109 for Qwen, 173 for Llama, 86 for Mistral), which suggests the post-hoc filtering didn't aggressively strip arguments like the paper framing indicated.

Looking at the actual post-hoc filtering applied to unconstrained output, the numbers are dramatically different—Qwen went from 5,467 arguments down to just 23 (99.6% discarded), Llama from 5,053 to 3 (99.9%), and Mistral from 6,034 to 0 (100% discarded). These represent the true post-hoc filtering impact when not constrained by the model's initial output.

For the grammar-only cross-model comparison between Qwen and Llama, I'm predicting that grammar constraints will eliminate evidence violations entirely while keeping relation overlap high around 65-80%, with argument class violations rising to 8-14% as latent violations surface. For the bootstrap confidence intervals on the EE metrics, the small effect sizes suggest trigger F1 improvements of 1.5-2 percentage points and entity F1 gains of 11-18 percentage points driven by format compliance, with all comparisons likely reaching statistical significance.

On latency, I'm looking at the overhead patterns from the registry—zero-shot SciERC shows 13.1% overhead and fine-tuned around 10-11.4%, so I'd expect the EE system to incur roughly 15-20% overhead given its more complex semantic constraints.

Now I'm structuring the YAML output to match what was requested, organizing the imagined experiments with their plan IDs, descriptions, and expected results in a comprehensive but concise format.

Writing YAML structure... I need to decide whether to use actual experimental data or generate predictions for the best-tier scenario. The user wants every prediction to include a rationale, which suggests I'm making predictions aligned with the best-tier definition. For experiments with actual data, I should use those results as they represent what happened in that scenario, but I need to check if all models mentioned in the best-tier narrative actually have complete data across the specified conditions—if some results don't match the tier's claims, I'll need to reconcile that discrepancy. The 70B LoRA results are critical for validating the core claim about scale-neutral behavior. I need to map out the planned experiments systematically—WikiEvents runs across Qwen, Llama, and Mistral are already complete, along with the grammar-only and post-hoc filtering variants. Now I'm organizing these into a comprehensive YAML structure grouped by experiment type to lay out detailed predictions for what the results should show. Now I need to write out the YAML configuration. Let me reconsider the 70B LoRA experiments more carefully—I should verify which model is actually being used since the registry entries show training is complete, but I need to confirm whether these are Llama-3.1-70B or a different base model before making predictions. So r16 is the batch identifier for all the 70B experiments, including both the zero-shot and LoRA variants. The LoRA training completed with solid metrics, though the unconstrained evaluation seems to have run without capturing results. Now I need to figure out what R_F1 and DR scores the 70B LoRA will achieve by looking at the patterns from the 8B LoRA results.

Looking at the progression from zero-shot to LoRA across both Qwen and Llama 8B models, I can see consistent improvements of around 35-40 percentage points on SciERC. Since the 70B zero-shot baseline is 11.22%, I'd expect the LoRA version to land somewhere in the 45-50% range. For DocRED, the same models show similar gains, so with a 70B zero-shot baseline of 13.03%, the LoRA should reach somewhere in the 45-50% range as well.

The dependency relation metrics tell a different story—the 70B LoRA unconstrained should perform much worse than the relation F1 scores, dropping to around 0.5-1.5% on SciERC and 0.3-0.6% on DocRED, while the constrained version should be nearly zero. For entity F1, I'm expecting the 70B LoRA to reach around 68-71% on SciERC and 84-87% on DocRED, which aligns with what I'm seeing from the 8B models.

Now I'm ready to generate the YAML configuration with these predicted performance ranges.

I need to think through which tables and figures are essential for the paper—the main results table covering all models and datasets, the WikiEvents results, ablation studies, and the 70B LoRA breakdown. For visualizations, I'm planning the violation landscape heatmap, per-relation performance breakdown, the architecture diagram, ablation comparisons, and the beam search sweep analysis. I should also make sure I'm capturing the beam search experiments and other critical analyses from the registry that support the best-tier narrative.

Writing YAML output... I need to decide whether to assign new plan IDs to the 70B LoRA experiments or use descriptive names instead, and clarify my approach: I'll include any experiment marked as "planned" in the plan (those without a result field), pulling actual data from the registry where available, then organize everything into a comprehensive YAML output covering the WikiEvents experiments and other pending items.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "31eed5fa-535c-465c-bbe5-f10123c8a9c8",
  "isSidechain": false,
  "requestId": "req_011CbH4CgVW9dLh3SAP6QmNg",
  "type": "assistant",
  "uuid": "98b5df8e-09fc-4a04-834d-643e5d999bfb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6",
  "sessionId": "b82a3282-ed21-4676-9e91-4d9b245dd612",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019oLzdkKruRH72uSAretjru",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10606,
      "cache_read_input_tokens": 55624,
      "output_tokens": 12174,
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
          "output_tokens": 12174,
          "cache_read_input_tokens": 55624,
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

### Assistant

_source line 20 · 2026-05-22T05:32:42.891Z_

Let me also check for any running 70B LoRA experiments to calibrate predictions.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "98b5df8e-09fc-4a04-834d-643e5d999bfb",
  "isSidechain": false,
  "requestId": "req_011CbH4CgVW9dLh3SAP6QmNg",
  "type": "assistant",
  "uuid": "361a2e4f-8fb2-4ed3-97e5-8a99771c86dd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6",
  "sessionId": "b82a3282-ed21-4676-9e91-4d9b245dd612",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019oLzdkKruRH72uSAretjru",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10606,
      "cache_read_input_tokens": 55624,
      "output_tokens": 12174,
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
          "output_tokens": 12174,
          "cache_read_input_tokens": 55624,
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

_source line 21 · 2026-05-22T05:32:43.516Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01BhDj5pLbc5mmeQRJypTBo4`</summary>

```json
{
  "pattern": "**/70b_lora*"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "361a2e4f-8fb2-4ed3-97e5-8a99771c86dd",
  "isSidechain": false,
  "requestId": "req_011CbH4CgVW9dLh3SAP6QmNg",
  "type": "assistant",
  "uuid": "2b8666d8-71d6-4e7c-8050-ab76c5ef7b5b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6",
  "sessionId": "b82a3282-ed21-4676-9e91-4d9b245dd612",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019oLzdkKruRH72uSAretjru",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10606,
      "cache_read_input_tokens": 55624,
      "output_tokens": 12174,
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
          "output_tokens": 12174,
          "cache_read_input_tokens": 55624,
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

_source line 22 · 2026-05-22T05:32:45.727Z_

<details><summary>↩ Tool result · `toolu_01HoQMtJ9rzeSo6yNTr32DP3`</summary>

```text
Found 10 files
projects/schema_semantic_constrained_ie/report.md
projects/schema_semantic_constrained_ie/memory.md
projects/schema_semantic_constrained_ie/ROADMAP.md
projects/schema_semantic_constrained_ie/artifacts/review_reports/round_16.md
projects/schema_semantic_constrained_ie/artifacts/review_reports/round_15.md
projects/schema_semantic_constrained_ie/artifacts/review_reports/round_13.md
projects/schema_semantic_constrained_ie/artifacts/review_reports/round_12.md
projects/schema_semantic_constrained_ie/artifacts/review_reports/round_11.md
projects/schema_semantic_constrained_ie/artifacts/review_reports/round_8.md
projects/schema_semantic_constrained_ie/docs/IDEA_BRIEF.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7f5aa0d9-d7ac-4185-baad-13056d036492",
  "isSidechain": false,
  "promptId": "786f7088-ac23-479c-aa7e-7dfebc108fef",
  "type": "user",
  "uuid": "95dda1b7-eab5-4166-88d9-18e0c24771af",
  "toolUseResult": {
    "mode": "files_with_matches",
    "filenames": [
      "projects/schema_semantic_constrained_ie/report.md",
      "projects/schema_semantic_constrained_ie/memory.md",
      "projects/schema_semantic_constrained_ie/ROADMAP.md",
      "projects/schema_semantic_constrained_ie/artifacts/review_reports/round_16.md",
      "projects/schema_semantic_constrained_ie/artifacts/review_reports/round_15.md",
      "projects/schema_semantic_constrained_ie/artifacts/review_reports/round_13.md",
      "projects/schema_semantic_constrained_ie/artifacts/review_reports/round_12.md",
      "projects/schema_semantic_constrained_ie/artifacts/review_reports/round_11.md",
      "projects/schema_semantic_constrained_ie/artifacts/review_reports/round_8.md",
      "projects/schema_semantic_constrained_ie/docs/IDEA_BRIEF.md"
    ],
    "numFiles": 10
  },
  "sourceToolAssistantUUID": "7f5aa0d9-d7ac-4185-baad-13056d036492",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6",
  "sessionId": "b82a3282-ed21-4676-9e91-4d9b245dd612",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-22T05:32:43.646Z_

<details><summary>↩ Tool result · `toolu_01BhDj5pLbc5mmeQRJypTBo4`</summary>

```text
No files found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2b8666d8-71d6-4e7c-8050-ab76c5ef7b5b",
  "isSidechain": false,
  "promptId": "786f7088-ac23-479c-aa7e-7dfebc108fef",
  "type": "user",
  "uuid": "cc119ca1-737c-41de-ba90-3bf69e4881e9",
  "toolUseResult": {
    "filenames": [],
    "durationMs": 119,
    "numFiles": 0,
    "truncated": false
  },
  "sourceToolAssistantUUID": "2b8666d8-71d6-4e7c-8050-ab76c5ef7b5b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6",
  "sessionId": "b82a3282-ed21-4676-9e91-4d9b245dd612",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-22T05:32:45.696Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01HoQMtJ9rzeSo6yNTr32DP3`</summary>

```json
{
  "pattern": "70b_lora|70B.*LoRA",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "glob": "*.md",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cc119ca1-737c-41de-ba90-3bf69e4881e9",
  "isSidechain": false,
  "requestId": "req_011CbH4CgVW9dLh3SAP6QmNg",
  "type": "assistant",
  "uuid": "7f5aa0d9-d7ac-4185-baad-13056d036492",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6",
  "sessionId": "b82a3282-ed21-4676-9e91-4d9b245dd612",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019oLzdkKruRH72uSAretjru",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10606,
      "cache_read_input_tokens": 55624,
      "output_tokens": 12174,
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
          "output_tokens": 12174,
          "cache_read_input_tokens": 55624,
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

### Runtime record

_source line 25_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：Reviewers 认可 violation landscape + composable two-layer architecture 为双重贡献；cross-task (RE+EE) 证据链完整；70B LoRA 结果干净 核心假设：['Violation landscape study 被视为独立 em…",
  "leafUuid": "95dda1b7-eab5-4166-88d9-18e0c24771af",
  "sessionId": "b82a3282-ed21-4676-9e91-4d9b245dd612"
}
```

---

### Runtime record

_source line 26_

```json
{
  "type": "ai-title",
  "aiTitle": "EMNLP 2026 Conference Main Submission Evaluation",
  "sessionId": "b82a3282-ed21-4676-9e91-4d9b245dd612"
}
```

---

### Tool call

_source line 27 · 2026-05-22T05:32:49.672Z_

<details open><summary>🔧 Tool call — Read · `toolu_01JwMARgzU76j3EX43ioAHf5`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/ROADMAP.md",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "95dda1b7-eab5-4166-88d9-18e0c24771af",
  "isSidechain": false,
  "requestId": "req_011CbH4V2YhQ1Y1dbvXYjqFW",
  "type": "assistant",
  "uuid": "c73264fd-dc1c-4bf2-a16b-58cf7b4ec157",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6",
  "sessionId": "b82a3282-ed21-4676-9e91-4d9b245dd612",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YEKpGL46VCYB9hAHjQtPmq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12436,
      "cache_read_input_tokens": 66230,
      "output_tokens": 276,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12436,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 276,
          "cache_read_input_tokens": 66230,
          "cache_creation_input_tokens": 12436,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12436
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

_source line 28 · 2026-05-22T05:32:49.679Z_

<details><summary>↩ Tool result · `toolu_01JwMARgzU76j3EX43ioAHf5`</summary>

```text
1	# schema_semantic_constrained_ie — Research Dashboard
2	
3	> 最后更新: 2026-05-21 03:37 UTC | 更新原因: D081 combined plan: D079 trie + D080 GoLLIE/triple/deployment + D081 user 5-point evaluation
4	
5	## 核心方向
6	OntoCoDec: 两层约束解码（grammar + semantic）将 IE schema 翻译为 token-level constraints，消除 LLM-based IE 的 type violations。**目标: EMNLP 2026 ARR May 25 提交**。详见 paper_framing.md。
7	
8	## 当前进展
9	**阶段**: D079+D080+D081 综合执行中 — **提交前最后一轮**
10	
11	**审稿轨迹**: R12 (3.5) → R13 (3.0) → R14 (3.5) → R15 (3.0) → R16 (3.0)
12	振荡模式：3.0-3.5 交替，结构性天花板约 3.5
13	
14	**并行工作流**:
15	- Trie baseline (P0): westd-21461 cuda:1 — SciERC 4 configs GCD-equivalent 对比
16	- GoLLIE head-to-head (P0): westd-16980 cuda:1 — 同模型 code-style prompt 对比
17	- Beam 998-doc (P0): 两台 cuda:0 — full DocRED CF 缓解证据
18	- Triple validity (P1): valid-triple precision + error propagation 分析
19	- Paper Agent: deployment-grade Abstract + DocRED data leakage 澄清
20	- R16 text modifications (MF2/MF3/W1-W6/M1-M7): 已完成
21	
22	**R15→R16 已确认的改善（保持）**:
23	- ✅ §5 显式 BoostCD/GCD 对比段落
24	- ✅ "formal guarantees" → "enforcement mechanisms"
25	- ✅ κ̄ 移出 contributions enumerate
26	- ✅ ≤ 8 页（Regression Checklist 10/10 PASS）
27	- ✅ Fallback causal tracing (100% DR from fallback)
28	- ✅ 跨语言限制 in Limitations
29	
30	## 近期任务
31	- [ ] P0: 确认 trie baseline Worker 状态 + 结果提取
32	- [ ] P0: GoLLIE SciERC head-to-head 实验
33	- [ ] P0: Beam 998-doc 结果提取 (Llama + Qwen)
34	- [ ] P1: Triple validity — valid-triple precision + error propagation
35	- [ ] P1: Paper Agent deployment-grade + DocRED leakage 澄清
36	- [ ] P2: WikiEvents 官方 test split 大小核实
37	- [ ] P2: 70B LoRA SciERC（条件启动：trie 完成后）
38	- [ ] Phase 2: 全部实验数据集成到论文
39	- [ ] Regression Checklist + R17 审稿
40	- [ ] May 25 EMNLP ARR 提交
41	
42	## GPU 预算
43	westd-16980 cuda:0,1 + westd-21461 cuda:0,1 (4× RTX PRO 6000 96GB)
44	当前占用：beam 998-doc ×2 GPU + trie baseline 1 GPU + GoLLIE 1 GPU = 4/4 满载
45	
46	## 时间线
47	- **May 21 (now)**: D079-D081 全部 dispatch — 4 GPU 满载并行
48	- **May 22 AM**: Trie + beam + GoLLIE 结果到齐 → 数据集成
49	- **May 22 PM**: R17 审稿（目标 3.5）
50	- **May 23-24**: 最终修复 + 提交前 24h 冻结
51	- **May 25**: EMNLP 2026 ARR 提交
52	
53	## 关键决策日志
54	
55	| ID | 日期 | 摘要 | 关联实验 |
56	|----|------|------|----------|
57	| D084 | 2026-05-22 | D084: 撤回 D083，恢复使用 70B DocRED ZS 数据（DR 14.98%→0%,  | r16_70b_docred_zs_s1 |
58	| D083 | 2026-05-22 | D083: 放弃 70B DocRED ZS 重跑，从论文移除该数据点。70B feasibilit | r16_70b_docred_zs_s1, r16_70b_lora_scierc, r16_70b_lora_docred |
59	| D082 | 2026-05-22 | D082: 70B LoRA DocRED 推理改用 200-doc 子集 + DocRED ZS  | r16_70b_lora_docred, r16_70b_docred_zs_s1 |
60	| D081 | 2026-05-21 | D081: 评估用户 5 项补充建议——downstream KG 扩展 Task E、beam=C | — |
61	| D080 | 2026-05-21 | D080: 采纳用户 3 项审稿建议——GoLLIE head-to-head + 下游 tripl | — |
62	| D079 | 2026-05-21 | D079: R16 Action Matrix——MF1 trie-based GCD-equiva | — |
63	| D078 | 2026-05-21 | D078: R15 Action Matrix 定稿——MF1 §5 显式对比, MF2 guara | — |
64	| D077 | 2026-05-20 | R14 Action Matrix 定稿——Grammar-only ablation refram | — |
65	| D076 | 2026-05-20 | R13 Action Matrix 定稿——全文 Claim Calibration Pass +  | — |
66	| D075 | 2026-05-20 | D075: SF2 BoostCD 不做实验对比——任务不匹配（Closed IE on Wiki- | — |
67	
68	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c73264fd-dc1c-4bf2-a16b-58cf7b4ec157",
  "isSidechain": false,
  "promptId": "786f7088-ac23-479c-aa7e-7dfebc108fef",
  "type": "user",
  "uuid": "e7c63153-df8b-44b6-85fe-76bf80fdc381",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/ROADMAP.md",
      "content": "# schema_semantic_constrained_ie — Research Dashboard\n\n> 最后更新: 2026-05-21 03:37 UTC | 更新原因: D081 combined plan: D079 trie + D080 GoLLIE/triple/deployment + D081 user 5-point evaluation\n\n## 核心方向\nOntoCoDec: 两层约束解码（grammar + semantic）将 IE schema 翻译为 token-level constraints，消除 LLM-based IE 的 type violations。**目标: EMNLP 2026 ARR May 25 提交**。详见 paper_framing.md。\n\n## 当前进展\n**阶段**: D079+D080+D081 综合执行中 — **提交前最后一轮**\n\n**审稿轨迹**: R12 (3.5) → R13 (3.0) → R14 (3.5) → R15 (3.0) → R16 (3.0)\n振荡模式：3.0-3.5 交替，结构性天花板约 3.5\n\n**并行工作流**:\n- Trie baseline (P0): westd-21461 cuda:1 — SciERC 4 configs GCD-equivalent 对比\n- GoLLIE head-to-head (P0): westd-16980 cuda:1 — 同模型 code-style prompt 对比\n- Beam 998-doc (P0): 两台 cuda:0 — full DocRED CF 缓解证据\n- Triple validity (P1): valid-triple precision + error propagation 分析\n- Paper Agent: deployment-grade Abstract + DocRED data leakage 澄清\n- R16 text modifications (MF2/MF3/W1-W6/M1-M7): 已完成\n\n**R15→R16 已确认的改善（保持）**:\n- ✅ §5 显式 BoostCD/GCD 对比段落\n- ✅ \"formal guarantees\" → \"enforcement mechanisms\"\n- ✅ κ̄ 移出 contributions enumerate\n- ✅ ≤ 8 页（Regression Checklist 10/10 PASS）\n- ✅ Fallback causal tracing (100% DR from fallback)\n- ✅ 跨语言限制 in Limitations\n\n## 近期任务\n- [ ] P0: 确认 trie baseline Worker 状态 + 结果提取\n- [ ] P0: GoLLIE SciERC head-to-head 实验\n- [ ] P0: Beam 998-doc 结果提取 (Llama + Qwen)\n- [ ] P1: Triple validity — valid-triple precision + error propagation\n- [ ] P1: Paper Agent deployment-grade + DocRED leakage 澄清\n- [ ] P2: WikiEvents 官方 test split 大小核实\n- [ ] P2: 70B LoRA SciERC（条件启动：trie 完成后）\n- [ ] Phase 2: 全部实验数据集成到论文\n- [ ] Regression Checklist + R17 审稿\n- [ ] May 25 EMNLP ARR 提交\n\n## GPU 预算\nwestd-16980 cuda:0,1 + westd-21461 cuda:0,1 (4× RTX PRO 6000 96GB)\n当前占用：beam 998-doc ×2 GPU + trie baseline 1 GPU + GoLLIE 1 GPU = 4/4 满载\n\n## 时间线\n- **May 21 (now)**: D079-D081 全部 dispatch — 4 GPU 满载并行\n- **May 22 AM**: Trie + beam + GoLLIE 结果到齐 → 数据集成\n- **May 22 PM**: R17 审稿（目标 3.5）\n- **May 23-24**: 最终修复 + 提交前 24h 冻结\n- **May 25**: EMNLP 2026 ARR 提交\n\n## 关键决策日志\n\n| ID | 日期 | 摘要 | 关联实验 |\n|----|------|------|----------|\n| D084 | 2026-05-22 | D084: 撤回 D083，恢复使用 70B DocRED ZS 数据（DR 14.98%→0%,  | r16_70b_docred_zs_s1 |\n| D083 | 2026-05-22 | D083: 放弃 70B DocRED ZS 重跑，从论文移除该数据点。70B feasibilit | r16_70b_docred_zs_s1, r16_70b_lora_scierc, r16_70b_lora_docred |\n| D082 | 2026-05-22 | D082: 70B LoRA DocRED 推理改用 200-doc 子集 + DocRED ZS  | r16_70b_lora_docred, r16_70b_docred_zs_s1 |\n| D081 | 2026-05-21 | D081: 评估用户 5 项补充建议——downstream KG 扩展 Task E、beam=C | — |\n| D080 | 2026-05-21 | D080: 采纳用户 3 项审稿建议——GoLLIE head-to-head + 下游 tripl | — |\n| D079 | 2026-05-21 | D079: R16 Action Matrix——MF1 trie-based GCD-equiva | — |\n| D078 | 2026-05-21 | D078: R15 Action Matrix 定稿——MF1 §5 显式对比, MF2 guara | — |\n| D077 | 2026-05-20 | R14 Action Matrix 定稿——Grammar-only ablation refram | — |\n| D076 | 2026-05-20 | R13 Action Matrix 定稿——全文 Claim Calibration Pass +  | — |\n| D075 | 2026-05-20 | D075: SF2 BoostCD 不做实验对比——任务不匹配（Closed IE on Wiki- | — |\n\n",
      "numLines": 68,
      "startLine": 1,
      "totalLines": 68
    }
  },
  "sourceToolAssistantUUID": "c73264fd-dc1c-4bf2-a16b-58cf7b4ec157",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6",
  "sessionId": "b82a3282-ed21-4676-9e91-4d9b245dd612",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-22T05:32:51.579Z_

<details open><summary>🔧 Tool call — Grep · `toolu_018SCtk9CKeLWDxK1bZW52c8`</summary>

```json
{
  "pattern": "70b.*lora|lora.*70b|r16_70b",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "output_mode": "content",
  "glob": "*.md",
  "-i": true,
  "head_limit": 40
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e7c63153-df8b-44b6-85fe-76bf80fdc381",
  "isSidechain": false,
  "requestId": "req_011CbH4V2YhQ1Y1dbvXYjqFW",
  "type": "assistant",
  "uuid": "9da508b2-3605-4b68-9c5d-258ffb695065",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6",
  "sessionId": "b82a3282-ed21-4676-9e91-4d9b245dd612",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YEKpGL46VCYB9hAHjQtPmq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12436,
      "cache_read_input_tokens": 66230,
      "output_tokens": 276,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12436,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 276,
          "cache_read_input_tokens": 66230,
          "cache_creation_input_tokens": 12436,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12436
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

_source line 30 · 2026-05-22T05:32:51.609Z_

<details><summary>↩ Tool result · `toolu_018SCtk9CKeLWDxK1bZW52c8`</summary>

```text
projects/schema_semantic_constrained_ie/ROADMAP.md:37:- [ ] P2: 70B LoRA SciERC（条件启动：trie 完成后）
projects/schema_semantic_constrained_ie/ROADMAP.md:57:| D084 | 2026-05-22 | D084: 撤回 D083，恢复使用 70B DocRED ZS 数据（DR 14.98%→0%,  | r16_70b_docred_zs_s1 |
projects/schema_semantic_constrained_ie/ROADMAP.md:58:| D083 | 2026-05-22 | D083: 放弃 70B DocRED ZS 重跑，从论文移除该数据点。70B feasibilit | r16_70b_docred_zs_s1, r16_70b_lora_scierc, r16_70b_lora_docred |
projects/schema_semantic_constrained_ie/ROADMAP.md:59:| D082 | 2026-05-22 | D082: 70B LoRA DocRED 推理改用 200-doc 子集 + DocRED ZS  | r16_70b_lora_docred, r16_70b_docred_zs_s1 |
projects/schema_semantic_constrained_ie/artifacts/review_reports/round_8.md:22:[Omitted long matching line]
projects/schema_semantic_constrained_ie/artifacts/review_reports/round_16.md:22:[Omitted long matching line]
projects/schema_semantic_constrained_ie/artifacts/review_reports/round_16.md:34:4. **Limitations section 异常全面**：涵盖 CF trade-off、English-only、LoRA-only、WikiEvents small test set、70B INT4 only、tokenizer assumptions、API-only models 排除——几乎预见性地回答了 reviewer 想问的问题。[R2-S3]
projects/schema_semantic_constrained_ie/artifacts/review_reports/round_15.md:21:[Omitted long matching line]
projects/schema_semantic_constrained_ie/artifacts/review_reports/round_13.md:22:[Omitted long matching line]
projects/schema_semantic_constrained_ie/artifacts/review_reports/round_12.md:22:[Omitted long matching line]
projects/schema_semantic_constrained_ie/artifacts/review_reports/round_11.md:24:[Omitted long matching line]
projects/schema_semantic_constrained_ie/report.md:8:| eval_70b_lora_docred_200_unconstrained | 70B LoRA-finetuned model (r16, Llama-3.1-70B-AWQ-INT4) will achieve higher R-F1 than 8B models on DocRED 200-doc subset unconstrained extraction, serving as the unconstrained baseline for S1 comparison at 70B scale | — | — | — |
projects/schema_semantic_constrained_ie/report.md:12:- r16_70b_lora_scierc_eval: 70B AWQ INT4 LoRA fine-tuned on SciERC will achieve higher R-F1 than 8B FT (Qwen 47.15, Llama 46.13) and S1 constraints will maintain DR→0% at 70B scale（准备中）
projects/schema_semantic_constrained_ie/report.md:16:- **eval_70b_lora_scierc_unconstrained** (success): 70B LoRA-finetuned model (r16, Llama-3.1-70B-AWQ-INT4) will achieve higher R-F1 than 8B models (Qwen FT R-F1=47.15, Llama FT R-F1=46.13) on SciERC unconstrained extraction due to larger model capacity ← 基于 r16_70b_lora_scierc
projects/schema_semantic_constrained_ie/report.md:17:- **r16_70b_docred_zs_s1** (success): Llama-3.1-70B-Instruct-AWQ-INT4 with Full S1 constrained decoding on DocRED ZS will achieve DR→0% with R-F1 stable vs unconstrained, extending 70B SciERC results to DocRED and confirming scale-independent constraint effectiveness across datasets
projects/schema_semantic_constrained_ie/memory.md:3:## 70B LoRA 推理状态 (2026-05-22 05:25 UTC)
projects/schema_semantic_constrained_ie/memory.md:6:- cuda:0: SciERC 70B LoRA S1 constrained — 34/551 (6.2%), ~9s/sample, ETA ~14:40 UTC
projects/schema_semantic_constrained_ie/memory.md:7:  - SciERC unconstrained 已完成 (551 lines, `/root/autodl-tmp/schema_outputs/r16_70b_lora_scierc/scierc_unconstrained.jsonl`)
projects/schema_semantic_constrained_ie/memory.md:8:- cuda:1: DocRED 70B LoRA unconstrained — 117/200 (58.5%), ~87s/sample, ETA ~15:22 UTC
projects/schema_semantic_constrained_ie/memory.md:13:- 有 70B AWQ INT4 模型，但**无 70B LoRA checkpoint**（只有 8B merged checkpoints）
projects/schema_semantic_constrained_ie/memory.md:14:- 70B LoRA checkpoints 在 westd-16980: `/root/autodl-tmp/checkpoints/70b_lora_docred/checkpoint-1146`, `/root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663`
projects/schema_semantic_constrained_ie/memory.md:22:- 如果把 70B LoRA DocRED checkpoint 拷到 westd-21461 并行跑 S1 → 可提前 ~5 小时
projects/schema_semantic_constrained_ie/memory.md:27:- r16_70b_docred_zs_s1 已用 eval_d064.py 修正: R-F1=13.05
projects/schema_semantic_constrained_ie/memory.md:30:- 70B AWQ INT4 + LoRA 需要 monkey-patch: `peft.import_utils.is_gptqmodel_available = lambda: False`
projects/schema_semantic_constrained_ie/docs/IDEA_BRIEF.md:185:19. **[Compute Budget 调整：§8]** — 从 ~38 H100-hours → ~75 H100-hours，反映新增的 baselines、LoRA fine-tuning、70B inference、streaming metrics、ablations。 — [命中 Feasibility：实事求是，不低估实施成本]
projects/schema_semantic_constrained_ie/docs/IDEA_BRIEF.md:194:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9da508b2-3605-4b68-9c5d-258ffb695065",
  "isSidechain": false,
  "promptId": "786f7088-ac23-479c-aa7e-7dfebc108fef",
  "type": "user",
  "uuid": "0e8d1893-663c-4e20-9e1b-863bb95aaea4",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "projects/schema_semantic_constrained_ie/ROADMAP.md:37:- [ ] P2: 70B LoRA SciERC（条件启动：trie 完成后）\nprojects/schema_semantic_constrained_ie/ROADMAP.md:57:| D084 | 2026-05-22 | D084: 撤回 D083，恢复使用 70B DocRED ZS 数据（DR 14.98%→0%,  | r16_70b_docred_zs_s1 |\nprojects/schema_semantic_constrained_ie/ROADMAP.md:58:| D083 | 2026-05-22 | D083: 放弃 70B DocRED ZS 重跑，从论文移除该数据点。70B feasibilit | r16_70b_docred_zs_s1, r16_70b_lora_scierc, r16_70b_lora_docred |\nprojects/schema_semantic_constrained_ie/ROADMAP.md:59:| D082 | 2026-05-22 | D082: 70B LoRA DocRED 推理改用 200-doc 子集 + DocRED ZS  | r16_70b_lora_docred, r16_70b_docred_zs_s1 |\nprojects/schema_semantic_constrained_ie/artifacts/review_reports/round_8.md:22:[Omitted long matching line]\nprojects/schema_semantic_constrained_ie/artifacts/review_reports/round_16.md:22:[Omitted long matching line]\nprojects/schema_semantic_constrained_ie/artifacts/review_reports/round_16.md:34:4. **Limitations section 异常全面**：涵盖 CF trade-off、English-only、LoRA-only、WikiEvents small test set、70B INT4 only、tokenizer assumptions、API-only models 排除——几乎预见性地回答了 reviewer 想问的问题。[R2-S3]\nprojects/schema_semantic_constrained_ie/artifacts/review_reports/round_15.md:21:[Omitted long matching line]\nprojects/schema_semantic_constrained_ie/artifacts/review_reports/round_13.md:22:[Omitted long matching line]\nprojects/schema_semantic_constrained_ie/artifacts/review_reports/round_12.md:22:[Omitted long matching line]\nprojects/schema_semantic_constrained_ie/artifacts/review_reports/round_11.md:24:[Omitted long matching line]\nprojects/schema_semantic_constrained_ie/report.md:8:| eval_70b_lora_docred_200_unconstrained | 70B LoRA-finetuned model (r16, Llama-3.1-70B-AWQ-INT4) will achieve higher R-F1 than 8B models on DocRED 200-doc subset unconstrained extraction, serving as the unconstrained baseline for S1 comparison at 70B scale | — | — | — |\nprojects/schema_semantic_constrained_ie/report.md:12:- r16_70b_lora_scierc_eval: 70B AWQ INT4 LoRA fine-tuned on SciERC will achieve higher R-F1 than 8B FT (Qwen 47.15, Llama 46.13) and S1 constraints will maintain DR→0% at 70B scale（准备中）\nprojects/schema_semantic_constrained_ie/report.md:16:- **eval_70b_lora_scierc_unconstrained** (success): 70B LoRA-finetuned model (r16, Llama-3.1-70B-AWQ-INT4) will achieve higher R-F1 than 8B models (Qwen FT R-F1=47.15, Llama FT R-F1=46.13) on SciERC unconstrained extraction due to larger model capacity ← 基于 r16_70b_lora_scierc\nprojects/schema_semantic_constrained_ie/report.md:17:- **r16_70b_docred_zs_s1** (success): Llama-3.1-70B-Instruct-AWQ-INT4 with Full S1 constrained decoding on DocRED ZS will achieve DR→0% with R-F1 stable vs unconstrained, extending 70B SciERC results to DocRED and confirming scale-independent constraint effectiveness across datasets\nprojects/schema_semantic_constrained_ie/memory.md:3:## 70B LoRA 推理状态 (2026-05-22 05:25 UTC)\nprojects/schema_semantic_constrained_ie/memory.md:6:- cuda:0: SciERC 70B LoRA S1 constrained — 34/551 (6.2%), ~9s/sample, ETA ~14:40 UTC\nprojects/schema_semantic_constrained_ie/memory.md:7:  - SciERC unconstrained 已完成 (551 lines, `/root/autodl-tmp/schema_outputs/r16_70b_lora_scierc/scierc_unconstrained.jsonl`)\nprojects/schema_semantic_constrained_ie/memory.md:8:- cuda:1: DocRED 70B LoRA unconstrained — 117/200 (58.5%), ~87s/sample, ETA ~15:22 UTC\nprojects/schema_semantic_constrained_ie/memory.md:13:- 有 70B AWQ INT4 模型，但**无 70B LoRA checkpoint**（只有 8B merged checkpoints）\nprojects/schema_semantic_constrained_ie/memory.md:14:- 70B LoRA checkpoints 在 westd-16980: `/root/autodl-tmp/checkpoints/70b_lora_docred/checkpoint-1146`, `/root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663`\nprojects/schema_semantic_constrained_ie/memory.md:22:- 如果把 70B LoRA DocRED checkpoint 拷到 westd-21461 并行跑 S1 → 可提前 ~5 小时\nprojects/schema_semantic_constrained_ie/memory.md:27:- r16_70b_docred_zs_s1 已用 eval_d064.py 修正: R-F1=13.05\nprojects/schema_semantic_constrained_ie/memory.md:30:- 70B AWQ INT4 + LoRA 需要 monkey-patch: `peft.import_utils.is_gptqmodel_available = lambda: False`\nprojects/schema_semantic_constrained_ie/docs/IDEA_BRIEF.md:185:19. **[Compute Budget 调整：§8]** — 从 ~38 H100-hours → ~75 H100-hours，反映新增的 baselines、LoRA fine-tuning、70B inference、streaming metrics、ablations。 — [命中 Feasibility：实事求是，不低估实施成本]\nprojects/schema_semantic_constrained_ie/docs/IDEA_BRIEF.md:194:[Omitted long matching line]",
    "numLines": 26
  },
  "sourceToolAssistantUUID": "9da508b2-3605-4b68-9c5d-258ffb695065",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6",
  "sessionId": "b82a3282-ed21-4676-9e91-4d9b245dd612",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-22T05:32:56.227Z_

<details open><summary>🔧 Tool call — Read · `toolu_01H6jSmCLL6Abrdgq1LJohty`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/report.md",
  "limit": 60
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0e8d1893-663c-4e20-9e1b-863bb95aaea4",
  "isSidechain": false,
  "requestId": "req_011CbH4VUqFSXiB7AAh3vUD9",
  "type": "assistant",
  "uuid": "6d099397-f9d1-4075-95a8-5d5ab4d8a3b0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6",
  "sessionId": "b82a3282-ed21-4676-9e91-4d9b245dd612",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KsSpjWm5TcDacUNHe44vwu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3988,
      "cache_read_input_tokens": 78666,
      "output_tokens": 172,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3988,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 172,
          "cache_read_input_tokens": 78666,
          "cache_creation_input_tokens": 3988,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3988
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

_source line 32 · 2026-05-22T05:32:56.234Z_

<details><summary>↩ Tool result · `toolu_01H6jSmCLL6Abrdgq1LJohty`</summary>

```text
1	# Handover — 2026-05-22
2	
3	> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。
4	
5	## 运行中
6	| exp_id | 假设 | 状态 | 关键指标 | W&B |
7	|--------|------|------|---------|-----|
8	| eval_70b_lora_docred_200_unconstrained | 70B LoRA-finetuned model (r16, Llama-3.1-70B-AWQ-INT4) will achieve higher R-F1 than 8B models on DocRED 200-doc subset unconstrained extraction, serving as the unconstrained baseline for S1 comparison at 70B scale | — | — | — |
9	| d066_beam_sweep | Beam width k∈{1,2,4,8} on SciERC (LoRA, Qwen3-8B) will show monotonic DR/CF reduction with diminishing returns past k=4, establishing the cost-effectiveness trade-off for the beam search appendix Pareto analysis. | — | — | — |
10	
11	## 待处理
12	- r16_70b_lora_scierc_eval: 70B AWQ INT4 LoRA fine-tuned on SciERC will achieve higher R-F1 than 8B FT (Qwen 47.15, Llama 46.13) and S1 constraints will maintain DR→0% at 70B scale（准备中）
13	- p1_llama_ee_ft（准备中）
14	
15	## 近期结论
16	- **eval_70b_lora_scierc_unconstrained** (success): 70B LoRA-finetuned model (r16, Llama-3.1-70B-AWQ-INT4) will achieve higher R-F1 than 8B models (Qwen FT R-F1=47.15, Llama FT R-F1=46.13) on SciERC unconstrained extraction due to larger model capacity ← 基于 r16_70b_lora_scierc
17	- **r16_70b_docred_zs_s1** (success): Llama-3.1-70B-Instruct-AWQ-INT4 with Full S1 constrained decoding on DocRED ZS will achieve DR→0% with R-F1 stable vs unconstrained, extending 70B SciERC results to DocRED and confirming scale-independent constraint effectiveness across datasets
18	- **d066_sweep_llama_beam8_unc** (success): d066 DocRED beam sweep sub-task: Llama beam8 unconstrained on 200-doc subset (westd-16980 GPU1). Part of d066_beam_sweep parent experiment. ← 基于 d066_beam_sweep
19	
20	## 趋势
21	成功 111 / 负向 7 / 失败 11 / 共 133
22	CF_pct: 0.04 ↑（近 3 次 success）
23	DR_pct: 0 →（近 3 次 success）
24	
25	## 下一步
26	（无活跃 idea，请通过 ideas.md 添加）
27	
28	## 资源状态
29	westd-16980: 无 GPU 信息
30	westd-21461: 空闲 cuda:0, cuda:1
31	
32	## 告警
33	- mvp_phase0_docred_schema_r2: 已被终止 — unknown
34	- w1_cf_fallback_docred: 已被终止 — unknown
35	- w1_cf_fallback_llama_scierc: 已被终止 — unknown
36	- w1_cf_fallback_llama_docred: 已被终止 — unknown
37	- w9_qwen_docred_zs_sampling: 训练失败 — unknown
38	- p8b_docred_latency: 训练失败 — unknown
39	- p1_ee_ft_composability: 训练失败 — unknown
40	- p1_ee_ft_composability_r2: 训练失败 — unknown
41	- p1_ee_ft_composability_r3: 训练失败 — unknown
42	- p1_ee_ft_composability_r4: 训练失败 — unknown
43	- p1_ee_ft_llama: 训练失败 — unknown
44	- d064_docred_full_beam: 训练失败 — unknown
45	- d066_docred_beam_sweep: 训练失败 — unknown
46	- d065_qwen_greedy_4096: 训练失败 — unknown
47	- d066_sweep_llama_scierc_beam1_unc: 训练失败 — unknown
48	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6d099397-f9d1-4075-95a8-5d5ab4d8a3b0",
  "isSidechain": false,
  "promptId": "786f7088-ac23-479c-aa7e-7dfebc108fef",
  "type": "user",
  "uuid": "2be0ea17-d99c-4720-acdf-570026668e2f",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/report.md",
      "content": "# Handover — 2026-05-22\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| eval_70b_lora_docred_200_unconstrained | 70B LoRA-finetuned model (r16, Llama-3.1-70B-AWQ-INT4) will achieve higher R-F1 than 8B models on DocRED 200-doc subset unconstrained extraction, serving as the unconstrained baseline for S1 comparison at 70B scale | — | — | — |\n| d066_beam_sweep | Beam width k∈{1,2,4,8} on SciERC (LoRA, Qwen3-8B) will show monotonic DR/CF reduction with diminishing returns past k=4, establishing the cost-effectiveness trade-off for the beam search appendix Pareto analysis. | — | — | — |\n\n## 待处理\n- r16_70b_lora_scierc_eval: 70B AWQ INT4 LoRA fine-tuned on SciERC will achieve higher R-F1 than 8B FT (Qwen 47.15, Llama 46.13) and S1 constraints will maintain DR→0% at 70B scale（准备中）\n- p1_llama_ee_ft（准备中）\n\n## 近期结论\n- **eval_70b_lora_scierc_unconstrained** (success): 70B LoRA-finetuned model (r16, Llama-3.1-70B-AWQ-INT4) will achieve higher R-F1 than 8B models (Qwen FT R-F1=47.15, Llama FT R-F1=46.13) on SciERC unconstrained extraction due to larger model capacity ← 基于 r16_70b_lora_scierc\n- **r16_70b_docred_zs_s1** (success): Llama-3.1-70B-Instruct-AWQ-INT4 with Full S1 constrained decoding on DocRED ZS will achieve DR→0% with R-F1 stable vs unconstrained, extending 70B SciERC results to DocRED and confirming scale-independent constraint effectiveness across datasets\n- **d066_sweep_llama_beam8_unc** (success): d066 DocRED beam sweep sub-task: Llama beam8 unconstrained on 200-doc subset (westd-16980 GPU1). Part of d066_beam_sweep parent experiment. ← 基于 d066_beam_sweep\n\n## 趋势\n成功 111 / 负向 7 / 失败 11 / 共 133\nCF_pct: 0.04 ↑（近 3 次 success）\nDR_pct: 0 →（近 3 次 success）\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nwestd-16980: 无 GPU 信息\nwestd-21461: 空闲 cuda:0, cuda:1\n\n## 告警\n- mvp_phase0_docred_schema_r2: 已被终止 — unknown\n- w1_cf_fallback_docred: 已被终止 — unknown\n- w1_cf_fallback_llama_scierc: 已被终止 — unknown\n- w1_cf_fallback_llama_docred: 已被终止 — unknown\n- w9_qwen_docred_zs_sampling: 训练失败 — unknown\n- p8b_docred_latency: 训练失败 — unknown\n- p1_ee_ft_composability: 训练失败 — unknown\n- p1_ee_ft_composability_r2: 训练失败 — unknown\n- p1_ee_ft_composability_r3: 训练失败 — unknown\n- p1_ee_ft_composability_r4: 训练失败 — unknown\n- p1_ee_ft_llama: 训练失败 — unknown\n- d064_docred_full_beam: 训练失败 — unknown\n- d066_docred_beam_sweep: 训练失败 — unknown\n- d065_qwen_greedy_4096: 训练失败 — unknown\n- d066_sweep_llama_scierc_beam1_unc: 训练失败 — unknown\n",
      "numLines": 48,
      "startLine": 1,
      "totalLines": 48
    }
  },
  "sourceToolAssistantUUID": "6d099397-f9d1-4075-95a8-5d5ab4d8a3b0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6",
  "sessionId": "b82a3282-ed21-4676-9e91-4d9b245dd612",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-22T05:32:56.559Z_

<details open><summary>🔧 Tool call — Read · `toolu_01LE6uLAvSJkkJL1cTZZd3PF`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/memory.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2be0ea17-d99c-4720-acdf-570026668e2f",
  "isSidechain": false,
  "requestId": "req_011CbH4VUqFSXiB7AAh3vUD9",
  "type": "assistant",
  "uuid": "507cc554-0f5c-4528-af30-a399dae2895c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6",
  "sessionId": "b82a3282-ed21-4676-9e91-4d9b245dd612",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KsSpjWm5TcDacUNHe44vwu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3988,
      "cache_read_input_tokens": 78666,
      "output_tokens": 172,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3988,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 172,
          "cache_read_input_tokens": 78666,
          "cache_creation_input_tokens": 3988,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3988
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

_source line 34 · 2026-05-22T05:32:56.563Z_

<details><summary>↩ Tool result · `toolu_01LE6uLAvSJkkJL1cTZZd3PF`</summary>

```text
1	# Memory — schema_semantic_constrained_ie
2	
3	## 70B LoRA 推理状态 (2026-05-22 05:25 UTC)
4	
5	### westd-16980
6	- cuda:0: SciERC 70B LoRA S1 constrained — 34/551 (6.2%), ~9s/sample, ETA ~14:40 UTC
7	  - SciERC unconstrained 已完成 (551 lines, `/root/autodl-tmp/schema_outputs/r16_70b_lora_scierc/scierc_unconstrained.jsonl`)
8	- cuda:1: DocRED 70B LoRA unconstrained — 117/200 (58.5%), ~87s/sample, ETA ~15:22 UTC
9	  - 完成后还需跑 DocRED S1 constrained (~200 samples, 可能需 3-5 小时)
10	
11	### westd-21461
12	- cuda:0,1: 完全空闲
13	- 有 70B AWQ INT4 模型，但**无 70B LoRA checkpoint**（只有 8B merged checkpoints）
14	- 70B LoRA checkpoints 在 westd-16980: `/root/autodl-tmp/checkpoints/70b_lora_docred/checkpoint-1146`, `/root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663`
15	- 环境就绪: torch 2.8, transformers 5.8.1, peft 0.19.1, xgrammar 0.1.33
16	- 磁盘: 75G 可用 (autodl-tmp)
17	
18	### 关键路径分析
19	- Paper L19 XX.XX 占位符需要 4 组数据: SciERC unc/S1 + DocRED unc/S1
20	- SciERC pair: unc ✅ + S1 running (~78 min) → 最快 ~14:40 UTC 可用
21	- DocRED pair: unc running (~120 min) + S1 还没开始 → 如果串行，S1 最快 ~20:00 UTC
22	- 如果把 70B LoRA DocRED checkpoint 拷到 westd-21461 并行跑 S1 → 可提前 ~5 小时
23	
24	## DocRED 评估注意事项
25	- violation_checker.py 对 DocRED 的 R-F1 计算有 schema mismatch（模型输出自然语言 relation names，gold 用 P-codes）
26	- 正确评估用 eval_d064.py 或需要在 violation_checker.py 加 name→P-code 映射
27	- r16_70b_docred_zs_s1 已用 eval_d064.py 修正: R-F1=13.05
28	
29	## PEFT AWQ 兼容性
30	- 70B AWQ INT4 + LoRA 需要 monkey-patch: `peft.import_utils.is_gptqmodel_available = lambda: False`
31	- 否则 PEFT 误检测 GPTQModel 导致加载失败
32	
33	## Monitor 脚本 mode 参数
34	- `--mode full_s1` 是正确的（不是 `--mode s1`）
35	- westd-16980 上的 monitor 脚本因为用了错误 mode 导致自动启动失败，已由 Worker 手动修正
36	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "507cc554-0f5c-4528-af30-a399dae2895c",
  "isSidechain": false,
  "promptId": "786f7088-ac23-479c-aa7e-7dfebc108fef",
  "type": "user",
  "uuid": "50083dbb-727e-4ae7-80d8-6ada76984ddf",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/memory.md",
      "content": "# Memory — schema_semantic_constrained_ie\n\n## 70B LoRA 推理状态 (2026-05-22 05:25 UTC)\n\n### westd-16980\n- cuda:0: SciERC 70B LoRA S1 constrained — 34/551 (6.2%), ~9s/sample, ETA ~14:40 UTC\n  - SciERC unconstrained 已完成 (551 lines, `/root/autodl-tmp/schema_outputs/r16_70b_lora_scierc/scierc_unconstrained.jsonl`)\n- cuda:1: DocRED 70B LoRA unconstrained — 117/200 (58.5%), ~87s/sample, ETA ~15:22 UTC\n  - 完成后还需跑 DocRED S1 constrained (~200 samples, 可能需 3-5 小时)\n\n### westd-21461\n- cuda:0,1: 完全空闲\n- 有 70B AWQ INT4 模型，但**无 70B LoRA checkpoint**（只有 8B merged checkpoints）\n- 70B LoRA checkpoints 在 westd-16980: `/root/autodl-tmp/checkpoints/70b_lora_docred/checkpoint-1146`, `/root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663`\n- 环境就绪: torch 2.8, transformers 5.8.1, peft 0.19.1, xgrammar 0.1.33\n- 磁盘: 75G 可用 (autodl-tmp)\n\n### 关键路径分析\n- Paper L19 XX.XX 占位符需要 4 组数据: SciERC unc/S1 + DocRED unc/S1\n- SciERC pair: unc ✅ + S1 running (~78 min) → 最快 ~14:40 UTC 可用\n- DocRED pair: unc running (~120 min) + S1 还没开始 → 如果串行，S1 最快 ~20:00 UTC\n- 如果把 70B LoRA DocRED checkpoint 拷到 westd-21461 并行跑 S1 → 可提前 ~5 小时\n\n## DocRED 评估注意事项\n- violation_checker.py 对 DocRED 的 R-F1 计算有 schema mismatch（模型输出自然语言 relation names，gold 用 P-codes）\n- 正确评估用 eval_d064.py 或需要在 violation_checker.py 加 name→P-code 映射\n- r16_70b_docred_zs_s1 已用 eval_d064.py 修正: R-F1=13.05\n\n## PEFT AWQ 兼容性\n- 70B AWQ INT4 + LoRA 需要 monkey-patch: `peft.import_utils.is_gptqmodel_available = lambda: False`\n- 否则 PEFT 误检测 GPTQModel 导致加载失败\n\n## Monitor 脚本 mode 参数\n- `--mode full_s1` 是正确的（不是 `--mode s1`）\n- westd-16980 上的 monitor 脚本因为用了错误 mode 导致自动启动失败，已由 Worker 手动修正\n",
      "numLines": 36,
      "startLine": 1,
      "totalLines": 36
    }
  },
  "sourceToolAssistantUUID": "507cc554-0f5c-4528-af30-a399dae2895c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6",
  "sessionId": "b82a3282-ed21-4676-9e91-4d9b245dd612",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 35_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：Reviewers 认可 violation landscape + composable two-layer architecture 为双重贡献；cross-task (RE+EE) 证据链完整；70B LoRA 结果干净 核心假设：['Violation landscape study 被视为独立 em…",
  "leafUuid": "50083dbb-727e-4ae7-80d8-6ada76984ddf",
  "sessionId": "b82a3282-ed21-4676-9e91-4d9b245dd612"
}
```

---

### Runtime record

_source line 36_

```json
{
  "type": "ai-title",
  "aiTitle": "EMNLP 2026 Conference Main Submission Evaluation",
  "sessionId": "b82a3282-ed21-4676-9e91-4d9b245dd612"
}
```

---

### Runtime record

_source line 37 · 2026-05-22T05:32:56.739Z_

```json
{
  "parentUuid": "50083dbb-727e-4ae7-80d8-6ada76984ddf",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "4c6f636a-f6fc-4a50-afe0-12a3f59e67e2",
  "timestamp": "2026-05-22T05:32:56.739Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6",
  "sessionId": "b82a3282-ed21-4676-9e91-4d9b245dd612",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 38 · 2026-05-22T05:33:34.591Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a much clearer picture. The 70B LoRA experiments are actively running:
- SciERC unconstrained: DONE (551 lines)
- SciERC S1 constrained: Running, 34/551 (6.2%)
- DocRED unconstrained: Running, 117/200 (58.5%)
- DocRED S1 constrained: Not started yet

The eval_70b_lora_scierc_unconstrained is marked as "success" in the recent conclusions but has empty metrics in the registry. The report says it's based on r16_70b_lora_scierc.


I need to predict outcomes for all four evaluations using the Llama-3.1-70B-AWQ-INT4 model with LoRA. For the SciERC unconstrained eval that's already done, I'm working from the report's hypothesis about expected performance levels.

Looking at the actual registry data though, I'm noticing discrepancies between what the report claims and what the metrics show. The Qwen 8B LoRA baseline is 43.86% R-F1 and Llama 8B LoRA is 45.45%, but the report mentions different numbers. I'm cross-checking against the beam sweep results to get the right baseline for comparison.

For the 70B LoRA predictions, I'm estimating the relation F1 should land around 47-49% given the larger model capacity, with entity F1 around 69-71%, and the unconstrained detection rate staying low at 0.5-1.5%. The zero-shot performance gap between 70B and 8B models is also informing my expectations here. Looking at the constrained results, the 70B model with LoRA should hit the best tier targets of DR≤0.1% and |ΔR-F1|≤0.3pp, likely around DR≈0.05% and ΔR-F1≈+0.1pp. For the DocRED subset, I'm projecting the 70B LoRA to reach roughly 45-48% R_F1 with minimal drift around 0.3%, following the pattern where larger models maintain better stability across different datasets.

Writing YAML output...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4c6f636a-f6fc-4a50-afe0-12a3f59e67e2",
  "isSidechain": false,
  "requestId": "req_011CbH4VqQkZ8PeKXcHzWM6U",
  "type": "assistant",
  "uuid": "c7a8b261-10c2-4876-96b4-4e52c2e08078",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6",
  "sessionId": "b82a3282-ed21-4676-9e91-4d9b245dd612",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HAEshrQDoZ9YwF3ZVSQZq4",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2591,
      "cache_read_input_tokens": 82654,
      "output_tokens": 17460,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2591,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 17460,
          "cache_read_input_tokens": 82654,
          "cache_creation_input_tokens": 2591,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2591
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

_source line 39 · 2026-05-22T05:38:36.617Z_

Now I have full context. The 70B LoRA experiments are actively running — SciERC unconstrained done, S1 constrained at 6.2%, DocRED unconstrained at 58.5%. Let me generate the complete best-tier predictions.

```yaml
tier: best
narrative_guidance: >
  原始 framing 完全成立——"universal ontology-constrained structured generation framework"。
  Paper story: violation landscape (empirical contribution #1) → composable constraint compilation
  (methodological contribution #2) → RE 验证 (3 models × 2 datasets × ZS+FT) + EE 跨任务泛化 +
  70B scale generalization。Claims 无需降级。Title 保留 "Type-Valid IE via Compiled Ontology Constraints"。
  CF 写入 §7 limitation + beam search mitigation 写入 §5.5，不影响 core claim。Conference main 稳过。
  70B LoRA 结果复现 8B LoRA 的 scale-neutral 模式：DR→近零、F1 中性/微正，confirming OntoCoDec
  是 model-scale-invariant 的 plug-in infrastructure。

imagined_experiments:
  # ============================================================
  # WikiEvents EE Baselines (P021, P023, P025)
  # ============================================================
  - name: "WikiEvents Qwen3-8B unconstrained"
    plan_id: "P021"
    description: "WikiEvents event extraction, Qwen3-8B, unconstrained baseline. 246 docs."
    expected_results:
      parse_success_rate: 0.886
      ET_pct: 0
      EV_pct: 24.0
      RoV_pct: 74.9
      AC_pct: 0.3
      CF_pct: 0
      trigger_f1: 0.1184
      argument_f1: 0.0009
      entity_f1: 0
    result_rationale: >
      EV=24% 来自 Qwen 对 56 类 hierarchical event type 的部分幻觉（约 1/4 输出使用非法 event name）。
      RoV=74.9% 是压倒性违规——80 个 argument roles conditioned on event type，zero-shot 模型几乎
      随机选择 role names。Entity F1=0% 因为 unconstrained 输出不符合 schema JSON 格式，parser 无法
      识别 entity mentions。AC 低(0.3%)因为大多数 argument 已经在 RoV 阶段被计为 invalid，
      仅 role-valid 的 argument 才会被检查 AC。这些 baseline 数字建立了 EE 比 RE 更严峻的 violation
      landscape，为 two-layer architecture 的必要性提供最强动机。
    tables:
      - name: "Table: WikiEvents ZS Violation Rates (3 Models)"
        columns: ["Metric", "Qwen Unc.", "Qwen S1", "Llama Unc.", "Llama S1", "Mistral Unc.", "Mistral S1"]
        rows:
          - ["Parse %", "88.6", "83.7", "91.9", "84.1", "88.6", "88.6"]
          - ["EV %", "24.0", "0", "10.5", "0", "37.3", "0"]
          - ["RoV %", "74.9", "0", "88.8", "0", "63.9", "0"]
          - ["AC %", "0.3", "2.1", "0.1", "3.8", "0", "1.3"]
          - ["CF %", "0", "21.1", "0", "17.2", "0", "14.9"]
          - ["Trigger F1", "11.8", "13.4", "5.7", "7.5", "2.4", "3.9"]
          - ["Entity F1", "0", "14.1", "0", "17.6", "0", "11.7"]
    figures_description:
      - "Stacked bar chart: EV+RoV+AC per model, unconstrained vs constrained。视觉上 unconstrained 全是 violation（接近 100%），constrained 仅剩 AC 残余（1-4%），强烈对比。"
    analysis: >
      WikiEvents 的 violation landscape 比 RE 严峻一个数量级：RoV 64-89% vs RE 的 RV 1-30%。
      这强化了 constraint decoding 在复杂 ontology 下的核心价值论证。Entity F1 从 0%→11-18% 不是
      语义改进而是 format compliance 恢复——grammar 产出 schema-valid JSON，parser 才能识别 entities。
      三模型一致的 EV/RoV→0% 确认 framework 跨任务泛化能力。

  - name: "WikiEvents Llama-3.1-8B unconstrained"
    plan_id: "P023"
    description: "WikiEvents event extraction, Llama-3.1-8B, unconstrained baseline. 246 docs."
    expected_results:
      parse_success_rate: 0.919
      ET_pct: 0
      EV_pct: 10.5
      RoV_pct: 88.8
      AC_pct: 0.1
      CF_pct: 0
      trigger_f1: 0.0572
      argument_f1: 0
      entity_f1: 0
    result_rationale: >
      Llama EV 最低(10.5%)说明其对 event type 名称的 memorization 更好（Llama 训练数据可能包含
      更多 KAIROS-adjacent 文本）。但 RoV 最高(88.8%)，表明即便知道正确 event type，argument role
      的 per-event-type 条件约束在 ZS 下几乎不可能满足。Trigger F1 5.7% 和 Arg F1 0% 确认 ZS EE
      是极困难任务，F1 是控制变量而非优化目标。与 Qwen 的对比（EV 24% vs 10.5%，RoV 75% vs 89%）
      证明不同 model family 的 failure mode 分布不同——进一步支持 model-agnostic constraint layer 的价值。
    tables: []
    figures_description: []
    analysis: >
      Llama 的 RoV=88.8% 是所有实验中最高的单项 violation rate，形成 compelling evidence：
      即便是表现最好的模型（EV 仅 10.5%），在无约束下仍有近 90% 的 argument role 违规。
      这个反直觉发现值得在 §5.4 重点强调。

  - name: "WikiEvents Mistral-7B unconstrained"
    plan_id: "P025"
    description: "WikiEvents event extraction, Mistral-7B-v0.3, unconstrained baseline. 246 docs."
    expected_results:
      parse_success_rate: 0.789
      ET_pct: 0
      EV_pct: 37.3
      RoV_pct: 63.9
      AC_pct: 0
      CF_pct: 0
      trigger_f1: 0.0241
      argument_f1: 0
      entity_f1: 0
    result_rationale: >
      Mistral EV 最高(37.3%)——SentencePiece tokenizer(~32K vocab) 对长 hierarchical event names
      的 tokenization 效率最低，更容易产生 OOV event types。RoV 相对最低(63.9%)可能是因为 Mistral
      输出 fewer arguments overall（质量更低但 surface-level violation 更少）。AC=0% 因为 Mistral
      基本不产出 entity type annotations（entity_f1=0%），没有可检查 AC 的 argument。
      Parse rate 最低(78.9%)反映 SentencePiece tokenizer 在 complex JSON 生成上的劣势。
    tables: []
    figures_description: []
    analysis: >
      三模型的 violation 模式形成互补证据：Qwen 中等 EV + 高 RoV，Llama 低 EV + 极高 RoV，
      Mistral 高 EV + 中等 RoV。每个模型的 failure mode 分布不同，但 OntoCoDec 均实现
      EV/RoV→0%——证明 framework 的 model-agnostic 特性。

  # ============================================================
  # WikiEvents EE Ablation (P027, P028)
  # ============================================================
  - name: "WikiEvents Mistral grammar_only v3"
    plan_id: "P027"
    description: "Grammar-only ablation on Mistral WikiEvents — proves semantic layer necessity for EE."
    expected_results:
      parse_success_rate: 0.886
      ET_pct: 0
      EV_pct: 0
      RoV_pct: 64.0
      AC_pct: 13.8
      CF_pct: 1.1
      entity_f1: 0.1192
      trigger_f1: 0.0337
      argument_f1: 0.0027
    result_rationale: >
      Grammar-only 消除 EV→0%（CFG 约束 event type vocabulary 是 context-free 的），但 RoV 仍有
      64%——因为 argument role 的合法性取决于所在 event type（per-event-type conditional constraint），
      这是 context-sensitive 的，CFG 无法表达。AC 从 0%→13.8% 是 latent violation surfacing：
      grammar 强制产出有效 role names 后，这些 role 对应的 entity type 约束才能被检查，暴露
      先前被 RoV 掩盖的 AC violations。这与 RE 中 DocRED grammar_only DR=26.17%（latent DR
      surfacing）模式完全一致——是 two-layer architecture 必要性的关键 ablation 证据。
    tables:
      - name: "Table: WikiEvents Grammar-Only Ablation (Mistral)"
        columns: ["Metric", "Unconstrained", "Grammar-Only", "Full S1"]
        rows:
          - ["EV %", "37.3", "0", "0"]
          - ["RoV %", "63.9", "64.0", "0"]
          - ["AC %", "0", "13.8", "1.3"]
          - ["CF %", "0", "1.1", "14.9"]
          - ["Entity F1", "0", "11.9", "11.7"]
    figures_description:
      - "Three-panel waterfall showing constraint layers progressively reducing violations: Unconstrained → Grammar-Only → Full S1。EV 在第一步消除，RoV 在第二步消除，AC surfacing 在第二步后暴露。"
    analysis: >
      Grammar-only ablation 是论文最重要的 EE 证据之一。它证明：(1) grammar 层对 EE 的 EV
      同样有效，(2) RoV 无法被 grammar 约束——需要 semantic layer，(3) AC surfacing 模式与
      RE 中 DR surfacing 一致——同一 latent violation 机制跨任务复现。结论：two-layer architecture
      不是便利选择而是 necessary decomposition。

  - name: "WikiEvents EE post-hoc filtering (3 models)"
    plan_id: "P028"
    description: "Post-hoc filtering baseline for EE — demonstrates infeasibility of filter-based approach for complex IE tasks."
    expected_results:
      qwen_args_before: 5467
      qwen_args_after: 23
      qwen_discard_rate: 0.996
      llama_args_before: 5053
      llama_args_after: 3
      llama_discard_rate: 0.999
      mistral_args_before: 6034
      mistral_args_after: 0
      mistral_discard_rate: 1.0
    result_rationale: >
      Post-hoc filtering 在 EE 上彻底失败——因为 RoV 64-89% + EV 10-37% 的累积 violation rate
      远超 RE 的 15-26%。RE 中 post-hoc 尚可保留 52-84% triples，但 EE 中 99.6-100% 的 arguments
      被丢弃。这是因为 EE 的约束层级更深（EV→RoV→AC 三级联，任何一级违规就被过滤），
      而 RE 仅有 DR 一级主要约束。Mistral 100% discard 是极端案例：EV=37.3% 的 event type
      已经不在 ontology 中，其下所有 arguments 自动 invalid。
      这个结果使 post-hoc 在 EE 场景下完全不可行——构成 decoding-time enforcement 的最强 motivation。
    tables:
      - name: "Table: Post-hoc Filtering Feasibility (RE vs EE)"
        columns: ["Setting", "Dataset", "Discard Rate %", "Viable?"]
        rows:
          - ["RE ZS", "SciERC (Qwen)", "16.8", "Yes (costly)"]
          - ["RE ZS", "DocRED (Qwen)", "48.1", "Marginal"]
          - ["RE ZS", "DocRED (Mistral)", "73.7", "No"]
          - ["EE ZS", "WikiEvents (Qwen)", "99.6", "No"]
          - ["EE ZS", "WikiEvents (Llama)", "99.9", "No"]
          - ["EE ZS", "WikiEvents (Mistral)", "100.0", "No"]
    figures_description:
      - "Bar chart: discard rate across RE/EE datasets, 按严重程度排列，显示从 16.8%→100% 的 escalation。视觉上 EE 部分完全是黑色（discarded），与 RE 形成鲜明对比。"
    analysis: >
      Post-hoc 在 EE 的 devastating failure 是论文叙事的关键转折点。RE 中 post-hoc 尚可作为
      "expensive but functional" baseline，但 EE 中其彻底崩溃证明：随 ontology 复杂度增加，
      post-hoc 的 scalability 是 O(violations^layers)——每增加一个约束层级，discard rate
      指数增长。这为 decoding-time enforcement 建立了不可替代的 positioning。

  # ============================================================
  # 70B Zero-Shot (P029, P030) — COMPLETED
  # ============================================================
  - name: "70B SciERC unconstrained + constrained"
    plan_id: "P029"
    description: "Llama-3.1-70B-Instruct AWQ-INT4 on SciERC, zero-shot. Scale dimension (8B→70B)."
    expected_results:
      unconstrained:
        DR_pct: 6.5
        RV_pct: 0.6
        ET_pct: 0
        CF_pct: 0
        E_F1: 35.17
        R_F1: 11.22
      constrained:
        DR_pct: 0
        RV_pct: 0
        ET_pct: 0
        CF_pct: 3.66
        E_F1: 35.14
        R_F1: 11.24
      delta_DR_pp: -6.5
      delta_R_F1_pp: 0.02
      DR_reduction_pct: 100
    result_rationale: >
      70B ZS 在 SciERC 上实现 DR=0%（完全消除），远超 8B 的 DR≈0.08-0.93%。这是因为：
      (1) 70B 的 baseline DR 仅 6.5%（8B 为 13-15%），更少的 violations 意味着更少的
      fallback events，semantic mask 覆盖率更高；(2) SciERC 7-relation ontology 约束空间小，
      semantic mask 几乎不产生空交集。R_F1 delta +0.02pp 是 F1-neutral 的理想结果。
      CF=3.66% 低于 8B Qwen 的 9.9%（70B 对 entity type 的一致性更好），但仍非零——
      确认 CF 是方法论固有限制而非小模型特有问题。
    tables:
      - name: "Table: 70B ZS Results (SciERC + DocRED)"
        columns: ["Dataset", "Setting", "DR %", "RV %", "ET %", "CF %", "R-F1 %", "E-F1 %"]
        rows:
          - ["SciERC", "Unc.", "6.5", "0.6", "0", "0", "11.22", "35.17"]
          - ["SciERC", "S1", "0", "0", "0", "3.66", "11.24", "35.14"]
          - ["DocRED", "Unc.", "15.0", "7.8", "0.02", "0.07", "13.03", "69.03"]
          - ["DocRED", "S1", "0", "0", "0", "7.01", "13.07", "69.05"]
    figures_description: []
    analysis: >
      70B ZS 在两个 RE 数据集上均实现 DR=0%，R-F1 完全中性——这是最干净的 scale generalization
      证据。与 8B ZS 的 DR 0.08-10.21% 相比，70B 的更低 baseline violations 使 OntoCoDec 更容易
      实现完全消除。关键 insight：constraint effectiveness 与 model scale 正相关（更好的模型 →
      更少 baseline violations → 更少 fallback → 更高 semantic coverage → DR→0%）。

  - name: "70B DocRED unconstrained + constrained"
    plan_id: "P030"
    description: "Llama-3.1-70B-Instruct AWQ-INT4 on DocRED, zero-shot. Scale dimension."
    expected_results:
      unconstrained:
        DR_pct: 15.0
        RV_pct: 7.8
        ET_pct: 0.02
        CF_pct: 0.07
        E_F1: 69.03
        R_F1: 13.03
      constrained:
        DR_pct: 0
        RV_pct: 0
        ET_pct: 0
        CF_pct: 7.01
        E_F1: 69.05
        R_F1: 13.07
      delta_DR_pp: -15.0
      delta_R_F1_pp: 0.04
      DR_reduction_pct: 100
    result_rationale: >
      70B 在 DocRED 96-relation ontology 上也实现 DR=0%，是整个实验矩阵中最难的 ZS 配置
      （ontology 最大 × 模型最大）。8B Qwen 在 DocRED 仅达 DR↓45%（残余 10.21%），8B Llama
      DR↓90%（残余 2.55%）——70B 一步到位 DR=0%，验证了 constraint tightness × model baseline
      的 dual-factor 理论：70B 的 RV=7.8%（远低于 Qwen 29.66%）意味着 grammar 层几乎不需要
      强制纠正 relation names，semantic 层面对的都是 legitimate relation types，constraint
      coverage 因此接近 100%。CF=7.01% 与 8B Llama(12.02%) 和 8B Qwen(2.57%) 处于中间水平。
    tables: []
    figures_description: []
    analysis: >
      70B DocRED DR=0% 是实验矩阵中最关键的数据点之一。它解决了 paper 长期面临的 "DocRED
      DR 残余" 问题——不是方法论缺陷，而是小模型 baseline violation rate 过高导致 fallback
      频繁。R-F1 delta +0.04pp 与 SciERC 的 +0.02pp 一致：scale up 后 F1 影响完全中性。

  # ============================================================
  # Error Analysis (P031)
  # ============================================================
  - name: "Error analysis / case study"
    plan_id: "P031"
    description: "10-20 representative cases from v3 EE results — AC residual analysis, CF root causes, qualitative evidence."
    expected_results:
      ac_residual_cases: 8
      ac_root_cause_semantic_confusion: 6
      ac_root_cause_bpe_collision: 2
      cf_root_cause_type_ambiguity: 7
      cf_root_cause_event_complexity: 3
      qualitative_constraint_save_cases: 5
    result_rationale: >
      AC 残余（1.3-3.8%）的主要来源是语义混淆（如 SideOfConflict vs SentencedPerson，两者共享
      "参与冲突" 的语义空间）——这是 entity type ontology 的固有模糊性，非方法缺陷。Mistral
      有 2 个 BPE collision 残余案例（SID/SEN/SIDE→'S'），但 collision fix 已将 AC 从 16.6%→1.3%。
      CF 根因分析将揭示 EE 的 CF 比 RE 更高（15-21% vs 10%）是因为 argument structure 更复杂——
      同一 entity 可能在同一文档的不同 events 中扮演不同角色（如 "Iran" 在 Attack 事件中是
      Attacker(GPE) 而在 Sanction 事件中是 Target(ORG)），type assignment 本质上 event-dependent。
      Qualitative "constraint save" 案例展示 OntoCoDec 将 hallucinated event types 重定向到
      语义最近的合法 type，保留信息提取的实质内容。
    tables: []
    figures_description:
      - "Case study figure: 2-3 个并排案例，左侧 unconstrained 输出（红色标注 violations），右侧 constrained 输出（绿色标注 corrections）。展示 grammar 层修正 event type + semantic 层修正 argument role 的联合效果。"
    analysis: >
      Error analysis 为 paper 提供 qualitative depth。AC 残余的 semantic confusion 根因分析
      证明这不是 engineering bug 而是 ontology design limitation——future work 可通过 entity
      type hierarchy（如 Person 子类型细分）减少混淆。CF 的 event-dependent type assignment
      分析首次系统性解释了为什么 EE 的 CF 高于 RE——argument 结构复杂度是根因。

  # ============================================================
  # EE FT Composability (P032)
  # ============================================================
  - name: "EE FT composability"
    plan_id: "P032"
    description: "Fine-tuned model + OntoCoDec composability test on WikiEvents EE."
    expected_results:
      qwen_ft:
        unconstrained_parse_rate: 0.85
        unconstrained_trigger_f1: 0.3208
        unconstrained_arg_f1: 0.0785
        unconstrained_rov: 0.3831
        unconstrained_ac: 0.0268
        constrained_parse_rate: 0.95
        constrained_trigger_f1: 0.2672
        constrained_arg_f1: 0.0818
        constrained_rov: 0
        constrained_ac: 0
      llama_ft:
        unconstrained_trigger_f1: 0.2752
        unconstrained_arg_f1: 0.0998
        unconstrained_rov: 0.088
        unconstrained_ac: 0.035
        constrained_trigger_f1: 0.2691
        constrained_arg_f1: 0.0891
        constrained_rov: 0
        constrained_ac: 0.008
    result_rationale: >
      EE FT composability 结果与 RE FT 模式一致：LoRA fine-tuning 大幅降低 baseline violations
      （Qwen RoV 74.9%→38.3%，Llama RoV 88.8%→8.8%），OntoCoDec 进一步消除至 0%。
      关键发现：(1) Llama FT 的 RoV 降幅更大（从 88.8%→8.8%，91% 削减），说明 Llama 对
      WikiEvents schema 的 LoRA 学习效率更高；(2) 即便 FT 后，Qwen 仍有 38.3% RoV——
      FT 无法完全解决 role constraint，OntoCoDec 仍有不可替代的价值；(3) Arg F1 在
      constrained 下微升（Qwen +0.33pp, Llama 微降 -1.07pp），确认 FT+constrained 的
      composability 在 EE 上同样成立。
    tables:
      - name: "Table: EE FT Composability (Qwen + Llama)"
        columns: ["Model", "Setting", "RoV %", "AC %", "Trigger F1", "Arg F1"]
        rows:
          - ["Qwen FT", "Unc.", "38.3", "2.7", "32.1", "7.9"]
          - ["Qwen FT", "S1", "0", "0", "26.7", "8.2"]
          - ["Llama FT", "Unc.", "8.8", "3.5", "27.5", "10.0"]
          - ["Llama FT", "S1", "0", "0.8", "26.9", "8.9"]
    figures_description: []
    analysis: >
      EE FT composability 完成了 "ZS composability (RE) → FT composability (RE) →
      ZS generalization (EE) → FT composability (EE)" 的完整证据链。四个 quadrant
      全部验证：OntoCoDec 在任何 task × training regime 组合下都能即插即用地消除 violations。
      这是 "universal framework" claim 的最强支撑。

  # ============================================================
  # Supplementary Experiments (P033, P034, P035)
  # ============================================================
  - name: "Grammar-only cross-model validation (Qwen/Llama EE)"
    plan_id: "P033"
    description: "Grammar-only ablation on Qwen/Llama WikiEvents EE for completeness — extends Mistral-only ablation."
    expected_results:
      qwen_grammar_only:
        EV_pct: 0
        RoV_pct: 68.0
        AC_pct: 9.5
        CF_pct: 0.8
        entity_f1: 0.14
        trigger_f1: 0.12
      llama_grammar_only:
        EV_pct: 0
        RoV_pct: 77.0
        AC_pct: 12.0
        CF_pct: 0.5
        entity_f1: 0.17
        trigger_f1: 0.06
    result_rationale: >
      预测基于 Mistral grammar_only 模式 + cross-model violation 基线差异。Qwen grammar_only
      RoV≈68%（vs Mistral 64%）略高因为 Qwen unconstrained RoV=74.9% 本身更高，grammar 层
      不改变 role generation pattern。Llama grammar_only RoV≈77%（vs 其 unconstrained 88.8%）——
      grammar 层通过消除 OOV event types 间接减少了约 12pp RoV（部分 role violations 源于
      hallucinated event types 下不存在的 roles）。AC surfacing pattern 在三个模型上一致：
      grammar_only AC=9-14% vs unconstrained AC=0-0.3%，确认 latent violation surfacing 是
      model-agnostic 的架构特性。这三个模型的 grammar_only 消融证据足以支持论文 §5.4 中
      "grammar layer necessary but insufficient for EE" 的 claim。
    tables:
      - name: "Table: Grammar-Only Ablation Across Models (WikiEvents)"
        columns: ["Model", "EV %", "RoV %", "AC %", "CF %"]
        rows:
          - ["Mistral Unc.", "37.3", "63.9", "0", "0"]
          - ["Mistral Grammar", "0", "64.0", "13.8", "1.1"]
          - ["Mistral Full S1", "0", "0", "1.3", "14.9"]
          - ["Qwen Unc.", "24.0", "74.9", "0.3", "0"]
          - ["Qwen Grammar*", "0", "68.0", "9.5", "0.8"]
          - ["Qwen Full S1", "0", "0", "2.1", "21.1"]
          - ["Llama Unc.", "10.5", "88.8", "0.1", "0"]
          - ["Llama Grammar*", "0", "77.0", "12.0", "0.5"]
          - ["Llama Full S1", "0", "0", "3.8", "17.2"]
    figures_description: []
    analysis: >
      Tier 3 优先级——Mistral grammar_only 已足够支撑论文 claim。如果 GPU 时间允许，
      Qwen/Llama grammar_only 为 appendix 完整性提供价值，但不影响核心叙事。
      三模型一致的 AC surfacing 模式是 bonus finding。

  - name: "Bootstrap CI for EE metrics"
    plan_id: "P034"
    description: "Statistical significance testing for WikiEvents EE metric changes."
    expected_results:
      qwen_trigger_f1_delta: 1.55
      qwen_trigger_f1_p: 0.02
      qwen_entity_f1_delta: 14.09
      qwen_entity_f1_p: "<0.001"
      llama_trigger_f1_delta: 1.76
      llama_trigger_f1_p: 0.03
      llama_entity_f1_delta: 17.63
      llama_entity_f1_p: "<0.001"
      mistral_trigger_f1_delta: 1.46
      mistral_trigger_f1_p: 0.05
      mistral_entity_f1_delta: 11.71
      mistral_entity_f1_p: "<0.001"
    result_rationale: >
      Entity F1 的 0%→11-18% 跳跃在统计上必然显著（p<0.001）——这是 floor-to-nonzero 的
      结构性变化，bootstrap 的每个 resample 都会反映这一模式。Trigger F1 的 +1.5-1.8pp
      变化相对较小（基线 2.4-11.8%），在 246 docs 样本下 p-values 预计在 0.02-0.05 范围——
      borderline significant。但论文不需要 trigger F1 的显著性作为 core claim，因为
      contribution 是 violation elimination 而非 F1 improvement。Entity F1 significance
      足以在 appendix 中报告。
    tables: []
    figures_description: []
    analysis: >
      Bootstrap CI 为 EE 结果提供 statistical rigor，但在 best tier 叙事下不是关键——
      EV/RoV→0% 的 exact match 不需要 CI，这些是确定性消除。CI 主要用于 F1 metrics，
      且 Entity F1 的 floor-to-nonzero 变化 trivially significant。放入 appendix。

  - name: "Latency overhead measurement"
    plan_id: "P035"
    description: "Wall-clock comparison: unconstrained vs constrained decoding overhead across tasks."
    expected_results:
      re_zs_scierc_overhead_pct: 13.1
      re_ft_scierc_overhead_pct: 10.0
      re_zs_scierc_mean_s: 4.71
      re_ft_scierc_mean_s: 2.873
      ee_zs_wikievents_overhead_pct: 18.0
      ee_zs_wikievents_mean_s: 12.5
      beam4_overhead_pct: 16.5
      beam4_mean_s: 4.013
    result_rationale: >
      RE ZS/FT latency已有实测数据（13.1%/10%）。EE latency预测~18%——高于 RE 的 13% 因为：
      (1) WikiEvents ontology 更大（56 event types × 80 roles vs SciERC 7 relations），
      semantic mask computation 更重；(2) JSON 结构更深（events 内嵌 arguments 内嵌 entities），
      更多 token positions 需要 mask 计算；(3) 但 absolute overhead 仍远低于 2× threshold，
      属于 practical deployment 可接受范围。Beam search 的 16.5% constraint overhead 与
      greedy 13.1% 接近——beam 本身的多路扩展已 dominate latency，constraint 的增量开销
      被 amortize。所有配置均在 1.2× 以下，不构成 deployment blocker。
    tables:
      - name: "Table: Latency Overhead Summary"
        columns: ["Setting", "Unc. (s/doc)", "Con. (s/doc)", "Overhead %"]
        rows:
          - ["RE ZS SciERC (8B)", "4.16", "4.71", "13.1"]
          - ["RE FT SciERC (8B)", "2.61", "2.87", "10.0"]
          - ["RE FT SciERC Beam-4 (8B)", "3.45", "4.01", "16.5"]
          - ["EE ZS WikiEvents (8B)*", "10.6", "12.5", "~18"]
    figures_description:
      - "Bar chart: latency overhead percentage across settings, with 20% threshold line。所有 bars 在 threshold 以下，视觉上证明 practical deployability。"
    analysis: >
      Latency overhead 10-18% 在所有配置下均可接受。关键论点：相比 post-hoc filtering
      需要额外 pipeline stage + re-extraction cycle，OntoCoDec 的 single-pass overhead
      在 engineering 上更优。EE 的 18% overhead 是 worst case，仍远低于 2× boundary。

  # ============================================================
  # 70B LoRA Evaluation (CRITICAL — Best Tier Key Metrics)
  # ============================================================
  - name: "70B LoRA SciERC unconstrained eval"
    plan_id: "R16-LoRA-SciERC-Unc"
    description: >
      Llama-3.1-70B-AWQ-INT4 LoRA fine-tuned on SciERC train set (3 epochs, checkpoint-663),
      unconstrained greedy eval on SciERC test (551 docs). Baseline for constrained comparison.
    expected_results:
      DR_pct: 0.8
      RV_pct: 0
      ET_pct: 0
      CF_pct: 0
      E_F1: 69.5
      E_P: 68.0
      E_R: 71.1
      R_F1: 48.2
      R_P: 44.8
      R_R: 52.3
      parse_fail_pct: 0
      total_samples: 551
    result_rationale: >
      8B LoRA baselines: Qwen DR=1.95%, R_F1=43.86%; Llama DR=1.11%, R_F1=45.45%。
      70B LoRA 预期 DR~0.8%——低于 8B 因为 70B 的 larger capacity 使 LoRA training 对
      ontology constraints 的学习更充分（eval_loss 0.0611 与 8B 的 0.0586-0.0595 接近，
      但 70B 基座本身更强）。R_F1~48.2% 高于 8B 的 43-45%，但提升幅度不大（~3-5pp）——
      SciERC 是小数据集（551 test, ~1.7K relations），LoRA 已经 saturate 了大部分
      learnable signal，scale 的 marginal gain 有限。E_F1~69.5% 略高于 8B 的 67-68%。
      RV/ET=0% 因为 LoRA training 已完全学会 SciERC 的 7 个 relation name 和 6 个 entity type。
      CF=0% 与 8B unconstrained 一致（无 semantic enforcement 时 CF 来自 model 自身一致性）。
    tables: []
    figures_description: []
    analysis: >
      70B LoRA unconstrained 的 DR=0.8% 确认 LoRA training 在 70B 上同样有效地降低
      baseline violations（从 ZS 6.5%→LoRA 0.8%，↓88%）。R_F1 48.2% 预期为 cross-model
      最高——为 "OntoCoDec composable with best available models" claim 提供 upper-bound 证据。

  - name: "70B LoRA SciERC constrained eval (Full S1)"
    plan_id: "R16-LoRA-SciERC-S1"
    description: >
      Same 70B LoRA model, Full S1 constrained decoding on SciERC test (551 docs).
      Best tier target: DR≤0.1%, |ΔR-F1|≤0.3pp.
    expected_results:
      DR_pct: 0.05
      RV_pct: 0
      ET_pct: 0
      CF_pct: 0.6
      E_F1: 69.5
      E_P: 68.0
      E_R: 71.1
      R_F1: 48.3
      R_P: 44.9
      R_R: 52.3
      parse_fail_pct: 0
      total_samples: 551
      delta_vs_unconstrained:
        DR_delta_pp: -0.75
        R_F1_delta_pp: 0.1
        E_F1_delta_pp: 0.0
    result_rationale: >
      DR 0.8%→0.05%：70B LoRA 的 baseline DR 已极低，S1 仅需处理少量残余 violations。
      参考 8B patterns——Qwen LoRA DR 1.95%→0%, Llama LoRA 1.11%→0.09%。70B LoRA 的
      baseline 更低（0.8%），constrained 后 DR~0.05% 合理（可能有 1-2 个 edge case triple
      因 fallback 未被 semantic mask 覆盖）。

      R_F1 delta +0.1pp：与 8B Llama LoRA 的 +0.02pp 一致，在 F1-neutral 范围内。
      LoRA 模型的 baseline RV 已经≈0%，grammar 层对 F1 无贡献；semantic 层的 DR reduction
      也不改变 F1（正确 triples 的 type 本就合法）。因此 F1 delta 应极小。

      CF 0%→0.6%：与 8B Qwen LoRA 的 0%→1.18% 和 Llama LoRA 的 0%→0.46% 一致。
      70B 的 CF 可能略低于 8B Qwen 但略高于 8B Llama——取 0.6% 作为中间值。

      这些数字完美落入 best tier ranges: DR 0.05% ∈ [0, 0.1]✓, ΔR-F1 +0.1pp ∈ [-0.3, 0.3]✓。
      Scale-neutral pattern confirmed：70B LoRA 复现了 8B LoRA 的 "DR→near-zero, F1-neutral"
      行为。
    tables:
      - name: "Table: LoRA Constrained Decoding Across Scales (SciERC)"
        columns: ["Model", "DR Unc. %", "DR S1 %", "DR Red. %", "R-F1 Unc.", "R-F1 S1", "Delta R-F1 pp"]
        rows:
          - ["Qwen 8B", "1.95", "0", "100", "43.86", "43.77", "-0.09"]
          - ["Llama 8B", "1.11", "0.09", "91.9", "45.45", "45.47", "+0.02"]
          - ["Llama 70B*", "0.8", "0.05", "93.8", "48.2", "48.3", "+0.1"]
    figures_description:
      - "Scale-neutral pattern chart: x-axis = model size (8B Qwen, 8B Llama, 70B Llama), y-axis = DR% (左轴, log scale) + R-F1 delta (右轴)。DR 在所有 scales 上→near-zero，R-F1 delta 在 ±0.3pp band 内。Visual message: OntoCoDec is scale-invariant。"
    analysis: >
      70B LoRA SciERC constrained eval 是 best tier 的 make-or-break 数据点。DR≤0.1% 和
      |ΔR-F1|≤0.3pp 的预期基于三条证据线的收敛：(1) 8B Qwen/Llama LoRA 均在此范围内，
      (2) 70B ZS 已达 DR=0%，(3) eval_loss 0.0611 与 8B 可比。唯一风险是 AWQ-INT4 量化
      引入微小的 logit distortion 使个别 edge case 的 semantic mask 不生效——但 8B 未使用
      量化也有残余 DR，故此风险不大。

  - name: "70B LoRA DocRED unconstrained eval (200-doc)"
    plan_id: "R16-LoRA-DocRED-Unc"
    description: >
      Llama-3.1-70B-AWQ-INT4 LoRA fine-tuned on DocRED train set (3 epochs, checkpoint-1146),
      unconstrained greedy eval on DocRED dev 200-doc subset. Per D082 decision.
    expected_results:
      DR_pct: 0.4
      RV_pct: 0.05
      ET_pct: 0
      CF_pct: 0.1
      E_F1: 86.0
      E_P: 86.5
      E_R: 85.5
      R_F1: 46.5
      R_P: 42.0
      R_R: 52.0
      parse_fail_pct: 1.5
      total_samples: 200
    result_rationale: >
      8B LoRA DocRED baselines: Qwen DR=0.76%, R_F1=40.86%; Llama DR=0.49%, R_F1=43.72%。
      70B LoRA 预期 DR~0.4%——略低于 8B Llama 的 0.49%，因为 70B 对 DocRED 96 relations
      的学习更充分（eval_loss 0.0635 vs 8B Llama 0.0624，接近但 70B 基座更强）。
      R_F1~46.5% 高于 8B Llama 43.72%，提升 ~3pp——与 SciERC 上的 scale gain 一致。
      E_F1~86% 高于 8B Llama 83.93%，70B 对 entity mention detection 的改善更明显
      （DocRED entity extraction 更复杂，benefit from larger model capacity）。
      RV~0.05%（而非 0%）因为 DocRED 96 relations 中可能有 1-2 个 long-tail relation
      在 training data 中出现极少，70B LoRA 偶尔 hallucinate 接近但不完全匹配的 name。
      200-doc subset per D082——足以建立 scale trend，不需要 998 全量。
    tables: []
    figures_description: []
    analysis: >
      200-doc subset 的统计功效：假设 DR σ≈0.3pp（基于 8B seed variance），200 docs
      给出 95% CI ≈ ±0.04pp，足以确认 DR<0.5%。R_F1 的 95% CI ≈ ±1.5pp，足以区分
      vs 8B baseline。Scale gain ~3pp R_F1 与 SciERC 一致——confirmation of scale trend。

  - name: "70B LoRA DocRED constrained eval (200-doc, Full S1)"
    plan_id: "R16-LoRA-DocRED-S1"
    description: >
      Same 70B LoRA model, Full S1 constrained decoding on DocRED dev 200-doc subset.
      Best tier target: DR≤0.2%, |ΔR-F1|≤0.5pp.
    expected_results:
      DR_pct: 0.08
      RV_pct: 0
      ET_pct: 0
      CF_pct: 0.3
      E_F1: 86.0
      E_P: 86.5
      E_R: 85.5
      R_F1: 46.6
      R_P: 42.1
      R_R: 52.1
      parse_fail_pct: 1.5
      total_samples: 200
      delta_vs_unconstrained:
        DR_delta_pp: -0.32
        R_F1_delta_pp: 0.1
        E_F1_delta_pp: 0.0
    result_rationale: >
      DR 0.4%→0.08%：DocRED 96-relation ontology 的 constraint space 比 SciERC 更大，
      fallback frequency 相应更高（cf. 8B Qwen DocRED fallback 57次/doc vs SciERC 11次/doc）。
      但 70B LoRA 的 baseline RV≈0.05%（远低于 8B ZS Qwen 的 29.66%），grammar-semantic
      mask 交集几乎不为空，因此 fallback 率极低。预期 DR~0.08%（200 docs 上大约 1-2 个
      residual violation triple），远在 best tier 0.2% 阈值内。

      R_F1 delta +0.1pp：与 8B Llama LoRA 的 +0.06pp 一致。70B LoRA 的 RV 已极低，
      grammar 层几乎不改变 prediction distribution；semantic 层的 DR reduction 也
      不影响 F1（被纠正的 triples 大多本就是 FP）。F1 delta 在 ±0.2pp 内是高置信度预期。

      CF 0.1%→0.3%：DocRED LoRA 的 CF 整体较低（8B Llama 0.21%, Qwen 0.41%）。
      70B 的 CF 预期在此范围内。CF 增量 0.2pp 远小于 ZS 场景（ZS 70B CF=7.01%）——
      LoRA training 显著减少了 entity type inconsistency。

      Best tier alignment: DR 0.08% ∈ [0, 0.2]✓, ΔR-F1 +0.1pp ∈ [-0.5, 0.5]✓。
      Scale-neutral pattern 在 DocRED 上同样成立。
    tables:
      - name: "Table: LoRA Constrained Decoding Across Scales (DocRED)"
        columns: ["Model", "DR Unc. %", "DR S1 %", "DR Red. %", "R-F1 Unc.", "R-F1 S1", "Delta R-F1 pp"]
        rows:
          - ["Qwen 8B (998d)", "0.76", "0.01", "98.7", "40.86", "40.56", "-0.30"]
          - ["Llama 8B (998d)", "0.49", "0.21", "57.1", "43.72", "43.78", "+0.06"]
          - ["Llama 70B (200d)*", "0.4", "0.08", "80.0", "46.5", "46.6", "+0.1"]
    figures_description:
      - "Paired bar chart: SciERC + DocRED side-by-side, 8B vs 70B LoRA, DR 和 R-F1 delta。两个数据集上 70B 均在 best tier target zone 内。"
    analysis: >
      70B LoRA DocRED 是 best tier 的第二个关键数据点。200-doc subset 的选择（D082）
      是 pragmatic——998-doc 全量需要 ~15 小时（87s/sample × 998），200-doc 4 小时可完成。
      统计功效足以确认 DR<0.2% 和 |ΔR-F1|<0.5pp。如果 200-doc 结果 clean，可在 paper
      中报告并注明 sample size，同时在 appendix 讨论 full-set extrapolation。

  # ============================================================
  # Summary Table: Full Experiment Matrix for Best Tier Paper
  # ============================================================
  - name: "Consolidated Results — Best Tier Paper Tables"
    plan_id: "SUMMARY"
    description: "All planned experiments consolidated into paper-ready tables."
    expected_results:
      total_experiment_configs: 45
      models_tested: 4
      datasets: 3
      tasks: 2
      scales: 2
      training_regimes: 2
    result_rationale: >
      Best tier paper 需要 4 个核心 tables：(1) RE main results（3 models × 2 datasets ×
      ZS unconstrained/constrained），(2) RE LoRA results（3 models × 2 datasets，含 70B），
      (3) WikiEvents EE results（3 models × unconstrained/constrained + grammar_only ablation），
      (4) 70B scale generalization summary（ZS + LoRA，SciERC + DocRED）。这四个 tables
      覆盖论文的全部 empirical claims。Appendix 另有 beam sweep、prompt sensitivity、
      latency、seed variance、post-hoc comparison 等补充 tables。
    tables:
      - name: "Paper Table 1: RE Zero-Shot Main Results"
        columns: ["Model", "Dataset", "Setting", "DR %", "RV %", "ET %", "CF %", "R-F1 %", "E-F1 %"]
        rows:
          - ["Qwen 8B", "SciERC", "Unc.", "15.37", "1.39", "0.40", "0.08", "8.23", "31.01"]
          - ["Qwen 8B", "SciERC", "Full S1", "0.93", "0", "0", "9.90", "8.36", "30.98"]
          - ["Qwen 8B", "DocRED", "Unc.", "18.46", "29.66", "2.48", "0.10", "7.74", "58.15"]
          - ["Qwen 8B", "DocRED", "Full S1", "10.21", "0.03", "0", "2.57", "8.23", "59.37"]
          - ["Llama 8B", "SciERC", "Unc.", "13.34", "0.55", "0", "0.24", "2.68", "23.56"]
          - ["Llama 8B", "SciERC", "Full S1", "0.08", "0", "0", "6.56", "2.54", "23.49"]
          - ["Llama 8B", "DocRED", "Unc.", "26.07", "16.03", "0.13", "0.17", "5.98", "55.65"]
          - ["Llama 8B", "DocRED", "Full S1", "2.55", "0", "0", "12.02", "6.27", "55.01"]
          - ["Mistral 7B", "SciERC", "Unc.", "56.94", "0", "1.50", "56.87", "3.66", "27.28"]
          - ["Mistral 7B", "SciERC", "Full S1", "13.40", "0", "0", "1.27", "3.67", "27.46"]
          - ["Mistral 7B", "DocRED", "Unc.", "57.42", "42.35", "7.58", "24.78", "4.34", "48.51"]
          - ["Mistral 7B", "DocRED", "Full S1", "33.20", "0", "0", "0.19", "5.52", "50.59"]
          - ["Llama 70B", "SciERC", "Unc.", "6.50", "0.60", "0", "0", "11.22", "35.17"]
          - ["Llama 70B", "SciERC", "Full S1", "0", "0", "0", "3.66", "11.24", "35.14"]
          - ["Llama 70B", "DocRED", "Unc.", "15.00", "7.80", "0.02", "0.07", "13.03", "69.03"]
          - ["Llama 70B", "DocRED", "Full S1", "0", "0", "0", "7.01", "13.07", "69.05"]
      - name: "Paper Table 2: LoRA Fine-Tuned + Constrained (Scale Comparison)"
        columns: ["Model", "Dataset", "N docs", "DR Unc. %", "DR S1 %", "R-F1 Unc.", "R-F1 S1", "Delta R-F1 pp", "CF S1 %"]
        rows:
          - ["Qwen 8B", "SciERC", "551", "1.95", "0", "43.86", "43.77", "-0.09", "1.18"]
          - ["Llama 8B", "SciERC", "551", "1.11", "0.09", "45.45", "45.47", "+0.02", "0.46"]
          - ["Llama 70B*", "SciERC", "551", "0.8", "0.05", "48.2", "48.3", "+0.1", "0.6"]
          - ["Qwen 8B", "DocRED", "998", "0.76", "0.01", "40.86", "40.56", "-0.30", "0.41"]
          - ["Llama 8B", "DocRED", "998", "0.49", "0.21", "43.72", "43.78", "+0.06", "0.21"]
          - ["Llama 70B*", "DocRED", "200", "0.4", "0.08", "46.5", "46.6", "+0.1", "0.3"]
      - name: "Paper Table 3: WikiEvents Event Extraction (ZS)"
        columns: ["Model", "Setting", "EV %", "RoV %", "AC %", "CF %", "Trig-F1 %", "Ent-F1 %"]
        rows:
          - ["Qwen 8B", "Unc.", "24.0", "74.9", "0.3", "0", "11.8", "0"]
          - ["Qwen 8B", "Full S1", "0", "0", "2.1", "21.1", "13.4", "14.1"]
          - ["Llama 8B", "Unc.", "10.5", "88.8", "0.1", "0", "5.7", "0"]
          - ["Llama 8B", "Full S1", "0", "0", "3.8", "17.2", "7.5", "17.6"]
          - ["Mistral 7B", "Unc.", "37.3", "63.9", "0", "0", "2.4", "0"]
          - ["Mistral 7B", "Full S1", "0", "0", "1.3", "14.9", "3.9", "11.7"]
          - ["Mistral 7B", "Grammar", "0", "64.0", "13.8", "1.1", "3.4", "11.9"]
    figures_description:
      - "Figure 1 (Intro/Method): Architecture diagram — ontology schema → compiler → grammar CFG + semantic TypeConstraintProcessor → bitwise AND → constrained LLM decoding。标注 enabling dependency arrow from grammar to semantic。"
      - "Figure 2 (§3 Violation Landscape): Heatmap of per-relation DR by model (SciERC 7 relations + DocRED top-10 relations)。Color intensity = violation rate，with tightness τ̄ annotated per relation。"
      - "Figure 3 (§5 Results): DR reduction waterfall across settings (Unconstrained → Grammar → Semantic → Full S1)，4-panel grid for SciERC/DocRED × Qwen/Llama。"
      - "Figure 4 (§5.4 EE): Stacked violation bar chart for WikiEvents (3 models × unc/grammar/S1)。Visual dominance of RoV in unconstrained，clean elimination in Full S1。"
      - "Figure 5 (§5.5 or Appendix): Scale-neutral pattern plot — 8B vs 70B，DR and R-F1 delta，confirming model-size-invariance。"
    analysis: >
      Best tier paper 的 table/figure 密度目标是 ~1 table + ~1 figure per page (8 pages)。
      4 tables + 5 figures = 9 visual elements 在 8 页正文中偏满——建议将 beam sweep 和
      prompt sensitivity tables 移入 appendix，正文保留 3 tables + 4 figures。
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c7a8b261-10c2-4876-96b4-4e52c2e08078",
  "isSidechain": false,
  "requestId": "req_011CbH4VqQkZ8PeKXcHzWM6U",
  "type": "assistant",
  "uuid": "23e0c4c4-3f28-41ef-aff3-e3901a65dd2d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6",
  "sessionId": "b82a3282-ed21-4676-9e91-4d9b245dd612",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HAEshrQDoZ9YwF3ZVSQZq4",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2591,
      "cache_read_input_tokens": 82654,
      "output_tokens": 17460,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2591,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 17460,
          "cache_read_input_tokens": 82654,
          "cache_creation_input_tokens": 2591,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2591
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：Reviewers 认可 violation landscape + composable two-layer architecture 为双重贡献；cross-task (RE+EE) 证据链完整；70B LoRA 结果干净 核心假设：['Violation landscape study 被视为独立 em…",
  "leafUuid": "23e0c4c4-3f28-41ef-aff3-e3901a65dd2d",
  "sessionId": "b82a3282-ed21-4676-9e91-4d9b245dd612"
}
```

---

### Runtime record

_source line 41_

```json
{
  "type": "ai-title",
  "aiTitle": "EMNLP 2026 Conference Main Submission Evaluation",
  "sessionId": "b82a3282-ed21-4676-9e91-4d9b245dd612"
}
```

---

### Runtime record

_source line 42_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：Reviewers 认可 violation landscape + composable two-layer architecture 为双重贡献；cross-task (RE+EE) 证据链完整；70B LoRA 结果干净 核心假设：['Violation landscape study 被视为独立 em…",
  "leafUuid": "23e0c4c4-3f28-41ef-aff3-e3901a65dd2d",
  "sessionId": "b82a3282-ed21-4676-9e91-4d9b245dd612"
}
```

---

### Runtime record

_source line 43_

```json
{
  "type": "ai-title",
  "aiTitle": "EMNLP 2026 Conference Main Submission Evaluation",
  "sessionId": "b82a3282-ed21-4676-9e91-4d9b245dd612"
}
```

---
