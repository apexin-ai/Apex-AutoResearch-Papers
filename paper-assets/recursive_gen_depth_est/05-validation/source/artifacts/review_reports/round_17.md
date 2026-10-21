---
round: 17
review_mode: fresh
overall_score: 3.0 - Findings
timestamp: 2026-05-25T21:45:34.036982+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 20 审稿报告

**Venue**: EMNLP 2026 (via ARR)
**Reviewers**: R1, R2 | 交叉回应完成 | 2 轮（初审 + 交叉）收敛

---

## Summary

本文研究递归生成文本的深度估计问题——判断一段文本经历了多少代 LLM 递归重写。作者构建了 3×3 atlas（3 个 1–1.5B 模型 × 3 种解码策略 × 6 个深度层），提取 19 个统计特征（含 12 个基于参考模型的困惑度类特征），使用随机森林分类器进行 4-class ordinal 分类，并提出 Effective Discriminable Depth (EDD) 指标量化可区分深度。主要发现：(1) 在已知模型-策略配置下，1–1.5B 规模深度估计达 78.5% 准确率，EDD₀.₇₀ ≥ 3 覆盖 8/9 cells；(2) 困惑度尾部统计量族主导分类性能；(3) d0（人类文本）高度可分（AUC > 0.98）。

两位 Reviewer 独立初审后完成交叉回应，关键问题充分收敛。核心共识：**论文在 1–1.5B 受控设定下的实证工作扎实，但多处 claim 系统性地超出证据支撑范围。**

---

## Strengths

**S1. 任务定义与问题建模**
首次将递归生成深度估计形式化为序数分类问题（§3.1），从"检测 AI 文本"扩展到"区分不同递归代数"。问题定义具有前瞻性——随着 LLM 生成文本回流训练数据，web 文本的递归深度将成为数据质量的重要维度。

**S2. 系统化 Benchmark 设计**
3 模型 × 3 策略 × 6 深度的 atlas 设计（§3.2–3.3）覆盖了关键实验维度。每个 cell 独立训练递归链、独立提取特征、独立训练分类器，避免跨 cell 数据泄漏。

**S3. EDD 指标的设计理念**
EDD 的 contiguous prefix 约束（Definition 1, §3.4）要求从 (0,1) 到 (d−1,d) 连续超过阈值——比简单的 max AUC 或 mean AUC 更保守但更有信息量。与 model collapse 理论中 per-step signal attenuation 的对接（§3.5）为指标提供了理论锚点。

**S4. 特征分析深度**
Group-level ablation（§4.2: perplexity family 单独 76.85% vs. full 78.45%）、CPI（B.3）、SHAP（B.4）、permutation importance 四种方法交叉验证，group-level 结论在所有方法下一致收敛。

**S5. d0 分离鲁棒性**
d0 vs. d1 在所有 9 cells 中 AUC > 0.98、recall > 97%（§4.1），在 cross-model（Table 18）和 cross-domain（B.26 arXiv ~74%）场景下保持强信号。对 AI 文本检测有直接实用价值。

**S6. 附录实验的广度**
Appendix 包含 cross-model（B.17–18）、cross-reference（B.19, B.22）、partial mixing（B.8）、prompted generation（B.23）、PLM baseline（B.13）、ordinal methods（B.25）、arXiv domain（B.26）等实验，展现系统性探索。

---

## Weaknesses

### Must-Fix

**W1. [Critical] "解码策略贡献至少与模型架构相当" 的 claim 无统计支撑**
§4.1 (p.5) 声称 "mean within-model strategy gap is 9.3 pp, comparable to the 7.2 pp mean within-strategy model gap; decoding strategy contributes at least as much as model family to performance variance"。此 claim 基于 3×3=9 cell 均值比较，2.1 pp 差异在如此小的样本上无任何统计效力。论文未进行 permutation test、bootstrap test 或任何假设检验。然而该 claim 在 Introduction (p.2) 被列为三大发现之一，证据强度与突出程度严重不匹配。
[R1 AGREE R2-N1，完全共识]

**W2. [Critical] Scale generalization 证据薄弱且自相矛盾**
论文在 Abstract 将 "signal attenuates with scale" 列为第三个 finding，但支撑证据：
- 7–8B 仅 2 个模型且行为矛盾（Llama-3.1-8B 单调衰减 vs. Qwen2.5-7B U 型恢复，B.19–20）
- 14B 仅 1 个模型，EDD₀.₇₀ 在 self-reference 下为 0，cross-reference 下为 2（B.19, Table 22）——同一文本更换 reference model 即产生 EDD 从 0 到 2 的跃变
- Qwen2.5-7B 的 U 型 AUC（d0v1=0.969, d2v3=0.709, d4v5=0.772）与 §3.5 per-step signal attenuation 理论矛盾，论文自行归因于 "cross-reference setup"（B.19），由此整个 7B+ scale 分析均受 reference model confound 污染
此 "finding" 最多为 "preliminary observation"。
[R1-N3 AGREE, R2-N2 AGREE, R2-N3 AGREE，完全共识]

**W3. [Critical] Full-replacement 假设与真实场景的根本性鸿沟**
Introduction 以 "web text containing their own outputs" 为动机，暗示对真实 web-scale 递归污染的适用性。但实验采用 100% replacement chain，partial mixing 仅覆盖 3/9 cells × 2 比例（25%, 50%）。50% mixing 下 GPT-2 XL 已失败（d2v3 AUC=0.695 < T=0.70），已测 3 cells 中 33% failure rate。最贴近真实场景的 5–10% 比例区间完全未测试。Limitations (p.9) 仅一句话带过。
[R1-N2 AGREE, R2-N3 AGREE，完全共识]

**W4. [Critical] Reference model 依赖限制结论的内在有效性**
19 个特征中 12 个依赖 Pythia-1.4B 作为 reference model。Pythia-1.4B 自引用优势 4–11 pp（B.17, Table 18）。14B 实验中 EDD 随 reference model 剧烈波动。

R2 提出重要缓解论据：主 benchmark 6/9 cells 为 cross-reference 设定且表现良好（62.4–85.9%），表明 depth signal 存在 intrinsic component——B.22 cross-reference control 中 d0-vs-d1 AUC 仍达 0.697。R1 认为 confound 贯穿全部实验。

**Director 判定**：14B scale 下 confound 不可忽视（Critical），1–1.5B 主 benchmark 中 cross-reference 的成功部分缓解了此问题。但论文未在正文充分讨论这一依赖的部署含义——12/19 特征绑定特定 reference model 对实际应用构成根本限制。
[R1-N1, R2 部分 AGREE：14B critical, 1–1.5B mitigated]

### Should-Fix

**W5. [Major] 特征多重共线性下个体排名叙事过强**
VIF > 10 覆盖 14–16/19 个特征（§3.3），个体排名 CI width 2.7–3.7。§4.2 叙事如 "p90_ppl and var_surprisal are consistently prominent" 基于不可靠的个体排名。

R2 提出有力缓解论据：group-level ablation + CPI + SHAP + permutation importance 四方法交叉验证，group-level 结论（困惑度尾部族主导）在所有方法下一致收敛。CPI 专为处理 correlated features 设计。即使个体排名不稳定，四种方法 top-group 同时失效的概率极低。

**Director 判定**：采纳 R2 论据，从 R1 的 Critical 降为 Warning。Group-level 结论成立，但个体特征的因果叙事应删除或弱化。
[R1-N4 Critical → R2 REBUT → Director 降为 Warning]

**W6. [Major] 多重比较未统一校正**
9 cells × 3 相邻深度对 = 27 次 AUC 测试，加上 feature ranking permutation test 等总量远超 50。脚注 5 "exploratory" 声明与正文 "signal persists in all 9 cells"、"depth 0 recall exceeds 97% in all 9 cells" 的 confirmatory 语气不匹配。建议对 27 次 depth-pair AUC 应用 Benjamini-Hochberg FDR correction——核心结论大概率不受影响，但 d2-vs-d3 borderline cases（特别是 GPT-2 XL top-k, EDD < 3）可能在 correction 后需调整措辞。
[R1-N5, R2 AGREE，完全共识]

**W7. [Major] PLM baseline 比较信息不对等**
B.13 PLM baseline 仅用 frozen CLS + linear probing（DeBERTa-v3-base 64.5%, RoBERTa-base 59.5%），这是已知最弱的 PLM adaptation 方式。RF 使用 12 个基于 reference model 的 token-level perplexity 特征，PLM 仅看原文 CLS embedding——二者信息输入不对等。§6 "end-to-end PLMs lag RF by 14–33 pp" 的 claim 可信度取决于 baseline 是否足够强。论文自身在 B.13 末尾承认 "whether larger PLMs can close the gap remains an open question"。
[R1 AGREE R2-W2，完全共识]

**W8. [Major] LoRA 作为递归训练代理的系统性偏差**
所有递归链使用 identical LoRA 配置（r=16, α=32, 3 epochs, Table 5）。LoRA 低秩约束可能系统性压缩相邻深度间的分布偏移幅度，导致 EDD 值为 LoRA-specific。未测试 r=4/r=64 对 depth signal 的影响。真实递归污染中训练方法异质（full fine-tuning, RLHF, distillation 等）。
[R1 AGREE R2-W4，完全共识]

**W9. [Warning] Seed corpus 仅 Wikipedia**
全部 atlas 基于 Wikipedia seed。arXiv 跨域下降约 4 pp（B.26: 74.1% vs. ~78%），但 arXiv 仍属学术/百科文体。未测试对话（Reddit）、创意写作（fiction）、代码等 far-domain 场景。
（注：R1 修正了 R2 初审中 "14 pp+" 的说法——实际 cross-domain 降约 4 pp，R2 混淆了 cross-domain 和 cross-model transfer。）
[R1 AGREE R2-W3，数字修正后共识]

**W10. [Warning] BOS seeding artifact**
BOS-seeded generation 与 prompted generation 差 13.8 pp（B.23），暗示深度信号部分源于 BOS seeding 特异性而非递归本身的分布偏移。
[R1-W2, R2 AGREE]

**W11. [Warning] 跨策略迁移有效性有限但 framing 过度**
Leave-one-out 4-class accuracy 45.95%（1.84× chance, §5.2）。Two-stage pipeline 恢复至 59.1%（+13.15 pp）。R2 指出论文未将 cross-strategy 作为主要贡献，这是合理的。但标题 "Statistical Fingerprints" 暗示的可迁移性与实证矛盾——fingerprint 在 forensics 文献中蕴含唯一性和跨条件稳定性。
[R1-W3, R2 部分 REBUT，分歧收窄为 framing 问题]

### Minor

**W12. [Info] EDD 阈值 T=0.70 迁移缺理论论证**
Hosmer & Lemeshow (2000) 的 0.70 标准源自 binary logistic regression，移植到 ordinal pairwise AUC 无理论桥梁。Sensitivity analysis（T ∈ {0.65, 0.70, 0.80}）部分缓解。建议正文明确 T=0.70 为 operational choice。
[R1-W1, R2 AGREE]

**W13. [Info] §3.5 "Theoretical Motivation" 内容为经验观察**
Section 标题 "Theoretical Motivation" 但内容主要是经验层面的观察和启发式推理，非严格理论推导。"Empirical Motivation" 可能更准确。
[R2-M5, R1 未反驳]

---

## Reviewer 分歧与 Director 裁定

| 问题 | R1 立场 | R2 立场 | Director 裁定 |
|------|---------|---------|---------------|
| Reference model confound 严重程度 | Critical, 贯穿全部实验 | Critical at 14B, mitigated at 1–1.5B (6/9 cross-ref cells work) | 采纳 R2 分层判断：14B Critical, 1–1.5B 有 intrinsic signal 但正文讨论不足 |
| Feature multicollinearity 严重程度 | Critical | Major (group-level analysis robust) | 降为 Warning——R2 的四方法收敛论据成立 |
| EDD 新颖性 | 有贡献 (contiguous prefix + model collapse) | 低 (AUC + threshold + max) | 采纳 R1——contiguous prefix 约束是有价值的设计选择 |
| Cross-strategy transfer 严重程度 | Should-Fix | 论文未 claim solved | Should-Fix (framing issue) |
| Non-ordinal classifier | Should-Fix | REBUT (B.25 ordinal methods 无增益) | 采纳 R2 rebuttal, dropped |

---

## Questions

**Q1.** 如果使用规模匹配的 reference model（如 OLMo-1B 做 OLMo 的 reference、GPT-2 XL 做 GPT-2 XL 的 reference），depth signal 是否保持？这是分离 reference model confound 与 intrinsic depth signal 的关键实验。

**Q2.** Table 1 中 7 个 model-free 特征（lexical 4 + repetition 3）单独使用能达到什么准确率？如果 >50%（2× chance），则部分回应 reference model confound 问题。§4.2 group ablation 暗示 model-free 特征远弱于 perplexity family。

**Q3.** 对 27 次 depth-pair AUC 测试应用 Benjamini-Hochberg FDR correction 后，哪些 cell 的 d2-vs-d3 判断会发生改变？

**Q4.** Qwen2.5-7B 的 U 型 AUC 恢复（d0v1=0.969, d2v3=0.709, d4v5=0.772）如何解释？论文归因于 cross-reference setup，但如果归因成立，则所有 cross-reference 实验的 AUC 模式都不可信。

**Q5.** 5–10% mixing ratio 下 depth estimation 的表现如何？这是 Introduction 动机与实验交付之间鸿沟的关键数据点。

---

## Missing References

两位 Reviewer 共同指出以下缺失引用（均 AGREE）：

1. **Stylometric analysis 文献**：论文的 19 个统计特征本质上是 stylometric features（TTR、hapax ratio、n-gram entropy 等）。Stamatatos (2009) 的 authorship attribution survey 是直接的方法论先驱。引用此文有助于定位 depth estimation 与 authorship attribution 的关系。

2. **Ordinal classification 文献**：Frank & Hall (2001) 将 ordinal 分类分解为二元子任务的方法与 EDD 的 pairwise binary classifier 有直接关联。

3. **Self-play / Self-improvement 文献**：Chen et al. (2024) Self-Play 和 Yuan et al. (2024) Self-Rewarding 代表刻意的递归生成范式，与本文"意外" web 递归污染形成有意义的对比。

---

## External Review

外部审稿：未请求。

---

## Visual Layout Check（非评分项）

视觉审查已完成（2026-05-25 21:15–21:19 UTC）。

| 严重级别 | 数量 |
|---------|------|
| Critical | 0 |
| Warning | 1 |
| Info | 11 |

**Warning**: Pages 1–2 连续纯文本无 display item，Figure 1 延迟至 page 3。建议将 Figure 1 提前至 page 2 底部（如版面允许）。

**Info 摘要**: Figure 2 (p.6) 热力图 cell 内数字约 6pt 密集阅读需放大 | Table 2 (p.5) 9 列紧凑但未溢出格式规范 | Figure 3 (p.7) 图例字号偏小建议确认灰度可区分性 | Figure 4 (p.8) + Table 4 清晰可读 | Limitations (p.9) 简短合规约 6 行 3 点 | Figure 5 (p.12) 混淆矩阵偏小但可读 | Page 13 附录密度高但不影响主文 | 全文 booktabs 格式统一无 LaTeX 渲染错误无 margin 溢出无未解析引用 | 参考文献格式统一编号连续

整体排版质量良好，无格式性问题影响审稿。

---

## Overall Assessment

**评分：3.0 / 5.0 — Findings**

本文在受控设定下（1–1.5B 模型、已知解码策略、100% replacement chain、Wikipedia seed）完成了系统化的递归生成深度估计实证研究。核心发现（d0 高度可分、困惑度尾部特征主导、相邻深度可区分深度约 3–5 代）在 9/9 cells 中一致复现，实证基础扎实。EDD 指标的 contiguous prefix 设计和与 model collapse 理论的对接是有价值的方法论贡献。

然而，论文存在**系统性的 claim-evidence 失配**：
- "解码策略贡献至少与模型架构相当"无统计检验（W1）
- "Signal attenuates with scale" 仅有 3 个 7B+ 模型、行为矛盾、且受 reference model confound 污染（W2）
- "Statistical features > PLM" 基于不公平的 frozen CLS baseline（W7）
- Introduction 动机暗示真实 web 场景适用性，但 5–10% mixing 未测试、full-replacement chain 为唯一主实验（W3）

此外，12/19 特征依赖特定 reference model（W4）、LoRA r=16 统一配置可能引入系统性偏差（W8）、seed corpus 仅限 Wikipedia（W9）——这些 scope 限制在正文中讨论不足。

**达到 Findings 接收水平的条件**：将 Critical claims 降级为 observations 或提供统计检验，在正文明确限定 scope（1–1.5B, within-strategy, controlled replacement），Discussion 充分讨论 reference model 依赖的部署含义。

**升级至 Conference (4.0) 需要**：(1) 至少一个 5–10% mixing ratio 实验；(2) 规模匹配的 reference model 对照实验（回答 Q1）；(3) 修正 PLM baseline 为 fine-tuned 设定。

---

## Detailed Comments

**Abstract**: 信息密度高但合规（<200 words）。"signal attenuates with scale" 需降级为 preliminary observation 或删除。14B 结果的 cross-ref vs self-ref 条件需分句澄清。

**§1 Introduction (p.1–2)**: Contribution 4（"decoding strategy affects cross-condition transfer more than model architecture"）在 §4.1 无统计检验支撑，建议改为 "decoding strategy and model architecture both contribute meaningfully to performance variance"。

**§3.3 Feature Extraction (p.4)**: 未引用 stylometric analysis 文献。19 个特征本质是 stylometric + perplexity features，应在 Related Work 或此处定位与 authorship attribution 的关系。

**§3.4 Definition 1 (p.4–5)**: EDD 形式化清晰。建议添加一句说明 T=0.70 为 operational choice（参照 sensitivity analysis），非理论推导。

**§3.5 Theoretical Motivation (p.5)**: 标题建议改为 "Empirical Motivation"——内容为经验观察而非严格理论推导。

**§4.1 (p.5)**: "mean within-model strategy gap is 9.3 pp, comparable to the 7.2 pp mean within-strategy model gap"——2.1 pp 差异在 9 cell 上无统计效力。要么补充 permutation test，要么将 "at least as much" 改为 "both contribute meaningfully"。

**§4.2 (p.6)**: 个体特征排名叙事（"p90_ppl and var_surprisal are consistently prominent"）在 VIF>10 下不可靠。建议改为 group-level 叙事："perplexity tail statistics family (p90_ppl, var_surprisal, kurtosis_ppl) collectively dominates"。

**§5.2 (p.8)**: 跨策略 45.95% 与标题 "Statistical Fingerprints" 暗示的可迁移性矛盾。正文应明确：当前深度估计 claim 限定于 "within known model-strategy configurations"。

**§6 Discussion (p.8)**: "end-to-end PLMs lag RF by 14–33 pp" 需加条件限定："under frozen CLS + linear probing"。Reference model 依赖的部署含义需单独一段讨论。

**Limitations (p.9)**: 覆盖 3 点，长度合规。建议将 full-replacement 假设的局限从 Limitations 提升到 Discussion 的显著位置。

**Appendix B.19**: Qwen2.5-7B U 型 AUC 是关键异常，需要超出 "likely originates from cross-reference setup" 的解释。如果归因于 cross-reference，则需讨论所有 cross-reference 实验结果的可信度边界。

**Appendix B.20**: 检查是否仍有 PLACEHOLDER 未填充（Round 19 发现）。