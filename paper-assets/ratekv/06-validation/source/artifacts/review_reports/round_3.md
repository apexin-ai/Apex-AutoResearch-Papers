---
round: 3
overall_score: weak reject
timestamp: 2026-05-15T15:42:23.926754+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 2 审稿报告 — ratekv

**论文**: When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic
**Venue**: EMNLP 2026 Main Conference (ACL ARR May cycle)
**审稿人**: Reviewer 1（方法严谨性 + 实验验证）、Reviewer 2（新颖性 + 完整性 + 写作）
**交叉回应**: 完成，1 轮即收敛

---

## Summary

本文研究 per-head mixed-precision KV cache 量化在硬件对齐 bit-width {2,4,8,16} 下的有效性。核心发现：(1) unconstrained MCKP/greedy solver 因 2-bit 量化误差的 super-additive compounding 导致灾难性退化（Qwen2.5-7B: 32-37 PPL vs uniform 15.45）；(2) 一条 cardinality constraint（限制 2-bit head 数量）即可修复；(3) 7 个模型中仅 Qwen2.5-7B 从非均匀分配获益（-29.4%），其余 6 个模型 ≈ uniform。论文提出基于 concentration + t₁/t₅ ratio 的经验判别规则来分类 spread/spike/flat 架构。

---

## Strengths

- **S1 [consensus]**: **有价值的负面结论**。6/7 模型上非均匀分配无效的系统性发现，对社区有重要参考价值——避免后续工作在不适用的架构上浪费算力。"When does it NOT help" 的研究视角在 KV cache 量化文献中稀缺。

- **S2 [consensus]**: **MCKP + cardinality constraint 形式化干净**。将 per-head bit-width 选择建模为 cardinality-constrained MCKP，cardinality constraint 作为 minimal intervention 的理论动机清晰。证明 constraint 使 greedy 和 MCKP 等价，支持 O(H log H) 简单实现。

- **S3 [consensus]**: **Compounding effect 的系统刻画**。Section 3.3 的 super-additivity 数据（1.56×–4.89×）和 U-shaped curve 为理解 2-bit 量化失败模式提供了有用的 empirical evidence，这一观察本身对社区有价值。

- **S4 [consensus]**: **实验设计覆盖全面**。5 架构族 7 模型（MHA 到 GQA 8:1），含 within-family scale contrast（Qwen 7B vs 14B）。Cross-dataset validation (96-97%)、multi-seed stability (10.99±0.06)、profiling resolution 消融、long-context generalization 等提升可信度。

- **S5 [consensus]**: **KIVI 对比的诚实定位**。明确承认 "orthogonal, not competitive"，KIVI+MCKP 无额外收益，方法仅在 symmetric-only 环境有独立价值。这种透明度值得肯定。

---

## Weaknesses

### Critical

- **W1: Decision rule 的 N=1 正样本构成根本性统计缺陷** [R1 critical, R2 AGREE]
  - 2 个自由参数（concentration ~0.50, t₁/t₅ ~0.70）在 7 个样本上 7/7 分类，正样本仅 Qwen2.5-7B。任何能将 1 点与 6 点分开的线性分界面都能 100%——这不是 discriminative power 的证据。无 LOO-CV、无 threshold sensitivity analysis、无 bootstrap CI。
  - **与 Round 1 关联**: Round 1 R1-W1 要求增加模型（done: +Qwen-14B, +Pythia）和降级 claim（done: "diagnostic framework" → "empirical decision rule"）。Round 2 判定：修复不充分。问题本质不变——正样本仍为 N=1。
  - **Round 2 新增层面 (R2-W2)**: 即使 rule 统计上成立，其实用价值也为零——profiling 数据已是 solver 输入，直接跑 O(H log H) solver 比判别规则更直接。Rule 的真正价值是解释性而非决策性，但论文定位为 Contribution 3。
  - **建议**: (a) 从 contribution 列表中移除或大幅降级为 "preliminary observation on 7 models with 1 positive case"；(b) 补充 threshold sensitivity analysis；(c) 如保留，重新定位为 analytical insight 而非 practical tool。

- **W2: Compounding 因果论证不够严谨** [R1 critical, R2 AGREE with nuance]
  - 论文将 2-bit compounding 定位为 "the cause of catastrophic failure"（Introduction contribution 1），但 super-additivity 数据仅在 Qwen2.5-7B 上收集。其他 6 个模型未展示 compounding curve。
  - R2 的 nuance：机制解释（residual stream error accumulation）物理上合理，Table 1 数据显示非线性放大确实存在，但 "cause" 在科学论文中需要排除替代假说的实验设计。
  - **建议**: (a) "cause" → "a major contributing factor"；(b) 在 1 个 flat + 1 个 spike 模型上展示 compounding curve；(c) 设计控制实验分离 compounding 与 selection effect。

### Major

- **W3: Abstract "29.4% reduction" 的突出呈现具有误导性** [R2 major, R1 AGREE]
  - 29.4% 仅来自 1/7 模型，但作为 abstract lead metric 给读者 "方法普遍有效" 的第一印象。Abstract 第 3 行确实有 "one spread-pattern model" 限定，但 headline 效应已经形成。
  - **建议**: 重组 abstract 叙事顺序：先陈述主要发现（"7 个模型中 6 个无收益"），再以 Qwen 为 case study 给出 29.4%。

- **W4: 与 RateQuant 的增量贡献界定模糊** [R2 major, R1 AGREE with reservation]
  - RateQuant 已将 per-head bit-width 选择公式化为 MCKP 并证明 greedy 最优性。本文技术增量归结为一条 linear inequality (Eq.2)。论文的真正贡献在于：(a) compounding diagnosis，(b) mostly-negative finding，(c) heterogeneity characterization——但叙事重心偏向算法。
  - R1 补充：RateQuant 处理 {2,3,4,5,6}，本文处理 {2,4,8,16}，这是实践中有意义的差异。但算法层面增量确实薄。
  - **建议**: Introduction 中明确区分——RateQuant 解决了 formulation，本文发现了 RateQuant 在实践中的 failure mode 并给出 characterization。

- **W5: 模型规模 ≤14B 限制泛化性** [R1 major, R2 AGREE]
  - KV cache 压缩需求主要在 70B+。Qwen 7B→14B 已显示 spread→flat dilution，暗示更大模型可能更 flat——进一步缩小方法适用范围。
  - **建议**: 至少验证 1 个 30B+ 模型，或分析 head 数量 scaling 对 concentration 的理论影响。

- **W6: Downstream evaluation 无 confidence intervals** [R1 major, R2 AGREE]
  - Table 3 差异 ±0.1-1.2%，完全在 0-shot 评估噪声范围内（typical std 0.5-1.5%）。3-seed stability 仅 Qwen PPL。
  - **建议**: 对 Table 3 关键对比加 3+ seed mean±std。

- **W7: Runtime benchmark 仅 PyTorch-level simulation** [R1 major, R2 AGREE with nuance]
  - 8.5% overhead 来自 dispatch，非 real kernel。论文在 Appendix K 有 caveat 但 Limitations section 未提及。
  - R2 nuance：核心贡献不是 runtime system，即使无 benchmark 论文 claim 仍成立。但既然展示了数据就需保证可信。
  - **建议**: 将 simulation caveat 移入 Limitations。如可能用 vLLM/TRT-LLM 做 real benchmark。

- **W8: "Catastrophic failure" 叙事过度渲染** [R2 minor-to-major, R1 AGREE]
  - "Catastrophic" 仅适用于 Qwen (3.3× bf16)。其他模型：Gemma-2 1.47×，其余 ~1.07-1.12×。Abstract 用复数 "spread architectures" 但只有 1 个 spread。
  - **建议**: 限定 "catastrophic" 于 Qwen/spread 语境。Flat 模型用 "moderate degradation"。

### Minor

- **W9: Spread/spike/flat 术语缺乏 formal definition** [R2 minor, R1 AGREE]
  - Soft boundaries（≳0.50, ≲0.70）有重叠。Flat 定义尤其模糊。需 crisp inequality。

- **W10: Limitations section 过于简短** [R2 minor, R1 strongly AGREE]
  - 仅 2 句。缺少：threshold generalization、downstream scope、calibration domain robustness、missing competitors。ACL ARR 要求充分讨论。

- **W11: Long-context 评估覆盖不足** [R1 minor, R2 AGREE]
  - 仅 Qwen + Llama × 8K。KV cache 压力场景在 32K-128K。

---

## Reviewer Consensus

以下问题两位 Reviewer 达成一致：

1. **[AGREE] Decision rule 是论文最大弱点**——N=1 正样本无统计意义，且与直接运行 solver 相比无实用增量。应从 contribution 降级或移除。
2. **[AGREE] Compounding 机制合理但 "cause" 措辞过强**——应改为 "major contributing factor"，并补充其他模型的 compounding 数据。
3. **[AGREE] Abstract framing 需调整**——先负面结论（6/7 无收益）再正面 case study（Qwen 29.4%）。
4. **[AGREE] 核心贡献应重新定位为实证发现**——算法增量薄（RateQuant + 一条约束），真正价值在 compounding diagnosis + mostly-negative finding。
5. **[AGREE] 模型规模和统计可靠性有待加强**——14B 上限、无 CI downstream、runtime simulation。
6. **[AGREE] Limitations 需大幅扩展**。

## Reviewer Divergence

1. **Baseline 缺失 (KVTuner 等)**：R1 认为 major weakness——缺少直接 competitor 对比。R2 rebut——KVTuner 是 layer-level 不是 per-head，GEAR/Kitty 是不同量化范式，非 fair baseline。R2 concedes KVTuner 可作 informative reference。**Director 判断**: R2 的 rebuttal 有理——granularity 和方法范式不同。但作为 informative comparison 纳入 KVTuner 是合理的改进方向。记为 optional action。
2. **Symmetric-only 定位**：R1 认为 minor weakness——实用场景不清晰。R2 rebut——symmetric 仍是 vLLM/SGLang 默认，kernel 更简单。**Director 判断**: R2 的 rebuttal 合理。低优先级。

---

## Questions（需要作者澄清）

1. 其他 6 模型是否也展示 super-additivity？如果是，为什么不从 constraint 获益？如果不是，compounding 机制如何普遍化？
2. Decision rule thresholds 的选择方法？Grid search vs visual inspection？Sensitivity analysis？
3. Spread pattern 是模型固有属性还是校准数据的函数？C4/WikiText-2 以外的 domain 如何？
4. Profiling + k sweep + solver 的端到端 wall-clock 开销是多少？
5. Flat 模型上 constrained MCKP 是否产生与 uniform 完全相同的 allocation？如果不同但 PPL 等效，这个 distinction 应明确。
6. Table 2 的 unconstrained MCKP 与 RateQuant 的精确关系？

---

## Missing References

**共识引用建议** (R1+R2 均提及或交叉同意)：
- 更新 bib 中已被会议接收的 arXiv preprints 的 venue 信息
- 核查 4 条 author 顺序不一致的条目（hooper2024kvquant, li2024snapkv, xiao2024streamingllm, xia2025kitty）

**R2 补充引用**：
- Cocktail (Tian et al., 2025): chunk-adaptive mixed precision
- MiKV / "No Token Left Behind" (Yao et al., 2024): token-level importance-aware mixed precision
- "More Tokens, Lower Precision" (2024): token-precision tradeoff

---

## Overall Assessment

### ARR 维度综合评分

| 维度 | R1 | R2 | 综合 |
|------|----|----|------|
| Soundness | 3.0/5 | 3.5/5 | **3.25/5** |
| Excitement | 2.5/5 | 2.5/5 | **2.5/5** |
| Overall | 2.5/5 | 3.0/5 | **2.75/5** |
| Confidence | 4/5 | 4/5 | **4/5** |
| Reproducibility | 4/5 | 3.5/5 | **3.75/5** |

### 总体评分: **weak reject** (main conference) / **borderline accept** (Findings)

### 判断依据

**Main conference bar 未达到**:
- 技术新颖性有限——核心算法增量是 RateQuant formulation + 一条 cardinality constraint
- 正面结果仅限 1/7 模型，方法适用范围极窄
- Decision rule（Contribution 3）在统计和实用两个维度上均不成立
- 模型规模上限 14B 限制了对 KV cache 压缩这一研究方向的实际影响

**Findings 可接受**:
- 实验工作扎实（7 模型、cross-dataset、multi-seed、KIVI 对比）
- "非均匀 KV cache 量化在大多数架构上无效" 的系统性负面结论对社区有重要参考价值
- Compounding effect 的刻画为后续工作提供了有用的 failure mode analysis
- 论文对自身方法局限性的承认（KIVI 比较、Limitations section）是诚实的

### 接收路径建议（供 Research Director 参考，非审稿建议）

如目标为 Findings:
1. [Must-Fix] 将 decision rule 从 Contribution 降级为 analytical observation
2. [Must-Fix] Abstract 重组——先负面结论再正面 case
3. [Must-Fix] "cause" → "contributing factor"，补 1-2 个模型 compounding curve
4. [Must-Fix] Limitations 大幅扩展
5. [Should-Fix] Downstream eval 加 CI
6. [Should-Fix] 形式化 spread/spike/flat 定义

如目标为 Main Conference:
- 以上全部 + 找到额外 spread 模型（N≥2 正样本）+ 30B+ 验证

---

## Issue Tracker 状态

- **Round 1**: 13 issues, 全部 resolved
- **Round 2**: 10 new open issues（2 critical, 6 warning, 2 info），2 divergence issues
- **跨轮复发**: R1-W1（diagnostic overfitting）在 Round 1 resolved 后 Round 2 重新 open——Round 1 的修复（增加 2 模型 + 降级 claim）未充分解决根本问题（N=1 正样本）