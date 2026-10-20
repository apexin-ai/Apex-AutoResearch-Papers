# Literature Survey: Formal Verification for LLM Reasoning & Test-time Verification Baselines

**Date**: 2026-05-14
**Scope**: 2023–2026, focusing on direct competitors to SVS and SOTA test-time verification baselines
**Cross-reference**: Papers already detailed in `docs/IDEA_BRIEF.md` are marked [IB] and summarized briefly; new findings are marked [NEW].

---

## Part I: 直接竞品 — Formal Verification for LLM Reasoning

### 1. Semantic Self-Verification (SSV) (IJCAI 2025) [NEW] ⚠️ 高度相关
- **方法**: 用 Z3 SMT solver 通过 concrete instantiation 验证 LLM 生成的 FOL formalization 正确性；使用 instantiation-guided refinement 改进 formalization；在 verified cases 上达到近乎 100% precision
- **与 SVS 的关系**: **高度 overlap** — 同样使用 Z3 验证 FOL formalization，但目标不同：SSV 验证单个 formalization 的正确性（通过实例化），SVS 用 verification score 做 chain selection
- **关键差异**: SSV 的核心创新是 instantiation-based self-verification（用具体实例检验抽象 formalization）；SVS 的核心创新是 graded multi-signal scoring + cross-chain consistency。SSV 可作为 SVS formalization 质量的补充模块。SSV 在 AR-LSAT 上达 71.3%（vs Logic-LM 43%），验证了 Z3-based verification 的有效性
- **arXiv ID**: 2501.16961

### 2. FoVer: First-Order Logic Verification (TACL 2025) [IB]
- **方法**: LLM 将 NL 翻译为 FOL，Z3 做 binary verification，然后 majority vote
- **与 SVS 的关系**: **直接 baseline** — SVS 的 "binary filter + SC" 消融项
- **关键差异**: FoVer 用 binary filter + majority vote；SVS 用 graded scoring + score-based selection
- **DOI**: 10.1162/TACL.a.41

### 3. VeriCoT: Neuro-symbolic Chain-of-Thought Validation (ICLR 2026) [IB]
- **方法**: 逐步 FOL 验证 CoT 的每一步，每条 chain 独立验证
- **与 SVS 的关系**: **直接 baseline** — 更细粒度的 step-level verification，但仍是 binary pre-filter
- **关键差异**: VeriCoT 做 step-level 验证；SVS 做 chain-level + cross-chain verification。VeriCoT 独立验证每条 chain，SVS 还检查 cross-chain consistency

### 4. LINC (EMNLP 2023) [IB]
- **方法**: FOL autoformalization + Prover9 验证 + voting over translation variants
- **与 SVS 的关系**: **直接 baseline** — 最早的 neurosymbolic FOL verification pipeline
- **关键差异**: LINC votes over multiple FOL translations of the same problem；SVS scores multiple reasoning chains of the same problem
- **arXiv ID**: 2309.12941

### 5. MATP: Multi-step Automated Theorem Proving (ICSE 2026) [IB]
- **方法**: Step-level FOL 验证，84-94% macro F1 on PrOntoQA/ProofWriter/FOLIO
- **与 SVS 的关系**: **互补** — 提供更精细的 step-level 验证信号
- **关键差异**: MATP 关注发现推理缺陷（error detection），SVS 关注 chain selection

### 6. MAD-LOGIC (ICLR 2026) [IB]
- **方法**: 将 NL 翻译为三种符号语言 (LP, FOL, SAT)，多 agent debate + solver 聚合
- **与 SVS 的关系**: **不同方向** — debate across formalizations vs. verification across reasoning chains
- **关键差异**: MAD-LOGIC 在同一问题的不同形式化间 debate；SVS 在同一问题的不同推理路径间验证一致性

### 7. FregeLogic (SemEval 2026) [IB]
- **方法**: Z3 作为 LLM ensemble 的 tiebreaker，用于 syllogism 验证，达 94.3%
- **与 SVS 的关系**: **概念验证** — 验证了 "solver as selector" 概念，但限于 syllogism
- **关键差异**: FregeLogic 用于 fixed ensemble tiebreaking on syllogisms；SVS 用于 sampled chain selection with graded scoring on general logical reasoning

### 8. Logic-LM (EMNLP 2023 Findings) [NEW]
- **方法**: LLM 将 NL 翻译为符号形式化 → 确定性 symbolic solver 求解 → self-refinement 利用 solver error messages 修正
- **与 SVS 的关系**: **不同方向** — Logic-LM 用 solver 做推理（替代 LLM reasoning），SVS 用 solver 做验证（评估 LLM reasoning）
- **关键差异**: Logic-LM 的 solver 是 reasoner（直接产出答案），SVS 的 solver 是 verifier（评估推理链质量）。Logic-LM 平均提升 39.2% over standard prompting
- **arXiv ID**: 2305.12295

### 9. SatLM (NeurIPS 2023) [NEW]
- **方法**: LLM 生成 declarative task specification → Z3 theorem prover 推导答案。在 LSAT、BoardgameQA 上达 SOTA
- **与 SVS 的关系**: **不同方向** — SatLM 用 Z3 做推理，SVS 用 Z3 做验证
- **关键差异**: SatLM 完全替代 LLM 推理（solver as reasoner），SVS 保留 LLM 推理并用 solver 评估
- **arXiv ID**: 2305.09656

### 10. LINA: LLM-driven Neurosymbolic Approach (ICLR 2026 submission) [NEW]
- **方法**: 使用 hypothetical-deductive method + FOL rules，LLM 自主完成从命题逻辑提取到推理的全过程，无需外部 solver
- **与 SVS 的关系**: **不同方向** — LINA 消除外部 solver 依赖，SVS 刻意依赖外部 solver 提供形式保证
- **关键差异**: LINA 在 LogiQA 上提升 35.24% over LINC/SatLM；SVS 的 formal guarantee 来自 Z3 而非 LLM internal reasoning
- **OpenReview**: 3BoCwZFRJX

### 11. MATH-VF: Step-Wise Formal Verification (arXiv, May 2025) [NEW]
- **方法**: Formalizer (LLM) 将 NL 解题过程翻译为 formal context → Critic (CAS + SMT solver) 逐步验证正确性 + 纠错反馈
- **与 SVS 的关系**: **互补** — MATH-VF 用于数学推理的逐步验证 + 修正，SVS 用于逻辑推理的 chain selection
- **关键差异**: MATH-VF 有 refinement loop（验证 + 修正），SVS 是 one-shot verification for selection。MATH-VF 针对数学，SVS 针对逻辑推理
- **arXiv ID**: 2505.20869

### 12. Safe: Retrospective Step-aware Formal Verification (arXiv, June 2025) [NEW]
- **方法**: 用 Lean 4 对数学推理每一步做 formal verification，识别 hallucination
- **与 SVS 的关系**: **互补** — 不同 formal system (Lean 4 vs Z3)，不同目标 (math vs logic)
- **关键差异**: Safe 用 Lean 4 做证明级验证，SVS 用 Z3 做 satisfiability 验证
- **arXiv ID**: 2506.04592

### 13. "Do LLMs Game Formalization?" (arXiv, April 2026) [NEW] ⚠️ 高度相关
- **方法**: 评估 GPT-5 和 DeepSeek-R1 在 FOLIO/Multi-LogiEval 上的 Lean 4 proof faithfulness
- **与 SVS 的关系**: **直接相关** — 揭示 autoformalization 的两类 unfaithfulness：GPT-5 fabricates axioms，DeepSeek-R1 mistranslates premises
- **关键差异**: 这篇论文是对 autoformalization 信任度的 critical evaluation。SVS 的 PCV 方法（Premise-Conditioned Verification）部分缓解了 premise mistranslation 问题（因为验证 claims 与 premises 的一致性）。**高 compilation rate ≠ faithful reasoning**，这对 SVS 的 formalization confidence 设计有直接启示
- **arXiv ID**: 2604.19459

### 14. VERGE: Formal Refinement and Guidance Engine (arXiv, Jan 2025) [IB]
- **方法**: Greedy MCS-based error localization via SMT solver + iterative refinement
- **与 SVS 的关系**: **技术借鉴** — SVS 的 graded internal consistency scoring 基于 VERGE 的 greedy MCS
- **arXiv ID**: 2601.20055

### 15. Grammars of Formal Uncertainty (NeurIPS 2025) [IB]
- **方法**: 量化何时信任 LLM autoformalization，AUROC > 0.93
- **与 SVS 的关系**: **互补** — 可用于 SVS 的 formalization confidence 信号

### 16. PRoSFI (arXiv, March 2026) [IB]
- **方法**: 训练 7B 模型生成 structured formal intermediates，76% GPT soundness on ProverQA
- **与 SVS 的关系**: **互补** — 验证了小模型可产出可验证的形式化表示
- **arXiv ID**: 2603.29500

### 17. SEP: Symbolic Equivalence Partitioning (arXiv, April 2026) [IB]
- **方法**: Z3-based symbolic execution 将代码按语义分组，选择 dominant 等价类做 best-of-N code selection
- **与 SVS 的关系**: **最近的 paradigm parallel** — 独立验证了 formal verifier 替代 learned verifier 做 best-of-N selection 的范式，但在 code domain
- **关键差异**: SEP 按语义等价分组（code domain），SVS 按逻辑一致性打分（logic domain）
- **arXiv ID**: 2604.06485

### 18. Autoformalization in the Era of LLMs: A Survey (arXiv, May 2025) [NEW]
- **方法**: 综合调研 autoformalization 在 LLM 时代的进展、挑战和应用
- **与 SVS 的关系**: **参考** — 提供 autoformalization 成熟度的全面评估
- **arXiv ID**: 2505.23486

### 19. LogicReward (ICLR 2026) [IB]
- **方法**: 训练时用 Isabelle 做 step-level verification，+11.6% over GPT-4o
- **与 SVS 的关系**: **互补** — training-time method vs. SVS inference-time

### 20. NL2FOL (IJCNLP 2025 Findings) [IB]
- **方法**: Step-by-step FOL formalization + SMT verification for logical fallacy detection，F1=78-80%
- **与 SVS 的关系**: **互补** — 验证了 FOL+SMT pipeline 可推广到 naturalistic inputs
- **arXiv ID**: 2405.02318

---

## Part II: Test-time Verification Baselines

### A. Learned Verifiers (ORM/PRM)

### 21. Logical Reasoning with ORMs (EMNLP 2025) [IB]
- **方法**: 训练 ORM 做 best-of-N selection on FOLIO/ProverQA/JustLogic
- **作为 baseline 的可行性**: **高** — 直接展示 best-of-N with learned verifiers > majority voting on logical reasoning
- **关键指标**: FOLIO, ProverQA, JustLogic; significantly outperforms SC on logical reasoning

### 22. ThinkPRM: Process Reward Models That Think (arXiv, April 2025) [NEW]
- **方法**: 用 long CoT 做 generative PRM，仅需 8K process labels（PRM800K 的 1%），在 ProcessBench/MATH-500/AIME'24 上 best-of-N 表现优于 discriminative PRM
- **作为 baseline 的可行性**: **中** — 主要在 math domain 评测，但代表了 PRM 的 SOTA；ThinkPRM-14B 超越了 100x 数据量训练的 discriminative PRM
- **关键指标**: ProcessBench, MATH-500, AIME'24, GPQA-Diamond (out-of-domain +8%)
- **arXiv ID**: 2504.16828

### 23. GenRM: Generative Verifiers (ICLR 2025) [NEW]
- **方法**: 用 next-token prediction 训练 verifier，支持 CoT reasoning 做 verification，best-of-N 大幅提升
- **作为 baseline 的可行性**: **中** — 代表 generative verification paradigm，与 SVS 形成 "learned generative verifier vs formal verifier" 对比
- **关键指标**: GSM8K (73→93.4%), algorithmic tasks (5→45.3%), MATH (28→44.6%)
- **arXiv ID**: 2408.15240

### 24. RLV: Putting the Value Back in RL (arXiv, May 2025) [NEW]
- **方法**: RL 训练中联合训练 reasoner + generative verifier，无额外开销。MATH accuracy +20% with parallel sampling
- **作为 baseline 的可行性**: **低** — 需要 RL 训练，SVS 是 training-free
- **关键指标**: MATH (+20% with parallel sampling), 8-32× efficient TTS scaling
- **arXiv ID**: 2505.04842

### 25. Scaling Generative Verifiers for Math (NeurIPS 2025) [NEW]
- **方法**: 将 GenSelect + LLM-as-a-Judge 扩展到 millions of tokens；RL 训练减少 prompt sensitivity
- **作为 baseline 的可行性**: **低** — 专注数学证明验证，但提供了 verification 方法的可靠性分析框架
- **关键指标**: Multiple math benchmarks; cautions against single-benchmark evaluation
- **arXiv ID**: 2511.13027

### 26. ReProbe: Internal State Probing (arXiv, Nov 2025) [NEW]
- **方法**: <10M 参数的 lightweight probe 分析 LLM 内部状态（hidden states, attention, logits）做 step-level verification，匹配或超越 810x 更大的 PRM
- **作为 baseline 的可行性**: **中** — 极低开销的 verification 方法，与 SVS 的 Z3 "near-zero cost" 在效率上可比
- **关键指标**: Math, planning, general QA; matches PRMs 810x larger
- **arXiv ID**: 2511.06209

### B. Reward-Free / Statistical Selection

### 27. Self-Certainty (NeurIPS 2025) [IB]
- **方法**: Token distribution 的 KL divergence 做 best-of-N selection，near-zero overhead
- **作为 baseline 的可行性**: **高** — SVS 的主要 reward-free 对比对象（statistical vs formal verification）
- **关键指标**: GSM8K, MATH, CRUXEval, LiveCodeBench

### 28. Latent Self-Consistency (LSC) (AAAI 2026) [NEW]
- **方法**: 在 EOS token 后添加少量 trainable tokens，用 learned embeddings 的 cosine similarity 做语义一致性选择
- **作为 baseline 的可行性**: **中** — 需少量训练，但在 short-form + long-form reasoning 上均超越 SC/USC/WUCS
- **关键指标**: MATH, MMLU, TruthfulQA; overhead <0.9% runtime
- **arXiv ID**: 2508.18395

### 29. Universal Self-Consistency (USC) (ICML 2024 Workshop) [NEW]
- **方法**: 用 LLM 自身选择 multiple candidates 中最一致的答案，适用于 free-form answers
- **作为 baseline 的可行性**: **中** — 扩展 SC 到 open-ended tasks，但需额外 LLM call
- **关键指标**: Math reasoning, code generation, summarization, open-ended QA
- **arXiv ID**: 2311.17311

### 30. RASC: Reasoning Aware Self-Consistency (NAACL 2025) [NEW]
- **方法**: 结合 answer-level + rationale-level features 做 sufficiency classifier，引导 stopping + weighted voting，减少 88% samples
- **作为 baseline 的可行性**: **中** — 高效 SC variant，但需训练 classifier
- **关键指标**: Reduces samples by ~88% with improved faithfulness
- **arXiv ID**: 2408.17017

### 31. Optimal Self-Consistency / Blend-ASC (arXiv, Nov 2025) [NEW]
- **方法**: 首次系统分析 SC 的 power-law scaling behavior；Blend-ASC 自适应 SC 算法在低/高 sample regime 均表现最优
- **作为 baseline 的可行性**: **中** — 提供 SC 效率的理论上界，可作为 SVS 超越 SC 的 calibration point
- **关键指标**: Power-law scaling analysis across multiple datasets
- **arXiv ID**: 2511.12309

### 32. CISC: Confidence Improves Self-Consistency (ACL 2025 Findings) [IB]
- **方法**: Neural confidence weighting for SC
- **作为 baseline 的可行性**: **高** — 简单有效的 weighted SC baseline

### C. Verification-Guided Search & Compute-Optimal Methods

### 33. V1: Pairwise Self-Verification (arXiv, March 2026) [NEW]
- **方法**: 不确定性引导的 tournament-based pairwise ranking；V1-PairRL 联合训练 generator + pairwise verifier。Pass@1 提升最多 10%
- **作为 baseline 的可行性**: **低** — 需要 RL 训练，但 V1-Infer（training-free）可作为参考
- **关键指标**: LiveCodeBench, CodeContests, SWE-Bench, AIME, HMMT
- **arXiv ID**: 2603.04304

### 34. VG-Search: Variable Granularity Search (NeurIPS 2025) [NEW]
- **方法**: 统一 beam search 和 best-of-N 的 tunable granularity 参数 g；adaptive VG-Search 提升 accuracy 3.1-3.6%，FLOPs 减少 52%
- **作为 baseline 的可行性**: **低** — 关注 search strategy 而非 verification signal，与 SVS 正交
- **关键指标**: +3.1% over Beam Search, +3.6% over Best-of-N, -52% FLOPs
- **arXiv ID**: 2505.11730

### 35. Snell et al.: Compute-Optimal Test-Time Scaling (ICLR 2025) [IB]
- **方法**: 最优 test-time compute 分配策略；难题用 best-of-N + PRM，易题用 sequential revision
- **作为 baseline 的可行性**: **高** — SVS 需在 difficulty-stratified 分析中对标此框架

### 36. Singhi et al.: Generation vs Verification Tradeoff (COLM 2025) [IB]
- **方法**: 推导 generation-vs-verification inference scaling laws；SC 比 GenRM 更 compute-efficient（GenRM 需 8x compute）
- **作为 baseline 的可行性**: **高** — SVS 的 compute-efficiency 论证直接基于此框架（Z3 near-zero cost vs learned verifier cost）

### D. Neurosymbolic Reasoning Baselines

### 37. LogicAgent (2026) [IB]
- **方法**: Multi-perspective semiotic reasoning，FOLIO +7.97, ProofWriter +7.28
- **作为 baseline 的可行性**: **高** — FOLIO/ProofWriter 上的 SOTA neurosymbolic method

### 38. Mixture-of-Thought (arXiv, May 2025) [IB]
- **方法**: Multi-modality reasoning，+11.7pp
- **作为 baseline 的可行性**: **中** — 强 baseline，但方法差异大
- **arXiv ID**: 2505.15817

### 39. LEVER: Learning to Verify (ICML 2023) [NEW]
- **方法**: 训练 verifier 根据 execution results 重排 code generations，提升 4.6-10.9%
- **作为 baseline 的可行性**: **低** — code domain，但验证了 execution-based verification for selection 的有效性
- **arXiv ID**: 2302.08468

### E. Surveys & Meta-analyses

### 40. "Trust but Verify!" — Verification for Test-time Scaling Survey (arXiv, Aug 2025) [NEW]
- **内容**: 全面调研 verifier training, types, 和在 TTS 中的使用。分类：prompt-based / discriminative / generative verifier；process / outcome verification
- **价值**: SVS 论文 Related Work 的重要参考，定位 Z3 作为 "non-neural verifier" 的独特类别
- **arXiv ID**: 2508.16665

### 41. What, How, Where, and How Well? — Test-Time Scaling Survey [NEW]
- **内容**: TTS 方法的全面分类（what to scale, how to scale, where to scale, evaluation）
- **价值**: 帮助 SVS 定位在 TTS 研究全景中的位置
- **URL**: https://testtimescaling.github.io/

---

## Part III: 竞争格局总结

### SVS 的独特性

1. **Graded verification scoring vs binary filtering**: 所有现有 formal verification 方法（FoVer, LINC, VeriCoT, MATP）都将 Z3 验证结果作为 binary filter（pass/fail）+ majority vote。SVS 首次将 formal verification 作为 graded scorer 用于 score-based chain selection。
2. **Cross-chain logical coherence (CCLC)**: 没有任何现有工作检查同答案推理链之间的逻辑兼容性。最接近的是 ConsistencyBench（cross-query consistency）和 cross-query contradiction detection（solver-augmented），但都不是 cross-chain。
3. **Formal verifier for selection paradigm**: SEP 在 code domain 独立验证了此范式（Z3-based selection without additional LLM inference）。SVS 是 logic domain 的首个实例。
4. **Compute-efficiency advantage over learned verifiers**: Z3 验证 near-zero cost vs ORM/PRM 需额外 neural forward pass。直接回应 Singhi et al. 的 generation-vs-verification tradeoff 分析。

### 最大竞争威胁

1. **SSV (IJCAI 2025)** ⚠️: 同样用 Z3 验证 FOL formalization，但 SSV 的 instantiation-based verification 是验证 formalization 正确性的更精细方法。如果 reviewer 认为 SSV + SC 已经足够好，SVS 的 graded scoring 的增量价值可能被质疑。**建议**: 明确与 SSV 区分（SSV 验证 formalization quality，SVS 用 verification 做 chain selection），并考虑集成 SSV 的 instantiation technique 到 SVS 的 formalization confidence 中。

2. **"Do LLMs Game Formalization?" (arXiv 2604.19459)** ⚠️: 揭示了 autoformalization unfaithfulness 的系统性风险。高 compilation rate ≠ faithful reasoning。这对 SVS pipeline 的信任度是根本性挑战。**建议**: 在论文中显式讨论此风险，强调 PCV 的 premise-conditioned 设计部分缓解了 premise mistranslation 问题。

3. **Self-Certainty (NeurIPS 2025)**: near-zero cost 的 reward-free selection baseline。如果 Self-Certainty 在 logical reasoning 上与 SVS 表现相当，则 SVS 的 autoformalization overhead 难以 justify。**建议**: RQ2 的 head-to-head 对比是关键，需确保在 hard problems（SC Q1-Q2 quartile）上展示 formal verification 的优势。

4. **ThinkPRM (arXiv 2504.16828)**: 仅需 1% process labels 即超越 discriminative PRM，代表了 learned verifier 的新 SOTA。虽然需要训练数据，但 data efficiency 大幅提升降低了 learned verifier 的 barrier。

### 无直接竞品的领域

- **Z3 graded scoring for chain selection**: 无
- **Cross-chain logical coherence checking**: 无
- **Formal verification compute-efficiency Pareto analysis vs learned/statistical verifiers on logic benchmarks**: 无

---

## Part IV: 推荐 Baselines（按优先级）

### P0: 必须包含
1. **Self-Consistency (SC)** — majority voting baseline (Wang et al., ICLR 2023)
2. **FoVer binary filter + SC** — 直接对比 binary vs graded verification (TACL 2025)
3. **Self-Certainty** — reward-free statistical baseline (NeurIPS 2025)
4. **ORM for Logical Reasoning** — learned verifier best-of-N baseline (EMNLP 2025)

### P1: 强烈建议
5. **LINC** — neurosymbolic FOL verification baseline (EMNLP 2023)
6. **CISC** — confidence-weighted SC (ACL 2025 Findings)
7. **VeriCoT** — step-level verification (ICLR 2026)

### P2: 时间允许
8. **USC / LSC** — 改进的 SC variants (ICML 2024 / AAAI 2026)
9. **Logic-LM** — solver-as-reasoner baseline (EMNLP 2023 Findings)
10. **SSV** — instantiation-based Z3 verification (IJCAI 2025)
11. **ThinkPRM** — SOTA generative PRM baseline (arXiv 2504.16828)

### Positioning Strategy

SVS 应定位为：
- **Primary narrative**: "Formal verification 从 binary filter 升级为 graded verifier，从 pre-filter for SC 升级为 替代 SC 的 selection mechanism"
- **Compute-efficiency story**: 直接对标 Singhi et al. 框架 — Z3 (near-zero cost verifier) vs learned verifiers (expensive) vs statistical signals (cheap but logic-blind)
- **与 SSV 的区分**: SSV 验证 formalization 质量（"is my FOL correct?"），SVS 用 verification score 做 chain selection（"which reasoning chain is best?"）
- **与 autoformalization faithfulness 风险的应对**: PCV 的 premise-conditioned 设计 + formalization confidence 信号 + round-trip faithfulness check
- **CCLC 作为独立贡献**: 即使 CCLC 效果有限，cross-chain consistency analysis 本身是对 ensemble agreement/diversity 理论在 formal logic 中的首次实例化

---

## Appendix: 按 arXiv ID 索引

| Paper | arXiv / Venue | Year | Category |
|-------|--------------|------|----------|
| Self-Consistency | 2203.11171 / ICLR 2023 | 2023 | Baseline |
| Logic-LM | 2305.12295 / EMNLP 2023 Findings | 2023 | FV-Competitor |
| SatLM | 2305.09656 / NeurIPS 2023 | 2023 | FV-Competitor |
| LINC | 2309.12941 / EMNLP 2023 | 2023 | FV-Competitor |
| LEVER | 2302.08468 / ICML 2023 | 2023 | TT-Baseline |
| USC | 2311.17311 / ICML 2024 Workshop | 2024 | TT-Baseline |
| GenRM | 2408.15240 / ICLR 2025 | 2025 | TT-Baseline |
| FoVer | TACL 2025 | 2025 | FV-Competitor |
| Snell et al. | ICLR 2025 | 2025 | TT-Baseline |
| Singhi et al. | COLM 2025 | 2025 | TT-Framework |
| Self-Certainty | NeurIPS 2025 | 2025 | TT-Baseline |
| SSV | 2501.16961 / IJCAI 2025 | 2025 | FV-Competitor |
| VERGE | 2601.20055 | 2025 | FV-Component |
| Grammars of Formal Uncertainty | NeurIPS 2025 | 2025 | FV-Component |
| MATH-VF | 2505.20869 | 2025 | FV-Adjacent |
| Safe | 2506.04592 | 2025 | FV-Adjacent |
| ThinkPRM | 2504.16828 | 2025 | TT-Baseline |
| RLV | 2505.04842 | 2025 | TT-Baseline |
| VG-Search | 2505.11730 / NeurIPS 2025 | 2025 | TT-Framework |
| ReProbe | 2511.06209 | 2025 | TT-Baseline |
| Optimal SC | 2511.12309 | 2025 | TT-Baseline |
| Scaling Gen. Verifiers | 2511.13027 / NeurIPS 2025 | 2025 | TT-Baseline |
| RASC | 2408.17017 / NAACL 2025 | 2025 | TT-Baseline |
| NL2FOL | 2405.02318 / IJCNLP 2025 | 2025 | FV-Component |
| ORM for Logic | EMNLP 2025 | 2025 | TT-Baseline |
| Trust but Verify Survey | 2508.16665 | 2025 | Survey |
| Autoformalization Survey | 2505.23486 | 2025 | Survey |
| VeriCoT | ICLR 2026 | 2026 | FV-Competitor |
| MAD-LOGIC | ICLR 2026 | 2026 | FV-Competitor |
| LogicReward | ICLR 2026 | 2026 | FV-Adjacent |
| MATP | ICSE 2026 | 2026 | FV-Competitor |
| FregeLogic | SemEval 2026 | 2026 | FV-Competitor |
| FoVer-PRM | ACL 2026 Findings | 2026 | FV-Adjacent |
| SEP | 2604.06485 | 2026 | FV-Parallel |
| Do LLMs Game Formalization? | 2604.19459 | 2026 | FV-Analysis |
| LINA | OpenReview 3BoCwZFRJX | 2026 | FV-Competitor |
| PRoSFI | 2603.29500 | 2026 | FV-Component |
| LogicAgent | 2026 | 2026 | Neurosymbolic |
| LSC | 2508.18395 / AAAI 2026 | 2026 | TT-Baseline |
| V1 | 2603.04304 | 2026 | TT-Baseline |
| Mixture-of-Thought | 2505.15817 | 2025 | Neurosymbolic |
| CISC | ACL 2025 Findings | 2025 | TT-Baseline |
