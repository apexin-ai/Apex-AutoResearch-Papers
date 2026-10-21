---
round: 11
review_mode: fresh
overall_score: 3.5
timestamp: 2026-05-22T13:40:33.147709+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 14 (Fresh)

**论文**: Beyond Self-Consistency: Why Self-Extracted Symbolic Constraints Show No Evidence of Improving LLM Reasoning
**Venue**: EMNLP 2026 (ARR May 2026)
**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计+统计分析；R2: 新颖性+完整性+Related Work+写作质量）
**审稿模式**: Fresh（重新审稿，无历史轮次记忆）

---

## Summary

本文研究 Self-Consistency (SC) 的一个零成本扩展——Symbolic Invariant Consensus Aggregation (SICA)，从推理链中提取逻辑约束并用 MAX-SAT (Z3) 选择最佳答案。在 6 个开源 LLM（7B–32B）+ 9 个模型（含 frontier）、3 个逻辑推理数据集、3000+ 条件评估上，论文发现 SICA 无显著改善（aggregate sign test: 5+/10−, p=0.30），并将失败归因于 Symbolic Confirmation Bias (SCB)：83.3% 的自提取约束支持错误多数答案（BR 1.66×–4.97×），MAX-SAT 在 94.4% 的问题上退化为 majority voting。论文提出三个诊断工具（K_eff, BR, C₀），测试了 27 种 training-free 补救策略（全部失败），并通过 cross-architecture NLI 验证证明外部验证可打破瓶颈（+6.67pp ProofWriter, p<0.001）。

---

## Strengths

**S1. 统计方法论异常扎实。** McNemar exact test + BH FDR correction + TOST equivalence test + Bootstrap CI + Power analysis 构成四重互补检验体系。10 个 underpowered 条件的 MDE 被透明报告（Appendix E），体现统计诚实性。在负面结果论文中达到极高水准。[R1 S1, R2 S1, 共识]

**S2. 实验规模和系统性覆盖令人信服。** 6 模型 × 3 数据集 × ~3000 condition-evaluations，覆盖 7B–32B 能力谱。Oracle control (+29.90pp Mistral, +14.22pp Qwen-14B FOLIO, +17.17pp ProofWriter) 有效分离 mechanism soundness 与 extraction quality，将问题精确定位到约束提取环节。[R1 S2, R2 S1, 共识]

**S3. 结构性归因超越简单否定。** Shuffle control（BR_null ≈ BR_obs, p>0.7）、process-level independence analysis（ProcessSim 0.69 vs κ 0.46）、CCR 分析（cross-arch CCR>0 vs same-model CCR<0）系统解释了*为什么*失败。这不是"一个方法不行"而是对失败机制的量化诊断。[R1 S3, R2 S2, 共识]

**S4. 补救分析近乎穷举。** 27 种 training-free 策略跨 4 类（prompt/method/trace-filtering/scoring）系统测试，全部 neutral-to-negative，显著增强了负面结论的说服力。[R1 S4, R2 S3, 共识]

**S5. 叙事结构清晰自洽。** CJT 理论 → SICA 方法 → 负面实验 → SCB 诊断 → Symbolic Mirage 形式化 → remediation 失败 → cross-arch escape，逻辑链完整。[R1 S5, R2 S5, 共识]

**S6. 附录详尽（~19 页）。** Case studies、prompts、algorithms、ablations、统计分析齐全。[R1 implied, R2 S5, 共识]

---

## Weaknesses

### Must-Fix（影响接收决定）

**N1. [critical, 共识] 标题声明范围显著超出实验证据覆盖面。**
标题说"LLM Reasoning"但全部主实验仅覆盖逻辑推理（FOLIO/ProofWriter/LogiQA）。数学推理（GSM8K）仅 n=30 pilot，StrategyQA/ARC-Challenge 仅出现在附录诊断中。当前社区对 symbolic verification 的主要兴趣在数学推理领域——标题 overclaim 是 *ACL 审稿常见降分理由。
- **R1**: critical（首提）
- **R2**: major（W4），交叉后同意 R1
- **建议**: 标题改为"Formal/Logical Reasoning"，或补充 GSM8K/MATH 中等规模实验（n≥200）

**N2. [critical→major, 共识] Symbolic Mirage Hypothesis 的验证存在部分循环论证。**
三个 predictions 中，Prediction 1（BR>1 across architectures）和 Prediction 2（no same-model intervention reduces BR below 1）本质上是对已观察数据的事后总结。只有 Prediction 3（cross-architecture escape）涉及独立数据。
- **R1**: major（N2, 首提循环论证角度）
- **R2**: critical（N1, 从新颖性角度；交叉后同意循环论证观点，但指出 Pred1 覆盖 9 模型超出初始 3 个为缓和因素）
- **建议**: 将 Pred 1-2 重定位为"observations that motivate the hypothesis"，仅 Pred 3 为 genuine prediction。降低"Hypothesis"措辞为"Diagnostic Framework"或"Empirical Pattern"

### Should-Fix（影响评分但不一票否决）

**W1. [major, 共识] Cross-architecture escape 证据不足以支撑结论强度。**
仅 6 个条件（4 generators × 1 dataset significant），单一 verifier 类型（NLI），仅 Mistral-7B 组合达到统计显著（+6.67pp, p<0.001）。NLI 三分类与 MAX-SAT 约束验证在任务性质上有本质区别，论文未充分讨论此 task gap。Capability gap 的单调性基于 n=6 数据点（共享 verifier 后有效 n 更小），Limitations 已标注 p=0.167。
- **R1**: major（W1）
- **R2**: major（W2），交叉后完全同意
- **建议**: 增加 generator/verifier 组合；讨论 NLI vs 约束逻辑验证的 task gap；结论措辞软化为"preliminary evidence"

**W2. [major, 共识] 8 页正文信息过载，关键贡献展开不足。**
§5.5（Remediation）仅 ~15 行总结 27 种策略；§6（Cross-Architecture）约半页完成方法+结果+分析；§7（Discussion）被压缩在 page 8 底部约 1/3 页，design principles 各仅一句话。
- **R2**: critical（N2, 首提）
- **R1**: 同意但降级为 major（8 页硬限制下空间约束真实存在）
- **建议**: 压缩 §3.1 CJT/K_eff 推导（非原创公式），将 ProcessSim/CCR 细节移入附录，腾出空间给 §5.5 深度分析 3-5 种代表性策略和 §7 Discussion

**W3. [major, 部分分歧] Claim scope 与统计功效不完全匹配。**
Abstract "no evidence of improvement" 暗示 SICA 确实无效，但 16 个非退化条件中 10 个 underpowered（MDE>2pp at 80% power），仅 4 个通过 TOST 等价检验。
- **R2**: major（W1）
- **R1**: REBUT——"no evidence"是统计学标准用语（absence of evidence），sign test + bootstrap CI + oracle control + 27 remediation 构成多层证据汇聚。但同意 Abstract 可增加 hedge。
- **建议**: Abstract 增加 power caveat，如"with Y conditions remaining underpowered for effects below ~2pp"

**W4. [moderate, 共识] BR 计算子集大小（n_err）未报告。**
高准确率模型（SC>80%）上错误子集可能<40题（Gemini-2.5-Pro interim n_err≈12），BR 统计可靠性存疑。
- **R1**: moderate（W3）
- **R2**: 同意
- **建议**: Table 2 增加 n_err 列

**W5. [moderate, 共识] Fleiss' κ 作为 ICC 近似仅有中等经验验证（r=0.625）。**
高准确率时 Fleiss' κ 系统性偏低（prevalence paradox），可能高估 K_eff。
- **R1**: moderate（W2）
- **R2**: 同意，但指出论文已声明 ordinal diagnostic
- **建议**: 报告 ICC 直接计算值作 robustness check

**W6. [minor-to-major, R2 首提] Related Work 遗漏近期重要工作。**
SETS (2025, self-verification 正面效果) 与本文负面发现形成直接对比但未被讨论。MAV (2025, multi-agent verification) 与 §6 高度相关。
- **R1**: 部分同意（需注意 concurrent submissions）
- **R2**: minor-to-major（W5）
- **建议**: §2 增加 SETS 等工作讨论，明确本文负面结论的适用边界

**W7. [minor, 共识] TOST equivalence margin ±2pp 选择依据不够充分。**
论文已有 margin sensitivity（±1/2/3pp），但正文呈现不够显著。
- **建议**: 在 §4.2 增加 margin sensitivity 结果摘要

### 小问题（不影响接收）

- 术语负载过重（SC/SICA/SCB/CJT/BR/K_eff/C₀/CCR/ProcessSim/DRC/TOST/MDE/FDR），建议增加术语表或减少非核心缩写 [R2, R1 同意]
- Table 1 "Type C" 标注缺少正文解释 [R1]
- GSM8K pilot (n=30) 应在首次出现处明确标注 "exploratory only" [R1]
- 多种子复制仅覆盖 2/6 模型 [R1, R2]
- Figure 1 仅展示正常流程，缺少 SCB failure mode 的视觉表现 [R2, R1 同意]
- Abstract 约 200 词内塞入 5 个技术概念，过于密集 [R2, R1 同意]

---

## Reviewer Consensus [AGREE]

1. **标题必须限定范围**：当前"LLM Reasoning"与实验仅覆盖逻辑推理不匹配 [R1-N1, R2-W4]
2. **Symbolic Mirage Predictions 1-2 非独立验证**：应重定位为归纳性观察 [R1-N2, R2 同意]
3. **Cross-architecture 证据为 preliminary**：仅 Mistral-7B 组合显著，需软化结论 [R1-W1, R2-W2]
4. **正文空间分配需优化**：§3.1 CJT 推导可压缩，腾出空间给 §5.5/§6/§7 [R2-N2, R1 同意]
5. **统计呈现可改善**：BR n_err 报告、TOST margin sensitivity 正文呈现、power statement 前移 [R1-W3/W5, R2-W1]
6. **Oracle control 是论文核心优势**：有效证明 mechanism soundness 并精确定位失败环节 [R1, R2]
7. **27 种 remediation 的穷举搜索是重要贡献**：全部失败显著增强负面结论说服力 [R1, R2]

## Reviewer Divergence [REBUT]

1. **Symbolic Mirage 新颖性**
   - R1（Excitement 3.5/5）: Z3 formal solver 使场景非平凡——论文证明的是"即使加了 external solver，extraction 仍注入偏差使验证层失效"，超越 Huang et al. 的一般性 self-correction 框架。BR 量化和退化条件（Eq.4）是新贡献。
   - R2（Excitement 2.5/5）: 核心发现在 Huang/Stechly 已知结论下可预见性较高。BR 只是简单比例度量。"Hypothesis"措辞偏强。
   - **Director 判断**: R1 的 Z3 区分论点有道理——formal solver 场景确实是 self-correction 文献未覆盖的具体化验证，但 R2 关于概念新颖性有限的评价也合理。建议降低"Hypothesis"措辞，但保留 SCB 量化作为独立贡献。

2. **"No evidence" 表述**
   - R1: 统计学标准用语，多层证据汇聚支撑
   - R2: 10/16 underpowered 时需更审慎
   - **Director 判断**: 表述技术上准确，但 Abstract 应增加 power caveat 避免过度解读

---

## Questions

Q1. 对 BR > 1 的模型，如果只保留与 ground truth 一致的约束（oracle filter 而非 full oracle），accuracy 如何变化？这比 full oracle 更接近"提升约束质量"的实际路径。[R1]

Q2. SETS (2025) 报告 self-verification 在 test-time scaling 中有正面效果。本文负面发现仅限于 symbolic constraint extraction 场景吗？两者机制差异的边界是什么？[R2]

Q3. 27 种 remediation 是否穷尽了合理方法空间？trained constraint extractor 和 ensemble of diverse extractors 是否被考虑过？[R1]

Q4. DeBERTa NLI verifier 的 standalone accuracy 在 FOLIO 上是多少（PW 上已报告 55.00%）？verifier error 与 generator error 的重叠模式如何？[R1, R2]

Q5. QwQ-32B 的高 SC baseline 导致的 ceiling effect 与 SCB 的相对贡献如何区分？[R2；R1 REBUT: 中等 SC regime 同样无改善，SCB 是更根本机制]

---

## Missing References

- SETS (2025, arXiv:2501.19306): self-verification 在 test-time scaling 中的正面结果，与本文负面发现直接对比 [R2, R1 部分同意]
- MAV (2025, arXiv:2502.20379): 多验证器扩展 test-time compute，与 §6 高度相关 [R2]
- Reflexion (Shinn et al., 2023): 自然语言反馈 self-correction，与 symbolic extraction 的差异可供讨论 [R1; R2 认为 minor]
- 注：Lightman et al. (2024) 和 Weng et al. (2023) 已被引用（R2 交叉回应确认）

---

## External Review

**状态**: 未请求（项目未配置外部审稿）

---

## Visual Layout Check（非评分项）

**状态**: 已完成（0 critical, 2 warning, 20 info）

**Warnings:**
1. Pages 3–5 连续 3 页无正式 display item（Figure 1 在 p2，Table 1 在 p6，跨度 4 页），审稿人可能产生"纯文本墙"印象。p5 的 Empirical Finding 灰色框部分缓解。
2. 末页（p27 appendix）仅顶部约 10 行文字，~90% 空白。

**正面:**
- 全文无 margin overflow、公式渲染错误、undefined references
- 表格全部使用 booktabs 风格，精度统一
- 颜色使用打印友好
- 主文 display items 5 个/8 页 = 0.63/页，对分析型论文合理
- 页数合规：正文 8 页 + Limitations 不计入限制

---

## Overall Assessment

**Overall Score: 3.5 / 5 (Borderline Conference)**

**置信度: 4/5**

| 维度 | R1 | R2 | 综合 |
|------|-----|-----|------|
| Soundness | 4/5 | 4/5 | 4/5 |
| Excitement | 3.5/5 | 2.5/5 | 3/5 |
| Reproducibility | 4/5 | 4/5 | 4/5 |
| Overall | 4 (Conference) | 3.5 (Borderline) | 3.5 (Borderline Conference) |

**综合评分理由:**

本文在方法论严谨性和实验系统性上达到了负面结果论文的高水准（Soundness 4/5），统计分析全面、Oracle control 有效、27 种 remediation 近乎穷举。然而，核心发现的新颖性存在争议（Excitement 2.5–3.5/5）：R1 认为 formal solver 场景的具体化验证有独立价值，R2 认为在 Huang et al. self-correction 框架下可预见。

两个共识问题压低了评分：(1) 标题"LLM Reasoning"显著超出实验覆盖面（仅逻辑推理），需限定或补实验；(2) Symbolic Mirage Hypothesis 的三个 predictions 中两个为事后总结，削弱了框架的预测力。Cross-architecture escape 作为建设性出路有价值但证据初步（仅 Mistral-7B 显著）。8 页正文的空间分配需优化。

**如果标题限定范围 + Symbolic Mirage 措辞调整 + Abstract 增加 power caveat，本文可达到 Conference 水准（4.0）。** 核心负面发现（SCB + formal verification layer vacuity）和诊断工具（K_eff, BR, C₀）对 neuro-symbolic reasoning 社区有实际价值。

---

## Detailed Comments

### §1 Introduction (p.1–2)
- "No prior work has systematically evaluated this"（p.1）表述准确但需在 §2 中更充分讨论为什么 symbolic extraction 被预期能不同于一般 self-correction（即 Z3 formal solver 作为 external component 的预期优势）
- Contributions 列表清晰（3 项），但 Contribution #1 措辞偏强（"first quantitative characterization"需确认 Stechly 等人未提供类似量化）
- Figure 1 pipeline 图清晰，但缺少 SCB failure mode 的可视化

### §2 Related Work (p.3)
- 覆盖面广（5 段落，~48 引用），specification-generation vs trace-extraction 的三范式分类有效
- 缺少 SETS (2025) 等 test-time scaling 正面结果的讨论
- 与 Huang et al. 的增量贡献可以更明确

### §3 Background & Setup (p.4–5)
- K_eff 公式（Eq.1）来自 Kish/Fleiss，非原创——§3.1 花费约半页推导可压缩
- SICA pipeline（§3.2）描述完备，Eq.2–4 推导清晰
- Symbolic Mirage Hypothesis（§3.3）：BR 定义合理，但三个 predictions 中 1-2 为事后归纳
- Empirical Finding 1-2 的灰色框格式是正面的视觉元素

### §4 Experiments (p.5–6)
- 模型选择合理（7B–32B + frontier cross-model），数据集覆盖逻辑推理三个子域
- 超参数（K=12, T=0.7, T_ext=0.3, α=0.5）各有依据
- Table 1 专业（booktabs, 显著性标记清晰），但 Type C 标注需正文解释
- Oracle control 是论文最强证据之一
- §4.2 应在正文增加 power statement 而非仅在 Appendix E

### §5 Analysis (p.6–8)
- §5.2 SCB 分析是论文核心贡献，shuffle control 优秀
- §5.3 ProcessSim 和 §5.4 CCR 可考虑移入附录以腾出空间
- §5.5 Remediation 正文仅~15行，建议深度分析3-5种代表性策略

### §6 Cross-Architecture (p.8)
- DeBERTa NLI proof-of-concept 有价值但证据初步
- Table 3 仅 Mistral-7B 显著；capability gap hypothesis 基于 n=6
- 需讨论 NLI classification vs symbolic extraction 的 task gap

### §7 Discussion (p.8)
- 被压缩至约 1/3 页，design principles 各仅一句话
- 对 neuro-symbolic reasoning 社区的实际指导不足

### Limitations (p.9)
- 覆盖了主要弱点（模型范围、英语仅、untrained extractors、power limitations、capability gap n=6）
- 简短（约 1/3 页），符合 EMNLP 规范

### 页数合规
- 正文 8 页 + Limitations 不计入限制 ✓
- ACL review template ✓
- Double-blind（Author: Anonymous）✓
- 无身份泄露检测到 ✓