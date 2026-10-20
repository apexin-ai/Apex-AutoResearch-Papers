---
round: 20
review_mode: fresh
overall_score: 3.0 Findings
timestamp: 2026-05-23T02:17:17.314427+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 20 审稿报告 — OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints

**Venue**: EMNLP 2026 (ARR May 2026) | **Deadline**: 2026-05-25 | **Format**: Long paper, 8-page limit

---

## Summary

OntoCoDec 将 IE 本体约束编译为可组合的 token-level 解码约束，设计了两层架构：grammar layer（基于 XGrammar 的 CFG 编译）保证 JSON 结构和词汇表合法性，semantic layer（运行时状态化 token masking + 动态 entity registry）执行 domain/range 类型约束。通过可判定性分析（Proposition 1）论证了两层的理论动机。在 SciERC、DocRED、WikiEvents 三个数据集上跨 3 个 8B 模型和 1 个 70B 模型进行了 zero-shot 和 LoRA fine-tuning 评估。核心结果：LoRA + greedy S1 下 DR < 0.1%，R-F1 41–47%；beam search (k=4) 消除所有 violation 类型但代价 1.54× latency。

---

## Strengths

**S1. 问题定义和分析框架优秀。** 四类 violation 分类法（DR/CF/RV/ET）定义清晰，三层可判定性分类（context-free / prefix-decidable / non-local）超越具体系统，为约束解码研究提供了有价值的概念工具。[R1, R2 共识]

**S2. 评估覆盖面在同类工作中罕见。** 3 数据集 × 3+ 模型 × 2 任务 × zero-shot/fine-tuned × beam/greedy，加上完整消融、bootstrap CI、Bonferroni correction、power analysis、cross-seed variance、order invariance 验证、GCD-equivalence baseline、70B 验证——系统性远超同类论文。[R1, R2 共识]

**S3. 对自身局限性异常诚实。** Limitations section 详细量化 CF trade-off、scale-dependent behavior、parse failure increase、quantization impact 等问题，未回避 uncomfortable results（如 well-calibrated model 上 S1 引入 up to 12.02% CF）。[R1, R2 共识]

**S4. 工程完整性和实用性强。** 从 ontology 自动编译约束、tokenizer-agnostic（BPE + SentencePiece）、order-invariant、runtime overhead 仅 10–13%（greedy）/ 54%（beam k=4）、scalability 验证至 200 entity types / 1,000 relations。Fine-tuning composability 证明约束解码与 LoRA 正交可组合，解决重要实际问题。[R1, R2 共识]

**S5. Proposition 1 + Pumping Lemma 证明为两层架构提供清晰理论动机。** 虽然形式化了已知直觉，但与 Remark (finite entity sets) 的区分展现了理论 impossibility vs 工程 intractability 的 nuanced 理解。[R2 S4, R1 部分认可]

---

## Weaknesses

### Must-Fix（影响接收决定）

**MF1. [CRITICAL] 正文超出 8 页限制（回归问题）** [R2-N1]
§7 Discussion and Conclusion 溢出至 page 9（约 13 行），`\clearpage` 后 Limitations 从 page 10 开始。EMNLP 2026 strict 8-page limit。此问题在 Round 15 首次发现、Round 18 标记为 resolved，但本轮回归。格式违规可能导致 desk reject。
- **Action**: 压缩 §7（当前约 150 词可压至 100 词）或从 §5/§6 回收空间。

**MF2. [CRITICAL] CF trade-off 在 Abstract/Introduction 中 framing 偏乐观** [R1-N2, R2-N2 共识]
(1) S1 在 SciERC ZS 上将 CF 从 0.08% 提升到 9.90%（124× 增幅），Llama DocRED 从 0.17% 到 12.02%（70×）。§5.1 的 "violation conversion" 聚合隐含 DR≈CF 可比性，但论文自身承认两者性质不同。(2) Abstract "CF remains ≤1.4%" 未充分强调 CF 是系统引入的——Qwen unconstrained CF=0，S1 后 CF=1.18%。(3) "reaches zero with beam search" 未提及 1.54× latency 代价和 fine-tuned 前提。此问题从 Round 15 持续至今，上轮 resolution（修改 Abstract 表述）被两位 Reviewer 认为不充分。
- **Action**: (1) Abstract 明确 CF 是 DR enforcement 的 side effect；(2) §5.1 讨论 DR-CF severity 不对等性及下游场景依赖；(3) "violation conversion" 框架增加 caveat。

**MF3. [CRITICAL] "Enabling dependency" 的 Corollary 标签混淆形式/经验 + scale sensitivity 在主文讨论不足** [R1-N1, R2-N3 共识]
(1) §3 "Corollary" 前半句从 Proposition 1 逻辑推出（CFG 无法执行 level 2），后半句（semantic-only 24% DR reduction）是经验观测——标签暗示两者都是形式推导。(2) 70B semantic-only 达 84% DR reduction vs 8B 24%，直接动摇 "两层缺一不可" 核心叙事。Introduction 仅以括号形式提及这一 scale sensitivity，给读者的 first impression 是两层缺一不可。§4 讨论了 scale-sensitivity 但未回溯更新 §3 框架。
- **Action**: (1) 将 "Corollary" 重新标记为 "Empirical Observation"；(2) 在 §3 即明确 dependency 强度 scale-dependent；(3) Introduction 显著讨论 scale sensitivity，限定为 "for 8B-class models" 或 reframe 为 "complementary layers with scale-dependent relative contribution"。

### Should-Fix（影响评分但不一票否决）

**SF1. κ̄ (constraint tightness) 仍过度展示** [R1-W1]
n=3 schemas, p=0.138 不显著。上轮已从 §5.2/§7/Limitations 中删除，但 §4 仍占一整段且在 abstract 中出现。

**SF2. 70B 验证仅覆盖单模型 + AWQ INT4 量化效应未隔离** [R1-W2, R2 部分同意]
连续 7 轮提出（R14 起）。Limitations 有 disclaimer 但缺实证。单模型不足以支撑 "70B-class validation" 泛化声称。

**SF3. Proposition 1 证明中 position-based → name-based 转换缺形式论证** [R1-W3]
Appendix O 承认 "core argument transfers" 但未给出形式证明。结论正确（name-based strictly harder）但论证不完整。

**SF4. DocRED 评估使用 dev set，超参数选择过程未披露** [R1-W4]
LoRA 训练使用 training examples，评估使用 998 dev documents，未说明超参数是否基于 dev set 调优。

**SF5. Bonferroni 校正后 min p=0.014 处于 borderline** [R1-W5]
4 配置 Bonferroni 阈值 0.0125，min p=0.014 刚好未通过。各配置独立 p 值和效应量未披露。

**SF6. 新颖性天花板：系统集成而非算法创新** [R2-W1, R1 部分认可]
Grammar layer 复用 XGrammar，semantic layer 是 continuation masking 直接实现，Proposition 1 形式化已知事实。论文已诚实定位为 "systematic engineering contribution"（§7），但这也限制了 excitement ceiling。与 PICARD 的区别（"rejection-based vs constructive forward masking"）更多在 IE-specific dynamic entity registry 而非 masking 方向性。R1 Excitement 3.5/5 vs R2 2.5/5——分歧属于 reviewer judgment。

**SF7. 主文 Related Work §6 过于精简，ADELIE 缺失** [R2-W2]
§6 仅 ~0.5 页，大量推迟至 Appendix B。ADELIE (Cheng et al., EMNLP 2024) 完全缺失；PICARD 对比仅一句。

**SF8. Running example 仍不充分** [R2-W3]
§3.3 有 Used-for 示例（R19 修复），但缺乏贯穿 §3-§4 展示两层协同约束全过程的完整 running example。

**SF9. Zero-shot 评估实际意义有限** [R2-W4]
R-F1 仅 4–8%，模型基本无法完成 IE 任务。约束改善 violation rate 的实际价值有限。论文定位为 "diagnostic probe" 合理但篇幅仍偏多。

**SF10. Abstract 信息密度过高** [R1 minor, R2-W5]
~180 词含 ≥15 个数字、6 个缩写、section 引用。建议精简至 2-3 个 headline 数字。

---

## Reviewer Consensus [AGREE]

| 问题 | R1 | R2 | 共识 |
|------|----|----|------|
| CF trade-off framing 偏乐观 | N2 (critical) | N2 (critical) | ✅ 完全一致 |
| Enabling dependency scale sensitivity | N1 (critical) | N3 (critical) | ✅ 完全一致（不同角度同一问题）|
| 评估系统性和全面性 | Strength | Strength | ✅ 完全一致 |
| 诚实的局限性讨论 | Strength | Strength | ✅ 完全一致 |
| 工程实用性 | Strength | Strength | ✅ 完全一致 |
| Abstract 密度过高 | Minor | W5 | ✅ 一致（严重度略有差异）|
| κ̄ 统计支撑不足 | W1 | 提及 | ✅ 方向一致 |

## Reviewer Divergence [分歧]

| 问题 | R1 | R2 | 分析 |
|------|----|----|------|
| 正文超页 | 未提出 | N1 (critical) | R2 正确——PDF 客观显示 §7 溢出至 page 9。R1 可能因聚焦方法/实验而忽略格式检查。采纳 R2 判断。|
| Excitement | 3.5/5 | 2.5/5 | R1 更看重可判定性分析框架的概念贡献，R2 更注重算法新颖性。两者都是合理视角——最终取决于 reviewer 对 "systems contribution" 的接受阈值。|
| Overall 评分 | 3.5 (Borderline Conf.) | 3.0 (Findings) | 差异主要来自 Excitement 维度。|

---

## Questions for Authors

**Q1.** [R2-Q1] Qwen unconstrained CF=0, S1 后 CF=1.18%。如果目标用户已用 well-calibrated model + LoRA，OntoCoDec 的 net benefit 是什么？是否有 downstream task（KG construction）实验量化 violation 减少的实际价值？

**Q2.** [R2-Q2] Proposition 1 证明了 unbounded entity set 下 cross-field constraints 非 CF，但 Remark 承认 finite entity set 下语言是 regular 的。Registry-based approach vs 大 DFA 的优势是 theoretical intractability avoidance 还是 practical engineering convenience？

**Q3.** [R2-Q3] 70B semantic-only 84% vs 8B 24%——是否有中间规模（13B, 32B）的 scaling curve？如果 enabling dependency 连续变化，论文 architectural contribution 是否应 reframe？

**Q4.** [R1-Q1] 33/36 residual DR violations 来自 Llama DocRED（92%）——是否暗示 Llama 在 DocRED entity typing 的系统性问题？

**Q5.** [R1-Q3] Beam search k=4 消除全部违规基于 single-run——是否有多次运行方差估计？

**Q6.** [R2-Q4] S2 在 70B 上 R-F1 下降 8.45pp 的 root cause 是什么？

---

## Missing References

1. **ADELIE** (Qi et al., EMNLP 2024) — "Aligning Large Language Models on Information Extraction"。近期 schema-aware IE 代表工作，应在 §6 讨论。[R2]
2. **SGLang** (Zheng et al., 2024/2025) — XGrammar 的主要部署框架，值得提及。[R2]
3. **Tam et al. (2024)** "Let Me Speak Freely" — format constraints 对 LLM reasoning 的影响，与 CF/DR trade-off 直接相关。[R1]

（DCCD, Thinking Before Constraining, CRANE, IterGen 已被引用。）

---

## External Review (Stanford Agentic Reviewer)

未配置，跳过。

---

## Visual Layout Check（非评分项）

视觉审查 Agent 超时（300s 后 timeout），未产出有效 findings。用户可重新触发 `dispatch_visual_check`。

---

## Overall Assessment

**综合评分: 3.0 (Findings)**
**评分范围: R1 3.5 (Borderline Conference) — R2 3.0 (Findings)**
**置信度: 4/5**

### 评分理由

**支持 Findings 接收：**
- 评估系统性和全面性在同类工作中突出（3 datasets × 3+ models × 2 tasks × full ablation matrix）
- Violation taxonomy 和可判定性分类法对社区有参考价值
- 工程贡献实用——自动编译、tokenizer-agnostic、低 overhead、composable with LoRA
- 诚实的局限性讨论提升了科学可信度

**未达 Conference (4.0) 的主要原因：**
- **新颖性有限**：核心是 XGrammar + entity registry masking 的系统集成，非新解码算法
- **CF trade-off 未解决**：方法将 DR 转化为 CF（well-calibrated models 上 CF 从 0→1.18%），beam search 可解决但代价 1.54× latency
- **Enabling dependency 的 scale sensitivity** 动摇了两层架构作为普适设计的 claim——70B 时 semantic layer 独立达 84% DR reduction
- **正文超页** 需立即修复（格式违规）

**与 Borderline Conference (3.5) 的距离：**
如果作者能 (1) 修复正文超页，(2) 更诚实 frame CF trade-off（特别是 Abstract），(3) 重新定位 enabling dependency 为 scale-dependent 而非 universal，(4) 提供 downstream task impact 评估，评分可能上调至 3.5。这些修改在 ARR revision 周期内可行。

---

## Detailed Comments（逐节）

**Abstract**: 信息密度过高（≥15 数字），CF 表述偏乐观，κ̄ 细节应移除。建议精简至 2-3 个 headline 数字。

**§1 Introduction**: Gap-bridge 叙事清晰。贡献列表第 2 项的 70B 例外仅以括号提及，应更显著。"violation conversion" 概念首次出现应附 caveat。

**§2 Background**: 简洁有效。Problem Statement 清晰。

**§3 Method**: Corollary 标签应改为 Empirical Observation。Running example (§3.3 Used-for) 存在但不足以覆盖完整的两层协同约束流程。Continuation masking vs token masking 术语关系需首次使用时明确。

**§4 Constraint Composition**: κ̄ 分析有概念价值但 n=3 统计效力不足，应标注 preliminary。Grammar-first fallback 的 CF↔DR trade-off 刻画清晰。

**§5 Experiments**: 消融设计合理。Bonferroni 校正 borderline (min p=0.014 vs 阈值 0.0125)，应报告各配置独立 p 值。"violation conversion" 框架需加 DR-CF severity 不对等 caveat。WikiEvents (n=20) 标注 Preliminary 合理但 power analysis 应在主文 prominently 引用。DocRED dev set 超参数选择策略需说明。

**§6 Related Work**: 过于精简（~0.5 页）。ADELIE 缺失；PICARD 对比应展开 2-3 句。

**§7 Discussion and Conclusion**: 溢出至 page 9（must fix）。内容本身定位准确——"systematic empirical framework rather than novel decoding algorithm"。

**Limitations**: 质量远超平均水平，逐项量化每个已知问题。CF downstream propagation 和 quantization impact 可进一步展开。

**Appendix**: ~25 页，内容详实（prompts, case studies, power analysis, scalability, order invariance, pumping lemma proof）。Proposition 1 的 position→name 转换在 Appendix O 需补充形式论证。