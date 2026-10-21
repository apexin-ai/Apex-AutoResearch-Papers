---
round: 7
review_mode: fresh
overall_score: 3.0 (Findings)
timestamp: 2026-05-22T15:09:38.741661+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---


# 审稿报告 — Round 9 (Fresh Review)

**项目**: exec-sim-repair-verifier
**目标 Venue**: EMNLP 2026 via ACL Rolling Review
**截止日期**: 2026-05-25
**Reviewer 编排**: 2 人（R1: 方法严谨性, R2: 新颖性与完整性）
**审稿轮次**: 1 轮独立审稿 + 1 轮交叉分享（关键问题已收敛，无需第 2 轮）

---

## Summary

本文系统比较了三种 execution-free code verification formulation（CLS 二分类、CWM 输出生成、TRAJ 轨迹评分），在匹配 LoRA 微调条件下跨两个代码 LLM 家族（Qwen3、DeepSeek-Coder）、两个复杂度层级和多种随机种子进行实验。主要发现：function-level CLS-CWM 统计等价（TOST p=0.007），repo-level 在 ≤8B LoRA 下出现 18-26pp 分歧（z=−23.7），识别三种失败模式（format collapse、decision collapse、aggregation penalty），以及错误互补性（oracle 90.63%/95.83%）。实验设计和统计方法在 NLP 实证研究中属上乘水平，但核心发现的 novelty 有限，repo-level 结论受多重 confounds 限制。

---

## Strengths

**S1. 匹配实验设计的严谨性** [consensus]
三种 formulation 共享相同训练数据、LoRA 配置、seed 和 evaluation protocol。在 formulation comparison 中达到了罕见的 controlled comparison 水平。这是论文最核心的方法论贡献。

**S2. 统计方法论完整且优于领域平均** [consensus]
TOST 等价检验（非 NHST non-significance）、clustered bootstrap with ICC/DEFF、Holm-Bonferroni 校正、mixed-effects regression——层层递进，正确选择且正确应用。

**S3. Threats to Validity 透明度高** [consensus]
§5.5 和 Appendix O 逐一识别并用实验证据量化 5 个 confound，超过大多数 NLP 论文仅做定性承认的水平。

**S4. Failure Mode Taxonomy 有实用价值** [consensus]
Table 4 的三类失败模式（format collapse, decision collapse, aggregation penalty）定义清晰、有实例支撑，为 practitioner 选择 formulation 提供可操作的诊断框架。

**S5. Error Complementarity 是最具洞察力的发现** [consensus]
Oracle 组合在 function-level 达 90.63%、repo-level variant-level 达 95.83%，表明不同 formulation 的错误模式是互补的。此发现不可从单一 formulation 结果推导，为 ensemble/routing 提供了实证基础。

**S6. 附录极其充分** [consensus]
14 页附录覆盖 ablations、error analysis、statistical tests、qualitative examples、convergence analysis，展现扎实实验工作量。可复现性评分 4/5。

---

## Weaknesses

### Must-Fix（共识 Critical）

**C1. TOST ±2pp SESOI 论证不充分** [全票共识: R1-N2, R2-W2]
两位 Reviewer 独立标记。±2pp 是等价检验框架中最关键的参数——直接决定 TOST 能否拒绝 H₀。当前论证（"2pp ≈ 2-3 problems out of 114, comparable to seed noise"）存在循环论证风险（seed noise 是实验属性而非领域阈值）。三个不足：(a) 代码验证中漏检 critical bug vs FP 成本不对称，flat ±2pp 不反映此结构；(b) function-level 和 repo-level 的 2pp 含义完全不同但 SESOI 未区分；(c) 未引用等价检验方法论文献（如 Wellek, 2010）。Appendix J 已有 sensitivity analysis（±1pp~±5pp，最小等价 margin ±1.52pp），但正文未引用。
**修复**: §3.4 加 domain-grounded SESOI justification；正文引用 Appendix J；引用 Wellek (2010)。

**C2. Contribution Novelty 与 "Design Space" Framing 不匹配** [R2 critical, R1 agrees Should-Fix; Director 裁定 Must-Fix]
标题声称 "Formulation Design Space"，但实际只比较三个已知 formulation（二分类、输出生成、序列分类）。真正的 design space 应涵盖 loss function 变体、decoding 策略、output format 设计等更多维度。这是 presentation issue（非方法论缺陷），但影响 reviewer 第一印象。
**修复**: 标题和 §1 从 "design space" 调整为 "systematic comparison"。

### Should-Fix（共识或多数）

**W1. Repo-level 因果性 claims 被 model identity dominance 削弱** [全票: R1-W1/W2, R2-W1]
Appendix M 报告 model identity 解释 >95% predictable variance；formulation×complexity interaction (z=−23.7) 统计显著但相对 model effects 较小。结合 8B repo-level 仅 3 seeds/model、variant-level n=48 (MDE≈25pp)，repo-level 结论不支持 strong causal claims。Abstract "model-dependent" 从 2 个 model family 过度泛化。
**修复**: (a) 正文讨论 model identity dominance（当前仅在 Appendix M）；(b) "model-dependent" 改为描述性表述；(c) variant-level 分析标注为 exploratory/descriptive。

**W2. CWM 评估指标非对称性未量化** [R1 critical, R2 warning; Director 裁定 Should-Fix]
CWM 使用 exact matching（保守）+ 不可解析输出默认 majority class (PASS)。两个偏差方向可能部分抵消。R2 指出 function-level unparseable 仅 1.39%，实际偏差 <1pp，不足以推翻 TOST 结论。Repo-level 的 parseable bias 在 Appendix N 已有分析。但 relaxed matching robustness check 可进一步加强 function-level 等价性证据。
**修复**: 对 1 个 function-level seed 做 relaxed matching 或 manual inspection 作为 appendix robustness check。

**W3. Function-level 等价性作为独立 Contribution 偏弱** [R2 critical, R1 部分同意]
分类与生成在短输出 task 上趋同可预期。方法论贡献（TOST 严格证明等价性）有价值，但发现本身不构成 surprise。
**修复**: 融入三层结构叙述，不作独立 contribution 列出；强调 TOST 方法论而非结论的贡献。

**W4. Checkpoint Selection 不一致** [全票: R1-W3]
CWM 所有 repo-level runs 因 NaN validation loss 使用 final epoch checkpoint；CLS 使用 val-best。CWM NaN val loss 可能是 formulation-inherent（可变输出长度导致 per-token loss 不稳定）——这本身是值得在正文讨论的 formulation weakness。
**修复**: (a) 解释 CWM NaN val loss 原因；(b) 讨论是否 formulation-inherent；(c) 如可能，报告 CWM 多 checkpoint 精度。

**W5. TRAJ Downsample Ablation 覆盖不足** [全票: R1-W4]
1 model × 1 seed × 1 level 不足以排除 ~180× 数据量差异作为主要 confound。
**修复**: 扩展至 ≥2 models 或明确标注为 limitation。

**W6. 遗漏相关工作** [R2-W5, R1 部分同意]
需验证并按相关性补充：CodeScaler (arXiv 2602.17684)、GenPRM (AAAI 2026)、ExecVerify (arXiv 2603.11226)。Self-Execution Simulation 已在 references 中（R2 误报遗漏）。
**修复**: WebSearch 验证真实性后加入。

### Minor

**M1.** Appendix M 补充 cluster-robust SEs 和 logistic regression 具体系数（R1-W5, R2 agrees）。
**M2.** Clustered bootstrap 实施细节（resample unit, block size）未说明（R1）。
**M3.** Figure 3 (Appendix) y-axis 不从 0 开始但未标注，不同于 Figure 2 的良好实践（R2-M2, R1 agrees）。
**M4.** Abstract 第一句 "relies on" 过于绝对，建议改为 "increasingly leverages"（R2-M3, R1 agrees）。
**M5.** Repo-level DEFF=114.3 → effective n≈86 未讨论对推断的限制（R1）。
**M6.** 缺少方法论引用：Wellek (2010) 等价检验教材, Moulton (1990) clustered data 经典文献（R1）。
**M7.** Figure 1 内部文字偏小（~60-65% 正文），打印时可能需放大（视觉审查）。

---

## Reviewer Consensus

两位 Reviewer 独立达成共识的关键判断：
- [AGREE] TOST ±2pp SESOI 需更强论证（最高权重共识 issue）
- [AGREE] Repo-level 结论受 model identity dominance、limited seeds、variant-level power 限制
- [AGREE] Function-level 等价性 novelty 有限
- [AGREE] DeepSeek 2-seed 不足以支撑 "model-dependent" 泛化
- [AGREE] Checkpoint selection 不一致是实质性 confound
- [AGREE] 统计方法论超过领域平均水平
- [AGREE] 匹配实验设计是核心优势

## Reviewer Divergence

| Issue | R1 | R2 | Director 裁定 |
|-------|----|----|--------------|
| CWM 评估非对称性严重性 | Must-Fix | Warning (func-level bias <1pp) | **Should-Fix** — function-level 偏差可忽略 |
| "Design space" framing 严重性 | Should-Fix | Must-Fix | **Must-Fix** — 影响第一印象 |
| CWM 术语 (R2-W3) | Rebut (沿用已发表术语) | Should-Fix | **Dismissed** — 作者使用 established terminology |
| 缺 execution-based 对比 (R2-W4) | Rebut (超出论文 scope) | Should-Fix | **Dismissed** — 超出论文明确界定的研究问题 |
| Failure mode taxonomy 偏向 CWM (R2-M4) | Rebut (CWM 天然更复杂) | Minor | **Dismissed** — R1 论证有说服力 |
| Extended Limitations (R2-M5) | Rebut (ACL 标准做法) | Minor | **Dismissed** — 页数限制下的标准做法 |

---

## Questions for Authors

1. CWM function-level exact match 中有多少比例的 "错误" 实际上是语义正确但格式不同？manual inspection 一个 seed 即可回答。[全票]
2. ±2pp SESOI 是 pre-registered 还是 post-hoc？如果 post-hoc，TOST 框架的效力减弱。[全票]
3. CWM repo-level runs 出现 NaN validation loss 的原因？formulation-inherent 还是 implementation issue？如果前者，是值得在正文讨论的 formulation weakness。[全票]
4. Oracle complementarity (90.63%/95.83%) 为 single-seed 估计——跨 seed 是否稳定？[全票]
5. 是否有 >8B 或 full fine-tuning 的 pilot data 暗示结论可能不同？[全票]

---

## Missing References

**已确认需要**:
- Wellek, S. (2010). "Testing Statistical Hypotheses of Equivalence and Noninferiority." — TOST 方法论标准教材
- Moulton, B. R. (1990). "An Illustration of a Pitfall in Estimating the Effects of Aggregate Variables on Micro Units." — clustered data 经典文献

**需作者验证真实性后补充**:
- CodeScaler (arXiv 2602.17684, Feb 2026) — execution-free reward model
- GenPRM (AAAI 2026, arXiv 2504.00891) — generative PRM with code verification
- ExecVerify (arXiv 2603.11226) — RL with verifiable stepwise rewards
- Self-Execution Simulation — **已在 references 中引用**（R2 误报遗漏）

---

## External Review

外部审稿：未请求（项目未启用 external_review）。

---

## Visual Layout Check（非评分项）

视觉审查已完成（0 critical, 2 warning, 6 info）：

**Warning**:
- 前两页连续纯文本无 display item，Figure 1 直到第 3 页才出现。审稿人需读完 ~2 页密集文字才看到第一张图，延迟锚定效应。建议将 Figure 1 提前或增加 teaser figure。
- 第 8 页 Related Work + Conclusion + Limitations 三节挤压，文字极度密集，给审稿人"赶工"印象。若 Related Work 能再压缩 3-5 行可改善呼吸感。

**Info**:
- Figure 1 内部文字 ~60-65% 正文字号，打印可能需放大
- Figure 2 y-axis 截断已标注（良好实践）
- Figure 3 (Appendix) 蓝/绿/青三色对色盲用户区分度有限，建议 Okabe-Ito 色板或 hatch pattern
- Table 2/3 排版清晰，Table 4 可读性良好
- Limitations 简洁覆盖 3 点，符合 EMNLP 要求

---

## Overall Assessment

**评分: 3.0 / 5 (Findings)**
**置信度: 4 / 5**

| 维度 | R1 | R2 | Director |
|------|----|----|----------|
| Soundness | 3.5 | 3.5 | 3.5 |
| Excitement | 2.5 | 2.5 | 2.5 |
| Reproducibility | 4.0 | 4.0 | 4.0 |
| Overall | 3.5 | 3.0 | **3.0** |

**定位：Findings of ACL，不足以进入 Main Conference。**

这是一篇方法论严谨度超过该领域平均水平的实证研究。匹配实验设计、多层统计检验、透明的 threats to validity 在 NLP empirical papers 中属上乘。Failure mode taxonomy 和 error complementarity 有实用价值。

但 novelty 和 excitement 不足以支撑 Main conference：
1. "Design space" framing 与实际三 formulation 比较之间有张力——论文是 rigorous formulation comparison，不是 design space exploration
2. Function-level 等价性在很大程度上可预期（短输出下分类与生成趋同）
3. Repo-level 结论严重受限于 ≤8B LoRA regime、model identity dominance (>95% variance)、limited seeds、n=48 variant-level power
4. 核心发现（generation 在复杂输出上格式崩溃）对 practitioner 而言不意外

**Findings 接收合适**。实验框架和统计方法论对领域有参考价值，failure mode taxonomy 和 error complementarity 可供后续工作引用。若能扩展至更多 model families、增加 repo-level seeds、解决 SESOI domain justification，有潜力提升至 3.5 (Borderline Conference)。

---

## Detailed Comments

### §1 Introduction
- "formulation design space" → "systematic formulation comparison" 更准确
- Contribution 1 (function-level equivalence) 可融入三层结构叙述，不必独立列出
- "model-dependent" (TRAJ parity) 应弱化为 "observed to differ between tested families"

### §2 Method
- §2.2 failure mode taxonomy：可增加 1-2 句 CLS/TRAJ 的失败模式特征描述
- SESOI ±2pp 在 §3.4 应有 domain-grounded justification 并 reference Appendix J

### §3 Experiments
- Table 1 footnote "not informational" → "insufficient seeds for statistical inference" 更清晰
- §3.4 应在正文引用 Appendix J 的 TOST sensitivity analysis
- §3.5 应讨论 model identity dominance（当前仅在 Appendix M）
- §3.7 CWM NaN val loss 值得作为 formulation-specific weakness 在正文讨论
- Variant-level 分析（Table 4, §3.5）应明确标注为 exploratory/descriptive

### §4 Related Work
- 核实并按相关性补充 CodeScaler、GenPRM、ExecVerify
- 加入 Wellek (2010) 和 Moulton (1990) 方法论引用

### §5 Conclusion
- "CLS is recommended primarily for its throughput advantage" 定位合理 ✓
- ≤8B LoRA regime qualifier 已出现 ✓

### Appendix
- Appendix J (TOST sensitivity) 应在正文 §3.4 被引用
- Appendix M 应补充 cluster-robust SEs 和 logistic regression 具体系数
- Clustered bootstrap 实施细节应补充（resample unit, block size, iteration count）
- DEFF=114.3 → effective n≈86 的含义应在正文或附录讨论
