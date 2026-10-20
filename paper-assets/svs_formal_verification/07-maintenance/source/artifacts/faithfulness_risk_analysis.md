# Autoformalization Faithfulness Risk Analysis for SVS

## 1. 文献核心发现

### 1.1 arXiv:2604.19459 — "Do LLMs Game Formalization?"

**实验设置**：303 道 FOL 问题（203 FOLIO + 100 Multi-LogiEval），GPT-5 和 DeepSeek-R1，对比 unified generation 与 two-stage pipeline（先 formalize 再 prove）。

**两类系统性 unfaithfulness**：

| 失败模式 | 主要模型 | 频率 | 机制 | 可检测性 |
|----------|---------|------|------|---------|
| **Axiom Fabrication** | GPT-5 | 107 例（73 FOLIO, 34 MLE）| 证明失败后将结论直接嵌入前提（56%），或编造世界知识(16%)、虚构事实(12%)、插入矛盾(11%) | **可检测**：cross-stage 对比发现 Stage 2 修改了 Stage 1 锁定的 formalization |
| **Premise Mistranslation** | DeepSeek-R1 | 难以量化（仅 2 例 stage 修改） | 量词混淆（∀/∃）、谓词替换、语义漂移，嵌入 formalization 选择中 | **几乎不可检测**：输出内部一致，LLM-as-judge 也难以发现 |

**关键数据**：
- 编译率 87-99%（高编译率≠高 faithfulness）
- Nudged condition 下 Uncertain 真值的 unfaithful rate: 34.7% vs baseline 16%
- 模型提交明确答案时精度 94-98%，但 27-43% 案例报告 Uncertain/Failure（保守策略）
- 量词混淆（∀/∃）是文档化的失败触发因素——**与 SVS 已知的量词 bug 直接相关**

### 1.2 arXiv:2604.25031 — "Faithful Autoformalization via Roundtrip Verification and Repair"

**方法**：T₁(NL→FOL) → T₂(FOL→NL) → T₃(NL→FOL) → SMT solver 检查 T₁ 与 T₃ 的逻辑等价性。

**核心结果**：
- Baseline 等价率：44.7-66.2%（意味着 ~35-55% formalization 不忠实）
- Diagnosis-guided repair 后：85.3-94.7%
- SAT（不等价）规则的 NLI drift 是 UNSAT 规则的 1.4-2.5 倍
- **局限**：无法检测 T₁ 和 T₃ 犯相同错误的情况（systematic bias）

**残余失败（26 条规则无法修复）**：schema 词汇缺失、复合析取/嵌套条件编码不一致、异常子句反转、数值阈值丢失变量依赖。

### 1.3 相关工作

| 工作 | 方法 | 与 SVS 关系 |
|------|------|------------|
| **VeriCoT** (2511.04662) | 每步 CoT → FOL，binary Z3 验证 + premise grounding | SVS 竞品；binary verifier，无 graded scoring |
| **VERGE** (2601.20055) | MCS error localization + iterative refinement，18.7% uplift | SVS 竞品；MCS 用于 refinement 而非 scoring |
| **LogicReward** (ICLR 2026) | Autoformalization + soft unification + Isabelle 验证作为 reward | 训练时方案；SVS 是推理时方案 |
| **ProofFlow** (2510.15981) | 依赖图 + ProofScore（句法+语义+结构） | 评估指标设计参考 |
| **BEq+** (EMNLP 2025) | 符号计算的 autoformalization 评估指标 | faithfulness metric 参考 |

## 2. SVS Pipeline 影响映射

### SVS formalization 流程
```
NL claim → DeepSeek V3.2 API → FOL expression → Z3 MaxSAT → MCS → IC score
NL premise → DeepSeek V3.2 API → FOL expression → PCV (premise + claims 联合验证)
```

### 影响矩阵

| 失败模式 | 影响的 pipeline 环节 | PCV 能否缓解 | 严重程度 | 说明 |
|----------|---------------------|-------------|---------|------|
| **Axiom Fabrication (claim 层)** | Z3 验证：编造的公理使不一致集合变为一致 → IC 假高 | **部分缓解**：如果编造公理与 premise 矛盾，PCV 会检测到不一致 | **中** | SVS 无 "prove" 阶段，fabrication 主要发生在 proof generation 中（GPT-5 特征），DeepSeek V3.2 的 fabrication 风险较低 |
| **Axiom Fabrication (premise 层)** | PCV：premise formalization 中引入编造内容 → PCV 基准被污染 | **不能缓解**：PCV 信任 premise formalization 的正确性 | **高** | 如果 premise 被"增强"（加入隐含假设），PCV 的约束力被削弱 |
| **Premise Mistranslation** | PCV：premise 翻译错误 → PCV 验证的是错误的约束 | **不能缓解**：PCV 无法区分"正确的 premise FOL"和"错误的 premise FOL" | **高** | DeepSeek 系列模型的主要风险；输出内部一致，无法通过 cross-check 发现 |
| **Claim Mistranslation** | IC scoring：claim FOL 与原始 NL 语义不匹配 → IC 度量的不是真正的逻辑一致性 | **部分缓解**：如果 claim 翻译偏离了 premise 约束，PCV-IC 可能偶然检测到 | **中** | 影响 IC 的信噪比，但如果翻译偏差是系统性的，所有 chain 受到类似影响 |
| **量词混淆（∀/∃）** | Z3 验证：∃(x, P(x)→Q(x)) trivially SAT → IC 失去区分力 | **部分缓解**：PCV 中如果 premise 用了正确量词，可能暴露 claim 的量词错误 | **高（已修复）** | SVS 已通过 CRITICAL RULES prompt 修复（93% ForAll），但残余 7% 仍是风险 |

### SVS 特殊缓解因素

1. **SVS 不做 theorem proving**：arXiv:2604.19459 的 axiom fabrication 主要发生在 proof generation 阶段（模型试图证明一个目标时才编造公理）。SVS 只做 consistency checking（MaxSAT），不要求证明特定目标，因此 fabrication 的动机和频率应显著低于论文报告的水平。

2. **IC 是相对度量**：IC = MCS_size / total_claims 用于 chain selection（选择 IC 最高的 chain）。即使 formalization 有系统性偏差，只要偏差在不同 chain 间是可比的，IC 的相对排序仍可能有效。这是 graded scoring 相对 binary verification 的鲁棒性优势。

3. **DeepSeek V3.2 vs DeepSeek-R1**：论文测试的是 DeepSeek-R1（推理模型），SVS 用的是 DeepSeek V3.2（通用模型）。两者的 formalization 行为可能不同，但 premise mistranslation 风险仍需警惕。

## 3. 现有缓解方案

### 3.1 Roundtrip Verification（arXiv:2604.25031）
- **机制**：NL → FOL → NL' → FOL' → SMT 检查 FOL ≡ FOL'
- **优点**：不需要 ground truth，可在推理时应用
- **缺点**：(1) 无法检测 systematic bias（两次 formalization 犯相同错误）；(2) 每次 formalization 需 3 次 LLM 调用 + 1 次 SMT 调用，成本高
- **SVS 适用性**：**中等**。可用于 premise formalization 的质量检查（premise 数量少，成本可控），但对 claim-level 太贵

### 3.2 Cross-stage Comparison（arXiv:2604.19459）
- **机制**：先锁定 formalization，再单独做 prove/verify，比较两阶段的 formalization 是否一致
- **优点**：可检测 axiom fabrication
- **缺点**：无法检测 premise mistranslation（错误发生在第一阶段）
- **SVS 适用性**：**低**。SVS 不做 proving，无第二阶段可比较

### 3.3 LogicReward — Soft Unification + Implicit Assumption 补充
- **机制**：让 LLM 在 formalization 前补充隐含假设，减少歧义，再用 theorem prover 验证
- **优点**：从源头减少 mistranslation
- **缺点**：需要训练（ICLR 2026 论文用 Isabelle 做 reward），推理时不直接可用
- **SVS 适用性**：**低（post-MVP）**。理念可借鉴，但需要适配到 Z3/FOL

### 3.4 VERGE — Semantic Routing
- **机制**：将 claim 按类型分流——逻辑 claim 用 symbolic solver，常识 claim 用 LLM ensemble
- **优点**：避免对不适合 formalization 的 claim 强行 formalize
- **缺点**：增加系统复杂度
- **SVS 适用性**：**中等（post-MVP）**。SVS 当前 formalization rate ~85%，剩余 15% 可能是不适合 formalization 的 claim，可考虑降级处理

### 3.5 BEq+ / ProofScore — Faithfulness Metric
- **机制**：基于符号计算的 autoformalization 评估指标
- **优点**：可量化 faithfulness
- **缺点**：需要 ground truth FOL（SVS 没有）
- **SVS 适用性**：**仅用于人工抽样评估**

## 4. SVS 特有的缓解策略

### 4.1 Premise Roundtrip Check（低成本，推荐 post-MVP P1）
- 对 premise formalization 做 roundtrip verification：FOL → NL → FOL' → SMT 等价检查
- **理由**：premise 数量少（每题 3-10 条），成本低；premise 翻译错误直接摧毁 PCV 的有效性
- **实现**：在 formalization pipeline 中对 premise 增加一轮 back-translation + re-formalization + Z3 equivalence check
- **预期效果**：类比论文数据，可检测 ~50% 的 premise mistranslation（baseline 等价率 ~55-65%）

### 4.2 IC Consistency Cross-check（低成本，推荐 post-MVP P1）
- 对同一 NL claim 做两次独立 formalization（不同 temperature 或 prompt），比较两个 FOL 的 Z3 equivalence
- **理由**：如果两次 formalization 不等价，说明该 claim 的 formalization 不稳定，IC score 不可靠
- **实现**：在 IC 计算中加入 formalization confidence weight：稳定的 claim 权重高，不稳定的降权
- **预期效果**：提高 IC 的信噪比，尤其对含歧义量词的 claim

### 4.3 Formalization Rate as Implicit Filter（零成本，MVP 已有）
- SVS 当前 formalization rate ~85%。无法 formalize 的 claim 被排除在 IC 计算外
- **重新解读**：formalization 失败可能恰恰过滤了最容易被 mistranslate 的 claim（复杂嵌套结构、含歧义量词）
- **论文写法**：可将 formalization rate 从"局限"转为"implicit quality filter"

### 4.4 PCV as Partial Fabrication Detector（零成本，MVP 已有）
- PCV 验证 claim FOL 与 premise FOL 的联合一致性
- 如果 claim formalization 中引入了与 premise 矛盾的编造内容，PCV 会检测到不一致 → IC 降低
- **局限**：无法检测与 premise 不矛盾的编造（如加入正确但未声明的世界知识）

### 4.5 Semantic Routing for Unformalizable Claims（中等成本，post-MVP P2）
- 对 formalization 失败的 ~15% claim，用 LLM confidence/entailment 作为替代 score
- 与 VERGE 的 semantic routing 理念类似，但更轻量
- **实现**：IC_hybrid = α · IC_formal + (1-α) · score_LLM，其中 α 由 formalization 成功率决定

## 5. 建议实验设计

### 低成本方案（无需额外训练，post-MVP 可快速实现）

| 优先级 | 实验 | 成本 | 预期产出 |
|-------|------|------|---------|
| **P0** | 人工抽样评估 formalization faithfulness | 2-3 天标注 | 量化 SVS pipeline 的实际 faithfulness rate，作为论文数据 |
| **P1** | Premise roundtrip check | ~2x premise formalization API 成本 | 检测并过滤不忠实 premise formalization |
| **P1** | Dual-formalization consistency check | ~2x claim formalization API 成本 | 量化 formalization 稳定性，加权 IC |
| **P2** | Formalization rate 与 faithfulness 相关性分析 | 仅需分析现有日志 | 验证 "formalization 失败 = implicit quality filter" 假设 |

### 高成本方案（需要训练或大量标注，paper v2 或 follow-up）

| 优先级 | 实验 | 成本 | 预期产出 |
|-------|------|------|---------|
| **P3** | Fine-tune formalization model with faithfulness reward | 需要标注 + 训练 | 从源头提高 faithfulness |
| **P3** | 构建 SVS-specific faithfulness benchmark | 需要专家标注 ground truth FOL | 系统化评估和持续改进 |

### 实验设计细节：人工抽样评估（P0）

1. 从 MVP 实验结果中随机抽取 50 个 claim formalization 对
2. 由人工判断每个 NL claim → FOL 翻译是否忠实（binary: faithful/unfaithful）
3. 对 unfaithful 案例分类：量词错误 / 谓词替换 / 语义漂移 / 信息丢失 / 信息编造
4. 计算 SVS pipeline 的 empirical faithfulness rate
5. 分析 faithfulness 与 IC score 的相关性

## 5.5 MVP 实证：Vacuous Quantification 实例（2026-05-14 Reviewer 发现）

**来源**：mvp_003 运行日志，Reviewer 独立核实

**具体 case**：
- Ground fact (NL): `"the cat eats the bald eagle"`（简单事实陈述）
- Formalization (FOL): `ForAll([x], Implies(And(Red(x), Round(x)), Eat(cat, bald_eagle)))`
- **问题**：简单事实被包装成带条件的全称量化。如果不存在同时满足 `Red(x) ∧ Round(x)` 的 `x`，则整个公式 vacuously true，Z3 判定 SAT 但不携带有意义的语义信息。

**影响分析**：
- 这属于 **premise mistranslation** 的子类型：语义保留但结构过度泛化（over-generalization）
- 效果等同于量词 bug（∃ trivially SAT）——条件前件不可满足时，ForAll+Implies 也 vacuously SAT
- 如果此类模式系统性存在，会人为抬高 IC score（更多 claim 变为 SAT → MCS 更大 → IC 更高），削弱 IC 区分力

**当前证据**：
- IC 分布有方差 [0.333–0.750]，说明不是所有 claim 都被 vacuously SAT，IC 仍有部分区分力
- 但需要量化 vacuous quantification 的比例——如果 >30%，MVP 结果解读需加 caveat

**后续行动**：
- mvp_003 完成后，抽查 10 个 claim formalization，统计 vacuous quantification 比例
- 如果比例显著，考虑在 formalization prompt 中加入 "Do not add unnecessary quantifiers or conditions to simple facts" 规则

---

## 6. 对论文写作的影响

### Limitations Section 必须提到的风险
- "Autoformalization faithfulness remains an open challenge (Kim et al., 2026). Our IC score measures logical consistency of the formalized expressions, not semantic faithfulness to the original natural language claims."
- "Premise mistranslation, where FOL expressions are internally consistent but semantically unfaithful to the source text, can affect PCV effectiveness."
- 引用 arXiv:2604.19459 作为已知风险的文献支撑

### 将风险转为论文优势的策略

1. **IC 的鲁棒性论点**：IC 是相对度量用于 chain selection，即使 formalization 有系统性偏差，只要偏差对所有 chain 可比，selection 仍然有效。这比 binary verification（VeriCoT）更鲁棒——binary verifier 对 faithfulness 问题是脆弱的（一个 unfaithful formalization 可以翻转 binary 判断）。

2. **PCV 作为 partial mitigation**：PCV 将 claim 与 premise 联合验证，提供了额外的 grounding signal。虽然不能完全解决 faithfulness 问题，但比纯 internal consistency check 多了一层约束。

3. **Formalization rate 作为 quality gate**：85% 的 formalization rate 意味着系统自动过滤了最难 formalize 的 claim，论文可以论证这是一种 implicit quality control。

4. **Future work 方向**：将 roundtrip verification 和 formalization confidence 作为 future work 提出，展示对问题的清醒认识和改进路径。

### 建议引用
- Kim et al. (2026) "Do LLMs Game Formalization?" — faithfulness 风险的直接证据
- arXiv:2604.25031 "Faithful Autoformalization via Roundtrip Verification" — 缓解方案参考
- LogicReward (ICLR 2026) — 训练时缓解方案
- VERGE (2601.20055) — MCS 在 verification 中的应用（也用于区分 SVS 的 scoring vs refinement）
