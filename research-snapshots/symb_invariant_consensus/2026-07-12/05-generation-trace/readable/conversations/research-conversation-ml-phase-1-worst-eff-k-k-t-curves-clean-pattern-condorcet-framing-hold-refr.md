# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义： 含义：Eff-K 作为预测器失败，K/T curves 无 clean pattern。核心 Condorcet framing 不 hold。需 refr

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-1/f34ece61-443f-4fad-9714-c7dbf3b3b1b5.jsonl`
- **Structured JSON:** [`deea990d77337f9afa0c.json`](../../sessions/de/deea990d77337f9afa0c.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-19T04:06:17.223Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-19T04:06:17.223Z",
  "sessionId": "f34ece61-443f-4fad-9714-c7dbf3b3b1b5",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：\n\n含义：Eff-K 作为预测器失败，K/T curves 无 clean pattern。核心 Condorcet framing 不 hold。需 reframe 为 comprehensive negative-results / diagnostic 贡献，保留 oracle gap 和 C0 diagnostic 作为 anchor。仍冲 Findings。\n核心假设：['exp-051 K sensitivity 无 inverted-U: flat, monotonically negative, 或 random walk (K=12 不是 peak 或与其他 K 无显著差异)', 'T sensitivity 无 clean peak: T=0.3 delta ≥+3pp (与 T=0.7 可比) → narrow window 叙事崩塌', \"exp-055 multi-temp 意外 positive (≥+2pp) → 'diversity alone 不足' claim 被动摇\", 'Eff-K 跨模型方向虽对 (Qwen→0, Mistral→variable) 但 Mistral 内 Eff-K 与 delta 完全无关 + PW-600 反例无法用 dual requirement 解释', '2/3 seeds significant 被 reviewer 视为 cherry-picking 而非 replicable effect']\n关键指标范围：{'mistral_k_peak_delta_pp': [1.0, 5.0], 'mistral_k_k4_delta_pp': [-5.0, 5.0], 'mistral_k_k20_delta_pp': [-5.0, 5.0], 'mistral_k_inverted_u_visual': '无可辨识 pattern，noise ≫ signal', 't03_delta_pp': [2.0, 6.0], 't05_delta_pp': [1.0, 5.0], 'multitemp_delta_pp': [1.0, 4.0], 'effk_sc_joint_prediction_accuracy': '≤6/12 conditions 方向正确', 'estimated_reviewer_avg': [2.5, 3.0]}\n叙事方向：放弃 Condorcet predictive framework 作为核心 claim。Reframe 为: \"Comprehensive Diagnostic Study of Symbolic Consensus Aggregation\"。 新 anchor claims: (1) Oracle gap (+14.22pp, p=2e-7) 证明 MAX-SAT 聚合机制有效但自提取是瓶颈——这是模型无关的 hard result; (2) 9 种修复全部失败的 breadth 本身是贡献——涵盖 prompting/architecture/capability/verification/diversity/filtering 全维度; (3) C0+SC 零成本部署诊断仍然 actionable; (4) Regime characterization (Type A/B/C) 作为 empirical taxonomy。 Condorcet/Eff-K 降为 \"one possible explanatory framework\" 放入 discussion，不作为 claim。 K/T sensitivity 如 noisy 则 frame 为 \"high variance evidence of fragility\" 而非 clean ablation。 title 改为偏 empirical: \"When Do Self-Extracted Symbolic Constraints Help LLM Reasoning? A Diagnostic Study\"。 投稿目标: Findings (≥3.0)。依赖 oracle gap 的硬证据 + remediation breadth + practical diagnostic 三条腿。 风险: reviewer 可能认为没有 clean positive result 的 analysis paper novelty 不足。 对冲: 强调 \"saving the community from pursuing a dead end\" 的 service contribution。\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: symb_invariant_consensus\nfocus: D060 纯 Analysis paper — Dual Bottleneck (Independence + Quality) framing。重点审查：1) Condorcet Eff-K 作为跨模型预测器是否有说服力（seed 内部非单调问题）；2) 9 种修复失败作为 structural bottleneck 证据是否充分；3) K/T sensitivity ablation 的 inverted-U 是否足够 clean；4) Analysis paper 在 EMNLP 2026 的竞争力（≥3.0 Findings 可达性）\n\n## paper_framing.md\n\n# Paper Framing — symb_invariant_consensus\n\n## Target Venue\n- Primary: EMNLP 2026 Main (ARR May 25)\n- Deadline: May 25, 2026 (ARR submission)\n\n## D060 Direction: Pure Analysis Paper — Independence Bottleneck\n\n**D059 method improvement 三路失败后，回归纯 analysis paper。** 但比 D058 的 analysis 更强：\n- **Condorcet independence 框架** 提供理论解释（非纯经验）\n- **9 种修复全部失败**（比原 6 种多 3 种靶向尝试）→ bottleneck 是 fundamental\n- **exp-052 p=0.039** → 2/3 seeds 显著 → 效应 IS real but fragile\n- **K sensitivity 倒 U 型** → clean ablation 贡献\n- **T sensitivity** → +4.90pp 仅在 T=0.7 存在，T=1.0 降到 +0.55pp → 效应极度脆弱\n- 用户指示: 投 May 25 不变，≥3.0 兜底\n\n## Core Claims (5 条) — D060 纯 Analysis Framing\n\n### Analysis Claims (已验证)\n\n1. **Independence Bottleneck**: Self-consistency 隐含 Condorcet Jury Theorem 的独立性假设，但同模型采样的 traces 高度相关。Worker 验证的 κ 值：\n   - Qwen-14B FOLIO: κ=0.744, Eff-K=1.31 (SC=75.49%, Δ=+0.25pp n.s.)\n   - Qwen-14B LogiQA: κ=0.821, Eff-K=1.20 (SC=78.5%, Δ=+0.50pp n.s.)\n   - Mistral-7B FOLIO s42 (exp-033): κ=0.500, Eff-K=1.85 (Δ=+4.90pp p=0.013) ← primary seed\n   - Mistral-7B FOLIO s123: κ=0.412, Eff-K=2.17 (Δ=+3.43pp p=0.039)\n   - Mistral-7B FOLIO s456: κ=0.401, Eff-K=2.22 (Δ=-0.49pp n.s.)\n   - Mistral-7B PW-600 (exp-046): κ=0.210, Eff-K=3.63 (Δ=-2.83pp p=0.010, SC=39%)\n   规律：跨模型对比清晰（Qwen Eff-K≈1.2-1.3 → 0 gain; Mistral Eff-K≈1.85-2.22 → variable gain）。但 Mistral seeds 内部，Eff-K 与 delta 非单调（exp-033 Eff-K 最低 1.85 却 delta 最高 +4.90pp）→ Eff-K 是跨模型必要条件，seed 内 variance 仍主导。exp-046 Eff-K 最高(3.63) 但 SC 太低(39%) 导致 delta 为负 → 需同时满足 sufficient Eff-K AND sufficient SC。\n\n2. **Oracle Gap Localizes Extraction Bottleneck**: Gold FOL + MAX-SAT = +14.22pp (p=2.0e-7)，自提取仅 +4.9pp (best case) = 35% utilization。聚合机制本身有效，瓶颈在自提取质量。Two-layer analysis:\n   - **Constraint taxonomy**: 43% trivially_satisfied（被所有候选答案满足的约束，不排除任何答案）\n   - **Discriminative filtering**: 仅 ~8% 约束在 MAX-SAT scoring 中完全 non-discriminative（移除后 0 gains）\n   - **关键区分**: 43% 和 8% 度量不同。trivially_satisfied 约束在 MAX-SAT 中仍可有不同满足程度（partial vs full），所以不全是 non-discriminative。但即使 constraints 是 discriminative 的，它们的\"区分方向\"与模型自身偏差一致（confirmation bias）。both_wrong 组 score_range=29.4。九种修复全部失败。\n\n3. **Regime-Dependent Capability Trap**: SICA 有效性取决于提取模型的基线准确率，存在双边界：\n   - Type A (SC ≥ ~60%): 确认偏差，constraints 镜像模型自身答案\n   - Type C (SC ≤ ~40%): traces 主要错误，constraints 是噪声 (exp-046: Δ=-2.83pp, p=0.0095)\n   - Goldilocks zone (~50-55% SC): 部分独立性 + 部分正确性 (exp-033: Δ=+4.90pp, p=0.013)\n   - Type B: 领域不可形式化 (LogiQA: contradiction rate 0.8%)\n\n4. **C0+SC Two-Dimensional Diagnostic**: C0 (multi-candidate rate) + SC accuracy 形成零成本部署诊断。C0<5% → degenerate; high C0 + high SC → trap; high C0 + low SC → potential gains。\n\n### Remediation Evidence (D060: 全部失败 — 强化 analysis narrative)\n\n5. **Nine Remediation Attempts All Failed**: 原 6 种 + 3 种靶向修复全部无效，证明 independence bottleneck 是结构性的：\n   - D059 三路 method improvement 全部失败：\n     - Discriminative Filtering: 119/204 处理后 0 gains 1 loss，~92% 约束本身就是 discriminative，过滤是 near-no-op\n     - T=1.0 (exp-054): delta 从 +4.90pp 崩塌到 +0.55pp，温度敏感性极端\n     - Multi-Temp (exp-055): 早期 n=28 delta=0.00pp（待完成，但预期 negative）\n   - 原 6 种：contrastive prompting, cross-model extraction, generational scaling, solver-guided refinement, consistency filtering, cross-trace UNSAT\n   - 9 种修复涵盖 prompting / architecture / capability / verification / diversity / filtering 全维度，全部失败 → trap is fundamental\n\n## Core Insight (D060 Updated — Dual Bottleneck)\n\n**Dual Requirement Framework**: SICA 效应需要同时满足两个条件，缺一不可：\n1. **Sufficient Independence** (Eff-K > threshold): traces 需要提供足够多的独立视角\n2. **Sufficient Quality** (SC > ~50%): traces 需要有足够的正确率，否则约束是噪声\n\nCondorcet Jury Theorem 要求投票者独立且 p>0.5。同模型采样的 reasoning traces 严重违反独立性假设（Fleiss' κ = 0.21–0.82，Eff-K 仅 1.20–3.63），解释了为什么简单增加 K 或添加符号约束不能突破 SC 的天花板。\n\n实验数据完美支持 dual requirement：\n- **Qwen-14B**: Eff-K≈1.2-1.3（独立性不足）→ 0 gain，无论 SC 多高\n- **Mistral-7B FOLIO**: Eff-K≈1.85-2.22（中等独立性）+ SC≈54%（中等质量）→ +4.90pp (2/3 seeds significant)\n- **Mistral-7B PW-600**: Eff-K=3.63（最高独立性）但 SC=39%（质量不足）→ -2.83pp\n- 只有 Goldilocks zone（中等 Eff-K + 中等 SC）出现正向 delta\n\nOracle control (+14.22pp) 证明 MAX-SAT 聚合机制本身有效，但自提取约束仅利用了 35% 的理论上限。Discriminative filtering 实验揭示关键机制：~92% 约束 ARE discriminative，但过滤掉 ~8% non-discriminative 约束后 delta 不变（0 gains）。问题不在约束缺乏判别力，而在于 discriminative constraints 的区分方向与模型偏差一致（confirmation bias）。\n\n**κ-delta 反相关解释**：exp-033 κ=0.500 比 exp-052/053 κ≈0.41 高，但 delta 最大。原因：exp-033 Unknown 比例低（49.9% vs 58.5%），traces 更 decisive（更多 True/False 判断）→ 同时导致更高 κ（更多 agreement）和更好的 constraint quality。κ 不是 SICA 效果的唯一决定因素。\n\n**Remediation insight (D060)**: 9 种修复尝试全部失败，包括直接靶向 independence（multi-temp diversity）和 constraint quality（discriminative filtering）。这证明 bottleneck 不是简单的 diversity 或 quality 问题，而是 same-model self-extraction 的根本性限制。\n\n**Key evidence**:\n- **Condorcet independence quantification (Worker-verified, 公式: Eff-K=K/(1+(K-1)κ))**: exp-033 Mistral-7B s42 κ=0.500 (Eff-K=1.85), Mistral-7B s123 κ=0.412 (Eff-K=2.17), Mistral-7B s456 κ=0.401 (Eff-K=2.22), Mistral-7B PW-600 κ=0.210 (Eff-K=3.63), Qwen-14B FOLIO κ=0.744 (Eff-K=1.31), Qwen-14B LogiQA κ=0.821 (Eff-K=1.20). 跨模型清晰: Qwen Eff-K≈1.2-1.3→0 gain, Mistral Eff-K≈1.85-3.63→variable. Eff-K necessary but not sufficient: exp-046 highest Eff-K(3.63) but negative delta(SC too low); within Mistral seeds Eff-K非单调 with delta.\n- **Oracle control (exp-031)**: Gold FOL + MAX-SAT = 89.71% vs SC 75.49% (+14.22pp, p=2.0e-7). Unknown-type +31.9pp.\n- **Two-layer constraint analysis**: 43% trivially_satisfied (taxonomy: satisfied by ALL answers) vs ~8% non-discriminative (filtering: same MAX-SAT score). Difference: trivially_satisfied constraints can still have different satisfaction DEGREES. Removing the 8% yields 0 gains → problem is not quality but confirmation bias direction.\n- **K sensitivity (inverted U)**: K=4(-1.47pp), K=8(-0.98pp), K=12(+4.90pp p=0.013), K=16(+1.47pp), K=20(pending). Peak at K=12, then decline. Non-monotonic. K=4 SC ≈ K=12 SC but SICA differs by 6.4pp — proves SICA extracts different information than SC.\n- **T sensitivity (extreme fragility)**: T=0.7(+4.90pp p=0.013), T=1.0(+0.49pp p=0.739). 温度从 0.7 提到 1.0 让增益降 90%。T=0.3 (exp-057, pending). SICA 效应极度依赖超参数。\n- **Regime boundary**: Qwen-14B (SC=75.49%) Δ=+0.25pp vs Mistral-7B (SC=54.41%) Δ=+4.90pp p=0.013\n- **Type C failure (exp-046)**: Mistral PW-D5 SC=39.33%, Δ=-2.83pp, p=0.010, κ=0.210, Eff-K=3.63, contradiction rate 5.5%. Highest Eff-K yet worst delta → independence alone insufficient when SC too low.\n- **Seed replication**: 2/3 seeds significant at α=0.05 (exp-033 p=0.013, exp-052 p=0.039), 1/3 null (exp-053). Effect IS real but fragile — motivates deep analysis of WHY.\n- **Nine remediation failures**: contrastive prompting, cross-model, generational scaling, solver-guided, consistency filtering, cross-trace UNSAT, discriminative filtering (0 gains), T=1.0 (delta collapse), multi-temp (pending, early 0.00pp). All failed → trap is fundamental.\n- **Entropy mechanism**: High-entropy problems proportion: Mistral 35.8% vs Qwen 10.3%. Unanimous rate: 18.6% vs 58.8%.\n- **Confirmation bias quantification**: Override precision 70.6% (Mistral) vs 28.6% (Qwen). Constraint agreement >80%: 31.9% vs 62.3%.\n\n## Story Spine (D059 Updated)\n\n- **Problem**: LLMs' reasoning can be improved by sampling multiple chains-of-thought and aggregating via majority voting (self-consistency). Recent work proposes symbolic augmentation: extract formal constraints from traces and use SAT solvers for answer selection. But does symbolic aggregation actually outperform simple voting?\n- **Theoretical lens**: Condorcet Jury Theorem requires voter independence. We quantify trace independence via Fleiss' κ and show Effective-K << nominal K. This explains the fundamental limitation of same-model trace aggregation.\n- **Systematic evaluation**: SICA (MAX-SAT over FOL constraints) across 3 domains × 5 model families. Oracle control separates extraction vs aggregation failure. Discriminative filtering reveals ~92% constraints are discriminative, yet SICA gains are fragile — confirmation bias, not constraint quality, is the bottleneck.\n- **Regime characterization**: Three failure modes (Type A/B/C) + narrow Goldilocks zone. C0+SC as deployment diagnostic.\n- **Remediation failures strengthen thesis**: 9 targeted interventions (prompting, architecture, capability, verification, diversity, filtering) all fail to close the oracle gap, proving the bottleneck is fundamental to same-model self-extraction.\n- **Headline result**: \"Across 5 model families, symbolic consensus aggregation shows a real but fragile effect: significant improvement in 2/3 seeds under specific conditions (Mistral-7B, FOLIO, T=0.7, K=12), but zero or negative gains under any perturbation. Condorcet analysis reveals the root cause: Effective-K = 1.3-1.8 for nominal K=12 due to trace non-independence. Oracle constraints prove the aggregation mechanism works (+14.22pp), but 9 remediation strategies all fail to overcome the self-extraction bottleneck. C0+SC provides a zero-cost deployment diagnostic.\"\n\n## Anticipated Reviewer Concerns & Defensive Experiments\n\n1. **\"Gains not statistically significant\"** → exp-033 p=0.013 (n=204), exp-031 oracle p=2.0e-7. Combined N>1,200.\n2. **\"Only one positive result (exp-033)\"** → Seed replication: 2/3 significant (p=0.013, p=0.039). Effect IS real but fragile — the fragility itself IS the finding (K/T sensitivity, Condorcet independence).\n3. **\"Condorcet framework is trivial\"** → Fleiss' κ quantification is novel in SC/SICA context. Eff-K is actionable: tells practitioners how many truly independent traces they get.\n4. **\"Multi-temp / filtering should work\"** → We tried both. Multi-temp (exp-055): negative. Disc. filtering: 0 gains. T=1.0: delta collapse. These failures STRENGTHEN the structural bottleneck thesis.\n5. **\"Only Qwen models\"** → 5 families: Qwen-14B, Mistral-7B, LLaMA-8B, DeepSeek-R1-7B, QwQ-32B.\n6. **\"Only logic domain\"** → FOLIO + ProofWriter + LogiQA + StrategyQA + ARC-Challenge. Type B (domain formalizability) is itself a finding.\n7. **\"Oracle is unfair comparison\"** → Diagnostic tool, not competing method. Separates extraction from aggregation.\n8. **\"MAX-SAT is over-engineering\"** → exp-013: MaxSAT ≈ count-only. This IS the independence bottleneck evidence.\n9. **\"Self-extraction confound\"** → Oracle control resolves completely.\n10. **\"Published methods achieve gains (DyLoS, Aristotle, FoVer)\"** → Different paradigm (external verifiers/trained extractors). We characterize same-model self-extraction.\n11. **\"C0 is trivially derived\"** → Zero-cost early stopping. Practical value.\n12. **\"Why not just use a reasoning model?\"** → QwQ-32B: C0<5%, SICA≡SC.\n13. **\"Random tiebreak baseline\"** → exp-003: SICA tiebreak 80% vs random 50%.\n14. **\"Method improvement is incremental\"** → Grounded in diagnosis (independence + taxonomy), not ad-hoc.\n15. **\"Weighted SC is simpler\"** → exp-016 planned. Weighted SC doesn't address independence.\n16. **\"Within-model ICL transition contradicts regime theory\"** → exp-050b (SC=57.79%, Δ=-3.52pp): ICL changes trace generation characteristics, not just SC level. Paper must distinguish \"same model, different prompt\" from \"same model, same prompt, different accuracy.\"\n\n## Working Title\n**\"Beyond Self-Consistency: How Trace Independence Limits Symbolic Consensus in LLM Reasoning\"**\n(Alternatives:\n- \"The Independence Bottleneck: Why Self-Extracted Symbolic Constraints Cannot Beat Majority Voting\"\n- \"Symbolic Consensus Under the Condorcet Lens: Independence, Extraction, and the Limits of Self-Aggregation\")\n\nNOTE (Dream D037): Title MUST be scoped to \"self-extracted constraints\" / \"SICA\". Published methods (DyLoS, Aristotle, FoVer) use different approaches.\n\n## Paper Structure (EMNLP 8pp + appendix)\n\n### Main Tables\n- T1: Main Results — models × domains, SC% / SICA% / Δpp / p-value, regime boundary\n- T2: Oracle Control — Gold-FOL+MAX-SAT vs SC vs SICA-self, causal separation\n- T3: Independence Quantification — Fleiss' κ / Eff-K / trace agreement per model\n- T4: Extraction Error Taxonomy — trivially_satisfied / discriminative / both_wrong rates\n- T5: K Sensitivity — K=4/8/12/16/20 with Eff-K and diversity metrics (inverted U curve)\n\n### Main Figures\n- F1: Method Pipeline (SICA + oracle control design)\n- F2: SC Accuracy vs SICA Δ scatter (hero figure, regime boundary)\n- F3: K Sensitivity with diversity metrics (K vs Δ, K vs Eff-K)\n- F4: Extraction error breakdown (stacked bar)\n\n### Appendix\n- K ablation details, temperature sensitivity, per-domain results, overhead analysis\n- Entropy-conditioned analysis (continuous scatter + bin sensitivity)\n- Six remediation strategy details\n- Confirmation bias quantification\n- Seed replication analysis\n- QwQ-32B / DeepSeek-R1 negative control\n\n## Claim Risk Notes (D059)\n- **Seed replication**: 2/3 significant (p=0.013, p=0.039), 1/3 null. Frame as \"real but fragile effect\" — motivates analysis of WHY.\n- **Method claims DEAD (D060)**: All three method improvements failed. Paper is pure analysis. 9 remediation failures are EVIDENCE, not limitation.\n- **Condorcet novelty**: ✅ VERIFIED. arXiv:2409.00094 applies CJT to cross-model LLM ensembles (different angle). No prior work applies Fleiss' κ or Eff-K to within-model SC traces. Our framing is novel.\n- **exp-050b complication**: ICL transition Δ=-3.52pp at SC=57.79% complicates simple \"SC determines SICA.\" Explain via trace generation characteristic change.\n- **Variable naming inconsistency**: 56.4% cross-trace pairs share zero Z3 variables. Key mechanism evidence.\n\n## Required Citations (minimum 30 references)\n\n- **SC & extensions**: Wang et al. 2023 (SC), Chen et al. 2023 (USC), Loo et al. 2025 (SC scaling plateaus), Taubenfeld et al. 2025 (weighted SC), DiVeRSe (Li et al. 2023)\n- **Neuro-symbolic reasoning**: DyLoS (EACL 2026), Aristotle (ACL 2025), FoVer (TACL 2025), LogicAgent (2025), Logic-LM (Pan et al. 2023), LINC (Olausson et al. 2023)\n- **Condorcet/voting theory**: Condorcet 1785, Austen-Smith & Banks 1996, **arXiv:2409.00094 (Examining Independence in Ensemble Sentiment Analysis, Sept 2024)** — closest prior work, applies CJT to cross-model LLM ensembles, finds independence violation. Our novelty: within-model trace independence + Fleiss' κ quantification + Eff-K + connection to symbolic aggregation\n- **Test-time compute**: Snell et al. 2025, DeepSeek-R1, Diversity-Aware Training\n- **Verification & reranking**: ORM (Cobbe et al. 2021), PRM (Lightman et al. 2023), Math-Shepherd\n- **Constraint satisfaction**: SATBench (EMNLP 2025), LLM Meets Constraint Propagation (IJCAI 2025)\n- **Debate & multi-agent**: Liang et al. 2023, Du et al. 2023\n\n## Claim Scoping Rules\n- n=60 conditions: \"suggestive/consistent with\" NOT \"confirming\"\n- n≥200 conditions: can \"confirm\"\n- Combined N>1,300: acceptable if breakdown clearly stated\n- Method claims: must show statistically significant improvement OR clear directional improvement with analysis\n- \"Independence bottleneck\" framing: systematic quantification + theoretical grounding\n\n\n## experiment_plan (with registry status)\n\n- id: exp-001\n  name: sica_expanded_14b\n  claim:\n  - 1\n  - 2\n  description: 'Full-scale evaluation: PW D5 600 + FOLIO 204 = 804 questions, K=12,\n    T=0.7. Maximizes statistical power for C3 significance.'\n  priority: P0\n  gpu_budget_hours: 14\n  deps: []\n  registry_id: sica_expanded_14b\n  status: DONE\n  conclusion: success\n  metrics:\n    sica_accuracy: 0.765\n    sc_accuracy: 0.762\n    sica_sc_gap_pp: 0.3\n    n_problems: 804\n    multi_candidate_rate: 0.3818\n    folio_sica: 0.794\n    folio_sc: 0.794\n    folio_gap_pp: 0\n    folio_n: 204\n    proofwriter_sica: 0.755\n    proofwriter_sc: 0.752\n    proofwriter_gap_pp: 0.3\n    proofwriter_n: 600\n    extraction_rate: 0.89\n    answer_extraction_rate: 1\n    contradiction_rate: 0.022\n    problems_with_contradictions: 331\n    truncated_traces: 0\n    wall_time_min: 826\n- id: exp-002\n  name: sica_k_ablation_14b\n  claim:\n  - 1\n  description: 'K sensitivity (K=6,8,11,12,16,20) on D012''s 60 questions. Includes\n    odd K=11 to test if SICA value persists without exact ties. Key questions: does\n    SICA benefit depend on tiebreaks? What happens at odd K? How does tiebreak frequency\n    change with K?'\n  priority: P0\n  gpu_budget_hours: 6\n  deps: []\n  status: planned\n  note: D024 增加 K=11（odd-K test, Dream 三档一致要求）。如 K=11 gap=0 → 确认 tie-only mechanism；如\n    gap>0 → SICA has value beyond tiebreaking。\n- id: exp-003\n  name: tiebreak_baseline_analysis\n  claim:\n  - 1\n  description: Compare SICA vs SC-random-tiebreak vs SC-deterministic on all available\n    data. CPU-only reanalysis. Quantify how much of SICA's gain survives against fair\n    baselines.\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - sica_d012_14b\n  status: planned\n  note: 'Completed as CPU analysis, no registry entry. Results: SICA tiebreak 80%\n    (4/5) vs random 50% vs alphabetical 60% vs first-seen 40%. Artifact: art_20260516_47de9d'\n- id: exp-004\n  name: sica_7b_scaling\n  claim:\n  - 2\n  - 3\n  description: 'Run SICA with Qwen2.5-7B-Instruct on same 60 questions. Test: does\n    weaker model → higher C0 → larger SICA gain? Validates C0-as-predictor claim.'\n  priority: P1\n  gpu_budget_hours: 2\n  deps:\n  - exp-001\n  status: planned\n- id: exp-005\n  name: qwq_32b_operating_regime\n  claim:\n  - 2\n  description: QwQ-32B negative results formatted for paper's Operating Regime Analysis\n    section. Data exists from MVP phase (AIME, MATH, ProofWriter, FOLIO). No new GPU\n    needed.\n  priority: P1\n  gpu_budget_hours: 0\n  deps: []\n  status: planned\n  note: 'Data from QwQ-32B MVP experiments: sica_aime30_v3 (AIME 22题, 0% multi-candidate),\n    sica_proofwriter30_v2 (PW 16题, 18.75% multi-candidate), sica_folio30 (FOLIO 10题,\n    0% multi-candidate). Combined C0=3.6%, SICA≡SC across all domains.'\n- id: exp-006\n  name: c0_diagnostic_validation\n  claim:\n  - 3\n  description: Plot C0 vs SICA-SC gap across all models and K values. Validate C0\n    as predictor. CPU-only analysis over exp-001/002/004/005 results.\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - exp-001\n  - exp-002\n  - exp-004\n  status: planned\n- id: exp-007\n  name: sica_72b_awq\n  claim:\n  - 2\n  description: 'Qwen2.5-72B-Instruct AWQ 4-bit on 60 questions. Scaling analysis:\n    high-baseline non-reasoning model. Within-Qwen scaling dimension.'\n  priority: P1\n  gpu_budget_hours: 4\n  deps:\n  - exp-001\n  status: planned\n  note: D019 升级 P2→P1. 72B-AWQ 4-bit ~36GB weights + KV cache ≈ 50-60GB, 98GB RTX\n    PRO 6000 单卡可放。\n- id: exp-008\n  name: constraint_quality_case_studies\n  claim:\n  - 1\n  description: Qualitative analysis of extracted constraints on 5-10 representative\n    questions. Are constraints semantically meaningful? Do excluded constraints correspond\n    to reasoning errors?\n  priority: P2\n  gpu_budget_hours: 0\n  deps:\n  - exp-001\n  status: planned\n- id: exp-009\n  name: overhead_analysis\n  claim:\n  - 1\n  description: 'Wall-time breakdown per question: generation, constraint extraction,\n    MaxSAT solving. Address ''is the overhead worth it'' concern.'\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - exp-001\n  status: planned\n  note: D021 升级 P2→P1. Reviewer 指出 EMNLP 审稿人对 practical impact 极敏感。\n- id: exp-010\n  name: sica_mistral_7b\n  claim:\n  - 2\n  - 3\n  description: 'Mistral-7B-Instruct-v0.3 on D012 60 questions (PW+FOLIO). Cross-family\n    validation: does C0 pattern hold outside Qwen? Eliminates ''Qwen-specific artifact''\n    attack.'\n  priority: P0\n  gpu_budget_hours: 1.5\n  deps: []\n  status: DONE\n  note: 'D021 新增. 必做——消除 Claim 2 致命弱点。Escalation: 若 C0>30% 且 gap>0 但 p>0.2，扩展到 200+\n    题（~3h GPU，margin 允许）。'\n  registry_id: exp-010-mistral-v3\n  conclusion: negative\n  metrics:\n    n: 60\n    k: 12\n    sica_accuracy: 0.4833\n    sc_accuracy: 0.4833\n    delta_pp: 0\n    multi_candidate_rate: 0.5\n    extraction_rate: 0.8819\n    answer_extraction_rate: 1\n    contradiction_rate: 0.0562\n    discordant_sica_wins: 2\n    discordant_sc_wins: 2\n    mcnemar_p: 1\n    proofwriter_sica: 0.4\n    proofwriter_sc: 0.4\n    proofwriter_delta_pp: 0\n    folio_sica: 0.5667\n    folio_sc: 0.5667\n    folio_delta_pp: 0\n    truncated_traces: 0\n    model: Mistral-7B-Instruct-v0.3\n    dataset: D012\n- id: exp-011\n  name: sica_llama_8b\n  claim:\n  - 2\n  - 3\n  description: LLaMA-3.1-8B-Instruct on D012 60 questions. Second non-Qwen family.\n    Combined with exp-010 gives 3-family coverage (Qwen/Mistral/LLaMA).\n  priority: P0\n  gpu_budget_hours: 1.5\n  deps: []\n  status: planned\n  note: D021 新增. 必做——3 家族是 EMNLP 最低门槛。需 HF_TOKEN（Meta license）或 ModelScope 镜像。Escalation\n    同 exp-010。\n- id: exp-012\n  name: gsm8k_pilot_14b\n  claim:\n  - 2\n  - 3\n  description: 'Qwen2.5-14B on GSM8K 30-question pilot (K=12). Cross-domain test:\n    is C0 high only in restricted-answer-space domains (NLI 3-class) or also in open-answer\n    math? If C0 low → C0=uncertainty signal (strengthens Claim 3). If C0 high → cross-domain\n    win.'\n  priority: P1\n  gpu_budget_hours: 1\n  deps: []\n  status: planned\n  note: D021 新增. Reviewer 预测 C0<20% (14B too strong on GSM8K). Any result is publishable\n    insight.\n- id: exp-013\n  name: constraint_ablation\n  claim:\n  - 1\n  - 2\n  description: 'CPU-only ablation: SICA-MaxSAT vs SICA-count-only (constraint count\n    per answer, no satisfiability) vs SICA-random-weight. Critical for D025 pivot:\n    if MaxSAT ≈ count-only → aggregation mechanism is vacuous, confirming capability\n    trap.'\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - exp-001\n  status: planned\n  note: 'D025 升级 P1→P0. 现在是 make-or-break: 如果 MaxSAT = count-only → 证明 SAT 解算无贡献（capability\n    trap 的 mechanism evidence）。必须用 exp-002 的 raw_constraints 数据。'\n- id: exp-014\n  name: sica_deepseek_r1_llama_8b\n  claim:\n  - 2\n  description: 'DeepSeek-R1-Distill-LLaMA-8B on D012 60 questions. Second reasoning\n    model data point with LLaMA base architecture: validates C0<5% generalizes beyond\n    QwQ-32B AND eliminates ''still Qwen family'' attack.'\n  priority: P1\n  gpu_budget_hours: 2\n  deps: []\n  status: planned\n  note: D021 新增. Reviewer 建议用 LLaMA 底座版本避免 Qwen 架构归属争议。\n- id: exp-015\n  name: logic_lm_baseline\n  claim:\n  - 1\n  description: Logic-LM × K + majority vote baseline on FOLIO. Run Logic-LM style\n    single-trace FOL verification K times, then majority vote. Isolates whether MAX-SAT\n    multi-trace aggregation adds value beyond FOL extraction itself.\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - exp-001\n  status: planned\n  note: 'D024 新增. Dream 三档一致要求 Logic-LM/LINC 比较。CPU-only: 用 exp-001 已有 traces + FOL\n    constraints 做单 trace verification then vote。'\n- id: exp-016\n  name: weighted_sc_baseline\n  claim:\n  - 1\n  - 3\n  description: 'Weighted SC baseline (Taubenfeld et al. 2024 style): weight votes\n    by trace confidence/length/perplexity. CPU-only reanalysis of exp-001/002 data.\n    Tests if simple weighting achieves same tiebreak quality without MAX-SAT.'\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - exp-001\n  status: planned\n  note: 'D024 新增. Dream 提出 weighted SC 是最直接竞争 baseline。实现方式: (1) uniform weight (=SC),\n    (2) length-weighted, (3) log-prob weighted (如 traces 有 logprobs), (4) constraint-count\n    weighted (no SAT)。'\n- id: exp-017\n  name: sica_strategyqa_14b\n  claim:\n  - 1\n  - 2\n  description: Qwen2.5-14B on StrategyQA 60 questions (K=12). Commonsense reasoning\n    domain — high predicted C0 (35-50%) but implicit reasoning chains → low expected\n    constraint quality. Tests capability trap in best-case-diversity scenario.\n  priority: P0\n  gpu_budget_hours: 1.5\n  deps: []\n  status: planned\n  note: D025 新增. Reviewer 推荐 ROI 最高 benchmark。如 C0>30% 且 SICA≈SC → 直接证明 capability\n    trap（diversity high but quality low → no gain）。\n- id: exp-018\n  name: sica_arc_challenge_14b\n  claim:\n  - 1\n  - 2\n  description: Qwen2.5-14B on ARC-Challenge 60 questions (K=12). Science reasoning,\n    4-choice format. Tests constraint mechanism in multi-choice scenario + different\n    domain.\n  priority: P0\n  gpu_budget_hours: 1.5\n  deps: []\n  status: planned\n  note: D025 新增. 4选1格式测试 constraint mechanism 泛化能力。与 FOLIO (3-class) + GSM8K (open)\n    + StrategyQA (binary) 形成答案格式多样性。\n- id: exp-019\n  name: constraint_quality_correlation\n  claim:\n  - 1\n  - 2\n  description: 'CPU-only analysis: compute constraint precision per domain × model,\n    correlate with C0 and SICA-SC gap. Formalizes the capability trap as inverse C0-quality\n    correlation. Uses data from exp-001/010/011/017/018.'\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - exp-001\n  - exp-017\n  - exp-018\n  status: planned\n  note: 'D025 新增. Hero figure (F2) 的数据来源。Constraint quality = (constraints consistent\n    with ground truth) / (total constraints). 预期: high C0 domains (StrategyQA) have\n    low quality, low C0 domains (math) have high quality but SICA=SC anyway.'\n\n\n## registry (completed experiments)\n\n- exp_id: crd_folio_main\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    divergence_rate: 0.422\n    diagnosis_rate: 0.872\n    error_types: 4\n    directed_advantage_pp: 4.7\n    directed_p_value: 0.63\n    localization_accuracy: 0.946\n    fol_accuracy: 0.789\n    code_accuracy: 0.598\n    oracle_accuracy: 0.878\n    pipeline_accuracy: 0.814\n    baseline_accuracy: 0.74\n    cost_multiplier: 5.76\n    dataset: FOLIO\n    n: 204\n- exp_id: smoke-test-5q\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: sica_smoke_5q\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    sica_accuracy: 0.8\n    sc_accuracy: 0.8\n    extraction_rate: 1\n    problems_with_contradictions: 1\n    total_problems: 5\n    total_time_s: 3505\n    avg_time_per_problem_s: 701\n    per_problem:\n    - id: algebra/2470\n      level: 1\n      sica_correct: true\n      sc_correct: true\n      constraints: 27\n      unique: 9\n      excluded: 0\n    - id: prealgebra/65\n      level: 2\n      sica_correct: true\n      sc_correct: true\n      constraints: 26\n      unique: 2\n      excluded: 0\n    - id: number_theory/847\n      level: 3\n      sica_correct: true\n      sc_correct: true\n      constraints: 21\n      unique: 11\n      excluded: 0\n      note: 14 JSON parse failures, 1693s\n    - id: precalculus/1199\n      level: 4\n      sica_correct: false\n      sc_correct: false\n      constraints: 35\n      unique: 6\n      excluded: 0\n      note: graph-reading problem, model cannot see image\n    - id: algebra/2277\n      level: 5\n      sica_correct: true\n      sc_correct: true\n      constraints: 60\n      unique: 6\n      satisfied: 3\n      excluded: 3\n- exp_id: sica_temp_diversity\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    temperatures_tested:\n    - 0.7\n    - 0.9\n    - 1\n    problems_tested: 3\n    problems_with_divergence: 0\n    finding: QwQ-32B produces zero answer divergence at all temperatures on MATH L4-5.\n      Reasoning model's deterministic chain dominates sampling randomness.\n    max_tokens_issue: 4096 tokens insufficient for some L5 problems (truncation)\n    recommendation: Use AIME 2024 (harder, ~79.5% acc) or non-reasoning model for\n      trace diversity\n- exp_id: mvp_math50_t07\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: sica_aime30_t07\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: sica_aime30_v2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    progress: 4/30\n    sica_accuracy_interim: 3/4 (75%)\n    sc_accuracy_interim: 3/4 (75%)\n    avg_time_per_problem_s: 557\n    p2_z3_error: Z3Exception on z3_maxsat.py:163, 0 constraints extracted\n    p5_vllm_stuck: vLLM timeout since ~22:11, retried multiple rounds\n    issue: vLLM service likely crashed or OOM at Problem 5\n    analysis_contradiction_rate_aime: 50% (2/4)\n    analysis_contradiction_rate_math: 20% (1/5)\n    analysis_unique_constraints_per_problem_aime: 18.7\n    analysis_exclusion_rate: 10.7%\n    analysis_sica_sc_agreement: 9/9 (100%)\n    analysis_signal: weak positive - mechanism works but SC too unanimous to flip\n    analysis_p2_failure: 0 constraints, 0 votes - answer extraction failure\n- exp_id: sica_aime30_v3\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    progress: 22/30\n    sica_accuracy_interim: 16/22 (72.7%)\n    sc_accuracy_interim: 16/22 (72.7%)\n    sica_sc_gap_pp: 0\n    avg_time_per_problem_s: 645.9\n    runtime_h: 5.9\n    remaining_problems: 8\n    vote_diversity_analysis:\n      valid_problems: 16\n      total_problems: 22\n      multi_candidate_rate: 0\n      zero_vote_problems: 6\n      zero_vote_indices:\n      - 1\n      - 7\n      - 8\n      - 10\n      - 13\n      - 14\n      constraints_extracted: 19/22\n      exclusion_rate: 0.387\n      conclusion: All 16 valid problems have exactly 1 candidate answer. SICA≡SC structurally.\n        MaxSAT exclusion operates but cannot change final selection with only 1 candidate.\n    process_status: gone (cron miss 1/5)\n- exp_id: sica_proofwriter30\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    sica_accuracy: 0/30 (0.0%)\n    sc_accuracy: 0/30 (0.0%)\n    sica_sc_gap_pp: 0\n    total_wall_time_s: 238.9\n    total_wall_time_min: 4\n    avg_time_per_problem_s: 8\n    traces_generated: 0\n    constraints_extracted: 0\n    traces_with_constraints: 0\n    unique_constraints: 0\n    maxsat_satisfied: 0\n    maxsat_excluded: 0\n    multi_candidate_rate: N/A (no traces generated)\n    vote_diversity: N/A\n    z3_errors: 0\n    z3_timeouts: 0\n    problems_with_contradiction: 0\n    problems_with_votes: 0\n    failure_mode: ALL_400_BAD_REQUEST\n    failure_count: 30/30\n    root_cause: max_tokens=16384 equals max_model_len=16384, leaving 0 tokens for\n      prompt input. Every API call returns 400.\n- exp_id: sica_folio30\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: sica_proofwriter30_v2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: sica_d016_c0_precheck\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    multi_candidate_rate_combined: 0.46\n    multi_candidate_rate_folio: 0.4\n    multi_candidate_rate_proofwriter: 0.5\n    sc_accuracy_combined: 0.73\n    sc_accuracy_folio: 0.8\n    sc_accuracy_proofwriter: 0.69\n    n_problems: 26\n    n_folio: 10\n    n_proofwriter: 16\n    K: 6\n    T: 0.7\n    total_time_s: 280\n    c0_gate: PASS (46% >= 20%)\n    model: Qwen2.5-14B-Instruct\n    vllm_gpu_mem_gib: 27.6\n    smoke_test: 2 problems end-to-end OK, constraints 21-26 per problem\n- exp_id: sica_d012_14b\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    sica_accuracy: 0.7333\n    sc_accuracy: 0.7\n    sica_sc_gap_pp: 3.3\n    c0_multi_candidate_rate: 0.5333\n    c1_extraction_rate: 1\n    c2_contradiction_problems: 34\n    c3_gap_pp: 3.3\n    bootstrap_p: 0.2261\n    proofwriter_sica: 0.6667\n    proofwriter_sc: 0.6667\n    folio_sica: 0.8\n    folio_sc: 0.7333\n    total_constraints_raw: 5849\n    total_constraints_unique: 1735\n    maxsat_exclusion_rate: 0.0259\n    wall_time_min: 58.3\n    d012_verdict: ALL_PASS\n- exp_id: sica_expanded_14b\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    sica_accuracy: 0.765\n    sc_accuracy: 0.762\n    sica_sc_gap_pp: 0.3\n    n_problems: 804\n    multi_candidate_rate: 0.3818\n    folio_sica: 0.794\n    folio_sc: 0.794\n    folio_gap_pp: 0\n    folio_n: 204\n    proofwriter_sica: 0.755\n    proofwriter_sc: 0.752\n    proofwriter_gap_pp: 0.3\n    proofwriter_n: 600\n    extraction_rate: 0.89\n    answer_extraction_rate: 1\n    contradiction_rate: 0.022\n    problems_with_contradictions: 331\n    truncated_traces: 0\n    wall_time_min: 826\n- exp_id: sica_k_sensitivity_14b\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    K6_sica: 0.733\n    K6_sc: 0.733\n    K6_gap_pp: 0\n    K8_sica: 0.733\n    K8_sc: 0.75\n    K8_gap_pp: -1.7\n    K11_sica: 0.733\n    K11_sc: 0.733\n    K11_gap_pp: 0\n    K12_sica: 0.7\n    K12_sc: 0.75\n    K12_gap_pp: -5\n    K16_sica: 0.717\n    K16_sc: 0.75\n    K16_gap_pp: -3.3\n    K20_sica: 0.7\n    K20_sc: 0.733\n    K20_gap_pp: -3.3\n    all_K_sica_leq_sc: true\n    larger_K_degrades_sica: true\n- exp_id: sica_constraint_ablation_013\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    maxsat_accuracy: 0.7649\n    count_only_accuracy: 0.7662\n    random_weight_accuracy: 0.7587\n    sc_baseline_accuracy: 0.7624\n    n_problems: 804\n    maxsat_correct: 615\n    count_only_correct: 616\n    random_weight_correct: 610\n    sc_correct: 613\n    agreement_maxsat_vs_countonly: 803/804\n    agreement_maxsat_vs_randomwt: 785/804\n    agreement_maxsat_vs_sc: 773/804\n    agreement_countonly_vs_randomwt: 786/804\n    agreement_countonly_vs_sc: 774/804\n    agreement_randomwt_vs_sc: 764/804\n    mcnemar_p_all_gt_0.7: true\n- exp_id: exp-005\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    qwq_aggregate_c0_nominal_pct: 10.3\n    qwq_aggregate_c0_effective_pct: 2.6\n    qwen14b_c0_pct: 46\n    diversity_ratio_effective: 17.7\n    aime_delta_pp: 0\n    proofwriter_delta_pp: -5.9\n    aime_n: 22\n    proofwriter_n: 17\n    temp_diversity_n: 5\n    folio_n: 2\n    total_problems: 46\n    c0_threshold: 20\n    qwq_below_threshold: true\n- exp_id: exp-011-llama8b\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp-016-weighted-sc\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    sica_accuracy: 0.7649\n    sc_uniform_accuracy: 0.7624\n    inv_length_accuracy: 0.7674\n    length_weighted_accuracy: 0.7525\n    constraint_count_accuracy: 0.7525\n    inv_length_vs_sc_p: 0.453\n    length_vs_sc_p: 0.153\n    inv_length_vs_sica_p: 0.864\n    length_vs_sica_p: 0.066\n    n_problems: 804\n    all_nonsignificant: true\n- exp_id: exp-010-mistral\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp-011-llama8b-v2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp-017-strategyqa\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp-018-arc\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp-010-mistral-v2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp-017-strategyqa-v2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp-017-strategyqa-v3\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n: 60\n    k: 12\n    sica_accuracy: 0.5667\n    sc_accuracy: 0.5333\n    delta_pp: 3.33\n    mcnemar_chi2: 0.5\n    mcnemar_p: n.s.\n    bootstrap_ci_95:\n    - 0\n    - 8.33\n    bootstrap_p_delta_le_0: 0.1346\n    multi_candidate_rate: 0.1\n    contradiction_detected: 5\n    extraction_rate_problem: 1\n    extraction_rate_trace: 0.704\n    discordant_sica_wins: 2\n    discordant_sc_wins: 0\n- exp_id: pilot-constraint-filtering\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    n: 43\n    thresholds_tested:\n    - 1\n    - 2\n    - 3\n    - 5\n    - 7\n    best_gap_pp: 2.33\n    best_T: 1\n    sica_T1: 0.7674\n    sc: 0.7442\n    T5_gap: 0\n    T7_gap: 0\n    discriminative_ratio_count: 0.115\n    discriminative_ratio_weight: 0.372\n    effective_flip_rate: 0.174\n    multi_answer_problems: 23\n    unanimous_problems: 20\n    problems_disc_favors_different: 4\n- exp_id: exp-018-arc-v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n: 60\n    k: 12\n    sica_accuracy: 0.95\n    sc_accuracy: 0.9667\n    delta_pp: -1.67\n    multi_candidate_rate: 0.05\n    extraction_rate: 1\n    contradiction_detected: 3\n    discordant_sica_wins: 0\n    discordant_sc_wins: 1\n    dataset: ARC-Challenge\n    model: Qwen2.5-14B-Instruct\n- exp_id: exp-011-llama8b-v3\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n: 60\n    k: 12\n    sica_accuracy: 0.6667\n    sc_accuracy: 0.6\n    delta_pp: 6.67\n    multi_candidate_rate: 0.6167\n    extraction_rate: 0.8556\n    answer_extraction_rate: 0.8958\n    contradiction_rate: 0.0527\n    problems_with_contradictions: 43\n    truncated_traces: 44\n    discordant_sica_wins: 5\n    discordant_sc_wins: 1\n    mcnemar_p: 0.2188\n    proofwriter_sica: 0.6333\n    proofwriter_sc: 0.6\n    proofwriter_delta_pp: 3.33\n    folio_sica: 0.7\n    folio_sc: 0.6\n    folio_delta_pp: 10\n    model: LLaMA-3.1-8B-Instruct\n    dataset: D012\n    wall_time_min: 66.4\n- exp_id: pilot-contrastive-prompt\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp-010-mistral-v3\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    n: 60\n    k: 12\n    sica_accuracy: 0.4833\n    sc_accuracy: 0.4833\n    delta_pp: 0\n    multi_candidate_rate: 0.5\n    extraction_rate: 0.8819\n    answer_extraction_rate: 1\n    contradiction_rate: 0.0562\n    discordant_sica_wins: 2\n    discordant_sc_wins: 2\n    mcnemar_p: 1\n    proofwriter_sica: 0.4\n    proofwriter_sc: 0.4\n    proofwriter_delta_pp: 0\n    folio_sica: 0.5667\n    folio_sc: 0.5667\n    folio_delta_pp: 0\n    truncated_traces: 0\n    model: Mistral-7B-Instruct-v0.3\n    dataset: D012\n- exp_id: exp-019-llama8b-strategyqa-200\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    n: 200\n    k: 12\n    sica_accuracy: 0.74\n    sc_accuracy: 0.72\n    delta_pp: 2\n    multi_candidate_rate: 0.41\n    mcnemar_p: 0.424\n    bootstrap_ci_95:\n    - -1.5\n    - 5.5\n    bootstrap_p_delta_le_0: 0.12\n    discordant_sica_wins: 9\n    discordant_sc_wins: 5\n    discordant_total: 14\n    discordant_rate: 0.07\n    sc_unanimous_rate: 0.545\n    model: LLaMA-3.1-8B-Instruct\n    dataset: StrategyQA\n    wall_time_min: 52\n- exp_id: exp-020-llama8b-folio-204\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    n: 204\n    k: 12\n    sica_accuracy: 0.608\n    sc_accuracy: 0.632\n    delta_pp: -2.45\n    mcnemar_p: 0.2668\n    bootstrap_ci_95:\n    - -5.88\n    - 0.98\n    bootstrap_p_sica_ge_sc: 0.1\n    discordant_sica_wins: 4\n    discordant_sc_wins: 9\n    discordant_total: 13\n    discordant_rate: 0.064\n    multi_candidate_rate: 0.618\n    extraction_rate: 0.942\n    answer_extraction_rate: 0.951\n    contradiction_rate: 0.062\n    both_wrong: 71\n    model: LLaMA-3.1-8B-Instruct\n    dataset: FOLIO-204\n    wall_time_min: 131.7\n- exp_id: exp-009-overhead-analysis\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n: 804\n    mean_total_wall_s: 61.6\n    mean_trace_gen_s: 31.6\n    trace_gen_pct: 51.3\n    mean_extract_s: 29\n    extract_pct: 47\n    mean_dedup_s: 1\n    dedup_pct: 1.6\n    mean_maxsat_s: 0.003\n    maxsat_pct: 0.005\n    sica_overhead_s: 30\n    sica_overhead_pct: 48.7\n    pw_overhead_pct: 51.3\n    folio_overhead_pct: 38.6\n    p50_overhead_pct: 48.9\n    p90_overhead_pct: 57.6\n- exp_id: exp-014-deepseek-r1-7b\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    n: 60\n    k: 12\n    sica_accuracy: 0.6833\n    sc_accuracy: 0.7167\n    delta_pp: -3.33\n    multi_candidate_rate: 0.583\n    extraction_rate: 0.839\n    answer_extraction_rate: 0.939\n    truncated_traces: 72\n    contradiction_rate: 0.037\n    wall_time_min: 100.3\n    mcnemar_p: 0.4795\n    discordant_sica_wins: 0\n    discordant_sc_wins: 2\n    model: DeepSeek-R1-Distill-Qwen-7B\n    dataset: D012\n- exp_id: temperature-ablation-t03\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    n: 60\n    k: 12\n    sica_accuracy: 0.7333\n    sc_accuracy: 0.7333\n    delta_pp: 0\n    multi_candidate_rate: 0.3\n    discordant_total: 0\n    model: Qwen2.5-14B-Instruct\n    dataset: D012\n    temperature: 0.3\n- exp_id: temperature-ablation-t05\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    n: 60\n    k: 12\n    sica_accuracy: 0.7667\n    sc_accuracy: 0.7667\n    delta_pp: 0\n    multi_candidate_rate: 0.383\n    discordant_total: 0\n    model: Qwen2.5-14B-Instruct\n    dataset: D012\n    temperature: 0.5\n- exp_id: temperature-ablation-t10\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    n: 60\n    k: 12\n    sica_accuracy: 0.75\n    sc_accuracy: 0.75\n    delta_pp: 0\n    multi_candidate_rate: 0.433\n    discordant_total: 0\n    model: Qwen2.5-14B-Instruct\n    dataset: D012\n    temperature: 1\n- exp_id: exp-021-oracle-folio\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n: 204\n    k: 12\n    oracle_sica_accuracy: 0.8824\n    sc_accuracy: 0.7941\n    sica_self_accuracy: 0.7941\n    oracle_vs_sc_delta_pp: 8.82\n    oracle_vs_sica_delta_pp: 8.82\n    mcnemar_p_oracle_vs_sc: 6.15e-05\n    z3_gold_agreement: 0.946\n    fol_parse_success: 1\n    model: Qwen2.5-14B-Instruct\n    dataset: FOLIO-204\n    constraint_source: gold FOL annotations\n- exp_id: exp-012-gsm8k-pilot\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    n: 30\n    k: 12\n    sica_accuracy: 0.9667\n    sc_accuracy: 0.9667\n    delta_pp: 0\n    multi_candidate_rate: 0.133\n    extraction_success_rate: 0.147\n    model: Qwen2.5-14B-Instruct\n    dataset: GSM8K\n    temperature: 0.7\n- exp_id: exp-004-qwen7b\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    n: 60\n    k: 12\n    sica_accuracy: 0.6833\n    sc_accuracy: 0.6833\n    delta_pp: 0\n    multi_candidate_rate: 0.433\n    extraction_rate: 0.9417\n    answer_extraction_rate: 1\n    contradiction_rate: 0.0274\n    discordant_sica_wins: 2\n    discordant_sc_wins: 2\n    mcnemar_p: 1\n    wall_time_s: 1838\n    truncated_traces: 0\n    model: Qwen2.5-7B-Instruct\n    dataset: D012\n    temperature: 0.7\n    folio_sica: 0.7667\n    folio_sc: 0.7333\n    folio_n: 30\n    proofwriter_sica: 0.6\n    proofwriter_sc: 0.6333\n    proofwriter_n: 30\n- exp_id: temperature-ablation-t07\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    n: 60\n    k: 12\n    sica_accuracy: 0.7167\n    sc_accuracy: 0.75\n    delta_pp: -3.33\n    multi_candidate_rate: 0.4\n    extraction_rate: 0.9208\n    answer_extraction_rate: 1\n    contradiction_rate: 0.022\n    discordant_sica_wins: 0\n    discordant_sc_wins: 2\n    truncated_traces: 0\n    model: Qwen2.5-14B-Instruct\n    dataset: D012\n    temperature: 0.7\n    proofwriter_sica: 0.6333\n    proofwriter_sc: 0.7\n    proofwriter_n: 30\n    folio_sica: 0.8\n    folio_sc: 0.8\n    folio_n: 30\n    wall_time_s: 3498.3\n- exp_id: exp-022-oracle-proofwriter\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n: 600\n    k: 12\n    oracle_sica_accuracy: 0.8667\n    sc_accuracy: 0.7517\n    sica_self_accuracy: 0.755\n    oracle_vs_sc_delta_pp: 11.5\n    mcnemar_p_oracle_vs_sc: 9.21e-15\n    z3_gold_agreement: 0.9714\n    z3_gold_agree_n: 577\n    z3_gold_total: 594\n    parse_errors: 6\n    parse_error_rate: 0.01\n    solver_errors: 0\n    solver_total: 7128\n    relneg_oracle: 0.7786\n    relneg_sc: 0.6\n    relneg_delta_pp: 17.86\n    relnoneg_oracle: 0.7945\n    relnoneg_sc: 0.6644\n    relnoneg_delta_pp: 13.01\n    attnoneg_oracle: 0.961\n    attnoneg_sc: 0.8701\n    attnoneg_delta_pp: 9.09\n    attneg_oracle: 0.9188\n    attneg_sc: 0.85\n    attneg_delta_pp: 6.87\n    model: Qwen2.5-14B-Instruct\n    dataset: ProofWriter-OWA-D5-600\n    constraint_source: gold DSL (raw_logic_programs)\n- exp_id: exp-023-discriminative-rate\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n_total: 804\n    n_multi_candidate: 307\n    source_disc_rate_weight: 0.392\n    source_disc_rate_weight_ci95:\n    - 0.387\n    - 0.398\n    source_disc_rate_count_est: 0.121\n    source_disc_rate_count_ci95:\n    - 0.12\n    - 0.123\n    z3_semantic_disc_rate: 0.082\n    z3_semantic_disc_ci95:\n    - 0.076\n    - 0.088\n    problems_with_disc: 289\n    problems_with_disc_rate: 0.941\n    pw_source_disc_weight: 0.364\n    folio_source_disc_weight: 0.54\n    pw_n_multi: 235\n    folio_n_multi: 72\n    pilot_rate_reported_count: 0.115\n    pilot_rate_reported_weight: 0.372\n    pilot_validation_weight: 0.376\n    pilot_delta_pp: 0.38\n    z3_answer_assertions: 642\n    z3_total_unique_constraints: 7844\n    model: Qwen2.5-14B-Instruct\n    dataset: FOLIO+ProofWriter-804\n- exp_id: exp-026-folio204-trace-regen\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n: 204\n    k: 12\n    sica_accuracy: 0.7451\n    sc_accuracy: 0.75\n    delta_pp: -0.49\n    extraction_rate: 0.9853\n    model: Qwen2.5-14B-Instruct\n    dataset: FOLIO-204\n    temperature_trace: 0.7\n    temperature_extraction: 0.3\n    wall_time_h: 2.5\n- exp_id: exp-027-qwen3-14b-non-thinking\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n: 204\n    k: 12\n    sica_accuracy: 0.8431\n    sc_accuracy: 0.8382\n    delta_pp: 0.49\n    extraction_rate: 0.995\n    contradiction_rate: 0.0283\n    problems_with_contradictions: 69\n    total_constraints: 16153\n    unique_constraints: 7031\n    wall_time_s: 11017\n    model: Qwen3-14B\n    dataset: FOLIO-204\n    mode: non-thinking\n- exp_id: exp-028-qwen3-14b-thinking\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: exp-029-contrastive-folio204\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    contrastive_accuracy: 0.7253\n    sc_accuracy: 0.7363\n    delta_pp: -1.1\n    discriminative_rate: 0.0604\n    discriminative_count: 11\n    n: 182\n    recovery_rate_pct: -8.3\n    mcnemar_chi2: 0.1\n    mcnemar_p: 0.7518\n    cont_only_correct: 4\n    sc_only_correct: 6\n    both_correct: 128\n    both_wrong: 44\n    supporting_pct: 43.2\n    opposing_pct: 56.8\n    avg_constraints_per_problem: 24.4\n    avg_unique_per_problem: 10.4\n    wall_time_min: 47.2\n- exp_id: exp-030-crossmodel-mistral-folio204\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    n: 204\n    k: 12\n    crossmodel_sica_accuracy: 0.75\n    sc_accuracy: 0.75\n    delta_pp: 0\n    discriminative_rate: 0\n    recovery_rate: 0\n    model_extraction: Mistral-7B-Instruct-v0.3\n    model_traces: Qwen2.5-14B-Instruct\n    dataset: FOLIO-204\n- exp_id: exp-031-oracle-folio-regen\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n: 204\n    k: 12\n    oracle_sica_accuracy: 0.8971\n    sc_accuracy: 0.7549\n    sica_self_accuracy: 0.7451\n    oracle_vs_sc_delta_pp: 14.22\n    oracle_vs_sica_delta_pp: 15.2\n    mcnemar_p_oracle_vs_sc: 2.0024e-07\n    mcnemar_b_c:\n      b_oracle_right_sc_wrong: 29\n      c_oracle_wrong_sc_right: 0\n    z3_gold_agreement: 0.951\n    z3_gold_agree_n: 194\n    z3_in_candidates_n: 178\n    fol_parse_success: 1\n    model: Qwen2.5-14B-Instruct\n    dataset: FOLIO-204\n    constraint_source: gold FOL annotations\n    traces_source: exp-026-folio204-trace-regen\n- exp_id: exp-033-qwen3-pw600-nonthinking\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp-035\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    n_problems: 203\n    sc_accuracy: 77.34\n    sica_accuracy: 76.85\n    delta_pp: -0.49\n    sica_correct: 156\n    sc_correct: 157\n    mcnemar_discordant_b: 1\n    mcnemar_discordant_c: 2\n    mcnemar_p_value: 1\n    c0_non_unanimous_rate: 0.5517\n    extraction_rate: 98.19\n    contradiction_rate: 1.58\n    problems_with_contradictions: 60\n    total_constraints: 12950\n    unique_constraints: 6515\n    dedup_ratio: 50.3\n    wall_time_min: 78.2\n    avg_per_problem_s: 23.1\n- exp_id: exp-034\n  name: ''\n  status: DEPLOYED\n  conclusion: failed\n  metrics:\n    n_problems: 93\n    n_target: 600\n    completion_pct: 15.5\n    sica_accuracy: 77.42\n    sc_accuracy: 74.19\n    delta_pp: 3.23\n    sica_correct: 72\n    sc_correct: 69\n    mcnemar_discordant_b: 6\n    mcnemar_discordant_c: 3\n    mcnemar_p_value: 0.5078\n    c0_non_unanimous_rate: 0.581\n    avg_majority_frac: 0.8324\n    extraction_rate: 99.19\n    contradiction_rate: 11.83\n    problems_with_contradictions: 11\n    avg_unique_constraints: 35.6\n    total_constraints: 14437\n    unique_constraints: 3308\n    dedup_ratio: 22.9\n    k: 12\n    level: OWA-D5\n    gt_distribution:\n      'True': 32\n      'False': 28\n      Unknown: 33\n    wall_time_s: 6086.4\n    status_note: 'INCOMPLETE: crashed at 93/600 (python not found after conda env\n      lost)'\n- exp_id: exp-007-qwen72b-awq\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp-004-qwen7b-rerun\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp-036-z3-feedback-folio204\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    z3fb_sica_accuracy: 0.775\n    vanilla_sica_accuracy: 0.745\n    sc_accuracy: 0.75\n    z3fb_vs_vanilla_delta: 0.03\n    unsat_traces: 22\n    total_traces: 2448\n    unsat_rate: 0.009\n    unsat_resolve_rate: 0.864\n    problems_flipped: 0\n    real_impact: 0\n- exp_id: exp-033\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n_problems: 204\n    sica_accuracy: 59.31\n    sc_accuracy: 54.41\n    delta_pp: 4.9\n    sica_correct: 121\n    sc_correct: 111\n    mcnemar_discordant_b: 12\n    mcnemar_discordant_c: 2\n    mcnemar_p_value: 0.0129\n    c0_non_unanimous_rate: 0.8137\n    avg_majority_frac: 0.7515\n    extraction_rate: 97.14\n    contradiction_rate: 3.5\n    problems_with_contradictions: 128\n    avg_unique_constraints: 39.3\n    maxsat_mean_sat_ratio: 0.9609\n    total_constraints: 14042\n    unique_constraints: 8021\n    wall_time_min: 81.4\n    k: 12\n- exp_id: exp-039-14b-pw600-16639\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp-040-qwen3-pw600-16639\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp-041-14b-folio204-16639\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    n: 204\n    dataset: FOLIO-204\n    model: Qwen2.5-14B-Instruct\n    k: 12\n    sica_accuracy: 75.49\n    sc_accuracy: 77.45\n    delta_pp: -1.96\n    sica_correct: 154\n    sc_correct: 158\n    mcnemar_discordant_b: 0\n    mcnemar_discordant_c: 4\n    mcnemar_p_value: 0.125\n    extraction_rate: 0.98\n    contradiction_rate: 0.0097\n- exp_id: exp-038-14b-logiqa200-16639\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    n: 200\n    dataset: LogiQA-200\n    model: Qwen2.5-14B-Instruct\n    k: 12\n    sica_accuracy: 78\n    sc_accuracy: 78.5\n    delta_pp: -0.5\n    mcnemar_p: 1\n    sica_correct: 156\n    sc_correct: 157\n    discordant_b: 1\n    discordant_c: 2\n    both_correct: 155\n    both_wrong: 42\n    extraction_rate: 0.864\n    fail_empty_rate: 0.122\n    avg_unique_constraints: 26.7\n    contradiction_rate: 0.008\n    wall_time_min: 126.8\n- exp_id: exp-042-premise-formalization\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp-043-consistency-filtering\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    sc_accuracy: 0.75\n    sica_t1_all: 0.7794\n    sica_t4: 0.75\n    sica_t6: 0.7549\n    sica_t8: 0.7549\n    avg_unique_constraints: 13.2\n    avg_filtered_t4: 1.8\n    avg_filtered_t6: 0.8\n    avg_filtered_t8: 0.3\n- exp_id: exp-044-icl-oracle\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp-045-backward-verification\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics: {}\n- exp_id: exp-036b-cross-trace-unsat\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    cross_unsat_rate_pair: 0.087\n    cross_unsat_rate_problem: 0.107\n    within_trace_unsat_rate: 0.009\n    unsat_pairs: 11\n    total_pairs: 126\n    problems_with_unsat: 9\n    multi_answer_problems: 84\n    single_answer_skip: 120\n    zero_shared_var_pairs_pct: 0.564\n    avg_shared_vars: 2.7\n    false_true_unsat_rate: 0.467\n    sica_cross_ut_accuracy: 0.745\n    sc_accuracy: 0.75\n    accuracy_impact: 0\n- exp_id: exp-042b-premise-formal\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp-044b-icl-oracle\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    n: 199\n    dataset: FOLIO-199\n    model: Qwen2.5-14B-Instruct\n    k: 12\n    sica_accuracy: 74.87\n    sc_accuracy: 74.37\n    delta_pp: 0.5\n    sica_correct: 149\n    sc_correct: 148\n    icl_examples: 5\n    extraction_failure_rate: 0.008\n- exp_id: exp-045b-backward-verify\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: exp-046-mistral-pw600\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    n: 600\n    sc_accuracy: 39.33\n    sica_accuracy: 36.5\n    delta_pp: -2.83\n    sc_wins: 30\n    sica_wins: 13\n    mcnemar_p: 0.0095\n    significant: true\n    dataset: ProofWriter-D5-600\n    model: Mistral-7B-Instruct-v0.3\n- exp_id: exp-028b-qwen3-thinking-folio204\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: exp-048-llama8b-pw600\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp-049-mistral-logiqa200\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp-050-mistral-icl-oracle-folio199\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp-050b-mistral-icl-oracle\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    n: 199\n    sc_accuracy: 57.79\n    sica_accuracy: 54.27\n    delta_pp: -3.52\n    sc_correct: 115\n    sica_correct: 108\n    discordant_b: 6\n    discordant_c: 13\n    mcnemar_p: 0.167\n    significant: false\n    wall_time_min: 93.8\n    extraction_success: 2333\n    extraction_fail: 55\n    per_answer:\n      'True':\n        n: 70\n        sica_acc: 50\n        sc_acc: 54.29\n      'False':\n        n: 61\n        sica_acc: 36.07\n        sc_acc: 44.26\n      Unknown:\n        n: 68\n        sica_acc: 75\n        sc_acc: 73.53\n- exp_id: exp-049b-mistral-logiqa200\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    n: 200\n    sc_accuracy: 51\n    sica_accuracy: 51.5\n    delta_pp: 0.5\n    sc_correct: 102\n    sica_correct: 103\n    discordant_b: 6\n    discordant_c: 5\n    mcnemar_p: 1\n    significant: false\n    wall_time_min: 78.6\n    extraction_rate: 0.9725\n    total_constraints: 10659\n    unique_constraints: 8934\n    contradiction_rate: 0.0196\n- exp_id: exp-051-mistral-k-sensitivity\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp-052-mistral-folio204-seed123\n  name: ''\n  status: QUEUED\n  conclusion: ''\n  metrics: {}\n- exp_id: exp-053-mistral-folio204-seed456\n  name: ''\n  status: QUEUED\n  conclusion: ''\n  metrics: {}\n- exp_id: exp-052\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n: 204\n    sc_accuracy: 53.9\n    sica_accuracy: 57.4\n    sc_correct: 110\n    sica_correct: 117\n    delta_pp: 3.43\n    discordant_b: 8\n    discordant_c: 1\n    extraction_rate: 0.971\n    contradiction_rate: 0.034\n    wall_time_min: 81.9\n    mcnemar_p: 0.0391\n    significant: true\n- exp_id: exp-053\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    n: 204\n    sc_accuracy: 56.37\n    sica_accuracy: 55.88\n    sc_correct: 115\n    sica_correct: 114\n    delta_pp: -0.49\n    discordant_b: 2\n    discordant_c: 3\n    extraction_rate: 0.97\n    contradiction_rate: 0.033\n    wall_time_min: 80.8\n    mcnemar_p: 1.0\n    significant: false\n- exp_id: exp-054-mistral-folio204-t10\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    n: 204\n    sc_accuracy: 54.9\n    sica_accuracy: 55.4\n    delta_pp: 0.49\n    discordant_b: 5\n    discordant_c: 4\n    mcnemar_chi2: 0.1111\n    mcnemar_p: 0.7389\n    extraction_rate: 97.3\n    contradiction_rate: 3\n    wall_time_min: 83\n- exp_id: exp-055-multitemp-mistral-folio\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp-057-mistral-folio204-t03\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp-058-mistral-folio204-t05\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: worst\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-19T04:06:17.226Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-19T04:06:17.226Z",
  "sessionId": "f34ece61-443f-4fad-9714-c7dbf3b3b1b5"
}
```

---

## Round 1

11 recorded events

### User

_source line 3 · 2026-05-19T04:06:17.244Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：

含义：Eff-K 作为预测器失败，K/T curves 无 clean pattern。核心 Condorcet framing 不 hold。需 reframe 为 comprehensive negative-results / diagnostic 贡献，保留 oracle gap 和 C0 diagnostic 作为 anchor。仍冲 Findings。
核心假设：['exp-051 K sensitivity 无 inverted-U: flat, monotonically negative, 或 random walk (K=12 不是 peak 或与其他 K 无显著差异)', 'T sensitivity 无 clean peak: T=0.3 delta ≥+3pp (与 T=0.7 可比) → narrow window 叙事崩塌', "exp-055 multi-temp 意外 positive (≥+2pp) → 'diversity alone 不足' claim 被动摇", 'Eff-K 跨模型方向虽对 (Qwen→0, Mistral→variable) 但 Mistral 内 Eff-K 与 delta 完全无关 + PW-600 反例无法用 dual requirement 解释', '2/3 seeds significant 被 reviewer 视为 cherry-picking 而非 replicable effect']
关键指标范围：{'mistral_k_peak_delta_pp': [1.0, 5.0], 'mistral_k_k4_delta_pp': [-5.0, 5.0], 'mistral_k_k20_delta_pp': [-5.0, 5.0], 'mistral_k_inverted_u_visual': '无可辨识 pattern，noise ≫ signal', 't03_delta_pp': [2.0, 6.0], 't05_delta_pp': [1.0, 5.0], 'multitemp_delta_pp': [1.0, 4.0], 'effk_sc_joint_prediction_accuracy': '≤6/12 conditions 方向正确', 'estimated_reviewer_avg': [2.5, 3.0]}
叙事方向：放弃 Condorcet predictive framework 作为核心 claim。Reframe 为: "Comprehensive Diagnostic Study of Symbolic Consensus Aggregation"。 新 anchor claims: (1) Oracle gap (+14.22pp, p=2e-7) 证明 MAX-SAT 聚合机制有效但自提取是瓶颈——这是模型无关的 hard result; (2) 9 种修复全部失败的 breadth 本身是贡献——涵盖 prompting/architecture/capability/verification/diversity/filtering 全维度; (3) C0+SC 零成本部署诊断仍然 actionable; (4) Regime characterization (Type A/B/C) 作为 empirical taxonomy。 Condorcet/Eff-K 降为 "one possible explanatory framework" 放入 discussion，不作为 claim。 K/T sensitivity 如 noisy 则 frame 为 "high variance evidence of fragility" 而非 clean ablation。 title 改为偏 empirical: "When Do Self-Extracted Symbolic Constraints Help LLM Reasoning? A Diagnostic Study"。 投稿目标: Findings (≥3.0)。依赖 oracle gap 的硬证据 + remediation breadth + practical diagnostic 三条腿。 风险: reviewer 可能认为没有 clean positive result 的 analysis paper novelty 不足。 对冲: 强调 "saving the community from pursuing a dead end" 的 service contribution。

基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。
每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。

# Project context
project: symb_invariant_consensus
focus: D060 纯 Analysis paper — Dual Bottleneck (Independence + Quality) framing。重点审查：1) Condorcet Eff-K 作为跨模型预测器是否有说服力（seed 内部非单调问题）；2) 9 种修复失败作为 structural bottleneck 证据是否充分；3) K/T sensitivity ablation 的 inverted-U 是否足够 clean；4) Analysis paper 在 EMNLP 2026 的竞争力（≥3.0 Findings 可达性）

## paper_framing.md

# Paper Framing — symb_invariant_consensus

## Target Venue
- Primary: EMNLP 2026 Main (ARR May 25)
- Deadline: May 25, 2026 (ARR submission)

## D060 Direction: Pure Analysis Paper — Independence Bottleneck

**D059 method improvement 三路失败后，回归纯 analysis paper。** 但比 D058 的 analysis 更强：
- **Condorcet independence 框架** 提供理论解释（非纯经验）
- **9 种修复全部失败**（比原 6 种多 3 种靶向尝试）→ bottleneck 是 fundamental
- **exp-052 p=0.039** → 2/3 seeds 显著 → 效应 IS real but fragile
- **K sensitivity 倒 U 型** → clean ablation 贡献
- **T sensitivity** → +4.90pp 仅在 T=0.7 存在，T=1.0 降到 +0.55pp → 效应极度脆弱
- 用户指示: 投 May 25 不变，≥3.0 兜底

## Core Claims (5 条) — D060 纯 Analysis Framing

### Analysis Claims (已验证)

1. **Independence Bottleneck**: Self-consistency 隐含 Condorcet Jury Theorem 的独立性假设，但同模型采样的 traces 高度相关。Worker 验证的 κ 值：
   - Qwen-14B FOLIO: κ=0.744, Eff-K=1.31 (SC=75.49%, Δ=+0.25pp n.s.)
   - Qwen-14B LogiQA: κ=0.821, Eff-K=1.20 (SC=78.5%, Δ=+0.50pp n.s.)
   - Mistral-7B FOLIO s42 (exp-033): κ=0.500, Eff-K=1.85 (Δ=+4.90pp p=0.013) ← primary seed
   - Mistral-7B FOLIO s123: κ=0.412, Eff-K=2.17 (Δ=+3.43pp p=0.039)
   - Mistral-7B FOLIO s456: κ=0.401, Eff-K=2.22 (Δ=-0.49pp n.s.)
   - Mistral-7B PW-600 (exp-046): κ=0.210, Eff-K=3.63 (Δ=-2.83pp p=0.010, SC=39%)
   规律：跨模型对比清晰（Qwen Eff-K≈1.2-1.3 → 0 gain; Mistral Eff-K≈1.85-2.22 → variable gain）。但 Mistral seeds 内部，Eff-K 与 delta 非单调（exp-033 Eff-K 最低 1.85 却 delta 最高 +4.90pp）→ Eff-K 是跨模型必要条件，seed 内 variance 仍主导。exp-046 Eff-K 最高(3.63) 但 SC 太低(39%) 导致 delta 为负 → 需同时满足 sufficient Eff-K AND sufficient SC。

2. **Oracle Gap Localizes Extraction Bottleneck**: Gold FOL + MAX-SAT = +14.22pp (p=2.0e-7)，自提取仅 +4.9pp (best case) = 35% utilization。聚合机制本身有效，瓶颈在自提取质量。Two-layer analysis:
   - **Constraint taxonomy**: 43% trivially_satisfied（被所有候选答案满足的约束，不排除任何答案）
   - **Discriminative filtering**: 仅 ~8% 约束在 MAX-SAT scoring 中完全 non-discriminative（移除后 0 gains）
   - **关键区分**: 43% 和 8% 度量不同。trivially_satisfied 约束在 MAX-SAT 中仍可有不同满足程度（partial vs full），所以不全是 non-discriminative。但即使 constraints 是 discriminative 的，它们的"区分方向"与模型自身偏差一致（confirmation bias）。both_wrong 组 score_range=29.4。九种修复全部失败。

3. **Regime-Dependent Capability Trap**: SICA 有效性取决于提取模型的基线准确率，存在双边界：
   - Type A (SC ≥ ~60%): 确认偏差，constraints 镜像模型自身答案
   - Type C (SC ≤ ~40%): traces 主要错误，constraints 是噪声 (exp-046: Δ=-2.83pp, p=0.0095)
   - Goldilocks zone (~50-55% SC): 部分独立性 + 部分正确性 (exp-033: Δ=+4.90pp, p=0.013)
   - Type B: 领域不可形式化 (LogiQA: contradiction rate 0.8%)

4. **C0+SC Two-Dimensional Diagnostic**: C0 (multi-candidate rate) + SC accuracy 形成零成本部署诊断。C0<5% → degenerate; high C0 + high SC → trap; high C0 + low SC → potential gains。

### Remediation Evidence (D060: 全部失败 — 强化 analysis narrative)

5. **Nine Remediation Attempts All Failed**: 原 6 种 + 3 种靶向修复全部无效，证明 independence bottleneck 是结构性的：
   - D059 三路 method improvement 全部失败：
     - Discriminative Filtering: 119/204 处理后 0 gains 1 loss，~92% 约束本身就是 discriminative，过滤是 near-no-op
     - T=1.0 (exp-054): delta 从 +4.90pp 崩塌到 +0.55pp，温度敏感性极端
     - Multi-Temp (exp-055): 早期 n=28 delta=0.00pp（待完成，但预期 negative）
   - 原 6 种：contrastive prompting, cross-model extraction, generational scaling, solver-guided refinement, consistency filtering, cross-trace UNSAT
   - 9 种修复涵盖 prompting / architecture / capability / verification / diversity / filtering 全维度，全部失败 → trap is fundamental

## Core Insight (D060 Updated — Dual Bottleneck)

**Dual Requirement Framework**: SICA 效应需要同时满足两个条件，缺一不可：
1. **Sufficient Independence** (Eff-K > threshold): traces 需要提供足够多的独立视角
2. **Sufficient Quality** (SC > ~50%): traces 需要有足够的正确率，否则约束是噪声

Condorcet Jury Theorem 要求投票者独立且 p>0.5。同模型采样的 reasoning traces 严重违反独立性假设（Fleiss' κ = 0.21–0.82，Eff-K 仅 1.20–3.63），解释了为什么简单增加 K 或添加符号约束不能突破 SC 的天花板。

实验数据完美支持 dual requirement：
- **Qwen-14B**: Eff-K≈1.2-1.3（独立性不足）→ 0 gain，无论 SC 多高
- **Mistral-7B FOLIO**: Eff-K≈1.85-2.22（中等独立性）+ SC≈54%（中等质量）→ +4.90pp (2/3 seeds significant)
- **Mistral-7B PW-600**: Eff-K=3.63（最高独立性）但 SC=39%（质量不足）→ -2.83pp
- 只有 Goldilocks zone（中等 Eff-K + 中等 SC）出现正向 delta

Oracle control (+14.22pp) 证明 MAX-SAT 聚合机制本身有效，但自提取约束仅利用了 35% 的理论上限。Discriminative filtering 实验揭示关键机制：~92% 约束 ARE discriminative，但过滤掉 ~8% non-discriminative 约束后 delta 不变（0 gains）。问题不在约束缺乏判别力，而在于 discriminative constraints 的区分方向与模型偏差一致（confirmation bias）。

**κ-delta 反相关解释**：exp-033 κ=0.500 比 exp-052/053 κ≈0.41 高，但 delta 最大。原因：exp-033 Unknown 比例低（49.9% vs 58.5%），traces 更 decisive（更多 True/False 判断）→ 同时导致更高 κ（更多 agreement）和更好的 constraint quality。κ 不是 SICA 效果的唯一决定因素。

**Remediation insight (D060)**: 9 种修复尝试全部失败，包括直接靶向 independence（multi-temp diversity）和 constraint quality（discriminative filtering）。这证明 bottleneck 不是简单的 diversity 或 quality 问题，而是 same-model self-extraction 的根本性限制。

**Key evidence**:
- **Condorcet independence quantification (Worker-verified, 公式: Eff-K=K/(1+(K-1)κ))**: exp-033 Mistral-7B s42 κ=0.500 (Eff-K=1.85), Mistral-7B s123 κ=0.412 (Eff-K=2.17), Mistral-7B s456 κ=0.401 (Eff-K=2.22), Mistral-7B PW-600 κ=0.210 (Eff-K=3.63), Qwen-14B FOLIO κ=0.744 (Eff-K=1.31), Qwen-14B LogiQA κ=0.821 (Eff-K=1.20). 跨模型清晰: Qwen Eff-K≈1.2-1.3→0 gain, Mistral Eff-K≈1.85-3.63→variable. Eff-K necessary but not sufficient: exp-046 highest Eff-K(3.63) but negative delta(SC too low); within Mistral seeds Eff-K非单调 with delta.
- **Oracle control (exp-031)**: Gold FOL + MAX-SAT = 89.71% vs SC 75.49% (+14.22pp, p=2.0e-7). Unknown-type +31.9pp.
- **Two-layer constraint analysis**: 43% trivially_satisfied (taxonomy: satisfied by ALL answers) vs ~8% non-discriminative (filtering: same MAX-SAT score). Difference: trivially_satisfied constraints can still have different satisfaction DEGREES. Removing the 8% yields 0 gains → problem is not quality but confirmation bias direction.
- **K sensitivity (inverted U)**: K=4(-1.47pp), K=8(-0.98pp), K=12(+4.90pp p=0.013), K=16(+1.47pp), K=20(pending). Peak at K=12, then decline. Non-monotonic. K=4 SC ≈ K=12 SC but SICA differs by 6.4pp — proves SICA extracts different information than SC.
- **T sensitivity (extreme fragility)**: T=0.7(+4.90pp p=0.013), T=1.0(+0.49pp p=0.739). 温度从 0.7 提到 1.0 让增益降 90%。T=0.3 (exp-057, pending). SICA 效应极度依赖超参数。
- **Regime boundary**: Qwen-14B (SC=75.49%) Δ=+0.25pp vs Mistral-7B (SC=54.41%) Δ=+4.90pp p=0.013
- **Type C failure (exp-046)**: Mistral PW-D5 SC=39.33%, Δ=-2.83pp, p=0.010, κ=0.210, Eff-K=3.63, contradiction rate 5.5%. Highest Eff-K yet worst delta → independence alone insufficient when SC too low.
- **Seed replication**: 2/3 seeds significant at α=0.05 (exp-033 p=0.013, exp-052 p=0.039), 1/3 null (exp-053). Effect IS real but fragile — motivates deep analysis of WHY.
- **Nine remediation failures**: contrastive prompting, cross-model, generational scaling, solver-guided, consistency filtering, cross-trace UNSAT, discriminative filtering (0 gains), T=1.0 (delta collapse), multi-temp (pending, early 0.00pp). All failed → trap is fundamental.
- **Entropy mechanism**: High-entropy problems proportion: Mistral 35.8% vs Qwen 10.3%. Unanimous rate: 18.6% vs 58.8%.
- **Confirmation bias quantification**: Override precision 70.6% (Mistral) vs 28.6% (Qwen). Constraint agreement >80%: 31.9% vs 62.3%.

## Story Spine (D059 Updated)

- **Problem**: LLMs' reasoning can be improved by sampling multiple chains-of-thought and aggregating via majority voting (self-consistency). Recent work proposes symbolic augmentation: extract formal constraints from traces and use SAT solvers for answer selection. But does symbolic aggregation actually outperform simple voting?
- **Theoretical lens**: Condorcet Jury Theorem requires voter independence. We quantify trace independence via Fleiss' κ and show Effective-K << nominal K. This explains the fundamental limitation of same-model trace aggregation.
- **Systematic evaluation**: SICA (MAX-SAT over FOL constraints) across 3 domains × 5 model families. Oracle control separates extraction vs aggregation failure. Discriminative filtering reveals ~92% constraints are discriminative, yet SICA gains are fragile — confirmation bias, not constraint quality, is the bottleneck.
- **Regime characterization**: Three failure modes (Type A/B/C) + narrow Goldilocks zone. C0+SC as deployment diagnostic.
- **Remediation failures strengthen thesis**: 9 targeted interventions (prompting, architecture, capability, verification, diversity, filtering) all fail to close the oracle gap, proving the bottleneck is fundamental to same-model self-extraction.
- **Headline result**: "Across 5 model families, symbolic consensus aggregation shows a real but fragile effect: significant improvement in 2/3 seeds under specific conditions (Mistral-7B, FOLIO, T=0.7, K=12), but zero or negative gains under any perturbation. Condorcet analysis reveals the root cause: Effective-K = 1.3-1.8 for nominal K=12 due to trace non-independence. Oracle constraints prove the aggregation mechanism works (+14.22pp), but 9 remediation strategies all fail to overcome the self-extraction bottleneck. C0+SC provides a zero-cost deployment diagnostic."

## Anticipated Reviewer Concerns & Defensive Experiments

1. **"Gains not statistically significant"** → exp-033 p=0.013 (n=204), exp-031 oracle p=2.0e-7. Combined N>1,200.
2. **"Only one positive result (exp-033)"** → Seed replication: 2/3 significant (p=0.013, p=0.039). Effect IS real but fragile — the fragility itself IS the finding (K/T sensitivity, Condorcet independence).
3. **"Condorcet framework is trivial"** → Fleiss' κ quantification is novel in SC/SICA context. Eff-K is actionable: tells practitioners how many truly independent traces they get.
4. **"Multi-temp / filtering should work"** → We tried both. Multi-temp (exp-055): negative. Disc. filtering: 0 gains. T=1.0: delta collapse. These failures STRENGTHEN the structural bottleneck thesis.
5. **"Only Qwen models"** → 5 families: Qwen-14B, Mistral-7B, LLaMA-8B, DeepSeek-R1-7B, QwQ-32B.
6. **"Only logic domain"** → FOLIO + ProofWriter + LogiQA + StrategyQA + ARC-Challenge. Type B (domain formalizability) is itself a finding.
7. **"Oracle is unfair comparison"** → Diagnostic tool, not competing method. Separates extraction from aggregation.
8. **"MAX-SAT is over-engineering"** → exp-013: MaxSAT ≈ count-only. This IS the independence bottleneck evidence.
9. **"Self-extraction confound"** → Oracle control resolves completely.
10. **"Published methods achieve gains (DyLoS, Aristotle, FoVer)"** → Different paradigm (external verifiers/trained extractors). We characterize same-model self-extraction.
11. **"C0 is trivially derived"** → Zero-cost early stopping. Practical value.
12. **"Why not just use a reasoning model?"** → QwQ-32B: C0<5%, SICA≡SC.
13. **"Random tiebreak baseline"** → exp-003: SICA tiebreak 80% vs random 50%.
14. **"Method improvement is incremental"** → Grounded in diagnosis (independence + taxonomy), not ad-hoc.
15. **"Weighted SC is simpler"** → exp-016 planned. Weighted SC doesn't address independence.
16. **"Within-model ICL transition contradicts regime theory"** → exp-050b (SC=57.79%, Δ=-3.52pp): ICL changes trace generation characteristics, not just SC level. Paper must distinguish "same model, different prompt" from "same model, same prompt, different accuracy."

## Working Title
**"Beyond Self-Consistency: How Trace Independence Limits Symbolic Consensus in LLM Reasoning"**
(Alternatives:
- "The Independence Bottleneck: Why Self-Extracted Symbolic Constraints Cannot Beat Majority Voting"
- "Symbolic Consensus Under the Condorcet Lens: Independence, Extraction, and the Limits of Self-Aggregation")

NOTE (Dream D037): Title MUST be scoped to "self-extracted constraints" / "SICA". Published methods (DyLoS, Aristotle, FoVer) use different approaches.

## Paper Structure (EMNLP 8pp + appendix)

### Main Tables
- T1: Main Results — models × domains, SC% / SICA% / Δpp / p-value, regime boundary
- T2: Oracle Control — Gold-FOL+MAX-SAT vs SC vs SICA-self, causal separation
- T3: Independence Quantification — Fleiss' κ / Eff-K / trace agreement per model
- T4: Extraction Error Taxonomy — trivially_satisfied / discriminative / both_wrong rates
- T5: K Sensitivity — K=4/8/12/16/20 with Eff-K and diversity metrics (inverted U curve)

### Main Figures
- F1: Method Pipeline (SICA + oracle control design)
- F2: SC Accuracy vs SICA Δ scatter (hero figure, regime boundary)
- F3: K Sensitivity with diversity metrics (K vs Δ, K vs Eff-K)
- F4: Extraction error breakdown (stacked bar)

### Appendix
- K ablation details, temperature sensitivity, per-domain results, overhead analysis
- Entropy-conditioned analysis (continuous scatter + bin sensitivity)
- Six remediation strategy details
- Confirmation bias quantification
- Seed replication analysis
- QwQ-32B / DeepSeek-R1 negative control

## Claim Risk Notes (D059)
- **Seed replication**: 2/3 significant (p=0.013, p=0.039), 1/3 null. Frame as "real but fragile effect" — motivates analysis of WHY.
- **Method claims DEAD (D060)**: All three method improvements failed. Paper is pure analysis. 9 remediation failures are EVIDENCE, not limitation.
- **Condorcet novelty**: ✅ VERIFIED. arXiv:2409.00094 applies CJT to cross-model LLM ensembles (different angle). No prior work applies Fleiss' κ or Eff-K to within-model SC traces. Our framing is novel.
- **exp-050b complication**: ICL transition Δ=-3.52pp at SC=57.79% complicates simple "SC determines SICA." Explain via trace generation characteristic change.
- **Variable naming inconsistency**: 56.4% cross-trace pairs share zero Z3 variables. Key mechanism evidence.

## Required Citations (minimum 30 references)

- **SC & extensions**: Wang et al. 2023 (SC), Chen et al. 2023 (USC), Loo et al. 2025 (SC scaling plateaus), Taubenfeld et al. 2025 (weighted SC), DiVeRSe (Li et al. 2023)
- **Neuro-symbolic reasoning**: DyLoS (EACL 2026), Aristotle (ACL 2025), FoVer (TACL 2025), LogicAgent (2025), Logic-LM (Pan et al. 2023), LINC (Olausson et al. 2023)
- **Condorcet/voting theory**: Condorcet 1785, Austen-Smith & Banks 1996, **arXiv:2409.00094 (Examining Independence in Ensemble Sentiment Analysis, Sept 2024)** — closest prior work, applies CJT to cross-model LLM ensembles, finds independence violation. Our novelty: within-model trace independence + Fleiss' κ quantification + Eff-K + connection to symbolic aggregation
- **Test-time compute**: Snell et al. 2025, DeepSeek-R1, Diversity-Aware Training
- **Verification & reranking**: ORM (Cobbe et al. 2021), PRM (Lightman et al. 2023), Math-Shepherd
- **Constraint satisfaction**: SATBench (EMNLP 2025), LLM Meets Constraint Propagation (IJCAI 2025)
- **Debate & multi-agent**: Liang et al. 2023, Du et al. 2023

## Claim Scoping Rules
- n=60 conditions: "suggestive/consistent with" NOT "confirming"
- n≥200 conditions: can "confirm"
- Combined N>1,300: acceptable if breakdown clearly stated
- Method claims: must show statistically significant improvement OR clear directional improvement with analysis
- "Independence bottleneck" framing: systematic quantification + theoretical grounding


## experiment_plan (with registry status)

- id: exp-001
  name: sica_expanded_14b
  claim:
  - 1
  - 2
  description: 'Full-scale evaluation: PW D5 600 + FOLIO 204 = 804 questions, K=12,
    T=0.7. Maximizes statistical power for C3 significance.'
  priority: P0
  gpu_budget_hours: 14
  deps: []
  registry_id: sica_expanded_14b
  status: DONE
  conclusion: success
  metrics:
    sica_accuracy: 0.765
    sc_accuracy: 0.762
    sica_sc_gap_pp: 0.3
    n_problems: 804
    multi_candidate_rate: 0.3818
    folio_sica: 0.794
    folio_sc: 0.794
    folio_gap_pp: 0
    folio_n: 204
    proofwriter_sica: 0.755
    proofwriter_sc: 0.752
    proofwriter_gap_pp: 0.3
    proofwriter_n: 600
    extraction_rate: 0.89
    answer_extraction_rate: 1
    contradiction_rate: 0.022
    problems_with_contradictions: 331
    truncated_traces: 0
    wall_time_min: 826
- id: exp-002
  name: sica_k_ablation_14b
  claim:
  - 1
  description: 'K sensitivity (K=6,8,11,12,16,20) on D012''s 60 questions. Includes
    odd K=11 to test if SICA value persists without exact ties. Key questions: does
    SICA benefit depend on tiebreaks? What happens at odd K? How does tiebreak frequency
    change with K?'
  priority: P0
  gpu_budget_hours: 6
  deps: []
  status: planned
  note: D024 增加 K=11（odd-K test, Dream 三档一致要求）。如 K=11 gap=0 → 确认 tie-only mechanism；如
    gap>0 → SICA has value beyond tiebreaking。
- id: exp-003
  name: tiebreak_baseline_analysis
  claim:
  - 1
  description: Compare SICA vs SC-random-tiebreak vs SC-deterministic on all available
    data. CPU-only reanalysis. Quantify how much of SICA's gain survives against fair
    baselines.
  priority: P0
  gpu_budget_hours: 0
  deps:
  - sica_d012_14b
  status: planned
  note: 'Completed as CPU analysis, no registry entry. Results: SICA tiebreak 80%
    (4/5) vs random 50% vs alphabetical 60% vs first-seen 40%. Artifact: art_20260516_47de9d'
- id: exp-004
  name: sica_7b_scaling
  claim:
  - 2
  - 3
  description: 'Run SICA with Qwen2.5-7B-Instruct on same 60 questions. Test: does
    weaker model → higher C0 → larger SICA gain? Validates C0-as-predictor claim.'
  priority: P1
  gpu_budget_hours: 2
  deps:
  - exp-001
  status: planned
- id: exp-005
  name: qwq_32b_operating_regime
  claim:
  - 2
  description: QwQ-32B negative results formatted for paper's Operating Regime Analysis
    section. Data exists from MVP phase (AIME, MATH, ProofWriter, FOLIO). No new GPU
    needed.
  priority: P1
  gpu_budget_hours: 0
  deps: []
  status: planned
  note: 'Data from QwQ-32B MVP experiments: sica_aime30_v3 (AIME 22题, 0% multi-candidate),
    sica_proofwriter30_v2 (PW 16题, 18.75% multi-candidate), sica_folio30 (FOLIO 10题,
    0% multi-candidate). Combined C0=3.6%, SICA≡SC across all domains.'
- id: exp-006
  name: c0_diagnostic_validation
  claim:
  - 3
  description: Plot C0 vs SICA-SC gap across all models and K values. Validate C0
    as predictor. CPU-only analysis over exp-001/002/004/005 results.
  priority: P1
  gpu_budget_hours: 0
  deps:
  - exp-001
  - exp-002
  - exp-004
  status: planned
- id: exp-007
  name: sica_72b_awq
  claim:
  - 2
  description: 'Qwen2.5-72B-Instruct AWQ 4-bit on 60 questions. Scaling analysis:
    high-baseline non-reasoning model. Within-Qwen scaling dimension.'
  priority: P1
  gpu_budget_hours: 4
  deps:
  - exp-001
  status: planned
  note: D019 升级 P2→P1. 72B-AWQ 4-bit ~36GB weights + KV cache ≈ 50-60GB, 98GB RTX
    PRO 6000 单卡可放。
- id: exp-008
  name: constraint_quality_case_studies
  claim:
  - 1
  description: Qualitative analysis of extracted constraints on 5-10 representative
    questions. Are constraints semantically meaningful? Do excluded constraints correspond
    to reasoning errors?
  priority: P2
  gpu_budget_hours: 0
  deps:
  - exp-001
  status: planned
- id: exp-009
  name: overhead_analysis
  claim:
  - 1
  description: 'Wall-time breakdown per question: generation, constraint extraction,
    MaxSAT solving. Address ''is the overhead worth it'' concern.'
  priority: P1
  gpu_budget_hours: 0
  deps:
  - exp-001
  status: planned
  note: D021 升级 P2→P1. Reviewer 指出 EMNLP 审稿人对 practical impact 极敏感。
- id: exp-010
  name: sica_mistral_7b
  claim:
  - 2
  - 3
  description: 'Mistral-7B-Instruct-v0.3 on D012 60 questions (PW+FOLIO). Cross-family
    validation: does C0 pattern hold outside Qwen? Eliminates ''Qwen-specific artifact''
    attack.'
  priority: P0
  gpu_budget_hours: 1.5
  deps: []
  status: DONE
  note: 'D021 新增. 必做——消除 Claim 2 致命弱点。Escalation: 若 C0>30% 且 gap>0 但 p>0.2，扩展到 200+
    题（~3h GPU，margin 允许）。'
  registry_id: exp-010-mistral-v3
  conclusion: negative
  metrics:
    n: 60
    k: 12
    sica_accuracy: 0.4833
    sc_accuracy: 0.4833
    delta_pp: 0
    multi_candidate_rate: 0.5
    extraction_rate: 0.8819
    answer_extraction_rate: 1
    contradiction_rate: 0.0562
    discordant_sica_wins: 2
    discordant_sc_wins: 2
    mcnemar_p: 1
    proofwriter_sica: 0.4
    proofwriter_sc: 0.4
    proofwriter_delta_pp: 0
    folio_sica: 0.5667
    folio_sc: 0.5667
    folio_delta_pp: 0
    truncated_traces: 0
    model: Mistral-7B-Instruct-v0.3
    dataset: D012
- id: exp-011
  name: sica_llama_8b
  claim:
  - 2
  - 3
  description: LLaMA-3.1-8B-Instruct on D012 60 questions. Second non-Qwen family.
    Combined with exp-010 gives 3-family coverage (Qwen/Mistral/LLaMA).
  priority: P0
  gpu_budget_hours: 1.5
  deps: []
  status: planned
  note: D021 新增. 必做——3 家族是 EMNLP 最低门槛。需 HF_TOKEN（Meta license）或 ModelScope 镜像。Escalation
    同 exp-010。
- id: exp-012
  name: gsm8k_pilot_14b
  claim:
  - 2
  - 3
  description: 'Qwen2.5-14B on GSM8K 30-question pilot (K=12). Cross-domain test:
    is C0 high only in restricted-answer-space domains (NLI 3-class) or also in open-answer
    math? If C0 low → C0=uncertainty signal (strengthens Claim 3). If C0 high → cross-domain
    win.'
  priority: P1
  gpu_budget_hours: 1
  deps: []
  status: planned
  note: D021 新增. Reviewer 预测 C0<20% (14B too strong on GSM8K). Any result is publishable
    insight.
- id: exp-013
  name: constraint_ablation
  claim:
  - 1
  - 2
  description: 'CPU-only ablation: SICA-MaxSAT vs SICA-count-only (constraint count
    per answer, no satisfiability) vs SICA-random-weight. Critical for D025 pivot:
    if MaxSAT ≈ count-only → aggregation mechanism is vacuous, confirming capability
    trap.'
  priority: P0
  gpu_budget_hours: 0
  deps:
  - exp-001
  status: planned
  note: 'D025 升级 P1→P0. 现在是 make-or-break: 如果 MaxSAT = count-only → 证明 SAT 解算无贡献（capability
    trap 的 mechanism evidence）。必须用 exp-002 的 raw_constraints 数据。'
- id: exp-014
  name: sica_deepseek_r1_llama_8b
  claim:
  - 2
  description: 'DeepSeek-R1-Distill-LLaMA-8B on D012 60 questions. Second reasoning
    model data point with LLaMA base architecture: validates C0<5% generalizes beyond
    QwQ-32B AND eliminates ''still Qwen family'' attack.'
  priority: P1
  gpu_budget_hours: 2
  deps: []
  status: planned
  note: D021 新增. Reviewer 建议用 LLaMA 底座版本避免 Qwen 架构归属争议。
- id: exp-015
  name: logic_lm_baseline
  claim:
  - 1
  description: Logic-LM × K + majority vote baseline on FOLIO. Run Logic-LM style
    single-trace FOL verification K times, then majority vote. Isolates whether MAX-SAT
    multi-trace aggregation adds value beyond FOL extraction itself.
  priority: P1
  gpu_budget_hours: 0
  deps:
  - exp-001
  status: planned
  note: 'D024 新增. Dream 三档一致要求 Logic-LM/LINC 比较。CPU-only: 用 exp-001 已有 traces + FOL
    constraints 做单 trace verification then vote。'
- id: exp-016
  name: weighted_sc_baseline
  claim:
  - 1
  - 3
  description: 'Weighted SC baseline (Taubenfeld et al. 2024 style): weight votes
    by trace confidence/length/perplexity. CPU-only reanalysis of exp-001/002 data.
    Tests if simple weighting achieves same tiebreak quality without MAX-SAT.'
  priority: P1
  gpu_budget_hours: 0
  deps:
  - exp-001
  status: planned
  note: 'D024 新增. Dream 提出 weighted SC 是最直接竞争 baseline。实现方式: (1) uniform weight (=SC),
    (2) length-weighted, (3) log-prob weighted (如 traces 有 logprobs), (4) constraint-count
    weighted (no SAT)。'
- id: exp-017
  name: sica_strategyqa_14b
  claim:
  - 1
  - 2
  description: Qwen2.5-14B on StrategyQA 60 questions (K=12). Commonsense reasoning
    domain — high predicted C0 (35-50%) but implicit reasoning chains → low expected
    constraint quality. Tests capability trap in best-case-diversity scenario.
  priority: P0
  gpu_budget_hours: 1.5
  deps: []
  status: planned
  note: D025 新增. Reviewer 推荐 ROI 最高 benchmark。如 C0>30% 且 SICA≈SC → 直接证明 capability
    trap（diversity high but quality low → no gain）。
- id: exp-018
  name: sica_arc_challenge_14b
  claim:
  - 1
  - 2
  description: Qwen2.5-14B on ARC-Challenge 60 questions (K=12). Science reasoning,
    4-choice format. Tests constraint mechanism in multi-choice scenario + different
    domain.
  priority: P0
  gpu_budget_hours: 1.5
  deps: []
  status: planned
  note: D025 新增. 4选1格式测试 constraint mechanism 泛化能力。与 FOLIO (3-class) + GSM8K (open)
    + StrategyQA (binary) 形成答案格式多样性。
- id: exp-019
  name: constraint_quality_correlation
  claim:
  - 1
  - 2
  description: 'CPU-only analysis: compute constraint precision per domain × model,
    correlate with C0 and SICA-SC gap. Formalizes the capability trap as inverse C0-quality
    correlation. Uses data from exp-001/010/011/017/018.'
  priority: P0
  gpu_budget_hours: 0
  deps:
  - exp-001
  - exp-017
  - exp-018
  status: planned
  note: 'D025 新增. Hero figure (F2) 的数据来源。Constraint quality = (constraints consistent
    with ground truth) / (total constraints). 预期: high C0 domains (StrategyQA) have
    low quality, low C0 domains (math) have high quality but SICA=SC anyway.'


## registry (completed experiments)

- exp_id: crd_folio_main
  name: ''
  status: DONE
  conclusion: success
  metrics:
    divergence_rate: 0.422
    diagnosis_rate: 0.872
    error_types: 4
    directed_advantage_pp: 4.7
    directed_p_value: 0.63
    localization_accuracy: 0.946
    fol_accuracy: 0.789
    code_accuracy: 0.598
    oracle_accuracy: 0.878
    pipeline_accuracy: 0.814
    baseline_accuracy: 0.74
    cost_multiplier: 5.76
    dataset: FOLIO
    n: 204
- exp_id: smoke-test-5q
  name: ''
  status: PREPARING
  conclusion: failed
  metrics: {}
- exp_id: sica_smoke_5q
  name: ''
  status: DONE
  conclusion: success
  metrics:
    sica_accuracy: 0.8
    sc_accuracy: 0.8
    extraction_rate: 1
    problems_with_contradictions: 1
    total_problems: 5
    total_time_s: 3505
    avg_time_per_problem_s: 701
    per_problem:
    - id: algebra/2470
      level: 1
      sica_correct: true
      sc_correct: true
      constraints: 27
      unique: 9
      excluded: 0
    - id: prealgebra/65
      level: 2
      sica_correct: true
      sc_correct: true
      constraints: 26
      unique: 2
      excluded: 0
    - id: number_theory/847
      level: 3
      sica_correct: true
      sc_correct: true
      constraints: 21
      unique: 11
      excluded: 0
      note: 14 JSON parse failures, 1693s
    - id: precalculus/1199
      level: 4
      sica_correct: false
      sc_correct: false
      constraints: 35
      unique: 6
      excluded: 0
      note: graph-reading problem, model cannot see image
    - id: algebra/2277
      level: 5
      sica_correct: true
      sc_correct: true
      constraints: 60
      unique: 6
      satisfied: 3
      excluded: 3
- exp_id: sica_temp_diversity
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    temperatures_tested:
    - 0.7
    - 0.9
    - 1
    problems_tested: 3
    problems_with_divergence: 0
    finding: QwQ-32B produces zero answer divergence at all temperatures on MATH L4-5.
      Reasoning model's deterministic chain dominates sampling randomness.
    max_tokens_issue: 4096 tokens insufficient for some L5 problems (truncation)
    recommendation: Use AIME 2024 (harder, ~79.5% acc) or non-reasoning model for
      trace diversity
- exp_id: mvp_math50_t07
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: sica_aime30_t07
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: sica_aime30_v2
  name: ''
  status: DONE
  conclusion: killed
  metrics:
    progress: 4/30
    sica_accuracy_interim: 3/4 (75%)
    sc_accuracy_interim: 3/4 (75%)
    avg_time_per_problem_s: 557
    p2_z3_error: Z3Exception on z3_maxsat.py:163, 0 constraints extracted
    p5_vllm_stuck: vLLM timeout since ~22:11, retried multiple rounds
    issue: vLLM service likely crashed or OOM at Problem 5
    analysis_contradiction_rate_aime: 50% (2/4)
    analysis_contradiction_rate_math: 20% (1/5)
    analysis_unique_constraints_per_problem_aime: 18.7
    analysis_exclusion_rate: 10.7%
    analysis_sica_sc_agreement: 9/9 (100%)
    analysis_signal: weak positive - mechanism works but SC too unanimous to flip
    analysis_p2_failure: 0 constraints, 0 votes - answer extraction failure
- exp_id: sica_aime30_v3
  name: ''
  status: DONE
  conclusion: killed
  metrics:
    progress: 22/30
    sica_accuracy_interim: 16/22 (72.7%)
    sc_accuracy_interim: 16/22 (72.7%)
    sica_sc_gap_pp: 0
    avg_time_per_problem_s: 645.9
    runtime_h: 5.9
    remaining_problems: 8
    vote_diversity_analysis:
      valid_problems: 16
      total_problems: 22
      multi_candidate_rate: 0
      zero_vote_problems: 6
      zero_vote_indices:
      - 1
      - 7
      - 8
      - 10
      - 13
      - 14
      constraints_extracted: 19/22
      exclusion_rate: 0.387
      conclusion: All 16 valid problems have exactly 1 candidate answer. SICA≡SC structurally.
        MaxSAT exclusion operates but cannot change final selection with only 1 candidate.
    process_status: gone (cron miss 1/5)
- exp_id: sica_proofwriter30
  name: ''
  status: DONE
  conclusion: failed
  metrics:
    sica_accuracy: 0/30 (0.0%)
    sc_accuracy: 0/30 (0.0%)
    sica_sc_gap_pp: 0
    total_wall_time_s: 238.9
    total_wall_time_min: 4
    avg_time_per_problem_s: 8
    traces_generated: 0
    constraints_extracted: 0
    traces_with_constraints: 0
    unique_constraints: 0
    maxsat_satisfied: 0
    maxsat_excluded: 0
    multi_candidate_rate: N/A (no traces generated)
    vote_diversity: N/A
    z3_errors: 0
    z3_timeouts: 0
    problems_with_contradiction: 0
    problems_with_votes: 0
    failure_mode: ALL_400_BAD_REQUEST
    failure_count: 30/30
    root_cause: max_tokens=16384 equals max_model_len=16384, leaving 0 tokens for
      prompt input. Every API call returns 400.
- exp_id: sica_folio30
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: sica_proofwriter30_v2
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: sica_d016_c0_precheck
  name: ''
  status: DONE
  conclusion: success
  metrics:
    multi_candidate_rate_combined: 0.46
    multi_candidate_rate_folio: 0.4
    multi_candidate_rate_proofwriter: 0.5
    sc_accuracy_combined: 0.73
    sc_accuracy_folio: 0.8
    sc_accuracy_proofwriter: 0.69
    n_problems: 26
    n_folio: 10
    n_proofwriter: 16
    K: 6
    T: 0.7
    total_time_s: 280
    c0_gate: PASS (46% >= 20%)
    model: Qwen2.5-14B-Instruct
    vllm_gpu_mem_gib: 27.6
    smoke_test: 2 problems end-to-end OK, constraints 21-26 per problem
- exp_id: sica_d012_14b
  name: ''
  status: DONE
  conclusion: success
  metrics:
    sica_accuracy: 0.7333
    sc_accuracy: 0.7
    sica_sc_gap_pp: 3.3
    c0_multi_candidate_rate: 0.5333
    c1_extraction_rate: 1
    c2_contradiction_problems: 34
    c3_gap_pp: 3.3
    bootstrap_p: 0.2261
    proofwriter_sica: 0.6667
    proofwriter_sc: 0.6667
    folio_sica: 0.8
    folio_sc: 0.7333
    total_constraints_raw: 5849
    total_constraints_unique: 1735
    maxsat_exclusion_rate: 0.0259
    wall_time_min: 58.3
    d012_verdict: ALL_PASS
- exp_id: sica_expanded_14b
  name: ''
  status: DONE
  conclusion: success
  metrics:
    sica_accuracy: 0.765
    sc_accuracy: 0.762
    sica_sc_gap_pp: 0.3
    n_problems: 804
    multi_candidate_rate: 0.3818
    folio_sica: 0.794
    folio_sc: 0.794
    folio_gap_pp: 0
    folio_n: 204
    proofwriter_sica: 0.755
    proofwriter_sc: 0.752
    proofwriter_gap_pp: 0.3
    proofwriter_n: 600
    extraction_rate: 0.89
    answer_extraction_rate: 1
    contradiction_rate: 0.022
    problems_with_contradictions: 331
    truncated_traces: 0
    wall_time_min: 826
- exp_id: sica_k_sensitivity_14b
  name: ''
  status: DONE
  conclusion: success
  metrics:
    K6_sica: 0.733
    K6_sc: 0.733
    K6_gap_pp: 0
    K8_sica: 0.733
    K8_sc: 0.75
    K8_gap_pp: -1.7
    K11_sica: 0.733
    K11_sc: 0.733
    K11_gap_pp: 0
    K12_sica: 0.7
    K12_sc: 0.75
    K12_gap_pp: -5
    K16_sica: 0.717
    K16_sc: 0.75
    K16_gap_pp: -3.3
    K20_sica: 0.7
    K20_sc: 0.733
    K20_gap_pp: -3.3
    all_K_sica_leq_sc: true
    larger_K_degrades_sica: true
- exp_id: sica_constraint_ablation_013
  name: ''
  status: DONE
  conclusion: success
  metrics:
    maxsat_accuracy: 0.7649
    count_only_accuracy: 0.7662
    random_weight_accuracy: 0.7587
    sc_baseline_accuracy: 0.7624
    n_problems: 804
    maxsat_correct: 615
    count_only_correct: 616
    random_weight_correct: 610
    sc_correct: 613
    agreement_maxsat_vs_countonly: 803/804
    agreement_maxsat_vs_randomwt: 785/804
    agreement_maxsat_vs_sc: 773/804
    agreement_countonly_vs_randomwt: 786/804
    agreement_countonly_vs_sc: 774/804
    agreement_randomwt_vs_sc: 764/804
    mcnemar_p_all_gt_0.7: true
- exp_id: exp-005
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    qwq_aggregate_c0_nominal_pct: 10.3
    qwq_aggregate_c0_effective_pct: 2.6
    qwen14b_c0_pct: 46
    diversity_ratio_effective: 17.7
    aime_delta_pp: 0
    proofwriter_delta_pp: -5.9
    aime_n: 22
    proofwriter_n: 17
    temp_diversity_n: 5
    folio_n: 2
    total_problems: 46
    c0_threshold: 20
    qwq_below_threshold: true
- exp_id: exp-011-llama8b
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: exp-016-weighted-sc
  name: ''
  status: DONE
  conclusion: success
  metrics:
    sica_accuracy: 0.7649
    sc_uniform_accuracy: 0.7624
    inv_length_accuracy: 0.7674
    length_weighted_accuracy: 0.7525
    constraint_count_accuracy: 0.7525
    inv_length_vs_sc_p: 0.453
    length_vs_sc_p: 0.153
    inv_length_vs_sica_p: 0.864
    length_vs_sica_p: 0.066
    n_problems: 804
    all_nonsignificant: true
- exp_id: exp-010-mistral
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: exp-011-llama8b-v2
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: exp-017-strategyqa
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: exp-018-arc
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: exp-010-mistral-v2
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: exp-017-strategyqa-v2
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: exp-017-strategyqa-v3
  name: ''
  status: DONE
  conclusion: success
  metrics:
    n: 60
    k: 12
    sica_accuracy: 0.5667
    sc_accuracy: 0.5333
    delta_pp: 3.33
    mcnemar_chi2: 0.5
    mcnemar_p: n.s.
    bootstrap_ci_95:
    - 0
    - 8.33
    bootstrap_p_delta_le_0: 0.1346
    multi_candidate_rate: 0.1
    contradiction_detected: 5
    extraction_rate_problem: 1
    extraction_rate_trace: 0.704
    discordant_sica_wins: 2
    discordant_sc_wins: 0
- exp_id: pilot-constraint-filtering
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    n: 43
    thresholds_tested:
    - 1
    - 2
    - 3
    - 5
    - 7
    best_gap_pp: 2.33
    best_T: 1
    sica_T1: 0.7674
    sc: 0.7442
    T5_gap: 0
    T7_gap: 0
    discriminative_ratio_count: 0.115
    discriminative_ratio_weight: 0.372
    effective_flip_rate: 0.174
    multi_answer_problems: 23
    unanimous_problems: 20
    problems_disc_favors_different: 4
- exp_id: exp-018-arc-v2
  name: ''
  status: DONE
  conclusion: success
  metrics:
    n: 60
    k: 12
    sica_accuracy: 0.95
    sc_accuracy: 0.9667
    delta_pp: -1.67
    multi_candidate_rate: 0.05
    extraction_rate: 1
    contradiction_detected: 3
    discordant_sica_wins: 0
    discordant_sc_wins: 1
    dataset: ARC-Challenge
    model: Qwen2.5-14B-Instruct
- exp_id: exp-011-llama8b-v3
  name: ''
  status: DONE
  conclusion: success
  metrics:
    n: 60
    k: 12
    sica_accuracy: 0.6667
    sc_accuracy: 0.6
    delta_pp: 6.67
    multi_candidate_rate: 0.6167
    extraction_rate: 0.8556
    answer_extraction_rate: 0.8958
    contradiction_rate: 0.0527
    problems_with_contradictions: 43
    truncated_traces: 44
    discordant_sica_wins: 5
    discordant_sc_wins: 1
    mcnemar_p: 0.2188
    proofwriter_sica: 0.6333
    proofwriter_sc: 0.6
    proofwriter_delta_pp: 3.33
    folio_sica: 0.7
    folio_sc: 0.6
    folio_delta_pp: 10
    model: LLaMA-3.1-8B-Instruct
    dataset: D012
    wall_time_min: 66.4
- exp_id: pilot-contrastive-prompt
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: exp-010-mistral-v3
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    n: 60
    k: 12
    sica_accuracy: 0.4833
    sc_accuracy: 0.4833
    delta_pp: 0
    multi_candidate_rate: 0.5
    extraction_rate: 0.8819
    answer_extraction_rate: 1
    contradiction_rate: 0.0562
    discordant_sica_wins: 2
    discordant_sc_wins: 2
    mcnemar_p: 1
    proofwriter_sica: 0.4
    proofwriter_sc: 0.4
    proofwriter_delta_pp: 0
    folio_sica: 0.5667
    folio_sc: 0.5667
    folio_delta_pp: 0
    truncated_traces: 0
    model: Mistral-7B-Instruct-v0.3
    dataset: D012
- exp_id: exp-019-llama8b-strategyqa-200
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    n: 200
    k: 12
    sica_accuracy: 0.74
    sc_accuracy: 0.72
    delta_pp: 2
    multi_candidate_rate: 0.41
    mcnemar_p: 0.424
    bootstrap_ci_95:
    - -1.5
    - 5.5
    bootstrap_p_delta_le_0: 0.12
    discordant_sica_wins: 9
    discordant_sc_wins: 5
    discordant_total: 14
    discordant_rate: 0.07
    sc_unanimous_rate: 0.545
    model: LLaMA-3.1-8B-Instruct
    dataset: StrategyQA
    wall_time_min: 52
- exp_id: exp-020-llama8b-folio-204
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    n: 204
    k: 12
    sica_accuracy: 0.608
    sc_accuracy: 0.632
    delta_pp: -2.45
    mcnemar_p: 0.2668
    bootstrap_ci_95:
    - -5.88
    - 0.98
    bootstrap_p_sica_ge_sc: 0.1
    discordant_sica_wins: 4
    discordant_sc_wins: 9
    discordant_total: 13
    discordant_rate: 0.064
    multi_candidate_rate: 0.618
    extraction_rate: 0.942
    answer_extraction_rate: 0.951
    contradiction_rate: 0.062
    both_wrong: 71
    model: LLaMA-3.1-8B-Instruct
    dataset: FOLIO-204
    wall_time_min: 131.7
- exp_id: exp-009-overhead-analysis
  name: ''
  status: DONE
  conclusion: success
  metrics:
    n: 804
    mean_total_wall_s: 61.6
    mean_trace_gen_s: 31.6
    trace_gen_pct: 51.3
    mean_extract_s: 29
    extract_pct: 47
    mean_dedup_s: 1
    dedup_pct: 1.6
    mean_maxsat_s: 0.003
    maxsat_pct: 0.005
    sica_overhead_s: 30
    sica_overhead_pct: 48.7
    pw_overhead_pct: 51.3
    folio_overhead_pct: 38.6
    p50_overhead_pct: 48.9
    p90_overhead_pct: 57.6
- exp_id: exp-014-deepseek-r1-7b
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    n: 60
    k: 12
    sica_accuracy: 0.6833
    sc_accuracy: 0.7167
    delta_pp: -3.33
    multi_candidate_rate: 0.583
    extraction_rate: 0.839
    answer_extraction_rate: 0.939
    truncated_traces: 72
    contradiction_rate: 0.037
    wall_time_min: 100.3
    mcnemar_p: 0.4795
    discordant_sica_wins: 0
    discordant_sc_wins: 2
    model: DeepSeek-R1-Distill-Qwen-7B
    dataset: D012
- exp_id: temperature-ablation-t03
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    n: 60
    k: 12
    sica_accuracy: 0.7333
    sc_accuracy: 0.7333
    delta_pp: 0
    multi_candidate_rate: 0.3
    discordant_total: 0
    model: Qwen2.5-14B-Instruct
    dataset: D012
    temperature: 0.3
- exp_id: temperature-ablation-t05
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    n: 60
    k: 12
    sica_accuracy: 0.7667
    sc_accuracy: 0.7667
    delta_pp: 0
    multi_candidate_rate: 0.383
    discordant_total: 0
    model: Qwen2.5-14B-Instruct
    dataset: D012
    temperature: 0.5
- exp_id: temperature-ablation-t10
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    n: 60
    k: 12
    sica_accuracy: 0.75
    sc_accuracy: 0.75
    delta_pp: 0
    multi_candidate_rate: 0.433
    discordant_total: 0
    model: Qwen2.5-14B-Instruct
    dataset: D012
    temperature: 1
- exp_id: exp-021-oracle-folio
  name: ''
  status: DONE
  conclusion: success
  metrics:
    n: 204
    k: 12
    oracle_sica_accuracy: 0.8824
    sc_accuracy: 0.7941
    sica_self_accuracy: 0.7941
    oracle_vs_sc_delta_pp: 8.82
    oracle_vs_sica_delta_pp: 8.82
    mcnemar_p_oracle_vs_sc: 6.15e-05
    z3_gold_agreement: 0.946
    fol_parse_success: 1
    model: Qwen2.5-14B-Instruct
    dataset: FOLIO-204
    constraint_source: gold FOL annotations
- exp_id: exp-012-gsm8k-pilot
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    n: 30
    k: 12
    sica_accuracy: 0.9667
    sc_accuracy: 0.9667
    delta_pp: 0
    multi_candidate_rate: 0.133
    extraction_success_rate: 0.147
    model: Qwen2.5-14B-Instruct
    dataset: GSM8K
    temperature: 0.7
- exp_id: exp-004-qwen7b
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    n: 60
    k: 12
    sica_accuracy: 0.6833
    sc_accuracy: 0.6833
    delta_pp: 0
    multi_candidate_rate: 0.433
    extraction_rate: 0.9417
    answer_extraction_rate: 1
    contradiction_rate: 0.0274
    discordant_sica_wins: 2
    discordant_sc_wins: 2
    mcnemar_p: 1
    wall_time_s: 1838
    truncated_traces: 0
    model: Qwen2.5-7B-Instruct
    dataset: D012
    temperature: 0.7
    folio_sica: 0.7667
    folio_sc: 0.7333
    folio_n: 30
    proofwriter_sica: 0.6
    proofwriter_sc: 0.6333
    proofwriter_n: 30
- exp_id: temperature-ablation-t07
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    n: 60
    k: 12
    sica_accuracy: 0.7167
    sc_accuracy: 0.75
    delta_pp: -3.33
    multi_candidate_rate: 0.4
    extraction_rate: 0.9208
    answer_extraction_rate: 1
    contradiction_rate: 0.022
    discordant_sica_wins: 0
    discordant_sc_wins: 2
    truncated_traces: 0
    model: Qwen2.5-14B-Instruct
    dataset: D012
    temperature: 0.7
    proofwriter_sica: 0.6333
    proofwriter_sc: 0.7
    proofwriter_n: 30
    folio_sica: 0.8
    folio_sc: 0.8
    folio_n: 30
    wall_time_s: 3498.3
- exp_id: exp-022-oracle-proofwriter
  name: ''
  status: DONE
  conclusion: success
  metrics:
    n: 600
    k: 12
    oracle_sica_accuracy: 0.8667
    sc_accuracy: 0.7517
    sica_self_accuracy: 0.755
    oracle_vs_sc_delta_pp: 11.5
    mcnemar_p_oracle_vs_sc: 9.21e-15
    z3_gold_agreement: 0.9714
    z3_gold_agree_n: 577
    z3_gold_total: 594
    parse_errors: 6
    parse_error_rate: 0.01
    solver_errors: 0
    solver_total: 7128
    relneg_oracle: 0.7786
    relneg_sc: 0.6
    relneg_delta_pp: 17.86
    relnoneg_oracle: 0.7945
    relnoneg_sc: 0.6644
    relnoneg_delta_pp: 13.01
    attnoneg_oracle: 0.961
    attnoneg_sc: 0.8701
    attnoneg_delta_pp: 9.09
    attneg_oracle: 0.9188
    attneg_sc: 0.85
    attneg_delta_pp: 6.87
    model: Qwen2.5-14B-Instruct
    dataset: ProofWriter-OWA-D5-600
    constraint_source: gold DSL (raw_logic_programs)
- exp_id: exp-023-discriminative-rate
  name: ''
  status: DONE
  conclusion: success
  metrics:
    n_total: 804
    n_multi_candidate: 307
    source_disc_rate_weight: 0.392
    source_disc_rate_weight_ci95:
    - 0.387
    - 0.398
    source_disc_rate_count_est: 0.121
    source_disc_rate_count_ci95:
    - 0.12
    - 0.123
    z3_semantic_disc_rate: 0.082
    z3_semantic_disc_ci95:
    - 0.076
    - 0.088
    problems_with_disc: 289
    problems_with_disc_rate: 0.941
    pw_source_disc_weight: 0.364
    folio_source_disc_weight: 0.54
    pw_n_multi: 235
    folio_n_multi: 72
    pilot_rate_reported_count: 0.115
    pilot_rate_reported_weight: 0.372
    pilot_validation_weight: 0.376
    pilot_delta_pp: 0.38
    z3_answer_assertions: 642
    z3_total_unique_constraints: 7844
    model: Qwen2.5-14B-Instruct
    dataset: FOLIO+ProofWriter-804
- exp_id: exp-026-folio204-trace-regen
  name: ''
  status: DONE
  conclusion: success
  metrics:
    n: 204
    k: 12
    sica_accuracy: 0.7451
    sc_accuracy: 0.75
    delta_pp: -0.49
    extraction_rate: 0.9853
    model: Qwen2.5-14B-Instruct
    dataset: FOLIO-204
    temperature_trace: 0.7
    temperature_extraction: 0.3
    wall_time_h: 2.5
- exp_id: exp-027-qwen3-14b-non-thinking
  name: ''
  status: DONE
  conclusion: success
  metrics:
    n: 204
    k: 12
    sica_accuracy: 0.8431
    sc_accuracy: 0.8382
    delta_pp: 0.49
    extraction_rate: 0.995
    contradiction_rate: 0.0283
    problems_with_contradictions: 69
    total_constraints: 16153
    unique_constraints: 7031
    wall_time_s: 11017
    model: Qwen3-14B
    dataset: FOLIO-204
    mode: non-thinking
- exp_id: exp-028-qwen3-14b-thinking
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: exp-029-contrastive-folio204
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    contrastive_accuracy: 0.7253
    sc_accuracy: 0.7363
    delta_pp: -1.1
    discriminative_rate: 0.0604
    discriminative_count: 11
    n: 182
    recovery_rate_pct: -8.3
    mcnemar_chi2: 0.1
    mcnemar_p: 0.7518
    cont_only_correct: 4
    sc_only_correct: 6
    both_correct: 128
    both_wrong: 44
    supporting_pct: 43.2
    opposing_pct: 56.8
    avg_constraints_per_problem: 24.4
    avg_unique_per_problem: 10.4
    wall_time_min: 47.2
- exp_id: exp-030-crossmodel-mistral-folio204
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    n: 204
    k: 12
    crossmodel_sica_accuracy: 0.75
    sc_accuracy: 0.75
    delta_pp: 0
    discriminative_rate: 0
    recovery_rate: 0
    model_extraction: Mistral-7B-Instruct-v0.3
    model_traces: Qwen2.5-14B-Instruct
    dataset: FOLIO-204
- exp_id: exp-031-oracle-folio-regen
  name: ''
  status: DONE
  conclusion: success
  metrics:
    n: 204
    k: 12
    oracle_sica_accuracy: 0.8971
    sc_accuracy: 0.7549
    sica_self_accuracy: 0.7451
    oracle_vs_sc_delta_pp: 14.22
    oracle_vs_sica_delta_pp: 15.2
    mcnemar_p_oracle_vs_sc: 2.0024e-07
    mcnemar_b_c:
      b_oracle_right_sc_wrong: 29
      c_oracle_wrong_sc_right: 0
    z3_gold_agreement: 0.951
    z3_gold_agree_n: 194
    z3_in_candidates_n: 178
    fol_parse_success: 1
    model: Qwen2.5-14B-Instruct
    dataset: FOLIO-204
    constraint_source: gold FOL annotations
    traces_source: exp-026-folio204-trace-regen
- exp_id: exp-033-qwen3-pw600-nonthinking
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: exp-035
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    n_problems: 203
    sc_accuracy: 77.34
    sica_accuracy: 76.85
    delta_pp: -0.49
    sica_correct: 156
    sc_correct: 157
    mcnemar_discordant_b: 1
    mcnemar_discordant_c: 2
    mcnemar_p_value: 1
    c0_non_unanimous_rate: 0.5517
    extraction_rate: 98.19
    contradiction_rate: 1.58
    problems_with_contradictions: 60
    total_constraints: 12950
    unique_constraints: 6515
    dedup_ratio: 50.3
    wall_time_min: 78.2
    avg_per_problem_s: 23.1
- exp_id: exp-034
  name: ''
  status: DEPLOYED
  conclusion: failed
  metrics:
    n_problems: 93
    n_target: 600
    completion_pct: 15.5
    sica_accuracy: 77.42
    sc_accuracy: 74.19
    delta_pp: 3.23
    sica_correct: 72
    sc_correct: 69
    mcnemar_discordant_b: 6
    mcnemar_discordant_c: 3
    mcnemar_p_value: 0.5078
    c0_non_unanimous_rate: 0.581
    avg_majority_frac: 0.8324
    extraction_rate: 99.19
    contradiction_rate: 11.83
    problems_with_contradictions: 11
    avg_unique_constraints: 35.6
    total_constraints: 14437
    unique_constraints: 3308
    dedup_ratio: 22.9
    k: 12
    level: OWA-D5
    gt_distribution:
      'True': 32
      'False': 28
      Unknown: 33
    wall_time_s: 6086.4
    status_note: 'INCOMPLETE: crashed at 93/600 (python not found after conda env
      lost)'
- exp_id: exp-007-qwen72b-awq
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: exp-004-qwen7b-rerun
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: exp-036-z3-feedback-folio204
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    z3fb_sica_accuracy: 0.775
    vanilla_sica_accuracy: 0.745
    sc_accuracy: 0.75
    z3fb_vs_vanilla_delta: 0.03
    unsat_traces: 22
    total_traces: 2448
    unsat_rate: 0.009
    unsat_resolve_rate: 0.864
    problems_flipped: 0
    real_impact: 0
- exp_id: exp-033
  name: ''
  status: DONE
  conclusion: success
  metrics:
    n_problems: 204
    sica_accuracy: 59.31
    sc_accuracy: 54.41
    delta_pp: 4.9
    sica_correct: 121
    sc_correct: 111
    mcnemar_discordant_b: 12
    mcnemar_discordant_c: 2
    mcnemar_p_value: 0.0129
    c0_non_unanimous_rate: 0.8137
    avg_majority_frac: 0.7515
    extraction_rate: 97.14
    contradiction_rate: 3.5
    problems_with_contradictions: 128
    avg_unique_constraints: 39.3
    maxsat_mean_sat_ratio: 0.9609
    total_constraints: 14042
    unique_constraints: 8021
    wall_time_min: 81.4
    k: 12
- exp_id: exp-039-14b-pw600-16639
  name: ''
  status: RUNNING
  conclusion: ''
  metrics: {}
- exp_id: exp-040-qwen3-pw600-16639
  name: ''
  status: RUNNING
  conclusion: ''
  metrics: {}
- exp_id: exp-041-14b-folio204-16639
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    n: 204
    dataset: FOLIO-204
    model: Qwen2.5-14B-Instruct
    k: 12
    sica_accuracy: 75.49
    sc_accuracy: 77.45
    delta_pp: -1.96
    sica_correct: 154
    sc_correct: 158
    mcnemar_discordant_b: 0
    mcnemar_discordant_c: 4
    mcnemar_p_value: 0.125
    extraction_rate: 0.98
    contradiction_rate: 0.0097
- exp_id: exp-038-14b-logiqa200-16639
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    n: 200
    dataset: LogiQA-200
    model: Qwen2.5-14B-Instruct
    k: 12
    sica_accuracy: 78
    sc_accuracy: 78.5
    delta_pp: -0.5
    mcnemar_p: 1
    sica_correct: 156
    sc_correct: 157
    discordant_b: 1
    discordant_c: 2
    both_correct: 155
    both_wrong: 42
    extraction_rate: 0.864
    fail_empty_rate: 0.122
    avg_unique_constraints: 26.7
    contradiction_rate: 0.008
    wall_time_min: 126.8
- exp_id: exp-042-premise-formalization
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: exp-043-consistency-filtering
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    sc_accuracy: 0.75
    sica_t1_all: 0.7794
    sica_t4: 0.75
    sica_t6: 0.7549
    sica_t8: 0.7549
    avg_unique_constraints: 13.2
    avg_filtered_t4: 1.8
    avg_filtered_t6: 0.8
    avg_filtered_t8: 0.3
- exp_id: exp-044-icl-oracle
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: exp-045-backward-verification
  name: ''
  status: DONE
  conclusion: negative
  metrics: {}
- exp_id: exp-036b-cross-trace-unsat
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    cross_unsat_rate_pair: 0.087
    cross_unsat_rate_problem: 0.107
    within_trace_unsat_rate: 0.009
    unsat_pairs: 11
    total_pairs: 126
    problems_with_unsat: 9
    multi_answer_problems: 84
    single_answer_skip: 120
    zero_shared_var_pairs_pct: 0.564
    avg_shared_vars: 2.7
    false_true_unsat_rate: 0.467
    sica_cross_ut_accuracy: 0.745
    sc_accuracy: 0.75
    accuracy_impact: 0
- exp_id: exp-042b-premise-formal
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: exp-044b-icl-oracle
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    n: 199
    dataset: FOLIO-199
    model: Qwen2.5-14B-Instruct
    k: 12
    sica_accuracy: 74.87
    sc_accuracy: 74.37
    delta_pp: 0.5
    sica_correct: 149
    sc_correct: 148
    icl_examples: 5
    extraction_failure_rate: 0.008
- exp_id: exp-045b-backward-verify
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: exp-046-mistral-pw600
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    n: 600
    sc_accuracy: 39.33
    sica_accuracy: 36.5
    delta_pp: -2.83
    sc_wins: 30
    sica_wins: 13
    mcnemar_p: 0.0095
    significant: true
    dataset: ProofWriter-D5-600
    model: Mistral-7B-Instruct-v0.3
- exp_id: exp-028b-qwen3-thinking-folio204
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: exp-048-llama8b-pw600
  name: ''
  status: RUNNING
  conclusion: ''
  metrics: {}
- exp_id: exp-049-mistral-logiqa200
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: exp-050-mistral-icl-oracle-folio199
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: exp-050b-mistral-icl-oracle
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    n: 199
    sc_accuracy: 57.79
    sica_accuracy: 54.27
    delta_pp: -3.52
    sc_correct: 115
    sica_correct: 108
    discordant_b: 6
    discordant_c: 13
    mcnemar_p: 0.167
    significant: false
    wall_time_min: 93.8
    extraction_success: 2333
    extraction_fail: 55
    per_answer:
      'True':
        n: 70
        sica_acc: 50
        sc_acc: 54.29
      'False':
        n: 61
        sica_acc: 36.07
        sc_acc: 44.26
      Unknown:
        n: 68
        sica_acc: 75
        sc_acc: 73.53
- exp_id: exp-049b-mistral-logiqa200
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    n: 200
    sc_accuracy: 51
    sica_accuracy: 51.5
    delta_pp: 0.5
    sc_correct: 102
    sica_correct: 103
    discordant_b: 6
    discordant_c: 5
    mcnemar_p: 1
    significant: false
    wall_time_min: 78.6
    extraction_rate: 0.9725
    total_constraints: 10659
    unique_constraints: 8934
    contradiction_rate: 0.0196
- exp_id: exp-051-mistral-k-sensitivity
  name: ''
  status: RUNNING
  conclusion: ''
  metrics: {}
- exp_id: exp-052-mistral-folio204-seed123
  name: ''
  status: QUEUED
  conclusion: ''
  metrics: {}
- exp_id: exp-053-mistral-folio204-seed456
  name: ''
  status: QUEUED
  conclusion: ''
  metrics: {}
- exp_id: exp-052
  name: ''
  status: DONE
  conclusion: success
  metrics:
    n: 204
    sc_accuracy: 53.9
    sica_accuracy: 57.4
    sc_correct: 110
    sica_correct: 117
    delta_pp: 3.43
    discordant_b: 8
    discordant_c: 1
    extraction_rate: 0.971
    contradiction_rate: 0.034
    wall_time_min: 81.9
    mcnemar_p: 0.0391
    significant: true
- exp_id: exp-053
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    n: 204
    sc_accuracy: 56.37
    sica_accuracy: 55.88
    sc_correct: 115
    sica_correct: 114
    delta_pp: -0.49
    discordant_b: 2
    discordant_c: 3
    extraction_rate: 0.97
    contradiction_rate: 0.033
    wall_time_min: 80.8
    mcnemar_p: 1.0
    significant: false
- exp_id: exp-054-mistral-folio204-t10
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    n: 204
    sc_accuracy: 54.9
    sica_accuracy: 55.4
    delta_pp: 0.49
    discordant_b: 5
    discordant_c: 4
    mcnemar_chi2: 0.1111
    mcnemar_p: 0.7389
    extraction_rate: 97.3
    contradiction_rate: 3
    wall_time_min: 83
- exp_id: exp-055-multitemp-mistral-folio
  name: ''
  status: RUNNING
  conclusion: ''
  metrics: {}
- exp_id: exp-057-mistral-folio204-t03
  name: ''
  status: RUNNING
  conclusion: ''
  metrics: {}
- exp_id: exp-058-mistral-folio204-t05
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


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "3d1d0d6f-44c9-4cd9-b0a7-76b8477535b6",
  "type": "user",
  "uuid": "aac4681e-9dbd-4e36-9ea1-e7912d210efb",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3",
  "sessionId": "f34ece61-443f-4fad-9714-c7dbf3b3b1b5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-19T04:06:17.242Z_

```json
{
  "parentUuid": "aac4681e-9dbd-4e36-9ea1-e7912d210efb",
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
  "uuid": "f4a07e9d-dd24-4585-abd4-f39b7c1049f7",
  "timestamp": "2026-05-19T04:06:17.242Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3",
  "sessionId": "f34ece61-443f-4fad-9714-c7dbf3b3b1b5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-19T04:06:17.242Z_

```json
{
  "parentUuid": "f4a07e9d-dd24-4585-abd4-f39b7c1049f7",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "e067eb24-8d9d-4100-acdd-08e06ab7f7e6",
  "timestamp": "2026-05-19T04:06:17.242Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3",
  "sessionId": "f34ece61-443f-4fad-9714-c7dbf3b3b1b5",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：Eff-K 作为预测器失败，K/T curves 无 clean pattern。核心 Condorcet framing 不 hold。需 reframe 为 comprehensive negative-results / diagnostic 贡献，保留 oracle gap 和 C0 diagnos…",
  "leafUuid": "e067eb24-8d9d-4100-acdd-08e06ab7f7e6",
  "sessionId": "f34ece61-443f-4fad-9714-c7dbf3b3b1b5"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyzing the independence bottleneck in self-extracted symbolic consensus",
  "sessionId": "f34ece61-443f-4fad-9714-c7dbf3b3b1b5"
}
```

---

### Assistant

_source line 8 · 2026-05-19T04:07:31.208Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed imagined/predicted data for each planned experiment in the experiment_plan, under the "worst" tier scenario. Let me carefully go through each experiment that has status "planned" or is still running/queued, and generate worst-case predictions with rationales.

Let me identify the experiments that need predictions. Looking at the experiment_plan and registry:

From experiment_plan (status: planned):
- exp-002: sica_k_ablation_14b (K sensitivity on D012 60 questions) - but registry has sica_k_sensitivity_14b DONE


- exp-003: tiebreak_baseline_analysis - noted as completed, artifact exists
- exp-004: sica_7b_scaling - registry has exp-004-qwen7b DONE
- exp-005: qwq_32b_operating_regime - registry has exp-005 DONE
- exp-006: c0_diagnostic_validation
- exp-007: sica_72b_awq - registry has exp-007-qwen72b-awq DONE (failed)
- exp-008: constraint_quality_case_studies
- exp-009: overhead_analysis - registry has exp-009-overhead-analysis DONE
- exp-010: sica_mistral_7b - still need to check status
- exp-011: sica_llama_8b - registry has exp-011-llama8b-v3 DONE
- exp-012: gsm8k_pilot_14b - registry has exp-012-gsm8k-pilot DONE
- exp-013: constraint_ablation - registry has sica_constraint_ablation_013 DONE
- exp-014: sica_deepseek_r1_llama_8b - registry has exp-014-deepseek-r1-7b DONE
- exp-015: logic_lm_baseline - need to verify
- exp-016: weighted_sc_baseline - registry has exp-016-weighted-sc DONE
- exp-017: sica_strategyqa_14b - registry has exp-017-strategyqa-v3 DONE
- exp-018: sica_arc_challenge_14b - registry has exp-018-arc-v, checking completion status
- exp-019: constraint_quality_correlation - DONE

I'm also seeing several experiments currently running in the registry. The user is asking me to expand on the planned experiments from the experiment_plan, so I need to focus on those that are still marked as planned rather than the ones already running or completed.

Looking through the experiment_plan, I'm noticing a discrepancy between what's marked as planned there and what the registry actually shows. Many experiments listed as planned in the plan have already been completed or failed in the registry - like exp-004, exp-005, exp-009 through exp-014 all show as DONE, while exp-007 shows as failed. A few are genuinely still in planned status like exp-002, exp-006, exp-008, and exp-015.

There are also some experiments running that aren't in the plan at all - exp-051 through exp-058 - which seem to be variations on sensitivity and temperature testing for different models.

I think what the user is asking for is worst-case predicted data for all the planned experiments in the plan, regardless of whether they've already been executed or not. So I need to generate predictions for both the ones that are actually done and the ones still pending. though actual data exists) and the ones truly pending.

Actually wait - re-reading the prompt: "基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。" This means for each experiment in the plan that has status "planned", generate detailed predicted data under the worst tier.

But many of these already have actual results in the registry. The user seems to want imagined/predicted results for all planned experiments under the worst scenario, regardless of whether some already completed. This is for paper planning purposes.

Actually, I think the intent is: the user defined the "worst" tier with specific ranges and narrative. They want me to generate concrete predicted numbers for ALL experiments in the plan, imagining what the worst-tier outcome would look like. This is a scenario planning exercise.

So I need to go through the planned experiments and generate worst-case predicted data for each one. Looking at the experiment plan, there are quite a few marked as planned - the K ablation, tiebreak baseline, Qwen scaling studies, QwQ operating regime, diagnostic validation, various model evaluations across different benchmarks, and ablation studies. I should also consider the running experiments that are critical to include in this worst-case scenario. -tier narrative:
- exp-051: Mistral K sensitivity
- exp-055: multi-temp
- exp-057: T=0.3
- exp-058: T=0.5

Let me focus on just the "planned" experiments from the registry, not the completed ones. For the worst-case tier, I need to define what would undermine each key claim: no inverted-U pattern for K sensitivity with K=12 failing to peak, temperature effects showing no clean optimum where T=0.3 performs comparably to T=0.7, multi-temperature results unexpectedly positive which would contradict the diversity narrative, and Mistral's internal efficiency-K relationship showing no correlation with the cross-model pattern. I'm also considering how 2 out of 3 seeds showing significance could be framed as cherry-picking. Now I'm looking at the expected metric ranges for these failure scenarios—K peak deltas between 1-5pp, K4 and K20 deltas spanning -5 to +5pp with no discernible inverted-U pattern, temperature deltas of 2-6pp at T=0.3 and 1-5pp at T=0.5, and multi-temp improvements of 1-4pp. I'm getting caught up in the details here. Let me step back and just generate worst-tier predictions for each planned experiment with concrete numbers and clear rationales, organized in YAML format. For the running experiments that are critical to the worst-tier definition, I should include those too even if they're not explicitly listed in the plan. I'll work through each one systematically—starting with the already-completed experiments like the K ablation and tiebreak baseline, then moving to the planned ones, assigning realistic worst-case values within the specified ranges. Looking at the remaining experiments, most show SICA providing no meaningful advantage over standard self-consistency across different models and datasets—GSM8K confirms this pattern with very low C0 scores. The constraint aggregation methods appear largely equivalent to simple counting, Logic-LM already achieves similar performance, and weighted variants don't improve results. Even on datasets where model capability is high, like StrategyQA, SICA still collapses to standard self-consistency, suggesting a fundamental capability trap. The correlation between constraint quality and performance remains too noisy to establish a reliable signal, and sensitivity analysis shows no clear optimization pattern.

Now I'm reconsidering which experiments to include in the full writeup—the plan specifies only those marked as "planned" in the registry, but the most critical findings actually come from the running experiments that revealed these core limitations, so I should incorporate both to give the complete picture. I'm looking at the remaining performance metrics for the worst-tier definition—T=0.5 gives modest gains of 1-5pp, multi-temperature shows 1-4pp improvement, and the effective K joint prediction only gets 6 out of 12 conditions right. Now I need to decide whether to use actual registry data for completed experiments or predict worst-case scenarios, since the user wants detailed data for the planned experiments and many of these have already run.

I'll go with worst-case predictions across the board so there's a clear baseline to compare against actual results later. Let me structure each experiment with name, plan ID, description, expected metrics, rationale, tables, figures, and analysis, then work through the full list of planned and critical running experiments.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e067eb24-8d9d-4100-acdd-08e06ab7f7e6",
  "isSidechain": false,
  "requestId": "req_011CbBGTp8fuCDnWu3N6k7ob",
  "type": "assistant",
  "uuid": "f51f0cc8-68dc-4815-822b-8aa766506b59",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3",
  "sessionId": "f34ece61-443f-4fad-9714-c7dbf3b3b1b5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FDGXEoQc91krEvoUH82Kcm",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 29067,
      "cache_read_input_tokens": 11841,
      "output_tokens": 14352,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 29067,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 14352,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 29067,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 29067
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

_source line 9 · 2026-05-19T04:11:03.434Z_

```yaml
tier: worst
narrative_guidance: >
  放弃 Condorcet predictive framework 作为核心 claim。Reframe 为 "Comprehensive Diagnostic Study of Symbolic Consensus Aggregation"。
  Eff-K 跨模型方向虽对但模型内无预测力，K/T curves 全是 noise，multi-temp 意外 positive 动摇 diversity 叙事。
  三条腿支撑投 Findings：(1) Oracle gap hard result; (2) 9 种修复 breadth; (3) C0+SC diagnostic。
  Title 改为 "When Do Self-Extracted Symbolic Constraints Help LLM Reasoning? A Diagnostic Study"。
  估计 reviewer avg 2.5–3.0。

imagined_experiments:
  # ── experiment_plan 中 status=planned 的实验 ──

  - name: "sica_k_ablation_14b"
    plan_id: "exp-002"
    description: "K=6/8/11/12/16/20 sensitivity on D012 60q, Qwen2.5-14B"
    expected_results:
      K6_delta_pp: 0.0
      K8_delta_pp: -1.7
      K11_delta_pp: 0.0
      K12_delta_pp: -5.0
      K16_delta_pp: -3.3
      K20_delta_pp: -3.3
      inverted_u_visual: "无——SICA 在所有 K 均 ≤ SC，随 K 增大单调恶化"
      K11_odd_k_gap: 0.0
    result_rationale: >
      Qwen-14B SC≈75% (Type A regime)，confirmation bias 主导。K 增大只增加冗余 correlated constraints，
      不增加独立信息。Eff-K≈1.3 意味着 K=6 和 K=20 的 effective voters 几乎相同（~1.3）。
      无 inverted-U 因为 14B 在此 regime 下 SICA 本身就没有正向效应，K 的变化只引入更多 noise。
      K=11 odd-K 消除 tiebreak 后 gap=0 进一步确认 14B 效应完全是 tiebreak artifact。
    tables: ["T5 (partial): K sensitivity — 仅 14B 列"]
    figures_description: ["F3 14B subplot: flat/declining line，无 peak"]
    analysis: >
      14B K ablation 在 worst tier 下完全符合 Type A 预期——SC 太高时 SICA 无论 K 取何值都无法超越。
      这本身不是 worst tier 的关键问题（实际已完成数据也如此），关键是 Mistral K ablation (exp-051)
      也无 clean pattern 时，整个 K sensitivity 叙事崩塌。

  - name: "tiebreak_baseline_analysis"
    plan_id: "exp-003"
    description: "SICA vs SC-random-tiebreak vs SC-deterministic, CPU-only"
    expected_results:
      sica_tiebreak_accuracy_pct: 80.0
      random_tiebreak_accuracy_pct: 50.0
      alphabetical_tiebreak_accuracy_pct: 60.0
      first_seen_tiebreak_accuracy_pct: 40.0
      n_tiebreak_problems: 5
    result_rationale: >
      Tiebreak 分析在 worst tier 下结果不变（已完成的 CPU 分析）。问题在于 n=5 tiebreak cases 太少，
      reviewer 会质疑 80% (4/5) 的 statistical power。且 SICA 的 tiebreak 优势仅在极少数问题上体现，
      不构成 compelling evidence。在 worst tier 下 reviewer 将此视为 anecdotal。
    tables: []
    figures_description: []
    analysis: >
      Tiebreak 80% 看似有意义但 n=5 完全无 statistical significance。
      Worst tier 下 reviewer 直接忽略此 result ("interesting but underpowered")。

  - name: "sica_7b_scaling"
    plan_id: "exp-004"
    description: "Qwen2.5-7B on D012 60q, test C0-as-predictor"
    expected_results:
      sica_accuracy: 0.683
      sc_accuracy: 0.683
      delta_pp: 0.0
      multi_candidate_rate: 0.433
      mcnemar_p: 1.0
      discordant_sica_wins: 2
      discordant_sc_wins: 2
    result_rationale: >
      7B SC≈68% 仍在 Type A regime 上沿（C0=43% 比 14B 高但仍不够）。
      Qwen 家族内 Eff-K 普遍 ≈1.2-1.3，7B 的 lower capability 提高 C0 但不提高 constraint quality。
      Constraints 仍然 mirror 模型偏差。Delta=0 确认 Qwen 家族 SICA 无效。
      Worst case: 与 14B 结果一致，无法单独贡献 regime boundary 叙事。
    tables: ["T1: Qwen-7B 行"]
    figures_description: ["F2: Qwen-7B 数据点落在 SC≈68% 区域，delta=0"]
    analysis: >
      Qwen-7B 支持跨模型 Eff-K 叙事（Qwen 家族 Eff-K 低→0 gain）但在 worst tier 下
      reviewer 认为这只是"同家族 same behavior"，不算独立 evidence。

  - name: "qwq_32b_operating_regime"
    plan_id: "exp-005"
    description: "QwQ-32B negative control, data from MVP phase"
    expected_results:
      aggregate_c0_effective_pct: 2.6
      aime_delta_pp: 0.0
      proofwriter_delta_pp: -5.9
      total_problems: 46
      c0_below_threshold: true
    result_rationale: >
      Reasoning model 的 deterministic chain 产生近乎相同 traces (C0 effective≈2.6%)。
      SICA≡SC 是必然——无 multi-candidate problems，MAX-SAT 无从发挥。
      PW delta=-5.9pp 因 n=17 不 significant 但方向 negative。
      Worst case: reviewer 认为 QwQ 是 trivially expected negative control，不算 contribution。
    tables: ["T1: QwQ-32B 行", "Appendix: QwQ negative control detail"]
    figures_description: ["F2: QwQ 数据点在 extreme right (high SC, C0≈0)"]
    analysis: >
      QwQ-32B C0<5% 是最 clean 的 negative result，但 worst tier 下 reviewer 视为 obvious——
      "当然 reasoning model 不需要 SICA"。价值被低估。

  - name: "c0_diagnostic_validation"
    plan_id: "exp-006"
    description: "C0 vs SICA-SC gap scatter across all models/K values"
    expected_results:
      conditions_plotted: 12
      c0_delta_correlation_r: 0.31
      c0_delta_correlation_p: 0.33
      correctly_predicted_direction: 5
      total_conditions: 12
      prediction_accuracy_pct: 41.7
    result_rationale: >
      Worst tier 核心假设: Eff-K+SC joint prediction ≤6/12 conditions 方向正确。
      C0 单独作为 predictor 更差——Mistral PW-600 (C0 high, delta negative) 和 
      LLaMA-8B FOLIO (C0 high, delta negative) 都是反例。
      Scatter plot 呈现 no clean trend，high C0 对应 both positive 和 negative deltas。
      Correlation r≈0.31 不 significant (p>0.3, n=12)。
    tables: []
    figures_description:
      - "F2 (scatter): C0 vs delta, 12 data points scattered without trend. Mistral-FOLIO s42 (+4.9pp) 和 LLaMA-D012 (+6.67pp) 是 outlier positive points，但 Mistral-PW (-2.83pp) 和 LLaMA-FOLIO-204 (-2.45pp) 在同样 high C0 区域为 negative。No regression line plotted because r n.s."
    analysis: >
      C0 diagnostic 在 worst tier 下失去 predictive power。只能做 necessary condition (C0<5% → SICA≡SC)
      但 sufficient condition 不成立。Reviewer 会说 "C0 just tells you there's variance, not that SICA helps"。
      降级为 "deployment screening tool" (排除 SICA 必然无用的 cases) 而非 "predictor"。

  - name: "sica_72b_awq"
    plan_id: "exp-007"
    description: "Qwen2.5-72B-AWQ 4-bit on D012 60q"
    expected_results:
      sica_accuracy: 0.817
      sc_accuracy: 0.833
      delta_pp: -1.67
      multi_candidate_rate: 0.20
      mcnemar_p: 0.625
      extraction_rate: 0.95
    result_rationale: >
      72B SC≈83% (deep Type A regime)。C0 进一步降至 ~20% 因为更大模型更 unanimous。
      SICA 因 confirmation bias 甚至略 negative——constraints 强化已有高置信度答案，
      少数 override 方向是错的。Qwen 家族 pattern 延续: 更大模型→更高 SC→更低 C0→更无用 SICA。
    tables: ["T1: Qwen-72B 行"]
    figures_description: ["F2: Qwen-72B 在 scatter 最右上方 (SC=83%, delta≈-1.7pp)"]
    analysis: >
      72B 进一步确认 Type A regime。但 worst tier 下 reviewer 说 "you're just showing that
      SICA doesn't help strong models — this is obvious"。缺乏新 insight。

  - name: "constraint_quality_case_studies"
    plan_id: "exp-008"
    description: "5-10 representative questions 的 constraint 质量定性分析"
    expected_results:
      cases_analyzed: 8
      trivially_satisfied_pct: 45
      confirmation_bias_cases: 6
      genuinely_informative_constraints: 1
      constraint_mirrors_model_answer_pct: 78
    result_rationale: >
      定性分析在 worst tier 下揭示 constraints 几乎完全 mirror 模型的 chain-of-thought 结论。
      Even "discriminative" constraints 的 discriminative direction 与模型偏差一致。
      唯一 genuinely informative case 是模型恰好 extract 了 premise 中的 explicit logical structure。
      但 reviewer 可能认为 case studies 是 cherry-picked。
    tables: []
    figures_description: ["F4 (stacked bar): constraint error breakdown — trivially_satisfied (45%), confirmation_bias (33%), genuinely_informative (12%), parse_error (10%)"]
    analysis: >
      Case studies 支持 confirmation bias 叙事但在 worst tier 下 reviewer 认为
      n=8 qualitative analysis 不算 rigorous evidence。"Show me this at scale" → 需要 exp-019 的 correlation，
      但 exp-019 也 noisy。

  - name: "overhead_analysis"
    plan_id: "exp-009"
    description: "Wall-time breakdown per question"
    expected_results:
      mean_total_wall_s: 61.6
      trace_gen_pct: 51.3
      extraction_pct: 47.0
      maxsat_pct: 0.005
      sica_overhead_pct: 48.7
    result_rationale: >
      SICA 几乎 doubles wall time (49% overhead) 但 delta≈0 across most conditions。
      Worst tier 下 cost-benefit 极差: 2× compute for 0 gain in majority of conditions,
      fragile +4.9pp in one specific setting (Mistral/FOLIO/T=0.7/K=12/s42)。
      Reviewer: "this is not practical"。
    tables: ["Appendix: overhead breakdown table"]
    figures_description: []
    analysis: >
      Overhead analysis 在 worst tier 下变成 anti-argument: "你花了 2× compute 得到了 noise"。
      但可以 reframe 为 "extraction is the bottleneck, not solving" (MAX-SAT <0.01% time)，
      说明未来研究应聚焦 extraction quality 而非 solver improvements。

  - name: "sica_llama_8b"
    plan_id: "exp-011"
    description: "LLaMA-3.1-8B on D012 60q"
    expected_results:
      sica_accuracy: 0.667
      sc_accuracy: 0.600
      delta_pp: 6.67
      multi_candidate_rate: 0.617
      mcnemar_p: 0.219
      truncated_traces: 44
      answer_extraction_rate: 0.896
    result_rationale: >
      LLaMA-8B delta=+6.67pp 看似 positive 但 p=0.219 (n=60) 完全 n.s.。
      且 truncated_traces=44 和 answer_extraction_rate=89.6% 说明 pipeline 对 LLaMA 有 artifacts。
      Worst tier 下 reviewer 质疑: (1) n.s. result; (2) 44 truncated traces 是否 confound;
      (3) answer extraction 失败的 traces 是否 systematically biased。
      扩展到 FOLIO-204 (exp-020) 后 delta 反转为 -2.45pp → D012 的 +6.67pp 是 small-n artifact。
    tables: ["T1: LLaMA-8B 行"]
    figures_description: ["F2: LLaMA-8B D012 (+6.67pp) 和 FOLIO-204 (-2.45pp) 两点展示 instability"]
    analysis: >
      LLaMA-8B 是 worst tier 的典型 case: small-n positive 被 larger-n 反转。
      Reviewer 会直接引用 FOLIO-204 result dismiss D012 result。
      Combined evidence: SICA on LLaMA 是 noise。

  - name: "gsm8k_pilot_14b"
    plan_id: "exp-012"
    description: "Qwen2.5-14B on GSM8K 30q pilot"
    expected_results:
      sica_accuracy: 0.967
      sc_accuracy: 0.967
      delta_pp: 0.0
      multi_candidate_rate: 0.133
      extraction_success_rate: 0.147
    result_rationale: >
      14B 在 GSM8K 准确率极高 (97%)，C0=13.3% 低于 threshold。
      更关键的是 FOL extraction 几乎完全失败 (success=14.7%) — math domain 的 constraints
      需要 numerical reasoning 而非 propositional logic，SICA pipeline 在此 domain 根本不适用。
      这不是 SICA 的 negative evidence 而是 domain mismatch。
    tables: ["T1: GSM8K 行 (footnote: extraction failure)"]
    figures_description: []
    analysis: >
      GSM8K 在 worst tier 下是 domain 不匹配的 obvious failure。Reviewer 不会 penalize 但也不加分。
      Reframe 为 Type B (domain not formalizable as FOL) 的 additional evidence。

  - name: "constraint_ablation"
    plan_id: "exp-013"
    description: "MaxSAT vs count-only vs random-weight, CPU-only on exp-001 data"
    expected_results:
      maxsat_accuracy: 0.765
      count_only_accuracy: 0.766
      random_weight_accuracy: 0.759
      sc_baseline_accuracy: 0.762
      agreement_maxsat_vs_countonly: "803/804"
      mcnemar_p_all_gt_05: true
    result_rationale: >
      MaxSAT 和 count-only 在 804 题中仅 1 题不同。这证明 MAX-SAT solver 几乎无贡献——
      简单 count constraints per answer 就等价。原因: constraints 的 satisfiability weights 
      几乎不区分 answers (mean_sat_ratio≈0.96，接近 1.0)。
      Worst tier 下 reviewer: "所以 SAT solver 是 over-engineering，constraint counting 就够了——
      但 counting 本身也不 work (delta≈0)"。双重打击。
    tables: ["Appendix: constraint ablation comparison"]
    figures_description: []
    analysis: >
      MaxSAT≈count-only 在 worst tier 下是 devastating: 论文的 "symbolic" 框架核心价值被掏空。
      但可 reframe 为 evidence: "even the most powerful aggregation mechanism cannot help 
      when constraints are non-independent"。即 solver 能力不是瓶颈，constraint quality/independence 才是。

  - name: "sica_deepseek_r1_llama_8b"
    plan_id: "exp-014"
    description: "DeepSeek-R1-Distill-Qwen-7B on D012 60q"
    expected_results:
      sica_accuracy: 0.683
      sc_accuracy: 0.717
      delta_pp: -3.33
      multi_candidate_rate: 0.583
      truncated_traces: 72
      mcnemar_p: 0.480
    result_rationale: >
      Reasoning model distillation 产生 longer traces (72 truncated) 但 reasoning quality 
      不 translate to better constraints。High C0 (58.3%) 但 delta negative — 
      与 Mistral-PW600 类似的 pattern (high diversity + low quality = negative)。
      Truncation 是额外 confound: 被截断的 traces 产生 incomplete constraints。
    tables: ["T1: DeepSeek-R1 行"]
    figures_description: ["F2: DeepSeek-R1 data point at SC≈72%, delta=-3.3pp"]
    analysis: >
      DeepSeek-R1 delta=-3.33pp 在 worst tier 下补充了 exp-046 (Mistral-PW) 的 evidence:
      high C0 但 low constraint quality → negative delta。但 reviewer 可能归咎于 truncation artifact 而非 fundamental。

  - name: "logic_lm_baseline"
    plan_id: "exp-015"
    description: "Logic-LM × K + majority vote on FOLIO, CPU-only"
    expected_results:
      logic_lm_k_vote_accuracy: 0.755
      sica_accuracy: 0.745
      sc_accuracy: 0.750
      logic_lm_vs_sc_delta_pp: 0.5
      logic_lm_vs_sica_delta_pp: 1.0
    result_rationale: >
      Logic-LM 单 trace FOL verification × K 然后 vote 的精度 ≈ SC ≈ SICA。
      原因: 单 trace FOL 质量和多 trace aggregated FOL 质量差不多——因为 traces 高度相关，
      多 trace 不增加新 constraint information。
      Worst tier: reviewer 说 "Logic-LM × K 就和 SICA 一样好，那 MAX-SAT aggregation 的意义是什么？"
    tables: ["Appendix: Logic-LM comparison"]
    figures_description: []
    analysis: >
      Logic-LM baseline 在 worst tier 下进一步削弱 MAX-SAT aggregation 的 novelty。
      但可以 reframe: "即使 Logic-LM style 的 approach 也不超过 SC，
      问题在 extraction 而非 aggregation strategy"——与 oracle gap 叙事一致。

  - name: "weighted_sc_baseline"
    plan_id: "exp-016"
    description: "Weighted SC (length/logprob/constraint-count) on exp-001 data"
    expected_results:
      sc_uniform_accuracy: 0.762
      inv_length_accuracy: 0.767
      length_weighted_accuracy: 0.753
      constraint_count_accuracy: 0.753
      all_nonsignificant: true
      inv_length_vs_sc_p: 0.453
    result_rationale: >
      所有 weighting schemes 与 uniform SC 无 significant 差异。
      Inv-length 略好 (+0.5pp) 但完全 n.s.。Constraint-count weighting 和 length-weighting 
      甚至略 worse。原因: weighting 不解决 independence 问题——如果 votes 本身高度相关，
      re-weighting 相关 votes 不改变结果。
    tables: ["Appendix: weighted SC comparison"]
    figures_description: []
    analysis: >
      Weighted SC 无效在 worst tier 下实际是 neutral-to-positive: 证明 simple weighting 
      也不能 beat SC，strengthens "independence is the bottleneck not aggregation strategy"。
      但 reviewer 可能说 "you should try more sophisticated weighting (e.g., diversity-weighted)"。

  - name: "sica_strategyqa_14b"
    plan_id: "exp-017"
    description: "Qwen2.5-14B on StrategyQA 60q"
    expected_results:
      sica_accuracy: 0.567
      sc_accuracy: 0.533
      delta_pp: 3.33
      multi_candidate_rate: 0.10
      mcnemar_p: "n.s."
      bootstrap_p: 0.135
      extraction_rate_trace: 0.704
    result_rationale: >
      StrategyQA C0=10% 远低于 FOLIO (38%)。Binary format + commonsense domain → 
      大多数问题 SC unanimous。Delta=+3.33pp 来自仅 2 个 discordant problems (n=60)，
      完全 n.s.。Extraction rate 低 (70%) 因为 commonsense reasoning 难以形式化为 FOL。
      Worst tier: reviewer 视为 Type B (domain 不可形式化) 的 additional evidence，
      但 +3.33pp 不是 clean null (creates ambiguity)。
    tables: ["T1: StrategyQA 行"]
    figures_description: ["F2: StrategyQA data point at SC≈53%, delta≈+3pp 但 with wide CI"]
    analysis: >
      StrategyQA 的 positive-but-n.s. delta 在 worst tier 下是 problematic: 
      不够 clean 作为 null result (方向 positive)，又不够 significant 作为 positive result。
      Reviewer 可能要求 larger n 来 resolve ambiguity。

  - name: "sica_arc_challenge_14b"
    plan_id: "exp-018"
    description: "Qwen2.5-14B on ARC-Challenge 60q"
    expected_results:
      sica_accuracy: 0.950
      sc_accuracy: 0.967
      delta_pp: -1.67
      multi_candidate_rate: 0.05
      discordant_sica_wins: 0
      discordant_sc_wins: 1
    result_rationale: >
      14B 在 ARC-Challenge 极强 (SC≈97%)，C0=5% — 几乎所有问题 unanimous。
      SICA 在唯一 discordant problem 上选错 → delta=-1.67pp。
      Deep Type A regime: 模型已经极度 confident 且正确，constraints 无法 add value。
    tables: ["T1: ARC 行"]
    figures_description: ["F2: ARC data point at extreme right (SC=97%, delta=-1.7pp)"]
    analysis: >
      ARC 是 clean Type A negative。Worst tier 下 reviewer 不 surprised 但也不 impressed。
      "Of course SICA doesn't help a 97% baseline" — trivially expected。

  - name: "constraint_quality_correlation"
    plan_id: "exp-019"
    description: "Constraint precision per domain × model, correlate with C0 and delta"
    expected_results:
      conditions_analyzed: 10
      constraint_precision_delta_r: 0.28
      constraint_precision_delta_p: 0.43
      c0_precision_r: -0.15
      c0_precision_p: 0.68
      high_c0_low_quality_conditions: 3
      high_c0_high_quality_conditions: 2
    result_rationale: >
      Worst tier: constraint quality 与 delta 之间无 significant correlation。
      High C0 不 predict low quality (counter to capability trap theory)——
      有 high C0 + high quality 的 conditions (LLaMA D012) 和 high C0 + low quality 的 (Mistral PW600)。
      R≈0.28 (n=10) 完全无 statistical power。
      Capability trap 作为 clean theory 不 hold: 实际 pattern 是 noisy 的 condition-specific interactions。
    tables: []
    figures_description: ["F2 (enhanced): scatter with constraint precision as color/size, no clean separation"]
    analysis: >
      exp-019 在 worst tier 下 kills the clean "inverse C0-quality correlation" story。
      No single metric (C0, Eff-K, constraint precision) predicts SICA effectiveness。
      Must retreat to "SICA effectiveness is determined by a complex interaction of factors 
      that we characterize but cannot predict" — weak for a paper claim。

  # ── Running experiments critical to worst tier definition ──

  - name: "mistral_k_sensitivity"
    plan_id: "exp-051"
    description: "Mistral-7B K=4/8/12/16/20 on FOLIO-204, seed 42"
    expected_results:
      K4_sica_accuracy: 0.534
      K4_sc_accuracy: 0.544
      K4_delta_pp: -0.98
      K8_sica_accuracy: 0.559
      K8_sc_accuracy: 0.539
      K8_delta_pp: 1.96
      K12_sica_accuracy: 0.593
      K12_sc_accuracy: 0.544
      K12_delta_pp: 4.90
      K16_sica_accuracy: 0.554
      K16_sc_accuracy: 0.539
      K16_delta_pp: 1.47
      K20_sica_accuracy: 0.524
      K20_sc_accuracy: 0.549
      K20_delta_pp: -2.45
      inverted_u_visual: "无可辨识 pattern，noise ≫ signal"
      peak_K: 12
      peak_delta_pp: 4.90
      k4_vs_k12_difference_significant: false
    result_rationale: >
      Worst tier 核心假设: K sensitivity 无 inverted-U。K=12 仍然是 peak (因为 exp-033 的 seed 42 
      就是用 K=12) 但 K=8 和 K=16 的 delta 在 noise band 内 random walk。
      K=4 delta≈-1pp, K=8≈+2pp, K=12≈+5pp, K=16≈+1.5pp, K=20≈-2.5pp。
      看 curve: 不是 smooth inverted-U 而是 up-down-up-down noise pattern。
      K=8→K=12 jump (+3pp) 和 K=12→K=16 drop (-3.4pp) 都可能是 random variation at n=204。
      CI bars 大量重叠，无法 reject "all K have same delta" null hypothesis。
      Eff-K 也不 monotonically increase with K (因为 κ 本身随 K 变化)。
    tables: ["T5: K sensitivity — Mistral 列 with CI"]
    figures_description:
      - "F3 main: K vs delta scatter for Mistral, error bars heavily overlapping. No smooth curve. K=12 is highest point but K=8 and K=16 within 1 CI of it."
      - "F3 inset: K vs Eff-K — Eff-K increases slightly with K but not monotonically (K=8 Eff-K could exceed K=12 Eff-K if κ happens to be lower at K=8)"
    analysis: >
      K sensitivity 在 worst tier 下是 paper 的最大损失之一。原本 inverted-U 是 Table 5 / Figure 3 的
      hero result，解释了 "why K=12 is optimal"。现在只能说 "K=12 happened to give the best result 
      in this specific seed, but we cannot distinguish signal from noise"。
      Frame 改为 "high variance across K values demonstrates fragility of the effect"——
      从 clean ablation contribution 降级为 fragility evidence。

  - name: "multitemp_mistral_folio"
    plan_id: "exp-055"
    description: "Multi-temperature (T=0.3/0.7/1.0 混合) Mistral-7B FOLIO-204"
    expected_results:
      sica_accuracy: 0.564
      sc_accuracy: 0.544
      delta_pp: 2.45
      mcnemar_p: 0.18
      trace_diversity_increase_pct: 35
      effk_multitemp: 2.8
      effk_single_t07: 1.85
    result_rationale: >
      Worst tier 核心假设: multi-temp 意外 positive (≥+2pp)。
      Multi-temp 通过混合不同温度 traces 确实增加了 diversity (Eff-K 从 1.85 → 2.8)。
      Delta=+2.45pp 虽然 n.s. (p=0.18) 但方向 positive。
      这动摇 "diversity alone is not sufficient" claim——如果 simple temperature mixing 
      就能 partially recover SICA effectiveness，那 independence bottleneck 不是 "fundamental"。
      Reviewer: "你说 9 种修复全部失败，但 multi-temp 实际上 showed promise？"
      无法再 claim "trap is fundamental" 当 diversity intervention shows positive direction。
    tables: ["T_remediation: multi-temp 行改为 '+2.45pp (n.s.)' 而非 'negative'"]
    figures_description: []
    analysis: >
      Multi-temp positive 是 worst tier 的 second most damaging result (after K sensitivity noise)。
      "9 种修复全部失败" 要改为 "8 种修复失败 + 1 种 promising but underpowered"。
      Reviewer 会问: "为什么不 scale up multi-temp to n=600？" — 如果我们没做，是 obvious gap；
      如果做了且 positive，paper narrative completely changes。
      唯一 defense: argue that +2.45pp n.s. is within noise, and even if real, 
      Eff-K increase from 1.85→2.8 still far below nominal K=12。

  - name: "mistral_folio204_t03"
    plan_id: "exp-057"
    description: "Mistral-7B FOLIO-204 at T=0.3"
    expected_results:
      sica_accuracy: 0.574
      sc_accuracy: 0.534
      delta_pp: 3.92
      mcnemar_p: 0.065
      multi_candidate_rate: 0.55
      effk_t03: 1.45
    result_rationale: >
      Worst tier 核心假设: T=0.3 delta ≥+3pp，与 T=0.7 的 +4.9pp 可比。
      T=0.3 SC 略低于 T=0.7 (53.4% vs 54.4%) 但 delta 仍然 substantial (+3.92pp)。
      这 destroys "narrow temperature window" narrative。原来的故事是 "SICA only works at T=0.7, 
      collapses at T=1.0" → 暗示 very specific sweet spot。
      现在 T=0.3 (+3.92pp), T=0.7 (+4.90pp), T=1.0 (+0.49pp) → SICA 在 low-to-medium T 
      都有效，只是 T=1.0 太 noisy 才 collapse。
      这个 pattern 不是 "fragile" 而是 "works except at high T"——undermines fragility framing。
    tables: ["Appendix T sensitivity table: T=0.3 行"]
    figures_description: ["T sensitivity subplot: T=0.3/0.5/0.7/1.0 curve 不是 sharp peak 而是 plateau that drops at T=1.0"]
    analysis: >
      T=0.3 comparable to T=0.7 是 worst tier 定义的关键指标。
      叙事从 "narrow window of fragile effect" 变成 "moderate robustness across low-medium temperatures, 
      failure only at high T"——这实际上 WEAKENS the pure-negative-results paper framing。
      If SICA works at T=0.3-0.7, it's not a "dead end" but a "limited but reproducible effect"。
      Reviewer: "这看起来不像 pure negative results，更像 modest positive results with caveats"。
      Paper 陷入尴尬中间地带: 不够 positive 做 method paper，不够 negative 做 clean diagnostic paper。

  - name: "mistral_folio204_t05"
    plan_id: "exp-058"
    description: "Mistral-7B FOLIO-204 at T=0.5"
    expected_results:
      sica_accuracy: 0.564
      sc_accuracy: 0.539
      delta_pp: 2.45
      mcnemar_p: 0.23
      multi_candidate_rate: 0.62
      effk_t05: 1.65
    result_rationale: >
      T=0.5 delta=+2.45pp 进一步填充 T sensitivity curve。
      Pattern: T=0.3 (+3.92pp) > T=0.5 (+2.45pp) < T=0.7 (+4.90pp) > T=1.0 (+0.49pp)。
      不是 monotonic decline 也不是 clean peak——是 noisy 的 non-monotonic pattern。
      T=0.5 比 T=0.3 低可能是 random noise at n=204。
      Combined with T=0.3 result，T sensitivity curve 是 "generally positive at low-medium T, 
      negative at high T" 但无 clean functional form。
    tables: ["Appendix T sensitivity table: T=0.5 行"]
    figures_description: ["T sensitivity subplot: 4-point curve showing non-monotonic noisy pattern"]
    analysis: >
      T=0.5 填充了 curve 但增加了 noise。4 个 temperature points 无 clean trend 
      (not inverted-U, not monotonic, not plateau-then-cliff)。
      Worst tier 下 T sensitivity section 从 "clean ablation" 降级为 "noisy exploration"。
      Only defensible claim: "SICA delta decreases substantially at T=1.0"，
      but even this is one data point (could reframe as "high temperature degrades constraint extraction" 
      which is somewhat obvious)。

  # ── Cross-cutting analysis experiments (planned, CPU-only) ──

  - name: "effk_sc_joint_prediction"
    plan_id: "cross-analysis"
    description: "Eff-K + SC joint prediction accuracy across all 12+ conditions"
    expected_results:
      total_conditions: 12
      correctly_predicted_positive: 2
      correctly_predicted_negative: 4
      incorrectly_predicted: 6
      prediction_accuracy_pct: 50.0
      key_failures:
        - "Mistral-PW600: Eff-K=3.63 (highest) predicts positive but delta=-2.83pp"
        - "Mistral-s42 vs s123: similar Eff-K+SC but delta differs by 1.47pp"
        - "LLaMA-D012: Eff-K unknown but high C0 → predicted positive, actual +6.67pp n.s."
        - "Mistral-s456: Eff-K=2.22 similar to s123 (2.17) but delta reverses sign"
    result_rationale: >
      Worst tier: Eff-K+SC framework predicts ≤6/12 conditions correctly (≤50%)。
      跨模型 direction 正确 (Qwen→0, Mistral→variable) 但 Mistral 内部完全不 work。
      Eff-K 与 delta 在 Mistral seeds 内无 monotonic relationship (s42: Eff-K=1.85, delta=+4.9; 
      s123: Eff-K=2.17, delta=+3.4; s456: Eff-K=2.22, delta=-0.5)——方向甚至相反。
      PW-600 (Eff-K=3.63, delta=-2.83) 用 "SC too low" 勉强解释，但 reviewer 会说 
      这是 post-hoc rationalization。
      Framework 降级: "Eff-K is a necessary condition for cross-model comparison 
      but has no within-model predictive power"——这是一个 much weaker claim。
    tables: ["T3: 增加 prediction hit/miss column"]
    figures_description: ["Eff-K vs delta scatter with SC as color — no clean separation boundary"]
    analysis: >
      Joint prediction ≤50% accuracy 是 worst tier 下 Condorcet framework 的死亡判决。
      不能说 "Eff-K predicts SICA effectiveness" 只能说 "Eff-K explains why Qwen family 
      uniformly fails"。Claim 1 从 "Independence Bottleneck" (predictive) 降为 
      "Independence Observation" (descriptive)。Condorcet 从 core claim 降入 discussion。
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f51f0cc8-68dc-4815-822b-8aa766506b59",
  "isSidechain": false,
  "requestId": "req_011CbBGTp8fuCDnWu3N6k7ob",
  "type": "assistant",
  "uuid": "93918675-211f-4d81-ab96-f6af5f548168",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3",
  "sessionId": "f34ece61-443f-4fad-9714-c7dbf3b3b1b5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FDGXEoQc91krEvoUH82Kcm",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 29067,
      "cache_read_input_tokens": 11841,
      "output_tokens": 14352,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 29067,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 14352,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 29067,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 29067
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：Eff-K 作为预测器失败，K/T curves 无 clean pattern。核心 Condorcet framing 不 hold。需 reframe 为 comprehensive negative-results / diagnostic 贡献，保留 oracle gap 和 C0 diagnos…",
  "leafUuid": "93918675-211f-4d81-ab96-f6af5f548168",
  "sessionId": "f34ece61-443f-4fad-9714-c7dbf3b3b1b5"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyzing the independence bottleneck in self-extracted symbolic consensus",
  "sessionId": "f34ece61-443f-4fad-9714-c7dbf3b3b1b5"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：Eff-K 作为预测器失败，K/T curves 无 clean pattern。核心 Condorcet framing 不 hold。需 reframe 为 comprehensive negative-results / diagnostic 贡献，保留 oracle gap 和 C0 diagnos…",
  "leafUuid": "93918675-211f-4d81-ab96-f6af5f548168",
  "sessionId": "f34ece61-443f-4fad-9714-c7dbf3b3b1b5"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyzing the independence bottleneck in self-extracted symbolic consensus",
  "sessionId": "f34ece61-443f-4fad-9714-c7dbf3b3b1b5"
}
```

---
