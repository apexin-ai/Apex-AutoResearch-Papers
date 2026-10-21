---
round: 3
overall_score: 3.0
timestamp: 2026-05-17T17:42:09.550359+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 4 (Fresh Review)

**论文**: "Decomposing Contamination from Calibration: An IRT Approach to LLM Benchmark Evaluation"
**Venue**: EMNLP 2026 Main Conference (ACL Rolling Review May 2026 cycle)
**截止日期**: 2026-05-25

**Reviewer 编排**: 2 名 Reviewer
- Reviewer 1: 方法严谨性 + 实验设计 + 统计推断
- Reviewer 2: 新颖性 + 论文完整性 + 写作质量 + 格式合规

**轮次**: Round 1 独立审稿 → 交叉分享 → 收敛（无 REBUT，1 轮即达共识）

---

## Summary

本文提出 ContamCal，一个两阶段框架：Stage 1 通过 Reciprocal Rank Fusion (RRF) 融合多种 contamination detection signals 生成 per-item exposure scores；Stage 2 将 exposure scores 嵌入 contamination-augmented IRT model (2PL+γ) 估计 decontaminated ability。核心实验在 Qwen2.5 (0.5B-3B) 上通过 LoRA SFT injection 在 MMLU/ARC/GSM8K 上进行受控 contamination 实验。主要发现是 null result：SFT-injected contamination 的 aggregate effect 仅 ~0.6-0.7pp，raw accuracy 已是最佳估计器，ContamCal 不优于 raw accuracy（Table 3: MAE 0.006 vs 0.009）。论文转向 diagnostic value 叙事，报告 γ 在 ARC 上 CI excluding zero 以及 MMLU Social Sciences 域级显著性。附带发现包括 Min-K%++ 在 0.5B 的 directional reversal 和 γ recovery 需 J≥50 的 identifiability 边界。

---

## Strengths

1. **受控实验设计精良**：24 个模型（3 scales × 4 dosages × 2 seeds）的 within-family design 在 contamination 研究中少见，严格隔离 dosage 为唯一自变量（§4.1）。

2. **诚实的科学态度**：坦率承认核心方法不优于 raw accuracy（Table 3），九项 limitations 全面且具体，negative result 的透明报告值得肯定。

3. **Identifiability analysis 有理论价值**：Simulation study（20 conditions × 10 seeds × 200 runs）建立的 AUC/J 边界（§5.3, Figure 2）为未来 IRT-based contamination diagnosis 提供定量指导。

4. **Min-K%++ directional reversal 发现有实用价值**：0.5B 上 Cohen's d = -1.55 to -1.98 的 reversal（§5.2）是重要的 practitioner warning，具有独立引用价值。

5. **跨领域理论连接**：将 IRT item compromise/explanatory IRT/DIF 框架引入 LLM contamination analysis（§2 ¶3），理论基础扎实。

6. **写作质量整体良好**：无 AI 写作标志（无 em-dash、-ing phrases 可控），术语定义完整（calibration disambiguation §2 ¶4），引用格式规范。

---

## Weaknesses

### Must-Fix（影响接收决定，6 项）

**[MF1] 标题/framing 与核心发现的叙事断裂** [R1: AGREE, R2: raised]
- 标题 "Decomposing Contamination from Calibration" 暗示有效分解框架，但核心结论是 aggregate level 无需分解（~0.6-0.7pp）。论文以 methods paper 包装了 negative result。"Diagnostic value" pivot 在 §1 ¶4 才出现，与 Contribution 1 "Empirical decomposition" 措辞矛盾。
- **建议**: 重新定位为实证调查（"Does contamination need calibration?"），而非方法论文（"Here is ContamCal"）。Introduction 从第一段即铺设 null 预期。

**[MF2] SFT injection 的 ecological validity 不足以支撑无条件 claim** [R1: raised, R2: AGREE]
- "Raw accuracy is already well-calibrated"（Abstract, §6）未加任何限定条件，但仅基于 LoRA SFT injection at ≤3B。Pretraining contamination 通过 trillion-token web crawl 分布式暴露，效应机制根本不同。Limitations §7 承认 "qualitatively different signatures"，但 claim 不受限。近期 pretraining-level dose-response 研究（arXiv 2601.04301）表明 pretraining contamination 效应显著更大。
- **建议**: (1) Abstract/Introduction/Conclusion 所有 claim 限定为 "under SFT injection at ≤3B scale"；(2) 引用 pretraining contamination 文献作为对比锚点。

**[MF3] Additive linear γ 假设未验证，oracle ablation 解释存在根本歧义** [R1: raised, R2: AGREE]
- Oracle ablation（AUC=1.0 perfect labels, γ = -0.012, CI [-0.145, 0.119], PPP=0.41）有两种同等合理的解释：(a) 真的没效应（item-level heterogeneity 抵消）；(b) 有效应但 additive linear γ 捕捉不到（model misspecification）。论文只采信 (a)，但 Limitations ¶9 自己承认 threshold 行为可能导致 γ 被稀释为零。如果解释 (b) 成立，整个 2PL+γ 框架的诊断价值受质疑。
- **建议**: 测试 item-level γ_i 或 γ×a_i 交互模型排除 misspecification；不可行则在所有 claim 中明确 "under the linear additive specification"。

**[MF4] 域级 γ 显著性（Social Sciences 1/8）缺多重比较校正** [R1: raised, R2: AGREE]
- 8 个 domain 独立检验，仅 Social Sciences 在 α=0.05 达到显著（γ = -0.57, CI [-1.05, -0.10]）。Bonferroni 校正后 α = 0.00625，CI 上界 -0.10 极可能越过零。BH 校正下 1/8 pattern 也大概率不通过。这是 "diagnostic value" 叙事的主要实证支撑——校正后消失则 Contribution 5 失去支持。
- **建议**: 报告 Bonferroni/BH 校正后结果；校正后不显著则重新表述为 "suggestive pattern requiring higher-powered replication"。

**[MF5] ARC PPP < 0.05 但 IRT 结果仍出现在主表** [R1: raised, R2: AGREE with nuance]
- ARC 在所有 J 配置（8, 13, 16）下 PPP < 0.05（§5.4），2PL+γ 模型拟合不合格。但 Table 3 报告 ARC IRT 结果无 PPP 注脚。ARC 的 ~0.7pp raw data observation 有效，但 IRT-derived 数值不可靠。
- **建议**: Table 3 ARC 列加 PPP 注脚；区分 raw observation vs IRT estimate 的可信度。

**[MF6] RRF multi-signal fusion 被自身实验否定** [R2: raised, R1: AGREE with nuance]
- S2 (Min-K%++) 在 0.5B 方向反转，S4 (Self-Critique) 在 <1.5B 近乎随机，§5.2 承认 "RRF fusion degrades to S1-only"。Contribution 2 声称 RRF-guided filtering 价值，但无 RRF vs S1-only 在 1.5B/3B 的直接消融。R1 补充：S2 在 3B 有 d≈+0.7，RRF 可能有 value，但必须提供实证。
- **建议**: 提供 RRF vs S1-only 在 1.5B/3B 的对比（τ, MAE, γ）；如 RRF ≤ S1-only，降格 Contribution 2。

---

### Should-Fix（影响评分，11 项）

**[SF1]** J 值跨分析不一致（13/16/24/18-28），全部远低于论文自证的 J≥50 threshold。所有 γ-based 结论本质上 underpowered。[R1, R2 AGREE]

**[SF2]** RRF-filtered 300 items vs random 2000 items 的 τ 对比（0.73 vs 0.46）可能存在 item discrimination confound。RRF 可能系统性选出高 a_i items，与 contamination signal 无关。需报告 RRF vs random subset 的平均 a_i。[R1 raised, R2 AGREE]

**[SF3]** CI coverage（MMLU 83%/89%/100%, ARC 45%/65%/90%）仅在 Limitations 报告。ARC under-coverage 与 PPP<0.05 互相印证 model misfit，应在主文讨论。[R1, R2 AGREE]

**[SF4]** Cross-family validation J=3-4（Llama 单 seed），且 §4.2 引用的 "Appendix E power analysis" 实际内容为 baseline tables（sec:full_baselines），power analysis 内容缺失。[R1, R2 AGREE; R2 确认为 content error]

**[SF5]** γ~N(0,1) 先验 sensitivity analysis 缺失。覆盖 ±2 logit units，若 effect 很小则 prior 选择对 posterior 影响实质性。需测试 N(0,0.5)/N(0,2) 并报告 e_ij 分布。[R1, R2 AGREE]

**[SF6]** Min-K%++ reversal 因果解释（"token-level surprisal disruption"）仅为 post-hoc 假设，无直接验证。替代解释（position bias confound、near-full-rank LoRA）未排除。[R1 raised, R2: AGREE but considers minor]

**[SF7]** Oracle ablation（§5.1）仅采信 "effect heterogeneity" 解释，未平衡讨论 "model misspecification" 可能性。[与 MF3 关联]

**[SF8]** 五个 Contributions 覆盖 null finding / item filtering / signal failure / identifiability / domain diagnosis，方向过于分散。建议合并为 2-3 个核心贡献。[R2 raised, R1: AGREE with reservation]

**[SF9]** 重要相关工作遗漏：Han et al. (EACL Findings 2026) "Quantifying Data Contamination in Psychometric Evaluations of LLMs" 是最直接的 concurrent work；arXiv 2601.04301 pretraining dose-response；Chen et al. (EMNLP 2025) contamination survey。此外缺 Bayesian workflow/model comparison 参考（WAIC/LOO-CV）。[R2 raised, R1: AGREE in principle]

**[SF10]** Table 2 (domain γ) PPP 列全为 "---"——per-domain model fit 不可验证，特别是 Social Sciences 作为唯一 significant domain。[R1, R2 AGREE]

**[SF11]** Abstract ~258 words（超 ACL 推荐 150-250），包含 ~10 个具体数字，信息过密。[R2 raised, R1 AGREE]

---

### Minor Issues（6 项）

1. B2 (Single2PL+γ) 在 §4.4 定义但 Table 3 中缺失
2. "-ing phrases" 在 Related Work 中偏多（"confirming that...", "enabling both..."）
3. §3.2 "Adaptation 1/2/3" 命名风格偏 didactic
4. `habba_2025_growing_pains` bib key 写 2025 但实际 year=2026
5. Eq. 2 additive interpretation ("difficulty shift by γ_k·e_ij/a_i") 仅在 linearization 下成立，非精确
6. 无法编译确认正文是否 ≤ 8 页

---

## Reviewer Consensus

所有关键问题达成共识。交叉回应中：
- R1 对 R2 的 9 个问题：7 × [AGREE]，2 × [AGREE with nuance]（R2-N3 RRF 和 R2-W2 贡献数量）
- R2 对 R1 的 10 个问题：9 × [AGREE]，1 × [AGREE with nuance]（R1-N4 ARC ~0.7pp 来源区分）
- 无任何 [REBUT]

核心共识：
1. **Null finding 的外部效度**是首要问题——SFT at ≤3B 不能泛化为 contamination 的一般性质
2. **Linear additive γ 的模型充分性**存在根本歧义——oracle ablation 无法区分 null effect vs misspecification
3. **Domain-level γ significance** 在多重比较校正后可能消失，削弱 diagnostic narrative
4. **RRF** 在当前实验条件下缺乏超越 S1-only 的实证支持

---

## Reviewer Divergence

无实质性分歧。仅有微小差异：
- R1 对 RRF 贡献被否定的程度略保守（S2 在 3B 有 d≈+0.7），R2 更绝对
- R2 认为 ARC ~0.7pp 在 Abstract 中可保留（来自 raw data 非 IRT），R1 倾向移除

---

## Questions（需作者澄清）

1. Table 2 各 MMLU domain 的 PPP 值是多少？如果 Social Sciences PPP < 0.05，其 γ significance 是否可信？
2. §4.2 声称 "post-hoc power calculations in Appendix E"——Appendix E (sec:full_baselines) 实际为 baseline tables。Power analysis 是否存在？
3. 在 1.5B/3B 上，RRF (S1+S2+S4) vs S1-only 的 τ/MAE/γ significance 对比结果如何？
4. 如果将 γ 替换为 item-level γ_i 或 γ×a_i 交互项，oracle ablation 中是否能检测到 item-level contamination effects？
5. RRF-selected 300 items 的平均 discrimination (a_i) 与 random 2000 items 相比如何？

---

## Missing References

| 论文 | 严重程度 | 理由 |
|------|----------|------|
| Han et al. (EACL Findings 2026) "Quantifying Data Contamination in Psychometric Evaluations of LLMs" | **高** | 直接将 psychometric/IRT + contamination 结合，最接近的 concurrent work |
| arXiv 2601.04301 (2026) "Quantifying the Effect of Test Set Contamination on Generative Evaluations" | **高** | Pretraining-level dose-response，与 null finding 形成关键对比 |
| Chen et al. (EMNLP 2025) contamination survey | **中** | 领域最全面综述 |
| arXiv 2411.03923 "Evaluation data contamination in LLMs: how do we measure it and (when) does it matter?" | **中** | Contamination measurement meta-analysis |
| Gelman et al. (2020) "Bayesian Workflow" / Gabry et al. (2019) Bayesian visualization | **低** | 先验选择和 PPP 的标准方法论参考 |

---

## Overall Assessment

**Overall Score: 3.0 (Findings)**
**Confidence: 4/5**

**评分依据 (EMNLP 2026 ARR scale)**:
- 3.0 = Findings（可被 Findings 接收）

**理由**:
论文提出了一个有价值的研究问题（IRT 能否分离 contamination 和 ability），实验设计严谨（受控 SFT injection, within-family design），且诚实报告 null result。Identifiability 分析和 Min-K%++ reversal 发现有独立价值。

但核心问题阻碍了 Main Conference 接收：
1. **方法不 work**: ContamCal 在其自身实验中不优于 trivial baseline (raw accuracy)
2. **Null finding 范围受限**: 仅 SFT at ≤3B，不能推广到 pretraining contamination（最实际的场景）
3. **Model specification 歧义**: Linear γ 的 null result 可能是 misspecification artifact
4. **统计推断问题**: 域级显著性缺多重校正，ARC model fit 不合格，Appendix E power analysis 缺失

要达到 Main Conference (≥4.0)，需要：
(a) 至少一个 pretraining contamination 或 7B+ 模型的验证案例
(b) 替代 γ 规范（item-level 或 interaction）的消融实验
(c) 多重比较校正后仍成立的 domain-level evidence
(d) RRF vs S1-only 的直接实证对比

当前版本修复 claim scoping（MF1-MF2）、补充 PPP/校正（MF4-MF5）、提供 RRF ablation（MF6）后可作为有价值的 Findings paper。

---

## Detailed Comments（逐节）

### Abstract
- ~258 words，超 ACL 推荐上限；数字过密（~10 个）
- "Raw accuracy is already well-calibrated" 缺限定条件
- 建议精简至 ~200 words，保留 2-3 关键数字

### Introduction (§1)
- 五段结构基本完整，但 "surprising null result" reveal 在 ¶4 才出现，更像实验报告而非故事驱动
- 五个 Contributions 方向分散，建议合并为 2-3 个
- Contribution 5 "without multiple comparison correction" 的脚注式说明不够——这直接影响结论成立性

### Related Work (§2)
- 四段结构清晰（detection, IRT, DIF, calibration disambiguation）
- PSN-IRT 已引用且有 differentiation
- 缺 Han et al. EACL 2026（最直接 concurrent work）
- 缺 pretraining dose-response 文献
- DIF 段落质量好，psychometric 连接准确

### Method (§3)
- 2PL+γ 模型公式规范，additive structure 解释清晰
- RRF 的 meta-circularity 避免论证合理
- 三个 Adaptations 在方法论上合理但呈现方式偏 didactic
- 缺 e_ij 的经验分布报告
- Identifiability 分析（Fisher information）论证充分

### Experimental Setup (§4)
- 受控实验设计是论文最强部分
- 0.5B 排除有充分理由（position bias）
- J=16 vs J=13 的差异来源（实验进度）应更 prominently 说明
- §4.2 cross-family 引用了不存在的 Appendix E power analysis

### Results (§5)
- §5.1 calibration results 清晰呈现 null finding
- Oracle ablation 是关键消融但解释一边倒
- §5.2 signal failure modes 是有价值的 empirical finding
- §5.3 identifiability boundaries 是重要理论贡献
- §5.4 domain analysis: Table 2 缺 PPP，Social Sciences significance 缺多重校正
- §5.5 cross-family: Table 4 呈现清晰，但 J=3-4 功效太低

### Discussion & Conclusion (§6)
- "Why not just use raw accuracy" 段落直接回应关键质疑，是好的写法
- 但 Conclusion 仍以无条件语气声称 null finding
- Future work 段过短，未讨论 pretraining contamination 的路径

### Limitations
- 九项 limitations 全面具体
- CI coverage 和 additive γ linearity 的讨论应移入主文
- SFT ecological validity 讨论有实质内容

### Ethics Statement
- 简洁合规

### Appendix
- Appendix A-D 内容合理
- Appendix E 内容错误（标称 power analysis 实为 baseline tables）
- Table 2 (domain γ) 和 Tables 5-6 补充了主文

### 格式合规
- ACL template + [review] option ✓
- Double-blind ✓
- Limitations/Ethics 位置正确 ✓
- Em-dash/en-dash 检查通过 ✓
- 引用格式 (natbib) 正确 ✓
- 页数无法编译确认 ⚠️