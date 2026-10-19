---
round: 7
overall_score: 3.0
timestamp: 2026-05-18T06:43:52.977657+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 Round 8 — contrastive_trace_safety

**论文**: Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models
**Venue**: EMNLP 2026 via ARR (Findings track)
**Deadline**: 2026-05-25
**Reviewer 编排**: R1 (方法/实验/统计) + R2 (新颖性/写作/Related Work/格式)
**轮次**: Round 1 独立审稿 → 交叉分享 → 收敛（1 轮达成共识）

---

## Summary

本文首次系统比较 hidden-state (HS) probes 和 text-based monitors 在推理模型 safety commitment point 检测上的表现，覆盖 4 个模型（R1-8B, OT-7B, QwQ-32B, R1-32B）、2 种架构（Llama, Qwen）、2 个尺度（7-8B, 32B）。核心方法论贡献是揭示层选择指标中 crossing rate 偏差可逆转 32B 模型上的 HS 优势结论。在修正层上，HS probes 在 384d MiniLM 基线上显著优于 text probes（Holm-Bonferroni 校正后 4 个模型均显著），但优势是 encoder-conditional 的（1024d BGE-large 仅 1/4 模型显著）。7 种替代方法均未能在所有模型上一致匹配监督探针。

---

## Strengths

1. **层选择敏感性是真正新颖的方法论贡献** [R1-S1, R2 同意]。crossing rate 偏差如何系统性选择浅层（QwQ L2=3%, R1-32B L10=16%）的机制分析清晰（cosine distance 分析, Appendix B），对整个 probing 社区有广泛警示价值，不限于 safety 任务。

2. **实验设计全面，负面结果报告诚实** [R1-S2, R2 同意]。7 种 baseline 方法的系统评估、PCA 维度控制实验、BGE-large encoder 鲁棒性测试、control task 验证（selectivity 12.5-19.7pp）、M002 bug 公开披露——科学诚实性高于同领域平均。

3. **统计方法严谨** [R1, R2 Soundness 3.5/5]。Holm-Bonferroni 校正、10k bootstrap CI、control task、multi-seed 验证（Appendix L）。超参数完整报告，代码承诺公开。

4. **写作质量整体良好** [R2]。Introduction 从具体问题切入（非泛泛 "LLMs have shown..."），五段结构完整。无 em-dash。Related Work 做归纳比较而非论文堆砌。46 篇引用含 2026 concurrent work。

5. **Bug 披露**（Appendix M）在学术论文中极为罕见 [R1-S4, R2]，体现最高可复现性标准。

---

## Weaknesses

### Must-Fix（影响接收决定）

**MF-1** [R1-N1, R2 AGREE] **"12/12 Holm-Bonferroni" 修辞框架夸大独立证据量**
3 个指标（bal_acc, precision, FPR）高度相关——全部依赖同一混淆矩阵，precision 和 FPR 都直接涉及 FP 计数。有效独立比较数约 4-6 个（模型级），不是 12 个。论文声称 "HB correction is stricter under positive dependence" 在技术上可辩护，但读者读到 "12/12 pass" 会自然理解为 12 条独立证据。R2 补充：如果改为 4-test HB（每模型取最保守 p），R1-8B FPR (p=0.044) 在 threshold 0.0125 下不通过。"Two complementary measurement families" 框架同样有问题——两个 family 都来自同一混淆矩阵，其"收敛"是预期的而非独立验证。
→ 建议：(1) 全文改为 "all 4 models significant, each on 3 correlated metrics (HB corrected)"；(2) "two complementary families" 改为 "所有不含 crossing rate 的指标一致选深层"；(3) 考虑 Hochberg step-up（正相关下合法且更有 power）。

**MF-2** [R1-N2, R2-N2, 完全共识] **32B 结果为 pilot-scale，不应与 7-8B 等量齐观地出现在 headline claims**
- R1-32B test n=20, validation ~4 traces; W=1 仅覆盖 5/20 traces (25%)——precision/lead time 基于 5 条 trace
- Multi-seed: R1-32B FPR std=0.145 (mean 0.207, CV=70%), precision std=0.128——单次 split 近乎随机
- QwQ-32B: position baseline bal_acc (0.832) > HS (0.796); HS precision +4.5pp / FPR -3.0pp 差异在 n=19 下无 p-value
- Bootstrap 在 n=19-20 下覆盖率不足（论文自引 Efron &amp; Tibshirani 1993 承认），未采用 exact permutation test
- Abstract "all four models" 将脆弱 32B 与稳健 7-8B 等量齐观
→ 建议：(1) Abstract/Introduction 分两级 claim: robust 7-8B vs pilot-scale 32B；(2) 32B 用 exact permutation test (2^20≈10^6, 完全可行)；(3) 主表添加 ±std；(4) 报告 R1-32B 5-trace 具体数据和 QwQ HS vs position p-value。

**MF-3** [R1-N3, R2 AGREE] **累积超参数过拟合风险未量化**
Layer (64层) × W (7选项) × K (5选项) × threshold × C 共 5+ 超参数在同一验证集上选择。32B 验证集约 4 条 trace。C-insensitivity (<2pp) 仅覆盖 C 一个超参数，不覆盖 layer/W/K 的联合选择。如果 "corrected layers" 本身是过拟合产物，则动摇 Contribution 1 在 32B 上的可信度。
→ 建议：(1) LOO-CV 验证 32B layer 选择跨 split 稳定性 (L60±? 的波动范围)；(2) 量化联合 DoF 对报告 p-value 的膨胀效应；(3) 至少讨论累积过拟合风险。

**MF-4** [R2-N1, R1-W1, 完全共识] **Encoder-conditional HS 优势在主叙事中被严重低估**
Abstract/Introduction 叙事重心在 384d MiniLM 结果 (+15.4 to +32.5pp)。MiniLM-L6-v2 是 2020 年的 22M 参数模型，在 2026 年不构成 competitive text baseline。BGE-large-1024d 仅 OT-7B 通过 HB (1/4 models)。BGE 行仅测 precision 未报告 bal_acc/FPR（cherry-picking 嫌疑）。Contribution 2 "Encoder-conditional HS advantage" 包含限定词但在反复引用 "+15.4 to +32.5pp" 时容易被忽略。
→ 建议：(1) Abstract 必须包含 1024d 限制 ("the advantage narrows substantially against a stronger 1024d encoder, 1/4 models significant")；(2) Contribution 2 重述为 "directional advantage that narrows with stronger encoders"；(3) BGE 补报全部 3 个指标。

---

### Should-Fix（影响评分但非一票否决）

**SF-1** [R2-W1, R1 AGREE] **Abstract 数据堆砌**。~251 words 包含 crossing rate 机制解释、HB 校正细节、多组 pp 数字、position baseline 具体数字 (0.832 vs 0.796)、"Seven alternative approaches fail"。更像 Results 压缩版。应砍统计细节保留 2-3 关键数字，按 problem→insight→finding→implication 结构重写，控制在 200 words。

**SF-2** [R1-W2, R2 AGREE] **QwQ-32B position baseline 缺残差化控制**。Position bal_acc 0.832 > HS 0.796；Appendix E control task 也 position > HS (0.705 vs 0.667)。HS precision/FPR 小幅优势无 p-value。缺 position-residualized HS features 实验。

**SF-3** [R1-W3, R2 AGREE] **Safe-trace FPR 39-52% 与 Introduction monitoring 叙事矛盾**。Introduction 开篇 "monitoring systems that must intervene before harmful content reaches users"，Discussion 才承认 "characterization tool"。Introduction 应更早限定为 phenomenon characterization。

**SF-4** [R1-W4, R2 AGREE] **K=5 选择依据不足**。K 消融 (Appendix I) 仅 W=1 下进行。K×W 交互未探索。"Pareto-optimal" 判断主观（K=7 在多数模型降 FPR 更多）。K 选择是否在验证集上——如是则加剧 MF-3。

**SF-5** [R1-W5, R2 AGREE] **Multi-seed 结果仅附录**。主 Table 基于单次 split。R1-32B precision std=0.128, FPR std=0.145 直接影响读者信任。应在主表添加 ±std。

**SF-6** [R2-W2, R1 nuanced AGREE] **Negative results framing 不公平**。BOCPD R1-8B 93% detection, RepE QwQ 0.756 bal_acc (vs supervised 0.778 差 2.2pp) 被统一 frame 为 "fail"。Precision-priority framing 在 experiments.tex L118 有先验声明（非完全事后），但 Table 5 措辞应改为 "no method consistently matches supervised probing across all four models"。

**SF-7** [R2-W3, R1 AGREE] **正文仅 1 张 Figure，最重要的 layer heatmap 在附录**。Layer heatmap (fig_layer_heatmap.pdf) 是 Contribution 1 最直观的证据，应移入正文。核心叙事优先级：layer selection > HS vs text > temporal improvement，Figure 排列应反映此优先级。

**SF-8** [R2-W4, R1 AGREE] **缺少实验直接使用工具的原始引用**。CUSUM 无 Page (1954)、MiniLM 无 Reimers &amp; Gurevych (2019)、BGE 无 Xiao et al. (2023)。另建议补充 Meng et al. (2022, causal tracing) 和 Li et al. (2024, ITI)。

**SF-9** [R2-W5, R1 nuanced AGREE] **Discussion 数字级重复**。与 Introduction/Experiments/Conclusion 有大量数字重复。泛化 hypothesis (crossing rate bias in other tasks) 和 deployment defaults 是新内容应保留，但数字重复应精简。

---

### Minor

- **m1** [R2-M1, R1 AGREE]: ~15+ 处 -ing 短语结尾模式 (AI 写作标志)，审稿人敏感度高
- **m2** [R2-M3, R1 AGREE]: Bug Disclosure (App M) "git history" 措辞有 double-blind 泄露风险，改为 "code will be released upon publication"
- **m3** [R2-M4, R1 AGREE]: Table 2 caption "p=0.35--0.83 (QwQ)" 应标注具体 metric 对应
- **m4** [R2-M5, R1 AGREE]: OpenThoughts (数据/方法) vs OpenThinker-7B (模型) 名称应区分
- **m5** [R1-M5, R2 AGREE]: Abstract 中 "crossing rate" 未在 Abstract 内定义
- **m6** [R1-M1, R2 AGREE]: GRU 70/30 vs LR 60/20/20 数据划分不一致
- **m7** [R1-M4, R2 partial REBUT]: HS probes 是否存在 textual leakage——PCA+control task 提供间接证据但非直接验证

---

## Reviewer Consensus

以下问题两位 Reviewer 完全共识 [AGREE]：
1. "12/12 HB" 修辞误导，有效独立比较 ~4-6 个 (MF-1)
2. 32B 结果为 pilot-scale，不应与 7-8B 并列在 headline claims (MF-2)
3. 累积超参数过拟合风险未量化 (MF-3)
4. Encoder-conditional 优势在叙事中被低估 (MF-4)
5. Abstract 数据堆砌 (SF-1)
6. QwQ-32B position baseline 缺残差化控制 (SF-2)
7. FPR vs monitoring 叙事矛盾 (SF-3)
8. Layer heatmap 应移入正文 (SF-7)
9. CUSUM/MiniLM/BGE 缺原始引用 (SF-8)

## Reviewer Divergence

1. **M2 (a4paper 选项)**: R2 提出 → R1 REBUT（ACL style file 内部处理页面尺寸，额外添加可能冲突）。**判定：R1 正确，非问题。**
2. **M4 (textual leakage)**: R1 提出 → R2 partial REBUT（PCA-384d 10/12 pass + control task selectivity 12.5-19.7pp 提供间接证据，但直接测试如 LEACE erasure 更有说服力）。**判定：非 blocker，列为 minor。**

---

## Questions for Authors

1. Bootstrap 重采样单元确认为 trace-level？n=20 bootstrap 分布是否平滑？
2. 是否考虑 exact permutation test (32B n=20, 2^20≈10^6 可行)？
3. Corrected layer 选择在不同 seed split 下是否稳定？QwQ L60 跨 5 seed 波动范围？
4. PCA-384d 保留 79-92% variance，但 Mahalanobis 实验显示 safety signal 在 minor components (<5% variance)——PCA 控制是否因保留了这些 minor components 而解释力不足？
5. QwQ-32B HS vs position baseline 是否有统计检验 p-value？
6. HS advantage 是否可能是高维统计优势 (5120d vs 384d) 而非 safety-specific structure？

---

## Missing References

必须补充：
- Page, E.S. (1954). Continuous inspection schemes. *Biometrika* — CUSUM 原始论文
- Reimers &amp; Gurevych (2019). Sentence-BERT — MiniLM 基础
- Xiao et al. (2023). C-Pack: Packaged Resources To Advance General Chinese Embedding — BGE

建议补充：
- Meng et al. (2022). Locating and Editing Factual Associations in GPT — causal tracing
- Li et al. (2024). Inference-Time Intervention — hidden-state intervention

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未请求。

---

## Overall Assessment

**Overall Score: 3.0 (Findings)**

| 维度 | R1 | R2 | 共识 |
|------|----|----|------|
| Soundness | 3/5 | 3.5/5 | 3.0-3.5 |
| Excitement | 3/5 | 2.5/5 | 2.5-3.0 |
| Reproducibility | 4/5 | 4/5 | 4/5 |
| Confidence | 4/5 | 4/5 | 4/5 |

**核心判断**：层选择敏感性是真正有价值的方法论贡献，7-8B 实验设计稳健，科学诚实度高（bug 披露、负面结果报告）。但：
- 32B 结果的统计基础太弱（n=19-20, val ~4, multi-seed CV=70%），不应与 7-8B 并列在 headline claims
- HS 优势对 encoder 选择高度敏感（BGE-large 1/4 HB pass），核心 claim 依赖弱 baseline
- "12/12 HB" 修辞框架恰恰犯了论文所批评的方法论包装错误
- Safe-trace FPR 39-52% 使论文实际贡献为 phenomenon characterization 而非 monitoring 工具
- 累积超参数过拟合在 32B 极小验证集上未量化

适合 Findings track，但需要在 4 个 Must-Fix 方向做实质性修正：(1) HB framing 诚实化，(2) 32B claim 分层降级，(3) encoder-conditional 前置，(4) 过拟合风险量化或至少充分讨论。

---

## Detailed Comments

### Abstract
当前 ~251 words，信息过载。删除 HB 细节、crossing rate 机制解释、position baseline 具体数字，按 problem→insight→finding→implication 重写。前置 encoder-conditional 限制和 32B pilot-scale caveat。

### Introduction
监控叙事过强。"monitoring systems that must intervene" 应更早衔接 "systematic characterization is a necessary first step"（L3 末尾已有但被淹没）。Contribution 2 重述为 "directional advantage narrowing with stronger encoders"。Contribution list 中 32B 部分加注 pilot-scale。

### Method
"Two complementary measurement families" 改为更诚实的描述。Bootstrap 说明应注明对 32B 小样本的局限。K=5 选择依据应明确（验证集/预定义）。

### Experiments
主 Table 添加 ±std（至少 caption）。BGE-large 补报全部指标。QwQ-32B 增加 HS vs position p-value。Layer heatmap 从附录移入正文。R1-32B 5-trace 数据应透明报告。

### Discussion
精简数字重复，保留泛化 hypothesis 和 deployment recommendations。

### Limitations
已有较好覆盖，但应增加累积超参数过拟合的定量讨论。

### Format
补充 CUSUM/MiniLM/BGE 原始引用。清除 ~15 处 -ing 短语结尾。Bug Disclosure 修改 git history 措辞。fig3_model_dependency.pdf 未引用则删除。