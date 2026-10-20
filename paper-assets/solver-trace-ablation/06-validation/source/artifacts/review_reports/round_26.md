---
round: 26
review_mode: fresh
overall_score: 3.0
timestamp: 2026-05-22T07:55:12.294988+00:00
reviewer_ids: ['1', '2']
cross_response_reviewer_ids: ['1', '2']
force_resubmit: False
---

# 审稿报告 — Round 28 (Fresh Review)

**论文**: Solver Trace Ablation Diagnoses Structural Degeneration and Goodhart Effects in GRPO-Trained Neurosymbolic Reasoning: A Case Study
**目标 Venue**: EMNLP 2026 via ACL Rolling Review (ARR) May 2026
**审稿模式**: Fresh（重新审稿）
**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计+统计方法; R2: 新颖性+完整性+Related Work+Framing）

---

## Summary

论文提出 Solver Trace Ablation (STA)，一种基于 leave-one-out (LOO) ablation 的诊断方法，用于检测 GRPO 训练的 neurosymbolic reasoning 模型中的结构退化。核心指标 Intensional Structural Reward (ISR) 量化 solver input 中各 component 的个体必要性。论文在 Qwen3-4B 上用 FOLIO 数据集进行了 6 种 reward condition × 3-5 seeds 的实验，发现：(C1) exec-only GRPO 下 ISR 崩溃而 prove rate 上升，揭示 execution-only evaluation 的 structural blind spot；(C2) ISR 作为 training reward 产生 seed-dependent 的 compositional Goodhart effect（CE→TS 的 hacking mode 转移），经 premise-count 控制后 ISR 优势从 3.2× 降至 1.06×。论文还提出了 8 种 hacking mode 的分类体系，并在 Prolog 和 ProofFOL 上提供了跨域/跨数据集的初步证据。

---

## Strengths

**S1. 重要且及时的选题。** 在 RL-trained reasoning 模型激增的背景下，识别 execution-only evaluation 的 structural blind spot 是一个真实且被低估的问题。STA 提供了可操作的诊断工具。（R1-S1, R2-S1 共识）

**S2. 严谨的实验控制设计。** Matched random control、shuffled-ISR deconfounding control、SFT baseline 的使用表明作者理解并控制了关键混淆变量。Seed-level 结果报告和 Fisher exact tests 体现了实验透明度。（R1-S3, R2-S2 共识）

**S3. 详尽且有教育价值的 hacking taxonomy。** 8 种 hacking mode（CE, TS, PG 等）每种都有 FOL/Prolog 示例、ISR interaction 分析和检测标准。这对理解 neurosymbolic reasoning 中的 reward gaming 机制有独立贡献价值。（R1-S2, R2-S3 共识）

**S4. 对自身局限性异常坦诚。** Case study 定位明确，Limitations 章节坦承单模型、有限统计效力、classifier 局限性。这种透明度在同类论文中罕见。（R1-S3, R2-S4 共识）

**S5. Goodhart 效应的实证展示。** ISR-as-reward 的 seed-dependent compositional shift（CE→TS）和 dose-response 模式（β=0.1/0.2/0.3）提供了 reward hacking 的细粒度实证。（R1-S4）

---

## Weaknesses

### Must-Fix（双 Reviewer 共识，影响接收决定）

**W1. [critical] Premise-count confound 控制后 ISR 聚合指标的区分力近乎消失。**
- ISR raw advantage 3.2× 降至 premise-count-matched 后的 1.06×（§4.3, Appendix C）
- 论文自身承认 "This confound explains the sole apparent ISR-reward success" (Appendix C)
- Matched comparison 无独立 p-value；N=16 matched pairs 本身也 underpowered
- R2 补充重要 nuance：ISR-as-aggregate 受 confound 严重影响，但 ISR-as-per-sample-diagnostic（通过 hacking taxonomy）相对 robust——论文应清晰分离这两种用途
- **共识**: 双 Reviewer AGREE (R1-N1 + R2-AGREE)

**W2. [critical] N=3 seeds 的统计效力严重不足。**
- N=3 时仅对 d≥2.0 有 80% power（§4.1）
- 多个核心 claim 依赖 seed-level 比较但无法达到显著性：ISR vs random prevalence p=0.182，ProofFOL p=0.10
- Main text 的 claim 语气有时超出 case study 的证据强度（如 §5 "five guidelines for GRPO-trained neurosymbolic systems" 的 prescriptive 口吻）
- **共识**: 双 Reviewer AGREE (R1-N2 + R2-W3)

**W3. [critical] "Compositional Goodhart effect" 缺乏操作性定义。**
- 论文自认 instantiates regressional Goodhart（§4.3），composition shift 是 regressional 的自然推论
- 无形式化定义（无数学表达式、无充要条件、无与 M&G taxonomy 其他变体的边界划分）
- Matched control 后 p=0.182, overall prevalence unchanged——"Goodhart effect" 的实际影响存疑
- **共识**: R1 AGREE + R2-N2

### Should-Fix（双 Reviewer 共识或一方提出另一方同意）

**W4. [warning] STA 方法论新颖性有限——LOO 是标准技术。**
- Algorithm 1 是直接的 LOO 循环，论文自认 "LOO ablation itself is standard"（§3.2）
- 与 Helff et al. (2026) IPT 概念同构："perturb input → observe output change → infer genuine reasoning"
- R2 标为 Must-Fix，R1 REBUT 建议降级——case study 定位 + taxonomy 贡献补偿了 algorithmic novelty
- **分歧记录**: R2 认为方法论不足以支撑 main contribution claim；R1 认为 findings 和 taxonomy 是核心贡献，方法论为工具

**W5. [warning] 标题 "Structural Degeneration" 与 ISR 测量 "component necessity" 之间存在概念跳跃。**
- ISR=0 不必然等于 structural degeneration（可能是 genuine redundancy）
- 推断链 ISR→LOO→taxonomy→degeneration 存在但标题直接跳到终点
- R2 标为 Must-Fix，R1 REBUT（taxonomy 提供推断桥梁）
- **共识**: 降级为 Should-Fix，但需在 §3.2 增加 validity discussion

**W6. [warning] ProofFOL "cross-dataset" 实为 same-task-family 验证。**
- FOLIO 和 ProofFOL 同属 FOL reasoning + Prover9，p=0.10 不显著
- "Cross-dataset" 标签误导——应标为 "within-task-family replication"
- 真正的 cross-domain 证据仅来自 Prolog（不同 solver/语言，但也仅 N=3）
- **共识**: R1-W3 + R2-W1 双方 AGREE

**W7. [warning] Seed 43 T=0.7 评估异常。**
- N=3 seeds 中 33% 使用不同评估协议（temperature=0.7 vs greedy）
- Checkpoints 已删除，无法 greedy re-evaluation
- 需在 main analysis 排除 seed 43 或报告含/不含 seed 43 的双版本统计
- **共识**: R1-W2 + R2-AGREE

**W8. [warning] CMH 检验中 within-seed 非独立性。**
- 100 个评估样本共享同一 trained model，存在 intra-cluster correlation
- 未报告 ICC
- R1 标为 Must-Fix，R2 REBUT 降级——CMH 是 supplementary，seed-level Fisher 为 primary
- **共识**: 降级为 Should-Fix，建议补报 ICC

**W9. [warning] Classifier 验证不足。**
- Precision 验证仅 50 样本且只覆盖 CE/TS 两种 text-match mode
- PG/CI 等需 functional analysis 的 mode 无独立验证
- Recall 未量化；缺 confusion matrix 和 threshold sensitivity analysis
- **共识**: R1-W1 + R2-W5 双方 AGREE

**W10. [warning] SFT baseline 收敛性未证明。**
- 未报告 SFT training loss curve 或 convergence diagnostic
- PR=13% 可能反映训练不足而非 structural integrity
- R2 部分缓解：92% vs 6% 差距大到训练不足不太可能完全解释
- **共识**: R1-W4 + R2-AGREE with reservation

**W11. [warning] 缩写密度过高。**
- ISR, STA, CE, TS, PG, CI, CwU, RE, RP, QaF, PR, NLI, LOO, FOL, SFT... 首次阅读者负担极重
- Table 1 几乎无法解读
- 需 reference table 或 caption 内展开缩写
- **共识**: R2-W2 + R1-AGREE

---

## Reviewer Consensus [AGREE]

1. **N=3 seeds 是整篇论文的核心统计瓶颈**——限制了 hypothesis testing 的可靠性，多个核心比较无法达到显著性
2. **Premise-count confound 严重削弱 ISR 聚合指标**——需分离 ISR 的 aggregate 用途（受 confound 影响）和 per-sample diagnostic 用途（相对 robust）
3. **"Compositional Goodhart" 应放弃新术语**——或提供形式化定义，或降级为 "observed regressional Goodhart pattern in hacking composition"
4. **ProofFOL 不构成 cross-domain validation**——应标为 within-task-family replication
5. **Classifier 验证需扩展**——per-mode precision/recall、confusion matrix
6. **Hacking taxonomy 是论文最强的独立贡献**——应加强而非弱化

## Reviewer Divergence [REBUT]

1. **STA 方法论新颖性** (R2 Must-Fix vs R1 Should-Fix): R2 认为 LOO→solver trace 是 incremental engineering，R1 认为 case study 框架下 findings/taxonomy 是核心贡献。R1 论据更有说服力——论文自定位为 case study，方法论新颖性期望应相应降低。
2. **标题 overclaim 程度** (R2 Must-Fix vs R1 Should-Fix): R2 认为 "Structural Degeneration" 超出 ISR 支撑，R1 认为 taxonomy 提供了推断桥梁。共识降级为 Should-Fix。

---

## Questions

1. Normalized ISR (ISR / E[ISR | premise_count]) 能否去除 premise-count confound？如果采用，cross-condition 比较结果是否改变？
2. 8 种 hacking modes 是否 exhaustive？non-hacking 样本是否经人工验证为 genuine reasoning？如果有，样本量多少？
3. SFT 在 1000 steps 是否收敛？请提供 training loss curve。
4. 增加 seeds 到 N=5 后，ISR vs Random 的 non-hacking rate 比较是否达到显著性？作者预期 Goodhart effect 会消失还是确认？
5. STA/ISR 在 PPO/DPO 下是否预期有类似 structural degeneration？

---

## Missing References

1. **Shapley value attribution** (Lundberg & Lee 2017, SHAP) — LOO 是 Shapley 的一阶近似，需 justify 选择 LOO 而非 Shapley（O(n) vs O(2^n)）
2. **Cook's distance / influence functions** (Cook 1977; Koh & Liang 2017) — ISR 可理解为 influence function 的 neurosymbolic 特化
3. **Mutation testing for ML** (DeepMutation, Ma et al. 2018) — 论文仅引用 1978/2011 经典，缺 ML-specific mutation testing 近期文献
4. **Helff et al. (2026) 名称核实** — 论文写 "Input Perturbation Testing (IPT)"，需确认与原文名称一致

---

## External Review (Stanford Agentic Reviewer)

未请求。

---

## Visual Layout Check（非评分项）

视觉审查完成。3 warnings:

1. **Pages 5-6 纯文本** — §3.3 + §4.1 + §4.2 连续两页无 figure/table/equation，审稿人进入 Experiments 后要翻到 p7 才见 Table 1。建议前移 display item。
2. **Page 7-8 display items 堆叠** — Table 1 + Figure 2 + Figure 3 集中在两页，与 p5-6 形成强烈反差。
3. **Appendix 末页空白** — Table 11-12 间约 50% 页面空白。

Info items: Figure 1 位置佳（p2 顶部）；Table 1 格式专业；Figure 2 坐标轴标签偏小（约正文 60%）；Figure 3 色盲友好性不足（8 色无 pattern 辅助）；Appendix Tables 7-10 字号极小。

---

## Overall Assessment

**评分: 3.0 (Findings)**
**置信度: 4/5 (High)**

| 维度 | R1 | R2 | 共识 |
|------|----|----|------|
| Overall | 3.0 | 3.5 | 3.0 |
| Soundness | 3/5 | 3.5/5 | 3/5 |
| Excitement | 3/5 | 3/5 | 3/5 |
| Reproducibility | 3/5 | 4/5 | 3.5/5 |

**核心判断**: 论文识别了一个真实且重要的问题（execution-only evaluation 的 structural blind spot），提供了有价值的诊断工具（STA/ISR + hacking taxonomy），实验控制设计严谨（matched random, shuffled-ISR, SFT baseline）。但三个核心问题共同制约了主会议接收：

1. **ISR 聚合指标的有效性存疑** — premise-count confound 控制后 3.2×→1.06×，核心诊断指标的 cross-condition 量化比较价值被严重削弱
2. **统计效力不足** — N=3 seeds 限制了多数核心 claim 的可靠性，多个比较未达显著性
3. **概念贡献薄弱** — "compositional Goodhart effect" 缺乏形式化定义，方法论新颖性有限（LOO 是标准技术的领域适配）

Hacking taxonomy（8 种 mode 的系统分类 + per-mode ISR interaction 分析）是论文最强的独立贡献，对 neurosymbolic reasoning 社区有实用价值，适合 Findings track 发表。

若要升级至主会议级别，需：(1) 至少 key conditions 扩展到 N=5 seeds；(2) 提出 normalized ISR 或其他去 confound 的聚合指标；(3) 放弃 "compositional Goodhart" 新术语或提供形式化定义；(4) 扩展 classifier 验证（per-mode precision/recall + confusion matrix）。

---

## Detailed Comments

### Abstract
- ISR collapse 数值（214×, 99.5%）来自单 seed 最极端值（seed 42），已标注但仍可能误导。建议以 3-seed pooled 统计为主叙事。
- "compositional Goodhart effect" 在 abstract 中使用但全文无形式化定义。

### Introduction (§1)
- Contributions (C1) "STA as a diagnostic framework" 的 framing 与 case study 定位存在张力——framework 暗示通用性，case study 暗示特定场景。
- Contributions 列表信息密度极高，首次阅读者难以消化。

### Method (§3)
- §3.2 ISR 的 premise-count confound 应前置讨论（目前在 Appendix C），而非等到 §4.3 才暴露。
- Algorithm 1 过于简单——增加 design choices 的讨论（为什么 LOO 而非 Shapley、component 粒度选择）可提升方法论深度。

### Experiments (§4)
- §4.1 Statistical considerations 段为正面做法，但 "Statistical considerations" 后面的 claims 有时超出了这些 caveats 的约束。
- §4.2 SFT baseline: 需报告 training loss convergence。
- §4.3 Goodhart: "compositional Goodhart effect" 的定义（p.5）应标注为 observed pattern 而非新概念。
- §4.4 ProofFOL: "cross-dataset evidence" 应改为 "within-task-family replication"。

### Limitations (§6)
- 覆盖充分。3 点左右，长度合适，符合 EMNLP 2026 要求。

### Appendix
- Appendix C (Extended Discussion) 的 premise-count confound 分析质量高但位置太靠后。
- Appendix D (Hacking Mode Definitions) 是论文最有价值的部分之一，示例清晰。
- Tables 7-10 字号过小但内容完整。

### References
- 39 条引用，覆盖 GRPO、reward hacking、mutation testing、neurosymbolic reasoning 核心文献。
- 缺失 Shapley values、influence functions、ML mutation testing 近期文献。
- PRIME 和 DeepSeek-Prover-V2 已引用（R2 交叉回应中确认）。

### Format Compliance
- 页数合规：主体 8 页 + Limitations（不计入页数）+ References（不限）+ Appendix（不限）
- 匿名合规：作者信息为 "Anonymous ACL submission"
- ACL style, \usepackage[review]{acl}
- Checklist 已包含