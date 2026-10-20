# ProvUIE 文献验证报告

> 生成时间: 2026-05-12 | 方法: WebSearch 多轮验证

---

## 1. R2GRPO (arXiv 2505.22068)

**真实性: ✅ 已确认**

- **完整标题**: "Beyond Path Selection — Better LLMs for Scientific Information Extraction with MimicSFT and Relevance and Rule-induced (R²) GRPO"
- **作者**: Ran Li, Shimin Di, Yuchen Liu, Chen Jing, Yu Qiu, Lei Chen
- **提交时间**: 2025 年 5 月 28 日
- **链接**: https://arxiv.org/abs/2505.22068

**方法摘要**: 提出两阶段方法：(1) MimicSFT 用高质量 reasoning trace 做 SFT 冷启动；(2) R²GRPO 用两类奖励训练——Relevancy Reward 将模型引用的推理内容映射到 gold evidence 并施加长度惩罚 `Map(ci, evidence_gold) - λ·(len(ci)/len(x))²·I(len>threshold)`，Rule-induced Reward 衡量结构抽取正确性。基座模型 Qwen2.5-7B-Instruct，在 SciERC 上达到 84.36 NER F1、66.81 RE F1。

**IDEA_BRIEF 声称验证**:

| 声称 | 状态 |
|------|------|
| 论文存在，arXiv ID 2505.22068 | ✅ 准确 |
| 引入 relevancy + rule-induced rewards | ✅ 准确 |
| Relevancy reward 映射 reasoning trace 到 gold evidence + 长度惩罚 | ✅ 准确 |
| 84.36 NER F1, 66.81 RE F1 on SciERC | ✅ 准确 |

**与 ProvUIE 的关系**: R2GRPO 的 Relevancy Reward 是 ProvUIE 证据忠实度奖励的直接灵感来源。R2GRPO 仅限于 Scientific IE (SciERC)，ProvUIE 将此思路扩展到 Universal IE (NER/RE/EE) 并用 NLI entailment + IoU 替代简单映射函数。差异化成立，但必须在 Related Work 中充分 credit R2GRPO。

**审稿人担忧回应**: 三位审稿人称找不到此论文，但验证确认论文存在。可能原因：论文 2025 年 5 月底提交，审稿时可能尚未被索引收录。Rebuttal 中应提供直接链接。

---

## 2. ProUIE (arXiv 2604.10633)

**真实性: ✅ 已确认**

- **完整标题**: "ProUIE: A Macro-to-Micro Progressive Learning Method for LLM-based Universal Information Extraction"
- **作者**: 小米 + 西交利物浦大学
- **提交时间**: 2026 年 4 月
- **基座模型**: Qwen3-4B
- **链接**: https://arxiv.org/abs/2604.10633

**方法摘要**: 三阶段渐进训练：
1. **Complete Modeling (CM)**: 全数据 SFT，按任务难度排序 (NER→RE→EE)
2. **Streamlined Alignment (SA)**: 简化格式 SFT，prompt 要求"输出必须是输入的精确子串"
3. **Deep Exploration (DE)**: GRPO + SFR (Stepwise Fine-grained Reward)

**SFR 奖励维度（详细）**:

| 任务 | 粗粒度 | 细粒度 |
|------|--------|--------|
| NER | entity type coverage | type-entity pair F1 |
| RE | relation type coverage | head entity F1, tail entity F1, triple F1 |
| EE | event type coverage, trigger coverage | role-argument pair F1 |

**关键结论: SFR 不包含任何 evidence/provenance/faithfulness 维度。** 所有奖励组件衡量的都是结构抽取正确性（类型覆盖率 + 结构单元 F1）。"输出为输入子串"仅是 Stage II 的 prompt 指令，不是奖励信号。

**IDEA_BRIEF 声称验证**:

| 声称 | 状态 |
|------|------|
| ProUIE 使用 GRPO + SFR 分层奖励 | ✅ 准确（审稿人指出的也正确） |
| SFR 仅衡量 structural extraction correctness | ✅ 准确 |
| ProUIE "relies on prompt-level substring instructions without reward verification" | ✅ 准确——子串约束是 prompt 指令，不是奖励维度 |
| ProUIE 不含 evidence/provenance 奖励 | ✅ 准确 |

**与 ProvUIE 的差异化**: **成立。** ProUIE 的 SFR 奖励纯粹衡量结构正确性；ProvUIE 新增证据忠实度维度（NLI entailment + IoU）作为可学习奖励信号，这是 ProUIE 未触及的方向。但需注意措辞——不应说 ProUIE "没有 GRPO"（它有），而应精确说 ProUIE 的 GRPO 奖励不包含 provenance 维度。

---

## 3. EAPO (arXiv 2601.10306)

**真实性: ✅ 已确认（但不针对 IE）**

- **完整标题**: "Evidence-Augmented Policy Optimization with Reward Co-Evolution for Long-Context Reasoning"
- **作者**: Xin Guan 等 (阿里通义实验室)
- **提交时间**: 2026 年 1 月
- **链接**: https://arxiv.org/abs/2601.10306

**方法摘要**: 将 RL 优化从稀疏结果奖励转向密集的 evidence-augmented 监督。核心贡献是 Group-Relative Evidence Reward——由奖励模型打分的过程监督信号，惩罚无依据的"lucky guess"，显式引导 evidence extraction 质量。配合 Adaptive Reward-Policy Co-Evolution 机制迭代优化奖励模型。

**关键事实**: 
- ✅ 使用 evidence 作为 GRPO 风格的奖励信号
- ❌ **不针对 IE 任务**——评测在 8 个长上下文 QA/推理基准上
- 概念上高度相关（evidence as reward in GRPO），但应用领域不同

**与 ProvUIE 的威胁分析**: **低威胁，但必须引用。** EAPO 在长上下文推理中用 evidence reward，ProvUIE 在 UIE 中用 evidence reward，方向类似但任务域不同。Related Work 中应将 EAPO 作为"evidence-augmented RL"的先驱工作引用，并明确 ProvUIE 的区分：(1) 针对结构化 IE 而非 QA，(2) evidence 定义不同（span-level IoU + NLI vs. passage-level），(3) 无需额外奖励模型。

---

## 4. Ground-GRPO

**真实性: ❌ 不存在**

多轮搜索（"Ground-GRPO"、"grounded GRPO information extraction"等）均未找到以此命名的论文。搜索中出现的近似结果：
- **G2RPO-A** (arXiv 2508.13023): Guided GRPO，数学推理，非 IE
- **Scaf-GRPO** (arXiv 2510.19807): Scaffolded GRPO，推理任务，非 IE
- **GRPO for GUI Grounding**: 视觉 UI 定位，非 NLP IE

**结论**: "Ground-GRPO" 作为论文名称不存在。如果 IDEA_BRIEF 中引用了此论文，应删除或替换为实际存在的相关工作。

---

## 5. MORE-R1 (arXiv 2603.09478)

**真实性: ✅ 已确认（多模态 RE）**

- **完整标题**: "MORE-R1: Guiding LVLM for Multimodal Object-Entity Relation Extraction via Stepwise Reasoning with Reinforcement Learning"
- **作者**: Xiang Yuan 等
- **提交时间**: 2026 年 3 月 10 日
- **链接**: https://arxiv.org/abs/2603.09478

**方法摘要**: 针对多模态对象-实体关系抽取 (MORE)，两阶段：(1) 冷启动 SFT 用自动构造的分步推理数据；(2) GRPO + Progressive Sample-Mixing Strategy 渐进引入难样本。奖励基于抽取正确性（verifiable reward），不含 evidence provenance 维度。

**与 ProvUIE 的威胁分析**: **低威胁。** MORE-R1 是多模态（视觉+文本）RE，ProvUIE 是纯文本 UIE。任务域不重叠。Related Work 中可作为"GRPO for IE"的补充引用。

---

## 6. LAT

**真实性: ❌ 未找到**

搜索 "LAT information extraction"、"LAT GRPO"、"latent alignment training information extraction" 等均未找到匹配论文。"Latent alignment" 在近期文献中指 latent reasoning representation 对齐（如 CoLaR, CODI），与 IE 无关。

**结论**: "LAT" 作为 IE + GRPO 相关论文不存在。应从引用列表中删除。

---

## 7. 额外发现：需关注的相关工作

搜索过程中发现以下未在 IDEA_BRIEF 中提及但高度相关的论文：

### MR-UIE (arXiv 2509.09082) ⚠️ 高相关
- **标题**: "Multi-Perspective Reasoning with Reinforcement Learning for Universal Information Extraction"
- **方法**: 使用 RL + 复合奖励评估 correctness、**faithfulness** 和 efficiency。包含 "evidence-first" prompting 视角。
- **威胁**: **中等。** MR-UIE 已在 UIE 的 RL 奖励中纳入了 faithfulness 维度，这与 ProvUIE 的核心 novelty 存在重叠。需仔细对比其 faithfulness 定义与 ProvUIE 的 NLI entailment + IoU 有何区别。

### Extract-0 (arXiv 2509.22906)
- **方法**: 7B 模型用 GRPO + semantic-similarity reward 做文档 IE。
- **威胁**: 低。针对文档 IE，非 UIE 框架。

### R1-RE (arXiv 2507.04642)
- **方法**: 用 RLVR (非 GRPO) 做跨域 relation extraction。
- **威胁**: 低。仅做 RE，不含 evidence 奖励。

---

## 8. 总结与建议

### 文献真实性总结

| 论文 | 状态 | arXiv ID | 对 ProvUIE 威胁 |
|------|------|----------|----------------|
| R2GRPO | ✅ 存在，内容匹配 | 2505.22068 | 低（灵感来源，需 credit） |
| ProUIE | ✅ 存在，SFR 无 evidence 维度 | 2604.10633 | 差异化成立 |
| EAPO | ✅ 存在，非 IE 任务 | 2601.10306 | 低（概念相关，需引用） |
| Ground-GRPO | ❌ 不存在 | — | 应删除引用 |
| MORE-R1 | ✅ 存在，多模态 RE | 2603.09478 | 低（任务域不同） |
| LAT | ❌ 未找到 | — | 应删除引用 |
| **MR-UIE** | ✅ 存在，UIE + faithfulness reward | 2509.09082 | **中等（需重点对比）** |

### Novelty 立论评估

**ProvUIE 的核心差异化——在 UIE GRPO 奖励中加入 evidence faithfulness 维度——基本成立**，但需调整：

1. **ProUIE 差异化描述需精确化**: 不能说 ProUIE "没有 RL/GRPO"（它有），应说 "ProUIE 的 SFR 奖励仅覆盖结构抽取正确性，不包含 evidence provenance 维度"。
2. **R2GRPO 引用问题已解决**: 论文真实存在，审稿人找不到可能因索引延迟。Rebuttal 提供直接链接即可。
3. **删除不存在的引用**: Ground-GRPO 和 LAT 不存在，必须从文稿中删除。
4. **补充 MR-UIE 作为 Related Work**: MR-UIE 在 UIE RL 奖励中已有 faithfulness 维度，这是对 ProvUIE novelty 的最大潜在威胁。必须仔细阅读 MR-UIE 原文，对比其 faithfulness 定义（可能是 output-level consistency）与 ProvUIE 的 span-level NLI entailment + IoU 的区别，在论文中明确差异。
5. **补充 EAPO、Extract-0 作为 Related Work**: 完善 "evidence-augmented RL" 和 "GRPO for IE" 两条线的文献覆盖。

### 建议优先行动

1. **立即**: 阅读 MR-UIE (2509.09082) 原文，确认其 faithfulness reward 的具体定义，评估与 ProvUIE 的重叠程度
2. **立即**: 删除 Ground-GRPO 和 LAT 的引用
3. **论文修改**: 精确化 ProUIE 差异化描述（"SFR 不含 evidence 维度" 而非 "没有 GRPO"）
4. **Related Work 补充**: 加入 EAPO、MR-UIE、Extract-0、MORE-R1
