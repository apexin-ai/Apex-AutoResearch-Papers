# Research conversation: [Director 指令] [Patch — 关键新结果] exp-021 Oracle FOLIO 完成，论文最重要的证据之一 **结果摘要**： | Method | Accuracy | Delta vs SC | McNemar p — Part 35 of 102

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction (July export snapshot)** · Conversation logs

[← Part 34](part-034.md) · [Transcript overview](../research-conversation-director-patch-exp-021-oracle-folio-method-accuracy-delta-vs-sc-mcnemar-p-copy-3.md) · [Part 36 →](part-036.md) · [Structured JSON](../../../sessions/cc/ccb8c980cc58c5332988.json)

## Round 383

### Tool result

_source line 8810 · 2026-05-20T09:35:48.062Z_

<details><summary>↩ Tool result · `toolu_01JZDuXZ67oQJE5dNbYfjXNr`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/paper_framing.md\", \"content\": \"# Paper Framing — symb_invariant_consensus\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main (ARR May 25)\\n- Deadline: May 25, 2026 (ARR submission)\\n\\n## D063 Direction: Entropy Decomposition + Quality Ladder — 目标 4.0\\n\\n**从 D060 \\\"Pure Analysis / negative result\\\" 升级为 \\\"Regime-Dependent Mechanism Analysis with Entropy Decomposition\\\"。** 用户决定冲 4.0。\\n\\n### Entropy Breakdown 验证结果 (2026-05-19 completed)\\n\\n**跨模型 entropy mechanism 一致性: 不成立。Selective SICA 非 universal 方案。**\\n\\n但 entropy decomposition 揭示了更有价值的 regime mechanism：\\n\\n| Experiment | Model | Dataset | High-E n | High-E Δpp | Low-E n | Low-E Δpp |\\n|-----------|-------|---------|----------|-----------|---------|----------|\\n| exp-033 s42 | Mistral-7B | FOLIO | 78 | **+12.8** | 126 | 0.0 |\\n| exp-052 s123 | Mistral-7B | FOLIO | 77 | **+9.1** | 127 | 0.0 |\\n| exp-053 s456 | Mistral-7B | FOLIO | 75 | -1.3 | 129 | 0.0 |\\n| exp-046 | Mistral-7B | PW-600 | 267 | -4.9 | 333 | -1.2 |\\n| exp-036 | Qwen2.5-14B | FOLIO | 37 | **-8.2** | 167 | -0.6 |\\n| exp-038 | Qwen2.5-14B | LogiQA | 23 | -4.3 | 177 | 0.0 |\\n| exp-035 | Qwen2.5-7B | FOLIO | 47 | -2.1 | 157 | 0.0 |\\n| exp-048 | LLaMA-8B | PW-600 | 76 | -3.9 | 104 | -1.9 |\\n\\n(注: SC/Δ 使用 pre-tiebreaking 值，entropy grouping 不受 tiebreaking 影响。D064 修正后 deltas 会略有变化但 pattern 不变。)\\n\\n**三个核心发现：**\\n1. **Low-entropy: SICA≈SC 跨模型一致** (8/8 experiments Δ≈0) → traces 一致时 constraints 无新信息\\n2. **High-entropy 方向因 regime 而异**：Goldilocks +12.8pp vs Type A -8.2pp vs Type C -4.9pp\\n3. **Mechanism 解释**：\\n   - Goldilocks (SC~55%, κ~0.46): 真实不确定性 → constraints 打破平局正确方向\\n   - Type A (SC>75%, κ>0.65): 偶发错误 → constraints 放大 confirmation bias\\n   - Type C (SC<40%, κ~0.20): 系统性错误 → constraints 是噪声\\n\\n### 调整后核心转变\\n\\n论文以 \\\"entropy decomposition 揭示 regime-dependent mechanism\\\" 为核心分析贡献（不是 universal diagnostic）：\\n- **Entropy decomposition 作为分析工具**：分离 SICA 作用点（high-entropy）vs 不作用点（low-entropy）\\n- **Regime mechanism 量化**：同样是 high-entropy 问题，direction depends on SC+κ → 完美支持 dual bottleneck\\n- **Abandoned**: Selective SICA 作为 universal practical contribution（只在 Goldilocks zone 有效）\\n- **Upgraded**: 核心图 = high-entropy Δ vs SC scatter（8 points, 3 regimes 清晰分离）\\n- **Quality Ladder** (D067: L1 NULL CONFIRMED)\\n  - L0: Self-extraction (Mistral→Mistral): 59.31%, Δ=+3.43pp ns\\n  - L1a: Qwen3-14B→Mistral traces: 60.29%, Δ=+4.41pp (+0.98pp vs self = 2题/204 = noise)\\n  - L1b: Qwen2.5-14B→Mistral traces: 58.33%, Δ=+2.45pp (-0.98pp vs self = 2题/204 = noise)\\n  - L3: Oracle 100% disc, Δ=+14.22pp p<0.001\\n  - **结论**: L1 ≈ L0 << L3。Bottleneck 在 traces（同源输入），不在 extractor（换模型无效）\\n  - **Paper contribution**: \\\"bottleneck is fundamental to extraction, not just model capability\\\" — 强化 structural limitation 论点\\n- **CJT/Eff-K 保留**：解释 why high-entropy behavior differs across regimes\\n\\nD060 要素全部保留：\\n- Condorcet independence 框架 → 理论基础\\n- 9 种修复全部失败 → structural limitation 证据\\n- 2/3 seeds positive trend but **0/3 significant** (D066: p=0.092/0.070/1.0) → Goldilocks zone 作为 directional trend, not confirmed effect\\n- K/T sensitivity non-monotonic → SC confound insight\\n- 用户指示: 投 May 25 不变，冲 4.0\\n\\n## Core Claims (5 条) — D060 纯 Analysis Framing\\n\\n### Analysis Claims (已验证)\\n\\n1. **Independence Bottleneck**: Self-consistency 隐含 Condorcet Jury Theorem 的独立性假设，但同模型采样的 traces 高度相关。Worker 验证的 κ 值：\\n   - Qwen-14B FOLIO: κ=0.744, Eff-K=1.31 (SC=75.49%, Δ=+0.25pp n.s.)\\n   - Qwen-14B LogiQA: κ=0.821, Eff-K=1.20 (SC=78.5%, Δ=+0.50pp n.s.)\\n   - Mistral-7B FOLIO s42 (exp-033): κ=0.501, Eff-K=1.84 (SC=55.88%, Δ=+3.43pp **p=0.092 ns**) ← primary seed [D064+D066]\\n   - Mistral-7B FOLIO s123: κ=0.491, Eff-K=1.88 (SC=54.41%, Δ=+2.94pp **p=0.070 ns**)\\n   - Mistral-7B FOLIO s456: κ=0.507, Eff-K=1.82 (SC=55.88%, Δ=0.00pp p=1.0 ns)\\n   - Mistral-7B PW-600 (exp-046): κ=0.210, Eff-K=3.63 (Δ=-2.83pp p=0.010, SC=39%)\\n   规律：跨模型对比清晰（Qwen Eff-K≈1.2-1.3 → 0 gain; Mistral Eff-K≈1.85-2.22 → variable gain）。但 Mistral seeds 内部，Eff-K 与 delta 非单调（exp-033 Eff-K 最低 1.85 却 delta 最高 +3.43pp）→ Eff-K 是跨模型必要条件，seed 内 variance 仍主导。exp-046 Eff-K 最高(3.63) 但 SC 太低(39%) 导致 delta 为负 → 需同时满足 sufficient Eff-K AND sufficient SC。\\n\\n2. **Oracle Gap Localizes Extraction Bottleneck**: Gold FOL + MAX-SAT = +14.22pp (p=2.0e-7)，自提取仅 +3.43pp (best seed, D064 corrected) = 24% utilization。聚合机制本身有效，瓶颈在自提取质量。Two-layer analysis:\\n   - **Constraint taxonomy**: 43% trivially_satisfied（被所有候选答案满足的约束，不排除任何答案）\\n   - **Discriminative filtering**: 仅 ~8% 约束在 MAX-SAT scoring 中完全 non-discriminative（移除后 0 gains）\\n   - **关键区分**: 43% 和 8% 度量不同。trivially_satisfied 约束在 MAX-SAT 中仍可有不同满足程度（partial vs full），所以不全是 non-discriminative。但即使 constraints 是 discriminative 的，它们的\\\"区分方向\\\"与模型自身偏差一致（confirmation bias）。both_wrong 组 score_range=29.4。九种修复全部失败。\\n\\n3. **Regime-Dependent Capability Trap**: SICA 有效性取决于提取模型的基线准确率，存在双边界：\\n   - Type A (SC ≥ ~60%): 确认偏差，constraints 镜像模型自身答案。**exp-034 vs exp-039 同配置 delta 翻转**: exp-034 Δ=+0.51pp (n=589), exp-039 Δ=-2.00pp (n=600)。SC baseline 方差 (3.38pp) >> SICA 效应 → Type A delta 是 trace sampling noise。SICA 比 SC 更稳定 (跨运行方差 0.87pp vs 3.38pp，仅 2 点，需更多 seed 验证)\\n   - Type C (SC ≤ ~40%): traces 主要错误，constraints 是噪声 (exp-046: Δ=-2.83pp, p=0.0095)\\n   - Goldilocks zone (~50-56% SC): 部分独立性 + 部分正确性 (exp-033: Δ=+3.43pp, p=0.092 ns; mean of 3 seeds: +2.12pp) ⚠️ D076 Reviewer: 0/3 seeds significant, 不应作为核心叙事支柱。作为 directional observation 保留，不做强 claim。\\n   - Type B: 领域不可形式化 (LogiQA: contradiction rate 0.8%)\\n\\n4. **C0+SC Two-Dimensional Diagnostic**: C0 (multi-candidate rate) + SC accuracy 形成零成本部署诊断。C0<5% → degenerate; high C0 + high SC → trap; high C0 + low SC → potential gains。\\n\\n### Remediation Evidence (D060: 全部失败 — 强化 analysis narrative)\\n\\n5. **Nine Remediation Attempts All Failed**: 原 6 种 + 3 种靶向修复全部无效，证明 independence bottleneck 是结构性的：\\n   - D059 三路 method improvement 全部失败：\\n     - Discriminative Filtering: 119/204 处理后 0 gains 1 loss，~92% 约束本身就是 discriminative，过滤是 near-no-op\\n     - T=1.0 (exp-054): delta 从 +3.43pp 崩塌到 0.00pp（D064 corrected），温度敏感性极端\\n     - Multi-Temp (exp-055): ✅ 完成，delta=+0.00pp (b=5,c=5 完美对称), SC=57.84%. 混合 T=0.3/0.7/1.2 各 4 traces 未改善 SICA。附带发现：multi-temp 提升 SC baseline (+3.4pp vs 单温度 54.41%)，说明混合温度对 majority voting 有帮助，但 SICA constraint extraction 无法利用这种 diversity → bottleneck 在 extraction 而非 trace diversity\\n   - 原 6 种：contrastive prompting, cross-model extraction, generational scaling, solver-guided refinement, consistency filtering, cross-trace UNSAT\\n   - 9 种修复涵盖 prompting / architecture / capability / verification / diversity / filtering 全维度，全部失败 → trap is fundamental\\n\\n## D070/D074 Update: Method-Level Interventions Also Fail — \\\"Fundamental Limitation\\\" Confirmed\\n\\n### Three Method Lines × Two Datasets = All Negative (D074)\\n\\nD070 从纯 analysis 升级为 analysis + method paper，但三条方法线全面失败（D074 确认），反而强化了原始 analysis 结论。\\n\\n**方法×数据集完整结果**：\\n| Method | FOLIO-204 | LogiQA-200 | Failure Mode |\\n|--------|-----------|------------|--------------|\\n| ICG (Independent Constraint Gen.) | Δ=-2.0pp (3-seed: -2.0/+1.5/-1.0, mean=-0.5pp±1.8pp, 噪声) | Δ=-0.5pp | Neutral — 独立约束质量≈trace-sourced约束 |\\n| Contrastive (Pro/Con Scoring) | Δ≈-16pp | Δ≈-7pp (interim) | Harmful — 26% degenerate scoring, pro/con 不平衡 |\\n| Debate (Proposer/Critic) | Δ=-18.6pp | Δ≈-28pp (interim) | Catastrophic — 7B 模型角色扮演严重退化推理 |\\n\\n**三种失败模式的分析价值**（论文 \\\"Why Methods Fail\\\" section）：\\n1. **ICG (neutral)**: 独立于 traces 生成的约束不比 trace-sourced 约束更好。说明 bottleneck 不仅是 \\\"约束来自 traces\\\"，而是模型的推理偏差从问题理解阶段就存在——独立约束和 trace-sourced 约束继承相同的 model bias。\\n2. **Contrastive (harmful)**: 强制 pro/con 评估引入 degenerate scoring（26% 问题无法有效区分）。7B 模型无法可靠生成平衡的对立约束——pro 约束系统性多于 con（94 pro vs 65 con），confirmation bias 从约束提取转移到了约束生成。\\n3. **Debate (catastrophic)**: Proposer/Critic/Defense 多角色链在 7B 模型上导致答案质量严重退化。辩论不仅未增加多样性，反而引入了角色扮演的额外认知负担。同模型辩论 = 同源性 + 角色扮演退化，双重损失。\\n\\n**Scale limitation caveat**: 所有方法测试在 7B 模型上。7B 模型生成 Z3 格式 FOL 约束的能力不足（ICG 多题 \\\"0/N constraints parsed\\\"）。14B+ 模型可能有不同结果——这既是 limitation 也是 future work 入口。\\n\\n### κ Generalization — Independence-Accuracy Trade-off (D075, CAPSTONE FINDING)\\n\\nexp-077 测量三种聚合方式在 Mistral-7B FOLIO-204 上的 κ 和 Eff-K：\\n| 聚合方式 | Fleiss' κ | Eff-K | 名义 K |\\n|----------|----------|-------|--------|\\n| Self-Consistency | 0.4384 | 2.02 | 10 |\\n| Diverse-Prompt | 0.4030 | 2.21 | 12 |\\n| LLM-Debate | 0.1549 | 4.44 | 12 |\\n\\n结合 exp-076 Debate Δ=-18.6pp 的准确率数据，揭示**同模型框架下的 fundamental independence-accuracy trade-off**：\\n- **SC/Diverse-Prompt**: κ~0.4，traces 高度相关但准确率正常。换 prompt 策略不改善独立性（Δκ=0.04）。\\n- **Debate**: κ=0.15，成功打破 trace 相关性（Eff-K 从 2.0 跃升到 4.4），但准确率崩溃 -18.6pp。低 κ 不代表\\\"更独立的推理\\\"——是 disagreement amplification（系统性噪声）。\\n- **Trade-off 本质**: 同一模型的推理能力是固定的。要么输出一致（高 κ, 正确但不独立），要么输出分歧（低 κ, 独立但不正确）。Condorcet Jury Theorem 要求 both independent AND accurate，同模型框架下无法同时满足。\\n\\n**论文叙事升级**: 从 \\\"methods fail\\\" → \\\"independence-accuracy trade-off is fundamental to same-model reasoning\\\"。突破瓶颈需要跨模型方案（不同模型天然更独立），Oracle 实验（gold FOL 来自外部知识源）已间接验证了这一点。\\n\\n### New Claim 6 (D070/D074)\\n\\n6. **Method-Level Interventions Cannot Break the Bottleneck**: 三种针对 independence bottleneck 不同环节的方法（ICG→循环依赖, Contrastive→confirmation bias, Debate→trace 同质性）在 2 个数据集上全部失败。加上之前 9 种 prompt-level 修复，共 12 种修复尝试全败。这证明 independence bottleneck 不是单一环节的问题，而是 same-model self-extraction 的根本性限制。\\n\\n### New Claim 7: Symbolic Confirmation Bias (D082 — CORE FINDING)\\n\\n7. **Symbolic Confirmation Bias**: LLM 从 CoT traces 提取的 FOL 约束系统性确认 trace 自身（可能错误的）答案，而非独立验证 ground truth。\\n   - SICA 判对题：gold constraint 78.1%，bias ratio = 0.28\\n   - SICA 判错题：错误 constraint 83.3%，bias ratio = **4.97×**\\n   - 97.6% SICA 错误与 SC 错误完全重合\\n   - SICA 翻盘的 12 例来自 minority trace diversity（43% gold support），不是 symbolic reasoning\\n   - **因果链**：模型推理→答案→从含答案 trace 提取 FOL→约束确认答案→聚合≈SC\\n   - **CEGIS 验证**：迭代精炼 R1 +3.43pp < 原始 SICA +4.9pp → 约束一致性不是瓶颈，偏向性才是\\n   - **Quality Ladder 验证**：L1 ≈ L0 << L3 → bottleneck 在 traces（同源输入），不在 extractor\\n\\n### New Claim 8: Process-κ (D082 — NEW METRIC)\\n\\n8. **Process-Level Independence (Process-κ)**: answer-κ 低估真实独立性瓶颈。CoT 推理过程相似性远高于答案一致性。\\n   - Mistral-7B FOLIO-204：CoT cosine similarity **0.69** >> answer-κ **0.41**\\n   - 两者几乎无相关性：r = -0.06, p = 0.36\\n   - 仅 **9.3%** trace 对是\\\"殊途同归\\\"（同答案不同路径）\\n   - answer-κ 是 true independence bottleneck 的 lower bound\\n   - 适用于所有 LLM trace aggregation 方法，不限于 SICA\\n\\n## D082/D085: Comprehensive Method Exhaustion — 25+ ALL Fail\\n\\nD080 启动全方向并行探索（Wave 1-3），在 D074 的 12 种修复基础上又测试 13+ 新干预：\\n\\n| 方法 | 类型 | 结果 | 关键数据 |\\n|------|------|------|----------|\\n| PROVE 代码验证 | paradigm shift | ❌ | Code gen 15.2%, accuracy=random |\\n| CEGIS 迭代精炼 | multi-round | ❌ | R1 +3.43pp < SICA +4.9pp |\\n| DeepConf 置信度 | filtering | ❌ | logprob 与正确性零相关 |\\n| Cross-model SICA | cross-model | ❌ | Δ=-0.49pp despite lower κ |\\n| Problem Perturbation | input diversity | ❌ | κ 升至 0.696 (反效果) |\\n| MIN-UNSAT | solver objective | ❌ | 49.5% < SC 54.4% |\\n| κ-aware SC | voting rule | ❌ | 11/11 Δ=0 |\\n| Z3 Trace Filter | trace filtering | ❌ | negative |\\n| Bootstrapped Gold | iterative | ❌ | negative |\\n| Selective Abstention | diagnostic | ⚡ | AUROC=0.673, +4.4pp@80%cov |\\n\\n**D085 总结**: 9 prompt-level + 3 method-level + 13 新方向 = **25+ 干预全部 negative**。Independence bottleneck 在 same-model self-extraction 框架下无解，所有维度（diversity/architecture/capability/verification/filtering/voting/solver/paradigm）已穷尽。\\n\\n### Updated Headline Result (D085)\\n\\n\\\"Across 6+ models and 4 domains, symbolic consensus aggregation shows no statistically significant positive effect. 25+ interventions spanning prompt engineering, method-level redesign (ICG, Contrastive, Debate), solver modifications, cross-model aggregation, code-based verification, and iterative refinement all fail. We identify the root cause as Symbolic Confirmation Bias: self-extracted FOL constraints systematically confirm the trace's own answer (bias ratio 4.97× on incorrect problems), making symbolic aggregation equivalent to majority voting. Process-level analysis reveals reasoning paths are far more homogeneous than answers suggest (cosine similarity 0.69 vs answer-κ 0.41). The one method that breaks trace correlation (Debate: κ 0.44→0.15) does so at catastrophic accuracy cost (-18.6pp), revealing a fundamental independence-accuracy trade-off. Oracle constraints prove the aggregation mechanism works (+14.22pp, p<0.001), localizing the bottleneck entirely to self-extraction quality.\\\"\\n\\n### Updated Story Spine (D074)\\n\\n- **Problem**: [unchanged]\\n- **Theoretical lens**: [unchanged]\\n- **Systematic evaluation**: [unchanged]\\n- **Regime characterization**: [unchanged]\\n- **Remediation failures strengthen thesis (D085 FINAL)**: 9 prompt-level + 3 method-level + 13 new directions = **25+ interventions** across ALL dimensions (diversity/architecture/capability/verification/filtering/voting/solver/paradigm), all fail → bottleneck is fundamental and exhaustively proven\\n- **Method failure analysis**: Three methods targeting different bottleneck aspects show three distinct failure modes (neutral/harmful/catastrophic), revealing that the bottleneck operates at multiple levels simultaneously\\n- **Independence-accuracy trade-off (HERO FINDING, D075)**: Debate breaks trace correlation (κ 0.44→0.15, Eff-K 2.0→4.4) but accuracy collapses (-18.6pp/-23.0pp). Same-model traces can be independent OR accurate, not both.\\n- **NEW — Symbolic Confirmation Bias (CORE FINDING, D082)**: Root cause identified — self-extracted FOL constraints systematically confirm the trace's own answer (bias ratio 4.97× on incorrect problems). Causal chain: model reasons → answer → FOL extraction confirms answer → aggregation ≈ SC. This is WHY 25+ methods fail.\\n- **NEW — Process-κ (NEW METRIC, D082)**: CoT reasoning similarity (0.69) >> answer-κ (0.41), r=-0.06. Only 9.3% of trace pairs are \\\"convergent reasoning.\\\" answer-κ underestimates the true bottleneck. Novel metric applicable to all LLM trace aggregation.\\n- **Actionable contribution**: C0+SC diagnostic + κ-based Eff-K estimation = zero-cost deployment toolkit. κ analysis shows SC itself has a scaling ceiling (Eff-K ≈ 2 means K>12 traces yield diminishing returns).\\n- **Universal across architectures (D078)**: Three families: Mistral-7B κ=0.438, LLaMA-8B κ=0.412, Qwen2.5-7B κ=0.658, Qwen2.5-14B κ=0.738. Family effect (Δκ=0.22) >> scale effect (Δκ=0.08).\\n- **Headline (D085)**: Independence bottleneck is structural, universal across architectures, and rooted in Symbolic Confirmation Bias. 25+ interventions spanning all conceivable dimensions fail. Process-κ reveals reasoning homogeneity far exceeds answer-level agreement. The independence-accuracy trade-off constrains all same-model trace aggregation.\\n\\n## Core Insight (D060 Updated — Dual Bottleneck)\\n\\n**Dual Requirement Framework**: SICA 效应需要同时满足两个条件，缺一不可：\\n1. **Sufficient Independence** (Eff-K > threshold): traces 需要提供足够多的独立视角\\n2. **Sufficient Quality** (SC > ~50%): traces 需要有足够的正确率，否则约束是噪声\\n\\nCondorcet Jury Theorem 要求投票者独立且 p>0.5。同模型采样的 reasoning traces 严重违反独立性假设（Fleiss' κ = 0.21–0.82，Eff-K 仅 1.20–3.63），解释了为什么简单增加 K 或添加符号约束不能突破 SC 的天花板。\\n\\n实验数据完美支持 dual requirement（κ 使用统一脚本 compute_fleiss_kappa_unified.py，SC/Δpp 使用 registry 原始值）：\\n- **Qwen family**: κ=0.66-0.82, Eff-K≈1.20-1.46（独立性不足）→ all near-zero delta，无论 SC 多高\\n- **Mistral-7B FOLIO**: κ≈0.46, Eff-K≈2.0（中等独立性）+ SC≈55%（中等质量）→ +3.43pp best seed, mean +2.12pp (2/3 seeds positive, 1 null)\\n- **Mistral-7B PW-600**: κ=0.20, Eff-K=3.76（最高独立性）但 SC=39%（质量不足）→ -2.83pp\\n- 只有 Goldilocks zone（中等 Eff-K + 中等 SC）出现正向 delta\\n- **Dual bottleneck 直接验证 (exp-055)**：Multi-temp κ=0.427 Eff-K=2.11（比单温度 κ≈0.46 Eff-K≈2.0 更独立）但 delta=0.00pp → 提高 independence 不够，还需要 extraction quality\\n- **T sensitivity 孤立尖峰 (4/4 complete, D064 corrected)**：T=0.3(Δ=-1.47), T=0.5(Δ=-0.98), T=0.7(Δ=+3.43, κ=0.460, Eff-K=1.98), T=1.0(Δ=0.00, κ=0.394, Eff-K=2.25)。T=0.7 孤立尖峰更突出。T=0.7 SC=55.88%（最低）→ entropy 最高 → SICA 操作空间最大。温度效应与 SC 效应互为 confound，论文需讨论\\n- **Thinking mode κ=0.913, Eff-K=1.09 (exp-028b)**：近乎确定性。思维模式让 traces 更一致 → 独立性更差。\\\"更好的推理\\\"反而加剧 independence bottleneck。\\n\\n**κ 是 model-level 稳定属性**：统一处理后 Mistral 三 seed κ 收敛至 0.457-0.460（之前 0.41-0.50 差异是非标准 answer 处理的 artifact）。κ 跨 seed 几乎相同，但 delta 差异大（+3.43 vs +2.94 vs 0.00）→ seed-level constraint quality variance 主导，非 κ。\\n\\n完整 κ 表（⚠️ D062: κ 将用 raw answers 重算，当前 unified 值为临时值。Qwen 无变化，Mistral 条件将更新）：\\n| Exp | Model | κ(unified→raw pending) | Eff-K | SC%(registry) | Δpp(registry) |\\n|-----|-------|------------|-------|---------------|---------------|\\n| exp-028b | Qwen3-14B thinking | 0.913 | 1.09 | ~84% | ~0 |\\n| exp-038 | Qwen-14B LogiQA | 0.821 | 1.20 | 78.50 | -0.50 |\\n| exp-027 | Qwen3-14B | 0.773 | 1.26 | 84.31 | +0.49 |\\n| exp-036 | Qwen2.5-14B | 0.744 | 1.31 | 75.49 | +0.25 |\\n| exp-035 | Qwen2.5-7B | 0.658 | 1.46 | 76.47 | -0.49 |\\n| exp-049b | Mistral-7B LogiQA | 0.512 | 1.81 | 51.00 | +0.50 |\\n| exp-057 | Mistral-7B T=0.3 | 0.502 | 1.84 | 58.33 | -1.47 |\\n| exp-058 | Mistral-7B T=0.5 | 0.516 | 1.80 | 58.33 | -0.98 |\\n| exp-033 | Mistral-7B s42 | 0.460 | 1.98 | 55.88 | +3.43 |\\n| exp-052 | Mistral-7B s123 | 0.457 | 1.99 | 54.41 | +2.94 |\\n| exp-053 | Mistral-7B s456 | 0.457 | 1.99 | 55.88 | 0.00 |\\n| exp-055 | Mistral-7B multi-T | 0.427 | 2.11 | 57.84 | 0.00 |\\n| exp-054 | Mistral-7B T=1.0 | 0.394 | 2.25 | 55.39 | 0.00 |\\n| exp-046 | Mistral-7B PW-600 | 0.200 | 3.76 | 39.33 | -2.83 |\\n注：κ 基于 T/F/U 三类归一化，Mistral-7B 约 12-16% traces 被归一化（Qwen 100% valid）。Mistral SC/Δpp 已更新为 D064 tiebreaking 修正值；Qwen 不受影响。\\n\\nOracle control (+14.22pp) 证明 MAX-SAT 聚合机制本身有效，但自提取约束仅利用了 24% 的理论上限。Discriminative filtering 实验揭示关键机制：~92% 约束 ARE discriminative，但过滤掉 ~8% non-discriminative 约束后 delta 不变（0 gains）。问题不在约束缺乏判别力，而在于 discriminative constraints 的区分方向与模型偏差一致（confirmation bias）。\\n\\n**Remediation insight (D060)**: 9 种修复尝试全部失败，包括直接靶向 independence（multi-temp diversity, exp-055: Eff-K 从 2.0→2.11 但 delta 仍为 0）和 constraint quality（discriminative filtering）。这证明 bottleneck 不是简单的 diversity 或 quality 问题，而是 same-model self-extraction 的根本性限制。\\n\\n**Key evidence**:\\n- **Condorcet independence quantification (统一脚本, 公式: Eff-K=K/(1+(K-1)κ))**: Mistral-7B FOLIO κ≈0.46 (Eff-K≈2.0, 三 seed 高度稳定), Mistral-7B PW-600 κ=0.200 (Eff-K=3.76), Qwen2.5-14B FOLIO κ=0.744 (Eff-K=1.31), Qwen2.5-14B LogiQA κ=0.821 (Eff-K=1.20), Qwen3-14B κ=0.773 (Eff-K=1.26), Qwen2.5-7B κ=0.658 (Eff-K=1.46). 跨模型清晰: Qwen Eff-K≈1.2-1.5→0 gain, Mistral FOLIO Eff-K≈2.0→variable gain, Mistral PW Eff-K=3.76 but SC too low→negative. κ stable across seeds (0.457-0.460), delta varies → seed-level constraint quality dominates.\\n- **Oracle control (exp-031)**: Gold FOL + MAX-SAT = 89.71% vs SC 75.49% (+14.22pp, p=2.0e-7). Unknown-type +31.9pp.\\n- **Two-layer constraint analysis**: 43% trivially_satisfied (taxonomy: satisfied by ALL answers) vs ~8% non-discriminative (filtering: same MAX-SAT score). Difference: trivially_satisfied constraints can still have different satisfaction DEGREES. Removing the 8% yields 0 gains → problem is not quality but confirmation bias direction.\\n- **K sensitivity (non-monotonic peak at K=12, 5/5 complete, D064+D066)**: K=4(-1.47pp), K=8(-1.96pp), K=12(+3.43pp p=0.092 ns), K=16(+1.47pp), K=20(+1.96pp). Peak at K=12, drops at K=16 but partially recovers at K=20. NOT clean inverted-U. K=12 SC=55.88% (post-fix). SC-confound with T sensitivity still holds. SICA at K=4 vs K=12 differs by ~4.9pp despite similar SC — proves SICA extracts different information than SC.\\n- **SC-confound (cross-cutting insight)**: K=12 和 T=0.7 都是 SC 最低 (54.41%) 的配置 → SICA \\\"最佳超参\\\"可能反映 entropy/operating-window 效应而非 K 或 T 的因果贡献。论文需要讨论这个 confound，但也可以正面利用：SC level 是更基本的预测变量，K 和 T 通过影响 SC 来间接影响 SICA delta。\\n- **T sensitivity (isolated peak, 4/4 complete, D064 corrected)**: T=0.3(Δ=-1.47pp), T=0.5(Δ=-0.98pp), T=0.7(Δ=+3.43pp p=0.092 ns), T=1.0(Δ=0.00pp). NOT smooth inverted-U — T=0.7 is an isolated spike. T=0.7 has lowest SC (55.88%) → highest entropy → largest SICA operating window. Temperature and SC effects confounded. Strengthens fragility narrative.\\n- **Regime boundary**: Qwen-14B (SC=75.49%) Δ=-0.98pp vs Mistral-7B (SC=55.88%) Δ=+3.43pp p=0.092 ns\\n- **Type C failure (exp-046)**: Mistral PW-D5 SC=39.33%, Δ=-2.83pp, p=0.010, κ=0.210, Eff-K=3.63, contradiction rate 5.5%. Highest Eff-K yet worst delta → independence alone insufficient when SC too low.\\n- **Seed replication (D064+D066)**: 2/3 seeds positive but **0/3 significant** after tiebreaking correction: s42 Δ=+3.43pp p=0.092, s123 Δ=+2.94pp p=0.070, s456 Δ=0.00pp p=1.0. Mean +2.12pp. Only significant McNemar effects are NEGATIVE: exp-046 Δ=-2.83pp p=0.014, exp-039 Δ=-2.50pp p=0.011. Paper must frame as \\\"positive directional trend\\\" not \\\"significant positive effect\\\".\\n- **Nine remediation failures (ALL CONFIRMED)**: contrastive prompting, cross-model, generational scaling, solver-guided, consistency filtering, cross-trace UNSAT, discriminative filtering (0 gains), T=1.0 (delta collapse +3.43→0.00pp, D064 corrected), multi-temp (delta=+0.00pp, b=5 c=5). All 9 failed → trap is fundamental, bottleneck is structural.\\n- **Entropy decomposition (VERIFIED 2026-05-19)**: High-entropy proportion: Mistral FOLIO 38% (78/204) vs Qwen FOLIO 18% (37/204) vs Qwen LogiQA 12% (23/200). SICA on high-entropy: Mistral FOLIO s42 +12.8pp, s123 +9.1pp, s456 -1.3pp; Qwen FOLIO -8.2pp; all others negative. Low-entropy: SICA≈SC across all 8 experiments (Δ≈0). Entropy decomposition reveals regime-dependent mechanism, NOT universal diagnostic.\\n- **Confirmation bias quantification**: ⚠️ \\\"62.3%\\\" and \\\"28.6%\\\" confirmed NOT present in any .tex file — likely hallucinated in earlier draft. DO NOT USE. Replace with verified metrics from experiment outputs only.\\n\\n## Story Spine (D059 Updated)\\n\\n- **Problem**: LLMs' reasoning can be improved by sampling multiple chains-of-thought and aggregating via majority voting (self-consistency). Recent work proposes symbolic augmentation: extract formal constraints from traces and use SAT solvers for answer selection. But does symbolic aggregation actually outperform simple voting?\\n- **Theoretical lens**: Condorcet Jury Theorem requires voter independence. We quantify trace independence via Fleiss' κ and show Effective-K << nominal K. This explains the fundamental limitation of same-model trace aggregation.\\n- **Systematic evaluation**: SICA (MAX-SAT over FOL constraints) across 3 domains × 5 model families. Oracle control separates extraction vs aggregation failure. Discriminative filtering reveals ~92% constraints are discriminative, yet SICA gains are fragile — confirmation bias, not constraint quality, is the bottleneck.\\n- **Regime characterization**: Three failure modes (Type A/B/C) + narrow Goldilocks zone. C0+SC as deployment diagnostic.\\n- **Remediation failures strengthen thesis**: 9 targeted interventions (prompting, architecture, capability, verification, diversity, filtering) all fail to close the oracle gap, proving the bottleneck is fundamental to same-model self-extraction.\\n- **Headline result (D066 McNemar corrected)**: \\\"Across 6 models and 4 domains, symbolic consensus aggregation shows no statistically significant positive effect under corrected tiebreaking (best seed +3.43pp, p=0.092). The only significant effects are negative (PW-600: -2.83pp p=0.014, -2.50pp p=0.011). However, entropy decomposition reveals a striking regime-dependent pattern: SICA's entire effect concentrates on high-entropy questions, with +12.8pp in the Goldilocks zone but -2 to -8pp elsewhere. Oracle constraints prove the aggregation mechanism works (+14.22pp, p<0.001), localizing the bottleneck to extraction quality (24% utilization). Condorcet analysis (Eff-K=1.2-2.0 for nominal K=12) explains trace non-independence. Nine remediation strategies all fail, confirming the bottleneck is structural to same-model self-extraction.\\\"\\n\\n## Anticipated Reviewer Concerns & Defensive Experiments\\n\\n1. **\\\"Gains not statistically significant\\\"** → Correct: no positive effect reaches significance (best p=0.092). This IS the finding. Oracle p=2.0e-7 proves the mechanism works; the insignificance of self-extraction gains demonstrates the extraction bottleneck. Regime pattern (8 entropy conditions) provides systematic evidence beyond any single p-value.\\n2. **\\\"Only one positive result (exp-033)\\\"** → Seed replication: 2/3 positive (s42 +3.43pp, s123 +2.94pp), 1/3 null (s456 0.00pp). Mean +2.12pp. Effect IS real but fragile — the fragility itself IS the finding.\\n3. **\\\"Condorcet framework is trivial\\\"** → Fleiss' κ quantification is novel in SC/SICA context. Eff-K is actionable: tells practitioners how many truly independent traces they get.\\n4. **\\\"Multi-temp / filtering should work\\\"** → We tried both. Multi-temp (exp-055): negative. Disc. filtering: 0 gains. T=1.0: delta collapse. These failures STRENGTHEN the structural bottleneck thesis.\\n5. **\\\"Only Qwen models\\\"** → 5 families: Qwen-14B, Mistral-7B, LLaMA-8B, DeepSeek-R1-7B, QwQ-32B.\\n6. **\\\"Only logic domain\\\"** → FOLIO + ProofWriter + LogiQA + StrategyQA + ARC-Challenge. Type B (domain formalizability) is itself a finding.\\n7. **\\\"Oracle is unfair comparison\\\"** → Diagnostic tool, not competing method. Separates extraction from aggregation.\\n8. **\\\"MAX-SAT is over-engineering\\\"** → exp-013: MaxSAT ≈ count-only. This IS the independence bottleneck evidence.\\n9. **\\\"Self-extraction confound\\\"** → Oracle control resolves completely.\\n10. **\\\"Published methods achieve gains (DyLoS, Aristotle, FoVer)\\\"** → Different paradigm (external verifiers/trained extractors). We characterize same-model self-extraction.\\n11. **\\\"C0 is trivially derived\\\"** → Zero-cost early stopping. Practical value.\\n12. **\\\"Why not just use a reasoning model?\\\"** → QwQ-32B: C0<5%, SICA≡SC.\\n13. **\\\"Random tiebreak baseline\\\"** → exp-003: SICA tiebreak 80% vs random 50%.\\n14. **\\\"Method improvement is incremental\\\"** → Grounded in diagnosis (independence + taxonomy), not ad-hoc.\\n15. **\\\"Weighted SC is simpler\\\"** → exp-016 planned. Weighted SC doesn't address independence.\\n16. **\\\"Within-model ICL transition contradicts regime theory\\\"** → exp-050b (SC=57.79%, Δ=-3.52pp): ICL changes trace generation characteristics, not just SC level. Paper must distinguish \\\"same model, different prompt\\\" from \\\"same model, same prompt, different accuracy.\\\"\\n\\n## Working Title\\n**\\\"Beyond Self-Consistency: How Trace Independence Limits Symbolic Consensus in LLM Reasoning\\\"**\\n(Alternatives:\\n- \\\"The Independence Bottleneck: Why Self-Extracted Symbolic Constraints Cannot Beat Majority Voting\\\"\\n- \\\"Symbolic Consensus Under the Condorcet Lens: Independence, Extraction, and the Limits of Self-Aggregation\\\")\\n\\nNOTE (Dream D037): Title MUST be scoped to \\\"self-extracted constraints\\\" / \\\"SICA\\\". Published methods (DyLoS, Aristotle, FoVer) use different approaches.\\n\\n## Paper Structure (EMNLP 8pp + appendix)\\n\\n### Main Tables\\n- T1: Main Results — models × domains, SC% / SICA% / Δpp / p-value, regime boundary\\n- T2: Oracle Control — Gold-FOL+MAX-SAT vs SC vs SICA-self, causal separation\\n- T3: Independence Quantification — Fleiss' κ / Eff-K / trace agreement per model\\n- T4: Extraction Error Taxonomy — trivially_satisfied / discriminative / both_wrong rates\\n- T5: K Sensitivity — K=4/8/12/16/20, non-monotonic (peak K=12, K=20 recovers), SC confound\\n\\n### Main Tables (continued)\\n- T6: Method-Level Intervention Results — 3 methods × 2 datasets, SC% / Method% / Δpp, failure mode classification\\n- T7: κ Generalization — SC / Debate / Diverse-Prompt κ and Eff-K (from exp-077, pending)\\n\\n### Main Figures\\n- F1: Method Pipeline (SICA + oracle control design)\\n- F2: SC Accuracy vs SICA Δ scatter (hero figure, regime boundary)\\n- F3: K Sensitivity with diversity metrics (K vs Δ, K vs Eff-K)\\n- F4: Extraction error breakdown (stacked bar)\\n- F5: Method intervention failure modes (grouped bar: ICG/Contrastive/Debate × FOLIO/LogiQA)\\n\\n### Appendix\\n- K ablation details, temperature sensitivity, per-domain results, overhead analysis\\n- Entropy-conditioned analysis (continuous scatter + bin sensitivity)\\n- Six remediation strategy details\\n- Confirmation bias quantification\\n- Seed replication analysis\\n- QwQ-32B / DeepSeek-R1 negative control\\n\\n## Claim Risk Notes (D059)\\n- **Seed replication**: 0/3 significant after D066 correction (p=0.092, 0.070, 1.0). 2/3 positive trend, 1/3 null. Mean +2.12pp. Frame as \\\"directional trend, not significant effect\\\" — fragility IS the finding.\\n- **Method claims DEAD (D060)**: All three method improvements failed. Paper is pure analysis. 9 remediation failures are EVIDENCE, not limitation.\\n- **Condorcet novelty**: ✅ VERIFIED. arXiv:2409.00094 applies CJT to cross-model LLM ensembles (different angle). No prior work applies Fleiss' κ or Eff-K to within-model SC traces. Our framing is novel.\\n- **exp-050b complication**: ICL transition Δ=-3.52pp at SC=57.79% complicates simple \\\"SC determines SICA.\\\" Explain via trace generation characteristic change.\\n- **Variable naming inconsistency**: 56.4% cross-trace pairs share zero Z3 variables. Key mechanism evidence.\\n\\n## Required Citations (minimum 30 references)\\n\\n- **SC & extensions**: Wang et al. 2023 (SC), Chen et al. 2023 (USC), Loo et al. 2025 (SC scaling plateaus), Taubenfeld et al. 2025 (weighted SC), DiVeRSe (Li et al. 2023)\\n- **Neuro-symbolic reasoning**: DyLoS (EACL 2026), Aristotle (ACL 2025), FoVer (TACL 2025), LogicAgent (2025), Logic-LM (Pan et al. 2023), LINC (Olausson et al. 2023)\\n- **Condorcet/voting theory**: Condorcet 1785, Austen-Smith & Banks 1996, **arXiv:2409.00094 (Examining Independence in Ensemble Sentiment Analysis, Sept 2024)** — closest prior work, applies CJT to cross-model LLM ensembles, finds independence violation. Our novelty: within-model trace independence + Fleiss' κ quantification + Eff-K + connection to symbolic aggregation\\n- **Test-time compute**: Snell et al. 2025, DeepSeek-R1, Diversity-Aware Training\\n- **Verification & reranking**: ORM (Cobbe et al. 2021), PRM (Lightman et al. 2023), Math-Shepherd\\n- **Constraint satisfaction**: SATBench (EMNLP 2025), LLM Meets Constraint Propagation (IJCAI 2025)\\n- **Debate & multi-agent**: Liang et al. 2023, Du et al. 2023\\n\\n## Additional Reviewer Concerns (D070/D074 Methods)\\n\\n17. **\\\"Why not use a larger model for constraint generation?\\\"** → Valid. All methods tested at 7B scale. ICG constraint parsing failures + Debate role-play degradation may be scale-dependent. This is explicitly noted as limitation and future work. The contribution is diagnosing the bottleneck and showing it's not trivially fixable, not claiming no fix exists at any scale.\\n18. **\\\"Only tested one model (Mistral-7B) for methods\\\"** → Methods are interventions on the extraction pipeline, not the base model. Testing on the same model that showed the clearest Goldilocks signal (Mistral-7B FOLIO) is the strongest test — if methods can't improve the best-case scenario, they won't help elsewhere.\\n19. **\\\"ICG multi-seed shows 1/3 positive\\\"** → Magnitudes (-2.0, +1.5, -1.0) are within SC baseline noise (3.5pp cross-seed). Mean ≈-0.5pp, std=1.8pp. No statistical significance. Properly framed as \\\"noise-level, neither improving nor degrading.\\\"\\n20. **\\\"Debate working in other papers\\\"** → Multi-agent debate literature uses diverse models or much larger models. Same-model 7B debate is a different regime. Our finding is specifically about same-model self-extraction limitations.\\n\\n## Claim Scoping Rules\\n- n=60 conditions: \\\"suggestive/consistent with\\\" NOT \\\"confirming\\\"\\n- n≥200 conditions: can \\\"confirm\\\"\\n- Combined N>1,300: acceptable if breakdown clearly stated\\n- Method claims: must show statistically significant improvement OR clear directional improvement with analysis\\n- \\\"Independence bottleneck\\\" framing: systematic quantification + theoretical grounding\\n\", \"total_chars\": 31186, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d4f8bb98-c0e4-41f7-839b-c73143d1396a",
  "isSidechain": false,
  "promptId": "3f50ba00-7d30-45ec-b450-7010d531c858",
  "type": "user",
  "uuid": "77cf5a4e-6311-4f0d-90dd-2f1b5fa1f95c",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/paper_framing.md\\\", \\\"content\\\": \\\"# Paper Framing — symb_invariant_consensus\\\\n\\\\n## Target Venue\\\\n- Primary: EMNLP 2026 Main (ARR May 25)\\\\n- Deadline: May 25, 2026 (ARR submission)\\\\n\\\\n## D063 Direction: Entropy Decomposition + Quality Ladder — 目标 4.0\\\\n\\\\n**从 D060 \\\\\\\"Pure Analysis / negative result\\\\\\\" 升级为 \\\\\\\"Regime-Dependent Mechanism Analysis with Entropy Decomposition\\\\\\\"。** 用户决定冲 4.0。\\\\n\\\\n### Entropy Breakdown 验证结果 (2026-05-19 completed)\\\\n\\\\n**跨模型 entropy mechanism 一致性: 不成立。Selective SICA 非 universal 方案。**\\\\n\\\\n但 entropy decomposition 揭示了更有价值的 regime mechanism：\\\\n\\\\n| Experiment | Model | Dataset | High-E n | High-E Δpp | Low-E n | Low-E Δpp |\\\\n|-----------|-------|---------|----------|-----------|---------|----------|\\\\n| exp-033 s42 | Mistral-7B | FOLIO | 78 | **+12.8** | 126 | 0.0 |\\\\n| exp-052 s123 | Mistral-7B | FOLIO | 77 | **+9.1** | 127 | 0.0 |\\\\n| exp-053 s456 | Mistral-7B | FOLIO | 75 | -1.3 | 129 | 0.0 |\\\\n| exp-046 | Mistral-7B | PW-600 | 267 | -4.9 | 333 | -1.2 |\\\\n| exp-036 | Qwen2.5-14B | FOLIO | 37 | **-8.2** | 167 | -0.6 |\\\\n| exp-038 | Qwen2.5-14B | LogiQA | 23 | -4.3 | 177 | 0.0 |\\\\n| exp-035 | Qwen2.5-7B | FOLIO | 47 | -2.1 | 157 | 0.0 |\\\\n| exp-048 | LLaMA-8B | PW-600 | 76 | -3.9 | 104 | -1.9 |\\\\n\\\\n(注: SC/Δ 使用 pre-tiebreaking 值，entropy grouping 不受 tiebreaking 影响。D064 修正后 deltas 会略有变化但 pattern 不变。)\\\\n\\\\n**三个核心发现：**\\\\n1. **Low-entropy: SICA≈SC 跨模型一致** (8/8 experiments Δ≈0) → traces 一致时 constraints 无新信息\\\\n2. **High-entropy 方向因 regime 而异**：Goldilocks +12.8pp vs Type A -8.2pp vs Type C -4.9pp\\\\n3. **Mechanism 解释**：\\\\n   - Goldilocks (SC~55%, κ~0.46): 真实不确定性 → constraints 打破平局正确方向\\\\n   - Type A (SC>75%, κ>0.65): 偶发错误 → constraints 放大 confirmation bias\\\\n   - Type C (SC<40%, κ~0.20): 系统性错误 → constraints 是噪声\\\\n\\\\n### 调整后核心转变\\\\n\\\\n论文以 \\\\\\\"entropy decomposition 揭示 regime-dependent mechanism\\\\\\\" 为核心分析贡献（不是 universal diagnostic）：\\\\n- **Entropy decomposition 作为分析工具**：分离 SICA 作用点（high-entropy）vs 不作用点（low-entropy）\\\\n- **Regime mechanism 量化**：同样是 high-entropy 问题，direction depends on SC+κ → 完美支持 dual bottleneck\\\\n- **Abandoned**: Selective SICA 作为 universal practical contribution（只在 Goldilocks zone 有效）\\\\n- **Upgraded**: 核心图 = high-entropy Δ vs SC scatter（8 points, 3 regimes 清晰分离）\\\\n- **Quality Ladder** (D067: L1 NULL CONFIRMED)\\\\n  - L0: Self-extraction (Mistral→Mistral): 59.31%, Δ=+3.43pp ns\\\\n  - L1a: Qwen3-14B→Mistral traces: 60.29%, Δ=+4.41pp (+0.98pp vs self = 2题/204 = noise)\\\\n  - L1b: Qwen2.5-14B→Mistral traces: 58.33%, Δ=+2.45pp (-0.98pp vs self = 2题/204 = noise)\\\\n  - L3: Oracle 100% disc, Δ=+14.22pp p<0.001\\\\n  - **结论**: L1 ≈ L0 << L3。Bottleneck 在 traces（同源输入），不在 extractor（换模型无效）\\\\n  - **Paper contribution**: \\\\\\\"bottleneck is fundamental to extraction, not just model capability\\\\\\\" — 强化 structural limitation 论点\\\\n- **CJT/Eff-K 保留**：解释 why high-entropy behavior differs across regimes\\\\n\\\\nD060 要素全部保留：\\\\n- Condorcet independence 框架 → 理论基础\\\\n- 9 种修复全部失败 → structural limitation 证据\\\\n- 2/3 seeds positive trend but **0/3 significant** (D066: p=0.092/0.070/1.0) → Goldilocks zone 作为 directional trend, not confirmed effect\\\\n- K/T sensitivity non-monotonic → SC confound insight\\\\n- 用户指示: 投 May 25 不变，冲 4.0\\\\n\\\\n## Core Claims (5 条) — D060 纯 Analysis Framing\\\\n\\\\n### Analysis Claims (已验证)\\\\n\\\\n1. **Independence Bottleneck**: Self-consistency 隐含 Condorcet Jury Theorem 的独立性假设，但同模型采样的 traces 高度相关。Worker 验证的 κ 值：\\\\n   - Qwen-14B FOLIO: κ=0.744, Eff-K=1.31 (SC=75.49%, Δ=+0.25pp n.s.)\\\\n   - Qwen-14B LogiQA: κ=0.821, Eff-K=1.20 (SC=78.5%, Δ=+0.50pp n.s.)\\\\n   - Mistral-7B FOLIO s42 (exp-033): κ=0.501, Eff-K=1.84 (SC=55.88%, Δ=+3.43pp **p=0.092 ns**) ← primary seed [D064+D066]\\\\n   - Mistral-7B FOLIO s123: κ=0.491, Eff-K=1.88 (SC=54.41%, Δ=+2.94pp **p=0.070 ns**)\\\\n   - Mistral-7B FOLIO s456: κ=0.507, Eff-K=1.82 (SC=55.88%, Δ=0.00pp p=1.0 ns)\\\\n   - Mistral-7B PW-600 (exp-046): κ=0.210, Eff-K=3.63 (Δ=-2.83pp p=0.010, SC=39%)\\\\n   规律：跨模型对比清晰（Qwen Eff-K≈1.2-1.3 → 0 gain; Mistral Eff-K≈1.85-2.22 → variable gain）。但 Mistral seeds 内部，Eff-K 与 delta 非单调（exp-033 Eff-K 最低 1.85 却 delta 最高 +3.43pp）→ Eff-K 是跨模型必要条件，seed 内 variance 仍主导。exp-046 Eff-K 最高(3.63) 但 SC 太低(39%) 导致 delta 为负 → 需同时满足 sufficient Eff-K AND sufficient SC。\\\\n\\\\n2. **Oracle Gap Localizes Extraction Bottleneck**: Gold FOL + MAX-SAT = +14.22pp (p=2.0e-7)，自提取仅 +3.43pp (best seed, D064 corrected) = 24% utilization。聚合机制本身有效，瓶颈在自提取质量。Two-layer analysis:\\\\n   - **Constraint taxonomy**: 43% trivially_satisfied（被所有候选答案满足的约束，不排除任何答案）\\\\n   - **Discriminative filtering**: 仅 ~8% 约束在 MAX-SAT scoring 中完全 non-discriminative（移除后 0 gains）\\\\n   - **关键区分**: 43% 和 8% 度量不同。trivially_satisfied 约束在 MAX-SAT 中仍可有不同满足程度（partial vs full），所以不全是 non-discriminative。但即使 constraints 是 discriminative 的，它们的\\\\\\\"区分方向\\\\\\\"与模型自身偏差一致（confirmation bias）。both_wrong 组 score_range=29.4。九种修复全部失败。\\\\n\\\\n3. **Regime-Dependent Capability Trap**: SICA 有效性取决于提取模型的基线准确率，存在双边界：\\\\n   - Type A (SC ≥ ~60%): 确认偏差，constraints 镜像模型自身答案。**exp-034 vs exp-039 同配置 delta 翻转**: exp-034 Δ=+0.51pp (n=589), exp-039 Δ=-2.00pp (n=600)。SC baseline 方差 (3.38pp) >> SICA 效应 → Type A delta 是 trace sampling noise。SICA 比 SC 更稳定 (跨运行方差 0.87pp vs 3.38pp，仅 2 点，需更多 seed 验证)\\\\n   - Type C (SC ≤ ~40%): traces 主要错误，constraints 是噪声 (exp-046: Δ=-2.83pp, p=0.0095)\\\\n   - Goldilocks zone (~50-56% SC): 部分独立性 + 部分正确性 (exp-033: Δ=+3.43pp, p=0.092 ns; mean of 3 seeds: +2.12pp) ⚠️ D076 Reviewer: 0/3 seeds significant, 不应作为核心叙事支柱。作为 directional observation 保留，不做强 claim。\\\\n   - Type B: 领域不可形式化 (LogiQA: contradiction rate 0.8%)\\\\n\\\\n4. **C0+SC Two-Dimensional Diagnostic**: C0 (multi-candidate rate) + SC accuracy 形成零成本部署诊断。C0<5% → degenerate; high C0 + high SC → trap; high C0 + low SC → potential gains。\\\\n\\\\n### Remediation Evidence (D060: 全部失败 — 强化 analysis narrative)\\\\n\\\\n5. **Nine Remediation Attempts All Failed**: 原 6 种 + 3 种靶向修复全部无效，证明 independence bottleneck 是结构性的：\\\\n   - D059 三路 method improvement 全部失败：\\\\n     - Discriminative Filtering: 119/204 处理后 0 gains 1 loss，~92% 约束本身就是 discriminative，过滤是 near-no-op\\\\n     - T=1.0 (exp-054): delta 从 +3.43pp 崩塌到 0.00pp（D064 corrected），温度敏感性极端\\\\n     - Multi-Temp (exp-055): ✅ 完成，delta=+0.00pp (b=5,c=5 完美对称), SC=57.84%. 混合 T=0.3/0.7/1.2 各 4 traces 未改善 SICA。附带发现：multi-temp 提升 SC baseline (+3.4pp vs 单温度 54.41%)，说明混合温度对 majority voting 有帮助，但 SICA constraint extraction 无法利用这种 diversity → bottleneck 在 extraction 而非 trace diversity\\\\n   - 原 6 种：contrastive prompting, cross-model extraction, generational scaling, solver-guided refinement, consistency filtering, cross-trace UNSAT\\\\n   - 9 种修复涵盖 prompting / architecture / capability / verification / diversity / filtering 全维度，全部失败 → trap is fundamental\\\\n\\\\n## D070/D074 Update: Method-Level Interventions Also Fail — \\\\\\\"Fundamental Limitation\\\\\\\" Confirmed\\\\n\\\\n### Three Method Lines × Two Datasets = All Negative (D074)\\\\n\\\\nD070 从纯 analysis 升级为 analysis + method paper，但三条方法线全面失败（D074 确认），反而强化了原始 analysis 结论。\\\\n\\\\n**方法×数据集完整结果**：\\\\n| Method | FOLIO-204 | LogiQA-200 | Failure Mode |\\\\n|--------|-----------|------------|--------------|\\\\n| ICG (Independent Constraint Gen.) | Δ=-2.0pp (3-seed: -2.0/+1.5/-1.0, mean=-0.5pp±1.8pp, 噪声) | Δ=-0.5pp | Neutral — 独立约束质量≈trace-sourced约束 |\\\\n| Contrastive (Pro/Con Scoring) | Δ≈-16pp | Δ≈-7pp (interim) | Harmful — 26% degenerate scoring, pro/con 不平衡 |\\\\n| Debate (Proposer/Critic) | Δ=-18.6pp | Δ≈-28pp (interim) | Catastrophic — 7B 模型角色扮演严重退化推理 |\\\\n\\\\n**三种失败模式的分析价值**（论文 \\\\\\\"Why Methods Fail\\\\\\\" section）：\\\\n1. **ICG (neutral)**: 独立于 traces 生成的约束不比 trace-sourced 约束更好。说明 bottleneck 不仅是 \\\\\\\"约束来自 traces\\\\\\\"，而是模型的推理偏差从问题理解阶段就存在——独立约束和 trace-sourced 约束继承相同的 model bias。\\\\n2. **Contrastive (harmful)**: 强制 pro/con 评估引入 degenerate scoring（26% 问题无法有效区分）。7B 模型无法可靠生成平衡的对立约束——pro 约束系统性多于 con（94 pro vs 65 con），confirmation bias 从约束提取转移到了约束生成。\\\\n3. **Debate (catastrophic)**: Proposer/Critic/Defense 多角色链在 7B 模型上导致答案质量严重退化。辩论不仅未增加多样性，反而引入了角色扮演的额外认知负担。同模型辩论 = 同源性 + 角色扮演退化，双重损失。\\\\n\\\\n**Scale limitation caveat**: 所有方法测试在 7B 模型上。7B 模型生成 Z3 格式 FOL 约束的能力不足（ICG 多题 \\\\\\\"0/N constraints parsed\\\\\\\"）。14B+ 模型可能有不同结果——这既是 limitation 也是 future work 入口。\\\\n\\\\n### κ Generalization — Independence-Accuracy Trade-off (D075, CAPSTONE FINDING)\\\\n\\\\nexp-077 测量三种聚合方式在 Mistral-7B FOLIO-204 上的 κ 和 Eff-K：\\\\n| 聚合方式 | Fleiss' κ | Eff-K | 名义 K |\\\\n|----------|----------|-------|--------|\\\\n| Self-Consistency | 0.4384 | 2.02 | 10 |\\\\n| Diverse-Prompt | 0.4030 | 2.21 | 12 |\\\\n| LLM-Debate | 0.1549 | 4.44 | 12 |\\\\n\\\\n结合 exp-076 Debate Δ=-18.6pp 的准确率数据，揭示**同模型框架下的 fundamental independence-accuracy trade-off**：\\\\n- **SC/Diverse-Prompt**: κ~0.4，traces 高度相关但准确率正常。换 prompt 策略不改善独立性（Δκ=0.04）。\\\\n- **Debate**: κ=0.15，成功打破 trace 相关性（Eff-K 从 2.0 跃升到 4.4），但准确率崩溃 -18.6pp。低 κ 不代表\\\\\\\"更独立的推理\\\\\\\"——是 disagreement amplification（系统性噪声）。\\\\n- **Trade-off 本质**: 同一模型的推理能力是固定的。要么输出一致（高 κ, 正确但不独立），要么输出分歧（低 κ, 独立但不正确）。Condorcet Jury Theorem 要求 both independent AND accurate，同模型框架下无法同时满足。\\\\n\\\\n**论文叙事升级**: 从 \\\\\\\"methods fail\\\\\\\" → \\\\\\\"independence-accuracy trade-off is fundamental to same-model reasoning\\\\\\\"。突破瓶颈需要跨模型方案（不同模型天然更独立），Oracle 实验（gold FOL 来自外部知识源）已间接验证了这一点。\\\\n\\\\n### New Claim 6 (D070/D074)\\\\n\\\\n6. **Method-Level Interventions Cannot Break the Bottleneck**: 三种针对 independence bottleneck 不同环节的方法（ICG→循环依赖, Contrastive→confirmation bias, Debate→trace 同质性）在 2 个数据集上全部失败。加上之前 9 种 prompt-level 修复，共 12 种修复尝试全败。这证明 independence bottleneck 不是单一环节的问题，而是 same-model self-extraction 的根本性限制。\\\\n\\\\n### New Claim 7: Symbolic Confirmation Bias (D082 — CORE FINDING)\\\\n\\\\n7. **Symbolic Confirmation Bias**: LLM 从 CoT traces 提取的 FOL 约束系统性确认 trace 自身（可能错误的）答案，而非独立验证 ground truth。\\\\n   - SICA 判对题：gold constraint 78.1%，bias ratio = 0.28\\\\n   - SICA 判错题：错误 constraint 83.3%，bias ratio = **4.97×**\\\\n   - 97.6% SICA 错误与 SC 错误完全重合\\\\n   - SICA 翻盘的 12 例来自 minority trace diversity（43% gold support），不是 symbolic reasoning\\\\n   - **因果链**：模型推理→答案→从含答案 trace 提取 FOL→约束确认答案→聚合≈SC\\\\n   - **CEGIS 验证**：迭代精炼 R1 +3.43pp < 原始 SICA +4.9pp → 约束一致性不是瓶颈，偏向性才是\\\\n   - **Quality Ladder 验证**：L1 ≈ L0 << L3 → bottleneck 在 traces（同源输入），不在 extractor\\\\n\\\\n### New Claim 8: Process-κ (D082 — NEW METRIC)\\\\n\\\\n8. **Process-Level Independence (Process-κ)**: answer-κ 低估真实独立性瓶颈。CoT 推理过程相似性远高于答案一致性。\\\\n   - Mistral-7B FOLIO-204：CoT cosine similarity **0.69** >> answer-κ **0.41**\\\\n   - 两者几乎无相关性：r = -0.06, p = 0.36\\\\n   - 仅 **9.3%** trace 对是\\\\\\\"殊途同归\\\\\\\"（同答案不同路径）\\\\n   - answer-κ 是 true independence bottleneck 的 lower bound\\\\n   - 适用于所有 LLM trace aggregation 方法，不限于 SICA\\\\n\\\\n## D082/D085: Comprehensive Method Exhaustion — 25+ ALL Fail\\\\n\\\\nD080 启动全方向并行探索（Wave 1-3），在 D074 的 12 种修复基础上又测试 13+ 新干预：\\\\n\\\\n| 方法 | 类型 | 结果 | 关键数据 |\\\\n|------|------|------|----------|\\\\n| PROVE 代码验证 | paradigm shift | ❌ | Code gen 15.2%, accuracy=random |\\\\n| CEGIS 迭代精炼 | multi-round | ❌ | R1 +3.43pp < SICA +4.9pp |\\\\n| DeepConf 置信度 | filtering | ❌ | logprob 与正确性零相关 |\\\\n| Cross-model SICA | cross-model | ❌ | Δ=-0.49pp despite lower κ |\\\\n| Problem Perturbation | input diversity | ❌ | κ 升至 0.696 (反效果) |\\\\n| MIN-UNSAT | solver objective | ❌ | 49.5% < SC 54.4% |\\\\n| κ-aware SC | voting rule | ❌ | 11/11 Δ=0 |\\\\n| Z3 Trace Filter | trace filtering | ❌ | negative |\\\\n| Bootstrapped Gold | iterative | ❌ | negative |\\\\n| Selective Abstention | diagnostic | ⚡ | AUROC=0.673, +4.4pp@80%cov |\\\\n\\\\n**D085 总结**: 9 prompt-level + 3 method-level + 13 新方向 = **25+ 干预全部 negative**。Independence bottleneck 在 same-model self-extraction 框架下无解，所有维度（diversity/architecture/capability/verification/filtering/voting/solver/paradigm）已穷尽。\\\\n\\\\n### Updated Headline Result (D085)\\\\n\\\\n\\\\\\\"Across 6+ models and 4 domains, symbolic consensus aggregation shows no statistically significant positive effect. 25+ interventions spanning prompt engineering, method-level redesign (ICG, Contrastive, Debate), solver modifications, cross-model aggregation, code-based verification, and iterative refinement all fail. We identify the root cause as Symbolic Confirmation Bias: self-extracted FOL constraints systematically confirm the trace's own answer (bias ratio 4.97× on incorrect problems), making symbolic aggregation equivalent to majority voting. Process-level analysis reveals reasoning paths are far more homogeneous than answers suggest (cosine similarity 0.69 vs answer-κ 0.41). The one method that breaks trace correlation (Debate: κ 0.44→0.15) does so at catastrophic accuracy cost (-18.6pp), revealing a fundamental independence-accuracy trade-off. Oracle constraints prove the aggregation mechanism works (+14.22pp, p<0.001), localizing the bottleneck entirely to self-extraction quality.\\\\\\\"\\\\n\\\\n### Updated Story Spine (D074)\\\\n\\\\n- **Problem**: [unchanged]\\\\n- **Theoretical lens**: [unchanged]\\\\n- **Systematic evaluation**: [unchanged]\\\\n- **Regime characterization**: [unchanged]\\\\n- **Remediation failures strengthen thesis (D085 FINAL)**: 9 prompt-level + 3 method-level + 13 new directions = **25+ interventions** across ALL dimensions (diversity/architecture/capability/verification/filtering/voting/solver/paradigm), all fail → bottleneck is fundamental and exhaustively proven\\\\n- **Method failure analysis**: Three methods targeting different bottleneck aspects show three distinct failure modes (neutral/harmful/catastrophic), revealing that the bottleneck operates at multiple levels simultaneously\\\\n- **Independence-accuracy trade-off (HERO FINDING, D075)**: Debate breaks trace correlation (κ 0.44→0.15, Eff-K 2.0→4.4) but accuracy collapses (-18.6pp/-23.0pp). Same-model traces can be independent OR accurate, not both.\\\\n- **NEW — Symbolic Confirmation Bias (CORE FINDING, D082)**: Root cause identified — self-extracted FOL constraints systematically confirm the trace's own answer (bias ratio 4.97× on incorrect problems). Causal chain: model reasons → answer → FOL extraction confirms answer → aggregation ≈ SC. This is WHY 25+ methods fail.\\\\n- **NEW — Process-κ (NEW METRIC, D082)**: CoT reasoning similarity (0.69) >> answer-κ (0.41), r=-0.06. Only 9.3% of trace pairs are \\\\\\\"convergent reasoning.\\\\\\\" answer-κ underestimates the true bottleneck. Novel metric applicable to all LLM trace aggregation.\\\\n- **Actionable contribution**: C0+SC diagnostic + κ-based Eff-K estimation = zero-cost deployment toolkit. κ analysis shows SC itself has a scaling ceiling (Eff-K ≈ 2 means K>12 traces yield diminishing returns).\\\\n- **Universal across architectures (D078)**: Three families: Mistral-7B κ=0.438, LLaMA-8B κ=0.412, Qwen2.5-7B κ=0.658, Qwen2.5-14B κ=0.738. Family effect (Δκ=0.22) >> scale effect (Δκ=0.08).\\\\n- **Headline (D085)**: Independence bottleneck is structural, universal across architectures, and rooted in Symbolic Confirmation Bias. 25+ interventions spanning all conceivable dimensions fail. Process-κ reveals reasoning homogeneity far exceeds answer-level agreement. The independence-accuracy trade-off constrains all same-model trace aggregation.\\\\n\\\\n## Core Insight (D060 Updated — Dual Bottleneck)\\\\n\\\\n**Dual Requirement Framework**: SICA 效应需要同时满足两个条件，缺一不可：\\\\n1. **Sufficient Independence** (Eff-K > threshold): traces 需要提供足够多的独立视角\\\\n2. **Sufficient Quality** (SC > ~50%): traces 需要有足够的正确率，否则约束是噪声\\\\n\\\\nCondorcet Jury Theorem 要求投票者独立且 p>0.5。同模型采样的 reasoning traces 严重违反独立性假设（Fleiss' κ = 0.21–0.82，Eff-K 仅 1.20–3.63），解释了为什么简单增加 K 或添加符号约束不能突破 SC 的天花板。\\\\n\\\\n实验数据完美支持 dual requirement（κ 使用统一脚本 compute_fleiss_kappa_unified.py，SC/Δpp 使用 registry 原始值）：\\\\n- **Qwen family**: κ=0.66-0.82, Eff-K≈1.20-1.46（独立性不足）→ all near-zero delta，无论 SC 多高\\\\n- **Mistral-7B FOLIO**: κ≈0.46, Eff-K≈2.0（中等独立性）+ SC≈55%（中等质量）→ +3.43pp best seed, mean +2.12pp (2/3 seeds positive, 1 null)\\\\n- **Mistral-7B PW-600**: κ=0.20, Eff-K=3.76（最高独立性）但 SC=39%（质量不足）→ -2.83pp\\\\n- 只有 Goldilocks zone（中等 Eff-K + 中等 SC）出现正向 delta\\\\n- **Dual bottleneck 直接验证 (exp-055)**：Multi-temp κ=0.427 Eff-K=2.11（比单温度 κ≈0.46 Eff-K≈2.0 更独立）但 delta=0.00pp → 提高 independence 不够，还需要 extraction quality\\\\n- **T sensitivity 孤立尖峰 (4/4 complete, D064 corrected)**：T=0.3(Δ=-1.47), T=0.5(Δ=-0.98), T=0.7(Δ=+3.43, κ=0.460, Eff-K=1.98), T=1.0(Δ=0.00, κ=0.394, Eff-K=2.25)。T=0.7 孤立尖峰更突出。T=0.7 SC=55.88%（最低）→ entropy 最高 → SICA 操作空间最大。温度效应与 SC 效应互为 confound，论文需讨论\\\\n- **Thinking mode κ=0.913, Eff-K=1.09 (exp-028b)**：近乎确定性。思维模式让 traces 更一致 → 独立性更差。\\\\\\\"更好的推理\\\\\\\"反而加剧 independence bottleneck。\\\\n\\\\n**κ 是 model-level 稳定属性**：统一处理后 Mistral 三 seed κ 收敛至 0.457-0.460（之前 0.41-0.50 差异是非标准 answer 处理的 artifact）。κ 跨 seed 几乎相同，但 delta 差异大（+3.43 vs +2.94 vs 0.00）→ seed-level constraint quality variance 主导，非 κ。\\\\n\\\\n完整 κ 表（⚠️ D062: κ 将用 raw answers 重算，当前 unified 值为临时值。Qwen 无变化，Mistral 条件将更新）：\\\\n| Exp | Model | κ(unified→raw pending) | Eff-K | SC%(registry) | Δpp(registry) |\\\\n|-----|-------|------------|-------|---------------|---------------|\\\\n| exp-028b | Qwen3-14B thinking | 0.913 | 1.09 | ~84% | ~0 |\\\\n| exp-038 | Qwen-14B LogiQA | 0.821 | 1.20 | 78.50 | -0.50 |\\\\n| exp-027 | Qwen3-14B | 0.773 | 1.26 | 84.31 | +0.49 |\\\\n| exp-036 | Qwen2.5-14B | 0.744 | 1.31 | 75.49 | +0.25 |\\\\n| exp-035 | Qwen2.5-7B | 0.658 | 1.46 | 76.47 | -0.49 |\\\\n| exp-049b | Mistral-7B LogiQA | 0.512 | 1.81 | 51.00 | +0.50 |\\\\n| exp-057 | Mistral-7B T=0.3 | 0.502 | 1.84 | 58.33 | -1.47 |\\\\n| exp-058 | Mistral-7B T=0.5 | 0.516 | 1.80 | 58.33 | -0.98 |\\\\n| exp-033 | Mistral-7B s42 | 0.460 | 1.98 | 55.88 | +3.43 |\\\\n| exp-052 | Mistral-7B s123 | 0.457 | 1.99 | 54.41 | +2.94 |\\\\n| exp-053 | Mistral-7B s456 | 0.457 | 1.99 | 55.88 | 0.00 |\\\\n| exp-055 | Mistral-7B multi-T | 0.427 | 2.11 | 57.84 | 0.00 |\\\\n| exp-054 | Mistral-7B T=1.0 | 0.394 | 2.25 | 55.39 | 0.00 |\\\\n| exp-046 | Mistral-7B PW-600 | 0.200 | 3.76 | 39.33 | -2.83 |\\\\n注：κ 基于 T/F/U 三类归一化，Mistral-7B 约 12-16% traces 被归一化（Qwen 100% valid）。Mistral SC/Δpp 已更新为 D064 tiebreaking 修正值；Qwen 不受影响。\\\\n\\\\nOracle control (+14.22pp) 证明 MAX-SAT 聚合机制本身有效，但自提取约束仅利用了 24% 的理论上限。Discriminative filtering 实验揭示关键机制：~92% 约束 ARE discriminative，但过滤掉 ~8% non-discriminative 约束后 delta 不变（0 gains）。问题不在约束缺乏判别力，而在于 discriminative constraints 的区分方向与模型偏差一致（confirmation bias）。\\\\n\\\\n**Remediation insight (D060)**: 9 种修复尝试全部失败，包括直接靶向 independence（multi-temp diversity, exp-055: Eff-K 从 2.0→2.11 但 delta 仍为 0）和 constraint quality（discriminative filtering）。这证明 bottleneck 不是简单的 diversity 或 quality 问题，而是 same-model self-extraction 的根本性限制。\\\\n\\\\n**Key evidence**:\\\\n- **Condorcet independence quantification (统一脚本, 公式: Eff-K=K/(1+(K-1)κ))**: Mistral-7B FOLIO κ≈0.46 (Eff-K≈2.0, 三 seed 高度稳定), Mistral-7B PW-600 κ=0.200 (Eff-K=3.76), Qwen2.5-14B FOLIO κ=0.744 (Eff-K=1.31), Qwen2.5-14B LogiQA κ=0.821 (Eff-K=1.20), Qwen3-14B κ=0.773 (Eff-K=1.26), Qwen2.5-7B κ=0.658 (Eff-K=1.46). 跨模型清晰: Qwen Eff-K≈1.2-1.5→0 gain, Mistral FOLIO Eff-K≈2.0→variable gain, Mistral PW Eff-K=3.76 but SC too low→negative. κ stable across seeds (0.457-0.460), delta varies → seed-level constraint quality dominates.\\\\n- **Oracle control (exp-031)**: Gold FOL + MAX-SAT = 89.71% vs SC 75.49% (+14.22pp, p=2.0e-7). Unknown-type +31.9pp.\\\\n- **Two-layer constraint analysis**: 43% trivially_satisfied (taxonomy: satisfied by ALL answers) vs ~8% non-discriminative (filtering: same MAX-SAT score). Difference: trivially_satisfied constraints can still have different satisfaction DEGREES. Removing the 8% yields 0 gains → problem is not quality but confirmation bias direction.\\\\n- **K sensitivity (non-monotonic peak at K=12, 5/5 complete, D064+D066)**: K=4(-1.47pp), K=8(-1.96pp), K=12(+3.43pp p=0.092 ns), K=16(+1.47pp), K=20(+1.96pp). Peak at K=12, drops at K=16 but partially recovers at K=20. NOT clean inverted-U. K=12 SC=55.88% (post-fix). SC-confound with T sensitivity still holds. SICA at K=4 vs K=12 differs by ~4.9pp despite similar SC — proves SICA extracts different information than SC.\\\\n- **SC-confound (cross-cutting insight)**: K=12 和 T=0.7 都是 SC 最低 (54.41%) 的配置 → SICA \\\\\\\"最佳超参\\\\\\\"可能反映 entropy/operating-window 效应而非 K 或 T 的因果贡献。论文需要讨论这个 confound，但也可以正面利用：SC level 是更基本的预测变量，K 和 T 通过影响 SC 来间接影响 SICA delta。\\\\n- **T sensitivity (isolated peak, 4/4 complete, D064 corrected)**: T=0.3(Δ=-1.47pp), T=0.5(Δ=-0.98pp), T=0.7(Δ=+3.43pp p=0.092 ns), T=1.0(Δ=0.00pp). NOT smooth inverted-U — T=0.7 is an isolated spike. T=0.7 has lowest SC (55.88%) → highest entropy → largest SICA operating window. Temperature and SC effects confounded. Strengthens fragility narrative.\\\\n- **Regime boundary**: Qwen-14B (SC=75.49%) Δ=-0.98pp vs Mistral-7B (SC=55.88%) Δ=+3.43pp p=0.092 ns\\\\n- **Type C failure (exp-046)**: Mistral PW-D5 SC=39.33%, Δ=-2.83pp, p=0.010, κ=0.210, Eff-K=3.63, contradiction rate 5.5%. Highest Eff-K yet worst delta → independence alone insufficient when SC too low.\\\\n- **Seed replication (D064+D066)**: 2/3 seeds positive but **0/3 significant** after tiebreaking correction: s42 Δ=+3.43pp p=0.092, s123 Δ=+2.94pp p=0.070, s456 Δ=0.00pp p=1.0. Mean +2.12pp. Only significant McNemar effects are NEGATIVE: exp-046 Δ=-2.83pp p=0.014, exp-039 Δ=-2.50pp p=0.011. Paper must frame as \\\\\\\"positive directional trend\\\\\\\" not \\\\\\\"significant positive effect\\\\\\\".\\\\n- **Nine remediation failures (ALL CONFIRMED)**: contrastive prompting, cross-model, generational scaling, solver-guided, consistency filtering, cross-trace UNSAT, discriminative filtering (0 gains), T=1.0 (delta collapse +3.43→0.00pp, D064 corrected), multi-temp (delta=+0.00pp, b=5 c=5). All 9 failed → trap is fundamental, bottleneck is structural.\\\\n- **Entropy decomposition (VERIFIED 2026-05-19)**: High-entropy proportion: Mistral FOLIO 38% (78/204) vs Qwen FOLIO 18% (37/204) vs Qwen LogiQA 12% (23/200). SICA on high-entropy: Mistral FOLIO s42 +12.8pp, s123 +9.1pp, s456 -1.3pp; Qwen FOLIO -8.2pp; all others negative. Low-entropy: SICA≈SC across all 8 experiments (Δ≈0). Entropy decomposition reveals regime-dependent mechanism, NOT universal diagnostic.\\\\n- **Confirmation bias quantification**: ⚠️ \\\\\\\"62.3%\\\\\\\" and \\\\\\\"28.6%\\\\\\\" confirmed NOT present in any .tex file — likely hallucinated in earlier draft. DO NOT USE. Replace with verified metrics from experiment outputs only.\\\\n\\\\n## Story Spine (D059 Updated)\\\\n\\\\n- **Problem**: LLMs' reasoning can be improved by sampling multiple chains-of-thought and aggregating via majority voting (self-consistency). Recent work proposes symbolic augmentation: extract formal constraints from traces and use SAT solvers for answer selection. But does symbolic aggregation actually outperform simple voting?\\\\n- **Theoretical lens**: Condorcet Jury Theorem requires voter independence. We quantify trace independence via Fleiss' κ and show Effective-K << nominal K. This explains the fundamental limitation of same-model trace aggregation.\\\\n- **Systematic evaluation**: SICA (MAX-SAT over FOL constraints) across 3 domains × 5 model families. Oracle control separates extraction vs aggregation failure. Discriminative filtering reveals ~92% constraints are discriminative, yet SICA gains are fragile — confirmation bias, not constraint quality, is the bottleneck.\\\\n- **Regime characterization**: Three failure modes (Type A/B/C) + narrow Goldilocks zone. C0+SC as deployment diagnostic.\\\\n- **Remediation failures strengthen thesis**: 9 targeted interventions (prompting, architecture, capability, verification, diversity, filtering) all fail to close the oracle gap, proving the bottleneck is fundamental to same-model self-extraction.\\\\n- **Headline result (D066 McNemar corrected)**: \\\\\\\"Across 6 models and 4 domains, symbolic consensus aggregation shows no statistically significant positive effect under corrected tiebreaking (best seed +3.43pp, p=0.092). The only significant effects are negative (PW-600: -2.83pp p=0.014, -2.50pp p=0.011). However, entropy decomposition reveals a striking regime-dependent pattern: SICA's entire effect concentrates on high-entropy questions, with +12.8pp in the Goldilocks zone but -2 to -8pp elsewhere. Oracle constraints prove the aggregation mechanism works (+14.22pp, p<0.001), localizing the bottleneck to extraction quality (24% utilization). Condorcet analysis (Eff-K=1.2-2.0 for nominal K=12) explains trace non-independence. Nine remediation strategies all fail, confirming the bottleneck is structural to same-model self-extraction.\\\\\\\"\\\\n\\\\n## Anticipated Reviewer Concerns & Defensive Experiments\\\\n\\\\n1. **\\\\\\\"Gains not statistically significant\\\\\\\"** → Correct: no positive effect reaches significance (best p=0.092). This IS the finding. Oracle p=2.0e-7 proves the mechanism works; the insignificance of self-extraction gains demonstrates the extraction bottleneck. Regime pattern (8 entropy conditions) provides systematic evidence beyond any single p-value.\\\\n2. **\\\\\\\"Only one positive result (exp-033)\\\\\\\"** → Seed replication: 2/3 positive (s42 +3.43pp, s123 +2.94pp), 1/3 null (s456 0.00pp). Mean +2.12pp. Effect IS real but fragile — the fragility itself IS the finding.\\\\n3. **\\\\\\\"Condorcet framework is trivial\\\\\\\"** → Fleiss' κ quantification is novel in SC/SICA context. Eff-K is actionable: tells practitioners how many truly independent traces they get.\\\\n4. **\\\\\\\"Multi-temp / filtering should work\\\\\\\"** → We tried both. Multi-temp (exp-055): negative. Disc. filtering: 0 gains. T=1.0: delta collapse. These failures STRENGTHEN the structural bottleneck thesis.\\\\n5. **\\\\\\\"Only Qwen models\\\\\\\"** → 5 families: Qwen-14B, Mistral-7B, LLaMA-8B, DeepSeek-R1-7B, QwQ-32B.\\\\n6. **\\\\\\\"Only logic domain\\\\\\\"** → FOLIO + ProofWriter + LogiQA + StrategyQA + ARC-Challenge. Type B (domain formalizability) is itself a finding.\\\\n7. **\\\\\\\"Oracle is unfair comparison\\\\\\\"** → Diagnostic tool, not competing method. Separates extraction from aggregation.\\\\n8. **\\\\\\\"MAX-SAT is over-engineering\\\\\\\"** → exp-013: MaxSAT ≈ count-only. This IS the independence bottleneck evidence.\\\\n9. **\\\\\\\"Self-extraction confound\\\\\\\"** → Oracle control resolves completely.\\\\n10. **\\\\\\\"Published methods achieve gains (DyLoS, Aristotle, FoVer)\\\\\\\"** → Different paradigm (external verifiers/trained extractors). We characterize same-model self-extraction.\\\\n11. **\\\\\\\"C0 is trivially derived\\\\\\\"** → Zero-cost early stopping. Practical value.\\\\n12. **\\\\\\\"Why not just use a reasoning model?\\\\\\\"** → QwQ-32B: C0<5%, SICA≡SC.\\\\n13. **\\\\\\\"Random tiebreak baseline\\\\\\\"** → exp-003: SICA tiebreak 80% vs random 50%.\\\\n14. **\\\\\\\"Method improvement is incremental\\\\\\\"** → Grounded in diagnosis (independence + taxonomy), not ad-hoc.\\\\n15. **\\\\\\\"Weighted SC is simpler\\\\\\\"** → exp-016 planned. Weighted SC doesn't address independence.\\\\n16. **\\\\\\\"Within-model ICL transition contradicts regime theory\\\\\\\"** → exp-050b (SC=57.79%, Δ=-3.52pp): ICL changes trace generation characteristics, not just SC level. Paper must distinguish \\\\\\\"same model, different prompt\\\\\\\" from \\\\\\\"same model, same prompt, different accuracy.\\\\\\\"\\\\n\\\\n## Working Title\\\\n**\\\\\\\"Beyond Self-Consistency: How Trace Independence Limits Symbolic Consensus in LLM Reasoning\\\\\\\"**\\\\n(Alternatives:\\\\n- \\\\\\\"The Independence Bottleneck: Why Self-Extracted Symbolic Constraints Cannot Beat Majority Voting\\\\\\\"\\\\n- \\\\\\\"Symbolic Consensus Under the Condorcet Lens: Independence, Extraction, and the Limits of Self-Aggregation\\\\\\\")\\\\n\\\\nNOTE (Dream D037): Title MUST be scoped to \\\\\\\"self-extracted constraints\\\\\\\" / \\\\\\\"SICA\\\\\\\". Published methods (DyLoS, Aristotle, FoVer) use different approaches.\\\\n\\\\n## Paper Structure (EMNLP 8pp + appendix)\\\\n\\\\n### Main Tables\\\\n- T1: Main Results — models × domains, SC% / SICA% / Δpp / p-value, regime boundary\\\\n- T2: Oracle Control — Gold-FOL+MAX-SAT vs SC vs SICA-self, causal separation\\\\n- T3: Independence Quantification — Fleiss' κ / Eff-K / trace agreement per model\\\\n- T4: Extraction Error Taxonomy — trivially_satisfied / discriminative / both_wrong rates\\\\n- T5: K Sensitivity — K=4/8/12/16/20, non-monotonic (peak K=12, K=20 recovers), SC confound\\\\n\\\\n### Main Tables (continued)\\\\n- T6: Method-Level Intervention Results — 3 methods × 2 datasets, SC% / Method% / Δpp, failure mode classification\\\\n- T7: κ Generalization — SC / Debate / Diverse-Prompt κ and Eff-K (from exp-077, pending)\\\\n\\\\n### Main Figures\\\\n- F1: Method Pipeline (SICA + oracle control design)\\\\n- F2: SC Accuracy vs SICA Δ scatter (hero figure, regime boundary)\\\\n- F3: K Sensitivity with diversity metrics (K vs Δ, K vs Eff-K)\\\\n- F4: Extraction error breakdown (stacked bar)\\\\n- F5: Method intervention failure modes (grouped bar: ICG/Contrastive/Debate × FOLIO/LogiQA)\\\\n\\\\n### Appendix\\\\n- K ablation details, temperature sensitivity, per-domain results, overhead analysis\\\\n- Entropy-conditioned analysis (continuous scatter + bin sensitivity)\\\\n- Six remediation strategy details\\\\n- Confirmation bias quantification\\\\n- Seed replication analysis\\\\n- QwQ-32B / DeepSeek-R1 negative control\\\\n\\\\n## Claim Risk Notes (D059)\\\\n- **Seed replication**: 0/3 significant after D066 correction (p=0.092, 0.070, 1.0). 2/3 positive trend, 1/3 null. Mean +2.12pp. Frame as \\\\\\\"directional trend, not significant effect\\\\\\\" — fragility IS the finding.\\\\n- **Method claims DEAD (D060)**: All three method improvements failed. Paper is pure analysis. 9 remediation failures are EVIDENCE, not limitation.\\\\n- **Condorcet novelty**: ✅ VERIFIED. arXiv:2409.00094 applies CJT to cross-model LLM ensembles (different angle). No prior work applies Fleiss' κ or Eff-K to within-model SC traces. Our framing is novel.\\\\n- **exp-050b complication**: ICL transition Δ=-3.52pp at SC=57.79% complicates simple \\\\\\\"SC determines SICA.\\\\\\\" Explain via trace generation characteristic change.\\\\n- **Variable naming inconsistency**: 56.4% cross-trace pairs share zero Z3 variables. Key mechanism evidence.\\\\n\\\\n## Required Citations (minimum 30 references)\\\\n\\\\n- **SC & extensions**: Wang et al. 2023 (SC), Chen et al. 2023 (USC), Loo et al. 2025 (SC scaling plateaus), Taubenfeld et al. 2025 (weighted SC), DiVeRSe (Li et al. 2023)\\\\n- **Neuro-symbolic reasoning**: DyLoS (EACL 2026), Aristotle (ACL 2025), FoVer (TACL 2025), LogicAgent (2025), Logic-LM (Pan et al. 2023), LINC (Olausson et al. 2023)\\\\n- **Condorcet/voting theory**: Condorcet 1785, Austen-Smith & Banks 1996, **arXiv:2409.00094 (Examining Independence in Ensemble Sentiment Analysis, Sept 2024)** — closest prior work, applies CJT to cross-model LLM ensembles, finds independence violation. Our novelty: within-model trace independence + Fleiss' κ quantification + Eff-K + connection to symbolic aggregation\\\\n- **Test-time compute**: Snell et al. 2025, DeepSeek-R1, Diversity-Aware Training\\\\n- **Verification & reranking**: ORM (Cobbe et al. 2021), PRM (Lightman et al. 2023), Math-Shepherd\\\\n- **Constraint satisfaction**: SATBench (EMNLP 2025), LLM Meets Constraint Propagation (IJCAI 2025)\\\\n- **Debate & multi-agent**: Liang et al. 2023, Du et al. 2023\\\\n\\\\n## Additional Reviewer Concerns (D070/D074 Methods)\\\\n\\\\n17. **\\\\\\\"Why not use a larger model for constraint generation?\\\\\\\"** → Valid. All methods tested at 7B scale. ICG constraint parsing failures + Debate role-play degradation may be scale-dependent. This is explicitly noted as limitation and future work. The contribution is diagnosing the bottleneck and showing it's not trivially fixable, not claiming no fix exists at any scale.\\\\n18. **\\\\\\\"Only tested one model (Mistral-7B) for methods\\\\\\\"** → Methods are interventions on the extraction pipeline, not the base model. Testing on the same model that showed the clearest Goldilocks signal (Mistral-7B FOLIO) is the strongest test — if methods can't improve the best-case scenario, they won't help elsewhere.\\\\n19. **\\\\\\\"ICG multi-seed shows 1/3 positive\\\\\\\"** → Magnitudes (-2.0, +1.5, -1.0) are within SC baseline noise (3.5pp cross-seed). Mean ≈-0.5pp, std=1.8pp. No statistical significance. Properly framed as \\\\\\\"noise-level, neither improving nor degrading.\\\\\\\"\\\\n20. **\\\\\\\"Debate working in other papers\\\\\\\"** → Multi-agent debate literature uses diverse models or much larger models. Same-model 7B debate is a different regime. Our finding is specifically about same-model self-extraction limitations.\\\\n\\\\n## Claim Scoping Rules\\\\n- n=60 conditions: \\\\\\\"suggestive/consistent with\\\\\\\" NOT \\\\\\\"confirming\\\\\\\"\\\\n- n≥200 conditions: can \\\\\\\"confirm\\\\\\\"\\\\n- Combined N>1,300: acceptable if breakdown clearly stated\\\\n- Method claims: must show statistically significant improvement OR clear directional improvement with analysis\\\\n- \\\\\\\"Independence bottleneck\\\\\\\" framing: systematic quantification + theoretical grounding\\\\n\\\", \\\"total_chars\\\": 31186, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/paper_framing.md\", \"content\": \"# Paper Framing — symb_invariant_consensus\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main (ARR May 25)\\n- Deadline: May 25, 2026 (ARR submission)\\n\\n## D063 Direction: Entropy Decomposition + Quality Ladder — 目标 4.0\\n\\n**从 D060 \\\"Pure Analysis / negative result\\\" 升级为 \\\"Regime-Dependent Mechanism Analysis with Entropy Decomposition\\\"。** 用户决定冲 4.0。\\n\\n### Entropy Breakdown 验证结果 (2026-05-19 completed)\\n\\n**跨模型 entropy mechanism 一致性: 不成立。Selective SICA 非 universal 方案。**\\n\\n但 entropy decomposition 揭示了更有价值的 regime mechanism：\\n\\n| Experiment | Model | Dataset | High-E n | High-E Δpp | Low-E n | Low-E Δpp |\\n|-----------|-------|---------|----------|-----------|---------|----------|\\n| exp-033 s42 | Mistral-7B | FOLIO | 78 | **+12.8** | 126 | 0.0 |\\n| exp-052 s123 | Mistral-7B | FOLIO | 77 | **+9.1** | 127 | 0.0 |\\n| exp-053 s456 | Mistral-7B | FOLIO | 75 | -1.3 | 129 | 0.0 |\\n| exp-046 | Mistral-7B | PW-600 | 267 | -4.9 | 333 | -1.2 |\\n| exp-036 | Qwen2.5-14B | FOLIO | 37 | **-8.2** | 167 | -0.6 |\\n| exp-038 | Qwen2.5-14B | LogiQA | 23 | -4.3 | 177 | 0.0 |\\n| exp-035 | Qwen2.5-7B | FOLIO | 47 | -2.1 | 157 | 0.0 |\\n| exp-048 | LLaMA-8B | PW-600 | 76 | -3.9 | 104 | -1.9 |\\n\\n(注: SC/Δ 使用 pre-tiebreaking 值，entropy grouping 不受 tiebreaking 影响。D064 修正后 deltas 会略有变化但 pattern 不变。)\\n\\n**三个核心发现：**\\n1. **Low-entropy: SICA≈SC 跨模型一致** (8/8 experiments Δ≈0) → traces 一致时 constraints 无新信息\\n2. **High-entropy 方向因 regime 而异**：Goldilocks +12.8pp vs Type A -8.2pp vs Type C -4.9pp\\n3. **Mechanism 解释**：\\n   - Goldilocks (SC~55%, κ~0.46): 真实不确定性 → constraints 打破平局正确方向\\n   - Type A (SC>75%, κ>0.65): 偶发错误 → constraints 放大 confirmation bias\\n   - Type C (SC<40%, κ~0.20): 系统性错误 → constraints 是噪声\\n\\n### 调整后核心转变\\n\\n论文以 \\\"entropy decomposition 揭示 regime-dependent mechanism\\\" 为核心分析贡献（不是 universal diagnostic）：\\n- **Entropy decomposition 作为分析工具**：分离 SICA 作用点（high-entropy）vs 不作用点（low-entropy）\\n- **Regime mechanism 量化**：同样是 high-entropy 问题，direction depends on SC+κ → 完美支持 dual bottleneck\\n- **Abandoned**: Selective SICA 作为 universal practical contribution（只在 Goldilocks zone 有效）\\n- **Upgraded**: 核心图 = high-entropy Δ vs SC scatter（8 points, 3 regimes 清晰分离）\\n- **Quality Ladder** (D067: L1 NULL CONFIRMED)\\n  - L0: Self-extraction (Mistral→Mistral): 59.31%, Δ=+3.43pp ns\\n  - L1a: Qwen3-14B→Mistral traces: 60.29%, Δ=+4.41pp (+0.98pp vs self = 2题/204 = noise)\\n  - L1b: Qwen2.5-14B→Mistral traces: 58.33%, Δ=+2.45pp (-0.98pp vs self = 2题/204 = noise)\\n  - L3: Oracle 100% disc, Δ=+14.22pp p<0.001\\n  - **结论**: L1 ≈ L0 << L3。Bottleneck 在 traces（同源输入），不在 extractor（换模型无效）\\n  - **Paper contribution**: \\\"bottleneck is fundamental to extraction, not just model capability\\\" — 强化 structural limitation 论点\\n- **CJT/Eff-K 保留**：解释 why high-entropy behavior differs across regimes\\n\\nD060 要素全部保留：\\n- Condorcet independence 框架 → 理论基础\\n- 9 种修复全部失败 → structural limitation 证据\\n- 2/3 seeds positive trend but **0/3 significant** (D066: p=0.092/0.070/1.0) → Goldilocks zone 作为 directional trend, not confirmed effect\\n- K/T sensitivity non-monotonic → SC confound insight\\n- 用户指示: 投 May 25 不变，冲 4.0\\n\\n## Core Claims (5 条) — D060 纯 Analysis Framing\\n\\n### Analysis Claims (已验证)\\n\\n1. **Independence Bottleneck**: Self-consistency 隐含 Condorcet Jury Theorem 的独立性假设，但同模型采样的 traces 高度相关。Worker 验证的 κ 值：\\n   - Qwen-14B FOLIO: κ=0.744, Eff-K=1.31 (SC=75.49%, Δ=+0.25pp n.s.)\\n   - Qwen-14B LogiQA: κ=0.821, Eff-K=1.20 (SC=78.5%, Δ=+0.50pp n.s.)\\n   - Mistral-7B FOLIO s42 (exp-033): κ=0.501, Eff-K=1.84 (SC=55.88%, Δ=+3.43pp **p=0.092 ns**) ← primary seed [D064+D066]\\n   - Mistral-7B FOLIO s123: κ=0.491, Eff-K=1.88 (SC=54.41%, Δ=+2.94pp **p=0.070 ns**)\\n   - Mistral-7B FOLIO s456: κ=0.507, Eff-K=1.82 (SC=55.88%, Δ=0.00pp p=1.0 ns)\\n   - Mistral-7B PW-600 (exp-046): κ=0.210, Eff-K=3.63 (Δ=-2.83pp p=0.010, SC=39%)\\n   规律：跨模型对比清晰（Qwen Eff-K≈1.2-1.3 → 0 gain; Mistral Eff-K≈1.85-2.22 → variable gain）。但 Mistral seeds 内部，Eff-K 与 delta 非单调（exp-033 Eff-K 最低 1.85 却 delta 最高 +3.43pp）→ Eff-K 是跨模型必要条件，seed 内 variance 仍主导。exp-046 Eff-K 最高(3.63) 但 SC 太低(39%) 导致 delta 为负 → 需同时满足 sufficient Eff-K AND sufficient SC。\\n\\n2. **Oracle Gap Localizes Extraction Bottleneck**: Gold FOL + MAX-SAT = +14.22pp (p=2.0e-7)，自提取仅 +3.43pp (best seed, D064 corrected) = 24% utilization。聚合机制本身有效，瓶颈在自提取质量。Two-layer analysis:\\n   - **Constraint taxonomy**: 43% trivially_satisfied（被所有候选答案满足的约束，不排除任何答案）\\n   - **Discriminative filtering**: 仅 ~8% 约束在 MAX-SAT scoring 中完全 non-discriminative（移除后 0 gains）\\n   - **关键区分**: 43% 和 8% 度量不同。trivially_satisfied 约束在 MAX-SAT 中仍可有不同满足程度（partial vs full），所以不全是 non-discriminative。但即使 constraints 是 discriminative 的，它们的\\\"区分方向\\\"与模型自身偏差一致（confirmation bias）。both_wrong 组 score_range=29.4。九种修复全部失败。\\n\\n3. **Regime-Dependent Capability Trap**: SICA 有效性取决于提取模型的基线准确率，存在双边界：\\n   - Type A (SC ≥ ~60%): 确认偏差，constraints 镜像模型自身答案。**exp-034 vs exp-039 同配置 delta 翻转**: exp-034 Δ=+0.51pp (n=589), exp-039 Δ=-2.00pp (n=600)。SC baseline 方差 (3.38pp) >> SICA 效应 → Type A delta 是 trace sampling noise。SICA 比 SC 更稳定 (跨运行方差 0.87pp vs 3.38pp，仅 2 点，需更多 seed 验证)\\n   - Type C (SC ≤ ~40%): traces 主要错误，constraints 是噪声 (exp-046: Δ=-2.83pp, p=0.0095)\\n   - Goldilocks zone (~50-56% SC): 部分独立性 + 部分正确性 (exp-033: Δ=+3.43pp, p=0.092 ns; mean of 3 seeds: +2.12pp) ⚠️ D076 Reviewer: 0/3 seeds significant, 不应作为核心叙事支柱。作为 directional observation 保留，不做强 claim。\\n   - Type B: 领域不可形式化 (LogiQA: contradiction rate 0.8%)\\n\\n4. **C0+SC Two-Dimensional Diagnostic**: C0 (multi-candidate rate) + SC accuracy 形成零成本部署诊断。C0<5% → degenerate; high C0 + high SC → trap; high C0 + low SC → potential gains。\\n\\n### Remediation Evidence (D060: 全部失败 — 强化 analysis narrative)\\n\\n5. **Nine Remediation Attempts All Failed**: 原 6 种 + 3 种靶向修复全部无效，证明 independence bottleneck 是结构性的：\\n   - D059 三路 method improvement 全部失败：\\n     - Discriminative Filtering: 119/204 处理后 0 gains 1 loss，~92% 约束本身就是 discriminative，过滤是 near-no-op\\n     - T=1.0 (exp-054): delta 从 +3.43pp 崩塌到 0.00pp（D064 corrected），温度敏感性极端\\n     - Multi-Temp (exp-055): ✅ 完成，delta=+0.00pp (b=5,c=5 完美对称), SC=57.84%. 混合 T=0.3/0.7/1.2 各 4 traces 未改善 SICA。附带发现：multi-temp 提升 SC baseline (+3.4pp vs 单温度 54.41%)，说明混合温度对 majority voting 有帮助，但 SICA constraint extraction 无法利用这种 diversity → bottleneck 在 extraction 而非 trace diversity\\n   - 原 6 种：contrastive prompting, cross-model extraction, generational scaling, solver-guided refinement, consistency filtering, cross-trace UNSAT\\n   - 9 种修复涵盖 prompting / architecture / capability / verification / diversity / filtering 全维度，全部失败 → trap is fundamental\\n\\n## D070/D074 Update: Method-Level Interventions Also Fail — \\\"Fundamental Limitation\\\" Confirmed\\n\\n### Three Method Lines × Two Datasets = All Negative (D074)\\n\\nD070 从纯 analysis 升级为 analysis + method paper，但三条方法线全面失败（D074 确认），反而强化了原始 analysis 结论。\\n\\n**方法×数据集完整结果**：\\n| Method | FOLIO-204 | LogiQA-200 | Failure Mode |\\n|--------|-----------|------------|--------------|\\n| ICG (Independent Constraint Gen.) | Δ=-2.0pp (3-seed: -2.0/+1.5/-1.0, mean=-0.5pp±1.8pp, 噪声) | Δ=-0.5pp | Neutral — 独立约束质量≈trace-sourced约束 |\\n| Contrastive (Pro/Con Scoring) | Δ≈-16pp | Δ≈-7pp (interim) | Harmful — 26% degenerate scoring, pro/con 不平衡 |\\n| Debate (Proposer/Critic) | Δ=-18.6pp | Δ≈-28pp (interim) | Catastrophic — 7B 模型角色扮演严重退化推理 |\\n\\n**三种失败模式的分析价值**（论文 \\\"Why Methods Fail\\\" section）：\\n1. **ICG (neutral)**: 独立于 traces 生成的约束不比 trace-sourced 约束更好。说明 bottleneck 不仅是 \\\"约束来自 traces\\\"，而是模型的推理偏差从问题理解阶段就存在——独立约束和 trace-sourced 约束继承相同的 model bias。\\n2. **Contrastive (harmful)**: 强制 pro/con 评估引入 degenerate scoring（26% 问题无法有效区分）。7B 模型无法可靠生成平衡的对立约束——pro 约束系统性多于 con（94 pro vs 65 con），confirmation bias 从约束提取转移到了约束生成。\\n3. **Debate (catastrophic)**: Proposer/Critic/Defense 多角色链在 7B 模型上导致答案质量严重退化。辩论不仅未增加多样性，反而引入了角色扮演的额外认知负担。同模型辩论 = 同源性 + 角色扮演退化，双重损失。\\n\\n**Scale limitation caveat**: 所有方法测试在 7B 模型上。7B 模型生成 Z3 格式 FOL 约束的能力不足（ICG 多题 \\\"0/N constraints parsed\\\"）。14B+ 模型可能有不同结果——这既是 limitation 也是 future work 入口。\\n\\n### κ Generalization — Independence-Accuracy Trade-off (D075, CAPSTONE FINDING)\\n\\nexp-077 测量三种聚合方式在 Mistral-7B FOLIO-204 上的 κ 和 Eff-K：\\n| 聚合方式 | Fleiss' κ | Eff-K | 名义 K |\\n|----------|----------|-------|--------|\\n| Self-Consistency | 0.4384 | 2.02 | 10 |\\n| Diverse-Prompt | 0.4030 | 2.21 | 12 |\\n| LLM-Debate | 0.1549 | 4.44 | 12 |\\n\\n结合 exp-076 Debate Δ=-18.6pp 的准确率数据，揭示**同模型框架下的 fundamental independence-accuracy trade-off**：\\n- **SC/Diverse-Prompt**: κ~0.4，traces 高度相关但准确率正常。换 prompt 策略不改善独立性（Δκ=0.04）。\\n- **Debate**: κ=0.15，成功打破 trace 相关性（Eff-K 从 2.0 跃升到 4.4），但准确率崩溃 -18.6pp。低 κ 不代表\\\"更独立的推理\\\"——是 disagreement amplification（系统性噪声）。\\n- **Trade-off 本质**: 同一模型的推理能力是固定的。要么输出一致（高 κ, 正确但不独立），要么输出分歧（低 κ, 独立但不正确）。Condorcet Jury Theorem 要求 both independent AND accurate，同模型框架下无法同时满足。\\n\\n**论文叙事升级**: 从 \\\"methods fail\\\" → \\\"independence-accuracy trade-off is fundamental to same-model reasoning\\\"。突破瓶颈需要跨模型方案（不同模型天然更独立），Oracle 实验（gold FOL 来自外部知识源）已间接验证了这一点。\\n\\n### New Claim 6 (D070/D074)\\n\\n6. **Method-Level Interventions Cannot Break the Bottleneck**: 三种针对 independence bottleneck 不同环节的方法（ICG→循环依赖, Contrastive→confirmation bias, Debate→trace 同质性）在 2 个数据集上全部失败。加上之前 9 种 prompt-level 修复，共 12 种修复尝试全败。这证明 independence bottleneck 不是单一环节的问题，而是 same-model self-extraction 的根本性限制。\\n\\n### New Claim 7: Symbolic Confirmation Bias (D082 — CORE FINDING)\\n\\n7. **Symbolic Confirmation Bias**: LLM 从 CoT traces 提取的 FOL 约束系统性确认 trace 自身（可能错误的）答案，而非独立验证 ground truth。\\n   - SICA 判对题：gold constraint 78.1%，bias ratio = 0.28\\n   - SICA 判错题：错误 constraint 83.3%，bias ratio = **4.97×**\\n   - 97.6% SICA 错误与 SC 错误完全重合\\n   - SICA 翻盘的 12 例来自 minority trace diversity（43% gold support），不是 symbolic reasoning\\n   - **因果链**：模型推理→答案→从含答案 trace 提取 FOL→约束确认答案→聚合≈SC\\n   - **CEGIS 验证**：迭代精炼 R1 +3.43pp < 原始 SICA +4.9pp → 约束一致性不是瓶颈，偏向性才是\\n   - **Quality Ladder 验证**：L1 ≈ L0 << L3 → bottleneck 在 traces（同源输入），不在 extractor\\n\\n### New Claim 8: Process-κ (D082 — NEW METRIC)\\n\\n8. **Process-Level Independence (Process-κ)**: answer-κ 低估真实独立性瓶颈。CoT 推理过程相似性远高于答案一致性。\\n   - Mistral-7B FOLIO-204：CoT cosine similarity **0.69** >> answer-κ **0.41**\\n   - 两者几乎无相关性：r = -0.06, p = 0.36\\n   - 仅 **9.3%** trace 对是\\\"殊途同归\\\"（同答案不同路径）\\n   - answer-κ 是 true independence bottleneck 的 lower bound\\n   - 适用于所有 LLM trace aggregation 方法，不限于 SICA\\n\\n## D082/D085: Comprehensive Method Exhaustion — 25+ ALL Fail\\n\\nD080 启动全方向并行探索（Wave 1-3），在 D074 的 12 种修复基础上又测试 13+ 新干预：\\n\\n| 方法 | 类型 | 结果 | 关键数据 |\\n|------|------|------|----------|\\n| PROVE 代码验证 | paradigm shift | ❌ | Code gen 15.2%, accuracy=random |\\n| CEGIS 迭代精炼 | multi-round | ❌ | R1 +3.43pp < SICA +4.9pp |\\n| DeepConf 置信度 | filtering | ❌ | logprob 与正确性零相关 |\\n| Cross-model SICA | cross-model | ❌ | Δ=-0.49pp despite lower κ |\\n| Problem Perturbation | input diversity | ❌ | κ 升至 0.696 (反效果) |\\n| MIN-UNSAT | solver objective | ❌ | 49.5% < SC 54.4% |\\n| κ-aware SC | voting rule | ❌ | 11/11 Δ=0 |\\n| Z3 Trace Filter | trace filtering | ❌ | negative |\\n| Bootstrapped Gold | iterative | ❌ | negative |\\n| Selective Abstention | diagnostic | ⚡ | AUROC=0.673, +4.4pp@80%cov |\\n\\n**D085 总结**: 9 prompt-level + 3 method-level + 13 新方向 = **25+ 干预全部 negative**。Independence bottleneck 在 same-model self-extraction 框架下无解，所有维度（diversity/architecture/capability/verification/filtering/voting/solver/paradigm）已穷尽。\\n\\n### Updated Headline Result (D085)\\n\\n\\\"Across 6+ models and 4 domains, symbolic consensus aggregation shows no statistically significant positive effect. 25+ interventions spanning prompt engineering, method-level redesign (ICG, Contrastive, Debate), solver modifications, cross-model aggregation, code-based verification, and iterative refinement all fail. We identify the root cause as Symbolic Confirmation Bias: self-extracted FOL constraints systematically confirm the trace's own answer (bias ratio 4.97× on incorrect problems), making symbolic aggregation equivalent to majority voting. Process-level analysis reveals reasoning paths are far more homogeneous than answers suggest (cosine similarity 0.69 vs answer-κ 0.41). The one method that breaks trace correlation (Debate: κ 0.44→0.15) does so at catastrophic accuracy cost (-18.6pp), revealing a fundamental independence-accuracy trade-off. Oracle constraints prove the aggregation mechanism works (+14.22pp, p<0.001), localizing the bottleneck entirely to self-extraction quality.\\\"\\n\\n### Updated Story Spine (D074)\\n\\n- **Problem**: [unchanged]\\n- **Theoretical lens**: [unchanged]\\n- **Systematic evaluation**: [unchanged]\\n- **Regime characterization**: [unchanged]\\n- **Remediation failures strengthen thesis (D085 FINAL)**: 9 prompt-level + 3 method-level + 13 new directions = **25+ interventions** across ALL dimensions (diversity/architecture/capability/verification/filtering/voting/solver/paradigm), all fail → bottleneck is fundamental and exhaustively proven\\n- **Method failure analysis**: Three methods targeting different bottleneck aspects show three distinct failure modes (neutral/harmful/catastrophic), revealing that the bottleneck operates at multiple levels simultaneously\\n- **Independence-accuracy trade-off (HERO FINDING, D075)**: Debate breaks trace correlation (κ 0.44→0.15, Eff-K 2.0→4.4) but accuracy collapses (-18.6pp/-23.0pp). Same-model traces can be independent OR accurate, not both.\\n- **NEW — Symbolic Confirmation Bias (CORE FINDING, D082)**: Root cause identified — self-extracted FOL constraints systematically confirm the trace's own answer (bias ratio 4.97× on incorrect problems). Causal chain: model reasons → answer → FOL extraction confirms answer → aggregation ≈ SC. This is WHY 25+ methods fail.\\n- **NEW — Process-κ (NEW METRIC, D082)**: CoT reasoning similarity (0.69) >> answer-κ (0.41), r=-0.06. Only 9.3% of trace pairs are \\\"convergent reasoning.\\\" answer-κ underestimates the true bottleneck. Novel metric applicable to all LLM trace aggregation.\\n- **Actionable contribution**: C0+SC diagnostic + κ-based Eff-K estimation = zero-cost deployment toolkit. κ analysis shows SC itself has a scaling ceiling (Eff-K ≈ 2 means K>12 traces yield diminishing returns).\\n- **Universal across architectures (D078)**: Three families: Mistral-7B κ=0.438, LLaMA-8B κ=0.412, Qwen2.5-7B κ=0.658, Qwen2.5-14B κ=0.738. Family effect (Δκ=0.22) >> scale effect (Δκ=0.08).\\n- **Headline (D085)**: Independence bottleneck is structural, universal across architectures, and rooted in Symbolic Confirmation Bias. 25+ interventions spanning all conceivable dimensions fail. Process-κ reveals reasoning homogeneity far exceeds answer-level agreement. The independence-accuracy trade-off constrains all same-model trace aggregation.\\n\\n## Core Insight (D060 Updated — Dual Bottleneck)\\n\\n**Dual Requirement Framework**: SICA 效应需要同时满足两个条件，缺一不可：\\n1. **Sufficient Independence** (Eff-K > threshold): traces 需要提供足够多的独立视角\\n2. **Sufficient Quality** (SC > ~50%): traces 需要有足够的正确率，否则约束是噪声\\n\\nCondorcet Jury Theorem 要求投票者独立且 p>0.5。同模型采样的 reasoning traces 严重违反独立性假设（Fleiss' κ = 0.21–0.82，Eff-K 仅 1.20–3.63），解释了为什么简单增加 K 或添加符号约束不能突破 SC 的天花板。\\n\\n实验数据完美支持 dual requirement（κ 使用统一脚本 compute_fleiss_kappa_unified.py，SC/Δpp 使用 registry 原始值）：\\n- **Qwen family**: κ=0.66-0.82, Eff-K≈1.20-1.46（独立性不足）→ all near-zero delta，无论 SC 多高\\n- **Mistral-7B FOLIO**: κ≈0.46, Eff-K≈2.0（中等独立性）+ SC≈55%（中等质量）→ +3.43pp best seed, mean +2.12pp (2/3 seeds positive, 1 null)\\n- **Mistral-7B PW-600**: κ=0.20, Eff-K=3.76（最高独立性）但 SC=39%（质量不足）→ -2.83pp\\n- 只有 Goldilocks zone（中等 Eff-K + 中等 SC）出现正向 delta\\n- **Dual bottleneck 直接验证 (exp-055)**：Multi-temp κ=0.427 Eff-K=2.11（比单温度 κ≈0.46 Eff-K≈2.0 更独立）但 delta=0.00pp → 提高 independence 不够，还需要 extraction quality\\n- **T sensitivity 孤立尖峰 (4/4 complete, D064 corrected)**：T=0.3(Δ=-1.47), T=0.5(Δ=-0.98), T=0.7(Δ=+3.43, κ=0.460, Eff-K=1.98), T=1.0(Δ=0.00, κ=0.394, Eff-K=2.25)。T=0.7 孤立尖峰更突出。T=0.7 SC=55.88%（最低）→ entropy 最高 → SICA 操作空间最大。温度效应与 SC 效应互为 confound，论文需讨论\\n- **Thinking mode κ=0.913, Eff-K=1.09 (exp-028b)**：近乎确定性。思维模式让 traces 更一致 → 独立性更差。\\\"更好的推理\\\"反而加剧 independence bottleneck。\\n\\n**κ 是 model-level 稳定属性**：统一处理后 Mistral 三 seed κ 收敛至 0.457-0.460（之前 0.41-0.50 差异是非标准 answer 处理的 artifact）。κ 跨 seed 几乎相同，但 delta 差异大（+3.43 vs +2.94 vs 0.00）→ seed-level constraint quality variance 主导，非 κ。\\n\\n完整 κ 表（⚠️ D062: κ 将用 raw answers 重算，当前 unified 值为临时值。Qwen 无变化，Mistral 条件将更新）：\\n| Exp | Model | κ(unified→raw pending) | Eff-K | SC%(registry) | Δpp(registry) |\\n|-----|-------|------------|-------|---------------|---------------|\\n| exp-028b | Qwen3-14B thinking | 0.913 | 1.09 | ~84% | ~0 |\\n| exp-038 | Qwen-14B LogiQA | 0.821 | 1.20 | 78.50 | -0.50 |\\n| exp-027 | Qwen3-14B | 0.773 | 1.26 | 84.31 | +0.49 |\\n| exp-036 | Qwen2.5-14B | 0.744 | 1.31 | 75.49 | +0.25 |\\n| exp-035 | Qwen2.5-7B | 0.658 | 1.46 | 76.47 | -0.49 |\\n| exp-049b | Mistral-7B LogiQA | 0.512 | 1.81 | 51.00 | +0.50 |\\n| exp-057 | Mistral-7B T=0.3 | 0.502 | 1.84 | 58.33 | -1.47 |\\n| exp-058 | Mistral-7B T=0.5 | 0.516 | 1.80 | 58.33 | -0.98 |\\n| exp-033 | Mistral-7B s42 | 0.460 | 1.98 | 55.88 | +3.43 |\\n| exp-052 | Mistral-7B s123 | 0.457 | 1.99 | 54.41 | +2.94 |\\n| exp-053 | Mistral-7B s456 | 0.457 | 1.99 | 55.88 | 0.00 |\\n| exp-055 | Mistral-7B multi-T | 0.427 | 2.11 | 57.84 | 0.00 |\\n| exp-054 | Mistral-7B T=1.0 | 0.394 | 2.25 | 55.39 | 0.00 |\\n| exp-046 | Mistral-7B PW-600 | 0.200 | 3.76 | 39.33 | -2.83 |\\n注：κ 基于 T/F/U 三类归一化，Mistral-7B 约 12-16% traces 被归一化（Qwen 100% valid）。Mistral SC/Δpp 已更新为 D064 tiebreaking 修正值；Qwen 不受影响。\\n\\nOracle control (+14.22pp) 证明 MAX-SAT 聚合机制本身有效，但自提取约束仅利用了 24% 的理论上限。Discriminative filtering 实验揭示关键机制：~92% 约束 ARE discriminative，但过滤掉 ~8% non-discriminative 约束后 delta 不变（0 gains）。问题不在约束缺乏判别力，而在于 discriminative constraints 的区分方向与模型偏差一致（confirmation bias）。\\n\\n**Remediation insight (D060)**: 9 种修复尝试全部失败，包括直接靶向 independence（multi-temp diversity, exp-055: Eff-K 从 2.0→2.11 但 delta 仍为 0）和 constraint quality（discriminative filtering）。这证明 bottleneck 不是简单的 diversity 或 quality 问题，而是 same-model self-extraction 的根本性限制。\\n\\n**Key evidence**:\\n- **Condorcet independence quantification (统一脚本, 公式: Eff-K=K/(1+(K-1)κ))**: Mistral-7B FOLIO κ≈0.46 (Eff-K≈2.0, 三 seed 高度稳定), Mistral-7B PW-600 κ=0.200 (Eff-K=3.76), Qwen2.5-14B FOLIO κ=0.744 (Eff-K=1.31), Qwen2.5-14B LogiQA κ=0.821 (Eff-K=1.20), Qwen3-14B κ=0.773 (Eff-K=1.26), Qwen2.5-7B κ=0.658 (Eff-K=1.46). 跨模型清晰: Qwen Eff-K≈1.2-1.5→0 gain, Mistral FOLIO Eff-K≈2.0→variable gain, Mistral PW Eff-K=3.76 but SC too low→negative. κ stable across seeds (0.457-0.460), delta varies → seed-level constraint quality dominates.\\n- **Oracle control (exp-031)**: Gold FOL + MAX-SAT = 89.71% vs SC 75.49% (+14.22pp, p=2.0e-7). Unknown-type +31.9pp.\\n- **Two-layer constraint analysis**: 43% trivially_satisfied (taxonomy: satisfied by ALL answers) vs ~8% non-discriminative (filtering: same MAX-SAT score). Difference: trivially_satisfied constraints can still have different satisfaction DEGREES. Removing the 8% yields 0 gains → problem is not quality but confirmation bias direction.\\n- **K sensitivity (non-monotonic peak at K=12, 5/5 complete, D064+D066)**: K=4(-1.47pp), K=8(-1.96pp), K=12(+3.43pp p=0.092 ns), K=16(+1.47pp), K=20(+1.96pp). Peak at K=12, drops at K=16 but partially recovers at K=20. NOT clean inverted-U. K=12 SC=55.88% (post-fix). SC-confound with T sensitivity still holds. SICA at K=4 vs K=12 differs by ~4.9pp despite similar SC — proves SICA extracts different information than SC.\\n- **SC-confound (cross-cutting insight)**: K=12 和 T=0.7 都是 SC 最低 (54.41%) 的配置 → SICA \\\"最佳超参\\\"可能反映 entropy/operating-window 效应而非 K 或 T 的因果贡献。论文需要讨论这个 confound，但也可以正面利用：SC level 是更基本的预测变量，K 和 T 通过影响 SC 来间接影响 SICA delta。\\n- **T sensitivity (isolated peak, 4/4 complete, D064 corrected)**: T=0.3(Δ=-1.47pp), T=0.5(Δ=-0.98pp), T=0.7(Δ=+3.43pp p=0.092 ns), T=1.0(Δ=0.00pp). NOT smooth inverted-U — T=0.7 is an isolated spike. T=0.7 has lowest SC (55.88%) → highest entropy → largest SICA operating window. Temperature and SC effects confounded. Strengthens fragility narrative.\\n- **Regime boundary**: Qwen-14B (SC=75.49%) Δ=-0.98pp vs Mistral-7B (SC=55.88%) Δ=+3.43pp p=0.092 ns\\n- **Type C failure (exp-046)**: Mistral PW-D5 SC=39.33%, Δ=-2.83pp, p=0.010, κ=0.210, Eff-K=3.63, contradiction rate 5.5%. Highest Eff-K yet worst delta → independence alone insufficient when SC too low.\\n- **Seed replication (D064+D066)**: 2/3 seeds positive but **0/3 significant** after tiebreaking correction: s42 Δ=+3.43pp p=0.092, s123 Δ=+2.94pp p=0.070, s456 Δ=0.00pp p=1.0. Mean +2.12pp. Only significant McNemar effects are NEGATIVE: exp-046 Δ=-2.83pp p=0.014, exp-039 Δ=-2.50pp p=0.011. Paper must frame as \\\"positive directional trend\\\" not \\\"significant positive effect\\\".\\n- **Nine remediation failures (ALL CONFIRMED)**: contrastive prompting, cross-model, generational scaling, solver-guided, consistency filtering, cross-trace UNSAT, discriminative filtering (0 gains), T=1.0 (delta collapse +3.43→0.00pp, D064 corrected), multi-temp (delta=+0.00pp, b=5 c=5). All 9 failed → trap is fundamental, bottleneck is structural.\\n- **Entropy decomposition (VERIFIED 2026-05-19)**: High-entropy proportion: Mistral FOLIO 38% (78/204) vs Qwen FOLIO 18% (37/204) vs Qwen LogiQA 12% (23/200). SICA on high-entropy: Mistral FOLIO s42 +12.8pp, s123 +9.1pp, s456 -1.3pp; Qwen FOLIO -8.2pp; all others negative. Low-entropy: SICA≈SC across all 8 experiments (Δ≈0). Entropy decomposition reveals regime-dependent mechanism, NOT universal diagnostic.\\n- **Confirmation bias quantification**: ⚠️ \\\"62.3%\\\" and \\\"28.6%\\\" confirmed NOT present in any .tex file — likely hallucinated in earlier draft. DO NOT USE. Replace with verified metrics from experiment outputs only.\\n\\n## Story Spine (D059 Updated)\\n\\n- **Problem**: LLMs' reasoning can be improved by sampling multiple chains-of-thought and aggregating via majority voting (self-consistency). Recent work proposes symbolic augmentation: extract formal constraints from traces and use SAT solvers for answer selection. But does symbolic aggregation actually outperform simple voting?\\n- **Theoretical lens**: Condorcet Jury Theorem requires voter independence. We quantify trace independence via Fleiss' κ and show Effective-K << nominal K. This explains the fundamental limitation of same-model trace aggregation.\\n- **Systematic evaluation**: SICA (MAX-SAT over FOL constraints) across 3 domains × 5 model families. Oracle control separates extraction vs aggregation failure. Discriminative filtering reveals ~92% constraints are discriminative, yet SICA gains are fragile — confirmation bias, not constraint quality, is the bottleneck.\\n- **Regime characterization**: Three failure modes (Type A/B/C) + narrow Goldilocks zone. C0+SC as deployment diagnostic.\\n- **Remediation failures strengthen thesis**: 9 targeted interventions (prompting, architecture, capability, verification, diversity, filtering) all fail to close the oracle gap, proving the bottleneck is fundamental to same-model self-extraction.\\n- **Headline result (D066 McNemar corrected)**: \\\"Across 6 models and 4 domains, symbolic consensus aggregation shows no statistically significant positive effect under corrected tiebreaking (best seed +3.43pp, p=0.092). The only significant effects are negative (PW-600: -2.83pp p=0.014, -2.50pp p=0.011). However, entropy decomposition reveals a striking regime-dependent pattern: SICA's entire effect concentrates on high-entropy questions, with +12.8pp in the Goldilocks zone but -2 to -8pp elsewhere. Oracle constraints prove the aggregation mechanism works (+14.22pp, p<0.001), localizing the bottleneck to extraction quality (24% utilization). Condorcet analysis (Eff-K=1.2-2.0 for nominal K=12) explains trace non-independence. Nine remediation strategies all fail, confirming the bottleneck is structural to same-model self-extraction.\\\"\\n\\n## Anticipated Reviewer Concerns & Defensive Experiments\\n\\n1. **\\\"Gains not statistically significant\\\"** → Correct: no positive effect reaches significance (best p=0.092). This IS the finding. Oracle p=2.0e-7 proves the mechanism works; the insignificance of self-extraction gains demonstrates the extraction bottleneck. Regime pattern (8 entropy conditions) provides systematic evidence beyond any single p-value.\\n2. **\\\"Only one positive result (exp-033)\\\"** → Seed replication: 2/3 positive (s42 +3.43pp, s123 +2.94pp), 1/3 null (s456 0.00pp). Mean +2.12pp. Effect IS real but fragile — the fragility itself IS the finding.\\n3. **\\\"Condorcet framework is trivial\\\"** → Fleiss' κ quantification is novel in SC/SICA context. Eff-K is actionable: tells practitioners how many truly independent traces they get.\\n4. **\\\"Multi-temp / filtering should work\\\"** → We tried both. Multi-temp (exp-055): negative. Disc. filtering: 0 gains. T=1.0: delta collapse. These failures STRENGTHEN the structural bottleneck thesis.\\n5. **\\\"Only Qwen models\\\"** → 5 families: Qwen-14B, Mistral-7B, LLaMA-8B, DeepSeek-R1-7B, QwQ-32B.\\n6. **\\\"Only logic domain\\\"** → FOLIO + ProofWriter + LogiQA + StrategyQA + ARC-Challenge. Type B (domain formalizability) is itself a finding.\\n7. **\\\"Oracle is unfair comparison\\\"** → Diagnostic tool, not competing method. Separates extraction from aggregation.\\n8. **\\\"MAX-SAT is over-engineering\\\"** → exp-013: MaxSAT ≈ count-only. This IS the independence bottleneck evidence.\\n9. **\\\"Self-extraction confound\\\"** → Oracle control resolves completely.\\n10. **\\\"Published methods achieve gains (DyLoS, Aristotle, FoVer)\\\"** → Different paradigm (external verifiers/trained extractors). We characterize same-model self-extraction.\\n11. **\\\"C0 is trivially derived\\\"** → Zero-cost early stopping. Practical value.\\n12. **\\\"Why not just use a reasoning model?\\\"** → QwQ-32B: C0<5%, SICA≡SC.\\n13. **\\\"Random tiebreak baseline\\\"** → exp-003: SICA tiebreak 80% vs random 50%.\\n14. **\\\"Method improvement is incremental\\\"** → Grounded in diagnosis (independence + taxonomy), not ad-hoc.\\n15. **\\\"Weighted SC is simpler\\\"** → exp-016 planned. Weighted SC doesn't address independence.\\n16. **\\\"Within-model ICL transition contradicts regime theory\\\"** → exp-050b (SC=57.79%, Δ=-3.52pp): ICL changes trace generation characteristics, not just SC level. Paper must distinguish \\\"same model, different prompt\\\" from \\\"same model, same prompt, different accuracy.\\\"\\n\\n## Working Title\\n**\\\"Beyond Self-Consistency: How Trace Independence Limits Symbolic Consensus in LLM Reasoning\\\"**\\n(Alternatives:\\n- \\\"The Independence Bottleneck: Why Self-Extracted Symbolic Constraints Cannot Beat Majority Voting\\\"\\n- \\\"Symbolic Consensus Under the Condorcet Lens: Independence, Extraction, and the Limits of Self-Aggregation\\\")\\n\\nNOTE (Dream D037): Title MUST be scoped to \\\"self-extracted constraints\\\" / \\\"SICA\\\". Published methods (DyLoS, Aristotle, FoVer) use different approaches.\\n\\n## Paper Structure (EMNLP 8pp + appendix)\\n\\n### Main Tables\\n- T1: Main Results — models × domains, SC% / SICA% / Δpp / p-value, regime boundary\\n- T2: Oracle Control — Gold-FOL+MAX-SAT vs SC vs SICA-self, causal separation\\n- T3: Independence Quantification — Fleiss' κ / Eff-K / trace agreement per model\\n- T4: Extraction Error Taxonomy — trivially_satisfied / discriminative / both_wrong rates\\n- T5: K Sensitivity — K=4/8/12/16/20, non-monotonic (peak K=12, K=20 recovers), SC confound\\n\\n### Main Tables (continued)\\n- T6: Method-Level Intervention Results — 3 methods × 2 datasets, SC% / Method% / Δpp, failure mode classification\\n- T7: κ Generalization — SC / Debate / Diverse-Prompt κ and Eff-K (from exp-077, pending)\\n\\n### Main Figures\\n- F1: Method Pipeline (SICA + oracle control design)\\n- F2: SC Accuracy vs SICA Δ scatter (hero figure, regime boundary)\\n- F3: K Sensitivity with diversity metrics (K vs Δ, K vs Eff-K)\\n- F4: Extraction error breakdown (stacked bar)\\n- F5: Method intervention failure modes (grouped bar: ICG/Contrastive/Debate × FOLIO/LogiQA)\\n\\n### Appendix\\n- K ablation details, temperature sensitivity, per-domain results, overhead analysis\\n- Entropy-conditioned analysis (continuous scatter + bin sensitivity)\\n- Six remediation strategy details\\n- Confirmation bias quantification\\n- Seed replication analysis\\n- QwQ-32B / DeepSeek-R1 negative control\\n\\n## Claim Risk Notes (D059)\\n- **Seed replication**: 0/3 significant after D066 correction (p=0.092, 0.070, 1.0). 2/3 positive trend, 1/3 null. Mean +2.12pp. Frame as \\\"directional trend, not significant effect\\\" — fragility IS the finding.\\n- **Method claims DEAD (D060)**: All three method improvements failed. Paper is pure analysis. 9 remediation failures are EVIDENCE, not limitation.\\n- **Condorcet novelty**: ✅ VERIFIED. arXiv:2409.00094 applies CJT to cross-model LLM ensembles (different angle). No prior work applies Fleiss' κ or Eff-K to within-model SC traces. Our framing is novel.\\n- **exp-050b complication**: ICL transition Δ=-3.52pp at SC=57.79% complicates simple \\\"SC determines SICA.\\\" Explain via trace generation characteristic change.\\n- **Variable naming inconsistency**: 56.4% cross-trace pairs share zero Z3 variables. Key mechanism evidence.\\n\\n## Required Citations (minimum 30 references)\\n\\n- **SC & extensions**: Wang et al. 2023 (SC), Chen et al. 2023 (USC), Loo et al. 2025 (SC scaling plateaus), Taubenfeld et al. 2025 (weighted SC), DiVeRSe (Li et al. 2023)\\n- **Neuro-symbolic reasoning**: DyLoS (EACL 2026), Aristotle (ACL 2025), FoVer (TACL 2025), LogicAgent (2025), Logic-LM (Pan et al. 2023), LINC (Olausson et al. 2023)\\n- **Condorcet/voting theory**: Condorcet 1785, Austen-Smith & Banks 1996, **arXiv:2409.00094 (Examining Independence in Ensemble Sentiment Analysis, Sept 2024)** — closest prior work, applies CJT to cross-model LLM ensembles, finds independence violation. Our novelty: within-model trace independence + Fleiss' κ quantification + Eff-K + connection to symbolic aggregation\\n- **Test-time compute**: Snell et al. 2025, DeepSeek-R1, Diversity-Aware Training\\n- **Verification & reranking**: ORM (Cobbe et al. 2021), PRM (Lightman et al. 2023), Math-Shepherd\\n- **Constraint satisfaction**: SATBench (EMNLP 2025), LLM Meets Constraint Propagation (IJCAI 2025)\\n- **Debate & multi-agent**: Liang et al. 2023, Du et al. 2023\\n\\n## Additional Reviewer Concerns (D070/D074 Methods)\\n\\n17. **\\\"Why not use a larger model for constraint generation?\\\"** → Valid. All methods tested at 7B scale. ICG constraint parsing failures + Debate role-play degradation may be scale-dependent. This is explicitly noted as limitation and future work. The contribution is diagnosing the bottleneck and showing it's not trivially fixable, not claiming no fix exists at any scale.\\n18. **\\\"Only tested one model (Mistral-7B) for methods\\\"** → Methods are interventions on the extraction pipeline, not the base model. Testing on the same model that showed the clearest Goldilocks signal (Mistral-7B FOLIO) is the strongest test — if methods can't improve the best-case scenario, they won't help elsewhere.\\n19. **\\\"ICG multi-seed shows 1/3 positive\\\"** → Magnitudes (-2.0, +1.5, -1.0) are within SC baseline noise (3.5pp cross-seed). Mean ≈-0.5pp, std=1.8pp. No statistical significance. Properly framed as \\\"noise-level, neither improving nor degrading.\\\"\\n20. **\\\"Debate working in other papers\\\"** → Multi-agent debate literature uses diverse models or much larger models. Same-model 7B debate is a different regime. Our finding is specifically about same-model self-extraction limitations.\\n\\n## Claim Scoping Rules\\n- n=60 conditions: \\\"suggestive/consistent with\\\" NOT \\\"confirming\\\"\\n- n≥200 conditions: can \\\"confirm\\\"\\n- Combined N>1,300: acceptable if breakdown clearly stated\\n- Method claims: must show statistically significant improvement OR clear directional improvement with analysis\\n- \\\"Independence bottleneck\\\" framing: systematic quantification + theoretical grounding\\n\", \"total_chars\": 31186, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "d4f8bb98-c0e4-41f7-839b-c73143d1396a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora"
}
```

</details>

---


### Tool call

_source line 8811 · 2026-05-20T09:35:48.556Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01Hr4b3Q7eVT9uLLGKcpnPsG`</summary>

```json
{
  "project": "symb_invariant_consensus",
  "file": "writing_plan.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "77cf5a4e-6311-4f0d-90dd-2f1b5fa1f95c",
  "isSidechain": false,
  "requestId": "req_011CbDbPqJj9ZYvDsx3j3Yxz",
  "type": "assistant",
  "uuid": "32cbf480-c5bb-4a08-82ea-0514a848ebaf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Bvksz7RVr2DMr5TjduKFiV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 939,
      "cache_read_input_tokens": 134187,
      "output_tokens": 273,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 939,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 273,
          "cache_read_input_tokens": 134187,
          "cache_creation_input_tokens": 939,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 939
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

_source line 8812 · 2026-05-20T09:35:48.569Z_

<details><summary>↩ Tool result · `toolu_01Hr4b3Q7eVT9uLLGKcpnPsG`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/writing_plan.yaml\", \"content\": \"# Writing Plan — symb_invariant_consensus\\n# Generated: 2026-05-19T20:30:00Z\\n# Full Draft: Independence Bottleneck — \\\"Fundamental Limitation\\\" paper\\n# Target: EMNLP 2026 ARR May cycle\\n# Paper Agent Step 1 output\\n\\nmeta:\\n  venue: EMNLP 2026\\n  track: main (ARR May cycle)\\n  template: docs/paper/acl.sty\\n  template_note: \\\"ACL/EMNLP shared template already in paper directory\\\"\\n  page_limit: 8\\n  deadline: 2026-05-25\\n  title: >\\n    Beyond Self-Consistency: How Trace Independence Limits\\n    Symbolic Consensus in LLM Reasoning\\n  core_claim: >\\n    Same-model self-extraction of symbolic constraints inherits trace\\n    correlation (Fleiss' κ=0.21–0.82, Eff-K=1.20–3.62 for nominal K=12),\\n    creating a structural independence bottleneck. Oracle gold-FOL yields\\n    +14.22pp (p<0.001) proving aggregation is sound, but self-extraction\\n    captures only 24%. κ generalization across aggregation methods reveals\\n    a fundamental independence-accuracy trade-off: Debate reduces κ from\\n    0.44→0.15 (Eff-K 2→4.4) but collapses accuracy by -18.6pp. Same-model\\n    methods cannot increase independence without degrading the signal that\\n    makes aggregation useful.\\n  paper_type: \\\"Fundamental limitation analysis (Condorcet framework + empirical diagnosis + 12 remediation failures)\\\"\\n  framing: \\\"Independence Bottleneck — structural limitation of same-model self-extraction\\\"\\n  created_at: 2026-05-19T20:30:00Z\\n\\n# ──────────────────────────────────────────────\\n# Contributions (5)\\n# ──────────────────────────────────────────────\\ncontributions:\\n  - id: C1\\n    label: \\\"Independence Bottleneck Quantification\\\"\\n    status: VERIFIED\\n    claim: >\\n      Fleiss' κ=0.21–0.82 (instruction-tuned), 0.91 (thinking mode).\\n      Eff-K=1.20–3.62 at K=12. Mistral 4-seed κ=0.41–0.51 (stable).\\n      Qwen Eff-K≈1.2–1.5 → near-zero Δ; Mistral PW Eff-K=3.62 but\\n      SC=39% → negative Δ. Dual requirement: sufficient Eff-K AND SC.\\n    evidence: \\\"Table 3, §5.1\\\"\\n\\n  - id: C2\\n    label: \\\"Oracle Gap Localizes Extraction Bottleneck\\\"\\n    status: VERIFIED\\n    claim: >\\n      Gold FOL: +14.22pp FOLIO (p<0.001), +11.50pp PW (p<0.001).\\n      Self-extraction captures 24% of oracle ceiling (best seed +3.43pp\\n      vs +14.22pp). Aggregation mechanism sound; extraction quality is\\n      the binding bottleneck.\\n    evidence: \\\"Table 1 oracle rows, §4.3\\\"\\n\\n  - id: C3\\n    label: \\\"Regime-Dependent Effect with 4-Seed Replication\\\"\\n    status: VERIFIED\\n    claim: >\\n      Intermediate-SC (~50–55%): best seed +3.43pp (p=0.092, ns);\\n      4-seed mean +1.47pp; 2/4 marginal (p<0.10), 0/4 significant.\\n      Type A (SC≥60%): 9 conditions N>2,800, no significant positive;\\n      significant negatives at -2.50pp (p=0.011) and -4.41pp (p=0.093).\\n      Type C (SC≤40%): -2.83pp (p=0.014).\\n    evidence: \\\"Table 1, Figure 2, §4.1–4.3\\\"\\n\\n  - id: C4\\n    label: \\\"Independence-Accuracy Trade-off Is Fundamental\\\"\\n    status: VERIFIED\\n    claim: >\\n      κ generalization (exp-077) reveals why same-model methods must fail:\\n      SC κ=0.44 (Eff-K=2.02); Diverse-Prompt κ=0.40 (Eff-K=2.21, ≈SC);\\n      Debate κ=0.15 (Eff-K=4.44) but Δ=-18.6pp. Methods that increase\\n      independence (Debate) destroy accuracy; methods that preserve accuracy\\n      (ICG, Diverse-Prompt) cannot break correlation. 12 remediations\\n      (9 prompt + 3 method) all fail — not engineering failure but\\n      fundamental trade-off in same-model aggregation.\\n    evidence: \\\"§5.6, Table T7 (κ generalization), method intervention table\\\"\\n\\n  - id: C5\\n    label: \\\"Entropy Decomposition Reveals Regime Mechanism\\\"\\n    status: VERIFIED\\n    claim: >\\n      Low-entropy: SICA≈SC across all 8 conditions (Δ≈0). High-entropy\\n      direction regime-dependent: +12.8pp intermediate-SC, -8.2pp Type A.\\n      Explains dual-channel mechanism (voting diversity + constraint\\n      homogenization).\\n    evidence: \\\"§5.5, entropy analysis\\\"\\n\\n# ──────────────────────────────────────────────\\n# Paper Outline\\n# ──────────────────────────────────────────────\\npaper_outline:\\n  - section: abstract\\n    file: abstract.tex\\n    word_budget: 220\\n    core_bullets:\\n      - \\\"Problem: SC (majority voting) plateaus; CJT explains why — traces lack independence\\\"\\n      - \\\"SICA pipeline evaluated across 6 models, 3 formal reasoning domains, N>3,000, 4-seed replication\\\"\\n      - \\\"Independence quantification: κ=0.21–0.82, Eff-K=1.20–3.62 at K=12\\\"\\n      - \\\"Regime: +3.43pp intermediate-SC (ns), -2.83pp Type C (p=0.014), ~0 Type A\\\"\\n      - \\\"Oracle +14.22pp/+11.50pp proves aggregation sound; self-extraction 24%\\\"\\n      - \\\"12 remediations (9 prompt + 3 method) all fail — bottleneck is structural\\\"\\n      - \\\"C0+SC zero-cost deployment diagnostic; paths forward require independence\\\"\\n    dependencies: [experiments, analysis, method]\\n\\n  - section: introduction\\n    file: introduction.tex\\n    word_budget: 1300\\n    core_bullets:\\n      - \\\"Hook: Test-time compute scaling via SC improves reasoning—but plateaus. Adding more traces yields diminishing returns.\\\"\\n      - \\\"Gap: Neuro-symbolic methods (Logic-LM, DyLoS, FoVer) improve reasoning with external/trained components. Can same-model self-extraction of formal constraints break the SC plateau without external tools?\\\"\\n      - \\\"Insight: CJT requires voter independence. Same-model traces violate this (Eff-K=1.20–3.62 for K=12). Self-extracted constraints inherit the correlation structure.\\\"\\n      - \\\"Evaluation: SICA pipeline + Condorcet analysis + oracle control across 6 models × 3 domains, 4-seed replication\\\"\\n      - \\\"Key result: Oracle +14.22pp proves mechanism works; self-extraction captures 24%. 12 remediations all fail.\\\"\\n      - \\\"Contributions: C1–C5\\\"\\n    dependencies: [experiments, analysis]\\n    figures: [fig1_pipeline]\\n    citation_hints:\\n      - \\\"SC: Wang et al. 2023\\\"\\n      - \\\"SC plateau: Loo et al. 2025\\\"\\n      - \\\"Logic-LM: Pan et al. 2023\\\"\\n      - \\\"DyLoS: Xu et al. 2026\\\"\\n      - \\\"CJT: Condorcet 1785, Ladha 1992\\\"\\n      - \\\"Self-correction parallel: Huang et al. 2024\\\"\\n\\n  - section: related_work\\n    file: related_work.tex\\n    word_budget: 750\\n    core_bullets:\\n      - \\\"SC and extensions: Wang 2023, USC, weighted SC (Taubenfeld 2025), DiVeRSe, scaling plateaus (Loo 2025)\\\"\\n      - \\\"Neuro-symbolic reasoning: Logic-LM, LINC, DyLoS, Aristotle, FoVer — all use external/trained components; we test same-model self-extraction\\\"\\n      - \\\"Condorcet/voting theory: CJT, correlated voters (Ladha 1992), LLM ensembles (Lefort 2024 arXiv:2409.00094, closest prior work)\\\"\\n      - \\\"Verification and reranking: ORM (Cobbe 2021), PRM (Lightman 2023), Math-Shepherd — trained verifier paradigm\\\"\\n      - \\\"Self-X limitations: Huang 2024 self-correction ≈ structural parallel to self-extraction\\\"\\n      - \\\"Debate/multi-agent: Liang 2023, Du 2023 — different regime (multi-model or larger models)\\\"\\n    dependencies: []\\n\\n  - section: method\\n    file: method.tex\\n    word_budget: 1100\\n    subsections:\\n      - id: \\\"sec:condorcet\\\"\\n        title: \\\"Self-Consistency and the Condorcet Independence Assumption\\\"\\n        word_budget: 300\\n        bullets:\\n          - \\\"SC as majority voting: sample K reasoning traces, select most common answer\\\"\\n          - \\\"CJT: K independent voters each with p>0.5 → P(majority correct) → 1 as K→∞\\\"\\n          - \\\"LLM traces violate independence: same model, same prompt, only sampling noise\\\"\\n          - \\\"Eff-K = K/(1+(K-1)κ) via Kish (1965) design effect; κ = Fleiss' kappa (1971)\\\"\\n          - \\\"When Eff-K≈1, additional traces ≈ no new information → SC plateau\\\"\\n      - id: \\\"sec:sica-pipeline\\\"\\n        title: \\\"SICA Pipeline\\\"\\n        word_budget: 400\\n        bullets:\\n          - \\\"Step 1: Generate K reasoning traces at temperature T\\\"\\n          - \\\"Step 2: Extract FOL constraints from each trace at T_ext=0.3\\\"\\n          - \\\"Step 3: Syntactic deduplication across traces\\\"\\n          - \\\"Step 4: Weighted partial MAX-SAT — hard clauses (answer assertion), soft clauses (constraints weighted by occurrence count)\\\"\\n          - \\\"Step 5: Z3 solver evaluates each candidate; answer with highest satisfiable weight selected\\\"\\n          - \\\"Timeout: 10s per candidate answer\\\"\\n      - id: \\\"sec:oracle-design\\\"\\n        title: \\\"Oracle Control Design\\\"\\n        word_budget: 200\\n        bullets:\\n          - \\\"Replace self-extracted constraints with gold FOL annotations (FOLIO) or gold DSL (ProofWriter)\\\"\\n          - \\\"Same Z3 evaluation pipeline; only constraint source changes\\\"\\n          - \\\"Causal intervention: isolates constraint quality from aggregation mechanism\\\"\\n      - id: \\\"sec:method-interventions\\\"\\n        title: \\\"Method-Level Interventions\\\"\\n        word_budget: 150\\n        bullets:\\n          - \\\"ICG: Generate constraints independently of traces (bypass trace-constraint coupling)\\\"\\n          - \\\"Contrastive: Pro/con constraint scoring per candidate answer\\\"\\n          - \\\"Debate: Proposer/Critic/Defense chain before constraint extraction\\\"\\n          - \\\"Each targets a different bottleneck aspect\\\"\\n    dependencies: []\\n    figures: [fig1_pipeline]\\n\\n  - section: experiments\\n    file: experiments.tex\\n    word_budget: 1800\\n    subsections:\\n      - id: \\\"sec:exp-setup\\\"\\n        title: \\\"Experimental Setup\\\"\\n        word_budget: 300\\n        bullets:\\n          - \\\"6 models: Mistral-7B-Instruct-v0.3, LLaMA-3.1-8B-Instruct, Qwen2.5-7B-Instruct, Qwen2.5-14B-Instruct, Qwen3-14B (non-thinking), Qwen3-14B (thinking mode for κ analysis)\\\"\\n          - \\\"3 formal reasoning domains: FOLIO (n=204), ProofWriter depth-5 (n=600), LogiQA (n=200)\\\"\\n          - \\\"Cross-domain diagnostic: StrategyQA (n=200)\\\"\\n          - \\\"Degenerate probes: QwQ-32B (AIME 2024), Qwen2.5-14B (GSM8K)\\\"\\n          - \\\"Default: K=12, T=0.7, T_ext=0.3, Z3 timeout 10s\\\"\\n          - \\\"Metrics: accuracy (%), Δ=SICA−SC (pp), McNemar exact test α=0.05\\\"\\n          - \\\"4-seed replication on primary condition (Mistral-7B FOLIO)\\\"\\n      - id: \\\"sec:main-results\\\"\\n        title: \\\"Main Results: A Regime-Dependent Effect\\\"\\n        word_budget: 500\\n        bullets:\\n          - \\\"Table 1: ~18 conditions grouped by regime + 2 oracle rows\\\"\\n          - \\\"Intermediate-SC (SC~50–55%): Mistral FOLIO best seed +3.43pp (p=0.092 ns); 4-seed mean +1.47pp; Mistral LogiQA +0.50pp\\\"\\n          - \\\"Type A (SC≥60%): 9 conditions N>2,800; no significant positive effect\\\"\\n          - \\\"  Significant negatives: Qwen14B PW -2.50pp (p=0.011); Mistral PW -2.83pp (p=0.014)\\\"\\n          - \\\"  LLaMA FOLIO -4.41pp (p=0.093, marginal)\\\"\\n          - \\\"  Qwen3-14B FOLIO -0.49pp, PW +0.67pp — generational scaling does not help\\\"\\n          - \\\"Type C (SC≤40%): Mistral PW-D5 Δ=-2.83pp p=0.014 — SICA significantly hurts\\\"\\n          - \\\"Degenerate: C0<5% → SICA≡SC by construction\\\"\\n          - \\\"Figure 2: SC vs Δ scatter showing regime boundaries\\\"\\n      - id: \\\"sec:oracle\\\"\\n        title: \\\"Oracle Control: Aggregation Is Sound\\\"\\n        word_budget: 250\\n        bullets:\\n          - \\\"FOLIO: oracle-SICA 89.71% vs SC 75.49% (+14.22pp, p<0.001)\\\"\\n          - \\\"ProofWriter: oracle-SICA 86.67% vs SC 75.17% (+11.50pp, p<0.001)\\\"\\n          - \\\"Self-extraction captures only 24.1% of FOLIO oracle ceiling\\\"\\n          - \\\"Aggregation mechanism is sound; extraction quality is binding constraint\\\"\\n      - id: \\\"sec:replication\\\"\\n        title: \\\"Four-Seed Replication\\\"\\n        word_budget: 250\\n        bullets:\\n          - \\\"Mistral-7B FOLIO-204: seeds 42, 123, 456, 789\\\"\\n          - \\\"s42: Δ=+3.43pp p=0.092; s123: +2.94pp p=0.070; s456: 0.00pp p=1.0; s789: -0.49pp p=1.0\\\"\\n          - \\\"2/4 marginal positive (p<0.10); 0/4 reaches p<0.05\\\"\\n          - \\\"4-seed mean: +1.47pp; range: +3.43 to -0.49\\\"\\n          - \\\"Fragility itself is the finding — motivates independence analysis\\\"\\n      - id: \\\"sec:failure-modes\\\"\\n        title: \\\"Failure Mode Analysis\\\"\\n        word_budget: 250\\n        bullets:\\n          - \\\"Type A: consistent traces → constraints mirror model's answers → MAX-SAT degenerates to counting\\\"\\n          - \\\"Type B: domain not formalizable (LogiQA contradiction rate 0.8%)\\\"\\n          - \\\"Type C: predominantly wrong traces → wrong constraints → solver amplifies errors\\\"\\n    dependencies: []\\n    tables: [tab1_main_results]\\n    figures: [fig2_regime_scatter]\\n    registry_refs:\\n      - exp-033  # Mistral FOLIO s42 (hero)\\n      - exp-052  # Mistral FOLIO s123\\n      - exp-053  # Mistral FOLIO s456\\n      - exp-067  # Mistral FOLIO s789\\n      - exp-046  # Mistral PW-600 (Type C)\\n      - exp-049b # Mistral LogiQA\\n      - exp-063  # LLaMA FOLIO\\n      - exp-019  # LLaMA StrategyQA\\n      - exp-061  # Qwen2.5-7B FOLIO\\n      - exp-026  # Qwen2.5-14B FOLIO (regen)\\n      - exp-038  # Qwen2.5-14B LogiQA\\n      - exp-039  # Qwen2.5-14B PW-600\\n      - exp-044b # Qwen2.5-14B FOLIO ICL\\n      - exp-027  # Qwen3-14B FOLIO\\n      - exp-040  # Qwen3-14B PW-600\\n      - exp-031  # Oracle FOLIO\\n      - exp-022  # Oracle PW\\n\\n  - section: analysis\\n    file: analysis.tex\\n    word_budget: 1500\\n    subsections:\\n      - id: \\\"sec:effective-k\\\"\\n        title: \\\"Condorcet Independence Analysis\\\"\\n        word_budget: 350\\n        bullets:\\n          - \\\"Table 3: Fleiss' κ and Eff-K per model-domain condition\\\"\\n          - \\\"Mistral FOLIO 4 seeds: κ=0.41–0.51, Eff-K=1.8–2.2 (cross-seed stable)\\\"\\n          - \\\"Qwen family: κ=0.66–0.82, Eff-K=1.2–1.5 → all near-zero Δ\\\"\\n          - \\\"Mistral PW: κ=0.21, Eff-K=3.62 but SC=39% → negative (highest independence, insufficient quality)\\\"\\n          - \\\"Qwen3-14B thinking: κ=0.91, Eff-K=1.09 → 'better reasoning' worsens independence\\\"\\n          - \\\"Dual requirement: need both sufficient Eff-K AND sufficient SC\\\"\\n          - \\\"Explains SC plateau: traces beyond Eff-K provide no new information\\\"\\n      - id: \\\"sec:extraction-taxonomy\\\"\\n        title: \\\"Constraint Quality Analysis\\\"\\n        word_budget: 200\\n        bullets:\\n          - \\\"Discriminative rate: ~8.2% (95% CI [7.6, 8.8])\\\"\\n          - \\\"Removing non-discriminative constraints: 0 gain → problem is direction not quality\\\"\\n          - \\\"Variable naming: 56.4% cross-trace constraint pairs share zero Z3 variables\\\"\\n          - \\\"~92% constraints ARE discriminative but discriminate in same direction as model bias\\\"\\n      - id: \\\"sec:entropy\\\"\\n        title: \\\"Entropy Decomposition\\\"\\n        word_budget: 200\\n        bullets:\\n          - \\\"Per-problem answer entropy separates SICA operating point\\\"\\n          - \\\"Low-entropy: SICA≈SC across all 8 conditions (Δ≈0) — traces agree, constraints add nothing\\\"\\n          - \\\"High-entropy: regime-dependent — +12.8pp intermediate-SC (s42), -8.2pp Type A (Qwen14B)\\\"\\n          - \\\"High-entropy proportion: Mistral 38% vs Qwen 18% → explains model-level Δ differences\\\"\\n          - \\\"Mechanism: low-entropy = direct CJT channel; high-entropy = indirect constraint channel\\\"\\n      - id: \\\"sec:ablation\\\"\\n        title: \\\"MAX-SAT Ablation\\\"\\n        word_budget: 100\\n        bullets:\\n          - \\\"MAX-SAT vs count-only: 803/804 agreement (Qwen14B, n=804)\\\"\\n          - \\\"Self-extracted constraints carry no signal beyond vote counts in high-SC regime\\\"\\n          - \\\"Confirms independence bottleneck causes MAX-SAT to degenerate\\\"\\n      - id: \\\"sec:k-t-sensitivity\\\"\\n        title: \\\"K and Temperature Sensitivity\\\"\\n        word_budget: 200\\n        bullets:\\n          - \\\"K sensitivity: K=4(-1.47), K=8(-1.96), K=12(+3.43), K=16(+1.47), K=20(+1.96)\\\"\\n          - \\\"K=12 is only setting with Δ>2pp; not clean inverted-U\\\"\\n          - \\\"T sensitivity: T=0.3(-1.47), T=0.5(-0.98), T=0.7(+3.43), T=1.0(0.00)\\\"\\n          - \\\"T=0.7 is isolated spike; only 1/4 temperatures positive\\\"\\n          - \\\"Both K=12 and T=0.7 coincide with lowest SC baseline → confound with operating window\\\"\\n          - \\\"Figure 3: two-panel K/T sensitivity plot\\\"\\n      - id: \\\"sec:remediation\\\"\\n        title: \\\"Remediation Analysis\\\"\\n        word_budget: 350\\n        bullets:\\n          - \\\"--- Prompt-level (9 strategies, 6 dimensions) ---\\\"\\n          - \\\"Prompting: contrastive extraction (disc_rate 8.2%→6.0%, Δ still mirrors bias)\\\"\\n          - \\\"Architecture: cross-model bilateral (weak→strong: 0% disc; strong→weak: ±1pp of self)\\\"\\n          - \\\"Capability: generational scaling Qwen3-14B (+0.49pp ns)\\\"\\n          - \\\"Verification: Z3 feedback (0.9% UNSAT), cross-trace UNSAT (56.4% zero shared vars)\\\"\\n          - \\\"Diversity: multi-temp (Δ=0.00pp), T=1.0 (Δ=0.00pp — collapse from +3.43)\\\"\\n          - \\\"Filtering: discriminative constraint filtering (0 gain), consistency filtering (reverts to SC)\\\"\\n          - \\\"ICL with gold FOL examples (+0.50pp ns)\\\"\\n          - \\\"--- Method-level (3 methods × 2 datasets) ---\\\"\\n          - \\\"ICG (Independent Constraint Gen.): FOLIO Δ=-2.0/+1.5pp (noise), LogiQA -0.5pp → neutral\\\"\\n          - \\\"  Insight: independent constraints ≈ trace-sourced → bias from problem understanding stage\\\"\\n          - \\\"Contrastive (Pro/Con Scoring): FOLIO -9.3pp, LogiQA pending → harmful\\\"\\n          - \\\"  Insight: 26% degenerate scoring, pro/con imbalance (94 pro vs 65 con)\\\"\\n          - \\\"Debate (Proposer/Critic): FOLIO -18.6pp, LogiQA pending → catastrophic\\\"\\n          - \\\"  Insight: 7B role-play degradation; same-model debate = same bias + cognitive overhead\\\"\\n          - \\\"Scale caveat: all method-level tested at 7B; 14B+ may differ\\\"\\n          - \\\"--- κ Generalization: Independence-Accuracy Trade-off (exp-077, CAPSTONE) ---\\\"\\n          - \\\"Table T7: SC κ=0.44 Eff-K=2.02 | Diverse-Prompt κ=0.40 Eff-K=2.21 | Debate κ=0.15 Eff-K=4.44\\\"\\n          - \\\"Diverse-Prompt ≈ SC κ → changing prompts cannot break correlation\\\"\\n          - \\\"Debate breaks κ (0.44→0.15) but accuracy collapses (-18.6pp)\\\"\\n          - \\\"FUNDAMENTAL TRADE-OFF: methods that increase independence destroy accuracy; methods that preserve accuracy cannot break correlation\\\"\\n          - \\\"This explains WHY same-model methods must fail — not just that they do\\\"\\n          - \\\"Implication: breaking bottleneck requires cross-model or external signal (consistent with oracle)\\\"\\n    dependencies: [experiments]\\n    tables: [tab3_independence, tab_method_interventions, tab_kappa_generalization]\\n    figures: [fig3_sensitivity]\\n    registry_refs:\\n      - exp-029  # contrastive prompting\\n      - exp-030  # cross-model extraction\\n      - exp-059  # cross-model Qwen3→Mistral\\n      - exp-060  # cross-model Qwen14B→Mistral\\n      - exp-027  # Qwen3-14B (generational)\\n      - exp-036  # Z3 feedback\\n      - exp-036b # cross-trace UNSAT\\n      - exp-043  # consistency filtering\\n      - exp-055  # multi-temp\\n      - exp-054  # T=1.0\\n      - exp-057  # T=0.3\\n      - exp-058  # T=0.5\\n      - exp-044b # ICL gold FOL\\n      - exp-074  # ICG FOLIO s42\\n      - exp-074c # ICG FOLIO s123\\n      - exp-075b # Contrastive FOLIO\\n      - exp-076  # Debate FOLIO\\n      - exp-079  # ICG LogiQA\\n      - exp-080  # Contrastive LogiQA\\n      - exp-078  # Debate LogiQA (RUNNING)\\n      - exp-077  # κ generalization (CAPSTONE)\\n\\n  - section: discussion\\n    file: discussion.tex\\n    word_budget: 450\\n    core_bullets:\\n      - \\\"Oracle causally isolates: aggregation mechanism sound, extraction is binding bottleneck\\\"\\n      - \\\"Dual-channel mechanism: direct (voting diversity → SC plateau) + indirect (constraint homogenization → MAX-SAT degeneration)\\\"\\n      - \\\"Oracle disambiguates: gold constraints on same correlated traces yield +14.22pp → indirect channel is proximal bottleneck\\\"\\n      - \\\"Independence-accuracy trade-off (exp-077): Debate breaks κ (0.44→0.15) but collapses accuracy (-18.6pp). Diverse-Prompt ≈ SC κ. Same-model methods face a fundamental Pareto frontier.\\\"\\n      - \\\"This trade-off explains WHY same-model methods must fail, not just that they do. Breaking correlation within a single model's distribution necessarily degrades the signal.\\\"\\n      - \\\"Published methods (DyLoS, Aristotle, FoVer, Logic-LM) bypass same-model extraction — consistent with trade-off: cross-model/external sources are naturally independent without sacrificing quality\\\"\\n      - \\\"Statistical evidence: 0/4 seeds significant positive; only significant effects are negative\\\"\\n      - \\\"C0+SC deployment diagnostic: C0<5%→degenerate, high SC→confirmation bias, low SC→error amplification\\\"\\n      - \\\"Three paths forward trade simplicity for independence: trained extractors, external provers, multi-model pipelines — all introduce signal outside the model's own distribution\\\"\\n    dependencies: [experiments, analysis]\\n\\n  - section: conclusion\\n    file: conclusion.tex\\n    word_budget: 300\\n    core_bullets:\\n      - \\\"SICA evaluated: 6 models spanning 3 families, 3 reasoning domains, N>3,000, 4-seed replication\\\"\\n      - \\\"Independence bottleneck: κ=0.21–0.82, Eff-K=1.20–3.62 → explains SC plateau and SICA failure\\\"\\n      - \\\"Intermediate-SC region: +3.43pp best seed (ns), 4-seed mean +1.47pp (2/4 positive, 2/4 null/negative)\\\"\\n      - \\\"Oracle +14.22pp/+11.50pp (p<0.001); 12 remediations all fail; independence-accuracy trade-off explains why\\\"\\n      - \\\"Limitations: trained extractors untested, narrow intermediate-SC zone, 7B-scale method testing, formal reasoning domains only\\\"\\n    dependencies: [experiments, analysis]\\n\\n# ──────────────────────────────────────────────\\n# Visualization Plan\\n# ──────────────────────────────────────────────\\nvisualization_plan:\\n  - fig_id: fig1_pipeline\\n    type: conceptual\\n    tool: matplotlib\\n    description: >\\n      SICA pipeline diagram: K traces → FOL constraint extraction →\\n      dedup → weighted partial MAX-SAT (Z3) → answer selection.\\n      Oracle branch replaces self-extracted constraints with gold FOL.\\n      Independence bottleneck annotation at extraction stage.\\n    narrative_intent: >\\n      The pipeline looks like it should introduce independent symbolic\\n      signal, but self-extraction inherits the same trace correlation —\\n      the independence bottleneck manifests at the extraction stage.\\n    design_notes:\\n      - \\\"Existing figure in paper; update to annotate independence bottleneck clearly\\\"\\n      - \\\"Add oracle branch as parallel path with green highlight\\\"\\n      - \\\"Add method-level intervention points (ICG/Contrastive/Debate) as annotation\\\"\\n    placement: method\\n    aspect_ratio: \\\"16:6\\\"\\n    data_source: \\\"manual (diagram)\\\"\\n    status: \\\"EXISTS — label update needed\\\"\\n\\n  - fig_id: fig2_regime_scatter\\n    type: statistical\\n    tool: matplotlib\\n    description: >\\n      SC accuracy (x-axis) vs SICA Δpp (y-axis) scatter plot.\\n      All model-domain conditions from Table 1. 4 replication seeds\\n      as separate points. Color/marker by model family.\\n      Shaded intermediate-SC band (50–55%). Regime zone labels.\\n    narrative_intent: >\\n      The intermediate-SC region is narrow and model-specific. Outside it,\\n      SICA is either neutral (Type A) or harmful (Type C). No condition\\n      shows statistically significant improvement.\\n    design_notes:\\n      - \\\"Pattern A: regime bands — light shading 50-55% SC, labeled zones\\\"\\n      - \\\"Solid markers: n≥100; hollow: n<50\\\"\\n      - \\\"Horizontal Δ=0 reference line (dashed)\\\"\\n      - \\\"4 Mistral FOLIO seeds clustered at SC≈54-56%\\\"\\n      - \\\"Star or bold outline for significant effects (p<0.05)\\\"\\n      - \\\"Annotate LLaMA -4.41pp as 'upper boundary' of intermediate-SC\\\"\\n    placement: experiments\\n    aspect_ratio: \\\"4:3\\\"\\n    data_source: \\\"registry: all Table 1 conditions (~18 points + oracle excluded)\\\"\\n    status: \\\"EXISTS — needs regeneration with 4-seed + new experiments\\\"\\n\\n  - fig_id: fig3_sensitivity\\n    type: statistical\\n    tool: matplotlib\\n    description: >\\n      Two-panel figure. (a) K sensitivity: K=4,8,12,16,20 vs Δpp.\\n      (b) T sensitivity: T=0.3,0.5,0.7,1.0 vs Δpp. Both annotated\\n      with SC baseline at each point.\\n    narrative_intent: >\\n      SICA's optimal hyperparameters are fragile: K=12 is the only\\n      setting with Δ>2pp, T=0.7 is an isolated spike. Both peaks\\n      coincide with the lowest SC baseline, suggesting the effect\\n      reflects operating window rather than causal K/T contribution.\\n    design_notes:\\n      - \\\"Panel (a): line plot K vs Δ, secondary y-axis or annotation for SC\\\"\\n      - \\\"Panel (b): line plot T vs Δ, annotate SC at each T\\\"\\n      - \\\"Dashed Δ=0 reference line in both panels\\\"\\n      - \\\"Highlight K=12 and T=0.7 as peaks; annotate SC values\\\"\\n      - \\\"Pattern: minimal, 2-panel with shared y-axis scale if possible\\\"\\n    placement: analysis\\n    aspect_ratio: \\\"2:1\\\"\\n    data_source: >\\n      K sensitivity: exp-051 data (K=4,8,12,16,20).\\n      T sensitivity: exp-033 (T=0.7), exp-054 (T=1.0), exp-057 (T=0.3), exp-058 (T=0.5).\\n    status: \\\"EXISTS — needs regeneration with corrected data + T panel\\\"\\n\\n# ──────────────────────────────────────────────\\n# Table Plan\\n# ──────────────────────────────────────────────\\ntable_plan:\\n  # Main text tables\\n  - table_id: tab1_main_results\\n    type: comparison\\n    placement: experiments\\n    width: \\\"table*\\\"\\n    caption: >\\n      SICA vs SC across all model-domain conditions (K=12, T=0.7).\\n      Grouped by SC accuracy regime. Bold: significant effects (p<0.05).\\n      Bottom: oracle controls with gold FOL annotations.\\n    columns: [Model, Domain, n, \\\"SC (%)\\\", \\\"SICA (%)\\\", \\\"Δ (pp)\\\", \\\"p\\\"]\\n    data_source: \\\"registry: see experiments.registry_refs\\\"\\n    notes: >\\n      ~18 data rows grouped as: Type C / Intermediate-SC (4 seeds) /\\n      Type A (9 conditions) / Degenerate / Oracle. Footnotes for\\n      StrategyQA diagnostic and ICL condition.\\n\\n  - table_id: tab3_independence\\n    type: statistics\\n    placement: analysis\\n    width: \\\"table\\\"\\n    caption: >\\n      Condorcet independence metrics per model-domain condition.\\n      κ = Fleiss' kappa (K=12 traces), Eff-K = K/(1+(K-1)κ).\\n    columns: [Model (seed), Domain, \\\"κ\\\", \\\"Eff-K\\\", \\\"SC (%)\\\", \\\"SICA Δ (pp)\\\"]\\n    data_source: \\\"comp-1 verified κ values + registry\\\"\\n    notes: >\\n      ~14 rows including 4 Mistral FOLIO seeds, Mistral PW/LogiQA,\\n      Qwen family, Qwen3 thinking mode.\\n\\n  - table_id: tab_method_interventions\\n    type: comparison\\n    placement: analysis\\n    width: \\\"table\\\"\\n    caption: >\\n      Method-level interventions targeting the independence bottleneck\\n      (Mistral-7B). Each targets a different aspect: ICG bypasses\\n      trace-constraint coupling, Contrastive adds adversarial scoring,\\n      Debate adds multi-role reasoning.\\n    columns: [Method, Target Aspect, \\\"FOLIO Δ (pp)\\\", \\\"LogiQA Δ (pp)\\\", Failure Mode]\\n    data_source: \\\"registry: exp-074, exp-074c, exp-075b, exp-076, exp-079, exp-080, exp-078\\\"\\n    notes: >\\n      3 methods × 2 datasets. ICG has multi-seed on FOLIO.\\n      Debate LogiQA (exp-078) may still be running; mark if unavailable.\\n\\n  - table_id: tab_kappa_generalization\\n    type: statistics\\n    placement: analysis\\n    width: \\\"table\\\"\\n    caption: >\\n      Independence-accuracy trade-off: Fleiss' κ and Eff-K across three\\n      aggregation methods on Mistral-7B FOLIO (exp-077). Debate achieves\\n      the highest Eff-K but collapses accuracy.\\n    columns: [Aggregation Method, \\\"κ\\\", \\\"Eff-K\\\", \\\"Nominal K\\\", \\\"Δ (pp)\\\"]\\n    data_source: \\\"registry: exp-077\\\"\\n    notes: >\\n      SC: κ=0.4384, Eff-K=2.02, K=10; Diverse-Prompt: κ=0.4030,\\n      Eff-K=2.21, K=12; Debate: κ=0.1549, Eff-K=4.44, K=12, Δ=-18.6pp.\\n      CAPSTONE finding: trade-off explains why same-model methods must fail.\\n\\n  # Appendix tables\\n  - table_id: tab_app_remediation\\n    type: comparison\\n    placement: appendix\\n    caption: \\\"Nine prompt-level remediation strategies.\\\"\\n    columns: [Strategy, Dimension, Key Metric, Result, exp_id]\\n\\n  - table_id: tab_app_entropy\\n    type: analysis\\n    placement: appendix\\n    caption: \\\"SICA Δ conditioned on per-problem answer entropy (high vs low).\\\"\\n    columns: [Model, Dataset, \\\"High-E n\\\", \\\"High-E Δ\\\", \\\"Low-E n\\\", \\\"Low-E Δ\\\"]\\n\\n  - table_id: tab_app_power_analysis\\n    type: analysis\\n    placement: appendix\\n    caption: \\\"Statistical power analysis for primary conditions.\\\"\\n\\n  - table_id: tab_app_bootstrap\\n    type: analysis\\n    placement: appendix\\n    caption: \\\"Bootstrap 95% CIs for selected conditions.\\\"\\n\\n  - table_id: tab_app_constraint_quality\\n    type: analysis\\n    placement: appendix\\n    caption: \\\"Constraint extraction quality metrics by model.\\\"\\n\\n  - table_id: tab_app_k_detail\\n    type: detail\\n    placement: appendix\\n    caption: \\\"K sensitivity: full metrics at each K value.\\\"\\n\\n# ──────────────────────────────────────────────\\n# Literature Strategy\\n# ──────────────────────────────────────────────\\nliterature_strategy:\\n  citation_budget: 42\\n  macro_context:\\n    - \\\"self-consistency and majority voting in LLM reasoning\\\"\\n    - \\\"neuro-symbolic methods combining LLMs with formal solvers\\\"\\n    - \\\"Condorcet Jury Theorem and ensemble independence\\\"\\n  micro_clusters:\\n    - cluster_name: \\\"self_consistency_and_variants\\\"\\n      target_count: 6\\n      must_cite:\\n        - \\\"Wang et al. 2023 (Self-Consistency)\\\"\\n        - \\\"Chen et al. 2024 (USC)\\\"\\n        - \\\"Loo et al. 2025 (SC scaling plateau)\\\"\\n        - \\\"Taubenfeld et al. 2025 (confidence-weighted SC)\\\"\\n        - \\\"Li et al. 2023 (DiVeRSe)\\\"\\n      search_queries:\\n        - \\\"self-consistency majority voting LLM reasoning 2024 2025\\\"\\n\\n    - cluster_name: \\\"symbolic_reasoning_llm\\\"\\n      target_count: 7\\n      must_cite:\\n        - \\\"Pan et al. 2023 (Logic-LM)\\\"\\n        - \\\"Olausson et al. 2023 (LINC)\\\"\\n        - \\\"Xu et al. 2026 (DyLoS)\\\"\\n        - \\\"Li et al. 2025 (Aristotle)\\\"\\n        - \\\"Wang et al. 2025 (FoVer)\\\"\\n      search_queries:\\n        - \\\"neuro-symbolic reasoning LLM formal logic solver 2025 2026\\\"\\n\\n    - cluster_name: \\\"condorcet_voting_theory\\\"\\n      target_count: 6\\n      must_cite:\\n        - \\\"Condorcet 1785\\\"\\n        - \\\"Austen-Smith & Banks 1996\\\"\\n        - \\\"Ladha 1992 (correlated voters)\\\"\\n        - \\\"Lefort et al. 2024 (arXiv:2409.00094)\\\"\\n        - \\\"Fleiss 1971 (kappa)\\\"\\n        - \\\"Kish 1965 (design effect / Eff-K)\\\"\\n      search_queries:\\n        - \\\"Condorcet jury theorem ensemble independence machine learning\\\"\\n\\n    - cluster_name: \\\"verification_reranking\\\"\\n      target_count: 4\\n      must_cite:\\n        - \\\"Cobbe et al. 2021 (ORM/GSM8K)\\\"\\n        - \\\"Lightman et al. 2023 (PRM)\\\"\\n        - \\\"Wang et al. 2024 (Math-Shepherd)\\\"\\n      search_queries:\\n        - \\\"process reward model verification LLM 2024\\\"\\n\\n    - cluster_name: \\\"test_time_compute\\\"\\n      target_count: 4\\n      must_cite:\\n        - \\\"Snell et al. 2025 (scaling test-time compute)\\\"\\n        - \\\"DeepSeek-AI 2025 (DeepSeek-R1)\\\"\\n      search_queries:\\n        - \\\"test-time compute scaling reasoning 2025 2026\\\"\\n\\n    - cluster_name: \\\"debate_multi_agent\\\"\\n      target_count: 3\\n      must_cite:\\n        - \\\"Liang et al. 2023 (multi-agent debate)\\\"\\n        - \\\"Du et al. 2023 (improving factuality via debate)\\\"\\n      search_queries:\\n        - \\\"LLM multi-agent debate reasoning 2024\\\"\\n\\n    - cluster_name: \\\"self_correction_negative\\\"\\n      target_count: 2\\n      must_cite:\\n        - \\\"Huang et al. 2024 (cannot self-correct reasoning)\\\"\\n      search_queries:\\n        - \\\"LLM self-correction limitation negative result 2024\\\"\\n\\n    - cluster_name: \\\"benchmarks\\\"\\n      target_count: 5\\n      must_cite:\\n        - \\\"Han et al. 2022 (FOLIO)\\\"\\n        - \\\"Tafjord et al. 2021 (ProofWriter)\\\"\\n        - \\\"Liu et al. 2020 (LogiQA)\\\"\\n        - \\\"Geva et al. 2021 (StrategyQA)\\\"\\n\\n    - cluster_name: \\\"constraint_satisfaction\\\"\\n      target_count: 2\\n      must_cite:\\n        - \\\"de Moura & Bjorner 2008 (Z3)\\\"\\n\\n    - cluster_name: \\\"oracle_diagnostic_methodology\\\"\\n      target_count: 2\\n      must_cite:\\n        - \\\"Press et al. 2023 (compositionality gap)\\\"\\n      search_queries:\\n        - \\\"oracle upper bound diagnosis pipeline bottleneck NLP\\\"\\n\\n# ──────────────────────────────────────────────\\n# Writing Order (strict serial)\\n# ──────────────────────────────────────────────\\nwriting_order:\\n  - method          # Foundation: Condorcet + SICA + Oracle + Method interventions\\n  - experiments     # Data-driven: Table 1 + oracle + replication + failure modes\\n  - analysis        # Deep dive: independence + extraction + entropy + K/T + remediation\\n  - related_work    # Positioning: standalone, can reference method/experiments\\n  - introduction    # Synthesis: depends on all above\\n  - discussion      # Interpretation: depends on all empirical\\n  - abstract        # Summary: last written\\n  - conclusion      # Summary: last written\\n\\n# ──────────────────────────────────────────────\\n# Page Budget (8pp main text target)\\n# ──────────────────────────────────────────────\\npage_budget:\\n  target: 8.0\\n  breakdown:\\n    abstract: 0.3\\n    introduction: 1.3\\n    related_work: 0.8\\n    method: 1.1\\n    experiments: 1.8\\n    analysis: 1.5\\n    discussion: 0.5\\n    conclusion: 0.3\\n    total_text: 7.6\\n    display_items_float: 0.4\\n  notes:\\n    - \\\"3 main-text figures + 3 main-text tables = 6 display items (within 4-7 budget for 8pp)\\\"\\n    - \\\"Oracle merged into Table 1 bottom rows (saves table float)\\\"\\n    - \\\"4-seed replication as rows in Table 1 (no separate table)\\\"\\n    - \\\"Prompt-level remediation: 1 paragraph main text + full table in appendix\\\"\\n    - \\\"Method interventions: compact table (3 rows) in main text\\\"\\n    - \\\"Entropy: compact paragraph + move detailed 8-condition table to appendix\\\"\\n\\n# ──────────────────────────────────────────────\\n# Key Data (truth source: registry, verified .tex)\\n# ──────────────────────────────────────────────\\nkey_data:\\n  hero_result:\\n    exp_id: exp-033\\n    model: Mistral-7B-Instruct-v0.3\\n    dataset: FOLIO-204\\n    seed: 42\\n    sc: 55.88\\n    sica: 59.31\\n    delta_pp: 3.43\\n    p: 0.092\\n    note: \\\"NOT significant at α=0.05. Directional trend only.\\\"\\n\\n  replication_4seed:\\n    - {exp_id: exp-033, seed: 42, sc: 55.88, delta_pp: 3.43, p: 0.092}\\n    - {exp_id: exp-052, seed: 123, sc: 54.41, delta_pp: 2.94, p: 0.070}\\n    - {exp_id: exp-053, seed: 456, sc: 55.88, delta_pp: 0.00, p: 1.0}\\n    - {exp_id: exp-067, seed: 789, sc: 54.41, delta_pp: -0.49, p: 1.0}\\n    mean_delta: 1.47\\n    note: \\\"2/4 marginal positive (p<0.10), 0/4 significant. Range +3.43 to -0.49.\\\"\\n\\n  oracle:\\n    - {exp_id: exp-031, dataset: FOLIO-204, oracle_acc: 89.71, sc: 75.49, delta_pp: 14.22, p: \\\"<0.001\\\"}\\n    - {exp_id: exp-022, dataset: PW-600, oracle_acc: 86.67, sc: 75.17, delta_pp: 11.50, p: \\\"<0.001\\\"}\\n    utilization: \\\"24.1% (best seed 3.43 / oracle 14.22)\\\"\\n\\n  type_c:\\n    exp_id: exp-046\\n    model: Mistral-7B\\n    dataset: ProofWriter-D5-600\\n    n: 600\\n    sc: 39.33\\n    sica: 36.50\\n    delta_pp: -2.83\\n    p: 0.014\\n\\n  independence:\\n    range_kappa: \\\"0.21–0.82 (instruction-tuned), 0.91 (thinking)\\\"\\n    range_eff_k: \\\"1.20–3.62\\\"\\n    mistral_folio_4seed_kappa: \\\"0.41–0.51\\\"\\n    mistral_folio_4seed_eff_k: \\\"1.8–2.2\\\"\\n\\n  method_interventions:\\n    - {method: ICG, folio_delta: \\\"-2.0/+1.5 (2 seeds)\\\", logiqa_delta: -0.5, mode: neutral}\\n    - {method: Contrastive, folio_delta: -9.31, logiqa_delta: \\\"pending\\\", mode: harmful}\\n    - {method: Debate, folio_delta: -18.63, logiqa_delta: \\\"pending (RUNNING)\\\", mode: catastrophic}\\n    note: \\\"All tested on Mistral-7B. 7B scale caveat.\\\"\\n\\n  kappa_generalization:\\n    exp_id: exp-077\\n    status: DONE\\n    note: \\\"CAPSTONE finding — independence-accuracy trade-off\\\"\\n    data:\\n      - {method: \\\"Self-Consistency\\\", kappa: 0.4384, eff_k: 2.02, nominal_k: 10}\\n      - {method: \\\"Diverse-Prompt\\\", kappa: 0.4030, eff_k: 2.21, nominal_k: 12}\\n      - {method: \\\"LLM-Debate\\\", kappa: 0.1549, eff_k: 4.44, nominal_k: 12, delta: -18.6}\\n    insight: >\\n      Methods that increase independence (Debate: κ↓) destroy accuracy (Δ=-18.6pp).\\n      Methods that preserve accuracy (Diverse-Prompt) cannot break correlation (κ≈SC).\\n      This is a Pareto frontier, not an engineering gap.\\n\\n  pending_data:\\n    - {exp_id: exp-074d, desc: \\\"ICG FOLIO seed456\\\", status: PREPARING}\\n    - {exp_id: exp-078, desc: \\\"Debate LogiQA\\\", status: RUNNING}\\n    - {exp_id: exp-080, desc: \\\"Contrastive LogiQA — check registry for final delta\\\", status: DONE}\\n    note: \\\"exp-077 DONE. Remaining expected by May 20 morning per Director\\\"\\n\", \"total_chars\": 35250, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "32cbf480-c5bb-4a08-82ea-0514a848ebaf",
  "isSidechain": false,
  "promptId": "3f50ba00-7d30-45ec-b450-7010d531c858",
  "type": "user",
  "uuid": "1f321fa3-c68a-4f74-90a6-56038cf03999",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/writing_plan.yaml\\\", \\\"content\\\": \\\"# Writing Plan — symb_invariant_consensus\\\\n# Generated: 2026-05-19T20:30:00Z\\\\n# Full Draft: Independence Bottleneck — \\\\\\\"Fundamental Limitation\\\\\\\" paper\\\\n# Target: EMNLP 2026 ARR May cycle\\\\n# Paper Agent Step 1 output\\\\n\\\\nmeta:\\\\n  venue: EMNLP 2026\\\\n  track: main (ARR May cycle)\\\\n  template: docs/paper/acl.sty\\\\n  template_note: \\\\\\\"ACL/EMNLP shared template already in paper directory\\\\\\\"\\\\n  page_limit: 8\\\\n  deadline: 2026-05-25\\\\n  title: >\\\\n    Beyond Self-Consistency: How Trace Independence Limits\\\\n    Symbolic Consensus in LLM Reasoning\\\\n  core_claim: >\\\\n    Same-model self-extraction of symbolic constraints inherits trace\\\\n    correlation (Fleiss' κ=0.21–0.82, Eff-K=1.20–3.62 for nominal K=12),\\\\n    creating a structural independence bottleneck. Oracle gold-FOL yields\\\\n    +14.22pp (p<0.001) proving aggregation is sound, but self-extraction\\\\n    captures only 24%. κ generalization across aggregation methods reveals\\\\n    a fundamental independence-accuracy trade-off: Debate reduces κ from\\\\n    0.44→0.15 (Eff-K 2→4.4) but collapses accuracy by -18.6pp. Same-model\\\\n    methods cannot increase independence without degrading the signal that\\\\n    makes aggregation useful.\\\\n  paper_type: \\\\\\\"Fundamental limitation analysis (Condorcet framework + empirical diagnosis + 12 remediation failures)\\\\\\\"\\\\n  framing: \\\\\\\"Independence Bottleneck — structural limitation of same-model self-extraction\\\\\\\"\\\\n  created_at: 2026-05-19T20:30:00Z\\\\n\\\\n# ──────────────────────────────────────────────\\\\n# Contributions (5)\\\\n# ──────────────────────────────────────────────\\\\ncontributions:\\\\n  - id: C1\\\\n    label: \\\\\\\"Independence Bottleneck Quantification\\\\\\\"\\\\n    status: VERIFIED\\\\n    claim: >\\\\n      Fleiss' κ=0.21–0.82 (instruction-tuned), 0.91 (thinking mode).\\\\n      Eff-K=1.20–3.62 at K=12. Mistral 4-seed κ=0.41–0.51 (stable).\\\\n      Qwen Eff-K≈1.2–1.5 → near-zero Δ; Mistral PW Eff-K=3.62 but\\\\n      SC=39% → negative Δ. Dual requirement: sufficient Eff-K AND SC.\\\\n    evidence: \\\\\\\"Table 3, §5.1\\\\\\\"\\\\n\\\\n  - id: C2\\\\n    label: \\\\\\\"Oracle Gap Localizes Extraction Bottleneck\\\\\\\"\\\\n    status: VERIFIED\\\\n    claim: >\\\\n      Gold FOL: +14.22pp FOLIO (p<0.001), +11.50pp PW (p<0.001).\\\\n      Self-extraction captures 24% of oracle ceiling (best seed +3.43pp\\\\n      vs +14.22pp). Aggregation mechanism sound; extraction quality is\\\\n      the binding bottleneck.\\\\n    evidence: \\\\\\\"Table 1 oracle rows, §4.3\\\\\\\"\\\\n\\\\n  - id: C3\\\\n    label: \\\\\\\"Regime-Dependent Effect with 4-Seed Replication\\\\\\\"\\\\n    status: VERIFIED\\\\n    claim: >\\\\n      Intermediate-SC (~50–55%): best seed +3.43pp (p=0.092, ns);\\\\n      4-seed mean +1.47pp; 2/4 marginal (p<0.10), 0/4 significant.\\\\n      Type A (SC≥60%): 9 conditions N>2,800, no significant positive;\\\\n      significant negatives at -2.50pp (p=0.011) and -4.41pp (p=0.093).\\\\n      Type C (SC≤40%): -2.83pp (p=0.014).\\\\n    evidence: \\\\\\\"Table 1, Figure 2, §4.1–4.3\\\\\\\"\\\\n\\\\n  - id: C4\\\\n    label: \\\\\\\"Independence-Accuracy Trade-off Is Fundamental\\\\\\\"\\\\n    status: VERIFIED\\\\n    claim: >\\\\n      κ generalization (exp-077) reveals why same-model methods must fail:\\\\n      SC κ=0.44 (Eff-K=2.02); Diverse-Prompt κ=0.40 (Eff-K=2.21, ≈SC);\\\\n      Debate κ=0.15 (Eff-K=4.44) but Δ=-18.6pp. Methods that increase\\\\n      independence (Debate) destroy accuracy; methods that preserve accuracy\\\\n      (ICG, Diverse-Prompt) cannot break correlation. 12 remediations\\\\n      (9 prompt + 3 method) all fail — not engineering failure but\\\\n      fundamental trade-off in same-model aggregation.\\\\n    evidence: \\\\\\\"§5.6, Table T7 (κ generalization), method intervention table\\\\\\\"\\\\n\\\\n  - id: C5\\\\n    label: \\\\\\\"Entropy Decomposition Reveals Regime Mechanism\\\\\\\"\\\\n    status: VERIFIED\\\\n    claim: >\\\\n      Low-entropy: SICA≈SC across all 8 conditions (Δ≈0). High-entropy\\\\n      direction regime-dependent: +12.8pp intermediate-SC, -8.2pp Type A.\\\\n      Explains dual-channel mechanism (voting diversity + constraint\\\\n      homogenization).\\\\n    evidence: \\\\\\\"§5.5, entropy analysis\\\\\\\"\\\\n\\\\n# ──────────────────────────────────────────────\\\\n# Paper Outline\\\\n# ──────────────────────────────────────────────\\\\npaper_outline:\\\\n  - section: abstract\\\\n    file: abstract.tex\\\\n    word_budget: 220\\\\n    core_bullets:\\\\n      - \\\\\\\"Problem: SC (majority voting) plateaus; CJT explains why — traces lack independence\\\\\\\"\\\\n      - \\\\\\\"SICA pipeline evaluated across 6 models, 3 formal reasoning domains, N>3,000, 4-seed replication\\\\\\\"\\\\n      - \\\\\\\"Independence quantification: κ=0.21–0.82, Eff-K=1.20–3.62 at K=12\\\\\\\"\\\\n      - \\\\\\\"Regime: +3.43pp intermediate-SC (ns), -2.83pp Type C (p=0.014), ~0 Type A\\\\\\\"\\\\n      - \\\\\\\"Oracle +14.22pp/+11.50pp proves aggregation sound; self-extraction 24%\\\\\\\"\\\\n      - \\\\\\\"12 remediations (9 prompt + 3 method) all fail — bottleneck is structural\\\\\\\"\\\\n      - \\\\\\\"C0+SC zero-cost deployment diagnostic; paths forward require independence\\\\\\\"\\\\n    dependencies: [experiments, analysis, method]\\\\n\\\\n  - section: introduction\\\\n    file: introduction.tex\\\\n    word_budget: 1300\\\\n    core_bullets:\\\\n      - \\\\\\\"Hook: Test-time compute scaling via SC improves reasoning—but plateaus. Adding more traces yields diminishing returns.\\\\\\\"\\\\n      - \\\\\\\"Gap: Neuro-symbolic methods (Logic-LM, DyLoS, FoVer) improve reasoning with external/trained components. Can same-model self-extraction of formal constraints break the SC plateau without external tools?\\\\\\\"\\\\n      - \\\\\\\"Insight: CJT requires voter independence. Same-model traces violate this (Eff-K=1.20–3.62 for K=12). Self-extracted constraints inherit the correlation structure.\\\\\\\"\\\\n      - \\\\\\\"Evaluation: SICA pipeline + Condorcet analysis + oracle control across 6 models × 3 domains, 4-seed replication\\\\\\\"\\\\n      - \\\\\\\"Key result: Oracle +14.22pp proves mechanism works; self-extraction captures 24%. 12 remediations all fail.\\\\\\\"\\\\n      - \\\\\\\"Contributions: C1–C5\\\\\\\"\\\\n    dependencies: [experiments, analysis]\\\\n    figures: [fig1_pipeline]\\\\n    citation_hints:\\\\n      - \\\\\\\"SC: Wang et al. 2023\\\\\\\"\\\\n      - \\\\\\\"SC plateau: Loo et al. 2025\\\\\\\"\\\\n      - \\\\\\\"Logic-LM: Pan et al. 2023\\\\\\\"\\\\n      - \\\\\\\"DyLoS: Xu et al. 2026\\\\\\\"\\\\n      - \\\\\\\"CJT: Condorcet 1785, Ladha 1992\\\\\\\"\\\\n      - \\\\\\\"Self-correction parallel: Huang et al. 2024\\\\\\\"\\\\n\\\\n  - section: related_work\\\\n    file: related_work.tex\\\\n    word_budget: 750\\\\n    core_bullets:\\\\n      - \\\\\\\"SC and extensions: Wang 2023, USC, weighted SC (Taubenfeld 2025), DiVeRSe, scaling plateaus (Loo 2025)\\\\\\\"\\\\n      - \\\\\\\"Neuro-symbolic reasoning: Logic-LM, LINC, DyLoS, Aristotle, FoVer — all use external/trained components; we test same-model self-extraction\\\\\\\"\\\\n      - \\\\\\\"Condorcet/voting theory: CJT, correlated voters (Ladha 1992), LLM ensembles (Lefort 2024 arXiv:2409.00094, closest prior work)\\\\\\\"\\\\n      - \\\\\\\"Verification and reranking: ORM (Cobbe 2021), PRM (Lightman 2023), Math-Shepherd — trained verifier paradigm\\\\\\\"\\\\n      - \\\\\\\"Self-X limitations: Huang 2024 self-correction ≈ structural parallel to self-extraction\\\\\\\"\\\\n      - \\\\\\\"Debate/multi-agent: Liang 2023, Du 2023 — different regime (multi-model or larger models)\\\\\\\"\\\\n    dependencies: []\\\\n\\\\n  - section: method\\\\n    file: method.tex\\\\n    word_budget: 1100\\\\n    subsections:\\\\n      - id: \\\\\\\"sec:condorcet\\\\\\\"\\\\n        title: \\\\\\\"Self-Consistency and the Condorcet Independence Assumption\\\\\\\"\\\\n        word_budget: 300\\\\n        bullets:\\\\n          - \\\\\\\"SC as majority voting: sample K reasoning traces, select most common answer\\\\\\\"\\\\n          - \\\\\\\"CJT: K independent voters each with p>0.5 → P(majority correct) → 1 as K→∞\\\\\\\"\\\\n          - \\\\\\\"LLM traces violate independence: same model, same prompt, only sampling noise\\\\\\\"\\\\n          - \\\\\\\"Eff-K = K/(1+(K-1)κ) via Kish (1965) design effect; κ = Fleiss' kappa (1971)\\\\\\\"\\\\n          - \\\\\\\"When Eff-K≈1, additional traces ≈ no new information → SC plateau\\\\\\\"\\\\n      - id: \\\\\\\"sec:sica-pipeline\\\\\\\"\\\\n        title: \\\\\\\"SICA Pipeline\\\\\\\"\\\\n        word_budget: 400\\\\n        bullets:\\\\n          - \\\\\\\"Step 1: Generate K reasoning traces at temperature T\\\\\\\"\\\\n          - \\\\\\\"Step 2: Extract FOL constraints from each trace at T_ext=0.3\\\\\\\"\\\\n          - \\\\\\\"Step 3: Syntactic deduplication across traces\\\\\\\"\\\\n          - \\\\\\\"Step 4: Weighted partial MAX-SAT — hard clauses (answer assertion), soft clauses (constraints weighted by occurrence count)\\\\\\\"\\\\n          - \\\\\\\"Step 5: Z3 solver evaluates each candidate; answer with highest satisfiable weight selected\\\\\\\"\\\\n          - \\\\\\\"Timeout: 10s per candidate answer\\\\\\\"\\\\n      - id: \\\\\\\"sec:oracle-design\\\\\\\"\\\\n        title: \\\\\\\"Oracle Control Design\\\\\\\"\\\\n        word_budget: 200\\\\n        bullets:\\\\n          - \\\\\\\"Replace self-extracted constraints with gold FOL annotations (FOLIO) or gold DSL (ProofWriter)\\\\\\\"\\\\n          - \\\\\\\"Same Z3 evaluation pipeline; only constraint source changes\\\\\\\"\\\\n          - \\\\\\\"Causal intervention: isolates constraint quality from aggregation mechanism\\\\\\\"\\\\n      - id: \\\\\\\"sec:method-interventions\\\\\\\"\\\\n        title: \\\\\\\"Method-Level Interventions\\\\\\\"\\\\n        word_budget: 150\\\\n        bullets:\\\\n          - \\\\\\\"ICG: Generate constraints independently of traces (bypass trace-constraint coupling)\\\\\\\"\\\\n          - \\\\\\\"Contrastive: Pro/con constraint scoring per candidate answer\\\\\\\"\\\\n          - \\\\\\\"Debate: Proposer/Critic/Defense chain before constraint extraction\\\\\\\"\\\\n          - \\\\\\\"Each targets a different bottleneck aspect\\\\\\\"\\\\n    dependencies: []\\\\n    figures: [fig1_pipeline]\\\\n\\\\n  - section: experiments\\\\n    file: experiments.tex\\\\n    word_budget: 1800\\\\n    subsections:\\\\n      - id: \\\\\\\"sec:exp-setup\\\\\\\"\\\\n        title: \\\\\\\"Experimental Setup\\\\\\\"\\\\n        word_budget: 300\\\\n        bullets:\\\\n          - \\\\\\\"6 models: Mistral-7B-Instruct-v0.3, LLaMA-3.1-8B-Instruct, Qwen2.5-7B-Instruct, Qwen2.5-14B-Instruct, Qwen3-14B (non-thinking), Qwen3-14B (thinking mode for κ analysis)\\\\\\\"\\\\n          - \\\\\\\"3 formal reasoning domains: FOLIO (n=204), ProofWriter depth-5 (n=600), LogiQA (n=200)\\\\\\\"\\\\n          - \\\\\\\"Cross-domain diagnostic: StrategyQA (n=200)\\\\\\\"\\\\n          - \\\\\\\"Degenerate probes: QwQ-32B (AIME 2024), Qwen2.5-14B (GSM8K)\\\\\\\"\\\\n          - \\\\\\\"Default: K=12, T=0.7, T_ext=0.3, Z3 timeout 10s\\\\\\\"\\\\n          - \\\\\\\"Metrics: accuracy (%), Δ=SICA−SC (pp), McNemar exact test α=0.05\\\\\\\"\\\\n          - \\\\\\\"4-seed replication on primary condition (Mistral-7B FOLIO)\\\\\\\"\\\\n      - id: \\\\\\\"sec:main-results\\\\\\\"\\\\n        title: \\\\\\\"Main Results: A Regime-Dependent Effect\\\\\\\"\\\\n        word_budget: 500\\\\n        bullets:\\\\n          - \\\\\\\"Table 1: ~18 conditions grouped by regime + 2 oracle rows\\\\\\\"\\\\n          - \\\\\\\"Intermediate-SC (SC~50–55%): Mistral FOLIO best seed +3.43pp (p=0.092 ns); 4-seed mean +1.47pp; Mistral LogiQA +0.50pp\\\\\\\"\\\\n          - \\\\\\\"Type A (SC≥60%): 9 conditions N>2,800; no significant positive effect\\\\\\\"\\\\n          - \\\\\\\"  Significant negatives: Qwen14B PW -2.50pp (p=0.011); Mistral PW -2.83pp (p=0.014)\\\\\\\"\\\\n          - \\\\\\\"  LLaMA FOLIO -4.41pp (p=0.093, marginal)\\\\\\\"\\\\n          - \\\\\\\"  Qwen3-14B FOLIO -0.49pp, PW +0.67pp — generational scaling does not help\\\\\\\"\\\\n          - \\\\\\\"Type C (SC≤40%): Mistral PW-D5 Δ=-2.83pp p=0.014 — SICA significantly hurts\\\\\\\"\\\\n          - \\\\\\\"Degenerate: C0<5% → SICA≡SC by construction\\\\\\\"\\\\n          - \\\\\\\"Figure 2: SC vs Δ scatter showing regime boundaries\\\\\\\"\\\\n      - id: \\\\\\\"sec:oracle\\\\\\\"\\\\n        title: \\\\\\\"Oracle Control: Aggregation Is Sound\\\\\\\"\\\\n        word_budget: 250\\\\n        bullets:\\\\n          - \\\\\\\"FOLIO: oracle-SICA 89.71% vs SC 75.49% (+14.22pp, p<0.001)\\\\\\\"\\\\n          - \\\\\\\"ProofWriter: oracle-SICA 86.67% vs SC 75.17% (+11.50pp, p<0.001)\\\\\\\"\\\\n          - \\\\\\\"Self-extraction captures only 24.1% of FOLIO oracle ceiling\\\\\\\"\\\\n          - \\\\\\\"Aggregation mechanism is sound; extraction quality is binding constraint\\\\\\\"\\\\n      - id: \\\\\\\"sec:replication\\\\\\\"\\\\n        title: \\\\\\\"Four-Seed Replication\\\\\\\"\\\\n        word_budget: 250\\\\n        bullets:\\\\n          - \\\\\\\"Mistral-7B FOLIO-204: seeds 42, 123, 456, 789\\\\\\\"\\\\n          - \\\\\\\"s42: Δ=+3.43pp p=0.092; s123: +2.94pp p=0.070; s456: 0.00pp p=1.0; s789: -0.49pp p=1.0\\\\\\\"\\\\n          - \\\\\\\"2/4 marginal positive (p<0.10); 0/4 reaches p<0.05\\\\\\\"\\\\n          - \\\\\\\"4-seed mean: +1.47pp; range: +3.43 to -0.49\\\\\\\"\\\\n          - \\\\\\\"Fragility itself is the finding — motivates independence analysis\\\\\\\"\\\\n      - id: \\\\\\\"sec:failure-modes\\\\\\\"\\\\n        title: \\\\\\\"Failure Mode Analysis\\\\\\\"\\\\n        word_budget: 250\\\\n        bullets:\\\\n          - \\\\\\\"Type A: consistent traces → constraints mirror model's answers → MAX-SAT degenerates to counting\\\\\\\"\\\\n          - \\\\\\\"Type B: domain not formalizable (LogiQA contradiction rate 0.8%)\\\\\\\"\\\\n          - \\\\\\\"Type C: predominantly wrong traces → wrong constraints → solver amplifies errors\\\\\\\"\\\\n    dependencies: []\\\\n    tables: [tab1_main_results]\\\\n    figures: [fig2_regime_scatter]\\\\n    registry_refs:\\\\n      - exp-033  # Mistral FOLIO s42 (hero)\\\\n      - exp-052  # Mistral FOLIO s123\\\\n      - exp-053  # Mistral FOLIO s456\\\\n      - exp-067  # Mistral FOLIO s789\\\\n      - exp-046  # Mistral PW-600 (Type C)\\\\n      - exp-049b # Mistral LogiQA\\\\n      - exp-063  # LLaMA FOLIO\\\\n      - exp-019  # LLaMA StrategyQA\\\\n      - exp-061  # Qwen2.5-7B FOLIO\\\\n      - exp-026  # Qwen2.5-14B FOLIO (regen)\\\\n      - exp-038  # Qwen2.5-14B LogiQA\\\\n      - exp-039  # Qwen2.5-14B PW-600\\\\n      - exp-044b # Qwen2.5-14B FOLIO ICL\\\\n      - exp-027  # Qwen3-14B FOLIO\\\\n      - exp-040  # Qwen3-14B PW-600\\\\n      - exp-031  # Oracle FOLIO\\\\n      - exp-022  # Oracle PW\\\\n\\\\n  - section: analysis\\\\n    file: analysis.tex\\\\n    word_budget: 1500\\\\n    subsections:\\\\n      - id: \\\\\\\"sec:effective-k\\\\\\\"\\\\n        title: \\\\\\\"Condorcet Independence Analysis\\\\\\\"\\\\n        word_budget: 350\\\\n        bullets:\\\\n          - \\\\\\\"Table 3: Fleiss' κ and Eff-K per model-domain condition\\\\\\\"\\\\n          - \\\\\\\"Mistral FOLIO 4 seeds: κ=0.41–0.51, Eff-K=1.8–2.2 (cross-seed stable)\\\\\\\"\\\\n          - \\\\\\\"Qwen family: κ=0.66–0.82, Eff-K=1.2–1.5 → all near-zero Δ\\\\\\\"\\\\n          - \\\\\\\"Mistral PW: κ=0.21, Eff-K=3.62 but SC=39% → negative (highest independence, insufficient quality)\\\\\\\"\\\\n          - \\\\\\\"Qwen3-14B thinking: κ=0.91, Eff-K=1.09 → 'better reasoning' worsens independence\\\\\\\"\\\\n          - \\\\\\\"Dual requirement: need both sufficient Eff-K AND sufficient SC\\\\\\\"\\\\n          - \\\\\\\"Explains SC plateau: traces beyond Eff-K provide no new information\\\\\\\"\\\\n      - id: \\\\\\\"sec:extraction-taxonomy\\\\\\\"\\\\n        title: \\\\\\\"Constraint Quality Analysis\\\\\\\"\\\\n        word_budget: 200\\\\n        bullets:\\\\n          - \\\\\\\"Discriminative rate: ~8.2% (95% CI [7.6, 8.8])\\\\\\\"\\\\n          - \\\\\\\"Removing non-discriminative constraints: 0 gain → problem is direction not quality\\\\\\\"\\\\n          - \\\\\\\"Variable naming: 56.4% cross-trace constraint pairs share zero Z3 variables\\\\\\\"\\\\n          - \\\\\\\"~92% constraints ARE discriminative but discriminate in same direction as model bias\\\\\\\"\\\\n      - id: \\\\\\\"sec:entropy\\\\\\\"\\\\n        title: \\\\\\\"Entropy Decomposition\\\\\\\"\\\\n        word_budget: 200\\\\n        bullets:\\\\n          - \\\\\\\"Per-problem answer entropy separates SICA operating point\\\\\\\"\\\\n          - \\\\\\\"Low-entropy: SICA≈SC across all 8 conditions (Δ≈0) — traces agree, constraints add nothing\\\\\\\"\\\\n          - \\\\\\\"High-entropy: regime-dependent — +12.8pp intermediate-SC (s42), -8.2pp Type A (Qwen14B)\\\\\\\"\\\\n          - \\\\\\\"High-entropy proportion: Mistral 38% vs Qwen 18% → explains model-level Δ differences\\\\\\\"\\\\n          - \\\\\\\"Mechanism: low-entropy = direct CJT channel; high-entropy = indirect constraint channel\\\\\\\"\\\\n      - id: \\\\\\\"sec:ablation\\\\\\\"\\\\n        title: \\\\\\\"MAX-SAT Ablation\\\\\\\"\\\\n        word_budget: 100\\\\n        bullets:\\\\n          - \\\\\\\"MAX-SAT vs count-only: 803/804 agreement (Qwen14B, n=804)\\\\\\\"\\\\n          - \\\\\\\"Self-extracted constraints carry no signal beyond vote counts in high-SC regime\\\\\\\"\\\\n          - \\\\\\\"Confirms independence bottleneck causes MAX-SAT to degenerate\\\\\\\"\\\\n      - id: \\\\\\\"sec:k-t-sensitivity\\\\\\\"\\\\n        title: \\\\\\\"K and Temperature Sensitivity\\\\\\\"\\\\n        word_budget: 200\\\\n        bullets:\\\\n          - \\\\\\\"K sensitivity: K=4(-1.47), K=8(-1.96), K=12(+3.43), K=16(+1.47), K=20(+1.96)\\\\\\\"\\\\n          - \\\\\\\"K=12 is only setting with Δ>2pp; not clean inverted-U\\\\\\\"\\\\n          - \\\\\\\"T sensitivity: T=0.3(-1.47), T=0.5(-0.98), T=0.7(+3.43), T=1.0(0.00)\\\\\\\"\\\\n          - \\\\\\\"T=0.7 is isolated spike; only 1/4 temperatures positive\\\\\\\"\\\\n          - \\\\\\\"Both K=12 and T=0.7 coincide with lowest SC baseline → confound with operating window\\\\\\\"\\\\n          - \\\\\\\"Figure 3: two-panel K/T sensitivity plot\\\\\\\"\\\\n      - id: \\\\\\\"sec:remediation\\\\\\\"\\\\n        title: \\\\\\\"Remediation Analysis\\\\\\\"\\\\n        word_budget: 350\\\\n        bullets:\\\\n          - \\\\\\\"--- Prompt-level (9 strategies, 6 dimensions) ---\\\\\\\"\\\\n          - \\\\\\\"Prompting: contrastive extraction (disc_rate 8.2%→6.0%, Δ still mirrors bias)\\\\\\\"\\\\n          - \\\\\\\"Architecture: cross-model bilateral (weak→strong: 0% disc; strong→weak: ±1pp of self)\\\\\\\"\\\\n          - \\\\\\\"Capability: generational scaling Qwen3-14B (+0.49pp ns)\\\\\\\"\\\\n          - \\\\\\\"Verification: Z3 feedback (0.9% UNSAT), cross-trace UNSAT (56.4% zero shared vars)\\\\\\\"\\\\n          - \\\\\\\"Diversity: multi-temp (Δ=0.00pp), T=1.0 (Δ=0.00pp — collapse from +3.43)\\\\\\\"\\\\n          - \\\\\\\"Filtering: discriminative constraint filtering (0 gain), consistency filtering (reverts to SC)\\\\\\\"\\\\n          - \\\\\\\"ICL with gold FOL examples (+0.50pp ns)\\\\\\\"\\\\n          - \\\\\\\"--- Method-level (3 methods × 2 datasets) ---\\\\\\\"\\\\n          - \\\\\\\"ICG (Independent Constraint Gen.): FOLIO Δ=-2.0/+1.5pp (noise), LogiQA -0.5pp → neutral\\\\\\\"\\\\n          - \\\\\\\"  Insight: independent constraints ≈ trace-sourced → bias from problem understanding stage\\\\\\\"\\\\n          - \\\\\\\"Contrastive (Pro/Con Scoring): FOLIO -9.3pp, LogiQA pending → harmful\\\\\\\"\\\\n          - \\\\\\\"  Insight: 26% degenerate scoring, pro/con imbalance (94 pro vs 65 con)\\\\\\\"\\\\n          - \\\\\\\"Debate (Proposer/Critic): FOLIO -18.6pp, LogiQA pending → catastrophic\\\\\\\"\\\\n          - \\\\\\\"  Insight: 7B role-play degradation; same-model debate = same bias + cognitive overhead\\\\\\\"\\\\n          - \\\\\\\"Scale caveat: all method-level tested at 7B; 14B+ may differ\\\\\\\"\\\\n          - \\\\\\\"--- κ Generalization: Independence-Accuracy Trade-off (exp-077, CAPSTONE) ---\\\\\\\"\\\\n          - \\\\\\\"Table T7: SC κ=0.44 Eff-K=2.02 | Diverse-Prompt κ=0.40 Eff-K=2.21 | Debate κ=0.15 Eff-K=4.44\\\\\\\"\\\\n          - \\\\\\\"Diverse-Prompt ≈ SC κ → changing prompts cannot break correlation\\\\\\\"\\\\n          - \\\\\\\"Debate breaks κ (0.44→0.15) but accuracy collapses (-18.6pp)\\\\\\\"\\\\n          - \\\\\\\"FUNDAMENTAL TRADE-OFF: methods that increase independence destroy accuracy; methods that preserve accuracy cannot break correlation\\\\\\\"\\\\n          - \\\\\\\"This explains WHY same-model methods must fail — not just that they do\\\\\\\"\\\\n          - \\\\\\\"Implication: breaking bottleneck requires cross-model or external signal (consistent with oracle)\\\\\\\"\\\\n    dependencies: [experiments]\\\\n    tables: [tab3_independence, tab_method_interventions, tab_kappa_generalization]\\\\n    figures: [fig3_sensitivity]\\\\n    registry_refs:\\\\n      - exp-029  # contrastive prompting\\\\n      - exp-030  # cross-model extraction\\\\n      - exp-059  # cross-model Qwen3→Mistral\\\\n      - exp-060  # cross-model Qwen14B→Mistral\\\\n      - exp-027  # Qwen3-14B (generational)\\\\n      - exp-036  # Z3 feedback\\\\n      - exp-036b # cross-trace UNSAT\\\\n      - exp-043  # consistency filtering\\\\n      - exp-055  # multi-temp\\\\n      - exp-054  # T=1.0\\\\n      - exp-057  # T=0.3\\\\n      - exp-058  # T=0.5\\\\n      - exp-044b # ICL gold FOL\\\\n      - exp-074  # ICG FOLIO s42\\\\n      - exp-074c # ICG FOLIO s123\\\\n      - exp-075b # Contrastive FOLIO\\\\n      - exp-076  # Debate FOLIO\\\\n      - exp-079  # ICG LogiQA\\\\n      - exp-080  # Contrastive LogiQA\\\\n      - exp-078  # Debate LogiQA (RUNNING)\\\\n      - exp-077  # κ generalization (CAPSTONE)\\\\n\\\\n  - section: discussion\\\\n    file: discussion.tex\\\\n    word_budget: 450\\\\n    core_bullets:\\\\n      - \\\\\\\"Oracle causally isolates: aggregation mechanism sound, extraction is binding bottleneck\\\\\\\"\\\\n      - \\\\\\\"Dual-channel mechanism: direct (voting diversity → SC plateau) + indirect (constraint homogenization → MAX-SAT degeneration)\\\\\\\"\\\\n      - \\\\\\\"Oracle disambiguates: gold constraints on same correlated traces yield +14.22pp → indirect channel is proximal bottleneck\\\\\\\"\\\\n      - \\\\\\\"Independence-accuracy trade-off (exp-077): Debate breaks κ (0.44→0.15) but collapses accuracy (-18.6pp). Diverse-Prompt ≈ SC κ. Same-model methods face a fundamental Pareto frontier.\\\\\\\"\\\\n      - \\\\\\\"This trade-off explains WHY same-model methods must fail, not just that they do. Breaking correlation within a single model's distribution necessarily degrades the signal.\\\\\\\"\\\\n      - \\\\\\\"Published methods (DyLoS, Aristotle, FoVer, Logic-LM) bypass same-model extraction — consistent with trade-off: cross-model/external sources are naturally independent without sacrificing quality\\\\\\\"\\\\n      - \\\\\\\"Statistical evidence: 0/4 seeds significant positive; only significant effects are negative\\\\\\\"\\\\n      - \\\\\\\"C0+SC deployment diagnostic: C0<5%→degenerate, high SC→confirmation bias, low SC→error amplification\\\\\\\"\\\\n      - \\\\\\\"Three paths forward trade simplicity for independence: trained extractors, external provers, multi-model pipelines — all introduce signal outside the model's own distribution\\\\\\\"\\\\n    dependencies: [experiments, analysis]\\\\n\\\\n  - section: conclusion\\\\n    file: conclusion.tex\\\\n    word_budget: 300\\\\n    core_bullets:\\\\n      - \\\\\\\"SICA evaluated: 6 models spanning 3 families, 3 reasoning domains, N>3,000, 4-seed replication\\\\\\\"\\\\n      - \\\\\\\"Independence bottleneck: κ=0.21–0.82, Eff-K=1.20–3.62 → explains SC plateau and SICA failure\\\\\\\"\\\\n      - \\\\\\\"Intermediate-SC region: +3.43pp best seed (ns), 4-seed mean +1.47pp (2/4 positive, 2/4 null/negative)\\\\\\\"\\\\n      - \\\\\\\"Oracle +14.22pp/+11.50pp (p<0.001); 12 remediations all fail; independence-accuracy trade-off explains why\\\\\\\"\\\\n      - \\\\\\\"Limitations: trained extractors untested, narrow intermediate-SC zone, 7B-scale method testing, formal reasoning domains only\\\\\\\"\\\\n    dependencies: [experiments, analysis]\\\\n\\\\n# ──────────────────────────────────────────────\\\\n# Visualization Plan\\\\n# ──────────────────────────────────────────────\\\\nvisualization_plan:\\\\n  - fig_id: fig1_pipeline\\\\n    type: conceptual\\\\n    tool: matplotlib\\\\n    description: >\\\\n      SICA pipeline diagram: K traces → FOL constraint extraction →\\\\n      dedup → weighted partial MAX-SAT (Z3) → answer selection.\\\\n      Oracle branch replaces self-extracted constraints with gold FOL.\\\\n      Independence bottleneck annotation at extraction stage.\\\\n    narrative_intent: >\\\\n      The pipeline looks like it should introduce independent symbolic\\\\n      signal, but self-extraction inherits the same trace correlation —\\\\n      the independence bottleneck manifests at the extraction stage.\\\\n    design_notes:\\\\n      - \\\\\\\"Existing figure in paper; update to annotate independence bottleneck clearly\\\\\\\"\\\\n      - \\\\\\\"Add oracle branch as parallel path with green highlight\\\\\\\"\\\\n      - \\\\\\\"Add method-level intervention points (ICG/Contrastive/Debate) as annotation\\\\\\\"\\\\n    placement: method\\\\n    aspect_ratio: \\\\\\\"16:6\\\\\\\"\\\\n    data_source: \\\\\\\"manual (diagram)\\\\\\\"\\\\n    status: \\\\\\\"EXISTS — label update needed\\\\\\\"\\\\n\\\\n  - fig_id: fig2_regime_scatter\\\\n    type: statistical\\\\n    tool: matplotlib\\\\n    description: >\\\\n      SC accuracy (x-axis) vs SICA Δpp (y-axis) scatter plot.\\\\n      All model-domain conditions from Table 1. 4 replication seeds\\\\n      as separate points. Color/marker by model family.\\\\n      Shaded intermediate-SC band (50–55%). Regime zone labels.\\\\n    narrative_intent: >\\\\n      The intermediate-SC region is narrow and model-specific. Outside it,\\\\n      SICA is either neutral (Type A) or harmful (Type C). No condition\\\\n      shows statistically significant improvement.\\\\n    design_notes:\\\\n      - \\\\\\\"Pattern A: regime bands — light shading 50-55% SC, labeled zones\\\\\\\"\\\\n      - \\\\\\\"Solid markers: n≥100; hollow: n<50\\\\\\\"\\\\n      - \\\\\\\"Horizontal Δ=0 reference line (dashed)\\\\\\\"\\\\n      - \\\\\\\"4 Mistral FOLIO seeds clustered at SC≈54-56%\\\\\\\"\\\\n      - \\\\\\\"Star or bold outline for significant effects (p<0.05)\\\\\\\"\\\\n      - \\\\\\\"Annotate LLaMA -4.41pp as 'upper boundary' of intermediate-SC\\\\\\\"\\\\n    placement: experiments\\\\n    aspect_ratio: \\\\\\\"4:3\\\\\\\"\\\\n    data_source: \\\\\\\"registry: all Table 1 conditions (~18 points + oracle excluded)\\\\\\\"\\\\n    status: \\\\\\\"EXISTS — needs regeneration with 4-seed + new experiments\\\\\\\"\\\\n\\\\n  - fig_id: fig3_sensitivity\\\\n    type: statistical\\\\n    tool: matplotlib\\\\n    description: >\\\\n      Two-panel figure. (a) K sensitivity: K=4,8,12,16,20 vs Δpp.\\\\n      (b) T sensitivity: T=0.3,0.5,0.7,1.0 vs Δpp. Both annotated\\\\n      with SC baseline at each point.\\\\n    narrative_intent: >\\\\n      SICA's optimal hyperparameters are fragile: K=12 is the only\\\\n      setting with Δ>2pp, T=0.7 is an isolated spike. Both peaks\\\\n      coincide with the lowest SC baseline, suggesting the effect\\\\n      reflects operating window rather than causal K/T contribution.\\\\n    design_notes:\\\\n      - \\\\\\\"Panel (a): line plot K vs Δ, secondary y-axis or annotation for SC\\\\\\\"\\\\n      - \\\\\\\"Panel (b): line plot T vs Δ, annotate SC at each T\\\\\\\"\\\\n      - \\\\\\\"Dashed Δ=0 reference line in both panels\\\\\\\"\\\\n      - \\\\\\\"Highlight K=12 and T=0.7 as peaks; annotate SC values\\\\\\\"\\\\n      - \\\\\\\"Pattern: minimal, 2-panel with shared y-axis scale if possible\\\\\\\"\\\\n    placement: analysis\\\\n    aspect_ratio: \\\\\\\"2:1\\\\\\\"\\\\n    data_source: >\\\\n      K sensitivity: exp-051 data (K=4,8,12,16,20).\\\\n      T sensitivity: exp-033 (T=0.7), exp-054 (T=1.0), exp-057 (T=0.3), exp-058 (T=0.5).\\\\n    status: \\\\\\\"EXISTS — needs regeneration with corrected data + T panel\\\\\\\"\\\\n\\\\n# ──────────────────────────────────────────────\\\\n# Table Plan\\\\n# ──────────────────────────────────────────────\\\\ntable_plan:\\\\n  # Main text tables\\\\n  - table_id: tab1_main_results\\\\n    type: comparison\\\\n    placement: experiments\\\\n    width: \\\\\\\"table*\\\\\\\"\\\\n    caption: >\\\\n      SICA vs SC across all model-domain conditions (K=12, T=0.7).\\\\n      Grouped by SC accuracy regime. Bold: significant effects (p<0.05).\\\\n      Bottom: oracle controls with gold FOL annotations.\\\\n    columns: [Model, Domain, n, \\\\\\\"SC (%)\\\\\\\", \\\\\\\"SICA (%)\\\\\\\", \\\\\\\"Δ (pp)\\\\\\\", \\\\\\\"p\\\\\\\"]\\\\n    data_source: \\\\\\\"registry: see experiments.registry_refs\\\\\\\"\\\\n    notes: >\\\\n      ~18 data rows grouped as: Type C / Intermediate-SC (4 seeds) /\\\\n      Type A (9 conditions) / Degenerate / Oracle. Footnotes for\\\\n      StrategyQA diagnostic and ICL condition.\\\\n\\\\n  - table_id: tab3_independence\\\\n    type: statistics\\\\n    placement: analysis\\\\n    width: \\\\\\\"table\\\\\\\"\\\\n    caption: >\\\\n      Condorcet independence metrics per model-domain condition.\\\\n      κ = Fleiss' kappa (K=12 traces), Eff-K = K/(1+(K-1)κ).\\\\n    columns: [Model (seed), Domain, \\\\\\\"κ\\\\\\\", \\\\\\\"Eff-K\\\\\\\", \\\\\\\"SC (%)\\\\\\\", \\\\\\\"SICA Δ (pp)\\\\\\\"]\\\\n    data_source: \\\\\\\"comp-1 verified κ values + registry\\\\\\\"\\\\n    notes: >\\\\n      ~14 rows including 4 Mistral FOLIO seeds, Mistral PW/LogiQA,\\\\n      Qwen family, Qwen3 thinking mode.\\\\n\\\\n  - table_id: tab_method_interventions\\\\n    type: comparison\\\\n    placement: analysis\\\\n    width: \\\\\\\"table\\\\\\\"\\\\n    caption: >\\\\n      Method-level interventions targeting the independence bottleneck\\\\n      (Mistral-7B). Each targets a different aspect: ICG bypasses\\\\n      trace-constraint coupling, Contrastive adds adversarial scoring,\\\\n      Debate adds multi-role reasoning.\\\\n    columns: [Method, Target Aspect, \\\\\\\"FOLIO Δ (pp)\\\\\\\", \\\\\\\"LogiQA Δ (pp)\\\\\\\", Failure Mode]\\\\n    data_source: \\\\\\\"registry: exp-074, exp-074c, exp-075b, exp-076, exp-079, exp-080, exp-078\\\\\\\"\\\\n    notes: >\\\\n      3 methods × 2 datasets. ICG has multi-seed on FOLIO.\\\\n      Debate LogiQA (exp-078) may still be running; mark if unavailable.\\\\n\\\\n  - table_id: tab_kappa_generalization\\\\n    type: statistics\\\\n    placement: analysis\\\\n    width: \\\\\\\"table\\\\\\\"\\\\n    caption: >\\\\n      Independence-accuracy trade-off: Fleiss' κ and Eff-K across three\\\\n      aggregation methods on Mistral-7B FOLIO (exp-077). Debate achieves\\\\n      the highest Eff-K but collapses accuracy.\\\\n    columns: [Aggregation Method, \\\\\\\"κ\\\\\\\", \\\\\\\"Eff-K\\\\\\\", \\\\\\\"Nominal K\\\\\\\", \\\\\\\"Δ (pp)\\\\\\\"]\\\\n    data_source: \\\\\\\"registry: exp-077\\\\\\\"\\\\n    notes: >\\\\n      SC: κ=0.4384, Eff-K=2.02, K=10; Diverse-Prompt: κ=0.4030,\\\\n      Eff-K=2.21, K=12; Debate: κ=0.1549, Eff-K=4.44, K=12, Δ=-18.6pp.\\\\n      CAPSTONE finding: trade-off explains why same-model methods must fail.\\\\n\\\\n  # Appendix tables\\\\n  - table_id: tab_app_remediation\\\\n    type: comparison\\\\n    placement: appendix\\\\n    caption: \\\\\\\"Nine prompt-level remediation strategies.\\\\\\\"\\\\n    columns: [Strategy, Dimension, Key Metric, Result, exp_id]\\\\n\\\\n  - table_id: tab_app_entropy\\\\n    type: analysis\\\\n    placement: appendix\\\\n    caption: \\\\\\\"SICA Δ conditioned on per-problem answer entropy (high vs low).\\\\\\\"\\\\n    columns: [Model, Dataset, \\\\\\\"High-E n\\\\\\\", \\\\\\\"High-E Δ\\\\\\\", \\\\\\\"Low-E n\\\\\\\", \\\\\\\"Low-E Δ\\\\\\\"]\\\\n\\\\n  - table_id: tab_app_power_analysis\\\\n    type: analysis\\\\n    placement: appendix\\\\n    caption: \\\\\\\"Statistical power analysis for primary conditions.\\\\\\\"\\\\n\\\\n  - table_id: tab_app_bootstrap\\\\n    type: analysis\\\\n    placement: appendix\\\\n    caption: \\\\\\\"Bootstrap 95% CIs for selected conditions.\\\\\\\"\\\\n\\\\n  - table_id: tab_app_constraint_quality\\\\n    type: analysis\\\\n    placement: appendix\\\\n    caption: \\\\\\\"Constraint extraction quality metrics by model.\\\\\\\"\\\\n\\\\n  - table_id: tab_app_k_detail\\\\n    type: detail\\\\n    placement: appendix\\\\n    caption: \\\\\\\"K sensitivity: full metrics at each K value.\\\\\\\"\\\\n\\\\n# ──────────────────────────────────────────────\\\\n# Literature Strategy\\\\n# ──────────────────────────────────────────────\\\\nliterature_strategy:\\\\n  citation_budget: 42\\\\n  macro_context:\\\\n    - \\\\\\\"self-consistency and majority voting in LLM reasoning\\\\\\\"\\\\n    - \\\\\\\"neuro-symbolic methods combining LLMs with formal solvers\\\\\\\"\\\\n    - \\\\\\\"Condorcet Jury Theorem and ensemble independence\\\\\\\"\\\\n  micro_clusters:\\\\n    - cluster_name: \\\\\\\"self_consistency_and_variants\\\\\\\"\\\\n      target_count: 6\\\\n      must_cite:\\\\n        - \\\\\\\"Wang et al. 2023 (Self-Consistency)\\\\\\\"\\\\n        - \\\\\\\"Chen et al. 2024 (USC)\\\\\\\"\\\\n        - \\\\\\\"Loo et al. 2025 (SC scaling plateau)\\\\\\\"\\\\n        - \\\\\\\"Taubenfeld et al. 2025 (confidence-weighted SC)\\\\\\\"\\\\n        - \\\\\\\"Li et al. 2023 (DiVeRSe)\\\\\\\"\\\\n      search_queries:\\\\n        - \\\\\\\"self-consistency majority voting LLM reasoning 2024 2025\\\\\\\"\\\\n\\\\n    - cluster_name: \\\\\\\"symbolic_reasoning_llm\\\\\\\"\\\\n      target_count: 7\\\\n      must_cite:\\\\n        - \\\\\\\"Pan et al. 2023 (Logic-LM)\\\\\\\"\\\\n        - \\\\\\\"Olausson et al. 2023 (LINC)\\\\\\\"\\\\n        - \\\\\\\"Xu et al. 2026 (DyLoS)\\\\\\\"\\\\n        - \\\\\\\"Li et al. 2025 (Aristotle)\\\\\\\"\\\\n        - \\\\\\\"Wang et al. 2025 (FoVer)\\\\\\\"\\\\n      search_queries:\\\\n        - \\\\\\\"neuro-symbolic reasoning LLM formal logic solver 2025 2026\\\\\\\"\\\\n\\\\n    - cluster_name: \\\\\\\"condorcet_voting_theory\\\\\\\"\\\\n      target_count: 6\\\\n      must_cite:\\\\n        - \\\\\\\"Condorcet 1785\\\\\\\"\\\\n        - \\\\\\\"Austen-Smith & Banks 1996\\\\\\\"\\\\n        - \\\\\\\"Ladha 1992 (correlated voters)\\\\\\\"\\\\n        - \\\\\\\"Lefort et al. 2024 (arXiv:2409.00094)\\\\\\\"\\\\n        - \\\\\\\"Fleiss 1971 (kappa)\\\\\\\"\\\\n        - \\\\\\\"Kish 1965 (design effect / Eff-K)\\\\\\\"\\\\n      search_queries:\\\\n        - \\\\\\\"Condorcet jury theorem ensemble independence machine learning\\\\\\\"\\\\n\\\\n    - cluster_name: \\\\\\\"verification_reranking\\\\\\\"\\\\n      target_count: 4\\\\n      must_cite:\\\\n        - \\\\\\\"Cobbe et al. 2021 (ORM/GSM8K)\\\\\\\"\\\\n        - \\\\\\\"Lightman et al. 2023 (PRM)\\\\\\\"\\\\n        - \\\\\\\"Wang et al. 2024 (Math-Shepherd)\\\\\\\"\\\\n      search_queries:\\\\n        - \\\\\\\"process reward model verification LLM 2024\\\\\\\"\\\\n\\\\n    - cluster_name: \\\\\\\"test_time_compute\\\\\\\"\\\\n      target_count: 4\\\\n      must_cite:\\\\n        - \\\\\\\"Snell et al. 2025 (scaling test-time compute)\\\\\\\"\\\\n        - \\\\\\\"DeepSeek-AI 2025 (DeepSeek-R1)\\\\\\\"\\\\n      search_queries:\\\\n        - \\\\\\\"test-time compute scaling reasoning 2025 2026\\\\\\\"\\\\n\\\\n    - cluster_name: \\\\\\\"debate_multi_agent\\\\\\\"\\\\n      target_count: 3\\\\n      must_cite:\\\\n        - \\\\\\\"Liang et al. 2023 (multi-agent debate)\\\\\\\"\\\\n        - \\\\\\\"Du et al. 2023 (improving factuality via debate)\\\\\\\"\\\\n      search_queries:\\\\n        - \\\\\\\"LLM multi-agent debate reasoning 2024\\\\\\\"\\\\n\\\\n    - cluster_name: \\\\\\\"self_correction_negative\\\\\\\"\\\\n      target_count: 2\\\\n      must_cite:\\\\n        - \\\\\\\"Huang et al. 2024 (cannot self-correct reasoning)\\\\\\\"\\\\n      search_queries:\\\\n        - \\\\\\\"LLM self-correction limitation negative result 2024\\\\\\\"\\\\n\\\\n    - cluster_name: \\\\\\\"benchmarks\\\\\\\"\\\\n      target_count: 5\\\\n      must_cite:\\\\n        - \\\\\\\"Han et al. 2022 (FOLIO)\\\\\\\"\\\\n        - \\\\\\\"Tafjord et al. 2021 (ProofWriter)\\\\\\\"\\\\n        - \\\\\\\"Liu et al. 2020 (LogiQA)\\\\\\\"\\\\n        - \\\\\\\"Geva et al. 2021 (StrategyQA)\\\\\\\"\\\\n\\\\n    - cluster_name: \\\\\\\"constraint_satisfaction\\\\\\\"\\\\n      target_count: 2\\\\n      must_cite:\\\\n        - \\\\\\\"de Moura & Bjorner 2008 (Z3)\\\\\\\"\\\\n\\\\n    - cluster_name: \\\\\\\"oracle_diagnostic_methodology\\\\\\\"\\\\n      target_count: 2\\\\n      must_cite:\\\\n        - \\\\\\\"Press et al. 2023 (compositionality gap)\\\\\\\"\\\\n      search_queries:\\\\n        - \\\\\\\"oracle upper bound diagnosis pipeline bottleneck NLP\\\\\\\"\\\\n\\\\n# ──────────────────────────────────────────────\\\\n# Writing Order (strict serial)\\\\n# ──────────────────────────────────────────────\\\\nwriting_order:\\\\n  - method          # Foundation: Condorcet + SICA + Oracle + Method interventions\\\\n  - experiments     # Data-driven: Table 1 + oracle + replication + failure modes\\\\n  - analysis        # Deep dive: independence + extraction + entropy + K/T + remediation\\\\n  - related_work    # Positioning: standalone, can reference method/experiments\\\\n  - introduction    # Synthesis: depends on all above\\\\n  - discussion      # Interpretation: depends on all empirical\\\\n  - abstract        # Summary: last written\\\\n  - conclusion      # Summary: last written\\\\n\\\\n# ──────────────────────────────────────────────\\\\n# Page Budget (8pp main text target)\\\\n# ──────────────────────────────────────────────\\\\npage_budget:\\\\n  target: 8.0\\\\n  breakdown:\\\\n    abstract: 0.3\\\\n    introduction: 1.3\\\\n    related_work: 0.8\\\\n    method: 1.1\\\\n    experiments: 1.8\\\\n    analysis: 1.5\\\\n    discussion: 0.5\\\\n    conclusion: 0.3\\\\n    total_text: 7.6\\\\n    display_items_float: 0.4\\\\n  notes:\\\\n    - \\\\\\\"3 main-text figures + 3 main-text tables = 6 display items (within 4-7 budget for 8pp)\\\\\\\"\\\\n    - \\\\\\\"Oracle merged into Table 1 bottom rows (saves table float)\\\\\\\"\\\\n    - \\\\\\\"4-seed replication as rows in Table 1 (no separate table)\\\\\\\"\\\\n    - \\\\\\\"Prompt-level remediation: 1 paragraph main text + full table in appendix\\\\\\\"\\\\n    - \\\\\\\"Method interventions: compact table (3 rows) in main text\\\\\\\"\\\\n    - \\\\\\\"Entropy: compact paragraph + move detailed 8-condition table to appendix\\\\\\\"\\\\n\\\\n# ──────────────────────────────────────────────\\\\n# Key Data (truth source: registry, verified .tex)\\\\n# ──────────────────────────────────────────────\\\\nkey_data:\\\\n  hero_result:\\\\n    exp_id: exp-033\\\\n    model: Mistral-7B-Instruct-v0.3\\\\n    dataset: FOLIO-204\\\\n    seed: 42\\\\n    sc: 55.88\\\\n    sica: 59.31\\\\n    delta_pp: 3.43\\\\n    p: 0.092\\\\n    note: \\\\\\\"NOT significant at α=0.05. Directional trend only.\\\\\\\"\\\\n\\\\n  replication_4seed:\\\\n    - {exp_id: exp-033, seed: 42, sc: 55.88, delta_pp: 3.43, p: 0.092}\\\\n    - {exp_id: exp-052, seed: 123, sc: 54.41, delta_pp: 2.94, p: 0.070}\\\\n    - {exp_id: exp-053, seed: 456, sc: 55.88, delta_pp: 0.00, p: 1.0}\\\\n    - {exp_id: exp-067, seed: 789, sc: 54.41, delta_pp: -0.49, p: 1.0}\\\\n    mean_delta: 1.47\\\\n    note: \\\\\\\"2/4 marginal positive (p<0.10), 0/4 significant. Range +3.43 to -0.49.\\\\\\\"\\\\n\\\\n  oracle:\\\\n    - {exp_id: exp-031, dataset: FOLIO-204, oracle_acc: 89.71, sc: 75.49, delta_pp: 14.22, p: \\\\\\\"<0.001\\\\\\\"}\\\\n    - {exp_id: exp-022, dataset: PW-600, oracle_acc: 86.67, sc: 75.17, delta_pp: 11.50, p: \\\\\\\"<0.001\\\\\\\"}\\\\n    utilization: \\\\\\\"24.1% (best seed 3.43 / oracle 14.22)\\\\\\\"\\\\n\\\\n  type_c:\\\\n    exp_id: exp-046\\\\n    model: Mistral-7B\\\\n    dataset: ProofWriter-D5-600\\\\n    n: 600\\\\n    sc: 39.33\\\\n    sica: 36.50\\\\n    delta_pp: -2.83\\\\n    p: 0.014\\\\n\\\\n  independence:\\\\n    range_kappa: \\\\\\\"0.21–0.82 (instruction-tuned), 0.91 (thinking)\\\\\\\"\\\\n    range_eff_k: \\\\\\\"1.20–3.62\\\\\\\"\\\\n    mistral_folio_4seed_kappa: \\\\\\\"0.41–0.51\\\\\\\"\\\\n    mistral_folio_4seed_eff_k: \\\\\\\"1.8–2.2\\\\\\\"\\\\n\\\\n  method_interventions:\\\\n    - {method: ICG, folio_delta: \\\\\\\"-2.0/+1.5 (2 seeds)\\\\\\\", logiqa_delta: -0.5, mode: neutral}\\\\n    - {method: Contrastive, folio_delta: -9.31, logiqa_delta: \\\\\\\"pending\\\\\\\", mode: harmful}\\\\n    - {method: Debate, folio_delta: -18.63, logiqa_delta: \\\\\\\"pending (RUNNING)\\\\\\\", mode: catastrophic}\\\\n    note: \\\\\\\"All tested on Mistral-7B. 7B scale caveat.\\\\\\\"\\\\n\\\\n  kappa_generalization:\\\\n    exp_id: exp-077\\\\n    status: DONE\\\\n    note: \\\\\\\"CAPSTONE finding — independence-accuracy trade-off\\\\\\\"\\\\n    data:\\\\n      - {method: \\\\\\\"Self-Consistency\\\\\\\", kappa: 0.4384, eff_k: 2.02, nominal_k: 10}\\\\n      - {method: \\\\\\\"Diverse-Prompt\\\\\\\", kappa: 0.4030, eff_k: 2.21, nominal_k: 12}\\\\n      - {method: \\\\\\\"LLM-Debate\\\\\\\", kappa: 0.1549, eff_k: 4.44, nominal_k: 12, delta: -18.6}\\\\n    insight: >\\\\n      Methods that increase independence (Debate: κ↓) destroy accuracy (Δ=-18.6pp).\\\\n      Methods that preserve accuracy (Diverse-Prompt) cannot break correlation (κ≈SC).\\\\n      This is a Pareto frontier, not an engineering gap.\\\\n\\\\n  pending_data:\\\\n    - {exp_id: exp-074d, desc: \\\\\\\"ICG FOLIO seed456\\\\\\\", status: PREPARING}\\\\n    - {exp_id: exp-078, desc: \\\\\\\"Debate LogiQA\\\\\\\", status: RUNNING}\\\\n    - {exp_id: exp-080, desc: \\\\\\\"Contrastive LogiQA — check registry for final delta\\\\\\\", status: DONE}\\\\n    note: \\\\\\\"exp-077 DONE. Remaining expected by May 20 morning per Director\\\\\\\"\\\\n\\\", \\\"total_chars\\\": 35250, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/writing_plan.yaml\", \"content\": \"# Writing Plan — symb_invariant_consensus\\n# Generated: 2026-05-19T20:30:00Z\\n# Full Draft: Independence Bottleneck — \\\"Fundamental Limitation\\\" paper\\n# Target: EMNLP 2026 ARR May cycle\\n# Paper Agent Step 1 output\\n\\nmeta:\\n  venue: EMNLP 2026\\n  track: main (ARR May cycle)\\n  template: docs/paper/acl.sty\\n  template_note: \\\"ACL/EMNLP shared template already in paper directory\\\"\\n  page_limit: 8\\n  deadline: 2026-05-25\\n  title: >\\n    Beyond Self-Consistency: How Trace Independence Limits\\n    Symbolic Consensus in LLM Reasoning\\n  core_claim: >\\n    Same-model self-extraction of symbolic constraints inherits trace\\n    correlation (Fleiss' κ=0.21–0.82, Eff-K=1.20–3.62 for nominal K=12),\\n    creating a structural independence bottleneck. Oracle gold-FOL yields\\n    +14.22pp (p<0.001) proving aggregation is sound, but self-extraction\\n    captures only 24%. κ generalization across aggregation methods reveals\\n    a fundamental independence-accuracy trade-off: Debate reduces κ from\\n    0.44→0.15 (Eff-K 2→4.4) but collapses accuracy by -18.6pp. Same-model\\n    methods cannot increase independence without degrading the signal that\\n    makes aggregation useful.\\n  paper_type: \\\"Fundamental limitation analysis (Condorcet framework + empirical diagnosis + 12 remediation failures)\\\"\\n  framing: \\\"Independence Bottleneck — structural limitation of same-model self-extraction\\\"\\n  created_at: 2026-05-19T20:30:00Z\\n\\n# ──────────────────────────────────────────────\\n# Contributions (5)\\n# ──────────────────────────────────────────────\\ncontributions:\\n  - id: C1\\n    label: \\\"Independence Bottleneck Quantification\\\"\\n    status: VERIFIED\\n    claim: >\\n      Fleiss' κ=0.21–0.82 (instruction-tuned), 0.91 (thinking mode).\\n      Eff-K=1.20–3.62 at K=12. Mistral 4-seed κ=0.41–0.51 (stable).\\n      Qwen Eff-K≈1.2–1.5 → near-zero Δ; Mistral PW Eff-K=3.62 but\\n      SC=39% → negative Δ. Dual requirement: sufficient Eff-K AND SC.\\n    evidence: \\\"Table 3, §5.1\\\"\\n\\n  - id: C2\\n    label: \\\"Oracle Gap Localizes Extraction Bottleneck\\\"\\n    status: VERIFIED\\n    claim: >\\n      Gold FOL: +14.22pp FOLIO (p<0.001), +11.50pp PW (p<0.001).\\n      Self-extraction captures 24% of oracle ceiling (best seed +3.43pp\\n      vs +14.22pp). Aggregation mechanism sound; extraction quality is\\n      the binding bottleneck.\\n    evidence: \\\"Table 1 oracle rows, §4.3\\\"\\n\\n  - id: C3\\n    label: \\\"Regime-Dependent Effect with 4-Seed Replication\\\"\\n    status: VERIFIED\\n    claim: >\\n      Intermediate-SC (~50–55%): best seed +3.43pp (p=0.092, ns);\\n      4-seed mean +1.47pp; 2/4 marginal (p<0.10), 0/4 significant.\\n      Type A (SC≥60%): 9 conditions N>2,800, no significant positive;\\n      significant negatives at -2.50pp (p=0.011) and -4.41pp (p=0.093).\\n      Type C (SC≤40%): -2.83pp (p=0.014).\\n    evidence: \\\"Table 1, Figure 2, §4.1–4.3\\\"\\n\\n  - id: C4\\n    label: \\\"Independence-Accuracy Trade-off Is Fundamental\\\"\\n    status: VERIFIED\\n    claim: >\\n      κ generalization (exp-077) reveals why same-model methods must fail:\\n      SC κ=0.44 (Eff-K=2.02); Diverse-Prompt κ=0.40 (Eff-K=2.21, ≈SC);\\n      Debate κ=0.15 (Eff-K=4.44) but Δ=-18.6pp. Methods that increase\\n      independence (Debate) destroy accuracy; methods that preserve accuracy\\n      (ICG, Diverse-Prompt) cannot break correlation. 12 remediations\\n      (9 prompt + 3 method) all fail — not engineering failure but\\n      fundamental trade-off in same-model aggregation.\\n    evidence: \\\"§5.6, Table T7 (κ generalization), method intervention table\\\"\\n\\n  - id: C5\\n    label: \\\"Entropy Decomposition Reveals Regime Mechanism\\\"\\n    status: VERIFIED\\n    claim: >\\n      Low-entropy: SICA≈SC across all 8 conditions (Δ≈0). High-entropy\\n      direction regime-dependent: +12.8pp intermediate-SC, -8.2pp Type A.\\n      Explains dual-channel mechanism (voting diversity + constraint\\n      homogenization).\\n    evidence: \\\"§5.5, entropy analysis\\\"\\n\\n# ──────────────────────────────────────────────\\n# Paper Outline\\n# ──────────────────────────────────────────────\\npaper_outline:\\n  - section: abstract\\n    file: abstract.tex\\n    word_budget: 220\\n    core_bullets:\\n      - \\\"Problem: SC (majority voting) plateaus; CJT explains why — traces lack independence\\\"\\n      - \\\"SICA pipeline evaluated across 6 models, 3 formal reasoning domains, N>3,000, 4-seed replication\\\"\\n      - \\\"Independence quantification: κ=0.21–0.82, Eff-K=1.20–3.62 at K=12\\\"\\n      - \\\"Regime: +3.43pp intermediate-SC (ns), -2.83pp Type C (p=0.014), ~0 Type A\\\"\\n      - \\\"Oracle +14.22pp/+11.50pp proves aggregation sound; self-extraction 24%\\\"\\n      - \\\"12 remediations (9 prompt + 3 method) all fail — bottleneck is structural\\\"\\n      - \\\"C0+SC zero-cost deployment diagnostic; paths forward require independence\\\"\\n    dependencies: [experiments, analysis, method]\\n\\n  - section: introduction\\n    file: introduction.tex\\n    word_budget: 1300\\n    core_bullets:\\n      - \\\"Hook: Test-time compute scaling via SC improves reasoning—but plateaus. Adding more traces yields diminishing returns.\\\"\\n      - \\\"Gap: Neuro-symbolic methods (Logic-LM, DyLoS, FoVer) improve reasoning with external/trained components. Can same-model self-extraction of formal constraints break the SC plateau without external tools?\\\"\\n      - \\\"Insight: CJT requires voter independence. Same-model traces violate this (Eff-K=1.20–3.62 for K=12). Self-extracted constraints inherit the correlation structure.\\\"\\n      - \\\"Evaluation: SICA pipeline + Condorcet analysis + oracle control across 6 models × 3 domains, 4-seed replication\\\"\\n      - \\\"Key result: Oracle +14.22pp proves mechanism works; self-extraction captures 24%. 12 remediations all fail.\\\"\\n      - \\\"Contributions: C1–C5\\\"\\n    dependencies: [experiments, analysis]\\n    figures: [fig1_pipeline]\\n    citation_hints:\\n      - \\\"SC: Wang et al. 2023\\\"\\n      - \\\"SC plateau: Loo et al. 2025\\\"\\n      - \\\"Logic-LM: Pan et al. 2023\\\"\\n      - \\\"DyLoS: Xu et al. 2026\\\"\\n      - \\\"CJT: Condorcet 1785, Ladha 1992\\\"\\n      - \\\"Self-correction parallel: Huang et al. 2024\\\"\\n\\n  - section: related_work\\n    file: related_work.tex\\n    word_budget: 750\\n    core_bullets:\\n      - \\\"SC and extensions: Wang 2023, USC, weighted SC (Taubenfeld 2025), DiVeRSe, scaling plateaus (Loo 2025)\\\"\\n      - \\\"Neuro-symbolic reasoning: Logic-LM, LINC, DyLoS, Aristotle, FoVer — all use external/trained components; we test same-model self-extraction\\\"\\n      - \\\"Condorcet/voting theory: CJT, correlated voters (Ladha 1992), LLM ensembles (Lefort 2024 arXiv:2409.00094, closest prior work)\\\"\\n      - \\\"Verification and reranking: ORM (Cobbe 2021), PRM (Lightman 2023), Math-Shepherd — trained verifier paradigm\\\"\\n      - \\\"Self-X limitations: Huang 2024 self-correction ≈ structural parallel to self-extraction\\\"\\n      - \\\"Debate/multi-agent: Liang 2023, Du 2023 — different regime (multi-model or larger models)\\\"\\n    dependencies: []\\n\\n  - section: method\\n    file: method.tex\\n    word_budget: 1100\\n    subsections:\\n      - id: \\\"sec:condorcet\\\"\\n        title: \\\"Self-Consistency and the Condorcet Independence Assumption\\\"\\n        word_budget: 300\\n        bullets:\\n          - \\\"SC as majority voting: sample K reasoning traces, select most common answer\\\"\\n          - \\\"CJT: K independent voters each with p>0.5 → P(majority correct) → 1 as K→∞\\\"\\n          - \\\"LLM traces violate independence: same model, same prompt, only sampling noise\\\"\\n          - \\\"Eff-K = K/(1+(K-1)κ) via Kish (1965) design effect; κ = Fleiss' kappa (1971)\\\"\\n          - \\\"When Eff-K≈1, additional traces ≈ no new information → SC plateau\\\"\\n      - id: \\\"sec:sica-pipeline\\\"\\n        title: \\\"SICA Pipeline\\\"\\n        word_budget: 400\\n        bullets:\\n          - \\\"Step 1: Generate K reasoning traces at temperature T\\\"\\n          - \\\"Step 2: Extract FOL constraints from each trace at T_ext=0.3\\\"\\n          - \\\"Step 3: Syntactic deduplication across traces\\\"\\n          - \\\"Step 4: Weighted partial MAX-SAT — hard clauses (answer assertion), soft clauses (constraints weighted by occurrence count)\\\"\\n          - \\\"Step 5: Z3 solver evaluates each candidate; answer with highest satisfiable weight selected\\\"\\n          - \\\"Timeout: 10s per candidate answer\\\"\\n      - id: \\\"sec:oracle-design\\\"\\n        title: \\\"Oracle Control Design\\\"\\n        word_budget: 200\\n        bullets:\\n          - \\\"Replace self-extracted constraints with gold FOL annotations (FOLIO) or gold DSL (ProofWriter)\\\"\\n          - \\\"Same Z3 evaluation pipeline; only constraint source changes\\\"\\n          - \\\"Causal intervention: isolates constraint quality from aggregation mechanism\\\"\\n      - id: \\\"sec:method-interventions\\\"\\n        title: \\\"Method-Level Interventions\\\"\\n        word_budget: 150\\n        bullets:\\n          - \\\"ICG: Generate constraints independently of traces (bypass trace-constraint coupling)\\\"\\n          - \\\"Contrastive: Pro/con constraint scoring per candidate answer\\\"\\n          - \\\"Debate: Proposer/Critic/Defense chain before constraint extraction\\\"\\n          - \\\"Each targets a different bottleneck aspect\\\"\\n    dependencies: []\\n    figures: [fig1_pipeline]\\n\\n  - section: experiments\\n    file: experiments.tex\\n    word_budget: 1800\\n    subsections:\\n      - id: \\\"sec:exp-setup\\\"\\n        title: \\\"Experimental Setup\\\"\\n        word_budget: 300\\n        bullets:\\n          - \\\"6 models: Mistral-7B-Instruct-v0.3, LLaMA-3.1-8B-Instruct, Qwen2.5-7B-Instruct, Qwen2.5-14B-Instruct, Qwen3-14B (non-thinking), Qwen3-14B (thinking mode for κ analysis)\\\"\\n          - \\\"3 formal reasoning domains: FOLIO (n=204), ProofWriter depth-5 (n=600), LogiQA (n=200)\\\"\\n          - \\\"Cross-domain diagnostic: StrategyQA (n=200)\\\"\\n          - \\\"Degenerate probes: QwQ-32B (AIME 2024), Qwen2.5-14B (GSM8K)\\\"\\n          - \\\"Default: K=12, T=0.7, T_ext=0.3, Z3 timeout 10s\\\"\\n          - \\\"Metrics: accuracy (%), Δ=SICA−SC (pp), McNemar exact test α=0.05\\\"\\n          - \\\"4-seed replication on primary condition (Mistral-7B FOLIO)\\\"\\n      - id: \\\"sec:main-results\\\"\\n        title: \\\"Main Results: A Regime-Dependent Effect\\\"\\n        word_budget: 500\\n        bullets:\\n          - \\\"Table 1: ~18 conditions grouped by regime + 2 oracle rows\\\"\\n          - \\\"Intermediate-SC (SC~50–55%): Mistral FOLIO best seed +3.43pp (p=0.092 ns); 4-seed mean +1.47pp; Mistral LogiQA +0.50pp\\\"\\n          - \\\"Type A (SC≥60%): 9 conditions N>2,800; no significant positive effect\\\"\\n          - \\\"  Significant negatives: Qwen14B PW -2.50pp (p=0.011); Mistral PW -2.83pp (p=0.014)\\\"\\n          - \\\"  LLaMA FOLIO -4.41pp (p=0.093, marginal)\\\"\\n          - \\\"  Qwen3-14B FOLIO -0.49pp, PW +0.67pp — generational scaling does not help\\\"\\n          - \\\"Type C (SC≤40%): Mistral PW-D5 Δ=-2.83pp p=0.014 — SICA significantly hurts\\\"\\n          - \\\"Degenerate: C0<5% → SICA≡SC by construction\\\"\\n          - \\\"Figure 2: SC vs Δ scatter showing regime boundaries\\\"\\n      - id: \\\"sec:oracle\\\"\\n        title: \\\"Oracle Control: Aggregation Is Sound\\\"\\n        word_budget: 250\\n        bullets:\\n          - \\\"FOLIO: oracle-SICA 89.71% vs SC 75.49% (+14.22pp, p<0.001)\\\"\\n          - \\\"ProofWriter: oracle-SICA 86.67% vs SC 75.17% (+11.50pp, p<0.001)\\\"\\n          - \\\"Self-extraction captures only 24.1% of FOLIO oracle ceiling\\\"\\n          - \\\"Aggregation mechanism is sound; extraction quality is binding constraint\\\"\\n      - id: \\\"sec:replication\\\"\\n        title: \\\"Four-Seed Replication\\\"\\n        word_budget: 250\\n        bullets:\\n          - \\\"Mistral-7B FOLIO-204: seeds 42, 123, 456, 789\\\"\\n          - \\\"s42: Δ=+3.43pp p=0.092; s123: +2.94pp p=0.070; s456: 0.00pp p=1.0; s789: -0.49pp p=1.0\\\"\\n          - \\\"2/4 marginal positive (p<0.10); 0/4 reaches p<0.05\\\"\\n          - \\\"4-seed mean: +1.47pp; range: +3.43 to -0.49\\\"\\n          - \\\"Fragility itself is the finding — motivates independence analysis\\\"\\n      - id: \\\"sec:failure-modes\\\"\\n        title: \\\"Failure Mode Analysis\\\"\\n        word_budget: 250\\n        bullets:\\n          - \\\"Type A: consistent traces → constraints mirror model's answers → MAX-SAT degenerates to counting\\\"\\n          - \\\"Type B: domain not formalizable (LogiQA contradiction rate 0.8%)\\\"\\n          - \\\"Type C: predominantly wrong traces → wrong constraints → solver amplifies errors\\\"\\n    dependencies: []\\n    tables: [tab1_main_results]\\n    figures: [fig2_regime_scatter]\\n    registry_refs:\\n      - exp-033  # Mistral FOLIO s42 (hero)\\n      - exp-052  # Mistral FOLIO s123\\n      - exp-053  # Mistral FOLIO s456\\n      - exp-067  # Mistral FOLIO s789\\n      - exp-046  # Mistral PW-600 (Type C)\\n      - exp-049b # Mistral LogiQA\\n      - exp-063  # LLaMA FOLIO\\n      - exp-019  # LLaMA StrategyQA\\n      - exp-061  # Qwen2.5-7B FOLIO\\n      - exp-026  # Qwen2.5-14B FOLIO (regen)\\n      - exp-038  # Qwen2.5-14B LogiQA\\n      - exp-039  # Qwen2.5-14B PW-600\\n      - exp-044b # Qwen2.5-14B FOLIO ICL\\n      - exp-027  # Qwen3-14B FOLIO\\n      - exp-040  # Qwen3-14B PW-600\\n      - exp-031  # Oracle FOLIO\\n      - exp-022  # Oracle PW\\n\\n  - section: analysis\\n    file: analysis.tex\\n    word_budget: 1500\\n    subsections:\\n      - id: \\\"sec:effective-k\\\"\\n        title: \\\"Condorcet Independence Analysis\\\"\\n        word_budget: 350\\n        bullets:\\n          - \\\"Table 3: Fleiss' κ and Eff-K per model-domain condition\\\"\\n          - \\\"Mistral FOLIO 4 seeds: κ=0.41–0.51, Eff-K=1.8–2.2 (cross-seed stable)\\\"\\n          - \\\"Qwen family: κ=0.66–0.82, Eff-K=1.2–1.5 → all near-zero Δ\\\"\\n          - \\\"Mistral PW: κ=0.21, Eff-K=3.62 but SC=39% → negative (highest independence, insufficient quality)\\\"\\n          - \\\"Qwen3-14B thinking: κ=0.91, Eff-K=1.09 → 'better reasoning' worsens independence\\\"\\n          - \\\"Dual requirement: need both sufficient Eff-K AND sufficient SC\\\"\\n          - \\\"Explains SC plateau: traces beyond Eff-K provide no new information\\\"\\n      - id: \\\"sec:extraction-taxonomy\\\"\\n        title: \\\"Constraint Quality Analysis\\\"\\n        word_budget: 200\\n        bullets:\\n          - \\\"Discriminative rate: ~8.2% (95% CI [7.6, 8.8])\\\"\\n          - \\\"Removing non-discriminative constraints: 0 gain → problem is direction not quality\\\"\\n          - \\\"Variable naming: 56.4% cross-trace constraint pairs share zero Z3 variables\\\"\\n          - \\\"~92% constraints ARE discriminative but discriminate in same direction as model bias\\\"\\n      - id: \\\"sec:entropy\\\"\\n        title: \\\"Entropy Decomposition\\\"\\n        word_budget: 200\\n        bullets:\\n          - \\\"Per-problem answer entropy separates SICA operating point\\\"\\n          - \\\"Low-entropy: SICA≈SC across all 8 conditions (Δ≈0) — traces agree, constraints add nothing\\\"\\n          - \\\"High-entropy: regime-dependent — +12.8pp intermediate-SC (s42), -8.2pp Type A (Qwen14B)\\\"\\n          - \\\"High-entropy proportion: Mistral 38% vs Qwen 18% → explains model-level Δ differences\\\"\\n          - \\\"Mechanism: low-entropy = direct CJT channel; high-entropy = indirect constraint channel\\\"\\n      - id: \\\"sec:ablation\\\"\\n        title: \\\"MAX-SAT Ablation\\\"\\n        word_budget: 100\\n        bullets:\\n          - \\\"MAX-SAT vs count-only: 803/804 agreement (Qwen14B, n=804)\\\"\\n          - \\\"Self-extracted constraints carry no signal beyond vote counts in high-SC regime\\\"\\n          - \\\"Confirms independence bottleneck causes MAX-SAT to degenerate\\\"\\n      - id: \\\"sec:k-t-sensitivity\\\"\\n        title: \\\"K and Temperature Sensitivity\\\"\\n        word_budget: 200\\n        bullets:\\n          - \\\"K sensitivity: K=4(-1.47), K=8(-1.96), K=12(+3.43), K=16(+1.47), K=20(+1.96)\\\"\\n          - \\\"K=12 is only setting with Δ>2pp; not clean inverted-U\\\"\\n          - \\\"T sensitivity: T=0.3(-1.47), T=0.5(-0.98), T=0.7(+3.43), T=1.0(0.00)\\\"\\n          - \\\"T=0.7 is isolated spike; only 1/4 temperatures positive\\\"\\n          - \\\"Both K=12 and T=0.7 coincide with lowest SC baseline → confound with operating window\\\"\\n          - \\\"Figure 3: two-panel K/T sensitivity plot\\\"\\n      - id: \\\"sec:remediation\\\"\\n        title: \\\"Remediation Analysis\\\"\\n        word_budget: 350\\n        bullets:\\n          - \\\"--- Prompt-level (9 strategies, 6 dimensions) ---\\\"\\n          - \\\"Prompting: contrastive extraction (disc_rate 8.2%→6.0%, Δ still mirrors bias)\\\"\\n          - \\\"Architecture: cross-model bilateral (weak→strong: 0% disc; strong→weak: ±1pp of self)\\\"\\n          - \\\"Capability: generational scaling Qwen3-14B (+0.49pp ns)\\\"\\n          - \\\"Verification: Z3 feedback (0.9% UNSAT), cross-trace UNSAT (56.4% zero shared vars)\\\"\\n          - \\\"Diversity: multi-temp (Δ=0.00pp), T=1.0 (Δ=0.00pp — collapse from +3.43)\\\"\\n          - \\\"Filtering: discriminative constraint filtering (0 gain), consistency filtering (reverts to SC)\\\"\\n          - \\\"ICL with gold FOL examples (+0.50pp ns)\\\"\\n          - \\\"--- Method-level (3 methods × 2 datasets) ---\\\"\\n          - \\\"ICG (Independent Constraint Gen.): FOLIO Δ=-2.0/+1.5pp (noise), LogiQA -0.5pp → neutral\\\"\\n          - \\\"  Insight: independent constraints ≈ trace-sourced → bias from problem understanding stage\\\"\\n          - \\\"Contrastive (Pro/Con Scoring): FOLIO -9.3pp, LogiQA pending → harmful\\\"\\n          - \\\"  Insight: 26% degenerate scoring, pro/con imbalance (94 pro vs 65 con)\\\"\\n          - \\\"Debate (Proposer/Critic): FOLIO -18.6pp, LogiQA pending → catastrophic\\\"\\n          - \\\"  Insight: 7B role-play degradation; same-model debate = same bias + cognitive overhead\\\"\\n          - \\\"Scale caveat: all method-level tested at 7B; 14B+ may differ\\\"\\n          - \\\"--- κ Generalization: Independence-Accuracy Trade-off (exp-077, CAPSTONE) ---\\\"\\n          - \\\"Table T7: SC κ=0.44 Eff-K=2.02 | Diverse-Prompt κ=0.40 Eff-K=2.21 | Debate κ=0.15 Eff-K=4.44\\\"\\n          - \\\"Diverse-Prompt ≈ SC κ → changing prompts cannot break correlation\\\"\\n          - \\\"Debate breaks κ (0.44→0.15) but accuracy collapses (-18.6pp)\\\"\\n          - \\\"FUNDAMENTAL TRADE-OFF: methods that increase independence destroy accuracy; methods that preserve accuracy cannot break correlation\\\"\\n          - \\\"This explains WHY same-model methods must fail — not just that they do\\\"\\n          - \\\"Implication: breaking bottleneck requires cross-model or external signal (consistent with oracle)\\\"\\n    dependencies: [experiments]\\n    tables: [tab3_independence, tab_method_interventions, tab_kappa_generalization]\\n    figures: [fig3_sensitivity]\\n    registry_refs:\\n      - exp-029  # contrastive prompting\\n      - exp-030  # cross-model extraction\\n      - exp-059  # cross-model Qwen3→Mistral\\n      - exp-060  # cross-model Qwen14B→Mistral\\n      - exp-027  # Qwen3-14B (generational)\\n      - exp-036  # Z3 feedback\\n      - exp-036b # cross-trace UNSAT\\n      - exp-043  # consistency filtering\\n      - exp-055  # multi-temp\\n      - exp-054  # T=1.0\\n      - exp-057  # T=0.3\\n      - exp-058  # T=0.5\\n      - exp-044b # ICL gold FOL\\n      - exp-074  # ICG FOLIO s42\\n      - exp-074c # ICG FOLIO s123\\n      - exp-075b # Contrastive FOLIO\\n      - exp-076  # Debate FOLIO\\n      - exp-079  # ICG LogiQA\\n      - exp-080  # Contrastive LogiQA\\n      - exp-078  # Debate LogiQA (RUNNING)\\n      - exp-077  # κ generalization (CAPSTONE)\\n\\n  - section: discussion\\n    file: discussion.tex\\n    word_budget: 450\\n    core_bullets:\\n      - \\\"Oracle causally isolates: aggregation mechanism sound, extraction is binding bottleneck\\\"\\n      - \\\"Dual-channel mechanism: direct (voting diversity → SC plateau) + indirect (constraint homogenization → MAX-SAT degeneration)\\\"\\n      - \\\"Oracle disambiguates: gold constraints on same correlated traces yield +14.22pp → indirect channel is proximal bottleneck\\\"\\n      - \\\"Independence-accuracy trade-off (exp-077): Debate breaks κ (0.44→0.15) but collapses accuracy (-18.6pp). Diverse-Prompt ≈ SC κ. Same-model methods face a fundamental Pareto frontier.\\\"\\n      - \\\"This trade-off explains WHY same-model methods must fail, not just that they do. Breaking correlation within a single model's distribution necessarily degrades the signal.\\\"\\n      - \\\"Published methods (DyLoS, Aristotle, FoVer, Logic-LM) bypass same-model extraction — consistent with trade-off: cross-model/external sources are naturally independent without sacrificing quality\\\"\\n      - \\\"Statistical evidence: 0/4 seeds significant positive; only significant effects are negative\\\"\\n      - \\\"C0+SC deployment diagnostic: C0<5%→degenerate, high SC→confirmation bias, low SC→error amplification\\\"\\n      - \\\"Three paths forward trade simplicity for independence: trained extractors, external provers, multi-model pipelines — all introduce signal outside the model's own distribution\\\"\\n    dependencies: [experiments, analysis]\\n\\n  - section: conclusion\\n    file: conclusion.tex\\n    word_budget: 300\\n    core_bullets:\\n      - \\\"SICA evaluated: 6 models spanning 3 families, 3 reasoning domains, N>3,000, 4-seed replication\\\"\\n      - \\\"Independence bottleneck: κ=0.21–0.82, Eff-K=1.20–3.62 → explains SC plateau and SICA failure\\\"\\n      - \\\"Intermediate-SC region: +3.43pp best seed (ns), 4-seed mean +1.47pp (2/4 positive, 2/4 null/negative)\\\"\\n      - \\\"Oracle +14.22pp/+11.50pp (p<0.001); 12 remediations all fail; independence-accuracy trade-off explains why\\\"\\n      - \\\"Limitations: trained extractors untested, narrow intermediate-SC zone, 7B-scale method testing, formal reasoning domains only\\\"\\n    dependencies: [experiments, analysis]\\n\\n# ──────────────────────────────────────────────\\n# Visualization Plan\\n# ──────────────────────────────────────────────\\nvisualization_plan:\\n  - fig_id: fig1_pipeline\\n    type: conceptual\\n    tool: matplotlib\\n    description: >\\n      SICA pipeline diagram: K traces → FOL constraint extraction →\\n      dedup → weighted partial MAX-SAT (Z3) → answer selection.\\n      Oracle branch replaces self-extracted constraints with gold FOL.\\n      Independence bottleneck annotation at extraction stage.\\n    narrative_intent: >\\n      The pipeline looks like it should introduce independent symbolic\\n      signal, but self-extraction inherits the same trace correlation —\\n      the independence bottleneck manifests at the extraction stage.\\n    design_notes:\\n      - \\\"Existing figure in paper; update to annotate independence bottleneck clearly\\\"\\n      - \\\"Add oracle branch as parallel path with green highlight\\\"\\n      - \\\"Add method-level intervention points (ICG/Contrastive/Debate) as annotation\\\"\\n    placement: method\\n    aspect_ratio: \\\"16:6\\\"\\n    data_source: \\\"manual (diagram)\\\"\\n    status: \\\"EXISTS — label update needed\\\"\\n\\n  - fig_id: fig2_regime_scatter\\n    type: statistical\\n    tool: matplotlib\\n    description: >\\n      SC accuracy (x-axis) vs SICA Δpp (y-axis) scatter plot.\\n      All model-domain conditions from Table 1. 4 replication seeds\\n      as separate points. Color/marker by model family.\\n      Shaded intermediate-SC band (50–55%). Regime zone labels.\\n    narrative_intent: >\\n      The intermediate-SC region is narrow and model-specific. Outside it,\\n      SICA is either neutral (Type A) or harmful (Type C). No condition\\n      shows statistically significant improvement.\\n    design_notes:\\n      - \\\"Pattern A: regime bands — light shading 50-55% SC, labeled zones\\\"\\n      - \\\"Solid markers: n≥100; hollow: n<50\\\"\\n      - \\\"Horizontal Δ=0 reference line (dashed)\\\"\\n      - \\\"4 Mistral FOLIO seeds clustered at SC≈54-56%\\\"\\n      - \\\"Star or bold outline for significant effects (p<0.05)\\\"\\n      - \\\"Annotate LLaMA -4.41pp as 'upper boundary' of intermediate-SC\\\"\\n    placement: experiments\\n    aspect_ratio: \\\"4:3\\\"\\n    data_source: \\\"registry: all Table 1 conditions (~18 points + oracle excluded)\\\"\\n    status: \\\"EXISTS — needs regeneration with 4-seed + new experiments\\\"\\n\\n  - fig_id: fig3_sensitivity\\n    type: statistical\\n    tool: matplotlib\\n    description: >\\n      Two-panel figure. (a) K sensitivity: K=4,8,12,16,20 vs Δpp.\\n      (b) T sensitivity: T=0.3,0.5,0.7,1.0 vs Δpp. Both annotated\\n      with SC baseline at each point.\\n    narrative_intent: >\\n      SICA's optimal hyperparameters are fragile: K=12 is the only\\n      setting with Δ>2pp, T=0.7 is an isolated spike. Both peaks\\n      coincide with the lowest SC baseline, suggesting the effect\\n      reflects operating window rather than causal K/T contribution.\\n    design_notes:\\n      - \\\"Panel (a): line plot K vs Δ, secondary y-axis or annotation for SC\\\"\\n      - \\\"Panel (b): line plot T vs Δ, annotate SC at each T\\\"\\n      - \\\"Dashed Δ=0 reference line in both panels\\\"\\n      - \\\"Highlight K=12 and T=0.7 as peaks; annotate SC values\\\"\\n      - \\\"Pattern: minimal, 2-panel with shared y-axis scale if possible\\\"\\n    placement: analysis\\n    aspect_ratio: \\\"2:1\\\"\\n    data_source: >\\n      K sensitivity: exp-051 data (K=4,8,12,16,20).\\n      T sensitivity: exp-033 (T=0.7), exp-054 (T=1.0), exp-057 (T=0.3), exp-058 (T=0.5).\\n    status: \\\"EXISTS — needs regeneration with corrected data + T panel\\\"\\n\\n# ──────────────────────────────────────────────\\n# Table Plan\\n# ──────────────────────────────────────────────\\ntable_plan:\\n  # Main text tables\\n  - table_id: tab1_main_results\\n    type: comparison\\n    placement: experiments\\n    width: \\\"table*\\\"\\n    caption: >\\n      SICA vs SC across all model-domain conditions (K=12, T=0.7).\\n      Grouped by SC accuracy regime. Bold: significant effects (p<0.05).\\n      Bottom: oracle controls with gold FOL annotations.\\n    columns: [Model, Domain, n, \\\"SC (%)\\\", \\\"SICA (%)\\\", \\\"Δ (pp)\\\", \\\"p\\\"]\\n    data_source: \\\"registry: see experiments.registry_refs\\\"\\n    notes: >\\n      ~18 data rows grouped as: Type C / Intermediate-SC (4 seeds) /\\n      Type A (9 conditions) / Degenerate / Oracle. Footnotes for\\n      StrategyQA diagnostic and ICL condition.\\n\\n  - table_id: tab3_independence\\n    type: statistics\\n    placement: analysis\\n    width: \\\"table\\\"\\n    caption: >\\n      Condorcet independence metrics per model-domain condition.\\n      κ = Fleiss' kappa (K=12 traces), Eff-K = K/(1+(K-1)κ).\\n    columns: [Model (seed), Domain, \\\"κ\\\", \\\"Eff-K\\\", \\\"SC (%)\\\", \\\"SICA Δ (pp)\\\"]\\n    data_source: \\\"comp-1 verified κ values + registry\\\"\\n    notes: >\\n      ~14 rows including 4 Mistral FOLIO seeds, Mistral PW/LogiQA,\\n      Qwen family, Qwen3 thinking mode.\\n\\n  - table_id: tab_method_interventions\\n    type: comparison\\n    placement: analysis\\n    width: \\\"table\\\"\\n    caption: >\\n      Method-level interventions targeting the independence bottleneck\\n      (Mistral-7B). Each targets a different aspect: ICG bypasses\\n      trace-constraint coupling, Contrastive adds adversarial scoring,\\n      Debate adds multi-role reasoning.\\n    columns: [Method, Target Aspect, \\\"FOLIO Δ (pp)\\\", \\\"LogiQA Δ (pp)\\\", Failure Mode]\\n    data_source: \\\"registry: exp-074, exp-074c, exp-075b, exp-076, exp-079, exp-080, exp-078\\\"\\n    notes: >\\n      3 methods × 2 datasets. ICG has multi-seed on FOLIO.\\n      Debate LogiQA (exp-078) may still be running; mark if unavailable.\\n\\n  - table_id: tab_kappa_generalization\\n    type: statistics\\n    placement: analysis\\n    width: \\\"table\\\"\\n    caption: >\\n      Independence-accuracy trade-off: Fleiss' κ and Eff-K across three\\n      aggregation methods on Mistral-7B FOLIO (exp-077). Debate achieves\\n      the highest Eff-K but collapses accuracy.\\n    columns: [Aggregation Method, \\\"κ\\\", \\\"Eff-K\\\", \\\"Nominal K\\\", \\\"Δ (pp)\\\"]\\n    data_source: \\\"registry: exp-077\\\"\\n    notes: >\\n      SC: κ=0.4384, Eff-K=2.02, K=10; Diverse-Prompt: κ=0.4030,\\n      Eff-K=2.21, K=12; Debate: κ=0.1549, Eff-K=4.44, K=12, Δ=-18.6pp.\\n      CAPSTONE finding: trade-off explains why same-model methods must fail.\\n\\n  # Appendix tables\\n  - table_id: tab_app_remediation\\n    type: comparison\\n    placement: appendix\\n    caption: \\\"Nine prompt-level remediation strategies.\\\"\\n    columns: [Strategy, Dimension, Key Metric, Result, exp_id]\\n\\n  - table_id: tab_app_entropy\\n    type: analysis\\n    placement: appendix\\n    caption: \\\"SICA Δ conditioned on per-problem answer entropy (high vs low).\\\"\\n    columns: [Model, Dataset, \\\"High-E n\\\", \\\"High-E Δ\\\", \\\"Low-E n\\\", \\\"Low-E Δ\\\"]\\n\\n  - table_id: tab_app_power_analysis\\n    type: analysis\\n    placement: appendix\\n    caption: \\\"Statistical power analysis for primary conditions.\\\"\\n\\n  - table_id: tab_app_bootstrap\\n    type: analysis\\n    placement: appendix\\n    caption: \\\"Bootstrap 95% CIs for selected conditions.\\\"\\n\\n  - table_id: tab_app_constraint_quality\\n    type: analysis\\n    placement: appendix\\n    caption: \\\"Constraint extraction quality metrics by model.\\\"\\n\\n  - table_id: tab_app_k_detail\\n    type: detail\\n    placement: appendix\\n    caption: \\\"K sensitivity: full metrics at each K value.\\\"\\n\\n# ──────────────────────────────────────────────\\n# Literature Strategy\\n# ──────────────────────────────────────────────\\nliterature_strategy:\\n  citation_budget: 42\\n  macro_context:\\n    - \\\"self-consistency and majority voting in LLM reasoning\\\"\\n    - \\\"neuro-symbolic methods combining LLMs with formal solvers\\\"\\n    - \\\"Condorcet Jury Theorem and ensemble independence\\\"\\n  micro_clusters:\\n    - cluster_name: \\\"self_consistency_and_variants\\\"\\n      target_count: 6\\n      must_cite:\\n        - \\\"Wang et al. 2023 (Self-Consistency)\\\"\\n        - \\\"Chen et al. 2024 (USC)\\\"\\n        - \\\"Loo et al. 2025 (SC scaling plateau)\\\"\\n        - \\\"Taubenfeld et al. 2025 (confidence-weighted SC)\\\"\\n        - \\\"Li et al. 2023 (DiVeRSe)\\\"\\n      search_queries:\\n        - \\\"self-consistency majority voting LLM reasoning 2024 2025\\\"\\n\\n    - cluster_name: \\\"symbolic_reasoning_llm\\\"\\n      target_count: 7\\n      must_cite:\\n        - \\\"Pan et al. 2023 (Logic-LM)\\\"\\n        - \\\"Olausson et al. 2023 (LINC)\\\"\\n        - \\\"Xu et al. 2026 (DyLoS)\\\"\\n        - \\\"Li et al. 2025 (Aristotle)\\\"\\n        - \\\"Wang et al. 2025 (FoVer)\\\"\\n      search_queries:\\n        - \\\"neuro-symbolic reasoning LLM formal logic solver 2025 2026\\\"\\n\\n    - cluster_name: \\\"condorcet_voting_theory\\\"\\n      target_count: 6\\n      must_cite:\\n        - \\\"Condorcet 1785\\\"\\n        - \\\"Austen-Smith & Banks 1996\\\"\\n        - \\\"Ladha 1992 (correlated voters)\\\"\\n        - \\\"Lefort et al. 2024 (arXiv:2409.00094)\\\"\\n        - \\\"Fleiss 1971 (kappa)\\\"\\n        - \\\"Kish 1965 (design effect / Eff-K)\\\"\\n      search_queries:\\n        - \\\"Condorcet jury theorem ensemble independence machine learning\\\"\\n\\n    - cluster_name: \\\"verification_reranking\\\"\\n      target_count: 4\\n      must_cite:\\n        - \\\"Cobbe et al. 2021 (ORM/GSM8K)\\\"\\n        - \\\"Lightman et al. 2023 (PRM)\\\"\\n        - \\\"Wang et al. 2024 (Math-Shepherd)\\\"\\n      search_queries:\\n        - \\\"process reward model verification LLM 2024\\\"\\n\\n    - cluster_name: \\\"test_time_compute\\\"\\n      target_count: 4\\n      must_cite:\\n        - \\\"Snell et al. 2025 (scaling test-time compute)\\\"\\n        - \\\"DeepSeek-AI 2025 (DeepSeek-R1)\\\"\\n      search_queries:\\n        - \\\"test-time compute scaling reasoning 2025 2026\\\"\\n\\n    - cluster_name: \\\"debate_multi_agent\\\"\\n      target_count: 3\\n      must_cite:\\n        - \\\"Liang et al. 2023 (multi-agent debate)\\\"\\n        - \\\"Du et al. 2023 (improving factuality via debate)\\\"\\n      search_queries:\\n        - \\\"LLM multi-agent debate reasoning 2024\\\"\\n\\n    - cluster_name: \\\"self_correction_negative\\\"\\n      target_count: 2\\n      must_cite:\\n        - \\\"Huang et al. 2024 (cannot self-correct reasoning)\\\"\\n      search_queries:\\n        - \\\"LLM self-correction limitation negative result 2024\\\"\\n\\n    - cluster_name: \\\"benchmarks\\\"\\n      target_count: 5\\n      must_cite:\\n        - \\\"Han et al. 2022 (FOLIO)\\\"\\n        - \\\"Tafjord et al. 2021 (ProofWriter)\\\"\\n        - \\\"Liu et al. 2020 (LogiQA)\\\"\\n        - \\\"Geva et al. 2021 (StrategyQA)\\\"\\n\\n    - cluster_name: \\\"constraint_satisfaction\\\"\\n      target_count: 2\\n      must_cite:\\n        - \\\"de Moura & Bjorner 2008 (Z3)\\\"\\n\\n    - cluster_name: \\\"oracle_diagnostic_methodology\\\"\\n      target_count: 2\\n      must_cite:\\n        - \\\"Press et al. 2023 (compositionality gap)\\\"\\n      search_queries:\\n        - \\\"oracle upper bound diagnosis pipeline bottleneck NLP\\\"\\n\\n# ──────────────────────────────────────────────\\n# Writing Order (strict serial)\\n# ──────────────────────────────────────────────\\nwriting_order:\\n  - method          # Foundation: Condorcet + SICA + Oracle + Method interventions\\n  - experiments     # Data-driven: Table 1 + oracle + replication + failure modes\\n  - analysis        # Deep dive: independence + extraction + entropy + K/T + remediation\\n  - related_work    # Positioning: standalone, can reference method/experiments\\n  - introduction    # Synthesis: depends on all above\\n  - discussion      # Interpretation: depends on all empirical\\n  - abstract        # Summary: last written\\n  - conclusion      # Summary: last written\\n\\n# ──────────────────────────────────────────────\\n# Page Budget (8pp main text target)\\n# ──────────────────────────────────────────────\\npage_budget:\\n  target: 8.0\\n  breakdown:\\n    abstract: 0.3\\n    introduction: 1.3\\n    related_work: 0.8\\n    method: 1.1\\n    experiments: 1.8\\n    analysis: 1.5\\n    discussion: 0.5\\n    conclusion: 0.3\\n    total_text: 7.6\\n    display_items_float: 0.4\\n  notes:\\n    - \\\"3 main-text figures + 3 main-text tables = 6 display items (within 4-7 budget for 8pp)\\\"\\n    - \\\"Oracle merged into Table 1 bottom rows (saves table float)\\\"\\n    - \\\"4-seed replication as rows in Table 1 (no separate table)\\\"\\n    - \\\"Prompt-level remediation: 1 paragraph main text + full table in appendix\\\"\\n    - \\\"Method interventions: compact table (3 rows) in main text\\\"\\n    - \\\"Entropy: compact paragraph + move detailed 8-condition table to appendix\\\"\\n\\n# ──────────────────────────────────────────────\\n# Key Data (truth source: registry, verified .tex)\\n# ──────────────────────────────────────────────\\nkey_data:\\n  hero_result:\\n    exp_id: exp-033\\n    model: Mistral-7B-Instruct-v0.3\\n    dataset: FOLIO-204\\n    seed: 42\\n    sc: 55.88\\n    sica: 59.31\\n    delta_pp: 3.43\\n    p: 0.092\\n    note: \\\"NOT significant at α=0.05. Directional trend only.\\\"\\n\\n  replication_4seed:\\n    - {exp_id: exp-033, seed: 42, sc: 55.88, delta_pp: 3.43, p: 0.092}\\n    - {exp_id: exp-052, seed: 123, sc: 54.41, delta_pp: 2.94, p: 0.070}\\n    - {exp_id: exp-053, seed: 456, sc: 55.88, delta_pp: 0.00, p: 1.0}\\n    - {exp_id: exp-067, seed: 789, sc: 54.41, delta_pp: -0.49, p: 1.0}\\n    mean_delta: 1.47\\n    note: \\\"2/4 marginal positive (p<0.10), 0/4 significant. Range +3.43 to -0.49.\\\"\\n\\n  oracle:\\n    - {exp_id: exp-031, dataset: FOLIO-204, oracle_acc: 89.71, sc: 75.49, delta_pp: 14.22, p: \\\"<0.001\\\"}\\n    - {exp_id: exp-022, dataset: PW-600, oracle_acc: 86.67, sc: 75.17, delta_pp: 11.50, p: \\\"<0.001\\\"}\\n    utilization: \\\"24.1% (best seed 3.43 / oracle 14.22)\\\"\\n\\n  type_c:\\n    exp_id: exp-046\\n    model: Mistral-7B\\n    dataset: ProofWriter-D5-600\\n    n: 600\\n    sc: 39.33\\n    sica: 36.50\\n    delta_pp: -2.83\\n    p: 0.014\\n\\n  independence:\\n    range_kappa: \\\"0.21–0.82 (instruction-tuned), 0.91 (thinking)\\\"\\n    range_eff_k: \\\"1.20–3.62\\\"\\n    mistral_folio_4seed_kappa: \\\"0.41–0.51\\\"\\n    mistral_folio_4seed_eff_k: \\\"1.8–2.2\\\"\\n\\n  method_interventions:\\n    - {method: ICG, folio_delta: \\\"-2.0/+1.5 (2 seeds)\\\", logiqa_delta: -0.5, mode: neutral}\\n    - {method: Contrastive, folio_delta: -9.31, logiqa_delta: \\\"pending\\\", mode: harmful}\\n    - {method: Debate, folio_delta: -18.63, logiqa_delta: \\\"pending (RUNNING)\\\", mode: catastrophic}\\n    note: \\\"All tested on Mistral-7B. 7B scale caveat.\\\"\\n\\n  kappa_generalization:\\n    exp_id: exp-077\\n    status: DONE\\n    note: \\\"CAPSTONE finding — independence-accuracy trade-off\\\"\\n    data:\\n      - {method: \\\"Self-Consistency\\\", kappa: 0.4384, eff_k: 2.02, nominal_k: 10}\\n      - {method: \\\"Diverse-Prompt\\\", kappa: 0.4030, eff_k: 2.21, nominal_k: 12}\\n      - {method: \\\"LLM-Debate\\\", kappa: 0.1549, eff_k: 4.44, nominal_k: 12, delta: -18.6}\\n    insight: >\\n      Methods that increase independence (Debate: κ↓) destroy accuracy (Δ=-18.6pp).\\n      Methods that preserve accuracy (Diverse-Prompt) cannot break correlation (κ≈SC).\\n      This is a Pareto frontier, not an engineering gap.\\n\\n  pending_data:\\n    - {exp_id: exp-074d, desc: \\\"ICG FOLIO seed456\\\", status: PREPARING}\\n    - {exp_id: exp-078, desc: \\\"Debate LogiQA\\\", status: RUNNING}\\n    - {exp_id: exp-080, desc: \\\"Contrastive LogiQA — check registry for final delta\\\", status: DONE}\\n    note: \\\"exp-077 DONE. Remaining expected by May 20 morning per Director\\\"\\n\", \"total_chars\": 35250, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "32cbf480-c5bb-4a08-82ea-0514a848ebaf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora"
}
```

</details>

---


### Tool call

_source line 8813 · 2026-05-20T09:35:48.911Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_017Tr6TLcs6Fc8Rv2CBggkKo`</summary>

```json
{
  "project": "symb_invariant_consensus",
  "limit": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1f321fa3-c68a-4f74-90a6-56038cf03999",
  "isSidechain": false,
  "requestId": "req_011CbDbPqJj9ZYvDsx3j3Yxz",
  "type": "assistant",
  "uuid": "51caf076-1012-4d3d-b45e-9a3243a00edd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Bvksz7RVr2DMr5TjduKFiV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 939,
      "cache_read_input_tokens": 134187,
      "output_tokens": 273,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 939,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 273,
          "cache_read_input_tokens": 134187,
          "cache_creation_input_tokens": 939,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 939
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

_source line 8814_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[服务器重启后首条消息] 当前日期: 2026-05-20。服务器刚重启，项目状态可能已更新。不要依赖对话历史中的状态信息，以 registry 当前值为准。  **用户消息：** [Director 指令] ## 写作任务：EMNLP 2026 ARR May 25 — Full Draft 更新  **DDL**: May 25, 2026（5 天） **模式**: Full Draft 更新…",
  "leafUuid": "51caf076-1012-4d3d-b45e-9a3243a00edd",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1"
}
```

---


### Runtime record

_source line 8815_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise paper results with oracle FOLIO constraint experiments",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1"
}
```

---


### Tool result

_source line 8816 · 2026-05-20T09:35:49.764Z_

<details><summary>↩ Tool result · `toolu_017Tr6TLcs6Fc8Rv2CBggkKo`</summary>

```text
Error: result (108,048 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-3-projects-symb-invariant-consensus--claude-sessions-paper-agent-644edc69/6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1/tool-results/mcp-agent-ml-research-read_registry-1779269749758.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-3-projects-symb-invariant-consensus--claude-sessions-paper-agent-644edc69/6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1/tool-results/mcp-agent-ml-research-read_registry-1779269749758.txt in sequential chunks until 100% of the content has been read.
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "51caf076-1012-4d3d-b45e-9a3243a00edd",
  "isSidechain": false,
  "promptId": "3f50ba00-7d30-45ec-b450-7010d531c858",
  "type": "user",
  "uuid": "932e0c2c-46c4-47cb-8e06-caea48468cba",
  "toolUseResult": "Error: result (108,048 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-3-projects-symb-invariant-consensus--claude-sessions-paper-agent-644edc69/6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1/tool-results/mcp-agent-ml-research-read_registry-1779269749758.txt.\nFormat: JSON with schema: {result: string}\nUse offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.\nREQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:\n- You MUST read the content from the file at /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-3-projects-symb-invariant-consensus--claude-sessions-paper-agent-644edc69/6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1/tool-results/mcp-agent-ml-research-read_registry-1779269749758.txt in sequential chunks until 100% of the content has been read.\n- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.\n- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***\n",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"exp-wave3-dir-i-z3-filter\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T09:23:12.344Z\", \"updated_at\": \"2026-05-20T09:25:19.523Z\", \"hypothesis\": \"Z3 Trace Filter: Per-trace FOL constraint set SAT/UNSAT check can identify internally contradictory traces; filtering them before SC voting will improve accuracy by removing logically flawed reasoning.\", \"conclusion\": \"negative\", \"metrics\": {\"n\": 204, \"sc_baseline\": 54.41, \"filtered_sc\": 53.92, \"delta_pp\": -0.49, \"unsat_traces\": 142, \"unsat_rate_pct\": 5.8, \"filter_precision_pct\": 49.12, \"questions_affected\": 7, \"improved\": 3, \"degraded\": 4}}, \"exp-wave3-dir-j-bootstrap\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T09:23:14.566Z\", \"updated_at\": \"2026-05-20T09:24:01.932Z\", \"hypothesis\": \"Bootstrapped Gold Approximation: Iterative conditional FOL extraction (using current best answer as condition) with Z3 consistency checks will progressively refine answers across rounds, converging to higher accuracy than single-pass SC.\", \"conclusion\": \"negative\", \"metrics\": {\"n\": 204, \"sc_baseline\": 54.41, \"r1_accuracy\": 56.86, \"r1_delta_pp\": 2.45, \"r1_flips\": 32, \"r1_improved\": 15, \"r1_degraded\": 10, \"r2_accuracy\": 54.41, \"r3_accuracy\": 54.9, \"r4_accuracy\": 54.41, \"r5_accuracy\": 52.45, \"convergence\": \"oscillating, no convergence\"}}, \"exp-cross-model-phase2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T09:20:34.520Z\", \"updated_at\": \"2026-05-20T09:21:07.052Z\", \"hypothesis\": \"Cross-model SICA: Aggregating traces from 3 model families (Mistral+LLaMA+Qwen, K=12 total) via SICA MAX-SAT will outperform cross-model SC by leveraging constraint diversity across architectures.\", \"conclusion\": \"negative\", \"metrics\": {\"n\": 204, \"cross_sc_accuracy\": 74.51, \"cross_sica_accuracy\": 74.02, \"delta_pp\": -0.49, \"mcnemar_p\": 1, \"config\": \"Mistral-7B(4) + LLaMA-8B(4) + Qwen-7B(4), K=12\"}}, \"exp-direction-d-cegis\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T08:53:01.301Z\", \"updated_at\": \"2026-05-20T09:20:32.244Z\", \"hypothesis\": \"CEGIS: Iterative counterexample-guided constraint refinement will improve SICA by using Z3 counterexamples to strengthen constraints across multiple rounds, breaking the single-pass extraction bottleneck.\", \"conclusion\": \"negative\", \"metrics\": {\"n\": 204, \"sc_baseline\": 54.41, \"r1_accuracy\": 57.84, \"r1_delta_pp\": 3.43, \"r2_accuracy\": 57.35, \"r2_delta_pp\": 2.94, \"r3_accuracy\": 57.84, \"r3_delta_pp\": 3.43, \"r1_unsat_traces\": 127, \"r2_unsat_traces\": 48, \"r3_unsat_traces\": 25, \"wall_time_min\": 51, \"extraction_calls\": 2448, \"refinement_calls\": 175}}, \"exp-confirmation-bias\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T08:53:05.574Z\", \"updated_at\": \"2026-05-20T08:55:26.899Z\", \"hypothesis\": \"Confirmation Bias quantification: Self-extracted constraints systematically point toward the majority answer even when it is wrong, creating a bias ratio significantly above 1.0 that explains SICA's failure mode.\", \"conclusion\": \"success\", \"metrics\": {\"bias_ratio\": 4.97, \"wrong_constraints_when_sica_errs\": 0.833, \"sica_errors_follow_sc\": 0.94}}, \"exp-cross-model-phase1\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T08:53:03.574Z\", \"updated_at\": \"2026-05-20T08:55:24.052Z\", \"hypothesis\": \"Cross-model aggregation: Mixing traces from different model families (Mistral/LLaMA/Qwen) will reduce inter-trace κ below the same-model ceiling of 0.41, increasing effective sample size.\", \"conclusion\": \"success\", \"metrics\": {\"kappa_cross\": 0.422, \"kappa_within\": 0.532, \"eff_k_cross\": 2.11, \"eff_k_within\": 1.52, \"accuracy_gain\": 0}}, \"exp-direction-e-abstention\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T08:52:59.761Z\", \"updated_at\": \"2026-05-20T08:55:21.063Z\", \"hypothesis\": \"Selective Abstention: Per-question answer entropy can serve as a reliable uncertainty signal; abstaining on high-entropy questions will improve accuracy on the remaining covered set.\", \"conclusion\": \"success\", \"metrics\": {\"auroc\": 0.673, \"coverage_80pct_delta_pp\": 4.4, \"coverage_60pct_delta_pp\": 8.8}}, \"exp-wild6-kappa-aware-sc\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T08:52:57.421Z\", \"updated_at\": \"2026-05-20T08:55:19.533Z\", \"hypothesis\": \"κ-aware SC: Weighting traces by per-question agreement level (inverse κ) in majority voting will improve SC by giving more weight to diverse-opinion questions where voting has more signal.\", \"conclusion\": \"negative\", \"metrics\": {\"conditions_tested\": 11, \"delta_pp_all\": 0, \"finding\": \"accuracy monotonically increases with agreement, SC already optimal\"}}, \"exp-wild1-max-unsat\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T08:52:55.446Z\", \"updated_at\": \"2026-05-20T08:55:17.946Z\", \"hypothesis\": \"MAX-UNSAT: Penalizing constraints in the unsatisfiable set (MIN-UNSAT variant) will improve SICA by actively downweighting contradictory constraints rather than only rewarding satisfiable ones.\", \"conclusion\": \"negative\", \"metrics\": {\"min_unsat_delta_pp\": -6.5, \"mean_excluded_constraints\": 1.3}}, \"exp-wild4-process-kappa\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T08:52:53.205Z\", \"updated_at\": \"2026-05-20T08:55:16.383Z\", \"hypothesis\": \"Process-κ: CoT reasoning process similarity (cosine) correlates with answer agreement, and measuring process-level κ reveals whether traces that agree on answers actually use similar reasoning paths.\", \"conclusion\": \"negative\", \"metrics\": {\"answer_kappa\": 0.4093, \"process_cosine_mean\": 0.6902, \"pearson_r\": -0.064, \"pearson_p\": 0.36, \"same_answer_diff_process_pct\": 9.3}}, \"exp-direction-a-prove\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T08:52:50.909Z\", \"updated_at\": \"2026-05-20T08:55:14.926Z\", \"hypothesis\": \"PROVE: LLM-generated verification code (verify() functions) can serve as external verifiers to rerank SC candidates, bypassing the self-extraction bottleneck.\", \"conclusion\": \"negative\", \"metrics\": {\"code_gen_rate\": 0.152, \"conclusive_rate\": 0.078, \"conclusive_accuracy\": 0.5, \"prove_fallback_accuracy\": 0.716, \"sc_baseline\": 0.735, \"delta_pp\": -1.9}}, \"exp-direction-b-deepconf\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T08:52:49.310Z\", \"updated_at\": \"2026-05-20T08:55:13.277Z\", \"hypothesis\": \"DeepConf: Low-confidence traces (by logprob) produce low-quality constraints; filtering them before SICA will improve accuracy by removing noise from the constraint pool.\", \"conclusion\": \"negative\", \"metrics\": {\"filtered_sc_75pct\": 52.9, \"filtered_sica_75pct\": 54.4, \"filtered_sc_50pct\": 52.9, \"logprob_correct\": -0.135, \"logprob_incorrect\": -0.141, \"delta_pp\": 0}}, \"exp-wild3-perturbation\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T08:47:10.815Z\", \"updated_at\": \"2026-05-20T08:48:02.574Z\", \"hypothesis\": \"Problem perturbation (variable renaming, premise reordering) will reduce inter-trace kappa by producing different reasoning paths for semantically equivalent problems, testing whether correlation comes from surface form vs model bias.\", \"conclusion\": \"negative\", \"metrics\": {\"original_k4_kappa\": 0.59, \"perturbed_k4_kappa\": 0.696, \"mixed_k8_kappa\": 0.627, \"original_sc_acc\": 80, \"perturbed_sc_acc\": 76.7, \"mixed_sc_acc\": 80}}, \"exp-wild2-ascii\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T08:47:08.985Z\", \"updated_at\": \"2026-05-20T08:48:01.074Z\", \"hypothesis\": \"ASCII padding in FOLIO prompts will reduce inter-trace Fleiss kappa by disrupting shared surface-level patterns, testing whether trace correlation comes from prompt content vs model architecture bias.\", \"conclusion\": \"negative\", \"metrics\": {\"group_a_standard_kappa\": 0.3906, \"group_b_fixed_padding_kappa\": 0.4006, \"group_c_variable_padding_kappa\": 0.3638, \"group_a_sc_acc\": 53.92, \"group_b_sc_acc\": 57.84, \"group_c_sc_acc\": 53.92}}, \"exp-084-debate-mistral-logiqa-seed123\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T22:33:19.983Z\", \"updated_at\": \"2026-05-20T02:47:44.350Z\", \"hypothesis\": \"Debate × Mistral-7B × LogiQA-200 seed=123 replication. exp-078 (seed=42) Δ=-23.0pp (catastrophic negative). Multi-seed 确认 Debate 在 LogiQA 上的大幅 negative 结果是否跨 seed 稳定。\", \"parent\": \"exp-078-debate-mistral-logiqa200\", \"conclusion\": \"negative\", \"metrics\": {\"n\": 200, \"debate_accuracy\": 0.29, \"sc_accuracy\": 0.505, \"delta\": -0.215, \"fallbacks\": 14, \"total_constraints\": 3220, \"wall_time_min\": 226.3}}, \"exp-082-contrastive-mistral-folio-seed123\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T21:27:49.643Z\", \"updated_at\": \"2026-05-20T01:00:18.542Z\", \"hypothesis\": \"Contrastive × Mistral-7B × FOLIO-204 seed=123 replication: verifying that the contrastive constraint generation pipeline produces consistent accuracy improvements over SC baseline when controlling for random seed, expecting accuracy within ±2pp of seed=42 run (exp-075b)\", \"parent\": \"exp-075b-contrastive-mistral-folio\", \"metrics\": {\"sc_accuracy\": 0.549, \"contrastive_accuracy\": 0.4951, \"delta\": -0.0539, \"n_samples\": 204, \"wall_time_min\": 206.3, \"degenerate_count\": 35, \"pro_constraints\": 1036, \"con_constraints\": 920}, \"conclusion\": \"negative\"}, \"exp-081-debate-mistral-folio-seed123\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T21:27:47.040Z\", \"updated_at\": \"2026-05-20T00:31:10.579Z\", \"hypothesis\": \"Debate × Mistral-7B × FOLIO-204 seed=123 replication: verifying that the debate-augmented constraint extraction pipeline produces consistent accuracy improvements over SC baseline when controlling for random seed, expecting accuracy within ±2pp of seed=42 run (exp-076)\", \"parent\": \"exp-076-debate-mistral-folio\", \"metrics\": {\"sc_accuracy\": 0.5588, \"debate_accuracy\": 0.4069, \"delta\": -0.152, \"n_samples\": 204, \"wall_time_min\": 177.6, \"fallbacks\": 18, \"both_correct\": 56, \"debate_improved\": 27, \"debate_degraded\": 58, \"both_wrong\": 63}, \"conclusion\": \"negative\"}, \"exp-085-contrastive-mistral-logiqa-seed123\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T22:37:05.631Z\", \"updated_at\": \"2026-05-20T00:21:11.042Z\", \"hypothesis\": \"Contrastive × Mistral-7B × LogiQA-200 seed=123 multi-seed replication。exp-080 (seed=42) Δ=-4.5pp (negative)。跨 seed 确认 Contrastive 在 LogiQA 上的 negative 结果稳定性，排除单 seed 偶然。\", \"parent\": \"exp-080-contrastive-mistral-logiqa200\", \"conclusion\": \"negative\", \"metrics\": {\"n\": 200, \"contrastive_accuracy\": 0.535, \"sc_accuracy\": 0.56, \"delta\": -0.025, \"delta_pp\": -2.5, \"contrastive_correct\": 107, \"sc_correct\": 112, \"k\": 12, \"k_contrast\": 3, \"temperature\": 0.7, \"seed\": 123, \"degenerate_count\": 51, \"total_pro_constraints\": 736, \"total_con_constraints\": 1059, \"wall_time_min\": 100.9}}, \"exp-013-constraint-ablation\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T00:08:40.394Z\", \"updated_at\": \"2026-05-20T00:09:33.110Z\", \"hypothesis\": \"MaxSAT satisfiability checking contributes minimal accuracy gains over naive constraint counting, because extracted constraints are too homogeneous (trace co-sourcing) to provide discriminative satisfiability signals. If SICA-MaxSAT ≈ SICA-count-only, the SAT solver is not the bottleneck — constraint quality is.\", \"conclusion\": \"success\", \"metrics\": {\"maxsat_acc\": 0.4229, \"count_only_acc\": 0.4216, \"random_weight_acc\": \"0.4206±0.0042\", \"sc_acc\": 0.4316, \"delta_maxsat_vs_countonly_pp\": 0.12, \"delta_maxsat_vs_sc_pp\": -0.87, \"agreement_maxsat_countonly\": 0.944, \"n_problems\": 804, \"folio_maxsat\": 0.5931, \"folio_count\": 0.5686, \"folio_sc\": 0.5441, \"pw_maxsat\": 0.365, \"pw_count\": 0.3717, \"pw_sc\": 0.3933}}, \"exp-075b-contrastive-mistral-folio\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T20:31:03.796Z\", \"updated_at\": \"2026-05-19T23:09:01.115Z\", \"hypothesis\": \"Contrastive × Mistral-7B × FOLIO-204 重跑（修复 normalization bug 后）。对每个候选答案生成 pro/con FOL 约束，用 normalized contrastive 评分代替同源约束。exp-075 因 session crash + normalization bug 失败。如果 normalized contrastive 约束提供独立于 traces 的判别信号，delta(Contrastive vs SC) > delta(SICA vs SC)。\", \"parent\": \"exp-075-contrastive-mistral-folio\", \"conclusion\": \"negative\", \"metrics\": {\"sc_accuracy\": 0.5686, \"contrastive_accuracy\": 0.4755, \"delta\": -0.0931, \"n_samples\": 204, \"wall_time_min\": 193.6, \"degenerate_count\": 41}}, \"exp-080-contrastive-mistral-logiqa200\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T20:14:59.602Z\", \"updated_at\": \"2026-05-19T22:47:45.758Z\", \"hypothesis\": \"Contrastive constraint generation with MAX-SAT consensus (SICA) transfers from FOLIO to LogiQA, improving accuracy over self-consistency baseline on 200 LogiQA problems with Mistral-7B (seed=42).\", \"parent\": \"exp-075b-contrastive-mistral-folio\", \"conclusion\": \"negative\", \"metrics\": {\"n\": 200, \"contrastive_accuracy\": 0.455, \"sc_accuracy\": 0.5, \"delta\": -0.045, \"k\": 12, \"k_contrast\": 3, \"temperature\": 0.7, \"seed\": 42, \"total_wall_time_s\": 6645.9, \"total_pro_constraints\": 762, \"total_con_constraints\": 1192, \"degenerate_count\": 42}}, \"exp-078-debate-mistral-logiqa200\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T18:51:21.070Z\", \"updated_at\": \"2026-05-19T22:29:09.471Z\", \"hypothesis\": \"Debate-augmented extraction with MAX-SAT consensus (SICA) transfers cross-dataset from FOLIO (3-class) to LogiQA (4-choice multichoice), maintaining accuracy gains over self-consistency baseline on 200 LogiQA problems with Mistral-7B.\", \"parent\": \"exp-076-debate-mistral-folio\", \"conclusion\": \"negative\", \"metrics\": {\"sc_accuracy\": 0.5, \"debate_accuracy\": 0.27, \"delta\": -0.23, \"n_samples\": 200, \"wall_time_min\": 211.5, \"fallbacks\": 16}}, \"exp-078\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T22:27:35.893Z\", \"updated_at\": \"2026-05-19T22:28:15.797Z\", \"conclusion\": \"negative\", \"metrics\": {\"sc_accuracy\": 0.5, \"debate_accuracy\": 0.27, \"delta\": -0.23, \"n_samples\": 200, \"fallbacks\": 16, \"wall_time_min\": 211.5}, \"hypothesis\": \"Multi-agent debate among Mistral-7B instances on LogiQA improves accuracy over self-consistency because inter-agent argumentation corrects reasoning errors that independent sampling cannot, yielding a positive delta on 200 problems.\"}, \"exp-083-icg-mistral-logiqa-seed123\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T21:11:59.619Z\", \"updated_at\": \"2026-05-19T22:22:34.341Z\", \"hypothesis\": \"ICG × Mistral-7B × LogiQA-200 seed=123 multi-seed replication。exp-079 (seed=42) Δ=-0.5pp (negative)。跨数据集 multi-seed 确认 ICG 方法在 LogiQA 上的 negative 结果稳定性。\", \"parent\": \"exp-079-icg-mistral-logiqa200\", \"conclusion\": \"negative\", \"metrics\": {\"n\": 200, \"sc_accuracy\": 0.365, \"icg_accuracy\": 0.33, \"delta_pp\": -3.5, \"sc_correct\": 73, \"icg_correct\": 66, \"both_correct\": 62, \"sc_only\": 11, \"icg_only\": 4, \"neither\": 123, \"mean_constraints_generated\": 31.4, \"mean_constraints_unique\": 27.9, \"mean_maxsat_satisfied\": 27.7, \"mean_maxsat_excluded\": 0.2, \"wall_time_s\": 3653.7, \"mean_wall_time_s\": 18.3}}, \"exp-074d-icg-mistral-folio-seed456\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T20:43:16.073Z\", \"updated_at\": \"2026-05-19T22:04:19.258Z\", \"hypothesis\": \"ICG × Mistral-7B × FOLIO-204 seed=456 第三组 seed replication。exp-074 (seed=42) Δ=-2.0pp, exp-074c (seed=123) 运行中。3-seed 数据确认 ICG 方法的 negative 结果跨 seed 稳定性，堵住 reviewer 单 seed 质疑。ICG 是三方法中 Δ 最接近零的，3-seed 数据最有论文价值。\", \"parent\": \"exp-074-icg-mistral-folio\", \"conclusion\": \"negative\", \"metrics\": {\"sc_accuracy\": 0.5588, \"icg_accuracy\": 0.549, \"delta\": -0.0098, \"n_samples\": 204, \"wall_time_min\": 57.3, \"three_seed_mean_sc\": 0.5572, \"three_seed_mean_icg\": 0.5523, \"three_seed_mean_delta\": -0.0049, \"three_seed_std_delta\": 0.0177, \"three_seed_details\": {\"seed_42\": {\"sc\": 0.5392, \"icg\": 0.5196, \"delta\": -0.0196}, \"seed_123\": {\"sc\": 0.5735, \"icg\": 0.5882, \"delta\": 0.0147}, \"seed_456\": {\"sc\": 0.5588, \"icg\": 0.549, \"delta\": -0.0098}}}}, \"exp-077-kappa-generalization\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T18:30:19.744Z\", \"updated_at\": \"2026-05-19T21:41:15.597Z\", \"hypothesis\": \"High Fleiss kappa (low independence) is a general property of same-model aggregation, not specific to SC+SICA. LLM-Debate and Diverse-Prompt aggregation on Mistral-7B will also exhibit high kappa and low Effective K, confirming the independence bottleneck is fundamental to single-model ensembles regardless of aggregation method.\", \"conclusion\": \"negative\", \"metrics\": {\"sc_kappa\": 0.4384, \"sc_eff_k\": 2.02, \"sc_nominal_k\": 10, \"debate_kappa\": 0.1549, \"debate_eff_k\": 4.44, \"debate_nominal_k\": 12, \"diverse_prompt_kappa\": 0.403, \"diverse_prompt_eff_k\": 2.21, \"diverse_prompt_nominal_k\": 12, \"n_samples\": 204}}, \"exp-077\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T21:36:46.336Z\", \"updated_at\": \"2026-05-19T21:37:22.166Z\", \"metrics\": {\"sc_kappa\": 0.4384, \"sc_eff_k\": 2.02, \"debate_kappa\": 0.1549, \"debate_eff_k\": 4.44, \"diverse_prompt_kappa\": 0.403, \"diverse_prompt_eff_k\": 2.21, \"n_questions\": 204, \"all_kappa_gt_04\": false, \"wall_time_min\": 184.9}, \"conclusion\": \"negative\", \"hypothesis\": \"All three LLM aggregation methods (Self-Consistency, LLM-Debate, Diverse-Prompt) suffer from the same independence bottleneck (Fleiss' κ > 0.4), because the shared model backbone forces correlated reasoning traces regardless of the aggregation strategy used.\"}, \"exp-075b\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T21:06:51.393Z\", \"updated_at\": \"2026-05-19T21:07:31.931Z\", \"conclusion\": \"negative\", \"metrics\": {\"sc_accuracy\": 0.5686, \"contrastive_accuracy\": 0.4755, \"delta\": -0.0931, \"n_samples\": 204, \"degenerate\": 41, \"wall_time_min\": 193.6}, \"hypothesis\": \"Contrastive pro/con argumentation with normalized scoring improves self-consistency accuracy on FOLIO logical reasoning over standard SC majority voting, by surfacing symbolic invariants through structured debate.\"}, \"exp-074c-icg-mistral-folio-seed123\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T20:06:50.097Z\", \"updated_at\": \"2026-05-19T21:06:21.214Z\", \"hypothesis\": \"ICG × Mistral-7B × FOLIO-204 seed=123 replication. exp-074 (seed=42) Δ=-2.0pp (negative). Multi-seed replication 确认 ICG 方法的 negative 结果是否跨 seed 稳定。如果 seed=123 也 negative，堵住 reviewer 单 seed 质疑。\", \"parent\": \"exp-074-icg-mistral-folio\", \"metrics\": {\"sc_accuracy\": 0.5735, \"icg_accuracy\": 0.5882, \"delta\": 0.0147, \"n_samples\": 204, \"wall_time_min\": 56.5}, \"conclusion\": \"negative\"}, \"exp-076-debate-mistral-folio\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T17:27:33.106Z\", \"updated_at\": \"2026-05-19T20:40:55.111Z\", \"hypothesis\": \"Debate-Augmented Extraction: 同模型 Proposer/Critic 对抗辩论生成多样化推理路径，从完整辩论记录提取 FOL 约束 + MAX-SAT 评分。在 Mistral-7B FOLIO-204 上测试。Dry-run 3 题 Debate 100% vs SC 67%。如果辩论打破 trace 同源性，delta(Debate vs SC) > delta(SICA vs SC)。parent=exp-033\", \"conclusion\": \"negative\", \"metrics\": {\"sc_accuracy\": 0.5686, \"debate_accuracy\": 0.3824, \"delta\": -0.1863, \"n_samples\": 204, \"wall_time_min\": 186.4, \"fallbacks\": 10, \"total_debate_constraints\": 3677}}, \"exp-079-icg-mistral-logiqa200\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T19:06:05.950Z\", \"updated_at\": \"2026-05-19T20:33:29.162Z\", \"hypothesis\": \"ICG × Mistral-7B × LogiQA-200 cross-dataset validation. 验证 ICG 方法在 LogiQA 多选题上是否有效。与 exp-074 (ICG×FOLIO) 和 exp-078 (Debate×LogiQA) 对比，构建方法×数据集交叉矩阵。如果 ICG 在 LogiQA 上也无效，进一步确认 independence bottleneck 的普遍性。\", \"parent\": \"exp-074-icg-mistral-folio\", \"conclusion\": \"negative\", \"metrics\": {\"sc_accuracy\": 0.475, \"icg_accuracy\": 0.47, \"delta\": -0.005, \"n_samples\": 200, \"wall_time_min\": 54.3}}, \"exp-072b-llama8b-logiqa200\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T17:46:38.067Z\", \"updated_at\": \"2026-05-19T20:02:06.149Z\", \"hypothesis\": \"LLaMA-3.1-8B-Instruct on LogiQA-200 with canonical SICA code (k=12, seed=42)（重跑）。exp-072 因 session crash 失败。产出 valid comparable SICA scores，replacing exp-069 which used outdated code.\", \"parent\": \"exp-072-llama8b-logiqa200\", \"conclusion\": \"negative\", \"metrics\": {\"sc_accuracy\": 0.595, \"sica_accuracy\": 0.585, \"delta\": -0.01, \"n_samples\": 200, \"k\": 12, \"wall_time_s\": 7310.5, \"extraction_success\": 2292, \"extraction_fail_json_parse\": 108}}, \"exp-074-icg-mistral-folio\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T17:06:33.965Z\", \"updated_at\": \"2026-05-19T19:42:58.267Z\", \"hypothesis\": \"ICG (Independent Constraint Generation): 独立于 reasoning traces 生成 FOL 约束，绕过 trace-sourced confirmation bias。直接从问题 premises 提取逻辑约束（不解题），用独立约束 + MAX-SAT 评分候选答案。在 Mistral-7B FOLIO-204 上测试，与标准 SICA (同源约束) 对比。预期：如果独立约束有效，delta(ICG vs SC) > delta(SICA vs SC)。\", \"metrics\": {\"sc_accuracy\": 0.5392, \"icg_accuracy\": 0.5196, \"delta\": -0.0196, \"n_samples\": 204, \"k\": 12, \"k_icg\": 10, \"wall_time_s\": 3368}, \"conclusion\": \"negative\"}, \"exp-073b-qwen7b-logiqa200-seed456\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T17:46:28.317Z\", \"updated_at\": \"2026-05-19T19:42:57.308Z\", \"hypothesis\": \"Qwen2.5-7B LogiQA seed=456 第三组 seed replication（重跑）。exp-073 因 session crash 失败。exp-070 (seed=42) SC=68.5% Δ=+2.5pp, exp-071 (seed=123) SC=69% Δ=-0.5pp。seed=456 是 Goldilocks tie-breaker。\", \"parent\": \"exp-070-qwen7b-logiqa200\", \"metrics\": {\"sc_accuracy\": 0.695, \"sica_accuracy\": 0.715, \"delta\": 0.02, \"n_samples\": 200, \"k\": 12, \"wall_time_s\": 3517.3}, \"conclusion\": \"success\"}, \"exp-073-qwen7b-logiqa200-seed456\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T15:21:57.207Z\", \"updated_at\": \"2026-05-19T18:55:51.568Z\", \"hypothesis\": \"Qwen2.5-7B LogiQA seed=456 第三组 seed replication。exp-070 (seed=42) SC=68.5% Δ=+2.5pp, exp-071 (seed=123) 进行中。seed=456 加固第二个 Goldilocks 数据点。如果 3 seeds 方向一致，累积证据支持 Qwen2.5-7B 在 LogiQA 上处于 Goldilocks regime。\", \"parent\": \"exp-070-qwen7b-logiqa200\", \"conclusion\": \"success\", \"metrics\": {\"sc_accuracy\": 0.7, \"sica_accuracy\": 0.705, \"delta\": 0.005, \"n_samples\": 200}}, \"exp-072-llama8b-logiqa200\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T15:21:53.401Z\", \"updated_at\": \"2026-05-19T18:55:50.780Z\", \"hypothesis\": \"LLaMA-3.1-8B-Instruct on LogiQA-200 with canonical SICA code (k=12, seed=42) will produce valid comparable SICA scores, replacing exp-069 which used outdated code.\", \"parent\": \"\", \"conclusion\": \"success\", \"metrics\": {\"sc_accuracy\": 0.62, \"sica_accuracy\": 0.63, \"delta\": 0.01, \"n_samples\": 200}}, \"exp-064-deepseek-r1-qwen3-8b-folio204\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T07:49:07.235Z\", \"updated_at\": \"2026-05-19T18:14:25.428Z\", \"hypothesis\": \"DeepSeek-R1-0528-Qwen3-8B (reasoning distill) 在 FOLIO-204 上 SICA vs SC。测试 reasoning 模型在 8B scale 是否出现 degenerate regime (C₀<5%) 或因 8B 能力较弱落入 error amplification / Goldilocks zone。\", \"parent\": \"exp-033\", \"conclusion\": \"success\", \"notes\": \"code_version=westd-16639-legacy, sica_not_comparable. 旧代码启动，SC 数据可用（不受代码版本影响），SICA/delta 不入 Table 1。Director 指令 2026-05-19T15:25 UTC。\", \"metrics\": {\"sc_accuracy\": 0.8382, \"sica_accuracy\": 0.8382, \"delta\": 0, \"n_samples\": 204, \"extraction_rate\": 0.3818, \"contradiction_rate\": 0.0165, \"wall_time_min\": 355.6}}, \"exp-075-contrastive-mistral-folio\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T17:27:29.909Z\", \"updated_at\": \"2026-05-19T17:40:54.883Z\", \"hypothesis\": \"Contrastive Constraint Generation: 对每个候选答案生成 pro/con FOL 约束，用对比评分代替同源约束。在 Mistral-7B FOLIO-204 上测试。如果 contrastive 约束提供独立于 traces 的判别信号，delta(Contrastive vs SC) > delta(SICA vs SC)。parent=exp-033\", \"conclusion\": \"failed\"}, \"exp-077-generalization-kappa\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-19T17:28:58.631Z\", \"updated_at\": \"2026-05-19T17:28:58.631Z\", \"hypothesis\": \"Generalization: independence bottleneck (high κ) applies to Debate and Diverse-Prompt aggregation, not just SC+SICA. 在 Mistral-7B FOLIO-204 上测量 3 种聚合方式的 Fleiss' κ + Eff-K: (a) Standard SC (复用 exp-033 traces), (b) LLM-Debate traces (4组×3轮=12 answer points), (c) Diverse-Prompt traces (4种 prompt×3次=12). 如果三种方式 κ 均 > 0.4，证明 independence bottleneck 是 same-model aggregation 的通病。\"}, \"exp-071-qwen7b-logiqa200-seed123\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T14:36:32.407Z\", \"updated_at\": \"2026-05-19T16:21:44.107Z\", \"hypothesis\": \"exp-070 seed replication: Qwen2.5-7B-Instruct 在 LogiQA-200 上 SICA vs SC, seed=123。exp-070 (seed=42) SC=68.5% Δ=+2.5pp p=0.125, 7 个 discordant pairs 统计功效不足。seed replication 加固 Goldilocks zone claim。如果 seed=123 也给出正向 Δ 且方向一致，则累积证据支持 Qwen2.5-7B 在 LogiQA 上处于 Goldilocks regime。\", \"parent\": \"exp-070-qwen7b-logiqa200\", \"conclusion\": \"negative\", \"metrics\": {\"sc_accuracy\": 0.69, \"sica_accuracy\": 0.685, \"delta\": -0.005, \"n_samples\": 200}}, \"exp-048-llama8b-pw600\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T20:30:33.025Z\", \"updated_at\": \"2026-05-19T15:41:14.159Z\", \"hypothesis\": \"LLaMA-3.1-8B-Instruct 在 ProofWriter-600 上 SICA vs SC。FOLIO-204 上 LLaMA-8B SC=63.2% delta=-2.45pp (exp-020)。PW 是更结构化的形式推理数据集，测试 SICA 在 PW 上对低能力模型是否有效（补充 regime boundary 跨域证据）。parent=exp-020\", \"conclusion\": \"negative\", \"notes\": \"code_version=westd-16639-legacy, sica_not_comparable. Reviewer verified: SC=70%, SICA=64.8%, delta=-5.2pp, n=600.\", \"metrics\": {\"sc_accuracy\": 0.7, \"sica_accuracy\": 0.648, \"delta\": -0.052, \"n_samples\": 600}}, \"exp-053-mistral-folio204-seed456\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T23:17:36.430Z\", \"updated_at\": \"2026-05-19T15:21:07.978Z\", \"hypothesis\": \"exp-033 replication (seed=456): Mistral-7B FOLIO-204 K=12 T=0.7，第二组独立 replication。与 exp-052 (seed=123) 一起验证 exp-033 结论 robustness。parent=exp-033\", \"conclusion\": \"killed\", \"notes\": \"Stale duplicate. 实际实验已在 exp-053 (短 ID) 下完成 (DONE)。本条目是重复创建的长名称版本，清理。\"}, \"exp-052-mistral-folio204-seed123\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T23:17:34.705Z\", \"updated_at\": \"2026-05-19T15:21:07.037Z\", \"hypothesis\": \"exp-033 replication (seed=123): Mistral-7B FOLIO-204 K=12 T=0.7，与 exp-033 (seed=42, delta=+4.90pp, p=0.013) 完全相同配置，仅 seed 不同。验证正向结果是否 seed-robust。parent=exp-033\", \"conclusion\": \"killed\", \"notes\": \"Stale duplicate. 实际实验已在 exp-052 (短 ID) 下完成 (DONE)。本条目是重复创建的长名称版本，清理。\"}, \"exp-069-llama8b-logiqa200\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T11:40:15.817Z\", \"updated_at\": \"2026-05-19T15:15:54.692Z\", \"hypothesis\": \"LLaMA-3.1-8B-Instruct 在 LogiQA-200 上 SICA vs SC。FOLIO-204 上 LLaMA-8B SC=66.18% delta=-4.41pp (exp-063, negative/error amplification)。LogiQA 上 Mistral-7B SC=51% delta=+0.5pp (exp-049b)，Qwen2.5-14B SC=78.5% delta=-0.50pp (exp-038)。测试 LLaMA-8B 在 LogiQA 上的 regime（SC 预计 50-60%，可能在 error amplification zone）。parent=exp-063-llama8b-folio204-16639\", \"parent\": \"exp-063-llama8b-folio204-16639\", \"notes\": \"code_version=westd-16639-legacy. Reviewer verified: SC=61%, SICA=58.5%, delta=-2.5pp, n=200.\", \"conclusion\": \"negative\", \"metrics\": {\"sc_accuracy\": 0.61, \"sica_accuracy\": 0.585, \"delta\": -0.025, \"n_samples\": 200}}, \"exp-065-qwen7b-pw600\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T08:49:16.855Z\", \"updated_at\": \"2026-05-19T15:15:51.839Z\", \"hypothesis\": \"Qwen2.5-7B 在 PW-D5-600 上 SICA vs SC。FOLIO SC=75.98% (confirmation bias)，PW 更难 SC 预计更低，测试不同 regime。parent=exp-061\", \"parent\": \"\", \"conclusion\": \"negative\", \"metrics\": {\"sc_accuracy\": 0.72, \"sica_accuracy\": 0.68, \"delta\": -0.04, \"n_samples\": 600}}, \"exp-062-gemma27b-folio204\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T07:41:54.628Z\", \"updated_at\": \"2026-05-19T15:15:50.853Z\", \"hypothesis\": \"Gemma-3-27B-IT (Google 架构) FOLIO-204 SICA vs SC。跨模型家族验证 regime-dependent pattern。27B 能力预计在 Qwen2.5-14B (~75% SC) 和 Qwen3-14B (~85% SC) 之间。\", \"conclusion\": \"negative\", \"metrics\": {\"sc_accuracy\": 0.809, \"sica_accuracy\": 0.804, \"delta\": -0.005, \"n_samples\": 204}}, \"exp-069-mistral-logiqa200\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T11:50:28.223Z\", \"updated_at\": \"2026-05-19T14:19:37.076Z\", \"hypothesis\": \"Mistral-7B-Instruct-v0.3 在 LogiQA-200 上 SICA vs SC。FOLIO-204 上 Mistral 是唯一 Goldilocks 候选 (SC≈55%, Δ=+4.90pp seed=42)。如果 LogiQA SC 也在 55-65% 且 Δ>0，则跨数据集验证 Goldilocks zone 存在。parent=exp-033\", \"parent\": \"exp-033\", \"conclusion\": \"negative\", \"metrics\": {\"sc_accuracy\": 0.495, \"sica_accuracy\": 0.465, \"delta\": -0.03, \"n_samples\": 200}, \"notes\": \"与 exp-049b 结果不一致调查：5/7 SICA 核心模块代码版本不同（md5 全部不匹配）。关键差异：scorer.py tie-breaking（049b: max() 随机 vs 069: sorted() 字母序）、constraint_extractor/z3_maxsat/pipeline 均有变化。049b 还设了 VLLM_USE_FLASHINFER_SAMPLER=0。prompt 模板相同。两组数据不可直接比较。exp-069 使用 westd-25068 上的最新代码版本。\"}, \"exp-070-qwen7b-logiqa200\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T11:40:18.453Z\", \"updated_at\": \"2026-05-19T14:18:52.579Z\", \"hypothesis\": \"Qwen2.5-7B-Instruct 在 LogiQA-200 上 SICA vs SC。FOLIO 上 SC=75.98% (Type A confirmation bias, Δ=+0.49pp)。LogiQA 可能更难，SC 可能降到 55-65% 进入 Goldilocks zone，或保持 >75% 继续 Type A。验证 regime 跨数据集一致性。parent=exp-061\", \"parent\": \"exp-061\", \"conclusion\": \"success\", \"metrics\": {\"sc_accuracy\": 0.685, \"sica_accuracy\": 0.71, \"delta\": 0.025, \"n_samples\": 200, \"sc_correct\": 137, \"sica_correct\": 142, \"discordant_b\": 1, \"discordant_c\": 6, \"mcnemar_chi2\": 2.2857, \"mcnemar_p\": 0.131, \"mcnemar_p_exact\": 0.125, \"significant_005\": false, \"cohens_kappa\": 0.917, \"kappa_interpretation\": \"almost_perfect\"}, \"notes\": \"Reviewer 独立验证（从 exp070_results.json 确认）：SC=137/200=68.5%, SICA=142/200=71.0%, Δ=+2.5pp。原 diagnostic worker 读取了错误数据源，误报 SC=SICA=79.5%（差距 11pp/22题）。已由 Director 指令修正。\"}, \"exp-068-qwen3-logiqa200\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T11:13:19.371Z\", \"updated_at\": \"2026-05-19T13:53:10.914Z\", \"hypothesis\": \"Qwen3-14B non-thinking 在 LogiQA-200 上 SICA vs SC。FOLIO SC=84.80%, PW SC=85.0%，LogiQA 预计也在 confirmation bias zone。验证跨数据集 Type A 一致性。parent=exp-040\", \"parent\": \"exp-040\", \"notes\": \"Reviewer 独立验证：输出文件完整，200/200 样本已处理。SC=SICA=0.81，null effect。原被 CRON 错误标记为 failed（无 W&B 数据时默认标 failed）。\", \"conclusion\": \"negative\", \"metrics\": {\"sc_accuracy\": 0.81, \"sica_accuracy\": 0.81, \"delta\": 0, \"n_samples\": 200}}, \"exp-064\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T08:56:53.587Z\", \"updated_at\": \"2026-05-19T12:13:57.742Z\", \"conclusion\": \"killed\"}, \"exp-067-mistral-folio-seed789\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T09:14:16.096Z\", \"updated_at\": \"2026-05-19T12:10:24.878Z\", \"hypothesis\": \"Mistral-7B FOLIO seed=789 第4 seed replication。已有 s42 +3.43pp, s123 +2.94pp, s456 0.00pp。增加统计样本验证 seed variance 和 SC-Δ 相关性。parent=exp-033\", \"parent\": \"exp-033\", \"conclusion\": \"success\", \"metrics\": {\"sc_accuracy\": 0.5441, \"sica_accuracy\": 0.5392, \"delta_pp\": -0.49, \"n\": 204, \"mcnemar_b\": 6, \"mcnemar_c\": 5, \"mcnemar_p\": 1, \"mcnemar_significant\": false, \"fleiss_kappa_raw\": 0.4124, \"eff_k\": 2.17}}, \"exp-063-llama8b-folio204-16639\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T07:40:38.262Z\", \"updated_at\": \"2026-05-19T12:02:49.523Z\", \"hypothesis\": \"LLaMA-3.1-8B-Instruct 在 FOLIO-204 上 SICA vs SC。此前 exp-020 在不同服务器上跑过 (SC=63.2%, delta=-2.45pp)，本实验在 westd-16639 复现并用修正后的 alphabetical tie-breaking SC。parent=exp-020\", \"parent\": \"exp-020\", \"conclusion\": \"negative\", \"metrics\": {\"sc_accuracy\": 0.6618, \"sica_accuracy\": 0.6176, \"delta_pp\": -4.41, \"n\": 204, \"mcnemar_b\": 16, \"mcnemar_c\": 7, \"mcnemar_p\": 0.0931, \"mcnemar_significant\": false}}, \"exp-063-llama8b-folio204\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-19T11:34:18.492Z\", \"updated_at\": \"2026-05-19T11:34:19.817Z\", \"conclusion\": \"negative\", \"metrics\": {\"n\": 204, \"sc_accuracy\": 0.6618, \"sica_accuracy\": 0.6176, \"delta_pp\": -4.41}}, \"exp-061-qwen7b-folio204\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T07:18:30.356Z\", \"updated_at\": \"2026-05-19T11:34:17.303Z\", \"hypothesis\": \"Qwen2.5-7B-Instruct 在 FOLIO-204 上 SICA vs SC。SC 预计 55-65%（介于 Mistral-7B ~55% 和 Qwen2.5-14B ~75% 之间），可能在 Goldilocks zone。\", \"parent\": \"exp-033\", \"conclusion\": \"negative\", \"metrics\": {\"n\": 204, \"sc_accuracy\": 0.7598, \"sica_accuracy\": 0.7647, \"delta_pp\": 0.49}}, \"exp-059-cross-qwen3-extractor\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T06:45:04.278Z\", \"updated_at\": \"2026-05-19T11:34:15.561Z\", \"hypothesis\": \"Qwen3-14B cross-model extraction should produce higher quality FOL constraints than Mistral-7B self-extraction (breaking confirmation bias), leading to higher SICA discriminative rate and accuracy delta over SC baseline.\", \"parent\": \"exp-033\", \"conclusion\": \"success\", \"metrics\": {\"n\": 204, \"cross_sica_accuracy\": 0.6029, \"orig_sica_accuracy\": 0.5931, \"sc_accuracy\": 0.5588, \"delta_cross_vs_sc_pp\": 4.41, \"delta_cross_vs_orig_pp\": 0.98}}, \"exp-063\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T07:40:39.276Z\", \"updated_at\": \"2026-05-19T11:20:57.939Z\", \"hypothesis\": \"LLaMA-3.1-8B-Instruct FOLIO-204 SICA vs SC（Meta 架构覆盖）。exp-020 旧数据 SC=63.2% delta=-2.45pp，本实验用修正 tie-breaking 重跑。parent=exp-020\", \"parent\": \"exp-020\", \"conclusion\": \"negative\", \"metrics\": {\"n\": 204, \"sc_accuracy\": 0.6618, \"sica_accuracy\": 0.6176, \"delta_pp\": -4.41}}, \"exp-040-qwen3-pw600-16639\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T18:01:31.954Z\", \"updated_at\": \"2026-05-19T11:03:11.142Z\", \"hypothesis\": \"Qwen3-14B non-thinking 在 ProofWriter-600 全量上 SICA vs SC：跨模型代际验证 capability trap 在 PW 数据集上是否持续。与 exp-039 (Qwen2.5-14B PW-600) 对比代际差异。\", \"notes\": \"westd-16639 实际目录: exp033_qwen3_14b_pw600_nonthinking, tmux: exp033, port: 8001, GPU 1. 162/600 (27.0%) at 22:28 UTC. Qwen3-14B thinking=false, 推理速度约为 Qwen2.5-14B 的一半。\", \"conclusion\": \"negative\", \"metrics\": {\"n\": 600, \"sc_accuracy\": 0.85, \"sica_accuracy\": 0.8567, \"delta_pp\": 0.67, \"extraction_rate\": 0.997, \"contradiction_rate\": 0.004, \"wall_time_min\": 1032.2, \"failure_type\": \"Type A (confirmation bias)\"}}, \"exp-060-cross-qwen25-14b-extractor\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T06:38:50.075Z\", \"updated_at\": \"2026-05-19T08:33:33.071Z\", \"hypothesis\": \"Qwen2.5-14B 跨模型提取 FOL 约束。与 exp-033 (Mistral self-extraction) 和 exp-059 (Qwen3 cross-extraction) 对比。parent=exp-033\", \"conclusion\": \"negative\", \"metrics\": {\"n\": 204, \"cross_sica_accuracy\": 0.5833, \"orig_sica_accuracy\": 0.5931, \"sc_accuracy\": 0.5588, \"delta_cross_vs_sc_pp\": 2.45, \"delta_cross_vs_orig_pp\": -0.98, \"divergence_rate\": 0.059, \"wall_time_min\": 106.1}}, \"exp-057-mistral-folio204-t03\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T02:49:57.330Z\", \"updated_at\": \"2026-05-19T07:37:40.489Z\", \"hypothesis\": \"T=0.3 低温 traces 更确定性更一致，SICA delta < T=0.7 的 +4.90pp。与 exp-054 (T=1.0, +0.49pp) 共同形成 T sensitivity ablation curve。parent=exp-033, D060 analysis paper\", \"parent\": \"exp-033\", \"conclusion\": \"negative\", \"metrics\": {\"n\": 204, \"sc_accuracy\": 0.5833, \"sica_accuracy\": 0.5686, \"delta_pp\": -1.47, \"mcnemar_p\": 0.5488}}, \"exp-034\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T16:15:24.666Z\", \"updated_at\": \"2026-05-19T05:50:00.000Z\", \"hypothesis\": \"Qwen2.5-14B-Instruct 在 ProofWriter-600 上 SICA vs SC（westd-25068 重跑）：在 full 600 题上验证 capability trap，复现 sica_expanded_14b 的 PW 子集结果（delta=+0.3pp）。代替原 StrategyQA 实验（exp-034 v1 因 extraction prompt bug + 平台 kill 失败）。\", \"conclusion\": \"negative\", \"metrics\": {\"n_problems\": 93, \"n_target\": 600, \"completion_pct\": 15.5, \"sica_accuracy\": 77.42, \"sc_accuracy\": 74.19, \"delta_pp\": 3.23, \"sica_correct\": 72, \"sc_correct\": 69, \"mcnemar_discordant_b\": 6, \"mcnemar_discordant_c\": 3, \"mcnemar_p_value\": 0.5078, \"c0_non_unanimous_rate\": 0.581, \"avg_majority_frac\": 0.8324, \"extraction_rate\": 99.19, \"contradiction_rate\": 11.83, \"problems_with_contradictions\": 11, \"avg_unique_constraints\": 35.6, \"total_constraints\": 14437, \"unique_constraints\": 3308, \"dedup_ratio\": 22.9, \"k\": 12, \"level\": \"OWA-D5\", \"gt_distribution\": {\"True\": 32, \"False\": 28, \"Unknown\": 33}, \"wall_time_s\": 6086.4, \"status_note\": \"INCOMPLETE: crashed at 93/600 (python not found after conda env lost)\"}, \"notes\": \"v4 完成。tmux=exp034_run, westd-25068 cuda:1。Qwen2.5-14B on PW-600, delta=+0.50pp (不显著)。\"}, \"exp-039-14b-pw600-16639\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T18:01:31.038Z\", \"updated_at\": \"2026-05-19T04:53:50.957Z\", \"hypothesis\": \"Qwen2.5-14B-Instruct 在 ProofWriter-600 全量上 SICA vs SC（westd-16639 重跑）：验证 capability trap 在 PW 数据集全量规模上是否持续。复现 sica_expanded_14b 的 PW 子集结果（delta=+0.3pp）。\", \"notes\": \"westd-16639 实际目录: exp032_qwen25_14b_pw600, tmux: exp032, port: 8000, GPU 0. 263/600 (43.8%) at 22:28 UTC.\", \"conclusion\": \"negative\", \"metrics\": {\"sica_accuracy\": 71.5, \"sc_accuracy\": 73.5, \"delta_pp\": -2.0, \"n_problems\": 600, \"extraction_rate\": 99.2, \"wall_time_min\": 659.6}}, \"exp-058-mistral-folio204-t05\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T03:10:13.574Z\", \"updated_at\": \"2026-05-19T04:38:50.593Z\", \"hypothesis\": \"T=0.5 delta 介于 T=0.3 和 T=0.7 之间，形成温度-SICA delta 曲线。与 exp-033 (T=0.7, +4.90pp) 和 exp-054 (T=1.0, +0.49pp) 共同构成 4 点 T sensitivity ablation。parent=exp-033, D060 analysis paper\", \"parent\": \"exp-033\", \"conclusion\": \"negative\", \"metrics\": {\"sc_accuracy\": 57.84, \"sica_accuracy\": 57.35, \"delta_pp\": -0.49, \"mcnemar_p\": 1, \"discordant_b\": 3, \"discordant_c\": 2, \"n_problems\": 204, \"n_completed\": 204, \"extraction_rate\": 97, \"wall_time_min\": 80}}, \"exp-051-mistral-k-sensitivity\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T22:32:12.672Z\", \"updated_at\": \"2026-05-19T04:37:35.722Z\", \"hypothesis\": \"Mistral-7B K sensitivity on FOLIO-204: K=[4,8,16,20]（K=12 已有 exp-033 delta=+4.90pp）。验证正向结果对 K 选择是否稳健。Reviewer 必问 ablation。parent=exp-033\", \"metrics\": {\"K4\": {\"SC\": 54.41, \"SICA\": 52.94, \"delta\": -1.47, \"b\": 7, \"c\": 10, \"McNemar_p\": 0.6291}, \"K8\": {\"SC\": 57.35, \"SICA\": 56.37, \"delta\": -0.98, \"b\": 4, \"c\": 6, \"McNemar_p\": 0.7539}, \"K12_exp033\": {\"SC\": 54.41, \"SICA\": 59.31, \"delta\": 4.9, \"b\": 12, \"c\": 2, \"McNemar_p\": 0.0129}, \"K16\": {\"SC\": 55.88, \"SICA\": 57.35, \"delta\": 1.47, \"b\": 10, \"c\": 7, \"McNemar_p\": 0.6291}, \"K20\": {\"SC\": 57.35, \"SICA\": 59.31, \"delta\": 1.96, \"b\": 5, \"c\": 1, \"McNemar_p\": 0.2188}}, \"conclusion\": \"success\", \"notes\": \"K sensitivity 完整 5 点数据确认 K=12 是最优点（delta=+4.90pp, p=0.013）。K<12 SICA 不如 SC（K=4: -1.47pp, K=8: -0.98pp），K>12 delta 回落但仍为正（K=16: +1.47pp, K=20: +1.96pp）。整体呈 peaked 曲线（非严格倒 U，K=20 略高于 K=16），但 K=12 peak 显著且两侧衰减明确。McNemar 仅 K=12 显著（p=0.013），其余 K 值均不显著。\"}, \"exp-055-multitemp-mistral-folio\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T02:17:09.293Z\", \"updated_at\": \"2026-05-19T03:53:56.005Z\", \"hypothesis\": \"Multi-temperature sampling 通过强制 trace diversity 提升 Effective-K，预期 SICA delta > exp-033 的 +4.9pp。混合 T=0.3/0.7/1.2 各 4 traces 比单一 T=0.7 的 12 traces 产生更多独立视角，从而让 MAX-SAT 有更多 discriminative 信号。parent=exp-033, D059\", \"parent\": \"exp-033\", \"conclusion\": \"negative\", \"metrics\": {\"n\": 204, \"sc_accuracy\": 57.84, \"sica_accuracy\": 57.84, \"delta_pp\": 0, \"discordant_b\": 5, \"discordant_c\": 5, \"mcnemar_p\": 1, \"significant\": false, \"agreement_rate\": 0.951, \"wall_time_min\": 83.2, \"temperatures\": \"0.3,0.7,1.2\", \"k_per_temp\": \"4,4,4\"}}, \"exp-028b-qwen3-thinking-folio204\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T20:30:30.635Z\", \"updated_at\": \"2026-05-19T03:34:08.736Z\", \"hypothesis\": \"Qwen3-14B thinking mode (enable_thinking=True, 32K context) 在 FOLIO-204 上 SICA vs SC。D028 pilot (35/204, delta=+2.86pp) 被 kill。thinking mode 产生更 diverse+higher-quality reasoning traces，如果同时提升 trace quality 和 diversity，可能打破 14B 级别的 capability trap。parent=exp-028\", \"conclusion\": \"killed\", \"notes\": \"失败根因：exp-058 部署到 cuda:3+port:8003 覆盖了 exp-028b 的 vLLM（非 OOM）。166/204 已完成，intermediates 完整保存。支持 resume（仅需 38 题 ~90min），但需等 exp-058 完成释放 cuda:3。\"}, \"exp-052\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T23:20:17.415Z\", \"updated_at\": \"2026-05-19T02:47:07.125Z\", \"hypothesis\": \"Seed replication of exp-033: the +4.90pp improvement on FOLIO-204 with Mistral-7B using symbolic invariant consensus (K=12) is reproducible across different random seeds, confirming the result is not a statistical fluke.\", \"metrics\": {\"n\": 204, \"sc_accuracy\": 53.9, \"sica_accuracy\": 57.4, \"sc_correct\": 110, \"sica_correct\": 117, \"delta_pp\": 3.43, \"discordant_b\": 8, \"discordant_c\": 1, \"extraction_rate\": 0.971, \"contradiction_rate\": 0.034, \"wall_time_min\": 81.9, \"mcnemar_p\": 0.0391, \"significant\": true}, \"conclusion\": \"success\", \"notes\": \"Seed=123: SICA=57.35% vs SC=53.92%, delta=+3.43pp, b=8, c=1, p=0.039. High entropy 区域 delta=+7.14pp。2/3 seeds 显著。\", \"parent\": \"exp-033\"}, \"exp-054-mistral-folio204-t10\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T01:17:52.972Z\", \"updated_at\": \"2026-05-19T02:44:50.785Z\", \"hypothesis\": \"T=1.0 增大 trace diversity，Adaptive SICA（high entropy 子集）delta 应 ≥ T=0.7 的 +4.9pp。更高温度 → 更多 high-entropy 问题 → SICA 在更大子集上有效 → overall delta 可能更大。同时测试 exp-033 (+4.9pp at T=0.7) 对温度的敏感性。parent=exp-033\", \"parent\": \"exp-033\", \"conclusion\": \"negative\", \"metrics\": {\"n\": 204, \"sc_accuracy\": 54.9, \"sica_accuracy\": 55.4, \"delta_pp\": 0.49, \"discordant_b\": 5, \"discordant_c\": 4, \"mcnemar_chi2\": 0.1111, \"mcnemar_p\": 0.7389, \"extraction_rate\": 97.3, \"contradiction_rate\": 3, \"wall_time_min\": 83}}, \"exp-046-mistral-pw600\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T20:16:46.346Z\", \"updated_at\": \"2026-05-19T01:15:51.422Z\", \"hypothesis\": \"Mistral-7B-Instruct-v0.3 在 ProofWriter-600 上 SICA vs SC：验证 regime boundary 跨域泛化。exp-033 (Mistral FOLIO-204) 显示 +4.90pp (p=0.013)，如果 PW-600 也显示正向 delta，则 regime-dependent capability trap 不是 FOLIO-specific artifact。\", \"conclusion\": \"negative\", \"metrics\": {\"n\": 600, \"sc_accuracy\": 39.33, \"sica_accuracy\": 36.5, \"delta_pp\": -2.83, \"sc_wins\": 30, \"sica_wins\": 13, \"mcnemar_p\": 0.0095, \"significant\": true, \"dataset\": \"ProofWriter-D5-600\", \"model\": \"Mistral-7B-Instruct-v0.3\"}}, \"exp-053\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T23:20:18.405Z\", \"updated_at\": \"2026-05-19T01:05:00.000Z\", \"hypothesis\": \"Seed replication of exp-033: the +4.90pp improvement on FOLIO-204 with Mistral-7B using symbolic invariant consensus (K=12) is reproducible across different random seeds, confirming the result is not a statistical fluke.\", \"metrics\": {\"n\": 204, \"sc_accuracy\": 56.37, \"sica_accuracy\": 55.88, \"sc_correct\": 115, \"sica_correct\": 114, \"delta_pp\": -0.49, \"discordant_b\": 2, \"discordant_c\": 3, \"extraction_rate\": 0.97, \"contradiction_rate\": 0.033, \"wall_time_min\": 80.8, \"mcnemar_p\": 1.0, \"significant\": false}, \"conclusion\": \"negative\", \"notes\": \"Seed=456: SICA=55.88% vs SC=56.37%, delta=-0.49pp, b=2, c=3, p=1.0. SC baseline 最高，capability trap 确认。跨 seed SC vs delta Pearson r=-0.8973。\", \"parent\": \"exp-033\"}, \"exp-050b-mistral-icl-oracle\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T21:31:50.554Z\", \"updated_at\": \"2026-05-18T23:19:54.810Z\", \"hypothesis\": \"Increasing vLLM max_model_len from 8192 to 16384 will resolve the context length overflow (input ~4400 + max_tokens 4096 > 8192) that caused 86% failure in exp-050, allowing Mistral-7B ICL Oracle with 5 gold FOL examples to complete evaluation on all 199 FOLIO problems.\", \"metrics\": {\"n\": 199, \"sc_accuracy\": 57.79, \"sica_accuracy\": 54.27, \"delta_pp\": -3.52, \"sc_correct\": 115, \"sica_correct\": 108, \"discordant_b\": 6, \"discordant_c\": 13, \"mcnemar_p\": 0.167, \"significant\": false, \"wall_time_min\": 93.8, \"extraction_success\": 2333, \"extraction_fail\": 55, \"per_answer\": {\"True\": {\"n\": 70, \"sica_acc\": 50, \"sc_acc\": 54.29}, \"False\": {\"n\": 61, \"sica_acc\": 36.07, \"sc_acc\": 44.26}, \"Unknown\": {\"n\": 68, \"sica_acc\": 75, \"sc_acc\": 73.53}}}, \"conclusion\": \"negative\", \"notes\": \"ICL Oracle (5 gold FOL examples) on Mistral-7B FOLIO-199: SICA=54.27% vs SC=57.79%, delta=-3.52pp (p=0.167, ns). ICL boosted SC from vanilla 54.41% (exp-033) to 57.79% (+3.38pp), but SICA did not benefit. ICL improves individual trace quality enough to boost majority vote, but the resulting constraints become less diverse/discriminative for MaxSAT weighting. Confirms capability trap: better extraction quality does not translate to SICA gains when it also reduces beneficial disagreement.\"}, \"exp-050-mistral-icl-oracle-folio199\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T20:48:25.841Z\", \"updated_at\": \"2026-05-18T23:19:53.802Z\", \"hypothesis\": \"Providing 5 gold FOL annotations as in-context learning examples will significantly improve the quality of symbolic constraint extraction from Mistral-7B reasoning traces, leading to higher SICA accuracy over SC baseline on FOLIO-199\", \"conclusion\": \"failed\"}, \"exp-049b-mistral-logiqa200\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T21:53:09.676Z\", \"updated_at\": \"2026-05-18T23:16:15.080Z\", \"hypothesis\": \"Mistral-7B LogiQA-200 v2: 修复 exp-049 部署失败（vLLM 启动但 pipeline 未运行，tmux session 丢失）。验证 Mistral 的 +4.90pp FOLIO 增益是否跨 LogiQA 复现。parent=exp-033\", \"metrics\": {\"n\": 200, \"sc_accuracy\": 51, \"sica_accuracy\": 51.5, \"delta_pp\": 0.5, \"sc_correct\": 102, \"sica_correct\": 103, \"discordant_b\": 6, \"discordant_c\": 5, \"mcnemar_p\": 1, \"significant\": false, \"wall_time_min\": 78.6, \"extraction_rate\": 0.9725, \"total_constraints\": 10659, \"unique_constraints\": 8934, \"contradiction_rate\": 0.0196}, \"conclusion\": \"negative\", \"notes\": \"Mistral-7B LogiQA-200: SICA=51.50% vs SC=51.00%, delta=+0.50pp (p=1.000, ns). Mistral's +4.90pp FOLIO advantage (exp-033) does not transfer to LogiQA. SC baseline 51% is near random for 4-choice MCQ. Consistent with exp-038 (14B LogiQA delta=-0.50pp): SICA provides no benefit on LogiQA regardless of model, likely because LogiQA's pragmatic reasoning resists symbolic constraint formalization.\"}, \"exp-044b-icl-oracle\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T20:16:44.204Z\", \"updated_at\": \"2026-05-18T22:59:34.846Z\", \"hypothesis\": \"ICL with Oracle Examples (v2, 正确模型 Qwen2.5-14B): 用 5 个 gold FOL annotations 作为 few-shot examples 教 LLM 提取高质量约束。如果 extraction quality 是 capability trap 瓶颈，oracle-guided extraction 应能产生更 discriminative 的约束，使 ICL-SICA > vanilla SICA (74.51%)。评测 199 题。v1 因使用错误模型 (Mistral-7B) 被 kill。\", \"metrics\": {\"n\": 199, \"dataset\": \"FOLIO-199\", \"model\": \"Qwen2.5-14B-Instruct\", \"k\": 12, \"sica_accuracy\": 74.87, \"sc_accuracy\": 74.37, \"delta_pp\": 0.5, \"sica_correct\": 149, \"sc_correct\": 148, \"icl_examples\": 5, \"extraction_failure_rate\": 0.008}, \"conclusion\": \"negative\"}, \"exp-049-mistral-logiqa200\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T20:30:34.577Z\", \"updated_at\": \"2026-05-18T21:53:04.043Z\", \"hypothesis\": \"Mistral-7B-Instruct-v0.3 在 LogiQA-200 上 SICA vs SC。FOLIO-204 上 Mistral delta=+4.90pp (exp-033, p=0.013)。14B 在 LogiQA 上 delta=-0.50pp (exp-038)。测试 regime boundary：Mistral 低 SC + 高 diversity 是否在 LogiQA 上也产生正向 SICA delta。parent=exp-033\", \"conclusion\": \"failed\"}, \"exp-041-14b-folio204-16639\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T18:01:33.016Z\", \"updated_at\": \"2026-05-18T21:08:19.597Z\", \"hypothesis\": \"Qwen2.5-14B-Instruct 在 FOLIO-204 上 SICA vs SC（westd-16639 独立重跑）：在不同服务器上复现 exp-001/026 结果，验证 capability trap 的可复现性和排除服务器环境差异。\", \"conclusion\": \"negative\", \"metrics\": {\"n\": 204, \"dataset\": \"FOLIO-204\", \"model\": \"Qwen2.5-14B-Instruct\", \"k\": 12, \"sica_accuracy\": 75.49, \"sc_accuracy\": 77.45, \"delta_pp\": -1.96, \"sica_correct\": 154, \"sc_correct\": 158, \"mcnemar_discordant_b\": 0, \"mcnemar_discordant_c\": 4, \"mcnemar_p_value\": 0.125, \"extraction_rate\": 0.98, \"contradiction_rate\": 0.0097}}, \"exp-045b-backward-verify\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T20:16:45.453Z\", \"updated_at\": \"2026-05-18T20:30:28.631Z\", \"hypothesis\": \"Backward Verification v2 (正确模型 Qwen2.5-14B): 翻转验证方向，对每个候选答案反向推理 premises，用 Z3 检查一致性。v1 使用错误模型 (Qwen-7B) 得到 -21pp，需确认 Qwen-14B 上是否仍为强 negative（预期是，因为根因是 FOL quality 而非 model capacity）。\", \"conclusion\": \"killed\"}, \"exp-045-backward-verification\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T19:01:40.541Z\", \"updated_at\": \"2026-05-18T20:30:00.573Z\", \"hypothesis\": \"Backward Verification: 翻转验证方向，对每个候选答案反向推理需要哪些 premises 成立/矛盾，用 Z3 检查哪个答案与 premises 最一致（矛盾最少）。如果 forward extraction 质量是瓶颈，backward verification 绕过 extraction 直接用 solver 判断一致性，可能打破 capability trap。\", \"conclusion\": \"negative\", \"notes\": \"v1: 可能使用了 Qwen-7B 残留 vLLM (exp-035 遗留 port 8003)。BV=53.92% vs SC=75.00%, delta=-21.08pp。Z3 SAT rate 95.3%=无判别力。True bias 72.5% vs gold 35.3%。根因：backward FOL generation 质量同样差，验证方向不解决 capability trap。即使换正确模型 (-21pp 幅度过大) 可能仍 negative。建议 Director 决策是否用 Qwen2.5-14B 重跑 v2。\"}, \"exp-038-14b-logiqa200-16639\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T18:01:33.795Z\", \"updated_at\": \"2026-05-18T20:27:39.296Z\", \"hypothesis\": \"Qwen2.5-14B-Instruct 在 LogiQA 2.0 (200题) 上 SICA vs SC：跨数据集验证 capability trap。LogiQA 是多选逻辑推理（非二元分类），constraint extraction 和 Z3 formalization 需要适配不同推理类型。\", \"conclusion\": \"negative\", \"metrics\": {\"n\": 200, \"dataset\": \"LogiQA-200\", \"model\": \"Qwen2.5-14B-Instruct\", \"k\": 12, \"sica_accuracy\": 78, \"sc_accuracy\": 78.5, \"delta_pp\": -0.5, \"mcnemar_p\": 1, \"sica_correct\": 156, \"sc_correct\": 157, \"discordant_b\": 1, \"discordant_c\": 2, \"both_correct\": 155, \"both_wrong\": 42, \"extraction_rate\": 0.864, \"fail_empty_rate\": 0.122, \"avg_unique_constraints\": 26.7, \"contradiction_rate\": 0.008, \"wall_time_min\": 126.8}, \"notes\": \"实验成功完成200/200题，之前被自动监控误判为failed。结果：SICA略逊于SC(-0.5%)，McNemar p=1.0完全不显著。仅3例disagreement(sica_only=1, sc_only=2)。extraction_rate=86.4%低于FOLIO实验(~90%+)，fail_empty=12.2%较高——LogiQA的非形式化推理对constraint extraction更难。contradiction_rate仅0.8%，几乎无矛盾检测。结论：SICA在LogiQA非形式逻辑推理上无增益，capability trap假设在此数据集上未验证。\"}, \"exp-033\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T17:42:09.819Z\", \"updated_at\": \"2026-05-18T20:25:06.703Z\", \"hypothesis\": \"Cross-family validation: Mistral-7B-Instruct-v0.3 在 FOLIO-204 全量上 SICA vs SC。验证 capability trap 跨模型家族在 full dataset 上是否持续（D012 pilot exp-010 已确认 delta=0, n=60）。\", \"metrics\": {\"n_problems\": 204, \"sica_accuracy\": 59.31, \"sc_accuracy\": 54.41, \"delta_pp\": 4.9, \"sica_correct\": 121, \"sc_correct\": 111, \"mcnemar_discordant_b\": 12, \"mcnemar_discordant_c\": 2, \"mcnemar_p_value\": 0.0129, \"c0_non_unanimous_rate\": 0.8137, \"avg_majority_frac\": 0.7515, \"extraction_rate\": 97.14, \"contradiction_rate\": 3.5, \"problems_with_contradictions\": 128, \"avg_unique_constraints\": 39.3, \"maxsat_mean_sat_ratio\": 0.9609, \"total_constraints\": 14042, \"unique_constraints\": 8021, \"wall_time_min\": 81.4, \"k\": 12}, \"conclusion\": \"success\", \"notes\": \"Mistral-7B FOLIO-204: SICA 59.31% vs SC 54.41%, delta=+4.90pp (McNemar p=0.013, significant). 首次 SICA 显著超越 SC。关键因素：C0=81.37%（远高于 Qwen-7B 的 55%），高 diversity 使 SC majority vote 退化，而 SICA MaxSAT 仍能从 noisy traces 中提取信号。Discordant: SICA-only=12, SC-only=2, 高度不对称。但绝对准确率低（59% vs Qwen-7B 77%），说明 Mistral-7B 基础推理能力弱。结论：capability trap 非普遍现象，依赖 diversity/quality 平衡——高 diversity + 低 quality 时 SICA 有优势。\"}, \"exp-042b-premise-formal\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T19:13:55.356Z\", \"updated_at\": \"2026-05-18T20:10:14.058Z\", \"hypothesis\": \"Premise-Only Formalization (重启): 绕过 CoT trace extraction，直接让 LLM 将 FOLIO premises + conclusion 形式化为 FOL，用 Z3 验证逻辑蕴含。K=12 独立 formalization + majority vote。如果 extraction quality 是 capability trap 的瓶颈，直接 formalization 应能产生更准确的约束，使 Premise-FOL > vanilla SICA。exp-042 因 vLLM 未启动失败，本次重启。\", \"parent\": \"exp-042-premise-formalization\", \"conclusion\": \"failed\", \"notes\": \"失败根因：run_premise_formalization.sh 参数顺序是 PORT GPU，但调用传了 GPU PORT (2 8002)，导致 CUDA_VISIBLE_DEVICES=8002 → NVMLError_InvalidArgument。vLLM 未启动，0 题完成。将在 cleanup Worker 中用显式命令重部署。\"}, \"exp-044-icl-oracle\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T19:01:36.630Z\", \"updated_at\": \"2026-05-18T19:54:58.560Z\", \"hypothesis\": \"ICL with Oracle Examples: 用 5 个 gold FOL annotations 作为 few-shot examples 教 LLM 提取高质量约束。如果 extraction quality 是 capability trap 瓶颈，oracle-guided extraction 应能产生更 discriminative 的约束，使 ICL-SICA > vanilla SICA (74.51%)。评测 199 题（排除 5 个 ICL examples）。\", \"conclusion\": \"failed\", \"notes\": \"v2 失败: vLLM server 连接中断 (httpx.ConnectError: All connection attempts failed)，EXIT_CODE=129 (SIGHUP)。实验跑完但数据无效：extraction 成功率仅 17.1% (307/1800, 1490 json_fail)，SC=46.23% 远低于 Qwen2.5-14B 预期 75.49%。结果不可用，需在 vLLM 稳定后重跑。worker_infra_westd25068-gpu-cleanup-redeploy 正在处理 westd-25068 基础设施。\"}, \"exp-035\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T16:02:20.251Z\", \"updated_at\": \"2026-05-18T19:07:57.772Z\", \"hypothesis\": \"Qwen2.5-7B-Instruct 在 FOLIO-204 上 SICA vs SC：within-family scaling 下界验证。弱模型 C0 更高（更多 diversity），但 constraint quality 更差，SICA 仍无法 outperform SC。与 exp-004-qwen7b (D012 delta=0) 在 full FOLIO 上的扩展验证。代替原 ARC-60 实验（exp-035 v1 因平台 kill 失败）。\", \"conclusion\": \"negative\", \"notes\": \"v2 完成: Qwen2.5-7B FOLIO-204, 203/204题有结果(1题缺失)。JSON summary是stale的(n=195时计算)，实际数据从results数组203条计算。SICA与SC仅3个discordant pairs，几乎完全一致。假设验证：SICA无法outperform SC on 7B，delta=-0.49pp (p=1.0)。C0=0.55高于14B但未能转化为SICA优势。注意7B SC(77.34%)意外高于14B SC(75.49%)，可能因FOLIO数据特性。\", \"metrics\": {\"n_problems\": 203, \"sc_accuracy\": 77.34, \"sica_accuracy\": 76.85, \"delta_pp\": -0.49, \"sica_correct\": 156, \"sc_correct\": 157, \"mcnemar_discordant_b\": 1, \"mcnemar_discordant_c\": 2, \"mcnemar_p_value\": 1, \"c0_non_unanimous_rate\": 0.5517, \"extraction_rate\": 98.19, \"contradiction_rate\": 1.58, \"problems_with_contradictions\": 60, \"total_constraints\": 12950, \"unique_constraints\": 6515, \"dedup_ratio\": 50.3, \"wall_time_min\": 78.2, \"avg_per_problem_s\": 23.1}}, \"exp-036b-cross-trace-unsat\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T19:04:24.962Z\", \"updated_at\": \"2026-05-18T19:04:55.982Z\", \"hypothesis\": \"Cross-trace UNSAT: 合并不同候选答案的 constraints，检查 answer_A 与 answer_B 的约束是否 UNSAT（矛盾）。预期 cross-answer 对比的 UNSAT rate 远高于 within-trace 检查，因为不同答案的约束应该矛盾。如果 UNSAT 信号强，可用于增强 SICA 打分的 discriminative power。\", \"conclusion\": \"negative\", \"metrics\": {\"cross_unsat_rate_pair\": 0.087, \"cross_unsat_rate_problem\": 0.107, \"within_trace_unsat_rate\": 0.009, \"unsat_pairs\": 11, \"total_pairs\": 126, \"problems_with_unsat\": 9, \"multi_answer_problems\": 84, \"single_answer_skip\": 120, \"zero_shared_var_pairs_pct\": 0.564, \"avg_shared_vars\": 2.7, \"false_true_unsat_rate\": 0.467, \"sica_cross_ut_accuracy\": 0.745, \"sc_accuracy\": 0.75, \"accuracy_impact\": 0}, \"notes\": \"Cross-trace UNSAT 验证了 Director 假设：cross-answer UNSAT rate (8.7%) 约为 within-trace (0.9%) 的 10x。但主要瓶颈是 Z3 变量命名不一致：56.4% 的 answer pairs 共享零变量，Z3 无法跨 trace 比较。False-True 对最具辨别力 (non-empty 中 46.7% UNSAT)。最终对准确率无影响（仅覆盖 9/204 问题），第 6 个 negative constructive。核心诊断价值：变量命名不一致是 capability trap 的关键机制之一。\"}, \"exp-042-premise-formalization\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T18:53:36.547Z\", \"updated_at\": \"2026-05-18T19:02:37.081Z\", \"hypothesis\": \"Premise-Only Formalization: 绕过 CoT trace extraction，直接让 LLM 将 FOLIO premises + conclusion 形式化为 FOL，用 Z3 验证逻辑蕴含。K=12 独立 formalization + majority vote。如果 extraction quality 是 capability trap 的瓶颈，直接 formalization 应能产生更准确的约束，使 Premise-FOL > vanilla SICA。\", \"conclusion\": \"failed\"}, \"exp-043-consistency-filtering\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T18:58:40.028Z\", \"updated_at\": \"2026-05-18T18:59:10.069Z\", \"hypothesis\": \"Constraint Consistency Filtering: 从已有 exp-001 数据中，只保留在 ≥T/K 条 trace 中出现的约束（T=4,6,8），用筛选后的约束跑 MAX-SAT。假设跨 trace 一致出现的约束质量更高，filtered SICA > full SICA。\", \"conclusion\": \"negative\", \"metrics\": {\"sc_accuracy\": 0.75, \"sica_t1_all\": 0.7794, \"sica_t4\": 0.75, \"sica_t6\": 0.7549, \"sica_t8\": 0.7549, \"avg_unique_constraints\": 13.2, \"avg_filtered_t4\": 1.8, \"avg_filtered_t6\": 0.8, \"avg_filtered_t8\": 0.3}, \"notes\": \"Consistency filtering NEGATIVE: 过滤后约束数量骤降（T≥4 仅 1.8/题, T≥8 仅 0.3/题），MaxSAT 无法区分答案，退化为 SC。根因：Z3 变量命名不一致导致语义等价约束被视为不同（avg 13.2 unique constraints/problem），跨 trace 一致性极低。第 5 个 negative constructive intervention。注意：T=1 的 77.94% 与 exp-001 的 74.51% 差异是已知 pipeline 非确定性问题（code path confound）。\"}, \"exp-036-z3-feedback-folio204\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T17:18:09.052Z\", \"updated_at\": \"2026-05-18T18:53:05.656Z\", \"hypothesis\": \"Z3 UNSAT core feedback refinement: closed-loop 方法用 Z3 solver 的 UNSAT core 指导 LLM 修正矛盾约束（最多 3 轮）。如果约束质量是瓶颈，solver 反馈应能提升 constraint discriminative power，使 Z3-feedback SICA > vanilla SICA。目标 recovery_rate > 0%（recovery_rate = Z3fb_delta / oracle_delta × 100%）。与之前 open-loop interventions（contrastive/cross-model/generational 全部失败）对比，closed-loop 利用 formal verification 信号可能是打破 capability trap 的关键。\", \"conclusion\": \"negative\", \"notes\": \"Z3 feedback mechanism had zero real impact. Apparent +3.0pp (77.5% vs 74.5%) entirely due to code path confound: JSON serialization vs in-memory processing caused different dedup/scoring behavior. UNSAT trigger rate 0.9% (22/2448 traces), too low for feedback loop to meaningfully activate. All observed delta on discordant problems came from pipeline non-determinism, not Z3 refinement. Fourth negative constructive intervention after contrastive, cross-model, generational.\", \"metrics\": {\"z3fb_sica_accuracy\": 0.775, \"vanilla_sica_accuracy\": 0.745, \"sc_accuracy\": 0.75, \"z3fb_vs_vanilla_delta\": 0.03, \"unsat_traces\": 22, \"total_traces\": 2448, \"unsat_rate\": 0.009, \"unsat_resolve_rate\": 0.864, \"problems_flipped\": 0, \"real_impact\": 0}}, \"exp-028-qwen3-14b-thinking\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T14:02:12.168Z\", \"updated_at\": \"2026-05-18T18:06:48.306Z\", \"hypothesis\": \"Qwen3-14B thinking mode 在 FOLIO 204 上 SICA vs SC：原生推理能力（内置 CoT）是否改变 capability trap？两种可能：(a) thinking mode 使 traces 更确定性（类似 QwQ-32B），C0 极低→SICA≡SC；(b) thinking mode 提升 constraint extraction 质量，打破 capability trap。预期 (a) 更可能。\", \"parent\": \"sica_expanded_14b\", \"conclusion\": \"killed\", \"notes\": \"Killed per D049: extraction_rate 73% below 80% threshold. Partial results (35/204): SICA 88.57%, SC 85.71%, delta +2.86pp. But extraction_rate degrading and ETA 16h+ made continued run not worthwhile. GPU freed for D050 constructive experiments.\"}, \"exp-033-qwen3-pw600-nonthinking\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T16:01:55.209Z\", \"updated_at\": \"2026-05-18T18:00:09.156Z\", \"hypothesis\": \"Qwen3-14B in non-thinking mode on ProofWriter 600 will show whether SICA's constraint-based consensus improves over SC@K for a model without chain-of-thought reasoning overhead, providing a controlled comparison against thinking-mode results.\", \"conclusion\": \"failed\", \"notes\": \"FAILED: AutoDL 平台级 SIGTERM 导致 vLLM EngineCore 崩溃 (00:05:54)，后紧急清理 Worker 误杀 tmux server 连带终止。518/600 intermediates 有效可恢复。\"}, \"exp-004-qwen7b-rerun\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T16:16:48.010Z\", \"updated_at\": \"2026-05-18T18:00:08.383Z\", \"hypothesis\": \"Qwen2.5-7B-Instruct 在 D012 60 题上 SICA vs SC rerun（修复后代码）：弱模型 C0 更高（更多 diversity），但 constraint quality 更差，SICA 仍无法 outperform SC。验证 capability trap 在 within-family scaling 的下界。与之前 exp-004-qwen7b (delta=0) 对比验证一致性。\", \"parent\": \"sica_expanded_14b\", \"conclusion\": \"failed\", \"notes\": \"FAILED: ModelScope 下载失败，Qwen2.5-7B-Instruct 模型下载未完成。实验从未开始运行。需要 HF 镜像修复后重试。\"}, \"exp-007-qwen72b-awq\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T16:16:47.099Z\", \"updated_at\": \"2026-05-18T18:00:07.574Z\", \"hypothesis\": \"Qwen2.5-72B-Instruct-AWQ (4-bit) 在 D012 60 题上 SICA vs SC：72B scaling 是否打破 capability trap？预期 SC baseline 更高（模型更强），但 SICA≈SC（extraction quality bottleneck 不随 model scale 改善），证明 scaling 不是 rescue path。\", \"parent\": \"sica_expanded_14b\", \"conclusion\": \"failed\", \"notes\": \"FAILED: HuggingFace 网络不通 (Network unreachable)，模型下载失败。72B AWQ 模型从未下载完成，实验从未开始运行。需要 HF 镜像修复后重试。\"}, \"exp-027-qwen3-14b-non-thinking\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T14:02:11.425Z\", \"updated_at\": \"2026-05-18T17:58:11.787Z\", \"hypothesis\": \"Qwen3-14B（代际升级）在 non-thinking mode 下 FOLIO 204 的 SICA vs SC：capability trap 是否在次世代模型持续？预期 Qwen3 基础能力提升使 SC baseline 更高，但 self-extraction 质量仍不足以产生 SICA 增益（delta≈0），证明 capability trap 是结构性的而非模型能力不足。\", \"parent\": \"sica_expanded_14b\", \"conclusion\": \"success\", \"metrics\": {\"n\": 204, \"k\": 12, \"sica_accuracy\": 0.8431, \"sc_accuracy\": 0.8382, \"delta_pp\": 0.49, \"extraction_rate\": 0.995, \"contradiction_rate\": 0.0283, \"problems_with_contradictions\": 69, \"total_constraints\": 16153, \"unique_constraints\": 7031, \"wall_time_s\": 11017, \"model\": \"Qwen3-14B\", \"dataset\": \"FOLIO-204\", \"mode\": \"non-thinking\"}, \"notes\": \"Qwen3-14B non-thinking FOLIO-204: SICA 84.31% vs SC 83.82%, delta=+0.49pp。Qwen3 SC baseline 83.82% 远高于 Qwen2.5-14B 的 75.00% (+8.82pp)，证明 Qwen3 基础能力显著提升。但 SICA-SC gap 仍≈0 (+0.49pp)，capability trap 在次世代模型上持续。Extraction rate 99.5% (vs 14B 98.5%)，contradiction rate 2.83%。论文价值：(1) 证明 capability trap 是结构性的，非模型能力不足；(2) 代际升级提升 SC 不提升 SICA delta。\"}, \"exp-030-crossmodel-mistral-folio204\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T14:47:46.451Z\", \"updated_at\": \"2026-05-18T16:16:11.345Z\", \"hypothesis\": \"Cross-model extraction: Mistral-7B 从 Qwen2.5-14B 的 FOLIO 204 traces 中提取 constraints，能否打破 same-model capability trap？不同模型有不同的 extraction bias，Mistral 可能提取出 Qwen self-extraction 遗漏的 discriminative constraints。目标 discriminative_rate >8.2%（baseline），recovery_rate >0%。\", \"parent\": \"exp-026-folio204-trace-regen\", \"conclusion\": \"negative\", \"metrics\": {\"n\": 204, \"k\": 12, \"crossmodel_sica_accuracy\": 0.75, \"sc_accuracy\": 0.75, \"delta_pp\": 0, \"discriminative_rate\": 0, \"recovery_rate\": 0, \"model_extraction\": \"Mistral-7B-Instruct-v0.3\", \"model_traces\": \"Qwen2.5-14B-Instruct\", \"dataset\": \"FOLIO-204\"}, \"notes\": \"NEGATIVE. Cross-model extraction (Mistral-7B extracts constraints from Qwen2.5-14B traces) 完全无效：SICA = SC = 75.00%, discriminative_rate=0%, recovery_rate=0%. Mistral 虽然是不同模型家族，但提取的 constraints 同样缺乏判别力。这进一步强化 capability trap 结论：问题不在 same-model bias，而在 LLM extraction 本身的能力限制——无论哪个模型做 extraction，都无法从 CoT traces 中提取出对答案有判别力的 symbolic constraints。论文 claim: cross-model 不是 rescue path。\"}, \"exp-031-oracle-folio-regen\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T15:48:41.292Z\", \"updated_at\": \"2026-05-18T15:55:28.070Z\", \"hypothesis\": \"Oracle SICA with gold FOL annotations on exp-026 regenerated traces (post normalization-fix): if constraint quality is the bottleneck, replacing self-extracted constraints with gold FOL + Z3 entailment should significantly outperform SC and SICA(self), replicating exp-021's finding on fixed code.\", \"conclusion\": \"success\", \"metrics\": {\"n\": 204, \"k\": 12, \"oracle_sica_accuracy\": 0.8971, \"sc_accuracy\": 0.7549, \"sica_self_accuracy\": 0.7451, \"oracle_vs_sc_delta_pp\": 14.22, \"oracle_vs_sica_delta_pp\": 15.2, \"mcnemar_p_oracle_vs_sc\": 2.0024e-07, \"mcnemar_b_c\": {\"b_oracle_right_sc_wrong\": 29, \"c_oracle_wrong_sc_right\": 0}, \"z3_gold_agreement\": 0.951, \"z3_gold_agree_n\": 194, \"z3_in_candidates_n\": 178, \"fol_parse_success\": 1, \"model\": \"Qwen2.5-14B-Instruct\", \"dataset\": \"FOLIO-204\", \"constraint_source\": \"gold FOL annotations\", \"traces_source\": \"exp-026-folio204-trace-regen\"}, \"notes\": \"KEY RESULT. Oracle-SICA (gold FOL + Z3 entailment + consistency-weighted voting) 89.71% vs SC 75.49% vs SICA(self) 74.51%, +14.22pp over SC, McNemar p=2.0e-07 极显著, b=29 c=0 (oracle 从未输给 SC)。Z3 gold agreement 95.10% (194/204), FOL parser 204/204 全成功。Per-type: True 97.2% (+4.1pp), False 93.6% (+6.3pp), Unknown 78.3% (+31.9pp)。与 exp-021 (88.24%, 旧 traces) 对比：oracle 准确率从 88.24% 提升至 89.71%（+1.47pp），delta 从 +8.82pp 增至 +14.22pp。差异来源：(1) exp-026 traces 的 SC baseline 更低 (75.49% vs 79.41%)；(2) Z3 agreement 从 94.6% 提升至 95.1%。结论与 exp-021 一致：MAX-SAT 聚合机制有效——瓶颈在约束提取质量。\"}, \"exp-029-contrastive-folio204\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T14:22:03.513Z\", \"updated_at\": \"2026-05-18T15:38:58.925Z\", \"hypothesis\": \"Contrastive constraint extraction (answer-conditioned supporting/opposing constraints with structured JSON output and MaxSAT integration) will achieve discriminative_rate >20% (vs baseline 8.2%) and positive recovery_rate on FOLIO 204, because per-candidate opposing constraints provide stronger signal than simple majority voting for disambiguating closely-scored answers.\", \"parent\": \"exp-026-folio204-trace-regen\", \"conclusion\": \"negative\", \"metrics\": {\"contrastive_accuracy\": 0.7253, \"sc_accuracy\": 0.7363, \"delta_pp\": -1.1, \"discriminative_rate\": 0.0604, \"discriminative_count\": 11, \"n\": 182, \"recovery_rate_pct\": -8.3, \"mcnemar_chi2\": 0.1, \"mcnemar_p\": 0.7518, \"cont_only_correct\": 4, \"sc_only_correct\": 6, \"both_correct\": 128, \"both_wrong\": 44, \"supporting_pct\": 43.2, \"opposing_pct\": 56.8, \"avg_constraints_per_problem\": 24.4, \"avg_unique_per_problem\": 10.4, \"wall_time_min\": 47.2}}, \"exp-026-folio204-trace-regen\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T11:41:13.054Z\", \"updated_at\": \"2026-05-18T14:46:34.862Z\", \"hypothesis\": \"FOLIO 204 全量 trace 重生成（Qwen2.5-14B, K=12, T=0.7 trace gen, T_ext=0.3 extraction）：在 westd-25068 上生成 FOLIO traces，用于 cross-model extraction 和 case study 选取。归一化 bug 已修复（startswith 方案），温度双参数已正确分离。\", \"parent\": \"sica_expanded_14b\", \"conclusion\": \"success\", \"metrics\": {\"n\": 204, \"k\": 12, \"sica_accuracy\": 0.7451, \"sc_accuracy\": 0.7549, \"delta_pp\": -0.98, \"extraction_rate\": 0.9853, \"model\": \"Qwen2.5-14B-Instruct\", \"dataset\": \"FOLIO-204\", \"temperature_trace\": 0.7, \"temperature_extraction\": 0.3, \"wall_time_h\": 2.5}, \"notes\": \"FOLIO 204 全量 trace 重生成完成 (204/204)。SICA 74.51% vs SC 75.00%, delta=-0.49pp，与 sica_expanded_14b FOLIO 子集 (79.4%/79.4%, delta=0) 一致——capability trap 在重生成 traces 上仍成立。归一化 bug 修复 + 温度双参数分离后 extraction_rate=98.53% (vs 之前 89%)。Traces 已被 exp-029 contrastive 实验复用。结果路径: /root/symb_invariant_consensus/results/folio_204_14b/folio_204_results.json\"}, \"exp-023-discriminative-rate\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T03:50:26.792Z\", \"updated_at\": \"2026-05-18T04:44:24.397Z\", \"hypothesis\": \"Full-dataset discriminative rate analysis (W1+W3 合并): Qwen2.5-14B 在 804 题上 self-extracted constraints 的 source-trace discriminativeness 和 Z3 semantic discriminativeness 均低于 15%，证明即使用 Z3 per-answer evaluation，self-extracted constraints 仍无判别力，封堵 oracle scoring confound。\", \"parent\": \"sica_constraint_ablation_013\", \"metrics\": {\"n_total\": 804, \"n_multi_candidate\": 307, \"source_disc_rate_weight\": 0.392, \"source_disc_rate_weight_ci95\": [0.387, 0.398], \"source_disc_rate_count_est\": 0.121, \"source_disc_rate_count_ci95\": [0.12, 0.123], \"z3_semantic_disc_rate\": 0.082, \"z3_semantic_disc_ci95\": [0.076, 0.088], \"problems_with_disc\": 289, \"problems_with_disc_rate\": 0.941, \"pw_source_disc_weight\": 0.364, \"folio_source_disc_weight\": 0.54, \"pw_n_multi\": 235, \"folio_n_multi\": 72, \"pilot_rate_reported_count\": 0.115, \"pilot_rate_reported_weight\": 0.372, \"pilot_validation_weight\": 0.376, \"pilot_delta_pp\": 0.38, \"z3_answer_assertions\": 642, \"z3_total_unique_constraints\": 7844, \"model\": \"Qwen2.5-14B-Instruct\", \"dataset\": \"FOLIO+ProofWriter-804\"}, \"conclusion\": \"success\", \"notes\": \"Full 804-instance discriminative rate (R3 W1+W3, v1+v2 合并). By weight: 39.2% [38.7, 39.8]; by count (est): 12.1% [12.0, 12.3]. Z3 semantic disc: 8.2% [7.6, 8.8]. Per-domain: FOLIO 54.0% > PW 36.4% (by weight). 289/307 multi-candidate 问题有≥1 discriminative constraint (94.1%). Pilot validation: weight 37.6% vs 报告 37.2% (delta 0.38pp); count 12.1% vs 报告 11.5% (delta 0.6pp)——高度一致。v2 修复了 v1 的 assertion weight 不对称问题。数据: /root/symb_invariant_consensus/analysis/discriminative_rate_full_804.json\"}, \"exp-022-oracle-proofwriter\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T03:47:31.892Z\", \"updated_at\": \"2026-05-18T03:48:13.174Z\", \"hypothesis\": \"ProofWriter oracle: gold DSL (raw_logic_programs) 通过 Z3 consistency checking 加权 K=12 traces，Oracle-SICA 应显著超越 SC 和 SICA(self)，在 ProofWriter 600 题上复现 FOLIO oracle (+8.82pp) 的 extraction bottleneck 结论。\", \"parent\": \"exp-021-oracle-folio\", \"conclusion\": \"success\", \"metrics\": {\"n\": 600, \"k\": 12, \"oracle_sica_accuracy\": 0.8667, \"sc_accuracy\": 0.7517, \"sica_self_accuracy\": 0.755, \"oracle_vs_sc_delta_pp\": 11.5, \"mcnemar_p_oracle_vs_sc\": 9.21e-15, \"z3_gold_agreement\": 0.9714, \"z3_gold_agree_n\": 577, \"z3_gold_total\": 594, \"parse_errors\": 6, \"parse_error_rate\": 0.01, \"solver_errors\": 0, \"solver_total\": 7128, \"relneg_oracle\": 0.7786, \"relneg_sc\": 0.6, \"relneg_delta_pp\": 17.86, \"relnoneg_oracle\": 0.7945, \"relnoneg_sc\": 0.6644, \"relnoneg_delta_pp\": 13.01, \"attnoneg_oracle\": 0.961, \"attnoneg_sc\": 0.8701, \"attnoneg_delta_pp\": 9.09, \"attneg_oracle\": 0.9188, \"attneg_sc\": 0.85, \"attneg_delta_pp\": 6.87, \"model\": \"Qwen2.5-14B-Instruct\", \"dataset\": \"ProofWriter-OWA-D5-600\", \"constraint_source\": \"gold DSL (raw_logic_programs)\"}, \"notes\": \"KEY RESULT. ProofWriter Oracle-SICA (gold DSL + Z3 + MAX-SAT) 86.67% vs SC 75.17% vs SICA(self) 75.50%, +11.50pp, McNemar p=9.21e-15 极显著。Z3 gold agreement 97.14% (577/594), parse errors 仅 6/600 (1%), solver errors 0/7128。Per-subtype: RelNeg +17.86pp > RelNoneg +13.01pp > AttNoneg +9.09pp > AttNeg +6.87pp——关系谓词（推理链更长）获益远大于属性谓词。与 FOLIO oracle (exp-021, +8.82pp, p=6.15e-5) 对比：ProofWriter delta 更大 (+11.50 vs +8.82) 且统计显著性高 6 个数量级。两个子域 Oracle 实验一致证明：MAX-SAT 聚合机制有效，瓶颈在 LLM self-extraction 质量。\"}, \"temperature-ablation-t07\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T18:03:05.890Z\", \"updated_at\": \"2026-05-17T19:11:20.157Z\", \"hypothesis\": \"Temperature ablation T=0.7 同源补跑：消除 T=0.7 数据来自不同 run (sica_d012_14b) 的混淆。预期 Δ=0（与 T=0.3/0.5/1.0 一致），C0 值可直接与其他温度点比较。\", \"parent\": \"temperature-ablation-t03\", \"metrics\": {\"n\": 60, \"k\": 12, \"sica_accuracy\": 0.7167, \"sc_accuracy\": 0.75, \"delta_pp\": -3.33, \"multi_candidate_rate\": 0.4, \"extraction_rate\": 0.9208, \"answer_extraction_rate\": 1, \"contradiction_rate\": 0.022, \"discordant_sica_wins\": 0, \"discordant_sc_wins\": 2, \"truncated_traces\": 0, \"model\": \"Qwen2.5-14B-Instruct\", \"dataset\": \"D012\", \"temperature\": 0.7, \"proofwriter_sica\": 0.6333, \"proofwriter_sc\": 0.7, \"proofwriter_n\": 30, \"folio_sica\": 0.8, \"folio_sc\": 0.8, \"folio_n\": 30, \"wall_time_s\": 3498.3}, \"notes\": \"T=0.7 同源补跑完成（60/60 题）。C0=40.0%，介于 T=0.5(38.3%) 和 T=1.0(43.3%) 之间，消除了旧数据 T=0.7(53.3%) 来自不同 run 的混淆。四温度点 C0 现呈单调递增：T=0.3(30%) → T=0.5(38.3%) → T=0.7(40.0%) → T=1.0(43.3%)。SICA 71.67% < SC 75.00%，delta=-3.33pp，discordant 0:2（SC wins only）。FOLIO 80%=80%，PW SICA 63.33% < SC 70%。结论与其他温度点一致：diversity 增加但 constraint quality 无改善，delta≈0。\", \"conclusion\": \"negative\"}, \"sica_constraint_ablation_013\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T20:26:35.414Z\", \"updated_at\": \"2026-05-17T18:38:00.543Z\", \"conclusion\": \"success\", \"hypothesis\": \"exp-013: MaxSAT 加权聚合是否比 count-only 或 random-weight 有显著优势？验证 SICA 核心机制（约束加权）的实际贡献\", \"parent\": \"sica_expanded_14b\", \"metrics\": {\"maxsat_accuracy\": 0.7649, \"count_only_accuracy\": 0.7662, \"random_weight_accuracy\": 0.7587, \"sc_baseline_accuracy\": 0.7624, \"n_problems\": 804, \"maxsat_correct\": 615, \"count_only_correct\": 616, \"random_weight_correct\": 610, \"sc_correct\": 613, \"agreement_maxsat_vs_countonly\": \"803/804\", \"agreement_maxsat_vs_randomwt\": \"785/804\", \"agreement_maxsat_vs_sc\": \"773/804\", \"agreement_countonly_vs_randomwt\": \"786/804\", \"agreement_countonly_vs_sc\": \"774/804\", \"agreement_randomwt_vs_sc\": \"764/804\", \"mcnemar_p_all_gt_0.7\": true}, \"notes\": \"exp-013 constraint ablation 完成，数据已从 ablation_results.json 交叉验证。关键修正：(1) 802/804 不存在于任何 pairwise comparison，原 registry 数据错误；(2) random-weight accuracy 修正为 75.87% (610/804)，原 76.37% 是近似值。核心发现：MaxSAT vs Count-only 803/804 agreement 确认 SAT solver 无增量。MaxSAT vs SC 773/804 (31 disagreements, 16 SICA wins / 14 SC wins / 1 both wrong diff)——SICA 改了 31 题但 wins/losses 几乎抵消。数据文件：/root/symb_invariant_consensus/analysis/exp013_agreement_matrix.json\"}, \"exp-004-qwen7b\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T17:09:36.912Z\", \"updated_at\": \"2026-05-17T18:10:04.422Z\", \"hypothesis\": \"Within-family scaling: Qwen2.5-7B-Instruct 在 D012 60 题上 SICA vs SC。弱模型预期 C0 > 14B（更多 diversity），但 constraint quality 预期更低，SICA-SC gap 预期≈0——验证 capability trap 的 scaling 维度。\", \"parent\": \"sica_expanded_14b\", \"conclusion\": \"negative\", \"notes\": \"Qwen2.5-7B within-family scaling: SICA=SC=68.33% (41/60), Δ=0.00pp, C0=43.3%, McNemar p=1.0。60 题全部完成（run.log 确认）。C0=43.3% 高于 14B 的 38.2%（弱模型更多 diversity），但 Δ=0 确认 capability trap 在 7B scale 同样成立。Discordant 2:2 完全对称。Per-domain: FOLIO SICA 76.7% vs SC 73.3% (+3.3pp), PW SICA 60.0% vs SC 63.3% (-3.3pp)，方向相反互相抵消。extraction_rate=94.2%。\", \"metrics\": {\"n\": 60, \"k\": 12, \"sica_accuracy\": 0.6833, \"sc_accuracy\": 0.6833, \"delta_pp\": 0, \"multi_candidate_rate\": 0.433, \"extraction_rate\": 0.9417, \"answer_extraction_rate\": 1, \"contradiction_rate\": 0.0274, \"discordant_sica_wins\": 2, \"discordant_sc_wins\": 2, \"mcnemar_p\": 1, \"wall_time_s\": 1838, \"truncated_traces\": 0, \"model\": \"Qwen2.5-7B-Instruct\", \"dataset\": \"D012\", \"temperature\": 0.7, \"folio_sica\": 0.7667, \"folio_sc\": 0.7333, \"folio_n\": 30, \"proofwriter_sica\": 0.6, \"proofwriter_sc\": 0.6333, \"proofwriter_n\": 30}}, \"temperature-ablation-t10\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T13:46:01.069Z\", \"updated_at\": \"2026-05-17T17:16:54.736Z\", \"hypothesis\": \"Temperature ablation T=1.0: 高温下 Qwen2.5-14B trace diversity 最大化（C0 预期>60%），SICA-SC gap 预期≈0 或负——验证最大 diversity 仍不能拯救 SICA，因为 constraint discriminative power 不随 diversity 增加\", \"parent\": \"sica_expanded_14b\", \"notes\": \"T=1.0 高温：C0=43.3%，低于 T=0.7 的 53.3%（注意：T=0.7 数据来自 sica_d012_14b 不同 run）。SICA=SC=75.00%，delta=0，discordant=0。最大温度仍不能拯救 SICA。Temperature ablation 结论：T=0.3(30%) → T=0.5(38.3%) → T=1.0(43.3%) 三点 C0 递增，但加上 T=0.7(53.3%, 来自 sica_d012_14b) 后整体非单调（T=0.7 > T=1.0）。不同 run 间 C0 有随机波动。核心结论不变：delta 始终=0，diversity 不是瓶颈。\", \"metrics\": {\"n\": 60, \"k\": 12, \"sica_accuracy\": 0.75, \"sc_accuracy\": 0.75, \"delta_pp\": 0, \"multi_candidate_rate\": 0.433, \"discordant_total\": 0, \"model\": \"Qwen2.5-14B-Instruct\", \"dataset\": \"D012\", \"temperature\": 1}, \"conclusion\": \"negative\"}, \"exp-012-gsm8k-pilot\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T16:47:20.559Z\", \"updated_at\": \"2026-05-17T17:09:35.283Z\", \"hypothesis\": \"Cross-domain validation: Qwen2.5-14B-Instruct 在 GSM8K (开放答案数学域) 30 题上 SICA vs SC。预期 C0<20%（14B 在 GSM8K 太强），验证 C0 作为 SICA 无效性预测指标。\", \"parent\": \"sica_expanded_14b\", \"metrics\": {\"n\": 30, \"k\": 12, \"sica_accuracy\": 0.9667, \"sc_accuracy\": 0.9667, \"delta_pp\": 0, \"multi_candidate_rate\": 0.133, \"extraction_success_rate\": 0.147, \"model\": \"Qwen2.5-14B-Instruct\", \"dataset\": \"GSM8K\", \"temperature\": 0.7}, \"conclusion\": \"negative\", \"notes\": \"GSM8K 30题：SICA=SC=96.67%，delta=0，C0=13.3%。开放答案数学域 baseline 极高（96.67%），几乎无 diversity（C0=13.3%），extraction_success_rate 仅 14.7%——数学域的 symbolic constraints 难以提取。支持 C0 作为 SICA 无效性预测指标。\"}, \"exp-021-oracle-folio\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T16:36:04.545Z\", \"updated_at\": \"2026-05-17T16:48:21.295Z\", \"hypothesis\": \"If we replace self-extracted constraints with gold FOL annotations verified by Z3, Oracle-SICA should significantly outperform both SC and SICA, demonstrating that constraint quality is the bottleneck for SICA gains on formal logic tasks.\", \"parent\": \"sica_expanded_14b\", \"conclusion\": \"success\", \"metrics\": {\"n\": 204, \"k\": 12, \"oracle_sica_accuracy\": 0.8824, \"sc_accuracy\": 0.7941, \"sica_self_accuracy\": 0.7941, \"oracle_vs_sc_delta_pp\": 8.82, \"oracle_vs_sica_delta_pp\": 8.82, \"mcnemar_p_oracle_vs_sc\": 6.15e-05, \"z3_gold_agreement\": 0.946, \"fol_parse_success\": 1, \"model\": \"Qwen2.5-14B-Instruct\", \"dataset\": \"FOLIO-204\", \"constraint_source\": \"gold FOL annotations\"}, \"notes\": \"KEY RESULT. Oracle-SICA (gold FOL + Z3 consistency check + MAX-SAT) 88.24% vs SC 79.41% vs SICA(self-extracted) 79.41%, +8.82pp, McNemar p=6.15e-05 高度显著。Z3 solver 与 gold answer 一致率 94.6%（193/204），FOL parser 204/204 全部成功。SICA(self)=SC 确认 LLM 自提取约束在 formal logic 上无有效信号。结论：MAX-SAT 聚合机制本身有效——瓶颈在约束提取质量，不在聚合算法。这直接回答了 Reviewer 的核心 confound 质疑。\"}, \"temperature-ablation-t05\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T13:45:59.468Z\", \"updated_at\": \"2026-05-17T16:47:09.843Z\", \"hypothesis\": \"Temperature ablation T=0.5: 中温下 Qwen2.5-14B trace diversity 中等（C0 预期 30-45%），SICA-SC gap 预期≈0——验证即使 diversity 适中，constraint quality 仍为瓶颈\", \"parent\": \"sica_expanded_14b\", \"notes\": \"T=0.5 中温：C0=38.3%，SICA=SC=76.67%，delta=0，discordant=0。中等 diversity 下 SICA 仍完全等于 SC。\", \"metrics\": {\"n\": 60, \"k\": 12, \"sica_accuracy\": 0.7667, \"sc_accuracy\": 0.7667, \"delta_pp\": 0, \"multi_candidate_rate\": 0.383, \"discordant_total\": 0, \"model\": \"Qwen2.5-14B-Instruct\", \"dataset\": \"D012\", \"temperature\": 0.5}, \"conclusion\": \"negative\"}, \"temperature-ablation-t03\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T13:45:57.395Z\", \"updated_at\": \"2026-05-17T16:47:07.935Z\", \"hypothesis\": \"Temperature ablation T=0.3: 低温下 Qwen2.5-14B trace diversity 降低（C0 预期<30%），SICA-SC gap 预期≈0——验证 diversity 不足时 SICA 无操作空间，capability trap 的下界\", \"parent\": \"sica_expanded_14b\", \"metrics\": {\"n\": 60, \"k\": 12, \"sica_accuracy\": 0.7333, \"sc_accuracy\": 0.7333, \"delta_pp\": 0, \"multi_candidate_rate\": 0.3, \"discordant_total\": 0, \"model\": \"Qwen2.5-14B-Instruct\", \"dataset\": \"D012\", \"temperature\": 0.3}, \"conclusion\": \"negative\", \"notes\": \"T=0.3 低温：C0=30%（符合预期低于 T=0.7 的 53%），SICA=SC=73.33%，delta=0，discordant=0。低温降低 diversity 但 SICA 无任何改变——约束完全无判别力。\"}, \"exp-014-deepseek-r1-7b\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T11:52:10.748Z\", \"updated_at\": \"2026-05-17T13:43:42.275Z\", \"hypothesis\": \"DeepSeek-R1-Distill-Qwen-7B（reasoning distill 模型）在 D012 上 SICA vs SC——预期 C0<5%（类似 QwQ-32B，reasoning model 的确定性链消灭多样性），作为第二个 reasoning model 数据点验证 capability trap\", \"parent\": \"sica_expanded_14b\", \"metrics\": {\"n\": 60, \"k\": 12, \"sica_accuracy\": 0.6833, \"sc_accuracy\": 0.7167, \"delta_pp\": -3.33, \"multi_candidate_rate\": 0.583, \"extraction_rate\": 0.839, \"answer_extraction_rate\": 0.939, \"truncated_traces\": 72, \"contradiction_rate\": 0.037, \"wall_time_min\": 100.3, \"mcnemar_p\": 0.4795, \"discordant_sica_wins\": 0, \"discordant_sc_wins\": 2, \"model\": \"DeepSeek-R1-Distill-Qwen-7B\", \"dataset\": \"D012\"}, \"conclusion\": \"negative\", \"notes\": \"假设预判错误：预期 C0<5%（类似 QwQ-32B reasoning model），实际 C0=58.3%。DeepSeek-R1-Distill-Qwen-7B 因 7B 容量不足以维持确定性推理链，表现为 instruction-scale model。SICA -3.3pp，两子域对称（FOLIO -3.3pp, PW -3.3pp）。重新定位为第四个 instruction-scale 模型验证 capability trap。\"}, \"exp-010-mistral-v3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T06:48:05.255Z\", \"updated_at\": \"2026-05-17T13:39:59.922Z\", \"hypothesis\": \"Cross-family validation: Mistral-7B-Instruct-v0.3 在 D012 数据集(30PW+30FOLIO)上是否复现 SICA≈SC pattern——验证 capability trap 跨模型家族泛化（v3: 脚本内含 vLLM 清理+conda 环境，解决 v2 SIGTERM 问题）\", \"parent\": \"sica_expanded_14b\", \"metrics\": {\"n\": 60, \"k\": 12, \"sica_accuracy\": 0.4833, \"sc_accuracy\": 0.4833, \"delta_pp\": 0, \"multi_candidate_rate\": 0.5, \"extraction_rate\": 0.8819, \"answer_extraction_rate\": 1, \"contradiction_rate\": 0.0562, \"discordant_sica_wins\": 2, \"discordant_sc_wins\": 2, \"mcnemar_p\": 1, \"proofwriter_sica\": 0.4, \"proofwriter_sc\": 0.4, \"proofwriter_delta_pp\": 0, \"folio_sica\": 0.5667, \"folio_sc\": 0.5667, \"folio_delta_pp\": 0, \"truncated_traces\": 0, \"model\": \"Mistral-7B-Instruct-v0.3\", \"dataset\": \"D012\"}, \"conclusion\": \"negative\", \"notes\": \"Mistral-7B cross-family: SICA 48.33% = SC 48.33%, delta=0.00pp。Multi-candidate rate 50%（30/60 题非 unanimous），SICA 仅改变 4 题（6.67% flip rate）。模型太弱：SC baseline 48.33%（近随机），trace 缺乏质量但有多样性。Discordant 2:2 平局，McNemar p=1.0。支持 operating regime 有下界：模型必须足够强才能生成有意义的 diverse traces。PW 40%/40%, FOLIO 56.67%/56.67%。\"}, \"sica_expanded_14b\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T05:12:00.374Z\", \"updated_at\": \"2026-05-17T13:26:43.835Z\", \"conclusion\": \"success\", \"metrics\": {\"sica_accuracy\": 0.765, \"sc_accuracy\": 0.762, \"sica_sc_gap_pp\": 0.3, \"n_problems\": 804, \"multi_candidate_rate\": 0.3818, \"folio_sica\": 0.794, \"folio_sc\": 0.794, \"folio_gap_pp\": 0, \"folio_n\": 204, \"proofwriter_sica\": 0.755, \"proofwriter_sc\": 0.752, \"proofwriter_gap_pp\": 0.3, \"proofwriter_n\": 600, \"extraction_rate\": 0.89, \"answer_extraction_rate\": 1, \"contradiction_rate\": 0.022, \"problems_with_contradictions\": 331, \"truncated_traces\": 0, \"wall_time_min\": 826}, \"notes\": \"实验完整完成 804/804 题并保存结果。EXIT_CODE=129 是 SIGHUP 伪信号（进程退出阶段收到），非真实失败。日志末尾打印 \\\"FULL_MVP_DONE\\\" 后才出现 exit code。D025 pivot 确认：SICA≈SC (+0.3pp, N=804)，D012 +3.3pp 是小样本噪声。FOLIO sub-claim dead (0pp)。\", \"hypothesis\": \"Qwen2.5-14B-Instruct 在 N=804 (600PW+204FOLIO) 上 SICA 相比 SC 有统计显著优势（p<0.05）——full-scale validation of D012 preliminary +3.3pp signal\", \"parent\": \"sica_d012_14b\"}, \"exp-019-llama8b-strategyqa-200\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T08:07:01.919Z\", \"updated_at\": \"2026-05-17T13:26:41.871Z\", \"hypothesis\": \"Powered test: SICA 在弱模型（LLaMA-3.1-8B）上的增益在 n=200 StrategyQA 题时达到统计显著（p<0.05）——验证 operating regime 假设（D031 + exp-011 directionally positive +6.67pp）\", \"parent\": \"exp-011-llama8b-v3\", \"metrics\": {\"n\": 200, \"k\": 12, \"sica_accuracy\": 0.74, \"sc_accuracy\": 0.72, \"delta_pp\": 2, \"multi_candidate_rate\": 0.41, \"mcnemar_p\": 0.424, \"bootstrap_ci_95\": [-1.5, 5.5], \"bootstrap_p_delta_le_0\": 0.12, \"discordant_sica_wins\": 9, \"discordant_sc_wins\": 5, \"discordant_total\": 14, \"discordant_rate\": 0.07, \"sc_unanimous_rate\": 0.545, \"model\": \"LLaMA-3.1-8B-Instruct\", \"dataset\": \"StrategyQA\", \"wall_time_min\": 52}, \"conclusion\": \"negative\", \"notes\": \"StrategyQA 200题 powered test: SICA 74% vs SC 72%, +2.00pp, McNemar p=0.424, bootstrap CI [-1.5, +5.5] 跨零。统计不显著。exp-011 的 +6.67pp 在扩大样本后缩水 70%——小样本噪声。关键发现：(1) LLaMA-8B 在 StrategyQA 上 SC=72%，高于预期的 sweet spot (55-65%)，(2) 仅 14/200 (7%) discordant pairs，54.5% 全票一致，(3) SICA 仅充当 tiebreaker（9 wins 中 6 个是平票）。StrategyQA 不在 operating regime sweet spot 内。exp-020 FOLIO (SC≈60%) 是真正的 definitive test。\"}, \"exp-018-arc-v2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T06:13:27.054Z\", \"updated_at\": \"2026-05-17T13:26:39.502Z\", \"hypothesis\": \"Cross-domain validation: Qwen2.5-14B-Instruct 在 ARC-Challenge (科学多选, ABCD) 上 SICA vs SC——验证 capability trap 是否跨任务类型泛化（v2: build_generator bug 已修复）\", \"parent\": \"sica_expanded_14b\", \"conclusion\": \"success\", \"metrics\": {\"n\": 60, \"k\": 12, \"sica_accuracy\": 0.95, \"sc_accuracy\": 0.9667, \"delta_pp\": -1.67, \"multi_candidate_rate\": 0.05, \"extraction_rate\": 1, \"contradiction_detected\": 3, \"discordant_sica_wins\": 0, \"discordant_sc_wins\": 1, \"dataset\": \"ARC-Challenge\", \"model\": \"Qwen2.5-14B-Instruct\"}, \"notes\": \"ARC-Challenge cross-domain: SICA 95.00% vs SC 96.67%, gap=-1.67pp. SICA 略逊于 SC。模型在 ARC 上 baseline 极高(96.67%)，接近天花板——高准确率区间多样性低，SICA 无操作空间。与 StrategyQA (+3.33pp n.s.) 对比：简单任务（高 baseline）SICA 无效或有害，中等难度任务有微弱正向趋势但不显著。整体支持 capability trap：模型能力越强/任务越简单 → SC 已近最优 → SICA 无增量。\"}, \"exp-009-overhead-analysis\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T11:51:43.293Z\", \"updated_at\": \"2026-05-17T12:01:08.521Z\", \"hypothesis\": \"SICA pipeline 的 wall-time overhead breakdown: trace generation vs constraint extraction vs MaxSAT solving 各占多少——量化 SICA 相对 SC 的额外计算成本\", \"metrics\": {\"n\": 804, \"mean_total_wall_s\": 61.6, \"mean_trace_gen_s\": 31.6, \"trace_gen_pct\": 51.3, \"mean_extract_s\": 29, \"extract_pct\": 47, \"mean_dedup_s\": 1, \"dedup_pct\": 1.6, \"mean_maxsat_s\": 0.003, \"maxsat_pct\": 0.005, \"sica_overhead_s\": 30, \"sica_overhead_pct\": 48.7, \"pw_overhead_pct\": 51.3, \"folio_overhead_pct\": 38.6, \"p50_overhead_pct\": 48.9, \"p90_overhead_pct\": 57.6}, \"conclusion\": \"success\", \"notes\": \"SICA overhead 分析 (804题)：总时间 61.6s/题，其中 trace 生成 31.6s (51.3%)，约束提取 29.0s (47.0%)，去重 1.0s (1.6%)，MaxSAT 0.003s (≈0%)。SICA vs SC 多花 30.0s/题 (+48.7%)，开销几乎全部来自 constraint extraction LLM 调用。MaxSAT 求解可忽略。论文 insight：SICA 的计算瓶颈不在 formal reasoning (SAT) 而在 LLM extraction，且 extraction 产出的约束缺乏判别力——高成本低回报。\"}, \"exp-020-llama8b-folio-204\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T08:12:49.897Z\", \"updated_at\": \"2026-05-17T11:50:57.467Z\", \"hypothesis\": \"Powered FOLIO test: SICA 在弱模型（LLaMA-3.1-8B）上 FOLIO 全量 204 题是否达到统计显著——FOLIO 在 exp-011 中信号最强（+10pp, bootstrap p≈0.04），n=204 几乎必然显著。保险实验：若 StrategyQA discordant rate 低导致 underpowered。\", \"parent\": \"exp-011-llama8b-v3\", \"metrics\": {\"n\": 204, \"k\": 12, \"sica_accuracy\": 0.608, \"sc_accuracy\": 0.632, \"delta_pp\": -2.45, \"mcnemar_p\": 0.2668, \"bootstrap_ci_95\": [-5.88, 0.98], \"bootstrap_p_sica_ge_sc\": 0.1, \"discordant_sica_wins\": 4, \"discordant_sc_wins\": 9, \"discordant_total\": 13, \"discordant_rate\": 0.064, \"multi_candidate_rate\": 0.618, \"extraction_rate\": 0.942, \"answer_extraction_rate\": 0.951, \"contradiction_rate\": 0.062, \"both_wrong\": 71, \"model\": \"LLaMA-3.1-8B-Instruct\", \"dataset\": \"FOLIO-204\", \"wall_time_min\": 131.7}, \"conclusion\": \"negative\", \"notes\": \"DEFINITIVE NEGATIVE。LLaMA-8B FOLIO 204题：SICA 60.8% vs SC 63.2%, delta=-2.45pp, McNemar p=0.2668, CI [-5.88, +0.98]。Discordant 4:9 SICA 输多赢少。exp-011 FOLIO +10pp 在 n=204 完全反转为 -2.45pp——确认为 Type I error (n=30 随机波动)。C0=61.8% 高（SICA 有操作空间），但约束改票时反而引入更多错误(9 SC wins vs 4 SICA wins)。Sweet spot hypothesis 被否定。SICA≤SC everywhere 确认。\"}, \"pilot-contrastive-prompt\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T06:18:22.559Z\", \"updated_at\": \"2026-05-17T08:02:40.938Z\", \"hypothesis\": \"Contrastive Prompt Extraction: 将 prompt 改为\\\"列出支持答案X/反对答案Y的证据\\\"能否将 discriminative ratio 从 37.2% 提升至 >70%，并使 SICA(contrastive) > SC ≥3pp——验证 answer-conditioned 约束是否解决 SICA 机制 vacuous 问题\", \"parent\": \"pilot-constraint-filtering\", \"conclusion\": \"failed\", \"notes\": \"脚本已验证可用（run_pilot_contrastive_v2.sh + pilot_contrastive_constraints.py）。修复方案：submit 时用 bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && bash /root/symb_invariant_consensus/scripts/run_pilot_contrastive_v2.sh\\\" 包裹。当前 GPU 被 exp-010-mistral-v3 占用（vLLM 87880MiB），等其完成后提交。\"}, \"exp-011-llama8b-v3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T06:15:02.161Z\", \"updated_at\": \"2026-05-17T07:59:02.260Z\", \"hypothesis\": \"Cross-family validation: LLaMA-3.1-8B-Instruct 在 D012 数据集(30PW+30FOLIO)上是否复现 SICA≈SC pattern——验证 capability trap 非 Qwen-specific（v3: 模型 shard 已修复，GPU 空闲后提交）\", \"parent\": \"sica_expanded_14b\", \"conclusion\": \"success\", \"metrics\": {\"n\": 60, \"k\": 12, \"sica_accuracy\": 0.6667, \"sc_accuracy\": 0.6, \"delta_pp\": 6.67, \"multi_candidate_rate\": 0.6167, \"extraction_rate\": 0.8556, \"answer_extraction_rate\": 0.8958, \"contradiction_rate\": 0.0527, \"problems_with_contradictions\": 43, \"truncated_traces\": 44, \"discordant_sica_wins\": 5, \"discordant_sc_wins\": 1, \"mcnemar_p\": 0.2188, \"proofwriter_sica\": 0.6333, \"proofwriter_sc\": 0.6, \"proofwriter_delta_pp\": 3.33, \"folio_sica\": 0.7, \"folio_sc\": 0.6, \"folio_delta_pp\": 10, \"model\": \"LLaMA-3.1-8B-Instruct\", \"dataset\": \"D012\", \"wall_time_min\": 66.4}, \"notes\": \"LLaMA-3.1-8B cross-family: SICA 66.7% vs SC 60.0%, +6.67pp (最大增益)。Discordant 5:1 强烈倾向 SICA。FOLIO +10pp, PW +3.33pp。McNemar p=0.22（n=60 受限）。Multi-candidate rate 61.7%（vs Qwen-14B 46%）——弱模型更多样→SICA 有更大操作空间。44 条 truncated traces（max-tokens 可能偏短），但仍有效。关键：SC baseline 60%（远低于 Qwen-14B 的 76%），验证 capability trap 的正面——模型弱时 SICA 有用。\"}, \"exp-010-mistral-v2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T03:26:42.201Z\", \"updated_at\": \"2026-05-17T06:19:34.268Z\", \"hypothesis\": \"Cross-family validation: Mistral-7B-Instruct-v0.3 在 D012 数据集(30PW+30FOLIO)上是否复现 SICA≈SC pattern——验证 capability trap 跨模型家族泛化（v2: 修复 max-model-len=8192 防 400 循环）\", \"parent\": \"sica_expanded_14b\", \"conclusion\": \"failed\", \"notes\": \"SIGTERM (exit 143) 在提交后 ~15s。根因：compound command 中 pkill -f \\\"vllm.entrypoints\\\" 可能误杀 tmux 父进程链。Director 已明确禁止 pkill 和 bash 脚本写在同一行。需要 v3：先手动清理 vLLM，再独立提交脚本。\"}, \"pilot-constraint-filtering\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T04:47:05.171Z\", \"updated_at\": \"2026-05-17T06:11:36.503Z\", \"hypothesis\": \"Constraint Consistency Filtering: 只保留在≥T条traces中重复出现的约束能否提升SICA accuracy超过SC——验证约束质量过滤是否解决capability trap\", \"parent\": \"sica_expanded_14b\", \"conclusion\": \"negative\", \"notes\": \"NEGATIVE confirmed. T=1/2/3 结果完全一致(+2.33pp=1题翻转), T≥5 SICA退化为SC。Discriminative analysis: unique constraints 中 11.5% 是 discriminative (by count), 37.2% (by weight)。但有效 flip 率仅 4/23=17.4%。根本原因：提取的约束是 domain facts (kind_charlie==True, Implies(...)) — 无论答案是什么，中间推理步骤大部分共通。约束系统未提取答案级别判别谓词。Constraint filtering 天花板极低，不是 rescue path。\", \"metrics\": {\"n\": 43, \"thresholds_tested\": [1, 2, 3, 5, 7], \"best_gap_pp\": 2.33, \"best_T\": 1, \"sica_T1\": 0.7674, \"sc\": 0.7442, \"T5_gap\": 0, \"T7_gap\": 0, \"discriminative_ratio_count\": 0.115, \"discriminative_ratio_weight\": 0.372, \"effective_flip_rate\": 0.174, \"multi_answer_problems\": 23, \"unanimous_problems\": 20, \"problems_disc_favors_different\": 4}}, \"exp-018-arc\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T03:19:51.591Z\", \"updated_at\": \"2026-05-17T05:31:46.070Z\", \"hypothesis\": \"Cross-domain validation: Qwen2.5-14B-Instruct 在 ARC-Challenge (科学多选, ABCD) 上 SICA vs SC——验证 capability trap 是否跨任务类型泛化（多选题型）\", \"parent\": \"sica_expanded_14b\", \"conclusion\": \"failed\", \"notes\": \"NameError: name 'build_generator' is not defined in eval_arc.py:142. 代码bug——函数未定义/未导入。Worker 诊断修复中。\"}, \"exp-017-strategyqa-v3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T04:17:54.931Z\", \"updated_at\": \"2026-05-17T05:29:12.136Z\", \"hypothesis\": \"Cross-domain validation: Qwen2.5-14B-Instruct 在 StrategyQA (常识推理, Yes/No) 上 SICA vs SC——验证 capability trap 是否跨任务类型泛化（v3: 修复 True/False→Yes/No 提取 bug）\", \"parent\": \"sica_expanded_14b\", \"conclusion\": \"success\", \"metrics\": {\"n\": 60, \"k\": 12, \"sica_accuracy\": 0.5667, \"sc_accuracy\": 0.5333, \"delta_pp\": 3.33, \"mcnemar_chi2\": 0.5, \"mcnemar_p\": \"n.s.\", \"bootstrap_ci_95\": [0, 8.33], \"bootstrap_p_delta_le_0\": 0.1346, \"multi_candidate_rate\": 0.1, \"contradiction_detected\": 5, \"extraction_rate_problem\": 1, \"extraction_rate_trace\": 0.704, \"discordant_sica_wins\": 2, \"discordant_sc_wins\": 0}, \"notes\": \"StrategyQA跨域验证: SICA 56.67% vs SC 53.33%, +3.33pp n.s. (p=0.13), 支持capability trap跨任务泛化; v3修复提取bug确认成功(100%问题级提取率); 2个discordant pairs均SICA胜出\"}, \"exp-017-strategyqa-v2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T03:50:55.005Z\", \"updated_at\": \"2026-05-17T04:27:27.997Z\", \"hypothesis\": \"Cross-domain validation: Qwen2.5-14B-Instruct 在 StrategyQA (常识推理, Yes/No) 上 SICA vs SC——验证 capability trap 是否跨任务类型泛化（非逻辑/数学域）\", \"parent\": \"sica_expanded_14b\", \"conclusion\": \"failed\"}, \"exp-017-strategyqa\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T03:19:50.628Z\", \"updated_at\": \"2026-05-17T03:50:54.370Z\", \"hypothesis\": \"Cross-domain validation: Qwen2.5-14B-Instruct 在 StrategyQA (常识推理, Yes/No) 上 SICA vs SC——验证 capability trap 是否跨任务类型泛化（非逻辑/数学域）\", \"parent\": \"sica_expanded_14b\", \"conclusion\": \"failed\"}, \"exp-010-mistral\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T01:04:36.900Z\", \"updated_at\": \"2026-05-17T03:37:29.439Z\", \"hypothesis\": \"Cross-family validation: Mistral-7B-Instruct-v0.3 在 D012 数据集上是否复现 SICA≈SC pattern——验证 capability trap 跨模型家族泛化\", \"parent\": \"sica_expanded_14b\", \"notes\": \"模型已确认完整下载：3 shards (4.95+5.00+4.55GB) + consolidated.safetensors (14.5GB)。排在 exp-018 之后启动。需要 Worker 准备启动脚本（参照 exp-011 模式）。\", \"conclusion\": \"failed\"}, \"exp-011-llama8b-v2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T03:19:49.625Z\", \"updated_at\": \"2026-05-17T03:24:54.392Z\", \"hypothesis\": \"Cross-family validation: LLaMA-3.1-8B-Instruct 在 D012 数据集(30PW+30FOLIO)上是否复现 SICA≈SC pattern——验证 capability trap 非 Qwen-specific (v2: 修复 GPU OOM，kill 旧 vLLM 后重跑)\", \"parent\": \"sica_expanded_14b\", \"conclusion\": \"failed\"}, \"sica_temp_diversity\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T12:14:34.555Z\", \"updated_at\": \"2026-05-17T03:21:14.807Z\", \"hypothesis\": \"不同 temperature (0.7/0.9/1.0) 下 QwQ-32B 是否产生足够的 trace 分歧以触发 MAX-SAT 矛盾检测\", \"conclusion\": \"negative\", \"metrics\": {\"temperatures_tested\": [0.7, 0.9, 1], \"problems_tested\": 3, \"problems_with_divergence\": 0, \"finding\": \"QwQ-32B produces zero answer divergence at all temperatures on MATH L4-5. Reasoning model's deterministic chain dominates sampling randomness.\", \"max_tokens_issue\": \"4096 tokens insufficient for some L5 problems (truncation)\", \"recommendation\": \"Use AIME 2024 (harder, ~79.5% acc) or non-reasoning model for trace diversity\"}, \"parent\": \"sica_smoke_5q\"}, \"sica_d012_14b\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T04:02:41.309Z\", \"updated_at\": \"2026-05-17T03:21:14.256Z\", \"conclusion\": \"success\", \"metrics\": {\"sica_accuracy\": 0.7333, \"sc_accuracy\": 0.7, \"sica_sc_gap_pp\": 3.3, \"c0_multi_candidate_rate\": 0.5333, \"c1_extraction_rate\": 1, \"c2_contradiction_problems\": 34, \"c3_gap_pp\": 3.3, \"bootstrap_p\": 0.2261, \"proofwriter_sica\": 0.6667, \"proofwriter_sc\": 0.6667, \"folio_sica\": 0.8, \"folio_sc\": 0.7333, \"total_constraints_raw\": 5849, \"total_constraints_unique\": 1735, \"maxsat_exclusion_rate\": 0.0259, \"wall_time_min\": 58.3, \"d012_verdict\": \"ALL_PASS\"}, \"hypothesis\": \"Qwen2.5-14B-Instruct 在 D012 (30PW+30FOLIO) 上 SICA pipeline 端到端有效：C0(多候选率≥20%) + C1(提取率≥80%) + C2(矛盾率≥10%) + C3(SICA>SC) 四项 sanity check 全通过\", \"parent\": \"sica_d016_c0_precheck\"}, \"sica_k_sensitivity_14b\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T05:12:03.025Z\", \"updated_at\": \"2026-05-17T03:19:48.625Z\", \"hypothesis\": \"K-ablation: K={6,8,11,12,16,20} 对 SICA 效果的影响。K=11(奇数)无平票，若 gap=0 则证明 SICA 仅靠 tiebreak 生效\", \"parent\": \"sica_expanded_14b\", \"conclusion\": \"success\", \"metrics\": {\"K6_sica\": 0.733, \"K6_sc\": 0.733, \"K6_gap_pp\": 0, \"K8_sica\": 0.733, \"K8_sc\": 0.75, \"K8_gap_pp\": -1.7, \"K11_sica\": 0.733, \"K11_sc\": 0.733, \"K11_gap_pp\": 0, \"K12_sica\": 0.7, \"K12_sc\": 0.75, \"K12_gap_pp\": -5, \"K16_sica\": 0.717, \"K16_sc\": 0.75, \"K16_gap_pp\": -3.3, \"K20_sica\": 0.7, \"K20_sc\": 0.733, \"K20_gap_pp\": -3.3, \"all_K_sica_leq_sc\": true, \"larger_K_degrades_sica\": true}, \"notes\": \"K-ablation 实际完成（EXIT_CODE=129 为 SIGHUP 假失败，同 sica_expanded_14b 模式）。结果：SICA ≤ SC for all K。K=11(奇数)验证 tiebreak 无贡献(gap=0)。K=12/16/20 SICA 退化 -3~5pp，表明更多 traces 引入更多低质量约束反而有害。直接强化 C1 (mechanism vacuous)。Artifact: art_20260517_2c1577。\"}, \"exp-011-llama8b\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T01:00:32.450Z\", \"updated_at\": \"2026-05-17T03:00:35.641Z\", \"hypothesis\": \"Cross-family validation: LLaMA-3.1-8B-Instruct 在 D012 数据集(30PW+30FOLIO)上是否复现 SICA≈SC pattern——验证 capability trap 非 Qwen-specific\", \"parent\": \"sica_expanded_14b\", \"notes\": \"Prep done by worker_prep_exp-011-llama8b_20260516T204635. Model: LLaMA-3.1-8B-Instruct (14GB, 4 shards). Script: /root/symb_invariant_consensus/scripts/run_exp011_llama8b.sh. Dataset: D012 (30 PW + 30 FOLIO = 60 题). 预估 ~25-30GB GPU, ~1-1.5h runtime. 等 sica_k_sensitivity_14b 完成后启动。\", \"conclusion\": \"failed\"}, \"exp-016-weighted-sc\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T01:01:51.841Z\", \"updated_at\": \"2026-05-17T01:02:16.162Z\", \"hypothesis\": \"加权投票变体(inverse-length/length-weighted/constraint-count)是否比 uniform SC 有统计显著优势——验证简单启发式能否替代 SICA 或超越 SC\", \"parent\": \"sica_expanded_14b\", \"conclusion\": \"success\", \"metrics\": {\"sica_accuracy\": 0.7649, \"sc_uniform_accuracy\": 0.7624, \"inv_length_accuracy\": 0.7674, \"length_weighted_accuracy\": 0.7525, \"constraint_count_accuracy\": 0.7525, \"inv_length_vs_sc_p\": 0.453, \"length_vs_sc_p\": 0.153, \"inv_length_vs_sica_p\": 0.864, \"length_vs_sica_p\": 0.066, \"n_problems\": 804, \"all_nonsignificant\": true}, \"notes\": \"exp-016 weighted SC baselines 完成。804题上所有加权变体 vs SC/SICA 均不显著(p>0.05)。Length-weighting 反而 -1pp（长 trace 略不可靠），inv-length +0.5pp 但非显著。结论：简单启发式加权不能替代也不能超越 uniform voting。支持 C1 (mechanism vacuous) — 问题不在聚合方式，而在约束质量本身。Artifacts: art_20260516_c7cc07 (report), art_20260516_7eef43 (data).\"}, \"exp-005\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T20:52:36.217Z\", \"updated_at\": \"2026-05-16T20:53:22.616Z\", \"hypothesis\": \"QwQ-32B 作为 reasoning model 展示 SICA 的 operating regime boundary: 模型过强→diversity 消失→SICA≡SC\", \"parent\": \"sica_aime30_v3\", \"metrics\": {\"qwq_aggregate_c0_nominal_pct\": 10.3, \"qwq_aggregate_c0_effective_pct\": 2.6, \"qwen14b_c0_pct\": 46, \"diversity_ratio_effective\": 17.7, \"aime_delta_pp\": 0, \"proofwriter_delta_pp\": -5.9, \"aime_n\": 22, \"proofwriter_n\": 17, \"temp_diversity_n\": 5, \"folio_n\": 2, \"total_problems\": 46, \"c0_threshold\": 20, \"qwq_below_threshold\": true}, \"conclusion\": \"negative\", \"notes\": \"exp-005 Operating Regime Analysis 完成。QwQ-32B 综合 46 题数据：effective C0=2.6%，远低于 20% 阈值。数学域 SICA≡SC (Δ=0pp, AIME 22题)，逻辑域 SICA&lt;SC (Δ=−5.9pp, PW 17题)。对比 Qwen2.5-14B C0=46% (17.7x)。直接支持 paper Claim 2 (operating regime boundary)。Artifacts: art_20260516_bf444f (data), art_20260516_d6966d (report)。\"}, \"sica_folio30\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T22:08:43.460Z\", \"updated_at\": \"2026-05-16T04:42:53.530Z\", \"hypothesis\": \"逻辑域（FOLIO）上 SICA 能否利用 FOL 标注检测跨路径矛盾并超越 SC@K=12——FOLIO 有天然 FOL 标注，是 SICA 约束提取的理想场景\", \"parent\": \"sica_aime30_v3\", \"notes\": \"废弃：QwQ-32B spec（max_tokens=12288），已被 sica_d012_14b（Qwen2.5-14B-Instruct 全量 D012 评估）覆盖。QwQ-32B 全域 C0 FAIL (3.6%)，模型已 pivot。\", \"conclusion\": \"killed\"}, \"sica_d016_c0_precheck\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T04:00:14.192Z\", \"updated_at\": \"2026-05-16T04:01:11.163Z\", \"hypothesis\": \"D016 模型 pivot C0 预检：Qwen2.5-14B-Instruct 在逻辑域是否产生足够 trace 多样性（多候选率 ≥20%）\", \"parent\": \"sica_proofwriter30_v2\", \"metrics\": {\"multi_candidate_rate_combined\": 0.46, \"multi_candidate_rate_folio\": 0.4, \"multi_candidate_rate_proofwriter\": 0.5, \"sc_accuracy_combined\": 0.73, \"sc_accuracy_folio\": 0.8, \"sc_accuracy_proofwriter\": 0.69, \"n_problems\": 26, \"n_folio\": 10, \"n_proofwriter\": 16, \"K\": 6, \"T\": 0.7, \"total_time_s\": 280, \"c0_gate\": \"PASS (46% >= 20%)\", \"model\": \"Qwen2.5-14B-Instruct\", \"vllm_gpu_mem_gib\": 27.6, \"smoke_test\": \"2 problems end-to-end OK, constraints 21-26 per problem\"}, \"conclusion\": \"success\", \"notes\": \"C0 PASS: Qwen2.5-14B-Instruct 多候选率 46% (FOLIO 40%, ProofWriter 50%)，远超 20% 阈值。对比 QwQ-32B 全域 3.6%，提升 12.8x。SC accuracy 73% (FOLIO 80%, PW 69%)。Smoke test 2题 SICA pipeline 端到端通过。vLLM PID 174291, 27.6 GiB, max-model-len=8192。Report: art_20260516_e2774d。\"}, \"sica_proofwriter30_v2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T22:19:01.325Z\", \"updated_at\": \"2026-05-16T01:38:43.002Z\", \"hypothesis\": \"逻辑域（ProofWriter D5）上 SICA 能否检测跨路径 FOL 约束矛盾并超越 SC@K=12（v2: max_tokens=12288 修复）\", \"parent\": \"sica_proofwriter30\", \"notes\": \"16/30 killed (Director 指令)。D012 四项全 FAIL。MaxSAT 根因诊断结论：三层问题叠加——(1) 约束提取失败 54.4%，QwQ-32B 收到 extraction prompt 后重新推理而非输出 JSON，3/4 多候选题提取为零；(2) 一致投票=一致约束，14/17 题 12/12 同一答案，约束天然不矛盾（正确行为非 bug）；(3) 评分偏差，唯一 SICA≠SC 的题 498_Q8，SICA 给少数派 38 分 > 多数派 27 分，因提取失败非随机。MaxSAT 求解器本身无 bug（注入测试 6/6 通过）。推荐修复：L3 自动注入 answer==trace_answer 约束使不同答案 trace 必有冲突；L1 提取用 system prompt 强制 JSON-only。\", \"conclusion\": \"killed\"}, \"sica_proofwriter30\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T22:08:42.831Z\", \"updated_at\": \"2026-05-15T22:18:19.326Z\", \"hypothesis\": \"逻辑域（ProofWriter D5）上 SICA 能否检测跨路径 FOL 约束矛盾并超越 SC@K=12——验证 SICA 在逻辑推理域的有效性\", \"parent\": \"sica_aime30_v3\", \"conclusion\": \"failed\", \"notes\": \"配置错误导致完全失败。--max-tokens 16384 等于 vLLM 的 --max-model-len 16384，prompt 输入空间为 0，所有 30 题从第 1 题起全部 400 Bad Request。没有生成任何 trace，没有提取约束，没有投票。4 分钟内跑完（全是 retry 耗时）。无法评估 sanity check 标准。需要用 --max-tokens 12288 或更小值重跑（AIME 实验用的 10240 正常工作）。\", \"metrics\": {\"sica_accuracy\": \"0/30 (0.0%)\", \"sc_accuracy\": \"0/30 (0.0%)\", \"sica_sc_gap_pp\": 0, \"total_wall_time_s\": 238.9, \"total_wall_time_min\": 4, \"avg_time_per_problem_s\": 8, \"traces_generated\": 0, \"constraints_extracted\": 0, \"traces_with_constraints\": 0, \"unique_constraints\": 0, \"maxsat_satisfied\": 0, \"maxsat_excluded\": 0, \"multi_candidate_rate\": \"N/A (no traces generated)\", \"vote_diversity\": \"N/A\", \"z3_errors\": 0, \"z3_timeouts\": 0, \"problems_with_contradiction\": 0, \"problems_with_votes\": 0, \"failure_mode\": \"ALL_400_BAD_REQUEST\", \"failure_count\": \"30/30\", \"root_cause\": \"max_tokens=16384 equals max_model_len=16384, leaving 0 tokens for prompt input. Every API call returns 400.\"}}, \"sica_aime30_v3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T16:13:04.296Z\", \"updated_at\": \"2026-05-15T22:07:55.967Z\", \"hypothesis\": \"AIME 2024 上 SICA 能否检测跨路径矛盾并超越 SC@K=12（v3: timeout=1800s, 从v2 P5恢复继续）\", \"parent\": \"sica_aime30_v2\", \"notes\": \"v3 killed at 22/30 (PID 129992, 6h11m). Vote diversity analysis: multi-candidate rate = 0.0%, all valid problems have exactly 1 candidate. SICA≡SC confirmed structural. 6/22 problems with 0 votes (extraction failure). 数学域结论锁定，转逻辑域。\", \"metrics\": {\"progress\": \"22/30\", \"sica_accuracy_interim\": \"16/22 (72.7%)\", \"sc_accuracy_interim\": \"16/22 (72.7%)\", \"sica_sc_gap_pp\": 0, \"avg_time_per_problem_s\": 645.9, \"runtime_h\": 5.9, \"remaining_problems\": 8, \"vote_diversity_analysis\": {\"valid_problems\": 16, \"total_problems\": 22, \"multi_candidate_rate\": 0, \"zero_vote_problems\": 6, \"zero_vote_indices\": [1, 7, 8, 10, 13, 14], \"constraints_extracted\": \"19/22\", \"exclusion_rate\": 0.387, \"conclusion\": \"All 16 valid problems have exactly 1 candidate answer. SICA≡SC structurally. MaxSAT exclusion operates but cannot change final selection with only 1 candidate.\"}, \"process_status\": \"gone (cron miss 1/5)\"}, \"conclusion\": \"killed\"}, \"sica_aime30_v2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T13:24:26.526Z\", \"updated_at\": \"2026-05-15T16:11:32.132Z\", \"hypothesis\": \"AIME 2024 上 SICA 能否检测跨路径矛盾并超越 SC@K=12（v2: 修复 timeout/hang bug 后重跑）\", \"conclusion\": \"killed\", \"metrics\": {\"progress\": \"4/30\", \"sica_accuracy_interim\": \"3/4 (75%)\", \"sc_accuracy_interim\": \"3/4 (75%)\", \"avg_time_per_problem_s\": 557, \"p2_z3_error\": \"Z3Exception on z3_maxsat.py:163, 0 constraints extracted\", \"p5_vllm_stuck\": \"vLLM timeout since ~22:11, retried multiple rounds\", \"issue\": \"vLLM service likely crashed or OOM at Problem 5\", \"analysis_contradiction_rate_aime\": \"50% (2/4)\", \"analysis_contradiction_rate_math\": \"20% (1/5)\", \"analysis_unique_constraints_per_problem_aime\": 18.7, \"analysis_exclusion_rate\": \"10.7%\", \"analysis_sica_sc_agreement\": \"9/9 (100%)\", \"analysis_signal\": \"weak positive - mechanism works but SC too unanimous to flip\", \"analysis_p2_failure\": \"0 constraints, 0 votes - answer extraction failure\"}, \"notes\": \"失败原因: Problem 5 (aime2024_II_05, 凸六边形几何题) 12条并发trace在单GPU上竞争资源→每条trace吞吐极低→客户端~600s超时后重试→旧请求仍在vLLM running→恶性循环卡死~1h47min | 已有成果: 4/30题完成 SICA 3/4=75% SC 3/4=75%, P2有Z3Exception(0 constraints extracted) | vLLM本身健康(test request <1s) | 建议: 降低并发k或分批处理trace(如4条/批), 增大client timeout, kill stuck requests后重启\"}, \"sica_aime30_t07\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T12:38:16.330Z\", \"updated_at\": \"2026-05-15T13:11:37.911Z\", \"hypothesis\": \"AIME 2024（QwQ-32B 弱项，~79.5% acc）上 SICA 能否检测更多跨路径矛盾并超越 SC@K=12——验证\\\"SICA 价值随问题难度递增\\\"假设\", \"conclusion\": \"killed\"}, \"mvp_math50_t07\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T12:16:29.416Z\", \"updated_at\": \"2026-05-15T12:21:37.283Z\", \"hypothesis\": \"SICA MVP: 50题MATH-500上跨路径MAX-SAT约束共识能否检测矛盾并超越SC@K=12\", \"conclusion\": \"killed\"}, \"sica_smoke_5q\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T11:38:43.996Z\", \"updated_at\": \"2026-05-15T11:39:13.456Z\", \"hypothesis\": \"SICA smoke test: 验证端到端 pipeline 可行性（5题 MATH-500, K=12, QwQ-32B）\", \"conclusion\": \"success\", \"metrics\": {\"sica_accuracy\": 0.8, \"sc_accuracy\": 0.8, \"extraction_rate\": 1, \"problems_with_contradictions\": 1, \"total_problems\": 5, \"total_time_s\": 3505, \"avg_time_per_problem_s\": 701, \"per_problem\": [{\"id\": \"algebra/2470\", \"level\": 1, \"sica_correct\": true, \"sc_correct\": true, \"constraints\": 27, \"unique\": 9, \"excluded\": 0}, {\"id\": \"prealgebra/65\", \"level\": 2, \"sica_correct\": true, \"sc_correct\": true, \"constraints\": 26, \"unique\": 2, \"excluded\": 0}, {\"id\": \"number_theory/847\", \"level\": 3, \"sica_correct\": true, \"sc_correct\": true, \"constraints\": 21, \"unique\": 11, \"excluded\": 0, \"note\": \"14 JSON parse failures, 1693s\"}, {\"id\": \"precalculus/1199\", \"level\": 4, \"sica_correct\": false, \"sc_correct\": false, \"constraints\": 35, \"unique\": 6, \"excluded\": 0, \"note\": \"graph-reading problem, model cannot see image\"}, {\"id\": \"algebra/2277\", \"level\": 5, \"sica_correct\": true, \"sc_correct\": true, \"constraints\": 60, \"unique\": 6, \"satisfied\": 3, \"excluded\": 3}]}}, \"smoke-test-5q\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-15T11:22:09.665Z\", \"updated_at\": \"2026-05-15T11:22:09.666Z\", \"conclusion\": \"failed\"}, \"crd_folio_main\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T09:35:42.037Z\", \"updated_at\": \"2026-05-15T09:36:24.832Z\", \"conclusion\": \"success\", \"hypothesis\": \"CRD: 双表征(FOL+SymPy)分歧检测+定向修复能提升逻辑推理准确率（非SICA方法）\", \"metrics\": {\"divergence_rate\": 0.422, \"diagnosis_rate\": 0.872, \"error_types\": 4, \"directed_advantage_pp\": 4.7, \"directed_p_value\": 0.63, \"localization_accuracy\": 0.946, \"fol_accuracy\": 0.789, \"code_accuracy\": 0.598, \"oracle_accuracy\": 0.878, \"pipeline_accuracy\": 0.814, \"baseline_accuracy\": 0.74, \"cost_multiplier\": 5.76, \"dataset\": \"FOLIO\", \"n\": 204}}}, \"count\": 139, \"total\": 139, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5387}}"
    }
  },
  "sourceToolAssistantUUID": "51caf076-1012-4d3d-b45e-9a3243a00edd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora"
}
```

</details>

---


### Runtime record

_source line 8817_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[服务器重启后首条消息] 当前日期: 2026-05-20。服务器刚重启，项目状态可能已更新。不要依赖对话历史中的状态信息，以 registry 当前值为准。  **用户消息：** [Director 指令] ## 写作任务：EMNLP 2026 ARR May 25 — Full Draft 更新  **DDL**: May 25, 2026（5 天） **模式**: Full Draft 更新…",
  "leafUuid": "932e0c2c-46c4-47cb-8e06-caea48468cba",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1"
}
```

---


### Runtime record

_source line 8818_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise paper results with oracle FOLIO constraint experiments",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1"
}
```

---


### Assistant

_source line 8819 · 2026-05-20T09:36:03.402Z_

<details><summary>Logged reasoning block</summary>

```text
The registry is very large. Let me read it in chunks to understand the full experiment list, particularly focusing on the new experiments (D082+ Symbolic Confirmation Bias, Process-κ, and the 25+ methods).

But actually, for the writing plan update, I don't need to read every single registry entry. I have the paper_framing.md which summarizes the key data. Let me focus on understanding:

1. What's NEW vs what already exists in the paper:
   - NEW: Claims 7 (Symbolic Confirmation Bias) and 8 (Process-κ) 
   - NEW: 25+ methods (up from 12)
   - EXISTING: Claims 1-6 are already in the paper
   
2. What sections need major rewriting vs patching

I should check the current tex files to see where the gaps are. I have analysis.tex and discussion.tex from earlier, but let me review the introduction and methods sections too, then scan the registry selectively for just the new experiments starting from D082.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "932e0c2c-46c4-47cb-8e06-caea48468cba",
  "isSidechain": false,
  "requestId": "req_011CbDbQFJccHf3R28y8NhJX",
  "type": "assistant",
  "uuid": "a568e0c0-4c71-4e40-933a-996f6564f36c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GMpr7RQ2sQkc4LhzdspSxb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 28687,
      "cache_read_input_tokens": 135126,
      "output_tokens": 971,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 28687,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 971,
          "cache_read_input_tokens": 135126,
          "cache_creation_input_tokens": 28687,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 28687
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

_source line 8820 · 2026-05-20T09:36:03.425Z_

Registry 太大，查关键新实验数据。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a568e0c0-4c71-4e40-933a-996f6564f36c",
  "isSidechain": false,
  "requestId": "req_011CbDbQFJccHf3R28y8NhJX",
  "type": "assistant",
  "uuid": "dcd11761-5e7f-4698-b317-ed0b078137e7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GMpr7RQ2sQkc4LhzdspSxb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 28687,
      "cache_read_input_tokens": 135126,
      "output_tokens": 971,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 28687,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 971,
          "cache_read_input_tokens": 135126,
          "cache_creation_input_tokens": 28687,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 28687
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

_source line 8821 · 2026-05-20T09:36:10.583Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01G6AEtAnqmmk4yy5g4nfWkJ`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-3-projects-symb-invariant-consensus--claude-sessions-paper-agent-644edc69/6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1/tool-results/mcp-agent-ml-research-read_registry-1779269749758.txt | python3 -c \"\nimport json, sys\ndata = json.loads(sys.stdin.read())\nreg = json.loads(data['result'])\nexps = reg.get('data', reg) if isinstance(reg, dict) else reg\nif isinstance(exps, dict) and 'experiments' in exps:\n    exps = exps['experiments']\nelif isinstance(exps, dict):\n    exps = list(exps.values())\n\n# Find experiments related to confirmation bias, process-kappa, blind FOL, and new methods\nkeywords = ['confirm', 'bias', 'process', 'blind', 'prove', 'cegis', 'deepconf', 'perturb', 'min-unsat', 'minunsat', 'kappa-aware', 'z3_filter', 'bootstrap', 'abstention', 'cross-model']\nfor exp in exps:\n    exp_id = exp.get('exp_id', exp.get('id', ''))\n    desc = str(exp.get('description', '')) + str(exp.get('name', '')) + str(exp.get('hypothesis', ''))\n    status = exp.get('status', '')\n    conclusion = str(exp.get('conclusion', ''))[:100]\n    metrics = str(exp.get('key_metrics', exp.get('metrics', '')))[:100]\n    if any(k in desc.lower() or k in exp_id.lower() for k in keywords) or int(exp_id.replace('exp-','').replace('comp-','').replace('a','').replace('b','').replace('c','').replace('d','')) > 80 if exp_id.startswith('exp-') and exp_id.replace('exp-','').replace('a','').replace('b','').replace('c','').replace('d','').isdigit() else False:\n        print(f'{exp_id} | {status} | {desc[:80]} | {conclusion} | {metrics}')\n\" 2>&1 | head -40",
  "description": "Extract new experiment entries from registry"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dcd11761-5e7f-4698-b317-ed0b078137e7",
  "isSidechain": false,
  "requestId": "req_011CbDbQFJccHf3R28y8NhJX",
  "type": "assistant",
  "uuid": "0fa081a7-34cf-4a9b-be0b-e965c6af2df8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GMpr7RQ2sQkc4LhzdspSxb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 28687,
      "cache_read_input_tokens": 135126,
      "output_tokens": 971,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 28687,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 971,
          "cache_read_input_tokens": 135126,
          "cache_creation_input_tokens": 28687,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 28687
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

_source line 8822 · 2026-05-20T09:36:10.964Z_

<details><summary>↩ Tool result · `toolu_01G6AEtAnqmmk4yy5g4nfWkJ`</summary>

```text
Traceback (most recent call last):
  File "&lt;string>", line 14, in &lt;module>
    exp_id = exp.get('exp_id', exp.get('id', ''))
             ^^^^^^^
AttributeError: 'str' object has no attribute 'get'
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0fa081a7-34cf-4a9b-be0b-e965c6af2df8",
  "isSidechain": false,
  "promptId": "3f50ba00-7d30-45ec-b450-7010d531c858",
  "type": "user",
  "uuid": "9d260a69-001a-4366-aade-e4e2fcccd3f5",
  "toolUseResult": {
    "stdout": "Traceback (most recent call last):\n  File \"&lt;string>\", line 14, in &lt;module>\n    exp_id = exp.get('exp_id', exp.get('id', ''))\n             ^^^^^^^\nAttributeError: 'str' object has no attribute 'get'",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "0fa081a7-34cf-4a9b-be0b-e965c6af2df8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora"
}
```

</details>

---


### Tool call

_source line 8823 · 2026-05-20T09:36:17.575Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01P1z7N6xphPPzsaC8TA51sj`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-3-projects-symb-invariant_consensus--claude-sessions-paper-agent-644edc69/6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1/tool-results/mcp-agent-ml-research-read_registry-1779269749758.txt 2>/dev/null | python3 -c \"\nimport json, sys\nraw = sys.stdin.read()\ndata = json.loads(raw)\nresult = json.loads(data['result']) if isinstance(data.get('result'), str) else data.get('result', data)\n# Explore structure\nif isinstance(result, dict):\n    print('Keys:', list(result.keys())[:10])\n    for k, v in list(result.items())[:2]:\n        print(f'{k}: {type(v).__name__}', str(v)[:200] if not isinstance(v, (dict,list)) else f'len={len(v)}')\nelif isinstance(result, list):\n    print(f'List of {len(result)}')\n    if result:\n        print(type(result[0]).__name__, str(result[0])[:300])\n\" 2>&1",
  "description": "Explore registry structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9d260a69-001a-4366-aade-e4e2fcccd3f5",
  "isSidechain": false,
  "requestId": "req_011CbDbRosiP4iC4H1Z5W56t",
  "type": "assistant",
  "uuid": "d85564ef-7420-4222-a409-006a751d5724",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CArnejRjNSXAJJhimANCri",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1049,
      "cache_read_input_tokens": 163813,
      "output_tokens": 389,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1049,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 389,
          "cache_read_input_tokens": 163813,
          "cache_creation_input_tokens": 1049,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1049
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

_source line 8824 · 2026-05-20T09:36:17.812Z_

<details><summary>↩ Tool result · reported error · `toolu_01P1z7N6xphPPzsaC8TA51sj`</summary>

```text
Exit code 1
Traceback (most recent call last):
  File "&lt;string>", line 4, in &lt;module>
    data = json.loads(raw)
  File "/usr/lib/python3.14/json/__init__.py", line 352, in loads
    return _default_decoder.decode(s)
           ~~~~~~~~~~~~~~~~~~~~~~~^^^
  File "/usr/lib/python3.14/json/decoder.py", line 345, in decode
    obj, end = self.raw_decode(s, idx=_w(s, 0).end())
               ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.14/json/decoder.py", line 363, in raw_decode
    raise JSONDecodeError("Expecting value", s, err.value) from None
json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d85564ef-7420-4222-a409-006a751d5724",
  "isSidechain": false,
  "promptId": "3f50ba00-7d30-45ec-b450-7010d531c858",
  "type": "user",
  "uuid": "a1dad59c-b15b-48c4-b085-6470e7141046",
  "toolUseResult": "Error: Exit code 1\nTraceback (most recent call last):\n  File \"&lt;string>\", line 4, in &lt;module>\n    data = json.loads(raw)\n  File \"/usr/lib/python3.14/json/__init__.py\", line 352, in loads\n    return _default_decoder.decode(s)\n           ~~~~~~~~~~~~~~~~~~~~~~~^^^\n  File \"/usr/lib/python3.14/json/decoder.py\", line 345, in decode\n    obj, end = self.raw_decode(s, idx=_w(s, 0).end())\n               ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/usr/lib/python3.14/json/decoder.py\", line 363, in raw_decode\n    raise JSONDecodeError(\"Expecting value\", s, err.value) from None\njson.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)",
  "sourceToolAssistantUUID": "d85564ef-7420-4222-a409-006a751d5724",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora"
}
```

</details>

---


### Tool call

_source line 8825 · 2026-05-20T09:36:21.537Z_

<details open><summary>🔧 Tool call — Bash · `toolu_0134Xdz3zPGnArfyRiK3JYt2`</summary>

```json
{
  "command": "ls -la /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea*gen*0513*3*symb*invariant*/*/tool-results/mcp-agent-ml-research-read_registry*.txt 2>/dev/null | head -5",
  "description": "Find registry results file"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a1dad59c-b15b-48c4-b085-6470e7141046",
  "isSidechain": false,
  "requestId": "req_011CbDbSKBLDV8T6DqYbyAkE",
  "type": "assistant",
  "uuid": "069fb5fa-04da-497f-84d8-58abc54e2e96",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015y5K1rUpZfdVGtmS2D7xyP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 624,
      "cache_read_input_tokens": 164862,
      "output_tokens": 141,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 624,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 141,
          "cache_read_input_tokens": 164862,
          "cache_creation_input_tokens": 624,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 624
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

_source line 8826 · 2026-05-20T09:36:21.597Z_

<details><summary>↩ Tool result · `toolu_0134Xdz3zPGnArfyRiK3JYt2`</summary>

```text
-rw-r--r-- 1 ubuntu ubuntu  93597 May 19 13:51 /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-3-projects-symb-invariant-consensus--claude-sessions-agent-47e5a40d/284700f5-3ec3-4517-aefd-608b02aaab75/tool-results/mcp-agent-ml-research-read_registry-1779198675059.txt
-rw-r--r-- 1 ubuntu ubuntu  99048 May 19 17:41 /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-3-projects-symb-invariant-consensus--claude-sessions-agent-47e5a40d/34d21c8b-30c6-4d2d-af7e-4249ae70ee7b/tool-results/mcp-agent-ml-research-read_registry-1779212473949.txt
-rw-r--r-- 1 ubuntu ubuntu 114188 May 20 08:51 /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-3-projects-symb-invariant-consensus--claude-sessions-agent-47e5a40d/34d21c8b-30c6-4d2d-af7e-4249ae70ee7b/tool-results/mcp-agent-ml-research-read_registry-1779267081565.txt
-rw-r--r-- 1 ubuntu ubuntu  91685 May 19 11:44 /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-3-projects-symb-invariant-consensus--claude-sessions-agent-d95f4807/1cceb03b-8d30-4289-938f-2d9ddab53b40/tool-results/mcp-agent-ml-research-read_registry-1779191070042.txt
-rw-r--r-- 1 ubuntu ubuntu 128603 May 18 19:19 /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-3-projects-symb-invariant-consensus--claude-sessions-agent-d95f4807/2ccf886d-12a4-4624-94af-fb6ea3ea41e0/tool-results/mcp-agent-ml-research-read_registry-1779131977191.txt
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "069fb5fa-04da-497f-84d8-58abc54e2e96",
  "isSidechain": false,
  "promptId": "3f50ba00-7d30-45ec-b450-7010d531c858",
  "type": "user",
  "uuid": "f24e00ba-4a2b-4b2f-81e7-11f19c7daf58",
  "toolUseResult": {
    "stdout": "-rw-r--r-- 1 ubuntu ubuntu  93597 May 19 13:51 /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-3-projects-symb-invariant-consensus--claude-sessions-agent-47e5a40d/284700f5-3ec3-4517-aefd-608b02aaab75/tool-results/mcp-agent-ml-research-read_registry-1779198675059.txt\n-rw-r--r-- 1 ubuntu ubuntu  99048 May 19 17:41 /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-3-projects-symb-invariant-consensus--claude-sessions-agent-47e5a40d/34d21c8b-30c6-4d2d-af7e-4249ae70ee7b/tool-results/mcp-agent-ml-research-read_registry-1779212473949.txt\n-rw-r--r-- 1 ubuntu ubuntu 114188 May 20 08:51 /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-3-projects-symb-invariant-consensus--claude-sessions-agent-47e5a40d/34d21c8b-30c6-4d2d-af7e-4249ae70ee7b/tool-results/mcp-agent-ml-research-read_registry-1779267081565.txt\n-rw-r--r-- 1 ubuntu ubuntu  91685 May 19 11:44 /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-3-projects-symb-invariant-consensus--claude-sessions-agent-d95f4807/1cceb03b-8d30-4289-938f-2d9ddab53b40/tool-results/mcp-agent-ml-research-read_registry-1779191070042.txt\n-rw-r--r-- 1 ubuntu ubuntu 128603 May 18 19:19 /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-3-projects-symb-invariant-consensus--claude-sessions-agent-d95f4807/2ccf886d-12a4-4624-94af-fb6ea3ea41e0/tool-results/mcp-agent-ml-research-read_registry-1779131977191.txt",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "069fb5fa-04da-497f-84d8-58abc54e2e96",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora"
}
```

</details>

---


### Tool call

_source line 8827 · 2026-05-20T09:36:26.056Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01P643d6ZA48DNnPocwkc6ho`</summary>

```json
{
  "project": "symb_invariant_consensus",
  "limit": 0,
  "fields": [
    "exp_id",
    "status",
    "description",
    "conclusion"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f24e00ba-4a2b-4b2f-81e7-11f19c7daf58",
  "isSidechain": false,
  "requestId": "req_011CbDbSbLRfJ4NZUbE6UjcF",
  "type": "assistant",
  "uuid": "c191a825-25f2-41b7-8a9d-f98c1397eeb3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DQ8TF94rkBzis432iXaSdU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 805,
      "cache_read_input_tokens": 165486,
      "output_tokens": 115,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 805,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 115,
          "cache_read_input_tokens": 165486,
          "cache_creation_input_tokens": 805,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 805
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

_source line 8828 · 2026-05-20T09:36:26.439Z_

<details><summary>↩ Tool result · `toolu_01P643d6ZA48DNnPocwkc6ho`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {\"exp-wave3-dir-i-z3-filter\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-wave3-dir-j-bootstrap\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-cross-model-phase2\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-direction-d-cegis\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-confirmation-bias\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"exp-cross-model-phase1\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"exp-direction-e-abstention\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"exp-wild6-kappa-aware-sc\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-wild1-max-unsat\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-wild4-process-kappa\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-direction-a-prove\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-direction-b-deepconf\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-wild3-perturbation\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-wild2-ascii\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-084-debate-mistral-logiqa-seed123\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-082-contrastive-mistral-folio-seed123\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-081-debate-mistral-folio-seed123\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-085-contrastive-mistral-logiqa-seed123\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-013-constraint-ablation\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"exp-075b-contrastive-mistral-folio\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-080-contrastive-mistral-logiqa200\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-078-debate-mistral-logiqa200\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-078\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-083-icg-mistral-logiqa-seed123\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-074d-icg-mistral-folio-seed456\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-077-kappa-generalization\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-077\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-075b\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-074c-icg-mistral-folio-seed123\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-076-debate-mistral-folio\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-079-icg-mistral-logiqa200\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-072b-llama8b-logiqa200\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-074-icg-mistral-folio\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-073b-qwen7b-logiqa200-seed456\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"exp-073-qwen7b-logiqa200-seed456\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"exp-072-llama8b-logiqa200\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"exp-064-deepseek-r1-qwen3-8b-folio204\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"exp-075-contrastive-mistral-folio\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"exp-077-generalization-kappa\": {\"status\": \"PREPARING\"}, \"exp-071-qwen7b-logiqa200-seed123\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-048-llama8b-pw600\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-053-mistral-folio204-seed456\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"exp-052-mistral-folio204-seed123\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"exp-069-llama8b-logiqa200\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-065-qwen7b-pw600\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-062-gemma27b-folio204\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-069-mistral-logiqa200\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-070-qwen7b-logiqa200\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"exp-068-qwen3-logiqa200\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-064\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"exp-067-mistral-folio-seed789\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"exp-063-llama8b-folio204-16639\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-063-llama8b-folio204\": {\"status\": \"PREPARING\", \"conclusion\": \"negative\"}, \"exp-061-qwen7b-folio204\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-059-cross-qwen3-extractor\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"exp-063\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-040-qwen3-pw600-16639\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-060-cross-qwen25-14b-extractor\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-057-mistral-folio204-t03\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-034\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-039-14b-pw600-16639\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-058-mistral-folio204-t05\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-051-mistral-k-sensitivity\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"exp-055-multitemp-mistral-folio\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-028b-qwen3-thinking-folio204\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"exp-052\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"exp-054-mistral-folio204-t10\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-046-mistral-pw600\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-053\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-050b-mistral-icl-oracle\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-050-mistral-icl-oracle-folio199\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"exp-049b-mistral-logiqa200\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-044b-icl-oracle\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-049-mistral-logiqa200\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"exp-041-14b-folio204-16639\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-045b-backward-verify\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"exp-045-backward-verification\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-038-14b-logiqa200-16639\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-033\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"exp-042b-premise-formal\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"exp-044-icl-oracle\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"exp-035\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-036b-cross-trace-unsat\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-042-premise-formalization\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"exp-043-consistency-filtering\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-036-z3-feedback-folio204\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-028-qwen3-14b-thinking\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"exp-033-qwen3-pw600-nonthinking\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"exp-004-qwen7b-rerun\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"exp-007-qwen72b-awq\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"exp-027-qwen3-14b-non-thinking\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"exp-030-crossmodel-mistral-folio204\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-031-oracle-folio-regen\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"exp-029-contrastive-folio204\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-026-folio204-trace-regen\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"exp-023-discriminative-rate\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"exp-022-oracle-proofwriter\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"temperature-ablation-t07\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"sica_constraint_ablation_013\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"exp-004-qwen7b\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"temperature-ablation-t10\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-012-gsm8k-pilot\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-021-oracle-folio\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"temperature-ablation-t05\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"temperature-ablation-t03\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-014-deepseek-r1-7b\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-010-mistral-v3\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"sica_expanded_14b\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"exp-019-llama8b-strategyqa-200\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-018-arc-v2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"exp-009-overhead-analysis\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"exp-020-llama8b-folio-204\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"pilot-contrastive-prompt\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"exp-011-llama8b-v3\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"exp-010-mistral-v2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"pilot-constraint-filtering\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-018-arc\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"exp-017-strategyqa-v3\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"exp-017-strategyqa-v2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"exp-017-strategyqa\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"exp-010-mistral\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"exp-011-llama8b-v2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"sica_temp_diversity\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"sica_d012_14b\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"sica_k_sensitivity_14b\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"exp-011-llama8b\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"exp-016-weighted-sc\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"exp-005\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"sica_folio30\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"sica_d016_c0_precheck\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"sica_proofwriter30_v2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"sica_proofwriter30\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"sica_aime30_v3\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"sica_aime30_v2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"sica_aime30_t07\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"mvp_math50_t07\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"sica_smoke_5q\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"smoke-test-5q\": {\"status\": \"PREPARING\", \"conclusion\": \"failed\"}, \"crd_folio_main\": {\"status\": \"DONE\", \"conclusion\": \"success\"}}, \"count\": 139, \"total\": 139, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3713}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c191a825-25f2-41b7-8a9d-f98c1397eeb3",
  "isSidechain": false,
  "promptId": "3f50ba00-7d30-45ec-b450-7010d531c858",
  "type": "user",
  "uuid": "44bef146-e640-45b1-ab88-3e23a6663cdc",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {\\\"exp-wave3-dir-i-z3-filter\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-wave3-dir-j-bootstrap\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-cross-model-phase2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-direction-d-cegis\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-confirmation-bias\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"exp-cross-model-phase1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"exp-direction-e-abstention\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"exp-wild6-kappa-aware-sc\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-wild1-max-unsat\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-wild4-process-kappa\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-direction-a-prove\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-direction-b-deepconf\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-wild3-perturbation\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-wild2-ascii\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-084-debate-mistral-logiqa-seed123\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-082-contrastive-mistral-folio-seed123\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-081-debate-mistral-folio-seed123\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-085-contrastive-mistral-logiqa-seed123\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-013-constraint-ablation\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"exp-075b-contrastive-mistral-folio\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-080-contrastive-mistral-logiqa200\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-078-debate-mistral-logiqa200\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-078\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-083-icg-mistral-logiqa-seed123\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-074d-icg-mistral-folio-seed456\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-077-kappa-generalization\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-077\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-075b\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-074c-icg-mistral-folio-seed123\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-076-debate-mistral-folio\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-079-icg-mistral-logiqa200\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-072b-llama8b-logiqa200\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-074-icg-mistral-folio\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-073b-qwen7b-logiqa200-seed456\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"exp-073-qwen7b-logiqa200-seed456\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"exp-072-llama8b-logiqa200\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"exp-064-deepseek-r1-qwen3-8b-folio204\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"exp-075-contrastive-mistral-folio\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"exp-077-generalization-kappa\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"exp-071-qwen7b-logiqa200-seed123\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-048-llama8b-pw600\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-053-mistral-folio204-seed456\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"exp-052-mistral-folio204-seed123\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"exp-069-llama8b-logiqa200\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-065-qwen7b-pw600\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-062-gemma27b-folio204\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-069-mistral-logiqa200\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-070-qwen7b-logiqa200\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"exp-068-qwen3-logiqa200\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-064\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"exp-067-mistral-folio-seed789\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"exp-063-llama8b-folio204-16639\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-063-llama8b-folio204\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-061-qwen7b-folio204\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-059-cross-qwen3-extractor\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"exp-063\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-040-qwen3-pw600-16639\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-060-cross-qwen25-14b-extractor\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-057-mistral-folio204-t03\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-034\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-039-14b-pw600-16639\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-058-mistral-folio204-t05\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-051-mistral-k-sensitivity\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"exp-055-multitemp-mistral-folio\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-028b-qwen3-thinking-folio204\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"exp-052\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"exp-054-mistral-folio204-t10\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-046-mistral-pw600\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-053\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-050b-mistral-icl-oracle\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-050-mistral-icl-oracle-folio199\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"exp-049b-mistral-logiqa200\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-044b-icl-oracle\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-049-mistral-logiqa200\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"exp-041-14b-folio204-16639\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-045b-backward-verify\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"exp-045-backward-verification\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-038-14b-logiqa200-16639\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-033\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"exp-042b-premise-formal\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"exp-044-icl-oracle\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"exp-035\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-036b-cross-trace-unsat\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-042-premise-formalization\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"exp-043-consistency-filtering\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-036-z3-feedback-folio204\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-028-qwen3-14b-thinking\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"exp-033-qwen3-pw600-nonthinking\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"exp-004-qwen7b-rerun\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"exp-007-qwen72b-awq\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"exp-027-qwen3-14b-non-thinking\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"exp-030-crossmodel-mistral-folio204\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-031-oracle-folio-regen\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"exp-029-contrastive-folio204\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-026-folio204-trace-regen\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"exp-023-discriminative-rate\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"exp-022-oracle-proofwriter\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"temperature-ablation-t07\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"sica_constraint_ablation_013\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"exp-004-qwen7b\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"temperature-ablation-t10\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-012-gsm8k-pilot\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-021-oracle-folio\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"temperature-ablation-t05\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"temperature-ablation-t03\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-014-deepseek-r1-7b\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-010-mistral-v3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"sica_expanded_14b\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"exp-019-llama8b-strategyqa-200\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-018-arc-v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"exp-009-overhead-analysis\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"exp-020-llama8b-folio-204\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"pilot-contrastive-prompt\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"exp-011-llama8b-v3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"exp-010-mistral-v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"pilot-constraint-filtering\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-018-arc\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"exp-017-strategyqa-v3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"exp-017-strategyqa-v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"exp-017-strategyqa\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"exp-010-mistral\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"exp-011-llama8b-v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"sica_temp_diversity\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"sica_d012_14b\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"sica_k_sensitivity_14b\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"exp-011-llama8b\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"exp-016-weighted-sc\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"exp-005\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"sica_folio30\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"sica_d016_c0_precheck\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"sica_proofwriter30_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"sica_proofwriter30\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"sica_aime30_v3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"sica_aime30_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"sica_aime30_t07\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"mvp_math50_t07\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"sica_smoke_5q\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"smoke-test-5q\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"crd_folio_main\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}}, \\\"count\\\": 139, \\\"total\\\": 139, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.3713}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"exp-wave3-dir-i-z3-filter\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-wave3-dir-j-bootstrap\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-cross-model-phase2\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-direction-d-cegis\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-confirmation-bias\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"exp-cross-model-phase1\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"exp-direction-e-abstention\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"exp-wild6-kappa-aware-sc\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-wild1-max-unsat\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-wild4-process-kappa\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-direction-a-prove\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-direction-b-deepconf\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-wild3-perturbation\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-wild2-ascii\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-084-debate-mistral-logiqa-seed123\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-082-contrastive-mistral-folio-seed123\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-081-debate-mistral-folio-seed123\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-085-contrastive-mistral-logiqa-seed123\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-013-constraint-ablation\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"exp-075b-contrastive-mistral-folio\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-080-contrastive-mistral-logiqa200\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-078-debate-mistral-logiqa200\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-078\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-083-icg-mistral-logiqa-seed123\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-074d-icg-mistral-folio-seed456\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-077-kappa-generalization\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-077\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-075b\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-074c-icg-mistral-folio-seed123\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-076-debate-mistral-folio\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-079-icg-mistral-logiqa200\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-072b-llama8b-logiqa200\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-074-icg-mistral-folio\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-073b-qwen7b-logiqa200-seed456\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"exp-073-qwen7b-logiqa200-seed456\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"exp-072-llama8b-logiqa200\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"exp-064-deepseek-r1-qwen3-8b-folio204\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"exp-075-contrastive-mistral-folio\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"exp-077-generalization-kappa\": {\"status\": \"PREPARING\"}, \"exp-071-qwen7b-logiqa200-seed123\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-048-llama8b-pw600\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-053-mistral-folio204-seed456\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"exp-052-mistral-folio204-seed123\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"exp-069-llama8b-logiqa200\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-065-qwen7b-pw600\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-062-gemma27b-folio204\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-069-mistral-logiqa200\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-070-qwen7b-logiqa200\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"exp-068-qwen3-logiqa200\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-064\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"exp-067-mistral-folio-seed789\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"exp-063-llama8b-folio204-16639\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-063-llama8b-folio204\": {\"status\": \"PREPARING\", \"conclusion\": \"negative\"}, \"exp-061-qwen7b-folio204\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-059-cross-qwen3-extractor\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"exp-063\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-040-qwen3-pw600-16639\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-060-cross-qwen25-14b-extractor\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-057-mistral-folio204-t03\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-034\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-039-14b-pw600-16639\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-058-mistral-folio204-t05\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-051-mistral-k-sensitivity\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"exp-055-multitemp-mistral-folio\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-028b-qwen3-thinking-folio204\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"exp-052\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"exp-054-mistral-folio204-t10\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-046-mistral-pw600\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-053\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-050b-mistral-icl-oracle\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-050-mistral-icl-oracle-folio199\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"exp-049b-mistral-logiqa200\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-044b-icl-oracle\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-049-mistral-logiqa200\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"exp-041-14b-folio204-16639\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-045b-backward-verify\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"exp-045-backward-verification\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-038-14b-logiqa200-16639\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-033\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"exp-042b-premise-formal\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"exp-044-icl-oracle\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"exp-035\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-036b-cross-trace-unsat\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-042-premise-formalization\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"exp-043-consistency-filtering\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-036-z3-feedback-folio204\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-028-qwen3-14b-thinking\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"exp-033-qwen3-pw600-nonthinking\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"exp-004-qwen7b-rerun\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"exp-007-qwen72b-awq\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"exp-027-qwen3-14b-non-thinking\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"exp-030-crossmodel-mistral-folio204\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-031-oracle-folio-regen\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"exp-029-contrastive-folio204\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-026-folio204-trace-regen\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"exp-023-discriminative-rate\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"exp-022-oracle-proofwriter\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"temperature-ablation-t07\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"sica_constraint_ablation_013\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"exp-004-qwen7b\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"temperature-ablation-t10\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-012-gsm8k-pilot\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-021-oracle-folio\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"temperature-ablation-t05\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"temperature-ablation-t03\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-014-deepseek-r1-7b\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-010-mistral-v3\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"sica_expanded_14b\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"exp-019-llama8b-strategyqa-200\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-018-arc-v2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"exp-009-overhead-analysis\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"exp-020-llama8b-folio-204\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"pilot-contrastive-prompt\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"exp-011-llama8b-v3\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"exp-010-mistral-v2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"pilot-constraint-filtering\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-018-arc\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"exp-017-strategyqa-v3\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"exp-017-strategyqa-v2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"exp-017-strategyqa\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"exp-010-mistral\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"exp-011-llama8b-v2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"sica_temp_diversity\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"sica_d012_14b\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"sica_k_sensitivity_14b\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"exp-011-llama8b\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"exp-016-weighted-sc\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"exp-005\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"sica_folio30\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"sica_d016_c0_precheck\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"sica_proofwriter30_v2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"sica_proofwriter30\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"sica_aime30_v3\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"sica_aime30_v2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"sica_aime30_t07\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"mvp_math50_t07\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"sica_smoke_5q\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"smoke-test-5q\": {\"status\": \"PREPARING\", \"conclusion\": \"failed\"}, \"crd_folio_main\": {\"status\": \"DONE\", \"conclusion\": \"success\"}}, \"count\": 139, \"total\": 139, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3713}}"
    }
  },
  "sourceToolAssistantUUID": "c191a825-25f2-41b7-8a9d-f98c1397eeb3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora"
}
```

</details>

---


### Runtime record

_source line 8829 · 2026-05-20T09:36:26.443Z_

```json
{
  "parentUuid": "44bef146-e640-45b1-ab88-3e23a6663cdc",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "8c772c75-576a-42f1-9742-1cfe49bcfc7c",
  "timestamp": "2026-05-20T09:36:26.443Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora"
}
```

---


### Runtime record

_source line 8830_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[服务器重启后首条消息] 当前日期: 2026-05-20。服务器刚重启，项目状态可能已更新。不要依赖对话历史中的状态信息，以 registry 当前值为准。  **用户消息：** [Director 指令] ## 写作任务：EMNLP 2026 ARR May 25 — Full Draft 更新  **DDL**: May 25, 2026（5 天） **模式**: Full Draft 更新…",
  "leafUuid": "8c772c75-576a-42f1-9742-1cfe49bcfc7c",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1"
}
```

---


### Runtime record

_source line 8831_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise paper results with oracle FOLIO constraint experiments",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1"
}
```

---


### Runtime record

_source line 8832_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[服务器重启后首条消息] 当前日期: 2026-05-20。服务器刚重启，项目状态可能已更新。不要依赖对话历史中的状态信息，以 registry 当前值为准。  **用户消息：** [Director 指令] ## 写作任务：EMNLP 2026 ARR May 25 — Full Draft 更新  **DDL**: May 25, 2026（5 天） **模式**: Full Draft 更新…",
  "leafUuid": "8c772c75-576a-42f1-9742-1cfe49bcfc7c",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1"
}
```

---


### Runtime record

_source line 8833_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise paper results with oracle FOLIO constraint experiments",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1"
}
```

---


### System

_source line 8834 · 2026-05-20T09:38:41.839Z_

```json
{
  "parentUuid": null,
  "logicalParentUuid": "8c772c75-576a-42f1-9742-1cfe49bcfc7c",
  "isSidechain": false,
  "type": "system",
  "subtype": "compact_boundary",
  "content": "Conversation compacted",
  "isMeta": false,
  "timestamp": "2026-05-20T09:38:41.839Z",
  "uuid": "e44ed9fe-e224-4a8f-8aea-68676b4e3228",
  "level": "info",
  "compactMetadata": {
    "trigger": "auto",
    "preTokens": 169438,
    "preCompactDiscoveredTools": [
      "CronList",
      "ExitPlanMode",
      "WebSearch",
      "mcp__agent-ml-research__check_paper_consistency",
      "mcp__agent-ml-research__check_provenance_completeness",
      "mcp__agent-ml-research__cleanup_pdf_images",
      "mcp__agent-ml-research__compute_coverage_matrix",
      "mcp__agent-ml-research__edit_paper_section",
      "mcp__agent-ml-research__get_worker_status",
      "mcp__agent-ml-research__list_artifacts",
      "mcp__agent-ml-research__list_workers",
      "mcp__agent-ml-research__load_project_config",
      "mcp__agent-ml-research__overleaf_status",
      "mcp__agent-ml-research__paper_agent_post_to_director",
      "mcp__agent-ml-research__paper_agent_request_review",
      "mcp__agent-ml-research__paper_compile_and_check",
      "mcp__agent-ml-research__pdf_to_images",
      "mcp__agent-ml-research__read_experiment_plan_with_status",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__read_roadmap",
      "mcp__agent-ml-research__register_artifact",
      "mcp__agent-ml-research__save_project_file",
      "mcp__agent-ml-research__spawn_worker",
      "mcp__agent-ml-research__verify_references",
      "mcp__agent-ml-research__write_paper_section"
    ],
    "postTokens": 8501,
    "durationMs": 135394
  },
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora"
}
```

---


## Round 384

## Round 384

74 recorded events


### User

_source line 8835 · 2026-05-20T09:38:41.840Z_

This session is being continued from a previous conversation that ran out of context. The summary below covers the earlier portion of the conversation.

Summary:
1. Primary Request and Intent:
   The Director is orchestrating a Paper Agent to produce/update an EMNLP 2026 ARR paper (8pp main text limit, DDL May 25). This session covers:
   - **F6 scatter plot page overflow fix**: Moving figure to appendix + compressing §5.3 and §6 to fit 8-page limit (Plan C approved by Director)
   - **Qwen2.5-14B cross-model κ patch**: Adding κ=0.74 data showing bottleneck worsens with scale
   - **D078 major framing change**: From "scale-dependent" to "universal across architectures" + adding LLaMA-8B and Qwen2.5-7B data
   - **LATEST (in progress): Full Draft update** — Director requests writing_plan.yaml for a major narrative update incorporating Symbolic Confirmation Bias (Claim 7), Process-κ (Claim 8), and 25+ failed methods (up from 12). Paper is now "comprehensive negative result + diagnostic analysis."

2. Key Technical Concepts:
   - **SICA pipeline**: K traces → FOL constraint extraction → dedup → weighted partial MAX-SAT (Z3) → answer selection
   - **Independence Bottleneck**: Same-model traces violate Condorcet independence; constraints inherit correlation
   - **Fleiss' κ and Effective-K**: κ=0.21–0.82 instruction-tuned, Eff-K=1.20–3.62 at K=12
   - **Independence-Accuracy Trade-off (HERO FINDING)**: SC/DP/ICG cluster at κ≈0.40–0.47; Debate κ=0.15/Eff-K=4.44 but Δ=-18.6pp
   - **Cross-architecture universality (D078)**: 3 families (Mistral κ=0.44, LLaMA κ=0.41, Qwen-7B κ=0.66, Qwen-14B κ=0.74) all exhibit κ≥0.41. Cross-family Δκ=0.22 >> within-family Δκ=0.08
   - **McNemar's paired test**: 3/6 method-dataset conditions significant negative; 0/9 SICA conditions significant positive
   - **ICG Paradox**: Superior constraints (99.4% Z3, 32.3% redundancy) but Δ≈0; κ=0.47 ≈ SC's 0.44
   - **NEW — Symbolic Confirmation Bias (D082, Claim 7)**: Bias ratio 4.97× on incorrect problems, 97.6% SICA errors overlap SC errors
   - **NEW — Process-κ (D082, Claim 8)**: CoT cosine similarity 0.69 >> answer-κ 0.41, r=-0.06, 9.3% convergent pairs
   - **NEW — 25+ interventions ALL fail** (up from 12): 9 prompt + 3 method + 13 new directions
   - **Oracle ceiling**: Gold FOL yields +14.22pp FOLIO, +11.50pp PW (p<0.001); self-extraction captures only 24%

3. Files and Code Sections:

   - **`docs/paper/analysis.tex`** (MOST MODIFIED)
     - Central analysis section. Contains §5.1 Condorcet Effective-K, §5.2 Supporting Diagnostics, §5.3 Remediation Analysis
     - §5.3 method interventions compressed to 1-2 sentences per method with appendix references
     - Table 4 (κ generalization) expanded to 7 rows with Model column:
     ```latex
     \caption{Independence-accuracy trade-off (FOLIO, $n = 204$). Top: aggregation methods on Mistral-7B; bottom: SC across three model families. All families produce $\kappa \geq 0.41$, confirming an architecture-independent ceiling.}
     \setlength{\tabcolsep}{3.5pt}
     \begin{tabular}{@{}llccrr@{}}
     \toprule
     Model & Aggregation & $\kappa$ & Eff-$K$ & $K$ & Acc.\ (\%) \\
     \midrule
     Mistral-7B & Debate & 0.15 & 4.44 & 12 & 38.24 \\
     & Diverse-Prompt & 0.40 & 2.21 & 12 & $\approx$\,55 \\
     & Self-Consistency & 0.44 & 2.02 & 10 & 56.86 \\
     & ICG & 0.47 & 1.93 & 10 & 51.96 \\
     \addlinespace
     LLaMA-3.1-8B & Self-Consistency & 0.41 & 1.93 & 12 & 66.18 \\
     Qwen2.5-7B & Self-Consistency & 0.66 & 1.46 & 12 & 77.45 \\
     Qwen2.5-14B & Self-Consistency & 0.74 & 1.32 & 12 & 75.49 \\
     \bottomrule
     ```
     - §5.1 cross-model sentence: "Cross-model validation with three families confirms universality: Mistral-7B (κ=0.44), LLaMA-3.1-8B (κ=0.41), Qwen2.5-7B (κ=0.66), and Qwen2.5-14B (κ=0.74) all produce κ well above zero"
     - §5.3 trade-off: "All three model families cluster above κ=0.40, confirming the ceiling is architecture-independent"

   - **`docs/paper/discussion.tex`**
     - Compressed in Plan C: trade-off paragraph references Table+Figure instead of restating κ numbers
     - Statistical evidence compressed to 3 sentences
     - Scale limitations rewritten for D078: "Within the Qwen family, κ increases from 0.66 (7B) to 0.74 (14B)...However, disentangling scale from architecture requires controlled same-family experiments across ≥3 scales"
     - Full current content (14 lines): oracle causality, dual-channel, trade-off, diagnostics, statistical evidence, scale limitations

   - **`docs/paper/abstract.tex`**
     - Final sentence: "The bottleneck is structural and universal---three model families (Mistral, LLaMA, Qwen) all exhibit $\kappa \geq 0.41$, and no aggregation method breaks through."

   - **`docs/paper/conclusion.tex`**
     - Updated: "structural and universal across three model families (Mistral, LLaMA, Qwen)"
     - Rest unchanged from prior session

   - **`docs/paper/appendix.tex`**
     - §Independence-Accuracy Scatter Plot (app:kappa-scatter): F6 figure moved from main text
     - §Cross-Model Kappa Analysis (app:cross-model-kappa): 6-row table (4 FOLIO + 2 PW), text emphasizes cross-family Δκ=0.22 >> within-family Δκ=0.08
     - §Constraint Quality (app:constraint-quality): Standard SICA/ICG/Contrastive comparison table
     - §Error Categorization (app:error-categorization): Debate and Contrastive discordant analyses
     - Plus many other appendix sections (prompts, Z3 pseudocode, diagnostics, power analysis, etc.)

   - **`docs/paper/introduction.tex`** — C1 contribution mentions "four aggregation methods", unchanged in this session

   - **`paper_framing.md`** — 31K chars, D085 final version. Key new content:
     - 8 Core Claims (up from 5-6), with Claims 7 (Symbolic Confirmation Bias) and 8 (Process-κ) as NEW
     - 25+ interventions ALL fail (9 prompt + 3 method + 13 new directions)
     - Updated story spine with Symbolic Confirmation Bias as root cause explanation
     - Headline: "Independence bottleneck is structural, universal across architectures, and rooted in Symbolic Confirmation Bias"

   - **`writing_plan.yaml`** — 35K chars, current version from 2026-05-19. Has 5 contributions (C1-C5), needs update to include C6 (method-level failures), C7 (Symbolic Confirmation Bias), C8 (Process-κ). Table plan has 7 main tables, 6 appendix tables. Writing order: method → experiments → analysis → related_work → introduction → discussion → abstract → conclusion.

4. Errors and Fixes:
   - **Page overflow after F6 figure**: Figure pushed main text past 8 pages. Fixed by moving to appendix, then further compressing §5.3 and §6 (Plan C).
   - **Hyperref warning**: `\section{Cross-Model $\kappa$ Analysis}` caused "Token not allowed in PDF string" warnings. Fixed by changing to `\section{Cross-Model Kappa Analysis}`.
   - **Table 5 overfull hbox**: Adding Model column caused 33pt overflow. Reduced to 8pt with `\setlength{\tabcolsep}{3.5pt}`. After D078 (7 rows), overflow increased to 14pt — acceptable visually.
   - **False system reminders**: Multiple "[系统提醒]...没有调用 main_agent_post_to_director" messages appeared. These are INCORRECT — Paper Agent uses `paper_agent_post_to_director` (not `main_agent_post_to_director`). Correctly ignored each time. The actual tool was always called correctly.

5. Problem Solving:
   - Successfully maintained main text within 8 pages across 4 patch rounds by: (a) moving F6 to appendix, (b) compressing §5.3 method interventions from ~25 to ~10 lines, (c) compressing §6 Discussion paragraphs, (d) carefully managing new text additions to stay within budget
   - Systematically cascaded framing changes across all files when switching from "scale-dependent" to "universal across architectures" (abstract, §5.1, §5.3, Table 5 caption, discussion, conclusion, appendix)
   - All `paper_agent_post_to_director` calls successful throughout session

6. All User Messages:
   - "Continue from where you left off." (initial session recovery)
   - "[系统提醒] 你刚才完成了 [Director 指令] 但没有调用 main_agent_post_to_director..." (FALSE, ~6 times, always ignored correctly)
   - "[Director 指令] 批准方案 C（A+B 组合），执行：1. §5.3 method interventions 压缩...2. §6 Discussion 精简...3. 确保主文 Conclusion 在 page 8 内结束"
   - "Continue from where you left off." (multiple times between patches)
   - "[Director 指令] [Patch] 新增跨模型 κ 数据 — Qwen2.5-14B independence bottleneck 比 Mistral-7B 更严重" — with κ=0.738, Eff-K=1.32 data and 5 patch targets
   - "Continue from where you left off." (multiple times)
   - "[Director 指令] [Patch] D078 Framing 重大调整：从 'scale-dependent' 改为 'universal across architectures' + 补充 2 个模型 κ 数据" — with LLaMA-8B (κ=0.412, Acc=66.18%) and Qwen2.5-7B (κ=0.658, Acc=77.45%), 7 modification targets
   - "Continue from where you left off." (multiple times)
   - "[Director 指令] ## 写作任务：EMNLP 2026 ARR May 25 — Full Draft 更新" — MAJOR: new narrative with 8 Core Claims, Symbolic Confirmation Bias, Process-κ, 25+ failed methods. Requests writing_plan.yaml generation first.
   - "CRITICAL: Respond with TEXT ONLY..." (this summary request)

7. Pending Tasks:
   - **Generate updated `writing_plan.yaml`** for Director approval — this is the explicit next step from the latest Director instruction. The plan must incorporate:
     - Claims 7 (Symbolic Confirmation Bias: 4.97× bias ratio) and 8 (Process-κ: cosine 0.69)
     - 25+ methods ALL negative narrative (up from 12)
     - Updated contributions list (C1-C8 vs current C1-C5)
     - Updated table plan (new tables for confirmation bias, process-κ)
     - Updated visualization plan
     - Updated page budget accounting for new content
   - **Direction F (Blind FOL)** results expected later (~5h) — Director says to Patch in when available
   - **F6 scatter plot update** (4→6 points with LLaMA-8B and Qwen2.5-7B) — Director suggested as optional future work

8. Current Work:
   The most recent Director instruction is a **Full Draft update** for EMNLP 2026 (DDL May 25). The Director explicitly requests: "请先生成 `writing_plan.yaml` 提交我审批。"
   
   I had begun reading inputs for the writing plan:
   - Read `paper_framing.md` (complete, 31K chars — D085 final narrative with 8 claims)
   - Read `writing_plan.yaml` (complete, 35K chars — current version with 5 contributions, needs major update)
   - Attempted to read registry (139 experiments, output too large for inline but got experiment list with statuses)
   - Had NOT yet started generating the new writing_plan.yaml
   
   Key new experiments identified in registry: `exp-confirmation-bias` (DONE/success), `exp-wild4-process-kappa` (DONE/negative), `exp-direction-a-prove` (DONE/negative), `exp-direction-d-cegis` (DONE/negative), `exp-direction-b-deepconf` (DONE/negative), `exp-wild3-perturbation` (DONE/negative), `exp-wild1-max-unsat` (DONE/negative), `exp-wild6-kappa-aware-sc` (DONE/negative), `exp-wave3-dir-i-z3-filter` (DONE/negative), `exp-wave3-dir-j-bootstrap` (DONE/negative), `exp-direction-e-abstention` (DONE/success), `exp-cross-model-phase1/2` (DONE)

9. Optional Next Step:
   Generate the updated `writing_plan.yaml` incorporating the D085 narrative. The Director explicitly said: "请先生成 `writing_plan.yaml` 提交我审批。" This plan needs to:
   - Expand contributions from 5 to 8 (adding C6: method-level failures comprehensive, C7: Symbolic Confirmation Bias, C8: Process-κ)
   - Update paper outline to prominently feature confirmation bias and process-κ
   - Add new tables/figures for the 25+ methods exhaustion, confirmation bias metrics, process-κ
   - Update the narrative from "independence bottleneck" to "Symbolic Confirmation Bias as root cause"
   - Assess which existing .tex sections need major rewrite vs patch (§5.3 and introduction likely need substantial rewriting; method.tex needs new subsections; experiments.tex needs expansion)
   - Read existing .tex files (introduction.tex, method.tex, experiments.tex, related_work.tex) to assess rewrite scope before generating the plan
   - Submit plan to Director via `paper_agent_post_to_director` for approval before executing

If you need specific details from before compaction (like exact code snippets, error messages, or content you generated), read the full transcript at: /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-3-projects-symb-invariant-consensus--claude-sessions-paper-agent-644edc69/6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1.jsonl
Continue the conversation from where it left off without asking the user any further questions. Resume directly — do not acknowledge the summary, do not recap what was happening, do not preface with "I'll continue" or similar. Pick up the last task as if the break never happened.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e44ed9fe-e224-4a8f-8aea-68676b4e3228",
  "isSidechain": false,
  "promptId": "3f50ba00-7d30-45ec-b450-7010d531c858",
  "type": "user",
  "isVisibleInTranscriptOnly": true,
  "isCompactSummary": true,
  "uuid": "4542ec3b-248b-4ddf-89fc-a6f8dbcc1992",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora"
}
```

</details>

---


### Runtime record

_source line 8836 · 2026-05-20T09:38:41.836Z_

```json
{
  "parentUuid": "4542ec3b-248b-4ddf-89fc-a6f8dbcc1992",
  "isSidechain": false,
  "attachment": {
    "type": "compact_file_reference",
    "filename": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex",
    "displayPath": "../../../docs/paper/appendix.tex"
  },
  "type": "attachment",
  "uuid": "7a8c9c64-b82e-45e9-86de-641cda0b2d8c",
  "timestamp": "2026-05-20T09:38:41.836Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora"
}
```

---


### Runtime record

_source line 8837 · 2026-05-20T09:38:41.792Z_

```json
{
  "parentUuid": "7a8c9c64-b82e-45e9-86de-641cda0b2d8c",
  "isSidechain": false,
  "attachment": {
    "type": "file",
    "filename": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/analysis.tex",
    "content": {
      "type": "text",
      "file": {
        "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/analysis.tex",
        "content": "\\section{Analysis}\n\\label{sec:analysis}\n\nThe regime-dependent pattern in \\S\\ref{sec:main-results} establishes \\emph{where} SICA succeeds and fails. This section investigates \\emph{why}: trace correlation quantifies the SC plateau (\\S\\ref{sec:effective-k}), supporting diagnostics confirm the mechanism (Appendices~\\ref{app:extraction}--\\ref{app:entropy}), and remediation analysis reveals a fundamental independence-accuracy trade-off (\\S\\ref{sec:remediation}).\n\n\\subsection{Condorcet Effective-K}\n\\label{sec:effective-k}\n\nTable~\\ref{tab:independence} reports Fleiss' $\\kappa$ and Effective-K (Eq.~\\ref{eq:effk}) across 15 conditions at $K = 12$. Among instruction-tuned models, $\\kappa$ ranges from 0.21 to 0.82, yielding $K_{\\text{eff}} = 1.20\\text{--}3.62$. Qwen3-14B in thinking mode reaches $\\kappa = 0.91$ ($K_{\\text{eff}} = 1.09$). The four Mistral-7B FOLIO seeds produce $\\kappa \\in [0.41, 0.51]$ ($K_{\\text{eff}} \\approx 1.8\\text{--}2.2$), yet $\\Delta$ ranges from $+3.43$ to $-0.49$\\,pp---seed-level constraint quality, not independence, drives the variation. Two conditions are jointly necessary for positive $\\Delta$: sufficient $K_{\\text{eff}}$ (Qwen conditions with $K_{\\text{eff}} \\leq 1.30$ never improve) and sufficient SC accuracy (Mistral on ProofWriter with the highest $K_{\\text{eff}} = 3.62$ but SC $= 39\\%$ produces significant degradation). Even when both hold, sampling variance determines whether the constraint pool is discriminative. Cross-model validation with three families confirms universality: Mistral-7B ($\\kappa = 0.44$), LLaMA-3.1-8B ($\\kappa = 0.41$), Qwen2.5-7B ($\\kappa = 0.66$), and Qwen2.5-14B ($\\kappa = 0.74$) all produce $\\kappa$ well above zero (Table~\\ref{tab:kappa_generalization}; Appendix~\\ref{app:cross-model-kappa}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Trace independence metrics ($K = 12$, sorted by $\\kappa$ descending). $\\kappa$: Fleiss' Kappa. $K_{\\text{eff}}$: Effective-K (Eq.~\\ref{eq:effk}). SC: Self-Consistency baseline. $\\Delta$: SICA $-$ SC (pp). {*}\\,$p < 0.05$; positive $\\Delta$ values do not reach significance. multi-T $= T \\in \\{0.3, 0.7, 1.2\\}$, 4 traces each.}\n\\label{tab:independence}\n\\begin{tabular}{@{}llccrr@{}}\n\\toprule\nModel & Condition & $\\kappa$ & $K_{\\text{eff}}$ & SC (\\%) & $\\Delta$ (pp) \\\\\n\\midrule\nQwen3 (think) & FOLIO & 0.91 & 1.09 & ${\\sim}$84 & ${\\sim}$0 \\\\\nQwen2.5-14B & LogiQA & 0.82 & 1.20 & 78.50 & $-$0.50 \\\\\nQwen3 & FOLIO & 0.77 & 1.26 & 84.80 & $-$0.49 \\\\\nQwen2.5-14B & FOLIO & 0.74 & 1.30 & 75.49 & $-$0.98 \\\\\nQwen2.5-7B & FOLIO & 0.66 & 1.46 & 75.98 & $+$0.49 \\\\\n\\addlinespace\nMistral-7B ($T{=}0.3$) & FOLIO & 0.53 & 1.77 & 58.33 & $-$1.47 \\\\\nMistral-7B & LogiQA & 0.51 & 1.81 & 51.00 & $+$0.50 \\\\\nMistral-7B (s456) & FOLIO & 0.51 & 1.82 & 55.88 & 0.00 \\\\\nMistral-7B (s42) & FOLIO & 0.50 & 1.84 & 55.88 & $+$3.43 \\\\\nMistral-7B (s123) & FOLIO & 0.49 & 1.88 & 54.41 & $+$2.94 \\\\\nMistral-7B (s789) & FOLIO & 0.41 & 2.17 & 54.41 & $-$0.49 \\\\\nMistral-7B ($T{=}0.5$) & FOLIO & 0.52 & 1.80 & 58.33 & $-$0.98 \\\\\nMistral-7B (multi-T) & FOLIO & 0.48 & 1.91 & 57.84 & 0.00 \\\\\nMistral-7B ($T{=}1.0$) & FOLIO & 0.48 & 1.91 & 55.39 & 0.00 \\\\\nMistral-7B & PW-D5 & 0.21 & 3.62 & 39.33 & $\\mathbf{-2.83}${*} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Supporting Diagnostic Analyses}\n\nFour additional analyses confirm the mechanism underlying SICA's failure. Extraction error taxonomy (Appendix~\\ref{app:extraction}): 91.8\\% of constraints are technically discriminative, but their discriminative direction mirrors the majority answer; 42.9\\% of constraints are redundant across traces (Appendix~\\ref{app:constraint-quality}), quantifying how co-sourcing from the same model produces near-duplicate formalizations. Removing the 8.2\\% non-discriminative constraints yields zero improvement. Constraint ablation (Appendix~\\ref{app:ablation}): on Mistral-7B ($n = 804$, FOLIO + ProofWriter pooled), MAX-SAT and count-only agree on 94.4\\% of predictions, with disagreements split nearly evenly (18 vs.\\ 17); the solver's weighted satisfiability computation adds no value over simple constraint counting because constraint weights carry information redundant with vote counts (Eq.~\\ref{eq:degenerate}). Per-domain, MAX-SAT provides a marginal edge in the intermediate-SC region (59.3\\% vs.\\ count-only 56.9\\%) but actively hurts in the Type~C regime (36.5\\% vs.\\ 37.2\\%), mirroring the regime-dependent pattern of SICA itself. Hyperparameter sensitivity (Appendix~\\ref{app:sensitivity}): $K = 12$ is the only setting with $\\Delta > 2$\\,pp among five $K$ values, and only $T = 0.7$ among four temperatures yields a positive effect; both peaks coincide with relatively low SC baselines rather than reflecting hyperparameter effects per se. Entropy decomposition (Appendix~\\ref{app:entropy}): all SICA effects concentrate in high-entropy problems ($\\Delta$ up to $+12.8$\\,pp in the intermediate-SC region), but the direction depends on the accuracy regime---high entropy signals correctable uncertainty only when the model has partial knowledge.\n\n\\subsection{Remediation Analysis}\n\\label{sec:remediation}\n\\label{sec:interventions}\n\nWe test twelve remediation strategies: nine prompt-level spanning six dimensions (Appendix Table~\\ref{tab:remediation}) and three method-level (Table~\\ref{tab:method_interventions}). All nine prompt-level strategies fail. Contrastive prompting reduces non-discriminative constraints from 8.2\\% to 6.0\\% but newly discriminative constraints still mirror the majority ($\\Delta = -1.1$\\,pp). Cross-model extraction fails in both directions: weaker models extracting from stronger traces yield 0\\% discriminative constraints; stronger models extracting from weaker traces produce accuracy within $\\pm$1\\,pp of self-extraction. Only 1 of 4 temperature settings yields a positive effect ($p = 0.092$); multi-temperature sampling produces $\\Delta = 0.00$\\,pp.\n\n\\paragraph{Method-level interventions.} Three method-level strategies target different aspects of the independence bottleneck on Mistral-7B (Table~\\ref{tab:method_interventions}). Independent Constraint Generation (ICG) bypasses trace-constraint coupling by generating constraints directly from premises. Despite producing objectively superior constraints---higher Z3 compilation, lower redundancy (Appendix~\\ref{app:constraint-quality})---ICG yields $\\Delta \\approx 0$ across three seeds (McNemar $p = .206$, n.s.). Per-constraint-set reranking produces $\\kappa = 0.47$, nearly identical to SC's $\\kappa = 0.44$: the bottleneck is a property of the model itself, not an artifact of trace co-sourcing. Contrastive scoring generates pro and con constraints per candidate but yields $\\Delta = -9.31$\\,pp on FOLIO ($p < 0.01$) and $-4.50$\\,pp on LogiQA (n.s.); 62.7\\% of constraints are trivially satisfied, explaining systematic degeneration (Appendices~\\ref{app:constraint-quality},~\\ref{app:error-categorization}). Debate adds a proposer-critic-defense chain, producing $\\Delta = -18.63$\\,pp and $-23.00$\\,pp ($p < 0.001$ on both datasets), with discordant pairs heavily skewed toward correct$\\to$wrong flips (Appendix~\\ref{app:error-categorization}). Three of six method-dataset conditions reach significance, all negative.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Method-level interventions on Mistral-7B with McNemar's paired test. All produce neutral-to-catastrophic results. ICG shows two FOLIO seeds; $p$ for the first. {*}{*}{*}\\,$p < 0.001$; {*}{*}\\,$p < 0.01$.}\n\\label{tab:method_interventions}\n\\begin{tabular}{@{}ll rc rc@{}}\n\\toprule\n& & \\multicolumn{2}{c}{FOLIO ($n = 204$)} & \\multicolumn{2}{c}{LogiQA ($n = 200$)} \\\\\n\\cmidrule(lr){3-4} \\cmidrule(lr){5-6}\nMethod & Target & $\\Delta$ (pp) & $p$ & $\\Delta$ (pp) & $p$ \\\\\n\\midrule\nSC baseline & --- & 0.00 & --- & 0.00 & --- \\\\\nICG & Trace coupling & $-$1.96\\,/\\,$+$1.47 & .206 & $-$0.50 & .706 \\\\\nContrastive & Scoring bias & $\\mathbf{-9.31}$ & .007 & $-$4.50 & .160 \\\\\nDebate & Role diversity & $\\mathbf{-18.63}$ & ${<}.001$ & $\\mathbf{-23.00}$ & ${<}.001$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Independence-accuracy trade-off.} Table~\\ref{tab:kappa_generalization} compares Fleiss' $\\kappa$ across four aggregation methods on Mistral-7B FOLIO and adds SC from three model families for cross-architecture validation. On Mistral-7B, SC ($\\kappa = 0.44$), Diverse-Prompt ($\\kappa = 0.40$), and ICG ($\\kappa = 0.47$) cluster at $\\kappa \\approx 0.40$--$0.47$, forming a same-model ceiling. Debate breaks through to $\\kappa = 0.15$ (Eff-$K = 4.44$) but collapses accuracy by $-18.6$\\,pp. All three model families cluster above $\\kappa = 0.40$, confirming the ceiling is architecture-independent (Appendix~\\ref{app:cross-model-kappa}). This constitutes a Pareto frontier (Figure~\\ref{fig:kappa-accuracy}): methods that increase trace independence destroy accuracy, while methods that preserve accuracy cannot break the correlation floor. The only demonstrated path past this frontier requires signal from outside the model's distribution, consistent with the oracle result (\\S\\ref{sec:oracle}) and published systems that bypass self-extraction \\citep{xu2026dylos, li2025aristotle, wang2025fover, pan2023logiclm}.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Independence-accuracy trade-off (FOLIO, $n = 204$). Top: aggregation methods on Mistral-7B; bottom: SC across three model families. All families produce $\\kappa \\geq 0.41$, confirming an architecture-independent ceiling. $\\kappa$: Fleiss' kappa on raw answers.}\n\\label{tab:kappa_generalization}\n\\setlength{\\tabcolsep}{3.5pt}\n\\begin{tabular}{@{}llccrr@{}}\n\\toprule\nModel & Aggregation & $\\kappa$ & Eff-$K$ & $K$ & Acc.\\ (\\%) \\\\\n\\midrule\nMistral-7B & Debate & 0.15 & 4.44 & 12 & 38.24 \\\\\n& Diverse-Prompt & 0.40 & 2.21 & 12 & 54.41 \\\\\n& Self-Consistency & 0.44 & 2.02 & 10 & 56.86 \\\\\n& ICG & 0.47 & 1.93 & 10 & 51.96 \\\\\n\\addlinespace\nLLaMA-3.1-8B & Self-Consistency & 0.41 & 2.17 & 12 & 66.18 \\\\\nQwen2.5-7B & Self-Consistency & 0.66 & 1.46 & 12 & 75.98 \\\\\nQwen2.5-14B & Self-Consistency & 0.74 & 1.32 & 12 & 75.49 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}",
        "numLines": 93,
        "startLine": 1,
        "totalLines": 93
      }
    },
    "displayPath": "../../../docs/paper/analysis.tex"
  },
  "type": "attachment",
  "uuid": "d6c9cf14-f91a-4899-976a-5f7abe12ae4f",
  "timestamp": "2026-05-20T09:38:41.792Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora"
}
```

---


### Runtime record

_source line 8838 · 2026-05-20T09:38:41.537Z_

```json
{
  "parentUuid": "d6c9cf14-f91a-4899-976a-5f7abe12ae4f",
  "isSidechain": false,
  "attachment": {
    "type": "file",
    "filename": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/conclusion.tex",
    "content": {
      "type": "text",
      "file": {
        "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/conclusion.tex",
        "content": "\\section{Conclusion}\\label{sec:conclusion}\n\nWe evaluated Symbolic Invariant Consensus Aggregation (SICA) across six models, three reasoning domains, and over 3,000 instances with four-seed replication. Grounded in the Condorcet Jury Theorem, our analysis explains why SC majority voting saturates and why symbolic constraint aggregation fails to break this plateau under same-model self-extraction---a bottleneck that is structural and universal across three model families (Mistral, LLaMA, Qwen).\n\nThe primary finding is a fundamental independence-accuracy trade-off. Fleiss' $\\kappa$ generalization across aggregation methods reveals a Pareto frontier: Debate reduces $\\kappa$ from 0.44 to 0.15 (Eff-$K$: $2.0 \\to 4.4$) but collapses accuracy by $-18.6$\\,pp on FOLIO ($-23.0$\\,pp on LogiQA); methods that preserve accuracy cannot break the correlation floor ($\\kappa \\geq 0.40$). This trade-off constrains all same-model trace aggregation, not only symbolic approaches, and twelve remediation strategies all fail to escape it.\n\nThe independence bottleneck quantifies SC's own scaling ceiling: same-model traces produce $\\kappa = 0.21$--$0.82$ (Eff-$K = 1.20$--$3.62$ at $K = 12$), meaning traces beyond 12 add negligible independent information. Oracle controls confirm the aggregation mechanism is sound ($+14.22$\\,pp FOLIO, $+11.50$\\,pp ProofWriter, $p < 0.001$); self-extraction captures only 24\\% of this ceiling. A directional positive trend ($+3.43$\\,pp best, $+1.47$\\,pp mean; none reaching $p < 0.05$) appears in one model-dataset condition, but its narrow operating range and seed sensitivity limit practical applicability. For practitioners, $C_0$ combined with SC accuracy provides a zero-cost diagnostic predicting when symbolic augmentation is unlikely to help. Three paths forward trade simplicity for independence: trained extractors, external provers, and multi-model pipelines.",
        "numLines": 7,
        "startLine": 1,
        "totalLines": 7
      }
    },
    "displayPath": "../../../docs/paper/conclusion.tex"
  },
  "type": "attachment",
  "uuid": "37d72d2f-f876-4593-8946-e8f36d6916ed",
  "timestamp": "2026-05-20T09:38:41.537Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora"
}
```

---


### Runtime record

_source line 8839 · 2026-05-20T09:38:41.535Z_

```json
{
  "parentUuid": "37d72d2f-f876-4593-8946-e8f36d6916ed",
  "isSidechain": false,
  "attachment": {
    "type": "file",
    "filename": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/discussion.tex",
    "content": {
      "type": "text",
      "file": {
        "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/discussion.tex",
        "content": "\\section{Discussion}\n\\label{sec:discussion}\n\nThe oracle experiments causally identify the failure source. Holding all pipeline components fixed and varying only constraint source, gold annotations yield $+14.22$\\,pp on FOLIO and $+11.50$\\,pp on ProofWriter ($p < 0.001$), while the best self-extraction captures only 24.1\\% of this ceiling. Because the aggregation mechanism is identical in both conditions, the gap localizes entirely to extraction quality.\n\nTrace correlation affects SICA through two channels. The \\emph{direct} channel limits voting diversity: Eff-$K < 2$ for many conditions (Table~\\ref{tab:independence}) confirms that same-model traces violate the CJT independence requirement, explaining the SC plateau. The \\emph{indirect} channel operates through constraint quality: correlated traces produce homogeneous constraints, causing MAX-SAT to degenerate to vote counting (Appendix~\\ref{app:ablation}). The oracle result disambiguates: gold constraints applied to the same correlated traces yield $+14.22$\\,pp, proving that constraint homogenization---not voting diversity---is the proximal bottleneck.\n\n\\paragraph{The independence-accuracy trade-off.} The $\\kappa$ generalization analysis (\\S\\ref{sec:remediation}, Table~\\ref{tab:kappa_generalization}) constitutes the primary finding. SC, Diverse-Prompt, and ICG form a same-model ceiling at $\\kappa \\approx 0.40$--$0.47$; Debate breaks through only at catastrophic accuracy cost (Figure~\\ref{fig:kappa-accuracy}). This trade-off constrains \\emph{all} same-model trace aggregation methods---not only symbolic approaches---because it arises from the model's output distribution, not from any specific aggregation procedure. Published systems that report positive results \\citep{xu2026dylos, li2025aristotle, wang2025fover, pan2023logiclm} each bypass same-model self-extraction.\n\n\\paragraph{Diagnostic tools for practitioners.} Our analysis yields two zero-cost diagnostics applicable before any constraint extraction. First, $C_0$ combined with SC accuracy predicts when symbolic augmentation is unlikely to help: $C_0 < 5\\%$ implies degeneration; SC $\\geq 60\\%$ implies confirmation bias; SC $\\leq 40\\%$ implies error amplification. Second, the $\\kappa$-based Eff-$K$ metric quantifies SC's own scaling ceiling: at Eff-$K \\approx 2$ (typical at $K = 12$), additional traces add negligible independent information regardless of aggregation method.\n\n\\paragraph{Statistical evidence.} The only statistically significant effects are negative: zero of nine SICA conditions reaches $p < 0.05$, while ProofWriter degradation ($p = 0.014$; $p = 0.011$) and three of six method-level conditions (Table~\\ref{tab:method_interventions}) reach significance, all negative. Oracle controls remain highly significant ($p < 0.001$). This asymmetry---zero significant positives against multiple significant negatives---constitutes the strongest statistical argument for the independence bottleneck.\n\n\\paragraph{Scale limitations and future work.} Within the Qwen family, $\\kappa$ increases from 0.66 (7B) to 0.74 (14B), consistent with the hypothesis that stronger models produce more correlated outputs. However, disentangling scale from architecture requires controlled same-family experiments across $\\geq$3 scales, which we leave to future work. Method-level interventions use Mistral-7B; whether 70B+ models shift the Pareto frontier is open. Three paths forward trade simplicity for independence: trained extractors, external provers, and multi-model pipelines.",
        "numLines": 14,
        "startLine": 1,
        "totalLines": 14
      }
    },
    "displayPath": "../../../docs/paper/discussion.tex"
  },
  "type": "attachment",
  "uuid": "7954b760-c989-47e1-8c29-ba2e7f415017",
  "timestamp": "2026-05-20T09:38:41.535Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora"
}
```

---


### Runtime record

_source line 8840 · 2026-05-20T09:38:41.536Z_

```json
{
  "parentUuid": "7954b760-c989-47e1-8c29-ba2e7f415017",
  "isSidechain": false,
  "attachment": {
    "type": "file",
    "filename": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/abstract.tex",
    "content": {
      "type": "text",
      "file": {
        "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/abstract.tex",
        "content": "Self-Consistency (SC) majority voting over chain-of-thought traces is the dominant test-time aggregation strategy for LLMs, but accuracy gains saturate as sample count grows. The Condorcet Jury Theorem (CJT) explains this plateau: same-model traces are correlated voters, so additional samples carry diminishing independent information. Symbolic constraints in first-order logic (FOL) appear to offer a way forward, but when extracted by the same model, they inherit the traces' correlation structure. We term this the \\emph{independence bottleneck}. We study it through Symbolic Invariant Consensus Aggregation (SICA), which extracts FOL constraints from reasoning traces and selects answers via weighted partial MAX-SAT. Evaluating six models (7B--32B) across three reasoning domains with over 3,000 instances and four-seed replication, we find that self-extracted constraints fail to surpass majority voting. A directional positive trend (best $+3.43$\\,pp, mean $+1.47$\\,pp; $p < 0.10$ in 2 of 4 seeds, none reaching $p < 0.05$) appears only in one model on one dataset at 50--55\\% SC baseline. Oracle controls with gold FOL confirm the aggregation mechanism is sound, yet self-extraction captures only 24\\% of the oracle ceiling. The central finding is a fundamental independence-accuracy trade-off revealed by Fleiss' $\\kappa$ generalization across aggregation methods: Debate reduces inter-trace $\\kappa$ from 0.44 to 0.15, tripling the effective sample size, but collapses accuracy by $-18.6$\\,pp on FOLIO and $-23.0$\\,pp on LogiQA. Methods that preserve accuracy cannot break the correlation floor. This trade-off constrains all same-model trace aggregation, not only symbolic approaches. The $\\kappa$-based Eff-$K$ metric quantifies SC's own scaling ceiling, and $C_0$ combined with SC accuracy provides a zero-cost deployment diagnostic. The bottleneck is structural and universal---three model families (Mistral, LLaMA, Qwen) all exhibit $\\kappa \\geq 0.41$, and no aggregation method breaks through.",
        "numLines": 1,
        "startLine": 1,
        "totalLines": 1
      }
    },
    "displayPath": "../../../docs/paper/abstract.tex"
  },
  "type": "attachment",
  "uuid": "6f5a6337-c04e-41e6-8513-68aa9fe4f8df",
  "timestamp": "2026-05-20T09:38:41.536Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora"
}
```

---


### Runtime record

_source line 8841 · 2026-05-20T09:38:41.838Z_

```json
{
  "parentUuid": "6f5a6337-c04e-41e6-8513-68aa9fe4f8df",
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
      "ListMcpResourcesTool",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "ReadMcpResourceTool",
      "RemoteTrigger",
      "TaskOutput",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__auto_build_provenance",
      "mcp__agent-ml-research__bootstrap_provenance",
      "mcp__agent-ml-research__check_figures_and_layout",
      "mcp__agent-ml-research__check_paper_consistency",
      "mcp__agent-ml-research__check_provenance_completeness",
      "mcp__agent-ml-research__cleanup_pdf_images",
      "mcp__agent-ml-research__compute_coverage_matrix",
      "mcp__agent-ml-research__edit_paper_section",
      "mcp__agent-ml-research__get_image_info",
      "mcp__agent-ml-research__get_worker_status",
      "mcp__agent-ml-research__list_artifacts",
      "mcp__agent-ml-research__list_workers",
      "mcp__agent-ml-research__load_project_config",
      "mcp__agent-ml-research__overleaf_init",
      "mcp__agent-ml-research__overleaf_pull",
      "mcp__agent-ml-research__overleaf_push",
      "mcp__agent-ml-research__overleaf_status",
      "mcp__agent-ml-research__overleaf_sync",
      "mcp__agent-ml-research__paper_agent_post_to_director",
      "mcp__agent-ml-research__paper_agent_request_review",
      "mcp__agent-ml-research__paper_compile_and_check",
      "mcp__agent-ml-research__pdf_to_images",
      "mcp__agent-ml-research__read_experiment_plan_with_status",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__read_roadmap",
      "mcp__agent-ml-research__register_artifact",
      "mcp__agent-ml-research__save_project_file",
      "mcp__agent-ml-research__send_progress",
      "mcp__agent-ml-research__spawn_worker",
      "mcp__agent-ml-research__verify_references",
      "mcp__agent-ml-research__write_paper_section"
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
      "ListMcpResourcesTool",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "ReadMcpResourceTool",
      "RemoteTrigger",
      "TaskOutput",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__auto_build_provenance",
      "mcp__agent-ml-research__bootstrap_provenance",
      "mcp__agent-ml-research__check_figures_and_layout",
      "mcp__agent-ml-research__check_paper_consistency",
      "mcp__agent-ml-research__check_provenance_completeness",
      "mcp__agent-ml-research__cleanup_pdf_images",
      "mcp__agent-ml-research__compute_coverage_matrix",
      "mcp__agent-ml-research__edit_paper_section",
      "mcp__agent-ml-research__get_image_info",
      "mcp__agent-ml-research__get_worker_status",
      "mcp__agent-ml-research__list_artifacts",
      "mcp__agent-ml-research__list_workers",
      "mcp__agent-ml-research__load_project_config",
      "mcp__agent-ml-research__overleaf_init",
      "mcp__agent-ml-research__overleaf_pull",
      "mcp__agent-ml-research__overleaf_push",
      "mcp__agent-ml-research__overleaf_status",
      "mcp__agent-ml-research__overleaf_sync",
      "mcp__agent-ml-research__paper_agent_post_to_director",
      "mcp__agent-ml-research__paper_agent_request_review",
      "mcp__agent-ml-research__paper_compile_and_check",
      "mcp__agent-ml-research__pdf_to_images",
      "mcp__agent-ml-research__read_experiment_plan_with_status",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__read_roadmap",
      "mcp__agent-ml-research__register_artifact",
      "mcp__agent-ml-research__save_project_file",
      "mcp__agent-ml-research__send_progress",
      "mcp__agent-ml-research__spawn_worker",
      "mcp__agent-ml-research__verify_references",
      "mcp__agent-ml-research__write_paper_section"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "7f4ab1de-8b29-46c7-a3e5-c50221d7a93a",
  "timestamp": "2026-05-20T09:38:41.838Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora"
}
```

---


### Runtime record

_source line 8842 · 2026-05-20T09:38:41.838Z_

```json
{
  "parentUuid": "7f4ab1de-8b29-46c7-a3e5-c50221d7a93a",
  "isSidechain": false,
  "attachment": {
    "type": "mcp_instructions_delta",
    "addedNames": [
      "agent-ml-research"
    ],
    "addedBlocks": [
      "## agent-ml-research\nML research experiment management tools"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "b60103e5-fb42-4a82-a136-4b5adbe2d385",
  "timestamp": "2026-05-20T09:38:41.838Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora"
}
```

---


### Runtime record

_source line 8843_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[服务器重启后首条消息] 当前日期: 2026-05-20。服务器刚重启，项目状态可能已更新。不要依赖对话历史中的状态信息，以 registry 当前值为准。  **用户消息：** [Director 指令] ## 写作任务：EMNLP 2026 ARR May 25 — Full Draft 更新  **DDL**: May 25, 2026（5 天） **模式**: Full Draft 更新…",
  "leafUuid": "4542ec3b-248b-4ddf-89fc-a6f8dbcc1992",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1"
}
```

---


### Runtime record

_source line 8844_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise paper results with oracle FOLIO constraint experiments",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1"
}
```

---


### Assistant

_source line 8845 · 2026-05-20T09:38:48.995Z_

<details><summary>Logged reasoning block</summary>

```text
I need to continue generating the updated `writing_plan.yaml` for Director approval. I had read the paper_framing.md and current writing_plan.yaml, but hadn't yet read the existing .tex files to assess rewrite scope. Let me read the key files I need to assess, then generate the plan.

Let me read the files I need:
1. introduction.tex - to assess rewrite scope
2. method.tex - needs new subsections for confirmation bias, process-κ
3. experiments.tex - needs expansion
4. related_work.tex - to assess scope
5. The current writing_plan.yaml again for reference


6. Registry for the new experiments

Now I'm starting to read through the files I haven't examined yet.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b60103e5-fb42-4a82-a136-4b5adbe2d385",
  "isSidechain": false,
  "requestId": "req_011CbDbcxE4dQQcv8UTbGDcc",
  "type": "assistant",
  "uuid": "0a58e933-2ccc-4e07-83ca-d9fb83fdb6ac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015y3NCLRjBVQZg7pQTXf6DC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 30791,
      "cache_read_input_tokens": 11841,
      "output_tokens": 509,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 30791,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 509,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 30791,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 30791
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

_source line 8846 · 2026-05-20T09:38:48.997Z_

Let me read the remaining .tex files to assess rewrite scope before generating the updated writing_plan.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0a58e933-2ccc-4e07-83ca-d9fb83fdb6ac",
  "isSidechain": false,
  "requestId": "req_011CbDbcxE4dQQcv8UTbGDcc",
  "type": "assistant",
  "uuid": "c506cb00-d87f-4bb7-9241-b2e176e5e9c3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015y3NCLRjBVQZg7pQTXf6DC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 30791,
      "cache_read_input_tokens": 11841,
      "output_tokens": 509,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 30791,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 509,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 30791,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 30791
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

_source line 8847 · 2026-05-20T09:38:49.012Z_

<details open><summary>🔧 Tool call — Read · `toolu_01B6qQ7AZ1QRo61geCrjSAdj`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c506cb00-d87f-4bb7-9241-b2e176e5e9c3",
  "isSidechain": false,
  "requestId": "req_011CbDbcxE4dQQcv8UTbGDcc",
  "type": "assistant",
  "uuid": "241c2d39-05ef-407f-8874-7af0e018ac65",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015y3NCLRjBVQZg7pQTXf6DC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 30791,
      "cache_read_input_tokens": 11841,
      "output_tokens": 509,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 30791,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 509,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 30791,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 30791
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

_source line 8848 · 2026-05-20T09:38:50.420Z_

<details><summary>↩ Tool result · `toolu_019T2XJmCi6RyfTXLpDJtKg4`</summary>

```text
1	\section{Related Work}
2	\label{sec:related-work}
3	
4	\paragraph{Self-Consistency and extensions.}
5	SC selects the most frequent answer across chain-of-thought traces \citep{wang2023sc}. Extensions include universal SC for free-form generation \citep{chen2024usc}, confidence weighting \citep{taubenfeld2025cisc}, diverse prompting with step-aware verification \citep{li2023diverse}, and reasoning-aware filtering \citep{wan2024rasc, kim2026reasc}. \citet{loo2025reevaluating} show that SC gains plateau early. Our Condorcet analysis explains this: $\kappa = 0.21$--$0.82$ compresses $K_{\text{eff}}$ to 1.20--3.62 for $K = 12$ (\S\ref{sec:effective-k}).
6	
7	\paragraph{Neuro-symbolic reasoning.}
8	Logic-LM \citep{pan2023logiclm} and LINC \citep{olausson2023linc} translate problems into FOL for external provers; LINC documents ${\sim}$40\% translation errors. More recent systems extend this: DyLoS \citep{xu2026dylos} selects solver types, Aristotle \citep{li2025aristotle} applies logic-complete decomposition, FoVer \citep{wang2025fover} trains FOL verifiers, and LogicAgent \citep{luo2025logicagent} employs multi-perspective grounding. Each introduces capabilities beyond the reasoning model. \citet{amonkar2025realitycheck} show that LLM formalization degrades with complexity, consistent with our findings. Our oracle controls confirm the aggregation mechanism is sound ($+14.22$\,pp FOLIO, $+11.50$\,pp ProofWriter); the failure localizes to self-extraction quality (\S\ref{sec:oracle}).
9	
10	\paragraph{Test-time compute and verification.}
11	Scaling test-time computation through additional traces \citep{snell2025scaling} faces the same correlation challenge: same-model attempts collapse into correlated solutions. Reasoning models intensify this (QwQ-32B: $C_0 = 2.6\%$). Trained verifiers offer an alternative: outcome reward models \citep{cobbe2021gsm8k}, process reward models \citep{lightman2024prm}, and Math-Shepherd \citep{wang2024mathshepherd}. Multi-agent debate refines answers through discussion \citep{liang2023encouraging, du2023improving}. Self-correction without external feedback degrades performance \citep{huang2024selfcorrect, stechly2025selfverification}, paralleling our finding.
12	
13	\paragraph{CJT and ensemble diversity.}
14	CJT \citep{condorcet1785} establishes that independent majority voting converges to truth. \citet{ladha1992correlated} prove correlated voters reduce effective ensemble size. \citet{lefort2024condorcet_llm} apply CJT to LLM ensemble classification. We extend this to reasoning-trace aggregation, measuring $\kappa$ and $K_{\text{eff}}$ across 15 conditions (\S\ref{sec:effective-k}).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "abc9a543-3323-42fa-9c2b-b4814d1af32f",
  "isSidechain": false,
  "promptId": "3f50ba00-7d30-45ec-b450-7010d531c858",
  "type": "user",
  "uuid": "2453c99b-7206-464c-8c51-758e073b5828",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/related_work.tex",
      "content": "\\section{Related Work}\n\\label{sec:related-work}\n\n\\paragraph{Self-Consistency and extensions.}\nSC selects the most frequent answer across chain-of-thought traces \\citep{wang2023sc}. Extensions include universal SC for free-form generation \\citep{chen2024usc}, confidence weighting \\citep{taubenfeld2025cisc}, diverse prompting with step-aware verification \\citep{li2023diverse}, and reasoning-aware filtering \\citep{wan2024rasc, kim2026reasc}. \\citet{loo2025reevaluating} show that SC gains plateau early. Our Condorcet analysis explains this: $\\kappa = 0.21$--$0.82$ compresses $K_{\\text{eff}}$ to 1.20--3.62 for $K = 12$ (\\S\\ref{sec:effective-k}).\n\n\\paragraph{Neuro-symbolic reasoning.}\nLogic-LM \\citep{pan2023logiclm} and LINC \\citep{olausson2023linc} translate problems into FOL for external provers; LINC documents ${\\sim}$40\\% translation errors. More recent systems extend this: DyLoS \\citep{xu2026dylos} selects solver types, Aristotle \\citep{li2025aristotle} applies logic-complete decomposition, FoVer \\citep{wang2025fover} trains FOL verifiers, and LogicAgent \\citep{luo2025logicagent} employs multi-perspective grounding. Each introduces capabilities beyond the reasoning model. \\citet{amonkar2025realitycheck} show that LLM formalization degrades with complexity, consistent with our findings. Our oracle controls confirm the aggregation mechanism is sound ($+14.22$\\,pp FOLIO, $+11.50$\\,pp ProofWriter); the failure localizes to self-extraction quality (\\S\\ref{sec:oracle}).\n\n\\paragraph{Test-time compute and verification.}\nScaling test-time computation through additional traces \\citep{snell2025scaling} faces the same correlation challenge: same-model attempts collapse into correlated solutions. Reasoning models intensify this (QwQ-32B: $C_0 = 2.6\\%$). Trained verifiers offer an alternative: outcome reward models \\citep{cobbe2021gsm8k}, process reward models \\citep{lightman2024prm}, and Math-Shepherd \\citep{wang2024mathshepherd}. Multi-agent debate refines answers through discussion \\citep{liang2023encouraging, du2023improving}. Self-correction without external feedback degrades performance \\citep{huang2024selfcorrect, stechly2025selfverification}, paralleling our finding.\n\n\\paragraph{CJT and ensemble diversity.}\nCJT \\citep{condorcet1785} establishes that independent majority voting converges to truth. \\citet{ladha1992correlated} prove correlated voters reduce effective ensemble size. \\citet{lefort2024condorcet_llm} apply CJT to LLM ensemble classification. We extend this to reasoning-trace aggregation, measuring $\\kappa$ and $K_{\\text{eff}}$ across 15 conditions (\\S\\ref{sec:effective-k}).",
      "numLines": 14,
      "startLine": 1,
      "totalLines": 14
    }
  },
  "sourceToolAssistantUUID": "abc9a543-3323-42fa-9c2b-b4814d1af32f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora"
}
```

</details>

---


### Tool result

_source line 8849 · 2026-05-20T09:38:49.032Z_

<details><summary>↩ Tool result · `toolu_01B6qQ7AZ1QRo61geCrjSAdj`</summary>

```text
1	\section{Introduction}\label{sec:introduction}
2	
3	Test-time computation scaling through multiple reasoning samples has emerged as a practical alternative to scaling model parameters \citep{snell2025scaling, guo2025deepseekr1}.
4	The dominant aggregation strategy, Self-Consistency (SC) \citep{wang2023sc}, samples $K$ chain-of-thought traces and selects the majority answer.
5	SC is simple, model-agnostic, and effective---but it is hitting a ceiling.
6	\citet{loo2025reevaluating} demonstrate that gains from increasing $K$ plateau and even decline for strong models.
7	The gap between SC's theoretical promise (independent correct voters converge to truth) and its practical behavior (saturating gains) points to a structural mismatch: same-model traces carry correlated errors, and majority voting has no mechanism to correct shared bias.
8	
9	Confidence-weighted \citep{taubenfeld2025cisc} and universal \citep{chen2024usc} extensions alleviate this to a degree, but the core limitation persists.
10	Trained reward models \citep{lightman2024prm, wang2024mathshepherd} and diversity-aware sampling \citep{diverseaware2026} break the plateau by injecting external signal, but require trained verifiers or sampling modifications.
11	A more fundamental question remains: can \emph{structured aggregation} over symbolic representations extract information from the same traces that majority voting cannot?
12	
13	Recent neuro-symbolic methods suggest that formal reasoning can complement LLM generation.
14	Logic-LM \citep{pan2023logiclm}, LINC \citep{olausson2023linc}, DyLoS \citep{xu2026dylos}, Aristotle \citep{li2025aristotle}, FoVer \citep{wang2025fover}, and LogicAgent \citep{luo2025logicagent} each report gains on logical reasoning benchmarks, but introduce components beyond the reasoning model: trained verifiers, solver selection, or external knowledge.
15	A simpler question precedes these extensions: can the \emph{same} model that generates reasoning traces also extract useful formal constraints from them?
16	Self-extraction would be a zero-cost upgrade requiring no additional model, training data, or external prover.
17	Yet no prior work has systematically evaluated whether self-extracted constraints are useful for aggregation.
18	This motivates our study of Symbolic Invariant Consensus Aggregation (SICA): extract FOL constraints from each of $K$ reasoning traces, deduplicate by syntactic equivalence, and select the answer best supported by a weighted partial MAX-SAT solution via Z3 \citep{demoura2008z3} (\S\ref{sec:pipeline}; Figure~\ref{fig:pipeline}).
19	
20	We ground our analysis in the Condorcet Jury Theorem (CJT) \citep{condorcet1785}: if $K$ independent voters each answer correctly with probability $p > 0.5$, the majority converges to truth as $K$ grows \citep{austensmith1996}.
21	When independence fails, as \citet{ladha1992correlated} show for correlated voters, additional samples carry diminishing information.
22	We measure inter-trace agreement with Fleiss' $\kappa$ \citep{fleiss1971kappa} and find values from 0.21 to 0.82 across instruction-tuned conditions (0.91 for thinking mode), yielding Eff-$K = 1.20\text{--}3.62$ for nominal $K = 12$ (\S\ref{sec:effective-k}).
23	At Eff-$K \approx 2$, traces beyond $K = 12$ add negligible independent information---a scaling ceiling that applies to SC itself, not only to symbolic aggregation.
24	When the same model both produces traces and extracts constraints, the constraints inherit the traces' biases \citep{huang2024selfcorrect, kambhampati2024position}.
25	We term this the \emph{independence bottleneck}: self-extracted constraints cannot supply the independent signal that CJT requires for aggregation to surpass SC.
26	\citet{lefort2024condorcet_llm} examine CJT violations in LLM ensembles, but no prior study connects this framework to symbolic constraint extraction.
27	
28	We evaluate SICA across six models (7B--32B), three reasoning domains (FOLIO \citep{han2022folio}, ProofWriter \citep{tafjord2021proofwriter}, LogiQA \citep{liu2020logiqa}), and over 3,000 instances with four-seed replication (Table~\ref{tab:main_results}).
29	The central finding is a fundamental independence-accuracy trade-off: $\kappa$ generalization across aggregation methods shows that Debate reduces inter-trace $\kappa$ from 0.44 to 0.15, tripling Eff-$K$, but collapses accuracy by $-18.6$\,pp on FOLIO and $-23.0$\,pp on LogiQA (\S\ref{sec:remediation}).
30	This trade-off constrains all same-model trace aggregation, not only symbolic approaches.
31	Oracle controls confirm the aggregation mechanism is sound: gold FOL yields $+14.22$\,pp on FOLIO and $+11.50$\,pp on ProofWriter ($p < 0.001$), yet self-extraction captures only 24\% of this ceiling.
32	Twelve remediation strategies (nine prompt-level, three method-level) all fail.
33	A directional positive trend occurs in one model-dataset condition (Mistral-7B on FOLIO, 2 of 4 seeds with $p < 0.10$, none reaching $p < 0.05$; best $+3.43$\,pp), but only in a narrow band around 50--55\% SC; outside it, constraints echo the majority (Type~A) or amplify errors (Type~C).
34	The bottleneck is structural at the 7B--14B scale tested; whether larger models or trained extractors can overcome it remains open.
35	
36	Our contributions are:
37	\begin{enumerate}
38	\item \textbf{Independence-Accuracy Trade-off (primary).} Fleiss' $\kappa$ generalization across four aggregation methods reveals a fundamental Pareto frontier: SC, Diverse-Prompt, and ICG cluster at $\kappa \approx 0.40$--$0.47$ (a same-model ceiling), while Debate reduces $\kappa$ to 0.15 (Eff-$K = 4.4$) but collapses accuracy by $-18.6$\,pp on FOLIO ($-23.0$\,pp on LogiQA). Twelve remediation strategies (nine prompt-level, three method-level) all fail, confirming that same-model aggregation cannot simultaneously achieve independence and accuracy (\S\ref{sec:remediation}).
39	
40	\item \textbf{Independence Bottleneck and Diagnostic Tools.} Same-model traces yield Fleiss' $\kappa = 0.21$--$0.82$ (Eff-$K = 1.20$--$3.62$ for $K = 12$), quantifying SC's own scaling ceiling: Eff-$K \approx 2$ means traces beyond $K = 12$ add negligible independent information for any aggregation method. The multi-candidate rate $C_0$ combined with SC accuracy provides a zero-cost deployment diagnostic predicting when symbolic augmentation is unlikely to help (\S\ref{sec:condorcet}, \S\ref{sec:effective-k}).
41	
42	\item \textbf{Oracle-Extraction Gap.} Oracle constraints yield $+14.22$\,pp on FOLIO and $+11.50$\,pp on ProofWriter ($p < 0.001$). Self-extraction captures only 24\% of this ceiling, localizing the failure to extraction quality, not the symbolic approach (\S\ref{sec:oracle}).
43	
44	\item \textbf{Regime-Dependent Pattern (directional).} A directional positive trend occurs in a narrow band ($\sim$50--55\% SC) in one model on one dataset (best $+3.43$\,pp, mean $+1.47$\,pp, none reaching $p < 0.05$). Three failure modes---confirmation bias, non-formalizability, error amplification---explain the regime boundaries (\S\ref{sec:main-results}).
45	\end{enumerate}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "241c2d39-05ef-407f-8874-7af0e018ac65",
  "isSidechain": false,
  "promptId": "3f50ba00-7d30-45ec-b450-7010d531c858",
  "type": "user",
  "uuid": "60038938-5bda-4d91-b4bb-9d68f5368c1d",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/introduction.tex",
      "content": "\\section{Introduction}\\label{sec:introduction}\n\nTest-time computation scaling through multiple reasoning samples has emerged as a practical alternative to scaling model parameters \\citep{snell2025scaling, guo2025deepseekr1}.\nThe dominant aggregation strategy, Self-Consistency (SC) \\citep{wang2023sc}, samples $K$ chain-of-thought traces and selects the majority answer.\nSC is simple, model-agnostic, and effective---but it is hitting a ceiling.\n\\citet{loo2025reevaluating} demonstrate that gains from increasing $K$ plateau and even decline for strong models.\nThe gap between SC's theoretical promise (independent correct voters converge to truth) and its practical behavior (saturating gains) points to a structural mismatch: same-model traces carry correlated errors, and majority voting has no mechanism to correct shared bias.\n\nConfidence-weighted \\citep{taubenfeld2025cisc} and universal \\citep{chen2024usc} extensions alleviate this to a degree, but the core limitation persists.\nTrained reward models \\citep{lightman2024prm, wang2024mathshepherd} and diversity-aware sampling \\citep{diverseaware2026} break the plateau by injecting external signal, but require trained verifiers or sampling modifications.\nA more fundamental question remains: can \\emph{structured aggregation} over symbolic representations extract information from the same traces that majority voting cannot?\n\nRecent neuro-symbolic methods suggest that formal reasoning can complement LLM generation.\nLogic-LM \\citep{pan2023logiclm}, LINC \\citep{olausson2023linc}, DyLoS \\citep{xu2026dylos}, Aristotle \\citep{li2025aristotle}, FoVer \\citep{wang2025fover}, and LogicAgent \\citep{luo2025logicagent} each report gains on logical reasoning benchmarks, but introduce components beyond the reasoning model: trained verifiers, solver selection, or external knowledge.\nA simpler question precedes these extensions: can the \\emph{same} model that generates reasoning traces also extract useful formal constraints from them?\nSelf-extraction would be a zero-cost upgrade requiring no additional model, training data, or external prover.\nYet no prior work has systematically evaluated whether self-extracted constraints are useful for aggregation.\nThis motivates our study of Symbolic Invariant Consensus Aggregation (SICA): extract FOL constraints from each of $K$ reasoning traces, deduplicate by syntactic equivalence, and select the answer best supported by a weighted partial MAX-SAT solution via Z3 \\citep{demoura2008z3} (\\S\\ref{sec:pipeline}; Figure~\\ref{fig:pipeline}).\n\nWe ground our analysis in the Condorcet Jury Theorem (CJT) \\citep{condorcet1785}: if $K$ independent voters each answer correctly with probability $p > 0.5$, the majority converges to truth as $K$ grows \\citep{austensmith1996}.\nWhen independence fails, as \\citet{ladha1992correlated} show for correlated voters, additional samples carry diminishing information.\nWe measure inter-trace agreement with Fleiss' $\\kappa$ \\citep{fleiss1971kappa} and find values from 0.21 to 0.82 across instruction-tuned conditions (0.91 for thinking mode), yielding Eff-$K = 1.20\\text{--}3.62$ for nominal $K = 12$ (\\S\\ref{sec:effective-k}).\nAt Eff-$K \\approx 2$, traces beyond $K = 12$ add negligible independent information---a scaling ceiling that applies to SC itself, not only to symbolic aggregation.\nWhen the same model both produces traces and extracts constraints, the constraints inherit the traces' biases \\citep{huang2024selfcorrect, kambhampati2024position}.\nWe term this the \\emph{independence bottleneck}: self-extracted constraints cannot supply the independent signal that CJT requires for aggregation to surpass SC.\n\\citet{lefort2024condorcet_llm} examine CJT violations in LLM ensembles, but no prior study connects this framework to symbolic constraint extraction.\n\nWe evaluate SICA across six models (7B--32B), three reasoning domains (FOLIO \\citep{han2022folio}, ProofWriter \\citep{tafjord2021proofwriter}, LogiQA \\citep{liu2020logiqa}), and over 3,000 instances with four-seed replication (Table~\\ref{tab:main_results}).\nThe central finding is a fundamental independence-accuracy trade-off: $\\kappa$ generalization across aggregation methods shows that Debate reduces inter-trace $\\kappa$ from 0.44 to 0.15, tripling Eff-$K$, but collapses accuracy by $-18.6$\\,pp on FOLIO and $-23.0$\\,pp on LogiQA (\\S\\ref{sec:remediation}).\nThis trade-off constrains all same-model trace aggregation, not only symbolic approaches.\nOracle controls confirm the aggregation mechanism is sound: gold FOL yields $+14.22$\\,pp on FOLIO and $+11.50$\\,pp on ProofWriter ($p < 0.001$), yet self-extraction captures only 24\\% of this ceiling.\nTwelve remediation strategies (nine prompt-level, three method-level) all fail.\nA directional positive trend occurs in one model-dataset condition (Mistral-7B on FOLIO, 2 of 4 seeds with $p < 0.10$, none reaching $p < 0.05$; best $+3.43$\\,pp), but only in a narrow band around 50--55\\% SC; outside it, constraints echo the majority (Type~A) or amplify errors (Type~C).\nThe bottleneck is structural at the 7B--14B scale tested; whether larger models or trained extractors can overcome it remains open.\n\nOur contributions are:\n\\begin{enumerate}\n\\item \\textbf{Independence-Accuracy Trade-off (primary).} Fleiss' $\\kappa$ generalization across four aggregation methods reveals a fundamental Pareto frontier: SC, Diverse-Prompt, and ICG cluster at $\\kappa \\approx 0.40$--$0.47$ (a same-model ceiling), while Debate reduces $\\kappa$ to 0.15 (Eff-$K = 4.4$) but collapses accuracy by $-18.6$\\,pp on FOLIO ($-23.0$\\,pp on LogiQA). Twelve remediation strategies (nine prompt-level, three method-level) all fail, confirming that same-model aggregation cannot simultaneously achieve independence and accuracy (\\S\\ref{sec:remediation}).\n\n\\item \\textbf{Independence Bottleneck and Diagnostic Tools.} Same-model traces yield Fleiss' $\\kappa = 0.21$--$0.82$ (Eff-$K = 1.20$--$3.62$ for $K = 12$), quantifying SC's own scaling ceiling: Eff-$K \\approx 2$ means traces beyond $K = 12$ add negligible independent information for any aggregation method. The multi-candidate rate $C_0$ combined with SC accuracy provides a zero-cost deployment diagnostic predicting when symbolic augmentation is unlikely to help (\\S\\ref{sec:condorcet}, \\S\\ref{sec:effective-k}).\n\n\\item \\textbf{Oracle-Extraction Gap.} Oracle constraints yield $+14.22$\\,pp on FOLIO and $+11.50$\\,pp on ProofWriter ($p < 0.001$). Self-extraction captures only 24\\% of this ceiling, localizing the failure to extraction quality, not the symbolic approach (\\S\\ref{sec:oracle}).\n\n\\item \\textbf{Regime-Dependent Pattern (directional).} A directional positive trend occurs in a narrow band ($\\sim$50--55\\% SC) in one model on one dataset (best $+3.43$\\,pp, mean $+1.47$\\,pp, none reaching $p < 0.05$). Three failure modes---confirmation bias, non-formalizability, error amplification---explain the regime boundaries (\\S\\ref{sec:main-results}).\n\\end{enumerate}",
      "numLines": 45,
      "startLine": 1,
      "totalLines": 45
    }
  },
  "sourceToolAssistantUUID": "241c2d39-05ef-407f-8874-7af0e018ac65",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora"
}
```

</details>

---


### Tool call

_source line 8850 · 2026-05-20T09:38:49.289Z_

<details open><summary>🔧 Tool call — Read · `toolu_01QiihkiWz8bwCHPiqutb6SB`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "60038938-5bda-4d91-b4bb-9d68f5368c1d",
  "isSidechain": false,
  "requestId": "req_011CbDbcxE4dQQcv8UTbGDcc",
  "type": "assistant",
  "uuid": "379f0ff5-fd19-4a76-900a-748b7fe94fd1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015y3NCLRjBVQZg7pQTXf6DC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 30791,
      "cache_read_input_tokens": 11841,
      "output_tokens": 509,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 30791,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 509,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 30791,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 30791
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

_source line 8851 · 2026-05-20T09:38:49.296Z_

<details><summary>↩ Tool result · `toolu_01QiihkiWz8bwCHPiqutb6SB`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Self-Consistency and the Condorcet Independence Assumption}
5	\label{sec:condorcet}
6	
7	Self-Consistency (SC) \citep{wang2023sc} samples $K$ reasoning traces and selects the majority answer. The Condorcet Jury Theorem (CJT) \citep{condorcet1785} guarantees that if $K$ independent voters are each correct with probability $p > 0.5$, the majority converges to truth as $K \to \infty$ \citep{austensmith1996}. LLM traces violate this independence: all $K$ samples come from the same model with only temperature as variation. Following \citet{ladha1992correlated} and the design-effect framework of \citet{kish1965survey}, we define effective sample size using Fleiss' $\kappa$ \citep{fleiss1971kappa} as proxy for intraclass correlation:
8	\begin{equation}
9	\label{eq:effk}
10	K_{\text{eff}} = \frac{K}{1 + (K - 1) \cdot \kappa}.
11	\end{equation}
12	In our experiments (\S\ref{sec:effective-k}), $\kappa$ ranges from 0.21 to 0.82 across instruction-tuned pairs (0.91 for thinking mode), yielding $K_{\text{eff}} \approx 1.2\text{--}3.6$ for $K = 12$. This \emph{independence bottleneck} motivates our investigation.
13	
14	\subsection{SICA Pipeline}
15	\label{sec:pipeline}
16	
17	Symbolic Invariant Consensus Aggregation (SICA) extends SC by extracting formal constraints from traces and selecting the answer best supported by the satisfiable subset (Figure~\ref{fig:pipeline}).
18	
19	\paragraph{Trace generation.} Given question $q$, an LLM generates $K$ traces $\{t_1, \ldots, t_K\}$ at temperature $T = 0.7$. Each trace $t_i$ yields answer $a_i$.
20	
21	\paragraph{Constraint extraction.}\label{sec:constraint-extraction} The same LLM extracts FOL constraints from each trace at $T_{\text{ext}} = 0.3$. The extraction prompt requests JSON output with constraint type, expression, and Z3-compatible formula (Appendix~\ref{app:prompts}). The \emph{extraction rate} is the fraction of traces yielding at least one parseable constraint.
22	
23	\paragraph{Deduplication and MAX-SAT.} Constraints are deduplicated by syntactic equivalence; each unique constraint $c_m$ receives weight $w_m$ equal to the number of source traces. The objective finds the largest-weight satisfiable subset:
24	\begin{equation}
25	\label{eq:maxsat}
26	\mathcal{C}^* = \arg\max_{\mathcal{S} \subseteq \mathcal{C}} \sum_{c \in \mathcal{S}} w_c \quad \text{s.t.} \quad \mathcal{S} \text{ is satisfiable.}
27	\end{equation}
28	Z3 \citep{demoura2008z3} solves this with a 10-second timeout. Answer assertion constraints ($\texttt{answer\_a} == \texttt{True}$, weight 1) ensure every candidate receives a nonzero base score, making SICA a strict generalization of SC.
29	
30	\paragraph{Scoring.} Let $\mathcal{C}^{\setminus} = \mathcal{C} \setminus \mathcal{C}^*$. Each candidate $a$ is scored by:
31	\begin{equation}
32	\label{eq:score}
33	\text{score}(a) = \sum_{c \in \mathcal{C}^*} w_c \cdot \sigma(c, a) - \alpha \sum_{c \in \mathcal{C}^{\setminus}} w_c \cdot \sigma(c, a),
34	\end{equation}
35	where $\sigma(c, a) = 1$ if $c$ was extracted from any trace producing answer $a$, and $\alpha = 0.5$. The selected answer is $a^* = \arg\max_{a} \text{score}(a)$.
36	
37	\paragraph{Degeneration under confirmation bias.} Self-extracted constraints are tightly coupled to their source answer. While ${\sim}$92\% are technically discriminative (Appendix~\ref{app:extraction}), their direction mirrors the model's answer distribution. Constraints from majority-answer traces use trace-specific variable names (56.4\% of cross-answer pairs share zero Z3 variables), so MAX-SAT retains nearly all ($|\mathcal{C}^{\setminus}| \approx 0$), and scoring degenerates to:
38	\begin{equation}
39	\label{eq:degenerate}
40	\text{score}(a) \approx \sum_{\substack{c \in \mathcal{C}^* \\ \text{source}(c) \to a}} w_c,
41	\end{equation}
42	equivalent to majority voting. The ablation in Appendix~\ref{app:ablation} confirms this empirically.
43	
44	\paragraph{The $C_0$ diagnostic.} The multi-candidate rate $C_0$ (fraction of questions with $>1$ distinct answer) is a zero-cost diagnostic computable before extraction. When $C_0 < 5\%$, SICA produces the same output as SC.
45	\begin{equation}
46	\label{eq:c0-def}
47	C_0 = \frac{|\{q \in \mathcal{Q} : |\mathcal{A}(q)| > 1\}|}{|\mathcal{Q}|}.
48	\end{equation}
49	
50	\begin{figure}[t]
51	\centering
52	\small
53	\begin{tikzpicture}[
54	    node distance=0.4cm and 0.35cm,
55	    box/.style={draw, rounded corners=2pt, minimum height=0.6cm,
56	                text width=1.6cm, align=center, font=\scriptsize},
57	    arr/.style={-{Stealth[length=4pt]}, thick},
58	    darr/.style={-{Stealth[length=4pt]}, thick, densely dashed},
59	    lbl/.style={font=\scriptsize, text=gray!70!black},
60	    ibottle/.style={draw=red!70!black, densely dashed, rounded corners=3pt,
61	                    inner sep=3pt},
62	]
63	\node[box] (q) {Question $q$};
64	\node[box, right=of q] (sample) {Sample $K$\\traces};
65	\node[box, right=of sample] (extract) {Extract FOL\\constraints};
66	\node[box, right=of extract] (dedup) {Dedup.\ +\\weight};
67	\node[box, right=of dedup] (maxsat) {MAX-SAT\\(Z3)};
68	
69	\node[box, below=0.7cm of maxsat, fill=gray!12] (ans) {Answer $a^*$};
70	\node[box, below=0.7cm of sample, fill=gray!12] (sc) {Majority\\vote};
71	
72	\draw[arr] (q) -- (sample);
73	\draw[arr] (sample) -- (extract);
74	\draw[arr] (extract) -- (dedup);
75	\draw[arr] (dedup) -- (maxsat);
76	\draw[arr] (maxsat) -- (ans);
77	\draw[arr] (sample) -- node[lbl, right, yshift=0pt] {SC} (sc);
78	
79	\node[lbl, above=0.01cm of maxsat] {SICA};
80	
81	\node[ibottle, fit=(sample)(extract), label={[font=\scriptsize\itshape, text=red!70!black]above:Independence Bottleneck}] {};
82	
83	\draw[darr, gray!60] ([xshift=-0.1cm]dedup.south) -- ++(0,-0.35) node[lbl, below, yshift=-0.05cm] {oracle: gold FOL};
84	\end{tikzpicture}
85	\caption{The SICA pipeline. SC selects the majority answer from $K$ traces. SICA extracts FOL constraints, deduplicates, and solves MAX-SAT via Z3. Red dashed box: the independence bottleneck. Dashed arrow: oracle variant with gold FOL.}
86	\label{fig:pipeline}
87	\end{figure}
88	
89	\subsection{Oracle Control Design}
90	\label{sec:oracle-design}
91	
92	To isolate whether the bottleneck lies in extraction or aggregation, we introduce an oracle control, following the compositionality-gap methodology of \citet{press2023compositionality}. Gold FOL annotations (FOLIO) or DSL rules (ProofWriter) replace self-extracted constraints; Z3 evaluates them against each candidate answer, with scoring unchanged (Eq.~\ref{eq:score}). If the oracle produces large gains while self-extraction does not, the failure localizes to extraction quality. Results appear in \S\ref{sec:oracle}.
93	
94	\subsection{Scope}
95	\label{sec:scope}
96	
97	SICA uses \emph{same-model self-extraction}: the same LLM generates traces and extracts constraints. We test twelve remediation strategies: nine prompt-level spanning six dimensions and three method-level (ICG, Contrastive, Debate) targeting the independence bottleneck (\S\ref{sec:remediation}). Methods using trained extractors, external provers, or multi-model ensembles fall outside scope.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "379f0ff5-fd19-4a76-900a-748b7fe94fd1",
  "isSidechain": false,
  "promptId": "3f50ba00-7d30-45ec-b450-7010d531c858",
  "type": "user",
  "uuid": "7769816a-52cf-46b3-a10d-cf83d802b061",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/method.tex",
      "content": "\\section{Method}\n\\label{sec:method}\n\n\\subsection{Self-Consistency and the Condorcet Independence Assumption}\n\\label{sec:condorcet}\n\nSelf-Consistency (SC) \\citep{wang2023sc} samples $K$ reasoning traces and selects the majority answer. The Condorcet Jury Theorem (CJT) \\citep{condorcet1785} guarantees that if $K$ independent voters are each correct with probability $p > 0.5$, the majority converges to truth as $K \\to \\infty$ \\citep{austensmith1996}. LLM traces violate this independence: all $K$ samples come from the same model with only temperature as variation. Following \\citet{ladha1992correlated} and the design-effect framework of \\citet{kish1965survey}, we define effective sample size using Fleiss' $\\kappa$ \\citep{fleiss1971kappa} as proxy for intraclass correlation:\n\\begin{equation}\n\\label{eq:effk}\nK_{\\text{eff}} = \\frac{K}{1 + (K - 1) \\cdot \\kappa}.\n\\end{equation}\nIn our experiments (\\S\\ref{sec:effective-k}), $\\kappa$ ranges from 0.21 to 0.82 across instruction-tuned pairs (0.91 for thinking mode), yielding $K_{\\text{eff}} \\approx 1.2\\text{--}3.6$ for $K = 12$. This \\emph{independence bottleneck} motivates our investigation.\n\n\\subsection{SICA Pipeline}\n\\label{sec:pipeline}\n\nSymbolic Invariant Consensus Aggregation (SICA) extends SC by extracting formal constraints from traces and selecting the answer best supported by the satisfiable subset (Figure~\\ref{fig:pipeline}).\n\n\\paragraph{Trace generation.} Given question $q$, an LLM generates $K$ traces $\\{t_1, \\ldots, t_K\\}$ at temperature $T = 0.7$. Each trace $t_i$ yields answer $a_i$.\n\n\\paragraph{Constraint extraction.}\\label{sec:constraint-extraction} The same LLM extracts FOL constraints from each trace at $T_{\\text{ext}} = 0.3$. The extraction prompt requests JSON output with constraint type, expression, and Z3-compatible formula (Appendix~\\ref{app:prompts}). The \\emph{extraction rate} is the fraction of traces yielding at least one parseable constraint.\n\n\\paragraph{Deduplication and MAX-SAT.} Constraints are deduplicated by syntactic equivalence; each unique constraint $c_m$ receives weight $w_m$ equal to the number of source traces. The objective finds the largest-weight satisfiable subset:\n\\begin{equation}\n\\label{eq:maxsat}\n\\mathcal{C}^* = \\arg\\max_{\\mathcal{S} \\subseteq \\mathcal{C}} \\sum_{c \\in \\mathcal{S}} w_c \\quad \\text{s.t.} \\quad \\mathcal{S} \\text{ is satisfiable.}\n\\end{equation}\nZ3 \\citep{demoura2008z3} solves this with a 10-second timeout. Answer assertion constraints ($\\texttt{answer\\_a} == \\texttt{True}$, weight 1) ensure every candidate receives a nonzero base score, making SICA a strict generalization of SC.\n\n\\paragraph{Scoring.} Let $\\mathcal{C}^{\\setminus} = \\mathcal{C} \\setminus \\mathcal{C}^*$. Each candidate $a$ is scored by:\n\\begin{equation}\n\\label{eq:score}\n\\text{score}(a) = \\sum_{c \\in \\mathcal{C}^*} w_c \\cdot \\sigma(c, a) - \\alpha \\sum_{c \\in \\mathcal{C}^{\\setminus}} w_c \\cdot \\sigma(c, a),\n\\end{equation}\nwhere $\\sigma(c, a) = 1$ if $c$ was extracted from any trace producing answer $a$, and $\\alpha = 0.5$. The selected answer is $a^* = \\arg\\max_{a} \\text{score}(a)$.\n\n\\paragraph{Degeneration under confirmation bias.} Self-extracted constraints are tightly coupled to their source answer. While ${\\sim}$92\\% are technically discriminative (Appendix~\\ref{app:extraction}), their direction mirrors the model's answer distribution. Constraints from majority-answer traces use trace-specific variable names (56.4\\% of cross-answer pairs share zero Z3 variables), so MAX-SAT retains nearly all ($|\\mathcal{C}^{\\setminus}| \\approx 0$), and scoring degenerates to:\n\\begin{equation}\n\\label{eq:degenerate}\n\\text{score}(a) \\approx \\sum_{\\substack{c \\in \\mathcal{C}^* \\\\ \\text{source}(c) \\to a}} w_c,\n\\end{equation}\nequivalent to majority voting. The ablation in Appendix~\\ref{app:ablation} confirms this empirically.\n\n\\paragraph{The $C_0$ diagnostic.} The multi-candidate rate $C_0$ (fraction of questions with $>1$ distinct answer) is a zero-cost diagnostic computable before extraction. When $C_0 < 5\\%$, SICA produces the same output as SC.\n\\begin{equation}\n\\label{eq:c0-def}\nC_0 = \\frac{|\\{q \\in \\mathcal{Q} : |\\mathcal{A}(q)| > 1\\}|}{|\\mathcal{Q}|}.\n\\end{equation}\n\n\\begin{figure}[t]\n\\centering\n\\small\n\\begin{tikzpicture}[\n    node distance=0.4cm and 0.35cm,\n    box/.style={draw, rounded corners=2pt, minimum height=0.6cm,\n                text width=1.6cm, align=center, font=\\scriptsize},\n    arr/.style={-{Stealth[length=4pt]}, thick},\n    darr/.style={-{Stealth[length=4pt]}, thick, densely dashed},\n    lbl/.style={font=\\scriptsize, text=gray!70!black},\n    ibottle/.style={draw=red!70!black, densely dashed, rounded corners=3pt,\n                    inner sep=3pt},\n]\n\\node[box] (q) {Question $q$};\n\\node[box, right=of q] (sample) {Sample $K$\\\\traces};\n\\node[box, right=of sample] (extract) {Extract FOL\\\\constraints};\n\\node[box, right=of extract] (dedup) {Dedup.\\ +\\\\weight};\n\\node[box, right=of dedup] (maxsat) {MAX-SAT\\\\(Z3)};\n\n\\node[box, below=0.7cm of maxsat, fill=gray!12] (ans) {Answer $a^*$};\n\\node[box, below=0.7cm of sample, fill=gray!12] (sc) {Majority\\\\vote};\n\n\\draw[arr] (q) -- (sample);\n\\draw[arr] (sample) -- (extract);\n\\draw[arr] (extract) -- (dedup);\n\\draw[arr] (dedup) -- (maxsat);\n\\draw[arr] (maxsat) -- (ans);\n\\draw[arr] (sample) -- node[lbl, right, yshift=0pt] {SC} (sc);\n\n\\node[lbl, above=0.01cm of maxsat] {SICA};\n\n\\node[ibottle, fit=(sample)(extract), label={[font=\\scriptsize\\itshape, text=red!70!black]above:Independence Bottleneck}] {};\n\n\\draw[darr, gray!60] ([xshift=-0.1cm]dedup.south) -- ++(0,-0.35) node[lbl, below, yshift=-0.05cm] {oracle: gold FOL};\n\\end{tikzpicture}\n\\caption{The SICA pipeline. SC selects the majority answer from $K$ traces. SICA extracts FOL constraints, deduplicates, and solves MAX-SAT via Z3. Red dashed box: the independence bottleneck. Dashed arrow: oracle variant with gold FOL.}\n\\label{fig:pipeline}\n\\end{figure}\n\n\\subsection{Oracle Control Design}\n\\label{sec:oracle-design}\n\nTo isolate whether the bottleneck lies in extraction or aggregation, we introduce an oracle control, following the compositionality-gap methodology of \\citet{press2023compositionality}. Gold FOL annotations (FOLIO) or DSL rules (ProofWriter) replace self-extracted constraints; Z3 evaluates them against each candidate answer, with scoring unchanged (Eq.~\\ref{eq:score}). If the oracle produces large gains while self-extraction does not, the failure localizes to extraction quality. Results appear in \\S\\ref{sec:oracle}.\n\n\\subsection{Scope}\n\\label{sec:scope}\n\nSICA uses \\emph{same-model self-extraction}: the same LLM generates traces and extracts constraints. We test twelve remediation strategies: nine prompt-level spanning six dimensions and three method-level (ICG, Contrastive, Debate) targeting the independence bottleneck (\\S\\ref{sec:remediation}). Methods using trained extractors, external provers, or multi-model ensembles fall outside scope.",
      "numLines": 97,
      "startLine": 1,
      "totalLines": 97
    }
  },
  "sourceToolAssistantUUID": "379f0ff5-fd19-4a76-900a-748b7fe94fd1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora"
}
```

</details>

---


### Tool call

_source line 8852 · 2026-05-20T09:38:50.291Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Mt9mbMUUXKnniBWrUPPnBd`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7769816a-52cf-46b3-a10d-cf83d802b061",
  "isSidechain": false,
  "requestId": "req_011CbDbcxE4dQQcv8UTbGDcc",
  "type": "assistant",
  "uuid": "021f66fd-76a5-4025-aaaa-2e52e70c30db",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015y3NCLRjBVQZg7pQTXf6DC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 30791,
      "cache_read_input_tokens": 11841,
      "output_tokens": 509,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 30791,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 509,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 30791,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 30791
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

_source line 8853 · 2026-05-20T09:38:50.295Z_

<details><summary>↩ Tool result · `toolu_01Mt9mbMUUXKnniBWrUPPnBd`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Setup}
5	\label{sec:exp-setup}
6	
7	We evaluate SICA against Self-Consistency (SC) across six models on three reasoning domains with over 3,000 instances.
8	
9	\paragraph{Models.} Qwen2.5-14B-Instruct, Qwen2.5-7B-Instruct, Qwen3-14B (non-thinking mode)~\citep{yang2024qwen25}, Mistral-7B-Instruct-v0.3~\citep{jiang2023mistral}, LLaMA-3.1-8B-Instruct~\citep{dubey2024llama3}, and QwQ-32B~\citep{qwen2024qwq} (7B--32B parameters).
10	
11	\paragraph{Datasets.} FOLIO~\citep{han2022folio} ($n{=}204$, with gold FOL annotations), ProofWriter depth-5~\citep{tafjord2021proofwriter} ($n{=}600$), LogiQA~\citep{liu2020logiqa} ($n{=}200$). StrategyQA~\citep{geva2021strategyqa} ($n{=}200$) serves as a domain-formalizability diagnostic. GSM8K~\citep{cobbe2021gsm8k} ($n{=}30$) and AIME 2024 ($n{=}22$) probe the degenerate regime ($C_0 < 5\%$).
12	
13	\paragraph{Parameters.} $K{=}12$ traces at $T{=}0.7$; extraction at $T_{\text{ext}}{=}0.3$. Z3 timeout: 10s. $\alpha{=}0.5$. Statistical significance via McNemar exact test ($\alpha{=}0.05$); 95\% bootstrap CIs from 10,000 resamples for $n \geq 200$.
14	
15	
16	\subsection{Main Results}
17	\label{sec:main-results}
18	
19	Table~\ref{tab:main_results} reports accuracy across all conditions sorted by SC baseline. SICA effectiveness depends sharply on the accuracy regime.
20	
21	\begin{table*}[t]
22	\centering
23	\small
24	\caption{SICA vs.\ SC across all conditions sorted by SC accuracy. $\Delta$ = SICA $-$ SC (pp). $^b$In-context learning with gold FOL examples. $\dagger$\,$n < 100$ (suggestive only). \textbf{Bold $\Delta$}: $p < 0.05$ (McNemar). {*}\,$p < 0.05$;\enspace{**}\,$p < 0.01$;\enspace{***}\,$p < 0.001$. Failure modes detailed in Appendix~\ref{app:failure-modes}.}
25	\label{tab:main_results}
26	\begin{tabular}{@{}llrrrrl@{}}
27	\toprule
28	Model & Domain & $n$ & SC (\%) & SICA (\%) & $\Delta$ (pp) & $p$ \\
29	\midrule
30	\multicolumn{7}{l}{\textit{Type C: error amplification (SC $\leq$ 40\%)}} \\
31	Mistral-7B & PW-D5 & 600 & 39.33 & 36.50 & $\mathbf{-2.83}$ & 0.014{*} \\
32	\midrule
33	\multicolumn{7}{l}{\textit{Intermediate SC (SC $\sim$50--55\%, Mistral-7B only)}} \\
34	Mistral-7B & LogiQA & 200 & 51.00 & 51.50 & $+$0.50 & 1.000 \\
35	Mistral-7B & FOLIO (s123) & 204 & 54.41 & 57.35 & $+$2.94 & 0.070 \\
36	Mistral-7B & FOLIO (s42) & 204 & 55.88 & \textbf{59.31} & $+$3.43 & 0.092 \\
37	Mistral-7B & FOLIO (s456) & 204 & 55.88 & 55.88 & 0.00 & 1.000 \\
38	Mistral-7B & FOLIO (s789) & 204 & 54.41 & 53.92 & $-$0.49 & 1.000 \\
39	\midrule
40	\multicolumn{7}{l}{\textit{Type A: confirmation bias (SC $\geq$ 60\%)}} \\
41	LLaMA-3.1-8B & FOLIO & 204 & 66.18 & 61.76 & $-$4.41 & 0.093 \\
42	LLaMA-3.1-8B & StrategyQA & 200 & 72.00 & 74.00 & $+$2.00 & 0.424 \\
43	Qwen2.5-14B & FOLIO (ICL)$^b$ & 199 & 74.37 & 74.87 & $+$0.50 & 1.000 \\
44	Qwen2.5-14B & PW-D5 & 600 & 75.17 & 72.67 & $\mathbf{-2.50}$ & 0.011{*} \\
45	Qwen2.5-14B & FOLIO & 204 & 75.49 & 74.51 & $-$0.98 & 1.000 \\
46	Qwen2.5-7B & FOLIO & 204 & 75.98 & 76.47 & $+$0.49 & 1.000 \\
47	Qwen2.5-14B & LogiQA & 200 & 78.50 & 78.00 & $-$0.50 & 1.000 \\
48	Qwen3-14B & FOLIO & 204 & 84.80 & \textbf{84.31} & $-$0.49 & 1.000 \\
49	Qwen3-14B & PW-D5 & 600 & 85.00 & 85.67 & $+$0.67 & 1.000 \\
50	\midrule
51	\multicolumn{7}{l}{\textit{Degenerate ($C_0 < 5\%$)}} \\
52	QwQ-32B & AIME 2024$^\dagger$ & 22 & 72.70 & 72.70 & 0.00 & \textrm{---} \\
53	Qwen2.5-14B & GSM8K$^\dagger$ & 30 & 96.67 & 96.67 & 0.00 & \textrm{---} \\
54	\midrule
55	\multicolumn{7}{l}{\textit{Oracle upper bound (gold FOL/DSL + Z3)}} \\
56	Qwen2.5-14B & FOLIO & 204 & 75.49 & \textbf{89.71} & $\mathbf{+14.22}$ & $2.0{\times}10^{-7}${***} \\
57	Qwen2.5-14B & ProofWriter & 600 & 75.17 & \textbf{86.67} & $\mathbf{+11.50}$ & $9.21{\times}10^{-15}${***} \\
58	\bottomrule
59	\end{tabular}
60	\end{table*}
61	
62	\paragraph{Intermediate-SC region.} Mistral-7B on FOLIO (SC $\sim$50--55\%) shows positive directional trends in 2 of 4 seeds: $\Delta = +3.43$\,pp ($p = 0.092$) and $+2.94$\,pp ($p = 0.070$); the remaining seeds show null or negative results. No seed reaches $p < 0.05$; the 4-seed mean is $+1.47$\,pp. Mistral-7B on LogiQA, despite the same SC range, yields only $\Delta = +0.50$\,pp ($p = 1.0$), attributable to domain formalizability (Appendix~\ref{app:failure-modes}).
63	
64	\paragraph{Type A (SC $\geq$ 60\%): confirmation bias.} Nine conditions with SC $\geq 63\%$ (combined $N > 2{,}800$) produce no significant positive effects. Qwen2.5-14B on ProofWriter shows significant degradation ($\Delta = -2.50$\,pp, $p = 0.011$). Even in-context learning with gold FOL examples ($\Delta = +0.50$\,pp, n.s.) cannot break confirmation bias.
65	
66	\paragraph{Type C (SC $\leq$ 40\%): error amplification.} Mistral-7B on ProofWriter ($n = 600$, SC $= 39.33\%$) shows $\Delta = -2.83$\,pp ($p = 0.014$): SICA \emph{significantly hurts} by formalizing incorrect reasoning.
67	
68	\paragraph{Degenerate cases.} When $C_0 < 5\%$, nearly all traces agree and SICA reduces to SC by construction.
69	
70	Figure~\ref{fig:regime-scatter} visualizes the regime dependence: the intermediate-SC region is narrow and observed only for Mistral-7B on FOLIO.
71	
72	\begin{figure}[t]
73	\centering
74	\includegraphics[width=\columnwidth]{f2_regime_scatter}
75	\caption{SICA $\Delta$ (pp) vs.\ SC baseline. Filled: $n \geq 100$; open: $n < 100$. The intermediate-SC region (50--55\%, shaded) contains the only positive trends (none reaching $p < 0.05$). Type~C: significant degradation ($p = 0.014$).}
76	\label{fig:regime-scatter}
77	\end{figure}
78	
79	
80	\subsection{Oracle Control}
81	\label{sec:oracle}
82	
83	Oracle variants replace self-extracted constraints with gold annotations: FOL from FOLIO ($n = 204$) and DSL from ProofWriter ($n = 600$). Oracle-SICA achieves 89.71\% on FOLIO ($\Delta = +14.22$\,pp, $p = 2.0 \times 10^{-7}$) and 86.67\% on ProofWriter ($\Delta = +11.50$\,pp, $p = 9.21 \times 10^{-15}$). Z3 agrees with gold labels on 95.1\% (FOLIO) and 97.1\% (ProofWriter) of problems.
84	
85	These results establish that the MAX-SAT mechanism is sound given discriminative constraints. Mistral-7B's best self-extracted result ($+3.43$\,pp) captures only 24.1\% of the FOLIO oracle ceiling. The remaining 75.9\% is lost to self-extraction quality.
86	
87	
88	\subsection{Four-Seed Replication}
89	\label{sec:replication}
90	
91	We replicate the intermediate-SC result with four seeds on Mistral-7B FOLIO ($n = 204$, $K = 12$, $T = 0.7$). Effects range from $+3.43$ to $-0.49$\,pp (mean $+1.47$\,pp); 2 of 4 seeds show marginal trends ($p < 0.10$), none reaches $p < 0.05$. Seeds~42 and~456 share identical SC baselines (55.88\%) yet produce different outcomes ($+3.43$ vs.\ $0.00$\,pp), indicating that seed-level constraint quality---not SC level alone---drives the effect. The entropy decomposition in Appendix~\ref{app:entropy} confirms that the aggregate $\Delta$ is driven by high-entropy problems: seed~42 achieves $+12.8$\,pp on this partition while seed~456 shows $-1.3$\,pp.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "021f66fd-76a5-4025-aaaa-2e52e70c30db",
  "isSidechain": false,
  "promptId": "3f50ba00-7d30-45ec-b450-7010d531c858",
  "type": "user",
  "uuid": "86bb60f9-f1f4-4a3e-83cf-4f0c487584a6",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/experiments.tex",
      "content": "\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Setup}\n\\label{sec:exp-setup}\n\nWe evaluate SICA against Self-Consistency (SC) across six models on three reasoning domains with over 3,000 instances.\n\n\\paragraph{Models.} Qwen2.5-14B-Instruct, Qwen2.5-7B-Instruct, Qwen3-14B (non-thinking mode)~\\citep{yang2024qwen25}, Mistral-7B-Instruct-v0.3~\\citep{jiang2023mistral}, LLaMA-3.1-8B-Instruct~\\citep{dubey2024llama3}, and QwQ-32B~\\citep{qwen2024qwq} (7B--32B parameters).\n\n\\paragraph{Datasets.} FOLIO~\\citep{han2022folio} ($n{=}204$, with gold FOL annotations), ProofWriter depth-5~\\citep{tafjord2021proofwriter} ($n{=}600$), LogiQA~\\citep{liu2020logiqa} ($n{=}200$). StrategyQA~\\citep{geva2021strategyqa} ($n{=}200$) serves as a domain-formalizability diagnostic. GSM8K~\\citep{cobbe2021gsm8k} ($n{=}30$) and AIME 2024 ($n{=}22$) probe the degenerate regime ($C_0 < 5\\%$).\n\n\\paragraph{Parameters.} $K{=}12$ traces at $T{=}0.7$; extraction at $T_{\\text{ext}}{=}0.3$. Z3 timeout: 10s. $\\alpha{=}0.5$. Statistical significance via McNemar exact test ($\\alpha{=}0.05$); 95\\% bootstrap CIs from 10,000 resamples for $n \\geq 200$.\n\n\n\\subsection{Main Results}\n\\label{sec:main-results}\n\nTable~\\ref{tab:main_results} reports accuracy across all conditions sorted by SC baseline. SICA effectiveness depends sharply on the accuracy regime.\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{SICA vs.\\ SC across all conditions sorted by SC accuracy. $\\Delta$ = SICA $-$ SC (pp). $^b$In-context learning with gold FOL examples. $\\dagger$\\,$n < 100$ (suggestive only). \\textbf{Bold $\\Delta$}: $p < 0.05$ (McNemar). {*}\\,$p < 0.05$;\\enspace{**}\\,$p < 0.01$;\\enspace{***}\\,$p < 0.001$. Failure modes detailed in Appendix~\\ref{app:failure-modes}.}\n\\label{tab:main_results}\n\\begin{tabular}{@{}llrrrrl@{}}\n\\toprule\nModel & Domain & $n$ & SC (\\%) & SICA (\\%) & $\\Delta$ (pp) & $p$ \\\\\n\\midrule\n\\multicolumn{7}{l}{\\textit{Type C: error amplification (SC $\\leq$ 40\\%)}} \\\\\nMistral-7B & PW-D5 & 600 & 39.33 & 36.50 & $\\mathbf{-2.83}$ & 0.014{*} \\\\\n\\midrule\n\\multicolumn{7}{l}{\\textit{Intermediate SC (SC $\\sim$50--55\\%, Mistral-7B only)}} \\\\\nMistral-7B & LogiQA & 200 & 51.00 & 51.50 & $+$0.50 & 1.000 \\\\\nMistral-7B & FOLIO (s123) & 204 & 54.41 & 57.35 & $+$2.94 & 0.070 \\\\\nMistral-7B & FOLIO (s42) & 204 & 55.88 & \\textbf{59.31} & $+$3.43 & 0.092 \\\\\nMistral-7B & FOLIO (s456) & 204 & 55.88 & 55.88 & 0.00 & 1.000 \\\\\nMistral-7B & FOLIO (s789) & 204 & 54.41 & 53.92 & $-$0.49 & 1.000 \\\\\n\\midrule\n\\multicolumn{7}{l}{\\textit{Type A: confirmation bias (SC $\\geq$ 60\\%)}} \\\\\nLLaMA-3.1-8B & FOLIO & 204 & 66.18 & 61.76 & $-$4.41 & 0.093 \\\\\nLLaMA-3.1-8B & StrategyQA & 200 & 72.00 & 74.00 & $+$2.00 & 0.424 \\\\\nQwen2.5-14B & FOLIO (ICL)$^b$ & 199 & 74.37 & 74.87 & $+$0.50 & 1.000 \\\\\nQwen2.5-14B & PW-D5 & 600 & 75.17 & 72.67 & $\\mathbf{-2.50}$ & 0.011{*} \\\\\nQwen2.5-14B & FOLIO & 204 & 75.49 & 74.51 & $-$0.98 & 1.000 \\\\\nQwen2.5-7B & FOLIO & 204 & 75.98 & 76.47 & $+$0.49 & 1.000 \\\\\nQwen2.5-14B & LogiQA & 200 & 78.50 & 78.00 & $-$0.50 & 1.000 \\\\\nQwen3-14B & FOLIO & 204 & 84.80 & \\textbf{84.31} & $-$0.49 & 1.000 \\\\\nQwen3-14B & PW-D5 & 600 & 85.00 & 85.67 & $+$0.67 & 1.000 \\\\\n\\midrule\n\\multicolumn{7}{l}{\\textit{Degenerate ($C_0 < 5\\%$)}} \\\\\nQwQ-32B & AIME 2024$^\\dagger$ & 22 & 72.70 & 72.70 & 0.00 & \\textrm{---} \\\\\nQwen2.5-14B & GSM8K$^\\dagger$ & 30 & 96.67 & 96.67 & 0.00 & \\textrm{---} \\\\\n\\midrule\n\\multicolumn{7}{l}{\\textit{Oracle upper bound (gold FOL/DSL + Z3)}} \\\\\nQwen2.5-14B & FOLIO & 204 & 75.49 & \\textbf{89.71} & $\\mathbf{+14.22}$ & $2.0{\\times}10^{-7}${***} \\\\\nQwen2.5-14B & ProofWriter & 600 & 75.17 & \\textbf{86.67} & $\\mathbf{+11.50}$ & $9.21{\\times}10^{-15}${***} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\paragraph{Intermediate-SC region.} Mistral-7B on FOLIO (SC $\\sim$50--55\\%) shows positive directional trends in 2 of 4 seeds: $\\Delta = +3.43$\\,pp ($p = 0.092$) and $+2.94$\\,pp ($p = 0.070$); the remaining seeds show null or negative results. No seed reaches $p < 0.05$; the 4-seed mean is $+1.47$\\,pp. Mistral-7B on LogiQA, despite the same SC range, yields only $\\Delta = +0.50$\\,pp ($p = 1.0$), attributable to domain formalizability (Appendix~\\ref{app:failure-modes}).\n\n\\paragraph{Type A (SC $\\geq$ 60\\%): confirmation bias.} Nine conditions with SC $\\geq 63\\%$ (combined $N > 2{,}800$) produce no significant positive effects. Qwen2.5-14B on ProofWriter shows significant degradation ($\\Delta = -2.50$\\,pp, $p = 0.011$). Even in-context learning with gold FOL examples ($\\Delta = +0.50$\\,pp, n.s.) cannot break confirmation bias.\n\n\\paragraph{Type C (SC $\\leq$ 40\\%): error amplification.} Mistral-7B on ProofWriter ($n = 600$, SC $= 39.33\\%$) shows $\\Delta = -2.83$\\,pp ($p = 0.014$): SICA \\emph{significantly hurts} by formalizing incorrect reasoning.\n\n\\paragraph{Degenerate cases.} When $C_0 < 5\\%$, nearly all traces agree and SICA reduces to SC by construction.\n\nFigure~\\ref{fig:regime-scatter} visualizes the regime dependence: the intermediate-SC region is narrow and observed only for Mistral-7B on FOLIO.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{f2_regime_scatter}\n\\caption{SICA $\\Delta$ (pp) vs.\\ SC baseline. Filled: $n \\geq 100$; open: $n < 100$. The intermediate-SC region (50--55\\%, shaded) contains the only positive trends (none reaching $p < 0.05$). Type~C: significant degradation ($p = 0.014$).}\n\\label{fig:regime-scatter}\n\\end{figure}\n\n\n\\subsection{Oracle Control}\n\\label{sec:oracle}\n\nOracle variants replace self-extracted constraints with gold annotations: FOL from FOLIO ($n = 204$) and DSL from ProofWriter ($n = 600$). Oracle-SICA achieves 89.71\\% on FOLIO ($\\Delta = +14.22$\\,pp, $p = 2.0 \\times 10^{-7}$) and 86.67\\% on ProofWriter ($\\Delta = +11.50$\\,pp, $p = 9.21 \\times 10^{-15}$). Z3 agrees with gold labels on 95.1\\% (FOLIO) and 97.1\\% (ProofWriter) of problems.\n\nThese results establish that the MAX-SAT mechanism is sound given discriminative constraints. Mistral-7B's best self-extracted result ($+3.43$\\,pp) captures only 24.1\\% of the FOLIO oracle ceiling. The remaining 75.9\\% is lost to self-extraction quality.\n\n\n\\subsection{Four-Seed Replication}\n\\label{sec:replication}\n\nWe replicate the intermediate-SC result with four seeds on Mistral-7B FOLIO ($n = 204$, $K = 12$, $T = 0.7$). Effects range from $+3.43$ to $-0.49$\\,pp (mean $+1.47$\\,pp); 2 of 4 seeds show marginal trends ($p < 0.10$), none reaches $p < 0.05$. Seeds~42 and~456 share identical SC baselines (55.88\\%) yet produce different outcomes ($+3.43$ vs.\\ $0.00$\\,pp), indicating that seed-level constraint quality---not SC level alone---drives the effect. The entropy decomposition in Appendix~\\ref{app:entropy} confirms that the aggregate $\\Delta$ is driven by high-entropy problems: seed~42 achieves $+12.8$\\,pp on this partition while seed~456 shows $-1.3$\\,pp.",
      "numLines": 91,
      "startLine": 1,
      "totalLines": 91
    }
  },
  "sourceToolAssistantUUID": "021f66fd-76a5-4025-aaaa-2e52e70c30db",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora"
}
```

</details>

---


### Tool call

_source line 8854 · 2026-05-20T09:38:50.416Z_

<details open><summary>🔧 Tool call — Read · `toolu_019T2XJmCi6RyfTXLpDJtKg4`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "86bb60f9-f1f4-4a3e-83cf-4f0c487584a6",
  "isSidechain": false,
  "requestId": "req_011CbDbcxE4dQQcv8UTbGDcc",
  "type": "assistant",
  "uuid": "abc9a543-3323-42fa-9c2b-b4814d1af32f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015y3NCLRjBVQZg7pQTXf6DC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 30791,
      "cache_read_input_tokens": 11841,
      "output_tokens": 509,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 30791,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 509,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 30791,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 30791
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

_source line 8855_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[服务器重启后首条消息] 当前日期: 2026-05-20。服务器刚重启，项目状态可能已更新。不要依赖对话历史中的状态信息，以 registry 当前值为准。  **用户消息：** [Director 指令] ## 写作任务：EMNLP 2026 ARR May 25 — Full Draft 更新  **DDL**: May 25, 2026（5 天） **模式**: Full Draft 更新…",
  "leafUuid": "2453c99b-7206-464c-8c51-758e073b5828",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1"
}
```

---


### Runtime record

_source line 8856_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise paper results with oracle FOLIO constraint experiments",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1"
}
```

---


### Assistant

_source line 8857 · 2026-05-20T09:38:55.875Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a comprehensive understanding of all the current .tex files. Let me also read the paper_framing.md (D085) to understand the new narrative, and the registry for the new experiments.

Actually, from the summary, I know the key points of the paper_framing.md (D085 final narrative with 8 claims). Let me read it to get the exact details needed for the writing plan.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2453c99b-7206-464c-8c51-758e073b5828",
  "isSidechain": false,
  "requestId": "req_011CbDbdZoThCZZs8GKFR7bs",
  "type": "assistant",
  "uuid": "51ee4f42-91dd-45e3-af7b-cf697a1eea26",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015cXg6VwXTKwZFu2H8e3N3j",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9413,
      "cache_read_input_tokens": 42632,
      "output_tokens": 273,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9413,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 273,
          "cache_read_input_tokens": 42632,
          "cache_creation_input_tokens": 9413,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9413
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

_source line 8858 · 2026-05-20T09:38:57.239Z_

Now let me read the paper_framing.md and registry for the new experiments.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "51ee4f42-91dd-45e3-af7b-cf697a1eea26",
  "isSidechain": false,
  "requestId": "req_011CbDbdZoThCZZs8GKFR7bs",
  "type": "assistant",
  "uuid": "cb3c23d9-fda8-49b0-b7fd-003a70fc0cab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015cXg6VwXTKwZFu2H8e3N3j",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9413,
      "cache_read_input_tokens": 42632,
      "output_tokens": 273,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9413,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 273,
          "cache_read_input_tokens": 42632,
          "cache_creation_input_tokens": 9413,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9413
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

_source line 8859 · 2026-05-20T09:38:58.166Z_

<details open><summary>🔧 Tool call — Read · `toolu_01B5fxzUBeJuoNy3Z7GPoGJj`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cb3c23d9-fda8-49b0-b7fd-003a70fc0cab",
  "isSidechain": false,
  "requestId": "req_011CbDbdZoThCZZs8GKFR7bs",
  "type": "assistant",
  "uuid": "92f951e2-e413-4b44-988e-f45c626c332f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015cXg6VwXTKwZFu2H8e3N3j",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9413,
      "cache_read_input_tokens": 42632,
      "output_tokens": 273,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9413,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 273,
          "cache_read_input_tokens": 42632,
          "cache_creation_input_tokens": 9413,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9413
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

_source line 8860 · 2026-05-20T09:38:58.334Z_

<details><summary>↩ Tool result · `toolu_01Hdq81fRD9xfST2r9GWHcZ6`</summary>

```text
No matching deferred tools found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3a4c5d3a-c5f9-4514-a2b0-d9e3dd7173fd",
  "isSidechain": false,
  "promptId": "3f50ba00-7d30-45ec-b450-7010d531c858",
  "type": "user",
  "uuid": "702bcb7e-8430-4499-b7f1-4af9b4cfbf76",
  "toolUseResult": {
    "matches": [],
    "query": "select:read_registry",
    "total_deferred_tools": 51
  },
  "sourceToolAssistantUUID": "3a4c5d3a-c5f9-4514-a2b0-d9e3dd7173fd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora"
}
```

</details>

---


### Tool result

_source line 8861 · 2026-05-20T09:38:58.170Z_

<details><summary>↩ Tool result · reported error · `toolu_01B5fxzUBeJuoNy3Z7GPoGJj`</summary>

```text
File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "92f951e2-e413-4b44-988e-f45c626c332f",
  "isSidechain": false,
  "promptId": "3f50ba00-7d30-45ec-b450-7010d531c858",
  "type": "user",
  "uuid": "51397176-f112-4d74-bb85-02b1a77b6e72",
  "toolUseResult": "Error: File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69.",
  "sourceToolAssistantUUID": "92f951e2-e413-4b44-988e-f45c626c332f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora"
}
```

</details>

---


### Tool call

_source line 8862 · 2026-05-20T09:38:58.331Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Hdq81fRD9xfST2r9GWHcZ6`</summary>

```json
{
  "query": "select:read_registry",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "51397176-f112-4d74-bb85-02b1a77b6e72",
  "isSidechain": false,
  "requestId": "req_011CbDbdZoThCZZs8GKFR7bs",
  "type": "assistant",
  "uuid": "3a4c5d3a-c5f9-4514-a2b0-d9e3dd7173fd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015cXg6VwXTKwZFu2H8e3N3j",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9413,
      "cache_read_input_tokens": 42632,
      "output_tokens": 273,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9413,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 273,
          "cache_read_input_tokens": 42632,
          "cache_creation_input_tokens": 9413,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9413
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

_source line 8863 · 2026-05-20T09:39:01.268Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01DV1VZTyfB4wzxD1gGCxA8r`</summary>

```json
{
  "pattern": "**/paper_framing.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "702bcb7e-8430-4499-b7f1-4af9b4cfbf76",
  "isSidechain": false,
  "requestId": "req_011CbDbe9gASxSDt7168mZPt",
  "type": "assistant",
  "uuid": "ec71b2dc-4fc2-4de6-81e6-0169a1d7a158",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LxxozYdqWGh1ZRx9y8SuQX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 394,
      "cache_read_input_tokens": 52045,
      "output_tokens": 169,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 394,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 169,
          "cache_read_input_tokens": 52045,
          "cache_creation_input_tokens": 394,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 394
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

_source line 8864 · 2026-05-20T09:39:01.284Z_

<details><summary>↩ Tool result · `toolu_01DV1VZTyfB4wzxD1gGCxA8r`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260516T051642/best/paper_framing.md
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260516T051642/median/paper_framing.md
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260516T051642/worst/paper_framing.md
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260516T054054/best/paper_framing.md
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260516T054054/median/paper_framing.md
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260516T054054/worst/paper_framing.md
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260516T124139/best/paper_framing.md
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260516T124139/median/paper_framing.md
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260516T124139/worst/paper_framing.md
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260516T155754/best/paper_framing.md
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260516T155754/median/paper_framing.md
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260516T155754/worst/paper_framing.md
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260517T144412/best/paper_framing.md
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260517T144412/median/paper_framing.md
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260517T144412/worst/paper_framing.md
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260517T165032/best/paper_framing.md
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260517T165032/median/paper_framing.md
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260517T165032/worst/paper_framing.md
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260519T034058/best/paper_framing.md
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260519T034058/median/paper_framing.md
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260519T034058/worst/paper_framing.md
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/paper_framing.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ec71b2dc-4fc2-4de6-81e6-0169a1d7a158",
  "isSidechain": false,
  "promptId": "3f50ba00-7d30-45ec-b450-7010d531c858",
  "type": "user",
  "uuid": "389a5f11-b4dc-40db-a8e5-e86f3a0c4e51",
  "toolUseResult": {
    "filenames": [
      "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260516T051642/best/paper_framing.md",
      "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260516T051642/median/paper_framing.md",
      "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260516T051642/worst/paper_framing.md",
      "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260516T054054/best/paper_framing.md",
      "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260516T054054/median/paper_framing.md",
      "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260516T054054/worst/paper_framing.md",
      "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260516T124139/best/paper_framing.md",
      "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260516T124139/median/paper_framing.md",
      "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260516T124139/worst/paper_framing.md",
      "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260516T155754/best/paper_framing.md",
      "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260516T155754/median/paper_framing.md",
      "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260516T155754/worst/paper_framing.md",
      "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260517T144412/best/paper_framing.md",
      "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260517T144412/median/paper_framing.md",
      "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260517T144412/worst/paper_framing.md",
      "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260517T165032/best/paper_framing.md",
      "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260517T165032/median/paper_framing.md",
      "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260517T165032/worst/paper_framing.md",
      "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260519T034058/best/paper_framing.md",
      "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260519T034058/median/paper_framing.md",
      "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260519T034058/worst/paper_framing.md",
      "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/paper_framing.md"
    ],
    "durationMs": 11,
    "numFiles": 22,
    "truncated": false
  },
  "sourceToolAssistantUUID": "ec71b2dc-4fc2-4de6-81e6-0169a1d7a158",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora"
}
```

</details>

---


### Tool call

_source line 8865 · 2026-05-20T09:39:01.625Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01EiDjNNzPVALpoDNs6kVYtU`</summary>

```json
{
  "query": "select:read_registry,read_project_file",
  "max_results": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "389a5f11-b4dc-40db-a8e5-e86f3a0c4e51",
  "isSidechain": false,
  "requestId": "req_011CbDbe9gASxSDt7168mZPt",
  "type": "assistant",
  "uuid": "b749fb5a-2563-4c8f-9188-659b3d60bb1e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LxxozYdqWGh1ZRx9y8SuQX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 394,
      "cache_read_input_tokens": 52045,
      "output_tokens": 169,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 394,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 169,
          "cache_read_input_tokens": 52045,
          "cache_creation_input_tokens": 394,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 394
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

_source line 8866 · 2026-05-20T09:39:01.628Z_

<details><summary>↩ Tool result · `toolu_01EiDjNNzPVALpoDNs6kVYtU`</summary>

```text
No matching deferred tools found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b749fb5a-2563-4c8f-9188-659b3d60bb1e",
  "isSidechain": false,
  "promptId": "3f50ba00-7d30-45ec-b450-7010d531c858",
  "type": "user",
  "uuid": "f9de2add-dd1c-4ef3-bcb3-6a71ad73eb1d",
  "toolUseResult": {
    "matches": [],
    "query": "select:read_registry,read_project_file",
    "total_deferred_tools": 51
  },
  "sourceToolAssistantUUID": "b749fb5a-2563-4c8f-9188-659b3d60bb1e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora"
}
```

</details>

---


### Runtime record

_source line 8867 · 2026-05-20T09:39:01.684Z_

```json
{
  "parentUuid": "f9de2add-dd1c-4ef3-bcb3-6a71ad73eb1d",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "eb04c02d-4b7b-43a6-aa44-492b6e030c37",
  "timestamp": "2026-05-20T09:39:01.684Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora"
}
```

---


### Tool call

_source line 8868 · 2026-05-20T09:39:04.889Z_

<details open><summary>🔧 Tool call — Read · `toolu_01ALsQpDUhcZmRT5Xgj7UACF`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eb04c02d-4b7b-43a6-aa44-492b6e030c37",
  "isSidechain": false,
  "requestId": "req_011CbDbePkkGHjfonRxJPkMr",
  "type": "assistant",
  "uuid": "a080a9f5-97fe-4315-ba24-f9ed98932995",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013A1P3r8XAxAzRPDjh7n1De",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1509,
      "cache_read_input_tokens": 52439,
      "output_tokens": 88,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1509,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 88,
          "cache_read_input_tokens": 52439,
          "cache_creation_input_tokens": 1509,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1509
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

_source line 8869 · 2026-05-20T09:39:05.154Z_

<details><summary>↩ Tool result · `toolu_01ALsQpDUhcZmRT5Xgj7UACF`</summary>

```text
1	# Paper Framing — symb_invariant_consensus
2	
3	## Target Venue
4	- Primary: EMNLP 2026 Main (ARR May 25)
5	- Deadline: May 25, 2026 (ARR submission)
6	
7	## D063 Direction: Entropy Decomposition + Quality Ladder — 目标 4.0
8	
9	**从 D060 "Pure Analysis / negative result" 升级为 "Regime-Dependent Mechanism Analysis with Entropy Decomposition"。** 用户决定冲 4.0。
10	
11	### Entropy Breakdown 验证结果 (2026-05-19 completed)
12	
13	**跨模型 entropy mechanism 一致性: 不成立。Selective SICA 非 universal 方案。**
14	
15	但 entropy decomposition 揭示了更有价值的 regime mechanism：
16	
17	| Experiment | Model | Dataset | High-E n | High-E Δpp | Low-E n | Low-E Δpp |
18	|-----------|-------|---------|----------|-----------|---------|----------|
19	| exp-033 s42 | Mistral-7B | FOLIO | 78 | **+12.8** | 126 | 0.0 |
20	| exp-052 s123 | Mistral-7B | FOLIO | 77 | **+9.1** | 127 | 0.0 |
21	| exp-053 s456 | Mistral-7B | FOLIO | 75 | -1.3 | 129 | 0.0 |
22	| exp-046 | Mistral-7B | PW-600 | 267 | -4.9 | 333 | -1.2 |
23	| exp-036 | Qwen2.5-14B | FOLIO | 37 | **-8.2** | 167 | -0.6 |
24	| exp-038 | Qwen2.5-14B | LogiQA | 23 | -4.3 | 177 | 0.0 |
25	| exp-035 | Qwen2.5-7B | FOLIO | 47 | -2.1 | 157 | 0.0 |
26	| exp-048 | LLaMA-8B | PW-600 | 76 | -3.9 | 104 | -1.9 |
27	
28	(注: SC/Δ 使用 pre-tiebreaking 值，entropy grouping 不受 tiebreaking 影响。D064 修正后 deltas 会略有变化但 pattern 不变。)
29	
30	**三个核心发现：**
31	1. **Low-entropy: SICA≈SC 跨模型一致** (8/8 experiments Δ≈0) → traces 一致时 constraints 无新信息
32	2. **High-entropy 方向因 regime 而异**：Goldilocks +12.8pp vs Type A -8.2pp vs Type C -4.9pp
33	3. **Mechanism 解释**：
34	   - Goldilocks (SC~55%, κ~0.46): 真实不确定性 → constraints 打破平局正确方向
35	   - Type A (SC>75%, κ>0.65): 偶发错误 → constraints 放大 confirmation bias
36	   - Type C (SC<40%, κ~0.20): 系统性错误 → constraints 是噪声
37	
38	### 调整后核心转变
39	
40	论文以 "entropy decomposition 揭示 regime-dependent mechanism" 为核心分析贡献（不是 universal diagnostic）：
41	- **Entropy decomposition 作为分析工具**：分离 SICA 作用点（high-entropy）vs 不作用点（low-entropy）
42	- **Regime mechanism 量化**：同样是 high-entropy 问题，direction depends on SC+κ → 完美支持 dual bottleneck
43	- **Abandoned**: Selective SICA 作为 universal practical contribution（只在 Goldilocks zone 有效）
44	- **Upgraded**: 核心图 = high-entropy Δ vs SC scatter（8 points, 3 regimes 清晰分离）
45	- **Quality Ladder** (D067: L1 NULL CONFIRMED)
46	  - L0: Self-extraction (Mistral→Mistral): 59.31%, Δ=+3.43pp ns
47	  - L1a: Qwen3-14B→Mistral traces: 60.29%, Δ=+4.41pp (+0.98pp vs self = 2题/204 = noise)
48	  - L1b: Qwen2.5-14B→Mistral traces: 58.33%, Δ=+2.45pp (-0.98pp vs self = 2题/204 = noise)
49	  - L3: Oracle 100% disc, Δ=+14.22pp p<0.001
50	  - **结论**: L1 ≈ L0 << L3。Bottleneck 在 traces（同源输入），不在 extractor（换模型无效）
51	  - **Paper contribution**: "bottleneck is fundamental to extraction, not just model capability" — 强化 structural limitation 论点
52	- **CJT/Eff-K 保留**：解释 why high-entropy behavior differs across regimes
53	
54	D060 要素全部保留：
55	- Condorcet independence 框架 → 理论基础
56	- 9 种修复全部失败 → structural limitation 证据
57	- 2/3 seeds positive trend but **0/3 significant** (D066: p=0.092/0.070/1.0) → Goldilocks zone 作为 directional trend, not confirmed effect
58	- K/T sensitivity non-monotonic → SC confound insight
59	- 用户指示: 投 May 25 不变，冲 4.0
60	
61	## Core Claims (5 条) — D060 纯 Analysis Framing
62	
63	### Analysis Claims (已验证)
64	
65	1. **Independence Bottleneck**: Self-consistency 隐含 Condorcet Jury Theorem 的独立性假设，但同模型采样的 traces 高度相关。Worker 验证的 κ 值：
66	   - Qwen-14B FOLIO: κ=0.744, Eff-K=1.31 (SC=75.49%, Δ=+0.25pp n.s.)
67	   - Qwen-14B LogiQA: κ=0.821, Eff-K=1.20 (SC=78.5%, Δ=+0.50pp n.s.)
68	   - Mistral-7B FOLIO s42 (exp-033): κ=0.501, Eff-K=1.84 (SC=55.88%, Δ=+3.43pp **p=0.092 ns**) ← primary seed [D064+D066]
69	   - Mistral-7B FOLIO s123: κ=0.491, Eff-K=1.88 (SC=54.41%, Δ=+2.94pp **p=0.070 ns**)
70	   - Mistral-7B FOLIO s456: κ=0.507, Eff-K=1.82 (SC=55.88%, Δ=0.00pp p=1.0 ns)
71	   - Mistral-7B PW-600 (exp-046): κ=0.210, Eff-K=3.63 (Δ=-2.83pp p=0.010, SC=39%)
72	   规律：跨模型对比清晰（Qwen Eff-K≈1.2-1.3 → 0 gain; Mistral Eff-K≈1.85-2.22 → variable gain）。但 Mistral seeds 内部，Eff-K 与 delta 非单调（exp-033 Eff-K 最低 1.85 却 delta 最高 +3.43pp）→ Eff-K 是跨模型必要条件，seed 内 variance 仍主导。exp-046 Eff-K 最高(3.63) 但 SC 太低(39%) 导致 delta 为负 → 需同时满足 sufficient Eff-K AND sufficient SC。
73	
74	2. **Oracle Gap Localizes Extraction Bottleneck**: Gold FOL + MAX-SAT = +14.22pp (p=2.0e-7)，自提取仅 +3.43pp (best seed, D064 corrected) = 24% utilization。聚合机制本身有效，瓶颈在自提取质量。Two-layer analysis:
75	   - **Constraint taxonomy**: 43% trivially_satisfied（被所有候选答案满足的约束，不排除任何答案）
76	   - **Discriminative filtering**: 仅 ~8% 约束在 MAX-SAT scoring 中完全 non-discriminative（移除后 0 gains）
77	   - **关键区分**: 43% 和 8% 度量不同。trivially_satisfied 约束在 MAX-SAT 中仍可有不同满足程度（partial vs full），所以不全是 non-discriminative。但即使 constraints 是 discriminative 的，它们的"区分方向"与模型自身偏差一致（confirmation bias）。both_wrong 组 score_range=29.4。九种修复全部失败。
78	
79	3. **Regime-Dependent Capability Trap**: SICA 有效性取决于提取模型的基线准确率，存在双边界：
80	   - Type A (SC ≥ ~60%): 确认偏差，constraints 镜像模型自身答案。**exp-034 vs exp-039 同配置 delta 翻转**: exp-034 Δ=+0.51pp (n=589), exp-039 Δ=-2.00pp (n=600)。SC baseline 方差 (3.38pp) >> SICA 效应 → Type A delta 是 trace sampling noise。SICA 比 SC 更稳定 (跨运行方差 0.87pp vs 3.38pp，仅 2 点，需更多 seed 验证)
81	   - Type C (SC ≤ ~40%): traces 主要错误，constraints 是噪声 (exp-046: Δ=-2.83pp, p=0.0095)
82	   - Goldilocks zone (~50-56% SC): 部分独立性 + 部分正确性 (exp-033: Δ=+3.43pp, p=0.092 ns; mean of 3 seeds: +2.12pp) ⚠️ D076 Reviewer: 0/3 seeds significant, 不应作为核心叙事支柱。作为 directional observation 保留，不做强 claim。
83	   - Type B: 领域不可形式化 (LogiQA: contradiction rate 0.8%)
84	
85	4. **C0+SC Two-Dimensional Diagnostic**: C0 (multi-candidate rate) + SC accuracy 形成零成本部署诊断。C0<5% → degenerate; high C0 + high SC → trap; high C0 + low SC → potential gains。
86	
87	### Remediation Evidence (D060: 全部失败 — 强化 analysis narrative)
88	
89	5. **Nine Remediation Attempts All Failed**: 原 6 种 + 3 种靶向修复全部无效，证明 independence bottleneck 是结构性的：
90	   - D059 三路 method improvement 全部失败：
91	     - Discriminative Filtering: 119/204 处理后 0 gains 1 loss，~92% 约束本身就是 discriminative，过滤是 near-no-op
92	     - T=1.0 (exp-054): delta 从 +3.43pp 崩塌到 0.00pp（D064 corrected），温度敏感性极端
93	     - Multi-Temp (exp-055): ✅ 完成，delta=+0.00pp (b=5,c=5 完美对称), SC=57.84%. 混合 T=0.3/0.7/1.2 各 4 traces 未改善 SICA。附带发现：multi-temp 提升 SC baseline (+3.4pp vs 单温度 54.41%)，说明混合温度对 majority voting 有帮助，但 SICA constraint extraction 无法利用这种 diversity → bottleneck 在 extraction 而非 trace diversity
94	   - 原 6 种：contrastive prompting, cross-model extraction, generational scaling, solver-guided refinement, consistency filtering, cross-trace UNSAT
95	   - 9 种修复涵盖 prompting / architecture / capability / verification / diversity / filtering 全维度，全部失败 → trap is fundamental
96	
97	## D070/D074 Update: Method-Level Interventions Also Fail — "Fundamental Limitation" Confirmed
98	
99	### Three Method Lines × Two Datasets = All Negative (D074)
100	
101	D070 从纯 analysis 升级为 analysis + method paper，但三条方法线全面失败（D074 确认），反而强化了原始 analysis 结论。
102	
103	**方法×数据集完整结果**：
104	| Method | FOLIO-204 | LogiQA-200 | Failure Mode |
105	|--------|-----------|------------|--------------|
106	| ICG (Independent Constraint Gen.) | Δ=-2.0pp (3-seed: -2.0/+1.5/-1.0, mean=-0.5pp±1.8pp, 噪声) | Δ=-0.5pp | Neutral — 独立约束质量≈trace-sourced约束 |
107	| Contrastive (Pro/Con Scoring) | Δ≈-16pp | Δ≈-7pp (interim) | Harmful — 26% degenerate scoring, pro/con 不平衡 |
108	| Debate (Proposer/Critic) | Δ=-18.6pp | Δ≈-28pp (interim) | Catastrophic — 7B 模型角色扮演严重退化推理 |
109	
110	**三种失败模式的分析价值**（论文 "Why Methods Fail" section）：
111	1. **ICG (neutral)**: 独立于 traces 生成的约束不比 trace-sourced 约束更好。说明 bottleneck 不仅是 "约束来自 traces"，而是模型的推理偏差从问题理解阶段就存在——独立约束和 trace-sourced 约束继承相同的 model bias。
112	2. **Contrastive (harmful)**: 强制 pro/con 评估引入 degenerate scoring（26% 问题无法有效区分）。7B 模型无法可靠生成平衡的对立约束——pro 约束系统性多于 con（94 pro vs 65 con），confirmation bias 从约束提取转移到了约束生成。
113	3. **Debate (catastrophic)**: Proposer/Critic/Defense 多角色链在 7B 模型上导致答案质量严重退化。辩论不仅未增加多样性，反而引入了角色扮演的额外认知负担。同模型辩论 = 同源性 + 角色扮演退化，双重损失。
114	
115	**Scale limitation caveat**: 所有方法测试在 7B 模型上。7B 模型生成 Z3 格式 FOL 约束的能力不足（ICG 多题 "0/N constraints parsed"）。14B+ 模型可能有不同结果——这既是 limitation 也是 future work 入口。
116	
117	### κ Generalization — Independence-Accuracy Trade-off (D075, CAPSTONE FINDING)
118	
119	exp-077 测量三种聚合方式在 Mistral-7B FOLIO-204 上的 κ 和 Eff-K：
120	| 聚合方式 | Fleiss' κ | Eff-K | 名义 K |
121	|----------|----------|-------|--------|
122	| Self-Consistency | 0.4384 | 2.02 | 10 |
123	| Diverse-Prompt | 0.4030 | 2.21 | 12 |
124	| LLM-Debate | 0.1549 | 4.44 | 12 |
125	
126	结合 exp-076 Debate Δ=-18.6pp 的准确率数据，揭示**同模型框架下的 fundamental independence-accuracy trade-off**：
127	- **SC/Diverse-Prompt**: κ~0.4，traces 高度相关但准确率正常。换 prompt 策略不改善独立性（Δκ=0.04）。
128	- **Debate**: κ=0.15，成功打破 trace 相关性（Eff-K 从 2.0 跃升到 4.4），但准确率崩溃 -18.6pp。低 κ 不代表"更独立的推理"——是 disagreement amplification（系统性噪声）。
129	- **Trade-off 本质**: 同一模型的推理能力是固定的。要么输出一致（高 κ, 正确但不独立），要么输出分歧（低 κ, 独立但不正确）。Condorcet Jury Theorem 要求 both independent AND accurate，同模型框架下无法同时满足。
130	
131	**论文叙事升级**: 从 "methods fail" → "independence-accuracy trade-off is fundamental to same-model reasoning"。突破瓶颈需要跨模型方案（不同模型天然更独立），Oracle 实验（gold FOL 来自外部知识源）已间接验证了这一点。
132	
133	### New Claim 6 (D070/D074)
134	
135	6. **Method-Level Interventions Cannot Break the Bottleneck**: 三种针对 independence bottleneck 不同环节的方法（ICG→循环依赖, Contrastive→confirmation bias, Debate→trace 同质性）在 2 个数据集上全部失败。加上之前 9 种 prompt-level 修复，共 12 种修复尝试全败。这证明 independence bottleneck 不是单一环节的问题，而是 same-model self-extraction 的根本性限制。
136	
137	### New Claim 7: Symbolic Confirmation Bias (D082 — CORE FINDING)
138	
139	7. **Symbolic Confirmation Bias**: LLM 从 CoT traces 提取的 FOL 约束系统性确认 trace 自身（可能错误的）答案，而非独立验证 ground truth。
140	   - SICA 判对题：gold constraint 78.1%，bias ratio = 0.28
141	   - SICA 判错题：错误 constraint 83.3%，bias ratio = **4.97×**
142	   - 97.6% SICA 错误与 SC 错误完全重合
143	   - SICA 翻盘的 12 例来自 minority trace diversity（43% gold support），不是 symbolic reasoning
144	   - **因果链**：模型推理→答案→从含答案 trace 提取 FOL→约束确认答案→聚合≈SC
145	   - **CEGIS 验证**：迭代精炼 R1 +3.43pp < 原始 SICA +4.9pp → 约束一致性不是瓶颈，偏向性才是
146	   - **Quality Ladder 验证**：L1 ≈ L0 << L3 → bottleneck 在 traces（同源输入），不在 extractor
147	
148	### New Claim 8: Process-κ (D082 — NEW METRIC)
149	
150	8. **Process-Level Independence (Process-κ)**: answer-κ 低估真实独立性瓶颈。CoT 推理过程相似性远高于答案一致性。
151	   - Mistral-7B FOLIO-204：CoT cosine similarity **0.69** >> answer-κ **0.41**
152	   - 两者几乎无相关性：r = -0.06, p = 0.36
153	   - 仅 **9.3%** trace 对是"殊途同归"（同答案不同路径）
154	   - answer-κ 是 true independence bottleneck 的 lower bound
155	   - 适用于所有 LLM trace aggregation 方法，不限于 SICA
156	
157	## D082/D085: Comprehensive Method Exhaustion — 25+ ALL Fail
158	
159	D080 启动全方向并行探索（Wave 1-3），在 D074 的 12 种修复基础上又测试 13+ 新干预：
160	
161	| 方法 | 类型 | 结果 | 关键数据 |
162	|------|------|------|----------|
163	| PROVE 代码验证 | paradigm shift | ❌ | Code gen 15.2%, accuracy=random |
164	| CEGIS 迭代精炼 | multi-round | ❌ | R1 +3.43pp < SICA +4.9pp |
165	| DeepConf 置信度 | filtering | ❌ | logprob 与正确性零相关 |
166	| Cross-model SICA | cross-model | ❌ | Δ=-0.49pp despite lower κ |
167	| Problem Perturbation | input diversity | ❌ | κ 升至 0.696 (反效果) |
168	| MIN-UNSAT | solver objective | ❌ | 49.5% < SC 54.4% |
169	| κ-aware SC | voting rule | ❌ | 11/11 Δ=0 |
170	| Z3 Trace Filter | trace filtering | ❌ | negative |
171	| Bootstrapped Gold | iterative | ❌ | negative |
172	| Selective Abstention | diagnostic | ⚡ | AUROC=0.673, +4.4pp@80%cov |
173	
174	**D085 总结**: 9 prompt-level + 3 method-level + 13 新方向 = **25+ 干预全部 negative**。Independence bottleneck 在 same-model self-extraction 框架下无解，所有维度（diversity/architecture/capability/verification/filtering/voting/solver/paradigm）已穷尽。
175	
176	### Updated Headline Result (D085)
177	
178	"Across 6+ models and 4 domains, symbolic consensus aggregation shows no statistically significant positive effect. 25+ interventions spanning prompt engineering, method-level redesign (ICG, Contrastive, Debate), solver modifications, cross-model aggregation, code-based verification, and iterative refinement all fail. We identify the root cause as Symbolic Confirmation Bias: self-extracted FOL constraints systematically confirm the trace's own answer (bias ratio 4.97× on incorrect problems), making symbolic aggregation equivalent to majority voting. Process-level analysis reveals reasoning paths are far more homogeneous than answers suggest (cosine similarity 0.69 vs answer-κ 0.41). The one method that breaks trace correlation (Debate: κ 0.44→0.15) does so at catastrophic accuracy cost (-18.6pp), revealing a fundamental independence-accuracy trade-off. Oracle constraints prove the aggregation mechanism works (+14.22pp, p<0.001), localizing the bottleneck entirely to self-extraction quality."
179	
180	### Updated Story Spine (D074)
181	
182	- **Problem**: [unchanged]
183	- **Theoretical lens**: [unchanged]
184	- **Systematic evaluation**: [unchanged]
185	- **Regime characterization**: [unchanged]
186	- **Remediation failures strengthen thesis (D085 FINAL)**: 9 prompt-level + 3 method-level + 13 new directions = **25+ interventions** across ALL dimensions (diversity/architecture/capability/verification/filtering/voting/solver/paradigm), all fail → bottleneck is fundamental and exhaustively proven
187	- **Method failure analysis**: Three methods targeting different bottleneck aspects show three distinct failure modes (neutral/harmful/catastrophic), revealing that the bottleneck operates at multiple levels simultaneously
188	- **Independence-accuracy trade-off (HERO FINDING, D075)**: Debate breaks trace correlation (κ 0.44→0.15, Eff-K 2.0→4.4) but accuracy collapses (-18.6pp/-23.0pp). Same-model traces can be independent OR accurate, not both.
189	- **NEW — Symbolic Confirmation Bias (CORE FINDING, D082)**: Root cause identified — self-extracted FOL constraints systematically confirm the trace's own answer (bias ratio 4.97× on incorrect problems). Causal chain: model reasons → answer → FOL extraction confirms answer → aggregation ≈ SC. This is WHY 25+ methods fail.
190	- **NEW — Process-κ (NEW METRIC, D082)**: CoT reasoning similarity (0.69) >> answer-κ (0.41), r=-0.06. Only 9.3% of trace pairs are "convergent reasoning." answer-κ underestimates the true bottleneck. Novel metric applicable to all LLM trace aggregation.
191	- **Actionable contribution**: C0+SC diagnostic + κ-based Eff-K estimation = zero-cost deployment toolkit. κ analysis shows SC itself has a scaling ceiling (Eff-K ≈ 2 means K>12 traces yield diminishing returns).
192	- **Universal across architectures (D078)**: Three families: Mistral-7B κ=0.438, LLaMA-8B κ=0.412, Qwen2.5-7B κ=0.658, Qwen2.5-14B κ=0.738. Family effect (Δκ=0.22) >> scale effect (Δκ=0.08).
193	- **Headline (D085)**: Independence bottleneck is structural, universal across architectures, and rooted in Symbolic Confirmation Bias. 25+ interventions spanning all conceivable dimensions fail. Process-κ reveals reasoning homogeneity far exceeds answer-level agreement. The independence-accuracy trade-off constrains all same-model trace aggregation.
194	
195	## Core Insight (D060 Updated — Dual Bottleneck)
196	
197	**Dual Requirement Framework**: SICA 效应需要同时满足两个条件，缺一不可：
198	1. **Sufficient Independence** (Eff-K > threshold): traces 需要提供足够多的独立视角
199	2. **Sufficient Quality** (SC > ~50%): traces 需要有足够的正确率，否则约束是噪声
200	
201	Condorcet Jury Theorem 要求投票者独立且 p>0.5。同模型采样的 reasoning traces 严重违反独立性假设（Fleiss' κ = 0.21–0.82，Eff-K 仅 1.20–3.63），解释了为什么简单增加 K 或添加符号约束不能突破 SC 的天花板。
202	
203	实验数据完美支持 dual requirement（κ 使用统一脚本 compute_fleiss_kappa_unified.py，SC/Δpp 使用 registry 原始值）：
204	- **Qwen family**: κ=0.66-0.82, Eff-K≈1.20-1.46（独立性不足）→ all near-zero delta，无论 SC 多高
205	- **Mistral-7B FOLIO**: κ≈0.46, Eff-K≈2.0（中等独立性）+ SC≈55%（中等质量）→ +3.43pp best seed, mean +2.12pp (2/3 seeds positive, 1 null)
206	- **Mistral-7B PW-600**: κ=0.20, Eff-K=3.76（最高独立性）但 SC=39%（质量不足）→ -2.83pp
207	- 只有 Goldilocks zone（中等 Eff-K + 中等 SC）出现正向 delta
208	- **Dual bottleneck 直接验证 (exp-055)**：Multi-temp κ=0.427 Eff-K=2.11（比单温度 κ≈0.46 Eff-K≈2.0 更独立）但 delta=0.00pp → 提高 independence 不够，还需要 extraction quality
209	- **T sensitivity 孤立尖峰 (4/4 complete, D064 corrected)**：T=0.3(Δ=-1.47), T=0.5(Δ=-0.98), T=0.7(Δ=+3.43, κ=0.460, Eff-K=1.98), T=1.0(Δ=0.00, κ=0.394, Eff-K=2.25)。T=0.7 孤立尖峰更突出。T=0.7 SC=55.88%（最低）→ entropy 最高 → SICA 操作空间最大。温度效应与 SC 效应互为 confound，论文需讨论
210	- **Thinking mode κ=0.913, Eff-K=1.09 (exp-028b)**：近乎确定性。思维模式让 traces 更一致 → 独立性更差。"更好的推理"反而加剧 independence bottleneck。
211	
212	**κ 是 model-level 稳定属性**：统一处理后 Mistral 三 seed κ 收敛至 0.457-0.460（之前 0.41-0.50 差异是非标准 answer 处理的 artifact）。κ 跨 seed 几乎相同，但 delta 差异大（+3.43 vs +2.94 vs 0.00）→ seed-level constraint quality variance 主导，非 κ。
213	
214	完整 κ 表（⚠️ D062: κ 将用 raw answers 重算，当前 unified 值为临时值。Qwen 无变化，Mistral 条件将更新）：
215	| Exp | Model | κ(unified→raw pending) | Eff-K | SC%(registry) | Δpp(registry) |
216	|-----|-------|------------|-------|---------------|---------------|
217	| exp-028b | Qwen3-14B thinking | 0.913 | 1.09 | ~84% | ~0 |
218	| exp-038 | Qwen-14B LogiQA | 0.821 | 1.20 | 78.50 | -0.50 |
219	| exp-027 | Qwen3-14B | 0.773 | 1.26 | 84.31 | +0.49 |
220	| exp-036 | Qwen2.5-14B | 0.744 | 1.31 | 75.49 | +0.25 |
221	| exp-035 | Qwen2.5-7B | 0.658 | 1.46 | 76.47 | -0.49 |
222	| exp-049b | Mistral-7B LogiQA | 0.512 | 1.81 | 51.00 | +0.50 |
223	| exp-057 | Mistral-7B T=0.3 | 0.502 | 1.84 | 58.33 | -1.47 |
224	| exp-058 | Mistral-7B T=0.5 | 0.516 | 1.80 | 58.33 | -0.98 |
225	| exp-033 | Mistral-7B s42 | 0.460 | 1.98 | 55.88 | +3.43 |
226	| exp-052 | Mistral-7B s123 | 0.457 | 1.99 | 54.41 | +2.94 |
227	| exp-053 | Mistral-7B s456 | 0.457 | 1.99 | 55.88 | 0.00 |
228	| exp-055 | Mistral-7B multi-T | 0.427 | 2.11 | 57.84 | 0.00 |
229	| exp-054 | Mistral-7B T=1.0 | 0.394 | 2.25 | 55.39 | 0.00 |
230	| exp-046 | Mistral-7B PW-600 | 0.200 | 3.76 | 39.33 | -2.83 |
231	注：κ 基于 T/F/U 三类归一化，Mistral-7B 约 12-16% traces 被归一化（Qwen 100% valid）。Mistral SC/Δpp 已更新为 D064 tiebreaking 修正值；Qwen 不受影响。
232	
233	Oracle control (+14.22pp) 证明 MAX-SAT 聚合机制本身有效，但自提取约束仅利用了 24% 的理论上限。Discriminative filtering 实验揭示关键机制：~92% 约束 ARE discriminative，但过滤掉 ~8% non-discriminative 约束后 delta 不变（0 gains）。问题不在约束缺乏判别力，而在于 discriminative constraints 的区分方向与模型偏差一致（confirmation bias）。
234	
235	**Remediation insight (D060)**: 9 种修复尝试全部失败，包括直接靶向 independence（multi-temp diversity, exp-055: Eff-K 从 2.0→2.11 但 delta 仍为 0）和 constraint quality（discriminative filtering）。这证明 bottleneck 不是简单的 diversity 或 quality 问题，而是 same-model self-extraction 的根本性限制。
236	
237	**Key evidence**:
238	- **Condorcet independence quantification (统一脚本, 公式: Eff-K=K/(1+(K-1)κ))**: Mistral-7B FOLIO κ≈0.46 (Eff-K≈2.0, 三 seed 高度稳定), Mistral-7B PW-600 κ=0.200 (Eff-K=3.76), Qwen2.5-14B FOLIO κ=0.744 (Eff-K=1.31), Qwen2.5-14B LogiQA κ=0.821 (Eff-K=1.20), Qwen3-14B κ=0.773 (Eff-K=1.26), Qwen2.5-7B κ=0.658 (Eff-K=1.46). 跨模型清晰: Qwen Eff-K≈1.2-1.5→0 gain, Mistral FOLIO Eff-K≈2.0→variable gain, Mistral PW Eff-K=3.76 but SC too low→negative. κ stable across seeds (0.457-0.460), delta varies → seed-level constraint quality dominates.
239	- **Oracle control (exp-031)**: Gold FOL + MAX-SAT = 89.71% vs SC 75.49% (+14.22pp, p=2.0e-7). Unknown-type +31.9pp.
240	- **Two-layer constraint analysis**: 43% trivially_satisfied (taxonomy: satisfied by ALL answers) vs ~8% non-discriminative (filtering: same MAX-SAT score). Difference: trivially_satisfied constraints can still have different satisfaction DEGREES. Removing the 8% yields 0 gains → problem is not quality but confirmation bias direction.
241	- **K sensitivity (non-monotonic peak at K=12, 5/5 complete, D064+D066)**: K=4(-1.47pp), K=8(-1.96pp), K=12(+3.43pp p=0.092 ns), K=16(+1.47pp), K=20(+1.96pp). Peak at K=12, drops at K=16 but partially recovers at K=20. NOT clean inverted-U. K=12 SC=55.88% (post-fix). SC-confound with T sensitivity still holds. SICA at K=4 vs K=12 differs by ~4.9pp despite similar SC — proves SICA extracts different information than SC.
242	- **SC-confound (cross-cutting insight)**: K=12 和 T=0.7 都是 SC 最低 (54.41%) 的配置 → SICA "最佳超参"可能反映 entropy/operating-window 效应而非 K 或 T 的因果贡献。论文需要讨论这个 confound，但也可以正面利用：SC level 是更基本的预测变量，K 和 T 通过影响 SC 来间接影响 SICA delta。
243	- **T sensitivity (isolated peak, 4/4 complete, D064 corrected)**: T=0.3(Δ=-1.47pp), T=0.5(Δ=-0.98pp), T=0.7(Δ=+3.43pp p=0.092 ns), T=1.0(Δ=0.00pp). NOT smooth inverted-U — T=0.7 is an isolated spike. T=0.7 has lowest SC (55.88%) → highest entropy → largest SICA operating window. Temperature and SC effects confounded. Strengthens fragility narrative.
244	- **Regime boundary**: Qwen-14B (SC=75.49%) Δ=-0.98pp vs Mistral-7B (SC=55.88%) Δ=+3.43pp p=0.092 ns
245	- **Type C failure (exp-046)**: Mistral PW-D5 SC=39.33%, Δ=-2.83pp, p=0.010, κ=0.210, Eff-K=3.63, contradiction rate 5.5%. Highest Eff-K yet worst delta → independence alone insufficient when SC too low.
246	- **Seed replication (D064+D066)**: 2/3 seeds positive but **0/3 significant** after tiebreaking correction: s42 Δ=+3.43pp p=0.092, s123 Δ=+2.94pp p=0.070, s456 Δ=0.00pp p=1.0. Mean +2.12pp. Only significant McNemar effects are NEGATIVE: exp-046 Δ=-2.83pp p=0.014, exp-039 Δ=-2.50pp p=0.011. Paper must frame as "positive directional trend" not "significant positive effect".
247	- **Nine remediation failures (ALL CONFIRMED)**: contrastive prompting, cross-model, generational scaling, solver-guided, consistency filtering, cross-trace UNSAT, discriminative filtering (0 gains), T=1.0 (delta collapse +3.43→0.00pp, D064 corrected), multi-temp (delta=+0.00pp, b=5 c=5). All 9 failed → trap is fundamental, bottleneck is structural.
248	- **Entropy decomposition (VERIFIED 2026-05-19)**: High-entropy proportion: Mistral FOLIO 38% (78/204) vs Qwen FOLIO 18% (37/204) vs Qwen LogiQA 12% (23/200). SICA on high-entropy: Mistral FOLIO s42 +12.8pp, s123 +9.1pp, s456 -1.3pp; Qwen FOLIO -8.2pp; all others negative. Low-entropy: SICA≈SC across all 8 experiments (Δ≈0). Entropy decomposition reveals regime-dependent mechanism, NOT universal diagnostic.
249	- **Confirmation bias quantification**: ⚠️ "62.3%" and "28.6%" confirmed NOT present in any .tex file — likely hallucinated in earlier draft. DO NOT USE. Replace with verified metrics from experiment outputs only.
250	
251	## Story Spine (D059 Updated)
252	
253	- **Problem**: LLMs' reasoning can be improved by sampling multiple chains-of-thought and aggregating via majority voting (self-consistency). Recent work proposes symbolic augmentation: extract formal constraints from traces and use SAT solvers for answer selection. But does symbolic aggregation actually outperform simple voting?
254	- **Theoretical lens**: Condorcet Jury Theorem requires voter independence. We quantify trace independence via Fleiss' κ and show Effective-K << nominal K. This explains the fundamental limitation of same-model trace aggregation.
255	- **Systematic evaluation**: SICA (MAX-SAT over FOL constraints) across 3 domains × 5 model families. Oracle control separates extraction vs aggregation failure. Discriminative filtering reveals ~92% constraints are discriminative, yet SICA gains are fragile — confirmation bias, not constraint quality, is the bottleneck.
256	- **Regime characterization**: Three failure modes (Type A/B/C) + narrow Goldilocks zone. C0+SC as deployment diagnostic.
257	- **Remediation failures strengthen thesis**: 9 targeted interventions (prompting, architecture, capability, verification, diversity, filtering) all fail to close the oracle gap, proving the bottleneck is fundamental to same-model self-extraction.
258	- **Headline result (D066 McNemar corrected)**: "Across 6 models and 4 domains, symbolic consensus aggregation shows no statistically significant positive effect under corrected tiebreaking (best seed +3.43pp, p=0.092). The only significant effects are negative (PW-600: -2.83pp p=0.014, -2.50pp p=0.011). However, entropy decomposition reveals a striking regime-dependent pattern: SICA's entire effect concentrates on high-entropy questions, with +12.8pp in the Goldilocks zone but -2 to -8pp elsewhere. Oracle constraints prove the aggregation mechanism works (+14.22pp, p<0.001), localizing the bottleneck to extraction quality (24% utilization). Condorcet analysis (Eff-K=1.2-2.0 for nominal K=12) explains trace non-independence. Nine remediation strategies all fail, confirming the bottleneck is structural to same-model self-extraction."
259	
260	## Anticipated Reviewer Concerns & Defensive Experiments
261	
262	1. **"Gains not statistically significant"** → Correct: no positive effect reaches significance (best p=0.092). This IS the finding. Oracle p=2.0e-7 proves the mechanism works; the insignificance of self-extraction gains demonstrates the extraction bottleneck. Regime pattern (8 entropy conditions) provides systematic evidence beyond any single p-value.
263	2. **"Only one positive result (exp-033)"** → Seed replication: 2/3 positive (s42 +3.43pp, s123 +2.94pp), 1/3 null (s456 0.00pp). Mean +2.12pp. Effect IS real but fragile — the fragility itself IS the finding.
264	3. **"Condorcet framework is trivial"** → Fleiss' κ quantification is novel in SC/SICA context. Eff-K is actionable: tells practitioners how many truly independent traces they get.
265	4. **"Multi-temp / filtering should work"** → We tried both. Multi-temp (exp-055): negative. Disc. filtering: 0 gains. T=1.0: delta collapse. These failures STRENGTHEN the structural bottleneck thesis.
266	5. **"Only Qwen models"** → 5 families: Qwen-14B, Mistral-7B, LLaMA-8B, DeepSeek-R1-7B, QwQ-32B.
267	6. **"Only logic domain"** → FOLIO + ProofWriter + LogiQA + StrategyQA + ARC-Challenge. Type B (domain formalizability) is itself a finding.
268	7. **"Oracle is unfair comparison"** → Diagnostic tool, not competing method. Separates extraction from aggregation.
269	8. **"MAX-SAT is over-engineering"** → exp-013: MaxSAT ≈ count-only. This IS the independence bottleneck evidence.
270	9. **"Self-extraction confound"** → Oracle control resolves completely.
271	10. **"Published methods achieve gains (DyLoS, Aristotle, FoVer)"** → Different paradigm (external verifiers/trained extractors). We characterize same-model self-extraction.
272	11. **"C0 is trivially derived"** → Zero-cost early stopping. Practical value.
273	12. **"Why not just use a reasoning model?"** → QwQ-32B: C0<5%, SICA≡SC.
274	13. **"Random tiebreak baseline"** → exp-003: SICA tiebreak 80% vs random 50%.
275	14. **"Method improvement is incremental"** → Grounded in diagnosis (independence + taxonomy), not ad-hoc.
276	15. **"Weighted SC is simpler"** → exp-016 planned. Weighted SC doesn't address independence.
277	16. **"Within-model ICL transition contradicts regime theory"** → exp-050b (SC=57.79%, Δ=-3.52pp): ICL changes trace generation characteristics, not just SC level. Paper must distinguish "same model, different prompt" from "same model, same prompt, different accuracy."
278	
279	## Working Title
280	**"Beyond Self-Consistency: How Trace Independence Limits Symbolic Consensus in LLM Reasoning"**
281	(Alternatives:
282	- "The Independence Bottleneck: Why Self-Extracted Symbolic Constraints Cannot Beat Majority Voting"
283	- "Symbolic Consensus Under the Condorcet Lens: Independence, Extraction, and the Limits of Self-Aggregation")
284	
285	NOTE (Dream D037): Title MUST be scoped to "self-extracted constraints" / "SICA". Published methods (DyLoS, Aristotle, FoVer) use different approaches.
286	
287	## Paper Structure (EMNLP 8pp + appendix)
288	
289	### Main Tables
290	- T1: Main Results — models × domains, SC% / SICA% / Δpp / p-value, regime boundary
291	- T2: Oracle Control — Gold-FOL+MAX-SAT vs SC vs SICA-self, causal separation
292	- T3: Independence Quantification — Fleiss' κ / Eff-K / trace agreement per model
293	- T4: Extraction Error Taxonomy — trivially_satisfied / discriminative / both_wrong rates
294	- T5: K Sensitivity — K=4/8/12/16/20, non-monotonic (peak K=12, K=20 recovers), SC confound
295	
296	### Main Tables (continued)
297	- T6: Method-Level Intervention Results — 3 methods × 2 datasets, SC% / Method% / Δpp, failure mode classification
298	- T7: κ Generalization — SC / Debate / Diverse-Prompt κ and Eff-K (from exp-077, pending)
299	
300	### Main Figures
301	- F1: Method Pipeline (SICA + oracle control design)
302	- F2: SC Accuracy vs SICA Δ scatter (hero figure, regime boundary)
303	- F3: K Sensitivity with diversity metrics (K vs Δ, K vs Eff-K)
304	- F4: Extraction error breakdown (stacked bar)
305	- F5: Method intervention failure modes (grouped bar: ICG/Contrastive/Debate × FOLIO/LogiQA)
306	
307	### Appendix
308	- K ablation details, temperature sensitivity, per-domain results, overhead analysis
309	- Entropy-conditioned analysis (continuous scatter + bin sensitivity)
310	- Six remediation strategy details
311	- Confirmation bias quantification
312	- Seed replication analysis
313	- QwQ-32B / DeepSeek-R1 negative control
314	
315	## Claim Risk Notes (D059)
316	- **Seed replication**: 0/3 significant after D066 correction (p=0.092, 0.070, 1.0). 2/3 positive trend, 1/3 null. Mean +2.12pp. Frame as "directional trend, not significant effect" — fragility IS the finding.
317	- **Method claims DEAD (D060)**: All three method improvements failed. Paper is pure analysis. 9 remediation failures are EVIDENCE, not limitation.
318	- **Condorcet novelty**: ✅ VERIFIED. arXiv:2409.00094 applies CJT to cross-model LLM ensembles (different angle). No prior work applies Fleiss' κ or Eff-K to within-model SC traces. Our framing is novel.
319	- **exp-050b complication**: ICL transition Δ=-3.52pp at SC=57.79% complicates simple "SC determines SICA." Explain via trace generation characteristic change.
320	- **Variable naming inconsistency**: 56.4% cross-trace pairs share zero Z3 variables. Key mechanism evidence.
321	
322	## Required Citations (minimum 30 references)
323	
324	- **SC & extensions**: Wang et al. 2023 (SC), Chen et al. 2023 (USC), Loo et al. 2025 (SC scaling plateaus), Taubenfeld et al. 2025 (weighted SC), DiVeRSe (Li et al. 2023)
325	- **Neuro-symbolic reasoning**: DyLoS (EACL 2026), Aristotle (ACL 2025), FoVer (TACL 2025), LogicAgent (2025), Logic-LM (Pan et al. 2023), LINC (Olausson et al. 2023)
326	- **Condorcet/voting theory**: Condorcet 1785, Austen-Smith & Banks 1996, **arXiv:2409.00094 (Examining Independence in Ensemble Sentiment Analysis, Sept 2024)** — closest prior work, applies CJT to cross-model LLM ensembles, finds independence violation. Our novelty: within-model trace independence + Fleiss' κ quantification + Eff-K + connection to symbolic aggregation
327	- **Test-time compute**: Snell et al. 2025, DeepSeek-R1, Diversity-Aware Training
328	- **Verification & reranking**: ORM (Cobbe et al. 2021), PRM (Lightman et al. 2023), Math-Shepherd
329	- **Constraint satisfaction**: SATBench (EMNLP 2025), LLM Meets Constraint Propagation (IJCAI 2025)
330	- **Debate & multi-agent**: Liang et al. 2023, Du et al. 2023
331	
332	## Additional Reviewer Concerns (D070/D074 Methods)
333	
334	17. **"Why not use a larger model for constraint generation?"** → Valid. All methods tested at 7B scale. ICG constraint parsing failures + Debate role-play degradation may be scale-dependent. This is explicitly noted as limitation and future work. The contribution is diagnosing the bottleneck and showing it's not trivially fixable, not claiming no fix exists at any scale.
335	18. **"Only tested one model (Mistral-7B) for methods"** → Methods are interventions on the extraction pipeline, not the base model. Testing on the same model that showed the clearest Goldilocks signal (Mistral-7B FOLIO) is the strongest test — if methods can't improve the best-case scenario, they won't help elsewhere.
336	19. **"ICG multi-seed shows 1/3 positive"** → Magnitudes (-2.0, +1.5, -1.0) are within SC baseline noise (3.5pp cross-seed). Mean ≈-0.5pp, std=1.8pp. No statistical significance. Properly framed as "noise-level, neither improving nor degrading."
337	20. **"Debate working in other papers"** → Multi-agent debate literature uses diverse models or much larger models. Same-model 7B debate is a different regime. Our finding is specifically about same-model self-extraction limitations.
338	
339	## Claim Scoping Rules
340	- n=60 conditions: "suggestive/consistent with" NOT "confirming"
341	- n≥200 conditions: can "confirm"
342	- Combined N>1,300: acceptable if breakdown clearly stated
343	- Method claims: must show statistically significant improvement OR clear directional improvement with analysis
344	- "Independence bottleneck" framing: systematic quantification + theoretical grounding
345	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a080a9f5-97fe-4315-ba24-f9ed98932995",
  "isSidechain": false,
  "promptId": "3f50ba00-7d30-45ec-b450-7010d531c858",
  "type": "user",
  "uuid": "d30f6760-b1d7-40e2-b49a-c9356dbd59eb",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/paper_framing.md",
      "content": "# Paper Framing — symb_invariant_consensus\n\n## Target Venue\n- Primary: EMNLP 2026 Main (ARR May 25)\n- Deadline: May 25, 2026 (ARR submission)\n\n## D063 Direction: Entropy Decomposition + Quality Ladder — 目标 4.0\n\n**从 D060 \"Pure Analysis / negative result\" 升级为 \"Regime-Dependent Mechanism Analysis with Entropy Decomposition\"。** 用户决定冲 4.0。\n\n### Entropy Breakdown 验证结果 (2026-05-19 completed)\n\n**跨模型 entropy mechanism 一致性: 不成立。Selective SICA 非 universal 方案。**\n\n但 entropy decomposition 揭示了更有价值的 regime mechanism：\n\n| Experiment | Model | Dataset | High-E n | High-E Δpp | Low-E n | Low-E Δpp |\n|-----------|-------|---------|----------|-----------|---------|----------|\n| exp-033 s42 | Mistral-7B | FOLIO | 78 | **+12.8** | 126 | 0.0 |\n| exp-052 s123 | Mistral-7B | FOLIO | 77 | **+9.1** | 127 | 0.0 |\n| exp-053 s456 | Mistral-7B | FOLIO | 75 | -1.3 | 129 | 0.0 |\n| exp-046 | Mistral-7B | PW-600 | 267 | -4.9 | 333 | -1.2 |\n| exp-036 | Qwen2.5-14B | FOLIO | 37 | **-8.2** | 167 | -0.6 |\n| exp-038 | Qwen2.5-14B | LogiQA | 23 | -4.3 | 177 | 0.0 |\n| exp-035 | Qwen2.5-7B | FOLIO | 47 | -2.1 | 157 | 0.0 |\n| exp-048 | LLaMA-8B | PW-600 | 76 | -3.9 | 104 | -1.9 |\n\n(注: SC/Δ 使用 pre-tiebreaking 值，entropy grouping 不受 tiebreaking 影响。D064 修正后 deltas 会略有变化但 pattern 不变。)\n\n**三个核心发现：**\n1. **Low-entropy: SICA≈SC 跨模型一致** (8/8 experiments Δ≈0) → traces 一致时 constraints 无新信息\n2. **High-entropy 方向因 regime 而异**：Goldilocks +12.8pp vs Type A -8.2pp vs Type C -4.9pp\n3. **Mechanism 解释**：\n   - Goldilocks (SC~55%, κ~0.46): 真实不确定性 → constraints 打破平局正确方向\n   - Type A (SC>75%, κ>0.65): 偶发错误 → constraints 放大 confirmation bias\n   - Type C (SC<40%, κ~0.20): 系统性错误 → constraints 是噪声\n\n### 调整后核心转变\n\n论文以 \"entropy decomposition 揭示 regime-dependent mechanism\" 为核心分析贡献（不是 universal diagnostic）：\n- **Entropy decomposition 作为分析工具**：分离 SICA 作用点（high-entropy）vs 不作用点（low-entropy）\n- **Regime mechanism 量化**：同样是 high-entropy 问题，direction depends on SC+κ → 完美支持 dual bottleneck\n- **Abandoned**: Selective SICA 作为 universal practical contribution（只在 Goldilocks zone 有效）\n- **Upgraded**: 核心图 = high-entropy Δ vs SC scatter（8 points, 3 regimes 清晰分离）\n- **Quality Ladder** (D067: L1 NULL CONFIRMED)\n  - L0: Self-extraction (Mistral→Mistral): 59.31%, Δ=+3.43pp ns\n  - L1a: Qwen3-14B→Mistral traces: 60.29%, Δ=+4.41pp (+0.98pp vs self = 2题/204 = noise)\n  - L1b: Qwen2.5-14B→Mistral traces: 58.33%, Δ=+2.45pp (-0.98pp vs self = 2题/204 = noise)\n  - L3: Oracle 100% disc, Δ=+14.22pp p<0.001\n  - **结论**: L1 ≈ L0 << L3。Bottleneck 在 traces（同源输入），不在 extractor（换模型无效）\n  - **Paper contribution**: \"bottleneck is fundamental to extraction, not just model capability\" — 强化 structural limitation 论点\n- **CJT/Eff-K 保留**：解释 why high-entropy behavior differs across regimes\n\nD060 要素全部保留：\n- Condorcet independence 框架 → 理论基础\n- 9 种修复全部失败 → structural limitation 证据\n- 2/3 seeds positive trend but **0/3 significant** (D066: p=0.092/0.070/1.0) → Goldilocks zone 作为 directional trend, not confirmed effect\n- K/T sensitivity non-monotonic → SC confound insight\n- 用户指示: 投 May 25 不变，冲 4.0\n\n## Core Claims (5 条) — D060 纯 Analysis Framing\n\n### Analysis Claims (已验证)\n\n1. **Independence Bottleneck**: Self-consistency 隐含 Condorcet Jury Theorem 的独立性假设，但同模型采样的 traces 高度相关。Worker 验证的 κ 值：\n   - Qwen-14B FOLIO: κ=0.744, Eff-K=1.31 (SC=75.49%, Δ=+0.25pp n.s.)\n   - Qwen-14B LogiQA: κ=0.821, Eff-K=1.20 (SC=78.5%, Δ=+0.50pp n.s.)\n   - Mistral-7B FOLIO s42 (exp-033): κ=0.501, Eff-K=1.84 (SC=55.88%, Δ=+3.43pp **p=0.092 ns**) ← primary seed [D064+D066]\n   - Mistral-7B FOLIO s123: κ=0.491, Eff-K=1.88 (SC=54.41%, Δ=+2.94pp **p=0.070 ns**)\n   - Mistral-7B FOLIO s456: κ=0.507, Eff-K=1.82 (SC=55.88%, Δ=0.00pp p=1.0 ns)\n   - Mistral-7B PW-600 (exp-046): κ=0.210, Eff-K=3.63 (Δ=-2.83pp p=0.010, SC=39%)\n   规律：跨模型对比清晰（Qwen Eff-K≈1.2-1.3 → 0 gain; Mistral Eff-K≈1.85-2.22 → variable gain）。但 Mistral seeds 内部，Eff-K 与 delta 非单调（exp-033 Eff-K 最低 1.85 却 delta 最高 +3.43pp）→ Eff-K 是跨模型必要条件，seed 内 variance 仍主导。exp-046 Eff-K 最高(3.63) 但 SC 太低(39%) 导致 delta 为负 → 需同时满足 sufficient Eff-K AND sufficient SC。\n\n2. **Oracle Gap Localizes Extraction Bottleneck**: Gold FOL + MAX-SAT = +14.22pp (p=2.0e-7)，自提取仅 +3.43pp (best seed, D064 corrected) = 24% utilization。聚合机制本身有效，瓶颈在自提取质量。Two-layer analysis:\n   - **Constraint taxonomy**: 43% trivially_satisfied（被所有候选答案满足的约束，不排除任何答案）\n   - **Discriminative filtering**: 仅 ~8% 约束在 MAX-SAT scoring 中完全 non-discriminative（移除后 0 gains）\n   - **关键区分**: 43% 和 8% 度量不同。trivially_satisfied 约束在 MAX-SAT 中仍可有不同满足程度（partial vs full），所以不全是 non-discriminative。但即使 constraints 是 discriminative 的，它们的\"区分方向\"与模型自身偏差一致（confirmation bias）。both_wrong 组 score_range=29.4。九种修复全部失败。\n\n3. **Regime-Dependent Capability Trap**: SICA 有效性取决于提取模型的基线准确率，存在双边界：\n   - Type A (SC ≥ ~60%): 确认偏差，constraints 镜像模型自身答案。**exp-034 vs exp-039 同配置 delta 翻转**: exp-034 Δ=+0.51pp (n=589), exp-039 Δ=-2.00pp (n=600)。SC baseline 方差 (3.38pp) >> SICA 效应 → Type A delta 是 trace sampling noise。SICA 比 SC 更稳定 (跨运行方差 0.87pp vs 3.38pp，仅 2 点，需更多 seed 验证)\n   - Type C (SC ≤ ~40%): traces 主要错误，constraints 是噪声 (exp-046: Δ=-2.83pp, p=0.0095)\n   - Goldilocks zone (~50-56% SC): 部分独立性 + 部分正确性 (exp-033: Δ=+3.43pp, p=0.092 ns; mean of 3 seeds: +2.12pp) ⚠️ D076 Reviewer: 0/3 seeds significant, 不应作为核心叙事支柱。作为 directional observation 保留，不做强 claim。\n   - Type B: 领域不可形式化 (LogiQA: contradiction rate 0.8%)\n\n4. **C0+SC Two-Dimensional Diagnostic**: C0 (multi-candidate rate) + SC accuracy 形成零成本部署诊断。C0<5% → degenerate; high C0 + high SC → trap; high C0 + low SC → potential gains。\n\n### Remediation Evidence (D060: 全部失败 — 强化 analysis narrative)\n\n5. **Nine Remediation Attempts All Failed**: 原 6 种 + 3 种靶向修复全部无效，证明 independence bottleneck 是结构性的：\n   - D059 三路 method improvement 全部失败：\n     - Discriminative Filtering: 119/204 处理后 0 gains 1 loss，~92% 约束本身就是 discriminative，过滤是 near-no-op\n     - T=1.0 (exp-054): delta 从 +3.43pp 崩塌到 0.00pp（D064 corrected），温度敏感性极端\n     - Multi-Temp (exp-055): ✅ 完成，delta=+0.00pp (b=5,c=5 完美对称), SC=57.84%. 混合 T=0.3/0.7/1.2 各 4 traces 未改善 SICA。附带发现：multi-temp 提升 SC baseline (+3.4pp vs 单温度 54.41%)，说明混合温度对 majority voting 有帮助，但 SICA constraint extraction 无法利用这种 diversity → bottleneck 在 extraction 而非 trace diversity\n   - 原 6 种：contrastive prompting, cross-model extraction, generational scaling, solver-guided refinement, consistency filtering, cross-trace UNSAT\n   - 9 种修复涵盖 prompting / architecture / capability / verification / diversity / filtering 全维度，全部失败 → trap is fundamental\n\n## D070/D074 Update: Method-Level Interventions Also Fail — \"Fundamental Limitation\" Confirmed\n\n### Three Method Lines × Two Datasets = All Negative (D074)\n\nD070 从纯 analysis 升级为 analysis + method paper，但三条方法线全面失败（D074 确认），反而强化了原始 analysis 结论。\n\n**方法×数据集完整结果**：\n| Method | FOLIO-204 | LogiQA-200 | Failure Mode |\n|--------|-----------|------------|--------------|\n| ICG (Independent Constraint Gen.) | Δ=-2.0pp (3-seed: -2.0/+1.5/-1.0, mean=-0.5pp±1.8pp, 噪声) | Δ=-0.5pp | Neutral — 独立约束质量≈trace-sourced约束 |\n| Contrastive (Pro/Con Scoring) | Δ≈-16pp | Δ≈-7pp (interim) | Harmful — 26% degenerate scoring, pro/con 不平衡 |\n| Debate (Proposer/Critic) | Δ=-18.6pp | Δ≈-28pp (interim) | Catastrophic — 7B 模型角色扮演严重退化推理 |\n\n**三种失败模式的分析价值**（论文 \"Why Methods Fail\" section）：\n1. **ICG (neutral)**: 独立于 traces 生成的约束不比 trace-sourced 约束更好。说明 bottleneck 不仅是 \"约束来自 traces\"，而是模型的推理偏差从问题理解阶段就存在——独立约束和 trace-sourced 约束继承相同的 model bias。\n2. **Contrastive (harmful)**: 强制 pro/con 评估引入 degenerate scoring（26% 问题无法有效区分）。7B 模型无法可靠生成平衡的对立约束——pro 约束系统性多于 con（94 pro vs 65 con），confirmation bias 从约束提取转移到了约束生成。\n3. **Debate (catastrophic)**: Proposer/Critic/Defense 多角色链在 7B 模型上导致答案质量严重退化。辩论不仅未增加多样性，反而引入了角色扮演的额外认知负担。同模型辩论 = 同源性 + 角色扮演退化，双重损失。\n\n**Scale limitation caveat**: 所有方法测试在 7B 模型上。7B 模型生成 Z3 格式 FOL 约束的能力不足（ICG 多题 \"0/N constraints parsed\"）。14B+ 模型可能有不同结果——这既是 limitation 也是 future work 入口。\n\n### κ Generalization — Independence-Accuracy Trade-off (D075, CAPSTONE FINDING)\n\nexp-077 测量三种聚合方式在 Mistral-7B FOLIO-204 上的 κ 和 Eff-K：\n| 聚合方式 | Fleiss' κ | Eff-K | 名义 K |\n|----------|----------|-------|--------|\n| Self-Consistency | 0.4384 | 2.02 | 10 |\n| Diverse-Prompt | 0.4030 | 2.21 | 12 |\n| LLM-Debate | 0.1549 | 4.44 | 12 |\n\n结合 exp-076 Debate Δ=-18.6pp 的准确率数据，揭示**同模型框架下的 fundamental independence-accuracy trade-off**：\n- **SC/Diverse-Prompt**: κ~0.4，traces 高度相关但准确率正常。换 prompt 策略不改善独立性（Δκ=0.04）。\n- **Debate**: κ=0.15，成功打破 trace 相关性（Eff-K 从 2.0 跃升到 4.4），但准确率崩溃 -18.6pp。低 κ 不代表\"更独立的推理\"——是 disagreement amplification（系统性噪声）。\n- **Trade-off 本质**: 同一模型的推理能力是固定的。要么输出一致（高 κ, 正确但不独立），要么输出分歧（低 κ, 独立但不正确）。Condorcet Jury Theorem 要求 both independent AND accurate，同模型框架下无法同时满足。\n\n**论文叙事升级**: 从 \"methods fail\" → \"independence-accuracy trade-off is fundamental to same-model reasoning\"。突破瓶颈需要跨模型方案（不同模型天然更独立），Oracle 实验（gold FOL 来自外部知识源）已间接验证了这一点。\n\n### New Claim 6 (D070/D074)\n\n6. **Method-Level Interventions Cannot Break the Bottleneck**: 三种针对 independence bottleneck 不同环节的方法（ICG→循环依赖, Contrastive→confirmation bias, Debate→trace 同质性）在 2 个数据集上全部失败。加上之前 9 种 prompt-level 修复，共 12 种修复尝试全败。这证明 independence bottleneck 不是单一环节的问题，而是 same-model self-extraction 的根本性限制。\n\n### New Claim 7: Symbolic Confirmation Bias (D082 — CORE FINDING)\n\n7. **Symbolic Confirmation Bias**: LLM 从 CoT traces 提取的 FOL 约束系统性确认 trace 自身（可能错误的）答案，而非独立验证 ground truth。\n   - SICA 判对题：gold constraint 78.1%，bias ratio = 0.28\n   - SICA 判错题：错误 constraint 83.3%，bias ratio = **4.97×**\n   - 97.6% SICA 错误与 SC 错误完全重合\n   - SICA 翻盘的 12 例来自 minority trace diversity（43% gold support），不是 symbolic reasoning\n   - **因果链**：模型推理→答案→从含答案 trace 提取 FOL→约束确认答案→聚合≈SC\n   - **CEGIS 验证**：迭代精炼 R1 +3.43pp < 原始 SICA +4.9pp → 约束一致性不是瓶颈，偏向性才是\n   - **Quality Ladder 验证**：L1 ≈ L0 << L3 → bottleneck 在 traces（同源输入），不在 extractor\n\n### New Claim 8: Process-κ (D082 — NEW METRIC)\n\n8. **Process-Level Independence (Process-κ)**: answer-κ 低估真实独立性瓶颈。CoT 推理过程相似性远高于答案一致性。\n   - Mistral-7B FOLIO-204：CoT cosine similarity **0.69** >> answer-κ **0.41**\n   - 两者几乎无相关性：r = -0.06, p = 0.36\n   - 仅 **9.3%** trace 对是\"殊途同归\"（同答案不同路径）\n   - answer-κ 是 true independence bottleneck 的 lower bound\n   - 适用于所有 LLM trace aggregation 方法，不限于 SICA\n\n## D082/D085: Comprehensive Method Exhaustion — 25+ ALL Fail\n\nD080 启动全方向并行探索（Wave 1-3），在 D074 的 12 种修复基础上又测试 13+ 新干预：\n\n| 方法 | 类型 | 结果 | 关键数据 |\n|------|------|------|----------|\n| PROVE 代码验证 | paradigm shift | ❌ | Code gen 15.2%, accuracy=random |\n| CEGIS 迭代精炼 | multi-round | ❌ | R1 +3.43pp < SICA +4.9pp |\n| DeepConf 置信度 | filtering | ❌ | logprob 与正确性零相关 |\n| Cross-model SICA | cross-model | ❌ | Δ=-0.49pp despite lower κ |\n| Problem Perturbation | input diversity | ❌ | κ 升至 0.696 (反效果) |\n| MIN-UNSAT | solver objective | ❌ | 49.5% < SC 54.4% |\n| κ-aware SC | voting rule | ❌ | 11/11 Δ=0 |\n| Z3 Trace Filter | trace filtering | ❌ | negative |\n| Bootstrapped Gold | iterative | ❌ | negative |\n| Selective Abstention | diagnostic | ⚡ | AUROC=0.673, +4.4pp@80%cov |\n\n**D085 总结**: 9 prompt-level + 3 method-level + 13 新方向 = **25+ 干预全部 negative**。Independence bottleneck 在 same-model self-extraction 框架下无解，所有维度（diversity/architecture/capability/verification/filtering/voting/solver/paradigm）已穷尽。\n\n### Updated Headline Result (D085)\n\n\"Across 6+ models and 4 domains, symbolic consensus aggregation shows no statistically significant positive effect. 25+ interventions spanning prompt engineering, method-level redesign (ICG, Contrastive, Debate), solver modifications, cross-model aggregation, code-based verification, and iterative refinement all fail. We identify the root cause as Symbolic Confirmation Bias: self-extracted FOL constraints systematically confirm the trace's own answer (bias ratio 4.97× on incorrect problems), making symbolic aggregation equivalent to majority voting. Process-level analysis reveals reasoning paths are far more homogeneous than answers suggest (cosine similarity 0.69 vs answer-κ 0.41). The one method that breaks trace correlation (Debate: κ 0.44→0.15) does so at catastrophic accuracy cost (-18.6pp), revealing a fundamental independence-accuracy trade-off. Oracle constraints prove the aggregation mechanism works (+14.22pp, p<0.001), localizing the bottleneck entirely to self-extraction quality.\"\n\n### Updated Story Spine (D074)\n\n- **Problem**: [unchanged]\n- **Theoretical lens**: [unchanged]\n- **Systematic evaluation**: [unchanged]\n- **Regime characterization**: [unchanged]\n- **Remediation failures strengthen thesis (D085 FINAL)**: 9 prompt-level + 3 method-level + 13 new directions = **25+ interventions** across ALL dimensions (diversity/architecture/capability/verification/filtering/voting/solver/paradigm), all fail → bottleneck is fundamental and exhaustively proven\n- **Method failure analysis**: Three methods targeting different bottleneck aspects show three distinct failure modes (neutral/harmful/catastrophic), revealing that the bottleneck operates at multiple levels simultaneously\n- **Independence-accuracy trade-off (HERO FINDING, D075)**: Debate breaks trace correlation (κ 0.44→0.15, Eff-K 2.0→4.4) but accuracy collapses (-18.6pp/-23.0pp). Same-model traces can be independent OR accurate, not both.\n- **NEW — Symbolic Confirmation Bias (CORE FINDING, D082)**: Root cause identified — self-extracted FOL constraints systematically confirm the trace's own answer (bias ratio 4.97× on incorrect problems). Causal chain: model reasons → answer → FOL extraction confirms answer → aggregation ≈ SC. This is WHY 25+ methods fail.\n- **NEW — Process-κ (NEW METRIC, D082)**: CoT reasoning similarity (0.69) >> answer-κ (0.41), r=-0.06. Only 9.3% of trace pairs are \"convergent reasoning.\" answer-κ underestimates the true bottleneck. Novel metric applicable to all LLM trace aggregation.\n- **Actionable contribution**: C0+SC diagnostic + κ-based Eff-K estimation = zero-cost deployment toolkit. κ analysis shows SC itself has a scaling ceiling (Eff-K ≈ 2 means K>12 traces yield diminishing returns).\n- **Universal across architectures (D078)**: Three families: Mistral-7B κ=0.438, LLaMA-8B κ=0.412, Qwen2.5-7B κ=0.658, Qwen2.5-14B κ=0.738. Family effect (Δκ=0.22) >> scale effect (Δκ=0.08).\n- **Headline (D085)**: Independence bottleneck is structural, universal across architectures, and rooted in Symbolic Confirmation Bias. 25+ interventions spanning all conceivable dimensions fail. Process-κ reveals reasoning homogeneity far exceeds answer-level agreement. The independence-accuracy trade-off constrains all same-model trace aggregation.\n\n## Core Insight (D060 Updated — Dual Bottleneck)\n\n**Dual Requirement Framework**: SICA 效应需要同时满足两个条件，缺一不可：\n1. **Sufficient Independence** (Eff-K > threshold): traces 需要提供足够多的独立视角\n2. **Sufficient Quality** (SC > ~50%): traces 需要有足够的正确率，否则约束是噪声\n\nCondorcet Jury Theorem 要求投票者独立且 p>0.5。同模型采样的 reasoning traces 严重违反独立性假设（Fleiss' κ = 0.21–0.82，Eff-K 仅 1.20–3.63），解释了为什么简单增加 K 或添加符号约束不能突破 SC 的天花板。\n\n实验数据完美支持 dual requirement（κ 使用统一脚本 compute_fleiss_kappa_unified.py，SC/Δpp 使用 registry 原始值）：\n- **Qwen family**: κ=0.66-0.82, Eff-K≈1.20-1.46（独立性不足）→ all near-zero delta，无论 SC 多高\n- **Mistral-7B FOLIO**: κ≈0.46, Eff-K≈2.0（中等独立性）+ SC≈55%（中等质量）→ +3.43pp best seed, mean +2.12pp (2/3 seeds positive, 1 null)\n- **Mistral-7B PW-600**: κ=0.20, Eff-K=3.76（最高独立性）但 SC=39%（质量不足）→ -2.83pp\n- 只有 Goldilocks zone（中等 Eff-K + 中等 SC）出现正向 delta\n- **Dual bottleneck 直接验证 (exp-055)**：Multi-temp κ=0.427 Eff-K=2.11（比单温度 κ≈0.46 Eff-K≈2.0 更独立）但 delta=0.00pp → 提高 independence 不够，还需要 extraction quality\n- **T sensitivity 孤立尖峰 (4/4 complete, D064 corrected)**：T=0.3(Δ=-1.47), T=0.5(Δ=-0.98), T=0.7(Δ=+3.43, κ=0.460, Eff-K=1.98), T=1.0(Δ=0.00, κ=0.394, Eff-K=2.25)。T=0.7 孤立尖峰更突出。T=0.7 SC=55.88%（最低）→ entropy 最高 → SICA 操作空间最大。温度效应与 SC 效应互为 confound，论文需讨论\n- **Thinking mode κ=0.913, Eff-K=1.09 (exp-028b)**：近乎确定性。思维模式让 traces 更一致 → 独立性更差。\"更好的推理\"反而加剧 independence bottleneck。\n\n**κ 是 model-level 稳定属性**：统一处理后 Mistral 三 seed κ 收敛至 0.457-0.460（之前 0.41-0.50 差异是非标准 answer 处理的 artifact）。κ 跨 seed 几乎相同，但 delta 差异大（+3.43 vs +2.94 vs 0.00）→ seed-level constraint quality variance 主导，非 κ。\n\n完整 κ 表（⚠️ D062: κ 将用 raw answers 重算，当前 unified 值为临时值。Qwen 无变化，Mistral 条件将更新）：\n| Exp | Model | κ(unified→raw pending) | Eff-K | SC%(registry) | Δpp(registry) |\n|-----|-------|------------|-------|---------------|---------------|\n| exp-028b | Qwen3-14B thinking | 0.913 | 1.09 | ~84% | ~0 |\n| exp-038 | Qwen-14B LogiQA | 0.821 | 1.20 | 78.50 | -0.50 |\n| exp-027 | Qwen3-14B | 0.773 | 1.26 | 84.31 | +0.49 |\n| exp-036 | Qwen2.5-14B | 0.744 | 1.31 | 75.49 | +0.25 |\n| exp-035 | Qwen2.5-7B | 0.658 | 1.46 | 76.47 | -0.49 |\n| exp-049b | Mistral-7B LogiQA | 0.512 | 1.81 | 51.00 | +0.50 |\n| exp-057 | Mistral-7B T=0.3 | 0.502 | 1.84 | 58.33 | -1.47 |\n| exp-058 | Mistral-7B T=0.5 | 0.516 | 1.80 | 58.33 | -0.98 |\n| exp-033 | Mistral-7B s42 | 0.460 | 1.98 | 55.88 | +3.43 |\n| exp-052 | Mistral-7B s123 | 0.457 | 1.99 | 54.41 | +2.94 |\n| exp-053 | Mistral-7B s456 | 0.457 | 1.99 | 55.88 | 0.00 |\n| exp-055 | Mistral-7B multi-T | 0.427 | 2.11 | 57.84 | 0.00 |\n| exp-054 | Mistral-7B T=1.0 | 0.394 | 2.25 | 55.39 | 0.00 |\n| exp-046 | Mistral-7B PW-600 | 0.200 | 3.76 | 39.33 | -2.83 |\n注：κ 基于 T/F/U 三类归一化，Mistral-7B 约 12-16% traces 被归一化（Qwen 100% valid）。Mistral SC/Δpp 已更新为 D064 tiebreaking 修正值；Qwen 不受影响。\n\nOracle control (+14.22pp) 证明 MAX-SAT 聚合机制本身有效，但自提取约束仅利用了 24% 的理论上限。Discriminative filtering 实验揭示关键机制：~92% 约束 ARE discriminative，但过滤掉 ~8% non-discriminative 约束后 delta 不变（0 gains）。问题不在约束缺乏判别力，而在于 discriminative constraints 的区分方向与模型偏差一致（confirmation bias）。\n\n**Remediation insight (D060)**: 9 种修复尝试全部失败，包括直接靶向 independence（multi-temp diversity, exp-055: Eff-K 从 2.0→2.11 但 delta 仍为 0）和 constraint quality（discriminative filtering）。这证明 bottleneck 不是简单的 diversity 或 quality 问题，而是 same-model self-extraction 的根本性限制。\n\n**Key evidence**:\n- **Condorcet independence quantification (统一脚本, 公式: Eff-K=K/(1+(K-1)κ))**: Mistral-7B FOLIO κ≈0.46 (Eff-K≈2.0, 三 seed 高度稳定), Mistral-7B PW-600 κ=0.200 (Eff-K=3.76), Qwen2.5-14B FOLIO κ=0.744 (Eff-K=1.31), Qwen2.5-14B LogiQA κ=0.821 (Eff-K=1.20), Qwen3-14B κ=0.773 (Eff-K=1.26), Qwen2.5-7B κ=0.658 (Eff-K=1.46). 跨模型清晰: Qwen Eff-K≈1.2-1.5→0 gain, Mistral FOLIO Eff-K≈2.0→variable gain, Mistral PW Eff-K=3.76 but SC too low→negative. κ stable across seeds (0.457-0.460), delta varies → seed-level constraint quality dominates.\n- **Oracle control (exp-031)**: Gold FOL + MAX-SAT = 89.71% vs SC 75.49% (+14.22pp, p=2.0e-7). Unknown-type +31.9pp.\n- **Two-layer constraint analysis**: 43% trivially_satisfied (taxonomy: satisfied by ALL answers) vs ~8% non-discriminative (filtering: same MAX-SAT score). Difference: trivially_satisfied constraints can still have different satisfaction DEGREES. Removing the 8% yields 0 gains → problem is not quality but confirmation bias direction.\n- **K sensitivity (non-monotonic peak at K=12, 5/5 complete, D064+D066)**: K=4(-1.47pp), K=8(-1.96pp), K=12(+3.43pp p=0.092 ns), K=16(+1.47pp), K=20(+1.96pp). Peak at K=12, drops at K=16 but partially recovers at K=20. NOT clean inverted-U. K=12 SC=55.88% (post-fix). SC-confound with T sensitivity still holds. SICA at K=4 vs K=12 differs by ~4.9pp despite similar SC — proves SICA extracts different information than SC.\n- **SC-confound (cross-cutting insight)**: K=12 和 T=0.7 都是 SC 最低 (54.41%) 的配置 → SICA \"最佳超参\"可能反映 entropy/operating-window 效应而非 K 或 T 的因果贡献。论文需要讨论这个 confound，但也可以正面利用：SC level 是更基本的预测变量，K 和 T 通过影响 SC 来间接影响 SICA delta。\n- **T sensitivity (isolated peak, 4/4 complete, D064 corrected)**: T=0.3(Δ=-1.47pp), T=0.5(Δ=-0.98pp), T=0.7(Δ=+3.43pp p=0.092 ns), T=1.0(Δ=0.00pp). NOT smooth inverted-U — T=0.7 is an isolated spike. T=0.7 has lowest SC (55.88%) → highest entropy → largest SICA operating window. Temperature and SC effects confounded. Strengthens fragility narrative.\n- **Regime boundary**: Qwen-14B (SC=75.49%) Δ=-0.98pp vs Mistral-7B (SC=55.88%) Δ=+3.43pp p=0.092 ns\n- **Type C failure (exp-046)**: Mistral PW-D5 SC=39.33%, Δ=-2.83pp, p=0.010, κ=0.210, Eff-K=3.63, contradiction rate 5.5%. Highest Eff-K yet worst delta → independence alone insufficient when SC too low.\n- **Seed replication (D064+D066)**: 2/3 seeds positive but **0/3 significant** after tiebreaking correction: s42 Δ=+3.43pp p=0.092, s123 Δ=+2.94pp p=0.070, s456 Δ=0.00pp p=1.0. Mean +2.12pp. Only significant McNemar effects are NEGATIVE: exp-046 Δ=-2.83pp p=0.014, exp-039 Δ=-2.50pp p=0.011. Paper must frame as \"positive directional trend\" not \"significant positive effect\".\n- **Nine remediation failures (ALL CONFIRMED)**: contrastive prompting, cross-model, generational scaling, solver-guided, consistency filtering, cross-trace UNSAT, discriminative filtering (0 gains), T=1.0 (delta collapse +3.43→0.00pp, D064 corrected), multi-temp (delta=+0.00pp, b=5 c=5). All 9 failed → trap is fundamental, bottleneck is structural.\n- **Entropy decomposition (VERIFIED 2026-05-19)**: High-entropy proportion: Mistral FOLIO 38% (78/204) vs Qwen FOLIO 18% (37/204) vs Qwen LogiQA 12% (23/200). SICA on high-entropy: Mistral FOLIO s42 +12.8pp, s123 +9.1pp, s456 -1.3pp; Qwen FOLIO -8.2pp; all others negative. Low-entropy: SICA≈SC across all 8 experiments (Δ≈0). Entropy decomposition reveals regime-dependent mechanism, NOT universal diagnostic.\n- **Confirmation bias quantification**: ⚠️ \"62.3%\" and \"28.6%\" confirmed NOT present in any .tex file — likely hallucinated in earlier draft. DO NOT USE. Replace with verified metrics from experiment outputs only.\n\n## Story Spine (D059 Updated)\n\n- **Problem**: LLMs' reasoning can be improved by sampling multiple chains-of-thought and aggregating via majority voting (self-consistency). Recent work proposes symbolic augmentation: extract formal constraints from traces and use SAT solvers for answer selection. But does symbolic aggregation actually outperform simple voting?\n- **Theoretical lens**: Condorcet Jury Theorem requires voter independence. We quantify trace independence via Fleiss' κ and show Effective-K << nominal K. This explains the fundamental limitation of same-model trace aggregation.\n- **Systematic evaluation**: SICA (MAX-SAT over FOL constraints) across 3 domains × 5 model families. Oracle control separates extraction vs aggregation failure. Discriminative filtering reveals ~92% constraints are discriminative, yet SICA gains are fragile — confirmation bias, not constraint quality, is the bottleneck.\n- **Regime characterization**: Three failure modes (Type A/B/C) + narrow Goldilocks zone. C0+SC as deployment diagnostic.\n- **Remediation failures strengthen thesis**: 9 targeted interventions (prompting, architecture, capability, verification, diversity, filtering) all fail to close the oracle gap, proving the bottleneck is fundamental to same-model self-extraction.\n- **Headline result (D066 McNemar corrected)**: \"Across 6 models and 4 domains, symbolic consensus aggregation shows no statistically significant positive effect under corrected tiebreaking (best seed +3.43pp, p=0.092). The only significant effects are negative (PW-600: -2.83pp p=0.014, -2.50pp p=0.011). However, entropy decomposition reveals a striking regime-dependent pattern: SICA's entire effect concentrates on high-entropy questions, with +12.8pp in the Goldilocks zone but -2 to -8pp elsewhere. Oracle constraints prove the aggregation mechanism works (+14.22pp, p<0.001), localizing the bottleneck to extraction quality (24% utilization). Condorcet analysis (Eff-K=1.2-2.0 for nominal K=12) explains trace non-independence. Nine remediation strategies all fail, confirming the bottleneck is structural to same-model self-extraction.\"\n\n## Anticipated Reviewer Concerns & Defensive Experiments\n\n1. **\"Gains not statistically significant\"** → Correct: no positive effect reaches significance (best p=0.092). This IS the finding. Oracle p=2.0e-7 proves the mechanism works; the insignificance of self-extraction gains demonstrates the extraction bottleneck. Regime pattern (8 entropy conditions) provides systematic evidence beyond any single p-value.\n2. **\"Only one positive result (exp-033)\"** → Seed replication: 2/3 positive (s42 +3.43pp, s123 +2.94pp), 1/3 null (s456 0.00pp). Mean +2.12pp. Effect IS real but fragile — the fragility itself IS the finding.\n3. **\"Condorcet framework is trivial\"** → Fleiss' κ quantification is novel in SC/SICA context. Eff-K is actionable: tells practitioners how many truly independent traces they get.\n4. **\"Multi-temp / filtering should work\"** → We tried both. Multi-temp (exp-055): negative. Disc. filtering: 0 gains. T=1.0: delta collapse. These failures STRENGTHEN the structural bottleneck thesis.\n5. **\"Only Qwen models\"** → 5 families: Qwen-14B, Mistral-7B, LLaMA-8B, DeepSeek-R1-7B, QwQ-32B.\n6. **\"Only logic domain\"** → FOLIO + ProofWriter + LogiQA + StrategyQA + ARC-Challenge. Type B (domain formalizability) is itself a finding.\n7. **\"Oracle is unfair comparison\"** → Diagnostic tool, not competing method. Separates extraction from aggregation.\n8. **\"MAX-SAT is over-engineering\"** → exp-013: MaxSAT ≈ count-only. This IS the independence bottleneck evidence.\n9. **\"Self-extraction confound\"** → Oracle control resolves completely.\n10. **\"Published methods achieve gains (DyLoS, Aristotle, FoVer)\"** → Different paradigm (external verifiers/trained extractors). We characterize same-model self-extraction.\n11. **\"C0 is trivially derived\"** → Zero-cost early stopping. Practical value.\n12. **\"Why not just use a reasoning model?\"** → QwQ-32B: C0<5%, SICA≡SC.\n13. **\"Random tiebreak baseline\"** → exp-003: SICA tiebreak 80% vs random 50%.\n14. **\"Method improvement is incremental\"** → Grounded in diagnosis (independence + taxonomy), not ad-hoc.\n15. **\"Weighted SC is simpler\"** → exp-016 planned. Weighted SC doesn't address independence.\n16. **\"Within-model ICL transition contradicts regime theory\"** → exp-050b (SC=57.79%, Δ=-3.52pp): ICL changes trace generation characteristics, not just SC level. Paper must distinguish \"same model, different prompt\" from \"same model, same prompt, different accuracy.\"\n\n## Working Title\n**\"Beyond Self-Consistency: How Trace Independence Limits Symbolic Consensus in LLM Reasoning\"**\n(Alternatives:\n- \"The Independence Bottleneck: Why Self-Extracted Symbolic Constraints Cannot Beat Majority Voting\"\n- \"Symbolic Consensus Under the Condorcet Lens: Independence, Extraction, and the Limits of Self-Aggregation\")\n\nNOTE (Dream D037): Title MUST be scoped to \"self-extracted constraints\" / \"SICA\". Published methods (DyLoS, Aristotle, FoVer) use different approaches.\n\n## Paper Structure (EMNLP 8pp + appendix)\n\n### Main Tables\n- T1: Main Results — models × domains, SC% / SICA% / Δpp / p-value, regime boundary\n- T2: Oracle Control — Gold-FOL+MAX-SAT vs SC vs SICA-self, causal separation\n- T3: Independence Quantification — Fleiss' κ / Eff-K / trace agreement per model\n- T4: Extraction Error Taxonomy — trivially_satisfied / discriminative / both_wrong rates\n- T5: K Sensitivity — K=4/8/12/16/20, non-monotonic (peak K=12, K=20 recovers), SC confound\n\n### Main Tables (continued)\n- T6: Method-Level Intervention Results — 3 methods × 2 datasets, SC% / Method% / Δpp, failure mode classification\n- T7: κ Generalization — SC / Debate / Diverse-Prompt κ and Eff-K (from exp-077, pending)\n\n### Main Figures\n- F1: Method Pipeline (SICA + oracle control design)\n- F2: SC Accuracy vs SICA Δ scatter (hero figure, regime boundary)\n- F3: K Sensitivity with diversity metrics (K vs Δ, K vs Eff-K)\n- F4: Extraction error breakdown (stacked bar)\n- F5: Method intervention failure modes (grouped bar: ICG/Contrastive/Debate × FOLIO/LogiQA)\n\n### Appendix\n- K ablation details, temperature sensitivity, per-domain results, overhead analysis\n- Entropy-conditioned analysis (continuous scatter + bin sensitivity)\n- Six remediation strategy details\n- Confirmation bias quantification\n- Seed replication analysis\n- QwQ-32B / DeepSeek-R1 negative control\n\n## Claim Risk Notes (D059)\n- **Seed replication**: 0/3 significant after D066 correction (p=0.092, 0.070, 1.0). 2/3 positive trend, 1/3 null. Mean +2.12pp. Frame as \"directional trend, not significant effect\" — fragility IS the finding.\n- **Method claims DEAD (D060)**: All three method improvements failed. Paper is pure analysis. 9 remediation failures are EVIDENCE, not limitation.\n- **Condorcet novelty**: ✅ VERIFIED. arXiv:2409.00094 applies CJT to cross-model LLM ensembles (different angle). No prior work applies Fleiss' κ or Eff-K to within-model SC traces. Our framing is novel.\n- **exp-050b complication**: ICL transition Δ=-3.52pp at SC=57.79% complicates simple \"SC determines SICA.\" Explain via trace generation characteristic change.\n- **Variable naming inconsistency**: 56.4% cross-trace pairs share zero Z3 variables. Key mechanism evidence.\n\n## Required Citations (minimum 30 references)\n\n- **SC & extensions**: Wang et al. 2023 (SC), Chen et al. 2023 (USC), Loo et al. 2025 (SC scaling plateaus), Taubenfeld et al. 2025 (weighted SC), DiVeRSe (Li et al. 2023)\n- **Neuro-symbolic reasoning**: DyLoS (EACL 2026), Aristotle (ACL 2025), FoVer (TACL 2025), LogicAgent (2025), Logic-LM (Pan et al. 2023), LINC (Olausson et al. 2023)\n- **Condorcet/voting theory**: Condorcet 1785, Austen-Smith & Banks 1996, **arXiv:2409.00094 (Examining Independence in Ensemble Sentiment Analysis, Sept 2024)** — closest prior work, applies CJT to cross-model LLM ensembles, finds independence violation. Our novelty: within-model trace independence + Fleiss' κ quantification + Eff-K + connection to symbolic aggregation\n- **Test-time compute**: Snell et al. 2025, DeepSeek-R1, Diversity-Aware Training\n- **Verification & reranking**: ORM (Cobbe et al. 2021), PRM (Lightman et al. 2023), Math-Shepherd\n- **Constraint satisfaction**: SATBench (EMNLP 2025), LLM Meets Constraint Propagation (IJCAI 2025)\n- **Debate & multi-agent**: Liang et al. 2023, Du et al. 2023\n\n## Additional Reviewer Concerns (D070/D074 Methods)\n\n17. **\"Why not use a larger model for constraint generation?\"** → Valid. All methods tested at 7B scale. ICG constraint parsing failures + Debate role-play degradation may be scale-dependent. This is explicitly noted as limitation and future work. The contribution is diagnosing the bottleneck and showing it's not trivially fixable, not claiming no fix exists at any scale.\n18. **\"Only tested one model (Mistral-7B) for methods\"** → Methods are interventions on the extraction pipeline, not the base model. Testing on the same model that showed the clearest Goldilocks signal (Mistral-7B FOLIO) is the strongest test — if methods can't improve the best-case scenario, they won't help elsewhere.\n19. **\"ICG multi-seed shows 1/3 positive\"** → Magnitudes (-2.0, +1.5, -1.0) are within SC baseline noise (3.5pp cross-seed). Mean ≈-0.5pp, std=1.8pp. No statistical significance. Properly framed as \"noise-level, neither improving nor degrading.\"\n20. **\"Debate working in other papers\"** → Multi-agent debate literature uses diverse models or much larger models. Same-model 7B debate is a different regime. Our finding is specifically about same-model self-extraction limitations.\n\n## Claim Scoping Rules\n- n=60 conditions: \"suggestive/consistent with\" NOT \"confirming\"\n- n≥200 conditions: can \"confirm\"\n- Combined N>1,300: acceptable if breakdown clearly stated\n- Method claims: must show statistically significant improvement OR clear directional improvement with analysis\n- \"Independence bottleneck\" framing: systematic quantification + theoretical grounding\n",
      "numLines": 345,
      "startLine": 1,
      "totalLines": 345
    }
  },
  "sourceToolAssistantUUID": "a080a9f5-97fe-4315-ba24-f9ed98932995",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora"
}
```

</details>

---


### Runtime record

_source line 8870_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[服务器重启后首条消息] 当前日期: 2026-05-20。服务器刚重启，项目状态可能已更新。不要依赖对话历史中的状态信息，以 registry 当前值为准。  **用户消息：** [Director 指令] ## 写作任务：EMNLP 2026 ARR May 25 — Full Draft 更新  **DDL**: May 25, 2026（5 天） **模式**: Full Draft 更新…",
  "leafUuid": "d30f6760-b1d7-40e2-b49a-c9356dbd59eb",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1"
}
```

---


### Runtime record

_source line 8871_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise paper results with oracle FOLIO constraint experiments",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1"
}
```

---


### Assistant

_source line 8872 · 2026-05-20T09:39:08.094Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a comprehensive picture. Let me also read the current writing_plan.yaml to understand what needs to change.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d30f6760-b1d7-40e2-b49a-c9356dbd59eb",
  "isSidechain": false,
  "requestId": "req_011CbDbeeaivC2VwLgRKhXRW",
  "type": "assistant",
  "uuid": "e71e45f1-40f3-4c7d-9b0f-c9d675ba0678",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TLkTBYkyiiyxGVh6y6ytgE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14166,
      "cache_read_input_tokens": 53948,
      "output_tokens": 146,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14166,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 146,
          "cache_read_input_tokens": 53948,
          "cache_creation_input_tokens": 14166,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14166
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

_source line 8873 · 2026-05-20T09:39:08.591Z_

Now let me read the current writing_plan.yaml and the registry for new experiments.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e71e45f1-40f3-4c7d-9b0f-c9d675ba0678",
  "isSidechain": false,
  "requestId": "req_011CbDbeeaivC2VwLgRKhXRW",
  "type": "assistant",
  "uuid": "844db542-6881-42de-862c-a29ef02813af",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TLkTBYkyiiyxGVh6y6ytgE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14166,
      "cache_read_input_tokens": 53948,
      "output_tokens": 146,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14166,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 146,
          "cache_read_input_tokens": 53948,
          "cache_creation_input_tokens": 14166,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14166
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

_source line 8874 · 2026-05-20T09:39:10.151Z_

<details open><summary>🔧 Tool call — Read · `toolu_01BaS8ipd3DDQT8dpa3bTAEJ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/writing_plan.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "844db542-6881-42de-862c-a29ef02813af",
  "isSidechain": false,
  "requestId": "req_011CbDbeeaivC2VwLgRKhXRW",
  "type": "assistant",
  "uuid": "5f8e59a7-5571-4c3d-8eee-6d9e8d454b63",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TLkTBYkyiiyxGVh6y6ytgE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14166,
      "cache_read_input_tokens": 53948,
      "output_tokens": 146,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14166,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 146,
          "cache_read_input_tokens": 53948,
          "cache_creation_input_tokens": 14166,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14166
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

_source line 8875 · 2026-05-20T09:39:10.458Z_

<details><summary>↩ Tool result · `toolu_01BaS8ipd3DDQT8dpa3bTAEJ`</summary>

```text
1	# Writing Plan — symb_invariant_consensus
2	# Generated: 2026-05-19T20:30:00Z
3	# Full Draft: Independence Bottleneck — "Fundamental Limitation" paper
4	# Target: EMNLP 2026 ARR May cycle
5	# Paper Agent Step 1 output
6	
7	meta:
8	  venue: EMNLP 2026
9	  track: main (ARR May cycle)
10	  template: docs/paper/acl.sty
11	  template_note: "ACL/EMNLP shared template already in paper directory"
12	  page_limit: 8
13	  deadline: 2026-05-25
14	  title: >
15	    Beyond Self-Consistency: How Trace Independence Limits
16	    Symbolic Consensus in LLM Reasoning
17	  core_claim: >
18	    Same-model self-extraction of symbolic constraints inherits trace
19	    correlation (Fleiss' κ=0.21–0.82, Eff-K=1.20–3.62 for nominal K=12),
20	    creating a structural independence bottleneck. Oracle gold-FOL yields
21	    +14.22pp (p<0.001) proving aggregation is sound, but self-extraction
22	    captures only 24%. κ generalization across aggregation methods reveals
23	    a fundamental independence-accuracy trade-off: Debate reduces κ from
24	    0.44→0.15 (Eff-K 2→4.4) but collapses accuracy by -18.6pp. Same-model
25	    methods cannot increase independence without degrading the signal that
26	    makes aggregation useful.
27	  paper_type: "Fundamental limitation analysis (Condorcet framework + empirical diagnosis + 12 remediation failures)"
28	  framing: "Independence Bottleneck — structural limitation of same-model self-extraction"
29	  created_at: 2026-05-19T20:30:00Z
30	
31	# ──────────────────────────────────────────────
32	# Contributions (5)
33	# ──────────────────────────────────────────────
34	contributions:
35	  - id: C1
36	    label: "Independence Bottleneck Quantification"
37	    status: VERIFIED
38	    claim: >
39	      Fleiss' κ=0.21–0.82 (instruction-tuned), 0.91 (thinking mode).
40	      Eff-K=1.20–3.62 at K=12. Mistral 4-seed κ=0.41–0.51 (stable).
41	      Qwen Eff-K≈1.2–1.5 → near-zero Δ; Mistral PW Eff-K=3.62 but
42	      SC=39% → negative Δ. Dual requirement: sufficient Eff-K AND SC.
43	    evidence: "Table 3, §5.1"
44	
45	  - id: C2
46	    label: "Oracle Gap Localizes Extraction Bottleneck"
47	    status: VERIFIED
48	    claim: >
49	      Gold FOL: +14.22pp FOLIO (p<0.001), +11.50pp PW (p<0.001).
50	      Self-extraction captures 24% of oracle ceiling (best seed +3.43pp
51	      vs +14.22pp). Aggregation mechanism sound; extraction quality is
52	      the binding bottleneck.
53	    evidence: "Table 1 oracle rows, §4.3"
54	
55	  - id: C3
56	    label: "Regime-Dependent Effect with 4-Seed Replication"
57	    status: VERIFIED
58	    claim: >
59	      Intermediate-SC (~50–55%): best seed +3.43pp (p=0.092, ns);
60	      4-seed mean +1.47pp; 2/4 marginal (p<0.10), 0/4 significant.
61	      Type A (SC≥60%): 9 conditions N>2,800, no significant positive;
62	      significant negatives at -2.50pp (p=0.011) and -4.41pp (p=0.093).
63	      Type C (SC≤40%): -2.83pp (p=0.014).
64	    evidence: "Table 1, Figure 2, §4.1–4.3"
65	
66	  - id: C4
67	    label: "Independence-Accuracy Trade-off Is Fundamental"
68	    status: VERIFIED
69	    claim: >
70	      κ generalization (exp-077) reveals why same-model methods must fail:
71	      SC κ=0.44 (Eff-K=2.02); Diverse-Prompt κ=0.40 (Eff-K=2.21, ≈SC);
72	      Debate κ=0.15 (Eff-K=4.44) but Δ=-18.6pp. Methods that increase
73	      independence (Debate) destroy accuracy; methods that preserve accuracy
74	      (ICG, Diverse-Prompt) cannot break correlation. 12 remediations
75	      (9 prompt + 3 method) all fail — not engineering failure but
76	      fundamental trade-off in same-model aggregation.
77	    evidence: "§5.6, Table T7 (κ generalization), method intervention table"
78	
79	  - id: C5
80	    label: "Entropy Decomposition Reveals Regime Mechanism"
81	    status: VERIFIED
82	    claim: >
83	      Low-entropy: SICA≈SC across all 8 conditions (Δ≈0). High-entropy
84	      direction regime-dependent: +12.8pp intermediate-SC, -8.2pp Type A.
85	      Explains dual-channel mechanism (voting diversity + constraint
86	      homogenization).
87	    evidence: "§5.5, entropy analysis"
88	
89	# ──────────────────────────────────────────────
90	# Paper Outline
91	# ──────────────────────────────────────────────
92	paper_outline:
93	  - section: abstract
94	    file: abstract.tex
95	    word_budget: 220
96	    core_bullets:
97	      - "Problem: SC (majority voting) plateaus; CJT explains why — traces lack independence"
98	      - "SICA pipeline evaluated across 6 models, 3 formal reasoning domains, N>3,000, 4-seed replication"
99	      - "Independence quantification: κ=0.21–0.82, Eff-K=1.20–3.62 at K=12"
100	      - "Regime: +3.43pp intermediate-SC (ns), -2.83pp Type C (p=0.014), ~0 Type A"
101	      - "Oracle +14.22pp/+11.50pp proves aggregation sound; self-extraction 24%"
102	      - "12 remediations (9 prompt + 3 method) all fail — bottleneck is structural"
103	      - "C0+SC zero-cost deployment diagnostic; paths forward require independence"
104	    dependencies: [experiments, analysis, method]
105	
106	  - section: introduction
107	    file: introduction.tex
108	    word_budget: 1300
109	    core_bullets:
110	      - "Hook: Test-time compute scaling via SC improves reasoning—but plateaus. Adding more traces yields diminishing returns."
111	      - "Gap: Neuro-symbolic methods (Logic-LM, DyLoS, FoVer) improve reasoning with external/trained components. Can same-model self-extraction of formal constraints break the SC plateau without external tools?"
112	      - "Insight: CJT requires voter independence. Same-model traces violate this (Eff-K=1.20–3.62 for K=12). Self-extracted constraints inherit the correlation structure."
113	      - "Evaluation: SICA pipeline + Condorcet analysis + oracle control across 6 models × 3 domains, 4-seed replication"
114	      - "Key result: Oracle +14.22pp proves mechanism works; self-extraction captures 24%. 12 remediations all fail."
115	      - "Contributions: C1–C5"
116	    dependencies: [experiments, analysis]
117	    figures: [fig1_pipeline]
118	    citation_hints:
119	      - "SC: Wang et al. 2023"
120	      - "SC plateau: Loo et al. 2025"
121	      - "Logic-LM: Pan et al. 2023"
122	      - "DyLoS: Xu et al. 2026"
123	      - "CJT: Condorcet 1785, Ladha 1992"
124	      - "Self-correction parallel: Huang et al. 2024"
125	
126	  - section: related_work
127	    file: related_work.tex
128	    word_budget: 750
129	    core_bullets:
130	      - "SC and extensions: Wang 2023, USC, weighted SC (Taubenfeld 2025), DiVeRSe, scaling plateaus (Loo 2025)"
131	      - "Neuro-symbolic reasoning: Logic-LM, LINC, DyLoS, Aristotle, FoVer — all use external/trained components; we test same-model self-extraction"
132	      - "Condorcet/voting theory: CJT, correlated voters (Ladha 1992), LLM ensembles (Lefort 2024 arXiv:2409.00094, closest prior work)"
133	      - "Verification and reranking: ORM (Cobbe 2021), PRM (Lightman 2023), Math-Shepherd — trained verifier paradigm"
134	      - "Self-X limitations: Huang 2024 self-correction ≈ structural parallel to self-extraction"
135	      - "Debate/multi-agent: Liang 2023, Du 2023 — different regime (multi-model or larger models)"
136	    dependencies: []
137	
138	  - section: method
139	    file: method.tex
140	    word_budget: 1100
141	    subsections:
142	      - id: "sec:condorcet"
143	        title: "Self-Consistency and the Condorcet Independence Assumption"
144	        word_budget: 300
145	        bullets:
146	          - "SC as majority voting: sample K reasoning traces, select most common answer"
147	          - "CJT: K independent voters each with p>0.5 → P(majority correct) → 1 as K→∞"
148	          - "LLM traces violate independence: same model, same prompt, only sampling noise"
149	          - "Eff-K = K/(1+(K-1)κ) via Kish (1965) design effect; κ = Fleiss' kappa (1971)"
150	          - "When Eff-K≈1, additional traces ≈ no new information → SC plateau"
151	      - id: "sec:sica-pipeline"
152	        title: "SICA Pipeline"
153	        word_budget: 400
154	        bullets:
155	          - "Step 1: Generate K reasoning traces at temperature T"
156	          - "Step 2: Extract FOL constraints from each trace at T_ext=0.3"
157	          - "Step 3: Syntactic deduplication across traces"
158	          - "Step 4: Weighted partial MAX-SAT — hard clauses (answer assertion), soft clauses (constraints weighted by occurrence count)"
159	          - "Step 5: Z3 solver evaluates each candidate; answer with highest satisfiable weight selected"
160	          - "Timeout: 10s per candidate answer"
161	      - id: "sec:oracle-design"
162	        title: "Oracle Control Design"
163	        word_budget: 200
164	        bullets:
165	          - "Replace self-extracted constraints with gold FOL annotations (FOLIO) or gold DSL (ProofWriter)"
166	          - "Same Z3 evaluation pipeline; only constraint source changes"
167	          - "Causal intervention: isolates constraint quality from aggregation mechanism"
168	      - id: "sec:method-interventions"
169	        title: "Method-Level Interventions"
170	        word_budget: 150
171	        bullets:
172	          - "ICG: Generate constraints independently of traces (bypass trace-constraint coupling)"
173	          - "Contrastive: Pro/con constraint scoring per candidate answer"
174	          - "Debate: Proposer/Critic/Defense chain before constraint extraction"
175	          - "Each targets a different bottleneck aspect"
176	    dependencies: []
177	    figures: [fig1_pipeline]
178	
179	  - section: experiments
180	    file: experiments.tex
181	    word_budget: 1800
182	    subsections:
183	      - id: "sec:exp-setup"
184	        title: "Experimental Setup"
185	        word_budget: 300
186	        bullets:
187	          - "6 models: Mistral-7B-Instruct-v0.3, LLaMA-3.1-8B-Instruct, Qwen2.5-7B-Instruct, Qwen2.5-14B-Instruct, Qwen3-14B (non-thinking), Qwen3-14B (thinking mode for κ analysis)"
188	          - "3 formal reasoning domains: FOLIO (n=204), ProofWriter depth-5 (n=600), LogiQA (n=200)"
189	          - "Cross-domain diagnostic: StrategyQA (n=200)"
190	          - "Degenerate probes: QwQ-32B (AIME 2024), Qwen2.5-14B (GSM8K)"
191	          - "Default: K=12, T=0.7, T_ext=0.3, Z3 timeout 10s"
192	          - "Metrics: accuracy (%), Δ=SICA−SC (pp), McNemar exact test α=0.05"
193	          - "4-seed replication on primary condition (Mistral-7B FOLIO)"
194	      - id: "sec:main-results"
195	        title: "Main Results: A Regime-Dependent Effect"
196	        word_budget: 500
197	        bullets:
198	          - "Table 1: ~18 conditions grouped by regime + 2 oracle rows"
199	          - "Intermediate-SC (SC~50–55%): Mistral FOLIO best seed +3.43pp (p=0.092 ns); 4-seed mean +1.47pp; Mistral LogiQA +0.50pp"
200	          - "Type A (SC≥60%): 9 conditions N>2,800; no significant positive effect"
201	          - "  Significant negatives: Qwen14B PW -2.50pp (p=0.011); Mistral PW -2.83pp (p=0.014)"
202	          - "  LLaMA FOLIO -4.41pp (p=0.093, marginal)"
203	          - "  Qwen3-14B FOLIO -0.49pp, PW +0.67pp — generational scaling does not help"
204	          - "Type C (SC≤40%): Mistral PW-D5 Δ=-2.83pp p=0.014 — SICA significantly hurts"
205	          - "Degenerate: C0<5% → SICA≡SC by construction"
206	          - "Figure 2: SC vs Δ scatter showing regime boundaries"
207	      - id: "sec:oracle"
208	        title: "Oracle Control: Aggregation Is Sound"
209	        word_budget: 250
210	        bullets:
211	          - "FOLIO: oracle-SICA 89.71% vs SC 75.49% (+14.22pp, p<0.001)"
212	          - "ProofWriter: oracle-SICA 86.67% vs SC 75.17% (+11.50pp, p<0.001)"
213	          - "Self-extraction captures only 24.1% of FOLIO oracle ceiling"
214	          - "Aggregation mechanism is sound; extraction quality is binding constraint"
215	      - id: "sec:replication"
216	        title: "Four-Seed Replication"
217	        word_budget: 250
218	        bullets:
219	          - "Mistral-7B FOLIO-204: seeds 42, 123, 456, 789"
220	          - "s42: Δ=+3.43pp p=0.092; s123: +2.94pp p=0.070; s456: 0.00pp p=1.0; s789: -0.49pp p=1.0"
221	          - "2/4 marginal positive (p<0.10); 0/4 reaches p<0.05"
222	          - "4-seed mean: +1.47pp; range: +3.43 to -0.49"
223	          - "Fragility itself is the finding — motivates independence analysis"
224	      - id: "sec:failure-modes"
225	        title: "Failure Mode Analysis"
226	        word_budget: 250
227	        bullets:
228	          - "Type A: consistent traces → constraints mirror model's answers → MAX-SAT degenerates to counting"
229	          - "Type B: domain not formalizable (LogiQA contradiction rate 0.8%)"
230	          - "Type C: predominantly wrong traces → wrong constraints → solver amplifies errors"
231	    dependencies: []
232	    tables: [tab1_main_results]
233	    figures: [fig2_regime_scatter]
234	    registry_refs:
235	      - exp-033  # Mistral FOLIO s42 (hero)
236	      - exp-052  # Mistral FOLIO s123
237	      - exp-053  # Mistral FOLIO s456
238	      - exp-067  # Mistral FOLIO s789
239	      - exp-046  # Mistral PW-600 (Type C)
240	      - exp-049b # Mistral LogiQA
241	      - exp-063  # LLaMA FOLIO
242	      - exp-019  # LLaMA StrategyQA
243	      - exp-061  # Qwen2.5-7B FOLIO
244	      - exp-026  # Qwen2.5-14B FOLIO (regen)
245	      - exp-038  # Qwen2.5-14B LogiQA
246	      - exp-039  # Qwen2.5-14B PW-600
247	      - exp-044b # Qwen2.5-14B FOLIO ICL
248	      - exp-027  # Qwen3-14B FOLIO
249	      - exp-040  # Qwen3-14B PW-600
250	      - exp-031  # Oracle FOLIO
251	      - exp-022  # Oracle PW
252	
253	  - section: analysis
254	    file: analysis.tex
255	    word_budget: 1500
256	    subsections:
257	      - id: "sec:effective-k"
258	        title: "Condorcet Independence Analysis"
259	        word_budget: 350
260	        bullets:
261	          - "Table 3: Fleiss' κ and Eff-K per model-domain condition"
262	          - "Mistral FOLIO 4 seeds: κ=0.41–0.51, Eff-K=1.8–2.2 (cross-seed stable)"
263	          - "Qwen family: κ=0.66–0.82, Eff-K=1.2–1.5 → all near-zero Δ"
264	          - "Mistral PW: κ=0.21, Eff-K=3.62 but SC=39% → negative (highest independence, insufficient quality)"
265	          - "Qwen3-14B thinking: κ=0.91, Eff-K=1.09 → 'better reasoning' worsens independence"
266	          - "Dual requirement: need both sufficient Eff-K AND sufficient SC"
267	          - "Explains SC plateau: traces beyond Eff-K provide no new information"
268	      - id: "sec:extraction-taxonomy"
269	        title: "Constraint Quality Analysis"
270	        word_budget: 200
271	        bullets:
272	          - "Discriminative rate: ~8.2% (95% CI [7.6, 8.8])"
273	          - "Removing non-discriminative constraints: 0 gain → problem is direction not quality"
274	          - "Variable naming: 56.4% cross-trace constraint pairs share zero Z3 variables"
275	          - "~92% constraints ARE discriminative but discriminate in same direction as model bias"
276	      - id: "sec:entropy"
277	        title: "Entropy Decomposition"
278	        word_budget: 200
279	        bullets:
280	          - "Per-problem answer entropy separates SICA operating point"
281	          - "Low-entropy: SICA≈SC across all 8 conditions (Δ≈0) — traces agree, constraints add nothing"
282	          - "High-entropy: regime-dependent — +12.8pp intermediate-SC (s42), -8.2pp Type A (Qwen14B)"
283	          - "High-entropy proportion: Mistral 38% vs Qwen 18% → explains model-level Δ differences"
284	          - "Mechanism: low-entropy = direct CJT channel; high-entropy = indirect constraint channel"
285	      - id: "sec:ablation"
286	        title: "MAX-SAT Ablation"
287	        word_budget: 100
288	        bullets:
289	          - "MAX-SAT vs count-only: 803/804 agreement (Qwen14B, n=804)"
290	          - "Self-extracted constraints carry no signal beyond vote counts in high-SC regime"
291	          - "Confirms independence bottleneck causes MAX-SAT to degenerate"
292	      - id: "sec:k-t-sensitivity"
293	        title: "K and Temperature Sensitivity"
294	        word_budget: 200
295	        bullets:
296	          - "K sensitivity: K=4(-1.47), K=8(-1.96), K=12(+3.43), K=16(+1.47), K=20(+1.96)"
297	          - "K=12 is only setting with Δ>2pp; not clean inverted-U"
298	          - "T sensitivity: T=0.3(-1.47), T=0.5(-0.98), T=0.7(+3.43), T=1.0(0.00)"
299	          - "T=0.7 is isolated spike; only 1/4 temperatures positive"
300	          - "Both K=12 and T=0.7 coincide with lowest SC baseline → confound with operating window"
301	          - "Figure 3: two-panel K/T sensitivity plot"
302	      - id: "sec:remediation"
303	        title: "Remediation Analysis"
304	        word_budget: 350
305	        bullets:
306	          - "--- Prompt-level (9 strategies, 6 dimensions) ---"
307	          - "Prompting: contrastive extraction (disc_rate 8.2%→6.0%, Δ still mirrors bias)"
308	          - "Architecture: cross-model bilateral (weak→strong: 0% disc; strong→weak: ±1pp of self)"
309	          - "Capability: generational scaling Qwen3-14B (+0.49pp ns)"
310	          - "Verification: Z3 feedback (0.9% UNSAT), cross-trace UNSAT (56.4% zero shared vars)"
311	          - "Diversity: multi-temp (Δ=0.00pp), T=1.0 (Δ=0.00pp — collapse from +3.43)"
312	          - "Filtering: discriminative constraint filtering (0 gain), consistency filtering (reverts to SC)"
313	          - "ICL with gold FOL examples (+0.50pp ns)"
314	          - "--- Method-level (3 methods × 2 datasets) ---"
315	          - "ICG (Independent Constraint Gen.): FOLIO Δ=-2.0/+1.5pp (noise), LogiQA -0.5pp → neutral"
316	          - "  Insight: independent constraints ≈ trace-sourced → bias from problem understanding stage"
317	          - "Contrastive (Pro/Con Scoring): FOLIO -9.3pp, LogiQA pending → harmful"
318	          - "  Insight: 26% degenerate scoring, pro/con imbalance (94 pro vs 65 con)"
319	          - "Debate (Proposer/Critic): FOLIO -18.6pp, LogiQA pending → catastrophic"
320	          - "  Insight: 7B role-play degradation; same-model debate = same bias + cognitive overhead"
321	          - "Scale caveat: all method-level tested at 7B; 14B+ may differ"
322	          - "--- κ Generalization: Independence-Accuracy Trade-off (exp-077, CAPSTONE) ---"
323	          - "Table T7: SC κ=0.44 Eff-K=2.02 | Diverse-Prompt κ=0.40 Eff-K=2.21 | Debate κ=0.15 Eff-K=4.44"
324	          - "Diverse-Prompt ≈ SC κ → changing prompts cannot break correlation"
325	          - "Debate breaks κ (0.44→0.15) but accuracy collapses (-18.6pp)"
326	          - "FUNDAMENTAL TRADE-OFF: methods that increase independence destroy accuracy; methods that preserve accuracy cannot break correlation"
327	          - "This explains WHY same-model methods must fail — not just that they do"
328	          - "Implication: breaking bottleneck requires cross-model or external signal (consistent with oracle)"
329	    dependencies: [experiments]
330	    tables: [tab3_independence, tab_method_interventions, tab_kappa_generalization]
331	    figures: [fig3_sensitivity]
332	    registry_refs:
333	      - exp-029  # contrastive prompting
334	      - exp-030  # cross-model extraction
335	      - exp-059  # cross-model Qwen3→Mistral
336	      - exp-060  # cross-model Qwen14B→Mistral
337	      - exp-027  # Qwen3-14B (generational)
338	      - exp-036  # Z3 feedback
339	      - exp-036b # cross-trace UNSAT
340	      - exp-043  # consistency filtering
341	      - exp-055  # multi-temp
342	      - exp-054  # T=1.0
343	      - exp-057  # T=0.3
344	      - exp-058  # T=0.5
345	      - exp-044b # ICL gold FOL
346	      - exp-074  # ICG FOLIO s42
347	      - exp-074c # ICG FOLIO s123
348	      - exp-075b # Contrastive FOLIO
349	      - exp-076  # Debate FOLIO
350	      - exp-079  # ICG LogiQA
351	      - exp-080  # Contrastive LogiQA
352	      - exp-078  # Debate LogiQA (RUNNING)
353	      - exp-077  # κ generalization (CAPSTONE)
354	
355	  - section: discussion
356	    file: discussion.tex
357	    word_budget: 450
358	    core_bullets:
359	      - "Oracle causally isolates: aggregation mechanism sound, extraction is binding bottleneck"
360	      - "Dual-channel mechanism: direct (voting diversity → SC plateau) + indirect (constraint homogenization → MAX-SAT degeneration)"
361	      - "Oracle disambiguates: gold constraints on same correlated traces yield +14.22pp → indirect channel is proximal bottleneck"
362	      - "Independence-accuracy trade-off (exp-077): Debate breaks κ (0.44→0.15) but collapses accuracy (-18.6pp). Diverse-Prompt ≈ SC κ. Same-model methods face a fundamental Pareto frontier."
363	      - "This trade-off explains WHY same-model methods must fail, not just that they do. Breaking correlation within a single model's distribution necessarily degrades the signal."
364	      - "Published methods (DyLoS, Aristotle, FoVer, Logic-LM) bypass same-model extraction — consistent with trade-off: cross-model/external sources are naturally independent without sacrificing quality"
365	      - "Statistical evidence: 0/4 seeds significant positive; only significant effects are negative"
366	      - "C0+SC deployment diagnostic: C0<5%→degenerate, high SC→confirmation bias, low SC→error amplification"
367	      - "Three paths forward trade simplicity for independence: trained extractors, external provers, multi-model pipelines — all introduce signal outside the model's own distribution"
368	    dependencies: [experiments, analysis]
369	
370	  - section: conclusion
371	    file: conclusion.tex
372	    word_budget: 300
373	    core_bullets:
374	      - "SICA evaluated: 6 models spanning 3 families, 3 reasoning domains, N>3,000, 4-seed replication"
375	      - "Independence bottleneck: κ=0.21–0.82, Eff-K=1.20–3.62 → explains SC plateau and SICA failure"
376	      - "Intermediate-SC region: +3.43pp best seed (ns), 4-seed mean +1.47pp (2/4 positive, 2/4 null/negative)"
377	      - "Oracle +14.22pp/+11.50pp (p<0.001); 12 remediations all fail; independence-accuracy trade-off explains why"
378	      - "Limitations: trained extractors untested, narrow intermediate-SC zone, 7B-scale method testing, formal reasoning domains only"
379	    dependencies: [experiments, analysis]
380	
381	# ──────────────────────────────────────────────
382	# Visualization Plan
383	# ──────────────────────────────────────────────
384	visualization_plan:
385	  - fig_id: fig1_pipeline
386	    type: conceptual
387	    tool: matplotlib
388	    description: >
389	      SICA pipeline diagram: K traces → FOL constraint extraction →
390	      dedup → weighted partial MAX-SAT (Z3) → answer selection.
391	      Oracle branch replaces self-extracted constraints with gold FOL.
392	      Independence bottleneck annotation at extraction stage.
393	    narrative_intent: >
394	      The pipeline looks like it should introduce independent symbolic
395	      signal, but self-extraction inherits the same trace correlation —
396	      the independence bottleneck manifests at the extraction stage.
397	    design_notes:
398	      - "Existing figure in paper; update to annotate independence bottleneck clearly"
399	      - "Add oracle branch as parallel path with green highlight"
400	      - "Add method-level intervention points (ICG/Contrastive/Debate) as annotation"
401	    placement: method
402	    aspect_ratio: "16:6"
403	    data_source: "manual (diagram)"
404	    status: "EXISTS — label update needed"
405	
406	  - fig_id: fig2_regime_scatter
407	    type: statistical
408	    tool: matplotlib
409	    description: >
410	      SC accuracy (x-axis) vs SICA Δpp (y-axis) scatter plot.
411	      All model-domain conditions from Table 1. 4 replication seeds
412	      as separate points. Color/marker by model family.
413	      Shaded intermediate-SC band (50–55%). Regime zone labels.
414	    narrative_intent: >
415	      The intermediate-SC region is narrow and model-specific. Outside it,
416	      SICA is either neutral (Type A) or harmful (Type C). No condition
417	      shows statistically significant improvement.
418	    design_notes:
419	      - "Pattern A: regime bands — light shading 50-55% SC, labeled zones"
420	      - "Solid markers: n≥100; hollow: n<50"
421	      - "Horizontal Δ=0 reference line (dashed)"
422	      - "4 Mistral FOLIO seeds clustered at SC≈54-56%"
423	      - "Star or bold outline for significant effects (p<0.05)"
424	      - "Annotate LLaMA -4.41pp as 'upper boundary' of intermediate-SC"
425	    placement: experiments
426	    aspect_ratio: "4:3"
427	    data_source: "registry: all Table 1 conditions (~18 points + oracle excluded)"
428	    status: "EXISTS — needs regeneration with 4-seed + new experiments"
429	
430	  - fig_id: fig3_sensitivity
431	    type: statistical
432	    tool: matplotlib
433	    description: >
434	      Two-panel figure. (a) K sensitivity: K=4,8,12,16,20 vs Δpp.
435	      (b) T sensitivity: T=0.3,0.5,0.7,1.0 vs Δpp. Both annotated
436	      with SC baseline at each point.
437	    narrative_intent: >
438	      SICA's optimal hyperparameters are fragile: K=12 is the only
439	      setting with Δ>2pp, T=0.7 is an isolated spike. Both peaks
440	      coincide with the lowest SC baseline, suggesting the effect
441	      reflects operating window rather than causal K/T contribution.
442	    design_notes:
443	      - "Panel (a): line plot K vs Δ, secondary y-axis or annotation for SC"
444	      - "Panel (b): line plot T vs Δ, annotate SC at each T"
445	      - "Dashed Δ=0 reference line in both panels"
446	      - "Highlight K=12 and T=0.7 as peaks; annotate SC values"
447	      - "Pattern: minimal, 2-panel with shared y-axis scale if possible"
448	    placement: analysis
449	    aspect_ratio: "2:1"
450	    data_source: >
451	      K sensitivity: exp-051 data (K=4,8,12,16,20).
452	      T sensitivity: exp-033 (T=0.7), exp-054 (T=1.0), exp-057 (T=0.3), exp-058 (T=0.5).
453	    status: "EXISTS — needs regeneration with corrected data + T panel"
454	
455	# ──────────────────────────────────────────────
456	# Table Plan
457	# ──────────────────────────────────────────────
458	table_plan:
459	  # Main text tables
460	  - table_id: tab1_main_results
461	    type: comparison
462	    placement: experiments
463	    width: "table*"
464	    caption: >
465	      SICA vs SC across all model-domain conditions (K=12, T=0.7).
466	      Grouped by SC accuracy regime. Bold: significant effects (p<0.05).
467	      Bottom: oracle controls with gold FOL annotations.
468	    columns: [Model, Domain, n, "SC (%)", "SICA (%)", "Δ (pp)", "p"]
469	    data_source: "registry: see experiments.registry_refs"
470	    notes: >
471	      ~18 data rows grouped as: Type C / Intermediate-SC (4 seeds) /
472	      Type A (9 conditions) / Degenerate / Oracle. Footnotes for
473	      StrategyQA diagnostic and ICL condition.
474	
475	  - table_id: tab3_independence
476	    type: statistics
477	    placement: analysis
478	    width: "table"
479	    caption: >
480	      Condorcet independence metrics per model-domain condition.
481	      κ = Fleiss' kappa (K=12 traces), Eff-K = K/(1+(K-1)κ).
482	    columns: [Model (seed), Domain, "κ", "Eff-K", "SC (%)", "SICA Δ (pp)"]
483	    data_source: "comp-1 verified κ values + registry"
484	    notes: >
485	      ~14 rows including 4 Mistral FOLIO seeds, Mistral PW/LogiQA,
486	      Qwen family, Qwen3 thinking mode.
487	
488	  - table_id: tab_method_interventions
489	    type: comparison
490	    placement: analysis
491	    width: "table"
492	    caption: >
493	      Method-level interventions targeting the independence bottleneck
494	      (Mistral-7B). Each targets a different aspect: ICG bypasses
495	      trace-constraint coupling, Contrastive adds adversarial scoring,
496	      Debate adds multi-role reasoning.
497	    columns: [Method, Target Aspect, "FOLIO Δ (pp)", "LogiQA Δ (pp)", Failure Mode]
498	    data_source: "registry: exp-074, exp-074c, exp-075b, exp-076, exp-079, exp-080, exp-078"
499	    notes: >
500	      3 methods × 2 datasets. ICG has multi-seed on FOLIO.
501	      Debate LogiQA (exp-078) may still be running; mark if unavailable.
502	
503	  - table_id: tab_kappa_generalization
504	    type: statistics
505	    placement: analysis
506	    width: "table"
507	    caption: >
508	      Independence-accuracy trade-off: Fleiss' κ and Eff-K across three
509	      aggregation methods on Mistral-7B FOLIO (exp-077). Debate achieves
510	      the highest Eff-K but collapses accuracy.
511	    columns: [Aggregation Method, "κ", "Eff-K", "Nominal K", "Δ (pp)"]
512	    data_source: "registry: exp-077"
513	    notes: >
514	      SC: κ=0.4384, Eff-K=2.02, K=10; Diverse-Prompt: κ=0.4030,
515	      Eff-K=2.21, K=12; Debate: κ=0.1549, Eff-K=4.44, K=12, Δ=-18.6pp.
516	      CAPSTONE finding: trade-off explains why same-model methods must fail.
517	
518	  # Appendix tables
519	  - table_id: tab_app_remediation
520	    type: comparison
521	    placement: appendix
522	    caption: "Nine prompt-level remediation strategies."
523	    columns: [Strategy, Dimension, Key Metric, Result, exp_id]
524	
525	  - table_id: tab_app_entropy
526	    type: analysis
527	    placement: appendix
528	    caption: "SICA Δ conditioned on per-problem answer entropy (high vs low)."
529	    columns: [Model, Dataset, "High-E n", "High-E Δ", "Low-E n", "Low-E Δ"]
530	
531	  - table_id: tab_app_power_analysis
532	    type: analysis
533	    placement: appendix
534	    caption: "Statistical power analysis for primary conditions."
535	
536	  - table_id: tab_app_bootstrap
537	    type: analysis
538	    placement: appendix
539	    caption: "Bootstrap 95% CIs for selected conditions."
540	
541	  - table_id: tab_app_constraint_quality
542	    type: analysis
543	    placement: appendix
544	    caption: "Constraint extraction quality metrics by model."
545	
546	  - table_id: tab_app_k_detail
547	    type: detail
548	    placement: appendix
549	    caption: "K sensitivity: full metrics at each K value."
550	
551	# ──────────────────────────────────────────────
552	# Literature Strategy
553	# ──────────────────────────────────────────────
554	literature_strategy:
555	  citation_budget: 42
556	  macro_context:
557	    - "self-consistency and majority voting in LLM reasoning"
558	    - "neuro-symbolic methods combining LLMs with formal solvers"
559	    - "Condorcet Jury Theorem and ensemble independence"
560	  micro_clusters:
561	    - cluster_name: "self_consistency_and_variants"
562	      target_count: 6
563	      must_cite:
564	        - "Wang et al. 2023 (Self-Consistency)"
565	        - "Chen et al. 2024 (USC)"
566	        - "Loo et al. 2025 (SC scaling plateau)"
567	        - "Taubenfeld et al. 2025 (confidence-weighted SC)"
568	        - "Li et al. 2023 (DiVeRSe)"
569	      search_queries:
570	        - "self-consistency majority voting LLM reasoning 2024 2025"
571	
572	    - cluster_name: "symbolic_reasoning_llm"
573	      target_count: 7
574	      must_cite:
575	        - "Pan et al. 2023 (Logic-LM)"
576	        - "Olausson et al. 2023 (LINC)"
577	        - "Xu et al. 2026 (DyLoS)"
578	        - "Li et al. 2025 (Aristotle)"
579	        - "Wang et al. 2025 (FoVer)"
580	      search_queries:
581	        - "neuro-symbolic reasoning LLM formal logic solver 2025 2026"
582	
583	    - cluster_name: "condorcet_voting_theory"
584	      target_count: 6
585	      must_cite:
586	        - "Condorcet 1785"
587	        - "Austen-Smith & Banks 1996"
588	        - "Ladha 1992 (correlated voters)"
589	        - "Lefort et al. 2024 (arXiv:2409.00094)"
590	        - "Fleiss 1971 (kappa)"
591	        - "Kish 1965 (design effect / Eff-K)"
592	      search_queries:
593	        - "Condorcet jury theorem ensemble independence machine learning"
594	
595	    - cluster_name: "verification_reranking"
596	      target_count: 4
597	      must_cite:
598	        - "Cobbe et al. 2021 (ORM/GSM8K)"
599	        - "Lightman et al. 2023 (PRM)"
600	        - "Wang et al. 2024 (Math-Shepherd)"
601	      search_queries:
602	        - "process reward model verification LLM 2024"
603	
604	    - cluster_name: "test_time_compute"
605	      target_count: 4
606	      must_cite:
607	        - "Snell et al. 2025 (scaling test-time compute)"
608	        - "DeepSeek-AI 2025 (DeepSeek-R1)"
609	      search_queries:
610	        - "test-time compute scaling reasoning 2025 2026"
611	
612	    - cluster_name: "debate_multi_agent"
613	      target_count: 3
614	      must_cite:
615	        - "Liang et al. 2023 (multi-agent debate)"
616	        - "Du et al. 2023 (improving factuality via debate)"
617	      search_queries:
618	        - "LLM multi-agent debate reasoning 2024"
619	
620	    - cluster_name: "self_correction_negative"
621	      target_count: 2
622	      must_cite:
623	        - "Huang et al. 2024 (cannot self-correct reasoning)"
624	      search_queries:
625	        - "LLM self-correction limitation negative result 2024"
626	
627	    - cluster_name: "benchmarks"
628	      target_count: 5
629	      must_cite:
630	        - "Han et al. 2022 (FOLIO)"
631	        - "Tafjord et al. 2021 (ProofWriter)"
632	        - "Liu et al. 2020 (LogiQA)"
633	        - "Geva et al. 2021 (StrategyQA)"
634	
635	    - cluster_name: "constraint_satisfaction"
636	      target_count: 2
637	      must_cite:
638	        - "de Moura & Bjorner 2008 (Z3)"
639	
640	    - cluster_name: "oracle_diagnostic_methodology"
641	      target_count: 2
642	      must_cite:
643	        - "Press et al. 2023 (compositionality gap)"
644	      search_queries:
645	        - "oracle upper bound diagnosis pipeline bottleneck NLP"
646	
647	# ──────────────────────────────────────────────
648	# Writing Order (strict serial)
649	# ──────────────────────────────────────────────
650	writing_order:
651	  - method          # Foundation: Condorcet + SICA + Oracle + Method interventions
652	  - experiments     # Data-driven: Table 1 + oracle + replication + failure modes
653	  - analysis        # Deep dive: independence + extraction + entropy + K/T + remediation
654	  - related_work    # Positioning: standalone, can reference method/experiments
655	  - introduction    # Synthesis: depends on all above
656	  - discussion      # Interpretation: depends on all empirical
657	  - abstract        # Summary: last written
658	  - conclusion      # Summary: last written
659	
660	# ──────────────────────────────────────────────
661	# Page Budget (8pp main text target)
662	# ──────────────────────────────────────────────
663	page_budget:
664	  target: 8.0
665	  breakdown:
666	    abstract: 0.3
667	    introduction: 1.3
668	    related_work: 0.8
669	    method: 1.1
670	    experiments: 1.8
671	    analysis: 1.5
672	    discussion: 0.5
673	    conclusion: 0.3
674	    total_text: 7.6
675	    display_items_float: 0.4
676	  notes:
677	    - "3 main-text figures + 3 main-text tables = 6 display items (within 4-7 budget for 8pp)"
678	    - "Oracle merged into Table 1 bottom rows (saves table float)"
679	    - "4-seed replication as rows in Table 1 (no separate table)"
680	    - "Prompt-level remediation: 1 paragraph main text + full table in appendix"
681	    - "Method interventions: compact table (3 rows) in main text"
682	    - "Entropy: compact paragraph + move detailed 8-condition table to appendix"
683	
684	# ──────────────────────────────────────────────
685	# Key Data (truth source: registry, verified .tex)
686	# ──────────────────────────────────────────────
687	key_data:
688	  hero_result:
689	    exp_id: exp-033
690	    model: Mistral-7B-Instruct-v0.3
691	    dataset: FOLIO-204
692	    seed: 42
693	    sc: 55.88
694	    sica: 59.31
695	    delta_pp: 3.43
696	    p: 0.092
697	    note: "NOT significant at α=0.05. Directional trend only."
698	
699	  replication_4seed:
700	    - {exp_id: exp-033, seed: 42, sc: 55.88, delta_pp: 3.43, p: 0.092}
701	    - {exp_id: exp-052, seed: 123, sc: 54.41, delta_pp: 2.94, p: 0.070}
702	    - {exp_id: exp-053, seed: 456, sc: 55.88, delta_pp: 0.00, p: 1.0}
703	    - {exp_id: exp-067, seed: 789, sc: 54.41, delta_pp: -0.49, p: 1.0}
704	    mean_delta: 1.47
705	    note: "2/4 marginal positive (p<0.10), 0/4 significant. Range +3.43 to -0.49."
706	
707	  oracle:
708	    - {exp_id: exp-031, dataset: FOLIO-204, oracle_acc: 89.71, sc: 75.49, delta_pp: 14.22, p: "<0.001"}
709	    - {exp_id: exp-022, dataset: PW-600, oracle_acc: 86.67, sc: 75.17, delta_pp: 11.50, p: "<0.001"}
710	    utilization: "24.1% (best seed 3.43 / oracle 14.22)"
711	
712	  type_c:
713	    exp_id: exp-046
714	    model: Mistral-7B
715	    dataset: ProofWriter-D5-600
716	    n: 600
717	    sc: 39.33
718	    sica: 36.50
719	    delta_pp: -2.83
720	    p: 0.014
721	
722	  independence:
723	    range_kappa: "0.21–0.82 (instruction-tuned), 0.91 (thinking)"
724	    range_eff_k: "1.20–3.62"
725	    mistral_folio_4seed_kappa: "0.41–0.51"
726	    mistral_folio_4seed_eff_k: "1.8–2.2"
727	
728	  method_interventions:
729	    - {method: ICG, folio_delta: "-2.0/+1.5 (2 seeds)", logiqa_delta: -0.5, mode: neutral}
730	    - {method: Contrastive, folio_delta: -9.31, logiqa_delta: "pending", mode: harmful}
731	    - {method: Debate, folio_delta: -18.63, logiqa_delta: "pending (RUNNING)", mode: catastrophic}
732	    note: "All tested on Mistral-7B. 7B scale caveat."
733	
734	  kappa_generalization:
735	    exp_id: exp-077
736	    status: DONE
737	    note: "CAPSTONE finding — independence-accuracy trade-off"
738	    data:
739	      - {method: "Self-Consistency", kappa: 0.4384, eff_k: 2.02, nominal_k: 10}
740	      - {method: "Diverse-Prompt", kappa: 0.4030, eff_k: 2.21, nominal_k: 12}
741	      - {method: "LLM-Debate", kappa: 0.1549, eff_k: 4.44, nominal_k: 12, delta: -18.6}
742	    insight: >
743	      Methods that increase independence (Debate: κ↓) destroy accuracy (Δ=-18.6pp).
744	      Methods that preserve accuracy (Diverse-Prompt) cannot break correlation (κ≈SC).
745	      This is a Pareto frontier, not an engineering gap.
746	
747	  pending_data:
748	    - {exp_id: exp-074d, desc: "ICG FOLIO seed456", status: PREPARING}
749	    - {exp_id: exp-078, desc: "Debate LogiQA", status: RUNNING}
750	    - {exp_id: exp-080, desc: "Contrastive LogiQA — check registry for final delta", status: DONE}
751	    note: "exp-077 DONE. Remaining expected by May 20 morning per Director"
752	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5f8e59a7-5571-4c3d-8eee-6d9e8d454b63",
  "isSidechain": false,
  "promptId": "3f50ba00-7d30-45ec-b450-7010d531c858",
  "type": "user",
  "uuid": "91c57cce-4e66-421d-b312-1863cc03c026",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/writing_plan.yaml",
      "content": "# Writing Plan — symb_invariant_consensus\n# Generated: 2026-05-19T20:30:00Z\n# Full Draft: Independence Bottleneck — \"Fundamental Limitation\" paper\n# Target: EMNLP 2026 ARR May cycle\n# Paper Agent Step 1 output\n\nmeta:\n  venue: EMNLP 2026\n  track: main (ARR May cycle)\n  template: docs/paper/acl.sty\n  template_note: \"ACL/EMNLP shared template already in paper directory\"\n  page_limit: 8\n  deadline: 2026-05-25\n  title: >\n    Beyond Self-Consistency: How Trace Independence Limits\n    Symbolic Consensus in LLM Reasoning\n  core_claim: >\n    Same-model self-extraction of symbolic constraints inherits trace\n    correlation (Fleiss' κ=0.21–0.82, Eff-K=1.20–3.62 for nominal K=12),\n    creating a structural independence bottleneck. Oracle gold-FOL yields\n    +14.22pp (p<0.001) proving aggregation is sound, but self-extraction\n    captures only 24%. κ generalization across aggregation methods reveals\n    a fundamental independence-accuracy trade-off: Debate reduces κ from\n    0.44→0.15 (Eff-K 2→4.4) but collapses accuracy by -18.6pp. Same-model\n    methods cannot increase independence without degrading the signal that\n    makes aggregation useful.\n  paper_type: \"Fundamental limitation analysis (Condorcet framework + empirical diagnosis + 12 remediation failures)\"\n  framing: \"Independence Bottleneck — structural limitation of same-model self-extraction\"\n  created_at: 2026-05-19T20:30:00Z\n\n# ──────────────────────────────────────────────\n# Contributions (5)\n# ──────────────────────────────────────────────\ncontributions:\n  - id: C1\n    label: \"Independence Bottleneck Quantification\"\n    status: VERIFIED\n    claim: >\n      Fleiss' κ=0.21–0.82 (instruction-tuned), 0.91 (thinking mode).\n      Eff-K=1.20–3.62 at K=12. Mistral 4-seed κ=0.41–0.51 (stable).\n      Qwen Eff-K≈1.2–1.5 → near-zero Δ; Mistral PW Eff-K=3.62 but\n      SC=39% → negative Δ. Dual requirement: sufficient Eff-K AND SC.\n    evidence: \"Table 3, §5.1\"\n\n  - id: C2\n    label: \"Oracle Gap Localizes Extraction Bottleneck\"\n    status: VERIFIED\n    claim: >\n      Gold FOL: +14.22pp FOLIO (p<0.001), +11.50pp PW (p<0.001).\n      Self-extraction captures 24% of oracle ceiling (best seed +3.43pp\n      vs +14.22pp). Aggregation mechanism sound; extraction quality is\n      the binding bottleneck.\n    evidence: \"Table 1 oracle rows, §4.3\"\n\n  - id: C3\n    label: \"Regime-Dependent Effect with 4-Seed Replication\"\n    status: VERIFIED\n    claim: >\n      Intermediate-SC (~50–55%): best seed +3.43pp (p=0.092, ns);\n      4-seed mean +1.47pp; 2/4 marginal (p<0.10), 0/4 significant.\n      Type A (SC≥60%): 9 conditions N>2,800, no significant positive;\n      significant negatives at -2.50pp (p=0.011) and -4.41pp (p=0.093).\n      Type C (SC≤40%): -2.83pp (p=0.014).\n    evidence: \"Table 1, Figure 2, §4.1–4.3\"\n\n  - id: C4\n    label: \"Independence-Accuracy Trade-off Is Fundamental\"\n    status: VERIFIED\n    claim: >\n      κ generalization (exp-077) reveals why same-model methods must fail:\n      SC κ=0.44 (Eff-K=2.02); Diverse-Prompt κ=0.40 (Eff-K=2.21, ≈SC);\n      Debate κ=0.15 (Eff-K=4.44) but Δ=-18.6pp. Methods that increase\n      independence (Debate) destroy accuracy; methods that preserve accuracy\n      (ICG, Diverse-Prompt) cannot break correlation. 12 remediations\n      (9 prompt + 3 method) all fail — not engineering failure but\n      fundamental trade-off in same-model aggregation.\n    evidence: \"§5.6, Table T7 (κ generalization), method intervention table\"\n\n  - id: C5\n    label: \"Entropy Decomposition Reveals Regime Mechanism\"\n    status: VERIFIED\n    claim: >\n      Low-entropy: SICA≈SC across all 8 conditions (Δ≈0). High-entropy\n      direction regime-dependent: +12.8pp intermediate-SC, -8.2pp Type A.\n      Explains dual-channel mechanism (voting diversity + constraint\n      homogenization).\n    evidence: \"§5.5, entropy analysis\"\n\n# ──────────────────────────────────────────────\n# Paper Outline\n# ──────────────────────────────────────────────\npaper_outline:\n  - section: abstract\n    file: abstract.tex\n    word_budget: 220\n    core_bullets:\n      - \"Problem: SC (majority voting) plateaus; CJT explains why — traces lack independence\"\n      - \"SICA pipeline evaluated across 6 models, 3 formal reasoning domains, N>3,000, 4-seed replication\"\n      - \"Independence quantification: κ=0.21–0.82, Eff-K=1.20–3.62 at K=12\"\n      - \"Regime: +3.43pp intermediate-SC (ns), -2.83pp Type C (p=0.014), ~0 Type A\"\n      - \"Oracle +14.22pp/+11.50pp proves aggregation sound; self-extraction 24%\"\n      - \"12 remediations (9 prompt + 3 method) all fail — bottleneck is structural\"\n      - \"C0+SC zero-cost deployment diagnostic; paths forward require independence\"\n    dependencies: [experiments, analysis, method]\n\n  - section: introduction\n    file: introduction.tex\n    word_budget: 1300\n    core_bullets:\n      - \"Hook: Test-time compute scaling via SC improves reasoning—but plateaus. Adding more traces yields diminishing returns.\"\n      - \"Gap: Neuro-symbolic methods (Logic-LM, DyLoS, FoVer) improve reasoning with external/trained components. Can same-model self-extraction of formal constraints break the SC plateau without external tools?\"\n      - \"Insight: CJT requires voter independence. Same-model traces violate this (Eff-K=1.20–3.62 for K=12). Self-extracted constraints inherit the correlation structure.\"\n      - \"Evaluation: SICA pipeline + Condorcet analysis + oracle control across 6 models × 3 domains, 4-seed replication\"\n      - \"Key result: Oracle +14.22pp proves mechanism works; self-extraction captures 24%. 12 remediations all fail.\"\n      - \"Contributions: C1–C5\"\n    dependencies: [experiments, analysis]\n    figures: [fig1_pipeline]\n    citation_hints:\n      - \"SC: Wang et al. 2023\"\n      - \"SC plateau: Loo et al. 2025\"\n      - \"Logic-LM: Pan et al. 2023\"\n      - \"DyLoS: Xu et al. 2026\"\n      - \"CJT: Condorcet 1785, Ladha 1992\"\n      - \"Self-correction parallel: Huang et al. 2024\"\n\n  - section: related_work\n    file: related_work.tex\n    word_budget: 750\n    core_bullets:\n      - \"SC and extensions: Wang 2023, USC, weighted SC (Taubenfeld 2025), DiVeRSe, scaling plateaus (Loo 2025)\"\n      - \"Neuro-symbolic reasoning: Logic-LM, LINC, DyLoS, Aristotle, FoVer — all use external/trained components; we test same-model self-extraction\"\n      - \"Condorcet/voting theory: CJT, correlated voters (Ladha 1992), LLM ensembles (Lefort 2024 arXiv:2409.00094, closest prior work)\"\n      - \"Verification and reranking: ORM (Cobbe 2021), PRM (Lightman 2023), Math-Shepherd — trained verifier paradigm\"\n      - \"Self-X limitations: Huang 2024 self-correction ≈ structural parallel to self-extraction\"\n      - \"Debate/multi-agent: Liang 2023, Du 2023 — different regime (multi-model or larger models)\"\n    dependencies: []\n\n  - section: method\n    file: method.tex\n    word_budget: 1100\n    subsections:\n      - id: \"sec:condorcet\"\n        title: \"Self-Consistency and the Condorcet Independence Assumption\"\n        word_budget: 300\n        bullets:\n          - \"SC as majority voting: sample K reasoning traces, select most common answer\"\n          - \"CJT: K independent voters each with p>0.5 → P(majority correct) → 1 as K→∞\"\n          - \"LLM traces violate independence: same model, same prompt, only sampling noise\"\n          - \"Eff-K = K/(1+(K-1)κ) via Kish (1965) design effect; κ = Fleiss' kappa (1971)\"\n          - \"When Eff-K≈1, additional traces ≈ no new information → SC plateau\"\n      - id: \"sec:sica-pipeline\"\n        title: \"SICA Pipeline\"\n        word_budget: 400\n        bullets:\n          - \"Step 1: Generate K reasoning traces at temperature T\"\n          - \"Step 2: Extract FOL constraints from each trace at T_ext=0.3\"\n          - \"Step 3: Syntactic deduplication across traces\"\n          - \"Step 4: Weighted partial MAX-SAT — hard clauses (answer assertion), soft clauses (constraints weighted by occurrence count)\"\n          - \"Step 5: Z3 solver evaluates each candidate; answer with highest satisfiable weight selected\"\n          - \"Timeout: 10s per candidate answer\"\n      - id: \"sec:oracle-design\"\n        title: \"Oracle Control Design\"\n        word_budget: 200\n        bullets:\n          - \"Replace self-extracted constraints with gold FOL annotations (FOLIO) or gold DSL (ProofWriter)\"\n          - \"Same Z3 evaluation pipeline; only constraint source changes\"\n          - \"Causal intervention: isolates constraint quality from aggregation mechanism\"\n      - id: \"sec:method-interventions\"\n        title: \"Method-Level Interventions\"\n        word_budget: 150\n        bullets:\n          - \"ICG: Generate constraints independently of traces (bypass trace-constraint coupling)\"\n          - \"Contrastive: Pro/con constraint scoring per candidate answer\"\n          - \"Debate: Proposer/Critic/Defense chain before constraint extraction\"\n          - \"Each targets a different bottleneck aspect\"\n    dependencies: []\n    figures: [fig1_pipeline]\n\n  - section: experiments\n    file: experiments.tex\n    word_budget: 1800\n    subsections:\n      - id: \"sec:exp-setup\"\n        title: \"Experimental Setup\"\n        word_budget: 300\n        bullets:\n          - \"6 models: Mistral-7B-Instruct-v0.3, LLaMA-3.1-8B-Instruct, Qwen2.5-7B-Instruct, Qwen2.5-14B-Instruct, Qwen3-14B (non-thinking), Qwen3-14B (thinking mode for κ analysis)\"\n          - \"3 formal reasoning domains: FOLIO (n=204), ProofWriter depth-5 (n=600), LogiQA (n=200)\"\n          - \"Cross-domain diagnostic: StrategyQA (n=200)\"\n          - \"Degenerate probes: QwQ-32B (AIME 2024), Qwen2.5-14B (GSM8K)\"\n          - \"Default: K=12, T=0.7, T_ext=0.3, Z3 timeout 10s\"\n          - \"Metrics: accuracy (%), Δ=SICA−SC (pp), McNemar exact test α=0.05\"\n          - \"4-seed replication on primary condition (Mistral-7B FOLIO)\"\n      - id: \"sec:main-results\"\n        title: \"Main Results: A Regime-Dependent Effect\"\n        word_budget: 500\n        bullets:\n          - \"Table 1: ~18 conditions grouped by regime + 2 oracle rows\"\n          - \"Intermediate-SC (SC~50–55%): Mistral FOLIO best seed +3.43pp (p=0.092 ns); 4-seed mean +1.47pp; Mistral LogiQA +0.50pp\"\n          - \"Type A (SC≥60%): 9 conditions N>2,800; no significant positive effect\"\n          - \"  Significant negatives: Qwen14B PW -2.50pp (p=0.011); Mistral PW -2.83pp (p=0.014)\"\n          - \"  LLaMA FOLIO -4.41pp (p=0.093, marginal)\"\n          - \"  Qwen3-14B FOLIO -0.49pp, PW +0.67pp — generational scaling does not help\"\n          - \"Type C (SC≤40%): Mistral PW-D5 Δ=-2.83pp p=0.014 — SICA significantly hurts\"\n          - \"Degenerate: C0<5% → SICA≡SC by construction\"\n          - \"Figure 2: SC vs Δ scatter showing regime boundaries\"\n      - id: \"sec:oracle\"\n        title: \"Oracle Control: Aggregation Is Sound\"\n        word_budget: 250\n        bullets:\n          - \"FOLIO: oracle-SICA 89.71% vs SC 75.49% (+14.22pp, p<0.001)\"\n          - \"ProofWriter: oracle-SICA 86.67% vs SC 75.17% (+11.50pp, p<0.001)\"\n          - \"Self-extraction captures only 24.1% of FOLIO oracle ceiling\"\n          - \"Aggregation mechanism is sound; extraction quality is binding constraint\"\n      - id: \"sec:replication\"\n        title: \"Four-Seed Replication\"\n        word_budget: 250\n        bullets:\n          - \"Mistral-7B FOLIO-204: seeds 42, 123, 456, 789\"\n          - \"s42: Δ=+3.43pp p=0.092; s123: +2.94pp p=0.070; s456: 0.00pp p=1.0; s789: -0.49pp p=1.0\"\n          - \"2/4 marginal positive (p<0.10); 0/4 reaches p<0.05\"\n          - \"4-seed mean: +1.47pp; range: +3.43 to -0.49\"\n          - \"Fragility itself is the finding — motivates independence analysis\"\n      - id: \"sec:failure-modes\"\n        title: \"Failure Mode Analysis\"\n        word_budget: 250\n        bullets:\n          - \"Type A: consistent traces → constraints mirror model's answers → MAX-SAT degenerates to counting\"\n          - \"Type B: domain not formalizable (LogiQA contradiction rate 0.8%)\"\n          - \"Type C: predominantly wrong traces → wrong constraints → solver amplifies errors\"\n    dependencies: []\n    tables: [tab1_main_results]\n    figures: [fig2_regime_scatter]\n    registry_refs:\n      - exp-033  # Mistral FOLIO s42 (hero)\n      - exp-052  # Mistral FOLIO s123\n      - exp-053  # Mistral FOLIO s456\n      - exp-067  # Mistral FOLIO s789\n      - exp-046  # Mistral PW-600 (Type C)\n      - exp-049b # Mistral LogiQA\n      - exp-063  # LLaMA FOLIO\n      - exp-019  # LLaMA StrategyQA\n      - exp-061  # Qwen2.5-7B FOLIO\n      - exp-026  # Qwen2.5-14B FOLIO (regen)\n      - exp-038  # Qwen2.5-14B LogiQA\n      - exp-039  # Qwen2.5-14B PW-600\n      - exp-044b # Qwen2.5-14B FOLIO ICL\n      - exp-027  # Qwen3-14B FOLIO\n      - exp-040  # Qwen3-14B PW-600\n      - exp-031  # Oracle FOLIO\n      - exp-022  # Oracle PW\n\n  - section: analysis\n    file: analysis.tex\n    word_budget: 1500\n    subsections:\n      - id: \"sec:effective-k\"\n        title: \"Condorcet Independence Analysis\"\n        word_budget: 350\n        bullets:\n          - \"Table 3: Fleiss' κ and Eff-K per model-domain condition\"\n          - \"Mistral FOLIO 4 seeds: κ=0.41–0.51, Eff-K=1.8–2.2 (cross-seed stable)\"\n          - \"Qwen family: κ=0.66–0.82, Eff-K=1.2–1.5 → all near-zero Δ\"\n          - \"Mistral PW: κ=0.21, Eff-K=3.62 but SC=39% → negative (highest independence, insufficient quality)\"\n          - \"Qwen3-14B thinking: κ=0.91, Eff-K=1.09 → 'better reasoning' worsens independence\"\n          - \"Dual requirement: need both sufficient Eff-K AND sufficient SC\"\n          - \"Explains SC plateau: traces beyond Eff-K provide no new information\"\n      - id: \"sec:extraction-taxonomy\"\n        title: \"Constraint Quality Analysis\"\n        word_budget: 200\n        bullets:\n          - \"Discriminative rate: ~8.2% (95% CI [7.6, 8.8])\"\n          - \"Removing non-discriminative constraints: 0 gain → problem is direction not quality\"\n          - \"Variable naming: 56.4% cross-trace constraint pairs share zero Z3 variables\"\n          - \"~92% constraints ARE discriminative but discriminate in same direction as model bias\"\n      - id: \"sec:entropy\"\n        title: \"Entropy Decomposition\"\n        word_budget: 200\n        bullets:\n          - \"Per-problem answer entropy separates SICA operating point\"\n          - \"Low-entropy: SICA≈SC across all 8 conditions (Δ≈0) — traces agree, constraints add nothing\"\n          - \"High-entropy: regime-dependent — +12.8pp intermediate-SC (s42), -8.2pp Type A (Qwen14B)\"\n          - \"High-entropy proportion: Mistral 38% vs Qwen 18% → explains model-level Δ differences\"\n          - \"Mechanism: low-entropy = direct CJT channel; high-entropy = indirect constraint channel\"\n      - id: \"sec:ablation\"\n        title: \"MAX-SAT Ablation\"\n        word_budget: 100\n        bullets:\n          - \"MAX-SAT vs count-only: 803/804 agreement (Qwen14B, n=804)\"\n          - \"Self-extracted constraints carry no signal beyond vote counts in high-SC regime\"\n          - \"Confirms independence bottleneck causes MAX-SAT to degenerate\"\n      - id: \"sec:k-t-sensitivity\"\n        title: \"K and Temperature Sensitivity\"\n        word_budget: 200\n        bullets:\n          - \"K sensitivity: K=4(-1.47), K=8(-1.96), K=12(+3.43), K=16(+1.47), K=20(+1.96)\"\n          - \"K=12 is only setting with Δ>2pp; not clean inverted-U\"\n          - \"T sensitivity: T=0.3(-1.47), T=0.5(-0.98), T=0.7(+3.43), T=1.0(0.00)\"\n          - \"T=0.7 is isolated spike; only 1/4 temperatures positive\"\n          - \"Both K=12 and T=0.7 coincide with lowest SC baseline → confound with operating window\"\n          - \"Figure 3: two-panel K/T sensitivity plot\"\n      - id: \"sec:remediation\"\n        title: \"Remediation Analysis\"\n        word_budget: 350\n        bullets:\n          - \"--- Prompt-level (9 strategies, 6 dimensions) ---\"\n          - \"Prompting: contrastive extraction (disc_rate 8.2%→6.0%, Δ still mirrors bias)\"\n          - \"Architecture: cross-model bilateral (weak→strong: 0% disc; strong→weak: ±1pp of self)\"\n          - \"Capability: generational scaling Qwen3-14B (+0.49pp ns)\"\n          - \"Verification: Z3 feedback (0.9% UNSAT), cross-trace UNSAT (56.4% zero shared vars)\"\n          - \"Diversity: multi-temp (Δ=0.00pp), T=1.0 (Δ=0.00pp — collapse from +3.43)\"\n          - \"Filtering: discriminative constraint filtering (0 gain), consistency filtering (reverts to SC)\"\n          - \"ICL with gold FOL examples (+0.50pp ns)\"\n          - \"--- Method-level (3 methods × 2 datasets) ---\"\n          - \"ICG (Independent Constraint Gen.): FOLIO Δ=-2.0/+1.5pp (noise), LogiQA -0.5pp → neutral\"\n          - \"  Insight: independent constraints ≈ trace-sourced → bias from problem understanding stage\"\n          - \"Contrastive (Pro/Con Scoring): FOLIO -9.3pp, LogiQA pending → harmful\"\n          - \"  Insight: 26% degenerate scoring, pro/con imbalance (94 pro vs 65 con)\"\n          - \"Debate (Proposer/Critic): FOLIO -18.6pp, LogiQA pending → catastrophic\"\n          - \"  Insight: 7B role-play degradation; same-model debate = same bias + cognitive overhead\"\n          - \"Scale caveat: all method-level tested at 7B; 14B+ may differ\"\n          - \"--- κ Generalization: Independence-Accuracy Trade-off (exp-077, CAPSTONE) ---\"\n          - \"Table T7: SC κ=0.44 Eff-K=2.02 | Diverse-Prompt κ=0.40 Eff-K=2.21 | Debate κ=0.15 Eff-K=4.44\"\n          - \"Diverse-Prompt ≈ SC κ → changing prompts cannot break correlation\"\n          - \"Debate breaks κ (0.44→0.15) but accuracy collapses (-18.6pp)\"\n          - \"FUNDAMENTAL TRADE-OFF: methods that increase independence destroy accuracy; methods that preserve accuracy cannot break correlation\"\n          - \"This explains WHY same-model methods must fail — not just that they do\"\n          - \"Implication: breaking bottleneck requires cross-model or external signal (consistent with oracle)\"\n    dependencies: [experiments]\n    tables: [tab3_independence, tab_method_interventions, tab_kappa_generalization]\n    figures: [fig3_sensitivity]\n    registry_refs:\n      - exp-029  # contrastive prompting\n      - exp-030  # cross-model extraction\n      - exp-059  # cross-model Qwen3→Mistral\n      - exp-060  # cross-model Qwen14B→Mistral\n      - exp-027  # Qwen3-14B (generational)\n      - exp-036  # Z3 feedback\n      - exp-036b # cross-trace UNSAT\n      - exp-043  # consistency filtering\n      - exp-055  # multi-temp\n      - exp-054  # T=1.0\n      - exp-057  # T=0.3\n      - exp-058  # T=0.5\n      - exp-044b # ICL gold FOL\n      - exp-074  # ICG FOLIO s42\n      - exp-074c # ICG FOLIO s123\n      - exp-075b # Contrastive FOLIO\n      - exp-076  # Debate FOLIO\n      - exp-079  # ICG LogiQA\n      - exp-080  # Contrastive LogiQA\n      - exp-078  # Debate LogiQA (RUNNING)\n      - exp-077  # κ generalization (CAPSTONE)\n\n  - section: discussion\n    file: discussion.tex\n    word_budget: 450\n    core_bullets:\n      - \"Oracle causally isolates: aggregation mechanism sound, extraction is binding bottleneck\"\n      - \"Dual-channel mechanism: direct (voting diversity → SC plateau) + indirect (constraint homogenization → MAX-SAT degeneration)\"\n      - \"Oracle disambiguates: gold constraints on same correlated traces yield +14.22pp → indirect channel is proximal bottleneck\"\n      - \"Independence-accuracy trade-off (exp-077): Debate breaks κ (0.44→0.15) but collapses accuracy (-18.6pp). Diverse-Prompt ≈ SC κ. Same-model methods face a fundamental Pareto frontier.\"\n      - \"This trade-off explains WHY same-model methods must fail, not just that they do. Breaking correlation within a single model's distribution necessarily degrades the signal.\"\n      - \"Published methods (DyLoS, Aristotle, FoVer, Logic-LM) bypass same-model extraction — consistent with trade-off: cross-model/external sources are naturally independent without sacrificing quality\"\n      - \"Statistical evidence: 0/4 seeds significant positive; only significant effects are negative\"\n      - \"C0+SC deployment diagnostic: C0<5%→degenerate, high SC→confirmation bias, low SC→error amplification\"\n      - \"Three paths forward trade simplicity for independence: trained extractors, external provers, multi-model pipelines — all introduce signal outside the model's own distribution\"\n    dependencies: [experiments, analysis]\n\n  - section: conclusion\n    file: conclusion.tex\n    word_budget: 300\n    core_bullets:\n      - \"SICA evaluated: 6 models spanning 3 families, 3 reasoning domains, N>3,000, 4-seed replication\"\n      - \"Independence bottleneck: κ=0.21–0.82, Eff-K=1.20–3.62 → explains SC plateau and SICA failure\"\n      - \"Intermediate-SC region: +3.43pp best seed (ns), 4-seed mean +1.47pp (2/4 positive, 2/4 null/negative)\"\n      - \"Oracle +14.22pp/+11.50pp (p<0.001); 12 remediations all fail; independence-accuracy trade-off explains why\"\n      - \"Limitations: trained extractors untested, narrow intermediate-SC zone, 7B-scale method testing, formal reasoning domains only\"\n    dependencies: [experiments, analysis]\n\n# ──────────────────────────────────────────────\n# Visualization Plan\n# ──────────────────────────────────────────────\nvisualization_plan:\n  - fig_id: fig1_pipeline\n    type: conceptual\n    tool: matplotlib\n    description: >\n      SICA pipeline diagram: K traces → FOL constraint extraction →\n      dedup → weighted partial MAX-SAT (Z3) → answer selection.\n      Oracle branch replaces self-extracted constraints with gold FOL.\n      Independence bottleneck annotation at extraction stage.\n    narrative_intent: >\n      The pipeline looks like it should introduce independent symbolic\n      signal, but self-extraction inherits the same trace correlation —\n      the independence bottleneck manifests at the extraction stage.\n    design_notes:\n      - \"Existing figure in paper; update to annotate independence bottleneck clearly\"\n      - \"Add oracle branch as parallel path with green highlight\"\n      - \"Add method-level intervention points (ICG/Contrastive/Debate) as annotation\"\n    placement: method\n    aspect_ratio: \"16:6\"\n    data_source: \"manual (diagram)\"\n    status: \"EXISTS — label update needed\"\n\n  - fig_id: fig2_regime_scatter\n    type: statistical\n    tool: matplotlib\n    description: >\n      SC accuracy (x-axis) vs SICA Δpp (y-axis) scatter plot.\n      All model-domain conditions from Table 1. 4 replication seeds\n      as separate points. Color/marker by model family.\n      Shaded intermediate-SC band (50–55%). Regime zone labels.\n    narrative_intent: >\n      The intermediate-SC region is narrow and model-specific. Outside it,\n      SICA is either neutral (Type A) or harmful (Type C). No condition\n      shows statistically significant improvement.\n    design_notes:\n      - \"Pattern A: regime bands — light shading 50-55% SC, labeled zones\"\n      - \"Solid markers: n≥100; hollow: n<50\"\n      - \"Horizontal Δ=0 reference line (dashed)\"\n      - \"4 Mistral FOLIO seeds clustered at SC≈54-56%\"\n      - \"Star or bold outline for significant effects (p<0.05)\"\n      - \"Annotate LLaMA -4.41pp as 'upper boundary' of intermediate-SC\"\n    placement: experiments\n    aspect_ratio: \"4:3\"\n    data_source: \"registry: all Table 1 conditions (~18 points + oracle excluded)\"\n    status: \"EXISTS — needs regeneration with 4-seed + new experiments\"\n\n  - fig_id: fig3_sensitivity\n    type: statistical\n    tool: matplotlib\n    description: >\n      Two-panel figure. (a) K sensitivity: K=4,8,12,16,20 vs Δpp.\n      (b) T sensitivity: T=0.3,0.5,0.7,1.0 vs Δpp. Both annotated\n      with SC baseline at each point.\n    narrative_intent: >\n      SICA's optimal hyperparameters are fragile: K=12 is the only\n      setting with Δ>2pp, T=0.7 is an isolated spike. Both peaks\n      coincide with the lowest SC baseline, suggesting the effect\n      reflects operating window rather than causal K/T contribution.\n    design_notes:\n      - \"Panel (a): line plot K vs Δ, secondary y-axis or annotation for SC\"\n      - \"Panel (b): line plot T vs Δ, annotate SC at each T\"\n      - \"Dashed Δ=0 reference line in both panels\"\n      - \"Highlight K=12 and T=0.7 as peaks; annotate SC values\"\n      - \"Pattern: minimal, 2-panel with shared y-axis scale if possible\"\n    placement: analysis\n    aspect_ratio: \"2:1\"\n    data_source: >\n      K sensitivity: exp-051 data (K=4,8,12,16,20).\n      T sensitivity: exp-033 (T=0.7), exp-054 (T=1.0), exp-057 (T=0.3), exp-058 (T=0.5).\n    status: \"EXISTS — needs regeneration with corrected data + T panel\"\n\n# ──────────────────────────────────────────────\n# Table Plan\n# ──────────────────────────────────────────────\ntable_plan:\n  # Main text tables\n  - table_id: tab1_main_results\n    type: comparison\n    placement: experiments\n    width: \"table*\"\n    caption: >\n      SICA vs SC across all model-domain conditions (K=12, T=0.7).\n      Grouped by SC accuracy regime. Bold: significant effects (p<0.05).\n      Bottom: oracle controls with gold FOL annotations.\n    columns: [Model, Domain, n, \"SC (%)\", \"SICA (%)\", \"Δ (pp)\", \"p\"]\n    data_source: \"registry: see experiments.registry_refs\"\n    notes: >\n      ~18 data rows grouped as: Type C / Intermediate-SC (4 seeds) /\n      Type A (9 conditions) / Degenerate / Oracle. Footnotes for\n      StrategyQA diagnostic and ICL condition.\n\n  - table_id: tab3_independence\n    type: statistics\n    placement: analysis\n    width: \"table\"\n    caption: >\n      Condorcet independence metrics per model-domain condition.\n      κ = Fleiss' kappa (K=12 traces), Eff-K = K/(1+(K-1)κ).\n    columns: [Model (seed), Domain, \"κ\", \"Eff-K\", \"SC (%)\", \"SICA Δ (pp)\"]\n    data_source: \"comp-1 verified κ values + registry\"\n    notes: >\n      ~14 rows including 4 Mistral FOLIO seeds, Mistral PW/LogiQA,\n      Qwen family, Qwen3 thinking mode.\n\n  - table_id: tab_method_interventions\n    type: comparison\n    placement: analysis\n    width: \"table\"\n    caption: >\n      Method-level interventions targeting the independence bottleneck\n      (Mistral-7B). Each targets a different aspect: ICG bypasses\n      trace-constraint coupling, Contrastive adds adversarial scoring,\n      Debate adds multi-role reasoning.\n    columns: [Method, Target Aspect, \"FOLIO Δ (pp)\", \"LogiQA Δ (pp)\", Failure Mode]\n    data_source: \"registry: exp-074, exp-074c, exp-075b, exp-076, exp-079, exp-080, exp-078\"\n    notes: >\n      3 methods × 2 datasets. ICG has multi-seed on FOLIO.\n      Debate LogiQA (exp-078) may still be running; mark if unavailable.\n\n  - table_id: tab_kappa_generalization\n    type: statistics\n    placement: analysis\n    width: \"table\"\n    caption: >\n      Independence-accuracy trade-off: Fleiss' κ and Eff-K across three\n      aggregation methods on Mistral-7B FOLIO (exp-077). Debate achieves\n      the highest Eff-K but collapses accuracy.\n    columns: [Aggregation Method, \"κ\", \"Eff-K\", \"Nominal K\", \"Δ (pp)\"]\n    data_source: \"registry: exp-077\"\n    notes: >\n      SC: κ=0.4384, Eff-K=2.02, K=10; Diverse-Prompt: κ=0.4030,\n      Eff-K=2.21, K=12; Debate: κ=0.1549, Eff-K=4.44, K=12, Δ=-18.6pp.\n      CAPSTONE finding: trade-off explains why same-model methods must fail.\n\n  # Appendix tables\n  - table_id: tab_app_remediation\n    type: comparison\n    placement: appendix\n    caption: \"Nine prompt-level remediation strategies.\"\n    columns: [Strategy, Dimension, Key Metric, Result, exp_id]\n\n  - table_id: tab_app_entropy\n    type: analysis\n    placement: appendix\n    caption: \"SICA Δ conditioned on per-problem answer entropy (high vs low).\"\n    columns: [Model, Dataset, \"High-E n\", \"High-E Δ\", \"Low-E n\", \"Low-E Δ\"]\n\n  - table_id: tab_app_power_analysis\n    type: analysis\n    placement: appendix\n    caption: \"Statistical power analysis for primary conditions.\"\n\n  - table_id: tab_app_bootstrap\n    type: analysis\n    placement: appendix\n    caption: \"Bootstrap 95% CIs for selected conditions.\"\n\n  - table_id: tab_app_constraint_quality\n    type: analysis\n    placement: appendix\n    caption: \"Constraint extraction quality metrics by model.\"\n\n  - table_id: tab_app_k_detail\n    type: detail\n    placement: appendix\n    caption: \"K sensitivity: full metrics at each K value.\"\n\n# ──────────────────────────────────────────────\n# Literature Strategy\n# ──────────────────────────────────────────────\nliterature_strategy:\n  citation_budget: 42\n  macro_context:\n    - \"self-consistency and majority voting in LLM reasoning\"\n    - \"neuro-symbolic methods combining LLMs with formal solvers\"\n    - \"Condorcet Jury Theorem and ensemble independence\"\n  micro_clusters:\n    - cluster_name: \"self_consistency_and_variants\"\n      target_count: 6\n      must_cite:\n        - \"Wang et al. 2023 (Self-Consistency)\"\n        - \"Chen et al. 2024 (USC)\"\n        - \"Loo et al. 2025 (SC scaling plateau)\"\n        - \"Taubenfeld et al. 2025 (confidence-weighted SC)\"\n        - \"Li et al. 2023 (DiVeRSe)\"\n      search_queries:\n        - \"self-consistency majority voting LLM reasoning 2024 2025\"\n\n    - cluster_name: \"symbolic_reasoning_llm\"\n      target_count: 7\n      must_cite:\n        - \"Pan et al. 2023 (Logic-LM)\"\n        - \"Olausson et al. 2023 (LINC)\"\n        - \"Xu et al. 2026 (DyLoS)\"\n        - \"Li et al. 2025 (Aristotle)\"\n        - \"Wang et al. 2025 (FoVer)\"\n      search_queries:\n        - \"neuro-symbolic reasoning LLM formal logic solver 2025 2026\"\n\n    - cluster_name: \"condorcet_voting_theory\"\n      target_count: 6\n      must_cite:\n        - \"Condorcet 1785\"\n        - \"Austen-Smith & Banks 1996\"\n        - \"Ladha 1992 (correlated voters)\"\n        - \"Lefort et al. 2024 (arXiv:2409.00094)\"\n        - \"Fleiss 1971 (kappa)\"\n        - \"Kish 1965 (design effect / Eff-K)\"\n      search_queries:\n        - \"Condorcet jury theorem ensemble independence machine learning\"\n\n    - cluster_name: \"verification_reranking\"\n      target_count: 4\n      must_cite:\n        - \"Cobbe et al. 2021 (ORM/GSM8K)\"\n        - \"Lightman et al. 2023 (PRM)\"\n        - \"Wang et al. 2024 (Math-Shepherd)\"\n      search_queries:\n        - \"process reward model verification LLM 2024\"\n\n    - cluster_name: \"test_time_compute\"\n      target_count: 4\n      must_cite:\n        - \"Snell et al. 2025 (scaling test-time compute)\"\n        - \"DeepSeek-AI 2025 (DeepSeek-R1)\"\n      search_queries:\n        - \"test-time compute scaling reasoning 2025 2026\"\n\n    - cluster_name: \"debate_multi_agent\"\n      target_count: 3\n      must_cite:\n        - \"Liang et al. 2023 (multi-agent debate)\"\n        - \"Du et al. 2023 (improving factuality via debate)\"\n      search_queries:\n        - \"LLM multi-agent debate reasoning 2024\"\n\n    - cluster_name: \"self_correction_negative\"\n      target_count: 2\n      must_cite:\n        - \"Huang et al. 2024 (cannot self-correct reasoning)\"\n      search_queries:\n        - \"LLM self-correction limitation negative result 2024\"\n\n    - cluster_name: \"benchmarks\"\n      target_count: 5\n      must_cite:\n        - \"Han et al. 2022 (FOLIO)\"\n        - \"Tafjord et al. 2021 (ProofWriter)\"\n        - \"Liu et al. 2020 (LogiQA)\"\n        - \"Geva et al. 2021 (StrategyQA)\"\n\n    - cluster_name: \"constraint_satisfaction\"\n      target_count: 2\n      must_cite:\n        - \"de Moura & Bjorner 2008 (Z3)\"\n\n    - cluster_name: \"oracle_diagnostic_methodology\"\n      target_count: 2\n      must_cite:\n        - \"Press et al. 2023 (compositionality gap)\"\n      search_queries:\n        - \"oracle upper bound diagnosis pipeline bottleneck NLP\"\n\n# ──────────────────────────────────────────────\n# Writing Order (strict serial)\n# ──────────────────────────────────────────────\nwriting_order:\n  - method          # Foundation: Condorcet + SICA + Oracle + Method interventions\n  - experiments     # Data-driven: Table 1 + oracle + replication + failure modes\n  - analysis        # Deep dive: independence + extraction + entropy + K/T + remediation\n  - related_work    # Positioning: standalone, can reference method/experiments\n  - introduction    # Synthesis: depends on all above\n  - discussion      # Interpretation: depends on all empirical\n  - abstract        # Summary: last written\n  - conclusion      # Summary: last written\n\n# ──────────────────────────────────────────────\n# Page Budget (8pp main text target)\n# ──────────────────────────────────────────────\npage_budget:\n  target: 8.0\n  breakdown:\n    abstract: 0.3\n    introduction: 1.3\n    related_work: 0.8\n    method: 1.1\n    experiments: 1.8\n    analysis: 1.5\n    discussion: 0.5\n    conclusion: 0.3\n    total_text: 7.6\n    display_items_float: 0.4\n  notes:\n    - \"3 main-text figures + 3 main-text tables = 6 display items (within 4-7 budget for 8pp)\"\n    - \"Oracle merged into Table 1 bottom rows (saves table float)\"\n    - \"4-seed replication as rows in Table 1 (no separate table)\"\n    - \"Prompt-level remediation: 1 paragraph main text + full table in appendix\"\n    - \"Method interventions: compact table (3 rows) in main text\"\n    - \"Entropy: compact paragraph + move detailed 8-condition table to appendix\"\n\n# ──────────────────────────────────────────────\n# Key Data (truth source: registry, verified .tex)\n# ──────────────────────────────────────────────\nkey_data:\n  hero_result:\n    exp_id: exp-033\n    model: Mistral-7B-Instruct-v0.3\n    dataset: FOLIO-204\n    seed: 42\n    sc: 55.88\n    sica: 59.31\n    delta_pp: 3.43\n    p: 0.092\n    note: \"NOT significant at α=0.05. Directional trend only.\"\n\n  replication_4seed:\n    - {exp_id: exp-033, seed: 42, sc: 55.88, delta_pp: 3.43, p: 0.092}\n    - {exp_id: exp-052, seed: 123, sc: 54.41, delta_pp: 2.94, p: 0.070}\n    - {exp_id: exp-053, seed: 456, sc: 55.88, delta_pp: 0.00, p: 1.0}\n    - {exp_id: exp-067, seed: 789, sc: 54.41, delta_pp: -0.49, p: 1.0}\n    mean_delta: 1.47\n    note: \"2/4 marginal positive (p<0.10), 0/4 significant. Range +3.43 to -0.49.\"\n\n  oracle:\n    - {exp_id: exp-031, dataset: FOLIO-204, oracle_acc: 89.71, sc: 75.49, delta_pp: 14.22, p: \"<0.001\"}\n    - {exp_id: exp-022, dataset: PW-600, oracle_acc: 86.67, sc: 75.17, delta_pp: 11.50, p: \"<0.001\"}\n    utilization: \"24.1% (best seed 3.43 / oracle 14.22)\"\n\n  type_c:\n    exp_id: exp-046\n    model: Mistral-7B\n    dataset: ProofWriter-D5-600\n    n: 600\n    sc: 39.33\n    sica: 36.50\n    delta_pp: -2.83\n    p: 0.014\n\n  independence:\n    range_kappa: \"0.21–0.82 (instruction-tuned), 0.91 (thinking)\"\n    range_eff_k: \"1.20–3.62\"\n    mistral_folio_4seed_kappa: \"0.41–0.51\"\n    mistral_folio_4seed_eff_k: \"1.8–2.2\"\n\n  method_interventions:\n    - {method: ICG, folio_delta: \"-2.0/+1.5 (2 seeds)\", logiqa_delta: -0.5, mode: neutral}\n    - {method: Contrastive, folio_delta: -9.31, logiqa_delta: \"pending\", mode: harmful}\n    - {method: Debate, folio_delta: -18.63, logiqa_delta: \"pending (RUNNING)\", mode: catastrophic}\n    note: \"All tested on Mistral-7B. 7B scale caveat.\"\n\n  kappa_generalization:\n    exp_id: exp-077\n    status: DONE\n    note: \"CAPSTONE finding — independence-accuracy trade-off\"\n    data:\n      - {method: \"Self-Consistency\", kappa: 0.4384, eff_k: 2.02, nominal_k: 10}\n      - {method: \"Diverse-Prompt\", kappa: 0.4030, eff_k: 2.21, nominal_k: 12}\n      - {method: \"LLM-Debate\", kappa: 0.1549, eff_k: 4.44, nominal_k: 12, delta: -18.6}\n    insight: >\n      Methods that increase independence (Debate: κ↓) destroy accuracy (Δ=-18.6pp).\n      Methods that preserve accuracy (Diverse-Prompt) cannot break correlation (κ≈SC).\n      This is a Pareto frontier, not an engineering gap.\n\n  pending_data:\n    - {exp_id: exp-074d, desc: \"ICG FOLIO seed456\", status: PREPARING}\n    - {exp_id: exp-078, desc: \"Debate LogiQA\", status: RUNNING}\n    - {exp_id: exp-080, desc: \"Contrastive LogiQA — check registry for final delta\", status: DONE}\n    note: \"exp-077 DONE. Remaining expected by May 20 morning per Director\"\n",
      "numLines": 752,
      "startLine": 1,
      "totalLines": 752
    }
  },
  "sourceToolAssistantUUID": "5f8e59a7-5571-4c3d-8eee-6d9e8d454b63",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora"
}
```

</details>

---


### Runtime record

_source line 8876_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[服务器重启后首条消息] 当前日期: 2026-05-20。服务器刚重启，项目状态可能已更新。不要依赖对话历史中的状态信息，以 registry 当前值为准。  **用户消息：** [Director 指令] ## 写作任务：EMNLP 2026 ARR May 25 — Full Draft 更新  **DDL**: May 25, 2026（5 天） **模式**: Full Draft 更新…",
  "leafUuid": "91c57cce-4e66-421d-b312-1863cc03c026",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1"
}
```

---


### Runtime record

_source line 8877_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise paper results with oracle FOLIO constraint experiments",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1"
}
```

---


### Assistant

_source line 8878 · 2026-05-20T09:39:15.496Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a thorough understanding of everything. Let me also read the paper_framing.md more carefully for the D085 updates — I can see that it's comprehensive in the file I already read. Let me now also check the registry for the new experiments mentioned in the framing (confirmation bias, process-κ, and the 13 new direction experiments).

Let me search for the registry.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "91c57cce-4e66-421d-b312-1863cc03c026",
  "isSidechain": false,
  "requestId": "req_011CbDbf3D1LcpFzDjEjaC6X",
  "type": "assistant",
  "uuid": "5c8f1376-ea95-475d-a207-d2b3d87e6a00",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qe3v2XSQxMvYGpk52PG2ed",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13776,
      "cache_read_input_tokens": 68114,
      "output_tokens": 214,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13776,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 214,
          "cache_read_input_tokens": 68114,
          "cache_creation_input_tokens": 13776,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13776
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

_source line 8879 · 2026-05-20T09:39:16.080Z_

Let me check the registry for the new experiments (confirmation bias, process-κ, and wave 1-3 experiments).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5c8f1376-ea95-475d-a207-d2b3d87e6a00",
  "isSidechain": false,
  "requestId": "req_011CbDbf3D1LcpFzDjEjaC6X",
  "type": "assistant",
  "uuid": "2f413e27-d0ad-4ee4-abec-64f61b3aa206",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qe3v2XSQxMvYGpk52PG2ed",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13776,
      "cache_read_input_tokens": 68114,
      "output_tokens": 214,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13776,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 214,
          "cache_read_input_tokens": 68114,
          "cache_creation_input_tokens": 13776,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13776
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

_source line 8880 · 2026-05-20T09:39:16.640Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01KB67ZXSnkjmykaK5JtdsvB`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2f413e27-d0ad-4ee4-abec-64f61b3aa206",
  "isSidechain": false,
  "requestId": "req_011CbDbf3D1LcpFzDjEjaC6X",
  "type": "assistant",
  "uuid": "e41568e6-44cd-4805-9336-173abb88476b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qe3v2XSQxMvYGpk52PG2ed",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13776,
      "cache_read_input_tokens": 68114,
      "output_tokens": 214,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13776,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 214,
          "cache_read_input_tokens": 68114,
          "cache_creation_input_tokens": 13776,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13776
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

_source line 8881 · 2026-05-20T09:39:16.643Z_

<details><summary>↩ Tool result · `toolu_01KB67ZXSnkjmykaK5JtdsvB`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__read_registry"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e41568e6-44cd-4805-9336-173abb88476b",
  "isSidechain": false,
  "promptId": "3f50ba00-7d30-45ec-b450-7010d531c858",
  "type": "user",
  "uuid": "c8e456f8-2dd2-4176-9e2b-99a902c7ddb2",
  "toolUseResult": {
    "matches": [
      "mcp__agent-ml-research__read_registry"
    ],
    "query": "select:mcp__agent-ml-research__read_registry",
    "total_deferred_tools": 51
  },
  "sourceToolAssistantUUID": "e41568e6-44cd-4805-9336-173abb88476b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora"
}
```

</details>

---


### Tool call

_source line 8882 · 2026-05-20T09:39:20.319Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01AgWoty2HKurcmHdM3Gxcrn`</summary>

```json
{
  "project": "symb_invariant_consensus",
  "filters": {
    "status": "DONE"
  },
  "fields": [
    "exp_id",
    "title",
    "conclusion",
    "metrics"
  ],
  "limit": 50
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c8e456f8-2dd2-4176-9e2b-99a902c7ddb2",
  "isSidechain": false,
  "requestId": "req_011CbDbfVsPEdfVYnfuCukgs",
  "type": "assistant",
  "uuid": "296867dc-00d4-4cc1-9c77-f8b50c23298e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011NByiv7W3ZnpJvDjbtzgEF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 575,
      "cache_read_input_tokens": 81890,
      "output_tokens": 139,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 575,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 139,
          "cache_read_input_tokens": 81890,
          "cache_creation_input_tokens": 575,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 575
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

_source line 8883 · 2026-05-20T09:39:20.797Z_

<details><summary>↩ Tool result · `toolu_01AgWoty2HKurcmHdM3Gxcrn`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {\"exp-wave3-dir-i-z3-filter\": {\"conclusion\": \"negative\", \"metrics\": {\"n\": 204, \"sc_baseline\": 54.41, \"filtered_sc\": 53.92, \"delta_pp\": -0.49, \"unsat_traces\": 142, \"unsat_rate_pct\": 5.8, \"filter_precision_pct\": 49.12, \"questions_affected\": 7, \"improved\": 3, \"degraded\": 4}}, \"exp-wave3-dir-j-bootstrap\": {\"conclusion\": \"negative\", \"metrics\": {\"n\": 204, \"sc_baseline\": 54.41, \"r1_accuracy\": 56.86, \"r1_delta_pp\": 2.45, \"r1_flips\": 32, \"r1_improved\": 15, \"r1_degraded\": 10, \"r2_accuracy\": 54.41, \"r3_accuracy\": 54.9, \"r4_accuracy\": 54.41, \"r5_accuracy\": 52.45, \"convergence\": \"oscillating, no convergence\"}}, \"exp-cross-model-phase2\": {\"conclusion\": \"negative\", \"metrics\": {\"n\": 204, \"cross_sc_accuracy\": 74.51, \"cross_sica_accuracy\": 74.02, \"delta_pp\": -0.49, \"mcnemar_p\": 1, \"config\": \"Mistral-7B(4) + LLaMA-8B(4) + Qwen-7B(4), K=12\"}}, \"exp-direction-d-cegis\": {\"conclusion\": \"negative\", \"metrics\": {\"n\": 204, \"sc_baseline\": 54.41, \"r1_accuracy\": 57.84, \"r1_delta_pp\": 3.43, \"r2_accuracy\": 57.35, \"r2_delta_pp\": 2.94, \"r3_accuracy\": 57.84, \"r3_delta_pp\": 3.43, \"r1_unsat_traces\": 127, \"r2_unsat_traces\": 48, \"r3_unsat_traces\": 25, \"wall_time_min\": 51, \"extraction_calls\": 2448, \"refinement_calls\": 175}}, \"exp-confirmation-bias\": {\"conclusion\": \"success\", \"metrics\": {\"bias_ratio\": 4.97, \"wrong_constraints_when_sica_errs\": 0.833, \"sica_errors_follow_sc\": 0.94}}, \"exp-cross-model-phase1\": {\"conclusion\": \"success\", \"metrics\": {\"kappa_cross\": 0.422, \"kappa_within\": 0.532, \"eff_k_cross\": 2.11, \"eff_k_within\": 1.52, \"accuracy_gain\": 0}}, \"exp-direction-e-abstention\": {\"conclusion\": \"success\", \"metrics\": {\"auroc\": 0.673, \"coverage_80pct_delta_pp\": 4.4, \"coverage_60pct_delta_pp\": 8.8}}, \"exp-wild6-kappa-aware-sc\": {\"conclusion\": \"negative\", \"metrics\": {\"conditions_tested\": 11, \"delta_pp_all\": 0, \"finding\": \"accuracy monotonically increases with agreement, SC already optimal\"}}, \"exp-wild1-max-unsat\": {\"conclusion\": \"negative\", \"metrics\": {\"min_unsat_delta_pp\": -6.5, \"mean_excluded_constraints\": 1.3}}, \"exp-wild4-process-kappa\": {\"conclusion\": \"negative\", \"metrics\": {\"answer_kappa\": 0.4093, \"process_cosine_mean\": 0.6902, \"pearson_r\": -0.064, \"pearson_p\": 0.36, \"same_answer_diff_process_pct\": 9.3}}, \"exp-direction-a-prove\": {\"conclusion\": \"negative\", \"metrics\": {\"code_gen_rate\": 0.152, \"conclusive_rate\": 0.078, \"conclusive_accuracy\": 0.5, \"prove_fallback_accuracy\": 0.716, \"sc_baseline\": 0.735, \"delta_pp\": -1.9}}, \"exp-direction-b-deepconf\": {\"conclusion\": \"negative\", \"metrics\": {\"filtered_sc_75pct\": 52.9, \"filtered_sica_75pct\": 54.4, \"filtered_sc_50pct\": 52.9, \"logprob_correct\": -0.135, \"logprob_incorrect\": -0.141, \"delta_pp\": 0}}, \"exp-wild3-perturbation\": {\"conclusion\": \"negative\", \"metrics\": {\"original_k4_kappa\": 0.59, \"perturbed_k4_kappa\": 0.696, \"mixed_k8_kappa\": 0.627, \"original_sc_acc\": 80, \"perturbed_sc_acc\": 76.7, \"mixed_sc_acc\": 80}}, \"exp-wild2-ascii\": {\"conclusion\": \"negative\", \"metrics\": {\"group_a_standard_kappa\": 0.3906, \"group_b_fixed_padding_kappa\": 0.4006, \"group_c_variable_padding_kappa\": 0.3638, \"group_a_sc_acc\": 53.92, \"group_b_sc_acc\": 57.84, \"group_c_sc_acc\": 53.92}}, \"exp-084-debate-mistral-logiqa-seed123\": {\"conclusion\": \"negative\", \"metrics\": {\"n\": 200, \"debate_accuracy\": 0.29, \"sc_accuracy\": 0.505, \"delta\": -0.215, \"fallbacks\": 14, \"total_constraints\": 3220, \"wall_time_min\": 226.3}}, \"exp-082-contrastive-mistral-folio-seed123\": {\"metrics\": {\"sc_accuracy\": 0.549, \"contrastive_accuracy\": 0.4951, \"delta\": -0.0539, \"n_samples\": 204, \"wall_time_min\": 206.3, \"degenerate_count\": 35, \"pro_constraints\": 1036, \"con_constraints\": 920}, \"conclusion\": \"negative\"}, \"exp-081-debate-mistral-folio-seed123\": {\"metrics\": {\"sc_accuracy\": 0.5588, \"debate_accuracy\": 0.4069, \"delta\": -0.152, \"n_samples\": 204, \"wall_time_min\": 177.6, \"fallbacks\": 18, \"both_correct\": 56, \"debate_improved\": 27, \"debate_degraded\": 58, \"both_wrong\": 63}, \"conclusion\": \"negative\"}, \"exp-085-contrastive-mistral-logiqa-seed123\": {\"conclusion\": \"negative\", \"metrics\": {\"n\": 200, \"contrastive_accuracy\": 0.535, \"sc_accuracy\": 0.56, \"delta\": -0.025, \"delta_pp\": -2.5, \"contrastive_correct\": 107, \"sc_correct\": 112, \"k\": 12, \"k_contrast\": 3, \"temperature\": 0.7, \"seed\": 123, \"degenerate_count\": 51, \"total_pro_constraints\": 736, \"total_con_constraints\": 1059, \"wall_time_min\": 100.9}}, \"exp-013-constraint-ablation\": {\"conclusion\": \"success\", \"metrics\": {\"maxsat_acc\": 0.4229, \"count_only_acc\": 0.4216, \"random_weight_acc\": \"0.4206±0.0042\", \"sc_acc\": 0.4316, \"delta_maxsat_vs_countonly_pp\": 0.12, \"delta_maxsat_vs_sc_pp\": -0.87, \"agreement_maxsat_countonly\": 0.944, \"n_problems\": 804, \"folio_maxsat\": 0.5931, \"folio_count\": 0.5686, \"folio_sc\": 0.5441, \"pw_maxsat\": 0.365, \"pw_count\": 0.3717, \"pw_sc\": 0.3933}}, \"exp-075b-contrastive-mistral-folio\": {\"conclusion\": \"negative\", \"metrics\": {\"sc_accuracy\": 0.5686, \"contrastive_accuracy\": 0.4755, \"delta\": -0.0931, \"n_samples\": 204, \"wall_time_min\": 193.6, \"degenerate_count\": 41}}, \"exp-080-contrastive-mistral-logiqa200\": {\"conclusion\": \"negative\", \"metrics\": {\"n\": 200, \"contrastive_accuracy\": 0.455, \"sc_accuracy\": 0.5, \"delta\": -0.045, \"k\": 12, \"k_contrast\": 3, \"temperature\": 0.7, \"seed\": 42, \"total_wall_time_s\": 6645.9, \"total_pro_constraints\": 762, \"total_con_constraints\": 1192, \"degenerate_count\": 42}}, \"exp-078-debate-mistral-logiqa200\": {\"conclusion\": \"negative\", \"metrics\": {\"sc_accuracy\": 0.5, \"debate_accuracy\": 0.27, \"delta\": -0.23, \"n_samples\": 200, \"wall_time_min\": 211.5, \"fallbacks\": 16}}, \"exp-078\": {\"conclusion\": \"negative\", \"metrics\": {\"sc_accuracy\": 0.5, \"debate_accuracy\": 0.27, \"delta\": -0.23, \"n_samples\": 200, \"fallbacks\": 16, \"wall_time_min\": 211.5}}, \"exp-083-icg-mistral-logiqa-seed123\": {\"conclusion\": \"negative\", \"metrics\": {\"n\": 200, \"sc_accuracy\": 0.365, \"icg_accuracy\": 0.33, \"delta_pp\": -3.5, \"sc_correct\": 73, \"icg_correct\": 66, \"both_correct\": 62, \"sc_only\": 11, \"icg_only\": 4, \"neither\": 123, \"mean_constraints_generated\": 31.4, \"mean_constraints_unique\": 27.9, \"mean_maxsat_satisfied\": 27.7, \"mean_maxsat_excluded\": 0.2, \"wall_time_s\": 3653.7, \"mean_wall_time_s\": 18.3}}, \"exp-074d-icg-mistral-folio-seed456\": {\"conclusion\": \"negative\", \"metrics\": {\"sc_accuracy\": 0.5588, \"icg_accuracy\": 0.549, \"delta\": -0.0098, \"n_samples\": 204, \"wall_time_min\": 57.3, \"three_seed_mean_sc\": 0.5572, \"three_seed_mean_icg\": 0.5523, \"three_seed_mean_delta\": -0.0049, \"three_seed_std_delta\": 0.0177, \"three_seed_details\": {\"seed_42\": {\"sc\": 0.5392, \"icg\": 0.5196, \"delta\": -0.0196}, \"seed_123\": {\"sc\": 0.5735, \"icg\": 0.5882, \"delta\": 0.0147}, \"seed_456\": {\"sc\": 0.5588, \"icg\": 0.549, \"delta\": -0.0098}}}}, \"exp-077-kappa-generalization\": {\"conclusion\": \"negative\", \"metrics\": {\"sc_kappa\": 0.4384, \"sc_eff_k\": 2.02, \"sc_nominal_k\": 10, \"debate_kappa\": 0.1549, \"debate_eff_k\": 4.44, \"debate_nominal_k\": 12, \"diverse_prompt_kappa\": 0.403, \"diverse_prompt_eff_k\": 2.21, \"diverse_prompt_nominal_k\": 12, \"n_samples\": 204}}, \"exp-077\": {\"metrics\": {\"sc_kappa\": 0.4384, \"sc_eff_k\": 2.02, \"debate_kappa\": 0.1549, \"debate_eff_k\": 4.44, \"diverse_prompt_kappa\": 0.403, \"diverse_prompt_eff_k\": 2.21, \"n_questions\": 204, \"all_kappa_gt_04\": false, \"wall_time_min\": 184.9}, \"conclusion\": \"negative\"}, \"exp-075b\": {\"conclusion\": \"negative\", \"metrics\": {\"sc_accuracy\": 0.5686, \"contrastive_accuracy\": 0.4755, \"delta\": -0.0931, \"n_samples\": 204, \"degenerate\": 41, \"wall_time_min\": 193.6}}, \"exp-074c-icg-mistral-folio-seed123\": {\"metrics\": {\"sc_accuracy\": 0.5735, \"icg_accuracy\": 0.5882, \"delta\": 0.0147, \"n_samples\": 204, \"wall_time_min\": 56.5}, \"conclusion\": \"negative\"}, \"exp-076-debate-mistral-folio\": {\"conclusion\": \"negative\", \"metrics\": {\"sc_accuracy\": 0.5686, \"debate_accuracy\": 0.3824, \"delta\": -0.1863, \"n_samples\": 204, \"wall_time_min\": 186.4, \"fallbacks\": 10, \"total_debate_constraints\": 3677}}, \"exp-079-icg-mistral-logiqa200\": {\"conclusion\": \"negative\", \"metrics\": {\"sc_accuracy\": 0.475, \"icg_accuracy\": 0.47, \"delta\": -0.005, \"n_samples\": 200, \"wall_time_min\": 54.3}}, \"exp-072b-llama8b-logiqa200\": {\"conclusion\": \"negative\", \"metrics\": {\"sc_accuracy\": 0.595, \"sica_accuracy\": 0.585, \"delta\": -0.01, \"n_samples\": 200, \"k\": 12, \"wall_time_s\": 7310.5, \"extraction_success\": 2292, \"extraction_fail_json_parse\": 108}}, \"exp-074-icg-mistral-folio\": {\"metrics\": {\"sc_accuracy\": 0.5392, \"icg_accuracy\": 0.5196, \"delta\": -0.0196, \"n_samples\": 204, \"k\": 12, \"k_icg\": 10, \"wall_time_s\": 3368}, \"conclusion\": \"negative\"}, \"exp-073b-qwen7b-logiqa200-seed456\": {\"metrics\": {\"sc_accuracy\": 0.695, \"sica_accuracy\": 0.715, \"delta\": 0.02, \"n_samples\": 200, \"k\": 12, \"wall_time_s\": 3517.3}, \"conclusion\": \"success\"}, \"exp-073-qwen7b-logiqa200-seed456\": {\"conclusion\": \"success\", \"metrics\": {\"sc_accuracy\": 0.7, \"sica_accuracy\": 0.705, \"delta\": 0.005, \"n_samples\": 200}}, \"exp-072-llama8b-logiqa200\": {\"conclusion\": \"success\", \"metrics\": {\"sc_accuracy\": 0.62, \"sica_accuracy\": 0.63, \"delta\": 0.01, \"n_samples\": 200}}, \"exp-064-deepseek-r1-qwen3-8b-folio204\": {\"conclusion\": \"success\", \"metrics\": {\"sc_accuracy\": 0.8382, \"sica_accuracy\": 0.8382, \"delta\": 0, \"n_samples\": 204, \"extraction_rate\": 0.3818, \"contradiction_rate\": 0.0165, \"wall_time_min\": 355.6}}, \"exp-075-contrastive-mistral-folio\": {\"conclusion\": \"failed\"}, \"exp-071-qwen7b-logiqa200-seed123\": {\"conclusion\": \"negative\", \"metrics\": {\"sc_accuracy\": 0.69, \"sica_accuracy\": 0.685, \"delta\": -0.005, \"n_samples\": 200}}, \"exp-048-llama8b-pw600\": {\"conclusion\": \"negative\", \"metrics\": {\"sc_accuracy\": 0.7, \"sica_accuracy\": 0.648, \"delta\": -0.052, \"n_samples\": 600}}, \"exp-053-mistral-folio204-seed456\": {\"conclusion\": \"killed\"}, \"exp-052-mistral-folio204-seed123\": {\"conclusion\": \"killed\"}, \"exp-069-llama8b-logiqa200\": {\"conclusion\": \"negative\", \"metrics\": {\"sc_accuracy\": 0.61, \"sica_accuracy\": 0.585, \"delta\": -0.025, \"n_samples\": 200}}, \"exp-065-qwen7b-pw600\": {\"conclusion\": \"negative\", \"metrics\": {\"sc_accuracy\": 0.72, \"sica_accuracy\": 0.68, \"delta\": -0.04, \"n_samples\": 600}}, \"exp-062-gemma27b-folio204\": {\"conclusion\": \"negative\", \"metrics\": {\"sc_accuracy\": 0.809, \"sica_accuracy\": 0.804, \"delta\": -0.005, \"n_samples\": 204}}, \"exp-069-mistral-logiqa200\": {\"conclusion\": \"negative\", \"metrics\": {\"sc_accuracy\": 0.495, \"sica_accuracy\": 0.465, \"delta\": -0.03, \"n_samples\": 200}}, \"exp-070-qwen7b-logiqa200\": {\"conclusion\": \"success\", \"metrics\": {\"sc_accuracy\": 0.685, \"sica_accuracy\": 0.71, \"delta\": 0.025, \"n_samples\": 200, \"sc_correct\": 137, \"sica_correct\": 142, \"discordant_b\": 1, \"discordant_c\": 6, \"mcnemar_chi2\": 2.2857, \"mcnemar_p\": 0.131, \"mcnemar_p_exact\": 0.125, \"significant_005\": false, \"cohens_kappa\": 0.917, \"kappa_interpretation\": \"almost_perfect\"}}, \"exp-068-qwen3-logiqa200\": {\"conclusion\": \"negative\", \"metrics\": {\"sc_accuracy\": 0.81, \"sica_accuracy\": 0.81, \"delta\": 0, \"n_samples\": 200}}, \"exp-064\": {\"conclusion\": \"killed\"}, \"exp-067-mistral-folio-seed789\": {\"conclusion\": \"success\", \"metrics\": {\"sc_accuracy\": 0.5441, \"sica_accuracy\": 0.5392, \"delta_pp\": -0.49, \"n\": 204, \"mcnemar_b\": 6, \"mcnemar_c\": 5, \"mcnemar_p\": 1, \"mcnemar_significant\": false, \"fleiss_kappa_raw\": 0.4124, \"eff_k\": 2.17}}}, \"count\": 50, \"total\": 136, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4604}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "296867dc-00d4-4cc1-9c77-f8b50c23298e",
  "isSidechain": false,
  "promptId": "3f50ba00-7d30-45ec-b450-7010d531c858",
  "type": "user",
  "uuid": "d268b20c-2d8b-4b16-be28-5b4c387a6d0e",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {\\\"exp-wave3-dir-i-z3-filter\\\": {\\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"n\\\": 204, \\\"sc_baseline\\\": 54.41, \\\"filtered_sc\\\": 53.92, \\\"delta_pp\\\": -0.49, \\\"unsat_traces\\\": 142, \\\"unsat_rate_pct\\\": 5.8, \\\"filter_precision_pct\\\": 49.12, \\\"questions_affected\\\": 7, \\\"improved\\\": 3, \\\"degraded\\\": 4}}, \\\"exp-wave3-dir-j-bootstrap\\\": {\\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"n\\\": 204, \\\"sc_baseline\\\": 54.41, \\\"r1_accuracy\\\": 56.86, \\\"r1_delta_pp\\\": 2.45, \\\"r1_flips\\\": 32, \\\"r1_improved\\\": 15, \\\"r1_degraded\\\": 10, \\\"r2_accuracy\\\": 54.41, \\\"r3_accuracy\\\": 54.9, \\\"r4_accuracy\\\": 54.41, \\\"r5_accuracy\\\": 52.45, \\\"convergence\\\": \\\"oscillating, no convergence\\\"}}, \\\"exp-cross-model-phase2\\\": {\\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"n\\\": 204, \\\"cross_sc_accuracy\\\": 74.51, \\\"cross_sica_accuracy\\\": 74.02, \\\"delta_pp\\\": -0.49, \\\"mcnemar_p\\\": 1, \\\"config\\\": \\\"Mistral-7B(4) + LLaMA-8B(4) + Qwen-7B(4), K=12\\\"}}, \\\"exp-direction-d-cegis\\\": {\\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"n\\\": 204, \\\"sc_baseline\\\": 54.41, \\\"r1_accuracy\\\": 57.84, \\\"r1_delta_pp\\\": 3.43, \\\"r2_accuracy\\\": 57.35, \\\"r2_delta_pp\\\": 2.94, \\\"r3_accuracy\\\": 57.84, \\\"r3_delta_pp\\\": 3.43, \\\"r1_unsat_traces\\\": 127, \\\"r2_unsat_traces\\\": 48, \\\"r3_unsat_traces\\\": 25, \\\"wall_time_min\\\": 51, \\\"extraction_calls\\\": 2448, \\\"refinement_calls\\\": 175}}, \\\"exp-confirmation-bias\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"bias_ratio\\\": 4.97, \\\"wrong_constraints_when_sica_errs\\\": 0.833, \\\"sica_errors_follow_sc\\\": 0.94}}, \\\"exp-cross-model-phase1\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"kappa_cross\\\": 0.422, \\\"kappa_within\\\": 0.532, \\\"eff_k_cross\\\": 2.11, \\\"eff_k_within\\\": 1.52, \\\"accuracy_gain\\\": 0}}, \\\"exp-direction-e-abstention\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"auroc\\\": 0.673, \\\"coverage_80pct_delta_pp\\\": 4.4, \\\"coverage_60pct_delta_pp\\\": 8.8}}, \\\"exp-wild6-kappa-aware-sc\\\": {\\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"conditions_tested\\\": 11, \\\"delta_pp_all\\\": 0, \\\"finding\\\": \\\"accuracy monotonically increases with agreement, SC already optimal\\\"}}, \\\"exp-wild1-max-unsat\\\": {\\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"min_unsat_delta_pp\\\": -6.5, \\\"mean_excluded_constraints\\\": 1.3}}, \\\"exp-wild4-process-kappa\\\": {\\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"answer_kappa\\\": 0.4093, \\\"process_cosine_mean\\\": 0.6902, \\\"pearson_r\\\": -0.064, \\\"pearson_p\\\": 0.36, \\\"same_answer_diff_process_pct\\\": 9.3}}, \\\"exp-direction-a-prove\\\": {\\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"code_gen_rate\\\": 0.152, \\\"conclusive_rate\\\": 0.078, \\\"conclusive_accuracy\\\": 0.5, \\\"prove_fallback_accuracy\\\": 0.716, \\\"sc_baseline\\\": 0.735, \\\"delta_pp\\\": -1.9}}, \\\"exp-direction-b-deepconf\\\": {\\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"filtered_sc_75pct\\\": 52.9, \\\"filtered_sica_75pct\\\": 54.4, \\\"filtered_sc_50pct\\\": 52.9, \\\"logprob_correct\\\": -0.135, \\\"logprob_incorrect\\\": -0.141, \\\"delta_pp\\\": 0}}, \\\"exp-wild3-perturbation\\\": {\\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"original_k4_kappa\\\": 0.59, \\\"perturbed_k4_kappa\\\": 0.696, \\\"mixed_k8_kappa\\\": 0.627, \\\"original_sc_acc\\\": 80, \\\"perturbed_sc_acc\\\": 76.7, \\\"mixed_sc_acc\\\": 80}}, \\\"exp-wild2-ascii\\\": {\\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"group_a_standard_kappa\\\": 0.3906, \\\"group_b_fixed_padding_kappa\\\": 0.4006, \\\"group_c_variable_padding_kappa\\\": 0.3638, \\\"group_a_sc_acc\\\": 53.92, \\\"group_b_sc_acc\\\": 57.84, \\\"group_c_sc_acc\\\": 53.92}}, \\\"exp-084-debate-mistral-logiqa-seed123\\\": {\\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"n\\\": 200, \\\"debate_accuracy\\\": 0.29, \\\"sc_accuracy\\\": 0.505, \\\"delta\\\": -0.215, \\\"fallbacks\\\": 14, \\\"total_constraints\\\": 3220, \\\"wall_time_min\\\": 226.3}}, \\\"exp-082-contrastive-mistral-folio-seed123\\\": {\\\"metrics\\\": {\\\"sc_accuracy\\\": 0.549, \\\"contrastive_accuracy\\\": 0.4951, \\\"delta\\\": -0.0539, \\\"n_samples\\\": 204, \\\"wall_time_min\\\": 206.3, \\\"degenerate_count\\\": 35, \\\"pro_constraints\\\": 1036, \\\"con_constraints\\\": 920}, \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-081-debate-mistral-folio-seed123\\\": {\\\"metrics\\\": {\\\"sc_accuracy\\\": 0.5588, \\\"debate_accuracy\\\": 0.4069, \\\"delta\\\": -0.152, \\\"n_samples\\\": 204, \\\"wall_time_min\\\": 177.6, \\\"fallbacks\\\": 18, \\\"both_correct\\\": 56, \\\"debate_improved\\\": 27, \\\"debate_degraded\\\": 58, \\\"both_wrong\\\": 63}, \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-085-contrastive-mistral-logiqa-seed123\\\": {\\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"n\\\": 200, \\\"contrastive_accuracy\\\": 0.535, \\\"sc_accuracy\\\": 0.56, \\\"delta\\\": -0.025, \\\"delta_pp\\\": -2.5, \\\"contrastive_correct\\\": 107, \\\"sc_correct\\\": 112, \\\"k\\\": 12, \\\"k_contrast\\\": 3, \\\"temperature\\\": 0.7, \\\"seed\\\": 123, \\\"degenerate_count\\\": 51, \\\"total_pro_constraints\\\": 736, \\\"total_con_constraints\\\": 1059, \\\"wall_time_min\\\": 100.9}}, \\\"exp-013-constraint-ablation\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"maxsat_acc\\\": 0.4229, \\\"count_only_acc\\\": 0.4216, \\\"random_weight_acc\\\": \\\"0.4206±0.0042\\\", \\\"sc_acc\\\": 0.4316, \\\"delta_maxsat_vs_countonly_pp\\\": 0.12, \\\"delta_maxsat_vs_sc_pp\\\": -0.87, \\\"agreement_maxsat_countonly\\\": 0.944, \\\"n_problems\\\": 804, \\\"folio_maxsat\\\": 0.5931, \\\"folio_count\\\": 0.5686, \\\"folio_sc\\\": 0.5441, \\\"pw_maxsat\\\": 0.365, \\\"pw_count\\\": 0.3717, \\\"pw_sc\\\": 0.3933}}, \\\"exp-075b-contrastive-mistral-folio\\\": {\\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"sc_accuracy\\\": 0.5686, \\\"contrastive_accuracy\\\": 0.4755, \\\"delta\\\": -0.0931, \\\"n_samples\\\": 204, \\\"wall_time_min\\\": 193.6, \\\"degenerate_count\\\": 41}}, \\\"exp-080-contrastive-mistral-logiqa200\\\": {\\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"n\\\": 200, \\\"contrastive_accuracy\\\": 0.455, \\\"sc_accuracy\\\": 0.5, \\\"delta\\\": -0.045, \\\"k\\\": 12, \\\"k_contrast\\\": 3, \\\"temperature\\\": 0.7, \\\"seed\\\": 42, \\\"total_wall_time_s\\\": 6645.9, \\\"total_pro_constraints\\\": 762, \\\"total_con_constraints\\\": 1192, \\\"degenerate_count\\\": 42}}, \\\"exp-078-debate-mistral-logiqa200\\\": {\\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"sc_accuracy\\\": 0.5, \\\"debate_accuracy\\\": 0.27, \\\"delta\\\": -0.23, \\\"n_samples\\\": 200, \\\"wall_time_min\\\": 211.5, \\\"fallbacks\\\": 16}}, \\\"exp-078\\\": {\\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"sc_accuracy\\\": 0.5, \\\"debate_accuracy\\\": 0.27, \\\"delta\\\": -0.23, \\\"n_samples\\\": 200, \\\"fallbacks\\\": 16, \\\"wall_time_min\\\": 211.5}}, \\\"exp-083-icg-mistral-logiqa-seed123\\\": {\\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"n\\\": 200, \\\"sc_accuracy\\\": 0.365, \\\"icg_accuracy\\\": 0.33, \\\"delta_pp\\\": -3.5, \\\"sc_correct\\\": 73, \\\"icg_correct\\\": 66, \\\"both_correct\\\": 62, \\\"sc_only\\\": 11, \\\"icg_only\\\": 4, \\\"neither\\\": 123, \\\"mean_constraints_generated\\\": 31.4, \\\"mean_constraints_unique\\\": 27.9, \\\"mean_maxsat_satisfied\\\": 27.7, \\\"mean_maxsat_excluded\\\": 0.2, \\\"wall_time_s\\\": 3653.7, \\\"mean_wall_time_s\\\": 18.3}}, \\\"exp-074d-icg-mistral-folio-seed456\\\": {\\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"sc_accuracy\\\": 0.5588, \\\"icg_accuracy\\\": 0.549, \\\"delta\\\": -0.0098, \\\"n_samples\\\": 204, \\\"wall_time_min\\\": 57.3, \\\"three_seed_mean_sc\\\": 0.5572, \\\"three_seed_mean_icg\\\": 0.5523, \\\"three_seed_mean_delta\\\": -0.0049, \\\"three_seed_std_delta\\\": 0.0177, \\\"three_seed_details\\\": {\\\"seed_42\\\": {\\\"sc\\\": 0.5392, \\\"icg\\\": 0.5196, \\\"delta\\\": -0.0196}, \\\"seed_123\\\": {\\\"sc\\\": 0.5735, \\\"icg\\\": 0.5882, \\\"delta\\\": 0.0147}, \\\"seed_456\\\": {\\\"sc\\\": 0.5588, \\\"icg\\\": 0.549, \\\"delta\\\": -0.0098}}}}, \\\"exp-077-kappa-generalization\\\": {\\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"sc_kappa\\\": 0.4384, \\\"sc_eff_k\\\": 2.02, \\\"sc_nominal_k\\\": 10, \\\"debate_kappa\\\": 0.1549, \\\"debate_eff_k\\\": 4.44, \\\"debate_nominal_k\\\": 12, \\\"diverse_prompt_kappa\\\": 0.403, \\\"diverse_prompt_eff_k\\\": 2.21, \\\"diverse_prompt_nominal_k\\\": 12, \\\"n_samples\\\": 204}}, \\\"exp-077\\\": {\\\"metrics\\\": {\\\"sc_kappa\\\": 0.4384, \\\"sc_eff_k\\\": 2.02, \\\"debate_kappa\\\": 0.1549, \\\"debate_eff_k\\\": 4.44, \\\"diverse_prompt_kappa\\\": 0.403, \\\"diverse_prompt_eff_k\\\": 2.21, \\\"n_questions\\\": 204, \\\"all_kappa_gt_04\\\": false, \\\"wall_time_min\\\": 184.9}, \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-075b\\\": {\\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"sc_accuracy\\\": 0.5686, \\\"contrastive_accuracy\\\": 0.4755, \\\"delta\\\": -0.0931, \\\"n_samples\\\": 204, \\\"degenerate\\\": 41, \\\"wall_time_min\\\": 193.6}}, \\\"exp-074c-icg-mistral-folio-seed123\\\": {\\\"metrics\\\": {\\\"sc_accuracy\\\": 0.5735, \\\"icg_accuracy\\\": 0.5882, \\\"delta\\\": 0.0147, \\\"n_samples\\\": 204, \\\"wall_time_min\\\": 56.5}, \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-076-debate-mistral-folio\\\": {\\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"sc_accuracy\\\": 0.5686, \\\"debate_accuracy\\\": 0.3824, \\\"delta\\\": -0.1863, \\\"n_samples\\\": 204, \\\"wall_time_min\\\": 186.4, \\\"fallbacks\\\": 10, \\\"total_debate_constraints\\\": 3677}}, \\\"exp-079-icg-mistral-logiqa200\\\": {\\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"sc_accuracy\\\": 0.475, \\\"icg_accuracy\\\": 0.47, \\\"delta\\\": -0.005, \\\"n_samples\\\": 200, \\\"wall_time_min\\\": 54.3}}, \\\"exp-072b-llama8b-logiqa200\\\": {\\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"sc_accuracy\\\": 0.595, \\\"sica_accuracy\\\": 0.585, \\\"delta\\\": -0.01, \\\"n_samples\\\": 200, \\\"k\\\": 12, \\\"wall_time_s\\\": 7310.5, \\\"extraction_success\\\": 2292, \\\"extraction_fail_json_parse\\\": 108}}, \\\"exp-074-icg-mistral-folio\\\": {\\\"metrics\\\": {\\\"sc_accuracy\\\": 0.5392, \\\"icg_accuracy\\\": 0.5196, \\\"delta\\\": -0.0196, \\\"n_samples\\\": 204, \\\"k\\\": 12, \\\"k_icg\\\": 10, \\\"wall_time_s\\\": 3368}, \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-073b-qwen7b-logiqa200-seed456\\\": {\\\"metrics\\\": {\\\"sc_accuracy\\\": 0.695, \\\"sica_accuracy\\\": 0.715, \\\"delta\\\": 0.02, \\\"n_samples\\\": 200, \\\"k\\\": 12, \\\"wall_time_s\\\": 3517.3}, \\\"conclusion\\\": \\\"success\\\"}, \\\"exp-073-qwen7b-logiqa200-seed456\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"sc_accuracy\\\": 0.7, \\\"sica_accuracy\\\": 0.705, \\\"delta\\\": 0.005, \\\"n_samples\\\": 200}}, \\\"exp-072-llama8b-logiqa200\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"sc_accuracy\\\": 0.62, \\\"sica_accuracy\\\": 0.63, \\\"delta\\\": 0.01, \\\"n_samples\\\": 200}}, \\\"exp-064-deepseek-r1-qwen3-8b-folio204\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"sc_accuracy\\\": 0.8382, \\\"sica_accuracy\\\": 0.8382, \\\"delta\\\": 0, \\\"n_samples\\\": 204, \\\"extraction_rate\\\": 0.3818, \\\"contradiction_rate\\\": 0.0165, \\\"wall_time_min\\\": 355.6}}, \\\"exp-075-contrastive-mistral-folio\\\": {\\\"conclusion\\\": \\\"failed\\\"}, \\\"exp-071-qwen7b-logiqa200-seed123\\\": {\\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"sc_accuracy\\\": 0.69, \\\"sica_accuracy\\\": 0.685, \\\"delta\\\": -0.005, \\\"n_samples\\\": 200}}, \\\"exp-048-llama8b-pw600\\\": {\\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"sc_accuracy\\\": 0.7, \\\"sica_accuracy\\\": 0.648, \\\"delta\\\": -0.052, \\\"n_samples\\\": 600}}, \\\"exp-053-mistral-folio204-seed456\\\": {\\\"conclusion\\\": \\\"killed\\\"}, \\\"exp-052-mistral-folio204-seed123\\\": {\\\"conclusion\\\": \\\"killed\\\"}, \\\"exp-069-llama8b-logiqa200\\\": {\\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"sc_accuracy\\\": 0.61, \\\"sica_accuracy\\\": 0.585, \\\"delta\\\": -0.025, \\\"n_samples\\\": 200}}, \\\"exp-065-qwen7b-pw600\\\": {\\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"sc_accuracy\\\": 0.72, \\\"sica_accuracy\\\": 0.68, \\\"delta\\\": -0.04, \\\"n_samples\\\": 600}}, \\\"exp-062-gemma27b-folio204\\\": {\\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"sc_accuracy\\\": 0.809, \\\"sica_accuracy\\\": 0.804, \\\"delta\\\": -0.005, \\\"n_samples\\\": 204}}, \\\"exp-069-mistral-logiqa200\\\": {\\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"sc_accuracy\\\": 0.495, \\\"sica_accuracy\\\": 0.465, \\\"delta\\\": -0.03, \\\"n_samples\\\": 200}}, \\\"exp-070-qwen7b-logiqa200\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"sc_accuracy\\\": 0.685, \\\"sica_accuracy\\\": 0.71, \\\"delta\\\": 0.025, \\\"n_samples\\\": 200, \\\"sc_correct\\\": 137, \\\"sica_correct\\\": 142, \\\"discordant_b\\\": 1, \\\"discordant_c\\\": 6, \\\"mcnemar_chi2\\\": 2.2857, \\\"mcnemar_p\\\": 0.131, \\\"mcnemar_p_exact\\\": 0.125, \\\"significant_005\\\": false, \\\"cohens_kappa\\\": 0.917, \\\"kappa_interpretation\\\": \\\"almost_perfect\\\"}}, \\\"exp-068-qwen3-logiqa200\\\": {\\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"sc_accuracy\\\": 0.81, \\\"sica_accuracy\\\": 0.81, \\\"delta\\\": 0, \\\"n_samples\\\": 200}}, \\\"exp-064\\\": {\\\"conclusion\\\": \\\"killed\\\"}, \\\"exp-067-mistral-folio-seed789\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"sc_accuracy\\\": 0.5441, \\\"sica_accuracy\\\": 0.5392, \\\"delta_pp\\\": -0.49, \\\"n\\\": 204, \\\"mcnemar_b\\\": 6, \\\"mcnemar_c\\\": 5, \\\"mcnemar_p\\\": 1, \\\"mcnemar_significant\\\": false, \\\"fleiss_kappa_raw\\\": 0.4124, \\\"eff_k\\\": 2.17}}}, \\\"count\\\": 50, \\\"total\\\": 136, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.4604}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"exp-wave3-dir-i-z3-filter\": {\"conclusion\": \"negative\", \"metrics\": {\"n\": 204, \"sc_baseline\": 54.41, \"filtered_sc\": 53.92, \"delta_pp\": -0.49, \"unsat_traces\": 142, \"unsat_rate_pct\": 5.8, \"filter_precision_pct\": 49.12, \"questions_affected\": 7, \"improved\": 3, \"degraded\": 4}}, \"exp-wave3-dir-j-bootstrap\": {\"conclusion\": \"negative\", \"metrics\": {\"n\": 204, \"sc_baseline\": 54.41, \"r1_accuracy\": 56.86, \"r1_delta_pp\": 2.45, \"r1_flips\": 32, \"r1_improved\": 15, \"r1_degraded\": 10, \"r2_accuracy\": 54.41, \"r3_accuracy\": 54.9, \"r4_accuracy\": 54.41, \"r5_accuracy\": 52.45, \"convergence\": \"oscillating, no convergence\"}}, \"exp-cross-model-phase2\": {\"conclusion\": \"negative\", \"metrics\": {\"n\": 204, \"cross_sc_accuracy\": 74.51, \"cross_sica_accuracy\": 74.02, \"delta_pp\": -0.49, \"mcnemar_p\": 1, \"config\": \"Mistral-7B(4) + LLaMA-8B(4) + Qwen-7B(4), K=12\"}}, \"exp-direction-d-cegis\": {\"conclusion\": \"negative\", \"metrics\": {\"n\": 204, \"sc_baseline\": 54.41, \"r1_accuracy\": 57.84, \"r1_delta_pp\": 3.43, \"r2_accuracy\": 57.35, \"r2_delta_pp\": 2.94, \"r3_accuracy\": 57.84, \"r3_delta_pp\": 3.43, \"r1_unsat_traces\": 127, \"r2_unsat_traces\": 48, \"r3_unsat_traces\": 25, \"wall_time_min\": 51, \"extraction_calls\": 2448, \"refinement_calls\": 175}}, \"exp-confirmation-bias\": {\"conclusion\": \"success\", \"metrics\": {\"bias_ratio\": 4.97, \"wrong_constraints_when_sica_errs\": 0.833, \"sica_errors_follow_sc\": 0.94}}, \"exp-cross-model-phase1\": {\"conclusion\": \"success\", \"metrics\": {\"kappa_cross\": 0.422, \"kappa_within\": 0.532, \"eff_k_cross\": 2.11, \"eff_k_within\": 1.52, \"accuracy_gain\": 0}}, \"exp-direction-e-abstention\": {\"conclusion\": \"success\", \"metrics\": {\"auroc\": 0.673, \"coverage_80pct_delta_pp\": 4.4, \"coverage_60pct_delta_pp\": 8.8}}, \"exp-wild6-kappa-aware-sc\": {\"conclusion\": \"negative\", \"metrics\": {\"conditions_tested\": 11, \"delta_pp_all\": 0, \"finding\": \"accuracy monotonically increases with agreement, SC already optimal\"}}, \"exp-wild1-max-unsat\": {\"conclusion\": \"negative\", \"metrics\": {\"min_unsat_delta_pp\": -6.5, \"mean_excluded_constraints\": 1.3}}, \"exp-wild4-process-kappa\": {\"conclusion\": \"negative\", \"metrics\": {\"answer_kappa\": 0.4093, \"process_cosine_mean\": 0.6902, \"pearson_r\": -0.064, \"pearson_p\": 0.36, \"same_answer_diff_process_pct\": 9.3}}, \"exp-direction-a-prove\": {\"conclusion\": \"negative\", \"metrics\": {\"code_gen_rate\": 0.152, \"conclusive_rate\": 0.078, \"conclusive_accuracy\": 0.5, \"prove_fallback_accuracy\": 0.716, \"sc_baseline\": 0.735, \"delta_pp\": -1.9}}, \"exp-direction-b-deepconf\": {\"conclusion\": \"negative\", \"metrics\": {\"filtered_sc_75pct\": 52.9, \"filtered_sica_75pct\": 54.4, \"filtered_sc_50pct\": 52.9, \"logprob_correct\": -0.135, \"logprob_incorrect\": -0.141, \"delta_pp\": 0}}, \"exp-wild3-perturbation\": {\"conclusion\": \"negative\", \"metrics\": {\"original_k4_kappa\": 0.59, \"perturbed_k4_kappa\": 0.696, \"mixed_k8_kappa\": 0.627, \"original_sc_acc\": 80, \"perturbed_sc_acc\": 76.7, \"mixed_sc_acc\": 80}}, \"exp-wild2-ascii\": {\"conclusion\": \"negative\", \"metrics\": {\"group_a_standard_kappa\": 0.3906, \"group_b_fixed_padding_kappa\": 0.4006, \"group_c_variable_padding_kappa\": 0.3638, \"group_a_sc_acc\": 53.92, \"group_b_sc_acc\": 57.84, \"group_c_sc_acc\": 53.92}}, \"exp-084-debate-mistral-logiqa-seed123\": {\"conclusion\": \"negative\", \"metrics\": {\"n\": 200, \"debate_accuracy\": 0.29, \"sc_accuracy\": 0.505, \"delta\": -0.215, \"fallbacks\": 14, \"total_constraints\": 3220, \"wall_time_min\": 226.3}}, \"exp-082-contrastive-mistral-folio-seed123\": {\"metrics\": {\"sc_accuracy\": 0.549, \"contrastive_accuracy\": 0.4951, \"delta\": -0.0539, \"n_samples\": 204, \"wall_time_min\": 206.3, \"degenerate_count\": 35, \"pro_constraints\": 1036, \"con_constraints\": 920}, \"conclusion\": \"negative\"}, \"exp-081-debate-mistral-folio-seed123\": {\"metrics\": {\"sc_accuracy\": 0.5588, \"debate_accuracy\": 0.4069, \"delta\": -0.152, \"n_samples\": 204, \"wall_time_min\": 177.6, \"fallbacks\": 18, \"both_correct\": 56, \"debate_improved\": 27, \"debate_degraded\": 58, \"both_wrong\": 63}, \"conclusion\": \"negative\"}, \"exp-085-contrastive-mistral-logiqa-seed123\": {\"conclusion\": \"negative\", \"metrics\": {\"n\": 200, \"contrastive_accuracy\": 0.535, \"sc_accuracy\": 0.56, \"delta\": -0.025, \"delta_pp\": -2.5, \"contrastive_correct\": 107, \"sc_correct\": 112, \"k\": 12, \"k_contrast\": 3, \"temperature\": 0.7, \"seed\": 123, \"degenerate_count\": 51, \"total_pro_constraints\": 736, \"total_con_constraints\": 1059, \"wall_time_min\": 100.9}}, \"exp-013-constraint-ablation\": {\"conclusion\": \"success\", \"metrics\": {\"maxsat_acc\": 0.4229, \"count_only_acc\": 0.4216, \"random_weight_acc\": \"0.4206±0.0042\", \"sc_acc\": 0.4316, \"delta_maxsat_vs_countonly_pp\": 0.12, \"delta_maxsat_vs_sc_pp\": -0.87, \"agreement_maxsat_countonly\": 0.944, \"n_problems\": 804, \"folio_maxsat\": 0.5931, \"folio_count\": 0.5686, \"folio_sc\": 0.5441, \"pw_maxsat\": 0.365, \"pw_count\": 0.3717, \"pw_sc\": 0.3933}}, \"exp-075b-contrastive-mistral-folio\": {\"conclusion\": \"negative\", \"metrics\": {\"sc_accuracy\": 0.5686, \"contrastive_accuracy\": 0.4755, \"delta\": -0.0931, \"n_samples\": 204, \"wall_time_min\": 193.6, \"degenerate_count\": 41}}, \"exp-080-contrastive-mistral-logiqa200\": {\"conclusion\": \"negative\", \"metrics\": {\"n\": 200, \"contrastive_accuracy\": 0.455, \"sc_accuracy\": 0.5, \"delta\": -0.045, \"k\": 12, \"k_contrast\": 3, \"temperature\": 0.7, \"seed\": 42, \"total_wall_time_s\": 6645.9, \"total_pro_constraints\": 762, \"total_con_constraints\": 1192, \"degenerate_count\": 42}}, \"exp-078-debate-mistral-logiqa200\": {\"conclusion\": \"negative\", \"metrics\": {\"sc_accuracy\": 0.5, \"debate_accuracy\": 0.27, \"delta\": -0.23, \"n_samples\": 200, \"wall_time_min\": 211.5, \"fallbacks\": 16}}, \"exp-078\": {\"conclusion\": \"negative\", \"metrics\": {\"sc_accuracy\": 0.5, \"debate_accuracy\": 0.27, \"delta\": -0.23, \"n_samples\": 200, \"fallbacks\": 16, \"wall_time_min\": 211.5}}, \"exp-083-icg-mistral-logiqa-seed123\": {\"conclusion\": \"negative\", \"metrics\": {\"n\": 200, \"sc_accuracy\": 0.365, \"icg_accuracy\": 0.33, \"delta_pp\": -3.5, \"sc_correct\": 73, \"icg_correct\": 66, \"both_correct\": 62, \"sc_only\": 11, \"icg_only\": 4, \"neither\": 123, \"mean_constraints_generated\": 31.4, \"mean_constraints_unique\": 27.9, \"mean_maxsat_satisfied\": 27.7, \"mean_maxsat_excluded\": 0.2, \"wall_time_s\": 3653.7, \"mean_wall_time_s\": 18.3}}, \"exp-074d-icg-mistral-folio-seed456\": {\"conclusion\": \"negative\", \"metrics\": {\"sc_accuracy\": 0.5588, \"icg_accuracy\": 0.549, \"delta\": -0.0098, \"n_samples\": 204, \"wall_time_min\": 57.3, \"three_seed_mean_sc\": 0.5572, \"three_seed_mean_icg\": 0.5523, \"three_seed_mean_delta\": -0.0049, \"three_seed_std_delta\": 0.0177, \"three_seed_details\": {\"seed_42\": {\"sc\": 0.5392, \"icg\": 0.5196, \"delta\": -0.0196}, \"seed_123\": {\"sc\": 0.5735, \"icg\": 0.5882, \"delta\": 0.0147}, \"seed_456\": {\"sc\": 0.5588, \"icg\": 0.549, \"delta\": -0.0098}}}}, \"exp-077-kappa-generalization\": {\"conclusion\": \"negative\", \"metrics\": {\"sc_kappa\": 0.4384, \"sc_eff_k\": 2.02, \"sc_nominal_k\": 10, \"debate_kappa\": 0.1549, \"debate_eff_k\": 4.44, \"debate_nominal_k\": 12, \"diverse_prompt_kappa\": 0.403, \"diverse_prompt_eff_k\": 2.21, \"diverse_prompt_nominal_k\": 12, \"n_samples\": 204}}, \"exp-077\": {\"metrics\": {\"sc_kappa\": 0.4384, \"sc_eff_k\": 2.02, \"debate_kappa\": 0.1549, \"debate_eff_k\": 4.44, \"diverse_prompt_kappa\": 0.403, \"diverse_prompt_eff_k\": 2.21, \"n_questions\": 204, \"all_kappa_gt_04\": false, \"wall_time_min\": 184.9}, \"conclusion\": \"negative\"}, \"exp-075b\": {\"conclusion\": \"negative\", \"metrics\": {\"sc_accuracy\": 0.5686, \"contrastive_accuracy\": 0.4755, \"delta\": -0.0931, \"n_samples\": 204, \"degenerate\": 41, \"wall_time_min\": 193.6}}, \"exp-074c-icg-mistral-folio-seed123\": {\"metrics\": {\"sc_accuracy\": 0.5735, \"icg_accuracy\": 0.5882, \"delta\": 0.0147, \"n_samples\": 204, \"wall_time_min\": 56.5}, \"conclusion\": \"negative\"}, \"exp-076-debate-mistral-folio\": {\"conclusion\": \"negative\", \"metrics\": {\"sc_accuracy\": 0.5686, \"debate_accuracy\": 0.3824, \"delta\": -0.1863, \"n_samples\": 204, \"wall_time_min\": 186.4, \"fallbacks\": 10, \"total_debate_constraints\": 3677}}, \"exp-079-icg-mistral-logiqa200\": {\"conclusion\": \"negative\", \"metrics\": {\"sc_accuracy\": 0.475, \"icg_accuracy\": 0.47, \"delta\": -0.005, \"n_samples\": 200, \"wall_time_min\": 54.3}}, \"exp-072b-llama8b-logiqa200\": {\"conclusion\": \"negative\", \"metrics\": {\"sc_accuracy\": 0.595, \"sica_accuracy\": 0.585, \"delta\": -0.01, \"n_samples\": 200, \"k\": 12, \"wall_time_s\": 7310.5, \"extraction_success\": 2292, \"extraction_fail_json_parse\": 108}}, \"exp-074-icg-mistral-folio\": {\"metrics\": {\"sc_accuracy\": 0.5392, \"icg_accuracy\": 0.5196, \"delta\": -0.0196, \"n_samples\": 204, \"k\": 12, \"k_icg\": 10, \"wall_time_s\": 3368}, \"conclusion\": \"negative\"}, \"exp-073b-qwen7b-logiqa200-seed456\": {\"metrics\": {\"sc_accuracy\": 0.695, \"sica_accuracy\": 0.715, \"delta\": 0.02, \"n_samples\": 200, \"k\": 12, \"wall_time_s\": 3517.3}, \"conclusion\": \"success\"}, \"exp-073-qwen7b-logiqa200-seed456\": {\"conclusion\": \"success\", \"metrics\": {\"sc_accuracy\": 0.7, \"sica_accuracy\": 0.705, \"delta\": 0.005, \"n_samples\": 200}}, \"exp-072-llama8b-logiqa200\": {\"conclusion\": \"success\", \"metrics\": {\"sc_accuracy\": 0.62, \"sica_accuracy\": 0.63, \"delta\": 0.01, \"n_samples\": 200}}, \"exp-064-deepseek-r1-qwen3-8b-folio204\": {\"conclusion\": \"success\", \"metrics\": {\"sc_accuracy\": 0.8382, \"sica_accuracy\": 0.8382, \"delta\": 0, \"n_samples\": 204, \"extraction_rate\": 0.3818, \"contradiction_rate\": 0.0165, \"wall_time_min\": 355.6}}, \"exp-075-contrastive-mistral-folio\": {\"conclusion\": \"failed\"}, \"exp-071-qwen7b-logiqa200-seed123\": {\"conclusion\": \"negative\", \"metrics\": {\"sc_accuracy\": 0.69, \"sica_accuracy\": 0.685, \"delta\": -0.005, \"n_samples\": 200}}, \"exp-048-llama8b-pw600\": {\"conclusion\": \"negative\", \"metrics\": {\"sc_accuracy\": 0.7, \"sica_accuracy\": 0.648, \"delta\": -0.052, \"n_samples\": 600}}, \"exp-053-mistral-folio204-seed456\": {\"conclusion\": \"killed\"}, \"exp-052-mistral-folio204-seed123\": {\"conclusion\": \"killed\"}, \"exp-069-llama8b-logiqa200\": {\"conclusion\": \"negative\", \"metrics\": {\"sc_accuracy\": 0.61, \"sica_accuracy\": 0.585, \"delta\": -0.025, \"n_samples\": 200}}, \"exp-065-qwen7b-pw600\": {\"conclusion\": \"negative\", \"metrics\": {\"sc_accuracy\": 0.72, \"sica_accuracy\": 0.68, \"delta\": -0.04, \"n_samples\": 600}}, \"exp-062-gemma27b-folio204\": {\"conclusion\": \"negative\", \"metrics\": {\"sc_accuracy\": 0.809, \"sica_accuracy\": 0.804, \"delta\": -0.005, \"n_samples\": 204}}, \"exp-069-mistral-logiqa200\": {\"conclusion\": \"negative\", \"metrics\": {\"sc_accuracy\": 0.495, \"sica_accuracy\": 0.465, \"delta\": -0.03, \"n_samples\": 200}}, \"exp-070-qwen7b-logiqa200\": {\"conclusion\": \"success\", \"metrics\": {\"sc_accuracy\": 0.685, \"sica_accuracy\": 0.71, \"delta\": 0.025, \"n_samples\": 200, \"sc_correct\": 137, \"sica_correct\": 142, \"discordant_b\": 1, \"discordant_c\": 6, \"mcnemar_chi2\": 2.2857, \"mcnemar_p\": 0.131, \"mcnemar_p_exact\": 0.125, \"significant_005\": false, \"cohens_kappa\": 0.917, \"kappa_interpretation\": \"almost_perfect\"}}, \"exp-068-qwen3-logiqa200\": {\"conclusion\": \"negative\", \"metrics\": {\"sc_accuracy\": 0.81, \"sica_accuracy\": 0.81, \"delta\": 0, \"n_samples\": 200}}, \"exp-064\": {\"conclusion\": \"killed\"}, \"exp-067-mistral-folio-seed789\": {\"conclusion\": \"success\", \"metrics\": {\"sc_accuracy\": 0.5441, \"sica_accuracy\": 0.5392, \"delta_pp\": -0.49, \"n\": 204, \"mcnemar_b\": 6, \"mcnemar_c\": 5, \"mcnemar_p\": 1, \"mcnemar_significant\": false, \"fleiss_kappa_raw\": 0.4124, \"eff_k\": 2.17}}}, \"count\": 50, \"total\": 136, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4604}}"
    }
  },
  "sourceToolAssistantUUID": "296867dc-00d4-4cc1-9c77-f8b50c23298e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora"
}
```

</details>

---


### Runtime record

_source line 8884_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[服务器重启后首条消息] 当前日期: 2026-05-20。服务器刚重启，项目状态可能已更新。不要依赖对话历史中的状态信息，以 registry 当前值为准。  **用户消息：** [Director 指令] ## 写作任务：EMNLP 2026 ARR May 25 — Full Draft 更新  **DDL**: May 25, 2026（5 天） **模式**: Full Draft 更新…",
  "leafUuid": "d268b20c-2d8b-4b16-be28-5b4c387a6d0e",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1"
}
```

---


### Runtime record

_source line 8885_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise paper results with oracle FOLIO constraint experiments",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1"
}
```

---


### Assistant

_source line 8886 · 2026-05-20T09:40:23.585Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have the full picture. Let me also check the new experiment data specifically for confirmation bias and process-κ to make sure I have exact numbers.

Key new experiments from registry:
- `exp-confirmation-bias`: bias_ratio=4.97, wrong_constraints_when_sica_errs=0.833, sica_errors_follow_sc=0.94
- `exp-wild4-process-kappa`: answer_kappa=0.4093, process_cosine_mean=0.6902, pearson_r=-0.064, pearson_p=0.36, same_answer_diff_process_pct=9.3


- `exp-direction-a-prove`: code_gen_rate=0.152, conclusive_accuracy=0.5, delta_pp=-1.9
- `exp-direction-d-cegis`: r1_accuracy=57.84, r1_delta_pp=3.43, r2→r3 oscillating
- `exp-direction-b-deepconf`: logprob_correct=-0.135, logprob_incorrect=-0.141, delta_pp=0
- `exp-wild3-perturbation`: perturbed kappa=0.696 (worse, higher), delta negative
- `exp-wild1-max-unsat`: min_unsat_delta_pp=-6.5
- `exp-wild6-kappa-aware-sc`: 11/11 Δ=0
- `exp-wave3-dir-i-z3-filter`: delta_pp=-0.49
- `exp-wave3-dir-j-bootstrap`: oscillating, no convergence
- `exp-cross-model-phase1`: kappa_cross=0.422, kappa_within=0.532, accuracy_gain=0
- `exp-cross-model-phase2`: delta_pp=-0.49
- `exp-direction-e-abstention`: AUROC=0.673, +4.4pp@80%cov (success as diagnostic)
- Various debate/contrastive/ICG seed variants

Now I need to understand the D085 framing narrative

. The core story is shifting: I've expanded the claims from five to eight, with the new ones focusing on comprehensive method failures and symbolic confirmation bias as the underlying mechanism. All 25+ interventions are failing, not just the initial batch, and this pattern holds across three different model families. I'm introducing Process-κ as a new diagnostic metric and updating the headline to reflect this universality. For the contributions, I'm keeping the first four mostly intact but adding universality across architectures, then introducing the three new claims about method failures, confirmation bias, and the process metric itself.

Writing config... I need to figure out the page layout strategically since eight pages is tight for eight major contributions. The current structure takes up about 6.5 pages, so I have limited room for the new confirmation bias analysis, process-κ metric, and expanded remediation methods. I'll need to push most of the new tables and figures to the appendix, keeping only the most critical visualizations in the main text to support the core narrative about confirmation bias as the root cause.

For the reorganized paper, I'm thinking: compress Related Work slightly to make room, integrate Process-κ into the Methods section, then restructure Analysis to weave together efficiency-κ, confirmation bias findings, and the remediation strategies. This keeps the focus tight while still covering all the contributions. The Discussion becomes more of a synthesis around confirmation bias as the unifying explanation rather than a detailed breakdown.

Now I'm mapping out what actually needs to go in the main text versus what can be relegated to appendix given the 8-page constraint. The core narrative is: symbolic confirmation bias explains why 25+ methods plateau, Process-κ quantifies the mechanism, and the independence-accuracy trade-off shows why self-extraction under the same model can't escape this. I should draft the writing plan to be explicit about page budgets and what evidence goes where. Let me think about the new sections:

**Method section** additions:
- Process-κ metric definition (small — 100 words)
- Confirmation bias analysis framework (small — 100 words)

**Analysis section** restructure:
- §5.1 Condorcet Effective-K (keep, ~300 words)
- §5.2 Symbolic Confirmation Bias (NEW — core analysis, ~250 words)
  - Bias ratio 4.97× on incorrect problems
  - 97.6% SICA errors overlap SC
  - Causal chain explanation
- §5.3 Process-κ (NEW — ~200 words)
  - CoT cosine 0.69 >> answer-κ 0.41
  - r=-0.06 (uncorrelated)
  - 9.3% convergent

Now I'm facing a tight page budget. Adding confirmation bias and process-κ sections requires about 0.5 pages, but I only have 1.5 pages for analysis currently. I need to cut the same amount elsewhere. I could compress the replication section from 250 to 150 words, trim the discussion by 0.15 pages, move the K/T sensitivity analysis to the appendix to save 0.2 pages, or condense the extraction taxonomy further. I need to reconcile what the Director asked for with what actually exists. The .tex files are already there, so technically this is Patch mode, but the Director explicitly requested "Full Draft 更新" and a writing_plan.yaml. I think they want me to regenerate the plan to guide this extensive narrative restructuring before I start executing the changes.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d268b20c-2d8b-4b16-be28-5b4c387a6d0e",
  "isSidechain": false,
  "requestId": "req_011CbDbfoTYshpriFTEyNB9i",
  "type": "assistant",
  "uuid": "04ce27e7-6195-4a23-b858-53b169a1e4aa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PWwvU2Vn3WSu2QKT4oJj6W",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5561,
      "cache_read_input_tokens": 82465,
      "output_tokens": 2605,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5561,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2605,
          "cache_read_input_tokens": 82465,
          "cache_creation_input_tokens": 5561,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5561
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

_source line 8887 · 2026-05-20T09:40:23.610Z_

Now let me read the paper-plan skill before generating the writing plan.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "04ce27e7-6195-4a23-b858-53b169a1e4aa",
  "isSidechain": false,
  "requestId": "req_011CbDbfoTYshpriFTEyNB9i",
  "type": "assistant",
  "uuid": "a85a50d7-0984-43a0-a64e-f0fd3527df1f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PWwvU2Vn3WSu2QKT4oJj6W",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5561,
      "cache_read_input_tokens": 82465,
      "output_tokens": 2605,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5561,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2605,
          "cache_read_input_tokens": 82465,
          "cache_creation_input_tokens": 5561,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5561
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

_source line 8888 · 2026-05-20T09:40:23.615Z_

<details open><summary>🔧 Tool call — Read · `toolu_0114U8wC7Qv8RCsLW24u3ug3`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/skills/paper-plan.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a85a50d7-0984-43a0-a64e-f0fd3527df1f",
  "isSidechain": false,
  "requestId": "req_011CbDbfoTYshpriFTEyNB9i",
  "type": "assistant",
  "uuid": "e8dd23a0-2a7a-4a13-8fc8-988917418e67",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PWwvU2Vn3WSu2QKT4oJj6W",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5561,
      "cache_read_input_tokens": 82465,
      "output_tokens": 2605,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5561,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2605,
          "cache_read_input_tokens": 82465,
          "cache_creation_input_tokens": 5561,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5561
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

_source line 8889 · 2026-05-20T09:40:23.631Z_

<details><summary>↩ Tool result · reported error · `toolu_0114U8wC7Qv8RCsLW24u3ug3`</summary>

```text
File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e8dd23a0-2a7a-4a13-8fc8-988917418e67",
  "isSidechain": false,
  "promptId": "3f50ba00-7d30-45ec-b450-7010d531c858",
  "type": "user",
  "uuid": "d94224d4-5cd4-4570-990d-ab33302711c2",
  "toolUseResult": "Error: File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69.",
  "sourceToolAssistantUUID": "e8dd23a0-2a7a-4a13-8fc8-988917418e67",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora"
}
```

</details>

---


### Tool call

_source line 8890 · 2026-05-20T09:40:26.427Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01TfqhB9bxV8cUWpU62JLLzt`</summary>

```json
{
  "pattern": "**/paper-plan.skill.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d94224d4-5cd4-4570-990d-ab33302711c2",
  "isSidechain": false,
  "requestId": "req_011CbDbkSY6ZwUuLqFHCEQ5T",
  "type": "assistant",
  "uuid": "23d3bea1-1a3c-448d-a604-e14b6e64a651",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QxazrDazZGfkLKJf4JGUNv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2674,
      "cache_read_input_tokens": 88026,
      "output_tokens": 95,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2674,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 95,
          "cache_read_input_tokens": 88026,
          "cache_creation_input_tokens": 2674,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2674
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
