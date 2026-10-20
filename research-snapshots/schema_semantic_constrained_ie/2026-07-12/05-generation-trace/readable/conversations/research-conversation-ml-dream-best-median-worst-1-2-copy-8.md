# Research conversation: 你是一位经验丰富的 ML 研究者。基于以下研究信息，为 Dream 模拟定义三档场景。 你需要同时定义 best / median / worst 三档： 1. 每档的核心假设（哪些假设成立/不成立） 2. 每档的关键实验指标预期范围（确保

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-3/f750eaf8-1f4f-4233-ab88-16d311b78e03.jsonl`
- **Structured JSON:** [`996f8dabfae4257e8825.json`](../../sessions/99/996f8dabfae4257e8825.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-16T17:32:50.721Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-16T17:32:50.721Z",
  "sessionId": "f750eaf8-1f4f-4233-ab88-16d311b78e03",
  "content": "你是一位经验丰富的 ML 研究者。基于以下研究信息，为 Dream 模拟定义三档场景。\n\n你需要同时定义 best / median / worst 三档：\n1. 每档的核心假设（哪些假设成立/不成立）\n2. 每档的关键实验指标预期范围（确保 best ≥ median ≥ worst 一致性）\n3. 每档的论文叙事方向——\n   - best: 原始 framing 完全成立，claims 无需调整\n   - median: 部分假设未完全验证，需要调整 claims 强度或补充实验\n   - worst: 核心假设不成立，需要找到新的 angle 来 reframe（但仍冲同一 venue，不降级目标）\n\n三档的具体含义不预设——根据这个研究的 paper_framing、已有数据和方法特性\n自行判断。但必须确保三档之间的数字和叙事逻辑一致。\n\n# Project context\nproject: schema_semantic_constrained_ie\nvenue: EMNLP 2026\nfocus: 最终评估：54 实验全部完成，FT ablation 8/8 互补性确认，post-hoc defense 成立，latency ≤5.4%。关注：claim 强度是否匹配证据、limitations 是否充分、novelty 定位 vs SynCode/IterGen/BoostCD 差异化是否清晰。\n\n## paper_framing.md\n\n# OntoCoDec — Paper Framing\n\n## Target Venue\nEMNLP 2026 (ARR submission May 25, 2026)\n\n## Title\nOntoCoDec: Type-Valid Information Extraction via Compiled Ontology Constraints\n(D015: \"Near-Complete\" dropped — DocRED residual DR=10.21% (Qwen) 不算 near-complete。论文贡献是方法，不是特定消除率。SciERC 0.93% 和 DocRED 2.55% (Llama) 可在正文中描述为 near-complete，但 title 不宜 overclaim。)\n\n## Core Insight\nLLM-based IE systems produce systematic ontology constraint violations concentrated in specific relation types. Prompt-level intervention (schema-informed prompting) reduces violations by ~62% but cannot eliminate them — certain relation types retain 25-30% violation rates even with explicit constraint descriptions. OntoCoDec provides **near-complete elimination (DR 15.4%→0.93%, ↓94%) at zero or positive F1 impact** through automatic ontology-to-decoder constraint compilation with two complementary layers.\n\n**Phase 2 confirmed (D012 bootstrap CI, v2 fix)**: Grammar+Semantic dual-layer constrained decoding reduces domain/range violations by 94%, eliminates entity-type and relation-vocabulary violations entirely (→0%). F1 impact is **dataset-dependent**:\n- SciERC: Rel F1 neutral (+0.13pp, p=0.58), Ent F1 neutral (-0.03pp, p=0.53)\n- DocRED: Rel F1 **significantly improved** (+0.50pp, p<0.001, 95% CI [+0.23, +0.81]); Ent F1 **significantly improved** (+1.23pp, p<0.001, 95% CI [+0.94, +1.55])\n- Mechanism: grammar 消除 OOV relation names (DocRED RV 29.66%→0.03%) + 非标 entity types (ET 2.48%→0%)。all_set F1 方法下 OOV=FP → fewer FP → higher precision/F1。SciERC baseline RV/ET 已很低，效果不显著。\n- **Grammar 层是 F1 提升的唯一来源**: grammar_only Ent F1=59.38% ≈ full_s1 59.37% (Δ+0.01pp, p=0.66)。Semantic 层对 F1 无额外贡献，专注 DR reduction。\n\n## Core Claims\n\n### Claim 1 (Empirical): Violation Landscape\nLLM-based IE systems violate ontology type constraints at non-trivial rates (15.4% per-triple on SciERC, 18.7% on DocRED). Violations are **not uniformly distributed** — they concentrate on relation types with tight domain/range constraints (Feature-of 33.5%, Compare 42.4%) while loose-constraint relations show near-zero violation (Used-for 0.8%).\n\n**Key insight**: Violation rate is driven by **constraint tightness**, not ontology size. A small ontology with tight constraints can produce more violations than a large ontology with loose constraints.\n\n**D014 修订**: DR reduction ceiling 由 **tightness × model RV baseline** 共同决定，非 tightness 单因素。Llama DocRED DR↓90.2% vs Qwen DR↓44.7%（同一 ontology τ̄=0.842）。机制：Qwen RV=29.66% >> Llama RV=16.03% → grammar 层将 OOV triples 强制匹配有效关系名 → 揭露大量 latent DR violations → 残余 DR 更高。这是比单一 tightness 更深的 insight。\n\n**Evidence**: SciERC (7 relations) 15.4%; DocRED (96 relations) 18.7% — comparable rates despite 14× ontology size difference. Schema-informed prompt on DocRED only achieves DR↓32% (vs SciERC ↓62%), confirming **prompt-level intervention scales poorly with ontology complexity**.\n\n### Claim 2 (Empirical): Prompt Insufficiency\nSchema-informed prompting (explicitly describing domain/range constraints in the prompt) reduces but does not eliminate violations:\n- Overall: 15.4% → 5.78% (-62.4%), still above 5%\n- Per-relation: Compare 42.4% → 27.6%, Evaluate-for 24.1% → 29.9% (**worse**)\n- Prompt intervention is unreliable at the per-relation level — some relations improve, one regresses\n\n**Narrative**: This is NOT about \"5.78% barely above 5%\". The story is: **prompt-level intervention is fundamentally unreliable as a guarantee mechanism**. It works statistically but cannot provide per-instance compliance. Three specific relation types retain >10% violation rates with schema-informed prompts. For safety-critical IE (biomedical, legal, regulatory), statistical reduction is insufficient — guaranteed compliance is required.\n\n### Claim 3 (Methodological): Composable Constraint Framework\nOntoCoDec automatically compiles IE ontology schemas into two composable constraint layers:\n1. **Grammar layer** (XGrammar): JSON structure + type vocabulary constraints (CFG-expressible)\n2. **Semantic layer** (TypeConstraintProcessor): Cross-field domain/range constraints via stateful entity registry + dynamic logit masking\n\nThe two layers are **complementary with enabling dependency**: grammar ensures every generated relation type is in the valid vocabulary, which enables the semantic layer to look up and enforce domain/range rules for that type. Without grammar, the semantic layer encounters unknown relation types and cannot enforce constraints (explaining why semantic_only achieves only ↓24% vs full_s1 ↓94%). This is NOT \"synergistic\" (mutual amplification) — grammar is a prerequisite for semantic, not vice versa.\n\nThe two layers compose via bitwise AND of token masks. Recommended framing: \"Grammar and semantic constraints compose via bitwise AND with an enabling dependency: grammar ensures structural validity, enabling semantic constraints to enforce domain/range rules. When constraint tightness creates empty intersection between layers, the system degrades gracefully to grammar-only constraints, maintaining structural validity as a guaranteed floor.\"\n\n**Graceful degradation + Fallback 频率量化** (D008 + Reviewer 发现):\nWhen $M_{semantic} \\cap M_{grammar} = \\emptyset$, the system falls back to grammar-only control.\n\n**关键量化数据（Reviewer 从日志挖掘）**:\n- Llama DocRED full_s1: **32,921 次 fallback / 577 docs = ~57 次/doc**\n- Llama SciERC full_s1: **5,882 次 fallback / 550 docs = ~10.7 次/doc**\n- DocRED fallback 频率是 SciERC 的 **5.3×**\n- Qwen DocRED fallback 率未知（日志当时无 fallback logging，需估算）\n\n**这直接解释了 DocRED DR 残余 10.19% vs SciERC 0.93%**: 更多 token 位置退化为 grammar-only → grammar-only 的 DR 已知为 26.17% → 高 fallback = 高残余 DR。\n\n**论文建议**: 在 §5 tightness 段报告 fallback 率，定义 \"Constraint Coverage\" 指标（semantic masking 实际生效的 token 比例）。这把 \"10.19% DR 残余\" 从弱点变成可量化分析的 finding。Frame as \"engineering robustness\" in §4; fallback 频率 + tightness 作为 §5 定量分析。\n\n**Decidability taxonomy**: Constraints classified by prefix-decidability:\n- (a) Purely local: entity type ∈ vocabulary (grammar layer)\n- (b) Prefix-decidable with state: relation argument types compatible with domain/range (semantic layer, requires entity registry)\n- (c) Truly non-local: forward coreference — out of scope for forward-only decoding\n\n### Claim 4 (Methodological): S1 vs S2 Decoding Strategies — Architectural Ablation\n- S1 (single-pass): Both layers applied throughout generation. **Recommended primary strategy** — simpler, slightly better metrics across the board.\n- S2 (two-pass): Pass 1 extracts entities (grammar-only), Pass 2 generates relations with input-dependent grammar compiled from Pass 1 entities.\n\n**S2 full results (551/551 SciERC)**: DR 0.97% (vs S1 0.93%), CF 8.03% (vs S1 9.9%), R-F1 8.03% (vs S1 8.36%). S2 does NOT solve CF — the 1.87pp reduction is not significant. S2 also slightly worse on DR and F1. **S2 is an architectural variant demonstrating framework flexibility, not a CF solution.** Position in paper as ablation (Section 5 or Appendix), not as a core contribution.\n\n⚠️ **Do NOT cite pilot50 DR=0% as S2 evidence** — small-sample artifact; full run shows DR=0.97%. Per-relation S2 DR is worse than S1 on Compare (4.6% vs 2.82%), Part-of (1.25% vs 0%), Used-for (0.12% vs 0%).\n\n## Anticipated Reviewer Concerns\n\n### C1: \"5.78% is barely above 5% — threshold is arbitrary\"\n**Response**: Don't argue about the threshold. Argue about per-relation distribution: Compare (27.6%), Evaluate-for (29.9%), Feature-of (11.3%) have double-digit violation rates with schema-informed prompt. The value proposition is per-relation guaranteed compliance, not overall statistical rate.\n\n### C2: \"Why not just post-hoc filter?\"\n**Response (D013, 实验结果已出)**:\n\nPost-hoc filtering 实验结果：post-hoc F1 > OntoCoDec F1（SciERC 8.63 vs 8.36, DocRED 9.61 vs 8.24）——因 low F1 regime 下移除 FP 大幅提升 precision。\n\n**论文 framing（不以 F1 论高低，多维对比）**:\n1. **Recall 维度（核心论点）**: OntoCoDec recall 上升 (SciERC +0.20pp, DocRED +0.56pp) = 概率质量重分配到合法 token 生效。Post-hoc recall 下降 (SciERC -0.72pp, DocRED -1.06pp) = 正确 triple 被误删。\n2. **Information coverage**: DocRED post-hoc 丢弃 **48.1%** triples（近半数信息丢失），SciERC 16.8%。OntoCoDec 保留全部 triple slots。\n3. **Operational**: OntoCoDec 产出即合规、无需后处理、支持流式。Post-hoc 需额外管线、不适用实时场景。\n4. **Precision trade-off（诚实承认）**: \"Post-hoc achieves higher precision by removing a large fraction of triples, many of which are incorrect. This trades information coverage for precision — valid when FP are costly, but inadequate when completeness matters.\"\n\n数据表：SciERC post-hoc rejection 16.8%, OntoCoDec recall 11.60 vs post-hoc 10.68; DocRED post-hoc rejection 48.1%, OntoCoDec recall 10.02 vs post-hoc 8.40。\n\n**Reviewer 补充发现（D013 后）**:\n5. **ET 残余**：post-hoc 只删 triples 不改 entity list，残余 ET=0.4% (SciERC) / 2.47% (DocRED)。OntoCoDec ET=0%。Post-hoc 无法解决 entity type 违规。\n6. **127 个被删 TP (DocRED)**：过滤前 TP=1137，过滤后 TP=1010。丢失的 127 个 TP（11.2%）是正确提取但 entity type 违规的 triple。OntoCoDec 通过生成时强制合法 type 保留这些 TP——\"prevent vs detect\" 核心论据的具体数据。\n7. **OntoCoDec+post-hoc 组合**（future work idea）：先 constrain 再 filter 残余 DR。低优先级，May 19 前不做。\n\n### C3: \"Bitwise AND of two masks is not novel\"\n**Response**: The novelty is not the AND operation — it's (a) the automatic compilation from ontology definitions (zero-code schema compliance), (b) the stateful entity registry enabling cross-field constraints during autoregressive generation, (c) the decidability taxonomy providing theoretical guidance, and (d) the systematic violation landscape measurement motivating the approach.\n\n### C4: \"Evaluate-for violation rate increases with schema-informed prompt\"\n**Response (prior-constraint conflict framework)**: Evaluate-for has 23/36 valid pairs; Method→Task is invalid for Evaluate-for but natural in the LLM's distributional prior (\"Method X evaluates for Task Y\" is semantically plausible). Schema-informed prompting creates a **prior-constraint conflict**: the model learns to avoid Method→Task for Evaluate-for (reducing count 133→87, -34.6%), but the remaining instances are harder boundary cases where the model's type assignment strategy becomes less stable. This is not just \"harder instances\" — it's an active interference between prompt-level constraint signals and the model's learned type associations.\n\n**This strengthens the paper's claim**: prompt-level intervention is not merely insufficient but potentially **counterproductive** for specific constraint configurations. Decoding-time enforcement avoids this issue entirely — it operates on logits, not on the model's reasoning process, so there is no prior-constraint conflict.\n\n### C5: \"Only tested on one model (Qwen3-8B)\"\n**Response**: Cross-model validation DONE (D016 bootstrap verified). Llama-3.1-8B 零代码修改：\n- SciERC: DR 13.34%→0.08% (↓99.4%), R-F1 -0.14pp (p=0.011, negligible), E-F1 NS\n- DocRED: DR 26.07%→2.55% (↓90.2%), R-F1 +0.29pp (p=0.013, significant), E-F1 -0.64pp (p=0.022, modest decline)\n- Parse failures: unconstrained 68 vs full_s1 91 (6.8% vs 9.1%)\n\n**Cross-model claim 指导（Reviewer 专项评估）**:\n- ✅ 可声明：\"OntoCoDec generalizes across model families without code modification\"（程序性事实，铁证）\n- ❌ 不可声明：\"consistently achieves the same reduction rate\"（仅 2 模型，不足以量化声明）\n- **RV↓DR↑ 正交性 finding**: Llama RV baseline 低(16%) 但 DR baseline 高(26%)，反向于 Qwen。证明两层约束解决正交 failure modes——vocabulary compliance ≠ semantic compliance。应作为 §5 cross-model 独立 finding 展开。\n- **Parse failure 偏差**: checker skip parse failures (不计入 F1)，Llama 68/998=6.8% vs Qwen 12/998=1.2%。偏差方向保守（不利于 constrained），不威胁 claim。但需 footnote 披露 + cross-model 表增加 parse failure rate 行。\n- **Llama SciERC CF=6.56%**: 比 Qwen 同量级更高，non-local constraint 问题在 Llama 上更突出，limitations 提及。\n- 等 llama_docred_full_s1 出来后定最终 claim 措辞。\n\n### C6: \"Constrained decoding degrades generation quality (CRANE, Structure Snowballing)\"\n**Response**: OntoCoDec's semantic constraints are narrower than full grammar constraints — only type tokens are masked, free text is unconstrained. **Bootstrap CI (10000×, D012 Qwen + D016 Llama, all registry-aligned)**:\n\n**Qwen3-8B**: SciERC R-F1 +0.13pp (p=0.58, NS), E-F1 -0.03pp (NS). DocRED R-F1 +0.50pp (p<0.001), E-F1 +1.23pp (p<0.001).\n**Llama-3.1-8B**: SciERC R-F1 -0.14pp (p=0.011, negligible), E-F1 NS. DocRED R-F1 +0.29pp (p=0.013), E-F1 -0.64pp (p=0.022).\n\n**Cross-model pattern**: DocRED R-F1 显著提升（两个模型）。E-F1 model-dependent（Qwen +1.23pp, Llama -0.64pp）。\n- 机制：grammar 消除 OOV relation names + 非标 entity types → all_set 方法下减少 FP → precision 提升。Grammar 是 F1 提升的唯一来源（grammar_only Ent F1=59.38% ≈ full_s1 59.37%, Δ=0.01pp, p=0.66）。Semantic 层对 F1 无额外贡献。\n- Frame as: \"On DocRED, R-F1 gains are significant for both models. Entity F1 impact is model-dependent.\"\n- 不升级为 core claim，但如实报告。\n\n### C7: \"Your method trades DR violations for CF violations (cross-field consistency)\"\n**Response**: Both S1 and S2 show elevated CF (per-triple rate ~8-10%). This is an inherent limitation of per-relation independent type enforcement. Must be proactively reported as a limitation. Defense:\n\n**CF 子类型分析（根因已确认）**：\n- **EVR（entity-vs-relation type drift）**: 占 CF 的 >90%。同一 entity 在 entity list 和 relation triple 中被赋予不同 type。S1: 245 entities (7.34%), S2: 178 entities (5.54%, -27%)\n- **Within-rel（同 entity 跨 relation type 不一致）**: S1: 10 (0.36%), S2: 18 (0.72%)\n- S2 减少 EVR 但增加 within-rel——trade-off 更复杂，不是单纯好/差\n\n**Top 冲突模式**: Generic↔OtherScientificTerm (60次), Material↔OtherScientificTerm (28次), Material↔Method (20次)。**这些是 SciERC type system 固有的语义边界模糊区**——同一术语在不同学术语境下确实可以被合理归类为不同 type。CF 在相当程度上是 type system 模糊性的体现，非纯粹的方法缺陷。\n\n**论证层次**：\n1. DR violations = structurally invalid triples（下游系统不可用）→ hard constraint\n2. CF violations = same entity gets different types across relations → individual triples remain type-valid, only cross-triple consistency broken → soft preference\n3. CF 的根因是 type system 语义边界模糊 + per-relation 独立 enforcement，非 bug\n4. Future work: cross-relation global consistency pass (entity-level type consensus before relation-specific enforcement)\n\n**机制归因（口径对账确认）**：grammar_only CF=0.08%（与 unconstrained 持平），full_s1 CF=9.90%，full_s2 CF=8.03%。**CF 100% 由 semantic 层引入，grammar 层无贡献。** 这为 \"CF 是 semantic type enforcement 的系统性副作用\" 提供干净的消融证据。\n\n**论文数字口径**：CF rate 用 violation_checker 口径（denominator=total_entities，与 DR/RV/ET 一致）。分析段落额外给 entity-level EVR 率 + 受影响样本比例。注意：analyze_cf 脚本的 EVR/WR 两维度不是独立的（WR⊂EVR），论文中不要作为两个独立维度报告。\n\n**Do NOT hide this data.** Proactive disclosure + severity distinction + root cause analysis + type ambiguity evidence + 消融归因 = 最强防御策略。\n\n### C8: \"Absolute F1 is too low (~8%) — results are not meaningful\"\n**Response**: This is a zero-shot extraction setting (no training data, no fine-tuning). Low F1 is expected — supervised SOTA on SciERC relation F1 is ~40-50%. Our contribution is the constraint enforcement method, not extraction quality. F1 is a control variable verifying constraints don't degrade quality, not an optimization target. Recommended framing: \"We evaluate in a zero-shot setting to demonstrate that our constraint enforcement method works without task-specific training. F1 is reported to verify that constraint enforcement does not degrade extraction quality, not as a claim of state-of-the-art performance.\"\n\n## Paper Structure (Draft)\n1. Introduction: Violation landscape motivation + composable constraint framework overview\n2. Background: Grammar-constrained decoding (XGrammar) + IE ontology structure\n3. Violation Landscape Study (Phase 0 empirics — independent contribution)\n4. OntoCoDec Framework: Compiler + TypeConstraintProcessor + S1/S2 strategies\n5. Experiments: Constrained vs unconstrained vs post-hoc vs prompt-based\n6. Related Work: 5 constraint paradigms (grammar, vocabulary, structural, type-checking, ontology)\n7. Conclusion\n\n## Claim Calibration (per Reviewer assessment)\n\n**Safe to claim (sufficient evidence from Phase 2)**:\n- \"First systematic study of ontology constraint violations in LLM-based IE\"\n- \"Violation rate correlates with constraint tightness, not ontology size\" (D014: DR reduction ceiling 由 tightness × model RV baseline 共同决定)\n- \"Grammar+semantic constrained decoding eliminates 94% of DR violations at zero F1 cost\" ✅ Phase 2 confirmed\n- \"Two-layer architecture provides complementary coverage — grammar enables semantic\" ✅ Ablation confirmed\n- \"Prompt-level intervention scales poorly with ontology complexity\" ✅ SciERC ↓62% vs DocRED ↓32%\n\n**Claim with caution**:\n- \"Near-complete type-valid IE\" — S1 0.93%, S2 0.97% residual, not truly 0%. Title updated to \"Near-Complete\"\n- \"Principled framework applicable to arbitrary IE ontologies\" — validated on 2 datasets + 1 model only\n- \"F1 improvement\" — SciERC: not significant (p=0.58), frame as F1-neutral; DocRED: significant (+0.50pp, p<0.001), 可报告但不升级为 core claim，归因于 OOV elimination 而非约束解码本身的提升\n- \"CF reveals type system ambiguity\" — 可在 §5.3 作为 analysis finding 展开（Generic↔OtherScientificTerm 等模式有独立 insight 价值），但 §7 必须同时保留 CF 作为 limitation + future work。**两处都要有，缺一不可。** 不能暗示\"因为是 type ambiguity 所以 CF 可接受\"\n\n**Do NOT claim**:\n- \"General infrastructure for IE\" — only zero-shot extraction validated\n- \"State-of-the-art\" — F1 is control variable, not optimization target (see C8)\n- \"Synergistic effect\" — mechanism is enabling dependency, not mutual amplification (see Claim 3)\n- \"S2 solves CF\" or \"S2 mitigates Structure Snowballing\" — data shows S2 ≈ S1 on all metrics; position as architectural variant only\n- \"Pilot50 DR=0%\" — small-sample artifact, full S2 has DR=0.97%\n- \"Grammar-first invariant\" 作为独立 claim — 证据不足（仅 1 次崩溃触发，实现是 fallback 非形式化保证）。写入 §4 方法论设计原则（1-2 句），不升级为 claim\n- \"Robust dual-layer composition across schema complexities\" — 等 DocRED 完成。最终如 fallback ≤5/998，可写经验性陈述，不做泛化 claim\n\n## Risk Ranking (ordered by reject probability)\n\n1. **CF violation trade-off under-addressed** (MEDIUM-HIGH): S1 9.9%, S2 8.03% — both elevated. **S2 confirmed: does NOT solve CF.** This is the #1 attack surface. Mitigated by proactive disclosure + severity distinction + root cause analysis (C7). Must be reported as explicit limitation with future work direction (global entity-type consensus).\n2. ~~**Single model limitation**~~ (RESOLVED): Llama-3.1-8B SciERC ✅ (DR↓99.4%) + DocRED ✅ (DR↓90.2%). 2 模型 × 2 数据集全矩阵完成。\n3. **Novelty perception** (MEDIUM): \"PLDI'25 for code → OntoCoDec for IE\" attack line. Must argue IE constraint structure differs fundamentally.\n4. ~~**DocRED Phase 2 weak**~~ (RESOLVED → reframed as D014): Qwen DR↓44.7%, Llama DR↓90.2% — both substantial. Weaker Qwen reduction explained by RV baseline interaction (D014), not method failure.\n5. ~~**Phase 2 F1 drop**~~ (RESOLVED): F1 confirmed neutral (SciERC) or positive (DocRED, p<0.001). Bootstrap CI D012 confirms. No longer a risk.\n\n## Critical Path to EMNLP Submission (May 25)\n\n- **May 13-14**: Phase 0 + Phase 1 + Phase 2 SciERC ✅\n- **May 14**: Phase 2 DocRED 4-way ablation ✅ + Llama SciERC cross-model ✅ + Dream 完成 (3/6)\n- **May 14-15**: Llama DocRED 2 组实验 ✅ + Checker 修正 ✅ + post-hoc baseline ✅ + bootstrap CI ✅ + related work ✅\n- **May 14-15**: D014 tightness claim 修订 + §5 cross-model subsection + abstract/conclusion 修正 (Agent 执行中)\n- **May 15-17**: 全文校对 + Discussion 整合 + 最终数字确认\n- **May 19**: 内部稿 → submit_paper_to_review\n- **May 19-24**: Review 修改 + 最终提交\n\n**当前瓶颈**: 无技术 blocker。等 Reviewer 跨文件一致性审查 + 编译验证后即可 submit_paper_to_review。\n\n## Status\n- Phase 0 SciERC: ✅ Complete (minimal + schema-informed)\n- Phase 0 DocRED: ✅ Complete (minimal 18.7% DR + schema-informed 12.8% DR)\n- Phase 1 Compiler: ✅ Complete (grammar + semantic layers integrated)\n- Phase 2 SciERC (5 configs): ✅ Complete (S1 DR↓94% F1-neutral, S2 降级为 ablation)\n- Phase 2 DocRED (4 configs): ✅ Complete (full_s1 DR↓45%, grammar ET/RV→0%)\n- Llama SciERC cross-model: ✅ Complete (DR↓99.4%, F1-neutral, 零代码修改)\n- Llama DocRED cross-model: ✅ Complete (full_s1 DR↓90.2%, unconstrained DR=26.07%)\n- Checker v2 (D011): ✅ Fixed (ET triple-counting → unique entity dedup)\n- Bootstrap CI (D012): ✅ Fixed + confirmed (entity filter bug resolved)\n- Post-hoc baseline (D013): ✅ Complete (multi-dimensional framing)\n- Related work: ✅ 42 bib entries, 4 additions merged\n- Dream 6/6 actions: ✅ All complete\n- CF violation analysis: ✅ Confirmed inherent limitation (S1 9.9% SciERC / 2.57% DocRED / 12.02% Llama DocRED)\n- D014 tightness revision: ✅ Complete (tightness × RV baseline dual-factor)\n- Llama bootstrap CI (D016): ✅ Fixed + verified (registry-aligned ≤0.05pp, all p-values in paper)\n- Paper compilation: ✅ 8 pages正文 + appendix\n\n\n## registry (completed experiments)\n\n- exp_id: mvp_phase0_violation_rate\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_triples: 1724\n    total_entities: 2474\n    json_parse_rate: 1\n    entity_type_violation_rate: 0.004\n    relation_vocabulary_violation_rate: 0.0139\n    domain_range_violation_rate: 0.1537\n    cross_field_consistency_violation_rate: 0.0008\n    go_nogo_metric: 0.1537\n    entity_f1: 0.3101\n    relation_f1: 0.0823\n    per_relation:\n      Used-for:\n        total: 787\n        dr_violations: 6\n        rate: 0.0076\n      Conjunction:\n        total: 32\n        dr_violations: 0\n        rate: 0\n      Hyponym-of:\n        total: 124\n        dr_violations: 18\n        rate: 0.1452\n      Evaluate-for:\n        total: 133\n        dr_violations: 32\n        rate: 0.2406\n      Part-of:\n        total: 72\n        dr_violations: 18\n        rate: 0.25\n      Feature-of:\n        total: 486\n        dr_violations: 163\n        rate: 0.3354\n      Compare:\n        total: 66\n        dr_violations: 28\n        rate: 0.4242\n- exp_id: mvp_phase0_violation_rate_docred\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_docs: 998\n    parsed_docs: 962\n    json_parse_rate: 0.964\n    total_entities: 19099\n    total_triples: 16540\n    entity_type_violation_rate: 0.075\n    relation_vocabulary_violation_rate: 0.289\n    domain_range_violation_rate: 0.187\n    cross_field_consistency_violation_rate: 0.0008\n    go_nogo_metric: 0.187\n    fuzzy_matches: 126\n    top_dr_violations_by_rate:\n      P35_head_of_state: 1\n      P710_participant: 0.919\n      P172_ethnic_group: 0.875\n    top_dr_violations_by_count:\n      P31_instance_of:\n        violations: 322\n        total: 533\n        rate: 0.604\n      P1001_applies_to_jurisdiction:\n        violations: 264\n        total: 594\n        rate: 0.444\n      P1344_participant_in:\n        violations: 194\n        total: 312\n        rate: 0.622\n- exp_id: mvp_phase0_scierc_schema\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    domain_range_violation_rate: 0.0578\n    relation_vocabulary_violation_rate: 0.003\n    entity_type_violation_rate: 0\n    total_violation_rate: 0.0253\n    go_nogo_metric: 0.0578\n    total_triples: 1661\n    vs_minimal_dr_reduction: -0.624\n    per_relation:\n      Used-for:\n        rate: TBD\n      Feature-of:\n        delta_pp: -22.3\n      Part-of:\n        delta_pp: -22.5\n      Compare:\n        delta_pp: -14.8\n      Evaluate-for:\n        delta_pp: 5.8\n    mcnemar_all_significant: true\n- exp_id: mvp_phase0_docred_schema\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_documents: 998\n    documents_checked: 943\n    parse_failures: 55\n    json_parse_rate: 0.9449\n    total_entities: 19524\n    total_triples: 16782\n    entity_type_violations: 119\n    entity_type_violation_rate: 0.0061\n    relation_vocabulary_violations: 3090\n    relation_vocabulary_violation_rate: 0.1841\n    relation_fuzzy_matches: 85\n    domain_range_violations: 2154\n    domain_range_violation_rate: 0.1284\n    cross_field_consistency_violations: 29\n    cross_field_consistency_violation_rate: 0.0015\n    total_violations_any: 5392\n    total_violation_rate: 0.1485\n    go_nogo_metric_dr: 0.1284\n- exp_id: phase2_scierc_grammar_only\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_samples: 551\n    total_triples: 1725\n    total_entities: 2474\n    json_parse_rate: 1\n    entity_type_violation_rate: 0\n    relation_vocabulary_violation_rate: 0\n    domain_range_violation_rate: 0.1484\n    cross_field_consistency_violation_rate: 0.0008\n    entity_f1: 0.3098\n    entity_precision: 0.2598\n    entity_recall: 0.3837\n    relation_f1: 0.0823\n    relation_precision: 0.0643\n    relation_recall: 0.114\n    checker_version: fixed_20260514_v2 (strip + alias + unique_et)\n- exp_id: phase2_scierc_semantic_only\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_samples: 551\n    total_triples: 1726\n    total_entities: 2474\n    json_parse_rate: 1\n    entity_type_violation_rate: 0.004\n    relation_vocabulary_violation_rate: 0.0151\n    domain_range_violation_rate: 0.1165\n    cross_field_consistency_violation_rate: 0.0271\n    entity_f1: 0.3101\n    entity_precision: 0.2605\n    entity_recall: 0.3831\n    relation_f1: 0.0815\n    relation_precision: 0.0637\n    relation_recall: 0.1129\n    checker_version: fixed_20260514_v2 (strip + alias + unique_et)\n- exp_id: phase2_scierc_full_s1\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_samples: 551\n    total_triples: 1729\n    total_entities: 2474\n    json_parse_rate: 1\n    entity_type_violation_rate: 0\n    relation_vocabulary_violation_rate: 0\n    domain_range_violation_rate: 0.0093\n    cross_field_consistency_violation_rate: 0.099\n    entity_f1: 0.3098\n    entity_precision: 0.2598\n    entity_recall: 0.3837\n    relation_f1: 0.0836\n    relation_precision: 0.0654\n    relation_recall: 0.116\n    checker_version: fixed_20260514_v2 (strip + alias + unique_et)\n- exp_id: phase2_scierc_unconstrained\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    json_parse_rate: 1\n    entity_f1: 0.3101\n    entity_precision: 0.2605\n    entity_recall: 0.3831\n    relation_f1: 0.0823\n    relation_precision: 0.0644\n    relation_recall: 0.114\n    entity_type_violation_rate: 0.004\n    relation_vocabulary_violation_rate: 0.0139\n    domain_range_violation_rate: 0.1537\n    cross_field_consistency_violation_rate: 0.0008\n    total_triples: 1724\n    total_entities: 2474\n    total_samples: 551\n    checker_version: fixed_20260514_v2 (strip + alias + unique_et)\n- exp_id: phase2_s2_pilot50\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    domain_range_violation_rate: 0.0205\n    relation_vocabulary_violation_rate: 0\n    relation_f1: 0.1008\n    samples: 50\n    predicted_relations: 146\n    true_positives: 13\n    gold_relations: 112\n    entity_f1_approx: 0.29\n    note: 'DR 修正: 原值 0 来自 dryrun (n=25 triples)。实际 pilot50 DR=3/146=2.05% (来自 violation_report_s2_pilot50.json)。'\n- exp_id: mvp_phase0_docred_schema_r2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: phase2_scierc_full_s2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_samples: 551\n    total_triples: 1644\n    total_entities: 2228\n    json_parse_rate: 1\n    entity_type_violation_rate: 0\n    relation_vocabulary_violation_rate: 0\n    domain_range_violation_rate: 0.0097\n    cross_field_consistency_violation_rate: 0.0803\n    entity_precision: 0.2797\n    entity_recall: 0.3712\n    entity_f1: 0.319\n    relation_precision: 0.064\n    relation_recall: 0.1078\n    relation_f1: 0.0803\n    checker_version: fixed_20260514_v2 (strip + alias + unique_et)\n- exp_id: phase2_docred_grammar_only\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    documents_checked: 985\n    parse_failures: 13\n    total_entities: 20150\n    total_triples: 17341\n    entity_type_violation_rate: 0\n    relation_vocabulary_violation_rate: 0.0003\n    domain_range_violation_rate: 0.2617\n    cross_field_consistency_violation_rate: 0.0007\n    relation_f1: 8.31\n    relation_precision: 7.06\n    relation_recall: 10.12\n    entity_f1: 59.38\n    entity_precision: 58.47\n    entity_recall: 60.32\n    unrecognized_relations: 5\n    f1_method: all_set\n    checker_version: fixed_20260514_v2 (strip + alias + unique_et)\n- exp_id: phase2_docred_full_s1\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    documents_checked: 987\n    parse_failures: 11\n    total_entities: 20187\n    total_triples: 17341\n    entity_type_violation_rate: 0\n    relation_vocabulary_violation_rate: 0.0003\n    domain_range_violation_rate: 0.1021\n    cross_field_consistency_violation_rate: 0.0257\n    entity_f1: 59.37\n    entity_precision: 58.45\n    entity_recall: 59.63\n    relation_f1: 8.23\n    relation_precision: 6.99\n    relation_recall: 10.01\n    unrecognized_relations: 5\n    f1_method: all_set\n    checker_version: fixed_20260514_v2 (strip + alias + unique_et)\n- exp_id: phase2_docred_unconstrained\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    documents_checked: 986\n    parse_failures: 12\n    total_entities: 20171\n    total_triples: 17497\n    entity_type_violation_rate: 0.0248\n    relation_vocabulary_violation_rate: 0.2966\n    domain_range_violation_rate: 0.1846\n    cross_field_consistency_violation_rate: 0.001\n    entity_f1: 58.15\n    entity_precision: 57.26\n    entity_recall: 58.32\n    relation_f1: 7.74\n    relation_precision: 6.55\n    relation_recall: 9.46\n    unrecognized_relations: 5189\n    f1_method: all_set (includes OOV predictions in denominator)\n    checker_version: fixed_20260514_v2 (strip + alias + unique_et)\n    et_v1: 0.0818\n    et_fix_note: v1 triple-counted ET across entity_list + relation head/tail; v2\n      deduplicates by (text, normalized_type)\n- exp_id: phase2_docred_semantic_only\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    documents_checked: 987\n    parse_failures: 11\n    total_entities: 20185\n    total_triples: 17571\n    entity_type_violation_rate: 0.0422\n    relation_vocabulary_violation_rate: 0.2987\n    domain_range_violation_rate: 0.1384\n    cross_field_consistency_violation_rate: 0.0105\n    entity_f1: 57.81\n    entity_precision: 57.27\n    entity_recall: 58.37\n    relation_f1: 7.7\n    relation_precision: 6.54\n    relation_recall: 9.37\n    f1_method: all_set\n    checker_version: fixed_20260514_v2 (strip + alias + unique_et)\n    et_v1: 0.1044\n    et_fix_note: v1 triple-counted ET across entity_list + relation head/tail; v2\n      deduplicates by (text, normalized_type)\n- exp_id: llama_scierc_unconstrained\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    entity_type_violation_rate: 0\n    relation_vocab_violation_rate: 0.0055\n    domain_range_violation_rate: 0.1334\n    cross_field_consistency_violations: 6\n    entity_f1: 0.2356\n    entity_precision: 0.1983\n    entity_recall: 0.2902\n    relation_f1: 0.0268\n    relation_precision: 0.0236\n    relation_recall: 0.031\n    total_entities: 2451\n    total_relations: 1274\n    json_parse_failures: 1\n    samples: 551\n    checker_version: fixed_20260514_v2 (strip + alias + unique_et)\n- exp_id: llama_scierc_full_s1\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    samples: 550\n    entities_extracted: 2469\n    relations_extracted: 1315\n    domain_range_violation_rate: 0.0008\n    relation_vocab_violation_rate: 0\n    entity_type_violation_rate: 0\n    cross_field_consistency_violation_rate: 0.0656\n    total_violation_rate: 0.0431\n    entity_f1: 0.2349\n    entity_precision: 0.1972\n    entity_recall: 0.2902\n    relation_f1: 0.0254\n    relation_precision: 0.0221\n    relation_recall: 0.0298\n    checker_version: fixed_20260514_v2 (strip + alias + unique_et)\n- exp_id: llama_docred_unconstrained\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    checker_version: fixed_20260514_v2\n    f1_method: all_set\n    documents: 998\n    documents_checked: 930\n    parse_failures: 68\n    unique_entities: 11525\n    total_triples: 16437\n    dr_eligible_triples: 13789\n    ET_rate_pct: 0.13\n    RV_rate_pct: 16.03\n    DR_rate_pct: 26.07\n    CF_rate_pct: 0.17\n    entity_precision: 61.22\n    entity_recall: 51.02\n    entity_f1: 55.65\n    relation_precision: 5.22\n    relation_recall: 7\n    relation_f1: 5.98\n    fuzzy_relation_matches: 121\n- exp_id: llama_docred_full_s1\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    checker_version: fixed_20260514_v2 (strip + alias + unique_et)\n    f1_method: all_set\n    violations:\n      ET: 0\n      RV: 0\n      DR: 2.55\n      CF: 12.02\n    f1:\n      entity_f1: 55.01\n      entity_precision: 61.41\n      entity_recall: 49.82\n      relation_f1: 6.27\n      relation_precision: 5.49\n      relation_recall: 7.32\n    counts:\n      documents: 998\n      documents_checked: 907\n      parse_failures: 91\n      unique_entities: 11296\n      triples: 16368\n- exp_id: posthoc_filtering_baseline\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    docred_f1_before: 7.74\n    docred_f1_after: 9.61\n    docred_precision_before: 6.55\n    docred_precision_after: 11.22\n    docred_recall_before: 9.46\n    docred_recall_after: 8.4\n    docred_rejection_rate: 0.481\n    docred_tp_before: 1137\n    docred_tp_after: 1010\n    docred_tp_lost: 127\n    docred_et_residual: 0.0247\n    scierc_f1_before: 8.23\n    scierc_f1_after: 8.63\n    scierc_rejection_rate: 0.168\n    scierc_recall_before: 11.4\n    scierc_recall_after: 10.68\n    scierc_tp_before: 111\n    scierc_tp_after: 104\n- exp_id: llama_docred_unconstrained_mt6144\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ET_rate: 0.13\n    RV_rate: 15.89\n    DR_rate: 26.18\n    DR_rate_eligible: 31.15\n    CF_rate: 0.17\n    entity_precision: 61.19\n    entity_recall: 51.06\n    entity_f1: 55.67\n    relation_precision: 5.18\n    relation_recall: 7\n    relation_f1: 5.95\n    parse_failures: 67\n    documents_checked: 931\n    total_documents: 998\n    unique_entities: 11534\n    total_triples: 16584\n    dr_eligible_triples: 13936\n    fuzzy_relation_matches: 121\n- exp_id: llama_docred_full_s1_mt6144\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    DR_rate_pct: 2.57\n    RV_rate_pct: 0\n    ET_rate_pct: 0\n    CF_rate_pct: 12.13\n    R_F1: 6.25\n    R_precision: 5.45\n    R_recall: 7.32\n    E_F1: 55.04\n    E_precision: 61.41\n    E_recall: 49.87\n    documents_total: 998\n    documents_checked: 908\n    parse_failures: 90\n    triples: 16471\n    unique_entities: 11307\n    fallback_events: 67911\n    wall_clock_seconds: 23926\n    vs_unconstrained_mt6144:\n      DR_delta_pp: -23.61\n      DR_reduction_pct: -90.2\n      R_F1_delta_pp: 0.3\n      E_F1_delta_pp: -0.63\n    vs_full_s1_mt4096:\n      DR_delta_pp: 0.02\n      R_F1_delta_pp: -0.02\n      E_F1_delta_pp: 0.03\n      CF_delta_pp: 0.11\n      parse_fail_delta: -1\n- exp_id: w1_cf_fallback_scierc_pilot\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    ET: 0\n    RV: 0\n    DR: 0.1478\n    CF: 0.0004\n    R_F1: 0.0823\n    R_P: 0.0643\n    R_R: 0.114\n    E_F1: 0.3098\n    E_P: 0.2598\n    E_R: 0.3837\n    entities: 2474\n    relations: 1725\n    samples: 551\n    grammar_first_fallback_rate: 0.3664\n    cf_registry_fallback_rate: 0.0448\n    total_mask_calls: 17024\n    violation_budget_DR_CF: 0.1482\n- exp_id: w1_cf_fallback_docred\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: w1_cf_fallback_llama_scierc\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: w1_cf_fallback_llama_docred\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: w5_lora_scierc_training\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 0.0634\n    eval_loss: 0.0586\n    eval_token_accuracy: 0.9816\n    eval_entropy: 0.9635\n    train_runtime_sec: 688.4\n    epochs: 3\n    checkpoint_path: /root/schema_semantic_constrained_ie/checkpoints/qwen3_8b_lora_scierc\n    merged_model_path: /root/schema_semantic_constrained_ie/checkpoints/qwen3_8b_lora_scierc_merged\n- exp_id: w5_lora_scierc_unconstrained_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    json_parse_rate: 1\n    entity_type_violation_rate: 0\n    relation_vocabulary_violation_rate: 0\n    domain_range_violation_rate: 0.0195\n    cross_field_consistency_violation_rate: 0\n    entity_f1: 0.6705\n    entity_precision: 0.6523\n    entity_recall: 0.6898\n    relation_f1: 0.4386\n    relation_precision: 0.4087\n    relation_recall: 0.4733\n    total_entities: 1784\n    total_relations: 1128\n    domain_range_violations: 22\n    go_nogo_metric: 0.0195\n    dr_gate: FAILED\n- exp_id: w5_lora_scierc_constrained_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    json_parse_rate: 1\n    entity_type_violation_rate: 0\n    relation_vocabulary_violation_rate: 0\n    domain_range_violation_rate: 0\n    cross_field_consistency_violation_rate: 0.0118\n    entity_f1: 0.6705\n    entity_precision: 0.6523\n    entity_recall: 0.6898\n    relation_f1: 0.4377\n    relation_precision: 0.4078\n    relation_recall: 0.4723\n    total_entities: 1784\n    total_relations: 1128\n    total_samples: 551\n    cross_field_consistency_violations: 21\n- exp_id: w5_llama_lora_scierc_training\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    eval_loss: 0.0595\n    eval_mean_token_accuracy: 0.9817\n    eval_entropy: 1.0565\n    train_loss: 0.0501\n    train_runtime_sec: 654.23\n    epochs: 3\n    train_samples_per_second: 8.08\n- exp_id: w5_llama_lora_scierc_unconstrained_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_samples: 551\n    total_entities: 1757\n    total_relations: 1082\n    json_parse_rate: 1\n    entity_type_violation_rate: 0\n    relation_vocabulary_violation_rate: 0\n    domain_range_violation_rate: 0.0111\n    cross_field_consistency_violation_rate: 0\n    total_violation_rate: 0.0042\n    entity_precision: 0.6647\n    entity_recall: 0.691\n    entity_f1: 0.6776\n    relation_precision: 0.432\n    relation_recall: 0.4795\n    relation_f1: 0.4545\n- exp_id: w5_llama_lora_scierc_constrained_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    domain_range_violation_rate: 0.0009\n    relation_vocabulary_violation_rate: 0\n    entity_type_violation_rate: 0\n    cross_field_consistency_violation_rate: 0.0046\n    relation_f1: 0.4547\n    relation_precision: 0.432\n    relation_recall: 0.4795\n    entity_f1: 0.6776\n    entity_precision: 0.6647\n    entity_recall: 0.691\n    total_relations: 1081\n    total_entities: 1757\n    total_samples: 551\n    parse_failures: 0\n- exp_id: w5_qwen_docred_lora_training\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    eval_loss: 0.0614\n    eval_mean_token_accuracy: 0.9804\n    eval_entropy: 0.715\n    train_loss: 0.0682\n    train_runtime_s: 5825.6\n    epochs: 3\n    adapter_path: /root/schema_semantic_constrained_ie/checkpoints/qwen_lora_docred\n    merged_path: /root/autodl-tmp/checkpoints/qwen_lora_docred_merged\n- exp_id: w5_docred_sft_data_gen\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_samples: 3053\n    dev_samples: 998\n    train_entities: 59493\n    train_relations: 38180\n    dev_entities: 19528\n    dev_relations: 12275\n- exp_id: w5_llama_docred_sft_data_gen\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_samples: 3053\n    dev_samples: 998\n    train_size_mb: 19\n    dev_size_mb: 6.1\n- exp_id: w5_llama_docred_lora_training\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 0.0572\n    eval_loss: 0.0624\n    token_acc: 98.06\n- exp_id: w5_llama_docred_lora_unconstrained_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ET_pct: 0\n    RV_pct: 0.15\n    DR_pct: 0.49\n    E_F1: 83.93\n    E_P: 84.93\n    E_R: 82.96\n    R_F1: 43.72\n    R_P: 38.59\n    R_R: 50.41\n    parse_fail_rate: 2.3\n    total_samples: 998\n    total_entities_pred: 19106\n    total_relations_pred: 16171\n- exp_id: w5_llama_docred_lora_constrained_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total: 998\n    parse_failures: 25\n    parse_fail_rate: 2.51\n    entities: 19077\n    relations: 16074\n    entity_f1: 85.23\n    entity_precision: 85.04\n    entity_recall: 85.41\n    relation_f1_all_set: 44.23\n    relation_precision_all_set: 38.82\n    relation_recall_all_set: 51.4\n    et_violations: 0\n    et_violation_rate: 0\n    rv_violations: 0\n    rv_violation_rate: 0\n    dr_violations: 33\n    dr_violation_rate: 0.2\n    cross_field_consistency_violations: 41\n    delta_vs_unconstrained:\n      delta_e_f1: 1.3\n      delta_r_f1: 0.51\n      delta_dr: -0.29\n      delta_rv: -0.15\n      note: Computed as constrained - unconstrained on full-set metrics (not intersection\n        subset). Corrected 2026-05-16 per Reviewer audit.\n- exp_id: w5_qwen_docred_lora_unconstrained_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ET_pct: 0\n    RV_pct: 0.27\n    DR_pct: 0.76\n    CF_pct: 0.12\n    E_F1: 82.15\n    E_P: 85.44\n    E_R: 79.11\n    R_F1: 40.86\n    R_P: 36.41\n    R_R: 46.56\n    parse_fail_rate: 7.11\n    total_samples: 998\n    success_samples: 927\n    fail_samples: 71\n    total_entities_pred: 18091\n    total_relations_pred: 15870\n    ET_pct_excl_fail: 0\n    RV_pct_excl_fail: 0.27\n    DR_pct_excl_fail: 0.76\n    CF_pct_excl_fail: 0.12\n    E_F1_excl_fail: 85.72\n    E_P_excl_fail: 85.44\n    E_R_excl_fail: 86\n    R_F1_excl_fail: 42.2\n    R_P_excl_fail: 36.41\n    R_R_excl_fail: 50.17\n- exp_id: w5_qwen_docred_lora_constrained_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ET_pct: 0\n    RV_pct: 0\n    DR_pct: 0.01\n    CF_pct: 0.41\n    E_F1: 81.43\n    E_P: 85.41\n    E_R: 77.81\n    R_F1: 40.56\n    R_P: 36.35\n    R_R: 45.86\n    parse_fail_rate: 8.52\n    total_samples: 998\n    success_samples: 913\n    fail_samples: 85\n    total_entities_pred: 17799\n    total_relations_pred: 15563\n    E_F1_excl_fail: 85.69\n    R_F1_excl_fail: 42.23\n    delta_vs_unconstrained:\n      delta_DR: -0.75\n      delta_RV: -0.27\n      delta_R_F1: -0.3\n      delta_R_F1_excl_fail: 0.03\n      DR_reduction_pct: 98.7\n      note: 'Constrained - unconstrained. Unconstrained: DR=0.76%, R_F1=40.86, R_F1_excl_fail=42.20'\n- exp_id: w6_mistral_scierc_unconstrained\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    E_P: 0.2402\n    E_R: 0.3156\n    E_F1: 0.2728\n    R_P: 0.0295\n    R_R: 0.0483\n    R_F1: 0.0366\n    ET_pct: 1.5\n    RV_pct: 0\n    DR_pct: 56.94\n    CF_pct: 56.87\n    parse_fail_rate: 0\n    total_samples: 551\n    total_pred_entities: 2202\n    total_pred_relations: 1593\n- exp_id: w6_mistral_scierc_constrained\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    E_P: 0.2437\n    E_R: 0.3144\n    E_F1: 0.2746\n    R_P: 0.0292\n    R_R: 0.0493\n    R_F1: 0.0367\n    ET_pct: 0\n    RV_pct: 0\n    DR_pct: 13.4\n    CF_pct: 1.27\n    CF_count: 21\n    parse_fail_rate: 0\n    total_samples: 551\n    total_pred_entities: 2162\n    total_pred_relations: 1647\n    delta_vs_unconstrained:\n      delta_E_F1: 0.0018\n      delta_R_F1: 0.0001\n      delta_ET: -1.5\n      delta_RV: 0\n      delta_DR: -43.54\n      note: 'Constrained - unconstrained. Baseline: E_F1=0.2728, R_F1=0.0366, DR=56.94%,\n        ET=1.5%, RV=0%'\n- exp_id: w6_mistral_docred_unconstrained\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_samples: 998\n    parse_failures: 7\n    parse_fail_rate: 0.7\n    total_pred_entities: 12580\n    total_pred_relations: 11879\n    ET_pct: 7.58\n    RV_pct: 42.35\n    DR_pct: 57.42\n    CF_pct: 24.78\n    E_P: 0.6221\n    E_R: 0.3975\n    E_F1: 0.4851\n    R_P: 0.0447\n    R_R: 0.0432\n    R_F1: 0.0434\n    f1_method: fuzzy_normalized\n    f1_note: Relation matching uses case-insensitive normalization with token-overlap\n      >80% and edit-distance ≤2 fallback. Strict R_F1=3.50% (delta +0.84pp from 98\n      additional TPs via fuzzy matching of Mistral underscore/abbreviation variants).\n- exp_id: w6_mistral_docred_constrained\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ET_pct: 0\n    RV_pct: 0\n    DR_pct: 33.2\n    CF_pct: 0.19\n    E_P: 65.02\n    E_R: 41.4\n    E_F1: 50.59\n    R_P: 5.67\n    R_R: 5.37\n    R_F1: 5.52\n    parse_fail_rate: 0.8\n    total_samples: 998\n    total_pred_entities: 12535\n    total_pred_relations: 11554\n    delta_vs_unconstrained:\n      ET_pct: -7.58\n      RV_pct: -42.35\n      DR_pct: -24.22\n      CF_pct: -24.59\n      E_F1: 2.08\n      R_F1: 2.02\n- exp_id: w7_qwen_scierc_ft_grammar_only\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ET_pct: 0\n    RV_pct: 0\n    DR_pct: 1.9\n    CF_pct: 0\n    parse_fail_rate: 0\n    total_samples: 551\n    total_entities: 1784\n    total_relations: 1128\n    E_P: 0.6523\n    E_R: 0.6898\n    E_F1: 0.6705\n    R_P: 0.4087\n    R_R: 0.4733\n    R_F1: 0.4386\n    DR_violations: 22\n    tokenizer_warning: false_positive_transformers_4.57.6\n- exp_id: w7_qwen_scierc_ft_semantic_only\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ET_pct: 0\n    RV_pct: 0\n    DR_pct: 0.6\n    CF_count: 15\n    parse_fail_rate: 0\n    total_samples: 551\n    total_entities: 1784\n    total_relations: 1128\n    E_P: 0.6523\n    E_R: 0.6898\n    E_F1: 0.6705\n    R_P: 0.4073\n    R_R: 0.4713\n    R_F1: 0.4369\n    DR_violations: 7\n    delta_vs_grammar_only:\n      DR_delta: -1.3\n      note: semantic_only DR=0.6% vs grammar_only DR=1.9%, semantic layer reduces\n        DR by 68%\n    delta_vs_unconstrained:\n      DR_delta: -1.35\n      note: unconstrained DR=1.95% → semantic_only 0.6%\n- exp_id: w7_llama_scierc_ft_grammar_only\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_samples: 551\n    json_parse_failures: 0\n    total_entities: 1757\n    total_relations: 1082\n    entity_type_violation_rate: 0\n    relation_vocabulary_violation_rate: 0\n    domain_range_violation_rate: 0.0111\n    cross_field_consistency_violation_rate: 0\n    entity_f1:\n      precision: 0.6647\n      recall: 0.691\n      f1: 0.6776\n    relation_f1:\n      precision: 0.432\n      recall: 0.4795\n      f1: 0.4545\n- exp_id: w7_llama_scierc_ft_semantic_only\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ET_pct: 0\n    RV_pct: 0\n    DR_pct: 0.65\n    CF_count: 2\n    E_F1: 67.76\n    E_P: 66.47\n    E_R: 69.1\n    R_F1: 45.47\n    R_P: 43.24\n    R_R: 47.95\n    total_entities: 1757\n    total_relations: 1081\n    json_parse_failures: 0\n- exp_id: w8_ft_posthoc_baseline\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ft_regime:\n      qwen_scierc:\n        R_F1_before: 43.86\n        R_F1_posthoc: 43.94\n        R_F1_constrained: 43.77\n        reject_rate_pct: 1.95\n        TP_lost: 4\n      llama_scierc:\n        R_F1_before: 45.45\n        R_F1_posthoc: 45.23\n        R_F1_constrained: 45.47\n        reject_rate_pct: 1.11\n        TP_lost: 5\n      qwen_docred:\n        R_F1_before: 40.91\n        R_F1_posthoc: 41.11\n        R_F1_constrained: TBD\n        reject_rate_pct: 1.03\n        TP_lost: 1\n      llama_docred:\n        R_F1_before: 43.77\n        R_F1_posthoc: 43.92\n        R_F1_constrained: 44.23\n        reject_rate_pct: 0.64\n        TP_lost: 1\n    zs_regime:\n      mistral_scierc:\n        triples: 1584\n        reject_pct: 20.27\n        R_F1_before: 0.0376\n        R_F1_posthoc: 0.0394\n        R_F1_constrained: 0.0367\n        TP_before: 48\n        TP_after: 44\n        TP_lost: 4\n      qwen_scierc:\n        triples: 1724\n        reject_pct: 16.76\n        R_F1_before: 0.0823\n        R_F1_posthoc: 0.0863\n        R_F1_constrained: 0.0836\n        TP_before: 111\n        TP_after: 104\n        TP_lost: 7\n      llama_scierc:\n        triples: 1274\n        reject_pct: 13.89\n        R_F1_before: 0.0268\n        R_F1_posthoc: 0.0271\n        R_F1_constrained: 0.0254\n        TP_before: 30\n        TP_after: 28\n        TP_lost: 2\n      qwen_docred:\n        triples: 17497\n        reject_pct: 48.12\n        R_F1_before: 0.0774\n        R_F1_posthoc: 0.0961\n        R_F1_constrained: 0.0823\n        TP_before: 1137\n        TP_after: 1010\n        TP_lost: 127\n      llama_docred:\n        triples: 16437\n        reject_pct: 42.18\n        R_F1_before: 0.0598\n        R_F1_posthoc: 0.0744\n        R_F1_constrained: 0.0627\n        TP_before: 850\n        TP_after: 802\n        TP_lost: 48\n      mistral_docred:\n        triples: 11836\n        reject_pct: 73.73\n        R_F1_before: 0.0434\n        R_F1_posthoc: 0.0385\n        R_F1_constrained: 0.0552\n        TP_before: 518\n        TP_after: 292\n        TP_lost: 226\n        removed_RV: 4172\n        removed_ET: 3382\n        removed_DR: 1173\n        note: Only ZS case where posthoc HURTS R_F1 — 73.7% rejection rate loses 43.6%\n          of TPs\n    key_finding: 'ZS: post-hoc R_F1 >= constrained R_F1 in 5/6 groups. Exception:\n      Mistral DocRED where extreme rejection rate (73.7%) causes net F1 loss. Constrained\n      decoding value is in structural guarantee (0% violations) and composability,\n      not F1 preservation.'\n- exp_id: w8_llama_docred_ft_grammar_only\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    E_F1: 84.04\n    R_F1: 43.77\n    entity_precision: 84.99\n    entity_recall: 83.11\n    relation_precision: 38.6\n    relation_recall: 50.53\n    ET_pct: 0\n    RV_pct: 0\n    DR_pct: 0.51\n    CF_pct: 0.12\n    parse_fail_rate: 2.3\n    total_samples: 998\n    total_relations: 16199\n    unique_entities: 13225\n    parse_failures: 23\n- exp_id: w8_qwen_docred_ft_grammar_only\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    E_F1: 82.19\n    E_P: 85.47\n    E_R: 79.16\n    R_F1: 40.85\n    R_P: 36.27\n    R_R: 46.77\n    ET_pct: 0\n    RV_pct: 0\n    DR_pct: 0.61\n    CF_pct: 0.11\n    parse_fail_rate: 7.01\n    total_samples: 998\n    parse_failures: 70\n- exp_id: w8_qwen_docred_ft_semantic_only\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    E_F1: 82.15\n    E_P: 85.58\n    E_R: 78.99\n    R_F1: 40.89\n    R_P: 36.35\n    R_R: 46.73\n    ET_pct: 0\n    RV_pct: 0.23\n    DR_pct: 0.21\n    CF_pct: 0.27\n    parse_fail_rate: 7.52\n    total_samples: 998\n    parse_failures: 75\n    documents_checked: 923\n    total_entities: 18025\n    total_triples: 15909\n    DR_violations: 34\n    RV_violations: 37\n    ET_violations: 0\n    CF_violations: 49\n- exp_id: w8_llama_docred_ft_semantic_only\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    E_F1: 84.02\n    E_P: 85.01\n    E_R: 83.06\n    R_F1: 43.9\n    R_P: 38.89\n    R_R: 50.4\n    ET_pct: 0\n    RV_pct: 0.15\n    DR_pct: 0.3\n    CF_pct: 0.16\n    parse_fail_rate: 2.4\n    total_samples: 998\n    parse_failures: 24\n    documents_checked: 974\n    total_entities: 19099\n    total_relations: 16038\n    DR_violations: 48\n    RV_violations: 24\n    ET_violations: 0\n    CF_violations: 31\n\n# 输出格式（YAML，仅输出一个 ```yaml 块，不要任何额外说明文字）\n\n```yaml\ntiers:\n  best:\n    meaning: \"...\"\n    key_assumptions: [...]\n    number_ranges: {metric_a: [low, high], metric_b: [...]}\n    narrative_direction: \"...\"\n  median:\n    meaning: \"...\"\n    ...\n  worst:\n    meaning: \"...\"\n    ...\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-16T17:32:50.724Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-16T17:32:50.724Z",
  "sessionId": "f750eaf8-1f4f-4233-ab88-16d311b78e03"
}
```

---

## Round 1

9 recorded events

### User

_source line 3 · 2026-05-16T17:32:50.746Z_

你是一位经验丰富的 ML 研究者。基于以下研究信息，为 Dream 模拟定义三档场景。

你需要同时定义 best / median / worst 三档：
1. 每档的核心假设（哪些假设成立/不成立）
2. 每档的关键实验指标预期范围（确保 best ≥ median ≥ worst 一致性）
3. 每档的论文叙事方向——
   - best: 原始 framing 完全成立，claims 无需调整
   - median: 部分假设未完全验证，需要调整 claims 强度或补充实验
   - worst: 核心假设不成立，需要找到新的 angle 来 reframe（但仍冲同一 venue，不降级目标）

三档的具体含义不预设——根据这个研究的 paper_framing、已有数据和方法特性
自行判断。但必须确保三档之间的数字和叙事逻辑一致。

# Project context
project: schema_semantic_constrained_ie
venue: EMNLP 2026
focus: 最终评估：54 实验全部完成，FT ablation 8/8 互补性确认，post-hoc defense 成立，latency ≤5.4%。关注：claim 强度是否匹配证据、limitations 是否充分、novelty 定位 vs SynCode/IterGen/BoostCD 差异化是否清晰。

## paper_framing.md

# OntoCoDec — Paper Framing

## Target Venue
EMNLP 2026 (ARR submission May 25, 2026)

## Title
OntoCoDec: Type-Valid Information Extraction via Compiled Ontology Constraints
(D015: "Near-Complete" dropped — DocRED residual DR=10.21% (Qwen) 不算 near-complete。论文贡献是方法，不是特定消除率。SciERC 0.93% 和 DocRED 2.55% (Llama) 可在正文中描述为 near-complete，但 title 不宜 overclaim。)

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

**当前瓶颈**: 无技术 blocker。等 Reviewer 跨文件一致性审查 + 编译验证后即可 submit_paper_to_review。

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

# 输出格式（YAML，仅输出一个 ```yaml 块，不要任何额外说明文字）

```yaml
tiers:
  best:
    meaning: "..."
    key_assumptions: [...]
    number_ranges: {metric_a: [low, high], metric_b: [...]}
    narrative_direction: "..."
  median:
    meaning: "..."
    ...
  worst:
    meaning: "..."
    ...
```


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "5c44dbb2-cbf2-4add-9ae9-72b0e2c2007b",
  "type": "user",
  "uuid": "d87df962-f4c8-47fc-9c01-a45738762dd4",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6",
  "sessionId": "f750eaf8-1f4f-4233-ab88-16d311b78e03",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-16T17:32:50.744Z_

```json
{
  "parentUuid": "d87df962-f4c8-47fc-9c01-a45738762dd4",
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
  "uuid": "a4b66abc-03bc-4c60-ad9e-57ac21045a3b",
  "timestamp": "2026-05-16T17:32:50.744Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6",
  "sessionId": "f750eaf8-1f4f-4233-ab88-16d311b78e03",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-16T17:32:50.744Z_

```json
{
  "parentUuid": "a4b66abc-03bc-4c60-ad9e-57ac21045a3b",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "41538940-d093-40ba-ba7c-ecb65ebcf505",
  "timestamp": "2026-05-16T17:32:50.744Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6",
  "sessionId": "f750eaf8-1f4f-4233-ab88-16d311b78e03",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。基于以下研究信息，为 Dream 模拟定义三档场景。  你需要同时定义 best / median / worst 三档： 1. 每档的核心假设（哪些假设成立/不成立） 2. 每档的关键实验指标预期范围（确保 best ≥ median ≥ worst 一致性） 3. 每档的论文叙事方向——    - best: 原始 framing 完全成立，claims 无需…",
  "leafUuid": "41538940-d093-40ba-ba7c-ecb65ebcf505",
  "sessionId": "f750eaf8-1f4f-4233-ab88-16d311b78e03"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Define best/median/worst scenarios for OntoCoDec",
  "sessionId": "f750eaf8-1f4f-4233-ab88-16d311b78e03"
}
```

---

### Assistant

_source line 8 · 2026-05-16T17:33:20.102Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to define three tiers (best/median/worst) for a Dream simulation of their OntoCoDec paper targeting EMNLP 2026. I need to analyze all the experimental data, paper framing, and claims to define realistic scenarios.

Let me synthesize the key information:

**Core method**: OntoCoDec - constrained decoding for IE that compiles ontology constraints into grammar + semantic layers.

**Key metrics from experiments**:
- DR reduction: 94% (Qwen SciERC), 90.2% (Llama DocRED), 44.7% (Qwen DocRED)


- F1 shows neutral to positive movement across datasets, with confidence elevation ranging from 8-10% on SciERC and 2.5-12% on DocRED
- Cross-model validation spans Qwen and Llama with Mistral as a third baseline, all 8 ablation components confirmed as complementary
- Latency overhead stays minimal at ≤5.4%

The main vulnerabilities I'm tracking are the confidence-F1 trade-off which could be perceived as medium-high risk, potential novelty concerns relative to existing constrained decoding work like SynCode and IterGen, and the notably weaker DR performance on Qwen DocRED that might limit generalization claims.

Now I'm thinking through the review landscape for EMNLP 2026. With 54 experiments complete, the paper's empirical foundation is solid, but I need to anticipate how reviewers will actually respond. The best scenario has reviewers accepting the framing and viewing the confidence limitation as transparent rather than damaging. More realistically, I'll face pushback on specific claims—whether the novelty holds up against prior work, whether the confidence trade-off is acceptable, or whether the Qwen DocRED weakness undermines the cross-model story. Worst case, reviewers question whether this is just applying existing constrained decoding to information extraction without sufficient conceptual contribution, or dismiss the absolute F1 gains as too marginal to matter. I need to clarify what the user is actually asking for—they want me to simulate review outcomes across different scenarios. Let me think through the key metrics that matter: how reviewers score the novelty, the confidence-recall trade-off, and the empirical results, then map those to overall acceptance likelihood. I should structure this around what assumptions would lead to each outcome tier and what the paper's own metrics would need to look like to convince reviewers.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "41538940-d093-40ba-ba7c-ecb65ebcf505",
  "isSidechain": false,
  "requestId": "req_011Cb6eYMs3sKDyC9nQnMuFa",
  "type": "assistant",
  "uuid": "da6f2e7c-3e61-4404-b539-72a7dca76fea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6",
  "sessionId": "f750eaf8-1f4f-4233-ab88-16d311b78e03",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011H1zQoym7dhQ3CmxmftMh7",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 25718,
      "cache_read_input_tokens": 11841,
      "output_tokens": 3403,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 25718,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 3403,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 25718,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 25718
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

_source line 9 · 2026-05-16T17:34:17.362Z_

```yaml
tiers:
  best:
    meaning: "所有核心 claim 经受住审稿，novelty 被认可为 IE-specific 贡献而非简单迁移，CF 作为诚实 limitation 被接受"
    key_assumptions:
      - "至少 2/3 审稿人认可 violation landscape study 作为独立贡献"
      - "enabling dependency（grammar→semantic）被视为 non-trivial 架构 insight，区别于 SynCode 的单层 CFG"
      - "tightness × RV baseline 双因子分析被认为是 deeper insight，非 post-hoc 解释"
      - "CF 主动披露 + type ambiguity 根因分析 + 消融归因被接受为充分的 limitation 处理"
      - "3 模型 × 2 数据集矩阵 + FT ablation 8/8 被视为充分的 generalization 证据"
      - "zero-shot 设定被理解为方法论选择而非能力不足"
    number_ranges:
      avg_reviewer_score: [3.75, 4.25]
      novelty_score: [3.5, 4.0]
      soundness_score: [4.0, 4.5]
      accept_probability_pct: [55, 75]
      major_revisions_requested: [0, 1]
      reviewer_concern_cf_severity: ["minor", "minor"]
    narrative_direction: >
      原始 framing 完全成立。Title "Type-Valid IE via Compiled Ontology Constraints" 精准定位贡献。
      §3 violation landscape 被引用为 empirical contribution。Claim 3 composable framework 的 enabling dependency
      被视为关键设计 insight。DR↓94% (SciERC) / ↓90.2% (Llama DocRED) at zero/positive F1 cost 是
      干净的主结果。CF 在 limitations 和 analysis 双重出现被审稿人正面评价为"refreshingly honest"。
      FT regime 下 DR 1.95%→0% + F1 neutral 补全了"method scales to supervised setting"的叙事。
      Post-hoc baseline 的多维对比（recall preservation + information coverage + ET residual）
      构成完整的 defense。Rebuttal 只需回应小的澄清问题，不需要额外实验。

  median:
    meaning: "核心方法被认可但 1-2 个维度受到实质性质疑，需要 rebuttal 中调整 claim 强度或补充分析"
    key_assumptions:
      - "1/3 审稿人质疑 novelty：'bitwise AND of two masks + entity registry 是 engineering，非 research contribution'"
      - "CF 9.9% (SciERC) 被至少一位审稿人视为 non-trivial 缺陷而非单纯 limitation"
      - "Qwen DocRED DR↓44.7% 被指出与 SciERC ↓94% 差距过大，tightness × RV 解释被认为是 post-hoc rationalization"
      - "zero-shot F1 ~8% 引发 C8 质疑，但 'control variable not optimization target' 被接受"
      - "跨模型 generalization 被认可但被指出只有 2 个同规模模型（8B），模型多样性不足"
      - "FT ablation 被接受为补充证据但审稿人指出 FT regime 下 baseline violation 已很低（~1-2%），constrained decoding 边际价值有限"
    number_ranges:
      avg_reviewer_score: [3.0, 3.5]
      novelty_score: [2.5, 3.5]
      soundness_score: [3.5, 4.0]
      accept_probability_pct: [25, 50]
      major_revisions_requested: [1, 3]
      reviewer_concern_cf_severity: ["moderate", "major"]
    narrative_direction: >
      需要在 rebuttal 中做 3 个调整：
      (1) Novelty 重新锚定——不再 frame 为"composable constraint framework"（太 generic），
      而是 frame 为"first decidability-aware type enforcement for autoregressive IE"，
      强调 decidability taxonomy (local / prefix-decidable / non-local) 是理论贡献，
      composability 是它的实现结果。与 SynCode 的区别：SynCode 处理 context-free 结构约束，
      OntoCoDec 处理 context-sensitive 类型约束（需要 entity registry 状态），属于不同
      decidability class。
      (2) CF claim 降级——从"CF reveals type system ambiguity"（有 insight 意味）调整为
      纯 limitation 表述："per-relation independent enforcement inherently cannot guarantee
      cross-relation consistency; global entity-type consensus is deferred to future work"。
      去掉 type ambiguity 的正面 framing 以避免"spin"指控。
      (3) DocRED 叙事调整——不再隐含"DR↓94%"为主数字（那是 SciERC），主表同时报告
      SciERC ↓94% 和 DocRED ↓44.7%/↓90.2%（Qwen/Llama），差异本身作为 finding
      （tightness × RV interaction）而非需要辩护的弱点。

  worst:
    meaning: "核心假设受到根本性质疑——novelty 被判定为 incremental，CF trade-off 被视为方法缺陷而非 type system 属性，需要 reframe angle"
    key_assumptions:
      - "2/3 审稿人判定 novelty 不足：'applying grammar-constrained decoding (XGrammar) to IE + adding a type checker is engineering contribution, not EMNLP-level research'"
      - "CF trade-off 被视为 fundamental design flaw：'method introduces more inconsistency than it removes — DR↓ but CF↑ 10×'"
      - "至少一位审稿人认为 violation landscape study 是 trivial observation（'of course LLMs violate schemas'）"
      - "post-hoc baseline 的 F1 优势被反过来论证：'post-hoc is simpler, higher F1, and good enough'"
      - "FT regime 下 constrained decoding 边际价值极小（DR 1.95%→0%, ΔF1≈0）被用来论证 'the problem disappears with fine-tuning, making the method unnecessary'"
      - "Mistral DR=13.4%（constrained 后仍高）被指出方法对某些模型效果有限"
    number_ranges:
      avg_reviewer_score: [2.25, 3.0]
      novelty_score: [2.0, 2.5]
      soundness_score: [3.0, 3.5]
      accept_probability_pct: [5, 20]
      major_revisions_requested: [3, 5]
      reviewer_concern_cf_severity: ["major", "fatal"]
    narrative_direction: >
      原始 framing "type-valid IE via compiled ontology constraints" 无法存活。需要 reframe 但不降级目标（仍冲 EMNLP）。
      三个候选 reframe angle（按可行性排序）：
      (A) "When Does Constrained Decoding Help IE? A Decidability-Aware Analysis"——
      把论文从 method paper 转型为 analysis paper。核心贡献变为 decidability taxonomy +
      violation landscape + 何时 constrained decoding 有效/无效的系统性分析。OntoCoDec 降级为
      analysis 的工具而非贡献本身。CF 从 limitation 变为 key finding（"prefix-decidable
      constraints reduce DR but introduce CF — revealing a fundamental decidability boundary
      for autoregressive IE"）。FT regime 的"边际价值小"也变成 finding 而非弱点。
      这个 angle 的 novelty 在于 systematic analysis，不在于 system。
      (B) "The Residual Violation Problem: Why Fine-Tuning Alone Cannot Guarantee
      Schema Compliance"——锚定 FT regime 的 residual violations（DR 0.49-1.95%），
      论证即使 SFT 后仍有 non-zero violations，constrained decoding 是唯一 guarantee 手段。
      需要补充 FT scaling 实验（更多 epochs / 更多 data）来证明 violations 不 converge to 0。
      (C) 保持 method paper 但大幅收缩 scope——去掉 zero-shot 结果，只报告 FT regime，
      frame 为 "last-mile compliance layer for fine-tuned IE models"。代价：丢失 violation
      landscape study 作为独立贡献，论文 contribution 减少。
      推荐 (A)：evidence 已足够，不需要额外实验，且 analysis paper 在 EMNLP 有清晰的 publication 路径。
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "da6f2e7c-3e61-4404-b539-72a7dca76fea",
  "isSidechain": false,
  "requestId": "req_011Cb6eYMs3sKDyC9nQnMuFa",
  "type": "assistant",
  "uuid": "c8e89c9e-0a6d-4961-9b59-b017ff9b4ec8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6",
  "sessionId": "f750eaf8-1f4f-4233-ab88-16d311b78e03",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011H1zQoym7dhQ3CmxmftMh7",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 25718,
      "cache_read_input_tokens": 11841,
      "output_tokens": 3403,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 25718,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 3403,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 25718,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 25718
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

_source line 10_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。基于以下研究信息，为 Dream 模拟定义三档场景。  你需要同时定义 best / median / worst 三档： 1. 每档的核心假设（哪些假设成立/不成立） 2. 每档的关键实验指标预期范围（确保 best ≥ median ≥ worst 一致性） 3. 每档的论文叙事方向——    - best: 原始 framing 完全成立，claims 无需…",
  "leafUuid": "c8e89c9e-0a6d-4961-9b59-b017ff9b4ec8",
  "sessionId": "f750eaf8-1f4f-4233-ab88-16d311b78e03"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Define best/median/worst scenarios for OntoCoDec",
  "sessionId": "f750eaf8-1f4f-4233-ab88-16d311b78e03"
}
```

---
