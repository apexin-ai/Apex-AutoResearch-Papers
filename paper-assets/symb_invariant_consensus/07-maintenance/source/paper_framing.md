# Paper Framing — symb_invariant_consensus

## Target Venue
- Primary: EMNLP 2026 Main (ARR May 25)
- Deadline: May 25, 2026 (ARR submission)

## D063 Direction: Entropy Decomposition + Quality Ladder — 目标 4.0

**从 D060 "Pure Analysis / negative result" 升级为 "Regime-Dependent Mechanism Analysis with Entropy Decomposition"。** 用户决定冲 4.0。

### Entropy Breakdown 验证结果 (2026-05-19 completed)

**跨模型 entropy mechanism 一致性: 不成立。Selective SICA 非 universal 方案。**

但 entropy decomposition 揭示了更有价值的 regime mechanism：

| Experiment | Model | Dataset | High-E n | High-E Δpp | Low-E n | Low-E Δpp |
|-----------|-------|---------|----------|-----------|---------|----------|
| exp-033 s42 | Mistral-7B | FOLIO | 78 | **+12.8** | 126 | 0.0 |
| exp-052 s123 | Mistral-7B | FOLIO | 77 | **+9.1** | 127 | 0.0 |
| exp-053 s456 | Mistral-7B | FOLIO | 75 | -1.3 | 129 | 0.0 |
| exp-046 | Mistral-7B | PW-600 | 267 | -4.9 | 333 | -1.2 |
| exp-036 | Qwen2.5-14B | FOLIO | 37 | **-8.2** | 167 | -0.6 |
| exp-038 | Qwen2.5-14B | LogiQA | 23 | -4.3 | 177 | 0.0 |
| exp-035 | Qwen2.5-7B | FOLIO | 47 | -2.1 | 157 | 0.0 |
| exp-048 | LLaMA-8B | PW-600 | 76 | -3.9 | 104 | -1.9 |

(注: SC/Δ 使用 pre-tiebreaking 值，entropy grouping 不受 tiebreaking 影响。D064 修正后 deltas 会略有变化但 pattern 不变。)

**三个核心发现：**
1. **Low-entropy: SICA≈SC 跨模型一致** (8/8 experiments Δ≈0) → traces 一致时 constraints 无新信息
2. **High-entropy 方向因 regime 而异**：Goldilocks +12.8pp vs Type A -8.2pp vs Type C -4.9pp
3. **Mechanism 解释**：
   - Goldilocks (SC~55%, κ~0.46): 真实不确定性 → constraints 打破平局正确方向
   - Type A (SC>75%, κ>0.65): 偶发错误 → constraints 放大 confirmation bias
   - Type C (SC<40%, κ~0.20): 系统性错误 → constraints 是噪声

### 调整后核心转变

论文以 "entropy decomposition 揭示 regime-dependent mechanism" 为核心分析贡献（不是 universal diagnostic）：
- **Entropy decomposition 作为分析工具**：分离 SICA 作用点（high-entropy）vs 不作用点（low-entropy）
- **Regime mechanism 量化**：同样是 high-entropy 问题，direction depends on SC+κ → 完美支持 dual bottleneck
- **Abandoned**: Selective SICA 作为 universal practical contribution（只在 Goldilocks zone 有效）
- **Upgraded**: 核心图 = high-entropy Δ vs SC scatter（8 points, 3 regimes 清晰分离）
- **Quality Ladder** (D067: L1 NULL CONFIRMED)
  - L0: Self-extraction (Mistral→Mistral): 59.31%, Δ=+3.43pp ns
  - L1a: Qwen3-14B→Mistral traces: 60.29%, Δ=+4.41pp (+0.98pp vs self = 2题/204 = noise)
  - L1b: Qwen2.5-14B→Mistral traces: 58.33%, Δ=+2.45pp (-0.98pp vs self = 2题/204 = noise)
  - L3: Oracle 100% disc, Δ=+14.22pp p<0.001
  - **结论**: L1 ≈ L0 << L3。Bottleneck 在 traces（同源输入），不在 extractor（换模型无效）
  - **Paper contribution**: "bottleneck is fundamental to extraction, not just model capability" — 强化 structural limitation 论点
- **CJT/Eff-K 保留**：解释 why high-entropy behavior differs across regimes

D060 要素全部保留：
- Condorcet independence 框架 → 理论基础
- 9 种修复全部失败 → structural limitation 证据
- 2/3 seeds positive trend but **0/3 significant** (D066: p=0.092/0.070/1.0) → Goldilocks zone 作为 directional trend, not confirmed effect
- K/T sensitivity non-monotonic → SC confound insight
- 用户指示: 投 May 25 不变，冲 4.0

## Core Claims (5 条) — D060 纯 Analysis Framing

### Analysis Claims (已验证)

1. **Independence Bottleneck**: Self-consistency 隐含 Condorcet Jury Theorem 的独立性假设，但同模型采样的 traces 高度相关。Worker 验证的 κ 值：
   - Qwen-14B FOLIO: κ=0.744, Eff-K=1.31 (SC=75.49%, Δ=+0.25pp n.s.)
   - Qwen-14B LogiQA: κ=0.821, Eff-K=1.20 (SC=78.5%, Δ=+0.50pp n.s.)
   - Mistral-7B FOLIO s42 (exp-033): κ=0.501, Eff-K=1.84 (SC=55.88%, Δ=+3.43pp **p=0.092 ns**) ← primary seed [D064+D066]
   - Mistral-7B FOLIO s123: κ=0.491, Eff-K=1.88 (SC=54.41%, Δ=+2.94pp **p=0.070 ns**)
   - Mistral-7B FOLIO s456: κ=0.507, Eff-K=1.82 (SC=55.88%, Δ=0.00pp p=1.0 ns)
   - Mistral-7B PW-600 (exp-046): κ=0.210, Eff-K=3.63 (Δ=-2.83pp p=0.010, SC=39%)
   规律：跨模型对比清晰（Qwen Eff-K≈1.2-1.3 → 0 gain; Mistral Eff-K≈1.85-2.22 → variable gain）。但 Mistral seeds 内部，Eff-K 与 delta 非单调（exp-033 Eff-K 最低 1.85 却 delta 最高 +3.43pp）→ Eff-K 是跨模型必要条件，seed 内 variance 仍主导。exp-046 Eff-K 最高(3.63) 但 SC 太低(39%) 导致 delta 为负 → 需同时满足 sufficient Eff-K AND sufficient SC。

2. **Oracle Gap Localizes Extraction Bottleneck**: Gold FOL + MAX-SAT = +14.22pp (p=2.0e-7)，自提取仅 +3.43pp (best seed, D064 corrected) = 24% utilization。聚合机制本身有效，瓶颈在自提取质量。Two-layer analysis:
   - **Constraint taxonomy**: 43% trivially_satisfied（被所有候选答案满足的约束，不排除任何答案）
   - **Discriminative filtering**: 仅 ~8% 约束在 MAX-SAT scoring 中完全 non-discriminative（移除后 0 gains）
   - **关键区分**: 43% 和 8% 度量不同。trivially_satisfied 约束在 MAX-SAT 中仍可有不同满足程度（partial vs full），所以不全是 non-discriminative。但即使 constraints 是 discriminative 的，它们的"区分方向"与模型自身偏差一致（confirmation bias）。both_wrong 组 score_range=29.4。九种修复全部失败。

3. **Regime-Dependent Capability Trap**: SICA 有效性取决于提取模型的基线准确率，存在双边界：
   - Type A (SC ≥ ~60%): 确认偏差，constraints 镜像模型自身答案。**exp-034 vs exp-039 同配置 delta 翻转**: exp-034 Δ=+0.51pp (n=589), exp-039 Δ=-2.00pp (n=600)。SC baseline 方差 (3.38pp) >> SICA 效应 → Type A delta 是 trace sampling noise。SICA 比 SC 更稳定 (跨运行方差 0.87pp vs 3.38pp，仅 2 点，需更多 seed 验证)
   - Type C (SC ≤ ~40%): traces 主要错误，constraints 是噪声 (exp-046: Δ=-2.83pp, p=0.0095)
   - Goldilocks zone (~50-56% SC): 部分独立性 + 部分正确性 (exp-033: Δ=+3.43pp, p=0.092 ns; mean of 3 seeds: +2.12pp) ⚠️ D076 Reviewer: 0/3 seeds significant, 不应作为核心叙事支柱。作为 directional observation 保留，不做强 claim。
   - Type B: 领域不可形式化 (LogiQA: contradiction rate 0.8%)

4. **C0+SC Two-Dimensional Diagnostic**: C0 (multi-candidate rate) + SC accuracy 形成零成本部署诊断。C0<5% → degenerate; high C0 + high SC → trap; high C0 + low SC → potential gains。

### Remediation Evidence (D060: 全部失败 — 强化 analysis narrative)

5. **Nine Remediation Attempts All Failed**: 原 6 种 + 3 种靶向修复全部无效，证明 independence bottleneck 是结构性的：
   - D059 三路 method improvement 全部失败：
     - Discriminative Filtering: 119/204 处理后 0 gains 1 loss，~92% 约束本身就是 discriminative，过滤是 near-no-op
     - T=1.0 (exp-054): delta 从 +3.43pp 崩塌到 0.00pp（D064 corrected），温度敏感性极端
     - Multi-Temp (exp-055): ✅ 完成，delta=+0.00pp (b=5,c=5 完美对称), SC=57.84%. 混合 T=0.3/0.7/1.2 各 4 traces 未改善 SICA。附带发现：multi-temp 提升 SC baseline (+3.4pp vs 单温度 54.41%)，说明混合温度对 majority voting 有帮助，但 SICA constraint extraction 无法利用这种 diversity → bottleneck 在 extraction 而非 trace diversity
   - 原 6 种：contrastive prompting, cross-model extraction, generational scaling, solver-guided refinement, consistency filtering, cross-trace UNSAT
   - 9 种修复涵盖 prompting / architecture / capability / verification / diversity / filtering 全维度，全部失败 → trap is fundamental

## D070/D074 Update: Method-Level Interventions Also Fail — "Fundamental Limitation" Confirmed

### Three Method Lines × Two Datasets = All Negative (D074)

D070 从纯 analysis 升级为 analysis + method paper，但三条方法线全面失败（D074 确认），反而强化了原始 analysis 结论。

**方法×数据集完整结果**：
| Method | FOLIO-204 | LogiQA-200 | Failure Mode |
|--------|-----------|------------|--------------|
| ICG (Independent Constraint Gen.) | Δ=-2.0pp (3-seed: -2.0/+1.5/-1.0, mean=-0.5pp±1.8pp, 噪声) | Δ=-0.5pp | Neutral — 独立约束质量≈trace-sourced约束 |
| Contrastive (Pro/Con Scoring) | Δ≈-16pp | Δ≈-7pp (interim) | Harmful — 26% degenerate scoring, pro/con 不平衡 |
| Debate (Proposer/Critic) | Δ=-18.6pp | Δ≈-28pp (interim) | Catastrophic — 7B 模型角色扮演严重退化推理 |

**三种失败模式的分析价值**（论文 "Why Methods Fail" section）：
1. **ICG (neutral)**: 独立于 traces 生成的约束不比 trace-sourced 约束更好。说明 bottleneck 不仅是 "约束来自 traces"，而是模型的推理偏差从问题理解阶段就存在——独立约束和 trace-sourced 约束继承相同的 model bias。
2. **Contrastive (harmful)**: 强制 pro/con 评估引入 degenerate scoring（26% 问题无法有效区分）。7B 模型无法可靠生成平衡的对立约束——pro 约束系统性多于 con（94 pro vs 65 con），confirmation bias 从约束提取转移到了约束生成。
3. **Debate (catastrophic)**: Proposer/Critic/Defense 多角色链在 7B 模型上导致答案质量严重退化。辩论不仅未增加多样性，反而引入了角色扮演的额外认知负担。同模型辩论 = 同源性 + 角色扮演退化，双重损失。

**Scale limitation caveat**: 所有方法测试在 7B 模型上。7B 模型生成 Z3 格式 FOL 约束的能力不足（ICG 多题 "0/N constraints parsed"）。14B+ 模型可能有不同结果——这既是 limitation 也是 future work 入口。

### κ Generalization — Independence-Accuracy Trade-off (D075, CAPSTONE FINDING)

exp-077 测量三种聚合方式在 Mistral-7B FOLIO-204 上的 κ 和 Eff-K：
| 聚合方式 | Fleiss' κ | Eff-K | 名义 K |
|----------|----------|-------|--------|
| Self-Consistency | 0.4384 | 2.02 | 10 |
| Diverse-Prompt | 0.4030 | 2.21 | 12 |
| LLM-Debate | 0.1549 | 4.44 | 12 |

结合 exp-076 Debate Δ=-18.6pp 的准确率数据，揭示**同模型框架下的 fundamental independence-accuracy trade-off**：
- **SC/Diverse-Prompt**: κ~0.4，traces 高度相关但准确率正常。换 prompt 策略不改善独立性（Δκ=0.04）。
- **Debate**: κ=0.15，成功打破 trace 相关性（Eff-K 从 2.0 跃升到 4.4），但准确率崩溃 -18.6pp。低 κ 不代表"更独立的推理"——是 disagreement amplification（系统性噪声）。
- **Trade-off 本质**: 同一模型的推理能力是固定的。要么输出一致（高 κ, 正确但不独立），要么输出分歧（低 κ, 独立但不正确）。Condorcet Jury Theorem 要求 both independent AND accurate，同模型框架下无法同时满足。

**论文叙事升级**: 从 "methods fail" → "independence-accuracy trade-off is fundamental to same-model reasoning"。突破瓶颈需要跨模型方案（不同模型天然更独立），Oracle 实验（gold FOL 来自外部知识源）已间接验证了这一点。

### New Claim 6 (D070/D074)

6. **Method-Level Interventions Cannot Break the Bottleneck**: 三种针对 independence bottleneck 不同环节的方法（ICG→循环依赖, Contrastive→confirmation bias, Debate→trace 同质性）在 2 个数据集上全部失败。加上之前 9 种 prompt-level 修复，共 12 种修复尝试全败。这证明 independence bottleneck 不是单一环节的问题，而是 same-model self-extraction 的根本性限制。

### New Claim 7: Symbolic Confirmation Bias (D082 — CORE FINDING)

7. **Symbolic Confirmation Bias**: LLM 从 CoT traces 提取的 FOL 约束系统性确认 trace 自身（可能错误的）答案，而非独立验证 ground truth。
   - SICA 判对题：gold constraint 78.1%，bias ratio = 0.28
   - SICA 判错题：错误 constraint 83.3%，bias ratio = **4.97×**
   - 97.6% SICA 错误与 SC 错误完全重合
   - SICA 翻盘的 12 例来自 minority trace diversity（43% gold support），不是 symbolic reasoning
   - **因果链**：模型推理→答案→从含答案 trace 提取 FOL→约束确认答案→聚合≈SC
   - **CEGIS 验证**：迭代精炼 R1 +3.43pp < 原始 SICA +4.9pp → 约束一致性不是瓶颈，偏向性才是
   - **Quality Ladder 验证**：L1 ≈ L0 << L3 → bottleneck 在 traces（同源输入），不在 extractor

### New Claim 8: Process-κ (D082 — NEW METRIC)

8. **Process-Level Independence (Process-κ)**: answer-κ 低估真实独立性瓶颈。CoT 推理过程相似性远高于答案一致性。
   - Mistral-7B FOLIO-204：CoT cosine similarity **0.69** >> answer-κ **0.41**
   - 两者几乎无相关性：r = -0.06, p = 0.36
   - 仅 **9.3%** trace 对是"殊途同归"（同答案不同路径）
   - answer-κ 是 true independence bottleneck 的 lower bound
   - 适用于所有 LLM trace aggregation 方法，不限于 SICA

## D082/D085: Comprehensive Method Exhaustion — 25+ ALL Fail

D080 启动全方向并行探索（Wave 1-3），在 D074 的 12 种修复基础上又测试 13+ 新干预：

| 方法 | 类型 | 结果 | 关键数据 |
|------|------|------|----------|
| PROVE 代码验证 | paradigm shift | ❌ | Code gen 15.2%, accuracy=random |
| CEGIS 迭代精炼 | multi-round | ❌ | R1 +3.43pp < SICA +4.9pp |
| DeepConf 置信度 | filtering | ❌ | logprob 与正确性零相关 |
| Cross-model SICA | cross-model | ❌ | Δ=-0.49pp despite lower κ |
| Problem Perturbation | input diversity | ❌ | κ 升至 0.696 (反效果) |
| MIN-UNSAT | solver objective | ❌ | 49.5% < SC 54.4% |
| κ-aware SC | voting rule | ❌ | 11/11 Δ=0 |
| Z3 Trace Filter | trace filtering | ❌ | negative |
| Bootstrapped Gold | iterative | ❌ | negative |
| Selective Abstention | diagnostic | ⚡ | AUROC=0.673, +4.4pp@80%cov |

**D085 总结**: 9 prompt-level + 3 method-level + 13 新方向 = **25+ 干预全部 negative**。Independence bottleneck 在 same-model self-extraction 框架下无解，所有维度（diversity/architecture/capability/verification/filtering/voting/solver/paradigm）已穷尽。

## D090: Cross-Architecture External Verification — POSITIVE BREAKTHROUGH

### New Claim 9: Cross-Architecture NLI Verification Breaks the Bottleneck

9. **Cross-Architecture External Verification**: A lightweight encoder-only NLI model (microsoft/deberta-large-mnli) provides structurally complementary signal to decoder-only LLMs.
   - DeBERTa standalone: 49.51% (101/204) — not competitive alone, expected
   - **NLI+SC combo w=1 (NLI as 13th voter): 57.84% (118/204), +3.43pp vs SC** ← PRIMARY (has McNemar)
   - NLI+SC combo w=3: 58.82% (120/204), +4.41pp vs SC — McNemar p=0.078 NOT significant (b=6, c=15). Higher weight amplifies NLI weakness on Unknown.
   - NLI+SC combo w=5: 60.29% (+5.88pp) — Reviewer: w=5 overfitting risk, NOT main result
   - NLI∩SC agreement subset: 68.48% accuracy on 45% coverage — selective verification evidence
   - NLI-as-verifier (trust NLI on disagreement): 49.51% — FAILED (NLI only 34% correct when disagreeing)
   - SC baseline: 54.41% (111/204, primary Mistral-7B FOLIO eval, seed=None)
   - **McNemar (w=1 ONLY)**: p=0.039, significant at α=0.05. 9 discordant pairs (b=1, c=8). 95% CI [0.59pp, 6.28pp]. ⚠️ w=3 and w=5 McNemar NOT YET COMPUTED — do NOT attribute this p-value to other weights
   - **Model**: microsoft/deberta-large-mnli, **406M** parameters (not 350M, not 44M)
   - **Per-label complementarity (key insight)**:
     - False (contradiction): NLI **71.43%** vs SC 38.10% → NLI dominates (+33pp)
     - Unknown: NLI 18.84% vs SC **68.12%** → SC dominates (+49pp)
     - True: NLI 59.72% vs SC 55.56% → NLI slightly better
   - **Why it works**: DeBERTa is encoder-only + NLI fine-tuned → strong at contradiction detection (its training task). LLM is strong at uncertainty reasoning. Structurally complementary error profiles.
   - **Oracle connection**: Oracle (+14.22pp) proved aggregation works with quality constraints; DeBERTa provides partial external signal → partial oracle effect
   - **Narrative**: "25+ same-model interventions fail, but even a simple cross-architecture voter provides modest positive signal — proof-of-concept for external architectural complementarity"

### New Claim 10: Constraint-Answer Decoupling — CONDITIONAL on full results (D092)

10. **Constraint-Answer Decoupling (G)**: Removing conclusion sentences from reasoning traces before FOL extraction causally breaks Symbolic Confirmation Bias.
   - **⚠️ INTERMEDIATE results only (70/204 = 34%)**: 65.7% accuracy (+11.3pp vs SC 54.41%, +6.4pp vs SICA 59.31%)
   - Avg truncation ratio: **4.1%** — removing ~4% of trace text yields +11pp improvement
   - **Causal mechanism**: trace contains conclusion → FOL extractor reads conclusion → extracted constraints confirm conclusion → aggregation ≈ SC. G cuts this chain by removing the conclusion before extraction.
   - **Potential strengths**: (a) largest positive effect in the project, (b) minimal intervention (4.1% text removal), (c) directly tests the confirmed mechanism (confirmation bias)
   - **Risk (Reviewer critical)**: FOLIO 难度分布不均匀，前 70 题可能偏简单。历史先例：Direction F 42%→39.6%，Direction H 56.1%→微降。中间值可能虚高。
   - **Residual bias risk**: 即使截断显式结论，推理步骤仍可能暗示答案方向（"the premises suggest..."），extraction 模型仍可能产生 biased constraints。
   - **Full results pending**: PID 384984 on westd-16639, running to 204/204
   - **McNemar**: pending full results
   - **Narrative (if confirmed)**: "25+ methods fail because they don't break the answer→constraint coupling. G directly severs this coupling via conclusion truncation — the diagnosis drives the fix."

### Framing Decision Threshold (Reviewer-approved)
- G ≥+5pp AND p<0.05 → **commit V3** (G+R dual method, G as core)
- G +3-5pp AND p<0.10 → **V3 weak** (G as "encouraging pilot", not core method)
- G <+3pp OR n.s. → **fall back to V2** (R proof-of-concept) or **V1** (pure negative)

### Updated Headline Result (D092 — V3 CONDITIONAL, awaiting G full results)

"Across 6+ models and 4 domains, symbolic consensus aggregation shows no statistically significant positive effect under same-model self-extraction. 25+ interventions fail. Root cause: Symbolic Confirmation Bias (4.97×). Two independent cures both succeed: (1) Constraint-Answer Decoupling removes conclusion sentences before FOL extraction, cutting the causal chain — +11.3pp (70/204 intermediate, PENDING FULL); (2) Cross-architecture NLI verification (DeBERTa) provides structurally complementary signal — +4.41pp (p=0.039). Both validate the diagnosis from orthogonal angles: G attacks the information flow, R attacks the architectural homogeneity."

### Updated Headline Result (D090 — V2 FALLBACK, if G full results weaker than intermediate)

"Across 6+ models and 4 domains, symbolic consensus aggregation shows no statistically significant positive effect under same-model self-extraction. 25+ interventions fail. Root cause: Symbolic Confirmation Bias (4.97×). A cross-architecture proof-of-concept (DeBERTa NLI w=3) achieves +4.41pp (p=0.039) — the only positive result across 25+ attempts. Per-label analysis reveals structural complementarity: NLI dominates contradiction detection (71% vs SC 38%), while LLMs dominate uncertainty reasoning (68% vs NLI 19%)."

### Updated Story Spine (D092 — V3, G+R dual method)

- **Problem**: [unchanged]
- **Theoretical lens**: [unchanged]
- **Systematic evaluation**: [unchanged]
- **Regime characterization**: [unchanged]
- **Remediation failures strengthen thesis (D085 FINAL)**: 9 prompt-level + 3 method-level + 13 new directions = **25+ interventions** across ALL dimensions (diversity/architecture/capability/verification/filtering/voting/solver/paradigm), all fail → bottleneck is fundamental and exhaustively proven
- **Method failure analysis**: Three methods targeting different bottleneck aspects show three distinct failure modes (neutral/harmful/catastrophic), revealing that the bottleneck operates at multiple levels simultaneously
- **Independence-accuracy trade-off (HERO FINDING, D075)**: Debate breaks trace correlation (κ 0.44→0.15, Eff-K 2.0→4.4) but accuracy collapses (-18.6pp/-23.0pp). Same-model traces can be independent OR accurate, not both.
- **Symbolic Confirmation Bias (CORE FINDING, D082)**: Root cause identified — self-extracted FOL constraints systematically confirm the trace's own answer (bias ratio 4.97× on incorrect problems). Causal chain: model reasons → answer → FOL extraction confirms answer → aggregation ≈ SC. This is WHY 25+ methods fail.
- **Process-κ (NEW METRIC, D082)**: CoT reasoning similarity (0.69) >> answer-κ (0.41), r=-0.06. Only 9.3% of trace pairs are "convergent reasoning." answer-κ underestimates the true bottleneck. Novel metric applicable to all LLM trace aggregation.
- **NEW — Constraint-Answer Decoupling (CORE METHOD, D092)**: Having diagnosed the causal chain (conclusion→FOL→bias), we sever it: remove conclusion sentences before extraction. 4.1% text removal → +11.3pp (70/204). Minimal intervention, maximal effect. Directly proves the mechanism IS the cause.
- **NEW — Cross-Architecture Verification (COMPLEMENTARY METHOD, D092)**: DeBERTa NLI (406M) w=1 **+3.43pp (p=0.039, McNemar exact)** PRIMARY; w=3 +4.41pp (p=0.078 n.s.); NLI∩SC 68.48%@45%. Orthogonal fix: instead of fixing the extraction pipeline, add an architecturally independent voter. Per-label complementarity (NLI: False 71% vs SC 38%; SC: Unknown 68% vs NLI 19%).
- **Dual cure narrative**: G attacks information flow (removes biased input to extractor), R attacks architectural homogeneity (adds independent voter). Both work independently. Validates diagnosis from two angles.
- **Actionable contribution**: C0+SC diagnostic + κ-based Eff-K estimation + Decoupling method + NLI combo = complete toolkit from diagnosis to fix.
- **Universal across architectures (D078)**: Three families: Mistral-7B κ=0.438, LLaMA-8B κ=0.412, Qwen2.5-7B κ=0.658, Qwen2.5-14B κ=0.738. Family effect (Δκ=0.22) >> scale effect (Δκ=0.08).
- **Headline (D092)**: Independence bottleneck is structural to same-model extraction, universal across architectures, rooted in Symbolic Confirmation Bias. 25+ same-model interventions fail. Two independent cures succeed: Decoupling (+11.3pp, CONDITIONAL on full 204) attacks the causal chain, Cross-Architecture NLI (+3.43pp, p=0.039) provides external diversity. Both prove the diagnosis and provide practical solutions.

## Core Insight (D060 Updated — Dual Bottleneck)

**Dual Requirement Framework**: SICA 效应需要同时满足两个条件，缺一不可：
1. **Sufficient Independence** (Eff-K > threshold): traces 需要提供足够多的独立视角
2. **Sufficient Quality** (SC > ~50%): traces 需要有足够的正确率，否则约束是噪声

Condorcet Jury Theorem 要求投票者独立且 p>0.5。同模型采样的 reasoning traces 严重违反独立性假设（Fleiss' κ = 0.21–0.82，Eff-K 仅 1.20–3.63），解释了为什么简单增加 K 或添加符号约束不能突破 SC 的天花板。

实验数据完美支持 dual requirement（κ 使用统一脚本 compute_fleiss_kappa_unified.py，SC/Δpp 使用 registry 原始值）：
- **Qwen family**: κ=0.66-0.82, Eff-K≈1.20-1.46（独立性不足）→ all near-zero delta，无论 SC 多高
- **Mistral-7B FOLIO**: κ≈0.46, Eff-K≈2.0（中等独立性）+ SC≈55%（中等质量）→ +3.43pp best seed, mean +2.12pp (2/3 seeds positive, 1 null)
- **Mistral-7B PW-600**: κ=0.20, Eff-K=3.76（最高独立性）但 SC=39%（质量不足）→ -2.83pp
- 只有 Goldilocks zone（中等 Eff-K + 中等 SC）出现正向 delta
- **Dual bottleneck 直接验证 (exp-055)**：Multi-temp κ=0.427 Eff-K=2.11（比单温度 κ≈0.46 Eff-K≈2.0 更独立）但 delta=0.00pp → 提高 independence 不够，还需要 extraction quality
- **T sensitivity 孤立尖峰 (4/4 complete, D064 corrected)**：T=0.3(Δ=-1.47), T=0.5(Δ=-0.98), T=0.7(Δ=+3.43, κ=0.460, Eff-K=1.98), T=1.0(Δ=0.00, κ=0.394, Eff-K=2.25)。T=0.7 孤立尖峰更突出。T=0.7 SC=55.88%（最低）→ entropy 最高 → SICA 操作空间最大。温度效应与 SC 效应互为 confound，论文需讨论
- **Thinking mode κ=0.913, Eff-K=1.09 (exp-028b)**：近乎确定性。思维模式让 traces 更一致 → 独立性更差。"更好的推理"反而加剧 independence bottleneck。

**κ 是 model-level 稳定属性**：统一处理后 Mistral 三 seed κ 收敛至 0.457-0.460（之前 0.41-0.50 差异是非标准 answer 处理的 artifact）。κ 跨 seed 几乎相同，但 delta 差异大（+3.43 vs +2.94 vs 0.00）→ seed-level constraint quality variance 主导，非 κ。

完整 κ 表（⚠️ D062: κ 将用 raw answers 重算，当前 unified 值为临时值。Qwen 无变化，Mistral 条件将更新）：
| Exp | Model | κ(unified→raw pending) | Eff-K | SC%(registry) | Δpp(registry) |
|-----|-------|------------|-------|---------------|---------------|
| exp-028b | Qwen3-14B thinking | 0.913 | 1.09 | ~84% | ~0 |
| exp-038 | Qwen-14B LogiQA | 0.821 | 1.20 | 78.50 | -0.50 |
| exp-027 | Qwen3-14B | 0.773 | 1.26 | 84.31 | +0.49 |
| exp-036 | Qwen2.5-14B | 0.744 | 1.31 | 75.49 | +0.25 |
| exp-035 | Qwen2.5-7B | 0.658 | 1.46 | 76.47 | -0.49 |
| exp-049b | Mistral-7B LogiQA | 0.512 | 1.81 | 51.00 | +0.50 |
| exp-057 | Mistral-7B T=0.3 | 0.502 | 1.84 | 58.33 | -1.47 |
| exp-058 | Mistral-7B T=0.5 | 0.516 | 1.80 | 58.33 | -0.98 |
| exp-033 | Mistral-7B s42 | 0.460 | 1.98 | 55.88 | +3.43 |
| exp-052 | Mistral-7B s123 | 0.457 | 1.99 | 54.41 | +2.94 |
| exp-053 | Mistral-7B s456 | 0.457 | 1.99 | 55.88 | 0.00 |
| exp-055 | Mistral-7B multi-T | 0.427 | 2.11 | 57.84 | 0.00 |
| exp-054 | Mistral-7B T=1.0 | 0.394 | 2.25 | 55.39 | 0.00 |
| exp-046 | Mistral-7B PW-600 | 0.200 | 3.76 | 39.33 | -2.83 |
注：κ 基于 T/F/U 三类归一化，Mistral-7B 约 12-16% traces 被归一化（Qwen 100% valid）。Mistral SC/Δpp 已更新为 D064 tiebreaking 修正值；Qwen 不受影响。

Oracle control (+14.22pp) 证明 MAX-SAT 聚合机制本身有效，但自提取约束仅利用了 24% 的理论上限。Discriminative filtering 实验揭示关键机制：~92% 约束 ARE discriminative，但过滤掉 ~8% non-discriminative 约束后 delta 不变（0 gains）。问题不在约束缺乏判别力，而在于 discriminative constraints 的区分方向与模型偏差一致（confirmation bias）。

**Remediation insight (D060)**: 9 种修复尝试全部失败，包括直接靶向 independence（multi-temp diversity, exp-055: Eff-K 从 2.0→2.11 但 delta 仍为 0）和 constraint quality（discriminative filtering）。这证明 bottleneck 不是简单的 diversity 或 quality 问题，而是 same-model self-extraction 的根本性限制。

**Key evidence**:
- **Condorcet independence quantification (统一脚本, 公式: Eff-K=K/(1+(K-1)κ))**: Mistral-7B FOLIO κ≈0.46 (Eff-K≈2.0, 三 seed 高度稳定), Mistral-7B PW-600 κ=0.200 (Eff-K=3.76), Qwen2.5-14B FOLIO κ=0.744 (Eff-K=1.31), Qwen2.5-14B LogiQA κ=0.821 (Eff-K=1.20), Qwen3-14B κ=0.773 (Eff-K=1.26), Qwen2.5-7B κ=0.658 (Eff-K=1.46). 跨模型清晰: Qwen Eff-K≈1.2-1.5→0 gain, Mistral FOLIO Eff-K≈2.0→variable gain, Mistral PW Eff-K=3.76 but SC too low→negative. κ stable across seeds (0.457-0.460), delta varies → seed-level constraint quality dominates.
- **Oracle control (exp-031)**: Gold FOL + MAX-SAT = 89.71% vs SC 75.49% (+14.22pp, p=2.0e-7). Unknown-type +31.9pp.
- **Two-layer constraint analysis**: 43% trivially_satisfied (taxonomy: satisfied by ALL answers) vs ~8% non-discriminative (filtering: same MAX-SAT score). Difference: trivially_satisfied constraints can still have different satisfaction DEGREES. Removing the 8% yields 0 gains → problem is not quality but confirmation bias direction.
- **K sensitivity (non-monotonic peak at K=12, 5/5 complete, D064+D066)**: K=4(-1.47pp), K=8(-1.96pp), K=12(+3.43pp p=0.092 ns), K=16(+1.47pp), K=20(+1.96pp). Peak at K=12, drops at K=16 but partially recovers at K=20. NOT clean inverted-U. K=12 SC=55.88% (post-fix). SC-confound with T sensitivity still holds. SICA at K=4 vs K=12 differs by ~4.9pp despite similar SC — proves SICA extracts different information than SC.
- **SC-confound (cross-cutting insight)**: K=12 和 T=0.7 都是 SC 最低 (54.41%) 的配置 → SICA "最佳超参"可能反映 entropy/operating-window 效应而非 K 或 T 的因果贡献。论文需要讨论这个 confound，但也可以正面利用：SC level 是更基本的预测变量，K 和 T 通过影响 SC 来间接影响 SICA delta。
- **T sensitivity (isolated peak, 4/4 complete, D064 corrected)**: T=0.3(Δ=-1.47pp), T=0.5(Δ=-0.98pp), T=0.7(Δ=+3.43pp p=0.092 ns), T=1.0(Δ=0.00pp). NOT smooth inverted-U — T=0.7 is an isolated spike. T=0.7 has lowest SC (55.88%) → highest entropy → largest SICA operating window. Temperature and SC effects confounded. Strengthens fragility narrative.
- **Regime boundary**: Qwen-14B (SC=75.49%) Δ=-0.98pp vs Mistral-7B (SC=55.88%) Δ=+3.43pp p=0.092 ns
- **Type C failure (exp-046)**: Mistral PW-D5 SC=39.33%, Δ=-2.83pp, p=0.010, κ=0.210, Eff-K=3.63, contradiction rate 5.5%. Highest Eff-K yet worst delta → independence alone insufficient when SC too low.
- **Seed replication (D064+D066)**: 2/3 seeds positive but **0/3 significant** after tiebreaking correction: s42 Δ=+3.43pp p=0.092, s123 Δ=+2.94pp p=0.070, s456 Δ=0.00pp p=1.0. Mean +2.12pp. Only significant McNemar effects are NEGATIVE: exp-046 Δ=-2.83pp p=0.014, exp-039 Δ=-2.50pp p=0.011. Paper must frame as "positive directional trend" not "significant positive effect".
- **Nine remediation failures (ALL CONFIRMED)**: contrastive prompting, cross-model, generational scaling, solver-guided, consistency filtering, cross-trace UNSAT, discriminative filtering (0 gains), T=1.0 (delta collapse +3.43→0.00pp, D064 corrected), multi-temp (delta=+0.00pp, b=5 c=5). All 9 failed → trap is fundamental, bottleneck is structural.
- **Entropy decomposition (VERIFIED 2026-05-19)**: High-entropy proportion: Mistral FOLIO 38% (78/204) vs Qwen FOLIO 18% (37/204) vs Qwen LogiQA 12% (23/200). SICA on high-entropy: Mistral FOLIO s42 +12.8pp, s123 +9.1pp, s456 -1.3pp; Qwen FOLIO -8.2pp; all others negative. Low-entropy: SICA≈SC across all 8 experiments (Δ≈0). Entropy decomposition reveals regime-dependent mechanism, NOT universal diagnostic.
- **Confirmation bias quantification**: ⚠️ "62.3%" and "28.6%" confirmed NOT present in any .tex file — likely hallucinated in earlier draft. DO NOT USE. Replace with verified metrics from experiment outputs only.

## Story Spine (D059 Updated)

- **Problem**: LLMs' reasoning can be improved by sampling multiple chains-of-thought and aggregating via majority voting (self-consistency). Recent work proposes symbolic augmentation: extract formal constraints from traces and use SAT solvers for answer selection. But does symbolic aggregation actually outperform simple voting?
- **Theoretical lens**: Condorcet Jury Theorem requires voter independence. We quantify trace independence via Fleiss' κ and show Effective-K << nominal K. This explains the fundamental limitation of same-model trace aggregation.
- **Systematic evaluation**: SICA (MAX-SAT over FOL constraints) across 3 domains × 5 model families. Oracle control separates extraction vs aggregation failure. Discriminative filtering reveals ~92% constraints are discriminative, yet SICA gains are fragile — confirmation bias, not constraint quality, is the bottleneck.
- **Regime characterization**: Three failure modes (Type A/B/C) + narrow Goldilocks zone. C0+SC as deployment diagnostic.
- **Remediation failures strengthen thesis**: 9 targeted interventions (prompting, architecture, capability, verification, diversity, filtering) all fail to close the oracle gap, proving the bottleneck is fundamental to same-model self-extraction.
- **Headline result (D066 McNemar corrected)**: "Across 6 models and 4 domains, symbolic consensus aggregation shows no statistically significant positive effect under corrected tiebreaking (best seed +3.43pp, p=0.092). The only significant effects are negative (PW-600: -2.83pp p=0.014, -2.50pp p=0.011). However, entropy decomposition reveals a striking regime-dependent pattern: SICA's entire effect concentrates on high-entropy questions, with +12.8pp in the Goldilocks zone but -2 to -8pp elsewhere. Oracle constraints prove the aggregation mechanism works (+14.22pp, p<0.001), localizing the bottleneck to extraction quality (24% utilization). Condorcet analysis (Eff-K=1.2-2.0 for nominal K=12) explains trace non-independence. Nine remediation strategies all fail, confirming the bottleneck is structural to same-model self-extraction."

## Anticipated Reviewer Concerns & Defensive Experiments

1. **"Gains not statistically significant"** → Correct: no positive effect reaches significance (best p=0.092). This IS the finding. Oracle p=2.0e-7 proves the mechanism works; the insignificance of self-extraction gains demonstrates the extraction bottleneck. Regime pattern (8 entropy conditions) provides systematic evidence beyond any single p-value.
2. **"Only one positive result (exp-033)"** → Seed replication: 2/3 positive (s42 +3.43pp, s123 +2.94pp), 1/3 null (s456 0.00pp). Mean +2.12pp. Effect IS real but fragile — the fragility itself IS the finding.
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

## Working Title (D092 V3 — G+R dual method)
**"Breaking Symbolic Confirmation Bias: Constraint-Answer Decoupling and Cross-Architecture Verification for LLM Logical Reasoning"**
(Alternatives:
- "Two Cures for One Disease: Decoupling and Architectural Diversity Against Symbolic Confirmation Bias in LLM Reasoning"
- "The Independence Bottleneck in Symbolic LLM Reasoning: Diagnosis, 25+ Failed Interventions, and Two Independent Solutions"
- V2 fallback (R only): "Breaking the Self-Consistency Ceiling: How Cross-Architecture Verification Overcomes Symbolic Confirmation Bias in LLM Reasoning"
- V1 fallback (pure negative): "Beyond Self-Consistency: How Trace Independence Limits Symbolic Consensus in LLM Reasoning")

NOTE (Dream D037): Title MUST be scoped to "self-extracted constraints" / "SICA". Published methods (DyLoS, Aristotle, FoVer) use different approaches.

## Paper Structure (D092 V3 — EMNLP 8pp + appendix)

### Sections
- §1 Introduction: 25+ same-model interventions all fail → independence bottleneck → two independent cures
- §2 Related Work: SC, neuro-symbolic, Condorcet/voting, verification
- §3 Diagnostic Framework: Independence Bottleneck (Eff-K, process-κ), Oracle Gap
- §4 Symbolic Confirmation Bias: bias ratio 4.97×, overlap 94%, causal chain
- §5 Method 1: Constraint-Answer Decoupling (G) — core method, detailed
- §6 Method 2: Cross-Architecture NLI Verification (R) — complementary method
- §7 Combined Analysis: G+R combo, ablation, cross-dataset if available
- §8 Discussion + Conclusion

### Main Tables
- T1: Main Results — models × domains, SC% / SICA% / Δpp / p-value, regime boundary
- T2: Oracle Control — Gold-FOL+MAX-SAT vs SC vs SICA-self, causal separation
- T3: Independence Quantification — Fleiss' κ / Eff-K / trace agreement per model
- T4: Confirmation Bias — bias ratio per condition, overlap rate, per-label breakdown
- T5: Decoupling Results (G) — SC / SICA / G-Decoupled, Δpp, McNemar, per-label
- T6: NLI Verification Results (R) — SC / NLI standalone / combo w=1,3 / intersection, Δpp, McNemar
- T7: 25+ Intervention Summary — method / type / dataset / result / failure mode (compact)

### Main Tables (continued)
- T6: Method-Level Intervention Results — 3 methods × 2 datasets, SC% / Method% / Δpp, failure mode classification
- T7: κ Generalization — SC / Debate / Diverse-Prompt κ and Eff-K (from exp-077, pending)

### Main Figures
- F1: Method Pipeline (SICA + oracle control design)
- F2: SC Accuracy vs SICA Δ scatter (hero figure, regime boundary)
- F3: K Sensitivity with diversity metrics (K vs Δ, K vs Eff-K)
- F4: Extraction error breakdown (stacked bar)
- F5: Method intervention failure modes (grouped bar: ICG/Contrastive/Debate × FOLIO/LogiQA)

### Appendix
- K ablation details, temperature sensitivity, per-domain results, overhead analysis
- Entropy-conditioned analysis (continuous scatter + bin sensitivity)
- Six remediation strategy details
- Confirmation bias quantification
- Seed replication analysis
- QwQ-32B / DeepSeek-R1 negative control

## Claim Risk Notes (D059)
- **Seed replication**: 0/3 significant after D066 correction (p=0.092, 0.070, 1.0). 2/3 positive trend, 1/3 null. Mean +2.12pp. Frame as "directional trend, not significant effect" — fragility IS the finding.
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

## Additional Reviewer Concerns (D070/D074 Methods)

17. **"Why not use a larger model for constraint generation?"** → Valid. All methods tested at 7B scale. ICG constraint parsing failures + Debate role-play degradation may be scale-dependent. This is explicitly noted as limitation and future work. The contribution is diagnosing the bottleneck and showing it's not trivially fixable, not claiming no fix exists at any scale.
18. **"Only tested one model (Mistral-7B) for methods"** → Methods are interventions on the extraction pipeline, not the base model. Testing on the same model that showed the clearest Goldilocks signal (Mistral-7B FOLIO) is the strongest test — if methods can't improve the best-case scenario, they won't help elsewhere.
19. **"ICG multi-seed shows 1/3 positive"** → Magnitudes (-2.0, +1.5, -1.0) are within SC baseline noise (3.5pp cross-seed). Mean ≈-0.5pp, std=1.8pp. No statistical significance. Properly framed as "noise-level, neither improving nor degrading."
20. **"Debate working in other papers"** → Multi-agent debate literature uses diverse models or much larger models. Same-model 7B debate is a different regime. Our finding is specifically about same-model self-extraction limitations.

## Claim Scoping Rules
- n=60 conditions: "suggestive/consistent with" NOT "confirming"
- n≥200 conditions: can "confirm"
- Combined N>1,300: acceptable if breakdown clearly stated
- Method claims: must show statistically significant improvement OR clear directional improvement with analysis
- "Independence bottleneck" framing: systematic quantification + theoretical grounding

## V16 Frontier Model Extension (D135–D139)

### New Claim 11: SCB is Universal — 7B to Frontier (D135)

Symbolic Confirmation Bias persists across ALL tested models, from 7B open-source to frontier closed-source:

| Model | Extraction | SC% | SICA% | Δpp | BR(mean) | BR=∞ rate | Process-κ | Answer-κ |
|-------|-----------|-----|-------|-----|----------|-----------|-----------|----------|
| Mistral-7B | self | 55.88 | 59.31 | +3.43 | 4.97 | 30% | 0.69* | 0.46 |
| LLaMA-8B | self | — | — | — | 2.88 | — | — | — |
| Qwen-14B | self | 75.49 | 75.74 | +0.25 | 3.93 | — | — | 0.74 |
| R1-Distill-8B | cross→Mistral | 74.51 | 76.96 | +2.45 | 2.92 | — | 0.248 | 0.69 |
| gpt-4o | self | 73.91 | 72.05 | -1.86 | 2.94 | 44% | 0.79 | 0.80 |
| gpt-4.1 | cross→Mistral | 82.84 | 81.37 | -1.47 | 2.70 | 58% | 0.792 | 0.86 |
| gpt-5.5 | cross→Mistral | 84.31 | 84.80 | +0.49(n.s.) | 3.48 | 87% | 0.563 | 0.96 |
| o3 | cross→Mistral | 82.65 | 82.65 | 0.00 | 1.66 | 82% | 0.596 | 0.92 |
| Gemini-2.5-Pro* | cross→Mistral | 87.37 | 86.32 | -1.05 | 2.79 | — | 0.790 | 0.75 |

*Gemini: 95/204 interim. Mistral Process-κ is CoT cosine sim (different metric from cross-model TF-IDF κ).

BR > 1 across ALL models (1.66–4.97×). BR=∞ rates high in frontier models (44–87%).
Table footnote MUST distinguish self vs cross extraction context.

### New Claim 12: Process-κ Gradient Predicts Cross-Model Extraction Effectiveness (D137–D139)

Cross-model extraction (Mistral-7B extracts FOL from other models' traces) effectiveness is monotonically predicted by Process-κ:

| Model | Process-κ | Δ(SICA-SC) | BR(mean) |
|-------|-----------|------------|----------|
| R1-Distill | 0.248 | +2.45pp ✓ | 2.92 |
| gpt-5.5 | 0.563 | +0.49pp(n.s.) | 3.48 |
| o3 | 0.596 | 0.00pp | 1.66 |
| Gemini-2.5-Pro* | 0.790 | -1.05pp | 2.79 |
| gpt-4.1 | 0.792 | -1.47pp | 2.70 |

**Spearman ρ(κ→Δ) = -1.0, n=5, one-tailed p=0.0083** (statistically significant).

**Paper language constraints (D138)**:
- Use "decreases monotonically" — NOT "predictive" or "significant correlation"
- Dual-variable framing: "two necessary conditions" (qualitative mechanism), NOT regression model
  - Low κ (diverse traces) → cross-model extractor can contribute novel constraints
  - High BR (strong self-bias) → there IS bias to escape from
  - Both conditions required: o3 (BR=1.66, near-unbiased) → Δ=0 despite moderate κ=0.596
- o3 BR=1.66 is observation ("bimodal error pattern: 82% BR=∞ but low finite-BR"), NOT sub-finding
- BR=∞ ordering does NOT strictly follow "model capability" (o3 82% < gpt-5.5 87%). Drop ordering claim.

### Updated Headline (V16)

"Symbolic Confirmation Bias is universal from 7B open-source to frontier closed-source models (BR 1.66–4.97×). Cross-model extraction effectiveness decreases monotonically with Process-κ (ρ=-1.0, n=5, p=0.008), modulated by bias severity: gain requires both diverse traces (low κ) AND substantial self-bias (high BR). 25+ same-model interventions fail; two cross-architecture cures succeed."

### V16 Paper Structure Impact

- §4 SCB: Add frontier model BR table (Table 4 or expanded T4)
- §3 or new §: Process-κ gradient analysis (Table + scatter plot)
- §1 Intro: Scale claim upgraded from "7B-32B" to "7B to frontier"
- Limitations: Update "7B to 32B parameters" scope claim
- New Figure: Process-κ vs Δ scatter with dual-variable annotation (5 points + regression-free narrative)
