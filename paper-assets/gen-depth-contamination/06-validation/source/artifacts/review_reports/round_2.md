---
round: 2
overall_score: borderline accept
timestamp: 2026-05-16T02:25:37.561601+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 4 圆桌审稿（EMNLP 2026 Main）

**论文**: "Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary"
**Venue**: EMNLP 2026 Main Conference (ARR May 2026 cycle)
**截止日期**: 2026-05-25
**审稿日期**: 2026-05-16
**Reviewer 编排**: 2 人（R1 方法严谨性, R2 新颖性与完整性）
**外部审稿**: 未启用

---

## Summary

本文定义并测量了递归合成文本的世代深度判别边界 K*_empirical——使用 15 维统计特征 + OBD-LightGBM 分类器，在 θ=0.60 阈值下，跨 5 种模型配置（1B-7B）和 4 种解码策略，得出 K*=2 的一致结果。论文通过交叉模型迁移（80-92% retention）、交叉评分器验证（ρ>0.90）、neural probe、frontier LLM zero-shot 对比和下游 6 策略过滤实验，构建了多维度的证据网络。研究问题新颖（经验证无 prior work），实验系统性超出一般 empirical paper 标准，但核心声明的强度在若干关键节点超出了实验证据的支撑范围。

---

## Strengths

**S1. 问题定义新颖且经过验证。** 两位 Reviewer 独立确认：经广泛文献搜索（含 SemEval-2024 Task 8 Subtask B、Cheng et al. 2025、Mehta 2025 等），现有工作均未直接估计递归生成深度。"首次系统测量 K*_empirical" 的 novelty claim 成立。[R1-S1, R2-S1 一致]

**S2. 实验设计系统性强。** 5 种 model-mode 配置 × 4 种解码策略 = 9 条件；cross-scorer validation（Pythia + OLMo 对 Qwen 打分）独立验证 feature ranking 的 scorer-invariance；neural probe 和 frontier LLM zero-shot 从不同角度交叉验证 K*=2。Triangulation 设计远超一般 empirical paper。[R1-S2, R2-S2 一致]

**S3. 统计方法论整体严谨。** Bootstrap 95% CI + permutation test + McNemar exact test + Holm-Bonferroni 多重比较校正，统计报告优于该领域平均水平。GroupKFold CV 按 seed document 分组正确防止数据泄露。[R1-S3, R2-S3 一致]

**S4. 下游验证有 practical value。** Section 5 的 6 种过滤策略对比验证了 K*=2 的 actionability。Graduated filtering 随 α 增大单调收敛到 binary 的实验尤其有说服力——将理论测量转化为可证伪预测。[R1-S5, R2-S4 一致]

**S5. 与最近 prior work 区分清晰。** Related Work 将 Drayson 2025 描述为"our framework 在 K*=1 时的特例"，贡献边界明确。[R2-S5]

**S6. Limitations 异常诚实。** 9 个具体限制条件 + Extended Limitations，在 ARR 投稿中属高水准自我审视。Limitations 和 Ethics Statement 均已作为独立 unnumbered section 存在，符合 ACL 2023+ 格式要求。[R1-S6, R2-S6 一致]

---

## Weaknesses

### Must-Fix（Critical / Major，两位 Reviewer 交叉确认一致）

**W1 [Critical — 共识]. "confirms K*=2 as a data property" 过度声称。**
- 位置: Abstract, Section 6.1, Conclusion
- Abstract line 38 "confirming K*=2 as a property of the data"；Discussion 6.1 "confirms that the saturation is a property of the data"。
- 论证基础: McNemar p=0.081 (vs GPT-5.5), p=0.069 (vs Claude)——均 > 0.05，仅表示"未能拒绝无差异零假设"，不等于"确认等效"。Bootstrap 95% CI 为 [-0.4, +10.0]pp 和 [0.0, +10.2]pp（后者下界恰为 0.0）。N=500 检验力有限。
- Neural probe K*_neural=3 (Qwen) 直接证明 K* 是 representation-dependent（Section 4.5, Table neural_probe_crossmodel），与 "data property" 叙事矛盾。
- **建议**: 所有 "confirms" 改为 "provides converging evidence consistent with"；补充 TOST equivalence testing 或明确 N=500 的检验力限制。
- **来源**: R2-W1 Major → R1 [AGREE]；R1-W6 Major → R2 [AGREE]

**W2 [Critical — 共识]. K*=2 一致性窗口仅 2pp，"invariant" 表述掩盖边际性。**
- 位置: Abstract, Section 4.1, Conclusion
- Section 4.1 承认 "unanimous K*=2 holds only within θ ∈ [0.580, 0.600]"——2pp 窗口。
- Qwen-continuation 1v2 CI lower bound = 0.602，仅超 θ=0.60 0.2pp（Table 1）。
- Cross-scorer 下 Qwen-cont K* 直接从 2 降至 1（Pythia-scored 1v2 AUC=0.5923, OLMo-scored=0.5858; Table crossscorer）。
- 论文推荐 continuation 为 canonical mode，但 canonical 条件需特定评分器才能维持 K*=2。
- Abstract/Conclusion "invariant across all 9 conditions" 给读者留下 robustness 远强于实际的印象。
- **建议**: 加限定词，如 "K*=2 at θ=0.60 across all tested configurations under self-scoring, though Qwen-continuation is marginal (CI lower exceeds θ by 0.2pp) and drops to K*=1 under cross-scoring"。
- **来源**: R1-W2 Critical + R1-W3 Major → R2 [AGREE]；R2-W2 Major → R1 [AGREE]

**W3 [Critical — 共识]. self_BLEU 特征的 label leakage 风险未解决。**
- 位置: Table S5, Section 3.2
- `self_bleu` 定义为 "Mean 4-gram BLEU against 100 random same-depth samples"——需要深度标签。
- CV 信息泄露: 若在 GroupKFold 划分前在全数据集上预计算，测试折文档的 self_BLEU 依赖同折同深度文档。
- 部署不可行: 实际部署中文档深度未知，无法选取同深度参考集。
- 缓解因素: self_BLEU 不在任何配置 top-3 features 中（Table 3），影响可能有限。
- 论文未报告去除 self_BLEU 后的消融（14D ablation）——这在 Round 3 已被提出（FR-3），本轮仍未在论文中体现。
- **建议**: (1) 报告 14D ablation 结果; (2) 说明 CV 中 self_BLEU 精确计算流程; (3) 讨论部署替代方案。
- **来源**: R1-W1 Critical → R2 [AGREE，承认是遗漏的重要技术问题]

### Should-Fix（Major，有共识但 severity 有轻微分歧）

**W4 [Major — 共识]. 解码消融 Table S2 缺 bootstrap CI。**
- Table S2 报告 4 种解码配置的 AUC 点估计，但无 CI。Nuc p=0.9 T=1.0 的 2v3 AUC=0.5917 距 θ 仅 0.83pp——若 CI 上界超过 0.60，该条件 K* 应为 3。"all 9 conditions yield K*=2" claim 中有 4 个条件缺乏统计支撑。
- **来源**: R1-W4 Major → R2 [AGREE]

**W5 [Major — 共识]. Cross-scorer 验证矩阵不完整。**
- 仅在 Qwen 生成文本上进行（Table crossscorer），未测试 Pythia/OLMo 生成文本的 cross-scorer K*。
- **来源**: R1-W3 → R2 [AGREE]

**W6 [Major — 共识]. Continuation 128→256 结构性差异可能贡献 0v1 AUC。**
- Depth-0 = 256 human tokens; depth-1 = 128 human + 128 machine。结构性 composition 差异可能人为抬高 0v1 AUC (>0.96)，不纯是生成质量信号。Depth-1 vs depth-2 的 structural composition 相同（均为 128 human prefix + 128 machine），所以 1v2 discrimination 基于纯分布差异。论文未讨论此 confound。
- **来源**: R1-Q6 → R2 [AGREE，承认是遗漏的第二个重要问题]

**W7 [Minor-to-Major — 轻微分歧]. 缺少文本长度消融。**
- 所有实验固定 256 tokens，更长文本的 per-document 统计特征更稳定，K* 可能上移。不在 Limitations 9 条中。
- R1 评为 Major; R2 降级为 Minor-to-Major（认为 256 tokens 匹配 web-scale 常见 chunk，且 K* 定义本就是条件性的）。
- **来源**: R1-W5 Major → R2 [REBUT severity, AGREE substance]

### Nice-to-Fix（Minor / Info）

**W8 [Minor]. "mode > model" claim 缺正式统计检验。** 8.4pp (mode) vs 3.9pp (model) 差异明显但无 mode×model 交互效应检验。[R1-W7, R2 AGREE]

**W9 [Minor]. 下游过滤效应量小且设定理想化。** Binary-ours vs no-filter = +0.76pp MMLU。100% synthetic 远离真实场景。"~50% reduction" framing 可能过度强调。[R1-W8, R2 部分 AGREE]

**W10 [Minor]. Abstract "80-92% cross-model transfer" 缺 continuation-mode 限定。** Rewrite→continuation 仅 61-63%。[R2-W5, R1 AGREE]

**W11 [Minor]. CoDeC (Zawalski 2026) 被误归类为 AI text detection。** 实际是 data contamination detection (membership inference)。[R2-W4, R1 AGREE]

**W12 [Minor]. OBD 缩写不一致。** Section 3.2 "Ordinal Binary Decomposition" vs Table S6 "One-Boundary Distinguisher"。[R1-W9, R2 AGREE]

**W13 [Minor]. "9 conditions" 含非独立解码变体。** 4 个 decoding 均为 Qwen-rewrite 变体，真正独立条件仅 5 个。[R1 交叉回应]

---

## Reviewer Consensus（交叉确认一致）

以下问题两位 Reviewer 在独立审稿中分别发现，交叉分享后达成完全共识：

| 问题 | R1 | R2 | 交叉结果 |
|------|-----|-----|----------|
| K*=2 边界脆弱性 / θ 窗口仅 2pp | W2 Critical | W2 Major | **双方 AGREE** |
| "data property" overclaiming | W6 Major (neural probe) | W1 Major (McNemar) | **双方 AGREE** |
| Cross-scorer 下 Qwen-cont K*→1 | W3 Major | W2 包含 | **双方 AGREE** |
| self_BLEU leakage | W1 Critical | 遗漏→交叉 AGREE | **双方 AGREE** |
| Continuation 128→256 structural confound | Q6 | 遗漏→交叉 AGREE | **双方 AGREE** |
| "confirms" → "converging evidence" | 隐含于 W6 | W1 explicit | **双方 AGREE** |
| Qwen-7B Base vs Instruct unexplained | Q4 | Q3 | **双方 AGREE** |

## Reviewer Divergence

| 问题 | R1 | R2 | 备注 |
|------|-----|-----|------|
| 文本长度消融 severity | Major | Minor-to-Major | 实质同意，severity 轻微分歧 |
| LLM failure 论证力度 | 三方法交汇较强 | 两个 Transformer 共享 blind spot | R1 反驳 R2-W6，补充 OBD + binary detector 为非 Transformer；R2 未再反驳。**Director 判定**: R1 的反驳有理——三种方法论基础不同的方法（statistical features, autoregressive LLM, binary detector confidence）交汇失败，论证力度超过"共享 blind spot"，但仍不足以用 "confirms" |

---

## Questions（需作者澄清）

**Q1.** self_BLEU 的精确计算流程：参考的 100 个同深度样本是否排除 CV 测试折？部署场景（深度未知）如何处理？[R1-Q1]

**Q2.** Table S2 的 4 个解码配置是否有 bootstrap CI？Nuc p=0.9 T=1.0 的 2v3 AUC (0.5917) 的 CI 上界是否超过 0.60？[R1-Q2]

**Q3.** Cross-scorer validation 为何仅在 Qwen 生成文本上执行？Pythia/OLMo 生成文本在 cross-scoring 下的 K* 如何？[R1-Q3, R2 AGREE]

**Q4.** Qwen-7B 为何选 Base 而非 Instruct？其他 Qwen 配置用 Instruct，选 Base 引入不必要 confound。[R1-Q4, R2-Q3]

**Q5.** θ=0.60 选择是否存在 circularity？Filtering 使用的是 θ=0.60 下的分类器。若 θ=0.55（部分 K*=3），graduated filtering 是否可能优于 binary？这将削弱 "K*=2 correctly predicts strategy ordering" 的声明。[R2-Q1, R1 AGREE]

**Q6.** Neural probe K*_neural=3 (Qwen) 如何与 "data property" 叙事协调？如果存在能达到 K*=3 的表征，这暗示 K*=2 是 feature-set limitation 而非 data property。[R2-Q2, R1 AGREE]

**Q7.** 15D 特征集中移除 self_BLEU 后，K* 是否变化？整体分类性能下降多少？[R1-Q5]

---

## Missing References（两位 Reviewer 汇总）

**高优先级（与核心论点直接相关）:**
1. **Dohmatob et al. (2025). "Strong Model Collapse." ICLR 2025.** (arXiv:2410.04840) — 极少量合成数据即导致 collapse，模型规模可能放大 collapse。直接关乎 scale-invariance claim。[R2-W3, R1 AGREE]
2. **Wang et al. (2024). "SemEval-2024 Task 8."** — Subtask B (multi-class source attribution) 是最相关的 beyond-binary shared task。[R2, R1 AGREE]
3. **Gerstgrasser et al. (2024). "Is Model Collapse Inevitable?"** (arXiv:2404.01413) — Accumulate regime 下 collapse 可避免，与本文 replace regime 互补。[R2, R1 AGREE]

**中优先级（补充文献覆盖）:**
4. Guo et al. (2024), "Curious Decline of Linguistic Diversity" — LLM 文本多样性随迭代递减 [R1]
5. Briesch et al. (2023), "Large Language Models Suffer from Their Own Output" — 早期自退化研究 [R1]
6. Padmakumar & He (2024) — LLM lexical diversity contraction [R1]

**引用真实性**: 28 条引用全部通过 R2 核查（OpenAlex API + arXiv 手动验证），无幻觉引用。

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未启用（项目配置 `external_review.paperreview_ai.enabled = false`）

---

## Overall Assessment

**评分: Borderline Accept (3.5/5)**
**置信度: 4/5**

| 维度 | R1 | R2 | 综合 |
|------|-----|-----|------|
| Soundness | 3.5 | 3.5 | **3.5** — 实验设计系统性强，统计分析大部分严谨，但 self_BLEU leakage、θ 窗口脆弱性、解码消融缺 CI、"confirms" overclaiming 是实质缺陷 |
| Excitement | 3.5 | 3.5 | **3.5** — 问题新颖（经验证无 prior work），K*=2 有 practical actionability，但结果可能被视为 somewhat expected |
| Reproducibility | 4 | 4 | **4** — 超参数、数据集、pipeline 描述详尽；self_BLEU 计算流程和 prompt 模板缺失 |
| Overall | 3.5 | 3.5 | **3.5** — 介于 Findings 和 Main Conference |

**核心判断**:

论文提出了一个新颖且有意义的研究问题——递归合成文本的世代深度判别边界——并通过系统性的多维度实验（5 模型配置、4 解码策略、cross-model transfer、cross-scorer validation、neural probe、LLM baseline、downstream filtering）构建了有说服力的证据网络。K*=2 的核心发现在多个维度得到交叉验证，"one-wash laundering effect" 概念有洞察力且可 actionable。

主要问题是 **claim 强度与证据之间的 gap**：
1. "confirms data property" 基于 McNemar non-significance + 被 neural probe K*_neural=3 直接反例；
2. "invariant across all 9 conditions" 掩盖了最边际条件仅超 θ 0.2pp 且 cross-scoring 下降至 K*=1；
3. self_BLEU leakage 是 Round 3 遗留的技术债，至今未在论文中报告消融结果。

这些问题均可通过 **措辞修正（非实验重做）** 解决：将 "confirms" 改为 "converging evidence"，"invariant" 加边际性限定，补报 14D ablation。修正后论文有潜力达到 EMNLP Main Conference 水准。当前状态下，Findings track 更为稳妥。

**Must-Fix Action Items（投稿前必须完成）:**
1. 所有 "confirms...data property" → "provides converging evidence consistent with"
2. Abstract/Conclusion "invariant" 加 marginal boundary hedge
3. 报告 14D ablation（去 self_BLEU）结果 + 说明计算流程
4. 补 Table S2 解码消融的 bootstrap CI
5. 讨论 continuation 128→256 structural confound
6. CoDeC 引用分类修正
7. 补充 Dohmatob 2025 "Strong Model Collapse" 等遗漏引用

---

## Detailed Comments（按论文节次）

### Abstract
- "confirming K*=2 as a property of the data" → 改为 "consistent with K*=2 as a data property"
- "80-92% cross-model transfer" → 加 "among continuation-mode generators"
- "invariant across all 9 conditions" → 加 "under self-scoring" + marginal boundary note

### Section 1 (Introduction)
- Line 11: CoDeC 移出 binary detection 列表
- Prompt-chain vs retrain-chain 区分已改善（line 7），本轮无新问题

### Section 3 (Method)
- Eq. 1: CI lower bound 仅超 θ 0.002 即声明 K*=2——考虑讨论是否需要 minimum margin
- self_BLEU 计算流程（Table S5）需补充 CV 泄露防护说明
- OBD 缩写统一为 "Ordinal Binary Decomposition"（Section 3.2 vs Table S6 冲突）

### Section 4 (Experiments)
- Section 4.1: "all 9 conditions" 应明确为 "5 independent model-mode + 4 decoding ablation variants"
- Section 4.2: cross-scorer 仅测 Qwen 生成文本，需补充或声明限制
- Section 4.4: "mode > model" (8.4pp vs 3.9pp) 可加 descriptive qualifier
- Section 4.5: neural probe K*_neural=3 的解读应与 "data property" claim 取得一致
- Section 4.6: 正文表述扎实，无新问题

### Section 5 (Filtering)
- Holm-Bonferroni 已补，统计处理本轮无新问题
- "~50% reduction" 加 "in this 100% synthetic upper-bound setting" caveat
- DSIR 对比公平性可讨论（bigram features 本身信息量低于 15D）

### Section 6 (Discussion)
- Section 6.1: "confirms" 是最重要的措辞修正位置
- Section 6.4: "Representation Dependence" 标题与 "data property" 叙事的张力需要在正文中 reconcile

### Conclusion
- 同 Abstract：加限定词

### Limitations
- 补充文本长度敏感性讨论
- 9 个限制条件已很全面，本轮新增不多

### Appendix
- Table S2: 补 bootstrap CI
- Table S3: Claude Opus 4.6 N=499（非 500），解释缺失 1 sample
- Table S6: OBD 缩写修正