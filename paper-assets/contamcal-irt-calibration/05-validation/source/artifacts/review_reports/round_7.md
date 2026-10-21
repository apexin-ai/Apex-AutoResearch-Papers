---
round: 7
review_mode: fresh
overall_score: 3.5 - Borderline Conference
timestamp: 2026-05-21T16:15:32.494539+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 9 (Fresh Review)

**论文**: "Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families"
**Venue**: EMNLP 2026 (ARR May cycle)
**Reviewer 编排**: 2 人（R1: 方法严谨性+实验+统计; R2: 新颖性+相关工作+写作+格式）
**审稿模式**: Fresh（重新审稿，无前轮记忆）

---

## Summary

论文通过 LoRA SFT 控制注入，以 5 个剂量水平向 4 个独立家族的 5 个模型（7B–14.7B）注入基准题目，发现污染并非一律导致分数膨胀，而是产生四种定性不同的 dose-response 模式（Immune/Collapse/V-Recovery/Benefit）。论文使用 ContamCal（RRF 多信号融合 + 2PL+γ IRT）量化污染效应并提供校准置信区间，DiD 分析未发现 item-specific memorization，跨 benchmark 迁移分析揭示方向性反转现象。

---

## Strengths

1. **研究问题精准且有实际价值**：现有文献几乎全做二元（有/无污染）比较，本文首次系统建模连续 dose-response 关系，填补了重要方法论空白。[R1,R2 共识]

2. **实验设计严谨**：控制 SFT 注入（已知 ground truth dosage）+ 4 家族 × 5 剂量 × 3 benchmark × 多 seed 的 factorial design + held-out 家族验证 + 跨 benchmark 迁移——这是为数不多遵循实验因果推断范式的 LLM 评估研究。[R1,R2 共识]

3. **IRT 框架技术实施扎实**：贝叶斯推断流程规范（R̂ < 1.01, ESS > 500, PPP 报告），收敛诊断充分，4 chains NUTS/HMC in Stan。提供校准的可信区间，对实践者有用。[R1,R2 共识]

4. **诚实报告零结果和局限**：DiD 非显著、ARC 功效不足、cross-seed CI 宽度、OLMo-2 种子敏感性均如实报告，无选择性呈现。[R1,R2 共识]

5. **附录极为详尽**：涵盖收敛诊断、功效分析、阈值鲁棒性、domain 分解、4PL 扩展等，达到高标准的可复现性（Reproducibility 4/5）。[R1,R2 共识]

6. **跨 benchmark 迁移分析有深度**：GSM8K 方向反转发现（Qwen-7B MMLU −1.8pp 但 GSM8K +10.1pp）和三种迁移模式（null/consistent/directional reversal）提供了超越单一 benchmark 的见解。[R1,R2 共识]

---

## Weaknesses（按严重程度排列）

### Must-Fix（影响接收决定）

**MF1** [critical, CONSENSUS] **分类法基于 ad-hoc 算法，缺乏正式 dose-response 建模**
- Algorithm 1 使用硬编码阈值（τ=2pp, n=5, ρ=0.3, λ=0.5pp）做规则分类，本质是描述性归纳。药理学有成熟的参数化 DR 模型（Hill 方程、4 参数 log-logistic、sigmoid Emax），可通过 AIC/BIC 做模型选择且自然提供分类不确定性。论文借用 "dose-response" 术语却未使用该领域的标准工具。Appendix P 的阈值鲁棒性测试（30 组 pass/fail）过于粗糙——无法判断某家族距分类边界多远。
- **位置**: Section 3.3, Algorithm 1 (p.5), Appendix P
- **建议**: (1) 拟合参数化 DR 模型并与 Algorithm 1 对比; (2) 至少提供 bootstrap 分类不确定性; (3) 引用 dose-response 经典文献

**MF2** [critical, CONSENSUS] **"架构决定脆弱性"因果声称超出证据**
- Abstract/Section 6/Conclusion 多处声称 "architecture rather than baseline ability determines vulnerability"。实际证据仅为：不同家族在相似 baseline 下表现不同（OLMo-2 vs LLaMA-3.1）。但"架构"之外存在大量未控制混淆：预训练数据分布与规模、tokenizer 覆盖率、合成数据策略（Phi-4）、训练步数与调度。R2 指出 Qwen 内部同架构不同规模（14B Collapse vs 7B V-Recovery）进一步削弱"架构决定"的叙事。数据能支撑的结论是"baseline ability alone does not determine vulnerability"，不是"architecture determines"。
- **位置**: Abstract, Section 1 C1, Section 5.1 ¶out-of-sample, Section 6 ¶1
- **建议**: 将 "architecture determines" 弱化为 "family-level factors beyond baseline ability"; 在 Section 6 列出未控制的混淆因素

**MF3** [critical, CONSENSUS] **N=4 家族对分类法泛化性的根本限制**
- 4 类模式恰好由 4 个家族产生：Immune (Phi-4), Collapse (Qwen-14B), V-Recovery (Qwen-7B), Benefit (OLMo-2/Gemma-2)。Collapse 和 V-Recovery 各仅 1 个家族代表。Held-out 验证仅覆盖 Immune。**§5.1 声称"each taxonomy pattern is attested in at least two independent families"与 Collapse 仅 Qwen-14B 的事实不符**——这是一个需要修正的事实错误。N=4 无法区分"4 种真实类型"和"每个家族有 idiosyncratic 行为"。规模范围 ≤14B，70B+ 模型的适用性完全未知。
- **位置**: Section 4.1, Section 5.1, Table 1
- **建议**: 将分类法定位为 "observed response profiles" / "preliminary taxonomy"; 修正 §5.1 的事实错误; 明确讨论 N=4 的泛化风险

### Should-Fix（影响评分但不一票否决）

**SF1** [warning, DIVERGENT — R2: Must-Fix, R1: Should-Fix] **LoRA SFT 注入的生态效度**
- 真实污染发生在预训练阶段（web crawl 泄露），与 LoRA SFT 注入在学习机制上截然不同。Limitations 仅一句话提及。Schaeffer et al. (2026) 展示了预训练污染下不同的 DR 关系，论文与其对比不充分。R1 反驳：控制实验需要已知 ground truth dosage，LoRA SFT 是目前唯一可控实验范式，paper 正确定位为 testbed。**共识：不否定论文贡献，但 Limitations 讨论需大幅扩展**。
- **建议**: 扩展 Limitations 中 SFT vs. pretraining 讨论; 与 Schaeffer et al. 做显式对比

**SF2** [warning, CONSENSUS] **DID 零效应过度解读**
- Section 5.4 标题 "No detectable item-specific memorization" 易被误读为"不存在 memorization"。Appendix N MDES 1.25–2.05pp 表明 ≤1.25pp 的效应无法排除。Contribution 2 使用同样过度确定的措辞。
- **建议**: Section 5.4 标题改为 "Limited Evidence for Item-Specific Memorization"; 正文报告 MDES 数值

**SF3** [warning, CONSENSUS] **LoRA r=16 统一配置的未讨论混淆**
- LoRA 相对表达能力与模型参数量成反比。Phi-4 14B Immune 可能部分源于 LoRA 容量不足。R2 反驳：Qwen-14B 同为 14B 却 Collapse，但两者架构效率不同。
- **建议**: 在 Limitations 讨论 LoRA 容量混淆; 理想情况测试 r∈{8,16,32,64}

**SF4** [warning, CONSENSUS] **曝光分数 s_ij 分类性能未报告**
- s_ij 作为核心协变量进入 IRT 模型，测量误差直接传递到 γ 估计。Ground truth 可得（控制注入已知 item membership），但未报告 s_ij 的 ROC-AUC、PR 曲线。
- **建议**: 补充 s_ij 在各 dosage 下区分 treated vs. untreated items 的分类性能

**SF5** [warning, CONSENSUS] **"65–70% MMLU 基线脆弱带"过于精确**
- 5 个数据点不支撑精确百分比区间。Gemma-2 在 ~62% 显示 Benefit（明显受影响），与"below band shows limited sensitivity"矛盾。
- **建议**: 弱化为定性描述 ("models with moderate baselines appear more vulnerable")

**SF6** [warning, CONSENSUS] **Schaeffer et al. (2026) 和 Han et al. (2026) 讨论不充分**
- 两篇最直接的竞争/互补工作：Schaeffer et al. 做预训练污染 DR，Han et al. 用 group-based DIF 量化污染。前者仅在 Conclusion 一句话提及，后者在 Related Work 一句。
- **建议**: 在 Related Work 用专段对比两篇工作的方法论差异

---

## Reviewer Consensus（[AGREE] 标记）

两位 Reviewer 在以下问题上完全一致：
1. **[AGREE]** N=4 家族泛化性不足是核心问题（MF3）
2. **[AGREE]** 因果声称"架构决定脆弱性"需降级为描述性发现（MF2）
3. **[AGREE]** DID 零效应需更审慎表述（SF2）
4. **[AGREE]** 正式 dose-response 建模或分类不确定性度量缺失（MF1）——R1 列为 Must-Fix，R2 初列 Should-Fix 后同意升级
5. **[AGREE]** 实验设计严谨、IRT 方法论扎实是明确优势
6. **[AGREE]** 附录质量高，可复现性好

## Reviewer Divergence（[REBUT] 标记）

1. **LoRA SFT 生态效度的严重性** — R2 视为 Must-Fix（"根本性不足"），R1 视为 Should-Fix（"可控实验的合理起点，加强讨论即可缓解"）。R1 提出关键反驳：预训练污染无法精确控制 dosage，LoRA SFT 是目前唯一可控实验范式。**Director 判断**：R1 论证更有说服力——作为首个系统 DR 研究，选择可控条件是合理的，但 Limitations 讨论确实需要大幅扩展。列为 Should-Fix。

2. **Calibration 基线强度** — R2 认为 Table 4 基线偏弱（Should-Fix），R1 认为基本合理（Minor）。R1 指出 ContamCal 本身即贝叶斯方法，要求"Bayesian calibration baseline"无意义；B3 (Vanilla 2PL) 已部分满足 IRT 变体对比。**Director 判断**：列为 Info，建议在附录补充 2PL vs. 2PL+γ ablation。

---

## Questions（需要作者澄清）

Q1: γ 参数的识别来源——主要从 within-model cross-item 的 s_ij 变异中识别，还是从 cross-dosage 的 s_ij 分布差异中识别？θ 和 γ 的分离依赖什么排除限制？[R1]

Q2: Algorithm 1 对输入噪声的敏感性——如果在每个 dosage 下 accuracy 加 ±1pp 均匀噪声，有多少家族的分类会变化？[R1]

Q3: Phi-4 的 Immune 是否更可能源于其大量使用合成数据的预训练策略，而非架构本身？[R1]

Q4: 将 LoRA rank 从 16 提升到 64（增加记忆容量），Phi-4 分类是否可能变化？[R1]

---

## Missing References

1. **Hill (1910)** — dose-response 建模奠基文献 [R1,R2]
2. **Ritz et al. (2015)** — `drc` R 包，4 参数 log-logistic 等标准 DR 模型 [R1,R2]
3. **Balloccu et al. (2024)** "Leak, Cheat, Repeat" (EACL 2024) — contamination 影响评估 [R2]
4. **Bordt et al. (2025)** "How Much Can We Forget about Data Contamination?" [R2, 需确认发表状态]

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未配置，跳过。

---

## Visual Layout Check（非评分项）

**状态**: ✅ 完成（耗时约 3 分钟）

**3 个 Warning**:
1. **Algorithm 1 跨页 (pp.4-5)**：伪代码 ~29 行从 Page 4 延续到 Page 5，需翻页阅读。建议压缩至单页或调整 float 位置。
2. **Figure 2 尺寸偏小 (p.8)**：DID 置信区间图压缩在约 1/4 栏宽，数据点和误差线在正常阅读距离下难以辨认。建议放大至半栏宽或用 figure* 全宽。
3. **Method 段视觉节奏单调 (pp.3-5)**：连续 3 页纯文本+公式，无 figure/table。建议增加 pipeline 示意图。

**9 个 Info**:
- Figure 1 图例字号偏小（≥9pt 建议）
- Figure 4 色阶建议确认色盲安全 colormap
- Figure 5 数字标注字号过小（~6-7pt）
- Page 13 display item 密度过高
- Table 1 排版规范 ✓
- Tables 2-3 格式规范 ✓
- Limitations 段简短、符合 EMNLP 要求 ✓
- 主正文 8 页 ✓ 符合 EMNLP 2026 限制
- 参考文献格式一致 ✓

---

## Overall Assessment

**评分**: 3.5 / 5 — **Borderline Conference**
**置信度**: 4/5（两位 Reviewer 均熟悉 IRT、LLM 评估和数据污染领域）

| 维度 | R1 | R2 | 综合 |
|------|----|----|------|
| Soundness | 3.5/5 | 3/5 | 3.25/5 |
| Excitement | 3.5/5 | 3.5/5 | 3.5/5 |
| Reproducibility | 4/5 | 4/5 | 4/5 |
| Overall | 3.5/5 | 3.5/5 | **3.5/5** |

**判断依据**：
- 研究问题重要、实验设计严谨、IRT 框架实施扎实——这些是明确的 Conference 级优势
- 三个 Must-Fix 问题（分类法缺乏统计基础、因果声称过强、N=4 泛化性不足）是阻碍 Conference 接收的主要障碍
- 关键在于：三个 Must-Fix **主要通过文本修订可解决**（弱化声称、补充讨论、添加不确定性度量），不需要推翻论文架构或重做实验
- 如果三个 Must-Fix 和主要 Should-Fix 得到充分处理，论文具备 3.5→4.0 (Conference) 的提升潜力
- 若仅部分修复，3.0 (Findings) 是合理的 fallback

---

## Detailed Comments（逐节）

### Abstract
- 过度声称 "architecture rather than baseline ability determines vulnerability"——应弱化为描述性发现
- "65–70% MMLU baseline band" 从 5 个数据点无法支撑如此精确的区间
- "No detectable item-specific memorization" 应标注 MDES

### Introduction (Section 1)
- 动机清晰，问题定义精准
- Contribution 1 中 "confirms generalizability" 对于 N=1 held-out 验证过度
- Contribution 2 "No detectable" 需加 "at current power level" 限定

### Related Work (Section 2)
- 缺少与 Schaeffer et al. (2026) 和 Han et al. (2026) 的专段对比
- 缺少 dose-response 建模经典文献引用
- 缺少 Balloccu et al. (2024), Bordt et al. (2025)

### Method (Section 3)
- 2PL+γ 模型设定合理，但先验分布应在正文给出（至少 θ 和 γ 的先验形式）
- Algorithm 1 缺乏统计基础——建议增加参数化 DR 模型或分类不确定性
- RRF 融合的 exposure score 分类性能未评估

### Experimental Setup (Section 4)
- 统一 LoRA r=16 的混淆需讨论
- SFT AUGMENT 模式说明清晰 ✓

### Results (Section 5)
- Table 1 呈现清晰 ✓
- §5.1 "each taxonomy pattern attested in ≥2 families" 对 Collapse 不成立——**事实错误**
- §5.4 标题需改为更审慎措辞; MDES 应在正文报告
- ARC PPP=0.003 应在主文讨论，不仅放附录
- Figure 1 仅 seed=42，建议加 error bars

### Discussion/Conclusion (Section 6)
- "architecture, not baseline ability alone, determines contamination vulnerability"——因果声称需降级
- 与 Schaeffer et al. 的对比仅一句话，需扩展

### Limitations
- 覆盖 3 个点（model scale, seed sensitivity, LoRA vs pretraining），结构合理
- SFT vs pretraining 讨论需大幅扩展（当前一句话）
- 应增加 LoRA 容量混淆讨论
- 应增加 instruction tuning vs continued pretraining 路径差异讨论

### Format
- ✅ 正文 8 页，符合 EMNLP 2026 Long paper 限制
- ✅ ACL review 模板
- ✅ Limitations 章节存在
- ✅ Ethics Statement 存在
- ✅ 匿名性完整
- ✅ 参考文献格式基本规范（minor year mismatches 需核查）