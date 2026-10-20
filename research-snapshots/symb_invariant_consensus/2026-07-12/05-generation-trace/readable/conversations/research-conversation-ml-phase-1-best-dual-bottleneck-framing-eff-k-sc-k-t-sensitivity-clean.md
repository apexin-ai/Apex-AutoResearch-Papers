# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义： 含义：Dual Bottleneck framing 完全成立：Eff-K+SC 作为跨条件预测器有效，K/T sensitivity 曲线 clean，所有

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-1/ce350913-1529-4773-bc92-65a3a830432f.jsonl`
- **Structured JSON:** [`2a55617cae27dbe43a3d.json`](../../sessions/2a/2a55617cae27dbe43a3d.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-19T03:42:52.126Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-19T03:42:52.126Z",
  "sessionId": "ce350913-1529-4773-bc92-65a3a830432f",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：\n\n含义：Dual Bottleneck framing 完全成立：Eff-K+SC 作为跨条件预测器有效，K/T sensitivity 曲线 clean，所有 pending 实验结果与理论一致。Main conference 可争取。\n核心假设：['exp-051 Mistral K sensitivity 呈现 clean inverted-U，peak 在 K=10-14 区间，两侧单调递减', 'T sensitivity 呈现 clean peaked curve: T=0.3 ≤+1pp, T=0.5 ~+2pp, T=0.7 +4.9pp, T=1.0 +0.5pp', 'exp-055 multi-temp 确认 negative (≤+0.5pp n.s.) → diversity alone 不足以打破 bottleneck', 'Eff-K × SC 双因子在所有已完成条件上 rank-consistent: 仅 Goldilocks zone (Eff-K>1.5 AND 45%&lt;SC<60%) 出现正向 delta', 'seed 内 κ-delta 非单调可被 Unknown 比例 / trace decisiveness 完全解释']\n关键指标范围：{'mistral_k_peak_delta_pp': [4.0, 6.0], 'mistral_k_k4_delta_pp': [-2.0, 1.0], 'mistral_k_k20_delta_pp': [-1.0, 2.0], 'mistral_k_inverted_u_visual': 'peak 与两侧差值 ≥2pp，无 non-monotonic outlier', 't03_delta_pp': [-1.0, 1.0], 't05_delta_pp': [0.5, 3.0], 'multitemp_delta_pp': [-2.0, 0.5], 'effk_sc_joint_prediction_accuracy': '≥10/12 conditions 方向正确 (正 delta 仅在 Goldilocks zone)', 'estimated_reviewer_avg': [3.0, 3.5]}\n叙事方向：原始 Dual Bottleneck framing 完全保留。五条 claims 无需降级。 Hero figure: SC×Eff-K scatter 清晰划分四象限，Goldilocks zone 与 positive delta 完美重合。 K sensitivity inverted-U 作为独立 ablation contribution。 T sensitivity 的 narrow window 强化\"效应真实但脆弱\"叙事——脆弱性本身 IS the finding。 9 种修复失败 + oracle gap 构成完整的\"结构性限制\"论证。 投稿目标: EMNLP Main，Findings 作为安全网。预期 score 3.0-3.5。\n\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: symb_invariant_consensus\nfocus: D060 纯 Analysis paper — Dual Bottleneck (Independence + Quality) framing。重点审查：1) Condorcet Eff-K 作为跨模型预测器是否有说服力（seed 内部非单调问题）；2) 9 种修复失败作为 structural bottleneck 证据是否充分；3) K/T sensitivity ablation 的 inverted-U 是否足够 clean；4) Analysis paper 在 EMNLP 2026 的竞争力（≥3.0 Findings 可达性）\n\n## paper_framing.md\n\n# Paper Framing — symb_invariant_consensus\n\n## Target Venue\n- Primary: EMNLP 2026 Main (ARR May 25)\n- Deadline: May 25, 2026 (ARR submission)\n\n## D060 Direction: Pure Analysis Paper — Independence Bottleneck\n\n**D059 method improvement 三路失败后，回归纯 analysis paper。** 但比 D058 的 analysis 更强：\n- **Condorcet independence 框架** 提供理论解释（非纯经验）\n- **9 种修复全部失败**（比原 6 种多 3 种靶向尝试）→ bottleneck 是 fundamental\n- **exp-052 p=0.039** → 2/3 seeds 显著 → 效应 IS real but fragile\n- **K sensitivity 倒 U 型** → clean ablation 贡献\n- **T sensitivity** → +4.90pp 仅在 T=0.7 存在，T=1.0 降到 +0.55pp → 效应极度脆弱\n- 用户指示: 投 May 25 不变，≥3.0 兜底\n\n## Core Claims (5 条) — D060 纯 Analysis Framing\n\n### Analysis Claims (已验证)\n\n1. **Independence Bottleneck**: Self-consistency 隐含 Condorcet Jury Theorem 的独立性假设，但同模型采样的 traces 高度相关。Worker 验证的 κ 值：\n   - Qwen-14B FOLIO: κ=0.744, Eff-K=1.31 (SC=75.49%, Δ=+0.25pp n.s.)\n   - Qwen-14B LogiQA: κ=0.821, Eff-K=1.20 (SC=78.5%, Δ=+0.50pp n.s.)\n   - Mistral-7B FOLIO s42 (exp-033): κ=0.500, Eff-K=1.85 (Δ=+4.90pp p=0.013) ← primary seed\n   - Mistral-7B FOLIO s123: κ=0.412, Eff-K=2.17 (Δ=+3.43pp p=0.039)\n   - Mistral-7B FOLIO s456: κ=0.401, Eff-K=2.22 (Δ=-0.49pp n.s.)\n   - Mistral-7B PW-600 (exp-046): κ=0.210, Eff-K=3.63 (Δ=-2.83pp p=0.010, SC=39%)\n   规律：跨模型对比清晰（Qwen Eff-K≈1.2-1.3 → 0 gain; Mistral Eff-K≈1.85-2.22 → variable gain）。但 Mistral seeds 内部，Eff-K 与 delta 非单调（exp-033 Eff-K 最低 1.85 却 delta 最高 +4.90pp）→ Eff-K 是跨模型必要条件，seed 内 variance 仍主导。exp-046 Eff-K 最高(3.63) 但 SC 太低(39%) 导致 delta 为负 → 需同时满足 sufficient Eff-K AND sufficient SC。\n\n2. **Oracle Gap Localizes Extraction Bottleneck**: Gold FOL + MAX-SAT = +14.22pp (p=2.0e-7)，自提取仅 +4.9pp (best case) = 35% utilization。聚合机制本身有效，瓶颈在自提取质量。Two-layer analysis:\n   - **Constraint taxonomy**: 43% trivially_satisfied（被所有候选答案满足的约束，不排除任何答案）\n   - **Discriminative filtering**: 仅 ~8% 约束在 MAX-SAT scoring 中完全 non-discriminative（移除后 0 gains）\n   - **关键区分**: 43% 和 8% 度量不同。trivially_satisfied 约束在 MAX-SAT 中仍可有不同满足程度（partial vs full），所以不全是 non-discriminative。但即使 constraints 是 discriminative 的，它们的\"区分方向\"与模型自身偏差一致（confirmation bias）。both_wrong 组 score_range=29.4。九种修复全部失败。\n\n3. **Regime-Dependent Capability Trap**: SICA 有效性取决于提取模型的基线准确率，存在双边界：\n   - Type A (SC ≥ ~60%): 确认偏差，constraints 镜像模型自身答案\n   - Type C (SC ≤ ~40%): traces 主要错误，constraints 是噪声 (exp-046: Δ=-2.83pp, p=0.0095)\n   - Goldilocks zone (~50-55% SC): 部分独立性 + 部分正确性 (exp-033: Δ=+4.90pp, p=0.013)\n   - Type B: 领域不可形式化 (LogiQA: contradiction rate 0.8%)\n\n4. **C0+SC Two-Dimensional Diagnostic**: C0 (multi-candidate rate) + SC accuracy 形成零成本部署诊断。C0<5% → degenerate; high C0 + high SC → trap; high C0 + low SC → potential gains。\n\n### Remediation Evidence (D060: 全部失败 — 强化 analysis narrative)\n\n5. **Nine Remediation Attempts All Failed**: 原 6 种 + 3 种靶向修复全部无效，证明 independence bottleneck 是结构性的：\n   - D059 三路 method improvement 全部失败：\n     - Discriminative Filtering: 119/204 处理后 0 gains 1 loss，~92% 约束本身就是 discriminative，过滤是 near-no-op\n     - T=1.0 (exp-054): delta 从 +4.90pp 崩塌到 +0.55pp，温度敏感性极端\n     - Multi-Temp (exp-055): 早期 n=28 delta=0.00pp（待完成，但预期 negative）\n   - 原 6 种：contrastive prompting, cross-model extraction, generational scaling, solver-guided refinement, consistency filtering, cross-trace UNSAT\n   - 9 种修复涵盖 prompting / architecture / capability / verification / diversity / filtering 全维度，全部失败 → trap is fundamental\n\n## Core Insight (D060 Updated — Dual Bottleneck)\n\n**Dual Requirement Framework**: SICA 效应需要同时满足两个条件，缺一不可：\n1. **Sufficient Independence** (Eff-K > threshold): traces 需要提供足够多的独立视角\n2. **Sufficient Quality** (SC > ~50%): traces 需要有足够的正确率，否则约束是噪声\n\nCondorcet Jury Theorem 要求投票者独立且 p>0.5。同模型采样的 reasoning traces 严重违反独立性假设（Fleiss' κ = 0.21–0.82，Eff-K 仅 1.20–3.63），解释了为什么简单增加 K 或添加符号约束不能突破 SC 的天花板。\n\n实验数据完美支持 dual requirement：\n- **Qwen-14B**: Eff-K≈1.2-1.3（独立性不足）→ 0 gain，无论 SC 多高\n- **Mistral-7B FOLIO**: Eff-K≈1.85-2.22（中等独立性）+ SC≈54%（中等质量）→ +4.90pp (2/3 seeds significant)\n- **Mistral-7B PW-600**: Eff-K=3.63（最高独立性）但 SC=39%（质量不足）→ -2.83pp\n- 只有 Goldilocks zone（中等 Eff-K + 中等 SC）出现正向 delta\n\nOracle control (+14.22pp) 证明 MAX-SAT 聚合机制本身有效，但自提取约束仅利用了 35% 的理论上限。Discriminative filtering 实验揭示关键机制：~92% 约束 ARE discriminative，但过滤掉 ~8% non-discriminative 约束后 delta 不变（0 gains）。问题不在约束缺乏判别力，而在于 discriminative constraints 的区分方向与模型偏差一致（confirmation bias）。\n\n**κ-delta 反相关解释**：exp-033 κ=0.500 比 exp-052/053 κ≈0.41 高，但 delta 最大。原因：exp-033 Unknown 比例低（49.9% vs 58.5%），traces 更 decisive（更多 True/False 判断）→ 同时导致更高 κ（更多 agreement）和更好的 constraint quality。κ 不是 SICA 效果的唯一决定因素。\n\n**Remediation insight (D060)**: 9 种修复尝试全部失败，包括直接靶向 independence（multi-temp diversity）和 constraint quality（discriminative filtering）。这证明 bottleneck 不是简单的 diversity 或 quality 问题，而是 same-model self-extraction 的根本性限制。\n\n**Key evidence**:\n- **Condorcet independence quantification (Worker-verified, 公式: Eff-K=K/(1+(K-1)κ))**: exp-033 Mistral-7B s42 κ=0.500 (Eff-K=1.85), Mistral-7B s123 κ=0.412 (Eff-K=2.17), Mistral-7B s456 κ=0.401 (Eff-K=2.22), Mistral-7B PW-600 κ=0.210 (Eff-K=3.63), Qwen-14B FOLIO κ=0.744 (Eff-K=1.31), Qwen-14B LogiQA κ=0.821 (Eff-K=1.20). 跨模型清晰: Qwen Eff-K≈1.2-1.3→0 gain, Mistral Eff-K≈1.85-3.63→variable. Eff-K necessary but not sufficient: exp-046 highest Eff-K(3.63) but negative delta(SC too low); within Mistral seeds Eff-K非单调 with delta.\n- **Oracle control (exp-031)**: Gold FOL + MAX-SAT = 89.71% vs SC 75.49% (+14.22pp, p=2.0e-7). Unknown-type +31.9pp.\n- **Two-layer constraint analysis**: 43% trivially_satisfied (taxonomy: satisfied by ALL answers) vs ~8% non-discriminative (filtering: same MAX-SAT score). Difference: trivially_satisfied constraints can still have different satisfaction DEGREES. Removing the 8% yields 0 gains → problem is not quality but confirmation bias direction.\n- **K sensitivity (inverted U)**: K=4(-1.47pp), K=8(-0.98pp), K=12(+4.90pp p=0.013), K=16(+1.47pp), K=20(pending). Peak at K=12, then decline. Non-monotonic. K=4 SC ≈ K=12 SC but SICA differs by 6.4pp — proves SICA extracts different information than SC.\n- **T sensitivity (extreme fragility)**: T=0.7(+4.90pp p=0.013), T=1.0(+0.49pp p=0.739). 温度从 0.7 提到 1.0 让增益降 90%。T=0.3 (exp-057, pending). SICA 效应极度依赖超参数。\n- **Regime boundary**: Qwen-14B (SC=75.49%) Δ=+0.25pp vs Mistral-7B (SC=54.41%) Δ=+4.90pp p=0.013\n- **Type C failure (exp-046)**: Mistral PW-D5 SC=39.33%, Δ=-2.83pp, p=0.010, κ=0.210, Eff-K=3.63, contradiction rate 5.5%. Highest Eff-K yet worst delta → independence alone insufficient when SC too low.\n- **Seed replication**: 2/3 seeds significant at α=0.05 (exp-033 p=0.013, exp-052 p=0.039), 1/3 null (exp-053). Effect IS real but fragile — motivates deep analysis of WHY.\n- **Nine remediation failures**: contrastive prompting, cross-model, generational scaling, solver-guided, consistency filtering, cross-trace UNSAT, discriminative filtering (0 gains), T=1.0 (delta collapse), multi-temp (pending, early 0.00pp). All failed → trap is fundamental.\n- **Entropy mechanism**: High-entropy problems proportion: Mistral 35.8% vs Qwen 10.3%. Unanimous rate: 18.6% vs 58.8%.\n- **Confirmation bias quantification**: Override precision 70.6% (Mistral) vs 28.6% (Qwen). Constraint agreement >80%: 31.9% vs 62.3%.\n\n## Story Spine (D059 Updated)\n\n- **Problem**: LLMs' reasoning can be improved by sampling multiple chains-of-thought and aggregating via majority voting (self-consistency). Recent work proposes symbolic augmentation: extract formal constraints from traces and use SAT solvers for answer selection. But does symbolic aggregation actually outperform simple voting?\n- **Theoretical lens**: Condorcet Jury Theorem requires voter independence. We quantify trace independence via Fleiss' κ and show Effective-K << nominal K. This explains the fundamental limitation of same-model trace aggregation.\n- **Systematic evaluation**: SICA (MAX-SAT over FOL constraints) across 3 domains × 5 model families. Oracle control separates extraction vs aggregation failure. Discriminative filtering reveals ~92% constraints are discriminative, yet SICA gains are fragile — confirmation bias, not constraint quality, is the bottleneck.\n- **Regime characterization**: Three failure modes (Type A/B/C) + narrow Goldilocks zone. C0+SC as deployment diagnostic.\n- **Remediation failures strengthen thesis**: 9 targeted interventions (prompting, architecture, capability, verification, diversity, filtering) all fail to close the oracle gap, proving the bottleneck is fundamental to same-model self-extraction.\n- **Headline result**: \"Across 5 model families, symbolic consensus aggregation shows a real but fragile effect: significant improvement in 2/3 seeds under specific conditions (Mistral-7B, FOLIO, T=0.7, K=12), but zero or negative gains under any perturbation. Condorcet analysis reveals the root cause: Effective-K = 1.3-1.8 for nominal K=12 due to trace non-independence. Oracle constraints prove the aggregation mechanism works (+14.22pp), but 9 remediation strategies all fail to overcome the self-extraction bottleneck. C0+SC provides a zero-cost deployment diagnostic.\"\n\n## Anticipated Reviewer Concerns & Defensive Experiments\n\n1. **\"Gains not statistically significant\"** → exp-033 p=0.013 (n=204), exp-031 oracle p=2.0e-7. Combined N>1,200.\n2. **\"Only one positive result (exp-033)\"** → Seed replication: 2/3 significant (p=0.013, p=0.039). Effect IS real but fragile — the fragility itself IS the finding (K/T sensitivity, Condorcet independence).\n3. **\"Condorcet framework is trivial\"** → Fleiss' κ quantification is novel in SC/SICA context. Eff-K is actionable: tells practitioners how many truly independent traces they get.\n4. **\"Multi-temp / filtering should work\"** → We tried both. Multi-temp (exp-055): negative. Disc. filtering: 0 gains. T=1.0: delta collapse. These failures STRENGTHEN the structural bottleneck thesis.\n5. **\"Only Qwen models\"** → 5 families: Qwen-14B, Mistral-7B, LLaMA-8B, DeepSeek-R1-7B, QwQ-32B.\n6. **\"Only logic domain\"** → FOLIO + ProofWriter + LogiQA + StrategyQA + ARC-Challenge. Type B (domain formalizability) is itself a finding.\n7. **\"Oracle is unfair comparison\"** → Diagnostic tool, not competing method. Separates extraction from aggregation.\n8. **\"MAX-SAT is over-engineering\"** → exp-013: MaxSAT ≈ count-only. This IS the independence bottleneck evidence.\n9. **\"Self-extraction confound\"** → Oracle control resolves completely.\n10. **\"Published methods achieve gains (DyLoS, Aristotle, FoVer)\"** → Different paradigm (external verifiers/trained extractors). We characterize same-model self-extraction.\n11. **\"C0 is trivially derived\"** → Zero-cost early stopping. Practical value.\n12. **\"Why not just use a reasoning model?\"** → QwQ-32B: C0<5%, SICA≡SC.\n13. **\"Random tiebreak baseline\"** → exp-003: SICA tiebreak 80% vs random 50%.\n14. **\"Method improvement is incremental\"** → Grounded in diagnosis (independence + taxonomy), not ad-hoc.\n15. **\"Weighted SC is simpler\"** → exp-016 planned. Weighted SC doesn't address independence.\n16. **\"Within-model ICL transition contradicts regime theory\"** → exp-050b (SC=57.79%, Δ=-3.52pp): ICL changes trace generation characteristics, not just SC level. Paper must distinguish \"same model, different prompt\" from \"same model, same prompt, different accuracy.\"\n\n## Working Title\n**\"Beyond Self-Consistency: How Trace Independence Limits Symbolic Consensus in LLM Reasoning\"**\n(Alternatives:\n- \"The Independence Bottleneck: Why Self-Extracted Symbolic Constraints Cannot Beat Majority Voting\"\n- \"Symbolic Consensus Under the Condorcet Lens: Independence, Extraction, and the Limits of Self-Aggregation\")\n\nNOTE (Dream D037): Title MUST be scoped to \"self-extracted constraints\" / \"SICA\". Published methods (DyLoS, Aristotle, FoVer) use different approaches.\n\n## Paper Structure (EMNLP 8pp + appendix)\n\n### Main Tables\n- T1: Main Results — models × domains, SC% / SICA% / Δpp / p-value, regime boundary\n- T2: Oracle Control — Gold-FOL+MAX-SAT vs SC vs SICA-self, causal separation\n- T3: Independence Quantification — Fleiss' κ / Eff-K / trace agreement per model\n- T4: Extraction Error Taxonomy — trivially_satisfied / discriminative / both_wrong rates\n- T5: K Sensitivity — K=4/8/12/16/20 with Eff-K and diversity metrics (inverted U curve)\n\n### Main Figures\n- F1: Method Pipeline (SICA + oracle control design)\n- F2: SC Accuracy vs SICA Δ scatter (hero figure, regime boundary)\n- F3: K Sensitivity with diversity metrics (K vs Δ, K vs Eff-K)\n- F4: Extraction error breakdown (stacked bar)\n\n### Appendix\n- K ablation details, temperature sensitivity, per-domain results, overhead analysis\n- Entropy-conditioned analysis (continuous scatter + bin sensitivity)\n- Six remediation strategy details\n- Confirmation bias quantification\n- Seed replication analysis\n- QwQ-32B / DeepSeek-R1 negative control\n\n## Claim Risk Notes (D059)\n- **Seed replication**: 2/3 significant (p=0.013, p=0.039), 1/3 null. Frame as \"real but fragile effect\" — motivates analysis of WHY.\n- **Method claims DEAD (D060)**: All three method improvements failed. Paper is pure analysis. 9 remediation failures are EVIDENCE, not limitation.\n- **Condorcet novelty**: ✅ VERIFIED. arXiv:2409.00094 applies CJT to cross-model LLM ensembles (different angle). No prior work applies Fleiss' κ or Eff-K to within-model SC traces. Our framing is novel.\n- **exp-050b complication**: ICL transition Δ=-3.52pp at SC=57.79% complicates simple \"SC determines SICA.\" Explain via trace generation characteristic change.\n- **Variable naming inconsistency**: 56.4% cross-trace pairs share zero Z3 variables. Key mechanism evidence.\n\n## Required Citations (minimum 30 references)\n\n- **SC & extensions**: Wang et al. 2023 (SC), Chen et al. 2023 (USC), Loo et al. 2025 (SC scaling plateaus), Taubenfeld et al. 2025 (weighted SC), DiVeRSe (Li et al. 2023)\n- **Neuro-symbolic reasoning**: DyLoS (EACL 2026), Aristotle (ACL 2025), FoVer (TACL 2025), LogicAgent (2025), Logic-LM (Pan et al. 2023), LINC (Olausson et al. 2023)\n- **Condorcet/voting theory**: Condorcet 1785, Austen-Smith & Banks 1996, **arXiv:2409.00094 (Examining Independence in Ensemble Sentiment Analysis, Sept 2024)** — closest prior work, applies CJT to cross-model LLM ensembles, finds independence violation. Our novelty: within-model trace independence + Fleiss' κ quantification + Eff-K + connection to symbolic aggregation\n- **Test-time compute**: Snell et al. 2025, DeepSeek-R1, Diversity-Aware Training\n- **Verification & reranking**: ORM (Cobbe et al. 2021), PRM (Lightman et al. 2023), Math-Shepherd\n- **Constraint satisfaction**: SATBench (EMNLP 2025), LLM Meets Constraint Propagation (IJCAI 2025)\n- **Debate & multi-agent**: Liang et al. 2023, Du et al. 2023\n\n## Claim Scoping Rules\n- n=60 conditions: \"suggestive/consistent with\" NOT \"confirming\"\n- n≥200 conditions: can \"confirm\"\n- Combined N>1,300: acceptable if breakdown clearly stated\n- Method claims: must show statistically significant improvement OR clear directional improvement with analysis\n- \"Independence bottleneck\" framing: systematic quantification + theoretical grounding\n\n\n## experiment_plan (with registry status)\n\n- id: exp-001\n  name: sica_expanded_14b\n  claim:\n  - 1\n  - 2\n  description: 'Full-scale evaluation: PW D5 600 + FOLIO 204 = 804 questions, K=12,\n    T=0.7. Maximizes statistical power for C3 significance.'\n  priority: P0\n  gpu_budget_hours: 14\n  deps: []\n  registry_id: sica_expanded_14b\n  status: DONE\n  conclusion: success\n  metrics:\n    sica_accuracy: 0.765\n    sc_accuracy: 0.762\n    sica_sc_gap_pp: 0.3\n    n_problems: 804\n    multi_candidate_rate: 0.3818\n    folio_sica: 0.794\n    folio_sc: 0.794\n    folio_gap_pp: 0\n    folio_n: 204\n    proofwriter_sica: 0.755\n    proofwriter_sc: 0.752\n    proofwriter_gap_pp: 0.3\n    proofwriter_n: 600\n    extraction_rate: 0.89\n    answer_extraction_rate: 1\n    contradiction_rate: 0.022\n    problems_with_contradictions: 331\n    truncated_traces: 0\n    wall_time_min: 826\n- id: exp-002\n  name: sica_k_ablation_14b\n  claim:\n  - 1\n  description: 'K sensitivity (K=6,8,11,12,16,20) on D012''s 60 questions. Includes\n    odd K=11 to test if SICA value persists without exact ties. Key questions: does\n    SICA benefit depend on tiebreaks? What happens at odd K? How does tiebreak frequency\n    change with K?'\n  priority: P0\n  gpu_budget_hours: 6\n  deps: []\n  status: planned\n  note: D024 增加 K=11（odd-K test, Dream 三档一致要求）。如 K=11 gap=0 → 确认 tie-only mechanism；如\n    gap>0 → SICA has value beyond tiebreaking。\n- id: exp-003\n  name: tiebreak_baseline_analysis\n  claim:\n  - 1\n  description: Compare SICA vs SC-random-tiebreak vs SC-deterministic on all available\n    data. CPU-only reanalysis. Quantify how much of SICA's gain survives against fair\n    baselines.\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - sica_d012_14b\n  status: planned\n  note: 'Completed as CPU analysis, no registry entry. Results: SICA tiebreak 80%\n    (4/5) vs random 50% vs alphabetical 60% vs first-seen 40%. Artifact: art_20260516_47de9d'\n- id: exp-004\n  name: sica_7b_scaling\n  claim:\n  - 2\n  - 3\n  description: 'Run SICA with Qwen2.5-7B-Instruct on same 60 questions. Test: does\n    weaker model → higher C0 → larger SICA gain? Validates C0-as-predictor claim.'\n  priority: P1\n  gpu_budget_hours: 2\n  deps:\n  - exp-001\n  status: planned\n- id: exp-005\n  name: qwq_32b_operating_regime\n  claim:\n  - 2\n  description: QwQ-32B negative results formatted for paper's Operating Regime Analysis\n    section. Data exists from MVP phase (AIME, MATH, ProofWriter, FOLIO). No new GPU\n    needed.\n  priority: P1\n  gpu_budget_hours: 0\n  deps: []\n  status: planned\n  note: 'Data from QwQ-32B MVP experiments: sica_aime30_v3 (AIME 22题, 0% multi-candidate),\n    sica_proofwriter30_v2 (PW 16题, 18.75% multi-candidate), sica_folio30 (FOLIO 10题,\n    0% multi-candidate). Combined C0=3.6%, SICA≡SC across all domains.'\n- id: exp-006\n  name: c0_diagnostic_validation\n  claim:\n  - 3\n  description: Plot C0 vs SICA-SC gap across all models and K values. Validate C0\n    as predictor. CPU-only analysis over exp-001/002/004/005 results.\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - exp-001\n  - exp-002\n  - exp-004\n  status: planned\n- id: exp-007\n  name: sica_72b_awq\n  claim:\n  - 2\n  description: 'Qwen2.5-72B-Instruct AWQ 4-bit on 60 questions. Scaling analysis:\n    high-baseline non-reasoning model. Within-Qwen scaling dimension.'\n  priority: P1\n  gpu_budget_hours: 4\n  deps:\n  - exp-001\n  status: planned\n  note: D019 升级 P2→P1. 72B-AWQ 4-bit ~36GB weights + KV cache ≈ 50-60GB, 98GB RTX\n    PRO 6000 单卡可放。\n- id: exp-008\n  name: constraint_quality_case_studies\n  claim:\n  - 1\n  description: Qualitative analysis of extracted constraints on 5-10 representative\n    questions. Are constraints semantically meaningful? Do excluded constraints correspond\n    to reasoning errors?\n  priority: P2\n  gpu_budget_hours: 0\n  deps:\n  - exp-001\n  status: planned\n- id: exp-009\n  name: overhead_analysis\n  claim:\n  - 1\n  description: 'Wall-time breakdown per question: generation, constraint extraction,\n    MaxSAT solving. Address ''is the overhead worth it'' concern.'\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - exp-001\n  status: planned\n  note: D021 升级 P2→P1. Reviewer 指出 EMNLP 审稿人对 practical impact 极敏感。\n- id: exp-010\n  name: sica_mistral_7b\n  claim:\n  - 2\n  - 3\n  description: 'Mistral-7B-Instruct-v0.3 on D012 60 questions (PW+FOLIO). Cross-family\n    validation: does C0 pattern hold outside Qwen? Eliminates ''Qwen-specific artifact''\n    attack.'\n  priority: P0\n  gpu_budget_hours: 1.5\n  deps: []\n  status: DONE\n  note: 'D021 新增. 必做——消除 Claim 2 致命弱点。Escalation: 若 C0>30% 且 gap>0 但 p>0.2，扩展到 200+\n    题（~3h GPU，margin 允许）。'\n  registry_id: exp-010-mistral-v3\n  conclusion: negative\n  metrics:\n    n: 60\n    k: 12\n    sica_accuracy: 0.4833\n    sc_accuracy: 0.4833\n    delta_pp: 0\n    multi_candidate_rate: 0.5\n    extraction_rate: 0.8819\n    answer_extraction_rate: 1\n    contradiction_rate: 0.0562\n    discordant_sica_wins: 2\n    discordant_sc_wins: 2\n    mcnemar_p: 1\n    proofwriter_sica: 0.4\n    proofwriter_sc: 0.4\n    proofwriter_delta_pp: 0\n    folio_sica: 0.5667\n    folio_sc: 0.5667\n    folio_delta_pp: 0\n    truncated_traces: 0\n    model: Mistral-7B-Instruct-v0.3\n    dataset: D012\n- id: exp-011\n  name: sica_llama_8b\n  claim:\n  - 2\n  - 3\n  description: LLaMA-3.1-8B-Instruct on D012 60 questions. Second non-Qwen family.\n    Combined with exp-010 gives 3-family coverage (Qwen/Mistral/LLaMA).\n  priority: P0\n  gpu_budget_hours: 1.5\n  deps: []\n  status: planned\n  note: D021 新增. 必做——3 家族是 EMNLP 最低门槛。需 HF_TOKEN（Meta license）或 ModelScope 镜像。Escalation\n    同 exp-010。\n- id: exp-012\n  name: gsm8k_pilot_14b\n  claim:\n  - 2\n  - 3\n  description: 'Qwen2.5-14B on GSM8K 30-question pilot (K=12). Cross-domain test:\n    is C0 high only in restricted-answer-space domains (NLI 3-class) or also in open-answer\n    math? If C0 low → C0=uncertainty signal (strengthens Claim 3). If C0 high → cross-domain\n    win.'\n  priority: P1\n  gpu_budget_hours: 1\n  deps: []\n  status: planned\n  note: D021 新增. Reviewer 预测 C0<20% (14B too strong on GSM8K). Any result is publishable\n    insight.\n- id: exp-013\n  name: constraint_ablation\n  claim:\n  - 1\n  - 2\n  description: 'CPU-only ablation: SICA-MaxSAT vs SICA-count-only (constraint count\n    per answer, no satisfiability) vs SICA-random-weight. Critical for D025 pivot:\n    if MaxSAT ≈ count-only → aggregation mechanism is vacuous, confirming capability\n    trap.'\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - exp-001\n  status: planned\n  note: 'D025 升级 P1→P0. 现在是 make-or-break: 如果 MaxSAT = count-only → 证明 SAT 解算无贡献（capability\n    trap 的 mechanism evidence）。必须用 exp-002 的 raw_constraints 数据。'\n- id: exp-014\n  name: sica_deepseek_r1_llama_8b\n  claim:\n  - 2\n  description: 'DeepSeek-R1-Distill-LLaMA-8B on D012 60 questions. Second reasoning\n    model data point with LLaMA base architecture: validates C0<5% generalizes beyond\n    QwQ-32B AND eliminates ''still Qwen family'' attack.'\n  priority: P1\n  gpu_budget_hours: 2\n  deps: []\n  status: planned\n  note: D021 新增. Reviewer 建议用 LLaMA 底座版本避免 Qwen 架构归属争议。\n- id: exp-015\n  name: logic_lm_baseline\n  claim:\n  - 1\n  description: Logic-LM × K + majority vote baseline on FOLIO. Run Logic-LM style\n    single-trace FOL verification K times, then majority vote. Isolates whether MAX-SAT\n    multi-trace aggregation adds value beyond FOL extraction itself.\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - exp-001\n  status: planned\n  note: 'D024 新增. Dream 三档一致要求 Logic-LM/LINC 比较。CPU-only: 用 exp-001 已有 traces + FOL\n    constraints 做单 trace verification then vote。'\n- id: exp-016\n  name: weighted_sc_baseline\n  claim:\n  - 1\n  - 3\n  description: 'Weighted SC baseline (Taubenfeld et al. 2024 style): weight votes\n    by trace confidence/length/perplexity. CPU-only reanalysis of exp-001/002 data.\n    Tests if simple weighting achieves same tiebreak quality without MAX-SAT.'\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - exp-001\n  status: planned\n  note: 'D024 新增. Dream 提出 weighted SC 是最直接竞争 baseline。实现方式: (1) uniform weight (=SC),\n    (2) length-weighted, (3) log-prob weighted (如 traces 有 logprobs), (4) constraint-count\n    weighted (no SAT)。'\n- id: exp-017\n  name: sica_strategyqa_14b\n  claim:\n  - 1\n  - 2\n  description: Qwen2.5-14B on StrategyQA 60 questions (K=12). Commonsense reasoning\n    domain — high predicted C0 (35-50%) but implicit reasoning chains → low expected\n    constraint quality. Tests capability trap in best-case-diversity scenario.\n  priority: P0\n  gpu_budget_hours: 1.5\n  deps: []\n  status: planned\n  note: D025 新增. Reviewer 推荐 ROI 最高 benchmark。如 C0>30% 且 SICA≈SC → 直接证明 capability\n    trap（diversity high but quality low → no gain）。\n- id: exp-018\n  name: sica_arc_challenge_14b\n  claim:\n  - 1\n  - 2\n  description: Qwen2.5-14B on ARC-Challenge 60 questions (K=12). Science reasoning,\n    4-choice format. Tests constraint mechanism in multi-choice scenario + different\n    domain.\n  priority: P0\n  gpu_budget_hours: 1.5\n  deps: []\n  status: planned\n  note: D025 新增. 4选1格式测试 constraint mechanism 泛化能力。与 FOLIO (3-class) + GSM8K (open)\n    + StrategyQA (binary) 形成答案格式多样性。\n- id: exp-019\n  name: constraint_quality_correlation\n  claim:\n  - 1\n  - 2\n  description: 'CPU-only analysis: compute constraint precision per domain × model,\n    correlate with C0 and SICA-SC gap. Formalizes the capability trap as inverse C0-quality\n    correlation. Uses data from exp-001/010/011/017/018.'\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - exp-001\n  - exp-017\n  - exp-018\n  status: planned\n  note: 'D025 新增. Hero figure (F2) 的数据来源。Constraint quality = (constraints consistent\n    with ground truth) / (total constraints). 预期: high C0 domains (StrategyQA) have\n    low quality, low C0 domains (math) have high quality but SICA=SC anyway.'\n\n\n## registry (completed experiments)\n\n- exp_id: crd_folio_main\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    divergence_rate: 0.422\n    diagnosis_rate: 0.872\n    error_types: 4\n    directed_advantage_pp: 4.7\n    directed_p_value: 0.63\n    localization_accuracy: 0.946\n    fol_accuracy: 0.789\n    code_accuracy: 0.598\n    oracle_accuracy: 0.878\n    pipeline_accuracy: 0.814\n    baseline_accuracy: 0.74\n    cost_multiplier: 5.76\n    dataset: FOLIO\n    n: 204\n- exp_id: smoke-test-5q\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: sica_smoke_5q\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    sica_accuracy: 0.8\n    sc_accuracy: 0.8\n    extraction_rate: 1\n    problems_with_contradictions: 1\n    total_problems: 5\n    total_time_s: 3505\n    avg_time_per_problem_s: 701\n    per_problem:\n    - id: algebra/2470\n      level: 1\n      sica_correct: true\n      sc_correct: true\n      constraints: 27\n      unique: 9\n      excluded: 0\n    - id: prealgebra/65\n      level: 2\n      sica_correct: true\n      sc_correct: true\n      constraints: 26\n      unique: 2\n      excluded: 0\n    - id: number_theory/847\n      level: 3\n      sica_correct: true\n      sc_correct: true\n      constraints: 21\n      unique: 11\n      excluded: 0\n      note: 14 JSON parse failures, 1693s\n    - id: precalculus/1199\n      level: 4\n      sica_correct: false\n      sc_correct: false\n      constraints: 35\n      unique: 6\n      excluded: 0\n      note: graph-reading problem, model cannot see image\n    - id: algebra/2277\n      level: 5\n      sica_correct: true\n      sc_correct: true\n      constraints: 60\n      unique: 6\n      satisfied: 3\n      excluded: 3\n- exp_id: sica_temp_diversity\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    temperatures_tested:\n    - 0.7\n    - 0.9\n    - 1\n    problems_tested: 3\n    problems_with_divergence: 0\n    finding: QwQ-32B produces zero answer divergence at all temperatures on MATH L4-5.\n      Reasoning model's deterministic chain dominates sampling randomness.\n    max_tokens_issue: 4096 tokens insufficient for some L5 problems (truncation)\n    recommendation: Use AIME 2024 (harder, ~79.5% acc) or non-reasoning model for\n      trace diversity\n- exp_id: mvp_math50_t07\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: sica_aime30_t07\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: sica_aime30_v2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    progress: 4/30\n    sica_accuracy_interim: 3/4 (75%)\n    sc_accuracy_interim: 3/4 (75%)\n    avg_time_per_problem_s: 557\n    p2_z3_error: Z3Exception on z3_maxsat.py:163, 0 constraints extracted\n    p5_vllm_stuck: vLLM timeout since ~22:11, retried multiple rounds\n    issue: vLLM service likely crashed or OOM at Problem 5\n    analysis_contradiction_rate_aime: 50% (2/4)\n    analysis_contradiction_rate_math: 20% (1/5)\n    analysis_unique_constraints_per_problem_aime: 18.7\n    analysis_exclusion_rate: 10.7%\n    analysis_sica_sc_agreement: 9/9 (100%)\n    analysis_signal: weak positive - mechanism works but SC too unanimous to flip\n    analysis_p2_failure: 0 constraints, 0 votes - answer extraction failure\n- exp_id: sica_aime30_v3\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    progress: 22/30\n    sica_accuracy_interim: 16/22 (72.7%)\n    sc_accuracy_interim: 16/22 (72.7%)\n    sica_sc_gap_pp: 0\n    avg_time_per_problem_s: 645.9\n    runtime_h: 5.9\n    remaining_problems: 8\n    vote_diversity_analysis:\n      valid_problems: 16\n      total_problems: 22\n      multi_candidate_rate: 0\n      zero_vote_problems: 6\n      zero_vote_indices:\n      - 1\n      - 7\n      - 8\n      - 10\n      - 13\n      - 14\n      constraints_extracted: 19/22\n      exclusion_rate: 0.387\n      conclusion: All 16 valid problems have exactly 1 candidate answer. SICA≡SC structurally.\n        MaxSAT exclusion operates but cannot change final selection with only 1 candidate.\n    process_status: gone (cron miss 1/5)\n- exp_id: sica_proofwriter30\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    sica_accuracy: 0/30 (0.0%)\n    sc_accuracy: 0/30 (0.0%)\n    sica_sc_gap_pp: 0\n    total_wall_time_s: 238.9\n    total_wall_time_min: 4\n    avg_time_per_problem_s: 8\n    traces_generated: 0\n    constraints_extracted: 0\n    traces_with_constraints: 0\n    unique_constraints: 0\n    maxsat_satisfied: 0\n    maxsat_excluded: 0\n    multi_candidate_rate: N/A (no traces generated)\n    vote_diversity: N/A\n    z3_errors: 0\n    z3_timeouts: 0\n    problems_with_contradiction: 0\n    problems_with_votes: 0\n    failure_mode: ALL_400_BAD_REQUEST\n    failure_count: 30/30\n    root_cause: max_tokens=16384 equals max_model_len=16384, leaving 0 tokens for\n      prompt input. Every API call returns 400.\n- exp_id: sica_folio30\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: sica_proofwriter30_v2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: sica_d016_c0_precheck\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    multi_candidate_rate_combined: 0.46\n    multi_candidate_rate_folio: 0.4\n    multi_candidate_rate_proofwriter: 0.5\n    sc_accuracy_combined: 0.73\n    sc_accuracy_folio: 0.8\n    sc_accuracy_proofwriter: 0.69\n    n_problems: 26\n    n_folio: 10\n    n_proofwriter: 16\n    K: 6\n    T: 0.7\n    total_time_s: 280\n    c0_gate: PASS (46% >= 20%)\n    model: Qwen2.5-14B-Instruct\n    vllm_gpu_mem_gib: 27.6\n    smoke_test: 2 problems end-to-end OK, constraints 21-26 per problem\n- exp_id: sica_d012_14b\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    sica_accuracy: 0.7333\n    sc_accuracy: 0.7\n    sica_sc_gap_pp: 3.3\n    c0_multi_candidate_rate: 0.5333\n    c1_extraction_rate: 1\n    c2_contradiction_problems: 34\n    c3_gap_pp: 3.3\n    bootstrap_p: 0.2261\n    proofwriter_sica: 0.6667\n    proofwriter_sc: 0.6667\n    folio_sica: 0.8\n    folio_sc: 0.7333\n    total_constraints_raw: 5849\n    total_constraints_unique: 1735\n    maxsat_exclusion_rate: 0.0259\n    wall_time_min: 58.3\n    d012_verdict: ALL_PASS\n- exp_id: sica_expanded_14b\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    sica_accuracy: 0.765\n    sc_accuracy: 0.762\n    sica_sc_gap_pp: 0.3\n    n_problems: 804\n    multi_candidate_rate: 0.3818\n    folio_sica: 0.794\n    folio_sc: 0.794\n    folio_gap_pp: 0\n    folio_n: 204\n    proofwriter_sica: 0.755\n    proofwriter_sc: 0.752\n    proofwriter_gap_pp: 0.3\n    proofwriter_n: 600\n    extraction_rate: 0.89\n    answer_extraction_rate: 1\n    contradiction_rate: 0.022\n    problems_with_contradictions: 331\n    truncated_traces: 0\n    wall_time_min: 826\n- exp_id: sica_k_sensitivity_14b\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    K6_sica: 0.733\n    K6_sc: 0.733\n    K6_gap_pp: 0\n    K8_sica: 0.733\n    K8_sc: 0.75\n    K8_gap_pp: -1.7\n    K11_sica: 0.733\n    K11_sc: 0.733\n    K11_gap_pp: 0\n    K12_sica: 0.7\n    K12_sc: 0.75\n    K12_gap_pp: -5\n    K16_sica: 0.717\n    K16_sc: 0.75\n    K16_gap_pp: -3.3\n    K20_sica: 0.7\n    K20_sc: 0.733\n    K20_gap_pp: -3.3\n    all_K_sica_leq_sc: true\n    larger_K_degrades_sica: true\n- exp_id: sica_constraint_ablation_013\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    maxsat_accuracy: 0.7649\n    count_only_accuracy: 0.7662\n    random_weight_accuracy: 0.7587\n    sc_baseline_accuracy: 0.7624\n    n_problems: 804\n    maxsat_correct: 615\n    count_only_correct: 616\n    random_weight_correct: 610\n    sc_correct: 613\n    agreement_maxsat_vs_countonly: 803/804\n    agreement_maxsat_vs_randomwt: 785/804\n    agreement_maxsat_vs_sc: 773/804\n    agreement_countonly_vs_randomwt: 786/804\n    agreement_countonly_vs_sc: 774/804\n    agreement_randomwt_vs_sc: 764/804\n    mcnemar_p_all_gt_0.7: true\n- exp_id: exp-005\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    qwq_aggregate_c0_nominal_pct: 10.3\n    qwq_aggregate_c0_effective_pct: 2.6\n    qwen14b_c0_pct: 46\n    diversity_ratio_effective: 17.7\n    aime_delta_pp: 0\n    proofwriter_delta_pp: -5.9\n    aime_n: 22\n    proofwriter_n: 17\n    temp_diversity_n: 5\n    folio_n: 2\n    total_problems: 46\n    c0_threshold: 20\n    qwq_below_threshold: true\n- exp_id: exp-011-llama8b\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp-016-weighted-sc\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    sica_accuracy: 0.7649\n    sc_uniform_accuracy: 0.7624\n    inv_length_accuracy: 0.7674\n    length_weighted_accuracy: 0.7525\n    constraint_count_accuracy: 0.7525\n    inv_length_vs_sc_p: 0.453\n    length_vs_sc_p: 0.153\n    inv_length_vs_sica_p: 0.864\n    length_vs_sica_p: 0.066\n    n_problems: 804\n    all_nonsignificant: true\n- exp_id: exp-010-mistral\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp-011-llama8b-v2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp-017-strategyqa\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp-018-arc\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp-010-mistral-v2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp-017-strategyqa-v2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp-017-strategyqa-v3\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n: 60\n    k: 12\n    sica_accuracy: 0.5667\n    sc_accuracy: 0.5333\n    delta_pp: 3.33\n    mcnemar_chi2: 0.5\n    mcnemar_p: n.s.\n    bootstrap_ci_95:\n    - 0\n    - 8.33\n    bootstrap_p_delta_le_0: 0.1346\n    multi_candidate_rate: 0.1\n    contradiction_detected: 5\n    extraction_rate_problem: 1\n    extraction_rate_trace: 0.704\n    discordant_sica_wins: 2\n    discordant_sc_wins: 0\n- exp_id: pilot-constraint-filtering\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    n: 43\n    thresholds_tested:\n    - 1\n    - 2\n    - 3\n    - 5\n    - 7\n    best_gap_pp: 2.33\n    best_T: 1\n    sica_T1: 0.7674\n    sc: 0.7442\n    T5_gap: 0\n    T7_gap: 0\n    discriminative_ratio_count: 0.115\n    discriminative_ratio_weight: 0.372\n    effective_flip_rate: 0.174\n    multi_answer_problems: 23\n    unanimous_problems: 20\n    problems_disc_favors_different: 4\n- exp_id: exp-018-arc-v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n: 60\n    k: 12\n    sica_accuracy: 0.95\n    sc_accuracy: 0.9667\n    delta_pp: -1.67\n    multi_candidate_rate: 0.05\n    extraction_rate: 1\n    contradiction_detected: 3\n    discordant_sica_wins: 0\n    discordant_sc_wins: 1\n    dataset: ARC-Challenge\n    model: Qwen2.5-14B-Instruct\n- exp_id: exp-011-llama8b-v3\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n: 60\n    k: 12\n    sica_accuracy: 0.6667\n    sc_accuracy: 0.6\n    delta_pp: 6.67\n    multi_candidate_rate: 0.6167\n    extraction_rate: 0.8556\n    answer_extraction_rate: 0.8958\n    contradiction_rate: 0.0527\n    problems_with_contradictions: 43\n    truncated_traces: 44\n    discordant_sica_wins: 5\n    discordant_sc_wins: 1\n    mcnemar_p: 0.2188\n    proofwriter_sica: 0.6333\n    proofwriter_sc: 0.6\n    proofwriter_delta_pp: 3.33\n    folio_sica: 0.7\n    folio_sc: 0.6\n    folio_delta_pp: 10\n    model: LLaMA-3.1-8B-Instruct\n    dataset: D012\n    wall_time_min: 66.4\n- exp_id: pilot-contrastive-prompt\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp-010-mistral-v3\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    n: 60\n    k: 12\n    sica_accuracy: 0.4833\n    sc_accuracy: 0.4833\n    delta_pp: 0\n    multi_candidate_rate: 0.5\n    extraction_rate: 0.8819\n    answer_extraction_rate: 1\n    contradiction_rate: 0.0562\n    discordant_sica_wins: 2\n    discordant_sc_wins: 2\n    mcnemar_p: 1\n    proofwriter_sica: 0.4\n    proofwriter_sc: 0.4\n    proofwriter_delta_pp: 0\n    folio_sica: 0.5667\n    folio_sc: 0.5667\n    folio_delta_pp: 0\n    truncated_traces: 0\n    model: Mistral-7B-Instruct-v0.3\n    dataset: D012\n- exp_id: exp-019-llama8b-strategyqa-200\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    n: 200\n    k: 12\n    sica_accuracy: 0.74\n    sc_accuracy: 0.72\n    delta_pp: 2\n    multi_candidate_rate: 0.41\n    mcnemar_p: 0.424\n    bootstrap_ci_95:\n    - -1.5\n    - 5.5\n    bootstrap_p_delta_le_0: 0.12\n    discordant_sica_wins: 9\n    discordant_sc_wins: 5\n    discordant_total: 14\n    discordant_rate: 0.07\n    sc_unanimous_rate: 0.545\n    model: LLaMA-3.1-8B-Instruct\n    dataset: StrategyQA\n    wall_time_min: 52\n- exp_id: exp-020-llama8b-folio-204\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    n: 204\n    k: 12\n    sica_accuracy: 0.608\n    sc_accuracy: 0.632\n    delta_pp: -2.45\n    mcnemar_p: 0.2668\n    bootstrap_ci_95:\n    - -5.88\n    - 0.98\n    bootstrap_p_sica_ge_sc: 0.1\n    discordant_sica_wins: 4\n    discordant_sc_wins: 9\n    discordant_total: 13\n    discordant_rate: 0.064\n    multi_candidate_rate: 0.618\n    extraction_rate: 0.942\n    answer_extraction_rate: 0.951\n    contradiction_rate: 0.062\n    both_wrong: 71\n    model: LLaMA-3.1-8B-Instruct\n    dataset: FOLIO-204\n    wall_time_min: 131.7\n- exp_id: exp-009-overhead-analysis\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n: 804\n    mean_total_wall_s: 61.6\n    mean_trace_gen_s: 31.6\n    trace_gen_pct: 51.3\n    mean_extract_s: 29\n    extract_pct: 47\n    mean_dedup_s: 1\n    dedup_pct: 1.6\n    mean_maxsat_s: 0.003\n    maxsat_pct: 0.005\n    sica_overhead_s: 30\n    sica_overhead_pct: 48.7\n    pw_overhead_pct: 51.3\n    folio_overhead_pct: 38.6\n    p50_overhead_pct: 48.9\n    p90_overhead_pct: 57.6\n- exp_id: exp-014-deepseek-r1-7b\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    n: 60\n    k: 12\n    sica_accuracy: 0.6833\n    sc_accuracy: 0.7167\n    delta_pp: -3.33\n    multi_candidate_rate: 0.583\n    extraction_rate: 0.839\n    answer_extraction_rate: 0.939\n    truncated_traces: 72\n    contradiction_rate: 0.037\n    wall_time_min: 100.3\n    mcnemar_p: 0.4795\n    discordant_sica_wins: 0\n    discordant_sc_wins: 2\n    model: DeepSeek-R1-Distill-Qwen-7B\n    dataset: D012\n- exp_id: temperature-ablation-t03\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    n: 60\n    k: 12\n    sica_accuracy: 0.7333\n    sc_accuracy: 0.7333\n    delta_pp: 0\n    multi_candidate_rate: 0.3\n    discordant_total: 0\n    model: Qwen2.5-14B-Instruct\n    dataset: D012\n    temperature: 0.3\n- exp_id: temperature-ablation-t05\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    n: 60\n    k: 12\n    sica_accuracy: 0.7667\n    sc_accuracy: 0.7667\n    delta_pp: 0\n    multi_candidate_rate: 0.383\n    discordant_total: 0\n    model: Qwen2.5-14B-Instruct\n    dataset: D012\n    temperature: 0.5\n- exp_id: temperature-ablation-t10\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    n: 60\n    k: 12\n    sica_accuracy: 0.75\n    sc_accuracy: 0.75\n    delta_pp: 0\n    multi_candidate_rate: 0.433\n    discordant_total: 0\n    model: Qwen2.5-14B-Instruct\n    dataset: D012\n    temperature: 1\n- exp_id: exp-021-oracle-folio\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n: 204\n    k: 12\n    oracle_sica_accuracy: 0.8824\n    sc_accuracy: 0.7941\n    sica_self_accuracy: 0.7941\n    oracle_vs_sc_delta_pp: 8.82\n    oracle_vs_sica_delta_pp: 8.82\n    mcnemar_p_oracle_vs_sc: 6.15e-05\n    z3_gold_agreement: 0.946\n    fol_parse_success: 1\n    model: Qwen2.5-14B-Instruct\n    dataset: FOLIO-204\n    constraint_source: gold FOL annotations\n- exp_id: exp-012-gsm8k-pilot\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    n: 30\n    k: 12\n    sica_accuracy: 0.9667\n    sc_accuracy: 0.9667\n    delta_pp: 0\n    multi_candidate_rate: 0.133\n    extraction_success_rate: 0.147\n    model: Qwen2.5-14B-Instruct\n    dataset: GSM8K\n    temperature: 0.7\n- exp_id: exp-004-qwen7b\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    n: 60\n    k: 12\n    sica_accuracy: 0.6833\n    sc_accuracy: 0.6833\n    delta_pp: 0\n    multi_candidate_rate: 0.433\n    extraction_rate: 0.9417\n    answer_extraction_rate: 1\n    contradiction_rate: 0.0274\n    discordant_sica_wins: 2\n    discordant_sc_wins: 2\n    mcnemar_p: 1\n    wall_time_s: 1838\n    truncated_traces: 0\n    model: Qwen2.5-7B-Instruct\n    dataset: D012\n    temperature: 0.7\n    folio_sica: 0.7667\n    folio_sc: 0.7333\n    folio_n: 30\n    proofwriter_sica: 0.6\n    proofwriter_sc: 0.6333\n    proofwriter_n: 30\n- exp_id: temperature-ablation-t07\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    n: 60\n    k: 12\n    sica_accuracy: 0.7167\n    sc_accuracy: 0.75\n    delta_pp: -3.33\n    multi_candidate_rate: 0.4\n    extraction_rate: 0.9208\n    answer_extraction_rate: 1\n    contradiction_rate: 0.022\n    discordant_sica_wins: 0\n    discordant_sc_wins: 2\n    truncated_traces: 0\n    model: Qwen2.5-14B-Instruct\n    dataset: D012\n    temperature: 0.7\n    proofwriter_sica: 0.6333\n    proofwriter_sc: 0.7\n    proofwriter_n: 30\n    folio_sica: 0.8\n    folio_sc: 0.8\n    folio_n: 30\n    wall_time_s: 3498.3\n- exp_id: exp-022-oracle-proofwriter\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n: 600\n    k: 12\n    oracle_sica_accuracy: 0.8667\n    sc_accuracy: 0.7517\n    sica_self_accuracy: 0.755\n    oracle_vs_sc_delta_pp: 11.5\n    mcnemar_p_oracle_vs_sc: 9.21e-15\n    z3_gold_agreement: 0.9714\n    z3_gold_agree_n: 577\n    z3_gold_total: 594\n    parse_errors: 6\n    parse_error_rate: 0.01\n    solver_errors: 0\n    solver_total: 7128\n    relneg_oracle: 0.7786\n    relneg_sc: 0.6\n    relneg_delta_pp: 17.86\n    relnoneg_oracle: 0.7945\n    relnoneg_sc: 0.6644\n    relnoneg_delta_pp: 13.01\n    attnoneg_oracle: 0.961\n    attnoneg_sc: 0.8701\n    attnoneg_delta_pp: 9.09\n    attneg_oracle: 0.9188\n    attneg_sc: 0.85\n    attneg_delta_pp: 6.87\n    model: Qwen2.5-14B-Instruct\n    dataset: ProofWriter-OWA-D5-600\n    constraint_source: gold DSL (raw_logic_programs)\n- exp_id: exp-023-discriminative-rate\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n_total: 804\n    n_multi_candidate: 307\n    source_disc_rate_weight: 0.392\n    source_disc_rate_weight_ci95:\n    - 0.387\n    - 0.398\n    source_disc_rate_count_est: 0.121\n    source_disc_rate_count_ci95:\n    - 0.12\n    - 0.123\n    z3_semantic_disc_rate: 0.082\n    z3_semantic_disc_ci95:\n    - 0.076\n    - 0.088\n    problems_with_disc: 289\n    problems_with_disc_rate: 0.941\n    pw_source_disc_weight: 0.364\n    folio_source_disc_weight: 0.54\n    pw_n_multi: 235\n    folio_n_multi: 72\n    pilot_rate_reported_count: 0.115\n    pilot_rate_reported_weight: 0.372\n    pilot_validation_weight: 0.376\n    pilot_delta_pp: 0.38\n    z3_answer_assertions: 642\n    z3_total_unique_constraints: 7844\n    model: Qwen2.5-14B-Instruct\n    dataset: FOLIO+ProofWriter-804\n- exp_id: exp-026-folio204-trace-regen\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n: 204\n    k: 12\n    sica_accuracy: 0.7451\n    sc_accuracy: 0.75\n    delta_pp: -0.49\n    extraction_rate: 0.9853\n    model: Qwen2.5-14B-Instruct\n    dataset: FOLIO-204\n    temperature_trace: 0.7\n    temperature_extraction: 0.3\n    wall_time_h: 2.5\n- exp_id: exp-027-qwen3-14b-non-thinking\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n: 204\n    k: 12\n    sica_accuracy: 0.8431\n    sc_accuracy: 0.8382\n    delta_pp: 0.49\n    extraction_rate: 0.995\n    contradiction_rate: 0.0283\n    problems_with_contradictions: 69\n    total_constraints: 16153\n    unique_constraints: 7031\n    wall_time_s: 11017\n    model: Qwen3-14B\n    dataset: FOLIO-204\n    mode: non-thinking\n- exp_id: exp-028-qwen3-14b-thinking\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: exp-029-contrastive-folio204\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    contrastive_accuracy: 0.7253\n    sc_accuracy: 0.7363\n    delta_pp: -1.1\n    discriminative_rate: 0.0604\n    discriminative_count: 11\n    n: 182\n    recovery_rate_pct: -8.3\n    mcnemar_chi2: 0.1\n    mcnemar_p: 0.7518\n    cont_only_correct: 4\n    sc_only_correct: 6\n    both_correct: 128\n    both_wrong: 44\n    supporting_pct: 43.2\n    opposing_pct: 56.8\n    avg_constraints_per_problem: 24.4\n    avg_unique_per_problem: 10.4\n    wall_time_min: 47.2\n- exp_id: exp-030-crossmodel-mistral-folio204\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    n: 204\n    k: 12\n    crossmodel_sica_accuracy: 0.75\n    sc_accuracy: 0.75\n    delta_pp: 0\n    discriminative_rate: 0\n    recovery_rate: 0\n    model_extraction: Mistral-7B-Instruct-v0.3\n    model_traces: Qwen2.5-14B-Instruct\n    dataset: FOLIO-204\n- exp_id: exp-031-oracle-folio-regen\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n: 204\n    k: 12\n    oracle_sica_accuracy: 0.8971\n    sc_accuracy: 0.7549\n    sica_self_accuracy: 0.7451\n    oracle_vs_sc_delta_pp: 14.22\n    oracle_vs_sica_delta_pp: 15.2\n    mcnemar_p_oracle_vs_sc: 2.0024e-07\n    mcnemar_b_c:\n      b_oracle_right_sc_wrong: 29\n      c_oracle_wrong_sc_right: 0\n    z3_gold_agreement: 0.951\n    z3_gold_agree_n: 194\n    z3_in_candidates_n: 178\n    fol_parse_success: 1\n    model: Qwen2.5-14B-Instruct\n    dataset: FOLIO-204\n    constraint_source: gold FOL annotations\n    traces_source: exp-026-folio204-trace-regen\n- exp_id: exp-033-qwen3-pw600-nonthinking\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp-035\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    n_problems: 203\n    sc_accuracy: 77.34\n    sica_accuracy: 76.85\n    delta_pp: -0.49\n    sica_correct: 156\n    sc_correct: 157\n    mcnemar_discordant_b: 1\n    mcnemar_discordant_c: 2\n    mcnemar_p_value: 1\n    c0_non_unanimous_rate: 0.5517\n    extraction_rate: 98.19\n    contradiction_rate: 1.58\n    problems_with_contradictions: 60\n    total_constraints: 12950\n    unique_constraints: 6515\n    dedup_ratio: 50.3\n    wall_time_min: 78.2\n    avg_per_problem_s: 23.1\n- exp_id: exp-034\n  name: ''\n  status: DEPLOYED\n  conclusion: failed\n  metrics:\n    n_problems: 93\n    n_target: 600\n    completion_pct: 15.5\n    sica_accuracy: 77.42\n    sc_accuracy: 74.19\n    delta_pp: 3.23\n    sica_correct: 72\n    sc_correct: 69\n    mcnemar_discordant_b: 6\n    mcnemar_discordant_c: 3\n    mcnemar_p_value: 0.5078\n    c0_non_unanimous_rate: 0.581\n    avg_majority_frac: 0.8324\n    extraction_rate: 99.19\n    contradiction_rate: 11.83\n    problems_with_contradictions: 11\n    avg_unique_constraints: 35.6\n    total_constraints: 14437\n    unique_constraints: 3308\n    dedup_ratio: 22.9\n    k: 12\n    level: OWA-D5\n    gt_distribution:\n      'True': 32\n      'False': 28\n      Unknown: 33\n    wall_time_s: 6086.4\n    status_note: 'INCOMPLETE: crashed at 93/600 (python not found after conda env\n      lost)'\n- exp_id: exp-007-qwen72b-awq\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp-004-qwen7b-rerun\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp-036-z3-feedback-folio204\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    z3fb_sica_accuracy: 0.775\n    vanilla_sica_accuracy: 0.745\n    sc_accuracy: 0.75\n    z3fb_vs_vanilla_delta: 0.03\n    unsat_traces: 22\n    total_traces: 2448\n    unsat_rate: 0.009\n    unsat_resolve_rate: 0.864\n    problems_flipped: 0\n    real_impact: 0\n- exp_id: exp-033\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n_problems: 204\n    sica_accuracy: 59.31\n    sc_accuracy: 54.41\n    delta_pp: 4.9\n    sica_correct: 121\n    sc_correct: 111\n    mcnemar_discordant_b: 12\n    mcnemar_discordant_c: 2\n    mcnemar_p_value: 0.0129\n    c0_non_unanimous_rate: 0.8137\n    avg_majority_frac: 0.7515\n    extraction_rate: 97.14\n    contradiction_rate: 3.5\n    problems_with_contradictions: 128\n    avg_unique_constraints: 39.3\n    maxsat_mean_sat_ratio: 0.9609\n    total_constraints: 14042\n    unique_constraints: 8021\n    wall_time_min: 81.4\n    k: 12\n- exp_id: exp-039-14b-pw600-16639\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp-040-qwen3-pw600-16639\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp-041-14b-folio204-16639\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    n: 204\n    dataset: FOLIO-204\n    model: Qwen2.5-14B-Instruct\n    k: 12\n    sica_accuracy: 75.49\n    sc_accuracy: 77.45\n    delta_pp: -1.96\n    sica_correct: 154\n    sc_correct: 158\n    mcnemar_discordant_b: 0\n    mcnemar_discordant_c: 4\n    mcnemar_p_value: 0.125\n    extraction_rate: 0.98\n    contradiction_rate: 0.0097\n- exp_id: exp-038-14b-logiqa200-16639\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    n: 200\n    dataset: LogiQA-200\n    model: Qwen2.5-14B-Instruct\n    k: 12\n    sica_accuracy: 78\n    sc_accuracy: 78.5\n    delta_pp: -0.5\n    mcnemar_p: 1\n    sica_correct: 156\n    sc_correct: 157\n    discordant_b: 1\n    discordant_c: 2\n    both_correct: 155\n    both_wrong: 42\n    extraction_rate: 0.864\n    fail_empty_rate: 0.122\n    avg_unique_constraints: 26.7\n    contradiction_rate: 0.008\n    wall_time_min: 126.8\n- exp_id: exp-042-premise-formalization\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp-043-consistency-filtering\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    sc_accuracy: 0.75\n    sica_t1_all: 0.7794\n    sica_t4: 0.75\n    sica_t6: 0.7549\n    sica_t8: 0.7549\n    avg_unique_constraints: 13.2\n    avg_filtered_t4: 1.8\n    avg_filtered_t6: 0.8\n    avg_filtered_t8: 0.3\n- exp_id: exp-044-icl-oracle\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp-045-backward-verification\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics: {}\n- exp_id: exp-036b-cross-trace-unsat\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    cross_unsat_rate_pair: 0.087\n    cross_unsat_rate_problem: 0.107\n    within_trace_unsat_rate: 0.009\n    unsat_pairs: 11\n    total_pairs: 126\n    problems_with_unsat: 9\n    multi_answer_problems: 84\n    single_answer_skip: 120\n    zero_shared_var_pairs_pct: 0.564\n    avg_shared_vars: 2.7\n    false_true_unsat_rate: 0.467\n    sica_cross_ut_accuracy: 0.745\n    sc_accuracy: 0.75\n    accuracy_impact: 0\n- exp_id: exp-042b-premise-formal\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp-044b-icl-oracle\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    n: 199\n    dataset: FOLIO-199\n    model: Qwen2.5-14B-Instruct\n    k: 12\n    sica_accuracy: 74.87\n    sc_accuracy: 74.37\n    delta_pp: 0.5\n    sica_correct: 149\n    sc_correct: 148\n    icl_examples: 5\n    extraction_failure_rate: 0.008\n- exp_id: exp-045b-backward-verify\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: exp-046-mistral-pw600\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    n: 600\n    sc_accuracy: 39.33\n    sica_accuracy: 36.5\n    delta_pp: -2.83\n    sc_wins: 30\n    sica_wins: 13\n    mcnemar_p: 0.0095\n    significant: true\n    dataset: ProofWriter-D5-600\n    model: Mistral-7B-Instruct-v0.3\n- exp_id: exp-028b-qwen3-thinking-folio204\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: exp-048-llama8b-pw600\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp-049-mistral-logiqa200\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp-050-mistral-icl-oracle-folio199\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp-050b-mistral-icl-oracle\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    n: 199\n    sc_accuracy: 57.79\n    sica_accuracy: 54.27\n    delta_pp: -3.52\n    sc_correct: 115\n    sica_correct: 108\n    discordant_b: 6\n    discordant_c: 13\n    mcnemar_p: 0.167\n    significant: false\n    wall_time_min: 93.8\n    extraction_success: 2333\n    extraction_fail: 55\n    per_answer:\n      'True':\n        n: 70\n        sica_acc: 50\n        sc_acc: 54.29\n      'False':\n        n: 61\n        sica_acc: 36.07\n        sc_acc: 44.26\n      Unknown:\n        n: 68\n        sica_acc: 75\n        sc_acc: 73.53\n- exp_id: exp-049b-mistral-logiqa200\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    n: 200\n    sc_accuracy: 51\n    sica_accuracy: 51.5\n    delta_pp: 0.5\n    sc_correct: 102\n    sica_correct: 103\n    discordant_b: 6\n    discordant_c: 5\n    mcnemar_p: 1\n    significant: false\n    wall_time_min: 78.6\n    extraction_rate: 0.9725\n    total_constraints: 10659\n    unique_constraints: 8934\n    contradiction_rate: 0.0196\n- exp_id: exp-051-mistral-k-sensitivity\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp-052-mistral-folio204-seed123\n  name: ''\n  status: QUEUED\n  conclusion: ''\n  metrics: {}\n- exp_id: exp-053-mistral-folio204-seed456\n  name: ''\n  status: QUEUED\n  conclusion: ''\n  metrics: {}\n- exp_id: exp-052\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n: 204\n    sc_accuracy: 53.9\n    sica_accuracy: 57.4\n    sc_correct: 110\n    sica_correct: 117\n    delta_pp: 3.43\n    discordant_b: 8\n    discordant_c: 1\n    extraction_rate: 0.971\n    contradiction_rate: 0.034\n    wall_time_min: 81.9\n    mcnemar_p: 0.0391\n    significant: true\n- exp_id: exp-053\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    n: 204\n    sc_accuracy: 56.37\n    sica_accuracy: 55.88\n    sc_correct: 115\n    sica_correct: 114\n    delta_pp: -0.49\n    discordant_b: 2\n    discordant_c: 3\n    extraction_rate: 0.97\n    contradiction_rate: 0.033\n    wall_time_min: 80.8\n    mcnemar_p: 1.0\n    significant: false\n- exp_id: exp-054-mistral-folio204-t10\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    n: 204\n    sc_accuracy: 54.9\n    sica_accuracy: 55.4\n    delta_pp: 0.49\n    discordant_b: 5\n    discordant_c: 4\n    mcnemar_chi2: 0.1111\n    mcnemar_p: 0.7389\n    extraction_rate: 97.3\n    contradiction_rate: 3\n    wall_time_min: 83\n- exp_id: exp-055-multitemp-mistral-folio\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp-057-mistral-folio204-t03\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp-058-mistral-folio204-t05\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: best\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-19T03:42:52.131Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-19T03:42:52.131Z",
  "sessionId": "ce350913-1529-4773-bc92-65a3a830432f"
}
```

---

## Round 1

11 recorded events

### User

_source line 3 · 2026-05-19T03:42:52.159Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：

含义：Dual Bottleneck framing 完全成立：Eff-K+SC 作为跨条件预测器有效，K/T sensitivity 曲线 clean，所有 pending 实验结果与理论一致。Main conference 可争取。
核心假设：['exp-051 Mistral K sensitivity 呈现 clean inverted-U，peak 在 K=10-14 区间，两侧单调递减', 'T sensitivity 呈现 clean peaked curve: T=0.3 ≤+1pp, T=0.5 ~+2pp, T=0.7 +4.9pp, T=1.0 +0.5pp', 'exp-055 multi-temp 确认 negative (≤+0.5pp n.s.) → diversity alone 不足以打破 bottleneck', 'Eff-K × SC 双因子在所有已完成条件上 rank-consistent: 仅 Goldilocks zone (Eff-K>1.5 AND 45%&lt;SC<60%) 出现正向 delta', 'seed 内 κ-delta 非单调可被 Unknown 比例 / trace decisiveness 完全解释']
关键指标范围：{'mistral_k_peak_delta_pp': [4.0, 6.0], 'mistral_k_k4_delta_pp': [-2.0, 1.0], 'mistral_k_k20_delta_pp': [-1.0, 2.0], 'mistral_k_inverted_u_visual': 'peak 与两侧差值 ≥2pp，无 non-monotonic outlier', 't03_delta_pp': [-1.0, 1.0], 't05_delta_pp': [0.5, 3.0], 'multitemp_delta_pp': [-2.0, 0.5], 'effk_sc_joint_prediction_accuracy': '≥10/12 conditions 方向正确 (正 delta 仅在 Goldilocks zone)', 'estimated_reviewer_avg': [3.0, 3.5]}
叙事方向：原始 Dual Bottleneck framing 完全保留。五条 claims 无需降级。 Hero figure: SC×Eff-K scatter 清晰划分四象限，Goldilocks zone 与 positive delta 完美重合。 K sensitivity inverted-U 作为独立 ablation contribution。 T sensitivity 的 narrow window 强化"效应真实但脆弱"叙事——脆弱性本身 IS the finding。 9 种修复失败 + oracle gap 构成完整的"结构性限制"论证。 投稿目标: EMNLP Main，Findings 作为安全网。预期 score 3.0-3.5。


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
  "promptId": "f3d087e2-424f-4bc4-83d1-1b1e056dff73",
  "type": "user",
  "uuid": "519c234a-9418-4c34-871f-5ac7f531e795",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3",
  "sessionId": "ce350913-1529-4773-bc92-65a3a830432f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-19T03:42:52.157Z_

```json
{
  "parentUuid": "519c234a-9418-4c34-871f-5ac7f531e795",
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
  "uuid": "301ea125-ddf9-441e-81eb-a6b0691a029c",
  "timestamp": "2026-05-19T03:42:52.157Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3",
  "sessionId": "ce350913-1529-4773-bc92-65a3a830432f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-19T03:42:52.157Z_

```json
{
  "parentUuid": "301ea125-ddf9-441e-81eb-a6b0691a029c",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "1883178d-93e6-4a93-b21d-f287d90b7cf6",
  "timestamp": "2026-05-19T03:42:52.157Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3",
  "sessionId": "ce350913-1529-4773-bc92-65a3a830432f",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：Dual Bottleneck framing 完全成立：Eff-K+SC 作为跨条件预测器有效，K/T sensitivity 曲线 clean，所有 pending 实验结果与理论一致。Main conference 可争取。 核心假设：['exp-051 Mistral K sensitivity 呈现…",
  "leafUuid": "1883178d-93e6-4a93-b21d-f287d90b7cf6",
  "sessionId": "ce350913-1529-4773-bc92-65a3a830432f"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Dual bottleneck framing validation across Mistral seeds and temperature sensitivity",
  "sessionId": "ce350913-1529-4773-bc92-65a3a830432f"
}
```

---

### Assistant

_source line 8 · 2026-05-19T03:48:03.200Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed predicted results for all "planned" experiments in the experiment_plan, under the "best" tier scenario. I need to go through each experiment that has status "planned" and predict what the results would look like if the best-case scenario holds.

Let me also check the currently RUNNING experiments, as those are also pending results.

Let me identify all experiments that are not DONE:

**Planned experiments:**
- exp-002: sica_k_ablation_14b (K sensitivity on D012 60 questions, Qwen-14B)
- exp-003: tiebreak_baseline_analysis (already done as CPU analysis, noted in plan)


- exp-006: c0_diagnostic_validation
- exp-008: constraint_quality_case_studies

Now I'm scanning through the registry to see which experiments are already completed or failed, filtering out the ones that don't need predictions.

Looking at the currently running experiments across different model configurations and parameter settings, and there are a few queued ones waiting to start.

Now I'm checking the experiment plan against the registry to see which ones marked as "planned" are actually complete or still need to run. Most of the earlier experiments through exp-019 are already done, with exp-051 currently executing. I need to identify which planned experiments still need detailed predicted data generated under the best tier. I'm seeing that many experiments marked as "planned" in the experiment_plan are actually already completed in the registry, so I need to clarify what the user is asking for—whether they want predictions for all planned experiments regardless of completion status, or just the ones that haven't been run yet. The core task seems to be generating detailed predictions for planned experiments that align with the "best" tier definition, but I should focus on those that are either still planned and not yet executed, or currently running or queued. I'm seeing a list of running experiments in the registry, but I think I've been overcomplicating this. The user is asking for predicted results for every planned experiment in the experiment_plan with detailed rationales, so let me just go through and list all the planned ones systematically. Looking at the additional experiments I need to run—exp-057 and exp-058 are testing temperature sensitivity at 0.3 and 0.5 respectively, while exp-039, exp-040, and exp-048 appear to be complementary validation runs that should help confirm the peaked curve pattern I'm expecting across the temperature range.

Now I'm examining the performance metrics across these conditions to establish the bounds for what constitutes a successful result—the Mistral K peak should land between 4-6 percentage points, the inverted-U shape needs to hold with at least 2pp difference between peak and edges, and the temperature effects should show that sweet spot around T=0.5 where I get the strongest gains.

I'm thinking through the predictions for the K ablation experiment on the 14B model, which was already run with Qwen and showed SICA staying below SC across all K values—that result actually fits the best tier framework because Qwen operates in a different regime where this relationship holds.

Now I'm working through the remaining experiments: the tiebreak test confirmed SICA at 80% versus random baseline, the 7B Qwen variant showed zero improvement, and the C0 diagnostic reveals a clean pattern where low C0 blocks gains entirely while high C0 combined with high SC also prevents improvement due to confirmation bias—only the mid-SC zone allows gains. The 72B model should show even stronger confirmation bias effects, pushing C0 lower and making SICA converge with SC.

Moving through the case studies which demonstrate semantically valid constraints but still suffer from confirmation bias, the overhead analysis is already documented, and LLaMA 8B shows a meaningful +6.67 percentage point gain with C0 at 61.7%. GSM8K pilot data shows minimal C0 at 13.3% with SICA matching SC, while Logic-LM experiments confirm that single-trace verification fails when traces aren't independent—the weighted SC variants all came back non-significant, and StrategyQA results are also in the registry.

For the running experiments, I need to track the sensitivity analyses: Mistral K sensitivity predicts a clean inverted-U pattern, multi-temperature work predicts negative effects, T=0.3 shows minimal gains around +1pp, and T=0.5 suggests roughly +2pp improvement. These are still active and critical to the best-tier narrative, though I'm realizing the user specifically asked for planned experiments, so I should clarify whether the running ones count toward that scope. I'm noticing a discrepancy between the experiment_plan document and the registry—the newer experiments like exp-051 through exp-058 aren't listed in the original plan but are referenced in the best tier definition, so I should include both the planned experiments from the document and these critical running ones from the registry. The cleanest approach is to cover all the planned experiments marked in the experiment_plan plus the key running experiments that matter for the best tier assessment.

Now I'm sorting through which experiments have already completed so I can use their actual results, versus which ones still need predictions—exp-002, exp-003, exp-004, exp-005, exp-009 through exp-012 are all marked as done in the registry, so I'll pull their real data rather than generating predictions for those.

Generating the YAML output... I'm reconsidering the scope here—the user asked for predictions on experiments in the plan, but the running experiments from the registry are actually critical to the best tier narrative, so I should include both the planned ones without results and the active registry experiments that matter for the core assumptions. I need to clarify which experiments are actually marked as planned versus completed in the experiment plan. Looking through the list, exp-001 and exp-010 are the only ones marked DONE, while everything else is planned. For the planned experiments that already have completed results in the registry, I should present those actual results as the expected outcomes under the best tier scenario, since they represent what actually happened.

For planned experiments without registry data and the running experiments that matter for the best tier narrative, I'll generate predictions based on best-tier assumptions. This approach keeps everything consistent with the known results while filling in gaps for the incomplete work.

Now I'm going to compile the full YAML with all planned and running experiments, making sure to include the critical running ones like exp-051, 055, 057, and 058. For each experiment, I'll use actual data where it exists and predictions where it doesn't.

Looking at the completed experiments: exp-002 shows SICA ≤ SC across all K values for Qwen-14B, which fits the best tier since Qwen-14B operates in the high SC regime where confirmation bias constrains SICA's effectiveness. exp-003 demonstrates SICA at 80% versus random at 50%, exp-004 shows delta=0 with C0=43.3% for Qwen 7B despite higher diversity than the 14B model, and exp-005 with QwQ-32B reveals near-zero effective diversity with SICA≡SC. I'm continuing through the remaining experiments to build out the complete picture. C0 diagnostic):** CPU analysis across all models. Under best, C0 alone isn't sufficient predictor, but Eff-K × SC together predict ≥10/12 conditions correctly.

**exp-007 (72B AWQ):** Failed in registry. Under best, if rerun: SC~85%, C0<10%, SICA≡SC. Confirms Type A at extreme.

**exp-008 (case studies):** Qualitative. Under best: constraints are semantically meaningful, but both_wrong cases show constraints from wrong reasoning are internally consistent but directionally aligned with model's error.

**exp-009 (overhead):** Done. ~49% overhead.

**exp-011 (LLaMA 8B):** Done. delta=+6.67pp n.s. (n=60). Under best, this is consistent with Goldilocks zone (SC=60%, C0=62%).

**exp-012 (GSM8K):** Done. C0=13%, SICA=SC. Math domain, model too strong.

**exp-013 (constraint ablation):** MaxSAT performs similarly to count-only baseline, pointing to an independence bottleneck.

**exp-014 (DeepSeek R1):** Reasoning model shows negative control with delta=-3.33pp.

**exp-015 (Logic-LM baseline):** Under best, Logic-LM × K approximates SC, but single-trace verification repeated K times doesn't improve results since traces are correlated.

**exp-016 (weighted SC):** All results non-significant.

**exp-017 (StrategyQA):** delta=+3.33pp n.s., C0=10%.

**exp-018 (ARC):** delta=-1.67pp, C0=5%.

**exp-019 (constraint quality correlation):** Looking at how constraint quality correlates with performance.

I'm seeing a clear pattern: when SC is high, constraints align too closely with the model's own reasoning and provide no new information. Mid-range SC yields some independent signal and potential gains, while low SC produces noisy constraints that actually hurt performance. For the running experiments, Mistral shows an inverted-U curve peaking around K=10-14 with gains of 4-6pp, while diversity alone through temperature sampling doesn't break the bottleneck.

Looking at the larger context experiments, Qwen-14B on ProofWriter stays in the high-SC regime with near-zero gains, Qwen3 shows small non-significant improvements, and LLaMA-8B lands in that mid-SC sweet spot consistent with the Goldilocks hypothesis. Now I'm organizing all these results into a structured format with proper justifications for each finding. Now I'm working through the specific performance numbers for exp-051, examining how Mistral's behavior changes across different K values—K=4 shows insufficient diversity with minimal gains, K=8 starts capturing independent perspectives with modest improvements, and K=12 hits the sweet spot where constraint aggregation becomes effective, matching the observed delta from exp-033.

For K=16 and K=20, I'm seeing diminishing returns as additional traces become increasingly correlated and add noise rather than signal. But I'm realizing that self-consistency accuracy shouldn't vary much across K values since it's just majority voting—the real question is whether the correlation structure of the traces changes with K, which would affect how stable that majority vote becomes.

Looking at the actual Qwen data, self-consistency stays pretty flat around 73-75% across K=6 through K=16, then dips slightly at K=20. For Mistral on FOLIO, I'm expecting similar stability around 54% across different K values, so I can use that as my baseline and focus on how SICA improves relative to it.

Now I'm working through the SICA values at each K level and calculating the deltas—K=12 shows the biggest improvement at nearly 5 percentage points, while K=4 and K=20 are more modest. The effective K values suggest diminishing returns as K increases, plateauing around 1.9. But I need to make sure these deltas fit within the tier constraints, so I'm adjusting to keep peak delta in the 4-6 range and the boundary values within their specified windows.

For temperature sensitivity, I'm checking how different T values affect performance—T=0.7 gives the strongest delta at 4.9pp, while T=0.3 and T=1.0 are weaker. The multi-temperature approach barely moves the needle. All these values align with their expected ranges, so I can use them as-is.

Now I'm pulling together the full YAML structure with all the planned experiments from the experiment plan, making sure everything is organized and detailed.

Looking at which experiments to include, I need the original planned ones (exp-002 through exp-019) plus the critical running experiments that define the best tier (exp-051, exp-055, exp-057, exp-058, exp-039, exp-040, exp-048). That gives me about 24 total.

I notice several of these are already completed in the registry—exp-003, exp-004, exp-005, exp-009, exp-012, exp-013, exp-014, exp-016, exp-017, exp-018—so for those I'll use the actual results rather than predictions. For the incomplete and running ones, I'll provide predicted values based on the patterns I've identified.

The structure needs to be clear: each experiment gets a name, plan ID, description, expected results with metrics, rationale for how it supports the best tier narrative, and any relevant analysis or tables. Let me start writing this out systematically. Now I'm mapping out the tables and figures that will support the narrative. The main results table will show performance across all models and domains, with separate tables for oracle controls, independence metrics like Fleiss' kappa, extraction error taxonomy, and K sensitivity analysis. For figures, I need the method pipeline diagram, a scatter plot showing the relationship between SC and effective K as the hero figure, sensitivity curves with diversity metrics, and a breakdown of extraction errors. Each experiment feeds into specific tables and figures, so I'm organizing them accordingly.

Now I'm finalizing the numbers and writing out the YAML structure. For the K ablation experiment on Qwen-14B that's already completed, I'm pulling the actual results showing that SICA stays at or below SC across all K values, which fits the best tier interpretation.

Qwen represents a Type A case where SC hovers around 75% but SICA can't improve it because the fundamental issue is confirmation bias, not diversity. This supports the dual bottleneck hypothesis—you need both effective K above a threshold AND sufficient SC to make progress. The tiebreak experiment shows SICA does add value in edge cases, but ties are infrequent enough that the overall impact is modest. Qwen 7B performs even worse with lower SC and high kappa, confirming the pattern. QwQ-32B is a reasoning model with near-zero diversity, so SICA and SC converge. I'm now validating the C0 diagnostic approach.

The CPU analysis shows the Eff-K × SC scatter correctly predicts at least 10 out of 12 conditions, with a clear Goldilocks zone emerging. The 72B AWQ model hit registry issues but the prediction suggests extreme Type A behavior with very high SC and minimal C0. Looking at case studies qualitatively, the constraints are semantically valid FOL expressions, the both_wrong cases reveal internally consistent but incorrect constraints, and override cases demonstrate SICA working when traces have genuine diversity. The overhead analysis shows about 49% total cost, almost entirely from extraction with MaxSAT being negligible. Now examining LLaMA 8B on D012...

For the LLaMA 8B experiment with n=60, I'm seeing a delta of +6.67 percentage points with C0 at 61.7% and a McNemar p-value of 0.2188, putting it near the Goldilocks zone. The GSM8K pilot shows very low performance with only 13.3% C0 and 14.7% extraction success—math constraints are barely extractable. The constraint ablation reveals MaxSAT performs nearly identically to count-only with just 1 difference out of 804 cases, suggesting the independence bottleneck is the real limiting factor. DeepSeek R1 shows a negative delta of -3.33 percentage points, similar to QwQ as a reasoning model control. For Logic-LM, the baseline approach would repeat single-trace FOL verification K times and take a majority vote, though this experiment isn't complete yet.

Looking at the remaining experiments, Logic-LM's accuracy should approximate standard chain-of-thought since single-trace verification doesn't aggregate information across traces. Weighted chain-of-thought methods don't break through the independence bottleneck—all approaches are non-significant. StrategyQA shows a small non-significant improvement of +3.33 percentage points with low constraint extractability in the commonsense domain. ARC-Challenge actually shows a slight decline of -1.67 percentage points because the model is already too strong at 96.7% accuracy, representing an extreme Type A case. The constraint quality correlation experiment is still pending dependencies, but the emerging pattern suggests high chain-of-thought conditions correlate with strong constraint-model agreement.

Now examining the Mistral K sensitivity results on FOLIO-204, I'm seeing a clean inverted-U pattern across different constraint counts. At K=4, performance is essentially flat with a negligible delta. K=8 shows a modest improvement of about 2 percentage points. K=12 reaches the peak with a 4.9 percentage point gain that's statistically significant.

Beyond that, K=16 drops back to 2.5 percentage points, and K=20 falls further to just 1 percentage point—both sides of the peak show consistent monotonic decline. The temperature experiments tell a similar story: multi-temperature testing yields no effect, while lower temperatures (0.3 and 0.5) produce minimal to modest gains of 0.5 and 2.0 percentage points respectively, with only the 0.5 temperature condition approaching statistical significance.

Now looking at results across different models and datasets. Qwen-14B and Qwen3 both show negligible improvements around 0.5 percentage points on ProofWriter-600, consistent with their FOLIO performance. LLaMA-8B on the same dataset achieves a 2 percentage point gain, approaching but not reaching significance.

I'm ready to compile the YAML now, but first I need to verify the joint prediction model—checking whether at least 10 out of 12 conditions show the expected pattern where positive deltas only appear in the Goldilocks zone. Running through the conditions systematically to validate the Eff-K and SC predictions against observed results. Looking at the rest of the validation results, most predictions are holding up well—the Mistral-7B FOLIO s456 case is an outlier where my model predicted gain but the actual delta was slightly negative, which is the only clear miss so far. The other cases continue to align with expectations, including the borderline Goldilocks scenarios and the cases where low semantic coverage correctly predicts no improvement. Mistral s456 is right in the sweet spot for the Goldilocks zone at 56.4% with an efficiency multiplier of 2.22, but the delta came in negative at -0.49pp—that's the one case that doesn't fit the pattern. The framework accounts for this through the trace decisiveness factor, so with 11 out of 12 conditions predicted correctly plus an explanation for the outlier, this meets the best tier threshold. Now I need to finalize the YAML output, though I should first clarify which exact 12 model-dataset combinations the best tier is evaluating. I'm seeing there are actually way more experimental conditions than the initial 12 mentioned—at least 20 different model and dataset combinations. The "12 conditions" in the best tier probably refers to the most critical or complete ones, so I'll just note that the threshold holds at 10 or more out of 12 rather than trying to pin down the exact count.

Now I'm writing out the YAML configuration. I need to include all the planned experiments from the original list—that's exp-002 through exp-019, excluding the ones already marked done. I should also incorporate the running experiments that are essential to the best tier narrative, even if they weren't in the original plan.

For the completed experiments, I'll pull the actual results from the registry data and frame them within the best tier story. For the ones still pending or running, I'll project what the best tier outcomes would look like. Some entries like the tiebreak analysis and qualitative case studies aren't as central to the main narrative, but I'll include them anyway and keep those descriptions concise.

My structure is to cover all 17 originally planned experiments plus the key ones currently running—that gets me to around 23 or 24 total. For the YAML output, I'll use compact metric dictionaries and focused rationales to keep it readable.

The critical piece here is that for already-completed experiments, the "expected_results" should just be the actual results we've already observed, since in the best tier scenario those are now facts. The rationale then explains how those actual outcomes fit the dual bottleneck framing and the Eff-K × SC joint prediction story.

Let me start drafting the full YAML now, organized by experiment ID. I need to check the memory directory for any relevant context before proceeding. Let me review what I already have from the system prompt—the experiment plan, registry, and paper framing should cover everything, so I can move forward with writing out the full YAML configuration.

For the K sensitivity experiment, I'm working with the established pattern from prior ablations, so K values like 4, 8, 12, 16, 20 make sense. The inverted-U curve needs to show the peak around K=12 with appropriate deltas at each point—starting weak at K=4, climbing through K=8, peaking at K=12 with the documented 4.9pp improvement, then declining again at higher values.

I'm verifying the curve satisfies all the constraints: the peak-to-trough differences exceed the 2pp threshold, the progression is monotonic on both sides of the peak, and there are no unexpected outliers breaking the pattern.

Now I'm looking at how temperature affects the results. The sensitivity analysis shows a clear peak at T=0.7 with lower deltas at the extremes, and the multi-temperature approach yields essentially no improvement. The numbers check out, so I'm ready to generate the configuration file.

Before I do that, I need to reconsider how the K parameter affects the self-consistency values, since changing K alters the majority voting dynamics in ways that could impact the overall performance.

Looking at Mistral on FOLIO-204, the individual trace accuracy sits around 50-55%, which means the self-consistency at K=12 of 54.4% is reasonable. When I adjust K to 4, the self-consistency should remain fairly stable since the per-trace accuracy doesn't change—it's mainly the voting pool that shrinks. Across different temperatures, self-consistency hovers consistently around 54-55%, so I'll use that as my baseline estimate.

Now I need to work through the effective K calculations...

For the K sensitivity, I'm computing how the effective number of independent traces changes as K increases. With a correlation coefficient around 0.5, the effective K grows from about 1.6 at K=4 up to roughly 1.88 at K=16, showing diminishing returns as K gets larger.

The inverted-U pattern emerges because while effective K does improve with larger K values, the noise from additional constraints grows faster than the signal gain—so there's a sweet spot around K=12 where I get meaningful constraint aggregation without the dilution that comes from too many noisy constraints at higher K values.

Now I'm organizing the experiments into groups: completed ones where I'll pull actual registry data, and the ones still pending that I'll need to fill in with my calculated predictions. I'm deciding which experiments to include in the YAML output — the user asked for all planned experiments, so I should cover the 17 from the original plan plus the critical running ones that define the best tier results, bringing it to around 24 total entries. For completed experiments I'll pull actual results data and explain their tier placement, while for pending ones I'll provide detailed predictions with clear reasoning.

Now I'm clarifying what those expansion experiments actually are: exp-039 and exp-040 are Qwen variants on ProofWriter-600 with larger context windows, and exp-048 is LLaMA-8B on the same benchmark. These fill out the main results table, with exp-039 showing minimal improvement over the baseline and exp-040 showing no delta at all.

But I'm noticing something odd — exp-001 already tested Qwen-14B on PW-600 and got a small delta of +0.3pp, so why is exp-039 retesting essentially the same setup? The key difference appears to be the token limit: exp-039 uses 16639 tokens versus the standard context, which likely enables longer trace generation and potentially better extraction quality. This might be a retry of exp-034, which crashed partway through.

Looking at exp-039's results, I'm seeing SC around 75% and SICA around 75.5%, giving a delta of about +0.5pp — still not statistically significant. Now I want to verify something against the user's best tier: exp-055 is marked as running with no metrics yet, but the plan notes predict an early delta of 0.00pp, which aligns with the expected ≤+0.5pp result. The pattern I'm seeing suggests that diversity improvements alone aren't breaking through the bottleneck, and the real gains seem to cluster in the Goldilocks zone where both efficiency and SC factors align.

Let me check the specific conditions: positive delta only appears when Eff-K exceeds 1.5 AND SC stays between 45-60%. Verifying against the Mistral experiments — exp-033 and exp-052 both fall in this zone with their respective deltas of +4.9pp and +3.43pp, but exp-053 breaks the pattern with negative delta despite being in the Goldilocks range, which needs investigation. Meanwhile, PW-600 sits outside the zone with SC below the threshold, confirming the boundary conditions.

Now looking at the other models: Qwen-14B's Eff-K falls short of 1.5, so the zero delta makes sense, but LLaMA D012 presents an edge case — it's sitting right at the 60% boundary with a positive delta of +6.67pp, which technically violates the strict upper bound of the Goldilocks zone.

Checking the other LLaMA variants, FOLIO-204 shows SC above 60% with negative delta, which aligns with expectations, while StrategyQA has a non-significant positive delta that I can reasonably interpret as "no meaningful gain" rather than a true positive effect.

The tier definition seems internally consistent when accounting for these boundary cases, so I'm ready to generate the YAML output.

Now I'm compiling the experiment entries—about 24 total—with each one including the core metadata, expected metrics, rationale for the best tier classification, relevant paper tables and figures, and key findings. I'll note which experiments are already in the registry versus planned, and I'm including the critical running experiments (051, 055, 057, 058) since they're essential to the tier definition, even though they weren't originally in the plan.

Before I start writing the full YAML, I need to estimate the Eff-K values for LLaMA-8B since we don't have κ data for it. Using an estimated κ around 0.35, LLaMA-8B lands in the Goldilocks zone on both D012 and FOLIO-204 with Eff-K values around 2.5, which aligns with the best tier criteria.

I also just realized the experiment_plan doesn't include several newer experiments like exp-051, 055, 057, and 058, but since the best tier definition explicitly references these, I need to add predictions for them as additional entries beyond what was originally planned. Now let me actually write this out.

I'm organizing the results by mapping experiments to their corresponding tables and figures—the main results table will include the completed experiments plus pending ones, the oracle control and independence sections have their specific experiment sets, and I'm tracking which experiments contribute κ values and error taxonomy data. For the figures, I'm planning the method pipeline visualization and then the performance curves.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1883178d-93e6-4a93-b21d-f287d90b7cf6",
  "isSidechain": false,
  "requestId": "req_011CbBEgEw2Y4rcdfjZkTCGC",
  "type": "assistant",
  "uuid": "a178c160-779d-4fcb-8a22-be668146c97c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3",
  "sessionId": "ce350913-1529-4773-bc92-65a3a830432f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WzYkXVMvS4oPU3f413eexN",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 28873,
      "cache_read_input_tokens": 11841,
      "output_tokens": 30308,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 28873,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 30308,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 28873,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 28873
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

_source line 9 · 2026-05-19T03:52:51.812Z_

```yaml
tier: best
narrative_guidance: >
  Dual Bottleneck framing 完全保留，五条 claims 无需降级。
  Hero figure: Eff-K × SC scatter 将所有已完成条件清晰划分为四象限——Goldilocks zone (Eff-K>1.5, 45%&lt;SC<60%) 与 positive delta 完美重合。
  K sensitivity inverted-U (Mistral K=12 peak, 两侧 ≥2pp drop) 作为独立 ablation contribution，证明 nominal K≠Eff-K 的 practical consequence。
  T sensitivity peaked curve (T=0.7 only window) 强化"效应真实但脆弱"叙事——脆弱性本身 IS the finding，非 limitation。
  9 种修复失败 + oracle gap 构成完整"结构性限制"论证，multi-temp failure 补上最后一环。
  Seed-internal κ-delta 非单调性由 Unknown 比例 / trace decisiveness 完全解释，不再是 framing 弱点。
  投稿 EMNLP Main，Findings 安全网。预期 reviewer avg 3.0-3.5。

imagined_experiments:
  # ===== 已完成实验（actual data，解释 best-tier 一致性）=====

  - name: sica_k_ablation_14b
    plan_id: exp-002
    description: "K sensitivity (K=6,8,11,12,16,20) on D012 60 questions, Qwen2.5-14B. 含 odd-K=11 测试 tie mechanism。"
    expected_results:
      K6_sica: 0.733
      K6_sc: 0.733
      K6_gap_pp: 0
      K8_sica: 0.733
      K8_sc: 0.75
      K8_gap_pp: -1.7
      K11_sica: 0.733
      K11_sc: 0.733
      K11_gap_pp: 0
      K12_sica: 0.70
      K12_sc: 0.75
      K12_gap_pp: -5.0
      K16_sica: 0.717
      K16_sc: 0.75
      K16_gap_pp: -3.3
      K20_sica: 0.70
      K20_sc: 0.733
      K20_gap_pp: -3.3
      all_K_sica_leq_sc: true
    result_rationale: >
      Qwen-14B 在 D012 上 SC≈73-75% (Type A regime)，Fleiss' κ≈0.74-0.82 → Eff-K≈1.2-1.3，远低于 1.5 阈值。
      无论 K 如何变化，traces 高度相关导致 Eff-K 始终不足。增加 K 反而引入更多 confirmation bias 约束，
      稀释已有的少量 discriminative 信息。K=11 odd-K 验证 SICA 在无 tie 时仍为 0 gap → tie 不是唯一机制
      但在 Type A 条件下连 tie 机制也被 confirmation bias 抵消。
      这组结果完美支持 Dual Bottleneck: 当 Eff-K 不足时，K 的增加无法弥补。
    tables: ["T5-K-Sensitivity (Qwen panel)"]
    figures_description: ["F3 左侧 panel: Qwen K vs Δ 平线 / 下降趋势，与 Mistral inverted-U 对比"]
    analysis: >
      Type A regime 的 K ablation negative control。与 exp-051 (Mistral) 形成鲜明对比:
      同样增加 K，Mistral 出现 inverted-U 而 Qwen 持续为负/零 → 区别在于 base independence (κ)，不在 K 本身。
      K=11 (odd) gap=0 确认 SICA value 不仅限于 tiebreaking。

  - name: tiebreak_baseline_analysis
    plan_id: exp-003
    description: "SICA vs SC-random-tiebreak vs SC-deterministic。CPU-only reanalysis。"
    expected_results:
      sica_tiebreak_accuracy_pct: 80
      random_tiebreak_pct: 50
      alphabetical_tiebreak_pct: 60
      first_seen_tiebreak_pct: 40
      n_ties: 5
    result_rationale: >
      在 tied cases 中 SICA 4/5 正确，random 期望 50%。说明 MAX-SAT 约束在 tie 情况下提供真实信号。
      但 tied cases 总量少(5/60=8.3%)，所以 tiebreak 机制对 overall accuracy 贡献有限(≤0.4pp)。
      这支持 best tier narrative: SICA 有 mechanism value 但实际 impact 受限于 independence bottleneck——
      traces 太相关导致 ties 本身就少。
    tables: ["T1 footnote (tiebreak analysis)"]
    figures_description: []
    analysis: >
      SICA tie resolution 有 80% precision，证明约束包含真实语义信息。
      但 tie 频率太低限制了 practical impact。这恰好是 independence bottleneck 的另一面证据。

  - name: sica_7b_scaling
    plan_id: exp-004
    description: "Qwen2.5-7B-Instruct on D012 60 questions (K=12, T=0.7)。Within-Qwen scaling 维度。"
    expected_results:
      n: 60
      sica_accuracy: 0.6833
      sc_accuracy: 0.6833
      delta_pp: 0
      multi_candidate_rate: 0.433
      extraction_rate: 0.9417
      mcnemar_p: 1.0
      folio_sica: 0.7667
      folio_sc: 0.7333
      pw_sica: 0.60
      pw_sc: 0.6333
    result_rationale: >
      Qwen-7B SC 降到 68.3% (vs 14B 的 75%)，C0 升到 43.3% (vs 14B 的 38%)。
      C0 上升但 delta 仍为 0 → 说明 C0 (diversity) 是必要非充分条件。
      Qwen family 的 κ 值仍然很高(估计 κ≈0.65-0.7)，Eff-K≈1.4，刚好低于 1.5 阈值。
      SC=68% 也在 Goldilocks 上界(60%)之上。双重不满足 → delta=0。
      这强化了 Dual Bottleneck framing: 即使降低模型大小增加多样性，同家族 trace 相关性仍太高。
    tables: ["T1-Main-Results (Qwen-7B row)", "T3-Independence (κ estimation)"]
    figures_description: ["F2 scatter: Qwen-7B 点落在 Eff-K<1.5 区域，与 Qwen-14B 相邻"]
    analysis: >
      Within-Qwen scaling: 7B→14B SC 增加但 delta 不变(均为 0)。
      排除 "Qwen-14B too strong" 假设——即使 weaker Qwen 也无法从 SICA 获益，问题在 family-level 的高 κ。

  - name: qwq_32b_operating_regime
    plan_id: exp-005
    description: "QwQ-32B negative results。Data from MVP phase。"
    expected_results:
      qwq_aggregate_c0_effective_pct: 2.6
      qwen14b_c0_pct: 46.0
      diversity_ratio_effective: 17.7
      aime_delta_pp: 0
      proofwriter_delta_pp: -5.9
      total_problems: 46
    result_rationale: >
      QwQ-32B 是 reasoning model，其 extended chain-of-thought 产生极度确定性的输出。
      C0_effective=2.6% 意味着几乎所有问题都有 unanimous answer → SICA≡SC structurally。
      这是 Claim 2 (regime-dependent) 的极端案例: reasoning model 的 trace 独立性接近零，
      Eff-K≈1.0，完全退化为 SC。PW delta=-5.9pp 说明少数 non-unanimous cases 中约束反而有害。
    tables: ["T1-Main-Results (QwQ-32B row)", "T3-Independence (QwQ entry)"]
    figures_description: ["F2 scatter: QwQ-32B 极端左上角 (Eff-K≈1.0, high SC)"]
    analysis: >
      Reasoning model negative control。C0_effective=2.6% vs non-reasoning Qwen-14B 46% →
      reasoning 能力消除了 trace diversity。SICA 对 reasoning model 完全无用，印证 independence bottleneck。

  - name: c0_diagnostic_validation
    plan_id: exp-006
    description: "Plot C0 / Eff-K × SC vs SICA-SC gap across all models。CPU-only meta-analysis。"
    expected_results:
      n_conditions: 12
      effk_sc_joint_correct_directions: 11
      goldilocks_positive_only: true
      c0_alone_prediction_accuracy: 7_of_12
      effk_sc_r_squared: 0.72
      goldilocks_zone_eff_k_lower: 1.5
      goldilocks_zone_sc_lower: 0.45
      goldilocks_zone_sc_upper: 0.60
      only_exception: "exp-053 (Mistral s456: Goldilocks zone 但 delta=-0.49pp，由 Unknown 比例/trace decisiveness 解释)"
    result_rationale: >
      汇总所有已完成条件后，Eff-K × SC 联合预测方向正确率 ≥10/12:
      - Type A (Qwen-14B/7B/3, ARC, GSM8K): Eff-K<1.5 → 0 delta ✓
      - QwQ/DeepSeek-R1: Eff-K≈1.0 → 0/negative ✓
      - Mistral FOLIO s42/s123: Goldilocks → positive ✓
      - Mistral PW-600: SC=39%<45% → negative ✓
      - LLaMA D012: SC≈60%(边界)，Eff-K≈2.5 → positive ✓
      - LLaMA FOLIO-204: SC=63%>60% → negative ✓
      exp-053 (Mistral s456) 是唯一 Goldilocks zone 内 delta 非正例外，但 Unknown 比例(58.5% vs exp-033 的 49.9%)
      和 trace decisiveness 差异完全解释了这一偏差。
      C0 单独预测不如 Eff-K × SC 联合(7/12 vs 11/12)，因为 C0 不区分 independence 和 quality。
    tables: ["T3-Independence (meta-analysis row)"]
    figures_description:
      - "F2 (Hero Figure): Eff-K × SC scatter, 四象限划分。x轴=Eff-K, y轴=SC, 点大小=|delta|, 颜色=delta 方向。
         Goldilocks zone (右中区域) 内所有实心点(positive delta)，zone 外所有空心点(zero/negative)。
         exp-053 标注为 explained outlier。"
    analysis: >
      Hero figure 的数据基础。证明 Eff-K × SC 是 parsimonious 且 predictive 的跨条件框架。
      C0 alone 不够 → 需要 independence 和 quality 两个维度。这是 Dual Bottleneck 的核心 empirical evidence。

  - name: sica_72b_awq
    plan_id: exp-007
    description: "Qwen2.5-72B-Instruct AWQ 4-bit on D012 60 questions。Within-Qwen extreme scaling。"
    expected_results:
      n: 60
      sica_accuracy: 0.8667
      sc_accuracy: 0.8667
      delta_pp: 0.0
      multi_candidate_rate: 0.10
      extraction_rate: 0.95
      mcnemar_p: 1.0
      estimated_kappa: 0.85
      estimated_eff_k: 1.18
    result_rationale: >
      72B 模型 SC 预期达 ~87% (远高于 14B 的 75%)，C0 降到 ~10% (Type A extreme)。
      κ≈0.85 → Eff-K≈1.18，是所有条件中最低的 Eff-K。
      几乎所有问题 unanimous → SICA≡SC。这是 Type A 的极端验证:
      模型能力越强 → traces 越一致 → 独立性越低 → SICA 越无用。
      Scaling 方向与 SICA utility 方向相反——这是 Dual Bottleneck 的 scaling implication。
    tables: ["T1-Main-Results (Qwen-72B row)", "T3-Independence"]
    figures_description: ["F2 scatter: 72B 在 extreme top-left (lowest Eff-K, highest SC)"]
    analysis: >
      Extreme Type A。与 Qwen-7B(delta=0, SC=68%) 和 14B(delta=0, SC=75%) 形成 within-family scaling curve:
      随模型增大，SC↑, Eff-K↓, delta 始终为 0。SICA 对 Qwen family 全面无效。

  - name: constraint_quality_case_studies
    plan_id: exp-008
    description: "5-10 representative questions 的约束质量定性分析。"
    expected_results:
      cases_analyzed: 8
      semantically_meaningful_pct: 87.5
      both_wrong_confirmation_bias_pct: 100
      override_correct_cases: 2
      trivially_satisfied_avg_pct: 43
      illustrative_patterns:
        - "correct_diverse: 约束来自不同推理路径，MAX-SAT 正确 override SC"
        - "confirmation_bias: 全部 12 traces 错误，约束一致指向错误答案"
        - "partial_correct: 8/12 traces 正确，约束方向一致但 discriminative power 低"
    result_rationale: >
      Case studies 预期展示三种模式:
      (1) Override success: 在 Goldilocks zone 问题上，traces 有足够多样性，部分 trace 的约束提供了
          SC vote 无法捕捉的 discriminative 信息，MAX-SAT 正确翻转。
      (2) Confirmation bias: both_wrong 问题上，约束语义上有效(syntactically correct FOL)但推理方向
          与模型错误一致——约束"正确反映了错误推理"。这解释了为什么 ~92% constraints 是 discriminative
          但 SICA 仍无法突破: discrimination 方向与模型 bias 对齐。
      (3) Trivially satisfied: ~43% 约束被所有候选答案满足，提供零 discriminative value。
    tables: ["Appendix: Qualitative case studies"]
    figures_description: ["F4 stacked bar 中的 illustrative examples"]
    analysis: >
      定性证据支持 confirmation bias 机制。约束质量本身不差(语义有效率 ~88%)，
      但"正确提取了错误推理"是比"提取质量差"更根本的问题。

  - name: overhead_analysis
    plan_id: exp-009
    description: "Wall-time breakdown: generation, extraction, MaxSAT solving。"
    expected_results:
      n: 804
      mean_total_wall_s: 61.6
      trace_gen_pct: 51.3
      extract_pct: 47.0
      maxsat_pct: 0.005
      sica_overhead_pct: 48.7
    result_rationale: >
      Extraction 占总时间 47%，几乎与 trace generation 持平(51%)。MAX-SAT solving 本身极快(0.005%)。
      SICA 的主要 overhead 在 LLM extraction call (每 trace 一次 extraction prompt)，不在 solver。
      这回答 reviewer concern "is the overhead worth it": ~2x wall-time for 0-5pp gain，
      在 best tier 下 Goldilocks zone 可获 4.9pp 但大多数条件 0 gain。
      Practical recommendation: C0+SC 诊断可在 overhead 前判断是否值得运行 SICA。
    tables: ["Appendix: Overhead analysis"]
    figures_description: []
    analysis: >
      Overhead 主要来自 extraction (LLM calls)，非 solver。C0+SC 前置诊断可避免无效 overhead。

  - name: sica_llama_8b
    plan_id: exp-011
    description: "LLaMA-3.1-8B-Instruct on D012 60 questions。Cross-family validation。"
    expected_results:
      n: 60
      sica_accuracy: 0.6667
      sc_accuracy: 0.60
      delta_pp: 6.67
      multi_candidate_rate: 0.6167
      mcnemar_p: 0.2188
      folio_delta_pp: 10.0
      pw_delta_pp: 3.33
      truncated_traces: 44
    result_rationale: >
      LLaMA-8B SC=60% (Goldilocks 上界), C0=61.7% (高 diversity)。
      delta=+6.67pp 是所有条件中最大的 point estimate，虽然 n=60 导致 p=0.22 不显著。
      这支持 Goldilocks zone 假说: SC 在 sweet spot 附近 + 高 C0 → 最大潜在 gain。
      但 n 太小无法达到 significance。Truncated traces (44/720) 是 LLaMA 的 context limit 问题，
      可能影响 constraint quality 但方向不确定。
      LLaMA 作为第三个 model family (Qwen/Mistral/LLaMA) 确认 cross-family generalizability。
    tables: ["T1-Main-Results (LLaMA-8B row)"]
    figures_description: ["F2 scatter: LLaMA D012 点在 Goldilocks zone 右缘"]
    analysis: >
      最大 point estimate (+6.67pp) 但 underpowered (n=60)。作为 directional evidence 支持 Goldilocks hypothesis。
      Cross-family validation 消除 "Qwen-specific" attack。

  - name: gsm8k_pilot_14b
    plan_id: exp-012
    description: "Qwen2.5-14B on GSM8K 30 questions (K=12)。Cross-domain test。"
    expected_results:
      n: 30
      sica_accuracy: 0.9667
      sc_accuracy: 0.9667
      delta_pp: 0
      multi_candidate_rate: 0.133
      extraction_success_rate: 0.147
    result_rationale: >
      GSM8K 是 open-answer math domain。Qwen-14B 在 GSM8K 准确率极高(96.7%) → C0=13.3%。
      更关键的是 extraction_success_rate 仅 14.7% → 数学推理链无法有效转化为 FOL 约束。
      这是 Type B (domain formalizability) 的变体: 数学推理的约束不是 NLI 式的命题逻辑，
      而是算术操作序列，当前 FOL extraction prompt 无法捕捉。
      双重失败 (low C0 + low extraction) → delta=0 是预期结果。
    tables: ["T1-Main-Results (GSM8K row)", "Appendix: Domain analysis"]
    figures_description: []
    analysis: >
      Math domain 的 formalizability barrier。即使有 diversity (13.3% C0)，extraction 失败率 85% →
      constraints 太少无法 aggregate。不同于 NLI 的 confirmation bias，这里是 extraction 本身失败。

  - name: constraint_ablation
    plan_id: exp-013
    description: "SICA-MaxSAT vs SICA-count-only vs SICA-random-weight。CPU-only on exp-001 data。"
    expected_results:
      maxsat_accuracy: 0.7649
      count_only_accuracy: 0.7662
      random_weight_accuracy: 0.7587
      sc_baseline_accuracy: 0.7624
      agreement_maxsat_vs_countonly: "803/804"
    result_rationale: >
      MaxSAT 与 count-only 仅差 1/804 问题(agreement 99.9%)。这是 independence bottleneck 的 mechanism evidence:
      当 traces 高度相关时，约束间的逻辑关系(satisfiability structure)退化为简单计数。
      MaxSAT solver 试图找最优 satisfiable assignment，但当 constraints 都指向同一方向时，
      satisfiability optimization ≡ counting。SAT 解算的理论优势被 trace non-independence 完全消解。
      random-weight 稍差(760.7 vs 764.9)说明 constraint 本身有一定信号(非纯随机)，但信号极弱。
    tables: ["T1 footnote or Appendix: Aggregation mechanism ablation"]
    figures_description: []
    analysis: >
      关键 mechanism insight: MaxSAT ≈ count-only 证明在高相关 trace 下，symbolic aggregation 退化为 voting。
      这不是 MaxSAT 的设计缺陷，而是输入(correlated constraints)的根本限制。

  - name: sica_deepseek_r1_llama_8b
    plan_id: exp-014
    description: "DeepSeek-R1-Distill-Qwen-7B on D012 60 questions。Reasoning model negative control。"
    expected_results:
      n: 60
      sica_accuracy: 0.6833
      sc_accuracy: 0.7167
      delta_pp: -3.33
      multi_candidate_rate: 0.583
      truncated_traces: 72
      mcnemar_p: 0.4795
    result_rationale: >
      DeepSeek-R1 是 distilled reasoning model。C0=58.3% 看似高(与 LLaMA 相当)，但 delta=-3.33pp。
      原因: (1) 72/720=10% traces truncated → constraint 质量受损；
      (2) reasoning model 的 extended thinking 产生更多 step-by-step 约束，
      这些约束在 wrong cases 更 decisively wrong (confirmation bias 更强)。
      与 QwQ-32B (C0≈3%, SICA≡SC) 不同，R1-distill 有 diversity 但 reasoning chain 的
      structured errors 导致约束系统性偏向模型自身 bias。
      这进一步支持 independence bottleneck: 即使 diversity 存在，same-model reasoning bias 仍主导。
    tables: ["T1-Main-Results (DeepSeek-R1 row)"]
    figures_description: ["F2 scatter: R1 在 mid-SC、mid-Eff-K 但 negative delta"]
    analysis: >
      Reasoning model 的 distilled 版本。与 QwQ 形成对比: QwQ 无 diversity (C0≈3%)，R1 有 diversity (C0=58%)
      但 delta 仍为负。证明 diversity alone 不足——还需 constraint quality (SC 条件)。

  - name: logic_lm_baseline
    plan_id: exp-015
    description: "Logic-LM × K + majority vote baseline on FOLIO。CPU-only reanalysis。"
    expected_results:
      logic_lm_k12_accuracy: 0.755
      sc_accuracy: 0.7549
      sica_accuracy: 0.7451
      logic_lm_vs_sc_delta_pp: 0.0
      logic_lm_vs_sica_delta_pp: 1.0
      agreement_with_sc: "198/204"
    result_rationale: >
      Logic-LM 风格: 对每条 trace 独立做 FOL extraction + Z3 verification，然后 majority vote。
      与 SICA 的关键区别: Logic-LM 不做 cross-trace constraint aggregation，仅做 per-trace verification。
      预测 Logic-LM ≈ SC (±0.5pp):
      (1) 单 trace verification 将 "model answer + FOL constraints" 视为一致性检查，
          但 confirmation bias 导致 constraints 几乎总是与 model answer 一致 → verification 几乎不翻转任何答案；
      (2) 即使偶尔翻转，翻转方向与 SC 误差方向无系统关系 → 期望值为零；
      (3) majority vote 后与 SC 无差异。
      这证明 SICA 的跨 trace 聚合(MAX-SAT)在理论上有价值(至少提供 tiebreaking)，
      但 Logic-LM 的单 trace 验证连 tiebreaking 都无法提供。
    tables: ["Appendix: Baseline comparison"]
    figures_description: []
    analysis: >
      Logic-LM ≈ SC 证明 per-trace FOL verification 在 same-model 设置下无增量价值。
      SICA 的 cross-trace aggregation 至少在 tie 时有 80% accuracy (exp-003)，Logic-LM 连这都没有。

  - name: weighted_sc_baseline
    plan_id: exp-016
    description: "Weighted SC (length/constraint-count weighting) baseline。CPU-only on exp-001 data。"
    expected_results:
      sc_uniform_accuracy: 0.7624
      inv_length_accuracy: 0.7674
      length_weighted_accuracy: 0.7525
      constraint_count_accuracy: 0.7525
      all_nonsignificant: true
      best_p_value: 0.066
    result_rationale: >
      四种加权方案均与 SC 无显著差异:
      (1) inverse-length 最好(+0.5pp, p=0.453): 短 trace 略微更准确，但信号太弱；
      (2) length-weighted 和 constraint-count 均为 -1.0pp: 长 trace 和多约束 trace 不代表更高质量，
          反而可能对应更复杂(更难)的推理路径；
      (3) 所有 p>0.05，没有任何加权方案能系统性改进 SC。
      这回应 reviewer concern "weighted SC 是否是更简单的替代方案": 不是。
      Weighting 假设 trace quality 可从 trace-level features 预测，但 independence bottleneck 意味着
      所有 traces 共享相同 bias → weighting 无法区分 "好的偏差" 和 "坏的偏差"。
    tables: ["Appendix: Weighted SC comparison"]
    figures_description: []
    analysis: >
      Weighted SC 全部失败。Trace-level reweighting 无法突破 independence bottleneck，
      因为 bias 是 model-level 的，不是 trace-level 的。SICA 的优势(tiebreaking)也非 weighting 可替代。

  - name: sica_strategyqa_14b
    plan_id: exp-017
    description: "Qwen2.5-14B on StrategyQA 60 questions (K=12)。Commonsense reasoning domain。"
    expected_results:
      n: 60
      sica_accuracy: 0.5667
      sc_accuracy: 0.5333
      delta_pp: 3.33
      multi_candidate_rate: 0.10
      extraction_rate_trace: 0.704
      bootstrap_p: 0.1346
      discordant_sica_wins: 2
      discordant_sc_wins: 0
    result_rationale: >
      StrategyQA 是 commonsense binary QA。C0=10% 极低 → 大多数问题 unanimous，SICA≡SC 在 90% 问题上。
      delta=+3.33pp(2/60 问题翻转)方向正确但 n.s.。
      C0 低的原因: commonsense reasoning 的 implicit chain 难以产生 answer diversity——
      模型要么"知道"答案(unanimous correct)要么系统性错误(unanimous wrong)。
      trace extraction rate 仅 70.4% → implicit reasoning 难以形式化为 FOL，
      这是 Type B (formalizability) 在 commonsense domain 的表现。
      尽管 delta 方向为正，bootstrap CI 包含 0 → 无法声称 SICA 在此 domain 有效。
    tables: ["T1-Main-Results (StrategyQA row)"]
    figures_description: ["F2 scatter: StrategyQA 点在 low-Eff-K, mid-SC"]
    analysis: >
      Commonsense domain 同时受 Type B (低 formalizability) 和 low C0 制约。
      +3.33pp 方向正确但不显著，纳入 "suggestive" 范畴。

  - name: sica_arc_challenge_14b
    plan_id: exp-018
    description: "Qwen2.5-14B on ARC-Challenge 60 questions (K=12)。Science reasoning 4-choice。"
    expected_results:
      n: 60
      sica_accuracy: 0.95
      sc_accuracy: 0.9667
      delta_pp: -1.67
      multi_candidate_rate: 0.05
      extraction_rate: 1.0
      discordant_sica_wins: 0
      discordant_sc_wins: 1
    result_rationale: >
      ARC-Challenge SC=96.7% → extreme Type A。C0=5% → 仅 3/60 问题有多答案候选。
      Qwen-14B 对 ARC 太强，traces 几乎完全一致。
      delta=-1.67pp: 在极少数 multi-candidate 问题上 SICA 反而选错(1 个 discordant case)。
      4-choice format 理论上应增加 diversity，但模型能力过强抵消了 format 效应。
      这是 Type A 的最极端案例: C0=5% + SC=97% → SICA 无空间可改善。
    tables: ["T1-Main-Results (ARC row)"]
    figures_description: ["F2 scatter: ARC 在 extreme top-left corner"]
    analysis: >
      SC=97% 的极端 Type A。4-choice format 未增加有效 diversity。
      证明 high-accuracy conditions 下 SICA 无增量价值。

  - name: constraint_quality_correlation
    plan_id: exp-019
    description: "Constraint quality (precision/bias direction) vs C0 vs delta 的跨条件 correlation analysis。CPU-only。"
    expected_results:
      n_conditions: 12
      correlation_sc_vs_constraint_agreement: 0.85
      correlation_effk_vs_delta_given_goldilocks: 0.62
      high_sc_constraint_agreement_pct: 82
      mid_sc_constraint_agreement_pct: 65
      low_sc_constraint_agreement_pct: 48
      goldilocks_constraint_precision: 0.71
      type_a_constraint_precision: 0.89
      type_c_constraint_precision: 0.43
      inverse_c0_quality_confirmed: true
    result_rationale: >
      跨条件分析预期揭示:
      (1) SC 与 constraint-model agreement 高度正相关 (r≈0.85): 模型越准 → 约束越与模型一致
          → confirmation bias 越强 → SICA 越无法翻转。
      (2) Type A (SC>60%): constraint precision 高(89%)但 agreement 也高(82%) → discriminative
          but in the same direction as model → zero gain。
      (3) Type C (SC<45%): constraint precision 低(43%) → 约束本身是噪声 → 有害。
      (4) Goldilocks (45-60% SC): constraint precision 中等(71%)，agreement 中等(65%) →
          存在足够的 independent correct constraints 可以 override → positive delta。
      这完成了 Dual Bottleneck 的 mechanism decomposition:
      Independence (Eff-K) 决定是否有多样视角，Quality (SC→constraint precision) 决定视角是否正确。
    tables: ["T4-Extraction-Error-Taxonomy (extended)"]
    figures_description:
      - "F4 extended: constraint agreement % vs SC% scatter，showing linear trend"
      - "F2 color-coded by constraint precision: 验证 Goldilocks zone 的 mechanism"
    analysis: >
      Mechanism decomposition 的最终证据。将 Dual Bottleneck 从 correlational (Eff-K × SC predicts delta)
      提升到 mechanistic (SC determines constraint quality direction，Eff-K determines diversity)。
      Confirmation bias 是 Type A 失败的 root cause，noise 是 Type C 失败的 root cause。

  # ===== RUNNING 实验（best-tier 预测）=====

  - name: mistral_k_sensitivity
    plan_id: exp-051
    description: "Mistral-7B K sensitivity on FOLIO-204 (K=4,8,12,16,20)。Best tier 核心: inverted-U。"
    expected_results:
      n: 204
      seed: 42
      K4_sc: 0.549
      K4_sica: 0.544
      K4_delta_pp: -0.5
      K4_eff_k: 1.60
      K4_p: 0.82
      K8_sc: 0.544
      K8_sica: 0.564
      K8_delta_pp: 2.0
      K8_eff_k: 1.78
      K8_p: 0.14
      K12_sc: 0.544
      K12_sica: 0.593
      K12_delta_pp: 4.9
      K12_eff_k: 1.85
      K12_p: 0.013
      K16_sc: 0.544
      K16_sica: 0.569
      K16_delta_pp: 2.5
      K16_eff_k: 1.88
      K16_p: 0.09
      K20_sc: 0.549
      K20_sica: 0.559
      K20_delta_pp: 1.0
      K20_eff_k: 1.90
      K20_p: 0.35
      inverted_u_visual: "peak K=12 (4.9pp), K=4 gap 5.4pp, K=20 gap 3.9pp, 两侧单调递减"
    result_rationale: >
      Inverted-U 的 mechanism:
      - K=4 (Eff-K=1.6): 刚过 1.5 阈值但仅 4 条 trace → 约束太少，MAX-SAT 无足够信息 override SC。
        少量约束的随机性导致偶尔错误翻转 → 期望值略负。
      - K=8 (Eff-K=1.78): 约束量开始充足(~8×39=312 raw, ~160 unique)，部分问题的 discriminative
        信息足以翻转。但 Eff-K 仍有限 → 仅能翻转最"容易"的 discordant cases → +2.0pp。
      - K=12 (Eff-K=1.85): Sweet spot。约束量充足(~470 raw, ~240 unique) 且 Eff-K≈1.85 提供
        足够独立视角。正好覆盖 10-12 个 discordant cases (12 wins, 2 losses) → +4.9pp。
      - K=16 (Eff-K=1.88): Eff-K 仅比 K=12 增加 0.03，但额外 4 条 trace 引入 ~120 条冗余约束。
        冗余约束倾向于与模型多数意见一致(confirmation bias) → 稀释 discriminative signal → +2.5pp。
      - K=20 (Eff-K=1.90): 进一步冗余。Eff-K 几乎不增长(1.90 vs 1.88) 但 noise 约束持续增加。
        大量一致性约束使 MAX-SAT 更倾向于多数意见(本质上退化为 weighted SC) → +1.0pp。
      两侧与 peak 差值: K=4 差 5.4pp ≥ 2pp ✓, K=20 差 3.9pp ≥ 2pp ✓。
      全程单调: -0.5 → +2.0 → +4.9 → +2.5 → +1.0 ✓。无 non-monotonic outlier ✓。
    tables: ["T5-K-Sensitivity (Mistral panel, primary)"]
    figures_description:
      - "F3 主 panel: K vs Δpp 曲线 (Mistral, seed=42)。清晰 inverted-U，peak at K=12。
         左侧: K=4→8→12 monotonic rise。右侧: K=12→16→20 monotonic decline。
         Secondary y-axis: Eff-K vs K (log-like curve showing diminishing returns)。
         Annotations: Eff-K 值标注在每个点旁。"
      - "F3 inset: Qwen K sensitivity 对比(平线) — 同一 figure 两个 panel 对比两种 regime"
    analysis: >
      Best tier 的核心 ablation contribution。Inverted-U 证明:
      (1) K 太少 → Eff-K 不足 → SICA 无法工作；
      (2) K 太多 → Eff-K 饱和但 confirmation bias 约束淹没 discriminative signal → SICA 退化。
      K=12 是该条件下的 sweet spot，由 Eff-K 增长曲线的 knee point 和 noise accumulation 的交叉决定。
      这独立于 T sensitivity 提供 ablation evidence for the independence bottleneck。

  - name: multitemp_mistral_folio
    plan_id: exp-055
    description: "Multi-temperature ensemble (e.g. T={0.5,0.7,0.9} × 4 traces each) Mistral FOLIO-204。"
    expected_results:
      n: 204
      sica_accuracy: 0.549
      sc_accuracy: 0.544
      delta_pp: 0.5
      mcnemar_p: 0.65
      significant: false
      multi_candidate_rate: 0.78
      extraction_rate: 0.96
    result_rationale: >
      Multi-temp 的设计意图是通过混合温度增加 trace diversity → 降低 κ → 提高 Eff-K。
      预测失败的原因:
      (1) Same-model bias 不随温度改变。T=0.5 和 T=0.9 的 traces 虽然 surface diversity 不同，
          但 reasoning direction 仍被模型 weights 主导 → κ 仅轻微下降(估计 κ≈0.45 vs single-temp κ=0.50)。
      (2) 混合温度引入 quality heterogeneity: T=0.5 traces 更准但更一致，T=0.9 traces 更 diverse 但更不准。
          这些约束混合后相互抵消 → 净效果接近零。
      (3) early n=28 已显示 delta=0.00pp，完整 n=204 预期在 [-0.5, +0.5]pp 范围。
      这是第 9 种修复失败，完成 remediation evidence: diversity alone (without quality improvement)
      无法打破 bottleneck。Multi-temp 增加的是 surface diversity (token-level)，不是 reasoning diversity (logic-level)。
    tables: ["T1 footnote or Appendix: Multi-temp remediation"]
    figures_description: []
    analysis: >
      第 9 种修复的最终确认。Diversity-focused intervention 失败证明 independence bottleneck 不是简单的
      "采样不够多样"问题，而是 same-model reasoning 的结构性限制。
      温度改变 token-level randomness 但不改变 reasoning-level bias。

  - name: mistral_folio204_t03
    plan_id: exp-057
    description: "Mistral-7B FOLIO-204 at T=0.3。T sensitivity curve 的低温端。"
    expected_results:
      n: 204
      sc_accuracy: 0.554
      sica_accuracy: 0.559
      delta_pp: 0.5
      mcnemar_p: 0.70
      significant: false
      multi_candidate_rate: 0.55
      extraction_rate: 0.975
      estimated_kappa: 0.58
      estimated_eff_k: 1.62
    result_rationale: >
      T=0.3 → traces 更 deterministic → κ 增高(估计 κ≈0.58 vs T=0.7 的 κ=0.50)。
      更高 κ → 更低 Eff-K (1.62 vs 1.85) → 独立视角更少 → SICA 能力下降。
      C0 也下降(55% vs T=0.7 的 81%) → 更多 unanimous 问题 → 更少可翻转空间。
      但 constraint extraction quality 可能略高(更确定性的推理 → 更一致的 FOL) →
      少量翻转可能正确 → delta 略正(+0.5pp) 但远不显著。
      T=0.3 的 0.5pp vs T=0.7 的 4.9pp → 差 4.4pp。低温下 independence 严重不足，
      即使 constraint quality 更好也无法弥补。
    tables: ["Appendix: T sensitivity (T=0.3 column)"]
    figures_description: ["F_appendix: T vs Δ peaked curve 的左侧数据点"]
    analysis: >
      T=0.3 验证 T sensitivity curve 左半段: 低温 → 低 diversity → 低 Eff-K → 低 delta。
      与 T=0.7 (+4.9pp) 形成 4.4pp 差距，证明温度对 independence 的直接影响。

  - name: mistral_folio204_t05
    plan_id: exp-058
    description: "Mistral-7B FOLIO-204 at T=0.5。T sensitivity curve 中间点。"
    expected_results:
      n: 204
      sc_accuracy: 0.549
      sica_accuracy: 0.569
      delta_pp: 2.0
      mcnemar_p: 0.12
      significant: false
      multi_candidate_rate: 0.68
      extraction_rate: 0.97
      estimated_kappa: 0.53
      estimated_eff_k: 1.73
    result_rationale: >
      T=0.5 是 T=0.3 和 T=0.7 的中间点。κ≈0.53 (介于 0.58 和 0.50 之间)，Eff-K≈1.73。
      C0≈68% (介于 55% 和 81%)。
      delta=+2.0pp: 有足够 diversity 产生一些翻转(~6 discordant SICA wins, ~2 losses)
      但 Eff-K 仍低于 K=12/T=0.7 的 1.85 → 翻转数量不足以达到 significance。
      这个中间值完美填充 T sensitivity curve:
      T=0.3(+0.5pp) → T=0.5(+2.0pp) → T=0.7(+4.9pp) → T=1.0(+0.5pp)
      形成清晰 peaked curve，peak at T=0.7。
      T=0.5 到 T=0.7 的跳升(+2.0pp → +4.9pp)说明 independence threshold effect:
      Eff-K 从 1.73 到 1.85 的小幅增长导致 delta 的 非线性跳升 → threshold 效应。
    tables: ["Appendix: T sensitivity (T=0.5 column)"]
    figures_description: ["F_appendix: T vs Δ peaked curve 的中间数据点，showing threshold-like jump from T=0.5 to T=0.7"]
    analysis: >
      T=0.5 填充 T sensitivity curve，揭示 T=0.5→0.7 的 threshold-like jump (+2.0→+4.9pp)。
      这个非线性跳升暗示 Eff-K 存在阈值效应: 在 ~1.75-1.85 区间 SICA 从"偶尔有效"变为"显著有效"。

  - name: 14b_pw600_16639
    plan_id: exp-039
    description: "Qwen2.5-14B on ProofWriter-D5-600 with max_tokens=16639 (larger context)。"
    expected_results:
      n: 600
      sc_accuracy: 0.752
      sica_accuracy: 0.755
      delta_pp: 0.3
      mcnemar_p: 0.80
      significant: false
      extraction_rate: 0.99
      contradiction_rate: 0.02
    result_rationale: >
      与 exp-001 (sica_expanded_14b) PW-600 结果一致: Qwen-14B 在 PW-600 SC≈75%，Type A regime。
      更大 context window 可能略微提高 extraction rate (0.99 vs 0.89) 和减少 truncation，
      但不改变 fundamental dynamics: κ≈0.82 → Eff-K≈1.20 → 远低于 1.5 阈值。
      delta≈+0.3pp 与 exp-001 一致。这验证了结果的 robustness 不受 context length 影响。
    tables: ["T1-Main-Results (Qwen-14B PW-600 row, updated)"]
    figures_description: []
    analysis: >
      Context length 增加未改变 Type A 结论。Eff-K 仍然太低。

  - name: qwen3_pw600_16639
    plan_id: exp-040
    description: "Qwen3-14B (non-thinking) on ProofWriter-D5-600 with max_tokens=16639。"
    expected_results:
      n: 600
      sc_accuracy: 0.775
      sica_accuracy: 0.773
      delta_pp: -0.2
      mcnemar_p: 0.85
      significant: false
      extraction_rate: 0.995
      contradiction_rate: 0.025
    result_rationale: >
      Qwen3-14B non-thinking 在 FOLIO-204 (exp-035) 上 SC=77.3%, delta=-0.49pp。
      PW-600 预期类似: SC≈77-78%，Type A regime。Qwen3 比 Qwen2.5-14B 略强(SC +2pp)，
      意味着 κ 可能更高 → Eff-K 更低 → delta 更不可能为正。
      这是 Qwen family scaling 的又一数据点: 模型更新(2.5→3) 提升 SC 但不改善 SICA 效果。
    tables: ["T1-Main-Results (Qwen3 PW-600 row)"]
    figures_description: ["F2 scatter: Qwen3 PW 在 Type A cluster"]
    analysis: >
      Qwen3 generational update 未改变 Type A 结论。SC 提升但 delta 不变/略负。

  - name: llama8b_pw600
    plan_id: exp-048
    description: "LLaMA-3.1-8B-Instruct on ProofWriter-D5-600。Goldilocks zone test at scale。"
    expected_results:
      n: 600
      sc_accuracy: 0.565
      sica_accuracy: 0.585
      delta_pp: 2.0
      mcnemar_p: 0.08
      significant: false
      multi_candidate_rate: 0.58
      extraction_rate: 0.86
      truncated_traces: 180
    result_rationale: >
      LLaMA-8B 在 D012 (n=60) 上 PW 部分 SC=60%, delta=+3.33pp。扩展到 PW-600 (n=600):
      SC 预期略降(~56-57%) 因为 PW-D5-600 含更多难题。这把 LLaMA PW 推入 Goldilocks zone 核心。
      delta=+2.0pp (vs D012 的 +3.33pp) 反映 regression to mean 但方向一致。
      n=600 提升 power → p≈0.08 接近但仍未达显著(effect size ~2pp 需 n>800 for α=0.05)。
      truncated traces (30%) 是 LLaMA 的 context length limitation，降低 constraint quality。
      这是 Goldilocks zone 在 large n 下的 directional confirmation: 正向趋势持续但 effect size
      不够大到在 n=600 达到 significance → "real but fragile" 叙事的更多 evidence。
    tables: ["T1-Main-Results (LLaMA PW-600 row)"]
    figures_description: ["F2 scatter: LLaMA PW 在 Goldilocks zone 内，方向正确"]
    analysis: >
      Goldilocks zone 在 PW domain 的 scaled test。+2.0pp 方向正确、p=0.08 borderline。
      支持效应存在但 fragile 的整体叙事。30% trace truncation 是 LLaMA-specific limitation。
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a178c160-779d-4fcb-8a22-be668146c97c",
  "isSidechain": false,
  "requestId": "req_011CbBEgEw2Y4rcdfjZkTCGC",
  "type": "assistant",
  "uuid": "42ce87b4-4172-4903-a2be-b60c46ca2ad0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3",
  "sessionId": "ce350913-1529-4773-bc92-65a3a830432f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WzYkXVMvS4oPU3f413eexN",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 28873,
      "cache_read_input_tokens": 11841,
      "output_tokens": 30308,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 28873,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 30308,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 28873,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 28873
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：Dual Bottleneck framing 完全成立：Eff-K+SC 作为跨条件预测器有效，K/T sensitivity 曲线 clean，所有 pending 实验结果与理论一致。Main conference 可争取。 核心假设：['exp-051 Mistral K sensitivity 呈现…",
  "leafUuid": "42ce87b4-4172-4903-a2be-b60c46ca2ad0",
  "sessionId": "ce350913-1529-4773-bc92-65a3a830432f"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Dual bottleneck framing validation across Mistral seeds and temperature sensitivity",
  "sessionId": "ce350913-1529-4773-bc92-65a3a830432f"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：Dual Bottleneck framing 完全成立：Eff-K+SC 作为跨条件预测器有效，K/T sensitivity 曲线 clean，所有 pending 实验结果与理论一致。Main conference 可争取。 核心假设：['exp-051 Mistral K sensitivity 呈现…",
  "leafUuid": "42ce87b4-4172-4903-a2be-b60c46ca2ad0",
  "sessionId": "ce350913-1529-4773-bc92-65a3a830432f"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Dual bottleneck framing validation across Mistral seeds and temperature sensitivity",
  "sessionId": "ce350913-1529-4773-bc92-65a3a830432f"
}
```

---
