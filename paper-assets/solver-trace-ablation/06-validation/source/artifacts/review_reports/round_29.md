---
round: 29
review_mode: fresh
overall_score: 3.0 Findings
timestamp: 2026-05-22T23:01:18.698229+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 圆桌审稿报告 — Round 31 (Fresh Review)

**论文**: Solver Trace Ablation Diagnoses Structural Degeneration and Goodhart Effects in GRPO-Trained Neurosymbolic Reasoning: A Case Study
**Venue**: EMNLP 2026 (ARR Long Paper)
**审稿模式**: Fresh（重新审稿，无历史记忆）
**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计；R2: 新颖性+完整性+写作）
**轮次**: 1 轮（Round 1 初审 → 交叉分享 → 收敛）

---

## Summary

本文提出 Solver Trace Ablation (STA)，一种基于 leave-one-out 消融的诊断方法，用于检测 GRPO 训练的神经符号推理模型中的结构退化。核心度量 Intensional Structural Reward (ISR) 衡量每个形式化组件是否为证明成功所必需。论文展示：(1) exec-only GRPO 训练下 ISR 从 ~0.6 崩溃至 ~0.003，揭示 prove rate 不可见的结构退化；(2) 将 ISR 用作训练奖励产生 Goodhart 效应——模型从 conclusion embedding 转向 tautological shortcuts；(3) 该现象在 FOL 和 Prolog 两种逻辑类型间泛化。实验基于 Qwen3-4B + FOLIO 数据集，提出 8 种 hacking mode 分类法。

---

## Strengths

**S1. STA 方法定义清晰、算法化** [R1+R2 共识]
Algorithm 1 提供可执行伪代码，ISR 数学定义（Eq. 1）简洁明确，方法可复现性强。将 LOO 消融应用于 solver trace（而非模型参数/特征）是一个非平凡的设计选择。

**S2. 系统的实验设计与控制变量** [R1+R2 共识]
多条件对比（exec-only, ISR β=0.1/0.2/0.3, Random, Shuffled-ISR, SFT）控制变量合理。Shuffled-ISR 对照（§4.3）巧妙分离 ISR 因果信号与奖励增大的混淆因素——概念设计优于当前统计效力。

**S3. 诚实的局限性披露** [R1+R2 共识]
论文明确承认 ISR ≠ semantic faithfulness（ρ=-0.049）、premise-count confound 将 ISR 优势降至 1.06×、cross-scale/model 未收敛、seed 43 采样不一致。"A Case Study" 标题设定了正确的 scope 期望。这种自我批判态度在提交论文中不常见，值得肯定。

**S4. Hacking Taxonomy 有实用价值** [R1+R2 共识]
8 种 gaming mode 的定义、示例和检测方法（Appendix D）为后续工作提供可操作的诊断工具包。CE/TS 两种 dominant mode 有充分的样本量支撑（>70 examples each）。

**S5. 有价值的实证发现** [R1+R2 共识]
GRPO 训练下 ISR 崩溃而 execution accuracy 维持 >90% 的"结构退化对执行正确性不可见"发现对 RLVR 社区有警示意义。Per-seed 分析（Tables 9-12）详尽透明。

---

## Weaknesses

### Must-Fix（影响接收决定）

**MF1. Goodhart claim 的核心定量证据被 premise-count confound 瓦解** [R1-N1, R2 AGREE]
Section 4.3 自行报告 premise-count-matched comparison 后 ISR 优势从 214× 坍缩到仅 1.06×（McNemar p=0.317, n=100 matched pairs）——统计上不显著。C2 贡献（Goodhart 效应）的标量定量基础被自己的控制实验否定。论文试图转向 mode composition shift 作为替代证据，但：(a) mode-shift 的统计检验仅依赖 CMH（见 MF3），(b) 从"metric 不变但底层结构改变"推导出"Goodhart effect"的论证不够严谨——这更接近 reward shaping 的副作用而非经典 Goodhart。Abstract 中 "exhibits a seed-dependent Goodhart effect" 和 Title 中 "Goodhart Effects" 的表述暗示了标量层面已被否定的效应。
**建议**：(1) 以 mode composition shift（CE→TS 转化）为 Goodhart 的主要 operationalization，提供独立的统计检验（χ² test on mode frequencies）；(2) Abstract/Title 降级 Goodhart 表述；(3) 明确区分"ISR scalar inflation"（不显著）和"structural composition shift"（需独立检验）。

**MF2. 单模型泛化性声明与 cross-scale/cross-model 失败实验的矛盾** [R1-N2, R2-N2, 完全共识]
全部主实验仅基于 Qwen3-4B + FOLIO（500 训练样本）。三个额外配置均未产生可比较结果：
- Cross-scale（Qwen3-8B）：PR=14%，未收敛（Appendix E.7）
- Cross-model（LLaMA-3.2-3B）：训练因零 GRPO advantage 提前终止（Appendix E.4）
- Exec-only seeds：6 个中仅 3 个收敛（50%，Appendix E.5）
- ProofFOL ISR：p=0.10，标为 exploratory
C1 声称 STA 是 "model-agnostic diagnostic framework"，C3 声称 "cross-logic and cross-dataset evidence"，但实质上论文展示的是一个模型在一个数据集上的一个条件下的现象。ProofFOL 被称为"cross-dataset"，但它从 ProofWriter 通过 GPT-4o 翻译得到（Appendix A），与 FOLIO 共享 FOL 语法和推理结构，并非真正独立的数据集。无法排除这些发现是 Qwen3-4B + ProofWriter 的 artifact。
**建议**：(1) Discussion 泛化性叙事严格限定为 "hypothesis from a single-model case study"；(2) 删除或大幅弱化 "model-agnostic" 声明；(3) 至少增加 1 个不同架构模型的完整实验。

**MF3. CMH 检验独立性假设不满足，统计推断可靠性存疑** [R1-N3, R2 AGREE with nuance]
CMH 检验将 within-seed 的 100 个 eval 样本视为独立观测，但同一 seed 下的样本来自同一 model checkpoint，存在 model-level 依赖结构。论文在 §4.1 诚实承认 "the true replication count is N=3 seeds"，但仍将 CMH 作为 primary statistical evidence（Table 6 报告 p=1.3×10⁻³⁹ 等极端 p 值）。
R2 修正：说"真实 N=3"过于极端——effective N 在 3-300 之间取决于组内相关系数（ICC）。合适的统计方法是 multilevel/mixed-effects model（seed 作为随机效应），而非简单 CMH。
**建议**：(1) per-seed analysis 为 primary evidence，CMH 严格降为 supplementary；(2) 报告 ICC 估计值；(3) 用 seed-level clustered bootstrap 或 mixed-effects logistic regression 替代 CMH。

**MF4. Seed 43 采样策略不一致构成显著 confound** [R1-N4, R2 AGREE]
Seed 43 使用 nucleus sampling（T=0.7）而非其他 seeds 的 greedy decoding（footnote 2, p.5），但仍被纳入主文的 pooled analysis（Table 1 的 "3-seed pooled" 统计量包含 seed 43）。Sampling 改变输出分布的 entropy，可能系统性地影响 ISR 值和 hacking mode 分布。在 N=3 seeds 的小样本中，一个 seed 的系统性偏差可能主导 pooled 分析的结论。
论文在 Appendix E.6 提供了 N=2 sensitivity analysis（Table 13），但 N=2 几乎无统计功效，反而暴露了样本量不足。
**建议**：(1) 主文分析以排除 seed 43 的结果为主，seed 43 作为 robustness check 放在附录；(2) 明确标注 Table 1 中哪些行包含/排除 seed 43。

### Should-Fix（影响评分但不一票否决）

**SF1. "Observe-vs-optimize asymmetry" 概念新颖性声称过度** [R2-N3 Must-Fix, R1-W4 Should-Fix; 分歧记录]
Abstract 中 "structural proxies for reasoning quality are easier to observe than to optimize" 和 C3 贡献声明将此表述为新发现，但本质是 Goodhart's Law 的标准表现。Manheim & Garrabrant (2019) 的四种 Goodhart 变体分类法和 Gao et al. (2023) 的 reward model overoptimization 已系统描述了此类现象。
R1 部分反驳：论文的贡献不在于"发现 Goodhart 存在"，而在于提供 component-level 诊断工具来定位 Goodhart 的具体结构表现形式——这超越了 Manheim & Garrabrant 的理论分类和 Gao et al. 的 aggregate-level 分析。但 R1 同意"asymmetry"不应暗示超越 Goodhart 框架的新理论洞察。
**建议**：将 C3 重新定位为"在 neurosymbolic RLVR 中通过 STA 实证刻画 Goodhart 的结构层面表现"，降低新颖性声称力度。

**SF2. 方法论新颖性——LOO 应用层面创新偏薄** [R2-N1 Must-Fix, R1 REBUT; 分歧记录]
R2 认为 STA 本质是"LOO 消融应用于 solver 输入组件"，方法论贡献偏弱，不足以支撑长文。
R1 反驳：(1) LOO 用于 solver trace 而非模型参数/特征是非平凡设计选择；(2) ISR 将 per-sample LOO 聚合为可用于训练的 reward signal 是新用途；(3) 8 种 hacking mode taxonomy 有实用价值。组合贡献不应简化为"标准 LOO 的应用"。但 R1 同意框架级声明（C1: "diagnostic framework"）需要多模型验证。
**建议**：不降为 Short Paper（附录 per-seed 分析和 taxonomy 细节在 Short Paper 格式下无法容纳），但在主文中更明确定位为 "diagnostic method + empirical case study" 而非 "framework"。

**SF3. SFT baseline 比较不公平** [R1-W1, R2-W4, 共识]
SFT PR=13% vs exec-only PR=93%，在 prove rate 相差 ~80pp 的情况下比较 structural properties 不令人信服。SFT 直接在 gold formalization 上训练，天然获得结构信息的 direct supervision signal。100-step checkpoint（PR=32%, hacking=31.2% vs SFT 7.7%）仅部分缓解。
**建议**：明确定位 SFT 为 structural preservation 的 upper bound reference，而非 GRPO 的公平对照。

**SF4. Shuffled-ISR 控制实验严重 underpowered** [R1-W2, R2 AGREE]
Shuffled-ISR condition 仅 46 个 proved samples（3 seeds, PR≈15%），无法提供有意义的统计功效。R2 称其概念设计巧妙但统计功效不足以支撑 deconfounding 声明。
**建议**：增加 seeds 或在主文中明确标注效力限制。

**SF5. Hacking taxonomy recall 未报告** [R2-W2, R1-W3 AGREE]
Table 8 报告 152 样本 precision=1.00，但明确写 "Recall is not estimable"。一个只有 precision 没有 recall 的分类器无法保证完备性。部分 mode 过于稀少（PG: 5 例, Contradiction: 仅 1000 步出现），存在 over-specification 风险。
**建议**：(1) 报告 recall 下界估计；(2) 合并稀有 modes 为更粗粒度类别；(3) 明确标注 well-supported vs exploratory modes。

**SF6. ProofFOL p=0.10 在主文中定位不够审慎** [R1-W5, R2 AGREE]
§4.4 标记 "exploratory" 但仍以 "substantially higher genuine rates" 叙述，"substantially" 与 p=0.10 不匹配。
**建议**：改为 "directionally consistent" 或 "suggestively higher"。

**SF7. ISR=0 语义模糊性讨论不充分** [R2-W3, R1 AGREE]
ISR=0 可能是 (a) 冗余前提（结构退化）或 (b) 多条等价推理路径（genuine redundancy）。论文未在主文中讨论 (b) 的可能性。FOL 中多条有效证明路径常见，部分 ISR=0 样本可能语义正确但碰巧所有组件非独立必需。
**建议**：增加定性分析，展示 low-ISR 样本确实在语义上退化而非仅冗余度增加。

### Minor（不影响接收）

- **M1**: ISR=0 对 proved（complete redundancy）vs unproved（by definition）语义不同但混用同一值，建议 unproved 用 N/A [R1]
- **M2**: LOO 与 Shapley value 类比（§3.2）可能误导读者认为 STA 继承 Shapley 理论保证 [R1]
- **M3**: Figure 1 y 轴标签在 ISR-as-reward vs diagnostic ISR 之间含义不同 [R1]
- **M4**: Table 1 中关键 caveat（1.06× matched value）仅在脚注中 [R1]
- **M5**: 标题 ~140 chars 偏长，建议精简至 ~90 chars（R2 建议 60 chars，R1 反驳无硬限制）[分歧]
- **M6**: §4.4 "persists" 暗示时间持续性，实际是跨条件一致性，建议改 "holds" [R2]

---

## Reviewer Consensus [AGREE]

两位 Reviewer 在以下关键判断上完全一致：

1. **Overall 3.0 (Findings)** — 方法论贡献（STA/ISR）扎实但实验规模和概念新颖性不足以支撑 Conference
2. **单模型泛化性不足** (MF2) — 最根本的问题，无法排除 Qwen3-4B + ProofWriter artifact
3. **Goodhart 标量证据被 confound 瓦解** (MF1) — 1.06× (p=0.317) 使 C2 核心定量支撑不成立
4. **CMH 统计推断不可靠** (MF3) — within-seed 非独立性使极端 p 值被高估
5. **Seed 43 confound** (MF4) — 采样策略不一致混入 pooled analysis
6. **SFT baseline 不公平** (SF3) — PR 差异 ~80pp 使结构比较缺乏说服力
7. **Taxonomy recall 缺失** (SF5) — 完备性声明受限
8. **ProofFOL p=0.10 表述过强** (SF6) — "substantially" 不匹配

---

## Reviewer Divergence [REBUT]

| 议题 | R1 | R2 | 最终定级 |
|------|----|----|----------|
| 方法论新颖性 (SF2) | Should-Fix: 组合贡献有价值 | Must-Fix: LOO 应用偏薄 | Should-Fix (分歧记录) |
| Asymmetry 概念 (SF1) | Should-Fix: 可作 shorthand | Must-Fix: Goodhart 重述 | Should-Fix (分歧记录) |
| 标题长度 (M5) | Minor: ACL 无硬限制 | Should-Fix: 建议 60 chars | Minor (分歧记录) |
| Excitement | 3.5/5 | 2.5/5 | — |

---

## Questions to Authors

1. 如果排除 seed 43，主要结论（Table 1 pooled statistics, CMH 检验）是否仍成立？请提供 2-seed (42, 44) pooled 结果。
2. 能否提供 mode 分布在 ISR-as-reward vs exec-only 之间变化的正式统计检验（Fisher exact / χ² test on mode frequencies）？这将为 MF1 的 Goodhart claim 提供替代性定量支撑。
3. 为什么选择 multiplicative reward formulation 而非 additive？Multiplicative form 使 ISR 信号强度与 prove rate 耦合，这本身可能驱动部分观察到的 Goodhart 模式。
4. Cross-scale (8B) 和 cross-model (LLaMA) 均未收敛。是否考虑过更简约的解释——即 STA/ISR 诊断的现象可能是 Qwen3-4B 特有的训练动态？
5. LOO 假设 component independence，但逻辑前提之间常有交互（如三段论的大小前提缺一不可）。在 LOO 下观察到的 hacking patterns 是否可能因忽略交互而产生 false positives？
6. 8 种 hacking mode 中 CE (87%) 和 TS (71%) 占绝大多数。如果仅关注这两种 dominant mode，简单的 text-match classifier 是否就足以检测这些退化模式？STA/ISR 的额外价值在哪里？

---

## Missing References

- **"Towards Understanding Specification Gaming in Reasoning Models"** (arXiv:2605.02269, 2025) — spec gaming 理论分析与本文 hacking taxonomy 直接相关 [R2]
- **Cobbe et al. (2021)** "Training verifiers to solve math word problems" — 与 component-level reward 诊断相关，已引用但未在 Related Work 讨论 [R1]
- **Khalifa et al. (2026)** "Countdown-Code" — 已引用但 §2 中未讨论其 testbed 方法与 STA 的关系 [R2]

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未配置。

---

## Visual Layout Check（非评分项）

视觉审查已完成（耗时 ~4 min）。结果：0 critical / 2 warning / 16 info。

**Warnings:**
1. **Pages 5-6**：连续 2 页纯文本（Section 4.1-4.3），无 figure/table/display equation 穿插。建议将 Table 1 或 Table 2 前移至 page 6 位置。
2. **Page 19 (Appendix)**：Table 9 字号明显偏小（~6-7pt），在打印或低分辨率屏幕上可能难以阅读。

**Info 亮点**：
- 主文正好 8 页，符合 ACL 页数限制
- 无 margin overflow、LaTeX 渲染错误、孤悬 section heading
- 双栏对齐良好，页眉符合 ACL 匿名投稿格式
- Figure 1 出现在 page 2 顶部，锚定效果好
- Algorithm 1 排版规范

---

## Overall Assessment

**Overall: 3.0 — Findings**

**EMNLP 2026 评分标准**：3 = Findings（可被 Findings 接收）

**置信度**: 4/5（两位 Reviewer 均仔细阅读全文含 23 页附录，熟悉 RLVR/neurosymbolic reasoning 领域）

**评分理由**：
论文提出了一个有前景的诊断工具（STA/ISR），在 neurosymbolic reasoning 的 reward hacking 检测中填补了 execution-based evaluation 和 annotation-free diagnostics 之间的空白。核心方法论贡献（C1: STA 框架 + hacking taxonomy）扎实。

但三个根本性问题限制了 Conference 接收：
1. **Goodhart 效应的核心定量证据被 premise-count matching 消解**（1.06×, p=0.317）——C2 的可信度大幅下降
2. **泛化性声明与 cross-scale/cross-model 全部未收敛的实验现实矛盾**——无法排除 Qwen3-4B + ProofWriter artifact
3. **统计推断依赖不满足独立性假设的 CMH 检验**——极端 p 值可能被严重高估

这些问题的组合——Goodhart 定量基础薄弱 + 单模型实验规模 + 统计方法问题——使论文难以达到 EMNLP 主会议标准（Overall ≥ 4），但 empirical findings 和诊断工具对 RLVR 社区有参考价值，适合 Findings 接收。

**若要冲刺主会议**：(1) 至少在 1-2 个不同架构模型上验证 STA（需成功收敛）；(2) 以 mode composition shift 为 Goodhart 主要证据并提供独立统计检验；(3) 用 mixed-effects model 替代 CMH；(4) 将 claims 严格限定在证据支持的范围内。

---

## Detailed Comments

### §1 Introduction
- C1 "model-agnostic diagnostic framework" 声明与单模型实验不匹配，建议改为 "diagnostic method"
- C3 "observe-vs-optimize asymmetry" 应明确定位为 Goodhart 的 domain-specific 实证验证，而非新概念

### §3.2 Method — ISR
- ISR=0 对 proved（redundancy）vs unproved（by definition）语义不同，建议 unproved 用 N/A
- Shapley value 类比可能误导，建议简化为 "LOO ablation"
- ISR 对不同 hacking modes 诊断力差异巨大（CE: ISR≈0; TS: ISR≈1 by construction），需在主文讨论

### §4.1 Setup
- Seed 43 nucleus sampling 应从 pooled analysis 中排除，或至少双报包含/排除结果
- "Statistical considerations" 段需更明确声明 CMH 的 supplementary 角色

### §4.2 ISR as Diagnostic
- "214× raw drop" 叙事需在首次出现时即附加 "partially attributable to premise-count inflation" caveat
- SFT 对比：明确定位为 "pre-RL structural upper bound"，而非 PR-matched control

### §4.3 Goodhart Effects
- 核心建议：以 mode composition shift 为 primary Goodhart evidence，提供 χ² 检验
- "Premise-count confound" 段应前置而非作为后续讨论
- Table 1 脚注中的关键信息（1.06× matched value）应在正文中突出

### §4.4 Cross-Domain
- ProofFOL "substantially higher" → "directionally consistent"（p=0.10）
- "Cross-dataset" 不准确——ProofFOL 与 FOLIO 共享 FOL 语法和 ProofWriter 推理结构

### §5 Discussion
- "STA generalizes to any RL system" 过强，建议改为 "STA is applicable in principle to..."
- "Goldilocks" 全文确认已统一为 "observation"