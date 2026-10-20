# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义： 含义：所有核心假设经受审稿检验；CF 被接受为 honest limitation 而非致命缺陷；novelty 认定充分 核心假设：["审稿人接受 'nea

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 24
- **Recorded user turns:** 1
- **Tool calls:** 3
- **Original source:** `logs/chats/exported-trajectories/account-1/3bf11c38-e586-47ea-b7d9-62bfeddfd8ee.jsonl`
- **Structured JSON:** [`8d5b7dace1eca174e0cd.json`](../../sessions/8d/8d5b7dace1eca174e0cd.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-14T20:53:33.146Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-14T20:53:33.146Z",
  "sessionId": "3bf11c38-e586-47ea-b7d9-62bfeddfd8ee",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：\n\n含义：所有核心假设经受审稿检验；CF 被接受为 honest limitation 而非致命缺陷；novelty 认定充分\n核心假设：[\"审稿人接受 'near-complete' framing（DR 0.93% SciERC / 2.55% Llama DocRED 足够接近 0%）\", 'CF trade-off 被视为 interesting finding（type system ambiguity analysis 被认可为独立贡献）', '2 模型 × 2 数据集被接受为 sufficient generalization evidence', 'zero-shot 低 F1 framing 无异议（F1 作为 control variable 而非 optimization target）', 'tightness × RV baseline dual-factor 被视为比单因素 tightness 更深的 insight', \"enabling dependency 机制（grammar enables semantic）被认为比 'bitwise AND' 有方法论深度\"]\n关键指标范围：{'arr_overall': [3.5, 4.0], 'arr_soundness': [3.5, 4.0], 'arr_novelty': [3.0, 3.5], 'major_weaknesses_per_reviewer': [0, 1], 'reviewers_flagging_cf_fatal': [0, 0], 'reviewers_flagging_novelty_insufficient': [0, 1], 'reviewers_accepting_zero_shot_framing': [2, 3], 'acceptance_probability_pct': [55, 75], 'revision_effort_days': [3, 7]}\n叙事方向：原始 framing 完全成立。Title 'Near-Complete Type-Valid IE' 无需修改。4 个 core claims 全部保留原始强度。CF 在 §5.3 作为 analysis finding + §7 limitation 双重定位即可。Violation landscape (Claim 1) + prompt insufficiency (Claim 2) 作为独立贡献获认可。Cross-model subsection 证明 generalizability。Post-hoc baseline 多维对比 (recall preservation + information coverage) 令审稿人信服。论文以 'systematic constraint enforcement framework with principled decidability taxonomy' 叙事通过。\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: schema_semantic_constrained_ie\nvenue: EMNLP 2026\nfocus: All 20 experiments complete with 2 models × 2 datasets full matrix. Key narrative updates: D014 dual-factor tightness × RV baseline, D013 post-hoc multi-dimensional framing, D012 bootstrap CI (dataset-dependent F1 impact), cross-model generalization confirmed but with model-specific effects (Llama E-F1 decline, parse failure increase, CF=12.02%). Paper has complete related work (42 refs), discussion paragraphs, and cross-model subsection draft.\n\n## paper_framing.md\n\n# OntoCoDec — Paper Framing\n\n## Target Venue\nEMNLP 2026 (ARR submission May 25, 2026)\n\n## Title\nOntoCoDec: Near-Complete Type-Valid Information Extraction via Compiled Ontology Constraints\n(Note: \"Guaranteed\" dropped per Reviewer — S1 DR=0.93%, S2 DR=0.97%, neither achieves 0%. \"Near-Complete\" is honest and defensible.)\n\n## Core Insight\nLLM-based IE systems produce systematic ontology constraint violations concentrated in specific relation types. Prompt-level intervention (schema-informed prompting) reduces violations by ~62% but cannot eliminate them — certain relation types retain 25-30% violation rates even with explicit constraint descriptions. OntoCoDec provides **near-complete elimination (DR 15.4%→0.93%, ↓94%) at zero or positive F1 impact** through automatic ontology-to-decoder constraint compilation with two complementary layers.\n\n**Phase 2 confirmed (D012 bootstrap CI, v2 fix)**: Grammar+Semantic dual-layer constrained decoding reduces domain/range violations by 94%, eliminates entity-type and relation-vocabulary violations entirely (→0%). F1 impact is **dataset-dependent**:\n- SciERC: Rel F1 neutral (+0.13pp, p=0.58), Ent F1 neutral (-0.03pp, p=0.53)\n- DocRED: Rel F1 **significantly improved** (+0.50pp, p<0.001, 95% CI [+0.23, +0.81]); Ent F1 **significantly improved** (+1.23pp, p<0.001, 95% CI [+0.94, +1.55])\n- Mechanism: grammar 消除 OOV relation names (DocRED RV 29.66%→0.03%) + 非标 entity types (ET 2.48%→0%)。all_set F1 方法下 OOV=FP → fewer FP → higher precision/F1。SciERC baseline RV/ET 已很低，效果不显著。\n- **Grammar 层是 F1 提升的唯一来源**: grammar_only Ent F1=59.38% ≈ full_s1 59.37% (Δ+0.01pp, p=0.66)。Semantic 层对 F1 无额外贡献，专注 DR reduction。\n\n## Core Claims\n\n### Claim 1 (Empirical): Violation Landscape\nLLM-based IE systems violate ontology type constraints at non-trivial rates (15.4% per-triple on SciERC, 18.7% on DocRED). Violations are **not uniformly distributed** — they concentrate on relation types with tight domain/range constraints (Feature-of 33.5%, Compare 42.4%) while loose-constraint relations show near-zero violation (Used-for 0.8%).\n\n**Key insight**: Violation rate is driven by **constraint tightness**, not ontology size. A small ontology with tight constraints can produce more violations than a large ontology with loose constraints.\n\n**D014 修订**: DR reduction ceiling 由 **tightness × model RV baseline** 共同决定，非 tightness 单因素。Llama DocRED DR↓90.2% vs Qwen DR↓44.7%（同一 ontology τ̄=0.842）。机制：Qwen RV=29.66% >> Llama RV=16.03% → grammar 层将 OOV triples 强制匹配有效关系名 → 揭露大量 latent DR violations → 残余 DR 更高。这是比单一 tightness 更深的 insight。\n\n**Evidence**: SciERC (7 relations) 15.4%; DocRED (96 relations) 18.7% — comparable rates despite 14× ontology size difference. Schema-informed prompt on DocRED only achieves DR↓32% (vs SciERC ↓62%), confirming **prompt-level intervention scales poorly with ontology complexity**.\n\n### Claim 2 (Empirical): Prompt Insufficiency\nSchema-informed prompting (explicitly describing domain/range constraints in the prompt) reduces but does not eliminate violations:\n- Overall: 15.4% → 5.78% (-62.4%), still above 5%\n- Per-relation: Compare 42.4% → 27.6%, Evaluate-for 24.1% → 29.9% (**worse**)\n- Prompt intervention is unreliable at the per-relation level — some relations improve, one regresses\n\n**Narrative**: This is NOT about \"5.78% barely above 5%\". The story is: **prompt-level intervention is fundamentally unreliable as a guarantee mechanism**. It works statistically but cannot provide per-instance compliance. Three specific relation types retain >10% violation rates with schema-informed prompts. For safety-critical IE (biomedical, legal, regulatory), statistical reduction is insufficient — guaranteed compliance is required.\n\n### Claim 3 (Methodological): Composable Constraint Framework\nOntoCoDec automatically compiles IE ontology schemas into two composable constraint layers:\n1. **Grammar layer** (XGrammar): JSON structure + type vocabulary constraints (CFG-expressible)\n2. **Semantic layer** (TypeConstraintProcessor): Cross-field domain/range constraints via stateful entity registry + dynamic logit masking\n\nThe two layers are **complementary with enabling dependency**: grammar ensures every generated relation type is in the valid vocabulary, which enables the semantic layer to look up and enforce domain/range rules for that type. Without grammar, the semantic layer encounters unknown relation types and cannot enforce constraints (explaining why semantic_only achieves only ↓24% vs full_s1 ↓94%). This is NOT \"synergistic\" (mutual amplification) — grammar is a prerequisite for semantic, not vice versa.\n\nThe two layers compose via bitwise AND of token masks. Recommended framing: \"Grammar and semantic constraints compose via bitwise AND with an enabling dependency: grammar ensures structural validity, enabling semantic constraints to enforce domain/range rules. When constraint tightness creates empty intersection between layers, the system degrades gracefully to grammar-only constraints, maintaining structural validity as a guaranteed floor.\"\n\n**Graceful degradation + Fallback 频率量化** (D008 + Reviewer 发现):\nWhen $M_{semantic} \\cap M_{grammar} = \\emptyset$, the system falls back to grammar-only control.\n\n**关键量化数据（Reviewer 从日志挖掘）**:\n- Llama DocRED full_s1: **32,921 次 fallback / 577 docs = ~57 次/doc**\n- Llama SciERC full_s1: **5,882 次 fallback / 550 docs = ~10.7 次/doc**\n- DocRED fallback 频率是 SciERC 的 **5.3×**\n- Qwen DocRED fallback 率未知（日志当时无 fallback logging，需估算）\n\n**这直接解释了 DocRED DR 残余 10.19% vs SciERC 0.93%**: 更多 token 位置退化为 grammar-only → grammar-only 的 DR 已知为 26.17% → 高 fallback = 高残余 DR。\n\n**论文建议**: 在 §5 tightness 段报告 fallback 率，定义 \"Constraint Coverage\" 指标（semantic masking 实际生效的 token 比例）。这把 \"10.19% DR 残余\" 从弱点变成可量化分析的 finding。Frame as \"engineering robustness\" in §4; fallback 频率 + tightness 作为 §5 定量分析。\n\n**Decidability taxonomy**: Constraints classified by prefix-decidability:\n- (a) Purely local: entity type ∈ vocabulary (grammar layer)\n- (b) Prefix-decidable with state: relation argument types compatible with domain/range (semantic layer, requires entity registry)\n- (c) Truly non-local: forward coreference — out of scope for forward-only decoding\n\n### Claim 4 (Methodological): S1 vs S2 Decoding Strategies — Architectural Ablation\n- S1 (single-pass): Both layers applied throughout generation. **Recommended primary strategy** — simpler, slightly better metrics across the board.\n- S2 (two-pass): Pass 1 extracts entities (grammar-only), Pass 2 generates relations with input-dependent grammar compiled from Pass 1 entities.\n\n**S2 full results (551/551 SciERC)**: DR 0.97% (vs S1 0.93%), CF 8.03% (vs S1 9.9%), R-F1 8.03% (vs S1 8.36%). S2 does NOT solve CF — the 1.87pp reduction is not significant. S2 also slightly worse on DR and F1. **S2 is an architectural variant demonstrating framework flexibility, not a CF solution.** Position in paper as ablation (Section 5 or Appendix), not as a core contribution.\n\n⚠️ **Do NOT cite pilot50 DR=0% as S2 evidence** — small-sample artifact; full run shows DR=0.97%. Per-relation S2 DR is worse than S1 on Compare (4.6% vs 2.82%), Part-of (1.25% vs 0%), Used-for (0.12% vs 0%).\n\n## Anticipated Reviewer Concerns\n\n### C1: \"5.78% is barely above 5% — threshold is arbitrary\"\n**Response**: Don't argue about the threshold. Argue about per-relation distribution: Compare (27.6%), Evaluate-for (29.9%), Feature-of (11.3%) have double-digit violation rates with schema-informed prompt. The value proposition is per-relation guaranteed compliance, not overall statistical rate.\n\n### C2: \"Why not just post-hoc filter?\"\n**Response (D013, 实验结果已出)**:\n\nPost-hoc filtering 实验结果：post-hoc F1 > OntoCoDec F1（SciERC 8.63 vs 8.36, DocRED 9.61 vs 8.24）——因 low F1 regime 下移除 FP 大幅提升 precision。\n\n**论文 framing（不以 F1 论高低，多维对比）**:\n1. **Recall 维度（核心论点）**: OntoCoDec recall 上升 (SciERC +0.20pp, DocRED +0.56pp) = 概率质量重分配到合法 token 生效。Post-hoc recall 下降 (SciERC -0.72pp, DocRED -1.06pp) = 正确 triple 被误删。\n2. **Information coverage**: DocRED post-hoc 丢弃 **48.1%** triples（近半数信息丢失），SciERC 16.8%。OntoCoDec 保留全部 triple slots。\n3. **Operational**: OntoCoDec 产出即合规、无需后处理、支持流式。Post-hoc 需额外管线、不适用实时场景。\n4. **Precision trade-off（诚实承认）**: \"Post-hoc achieves higher precision by removing a large fraction of triples, many of which are incorrect. This trades information coverage for precision — valid when FP are costly, but inadequate when completeness matters.\"\n\n数据表：SciERC post-hoc rejection 16.8%, OntoCoDec recall 11.60 vs post-hoc 10.68; DocRED post-hoc rejection 48.1%, OntoCoDec recall 10.02 vs post-hoc 8.40。\n\n**Reviewer 补充发现（D013 后）**:\n5. **ET 残余**：post-hoc 只删 triples 不改 entity list，残余 ET=0.4% (SciERC) / 2.47% (DocRED)。OntoCoDec ET=0%。Post-hoc 无法解决 entity type 违规。\n6. **127 个被删 TP (DocRED)**：过滤前 TP=1137，过滤后 TP=1010。丢失的 127 个 TP（11.2%）是正确提取但 entity type 违规的 triple。OntoCoDec 通过生成时强制合法 type 保留这些 TP——\"prevent vs detect\" 核心论据的具体数据。\n7. **OntoCoDec+post-hoc 组合**（future work idea）：先 constrain 再 filter 残余 DR。低优先级，May 19 前不做。\n\n### C3: \"Bitwise AND of two masks is not novel\"\n**Response**: The novelty is not the AND operation — it's (a) the automatic compilation from ontology definitions (zero-code schema compliance), (b) the stateful entity registry enabling cross-field constraints during autoregressive generation, (c) the decidability taxonomy providing theoretical guidance, and (d) the systematic violation landscape measurement motivating the approach.\n\n### C4: \"Evaluate-for violation rate increases with schema-informed prompt\"\n**Response (prior-constraint conflict framework)**: Evaluate-for has 23/36 valid pairs; Method→Task is invalid for Evaluate-for but natural in the LLM's distributional prior (\"Method X evaluates for Task Y\" is semantically plausible). Schema-informed prompting creates a **prior-constraint conflict**: the model learns to avoid Method→Task for Evaluate-for (reducing count 133→87, -34.6%), but the remaining instances are harder boundary cases where the model's type assignment strategy becomes less stable. This is not just \"harder instances\" — it's an active interference between prompt-level constraint signals and the model's learned type associations.\n\n**This strengthens the paper's claim**: prompt-level intervention is not merely insufficient but potentially **counterproductive** for specific constraint configurations. Decoding-time enforcement avoids this issue entirely — it operates on logits, not on the model's reasoning process, so there is no prior-constraint conflict.\n\n### C5: \"Only tested on one model (Qwen3-8B)\"\n**Response**: Cross-model validation DONE. Llama-3.1-8B 零代码修改：\n- SciERC: DR 13.34%→0.08% (↓99.4%), F1-neutral (-0.14pp)\n- DocRED unconstrained: DR 26.15%, RV 16.03%, R-F1 5.98% (parse failures 6.8% vs Qwen 1.2%)\n- DocRED full_s1: 🔄 ETA ~20:19 UTC\n\n**Cross-model claim 指导（Reviewer 专项评估）**:\n- ✅ 可声明：\"OntoCoDec generalizes across model families without code modification\"（程序性事实，铁证）\n- ❌ 不可声明：\"consistently achieves the same reduction rate\"（仅 2 模型，不足以量化声明）\n- **RV↓DR↑ 正交性 finding**: Llama RV baseline 低(16%) 但 DR baseline 高(26%)，反向于 Qwen。证明两层约束解决正交 failure modes——vocabulary compliance ≠ semantic compliance。应作为 §5 cross-model 独立 finding 展开。\n- **Parse failure 偏差**: checker skip parse failures (不计入 F1)，Llama 68/998=6.8% vs Qwen 12/998=1.2%。偏差方向保守（不利于 constrained），不威胁 claim。但需 footnote 披露 + cross-model 表增加 parse failure rate 行。\n- **Llama SciERC CF=6.56%**: 比 Qwen 同量级更高，non-local constraint 问题在 Llama 上更突出，limitations 提及。\n- 等 llama_docred_full_s1 出来后定最终 claim 措辞。\n\n### C6: \"Constrained decoding degrades generation quality (CRANE, Structure Snowballing)\"\n**Response**: OntoCoDec's semantic constraints are narrower than full grammar constraints — only type tokens are masked, free text is unconstrained. **D012 Bootstrap CI (10000×, v2 fix) 结果**:\n- SciERC: Rel F1 +0.13pp (p=0.58), Ent F1 -0.03pp (p=0.53) → **F1-neutral**\n- DocRED: Rel F1 +0.50pp (p<0.001, CI [+0.23, +0.81]), Ent F1 +1.23pp (p<0.001, CI [+0.94, +1.55]) → **双双显著提升**\n- 机制：grammar 消除 OOV relation names + 非标 entity types → all_set 方法下减少 FP → precision 提升。Grammar 是 F1 提升的唯一来源（grammar_only Ent F1=59.38% ≈ full_s1 59.37%, Δ=0.01pp, p=0.66）。Semantic 层对 F1 无额外贡献。\n- Frame as: \"Constraint enforcement preserves or improves extraction quality: F1-neutral on SciERC; statistically significant Rel F1 and Entity F1 improvement on DocRED (p<0.001).\"\n- 不升级为 core claim，但如实报告 significance + 机制归因。Note: S2 shows marginally lower F1 and fewer triples (1644 vs 1729) — two-pass does not improve quality.\n\n### C7: \"Your method trades DR violations for CF violations (cross-field consistency)\"\n**Response**: Both S1 and S2 show elevated CF (per-triple rate ~8-10%). This is an inherent limitation of per-relation independent type enforcement. Must be proactively reported as a limitation. Defense:\n\n**CF 子类型分析（根因已确认）**：\n- **EVR（entity-vs-relation type drift）**: 占 CF 的 >90%。同一 entity 在 entity list 和 relation triple 中被赋予不同 type。S1: 245 entities (7.34%), S2: 178 entities (5.54%, -27%)\n- **Within-rel（同 entity 跨 relation type 不一致）**: S1: 10 (0.36%), S2: 18 (0.72%)\n- S2 减少 EVR 但增加 within-rel——trade-off 更复杂，不是单纯好/差\n\n**Top 冲突模式**: Generic↔OtherScientificTerm (60次), Material↔OtherScientificTerm (28次), Material↔Method (20次)。**这些是 SciERC type system 固有的语义边界模糊区**——同一术语在不同学术语境下确实可以被合理归类为不同 type。CF 在相当程度上是 type system 模糊性的体现，非纯粹的方法缺陷。\n\n**论证层次**：\n1. DR violations = structurally invalid triples（下游系统不可用）→ hard constraint\n2. CF violations = same entity gets different types across relations → individual triples remain type-valid, only cross-triple consistency broken → soft preference\n3. CF 的根因是 type system 语义边界模糊 + per-relation 独立 enforcement，非 bug\n4. Future work: cross-relation global consistency pass (entity-level type consensus before relation-specific enforcement)\n\n**机制归因（口径对账确认）**：grammar_only CF=0.08%（与 unconstrained 持平），full_s1 CF=9.90%，full_s2 CF=8.03%。**CF 100% 由 semantic 层引入，grammar 层无贡献。** 这为 \"CF 是 semantic type enforcement 的系统性副作用\" 提供干净的消融证据。\n\n**论文数字口径**：CF rate 用 violation_checker 口径（denominator=total_entities，与 DR/RV/ET 一致）。分析段落额外给 entity-level EVR 率 + 受影响样本比例。注意：analyze_cf 脚本的 EVR/WR 两维度不是独立的（WR⊂EVR），论文中不要作为两个独立维度报告。\n\n**Do NOT hide this data.** Proactive disclosure + severity distinction + root cause analysis + type ambiguity evidence + 消融归因 = 最强防御策略。\n\n### C8: \"Absolute F1 is too low (~8%) — results are not meaningful\"\n**Response**: This is a zero-shot extraction setting (no training data, no fine-tuning). Low F1 is expected — supervised SOTA on SciERC relation F1 is ~40-50%. Our contribution is the constraint enforcement method, not extraction quality. F1 is a control variable verifying constraints don't degrade quality, not an optimization target. Recommended framing: \"We evaluate in a zero-shot setting to demonstrate that our constraint enforcement method works without task-specific training. F1 is reported to verify that constraint enforcement does not degrade extraction quality, not as a claim of state-of-the-art performance.\"\n\n## Paper Structure (Draft)\n1. Introduction: Violation landscape motivation + composable constraint framework overview\n2. Background: Grammar-constrained decoding (XGrammar) + IE ontology structure\n3. Violation Landscape Study (Phase 0 empirics — independent contribution)\n4. OntoCoDec Framework: Compiler + TypeConstraintProcessor + S1/S2 strategies\n5. Experiments: Constrained vs unconstrained vs post-hoc vs prompt-based\n6. Related Work: 5 constraint paradigms (grammar, vocabulary, structural, type-checking, ontology)\n7. Conclusion\n\n## Claim Calibration (per Reviewer assessment)\n\n**Safe to claim (sufficient evidence from Phase 2)**:\n- \"First systematic study of ontology constraint violations in LLM-based IE\"\n- \"Violation rate correlates with constraint tightness, not ontology size\" (D014: DR reduction ceiling 由 tightness × model RV baseline 共同决定)\n- \"Grammar+semantic constrained decoding eliminates 94% of DR violations at zero F1 cost\" ✅ Phase 2 confirmed\n- \"Two-layer architecture provides complementary coverage — grammar enables semantic\" ✅ Ablation confirmed\n- \"Prompt-level intervention scales poorly with ontology complexity\" ✅ SciERC ↓62% vs DocRED ↓32%\n\n**Claim with caution**:\n- \"Near-complete type-valid IE\" — S1 0.93%, S2 0.97% residual, not truly 0%. Title updated to \"Near-Complete\"\n- \"Principled framework applicable to arbitrary IE ontologies\" — validated on 2 datasets + 1 model only\n- \"F1 improvement\" — SciERC: not significant (p=0.58), frame as F1-neutral; DocRED: significant (+0.50pp, p<0.001), 可报告但不升级为 core claim，归因于 OOV elimination 而非约束解码本身的提升\n- \"CF reveals type system ambiguity\" — 可在 §5.3 作为 analysis finding 展开（Generic↔OtherScientificTerm 等模式有独立 insight 价值），但 §7 必须同时保留 CF 作为 limitation + future work。**两处都要有，缺一不可。** 不能暗示\"因为是 type ambiguity 所以 CF 可接受\"\n\n**Do NOT claim**:\n- \"General infrastructure for IE\" — only zero-shot extraction validated\n- \"State-of-the-art\" — F1 is control variable, not optimization target (see C8)\n- \"Synergistic effect\" — mechanism is enabling dependency, not mutual amplification (see Claim 3)\n- \"S2 solves CF\" or \"S2 mitigates Structure Snowballing\" — data shows S2 ≈ S1 on all metrics; position as architectural variant only\n- \"Pilot50 DR=0%\" — small-sample artifact, full S2 has DR=0.97%\n- \"Grammar-first invariant\" 作为独立 claim — 证据不足（仅 1 次崩溃触发，实现是 fallback 非形式化保证）。写入 §4 方法论设计原则（1-2 句），不升级为 claim\n- \"Robust dual-layer composition across schema complexities\" — 等 DocRED 完成。最终如 fallback ≤5/998，可写经验性陈述，不做泛化 claim\n\n## Risk Ranking (ordered by reject probability)\n\n1. **CF violation trade-off under-addressed** (MEDIUM-HIGH): S1 9.9%, S2 8.03% — both elevated. **S2 confirmed: does NOT solve CF.** This is the #1 attack surface. Mitigated by proactive disclosure + severity distinction + root cause analysis (C7). Must be reported as explicit limitation with future work direction (global entity-type consensus).\n2. ~~**Single model limitation**~~ (RESOLVED): Llama-3.1-8B SciERC ✅ (DR↓99.4%) + DocRED ✅ (DR↓90.2%). 2 模型 × 2 数据集全矩阵完成。\n3. **Novelty perception** (MEDIUM): \"PLDI'25 for code → OntoCoDec for IE\" attack line. Must argue IE constraint structure differs fundamentally.\n4. ~~**DocRED Phase 2 weak**~~ (RESOLVED → reframed as D014): Qwen DR↓44.7%, Llama DR↓90.2% — both substantial. Weaker Qwen reduction explained by RV baseline interaction (D014), not method failure.\n5. ~~**Phase 2 F1 drop**~~ (RESOLVED): F1 confirmed neutral (SciERC) or positive (DocRED, p<0.001). Bootstrap CI D012 confirms. No longer a risk.\n\n## Critical Path to EMNLP Submission (May 25)\n\n- **May 13-14**: Phase 0 + Phase 1 + Phase 2 SciERC ✅\n- **May 14**: Phase 2 DocRED 4-way ablation ✅ + Llama SciERC cross-model ✅ + Dream 完成 (3/6)\n- **May 14-15**: Llama DocRED 2 组实验 ✅ + Checker 修正 ✅ + post-hoc baseline ✅ + bootstrap CI ✅ + related work ✅\n- **May 14-15**: D014 tightness claim 修订 + §5 cross-model subsection + abstract/conclusion 修正 (Agent 执行中)\n- **May 15-17**: 全文校对 + Discussion 整合 + 最终数字确认\n- **May 19**: 内部稿 → submit_paper_to_review\n- **May 19-24**: Review 修改 + 最终提交\n\n**当前瓶颈**: D014 论文修订（tightness claim + cross-model subsection + E-F1 claim limitation）\n\n## Status\n- Phase 0 SciERC: ✅ Complete (minimal + schema-informed)\n- Phase 0 DocRED: ✅ Complete (minimal 18.7% DR + schema-informed 12.8% DR)\n- Phase 1 Compiler: ✅ Complete (grammar + semantic layers integrated)\n- Phase 2 SciERC (5 configs): ✅ Complete (S1 DR↓94% F1-neutral, S2 降级为 ablation)\n- Phase 2 DocRED (4 configs): ✅ Complete (full_s1 DR↓45%, grammar ET/RV→0%)\n- Llama SciERC cross-model: ✅ Complete (DR↓99.4%, F1-neutral, 零代码修改)\n- Llama DocRED cross-model: ✅ Complete (full_s1 DR↓90.2%, unconstrained DR=26.07%)\n- Checker v2 (D011): ✅ Fixed (ET triple-counting → unique entity dedup)\n- Bootstrap CI (D012): ✅ Fixed + confirmed (entity filter bug resolved)\n- Post-hoc baseline (D013): ✅ Complete (multi-dimensional framing)\n- Related work: ✅ 42 bib entries, 4 additions merged\n- Dream 6/6 actions: ✅ All complete\n- CF violation analysis: ✅ Confirmed inherent limitation (S1 9.9% SciERC / 2.57% DocRED / 12.02% Llama DocRED)\n- D014 tightness revision: 🔄 Agent executing (tightness × RV baseline dual-factor)\n\n\n## registry (completed experiments)\n\n- exp_id: mvp_phase0_violation_rate\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_triples: 1724\n    total_entities: 2474\n    json_parse_rate: 1\n    entity_type_violation_rate: 0.004\n    relation_vocabulary_violation_rate: 0.0139\n    domain_range_violation_rate: 0.1537\n    cross_field_consistency_violation_rate: 0.0008\n    go_nogo_metric: 0.1537\n    entity_f1: 0.3101\n    relation_f1: 0.0823\n    per_relation:\n      Used-for:\n        total: 787\n        dr_violations: 6\n        rate: 0.0076\n      Conjunction:\n        total: 32\n        dr_violations: 0\n        rate: 0\n      Hyponym-of:\n        total: 124\n        dr_violations: 18\n        rate: 0.1452\n      Evaluate-for:\n        total: 133\n        dr_violations: 32\n        rate: 0.2406\n      Part-of:\n        total: 72\n        dr_violations: 18\n        rate: 0.25\n      Feature-of:\n        total: 486\n        dr_violations: 163\n        rate: 0.3354\n      Compare:\n        total: 66\n        dr_violations: 28\n        rate: 0.4242\n- exp_id: mvp_phase0_violation_rate_docred\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_docs: 998\n    parsed_docs: 962\n    json_parse_rate: 0.964\n    total_entities: 19099\n    total_triples: 16540\n    entity_type_violation_rate: 0.075\n    relation_vocabulary_violation_rate: 0.289\n    domain_range_violation_rate: 0.187\n    cross_field_consistency_violation_rate: 0.0008\n    go_nogo_metric: 0.187\n    fuzzy_matches: 126\n    top_dr_violations_by_rate:\n      P35_head_of_state: 1\n      P710_participant: 0.919\n      P172_ethnic_group: 0.875\n    top_dr_violations_by_count:\n      P31_instance_of:\n        violations: 322\n        total: 533\n        rate: 0.604\n      P1001_applies_to_jurisdiction:\n        violations: 264\n        total: 594\n        rate: 0.444\n      P1344_participant_in:\n        violations: 194\n        total: 312\n        rate: 0.622\n- exp_id: mvp_phase0_scierc_schema\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    domain_range_violation_rate: 0.0578\n    relation_vocabulary_violation_rate: 0.003\n    entity_type_violation_rate: 0\n    total_violation_rate: 0.0253\n    go_nogo_metric: 0.0578\n    total_triples: 1661\n    vs_minimal_dr_reduction: -0.624\n    per_relation:\n      Used-for:\n        rate: TBD\n      Feature-of:\n        delta_pp: -22.3\n      Part-of:\n        delta_pp: -22.5\n      Compare:\n        delta_pp: -14.8\n      Evaluate-for:\n        delta_pp: 5.8\n    mcnemar_all_significant: true\n- exp_id: mvp_phase0_docred_schema\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_documents: 998\n    documents_checked: 943\n    parse_failures: 55\n    json_parse_rate: 0.9449\n    total_entities: 19524\n    total_triples: 16782\n    entity_type_violations: 119\n    entity_type_violation_rate: 0.0061\n    relation_vocabulary_violations: 3090\n    relation_vocabulary_violation_rate: 0.1841\n    relation_fuzzy_matches: 85\n    domain_range_violations: 2154\n    domain_range_violation_rate: 0.1284\n    cross_field_consistency_violations: 29\n    cross_field_consistency_violation_rate: 0.0015\n    total_violations_any: 5392\n    total_violation_rate: 0.1485\n    go_nogo_metric_dr: 0.1284\n- exp_id: phase2_scierc_grammar_only\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_samples: 551\n    total_triples: 1725\n    total_entities: 2474\n    json_parse_rate: 1\n    entity_type_violation_rate: 0\n    relation_vocabulary_violation_rate: 0\n    domain_range_violation_rate: 0.1484\n    cross_field_consistency_violation_rate: 0.0008\n    entity_f1: 0.3098\n    entity_precision: 0.2598\n    entity_recall: 0.3837\n    relation_f1: 0.0823\n    relation_precision: 0.0643\n    relation_recall: 0.114\n    checker_version: fixed_20260514_v2 (strip + alias + unique_et)\n- exp_id: phase2_scierc_semantic_only\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_samples: 551\n    total_triples: 1726\n    total_entities: 2474\n    json_parse_rate: 1\n    entity_type_violation_rate: 0.004\n    relation_vocabulary_violation_rate: 0.0151\n    domain_range_violation_rate: 0.1165\n    cross_field_consistency_violation_rate: 0.0271\n    entity_f1: 0.3101\n    entity_precision: 0.2605\n    entity_recall: 0.3831\n    relation_f1: 0.0815\n    relation_precision: 0.0637\n    relation_recall: 0.1129\n    checker_version: fixed_20260514_v2 (strip + alias + unique_et)\n- exp_id: phase2_scierc_full_s1\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_samples: 551\n    total_triples: 1729\n    total_entities: 2474\n    json_parse_rate: 1\n    entity_type_violation_rate: 0\n    relation_vocabulary_violation_rate: 0\n    domain_range_violation_rate: 0.0093\n    cross_field_consistency_violation_rate: 0.099\n    entity_f1: 0.3098\n    entity_precision: 0.2598\n    entity_recall: 0.3837\n    relation_f1: 0.0836\n    relation_precision: 0.0654\n    relation_recall: 0.116\n    checker_version: fixed_20260514_v2 (strip + alias + unique_et)\n- exp_id: phase2_scierc_unconstrained\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    json_parse_rate: 1\n    entity_f1: 0.3101\n    entity_precision: 0.2605\n    entity_recall: 0.3831\n    relation_f1: 0.0823\n    relation_precision: 0.0644\n    relation_recall: 0.114\n    entity_type_violation_rate: 0.004\n    relation_vocabulary_violation_rate: 0.0139\n    domain_range_violation_rate: 0.1537\n    cross_field_consistency_violation_rate: 0.0008\n    total_triples: 1724\n    total_entities: 2474\n    total_samples: 551\n    checker_version: fixed_20260514_v2 (strip + alias + unique_et)\n- exp_id: phase2_s2_pilot50\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    domain_range_violation_rate: 0.0205\n    relation_vocabulary_violation_rate: 0\n    relation_f1: 0.1008\n    samples: 50\n    predicted_relations: 146\n    true_positives: 13\n    gold_relations: 112\n    entity_f1_approx: 0.29\n    note: 'DR 修正: 原值 0 来自 dryrun (n=25 triples)。实际 pilot50 DR=3/146=2.05% (来自 violation_report_s2_pilot50.json)。'\n- exp_id: mvp_phase0_docred_schema_r2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: phase2_scierc_full_s2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_samples: 551\n    total_triples: 1644\n    total_entities: 2228\n    json_parse_rate: 1\n    entity_type_violation_rate: 0\n    relation_vocabulary_violation_rate: 0\n    domain_range_violation_rate: 0.0097\n    cross_field_consistency_violation_rate: 0.0803\n    entity_precision: 0.2797\n    entity_recall: 0.3712\n    entity_f1: 0.319\n    relation_precision: 0.064\n    relation_recall: 0.1078\n    relation_f1: 0.0803\n    checker_version: fixed_20260514_v2 (strip + alias + unique_et)\n- exp_id: phase2_docred_grammar_only\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    documents_checked: 985\n    parse_failures: 13\n    total_entities: 20150\n    total_triples: 17341\n    entity_type_violation_rate: 0\n    relation_vocabulary_violation_rate: 0.0003\n    domain_range_violation_rate: 0.2617\n    cross_field_consistency_violation_rate: 0.0007\n    relation_f1: 8.31\n    relation_precision: 7.06\n    relation_recall: 10.12\n    entity_f1: 59.38\n    entity_precision: 58.47\n    entity_recall: 60.32\n    unrecognized_relations: 5\n    f1_method: all_set\n    checker_version: fixed_20260514_v2 (strip + alias + unique_et)\n- exp_id: phase2_docred_full_s1\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    documents_checked: 987\n    parse_failures: 11\n    total_entities: 20187\n    total_triples: 17341\n    entity_type_violation_rate: 0\n    relation_vocabulary_violation_rate: 0.0003\n    domain_range_violation_rate: 0.1021\n    cross_field_consistency_violation_rate: 0.0257\n    entity_f1: 59.37\n    entity_precision: 58.45\n    entity_recall: 59.63\n    relation_f1: 8.23\n    relation_precision: 6.99\n    relation_recall: 10.01\n    unrecognized_relations: 5\n    f1_method: all_set\n    checker_version: fixed_20260514_v2 (strip + alias + unique_et)\n- exp_id: phase2_docred_unconstrained\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    documents_checked: 986\n    parse_failures: 12\n    total_entities: 20171\n    total_triples: 17497\n    entity_type_violation_rate: 0.0248\n    relation_vocabulary_violation_rate: 0.2966\n    domain_range_violation_rate: 0.1846\n    cross_field_consistency_violation_rate: 0.001\n    entity_f1: 58.15\n    entity_precision: 57.26\n    entity_recall: 58.32\n    relation_f1: 7.74\n    relation_precision: 6.55\n    relation_recall: 9.46\n    unrecognized_relations: 5189\n    f1_method: all_set (includes OOV predictions in denominator)\n    checker_version: fixed_20260514_v2 (strip + alias + unique_et)\n    et_v1: 0.0818\n    et_fix_note: v1 triple-counted ET across entity_list + relation head/tail; v2\n      deduplicates by (text, normalized_type)\n- exp_id: phase2_docred_semantic_only\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    documents_checked: 987\n    parse_failures: 11\n    total_entities: 20185\n    total_triples: 17571\n    entity_type_violation_rate: 0.0422\n    relation_vocabulary_violation_rate: 0.2987\n    domain_range_violation_rate: 0.1384\n    cross_field_consistency_violation_rate: 0.0105\n    entity_f1: 57.81\n    entity_precision: 57.27\n    entity_recall: 58.37\n    relation_f1: 7.7\n    relation_precision: 6.54\n    relation_recall: 9.37\n    f1_method: all_set\n    checker_version: fixed_20260514_v2 (strip + alias + unique_et)\n    et_v1: 0.1044\n    et_fix_note: v1 triple-counted ET across entity_list + relation head/tail; v2\n      deduplicates by (text, normalized_type)\n- exp_id: llama_scierc_unconstrained\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    entity_type_violation_rate: 0\n    relation_vocab_violation_rate: 0.0055\n    domain_range_violation_rate: 0.1334\n    cross_field_consistency_violations: 6\n    entity_f1: 0.2356\n    entity_precision: 0.1983\n    entity_recall: 0.2902\n    relation_f1: 0.0268\n    relation_precision: 0.0236\n    relation_recall: 0.031\n    total_entities: 2451\n    total_relations: 1274\n    json_parse_failures: 1\n    samples: 551\n    checker_version: fixed_20260514_v2 (strip + alias + unique_et)\n- exp_id: llama_scierc_full_s1\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    samples: 550\n    entities_extracted: 2469\n    relations_extracted: 1315\n    domain_range_violation_rate: 0.0008\n    relation_vocab_violation_rate: 0\n    entity_type_violation_rate: 0\n    cross_field_consistency_violation_rate: 0.0656\n    total_violation_rate: 0.0431\n    entity_f1: 0.2349\n    entity_precision: 0.1972\n    entity_recall: 0.2902\n    relation_f1: 0.0254\n    relation_precision: 0.0221\n    relation_recall: 0.0298\n    checker_version: fixed_20260514_v2 (strip + alias + unique_et)\n- exp_id: llama_docred_unconstrained\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    checker_version: fixed_20260514_v2\n    f1_method: all_set\n    documents: 998\n    documents_checked: 930\n    parse_failures: 68\n    unique_entities: 11525\n    total_triples: 16437\n    dr_eligible_triples: 13789\n    ET_rate_pct: 0.13\n    RV_rate_pct: 16.03\n    DR_rate_pct: 26.07\n    CF_rate_pct: 0.17\n    entity_precision: 61.22\n    entity_recall: 51.02\n    entity_f1: 55.65\n    relation_precision: 5.22\n    relation_recall: 7\n    relation_f1: 5.98\n    fuzzy_relation_matches: 121\n- exp_id: llama_docred_full_s1\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    checker_version: fixed_20260514_v2 (strip + alias + unique_et)\n    f1_method: all_set\n    violations:\n      ET: 0\n      RV: 0\n      DR: 2.55\n      CF: 12.02\n    f1:\n      entity_f1: 55.01\n      entity_precision: 61.41\n      entity_recall: 49.82\n      relation_f1: 6.27\n      relation_precision: 5.49\n      relation_recall: 7.32\n    counts:\n      documents: 998\n      documents_checked: 907\n      parse_failures: 91\n      unique_entities: 11296\n      triples: 16368\n- exp_id: posthoc_filtering_baseline\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    docred_f1_before: 7.74\n    docred_f1_after: 9.61\n    docred_precision_before: 6.55\n    docred_precision_after: 11.22\n    docred_recall_before: 9.46\n    docred_recall_after: 8.4\n    docred_rejection_rate: 0.481\n    docred_tp_before: 1137\n    docred_tp_after: 1010\n    docred_tp_lost: 127\n    docred_et_residual: 0.0247\n    scierc_f1_before: 8.23\n    scierc_f1_after: 8.63\n    scierc_rejection_rate: 0.168\n    scierc_recall_before: 11.4\n    scierc_recall_after: 10.68\n    scierc_tp_before: 111\n    scierc_tp_after: 104\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: best\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-14T20:53:33.149Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-14T20:53:33.149Z",
  "sessionId": "3bf11c38-e586-47ea-b7d9-62bfeddfd8ee"
}
```

---

## Round 1

22 recorded events

### User

_source line 3 · 2026-05-14T20:53:33.173Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：

含义：所有核心假设经受审稿检验；CF 被接受为 honest limitation 而非致命缺陷；novelty 认定充分
核心假设：["审稿人接受 'near-complete' framing（DR 0.93% SciERC / 2.55% Llama DocRED 足够接近 0%）", 'CF trade-off 被视为 interesting finding（type system ambiguity analysis 被认可为独立贡献）', '2 模型 × 2 数据集被接受为 sufficient generalization evidence', 'zero-shot 低 F1 framing 无异议（F1 作为 control variable 而非 optimization target）', 'tightness × RV baseline dual-factor 被视为比单因素 tightness 更深的 insight', "enabling dependency 机制（grammar enables semantic）被认为比 'bitwise AND' 有方法论深度"]
关键指标范围：{'arr_overall': [3.5, 4.0], 'arr_soundness': [3.5, 4.0], 'arr_novelty': [3.0, 3.5], 'major_weaknesses_per_reviewer': [0, 1], 'reviewers_flagging_cf_fatal': [0, 0], 'reviewers_flagging_novelty_insufficient': [0, 1], 'reviewers_accepting_zero_shot_framing': [2, 3], 'acceptance_probability_pct': [55, 75], 'revision_effort_days': [3, 7]}
叙事方向：原始 framing 完全成立。Title 'Near-Complete Type-Valid IE' 无需修改。4 个 core claims 全部保留原始强度。CF 在 §5.3 作为 analysis finding + §7 limitation 双重定位即可。Violation landscape (Claim 1) + prompt insufficiency (Claim 2) 作为独立贡献获认可。Cross-model subsection 证明 generalizability。Post-hoc baseline 多维对比 (recall preservation + information coverage) 令审稿人信服。论文以 'systematic constraint enforcement framework with principled decidability taxonomy' 叙事通过。

基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。
每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。

# Project context
project: schema_semantic_constrained_ie
venue: EMNLP 2026
focus: All 20 experiments complete with 2 models × 2 datasets full matrix. Key narrative updates: D014 dual-factor tightness × RV baseline, D013 post-hoc multi-dimensional framing, D012 bootstrap CI (dataset-dependent F1 impact), cross-model generalization confirmed but with model-specific effects (Llama E-F1 decline, parse failure increase, CF=12.02%). Paper has complete related work (42 refs), discussion paragraphs, and cross-model subsection draft.

## paper_framing.md

# OntoCoDec — Paper Framing

## Target Venue
EMNLP 2026 (ARR submission May 25, 2026)

## Title
OntoCoDec: Near-Complete Type-Valid Information Extraction via Compiled Ontology Constraints
(Note: "Guaranteed" dropped per Reviewer — S1 DR=0.93%, S2 DR=0.97%, neither achieves 0%. "Near-Complete" is honest and defensible.)

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
**Response**: Cross-model validation DONE. Llama-3.1-8B 零代码修改：
- SciERC: DR 13.34%→0.08% (↓99.4%), F1-neutral (-0.14pp)
- DocRED unconstrained: DR 26.15%, RV 16.03%, R-F1 5.98% (parse failures 6.8% vs Qwen 1.2%)
- DocRED full_s1: 🔄 ETA ~20:19 UTC

**Cross-model claim 指导（Reviewer 专项评估）**:
- ✅ 可声明："OntoCoDec generalizes across model families without code modification"（程序性事实，铁证）
- ❌ 不可声明："consistently achieves the same reduction rate"（仅 2 模型，不足以量化声明）
- **RV↓DR↑ 正交性 finding**: Llama RV baseline 低(16%) 但 DR baseline 高(26%)，反向于 Qwen。证明两层约束解决正交 failure modes——vocabulary compliance ≠ semantic compliance。应作为 §5 cross-model 独立 finding 展开。
- **Parse failure 偏差**: checker skip parse failures (不计入 F1)，Llama 68/998=6.8% vs Qwen 12/998=1.2%。偏差方向保守（不利于 constrained），不威胁 claim。但需 footnote 披露 + cross-model 表增加 parse failure rate 行。
- **Llama SciERC CF=6.56%**: 比 Qwen 同量级更高，non-local constraint 问题在 Llama 上更突出，limitations 提及。
- 等 llama_docred_full_s1 出来后定最终 claim 措辞。

### C6: "Constrained decoding degrades generation quality (CRANE, Structure Snowballing)"
**Response**: OntoCoDec's semantic constraints are narrower than full grammar constraints — only type tokens are masked, free text is unconstrained. **D012 Bootstrap CI (10000×, v2 fix) 结果**:
- SciERC: Rel F1 +0.13pp (p=0.58), Ent F1 -0.03pp (p=0.53) → **F1-neutral**
- DocRED: Rel F1 +0.50pp (p<0.001, CI [+0.23, +0.81]), Ent F1 +1.23pp (p<0.001, CI [+0.94, +1.55]) → **双双显著提升**
- 机制：grammar 消除 OOV relation names + 非标 entity types → all_set 方法下减少 FP → precision 提升。Grammar 是 F1 提升的唯一来源（grammar_only Ent F1=59.38% ≈ full_s1 59.37%, Δ=0.01pp, p=0.66）。Semantic 层对 F1 无额外贡献。
- Frame as: "Constraint enforcement preserves or improves extraction quality: F1-neutral on SciERC; statistically significant Rel F1 and Entity F1 improvement on DocRED (p<0.001)."
- 不升级为 core claim，但如实报告 significance + 机制归因。Note: S2 shows marginally lower F1 and fewer triples (1644 vs 1729) — two-pass does not improve quality.

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

## Paper Structure (Draft)
1. Introduction: Violation landscape motivation + composable constraint framework overview
2. Background: Grammar-constrained decoding (XGrammar) + IE ontology structure
3. Violation Landscape Study (Phase 0 empirics — independent contribution)
4. OntoCoDec Framework: Compiler + TypeConstraintProcessor + S1/S2 strategies
5. Experiments: Constrained vs unconstrained vs post-hoc vs prompt-based
6. Related Work: 5 constraint paradigms (grammar, vocabulary, structural, type-checking, ontology)
7. Conclusion

## Claim Calibration (per Reviewer assessment)

**Safe to claim (sufficient evidence from Phase 2)**:
- "First systematic study of ontology constraint violations in LLM-based IE"
- "Violation rate correlates with constraint tightness, not ontology size" (D014: DR reduction ceiling 由 tightness × model RV baseline 共同决定)
- "Grammar+semantic constrained decoding eliminates 94% of DR violations at zero F1 cost" ✅ Phase 2 confirmed
- "Two-layer architecture provides complementary coverage — grammar enables semantic" ✅ Ablation confirmed
- "Prompt-level intervention scales poorly with ontology complexity" ✅ SciERC ↓62% vs DocRED ↓32%

**Claim with caution**:
- "Near-complete type-valid IE" — S1 0.93%, S2 0.97% residual, not truly 0%. Title updated to "Near-Complete"
- "Principled framework applicable to arbitrary IE ontologies" — validated on 2 datasets + 1 model only
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
- **May 14-15**: Llama DocRED 2 组实验 ✅ + Checker 修正 ✅ + post-hoc baseline ✅ + bootstrap CI ✅ + related work ✅
- **May 14-15**: D014 tightness claim 修订 + §5 cross-model subsection + abstract/conclusion 修正 (Agent 执行中)
- **May 15-17**: 全文校对 + Discussion 整合 + 最终数字确认
- **May 19**: 内部稿 → submit_paper_to_review
- **May 19-24**: Review 修改 + 最终提交

**当前瓶颈**: D014 论文修订（tightness claim + cross-model subsection + E-F1 claim limitation）

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
- D014 tightness revision: 🔄 Agent executing (tightness × RV baseline dual-factor)


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
  "promptId": "089efba6-2603-40fc-bf34-cb35ad758100",
  "type": "user",
  "uuid": "03321d19-541e-4bd4-ad97-43fa0dbb504d",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6",
  "sessionId": "3bf11c38-e586-47ea-b7d9-62bfeddfd8ee",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-14T20:53:33.172Z_

```json
{
  "parentUuid": "03321d19-541e-4bd4-ad97-43fa0dbb504d",
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
  "uuid": "26f5f7c1-6185-4c0b-b60d-02877b3cd5bd",
  "timestamp": "2026-05-14T20:53:33.172Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6",
  "sessionId": "3bf11c38-e586-47ea-b7d9-62bfeddfd8ee",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-14T20:53:33.172Z_

```json
{
  "parentUuid": "26f5f7c1-6185-4c0b-b60d-02877b3cd5bd",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "8ad823f4-d5e9-47fd-b89b-03c50ff559d2",
  "timestamp": "2026-05-14T20:53:33.172Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6",
  "sessionId": "3bf11c38-e586-47ea-b7d9-62bfeddfd8ee",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：所有核心假设经受审稿检验；CF 被接受为 honest limitation 而非致命缺陷；novelty 认定充分 核心假设：[\"审稿人接受 'near-complete' framing（DR 0.93% SciERC / 2.55% Llama DocRED 足够接近 0%）\", 'CF trade-o…",
  "leafUuid": "8ad823f4-d5e9-47fd-b89b-03c50ff559d2",
  "sessionId": "3bf11c38-e586-47ea-b7d9-62bfeddfd8ee"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "OntoCoDec constraint enforcement framework paper",
  "sessionId": "3bf11c38-e586-47ea-b7d9-62bfeddfd8ee"
}
```

---

### Assistant

_source line 8 · 2026-05-14T20:53:37.759Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to look at the experiment_plan file to find all planned experiments, then for each one, generate detailed predicted data under the "best" tier definition they've provided.

Let me first find and read the experiment plan file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8ad823f4-d5e9-47fd-b89b-03c50ff559d2",
  "isSidechain": false,
  "requestId": "req_011Cb38EE7DUN3Ht2mDjLQSR",
  "type": "assistant",
  "uuid": "893900c7-f784-4305-b20b-df3311e585ea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6",
  "sessionId": "3bf11c38-e586-47ea-b7d9-62bfeddfd8ee",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016i7pZEj95onz1WV1HyXRBX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 18406,
      "cache_read_input_tokens": 11841,
      "output_tokens": 174,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18406,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 174,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 18406,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18406
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

_source line 9 · 2026-05-14T20:53:37.762Z_

Let me find and read the experiment plan file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "893900c7-f784-4305-b20b-df3311e585ea",
  "isSidechain": false,
  "requestId": "req_011Cb38EE7DUN3Ht2mDjLQSR",
  "type": "assistant",
  "uuid": "01d1bd12-9217-4623-8731-f3f0a46e1366",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6",
  "sessionId": "3bf11c38-e586-47ea-b7d9-62bfeddfd8ee",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016i7pZEj95onz1WV1HyXRBX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 18406,
      "cache_read_input_tokens": 11841,
      "output_tokens": 174,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18406,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 174,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 18406,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18406
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

_source line 10 · 2026-05-14T20:53:38.379Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01D6ENe5zAqY3Qp3BLi8hM6L`</summary>

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
  "parentUuid": "01d1bd12-9217-4623-8731-f3f0a46e1366",
  "isSidechain": false,
  "requestId": "req_011Cb38EE7DUN3Ht2mDjLQSR",
  "type": "assistant",
  "uuid": "0a4949b8-3f86-4236-a47c-9c5e9fd60460",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6",
  "sessionId": "3bf11c38-e586-47ea-b7d9-62bfeddfd8ee",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016i7pZEj95onz1WV1HyXRBX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 18406,
      "cache_read_input_tokens": 11841,
      "output_tokens": 174,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18406,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 174,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 18406,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18406
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

_source line 11 · 2026-05-14T20:53:38.528Z_

<details><summary>↩ Tool result · `toolu_01D6ENe5zAqY3Qp3BLi8hM6L`</summary>

```text
projects/prov_grounded_uie/experiment_plan.yaml
projects/schema_semantic_constrained_ie/experiment_plan.lock
projects/schema_semantic_constrained_ie/experiment_plan.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3d4a3f22-cfd7-4212-8748-6de8a995819e",
  "isSidechain": false,
  "promptId": "089efba6-2603-40fc-bf34-cb35ad758100",
  "type": "user",
  "uuid": "7a2cd0db-0a23-41e8-b2b5-56783e22d6e2",
  "toolUseResult": {
    "filenames": [
      "projects/prov_grounded_uie/experiment_plan.yaml",
      "projects/schema_semantic_constrained_ie/experiment_plan.lock",
      "projects/schema_semantic_constrained_ie/experiment_plan.yaml"
    ],
    "durationMs": 139,
    "numFiles": 3,
    "truncated": false
  },
  "sourceToolAssistantUUID": "0a4949b8-3f86-4236-a47c-9c5e9fd60460",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6",
  "sessionId": "3bf11c38-e586-47ea-b7d9-62bfeddfd8ee",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-14T20:53:38.514Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01KsbTtFUcfuDqK5VP4j5jEP`</summary>

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
  "parentUuid": "0a4949b8-3f86-4236-a47c-9c5e9fd60460",
  "isSidechain": false,
  "requestId": "req_011Cb38EE7DUN3Ht2mDjLQSR",
  "type": "assistant",
  "uuid": "3d4a3f22-cfd7-4212-8748-6de8a995819e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6",
  "sessionId": "3bf11c38-e586-47ea-b7d9-62bfeddfd8ee",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016i7pZEj95onz1WV1HyXRBX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 18406,
      "cache_read_input_tokens": 11841,
      "output_tokens": 174,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18406,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 174,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 18406,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18406
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

_source line 13 · 2026-05-14T20:53:38.626Z_

<details><summary>↩ Tool result · `toolu_01KsbTtFUcfuDqK5VP4j5jEP`</summary>

```text
projects/prov_grounded_uie/logs/workers/worker_code_experiment-plan_20260512T114557.log
projects/prov_grounded_uie/logs/workers/worker_code_experiment-plan_20260512T114557_result.json
projects/prov_grounded_uie/experiment_plan.yaml
projects/schema_semantic_constrained_ie/experiment_plan.lock
projects/schema_semantic_constrained_ie/experiment_plan.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3d4a3f22-cfd7-4212-8748-6de8a995819e",
  "isSidechain": false,
  "promptId": "089efba6-2603-40fc-bf34-cb35ad758100",
  "type": "user",
  "uuid": "500351d7-eade-4012-9754-d815f9935442",
  "toolUseResult": {
    "filenames": [
      "projects/prov_grounded_uie/logs/workers/worker_code_experiment-plan_20260512T114557.log",
      "projects/prov_grounded_uie/logs/workers/worker_code_experiment-plan_20260512T114557_result.json",
      "projects/prov_grounded_uie/experiment_plan.yaml",
      "projects/schema_semantic_constrained_ie/experiment_plan.lock",
      "projects/schema_semantic_constrained_ie/experiment_plan.yaml"
    ],
    "durationMs": 107,
    "numFiles": 5,
    "truncated": false
  },
  "sourceToolAssistantUUID": "3d4a3f22-cfd7-4212-8748-6de8a995819e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6",
  "sessionId": "3bf11c38-e586-47ea-b7d9-62bfeddfd8ee",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-14T20:53:42.150Z_

<details open><summary>🔧 Tool call — Read · `toolu_01U1ZVNv84Er59VuJ6PhabCc`</summary>

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
  "parentUuid": "500351d7-eade-4012-9754-d815f9935442",
  "isSidechain": false,
  "requestId": "req_011Cb38EdNwyJrPik5svv8tj",
  "type": "assistant",
  "uuid": "e9c172b8-ff26-4183-af93-1b3f1178c7a3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6",
  "sessionId": "3bf11c38-e586-47ea-b7d9-62bfeddfd8ee",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AAVjp1S9ZLCRJm2G4GJDsg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 401,
      "cache_read_input_tokens": 30247,
      "output_tokens": 88,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 401,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 88,
          "cache_read_input_tokens": 30247,
          "cache_creation_input_tokens": 401,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 401
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

_source line 15 · 2026-05-14T20:53:42.163Z_

<details><summary>↩ Tool result · `toolu_01U1ZVNv84Er59VuJ6PhabCc`</summary>

```text
1	## OntoCoDec Experiment Plan
2	## Target: EMNLP 2026 ARR (May 25, 2026)
3	## Last updated: 2026-05-14
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
37	experiments:
38	  # --- Phase 0: Violation Landscape (ALL COMPLETE) ---
39	  - plan_id: P001
40	    name: SciERC violation rate (minimal prompt)
41	    claim: C1_violation_landscape
42	    registry_id: mvp_phase0_violation_rate
43	    priority: 1
44	    result: "DR=15.4%, 1724 triples"
45	
46	  - plan_id: P002
47	    name: SciERC violation rate (schema-informed prompt)
48	    claim: C2_prompt_insufficiency
49	    registry_id: mvp_phase0_scierc_schema
50	    priority: 1
51	    result: "DR=5.78%, -62.4% reduction, Evaluate-for regression"
52	
53	  - plan_id: P003
54	    name: DocRED violation rate (minimal prompt)
55	    claim: C1_violation_landscape
56	    registry_id: mvp_phase0_violation_rate_docred
57	    priority: 1
58	    result: "DR=18.7%, RV=28.9%"
59	
60	  - plan_id: P004
61	    name: DocRED violation rate (schema-informed prompt)
62	    claim: C2_prompt_insufficiency
63	    registry_id: mvp_phase0_docred_schema
64	    priority: 1
65	    result: "DR=12.8%, -32% reduction (weaker than SciERC)"
66	
67	  # --- Phase 2: SciERC Ablation (ALL COMPLETE) ---
68	  - plan_id: P005a
69	    name: SciERC unconstrained baseline
70	    claim: C3_composable_framework
71	    registry_id: phase2_scierc_unconstrained
72	    priority: 1
73	    result: "DR=15.37%, RV=1.39%, ET=0.40%, R-F1=8.23%"
74	
75	  - plan_id: P005
76	    name: SciERC grammar-only
77	    claim: C3_composable_framework
78	    registry_id: phase2_scierc_grammar_only
79	    priority: 1
80	    result: "RV→0%, ET→0%, DR=14.84% (grammar alone doesn't reduce DR), E-F1=30.98%"
81	
82	  - plan_id: P006
83	    name: SciERC semantic-only
84	    claim: C3_composable_framework
85	    registry_id: phase2_scierc_semantic_only
86	    priority: 1
87	    result: "DR=11.65% (↓24%), RV/ET unchanged, demonstrates enabling dependency"
88	
89	  - plan_id: P007
90	    name: SciERC full S1
91	    claim: C3_composable_framework
92	    registry_id: phase2_scierc_full_s1
93	    priority: 1
94	    result: "DR=0.93% (↓94%), RV/ET→0%, CF=9.90%, R-F1=8.36% (+0.13pp, p=0.58)"
95	
96	  - plan_id: P008
97	    name: SciERC full S2 (ablation)
98	    claim: C4_s1_vs_s2
99	    registry_id: phase2_scierc_full_s2
100	    priority: 1
101	    result: "DR=0.97%, CF=8.03%, R-F1=8.03% (worse than S1). Demoted."
102	
103	  # --- Phase 2: DocRED Ablation (ALL COMPLETE) ---
104	  - plan_id: P009
105	    name: DocRED unconstrained baseline
106	    claim: C3_composable_framework
107	    registry_id: phase2_docred_unconstrained
108	    priority: 1
109	    result: "DR=18.46%, RV=29.66%, ET=2.48%, R-F1=7.73%"
110	
111	  - plan_id: P010
112	    name: DocRED grammar-only
113	    claim: C3_composable_framework
114	    registry_id: phase2_docred_grammar_only
115	    priority: 1
116	    result: "RV→0.03%, ET→0%, E-F1=59.38% (grammar drives all E-F1 gain)"
117	
118	  - plan_id: P011
119	    name: DocRED semantic-only
120	    claim: C3_composable_framework
121	    registry_id: phase2_docred_semantic_only
122	    priority: 1
123	    result: "DR=13.96%, ET=4.22%"
124	
125	  - plan_id: P012
126	    name: DocRED full S1
127	    claim: C3_composable_framework
128	    registry_id: phase2_docred_full_s1
129	    priority: 1
130	    result: "DR=10.21% (↓45%), RV→0.03%, ET→0%, CF=2.57%, R-F1=8.23% (+0.50pp, p<0.001), E-F1=59.37% (+1.22pp, p<0.001)"
131	
132	  # --- Phase 2: Cross-Model (ALL COMPLETE) ---
133	  - plan_id: P013
134	    name: Llama SciERC unconstrained
135	    claim: C5_cross_model
136	    registry_id: llama_scierc_unconstrained
137	    priority: 2
138	    result: "DR=17.53%, RV=0.23%, ET=0.27%"
139	
140	  - plan_id: P014
141	    name: Llama SciERC full S1
142	    claim: C5_cross_model
143	    registry_id: llama_scierc_full_s1
144	    priority: 2
145	    result: "DR=0.10% (↓99.4%), RV/ET→0%, R-F1 neutral"
146	
147	  - plan_id: P015
148	    name: Llama DocRED unconstrained
149	    claim: C5_cross_model
150	    registry_id: llama_docred_unconstrained
151	    priority: 2
152	    result: "DR=26.07%, RV=16.03%, ET=0.13%, R-F1=5.98%"
153	
154	  - plan_id: P016
155	    name: Llama DocRED full S1
156	    claim: C5_cross_model
157	    registry_id: llama_docred_full_s1
158	    priority: 2
159	    result: "DR=2.55% (↓90.2%), RV/ET→0%, CF=12.02%, R-F1=6.27% (+0.29pp), E-F1=55.01% (-0.64pp), parse_failures=91/998"
160	
161	  # --- Supplementary (ALL COMPLETE) ---
162	  - plan_id: P017
163	    name: S2 pilot (50 docs)
164	    claim: C4_s1_vs_s2
165	    registry_id: phase2_s2_pilot50
166	    priority: 3
167	    result: "Pilot confirmed S2 works, full run in P008"
168	
169	  - plan_id: P018
170	    name: Post-hoc filtering baseline
171	    claim: C6_f1_impact
172	    registry_id: posthoc_filtering_baseline
173	    priority: 2
174	    result: "Post-hoc F1 > OntoCoDec F1 on both datasets. Framing: multi-dimensional (D013)"
175	    note: "Not in registry — computed offline"
176	
177	  - plan_id: P019
178	    name: Bootstrap CI (10000 iterations)
179	    claim: C6_f1_impact
180	    registry_id: d012_bootstrap_ci
181	    priority: 1
182	    result: "SciERC R-F1 +0.13pp p=0.58; DocRED R-F1 +0.50pp p<0.001, E-F1 +1.23pp p<0.001"
183	    note: "Computed offline, not GPU experiment"
184	
185	  - plan_id: P020
186	    name: DocRED schema compilation (Phase 0 R2)
187	    claim: C1_violation_landscape
188	    registry_id: mvp_phase0_docred_schema_r2
189	    priority: 3
190	    result: "killed — superseded by P004"
191	
192	gpu_budget:
193	  allocated: "westd-16980 cuda:0, cuda:1 (2x RTX PRO 6000 96GB)"
194	  total_used: "~30 GPU-hours"
195	  status: "All experiments complete. GPUs idle."
196	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e9c172b8-ff26-4183-af93-1b3f1178c7a3",
  "isSidechain": false,
  "promptId": "089efba6-2603-40fc-bf34-cb35ad758100",
  "type": "user",
  "uuid": "33151c19-2e13-4e14-a0e9-dfc2d513a641",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/experiment_plan.yaml",
      "content": "## OntoCoDec Experiment Plan\n## Target: EMNLP 2026 ARR (May 25, 2026)\n## Last updated: 2026-05-14\n\nclaims:\n  C1_violation_landscape:\n    description: \"LLM-based IE violates ontology type constraints at non-trivial rates; violation rate driven by constraint tightness × model RV baseline, not ontology size\"\n    status: supported\n    evidence_strength: strong\n\n  C2_prompt_insufficiency:\n    description: \"Schema-informed prompting reduces but cannot eliminate violations; unreliable per-relation\"\n    status: supported\n    evidence_strength: strong\n\n  C3_composable_framework:\n    description: \"OntoCoDec compiles IE ontology schemas into two composable constraint layers (grammar+semantic) with enabling dependency; near-complete DR elimination\"\n    status: supported\n    evidence_strength: strong\n\n  C4_s1_vs_s2:\n    description: \"S2 two-pass offers no advantage over S1 single-pass; S1 adopted as primary\"\n    status: supported_demoted\n    evidence_strength: moderate\n    note: \"S2 demoted to ablation (D007). S1 simpler + marginally better F1.\"\n\n  C5_cross_model:\n    description: \"OntoCoDec generalizes across models without code modification; DR reduction magnitude varies with model RV baseline\"\n    status: supported\n    evidence_strength: strong\n\n  C6_f1_impact:\n    description: \"Constraint enforcement preserves or improves F1; improvement is model/dataset-dependent (Qwen DocRED significant, SciERC neutral)\"\n    status: supported\n    evidence_strength: strong\n\nexperiments:\n  # --- Phase 0: Violation Landscape (ALL COMPLETE) ---\n  - plan_id: P001\n    name: SciERC violation rate (minimal prompt)\n    claim: C1_violation_landscape\n    registry_id: mvp_phase0_violation_rate\n    priority: 1\n    result: \"DR=15.4%, 1724 triples\"\n\n  - plan_id: P002\n    name: SciERC violation rate (schema-informed prompt)\n    claim: C2_prompt_insufficiency\n    registry_id: mvp_phase0_scierc_schema\n    priority: 1\n    result: \"DR=5.78%, -62.4% reduction, Evaluate-for regression\"\n\n  - plan_id: P003\n    name: DocRED violation rate (minimal prompt)\n    claim: C1_violation_landscape\n    registry_id: mvp_phase0_violation_rate_docred\n    priority: 1\n    result: \"DR=18.7%, RV=28.9%\"\n\n  - plan_id: P004\n    name: DocRED violation rate (schema-informed prompt)\n    claim: C2_prompt_insufficiency\n    registry_id: mvp_phase0_docred_schema\n    priority: 1\n    result: \"DR=12.8%, -32% reduction (weaker than SciERC)\"\n\n  # --- Phase 2: SciERC Ablation (ALL COMPLETE) ---\n  - plan_id: P005a\n    name: SciERC unconstrained baseline\n    claim: C3_composable_framework\n    registry_id: phase2_scierc_unconstrained\n    priority: 1\n    result: \"DR=15.37%, RV=1.39%, ET=0.40%, R-F1=8.23%\"\n\n  - plan_id: P005\n    name: SciERC grammar-only\n    claim: C3_composable_framework\n    registry_id: phase2_scierc_grammar_only\n    priority: 1\n    result: \"RV→0%, ET→0%, DR=14.84% (grammar alone doesn't reduce DR), E-F1=30.98%\"\n\n  - plan_id: P006\n    name: SciERC semantic-only\n    claim: C3_composable_framework\n    registry_id: phase2_scierc_semantic_only\n    priority: 1\n    result: \"DR=11.65% (↓24%), RV/ET unchanged, demonstrates enabling dependency\"\n\n  - plan_id: P007\n    name: SciERC full S1\n    claim: C3_composable_framework\n    registry_id: phase2_scierc_full_s1\n    priority: 1\n    result: \"DR=0.93% (↓94%), RV/ET→0%, CF=9.90%, R-F1=8.36% (+0.13pp, p=0.58)\"\n\n  - plan_id: P008\n    name: SciERC full S2 (ablation)\n    claim: C4_s1_vs_s2\n    registry_id: phase2_scierc_full_s2\n    priority: 1\n    result: \"DR=0.97%, CF=8.03%, R-F1=8.03% (worse than S1). Demoted.\"\n\n  # --- Phase 2: DocRED Ablation (ALL COMPLETE) ---\n  - plan_id: P009\n    name: DocRED unconstrained baseline\n    claim: C3_composable_framework\n    registry_id: phase2_docred_unconstrained\n    priority: 1\n    result: \"DR=18.46%, RV=29.66%, ET=2.48%, R-F1=7.73%\"\n\n  - plan_id: P010\n    name: DocRED grammar-only\n    claim: C3_composable_framework\n    registry_id: phase2_docred_grammar_only\n    priority: 1\n    result: \"RV→0.03%, ET→0%, E-F1=59.38% (grammar drives all E-F1 gain)\"\n\n  - plan_id: P011\n    name: DocRED semantic-only\n    claim: C3_composable_framework\n    registry_id: phase2_docred_semantic_only\n    priority: 1\n    result: \"DR=13.96%, ET=4.22%\"\n\n  - plan_id: P012\n    name: DocRED full S1\n    claim: C3_composable_framework\n    registry_id: phase2_docred_full_s1\n    priority: 1\n    result: \"DR=10.21% (↓45%), RV→0.03%, ET→0%, CF=2.57%, R-F1=8.23% (+0.50pp, p<0.001), E-F1=59.37% (+1.22pp, p<0.001)\"\n\n  # --- Phase 2: Cross-Model (ALL COMPLETE) ---\n  - plan_id: P013\n    name: Llama SciERC unconstrained\n    claim: C5_cross_model\n    registry_id: llama_scierc_unconstrained\n    priority: 2\n    result: \"DR=17.53%, RV=0.23%, ET=0.27%\"\n\n  - plan_id: P014\n    name: Llama SciERC full S1\n    claim: C5_cross_model\n    registry_id: llama_scierc_full_s1\n    priority: 2\n    result: \"DR=0.10% (↓99.4%), RV/ET→0%, R-F1 neutral\"\n\n  - plan_id: P015\n    name: Llama DocRED unconstrained\n    claim: C5_cross_model\n    registry_id: llama_docred_unconstrained\n    priority: 2\n    result: \"DR=26.07%, RV=16.03%, ET=0.13%, R-F1=5.98%\"\n\n  - plan_id: P016\n    name: Llama DocRED full S1\n    claim: C5_cross_model\n    registry_id: llama_docred_full_s1\n    priority: 2\n    result: \"DR=2.55% (↓90.2%), RV/ET→0%, CF=12.02%, R-F1=6.27% (+0.29pp), E-F1=55.01% (-0.64pp), parse_failures=91/998\"\n\n  # --- Supplementary (ALL COMPLETE) ---\n  - plan_id: P017\n    name: S2 pilot (50 docs)\n    claim: C4_s1_vs_s2\n    registry_id: phase2_s2_pilot50\n    priority: 3\n    result: \"Pilot confirmed S2 works, full run in P008\"\n\n  - plan_id: P018\n    name: Post-hoc filtering baseline\n    claim: C6_f1_impact\n    registry_id: posthoc_filtering_baseline\n    priority: 2\n    result: \"Post-hoc F1 > OntoCoDec F1 on both datasets. Framing: multi-dimensional (D013)\"\n    note: \"Not in registry — computed offline\"\n\n  - plan_id: P019\n    name: Bootstrap CI (10000 iterations)\n    claim: C6_f1_impact\n    registry_id: d012_bootstrap_ci\n    priority: 1\n    result: \"SciERC R-F1 +0.13pp p=0.58; DocRED R-F1 +0.50pp p<0.001, E-F1 +1.23pp p<0.001\"\n    note: \"Computed offline, not GPU experiment\"\n\n  - plan_id: P020\n    name: DocRED schema compilation (Phase 0 R2)\n    claim: C1_violation_landscape\n    registry_id: mvp_phase0_docred_schema_r2\n    priority: 3\n    result: \"killed — superseded by P004\"\n\ngpu_budget:\n  allocated: \"westd-16980 cuda:0, cuda:1 (2x RTX PRO 6000 96GB)\"\n  total_used: \"~30 GPU-hours\"\n  status: \"All experiments complete. GPUs idle.\"\n",
      "numLines": 196,
      "startLine": 1,
      "totalLines": 196
    }
  },
  "sourceToolAssistantUUID": "e9c172b8-ff26-4183-af93-1b3f1178c7a3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6",
  "sessionId": "3bf11c38-e586-47ea-b7d9-62bfeddfd8ee",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 16 · 2026-05-14T20:53:42.275Z_

````json
{
  "parentUuid": "33151c19-2e13-4e14-a0e9-dfc2d513a641",
  "isSidechain": false,
  "attachment": {
    "type": "nested_memory",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/CLAUDE.md",
    "content": {
      "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/CLAUDE.md",
      "type": "Project",
      "content": "## 当前项目\n当前绑定项目：**schema_semantic_constrained_ie**\n\n## 按需查阅\n- 项目配置：`load_project_config(\"schema_semantic_constrained_ie\")` 或 `load_project_config(\"schema_semantic_constrained_ie\", section=\"execution\")`\n- 知识文件：`read_project_file(file=...)` 读取项目文件（ROADMAP.md/memory.md/ideas.md/report.md 等）\n- 路线图：`read_roadmap()` 读取研究方向和短期任务\n- 产出目录：`/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/`（写文件后用 `register_artifact` 注册）\n\n## Worker 操作规范\n\n### ssh-env-setup\n\n# 远程服务器环境搭建规范\n\n## 核心原则\n\n**先探测，再安装。** 不要假设服务器上什么都没有——很多包已经装好了。安装前必须走 discovery 流程。\n\n**镜像快速路径**：连接服务器后，先用 `detect_image` 检测是否为预置镜像。如果是已知镜像且版本匹配，跳过基础环境搭建（Phase 1-4），直接安装项目特有依赖。未检测到镜像时走传统流程。\n\n**aml-train 镜像使用 conda 环境**（不是 venv）。环境激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`。pip/python 在 `/root/miniconda3/bin/` 下。**不要假设 .venv 存在，不要创建 venv。**\n\n## Phase 1: 环境探测（用 ssh_read_only）\n\n连接到服务器后，第一步永远是收集信息，不要直接装东西：\n\n```bash\n# 1. Python 环境\nwhich python3 && python3 --version\npip3 --version 2>/dev/null || echo \"NO_PIP\"\n\n# 2. CUDA 环境\nnvidia-smi --query-gpu=name,memory.total,driver_version --format=csv,noheader 2>/dev/null || echo \"NO_GPU\"\nnvcc --version 2>/dev/null | grep \"release\" || echo \"NO_NVCC\"\n\n# 3. 包管理器\nls -d /opt/miniconda3 ~/miniconda3 ~/.conda 2>/dev/null || echo \"NO_CONDA\"\nls -d .venv venv env 2>/dev/null || echo \"NO_VENV\"\npip3 list --format=freeze 2>/dev/null | grep -iE \"torch|transformers|flash\" || echo \"NO_ML_PKGS\"\n\n# 4. PEP 668 检查\npython3 -c \"import sysconfig; print(sysconfig.get_path('stdlib'))\" 2>/dev/null\nls /usr/lib/python*/EXTERNALLY-MANAGED 2>/dev/null && echo \"PEP668_MANAGED\" || echo \"PEP668_OK\"\n```\n\n根据探测结果决定安装策略，不要猜。\n\n## Phase 2: 环境策略选择\n\n根据 Phase 1 结果选择**一个**策略，不要混用：\n\n| 探测结果 | 策略 | 说明 |\n|----------|------|------|\n| 项目目录有 `.venv/` | 用它：`source .venv/bin/activate` | 最优先 |\n| 有 conda 且有写权限 | `conda activate base` 或创建专属 env | 次优先 |\n| PEP668_MANAGED + 无 venv | 创建 venv：`python3 -m venv .venv && source .venv/bin/activate` | 不要用 --break-system-packages |\n| PEP668_OK（无保护） | 直接 `pip install`（旧系统） | 仍建议 venv |\n\n**决不混用 conda install + pip install 到同一环境。** 选了 pip 就全用 pip。\n\n## Phase 3: PyTorch 安装\n\n### CUDA 版本映射（2025-2026 常用）\n\n先从 `nvcc --version` 或 `nvidia-smi` 获取 CUDA 版本，然后匹配：\n\n| CUDA 版本 | PyTorch pip index URL | 推荐 torch 版本 |\n|-----------|----------------------|-----------------|\n| 11.8 | `https://download.pytorch.org/whl/cu118` | ≥ 2.0 |\n| 12.1 | `https://download.pytorch.org/whl/cu121` | ≥ 2.1 |\n| 12.4 | `https://download.pytorch.org/whl/cu124` | ≥ 2.4 |\n| 12.6 | `https://download.pytorch.org/whl/cu126` | ≥ 2.6 |\n\n**不要猜版本号。** 如果不确定可用版本：\n```bash\npip index versions torch --index-url https://download.pytorch.org/whl/cu121 2>/dev/null | head -3\n```\n\n安装命令：\n```bash\npip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu{CUDA_SHORT}\n```\n\n### 大包超时处理\n\nPyTorch wheel 约 500MB-2GB，默认 SSH 超时可能不够。策略：\n\n```bash\n# 方法 1: nohup + 轮询（推荐）\nnohup pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121 > /tmp/pip_install.log 2>&1 &\necho $!  # 记录 PID\n\n# 后续用 ssh_read_only 轮询\ncat /tmp/pip_install.log | tail -5\nps -p &lt;PID> -o pid= 2>/dev/null && echo \"STILL_RUNNING\" || echo \"DONE\"\n```\n\n```bash\n# 方法 2: 加大 pip 超时\npip install --timeout 300 torch ...\n```\n\n## Phase 4: 验证（必须执行）\n\n安装后必须验证，不要假设成功：\n\n```bash\npython3 -c \"\nimport torch\nprint(f'torch={torch.__version__}, cuda={torch.cuda.is_available()}, gpus={torch.cuda.device_count()}')\nif torch.cuda.is_available():\n    for i in range(torch.cuda.device_count()):\n        print(f'  GPU {i}: {torch.cuda.get_device_name(i)} ({torch.cuda.get_device_properties(i).total_mem // 1024**3}GB)')\n\"\n```\n\n验证失败的常见原因：\n- `torch.cuda.is_available()` 返回 False → CUDA 版本和 torch 不匹配，重装正确版本\n- `ImportError: libcudnn` → 缺 cuDNN，装 `nvidia-cudnn-cu1x`\n- GPU 数量不对 → 检查 `CUDA_VISIBLE_DEVICES` 环境变量\n\n## Phase 5: 项目依赖\n\n基础环境就绪后，安装项目依赖：\n\n```bash\n# 优先用 requirements.txt / pyproject.toml\npip install -r requirements.txt  # 或 pip install -e .\n\n# 常用 ML 依赖补装\npip install transformers datasets einops accelerate wandb\n```\n\nflash-attention 特殊处理（编译型包）：\n```bash\n# 需要匹配的 CUDA toolkit，编译耗时 5-15 分钟\npip install flash-attn --no-build-isolation\n# 如果编译失败，试预编译版本\npip install flash-attn --no-build-isolation 2>/dev/null || pip install flash-attn-wheels\n```\n\n## ssh_read_only vs ssh_execute 使用规则\n\n| 操作 | 用哪个工具 |\n|------|-----------|\n| 检查环境（python --version, nvidia-smi, pip list） | `ssh_read_only` |\n| 读文件内容、查日志 | `ssh_read_only` |\n| 安装包（pip install, conda install） | `ssh_execute` |\n| 创建/修改文件、启动进程 | `ssh_execute` |\n| 运行实验脚本 | `ssh_execute` |\n\n**原则：能用 read_only 就用 read_only，只有要改变服务器状态时才用 execute。**\n\n## AutoDL 专项注意事项\n\nAutoDL 实例有一系列特殊约束，5 个项目反复踩坑，必须遵守：\n\n### 磁盘\n- **根分区只有 ~30GB，严禁存大文件。** 模型、数据集、HF cache 全部放数据盘 `/root/autodl-tmp/`\n- 设置 `HF_HOME=/root/autodl-tmp/.hf_cache`，否则 HF 默认缓存到根分区导致磁盘满\n- 下载模型时用 `--local-dir /root/autodl-tmp/models/&lt;name>`，不要用默认路径\n\n### 网络\n- pip install / git clone 前必须 `source /etc/network_turbo` 启用代理加速，否则 pypi.nvidia.com 504 超时、GitHub TLS 断连\n- HF 下载设 `HF_HUB_DISABLE_XET=1`，xet_get 在 AutoDL 上返回 401\n- **SSL 证书**：`network_turbo` 的代理使用自签名证书，Python 默认 SSL 验证会失败。必须设置 `REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt` 和 `SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt`，否则 HF 下载、datasets 加载等全部报 SSL 错误\n- **大模型下载优先用 ModelScope**：AutoDL 代理下载 HuggingFace 大文件极慢（~200KB/s），改用 ModelScope 国内 CDN 速度快很多。`pip install modelscope && python -c \"from modelscope import snapshot_download; snapshot_download('Qwen/Qwen2.5-7B-Instruct', cache_dir='/root/autodl-tmp/.hf_cache')\"`\n\n### SSH\n- **AutoDL 实例重启后 SSH 端口会变。** 连接失败时不要反复重试，应提示用户去控制台查新端口并更新 `~/.ssh/config`\n\n## 经验沉淀\n\n- [2026-04-05] Worker 首次连接服务器时，先用一条 ssh_read_only 组合命令完成全部探测，减少 SSH 往返次数\n- [2026-04-05] 遇到 PEP 668 时创建 venv 而非 --break-system-packages，避免污染系统 Python\n- [2026-04-05] PyTorch 大包安装用 nohup 后台执行 + 轮询方式，避免 SSH 超时导致安装中断\n- [2026-04-05] conda 环境和 pip 不要混用——如果项目用 pip，就全部用 pip\n- [2026-04-09] sync_code 前确保本地 commit 已 push 到 remote，否则服务器 git pull 拉不到最新代码\n- [2026-04-09] venv 创建后用 `which python` 验证路径指向正确的 venv python，不要假设系统 PATH 正确\n\n## 更多 Skills（按需加载）\n\n执行相关任务前，先 Read 对应 skill 获取环境配置和最佳实践。\n\n- **check-training-status** — 当用户问训练进度/实验状态/查状态时使用。用专用工具查看训练状态，禁止 ssh_execute。  →  `/home/ubuntu/agent-ml-research/skills/global/check-training-status.skill.md`\n- **rebuttal** — 撰写和优化学术 rebuttal——逐条回应审稿意见，生成 response letter。当收到审稿意见、需要写 rebuttal、回复 reviewer 评论时使用。关键词：rebuttal、审稿意见、reviewer response、author response、meta-review、AC 意见。  →  `/home/ubuntu/agent-ml-research/skills/global/rebuttal.skill.md`\n- **review-reviewer-session-start** — Review Reviewer session 启动初始化——检查论文格式、编译状态、材料清单。Review Reviewer 角色 session 启动时自动使用。  →  `/home/ubuntu/agent-ml-research/skills/global/review-reviewer-session-start.skill.md`\n- **reference-audit** — 引用验证与审计——检查 bib 条目完整性、引用真实性、格式一致性。写论文、审查论文、提交前检查引用时使用。关键词：citation verification、引用检查、bib 审计、fake citation、引用格式。  →  `/home/ubuntu/agent-ml-research/skills/global/reference-audit.skill.md`\n- **accelerate-distributed** — HuggingFace Accelerate 分布式训练指南——4行代码实现多GPU/DeepSpeed/FSDP/混合精度。多GPU训练时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/accelerate-distributed.skill.md`\n- **draw-paper-figure** — 生成学术论文级 matplotlib 图表——reliability diagrams、ECE heatmap、T* scatter plot、模型对比图，直接在 A6000 服务器上执行，输出 PDF/PNG  →  `/home/ubuntu/agent-ml-research/skills/global/draw-paper-figure.skill.md`\n- **experiment-analysis** — 实验结果分析框架——统计显著性检验、消融分析、baseline 对比、可视化建议。分析实验结果或撰写论文 Results 部分时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/experiment-analysis.skill.md`\n- **hf-hub** — HuggingFace Hub CLI (hf) — 下载/上传模型和数据集、管理缓存、搜索论文和模型。涉及 HuggingFace 资源操作时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/hf-hub.skill.md`\n- **latex-paper** — ML 顶会论文 LaTeX 写作全流程——Claim-Evidence 方法论、引用防幻觉、顶会模板速查、投稿工程链、会议转投。写论文/投稿时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md`\n- **lm-eval-harness** — lm-evaluation-harness 模型评估指南——MMLU/GSM8K/HumanEval 等 60+ 学术基准测试。评估模型质量、对比实验时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/lm-eval-harness.skill.md`\n- **ml-experiment-guide** — 跨项目 ML 实验避坑指南——从多个项目沉淀的通用踩坑经验与最佳实践。当 Worker 准备写实验代码、或排查实验问题时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/ml-experiment-guide.skill.md`\n- **paper-banana** — 用 PaperBanana 生成发表级学术统计图——LLM 写 matplotlib 代码 + Critic 迭代 3 轮，输入 CSV/JSON 数据 + 意图描述即可。需要 GOOGLE_API_KEY。  →  `/home/ubuntu/agent-ml-research/skills/global/paper-banana.skill.md`\n- **paper-image-extractor** — 从论文 PDF 或 arXiv 源码包提取图表——优先 arXiv 原始图片，回退 PDF 解析。用户说\"提取图\"/\"抽图\"/\"extract figures\"时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/paper-image-extractor.skill.md`\n- **peft-lora** — PEFT/LoRA/QLoRA 参数高效微调指南——LoRA 配置选择、QLoRA 量化训练、Adapter 管理与合并。微调大模型时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/peft-lora.skill.md`\n- **research-news** — 每日论文推荐——搜索 arXiv 最新论文，按相关性/新颖性/影响力评分，生成推荐列表。Director 说\"有什么新论文\"/\"最近进展\"/\"research news\"时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/research-news.skill.md`\n- **trl-training** — TRL (Transformer Reinforcement Learning) 训练指南——SFT/DPO/GRPO/KTO 配置与最佳实践。训练或对齐语言模型时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/trl-training.skill.md`\n- **wandb-guide** — W&B 查询最佳实践——如何高效使用 fetch_wandb_metrics / compare_wandb_runs / get_best_wandb_run 分析实验结果。分析实验指标时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/wandb-guide.skill.md`\n",
      "contentDiffersFromDisk": false
    },
    "displayPath": "projects/schema_semantic_constrained_ie/.claude/CLAUDE.md"
  },
  "type": "attachment",
  "uuid": "90513574-9ae6-408b-ae66-f96d7df6488f",
  "timestamp": "2026-05-14T20:53:42.275Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6",
  "sessionId": "3bf11c38-e586-47ea-b7d9-62bfeddfd8ee",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：所有核心假设经受审稿检验；CF 被接受为 honest limitation 而非致命缺陷；novelty 认定充分 核心假设：[\"审稿人接受 'near-complete' framing（DR 0.93% SciERC / 2.55% Llama DocRED 足够接近 0%）\", 'CF trade-o…",
  "leafUuid": "90513574-9ae6-408b-ae66-f96d7df6488f",
  "sessionId": "3bf11c38-e586-47ea-b7d9-62bfeddfd8ee"
}
```

---

### Runtime record

_source line 18_

```json
{
  "type": "ai-title",
  "aiTitle": "OntoCoDec constraint enforcement framework paper",
  "sessionId": "3bf11c38-e586-47ea-b7d9-62bfeddfd8ee"
}
```

---

### Assistant

_source line 19 · 2026-05-14T20:53:57.029Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have the full experiment plan with all 20 experiments (P001-P020). All are marked as complete with results. The user wants me to generate detailed predicted data for each planned experiment under the "best" tier definition.

Let me also check the registry data more carefully from the CLAUDE.md to get all the actual metrics, then produce the imagined experiments YAML with predicted results that align with the "best" tier narrative.

The "best" tier means:
- All core assumptions pass reviewer scrutiny
- CF accepted as honest limitation, not fatal
- Novelty deemed sufficient
- ARR overall: 3.5-4.0, soundness: 3.5-4.0, novelty: 3.0-3.5


- Major weaknesses per reviewer: 0-1
- 0 reviewers flagging CF as fatal
- 0-1 reviewers flagging novelty insufficient
- 2-3 reviewers accepting zero-shot framing
- Acceptance probability: 55-75%
- Revision effort: 3-7 days

The narrative stays intact—original framing holds, title unchanged, all 4 core claims at full strength, with CF dual-positioned in §5.3 and §7. Now I need to craft result_rationale for each experiment explaining why these specific results would emerge under this tier, then generate the complete YAML output.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "90513574-9ae6-408b-ae66-f96d7df6488f",
  "isSidechain": false,
  "requestId": "req_011Cb38Etvq8NXc6NgvHCXdg",
  "type": "assistant",
  "uuid": "8d18bb91-f1e1-4a1f-a0a4-e2a42efac0fe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6",
  "sessionId": "3bf11c38-e586-47ea-b7d9-62bfeddfd8ee",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VyNuWJ5jvbJvbfFKpVjd1R",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7954,
      "cache_read_input_tokens": 30648,
      "output_tokens": 17087,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7954,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 17087,
          "cache_read_input_tokens": 30648,
          "cache_creation_input_tokens": 7954,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7954
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

_source line 20 · 2026-05-14T20:59:19.311Z_

```yaml
tier: best
narrative_guidance: >
  原始 framing 完全成立。Title 'Near-Complete Type-Valid IE' 无需修改。4 个 core claims 全部保留原始强度。
  CF 在 §5.3 作为 analysis finding + §7 limitation 双重定位即可。Violation landscape (Claim 1) + prompt insufficiency (Claim 2)
  作为独立贡献获认可。Cross-model subsection 证明 generalizability。Post-hoc baseline 多维对比令审稿人信服。
  论文以 'systematic constraint enforcement framework with principled decidability taxonomy' 叙事通过。
  审稿人整体认可方法的工程成熟度和实验完整度，主要保留意见集中在 novelty 边界（1/3 审稿人标记）和 CF 深度分析。

imagined_experiments:
  # ============================================================
  # Phase 0: Violation Landscape
  # ============================================================
  - name: "SciERC violation rate (minimal prompt)"
    plan_id: "P001"
    description: >
      Qwen3-8B 零样本抽取 SciERC 551 篇摘要，minimal prompt（仅给 relation list），
      运行 violation_checker 统计四类违规率，建立 unconstrained baseline。
    expected_results:
      total_triples: 1724
      total_entities: 2474
      json_parse_rate: 1.0
      entity_type_violation_rate: 0.004
      relation_vocabulary_violation_rate: 0.0139
      domain_range_violation_rate: 0.1537
      cross_field_consistency_violation_rate: 0.0008
      entity_f1: 0.3101
      relation_f1: 0.0823
      per_relation_dr_Used-for: 0.0076
      per_relation_dr_Conjunction: 0.0
      per_relation_dr_Hyponym-of: 0.1452
      per_relation_dr_Evaluate-for: 0.2406
      per_relation_dr_Part-of: 0.25
      per_relation_dr_Feature-of: 0.3354
      per_relation_dr_Compare: 0.4242
    result_rationale: >
      best 档下 15.4% 的 DR 是建立 Claim 1 的关键锚点。审稿人接受这一数值为 "non-trivial" 而非 "marginal"，
      因为 per-relation 分布呈现清晰的 tightness-driven 模式：loose-constraint 的 Used-for (0.76%) 
      vs tight-constraint 的 Compare (42.4%) 形成 56× 差异。这一分布非均匀性本身构成独立 finding，
      而非简单的 "LLM 会犯错"。7-relation 的 SciERC 作为小而精的 ontology，提供了可解读的 per-relation 
      细粒度分析基础。审稿人在 best 档不会质疑 15.4% 的实际意义——这个数值足够大以激发方法动机，
      又足够结构化以支撑 tightness 分析。
    tables:
      - table_id: "T1"
        caption: "Per-relation DR violation rates on SciERC (Qwen3-8B, minimal prompt)"
        description: >
          7 行（每 relation 一行），列: Relation | #Triples | #DR_Violations | DR_Rate(%) | τ̄ (constraint tightness)。
          按 DR rate 降序排列。展示 violation 与 tightness 的正相关。
    figures_description:
      - "Fig 1: Bar chart of per-relation DR rates overlaid with constraint tightness τ̄ (dual y-axis)，视觉化 Claim 1 的 tightness-violation 正相关"
    analysis: >
      15.4% 整体 DR 为方法提供强动机。关键 insight 不在均值而在分布：
      Compare (42.4%) 和 Feature-of (33.5%) 各只有 2-3 个有效 (head_type, tail_type) 对（高 tightness），
      而 Used-for 接受 5/6 entity types 做 head（低 tightness），DR 仅 0.76%。
      这直接支撑 "violation rate driven by constraint tightness, not ontology size" 的 Claim 1 措辞。

  - name: "SciERC violation rate (schema-informed prompt)"
    plan_id: "P002"
    description: >
      同一模型/数据集，prompt 中显式描述每个 relation 的 domain/range 约束，
      测试 prompt-level intervention 的违规消减效果。
    expected_results:
      total_triples: 1661
      domain_range_violation_rate: 0.0578
      relation_vocabulary_violation_rate: 0.003
      entity_type_violation_rate: 0.0
      overall_dr_reduction_pct: -62.4
      per_relation_Feature-of_delta_pp: -22.3
      per_relation_Part-of_delta_pp: -22.5
      per_relation_Compare_delta_pp: -14.8
      per_relation_Evaluate-for_delta_pp: +5.8
      mcnemar_all_significant: true
    result_rationale: >
      best 档下审稿人接受 62.4% reduction 是 "substantial but insufficient" 的 framing。
      关键说服力来自 Evaluate-for 的 +5.8pp 回归——这不是噪声而是 prior-constraint conflict 的系统性表现：
      schema prompt 让模型 "知道" 约束但在 boundary case 上反而 destabilize type assignment。
      3 个 relation 保留 >10% DR（Compare 27.6%, Evaluate-for 29.9%, Feature-of 11.3%）
      直接证伪 "prompt 足够" 的反驳。best 档审稿人不会纠缠 "5.78% 刚过 5% 阈值"——
      因为论文 framing 不依赖阈值而依赖 per-relation unreliability。
    tables:
      - table_id: "T2"
        caption: "Schema-informed prompt effect on DR by relation type (SciERC)"
        description: >
          7 行, 列: Relation | DR_minimal(%) | DR_schema(%) | Δpp | Direction。
          Evaluate-for 行高亮为红色（回归）。
    figures_description:
      - "Fig 2: Paired bar chart (minimal vs schema-informed) per relation，Evaluate-for 标注 regression arrow + prior-constraint conflict 注释"
    analysis: >
      schema-informed prompt 在 overall 层面有效（-62.4%）但 per-relation 不可靠。
      Evaluate-for 回归是 Claim 2 最强论据：即使告诉模型正确约束，
      Method→Task 的分布先验（"Method X evaluates for Task Y" 语义合理）与 schema 约束冲突，
      导致 type assignment 不稳定。这为 decoding-time enforcement 提供理论动机——
      logit masking 不干扰模型推理过程，因此不存在 prior-constraint conflict。

  - name: "DocRED violation rate (minimal prompt)"
    plan_id: "P003"
    description: >
      Qwen3-8B 零样本抽取 DocRED 998 篇文档（96 relation types），
      minimal prompt，测试大 ontology 下的违规 landscape。
    expected_results:
      total_docs: 998
      parsed_docs: 962
      json_parse_rate: 0.964
      total_entities: 19099
      total_triples: 16540
      entity_type_violation_rate: 0.075
      relation_vocabulary_violation_rate: 0.289
      domain_range_violation_rate: 0.187
      cross_field_consistency_violation_rate: 0.0008
      top_dr_by_rate_P35: 1.0
      top_dr_by_rate_P710: 0.919
      top_dr_by_count_P31_instance_of: 0.604
    result_rationale: >
      18.7% DR 与 SciERC 的 15.4% 可比（despite 14× ontology size difference），
      直接支撑 "violation rate driven by tightness, not ontology size"。
      best 档审稿人接受这一对比为 Claim 1 的关键证据。
      28.9% RV（OOV relation names）在 96-relation ontology 中符合预期——
      模型在大 vocabulary 下更容易 hallucinate 不存在的 relation name。
      这也预示了 grammar 层在 DocRED 上的 F1 提升机制（消除 OOV=FP）。
      7.5% ET 同理，模型在 DocRED 的 entity type system 上表现更差。
    tables:
      - table_id: "T3a"
        caption: "DocRED violation landscape (Qwen3-8B, minimal prompt) — top DR by rate and count"
        description: >
          两个子表：top-10 by rate, top-10 by absolute count。
          展示 long-tail 分布（P35 100% 但仅几个 instance vs P31 60.4% 但 322 violations）。
    figures_description:
      - "Fig 3: Scatter plot of per-relation DR rate vs constraint tightness τ̄ across all 96 DocRED relations，size=triple count，color=violation count"
    analysis: >
      DocRED 的 18.7% DR 与 SciERC 15.4% 在同一量级，而 ontology 复杂度差 14×，
      证明 violation rate 不随 ontology scale 线性增长。真正的驱动因素是 per-relation tightness。
      RV 28.9% 是 DocRED 特有问题（SciERC 仅 1.39%），因为 96 个 Wikidata property ID 
      远超模型的 zero-shot vocabulary 记忆能力。这个 RV-DR 正交性在后续 cross-model 分析中
      成为 D014 dual-factor insight 的基础。

  - name: "DocRED violation rate (schema-informed prompt)"
    plan_id: "P004"
    description: >
      DocRED + schema-informed prompt，测试 prompt-level intervention 在大 ontology 上的 scaling。
    expected_results:
      total_docs: 998
      documents_checked: 943
      parse_failures: 55
      json_parse_rate: 0.9449
      total_entities: 19524
      total_triples: 16782
      entity_type_violation_rate: 0.0061
      relation_vocabulary_violation_rate: 0.1841
      domain_range_violation_rate: 0.1284
      cross_field_consistency_violation_rate: 0.0015
      dr_reduction_pct: -31.3
    result_rationale: >
      DocRED 上 schema prompt 仅降 DR 31.3%（vs SciERC 62.4%），直接证明
      "prompt-level intervention scales poorly with ontology complexity"。
      best 档审稿人接受此 scaling gap 为 Claim 2 在大 ontology 上的推广证据。
      机制清晰：96 个 relation 的约束信息在 prompt 中形成 information overload，
      模型无法同时维持所有约束的 working memory。RV 仅从 28.9%→18.4%（-36%）
      说明 prompt 对 vocabulary 问题的帮助也有限。
    tables: []
    figures_description:
      - "Fig 4: Grouped bar chart comparing DR reduction (%) across SciERC vs DocRED for minimal→schema transition，标注 scaling gap"
    analysis: >
      SciERC -62.4% vs DocRED -31.3% 的 scaling gap 是 Claim 2 的跨数据集验证。
      论文中 frame 为："Prompt-level constraint enforcement shows diminishing returns 
      with ontology scale: 62% reduction on a 7-relation schema vs 31% on 96 relations."
      这建立了 decoding-time enforcement 的 necessity argument。

  # ============================================================
  # Phase 2: SciERC Ablation (4-way + S2)
  # ============================================================
  - name: "SciERC unconstrained baseline"
    plan_id: "P005a"
    description: >
      Phase 2 baseline：与 Phase 0 minimal prompt 相同配置但使用 Phase 2 pipeline，
      确保 ablation 各组共享同一推理环境。
    expected_results:
      total_triples: 1724
      total_entities: 2474
      json_parse_rate: 1.0
      entity_type_violation_rate: 0.004
      relation_vocabulary_violation_rate: 0.0139
      domain_range_violation_rate: 0.1537
      cross_field_consistency_violation_rate: 0.0008
      entity_f1: 0.3101
      relation_f1: 0.0823
    result_rationale: >
      与 P001 数值一致（同 seed、同 prompt、同 checker v2），验证 Phase 2 pipeline 
      未引入额外差异。best 档下这种内部一致性增强 reviewer 对实验严谨性的信心。
      R-F1=8.23% 在 zero-shot setting 下是 expected baseline——supervised SOTA ~40-50%，
      zero-shot 下 8% 符合 "F1 as control variable" framing。
    tables:
      - table_id: "T4"
        caption: "SciERC 4-way ablation results"
        description: >
          4 行 (unconstrained / grammar_only / semantic_only / full_s1)，
          列: Config | ET(%) | RV(%) | DR(%) | CF(%) | E-F1(%) | R-F1(%) | #Triples。
          full_s1 行加粗。
    figures_description: []
    analysis: >
      Baseline 复现确认 Phase 0 → Phase 2 pipeline 无偏差。
      所有后续 ablation Δ 均以此为锚。

  - name: "SciERC grammar-only"
    plan_id: "P005"
    description: >
      仅启用 grammar 层（XGrammar CFG：JSON structure + type/relation vocabulary 约束），
      semantic 层关闭。测试 grammar 层的独立贡献。
    expected_results:
      total_triples: 1725
      total_entities: 2474
      json_parse_rate: 1.0
      entity_type_violation_rate: 0.0
      relation_vocabulary_violation_rate: 0.0
      domain_range_violation_rate: 0.1484
      cross_field_consistency_violation_rate: 0.0008
      entity_f1: 0.3098
      relation_f1: 0.0823
    result_rationale: >
      grammar 层完美消除 ET 和 RV（均→0%），但 DR 基本不变（14.84% vs 15.37%，-3.4%）。
      这在 best 档下是 enabling dependency argument 的核心证据：grammar 确保 vocabulary 合规，
      但无法执行 cross-field 的 domain/range 约束——这需要 semantic 层的 stateful entity registry。
      CF 不变（0.08%）证明 grammar 层不引入 CF（后续确认 CF 100% 来自 semantic 层）。
      F1 几乎不变（-0.03pp E-F1, 0pp R-F1），证明 grammar 约束不降质——
      因为 SciERC 的 RV baseline 很低（1.39%），消除少量 OOV 对 F1 影响微小。
    tables: []
    figures_description:
      - "Fig 5: Stacked bar chart showing violation composition (ET/RV/DR/CF) across 4 ablation configs，visualize each layer's specific contribution"
    analysis: >
      grammar_only 是 ablation 设计中的 "structural floor"：保证 JSON 格式正确 + vocabulary 合规，
      但 DR 几乎不降。这与 semantic_only 的 DR↓24% 形成对比——但 semantic_only 无法消除 RV/ET。
      两层的 complementary coverage 在此清晰展现。
      grammar_only CF=0.08% ≈ unconstrained 0.08%，是后续 "CF 100% 由 semantic 层引入" 消融的关键锚点。

  - name: "SciERC semantic-only"
    plan_id: "P006"
    description: >
      仅启用 semantic 层（TypeConstraintProcessor + entity registry + logit masking），
      grammar 层关闭。测试 semantic 层在无 vocabulary 保障下的独立效果。
    expected_results:
      total_triples: 1726
      total_entities: 2474
      json_parse_rate: 1.0
      entity_type_violation_rate: 0.004
      relation_vocabulary_violation_rate: 0.0151
      domain_range_violation_rate: 0.1165
      cross_field_consistency_violation_rate: 0.0271
      entity_f1: 0.3101
      relation_f1: 0.0815
    result_rationale: >
      semantic_only DR=11.65%（↓24%），远弱于 full_s1 的 ↓94%。
      best 档下这是 enabling dependency 的决定性证据：semantic 层遇到 OOV relation name 时
      无法查找对应的 domain/range rule → 退化为无约束。RV 不变（1.51%）因为 semantic 层
      不管 vocabulary——这是 grammar 层的职责。CF 升至 2.71%（从 0.08%），
      首次显示 semantic 层引入 CF 的趋势（full_s1 将升至 9.9%）。
      R-F1 微降 0.08pp，在统计误差范围内。
    tables: []
    figures_description: []
    analysis: >
      semantic_only ↓24% vs full_s1 ↓94% 的 70pp gap 是 "grammar enables semantic" 
      enabling dependency 的量化证据。Without grammar ensuring valid relation names，
      semantic layer 只能在它碰巧能识别的 relation name 上执行 DR masking。
      这排除了 "两层独立 additive" 的解释——如果独立，
      full_s1 DR 应约等于 grammar_DR × semantic_DR / unconstrained_DR ≈ 11.3%，
      而实际 0.93% 远低于此，证明 enabling 而非 additive composition。

  - name: "SciERC full S1 (grammar + semantic, single-pass)"
    plan_id: "P007"
    description: >
      两层同时启用，single-pass decoding。主要配置，全指标 comprehensive 评估。
    expected_results:
      total_triples: 1729
      total_entities: 2474
      json_parse_rate: 1.0
      entity_type_violation_rate: 0.0
      relation_vocabulary_violation_rate: 0.0
      domain_range_violation_rate: 0.0093
      cross_field_consistency_violation_rate: 0.099
      entity_f1: 0.3098
      relation_f1: 0.0836
      rel_f1_delta_pp: +0.13
      rel_f1_p_value: 0.58
      ent_f1_delta_pp: -0.03
      ent_f1_p_value: 0.53
      dr_reduction_pct: 94.0
      residual_dr_triples: 16
      fallback_events_total: 5882
      fallback_per_doc: 10.7
    result_rationale: >
      DR=0.93%（↓94%）是论文 title "Near-Complete" 的锚定数值。
      best 档审稿人接受 0.93% 为 "near-complete"——16 个残余 DR violation 中
      大部分发生在 Compare 和 Evaluate-for 等 high-tightness relations，
      对应 fallback 事件（semantic mask ∩ grammar mask = ∅ → 退化为 grammar-only）。
      fallback ~10.7 次/doc 说明 semantic masking 覆盖率合理（SciERC 7 relations 相对简单）。
      
      CF=9.9% 是 trade-off 的体现。best 档下审稿人接受这是 honest limitation 而非 fatal flaw，
      因为：(1) DR violation 产生 structurally invalid triples，CF violation 的 individual triples 
      仍然 type-valid；(2) CF 根因是 type system ambiguity（Generic↔OtherScientificTerm 等），
      有独立 analysis 价值；(3) proactive disclosure + severity distinction 防御策略到位。
      
      R-F1 +0.13pp（p=0.58）统计不显著，frame 为 "F1-neutral"。
      best 档下这正是期望结果——constraint enforcement 的价值在 compliance 而非 F1 提升。
    tables:
      - table_id: "T4_full"
        caption: "SciERC full ablation with bootstrap CI"
        description: >
          扩展 T4 增加 95% CI 列和 p-value 列。full_s1 行标注 "primary configuration"。
      - table_id: "T5"
        caption: "SciERC CF subtype analysis"
        description: >
          3 行: EVR (entity-vs-relation drift) | Within-rel | Total。
          列: Subtype | #Entities | Rate(%) | Top conflict pattern。
    figures_description:
      - "Fig 6: Waterfall chart showing DR reduction path: unconstrained (15.37%) → grammar_only (14.84%) → semantic_only (11.65%) → full_s1 (0.93%)，标注 enabling dependency"
    analysis: >
      SciERC full_s1 是论文的 flagship result。DR ↓94% at F1-neutral 完美支撑 Claim 3。
      CF 9.9% 需要在 §5.3 和 §7 双重处理：§5.3 展开 EVR subtype 分析（>90% 是 EVR，
      top pattern Generic↔OtherScientificTerm 60 次），§7 列为 explicit limitation + future work。
      fallback 数据（10.7/doc）支撑 "Constraint Coverage" 指标的引入——
      在 SciERC 上约 85-90% 的 type-token positions 得到 semantic masking 保护。

  - name: "SciERC full S2 (two-pass, ablation)"
    plan_id: "P008"
    description: >
      两遍解码：Pass 1 仅抽 entity（grammar-only），Pass 2 编译 input-dependent grammar + semantic，
      测试 S2 架构变体。已降级为 ablation。
    expected_results:
      total_triples: 1644
      total_entities: 2228
      json_parse_rate: 1.0
      entity_type_violation_rate: 0.0
      relation_vocabulary_violation_rate: 0.0
      domain_range_violation_rate: 0.0097
      cross_field_consistency_violation_rate: 0.0803
      entity_f1: 0.319
      relation_f1: 0.0803
      entity_precision: 0.2797
      entity_recall: 0.3712
    result_rationale: >
      S2 DR=0.97% ≈ S1 0.93%，CF=8.03% vs S1 9.90%（-1.87pp，不显著）。
      best 档下 S2 作为 architectural variant 展示 framework flexibility，
      但不构成 CF solution。审稿人看到 S2 在所有 metric 上 ≤ S1：
      fewer triples (1644 vs 1729)、lower R-F1 (8.03% vs 8.36%)、
      DR 略高——这支持 S1 作为 primary 的决策。
      S2 的存在价值是证明 framework 支持多种 decoding strategy compilation，
      而非锁定在单一架构上。less-is-more：demoting S2 to ablation 
      反而增强了论文的 intellectual honesty，best 档审稿人对此评价正面。
    tables:
      - table_id: "T6"
        caption: "S1 vs S2 comparison (SciERC)"
        description: >
          2 行 (S1/S2), 列: Strategy | #Triples | DR(%) | CF(%) | R-F1(%) | E-F1(%)。
          附 footnote: S2 positioned as ablation, not primary.
    figures_description: []
    analysis: >
      S2 确认 "does NOT solve CF"。在 best 档下这是重要的 null result——
      防止审稿人追问 "why not just use S2 to fix CF"。
      CF 的 EVR subtype 在 S2 下降 27%（245→178 entities），但 within-rel 反增（10→18），
      说明 two-pass 的 entity-first strategy 稳定了 entity-level types 
      但 relation-level type assignment 反而更不一致。
      这个 nuanced trade-off 在 appendix 中 1-2 段解释即可。

  # ============================================================
  # Phase 2: DocRED Ablation (4-way)
  # ============================================================
  - name: "DocRED unconstrained baseline"
    plan_id: "P009"
    description: >
      Qwen3-8B DocRED 998 docs unconstrained baseline（Phase 2 pipeline，checker v2）。
    expected_results:
      documents_checked: 986
      parse_failures: 12
      total_entities: 20171
      total_triples: 17497
      entity_type_violation_rate: 0.0248
      relation_vocabulary_violation_rate: 0.2966
      domain_range_violation_rate: 0.1846
      cross_field_consistency_violation_rate: 0.001
      entity_f1: 58.15
      relation_f1: 7.74
      unrecognized_relations: 5189
    result_rationale: >
      DocRED unconstrained 呈现与 SciERC 不同的 violation profile：
      RV=29.66% 远高于 SciERC 1.39%（96 个 Wikidata property ID 超出模型 vocabulary 记忆），
      ET=2.48% 远高于 SciERC 0.4%。DR=18.46% 与 SciERC 15.37% 可比。
      best 档下这个 RV-DR 正交性（RV 高但 DR comparable）是 D014 dual-factor insight 的基础：
      grammar 消除 RV 后会揭露 latent DR violations，使得 "grammar enables semantic" 
      在 DocRED 上呈现更复杂的动态。5189 个 OOV relations 在 all_set F1 方法下全计为 FP，
      解释了为什么 grammar 层消除 OOV 能直接提升 DocRED F1。
    tables:
      - table_id: "T7"
        caption: "DocRED 4-way ablation results"
        description: >
          4 行 (unconstrained / grammar_only / semantic_only / full_s1)，
          列同 T4 但增加 #Unrecognized_Rels 列。all_set F1 method 标注。
    figures_description: []
    analysis: >
      DocRED baseline 建立了大 ontology 的 violation profile。
      RV 29.66% 将是 grammar 层 F1 提升的机制来源——
      5189 个 OOV relations 被 grammar 强制映射为有效 name 后，
      FP 大幅减少 → precision 提升 → F1 提升。

  - name: "DocRED grammar-only"
    plan_id: "P010"
    description: >
      DocRED 仅 grammar 层，测试 vocabulary/ET 消除效果和 F1 影响。
    expected_results:
      documents_checked: 985
      parse_failures: 13
      total_entities: 20150
      total_triples: 17341
      entity_type_violation_rate: 0.0
      relation_vocabulary_violation_rate: 0.0003
      domain_range_violation_rate: 0.2617
      cross_field_consistency_violation_rate: 0.0007
      entity_f1: 59.38
      relation_f1: 8.31
      relation_recall: 10.12
      unrecognized_relations: 5
    result_rationale: >
      grammar_only 完美消除 ET（→0%）和 RV（→0.03%，仅 5 个残余，可能是 alias 边界情况）。
      关键 finding：DR 从 18.46% 升至 26.17%（+7.71pp）。
      best 档下审稿人理解此反直觉结果的机制：grammar 将 OOV relation names 强制映射为
      有效 vocabulary → 暴露了之前隐藏在 OOV triples 中的 latent DR violations。
      之前这些 triple 的 relation name 无效，checker 可能无法评估其 DR→ 
      现在 relation name 有效了，DR check 才能执行，揭露大量 domain/range 不匹配。
      
      E-F1=59.38%（+1.23pp vs unconstrained 58.15%）直接来自 ET→0% 消除 FP。
      R-F1=8.31%（+0.57pp）来自 RV→0% 消除 OOV FP。
      grammar_only 是 "grammar drives all F1 gain" 的关键证据——
      后续 full_s1 E-F1=59.37%（Δ=-0.01pp, p=0.66）证明 semantic 层对 F1 无贡献。
    tables: []
    figures_description:
      - "Fig 7: Sankey diagram showing triple flow: unconstrained OOV triples (5189) → grammar remapping → revealed DR violations"
    analysis: >
      grammar_only DR↑至 26.17% 是整个 ablation 中最反直觉的数据点。
      论文中需要 1 段解释 "latent DR violation reveal" 机制。
      这也是 D014 dual-factor insight 的关键数据：
      Qwen RV=29.66% >> Llama RV=16.03% → Qwen grammar 揭露更多 latent DR → 
      Qwen full_s1 残余 DR 更高（10.21% vs 2.55%）。
      grammar_only CF=0.07% ≈ unconstrained，再次确认 grammar 不引入 CF。

  - name: "DocRED semantic-only"
    plan_id: "P011"
    description: >
      DocRED 仅 semantic 层，测试无 vocabulary 保障下 semantic 层在大 ontology 上的效果。
    expected_results:
      documents_checked: 987
      parse_failures: 11
      total_entities: 20185
      total_triples: 17571
      entity_type_violation_rate: 0.0422
      relation_vocabulary_violation_rate: 0.2987
      domain_range_violation_rate: 0.1384
      cross_field_consistency_violation_rate: 0.0105
      entity_f1: 57.81
      relation_f1: 7.70
    result_rationale: >
      semantic_only DR=13.84%（↓25%），与 SciERC semantic_only ↓24% 一致，
      进一步验证 "semantic alone without grammar prerequisite" 的 ceiling ~25%。
      RV 不变（29.87%）——semantic 层不管 vocabulary，与预期一致。
      ET 上升至 4.22%（from 2.48%），因为 semantic 层的 logit masking 
      在遇到 OOV relation 时的 fallback 行为可能干扰 entity type generation。
      CF=1.05%（from 0.10%），semantic 层即使在 degraded mode 也开始引入 CF。
      E-F1 微降 0.34pp，R-F1 微降 0.04pp——semantic_only 在 DocRED 上略有负面影响，
      因为没有 grammar 层保障 vocabulary，semantic masking 在 OOV context 中产生 noise。
    tables: []
    figures_description: []
    analysis: >
      semantic_only 在两个数据集上一致展现 ~25% DR ceiling，
      强化 "grammar is prerequisite" 的 enabling dependency argument。
      ET 上升（2.48%→4.22%）是 semantic 层 "在 OOV 环境中挣扎" 的信号——
      当 relation name 不在 valid vocabulary 中，TypeConstraintProcessor 
      无法查找 domain/range rule，其 fallback 行为可能 inadvertently 
      影响相邻的 entity type token generation。
      这个 negative interaction 在 full system 中被 grammar 层 prevent。

  - name: "DocRED full S1"
    plan_id: "P012"
    description: >
      DocRED grammar+semantic single-pass，主要配置，完整评估。
    expected_results:
      documents_checked: 987
      parse_failures: 11
      total_entities: 20187
      total_triples: 17341
      entity_type_violation_rate: 0.0
      relation_vocabulary_violation_rate: 0.0003
      domain_range_violation_rate: 0.1021
      cross_field_consistency_violation_rate: 0.0257
      entity_f1: 59.37
      relation_f1: 8.23
      rel_f1_delta_pp: +0.50
      rel_f1_p_value: "<0.001"
      rel_f1_ci_95: "[+0.23, +0.81]"
      ent_f1_delta_pp: +1.23
      ent_f1_p_value: "<0.001"
      ent_f1_ci_95: "[+0.94, +1.55]"
      dr_reduction_pct: 44.7
      fallback_events_per_doc_est: "~57"
      unrecognized_relations: 5
    result_rationale: >
      DR=10.21%（↓44.7%）远弱于 SciERC ↓94%。best 档下审稿人接受 D014 dual-factor 解释：
      不是方法在 DocRED 上失败，而是 Qwen 的高 RV baseline（29.66%）经 grammar 消除后
      暴露大量 latent DR violations，加上 DocRED ontology 高 tightness（τ̄=0.842）
      导致更多 semantic mask ∩ grammar mask = ∅ 的 fallback 事件（~57 次/doc vs SciERC 10.7 次/doc）。
      fallback 退化为 grammar-only（DR ~26.17%）→ 高 fallback = 高残余 DR。
      
      F1 双双显著提升：R-F1 +0.50pp (p<0.001), E-F1 +1.23pp (p<0.001)。
      best 档下这是 bonus finding（不升级为 core claim）：机制清晰，
      grammar 消除 OOV → 减少 FP → precision 提升。grammar_only E-F1=59.38% ≈ full_s1 59.37%
      确认 semantic 层对 F1 零贡献——F1 提升完全来自 grammar 层。
      
      CF=2.57% 远低于 SciERC 9.9%。DocRED 的 entity type system（PER/LOC/ORG 等）
      比 SciERC（Generic/OtherScientificTerm 等）语义边界更清晰，
      因此 type assignment 跨 relation 更一致。
    tables:
      - table_id: "T7_full"
        caption: "DocRED full ablation with bootstrap CI and significance tests"
        description: >
          扩展 T7 增加 CI 和 p-value 列。full_s1 R-F1/E-F1 significance 用 ** 标注。
      - table_id: "T8"
        caption: "Fallback frequency comparison (SciERC vs DocRED)"
        description: >
          2 行 (SciERC/DocRED), 列: Dataset | Fallback_total | Fallback_per_doc | DR_residual(%) | τ̄。
    figures_description:
      - "Fig 8: Dual-axis plot: fallback frequency per doc vs residual DR(%) across SciERC and DocRED，标注 Constraint Coverage metric"
    analysis: >
      DocRED full_s1 展示了方法在高复杂度 ontology 上的 honest performance profile。
      ↓44.7% 不如 SciERC ↓94% 但仍 substantial（18.46%→10.21%），
      加上 ET→0%、RV→0% 的完全消除和 F1 显著提升，整体效果是正面的。
      D014 dual-factor 解释把 weaker DR reduction 从弱点转为 analytical finding：
      "residual DR is predictable from constraint tightness × model RV baseline"。
      Constraint Coverage 指标量化了 semantic masking 在 DocRED 上的有效覆盖率（~40-50%），
      为 future work（更好的 fallback strategy）提供了定量 baseline。

  # ============================================================
  # Phase 2: Cross-Model (Llama-3.1-8B)
  # ============================================================
  - name: "Llama SciERC unconstrained"
    plan_id: "P013"
    description: >
      Llama-3.1-8B zero-shot SciERC unconstrained，建立 cross-model baseline。
      零代码修改——same prompt, same pipeline, different model weights。
    expected_results:
      total_entities: 2451
      total_relations: 1274
      json_parse_failures: 1
      entity_type_violation_rate: 0.0
      relation_vocabulary_violation_rate: 0.0055
      domain_range_violation_rate: 0.1334
      cross_field_consistency_violations: 6
      entity_f1: 0.2356
      relation_f1: 0.0268
    result_rationale: >
      Llama SciERC unconstrained 展示了不同的 violation profile：
      DR=13.34%（vs Qwen 15.37%，lower），RV=0.55%（vs Qwen 1.39%，lower），
      ET=0%（vs Qwen 0.4%，same range）。
      best 档下这一跨模型 violation landscape 对比有独立 value：
      不同模型在同一 ontology 上的 violation patterns 不同但 rates comparable，
      说明 violations 是任务结构性问题而非特定模型的 idiosyncrasy。
      R-F1=2.68% 显著低于 Qwen 8.23%，因为 Llama 在 SciERC format 上 recall 更差，
      但这不影响 constraint evaluation——low F1 ≠ low violation rate 的分离本身有 insight 价值。
      fewer relations extracted (1274 vs 1724) 说明 Llama 更保守但不更 accurate per-triple。
    tables:
      - table_id: "T9"
        caption: "Cross-model comparison: Qwen vs Llama on SciERC"
        description: >
          2 大行 (Qwen/Llama) × 2 小行 (unconstrained/full_s1)，
          列: Model | Config | ET(%) | RV(%) | DR(%) | CF(%) | R-F1(%) | Parse_fail(%)。
    figures_description: []
    analysis: >
      Llama baseline 确认 violation 是 task-structural 而非 model-specific。
      ET=0% 有趣——Llama 对 SciERC entity types 的 vocabulary 记忆优于 Qwen，
      但 DR 仍有 13.34%，说明 vocabulary correctness ≠ semantic correctness，
      进一步支撑 two-layer design rationale。

  - name: "Llama SciERC full S1"
    plan_id: "P014"
    description: >
      Llama-3.1-8B + OntoCoDec full S1 on SciERC。核心 cross-model generalization 实验。
    expected_results:
      samples: 550
      entities_extracted: 2469
      relations_extracted: 1315
      domain_range_violation_rate: 0.0008
      relation_vocabulary_violation_rate: 0.0
      entity_type_violation_rate: 0.0
      cross_field_consistency_violation_rate: 0.0656
      entity_f1: 0.2349
      relation_f1: 0.0254
      dr_reduction_pct: 99.4
    result_rationale: >
      DR=0.08%（↓99.4%）——比 Qwen 的 ↓94% 更强。
      best 档下这是最有力的 cross-model evidence：零代码修改，DR 近乎完全消除。
      机制：Llama SciERC RV baseline 已经很低（0.55%），grammar 层几乎无需做 vocabulary 修正，
      semantic 层直接在 clean vocabulary 上高效执行 domain/range masking → 更少 fallback → 
      更低残余 DR。这与 D014 dual-factor model 完美一致：
      low RV baseline → fewer latent DR reveals → lower residual DR。
      
      CF=6.56%（vs Qwen 9.90%），仍然 elevated。Llama 的 type assignment 
      在 SciERC ambiguous types 上比 Qwen 稍稳定但仍受 type system ambiguity 影响。
      R-F1=2.54%（-0.14pp from unconstrained 2.68%），F1-neutral。
      best 档审稿人接受 2 模型 × 2 数据集为 sufficient generalization evidence，
      但 may suggest additional models in future work。
    tables: []
    figures_description:
      - "Fig 9: Bar chart comparing DR reduction % across 4 cells of 2×2 matrix (Qwen×SciERC, Qwen×DocRED, Llama×SciERC, Llama×DocRED)"
    analysis: >
      Llama SciERC ↓99.4% 是 2×2 matrix 中最强的单 cell。
      与 Qwen SciERC ↓94% 的差距来自 RV baseline 差异（0.55% vs 1.39%）——
      lower RV → less latent DR reveal → purer semantic enforcement。
      这支撑论文的 programmatic claim "generalizes across model families without code modification"。
      CF=6.56% 在 limitations 中需提及 "non-local constraint 问题在 Llama 上更突出"——
      虽然低于 Qwen 9.9%，但考虑到 Llama fewer relations extracted（1315 vs 1729），
      per-entity CF probability 可能更高。

  - name: "Llama DocRED unconstrained"
    plan_id: "P015"
    description: >
      Llama-3.1-8B DocRED unconstrained baseline。测试不同 model family 在大 ontology 上的 violation profile。
    expected_results:
      documents: 998
      documents_checked: 930
      parse_failures: 68
      unique_entities: 11525
      total_triples: 16437
      ET_rate_pct: 0.13
      RV_rate_pct: 16.03
      DR_rate_pct: 26.07
      CF_rate_pct: 0.17
      entity_f1: 55.65
      relation_f1: 5.98
      fuzzy_relation_matches: 121
    result_rationale: >
      Llama DocRED 展示 RV↓DR↑ 正交性：RV=16.03%（vs Qwen 29.66%, lower）
      但 DR=26.07%（vs Qwen 18.46%, higher）。
      best 档下这是 D014 insight 的关键对比数据——vocabulary compliance 和 semantic compliance 
      是正交 failure modes，不同模型在两个维度上的表现可以反向。
      parse_failures=68/998=6.8%（vs Qwen 12/998=1.2%）——Llama 的 JSON format compliance 更差，
      但 bias 方向是保守的（parse failure 不计入 F1 也不计入 violation rate，不利于 constrained condition）。
      E-F1=55.65%（vs Qwen 58.15%），Llama 在 DocRED entity extraction 上略弱。
    tables: []
    figures_description:
      - "Fig 10: 2×2 heatmap showing RV(%) and DR(%) for Qwen×DocRED and Llama×DocRED，标注 orthogonality"
    analysis: >
      RV↓DR↑ 正交性是跨模型分析最重要的 finding。
      Llama vocabulary 记忆更好（RV 16% vs 30%）但 semantic constraint compliance 更差（DR 26% vs 18%），
      证明 "knowing the right relation name ≠ knowing the right type constraint"。
      这为两层设计提供了 model-agnostic justification：
      任何模型都可能在 vocabulary 或 semantics 上各有强弱，
      两层分别 address 正交维度。

  - name: "Llama DocRED full S1"
    plan_id: "P016"
    description: >
      Llama-3.1-8B + OntoCoDec full S1 on DocRED。2×2 matrix 的最后一个 cell。
    expected_results:
      documents: 998
      documents_checked: 907
      parse_failures: 91
      unique_entities: 11296
      total_triples: 16368
      ET: 0.0
      RV: 0.0
      DR: 2.55
      CF: 12.02
      entity_f1: 55.01
      entity_precision: 61.41
      entity_recall: 49.82
      relation_f1: 6.27
      relation_precision: 5.49
      relation_recall: 7.32
      dr_reduction_pct: 90.2
      ent_f1_delta_pp: -0.64
      rel_f1_delta_pp: +0.29
    result_rationale: >
      DR=2.55%（↓90.2%）——大幅优于 Qwen ↓44.7%。
      best 档下 D014 dual-factor model 完美解释此差异：
      Llama RV=16.03% << Qwen RV=29.66% → grammar 消除 fewer OOV → 
      fewer latent DR reveals → semantic 层在 cleaner input 上更有效 → lower residual DR。
      同一 ontology（τ̄=0.842）、同一方法、同一 pipeline——
      DR reduction 差异（90.2% vs 44.7%）完全由 model RV baseline 差异解释。
      这是比单一 tightness 更深的 insight，审稿人在 best 档认可为独立 finding。
      
      CF=12.02%——2×2 matrix 中最高。Llama 在 DocRED entity types 上的 cross-relation 
      type assignment 一致性最差。这与 parse_failures=91（9.1%，也是最高）相关——
      Llama 在 DocRED 上的生成 stability 整体较弱。
      best 档审稿人接受此 CF 作为 limitation 的一部分，
      因为 per-triple type validity 仍然保证（CF 是 cross-triple consistency 问题）。
      
      E-F1=55.01%（-0.64pp），轻微下降。best 档下需 footnote 说明 
      parse_failures 增加（68→91）可能是 constrained decoding 在 Llama 上 
      偶尔产生更多 format compliance issue（但仍 <10%），
      且 bias 方向保守。R-F1=6.27%（+0.29pp）微正。
    tables:
      - table_id: "T10"
        caption: "Complete 2×2 cross-model × cross-dataset matrix"
        description: >
          4 大行 (Qwen-SciERC / Qwen-DocRED / Llama-SciERC / Llama-DocRED) × 
          2 小行 (unconstrained / full_s1)，
          列: Model | Dataset | Config | ET(%) | RV(%) | DR(%) | CF(%) | R-F1(%) | E-F1(%) | Parse_fail(%) | DR_Δ(%)。
          这是论文的 central results table。
      - table_id: "T11"
        caption: "D014 dual-factor analysis: tightness × RV baseline → DR reduction"
        description: >
          4 行 (matrix cells), 列: Cell | τ̄ | RV_baseline(%) | DR_unconstrained(%) | 
          DR_full_s1(%) | DR_Δ(%) | Predicted_factor。标注 RV baseline 解释的 variance。
    figures_description:
      - "Fig 11: Scatter plot with 4 points: x=RV_baseline, y=DR_reduction_pct, color=dataset, shape=model. 标注 RV-DR_reduction 正相关趋势线（仅 2 model，descriptive not inferential）"
    analysis: >
      Llama DocRED full_s1 完成了 2×2 matrix。DR reduction spectrum：
      99.4% (Llama-SciERC) > 94% (Qwen-SciERC) > 90.2% (Llama-DocRED) > 44.7% (Qwen-DocRED)。
      这个 ordering 完美映射到 RV baseline ordering：
      0.55% < 1.39% < 16.03% < 29.66%——lower RV baseline → higher DR reduction。
      D014 claim "DR reduction ceiling 由 tightness × model RV baseline 共同决定" 
      获得 4-cell empirical support。
      
      CF gradient 也有 pattern：SciERC CF (6.56-9.9%) > DocRED CF (2.57-12.02%)，
      但 Llama DocRED CF=12.02% 是 outlier——可能与 Llama 在 DocRED 上的高 parse failure 
      和更弱的 format stability 相关。limitations 中需讨论。

  # ============================================================
  # Supplementary Experiments
  # ============================================================
  - name: "S2 pilot (50 docs)"
    plan_id: "P017"
    description: >
      S2 two-pass strategy 在 SciERC 前 50 篇上的 pilot run，验证 pipeline 正确性后再跑 full scale。
    expected_results:
      samples: 50
      predicted_relations: 146
      domain_range_violation_rate: 0.0205
      relation_vocabulary_violation_rate: 0.0
      relation_f1: 0.1008
      true_positives: 13
      gold_relations: 112
    result_rationale: >
      pilot DR=2.05%（3/146 triples），为 full run 提供了 S2 pipeline 功能验证。
      best 档下审稿人不会看到 pilot 数据——它只出现在 supplementary material 或被完全省略。
      pilot 的历史作用是决策支持（go/no-go for full S2 run）。
      注意 pilot 最初报告 DR=0% 是 small-sample artifact（n=25 triples from dryrun），
      actual pilot50 为 2.05%。论文中严禁引用 pilot DR=0%。
    tables: []
    figures_description: []
    analysis: >
      pilot 仅作为 engineering checkpoint。full run P008 (DR=0.97%) 是唯一有效的 S2 evidence。
      best 档论文中不引用 pilot 数据。

  - name: "Post-hoc filtering baseline"
    plan_id: "P018"
    description: >
      对 unconstrained output 应用 post-hoc violation filtering（删除含 DR/ET violation 的 triples），
      作为 naive baseline 与 OntoCoDec 进行多维对比。
    expected_results:
      docred_f1_before: 7.74
      docred_f1_after: 9.61
      docred_precision_after: 11.22
      docred_recall_before: 9.46
      docred_recall_after: 8.40
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
    result_rationale: >
      post-hoc F1 > OntoCoDec F1（SciERC 8.63 vs 8.36, DocRED 9.61 vs 8.23）。
      best 档下审稿人理解 "post-hoc wins on F1" 不构成 fatal weakness，
      因为论文 framing 是多维对比而非 F1 竞赛。关键维度：
      
      1. Recall preservation: OntoCoDec recall 上升（+0.20pp SciERC, +0.56pp DocRED）
         vs post-hoc recall 下降（-0.72pp, -1.06pp）。概率质量重分配 vs 信息删除。
      2. Information coverage: DocRED post-hoc 丢弃 48.1% triples（近半数信息），
         OntoCoDec 保留全部 triple slots。
      3. 127 个被删 TP (DocRED): 正确提取但 entity type 违规的 triple，
         OntoCoDec 通过生成时强制合法 type 保留这些 TP——"prevent vs detect" 核心论据。
      4. ET 残余: post-hoc 只删 triples 不改 entity list，残余 ET=2.47% (DocRED)。
         OntoCoDec ET=0%。Post-hoc 根本无法解决 entity type violations。
      
      best 档审稿人被多维对比说服，不会追问 "why not just post-hoc"。
    tables:
      - table_id: "T12"
        caption: "OntoCoDec vs post-hoc filtering: multi-dimensional comparison"
        description: >
          2 数据集 × 3 方法 (unconstrained / OntoCoDec / post-hoc)，
          列: Method | DR(%) | ET(%) | R-F1(%) | Precision(%) | Recall(%) | Rejection(%) | #TP | Coverage。
          OntoCoDec 和 post-hoc 各自的优势列标绿/蓝。
    figures_description:
      - "Fig 12: Radar chart (4 axes: DR elimination, recall preservation, information coverage, ET elimination) comparing OntoCoDec vs post-hoc，visualize multi-dimensional trade-off"
    analysis: >
      post-hoc 是论文必须 beat（or credibly argue against）的 strongest naive baseline。
      best 档下多维 framing 成功：F1 差异 acknowledged but contextualized。
      127 个被删 TP 是最有力的数据点——这些是 post-hoc 的 collateral damage，
      OntoCoDec 通过 generation-time constraint 保留了它们。
      "prevent vs detect" 叙事在 best 档获得 2/3 审稿人认可。

  - name: "Bootstrap CI (10000 iterations)"
    plan_id: "P019"
    description: >
      对 SciERC 和 DocRED 的 unconstrained vs full_s1 F1 差异进行 10000 次 bootstrap 
      重采样，计算 95% CI 和 permutation p-value，提供统计显著性证据。
    expected_results:
      scierc_rel_f1_delta: +0.13
      scierc_rel_f1_p: 0.58
      scierc_ent_f1_delta: -0.03
      scierc_ent_f1_p: 0.53
      docred_rel_f1_delta: +0.50
      docred_rel_f1_p: "<0.001"
      docred_rel_f1_ci: "[+0.23, +0.81]"
      docred_ent_f1_delta: +1.23
      docred_ent_f1_p: "<0.001"
      docred_ent_f1_ci: "[+0.94, +1.55]"
    result_rationale: >
      best 档下 bootstrap CI 提供了 reviewers 期望的统计严谨性。
      SciERC p=0.58/0.53 → "F1-neutral"，exactly 论文 framing 需要的结论。
      DocRED p<0.001 for both R-F1 and E-F1 → "statistically significant improvement"，
      但不升级为 core claim（归因于 OOV elimination 的 grammar 层，不是约束解码的 inherent benefit）。
      CI 宽度合理（R-F1 CI width=0.58pp, E-F1 CI width=0.61pp），
      10000 iterations 在 ML 论文中是标准做法。
      
      审稿人在 best 档接受 "F1-neutral on SciERC, significant improvement on DocRED" 
      的 dataset-dependent framing，因为机制归因清晰（grammar 消除 OOV → 减 FP → 提 precision），
      不是 magic improvement 而是 well-understood 的 side-effect。
    tables:
      - table_id: "T13"
        caption: "Bootstrap CI for F1 impact (10000 iterations)"
        description: >
          4 行 (SciERC-Rel / SciERC-Ent / DocRED-Rel / DocRED-Ent)，
          列: Metric | Δ(pp) | 95% CI | p-value | Significance。
    figures_description:
      - "Fig 13: Bootstrap distribution histograms (4 panels) with observed Δ marked by vertical line and 95% CI shaded"
    analysis: >
      bootstrap 结果在 best 档下是 Claim 6 (F1 impact) 的 definitive evidence。
      不同数据集不同结果这一事实本身就有 insight 价值——
      constraint enforcement 的 F1 impact 取决于 baseline violation profile 
      (high RV → OOV elimination → F1 boost; low RV → minimal F1 effect)。
      这个 conditional 关系比 blanket "constraint improves F1" 更 nuanced 也更可信。

  - name: "DocRED schema compilation (Phase 0 R2)"
    plan_id: "P020"
    description: >
      DocRED schema-informed prompt 第二轮尝试（不同 prompt 格式）。已被 P004 supersede，killed。
    expected_results:
      status: killed
      reason: "superseded by P004"
    result_rationale: >
      P020 被 kill 因为 P004 已提供充分的 DocRED schema-informed baseline。
      best 档下此实验不出现在论文中，仅在 experiment registry 中记录为 "killed"。
      不需要额外解释或 justification。
    tables: []
    figures_description: []
    analysis: >
      无分析价值。记录保留用于实验管理 audit trail。
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8d18bb91-f1e1-4a1f-a0a4-e2a42efac0fe",
  "isSidechain": false,
  "requestId": "req_011Cb38Etvq8NXc6NgvHCXdg",
  "type": "assistant",
  "uuid": "56d2655f-07c7-450e-901a-9247e19fef0b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6",
  "sessionId": "3bf11c38-e586-47ea-b7d9-62bfeddfd8ee",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VyNuWJ5jvbJvbfFKpVjd1R",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7954,
      "cache_read_input_tokens": 30648,
      "output_tokens": 17087,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7954,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 17087,
          "cache_read_input_tokens": 30648,
          "cache_creation_input_tokens": 7954,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7954
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

_source line 21_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：所有核心假设经受审稿检验；CF 被接受为 honest limitation 而非致命缺陷；novelty 认定充分 核心假设：[\"审稿人接受 'near-complete' framing（DR 0.93% SciERC / 2.55% Llama DocRED 足够接近 0%）\", 'CF trade-o…",
  "leafUuid": "56d2655f-07c7-450e-901a-9247e19fef0b",
  "sessionId": "3bf11c38-e586-47ea-b7d9-62bfeddfd8ee"
}
```

---

### Runtime record

_source line 22_

```json
{
  "type": "ai-title",
  "aiTitle": "OntoCoDec constraint enforcement framework paper",
  "sessionId": "3bf11c38-e586-47ea-b7d9-62bfeddfd8ee"
}
```

---

### Runtime record

_source line 23_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：所有核心假设经受审稿检验；CF 被接受为 honest limitation 而非致命缺陷；novelty 认定充分 核心假设：[\"审稿人接受 'near-complete' framing（DR 0.93% SciERC / 2.55% Llama DocRED 足够接近 0%）\", 'CF trade-o…",
  "leafUuid": "56d2655f-07c7-450e-901a-9247e19fef0b",
  "sessionId": "3bf11c38-e586-47ea-b7d9-62bfeddfd8ee"
}
```

---

### Runtime record

_source line 24_

```json
{
  "type": "ai-title",
  "aiTitle": "OntoCoDec constraint enforcement framework paper",
  "sessionId": "3bf11c38-e586-47ea-b7d9-62bfeddfd8ee"
}
```

---
