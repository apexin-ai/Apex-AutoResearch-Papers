---
round: 18
review_mode: fresh
overall_score: 3.0 - Findings
timestamp: 2026-05-22T23:01:44.847271+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 18 审稿报告 — DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection

**Target Venue**: EMNLP 2026 (ARR May 2026)
**Deadline**: 2026-05-25 (AoE)
**Reviewer Panel**: Reviewer 1 (方法严谨性 + 实验设计 + 统计方法), Reviewer 2 (新颖性 + 完整性 + 写作质量 + 格式)
**Review Mode**: Fresh (无跨轮记忆)

---

## Summary

本文提出 DisPeD，一个两阶段 pipeline (DeBERTa encoder + frozen BiGRU)，通过 13 种 encoder 配置的控制消融研究，将多轮越狱检测的跨攻击泛化分解为 attack-side (discriminative compression via classification DAPT) 和 benign-side (few-shot domain adaptation) 两个正交轴。核心发现：在合成多轮数据上，domain-relevant classification objectives（包括 scrambled labels）足以实现跨攻击泛化 (OOD F1=0.97-1.0)，而 MLM 在 mixed-LLM 条件下崩溃；10-25 条 benign 对话可将 FPR 降至部署水平。但核心 evidence hierarchy 在人工数据 (ToxicChat) 上完全逆转 (JB-MLM 0.837 > 9-class 0.596)。

---

## Strengths

1. **系统性消融设计** [S1, 共识]：7 个 Stage-1 变体 × 3 种 encoder 架构 × 多 OOD 攻击家族，在 jailbreak detection 领域罕见的 factorial controlled study。每个变体隔离单一因素 (label granularity, label correctness, supervision type, domain relevance)，具有方法论示范价值。

2. **结果呈现透明度极高** [S2, 共识]：主动报告所有 negative results——ToxicChat 层级反转、mixed-LLM 崩溃 (AA F1=0.504)、WildChat FPR 68.1%、RoBERTa-large 逆转。这在投稿论文中不常见。

3. **丰富的 Appendix** [S3, 共识]：26 页中 14 页 Appendix，覆盖 error analysis、cross-LLM validation、TOST sensitivity、scale validation、SVD layer-wise analysis、cross-hardware replication 等，显著增强可重复性。

4. **统计工具箱完善** [S4, 共识]：TOST 等价性检验 (扩展至 10 seeds)、BCa bootstrap CI、permutation test、Fisher ratio、CKA 的组合使用，优于同领域多数论文。per-seed verification (Table 39) 和 cross-hardware replication (Table 41) 提供了额外稳健性证据。

5. **Representation analysis 有洞察力** [S5, R2 发现]：Appendix T discriminative probe 显示 classification DAPT 的 top-3 SVD 维度即可实现完美 ActorAttack 检测 (vs MLM 用全部 768 维仅 0.636)，提供了质性不同（而非仅量变）的 representation structure 证据。

6. **Pipeline 高效实用** [S6, 共识]：DeBERTa+BiGRU 仅需 868MB GPU、<5 分钟训练，比 LLM-as-judge 快 24.3×（deployment cost comparison, 非 contribution claim）。

---

## Weaknesses

### Must-Fix（影响接收决定）

**MF1** [critical, 共识] **核心 evidence hierarchy 仅在合成数据上成立，人工数据上完全逆转**
- ToxicChat (408 human-written conversations): JB-MLM 0.837±0.013 > Binary 0.705 > Scrambled 0.616 > 9-class 0.596±0.087 (Table 5)
- 论文核心 contribution "domain-relevant classification objectives suffice for cross-attack generalization" 仅在 Qwen3-8B 合成多轮数据上验证
- Abstract "this advantage reverses on human-authored single-turn data" 过于轻描淡写，未传达这是对核心 claim 的根本性限制
- ToxicChat 同时变化两个因素 (synthetic→human + multi-turn→single-turn)，无法归因。Appendix Z.1 truncation 实验 ("truncation widens the 9-class advantage") 暗示但未 conclusively 证明 multi-turn vs single-turn 是主因
- 65% 的 ToxicChat gap 来自 false positives (FPR 0.510 vs 0.167)，表明 classification DAPT 在 domain transfer 时产生系统性误判
- **要求**：(1) Abstract/Introduction 显著呈现此限制——明确 hierarchy 目前仅在 single-LLM synthetic multi-turn data 上验证；(2) 分析逆转原因 (synthetic single-turn 实验可区分两个因素)；(3) 弱化 "deterministic partition sufficiency" 为条件性结论

**MF2** [critical, 共识] **"Structural complexity" 缺乏形式化定义**
- 论文反复区分 "template attacks" (DD, FITD) 和 "structurally complex attacks" (ActorAttack)，基于此提出 "complexity-dependent boundary" 作为核心 Contribution 2
- "Structural complexity" 从未被形式化定义。Limitations 承认 "structural complexity is not formally defined"，但这个概念是论文两个核心 contribution 之一的基础
- 没有 operationalizable 定义，读者无法判断新攻击属于哪一类，也无法预测模型表现
- **要求**：(1) 提出可操作的复杂度 proxy (对话轮数方差、策略转移熵、模板匹配度) 并验证与检测难度的相关性；(2) 或将 claim 降级为观察性——"我们观察到 ActorAttack 更难检测"而非 "存在 complexity-dependent boundary"

### Should-Fix（影响评分）

**SF1** [warning, 共识] **新颖性受限——DAPT 有效性是已知结论的 domain-specific 确认**
- "Continued pretraining on domain data improves downstream performance" 与 Gururangan et al. (2020) "Don't Stop Pretraining" 高度一致
- Two-stage pipeline 与 DeepContext 架构等价 (Section 4.1 自承认)
- Scrambled ≈ correct labels 在 template attacks 上有趣但在 ActorAttack 上 TOST 不通过 (p=0.183, d=0.44)——在"难"的 case 上 label correctness 可能 matters
- **缓解因素**：R1 指出控制消融的方法论贡献不应简化为 "DAPT confirmation"——scrambled 等价性、两轴分解、MLM mixed-LLM collapse 有独立价值
- **建议**：重新定位核心 novelty 为消融发现集合 (scrambled equivalence + MLM fragility + discriminative subspace) 而非 "DAPT works"

**SF2** [warning, 共识] **"Discriminative compression" 因果框架超出证据支撑**
- SVD/CKA/Fisher/discriminative probe 均为 correlational evidence
- Section 5 措辞 ("Classification DAPT compresses features") 暗示因果关系
- Appendix T probe (3/768 dims → perfect AA detection) 提供了质性差异证据但仍非因果
- **建议**：将因果 framing 降级为 "consistent with / suggestive of"；讨论至少一种替代解释 (如 task-relevant feature memorization)

**SF3** [warning, 共识] **缺少与已发表多轮检测方法的直接实验对比**
- DeepContext, BIID, G-Guard, JailDAM 均仅在 Related Work 讨论，无直接实验
- Appendix R BERT-base proxy 确认架构不是关键差异但无法替代直接对比
- 论文未说明缺少直接对比的原因 (代码不可用? 评估 protocol 不兼容?)
- **建议**：至少增加一段解释为何缺少直接对比，并提供方法比较表

**SF4** [warning, 共识] **Mixed-LLM 结果过弱**
- Mixed-LLM training: AA F1=0.504±0.107 低于 majority-class baseline (~0.808)
- MLM 完全崩溃到 vanilla 水平 (0.289)
- Cross-LLM pilot 每 family n=10，95% CI 下界仅 72.2%
- Abstract "shows partial robustness under mixed-LLM training" 与 AA=0.504 不匹配
- **建议**：标注为 exploratory/pilot；Abstract 措辞需更精确限定

**SF5** [warning, 共识] **RoBERTa-large 逆转削弱 DAPT 必要性论证**
- Vanilla RoBERTa-large (355M) AA F1=1.000 vs 9-class DAPT 0.946——DAPT 有害
- 所有 continued pretraining 降低大模型 AA 性能 (representation drift)
- DAPT 效用是 scale-dependent 的，但 Abstract/Conclusion 未传达此限定
- **建议**：Discussion 明确 DAPT 适用范围为 small-to-medium encoders

**SF6** [warning, 共识] **Benign-side 适应评估为 IID**
- WildChat/OASST2 的训练和评估数据同源 (GPT-3.5 users / OASST2 crowdsource)
- 论文自承认 "this is therefore an IID evaluation of benign coverage, not an OOD generalization test"
- Introduction "10-25 target-domain conversations reduce FPR from 58-68% to 0-1.5%" 可能给读者 OOD 泛化成功的印象
- **建议**：在 Introduction/Conclusion 相关 claim 中加入 "(IID evaluation)" 限定

**SF7** [warning, 共识] **样本量较小，部分统计 claim 效力有限**
- OOD 测试集 76-118 条 (单个 FN 导致 ~1.3pp F1 波动)
- "4-20× variance reduction" (std 0.005 vs 0.115) 基于 n=3 seeds，F-test (2,2 df) 几乎无 power
- Population std (N divisor) 在 n=3 时低估不确定性约 18%——论文已声明但读者可能忽略
- **缓解因素**：10-seed TOST、per-seed ordering (Table 39)、cross-hardware (Table 41) 提供了多层补充验证
- **建议**：variance reduction claim 降级为 "observed directional pattern"；正文简要论证 TOST 5pp margin 选择

**SF8** [warning, R2-W5 / R1 REBUT] **Abstract 信息密度过高**
- 10 行内包含 F1 数值、两轴分解、速度比较、人工数据逆转 caveat
- 核心 message ("domain-relevant classification triggers discriminative compression") 被数字淹没
- R1 反驳: 问题不在密度而在 claim calibration——ToxicChat 逆转和 benign IID 条件未充分体现
- **共识**：claim calibration 比密度更重要；精简 Abstract 聚焦核心 finding 有益但非必须

---

## Reviewer Consensus [AGREE]

1. **ToxicChat 层级反转是论文最根本的问题** [R1-N2 + R2-N1, 双方 AGREE]
2. **"Structural complexity" 需要形式化定义或降级为观察** [R2-N3 + R1 AGREE]
3. **DAPT 有效性已知，控制消融有方法论价值但需重新定位 novelty** [R2-N2 + R1 AGREE with nuance]
4. **Discriminative compression 应降级为 correlational interpretation** [R1-W1 + R2 AGREE]
5. **缺少直接实验对比是 weakness** [R1-W2 + R2 AGREE]
6. **Mixed-LLM AA=0.504 过弱，Abstract 措辞需修正** [R2-W4 + R1 AGREE]
7. **RoBERTa-large 逆转需在 Discussion 深入讨论** [R2-W1 + R1 AGREE]
8. **TOST 5pp margin 需论证** [R1-W3 + R2 AGREE]
9. **Overall 3.0 (Findings)** [双方一致]

## Reviewer Divergence [REBUT]

1. **OOD benign IID disclosure 是否充分** [R1 Must-Fix → R2 REBUT]
   - R1 认为 disclosure 不足，OOD F1≈0.97 的 caveat 在 Abstract 不明显
   - R2 提供文本证据：Abstract 第 7 行已有 "(attack-side OOD, benign IID)"；Section 4 术语段已形式化定义；Table 2-3 caption 均标注
   - **Director 判定**：R2 rebuttal 有效——论文已在多处标注。但缺少双重 OOD (attack OOD + benign OOD 同时) 评估是合理的 Should-Fix (SF6)

2. **n=3 seeds 统计问题是否构成 Must-Fix** [R1 Must-Fix → R2 REBUT]
   - R1 认为方差比较无统计效力，population std 有偏
   - R2 指出论文已有 10-seed TOST (p < 10⁻⁸)、per-seed ordering (Table 39, 所有 pairwise orderings 每 seed 一致)、cross-hardware (Table 41)、明确 population std 声明；核心等价性结论不依赖 3-seed 方差
   - **Director 判定**：R2 rebuttal 部分有效——核心结论的统计基础因多层补充验证基本稳固，但 "4-20× variance reduction" claim 需降级。降为 Should-Fix (SF7)

3. **Abstract 信息密度** [R2 Should-Fix → R1 REBUT]
   - R2 认为需精简；R1 认为问题在 claim calibration 而非密度
   - **Director 判定**：分歧为偏好差异，不影响核心结论

---

## Questions to Authors

1. 能否提供 benign 也 OOD 的完整双重 OOD 评估 (OOD attack + OOD benign，不注入额外 domain 数据)？这将量化 F1≈0.97 中有多少来自 benign-side IID 优势。
2. ToxicChat 层级反转的根因：是 single-turn vs multi-turn 的差异，还是 synthetic vs human 的差异？用 Qwen3-8B 生成 single-turn jailbreak 测试（保持 synthetic），如层级反转则 single-turn 是主因。
3. 能否对 "structural complexity" 提出至少 1-2 个可量化 proxy (如策略转移熵、对话轮数方差)?
4. 能否对 "4-20× variance reduction" claim 提供 formal test (Levene's test) 的 p-value？如 power 不足则降级为 descriptive observation。

---

## Missing References

**R2 建议（需验证真实性）**:
1. Attention-Aware GNN-based Input Defense (2025) — GNN 建模 turn 间关系，与 encoder-based 方法有对比价值
2. Active Honeypot Guardrail System (2025) — 主动探测多轮越狱意图，代表不同防御范式
3. Representation Bending for LLM Safety (2025) — representation-level safety 的另一方法
4. "A Representation Engineering Perspective on the Effectiveness of Multi-Turn Jailbreaks" (2025) — **高度相关**，从 RepEng 角度分析多轮越狱，与本文 CKA/t-SNE/probe 分析直接对话

**R1 注意**：Reviewer 建议的引用有时为 hallucinated references，需优先验证第 4 篇的真实性。

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未请求。项目配置中未启用 paperreview.ai 外部审稿线。

---

## Visual Layout Check（非评分项）

**状态**: 完成 (2026-05-22 22:42 → 22:45, ~4 分钟)
**结果**: 0 critical, 2 warning, 18 info

**Warnings**:
1. **Pages 3-4 连续纯文本**：Method §3 + Experiments §4 开头无任何 figure/table/equation 穿插，审稿人容易失去视觉节奏。建议插入公式或伪代码块。
2. **Figure 3 (Appendix, p.15) 策略转移矩阵热力图标签过小**：9×9 矩阵策略标签 ≤6pt，屏幕和打印均难辨认。

**Info highlights**:
- 主正文 8 页，符合 EMNLP 2026 限制。Limitations + Ethics 在 page 9，不计入。
- Display items: 2 figures + 5 tables = 7 个 / 8 页 ≈ 0.875/页，密度适中。
- 所有表格使用 booktabs 风格，无竖线，最优值加粗。
- 未发现 margin 溢出、公式渲染错误、section heading 孤悬等问题。
- References ~3.5 页，格式统一，无 [?] 未解析引用。
- Figure 2 legend/axis label 字号偏小 (~60-65% 正文字号)，打印版可能吃力。

---

## Overall Assessment

**Overall Score: 3.0 (Findings)**
**Confidence: 4/5**

这是一项设计严谨、呈现透明的控制消融研究，对理解 encoder adaptation 在多轮越狱检测中的作用有贡献。13 种 encoder 配置的系统性实验设计、多层统计验证 (TOST/bootstrap/permutation)、以及对 negative results 的诚实报告是论文的核心优势。

**阻碍提升至 Conference (4.0) 的核心原因：**
1. **External validity 不足**：核心 evidence hierarchy 仅在 single-LLM synthetic multi-turn data 上成立，在 ToxicChat 人工数据上完全逆转。这不是边缘限制，而是对论文最核心 claim 的根本性挑战。
2. **新颖性有限**：DAPT 有效性是已知结论 (Gururangan 2020) 的 domain-specific 确认；pipeline 与 DeepContext 等价；scrambled labels 等价性在难攻击上不成立。控制消融的方法论有价值，但核心 insight 的 novelty 不足以支撑主会议。
3. **核心概念未定义**："structural complexity" 是两个 contribution 之一的基础但缺乏形式化定义。

**Findings 级别的理由：**
- 系统性消融设计在该领域罕见，具有方法论参考价值
- 两轴分解 (attack-side + benign-side) 虽非革命性但是有用的分析框架
- 透明度和可重复性标准高
- Few-shot benign adaptation 的实用价值（尽管 IID 评估）
- 24.3× inference speedup 的部署价值

**建议接收为 Findings paper**，前提是 camera-ready 中：(1) 显著收窄 evidence hierarchy 的适用范围声明，(2) 将 "structural complexity" 降级为观察或提供形式化定义，(3) 重新定位核心 novelty 为消融发现集合。

---

## Detailed Comments

### Abstract & Introduction
- Abstract 第 7 行 "(attack-side OOD, benign IID)" 标注已到位——但 "this advantage reverses on human-authored single-turn data" 过于轻描淡写。建议改为明确 scope 限定："these findings are established on synthetic multi-turn data generated by a single LLM; the evidence hierarchy reverses on human-authored single-turn data (Section 4.6), indicating condition-specific rather than general mechanisms"
- "shows partial robustness under mixed-LLM training" (Abstract) 与 AA F1=0.504 < majority baseline 不匹配。需修正为 "template attacks remain detectable while structurally complex attacks degrade substantially (F1=0.504)"——论文当前措辞已接近此表述但 "partial robustness" 仍有误导
- Contribution 2 "deterministic partition sufficiency with complexity-dependent boundary" 的 "structural complexity" 需要定义或降级
- Introduction 中 "24.3× inference speedup" 已正确标注为 "a deployment cost comparison"——保持

### Method (Section 3)
- 7 个变体的设计清晰，每个隔离单一因素
- Strategy annotation (κ=0.78, n=50) 质量不高但因 scrambled 等价性而重要性降低——论文已正确处理这一矛盾
- Footnote 1 ("Disentangled refers to...systematic disentanglement") 仍循环——建议改写

### Experiments (Section 4)
- Section 4.1 Data 段落的 IID/OOD 数据划分清晰度已改善，但 Table 2 caption 可在表内更明确定义
- Section 4.2 evidence hierarchy 的 inline 排列格式过于紧凑——建议改为换行或小表
- F1 报告方式不完全一致 (MLM-only IID 单 seed, OOD 3 seed; 有脚注但容易混淆)
- Turn-count baseline (F1=0.42-0.56) 有效排除了长度混淆——这一数据在 Section 4.2 Summary 中的呈现位置合适

### Discussion (Section 5)
- "Condition-specific advantage" 段落正确分析了 ToxicChat 逆转但需更深入
- "Discriminative compression" 的因果语言需系统性降级
- RoBERTa-large 逆转的 implication (DAPT scale-dependent utility) 需更深入讨论
- Mean pooling ≈ BiGRU 的 implication ("detection is turn-level anomaly aggregation") 已有讨论

### Limitations (Section 7)
- 覆盖了 3 个关键限制 (synthetic data, benign-side evaluation scope, persuasion-only scope)
- 符合 EMNLP 2026 规范（简短，~8 行，不计入页数）

### Format Compliance
- ✅ 正文 8 页（Section 6 Conclusion 在 page 8 底部结束）
- ✅ ACL style template (acl.sty with [review] option)
- ✅ Double-blind (author = "Anonymous", 无 self-citation 泄露)
- ✅ Limitations section 存在
- ✅ Ethics statement 存在
- ✅ Checklist 未在 PDF 中（注释说明在 OpenReview form，符合 EMNLP 2026 要求）
- ✅ Appendix 双栏格式
- ✅ References 格式基本统一（部分 arXiv preprints 未标注 arXiv，可接受）