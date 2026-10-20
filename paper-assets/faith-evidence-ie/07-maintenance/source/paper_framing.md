# Paper Framing — FREIGE

> **状态**: Round 2 审稿修复中（D155 Action Matrix）— Round 2 得分 3.0 (Findings)，升级路径明确 (3.0→3.5→4.0)
> **最后更新**: 2026-05-23 (D155: Round 2 Action Matrix 执行中; W1 variance 降级 + W2 EDCR partial correlation + 9 writing patches 派发)
> **审稿 Round 1**: 3.0 → Round 1 修复后提交 Round 2
> **审稿 Round 2**: 3.0 (Findings)。3 个系统性问题：统计方法论(W1/W2)、方法原创性(W3)、decoupling spectrum 深度(W4/W5)
> **W1 降级决策**: Abstract/Contributions 用 "consistently reduces training seed variance" (Reviewer 建议 "consistently" 优于 "substantially"——描述 4/4 方向一致性，不暗示 p<0.05)。正文三层证据：sign test p=0.0625 (n=4 结构性上限) + 1.7B χ² CI 不重叠 + Cohen's d 3/4 large。分析正文保留具体数字+统计 caveat
> **贡献重构**: 4 贡献 → 3 贡献（CED 合并入 RSFT，EDCR 降级为分析工具）
> **Dream v1**: best=2.5, median=3.0, worst=2.5 → reframe 完成
> **Dream v2**: best=3.0, median=2.5, worst=2.5

## ⚠️ Post-Review Contribution Restructuring (D103)

审稿后从 4 贡献重构为 3 贡献：

### 原 4 贡献
1. Task formalization (evidence-grounded DocRE)
2. EDCR diagnostic metric
3. Decoupling spectrum
4. CED scoring

### 新 3 贡献
1. **Evidence-grounded DocRE + RSFT with NLI-based scoring** — 合并原 C1+C4。CED 不再作为独立贡献，NLI-based scoring（CED/flat-NLI 等效）是 RSFT 有效的关键组件
2. **Decoupling spectrum（观察性，非因果）** — 原 C3 降级为观察性描述。"co-occurs with" 替代 "acts as amplifier"。EDCR 作为分析工具嵌入此贡献（不独立列出）
3. **Evidence tax landscape + RSFT variance compression** — 原 C5 提升为正式贡献。Within-family threshold（1.7B 获益，4B+ 中性）+ cross-architecture variation（Qwen 8B ≈0 vs LLaMA 8B evidence helpful）+ RSFT 跨 scale 压缩 seed 方差。**Variance compression 是 C3 核心**（最稳固的 sub-finding，不受 M027 修正影响）。⚠️ **D155 W1 降级**: Abstract/Contributions 用 "consistently reduces" 定性表述 + sign test (4/4 scales 同方向, p=0.0625 n=4 结构性上限)，不再给具体倍数。分析正文保留 per-scale 数字 (1.7B 31×, 4B 7.5×, 8B 6.5×, LLaMA 4.6×) + χ² CI caveat

### 关键 claim 调整
- 所有因果 claim → 观察性描述（GRPO "acts as catastrophic amplifier" → "co-occurs with"）
- EDCR ρ 从 -0.965 (n=15) 改为去重后数值（待 Agent 计算完成）
- "+8pp" → matched@2048 fair subset: 1.7B=-5.63pp, 4B=+0.73pp, 8B=+0.04pp（D144 corrected）。Abstract 加 "on a controlled evaluation subset"
- "matches 8B SFT" → "approaches 8B SFT"
- CED vs flat-NLI 不再区分，统称 "NLI-based scoring"

## Target Venue

- Primary: **EMNLP 2026 Main** (ARR July cycle, ~July 15-25 → commit EMNLP Aug/Sep)
- Fallback: AAAI 2027 (abstract July 25, paper Aug 1)

## Core Insight

**统一主线 (D131)**: Evidence generation in LLM-based DocRE is not a fixed cost — its role depends on **model capacity** (scale-dependent tax), **training paradigm** (decoupling spectrum), and **data quality** (NLI-based filtering). RSFT navigates this landscape by eliminating the tax while preserving evidence faithfulness.

本文提出 **evidence-grounded DocRE** 作为新任务范式：LLM 同时输出关系三元组和支撑证据句。核心发现是 evidence generation 的效果并非简单的有益/有害二分，而是一个由三个维度决定的 landscape：

1. **Model capacity × evidence tax** (C3): Within-family threshold——1.7B 从 evidence 获益（matched@2048 fair_tax=-5.63pp），4B/8B/14B 趋零（+0.73pp/+0.04pp/+0.03pp）。Cross-architecture variation——LLaMA 8B 与 Qwen 8B pattern 不同（SFT tax 极不稳定，RSFT tax=-2.17pp）。⚠️ D144 修正：4B 从 +7.5pp→+0.73pp，"non-monotonic"/"capacity valley" 叙事已废弃。
2. **Training paradigm × decoupling** (C2): RL 优化压力与 evidence-extraction decoupling severity 正相关（GRPO catastrophic > DPO gradual > RSFT none）。越激进的优化越破坏 RE-evidence 平衡。
3. **Data quality × training reliability** (C1+C3): NLI-based quality filtering (CED/flat-NLI) 不仅提升 mean performance（+3-5pp），更 dramatically 压缩 seed variance（4.6-31×）。1.7B RSFT（std=0.09pp）比 8B SFT（std=3.23pp）更 predictable——小模型通过 quality filtering 获得大模型才有的稳定性。

**RSFT 是唯一同时在三个维度上表现良好的方法**：不引入 decoupling（维度2），压缩 evidence tax 至接近零（维度1），且通过 quality filtering 保证 training reliability（维度3）。

CED (Contrastive Evidence Discrimination) 是一种 NLI-based 候选筛选函数，与 flat-NLI 统计不可区分（D078 p=0.44），但均显著优于 random/no scoring。CED 因可解释性优势作为默认推荐。

## Story Arc (D131: unified narrative)

**One-sentence pitch**: Evidence generation in DocRE is a landscape shaped by capacity, paradigm, and data quality — and RSFT is the only method that navigates all three axes successfully.

1. **Problem**: LLM DocRE 无证据 → 部署障碍
2. **New task**: evidence-grounded DocRE — 同时生成关系和证据
3. **The landscape** (统一主线的三个 facet):
   - **3a. Capacity axis** (C3): evidence tax 存在 within-family threshold——1.7B 获益（-5.63pp matched@2048 fair），4B+ 中性（+0.73pp/+0.04pp/+0.03pp）。推翻"evidence 总有代价"。Cross-architecture: Qwen 8B ≈0 vs LLaMA 8B evidence helpful，说明 tax 受架构影响不仅受 scale
   - **3b. Paradigm axis** (C2): RL optimization pressure 与 decoupling severity 正相关（GRPO catastrophic > DPO gradual > RSFT none）。QLoRA 放大 mild→catastrophic（intra-task trade-off，非 inter-task forgetting）
   - **3c. Quality axis** (C1): NLI-based scoring 不仅提升 mean（+3-5pp），更压缩 variance 4.6-31×（within-scale: 1.7B 31×, 4B 7.5×, 8B 6.5×, LLaMA-8B 4.6×）。Training reliability 是 quality filtering 的本质效应
4. **RSFT navigates the landscape**: 唯一同时在三个轴上表现良好的方法——无 decoupling + 压缩 tax + 保证 reliability
5. **Practical toolkit**: CED reranker（response-level，恢复 97% evidence 代价），joint generation > post-hoc retrieval（EDCR 低 11pp）
6. **Diagnostic**: EDCR 双层诊断——方法级量化 decoupling，per-relation 级定位薄弱关系类型
7. **Scaling evidence**: 4 Qwen scales (1.7B/4B/8B/14B) + LLaMA-8B 跨家族 + Re-DocRED 跨数据集
8. **Mechanistic decomposition**: duplication regularization (主因, 1.7B 最强) + truncation asymmetry + fair comparison residual — 解释 WHY 而非只报 WHAT。⚠️ 4B 特有分析需 @2048 matched 数据重做（D144 invalidated "capacity valley"）

## Core Claims (reframed after Dream v1, updated D068-D083)

### Claim 1 (Main): Evidence-grounded DocRE 是可行的新能力
- FREIGE 是首个**基于生成式 LLM** 的 evidence-grounded DocRE 方法（⚠️ 必须始终保持 "generative LLM" 限定词——SAIS 已做 encoder-based evidence retrieval + DocRE）
- **关键区分 (Reviewer warning)**：encoder-based evidence *retrieval*（SAIS, DREEAM — 分类哪些句子是证据，evidence supervision 提升 RE）vs generative evidence *production*（FREIGE — LLM 生成证据文本，额外生成负担导致 scale-dependent 代价）。论文 Related Work 必须精准讨论此对比，否则审稿人会问 "为什么 SAIS 说 evidence 有用，你说 evidence 有害"
- **Evidence generation tax**: scale-dependent，详见 Claim 5（D079/D082/D083）
- RSFT 在 4/4 Qwen 配置 + LLaMA 下均超过 SFT baseline（Ign-F1 +1.24~6.55pp）
- **CED reranker 是最优实用方案**: rel_f1=0.4864（仅低于 no-evidence 0.29pp），evi_f1=0.8188（plan_005 ✅）
- **D076 统一协议最终数字（ign_f1，可写入论文）**:
  - SFT baseline: ign_f1=0.3974
  - CED RSFT mean: ign_f1=0.4467 (s42=0.4423, s44=0.4511)
  - flat-NLI RSFT mean: ign_f1=0.4475 (s42=0.4448, s43_r2=0.4503)
  - CED vs flat-NLI Δ=0.0008，统计不可区分（D078 p=0.44）
- **Cross-family validation (D082/D130)**: LLaMA-3.1-8B SFT ign_f1=0.5384 (rel_f1=0.5514), evi_f1=0.8151; no-evidence ign_f1=0.5452 (rel_f1=0.5624). SFT evidence tax=+0.68pp（微弱代价）
- **Cross-dataset validation (D080)**: Re-DocRED Ign-F1 下降 3.15pp 但 Evi-F1 保持 0.817——evidence extraction 能力跨数据集泛化
- 需要 DREEAM-protocol 对齐的 Evi-F1 对比（D041 在处理中）
- **RSFT 方法论定位**：诚实承认 RSFT 是 STaR (NeurIPS 2022) 的单轮变体 + evidence quality scoring。创新点在于将 STaR-like self-improvement 应用于 evidence-grounded DocRE + CED/NLI 作为 domain-specific quality filter，而非框架本身
- **Evaluation caveat** (Limitations): GenRES 指出 exact match F1 低估 generative RE，FREIGE 所有 eval 用 exact match，应承认此局限（对所有方法同等适用，相对比较有效）

### Claim 2 (Core finding): RL optimization pressure 与 evidence-extraction decoupling severity 正相关（D068/D069 修正）
- **Decoupling spectrum**: 优化强度越大，decoupling 越严重
  - GRPO QLoRA: catastrophic（rel_f1=0.0138, evi_f1=0.850, EDCR=0.99）— QLoRA 放大 decoupling
  - GRPO bf16: mild（rel_f1 从 0.4549→~0.434, -2pp; step_30=0.434, step_50=0.4276, step_70=0.4341）— 退化可控但持续（D065/D066）
  - DPO bf16 1ep→3ep: gradual（Ign-F1 38.88→TBD, rel_f1 0.4034→0.3429）— 随训练渐进退化（D067/D068）
  - RSFT: none — 无 decoupling，唯一有效路线
- **QLoRA 是 catastrophic amplifier，不是 root cause**: bf16 GRPO 仅 mild decoupling（-2pp），QLoRA 放大至 catastrophic（-39pp）（D054/D065/D066）
- **Decoupling 是 RL-for-IE 的通用梯度**: 跨方法（GRPO/DPO）、跨量化策略（QLoRA/bf16）一致出现，严重程度与优化压力正相关
- 三档 Dream 审稿均认为此发现\"genuinely novel and striking\"
- **已完成**: GRPO G=8 bf16 确认 mild decoupling（plan_011 ✅）; DPO 1ep/3ep 确认 gradual decoupling（plan_012 ✅）

### Claim 3 (Ablation): NLI-based scoring 提升 RSFT 质量——CED 与 flat-NLI 统计不可区分（D078）
- CED 和 flat-NLI 都显著优于 random/no scoring
- **D078 paired t-test 最终结论**: CED vs flat-NLI p=0.44，统计不可区分
  - CED RSFT mean rel_f1=0.4569 vs flat-NLI mean rel_f1=0.4561（Δ=0.0008）
  - 两种 scoring function 等效，CED 因可解释性（contrastive evidence discrimination）作为默认推荐
- ~~**Critical**: 如果 CED 不显著优于 flat-NLI → CED 降级为"one possible scoring function"~~ → **已确认降级（D078）**
- **论文叙事**: "NLI-based scoring（无论 CED 或 flat-NLI）是 RSFT 有效的关键——两种变体均等效提升质量，CED 额外提供可解释的 evidence discrimination"
- **top_k selection ablation (k=1 vs k=3)**:
  - k=1 (best-of-8) 优于 k=3 (top3-of-8)，CED scoring precision 随 k 增大下降
  - k=1 均值 (3 seeds s42/s43/s44): Ign-F1=45.00, rel_f1=0.4596, evi_f1=81.43, EDCR=0.6434
  - k=3 (1 seed, reeval_rsft_topk3): Ign-F1=43.64, rel_f1=0.4454, evi_f1=80.88, EDCR=0.6635
  - Δ (k=3 vs k=1 mean): Ign-F1 **-1.36pp**, rel_f1 **-1.42pp**, evi_f1 **-0.55pp**, EDCR +0.02
  - 训练数据质量下降: k=1 mean_f1=0.6157, mean_ced=0.6683 → k=3 mean_f1=0.5761, mean_ced=0.6205（来源: mvp2_rsft_ced_scoring / mvp2_rsft_ced_scoring_topk3_r2）
  - 训练集规模: k=1 选出 2718 样本 (12.4%), k=3 选出 8037 样本 (37%), 数据量 ×2.96 但质量下降抵消数量优势
  - **叙事**: 低排名 response 引入噪声——rank 2-3 样本的 F1 和 CED 分数均显著低于 rank 1，扩大训练集规模无法补偿数据质量的稀释。这表明 RSFT 的关键不在数据量而在 scoring precision
  - **注**: k=3 仅 1 seed，差异方向一致但尚不具备统计显著性；作为 ablation table 中的辅助行呈现，不作为独立 claim
  - **D102 跨 scale k=1 vs k=3 验证结果**:
    - 1.7B: k=1 +0.72pp ✓ | 4B: k=1 +1.02pp ✓ | LLaMA-8B: k=1 +1.51pp ✓ | 8B: k=1 -0.57pp (within seed variance 0.95pp)
    - **不能说 "k=1 consistently outperforms k=3"**（8B 方向相反）
    - **正确 framing**: "Methodological correction to match claimed k=1 protocol yields comparable or improved results across scales"
    - D102 的核心目标是方法学一致性修正，不是证明 k=1 更好

### Claim 4 (Diagnostic): EDCR 双层诊断价值（D070/D072）
- **Layer 1 — 方法级**: EDCR 量化 evidence-extraction decoupling，与 Claim 2 spectrum 呼应
  - 方法级 EDCR 与 rel_f1 Spearman ρ=-0.965（plan_003 ✅）——本质是 decoupling 的度量
  - EDCR 识别病理模型（GRPO QLoRA: EDCR≈1.0）
- **Layer 2 — per-relation-type**: EDCR 提供 evi_f1 不捕捉的 relation-type 诊断信息 ✅
  - per-relation ρ(EDCR, evi_f1) = **-0.064** (p=0.58) → **完全独立于 evi_f1**
  - per-relation ρ(EDCR, rel_f1) = -0.793 (p<0.001) → 与 rel_f1 强相关但非完美
  - per-relation ρ(evi_f1, rel_f1) = -0.013 (p=0.91) → evidence 质量与抽取能力在 relation type 间完全解耦
  - 典型案例：date_of_birth (EDCR=0.118, 高 faithful) vs head_of_government (EDCR=0.956, 高 decoupled)
  - 93 relation types 分析（≥5 样本），76 个有非零数据
- **论文叙事**: EDCR 在方法级是 decoupling 度量工具（横向对比方法），在 relation 级是难度诊断工具（纵向定位薄弱 relation）——两层叙事互补
- **仍需**: 100 例人工标注验证（RC6）

### Claim 5 (Scaling): Within-Family Threshold + Cross-Architecture Variation + Variance Compression（D079/D082/D083/D144/D145）
- **核心发现 (D144/D145, matched@2048 fair_tax)**: evidence generation 的效果存在 capacity threshold + architecture dependence
  - **1.7B (Qwen3-1.7B)**: fair_tax=**-5.63pp** (evidence beneficial, matched@2048 fair subset) — evidence generation 起隐式正则化作用，防止小模型过拟合
  - **4B (Qwen3-4B)**: fair_tax=**≈0** (3-seed: s42=+0.73, s43=-0.20, s44=+0.21; mean=+0.25±0.47pp) — D146 confirmed: 4B 容量足够 absorb evidence 负担。Base ign_f1 跨 seed std=3.6pp 但 tax std=0.47pp——tax 本身也表现出"压缩"特性
  - **8B Qwen (Qwen3-8B)**: fair_tax=**+0.04pp** (neutral, matched@2048 fair subset) — 容量完全 absorb
  - **8B LLaMA (LLaMA-3.1-8B)**: SFT matched@2048 fair_tax 3-seed 全负但高方差（s42=-1.53pp, s43=-11.20pp, s44=-2.83pp; mean=-5.19±5.25pp）。⚠️ 旧 @1024 mismatched 数据(s42=+1.20pp)已废弃——方向翻转是截断伪影。RSFT tax=-2.17pp±0.76pp (3-seed stable)
  - **14B (Qwen3-14B)**: tax=**+0.03pp** (neutral, 截断对称无需 @2048 matched)
- **Within-family threshold (Qwen, D146 confirmed)**: 1.7B 获益（-5.63pp，小模型需要 evidence 作为推理脚手架），4B/8B/14B 中性（4B 3-seed mean=+0.25±0.47pp, 8B +0.04pp, 14B +0.03pp）。Threshold 在 1.7B-4B 之间
- **Cross-architecture variation**: 同为 8B，Qwen tax≈0 vs LLaMA tax 高方差但方向一致（matched@2048: 3-seed 全负，mean=-5.19±5.25pp）。⚠️ 旧叙事"direction unstable"已废弃——@1024 mismatched 导致的 positive tax 是截断伪影。新叙事：LLaMA 8B evidence consistently helps（与 1.7B Qwen 方向一致），但 magnitude 极不稳定（std=5.25pp vs Qwen 4B std=0.47pp），说明 architecture/pretraining 影响 tax magnitude stability 而非 direction
- **⚠️ 已废弃叙事 (D144)**: "non-monotonic scaling"、"capacity valley at 4B"——M027 修正后 4B tax 从 +7.5pp→+0.73pp，低谷不存在
- **Mechanistic analysis (plan_020 完成)**：3 层机制解释 scale-dependent tax：
  - **(1) Duplication regularization（主因）**: monotonic decline — 1.7B 27.5pp gap (60.5%→33.0%), 4B 12.1pp gap (43.2%→31.1%), 8B 3.7pp gap (32.9%→29.2%)。正则化效应随容量增大递减
  - **(2) Truncation asymmetry**: 1.7B Δ=19pp (no-evi worse), 4B Δ=2pp (neutral), 8B Δ=-9pp (evi worse, tokens 消耗输出预算)
  - **(3) Fair comparison residual**: 排除截断后，1.7B evidence 仍提升 5.63pp (matched@2048 fair_tax)，8B Qwen +0.04pp，8B LLaMA seed-dependent — 证明 1.7B 有真实 reasoning scaffold 效应
  - **~~4B "capacity valley"~~ INVALIDATED (D144)**: M027 修正后 4B fair_tax=+0.73pp（非 +7.5pp），4B 不再是 outlier。plan_020 中 4B 特有的 mechanistic decomposition 需要用 matched@2048 数据重新评估
- **论文叙事 (D144 revised)**: "Evidence as implicit regularization for small models" — 推翻 "evidence 总有代价" 的简单叙事。1.7B 的 60.5%→33.0% duplication rate 是最有冲击力的数据点。新 framing: within-family threshold（小模型获益，大模型中性）+ cross-architecture variation + variance compression（核心）。不再是 "non-monotonic curve" 而是 "capacity threshold + architecture dependence"
- **Cross-family robustness (D130→LLaMA 3-seed 完成)**: 
  - LLaMA-8B SFT 3-seed: mean=0.5109 (std=2.92pp, s42=0.5384/s43=0.5142/s44=0.4802)
  - LLaMA-8B RSFT 3-seed: mean=0.5654 (std=0.64pp, s42=0.5714/s43=0.5662/s44=0.5587)
  - RSFT gain = +5.45pp (0.5654 vs 0.5109)
  - **Variance compression = 4.6×** (2.92pp→0.64pp)。LLaMA 4.6× 现纳入统一范围 4.6-31×（Director D152+ 决策）
  - 论文叙事：跨家族 "4.6-31×" 统一 claim（Qwen 6.5-31× + LLaMA 4.6×）。LLaMA 作为 cross-family validation 强化 variance compression 的普遍性
- **Evidence 角色转化 (D130→D135 完成)**: LLaMA SFT inference-time tax = +1.35pp fair (s42, D134)。RSFT inference-time tax = -1.14pp±0.76pp (3-seed)。SFT evidence 有害 → RSFT evidence 有益——CED filtering 将 evidence 从负担转为信号。跨家族方向一致：Qwen-8B RSFT -0.78pp, LLaMA-8B RSFT -1.14pp（都是 evidence helps）
- **LLaMA RSFT no-evi variance compression (D135 新发现)**: RSFT no-evi std=0.13pp vs with-evi std=0.64pp (4.9× narrower)。Evidence generation 本身引入额外方差——no-evidence mode 下 RSFT 的 seed variance 更极端地被压缩。这进一步支撑 C3: variance compression 的核心驱动力是 CED filtering 消除 seed-dependent 训练噪声，evidence 生成只是次要方差源
- **Evidence tax methodology correction (D137: matched@2048 required)**:
  - **Control 结果**: s42 with-evi @2048 ign_f1=0.5649 vs @1024 ign_f1=0.5384, delta=+2.65pp。with-evi 也受 1024 截断影响。**所有 evidence tax 必须用 matched token budget（both@2048）**
  - **D136 "方向不稳定" INVALIDATED**: s42 mismatched tax=+1.20pp（positive，evidence hurts）是截断伪影。Matched@2048 下 s42 tax=-4.39pp（negative，evidence helps）。方向翻转是因为 with-evi@1024 被截断压低了
  - **新叙事方向**: 如果 matched@2048 下所有 seed 都是 negative → SFT evidence tax 方向一致（evidence consistently helps），但**量级不稳定**（magnitude varies across seeds）。RSFT 仍更稳定。具体 claim 待 3-seed matched 数据齐全后定
  - **保守性论证**: mismatched (no-evi@2048 vs with-evi@1024) 报告的 tax 是 conservative estimate——低估了 evidence 的好处。论文可用此作为 robustness argument
  - **RSFT truncation robustness (sub-finding 仍成立)**: RSFT no-evi truncation 18-19% at 1024，性能稳定；SFT no-evi 需要 2048 且仍有 25% 残余截断。RSFT 通过 CED filtering 学习了简洁输出结构
  - **待完成**: 4B s43/s44 @2048 pairs（正在跑），完成后算 3-seed 4B mean±std 确认 threshold 方向。14B RSFT @2048 不需要（截断对称）
  - **✅ Qwen matched@2048 已完成 (D145)**: 1.7B fair_tax=-5.63pp, 4B s42 fair_tax=+0.73pp, 8B fair_tax=+0.04pp。M027 adapter 错误同时修正。4B s43/s44 @2048 运行中
- **RSFT 弥合 scale gap (D094→D102→D118)**: 1.7B RSFT 3-seed mean=**0.5119** (std=0.09pp) vs 8B SFT 3-seed mean=**0.5019** (std=3.23pp)，Δ=+1.0pp, p=0.65 不显著——CED-RSFT 使 1.7B 模型**接近** 4.7× 大的 8B SFT，但差异在统计噪声内。"surpasses" claim 被 D118 否定（8B SFT s43=0.5324 拉高均值），回退为 "approaches"
- **Variance Compression 为核心发现 (D118, W2 修正)**: RSFT 跨 3 个尺度压缩 seed 方差——1.7B **31×** (2.79pp→0.09pp), 4B **7.5×** (3.80pp→0.51pp), 8B **6.5×** (3.23pp→0.50pp)。这不仅是副产品而是 CED filtering 的本质效应：质量过滤消除了 seed-dependent 的训练噪声。注：8B 压缩倍数从 17× 修正为 6.5×（D152: plan_006 ign_f1=0.5433 用旧 RSFT 模型 checkpoint-3393，d102 系列 k1 RSFT 正确 s42=0.5376。修正后 RSFT std=0.50pp，压缩倍数 3.23/0.50=6.5×）
- **14B SFT evidence tax ≈ 0 (D117)**: 14B with-evidence=0.5507, no-evidence=0.5510, tax=+0.03pp——14B 容量完全 absorb evidence 生成负担，延续 8B 的 neutral 趋势
- **14B RSFT 完成 (D138)**: ign_f1=**0.5886** (全项目最高), f1=0.6009, format=100%, evi_f1=0.8392, edcr=0.5396。RSFT gain=+3.79pp (vs 14B SFT 0.5507)。Evidence tax=-4.54pp（evidence 强烈有益）。**截断对称**: no-evi 10.8% vs with-evi 10.7%，@1024 tax 可信，无需 @2048 matched。RSFT 训练使 14B 输出简洁对称——与 SFT no-evi 的冗长退化形成对比
- **RSFT evidence tax (D119/D121)**: RSFT 系统性压缩 evidence 代价——4B RSFT tax=**+0.94pp** (@1024; SFT matched@2048 fair=+0.73pp, 两者均近零), 8B RSFT tax=**-0.78pp** (@1024)。⚠️ RSFT @1024 vs SFT @2048 matched 不直接可比——RSFT tax 也可能需 @2048 重算。但定性结论不变：RSFT 在 ≥4B 尺度 evidence tax 趋零
- **Test set evidence tax spot-check (D147 验证, ✅ 全部完成)**:
  | Scale | Dev fair_tax | Test tax | 一致? |
  |-------|-------------|----------|--------|
  | 1.7B | -5.63pp | -4.86pp | ✅ helps |
  | 4B | +0.25±0.47pp | -0.13pp | ✅ neutral |
  | 8B | +0.04pp | -1.71pp | ⚠️ dev neutral → test mild benefit |
  | 14B | +0.03pp | -0.32pp | ✅ neutral |
  | LLaMA-8B | -5.19pp | -4.94pp | ✅ helps |
  - **结论**: test set 上 evidence 从不 hurt performance。5/5 scales 全部与 dev 方向一致。小模型（1.7B Qwen, LLaMA-8B）获益最大
  - 8B deviation: 幅度小 (-1.71pp)，属 near-neutral 范围。评估协议差异（dev matched@2048 vs test full 500 docs）可能部分解释
  - **措辞 (Reviewer 评估)**: "we observe" 动词保留，可去掉 "(on the development set)" scope 限定改为 "(within the Qwen3 family)"。Mechanism-level hedge（implicit regularization）全部保留
- **RSFT test evidence tax (D153/D154, ✅ 全部完成)**:
  | Scale | RSFT with-evi | RSFT no-evi | RSFT test tax | 解读 |
  |-------|-------------|----------|--------|--------|
  | 1.7B | 29.33 | 23.90 | -5.43pp‡ | evidence strongly helps |
  | 4B | 25.01 | 26.52 | +1.51pp | only Qwen3 scale with positive RSFT tax |
  | 8B | 33.53 | 33.19 | -0.34pp | near-neutral |
  | 14B | 38.49 | 39.26 | +0.77pp† | mild evidence cost |
  | LLaMA-8B | 35.99 | 33.34 | -2.65pp | evidence helps |
  - **D153 Version B confirmed ("heterogeneous, scale-dependent")**: RSFT 对 evidence dependence 的影响高度异质——1.7B/LLaMA 保持 evidence benefit, 8B near-neutral, 4B/14B 轻微 evidence cost。**Version A ("systematically compresses") DEAD**——2/5 scales 实际 amplify 或 flip evidence tax
  - **与 SFT test tax 对比**: 1.7B RSFT tax(-5.43) > SFT tax(-4.86), evidence benefit 扩大; 4B RSFT(+1.51) vs SFT(-0.13) 方向翻转; 14B RSFT(+0.77) vs SFT(-0.32) 方向翻转; 8B/LLaMA 方向一致
  - **叙事**: RSFT 不统一压缩 evidence tax, 而是 scale-dependent 地重塑 model-evidence 关系——小模型获益放大, 中大模型可能引入轻微代价
- **D112 Method B (full pipeline from s44 SFT)**: 4B RSFT bf16 ign_f1=**0.5152** (+4.18pp over SFT s44=0.4734)——确认 RSFT 不依赖特定 SFT seed，pipeline 可复现

### Deep Error Analysis (plan_021 完成)
- **SFT→RSFT 三大改善机制（3 尺度一致）**:
  - **(1) Truncation FN 减少 -16~22%**: 1.7B 获益最大 (-841 FN)。与 evidence tax 的 truncation asymmetry 互洽
  - **(2) Hallucinated FP 减少 -6~12%**: LLaMA 获益最大 (-593, -11.8%)。CED filtering 淘汰了低质量 hallucinated responses
  - **(3) Duplicate 减少 -11~20%**: 1.7B 获益最大 (-20.2%)。与 duplication regularization 发现完全对应
- **未改善**: Evidence exact match 变化 <0.4pp（evidence grounding 需专门信号）; Relation confusion FP 稳定; Rare relation FN 稳定
- **与 Evidence Tax 分析的闭环**: Evidence regularization (tax analysis) ↔ RSFT format regularization (error analysis) 是同一机制的两个视角。小模型需要结构化约束来避免退化输出
- **Per-relation 获益最大**: participant, conflict, league, screenwriter, operator, contains_admin_territory — 跨句推理或长尾实体关系
- **Over-citation trend**: 大模型 over-citation 增加 (12%→17%)，边际预测的 evidence 精度下降
- **k=1 vs k=3 对比**: 1.7B + LLaMA k=1 优于 k=3; 8B k=3 略优 (+0.57 ign_f1)
- **关键 negative finding**: Evidence quality 完全不变 (exact match Δ<0.4pp) → RSFT 改善 RE 但不改善 evidence grounding → 需要专门的 evidence-aware 训练信号 → 直接 motivates GRPO+CED。形成完整 pipeline 故事线：SFT→RSFT(RE提升)→GRPO+CED(evidence提升)
- **Limitation**: "FN: other" 增加 ~13-15%（RSFT 消除 easy errors 但不解决 hard cases: 复杂推理、知识缺失）
- **产出**: art_20260518_cfce4e, LaTeX 表格已生成

## MVP Evidence Summary (D071: 主表报 Ign-F1，附录报 F1; D076 统一协议 rel_f1)

| Config | Ign-F1 | F1 | Δ vs SFT (Ign-F1) | Evi-F1 (cond) | Evi-F1 (joint) | EDCR |
|--------|--------|------|-------------------|---------------|---------------|------|
| **SFT no-evidence** | **47.21** | 48.76 | **+7.47pp** | **—** | **—** | **—** |
| SFT baseline (D076) | 39.74 | 40.49 | — | 79.86 | 31.47 | 0.6982 |
| **CED reranker** | **TBD** | 48.64 | **TBD** | **81.88** | — | **0.6156** |
| RSFT CED s43 (best) | **45.85** | 46.83 | **+6.11pp** | 81.56 | 37.11 | 0.6388 |
| RSFT CED s44 | 45.51 | 46.55 | +5.77pp | 80.87 | 37.13 | 0.6350 |
| RSFT CED s42 | 43.63 | 44.49 | +3.89pp | 81.87 | 34.68 | 0.6565 |
| RSFT CED k=3 | 43.64 | 44.54 | +3.90pp | 80.88 | — | 0.6635 |
| RSFT r2a (1ep) | 44.01 | 44.94 | +4.27pp | 81.08 | 35.09 | 0.6641 |
| RSFT r2b (1ep) | 44.10 | 44.93 | +4.36pp | 81.28 | 34.90 | 0.6609 |
| flat-NLI s42 | 44.49 | 45.39 | +4.75pp | 80.43 | — | 0.6431 |
| flat-NLI s43 (reeval) | TBD | 45.23 | TBD | 81.58 | — | 0.6505 |
| DPO bf16 1ep | 38.88 | 40.34 | -0.86pp | 80.88 | — | 0.7139 |
| DPO bf16 3ep | TBD | 34.29 | TBD | — | — | — |
| GRPO bf16 G=8 (best step) | 45.59 | ~43.4 | +5.85pp | 80.86 | — | — |
| GRPO QLoRA (lr=5e-6) | TBD | 1.38 | TBD | 85.00 | — | 0.9900 |

注：Evi-F1 以百分比显示（×100）。Ign-F1 修正后排名无实质变化（仅 r2a/r2b 互换，差 0.09pp）。TBD 项等待 metrics_v2.json 补算。GRPO bf16 Ign-F1=45.59 > F1=43.4 因 train triples 过滤效应。RSFT CED k=3 数据来源: reeval_rsft_topk3 (ign_f1_corrected=true)。

### D076 统一协议 ign_f1（D152+ 全表修正为 ign_f1）

| Config | ign_f1 | evi_f1 |
|--------|--------|--------|
| SFT baseline | 0.3974 | — |
| CED RSFT mean (s42, s44) | **0.4467** | — |
| CED RSFT s42 | 0.4423 | — |
| CED RSFT s44 | 0.4511 | — |
| flat-NLI RSFT mean (s42, s43_r2) | **0.4475** | — |
| flat-NLI RSFT s42 | 0.4448 | — |
| flat-NLI RSFT s43_r2 | 0.4503 | — |
| LLaMA-8B SFT | 0.5384 | 0.8151 |
| LLaMA-8B no-evidence | 0.5452 | — |
| **--- RSFT Scaling Study (D102 k=1 corrected) ---** | | |
| Qwen3-1.7B SFT | 0.4786 | — |
| Qwen3-1.7B RSFT k=1 s42 | **0.5122** (+3.4pp) | 0.8243, EDCR=0.6224 |
| Qwen3-8B SFT | 0.5051 | — |
| Qwen3-8B RSFT k=1 s42 | **0.5376** | 0.8136, EDCR=0.6231 |
| Qwen3-8B RSFT k=1 s43 | **0.5471** | 0.8180, EDCR=0.6094 |
| Qwen3-8B RSFT k=1 s44 | **0.5451** | 0.8145, EDCR=0.6233 |
| Qwen3-8B RSFT k=1 mean | **0.5433** (std=0.50pp) | — |
| LLaMA-8B RSFT k=1 3-seed mean | **0.5654** (+2.70pp) | std=0.52pp |
| LLaMA-8B RSFT k=1 s42 | 0.5714 | 0.8238, EDCR=0.5799 |
| LLaMA-8B RSFT k=1 s43 | 0.5662 | 0.8287, EDCR=0.5783 |
| LLaMA-8B RSFT k=1 s44 | 0.5587 | 0.8328, EDCR=0.5829 |
| **--- Post-hoc Baseline (D091) ---** | | |
| BM25 entity k=2 | 0.4876 (no-evi) | evi_f1_joint=0.347 |
| BM25 oracle_k | 0.4876 | evi_f1_joint=0.383 |

### Evidence Tax Scaling（D079/D082/D083/D117/D119/D125/D127/D144/D145）

> **符号约定** (D127): tax = ign_f1(no_evidence) - ign_f1(with_evidence)。正值=代价，负值=收益。

| Model | SFT Tax | RSFT Tax | 解读 |
|-------|---------|----------|------|
| Qwen3-1.7B | **-5.63pp** (matched@2048 fair) | **-7.75pp** (@1024) | Within-family threshold: 小模型真实依赖 evidence 作为推理脚手架。matched@2048 fair subset 确认 |
| Qwen3-4B | **≈0** (3-seed mean=+0.25±0.47pp, D146) | **+0.94pp** (@1024) | neutral confirmed (3-seed)。Tax std=0.47pp vs base std=3.6pp——evidence tax 本身表现压缩特性 |
| Qwen3-8B | **+0.04pp** (matched@2048 fair) | **-0.78pp** (@1024) | neutral |
| Qwen3-14B | **+0.03pp** (截断对称，@1024 可信) | **-4.54pp** (D138) | SFT neutral; RSFT evidence 强烈有益 |
| LLaMA-3.1-8B | ⚠️ **极不稳定**: s42 fair=+1.35pp, s44 fair=**-12.62pp**, s43 待完成 | **-1.14pp±0.76pp** (3-seed: s42=-1.88, s43=-1.16, s44=-0.37) | D134/D136: SFT tax swing ~14pp (seed lottery), RSFT tax swing ~1.5pp。**RSFT 压缩 evidence tax 方差 ~10×**。s44 SFT 无 evidence 后 recall 腰斩 (0.49→0.26) + truncation 激增 (240→411)——弱 seed 模型依赖 evidence 作为结构化约束。RSFT format 99.9% 无需 fair correction |

### Cross-Dataset Validation（D080）

| Dataset | Ign-F1 Δ | Evi-F1 | 说明 |
|---------|----------|--------|------|
| DocRED (in-domain) | baseline | — | — |
| Re-DocRED | -3.15pp | 0.817 | evidence extraction 泛化，relation extraction 有损 |

## Anticipated Reviewer Concerns (updated from Dream, D068-D083)

### RC1: "Online RL" 标题过度声称（Dream 三档一致 Critical）
- ~~标题和 claim 收窄到 "GRPO fails for DocRE"~~
- **D068/D069 修正**: 重新定位为 "RL optimization pressure correlates with decoupling severity"——不是 GRPO 特有问题，而是 RL-for-IE 的通用梯度
- DPO 数据支撑 decoupling spectrum（gradual decay confirms the pattern）

### RC2: GRPO G=4 太小 + LoRA confound（Dream 三档一致 Major）
- GRPO G=8 bf16 实验 ✅ — 确认 mild decoupling（-2pp），QLoRA 是 catastrophic amplifier（D065/D066）
- LoRA confound 已解决：bf16 LoRA vs QLoRA 直接对比

### RC3: CED 不显著优于 flat-NLI（Dream 三档一致 Major）
- **已解决（D078）**: paired t-test p=0.44，CED 与 flat-NLI 统计不可区分
- **应对**: 不再声称 CED > flat-NLI；论文定位为 "NLI-based scoring 是关键（CED 和 flat-NLI 均有效），CED 因可解释性作为默认推荐"
- ~~5+ seeds 统计检验~~ → 不再需要，D078 已给出明确结论

### RC4: RSFT 不新颖
- 不声称 RSFT 是贡献；贡献在于任务定义 + decoupling 发现 + EDCR
- 诚实定位 RSFT 为 STaR (NeurIPS 2022) 单轮变体 + domain-specific quality filter

### RC12: SAIS 说 evidence 有用，为何 FREIGE 说 evidence 有害？（文献审查 2026-05-16）
- **关键区分**: discriminative evidence *retrieval*（SAIS/DREEAM — 分类句子是否为证据，作为监督信号提升 RE）vs generative evidence *production*（FREIGE — LLM 生成完整证据文本，额外生成负担导致 scale-dependent 代价）
- SAIS 的 evidence supervision 是分类任务，不增加输出长度；FREIGE 的 evidence generation 显著增加生成序列长度，模型需分配容量同时完成 RE + evidence 生成
- **D079/D083/D144 新弹药**: evidence tax 存在 within-family threshold——1.7B 模型中 evidence 有益（matched@2048 fair_tax=-5.63pp），与 SAIS 的发现方向一致。4B+ 中性（非有害）。这说明 evidence 的效果取决于模型容量和任务范式的交互，而非简单的有害/有益二分
- **应对**: Related Work 中精准讨论此对比，明确 FREIGE 研究的是 *generative production* 设定下的代价，与 *retrieval* 设定下的增益不矛盾——两者揭示了 evidence 在不同范式下的不同角色

### RC13: 单模型单数据集泛化性不足（D077 scope 扩展）
- ~~plan_006: Qwen3-1.7B / 8B model size ablation~~ ✅ D079/D083 完成
- ~~plan_016: LLaMA-3.1-8B cross-family validation~~ ✅ D082 完成
- ~~plan_007: Re-DocRED cross-dataset evaluation~~ ✅ D080 完成
- **结果**: 三项泛化实验全部完成，支撑 C5 scaling pattern + cross-family + cross-dataset 叙事

### RC5: 评测可比性 — ✅ RESOLVED (D093)
- **DREEAM 协议确认**: DREEAM 的 evi_f1=54.01% 等价于我们的 evi_f1_joint（FP/FN triples 计入分母）
- 我们最好: LLaMA-8B RSFT evi_f1_joint=45.71%（差 8.3pp，主要由 RE gap 6.8pp 驱动）
- TP-only evi_f1=82.55% 证明正确预测 triple 的 evidence 质量优秀
- **论文必须**: (1) 用 evi_f1_joint 对比 DREEAM (2) 同时报 TP-only 证明 evidence 质量高 (3) 标明版本避免混淆
- **Framing**: generative LLM 首次做 evidence-grounded DocRE vs encoder-based 专用模型，差距主要来自 RE 而非 evidence

### RC6: EDCR 缺人工验证
- 100 例小规模标注

### RC7: Missing DPO/PPO（Dream 两档 Major）
- DPO experiment ✅ — 结果确认 decoupling spectrum（D067/D068）

### RC8: Dev-test degradation
- **Evidence tax test spot-check (D147, in progress)**:
  - 1.7B: dev -5.63pp → test -4.86pp ✅ (both evidence helps)
  - 14B: dev +0.03pp → test -0.32pp ✅ (both near-neutral)
  - 8B: dev +0.04pp → test **-1.71pp** ⚠️ (dev neutral, test mild benefit — 方向轻微不一致，但幅度仍属 near-neutral 范围，远小于 1.7B 的 ~5pp)
  - 4B/LLaMA: pending
- **8B deviation 缓解因素**: (1) dev 用 matched@2048 format-compliant intersection protocol，test 用全量 500 docs——评估协议不同; (2) 单 seed 无 error bar; (3) -1.71pp 仍远小于 1.7B 阈值效应
- **措辞影响**: 保持 "approximately neutral at ≥4B"，不 claim "exactly neutral"。可加注 "with possible mild benefit at larger scales"

### RC9: 连接 reward overoptimization 文献
- 显式引用 Gao et al. 2023

### RC10: Post-hoc evidence retrieval baseline — ✅ RESOLVED (D091)
- BM25 entity_only k=2: evi_f1_joint=0.347, EDCR=0.766 → 弱于 RSFT joint generation (0.361, EDCR=0.654)
- Oracle_k (=GT k): evi_f1_joint=0.383 略胜 RSFT，但 EDCR 仍差 7.9pp 且不实用
- 防御策略：指出 joint generation 的 evidence 更 faithful（EDCR 低 11pp），且一次推理完成无需额外检索管线
- NLI retrieval 变体降为 rebuttal 备用

### RC11: "RL 不遗忘" 文献与 Claim 2 的张力（文献扫描 2026-05-16）
- 近期多篇论文（arXiv 2507.05386, 2506.23508, 2509.04259）论证 RL fine-tuning 天然缓解 catastrophic forgetting
- **关键区分**: FREIGE 的 decoupling 是 **intra-task multi-objective trade-off**（RE 抽取 vs evidence 生成两个优化目标的竞争），不是 **inter-task forgetting**（丢失预训练知识）。两者机制不同
- bf16 GRPO 的 mild decoupling（-2pp）恰好印证这一点：模型没有忘记"怎么做 IE"，而是在 evidence reward 压力下偏移了 RE-evidence 的资源分配
- **应对**: Related Work / Discussion 中显式回应这组文献，区分 intra-task trade-off vs inter-task forgetting
- **QuRL/QaRL 文献支撑 Claim 2**: QuRL 发现 quantized vs full-precision actor divergence 在长训练中指数增长（直接支撑 QLoRA amplification 叙事）；QaRL 的 error token failure mode 与 QLoRA GRPO garbled evidence 吻合

## Key Baselines (12+)

1. **SFT-only**: Qwen3-4B + LoRA SFT（with evidence）
1b. **SFT no-evidence**: Qwen3-4B + LoRA SFT（无 evidence，upper bound ablation）
2. **RSFT flat-NLI**: flat-NLI scored RSFT（核心 ablation）
3. **RSFT CED**: CED scored RSFT（主方法）
4. **CED-as-reranker**: 推理时 CED 重排（无训练）
5. **DPO+CED**: offline preference learning — gradual decoupling（D067/D068）
6. **GRPO+CED (QLoRA, G=4)**: catastrophic decoupling baseline
7. **GRPO+CED (bf16, G=8)**: mild decoupling — QLoRA confound 排除（D065/D066）
8. **Post-hoc retrieval**: SFT + BM25 evidence（NEW）
9. **DREEAM**: encoder evidence SOTA
10. **SAIS**: encoder evidence baseline
11. **DocKS-RAG**: extraction SOTA（无 evidence）
12. **LMRC**: generative LLM SOTA（无 evidence）

## Publishability Threshold (revised after D078-D083)

- **必要条件**: (1) RSFT 在 test set 上 Ign-F1 显著 > SFT (2) DREEAM-protocol Evi-F1 可报告 (3) Decoupling spectrum 有完整数据支撑（GRPO QLoRA/bf16 + DPO + RSFT）
- **充分条件**: 上述 + EDCR 人工验证 + scaling pattern (C5) 完整
- **已达成**: CED vs flat-NLI 统计检验完成（D078: 不可区分，不再是充分条件要素）; 泛化实验完成（D079/D080/D082/D083）
- **Failure pivot**: decoupling spectrum 不成立（bf16 GRPO 也 catastrophic）→ scope 大幅缩减。**已排除**: bf16 GRPO 确认 mild（D065/D066）

## Statistical Rigor Requirements (D131)

- 所有 multi-seed 结果报 **sample std (ddof=1)** + **N** 标注
- 表头标注 seed 数量（e.g., "mean ± std (N=3)"）
- Appendix 放 bootstrap CI（1000 resamples）
- 关键 claim 做 paired t-test 或 Wilcoxon（RSFT > SFT per scale）
- Variance compression 防御：4 个独立 scale 同方向压缩 + 明确 mechanism (CED filtering)

## Research Phase Priorities (revised D131)

**Active（迁移后立即执行）**:
| Priority | 实验 | Claim | GPU-h | 状态 |
|----------|------|-------|-------|------|
| P0 | 14B RSFT gen resume + CED + train + eval | C3 | ~15-20h | 等迁移 milestone B |
| P0 | LLaMA SFT s43/s44 retrain + eval (3-seed) | C3 | ~6h | 等迁移 milestone A |
| P0 | eval_llama_sft_s42_no_evidence_std | C3 | ~0.5h | 等 LLaMA SFT 完成 |
| P0 | Test set eval: SFT + RSFT best + no-evidence (3 configs) | C1 | ~3h | 等 14B 完成 |

**Writing（迁移期间可推进）**:
| Priority | 任务 | 说明 |
|----------|------|------|
| P0 | 统一叙事主线 rewrite (Intro/Abstract/Conclusion) | D131 unified narrative |
| P0 | 所有表格加 error bars / std / N 标注 | Statistical rigor |
| P0 | Evidence tax 表统一为 inference-time | 方法论一致性 |

**Deferred / Rebuttal 弹药**:
| Priority | 实验 | 说明 |
|----------|------|------|
| P1 | EDCR human validation (100例) | C4 |
| P1 | 14B RSFT 2nd seed | 从 single observation 升级为 reproducible |
| P2 | 3rd model family (plan_022) | Reviewer 建议不是 submission 必需 |
| P2 | DocKS-RAG / LMRC 复现 | Generative SOTA 对比 |
| P2 | Advantage variance measurement | C2 |
