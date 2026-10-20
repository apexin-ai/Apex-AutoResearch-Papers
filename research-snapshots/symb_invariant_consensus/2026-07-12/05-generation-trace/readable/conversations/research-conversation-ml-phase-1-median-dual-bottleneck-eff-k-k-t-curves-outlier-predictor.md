# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义： 含义：Dual Bottleneck 方向成立但 Eff-K 预测力有噪声。K/T curves 有 outlier 需解释。需弱化 'predictor

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 27
- **Recorded user turns:** 1
- **Tool calls:** 4
- **Original source:** `logs/chats/exported-trajectories/account-2/94c4266a-dd51-40f0-bc57-040b308715ff.jsonl`
- **Structured JSON:** [`87711ba31547fde1abbc.json`](../../sessions/87/87711ba31547fde1abbc.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-19T03:52:54.530Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-19T03:52:54.530Z",
  "sessionId": "94c4266a-dd51-40f0-bc57-040b308715ff",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：\n\n含义：Dual Bottleneck 方向成立但 Eff-K 预测力有噪声。K/T curves 有 outlier 需解释。需弱化 'predictor' 为 'necessary condition'，重心转向 oracle gap + remediation failures。Findings 可达。\n核心假设：['exp-051 K sensitivity 大致呈 inverted-U 但有 1-2 个 non-monotonic 点 (如 K=8 高于 K=12 或 K=16 反弹)', 'T sensitivity 方向正确 (T=0.7 peak) 但 T=0.3 或 T=0.5 有意外正值 (如 T=0.3 ~+2pp)', 'exp-055 multi-temp 接近 0 但 CI 包含正值', 'Eff-K 跨模型方向正确 (Qwen→0, Mistral→positive) 但 seed 内和 condition 内 variance 大到无法做定量预测', 'exp-050b ICL complication 无法完全解释，需在 paper 中作为 limitation 处理']\n关键指标范围：{'mistral_k_peak_delta_pp': [2.5, 5.0], 'mistral_k_k4_delta_pp': [-3.0, 3.0], 'mistral_k_k20_delta_pp': [-3.0, 3.0], 'mistral_k_inverted_u_visual': '大致 peak 在 K=10-14 但 1-2 点偏离趋势', 't03_delta_pp': [-2.0, 3.0], 't05_delta_pp': [-1.0, 4.0], 'multitemp_delta_pp': [-3.0, 1.5], 'effk_sc_joint_prediction_accuracy': '7-9/12 conditions 方向正确', 'estimated_reviewer_avg': [2.8, 3.2]}\n叙事方向：弱化 Claim 1 措辞: Eff-K 从 \"predictor\" 降为 \"necessary condition that interacts with SC\"。 承认 seed variance 是 open question，明确表述为 \"Eff-K explains cross-model variance; within-model variance remains dominated by stochastic factors\"。 K/T sensitivity 如有 outlier，用 error bar / CI overlay 展示 noise level，frame 为 \"directionally consistent despite noise\"。 论文重心从 Condorcet 理论预测力 转向 oracle gap (最强证据, p=2e-7) + 9 remediation failures (breadth argument)。 Condorcet 框架降为 \"explanatory lens\" 而非 \"predictive framework\"。 exp-050b ICL complication 放 discussion 作为 future work。 投稿目标: Findings (≥3.0)。如 reviewers 认可 breadth of analysis 可能升 Main。\n\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: symb_invariant_consensus\nfocus: D060 纯 Analysis paper — Dual Bottleneck (Independence + Quality) framing。重点审查：1) Condorcet Eff-K 作为跨模型预测器是否有说服力（seed 内部非单调问题）；2) 9 种修复失败作为 structural bottleneck 证据是否充分；3) K/T sensitivity ablation 的 inverted-U 是否足够 clean；4) Analysis paper 在 EMNLP 2026 的竞争力（≥3.0 Findings 可达性）\n\n## paper_framing.md\n\n# Paper Framing — symb_invariant_consensus\n\n## Target Venue\n- Primary: EMNLP 2026 Main (ARR May 25)\n- Deadline: May 25, 2026 (ARR submission)\n\n## D060 Direction: Pure Analysis Paper — Independence Bottleneck\n\n**D059 method improvement 三路失败后，回归纯 analysis paper。** 但比 D058 的 analysis 更强：\n- **Condorcet independence 框架** 提供理论解释（非纯经验）\n- **9 种修复全部失败**（比原 6 种多 3 种靶向尝试）→ bottleneck 是 fundamental\n- **exp-052 p=0.039** → 2/3 seeds 显著 → 效应 IS real but fragile\n- **K sensitivity 倒 U 型** → clean ablation 贡献\n- **T sensitivity** → +4.90pp 仅在 T=0.7 存在，T=1.0 降到 +0.55pp → 效应极度脆弱\n- 用户指示: 投 May 25 不变，≥3.0 兜底\n\n## Core Claims (5 条) — D060 纯 Analysis Framing\n\n### Analysis Claims (已验证)\n\n1. **Independence Bottleneck**: Self-consistency 隐含 Condorcet Jury Theorem 的独立性假设，但同模型采样的 traces 高度相关。Worker 验证的 κ 值：\n   - Qwen-14B FOLIO: κ=0.744, Eff-K=1.31 (SC=75.49%, Δ=+0.25pp n.s.)\n   - Qwen-14B LogiQA: κ=0.821, Eff-K=1.20 (SC=78.5%, Δ=+0.50pp n.s.)\n   - Mistral-7B FOLIO s42 (exp-033): κ=0.500, Eff-K=1.85 (Δ=+4.90pp p=0.013) ← primary seed\n   - Mistral-7B FOLIO s123: κ=0.412, Eff-K=2.17 (Δ=+3.43pp p=0.039)\n   - Mistral-7B FOLIO s456: κ=0.401, Eff-K=2.22 (Δ=-0.49pp n.s.)\n   - Mistral-7B PW-600 (exp-046): κ=0.210, Eff-K=3.63 (Δ=-2.83pp p=0.010, SC=39%)\n   规律：跨模型对比清晰（Qwen Eff-K≈1.2-1.3 → 0 gain; Mistral Eff-K≈1.85-2.22 → variable gain）。但 Mistral seeds 内部，Eff-K 与 delta 非单调（exp-033 Eff-K 最低 1.85 却 delta 最高 +4.90pp）→ Eff-K 是跨模型必要条件，seed 内 variance 仍主导。exp-046 Eff-K 最高(3.63) 但 SC 太低(39%) 导致 delta 为负 → 需同时满足 sufficient Eff-K AND sufficient SC。\n\n2. **Oracle Gap Localizes Extraction Bottleneck**: Gold FOL + MAX-SAT = +14.22pp (p=2.0e-7)，自提取仅 +4.9pp (best case) = 35% utilization。聚合机制本身有效，瓶颈在自提取质量。Two-layer analysis:\n   - **Constraint taxonomy**: 43% trivially_satisfied（被所有候选答案满足的约束，不排除任何答案）\n   - **Discriminative filtering**: 仅 ~8% 约束在 MAX-SAT scoring 中完全 non-discriminative（移除后 0 gains）\n   - **关键区分**: 43% 和 8% 度量不同。trivially_satisfied 约束在 MAX-SAT 中仍可有不同满足程度（partial vs full），所以不全是 non-discriminative。但即使 constraints 是 discriminative 的，它们的\"区分方向\"与模型自身偏差一致（confirmation bias）。both_wrong 组 score_range=29.4。九种修复全部失败。\n\n3. **Regime-Dependent Capability Trap**: SICA 有效性取决于提取模型的基线准确率，存在双边界：\n   - Type A (SC ≥ ~60%): 确认偏差，constraints 镜像模型自身答案\n   - Type C (SC ≤ ~40%): traces 主要错误，constraints 是噪声 (exp-046: Δ=-2.83pp, p=0.0095)\n   - Goldilocks zone (~50-55% SC): 部分独立性 + 部分正确性 (exp-033: Δ=+4.90pp, p=0.013)\n   - Type B: 领域不可形式化 (LogiQA: contradiction rate 0.8%)\n\n4. **C0+SC Two-Dimensional Diagnostic**: C0 (multi-candidate rate) + SC accuracy 形成零成本部署诊断。C0<5% → degenerate; high C0 + high SC → trap; high C0 + low SC → potential gains。\n\n### Remediation Evidence (D060: 全部失败 — 强化 analysis narrative)\n\n5. **Nine Remediation Attempts All Failed**: 原 6 种 + 3 种靶向修复全部无效，证明 independence bottleneck 是结构性的：\n   - D059 三路 method improvement 全部失败：\n     - Discriminative Filtering: 119/204 处理后 0 gains 1 loss，~92% 约束本身就是 discriminative，过滤是 near-no-op\n     - T=1.0 (exp-054): delta 从 +4.90pp 崩塌到 +0.55pp，温度敏感性极端\n     - Multi-Temp (exp-055): 早期 n=28 delta=0.00pp（待完成，但预期 negative）\n   - 原 6 种：contrastive prompting, cross-model extraction, generational scaling, solver-guided refinement, consistency filtering, cross-trace UNSAT\n   - 9 种修复涵盖 prompting / architecture / capability / verification / diversity / filtering 全维度，全部失败 → trap is fundamental\n\n## Core Insight (D060 Updated — Dual Bottleneck)\n\n**Dual Requirement Framework**: SICA 效应需要同时满足两个条件，缺一不可：\n1. **Sufficient Independence** (Eff-K > threshold): traces 需要提供足够多的独立视角\n2. **Sufficient Quality** (SC > ~50%): traces 需要有足够的正确率，否则约束是噪声\n\nCondorcet Jury Theorem 要求投票者独立且 p>0.5。同模型采样的 reasoning traces 严重违反独立性假设（Fleiss' κ = 0.21–0.82，Eff-K 仅 1.20–3.63），解释了为什么简单增加 K 或添加符号约束不能突破 SC 的天花板。\n\n实验数据完美支持 dual requirement：\n- **Qwen-14B**: Eff-K≈1.2-1.3（独立性不足）→ 0 gain，无论 SC 多高\n- **Mistral-7B FOLIO**: Eff-K≈1.85-2.22（中等独立性）+ SC≈54%（中等质量）→ +4.90pp (2/3 seeds significant)\n- **Mistral-7B PW-600**: Eff-K=3.63（最高独立性）但 SC=39%（质量不足）→ -2.83pp\n- 只有 Goldilocks zone（中等 Eff-K + 中等 SC）出现正向 delta\n\nOracle control (+14.22pp) 证明 MAX-SAT 聚合机制本身有效，但自提取约束仅利用了 35% 的理论上限。Discriminative filtering 实验揭示关键机制：~92% 约束 ARE discriminative，但过滤掉 ~8% non-discriminative 约束后 delta 不变（0 gains）。问题不在约束缺乏判别力，而在于 discriminative constraints 的区分方向与模型偏差一致（confirmation bias）。\n\n**κ-delta 反相关解释**：exp-033 κ=0.500 比 exp-052/053 κ≈0.41 高，但 delta 最大。原因：exp-033 Unknown 比例低（49.9% vs 58.5%），traces 更 decisive（更多 True/False 判断）→ 同时导致更高 κ（更多 agreement）和更好的 constraint quality。κ 不是 SICA 效果的唯一决定因素。\n\n**Remediation insight (D060)**: 9 种修复尝试全部失败，包括直接靶向 independence（multi-temp diversity）和 constraint quality（discriminative filtering）。这证明 bottleneck 不是简单的 diversity 或 quality 问题，而是 same-model self-extraction 的根本性限制。\n\n**Key evidence**:\n- **Condorcet independence quantification (Worker-verified, 公式: Eff-K=K/(1+(K-1)κ))**: exp-033 Mistral-7B s42 κ=0.500 (Eff-K=1.85), Mistral-7B s123 κ=0.412 (Eff-K=2.17), Mistral-7B s456 κ=0.401 (Eff-K=2.22), Mistral-7B PW-600 κ=0.210 (Eff-K=3.63), Qwen-14B FOLIO κ=0.744 (Eff-K=1.31), Qwen-14B LogiQA κ=0.821 (Eff-K=1.20). 跨模型清晰: Qwen Eff-K≈1.2-1.3→0 gain, Mistral Eff-K≈1.85-3.63→variable. Eff-K necessary but not sufficient: exp-046 highest Eff-K(3.63) but negative delta(SC too low); within Mistral seeds Eff-K非单调 with delta.\n- **Oracle control (exp-031)**: Gold FOL + MAX-SAT = 89.71% vs SC 75.49% (+14.22pp, p=2.0e-7). Unknown-type +31.9pp.\n- **Two-layer constraint analysis**: 43% trivially_satisfied (taxonomy: satisfied by ALL answers) vs ~8% non-discriminative (filtering: same MAX-SAT score). Difference: trivially_satisfied constraints can still have different satisfaction DEGREES. Removing the 8% yields 0 gains → problem is not quality but confirmation bias direction.\n- **K sensitivity (inverted U)**: K=4(-1.47pp), K=8(-0.98pp), K=12(+4.90pp p=0.013), K=16(+1.47pp), K=20(pending). Peak at K=12, then decline. Non-monotonic. K=4 SC ≈ K=12 SC but SICA differs by 6.4pp — proves SICA extracts different information than SC.\n- **T sensitivity (extreme fragility)**: T=0.7(+4.90pp p=0.013), T=1.0(+0.49pp p=0.739). 温度从 0.7 提到 1.0 让增益降 90%。T=0.3 (exp-057, pending). SICA 效应极度依赖超参数。\n- **Regime boundary**: Qwen-14B (SC=75.49%) Δ=+0.25pp vs Mistral-7B (SC=54.41%) Δ=+4.90pp p=0.013\n- **Type C failure (exp-046)**: Mistral PW-D5 SC=39.33%, Δ=-2.83pp, p=0.010, κ=0.210, Eff-K=3.63, contradiction rate 5.5%. Highest Eff-K yet worst delta → independence alone insufficient when SC too low.\n- **Seed replication**: 2/3 seeds significant at α=0.05 (exp-033 p=0.013, exp-052 p=0.039), 1/3 null (exp-053). Effect IS real but fragile — motivates deep analysis of WHY.\n- **Nine remediation failures**: contrastive prompting, cross-model, generational scaling, solver-guided, consistency filtering, cross-trace UNSAT, discriminative filtering (0 gains), T=1.0 (delta collapse), multi-temp (pending, early 0.00pp). All failed → trap is fundamental.\n- **Entropy mechanism**: High-entropy problems proportion: Mistral 35.8% vs Qwen 10.3%. Unanimous rate: 18.6% vs 58.8%.\n- **Confirmation bias quantification**: Override precision 70.6% (Mistral) vs 28.6% (Qwen). Constraint agreement >80%: 31.9% vs 62.3%.\n\n## Story Spine (D059 Updated)\n\n- **Problem**: LLMs' reasoning can be improved by sampling multiple chains-of-thought and aggregating via majority voting (self-consistency). Recent work proposes symbolic augmentation: extract formal constraints from traces and use SAT solvers for answer selection. But does symbolic aggregation actually outperform simple voting?\n- **Theoretical lens**: Condorcet Jury Theorem requires voter independence. We quantify trace independence via Fleiss' κ and show Effective-K << nominal K. This explains the fundamental limitation of same-model trace aggregation.\n- **Systematic evaluation**: SICA (MAX-SAT over FOL constraints) across 3 domains × 5 model families. Oracle control separates extraction vs aggregation failure. Discriminative filtering reveals ~92% constraints are discriminative, yet SICA gains are fragile — confirmation bias, not constraint quality, is the bottleneck.\n- **Regime characterization**: Three failure modes (Type A/B/C) + narrow Goldilocks zone. C0+SC as deployment diagnostic.\n- **Remediation failures strengthen thesis**: 9 targeted interventions (prompting, architecture, capability, verification, diversity, filtering) all fail to close the oracle gap, proving the bottleneck is fundamental to same-model self-extraction.\n- **Headline result**: \"Across 5 model families, symbolic consensus aggregation shows a real but fragile effect: significant improvement in 2/3 seeds under specific conditions (Mistral-7B, FOLIO, T=0.7, K=12), but zero or negative gains under any perturbation. Condorcet analysis reveals the root cause: Effective-K = 1.3-1.8 for nominal K=12 due to trace non-independence. Oracle constraints prove the aggregation mechanism works (+14.22pp), but 9 remediation strategies all fail to overcome the self-extraction bottleneck. C0+SC provides a zero-cost deployment diagnostic.\"\n\n## Anticipated Reviewer Concerns & Defensive Experiments\n\n1. **\"Gains not statistically significant\"** → exp-033 p=0.013 (n=204), exp-031 oracle p=2.0e-7. Combined N>1,200.\n2. **\"Only one positive result (exp-033)\"** → Seed replication: 2/3 significant (p=0.013, p=0.039). Effect IS real but fragile — the fragility itself IS the finding (K/T sensitivity, Condorcet independence).\n3. **\"Condorcet framework is trivial\"** → Fleiss' κ quantification is novel in SC/SICA context. Eff-K is actionable: tells practitioners how many truly independent traces they get.\n4. **\"Multi-temp / filtering should work\"** → We tried both. Multi-temp (exp-055): negative. Disc. filtering: 0 gains. T=1.0: delta collapse. These failures STRENGTHEN the structural bottleneck thesis.\n5. **\"Only Qwen models\"** → 5 families: Qwen-14B, Mistral-7B, LLaMA-8B, DeepSeek-R1-7B, QwQ-32B.\n6. **\"Only logic domain\"** → FOLIO + ProofWriter + LogiQA + StrategyQA + ARC-Challenge. Type B (domain formalizability) is itself a finding.\n7. **\"Oracle is unfair comparison\"** → Diagnostic tool, not competing method. Separates extraction from aggregation.\n8. **\"MAX-SAT is over-engineering\"** → exp-013: MaxSAT ≈ count-only. This IS the independence bottleneck evidence.\n9. **\"Self-extraction confound\"** → Oracle control resolves completely.\n10. **\"Published methods achieve gains (DyLoS, Aristotle, FoVer)\"** → Different paradigm (external verifiers/trained extractors). We characterize same-model self-extraction.\n11. **\"C0 is trivially derived\"** → Zero-cost early stopping. Practical value.\n12. **\"Why not just use a reasoning model?\"** → QwQ-32B: C0<5%, SICA≡SC.\n13. **\"Random tiebreak baseline\"** → exp-003: SICA tiebreak 80% vs random 50%.\n14. **\"Method improvement is incremental\"** → Grounded in diagnosis (independence + taxonomy), not ad-hoc.\n15. **\"Weighted SC is simpler\"** → exp-016 planned. Weighted SC doesn't address independence.\n16. **\"Within-model ICL transition contradicts regime theory\"** → exp-050b (SC=57.79%, Δ=-3.52pp): ICL changes trace generation characteristics, not just SC level. Paper must distinguish \"same model, different prompt\" from \"same model, same prompt, different accuracy.\"\n\n## Working Title\n**\"Beyond Self-Consistency: How Trace Independence Limits Symbolic Consensus in LLM Reasoning\"**\n(Alternatives:\n- \"The Independence Bottleneck: Why Self-Extracted Symbolic Constraints Cannot Beat Majority Voting\"\n- \"Symbolic Consensus Under the Condorcet Lens: Independence, Extraction, and the Limits of Self-Aggregation\")\n\nNOTE (Dream D037): Title MUST be scoped to \"self-extracted constraints\" / \"SICA\". Published methods (DyLoS, Aristotle, FoVer) use different approaches.\n\n## Paper Structure (EMNLP 8pp + appendix)\n\n### Main Tables\n- T1: Main Results — models × domains, SC% / SICA% / Δpp / p-value, regime boundary\n- T2: Oracle Control — Gold-FOL+MAX-SAT vs SC vs SICA-self, causal separation\n- T3: Independence Quantification — Fleiss' κ / Eff-K / trace agreement per model\n- T4: Extraction Error Taxonomy — trivially_satisfied / discriminative / both_wrong rates\n- T5: K Sensitivity — K=4/8/12/16/20 with Eff-K and diversity metrics (inverted U curve)\n\n### Main Figures\n- F1: Method Pipeline (SICA + oracle control design)\n- F2: SC Accuracy vs SICA Δ scatter (hero figure, regime boundary)\n- F3: K Sensitivity with diversity metrics (K vs Δ, K vs Eff-K)\n- F4: Extraction error breakdown (stacked bar)\n\n### Appendix\n- K ablation details, temperature sensitivity, per-domain results, overhead analysis\n- Entropy-conditioned analysis (continuous scatter + bin sensitivity)\n- Six remediation strategy details\n- Confirmation bias quantification\n- Seed replication analysis\n- QwQ-32B / DeepSeek-R1 negative control\n\n## Claim Risk Notes (D059)\n- **Seed replication**: 2/3 significant (p=0.013, p=0.039), 1/3 null. Frame as \"real but fragile effect\" — motivates analysis of WHY.\n- **Method claims DEAD (D060)**: All three method improvements failed. Paper is pure analysis. 9 remediation failures are EVIDENCE, not limitation.\n- **Condorcet novelty**: ✅ VERIFIED. arXiv:2409.00094 applies CJT to cross-model LLM ensembles (different angle). No prior work applies Fleiss' κ or Eff-K to within-model SC traces. Our framing is novel.\n- **exp-050b complication**: ICL transition Δ=-3.52pp at SC=57.79% complicates simple \"SC determines SICA.\" Explain via trace generation characteristic change.\n- **Variable naming inconsistency**: 56.4% cross-trace pairs share zero Z3 variables. Key mechanism evidence.\n\n## Required Citations (minimum 30 references)\n\n- **SC & extensions**: Wang et al. 2023 (SC), Chen et al. 2023 (USC), Loo et al. 2025 (SC scaling plateaus), Taubenfeld et al. 2025 (weighted SC), DiVeRSe (Li et al. 2023)\n- **Neuro-symbolic reasoning**: DyLoS (EACL 2026), Aristotle (ACL 2025), FoVer (TACL 2025), LogicAgent (2025), Logic-LM (Pan et al. 2023), LINC (Olausson et al. 2023)\n- **Condorcet/voting theory**: Condorcet 1785, Austen-Smith & Banks 1996, **arXiv:2409.00094 (Examining Independence in Ensemble Sentiment Analysis, Sept 2024)** — closest prior work, applies CJT to cross-model LLM ensembles, finds independence violation. Our novelty: within-model trace independence + Fleiss' κ quantification + Eff-K + connection to symbolic aggregation\n- **Test-time compute**: Snell et al. 2025, DeepSeek-R1, Diversity-Aware Training\n- **Verification & reranking**: ORM (Cobbe et al. 2021), PRM (Lightman et al. 2023), Math-Shepherd\n- **Constraint satisfaction**: SATBench (EMNLP 2025), LLM Meets Constraint Propagation (IJCAI 2025)\n- **Debate & multi-agent**: Liang et al. 2023, Du et al. 2023\n\n## Claim Scoping Rules\n- n=60 conditions: \"suggestive/consistent with\" NOT \"confirming\"\n- n≥200 conditions: can \"confirm\"\n- Combined N>1,300: acceptable if breakdown clearly stated\n- Method claims: must show statistically significant improvement OR clear directional improvement with analysis\n- \"Independence bottleneck\" framing: systematic quantification + theoretical grounding\n\n\n## experiment_plan (with registry status)\n\n- id: exp-001\n  name: sica_expanded_14b\n  claim:\n  - 1\n  - 2\n  description: 'Full-scale evaluation: PW D5 600 + FOLIO 204 = 804 questions, K=12,\n    T=0.7. Maximizes statistical power for C3 significance.'\n  priority: P0\n  gpu_budget_hours: 14\n  deps: []\n  registry_id: sica_expanded_14b\n  status: DONE\n  conclusion: success\n  metrics:\n    sica_accuracy: 0.765\n    sc_accuracy: 0.762\n    sica_sc_gap_pp: 0.3\n    n_problems: 804\n    multi_candidate_rate: 0.3818\n    folio_sica: 0.794\n    folio_sc: 0.794\n    folio_gap_pp: 0\n    folio_n: 204\n    proofwriter_sica: 0.755\n    proofwriter_sc: 0.752\n    proofwriter_gap_pp: 0.3\n    proofwriter_n: 600\n    extraction_rate: 0.89\n    answer_extraction_rate: 1\n    contradiction_rate: 0.022\n    problems_with_contradictions: 331\n    truncated_traces: 0\n    wall_time_min: 826\n- id: exp-002\n  name: sica_k_ablation_14b\n  claim:\n  - 1\n  description: 'K sensitivity (K=6,8,11,12,16,20) on D012''s 60 questions. Includes\n    odd K=11 to test if SICA value persists without exact ties. Key questions: does\n    SICA benefit depend on tiebreaks? What happens at odd K? How does tiebreak frequency\n    change with K?'\n  priority: P0\n  gpu_budget_hours: 6\n  deps: []\n  status: planned\n  note: D024 增加 K=11（odd-K test, Dream 三档一致要求）。如 K=11 gap=0 → 确认 tie-only mechanism；如\n    gap>0 → SICA has value beyond tiebreaking。\n- id: exp-003\n  name: tiebreak_baseline_analysis\n  claim:\n  - 1\n  description: Compare SICA vs SC-random-tiebreak vs SC-deterministic on all available\n    data. CPU-only reanalysis. Quantify how much of SICA's gain survives against fair\n    baselines.\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - sica_d012_14b\n  status: planned\n  note: 'Completed as CPU analysis, no registry entry. Results: SICA tiebreak 80%\n    (4/5) vs random 50% vs alphabetical 60% vs first-seen 40%. Artifact: art_20260516_47de9d'\n- id: exp-004\n  name: sica_7b_scaling\n  claim:\n  - 2\n  - 3\n  description: 'Run SICA with Qwen2.5-7B-Instruct on same 60 questions. Test: does\n    weaker model → higher C0 → larger SICA gain? Validates C0-as-predictor claim.'\n  priority: P1\n  gpu_budget_hours: 2\n  deps:\n  - exp-001\n  status: planned\n- id: exp-005\n  name: qwq_32b_operating_regime\n  claim:\n  - 2\n  description: QwQ-32B negative results formatted for paper's Operating Regime Analysis\n    section. Data exists from MVP phase (AIME, MATH, ProofWriter, FOLIO). No new GPU\n    needed.\n  priority: P1\n  gpu_budget_hours: 0\n  deps: []\n  status: planned\n  note: 'Data from QwQ-32B MVP experiments: sica_aime30_v3 (AIME 22题, 0% multi-candidate),\n    sica_proofwriter30_v2 (PW 16题, 18.75% multi-candidate), sica_folio30 (FOLIO 10题,\n    0% multi-candidate). Combined C0=3.6%, SICA≡SC across all domains.'\n- id: exp-006\n  name: c0_diagnostic_validation\n  claim:\n  - 3\n  description: Plot C0 vs SICA-SC gap across all models and K values. Validate C0\n    as predictor. CPU-only analysis over exp-001/002/004/005 results.\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - exp-001\n  - exp-002\n  - exp-004\n  status: planned\n- id: exp-007\n  name: sica_72b_awq\n  claim:\n  - 2\n  description: 'Qwen2.5-72B-Instruct AWQ 4-bit on 60 questions. Scaling analysis:\n    high-baseline non-reasoning model. Within-Qwen scaling dimension.'\n  priority: P1\n  gpu_budget_hours: 4\n  deps:\n  - exp-001\n  status: planned\n  note: D019 升级 P2→P1. 72B-AWQ 4-bit ~36GB weights + KV cache ≈ 50-60GB, 98GB RTX\n    PRO 6000 单卡可放。\n- id: exp-008\n  name: constraint_quality_case_studies\n  claim:\n  - 1\n  description: Qualitative analysis of extracted constraints on 5-10 representative\n    questions. Are constraints semantically meaningful? Do excluded constraints correspond\n    to reasoning errors?\n  priority: P2\n  gpu_budget_hours: 0\n  deps:\n  - exp-001\n  status: planned\n- id: exp-009\n  name: overhead_analysis\n  claim:\n  - 1\n  description: 'Wall-time breakdown per question: generation, constraint extraction,\n    MaxSAT solving. Address ''is the overhead worth it'' concern.'\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - exp-001\n  status: planned\n  note: D021 升级 P2→P1. Reviewer 指出 EMNLP 审稿人对 practical impact 极敏感。\n- id: exp-010\n  name: sica_mistral_7b\n  claim:\n  - 2\n  - 3\n  description: 'Mistral-7B-Instruct-v0.3 on D012 60 questions (PW+FOLIO). Cross-family\n    validation: does C0 pattern hold outside Qwen? Eliminates ''Qwen-specific artifact''\n    attack.'\n  priority: P0\n  gpu_budget_hours: 1.5\n  deps: []\n  status: DONE\n  note: 'D021 新增. 必做——消除 Claim 2 致命弱点。Escalation: 若 C0>30% 且 gap>0 但 p>0.2，扩展到 200+\n    题（~3h GPU，margin 允许）。'\n  registry_id: exp-010-mistral-v3\n  conclusion: negative\n  metrics:\n    n: 60\n    k: 12\n    sica_accuracy: 0.4833\n    sc_accuracy: 0.4833\n    delta_pp: 0\n    multi_candidate_rate: 0.5\n    extraction_rate: 0.8819\n    answer_extraction_rate: 1\n    contradiction_rate: 0.0562\n    discordant_sica_wins: 2\n    discordant_sc_wins: 2\n    mcnemar_p: 1\n    proofwriter_sica: 0.4\n    proofwriter_sc: 0.4\n    proofwriter_delta_pp: 0\n    folio_sica: 0.5667\n    folio_sc: 0.5667\n    folio_delta_pp: 0\n    truncated_traces: 0\n    model: Mistral-7B-Instruct-v0.3\n    dataset: D012\n- id: exp-011\n  name: sica_llama_8b\n  claim:\n  - 2\n  - 3\n  description: LLaMA-3.1-8B-Instruct on D012 60 questions. Second non-Qwen family.\n    Combined with exp-010 gives 3-family coverage (Qwen/Mistral/LLaMA).\n  priority: P0\n  gpu_budget_hours: 1.5\n  deps: []\n  status: planned\n  note: D021 新增. 必做——3 家族是 EMNLP 最低门槛。需 HF_TOKEN（Meta license）或 ModelScope 镜像。Escalation\n    同 exp-010。\n- id: exp-012\n  name: gsm8k_pilot_14b\n  claim:\n  - 2\n  - 3\n  description: 'Qwen2.5-14B on GSM8K 30-question pilot (K=12). Cross-domain test:\n    is C0 high only in restricted-answer-space domains (NLI 3-class) or also in open-answer\n    math? If C0 low → C0=uncertainty signal (strengthens Claim 3). If C0 high → cross-domain\n    win.'\n  priority: P1\n  gpu_budget_hours: 1\n  deps: []\n  status: planned\n  note: D021 新增. Reviewer 预测 C0<20% (14B too strong on GSM8K). Any result is publishable\n    insight.\n- id: exp-013\n  name: constraint_ablation\n  claim:\n  - 1\n  - 2\n  description: 'CPU-only ablation: SICA-MaxSAT vs SICA-count-only (constraint count\n    per answer, no satisfiability) vs SICA-random-weight. Critical for D025 pivot:\n    if MaxSAT ≈ count-only → aggregation mechanism is vacuous, confirming capability\n    trap.'\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - exp-001\n  status: planned\n  note: 'D025 升级 P1→P0. 现在是 make-or-break: 如果 MaxSAT = count-only → 证明 SAT 解算无贡献（capability\n    trap 的 mechanism evidence）。必须用 exp-002 的 raw_constraints 数据。'\n- id: exp-014\n  name: sica_deepseek_r1_llama_8b\n  claim:\n  - 2\n  description: 'DeepSeek-R1-Distill-LLaMA-8B on D012 60 questions. Second reasoning\n    model data point with LLaMA base architecture: validates C0<5% generalizes beyond\n    QwQ-32B AND eliminates ''still Qwen family'' attack.'\n  priority: P1\n  gpu_budget_hours: 2\n  deps: []\n  status: planned\n  note: D021 新增. Reviewer 建议用 LLaMA 底座版本避免 Qwen 架构归属争议。\n- id: exp-015\n  name: logic_lm_baseline\n  claim:\n  - 1\n  description: Logic-LM × K + majority vote baseline on FOLIO. Run Logic-LM style\n    single-trace FOL verification K times, then majority vote. Isolates whether MAX-SAT\n    multi-trace aggregation adds value beyond FOL extraction itself.\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - exp-001\n  status: planned\n  note: 'D024 新增. Dream 三档一致要求 Logic-LM/LINC 比较。CPU-only: 用 exp-001 已有 traces + FOL\n    constraints 做单 trace verification then vote。'\n- id: exp-016\n  name: weighted_sc_baseline\n  claim:\n  - 1\n  - 3\n  description: 'Weighted SC baseline (Taubenfeld et al. 2024 style): weight votes\n    by trace confidence/length/perplexity. CPU-only reanalysis of exp-001/002 data.\n    Tests if simple weighting achieves same tiebreak quality without MAX-SAT.'\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - exp-001\n  status: planned\n  note: 'D024 新增. Dream 提出 weighted SC 是最直接竞争 baseline。实现方式: (1) uniform weight (=SC),\n    (2) length-weighted, (3) log-prob weighted (如 traces 有 logprobs), (4) constraint-count\n    weighted (no SAT)。'\n- id: exp-017\n  name: sica_strategyqa_14b\n  claim:\n  - 1\n  - 2\n  description: Qwen2.5-14B on StrategyQA 60 questions (K=12). Commonsense reasoning\n    domain — high predicted C0 (35-50%) but implicit reasoning chains → low expected\n    constraint quality. Tests capability trap in best-case-diversity scenario.\n  priority: P0\n  gpu_budget_hours: 1.5\n  deps: []\n  status: planned\n  note: D025 新增. Reviewer 推荐 ROI 最高 benchmark。如 C0>30% 且 SICA≈SC → 直接证明 capability\n    trap（diversity high but quality low → no gain）。\n- id: exp-018\n  name: sica_arc_challenge_14b\n  claim:\n  - 1\n  - 2\n  description: Qwen2.5-14B on ARC-Challenge 60 questions (K=12). Science reasoning,\n    4-choice format. Tests constraint mechanism in multi-choice scenario + different\n    domain.\n  priority: P0\n  gpu_budget_hours: 1.5\n  deps: []\n  status: planned\n  note: D025 新增. 4选1格式测试 constraint mechanism 泛化能力。与 FOLIO (3-class) + GSM8K (open)\n    + StrategyQA (binary) 形成答案格式多样性。\n- id: exp-019\n  name: constraint_quality_correlation\n  claim:\n  - 1\n  - 2\n  description: 'CPU-only analysis: compute constraint precision per domain × model,\n    correlate with C0 and SICA-SC gap. Formalizes the capability trap as inverse C0-quality\n    correlation. Uses data from exp-001/010/011/017/018.'\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - exp-001\n  - exp-017\n  - exp-018\n  status: planned\n  note: 'D025 新增. Hero figure (F2) 的数据来源。Constraint quality = (constraints consistent\n    with ground truth) / (total constraints). 预期: high C0 domains (StrategyQA) have\n    low quality, low C0 domains (math) have high quality but SICA=SC anyway.'\n\n\n## registry (completed experiments)\n\n- exp_id: crd_folio_main\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    divergence_rate: 0.422\n    diagnosis_rate: 0.872\n    error_types: 4\n    directed_advantage_pp: 4.7\n    directed_p_value: 0.63\n    localization_accuracy: 0.946\n    fol_accuracy: 0.789\n    code_accuracy: 0.598\n    oracle_accuracy: 0.878\n    pipeline_accuracy: 0.814\n    baseline_accuracy: 0.74\n    cost_multiplier: 5.76\n    dataset: FOLIO\n    n: 204\n- exp_id: smoke-test-5q\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: sica_smoke_5q\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    sica_accuracy: 0.8\n    sc_accuracy: 0.8\n    extraction_rate: 1\n    problems_with_contradictions: 1\n    total_problems: 5\n    total_time_s: 3505\n    avg_time_per_problem_s: 701\n    per_problem:\n    - id: algebra/2470\n      level: 1\n      sica_correct: true\n      sc_correct: true\n      constraints: 27\n      unique: 9\n      excluded: 0\n    - id: prealgebra/65\n      level: 2\n      sica_correct: true\n      sc_correct: true\n      constraints: 26\n      unique: 2\n      excluded: 0\n    - id: number_theory/847\n      level: 3\n      sica_correct: true\n      sc_correct: true\n      constraints: 21\n      unique: 11\n      excluded: 0\n      note: 14 JSON parse failures, 1693s\n    - id: precalculus/1199\n      level: 4\n      sica_correct: false\n      sc_correct: false\n      constraints: 35\n      unique: 6\n      excluded: 0\n      note: graph-reading problem, model cannot see image\n    - id: algebra/2277\n      level: 5\n      sica_correct: true\n      sc_correct: true\n      constraints: 60\n      unique: 6\n      satisfied: 3\n      excluded: 3\n- exp_id: sica_temp_diversity\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    temperatures_tested:\n    - 0.7\n    - 0.9\n    - 1\n    problems_tested: 3\n    problems_with_divergence: 0\n    finding: QwQ-32B produces zero answer divergence at all temperatures on MATH L4-5.\n      Reasoning model's deterministic chain dominates sampling randomness.\n    max_tokens_issue: 4096 tokens insufficient for some L5 problems (truncation)\n    recommendation: Use AIME 2024 (harder, ~79.5% acc) or non-reasoning model for\n      trace diversity\n- exp_id: mvp_math50_t07\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: sica_aime30_t07\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: sica_aime30_v2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    progress: 4/30\n    sica_accuracy_interim: 3/4 (75%)\n    sc_accuracy_interim: 3/4 (75%)\n    avg_time_per_problem_s: 557\n    p2_z3_error: Z3Exception on z3_maxsat.py:163, 0 constraints extracted\n    p5_vllm_stuck: vLLM timeout since ~22:11, retried multiple rounds\n    issue: vLLM service likely crashed or OOM at Problem 5\n    analysis_contradiction_rate_aime: 50% (2/4)\n    analysis_contradiction_rate_math: 20% (1/5)\n    analysis_unique_constraints_per_problem_aime: 18.7\n    analysis_exclusion_rate: 10.7%\n    analysis_sica_sc_agreement: 9/9 (100%)\n    analysis_signal: weak positive - mechanism works but SC too unanimous to flip\n    analysis_p2_failure: 0 constraints, 0 votes - answer extraction failure\n- exp_id: sica_aime30_v3\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    progress: 22/30\n    sica_accuracy_interim: 16/22 (72.7%)\n    sc_accuracy_interim: 16/22 (72.7%)\n    sica_sc_gap_pp: 0\n    avg_time_per_problem_s: 645.9\n    runtime_h: 5.9\n    remaining_problems: 8\n    vote_diversity_analysis:\n      valid_problems: 16\n      total_problems: 22\n      multi_candidate_rate: 0\n      zero_vote_problems: 6\n      zero_vote_indices:\n      - 1\n      - 7\n      - 8\n      - 10\n      - 13\n      - 14\n      constraints_extracted: 19/22\n      exclusion_rate: 0.387\n      conclusion: All 16 valid problems have exactly 1 candidate answer. SICA≡SC structurally.\n        MaxSAT exclusion operates but cannot change final selection with only 1 candidate.\n    process_status: gone (cron miss 1/5)\n- exp_id: sica_proofwriter30\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    sica_accuracy: 0/30 (0.0%)\n    sc_accuracy: 0/30 (0.0%)\n    sica_sc_gap_pp: 0\n    total_wall_time_s: 238.9\n    total_wall_time_min: 4\n    avg_time_per_problem_s: 8\n    traces_generated: 0\n    constraints_extracted: 0\n    traces_with_constraints: 0\n    unique_constraints: 0\n    maxsat_satisfied: 0\n    maxsat_excluded: 0\n    multi_candidate_rate: N/A (no traces generated)\n    vote_diversity: N/A\n    z3_errors: 0\n    z3_timeouts: 0\n    problems_with_contradiction: 0\n    problems_with_votes: 0\n    failure_mode: ALL_400_BAD_REQUEST\n    failure_count: 30/30\n    root_cause: max_tokens=16384 equals max_model_len=16384, leaving 0 tokens for\n      prompt input. Every API call returns 400.\n- exp_id: sica_folio30\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: sica_proofwriter30_v2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: sica_d016_c0_precheck\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    multi_candidate_rate_combined: 0.46\n    multi_candidate_rate_folio: 0.4\n    multi_candidate_rate_proofwriter: 0.5\n    sc_accuracy_combined: 0.73\n    sc_accuracy_folio: 0.8\n    sc_accuracy_proofwriter: 0.69\n    n_problems: 26\n    n_folio: 10\n    n_proofwriter: 16\n    K: 6\n    T: 0.7\n    total_time_s: 280\n    c0_gate: PASS (46% >= 20%)\n    model: Qwen2.5-14B-Instruct\n    vllm_gpu_mem_gib: 27.6\n    smoke_test: 2 problems end-to-end OK, constraints 21-26 per problem\n- exp_id: sica_d012_14b\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    sica_accuracy: 0.7333\n    sc_accuracy: 0.7\n    sica_sc_gap_pp: 3.3\n    c0_multi_candidate_rate: 0.5333\n    c1_extraction_rate: 1\n    c2_contradiction_problems: 34\n    c3_gap_pp: 3.3\n    bootstrap_p: 0.2261\n    proofwriter_sica: 0.6667\n    proofwriter_sc: 0.6667\n    folio_sica: 0.8\n    folio_sc: 0.7333\n    total_constraints_raw: 5849\n    total_constraints_unique: 1735\n    maxsat_exclusion_rate: 0.0259\n    wall_time_min: 58.3\n    d012_verdict: ALL_PASS\n- exp_id: sica_expanded_14b\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    sica_accuracy: 0.765\n    sc_accuracy: 0.762\n    sica_sc_gap_pp: 0.3\n    n_problems: 804\n    multi_candidate_rate: 0.3818\n    folio_sica: 0.794\n    folio_sc: 0.794\n    folio_gap_pp: 0\n    folio_n: 204\n    proofwriter_sica: 0.755\n    proofwriter_sc: 0.752\n    proofwriter_gap_pp: 0.3\n    proofwriter_n: 600\n    extraction_rate: 0.89\n    answer_extraction_rate: 1\n    contradiction_rate: 0.022\n    problems_with_contradictions: 331\n    truncated_traces: 0\n    wall_time_min: 826\n- exp_id: sica_k_sensitivity_14b\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    K6_sica: 0.733\n    K6_sc: 0.733\n    K6_gap_pp: 0\n    K8_sica: 0.733\n    K8_sc: 0.75\n    K8_gap_pp: -1.7\n    K11_sica: 0.733\n    K11_sc: 0.733\n    K11_gap_pp: 0\n    K12_sica: 0.7\n    K12_sc: 0.75\n    K12_gap_pp: -5\n    K16_sica: 0.717\n    K16_sc: 0.75\n    K16_gap_pp: -3.3\n    K20_sica: 0.7\n    K20_sc: 0.733\n    K20_gap_pp: -3.3\n    all_K_sica_leq_sc: true\n    larger_K_degrades_sica: true\n- exp_id: sica_constraint_ablation_013\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    maxsat_accuracy: 0.7649\n    count_only_accuracy: 0.7662\n    random_weight_accuracy: 0.7587\n    sc_baseline_accuracy: 0.7624\n    n_problems: 804\n    maxsat_correct: 615\n    count_only_correct: 616\n    random_weight_correct: 610\n    sc_correct: 613\n    agreement_maxsat_vs_countonly: 803/804\n    agreement_maxsat_vs_randomwt: 785/804\n    agreement_maxsat_vs_sc: 773/804\n    agreement_countonly_vs_randomwt: 786/804\n    agreement_countonly_vs_sc: 774/804\n    agreement_randomwt_vs_sc: 764/804\n    mcnemar_p_all_gt_0.7: true\n- exp_id: exp-005\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    qwq_aggregate_c0_nominal_pct: 10.3\n    qwq_aggregate_c0_effective_pct: 2.6\n    qwen14b_c0_pct: 46\n    diversity_ratio_effective: 17.7\n    aime_delta_pp: 0\n    proofwriter_delta_pp: -5.9\n    aime_n: 22\n    proofwriter_n: 17\n    temp_diversity_n: 5\n    folio_n: 2\n    total_problems: 46\n    c0_threshold: 20\n    qwq_below_threshold: true\n- exp_id: exp-011-llama8b\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp-016-weighted-sc\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    sica_accuracy: 0.7649\n    sc_uniform_accuracy: 0.7624\n    inv_length_accuracy: 0.7674\n    length_weighted_accuracy: 0.7525\n    constraint_count_accuracy: 0.7525\n    inv_length_vs_sc_p: 0.453\n    length_vs_sc_p: 0.153\n    inv_length_vs_sica_p: 0.864\n    length_vs_sica_p: 0.066\n    n_problems: 804\n    all_nonsignificant: true\n- exp_id: exp-010-mistral\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp-011-llama8b-v2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp-017-strategyqa\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp-018-arc\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp-010-mistral-v2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp-017-strategyqa-v2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp-017-strategyqa-v3\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n: 60\n    k: 12\n    sica_accuracy: 0.5667\n    sc_accuracy: 0.5333\n    delta_pp: 3.33\n    mcnemar_chi2: 0.5\n    mcnemar_p: n.s.\n    bootstrap_ci_95:\n    - 0\n    - 8.33\n    bootstrap_p_delta_le_0: 0.1346\n    multi_candidate_rate: 0.1\n    contradiction_detected: 5\n    extraction_rate_problem: 1\n    extraction_rate_trace: 0.704\n    discordant_sica_wins: 2\n    discordant_sc_wins: 0\n- exp_id: pilot-constraint-filtering\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    n: 43\n    thresholds_tested:\n    - 1\n    - 2\n    - 3\n    - 5\n    - 7\n    best_gap_pp: 2.33\n    best_T: 1\n    sica_T1: 0.7674\n    sc: 0.7442\n    T5_gap: 0\n    T7_gap: 0\n    discriminative_ratio_count: 0.115\n    discriminative_ratio_weight: 0.372\n    effective_flip_rate: 0.174\n    multi_answer_problems: 23\n    unanimous_problems: 20\n    problems_disc_favors_different: 4\n- exp_id: exp-018-arc-v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n: 60\n    k: 12\n    sica_accuracy: 0.95\n    sc_accuracy: 0.9667\n    delta_pp: -1.67\n    multi_candidate_rate: 0.05\n    extraction_rate: 1\n    contradiction_detected: 3\n    discordant_sica_wins: 0\n    discordant_sc_wins: 1\n    dataset: ARC-Challenge\n    model: Qwen2.5-14B-Instruct\n- exp_id: exp-011-llama8b-v3\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n: 60\n    k: 12\n    sica_accuracy: 0.6667\n    sc_accuracy: 0.6\n    delta_pp: 6.67\n    multi_candidate_rate: 0.6167\n    extraction_rate: 0.8556\n    answer_extraction_rate: 0.8958\n    contradiction_rate: 0.0527\n    problems_with_contradictions: 43\n    truncated_traces: 44\n    discordant_sica_wins: 5\n    discordant_sc_wins: 1\n    mcnemar_p: 0.2188\n    proofwriter_sica: 0.6333\n    proofwriter_sc: 0.6\n    proofwriter_delta_pp: 3.33\n    folio_sica: 0.7\n    folio_sc: 0.6\n    folio_delta_pp: 10\n    model: LLaMA-3.1-8B-Instruct\n    dataset: D012\n    wall_time_min: 66.4\n- exp_id: pilot-contrastive-prompt\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp-010-mistral-v3\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    n: 60\n    k: 12\n    sica_accuracy: 0.4833\n    sc_accuracy: 0.4833\n    delta_pp: 0\n    multi_candidate_rate: 0.5\n    extraction_rate: 0.8819\n    answer_extraction_rate: 1\n    contradiction_rate: 0.0562\n    discordant_sica_wins: 2\n    discordant_sc_wins: 2\n    mcnemar_p: 1\n    proofwriter_sica: 0.4\n    proofwriter_sc: 0.4\n    proofwriter_delta_pp: 0\n    folio_sica: 0.5667\n    folio_sc: 0.5667\n    folio_delta_pp: 0\n    truncated_traces: 0\n    model: Mistral-7B-Instruct-v0.3\n    dataset: D012\n- exp_id: exp-019-llama8b-strategyqa-200\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    n: 200\n    k: 12\n    sica_accuracy: 0.74\n    sc_accuracy: 0.72\n    delta_pp: 2\n    multi_candidate_rate: 0.41\n    mcnemar_p: 0.424\n    bootstrap_ci_95:\n    - -1.5\n    - 5.5\n    bootstrap_p_delta_le_0: 0.12\n    discordant_sica_wins: 9\n    discordant_sc_wins: 5\n    discordant_total: 14\n    discordant_rate: 0.07\n    sc_unanimous_rate: 0.545\n    model: LLaMA-3.1-8B-Instruct\n    dataset: StrategyQA\n    wall_time_min: 52\n- exp_id: exp-020-llama8b-folio-204\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    n: 204\n    k: 12\n    sica_accuracy: 0.608\n    sc_accuracy: 0.632\n    delta_pp: -2.45\n    mcnemar_p: 0.2668\n    bootstrap_ci_95:\n    - -5.88\n    - 0.98\n    bootstrap_p_sica_ge_sc: 0.1\n    discordant_sica_wins: 4\n    discordant_sc_wins: 9\n    discordant_total: 13\n    discordant_rate: 0.064\n    multi_candidate_rate: 0.618\n    extraction_rate: 0.942\n    answer_extraction_rate: 0.951\n    contradiction_rate: 0.062\n    both_wrong: 71\n    model: LLaMA-3.1-8B-Instruct\n    dataset: FOLIO-204\n    wall_time_min: 131.7\n- exp_id: exp-009-overhead-analysis\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n: 804\n    mean_total_wall_s: 61.6\n    mean_trace_gen_s: 31.6\n    trace_gen_pct: 51.3\n    mean_extract_s: 29\n    extract_pct: 47\n    mean_dedup_s: 1\n    dedup_pct: 1.6\n    mean_maxsat_s: 0.003\n    maxsat_pct: 0.005\n    sica_overhead_s: 30\n    sica_overhead_pct: 48.7\n    pw_overhead_pct: 51.3\n    folio_overhead_pct: 38.6\n    p50_overhead_pct: 48.9\n    p90_overhead_pct: 57.6\n- exp_id: exp-014-deepseek-r1-7b\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    n: 60\n    k: 12\n    sica_accuracy: 0.6833\n    sc_accuracy: 0.7167\n    delta_pp: -3.33\n    multi_candidate_rate: 0.583\n    extraction_rate: 0.839\n    answer_extraction_rate: 0.939\n    truncated_traces: 72\n    contradiction_rate: 0.037\n    wall_time_min: 100.3\n    mcnemar_p: 0.4795\n    discordant_sica_wins: 0\n    discordant_sc_wins: 2\n    model: DeepSeek-R1-Distill-Qwen-7B\n    dataset: D012\n- exp_id: temperature-ablation-t03\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    n: 60\n    k: 12\n    sica_accuracy: 0.7333\n    sc_accuracy: 0.7333\n    delta_pp: 0\n    multi_candidate_rate: 0.3\n    discordant_total: 0\n    model: Qwen2.5-14B-Instruct\n    dataset: D012\n    temperature: 0.3\n- exp_id: temperature-ablation-t05\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    n: 60\n    k: 12\n    sica_accuracy: 0.7667\n    sc_accuracy: 0.7667\n    delta_pp: 0\n    multi_candidate_rate: 0.383\n    discordant_total: 0\n    model: Qwen2.5-14B-Instruct\n    dataset: D012\n    temperature: 0.5\n- exp_id: temperature-ablation-t10\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    n: 60\n    k: 12\n    sica_accuracy: 0.75\n    sc_accuracy: 0.75\n    delta_pp: 0\n    multi_candidate_rate: 0.433\n    discordant_total: 0\n    model: Qwen2.5-14B-Instruct\n    dataset: D012\n    temperature: 1\n- exp_id: exp-021-oracle-folio\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n: 204\n    k: 12\n    oracle_sica_accuracy: 0.8824\n    sc_accuracy: 0.7941\n    sica_self_accuracy: 0.7941\n    oracle_vs_sc_delta_pp: 8.82\n    oracle_vs_sica_delta_pp: 8.82\n    mcnemar_p_oracle_vs_sc: 6.15e-05\n    z3_gold_agreement: 0.946\n    fol_parse_success: 1\n    model: Qwen2.5-14B-Instruct\n    dataset: FOLIO-204\n    constraint_source: gold FOL annotations\n- exp_id: exp-012-gsm8k-pilot\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    n: 30\n    k: 12\n    sica_accuracy: 0.9667\n    sc_accuracy: 0.9667\n    delta_pp: 0\n    multi_candidate_rate: 0.133\n    extraction_success_rate: 0.147\n    model: Qwen2.5-14B-Instruct\n    dataset: GSM8K\n    temperature: 0.7\n- exp_id: exp-004-qwen7b\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    n: 60\n    k: 12\n    sica_accuracy: 0.6833\n    sc_accuracy: 0.6833\n    delta_pp: 0\n    multi_candidate_rate: 0.433\n    extraction_rate: 0.9417\n    answer_extraction_rate: 1\n    contradiction_rate: 0.0274\n    discordant_sica_wins: 2\n    discordant_sc_wins: 2\n    mcnemar_p: 1\n    wall_time_s: 1838\n    truncated_traces: 0\n    model: Qwen2.5-7B-Instruct\n    dataset: D012\n    temperature: 0.7\n    folio_sica: 0.7667\n    folio_sc: 0.7333\n    folio_n: 30\n    proofwriter_sica: 0.6\n    proofwriter_sc: 0.6333\n    proofwriter_n: 30\n- exp_id: temperature-ablation-t07\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    n: 60\n    k: 12\n    sica_accuracy: 0.7167\n    sc_accuracy: 0.75\n    delta_pp: -3.33\n    multi_candidate_rate: 0.4\n    extraction_rate: 0.9208\n    answer_extraction_rate: 1\n    contradiction_rate: 0.022\n    discordant_sica_wins: 0\n    discordant_sc_wins: 2\n    truncated_traces: 0\n    model: Qwen2.5-14B-Instruct\n    dataset: D012\n    temperature: 0.7\n    proofwriter_sica: 0.6333\n    proofwriter_sc: 0.7\n    proofwriter_n: 30\n    folio_sica: 0.8\n    folio_sc: 0.8\n    folio_n: 30\n    wall_time_s: 3498.3\n- exp_id: exp-022-oracle-proofwriter\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n: 600\n    k: 12\n    oracle_sica_accuracy: 0.8667\n    sc_accuracy: 0.7517\n    sica_self_accuracy: 0.755\n    oracle_vs_sc_delta_pp: 11.5\n    mcnemar_p_oracle_vs_sc: 9.21e-15\n    z3_gold_agreement: 0.9714\n    z3_gold_agree_n: 577\n    z3_gold_total: 594\n    parse_errors: 6\n    parse_error_rate: 0.01\n    solver_errors: 0\n    solver_total: 7128\n    relneg_oracle: 0.7786\n    relneg_sc: 0.6\n    relneg_delta_pp: 17.86\n    relnoneg_oracle: 0.7945\n    relnoneg_sc: 0.6644\n    relnoneg_delta_pp: 13.01\n    attnoneg_oracle: 0.961\n    attnoneg_sc: 0.8701\n    attnoneg_delta_pp: 9.09\n    attneg_oracle: 0.9188\n    attneg_sc: 0.85\n    attneg_delta_pp: 6.87\n    model: Qwen2.5-14B-Instruct\n    dataset: ProofWriter-OWA-D5-600\n    constraint_source: gold DSL (raw_logic_programs)\n- exp_id: exp-023-discriminative-rate\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n_total: 804\n    n_multi_candidate: 307\n    source_disc_rate_weight: 0.392\n    source_disc_rate_weight_ci95:\n    - 0.387\n    - 0.398\n    source_disc_rate_count_est: 0.121\n    source_disc_rate_count_ci95:\n    - 0.12\n    - 0.123\n    z3_semantic_disc_rate: 0.082\n    z3_semantic_disc_ci95:\n    - 0.076\n    - 0.088\n    problems_with_disc: 289\n    problems_with_disc_rate: 0.941\n    pw_source_disc_weight: 0.364\n    folio_source_disc_weight: 0.54\n    pw_n_multi: 235\n    folio_n_multi: 72\n    pilot_rate_reported_count: 0.115\n    pilot_rate_reported_weight: 0.372\n    pilot_validation_weight: 0.376\n    pilot_delta_pp: 0.38\n    z3_answer_assertions: 642\n    z3_total_unique_constraints: 7844\n    model: Qwen2.5-14B-Instruct\n    dataset: FOLIO+ProofWriter-804\n- exp_id: exp-026-folio204-trace-regen\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n: 204\n    k: 12\n    sica_accuracy: 0.7451\n    sc_accuracy: 0.75\n    delta_pp: -0.49\n    extraction_rate: 0.9853\n    model: Qwen2.5-14B-Instruct\n    dataset: FOLIO-204\n    temperature_trace: 0.7\n    temperature_extraction: 0.3\n    wall_time_h: 2.5\n- exp_id: exp-027-qwen3-14b-non-thinking\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n: 204\n    k: 12\n    sica_accuracy: 0.8431\n    sc_accuracy: 0.8382\n    delta_pp: 0.49\n    extraction_rate: 0.995\n    contradiction_rate: 0.0283\n    problems_with_contradictions: 69\n    total_constraints: 16153\n    unique_constraints: 7031\n    wall_time_s: 11017\n    model: Qwen3-14B\n    dataset: FOLIO-204\n    mode: non-thinking\n- exp_id: exp-028-qwen3-14b-thinking\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: exp-029-contrastive-folio204\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    contrastive_accuracy: 0.7253\n    sc_accuracy: 0.7363\n    delta_pp: -1.1\n    discriminative_rate: 0.0604\n    discriminative_count: 11\n    n: 182\n    recovery_rate_pct: -8.3\n    mcnemar_chi2: 0.1\n    mcnemar_p: 0.7518\n    cont_only_correct: 4\n    sc_only_correct: 6\n    both_correct: 128\n    both_wrong: 44\n    supporting_pct: 43.2\n    opposing_pct: 56.8\n    avg_constraints_per_problem: 24.4\n    avg_unique_per_problem: 10.4\n    wall_time_min: 47.2\n- exp_id: exp-030-crossmodel-mistral-folio204\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    n: 204\n    k: 12\n    crossmodel_sica_accuracy: 0.75\n    sc_accuracy: 0.75\n    delta_pp: 0\n    discriminative_rate: 0\n    recovery_rate: 0\n    model_extraction: Mistral-7B-Instruct-v0.3\n    model_traces: Qwen2.5-14B-Instruct\n    dataset: FOLIO-204\n- exp_id: exp-031-oracle-folio-regen\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n: 204\n    k: 12\n    oracle_sica_accuracy: 0.8971\n    sc_accuracy: 0.7549\n    sica_self_accuracy: 0.7451\n    oracle_vs_sc_delta_pp: 14.22\n    oracle_vs_sica_delta_pp: 15.2\n    mcnemar_p_oracle_vs_sc: 2.0024e-07\n    mcnemar_b_c:\n      b_oracle_right_sc_wrong: 29\n      c_oracle_wrong_sc_right: 0\n    z3_gold_agreement: 0.951\n    z3_gold_agree_n: 194\n    z3_in_candidates_n: 178\n    fol_parse_success: 1\n    model: Qwen2.5-14B-Instruct\n    dataset: FOLIO-204\n    constraint_source: gold FOL annotations\n    traces_source: exp-026-folio204-trace-regen\n- exp_id: exp-033-qwen3-pw600-nonthinking\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp-035\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    n_problems: 203\n    sc_accuracy: 77.34\n    sica_accuracy: 76.85\n    delta_pp: -0.49\n    sica_correct: 156\n    sc_correct: 157\n    mcnemar_discordant_b: 1\n    mcnemar_discordant_c: 2\n    mcnemar_p_value: 1\n    c0_non_unanimous_rate: 0.5517\n    extraction_rate: 98.19\n    contradiction_rate: 1.58\n    problems_with_contradictions: 60\n    total_constraints: 12950\n    unique_constraints: 6515\n    dedup_ratio: 50.3\n    wall_time_min: 78.2\n    avg_per_problem_s: 23.1\n- exp_id: exp-034\n  name: ''\n  status: DEPLOYED\n  conclusion: failed\n  metrics:\n    n_problems: 93\n    n_target: 600\n    completion_pct: 15.5\n    sica_accuracy: 77.42\n    sc_accuracy: 74.19\n    delta_pp: 3.23\n    sica_correct: 72\n    sc_correct: 69\n    mcnemar_discordant_b: 6\n    mcnemar_discordant_c: 3\n    mcnemar_p_value: 0.5078\n    c0_non_unanimous_rate: 0.581\n    avg_majority_frac: 0.8324\n    extraction_rate: 99.19\n    contradiction_rate: 11.83\n    problems_with_contradictions: 11\n    avg_unique_constraints: 35.6\n    total_constraints: 14437\n    unique_constraints: 3308\n    dedup_ratio: 22.9\n    k: 12\n    level: OWA-D5\n    gt_distribution:\n      'True': 32\n      'False': 28\n      Unknown: 33\n    wall_time_s: 6086.4\n    status_note: 'INCOMPLETE: crashed at 93/600 (python not found after conda env\n      lost)'\n- exp_id: exp-007-qwen72b-awq\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp-004-qwen7b-rerun\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp-036-z3-feedback-folio204\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    z3fb_sica_accuracy: 0.775\n    vanilla_sica_accuracy: 0.745\n    sc_accuracy: 0.75\n    z3fb_vs_vanilla_delta: 0.03\n    unsat_traces: 22\n    total_traces: 2448\n    unsat_rate: 0.009\n    unsat_resolve_rate: 0.864\n    problems_flipped: 0\n    real_impact: 0\n- exp_id: exp-033\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n_problems: 204\n    sica_accuracy: 59.31\n    sc_accuracy: 54.41\n    delta_pp: 4.9\n    sica_correct: 121\n    sc_correct: 111\n    mcnemar_discordant_b: 12\n    mcnemar_discordant_c: 2\n    mcnemar_p_value: 0.0129\n    c0_non_unanimous_rate: 0.8137\n    avg_majority_frac: 0.7515\n    extraction_rate: 97.14\n    contradiction_rate: 3.5\n    problems_with_contradictions: 128\n    avg_unique_constraints: 39.3\n    maxsat_mean_sat_ratio: 0.9609\n    total_constraints: 14042\n    unique_constraints: 8021\n    wall_time_min: 81.4\n    k: 12\n- exp_id: exp-039-14b-pw600-16639\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp-040-qwen3-pw600-16639\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp-041-14b-folio204-16639\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    n: 204\n    dataset: FOLIO-204\n    model: Qwen2.5-14B-Instruct\n    k: 12\n    sica_accuracy: 75.49\n    sc_accuracy: 77.45\n    delta_pp: -1.96\n    sica_correct: 154\n    sc_correct: 158\n    mcnemar_discordant_b: 0\n    mcnemar_discordant_c: 4\n    mcnemar_p_value: 0.125\n    extraction_rate: 0.98\n    contradiction_rate: 0.0097\n- exp_id: exp-038-14b-logiqa200-16639\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    n: 200\n    dataset: LogiQA-200\n    model: Qwen2.5-14B-Instruct\n    k: 12\n    sica_accuracy: 78\n    sc_accuracy: 78.5\n    delta_pp: -0.5\n    mcnemar_p: 1\n    sica_correct: 156\n    sc_correct: 157\n    discordant_b: 1\n    discordant_c: 2\n    both_correct: 155\n    both_wrong: 42\n    extraction_rate: 0.864\n    fail_empty_rate: 0.122\n    avg_unique_constraints: 26.7\n    contradiction_rate: 0.008\n    wall_time_min: 126.8\n- exp_id: exp-042-premise-formalization\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp-043-consistency-filtering\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    sc_accuracy: 0.75\n    sica_t1_all: 0.7794\n    sica_t4: 0.75\n    sica_t6: 0.7549\n    sica_t8: 0.7549\n    avg_unique_constraints: 13.2\n    avg_filtered_t4: 1.8\n    avg_filtered_t6: 0.8\n    avg_filtered_t8: 0.3\n- exp_id: exp-044-icl-oracle\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp-045-backward-verification\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics: {}\n- exp_id: exp-036b-cross-trace-unsat\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    cross_unsat_rate_pair: 0.087\n    cross_unsat_rate_problem: 0.107\n    within_trace_unsat_rate: 0.009\n    unsat_pairs: 11\n    total_pairs: 126\n    problems_with_unsat: 9\n    multi_answer_problems: 84\n    single_answer_skip: 120\n    zero_shared_var_pairs_pct: 0.564\n    avg_shared_vars: 2.7\n    false_true_unsat_rate: 0.467\n    sica_cross_ut_accuracy: 0.745\n    sc_accuracy: 0.75\n    accuracy_impact: 0\n- exp_id: exp-042b-premise-formal\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp-044b-icl-oracle\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    n: 199\n    dataset: FOLIO-199\n    model: Qwen2.5-14B-Instruct\n    k: 12\n    sica_accuracy: 74.87\n    sc_accuracy: 74.37\n    delta_pp: 0.5\n    sica_correct: 149\n    sc_correct: 148\n    icl_examples: 5\n    extraction_failure_rate: 0.008\n- exp_id: exp-045b-backward-verify\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: exp-046-mistral-pw600\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    n: 600\n    sc_accuracy: 39.33\n    sica_accuracy: 36.5\n    delta_pp: -2.83\n    sc_wins: 30\n    sica_wins: 13\n    mcnemar_p: 0.0095\n    significant: true\n    dataset: ProofWriter-D5-600\n    model: Mistral-7B-Instruct-v0.3\n- exp_id: exp-028b-qwen3-thinking-folio204\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: exp-048-llama8b-pw600\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp-049-mistral-logiqa200\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp-050-mistral-icl-oracle-folio199\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp-050b-mistral-icl-oracle\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    n: 199\n    sc_accuracy: 57.79\n    sica_accuracy: 54.27\n    delta_pp: -3.52\n    sc_correct: 115\n    sica_correct: 108\n    discordant_b: 6\n    discordant_c: 13\n    mcnemar_p: 0.167\n    significant: false\n    wall_time_min: 93.8\n    extraction_success: 2333\n    extraction_fail: 55\n    per_answer:\n      'True':\n        n: 70\n        sica_acc: 50\n        sc_acc: 54.29\n      'False':\n        n: 61\n        sica_acc: 36.07\n        sc_acc: 44.26\n      Unknown:\n        n: 68\n        sica_acc: 75\n        sc_acc: 73.53\n- exp_id: exp-049b-mistral-logiqa200\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    n: 200\n    sc_accuracy: 51\n    sica_accuracy: 51.5\n    delta_pp: 0.5\n    sc_correct: 102\n    sica_correct: 103\n    discordant_b: 6\n    discordant_c: 5\n    mcnemar_p: 1\n    significant: false\n    wall_time_min: 78.6\n    extraction_rate: 0.9725\n    total_constraints: 10659\n    unique_constraints: 8934\n    contradiction_rate: 0.0196\n- exp_id: exp-051-mistral-k-sensitivity\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp-052-mistral-folio204-seed123\n  name: ''\n  status: QUEUED\n  conclusion: ''\n  metrics: {}\n- exp_id: exp-053-mistral-folio204-seed456\n  name: ''\n  status: QUEUED\n  conclusion: ''\n  metrics: {}\n- exp_id: exp-052\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n: 204\n    sc_accuracy: 53.9\n    sica_accuracy: 57.4\n    sc_correct: 110\n    sica_correct: 117\n    delta_pp: 3.43\n    discordant_b: 8\n    discordant_c: 1\n    extraction_rate: 0.971\n    contradiction_rate: 0.034\n    wall_time_min: 81.9\n    mcnemar_p: 0.0391\n    significant: true\n- exp_id: exp-053\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    n: 204\n    sc_accuracy: 56.37\n    sica_accuracy: 55.88\n    sc_correct: 115\n    sica_correct: 114\n    delta_pp: -0.49\n    discordant_b: 2\n    discordant_c: 3\n    extraction_rate: 0.97\n    contradiction_rate: 0.033\n    wall_time_min: 80.8\n    mcnemar_p: 1.0\n    significant: false\n- exp_id: exp-054-mistral-folio204-t10\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    n: 204\n    sc_accuracy: 54.9\n    sica_accuracy: 55.4\n    delta_pp: 0.49\n    discordant_b: 5\n    discordant_c: 4\n    mcnemar_chi2: 0.1111\n    mcnemar_p: 0.7389\n    extraction_rate: 97.3\n    contradiction_rate: 3\n    wall_time_min: 83\n- exp_id: exp-055-multitemp-mistral-folio\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp-057-mistral-folio204-t03\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp-058-mistral-folio204-t05\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: median\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-19T03:52:54.534Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-19T03:52:54.534Z",
  "sessionId": "94c4266a-dd51-40f0-bc57-040b308715ff"
}
```

---

## Round 1

25 recorded events

### User

_source line 3 · 2026-05-19T03:52:54.556Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：

含义：Dual Bottleneck 方向成立但 Eff-K 预测力有噪声。K/T curves 有 outlier 需解释。需弱化 'predictor' 为 'necessary condition'，重心转向 oracle gap + remediation failures。Findings 可达。
核心假设：['exp-051 K sensitivity 大致呈 inverted-U 但有 1-2 个 non-monotonic 点 (如 K=8 高于 K=12 或 K=16 反弹)', 'T sensitivity 方向正确 (T=0.7 peak) 但 T=0.3 或 T=0.5 有意外正值 (如 T=0.3 ~+2pp)', 'exp-055 multi-temp 接近 0 但 CI 包含正值', 'Eff-K 跨模型方向正确 (Qwen→0, Mistral→positive) 但 seed 内和 condition 内 variance 大到无法做定量预测', 'exp-050b ICL complication 无法完全解释，需在 paper 中作为 limitation 处理']
关键指标范围：{'mistral_k_peak_delta_pp': [2.5, 5.0], 'mistral_k_k4_delta_pp': [-3.0, 3.0], 'mistral_k_k20_delta_pp': [-3.0, 3.0], 'mistral_k_inverted_u_visual': '大致 peak 在 K=10-14 但 1-2 点偏离趋势', 't03_delta_pp': [-2.0, 3.0], 't05_delta_pp': [-1.0, 4.0], 'multitemp_delta_pp': [-3.0, 1.5], 'effk_sc_joint_prediction_accuracy': '7-9/12 conditions 方向正确', 'estimated_reviewer_avg': [2.8, 3.2]}
叙事方向：弱化 Claim 1 措辞: Eff-K 从 "predictor" 降为 "necessary condition that interacts with SC"。 承认 seed variance 是 open question，明确表述为 "Eff-K explains cross-model variance; within-model variance remains dominated by stochastic factors"。 K/T sensitivity 如有 outlier，用 error bar / CI overlay 展示 noise level，frame 为 "directionally consistent despite noise"。 论文重心从 Condorcet 理论预测力 转向 oracle gap (最强证据, p=2e-7) + 9 remediation failures (breadth argument)。 Condorcet 框架降为 "explanatory lens" 而非 "predictive framework"。 exp-050b ICL complication 放 discussion 作为 future work。 投稿目标: Findings (≥3.0)。如 reviewers 认可 breadth of analysis 可能升 Main。


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
tier: median
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
  "promptId": "d07b33c5-7e32-4212-9636-fcf6c376c96b",
  "type": "user",
  "uuid": "390b432e-ee14-483a-bc30-7ef32d8ecda0",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3",
  "sessionId": "94c4266a-dd51-40f0-bc57-040b308715ff",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-19T03:52:54.554Z_

```json
{
  "parentUuid": "390b432e-ee14-483a-bc30-7ef32d8ecda0",
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
  "uuid": "da472c54-ffd4-4fb1-b451-96792f146596",
  "timestamp": "2026-05-19T03:52:54.554Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3",
  "sessionId": "94c4266a-dd51-40f0-bc57-040b308715ff",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-19T03:52:54.554Z_

```json
{
  "parentUuid": "da472c54-ffd4-4fb1-b451-96792f146596",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "5d6efba2-79a7-440b-9c0a-82c6dbe00c34",
  "timestamp": "2026-05-19T03:52:54.554Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3",
  "sessionId": "94c4266a-dd51-40f0-bc57-040b308715ff",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：Dual Bottleneck 方向成立但 Eff-K 预测力有噪声。K/T curves 有 outlier 需解释。需弱化 'predictor' 为 'necessary condition'，重心转向 oracle gap + remediation failures。Findings 可达。 核…",
  "leafUuid": "5d6efba2-79a7-440b-9c0a-82c6dbe00c34",
  "sessionId": "94c4266a-dd51-40f0-bc57-040b308715ff"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Condorcet independence analysis of self-consistency trace aggregation",
  "sessionId": "94c4266a-dd51-40f0-bc57-040b308715ff"
}
```

---

### Assistant

_source line 8 · 2026-05-19T04:02:01.243Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed imagined/predicted experimental data for all "planned" or "running/queued" experiments in the experiment_plan, based on the "median" tier definition provided. Let me go through each experiment and generate realistic predicted results.

Let me first identify all experiments that need predictions. Looking at the experiment_plan and registry:

**Planned experiments (from experiment_plan):**
- exp-002: sica_k_ablation_14b (K sensitivity on D012 60q) - planned
- exp-003: tiebreak_baseline_analysis - planned (but note says completed as CPU analysis)


- exp-004: sica_7b_scaling - planned (though registry shows exp-004-qwen7b already done)
- exp-005: qwq_32b_operating_regime - planned (registry shows exp-005 completed)
- exp-006: c0_diagnostic_validation - planned
- exp-007: sica_72b_awq - planned (registry shows exp-007-qwen72b-awq done/failed)
- exp-008: constraint_quality_case_studies - planned
- exp-009: overhead_analysis - planned (registry shows exp-009-overhead-analysis completed)
- exp-010: sica_mistral_7b - done
- exp-011: sica_llama_8b - planned (registry shows exp-011-llama8b-v3 done)
- exp-012: gsm8k_pilot_14b - planned (registry shows exp-012-gsm8k-pilot done)
- exp-013: constraint_ablation - planned (registry shows sica_constraint_ablation_013 done)
- exp-014: sica_deepseek_r1_llama_8b - planned (registry shows exp-014-deepseek-r1-7b done)
- exp-015: logic_lm_baseline - planned
- exp-016: weighted_sc_baseline - planned (registry shows exp-016-weighted-sc done)
- exp-017: sica_strategyqa_14b - planned (registry shows exp-017-strategyqa-v3 done)
- exp-018: sica_arc_challenge_14b - planned (registry shows exp-018-arc-v incomplete)
- exp-019: constraint_quality_correlation - planned

Looking at the registry entries, most of these planned experiments actually show completion status. I'm noticing a discrepancy between what's marked as planned in the experiment plan versus what's already finished in the registry. Several experiments like exp-039, exp-040, exp-048, exp-051, exp-055, exp-057, and exp-058 are currently running. I need to figure out which experiments are actually still in planned status versus which ones have already been executed or are actively running.

Let me identify the truly planned experiments from the experiment_plan that haven't been started yet: exp-002 (sica_k_ablation_14b), exp-003 (tiebreak_baseline_analysis), exp-004 (sica_7b_scaling), exp-005 (qwq_32b_operating_regime), exp-006 (c0_diagnostic_validation), exp-007 (sica_72b_awq), and exp-008 (constraint_quality_case).

Looking at the additional planned experiments in the list—exp-009 through exp-019—many of these show as completed in the registry under different versions or registry IDs, which creates some ambiguity about what the user actually wants. The instructions say to generate data for each planned experiment, but I need to clarify whether that means all experiments marked as "planned" status or only those that are genuinely outstanding and haven't been run yet. I need to generate imagined data for all the planned experiments listed in the experiment_plan, treating this as a complete hypothetical exercise where I'm creating median-tier predictions across the board, regardless of whether some experiments already have real registry data. I should also include the running experiments that aren't yet in the plan to get a full picture of what the median tier would look like. Looking at the median tier results, the oracle gap provides the strongest evidence for the findings, while the K/T curves show high seed variance with some outliers. The metric ranges across experiments show consistent patterns—Mistral's K sensitivity peaks around K=10-14, temperature effects vary between -2 to 4 percentage points, and the remediation failures across 9 cases support a breadth argument that could work as a Main finding if reviewers value that angle.

Now I'm moving through the planned experiments to generate predictions. I've already noted that the registry shows sica_k_sensitivity_14b is complete for the Qwen-14B model, confirming all K values stay below the sensitivity ceiling for the median tier.

For the tiebreak baseline analysis, the results are in—SICA's tiebreak strategy achieved 80% compared to random's 50%, so that's already done. The 7B scaling experiment with Qwen2.5 also finished with delta=0 and C0 at 43.3%, and the QwQ-32B operating regime test came back negative at 2.6% effective performance. Now I'm looking at the C0 diagnostic validation experiment, which focuses on CPU-only analysis comparing C0 performance across different conditions.

The 72B-AWQ scaling test with Qwen2.5 failed and still needs to be run, while the constraint quality case studies remain planned for qualitative analysis. The overhead analysis is already complete, and the LLaMA-3.1-8B experiment finished with a delta of +6.67 percentage points though the p-value of 0.22 suggests it's not statistically significant. I still need to check on the GSM8K pilot with the 14B model.

Looking at the completed experiments, the constraint ablation showed MaxSAT and count-only constraints perform equivalently, the DeepSeek-R1 variant actually decreased performance by 3.33 percentage points, and the weighted self-consistency baseline showed no significant improvements. The Logic-LM comparison is still pending, and I'm tracking the StrategyQA results which showed a +3.33 percentage point improvement.

Now I'm reviewing the remaining experiments that need predictions—there's a batch of eight running across different model configurations and parameter settings, including variants with different temperature values and token counts. I'm reconsidering something about how these fit together. I need to generate predictions for all planned experiments in the plan, including the ones currently running, since the user wants detailed data for each. For experiments already completed with real data, I'll note those as-is, but for the pending and running ones, I'll create realistic median-tier projections to show what the full paper narrative would look like. Let me just be comprehensive and generate predictions for everything that doesn't have final data. I'll also include running experiments.

Let me think about what median tier predictions would look like for each:

**exp-002: sica_k_ablation_14b (Qwen-14B, K=6,8,11,12,16,20, D012 60q)**
Already done in registry (sica_k_sensitivity_14b). Shows SICA ≤ SC at all K. In median tier, Qwen-14B has too low Eff-K for SICA to help. The actual results already align with median tier expectations.

Actually, let me just focus on experiments that are truly planned or running. The user probably wants a comprehensive picture.

Going through the experiment plan, I see most of these are already completed—Qwen-7B, QwQ-32B, the overhead analysis, LLaMA-8B, GSM8K, constraint ablation, DeepSeek-R1, weighted SC, StrategyQA, and ARC-Challenge all have results. The ones still pending are the C0 diagnostic, constraint quality case studies, Logic-LM baseline, and constraint quality correlation. The 72B AWQ experiment failed in the registry, so that's a dead end.

For the additional experiments listed—the PW600 variants and Mistral sensitivity tests—I should generate median-tier predictions since these haven't been run yet. I'll create YAML entries for all planned experiments with realistic imagined results that reflect what we'd expect from the median tier. The key insight is that Eff-K prediction works but has noise, and the K/T curves show outliers, so I should frame this as a necessary condition rather than a strict predictor. The main findings will focus on the oracle gap and why remediation attempts fail, which are achievable narratives.

Now I'm working through the experimental data systematically. The completed experiments from the registry show consistent patterns—SICA stays below SC for Qwen-14B across different K values, the tiebreak baseline achieves 80% accuracy versus 50% random, and the 7B scaling shows zero delta with a C0 of 43.3%. The QwQ-32B results are negative with very low C0 at 2.6%, and I'm moving into the diagnostic validation experiments next.

For the CPU analysis in exp-006, I need to examine how C0 relates to the SICA-SC gap—there's directional predictiveness but considerable noise in the median tier. The 72B AWQ experiment failed to register, but the pattern suggests high-SC models tend toward low C0 and SICA approximating SC. The constraint quality case studies will be qualitative, showing mixed results in the median tier with some meaningful constraints and others that are trivial. The overhead analysis is complete at 48.7%, and the LLaMA-8B results show a small positive delta of 6.67 percentage points that isn't statistically significant. The GSM8K pilot on 14B is registered with zero delta.

Now looking at the next batch: the constraint ablation shows MaxSAT performing similarly to count-only baselines. DeepSeek R1 with LLaMA-8B shows a slight negative delta of 3.33 percentage points. Logic-LM appears equivalent to SC in the median tier with no meaningful difference. The weighted SC baseline yields all non-significant results. StrategyQA on 14B shows a small positive delta of 3.33 percentage points that's not significant, while ARC Challenge on 14B shows a small negative delta of 1.67 percentage points with C0 at 5%. The constraint quality correlation analysis isn't complete yet but suggests an inverse relationship between C0 and quality that's noisy. I'm currently running the 14B experiment.

Moving forward, I'm testing PW600 with Qwen-14B using longer context—expecting similar performance to the expanded 14B variant but with better extraction. Qwen3 on PW600 should behave like the FOLIO version. LLaMA-8B on PW600 is expected to show moderate C0 with a small positive but non-significant delta. For the Mistral K sensitivity analysis on FOLIO, I'm varying K from 4 to 20 and seeing an inverted-U pattern peaking around K=10-14, though there are a couple of non-monotonic points. Still working through the multi-temperature Mistral FOLIO experiment.

Now I'm looking at temperature sensitivity across different settings—T=0.3 shows a median delta between -2.0 and 3.0, while T=0.5 ranges from -1.0 to 4.0. I need to draft the full YAML output with detailed result rationales for each experiment, and I should verify which running experiments aren't yet in the plan.

Looking at the registry, I have several running experiments that need predictions: the 14b and Qwen variants, the Llama 8B setup, the k-sensitivity test, and the multi-temperature ensemble along with the temperature variants. I also notice exp-052 and exp-053 are already completed in the registry even though they're queued, so I'll focus predictions on the truly running ones. The user wants detailed coverage of every planned experiment from the experiment_plan, so I'll organize the YAML by planned experiments first, then add running ones that aren't yet documented.

For the predictions, I need to stay consistent with median-tier performance: mistral_k_peak_delta_pp around 3.8pp, mistral_k_k values in the expected range, and similar patterns across the other models. I'll generate predictions for all 24 experiments total and let the user cross-reference with actual registry data where it exists. Looking at the Mistral K sensitivity results, I'm seeing a non-monotonic pattern where K=8 actually peaks higher than K=12, which is interesting since K=12 matches the exp-033 baseline. The performance then declines through K=16 before showing another uptick at K=20, suggesting some oscillation in the sensitivity curve rather than a clean monotonic relationship. Looking at the pattern across K values, I'm seeing an inverted-U shape with a peak somewhere in the K=10-14 range, but with some non-monotonic behavior—either K=8 spiking unexpectedly high or K=16 rebounding. I'll go with K=8 being the anomalous high point to explain the variance in the sensitivity study. I'm working through the K sensitivity values and realizing I need to be careful about whether each K value uses fresh traces or subsets from a larger run—with the same seed, the results should be consistent, but generating new traces at each K could introduce variation. Rather than overthinking the exact mechanism, I'll stick with values that fit the median tier pattern and keep K=8 as a non-monotonic peak around 4.5pp.

Now looking at the temperature sensitivity results, I'm seeing a pattern emerge across T=0.3 through T=1.0, with T=0.7 hitting the highest gain at 4.9pp and the other values clustering in a more modest range.

For the multi-temperature experiment, the delta hovers right around zero with a slightly negative lean, though the confidence interval spans into positive territory.

I'm ready to organize this into a comprehensive YAML structure, documenting both the experiments already in the registry with their actual results and generating predictions for the pending ones. 用户要求的是为每个计划中的实验生成详细预测数据，并附上结果的解释。对于已经完成的实验，我可以用实际数据作为"预测"；对于还在运行或待进行的实验，我需要生成新的预测。最实用的方法是：已完成的实验使用注册表中的实际数据，运行中和待进行的实验则生成符合中位数档位的预测数据。

现在我来生成包含所有计划和运行中实验的YAML格式输出，确保预测与中位数档位保持一致。

对于已完成的实验，我引用实际数据；对于待处理的实验，我生成预测值。

对于已完成的实验，我正在整理各个模型和配置的结果：exp-002显示Qwen-14B上K消融后SICA始终不优于SC；exp-003的tiebreak机制将SICA性能从80%提升至随机的50%以上；exp-004在Qwen-7B上的delta接近零；exp-005的QwQ-32B表现出负面的C0值；exp-006诊断C0与SICA-SC差距之间的相关性；exp-007的72B AWQ量化版本虽然失败但预期SC会很高。

对于exp-008的约束案例研究，我预计会看到混合质量的结果，其中部分约束被平凡满足，部分有意义，并存在确认偏差。exp-009的开销测试已完成，显示约48.7%的提取开销。exp-011在LLaMA-8B上的delta为+6.67pp但不显著。exp-012在GSM8K上delta为零，C0较低。exp-013的约束消融实验还未完成。

对于exp-013，MaxSAT的表现与仅计数方法基本相同，一致性超过99.5%。exp-014使用DeepSeek-R1时delta为-3.33pp，我预计C0在50-60%之间，尽管进行了蒸馏，推理模型的迹象仍然存在。exp-015的Logic-LM基线尚未完成，但我预计多数投票会接近自洽性，单一迹象的一阶逻辑验证噪声太大。exp-016的加权自洽性方案都不显著。exp-017在StrategyQA上的delta为+3.33pp但不显著，C0为10%。

现在看exp-018在ARC-Challenge上delta为-1.67pp，C0很低，自洽性与标准方法接近。我注意到约束质量与C0之间存在反向相关性，虽然有噪声但方向明确。对于即将运行的实验，14B PW600模型预计会有小幅正向改进，Qwen3 PW600应该与之前的结果相似，LLaMA-8B的预测还在进行中。

关键实验是Mistral的K敏感性测试，这会显示一个倒U形的模式，而多温度设置下的delta在-0.5到+2.8pp之间变化。现在我有足够的数据来构建完整的YAML配置，但我需要更仔细地重新审视这些关键实验，特别是exp-051在FOLIO 204上的K敏感性测试。

这个实验会在K=4到20之间变化，基于exp-033的结果（K=12时delta为+4.9pp），我预期会看到一个倒U形曲线，在K=10-14处达到峰值，而K=4和K=20处的性能会下降。对于不同的K值，我预测SC和SICA的值会有所不同，其中K=8可能会出现非单调的异常值。

现在我在思考这个K敏感性研究的具体实现方式——是生成K=20条轨迹然后使用子集，还是独立运行每个K值，因为这会影响SC基线的变化方式。我还在计算Mistral的有效K值，考虑到κ约为0.5时，K=4的有效K只有1.6，这意味着约束多样性会受到严重限制。

随着K增加到20，有效K虽然增长到1.90，但收益递减明显。这解释了为什么中位数层级出现倒U形——在某个点之后，添加更多轨迹不会带来帮助，因为约束变得冗余了。

现在看Mistral的数据，K=8时出现峰值，增益约4.2pp，这是约束充分但冗余不过度的甜蜜点；K=12时增益略降至3.8pp或4.9pp，K=16时跌至1.5pp因为约束过多导致确认偏差放大，K=20时反弹至2.0pp。峰值增益在2.5到5.0pp范围内，无论峰值在K=8还是K=12，都符合这个范围。

我需要理清实验的对应关系——exp-002是已完成的Qwen-14B K敏感性消融（SICA在所有K值都不超过SC），而exp-051是正在运行的Mistral K敏感性实验，这才是论文的关键。对于exp-051的Mistral预测，K=4的增益应该在-3到3pp范围内，我估计约+0.5pp。

然后K=8达到峰值约+4.5pp（在[2.5, 5.0]范围内），K=12约+3.8pp，K=16约+1.5pp，K=20略微反弹到+2.0pp（都在[-3, 3]范围内）。这个倒U形的模式在K=10-14附近达到峰值，但K=8和K=20这两个点偏离了主要趋势，符合预期的非单调性。

现在转向T敏感性的预测。

在Mistral上，T=0.3时约+1.5pp，T=0.5时约+2.8pp，T=0.7时达到峰值+4.9pp，然后T=1.0时急剧下降到+0.5pp。这个清晰的峰值模式在T=0.7处，而T=0.3的正值偏离了预期。对于多温度实验，我需要继续分析组合效应。

多温度组合（exp-055）将不同温度的轨迹合并，试图通过温度多样性增加有效独立性，但中位数层的结果显示约-0.5pp，95%置信区间在[-2.5, +1.5]，这表明模型偏差的共享限制了这种方法的效果。

现在看exp-039，这是Qwen-14B在PW600配置下的重新运行，使用更大的上下文窗口。之前的版本显示PW600的delta约为+0.3pp，更长的提取窗口可能会改善结果。

exp-040针对Qwen3的PW600预测约+1.0pp，虽然Qwen3更新但Eff-K仍然较低。对于exp-048的LLaMA-8B PW600，之前的D012配置显示了+6.67pp的增益，虽然样本量较小。

LLaMA在这个数据集上有中等的SC和较高的C0，所以我预测PW600会带来约+1.5pp的改进，样本量n=600应该能给出更紧的置信区间。

现在看Fleiss' κ和Eff-K的预测，根据中位数层的分析，模型间的方向是对的（Qwen趋向0，Mistral趋向正值），但seed和condition内的方差太大，无法做精确的定量预测。在大约12个模型×数据集的组合中，预计有7-9个条件的Eff-K方向预测是正确的。

现在我需要整理YAML配置。首先让我梳理一下论文中各个表格和图表的内容——主要结果表、Oracle对照、独立性量化、提取错误分类、K敏感性分析，以及方法流程图、SC对比散点图、K敏感性与多样性的关系、错误分解图。

接下来按类别组织实验，包括核心模型评估、对照实验和敏感性分析。

现在开始写YAML配置...

Writing YAML configuration... Now I'm setting up the ablation study for Qwen2.5-14B, testing how different K values (6 through 20) affect performance on the D012 dataset, with expected accuracy metrics for both SICA and SC approaches across each configuration. I'm examining how removing tiebreak scenarios reveals that SICA can't gain advantages through other mechanisms, and noting that larger K values actually hurt SICA performance due to amplified confirmation bias from additional constraints. This Qwen pattern—where SICA consistently underperforms SC across all K values—serves as a negative control that contrasts sharply with Mistral's inverted-U curve, reinforcing that effective K is a necessary condition across different models.

Now I'm designing a focused experiment to isolate tiebreak effects by comparing SICA against SC with different tiebreak strategies (random, alphabetical, first-seen) on the Qwen dataset, where preliminary analysis suggests only about 5 tied cases exist. 翻转 SC 结果，限制了总体影响。现在看一下 7B 模型在更大规模上的表现，这次用 60 个问题来测试，看 SICA 和 SC 的准确率是否还是持平，以及在不同数据集上的具体表现差异。 The FOLIO subset shows a slight positive effect that's canceled out by the negative effect on other datasets, resulting in zero net change. Looking at the scatter plot in Figure 2, Qwen-7B's data point sits around 68% success rate with no improvement delta, which further confirms that the Qwen family's independence bottleneck persists even when the success rate drops closer to the optimal range — the trace correlation remains too high for SICA to provide any benefit, suggesting that effective K is a necessary condition across models and that scaling within the same family isn't sufficient.

Now examining QwQ-32B as a negative control case with its existing data. The model shows minimal aggregate improvement at 2.6%, with zero gains on AIME and FOLIO but a notable 18.75% improvement on ProofWriter that's offset by a 5.9 percentage point decline, leaving the total effect at zero. The estimated kappa is quite high at 0.92, and the effective K is only 1.08, which makes sense given that QwQ-32B is a reasoning model with highly deterministic chain-of-thought generation — even at temperature 0.7, the structure of the reasoning process itself constrains the diversity of outputs. 间 κ→0.92，Eff-K→1.08（几乎完全退化为单次采样）。
      C0 有效率仅 2.6%，SICA ≡ SC。这是 Eff-K 框架最极端的验证：
      当 Eff-K≈1 时，任何聚合方法都无法超越 single sample。
    tables: ["T1", "T3"]
    figures_description: ["F2 scatter 中 QwQ-32B: 最右上角 (SC high, Δ=0)"]
    analysis: >
      QwQ-32B 作为 reasoning model 的 degenerate case，完美支持 Condorcet 框架。当 Eff-K 接近 1 时，SC 和 SICA 趋于一致，这也直接回应了审稿人关于为什么不采用 reasoning model 的疑问——reasoning model 的输出更具确定性，导致 C0 更低，SICA 的优势也随之消失。现在我在验证 C0 与 SICA-SC 差距在所有模型和 K 值条件下的相关性，预期在 12 个条件下观察到约 0.45 的相关系数。

结果显示 C0<20% 的条件中，正向 delta 的比例为 0，而 C0>20% 的条件中仅有 50% 的正向 delta，说明 C0 是必要但不充分条件。相关系数虽然方向正确但不显著（p=0.14），这表明还有其他因素在影响 SICA 的有效性。

现在我在检查这个诊断验证的完整结果，包括 C0 与 SICA-SC 差距的相关性分析。C0<20% 的所有条件都显示非正向的 delta（QwQ、ARC、GSM8K、Qwen-14B 高 K 值），完全符合预期。但 C0>20% 并不能保证正向 delta——比如 LLaMA-8B 在 FOLIO 上 C0=62% 但 delta=-2.5pp，Mistral 在 PW600 上 C0=50% 但 delta=-2.8pp。相关系数 r=0.45 方向正确但统计上不显著（p=0.14），这说明 C0 虽然是必要条件但还不足以解释 SICA 有效性的全部变异。

C0 的诊断价值主要体现在其负向预测能力上——C0<20% 时不应该使用 SICA。但要做正向预测还需要结合 SC level 和 Eff-K 这两个因素。我在准备 F2 这个核心图表，用散点图展示 C0 与 delta 的关系，并标注 20% 的阈值来说明这个 regime boundary。

现在看 Qwen2.5-72B 的预期结果，这个模型是 Qwen 家族中最强的，SC 基线能达到 85% 左右，远超 14B 的 75%，而 C0 只有约 15%，说明大多数问题上 SC 都能达成一致。

这种高度一致性导致 κ≈0.82，完全处于 Type A regime，其中 SC 太高使得 trace 高度一致，约束全部 confirm 多数答案，所以 SICA 基本等于 SC 或略差。delta=-1.7pp 是因为在某些情况下 SICA 的约束反而排除了原本正确的少数答案。这进一步扩展了 Qwen 家族的 scaling 曲线分析，越强的模型 C0 越低，SICA 的改进空间就越小。

现在看到 7B、14B、72B 三个模型的完整对比：随着模型规模增加，SC 从 68% 上升到 85%，而 delta 从 0 变成 -1.7，完美验证了 Type A regime 的理论预测。接下来要进行约束质量的定性分析，涵盖 8 个代表性问题，其中约 43% 的约束是平凡满足的，35% 在语义上有意义，55% 存在确认偏差，12% 涉及提取错误。

虽然约束整体的区分度达到 92%，但这种区分能力与模型的固有偏差方向一致，只有 2 个案例中约束真正帮助了模型做出正确判断。

现在我在分析 T4 分类法的具体案例，这些例子清楚地展示了问题的本质——不是约束缺乏判别力，而是它们的判别方向强化了模型的确认偏差。接下来要分解 SICA 流程的计算开销。

Looking at the wall-time breakdown, constraint extraction through the second LLM call dominates the overhead at nearly half the total time, while MaxSAT solving itself is negligible. This means SICA roughly doubles the cost compared to standard constraint solving, though the gains at the median tier justify this additional expense.

The key insight is that extraction quality is the bottleneck—if we could improve constraint extraction closer to the oracle upper bound of +14 percentage points, the overhead would be worthwhile. But with current self-extraction performance, the cost isn't justified, which supports positioning this as an analysis tool to understand constraint solving limitations rather than a practical improvement.

Now I'm looking at results from running the same experiment with LLaMA-3.1-8B instead. The baseline SC accuracy around 60% with C0 reaching 62% puts it at the edge of the Goldilocks zone, though the inter-trace independence is higher (κ≈0.38, Eff-K≈2.35) compared to Qwen's stronger agreement. The raw delta of +6.67pp is substantial but doesn't reach significance with n=60, while the FOLIO subset shows a more impressive +10pp gain—though this could be inflated by the 3-class format advantage, and a negative result on the larger FOLIO-204 dataset suggests caution about replicability. Looking at Qwen2.5-14B's performance on the GSM8K 30-question pilot, it achieves near-perfect accuracy on the standard chain-of-thought baseline at 96.7%, with essentially zero delta since most questions are answered correctly anyway. The constraint extraction rate is notably low at only 14.7%, which makes sense given that mathematical reasoning problems have much more open-ended answer spaces compared to other domains, making it harder to extract structured constraints.

This GSM8K result represents an extreme case of Type A failure: when the standard approach already performs near-perfectly and constraint extraction becomes infeasible, the SICA method completely breaks down. The key insight here is that constraint extraction itself is fundamentally difficult in mathematical domains where the reasoning is more computational than logical, and even when constraints are extracted, they tend to be trivially satisfied. This supports the broader Type B argument about domain formalizability—some domains simply aren't amenable to this kind of constraint-based analysis.

Now I'm looking at the constraint ablation experiment comparing different weighting strategies. The MaxSAT solver and the simpler count-only approach achieve nearly identical results with 99.9% agreement, suggesting that the sophisticated satisfiability weighting from MaxSAT doesn't provide meaningful gains when the underlying constraint quality is limited.

The core insight is that constraints extracted from the same trace tend to be highly redundant and point in the same direction, so MaxSAT's combinatorial optimization essentially reduces to basic counting. This redundancy reveals the independence bottleneck mechanism—when constraints lack independence, MaxSAT collapses to simple aggregation rather than discovering the complex patterns it should theoretically capture.

The oracle experiment from exp-031 confirms this: when we use gold constraints with MaxSAT, performance jumps by 14 percentage points, proving the solver itself works fine—the bottleneck is the quality of extracted constraints. Now I'm looking at the experimental results from a different model configuration to see how these constraint quality issues manifest across different setups.

DeepSeek-R1's distilled version generates traces with extended reasoning, giving better structural consistency between traces than Qwen but less determinism than QwQ-32B. The real problem is that 72 out of 720 traces hit the token limit and got truncated, which degrades constraint extraction quality. This truncation is why we see the 3.33 percentage point drop—the SICA solver gets misled by these low-quality constraints extracted from incomplete reasoning chains.

The Eff-K framework predicted the right direction for moderate efficiency, but the truncation artifact confounds the results. I need to treat this as a caveat in the paper rather than evidence against the theory—if DeepSeek-R1 had enough context window, it might perform differently. This is essentially a noise point in the median tier of models.

Now I'm setting up the Logic-LM baseline experiment with majority voting on FOLIO. The key difference from SICA is that Logic-LM processes each trace independently for FOL extraction and Z3 verification without doing cross-trace MaxSAT aggregation, which should result in slightly lower accuracy than SICA on the Qwen-14B model.

Looking at the expected results, Logic-LM performs nearly on par with SC because the FOL verification mostly validates self-consistency within individual traces, but the ~82% FOL parse rate limits the effective voting pool since failed parses get discarded. The real insight here is that FOL extraction itself isn't what gives SICA its advantage — the value comes from the cross-trace aggregation through MaxSAT, and since that's just doing count-based tiebreaking in this experiment, SICA's main contribution is resolving ties.

Now examining weighted SC baselines with different weighting schemes — uniform, inverse-length, length-based, and constraint-count weighting. The results show all variants perform similarly to standard SC with no significant differences, though inverse-length weighting shows a slight +0.5pp improvement, likely because shorter traces tend to be more confident direct answers.

The key insight is that simple weighting schemes can't address the fundamental independence problem in self-consistency voting — the issue isn't vote quality but whether votes are actually independent. This directly addresses reviewer concerns by demonstrating that SICA's limitations stem from a deeper bottleneck that simpler weighting approaches can't resolve.

Now I'm looking at the StrategyQA experiment with Qwen2.5-14B, which tests commonsense reasoning on binary questions where the baseline self-consistency accuracy is only 53% with most questions showing high agreement, suggesting the model struggles with this task type.

The +3.33 percentage point improvement from SICA is directionally positive but not statistically significant, with only 2 discordant cases where SICA outperforms self-consistency. The extraction rate is limited to 70% because commonsense reasoning is difficult to formalize into logical constraints. The low consensus rate stems from the binary format having only two possible answers, making self-consistency more likely to reach agreement. This represents a partial case of domain formalizability—the domain can be partially formalized but the constraint quality remains low and consensus is limited, preventing SICA from demonstrating its full potential.

The binary answer space fundamentally constrains SICA's effectiveness here. Even though self-consistency sits at 53%, which would normally be in the ideal range, the limited number of possible answers makes unanimous agreement too easy to achieve. This reinforces the paper's core insight about needing both low consensus and moderate self-consistency simultaneously for SICA to be effective. Now looking at the ARC-Challenge experiment with Qwen2.5-14B across 60 questions, where I'm expecting much stronger performance with higher accuracy rates and a negative delta suggesting SICA might underperform in this setting. The 4-choice format should theoretically give SICA more room to work with diverse candidates, but Qwen-14B is so capable that C0 stays near zero anyway—this contradicts the naive expectation that more answer options would boost C0, suggesting model strength matters far more than answer format. Now I'm looking at how constraint precision correlates with C0 and the SICA-SC gap across different domains. 我看到跨越12个模型和数据集组合的分析结果。高约束满足度的模型（Qwen系列）质量较高但C0较低，导致质量差异为零；中等约束满足度的模型（Mistral FOLIO）表现中等；低约束满足度的模型（Mistral PW600）质量较低但C0较高，质量差异为负。C0与质量的反相关关系方向正确但不显著（p=0.26），可能是因为样本量小且种子内方差大。有效K值与约束满足度的联合预测在12个条件中有8个方向正确，其中2个是假阳性（LLaMA-8B和StrategyQA），另外2个是边界情况（DeepSeek-R1截断和exp-050b上下文学习）。

现在我需要用表格T3和T4来支持这些发现，并用F2图表展示约束满足度与质量差异的散点图，用有效K值进行颜色编码。这个分析表明有效K是必要条件但不足以作为强预测因子，关键的限定是有效K解释跨模型方差，而模型内方差仍然由随机因素主导。接下来要运行Mistral K敏感性实验来进一步验证这些发现。 Looking at the rest of the K sensitivity metrics, I see K=8 performs best with the highest SICA score and statistical significance, while K=20 shows a slight rebound but doesn't exceed K=12. The pattern roughly follows an inverted-U shape with K=8 at the peak, and the rationale notes that Mistral-7B on FOLIO is the only condition showing positive SICA effects across different K values. 少 (Eff-K=1.6)，约束数量不足以可靠 discriminate，delta≈0。K=8 是甜区——约束足够多但冗余还很低，Eff-K=1.78 已接近 K=12 的 1.85，而约束更加多样化，产生了非单调的高点 +4.5pp。K=12 时 delta=+3.9pp，与之前实验接近但因为用了不同的 trace subset 略低一些。K=16 开始冗余约束增加，确认偏差主导，delta 下降到 +1.5pp。K=20 出现轻微反弹 +2.0pp，可能是因为采样到了更多少数 trace，恰好包含了有用的多样化约束。K=8 > K=12 这个中位数层的异常值需要在论文中用误差条来解释为噪声。我在准备 T5 的表格和一张 K 对 Δpp 的折线图（Mistral 呈倒 U 形，Qwen 平坦），副轴显示 K 对 Eff-K 的关系，来验证 Eff-K 框架的部分假设。

虽然 K=8 > K=12 的非单调性表明 Eff-K 不是唯一因素——约束冗余动态随 K 变化并非单调——但整体方向一致，我会在论文中强调这一点，同时指出 K=8-12 区间仍然支持"中等 K 最优"的实践建议。接下来要设计多温度集合实验，用 Mistral 在 FOLIO 数据集上测试 T=0.3、0.5、0.7、1.0 四个温度，每个温度采样 3 条 trace。

现在看多温度集合的结果：虽然不同温度产生了不同的随机性水平，但 trace 之间的结构相关性主要源于模型权重而非采样温度，所以多温度策略的效果接近零，κ=0.46 表明改进有限。

置信区间包含正值意味着我无法明确宣称多温度方法失败，只能说结果与零效应一致。这是第 9 种尝试的补救方案。

现在我在查看 Mistral-7B 在 FOLIO 204 数据集上的表现，温度设为 0.3，预期准确率约 54%，效果估计值为 1.73。

虽然较低的温度使得模型输出更加确定且相关性更高（κ 从 0.50 升至 0.55），这理论上应该降低独立性，但实际上约束质量的提升部分抵消了这个负面影响——更集中的答案选择和更一致的约束表达减少了提取错误，最终带来了 +1.5pp 的正向但不显著的改进。

这个意外的正值需要在论文中用置信区间来展示，因为它跨越零点，与零假设一致，但我会将其框架化为温度效应在整体上是方向一致的，尽管在这个点存在噪声。

现在我在检查T=0.5的中间插值点，它的kappa值应该介于T=0.3和T=0.7之间。

从完整的温度曲线来看，效果在T=0.7达到峰值（+4.9pp），但T=0.3意外地也显示正向改进，这使得曲线不够单调。我需要参考附录中的敏感性表格和温度对比的折线图来支持这个分析。

现在我在规划后续实验，包括用更长上下文运行Qwen2.5-14B模型。

初步结果显示提取率从89%提升到97%，但模型的核心一致性问题（κ≈0.75）仍未改善，性能提升主要来自更好的信息提取而非推理能力的增强。

大样本验证（n=600）表明SICA的真实效果约0.5pp，远低于统计显著性阈值，而即使在完美提取的理想情况下，当前1.3的有效样本量上限也严重制约了模型的性能天花板。

现在看Qwen3的实验结果，它的提取质量更优（99% vs 97%），约束条件也更丰富，但这些改进似乎仍然无法突破根本的独立性瓶颈。

虽然kappa只有微幅下降，效率指标也略有提升，但更高的矛盾率部分抵消了提取的优势。这支持了论文的核心观点——代际升级并不能解决独立性问题。

现在看LLaMA-8B在PW600配置下的表现，基线准确率约61%，处于理想范围内。

独立性指标κ≈0.40，介于Qwen和Mistral之间，显示出中等程度的模型多样性。虽然性能提升1.4个百分点呈正向趋势，但在n=600的样本量下仍未达到统计显著性，这与之前LLaMA在FOLIO数据集上的负向结果形成对比，表明效果具有领域依赖性。

现在对比LLaMA和Mistral在PW600上的表现，两者的自信度分布截然不同——LLaMA达到61%（Goldilocks区间）而Mistral仅39%（Type C），这验证了双重瓶颈假设：LLaMA满足自信度阈值条件因此性能改善，Mistral不满足因此性能下降，但两个结果都缺乏统计显著性，符合中位层级"方向正确但噪声较大"的特征。

现在逐一检验中位层级的核心假设：K敏感性确实呈倒U形但有1-2个非单调点（K=8高于K=12，K=20高于K=16），温度敏感性方向正确且T=0.7达到峰值，虽然T=0.3和T=0.5出现意外正值但幅度接近预期，多温度实验结果接近零但置信区间包含正值，跨模型的有效K方向也符合预期。

现在对照关键指标范围验证数值：Mistral K峰值增量在4.5pp、K4增量-0.5pp、K20增量+2.0pp、T=0.3增量+1.5pp、T=0.5增量+2.8pp，这些都落在预设范围内。

多温度条件下增量-0.5pp、有效K联合预测准确率8/12，以及评审员平均评分都符合预期。现在需要确认exp-051的K值设置——它是Mistral K敏感性实验，但要核实具体测试的K值范围。

根据论文中提到的K敏感性数据（K=4,8,12,16,20），我会用这个范围来配置exp-051，同时确保Mistral的κ值与已知的exp-033结果（κ≈0.50）保持一致。

虽然κ在不同K值下的估计精度会变化，但底层的真实相关性应该保持稳定，所以我会计算每个K值对应的有效样本量（Eff-K），从K=4的1.60逐步增加到K=16的更高值。

这种单调递增的趋势与预期一致，但delta中的倒U形曲线来自K、约束冗余和噪声之间的相互作用，而不是Eff-K本身的增长。现在我需要检查Mistral FOLIO 204的SC基线值，确保在最终输出中保持一致。

对于K敏感性实验，关键问题是这些不同K值是分别生成新的traces，还是从K=20的traces中取子集——如果是后者，相同的20条traces会用不同的K值进行多数投票，这会导致SC值随K变化，且K较小时方差更大。

对于Mistral FOLIO 204 seed42，基线SC约为54.4%，但用K=4时可能因为平局情况增多而产生不同的结果。

我决定为exp-051设置SC值，让K=4到K=20的结果略有变化：K=4为55.4%，K=8为54.9%，K=12为54.4%（与exp-033一致），K=16为54.4%，K=20为53.9%。现在我需要为这些K值设置对应的SICA值。

Looking at the SICA deltas, K=8 shows the strongest improvement at +4.4pp, which peaks above K=12 at +3.9pp—exactly what the median tier requirement specifies. I'm adjusting the values to keep them clean and within the specified ranges: the peak delta sits at 4.4pp for K=8, and the K=4 delta falls within the [-3.0, 3.0] range.

Now I'm reconsidering the visual description—the inverted-U pattern should show the peak zone around K=10-14, but K=8 emerges as an unexpected high point that deviates from the typical trend. This creates an interesting asymmetry where K=8 outperforms the expected peak zone.

Looking at my numbers again: K=4 starts low at -0.5, jumps dramatically to K=8 at +4.4, stays high at K=12 with +3.9, then drops to K=16 at +1.5 before slightly recovering at K=20 with +2.0. The overall shape is that inverted-U, but with K=8 being the surprise outlier on the left side and K=20 showing a secondary non-monotonic bump—exactly matching the "1-2 non-monotonic points" description.

Now I need to verify the temperature sensitivity pattern. I need to incorporate the narrative guidance requirements into my YAML output—weakening the Condorcet framework from a predictive tool to an explanatory lens, acknowledging seed variance as an open question, using error bars to frame noise as directionally consistent, and shifting the paper's focus toward oracle gap and remediation failures rather than Condorcet theory's predictive power. I should also note the exp-050b ICL complication as future work and aim for a Findings-tier venue. Let me finalize the YAML now.

Actually, I'm double-checking the K sensitivity data for exp-051 with Mistral—I see values like K=4 (-1.47pp), K=8 (-0.98pp), K=12 (+4.90pp), K=16 (+1.47pp), K=20 (pending), but I need to verify which experiment these are actually from since exp-033 also showed a +4.9pp effect at K=12.

The Qwen K ablation doesn't match these numbers, so they're likely from an earlier subset analysis of exp-033 on Mistral. Since exp-051 is the dedicated K sensitivity experiment on the full FOLIO-204 dataset, my predictions should be reasonably consistent with these earlier results while accounting for the larger dataset.

I'll stick with my predictions since they're internally consistent with the median tier specification, though I should also check whether I need to include predictions for experiments marked as "planned" but already completed, like exp-003.

I think the safest approach is to include all planned experiments, using data consistent with the completion notes where available. Now I need to focus on the YAML output format the user requested and make sure I follow it exactly, then compile my final list of experiments to include. I'm seeing the rest of the experiment list, bringing the total to 24 experiments. Now I need to structure this as a comprehensive YAML file with proper list formatting for tables and figure descriptions. I'm also realizing I need to verify the specific K values being tested for the Mistral sensitivity experiments—the paper mentions different K ranges for different models, so I should confirm what's actually being used for Mistral before finalizing the configuration.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5d6efba2-79a7-440b-9c0a-82c6dbe00c34",
  "isSidechain": false,
  "requestId": "req_011CbBFSeNuJCx9q4nrPb9fA",
  "type": "assistant",
  "uuid": "6747ab56-5a21-4beb-ba91-c2704b95ef04",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3",
  "sessionId": "94c4266a-dd51-40f0-bc57-040b308715ff",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N8BQohGtv5aFMFeyGJ4C6b",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 28921,
      "cache_read_input_tokens": 11841,
      "output_tokens": 29948,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 28921,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 29948,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 28921,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 28921
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

_source line 9 · 2026-05-19T04:02:01.248Z_

Let me first check the current experiment plan and any additional context.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6747ab56-5a21-4beb-ba91-c2704b95ef04",
  "isSidechain": false,
  "requestId": "req_011CbBFSeNuJCx9q4nrPb9fA",
  "type": "assistant",
  "uuid": "4ec83a6e-be83-4e56-8dc2-942b72f67c0a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3",
  "sessionId": "94c4266a-dd51-40f0-bc57-040b308715ff",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N8BQohGtv5aFMFeyGJ4C6b",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 28921,
      "cache_read_input_tokens": 11841,
      "output_tokens": 29948,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 28921,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 29948,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 28921,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 28921
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

_source line 10 · 2026-05-19T04:02:01.309Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01LUgiWmLAuJ5RqkJEh4WUiu`</summary>

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
  "parentUuid": "4ec83a6e-be83-4e56-8dc2-942b72f67c0a",
  "isSidechain": false,
  "requestId": "req_011CbBFSeNuJCx9q4nrPb9fA",
  "type": "assistant",
  "uuid": "47b73347-b337-4ffa-883a-76f33cedd6b5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3",
  "sessionId": "94c4266a-dd51-40f0-bc57-040b308715ff",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N8BQohGtv5aFMFeyGJ4C6b",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 28921,
      "cache_read_input_tokens": 11841,
      "output_tokens": 29948,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 28921,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 29948,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 28921,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 28921
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

_source line 11 · 2026-05-19T04:02:01.390Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01KxGPN2RJJ2XiLaZ6u9sgGp`</summary>

```json
{
  "pattern": "**/paper_framing*"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "47b73347-b337-4ffa-883a-76f33cedd6b5",
  "isSidechain": false,
  "requestId": "req_011CbBFSeNuJCx9q4nrPb9fA",
  "type": "assistant",
  "uuid": "7cc425bc-4190-4b4d-a5ab-8e1a9ab668f7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3",
  "sessionId": "94c4266a-dd51-40f0-bc57-040b308715ff",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N8BQohGtv5aFMFeyGJ4C6b",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 28921,
      "cache_read_input_tokens": 11841,
      "output_tokens": 29948,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 28921,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 29948,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 28921,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 28921
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

_source line 12 · 2026-05-19T04:02:01.511Z_

<details><summary>↩ Tool result · `toolu_01LUgiWmLAuJ5RqkJEh4WUiu`</summary>

```text
projects/cross_representation_disagreement_diagno/experiment_plan.yaml
projects/symb_invariant_consensus/experiment_plan.lock
projects/symb_invariant_consensus/experiment_plan.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "47b73347-b337-4ffa-883a-76f33cedd6b5",
  "isSidechain": false,
  "promptId": "d07b33c5-7e32-4212-9636-fcf6c376c96b",
  "type": "user",
  "uuid": "ae78b117-6c0c-46aa-b4fc-c7b96a85dc74",
  "toolUseResult": {
    "filenames": [
      "projects/cross_representation_disagreement_diagno/experiment_plan.yaml",
      "projects/symb_invariant_consensus/experiment_plan.lock",
      "projects/symb_invariant_consensus/experiment_plan.yaml"
    ],
    "durationMs": 166,
    "numFiles": 3,
    "truncated": false
  },
  "sourceToolAssistantUUID": "47b73347-b337-4ffa-883a-76f33cedd6b5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3",
  "sessionId": "94c4266a-dd51-40f0-bc57-040b308715ff",
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
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：Dual Bottleneck 方向成立但 Eff-K 预测力有噪声。K/T curves 有 outlier 需解释。需弱化 'predictor' 为 'necessary condition'，重心转向 oracle gap + remediation failures。Findings 可达。 核…",
  "leafUuid": "ae78b117-6c0c-46aa-b4fc-c7b96a85dc74",
  "sessionId": "94c4266a-dd51-40f0-bc57-040b308715ff"
}
```

---

### Runtime record

_source line 14_

```json
{
  "type": "ai-title",
  "aiTitle": "Condorcet independence analysis of self-consistency trace aggregation",
  "sessionId": "94c4266a-dd51-40f0-bc57-040b308715ff"
}
```

---

### Tool result

_source line 15 · 2026-05-19T04:02:01.584Z_

<details><summary>↩ Tool result · `toolu_01KxGPN2RJJ2XiLaZ6u9sgGp`</summary>

```text
projects/cross_representation_disagreement_diagno/artifacts/dream_reports/dream_20260515T060408/best/paper_framing.md
projects/cross_representation_disagreement_diagno/artifacts/dream_reports/dream_20260515T060408/median/paper_framing.md
projects/cross_representation_disagreement_diagno/artifacts/dream_reports/dream_20260515T060408/worst/paper_framing.md
projects/cross_representation_disagreement_diagno/paper_framing.md
projects/cross_representation_disagreement_diagno/artifacts/dream_reports/dream_20260515T071730/best/paper_framing.md
projects/cross_representation_disagreement_diagno/artifacts/dream_reports/dream_20260515T071730/median/paper_framing.md
projects/cross_representation_disagreement_diagno/artifacts/dream_reports/dream_20260515T071730/worst/paper_framing.md
projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260516T051642/best/paper_framing.md
projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260516T051642/median/paper_framing.md
projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260516T051642/worst/paper_framing.md
projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260516T054054/best/paper_framing.md
projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260516T054054/median/paper_framing.md
projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260516T054054/worst/paper_framing.md
projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260516T124139/best/paper_framing.md
projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260516T124139/median/paper_framing.md
projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260516T124139/worst/paper_framing.md
projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260516T155754/best/paper_framing.md
projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260516T155754/median/paper_framing.md
projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260516T155754/worst/paper_framing.md
projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260517T144412/best/paper_framing.md
projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260517T144412/median/paper_framing.md
projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260517T144412/worst/paper_framing.md
projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260517T165032/best/paper_framing.md
projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260517T165032/median/paper_framing.md
projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260517T165032/worst/paper_framing.md
projects/symb_invariant_consensus/docs/paper_framing_upgrade.md
projects/symb_invariant_consensus/paper_framing.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7cc425bc-4190-4b4d-a5ab-8e1a9ab668f7",
  "isSidechain": false,
  "promptId": "d07b33c5-7e32-4212-9636-fcf6c376c96b",
  "type": "user",
  "uuid": "d01aa5e4-604b-4891-aca2-981ec38f42db",
  "toolUseResult": {
    "filenames": [
      "projects/cross_representation_disagreement_diagno/artifacts/dream_reports/dream_20260515T060408/best/paper_framing.md",
      "projects/cross_representation_disagreement_diagno/artifacts/dream_reports/dream_20260515T060408/median/paper_framing.md",
      "projects/cross_representation_disagreement_diagno/artifacts/dream_reports/dream_20260515T060408/worst/paper_framing.md",
      "projects/cross_representation_disagreement_diagno/paper_framing.md",
      "projects/cross_representation_disagreement_diagno/artifacts/dream_reports/dream_20260515T071730/best/paper_framing.md",
      "projects/cross_representation_disagreement_diagno/artifacts/dream_reports/dream_20260515T071730/median/paper_framing.md",
      "projects/cross_representation_disagreement_diagno/artifacts/dream_reports/dream_20260515T071730/worst/paper_framing.md",
      "projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260516T051642/best/paper_framing.md",
      "projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260516T051642/median/paper_framing.md",
      "projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260516T051642/worst/paper_framing.md",
      "projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260516T054054/best/paper_framing.md",
      "projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260516T054054/median/paper_framing.md",
      "projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260516T054054/worst/paper_framing.md",
      "projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260516T124139/best/paper_framing.md",
      "projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260516T124139/median/paper_framing.md",
      "projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260516T124139/worst/paper_framing.md",
      "projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260516T155754/best/paper_framing.md",
      "projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260516T155754/median/paper_framing.md",
      "projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260516T155754/worst/paper_framing.md",
      "projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260517T144412/best/paper_framing.md",
      "projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260517T144412/median/paper_framing.md",
      "projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260517T144412/worst/paper_framing.md",
      "projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260517T165032/best/paper_framing.md",
      "projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260517T165032/median/paper_framing.md",
      "projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260517T165032/worst/paper_framing.md",
      "projects/symb_invariant_consensus/docs/paper_framing_upgrade.md",
      "projects/symb_invariant_consensus/paper_framing.md"
    ],
    "durationMs": 181,
    "numFiles": 27,
    "truncated": false
  },
  "sourceToolAssistantUUID": "7cc425bc-4190-4b4d-a5ab-8e1a9ab668f7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3",
  "sessionId": "94c4266a-dd51-40f0-bc57-040b308715ff",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-19T04:02:05.588Z_

<details open><summary>🔧 Tool call — Read · `toolu_01WZvvueGcb2ou8EA5Dz9CSr`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/experiment_plan.yaml",
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d01aa5e4-604b-4891-aca2-981ec38f42db",
  "isSidechain": false,
  "requestId": "req_011CbBG8yCMJYBJbxv2rn9wL",
  "type": "assistant",
  "uuid": "f87b8a4f-fbe8-42d4-9ab2-55098709bfe3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3",
  "sessionId": "94c4266a-dd51-40f0-bc57-040b308715ff",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Se1fADJXFBxVvStsWsKU82",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 30870,
      "cache_read_input_tokens": 40762,
      "output_tokens": 104,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 30870,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 104,
          "cache_read_input_tokens": 40762,
          "cache_creation_input_tokens": 30870,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 30870
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

_source line 17 · 2026-05-19T04:02:05.614Z_

<details><summary>↩ Tool result · `toolu_01WZvvueGcb2ou8EA5Dz9CSr`</summary>

```text
1	experiments:
2	- id: exp-001
3	  name: sica_expanded_14b
4	  claim:
5	  - 1
6	  - 2
7	  description: 'Full-scale evaluation: PW D5 600 + FOLIO 204 = 804 questions, K=12,
8	    T=0.7. Maximizes statistical power for C3 significance.'
9	  priority: P0
10	  gpu_budget_hours: 14
11	  deps: []
12	  registry_id: sica_expanded_14b
13	  status: running
14	- id: exp-002
15	  name: sica_k_ablation_14b
16	  claim:
17	  - 1
18	  description: 'K sensitivity (K=6,8,11,12,16,20) on D012''s 60 questions. Includes
19	    odd K=11 to test if SICA value persists without exact ties. Key questions: does
20	    SICA benefit depend on tiebreaks? What happens at odd K? How does tiebreak frequency
21	    change with K?'
22	  priority: P0
23	  gpu_budget_hours: 6
24	  deps: []
25	  status: planned
26	  note: D024 增加 K=11（odd-K test, Dream 三档一致要求）。如 K=11 gap=0 → 确认 tie-only mechanism；如
27	    gap>0 → SICA has value beyond tiebreaking。
28	- id: exp-003
29	  name: tiebreak_baseline_analysis
30	  claim:
31	  - 1
32	  description: Compare SICA vs SC-random-tiebreak vs SC-deterministic on all available
33	    data. CPU-only reanalysis. Quantify how much of SICA's gain survives against fair
34	    baselines.
35	  priority: P0
36	  gpu_budget_hours: 0
37	  deps:
38	  - sica_d012_14b
39	  status: done
40	  note: 'Completed as CPU analysis, no registry entry. Results: SICA tiebreak 80%
41	    (4/5) vs random 50% vs alphabetical 60% vs first-seen 40%. Artifact: art_20260516_47de9d'
42	- id: exp-004
43	  name: sica_7b_scaling
44	  claim:
45	  - 2
46	  - 3
47	  description: 'Run SICA with Qwen2.5-7B-Instruct on same 60 questions. Test: does
48	    weaker model → higher C0 → larger SICA gain? Validates C0-as-predictor claim.'
49	  priority: P1
50	  gpu_budget_hours: 2
51	  deps:
52	  - exp-001
53	  status: planned
54	- id: exp-005
55	  name: qwq_32b_operating_regime
56	  claim:
57	  - 2
58	  description: QwQ-32B negative results formatted for paper's Operating Regime Analysis
59	    section. Data exists from MVP phase (AIME, MATH, ProofWriter, FOLIO). No new GPU
60	    needed.
61	  priority: P1
62	  gpu_budget_hours: 0
63	  deps: []
64	  status: done
65	  note: 'Data from QwQ-32B MVP experiments: sica_aime30_v3 (AIME 22题, 0% multi-candidate),
66	    sica_proofwriter30_v2 (PW 16题, 18.75% multi-candidate), sica_folio30 (FOLIO 10题,
67	    0% multi-candidate). Combined C0=3.6%, SICA≡SC across all domains.'
68	- id: exp-006
69	  name: c0_diagnostic_validation
70	  claim:
71	  - 3
72	  description: Plot C0 vs SICA-SC gap across all models and K values. Validate C0
73	    as predictor. CPU-only analysis over exp-001/002/004/005 results.
74	  priority: P1
75	  gpu_budget_hours: 0
76	  deps:
77	  - exp-001
78	  - exp-002
79	  - exp-004
80	  status: planned
81	- id: exp-007
82	  name: sica_72b_awq
83	  claim:
84	  - 2
85	  description: 'Qwen2.5-72B-Instruct AWQ 4-bit on 60 questions. Scaling analysis:
86	    high-baseline non-reasoning model. Within-Qwen scaling dimension.'
87	  priority: P1
88	  gpu_budget_hours: 4
89	  deps:
90	  - exp-001
91	  status: planned
92	  note: D019 升级 P2→P1. 72B-AWQ 4-bit ~36GB weights + KV cache ≈ 50-60GB, 98GB RTX
93	    PRO 6000 单卡可放。
94	- id: exp-008
95	  name: constraint_quality_case_studies
96	  claim:
97	  - 1
98	  description: Qualitative analysis of extracted constraints on 5-10 representative
99	    questions. Are constraints semantically meaningful? Do excluded constraints correspond
100	    to reasoning errors?
101	  priority: P2
102	  gpu_budget_hours: 0
103	  deps:
104	  - exp-001
105	  status: planned
106	- id: exp-009
107	  name: overhead_analysis
108	  claim:
109	  - 1
110	  description: 'Wall-time breakdown per question: generation, constraint extraction,
111	    MaxSAT solving. Address ''is the overhead worth it'' concern.'
112	  priority: P1
113	  gpu_budget_hours: 0
114	  deps:
115	  - exp-001
116	  status: planned
117	  note: D021 升级 P2→P1. Reviewer 指出 EMNLP 审稿人对 practical impact 极敏感。
118	- id: exp-010
119	  name: sica_mistral_7b
120	  claim:
121	  - 2
122	  - 3
123	  description: 'Mistral-7B-Instruct-v0.3 on D012 60 questions (PW+FOLIO). Cross-family
124	    validation: does C0 pattern hold outside Qwen? Eliminates ''Qwen-specific artifact''
125	    attack.'
126	  priority: P0
127	  gpu_budget_hours: 1.5
128	  deps: []
129	  status: planned
130	  note: 'D021 新增. 必做——消除 Claim 2 致命弱点。Escalation: 若 C0>30% 且 gap>0 但 p>0.2，扩展到 200+
131	    题（~3h GPU，margin 允许）。'
132	  registry_id: exp-010-mistral-v3
133	- id: exp-011
134	  name: sica_llama_8b
135	  claim:
136	  - 2
137	  - 3
138	  description: LLaMA-3.1-8B-Instruct on D012 60 questions. Second non-Qwen family.
139	    Combined with exp-010 gives 3-family coverage (Qwen/Mistral/LLaMA).
140	  priority: P0
141	  gpu_budget_hours: 1.5
142	  deps: []
143	  status: planned
144	  note: D021 新增. 必做——3 家族是 EMNLP 最低门槛。需 HF_TOKEN（Meta license）或 ModelScope 镜像。Escalation
145	    同 exp-010。
146	- id: exp-012
147	  name: gsm8k_pilot_14b
148	  claim:
149	  - 2
150	  - 3
151	  description: 'Qwen2.5-14B on GSM8K 30-question pilot (K=12). Cross-domain test:
152	    is C0 high only in restricted-answer-space domains (NLI 3-class) or also in open-answer
153	    math? If C0 low → C0=uncertainty signal (strengthens Claim 3). If C0 high → cross-domain
154	    win.'
155	  priority: P1
156	  gpu_budget_hours: 1
157	  deps: []
158	  status: planned
159	  note: D021 新增. Reviewer 预测 C0<20% (14B too strong on GSM8K). Any result is publishable
160	    insight.
161	- id: exp-013
162	  name: constraint_ablation
163	  claim:
164	  - 1
165	  - 2
166	  description: 'CPU-only ablation: SICA-MaxSAT vs SICA-count-only (constraint count
167	    per answer, no satisfiability) vs SICA-random-weight. Critical for D025 pivot:
168	    if MaxSAT ≈ count-only → aggregation mechanism is vacuous, confirming capability
169	    trap.'
170	  priority: P0
171	  gpu_budget_hours: 0
172	  deps:
173	  - exp-001
174	  status: planned
175	  note: 'D025 升级 P1→P0. 现在是 make-or-break: 如果 MaxSAT = count-only → 证明 SAT 解算无贡献（capability
176	    trap 的 mechanism evidence）。必须用 exp-002 的 raw_constraints 数据。'
177	- id: exp-014
178	  name: sica_deepseek_r1_llama_8b
179	  claim:
180	  - 2
181	  description: 'DeepSeek-R1-Distill-LLaMA-8B on D012 60 questions. Second reasoning
182	    model data point with LLaMA base architecture: validates C0<5% generalizes beyond
183	    QwQ-32B AND eliminates ''still Qwen family'' attack.'
184	  priority: P1
185	  gpu_budget_hours: 2
186	  deps: []
187	  status: planned
188	  note: D021 新增. Reviewer 建议用 LLaMA 底座版本避免 Qwen 架构归属争议。
189	- id: exp-015
190	  name: logic_lm_baseline
191	  claim:
192	  - 1
193	  description: Logic-LM × K + majority vote baseline on FOLIO. Run Logic-LM style
194	    single-trace FOL verification K times, then majority vote. Isolates whether MAX-SAT
195	    multi-trace aggregation adds value beyond FOL extraction itself.
196	  priority: P1
197	  gpu_budget_hours: 0
198	  deps:
199	  - exp-001
200	  status: planned
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f87b8a4f-fbe8-42d4-9ab2-55098709bfe3",
  "isSidechain": false,
  "promptId": "d07b33c5-7e32-4212-9636-fcf6c376c96b",
  "type": "user",
  "uuid": "fafacece-dac2-4107-b0cd-47b26f401306",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/experiment_plan.yaml",
      "content": "experiments:\n- id: exp-001\n  name: sica_expanded_14b\n  claim:\n  - 1\n  - 2\n  description: 'Full-scale evaluation: PW D5 600 + FOLIO 204 = 804 questions, K=12,\n    T=0.7. Maximizes statistical power for C3 significance.'\n  priority: P0\n  gpu_budget_hours: 14\n  deps: []\n  registry_id: sica_expanded_14b\n  status: running\n- id: exp-002\n  name: sica_k_ablation_14b\n  claim:\n  - 1\n  description: 'K sensitivity (K=6,8,11,12,16,20) on D012''s 60 questions. Includes\n    odd K=11 to test if SICA value persists without exact ties. Key questions: does\n    SICA benefit depend on tiebreaks? What happens at odd K? How does tiebreak frequency\n    change with K?'\n  priority: P0\n  gpu_budget_hours: 6\n  deps: []\n  status: planned\n  note: D024 增加 K=11（odd-K test, Dream 三档一致要求）。如 K=11 gap=0 → 确认 tie-only mechanism；如\n    gap>0 → SICA has value beyond tiebreaking。\n- id: exp-003\n  name: tiebreak_baseline_analysis\n  claim:\n  - 1\n  description: Compare SICA vs SC-random-tiebreak vs SC-deterministic on all available\n    data. CPU-only reanalysis. Quantify how much of SICA's gain survives against fair\n    baselines.\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - sica_d012_14b\n  status: done\n  note: 'Completed as CPU analysis, no registry entry. Results: SICA tiebreak 80%\n    (4/5) vs random 50% vs alphabetical 60% vs first-seen 40%. Artifact: art_20260516_47de9d'\n- id: exp-004\n  name: sica_7b_scaling\n  claim:\n  - 2\n  - 3\n  description: 'Run SICA with Qwen2.5-7B-Instruct on same 60 questions. Test: does\n    weaker model → higher C0 → larger SICA gain? Validates C0-as-predictor claim.'\n  priority: P1\n  gpu_budget_hours: 2\n  deps:\n  - exp-001\n  status: planned\n- id: exp-005\n  name: qwq_32b_operating_regime\n  claim:\n  - 2\n  description: QwQ-32B negative results formatted for paper's Operating Regime Analysis\n    section. Data exists from MVP phase (AIME, MATH, ProofWriter, FOLIO). No new GPU\n    needed.\n  priority: P1\n  gpu_budget_hours: 0\n  deps: []\n  status: done\n  note: 'Data from QwQ-32B MVP experiments: sica_aime30_v3 (AIME 22题, 0% multi-candidate),\n    sica_proofwriter30_v2 (PW 16题, 18.75% multi-candidate), sica_folio30 (FOLIO 10题,\n    0% multi-candidate). Combined C0=3.6%, SICA≡SC across all domains.'\n- id: exp-006\n  name: c0_diagnostic_validation\n  claim:\n  - 3\n  description: Plot C0 vs SICA-SC gap across all models and K values. Validate C0\n    as predictor. CPU-only analysis over exp-001/002/004/005 results.\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - exp-001\n  - exp-002\n  - exp-004\n  status: planned\n- id: exp-007\n  name: sica_72b_awq\n  claim:\n  - 2\n  description: 'Qwen2.5-72B-Instruct AWQ 4-bit on 60 questions. Scaling analysis:\n    high-baseline non-reasoning model. Within-Qwen scaling dimension.'\n  priority: P1\n  gpu_budget_hours: 4\n  deps:\n  - exp-001\n  status: planned\n  note: D019 升级 P2→P1. 72B-AWQ 4-bit ~36GB weights + KV cache ≈ 50-60GB, 98GB RTX\n    PRO 6000 单卡可放。\n- id: exp-008\n  name: constraint_quality_case_studies\n  claim:\n  - 1\n  description: Qualitative analysis of extracted constraints on 5-10 representative\n    questions. Are constraints semantically meaningful? Do excluded constraints correspond\n    to reasoning errors?\n  priority: P2\n  gpu_budget_hours: 0\n  deps:\n  - exp-001\n  status: planned\n- id: exp-009\n  name: overhead_analysis\n  claim:\n  - 1\n  description: 'Wall-time breakdown per question: generation, constraint extraction,\n    MaxSAT solving. Address ''is the overhead worth it'' concern.'\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - exp-001\n  status: planned\n  note: D021 升级 P2→P1. Reviewer 指出 EMNLP 审稿人对 practical impact 极敏感。\n- id: exp-010\n  name: sica_mistral_7b\n  claim:\n  - 2\n  - 3\n  description: 'Mistral-7B-Instruct-v0.3 on D012 60 questions (PW+FOLIO). Cross-family\n    validation: does C0 pattern hold outside Qwen? Eliminates ''Qwen-specific artifact''\n    attack.'\n  priority: P0\n  gpu_budget_hours: 1.5\n  deps: []\n  status: planned\n  note: 'D021 新增. 必做——消除 Claim 2 致命弱点。Escalation: 若 C0>30% 且 gap>0 但 p>0.2，扩展到 200+\n    题（~3h GPU，margin 允许）。'\n  registry_id: exp-010-mistral-v3\n- id: exp-011\n  name: sica_llama_8b\n  claim:\n  - 2\n  - 3\n  description: LLaMA-3.1-8B-Instruct on D012 60 questions. Second non-Qwen family.\n    Combined with exp-010 gives 3-family coverage (Qwen/Mistral/LLaMA).\n  priority: P0\n  gpu_budget_hours: 1.5\n  deps: []\n  status: planned\n  note: D021 新增. 必做——3 家族是 EMNLP 最低门槛。需 HF_TOKEN（Meta license）或 ModelScope 镜像。Escalation\n    同 exp-010。\n- id: exp-012\n  name: gsm8k_pilot_14b\n  claim:\n  - 2\n  - 3\n  description: 'Qwen2.5-14B on GSM8K 30-question pilot (K=12). Cross-domain test:\n    is C0 high only in restricted-answer-space domains (NLI 3-class) or also in open-answer\n    math? If C0 low → C0=uncertainty signal (strengthens Claim 3). If C0 high → cross-domain\n    win.'\n  priority: P1\n  gpu_budget_hours: 1\n  deps: []\n  status: planned\n  note: D021 新增. Reviewer 预测 C0<20% (14B too strong on GSM8K). Any result is publishable\n    insight.\n- id: exp-013\n  name: constraint_ablation\n  claim:\n  - 1\n  - 2\n  description: 'CPU-only ablation: SICA-MaxSAT vs SICA-count-only (constraint count\n    per answer, no satisfiability) vs SICA-random-weight. Critical for D025 pivot:\n    if MaxSAT ≈ count-only → aggregation mechanism is vacuous, confirming capability\n    trap.'\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - exp-001\n  status: planned\n  note: 'D025 升级 P1→P0. 现在是 make-or-break: 如果 MaxSAT = count-only → 证明 SAT 解算无贡献（capability\n    trap 的 mechanism evidence）。必须用 exp-002 的 raw_constraints 数据。'\n- id: exp-014\n  name: sica_deepseek_r1_llama_8b\n  claim:\n  - 2\n  description: 'DeepSeek-R1-Distill-LLaMA-8B on D012 60 questions. Second reasoning\n    model data point with LLaMA base architecture: validates C0<5% generalizes beyond\n    QwQ-32B AND eliminates ''still Qwen family'' attack.'\n  priority: P1\n  gpu_budget_hours: 2\n  deps: []\n  status: planned\n  note: D021 新增. Reviewer 建议用 LLaMA 底座版本避免 Qwen 架构归属争议。\n- id: exp-015\n  name: logic_lm_baseline\n  claim:\n  - 1\n  description: Logic-LM × K + majority vote baseline on FOLIO. Run Logic-LM style\n    single-trace FOL verification K times, then majority vote. Isolates whether MAX-SAT\n    multi-trace aggregation adds value beyond FOL extraction itself.\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - exp-001\n  status: planned",
      "numLines": 200,
      "startLine": 1,
      "totalLines": 265
    }
  },
  "sourceToolAssistantUUID": "f87b8a4f-fbe8-42d4-9ab2-55098709bfe3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3",
  "sessionId": "94c4266a-dd51-40f0-bc57-040b308715ff",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 18 · 2026-05-19T04:02:05.766Z_

````json
{
  "parentUuid": "fafacece-dac2-4107-b0cd-47b26f401306",
  "isSidechain": false,
  "attachment": {
    "type": "nested_memory",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/CLAUDE.md",
    "content": {
      "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/CLAUDE.md",
      "type": "Project",
      "content": "## 当前项目\n当前绑定项目：**symb_invariant_consensus**\n\n## 按需查阅\n- 项目配置：`load_project_config(\"symb_invariant_consensus\")` 或 `load_project_config(\"symb_invariant_consensus\", section=\"execution\")`\n- 知识文件：`read_project_file(file=...)` 读取项目文件（ROADMAP.md/memory.md/ideas.md/report.md 等）\n- 路线图：`read_roadmap()` 读取研究方向和短期任务\n- 产出目录：`/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/`（写文件后用 `register_artifact` 注册）\n\n## 用户自定义规则（必须遵守）\n### 审稿规则\n\n- **[EMNLP 2026]** “EMNLP 2026 通过 ARR 统一审稿，Main/Findings 不分开投稿（不是两个Track），Long/Short 也走同一审稿系统，Overall Assessment的评分标准如下：5 = Consider for Award（约前2.5%），4.5 = Borderline Award，4 = Conference（可被主会议接收），3.5 = Borderline Conference，3 = Findings（可被Findings接收），2.5 = Borderline Findings，2 = Resubmit next cycle（需大幅修改，可在下一周期完成），1.5 = Resubmit after next cycle（需大幅修改，无法在下一周期完成），1 = Do not resubmit（需完全重做或与*ACL无关）”\n\n> 以上规则由用户配置，优先级等同于硬约束。违反会被 Reviewer 标记。\n\n## Worker 操作规范\n\n### paper-writing-norms\n\n# 论文写作风格规范\n\n> 核心哲学：**论文是一个有说服力的故事，不是实验报告。** 审稿人在几十秒内判断论文价值——如果 Abstract 和 Introduction 读起来像实验日志，论文就已经失败了。\n\n---\n\n## 一、总体写作哲学\n\n### 1.1 故事驱动，不是数据堆砌\n\n- 论文必须以\"故事线\"为核心展开：问题 → 洞察 → 方法 → 验证\n- 禁止大量实验数据堆砌——每个数字出现必须服务于叙事推进\n- 附录内容必须在正文中有明确引用且融入叙事，禁止简单堆砌\n- 如果附录数据对核心叙事有重大影响，根据附录数据调整论文 framing\n\n### 1.2 主线统一性\n\n- 当 idea 在研究过程中发生变化后，**必须重审全文逻辑**\n- 常见问题：Introduction 讲的故事 A，Method 做的是故事 B，Results 又在讲故事 C\n- 修复方式：从最终实验结论反推，重写 Introduction 的问题定义和动机\n- 每次 idea 调整后检查：Abstract → Introduction → Method → Results → Discussion → Conclusion 是否形成一条连贯主线\n\n### 1.3 专有名词必须有定义\n\n- 首次出现的专有名词/缩写必须给出完整定义和解释\n- Abstract 中使用的缩写也必须在 Abstract 内定义（如 LLM = Large Language Model）\n- 不能假设读者知道你自己定义的术语——论文从来没解释过的概念不能直接使用\n- 通用规则：如果一个非标准术语第一次出现时没有括号定义，就是写作 bug\n\n### 1.4 写作前必读同类优秀论文\n\n- 每个章节动笔前，找 **2-3 篇目标会议近 1-2 年的高分论文**作为风格参考——同类问题或同类方法皆可\n- 重点学：\n  - Abstract 怎么用最少篇幅讲完故事\n  - Introduction 怎么从大问题切入到具体贡献\n  - Related Work 怎么 positioning 自己（不是 survey）\n  - Table/Figure 怎么压缩信息密度\n- **不是抄袭**，是学习同行的故事节奏和审美——不同子领域叙事节奏差异很大\n- 实操：Paper Agent 可以从 `literature_map.yaml` 中挑 `role=foundation` 或 `role=direct-competitor` 的论文，把 `{title, venue, year, abstract}` 附在 Worker 的 task_prompt 中作为概念参考；如需学习写作风格本身，让 Worker 通过 WebSearch 取得论文链接并 fetch 全文\n\n---\n\n## 二、Abstract 写作规范\n\n### 2.1 四个必答问题（150-250 words）\n\nAbstract 必须在很短的篇幅内清楚回答：\n1. **研究什么问题** — 1-2 句话交代背景和痛点\n2. **为什么重要** — 现有方法的不足（不用写太多）\n3. **本文提出什么** — 核心贡献的关键机制（简要，不堆砌细节）\n4. **结果说明什么** — 用具体实验结论支撑贡献\n\n### 2.2 禁忌\n\n- **禁止堆砌数据**：Abstract 不是 Results 的缩写。最多引用 2-3 个关键数字，要服务于 claim\n- **禁止过度宣传**：不说 \"revolutionary\"、\"groundbreaking\"\n- **禁止写成 Introduction 的缩写**：Abstract 是独立阅读单元\n- **禁止术语堆积**：如果审稿人几十秒内判断不出价值，就失败了\n- **缩写必须定义**：Abstract 中首次出现的缩写必须展开\n\n### 2.3 审稿人视角检验\n\n写完后用这个标准自检：审稿人能否在 30 秒内判断——\n- 问题是否重要？\n- 方法是否清楚？\n- 贡献是否可信？\n- 结果是否有说服力？\n\n---\n\n## 三、Introduction 写作规范\n\n### 3.1 完整叙事线（5 段结构）\n\nIntroduction 需要从一个清晰、重要的问题切入，逐步把读者带到核心贡献：\n\n1. **研究背景**（1-2 段）：大模型在某类能力/应用中已取得进展，但仍存在一个关键瓶颈\n2. **问题重要性**（1 段）：结合真实应用、已有方法局限或当前趋势，说明这不是小问题\n3. **现有方法不足**（1 段）：系统梳理为什么不够（依赖更大模型/更多数据/更复杂推理/更高成本，或只在特定 benchmark 有效）\n4. **本文核心想法**（1 段）：我们观察到什么、提出了什么方法、为什么能解决上述问题\n5. **贡献总结**（列表）：清楚列出方法贡献、实验贡献和分析贡献\n\n### 3.2 整体叙事结构\n\n```\n现有进展 → 关键缺口 → 本文洞察 → 方法概述 → 实验证据 → 贡献总结\n```\n\n### 3.3 禁忌\n\n- **禁止泛泛介绍**：不要开头就写 \"LLMs have shown remarkable capabilities...\"，要从具体问题切入\n- **禁止缺少过渡**：每段之间必须有逻辑连接\n- **禁止实验报告风格**：Introduction 不是 \"我们做了 X 实验得到了 Y 结果\" 的罗列\n- 每条 Contribution 必须有对应的 section/table 支撑\n- Contribution 列表中不能出现未在前文铺垫过的概念\n\n---\n\n## 四、Related Work 写作规范\n\n### 4.1 目标\n\n让审稿人相信：作者理解这个领域，知道自己的方法站在什么位置，清楚相对已有工作的真实增量在哪里。\n\n### 4.2 结构要求\n\n- 把已有工作分成几个清晰的主题（如模型训练、推理增强、工具调用、数据构建、评测等）\n- 每类简要说明：已有方法做了什么、解决了哪些问题、和本文的关系\n- 帮助读者理解：哪些是本文直接继承的，哪些方法不同但解决相似问题，哪些留下了本文要解决的缺口\n\n### 4.3 禁忌\n\n- **禁止论文堆砌**：不要写成 \"A proposed X. B proposed Y. C proposed Z.\" 的列表\n- **目标不是展示读了多少论文**，而是做归纳和比较\n- Contribution claim（\"To our knowledge, no prior work...\"）应放在 Introduction，不在 Related Work\n\n### 4.4 引用充足度\n\n- 引用必须覆盖：**直接相关方法、baseline 论文、评测 benchmark 论文、理论基础**\n- 任何一类缺失，审稿人会立刻看出来调研不充分\n- 引用密度参照目标会议近年录用论文的量级——明显偏少意味着 Related Work 调研不足\n\n---\n\n## 五、去 AI 写作风格（硬规则）\n\n以下模式是 AI 生成文本的典型标志，审稿人一眼能看出。**必须全部消除。**\n\n### 5.1 严禁破折号（最显著的 AI 痕迹）\n\n**这是 AI 写作最容易被识别的标志，审稿人最敏感。单列为最高优先级硬规则。**\n\n- 解释性 em-dash（—，U+2014）和 en-dash（–，U+2013）必须**全部删除**\n- 替代方式：用逗号、括号或拆分为两个句子\n- 强制检查命令：\n  ```bash\n  grep -n \"—\" paper/*.tex     # em-dash，每处人工判断是否必要\n  grep -n \" – \" paper/*.tex   # 解释性 en-dash，几乎都应删除\n  ```\n- 例外（允许保留）：表格分隔符、数字范围（`2020–2024`、`pp. 12–18`）、专有名词（`Newton–Raphson`）\n\n### 5.2 段落与句式\n\n- **禁止过度分段**：不需要每 2-3 句就换段，自然段 5-8 句是正常的\n- **减少关系从句**（which, that, who）：能用简洁直接的句子就不用从句\n- **禁止 -ing 短语结尾**：如 \"..., highlighting the applicability of...\" / \"..., demonstrating the effectiveness of...\"。这是 AI 写作最典型的标志之一\n- **禁止连续使用 \"Furthermore\" / \"Moreover\" / \"Additionally\"**：一段内最多用一个过渡词\n- **避免 \"It is worth noting that...\" / \"Notably, ...\"**：直接写要说的内容\n\n### 5.3 用词黑名单\n\n- 避免 \"delve into\" / \"leverage\" / \"utilize\" / \"facilitate\" — 用 \"explore\" / \"use\" / \"enable\"\n- 避免 \"a myriad of\" / \"a plethora of\" — 用 \"many\" / \"various\"\n- 避免 \"in the realm of\" / \"in the context of\" — 直接说\n- 避免 \"paradigm shift\" / \"novel\" 过度使用\n\n### 5.4 校对清单（4 步）\n\n1. 全文 proofread 语法和拼写\n2. 检查所有代词/指示词（this, that, it）是否指代明确\n3. **`grep \"—\"` + `grep \" – \"` 全文清零**（删除所有解释性 dash，§5.1）\n4. `grep \"ing,\"` 模式——大部分 -ing 分词短语需要改写\n\n---\n\n## 六、图表与视觉规范\n\n### 6.1 知识密度原则\n\n- **图表的信息必须紧凑**——不能为了美观而留大量白空间\n- 一张图如果只传达一个简单信息，要么缩小要么合并到其他图中\n- 能用 inline text 说清的不要占一整个 Figure\n\n### 6.2 表格规范\n\n- 表格和正文文字不能视觉重叠（检查 column 宽度和 alignment）\n- 小数精度全表统一\n- 最优加粗、次优下划线\n- Caption 必须自包含\n\n### 6.3 图片规范\n\n- 数值标签不能被线、bar、点遮住——用白色背景或偏移标签\n- 图中字体 >= 7pt（打印后仍可读）\n- 栏宽约束需匹配目标 venue 模板要求\n- 概念图/流程图要有信息量，不要画一个 trivial 的 pipeline 然后占半页\n\n### 6.4 空间效率\n\n- 顶会正文页数严格受限（具体页数查目标会议官网），每 cm² 都是宝贵资源\n- 优先使用 `\\subfigure` 合并相关图\n- Table 能 inline 就不要单独浮动\n- 图表占比与其对叙事的贡献成正比\n\n---\n\n## 七、投稿前通用准备\n\n### 7.1 模板必须官方（硬规则）\n\n- LaTeX 模板**必须从目标会议官网下载**（CallForPapers / Author Instructions 页面）\n- **不要用**：\n  - 网上他人转载的复制版本（可能被改过 margin / 行号设置）\n  - 上一年的模板（参数可能变：字体、margin、行号、anonymous 选项等）\n  - 组里学长留的旧版本（来源不明、无法追溯）\n- 风险：\n  - 样式不符合 → desk reject\n  - margin 不对 → 被审稿人质疑诚信\n  - reference 格式错 → 被认为不规范\n- 流程：先查会议官网 templates → 找不到再 `WebSearch \"{venue} {year} latex template official\"` → 仍找不到汇报 Director（不要用就近年版本顶替）\n- `\\documentclass[]{}` 选项必须与目标 venue + 阶段（review / camera-ready）一致\n\n### 7.2 投稿要求逐项核对\n\n- 目标会议如要求 Checklist / Ethical Statement / Broader Impact Statement / Reproducibility Statement，必须**认真填每一项**，不要全写 N/A\n- 页数限制：查目标会议官网\n- 匿名化要求：review 版 vs camera-ready 版本设置不同\n- 行号开启（review 版常需）\n- 字体大小、margin 不得修改 sty 文件\n\n### 7.3 最终修改 10 项检查流程\n\n提交前必须逐一检查：\n1. 所有最新实验结果已全部录入\n2. 根据实验结果将叙事调至最优状态\n3. 附录所有内容在正文中被引用且融入叙事\n4. 无数据堆砌（每个数字服务于叙事推进）\n5. Abstract 和 Introduction 具有吸引力（不是实验报告风格）\n6. 全文主线统一（idea 变化后各章节逻辑一致）\n7. 所有专有名词有定义\n8. 无 AI 风格标志（dash、-ing phrases、过度分段）\n9. 图表知识密度高、无视觉遮挡\n10. Reference 覆盖直接相关方法、baseline、benchmark、理论基础\n\n## 更多 Skills（按需加载）\n\n执行相关任务前，先 Read 对应 skill 获取环境配置和最佳实践。\n\n- **ssh-env-setup** — 远程服务器 Python/CUDA 环境搭建规范——discovery-first 流程、PEP 668 处理、PyTorch 版本选择。当需要在远程服务器搭建训练环境时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/ssh-env-setup.skill.md`\n- **check-training-status** — 当用户问训练进度/实验状态/查状态时使用。用专用工具查看训练状态，禁止 ssh_execute。  →  `/home/ubuntu/agent-ml-research/skills/global/check-training-status.skill.md`\n- **rebuttal** — 撰写和优化学术 rebuttal——逐条回应审稿意见，生成 response letter。当收到审稿意见、需要写 rebuttal、回复 reviewer 评论时使用。关键词：rebuttal、审稿意见、reviewer response、author response、meta-review、AC 意见。  →  `/home/ubuntu/agent-ml-research/skills/global/rebuttal.skill.md`\n- **review-reviewer-session-start** — Review Reviewer session 启动初始化——检查论文格式、编译状态、材料清单。Review Reviewer 角色 session 启动时自动使用。  →  `/home/ubuntu/agent-ml-research/skills/global/review-reviewer-session-start.skill.md`\n- **reference-audit** — 引用验证与审计——检查 bib 条目完整性、引用真实性、格式一致性。写论文、审查论文、提交前检查引用时使用。关键词：citation verification、引用检查、bib 审计、fake citation、引用格式。  →  `/home/ubuntu/agent-ml-research/skills/global/reference-audit.skill.md`\n- **accelerate-distributed** — HuggingFace Accelerate 分布式训练指南——4行代码实现多GPU/DeepSpeed/FSDP/混合精度。多GPU训练时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/accelerate-distributed.skill.md`\n- **draw-paper-figure** — 生成学术论文级 matplotlib 图表——按 narrative_intent + design_notes 设计，从 pattern 库选用技法，远程 SSH 执行输出 PDF/PNG  →  `/home/ubuntu/agent-ml-research/skills/global/draw-paper-figure.skill.md`\n- **experiment-analysis** — 实验结果分析框架——统计显著性检验、消融分析、baseline 对比、可视化建议。分析实验结果或撰写论文 Results 部分时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/experiment-analysis.skill.md`\n- **hf-hub** — HuggingFace Hub CLI (hf) — 下载/上传模型和数据集、管理缓存、搜索论文和模型。涉及 HuggingFace 资源操作时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/hf-hub.skill.md`\n- **latex-paper** — ML 顶会论文 LaTeX 写作全流程——Claim-Evidence 方法论、引用防幻觉、顶会模板速查、投稿工程链、会议转投。写论文/投稿时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md`\n- **lm-eval-harness** — lm-evaluation-harness 模型评估指南——MMLU/GSM8K/HumanEval 等 60+ 学术基准测试。评估模型质量、对比实验时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/lm-eval-harness.skill.md`\n- **ml-experiment-guide** — 跨项目 ML 实验避坑指南——从多个项目沉淀的通用踩坑经验与最佳实践。当 Worker 准备写实验代码、或排查实验问题时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/ml-experiment-guide.skill.md`\n- **paper-banana** — 用 PaperBanana 生成学术图表——概念图（架构/流程/framework）首选，探索性统计图也可。LLM 写 matplotlib 代码 + VLM Critic 闭环迭代。需要 GOOGLE_API_KEY。  →  `/home/ubuntu/agent-ml-research/skills/global/paper-banana.skill.md`\n- **paper-image-extractor** — 从论文 PDF 或 arXiv 源码包提取图表——优先 arXiv 原始图片，回退 PDF 解析。用户说\"提取图\"/\"抽图\"/\"extract figures\"时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/paper-image-extractor.skill.md`\n- **peft-lora** — PEFT/LoRA/QLoRA 参数高效微调指南——LoRA 配置选择、QLoRA 量化训练、Adapter 管理与合并。微调大模型时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/peft-lora.skill.md`\n- **research-news** — 每日论文推荐——搜索 arXiv 最新论文，按相关性/新颖性/影响力评分，生成推荐列表。Director 说\"有什么新论文\"/\"最近进展\"/\"research news\"时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/research-news.skill.md`\n- **trl-training** — TRL (Transformer Reinforcement Learning) 训练指南——SFT/DPO/GRPO/KTO 配置与最佳实践。训练或对齐语言模型时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/trl-training.skill.md`\n- **wandb-guide** — W&B 查询最佳实践——如何高效使用 fetch_wandb_metrics / compare_wandb_runs / get_best_wandb_run 分析实验结果。分析实验指标时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/wandb-guide.skill.md`\n",
      "contentDiffersFromDisk": false
    },
    "displayPath": "projects/symb_invariant_consensus/.claude/CLAUDE.md"
  },
  "type": "attachment",
  "uuid": "3a40950c-9942-41ec-a204-961ef40cb856",
  "timestamp": "2026-05-19T04:02:05.766Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3",
  "sessionId": "94c4266a-dd51-40f0-bc57-040b308715ff",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
````

---

### Runtime record

_source line 19_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：Dual Bottleneck 方向成立但 Eff-K 预测力有噪声。K/T curves 有 outlier 需解释。需弱化 'predictor' 为 'necessary condition'，重心转向 oracle gap + remediation failures。Findings 可达。 核…",
  "leafUuid": "3a40950c-9942-41ec-a204-961ef40cb856",
  "sessionId": "94c4266a-dd51-40f0-bc57-040b308715ff"
}
```

---

### Runtime record

_source line 20_

```json
{
  "type": "ai-title",
  "aiTitle": "Condorcet independence analysis of self-consistency trace aggregation",
  "sessionId": "94c4266a-dd51-40f0-bc57-040b308715ff"
}
```

---

### Tool call

_source line 21 · 2026-05-19T04:02:10.227Z_

<details open><summary>🔧 Tool call — Read · `toolu_014N7frXxdZCStDHMeicbf1C`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/experiment_plan.yaml",
  "offset": 200,
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3a40950c-9942-41ec-a204-961ef40cb856",
  "isSidechain": false,
  "requestId": "req_011CbBG9GwCNLmtHBRVqVZbA",
  "type": "assistant",
  "uuid": "0c9d1908-a3e5-43b7-8882-ff937683ac77",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3",
  "sessionId": "94c4266a-dd51-40f0-bc57-040b308715ff",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0183LV9eg83DzChMYtc2PGkD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9571,
      "cache_read_input_tokens": 71632,
      "output_tokens": 121,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9571,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 121,
          "cache_read_input_tokens": 71632,
          "cache_creation_input_tokens": 9571,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9571
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

_source line 22 · 2026-05-19T04:02:10.274Z_

<details><summary>↩ Tool result · `toolu_014N7frXxdZCStDHMeicbf1C`</summary>

```text
200	  status: planned
201	  note: 'D024 新增. Dream 三档一致要求 Logic-LM/LINC 比较。CPU-only: 用 exp-001 已有 traces + FOL
202	    constraints 做单 trace verification then vote。'
203	- id: exp-016
204	  name: weighted_sc_baseline
205	  claim:
206	  - 1
207	  - 3
208	  description: 'Weighted SC baseline (Taubenfeld et al. 2024 style): weight votes
209	    by trace confidence/length/perplexity. CPU-only reanalysis of exp-001/002 data.
210	    Tests if simple weighting achieves same tiebreak quality without MAX-SAT.'
211	  priority: P1
212	  gpu_budget_hours: 0
213	  deps:
214	  - exp-001
215	  status: planned
216	  note: 'D024 新增. Dream 提出 weighted SC 是最直接竞争 baseline。实现方式: (1) uniform weight (=SC),
217	    (2) length-weighted, (3) log-prob weighted (如 traces 有 logprobs), (4) constraint-count
218	    weighted (no SAT)。'
219	- id: exp-017
220	  name: sica_strategyqa_14b
221	  claim:
222	  - 1
223	  - 2
224	  description: Qwen2.5-14B on StrategyQA 60 questions (K=12). Commonsense reasoning
225	    domain — high predicted C0 (35-50%) but implicit reasoning chains → low expected
226	    constraint quality. Tests capability trap in best-case-diversity scenario.
227	  priority: P0
228	  gpu_budget_hours: 1.5
229	  deps: []
230	  status: planned
231	  note: D025 新增. Reviewer 推荐 ROI 最高 benchmark。如 C0>30% 且 SICA≈SC → 直接证明 capability
232	    trap（diversity high but quality low → no gain）。
233	- id: exp-018
234	  name: sica_arc_challenge_14b
235	  claim:
236	  - 1
237	  - 2
238	  description: Qwen2.5-14B on ARC-Challenge 60 questions (K=12). Science reasoning,
239	    4-choice format. Tests constraint mechanism in multi-choice scenario + different
240	    domain.
241	  priority: P0
242	  gpu_budget_hours: 1.5
243	  deps: []
244	  status: planned
245	  note: D025 新增. 4选1格式测试 constraint mechanism 泛化能力。与 FOLIO (3-class) + GSM8K (open)
246	    + StrategyQA (binary) 形成答案格式多样性。
247	- id: exp-019
248	  name: constraint_quality_correlation
249	  claim:
250	  - 1
251	  - 2
252	  description: 'CPU-only analysis: compute constraint precision per domain × model,
253	    correlate with C0 and SICA-SC gap. Formalizes the capability trap as inverse C0-quality
254	    correlation. Uses data from exp-001/010/011/017/018.'
255	  priority: P0
256	  gpu_budget_hours: 0
257	  deps:
258	  - exp-001
259	  - exp-017
260	  - exp-018
261	  status: planned
262	  note: 'D025 新增. Hero figure (F2) 的数据来源。Constraint quality = (constraints consistent
263	    with ground truth) / (total constraints). 预期: high C0 domains (StrategyQA) have
264	    low quality, low C0 domains (math) have high quality but SICA=SC anyway.'
265	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0c9d1908-a3e5-43b7-8882-ff937683ac77",
  "isSidechain": false,
  "promptId": "d07b33c5-7e32-4212-9636-fcf6c376c96b",
  "type": "user",
  "uuid": "cd875876-0baf-4f22-9b79-733a18a2b239",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/experiment_plan.yaml",
      "content": "  status: planned\n  note: 'D024 新增. Dream 三档一致要求 Logic-LM/LINC 比较。CPU-only: 用 exp-001 已有 traces + FOL\n    constraints 做单 trace verification then vote。'\n- id: exp-016\n  name: weighted_sc_baseline\n  claim:\n  - 1\n  - 3\n  description: 'Weighted SC baseline (Taubenfeld et al. 2024 style): weight votes\n    by trace confidence/length/perplexity. CPU-only reanalysis of exp-001/002 data.\n    Tests if simple weighting achieves same tiebreak quality without MAX-SAT.'\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - exp-001\n  status: planned\n  note: 'D024 新增. Dream 提出 weighted SC 是最直接竞争 baseline。实现方式: (1) uniform weight (=SC),\n    (2) length-weighted, (3) log-prob weighted (如 traces 有 logprobs), (4) constraint-count\n    weighted (no SAT)。'\n- id: exp-017\n  name: sica_strategyqa_14b\n  claim:\n  - 1\n  - 2\n  description: Qwen2.5-14B on StrategyQA 60 questions (K=12). Commonsense reasoning\n    domain — high predicted C0 (35-50%) but implicit reasoning chains → low expected\n    constraint quality. Tests capability trap in best-case-diversity scenario.\n  priority: P0\n  gpu_budget_hours: 1.5\n  deps: []\n  status: planned\n  note: D025 新增. Reviewer 推荐 ROI 最高 benchmark。如 C0>30% 且 SICA≈SC → 直接证明 capability\n    trap（diversity high but quality low → no gain）。\n- id: exp-018\n  name: sica_arc_challenge_14b\n  claim:\n  - 1\n  - 2\n  description: Qwen2.5-14B on ARC-Challenge 60 questions (K=12). Science reasoning,\n    4-choice format. Tests constraint mechanism in multi-choice scenario + different\n    domain.\n  priority: P0\n  gpu_budget_hours: 1.5\n  deps: []\n  status: planned\n  note: D025 新增. 4选1格式测试 constraint mechanism 泛化能力。与 FOLIO (3-class) + GSM8K (open)\n    + StrategyQA (binary) 形成答案格式多样性。\n- id: exp-019\n  name: constraint_quality_correlation\n  claim:\n  - 1\n  - 2\n  description: 'CPU-only analysis: compute constraint precision per domain × model,\n    correlate with C0 and SICA-SC gap. Formalizes the capability trap as inverse C0-quality\n    correlation. Uses data from exp-001/010/011/017/018.'\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - exp-001\n  - exp-017\n  - exp-018\n  status: planned\n  note: 'D025 新增. Hero figure (F2) 的数据来源。Constraint quality = (constraints consistent\n    with ground truth) / (total constraints). 预期: high C0 domains (StrategyQA) have\n    low quality, low C0 domains (math) have high quality but SICA=SC anyway.'\n",
      "numLines": 66,
      "startLine": 200,
      "totalLines": 265
    }
  },
  "sourceToolAssistantUUID": "0c9d1908-a3e5-43b7-8882-ff937683ac77",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3",
  "sessionId": "94c4266a-dd51-40f0-bc57-040b308715ff",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-19T04:06:14.930Z_

I have all the context needed. Now generating the comprehensive median-tier imagined data for all planned and running experiments.

```yaml
tier: median
narrative_guidance: >
  Dual Bottleneck 框架方向正确但 Eff-K 作为定量预测器有噪声，需弱化为 "necessary condition that interacts with SC"。
  K/T sensitivity curves 呈大致 inverted-U / peak-at-0.7 但各有 1-2 个 non-monotonic outlier，
  用 error bar / CI overlay 展示 noise level，frame 为 "directionally consistent despite noise"。
  论文重心从 Condorcet 理论预测力转向 oracle gap (+14.22pp, p=2e-7) + 9 remediation failures (breadth argument)。
  Condorcet 框架降为 "explanatory lens" 而非 "predictive framework"。
  Seed variance 明确表述为 "Eff-K explains cross-model variance; within-model variance remains dominated by stochastic factors"。
  exp-050b ICL complication 放 discussion 作为 limitation / future work。
  投稿目标 Findings (≥3.0)；如 breadth of analysis 获审稿人认可可能升 Main (≤3.2)。

imagined_experiments:

  # ============================================================
  #  Core Model Evaluations (planned in experiment_plan)
  # ============================================================

  - name: "sica_k_ablation_14b"
    plan_id: "exp-002"
    description: "Qwen2.5-14B K sensitivity (K=6,8,11,12,16,20) on D012 60 questions"
    expected_results:
      n: 60
      K6_sica: 0.733
      K6_sc: 0.733
      K6_delta_pp: 0.0
      K8_sica: 0.717
      K8_sc: 0.750
      K8_delta_pp: -3.3
      K11_sica: 0.733
      K11_sc: 0.733
      K11_delta_pp: 0.0
      K12_sica: 0.717
      K12_sc: 0.750
      K12_delta_pp: -3.3
      K16_sica: 0.700
      K16_sc: 0.733
      K16_delta_pp: -3.3
      K20_sica: 0.700
      K20_sc: 0.717
      K20_delta_pp: -1.7
      all_K_sica_leq_sc: true
      kappa_14b_estimated: 0.76
      eff_k_range: "1.25–1.32"
    result_rationale: >
      Qwen-14B Fleiss' κ≈0.76，Eff-K 仅 1.25–1.32，trace 间几乎完全相关。
      增加 K 只叠加冗余 trace 而不增加独立信息。Qwen SC 基线 ~75% 处于 Type A regime
      (confirmation bias)，约束方向镜像模型偏差。因此所有 K 值 SICA ≤ SC。
      K=11 (odd) 消除 exact-tie 场景，gap=0 确认 Qwen 上 SICA 无 tiebreak 之外的获益机制。
      Larger K 时 SICA 略劣，因更多约束放大了 confirmation bias。
    tables: ["T5"]
    figures_description:
      - "F3 中 Qwen 对照线 (flat/declining)，与 Mistral inverted-U 形成对比"
    analysis: >
      Qwen 全 K 值 SICA≤SC 是 Eff-K 理论的 negative control。K=11 gap=0 额外确认
      SICA 对 Qwen 无非 tiebreak 价值。与 exp-051 (Mistral inverted-U) 对比是 T5 的核心叙事。

  - name: "tiebreak_baseline_analysis"
    plan_id: "exp-003"
    description: "SICA vs SC-random/deterministic tiebreak，CPU-only 重分析"
    expected_results:
      n_tiebreak_cases: 5
      sica_tiebreak_win_rate: 0.80
      random_tiebreak_win_rate: 0.50
      alphabetical_tiebreak_win_rate: 0.60
      first_seen_tiebreak_win_rate: 0.40
    result_rationale: >
      Qwen-14B D012 中仅 ~5 个 tied cases (C0=53% 但多数 multi-candidate 问题 SC 有明确多数)。
      SICA 4/5 选对 (80%) 优于 random (50%)，但 n 太小无统计显著性。
      说明 SICA tiebreak 机制本身有效，但 Qwen 上 tied 场景太少，整体增益被稀释到 ~0pp。
    tables: ["T1 footnote"]
    figures_description: []
    analysis: >
      Tiebreak 是 SICA 唯一有效的子机制。Qwen 高 κ 条件下约束无法在 non-tied cases 中翻转 SC，
      限制了总体影响。回应 reviewer concern #13 (random tiebreak baseline)。

  - name: "sica_7b_scaling"
    plan_id: "exp-004"
    description: "Qwen2.5-7B-Instruct on D012 60 questions (K=12, T=0.7)"
    expected_results:
      n: 60
      sica_accuracy: 0.683
      sc_accuracy: 0.683
      delta_pp: 0.0
      multi_candidate_rate: 0.433
      extraction_rate: 0.942
      mcnemar_p: 1.0
      kappa_estimated: 0.68
      eff_k_estimated: 1.42
      folio_sica: 0.767
      folio_sc: 0.733
      proofwriter_sica: 0.600
      proofwriter_sc: 0.633
    result_rationale: >
      Qwen-7B 比 14B 弱但同家族，κ 仍高 (~0.68)，Eff-K~1.42。C0 比 14B 高 (43% vs 38%)
      但 constraint quality 同样受 Qwen 系 confirmation bias 影响。SC 基线 ~68% 处于
      Type A 边缘。Delta=0 因为 FOLIO 微正 (+3.3pp) 被 PW 微负 (-3.3pp) 抵消。
      Qwen 家族内 scaling 不改变 SICA 效果方向。
    tables: ["T1", "T3"]
    figures_description:
      - "F2 scatter: Qwen-7B (SC≈68%, Δ=0)"
    analysis: >
      Qwen-7B 进一步确认 Qwen 家族的 independence bottleneck。即使 SC 降到 68%
      (更接近 Goldilocks)，trace κ 仍高到 SICA 无法获益。支持 "Eff-K 是跨模型必要条件"。

  - name: "qwq_32b_operating_regime"
    plan_id: "exp-005"
    description: "QwQ-32B 已有数据汇总为 negative control"
    expected_results:
      total_problems: 46
      qwq_aggregate_c0_effective_pct: 2.6
      aime_c0: 0.0
      proofwriter_c0: 18.75
      folio_c0: 0.0
      aime_delta_pp: 0.0
      proofwriter_delta_pp: -5.9
      kappa_estimated: 0.92
      eff_k_estimated: 1.08
    result_rationale: >
      QwQ-32B 作为 reasoning model，内置 CoT 极度 deterministic。即使 T=0.7，reasoning chain
      使 trace 间 κ→0.92，Eff-K→1.08 (几乎退化为单次采样)。C0 有效率仅 2.6%，SICA≡SC。
      这是 Eff-K 框架最极端的验证：Eff-K≈1 时任何聚合方法都无法超越 single sample。
    tables: ["T1", "T3"]
    figures_description:
      - "F2 scatter 最右上角: QwQ-32B (SC high, Δ=0)"
    analysis: >
      QwQ-32B 是 degenerate case。完美回应 reviewer concern #12 "为什么不用 reasoning model"。
      Reasoning model trace 更 deterministic → C0→0 → SICA 退化。放 Appendix 详述。

  - name: "c0_diagnostic_validation"
    plan_id: "exp-006"
    description: "C0 vs SICA-SC gap 跨所有 model×dataset 条件的 scatter 分析"
    expected_results:
      n_conditions: 12
      c0_delta_pearson_r: 0.45
      c0_delta_pearson_p: 0.14
      c0_below_20_conditions: 4
      c0_below_20_all_delta_leq_0: true
      c0_above_20_positive_delta_rate: 0.50
      outlier_conditions: 2
      c0_necessary_not_sufficient: true
    result_rationale: >
      C0<20% 的 4 个条件 (QwQ-32B, ARC-14B, GSM8K-14B, Qwen-72B) 全部 delta≤0，
      C0 作为必要条件方向正确。但 C0>20% 不保证正 delta：LLaMA FOLIO-204 C0=62% delta=-2.5pp，
      Mistral PW600 C0=50% delta=-2.8pp。r=0.45 方向正确但 p=0.14 不显著 (12 个点太少)。
      C0 只捕捉 diversity 维度，不反映 constraint quality，因此不够做 "predictor"。
    tables: ["T1 summary"]
    figures_description:
      - "F2 hero figure: C0 (x) vs Δpp (y) scatter，C0=20% 虚线 threshold"
    analysis: >
      C0 零成本部署诊断的价值在于 negative predictive power：C0<20% → 不要部署 SICA。
      Positive prediction 需结合 SC level 和 Eff-K。这是 median tier "necessary condition"
      叙事的定量支撑，也是 Claim 4 (C0+SC diagnostic) 的核心证据。

  - name: "sica_72b_awq"
    plan_id: "exp-007"
    description: "Qwen2.5-72B-Instruct AWQ 4-bit on D012 60 questions"
    expected_results:
      n: 60
      sica_accuracy: 0.833
      sc_accuracy: 0.850
      delta_pp: -1.7
      multi_candidate_rate: 0.15
      extraction_rate: 0.95
      kappa_estimated: 0.82
      eff_k_estimated: 1.20
      mcnemar_p: 1.0
    result_rationale: >
      72B 是 Qwen 家族最强模型，SC 基线 ~85%，C0 仅 15%。κ≈0.82，Eff-K≈1.20。
      完全处于 Type A regime：trace 高度一致 → 约束全部 confirm 多数答案 → SICA=SC 或略劣。
      delta=-1.7pp 因为个别 case 中 SICA 约束排除了原本正确的少数答案。
      形成 Qwen 内 7B/14B/72B scaling curve：越强 → C0 越低 → SICA 越无效到有害。
    tables: ["T1"]
    figures_description:
      - "F2 scatter: Qwen-72B (SC≈85%, Δ≈-1.7)"
    analysis: >
      72B 完善 Qwen 家族 scaling 分析：7B(SC=68%,Δ=0) → 14B(SC=75%,Δ=+0.3) → 72B(SC=85%,Δ=-1.7)。
      Model size↑ → SC↑ C0↓ Eff-K↓。完美支持 Type A regime 理论。回应 reviewer concern #5 模型覆盖。

  - name: "constraint_quality_case_studies"
    plan_id: "exp-008"
    description: "5-10 道代表性问题的约束质量定性分析"
    expected_results:
      n_cases: 8
      trivially_satisfied_pct: 43
      semantically_meaningful_pct: 35
      confirmation_bias_aligned_pct: 55
      extraction_error_pct: 12
      cases_constraint_flips_correct: 2
      cases_constraint_flips_wrong: 1
    result_rationale: >
      定性分析揭示三种典型约束模式：(1) 43% trivially satisfied — 被所有候选答案满足；
      (2) 35% semantically meaningful 但方向与模型多数答案一致 (confirmation bias)；
      (3) 12% 提取错误 (语法错误、变量名不一致)。净效果：~92% 约束 ARE discriminative (exp-023)
      但 discrimination 方向与模型偏差对齐。2/8 cases 翻转正确，1/8 翻转错误。
    tables: ["T4"]
    figures_description:
      - "F4 stacked bar: constraint quality breakdown by category"
    analysis: >
      Case studies 为 T4 taxonomy 提供具体例子。关键 insight：问题不在约束缺乏判别力，
      而在 discriminative 约束的区分方向与模型偏差一致。是 confirmation bias 的 mechanism-level 证据。

  - name: "overhead_analysis"
    plan_id: "exp-009"
    description: "SICA pipeline wall-time 分解 (n=804)"
    expected_results:
      n: 804
      mean_total_wall_s: 61.6
      trace_gen_pct: 51.3
      extract_pct: 47.0
      dedup_pct: 1.6
      maxsat_pct: 0.005
      sica_overhead_pct: 48.7
      p90_overhead_pct: 57.6
    result_rationale: >
      SICA 额外开销几乎全部来自 constraint extraction (LLM 二次调用 ~47%)，MaxSAT 求解极快 (<0.01%)。
      总成本约 SC 的 2 倍。在 median tier 下 SICA 增益 ≤+5pp 且仅在特定条件下有效，
      但成本翻倍。Paper 应 frame 为 analysis tool 而非 practical improvement。
    tables: ["Appendix overhead table"]
    figures_description: []
    analysis: >
      48.7% overhead 全来自 extraction。如果 extraction 可做更好 (oracle gap +14pp 显示上限)，
      overhead 合理。但当前 self-extraction 质量使 overhead 不值。支持 pure analysis framing。

  - name: "sica_llama_8b"
    plan_id: "exp-011"
    description: "LLaMA-3.1-8B-Instruct on D012 60 questions (K=12, T=0.7)"
    expected_results:
      n: 60
      sica_accuracy: 0.667
      sc_accuracy: 0.600
      delta_pp: 6.67
      multi_candidate_rate: 0.617
      extraction_rate: 0.856
      mcnemar_p: 0.219
      kappa_estimated: 0.38
      eff_k_estimated: 2.35
      folio_delta_pp: 10.0
      proofwriter_delta_pp: 3.33
      truncated_traces: 44
    result_rationale: >
      LLaMA-8B SC 基线 ~60%，C0 高达 62%，处于 Goldilocks zone 边缘。κ≈0.38，Eff-K≈2.35，
      trace 间独立性明显高于 Qwen。+6.67pp 是 D012 上最大 raw delta，但 n=60 致 p=0.22 不显著。
      FOLIO 子集 +10pp 突出。但 exp-020 (LLaMA FOLIO-204 delta=-2.45pp) 警告这可能是 small-n artifact。
      在 median tier 中是 "suggestive but unreplicated"。
    tables: ["T1", "T3"]
    figures_description:
      - "F2 scatter: LLaMA-8B D012 (SC≈60%, Δ=+6.7, n.s.) 高亮但标注 n=60"
    analysis: >
      LLaMA-8B 支持 "moderate Eff-K can enable gains" 但 exp-020 的反转 (-2.45pp) 限制了 claim 强度。
      在 paper 中作为 directional evidence，不能做 confirmation。

  - name: "gsm8k_pilot_14b"
    plan_id: "exp-012"
    description: "Qwen2.5-14B on GSM8K 30-question pilot (K=12)"
    expected_results:
      n: 30
      sica_accuracy: 0.967
      sc_accuracy: 0.967
      delta_pp: 0.0
      multi_candidate_rate: 0.133
      extraction_success_rate: 0.147
    result_rationale: >
      Qwen-14B GSM8K SC~97%，几乎全对。C0 仅 13%。更关键的是 extraction rate 仅 15% —
      数学域 constraint extraction 困难得多 (开放答案空间，数值计算而非逻辑推理)。
      GSM8K 是 Type A 极端 + Type B 部分：SC 太高 AND domain formalization 困难。
    tables: ["T1"]
    figures_description:
      - "F2 scatter: GSM8K (SC≈97%, Δ=0)"
    analysis: >
      GSM8K 贡献两个 insight：(1) 数学域 extraction 本身困难，C0 不适用；
      (2) 简单 math 上 SC 太高无论如何 SICA 无效。支持 Type B (domain formalizability)。

  - name: "constraint_ablation"
    plan_id: "exp-013"
    description: "MaxSAT vs count-only vs random-weight 消融 (n=804)"
    expected_results:
      maxsat_accuracy: 0.765
      count_only_accuracy: 0.766
      random_weight_accuracy: 0.759
      sc_baseline: 0.762
      agreement_maxsat_vs_countonly: "803/804"
      mcnemar_all_nonsignificant: true
    result_rationale: >
      MaxSAT 与 count-only agreement 达 803/804 (99.9%)。MaxSAT 的 satisfiability weighting
      在当前约束质量下无额外贡献 — 简单计数就能达到相同效果。根因：约束间高度冗余 (同 trace 提取
      的约束倾向同方向)，MaxSAT 组合优化退化为简单计数。是 independence bottleneck 的 mechanism-level 证据。
    tables: ["T1 footnote / Appendix"]
    figures_description: []
    analysis: >
      MaxSAT=count-only 是 capability trap 核心机制证据。若约束独立，MaxSAT 应发现组合 patterns。
      约束高冗余使求解器退化。对比 exp-031 oracle (+14pp) 证明 solver 本身没问题，是输入约束质量限制。

  - name: "sica_deepseek_r1_llama_8b"
    plan_id: "exp-014"
    description: "DeepSeek-R1-Distill-Qwen-7B on D012 60 questions"
    expected_results:
      n: 60
      sica_accuracy: 0.683
      sc_accuracy: 0.717
      delta_pp: -3.33
      multi_candidate_rate: 0.583
      extraction_rate: 0.839
      truncated_traces: 72
      mcnemar_p: 0.480
      kappa_estimated: 0.52
      eff_k_estimated: 1.78
    result_rationale: >
      DeepSeek-R1 蒸馏版 trace 带 extended thinking，C0=58% (vs QwQ 2.6%) 但 72/720 traces
      被 truncated (max_tokens 限制)。Truncation 破坏 constraint extraction 质量导致 delta=-3.33pp。
      Eff-K 理论预测方向正确 (moderate Eff-K≈1.78 应有正向潜力) 但 truncation confound 使预测失效。
      这是 median tier "noise point" 之一。
    tables: ["T1", "T3"]
    figures_description:
      - "F2 scatter: DeepSeek-R1 标注 'truncation confound'"
    analysis: >
      DeepSeek-R1 的 negative delta 由 truncation artifact 驱动，非 independence bottleneck 反例。
      Paper 中作为 caveat 处理。占 Eff-K 预测失败的 12 条件中的 1 个。

  - name: "logic_lm_baseline"
    plan_id: "exp-015"
    description: "Logic-LM × K + majority vote baseline on FOLIO"
    expected_results:
      n: 204
      logic_lm_k12_accuracy: 0.740
      sc_k12_accuracy: 0.755
      sica_k12_accuracy: 0.745
      logic_lm_vs_sc_delta_pp: -1.5
      logic_lm_single_trace_accuracy: 0.720
      fol_parse_rate: 0.82
    result_rationale: >
      Logic-LM 对每条 trace 独立做 FOL extraction + Z3 verification 然后 majority vote。
      在 Qwen-14B 高 κ 条件下，Logic-LM ≈ SC 因为每条 trace 的 FOL verification 大多验证了
      trace 自身的答案 (self-consistency within trace)。FOL parse rate ~82% 限制了有效 trace 数量。
      Logic-LM 略劣于 SC 因为 parse failure 的 trace 被丢弃降低了 vote pool。
    tables: ["Appendix baseline comparison"]
    figures_description: []
    analysis: >
      Logic-LM 证明 FOL extraction 本身不是 SICA 的 value add —— 差异在于跨 trace aggregation (MaxSAT)。
      但 MaxSAT=count-only (exp-013)，所以 SICA 唯一贡献是 tiebreak。加强 capability trap 论证。

  - name: "weighted_sc_baseline"
    plan_id: "exp-016"
    description: "Weighted SC baseline (uniform/length/inv-length/constraint-count) on 804 questions"
    expected_results:
      sc_uniform: 0.762
      inv_length_weighted: 0.767
      length_weighted: 0.753
      constraint_count_weighted: 0.753
      sica: 0.765
      inv_length_vs_sc_p: 0.453
      all_nonsignificant: true
    result_rationale: >
      所有 weighting scheme 与 SC 无显著差异。Inv-length (+0.5pp) 略正 — 更短 trace 更可能是
      confident 回答。但效果太小属随机波动。关键 takeaway：simple weighting 无法替代 independence —
      问题不在 vote quality 而在 vote independence。Correlated votes 怎么 weight 仍然 correlated。
    tables: ["Appendix baseline comparison"]
    figures_description: []
    analysis: >
      回应 reviewer concern #15。所有 weighting 全 n.s.，证明 independence bottleneck 是根本性的，
      不能通过 simpler weighting 解决。

  - name: "sica_strategyqa_14b"
    plan_id: "exp-017"
    description: "Qwen2.5-14B on StrategyQA 60 questions (K=12)"
    expected_results:
      n: 60
      sica_accuracy: 0.567
      sc_accuracy: 0.533
      delta_pp: 3.33
      multi_candidate_rate: 0.10
      extraction_rate_trace: 0.704
      bootstrap_p: 0.135
      contradiction_detected: 5
      discordant_sica_wins: 2
      discordant_sc_wins: 0
    result_rationale: >
      StrategyQA binary (Yes/No)，Qwen-14B SC~53% (接近随机)。C0 仅 10% 因为 binary format
      只有 2 个候选，SC 容易 unanimous。Extraction rate 仅 70% (commonsense 难形式化为 FOL)。
      +3.33pp 正向但 n.s. (仅 2 个 discordant cases)。Type B partial case：domain 部分可形式化
      但约束质量低且 C0 低。
    tables: ["T1"]
    figures_description:
      - "F2 scatter: StrategyQA (SC≈53%, Δ=+3.3, n.s.)"
    analysis: >
      StrategyQA 低 C0 (10%) 说明 binary format 限制了 SICA 应用空间。即使 SC 在 Goldilocks zone，
      answer space 太小导致 SC 容易 unanimous。支持 "C0+SC two-dimensional diagnostic"。

  - name: "sica_arc_challenge_14b"
    plan_id: "exp-018"
    description: "Qwen2.5-14B on ARC-Challenge 60 questions (K=12)"
    expected_results:
      n: 60
      sica_accuracy: 0.950
      sc_accuracy: 0.967
      delta_pp: -1.67
      multi_candidate_rate: 0.05
      extraction_rate: 1.0
      contradiction_detected: 3
      discordant_sica_wins: 0
      discordant_sc_wins: 1
    result_rationale: >
      Qwen-14B ARC-Challenge SC=96.7%，极高基线。C0 仅 5% — 虽是 4-choice format (理论上 C0 应更高)
      但 14B 太强，高度确信一个选项。delta=-1.67pp 因仅有的 3 个 multi-candidate 问题中 SICA 1 个选错。
      Type A extreme：模型太强 → C0→0 → SICA 退化。
    tables: ["T1"]
    figures_description:
      - "F2 scatter: ARC (SC≈97%, Δ=-1.7)"
    analysis: >
      ARC 的 4-choice format 理论上给 SICA 更多空间，但实际 C0 极低。
      说明 C0 主要由模型能力决定而非答案格式。Type A 极端案例。

  - name: "constraint_quality_correlation"
    plan_id: "exp-019"
    description: "Constraint precision × C0 × SICA-SC gap 跨域跨模型相关分析"
    expected_results:
      n_conditions: 12
      constraint_precision_mean: 0.62
      constraint_precision_range: [0.45, 0.82]
      c0_quality_correlation_r: -0.35
      c0_quality_correlation_p: 0.26
      quality_delta_correlation_r: 0.28
      quality_delta_correlation_p: 0.38
      effk_sc_joint_prediction_correct: 8
      effk_sc_joint_prediction_total: 12
      false_positive_conditions:
        - "LLaMA-8B D012 (Eff-K=2.35, SC=60% → predicted positive, actual n.s.)"
        - "StrategyQA-14B (SC=53% in zone but C0=10% → no room)"
      false_negative_conditions:
        - "DeepSeek-R1 (truncation confound)"
        - "exp-050b ICL (trace generation characteristic change)"
    result_rationale: >
      高 SC 条件 (Qwen-14B/72B): quality~0.75-0.82, C0 低 → delta=0。
      中 SC 条件 (Mistral FOLIO): quality~0.60-0.65, C0 中等 → delta variable。
      低 SC 条件 (Mistral PW600): quality~0.45-0.50, C0 高 → delta negative。
      C0-quality 反相关 r=-0.35 方向正确但 p=0.26 (12 点太少+seed variance)。
      Eff-K+SC 联合预测 8/12 方向正确：2 false positive (LLaMA D012, StrategyQA)，
      2 edge case (DeepSeek truncation, exp-050b ICL)。8/12 支持 "necessary condition"
      但不够强做 "predictor"。
    tables: ["T3 extended", "T4"]
    figures_description:
      - "F2 hero: SC vs Δ scatter with Eff-K color coding and constraint quality annotations"
    analysis: >
      8/12 方向正确是 median tier 最关键的 qualification。Paper 核心表述：
      "Eff-K explains cross-model variance; within-model variance remains dominated by stochastic factors."
      F2 用 Eff-K color coding 展示跨模型 pattern + error bar 展示 within-seed noise。

  # ============================================================
  #  Running Experiments — Critical for Paper Claims
  # ============================================================

  - name: "mistral_k_sensitivity"
    plan_id: "exp-051"
    description: "Mistral-7B K sensitivity (K=4,8,12,16,20) on FOLIO 204, seed=42"
    expected_results:
      n: 204
      K4_sc_pct: 55.4
      K4_sica_pct: 54.9
      K4_delta_pp: -0.5
      K4_eff_k: 1.60
      K4_mcnemar_p: 0.85
      K8_sc_pct: 54.9
      K8_sica_pct: 59.3
      K8_delta_pp: 4.4
      K8_eff_k: 1.78
      K8_mcnemar_p: 0.030
      K12_sc_pct: 54.4
      K12_sica_pct: 58.3
      K12_delta_pp: 3.9
      K12_eff_k: 1.85
      K12_mcnemar_p: 0.022
      K16_sc_pct: 54.4
      K16_sica_pct: 55.9
      K16_delta_pp: 1.5
      K16_eff_k: 1.88
      K16_mcnemar_p: 0.38
      K20_sc_pct: 53.9
      K20_sica_pct: 55.9
      K20_delta_pp: 2.0
      K20_eff_k: 1.90
      K20_mcnemar_p: 0.30
      peak_K: 8
      non_monotonic_points: ["K=8 高于 K=12", "K=20 略高于 K=16"]
      inverted_u_visual: "大致 inverted-U 但 K=8 是实际最高点 (+4.4pp)，K=20 相对 K=16 有微弱反弹"
    result_rationale: >
      Mistral FOLIO seed42 是唯一有正向 SICA 效果的核心条件。K sensitivity 预期大致 inverted-U：
      — K=4 (Eff-K=1.60): trace 太少，约束不足以可靠 discriminate，delta≈0。
      — K=8 (Eff-K=1.78): 甜区 — 足够多约束但冗余尚低。约束间 overlap 比 K=12 更低，
        产生 non-monotonic 高点 +4.4pp。这是核心 outlier。
      — K=12 (Eff-K=1.85): delta=+3.9pp，与 exp-033 的 +4.9pp 接近但略低 (K ablation 用
        K=20 traces 的 subset，与 exp-033 独立生成的 K=12 traces 有差异)。
      — K=16 (Eff-K=1.88): 冗余约束增加，confirmation bias dominate，delta 下降到 +1.5pp。
      — K=20 (Eff-K=1.90): 微弱反弹 +2.0pp — 第二个 non-monotonic 点。可能因 K=20 采样到
        更多 minority traces 偶然包含有用 diverse constraint。
      K=8 > K=12 是 median tier 的核心 outlier。Paper 应用 CI overlay + error bar 处理。
    tables: ["T5"]
    figures_description:
      - "F3 主图: K vs Δpp 折线 (Mistral inverted-U with CI bands + Qwen flat 对照)，K vs Eff-K 次轴"
    analysis: >
      K sensitivity inverted-U 部分验证 Eff-K 框架：K↑ → Eff-K↑ (diminishing returns) → delta 先升后降。
      但 K=8 > K=12 的 non-monotonicity 说明 Eff-K 不是唯一因素。
      Paper frame: "directionally consistent despite noise; peak at K=8-12 supports moderate K recommendation."
      与 Qwen flat line 对比是 T5/F3 核心叙事。

  - name: "multitemp_mistral_folio"
    plan_id: "exp-055"
    description: "Multi-temperature ensemble (T=0.3/0.5/0.7/1.0 × 3 traces each = K=12) Mistral FOLIO 204"
    expected_results:
      n: 204
      sc_accuracy_pct: 54.4
      sica_multitemp_pct: 53.9
      delta_pp: -0.5
      ci_95: [-3.0, 1.5]
      ci_includes_positive: true
      mcnemar_p: 0.75
      kappa_multitemp: 0.46
      eff_k_multitemp: 1.94
    result_rationale: >
      Multi-temp 设计意图通过温度多样性增加 trace independence。但 trace 间 structural correlation
      主要来自模型权重而非采样温度。κ=0.46 (vs single-temp T=0.7 κ=0.50) 仅微幅下降，
      Eff-K 从 1.85 增到 1.94 — 微弱 independence 提升不足以克服混合温度的 constraint quality 下降
      (低 T trace 更 repetitive 且 extraction 更 noisy，高 T trace 更 random)。
      CI [-3.0, +1.5] 包含正值，不能宣称 definitively fails，只能说 "consistent with null"。
    tables: ["Appendix remediation table"]
    figures_description: []
    analysis: >
      Multi-temp 是第 9 种 remediation failure (最弱证据，CI 跨 0)。Paper 处理为：
      "multi-temp did not significantly improve; any positive effect, if it exists,
      is small relative to the oracle gap (+14pp)."

  - name: "mistral_folio204_t03"
    plan_id: "exp-057"
    description: "Mistral-7B FOLIO 204 at T=0.3"
    expected_results:
      n: 204
      sc_accuracy_pct: 53.9
      sica_accuracy_pct: 55.4
      delta_pp: 1.5
      mcnemar_p: 0.42
      ci_95: [-2.0, 5.0]
      multi_candidate_rate: 0.65
      kappa_estimated: 0.55
      eff_k_estimated: 1.73
      extraction_rate: 0.96
    result_rationale: >
      T=0.3 使 trace 更 deterministic，κ↑至 0.55 (vs T=0.7 的 0.50)，Eff-K↓至 1.73。
      理论上应更差。但 median tier 预测意外正值 +1.5pp：低温 trace 虽更 correlated
      但也更 confident，约束表达更一致 (fewer extraction errors)。Quality↑ 部分抵消 independence↓。
      +1.5pp 属 stochastic noise (CI [-2, 5] 跨 0)。
      这是 T sensitivity curve 的关键 complication：T=0.3 意外正值打破 monotonicity。
    tables: ["Appendix T sensitivity table"]
    figures_description:
      - "Appendix: T vs Δpp 折线图，T=0.3 标注 CI overlay"
    analysis: >
      T=0.3 +1.5pp 是 narrative complication。理论预测低 T → 差效果，但实际微正。
      CI 跨 0 所以与 null 一致。Frame: "temperature effect directionally consistent
      (peak at T=0.7) despite noise at T=0.3."

  - name: "mistral_folio204_t05"
    plan_id: "exp-058"
    description: "Mistral-7B FOLIO 204 at T=0.5"
    expected_results:
      n: 204
      sc_accuracy_pct: 54.4
      sica_accuracy_pct: 57.2
      delta_pp: 2.8
      mcnemar_p: 0.15
      ci_95: [-0.5, 6.0]
      multi_candidate_rate: 0.75
      kappa_estimated: 0.48
      eff_k_estimated: 1.81
      extraction_rate: 0.97
    result_rationale: >
      T=0.5 是 T=0.3 和 T=0.7 的插值。κ=0.48 介于两者之间，Eff-K=1.81。
      Delta +2.8pp 正向但 p=0.15 不显著。完整 T curve: T=0.3(+1.5) → T=0.5(+2.8)
      → T=0.7(+4.9) → T=1.0(+0.5)。大致 peak-at-0.7 但 T=0.3 意外正值使 curve 不完全 monotonic。
      T=0.5 的 trace 比 T=0.3 更 diverse 但比 T=0.7 更 consistent，quality-independence trade-off
      使效果介于两者之间。
    tables: ["Appendix T sensitivity table"]
    figures_description:
      - "Appendix: T vs Δpp with full curve T=0.3/0.5/0.7/1.0 and CI bands"
    analysis: >
      完整 T curve 支持 "T=0.7 peak" 但不完全 monotonic。Paper frame:
      "SICA gains are concentrated in narrow T range around 0.5-0.7; extreme fragility
      to hyperparameter choice is itself evidence of the independence bottleneck."

  # ============================================================
  #  Running Experiments — Extended Evaluations
  # ============================================================

  - name: "14b_pw600_16639"
    plan_id: "exp-039"
    description: "Qwen2.5-14B PW-D5-600 with max_tokens=16639 (longer context rerun)"
    expected_results:
      n: 600
      sica_accuracy_pct: 75.8
      sc_accuracy_pct: 75.2
      delta_pp: 0.6
      mcnemar_p: 0.65
      extraction_rate: 0.97
      contradiction_rate: 0.018
      kappa_estimated: 0.75
      eff_k_estimated: 1.30
    result_rationale: >
      16639 token context 解决早期 truncation 问题，extraction rate 89%→97%。
      但 Qwen-14B κ≈0.75 Eff-K≈1.30 不变。Delta +0.6pp (比 sica_expanded_14b 的 +0.3pp 略好)
      因为 better extraction 减少 noise constraints，但 independence bottleneck 仍限制。
      n=600 给出更 precise estimate：SICA 在 Qwen PW 上 true effect ~0.5pp 但远不显著。
    tables: ["T1"]
    figures_description: []
    analysis: >
      Extraction improvement (89→97%) 仅转化 ~0.3pp 额外增益。
      证明 extraction quality 有微弱贡献但远不足以克服 independence bottleneck。

  - name: "qwen3_pw600_16639"
    plan_id: "exp-040"
    description: "Qwen3-14B PW-D5-600 with max_tokens=16639"
    expected_results:
      n: 600
      sica_accuracy_pct: 76.2
      sc_accuracy_pct: 75.8
      delta_pp: 0.4
      mcnemar_p: 0.72
      extraction_rate: 0.99
      contradiction_rate: 0.025
      kappa_estimated: 0.72
      eff_k_estimated: 1.35
    result_rationale: >
      Qwen3 extraction 更好 (99%) 且约束更多 (exp-027 显示 unique 7031)。
      但 κ 仅微降 (0.72 vs Qwen2.5 0.75)，Eff-K 微升 (1.35 vs 1.30)。
      Qwen 家族 generation pattern 跨代相对稳定。Delta +0.4pp 在 noise range 内。
      更好 extraction 被更高 contradiction rate (2.5%) 部分抵消。
    tables: ["T1"]
    figures_description: []
    analysis: >
      Qwen3 vs Qwen2.5 generational scaling 不改变 fundamental picture。
      支持 "generational scaling does not resolve independence bottleneck" (remediation failure 之一)。

  - name: "llama8b_pw600"
    plan_id: "exp-048"
    description: "LLaMA-3.1-8B PW-D5-600"
    expected_results:
      n: 600
      sica_accuracy_pct: 62.2
      sc_accuracy_pct: 60.8
      delta_pp: 1.4
      mcnemar_p: 0.32
      multi_candidate_rate: 0.55
      extraction_rate: 0.85
      kappa_estimated: 0.40
      eff_k_estimated: 2.22
    result_rationale: >
      LLaMA-8B PW600 SC~61% (Goldilocks zone)，C0=55%。κ≈0.40, Eff-K≈2.22 — 比 Qwen 更
      independent 但低于 Mistral PW (κ=0.21, Eff-K=3.63)。Delta +1.4pp 正向但 n.s.
      n=600 给出比 D012 (n=60) 更 tight 的 CI，确认 LLaMA PW 有微弱正向趋势但不 significant。
      与 exp-046 (Mistral PW600 delta=-2.83pp, SC=39%) 对比验证 dual bottleneck：
      LLaMA 满足 SC>50% → delta 正向；Mistral 不满足 → delta 负向。
    tables: ["T1"]
    figures_description:
      - "F2 scatter: LLaMA-8B PW600 (SC≈61%, Δ=+1.4) vs Mistral PW600 (SC≈39%, Δ=-2.8)"
    analysis: >
      LLaMA vs Mistral PW600 对比是 dual bottleneck (independence + quality) 的直接证据。
      两者 Eff-K 都较高 (2.22 vs 3.63) 但 SC 差异导致完全不同结果。
      支持 "sufficient Eff-K AND sufficient SC" 的联合条件。
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cd875876-0baf-4f22-9b79-733a18a2b239",
  "isSidechain": false,
  "requestId": "req_011CbBG9cyxExoegyL4TTMMj",
  "type": "assistant",
  "uuid": "5865803c-958c-497c-aad2-a4f55718cd45",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3",
  "sessionId": "94c4266a-dd51-40f0-bc57-040b308715ff",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AMiG2XQwzvjC39UJRCgw6d",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1157,
      "cache_read_input_tokens": 81203,
      "output_tokens": 12467,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1157,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 12467,
          "cache_read_input_tokens": 81203,
          "cache_creation_input_tokens": 1157,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1157
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

_source line 24_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：Dual Bottleneck 方向成立但 Eff-K 预测力有噪声。K/T curves 有 outlier 需解释。需弱化 'predictor' 为 'necessary condition'，重心转向 oracle gap + remediation failures。Findings 可达。 核…",
  "leafUuid": "5865803c-958c-497c-aad2-a4f55718cd45",
  "sessionId": "94c4266a-dd51-40f0-bc57-040b308715ff"
}
```

---

### Runtime record

_source line 25_

```json
{
  "type": "ai-title",
  "aiTitle": "Condorcet independence analysis of self-consistency trace aggregation",
  "sessionId": "94c4266a-dd51-40f0-bc57-040b308715ff"
}
```

---

### Runtime record

_source line 26_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：Dual Bottleneck 方向成立但 Eff-K 预测力有噪声。K/T curves 有 outlier 需解释。需弱化 'predictor' 为 'necessary condition'，重心转向 oracle gap + remediation failures。Findings 可达。 核…",
  "leafUuid": "5865803c-958c-497c-aad2-a4f55718cd45",
  "sessionId": "94c4266a-dd51-40f0-bc57-040b308715ff"
}
```

---

### Runtime record

_source line 27_

```json
{
  "type": "ai-title",
  "aiTitle": "Condorcet independence analysis of self-consistency trace aggregation",
  "sessionId": "94c4266a-dd51-40f0-bc57-040b308715ff"
}
```

---
