---
round: 15
review_mode: fresh
overall_score: 3.0
timestamp: 2026-05-22T13:09:51.306908+00:00
reviewer_ids: ['1', '2']
cross_response_reviewer_ids: ['1', '2']
force_resubmit: False
---

# 审稿报告 — Round 15 (Fresh Review)

**论文**: DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection
**目标 Venue**: EMNLP 2026 (ACL Rolling Review, May cycle)
**审稿模式**: Fresh (重新审稿)
**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计+统计有效性；R2: 新颖性+完整性+写作质量+相关工作）

---

## Summary

本文提出 DisPeD，通过 13 种 encoder 配置（7 种 Stage-1 DAPT 变体 × 3 种模型规模 125-355M）的受控消融实验，研究何种编码器适应性质驱动多轮 jailbreak 检测的跨攻击泛化。核心设计：Stage-1 变体共享冻结的 Stage-2 BiGRU 分类器，逐项隔离域暴露、分类监督、标签正确性、标签粒度、域特异性的贡献。实验覆盖 4 种 OOD 攻击家族、跨架构验证、混合 LLM 训练、人类数据（ToxicChat）验证、扰动鲁棒性、良性分布适配。主要发现：(1) 域暴露是跨攻击泛化的首要驱动力，分类监督主要贡献方差缩减；(2) 任意确定性标签划分即可触发泛化（scrambled ≈ correct on DD/FITD, d<0.1），但存在攻击复杂度依赖边界（ActorAttack d=0.44）；(3) 泛化分解为正交的攻击侧（DAPT）和良性侧（10-25 条对话 FPR 校准）两轴。

---

## Strengths

**S1. [共识] 受控消融设计精巧** — 7 种 Stage-1 变体 + 冻结 Stage-2 的设计是消融实验的范本。每个变体恰好隔离一个因素，同时保持其他一切恒定。两位 Reviewer 均给出最高评价。

**S2. [共识] 异常充分的实验覆盖** — 25 页附录包含约 38 个表格/图表，涵盖 data efficiency、temporal aggregation、causal subspace probe、cross-hardware replication (5 seeds, 不同 GPU)、length independence verification、TOST sensitivity analysis、layer-wise representation analysis 等。这是 jailbreak 检测文献中最彻底的消融研究之一。

**S3. [共识] 诚实报告不利结果** — 论文突出报告了削弱其声明的结果：ToxicChat 层级逆转 (JB-MLM 0.837 >> 9-class 0.596)、WildChat FPR 68.1%、mixed-LLM AA F1=0.504、RoBERTa-large DAPT 退化。这种诚实增强了科学可信度。

**S4. [共识] Scrambled label 结果有信息量** — 精确划定了边界：域相关的标签划分重要（topic fails），但标签正确性在模板攻击上可忽略 (d<0.1)。TOST 从 δ=5pp 到 δ=2pp、n=3 到 n=10 的系统检验尤其值得称赞。对低资源安全标注场景有直接意义。

**S5. [共识] 两轴分解概念清晰** — 攻击侧泛化（DAPT 驱动）与良性侧 FPR 缩减（目标域校准）的分离在概念上简洁，每个轴独立验证（攻击侧: Table 3; 良性侧: Tables 21-22, Appendix O-P）。

**S6. [共识] 统计实践规范** — TOST 等价检验、Cohen's d、BCa bootstrap CI（标注为 exploratory）、paired permutation tests、多种子评估——统计报告质量高于该领域平均水平。

**S7. [共识] 实用协议** — 24.3× 推理加速 vs LLM-as-judge；10-25 条良性对话 FPR 校准；总训练成本 < 4 GPU-hours on single A100。

---

## Weaknesses

### Must-Fix（影响接收决定）

**MF1. [critical, 共识] ToxicChat 证据层级逆转严重削弱核心声明的泛化范围**
- 位置：Table 5, Section 4.6, Section 5 Discussion, Section 6 Conclusion
- 在唯一的人类数据验证中，JB-MLM (0.837±0.013) 远超 9-class (0.596±0.087)——合成数据上的证据层级完全逆转。这不是边界条件，而是对论文中心论点（classification supervision > MLM）的直接挑战。
- Discussion 将逆转归因于"条件特异性优势"（多轮合成 vs 单轮人类），但这两个因素（单轮/多轮 × 合成/人类）是混淆的，论文未尝试解耦。
- Conclusion 声称 "yields a two-step protocol without target-domain attack data"，但 ToxicChat 结果表明此协议在缺乏分布匹配数据时失效。
- **建议**: (a) 截断合成越狱至单轮，检验 classification vs MLM 以隔离多轮因素；(b) Abstract/Conclusion 明确限定证据层级范围为"合成多轮设定"；(c) Discussion 提供 FP vs FN 分解和 variance 反转的机制解释；(d) 缓和 "two-step protocol" 为需要 deployment-distribution benign calibration 的协议。
- R1 评估: "对核心发现泛化性的直接挑战"（drives 3.0）；R2 评估: "根本性实际局限"（drives 3.5）。分歧在严重性，非事实。

**MF2. [critical, R1 主导] Mixed-LLM ActorAttack F1=0.504 低于 trivial baseline**
- 位置：Table 14, Section 4.5, Appendix I
- 考虑测试集类别比例（80 jailbreak : 38 benign），全预测为 jailbreak 即可达 F1≈0.808。9-class 在混合 Qwen+Llama 训练下仅达 0.504±0.107——远低于此 trivial baseline。MLM 更崩溃至 0.289（≈vanilla 0.291）。
- 这表明方法在训练数据多样性增加时对结构复杂攻击严重失效，严重限制了部署前景。
- **建议**: (a) 分析 AA 在 mixed-LLM 下的具体失败模式（LLM 风格多样性混淆 vs 单源数据量不足？）；(b) 测试中间混合比例理解退化曲线；(c) 调整实用部署声明。

**MF3. [critical, 共识] WildChat FPR=68.1% 与 10-shot 修复验证不足**
- 位置：Table 19 (Appendix O), Tables 21-22 (Appendix P)
- 9-class 在 WildChat 上 FPR=68.1%±6.4%——比 vanilla (48.1%) 更差。DAPT 加剧而非缓解 benign distribution 偏差。
- 10-shot 修复有前景（FPR→0%）但验证强度不足：(a) 评估仅 n=49 样本（95% CI 上界 6.1%）；(b) WildChat 评估集与训练同源 (IID)；(c) OASST2 需 25 条才达 FPR=1.0%±0.5%，表明修复效果随来源而异。
- **建议**: (a) 在训练未见过的良性来源上评估修复效果（真正 OOD 良性）；(b) 增大评估集规模和种子数；(c) 将 Conclusion "two-step protocol" 降格为 "preliminary evidence"。

**MF4. [warning→critical by R2, 共识降级为 warning] 系统名称 "DisPeD" 与核心发现存在张力**
- 位置：Title, Section 3
- "DisPeD = Disentangled Pattern Detection" 暗示检测依赖模式解耦，但 scrambled label 结果（Table 3: scrambled ≈ 9-class on DD）表明特定模式标签非必要。
- R2 标为 critical，R1 降级为 warning："disentangled" 可指两阶段架构设计（解耦 encoder adaptation 和 temporal classification），通过 footnote 澄清即可。
- **建议**: 重命名系统或首次出现时加 footnote 明确 "disentangled" 指两阶段架构而非标签语义。

### Should-Fix（影响评分但不一票否决）

**SF1. [共识] "判别性压缩"机制解释因果链不完整**
- 位置：Section 5, Appendix S, Figure 4
- MLM-only 已在 K≤5 时达 F1>0.97，分类监督的增量价值主要在全长度稳定性和 mixed-LLM 鲁棒性。但论文将 "discriminative compression" 呈现为独立的、更深层的机制。
- R1 反驳了 R2 关于"因果探针反映任务低维度"的质疑（Table 28: MLM 768-dim=0.636 直接证明压缩是分类特有的），但双方一致认为因果语言过强。
- **建议**: 弱化因果语言，将 compression 定位为分类监督的关联现象（correlate），而非已确立的因果机制。

**SF2. [共识] 相对 Zhang et al. (2021) / Maennel et al. (2020) 的新颖性界定不充分**
- 位置：Section 5 ("extends Zhang et al. in the opposite direction")
- Scrambled label 发现是已知现象（分类信号诱导表征压缩）在安全域 encoder adaptation 的实例化。"Opposite direction" framing 不准确——Zhang 展示 memorization → generalization (fine-tuning 后)，本文展示 random-like labels → OOD generalization，底层机制一致。
- **建议**: 重新框架为"验证 random-label 泛化现象扩展到 encoder adaptation 安全域，并发现域相关标签划分是必要条件"。

**SF3. [共识] Abstract 信息密度过高**
- ~250 词内含 12+ 具体数值（"125-355M"、"60 percentage points"、"d<0.1"、"d=0.44"、"24.3×" 等），核心研究问题被数字淹没。
- **建议**: 以研究问题和关键 surprising finding (scrambled labels work) 开头；保留 2-3 个最关键数值；细节移至 Introduction。

**SF4. [共识] Contribution 2 (complexity-dependent boundary) 证据基础狭窄**
- 仅基于 DD/FITD（模板）vs ActorAttack（结构复杂）的对比，2-3 个数据点。"Structural complexity" 未正式定义。
- **建议**: 降级为观察性发现（observation），或正式定义 complexity（如 role shift 数量、topic 变化、对话深度）。

**SF5. [R1 主导] 对话长度混淆在主文未讨论**
- 良性 12-20 turns vs 越狱 3-10 turns 零重叠。Appendix U 有三个控制实验（truncation FPR=0%, K=1 F1=0.773, padding AA Δ=-57.9pp），但主文完全未提及。
- **建议**: 在 Section 4 或 5 简要讨论长度混淆及 Appendix U 的控制实验结论。

**SF6. [R1 主导] "方差缩减 4-20×" 声明基于 n=3 seeds**
- n=3 时方差估计 CI 极宽。Cross-hardware replication (Table 39, n=5) 中 4.6× 更可信。
- **建议**: 软化为 "observed 4-20× lower variance across 3 seeds"。

**SF7. [R1 主导] Table 15 (1000-conversation) 退化削弱 "composition not scale" 声明**
- 9-class DD 从 0.994 降至 0.889，MLM 崩溃至 0.338。缺乏隔离 composition 和 scale 的受控实验。
- **建议**: 从 1000 中重采样 350 训练并比较；审慎限定声明。

**SF8. [R1 主导] BCa bootstrap 跨 seed 池化可能违反独立性**
- 论文已标记 "exploratory"，这是恰当的。但主文仍使用池化 CI 作为关键证据。
- **建议**: 每个 seed 内独立计算 CI 并报告范围，或使用分层 bootstrap。

---

## Reviewer Consensus [AGREE]

1. **ToxicChat 逆转是本论文最核心的问题** — 证据层级在唯一人类验证集上完全反转，直接限制核心贡献的适用范围。两位 Reviewer 一致要求在 Abstract/Conclusion 限定 claim scope 为合成多轮设定。
2. **消融方法论是本文最大贡献** — 7 Stage-1 变体 + 冻结 Stage-2 的设计是同类研究范本，25 页附录展现罕见的实验彻底性。
3. **Scrambled label 结果有信息量** — 精确划定了"标签正确性在模板攻击上可忽略但在结构复杂攻击上有中等影响"的边界。
4. **Abstract 信息密度需降低** — 数值过多淹没核心研究问题。
5. **Complexity-dependent boundary 应降级为观察** — 证据基础仅 2-3 个数据点。
6. **系统命名需要调整或澄清** — "Disentangled Pattern Detection" 与 scrambled label 发现存在张力。
7. **判别性压缩的因果语言需弱化** — 应定位为关联现象而非已确立机制。Table 28 中 MLM 768-dim=0.636 证明压缩是分类特有的（R1 有效反驳了 R2 的"任务低维度"解读），但因果链仍不完整。
8. **Zhang/Maennel 的增量贡献需更准确表述** — 应框架为已知现象在安全域的验证+域相关性作为必要条件。

---

## Reviewer Divergence [REBUT]

**主要分歧：ToxicChat 逆转的严重性评估**
- R1 (3.0): 视为"对核心发现泛化性的直接挑战"——论文核心贡献是证据层级，层级在唯一人类数据上逆转则贡献范围大幅收窄。补充人类多轮验证或解耦单轮/多轮因素可改变此评估。
- R2 (3.5): 视为"根本性实际局限"但方法论贡献（controlled ablation design）本身足以 borderline Conference。证据层级在其范围内（合成多轮）有效。
- **Director 判断**: R1 的论点更有说服力——论文标题和 Introduction 的框架 ("What representation properties enable cross-attack generalization?") 暗示的范围远超合成多轮设定。如果核心发现仅在合成数据上成立，从方法论角度看是 sound 但 excitement 受限。

**次要分歧：系统命名严重性**
- R2: critical (标题是 meta-reviewer 首先看到的)
- R1: warning (命名选择非科学错误，footnote 可解决)
- **Director 判断**: 介于两者之间。命名确实制造认知失调，但不影响科学结论。标记为 should-fix。

---

## Questions for Authors

**Q1. [R1]** ToxicChat 逆转能否解耦？截断合成越狱至单轮后比较 classification vs MLM，可隔离多轮因素与合成/人类因素。

**Q2. [R2]** 若 MLM 在 ToxicChat 上最优，对实践者的推荐是什么？分类监督在人类数据上有害——此叙事需要直接面对。

**Q3. [R1]** Causal subspace probe (Table 28) 的训练/测试划分具体是什么？如果 probe 在同分布数据上训练和评估，则仅证明线性可分。

**Q4. [R2]** Scrambled label 实验是否测试了多个标签排列（Stage-1 标签分配 seed），还是仅单一排列？TOST 10 seeds 是分类训练 seed 还是标签 scrambling seed？

**Q5. [R1]** Mixed-LLM AA F1=0.504 的 per-seed 分解？是否有某个 seed 贡献了大部分退化？

**Q6. [R1]** Qwen3-8B 策略标注的具体 prompt 是什么？

---

## Missing References

两位 Reviewer 共同识别的遗漏（按相关性排序）：

1. **Hsu et al. (2024)** "Improved Large Language Model Jailbreak Detection via Pretrained Embeddings" (arxiv 2412.01547) — 同样使用 pretrained encoder embeddings 进行 jailbreak detection，**直接相关**
2. **M2S** (March 2025, arxiv 2503.04856) — Multi-turn to Single-turn 转换检测方案，作为替代架构方法
3. **TrajGuard** (Xie et al., 2026, arxiv 2604.07727) — streaming hidden-state trajectory detection，与 BiGRU temporal aggregation 直接相关
4. **SAE as Jailbreak Mitigators** (Feb 2026, arxiv 2602.12418) — SAE-based defense via feature-level steering

注：TrajGuard (April 2026) 和 SAE Mitigators (Feb 2026) 可能在投稿 timeline 之后发表，作者应自行判断 timeline 合理性。

---

## External Review (Stanford Agentic Reviewer)

外部审稿未配置（`external_review.paperreview_ai.enabled` 未启用）。

---

## Visual Layout Check（非评分项）

视觉审查已完成（3 warnings, 8 info, 0 critical）。

**Warnings:**
1. **Page 5**: Figure 2 两个子图尺寸偏小，axis tick labels 和 legend 约为正文字号的 50-60%，打印后可能难以辨认。建议放大为 `figure*` 全宽或增大字号至 ≥8pt。
2. **Page 8**: Discussion (§5)、Conclusion (§6)、Limitations (§7) 三个 section 全部挤在同一页，Discussion 段落仅约 6-7 行。审稿人可能认为 Discussion 不够充分。
3. **Page 14**: Tables 8-9 列数多（≥8列），字号明显小于正文，阅读体验较差。建议拆表或使用 landscape。

**Info 项（参考）:**
- 首页无视觉锚点（Figure 1 在 page 2）
- Figure 2 color scheme 未验证色盲友好性
- Figure 3 热力图 cell 内数字在低分辨率打印可能模糊
- Figure 4/5 共享一页，每图尺寸受限
- Figure 6 y 轴标签字号偏小
- 表格 booktabs 风格一致 ✓，参考文献格式统一 ✓，无 margin 溢出 ✓

---

## Overall Assessment

**Overall: 3.0 (Findings)**

| 维度 | R1 | R2 | 加权 |
|------|-----|-----|------|
| Soundness | 3.5/5 | 4.0/5 | 3.5/5 |
| Excitement | 3.0/5 | 3.0/5 | 3.0/5 |
| Reproducibility | 4.0/5 | 4.0/5 | 4.0/5 |
| Confidence | 4/5 | 4/5 | 4/5 |

**评分理由**:

本文最大贡献在于消融方法论本身——13 种配置 × 3 规模的受控设计是该领域的范本，25 页附录展现了罕见的实验彻底性，不利结果的诚实报告增添了科学价值。Scrambled label 发现和两轴分解框架均有信息量。

然而三个关键问题将论文限制在 Findings 水平：

**(1) 核心发现范围受限**: 证据层级（classification > MLM > vanilla）在唯一人类验证集 ToxicChat 上完全逆转（JB-MLM 0.837 >> 9-class 0.596）。论文框架暗示的泛化范围（"What representation properties enable cross-attack generalization?"）远超实际证据所支撑的范围（合成多轮 Qwen3-8B 数据上的跨攻击家族泛化）。

**(2) 部署鸿沟未弥合**: WildChat FPR 68.1%（DAPT 恶化而非改善）+ 10-shot 修复仅在 n=49 IID 样本上验证。Mixed-LLM ActorAttack F1=0.504 低于全预测 trivial baseline (~0.808)。"Two-step protocol" 的实际可靠性未充分建立。

**(3) 新颖性有限**: 核心技术（DAPT）非新方法；scrambled label 发现与 Zhang et al. (2021)/Maennel et al. (2020) 的增量区分不足；"opposite direction" framing 不准确。

论文适合 Findings：方法论 sound、发现在其范围内有 insight、统计实践规范。若能 (a) 补充人类多轮验证或解耦 ToxicChat 逆转因素、(b) 更严格的良性侧评估、(c) 修正 claim scope 以匹配实际证据范围，有潜力在后续周期达到 Conference 水平。

---

## Detailed Comments

### Abstract / Introduction
- Abstract 以研究问题开头是好的，但随后 12+ 数值淹没了核心 insight。保留"Llama Guard 3 detects only 1.8%"、"classification DAPT 0.97-1.0 vs vanilla 0.28-0.31"、"24.3× speedup"三个关键数据即可。
- Introduction 三个贡献中，C1（systematic ablation）有充分支撑；C2（deterministic partition sufficiency）应限定为观察性发现；C3（two-step protocol）应降格为 preliminary evidence。
- "DisPeD = Disentangled Pattern Detection" 应在首次出现时 footnote 澄清 "disentangled" 指两阶段架构解耦。

### Method (Section 3)
- 7 变体设计精巧，每个恰好隔离一个因素。Table 1 清晰。
- κ=0.78 属于"substantial"但未达 "almost perfect"(0.81+)，对 AA (d=0.44) 更相关。建议明确此差异化影响。
- 建议在 Section 3.2 简要提及 BiGRU 选择动机（便于表示分析而非优于 mean pooling）。

### Experiments (Section 4)
- 主文应简要讨论长度混淆（benign 12-20 vs jailbreak 3-10 turns 零重叠）及 Appendix U 控制实验结论。
- "Cross-attack generalization" 和 "OOD" 混用——建议在 Section 4 开头更精确定义 OOD 指 attack-family shift。
- Table 2 caption 应添加 "OOD F1 reflects attack-side generalization only; benign samples are IID"。
- "Variance reduction 4-20×" 应软化为 "observed" 或提供 n≥5 seed 支撑。
- Table 15 (1000-conversation) 退化需受控 scale 实验（从 1000 中重采样 350）才能支撑 "composition not scale" 声明。

### Discussion (Section 5)
- "Discriminative compression" 应弱化因果语言——Table 28 证明压缩是分类特有的，但因果链（compression → generalization）仍有缺口。
- "Extends Zhang et al. in the opposite direction" 应修正为更准确的增量定位。
- ToxicChat 逆转的讨论段落过短（约 3 行）。应扩展为独立 paragraph，包含 FP/FN 分解和 variance 反转机制。

### Conclusion (Section 6)
- "Two-step protocol without target-domain attack data" 需加入 caveat：需要 deployment-distribution benign calibration，且协议在人类数据上未验证。
- 建议更突出 ActorAttack 非等价结果（d=0.44）。

### Limitations (Section 7)
- 覆盖合理但可更明确地承认：(a) 证据层级仅在合成多轮设定下成立；(b) 10-shot benign 修复为 IID 验证，非 OOD。

### Format
- 使用 `\usepackage[review]{acl}` ✓
- `\author{Anonymous}` ✓
- Limitations section 存在且不计页数 ✓
- Discussion/Conclusion/Limitations 挤在 page 8——建议适度压缩确保阅读舒适度
