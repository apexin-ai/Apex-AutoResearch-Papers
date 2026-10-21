---
round: 44
review_mode: fresh
overall_score: 3.0 - Findings
timestamp: 2026-05-22T07:42:49.363178+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 44 审稿报告（EMNLP 2026 / ARR May 2026）

**论文**: Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text
**Venue**: EMNLP 2026 via ARR May 2026 cycle | Long paper | Double-blind
**审稿轮次**: Round 44 (fresh review, 2 Reviewers, 1 轮 + 交叉分享)

---

## Summary

本文提出 DDR（differential depth response）分解框架，将递归 LLM 生成中的分布漂移分解为 location（单调漂移）和 shape（近似不变）两个成分。基于 8 个 base-model generators（5 个 family），作者构建了 7-feature depth classifier，在 leave-one-generator-out 下实现 binary F1=0.694，端到端 QLoRA 达到 3-class F1=0.905。DDR 分析视角新颖，验证极其全面（25+ 附录实验），但理论动机薄弱、framing 雄心超出实际能力（3-class, base-model only）、分类性能与已有方法持平。

---

## Strengths

**S1.** DDR location/shape 分解是 AI text detection 文献中未见的结构化分析视角，将递归生成的分布变化从 undifferentiated drift 提升为可解释的两成分模型。与 model collapse 文献（weight-update tail erosion）形成清晰互补（§5）。

**S2.** 验证体系在 empirical study 中属顶级水平：k-means clustering（silhouette=0.660）、per-generator replication（8/8 一致）、exhaustive 35-split enumeration（排名第 1）、TOST + bootstrap、Granger causality、跨温度/跨域/跨解码策略鲁棒性检验。

**S3.** 对 gen-0 seed sharing 的透明处理体现强方法论意识：主动识别 3-class F1 高估问题，采用 leak-free binary F1 作为主指标，提供 independent-seed（F1=0.680）和 seed-level demeaning（F1=0.701）两个控制实验。

**S4.** LOGO 和 LOFO 协议设计严格——LOGO 测未见 generator 泛化（binary F1=0.694），LOFO 测未见 family 泛化（F1=0.686），两者差距仅 0.8pp，说明 family-level 泛化良好。

**S5.** 附录 25+ 个分析几乎覆盖所有可预见的 reviewer 问题（DDR partition validation、TOST、cross-generator transfer matrix、decoding strategy robustness、feature distribution analysis 等），信息密度高且组织有序。

---

## Weaknesses

### Must-Fix（影响接收决定）

**[MF-1] DDR 理论动机薄弱，核心机制停留在假设层面** [共识: R1-N1 raised, R2 agree]
- §4.2 对 location drift / shape stationarity 的解释仅为 "we hypothesize this reflects the mixing property of finite-vocabulary autoregressive processes"，引用 Markovian chains 文章但无形式化推导。§5 明确承认 "a formal derivation remains future work"。
- DDR 框架的价值取决于其是 principled decomposition 还是 post-hoc observation。缺乏理论支撑，读者无法判断该 partition 在新条件（新架构、新语言）下是否成立。Gemma-2-2B 的完全失败（3-class F1=0.028, Appendix z.5）恰好印证了这一担忧。
- R2 补充：作为 empirical study 不必然需要完整推导（Shumailov et al. 2024 model collapse 论文同样缺形式化证明），但需至少提供 simplified model 下的 sketch proof。
- **建议**：提供 simplified Markov chain / softmax-temperature model 下的 sketch proof，说明为什么 entropy max/min 在 autoregressive sampling 下保持 invariant；或至少将 partition 明确定位为 descriptive empirical finding 而非 principled decomposition。

**[MF-2] Cross-model chain F1=0.830 提升未排除 generator diversity accumulation confound** [共识: R1-N2 raised, R2 agree]
- Cross-model chains 的 binary F1=0.830 显著高于 single-generator LOGO (0.694)，+13.6pp。替代假设：cross-model chain 中每步引入不同 generator 的 stylistic fingerprint，分类器可能检测 *generator diversity 的累积效应* 而非 *depth per se*。
- Appendix y Table 39 是 single-generator transfer matrix，并非 R1 要求的 diversity-controlled chain 对比。
- **建议**：(a) 控制实验——same-family cross-size chains vs cross-family chains；(b) 分析 cross-model chain 中 stationary vs drifting features 的贡献比例变化；(c) 至少在 Discussion 中讨论此替代假设。

**[MF-3] Abstract "shape features d ≤ 0.10" overclaim — 掩盖三分 partition 结构** [共识: R2-N1 raised, R1 agree]
- Abstract 声称 shape features "remain near-stationary (d ≤ 0.10)"，但 §4.2 将 entropy_std 归类为 intermediate（d=0.55），k-means 也将其独立分 cluster。此外 tail_decay 仅 4/8 generators 通过 TOST，entropy_min 在 gen-0/gen-1 边界 |ρ|=0.40。实际 partition 为 3-drifting / 1-intermediate / 1-boundary / 2-truly-stationary，远非 clean binary。
- Abstract 的二分法（location drift vs shape stationary）掩盖了论文自身承认的复杂结构，对核心理论贡献（DDR clean asymmetry）的精确性构成损害。
- **建议**：Abstract 修正为 "three near-stationary features (d < 0.10) and one intermediate"；主文 §4.2 更诚实地呈现 boundary features，不将其降格为括号补充。

**[MF-4] DDR 7-feature ensemble 与 detection baseline ensemble 性能持平** [R2-N3 raised, R1 agree with nuance]
- Table 3 显示 7-feature DDR binary F1=0.705 vs 4-det+surface F1=0.708，差异仅 0.3pp。DDR 特征组的分类价值未超越已有检测方法的简单组合。
- R1 部分 rebut：论文 §4.3 已将 DDR 定位为分析框架而非性能工具，2.4× lower cost 是附加优势。但 Contributions 和 Abstract 的 framing 仍暗示性能优势。
- **共识建议**：§1 Contributions 明确区分 "分析贡献（DDR 分解洞察）" 和 "工程贡献（分类器）"，承认后者 "comparable to baseline ensembles at lower cost" 而非核心 claim。

### Should-Fix（影响评分但不一票否决）

**[SF-1] Base-model-only scope 与 real-world motivation 错位** [共识: R2-W2 raised, R1 agree; 跨轮次 persistent issue since R34]
- §1 用 scientific publications 和 data provenance 作 motivation，但这些场景通常涉及 instruction-tuned models。Appendix k 显示 instruction tuning 使 DDR "压缩"，3-class F1 降低 3.7-19.9pp。Abstract 最后一句 scope 限定位置太靠后。
- **建议**：将 scope 限定前移至 Abstract 第 1-2 句或 §1 第 1 段；将 motivation 从 real-world detection 调整为 base-model generation dynamics 的科学分析。

**[SF-2] 与 model collapse 文献的 novelty 区分不够清晰** [共识: R2-W1 raised, R1 agree; persistent since R39]
- 递归生成导致分布压缩是 model collapse 文献已知结论。DDR 的增量贡献（location/shape 分解 + ordinal classifier）在 §2.2 中定位不够清晰。Appendix z.6 Table 46 的三方对比表质量好但放在附录太深。
- **建议**：将 Table 46 核心区分点上提到 §2.2 正文，用 1-2 句话明确 DDR 与 model collapse（weight-update tail erosion）和 concurrent inference-chain work 的 delta。

**[SF-3] XGBoost vs QLoRA 11.6pp gap 解释缺乏实证** [共识: R1-W3 raised, R2 agree; persistent since R42]
- §4.1 "token embeddings capture sequential patterns beyond the seven summary statistics" 是 unsubstantiated claim，未区分 input representation、joint optimization、model capacity 三个可能因素。
- **建议**：移除或软化该 claim；承认 gap 来源未消融；或做简单 ablation（如 QLoRA on 7-feature input vs raw tokens）。

**[SF-4] 6-gen vs 8-gen subset 不一致** [共识: R1-W4 raised, R2 agree; persistent since R43]
- QLoRA 3-class F1=0.905（6-gen）vs Table 2 3-class F1=0.762（8-gen），不同 subset 使 Abstract 中两个 F1 不可直接比较，认知负担高。
- **建议**：QLoRA Table 7 增加 8-gen 结果，或报告 6-gen XGBoost 对应数字，实现 apple-to-apple 比较。

**[SF-5] Downstream utility 实验反向削弱 motivation** [R2-W3 raised, R1 agree with nuance; persistent since R42]
- Appendix m TOST 显示 depth-aware curation ≈ random subsampling，否定了 depth profiling 在数据策划场景中的效用，与 Introduction "corpus curation" 动机矛盾。n=3 seeds 统计功效极低。
- R1 补充：仅测单一下游场景，不排除其他任务效用；batch contamination estimation（±3-4%）已展示一个实际用途。
- **建议**：将 motivation 从 "curation improves quality" 调整为 "provenance auditing and contamination monitoring"。

**[SF-6] 术语不一致：entropy vs NLL** [共识: R2-W4 raised, R1 agree; persistent since R32]
- 5/7 features 以 "entropy_" 命名但实际计算 reference-model NLL。§3.3 disclaimer 不足以覆盖全文。
- **建议**：Table 1 标注 "NLL-based"，或统一改名为 nll_mean/nll_std 等。

**[SF-7] Abstract QLoRA F1=0.905 缺 seed sharing caveat 和评估协议区分** [共识: R1-W2 + R2-N2 交叉]
- Abstract 并列 binary F1=0.694（LOGO, leak-free）和 3-class F1=0.905（QLoRA, 6-gen, within-model 5-fold CV），未标注评估协议差异，读者易高估实际性能。
- **建议**：Abstract 中 QLoRA F1 附带 caveat，或改为 binary F1；所有 3-class F1 表格统一标注 seed sharing caveat。

### Minor（不影响接收）

1. Table 3 caption 过长，建议 profiling 说明移至 footnote [R1]
2. Figure 3 y轴从约 0.4 起始放大了方法间差异视觉效果 [R1]
3. Appendix 编号系统庞大（a 到 z.7, 26+ sections），导航困难 [R1+R2]
4. Downstream utility n=3 seeds 统计功效不足 [R1+R2]
5. Gemma-2-2B 完全失败（3-class F1=0.028）对 "generator-agnostic" 定位构成隐忧，建议 Limitations 讨论 [R1+R2]
6. Figure 1 灰度打印下颜色区分困难，考虑增加 marker 形状 [R2]

---

## Reviewer Consensus [AGREE]

1. **DDR 理论动机薄弱** (MF-1)：两位均同意核心机制缺形式化支撑是主要短板，但 R2 认为 empirical paper 标准下可降级至 strong warning（Shumailov et al. 2024 同样缺完整推导）。共识：至少需 sketch proof。
2. **Cross-model chain confound** (MF-2)：R1 提出，R2 完全同意并补充具体控制实验设计。
3. **Abstract shape feature overclaim** (MF-3)：R2 提出，R1 同意并补充了 tail_decay 和 entropy_min 的 boundary 问题，共同强化了论证。
4. **DDR vs baseline 性能持平** (MF-4)：R2 提出，R1 同意事实但认为论文已部分定位（§4.3 最后一句）。共识：framing 需更诚实。
5. **Base-model scope 错位** (SF-1)：两位完全同意。
6. **术语不一致** (SF-6)：两位完全同意。
7. **Abstract QLoRA F1 误导** (SF-7)：两位完全同意。

## Reviewer Divergence [REBUT]

1. **标题 "Depth Profiling" 是否需要修改**：R2 认为标题暗示精细刻画能力，建议改为 "Classifying Shallow vs. Deep Recursive Generation"。R1 rebut：副标题 "Classifying Recursive Generation Depth" 已足够精确，"profiling" 在统计学中指 characterization 不必然意味连续量化。**Director 判断**：标题本身可接受，但 Abstract 需更清楚地区分评估协议和实际分辨率上限。
2. **Abstract 信息密度**：R2 认为数字过多（8+ 数值），建议精简。R1 rebut：信息密度可接受，真正问题是 qualifier 缺失（d ≤ 0.10 不含 entropy_std、两个 F1 评估条件差异）。**Director 判断**：两者可合并修复——修正 qualifier 的同时适当精简。
3. **Pythia-410M family proximity**：R1 认为 9.1pp per-generator variance 中 family proximity 贡献比例未量化。R2 部分 rebut：Appendix s cross-family reference validation 已部分定量化（spread=0.013）。**Director 判断**：证据充分但主文呈现不足，降级为 minor presentation issue。

---

## Questions for Authors

1. DDR partition 在 instruction-tuned 模型下 "被压缩" 的具体机制是什么？RLHF/SFT 改变了哪个层面的 distributional dynamics？
2. 如果将 7-feature DDR set 与 4-detector scores 合并为 11-feature ensemble，是否能突破当前性能上限？这能帮助区分 DDR 是否提供了与 detection scores 正交的信息。
3. Cross-model chain 中 same-family cross-size chains（如 Pythia-1B → Pythia-2.8B）vs cross-family chains 的 F1 差异有多大？
4. 为什么选择 Pythia-410M 作为唯一 reference model？若 reference model 选择影响 DDR partition 结构本身（而非仅分类性能），这需要更多讨论。

---

## Missing References

R1 建议补充：
1. **Ordinal classification 方法论文献**：论文使用了 CORAL、CORN、Frank-Hall（Appendix h）但 Related Work §2 中未讨论 ordinal regression 的方法论基础。
2. **Watermarking 与 depth 的关系**：Kirchenbauer et al. (2023) 的 watermarking 方法在递归生成场景下的行为。

R2 未发现重大遗漏。引用覆盖面（70+ 篇）充分。

---

## External Review (Stanford Agentic Reviewer)

**状态**：未请求（项目未配置外部审稿）。

---

## Visual Layout Check（非评分项）

**状态**：done（耗时约 3.5 分钟）

**Critical**:
- Page 37（最后一页）：Figure 15 仅占下方约 30%，上方 65-70% 纯空白。审稿人翻到最后一页看到大面积空白会留下论文草率印象。建议上移或与前页合并。

**Warning**:
- Page 1-2：连续两页纯文本（Abstract + Introduction + Related Work 开头），核心视觉结果 Figure 1 到 page 6 才出现。建议提前一个结果预览。
- Page 4：纯文本页（Method §3.2-3.3），与 Table 1 后形成长文字段落。
- Page 24：底部约 55-60% 空白。
- Page 36：Table 46 文字非常小且密集，可读性受限。

**Info** (16 items)：Figure 1-3 质量良好，颜色编码语义清晰，Limitations/Ethics/References 格式合规。

---

## Overall Assessment

**Overall Score: 3.0 — Findings**
**置信度: 4/5**

**评分理由**：

两位 Reviewer 独立给出 3.5（Borderline Conference），交叉分享后高度收敛。综合评判将分数调整至 3.0（Findings），理由如下：

1. **4 个 Must-Fix 形成 coherent 的 concerns 链条**：DDR 理论动机薄弱（MF-1）→ partition 实际比声称的更 messy（MF-3）→ 分类性能与现有方法持平（MF-4）→ cross-model 泛化证据存疑（MF-2）。这些不是孤立问题，而是共同指向 DDR 框架尚未成熟到 Conference 级别。

2. **Scope-motivation mismatch 是跨轮次 persistent issue**（自 Round 34 起）：base-model-only 限制 + instruction-tuned 退化 + downstream null result 共同制约了实际影响力。论文的 real-world motivation 叙事与实验覆盖范围之间的 gap 在多轮审稿后仍未充分弥合。

3. **但论文有 genuine merit**：DDR location/shape 分解是有意义的分析贡献，25+ 附录实验展示了少见的方法论严谨度，对 gen-0 seed sharing 的透明处理、LOGO/LOFO 设计、多维度鲁棒性检验均值得肯定。这些优点使其符合 Findings 接收标准。

**对 Conference 的距离**：需要 (a) 至少一个 sketch proof 支撑 DDR 的理论地位，(b) 排除 cross-model chain 的 diversity confound，(c) 修正 Abstract/framing 的 overclaiming，(d) 更诚实地定位贡献性质（分析框架 > 分类性能）。

---

## Detailed Comments（逐节）

**Abstract**: 需修正 "d ≤ 0.10" overclaim（排除 entropy_std）；两个 F1 需标注评估协议差异；scope 限定（base-model only）前移；考虑精简数字或增加 qualifier。

**§1 Introduction**: Scope-motivation 调整——缩短 real-world detection hook，增加 base-model generation dynamics 的科学性 motivation；Contributions 明确区分分析贡献 vs 工程贡献。

**§2 Related Work**: 将 Table 46 核心区分点上提到 §2.2 正文；与 model collapse 文献的 novelty delta 需更 sharp。

**§3 Method**: 术语统一（entropy → ref-NLL 或标注 NLL-based）；reference model 选择的讨论可扩展。

**§4.1 Results**: Cross-model chain 需讨论 diversity accumulation confound；XGBoost vs QLoRA gap 的 claim 需弱化或增加实证。

**§4.2 DDR Analysis**: 主文需更诚实地呈现 boundary features 和 partition 的模糊边界；理论动机需加强（sketch proof or explicit descriptive positioning）。

**§4.3 Baselines**: 叙事重心向 multi-feature ensemble comparison 倾斜；承认分类性能 "comparable at lower cost"。

**§5 Discussion**: Downstream 引用降调；descriptive vs mechanistic 区分需明确。

**§7 Limitations**: 增加 architecture sensitivity 讨论（Gemma-2-2B evidence）。

**Appendix**: 6-gen vs 8-gen 不一致需 apple-to-apple 桥接；QLoRA 补充 8-gen 结果。

**格式合规**: 页数（≤8 正文）✓ | 匿名化 ✓ | ACL 模板 ✓