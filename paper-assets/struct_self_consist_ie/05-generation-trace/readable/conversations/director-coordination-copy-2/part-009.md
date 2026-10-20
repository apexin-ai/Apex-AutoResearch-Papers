# Director coordination — Part 9 of 16

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Conversation logs

[← Part 8](part-008.md) · [Transcript overview](../director-coordination-copy-2.md) · [Part 10 →](part-010.md) · [Structured JSON](../../../sessions/6a/6a5a1a2f9a2bf6bdf404.json)

## Round 193

### Tool call

_source line 2589 · 2026-05-20T12:48:05.464344+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "struct_self_consist_ie",
  "text": "你是 Reviewer 2，负责**新颖性 + 论文完整性 + 写作质量 + Related Work**。\n\n## 投稿信息\n- **Venue**: EMNLP 2026 Main Conference (Long Paper via ARR May 2026)\n- **Deadline**: 2026-05-25\n- **页数限制**: 正文 ≤ 8 页，参考文献不限。Limitations 和 Ethics Statement 不计入页数\n- **模板**: ACL style template（double-blind）\n- **匿名规则**: double-blind\n\n## 论文路径\n- LaTeX: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf`\n- Sections 目录: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/`\n\n## 审查侧重\n\n请重点审查以下方面：\n\n1. **新颖性评估**：\n   - 核心贡献的新颖性：(a) QE framework for NER, (b) correlation-selection gap 诊断, (c) entity construction, (d) degeneracy decomposition\n   - Entity construction 本质上是 Florian et al. (2003) entity voting 迁移到 stochastic sampling + LP weighting。LP weighting 增量仅 0.28-0.66pp——这是否足够作为独立贡献？\n   - 与 Yao et al. (2026) 的差异化是否清晰？他们也做了 LLM-based NER/RE 的 consistency 分析\n   - 论文定位为 \"diagnostic + partial mitigation\" 而非 \"提出新方法\"——对 EMNLP Main 是否足够？\n   - \"Correlation-selection gap\" 中哪些部分是 by construction（instance-level signals 无法做 selection 是定义决定的），哪些是 empirical finding？\n\n2. **论文完整性**：\n   - 贡献 1-4 的支撑是否充分？每个 claim 是否都有足够的实验证据？\n   - SCD (§5.2) 标注为 \"ongoing\"——在投稿版本中包含未完成的工作是否合适？\n   - Cross-model self-consistency (§5.1) 标注为 \"preliminary\"——同上\n   - Limitations 是否诚实全面？是否有明显遗漏？\n   - 仅测试 LoRA fine-tuned models + 72B zero-shot——scope 声明是否充分？\n\n3. **写作质量**：\n   - Abstract 信息密度是否合适（当前已控制在 4 个关键数字）？\n   - Introduction 的叙事结构：problem → gap → contributions 是否清晰？\n   - 术语一致性（F1 metric 的不同称呼、signal 名称等）\n   - 图表质量：Figure 1 概览图、Figure 2 selection gap 图、散点图等\n   - 正文 8 页限制是否满足？（PDF 38 页含 appendix）\n\n4. **Related Work**：\n   - 引用覆盖度：test-time scaling、consistency for IE、MBR decoding、uncertainty estimation\n   - 是否有遗漏的重要相关工作？特别是：\n     - Ensemble-based IE 方法\n     - Per-sample confidence estimation（Self-Certainty, P(True) 等——论文在 Limitations 中提到但未测试）\n     - Constrained decoding 与 diversity 的关系\n   - 与最新 2025-2026 工作的对比是否充分？\n\n请按以下格式输出审稿意见：\n1. Summary（2-3 句）\n2. Strengths（逐条）\n3. Weaknesses（逐条，标注 severity: critical/warning/info）\n4. Questions（需要作者回答的）\n5. Missing References（如有）\n6. Overall Assessment + 评分 + 置信度"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "struct_self_consist_ie",
    "text": "你是 Reviewer 2，负责**新颖性 + 论文完整性 + 写作质量 + Related Work**。\n\n## 投稿信息\n- **Venue**: EMNLP 2026 Main Conference (Long Paper via ARR May 2026)\n- **Deadline**: 2026-05-25\n- **页数限制**: 正文 ≤ 8 页，参考文献不限。Limitations 和 Ethics Statement 不计入页数\n- **模板**: ACL style template（double-blind）\n- **匿名规则**: double-blind\n\n## 论文路径\n- LaTeX: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf`\n- Sections 目录: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/`\n\n## 审查侧重\n\n请重点审查以下方面：\n\n1. **新颖性评估**：\n   - 核心贡献的新颖性：(a) QE framework for NER, (b) correlation-selection gap 诊断, (c) entity construction, (d) degeneracy decomposition\n   - Entity construction 本质上是 Florian et al. (2003) entity voting 迁移到 stochastic sampling + LP weighting。LP weighting 增量仅 0.28-0.66pp——这是否足够作为独立贡献？\n   - 与 Yao et al. (2026) 的差异化是否清晰？他们也做了 LLM-based NER/RE 的 consistency 分析\n   - 论文定位为 \"diagnostic + partial mitigation\" 而非 \"提出新方法\"——对 EMNLP Main 是否足够？\n   - \"Correlation-selection gap\" 中哪些部分是 by construction（instance-level signals 无法做 selection 是定义决定的），哪些是 empirical finding？\n\n2. **论文完整性**：\n   - 贡献 1-4 的支撑是否充分？每个 claim 是否都有足够的实验证据？\n   - SCD (§5.2) 标注为 \"ongoing\"——在投稿版本中包含未完成的工作是否合适？\n   - Cross-model self-consistency (§5.1) 标注为 \"preliminary\"——同上\n   - Limitations 是否诚实全面？是否有明显遗漏？\n   - 仅测试 LoRA fine-tuned models + 72B zero-shot——scope 声明是否充分？\n\n3. **写作质量**：\n   - Abstract 信息密度是否合适（当前已控制在 4 个关键数字）？\n   - Introduction 的叙事结构：problem → gap → contributions 是否清晰？\n   - 术语一致性（F1 metric 的不同称呼、signal 名称等）\n   - 图表质量：Figure 1 概览图、Figure 2 selection gap 图、散点图等\n   - 正文 8 页限制是否满足？（PDF 38 页含 appendix）\n\n4. **Related Work**：\n   - 引用覆盖度：test-time scaling、consistency for IE、MBR decoding、uncertainty estimation\n   - 是否有遗漏的重要相关工作？特别是：\n     - Ensemble-based IE 方法\n     - Per-sample confidence estimation（Self-Certainty, P(True) 等——论文在 Limitations 中提到但未测试）\n     - Constrained decoding 与 diversity 的关系\n   - 与最新 2025-2026 工作的对比是否充分？\n\n请按以下格式输出审稿意见：\n1. Summary（2-3 句）\n2. Strengths（逐条）\n3. Weaknesses（逐条，标注 severity: critical/warning/info）\n4. Questions（需要作者回答的）\n5. Missing References（如有）\n6. Overall Assessment + 评分 + 置信度"
  }
}
```

</details>

---


### Tool result

_source line 2590 · 2026-05-20T12:48:07.081338+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1616
}
```

</details>

---


### Assistant

_source line 2591 · 2026-05-20T12:48:14.163087+00:00_

视觉审查已派发，两位 Reviewer 已分配。等待审稿结果返回。

- **视觉审查 Agent**: 已启动（fire-and-forget）
- **Reviewer 1**（方法/实验/统计）: 已分配
- **Reviewer 2**（新颖性/完整性/写作/Related Work）: 已分配

等待 Reviewer 返回初审意见，届时进入 Step 2 交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 194

## Round 194

24 recorded events


### User

_source line 2592 · 2026-05-20T12:54:08.696944+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 审稿意见（方法严谨性 + 实验设计 + 统计分析）

**论文**: "Strong Predictors, Weak Selectors: Addressing the Correlation-Selection Gap in Self-Consistency for Named Entity Recognition"
**Venue**: EMNLP 2026 Long Paper (ARR May 2026)

---

## 1. Summary

本文研究自一致性（self-consistency）在 NER 等结构化预测任务中的失效机制。作者提出一个包含五种置信度信号的诊断框架，发现所有信号均能可靠估计生成质量（ρ up to 0.45, AUROC up to 0.82），但无法有效执行 sample selection——即"correlation-selection gap"。论文将失效归因于三种结构性故障模式（instance degeneracy、isolated headroom、LP compression），提出 entity-level construction（形式化为 MBR decoding）部分弥合该差距，并给出退化分解的理论上界。

---

## 2. Strengths

**S1. 系统且原创的诊断框架。** 将 test-time scaling 问题分解为 quality estimation vs. sample selection 两个正交维度，是对该领域的结构性贡献。五种信号跨四个 NER 基准的全面评估（Table 3, Figure 6 heatmaps）提供了比现有文献更细粒度的理解。

**S2. 统计处理水准显著高于同类工作。** Bootstrap CI（Table 13）、Holm-Bonferroni 多重检验校正（k=57）、paired bootstrap 对比、TOST 等价性检验（Table 16, Appendix F）、permutation tests（Table 9）——在 NLP 论文中罕见地系统。效果量和 p 值的报告（包括不显著结果如 SciERC p_adj=0.20）是诚实的学术实践。

**S3. Entity construction 与 MBR 的理论联系。** Proposition 1（§6.1）将 entity-level majority vote 形式化为 MBR decoding with balanced set-overlaps，提供了清晰的决策论基础。这不仅解释了方法为何有效，也指出了适用边界。

**S4. 极其详尽的 appendix。** 28 页补充材料覆盖了 robustness（N-scaling, temperature, seed stability）、controlled ablations（§7.4）、per-entity-type analysis（Appendix W）、free-form decoding ablation（Appendix O）、cross-dataset OOD（Appendix S）等，几乎预见了所有可能的审稿疑问。

**S5. 实用的诊断协议。** §Z 的三步协议（measure degeneracy → assess signal-quality alignment → evaluate aggregation）为从业者提供了可直接使用的框架，超越了纯分析论文的范畴。

---

## 3. Weaknesses

### Must-Fix 问题（影响接收决定）

**N1 [critical] "Correlation-selection gap" 的核心发现存在 by-construction 成分**

- **具体位置**: §4 第一段, Abstract, §1
- **问题**: 论文的五种信号中，四种（SJ, VC, FK, EM）是 instance-level 的——§4 开头明确承认"Four of five signals assign identical scores to all candidates from the same input by construction"。这意味着这四种信号在设计上就不可能进行 per-sample selection，correlation-selection gap 对它们而言是**定义性推论**而非经验发现。唯一具备 per-sample discrimination 能力的 LP 确实展现了部分 selection 能力（Few-NERD +1.30pp, p<0.01），但被 compression 限制。论文将五种信号的 gap 统一呈现为一个"surprising empirical finding"，夸大了发现的经验性成分。
- **为什么影响接收**: 这是论文的 title claim 和核心叙事。如果 4/5 的 gap 是 by construction，则论文的 empirical contribution 实质上缩小为"LP 的 selection 能力受 compression 限制"，叙事力度显著减弱。
- **建议修改方向**: (1) 在 §4 开头明确区分 definitional gap（instance-level signals）和 empirical gap（LP），给两类 gap 不同的权重；(2) 重写 abstract/intro 的叙事框架，将 LP 的 compression-limited selection 作为核心经验发现，而非将所有五种信号的 gap 等权呈现；(3) 讨论为何不设计更多 per-sample signals（如 per-sample entropy、token-level LP variance 等）。

**N2 [critical] Cross-dataset 分析（ρ=0.052, p=0.81, n=23）严重 underpowered，但被用于支持 null 结论**

- **具体位置**: §7.3 ("degeneracy alone does not predict LP gain"), Figure 3, 正文 p.6
- **问题**: 23 个 configurations 的 cross-dataset 相关分析被用于得出"degeneracy does not predict LP gain"（ρ=0.052, p=0.81）。但 n=23 的 statistical power 极低：检测 ρ=0.3 at α=0.05, 80% power 需要 n≈85；检测 ρ=0.4 也需要 n≈47。当前样本量的 power 仅约 50%（for ρ=0.4），无法可靠地拒绝中等效应量的备择假设。论文将 p=0.81 解读为"degeneracy does not predict"，但这可能仅仅是 underpowered。
- **为什么影响接收**: 这一 null 结论直接支撑了论文的核心论点之一——degeneracy 是 dataset-intrinsic 的而非 predictive 的。如果该结论不可靠，§6.3 degeneracy decomposition 的 practical relevance 会受质疑。
- **建议修改方向**: (1) 报告 post-hoc power analysis，明确当前样本量可检测的最小效应量；(2) 将结论措辞从 "does not predict" 改为 "we did not find evidence for prediction, but the analysis is underpowered (n=23)"；(3) 如有可能，增加更多 configurations（更多 model sizes、temperatures、N 值）以提高统计效力。

### Should-Fix 问题（影响评分但不一票否决）

**W1 [warning] SciERC entity construction 增益（+1.02pp）未通过多重检验校正**

- **具体位置**: §7.5, Table 6, p.8
- **问题**: Few-NERD 上的 +1.40pp 通过了 Holm-Bonferroni (k=57)，但 SciERC 上的 +1.02pp 校正后 p_adj=0.20，**不显著**。论文在正文中的呈现方式（"LP-weighted entity construction yields ... +1.02pp on SciERC"）容易让读者忽略这一不显著性。两个数据集是论文的主要实验平台，其中一个的核心结果不显著，这对方法的 generalizability 是实质性打击。
- **建议**: 在正文中更显著地标注 SciERC p_adj=0.20（不仅在括号内），讨论为何 SciERC 不显著（样本量？degeneracy 程度？），以及这对方法适用范围的含义。

**W2 [warning] Holm-Bonferroni k=57 的 family 定义不透明**

- **具体位置**: §7.5, p.8
- **问题**: 论文使用 k=57 进行 Holm-Bonferroni 校正，但从未明确解释这 57 个假设检验的具体构成。是所有 pairwise signal comparisons × datasets？所有论文中的统计检验？还是 entity construction 相关的所有对比？Family 定义直接影响校正严格程度，对读者评估结果可靠性至关重要。
- **建议**: 在 appendix 中列出 57 个检验的明细（或至少给出构成规则），并讨论 family 定义的选择是否保守/宽松。

**W3 [warning] 72B zero-shot vs 8B fine-tuned 比较同时变化了三个因素**

- **具体位置**: Table 2 (p.6), §6.2, Limitations (p.8)
- **问题**: 72B zero-shot 与 8B fine-tuned 的对比同时改变了 model scale、training regime（zero-shot vs. fine-tuned）、和 quantization。论文在 Limitations 中坦承 "individual effects cannot be disentangled"，但在 §6.2 Scaling Behavior 中仍从该对比中得出关于 scaling 的结论（"the gap persists at 72B"）。
- **建议**: (1) §6.2 的 conclusions 应更加审慎，明确标注 confounded comparison；(2) 如有可能，加入 72B fine-tuned 或 8B zero-shot 的对比点以分离因素。

**W4 [warning] 关键实验的 seed 数量偏少（2-3 seeds）**

- **具体位置**: Table 1 (2-seed mean for SciERC), Table 3 (3 seeds), Appendix H (Table 18)
- **问题**: 主要 QE 结果（Table 3）使用 primary seed=42 + 3 seeds 报告 σ=0.012。SciERC LP selection（Table 1）仅 2-seed mean。Appendix H Table 18 的 multi-seed stability 分析使用 3 seeds。考虑到 few-shot NER 的高方差（论文自身报告 Few-NERD VC σ=0.48pp），3 seeds 的统计效力有限。特别是 SciERC 样本量只有 n=529，seed 间的方差可能被低估。
- **建议**: (1) 讨论为何 3 seeds 足够（或坦承不够）；(2) 对核心结论，报告 3-seed results 是否改变任何 directional finding。

**W5 [warning] Proposition 1 的 "entity-wise independence" 假设未经验证**

- **具体位置**: §6.1, Appendix N.1
- **问题**: Proposition 1 将 entity construction 形式化为 MBR，但核心假设是 entity-wise independence——每个 entity candidate 的 inclusion decision 独立于其他 entities。在实际 NER 中，entities 之间存在强依赖（嵌套实体、句法约束、同一 span 的竞争标注）。论文未提供经验证据验证该假设在实际数据上的近似程度。
- **建议**: (1) 在 SciERC/Few-NERD 上测量 entity decisions 之间的 conditional dependence（如计算 entity co-occurrence 的互信息）；(2) 或至少讨论该假设的违反对结论的影响方向和程度。

**W6 [warning] Degeneracy bound 极度松弛，实际恢复率仅 3-12%**

- **具体位置**: §6.3, Figure 9 (p.27), Appendix N.3
- **问题**: 退化分解上界 E[ΔF₁] ≤ (1−D)·G_nd 在所有 16 个 positive-gain configurations 中，实际 SC gain 仅占上界的 3-12%（论文 p.6: "the bound is loose because α — signal alignment — is the bottleneck"）。这意味着该 bound 的预测能力极弱——知道上界几乎不能帮助判断 SC 是否有效。
- **建议**: 讨论 bound 的 tightening 方向（能否引入 α 的 empirical estimate 使 bound 更 informative？），以及在 bound 如此松弛的情况下，decomposition 的实际价值体现在哪里（diagnostic insight vs. predictive power）。

---

## 4. 小问题（不影响接收）

- **Table 2 中 "n/a" 和 "†" 标记的说明分散在 caption 和 footnotes 中**，建议统一到 caption 底部，减少读者认知负担。
- **Figure 1** 的三个 panel 信息密度不均：左侧 quality estimation 部分的 0.82/0.39 数字含义需要参照正文才能理解，建议在图注中简要说明。
- **§3.2 Soft Jaccard 公式 (Eq. 1)**: 分母使用 max(|y_i|, |y_j|) 而非 min 或 union——这使其更接近 containment similarity 而非 Jaccard。建议在正文中简要说明选择 max 而非 union 的理由。
- **Appendix Z 的 protocol** 很实用，但缺少 failure mode 的决策分支——当 degeneracy > 70% 时建议什么替代方案？

---

## 5. Questions for Authors

**Q1**: 你们考虑过设计更多 per-sample signals 吗（如 per-token LP variance、entity-boundary LP gradient、sample-specific entropy）？如果 4/5 signals 的 selection 失效是 by construction，为何不在实验中包含更多 per-sample alternatives 与 LP 对比？

**Q2**: Cross-dataset analysis (n=23) 的 post-hoc power 是多少？能检测到的最小 ρ 是多少（at 80% power, α=0.05）？

**Q3**: Holm-Bonferroni k=57 中的 57 个检验具体是哪些？Family 边界如何划定？

**Q4**: Entity-wise independence 假设（Proposition 1）在 SciERC 的嵌套实体和 Few-NERD 的 fine-grained types 上，近似程度如何？你们有量化过 entity decisions 之间的依赖强度吗？

**Q5**: Degeneracy bound 的实际恢复率 3-12% 意味着 bound 极松——你们是否尝试过 tighter characterization（如 conditional on α 的 expected gain）？

**Q6**: 如果在 SciERC 上增加到 5+ seeds，+1.02pp 的 entity construction gain 是否有可能达到统计显著？当前 2-3 seeds 的设计是否受限于计算资源？

---

## 6. Missing References

未发现重大遗漏。论文引用了 self-consistency (Wang et al., 2023)、MBR decoding (Eikema and Aziz, 2022; Kumar and Byrne, 2004)、NER calibration (Xia et al., 2025) 等核心文献。可考虑补充：
- Malinin and Gales (2021) 关于 structured prediction 中 predictive uncertainty 的工作（如与 LP compression 的关联）
- Gleave and Irving (2022) 关于 reward model overoptimization 的分析（与 signal alignment bottleneck 的类比）

---

## 7. Overall Assessment

### 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| **Soundness** | 3.5/5 | 诊断框架设计合理，统计处理优秀；但核心 claim（correlation-selection gap）存在 by-construction 成分（N1），cross-dataset null 结论 underpowered（N2），SciERC 核心结果未通过多重检验（W1） |
| **Excitement** | 3/5 | 对 NER test-time scaling 的系统性诊断有价值，entity construction-MBR 联系新颖；但实际方法增益modest（+1-1.4pp），degeneracy bound 太松（W6），叙事 novelty 部分被 by-construction 问题稀释 |
| **Reproducibility** | 4/5 | 超详细 appendix（hyperparameters Table 19, prompt template §I.1, training config），承诺 release code/data；但缺少 total GPU hours 的完整报告（仅说"under 2 hours per config"） |
| **Overall Assessment** | **3.5** (Borderline Conference) | 这是一篇执行质量很高的诊断性工作——统计严谨性在 NLP 论文中属上乘，框架设计系统。但 (1) title claim 的核心发现部分是定义推论而非纯经验发现，(2) 关键 null 结论的统计效力不足，(3) 提出的方法增益modest且在一个主要数据集上不显著。如果作者能在 rebuttal 中 (a) 重构叙事以分离 definitional vs empirical gap，(b) 补充 power analysis，(c) 增加 SciERC seeds，则有望升至 Conference。|
| **Confidence** | 4/5 | 仔细阅读了全文（含全部 28 页 appendix），熟悉 self-consistency、MBR decoding 和 NER 评估方法 |

**一句话总结**: 执行精良的诊断框架，但核心 "correlation-selection gap" 的 4/5 是定义推论而非经验发现，cross-dataset null 结论 underpowered，entity construction 增益 modest 且 SciERC 上未过多重检验校正——Borderline Conference，rebuttal 有机会。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 2593 · 2026-05-20T12:54:34.009759+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,director_post_to_reviewer,dispatch_visual_check,get_external_review_status,get_visual_check_status,read_project_file,request_external_review,submit_review_report_to_research_director,update_review_issues",
  "max_results": "11"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,director_post_to_reviewer,dispatch_visual_check,get_external_review_status,get_visual_check_status,read_project_file,request_external_review,submit_review_report_to_research_director,update_review_issues",
    "max_results": "11"
  }
}
```

</details>

---


### Tool result

_source line 2594 · 2026-05-20T12:54:34.010190+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2595 · 2026-05-20T12:54:34.110703+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 2596 · 2026-05-20T12:54:34.161561+00:00_

1	---
2	name: review-director-session-start
3	description: Review Director session 启动初始化流程——圆桌多轮审稿协议。Review Director 角色 session 启动时自动使用。
4	priority: 9
5	scope: global
6	tags:
7	- workflow
8	- review
9	- session
10	version: 3
11	roles:
12	- review_director
13	---
14	
15	# Review Director Session 启动流程（圆桌会议模式）
16	
17	## 初始化
18	
19	1. `director_get_project_overview(project)` — 了解研究现状（实验状态、最新报告）
20	2. 读取论文文件状态：检查 `projects/{project}/paper/` 或 `main.tex` 是否存在
21	3. 检查是否有来自 Research Director 的论文提交（`[论文提交]` 消息）
22	4. 向用户简要汇报：
23	   - **投稿目标**：venue 和 deadline
24	   - **论文状态**：当前草稿位置和版本
25	   - **资料完整性**：提交的材料是否齐全
26	   - **下一步**：即将开始的圆桌审稿流程
27	
28	## 评审流程（收到论文提交后执行）
29	
30	### Step 0 — 资料检查 + Venue 调研（必须先做，不可跳过）
31	
32	1. 检查提交资料完整性：论文文件是否存在、是否可读、补充材料是否齐全
33	2. 确认目标投稿 venue（从提交消息中获取）
34	3. 用 `web_search` 搜索该 venue 当前轮次的 CFP（Call for Papers），关键词示例：
35	   - `"&lt;venue name> 2026 call for papers" site:aclweb.org`
36	   - `"&lt;venue name> 2026 submission deadline"`
37	   - `"&lt;venue name> 2026 author guidelines"`
38	4. **验证 deadline 未过期**：今天日期与截止日期对比，若已过期立即通知用户，不继续
39	5. 提取当前版本的格式要求：
40	   - 页数限制（正文 / 附录 / 参考文献）
41	   - 模板（ACL / IEEE / NeurIPS / ICML / ...）
42	   - 匿名规则（double-blind / single-blind / open）
43	   - 附录规则（是否允许、是否参与审稿）
44	   - 引用格式（natbib / biblatex / 特定 .bst）
45	6. 将以上信息作为上下文，随任务一起传递给 Reviewer
46	
47	⚠️ 禁止使用训练知识中的 venue 要求——格式标准每年都会更新，必须实时搜索确认。
48	
49	### Step 0.5 — 决定 Reviewer 编排
50	
51	根据 venue 类型和论文特点，决定：
52	- 需要几个 Reviewer（1-5 人）
53	- 每个 Reviewer 的审查侧重
54	
55	参考：
56	- **顶会长文**（NeurIPS/ICML/ACL）：3 人（方法/实验 + novelty/related work + 格式/ethics）
57	- **一般会议**（EMNLP/NAACL）：2 人（方法严谨性 + 新颖性/完整性）
58	- **Workshop / 短文**：1 人（全面审查）
59	
60	向 Group C（即项目配置中的 `feishu.review_chat_id` 审稿群）汇报编排决定。
61	
62	### Step 0.6 — 外部审稿线（与 Step 1 并行）
63	
64	检查项目配置中 `external_review.paperreview_ai.enabled` 是否为 `true`：
65	- 如果启用：调用 `request_external_review(project, paper_pdf_path, venue)` 向用户群发送协助提交卡片
66	- 这一步与 Step 1（内部 Reviewer 分配）**并行执行**，不阻塞内部审稿流程
67	- 外部结果到达后（用户在群里粘贴），纳入 Step 4 最终报告
68	- 如果到 Ste
…[truncated 3286 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2597 · 2026-05-20T12:54:37.723453+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
  "max_results": "11"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
    "max_results": "11"
  }
}
```

</details>

---


### Tool result

_source line 2598 · 2026-05-20T12:54:37.774140+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2599 · 2026-05-20T12:54:42.190291+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool call

_source line 2600 · 2026-05-20T12:54:42.541767+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file,WebSearch",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_project_file,WebSearch",
    "max_results": "2"
  }
}
```

</details>

---


### Tool result

_source line 2601 · 2026-05-20T12:54:42.745404+00:00_

{"result":"# 项目 struct_self_consist_ie 概况\n\n## 实验状态 (190 个)\n\n- **exp_002_ner_conll2003**: DONE (success) — \n- **exp_004_re_diagnostic**: DONE (success) — \n- **exp_005**: DONE (success) — \n- **exp_014_entity_majority_voting**: DONE (success) — \n- **exp_013_exact_match_voting**: DONE (negative) — \n- **exp_012_logprob_baseline**: DONE (success) — \n- **mvp_pilot_005**: DONE (negative) — \n- **e1_component_wise_re_sj**: DONE (negative) — \n- **mvp_pilot_004**: DONE (negative) — \n- **ft_002_v2**: DONE (success) — \n- **mvp_pilot_002**: DONE (failed) — \n- **ft_002**: DONE (killed) — \n- **ft_001**: DONE (success) — \n- **mvp_pilot_003**: DONE (negative) — \n- **mvp_pilot_001**: DONE (negative) — \n\n## 最新报告\n# Handover — 2026-05-20\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| exp_b1_scd_threshold_ablation | Construction threshold sweep for SCD pseudo-label generation on FewNERD: θ∈{1/N, 2/N, 3/N, 0.5}. Higher θ = more conservative pseudo-labels (higher precision, lower recall). Optimal θ balances pseudo-label quality vs quantity for SCD training effectiveness. | — | — | — |\n| exp_b1_scd_fewnerd_curriculum_q | Q variant SCD with curriculum ordering: use B2 entity verifier confidence to stratify pseudo-labels (conf>0.8→Round1, 0.5-0.8→Round2, conf<0.5→discard). Curriculum by verifier confidence improves SCD convergence and final greedy F1 vs standard flat SCD on FewNERD. | — | — | — |\n| exp_b1_scd_fewnerd_standard | Standard Self-Consistency Distillation on FewNERD: fine-tune Qwen3-8B-FT with theta2n construction pseudo-labels (32,565 instances) mixed 1:1 with gold data. Greedy F1 after SCD should approach N=8 construction F1 (0.764 vs current 0.748). Transductive setting: pseudo-labels from test set SC outputs. | — | — | — |\n\n## 待处理\n- exp_b3_prompted_diversity: Structurally diverse prompt templates (role framing, output format variants, few-shot exemplar diversity) increase in
…[truncated 1741 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 555
}
```

</details>

---


### Tool result

_source line 2602 · 2026-05-20T12:54:42.745861+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "elapsed_ms": 204
}
```

</details>

---


### Tool call

_source line 2603 · 2026-05-20T12:58:06.240461+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "struct_self_consist_ie",
  "text": "## 任务：独立审稿 + 交叉回应 Reviewer 1\n\n**论文**: \"Strong Predictors, Weak Selectors: Addressing the Correlation-Selection Gap in Self-Consistency for Named Entity Recognition\"\n**路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex`\n**PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf`\n\n### Venue 信息\n- **Venue**: EMNLP 2026 Long Paper，通过 ARR (May 2026 cycle) 统一审稿\n- **页数限制**: 正文严格 8 页，参考文献不限页数，Limitations/Ethics 不计入页数（不含过多额外内容）\n- **匿名规则**: Double-blind\n- **评分标准**: 5=Consider for Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n### 你的审查侧重：新颖性 + 完整性\n重点评估：\n1. **新颖性**：correlation-selection gap 这一框架对领域的实际贡献，与已有 test-time scaling / self-consistency / MBR decoding 文献的区分度\n2. **完整性**：相关工作覆盖是否充分，实验设计是否覆盖了必要的 baseline 和 ablation，论文叙事逻辑是否完整自洽\n3. **写作质量**：论文结构、可读性、figure/table 的信息传达效率\n4. **格式合规**：是否符合 EMNLP 2026 的 8 页限制、double-blind 匿名要求\n\n### Part 1: 请先完成你的独立审稿\n按标准结构输出：Summary → Strengths → Weaknesses (Must-Fix / Should-Fix) → Questions → Missing References → Overall Assessment（含 Soundness/Excitement/Reproducibility/Overall 评分和 Confidence）\n\n### Part 2: 交叉回应 Reviewer 1\n以下是 Reviewer 1（方法严谨性 + 实验设计 + 统计分析）的完整审稿意见。请逐条回应其 Weaknesses 和 Questions，标注 [AGREE] 或 [REBUT]，并提供你自己的判断依据（cite 具体 Section/Table/Figure）。\n\n---\n\n# Reviewer 1 审稿意见（完整原文）\n\n## 1. Summary\n\n本文研究自一致性（self-consistency）在 NER 等结构化预测任务中的失效机制。作者提出一个包含五种置信度信号的诊断框架，发现所有信号均能可靠估计生成质量（ρ up to 0.45, AUROC up to 0.82），但无法有效执行 sample selection——即\"correlation-selection gap\"。论文将失效归因于三种结构性故障模式（instance degeneracy、isolated headroom、LP compression），提出 entity-level construction（形式化为 MBR decoding）部分弥合该差距，并给出退化分解的理论上界。\n\n## 2. Strengths\n\n**S1. 系统且原创的诊断框架。** 将 test-time scaling 问题分解为 quality estimation vs. sample selection 两个正交维度，是对该领域的结构性贡献。五种信号跨四个 NER 基准的全面评估（Table 3, Figure 6 heatmaps）提供了比现有文献更细粒度的理解。\n\n**S2. 统计处理水准显著高于同类工作。** Bootstrap CI（Table 13）、Holm-Bonferroni 多重检验校正（k=57）、paired bootstrap 对比、TOST 等价性检验（Table 16, Appendix F）、permutation tests（Table 9）——在 NLP 论文中罕见地系统。效果量和 p 值的报告（包括不显著结果如 SciERC p_adj=0.20）是诚实的学术实践。\n\n**S3. Entity construction 与 MBR 的理论联系。** Proposition 1（§6.1）将 entity-level majority vote 形式化为 MBR decoding with balanced set-overlaps，提供了清晰的决策论基础。这不仅解释了方法为何有效，也指出了适用边界。\n\n**S4. 极其详尽的 appendix。** 28 页补充材料覆盖了 robustness（N-scaling, temperature, seed stability）、controlled ablations（§7.4）、per-entity-type analysis（Appendix W）、free-form decoding ablation（Appendix O）、cross-dataset OOD（Appendix S）等，几乎预见了所有可能的审稿疑问。\n\n**S5. 实用的诊断协议。** §Z 的三步协议（measure degeneracy → assess signal-quality alignment → evaluate aggregation）为从业者提供了可直接使用的框架，超越了纯分析论文的范畴。\n\n## 3. Weaknesses\n\n### Must-Fix 问题（影响接收决定）\n\n**N1 [critical] \"Correlation-selection gap\" 的核心发现存在 by-construction 成分**\n\n- **具体位置**: §4 第一段, Abstract, §1\n- **问题**: 论文的五种信号中，四种（SJ, VC, FK, EM）是 instance-level 的——§4 开头明确承认\"Four of five signals assign identical scores to all candidates from the same input by construction\"。这意味着这四种信号在设计上就不可能进行 per-sample selection，correlation-selection gap 对它们而言是**定义性推论**而非经验发现。唯一具备 per-sample discrimination 能力的 LP 确实展现了部分 selection 能力（Few-NERD +1.30pp, p<0.01），但被 compression 限制。论文将五种信号的 gap 统一呈现为一个\"surprising empirical finding\"，夸大了发现的经验性成分。\n- **为什么影响接收**: 这是论文的 title claim 和核心叙事。如果 4/5 的 gap 是 by construction，则论文的 empirical contribution 实质上缩小为\"LP 的 selection 能力受 compression 限制\"，叙事力度显著减弱。\n- **建议修改方向**: (1) 在 §4 开头明确区分 definitional gap（instance-level signals）和 empirical gap（LP），给两类 gap 不同的权重；(2) 重写 abstract/intro 的叙事框架，将 LP 的 compression-limited selection 作为核心经验发现，而非将所有五种信号的 gap 等权呈现；(3) 讨论为何不设计更多 per-sample signals（如 per-sample entropy、token-level LP variance 等）。\n\n**N2 [critical] Cross-dataset 分析（ρ=0.052, p=0.81, n=23）严重 underpowered，但被用于支持 null 结论**\n\n- **具体位置**: §7.3 (\"degeneracy alone does not predict LP gain\"), Figure 3, 正文 p.6\n- **问题**: 23 个 configurations 的 cross-dataset 相关分析被用于得出\"degeneracy does not predict LP gain\"（ρ=0.052, p=0.81）。但 n=23 的 statistical power 极低：检测 ρ=0.3 at α=0.05, 80% power 需要 n≈85；检测 ρ=0.4 也需要 n≈47。当前样本量的 power 仅约 50%（for ρ=0.4），无法可靠地拒绝中等效应量的备择假设。论文将 p=0.81 解读为\"degeneracy does not predict\"，但这可能仅仅是 underpowered。\n- **为什么影响接收**: 这一 null 结论直接支撑了论文的核心论点之一——degeneracy 是 dataset-intrinsic 的而非 predictive 的。如果该结论不可靠，§6.3 degeneracy decomposition 的 practical relevance 会受质疑。\n- **建议修改方向**: (1) 报告 post-hoc power analysis，明确当前样本量可检测的最小效应量；(2) 将结论措辞从 \"does not predict\" 改为 \"we did not find evidence for prediction, but the analysis is underpowered (n=23)\"；(3) 如有可能，增加更多 configurations（更多 model sizes、temperatures、N 值）以提高统计效力。\n\n### Should-Fix 问题（影响评分但不一票否决）\n\n**W1 [warning] SciERC entity construction 增益（+1.02pp）未通过多重检验校正**\n\n- **具体位置**: §7.5, Table 6, p.8\n- **问题**: Few-NERD 上的 +1.40pp 通过了 Holm-Bonferroni (k=57)，但 SciERC 上的 +1.02pp 校正后 p_adj=0.20，**不显著**。论文在正文中的呈现方式（\"LP-weighted entity construction yields ... +1.02pp on SciERC\"）容易让读者忽略这一不显著性。两个数据集是论文的主要实验平台，其中一个的核心结果不显著，这对方法的 generalizability 是实质性打击。\n- **建议**: 在正文中更显著地标注 SciERC p_adj=0.20（不仅在括号内），讨论为何 SciERC 不显著（样本量？degeneracy 程度？），以及这对方法适用范围的含义。\n\n**W2 [warning] Holm-Bonferroni k=57 的 family 定义不透明**\n\n- **具体位置**: §7.5, p.8\n- **问题**: 论文使用 k=57 进行 Holm-Bonferroni 校正，但从未明确解释这 57 个假设检验的具体构成。是所有 pairwise signal comparisons × datasets？所有论文中的统计检验？还是 entity construction 相关的所有对比？Family 定义直接影响校正严格程度，对读者评估结果可靠性至关重要。\n- **建议**: 在 appendix 中列出 57 个检验的明细（或至少给出构成规则），并讨论 family 定义的选择是否保守/宽松。\n\n**W3 [warning] 72B zero-shot vs 8B fine-tuned 比较同时变化了三个因素**\n\n- **具体位置**: Table 2 (p.6), §6.2, Limitations (p.8)\n- **问题**: 72B zero-shot 与 8B fine-tuned 的对比同时改变了 model scale、training regime（zero-shot vs. fine-tuned）、和 quantization。论文在 Limitations 中坦承 \"individual effects cannot be disentangled\"，但在 §6.2 Scaling Behavior 中仍从该对比中得出关于 scaling 的结论（\"the gap persists at 72B\"）。\n- **建议**: (1) §6.2 的 conclusions 应更加审慎，明确标注 confounded comparison；(2) 如有可能，加入 72B fine-tuned 或 8B zero-shot 的对比点以分离因素。\n\n**W4 [warning] 关键实验的 seed 数量偏少（2-3 seeds）**\n\n- **具体位置**: Table 1 (2-seed mean for SciERC), Table 3 (3 seeds), Appendix H (Table 18)\n- **问题**: 主要 QE 结果（Table 3）使用 primary seed=42 + 3 seeds 报告 σ=0.012。SciERC LP selection（Table 1）仅 2-seed mean。Appendix H Table 18 的 multi-seed stability 分析使用 3 seeds。考虑到 few-shot NER 的高方差（论文自身报告 Few-NERD VC σ=0.48pp），3 seeds 的统计效力有限。特别是 SciERC 样本量只有 n=529，seed 间的方差可能被低估。\n- **建议**: (1) 讨论为何 3 seeds 足够（或坦承不够）；(2) 对核心结论，报告 3-seed results 是否改变任何 directional finding。\n\n**W5 [warning] Proposition 1 的 \"entity-wise independence\" 假设未经验证**\n\n- **具体位置**: §6.1, Appendix N.1\n- **问题**: Proposition 1 将 entity construction 形式化为 MBR，但核心假设是 entity-wise independence——每个 entity candidate 的 inclusion decision 独立于其他 entities。在实际 NER 中，entities 之间存在强依赖（嵌套实体、句法约束、同一 span 的竞争标注）。论文未提供经验证据验证该假设在实际数据上的近似程度。\n- **建议**: (1) 在 SciERC/Few-NERD 上测量 entity decisions 之间的 conditional dependence（如计算 entity co-occurrence 的互信息）；(2) 或至少讨论该假设的违反对结论的影响方向和程度。\n\n**W6 [warning] Degeneracy bound 极度松弛，实际恢复率仅 3-12%**\n\n- **具体位置**: §6.3, Figure 9 (p.27), Appendix N.3\n- **问题**: 退化分解上界 E[ΔF₁] ≤ (1−D)·G_nd 在所有 16 个 positive-gain configurations 中，实际 SC gain 仅占上界的 3-12%（论文 p.6: \"the bound is loose because α — signal alignment — is the bottleneck\"）。这意味着该 bound 的预测能力极弱——知道上界几乎不能帮助判断 SC 是否有效。\n- **建议**: 讨论 bound 的 tightening 方向（能否引入 α 的 empirical estimate 使 bound 更 informative？），以及在 bound 如此松弛的情况下，decomposition 的实际价值体现在哪里（diagnostic insight vs. predictive power）。\n\n## 4. 小问题（不影响接收）\n\n- **Table 2 中 \"n/a\" 和 \"†\" 标记的说明分散在 caption 和 footnotes 中**，建议统一到 caption 底部，减少读者认知负担。\n- **Figure 1** 的三个 panel 信息密度不均：左侧 quality estimation 部分的 0.82/0.39 数字含义需要参照正文才能理解，建议在图注中简要说明。\n- **§3.2 Soft Jaccard 公式 (Eq. 1)**: 分母使用 max(|y_i|, |y_j|) 而非 min 或 union——这使其更接近 containment similarity 而非 Jaccard。建议在正文中简要说明选择 max 而非 union 的理由。\n- **Appendix Z 的 protocol** 很实用，但缺少 failure mode 的决策分支——当 degeneracy > 70% 时建议什么替代方案？\n\n## 5. Questions for Authors\n\n**Q1**: 你们考虑过设计更多 per-sample signals 吗（如 per-token LP variance、entity-boundary LP gradient、sample-specific entropy）？如果 4/5 signals 的 selection 失效是 by construction，为何不在实验中包含更多 per-sample alternatives 与 LP 对比？\n\n**Q2**: Cross-dataset analysis (n=23) 的 post-hoc power 是多少？能检测到的最小 ρ 是多少（at 80% power, α=0.05）？\n\n**Q3**: Holm-Bonferroni k=57 中的 57 个检验具体是哪些？Family 边界如何划定？\n\n**Q4**: Entity-wise independence 假设（Proposition 1）在 SciERC 的嵌套实体和 Few-NERD 的 fine-grained types 上，近似程度如何？你们有量化过 entity decisions 之间的依赖强度吗？\n\n**Q5**: Degeneracy bound 的实际恢复率 3-12% 意味着 bound 极松——你们是否尝试过 tighter characterization（如 conditional on α 的 expected gain）？\n\n**Q6**: 如果在 SciERC 上增加到 5+ seeds，+1.02pp 的 entity construction gain 是否有可能达到统计显著？当前 2-3 seeds 的设计是否受限于计算资源？\n\n## 6. Missing References\n\n未发现重大遗漏。论文引用了 self-consistency (Wang et al., 2023)、MBR decoding (Eikema and Aziz, 2022; Kumar and Byrne, 2004)、NER calibration (Xia et al., 2025) 等核心文献。可考虑补充：\n- Malinin and Gales (2021) 关于 structured prediction 中 predictive uncertainty 的工作（如与 LP compression 的关联）\n- Gleave and Irving (2022) 关于 reward model overoptimization 的分析（与 signal alignment bottleneck 的类比）\n\n## 7. Overall Assessment\n\n### 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| **Soundness** | 3.5/5 | 诊断框架设计合理，统计处理优秀；但核心 claim（correlation-selection gap）存在 by-construction 成分（N1），cross-dataset null 结论 underpowered（N2），SciERC 核心结果未通过多重检验（W1） |\n| **Excitement** | 3/5 | 对 NER test-time scaling 的系统性诊断有价值，entity construction-MBR 联系新颖；但实际方法增益modest（+1-1.4pp），degeneracy bound 太松（W6），叙事 novelty 部分被 by-construction 问题稀释 |\n| **Reproducibility** | 4/5 | 超详细 appendix（hyperparameters Table 19, prompt template §I.1, training config），承诺 release code/data；但缺少 total GPU hours 的完整报告（仅说\"under 2 hours per config\"） |\n| **Overall Assessment** | **3.5** (Borderline Conference) | 这是一篇执行质量很高的诊断性工作——统计严谨性在 NLP 论文中属上乘，框架设计系统。但 (1) title claim 的核心发现部分是定义推论而非纯经验发现，(2) 关键 null 结论的统计效力不足，(3) 提出的方法增益modest且在一个主要数据集上不显著。如果作者能在 rebuttal 中 (a) 重构叙事以分离 definitional vs empirical gap，(b) 补充 power analysis，(c) 增加 SciERC seeds，则有望升至 Conference。|\n| **Confidence** | 4/5 | 仔细阅读了全文（含全部 28 页 appendix），熟悉 self-consistency、MBR decoding 和 NER 评估方法 |\n\n**一句话总结**: 执行精良的诊断框架，但核心 \"correlation-selection gap\" 的 4/5 是定义推论而非经验发现，cross-dataset null 结论 underpowered，entity construction 增益 modest 且 SciERC 上未过多重检验校正——Borderline Conference，rebuttal 有机会。\n\n---\n\n请完成以上两部分后统一提交。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "struct_self_consist_ie",
    "text": "## 任务：独立审稿 + 交叉回应 Reviewer 1\n\n**论文**: \"Strong Predictors, Weak Selectors: Addressing the Correlation-Selection Gap in Self-Consistency for Named Entity Recognition\"\n**路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex`\n**PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf`\n\n### Venue 信息\n- **Venue**: EMNLP 2026 Long Paper，通过 ARR (May 2026 cycle) 统一审稿\n- **页数限制**: 正文严格 8 页，参考文献不限页数，Limitations/Ethics 不计入页数（不含过多额外内容）\n- **匿名规则**: Double-blind\n- **评分标准**: 5=Consider for Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n### 你的审查侧重：新颖性 + 完整性\n重点评估：\n1. **新颖性**：correlation-selection gap 这一框架对领域的实际贡献，与已有 test-time scaling / self-consistency / MBR decoding 文献的区分度\n2. **完整性**：相关工作覆盖是否充分，实验设计是否覆盖了必要的 baseline 和 ablation，论文叙事逻辑是否完整自洽\n3. **写作质量**：论文结构、可读性、figure/table 的信息传达效率\n4. **格式合规**：是否符合 EMNLP 2026 的 8 页限制、double-blind 匿名要求\n\n### Part 1: 请先完成你的独立审稿\n按标准结构输出：Summary → Strengths → Weaknesses (Must-Fix / Should-Fix) → Questions → Missing References → Overall Assessment（含 Soundness/Excitement/Reproducibility/Overall 评分和 Confidence）\n\n### Part 2: 交叉回应 Reviewer 1\n以下是 Reviewer 1（方法严谨性 + 实验设计 + 统计分析）的完整审稿意见。请逐条回应其 Weaknesses 和 Questions，标注 [AGREE] 或 [REBUT]，并提供你自己的判断依据（cite 具体 Section/Table/Figure）。\n\n---\n\n# Reviewer 1 审稿意见（完整原文）\n\n## 1. Summary\n\n本文研究自一致性（self-consistency）在 NER 等结构化预测任务中的失效机制。作者提出一个包含五种置信度信号的诊断框架，发现所有信号均能可靠估计生成质量（ρ up to 0.45, AUROC up to 0.82），但无法有效执行 sample selection——即\"correlation-selection gap\"。论文将失效归因于三种结构性故障模式（instance degeneracy、isolated headroom、LP compression），提出 entity-level construction（形式化为 MBR decoding）部分弥合该差距，并给出退化分解的理论上界。\n\n## 2. Strengths\n\n**S1. 系统且原创的诊断框架。** 将 test-time scaling 问题分解为 quality estimation vs. sample selection 两个正交维度，是对该领域的结构性贡献。五种信号跨四个 NER 基准的全面评估（Table 3, Figure 6 heatmaps）提供了比现有文献更细粒度的理解。\n\n**S2. 统计处理水准显著高于同类工作。** Bootstrap CI（Table 13）、Holm-Bonferroni 多重检验校正（k=57）、paired bootstrap 对比、TOST 等价性检验（Table 16, Appendix F）、permutation tests（Table 9）——在 NLP 论文中罕见地系统。效果量和 p 值的报告（包括不显著结果如 SciERC p_adj=0.20）是诚实的学术实践。\n\n**S3. Entity construction 与 MBR 的理论联系。** Proposition 1（§6.1）将 entity-level majority vote 形式化为 MBR decoding with balanced set-overlaps，提供了清晰的决策论基础。这不仅解释了方法为何有效，也指出了适用边界。\n\n**S4. 极其详尽的 appendix。** 28 页补充材料覆盖了 robustness（N-scaling, temperature, seed stability）、controlled ablations（§7.4）、per-entity-type analysis（Appendix W）、free-form decoding ablation（Appendix O）、cross-dataset OOD（Appendix S）等，几乎预见了所有可能的审稿疑问。\n\n**S5. 实用的诊断协议。** §Z 的三步协议（measure degeneracy → assess signal-quality alignment → evaluate aggregation）为从业者提供了可直接使用的框架，超越了纯分析论文的范畴。\n\n## 3. Weaknesses\n\n### Must-Fix 问题（影响接收决定）\n\n**N1 [critical] \"Correlation-selection gap\" 的核心发现存在 by-construction 成分**\n\n- **具体位置**: §4 第一段, Abstract, §1\n- **问题**: 论文的五种信号中，四种（SJ, VC, FK, EM）是 instance-level 的——§4 开头明确承认\"Four of five signals assign identical scores to all candidates from the same input by construction\"。这意味着这四种信号在设计上就不可能进行 per-sample selection，correlation-selection gap 对它们而言是**定义性推论**而非经验发现。唯一具备 per-sample discrimination 能力的 LP 确实展现了部分 selection 能力（Few-NERD +1.30pp, p<0.01），但被 compression 限制。论文将五种信号的 gap 统一呈现为一个\"surprising empirical finding\"，夸大了发现的经验性成分。\n- **为什么影响接收**: 这是论文的 title claim 和核心叙事。如果 4/5 的 gap 是 by construction，则论文的 empirical contribution 实质上缩小为\"LP 的 selection 能力受 compression 限制\"，叙事力度显著减弱。\n- **建议修改方向**: (1) 在 §4 开头明确区分 definitional gap（instance-level signals）和 empirical gap（LP），给两类 gap 不同的权重；(2) 重写 abstract/intro 的叙事框架，将 LP 的 compression-limited selection 作为核心经验发现，而非将所有五种信号的 gap 等权呈现；(3) 讨论为何不设计更多 per-sample signals（如 per-sample entropy、token-level LP variance 等）。\n\n**N2 [critical] Cross-dataset 分析（ρ=0.052, p=0.81, n=23）严重 underpowered，但被用于支持 null 结论**\n\n- **具体位置**: §7.3 (\"degeneracy alone does not predict LP gain\"), Figure 3, 正文 p.6\n- **问题**: 23 个 configurations 的 cross-dataset 相关分析被用于得出\"degeneracy does not predict LP gain\"（ρ=0.052, p=0.81）。但 n=23 的 statistical power 极低：检测 ρ=0.3 at α=0.05, 80% power 需要 n≈85；检测 ρ=0.4 也需要 n≈47。当前样本量的 power 仅约 50%（for ρ=0.4），无法可靠地拒绝中等效应量的备择假设。论文将 p=0.81 解读为\"degeneracy does not predict\"，但这可能仅仅是 underpowered。\n- **为什么影响接收**: 这一 null 结论直接支撑了论文的核心论点之一——degeneracy 是 dataset-intrinsic 的而非 predictive 的。如果该结论不可靠，§6.3 degeneracy decomposition 的 practical relevance 会受质疑。\n- **建议修改方向**: (1) 报告 post-hoc power analysis，明确当前样本量可检测的最小效应量；(2) 将结论措辞从 \"does not predict\" 改为 \"we did not find evidence for prediction, but the analysis is underpowered (n=23)\"；(3) 如有可能，增加更多 configurations（更多 model sizes、temperatures、N 值）以提高统计效力。\n\n### Should-Fix 问题（影响评分但不一票否决）\n\n**W1 [warning] SciERC entity construction 增益（+1.02pp）未通过多重检验校正**\n\n- **具体位置**: §7.5, Table 6, p.8\n- **问题**: Few-NERD 上的 +1.40pp 通过了 Holm-Bonferroni (k=57)，但 SciERC 上的 +1.02pp 校正后 p_adj=0.20，**不显著**。论文在正文中的呈现方式（\"LP-weighted entity construction yields ... +1.02pp on SciERC\"）容易让读者忽略这一不显著性。两个数据集是论文的主要实验平台，其中一个的核心结果不显著，这对方法的 generalizability 是实质性打击。\n- **建议**: 在正文中更显著地标注 SciERC p_adj=0.20（不仅在括号内），讨论为何 SciERC 不显著（样本量？degeneracy 程度？），以及这对方法适用范围的含义。\n\n**W2 [warning] Holm-Bonferroni k=57 的 family 定义不透明**\n\n- **具体位置**: §7.5, p.8\n- **问题**: 论文使用 k=57 进行 Holm-Bonferroni 校正，但从未明确解释这 57 个假设检验的具体构成。是所有 pairwise signal comparisons × datasets？所有论文中的统计检验？还是 entity construction 相关的所有对比？Family 定义直接影响校正严格程度，对读者评估结果可靠性至关重要。\n- **建议**: 在 appendix 中列出 57 个检验的明细（或至少给出构成规则），并讨论 family 定义的选择是否保守/宽松。\n\n**W3 [warning] 72B zero-shot vs 8B fine-tuned 比较同时变化了三个因素**\n\n- **具体位置**: Table 2 (p.6), §6.2, Limitations (p.8)\n- **问题**: 72B zero-shot 与 8B fine-tuned 的对比同时改变了 model scale、training regime（zero-shot vs. fine-tuned）、和 quantization。论文在 Limitations 中坦承 \"individual effects cannot be disentangled\"，但在 §6.2 Scaling Behavior 中仍从该对比中得出关于 scaling 的结论（\"the gap persists at 72B\"）。\n- **建议**: (1) §6.2 的 conclusions 应更加审慎，明确标注 confounded comparison；(2) 如有可能，加入 72B fine-tuned 或 8B zero-shot 的对比点以分离因素。\n\n**W4 [warning] 关键实验的 seed 数量偏少（2-3 seeds）**\n\n- **具体位置**: Table 1 (2-seed mean for SciERC), Table 3 (3 seeds), Appendix H (Table 18)\n- **问题**: 主要 QE 结果（Table 3）使用 primary seed=42 + 3 seeds 报告 σ=0.012。SciERC LP selection（Table 1）仅 2-seed mean。Appendix H Table 18 的 multi-seed stability 分析使用 3 seeds。考虑到 few-shot NER 的高方差（论文自身报告 Few-NERD VC σ=0.48pp），3 seeds 的统计效力有限。特别是 SciERC 样本量只有 n=529，seed 间的方差可能被低估。\n- **建议**: (1) 讨论为何 3 seeds 足够（或坦承不够）；(2) 对核心结论，报告 3-seed results 是否改变任何 directional finding。\n\n**W5 [warning] Proposition 1 的 \"entity-wise independence\" 假设未经验证**\n\n- **具体位置**: §6.1, Appendix N.1\n- **问题**: Proposition 1 将 entity construction 形式化为 MBR，但核心假设是 entity-wise independence——每个 entity candidate 的 inclusion decision 独立于其他 entities。在实际 NER 中，entities 之间存在强依赖（嵌套实体、句法约束、同一 span 的竞争标注）。论文未提供经验证据验证该假设在实际数据上的近似程度。\n- **建议**: (1) 在 SciERC/Few-NERD 上测量 entity decisions 之间的 conditional dependence（如计算 entity co-occurrence 的互信息）；(2) 或至少讨论该假设的违反对结论的影响方向和程度。\n\n**W6 [warning] Degeneracy bound 极度松弛，实际恢复率仅 3-12%**\n\n- **具体位置**: §6.3, Figure 9 (p.27), Appendix N.3\n- **问题**: 退化分解上界 E[ΔF₁] ≤ (1−D)·G_nd 在所有 16 个 positive-gain configurations 中，实际 SC gain 仅占上界的 3-12%（论文 p.6: \"the bound is loose because α — signal alignment — is the bottleneck\"）。这意味着该 bound 的预测能力极弱——知道上界几乎不能帮助判断 SC 是否有效。\n- **建议**: 讨论 bound 的 tightening 方向（能否引入 α 的 empirical estimate 使 bound 更 informative？），以及在 bound 如此松弛的情况下，decomposition 的实际价值体现在哪里（diagnostic insight vs. predictive power）。\n\n## 4. 小问题（不影响接收）\n\n- **Table 2 中 \"n/a\" 和 \"†\" 标记的说明分散在 caption 和 footnotes 中**，建议统一到 caption 底部，减少读者认知负担。\n- **Figure 1** 的三个 panel 信息密度不均：左侧 quality estimation 部分的 0.82/0.39 数字含义需要参照正文才能理解，建议在图注中简要说明。\n- **§3.2 Soft Jaccard 公式 (Eq. 1)**: 分母使用 max(|y_i|, |y_j|) 而非 min 或 union——这使其更接近 containment similarity 而非 Jaccard。建议在正文中简要说明选择 max 而非 union 的理由。\n- **Appendix Z 的 protocol** 很实用，但缺少 failure mode 的决策分支——当 degeneracy > 70% 时建议什么替代方案？\n\n## 5. Questions for Authors\n\n**Q1**: 你们考虑过设计更多 per-sample signals 吗（如 per-token LP variance、entity-boundary LP gradient、sample-specific entropy）？如果 4/5 signals 的 selection 失效是 by construction，为何不在实验中包含更多 per-sample alternatives 与 LP 对比？\n\n**Q2**: Cross-dataset analysis (n=23) 的 post-hoc power 是多少？能检测到的最小 ρ 是多少（at 80% power, α=0.05）？\n\n**Q3**: Holm-Bonferroni k=57 中的 57 个检验具体是哪些？Family 边界如何划定？\n\n**Q4**: Entity-wise independence 假设（Proposition 1）在 SciERC 的嵌套实体和 Few-NERD 的 fine-grained types 上，近似程度如何？你们有量化过 entity decisions 之间的依赖强度吗？\n\n**Q5**: Degeneracy bound 的实际恢复率 3-12% 意味着 bound 极松——你们是否尝试过 tighter characterization（如 conditional on α 的 expected gain）？\n\n**Q6**: 如果在 SciERC 上增加到 5+ seeds，+1.02pp 的 entity construction gain 是否有可能达到统计显著？当前 2-3 seeds 的设计是否受限于计算资源？\n\n## 6. Missing References\n\n未发现重大遗漏。论文引用了 self-consistency (Wang et al., 2023)、MBR decoding (Eikema and Aziz, 2022; Kumar and Byrne, 2004)、NER calibration (Xia et al., 2025) 等核心文献。可考虑补充：\n- Malinin and Gales (2021) 关于 structured prediction 中 predictive uncertainty 的工作（如与 LP compression 的关联）\n- Gleave and Irving (2022) 关于 reward model overoptimization 的分析（与 signal alignment bottleneck 的类比）\n\n## 7. Overall Assessment\n\n### 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| **Soundness** | 3.5/5 | 诊断框架设计合理，统计处理优秀；但核心 claim（correlation-selection gap）存在 by-construction 成分（N1），cross-dataset null 结论 underpowered（N2），SciERC 核心结果未通过多重检验（W1） |\n| **Excitement** | 3/5 | 对 NER test-time scaling 的系统性诊断有价值，entity construction-MBR 联系新颖；但实际方法增益modest（+1-1.4pp），degeneracy bound 太松（W6），叙事 novelty 部分被 by-construction 问题稀释 |\n| **Reproducibility** | 4/5 | 超详细 appendix（hyperparameters Table 19, prompt template §I.1, training config），承诺 release code/data；但缺少 total GPU hours 的完整报告（仅说\"under 2 hours per config\"） |\n| **Overall Assessment** | **3.5** (Borderline Conference) | 这是一篇执行质量很高的诊断性工作——统计严谨性在 NLP 论文中属上乘，框架设计系统。但 (1) title claim 的核心发现部分是定义推论而非纯经验发现，(2) 关键 null 结论的统计效力不足，(3) 提出的方法增益modest且在一个主要数据集上不显著。如果作者能在 rebuttal 中 (a) 重构叙事以分离 definitional vs empirical gap，(b) 补充 power analysis，(c) 增加 SciERC seeds，则有望升至 Conference。|\n| **Confidence** | 4/5 | 仔细阅读了全文（含全部 28 页 appendix），熟悉 self-consistency、MBR decoding 和 NER 评估方法 |\n\n**一句话总结**: 执行精良的诊断框架，但核心 \"correlation-selection gap\" 的 4/5 是定义推论而非经验发现，cross-dataset null 结论 underpowered，entity construction 增益 modest 且 SciERC 上未过多重检验校正——Borderline Conference，rebuttal 有机会。\n\n---\n\n请完成以上两部分后统一提交。"
  }
}
```

</details>

---


### Tool result

_source line 2604 · 2026-05-20T12:58:10.312443+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 4071
}
```

</details>

---


### Tool call

_source line 2605 · 2026-05-20T12:58:17.685439+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 2606 · 2026-05-20T12:58:17.686251+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2607 · 2026-05-20T12:58:17.686494+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 2608 · 2026-05-20T12:58:17.737040+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-20T12:47:27.106227+00:00\", \"completed_at\": \"2026-05-20T12:50:52.542978+00:00\", \"findings\": [{\"severity\": \"critical\", \"dimension\": \"page 31\", \"message\": \"Figure 10 是文字占位符，未渲染实际图表。显示 \\\"[Figure placeholder: Oracle F1 (N) scaling curves] / 6 curves (Qwen3-8B + LLaMA-3.1-8B × SciERC / FewNERD / CoNLL) + greedy horizontal lines = power-law fit / stable across pending. / 14B/32B curves pending.\\\"。审稿人会立即判断论文未完成。\"}, {\"severity\": \"warning\", \"dimension\": \"page 1-2\", \"message\": \"连续 2 页纯文本（Abstract + Introduction + Background），无任何 display item。第一个视觉锚点（Figure 1）直到第 3 页顶部才出现。对 8 页主体论文而言，前 25% 无视觉支撑，审稿人第一印象偏\\\"文字墙\\\"。\"}, {\"severity\": \"warning\", \"dimension\": \"page 5\", \"message\": \"又一个纯文本页（Section 5 Adaptive Methods + Section 6 Theory & Scaling Law），与前面 p1-2 形成\\\"纯文字-图表密集-纯文字\\\"的不均匀节奏。\"}, {\"severity\": \"warning\", \"dimension\": \"page 7\", \"message\": \"页面过度拥挤：Tables 3, 4, 5 + Figure 3 同时堆叠在一页。Figure 3（Instance degeneracy 图）被挤压得很小，细节难以辨认。与 page 5 的空旷形成强烈反差。\"}, {\"severity\": \"warning\", \"dimension\": \"page 7\", \"message\": \"Figure 3 尺寸过小，坐标轴标签和图例在当前大小下接近可读性下限。建议单独给更多空间或移至附录扩大尺寸。\"}, {\"severity\": \"info\", \"dimension\": \"page 3\", \"message\": \"Figure 1（Overview 概念图）作为首个 display item 整体有效传达核心概念（correlation-selection gap），但面板内注释文字偏小（约 6-7pt），三个面板水平排列后单个面板宽度有限。Caption 自包含性好。\"}, {\"severity\": \"info\", \"dimension\": \"page 4\", \"message\": \"Figure 2 柱状图颜色区分度好（蓝/绿/灰），legend 可读。Table 1 使用 booktabs 风格，最优值加粗，格式规范。\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"主体末页（第 8 页）内容充实（Table 6 + Discussion + Conclusion + Limitations），空间利用率 >90%，无异常空白。\"}, {\"severity\": \"info\", \"dimension\": \"page 18\", \"message\": \"Figure 6 热力图使用绿-黄-红渐变色阶，红绿对比对色盲读者不友好。建议改用蓝-白-红或 viridis 色阶。\"}, {\"severity\": \"info\", \"dimension\": \"page 18\", \"message\": \"Figure 7（scatter plot）尺寸偏小，点标签拥挤。作为附录图可接受，但若移入主体需放大。\"}, {\"severity\"
…[truncated 652 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2609 · 2026-05-20T12:58:30.631353+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "struct_self_consist_ie",
  "file": "config.yaml",
  "max_chars": "5000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "struct_self_consist_ie",
    "file": "config.yaml",
    "max_chars": "5000"
  }
}
```

</details>

---


### Tool result

_source line 2610 · 2026-05-20T12:58:30.731942+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'mistakes.yaml', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'config.yaml'\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 2611 · 2026-05-20T12:58:34.412457+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/struct_self_consist_ie/**/config*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/struct_self_consist_ie/**/config*.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects"
  }
}
```

</details>

---


### Tool result

_source line 2612 · 2026-05-20T12:58:34.563268+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 2613 · 2026-05-20T12:58:37.977286+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review|paperreview_ai",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "output_mode": "content",
  "head_limit": "20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review|paperreview_ai",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
    "output_mode": "content",
    "head_limit": "20"
  }
}
```

</details>

---


### Tool result

_source line 2614 · 2026-05-20T12:58:38.280851+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_14.md:185:外部审稿：未启用（项目配置中 `external_review.paperreview_ai.enabled` 未设置）。
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_3.md:163:外部审稿：未启用（项目配置中 `external_review.paperreview_ai.enabled` 未设置）
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_23.md:149:外部审稿：未启用（项目配置中 `external_review.paperreview_ai.enabled` 未设置）。
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_10.md:166:项目未配置 paperreview.ai 外部审稿（external_review.paperreview_ai.enabled 未启用）。外部审稿：未请求。
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_2.md:156:外部审稿：未配置（项目未启用 `external_review.paperreview_ai.enabled`）。
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_21.md:165:外部审稿：未启用（项目配置中 `external_review.paperreview_ai.enabled` 未设置）。
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_7.md:138:External review not configured (paperreview_ai.enabled not set). Status: not_requested.
AGENTS.md:82:如果项目配置了外部审稿（`external_review.paperreview_ai.enabled: true`）：
AGENTS.md:83:- 在分配内部 Reviewer 的同时，调用 `request_external_review()` 向用户群发送协助卡片
AGENTS.md:87:- 如果内部审稿结束时外部结果仍未返回，用 `get_external_review_status()` 检查状态，在报告中标注「外部审稿：未返回」
AGENTS.md:162:`director_get_project_overview`, `director_post_to_reviewer`, `dispatch_visual_check`, `get_external_review_status`, `get_visual_check_status`, `read_local_file`, `read_project_file`, `request_external_review`, `request_study_approval`, `submit_review_report_to_research_director`, `update_review_issues`
CLAUDE.md:82:如果项目配置了外部审稿（`external_review.paperreview_ai.enabled: true`）：
CLAUDE.md:83:- 在分配内部 Reviewer 的同时，调用 `request_extern
…[truncated 1539 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Grep",
  "elapsed_ms": 303
}
```

</details>

---


### Assistant

_source line 2615 · 2026-05-20T12:58:53.850921+00:00_

外部审稿未启用（历史一致），跳过。当前状态汇报：

---

**圆桌审稿 Round 1 — 进度更新**

| 线程 | 状态 |
|------|------|
| Reviewer 1（方法严谨性） | ✅ 初审完成 — Overall 3.5 (Borderline Conference) |
| Reviewer 2（新颖性/完整性） | 🔄 已派发，含 R1 完整意见供交叉回应 |
| 外部审稿 | ⏭️ 未启用 |
| 视觉审查 | ✅ 已完成 — 1 critical / 4 warning / 9 info |

**视觉审查关键发现**：
- **[Critical]** p.31 Figure 10 仍为文字占位符，未渲染实际图表——审稿人会判定论文未完成
- **[Warning]** p.1-2 连续纯文本无 display item，首个视觉锚点（Figure 1）在 p.3 才出现
- **[Warning]** p.7 过度拥挤（Tables 3/4/5 + Figure 3 堆叠），Figure 3 被挤压至可读性下限
- **[Warning]** p.5 又一纯文本页，与 p.7 形成不均匀节奏

等待 Reviewer 2 完成独立审稿 + 交叉回应后，进入收敛判断阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 195

## Round 195

2 recorded events


### User

_source line 2616 · 2026-05-20T12:58:56.504480+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

**核心判断**: Overall 3.5（Borderline Conference）。

**三个关键问题**:
1. **Correlation-selection gap 的 by-construction 成分**（N1, critical）——4/5 信号是 instance-level 的，无法做 per-sample selection 是设计决定而非经验发现，需要重构叙事
2. **Cross-dataset null 结论 underpowered**（N2, critical）——n=23 的相关分析无法可靠支持"degeneracy does not predict LP gain"
3. **SciERC entity construction +1.02pp 未过 Holm-Bonferroni**（W1, warning）——两个主要数据集之一的核心结果不显著（p_adj=0.20）

**主要优势**: 统计处理水准在 NLP 论文中属上乘（bootstrap CI、TOST、permutation tests、Holm-Bonferroni），诊断框架系统性强，28 页 appendix 极详尽。如果 rebuttal 能分离 definitional vs. empirical gap 并补充 power analysis，有望升至 Conference。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 2617 · 2026-05-20T12:59:07.766654+00:00_

Reviewer 1 确认收到。当前状态：

| 环节 | 状态 |
|------|------|
| Reviewer 1（方法严谨性） | ✅ 完成，Overall 3.5 |
| Reviewer 2（新颖性/完整性） | 🔄 已派发，等待独立审稿 + 交叉回应 |
| 外部审稿 | 未启用（项目未配置） |
| 视觉审查 | ✅ 已完成（1 critical / 4 warning / 9 info） |

等待 Reviewer 2 返回后进入交叉分享第二阶段（Reviewer 1 回应 Reviewer 2），随后收敛汇总。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 196

## Round 196

6 recorded events


### User

_source line 2618 · 2026-05-20T13:00:38.267217+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 审稿意见（新颖性 + 论文完整性 + 写作质量 + Related Work）

### 总体评分
**Overall**: 3.0 / 5（Findings）
**Confidence**: 4 / 5
**一句话总结**: 对 self-consistency 在 NER 上失效的诊断分析扎实且系统，但核心 finding 部分是 by construction 而非 empirical surprise，两个关键贡献（SCD、cross-model SC）标注为未完成，entity construction 的增量过小（0.28–0.66pp），作为 Main conference 论文的新颖性和完整性不足，适合 Findings track。

### 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 核心分析方法论合理，degeneracy decomposition 有理论支撑（Proposition 1, Corollary 1），但 §5.1 cross-model 和 §5.2 SCD 均为 incomplete/preliminary，削弱了 claim 的证据链 |
| Excitement | 2.5/5 | 选题重要（test-time scaling 在 structured prediction 上的 failure mode），但 "instance-level signals cannot select among per-input candidates" 的核心结论很大程度是定义决定的，不是令人惊讶的发现 |
| Reproducibility | 4/5 | 实验细节充分（Appendix I 含完整 hyperparameters, prompt template），承诺释放代码和数据，4 个公开 benchmark |
| Overall Assessment | 3.0/5 | Findings |

---

### Must-Fix 问题（影响接收决定）

**N1** [critical] Correlation-selection gap 的 "by construction" vs "empirical finding" 边界不清

- 具体位置：§4（p4），§3.1（p3），Figure 1
- 问题：论文核心贡献之一是 "correlation-selection gap"——consistency signals 能预测质量但无法改善 selection。但 §3.1 已明确定义 instance-level signals（SJ, FK, EM, VC）为 "instance-level aggregates assigning identical scores to all N candidates"。一个对 N 个候选分数相同的信号在定义上就不能做 selection——这不是 empirical finding，是 tautology。Introduction 和 Abstract 将其框定为需要"diagnose"的"gap"，制造了虚假的 surprise。真正的 empirical contribution 仅限于：(a) LP 是唯一有 per-sample discrimination 的信号，且 LP selection 仅在 Few-NERD 上成功；(b) 三个 governing factors 的定量刻画。
- 为什么影响接收：如果一半的 "diagnostic contribution" 是 definitional，贡献量被高估。
- 建议：在 §3/§4 显式区分 definitional layer 和 empirical layer，重新校准 Introduction/Abstract 的叙事。

**N2** [critical] §5.1 Cross-Model SC 和 §5.2 SCD 标注为 "preliminary"/"ongoing"——投稿版本包含未完成工作

- 具体位置：§5.1（p5）"preliminary"；§5.2（p5）"SCD is ongoing"
- 问题：Adaptive Methods 章节的 2/3 内容（§5.1 cross-model, §5.2 SCD）声明未完成。§5.2 完全没有实验结果。在 ARR 提交 incomplete work 会被 AC 视为 premature。
- 建议：要么完成实验再提交，要么将 §5.1/§5.2 移至 Future Work 而非 contribution claim。

**N3** [critical] Entity construction 增量贡献过小，难以作为独立贡献

- 具体位置：§6.1（p5-6），Table 6（p8），Contribution 3（p2）
- 问题：Entity construction = Florian et al. (2003) entity voting + LP weighting。LP weighting vs majority vote 增量仅 +1.10pp（Few-NERD）、+1.02pp（SciERC），recover 了约 25% 的 oracle gap。LP-weighted 和 uniform weighting 差异在 [0.15, 0.35] 范围内，zero-shot 时几乎消失。
- 建议：弱化为 diagnostic 副产品，或增加更多 task/model 的 generalizability 实验。

---

### Should-Fix 问题

**W1** [warning] 实验 scope 窄于 claim——仅 LoRA fine-tuned + 72B zero-shot，缺 API 模型。

**W2** [warning] Self-Certainty、P(True) 等 per-sample confidence 方法未测试——这些恰恰可能绕过 selection gap。

**W3** [warning] 与 Yao et al. (2026) 的差异化不足——两篇都发现 NER/RE 的 consistency-accuracy correlation 弱，需显式对比。

**W4** [warning] 术语/metric 命名不一致，F1 的不同变体和 signal 缩写混用。

**W5** [warning] 30 页附录暗示 scope 可能过大，§5.1/5.2 和 RE extension 可考虑缩减。

---

### 小问题
- Figure 2 颜色方案在打印时可读性弱
- §6.3 decomposition 公式在正文中缺 intuitive explanation
- Bib 文件有 17 个 orphan entries 需清理
- Table 2 "†" 标记解释不直观

---

### 主要优势
1. 选题重要且及时（test-time scaling + structured prediction failure mode）
2. 实验设计严谨（4 benchmark × 8 model × 5 signal）
3. Degeneracy decomposition（§6.3）是最强贡献——E[Δ_F1] ≤ (1−D)·G_nd bound 可验证
4. MBR 连接自然有洞察（§6.1, Appendix N.2）
5. 诚实的 Limitations

---

### Questions
1. 能否量化 gap 中多少是 tautological（instance-level by definition）vs empirical（LP degeneracy）？
2. SCD/cross-model 完整实验预计何时完成？
3. Self-Certainty 在 constrained decoding 下是否可用？
4. Free-form decoding 下 LP selection 更有效（Appendix O）——为何不在正文 highlight？
5. N-scaling 仅到 N=32——有 N=256 的数据吗？

---

### Missing References
1. EL4NER (arXiv:2505.23038, May 2025) — multi-LLM ensemble for NER
2. Structure-Conditional MBR (EMNLP 2025) — MBR for structured outputs
3. Self-Certainty for Best-of-N (arXiv:2502.18581) — per-sample signal bypassing selection gap
4. G2: Guided Generation for Diversity (arXiv:2511.00432) — diversity in generation

---

### Overall Assessment
**3.0（Findings）**。degeneracy decomposition 有价值，但 by-construction finding、incomplete contributions（SCD/cross-model）、过小的 entity construction 增量共同限制了 excitement。完成 §5.1/5.2 + 增加 Self-Certainty baseline + 重新校准叙事 → 潜力 3.5。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 2619 · 2026-05-20T13:01:16.228253+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "struct_self_consist_ie",
  "text": "## 交叉回应任务\n\n以下是 Reviewer 2（新颖性 + 完整性）的完整审稿意见。请逐条回应其 **Must-Fix (N1-N3)** 和 **Should-Fix (W1-W5)** 问题，每条标注 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并引用具体 Section/Table/Figure 作为证据。\n\n---\n\n# Reviewer 2 完整审稿意见\n\n### 总体评分\n**Overall**: 3.0 / 5（Findings）\n**Confidence**: 4 / 5\n**一句话总结**: 对 self-consistency 在 NER 上失效的诊断分析扎实且系统，但核心 finding 部分是 by construction 而非 empirical surprise，两个关键贡献（SCD、cross-model SC）标注为未完成，entity construction 的增量过小（0.28–0.66pp），作为 Main conference 论文的新颖性和完整性不足，适合 Findings track。\n\n### Must-Fix 问题\n\n**N1** [critical] Correlation-selection gap 的 \"by construction\" vs \"empirical finding\" 边界不清\n\n- 具体位置：§4（p4），§3.1（p3），Figure 1\n- 问题：论文核心贡献之一是 \"correlation-selection gap\"——consistency signals 能预测质量但无法改善 selection。但 §3.1 已明确定义 instance-level signals（SJ, FK, EM, VC）为 \"instance-level aggregates assigning identical scores to all N candidates\"。一个对 N 个候选分数相同的信号在定义上就不能做 selection——这不是 empirical finding，是 tautology。Introduction 和 Abstract 将其框定为需要\"diagnose\"的\"gap\"，制造了虚假的 surprise。真正的 empirical contribution 仅限于：(a) LP 是唯一有 per-sample discrimination 的信号，且 LP selection 仅在 Few-NERD 上成功；(b) 三个 governing factors 的定量刻画。\n- 为什么影响接收：如果一半的 \"diagnostic contribution\" 是 definitional，贡献量被高估。\n\n**N2** [critical] §5.1 Cross-Model SC 和 §5.2 SCD 标注为 \"preliminary\"/\"ongoing\"——投稿版本包含未完成工作\n\n- 具体位置：§5.1（p5）\"preliminary\"；§5.2（p5）\"SCD is ongoing\"\n- 问题：Adaptive Methods 章节的 2/3 内容（§5.1 cross-model, §5.2 SCD）声明未完成。§5.2 完全没有实验结果。在 ARR 提交 incomplete work 会被 AC 视为 premature。\n\n**N3** [critical] Entity construction 增量贡献过小，难以作为独立贡献\n\n- 具体位置：§6.1（p5-6），Table 6（p8），Contribution 3（p2）\n- 问题：Entity construction = Florian et al. (2003) entity voting + LP weighting。LP weighting vs majority vote 增量仅 +1.10pp（Few-NERD）、+1.02pp（SciERC），recover 了约 25% 的 oracle gap。LP-weighted 和 uniform weighting 差异在 [0.15, 0.35] 范围内，zero-shot 时几乎消失。\n\n### Should-Fix 问题\n\n**W1** [warning] 实验 scope 窄于 claim——仅 LoRA fine-tuned + 72B zero-shot，缺 API 模型。\n\n**W2** [warning] Self-Certainty、P(True) 等 per-sample confidence 方法未测试——这些恰恰可能绕过 selection gap。\n\n**W3** [warning] 与 Yao et al. (2026) 的差异化不足——两篇都发现 NER/RE 的 consistency-accuracy correlation 弱，需显式对比。\n\n**W4** [warning] 术语/metric 命名不一致，F1 的不同变体和 signal 缩写混用。\n\n**W5** [warning] 30 页附录暗示 scope 可能过大，§5.1/5.2 和 RE extension 可考虑缩减。\n\n### Missing References\n1. EL4NER (arXiv:2505.23038, May 2025) — multi-LLM ensemble for NER\n2. Structure-Conditional MBR (EMNLP 2025) — MBR for structured outputs\n3. Self-Certainty for Best-of-N (arXiv:2502.18581) — per-sample signal bypassing selection gap\n4. G2: Guided Generation for Diversity (arXiv:2511.00432) — diversity in generation\n\n### Questions\n1. 能否量化 gap 中多少是 tautological（instance-level by definition）vs empirical（LP degeneracy）？\n2. SCD/cross-model 完整实验预计何时完成？\n3. Self-Certainty 在 constrained decoding 下是否可用？\n4. Free-form decoding 下 LP selection 更有效（Appendix O）——为何不在正文 highlight？\n5. N-scaling 仅到 N=32——有 N=256 的数据吗？\n\n---\n\n请对以上 N1-N3、W1-W5 逐条给出 [AGREE] 或 [REBUT]，引用论文具体位置支撑你的判断。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "struct_self_consist_ie",
    "text": "## 交叉回应任务\n\n以下是 Reviewer 2（新颖性 + 完整性）的完整审稿意见。请逐条回应其 **Must-Fix (N1-N3)** 和 **Should-Fix (W1-W5)** 问题，每条标注 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并引用具体 Section/Table/Figure 作为证据。\n\n---\n\n# Reviewer 2 完整审稿意见\n\n### 总体评分\n**Overall**: 3.0 / 5（Findings）\n**Confidence**: 4 / 5\n**一句话总结**: 对 self-consistency 在 NER 上失效的诊断分析扎实且系统，但核心 finding 部分是 by construction 而非 empirical surprise，两个关键贡献（SCD、cross-model SC）标注为未完成，entity construction 的增量过小（0.28–0.66pp），作为 Main conference 论文的新颖性和完整性不足，适合 Findings track。\n\n### Must-Fix 问题\n\n**N1** [critical] Correlation-selection gap 的 \"by construction\" vs \"empirical finding\" 边界不清\n\n- 具体位置：§4（p4），§3.1（p3），Figure 1\n- 问题：论文核心贡献之一是 \"correlation-selection gap\"——consistency signals 能预测质量但无法改善 selection。但 §3.1 已明确定义 instance-level signals（SJ, FK, EM, VC）为 \"instance-level aggregates assigning identical scores to all N candidates\"。一个对 N 个候选分数相同的信号在定义上就不能做 selection——这不是 empirical finding，是 tautology。Introduction 和 Abstract 将其框定为需要\"diagnose\"的\"gap\"，制造了虚假的 surprise。真正的 empirical contribution 仅限于：(a) LP 是唯一有 per-sample discrimination 的信号，且 LP selection 仅在 Few-NERD 上成功；(b) 三个 governing factors 的定量刻画。\n- 为什么影响接收：如果一半的 \"diagnostic contribution\" 是 definitional，贡献量被高估。\n\n**N2** [critical] §5.1 Cross-Model SC 和 §5.2 SCD 标注为 \"preliminary\"/\"ongoing\"——投稿版本包含未完成工作\n\n- 具体位置：§5.1（p5）\"preliminary\"；§5.2（p5）\"SCD is ongoing\"\n- 问题：Adaptive Methods 章节的 2/3 内容（§5.1 cross-model, §5.2 SCD）声明未完成。§5.2 完全没有实验结果。在 ARR 提交 incomplete work 会被 AC 视为 premature。\n\n**N3** [critical] Entity construction 增量贡献过小，难以作为独立贡献\n\n- 具体位置：§6.1（p5-6），Table 6（p8），Contribution 3（p2）\n- 问题：Entity construction = Florian et al. (2003) entity voting + LP weighting。LP weighting vs majority vote 增量仅 +1.10pp（Few-NERD）、+1.02pp（SciERC），recover 了约 25% 的 oracle gap。LP-weighted 和 uniform weighting 差异在 [0.15, 0.35] 范围内，zero-shot 时几乎消失。\n\n### Should-Fix 问题\n\n**W1** [warning] 实验 scope 窄于 claim——仅 LoRA fine-tuned + 72B zero-shot，缺 API 模型。\n\n**W2** [warning] Self-Certainty、P(True) 等 per-sample confidence 方法未测试——这些恰恰可能绕过 selection gap。\n\n**W3** [warning] 与 Yao et al. (2026) 的差异化不足——两篇都发现 NER/RE 的 consistency-accuracy correlation 弱，需显式对比。\n\n**W4** [warning] 术语/metric 命名不一致，F1 的不同变体和 signal 缩写混用。\n\n**W5** [warning] 30 页附录暗示 scope 可能过大，§5.1/5.2 和 RE extension 可考虑缩减。\n\n### Missing References\n1. EL4NER (arXiv:2505.23038, May 2025) — multi-LLM ensemble for NER\n2. Structure-Conditional MBR (EMNLP 2025) — MBR for structured outputs\n3. Self-Certainty for Best-of-N (arXiv:2502.18581) — per-sample signal bypassing selection gap\n4. G2: Guided Generation for Diversity (arXiv:2511.00432) — diversity in generation\n\n### Questions\n1. 能否量化 gap 中多少是 tautological（instance-level by definition）vs empirical（LP degeneracy）？\n2. SCD/cross-model 完整实验预计何时完成？\n3. Self-Certainty 在 constrained decoding 下是否可用？\n4. Free-form decoding 下 LP selection 更有效（Appendix O）——为何不在正文 highlight？\n5. N-scaling 仅到 N=32——有 N=256 的数据吗？\n\n---\n\n请对以上 N1-N3、W1-W5 逐条给出 [AGREE] 或 [REBUT]，引用论文具体位置支撑你的判断。"
  }
}
```

</details>

---


### Tool result

_source line 2620 · 2026-05-20T13:01:32.837138+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 16608
}
```

</details>

---


### Tool call

_source line 2621 · 2026-05-20T13:01:33.038020+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "struct_self_consist_ie",
  "text": "## 补充任务：交叉回应 Reviewer 1 的 Weaknesses\n\n你之前的审稿中未对 Reviewer 1 的各项 Weakness 做显式 [AGREE]/[REBUT] 回应。请现在逐条回应以下 Reviewer 1 的问题，每条标注 **[AGREE]** 或 **[REBUT]**，并引用论文具体 Section/Table/Figure 作为判断依据。\n\n---\n\n### Reviewer 1 的 Must-Fix\n\n**R1-N1** [critical] \"Correlation-selection gap\" 的核心发现存在 by-construction 成分\n- 4/5 信号是 instance-level 的，无法做 per-sample selection 是设计决定而非经验发现\n- 论文将五种信号的 gap 统一呈现为 \"surprising empirical finding\"，夸大了经验性成分\n- 唯一有 per-sample discrimination 的 LP 确实展现了部分 selection 能力但被 compression 限制\n\n**R1-N2** [critical] Cross-dataset 分析（ρ=0.052, p=0.81, n=23）严重 underpowered\n- n=23 的 power 仅约 50%（for ρ=0.4），无法可靠支持 \"degeneracy does not predict LP gain\" 的 null 结论\n- 检测 ρ=0.3 at 80% power 需要 n≈85\n\n### Reviewer 1 的 Should-Fix\n\n**R1-W1** [warning] SciERC entity construction +1.02pp 校正后 p_adj=0.20 不显著\n- 两个主要数据集之一的核心结果不显著\n\n**R1-W2** [warning] Holm-Bonferroni k=57 的 family 定义不透明\n- 57 个检验的具体构成未说明\n\n**R1-W3** [warning] 72B zero-shot vs 8B fine-tuned 同时变化三个因素（scale + training + quantization）\n- confounded comparison 但被用于得出 scaling 结论\n\n**R1-W4** [warning] 关键实验 seed 数量偏少（2-3 seeds）\n- SciERC 仅 2-seed mean，3 seeds 统计效力有限\n\n**R1-W5** [warning] Proposition 1 的 entity-wise independence 假设未经验证\n- NER 中 entities 之间存在强依赖（嵌套、句法约束、竞争标注）\n\n**R1-W6** [warning] Degeneracy bound 极度松弛（实际恢复率 3-12%）\n- bound 预测能力极弱\n\n---\n\n请逐条（R1-N1, R1-N2, R1-W1 ~ R1-W6）给出 [AGREE] 或 [REBUT] + 理由。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "struct_self_consist_ie",
    "text": "## 补充任务：交叉回应 Reviewer 1 的 Weaknesses\n\n你之前的审稿中未对 Reviewer 1 的各项 Weakness 做显式 [AGREE]/[REBUT] 回应。请现在逐条回应以下 Reviewer 1 的问题，每条标注 **[AGREE]** 或 **[REBUT]**，并引用论文具体 Section/Table/Figure 作为判断依据。\n\n---\n\n### Reviewer 1 的 Must-Fix\n\n**R1-N1** [critical] \"Correlation-selection gap\" 的核心发现存在 by-construction 成分\n- 4/5 信号是 instance-level 的，无法做 per-sample selection 是设计决定而非经验发现\n- 论文将五种信号的 gap 统一呈现为 \"surprising empirical finding\"，夸大了经验性成分\n- 唯一有 per-sample discrimination 的 LP 确实展现了部分 selection 能力但被 compression 限制\n\n**R1-N2** [critical] Cross-dataset 分析（ρ=0.052, p=0.81, n=23）严重 underpowered\n- n=23 的 power 仅约 50%（for ρ=0.4），无法可靠支持 \"degeneracy does not predict LP gain\" 的 null 结论\n- 检测 ρ=0.3 at 80% power 需要 n≈85\n\n### Reviewer 1 的 Should-Fix\n\n**R1-W1** [warning] SciERC entity construction +1.02pp 校正后 p_adj=0.20 不显著\n- 两个主要数据集之一的核心结果不显著\n\n**R1-W2** [warning] Holm-Bonferroni k=57 的 family 定义不透明\n- 57 个检验的具体构成未说明\n\n**R1-W3** [warning] 72B zero-shot vs 8B fine-tuned 同时变化三个因素（scale + training + quantization）\n- confounded comparison 但被用于得出 scaling 结论\n\n**R1-W4** [warning] 关键实验 seed 数量偏少（2-3 seeds）\n- SciERC 仅 2-seed mean，3 seeds 统计效力有限\n\n**R1-W5** [warning] Proposition 1 的 entity-wise independence 假设未经验证\n- NER 中 entities 之间存在强依赖（嵌套、句法约束、竞争标注）\n\n**R1-W6** [warning] Degeneracy bound 极度松弛（实际恢复率 3-12%）\n- bound 预测能力极弱\n\n---\n\n请逐条（R1-N1, R1-N2, R1-W1 ~ R1-W6）给出 [AGREE] 或 [REBUT] + 理由。"
  }
}
```

</details>

---


### Tool result

_source line 2622 · 2026-05-20T13:01:34.391694+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1353
}
```

</details>

---


### Assistant

_source line 2623 · 2026-05-20T13:01:43.485110+00:00_

交叉分享已派发。当前状态：

| 步骤 | 状态 |
|------|------|
| Reviewer 1 初审 | ✅ Overall 3.5 (Borderline Conference) |
| Reviewer 2 初审 | ✅ Overall 3.0 (Findings) |
| R1 交叉回应 R2 | 🔄 进行中 |
| R2 交叉回应 R1 | 🔄 进行中 |
| 视觉审查 | ✅ 完成 (1 critical + 4 warning) |
| 外部审稿 | ⬜ 未启用 |

**两位 Reviewer 的核心共识**：correlation-selection gap 的 by-construction 成分（R1-N1 / R2-N1 指向同一问题）。

**主要分歧待确认**：
- R2 提出 §5.1/§5.2 未完成工作是 critical 问题（R2-N2），R1 未提及
- R2 认为 entity construction 增量过小不足以作为独立贡献（R2-N3），R1 对此更温和
- R1 的 cross-dataset underpowered 分析（R1-N2）是否被 R2 认同

等待两位 Reviewer 的交叉回应返回后进入 Step 3（收敛判断）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 197

## Round 197

2 recorded events


### User

_source line 2624 · 2026-05-20T13:01:46.345267+00:00_

[Reviewer 2 审稿结果]:
审稿意见已提交给 Review Director。

**核心判断：Overall 3.0（Findings）**

三个 critical 问题：
1. Correlation-selection gap 的核心 finding 大部分是 definitional（instance-level signals 按定义不能做 per-sample selection），论文叙事上放大了 surprise 程度
2. §5.1/§5.2 两个 adaptive methods 标注 "preliminary"/"ongoing"，投稿版本包含未完成工作
3. Entity construction 增量仅 +0.28–1.3pp，作为独立贡献偏弱

最强贡献是 degeneracy decomposition（§6.3）的理论 bound 和 MBR 连接。完成实验 + 增加 Self-Certainty baseline + 校准叙事后有潜力提升到 3.5。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 2625 · 2026-05-20T13:01:56.147318+00:00_

交叉回应任务已派发给两位 Reviewer，等待回复中。

当前进度：
- **Reviewer 1** ✅ 初审完成 (3.5) → 🔄 等待对 R2 的交叉回应
- **Reviewer 2** ✅ 初审完成 (3.0) → 🔄 等待对 R1 的交叉回应
- **视觉审查** ✅ 已完成 (1 critical / 4 warning / 9 info)
- **外部审稿** 未启用

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 198

## Round 198

2 recorded events


### User

_source line 2626 · 2026-05-20T13:04:53.002804+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 交叉回应：对 Reviewer 2 审稿意见的逐条回应

---

### Must-Fix 问题

**[AGREE with nuance] R2-N1: Correlation-selection gap 的 "by construction" vs "empirical finding" 边界不清**

R2 的核心观察是正确的：§3.1（p3）明确定义 instance-level signals（SJ, FK, EM, VC）为 "instance-level aggregates assigning identical scores to all N candidates"，Figure 1 中间面板也清楚标注 "same score for all yi given x — Cannot discriminate among samples"。一个对所有候选打相同分数的信号不能做 selection，这确实是 definitional 而非 empirical surprise。Abstract 和 Introduction 用 "diagnose" 和 "gap" 的措辞在一定程度上夸大了发现的意外性。

**但我认为 R2 略微低估了实际 empirical 贡献的分量。** 具体而言：
1. 在 text generation 的 SC 文献中（Wang et al., 2023; Brown et al., 2024），majority voting 等聚合方法确实能提供 per-sample discrimination（因为输出空间离散且重叠度高）。论文的贡献在于系统性地证明这些信号在 structured prediction（NER）上 degenerate 为 instance-level——这不是先验显然的，需要 empirical verification。
2. LP 作为唯一 per-sample signal 的 selection 分析（仅在 Few-NERD 成功，+1.30pp；其他数据集失败）以及三个 governing factors（instance degeneracy、oracle headroom、LP-quality alignment）的定量刻画（§4, p4; Figure 2, Table 1）是纯 empirical 的贡献。
3. §6.3 的 degeneracy decomposition（E[Δ_F1] = (1−D)·G_od，p6）将 selection gap 量化为可测量的因素，这超越了 tautology。

**建议**：同意论文应在 framing 上更诚实——明确区分 "definitional gap"（4/5 signals 天然无 discrimination）和 "empirical gap"（LP 有 discrimination 但多数场景仍失败），而不是将两者混为一个需要 "diagnose" 的统一现象。这是 presentation 问题，不是 contribution 问题。

---

**[AGREE] R2-N2: §5.1 和 §5.3 包含未完成工作**

（注：R2 原文写的是 §5.2 SCD，实际应为 §5.3——§5.2 Trained Verifiers 有完整实验结果 AUC=0.923±0.002。）

§5.1 Cross-Model SC（p5）明确使用 "In preliminary experiments" 措辞，仅报告了 Qwen3-8B + LLaMA-3.1-8B 两个模型在 SciERC 上的初步结果（+0.12pp over pure LLaMA）。§5.3 SCD（p5）直接写 "SCD is ongoing; we include it as a motivated direction grounded in the diagnostic findings above"——完全没有实验结果。

在 ARR 提交中包含明确标注为 "preliminary" 和 "ongoing" 的内容确实不妥。AC 和 reviewer 会合理地认为这是 premature submission。即使论文将 §5 框定为 "adaptive methods"，§5.1 和 §5.3 更适合放在 future work 而非作为正文章节呈现。

**建议**：删除 §5.3 SCD 全部内容，将 §5.1 cross-model 实验要么补充完整（多数据集、多模型组合），要么降级为 Discussion 中的一句话展望。§5.2 Trained Verifiers 可保留，因为有完整实验。

---

**[REBUT] R2-N3: Entity construction 增量贡献过小**

R2 认为 entity construction 增量仅 0.28–0.66pp（LP-weighted vs uniform 的差异），作为独立贡献过小。我不同意将这个判为 critical。

1. **增量的参照基准应是 greedy baseline 而非 uniform weighting。** Table 6（p8）显示 entity construction 相对 greedy 的提升为：Few-NERD +1.4pp，SciERC +1.02pp。这是不需要任何 sample ranking/selection 的纯聚合方法——在论文已经证明 selection 大面积失败的背景下，这个 bypass selection 的路径本身有方法论价值。
2. **Oracle gap recovery 需要在上下文中理解。** Few-NERD oracle gap 约 4.1pp（Table 6: oracle 74.71 vs greedy 70.60），entity construction 恢复了 ~34%（非 R2 说的 25%）。对于一个无需训练、无需 model-internal access 的 unsupervised 方法，1/3 的 oracle gap 恢复率并不差。
3. **方法论贡献超越数字。** §6.1（p5-6）将 entity construction 形式化为 MBR decoding 的特例（Proposition 1），建立了 structured SC 与 MBR 文献的理论连接。这个 framing 的价值不取决于具体 pp 数字。
4. **LP-weighted vs uniform 的差异虽小（0.15–0.35pp），但方向一致且统计显著**（Table 6 注释提到 Holm-Bonferroni p<0.001）。Zero-shot 时差异消失恰恰印证了 §4 的 diagnostic：zero-shot 场景下 LP quality alignment 更差。

我认为 entity construction 作为 contribution 3 是合理的——它不是一个 state-of-the-art 方法，而是诊断性工作自然产出的、有理论基础的实用方案。但我同意 R2 的隐含建议：论文不应过度宣传这个增量。

---

### Should-Fix 问题

**[AGREE] R2-W1: 实验 scope 窄于 claim——缺 API 模型**

论文使用 8 个模型（4B-8B fine-tuned + 72B zero-shot），4 个数据集，这对 open-weight 模型的覆盖是合理的。但 §8 Discussion（p8）和 Conclusion 的 claim 隐含了对 LLM-based NER 的一般性结论，而未测试任何 API 模型（GPT-4o、Claude 等）。API 模型可能在 decoding 策略、内部 calibration 上有不同表现——特别是 LP 信号在 API 场景下通常不可用，这会改变 selection 策略的适用性。建议在 Limitations 中明确声明 scope 限于 open-weight models，或补充至少一个 API 模型的实验。

---

**[AGREE] R2-W2: Self-Certainty、P(True) 等 per-sample confidence 方法未测试**

p9（Responsible NLP Checklist 前的讨论）作者自己承认 "Self-Certainty (Kang et al., 2025) ... and P(True) (Kadavath et al., 2022) ... were not evaluated"。这些方法恰恰产生 per-sample scores，理论上可以绕过论文诊断出的 instance-level signal 的 selection gap。论文的核心 narrative 是 "consistency signals 不能做 selection"，但如果存在已知的 per-sample confidence 方法可以做 selection，这个 narrative 就不完整。

这不需要成为本文的实验内容，但至少需要在 Related Work 或 Discussion 中进行实质性讨论：这些方法在 constrained decoding 下是否可行？它们的 computational cost 如何？如果它们能 work，论文的 entity construction 路线相对于 confidence-based selection 的 advantage 是什么？

---

**[AGREE with nuance] R2-W3: 与 Yao et al. (2026) 的差异化不足**

p1 有一句话 differentiation："Unlike Yao et al. (2026), who demonstrate that self-consistency correlates with task accuracy, we provide the first systematic empirical characterization of when and why test-time scaling via LP-based selection succeeds or fails for structured prediction"。p2-3 Related Work 中也有引用。

但我认为这个 differentiation 确实不够充分。两篇论文在 high-level finding 上有显著重叠（NER/RE 的 consistency-accuracy correlation 弱），读者需要更清楚地理解：(a) Yao et al. 的 scope 和方法论与本文有何具体区别？(b) 本文的 three governing factors 和 degeneracy decomposition 是否在 Yao et al. 的框架中已有对应？(c) Entity construction 是本文独有的贡献吗？建议在 §2 Related Work 增加一个专门的段落做 head-to-head comparison。

---

**[AGREE] R2-W4: 术语/metric 命名不一致**

论文中确实存在 F1 变体混用的问题。§3.3（p3-4）使用 "instance-level F1 (exact span-and-type match)"，Table 1 标注 "macro F1"，§7.2（p7）提到 "per-instance macro-F1"，而 Table 3 标题用 "per-dataset median F1"。Signal 缩写方面，SJ/FK/EM/VC/LP 在首次定义后使用一致，但 "consensus-proximity" 和 "MBR" 的关系需要更清晰地说明。这类术语问题容易修复但不应忽视——reviewer 如果在第一遍阅读时被混淆，会对整篇论文的严谨度产生负面印象。

---

**[REBUT] R2-W5: 30 页附录暗示 scope 过大，§5.1/5.2 和 RE extension 应缩减**

诊断性/分析性论文的附录天然比 method paper 更长——读者和 reviewer 需要验证诊断结论的完整证据链。论文的 38 页中包括 4 个数据集 × 8 个模型 × 5 个信号的完整实验矩阵，这些是支撑正文 claim 的必要材料，不是 padding。

我同意 §5.1/§5.3 的未完成内容应删除（见我对 N2 的回应），但 RE extension（Appendix M）和详细的 ablation 表格不应删减——它们恰恰是论文 thoroughness 的体现。如果缩减这些附录，反而会被其他 reviewer 批评 "evidence 不充分"。问题不在于附录长度，而在于正文中不应 reference 未完成的附录内容。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 2627 · 2026-05-20T13:05:10.400337+00:00_

Reviewer 1 交叉回应已收到。关键判断：

| R2 问题 | R1 回应 | 要点 |
|---------|---------|------|
| N1 by-construction | AGREE with nuance | 同意 framing 需修正，但认为 empirical 贡献（LP 分析 + governing factors）被低估 |
| N2 未完成工作 | AGREE | §5.1/§5.3 应删除或移至 Future Work |
| N3 增量过小 | REBUT | 参照基准应为 greedy（+1.4pp），非 uniform（+0.3pp）；34% oracle recovery 对 unsupervised 方法合理 |
| W1-W4 | 全部 AGREE | scope 限制、Self-Certainty 缺失、Yao et al. 区分不足、术语混用 |
| W5 附录过长 | REBUT | 诊断性论文需要完整证据链，附录长度合理 |

等待 Reviewer 2 对 Reviewer 1 各项 Weakness 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 199

## Round 199

2 recorded events


### User

_source line 2628 · 2026-05-20T13:05:13.837934+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交给 Review Director。总结我的判断：

**Must-Fix：**
- **N1** [AGREE with nuance]：R2 说 4/5 信号的 selection 失败是 tautological 这点正确，但论文的 empirical 贡献（LP 分析、三个 governing factors、degeneracy decomposition）比 R2 认定的更有实质。核心问题是 framing 过度宣传 surprise，建议区分 definitional gap 和 empirical gap。
- **N2** [AGREE]：§5.1 preliminary + §5.3 ongoing 确实不应出现在 ARR 提交中。（纠正了 R2 的节号错误：实际是 §5.3 SCD 而非 §5.2。）
- **N3** [REBUT]：不同意判为 critical。Entity construction 相对 greedy +1.4pp（Few-NERD），作为无需训练的 unsupervised 聚合方法，恢复 ~34% oracle gap 是合理的；且有 MBR 理论连接（Proposition 1）。

**Should-Fix：**
- **W1** [AGREE]：缺 API 模型限制了 generalizability。
- **W2** [AGREE]：Self-Certainty/P(True) 未测试是明显缺口，至少需实质性讨论。
- **W3** [AGREE with nuance]：有初步 differentiation 但不够充分，需 head-to-head 对比段落。
- **W4** [AGREE]：F1 变体和术语命名确实混乱，容易修复。
- **W5** [REBUT]：诊断性论文附录长是正常的，问题在于正文引用了未完成内容而非附录本身过长。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 2629 · 2026-05-20T13:05:23.492475+00:00_

Reviewer 1 交叉回应已收到。等待 Reviewer 2 对 Reviewer 1 各项 Weakness (R1-N1, R1-N2, R1-W1~W6) 的交叉回应，收齐后进入收敛判断。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 200

## Round 200

24 recorded events


### User

_source line 2630 · 2026-05-20T13:12:45.230634+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 审稿意见

---

# Part 1: 独立审稿

## 1. Summary

本文研究自一致性（self-consistency, SC）在命名实体识别（NER）中的失效机制。作者构建了包含五种置信度信号（SJ, VC, FK, EM, LP）的诊断框架，在四个 NER 基准（SciERC, Few-NERD, CoNLL, WNUT-17）上系统评估质量估计与样本选择两个维度。核心发现是所有信号均能可靠估计生成质量（ρ up to 0.45, AUROC up to 0.82），但无法有效执行样本选择——作者称之为"correlation-selection gap"。论文识别出三种结构性故障模式（instance degeneracy、isolated headroom、LP compression），提出 entity-level construction（形式化为 MBR decoding, Proposition 1）部分弥合该差距（Few-NERD +1.40pp, SciERC +1.02pp），并给出退化分解上界 E[ΔF₁] ≤ (1−D)·G_nd。

## 2. Strengths

**S1. 质量估计与样本选择的正交分解是论文最具价值的概念贡献。** 将 test-time scaling 分解为"你能不能判断好坏"和"你能不能据此选出好的"两个可独立评估的维度，结构清晰且可操作。五种信号覆盖了 consensus-based（SJ, VC, FK, EM）和 model-internal（LP）两类方法，在四个数据集上的全面对比（Table 3, Figure 6 heatmaps）为后续研究提供了有参考价值的 empirical landscape。

**S2. Entity construction 与 MBR 的形式化联系。** Proposition 1（§6.1）将 entity-level majority vote 推导为 MBR decoding with balanced set-overlaps，证明流程简洁，为方法提供了决策论基础，并指明了适用边界（entity-wise independence 假设）。

**S3. 极为详尽的补充材料。** 28 页 appendix 覆盖了 N-scaling（Appendix Q）、temperature sensitivity（Appendix R）、seed stability（Appendix H）、per-entity-type analysis（Appendix W）、free-form decoding ablation（Appendix O）、cross-dataset OOD（Appendix S）、TOST 等价性检验（Appendix F, Table 16）、epoch confound analysis（Appendix Y）、LP selection failure stability（Appendix P）等，几乎预见了所有可能的审稿疑问。这一彻底程度在 NLP 论文中罕见。

**S4. 统计处理诚实且规范。** Bootstrap CI（Table 13）、Holm-Bonferroni 校正（k=57）、TOST 等价性检验、permutation tests、显著与不显著结果均如实报告（如 SciERC p_adj=0.20），是负责任的学术实践。

**S5. 实用的诊断协议。** §Z 的三步协议（measure degeneracy → assess signal-quality alignment → evaluate aggregation）超越了纯分析论文的范畴，为从业者提供了可直接使用的工作流。

## 3. Weaknesses

### Must-Fix 问题（影响接收决定）

**N1 [critical] 论文以"structured IE"和"structured prediction"为框架，但实验仅覆盖 NER 单一子任务**

- **具体位置**: Abstract ("structured prediction task"), §1 ("any set-valued structured prediction task"), Title
- **问题**: 论文标题限定为 NER，但 Abstract 和 Introduction 的叙事反复将贡献推广到"structured prediction"和"structured IE"。然而实验仅覆盖 NER。唯一的非 NER 实验是 Appendix M 的 RE 扩展（约 1.5 页），且结果显示 RE 的信号行为与 NER 质性不同：structural signals（SJ, FK, EM）的相关性在 RE 上接近零（Table 38: SciERC RE ρ near 0），LP 是唯一正向信号，这**直接挑战**了三种故障模式分类法在 NER 之外的适用性。如果 structural signals 在 RE 上根本不 work，那么论文基于 NER 构建的"instance-level signals 都能做 QE 但不能做 selection"这一核心叙事在其他 structured IE 任务上可能不成立。
- **为什么影响接收**: 论文的 framing 暗示了超越 NER 的通用性，但 RE 的初步证据反而显示框架可能是 NER-specific 的。这种 framing 与证据之间的落差会影响读者对贡献的可靠性判断。
- **建议修改方向**: (1) 将 Abstract/Intro 的叙事严格限定为 NER，不再声称 structured prediction 通用性；(2) 将 Appendix M 的 RE 结果提升到正文，明确讨论框架在 RE 上的不同表现及其含义；(3) 或者补充 event extraction / nested NER 的实验，验证框架的可推广性。

**N2 [critical] Entity construction 相对于已有 MBR/ensemble 文献的新颖性被高估**

- **具体位置**: §5.3, §6.1, Abstract ("Entity-level construction ... partially closes the gap"), Contribution 3 (p.2)
- **问题**: Entity-level construction 的核心思想——从多个样本中聚合 entity mentions 而非选择单个最佳样本——是将 MBR decoding 应用到 set-valued outputs 的自然且直观的做法。Proposition 1 的形式化虽然简洁，但 majority voting ↔ MBR 的联系本身是已知的（Kumar and Byrne, 2004; Eikema and Aziz, 2022）。论文的实际方法贡献缩小为：(a) 在 NER 上实证证明 entity-level aggregation 优于 sample-level selection（+1.0–1.4pp），(b) LP-weighting 优于 uniform weighting。这两个发现有用但增量性较强。论文将 entity construction 与诊断框架并列为同等重要的贡献，但实际新颖性主要在诊断框架而非方法本身。
- **为什么影响接收**: 如果方法贡献的新颖性有限，论文的 overall contribution 主要依赖诊断框架的新颖性和洞察深度。这对一篇同时包含 analysis 和 method 的论文来说，需要在叙事上更诚实地定位。
- **建议修改方向**: 更明确地将论文定位为 diagnostic/analysis 论文，entity construction 作为诊断框架的 proof-of-concept validation，而非独立的方法贡献。

### Should-Fix 问题（影响评分但不一票否决）

**W1 [warning] LP compression 缺乏与 LLM 校准文献的对接**

- **具体位置**: §4 ("LP compression"), §K (Appendix), Figure 8
- **问题**: LP compression 是论文识别的关键瓶颈——63% 的 instances 的 within-instance LP range 在 0.041 nat 以内（Figure 8），导致 LP 无法有效区分候选样本。但论文将此仅作为经验观察呈现，未与 LLM 校准文献对接。Auto-regressive 模型的概率压缩/过度自信是校准研究的核心话题（Kadavath et al., 2022 已被引用但未深入讨论其机制；Xiong et al., 2024 uncertainty quantification survey 对此有系统综述）。Teacher-forcing 训练导致的 exposure bias、length normalization 对概率分布的影响、constrained decoding 对 LP 动态范围的压缩——这些机制都可能解释 LP compression 的成因，进而指向可能的 remedies。
- **建议**: 在 §K 或 Discussion 中增加一段，讨论 LP compression 可能的 mechanistic 解释，将其与 LLM 校准文献联系起来。

**W2 [warning] "三种故障模式"的框架暗示了不存在的正交性**

- **具体位置**: §4 ("We diagnose three structural failure modes"), §6.3
- **问题**: Instance degeneracy、isolated headroom、LP compression 被呈现为三种独立的故障模式，但它们之间存在层级依赖而非正交关系：degeneracy 限制了最大可能增益（上界 (1−D)·G_nd）→ 在非退化实例中，headroom 的分布决定了潜在增益 → LP compression 限制了对这些潜在增益的利用。这是一个 cascade 而非三个独立维度。论文自身的证据也指向这一点：degeneracy decomposition 的 bound 极松（实际恢复率 3-12%），因为 α（signal alignment）是真正的瓶颈，而 α 正是 LP compression 和 isolated headroom 的混合效应。将其呈现为"三种故障模式"可能误导读者认为可以独立诊断和解决每种故障。
- **建议**: 将叙事重构为"诊断级联"（diagnostic cascade），明确三者的层级关系：degeneracy 设定 ceiling → headroom distribution 决定 opportunity → LP compression 限制 exploitation。

**W3 [warning] Related work 对 test-time scaling 近期文献的覆盖存在结构性缺口**

- **具体位置**: §2 "Background & Related Work"
- **问题**: §2 覆盖了 self-consistency（Wang et al., 2023）、MBR decoding、best-of-N with verifiers 的基本框架。但缺少以下与论文核心问题直接相关的文献讨论：
  - (1) **Process-level reward models**（per-step guidance vs. outcome-level selection）——论文的 LP 是 outcome-level 信号，是否 process-level 信号能突破 compression 限制？
  - (2) **Self-refinement / iterative improvement**——作为 multi-sample generation 的替代范式，与 SC 的 tradeoff 是什么？
  - (3) **Diverse beam search / structured sampling**——作为替代 temperature sampling 的多样性注入方法，是否能缓解 degeneracy？
  这些不需要实验对比，但需要在 related work 或 discussion 中进行概念性讨论。
- **建议**: 在 §2 或 §8 Discussion 中增加一段，将论文的发现与 process reward models 和 iterative refinement 的范式关联起来。

**W4 [warning] 引用质量存在问题：4 条引用未通过在线验证，3 条存在实质性元数据错误，17 条 orphan bib entries**

- **具体位置**: References (pp.10-14), .bib 文件
- **问题**: 引用验证（OpenAlex 交叉查验）发现：
  - **4 条引用未找到**：`hobelsberger2025systematic`, `lightman2024verify`, `venktesh2025trust`, `aggarwal2023adaptive`。其中 Lightman et al. "Let's Verify Step by Step" 可能是元数据错误（原文 2023 年发表），其余需手动核实。
  - **3 条实质性不匹配**：`feng2025optimal`（第一作者 bib=Feng vs API=Austin）, `park2024grammar`（第一作者 bib=Park vs API=Berg-Kirkpatrick）, `chen2025twofailures`（年份 bib=2025 vs API=2023）。
  - **17 条 orphan bib entries**：在 .bib 文件中存在但从未在论文中引用。
  这些问题不影响论文核心结论，但反映出 bibliography 管理不够审慎。
- **建议**: 逐条核实 not-found 和 mismatch 的引用，清理 orphan entries。

**W5 [warning] N-scaling 分析（Appendix Q）与理论框架脱节**

- **具体位置**: Appendix Q (Tables 31, 36), §6.3
- **问题**: N-scaling 分析清晰展示了 oracle headroom 随 N 单调增长但 SC gain 快速饱和的现象（Table 36）。这对从业者很有价值，但论文未将其与 degeneracy decomposition 联系起来——D 如何随 N 变化？upper bound (1−D)·G_nd 是否能预测 N-scaling 曲线的形状？bound 随 N 是 tighten 还是更 loose？理论框架应能解释或预测 scaling 行为，其未能做到是一个遗憾。
- **建议**: 在 Appendix Q 中增加 D(N) 和 bound(N) 的分析，展示 degeneracy decomposition 在 N-scaling 维度上的预测能力。

## 4. 小问题（不影响接收）

- **Figure 2 (p.4)**: bar chart 在灰度打印下 oracle/greedy/random 的颜色区分度不足，建议使用 hatching patterns。
- **Table 2 (p.6)**: 列头 "Degen" 缩写不够自明，首次出现时应标注全称。
- **§3.2 Soft Jaccard 公式 (Eq. 1)**: 分母使用 max(|y_i|, |y_j|) 而非标准 Jaccard 的 union。这使其更接近 containment similarity。建议注明选择 max 而非 union 的理由（computational efficiency? better calibration?）。
- **Limitations section (p.8)**: 覆盖全面但偏长，更适合精简为 3-4 个最核心的 limitation 而非事无巨细的列举。
- **Appendix Z diagnostic protocol**: 缺少当 degeneracy > 70% 时的 actionable fallback——当 entity construction 也失效时（如 CoNLL），practitioners 应采取什么替代策略？

## 5. Questions for Authors

**Q1**: Appendix M 的 RE 结果显示 structural signals 在 RE 上相关性接近零。这是否意味着论文的三种故障模式分类法（尤其是以 instance degeneracy 和 LP compression 为主的叙事）是 NER-specific 的？如果是，论文对 structured IE 社区的指导意义会如何改变？

**Q2**: LP compression 的成因是什么？是 auto-regressive factorization 的固有属性、constrained decoding 的副作用、还是模型校准问题？你们是否尝试过 per-entity LP（而非 full-sequence LP）来规避 compression？

**Q3**: Entity construction 在 CoNLL 上失败（Table 6: −0.29pp），在 SciERC 上也未通过多重检验（p_adj=0.20）。在 4 个数据集中 2 个不 work 或不显著，这对方法 generalizability 的含义是什么？是否存在可先验判断 entity construction 何时有效的条件？

**Q4**: 论文将 entity construction 与 trained verifier（§G, DeBERTa）对比，verifier 达到 AUROC=0.987 但 selection 增益仅 +4.23pp。这个结果暗示 correlation-selection gap 即使对 near-perfect quality estimators 也成立。为什么不将此发现提升到正文？这可能是论文最有冲击力的 empirical finding。

**Q5**: Cross-model SC（聚合来自不同模型的样本）是否能比 cross-dataset transfer（§5.1）更有效地增加多样性？你们是否考虑过这种设置？

## 6. Missing References

引用验证发现的问题见 W4。除此之外：
- Malinin and Gales (2021) "Uncertainty Estimation in Autoregressive Structured Prediction" — 直接相关于 structured prediction 中的不确定性估计与 LP compression 的关联
- Xiong et al. (2024) uncertainty quantification survey — 与 LP 作为置信度信号的校准问题直接相关

## 7. Overall Assessment

### 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| **Soundness** | 3.5/5 | 诊断框架设计合理、统计处理规范；但实验仅覆盖 NER，Appendix M RE 的证据反而挑战了框架的通用性；entity construction 在 SciERC 上未过多重检验 |
| **Excitement** | 3/5 | Quality estimation vs. selection 的分解有概念价值；但 entity construction 是 MBR 的直接应用（新颖性有限），实际增益 modest（+1.0-1.4pp），且框架的 NER 之外推广存疑 |
| **Reproducibility** | 4/5 | 超详细 appendix（hyperparameters Table 19, prompt template §I.1, training config），承诺 release；缺完整 GPU hours 报告 |
| **Overall Assessment** | **3.5** (Borderline Conference) | 这是一篇执行质量很高的诊断性论文。Quality estimation vs. selection 的分解是有价值的概念贡献，统计处理在 NLP 论文中属上乘，28 页 appendix 展现了极强的 due diligence。但 (1) 框架声称 structured prediction 通用性但实验仅限 NER，且 RE 初步证据挑战了可推广性，(2) entity construction 作为方法贡献新颖性有限（MBR 的直接应用），(3) 实际增益 modest（+1.0-1.4pp）且在 SciERC 上不显著。如果作者能在 rebuttal 中 (a) 收紧 framing 到 NER，(b) 补充至少一个非 NER structured task 的 pilot 实验，(c) 将 trained verifier 的 gap-persists 发现提升到正文，则有望达到 Conference。 |
| **Confidence** | 4/5 | 仔细阅读了全文含全部 38 页，熟悉 self-consistency、MBR decoding、NER 评估和 LLM 校准文献 |

**一句话总结**: 执行精良的 NER 诊断框架，QE-vs-selection 分解有概念贡献，但 NER-only 实验无法支撑 structured prediction 的通用性声称，entity construction 新颖性有限，增益 modest——Borderline Conference，rebuttal 需收紧 framing 并补充非 NER 证据。

---

# Part 2: 交叉回应 Reviewer 1

## R1 Must-Fix 问题

**[PARTIAL AGREE] R1-N1: "Correlation-selection gap" 的 by-construction 成分**

R1 指出 4/5 信号是 instance-level 的，因此它们的 selection 失效是 definitional 而非 empirical。这个观察在**技术细节上是正确的**——instance-level signals 确实"by construction"无法在同一 input 的不同 candidates 之间做区分。

但我认为 R1 对论文贡献的影响**有所高估**。原因：
1. **Instance-level signals 的 selection 失效并非完全 trivial**。即使信号不能区分同一 input 的 candidates，它仍可用于 instance-level 的 best-of-N filtering——识别出哪些 instances 的 greedy output 可能 unreliable，然后对这些 instances 进行替换。论文在 Table 1 中测试了这一策略，发现效果有限。这是一个有经验内容的 finding：好的 quality estimator 预期能识别"哪些 instances 需要帮助"，但即使如此，帮助也难以有效执行。
2. **核心洞察在于 "strong predictors, weak selectors" 的反差**。论文的 title claim 不仅仅是"selection fails"，而是"即使 quality estimation 很好，selection 仍然 fails"。这一反差对 instance-level signals 和 per-sample signals 都有经验贡献——前者的 instance-level filtering 失效，后者（LP）的 per-sample 选择受 compression 限制。
3. 但 R1 的改进建议是合理的：论文应在 §4 更清晰地区分 **definitional gap**（instance-level signals by design cannot do per-sample selection）和 **empirical gap**（LP has per-sample discriminability but compression limits its effectiveness; instance-level signals can't even do effective instance-level filtering）。

**结论**: gap 不完全是 by-construction——Table 1 的 instance-level filtering 实验有 empirical 内容——但论文的叙事确实应更清晰地分层。建议接受 R1 的修改方向 (1) 和 (2)，但不必将论文贡献缩小为"only about LP"。

**[AGREE] R1-N2: Cross-dataset analysis (n=23) underpowered**

完全同意 R1 的统计分析。n=23 检测 ρ=0.3 at α=0.05, 80% power 需要 n≈85，当前样本量的 power 确实不足。论文的 "degeneracy does not predict LP gain"（ρ=0.052, p=0.81）结论过强。

补充一点：这个 null finding 虽然被用于支持"degeneracy is dataset-intrinsic"的论点（§7.3, Figure 3），但论文的核心 decomposition（§6.3）的 **validity 不依赖于此 null finding**——upper bound E[ΔF₁] ≤ (1−D)·G_nd 作为数学恒等式无条件成立。受影响的主要是 degeneracy 的 interpretive status（是 diagnostic indicator 还是 predictive variable）。R1 建议的 power analysis 和措辞软化是必要的。

## R1 Should-Fix 问题

**[AGREE] R1-W1: SciERC entity construction p_adj=0.20 不显著**

完全同意。在 2 个主要数据集中有 1 个核心结果不显著，这对方法 generalizability 是实质性打击。正文应更醒目地呈现这一不显著性，而非仅在括号内标注。

我进一步补充：考虑到 CoNLL 上 entity construction 增益为负（Table 6: −0.29pp），**4 个数据集中仅 Few-NERD 1 个数据集的 entity construction 增益是显著的**。这进一步限制了方法的 generalizability claim。

**[AGREE] R1-W2: k=57 Holm-Bonferroni family 定义不透明**

同意。Family 定义直接影响校正严格程度。如果 57 涵盖了论文中所有统计检验，这是保守的（正确做法）；如果仅覆盖了部分检验，则可能偏宽松。需要在 appendix 中列出明细。

**[AGREE] R1-W3: 72B vs 8B 比较 confounded**

同意，但作者在 Limitations (p.8) 中已坦承 "individual effects cannot be disentangled"。这不是隐瞒而是资源限制。§6.2 的结论确实应更 hedged——从"the gap persists at 72B"改为"the gap persists under this specific 72B zero-shot configuration, though scale, training regime, and quantization effects are confounded"。

**[PARTIAL AGREE] R1-W4: Seed 数量偏少（2-3 seeds）**

部分同意。3 seeds 在 NLP 实验中是常见实践，但对小数据集（SciERC n=529）的高方差任务确实不够。然而：
- Appendix H (Table 18) 的 multi-seed stability 分析表明 signal rankings 在 3 seeds 下稳定（σ ≤ 0.025）
- 关键 directional findings（LP 是最佳 selection 信号）在所有 seeds 下一致
- 主要问题集中在 SciERC 的 entity construction 增益（2-seed mean），这确实可能因 seed 不足而不可靠

建议对 SciERC 核心结果增加到 5 seeds 是合理的，但 3-seed 的 signal ranking stability 分析已经部分回应了这个 concern。

**[AGREE] R1-W5: Entity-wise independence 假设未验证**

同意。Proposition 1 的核心假设在实际 NER 中会被违反（嵌套实体、同一 span 的竞争标注、type 间的语义约束）。论文应提供经验验证或至少定量讨论违反程度。

我补充一个观察：Appendix V（entity-level majority voting results）的 Table 50 显示 entity construction 在 degenerate subsets（所有 N samples yield identical F1）上一致为负。如果 entity-wise independence 严重被违反，可能正是在这些 degenerate instances 上（所有 samples 高度一致，entity 间依赖最强），entity construction 的拆解才最容易引入错误。这提供了一个 independence violation → method failure 的可能 pathway。

**[PARTIAL AGREE] R1-W6: Degeneracy bound 极度松弛（3-12%）**

同意 bound 极松，但我对其价值的判断与 R1 略有不同。

论文 p.6 明确解释了 bound 松弛的原因："the bound is loose because α — signal alignment — is the bottleneck"。bound 的 **diagnostic 价值**在于将 SC 失效分解为两个可独立测量的组分：(1) degeneracy 导致的 ceiling（由 D 量化），(2) 在非退化实例上的信号利用效率（由 α 量化）。即使 bound 不 tight，这个分解仍然告诉我们 **bottleneck 在哪里**——不是 degeneracy 本身（(1−D) 项通常在 0.3-0.6），而是 signal alignment。

R1 建议引入 α 的 empirical estimate 来 tighten bound——这是有价值的方向，但可能超出当前论文的范围。更现实的改进是在论文中明确讨论 bound 的 "diagnostic vs. predictive" 定位。

## R1 Questions

**Q1 (更多 per-sample signals)**: 同意这是一个重要的未探索方向。论文仅有 LP 一种 per-sample signal，增加 per-token LP variance、entity-boundary LP gradient 等可能提供更丰富的 selection 信号。但我注意到 Appendix K 已分析了 entity-token LP（§Y.3），发现 within-instance variance 更高但 AUROC 反而下降，暗示更细粒度的 LP 信号未必能突破 compression 限制。

**Q2 (Power analysis)**: 完全赞同需要 power analysis。

**Q3 (k=57 明细)**: 完全赞同需要透明化。

**Q4 (Entity-wise independence)**: 同意需要经验验证。我在 W5 回应中补充了 degenerate subsets 上 entity construction 失效的可能 pathway。

**Q5 (Tighter bound)**: 部分赞同。见 W6 回应。

**Q6 (增加 SciERC seeds)**: 赞同。SciERC 的 +1.02pp 在 2-seed mean 下不显著，增加到 5+ seeds 是判断该增益是否 real 的必要步骤。

## R1 总体评价的交叉意见

R1 给出 3.5 Borderline Conference，我给出同样的分数但 **理由侧重不同**：

- R1 的核心 concern 是 by-construction gap 和 statistical power。我认为 by-construction 问题没有 R1 描述的那么严重（instance-level filtering 有 empirical 内容），但 statistical power 问题确实成立。
- **我的核心 concern 是 novelty 和 completeness**：(1) NER-only 实验无法支撑 structured prediction 的 framing，且 RE 证据反向（这一点 R1 未涉及）；(2) entity construction 的方法新颖性有限（R1 也未强调这点）。
- 我们 **共同同意** SciERC p_adj=0.20 不显著是方法 generalizability 的实质性问题，k=57 family 需要透明化，以及 entity-wise independence 需要验证。

综合两位 reviewer 的意见，论文在 rebuttal 中需要回应的 **最核心问题** 是：
1. 收紧 structured prediction framing（R2-N1）
2. 重构叙事分离 definitional vs. empirical gap（R1-N1）
3. 补充 power analysis（R1-N2）
4. 解释 SciERC 不显著和 entity construction generalizability（R1-W1 + R2-N2）


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 2631 · 2026-05-20T13:13:28.274368+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "round_*.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "round_*.md",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports"
  }
}
```

</details>

---


### Tool result

_source line 2632 · 2026-05-20T13:13:28.575444+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_0.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_1.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_2.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_3.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_4.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_5.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_6.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_7.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_7_consistency.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_9.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_10.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_11.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_12.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_13.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_14.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_15.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_16.md
/home/ubu
…[truncated 809 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 2633 · 2026-05-20T13:13:28.678352+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 2634 · 2026-05-20T13:13:28.678864+00:00_

1	issues:
2	  # ===== 历史 resolved issues（保留记录）=====
3	  - id: "R1-W1"
4	    summary: "Few-NERD 3-epoch vs SciERC 5-epoch 训练时长混淆效应"
5	    category: experiment
6	    severity: critical
7	    status: resolved
8	    first_raised_round: 1
9	    last_seen_round: 19
10	    resolution: "Reviewer PASS: 脚注+§4.1+appendix epoch data 一致。tab:epoch_confound caption 已注明 5K subsample。"
11	    resolution_round: 19
12	
13	  - id: "R1-W2"
14	    summary: "\"Two jointly necessary conditions\" 因果性表述过强"
15	    category: framing
16	    severity: critical
17	    status: resolved
18	    first_raised_round: 1
19	    last_seen_round: 21
20	    resolution: "全文降级为 empirical pattern/factors。Reviewer 确认正文+appendix 15处+4处残留全部修复，0 因果语言残留。"
21	    resolution_round: 21
22	
23	  - id: "R2-N1"
24	    summary: "Contribution 1 'methodological premise' 是定义推论"
25	    category: framing
26	    severity: critical
27	    status: resolved
28	    first_raised_round: 1
29	    last_seen_round: 19
30	    resolution: "Reviewer PASS: 标题改为 'Quality estimation framework'; Abstract 干净。"
31	    resolution_round: 19
32	
33	  - id: "R2-N2"
34	    summary: "与 MBR 文献差异化定位不够锐利"
35	    category: framing
36	    severity: warning
37	    status: resolved
38	    first_raised_round: 1
39	    last_seen_round: 19
40	    resolution: "Reviewer PASS: Introduction 区分清晰，ρ=0.52 数据一致。"
41	    resolution_round: 19
42	
43	  - id: "R2-N4"
44	    summary: "模型规模 3B-8B，70B+ 未知"
45	    category: experiment
46	    severity: info
47	    status: resolved
48	    first_raised_round: 1
49	    last_seen_round: 19
50	    resolution: "Round 20 检查 PASS: limitations.tex '4B-8B scale; 70B+ untested'。"
51	    resolution_round: 19
52	
53	  - id: "R1-W3"
54	    summary: "2-seed 统计效力不足"
55	    category: experiment
56	    severity: warning
57	    status: resolved
58	    first_raised_round: 1
59	    last_seen_round: 19
60	    resolution: "Reviewer PASS: tab:fewnerd 脚注 '3-seed mean: +0.04±0.48pp'。"
61	    resolution_round: 19
62	
63	  - id: "R1-W4"
64	    summary: "P
…[truncated 1102 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2635 · 2026-05-20T13:13:32.342357+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml",
  "offset": "100",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml",
    "offset": "100",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 2636 · 2026-05-20T13:13:32.342917+00:00_

100	    resolution: "Round 20 检查 PASS: 脚注解释了 3-seed mean 和 epoch 差异。"
101	    resolution_round: 19
102	
103	  - id: "R2-W1"
104	    summary: "Abstract 数字过载"
105	    category: writing
106	    severity: warning
107	    status: resolved
108	    first_raised_round: 1
109	    last_seen_round: 19
110	    resolution: "Reviewer PASS: Abstract 含 3 个数字 (≤3)。"
111	    resolution_round: 19
112	
113	  - id: "R2-W2"
114	    summary: "Actionable contribution 偏薄"
115	    category: framing
116	    severity: warning
117	    status: resolved
118	    first_raised_round: 1
119	    last_seen_round: 21
120	    resolution: "Conclusion 新增 practitioner guidance。"
121	    resolution_round: 21
122	
123	  - id: "R2-W3"
124	    summary: "Discussion 过于碎片化"
125	    category: writing
126	    severity: info
127	    status: resolved
128	    first_raised_round: 1
129	    last_seen_round: 19
130	    resolution: "5 段合并完成。"
131	    resolution_round: 19
132	
133	  - id: "R2-W5"
134	    summary: "核心数字跨 section 重复"
135	    category: writing
136	    severity: info
137	    status: resolved
138	    first_raised_round: 1
139	    last_seen_round: 19
140	    resolution: "属正常范围。"
141	    resolution_round: 19
142	
143	  - id: "R2-W4-baseline"
144	    summary: "缺少 baseline signals"
145	    category: experiment
146	    severity: warning
147	    status: resolved
148	    first_raised_round: 1
149	    last_seen_round: 19
150	    resolution: "Round 20 检查 PASS。"
151	    resolution_round: 19
152	
153	  - id: "R2-W4-re"
154	    summary: "RE extension preliminary 但引用频繁"
155	    category: framing
156	    severity: info
157	    status: resolved
158	    first_raised_round: 1
159	    last_seen_round: 19
160	    resolution: "Round 20 检查 PASS。"
161	    resolution_round: 19
162	
163	  - id: "R1-MR1"
164	    summary: "缺失引用: Geifman & El-Yaniv 2017, XGrammar 等"
165	    category: format
166	    severity: warning
167	    status: resolved
168	    first_raised_round: 1
169	    last_seen_round: 20
170	    resolution: "Paper Agent 补全 4 篇。"
…[truncated 3755 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2637 · 2026-05-20T13:13:35.651562+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml",
  "offset": "299",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml",
    "offset": "299",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 2638 · 2026-05-20T13:13:35.702323+00:00_

299	    last_seen_round: 21
300	    resolution: "Method §3.3 列出 4 值 + 3 类 protocol variants。"
301	    resolution_round: 21
302	
303	  - id: "R21-I1"
304	    summary: "Appendix 残留实验标识"
305	    category: format
306	    severity: info
307	    status: resolved
308	    first_raised_round: 21
309	    last_seen_round: 21
310	    resolution: "全文搜索确认无残留。"
311	    resolution_round: 21
312	
313	  - id: "R21-I2"
314	    summary: "'Capability trap' 措辞过强"
315	    category: writing
316	    severity: info
317	    status: resolved
318	    first_raised_round: 21
319	    last_seen_round: 21
320	    resolution: "统一使用 'capability-diversity tension'。"
321	    resolution_round: 21
322	
323	  - id: "R21-I3"
324	    summary: "3 处 -ing 短语残留"
325	    category: writing
326	    severity: info
327	    status: resolved
328	    first_raised_round: 21
329	    last_seen_round: 21
330	    resolution: "3 处改写完成。"
331	    resolution_round: 21
332	
333	  - id: "R21-MR1"
334	    summary: "缺失引用: Farquhar et al., Chen et al. pass@k"
335	    category: format
336	    severity: warning
337	    status: resolved
338	    first_raised_round: 21
339	    last_seen_round: 21
340	    resolution: "已补入 Related Work。"
341	    resolution_round: 21
342	
343	  - id: "R21-Q3"
344	    summary: "Per-entity-type ρ=-0.881 effective df 问题"
345	    category: experiment
346	    severity: info
347	    status: resolved
348	    first_raised_round: 21
349	    last_seen_round: 21
350	    resolution: "Appendix 已有 df=4 adjustment。"
351	    resolution_round: 21
352	
353	  - id: "R22-N1"
354	    summary: "正文再次超页约 2 页"
355	    category: format
356	    severity: critical
357	    status: resolved
358	    first_raised_round: 22
359	    last_seen_round: 23
360	    resolution: "Multiple compression rounds completed. ≤8 pages confirmed."
361	    resolution_round: 23
362	
363	  - id: "R22-N2"
364	    summary: "标题暗示纯 negative result"
365	    category: framing
366	    severity: critical
367	    status: resolved
368	    first_raised_round: 22
369	    
…[truncated 4639 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2639 · 2026-05-20T13:13:38.542102+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml",
  "offset": "498",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml",
    "offset": "498",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 2640 · 2026-05-20T13:13:38.592766+00:00_

498	    category: format
499	    severity: warning
500	    status: resolved
501	    first_raised_round: 22
502	    last_seen_round: 24
503	    resolution: "Paper Agent R24 Patch: LLM-Blender + CISC/Self-Certainty 技术差异 + orphan bib 清理。xie2023zeroshot 恢复引用。"
504	    resolution_round: 24
505	
506	  - id: "R22-FIG1"
507	    summary: "fig_overview 缺少 Construction 贡献 + 残留 RE 文字"
508	    category: format
509	    severity: warning
510	    status: resolved
511	    first_raised_round: 22
512	    last_seen_round: 23
513	    resolution: "fig_overview regenerated as three-column layout."
514	    resolution_round: 23
515	
516	  - id: "R22-FIG2"
517	    summary: "fig_selection_gap caption 仍引用旧双面板格式"
518	    category: format
519	    severity: info
520	    status: resolved
521	    first_raised_round: 22
522	    last_seen_round: 23
523	    resolution: "Regenerated as single-panel NER-only."
524	    resolution_round: 23
525	
526	  - id: "R23-N1"
527	    summary: "Entity-level construction 新颖性不足"
528	    category: framing
529	    severity: critical
530	    status: resolved
531	    first_raised_round: 23
532	    last_seen_round: 24
533	    mentions:
534	      - round: 23
535	        reviewers: [1, 2]
536	        note: "两位 Reviewer 独立列为 critical。"
537	      - round: 24
538	        reviewers: [1, 2]
539	        note: "R24 共识：entity construction = Florian et al. (2003) entity voting 迁移到 stochastic sampling + LP weighting。LP weighting 增量仅 0.28-0.66pp。R1 建议降级为 'straightforward application motivated by diagnostic'，不作为主要贡献。R2 维持 critical。Director 判断：作为独立方法贡献确实不足以支撑 EMNLP Main，但作为诊断的自然推论可接受——前提是 narrative 不将其作为核心卖点。"
540	    action_items:
541	      - round: 24
542	        action: "将 entity construction 从 'principled resolution' 降级为 'diagnostic-motivated mitigation'。Title 中 'Resolving' 改为 'Addressing'/'Mitigating'。Contribution 3 降调。"
543	        assigned_to: research_director
544	        status: done
545	    resolution: "Paper Agent R24 Patch: construction 降级为 diagnostic-motivated mitigation, Ti
…[truncated 5531 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2641 · 2026-05-20T13:13:41.503064+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml",
  "offset": "697",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml",
    "offset": "697",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 2642 · 2026-05-20T13:13:41.553777+00:00_

697	    category: experiment
698	    severity: warning
699	    status: resolved
700	    resolution: "Paper Agent R24 Patch: SciERC selection 结果处加 'selection effects below this threshold cannot be reliably detected'。"
701	    resolution_round: 24
702	    first_raised_round: 24
703	    last_seen_round: 24
704	
705	  - id: "R24-W3"
706	    summary: "Related Work 缺少与 Taubenfeld (CISC) / Kang (Self-Certainty) 的技术差异对比"
707	    category: writing
708	    severity: warning
709	    status: resolved
710	    resolution: "Paper Agent R24 Patch: RW 增加 2 句 CISC/Self-Certainty 技术差异。"
711	    resolution_round: 24
712	    first_raised_round: 24
713	    last_seen_round: 24
714	
715	  - id: "R24-W4"
716	    summary: "English-only + NER-heavy 泛化局限未在 Limitations 中讨论语言覆盖"
717	    category: writing
718	    severity: warning
719	    status: resolved
720	    resolution: "Paper Agent R24 Patch: Limitations 增加 1 句 English-only 语言覆盖限制。"
721	    resolution_round: 24
722	    first_raised_round: 24
723	    last_seen_round: 24
724	
725	  - id: "R24-W5"
726	    summary: "Self-Certainty (Kang 2025) 和 P(True) (Kadavath 2022) 未测试，削弱 per-sample signal 结论的完整性"
727	    category: experiment
728	    severity: warning
729	    status: wont_fix
730	    resolution: "DDL 前无法新增 signal 实验。已在 Limitations 列出。Verbalized confidence + hidden probes 已测试且同样失败，间接支持结论。"
731	    first_raised_round: 24
732	    last_seen_round: 24
733	
734	  - id: "R24-W6"
735	    summary: "Appendix D 'as a reviewer correctly noted' 暗示审稿历史"
736	    category: writing
737	    severity: warning
738	    status: resolved
739	    resolution: "Paper Agent R24 Patch: 删除，改为直接陈述。"
740	    resolution_round: 24
741	    first_raised_round: 24
742	    last_seen_round: 24
743	
744	  - id: "R24-I1"
745	    summary: "Table 2 中 EM/VC 的 p 值标 '---' 应报告具体数值"
746	    category: experiment
747	    severity: info
748	    status: resolved
749	    resolution: "Paper Agent R24 Patch: '---' → 'n/a†' + caption footnote。"
750	    resolution_round: 24
751	    first_raised_r
…[truncated 1473 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2643 · 2026-05-20T13:13:48.198266+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml",
  "offset": "799",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml",
    "offset": "799",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 2644 · 2026-05-20T13:13:48.249045+00:00_

799	        status: open

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2645 · 2026-05-20T13:14:34.017537+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool call

_source line 2646 · 2026-05-20T13:14:34.018023+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 2647 · 2026-05-20T13:14:34.118845+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-20T12:47:27.106227+00:00\", \"completed_at\": \"2026-05-20T12:50:52.542978+00:00\", \"findings\": [{\"severity\": \"critical\", \"dimension\": \"page 31\", \"message\": \"Figure 10 是文字占位符，未渲染实际图表。显示 \\\"[Figure placeholder: Oracle F1 (N) scaling curves] / 6 curves (Qwen3-8B + LLaMA-3.1-8B × SciERC / FewNERD / CoNLL) + greedy horizontal lines = power-law fit / stable across pending. / 14B/32B curves pending.\\\"。审稿人会立即判断论文未完成。\"}, {\"severity\": \"warning\", \"dimension\": \"page 1-2\", \"message\": \"连续 2 页纯文本（Abstract + Introduction + Background），无任何 display item。第一个视觉锚点（Figure 1）直到第 3 页顶部才出现。对 8 页主体论文而言，前 25% 无视觉支撑，审稿人第一印象偏\\\"文字墙\\\"。\"}, {\"severity\": \"warning\", \"dimension\": \"page 5\", \"message\": \"又一个纯文本页（Section 5 Adaptive Methods + Section 6 Theory & Scaling Law），与前面 p1-2 形成\\\"纯文字-图表密集-纯文字\\\"的不均匀节奏。\"}, {\"severity\": \"warning\", \"dimension\": \"page 7\", \"message\": \"页面过度拥挤：Tables 3, 4, 5 + Figure 3 同时堆叠在一页。Figure 3（Instance degeneracy 图）被挤压得很小，细节难以辨认。与 page 5 的空旷形成强烈反差。\"}, {\"severity\": \"warning\", \"dimension\": \"page 7\", \"message\": \"Figure 3 尺寸过小，坐标轴标签和图例在当前大小下接近可读性下限。建议单独给更多空间或移至附录扩大尺寸。\"}, {\"severity\": \"info\", \"dimension\": \"page 3\", \"message\": \"Figure 1（Overview 概念图）作为首个 display item 整体有效传达核心概念（correlation-selection gap），但面板内注释文字偏小（约 6-7pt），三个面板水平排列后单个面板宽度有限。Caption 自包含性好。\"}, {\"severity\": \"info\", \"dimension\": \"page 4\", \"message\": \"Figure 2 柱状图颜色区分度好（蓝/绿/灰），legend 可读。Table 1 使用 booktabs 风格，最优值加粗，格式规范。\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"主体末页（第 8 页）内容充实（Table 6 + Discussion + Conclusion + Limitations），空间利用率 >90%，无异常空白。\"}, {\"severity\": \"info\", \"dimension\": \"page 18\", \"message\": \"Figure 6 热力图使用绿-黄-红渐变色阶，红绿对比对色盲读者不友好。建议改用蓝-白-红或 viridis 色阶。\"}, {\"severity\": \"info\", \"dimension\": \"page 18\", \"message\": \"Figure 7（scatter plot）尺寸偏小，点标签拥挤。作为附录图可接受，但若移入主体需放大。\"}, {\"severity\"
…[truncated 652 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 101
}
```

</details>

---


### Tool result

_source line 2648 · 2026-05-20T13:14:34.119415+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 2649 · 2026-05-20T13:22:11.905301+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "struct_self_consist_ie",
  "issues_yaml": "issues:\n  # ===== 历史 resolved issues =====\n  - id: \"R1-W1\"\n    summary: \"Few-NERD 3-epoch vs SciERC 5-epoch 训练时长混淆效应\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Reviewer PASS: 脚注+§4.1+appendix epoch data 一致。tab:epoch_confound caption 已注明 5K subsample。\"\n    resolution_round: 19\n\n  - id: \"R1-W2\"\n    summary: \"\\\"Two jointly necessary conditions\\\" 因果性表述过强\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 21\n    resolution: \"全文降级为 empirical pattern/factors。Reviewer 确认正文+appendix 15处+4处残留全部修复，0 因果语言残留。\"\n    resolution_round: 21\n\n  - id: \"R2-N1\"\n    summary: \"Contribution 1 'methodological premise' 是定义推论\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Reviewer PASS: 标题改为 'Quality estimation framework'; Abstract 干净。\"\n    resolution_round: 19\n\n  - id: \"R2-N2\"\n    summary: \"与 MBR 文献差异化定位不够锐利\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Reviewer PASS: Introduction 区分清晰，ρ=0.52 数据一致。\"\n    resolution_round: 19\n\n  - id: \"R2-N4\"\n    summary: \"模型规模 3B-8B，70B+ 未知\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Round 20 检查 PASS: limitations.tex '4B-8B scale; 70B+ untested'。\"\n    resolution_round: 19\n\n  - id: \"R1-W3\"\n    summary: \"2-seed 统计效力不足\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Reviewer PASS: tab:fewnerd 脚注 '3-seed mean: +0.04±0.48pp'。\"\n    resolution_round: 19\n\n  - id: \"R1-W4\"\n    summary: \"Per-entity-type non-independence\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Reviewer PASS: appendix ICC=-0.004 written。\"\n    resolution_round: 19\n\n  - id: \"R1-W5\"\n    summary: \"\\\"Supervised verifier\\\" framing 误导\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Reviewer PASS: 'supervised verifier' 0 matches。\"\n    resolution_round: 19\n\n  - id: \"R1-W6\"\n    summary: \"Degeneracy 定义需区分\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Round 20 检查 PASS: introduction.tex 有完整定义。\"\n    resolution_round: 19\n\n  - id: \"R1-W7\"\n    summary: \"SciERC greedy F1 不一致\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Round 20 检查 PASS: 脚注解释了 3-seed mean 和 epoch 差异。\"\n    resolution_round: 19\n\n  - id: \"R2-W1\"\n    summary: \"Abstract 数字过载\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Reviewer PASS: Abstract 含 3 个数字 (≤3)。\"\n    resolution_round: 19\n\n  - id: \"R2-W2\"\n    summary: \"Actionable contribution 偏薄\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 21\n    resolution: \"Conclusion 新增 practitioner guidance。\"\n    resolution_round: 21\n\n  - id: \"R2-W3\"\n    summary: \"Discussion 过于碎片化\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"5 段合并完成。\"\n    resolution_round: 19\n\n  - id: \"R2-W5\"\n    summary: \"核心数字跨 section 重复\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"属正常范围。\"\n    resolution_round: 19\n\n  - id: \"R2-W4-baseline\"\n    summary: \"缺少 baseline signals\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Round 20 检查 PASS。\"\n    resolution_round: 19\n\n  - id: \"R2-W4-re\"\n    summary: \"RE extension preliminary 但引用频繁\"\n    category: framing\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Round 20 检查 PASS。\"\n    resolution_round: 19\n\n  - id: \"R1-MR1\"\n    summary: \"缺失引用: Geifman & El-Yaniv 2017, XGrammar 等\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 20\n    resolution: \"Paper Agent 补全 4 篇。\"\n    resolution_round: 20\n\n  - id: \"R19-I8\"\n    summary: \"Table 3 EM/VC 缺 p-values\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    resolution: \"Reviewer PASS。\"\n    resolution_round: 19\n\n  - id: \"R19-I9\"\n    summary: \"Per-type LP selection 异质性\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    resolution: \"Reviewer PASS。\"\n    resolution_round: 19\n\n  - id: \"R19-DATA1\"\n    summary: \"LLaMA CoNLL degeneracy 86.4% vs 89.2%\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    resolution: \"根因修复完成。\"\n    resolution_round: 19\n\n  - id: \"R2-N3\"\n    summary: \"Title scope: 'Structured IE' 过宽\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 21\n    resolution: \"Title 已为 NER-specific。Reviewer 确认无需修改。\"\n    resolution_round: 21\n\n  - id: \"R21-C1\"\n    summary: \"正文页数超限 (~9.5 页 vs ACL 8 页限制)\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"Discussion 3段压缩 + Conclusion 压缩。Reviewer PASS: Sections 1-6 + Limitations 在 page 8 结束。\"\n    resolution_round: 21\n\n  - id: \"R21-C2\"\n    summary: \"'两个条件'框架跨数据集经验基础不足（仅 3 数据点）\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"全文 15 处降级 + appendix 4 处残留修复。Reviewer 确认 0 因果语言残留。\"\n    resolution_round: 21\n\n  - id: \"R21-W1\"\n    summary: \"Epoch confound 对 headline result 的影响正文处理不充分\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"experiments.tex 新增 epoch-controlled comparison。\"\n    resolution_round: 21\n\n  - id: \"R21-W2\"\n    summary: \"SciERC 作为 primary test bed 系统性 underpowered\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"Few-NERD 定位为 'definitive test'。\"\n    resolution_round: 21\n\n  - id: \"R21-W3\"\n    summary: \"DALS 定位与诊断性论文冲突 + ε data-snooping\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"DALS 已移入 appendix。\"\n    resolution_round: 21\n\n  - id: \"R21-W4\"\n    summary: \"新颖性增量需更精确定位\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"Intro L8 强化。\"\n    resolution_round: 21\n\n  - id: \"R21-W5\"\n    summary: \"LP ρ 跨表不一致 (0.205 vs 0.215)\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"审计确认论文全文统一使用 0.205。\"\n    resolution_round: 21\n\n  - id: \"R21-W6\"\n    summary: \"Table 3 的 7 个连续脚注\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"7→2 脚注。\"\n    resolution_round: 21\n\n  - id: \"R21-W7\"\n    summary: \"Greedy F1 多表数值不一致 (4 values)\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"Method §3.3 列出 4 值 + 3 类 protocol variants。\"\n    resolution_round: 21\n\n  - id: \"R21-I1\"\n    summary: \"Appendix 残留实验标识\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"全文搜索确认无残留。\"\n    resolution_round: 21\n\n  - id: \"R21-I2\"\n    summary: \"'Capability trap' 措辞过强\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"统一使用 'capability-diversity tension'。\"\n    resolution_round: 21\n\n  - id: \"R21-I3\"\n    summary: \"3 处 -ing 短语残留\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"3 处改写完成。\"\n    resolution_round: 21\n\n  - id: \"R21-MR1\"\n    summary: \"缺失引用: Farquhar et al., Chen et al. pass@k\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"已补入 Related Work。\"\n    resolution_round: 21\n\n  - id: \"R21-Q3\"\n    summary: \"Per-entity-type ρ=-0.881 effective df 问题\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"Appendix 已有 df=4 adjustment。\"\n    resolution_round: 21\n\n  - id: \"R22-N1\"\n    summary: \"正文再次超页约 2 页\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 23\n    resolution: \"Multiple compression rounds completed. ≤8 pages confirmed.\"\n    resolution_round: 23\n\n  - id: \"R22-N2\"\n    summary: \"标题暗示纯 negative result\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 23\n    resolution: \"Title updated to cover both diagnostic and resolving contributions.\"\n    resolution_round: 23\n\n  - id: \"R22-W1\"\n    summary: \"correlation-selection gap 概念缺乏理论深度\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 24\n    resolution: \"D162: 23-config 回归 R²=-8.53，公式彻底失败。删除公式，改为定性叙述三因素影响。Paper Agent 已执行。\"\n    resolution_round: 24\n\n  - id: \"R22-W2\"\n    summary: \"Abstract 中 LP 和 AUROC 缩写未展开\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 23\n    resolution: \"LP and AUROC expanded in Abstract.\"\n    resolution_round: 23\n\n  - id: \"R22-W3\"\n    summary: \"LP-alignment gating protocol 使用 test set 做 probe\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 23\n    resolution: \"Dev set gating implemented.\"\n    resolution_round: 23\n\n  - id: \"R22-W4\"\n    summary: \"SciERC seed sensitivity 高 (σ=0.48 pp)\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 23\n    resolution: \"Switched to multi-seed reporting throughout.\"\n    resolution_round: 23\n\n  - id: \"R22-W5\"\n    summary: \"Entity construction 阈值 θ 跨数据集不一致\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 24\n    resolution: \"Paper Agent R24 Patch: 正文 'tuning-free' → 'empirically robust default'; Table 5 caption → 'default heuristic'。\"\n    resolution_round: 24\n\n  - id: \"R22-W6\"\n    summary: \"'the correct self-consistency analogy' 措辞过于绝对\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 23\n    resolution: \"Changed to 'a more effective self-consistency analogy'.\"\n    resolution_round: 23\n\n  - id: \"R22-W7\"\n    summary: \"仅测试 LoRA 微调但 claim 范围不限定\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 22\n    last_seen_round: 25\n    mentions:\n      - round: 22\n        reviewers: [1, 2]\n        note: \"所有实验均为 LoRA fine-tuned models。\"\n      - round: 23\n        reviewers: [1, 2]\n        note: \"Introduction qualified with 'fine-tuned 4B-8B models'.\"\n      - round: 24\n        reviewers: [1, 2]\n        note: \"R24：scope 声明在 Introduction 和 Limitations 中已存在。72B zero-shot 实验将直接回应此问题。\"\n      - round: 25\n        reviewers: [1, 2]\n        note: \"72B zero-shot 已加入但 API 模型仍缺。R1 AGREE R2-W1: LP 信号在 API 场景不可用，改变 selection 策略适用性。R2 建议 Limitations 明确声明 scope 限于 open-weight models。\"\n\n  - id: \"R22-I1\"\n    summary: \"实体匹配标准分散在 §3.2 各段落中\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 22\n    last_seen_round: 24\n    mentions:\n      - round: 25\n        reviewers: []\n        note: \"本轮未提及，可能已修复，待 Research Director 确认\"\n\n  - id: \"R22-I2\"\n    summary: \"冠词错误 + 引用格式不一致\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 23\n    resolution: \"Fixed.\"\n    resolution_round: 23\n\n  - id: \"R22-I3\"\n    summary: \"Figure 3 scatter plot 标签在打印尺寸下可能难辨\"\n    category: format\n    severity: info\n    status: open\n    first_raised_round: 22\n    last_seen_round: 25\n    mentions:\n      - round: 25\n        reviewers: [1, 2]\n        note: \"视觉审查确认 Figure 3 过小（p7），R1 提到 Figure 1 面板注释 6-7pt。\"\n\n  - id: \"R22-MR1\"\n    summary: \"缺失引用: ensemble-based IE, Xie et al. 2023\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 24\n    resolution: \"Paper Agent R24 Patch: LLM-Blender + CISC/Self-Certainty 技术差异 + orphan bib 清理。xie2023zeroshot 恢复引用。\"\n    resolution_round: 24\n\n  - id: \"R22-FIG1\"\n    summary: \"fig_overview 缺少 Construction 贡献 + 残留 RE 文字\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 23\n    resolution: \"fig_overview regenerated as three-column layout.\"\n    resolution_round: 23\n\n  - id: \"R22-FIG2\"\n    summary: \"fig_selection_gap caption 仍引用旧双面板格式\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 23\n    resolution: \"Regenerated as single-panel NER-only.\"\n    resolution_round: 23\n\n  - id: \"R23-N1\"\n    summary: \"Entity-level construction 新颖性不足\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 23\n    last_seen_round: 25\n    mentions:\n      - round: 23\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 独立列为 critical。\"\n      - round: 24\n        reviewers: [1, 2]\n        note: \"降级为 diagnostic-motivated mitigation。R24 Patch 完成。\"\n      - round: 25\n        reviewers: [1, 2]\n        note: \"R2 再次列为 critical（N3: 增量 +1.0-1.4pp 过小，MBR 直接应用新颖性有限）。R1 REBUT: 恢复 34% oracle gap 合理，MBR 形式化有独立贡献。Director 判断: 作为诊断副产品可接受，R24 降级已正确，无需进一步修改——但不应回升为核心卖点。维持 resolved。\"\n    resolution: \"Paper Agent R24 Patch: construction 降级为 diagnostic-motivated mitigation, Title 'Addressing', Contribution 3 降调完成。\"\n    resolution_round: 24\n\n  - id: \"R23-N2\"\n    summary: \"Correlation-selection gap 部分 by construction\"\n    category: framing\n    severity: critical\n    status: in_progress\n    first_raised_round: 23\n    last_seen_round: 25\n    mentions:\n      - round: 23\n        reviewers: [1, 2]\n        note: \"R2 列为 critical，R1 部分同意。\"\n      - round: 24\n        reviewers: [1, 2]\n        note: \"R1 rebuttal 有效——MBR consensus-proximity 确实给不同 sample 赋不同分数，其失败是 empirical finding。但 umbrella term 模糊了边界。\"\n      - round: 25\n        reviewers: [1, 2]\n        note: \"R25 两位 Reviewer 再次独立提出。R1 N1 (critical): 4/5 signals by construction 无 per-sample discrimination。R2 N1 (critical): tautology，Introduction 制造虚假 surprise。交叉后共识: 需在 §4 明确区分 definitional gap（4 instance-level signals）和 empirical gap（LP compression-limited selection），重新校准 Abstract/Intro 叙事。R2 补充: empirical 贡献（LP 分析、governing factors）比 by-construction 部分更有价值。\"\n    action_items:\n      - round: 25\n        action: \"§4 首段明确区分 definitional gap 和 empirical gap。Abstract/Intro 移除 'surprising'/'diagnose' 对 instance-level signals 的应用。\"\n        assigned_to: research_director\n        status: open\n\n  - id: \"R23-N3\"\n    summary: \"Expected selection gain 'bound' 中 g(·) 未定义\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 23\n    last_seen_round: 23\n    resolution: \"Changed to 'approximately factored as'. Framed as heuristic.\"\n    resolution_round: 23\n\n  - id: \"R23-W1\"\n    summary: \"ε=0.05 non-tied subset 是 post-hoc 最优切点\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 23\n    last_seen_round: 23\n    resolution: \"标记为 exploratory。\"\n    resolution_round: 23\n\n  - id: \"R23-W2\"\n    summary: \"Complementarity claim 仅基于 2 informative data points\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 23\n    last_seen_round: 23\n    resolution: \"Softened scope.\"\n    resolution_round: 23\n\n  - id: \"R23-W3\"\n    summary: \"Abstract 信息密度过高\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 23\n    last_seen_round: 23\n    resolution: \"Reduced to 4 key numbers.\"\n    resolution_round: 23\n\n  - id: \"R23-W4\"\n    summary: \"Table 4 (entity construction) 缺少 multi-seed ±σ\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 23\n    last_seen_round: 23\n    resolution: \"Updated with multi-seed mean±σ.\"\n    resolution_round: 23\n\n  - id: \"R23-I1\"\n    summary: \"Figure 1 caption ρ scope 不一致\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 23\n    last_seen_round: 23\n    resolution: \"Caption updated.\"\n    resolution_round: 23\n\n  - id: \"R23-I2\"\n    summary: \"WNUT-17 正文分析不足\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 23\n    last_seen_round: 23\n    mentions:\n      - round: 25\n        reviewers: []\n        note: \"本轮未提及，可能已修复，待 Research Director 确认\"\n\n  - id: \"R23-MR1\"\n    summary: \"缺失引用: Florian 2003, Luo 2023, Wiher 2022\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 23\n    last_seen_round: 24\n    resolution: \"合并到 R22-MR1 统一处理完成。\"\n    resolution_round: 24\n\n  # ===== Round 24 issues =====\n\n  - id: \"R24-N1\"\n    summary: \"分解公式 E[ΔF1]≈(1-d)·Δ_oracle·g(ρ_within) 仅 3 macro-level data points 验证\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 24\n    last_seen_round: 24\n    resolution: \"D162: 23-config 回归 R²=-8.53，公式完全无预测力。删除公式，改为定性叙述三因素影响。\"\n    resolution_round: 24\n\n  - id: \"R24-N2\"\n    summary: \"Gating protocol 循环性 + 验证不足\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 24\n    last_seen_round: 24\n    resolution: \"Bootstrap CI 完成：τ=0.3 位于稳定区间中心。Paper Agent 已实现三路路由。\"\n    resolution_round: 24\n\n  - id: \"R24-W1\"\n    summary: \"'Resolving' framing 过强：entity construction 仅恢复 8-11% oracle headroom\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 24\n    last_seen_round: 24\n    resolution: \"Paper Agent R24 Patch: Title 'Resolving' → 'Addressing', Contribution 3 降级。\"\n    resolution_round: 24\n\n  - id: \"R24-W2\"\n    summary: \"SciERC selection 结果 underpowered (n=529, MDE≈1.5pp)\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 24\n    last_seen_round: 24\n    resolution: \"Paper Agent R24 Patch: SciERC selection 结果处加 detection threshold caveat。\"\n    resolution_round: 24\n\n  - id: \"R24-W3\"\n    summary: \"Related Work 缺少与 CISC/Self-Certainty 技术差异对比\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 24\n    last_seen_round: 24\n    resolution: \"Paper Agent R24 Patch: RW 增加 2 句技术差异。\"\n    resolution_round: 24\n\n  - id: \"R24-W4\"\n    summary: \"English-only + NER-heavy 泛化局限未在 Limitations 讨论\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 24\n    last_seen_round: 24\n    resolution: \"Paper Agent R24 Patch: Limitations 增加 1 句。\"\n    resolution_round: 24\n\n  - id: \"R24-W5\"\n    summary: \"Self-Certainty (Kang 2025) 和 P(True) (Kadavath 2022) 未测试\"\n    category: experiment\n    severity: warning\n    status: wont_fix\n    first_raised_round: 24\n    last_seen_round: 25\n    resolution: \"DDL 前无法新增 signal 实验。已在 Limitations 列出。\"\n    mentions:\n      - round: 25\n        reviewers: [1, 2]\n        note: \"R25 再次提出（R2-W2, R1 AGREE）。两位 Reviewer 共识: 这些 per-sample confidence 方法理论上可绕过 selection gap，论文核心叙事因此不完整。建议至少在 Related Work/Discussion 做实质性讨论。\"\n\n  - id: \"R24-W6\"\n    summary: \"Appendix D 'as a reviewer correctly noted' 暗示审稿历史\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 24\n    last_seen_round: 24\n    resolution: \"Paper Agent R24 Patch: 删除，改为直接陈述。\"\n    resolution_round: 24\n\n  - id: \"R24-I1\"\n    summary: \"Table 2 中 EM/VC 的 p 值标 '---'\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 24\n    last_seen_round: 24\n    resolution: \"'---' → 'n/a†' + caption footnote。\"\n    resolution_round: 24\n\n  - id: \"R24-I2\"\n    summary: \"F1 metric 术语不统一\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 24\n    last_seen_round: 25\n    resolution: \"Paper Agent R24 Patch: method.tex 加定义。\"\n    resolution_round: 24\n    mentions:\n      - round: 25\n        reviewers: [1, 2]\n        note: \"R2-W4 再次指出术语/metric 命名不一致（F1 变体混用、signal 缩写），R1 AGREE。上轮修复可能不够彻底，需重新审查。\"\n\n  - id: \"R24-I3\"\n    summary: \"orphan bib entries 待清理\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 24\n    last_seen_round: 24\n    resolution: \"Paper Agent R24 Patch: 删除 8 条 + xie2023zeroshot 恢复。\"\n    resolution_round: 24\n\n  - id: \"R24-I4\"\n    summary: \"SJ 分母边界情况未讨论\"\n    category: method\n    severity: info\n    status: resolved\n    first_raised_round: 24\n    last_seen_round: 24\n    resolution: \"Paper Agent R24 Patch: footnote 补充。\"\n    resolution_round: 24\n\n  - id: \"R24-I5\"\n    summary: \"Abstract ρ up to 0.45 取自 CoNLL EM（最易数据集）\"\n    category: writing\n    severity: info\n    status: in_progress\n    first_raised_round: 24\n    last_seen_round: 24\n    mentions:\n      - round: 25\n        reviewers: []\n        note: \"本轮未提及。\"\n\n  # ===== Round 25 new issues =====\n\n  - id: \"R25-N1\"\n    summary: \"Cross-dataset 分析（n=23, ρ=0.052, p=0.81）严重 underpowered，不能支持 null 结论\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 25\n    last_seen_round: 25\n    mentions:\n      - round: 25\n        reviewers: [1, 2]\n        note: \"R1-N2 (critical) + R2 交叉 AGREE。n=23 的 power 仅约 50% for ρ=0.4。'Degeneracy does not predict LP gain' 结论过强。R2 补充: decomposition 的数学有效性不依赖此 null finding，但 interpretive status 受影响。\"\n    action_items:\n      - round: 25\n        action: \"报告 post-hoc power analysis（可检测的最小 ρ）。将结论从 'does not predict' 改为 'we did not find evidence, but analysis is underpowered'。增加更多 configurations 或坦承 limitation。\"\n        assigned_to: research_director\n        status: open\n\n  - id: \"R25-N2\"\n    summary: \"§5.1 Cross-Model SC ('preliminary') 和 §5.3 SCD ('ongoing') 包含未完成工作\"\n    category: framing\n    severity: critical\n    status: open\n    first_raised_round: 25\n    last_seen_round: 25\n    mentions:\n      - round: 25\n        reviewers: [1, 2]\n        note: \"R2-N2 (critical) + R1 AGREE。§5.3 完全无实验结果。ARR 提交 incomplete work 会被 AC 视为 premature。R1 纠正 R2 节号错误（§5.3 非 §5.2）。§5.2 Trained Verifiers 有完整实验可保留。\"\n    action_items:\n      - round: 25\n        action: \"删除 §5.3 SCD 全部内容。§5.1 cross-model 要么补完（多数据集多模型）要么降级为 Discussion/Future Work。\"\n        assigned_to: research_director\n        status: open\n\n  - id: \"R25-N3\"\n    summary: \"NER-only 实验无法支撑 'structured prediction' framing，RE 证据反向\"\n    category: framing\n    severity: critical\n    status: open\n    first_raised_round: 25\n    last_seen_round: 25\n    mentions:\n      - round: 25\n        reviewers: [2]\n        note: \"R2-N1 (critical)。Abstract/Intro 叙事推广到 structured prediction，但仅有 NER 实验。Appendix M RE 结果显示 structural signals 接近零——直接挑战框架的 NER 之外适用性。R1 未在初审中涉及此问题，也未在交叉中 rebut。\"\n    action_items:\n      - round: 25\n        action: \"将 Abstract/Intro 叙事严格限定为 NER。将 Appendix M RE 结果提升到正文讨论框架在非 NER 任务上的局限性。\"\n        assigned_to: research_director\n        status: open\n\n  - id: \"R25-W1\"\n    summary: \"SciERC entity construction +1.02pp 未过 Holm-Bonferroni (p_adj=0.20)；4 个数据集仅 1 个显著\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 25\n    last_seen_round: 25\n    mentions:\n      - round: 25\n        reviewers: [1, 2]\n        note: \"R1-W1 (warning) + R2 AGREE 并加强: CoNLL 增益为负 (−0.29pp)，4 数据集中仅 Few-NERD 显著。正文呈现方式让读者容易忽略不显著性。\"\n    action_items:\n      - round: 25\n        action: \"正文更醒目标注 SciERC p_adj=0.20。讨论仅 1/4 数据集显著的适用范围含义。\"\n        assigned_to: research_director\n        status: open\n\n  - id: \"R25-W2\"\n    summary: \"Holm-Bonferroni k=57 的 family 定义不透明\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 25\n    last_seen_round: 25\n    mentions:\n      - round: 25\n        reviewers: [1, 2]\n        note: \"R1-W2 (warning) + R2 AGREE。57 个检验的具体构成从未说明。\"\n    action_items:\n      - round: 25\n        action: \"Appendix 列出 57 个检验的构成规则或完整明细。\"\n        assigned_to: research_director\n        status: open\n\n  - id: \"R25-W3\"\n    summary: \"72B zero-shot vs 8B fine-tuned 三因素混淆（scale + training + quantization）\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 25\n    last_seen_round: 25\n    mentions:\n      - round: 25\n        reviewers: [1, 2]\n        note: \"R1-W3 (warning) + R2 AGREE。§6.2 从 confounded comparison 得出 scaling 结论。Limitations 已坦承但正文结论未 hedge。\"\n    action_items:\n      - round: 25\n        action: \"§6.2 结论明确标注 confounded comparison，从 'gap persists at 72B' 改为 'gap persists under this specific 72B zero-shot configuration'。\"\n        assigned_to: research_director\n        status: open\n\n  - id: \"R25-W4\"\n    summary: \"关键实验 seed 数量偏少（SciERC 2-seed, 主要结果 3 seeds）\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 25\n    last_seen_round: 25\n    mentions:\n      - round: 25\n        reviewers: [1, 2]\n        note: \"R1-W4 (warning) + R2 PARTIAL AGREE。SciERC n=529 高方差任务 2-3 seeds 效力有限。R2 认为 Appendix H signal ranking stability 部分回应了 concern。\"\n    action_items:\n      - round: 25\n        action: \"对 SciERC entity construction 核心结果增加到 5 seeds，或坦承当前 2-seed mean 可能不可靠。\"\n        assigned_to: research_director\n        status: open\n\n  - id: \"R25-W5\"\n    summary: \"Proposition 1 entity-wise independence 假设未经验验证\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 25\n    last_seen_round: 25\n    mentions:\n      - round: 25\n        reviewers: [1, 2]\n        note: \"R1-W5 (warning) + R2 AGREE。NER 中 entities 间有强依赖（嵌套、竞争标注）。R2 补充: degenerate subsets 上 entity construction 失效可能正是 independence violation 导致。\"\n    action_items:\n      - round: 25\n        action: \"在 SciERC/Few-NERD 上测量 entity decision 之间的 conditional dependence，或至少讨论假设违反的影响方向和程度。\"\n        assigned_to: research_director\n        status: open\n\n  - id: \"R25-W6\"\n    summary: \"Degeneracy bound E[ΔF₁] ≤ (1−D)·G_nd 极度松弛（实际恢复率 3-12%）\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 25\n    last_seen_round: 25\n    mentions:\n      - round: 25\n        reviewers: [1, 2]\n        note: \"R1-W6 (warning) + R2 PARTIAL AGREE。R1: 预测能力极弱。R2: diagnostic 价值仍在（识别 α 为 bottleneck），但同意需明确定位。\"\n    action_items:\n      - round: 25\n        action: \"明确 bound 的定位为 diagnostic（识别 bottleneck 在 α）而非 predictive。讨论 tightening 方向。\"\n        assigned_to: research_director\n        status: open\n\n  - id: \"R25-W7\"\n    summary: \"Yao et al. (2026) 差异化不足，high-level finding 重叠\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 25\n    last_seen_round: 25\n    mentions:\n      - round: 25\n        reviewers: [1, 2]\n        note: \"R2-W3 (warning) + R1 AGREE with nuance。两篇论文在 NER/RE consistency-accuracy correlation 弱上有显著重叠。现有 1 句 differentiation 不够充分。\"\n    action_items:\n      - round: 25\n        action: \"§2 Related Work 增加专门段落做与 Yao et al. (2026) 的 head-to-head comparison。\"\n        assigned_to: research_director\n        status: open\n\n  - id: \"R25-W8\"\n    summary: \"引用质量: 4 条未找到、3 条元数据不匹配、17 条 orphan bib\"\n    category: format\n    severity: warning\n    status: open\n    first_raised_round: 25\n    last_seen_round: 25\n    mentions:\n      - round: 25\n        reviewers: [2]\n        note: \"R2-W4。OpenAlex 交叉查验发现问题。hobelsberger2025, lightman2024, venktesh2025, aggarwal2023 未找到。feng2025/park2024/chen2025 元数据不匹配。17 条 orphan bib entries。\"\n    action_items:\n      - round: 25\n        action: \"逐条核实 not-found 和 mismatch 引用，清理 17 条 orphan entries。\"\n        assigned_to: research_director\n        status: open\n\n  - id: \"R25-W9\"\n    summary: \"LP compression 缺与 LLM 校准文献的机制性对接\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 25\n    last_seen_round: 25\n    mentions:\n      - round: 25\n        reviewers: [2]\n        note: \"R2-W1 (warning)。63% instances 的 LP range 在 0.041 nat 以内，但未讨论成因（exposure bias、length normalization、constrained decoding 对 LP 动态范围的压缩）。\"\n    action_items:\n      - round: 25\n        action: \"§K 或 Discussion 增加一段讨论 LP compression 的 mechanistic 解释及与 LLM 校准文献的联系。\"\n        assigned_to: research_director\n        status: open\n\n  - id: \"R25-W10\"\n    summary: \"三种故障模式呈 cascade 而非正交关系\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 25\n    last_seen_round: 25\n    mentions:\n      - round: 25\n        reviewers: [2]\n        note: \"R2-W2 (warning)。Degeneracy → headroom → LP compression 是层级依赖，非正交维度。论文呈现为'三种独立故障模式'可能误导。\"\n    action_items:\n      - round: 25\n        action: \"将叙事重构为 diagnostic cascade，明确三者的层级关系。\"\n        assigned_to: research_director\n        status: open\n\n  - id: \"R25-MR1\"\n    summary: \"缺失引用: Malinin & Gales 2021, Xiong et al. 2024, EL4NER, Structure-Conditional MBR, Self-Certainty BoN, G2\"\n    category: format\n    severity: warning\n    status: open\n    first_raised_round: 25\n    last_seen_round: 25\n    mentions:\n      - round: 25\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 共同建议 Malinin & Gales (2021), Xiong et al. (2024)。R1 额外: Gleave & Irving (2022)。R2 额外: EL4NER, Structure-Conditional MBR (EMNLP 2025), Self-Certainty BoN (arXiv:2502.18581), G2 (arXiv:2511.00432)。\"\n    action_items:\n      - round: 25\n        action: \"核实并补充上述引用，优先处理两位 Reviewer 共同建议的 2 篇。\"\n        assigned_to: research_director\n        status: open\n\n  - id: \"R25-VIS1\"\n    summary: \"Appendix Figure 10 (p31) 是文字占位符，未渲染实际图表\"\n    category: format\n    severity: critical\n    status: open\n    first_raised_round: 25\n    last_seen_round: 25\n    mentions:\n      - round: 25\n        reviewers: []\n        note: \"视觉审查发现。显示 '[Figure placeholder: Oracle F1 (N) scaling curves]'。审稿人会立即判断论文未完成。\"\n    action_items:\n      - round: 25\n        action: \"替换 Figure 10 占位符为实际渲染图表，或删除该 figure。\"\n        assigned_to: research_director\n        status: open"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "struct_self_consist_ie",
    "issues_yaml": "issues:\n  # ===== 历史 resolved issues =====\n  - id: \"R1-W1\"\n    summary: \"Few-NERD 3-epoch vs SciERC 5-epoch 训练时长混淆效应\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Reviewer PASS: 脚注+§4.1+appendix epoch data 一致。tab:epoch_confound caption 已注明 5K subsample。\"\n    resolution_round: 19\n\n  - id: \"R1-W2\"\n    summary: \"\\\"Two jointly necessary conditions\\\" 因果性表述过强\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 21\n    resolution: \"全文降级为 empirical pattern/factors。Reviewer 确认正文+appendix 15处+4处残留全部修复，0 因果语言残留。\"\n    resolution_round: 21\n\n  - id: \"R2-N1\"\n    summary: \"Contribution 1 'methodological premise' 是定义推论\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Reviewer PASS: 标题改为 'Quality estimation framework'; Abstract 干净。\"\n    resolution_round: 19\n\n  - id: \"R2-N2\"\n    summary: \"与 MBR 文献差异化定位不够锐利\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Reviewer PASS: Introduction 区分清晰，ρ=0.52 数据一致。\"\n    resolution_round: 19\n\n  - id: \"R2-N4\"\n    summary: \"模型规模 3B-8B，70B+ 未知\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Round 20 检查 PASS: limitations.tex '4B-8B scale; 70B+ untested'。\"\n    resolution_round: 19\n\n  - id: \"R1-W3\"\n    summary: \"2-seed 统计效力不足\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Reviewer PASS: tab:fewnerd 脚注 '3-seed mean: +0.04±0.48pp'。\"\n    resolution_round: 19\n\n  - id: \"R1-W4\"\n    summary: \"Per-entity-type non-independence\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Reviewer PASS: appendix ICC=-0.004 written。\"\n    resolution_round: 19\n\n  - id: \"R1-W5\"\n    summary: \"\\\"Supervised verifier\\\" framing 误导\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Reviewer PASS: 'supervised verifier' 0 matches。\"\n    resolution_round: 19\n\n  - id: \"R1-W6\"\n    summary: \"Degeneracy 定义需区分\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Round 20 检查 PASS: introduction.tex 有完整定义。\"\n    resolution_round: 19\n\n  - id: \"R1-W7\"\n    summary: \"SciERC greedy F1 不一致\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Round 20 检查 PASS: 脚注解释了 3-seed mean 和 epoch 差异。\"\n    resolution_round: 19\n\n  - id: \"R2-W1\"\n    summary: \"Abstract 数字过载\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Reviewer PASS: Abstract 含 3 个数字 (≤3)。\"\n    resolution_round: 19\n\n  - id: \"R2-W2\"\n    summary: \"Actionable contribution 偏薄\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 21\n    resolution: \"Conclusion 新增 practitioner guidance。\"\n    resolution_round: 21\n\n  - id: \"R2-W3\"\n    summary: \"Discussion 过于碎片化\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"5 段合并完成。\"\n    resolution_round: 19\n\n  - id: \"R2-W5\"\n    summary: \"核心数字跨 section 重复\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"属正常范围。\"\n    resolution_round: 19\n\n  - id: \"R2-W4-baseline\"\n    summary: \"缺少 baseline signals\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Round 20 检查 PASS。\"\n    resolution_round: 19\n\n  - id: \"R2-W4-re\"\n    summary: \"RE extension preliminary 但引用频繁\"\n    category: framing\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Round 20 检查 PASS。\"\n    resolution_round: 19\n\n  - id: \"R1-MR1\"\n    summary: \"缺失引用: Geifman & El-Yaniv 2017, XGrammar 等\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 20\n    resolution: \"Paper Agent 补全 4 篇。\"\n    resolution_round: 20\n\n  - id: \"R19-I8\"\n    summary: \"Table 3 EM/VC 缺 p-values\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    resolution: \"Reviewer PASS。\"\n    resolution_round: 19\n\n  - id: \"R19-I9\"\n    summary: \"Per-type LP selection 异质性\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    resolution: \"Reviewer PASS。\"\n    resolution_round: 19\n\n  - id: \"R19-DATA1\"\n    summary: \"LLaMA CoNLL degeneracy 86.4% vs 89.2%\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    resolution: \"根因修复完成。\"\n    resolution_round: 19\n\n  - id: \"R2-N3\"\n    summary: \"Title scope: 'Structured IE' 过宽\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 21\n    resolution: \"Title 已为 NER-specific。Reviewer 确认无需修改。\"\n    resolution_round: 21\n\n  - id: \"R21-C1\"\n    summary: \"正文页数超限 (~9.5 页 vs ACL 8 页限制)\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"Discussion 3段压缩 + Conclusion 压缩。Reviewer PASS: Sections 1-6 + Limitations 在 page 8 结束。\"\n    resolution_round: 21\n\n  - id: \"R21-C2\"\n    summary: \"'两个条件'框架跨数据集经验基础不足（仅 3 数据点）\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"全文 15 处降级 + appendix 4 处残留修复。Reviewer 确认 0 因果语言残留。\"\n    resolution_round: 21\n\n  - id: \"R21-W1\"\n    summary: \"Epoch confound 对 headline result 的影响正文处理不充分\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"experiments.tex 新增 epoch-controlled comparison。\"\n    resolution_round: 21\n\n  - id: \"R21-W2\"\n    summary: \"SciERC 作为 primary test bed 系统性 underpowered\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"Few-NERD 定位为 'definitive test'。\"\n    resolution_round: 21\n\n  - id: \"R21-W3\"\n    summary: \"DALS 定位与诊断性论文冲突 + ε data-snooping\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"DALS 已移入 appendix。\"\n    resolution_round: 21\n\n  - id: \"R21-W4\"\n    summary: \"新颖性增量需更精确定位\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"Intro L8 强化。\"\n    resolution_round: 21\n\n  - id: \"R21-W5\"\n    summary: \"LP ρ 跨表不一致 (0.205 vs 0.215)\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"审计确认论文全文统一使用 0.205。\"\n    resolution_round: 21\n\n  - id: \"R21-W6\"\n    summary: \"Table 3 的 7 个连续脚注\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"7→2 脚注。\"\n    resolution_round: 21\n\n  - id: \"R21-W7\"\n    summary: \"Greedy F1 多表数值不一致 (4 values)\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"Method §3.3 列出 4 值 + 3 类 protocol variants。\"\n    resolution_round: 21\n\n  - id: \"R21-I1\"\n    summary: \"Appendix 残留实验标识\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"全文搜索确认无残留。\"\n    resolution_round: 21\n\n  - id: \"R21-I2\"\n    summary: \"'Capability trap' 措辞过强\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"统一使用 'capability-diversity tension'。\"\n    resolution_round: 21\n\n  - id: \"R21-I3\"\n    summary: \"3 处 -ing 短语残留\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"3 处改写完成。\"\n    resolution_round: 21\n\n  - id: \"R21-MR1\"\n    summary: \"缺失引用: Farquhar et al., Chen et al. pass@k\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"已补入 Related Work。\"\n    resolution_round: 21\n\n  - id: \"R21-Q3\"\n    summary: \"Per-entity-type ρ=-0.881 effective df 问题\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"Appendix 已有 df=4 adjustment。\"\n    resolution_round: 21\n\n  - id: \"R22-N1\"\n    summary: \"正文再次超页约 2 页\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 23\n    resolution: \"Multiple compression rounds completed. ≤8 pages confirmed.\"\n    resolution_round: 23\n\n  - id: \"R22-N2\"\n    summary: \"标题暗示纯 negative result\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 23\n    resolution: \"Title updated to cover both diagnostic and resolving contributions.\"\n    resolution_round: 23\n\n  - id: \"R22-W1\"\n    summary: \"correlation-selection gap 概念缺乏理论深度\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 24\n    resolution: \"D162: 23-config 回归 R²=-8.53，公式彻底失败。删除公式，改为定性叙述三因素影响。Paper Agent 已执行。\"\n    resolution_round: 24\n\n  - id: \"R22-W2\"\n    summary: \"Abstract 中 LP 和 AUROC 缩写未展开\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 23\n    resolution: \"LP and AUROC expanded in Abstract.\"\n    resolution_round: 23\n\n  - id: \"R22-W3\"\n    summary: \"LP-alignment gating protocol 使用 test set 做 probe\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 23\n    resolution: \"Dev set gating implemented.\"\n    resolution_round: 23\n\n  - id: \"R22-W4\"\n    summary: \"SciERC seed sensitivity 高 (σ=0.48 pp)\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 23\n    resolution: \"Switched to multi-seed reporting throughout.\"\n    resolution_round: 23\n\n  - id: \"R22-W5\"\n    summary: \"Entity construction 阈值 θ 跨数据集不一致\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 24\n    resolution: \"Paper Agent R24 Patch: 正文 'tuning-free' → 'empirically robust default'; Table 5 caption → 'default heuristic'。\"\n    resolution_round: 24\n\n  - id: \"R22-W6\"\n    summary: \"'the correct self-consistency analogy' 措辞过于绝对\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 23\n    resolution: \"Changed to 'a more effective self-consistency analogy'.\"\n    resolution_round: 23\n\n  - id: \"R22-W7\"\n    summary: \"仅测试 LoRA 微调但 claim 范围不限定\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 22\n    last_seen_round: 25\n    mentions:\n      - round: 22\n        reviewers: [1, 2]\n        note: \"所有实验均为 LoRA fine-tuned models。\"\n      - round: 23\n        reviewers: [1, 2]\n        note: \"Introduction qualified with 'fine-tuned 4B-8B models'.\"\n      - round: 24\n        reviewers: [1, 2]\n        note: \"R24：scope 声明在 Introduction 和 Limitations 中已存在。72B zero-shot 实验将直接回应此问题。\"\n      - round: 25\n        reviewers: [1, 2]\n        note: \"72B zero-shot 已加入但 API 模型仍缺。R1 AGREE R2-W1: LP 信号在 API 场景不可用，改变 selection 策略适用性。R2 建议 Limitations 明确声明 scope 限于 open-weight models。\"\n\n  - id: \"R22-I1\"\n    summary: \"实体匹配标准分散在 §3.2 各段落中\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 22\n    last_seen_round: 24\n    mentions:\n      - round: 25\n        reviewers: []\n        note: \"本轮未提及，可能已修复，待 Research Director 确认\"\n\n  - id: \"R22-I2\"\n    summary: \"冠词错误 + 引用格式不一致\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 23\n    resolution: \"Fixed.\"\n    resolution_round: 23\n\n  - id: \"R22-I3\"\n    summary: \"Figure 3 scatter plot 标签在打印尺寸下可能难辨\"\n    category: format\n    severity: info\n    status: open\n    first_raised_round: 22\n    last_seen_round: 25\n    mentions:\n      - round: 25\n        reviewers: [1, 2]\n        note: \"视觉审查确认 Figure 3 过小（p7），R1 提到 Figure 1 面板注释 6-7pt。\"\n\n  - id: \"R22-MR1\"\n    summary: \"缺失引用: ensemble-based IE, Xie et al. 2023\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 24\n    resolution: \"Paper Agent R24 Patch: LLM-Blender + CISC/Self-Certainty 技术差异 + orphan bib 清理。xie2023zeroshot 恢复引用。\"\n    resolution_round: 24\n\n  - id: \"R22-FIG1\"\n    summary: \"fig_overview 缺少 Construction 贡献 + 残留 RE 文字\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 23\n    resolution: \"fig_overview regenerated as three-column layout.\"\n    resolution_round: 23\n\n  - id: \"R22-FIG2\"\n    summary: \"fig_selection_gap caption 仍引用旧双面板格式\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 23\n    resolution: \"Regenerated as single-panel NER-only.\"\n    resolution_round: 23\n\n  - id: \"R23-N1\"\n    summary: \"Entity-level construction 新颖性不足\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 23\n    last_seen_round: 25\n    mentions:\n      - round: 23\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 独立列为 critical。\"\n      - round: 24\n        reviewers: [1, 2]\n        note: \"降级为 diagnostic-motivated mitigation。R24 Patch 完成。\"\n      - round: 25\n        reviewers: [1, 2]\n        note: \"R2 再次列为 critical（N3: 增量 +1.0-1.4pp 过小，MBR 直接应用新颖性有限）。R1 REBUT: 恢复 34% oracle gap 合理，MBR 形式化有独立贡献。Director 判断: 作为诊断副产品可接受，R24 降级已正确，无需进一步修改——但不应回升为核心卖点。维持 resolved。\"\n    resolution: \"Paper Agent R24 Patch: construction 降级为 diagnostic-motivated mitigation, Title 'Addressing', Contribution 3 降调完成。\"\n    resolution_round: 24\n\n  - id: \"R23-N2\"\n    summary: \"Correlation-selection gap 部分 by construction\"\n    category: framing\n    severity: critical\n    status: in_progress\n    first_raised_round: 23\n    last_seen_round: 25\n    mentions:\n      - round: 23\n        reviewers: [1, 2]\n        note: \"R2 列为 critical，R1 部分同意。\"\n      - round: 24\n        reviewers: [1, 2]\n        note: \"R1 rebuttal 有效——MBR consensus-proximity 确实给不同 sample 赋不同分数，其失败是 empirical finding。但 umbrella term 模糊了边界。\"\n      - round: 25\n        reviewers: [1, 2]\n        note: \"R25 两位 Reviewer 再次独立提出。R1 N1 (critical): 4/5 signals by construction 无 per-sample discrimination。R2 N1 (critical): tautology，Introduction 制造虚假 surprise。交叉后共识: 需在 §4 明确区分 definitional gap（4 instance-level signals）和 empirical gap（LP compression-limited selection），重新校准 Abstract/Intro 叙事。R2 补充: empirical 贡献（LP 分析、governing factors）比 by-construction 部分更有价值。\"\n    action_items:\n      - round: 25\n        action: \"§4 首段明确区分 definitional gap 和 empirical gap。Abstract/Intro 移除 'surprising'/'diagnose' 对 instance-level signals 的应用。\"\n        assigned_to: research_director\n        status: open\n\n  - id: \"R23-N3\"\n    summary: \"Expected selection gain 'bound' 中 g(·) 未定义\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 23\n    last_seen_round: 23\n    resolution: \"Changed to 'approximately factored as'. Framed as heuristic.\"\n    resolution_round: 23\n\n  - id: \"R23-W1\"\n    summary: \"ε=0.05 non-tied subset 是 post-hoc 最优切点\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 23\n    last_seen_round: 23\n    resolution: \"标记为 exploratory。\"\n    resolution_round: 23\n\n  - id: \"R23-W2\"\n    summary: \"Complementarity claim 仅基于 2 informative data points\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 23\n    last_seen_round: 23\n    resolution: \"Softened scope.\"\n    resolution_round: 23\n\n  - id: \"R23-W3\"\n    summary: \"Abstract 信息密度过高\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 23\n    last_seen_round: 23\n    resolution: \"Reduced to 4 key numbers.\"\n    resolution_round: 23\n\n  - id: \"R23-W4\"\n    summary: \"Table 4 (entity construction) 缺少 multi-seed ±σ\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 23\n    last_seen_round: 23\n    resolution: \"Updated with multi-seed mean±σ.\"\n    resolution_round: 23\n\n  - id: \"R23-I1\"\n    summary: \"Figure 1 caption ρ scope 不一致\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 23\n    last_seen_round: 23\n    resolution: \"Caption updated.\"\n    resolution_round: 23\n\n  - id: \"R23-I2\"\n    summary: \"WNUT-17 正文分析不足\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 23\n    last_seen_round: 23\n    mentions:\n      - round: 25\n        reviewers: []\n        note: \"本轮未提及，可能已修复，待 Research Director 确认\"\n\n  - id: \"R23-MR1\"\n    summary: \"缺失引用: Florian 2003, Luo 2023, Wiher 2022\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 23\n    last_seen_round: 24\n    resolution: \"合并到 R22-MR1 统一处理完成。\"\n    resolution_round: 24\n\n  # ===== Round 24 issues =====\n\n  - id: \"R24-N1\"\n    summary: \"分解公式 E[ΔF1]≈(1-d)·Δ_oracle·g(ρ_within) 仅 3 macro-level data points 验证\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 24\n    last_seen_round: 24\n    resolution: \"D162: 23-config 回归 R²=-8.53，公式完全无预测力。删除公式，改为定性叙述三因素影响。\"\n    resolution_round: 24\n\n  - id: \"R24-N2\"\n    summary: \"Gating protocol 循环性 + 验证不足\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 24\n    last_seen_round: 24\n    resolution: \"Bootstrap CI 完成：τ=0.3 位于稳定区间中心。Paper Agent 已实现三路路由。\"\n    resolution_round: 24\n\n  - id: \"R24-W1\"\n    summary: \"'Resolving' framing 过强：entity construction 仅恢复 8-11% oracle headroom\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 24\n    last_seen_round: 24\n    resolution: \"Paper Agent R24 Patch: Title 'Resolving' → 'Addressing', Contribution 3 降级。\"\n    resolution_round: 24\n\n  - id: \"R24-W2\"\n    summary: \"SciERC selection 结果 underpowered (n=529, MDE≈1.5pp)\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 24\n    last_seen_round: 24\n    resolution: \"Paper Agent R24 Patch: SciERC selection 结果处加 detection threshold caveat。\"\n    resolution_round: 24\n\n  - id: \"R24-W3\"\n    summary: \"Related Work 缺少与 CISC/Self-Certainty 技术差异对比\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 24\n    last_seen_round: 24\n    resolution: \"Paper Agent R24 Patch: RW 增加 2 句技术差异。\"\n    resolution_round: 24\n\n  - id: \"R24-W4\"\n    summary: \"English-only + NER-heavy 泛化局限未在 Limitations 讨论\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 24\n    last_seen_round: 24\n    resolution: \"Paper Agent R24 Patch: Limitations 增加 1 句。\"\n    resolution_round: 24\n\n  - id: \"R24-W5\"\n    summary: \"Self-Certainty (Kang 2025) 和 P(True) (Kadavath 2022) 未测试\"\n    category: experiment\n    severity: warning\n    status: wont_fix\n    first_raised_round: 24\n    last_seen_round: 25\n    resolution: \"DDL 前无法新增 signal 实验。已在 Limitations 列出。\"\n    mentions:\n      - round: 25\n        reviewers: [1, 2]\n        note: \"R25 再次提出（R2-W2, R1 AGREE）。两位 Reviewer 共识: 这些 per-sample confidence 方法理论上可绕过 selection gap，论文核心叙事因此不完整。建议至少在 Related Work/Discussion 做实质性讨论。\"\n\n  - id: \"R24-W6\"\n    summary: \"Appendix D 'as a reviewer correctly noted' 暗示审稿历史\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 24\n    last_seen_round: 24\n    resolution: \"Paper Agent R24 Patch: 删除，改为直接陈述。\"\n    resolution_round: 24\n\n  - id: \"R24-I1\"\n    summary: \"Table 2 中 EM/VC 的 p 值标 '---'\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 24\n    last_seen_round: 24\n    resolution: \"'---' → 'n/a†' + caption footnote。\"\n    resolution_round: 24\n\n  - id: \"R24-I2\"\n    summary: \"F1 metric 术语不统一\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 24\n    last_seen_round: 25\n    resolution: \"Paper Agent R24 Patch: method.tex 加定义。\"\n    resolution_round: 24\n    mentions:\n      - round: 25\n        reviewers: [1, 2]\n        note: \"R2-W4 再次指出术语/metric 命名不一致（F1 变体混用、signal 缩写），R1 AGREE。上轮修复可能不够彻底，需重新审查。\"\n\n  - id: \"R24-I3\"\n    summary: \"orphan bib entries 待清理\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 24\n    last_seen_round: 24\n    resolution: \"Paper Agent R24 Patch: 删除 8 条 + xie2023zeroshot 恢复。\"\n    resolution_round: 24\n\n  - id: \"R24-I4\"\n    summary: \"SJ 分母边界情况未讨论\"\n    category: method\n    severity: info\n    status: resolved\n    first_raised_round: 24\n    last_seen_round: 24\n    resolution: \"Paper Agent R24 Patch: footnote 补充。\"\n    resolution_round: 24\n\n  - id: \"R24-I5\"\n    summary: \"Abstract ρ up to 0.45 取自 CoNLL EM（最易数据集）\"\n    category: writing\n    severity: info\n    status: in_progress\n    first_raised_round: 24\n    last_seen_round: 24\n    mentions:\n      - round: 25\n        reviewers: []\n        note: \"本轮未提及。\"\n\n  # ===== Round 25 new issues =====\n\n  - id: \"R25-N1\"\n    summary: \"Cross-dataset 分析（n=23, ρ=0.052, p=0.81）严重 underpowered，不能支持 null 结论\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 25\n    last_seen_round: 25\n    mentions:\n      - round: 25\n        reviewers: [1, 2]\n        note: \"R1-N2 (critical) + R2 交叉 AGREE。n=23 的 power 仅约 50% for ρ=0.4。'Degeneracy does not predict LP gain' 结论过强。R2 补充: decomposition 的数学有效性不依赖此 null finding，但 interpretive status 受影响。\"\n    action_items:\n      - round: 25\n        action: \"报告 post-hoc power analysis（可检测的最小 ρ）。将结论从 'does not predict' 改为 'we did not find evidence, but analysis is underpowered'。增加更多 configurations 或坦承 limitation。\"\n        assigned_to: research_director\n        status: open\n\n  - id: \"R25-N2\"\n    summary: \"§5.1 Cross-Model SC ('preliminary') 和 §5.3 SCD ('ongoing') 包含未完成工作\"\n    category: framing\n    severity: critical\n    status: open\n    first_raised_round: 25\n    last_seen_round: 25\n    mentions:\n      - round: 25\n        reviewers: [1, 2]\n        note: \"R2-N2 (critical) + R1 AGREE。§5.3 完全无实验结果。ARR 提交 incomplete work 会被 AC 视为 premature。R1 纠正 R2 节号错误（§5.3 非 §5.2）。§5.2 Trained Verifiers 有完整实验可保留。\"\n    action_items:\n      - round: 25\n        action: \"删除 §5.3 SCD 全部内容。§5.1 cross-model 要么补完（多数据集多模型）要么降级为 Discussion/Future Work。\"\n        assigned_to: research_director\n        status: open\n\n  - id: \"R25-N3\"\n    summary: \"NER-only 实验无法支撑 'structured prediction' framing，RE 证据反向\"\n    category: framing\n    severity: critical\n    status: open\n    first_raised_round: 25\n    last_seen_round: 25\n    mentions:\n      - round: 25\n        reviewers: [2]\n        note: \"R2-N1 (critical)。Abstract/Intro 叙事推广到 structured prediction，但仅有 NER 实验。Appendix M RE 结果显示 structural signals 接近零——直接挑战框架的 NER 之外适用性。R1 未在初审中涉及此问题，也未在交叉中 rebut。\"\n    action_items:\n      - round: 25\n        action: \"将 Abstract/Intro 叙事严格限定为 NER。将 Appendix M RE 结果提升到正文讨论框架在非 NER 任务上的局限性。\"\n        assigned_to: research_director\n        status: open\n\n  - id: \"R25-W1\"\n    summary: \"SciERC entity construction +1.02pp 未过 Holm-Bonferroni (p_adj=0.20)；4 个数据集仅 1 个显著\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 25\n    last_seen_round: 25\n    mentions:\n      - round: 25\n        reviewers: [1, 2]\n        note: \"R1-W1 (warning) + R2 AGREE 并加强: CoNLL 增益为负 (−0.29pp)，4 数据集中仅 Few-NERD 显著。正文呈现方式让读者容易忽略不显著性。\"\n    action_items:\n      - round: 25\n        action: \"正文更醒目标注 SciERC p_adj=0.20。讨论仅 1/4 数据集显著的适用范围含义。\"\n        assigned_to: research_director\n        status: open\n\n  - id: \"R25-W2\"\n    summary: \"Holm-Bonferroni k=57 的 family 定义不透明\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 25\n    last_seen_round: 25\n    mentions:\n      - round: 25\n        reviewers: [1, 2]\n        note: \"R1-W2 (warning) + R2 AGREE。57 个检验的具体构成从未说明。\"\n    action_items:\n      - round: 25\n        action: \"Appendix 列出 57 个检验的构成规则或完整明细。\"\n        assigned_to: research_director\n        status: open\n\n  - id: \"R25-W3\"\n    summary: \"72B zero-shot vs 8B fine-tuned 三因素混淆（scale + training + quantization）\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 25\n    last_seen_round: 25\n    mentions:\n      - round: 25\n        reviewers: [1, 2]\n        note: \"R1-W3 (warning) + R2 AGREE。§6.2 从 confounded comparison 得出 scaling 结论。Limitations 已坦承但正文结论未 hedge。\"\n    action_items:\n      - round: 25\n        action: \"§6.2 结论明确标注 confounded comparison，从 'gap persists at 72B' 改为 'gap persists under this specific 72B zero-shot configuration'。\"\n        assigned_to: research_director\n        status: open\n\n  - id: \"R25-W4\"\n    summary: \"关键实验 seed 数量偏少（SciERC 2-seed, 主要结果 3 seeds）\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 25\n    last_seen_round: 25\n    mentions:\n      - round: 25\n        reviewers: [1, 2]\n        note: \"R1-W4 (warning) + R2 PARTIAL AGREE。SciERC n=529 高方差任务 2-3 seeds 效力有限。R2 认为 Appendix H signal ranking stability 部分回应了 concern。\"\n    action_items:\n      - round: 25\n        action: \"对 SciERC entity construction 核心结果增加到 5 seeds，或坦承当前 2-seed mean 可能不可靠。\"\n        assigned_to: research_director\n        status: open\n\n  - id: \"R25-W5\"\n    summary: \"Proposition 1 entity-wise independence 假设未经验验证\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 25\n    last_seen_round: 25\n    mentions:\n      - round: 25\n        reviewers: [1, 2]\n        note: \"R1-W5 (warning) + R2 AGREE。NER 中 entities 间有强依赖（嵌套、竞争标注）。R2 补充: degenerate subsets 上 entity construction 失效可能正是 independence violation 导致。\"\n    action_items:\n      - round: 25\n        action: \"在 SciERC/Few-NERD 上测量 entity decision 之间的 conditional dependence，或至少讨论假设违反的影响方向和程度。\"\n        assigned_to: research_director\n        status: open\n\n  - id: \"R25-W6\"\n    summary: \"Degeneracy bound E[ΔF₁] ≤ (1−D)·G_nd 极度松弛（实际恢复率 3-12%）\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 25\n    last_seen_round: 25\n    mentions:\n      - round: 25\n        reviewers: [1, 2]\n        note: \"R1-W6 (warning) + R2 PARTIAL AGREE。R1: 预测能力极弱。R2: diagnostic 价值仍在（识别 α 为 bottleneck），但同意需明确定位。\"\n    action_items:\n      - round: 25\n        action: \"明确 bound 的定位为 diagnostic（识别 bottleneck 在 α）而非 predictive。讨论 tightening 方向。\"\n        assigned_to: research_director\n        status: open\n\n  - id: \"R25-W7\"\n    summary: \"Yao et al. (2026) 差异化不足，high-level finding 重叠\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 25\n    last_seen_round: 25\n    mentions:\n      - round: 25\n        reviewers: [1, 2]\n        note: \"R2-W3 (warning) + R1 AGREE with nuance。两篇论文在 NER/RE consistency-accuracy correlation 弱上有显著重叠。现有 1 句 differentiation 不够充分。\"\n    action_items:\n      - round: 25\n        action: \"§2 Related Work 增加专门段落做与 Yao et al. (2026) 的 head-to-head comparison。\"\n        assigned_to: research_director\n        status: open\n\n  - id: \"R25-W8\"\n    summary: \"引用质量: 4 条未找到、3 条元数据不匹配、17 条 orphan bib\"\n    category: format\n    severity: warning\n    status: open\n    first_raised_round: 25\n    last_seen_round: 25\n    mentions:\n      - round: 25\n        reviewers: [2]\n        note: \"R2-W4。OpenAlex 交叉查验发现问题。hobelsberger2025, lightman2024, venktesh2025, aggarwal2023 未找到。feng2025/park2024/chen2025 元数据不匹配。17 条 orphan bib entries。\"\n    action_items:\n      - round: 25\n        action: \"逐条核实 not-found 和 mismatch 引用，清理 17 条 orphan entries。\"\n        assigned_to: research_director\n        status: open\n\n  - id: \"R25-W9\"\n    summary: \"LP compression 缺与 LLM 校准文献的机制性对接\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 25\n    last_seen_round: 25\n    mentions:\n      - round: 25\n        reviewers: [2]\n        note: \"R2-W1 (warning)。63% instances 的 LP range 在 0.041 nat 以内，但未讨论成因（exposure bias、length normalization、constrained decoding 对 LP 动态范围的压缩）。\"\n    action_items:\n      - round: 25\n        action: \"§K 或 Discussion 增加一段讨论 LP compression 的 mechanistic 解释及与 LLM 校准文献的联系。\"\n        assigned_to: research_director\n        status: open\n\n  - id: \"R25-W10\"\n    summary: \"三种故障模式呈 cascade 而非正交关系\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 25\n    last_seen_round: 25\n    mentions:\n      - round: 25\n        reviewers: [2]\n        note: \"R2-W2 (warning)。Degeneracy → headroom → LP compression 是层级依赖，非正交维度。论文呈现为'三种独立故障模式'可能误导。\"\n    action_items:\n      - round: 25\n        action: \"将叙事重构为 diagnostic cascade，明确三者的层级关系。\"\n        assigned_to: research_director\n        status: open\n\n  - id: \"R25-MR1\"\n    summary: \"缺失引用: Malinin & Gales 2021, Xiong et al. 2024, EL4NER, Structure-Conditional MBR, Self-Certainty BoN, G2\"\n    category: format\n    severity: warning\n    status: open\n    first_raised_round: 25\n    last_seen_round: 25\n    mentions:\n      - round: 25\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 共同建议 Malinin & Gales (2021), Xiong et al. (2024)。R1 额外: Gleave & Irving (2022)。R2 额外: EL4NER, Structure-Conditional MBR (EMNLP 2025), Self-Certainty BoN (arXiv:2502.18581), G2 (arXiv:2511.00432)。\"\n    action_items:\n      - round: 25\n        action: \"核实并补充上述引用，优先处理两位 Reviewer 共同建议的 2 篇。\"\n        assigned_to: research_director\n        status: open\n\n  - id: \"R25-VIS1\"\n    summary: \"Appendix Figure 10 (p31) 是文字占位符，未渲染实际图表\"\n    category: format\n    severity: critical\n    status: open\n    first_raised_round: 25\n    last_seen_round: 25\n    mentions:\n      - round: 25\n        reviewers: []\n        note: \"视觉审查发现。显示 '[Figure placeholder: Oracle F1 (N) scaling curves]'。审稿人会立即判断论文未完成。\"\n    action_items:\n      - round: 25\n        action: \"替换 Figure 10 占位符为实际渲染图表，或删除该 figure。\"\n        assigned_to: research_director\n        status: open"
  }
}
```

</details>

---


### Tool result

_source line 2650 · 2026-05-20T13:22:12.059830+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml\", \"bytes\": 30316}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 154
}
```

</details>

---


### Tool call

_source line 2651 · 2026-05-20T13:24:41.071162+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# Round 25 审稿报告\n\n**论文**: \"Strong Predictors, Weak Selectors: Addressing the Correlation-Selection Gap in Self-Consistency for Named Entity Recognition\"\n**Venue**: EMNLP 2026 Long Paper (ARR May 2026)\n**Reviewers**: R1（方法严谨性 + 实验设计 + 统计分析）, R2（新颖性 + 完整性 + 写作质量）\n**日期**: 2026-05-20\n\n---\n\n## Summary\n\n本文研究自一致性（self-consistency）在 NER 中的失效机制。作者构建包含五种置信度信号（SJ, VC, FK, EM, LP）的诊断框架，在四个 NER 基准上系统评估质量估计与样本选择两个维度，发现所有信号均能可靠估计生成质量（ρ up to 0.45, AUROC up to 0.82）但无法有效执行样本选择——即\"correlation-selection gap\"。论文识别三种结构性故障模式（instance degeneracy、isolated headroom、LP compression），提出 entity-level construction（形式化为 MBR decoding）部分弥合该差距（Few-NERD +1.40pp, SciERC +1.02pp），并给出退化分解上界。\n\n## Strengths\n\n**S1. QE vs. selection 的正交分解是最有概念价值的贡献。** 将 test-time scaling 分解为\"能否判断好坏\"和\"能否据此选出好的\"两个可独立评估的维度，结构清晰可操作。五种信号跨四个 NER 基准的全面评估提供了比现有文献更细粒度的理解。（两位 Reviewer 共识）\n\n**S2. 统计处理水准在 NLP 论文中属上乘。** Bootstrap CI（Table 13）、Holm-Bonferroni 多重检验校正（k=57）、TOST 等价性检验（Table 16, Appendix F）、permutation tests（Table 9），不显著结果如实报告（SciERC p_adj=0.20）。（两位 Reviewer 共识，特别认可）\n\n**S3. Entity construction 与 MBR 的形式化联系。** Proposition 1（§6.1）将 entity-level majority vote 推导为 MBR decoding with balanced set-overlaps，提供清晰的决策论基础。\n\n**S4. 极其详尽的补充材料。** 28 页 appendix 覆盖 N-scaling、temperature、seed stability、per-entity-type analysis、free-form decoding ablation、cross-dataset OOD 等。在 NLP 论文中罕见的 thoroughness。\n\n**S5. 实用的诊断协议。** §Z 的三步协议为从业者提供可直接使用的工作流。\n\n## Weaknesses\n\n### 两位 Reviewer 共识的 Must-Fix 问题\n\n**[CONSENSUS CRITICAL] W1. Correlation-selection gap 的 by-construction 成分未区分**\n- R1-N1 + R2-N1。4/5 信号（SJ, VC, FK, EM）是 instance-level 的，§3.1 已明确定义其对 N 个候选打相同分数——selection 失效是定义推论而非经验发现。论文将五种信号的 gap 统一呈现为需要\"diagnose\"的\"surprising finding\"，夸大了经验性成分。唯一具备 per-sample discrimination 的 LP 确实展现了部分 selection 能力但被 compression 限制。\n- **交叉共识**: R2 认为这是 tautology 层面的过度宣传；R1 认为 LP 分析和 governing factors 的 empirical 贡献被 R2 略微低估。两位均同意需明确区分 definitional gap 和 empirical gap。\n- **历史**: 此问题自 Round 23 持续存在（R23-N2, in_progress），本轮两位 Reviewer 再次独立提出。\n- **建议**: §4 首段明确区分 definitional gap（instance-level signals by design cannot select）和 empirical gap（LP has per-sample discriminability but compression limits effectiveness）。重新校准 Abstract/Intro 叙事，移除对 instance-level signals 的 \"surprising\"/\"diagnose\" 框定。\n\n**[CONSENSUS CRITICAL] W2. Cross-dataset 分析（n=23, ρ=0.052, p=0.81）严重 underpowered**\n- R1-N2 (critical) + R2 交叉 AGREE。23 个 configurations 的 statistical power 极低：检测 ρ=0.3 at α=0.05, 80% power 需要 n≈85；当前 power 仅约 50%（for ρ=0.4）。\"Degeneracy does not predict LP gain\" 的 null 结论不可靠。\n- R2 补充：decomposition 的数学有效性不依赖此 null finding，但 degeneracy 的 interpretive status（diagnostic indicator vs. predictive variable）受影响。\n- **建议**: (1) 报告 post-hoc power analysis，明确可检测的最小 ρ；(2) 将结论从\"does not predict\"改为\"we did not find evidence for prediction, but the analysis is underpowered (n=23)\"；(3) 如有可能增加 configurations。\n\n**[CONSENSUS CRITICAL] W3. §5.1/§5.3 包含未完成工作**\n- R2-N2 (critical) + R1 AGREE。§5.1 Cross-Model SC 标注\"preliminary\"（仅 SciERC 一个数据集初步结果 +0.12pp）；§5.3 SCD 标注\"ongoing\"且完全无实验结果。ARR 提交 incomplete work 会被 AC 视为 premature。\n- R1 纠正 R2 的节号：实际为 §5.3（非 §5.2），§5.2 Trained Verifiers 有完整实验（AUC=0.923±0.002）可保留。\n- **建议**: 删除 §5.3 全部内容，§5.1 要么补完（多数据集多模型组合）要么降级为 Discussion/Future Work。\n\n### 存在分歧的问题\n\n**[DIVERGENCE] W4. Entity construction 贡献度**\n- **R2 判 critical** (N3): entity construction = Florian et al. (2003) entity voting + LP weighting，增量仅 +1.0-1.4pp vs greedy，LP-weighted vs uniform 差异 0.15-0.35pp，新颖性有限，作为独立贡献过弱。\n- **R1 REBUT**: 参照基准应为 greedy 而非 uniform weighting；Few-NERD 恢复 ~34% oracle gap（非 R2 估的 25%）；MBR 形式化（Proposition 1）有独立理论贡献；无需训练的 unsupervised 方法在 selection 大面积失败的背景下有方法论价值。\n- **Director 判断**: 作为独立方法贡献确实增量性较强，但作为诊断框架的 proof-of-concept 合理。R24 已将其从\"principled resolution\"降级为\"diagnostic-motivated mitigation\"，这一定位正确，不应再作为核心卖点。\n\n### 两位 Reviewer 共识的 Should-Fix 问题\n\n**[CONSENSUS WARNING] W5. SciERC entity construction p_adj=0.20 不显著；仅 1/4 数据集显著**\n- R1-W1 + R2 AGREE 并加强。Few-NERD +1.40pp 显著，但 SciERC +1.02pp 校正后 p_adj=0.20 不显著；CoNLL 增益为负（−0.29pp）。4 个数据集中仅 Few-NERD 显著。\n- **建议**: 正文更醒目标注 SciERC p_adj=0.20，讨论仅 1/4 显著的适用范围含义。\n\n**[CONSENSUS WARNING] W6. k=57 Holm-Bonferroni family 定义不透明**\n- R1-W2 + R2 AGREE。57 个检验的构成从未说明。Family 定义直接影响校正严格程度。\n- **建议**: Appendix 列出构成规则或完整明细。\n\n**[CONSENSUS WARNING] W7. 72B zero-shot vs 8B fine-tuned 三因素混淆**\n- R1-W3 + R2 AGREE。同时变化 scale + training regime + quantization，但 §6.2 从中得出 scaling 结论。Limitations 已坦承但正文未 hedge。\n- **建议**: §6.2 结论明确标注 confounded comparison。\n\n**[CONSENSUS WARNING] W8. Seed 数量偏少（SciERC 2-seed, 主要结果 3 seeds）**\n- R1-W4 + R2 PARTIAL AGREE。SciERC n=529 高方差任务 2-3 seeds 效力有限。R2 认为 Appendix H 的 signal ranking stability 部分回应此 concern。\n- **建议**: 对 SciERC entity construction 核心结果增加到 5 seeds。\n\n**[CONSENSUS WARNING] W9. Proposition 1 entity-wise independence 假设未验证**\n- R1-W5 + R2 AGREE。NER 中 entities 间有强依赖（嵌套实体、句法约束、竞争标注）。R2 补充 degenerate subsets 上 entity construction 失效可能正是 independence violation 导致。\n- **建议**: 提供经验验证或讨论违反程度。\n\n**[CONSENSUS WARNING] W10. Degeneracy bound 极度松弛（实际恢复率 3-12%）**\n- R1-W6 + R2 PARTIAL AGREE。R1 认为预测能力极弱；R2 认为 diagnostic 价值仍在（识别 α 为 bottleneck）。两者同意需明确定位。\n- **建议**: 明确 bound 为 diagnostic（识别 bottleneck）而非 predictive，讨论 tightening 方向。\n\n**[CONSENSUS WARNING] W11. 缺 API 模型和 Self-Certainty/P(True) per-sample signals**\n- R2-W1 + R2-W2, R1 均 AGREE。scope 限于 open-weight models（LP 在 API 场景不可用）；Self-Certainty/P(True) 未测试但理论上可绕过 selection gap。\n- **建议**: Limitations 明确声明 scope 限于 open-weight；Related Work/Discussion 实质性讨论 per-sample confidence 方法。\n\n**[R2 UNIQUE] W12. NER-only 实验无法支撑 \"structured prediction\" framing**\n- R2-N1。Abstract/Intro 叙事推广到 structured prediction，但仅有 NER 实验。Appendix M RE 结果显示 structural signals 在 RE 上接近零——直接挑战框架的通用性。\n- **建议**: 严格限定叙事为 NER，或将 RE 结果提升到正文讨论局限性。\n\n**[R2 UNIQUE] W13. 引用质量问题**\n- R2-W4。4 条引用未通过 OpenAlex 验证（hobelsberger2025, lightman2024, venktesh2025, aggarwal2023），3 条实质性元数据不匹配，17 条 orphan bib entries。\n\n**[CONSENSUS WARNING] W14. 与 Yao et al. (2026) 差异化不足**\n- R2-W3, R1 AGREE with nuance。两篇论文 high-level finding 重叠，需 head-to-head 对比段落。\n\n### 其他 Should-Fix (R2 独有)\n- **W15. LP compression 缺与 LLM 校准文献的机制性对接**（R2-W1）\n- **W16. 三种故障模式呈 cascade 而非正交关系**（R2-W2）——应重构为 diagnostic cascade\n- **W17. Related work 缺 process reward models / self-refinement / diverse beam search 讨论**（R2-W3）\n- **W18. N-scaling 分析未与 degeneracy decomposition 联系（D(N), bound(N)）**（R2-W5）\n\n### 小问题（不影响接收）\n- Table 2 \"n/a\" / \"†\" 标记分散（R1）\n- Figure 1 面板注释 6-7pt 偏小（R1, 视觉审查）\n- §3.2 Eq.1 Soft Jaccard 分母 max vs union 选择理由（R1, R2）\n- Appendix Z 缺 degeneracy > 70% fallback（R1, R2）\n- F1 变体和术语命名不一致（R2-W4, R1 AGREE）\n- Figure 2 灰度打印可读性弱（R2）\n- §6.3 decomposition 正文缺 intuitive explanation（R2）\n- Limitations section 偏长（R2）\n\n## Reviewer Consensus\n\n两位 Reviewer 在以下关键问题上达成共识：\n1. ✅ By-construction gap 需分层叙事（R1-N1 + R2-N1: AGREE）\n2. ✅ §5.1/§5.3 未完成工作不应在 ARR 提交（R2-N2: R1 AGREE）\n3. ✅ Cross-dataset null 结论 underpowered（R1-N2: R2 AGREE）\n4. ✅ SciERC p_adj=0.20 不显著限制 generalizability（R1-W1: R2 AGREE 并加强）\n5. ✅ k=57 family 需透明化（R1-W2: R2 AGREE）\n6. ✅ 72B comparison confounded（R1-W3: R2 AGREE）\n7. ✅ Entity-wise independence 需验证（R1-W5: R2 AGREE）\n8. ✅ 缺 Self-Certainty/P(True) 实质性讨论（R2-W2: R1 AGREE）\n9. ✅ Yao et al. 差异化不足（R2-W3: R1 AGREE）\n10. ✅ 术语不一致（R2-W4: R1 AGREE）\n\n## Reviewer Divergence\n\n1. **Entity construction 贡献度**: R2 判 critical（增量过小，MBR 直接应用），R1 REBUT（34% oracle gap, MBR 理论贡献独立）。Director 判断：作为诊断副产品合理，不应作为核心卖点。\n2. **附录长度**: R2 认为 30 页暗示 scope 过大，R1 REBUT（诊断性论文附录长正常，问题在于引用未完成内容）。\n3. **Degeneracy bound 价值**: R1 认为预测能力极弱，R2 认为 diagnostic 价值仍在。两者对 bound 实用性期望不同，但都同意需明确定位。\n\n## Questions for Authors\n\n1. 能否量化 correlation-selection gap 中 definitional（instance-level by design）vs empirical（LP compression）的比例？\n2. Cross-dataset analysis (n=23) 的 post-hoc power 是多少？80% power 下可检测的最小 ρ？\n3. Holm-Bonferroni k=57 的 57 个检验具体构成？\n4. Entity-wise independence（Proposition 1）在嵌套实体和 fine-grained types 上的近似程度？\n5. §5.1/§5.3 完整实验何时完成？若来不及，是否移至 Future Work？\n6. Appendix M 的 RE 结果是否意味着框架是 NER-specific 的？\n7. Self-Certainty 在 constrained decoding 下是否可用？与 entity construction 的优势对比？\n8. LP compression 的机制成因？是否尝试过 per-entity LP？\n9. Free-form decoding 下 LP selection 更有效（Appendix O）——为何不在正文 highlight？\n10. Trained verifier AUROC=0.987 但 selection 增益仅 +4.23pp——这是否是最有冲击力的 finding？\n\n## Missing References\n\n两位 Reviewer 共同建议：\n- Malinin and Gales (2021) — structured prediction 中 predictive uncertainty\n- Xiong et al. (2024) — uncertainty quantification survey\n\nR1 额外建议：\n- Gleave and Irving (2022) — reward model overoptimization\n\nR2 额外建议：\n- EL4NER (arXiv:2505.23038) — multi-LLM ensemble for NER\n- Structure-Conditional MBR (EMNLP 2025) — MBR for structured outputs\n- Self-Certainty for Best-of-N (arXiv:2502.18581) — per-sample signal\n- G2: Guided Generation for Diversity (arXiv:2511.00432)\n\nR2 引用审计：4 条未通过在线验证，3 条元数据不匹配，17 条 orphan bib entries（详见 W13）。\n\n## External Review\n\n外部审稿：未启用（项目配置中 `external_review.paperreview_ai.enabled` 未设置）。\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成（2026-05-20 12:47–12:50）。发现 1 critical + 4 warning + 9 info：\n\n**Critical:**\n- **Page 31**: Figure 10 是文字占位符（\"[Figure placeholder: Oracle F1 (N) scaling curves]...\"），未渲染实际图表。审稿人会立即判断论文未完成。\n\n**Warning:**\n- **Page 1-2**: 连续 2 页纯文本（Abstract + Introduction + Background），首个 display item（Figure 1）直到第 3 页才出现。前 25% 无视觉支撑。\n- **Page 5**: 又一个纯文本页（§5 + §6），与 p1-2 形成不均匀节奏。\n- **Page 7**: Tables 3, 4, 5 + Figure 3 同页过度拥挤，Figure 3 被挤压。\n- **Page 7**: Figure 3 尺寸过小，坐标轴标签接近可读性下限。\n\n**Info:** Figure 1 面板注释 6-7pt; Figure 2 颜色区分度好; Table 1 booktabs 规范; 主体 9 个 display items 密度合理; 附录 25 页 thoroughness 好; 参考文献格式统一无未解析引用; Figure 6 热力图色阶对色盲不友好; Figure 7 偏小但附录可接受。\n\n## Overall Assessment\n\n### 综合评分\n\n| 维度 | R1 | R2 | 综合 |\n|------|----|----|------|\n| Soundness | 3.5/5 | 3.5/5 | **3.5/5** |\n| Excitement | 3/5 | 3/5 | **3/5** |\n| Reproducibility | 4/5 | 4/5 | **4/5** |\n| Overall | 3.5 | 3.5 | **3.5 (Borderline Conference)** |\n| Confidence | 4/5 | 4/5 | 4/5 |\n\n### Overall Assessment: 3.5 — Borderline Conference\n\n这是一篇执行质量很高的诊断性论文。QE vs. selection 的正交分解是有价值的概念贡献，统计处理在 NLP 论文中属上乘，28 页 appendix 展现了极强的 due diligence。\n\n**三个必须解决的核心问题：**\n\n1. **叙事诚信**: Correlation-selection gap 的 4/5 是 definitional 而非 empirical finding，论文 framing 制造了虚假 surprise。需明确分层：definitional gap → empirical gap（LP compression, governing factors）。\n\n2. **统计效力不足**: Cross-dataset null 结论基于 n=23 underpowered 分析；SciERC 核心结果 p_adj=0.20 未过多重检验；4 个数据集中仅 1 个 entity construction 增益显著。\n\n3. **未完成内容**: §5.1 \"preliminary\" + §5.3 \"ongoing\" 在 ARR 提交中不可接受；Appendix Figure 10 是文字占位符。\n\n**Rebuttal 关键路径：**\n- (a) 重构叙事分离 definitional vs. empirical gap\n- (b) 删除 §5.3，§5.1 补完或移至 Future Work\n- (c) 补充 power analysis，软化 null 结论措辞\n- (d) 替换 Figure 10 占位符\n- (e) 增加 SciERC seeds 或坦承 entity construction 仅在 Few-NERD 显著\n\n若 (a)-(d) 在 rebuttal 期间完成，论文有望升至 4.0 (Conference)。\n\n## Detailed Comments\n\n### §1 Introduction\n- 收紧 structured prediction/structured IE 叙事为 NER-specific（R2-N1）\n- 将 \"surprising finding\" 框定改为 \"systematic characterization\"（R1-N1, R2-N1）\n\n### §2 Related Work\n- 增加与 Yao et al. (2026) 的 head-to-head 段落（R2-W3, R1 AGREE）\n- 讨论 process reward models、self-refinement、diverse beam search（R2-W3）\n- Self-Certainty/P(True) 概念性讨论（R2-W2, R1 AGREE）\n\n### §3 Methodology\n- Eq.1 Soft Jaccard 分母 max vs union 选择理由（R1, R2）\n- 术语统一：F1 变体、signal 缩写（R2-W4, R1 AGREE）\n\n### §4 Diagnostic Framework\n- 首段明确区分 definitional gap 和 empirical gap（R1-N1, R2-N1 核心修改点）\n- LP compression 与 LLM 校准文献对接（R2-W1）\n\n### §5 Adaptive Methods\n- 删除 §5.3 SCD（R2-N2, R1 AGREE）\n- §5.1 补完或降级（R2-N2, R1 AGREE）\n- §5.2 Trained Verifiers 保留\n\n### §6 Theory\n- Proposition 1 entity-wise independence 需验证或讨论（R1-W5, R2 AGREE）\n- §6.2 scaling 结论 hedge confounded comparison（R1-W3, R2 AGREE）\n- §6.3 bound 明确为 diagnostic 而非 predictive（R1-W6, R2 PARTIAL AGREE）\n- 三因素改为 cascade 叙事（R2-W2）\n\n### §7 Experiments\n- §7.3 cross-dataset null 结论加 power analysis 和 hedging（R1-N2, R2 AGREE）\n- §7.5 SciERC p_adj=0.20 更醒目标注（R1-W1, R2 AGREE）\n- k=57 family 明细（R1-W2, R2 AGREE）\n- 考虑提升 trained verifier gap-persists finding 到正文（R2 Q4）\n\n### Appendix\n- Figure 10 占位符必须替换（视觉审查 critical）\n- N-scaling 与 D(N)/bound(N) 联系（R2-W5）\n- §Z 增加 degeneracy > 70% fallback（R1, R2）\n- 清理 orphan bib + 核实引用问题（R2-W4）",
  "project": "struct_self_consist_ie",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.5 - Borderline Conference",
  "review_chat_id": "oc_3897c2857f11615119e277e820eae311"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# Round 25 审稿报告\n\n**论文**: \"Strong Predictors, Weak Selectors: Addressing the Correlation-Selection Gap in Self-Consistency for Named Entity Recognition\"\n**Venue**: EMNLP 2026 Long Paper (ARR May 2026)\n**Reviewers**: R1（方法严谨性 + 实验设计 + 统计分析）, R2（新颖性 + 完整性 + 写作质量）\n**日期**: 2026-05-20\n\n---\n\n## Summary\n\n本文研究自一致性（self-consistency）在 NER 中的失效机制。作者构建包含五种置信度信号（SJ, VC, FK, EM, LP）的诊断框架，在四个 NER 基准上系统评估质量估计与样本选择两个维度，发现所有信号均能可靠估计生成质量（ρ up to 0.45, AUROC up to 0.82）但无法有效执行样本选择——即\"correlation-selection gap\"。论文识别三种结构性故障模式（instance degeneracy、isolated headroom、LP compression），提出 entity-level construction（形式化为 MBR decoding）部分弥合该差距（Few-NERD +1.40pp, SciERC +1.02pp），并给出退化分解上界。\n\n## Strengths\n\n**S1. QE vs. selection 的正交分解是最有概念价值的贡献。** 将 test-time scaling 分解为\"能否判断好坏\"和\"能否据此选出好的\"两个可独立评估的维度，结构清晰可操作。五种信号跨四个 NER 基准的全面评估提供了比现有文献更细粒度的理解。（两位 Reviewer 共识）\n\n**S2. 统计处理水准在 NLP 论文中属上乘。** Bootstrap CI（Table 13）、Holm-Bonferroni 多重检验校正（k=57）、TOST 等价性检验（Table 16, Appendix F）、permutation tests（Table 9），不显著结果如实报告（SciERC p_adj=0.20）。（两位 Reviewer 共识，特别认可）\n\n**S3. Entity construction 与 MBR 的形式化联系。** Proposition 1（§6.1）将 entity-level majority vote 推导为 MBR decoding with balanced set-overlaps，提供清晰的决策论基础。\n\n**S4. 极其详尽的补充材料。** 28 页 appendix 覆盖 N-scaling、temperature、seed stability、per-entity-type analysis、free-form decoding ablation、cross-dataset OOD 等。在 NLP 论文中罕见的 thoroughness。\n\n**S5. 实用的诊断协议。** §Z 的三步协议为从业者提供可直接使用的工作流。\n\n## Weaknesses\n\n### 两位 Reviewer 共识的 Must-Fix 问题\n\n**[CONSENSUS CRITICAL] W1. Correlation-selection gap 的 by-construction 成分未区分**\n- R1-N1 + R2-N1。4/5 信号（SJ, VC, FK, EM）是 instance-level 的，§3.1 已明确定义其对 N 个候选打相同分数——selection 失效是定义推论而非经验发现。论文将五种信号的 gap 统一呈现为需要\"diagnose\"的\"surprising finding\"，夸大了经验性成分。唯一具备 per-sample discrimination 的 LP 确实展现了部分 selection 能力但被 compression 限制。\n- **交叉共识**: R2 认为这是 tautology 层面的过度宣传；R1 认为 LP 分析和 governing factors 的 empirical 贡献被 R2 略微低估。两位均同意需明确区分 definitional gap 和 empirical gap。\n- **历史**: 此问题自 Round 23 持续存在（R23-N2, in_progress），本轮两位 Reviewer 再次独立提出。\n- **建议**: §4 首段明确区分 definitional gap（instance-level signals by design cannot select）和 empirical gap（LP has per-sample discriminability but compression limits effectiveness）。重新校准 Abstract/Intro 叙事，移除对 instance-level signals 的 \"surprising\"/\"diagnose\" 框定。\n\n**[CONSENSUS CRITICAL] W2. Cross-dataset 分析（n=23, ρ=0.052, p=0.81）严重 underpowered**\n- R1-N2 (critical) + R2 交叉 AGREE。23 个 configurations 的 statistical power 极低：检测 ρ=0.3 at α=0.05, 80% power 需要 n≈85；当前 power 仅约 50%（for ρ=0.4）。\"Degeneracy does not predict LP gain\" 的 null 结论不可靠。\n- R2 补充：decomposition 的数学有效性不依赖此 null finding，但 degeneracy 的 interpretive status（diagnostic indicator vs. predictive variable）受影响。\n- **建议**: (1) 报告 post-hoc power analysis，明确可检测的最小 ρ；(2) 将结论从\"does not predict\"改为\"we did not find evidence for prediction, but the analysis is underpowered (n=23)\"；(3) 如有可能增加 configurations。\n\n**[CONSENSUS CRITICAL] W3. §5.1/§5.3 包含未完成工作**\n- R2-N2 (critical) + R1 AGREE。§5.1 Cross-Model SC 标注\"preliminary\"（仅 SciERC 一个数据集初步结果 +0.12pp）；§5.3 SCD 标注\"ongoing\"且完全无实验结果。ARR 提交 incomplete work 会被 AC 视为 premature。\n- R1 纠正 R2 的节号：实际为 §5.3（非 §5.2），§5.2 Trained Verifiers 有完整实验（AUC=0.923±0.002）可保留。\n- **建议**: 删除 §5.3 全部内容，§5.1 要么补完（多数据集多模型组合）要么降级为 Discussion/Future Work。\n\n### 存在分歧的问题\n\n**[DIVERGENCE] W4. Entity construction 贡献度**\n- **R2 判 critical** (N3): entity construction = Florian et al. (2003) entity voting + LP weighting，增量仅 +1.0-1.4pp vs greedy，LP-weighted vs uniform 差异 0.15-0.35pp，新颖性有限，作为独立贡献过弱。\n- **R1 REBUT**: 参照基准应为 greedy 而非 uniform weighting；Few-NERD 恢复 ~34% oracle gap（非 R2 估的 25%）；MBR 形式化（Proposition 1）有独立理论贡献；无需训练的 unsupervised 方法在 selection 大面积失败的背景下有方法论价值。\n- **Director 判断**: 作为独立方法贡献确实增量性较强，但作为诊断框架的 proof-of-concept 合理。R24 已将其从\"principled resolution\"降级为\"diagnostic-motivated mitigation\"，这一定位正确，不应再作为核心卖点。\n\n### 两位 Reviewer 共识的 Should-Fix 问题\n\n**[CONSENSUS WARNING] W5. SciERC entity construction p_adj=0.20 不显著；仅 1/4 数据集显著**\n- R1-W1 + R2 AGREE 并加强。Few-NERD +1.40pp 显著，但 SciERC +1.02pp 校正后 p_adj=0.20 不显著；CoNLL 增益为负（−0.29pp）。4 个数据集中仅 Few-NERD 显著。\n- **建议**: 正文更醒目标注 SciERC p_adj=0.20，讨论仅 1/4 显著的适用范围含义。\n\n**[CONSENSUS WARNING] W6. k=57 Holm-Bonferroni family 定义不透明**\n- R1-W2 + R2 AGREE。57 个检验的构成从未说明。Family 定义直接影响校正严格程度。\n- **建议**: Appendix 列出构成规则或完整明细。\n\n**[CONSENSUS WARNING] W7. 72B zero-shot vs 8B fine-tuned 三因素混淆**\n- R1-W3 + R2 AGREE。同时变化 scale + training regime + quantization，但 §6.2 从中得出 scaling 结论。Limitations 已坦承但正文未 hedge。\n- **建议**: §6.2 结论明确标注 confounded comparison。\n\n**[CONSENSUS WARNING] W8. Seed 数量偏少（SciERC 2-seed, 主要结果 3 seeds）**\n- R1-W4 + R2 PARTIAL AGREE。SciERC n=529 高方差任务 2-3 seeds 效力有限。R2 认为 Appendix H 的 signal ranking stability 部分回应此 concern。\n- **建议**: 对 SciERC entity construction 核心结果增加到 5 seeds。\n\n**[CONSENSUS WARNING] W9. Proposition 1 entity-wise independence 假设未验证**\n- R1-W5 + R2 AGREE。NER 中 entities 间有强依赖（嵌套实体、句法约束、竞争标注）。R2 补充 degenerate subsets 上 entity construction 失效可能正是 independence violation 导致。\n- **建议**: 提供经验验证或讨论违反程度。\n\n**[CONSENSUS WARNING] W10. Degeneracy bound 极度松弛（实际恢复率 3-12%）**\n- R1-W6 + R2 PARTIAL AGREE。R1 认为预测能力极弱；R2 认为 diagnostic 价值仍在（识别 α 为 bottleneck）。两者同意需明确定位。\n- **建议**: 明确 bound 为 diagnostic（识别 bottleneck）而非 predictive，讨论 tightening 方向。\n\n**[CONSENSUS WARNING] W11. 缺 API 模型和 Self-Certainty/P(True) per-sample signals**\n- R2-W1 + R2-W2, R1 均 AGREE。scope 限于 open-weight models（LP 在 API 场景不可用）；Self-Certainty/P(True) 未测试但理论上可绕过 selection gap。\n- **建议**: Limitations 明确声明 scope 限于 open-weight；Related Work/Discussion 实质性讨论 per-sample confidence 方法。\n\n**[R2 UNIQUE] W12. NER-only 实验无法支撑 \"structured prediction\" framing**\n- R2-N1。Abstract/Intro 叙事推广到 structured prediction，但仅有 NER 实验。Appendix M RE 结果显示 structural signals 在 RE 上接近零——直接挑战框架的通用性。\n- **建议**: 严格限定叙事为 NER，或将 RE 结果提升到正文讨论局限性。\n\n**[R2 UNIQUE] W13. 引用质量问题**\n- R2-W4。4 条引用未通过 OpenAlex 验证（hobelsberger2025, lightman2024, venktesh2025, aggarwal2023），3 条实质性元数据不匹配，17 条 orphan bib entries。\n\n**[CONSENSUS WARNING] W14. 与 Yao et al. (2026) 差异化不足**\n- R2-W3, R1 AGREE with nuance。两篇论文 high-level finding 重叠，需 head-to-head 对比段落。\n\n### 其他 Should-Fix (R2 独有)\n- **W15. LP compression 缺与 LLM 校准文献的机制性对接**（R2-W1）\n- **W16. 三种故障模式呈 cascade 而非正交关系**（R2-W2）——应重构为 diagnostic cascade\n- **W17. Related work 缺 process reward models / self-refinement / diverse beam search 讨论**（R2-W3）\n- **W18. N-scaling 分析未与 degeneracy decomposition 联系（D(N), bound(N)）**（R2-W5）\n\n### 小问题（不影响接收）\n- Table 2 \"n/a\" / \"†\" 标记分散（R1）\n- Figure 1 面板注释 6-7pt 偏小（R1, 视觉审查）\n- §3.2 Eq.1 Soft Jaccard 分母 max vs union 选择理由（R1, R2）\n- Appendix Z 缺 degeneracy > 70% fallback（R1, R2）\n- F1 变体和术语命名不一致（R2-W4, R1 AGREE）\n- Figure 2 灰度打印可读性弱（R2）\n- §6.3 decomposition 正文缺 intuitive explanation（R2）\n- Limitations section 偏长（R2）\n\n## Reviewer Consensus\n\n两位 Reviewer 在以下关键问题上达成共识：\n1. ✅ By-construction gap 需分层叙事（R1-N1 + R2-N1: AGREE）\n2. ✅ §5.1/§5.3 未完成工作不应在 ARR 提交（R2-N2: R1 AGREE）\n3. ✅ Cross-dataset null 结论 underpowered（R1-N2: R2 AGREE）\n4. ✅ SciERC p_adj=0.20 不显著限制 generalizability（R1-W1: R2 AGREE 并加强）\n5. ✅ k=57 family 需透明化（R1-W2: R2 AGREE）\n6. ✅ 72B comparison confounded（R1-W3: R2 AGREE）\n7. ✅ Entity-wise independence 需验证（R1-W5: R2 AGREE）\n8. ✅ 缺 Self-Certainty/P(True) 实质性讨论（R2-W2: R1 AGREE）\n9. ✅ Yao et al. 差异化不足（R2-W3: R1 AGREE）\n10. ✅ 术语不一致（R2-W4: R1 AGREE）\n\n## Reviewer Divergence\n\n1. **Entity construction 贡献度**: R2 判 critical（增量过小，MBR 直接应用），R1 REBUT（34% oracle gap, MBR 理论贡献独立）。Director 判断：作为诊断副产品合理，不应作为核心卖点。\n2. **附录长度**: R2 认为 30 页暗示 scope 过大，R1 REBUT（诊断性论文附录长正常，问题在于引用未完成内容）。\n3. **Degeneracy bound 价值**: R1 认为预测能力极弱，R2 认为 diagnostic 价值仍在。两者对 bound 实用性期望不同，但都同意需明确定位。\n\n## Questions for Authors\n\n1. 能否量化 correlation-selection gap 中 definitional（instance-level by design）vs empirical（LP compression）的比例？\n2. Cross-dataset analysis (n=23) 的 post-hoc power 是多少？80% power 下可检测的最小 ρ？\n3. Holm-Bonferroni k=57 的 57 个检验具体构成？\n4. Entity-wise independence（Proposition 1）在嵌套实体和 fine-grained types 上的近似程度？\n5. §5.1/§5.3 完整实验何时完成？若来不及，是否移至 Future Work？\n6. Appendix M 的 RE 结果是否意味着框架是 NER-specific 的？\n7. Self-Certainty 在 constrained decoding 下是否可用？与 entity construction 的优势对比？\n8. LP compression 的机制成因？是否尝试过 per-entity LP？\n9. Free-form decoding 下 LP selection 更有效（Appendix O）——为何不在正文 highlight？\n10. Trained verifier AUROC=0.987 但 selection 增益仅 +4.23pp——这是否是最有冲击力的 finding？\n\n## Missing References\n\n两位 Reviewer 共同建议：\n- Malinin and Gales (2021) — structured prediction 中 predictive uncertainty\n- Xiong et al. (2024) — uncertainty quantification survey\n\nR1 额外建议：\n- Gleave and Irving (2022) — reward model overoptimization\n\nR2 额外建议：\n- EL4NER (arXiv:2505.23038) — multi-LLM ensemble for NER\n- Structure-Conditional MBR (EMNLP 2025) — MBR for structured outputs\n- Self-Certainty for Best-of-N (arXiv:2502.18581) — per-sample signal\n- G2: Guided Generation for Diversity (arXiv:2511.00432)\n\nR2 引用审计：4 条未通过在线验证，3 条元数据不匹配，17 条 orphan bib entries（详见 W13）。\n\n## External Review\n\n外部审稿：未启用（项目配置中 `external_review.paperreview_ai.enabled` 未设置）。\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成（2026-05-20 12:47–12:50）。发现 1 critical + 4 warning + 9 info：\n\n**Critical:**\n- **Page 31**: Figure 10 是文字占位符（\"[Figure placeholder: Oracle F1 (N) scaling curves]...\"），未渲染实际图表。审稿人会立即判断论文未完成。\n\n**Warning:**\n- **Page 1-2**: 连续 2 页纯文本（Abstract + Introduction + Background），首个 display item（Figure 1）直到第 3 页才出现。前 25% 无视觉支撑。\n- **Page 5**: 又一个纯文本页（§5 + §6），与 p1-2 形成不均匀节奏。\n- **Page 7**: Tables 3, 4, 5 + Figure 3 同页过度拥挤，Figure 3 被挤压。\n- **Page 7**: Figure 3 尺寸过小，坐标轴标签接近可读性下限。\n\n**Info:** Figure 1 面板注释 6-7pt; Figure 2 颜色区分度好; Table 1 booktabs 规范; 主体 9 个 display items 密度合理; 附录 25 页 thoroughness 好; 参考文献格式统一无未解析引用; Figure 6 热力图色阶对色盲不友好; Figure 7 偏小但附录可接受。\n\n## Overall Assessment\n\n### 综合评分\n\n| 维度 | R1 | R2 | 综合 |\n|------|----|----|------|\n| Soundness | 3.5/5 | 3.5/5 | **3.5/5** |\n| Excitement | 3/5 | 3/5 | **3/5** |\n| Reproducibility | 4/5 | 4/5 | **4/5** |\n| Overall | 3.5 | 3.5 | **3.5 (Borderline Conference)** |\n| Confidence | 4/5 | 4/5 | 4/5 |\n\n### Overall Assessment: 3.5 — Borderline Conference\n\n这是一篇执行质量很高的诊断性论文。QE vs. selection 的正交分解是有价值的概念贡献，统计处理在 NLP 论文中属上乘，28 页 appendix 展现了极强的 due diligence。\n\n**三个必须解决的核心问题：**\n\n1. **叙事诚信**: Correlation-selection gap 的 4/5 是 definitional 而非 empirical finding，论文 framing 制造了虚假 surprise。需明确分层：definitional gap → empirical gap（LP compression, governing factors）。\n\n2. **统计效力不足**: Cross-dataset null 结论基于 n=23 underpowered 分析；SciERC 核心结果 p_adj=0.20 未过多重检验；4 个数据集中仅 1 个 entity construction 增益显著。\n\n3. **未完成内容**: §5.1 \"preliminary\" + §5.3 \"ongoing\" 在 ARR 提交中不可接受；Appendix Figure 10 是文字占位符。\n\n**Rebuttal 关键路径：**\n- (a) 重构叙事分离 definitional vs. empirical gap\n- (b) 删除 §5.3，§5.1 补完或移至 Future Work\n- (c) 补充 power analysis，软化 null 结论措辞\n- (d) 替换 Figure 10 占位符\n- (e) 增加 SciERC seeds 或坦承 entity construction 仅在 Few-NERD 显著\n\n若 (a)-(d) 在 rebuttal 期间完成，论文有望升至 4.0 (Conference)。\n\n## Detailed Comments\n\n### §1 Introduction\n- 收紧 structured prediction/structured IE 叙事为 NER-specific（R2-N1）\n- 将 \"surprising finding\" 框定改为 \"systematic characterization\"（R1-N1, R2-N1）\n\n### §2 Related Work\n- 增加与 Yao et al. (2026) 的 head-to-head 段落（R2-W3, R1 AGREE）\n- 讨论 process reward models、self-refinement、diverse beam search（R2-W3）\n- Self-Certainty/P(True) 概念性讨论（R2-W2, R1 AGREE）\n\n### §3 Methodology\n- Eq.1 Soft Jaccard 分母 max vs union 选择理由（R1, R2）\n- 术语统一：F1 变体、signal 缩写（R2-W4, R1 AGREE）\n\n### §4 Diagnostic Framework\n- 首段明确区分 definitional gap 和 empirical gap（R1-N1, R2-N1 核心修改点）\n- LP compression 与 LLM 校准文献对接（R2-W1）\n\n### §5 Adaptive Methods\n- 删除 §5.3 SCD（R2-N2, R1 AGREE）\n- §5.1 补完或降级（R2-N2, R1 AGREE）\n- §5.2 Trained Verifiers 保留\n\n### §6 Theory\n- Proposition 1 entity-wise independence 需验证或讨论（R1-W5, R2 AGREE）\n- §6.2 scaling 结论 hedge confounded comparison（R1-W3, R2 AGREE）\n- §6.3 bound 明确为 diagnostic 而非 predictive（R1-W6, R2 PARTIAL AGREE）\n- 三因素改为 cascade 叙事（R2-W2）\n\n### §7 Experiments\n- §7.3 cross-dataset null 结论加 power analysis 和 hedging（R1-N2, R2 AGREE）\n- §7.5 SciERC p_adj=0.20 更醒目标注（R1-W1, R2 AGREE）\n- k=57 family 明细（R1-W2, R2 AGREE）\n- 考虑提升 trained verifier gap-persists finding 到正文（R2 Q4）\n\n### Appendix\n- Figure 10 占位符必须替换（视觉审查 critical）\n- N-scaling 与 D(N)/bound(N) 联系（R2-W5）\n- §Z 增加 degeneracy > 70% fallback（R1, R2）\n- 清理 orphan bib + 核实引用问题（R2-W4）",
    "project": "struct_self_consist_ie",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.5 - Borderline Conference",
    "review_chat_id": "oc_3897c2857f11615119e277e820eae311"
  }
}
```

</details>

---


### Tool result

_source line 2652 · 2026-05-20T13:24:45.318729+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_1b56445332d8ca2b4964b30f300f0e00:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4247
}
```

</details>

---


### Assistant

_source line 2653 · 2026-05-20T13:24:54.842879+00:00_

Round 25 审稿报告已投递。

**审稿结果：3.5 — Borderline Conference**

两位 Reviewer 均给出 3.5，在以下核心问题上达成共识：

1. **[Critical] By-construction gap 叙事**：4/5 信号的 selection 失效是定义推论非经验发现，需在 §4 分层 definitional vs. empirical gap
2. **[Critical] Cross-dataset n=23 underpowered**：null 结论"degeneracy does not predict"统计效力不足，需 power analysis + 措辞软化
3. **[Critical] §5.1/§5.3 未完成工作**：ARR 提交中出现 "preliminary"/"ongoing" 不可接受，需删除或补完
4. **[Critical] Figure 10 占位符**：附录存在未渲染的文字占位符

唯一分歧在 entity construction 贡献度（R2 判增量过小，R1 认为诊断副产品合理）——R24 已正确降级为 diagnostic-motivated mitigation。

Issue tracker 已同步更新（新增 14 条 R25 issues + 更新 4 条历史 issues）。报告已投递至 Research Director。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 201

## Round 201

2 recorded events


### User

_source line 2654 · 2026-05-20T13:24:55.988905+00:00_

[Reviewer 2 审稿结果]:
审稿已完成并提交给 Review Director。

**总结**：

- **Overall Assessment: 3.5 (Borderline Conference)**
- **核心优点**: QE-vs-selection 分解是有价值的概念贡献，统计处理规范，28 页 appendix 展现极强的 due diligence
- **Must-Fix**: (1) 论文声称 structured prediction 通用性但仅有 NER 实验，且 RE 初步证据反向挑战框架可推广性；(2) Entity construction 是 MBR 的直接应用，方法新颖性有限
- **交叉回应 R1**: 对 R1-N1 (by-construction gap) 部分同意——instance-level filtering 的失效有经验内容，不完全是定义推论；对 R1-N2 (underpowered n=23) 完全同意；对 R1-W1-W6 大部分同意并补充了额外证据（如 4/4 数据集中仅 1 个 entity construction 显著、degenerate subsets 上 independence violation 的可能 pathway）

---

[Reviewer 2 审稿意见]:

# Reviewer 2 交叉回应 Reviewer 1（逐条 [AGREE]/[REBUT]）

---

## Must-Fix

### [PARTIAL AGREE] R1-N1: "Correlation-selection gap" 存在 by-construction 成分

R1 的技术观察是正确的：4/5 信号（SJ, VC, FK, EM）是 instance-level 的，§4 开头明确承认 "Four of five signals assign identical scores to all candidates from the same input by construction"，因此它们无法做 per-sample selection 是 definitional 的。

**但我认为 R1 高估了对论文贡献的影响，理由如下：**

1. **Instance-level signals 仍有非 trivial 的 selection pathway**。即使信号不能区分同一 input 的 candidates，仍可用于 instance-level best-of-N filtering——识别出 greedy 可能不可靠的 instances，对其进行 random replacement。论文在 Table 1 中实测了这一策略，结果：LP 在 Few-NERD 上 +1.30pp (p<0.01)，但其余信号即使在 instance-level filtering 上也无显著增益。这不是 by-construction 能推出的结论——一个高 AUROC 的 instance-level quality estimator 预期应能有效 filter，但实际不能。这是 empirical finding。

2. **"Strong predictors, weak selectors" 的反差本身有经验内容**。论文的 title claim 是"好的 quality estimator ≠ 好的 selector"。对 instance-level signals，gap 体现在 instance-level filtering 无效（Table 1）；对 LP，gap 体现在 per-sample selection 受 compression 限制（Figure 8: 63% instances within-instance LP range < 0.041 nat）。两类 gap 有不同的 empirical characterization。

3. **R1 的改进建议 (1)(2) 合理，(3) 可选**。论文确实应在 §4 明确区分 definitional gap 和 empirical gap 两个层次，重写 abstract/intro 以分层呈现。但增加更多 per-sample signals（R1 建议 (3)）属于 future work 而非当前论文的必要修改。

**结论**：gap 不完全是 by-construction——Table 1 的 instance-level filtering 失效和 Figure 8 的 LP compression 都有 empirical 内容——但叙事确实应分层。R1 的修改方向 (1)(2) 应采纳。

---

### [AGREE] R1-N2: Cross-dataset 分析 (n=23) underpowered

完全同意。n=23 检测 ρ=0.3 at α=0.05, 80% power 需要 n≈85；检测 ρ=0.4 需要 n≈47。当前 power 约 50%（for ρ=0.4），不足以支持 "degeneracy does not predict LP gain" 的 null 结论。

补充两点：
1. **该 null finding 的角色可以被降级而不影响核心论点**。Degeneracy decomposition（§6.3）的 upper bound E[ΔF₁] ≤ (1−D)·G_nd 作为数学恒等式无条件成立，不依赖于 degeneracy 是否 predictive。受影响的主要是 degeneracy 的 interpretive status——是 dataset-intrinsic property 还是 actionable predictor。
2. **Figure 3 的可视化本身也暗示了无信号**：23 个点几乎均匀散布，无明显趋势。但如 R1 所言，这可能是 underpowered 的表现而非真正的 null。

R1 的三条建议均应采纳：报告 post-hoc power analysis、软化措辞为 "we did not find evidence"、增加 configurations。

---

## Should-Fix

### [AGREE] R1-W1: SciERC entity construction p_adj=0.20 不显著

完全同意。正文 §7.5 呈现方式 "LP-weighted entity construction yields ... +1.02pp on SciERC" 容易让读者忽略不显著性，p_adj=0.20 仅在括号内出现。

**进一步补充**：结合 CoNLL 上 entity construction 增益为负（Table 6: −0.29pp），**4 个数据集中仅 Few-NERD 的 +1.40pp 通过了 Holm-Bonferroni 校正**。这意味着 entity construction 的显著增益仅在 1/4 数据集上成立，对方法 generalizability 的打击比 R1 描述的"2 个主要数据集中 1 个不显著"更严重。

建议：正文中应将 SciERC p_adj=0.20 和 CoNLL −0.29pp 并列呈现，明确讨论 entity construction 的 applicability conditions（低 degeneracy + 足够 oracle headroom 可能是必要条件，Few-NERD 同时满足而其他数据集不满足）。

---

### [AGREE] R1-W2: k=57 family 定义不透明

完全同意。Family 定义直接影响校正严格程度——如果 k=57 涵盖论文全部统计检验则偏保守（合理），如果仅覆盖 entity construction 相关检验则可能偏宽松。正文 §7.5 仅写 "Holm-Bonferroni at k=57" 但未解释构成。

建议：在 Appendix 中列出 57 个检验的分组构成规则（至少说明是 "所有 pairwise signal comparisons × datasets" 还是 "论文中所有报告的 p-values"），并讨论 family 边界选择的保守/宽松程度。

---

### [AGREE] R1-W3: 72B vs 8B 比较 confounded

同意 confounded comparison 的问题客观存在。Table 2 (p.6) 的对比同时变化了 model scale（8B→72B）、training regime（fine-tuned→zero-shot）、quantization，§6.2 "Scaling Behavior" 的结论 "the gap persists at 72B" 确实过强。

**但有一个缓解因素**：Limitations (p.8) 坦承 "simultaneously varies model family, regime, and quantization, so individual effects cannot be disentangled"。这不是隐瞒而是资源限制下的诚实标注。

建议：§6.2 的 conclusions 应从 "the gap persists at 72B" 改为 "the gap persists under this specific 72B zero-shot configuration, though scale, training regime, and quantization effects are confounded (see Limitations)"。增加 72B fine-tuned 或 8B zero-shot 数据点是理想的但可能超出 rebuttal 资源范围。

---

### [PARTIAL AGREE] R1-W4: Seed 数量偏少（2-3 seeds）

部分同意。3 seeds 是 NLP 实验中的常见实践，但对 SciERC（n=529）这样的小数据集、高方差任务确实有限。

**缓解证据**：
- Appendix H Table 18 的 multi-seed stability 分析显示 signal rankings 在 3 seeds 下稳定（所有信号 σ ≤ 0.025 on selection F1）
- LP 作为最佳 selection 信号的 directional finding 在所有 seeds 下一致
- 3-seed 的 cross-seed standard deviation（Table 33: mean σ = 0.0145 on NER, 0.0114 on RE）表明 seed 间变异较小

**未被缓解的部分**：SciERC entity construction 的 +1.02pp 使用 2-seed mean（Table 6 caption），这确实不够。增加到 5+ seeds 是判断该增益是否 real 的必要步骤，R1 的建议 (§Q6) 合理。

---

### [AGREE] R1-W5: Entity-wise independence 假设未验证

完全同意。Proposition 1（§6.1, Appendix N.1）假设每个 entity 的 inclusion decision 独立于其他 entities。在实际 NER 中，这会被多种因素违反：嵌套实体（SciERC 有大量嵌套的 Task/Method/Material）、同一 span 的竞争标注、type 间的语义约束（如一个 span 不太可能同时是 PER 和 LOC）。

**补充观察**：Appendix V Table 50 显示 entity construction 在 degenerate subsets（所有 N samples yield identical F1）上一致为负（SciERC: −1.57pp, CoNLL: −1.19pp, Few-NERD: −1.13pp）。在这些高退化实例上，所有 samples 高度一致→ entity 间依赖最强→ entity construction 的 entity-wise 拆解最容易引入 spurious entities。这提供了一条 independence violation → method failure 的 empirical pathway，间接佐证了 R1 的 concern。

建议：(1) 测量 entity decisions 间的 conditional dependence（如 entity co-occurrence 的 pointwise mutual information），至少在一个数据集上；(2) 讨论 independence violation 的影响方向——可能导致 entity construction 系统性引入 false positives（当 entities 正相关）或遗漏 co-occurring entities（当 entities 负相关）。

---

### [PARTIAL AGREE] R1-W6: Degeneracy bound 极度松弛（3-12%）

同意 bound 极松（16 个 positive-gain configurations 中实际 SC gain 仅占 upper bound 的 3-12%），predictive power 确实很弱。

**但我对 bound 价值的判断与 R1 不同**：

bound 的核心价值是 **diagnostic** 而非 **predictive**。将 SC 失效分解为 E[ΔF₁] ≤ (1−D)·G_nd：
- **(1−D)** 量化 degeneracy 导致的 ceiling。论文数据：SciERC D=0.70, Few-NERD D=0.13, CoNLL D=0.68（Figure 9, p.27）。(1−D) 告诉我们 degeneracy 吃掉了多少潜在空间。
- **G_nd** 量化非退化实例上的 oracle headroom。
- **Bound loose 因为 α（signal alignment）是真正的瓶颈**（p.6 明确说明）。这本身就是一个有价值的诊断洞察：SC 失效的 primary bottleneck 不是 degeneracy 本身（(1−D) 通常在 0.3-0.6），而是在非退化实例上的信号利用效率。

R1 建议引入 α 的 empirical estimate 来 tighten bound——方向合理但可能需要额外假设（α 的分布形式）。更现实的改进是在论文中明确讨论 bound 的 "diagnostic decomposition" 定位 vs. 读者可能期望的 "predictive bound" 定位，manage expectations。

---

## 总结

| R1 问题 | 判断 | 核心理由 |
|---------|------|---------|
| R1-N1 by-construction gap | PARTIAL AGREE | 技术观察正确，但 Table 1 instance-level filtering 失效有 empirical 内容；叙事应分层 |
| R1-N2 underpowered n=23 | AGREE | 统计分析无争议，需补 power analysis 和软化措辞 |
| R1-W1 SciERC p_adj=0.20 | AGREE | 进一步补充：4 数据集中仅 Few-NERD 1 个显著 |
| R1-W2 k=57 不透明 | AGREE | 需在 appendix 列出构成明细 |
| R1-W3 72B vs 8B confounded | AGREE | Limitations 已坦承，§6.2 结论需更 hedged |
| R1-W4 seed 数量少 | PARTIAL AGREE | Appendix H 显示 signal rankings 稳定，但 SciERC 2-seed 确实不够 |
| R1-W5 independence 未验证 | AGREE | Table 50 degenerate subset 的负增益间接佐证 concern |
| R1-W6 bound 极松 | PARTIAL AGREE | bound 松弛但 diagnostic 价值成立；predictive power 确实弱 |


---

[Reviewer 2 审稿结果]:
已提交。逐条回应如下：

| R1 问题 | 判断 | 核心理由 |
|---------|------|--------|
| **R1-N1** by-construction gap | **PARTIAL AGREE** | 4/5 信号 instance-level 是事实，但 Table 1 的 instance-level filtering 失效有 empirical 内容，gap 并非完全 definitional；叙事应分层区分 |
| **R1-N2** underpowered n=23 | **AGREE** | n=23 power 不足无争议，需补 power analysis 并软化 null 结论措辞 |
| **R1-W1** SciERC p_adj=0.20 | **AGREE** | 进一步补充：4 个数据集中仅 Few-NERD 1 个 entity construction 增益显著，问题比 R1 描述的更严重 |
| **R1-W2** k=57 不透明 | **AGREE** | 需在 appendix 列出 57 个检验的构成明细 |
| **R1-W3** 72B vs 8B confounded | **AGREE** | Limitations 已坦承，但 §6.2 结论需更 hedged |
| **R1-W4** seed 数量少 | **PARTIAL AGREE** | Appendix H 显示 signal rankings 3-seed 稳定，但 SciERC 2-seed mean 确实不够 |
| **R1-W5** independence 未验证 | **AGREE** | 补充：Table 50 degenerate subset 上 entity construction 一致为负，间接佐证 independence violation → method failure 的 pathway |
| **R1-W6** bound 极松 | **PARTIAL AGREE** | bound 松弛但 diagnostic decomposition 价值成立（识别 α 为真正 bottleneck）；predictive power 确实弱 |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 2655 · 2026-05-20T13:25:11.812348+00:00_

Round 25 审稿报告已投递至 Research Director，评分 **3.5 (Borderline Conference)**。

**本轮审稿总结：**

两位 Reviewer 独立初审后完成交叉回应，10 项关键问题达成共识，1 项存在分歧（entity construction 贡献度严重性判定）。无需第二轮。

**三个必须解决的核心问题：**
1. **叙事诚信** — correlation-selection gap 的 4/5 是 definitional 而非 empirical finding，需在 §4 分层区分
2. **统计效力** — cross-dataset null 结论 underpowered (n=23)；SciERC p_adj=0.20 不显著；4 个数据集仅 1 个 entity construction 增益显著
3. **未完成内容** — §5.1 "preliminary" + §5.3 "ongoing" 不可接受；Appendix Figure 10 是文字占位符

Issue Tracker 已同步更新（R25: 3 critical + 12 warning 新增，6 项既有 issue 更新）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 202

## Round 202

74 recorded events


### User

_source line 2656 · 2026-05-20T14:17:36.701942+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: struct_self_consist_ie
- 论文路径: /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: Main Conference (ARR May 2026)
- 截止日期: 2026-05-25

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 2657 · 2026-05-20T14:17:42.856108+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 2658 · 2026-05-20T14:17:42.907278+00:00_

1	---
2	name: review-director-session-start
3	description: Review Director session 启动初始化流程——圆桌多轮审稿协议。Review Director 角色 session 启动时自动使用。
4	priority: 9
5	scope: global
6	tags:
7	- workflow
8	- review
9	- session
10	version: 3
11	roles:
12	- review_director
13	---
14	
15	# Review Director Session 启动流程（圆桌会议模式）
16	
17	## 初始化
18	
19	1. `director_get_project_overview(project)` — 了解研究现状（实验状态、最新报告）
20	2. 读取论文文件状态：检查 `projects/{project}/paper/` 或 `main.tex` 是否存在
21	3. 检查是否有来自 Research Director 的论文提交（`[论文提交]` 消息）
22	4. 向用户简要汇报：
23	   - **投稿目标**：venue 和 deadline
24	   - **论文状态**：当前草稿位置和版本
25	   - **资料完整性**：提交的材料是否齐全
26	   - **下一步**：即将开始的圆桌审稿流程
27	
28	## 评审流程（收到论文提交后执行）
29	
30	### Step 0 — 资料检查 + Venue 调研（必须先做，不可跳过）
31	
32	1. 检查提交资料完整性：论文文件是否存在、是否可读、补充材料是否齐全
33	2. 确认目标投稿 venue（从提交消息中获取）
34	3. 用 `web_search` 搜索该 venue 当前轮次的 CFP（Call for Papers），关键词示例：
35	   - `"&lt;venue name> 2026 call for papers" site:aclweb.org`
36	   - `"&lt;venue name> 2026 submission deadline"`
37	   - `"&lt;venue name> 2026 author guidelines"`
38	4. **验证 deadline 未过期**：今天日期与截止日期对比，若已过期立即通知用户，不继续
39	5. 提取当前版本的格式要求：
40	   - 页数限制（正文 / 附录 / 参考文献）
41	   - 模板（ACL / IEEE / NeurIPS / ICML / ...）
42	   - 匿名规则（double-blind / single-blind / open）
43	   - 附录规则（是否允许、是否参与审稿）
44	   - 引用格式（natbib / biblatex / 特定 .bst）
45	6. 将以上信息作为上下文，随任务一起传递给 Reviewer
46	
47	⚠️ 禁止使用训练知识中的 venue 要求——格式标准每年都会更新，必须实时搜索确认。
48	
49	### Step 0.5 — 决定 Reviewer 编排
50	
51	根据 venue 类型和论文特点，决定：
52	- 需要几个 Reviewer（1-5 人）
53	- 每个 Reviewer 的审查侧重
54	
55	参考：
56	- **顶会长文**（NeurIPS/ICML/ACL）：3 人（方法/实验 + novelty/related work + 格式/ethics）
57	- **一般会议**（EMNLP/NAACL）：2 人（方法严谨性 + 新颖性/完整性）
58	- **Workshop / 短文**：1 人（全面审查）
59	
60	向 Group C（即项目配置中的 `feishu.review_chat_id` 审稿群）汇报编排决定。
61	
62	### Step 0.6 — 外部审稿线（与 Step 1 并行）
63	
64	检查项目配置中 `external_review.paperreview_ai.enabled` 是否为 `true`：
65	- 如果启用：调用 `request_external_review(project, paper_pdf_path, venue)` 向用户群发送协助提交卡片
66	- 这一步与 Step 1（内部 Reviewer 分配）**并行执行**，不阻塞内部审稿流程
67	- 外部结果到达后（用户在群里粘贴），纳入 Step 4 最终报告
68	- 如果到 Ste
…[truncated 3286 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 2659 · 2026-05-20T14:17:48.825714+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,read_project_file,mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,read_project_file,mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 2660 · 2026-05-20T14:17:48.826152+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2661 · 2026-05-20T14:17:49.679395+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 2662 · 2026-05-20T14:17:49.679815+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2663 · 2026-05-20T14:17:50.131073+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__get_visual_check_status",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__get_visual_check_status",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 2664 · 2026-05-20T14:17:50.131490+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2665 · 2026-05-20T14:17:50.583522+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,WebFetch,TodoWrite",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,WebFetch,TodoWrite",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 2666 · 2026-05-20T14:17:50.634607+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 2667 · 2026-05-20T14:17:59.166747+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': '初始化：获取项目概览 + 检查论文文件', 'status': 'in_progress', 'activeForm': '获取项目概览和检查论文文件'}, {'content': 'Step 0: Venue 调研（WebSearch EMNLP 2026 CFP）', 'status': 'pending', 'activeForm': '搜索 EMNLP 2026 CFP 和格式要求'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'pending', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.6/0.7: 派发外部审稿 + 视觉审查', 'status': 'pending', 'activeForm': '派发外部审稿和视觉审查'}, {'content': 'Step 1: Round 1 独立审稿（分配 Reviewer 任务）', 'status': 'pending', 'activeForm': '分配 Reviewer 审稿任务'}, {'content': 'Step 2: 交叉分享', 'status': 'pending', 'activeForm': '交叉分享 Reviewer 意见'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断是否收敛'}, {'content': 'Step 4: 汇总报告 + 投递', 'status': 'pending', 'activeForm': '汇总审稿报告并投递'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': '初始化：获取项目概览 + 检查论文文件', 'status': 'in_progress', 'activeForm': '获取项目概览和检查论文文件'}, {'content': 'Step 0: Venue 调研（WebSearch EMNLP 2026 CFP）', 'status': 'pending', 'activeForm': '搜索 EMNLP 2026 CFP 和格式要求'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'pending', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.6/0.7: 派发外部审稿 + 视觉审查', 'status': 'pending', 'activeForm': '派发外部审稿和视觉审查'}, {'content': 'Step 1: Round 1 独立审稿（分配 Reviewer 任务）', 'status': 'pending', 'activeForm': '分配 Reviewer 审稿任务'}, {'content': 'Step 2: 交叉分享', 'status': 'pending', 'activeForm': '交叉分享 Reviewer 意见'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断是否收敛'}, {'content': 'Step 4: 汇总报告 + 投递', 'status': 'pending', 'activeForm': '汇总审稿报告并投递'}]"
  }
}
```

</details>

---


### Tool result

_source line 2668 · 2026-05-20T14:17:59.167250+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2669 · 2026-05-20T14:18:02.485884+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 2670 · 2026-05-20T14:18:03.898836+00:00_

{"result":"# 项目 struct_self_consist_ie 概况\n\n## 实验状态 (190 个)\n\n- **exp_002_ner_conll2003**: DONE (success) — \n- **exp_004_re_diagnostic**: DONE (success) — \n- **exp_005**: DONE (success) — \n- **exp_014_entity_majority_voting**: DONE (success) — \n- **exp_013_exact_match_voting**: DONE (negative) — \n- **exp_012_logprob_baseline**: DONE (success) — \n- **mvp_pilot_005**: DONE (negative) — \n- **e1_component_wise_re_sj**: DONE (negative) — \n- **mvp_pilot_004**: DONE (negative) — \n- **ft_002_v2**: DONE (success) — \n- **mvp_pilot_002**: DONE (failed) — \n- **ft_002**: DONE (killed) — \n- **ft_001**: DONE (success) — \n- **mvp_pilot_003**: DONE (negative) — \n- **mvp_pilot_001**: DONE (negative) — \n\n## 最新报告\n# Handover — 2026-05-20\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| exp_b1_scd_threshold_ablation | Construction threshold sweep for SCD pseudo-label generation on FewNERD: θ∈{1/N, 2/N, 3/N, 0.5}. Higher θ = more conservative pseudo-labels (higher precision, lower recall). Optimal θ balances pseudo-label quality vs quantity for SCD training effectiveness. | — | — | — |\n| exp_b1_scd_fewnerd_curriculum_q | Q variant SCD with curriculum ordering: use B2 entity verifier confidence to stratify pseudo-labels (conf>0.8→Round1, 0.5-0.8→Round2, conf<0.5→discard). Curriculum by verifier confidence improves SCD convergence and final greedy F1 vs standard flat SCD on FewNERD. | — | — | — |\n| exp_b1_scd_fewnerd_standard | Standard Self-Consistency Distillation on FewNERD: fine-tune Qwen3-8B-FT with theta2n construction pseudo-labels (32,565 instances) mixed 1:1 with gold data. Greedy F1 after SCD should approach N=8 construction F1 (0.764 vs current 0.748). Transductive setting: pseudo-labels from test set SC outputs. | — | — | — |\n\n## 待处理\n- exp_b3_prompted_diversity: Structurally diverse prompt templates (role framing, output format variants, few-shot exemplar diversity) increase in
…[truncated 1741 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1412
}
```

</details>

---


### Tool call

_source line 2671 · 2026-05-20T14:18:04.477413+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex",
  "limit": "120"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex",
    "limit": "120"
  }
}
```

</details>

---


### Tool result

_source line 2672 · 2026-05-20T14:18:04.782952+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{inconsolata}
11	\usepackage{graphicx}
12	\usepackage{booktabs}
13	\usepackage{amsmath}
14	\usepackage{amssymb}
15	\usepackage{amsthm}
16	\newtheorem{proposition}{Proposition}
17	\newtheorem{theorem}{Theorem}
18	\newtheorem{corollary}{Corollary}
19	\newtheorem{definition}{Definition}
20	\usepackage{multirow}
21	\usepackage{xcolor}
22	\usepackage{subcaption}
23	\usepackage{alphalph}
24	
25	\graphicspath{{figures/}}
26	
27	\title{Strong Predictors, Weak Selectors:\\ The Correlation-Selection Gap in Self-Consistency for Named Entity Recognition}
28	
29	\author{Anonymous}
30	
31	\begin{document}
32	\maketitle
33	
34	\input{sections/abstract}
35	\input{sections/introduction}
36	\input{sections/background}
37	\input{sections/diagnostic}
38	\input{sections/single_signal}
39	\input{sections/adaptive}
40	\input{sections/theory}
41	\input{sections/experiments_main}
42	\input{sections/discussion}
43	\input{sections/conclusion}
44	
45	\section*{Limitations}
46	\input{sections/limitations}
47	
48	\section*{Ethics Statement}
49	All experiments use publicly available benchmarks (SciERC, CoNLL-2003, WNUT-17) and open-weight models (Qwen3-8B, Qwen3-4B, LLaMA-3.1-8B).
50	CoNLL-2003 is derived from the Reuters RCV1 corpus, which is available for research purposes under a NIST agreement; we use the standard research distribution.
51	No new human data was collected or annotated for this study.
52	Our findings on signal limitations could inform more reliable deployment of IE systems by guiding practitioners toward appropriate confidence signals for their use case.
53	Code and data will be released upon acceptance at [anonymized URL].
54	
55	\section*{Responsible NLP Research Checklist}
56	\input{sections/checklist}
57	
58	\bibliography{references}
59	
60	\appendix
61	\renewcommand{\the
…[truncated 91 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 305
}
```

</details>

---


### Tool call

_source line 2673 · 2026-05-20T14:18:04.833728+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 2674 · 2026-05-20T14:18:04.884291+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/acl.sty
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/acl_natbib.bst
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/figures/fig_reliability.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/figures/fig_signal_heatmap.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/figures/fig_temperature_robustness.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/figures/fig_length_logprob_scatter.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/figures/fig_lp_range_cdf.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/figures/fig_degeneracy_lp_scatter.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/checklist.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/figures/fig_overview.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/figures/fig_overview.png
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/figures/fig_selection_gap.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/figures/fig_selection_gap.png
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/figures/fig_bound.png
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/theoretical.tex

…[truncated 4944 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2675 · 2026-05-20T14:18:18.214820+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': '初始化：获取项目概览 + 检查论文文件', 'status': 'completed', 'activeForm': '获取项目概览和检查论文文件'}, {'content': 'Step 0: Venue 调研（WebSearch EMNLP 2026 CFP）', 'status': 'in_progress', 'activeForm': '搜索 EMNLP 2026 CFP 和格式要求'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'pending', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.6/0.7: 派发外部审稿 + 视觉审查', 'status': 'pending', 'activeForm': '派发外部审稿和视觉审查'}, {'content': 'Step 1: Round 1 独立审稿（分配 Reviewer 任务）', 'status': 'pending', 'activeForm': '分配 Reviewer 审稿任务'}, {'content': 'Step 2: 交叉分享', 'status': 'pending', 'activeForm': '交叉分享 Reviewer 意见'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断是否收敛'}, {'content': 'Step 4: 汇总报告 + 投递', 'status': 'pending', 'activeForm': '汇总审稿报告并投递'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': '初始化：获取项目概览 + 检查论文文件', 'status': 'completed', 'activeForm': '获取项目概览和检查论文文件'}, {'content': 'Step 0: Venue 调研（WebSearch EMNLP 2026 CFP）', 'status': 'in_progress', 'activeForm': '搜索 EMNLP 2026 CFP 和格式要求'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'pending', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.6/0.7: 派发外部审稿 + 视觉审查', 'status': 'pending', 'activeForm': '派发外部审稿和视觉审查'}, {'content': 'Step 1: Round 1 独立审稿（分配 Reviewer 任务）', 'status': 'pending', 'activeForm': '分配 Reviewer 审稿任务'}, {'content': 'Step 2: 交叉分享', 'status': 'pending', 'activeForm': '交叉分享 Reviewer 意见'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断是否收敛'}, {'content': 'Step 4: 汇总报告 + 投递', 'status': 'pending', 'activeForm': '汇总审稿报告并投递'}]"
  }
}
```

</details>

---


### Tool result

_source line 2676 · 2026-05-20T14:18:18.215342+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2677 · 2026-05-20T14:18:18.666940+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers ARR submission guidelines site:aclweb.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers ARR submission guidelines site:aclweb.org"
  }
}
```

</details>

---


### Tool call

_source line 2678 · 2026-05-20T14:18:19.619934+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 author guidelines submission format page limit"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 author guidelines submission format page limit"
  }
}
```

</details>

---


### Tool call

_source line 2679 · 2026-05-20T14:18:20.322637+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "struct_self_consist_ie",
  "file": "paper_checklist.yaml",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "struct_self_consist_ie",
    "file": "paper_checklist.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 2680 · 2026-05-20T14:18:24.235433+00:00_

Web search results for query: "EMNLP 2026 call for papers ARR submission guidelines site:aclweb.org"

Links: [{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"*SEM 2026: Commitment Link for ARR-Reviewed Papers (Deadline: 10 April 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/sem-2026-commitment-link-arr-reviewed-papers-deadline-10-april-2026"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"The 64th Annual Meeting of the Association for Computational Linguistics - ACL 2026","url":"https://2026.aclweb.org/"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"Call for Papers: The 20th Linguistic Annotation Workshop (LAW XX), co-located with ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-20th-linguistic-annotation-workshop-law-xx-co-located-acl-2026"},{"title":"Jan. 2025 ACL Standing Committee on Peer Review (COPR) Report 1","url":"https://www.aclweb.org/adminwiki/images/9/9e/COPR-5-cycle-report-to-publish.pdf"},{"title":"First Call for Papers – EACL 2026 Student Research Workshop (SRW) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/first-call-papers-eacl-2026-student-research-workshop-srw"}]

I found some relevant information about EMNLP 2
…[truncated 1150 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "elapsed_ms": 5568
}
```

</details>

---


### Tool result

_source line 2681 · 2026-05-20T14:18:27.028525+00:00_

Web search results for query: "ACL Rolling Review 2026 author guidelines submission format page limit"

Links: [{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"Author Guidelines for Student Research Workshop Papers -","url":"https://2026.eacl.org/calls/srw/guidelines/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Paper formatting guidelines - ACLPUB","url":"https://acl-org.github.io/ACLPUB/formatting.html"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"}]

Based on the search results, here's information about ACL Rolling Review 2026 author guidelines:

## Page Limits

Final versions of accepted papers will be given one additional page of content (up to 9 pages for long papers, up to 5 pages for short papers) to address reviewers' comments. This indicates the standard page limits are 8 pages for long papers and 4 pages for short papers.

## Submission Format

The paper follows ACL formatting. There is an official Overleaf template. Note that this template has a [review] setting that must be on for the submission. Additionally, ARR abandons the MS Word Template for conference submissions. The submissions based on the Word template will be desk-rejected starting from March 2026.

## Key Requirements

- Papers must not include autho
…[truncated 636 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "elapsed_ms": 7408
}
```

</details>

---


### Tool result

_source line 2682 · 2026-05-20T14:18:27.029015+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'struct_self_consist_ie'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 6706
}
```

</details>

---


### Tool call

_source line 2683 · 2026-05-20T14:18:31.891985+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "http://aclrollingreview.org/cfp",
  "prompt": "Extract all submission requirements: page limits for long/short papers, formatting requirements, anonymity rules, appendix rules, citation format, deadline info, and any other author guidelines."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebFetch",
  "tool_args": {
    "url": "http://aclrollingreview.org/cfp",
    "prompt": "Extract all submission requirements: page limits for long/short papers, formatting requirements, anonymity rules, appendix rules, citation format, deadline info, and any other author guidelines."
  }
}
```

</details>

---


### Tool call

_source line 2684 · 2026-05-20T14:18:32.795316+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 commitment deadline ARR cycle May 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 commitment deadline ARR cycle May 2026"
  }
}
```

</details>

---


### Tool call

_source line 2685 · 2026-05-20T14:18:33.297961+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "struct_self_consist_ie",
  "file": "writing_plan.yaml",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "struct_self_consist_ie",
    "file": "writing_plan.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 2686 · 2026-05-20T14:18:38.983678+00:00_

# ACL Rolling Review: Submission Requirements Summary

## Page Limits

**Long Papers:**
- Up to 8 pages of content
- Unlimited space for required limitations section and optional ethical considerations
- Unlimited reference pages

**Short Papers:**
- Up to 4 pages of content
- Unlimited space for required limitations section and optional ethical considerations
- Unlimited reference pages

*Papers exceeding length requirements or lacking a limitations section face desk rejection.*

## Formatting Requirements

Submissions must adhere to the official ACL style template and follow "*ACL" formatting guidelines. The template is available on GitHub at acl-org/acl-style-files. Non-compliance with style specifications—including page size, margins, and font sizes—results in automatic rejection without review.

## Anonymity Rules

Authors must remove all identifying information including names and affiliations. Self-citations should be reformatted (e.g., "Smith showed..." rather than "We previously showed..."). Supplementary materials and repository links must also be anonymized. "Links to file hosting services that can track downloads, such as Dropbox, are not allowed." Violations result in desk rejection.

## Appendix Guidelines

Appendices follow the main paper after references and don't count toward page limits. They must maintain anonymization and use double-column formatting. Critical methodological content should appear in the main paper, not appendices, to avoid circumventing page restrictions.

## Citation Format

For concurrent submissions on related topics with overlapping authors, use this format: "Anonymous (2026). Paper title. Under review." Include such anonymized papers as supplementary material.

## Key Deadlines & Submission Process

- Submissions occur every two months via OpenReview.net
- Author registration required within 48 hours post-submission
- Metadata fields remain editable for 48 hours after deadlines

## Additional Critical Requirements

- **Limit
…[truncated 318 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebFetch",
  "elapsed_ms": 7091
}
```

</details>

---


### Tool result

_source line 2687 · 2026-05-20T14:18:39.840251+00:00_

Web search results for query: "EMNLP 2026 commitment deadline ARR cycle May 2026"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"EMNLP 2026 Workshop WiNLP ARR Commitment | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FWorkshop%2FWiNLP_ARR_Commitment"},{"title":"EMNLP 2026 2026 Deadlines — Submission, Rebuttal & Dates | Paperpin | Paperpin","url":"https://www.getpaperpin.com/deadlines/emnlp26"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"emnlp 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=emnlp26"}]

Based on the search results, here is the information about EMNLP 2026 commitment deadline and the ARR cycle in May 2026:

## Key Dates for EMNLP 2026

The ARR submission deadline for long and short papers is May 25, 2026, and the EMNLP commitment deadline is August 2, 2026.

## Important Policy for ARR 2026 May Cycle

For the ARR 2026 May cycle aligned with both EMNLP and AACL, authors must explicitly declare which conference they intend to commit to at submission time, and this choi
…[truncated 683 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "elapsed_ms": 7044
}
```

</details>

---


### Tool result

_source line 2688 · 2026-05-20T14:18:39.891750+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/writing_plan.yaml\", \"content\": \"meta:\\n  venue: EMNLP 2026 Main (via ARR May)\\n  track: main\\n  template: null  # ARR/ACL format — need to download acl2023.sty or latest ARR template\\n  template_note: \\\"No local template found. Worker should download latest ARR LaTeX template from ACL Rolling Review.\\\"\\n  page_limit: 8  # + unlimited references\\n  deadline: 2026-05-25\\n  core_claim: >\\n    Structural consistency signals are the strongest unsupervised quality estimators for LLM-based IE —\\n    entity voting leads ρ (0.38) while EM leads AUROC (0.75), with soft Jaccard as complementary robust signal\\n    (temperature-stable: NER Δρ=0.028; conditional filtering ρ=0.31). A correlation-selection gap means\\n    this does not translate to best-of-N selection — no signal reliably surpasses greedy on either task\\n    (p>0.39, bootstrap). Signal effectiveness is task-difficulty-dependent: easy tasks favor exact-match,\\n    hard tasks favor structural consistency, and SJ strength scales with both sample size (N=8→16 ρ +0.052)\\n    and instance complexity (entity count 6+ ρ=0.55). RE reveals a capability boundary: when compound\\n    error propagation dominates (~44% zero-F1), all signals weaken (ρ=0.134-0.350) — conditional filtering restores\\n    structural signal advantage (SJ ρ=0.31) while logprob collapses (ρ=-0.03).\\n  created_at: 2026-05-14T13:00:00Z\\n  selected_title: \\\"Strong Predictors, Weak Selectors: A Systematic Comparison of Confidence Signals for Test-Time Scaling in Information Extraction\\\"\\n  director_approval: \\\"2026-05-14 approved with modifications: title #2 selected, RE must distinguish joint vs RE-only protocol (D023), 3 tables confirmed (tab_robustness kept), exp_003/exp_007 pending — Director will notify for Patch\\\"\\n  re_protocol_note: \\\"D023: Joint RE SJ ρ=0.267 < FK ρ=0.315; RE-only 
…[truncated 1414 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 6593
}
```

</details>

---


### Tool call

_source line 2689 · 2026-05-20T14:18:46.263373+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://2026.emnlp.org/calls/main_conference_papers/",
  "prompt": "Extract all submission requirements: page limits, formatting, anonymity rules, appendix rules, topics of interest, key dates, and any specific EMNLP 2026 requirements."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://2026.emnlp.org/calls/main_conference_papers/",
    "prompt": "Extract all submission requirements: page limits, formatting, anonymity rules, appendix rules, topics of interest, key dates, and any specific EMNLP 2026 requirements."
  }
}
```

</details>

---


### Tool call

_source line 2690 · 2026-05-20T14:18:46.716862+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 2691 · 2026-05-20T14:18:47.670229+00:00_

1	\begin{abstract}
2	Test-time compute scaling---repeated sampling with selection or aggregation---yields large gains on discrete-answer reasoning and code generation, but named entity recognition (NER) produces \textit{sets} of entities with partial overlap, where standard aggregation mechanisms break down.
3	We evaluate five confidence signals for quality estimation (QE) and sample selection on four NER benchmarks across fine-tuned 4B\textendash 8B and zero-shot 72B models.
4	All signals achieve reliable QE ($\rho$ up to 0.45 on CoNLL-2003, area under the ROC curve [AUROC] up to 0.82), enabling selective prediction ($+5$--$8$\,pp F1 at 80\% coverage).
5	For instance-level selection, log-probability (LP) succeeds only where LP-quality alignment is strong, and gains are absent elsewhere despite large oracle headroom (the \textbf{correlation-selection gap}).
6	We identify a diagnostic cascade---instance degeneracy sets the ceiling on improvement, oracle headroom determines the opportunity, and LP compression limits exploitation---that persists under our 72B zero-shot configuration, providing the first systematic characterization of when test-time scaling succeeds or fails for NER and similar set-valued extraction tasks.
7	The diagnostic motivates entity-level \textit{construction}, adapting entity voting to stochastic sampling: LP-weighted aggregation improves F1 by $+1.40$\,pp on Few-NERD (Holm-adjusted $p{=}0.006$, construction family $k{=}10$) and $+1.02$\,pp on SciERC ($p{=}0.004$, $p_{\text{adj}}{=}0.20$) under fine-tuning. Construction and LP selection are complementary, governed by LP-quality alignment; a degeneracy decomposition confirms that SC gain vanishes when degeneracy exceeds 70\%.
8	\end{abstract}
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 953
}
```

</details>

---


### Tool call

_source line 2692 · 2026-05-20T14:18:47.670560+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 2693 · 2026-05-20T14:18:47.821376+00:00_

1	\section{Introduction}\label{sec:introduction}
2	
3	Test-time compute scaling has emerged as a complement to model scaling \cite{snell2025scaling}: repeated sampling with majority voting \citep{wang2023selfconsistency}, best-of-$N$ with learned verifiers \cite{cobbe2021verifiers, brown2024monkeys}, and extended chain-of-thought \cite{muennighoff2025s1} yield large gains on reasoning and code generation, but the evidence concentrates on tasks with discrete answers or execution-based verification.
4	Named entity recognition (NER) poses a structurally different challenge: the output is a \textit{set} of entities, two samples may extract overlapping but non-identical sets, and there is no obvious majority to vote on.
5	We hypothesize this challenge generalizes to other set-valued extraction tasks (e.g., relation extraction), but verify only NER here.
6	
7	Prior work on confidence estimation for LLM-based IE has conflated \textit{quality estimation} (which inputs does the model handle reliably?) with \textit{sample selection} (which of $N$ outputs is best?).
8	Existing self-consistency methods \cite{wang2023selfconsistency, chen2024usc, taubenfeld2025cisc, kang2025selfcertainty} assume outputs can be grouped by equivalence, an assumption that breaks for entity sets with partial overlap.
9	Unlike \citet{yao2026consistency}, who demonstrate that self-consistency correlates with task accuracy, we provide the first systematic empirical characterization of \textit{when and why} test-time scaling via LP-based selection succeeds or fails for NER, diagnosing degeneracy and compression as the two blocking mechanisms.
10	
11	A key distinction structures our analysis: four of five signals (Soft Jaccard, voting confidence, Fleiss' $\kappa$, exact match) are instance-level aggregates that assign identical scores to all $N$ candidates for a given input; only log-probability (LP) is natively per-sample.
12	All signals achieve reliable quality estimation ($\rho$ up to 0.45, AUROC up t
…[truncated 3912 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 2694 · 2026-05-20T14:18:47.821863+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/background.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/background.tex"
  }
}
```

</details>

---


### Tool result

_source line 2695 · 2026-05-20T14:18:47.872859+00:00_

1	\section{Background \& Related Work}\label{sec:related}
2	
3	\paragraph{Test-time compute scaling.}
4	Test-time compute scaling encompasses three families: (a) extended chain-of-thought reasoning \cite{muennighoff2025s1}, (b) repeated sampling with majority voting (self-consistency; \citealp{wang2023selfconsistency}) and its extensions to free-form text \cite{chen2024usc, thirukovalluru2024atomic, manakul2023selfcheckgpt}, and (c) best-of-$N$ selection via compute-optimal allocation \cite{snell2025scaling, brown2024monkeys}.
5	Reward-free selectors \cite{taubenfeld2025cisc, kang2025selfcertainty, wang2025rankedvoting, oh2026latentsc} and adaptive gating variants \cite{aggarwal2023adaptive, wang2025make, feng2025optimal, kim2026reasc} reduce inference cost; \citet{chen2025twofailures} diagnose failure modes.
6	All target discrete-answer reasoning; structured prediction requires different aggregation mechanisms because degeneracy operates at the entity-set level.
7	
8	\paragraph{Consistency for structured IE.}
9	\citet{yao2026consistency} demonstrate that self-consistency correlates with task accuracy for LLM-based NER/RE, establishing the QE value of consistency signals.
10	Our work addresses the complementary question: \textit{when and why} does this correlation translate into selection or construction gains?
11	We identify degeneracy and LP compression as two mechanisms that prevent strong QE from yielding selection improvements, providing a diagnostic characterization absent from their analysis.
12	CoCoA \cite{vashurin2025cocoa} fuses confidence with consistency; our supervised baseline confirms combination is not the bottleneck (\S\ref{sec:robustness_main}).
13	Earlier work on confidence for structured prediction \cite{culotta2004confidence, mejer2010confidence, fomicheva2020unsupervised} establishes the paradigm we extend to set-valued outputs.
14	Ensemble approaches aggregate predictions from multiple models or prompts \cite{florian2003named, xiao2025el4ner};
…[truncated 3059 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 2696 · 2026-05-20T14:18:51.438033+00:00_

# EMNLP 2026 Submission Requirements Summary

## Page Limits
- **Long papers:** 8 pages (9 pages for camera-ready versions)
- **Short papers:** 4 pages (5 pages for camera-ready versions)

## Formatting & Anonymity
Papers must follow "ARR submission requirements" including two-way anonymized review procedures. Per the policy, "there is no anonymity period requirement."

## Appendices & Supplementary Materials
The CFP permits "optional supplementary materials, appendices, software and data" submissions alongside papers.

## Key Submission Topics
EMNLP welcomes work spanning 25+ areas including machine translation, information extraction, language modeling, LLM agents, ethics/bias, and human-centered NLP.

## Special Theme Track
"New Missions for NLP Research" invites papers addressing progress evaluation, system-level research, scientific understanding of language, data governance, and LLMs as research tools.

## Critical Dates
- **ARR Deadline:** May 25, 2026
- **Reviewer Registration:** May 27, 2026
- **EMNLP Commitment:** August 2, 2026
- **Acceptance Notification:** August 20, 2026
- **Conference:** October 24-29, 2026

## EMNLP-Specific Requirements
Authors must "explicitly declare which conference they intend to commit to at submission time." Dual submissions are prohibited. Author lists cannot be modified during the commitment phase.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebFetch",
  "elapsed_ms": 5174
}
```

</details>

---


### Tool call

_source line 2697 · 2026-05-20T14:18:57.306152+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/diagnostic.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/diagnostic.tex"
  }
}
```

</details>

---


### Tool result

_source line 2698 · 2026-05-20T14:18:57.757793+00:00_

1	\section{Diagnostic Framework}\label{sec:method}
2	
3	\subsection{Problem Formulation}\label{sec:formulation}
4	
5	Given model $\mathcal{M}$ and input $x$, we sample $N$ outputs $\{y_1, \ldots, y_N\}$ at temperature $T > 0$ via constrained decoding \cite{willard2023guided}, where each $y_i$ is an entity set.
6	A \textbf{per-sample signal} $c_{\text{ps}}: (x, y_i) \to \mathbb{R}$ scores each output independently; an \textbf{instance-level signal} $c_{\text{il}}: (x, \{y_i\}_{i=1}^N) \to \mathbb{R}$ produces a single score per input (notation in Appendix~\ref{app:notation}).
7	This distinction is consequential: 4 of 5 signals are instance-level aggregates assigning identical scores to all $N$ candidates.
8	Only LP carries per-sample discriminative power: ensemble optimization assigns LP mean weight $0.78$, with structural signals receiving zero weight (Appendix~\ref{app:supervised_combination}).
9	When LP fails---as in few-shot regimes where LP $\rho{\to}0$ (\S\ref{sec:scaling})---no alternative per-sample signal exists.
10	
11	\subsection{Confidence Signals}\label{sec:signals}
12	
13	Entity matching uses exact span and type match.
14	We evaluate four \textit{consistency signals}---\textit{structural} (Soft Jaccard [SJ], entity voting confidence [VC]) and \textit{surface} (exact match [EM], Fleiss' $\kappa$ [FK])---and log-probability [LP] as the sole \textit{model-internal}, per-sample signal.
15	
16	\paragraph{Log-probability (per-sample).}
17	$c_{\text{lp}}(y_i) = |y_i|^{-1} \sum_{j} \log p_{\mathcal{M}}(t_j \mid t_{<j}, x)$.
18	
19	\paragraph{Soft Jaccard (structural, instance-level).}
20	For samples $y_i, y_j$, we group by type, compute max-weight bipartite matching (Hungarian algorithm, token-level IoU):
21	\begin{equation}\label{eq:sj}
22	\text{SJ}(y_i, y_j) = \frac{\sum_{m \in M} \text{sim}(a_m, b_m)}{\sum_{g} \max(|g_i|, |g_j|)}
23	\end{equation}
24	Instance-level QE averages over all pairs: $c_{\text{sj}}(x) = \binom{N}{2}^{-1} \sum_{i<j} \text{SJ}(y_i, y_
…[truncated 1482 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 2699 · 2026-05-20T14:18:57.758315+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/single_signal.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/single_signal.tex"
  }
}
```

</details>

---


### Tool result

_source line 2700 · 2026-05-20T14:18:58.259721+00:00_

1	\section{Why Single-Signal Selection Fails}\label{sec:selection_gap}
2	
3	\paragraph{Definitional vs.\ empirical.}
4	We decompose the correlation-selection gap into two layers.
5	The first is structural: four of five signals are instance-level aggregates that assign identical scores to all $N$ candidates from a given input (\S\ref{sec:formulation}), so they estimate quality across inputs but cannot rank candidates within an instance---selection failure is a design property, not an empirical finding.
6	The second layer is empirical and constitutes the core diagnostic: LP---the only per-sample signal---suffers compression under constrained decoding, with 60\% of SciERC instances showing within-instance LP range below 0.041 nats (Appendix~\ref{app:logprob_ties}), effectively eliminating the variation needed for sample discrimination. Even where LP varies, selection gains depend on LP-quality alignment rather than degeneracy alone.
7	Cross-instance $\rho$ (Table~\ref{tab:quality_estimation}) is attenuated by varying instance difficulty; within-instance $\rho$ directly measures whether LP discriminates candidates for a fixed input, making it the relevant predictor of selection success.
8	
9	\begin{table}[t]
10	\centering
11	\small
12	\caption{Best-of-$N$ selection (macro F1) on SciERC ($N{=}8$, $T{=}1.0$, 2-seed mean${\pm}\sigma$). LP is per-sample; others use consensus-proximity. $^\dagger$One score per input.}
13	\label{tab:selection}
14	\begin{tabular}{lcc}
15	\toprule
16	Method & NER F1 & $p$ \\
17	\midrule
18	Oracle & $0.775 \pm 0.001$ & --- \\
19	Greedy ($T{=}0$) & $0.645 \pm 0.001$ & --- \\
20	\midrule
21	LP           & $\mathbf{0.647} \pm 0.005$ & .29 \\
22	SJ           & $0.646 \pm 0.002$ & .67 \\
23	FK           & $0.646 \pm 0.001$ & .79 \\
24	EM           & $0.637 \pm 0.001$ & n/a$^\dagger$ \\
25	VC           & $0.623 \pm 0.004$ & n/a$^\dagger$ \\
26	\midrule
27	Random       & $0.610 \pm 0.003$ & --- \\
28	\bottomrule
29	\end{tabular}
30	\end{table}
31	
32	\
…[truncated 2009 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 501
}
```

</details>

---


### Tool call

_source line 2701 · 2026-05-20T14:18:58.260155+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/adaptive.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/adaptive.tex"
  }
}
```

</details>

---


### Tool result

_source line 2702 · 2026-05-20T14:18:58.911813+00:00_

1	\section{Adaptive Methods}\label{sec:adaptive}
2	
3	Since instance-level selection fails (\S\ref{sec:selection_gap}), we present approaches that extract value from multi-sample generation beyond single-signal sample ranking.
4	
5	\subsection{Cross-Model Self-Consistency}\label{sec:cross_model}
6	
7	Diversity from stochastic sampling within a single model is limited by architecture-specific degeneracy (\S\ref{sec:selection_gap}).
8	Mixing samples from architecturally distinct models---which produce complementary error patterns---can partially bypass this bottleneck.
9	
10	In an exploratory extension combining 4 samples each from Qwen3-8B and LLaMA-3.1-8B (both fine-tuned on SciERC), LP-weighted entity construction yields $+0.42$\,pp over pure LLaMA sampling ($p{<}0.001$, 95\% CI $[0.27, 0.58]$; $N{=}8$ total), suggesting cross-architecture diversity can partially compensate for within-model degeneracy.
11	
12	\subsection{Trained Verifiers: High Discrimination, Low Transfer}\label{sec:verifier}
13	
14	A LightGBM entity-level classifier (5 features: agreement count, LP, VC, SJ, FK) achieves AUC${=}0.923{\pm}0.002$ under out-of-fold evaluation, confirming that entity correctness is learnable from the available signals.
15	Yet this discrimination translates poorly to F1: OOF construction yields only $+0.30$\,pp overall, with per-dataset gains of $+1.28$\,pp on SciERC, $+0.55$\,pp on CoNLL, and $+0.02$\,pp on Few-NERD.
16	The near-zero Few-NERD gain despite AUC${>}0.92$ reveals that frequency-based threshold construction (\S\ref{sec:prescriptive}) already captures most of the verifier's signal; SciERC---with low degeneracy and diverse entity-level errors---is the exception where learned discrimination adds value beyond majority vote.
17	Cross-dataset transfer remains negative (B2-v2: $-0.76$\,pp; B2-v3: $-1.02$\,pp on Few-NERD; Appendix~\ref{app:verifier_transfer}), confirming dataset-specific feature mappings.
18	Even a trained discriminator with near-perfect entity cl
…[truncated 312 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 651
}
```

</details>

---


### Tool call

_source line 2703 · 2026-05-20T14:18:58.912182+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/theory.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/theory.tex"
  }
}
```

</details>

---


### Tool result

_source line 2704 · 2026-05-20T14:18:58.962574+00:00_

1	\section{Threshold Regime Analysis}\label{sec:theory_scaling}
2	
3	\subsection{Entity Construction as MBR Decoding}\label{sec:mbr_theory}
4	
5	Following the MBR framework (Appendix~\ref{app:mbr_proof}), entity-level construction selects $\hat{y}_{\textup{MBR}} = \{e \in E_\cup : \hat{p}(e) > \alpha/(\alpha{+}1)\}$ under balanced set-overlap utility; $\alpha{=}1$ recovers the majority-vote threshold $\hat{p}(e) > \tfrac{1}{2}$ used throughout (Proposition~\ref{prop:construction_mbr}).
6	Signal-derived weights $w_i$ yield quality-weighted MBR: $\hat{p}_w(e) = \sum_{i} w_i \, \mathbf{1}[e {\in} y_i] / \sum_{i} w_i$.
7	Weighted MBR improves when $w_i$ correlates with $u(y_i, y^*)$ within instances; when this correlation is weak (LP on SciERC: $\rho{\approx}0.2$; few-shot: \S\ref{sec:scaling}), weighting degrades (\S\ref{sec:prescriptive}).
8	
9	\subsection{Scaling and Inverse Scaling}\label{sec:scaling}
10	
11	Oracle F1 follows $F_1(N) = a - b \cdot N^{-c}$ ($R^2 > 0.999$; Figure~\ref{fig:oracle_scaling}): Few-NERD ($c{\approx}0.61$) scales comparably to reasoning tasks \cite{brown2024monkeys}, while SciERC converges more slowly ($c{\approx}0.35$).
12	The ceiling grows, but confidence-based aggregation recovers ${<}1$\,pp---a persistent aggregation gap.
13	The gap persists across scales: LP $\rho$ drops without fine-tuning, structural signals generalize (Few-NERD VC $\rho{=}0.416$), and degeneracy is model-family-dependent rather than scale-dependent (Qwen2.5: $31.7$--$46.2$\% vs.\ Qwen3: $13.0$\% on Few-NERD; Appendix~\ref{app:cross_scale}).
14	
15	\paragraph{Inverse scaling under adaptive thresholds.}
16	Across methods and configurations, increasing $N$ \textit{decreases} construction F1 in 40 of 58 observed transitions (paired bootstrap, $p{<}0.05$; Appendix~\ref{app:n_scaling}).
17	The threshold $\theta$ controls the severity of the precision-recall trade-off: operating below $\theta{=}\tfrac{1}{2}$ amplifies precision degradation with $N$, while $\theta{\geq}\tfr
…[truncated 1643 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2705 · 2026-05-20T14:19:07.459486+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments_main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments_main.tex"
  }
}
```

</details>

---


### Tool result

_source line 2706 · 2026-05-20T14:19:07.459949+00:00_

1	\section{Experiments}\label{sec:experiments}
2	
3	\subsection{Experimental Setup}\label{sec:setup}
4	
5	\paragraph{Datasets.}
6	We evaluate on four English NER benchmarks spanning a difficulty gradient.
7	\textbf{SciERC} \cite{luan2018scierc} (551 test instances, 6 entity types) is the primary medium-difficulty test bed (${\approx}$65\% F1).
8	\textbf{Few-NERD} \cite{ding2021fewnerd} (INTRA coarse; 37{,}648 instances, 8 entity types, ${\approx}$75\% F1) provides a low-degeneracy contrast where LP selection succeeds (\S\ref{sec:selection_gap}).
9	\textbf{CoNLL-2003} \cite{tjongkimsang2003conll} (3{,}453 test sentences, 4 entity types, ${\approx}$91\% F1) serves as a ceiling-effect control.
10	\textbf{WNUT-17} \cite{derczynski2017wnut} (1{,}287 social media instances, 51\% zero F1) probes the signal-collapse boundary.
11	
12	\paragraph{Models and sampling.}
13	\textbf{Qwen3-8B} and \textbf{LLaMA-3.1-8B-Instruct} are LoRA fine-tuned using LLaMA Factory \cite{zheng2024llamafactory} (Appendix~\ref{app:training}; Few-NERD uses 3 epochs vs.\ 5 for others; Appendix~\ref{app:epoch_confound}).
14	$N{=}8$ samples at $T{=}1.0$ (primary) with vLLM constrained decoding \cite{willard2023guided}; $N{=}16$ for scaling (Appendix~\ref{app:n_scaling}).
15	
16	%% ============================================================
17	\subsection{Quality Estimation Results}\label{sec:qe_results}
18	
19	\begin{table*}[t]
20	\centering
21	\small
22	\caption{NER quality estimation ($\rho$ and AUROC; $N{=}8$, primary seed${=}42$; 3-seed $\sigma{\leq}0.026$ in Table~\ref{tab:multiseed}). AUROC binarizes at per-dataset median F1. Best in \textbf{bold}. RE in Appendix~\ref{app:re_extension}; $N{=}16$ in Table~\ref{tab:robustness}.}
23	\label{tab:quality_estimation}
24	\begin{tabular}{ll cc cc cc}
25	\toprule
26	& & \multicolumn{2}{c}{\textbf{SciERC}} & \multicolumn{2}{c}{\textbf{CoNLL (Qwen)}} & \multicolumn{2}{c}{\textbf{CoNLL (LLaMA)}} \\
27	\cmidrule(lr){3-4} \cmidrule(lr){5-6} \cmidrule(lr){7-8}

…[truncated 8795 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2707 · 2026-05-20T14:19:08.062845+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 2708 · 2026-05-20T14:19:08.063229+00:00_

1	\section{Discussion}\label{sec:discussion}
2	
3	NER exhibits oracle scaling comparable to reasoning ($c{\approx}0.5$; \S\ref{sec:scaling}), but aggregation cannot close the gap: degeneracy (17.8--67.9\%), limited headroom, and LP-quality alignment ($\rho$ 0.043--0.667) constrain it.
4	Temperature disentangles these at $T{=}1.2$ (degeneracy 14.9\%, LP $\rho{=}0.225$; Table~\ref{tab:t_degeneracy}).
5	
6	\paragraph{From diagnosis to practice.}\label{sec:selection_method}
7	Entity-level construction bypasses both failure mechanisms, with gains positive when degeneracy ${<}22$\% and absent when ${>}31$\% (all $p{<}0.01$; Appendix~\ref{app:epoch_confound}). Under 72B few-shot, construction fails yet QE remains effective (SJ $\rho$ 0.29--0.44; Appendix~\ref{app:fs_error}).
8	Alternative strategies (DALS, MBR, DGS) and supervised mixtures fail to beat greedy (Appendix~\ref{app:dals}, \ref{app:supervised_combination}, \ref{app:when_selection_works}).
9	
10	\paragraph{LP compression and calibration.}
11	LP compression connects to broader calibration challenges in fine-tuned LLMs \cite{kadavath2022language, xiong2024verbalized}: teacher-forcing training and constrained decoding compress the LP dynamic range, leaving within-instance variation insufficient for sample discrimination (median LP range 0.041 nats on SciERC; Appendix~\ref{app:logprob_ties}).
12	\citet{yun2025price} observe similar diversity collapse under structured output formats.
13	Potential remedies---per-token LP variance, calibration-aware scoring, or temperature-adjusted LP---remain untested for entity-level ranking.
14	Two per-sample alternatives could bypass the LP compression bottleneck: Self-Certainty \cite{kang2025selfcertainty} derives confidence from consistency of token-level self-evaluation, while P(True) \cite{kadavath2022language} elicits the model's own correctness probability.
15	Both produce per-sample scores without relying on sequence-level log-probabilities; whether they suffer similar compr
…[truncated 75 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2709 · 2026-05-20T14:19:08.314285+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 2710 · 2026-05-20T14:19:08.916687+00:00_

1	\section{Conclusion}\label{sec:conclusion}
2	
3	NER exhibits oracle scaling comparable to reasoning ($c{\approx}0.5$) but aggregation fails: a degeneracy decomposition ($\theta_{\text{crit}}{=}0.70$; \S\ref{sec:theory}) formalizes when SC becomes futile.
4	Entity-level construction partially closes the gap ($+1.40$\,pp Few-NERD, $+1.02$\,pp SciERC); a trained verifier achieves AUC${=}0.92$ but yields only $+0.30$\,pp via OOF construction, with negative cross-dataset transfer---content-aware methods \cite{cobbe2021verifiers} may bridge this.
5	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 602
}
```

</details>

---


### Tool call

_source line 2711 · 2026-05-20T14:19:08.967228+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 2712 · 2026-05-20T14:19:09.017833+00:00_

1	Our evaluation covers four NER datasets; an exploratory RE extension on SciERC is reported in Appendix~\ref{app:re_extension} but generalization to other RE benchmarks remains unvalidated.
2	All experiments use English-language datasets; cross-lingual generalization remains untested.
3	Cross-model consistency results (\S\ref{sec:cross_model}) are limited to one dataset (SciERC) and one model pair (Qwen3-8B + LLaMA-3.1-8B).
4	Entity-level construction assumes the model produces useful partial outputs across samples; when model capability is insufficient (WNUT-17, 51\% F1${=}0$), this precondition fails and construction cannot improve over greedy.
5	We cover 4B\textendash 8B fine-tuned and 72B zero-shot; the gap persists at 72B but behavior with closed-source APIs or 72B fine-tuning is untested.
6	The 72B zero-shot comparison simultaneously varies model family (Qwen3$\to$Qwen2.5), training regime (fine-tuned$\to$zero-shot), and quantization (FP16$\to$AWQ 4-bit); these factors cannot be fully disentangled.
7	Our supervised approaches (DeBERTa verifier, hidden state probes, MLP/RF on signal combinations) all fail to close the oracle gap; whether content-aware verifiers with access to task-specific structure could succeed remains open.
8	
9	We evaluate at $N{=}8$ (primary) and $N{=}16$; behavior at larger sample sizes is unknown (Appendix~\ref{app:n_scaling}).
10	The free-form ablation covers SciERC NER and CoNLL NER with one model; RE free-form results are in Appendix~\ref{app:re_extension}.
11	Qwen3-8B's SciERC checkpoint used empty \texttt{&lt;think>&lt;/think>} blocks; a three-part analysis rules out this confound (Appendix~\ref{app:thinking_token}).
12	LP compression worsens on easy datasets at lower temperature (CoNLL tied fractions reach 95.8\% at $T{=}0.7$); whether reduced temperature translates to selection gains remains untested.
13	We tested verbalized confidence \cite{lin2022teaching, tian2023calibration} as a second per-sample signal; it exhibits severe overcon
…[truncated 2487 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2713 · 2026-05-20T14:19:14.922156+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 2714 · 2026-05-20T14:19:15.475362+00:00_

File content (52287 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 553
}
```

</details>

---


### Tool call

_source line 2715 · 2026-05-20T14:19:15.626232+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "struct_self_consist_ie",
  "file": "decisions.yaml",
  "max_chars": "6000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "struct_self_consist_ie",
    "file": "decisions.yaml",
    "max_chars": "6000"
  }
}
```

</details>

---


### Tool result

_source line 2716 · 2026-05-20T14:19:15.727140+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/decisions.yaml\", \"content\": \"_next_id: 197\\ndecisions:\\n- id: D001\\n  date: 2026-05-14 04:23 UTC\\n  summary: 'MVP 方案: ACE05 上验证 structural consistency vs Fleiss'' Kappa 的 correlation\\n    差异'\\n  rationale: 'PMC12888769 用 surface-level Fleiss'' Kappa 在 zero-shot 模型上得到 ρ=0.20-0.28，我们假设\\n    fine-tuned 模型 + structural consistency (soft Jaccard) 能达到 ρ≥0.40。这是整个论文的基础假设——如果\\n    structural consistency 不能更好地预测准确率，后续的 adaptive gating 无从谈起。Phase 0 pilot 设计: Qwen3-8B\\n    fine-tuned on ACE05, N=8 samples, 200 instances, 对比两种 consistency metric 的 Spearman\\n    ρ。Pass ≥0.40, Fail <0.30。'\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-14 04:27 UTC\\n  summary: 采纳 Reviewer 审查意见，收紧 MVP pass/fail 标准\\n  rationale: 'Reviewer 指出 5 个问题，全部合理采纳：(1) PASS 必须要求 EAE (high-headroom subtask) ρ≥0.40，仅\\n    NER 通过不够（ceiling effect 可能虚高）；(2) MARGINAL 区间加 time-boxed protocol: N=16 追加 +\\n    1天上限；(3) 加 fine-tuning 质量门控 (NER≥73, EAE≥45)，模型不行时先修 fine-tuning；(4) ACE05 今天必须确认；(5)\\n    监控 T=1.0 per-sample F1 分布，>30% F1=0 时追加 T=0.7。'\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-14 04:53 UTC\\n  summary: SciERC RE 替代 ACE05 EAE 作为 MVP high-headroom subtask\\n  rationale: ACE05 需 LDC 许可，用户未确认。SciERC 公开可得，有 NER+RE 两个 subtask。RE base F1 ~47（与\\n    ACE05 EAE ~52 相当），结构复杂度高（entity pair + relation type），headroom 大，是 EAE 的合理替代。PASS\\n    标准更新为 RE ρ≥0.40。需要补实现 RE 的 consistency + evaluation + pipeline 支持。\\n  related_experiments: []\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-14 07:38 UTC\\n  summary: 'Gate 0: NER PASS (60.4%), RE FAIL (33.8%). 执行方案 C——当前模型先跑 pilot + 追训改进版，需修复\\n    RE evaluation'\\n  rationale: RE 33.8% 低于 40% 阈值但不阻塞 pilot：(1) headroom 大，oracle best-of-N 有提升空间；(2)\\n    consistency correlation 不要求高绝对 F1，要求 per-instance variance；(3) 弱模型上验证假设结论更强。但\\n    Reviewer 发
…[truncated 4585 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 2717 · 2026-05-20T14:19:20.191300+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "output_mode": "content",
  "glob": "*.yaml",
  "head_limit": "20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
    "output_mode": "content",
    "glob": "*.yaml",
    "head_limit": "20"
  }
}
```

</details>

---


### Tool result

_source line 2718 · 2026-05-20T14:19:20.644111+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Grep",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 2719 · 2026-05-20T14:19:20.795123+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 2720 · 2026-05-20T14:19:20.845989+00:00_

1	\section{Notation}\label{app:notation}
2	
3	Table~\ref{tab:notation} summarizes the notation used throughout the paper.
4	
5	\begin{table}[h]
6	\centering
7	\small
8	\begin{tabular}{cl}
9	\toprule
10	Symbol & Meaning \\
11	\midrule
12	$\mathcal{M}$ & Language model \\
13	$x$ & Input instance \\
14	$y_i$ & $i$-th stochastic sample \\
15	$N$ & Number of samples \\
16	$T$ & Sampling temperature \\
17	$c(\cdot)$ & Confidence signal \\
18	SJ & Soft Jaccard similarity \\
19	FK & Fleiss' $\kappa$ \\
20	EM & Exact-match voting rate \\
21	VC ($c_{\mathrm{vc}}$) & Entity voting confidence \\
22	LP ($c_{\mathrm{lp}}$) & Log-probability (mean token log-likelihood) \\
23	\bottomrule
24	\end{tabular}
25	\caption{Notation used throughout the paper.}
26	\label{tab:notation}
27	\end{table}
28	
29	\section{Robustness Analysis}\label{app:robustness}
30	
31	We exclude instances with empty gold annotations from all correlation analyses (CoNLL: 697/3{,}453 instances, 20.2\%; SciERC: 22/551, 4.0\%).
32	For these instances, F1 is trivially zero regardless of prediction quality, and consistency signals reflect agreement on the empty set rather than extraction quality. Including them inflates or deflates Spearman $\rho$ depending on signal behavior at the boundary.
33	
34	\begin{table}[t]
35	\centering
36	\small
37	\caption{Signal robustness across configurations (Spearman $\rho$). Top: temperature on Qwen SciERC. Middle: sample size on Qwen SciERC. Bottom: transfer across model families (both 8B) (LLaMA CoNLL $N{=}16$, 3-seed mean $\pm\sigma$). $^\dagger$Mean over 3 seeds ($\sigma{=}0.013$; individual: 0.398, 0.423, 0.410). $\sigma$ computed as sample standard deviation.}
38	\label{tab:robustness}
39	\begin{tabular}{llcc}
40	\toprule
41	& & NER $\rho$ & RE $\rho$ \\
42	\midrule
43	\multicolumn{4}{l}{\textit{Temperature} (Qwen SciERC, $N{=}8$)} \\
44	\quad SJ & $T{=}0.7$ & 0.364 & 0.234 \\
45	\quad SJ & $T{=}1.0$ & 0.360 & 0.250 \\
46	\quad FK & $T{=}0.7$ & 0.289 & 0.184 \\
47	\quad FK & $
…[truncated 4982 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2721 · 2026-05-20T14:19:54.188089+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': '初始化：获取项目概览 + 检查论文文件', 'status': 'completed', 'activeForm': '获取项目概览和检查论文文件'}, {'content': 'Step 0: Venue 调研（WebSearch EMNLP 2026 CFP）', 'status': 'completed', 'activeForm': '搜索 EMNLP 2026 CFP 和格式要求'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.6/0.7: 派发视觉审查 + 分配 Reviewer 任务', 'status': 'in_progress', 'activeForm': '派发视觉审查并分配 Reviewer 任务'}, {'content': 'Step 2: 交叉分享', 'status': 'pending', 'activeForm': '交叉分享 Reviewer 意见'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断是否收敛'}, {'content': 'Step 4: 汇总报告 + 投递', 'status': 'pending', 'activeForm': '汇总审稿报告并投递'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': '初始化：获取项目概览 + 检查论文文件', 'status': 'completed', 'activeForm': '获取项目概览和检查论文文件'}, {'content': 'Step 0: Venue 调研（WebSearch EMNLP 2026 CFP）', 'status': 'completed', 'activeForm': '搜索 EMNLP 2026 CFP 和格式要求'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.6/0.7: 派发视觉审查 + 分配 Reviewer 任务', 'status': 'in_progress', 'activeForm': '派发视觉审查并分配 Reviewer 任务'}, {'content': 'Step 2: 交叉分享', 'status': 'pending', 'activeForm': '交叉分享 Reviewer 意见'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断是否收敛'}, {'content': 'Step 4: 汇总报告 + 投递', 'status': 'pending', 'activeForm': '汇总审稿报告并投递'}]"
  }
}
```

</details>

---


### Tool result

_source line 2722 · 2026-05-20T14:19:54.188631+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2723 · 2026-05-20T14:19:56.515920+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "struct_self_consist_ie",
  "review_chat_id": "oc_3897c2857f11615119e277e820eae311"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "struct_self_consist_ie",
    "review_chat_id": "oc_3897c2857f11615119e277e820eae311"
  }
}
```

</details>

---


### Tool result

_source line 2724 · 2026-05-20T14:20:17.923638+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 21407
}
```

</details>

---


### Tool call

_source line 2725 · 2026-05-20T14:20:18.036372+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "struct_self_consist_ie",
  "text": "## Round 1 审稿任务 — Reviewer 1（方法严谨性 + 实验有效性）\n\n### Venue 信息\n- **目标**: EMNLP 2026 Main Conference (via ARR May 2026)\n- **Deadline**: 2026-05-25\n- **页数限制**: Long paper, 8页正文 + 无限参考文献; Limitations/Ethics 不计页数\n- **模板**: ACL style (`\\usepackage[review]{acl}`)\n- **匿名规则**: Double-blind\n\n### 论文路径\n- LaTeX: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf`\n\n### 论文概要\n\"Strong Predictors, Weak Selectors: The Correlation-Selection Gap in Self-Consistency for Named Entity Recognition\"\n研究 test-time compute scaling (self-consistency) 应用于 NER 的效果。评估 5 种 confidence signals（SJ, VC, FK, EM, LP）在 4 个 NER benchmark 上的 quality estimation 和 sample selection 表现。核心发现：信号能做 QE（ρ up to 0.45, AUROC 0.82）但选不出最好的 sample（correlation-selection gap）。提出 entity-level construction 作为缓解方案（+1.40pp Few-NERD）。理论分析给出 degeneracy decomposition。\n\n### 你的审查侧重（方法严谨性 + 实验有效性）\n\n请重点审查以下方面：\n\n1. **诊断框架设计**：\n   - \"correlation-selection gap\" 概念是否定义严格？instance-level signal 无法做 selection 是否是 trivially true（它们本来就是 instance-level 的）？\n   - diagnostic cascade（degeneracy → headroom → LP compression）的逻辑链是否严密？是否有 confound？\n\n2. **统计检验**：\n   - 多重比较校正（Holm-Bonferroni）是否正确应用？family 划分是否合理？\n   - Bootstrap 检验的实施细节：seed 数量（3 seeds）是否足够？SciERC 单 seed 的统计效力？\n   - MDE (minimum detectable effect) 计算是否合理？\n\n3. **实验设计**：\n   - 4 个数据集的选择是否覆盖了 claim 所需的难度梯度？\n   - N=8 primary + N=16 scaling 是否充分？为什么不测更大 N？\n   - 仅 4B-8B fine-tuned + 72B zero-shot，是否有 scale confound？\n   - Few-NERD 3 epochs vs 其他 5 epochs 的 epoch confound 是否充分控制？\n\n4. **消融分析**：\n   - LoRA rank ablation、temperature ablation 的设计是否合理？\n   - 训练好的 verifier (LightGBM, AUC=0.923) 只提升 +0.30pp，这个负面结果是否可靠？\n   - Cross-model consistency 仅测 1 个数据集 1 对模型，是否过于初步？\n\n5. **指标与评估**：\n   - Spearman ρ 和 AUROC 作为 QE 指标是否恰当？\n   - 排除无 gold annotation 的 instance 是否引入 bias？\n   - Entity matching 使用 exact span + type match，是否过于严格？\n\n请按 ARR 标准输出完整审稿报告（Summary / Strengths / Weaknesses / Questions / Minor Issues），并给出 Overall Assessment 评分（1-5 scale，参照 EMNLP 2026 标准）和 Confidence。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "struct_self_consist_ie",
    "text": "## Round 1 审稿任务 — Reviewer 1（方法严谨性 + 实验有效性）\n\n### Venue 信息\n- **目标**: EMNLP 2026 Main Conference (via ARR May 2026)\n- **Deadline**: 2026-05-25\n- **页数限制**: Long paper, 8页正文 + 无限参考文献; Limitations/Ethics 不计页数\n- **模板**: ACL style (`\\usepackage[review]{acl}`)\n- **匿名规则**: Double-blind\n\n### 论文路径\n- LaTeX: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf`\n\n### 论文概要\n\"Strong Predictors, Weak Selectors: The Correlation-Selection Gap in Self-Consistency for Named Entity Recognition\"\n研究 test-time compute scaling (self-consistency) 应用于 NER 的效果。评估 5 种 confidence signals（SJ, VC, FK, EM, LP）在 4 个 NER benchmark 上的 quality estimation 和 sample selection 表现。核心发现：信号能做 QE（ρ up to 0.45, AUROC 0.82）但选不出最好的 sample（correlation-selection gap）。提出 entity-level construction 作为缓解方案（+1.40pp Few-NERD）。理论分析给出 degeneracy decomposition。\n\n### 你的审查侧重（方法严谨性 + 实验有效性）\n\n请重点审查以下方面：\n\n1. **诊断框架设计**：\n   - \"correlation-selection gap\" 概念是否定义严格？instance-level signal 无法做 selection 是否是 trivially true（它们本来就是 instance-level 的）？\n   - diagnostic cascade（degeneracy → headroom → LP compression）的逻辑链是否严密？是否有 confound？\n\n2. **统计检验**：\n   - 多重比较校正（Holm-Bonferroni）是否正确应用？family 划分是否合理？\n   - Bootstrap 检验的实施细节：seed 数量（3 seeds）是否足够？SciERC 单 seed 的统计效力？\n   - MDE (minimum detectable effect) 计算是否合理？\n\n3. **实验设计**：\n   - 4 个数据集的选择是否覆盖了 claim 所需的难度梯度？\n   - N=8 primary + N=16 scaling 是否充分？为什么不测更大 N？\n   - 仅 4B-8B fine-tuned + 72B zero-shot，是否有 scale confound？\n   - Few-NERD 3 epochs vs 其他 5 epochs 的 epoch confound 是否充分控制？\n\n4. **消融分析**：\n   - LoRA rank ablation、temperature ablation 的设计是否合理？\n   - 训练好的 verifier (LightGBM, AUC=0.923) 只提升 +0.30pp，这个负面结果是否可靠？\n   - Cross-model consistency 仅测 1 个数据集 1 对模型，是否过于初步？\n\n5. **指标与评估**：\n   - Spearman ρ 和 AUROC 作为 QE 指标是否恰当？\n   - 排除无 gold annotation 的 instance 是否引入 bias？\n   - Entity matching 使用 exact span + type match，是否过于严格？\n\n请按 ARR 标准输出完整审稿报告（Summary / Strengths / Weaknesses / Questions / Minor Issues），并给出 Overall Assessment 评分（1-5 scale，参照 EMNLP 2026 标准）和 Confidence。"
  }
}
```

</details>

---


### Tool result

_source line 2726 · 2026-05-20T14:20:35.070962+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 17034
}
```

</details>

---


### Tool call

_source line 2727 · 2026-05-20T14:20:35.221920+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "struct_self_consist_ie",
  "text": "## Round 1 审稿任务 — Reviewer 2（新颖性 + 完整性 + 写作质量）\n\n### Venue 信息\n- **目标**: EMNLP 2026 Main Conference (via ARR May 2026)\n- **Deadline**: 2026-05-25\n- **页数限制**: Long paper, 8页正文 + 无限参考文献; Limitations/Ethics 不计页数\n- **模板**: ACL style (`\\usepackage[review]{acl}`)\n- **匿名规则**: Double-blind\n\n### 论文路径\n- LaTeX: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf`\n\n### 论文概要\n\"Strong Predictors, Weak Selectors: The Correlation-Selection Gap in Self-Consistency for Named Entity Recognition\"\n研究 test-time compute scaling (self-consistency) 应用于 NER 的效果。评估 5 种 confidence signals（SJ, VC, FK, EM, LP）在 4 个 NER benchmark 上的 quality estimation 和 sample selection 表现。核心发现：信号能做 QE（ρ up to 0.45, AUROC 0.82）但选不出最好的 sample（correlation-selection gap）。提出 entity-level construction 作为缓解方案（+1.40pp Few-NERD）。理论分析给出 degeneracy decomposition。\n\n### 你的审查侧重（新颖性 + 完整性 + 写作质量）\n\n请重点审查以下方面：\n\n1. **新颖性与贡献评估**：\n   - \"Correlation-selection gap\" 作为核心贡献，相比 Yao et al. (2026)、Chen et al. (2025 two failures)、Eikema et al. (2025 structured MBR) 的增量贡献有多大？\n   - Entity-level construction 是否只是 ensemble NER entity voting (Florian et al. 2003) 的简单迁移？\n   - Degeneracy decomposition 的理论贡献是否 non-trivial？bound 是否太 loose（ratio 3-12%）？\n   - 4 个 contributions 是否都成立？有没有 overclaim？\n\n2. **Related Work 覆盖**：\n   - 是否遗漏重要相关工作？特别关注：\n     - 其他 structured prediction 的 test-time scaling 工作\n     - LLM-based NER 的 confidence estimation 最新工作\n     - MBR decoding 在非 MT 领域的应用\n     - Entity-level aggregation/ensemble 方法\n   - 与 Yao et al. (2026) 的区分是否清晰充分？\n\n3. **论文叙事与组织**：\n   - Section 结构是否清晰？（Background → Diagnostic → Single Signal → Adaptive → Theory → Experiments → Discussion）\n   - 论文读起来是否像一个连贯的 story 还是多个拼接的 study？\n   - Abstract 和 Introduction 的 claim 是否被 body 充分支持？\n   - 是否有 hedging 不足或过度的问题？\n\n4. **格式合规性**：\n   - 正文是否在 8 页限制内？（需要检查 PDF 页面分布）\n   - 参考文献格式是否统一？是否有不完整的 bib 条目？\n   - Figure/Table 的 caption 是否自解释？\n   - 匿名是否完整（没有泄露作者信息）？\n\n5. **写作质量**：\n   - 符号使用是否一致？\n   - 技术术语定义是否清晰？\n   - 图表质量如何？是否有视觉上难以阅读的问题？\n   - Limitations section 是否诚实全面？\n\n请按 ARR 标准输出完整审稿报告（Summary / Strengths / Weaknesses / Questions / Minor Issues），并给出 Overall Assessment 评分（1-5 scale，参照 EMNLP 2026 标准）和 Confidence。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "struct_self_consist_ie",
    "text": "## Round 1 审稿任务 — Reviewer 2（新颖性 + 完整性 + 写作质量）\n\n### Venue 信息\n- **目标**: EMNLP 2026 Main Conference (via ARR May 2026)\n- **Deadline**: 2026-05-25\n- **页数限制**: Long paper, 8页正文 + 无限参考文献; Limitations/Ethics 不计页数\n- **模板**: ACL style (`\\usepackage[review]{acl}`)\n- **匿名规则**: Double-blind\n\n### 论文路径\n- LaTeX: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf`\n\n### 论文概要\n\"Strong Predictors, Weak Selectors: The Correlation-Selection Gap in Self-Consistency for Named Entity Recognition\"\n研究 test-time compute scaling (self-consistency) 应用于 NER 的效果。评估 5 种 confidence signals（SJ, VC, FK, EM, LP）在 4 个 NER benchmark 上的 quality estimation 和 sample selection 表现。核心发现：信号能做 QE（ρ up to 0.45, AUROC 0.82）但选不出最好的 sample（correlation-selection gap）。提出 entity-level construction 作为缓解方案（+1.40pp Few-NERD）。理论分析给出 degeneracy decomposition。\n\n### 你的审查侧重（新颖性 + 完整性 + 写作质量）\n\n请重点审查以下方面：\n\n1. **新颖性与贡献评估**：\n   - \"Correlation-selection gap\" 作为核心贡献，相比 Yao et al. (2026)、Chen et al. (2025 two failures)、Eikema et al. (2025 structured MBR) 的增量贡献有多大？\n   - Entity-level construction 是否只是 ensemble NER entity voting (Florian et al. 2003) 的简单迁移？\n   - Degeneracy decomposition 的理论贡献是否 non-trivial？bound 是否太 loose（ratio 3-12%）？\n   - 4 个 contributions 是否都成立？有没有 overclaim？\n\n2. **Related Work 覆盖**：\n   - 是否遗漏重要相关工作？特别关注：\n     - 其他 structured prediction 的 test-time scaling 工作\n     - LLM-based NER 的 confidence estimation 最新工作\n     - MBR decoding 在非 MT 领域的应用\n     - Entity-level aggregation/ensemble 方法\n   - 与 Yao et al. (2026) 的区分是否清晰充分？\n\n3. **论文叙事与组织**：\n   - Section 结构是否清晰？（Background → Diagnostic → Single Signal → Adaptive → Theory → Experiments → Discussion）\n   - 论文读起来是否像一个连贯的 story 还是多个拼接的 study？\n   - Abstract 和 Introduction 的 claim 是否被 body 充分支持？\n   - 是否有 hedging 不足或过度的问题？\n\n4. **格式合规性**：\n   - 正文是否在 8 页限制内？（需要检查 PDF 页面分布）\n   - 参考文献格式是否统一？是否有不完整的 bib 条目？\n   - Figure/Table 的 caption 是否自解释？\n   - 匿名是否完整（没有泄露作者信息）？\n\n5. **写作质量**：\n   - 符号使用是否一致？\n   - 技术术语定义是否清晰？\n   - 图表质量如何？是否有视觉上难以阅读的问题？\n   - Limitations section 是否诚实全面？\n\n请按 ARR 标准输出完整审稿报告（Summary / Strengths / Weaknesses / Questions / Minor Issues），并给出 Overall Assessment 评分（1-5 scale，参照 EMNLP 2026 标准）和 Confidence。"
  }
}
```

</details>

---


### Tool result

_source line 2728 · 2026-05-20T14:20:36.735394+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1513
}
```

</details>

---


### Assistant

_source line 2729 · 2026-05-20T14:20:44.881172+00:00_

所有任务已派发：

| 任务 | 状态 |
|------|------|
| 视觉审查 Agent | ✅ 已启动（fire-and-forget） |
| Reviewer 1（方法严谨性） | ✅ 已分配 |
| Reviewer 2（新颖性+完整性） | ✅ 已分配 |
| 外部审稿 | ⏭️ 跳过（项目未配置） |

等待两位 Reviewer 返回 Round 1 独立审稿意见。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 203

## Round 203

2 recorded events


### User

_source line 2730 · 2026-05-20T14:30:18.096275+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 审稿报告 — Round 1（方法严谨性 + 实验有效性）

**论文**: "Strong Predictors, Weak Selectors: The Correlation-Selection Gap in Self-Consistency for Named Entity Recognition"
**Venue**: EMNLP 2026 Main Conference via ARR May 2026

---

## 总体评分
**Overall Assessment: 3.5 = Borderline Conference**
**一句话总结**: 诊断框架扎实、统计方法论远超NLP平均水准，但核心概念"correlation-selection gap"对4/5信号是定义上的必然（instance-level信号无法做within-instance selection），削弱了novelty；construction缓解方案效果不一致，最关键的CoNLL数据集上几乎无效。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 统计方法论出色（Holm-Bonferroni, bootstrap CI, MDE, power analysis），但核心framing有structural tautology问题；SciERC部分分析single-seed；scale confound未充分控制 |
| Excitement | 2.5/5 | 研究问题有意义（SC for structured IE），但核心发现的surprise factor有限——4/5 instance-level信号不能做selection是设计属性而非实验发现；construction mitigation效果不一致 |
| Reproducibility | 4/5 | 超详细的附录（55个表格），checklist完整，hyperparameter全部报告，training config明确；代码承诺release |
| Confidence | 4/5 | 本人熟悉self-consistency、NER evaluation和统计检验方法 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] "Correlation-Selection Gap"概念对4/5信号是 structural tautology，framing过度渲染novelty

- **具体位置**: Title, Abstract (第1段), Section 3.1, Section 4
- **问题**: 论文评估5个confidence signals用于sample selection，但4个（SJ, VC, FK, EM）是instance-level aggregates——它们对同一instance的所有N个candidates赋予相同分数（Section 3.1明确说明: "4 of 5 signals are instance-level aggregates assigning identical scores to all N candidates"）。这意味着这4个信号**根据定义就无法做within-instance ranking**。称之为"correlation-selection gap"暗示存在一个令人惊讶的差距，但实际上对这4个信号而言，"gap"只是它们的设计属性。
- **论文在Section 4确实做了structural vs. empirical的区分**（"selection failure is a design property, not an empirical finding"），但Abstract和Intro的framing没有前置这个区分——读者读到"we evaluate five confidence signals for QE and sample selection"时，会期待5个信号都是selection的候选者。
- **真正的empirical贡献是LP也失败了**（within-instance LP range仅~0.041 nats, Section 4），但这个贡献在当前framing下被淹没。
- **为什么影响接收**: 如果审稿人在读完Section 3.1后意识到80%的信号trivially不能做selection，会质疑论文的核心novelty。这是一个可以修复的framing问题而非致命缺陷，但目前的呈现方式会降低excitement评分。
- **建议**: Abstract和Intro应明确前置structural/empirical二分法。改为：(1) instance-level信号本质上不能做selection（这是结构性的，不需要实验来验证）；(2) LP是唯一的per-sample信号，但其within-instance discriminability极低（这才是核心实验发现）；(3) construction通过改变aggregation粒度来绕过structural limitation。

**N2** [critical] Construction mitigation的效果在数据集间不一致，且关键结果的统计显著性存疑

- **具体位置**: Section 6.1, Table 5, Section 7.5, Table 13 (Appendix e)
- **问题**: Entity-level construction被作为论文的核心"actionable contribution"（Section 2第3点: "Entity-level construction as a diagnostics-motivated mitigation"），但效果不一致:
  - Few-NERD: **+1.40pp**（Holm p_adj=0.006，家族k=19，显著）✓
  - SciERC: **+1.39pp**（Table 13 Row 22显示家族内p_adj=0.038，但Section 2报告"p_adj=0.20"——这两个数字矛盾，需要澄清；若全局k=57下p_adj=0.20，则不显著）
  - CoNLL: **+0.02pp**（不显著）✗
  - CoNLL (LLaMA): **+0.12pp**（边缘）
- 论文本身承认"ineffective on CoNLL (−0.39pp) where degeneracy is high (§7.5)"，但主文framing仍将construction呈现为可靠的缓解方案。
- **另一个问题**: SciERC的p_adj在主文Section 2和Table 13之间存在数值矛盾（0.20 vs. 0.038），需要澄清。如果正确值是p_adj=0.20（全局校正），那么construction仅在Few-NERD上统计显著。
- **为什么影响接收**: 论文的三个贡献中，Contribution 3 (construction mitigation)是最具实际价值的。如果它只在1/3或2/3数据集上work，且在高degeneracy（论文诊断的核心问题）条件下反而失效，这严重限制了practical impact。
- **建议**: (1) 澄清p_adj数值矛盾；(2) 主文中诚实地呈现construction的适用条件（低degeneracy + 足够headroom）；(3) 增加对CoNLL失败的分析——是因为degeneracy太高（67-70%）还是headroom太小？

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] N=8/16对于研究"test-time compute scaling"而言范围过窄

- **具体位置**: Section 7.1, Table 7, Figure 10 (Appendix r, p.28)
- **问题**: 论文在Abstract中引用"test-time compute scaling"作为研究背景，但primary实验仅用N=8，scaling分析仅到N=16。Figure 10显示ρ在N=16时仍在增长（Qwen SciERC NER）。相关文献（Brown et al., 2024; Snell et al., 2025）通常测试到N=64或更大。不测更大N，无法确定"diminishing returns"是真实现象还是N不够大。
- **缓解**: 论文确实报告了N=16的scaling趋势（Table 7），且CoNLL在N=16时oracle headroom仅2.5pp，支持diminishing returns的局部结论。但Few-NERD在N=16时LP仍有+0.30pp gain（Table 11），说明更大N可能有用。
- **建议**: 至少补充N=32的实验（即使仅在1-2个数据集上），或在Limitations中明确承认N范围的局限性。

**W2** [warning] Fine-tuned 4B-8B vs. Zero-shot 72B的scale/regime confound

- **具体位置**: Section 7.1, Table 19, Table 55 (Appendix, p.42)
- **问题**: Fine-tuned模型为4B-8B（Qwen3-8B, LLaMA-3.1-8B），zero-shot为72B（Qwen2.5-72B-AWQ）。degeneracy率在两种regime间差异显著（SciERC: fine-tuned ~17.8% vs. zero-shot不同），但无法归因于fine-tuning、model size还是model architecture。Table 55提供了72B模型ZS vs. FS的比较，但仅限于这一个模型家族。
- **建议**: 补充zero-shot 8B或few-shot 8B实验来部分控制scale confound，或在Discussion中更明确地讨论这个confound的影响。

**W3** [warning] Cross-model consistency实验过于初步

- **具体位置**: Section 5.1, 最后一段
- **问题**: Cross-architecture diversity实验仅在1个数据集（Few-NERD）上测试1对模型（Qwen3-8B + LLaMA-3.1-8B），每模型4 samples（N=8 total）。单数据集单配对的结果（+0.32pp, p=0.001, 95% CI [0.27, 0.38]）不足以支撑"cross-architecture diversity can partially compensate for within-model degeneracy"这一general claim。
- **建议**: 要么扩展到更多数据集/模型对，要么将该段语气降级为"preliminary observation"而非claim。

**W4** [warning] SciERC部分关键分析基于single seed

- **具体位置**: Table 5脚注, Section 9 (Limitations), Table 18 (Appendix i)
- **问题**: SciERC是论文中分析最详细的数据集（degeneracy decomposition、FK independence test、calibration分析、hidden state probes等），但部分分析使用single seed。虽然Table 18显示multi-seed quality estimation是稳定的（3 seeds, σ报告），且bootstrap CI提供了within-seed variance，但单seed的degeneracy rate、LP range分布等可能受特定training run影响。
- **缓解**: 论文在Limitations中承认了这一点，Table 5报告了multi-seed结果（3-seed mean for Few-NERD/CoNLL）。

**W5** [warning] Trained verifier (LightGBM) 的负面结果可能不够conclusive

- **具体位置**: Section 5.2
- **问题**: LightGBM entity-level classifier（5 features）AUC=0.923±0.002 但只提升+0.30pp OOF construction。论文由此得出"frequency-based threshold construction already captures most of the verifier's signal"。但: (1) verifier仅在SciERC上测试；(2) 特征集有限（5个信号）——未尝试更丰富的特征（如entity type、sentence length、LP variance等）；(3) Cross-dataset transfer测试（Few-NERD→SciERC）结果为负（-0.70pp），但这可能是domain shift而非verifier inherent limitation。
- **建议**: 讨论feature engineering的局限性，或至少承认当前verifier实验是exploratory的。

---

## 小问题（不影响接收）

- **M1**: Table 1 (p.4) "One score per input"列中，LP标注为"per-sample"但表头说"One score per input"——建议用更清晰的列名区分instance-level vs. per-sample。
- **M2**: Section 6.3 degeneracy decomposition的证明（Appendix o.3）中，Proposition 1的条件"under entity-wise independence"在什么场景下不成立？论文未讨论这个假设何时会被violated（例如，实体间有dependency的嵌套NER）。
- **M3**: 脚注9 (p.21) 报告Holm-Bonferroni的family分组: "selection (k=19), construction (k=10), and signal comparison (k=9)"，总计k=38，但Table 13列出k=57。差异的k=19来自哪里？需要在附录中更清楚地列出family分组。
- **M4**: Figure 1 (p.3) 的三面板设计直观有效，但"selection gap"中间面板的示意过于简化——没有展示LP作为唯一per-sample信号的特殊地位。
- **M5**: Section 7.4 "Robustness"最后提到"Consistency signals are robust across T∈{0.7, 1.0} with uniform N-scaling gains"，但Table 37 (p.39) 显示LP在T=0.5时增幅最大（+14.6pp）——这个temperature dependence值得在主文中mention。
- **M6**: 论文大量依赖SciERC作为primary testbed，但SciERC仅有551个test instances——对于细粒度的subgroup分析（如per-entity-type LP selection, Table 43），sample size可能不足。

---

## 主要优势

1. **统计方法论远超NLP社区平均水平**: Holm-Bonferroni多重比较校正、Bootstrap CI (B=10,000)、MDE/power analysis (Table 50)、TOST equivalence testing (Table 16)——这种统计严谨性在NER/IE论文中极为罕见，值得肯定。
2. **Degeneracy decomposition提供了clean的理论框架**: E[Δ|F1] = (1−D)·G_nd（Proposition 1, Appendix o.3）将selection gain分解为degeneracy rate和non-degenerate oracle gap，有证明且有numerical verification（Table 28, p.37）。
3. **诊断框架的实用价值**: 论文提出的diagnostic protocol（Appendix ab, p.34）——degeneracy measurement → signal-quality alignment → aggregation strategy evaluation——为未来SC-for-IE研究提供了可复用的方法论。
4. **极其详尽的附录**: 55个表格覆盖temperature ablation、LoRA rank ablation、free-form decoding对比、calibration分析、hidden state probes、per-entity-type分析等，体现了对robustness的认真态度。
5. **负面结果的诚实报告**: trained verifier失败（§5.2）、cross-model仅preliminary（§5.1）、construction在CoNLL无效（§7.5）——这种transparency在审稿中加分。
6. **Entity-level construction是一个novel且直觉合理的idea**: 将aggregation粒度从sample降到entity，利用不同sample间entity-level的互补性——即使效果不一致，这个方向值得探索。

---

## 对Director指定审查维度的逐项回应

### 1. 诊断框架设计
- "Correlation-selection gap"对instance-level信号（4/5）是trivially true（见N1）。对LP则是genuine empirical finding（within-instance LP range ~0.041 nats）。
- Diagnostic cascade逻辑链（degeneracy → headroom → LP compression）基本严密，但degeneracy和headroom不独立（高degeneracy → degenerate instances的headroom为0），论文通过decomposition E[Δ|F1]=(1-D)·G_nd处理了这个关联。

### 2. 统计检验
- Holm-Bonferroni正确应用，但family划分存在不一致（脚注9 vs. Table 13，见M3）。
- 3 seeds对fine-tuned模型是标准做法；SciERC single-seed是limitation但有bootstrap CI缓解。
- MDE计算合理（Table 50），诚实承认小样本只能检测large effects。
- **一个concern**: Section 2报告SciERC construction p_adj=0.20与Table 13的p_adj=0.038矛盾（见N2），可能源于不同family scope。

### 3. 实验设计
- 4数据集覆盖了difficulty gradient（SciERC ~65% F1 → CoNLL >90% F1），合理但缺biomedical NER。
- N=8/16偏小（见W1），特别是声称研究"test-time compute scaling"。
- Scale confound存在但不致命（见W2），Table 55提供了部分控制。
- Few-NERD 3 epochs vs. 其他5 epochs：Table 19显示这是有意的（可能为防过拟合），但主文未解释原因。

### 4. 消融分析
- LoRA rank ablation（Table 7, Section 7.4）设计合理，结果稳定。
- Temperature ablation（Table 37, Appendix s）覆盖4个温度，结论合理。
- Trained verifier负面结果基本可靠但scope有限（见W5）。
- Cross-model consistency过于初步（见W3）。

### 5. 指标与评估
- Spearman ρ和AUROC作为QE指标恰当。
- 排除无gold annotation的instance（Appendix b）可能引入bias（高F1 instance被over-represented），但影响有限（CoNLL仅排除~3%）。
- Exact span+type match是NER标准做法。论文在Appendix q (p.24)讨论了RE的partial match，说明对匹配标准有思考。

---

**Overall: 3.5 (Borderline Conference)** — 分析扎实、统计严谨、附录详尽，但核心novelty被framing稀释（gap对instance-level信号是tautology），construction mitigation效果不一致限制了practical impact。适合Findings。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 2731 · 2026-05-20T14:30:26.938549+00:00_

Reviewer 1 报告已收到（3.5 Borderline Conference）。等待 Reviewer 2 报告后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 204

## Round 204

4 recorded events


### User

_source line 2732 · 2026-05-20T14:30:29.600974+00:00_

[Reviewer 1 审稿结果]:
审稿报告已提交给 Review Director。引用验证结果也出来了。

**审稿报告核心结论：Overall 3.5 (Borderline Conference)**

关键问题：
1. **[Critical] N1**: "Correlation-selection gap"对4/5 instance-level信号是 structural tautology，framing过度渲染novelty
2. **[Critical] N2**: Construction mitigation效果不一致（仅Few-NERD显著，SciERC的p_adj存在数值矛盾，CoNLL无效）
3. **[Warning] W1-W5**: N=8/16范围过窄、scale confound、cross-model过于初步、SciERC single-seed、trained verifier scope有限

引用验证方面：96条引用中83条验证通过，4条未找到（其中2条可能是API限制），2条年份可能有误（`chen2025twofailures`和`wang2025gptner`实际可能是2023年发表），17条orphan bib entries未被引用（不影响渲染）。无broken citations。引用整体质量良好。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 2733 · 2026-05-20T14:30:44.752828+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': '初始化：获取项目概览 + 检查论文文件', 'status': 'completed', 'activeForm': '获取项目概览和检查论文文件'}, {'content': 'Step 0: Venue 调研（WebSearch EMNLP 2026 CFP）', 'status': 'completed', 'activeForm': '搜索 EMNLP 2026 CFP 和格式要求'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.6/0.7: 派发视觉审查 + 分配 Reviewer 任务', 'status': 'completed', 'activeForm': '派发视觉审查并分配 Reviewer 任务'}, {'content': '收集 R1 审稿报告', 'status': 'completed', 'activeForm': '收集 R1 审稿报告'}, {'content': '收集 R2 审稿报告', 'status': 'in_progress', 'activeForm': '等待 R2 审稿报告'}, {'content': 'Step 2: 交叉分享', 'status': 'pending', 'activeForm': '交叉分享 Reviewer 意见'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断是否收敛'}, {'content': 'Step 4: 汇总报告 + 投递', 'status': 'pending', 'activeForm': '汇总审稿报告并投递'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': '初始化：获取项目概览 + 检查论文文件', 'status': 'completed', 'activeForm': '获取项目概览和检查论文文件'}, {'content': 'Step 0: Venue 调研（WebSearch EMNLP 2026 CFP）', 'status': 'completed', 'activeForm': '搜索 EMNLP 2026 CFP 和格式要求'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.6/0.7: 派发视觉审查 + 分配 Reviewer 任务', 'status': 'completed', 'activeForm': '派发视觉审查并分配 Reviewer 任务'}, {'content': '收集 R1 审稿报告', 'status': 'completed', 'activeForm': '收集 R1 审稿报告'}, {'content': '收集 R2 审稿报告', 'status': 'in_progress', 'activeForm': '等待 R2 审稿报告'}, {'content': 'Step 2: 交叉分享', 'status': 'pending', 'activeForm': '交叉分享 Reviewer 意见'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断是否收敛'}, {'content': 'Step 4: 汇总报告 + 投递', 'status': 'pending', 'activeForm': '汇总审稿报告并投递'}]"
  }
}
```

</details>

---


### Tool result

_source line 2734 · 2026-05-20T14:30:44.753357+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---


### Assistant

_source line 2735 · 2026-05-20T14:30:46.795502+00:00_

R1 审稿报告已收到，记录关键发现：

- **Overall: 3.5 (Borderline Conference)**
- 2 个 Critical issues（N1: framing tautology, N2: construction inconsistency + p_adj 矛盾）
- 5 个 Warning issues（W1-W5）
- 6 个 Minor issues（M1-M6）
- 引用验证：96 条中 83 条通过，整体良好

等待 R2 报告后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 205

## Round 205

8 recorded events


### User

_source line 2736 · 2026-05-20T14:30:52.847569+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 — Round 1 审稿报告

**论文**: "Strong Predictors, Weak Selectors: The Correlation-Selection Gap in Self-Consistency for Named Entity Recognition"
**Venue**: EMNLP 2026 (via ARR May 2026)
**审查侧重**: 新颖性 + 完整性 + 写作质量

---

## 总体评分
**Overall**: 3.0 / 5 — Findings
**一句话总结**: 扎实的实证研究揭示了 self-consistency 信号在 NER 上"能估质量、不能选最优"的 gap，但四项贡献各自增量偏小，entity-level construction 新颖性不足，理论 bound 过松，且存在重要缺引。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5 / 5 | 主要 claim 有实验支撑，但"first systematic characterization"过度声称；degeneracy bound 仅捕获 3-12% 的实际 gap，理论贡献名不副实 |
| Excitement | 3.0 / 5 | Correlation-selection gap 是有价值的实证洞察，但 entity-level mitigation 效果有限（+1.40pp），整体 novelty 偏 incremental |
| Reproducibility | 4.0 / 5 | 实验设置详尽（Appendix j-k），4 个公开数据集，承诺发布代码；LoRA 超参、prompt 模板均有报告 |
| Overall Assessment | 3.0 / 5 | Findings 水平：有用的实证发现 + 实操指导，但单项贡献深度不够，不达主会议 novelty 门槛 |
| Confidence | 4 / 5 | 熟悉 test-time scaling、MBR decoding、LLM-based NER 相关文献 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] Entity-level construction 的新颖性被高估，缺少关键引用

- 具体位置：Section 6.1, Contribution #3 (§1, page 2)
- 问题：论文将 entity-level construction 定位为 contribution #3，声称"adapting entity voting from ensemble NER (Florian et al., 2003) to stochastic sampling"。然而：
  - (a) **EL4NER** (arXiv:2505.23038, May 2025) 已系统实现了基于多 LLM 的 entity-level span 提取 + entity type voting 的两阶段 ensemble NER pipeline，且在 ICL 设置下取得 SOTA。这篇直接相关的工作未被引用。
  - (b) Xie et al. (2023a) 的 entity voting 方法（论文自己在 §2 引用）已是 entity-level aggregation 的先驱。论文的"novelty"本质上是将已有的 entity voting 重新用 MBR 框架包装，并在 SC 语境下做了消融。
  - (c) +1.40pp (Few-NERD) 和 +0.12pp (Few-NERD) / +0.55pp (SciERC) 的改进幅度有限，不足以支撑单独作为一项 contribution。
- 为什么影响接收：缺少直接相关的 2025 工作引用，且现有 contribution 的增量贡献被高估，会影响 novelty 判断。
- 建议修改方向：(1) 补引 EL4NER 并明确区分（单模型内 SC vs. 多模型 ensemble）；(2) 将 entity-level construction 降级为 diagnostic-motivated ablation 而非 standalone contribution；(3) 如果保留为 contribution，需要在更多数据集/模型上展示稳健的改进。

**N2** [critical] Degeneracy decomposition 的理论贡献过于 loose，不足以作为独立 contribution

- 具体位置：Section 6.3, Proposition 1 (page 6), §o.3 (Appendix, page 25-26)
- 问题：E[ΔF₁] ≤ (1−D)·G_adj 的 bound 仅能解释实际 correlation-selection gap 的 3-12%（论文自承，§6.3 "the bound is loose"）。具体数值：
  - SciERC: bound ratio 3.1×(Figure 9)
  - CoNLL: bound 仅捕获 ~6.8% 的 gap
  - 论文在 Appendix o.4 进一步验证了 bound 太松（"the best signal recovers only 6.8% of the non-degenerate oracle gap on average"）
  
  Proposition 1 本身是 MBR for balanced set-overlap 的直接推导（F1 的 non-linear + closed-form threshold 在 Dembczyński et al. 2011 已有），新增理论贡献主要是 degeneracy rate D 的定义和分解，但 D 本身只是一个描述性统计量，不提供优化方向或 actionable insight。
- 为什么影响接收：作为 Contribution #4，理论分析未能提供超出 descriptive statistics 的洞察。3-12% 的解释力使其在审稿人眼中更像 negative result 的理论注脚，而非独立贡献。
- 建议修改方向：(1) 将 degeneracy decomposition 从 contribution 列表降级为 analysis tool，在 §6.3 讨论其局限性；(2) 或者 tighten the bound——考虑 non-degenerate instances 内部的 signal-dependent gap，给出更细粒度的分解。

**N3** [critical] "First systematic characterization" 的声称过强

- 具体位置：Abstract ("we provide the first systematic characterization"), §1 page 2 ("the first systematic empirical characterization of when and why test-time scaling via LP-based selection succeeds or fails for NER")
- 问题：
  - Chen et al. (2023, arXiv:2305.14279) 已系统研究了 self-consistency 在 multi-step reasoning 中的两种 failure modes（hypothetical + compositional consistency）
  - Eikema et al. (2025, EMNLP) 已研究 structured MBR decoding 中 standard utility functions 在 structured outputs 上的失效
  - Kang et al. (2025) Self-Certainty 和 Taubenfeld et al. (2025) 已研究 confidence signals 与 SC 的关系
  - 论文的"first"仅限于 NER 任务 + 这 5 个 specific signals 的组合，但 Abstract 和 Introduction 中的措辞暗示更广泛的 novelty
- 为什么影响接收：Overclaiming 是 ARR 审稿中的常见拒绝理由。如果不精确限定 scope，reviewer 会质疑作者对相关工作的了解程度。
- 建议修改方向：改为 "the first systematic empirical characterization of the correlation-selection gap **for NER**" 或 "**in the context of structured entity extraction**"。

**N4** [critical] 多处参考文献错误

- 具体位置：References (pages 11-14)
- 问题（引用验证工具检出）：
  - **chen2025twofailures**: 论文标注 2025，但实际发表于 2023 (arXiv:2305.14279)。TMLR 版可能是 2024，但绝非 2025。
  - **feng2025optimal**: bib 中第一作者 "Feng"，但 OpenAlex 显示实际第一作者应为 "Austin"——需核实。
  - **park2024grammar**: bib 中第一作者 "Park"，但 OpenAlex 显示 "Berg-Kirkpatrick"——可能是 bib 条目张冠李戴。
  - **hobelsberger2025systematic**: "Systematic Evaluation of Uncertainty Estimation Methods in Large Language Models"——在 OpenAlex、Semantic Scholar 均无法验证，最佳匹配相似度仅 0.236。**疑似虚构引用**（fabricated reference），这在 ARR 审稿中是严重问题。
  - **17 个 orphan bib entries**（在 .bib 中但未被引用），包括 openai2024o1、min2022rethinking 等。虽不影响接收，但反映提交前 cleanup 不足。
- 为什么影响接收：虚构引用（如属实）可导致 desk reject。年份和作者错误影响可信度。
- 建议修改方向：(1) 立即核实 hobelsberger2025systematic 的真实性；(2) 修正 chen2025twofailures 年份；(3) 核实 feng2025optimal 和 park2024grammar 的作者信息；(4) 清理 orphan bib entries。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] 模型多样性有限

- 具体位置：§7.1 (page 7), Table 2-5
- 问题：仅使用 Qwen3-8B 和 LLaMA-3.1-8B-Instruct 两个 ~8B 模型。两个模型来自不同 family 但参数规模相同。论文在 Discussion (§8) 承认"we cover 4B-8B fine-tuned and 72B zero-shot; the gap persists at 72B"，但 72B 结果仅在 Appendix r 简略提及，且未在主表格中展示。
  - 缺少 >70B 规模的 fine-tuned 模型测试
  - 缺少 closed-source 模型（如 GPT-4）的比较
  - 仅测试 English NER datasets
- 建议：至少在主表格中加入 72B 结果，或讨论为什么 model scale 不是关键变量。

**W2** [warning] Correlation-selection gap 的因果方向未建立

- 具体位置：§4 (pages 4-5), Figure 2-3, "Diagnostic cascade"
- 问题：论文将 diagnostic cascade 描述为因果链（"instance degeneracy sets the ceiling, oracle headroom determines the opportunity, and LP compression limits exploitation"），但实际上这只是三个相关变量的描述性分析。论文未排除混淆变量的可能性——例如，instance difficulty 可能同时影响 degeneracy、headroom 和 compression。
- 建议：明确标注为 descriptive decomposition 而非 causal cascade，或提供干预性实验。

**W3** [warning] 论文试图同时做太多事情

- 具体位置：整篇论文的 4 个 contributions
- 问题：论文同时包含：(1) QE evaluation benchmark, (2) selection failure diagnosis, (3) entity-level construction mitigation, (4) degeneracy theory。每项都是半页到一页的篇幅，导致每个方向的深度不够。例如：
  - Entity-level construction 没有和 EL4NER 或其他 entity-level methods 做充分对比
  - Degeneracy bound 太松但没有深入分析 tightness
  - QE evaluation 的 5 signals 仅选取了部分（缺少 PTrue、Self-Certainty 等近期信号）
- 建议：考虑聚焦 contributions #1 + #2（QE + selection failure diagnosis），将 #3 和 #4 作为 follow-up 讨论。

**W4** [warning] Missing related work: structured prediction 的 test-time scaling

- 具体位置：§2 Background & Related Work
- 问题：
  - "Beyond Majority Voting: LLM Aggregation by Leveraging Higher-Order Information" (arXiv:2510.01499, Oct 2025)——探索了超越 majority voting 的 aggregation 方法
  - "Scalable Best-of-N Selection via Self-Certainty" (arXiv:2502.18581)——直接相关的 best-of-N selection 方法
  - "Optimal Aggregation of LLM and PRM Signals for Efficient Test-Time Scaling" (arXiv:2510.13918)——多 signal 聚合的理论框架
  这些工作在 aggregation 和 signal combination 方面有直接相关性。
- 建议：在 §2 增加对 aggregation beyond majority voting 的讨论。

---

## 小问题（不影响接收）

- **M1**: Table 1 (page 4) 中 Oracle 行的 "NER F1" 和 "NBR F1" 列标题含义不够直观，caption 未完整解释 NBR 的含义（是 "NER Benchmark Results" 还是其他？实际看内容应是 "NER F1"）。→ 核实后统一。
- **M2**: Figure 2 (page 5) 的 y 轴标签 "μ" 较小，且 dashed green line 的 legend "greedy single" 与正文 "greedy (3-seed)" 表述不一致。
- **M3**: §3.2 中 Fleiss' κ (FK) 的定义引用了 Fleiss (1971)，但 FK 在文中被描述为 "inter-rater agreement"，而实际用法是 type-level agreement across N samples——这不是标准的 inter-rater reliability 场景，应补充说明。
- **M4**: Appendix b (Robustness Analysis) 的 "gold annotations" filtering 条件未在主文中提及，可能影响主表结果的可比性。
- **M5**: 论文在 §8 Discussion 提到 "LP compression on SciERC; Appendix i"——但 Appendix i 是关于 "Multi-Seed Stability"，§8 引用可能有误。
- **M6**: 17 个 orphan bib entries 应清理（包括 openai2024o1、min2022rethinking、sagi2018ensemble 等未被引用的条目）。

---

## 格式合规性

| 检查项 | 结果 | 备注 |
|--------|------|------|
| 正文 ≤ 8 页 | ✓ | Sections 1-9 (through Conclusion) 在 page 8 结束，Limitations 从 page 8 底部开始（不计入页数限制） |
| 匿名 | ✓ | "Anonymous ACL submission"，未发现 deanonymization |
| ACL style | ✓ | 使用 `\usepackage[review]{acl}` |
| Limitations section | ✓ | 存在于 page 8-9，内容诚实（讨论了 model scale、English-only、no open-ended QA 等限制） |
| Ethics statement | ✓ | 存在于 page 9 |
| NLP Checklist | ✓ | Pages 9-10，回答完整 |
| Figure/Table captions | ⚠ | 大部分自解释，但 Table 1 的 "NBR F1" 需澄清 |
| 参考文献格式 | ⚠ | 存在年份错误和可疑引用（见 N4） |

---

## 主要优势

1. **问题定义清晰且有实际价值**：correlation-selection gap 是一个简洁、可操作的概念，对 NER practitioners 直接有用——知道信号能做 QE (ρ up to 0.45, AUROC 0.82) 但选不出最好的 sample，这改变了使用 test-time scaling 的策略。

2. **实验设计系统全面**：5 signals × 4 datasets × 2 models × 4B-8B fine-tuned + 72B zero-shot，覆盖面在同类工作中属优秀。Bootstrap CI (3 seeds, 10,000 resamples)、Holm-Bonferroni correction、permutation tests 等统计方法的使用体现了严谨性。

3. **Diagnostic cascade 分析有洞察力**：Figure 3 的 degeneracy × LP compression 交互分析、Figure 8 的 within-instance LP range CDF 分析，为理解"为什么信号选不出最优"提供了直觉。

4. **Prescriptive guidance 有实操价值**：§7.5 给出的三条建议（filtering low-confidence → LP selection → entity-level construction 在 degeneracy 高时使用）对 practitioners 直接有用。

5. **Appendix 极其详尽**（30 页）：robustness analyses、ablation studies、full signal comparisons、calibration analysis 等，展示了作者的严谨态度。

---

## 对 Director 的总结

这是一篇扎实的实证论文，core insight（correlation-selection gap）有价值。但四项 contributions 中，#3（entity-level construction）新颖性不足且缺少关键引用（EL4NER），#4（degeneracy bound）过松不足以作为独立贡献。"First systematic characterization" 的 overclaim 需要 scope down。参考文献存在需要立即处理的问题（疑似虚构引用 hobelsberger2025systematic）。

建议评级 **3.0 (Findings)**：有用的实证发现适合 Findings track，但 novelty 和 excitement 不达主会议水平。如果作者能 (1) 修正 overclaims，(2) 补引并区分 EL4NER，(3) 修复引用问题，(4) 将论文聚焦到最强的 contributions (#1 + #2)，这篇论文在 Findings 中会是一篇有价值的工作。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 2737 · 2026-05-20T14:31:18.779296+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': '初始化：获取项目概览 + 检查论文文件', 'status': 'completed', 'activeForm': '获取项目概览和检查论文文件'}, {'content': 'Step 0: Venue 调研（WebSearch EMNLP 2026 CFP）', 'status': 'completed', 'activeForm': '搜索 EMNLP 2026 CFP 和格式要求'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.6/0.7: 派发视觉审查 + 分配 Reviewer 任务', 'status': 'completed', 'activeForm': '派发视觉审查并分配 Reviewer 任务'}, {'content': '收集 R1 审稿报告', 'status': 'completed', 'activeForm': '收集 R1 审稿报告'}, {'content': '收集 R2 审稿报告', 'status': 'completed', 'activeForm': '收集 R2 审稿报告'}, {'content': 'Step 2: 交叉分享（R1↔R2 互看报告 + 逐条回应）', 'status': 'in_progress', 'activeForm': '交叉分享 Reviewer 意见'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断是否收敛'}, {'content': 'Step 4: 汇总报告 + 投递', 'status': 'pending', 'activeForm': '汇总审稿报告并投递'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': '初始化：获取项目概览 + 检查论文文件', 'status': 'completed', 'activeForm': '获取项目概览和检查论文文件'}, {'content': 'Step 0: Venue 调研（WebSearch EMNLP 2026 CFP）', 'status': 'completed', 'activeForm': '搜索 EMNLP 2026 CFP 和格式要求'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.6/0.7: 派发视觉审查 + 分配 Reviewer 任务', 'status': 'completed', 'activeForm': '派发视觉审查并分配 Reviewer 任务'}, {'content': '收集 R1 审稿报告', 'status': 'completed', 'activeForm': '收集 R1 审稿报告'}, {'content': '收集 R2 审稿报告', 'status': 'completed', 'activeForm': '收集 R2 审稿报告'}, {'content': 'Step 2: 交叉分享（R1↔R2 互看报告 + 逐条回应）', 'status': 'in_progress', 'activeForm': '交叉分享 Reviewer 意见'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断是否收敛'}, {'content': 'Step 4: 汇总报告 + 投递', 'status': 'pending', 'activeForm': '汇总审稿报告并投递'}]"
  }
}
```

</details>

---


### Tool result

_source line 2738 · 2026-05-20T14:31:18.779700+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2739 · 2026-05-20T14:31:39.343330+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "struct_self_consist_ie",
  "text": "## 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见\n\n以下是 Reviewer 2 的完整审稿原文。请逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n## Reviewer 2 审稿报告（Overall: 3.0 Findings）\n\n### Must-Fix 问题\n\n**R2-N1** [critical] Entity-level construction 的新颖性被高估，缺少关键引用\n- EL4NER (arXiv:2505.23038, May 2025) 已系统实现了基于多 LLM 的 entity-level span 提取 + entity type voting 的两阶段 ensemble NER pipeline，且在 ICL 设置下取得 SOTA。未被引用。\n- Xie et al. (2023a) 的 entity voting 方法已是 entity-level aggregation 的先驱。论文的\"novelty\"本质上是将已有的 entity voting 重新用 MBR 框架包装。\n- +1.40pp (Few-NERD) 改进幅度有限，不足以支撑单独作为一项 contribution。\n- 建议：补引 EL4NER 并明确区分；将 entity-level construction 降级为 diagnostic-motivated ablation 而非 standalone contribution。\n\n**R2-N2** [critical] Degeneracy decomposition 的理论贡献过于 loose，不足以作为独立 contribution\n- E[ΔF₁] ≤ (1−D)·G_adj 的 bound 仅能解释实际 gap 的 3-12%。\n- Proposition 1 本身是 MBR for balanced set-overlap 的直接推导；D 本身只是描述性统计量。\n- 建议：降级为 analysis tool，或 tighten the bound。\n\n**R2-N3** [critical] \"First systematic characterization\" 的声称过强\n- Chen et al. (2023), Eikema et al. (2025), Kang et al. (2025), Taubenfeld et al. (2025) 已有相关 systematic studies。\n- 论文的\"first\"仅限于 NER + 这 5 个 specific signals 的组合。\n- 建议：限定 scope 为 \"for NER\" 或 \"in the context of structured entity extraction\"。\n\n**R2-N4** [critical] 多处参考文献错误\n- chen2025twofailures: 实际发表于 2023 (arXiv:2305.14279)\n- feng2025optimal 和 park2024grammar: 第一作者可能有误\n- hobelsberger2025systematic: 疑似虚构引用\n- 17 个 orphan bib entries\n\n### Should-Fix 问题\n\n**R2-W1** [warning] 模型多样性有限（仅 2 个 ~8B 模型，缺 closed-source）\n**R2-W2** [warning] Diagnostic cascade 是描述性分析而非因果链\n**R2-W3** [warning] 论文试图同时做太多事情（4 contributions 各自深度不够）\n**R2-W4** [warning] Missing related work（Beyond Majority Voting, Scalable BoN via Self-Certainty, Optimal Aggregation）\n\n### 小问题\nM1-M6: Table 1 列标题、Figure 2 y轴标签、FK定义说明、gold filtering、appendix引用错误、orphan bib entries\n\n### 主要优势\n1. 问题定义清晰有实际价值\n2. 实验设计系统全面\n3. Diagnostic cascade 分析有洞察力\n4. Prescriptive guidance 有实操价值\n5. Appendix 极其详尽\n\n---\n\n请对上述每个 Must-Fix (N1-N4) 和 Should-Fix (W1-W4) 问题给出 [AGREE] 或 [REBUT] 回应。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "struct_self_consist_ie",
    "text": "## 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见\n\n以下是 Reviewer 2 的完整审稿原文。请逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n## Reviewer 2 审稿报告（Overall: 3.0 Findings）\n\n### Must-Fix 问题\n\n**R2-N1** [critical] Entity-level construction 的新颖性被高估，缺少关键引用\n- EL4NER (arXiv:2505.23038, May 2025) 已系统实现了基于多 LLM 的 entity-level span 提取 + entity type voting 的两阶段 ensemble NER pipeline，且在 ICL 设置下取得 SOTA。未被引用。\n- Xie et al. (2023a) 的 entity voting 方法已是 entity-level aggregation 的先驱。论文的\"novelty\"本质上是将已有的 entity voting 重新用 MBR 框架包装。\n- +1.40pp (Few-NERD) 改进幅度有限，不足以支撑单独作为一项 contribution。\n- 建议：补引 EL4NER 并明确区分；将 entity-level construction 降级为 diagnostic-motivated ablation 而非 standalone contribution。\n\n**R2-N2** [critical] Degeneracy decomposition 的理论贡献过于 loose，不足以作为独立 contribution\n- E[ΔF₁] ≤ (1−D)·G_adj 的 bound 仅能解释实际 gap 的 3-12%。\n- Proposition 1 本身是 MBR for balanced set-overlap 的直接推导；D 本身只是描述性统计量。\n- 建议：降级为 analysis tool，或 tighten the bound。\n\n**R2-N3** [critical] \"First systematic characterization\" 的声称过强\n- Chen et al. (2023), Eikema et al. (2025), Kang et al. (2025), Taubenfeld et al. (2025) 已有相关 systematic studies。\n- 论文的\"first\"仅限于 NER + 这 5 个 specific signals 的组合。\n- 建议：限定 scope 为 \"for NER\" 或 \"in the context of structured entity extraction\"。\n\n**R2-N4** [critical] 多处参考文献错误\n- chen2025twofailures: 实际发表于 2023 (arXiv:2305.14279)\n- feng2025optimal 和 park2024grammar: 第一作者可能有误\n- hobelsberger2025systematic: 疑似虚构引用\n- 17 个 orphan bib entries\n\n### Should-Fix 问题\n\n**R2-W1** [warning] 模型多样性有限（仅 2 个 ~8B 模型，缺 closed-source）\n**R2-W2** [warning] Diagnostic cascade 是描述性分析而非因果链\n**R2-W3** [warning] 论文试图同时做太多事情（4 contributions 各自深度不够）\n**R2-W4** [warning] Missing related work（Beyond Majority Voting, Scalable BoN via Self-Certainty, Optimal Aggregation）\n\n### 小问题\nM1-M6: Table 1 列标题、Figure 2 y轴标签、FK定义说明、gold filtering、appendix引用错误、orphan bib entries\n\n### 主要优势\n1. 问题定义清晰有实际价值\n2. 实验设计系统全面\n3. Diagnostic cascade 分析有洞察力\n4. Prescriptive guidance 有实操价值\n5. Appendix 极其详尽\n\n---\n\n请对上述每个 Must-Fix (N1-N4) 和 Should-Fix (W1-W4) 问题给出 [AGREE] 或 [REBUT] 回应。"
  }
}
```

</details>

---


### Tool result

_source line 2740 · 2026-05-20T14:32:05.739308+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 26395
}
```

</details>

---


### Tool call

_source line 2741 · 2026-05-20T14:32:05.890969+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "struct_self_consist_ie",
  "text": "## 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见\n\n以下是 Reviewer 1 的完整审稿原文。请逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n \n---\n\n## Reviewer 1 审稿报告（Overall: 3.5 Borderline Conference）\n\n### Must-Fix 问题\n\n**R1-N1** [critical] \"Correlation-Selection Gap\"概念对4/5信号是 structural tautology，framing过度渲染novelty\n- 4/5 信号（SJ, VC, FK, EM）是 instance-level aggregates，对同一 instance 的所有 N 个 candidates 赋予相同分数——它们根据定义就无法做 within-instance ranking。\n- 论文在 Section 4 做了 structural vs. empirical 的区分，但 Abstract 和 Intro 的 framing 没有前置这个区分。\n- 真正的 empirical 贡献是 LP 也失败了（within-instance LP range ~0.041 nats），但在当前 framing 下被淹没。\n- 建议：Abstract/Intro 应前置 structural/empirical 二分法，突出 LP 作为唯一 per-sample 信号的 compression 问题。\n\n**R1-N2** [critical] Construction mitigation效果在数据集间不一致，且关键结果的统计显著性存疑\n- Few-NERD: +1.40pp（Holm p_adj=0.006，显著）✓\n- SciERC: +1.02pp（Section 2 报告 p_adj=0.20，但 Table 13 显示 p_adj=0.038——数值矛盾）\n- CoNLL: -0.39pp（不显著）✗\n- 建议：澄清 p_adj 矛盾；增加对 CoNLL 失败的分析。\n\n### Should-Fix 问题\n\n**R1-W1** [warning] N=8/16 对于研究\"test-time compute scaling\"而言范围过窄\n- 相关文献（Brown et al., 2024; Snell et al., 2025）通常测试到 N=64 或更大。\n- Few-NERD N=16 LP 仍有 +0.30pp gain，更大 N 可能有用。\n\n**R1-W2** [warning] Fine-tuned 4B-8B vs. Zero-shot 72B 的 scale/regime confound\n- 无法归因于 fine-tuning、model size 还是 model architecture。\n\n**R1-W3** [warning] Cross-model consistency 实验过于初步\n- 仅 1 个数据集（Few-NERD）+ 1 对模型（Qwen3-8B + LLaMA-3.1-8B），不足以支撑 general claim。\n\n**R1-W4** [warning] SciERC 部分关键分析基于 single seed\n- SciERC 是分析最详细的数据集，但部分分析 single seed。有 bootstrap CI 缓解但不够。\n\n**R1-W5** [warning] Trained verifier (LightGBM) 的负面结果可能不够 conclusive\n- 仅 SciERC 上测试，特征集有限（5个信号），cross-dataset transfer 负面可能是 domain shift。\n\n### 小问题\nM1-M6: Table 1 列名、Proposition 1 entity-wise independence 假设、Holm family 分组不一致、Figure 1 中间面板、T=0.5 LP 增幅、SciERC 551 instances 对 subgroup 分析不足\n\n### 主要优势\n1. 统计方法论远超 NLP 社区平均水平\n2. Degeneracy decomposition 提供 clean 理论框架\n3. 诊断框架的实用价值\n4. 极其详尽的附录（55个表格）\n5. 负面结果的诚实报告\n6. Entity-level construction 是 novel 且直觉合理的 idea\n\n---\n\n请对上述每个 Must-Fix (N1-N2) 和 Should-Fix (W1-W5) 问题给出 [AGREE] 或 [REBUT] 回应。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "struct_self_consist_ie",
    "text": "## 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见\n\n以下是 Reviewer 1 的完整审稿原文。请逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n \n---\n\n## Reviewer 1 审稿报告（Overall: 3.5 Borderline Conference）\n\n### Must-Fix 问题\n\n**R1-N1** [critical] \"Correlation-Selection Gap\"概念对4/5信号是 structural tautology，framing过度渲染novelty\n- 4/5 信号（SJ, VC, FK, EM）是 instance-level aggregates，对同一 instance 的所有 N 个 candidates 赋予相同分数——它们根据定义就无法做 within-instance ranking。\n- 论文在 Section 4 做了 structural vs. empirical 的区分，但 Abstract 和 Intro 的 framing 没有前置这个区分。\n- 真正的 empirical 贡献是 LP 也失败了（within-instance LP range ~0.041 nats），但在当前 framing 下被淹没。\n- 建议：Abstract/Intro 应前置 structural/empirical 二分法，突出 LP 作为唯一 per-sample 信号的 compression 问题。\n\n**R1-N2** [critical] Construction mitigation效果在数据集间不一致，且关键结果的统计显著性存疑\n- Few-NERD: +1.40pp（Holm p_adj=0.006，显著）✓\n- SciERC: +1.02pp（Section 2 报告 p_adj=0.20，但 Table 13 显示 p_adj=0.038——数值矛盾）\n- CoNLL: -0.39pp（不显著）✗\n- 建议：澄清 p_adj 矛盾；增加对 CoNLL 失败的分析。\n\n### Should-Fix 问题\n\n**R1-W1** [warning] N=8/16 对于研究\"test-time compute scaling\"而言范围过窄\n- 相关文献（Brown et al., 2024; Snell et al., 2025）通常测试到 N=64 或更大。\n- Few-NERD N=16 LP 仍有 +0.30pp gain，更大 N 可能有用。\n\n**R1-W2** [warning] Fine-tuned 4B-8B vs. Zero-shot 72B 的 scale/regime confound\n- 无法归因于 fine-tuning、model size 还是 model architecture。\n\n**R1-W3** [warning] Cross-model consistency 实验过于初步\n- 仅 1 个数据集（Few-NERD）+ 1 对模型（Qwen3-8B + LLaMA-3.1-8B），不足以支撑 general claim。\n\n**R1-W4** [warning] SciERC 部分关键分析基于 single seed\n- SciERC 是分析最详细的数据集，但部分分析 single seed。有 bootstrap CI 缓解但不够。\n\n**R1-W5** [warning] Trained verifier (LightGBM) 的负面结果可能不够 conclusive\n- 仅 SciERC 上测试，特征集有限（5个信号），cross-dataset transfer 负面可能是 domain shift。\n\n### 小问题\nM1-M6: Table 1 列名、Proposition 1 entity-wise independence 假设、Holm family 分组不一致、Figure 1 中间面板、T=0.5 LP 增幅、SciERC 551 instances 对 subgroup 分析不足\n\n### 主要优势\n1. 统计方法论远超 NLP 社区平均水平\n2. Degeneracy decomposition 提供 clean 理论框架\n3. 诊断框架的实用价值\n4. 极其详尽的附录（55个表格）\n5. 负面结果的诚实报告\n6. Entity-level construction 是 novel 且直觉合理的 idea\n\n---\n\n请对上述每个 Must-Fix (N1-N2) 和 Should-Fix (W1-W5) 问题给出 [AGREE] 或 [REBUT] 回应。"
  }
}
```

</details>

---


### Tool result

_source line 2742 · 2026-05-20T14:32:07.506088+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1615
}
```

</details>

---


### Assistant

_source line 2743 · 2026-05-20T14:32:10.741825+00:00_

交叉分享已发出，两位 Reviewer 正在互审对方意见。等待回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 206

## Round 206

2 recorded events


### User

_source line 2744 · 2026-05-20T14:32:13.588442+00:00_

[Reviewer 2 审稿结果]:
审稿报告已提交给 Review Director。

**核心判断**：Overall 3.0 (Findings)。

**四个 Must-Fix 问题**：
1. Entity-level construction 新颖性不足——缺引 EL4NER (2025)，改进幅度有限 (+1.40pp)
2. Degeneracy bound 太松 (3-12%)，不足以作为独立 contribution
3. "First systematic characterization" overclaim，需 scope down 到 NER
4. 参考文献存在年份错误、作者错误、疑似虚构引用 (hobelsberger2025systematic)

**主要优势**：correlation-selection gap 概念清晰有价值，实验设计系统全面，30 页附录展示了严谨的 robustness 分析。适合 Findings track 但未达主会议 novelty 门槛。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 2745 · 2026-05-20T14:32:25.132416+00:00_

R2 初审报告已确认收到。交叉分享请求已发送给两位 Reviewer，等待 [AGREE]/[REBUT] 回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 207

## Round 207

2 recorded events


### User

_source line 2746 · 2026-05-20T14:33:46.852511+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 交叉回应 — 对 Reviewer 2 审稿意见的逐条回应

---

### Must-Fix 问题

**[AGREE with nuance] R2-N1: Entity-level construction 新颖性被高估**

R2 的核心论点成立。论文在 Section 2 (p.2) 已明确引用 Xie et al. (2023a) 为 "the closest prior work to our entity-level construction"，说明作者知道 entity voting 不是全新的。但有两点需要区分：

1. **EL4NER 引用**: 若 EL4NER (arXiv:2505.23038, May 2025) 确实实现了 multi-LLM entity-level span extraction + type voting pipeline 且取得 SOTA，这是必须引用的相关工作。不过需要核实该文是否在本文提交截止日（ARR May 2026）前已公开。如果是，确实应引用并明确区分。

2. **MBR 框架的增量贡献**: 论文的 Proposition 1 (Appendix o.3, p.25) 将 entity construction 形式化为 balanced set-overlap 的 MBR decoding，且引入了 LP-weighted voting（权重 w_i 基于 LP 信号）。这与简单的 majority entity voting 有技术区别：LP-weighted construction 在 Few-NERD 上比 uniform construction 多 +0.30pp（Table 5, "LP-wtd" vs "uniform"列对比）。但这个增量是否足以支撑独立 contribution 值得商榷。

3. **我在自己的 N2 中已指出**: construction 效果不一致（Few-NERD +1.40pp 显著，SciERC +1.39pp 显著性存疑，CoNLL +0.02pp 无效），这与 R2 对 "+1.40pp 改进有限" 的判断一致。

**建议**: 同意 R2 的建议——将 construction 降级为 diagnostic-motivated ablation，而非 standalone contribution。同时补引 EL4NER 并明确 LP-weighted MBR 与 simple entity voting 的区别。

---

**[REBUT with partial agreement] R2-N2: Degeneracy decomposition 理论贡献过于 loose**

R2 称 "bound 仅能解释实际 gap 的 3-12%"——这一说法需要澄清。

1. **Equality vs. Bound**: 论文 Section 4 (p.4) 和 Section 6.3 给出的是 **decomposition equality** E[Δ|F₁] = (1−D)·G_nd，不是 upper bound。Table 28 (p.37) 的 "Bound verification" 展示实际 Δ 与 (1−D)·G_nd 的对比，数值上吻合度相当高（例如 SciERC Qwen3-8B: predicted 0.297 vs actual 通过 numerical verification 验证）。如果 R2 说的 "3-12%" 来自其他数字，需要具体指出。

2. **描述性统计量的价值**: D 确实是描述性统计量，但它的实用性在于将 selection failure 归因到一个可直接测量的 property——degeneracy rate。这使得论文的 diagnostic protocol (Appendix ab, p.34) 可以在第一步就通过测量 D 来判断 SC 是否有收益空间。这个实用价值不应被忽视。

3. **部分同意**: Proposition 1 的证明（Appendix o.3, p.25）确实是 MBR for balanced set-overlap 的相对直接推导。将其作为与 QE diagnostic 和 construction 并列的独立 contribution 可能确实高估了理论贡献。

**建议**: 部分同意降级为 analysis tool。但不同意 "仅解释 3-12%" 的判断——需要 R2 给出具体引用来源。Decomposition 的价值主要在实用层面（快速判断 SC 可行性），而非理论深度。

---

**[AGREE] R2-N3: "First systematic characterization" 声称过强**

完全同意。论文 Section 2 (p.2) 自己引用了多项相关系统性研究：
- Chen et al. (2025/2023): "Two Failures of Self-Consistency" — SC for multi-step reasoning 的系统分析
- Eikema et al. (2025): MBR decoding 的系统框架
- Brown et al. (2024): test-time compute scaling 的系统研究
- Kang et al. (2025): Self-Certainty for BoN selection

这些工作已经对 SC 的 failure modes、optimal aggregation 等做了系统研究，只是没有聚焦 NER/structured IE。论文的 "first" 应严格限定为 "for structured entity extraction tasks" 或 "in the NER domain"。当前 Abstract 中的 "first systematic characterization of self-consistency as a test-time scaling diagnostic" 过于宽泛。

---

**[AGREE] R2-N4: 参考文献错误**

我的独立引用验证（通过 verify_references 工具）完全印证了 R2 的发现：

| 问题 | 详情 | 我的验证结果 |
|------|------|------------|
| chen2025twofailures 年份 | bib=2025, 实际=2023 | ✓ 确认 (OpenAlex API返回2023) |
| feng2025optimal 作者 | bib首作=feng, API返回=austin | ✓ 确认 (需人工核实是否为first name confusion) |
| park2024grammar 作者 | bib首作=park, API返回=berg-kirkpatrick | ✓ 确认 |
| hobelsberger2025systematic | 未找到 (similarity=0.236) | ✓ 确认 (疑似虚构或极新preprint) |
| 17 orphan bib entries | 在 .bib 中但未被 \cite | ✓ 确认 (包括 suzgun2023crowd, wang2025gptner, openai2024o1 等) |

**补充**: 我的验证还发现 lightman2024verify ("Let's Verify Step by Step") 也未被 API 找到 (similarity=0.246)，但这是 OpenAI 的知名论文，属于 API 检索局限而非虚构。wang2025gptner 年份也有问题 (bib=2025, API=2023)，但它是 orphan entry 不影响正文。

**需要特别关注**: hobelsberger2025systematic 如果确实是虚构引用，这是严重的学术诚信问题。建议作者立即核实。

---

### Should-Fix 问题

**[AGREE] R2-W1: 模型多样性有限**

与我的 W2 一致。2 个 ~8B fine-tuned 模型 + 1 个 72B zero-shot 模型，缺少 closed-source 模型（GPT-4o, Claude 等）。特别是 zero-shot NER 场景下，closed-source 模型可能有不同的 degeneracy patterns。不过考虑到论文的 scope 和计算成本，这是一个可以接受的 limitation 而非致命缺陷。

---

**[AGREE with nuance] R2-W2: Diagnostic cascade 是描述性分析而非因果链**

R2 指出 cascade 的 "因果性" 问题是合理的。论文的 diagnostic cascade (degeneracy → headroom → LP compression) 展示的是 correlational structure：高 degeneracy 与低 selection gains 共现，但无法排除第三变量（如 task difficulty 同时驱动 degeneracy 和 selection failure）。

**但有两点缓解**：
1. Entity-level construction 实验（Section 6.1）部分建立了因果性：改变 aggregation 粒度（从 sample-level 到 entity-level）→ 在低 degeneracy 条件下改善 gains，在高 degeneracy 条件下无效。这与 cascade 的预测一致。
2. Epoch confound analysis (Appendix aa, p.31) 展示了 training convergence 如何 modulate degeneracy → 间接支持 degeneracy 的因果角色。

总体同意标注为 "descriptive diagnostic" 比 "causal chain" 更准确。

---

**[REBUT] R2-W3: 论文试图同时做太多事情（4 contributions 各自深度不够）**

部分不同意。R2 的判断适用于某些 contributions（construction 和 decomposition 确实单独来看偏浅），但论文的价值在于 **四个部分构成的整体故事**，而非单个 contribution 的深度：

1. **QE diagnostic** (Contribution 1) 本身就是一项全面的 empirical study——5 signals × 4 datasets × 3 model configs，附带严格的统计检验（Holm-Bonferroni k=57, bootstrap CI, MDE/power analysis）。我在自己的审稿中将统计方法论标注为"远超NLP社区平均水平"。这不是"浅"。
2. **Failure mode analysis** (Contribution 2) + **construction** (Contribution 3) + **decomposition** (Contribution 4) 共同回答了 "为什么SC对NER不work" + "怎么缓解" 的完整问题。拆成多篇反而会丢失叙事连贯性。

**但同意**: 如果按 R2 建议将 construction 降级为 ablation、decomposition 降级为 analysis tool，论文可以重新定位为 2 个 core contributions (QE diagnostic + failure mode analysis) + 2 个 supporting analyses (construction ablation + decomposition tool)，这样深度更集中。

---

**[AGREE conditionally] R2-W4: Missing related work**

无法独立核实 R2 列出的具体缺失引用（Beyond Majority Voting, Scalable BoN via Self-Certainty, Optimal Aggregation），但论文的 Related Work (Section 2) 确实聚焦于 SC 和 NER 的直接交叉，对 broader aggregation/selection 文献的覆盖可能不足。如果 R2 列出的工作确实相关（特别是 Self-Certainty for BoN selection — 论文已引用 Kang et al. 2025 但可能未充分讨论），应补充。

建议作者核实 R2 列出的具体引用并按相关性补充。

---

### 小问题 R2-M1 至 M6

大部分与我的小问题列表重叠或互补，不逐条回应。值得注意的是 R2-M1 (Table 1 列标题) 与我的 M1 相同——Table 1 的 "One score per input" 列确实容易误导。

---

### 综合评估

R2 给出 Overall 3.0 (Findings)，我给出 3.5 (Borderline Conference)。差异主要在于：

1. **统计方法论的权重**: 我对论文的统计严谨性（Holm-Bonferroni, bootstrap CI, MDE, power analysis, TOST equivalence）给予更高权重——这在 NLP 社区极为罕见，具有示范价值。R2 似乎更侧重 novelty。
2. **Construction novelty**: R2 的 EL4NER 引用如果确实相关，会进一步削弱 Contribution 3 的 novelty。我的评分未考虑 EL4NER（我的审稿中未发现该引用），如果确认，我可能也会降至 3.0-3.5 区间。
3. **"First systematic" claim**: 我同意 R2 的判断，这个 claim 需要限定 scope。

**如果作者按 R2 和我的建议修改**（限定 "first" scope、降级 construction 和 decomposition、修复引用、改善 framing），论文作为 Findings 是合适的——扎实的 diagnostic empirical study，统计方法论值得学习，但 novelty 和 practical impact 不足以支撑 Main Conference。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 2747 · 2026-05-20T14:33:53.836252+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 208

## Round 208

2 recorded events


### User

_source line 2748 · 2026-05-20T14:33:56.434895+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交。总结：

- **R2-N1 (construction novelty)**: AGREE with nuance — 论文已引 Xie et al. 但应补引 EL4NER，同意降级为 ablation
- **R2-N2 (decomposition loose)**: REBUT partially — 论文给的是 equality 非 bound，R2 的 "3-12%" 需要出处；同意降级为 analysis tool
- **R2-N3 ("first systematic" overclaim)**: AGREE — 应限定为 "for NER"
- **R2-N4 (reference errors)**: AGREE — 我的独立验证完全印证
- **R2-W1 (model diversity)**: AGREE
- **R2-W2 (descriptive not causal)**: AGREE with nuance — construction 实验部分建立因果性
- **R2-W3 (too many contributions)**: REBUT — 整体叙事有价值，但同意重新分层（2 core + 2 supporting）
- **R2-W4 (missing related work)**: AGREE conditionally — 需作者核实具体引用

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 2749 · 2026-05-20T14:34:05.013813+00:00_

R1 交叉回应已收到。R1 对 R2 的 4 个 Must-Fix 中 3 个 AGREE（N1/N3/N4），1 个 partial REBUT（N2 关于 bound vs equality 的区分）。关键共识正在形成：construction 降级 + overclaim 修正 + 引用修复。

等待 R2 对 R1 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 209

## Round 209

22 recorded events


### User

_source line 2750 · 2026-05-20T14:35:06.048949+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 — 交叉回应 Reviewer 1 审稿意见

---

### Must-Fix 问题

**[AGREE] R1-N1: "Correlation-Selection Gap" 对 4/5 信号是 structural tautology，framing 过度渲染 novelty**

同意。这是 R1 最尖锐的观察。论文自己在 §4 (page 4) 明确承认："four of five signals are instance-level aggregates that assign identical scores to all N candidates...selection failure is a design property, not an empirical finding." §1 Contribution #2 也写道 "That 4/5 signals are instance-level is definitional"。

但 Abstract 和 Introduction 的 framing 完全没有前置这个关键区分。Abstract 写 "We evaluate five confidence signals...all signals achieve reliable QE...but gains are absent...despite large oracle headrooms (the correlation-selection gap)" ——读者会以为 5 个信号都是 empirical failure，而非 4 个是 definitional + 1 个是 empirical。

真正的 empirical surprise（LP compression: within-instance range ≈0.041 nats，60% instances，§4 page 4; Figure 8 page 23 的 CDF 分析）在当前 framing 下被淹没。**建议修改 Abstract/Intro 将 structural/empirical 二分法前置，将论文的核心 empirical 贡献重新聚焦到 LP 的 compression failure 上。**

补充：我在自己的审稿中也指出了 overclaim 问题（我的 N3），但 R1 对 structural tautology 的诊断比我更精准——不仅是措辞问题，而是整个 framing architecture 需要重构。

---

**[AGREE] R1-N2: Construction mitigation 效果在数据集间不一致，p_adj 数值矛盾**

同意，这是一个需要修复的问题。

关于数据集不一致性：论文 §8 (page 8) 自己承认 "Entity construction yields significant gains only when degeneracy is low and oracle headroom is sufficient (Few-NERD: D=0.13%, headroom=1.2 1pp); on datasets where either condition fails, construction is ineffective。" CoNLL 上 -0.39pp 的负面结果表明 entity-level construction 不是一个 robust 的解决方案。

关于 p_adj 矛盾：§1 page 2 明确报告 SciERC construction p_adj=0.20（按 Holm 校正，construction family k=10），如果 Table 13 确实显示 p_adj=0.038，这可能源于 Holm family 分组不同（k=10 vs. 其他 k 值）。但无论原因如何，同一结果在不同位置给出不同 p_adj 而未解释差异，属于报告失误。

补充：我在自己的 N1 中从 novelty 角度批评了 entity-level construction（缺引 EL4NER），R1 从 empirical robustness 角度批评——两个视角叠加后，entity-level construction 作为独立 contribution 更难站住脚。

---

### Should-Fix 问题

**[AGREE] R1-W1: N=8/16 对 test-time compute scaling 研究范围过窄**

同意。Test-time scaling 文献（Brown et al., 2024; Snell et al., 2025）通常评估到 N=64+。论文仅在 Appendix r 报告了 N=16 结果，且 page 7 Table 3 显示 Few-NERD N=16 LP 仍有 +0.30pp gain，存在继续 scaling 的空间。

不过我补充一个缓解因素：NER 的 per-sample generation cost 显著高于 reasoning tasks（需要处理完整 entity set 而非单个 answer），因此 N=64 的计算成本远高于 math reasoning 场景。论文可以在 Discussion 中以 cost-efficiency 角度论证 N=8 的实际合理性，但当前完全没有讨论这一点。

---

**[AGREE] R1-W2: Fine-tuned 4B-8B vs. Zero-shot 72B 的 confound**

同意。我在自己的审稿 W1 中也指出了模型多样性不足。fine-tuning、model size、architecture 三个变量同时变化，无法归因。至少需要一个 fine-tuned 72B 或 zero-shot 8B 作为控制。

---

**[REBUT] R1-W3: Cross-model consistency 实验"过于初步"——部分反驳**

R1 说仅 1 个数据集 + 1 对模型不足以支撑 general claim。这点本身我同意——实验确实有限。但我认为 R1 对这个实验的期待可能过高。

看 §5.1 (page 5)：cross-model experiment 的定位是 "an exploratory extension combining 4 samples each from Qwen3-8B and LLaMA-3.1-8B"，且结果只是 "+0.32 pp over pure LLaMA sum"，95% CI 含 0。论文没有从这个实验中声称 general conclusion——它被标注为 exploratory，且放在 Adaptive Methods 部分而非 main results。

**但 R1 的 concern 本身是对的**：如果论文要在 §5.1 花半栏讨论 cross-model SC，reading expectation 是应该有更充分的 evidence。建议要么扩展实验，要么将其缩减为 1-2 句 footnote。

---

**[AGREE] R1-W4: SciERC 部分关键分析基于 single seed**

同意。论文在统计方法上非常严谨（bootstrap CI, Holm correction, permutation tests），但如果 SciERC 的 detailed diagnostic analyses（如 diagnostic cascade decomposition, Figure 3）是基于 single seed，则与论文的整体统计标准不一致。

Page 7 Table 3 的 caption 确认主结果用了 "3-seed mean; SciERC: single-seed, ρ: paired bootstrap"——SciERC 的 selection 分析确实是 single seed。考虑到 SciERC 仅 551 instances (page 4)，这对 subgroup 分析（如 high/low degeneracy split）的统计 power 确实不足。

---

**[REBUT] R1-W5: Trained verifier (LightGBM) 负面结果"不够 conclusive"——部分反驳**

R1 认为仅在 SciERC 上测试，特征集有限（5 signals），负面结果可能是 domain shift。

我部分反驳：

1. LightGBM 的 AUC=0.923±0.002 (§5.2, page 5) 表明特征集足以做 quality discrimination——问题不在于特征不够，而在于 discrimination 无法转化为 selection gain (+0.30pp)。这恰恰是 correlation-selection gap 的又一实例。

2. Cross-dataset transfer 确实是负面的（page 22: "Cross-dataset transfer to Few-NERD is negative: −0.70pp"），但这更可能反映 NER 数据集间 entity schema 差异（SciERC 6 types vs. Few-NERD 66 types），而非简单 domain shift。论文对此有合理分析（page 22 §h.3）。

3. 但我同意 R1 的 concern 方向：**仅 1 个训练数据集上的 negative result 不足以判定 "learned verifiers cannot close the gap"**。在 Few-NERD（更多 instances, 更多 entity types）上训练 verifier 可能有不同结果。论文应 soften §5.2 的结论从 "cannot close" 到 "do not close in our setting"。

---

### 关于 R1 主要优势评价的补充意见

**R1 Strength #2: "Degeneracy decomposition provides clean theoretical framework"——我不同意**

R1 评价 degeneracy decomposition 为 "clean theoretical framework"，但我在自己的审稿 N2 中认为 bound 太松（仅解释 3-12% 的 gap, page 6 §6.3, page 26 Appendix o.4）。E[ΔF₁] ≤ (1−D)·G_adj 本质上是 MBR balanced set-overlap 的直接推导，理论 novelty 有限；D 只是 degeneracy rate 的描述统计量，不提供优化方向。"Clean" 和 "useful" 不能等同——一个 captures only 3-12% of variance 的 bound 的实用价值存疑。

**R1 Strength #6: "Entity-level construction is novel and intuitive"——我不同意**

R1 评价 entity-level construction 为 "novel"。但如我在 N1 中指出：(a) EL4NER (arXiv:2505.23038, May 2025) 已实现 entity-level span extraction + type voting 的两阶段 ensemble NER；(b) Xie et al. (2023a) 已是 entity-level voting 的先驱；(c) 论文自己承认灵感来自 Florian et al. (2003) 的 ensemble NER。将已有 idea 在 SC 框架下重新包装，novelty 有限。"Intuitive" 我同意，但 "novel" 我不同意。

---

### R2 vs R1 评分差异说明

R1 给 3.5 (Borderline Conference)，我给 3.0 (Findings)。差异主要源于：

1. **对 entity-level construction novelty 的判断**：R1 认为 novel, 我认为 incremental（EL4NER 未被引用）。
2. **对 degeneracy theory 的评价**：R1 认为 clean framework, 我认为 bound 太松不足以作为 contribution。
3. **对 overclaiming 严重程度的判断**：R1 准确诊断了 structural tautology 问题但仍给 3.5，我认为 Abstract/Intro 的 framing 问题 + entity-level overclaim + theory overclaim 叠加后，论文需要 significant reframing 才能达到主会议水平。

**共识点**：两位 Reviewer 一致认为 (1) 核心 empirical finding（LP compression failure）有价值；(2) 统计方法论优于 NLP 社区平均；(3) 论文需要 scope down overclaims；(4) 模型/scaling 范围有限。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 2751 · 2026-05-20T14:35:39.117041+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': '初始化：获取项目概览 + 检查论文文件', 'status': 'completed', 'activeForm': '获取项目概览和检查论文文件'}, {'content': 'Step 0: Venue 调研（WebSearch EMNLP 2026 CFP）', 'status': 'completed', 'activeForm': '搜索 EMNLP 2026 CFP 和格式要求'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.6/0.7: 派发视觉审查 + 分配 Reviewer 任务', 'status': 'completed', 'activeForm': '派发视觉审查并分配 Reviewer 任务'}, {'content': '收集 R1 + R2 审稿报告', 'status': 'completed', 'activeForm': '收集审稿报告'}, {'content': 'Step 2: 交叉分享', 'status': 'completed', 'activeForm': '交叉分享 Reviewer 意见'}, {'content': 'Step 3: 收敛判断', 'status': 'completed', 'activeForm': '判断是否收敛'}, {'content': 'Step 4: 汇总报告 + 投递', 'status': 'in_progress', 'activeForm': '汇总审稿报告并投递'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': '初始化：获取项目概览 + 检查论文文件', 'status': 'completed', 'activeForm': '获取项目概览和检查论文文件'}, {'content': 'Step 0: Venue 调研（WebSearch EMNLP 2026 CFP）', 'status': 'completed', 'activeForm': '搜索 EMNLP 2026 CFP 和格式要求'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.6/0.7: 派发视觉审查 + 分配 Reviewer 任务', 'status': 'completed', 'activeForm': '派发视觉审查并分配 Reviewer 任务'}, {'content': '收集 R1 + R2 审稿报告', 'status': 'completed', 'activeForm': '收集审稿报告'}, {'content': 'Step 2: 交叉分享', 'status': 'completed', 'activeForm': '交叉分享 Reviewer 意见'}, {'content': 'Step 3: 收敛判断', 'status': 'completed', 'activeForm': '判断是否收敛'}, {'content': 'Step 4: 汇总报告 + 投递', 'status': 'in_progress', 'activeForm': '汇总审稿报告并投递'}]"
  }
}
```

</details>

---


### Tool result

_source line 2752 · 2026-05-20T14:35:39.117495+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2753 · 2026-05-20T14:35:39.970418+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 2754 · 2026-05-20T14:35:40.472562+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-20T14:20:00.726427+00:00\", \"completed_at\": \"2026-05-20T14:24:24.116789+00:00\", \"findings\": [{\"severity\": \"critical\", \"dimension\": \"page 7\", \"message\": \"Display items 严重过密：4 个表格（Table 2/3/4/5）+ 1 个 figure（Figure 3）挤在同一页，每个 item 空间被严重压缩。Figure 3 的条形图非常小，文字和数据标签可读性显著下降。相比之下，相邻的页 6 和页 8 均为纯文本无任何 display item——分布极不均匀。建议将 Table 4/5 或 Figure 3 移至页 6 或页 8 以平衡视觉节奏\"}, {\"severity\": \"warning\", \"dimension\": \"page 6\", \"message\": \"纯文本页：Section 6.3 + Section 7 开头 + 7.1 + 7.2，整页无任何 figure/table/equation 穿插，紧接同样纯文本的页 8，中间仅隔过度拥挤的页 7。审稿人在此区域会感到阅读单调\"}, {\"severity\": \"warning\", \"dimension\": \"page 8\", \"message\": \"纯文本页：Section 7.4/7.5 + Discussion + Conclusion + Limitations 起始，整页无 display item。与页 6 形成\\\"文-密-文\\\"的不良节奏\"}, {\"severity\": \"warning\", \"dimension\": \"page 42\", \"message\": \"末页仅 Table 55 占 ~25% 面积，~75% 空白。可将前页部分内容后移或合并附录末尾表格以填充空间\"}, {\"severity\": \"warning\", \"dimension\": \"page 34\", \"message\": \"Appendix 评估协议（Evaluation Protocol）结束于页面 ~40% 处，下方 ~60% 大面积空白\"}, {\"severity\": \"warning\", \"dimension\": \"pages 36-41\", \"message\": \"附录表格页极度密集（每页 7-8 个小表格），部分表格字号偏小，在 150dpi 下已接近可读性边界。虽然附录可接受更高密度，但仍建议确认打印时字号 ≥7pt\"}, {\"severity\": \"info\", \"dimension\": \"page 3\", \"message\": \"Figure 1 使用绿/蓝/橙色区分三个面板，颜色区分度良好，色盲友好\"}, {\"severity\": \"info\", \"dimension\": \"page 18\", \"message\": \"Figure 6 的 heatmap 使用红-黄-绿渐变色阶，红绿色盲读者可能难以区分极端值。建议考虑 viridis 或 blue-orange 色阶替代\"}, {\"severity\": \"info\", \"dimension\": \"page 5\", \"message\": \"Figure 2 bar chart 字号偏小但尚可读；页面同时包含 Section 5/6 的多个 subsection 开头，布局紧凑但未溢出\"}, {\"severity\": \"info\", \"dimension\": \"pages 1-2\", \"message\": \"前两页均为纯文本（Title/Abstract/Intro + Background），首个视觉锚点推迟到第 3 页。非硬性问题——Introduction 内容确实需要文字铺垫——但若能在页 2 右栏底部预览 Figure 1 会更佳\"}, {\"severity\": \"info\", \"dimension\": \"全文\", \"message\": \"所有表格使用 booktabs 风格（\\\\toprule/\\\\midrule/\\\\bottomrule），无竖线，最优值加粗标注——排版
…[truncated 404 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 2755 · 2026-05-20T14:35:40.472894+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 2756 · 2026-05-20T14:35:41.878048+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 1405
}
```

</details>

---


### Tool call

_source line 2757 · 2026-05-20T14:35:41.930305+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "review_issues",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "review_issues",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts",
    "output_mode": "files_with_matches"
  }
}
```

</details>

---


### Tool result

_source line 2758 · 2026-05-20T14:35:42.031101+00:00_

Found 3 files
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260516T092241/logs/review_median.log
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260516T092241/logs/phase2_worst_attempt0.log
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T203201/logs/phase2_worst_attempt0.log

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Grep",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 2759 · 2026-05-20T14:35:46.999120+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review_issues.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review_issues.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 2760 · 2026-05-20T14:35:47.049753+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2761 · 2026-05-20T14:35:50.059892+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_project_file",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 2762 · 2026-05-20T14:35:50.110452+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2763 · 2026-05-20T14:35:53.191510+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 2764 · 2026-05-20T14:35:53.542199+00:00_

1	issues:
2	  # ===== 历史 resolved issues =====
3	  - id: "R1-W1"
4	    summary: "Few-NERD 3-epoch vs SciERC 5-epoch 训练时长混淆效应"
5	    category: experiment
6	    severity: critical
7	    status: resolved
8	    first_raised_round: 1
9	    last_seen_round: 19
10	    resolution: "Reviewer PASS: 脚注+§4.1+appendix epoch data 一致。tab:epoch_confound caption 已注明 5K subsample。"
11	    resolution_round: 19
12	
13	  - id: "R1-W2"
14	    summary: "\"Two jointly necessary conditions\" 因果性表述过强"
15	    category: framing
16	    severity: critical
17	    status: resolved
18	    first_raised_round: 1
19	    last_seen_round: 21
20	    resolution: "全文降级为 empirical pattern/factors。Reviewer 确认正文+appendix 15处+4处残留全部修复，0 因果语言残留。"
21	    resolution_round: 21
22	
23	  - id: "R2-N1"
24	    summary: "Contribution 1 'methodological premise' 是定义推论"
25	    category: framing
26	    severity: critical
27	    status: resolved
28	    first_raised_round: 1
29	    last_seen_round: 19
30	    resolution: "Reviewer PASS: 标题改为 'Quality estimation framework'; Abstract 干净。"
31	    resolution_round: 19
32	
33	  - id: "R2-N2"
34	    summary: "与 MBR 文献差异化定位不够锐利"
35	    category: framing
36	    severity: warning
37	    status: resolved
38	    first_raised_round: 1
39	    last_seen_round: 19
40	    resolution: "Reviewer PASS: Introduction 区分清晰，ρ=0.52 数据一致。"
41	    resolution_round: 19
42	
43	  - id: "R2-N4"
44	    summary: "模型规模 3B-8B，70B+ 未知"
45	    category: experiment
46	    severity: info
47	    status: resolved
48	    first_raised_round: 1
49	    last_seen_round: 19
50	    resolution: "Round 20 检查 PASS: limitations.tex '4B-8B scale; 70B+ untested'。"
51	    resolution_round: 19
52	
53	  - id: "R1-W3"
54	    summary: "2-seed 统计效力不足"
55	    category: experiment
56	    severity: warning
57	    status: resolved
58	    first_raised_round: 1
59	    last_seen_round: 19
60	    resolution: "Reviewer PASS: tab:fewnerd 脚注 '3-seed mean: +0.04±0.48pp'。"
61	    resolution_round: 19
62	
63	  - id: "R1-W4"
64	    summary: "Per-en
…[truncated 32607 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 350
}
```

</details>

---


### Tool call

_source line 2765 · 2026-05-20T14:40:21.502543+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "struct_self_consist_ie",
  "issues_yaml": "issues:\n  # ===== 历史 resolved issues (保留，省略细节) =====\n  - id: \"R1-W1\"\n    summary: \"Few-NERD 3-epoch vs SciERC 5-epoch 训练时长混淆效应\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Reviewer PASS: 脚注+§4.1+appendix epoch data 一致。tab:epoch_confound caption 已注明 5K subsample。\"\n    resolution_round: 19\n\n  - id: \"R1-W2\"\n    summary: \"\\\"Two jointly necessary conditions\\\" 因果性表述过强\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 21\n    resolution: \"全文降级为 empirical pattern/factors。Reviewer 确认正文+appendix 15处+4处残留全部修复，0 因果语言残留。\"\n    resolution_round: 21\n\n  - id: \"R2-N1-old\"\n    summary: \"Contribution 1 'methodological premise' 是定义推论\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Reviewer PASS: 标题改为 'Quality estimation framework'; Abstract 干净。\"\n    resolution_round: 19\n\n  - id: \"R2-N2-old\"\n    summary: \"与 MBR 文献差异化定位不够锐利\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Reviewer PASS: Introduction 区分清晰，ρ=0.52 数据一致。\"\n    resolution_round: 19\n\n  - id: \"R2-N4-old\"\n    summary: \"模型规模 3B-8B，70B+ 未知\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Round 20 检查 PASS: limitations.tex '4B-8B scale; 70B+ untested'。\"\n    resolution_round: 19\n\n  - id: \"R1-W3-old\"\n    summary: \"2-seed 统计效力不足\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Reviewer PASS: tab:fewnerd 脚注 '3-seed mean: +0.04±0.48pp'。\"\n    resolution_round: 19\n\n  - id: \"R1-W4-old\"\n    summary: \"Per-entity-type non-independence\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Reviewer PASS: appendix ICC=-0.004 written。\"\n    resolution_round: 19\n\n  - id: \"R1-W5-old\"\n    summary: \"\\\"Supervised verifier\\\" framing 误导\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Reviewer PASS: 'supervised verifier' 0 matches。\"\n    resolution_round: 19\n\n  - id: \"R1-W6\"\n    summary: \"Degeneracy 定义需区分\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Round 20 检查 PASS: introduction.tex 有完整定义。\"\n    resolution_round: 19\n\n  - id: \"R1-W7\"\n    summary: \"SciERC greedy F1 不一致\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Round 20 检查 PASS: 脚注解释了 3-seed mean 和 epoch 差异。\"\n    resolution_round: 19\n\n  - id: \"R2-W1-old\"\n    summary: \"Abstract 数字过载\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Reviewer PASS: Abstract 含 3 个数字 (≤3)。\"\n    resolution_round: 19\n\n  - id: \"R2-W2-old\"\n    summary: \"Actionable contribution 偏薄\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 21\n    resolution: \"Conclusion 新增 practitioner guidance。\"\n    resolution_round: 21\n\n  - id: \"R2-W3-old\"\n    summary: \"Discussion 过于碎片化\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"5 段合并完成。\"\n    resolution_round: 19\n\n  - id: \"R2-W5-old\"\n    summary: \"核心数字跨 section 重复\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"属正常范围。\"\n    resolution_round: 19\n\n  - id: \"R2-W4-baseline\"\n    summary: \"缺少 baseline signals\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Round 20 检查 PASS。\"\n    resolution_round: 19\n\n  - id: \"R2-W4-re\"\n    summary: \"RE extension preliminary 但引用频繁\"\n    category: framing\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Round 20 检查 PASS。\"\n    resolution_round: 19\n\n  - id: \"R1-MR1\"\n    summary: \"缺失引用: Geifman & El-Yaniv 2017, XGrammar 等\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 20\n    resolution: \"Paper Agent 补全 4 篇。\"\n    resolution_round: 20\n\n  - id: \"R19-I8\"\n    summary: \"Table 3 EM/VC 缺 p-values\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    resolution: \"Reviewer PASS。\"\n    resolution_round: 19\n\n  - id: \"R19-I9\"\n    summary: \"Per-type LP selection 异质性\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    resolution: \"Reviewer PASS。\"\n    resolution_round: 19\n\n  - id: \"R19-DATA1\"\n    summary: \"LLaMA CoNLL degeneracy 86.4% vs 89.2%\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    resolution: \"根因修复完成。\"\n    resolution_round: 19\n\n  - id: \"R2-N3-old\"\n    summary: \"Title scope: 'Structured IE' 过宽\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 21\n    resolution: \"Title 已为 NER-specific。Reviewer 确认无需修改。\"\n    resolution_round: 21\n\n  - id: \"R21-C1\"\n    summary: \"正文页数超限 (~9.5 页 vs ACL 8 页限制)\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"Discussion 3段压缩 + Conclusion 压缩。Reviewer PASS: Sections 1-9 + Limitations 在 page 8 结束。\"\n    resolution_round: 21\n\n  - id: \"R21-C2\"\n    summary: \"'两个条件'框架跨数据集经验基础不足（仅 3 数据点）\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"全文 15 处降级 + appendix 4 处残留修复。Reviewer 确认 0 因果语言残留。\"\n    resolution_round: 21\n\n  - id: \"R21-W1\"\n    summary: \"Epoch confound 对 headline result 的影响正文处理不充分\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"experiments.tex 新增 epoch-controlled comparison。\"\n    resolution_round: 21\n\n  - id: \"R21-W2\"\n    summary: \"SciERC 作为 primary test bed 系统性 underpowered\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"Few-NERD 定位为 'definitive test'。\"\n    resolution_round: 21\n\n  - id: \"R21-W3\"\n    summary: \"DALS 定位与诊断性论文冲突 + ε data-snooping\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"DALS 已移入 appendix。\"\n    resolution_round: 21\n\n  - id: \"R21-W4\"\n    summary: \"新颖性增量需更精确定位\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"Intro L8 强化。\"\n    resolution_round: 21\n\n  - id: \"R21-W5\"\n    summary: \"LP ρ 跨表不一致 (0.205 vs 0.215)\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"审计确认论文全文统一使用 0.205。\"\n    resolution_round: 21\n\n  - id: \"R21-W6\"\n    summary: \"Table 3 的 7 个连续脚注\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"7→2 脚注。\"\n    resolution_round: 21\n\n  - id: \"R21-W7\"\n    summary: \"Greedy F1 多表数值不一致 (4 values)\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"Method §3.3 列出 4 值 + 3 类 protocol variants。\"\n    resolution_round: 21\n\n  - id: \"R21-I1\"\n    summary: \"Appendix 残留实验标识\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"全文搜索确认无残留。\"\n    resolution_round: 21\n\n  - id: \"R21-I2\"\n    summary: \"'Capability trap' 措辞过强\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"统一使用 'capability-diversity tension'。\"\n    resolution_round: 21\n\n  - id: \"R21-I3\"\n    summary: \"3 处 -ing 短语残留\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"3 处改写完成。\"\n    resolution_round: 21\n\n  - id: \"R21-MR1\"\n    summary: \"缺失引用: Farquhar et al., Chen et al. pass@k\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"已补入 Related Work。\"\n    resolution_round: 21\n\n  - id: \"R21-Q3\"\n    summary: \"Per-entity-type ρ=-0.881 effective df 问题\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"Appendix 已有 df=4 adjustment。\"\n    resolution_round: 21\n\n  - id: \"R22-N1\"\n    summary: \"正文再次超页约 2 页\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 23\n    resolution: \"Multiple compression rounds completed. ≤8 pages confirmed.\"\n    resolution_round: 23\n\n  - id: \"R22-N2\"\n    summary: \"标题暗示纯 negative result\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 23\n    resolution: \"Title updated to cover both diagnostic and resolving contributions.\"\n    resolution_round: 23\n\n  - id: \"R22-W1\"\n    summary: \"correlation-selection gap 概念缺乏理论深度\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 24\n    resolution: \"D162: 23-config 回归 R²=-8.53，公式彻底失败。删除公式，改为定性叙述三因素影响。Paper Agent 已执行。\"\n    resolution_round: 24\n\n  - id: \"R22-W2\"\n    summary: \"Abstract 中 LP 和 AUROC 缩写未展开\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 23\n    resolution: \"LP and AUROC expanded in Abstract.\"\n    resolution_round: 23\n\n  - id: \"R22-W3\"\n    summary: \"LP-alignment gating protocol 使用 test set 做 probe\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 23\n    resolution: \"Dev set gating implemented.\"\n    resolution_round: 23\n\n  - id: \"R22-W4\"\n    summary: \"SciERC seed sensitivity 高 (σ=0.48 pp)\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 23\n    resolution: \"Switched to multi-seed reporting throughout.\"\n    resolution_round: 23\n\n  - id: \"R22-W5\"\n    summary: \"Entity construction 阈值 θ 跨数据集不一致\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 24\n    resolution: \"Paper Agent R24 Patch: 正文 'tuning-free' → 'empirically robust default'; Table 5 caption → 'default heuristic'。\"\n    resolution_round: 24\n\n  - id: \"R22-W6\"\n    summary: \"'the correct self-consistency analogy' 措辞过于绝对\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 23\n    resolution: \"Changed to 'a more effective self-consistency analogy'.\"\n    resolution_round: 23\n\n  - id: \"R22-W7\"\n    summary: \"仅测试 LoRA 微调但 claim 范围不限定\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 22\n    last_seen_round: 26\n    mentions:\n      - round: 22\n        reviewers: [1, 2]\n        note: \"所有实验均为 LoRA fine-tuned models。\"\n      - round: 23\n        reviewers: [1, 2]\n        note: \"Introduction qualified with 'fine-tuned 4B-8B models'.\"\n      - round: 24\n        reviewers: [1, 2]\n        note: \"R24：scope 声明在 Introduction 和 Limitations 中已存在。72B zero-shot 实验将直接回应此问题。\"\n      - round: 25\n        reviewers: [1, 2]\n        note: \"72B zero-shot 已加入但 API 模型仍缺。\"\n      - round: 26\n        reviewers: [1, 2]\n        note: \"R26-R1-W2 + R2-W1: 仅2个~8B fine-tuned + 1个72B zero-shot。缺closed-source模型。72B结果仅在Appendix。scale/regime/architecture三因素混淆。\"\n\n  - id: \"R22-I1\"\n    summary: \"实体匹配标准分散在 §3.2 各段落中\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 22\n    last_seen_round: 25\n    mentions:\n      - round: 26\n        reviewers: []\n        note: \"本轮未提及，可能已修复，待 Research Director 确认\"\n\n  - id: \"R22-I2\"\n    summary: \"冠词错误 + 引用格式不一致\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 23\n    resolution: \"Fixed.\"\n    resolution_round: 23\n\n  - id: \"R22-I3\"\n    summary: \"Figure 3 scatter plot 标签在打印尺寸下可能难辨\"\n    category: format\n    severity: info\n    status: open\n    first_raised_round: 22\n    last_seen_round: 26\n    mentions:\n      - round: 25\n        reviewers: [1, 2]\n        note: \"视觉审查确认 Figure 3 过小（p7），R1 提到 Figure 1 面板注释 6-7pt。\"\n      - round: 26\n        reviewers: [1]\n        note: \"R26视觉审查再次确认p7 display items过密，Figure 3可读性差。\"\n\n  - id: \"R22-MR1\"\n    summary: \"缺失引用: ensemble-based IE, Xie et al. 2023\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 24\n    resolution: \"Paper Agent R24 Patch: LLM-Blender + CISC/Self-Certainty 技术差异 + orphan bib 清理。xie2023zeroshot 恢复引用。\"\n    resolution_round: 24\n\n  - id: \"R22-FIG1\"\n    summary: \"fig_overview 缺少 Construction 贡献 + 残留 RE 文字\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 23\n    resolution: \"fig_overview regenerated as three-column layout.\"\n    resolution_round: 23\n\n  - id: \"R22-FIG2\"\n    summary: \"fig_selection_gap caption 仍引用旧双面板格式\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 23\n    resolution: \"Regenerated as single-panel NER-only.\"\n    resolution_round: 23\n\n  - id: \"R23-N1\"\n    summary: \"Entity-level construction 新颖性不足\"\n    category: framing\n    severity: critical\n    status: in_progress\n    first_raised_round: 23\n    last_seen_round: 26\n    mentions:\n      - round: 23\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 独立列为 critical。\"\n      - round: 24\n        reviewers: [1, 2]\n        note: \"降级为 diagnostic-motivated mitigation。R24 Patch 完成。\"\n      - round: 25\n        reviewers: [1, 2]\n        note: \"R2 再次列为 critical。R1 REBUT。Director 判断维持 resolved。\"\n      - round: 26\n        reviewers: [1, 2]\n        note: \"R26再次独立提出。R2-N1: 缺引EL4NER (arXiv:2505.23038)，+1.40pp改进有限，本质是已有entity voting的MBR包装。R1交叉AGREE降级为ablation。共识: construction不应作为standalone contribution。另需补引EL4NER。\"\n    action_items:\n      - round: 26\n        action: \"补引EL4NER并区分(单模型SC vs 多模型ensemble)。确认construction在正文中已降级为diagnostic-motivated ablation而非contribution。\"\n        assigned_to: research_director\n        status: open\n\n  - id: \"R23-N2\"\n    summary: \"Correlation-selection gap 部分 by construction（framing tautology）\"\n    category: framing\n    severity: critical\n    status: in_progress\n    first_raised_round: 23\n    last_seen_round: 26\n    mentions:\n      - round: 23\n        reviewers: [1, 2]\n        note: \"R2 列为 critical，R1 部分同意。\"\n      - round: 24\n        reviewers: [1, 2]\n        note: \"R1 rebuttal 有效——MBR consensus-proximity 确实给不同 sample 赋不同分数。\"\n      - round: 25\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 再次独立提出。\"\n      - round: 26\n        reviewers: [1, 2]\n        note: \"R26两位Reviewer再次独立提出且交叉后完全共识。R1-N1: 4/5信号by construction无法做selection，论文§4自承'design property not empirical finding'，但Abstract/Intro未前置此区分。R2交叉AGREE并加强: 真正empirical surprise是LP compression（0.041 nats），被当前framing淹没。共识: 必须重构Abstract/Intro将structural/empirical二分法前置。\"\n    action_items:\n      - round: 26\n        action: \"重构Abstract和Introduction: (1) 前置4/5信号是instance-level的structural limitation; (2) 聚焦LP compression作为核心empirical finding; (3) 移除对instance-level信号selection failure的'surprising'/'diagnose'措辞。\"\n        assigned_to: research_director\n        status: open\n\n  - id: \"R23-N3\"\n    summary: \"Expected selection gain 'bound' 中 g(·) 未定义\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 23\n    last_seen_round: 23\n    resolution: \"Changed to 'approximately factored as'. Framed as heuristic.\"\n    resolution_round: 23\n\n  - id: \"R23-W1\"\n    summary: \"ε=0.05 non-tied subset 是 post-hoc 最优切点\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 23\n    last_seen_round: 23\n    resolution: \"标记为 exploratory。\"\n    resolution_round: 23\n\n  - id: \"R23-W2\"\n    summary: \"Complementarity claim 仅基于 2 informative data points\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 23\n    last_seen_round: 23\n    resolution: \"Softened scope.\"\n    resolution_round: 23\n\n  - id: \"R23-W3\"\n    summary: \"Abstract 信息密度过高\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 23\n    last_seen_round: 23\n    resolution: \"Reduced to 4 key numbers.\"\n    resolution_round: 23\n\n  - id: \"R23-W4\"\n    summary: \"Table 4 (entity construction) 缺少 multi-seed ±σ\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 23\n    last_seen_round: 23\n    resolution: \"Updated with multi-seed mean±σ.\"\n    resolution_round: 23\n\n  - id: \"R23-I1\"\n    summary: \"Figure 1 caption ρ scope 不一致\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 23\n    last_seen_round: 23\n    resolution: \"Caption updated.\"\n    resolution_round: 23\n\n  - id: \"R23-I2\"\n    summary: \"WNUT-17 正文分析不足\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 23\n    last_seen_round: 26\n    mentions:\n      - round: 26\n        reviewers: []\n        note: \"本轮未提及，可能已修复，待 Research Director 确认\"\n\n  - id: \"R23-MR1\"\n    summary: \"缺失引用: Florian 2003, Luo 2023, Wiher 2022\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 23\n    last_seen_round: 24\n    resolution: \"合并到 R22-MR1 统一处理完成。\"\n    resolution_round: 24\n\n  # ===== Round 24 issues =====\n\n  - id: \"R24-N1\"\n    summary: \"分解公式 E[ΔF1]≈(1-d)·Δ_oracle·g(ρ_within) 仅 3 macro-level data points 验证\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 24\n    last_seen_round: 24\n    resolution: \"D162: 23-config 回归 R²=-8.53，公式完全无预测力。删除公式，改为定性叙述三因素影响。\"\n    resolution_round: 24\n\n  - id: \"R24-N2\"\n    summary: \"Gating protocol 循环性 + 验证不足\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 24\n    last_seen_round: 24\n    resolution: \"Bootstrap CI 完成：τ=0.3 位于稳定区间中心。Paper Agent 已实现三路路由。\"\n    resolution_round: 24\n\n  - id: \"R24-W1\"\n    summary: \"'Resolving' framing 过强：entity construction 仅恢复 8-11% oracle headroom\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 24\n    last_seen_round: 24\n    resolution: \"Paper Agent R24 Patch: Title 'Resolving' → 'Addressing', Contribution 3 降级。\"\n    resolution_round: 24\n\n  - id: \"R24-W2\"\n    summary: \"SciERC selection 结果 underpowered (n=529, MDE≈1.5pp)\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 24\n    last_seen_round: 24\n    resolution: \"Paper Agent R24 Patch: SciERC selection 结果处加 detection threshold caveat。\"\n    resolution_round: 24\n\n  - id: \"R24-W3\"\n    summary: \"Related Work 缺少与 CISC/Self-Certainty 技术差异对比\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 24\n    last_seen_round: 24\n    resolution: \"Paper Agent R24 Patch: RW 增加 2 句技术差异。\"\n    resolution_round: 24\n\n  - id: \"R24-W4\"\n    summary: \"English-only + NER-heavy 泛化局限未在 Limitations 讨论\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 24\n    last_seen_round: 24\n    resolution: \"Paper Agent R24 Patch: Limitations 增加 1 句。\"\n    resolution_round: 24\n\n  - id: \"R24-W5\"\n    summary: \"Self-Certainty (Kang 2025) 和 P(True) (Kadavath 2022) 未测试\"\n    category: experiment\n    severity: warning\n    status: wont_fix\n    first_raised_round: 24\n    last_seen_round: 26\n    resolution: \"DDL 前无法新增 signal 实验。已在 Limitations 列出。\"\n    mentions:\n      - round: 26\n        reviewers: [1, 2]\n        note: \"R26未直接再提，但R2-W3指出缺少PTrue/Self-Certainty等近期信号。论文在Discussion §8已提及作为future direction。\"\n\n  - id: \"R24-W6\"\n    summary: \"Appendix D 'as a reviewer correctly noted' 暗示审稿历史\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 24\n    last_seen_round: 24\n    resolution: \"Paper Agent R24 Patch: 删除，改为直接陈述。\"\n    resolution_round: 24\n\n  - id: \"R24-I1\"\n    summary: \"Table 2 中 EM/VC 的 p 值标 '---'\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 24\n    last_seen_round: 24\n    resolution: \"'---' → 'n/a†' + caption footnote。\"\n    resolution_round: 24\n\n  - id: \"R24-I2\"\n    summary: \"F1 metric 术语不统一\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 24\n    last_seen_round: 24\n    resolution: \"Paper Agent R24 Patch: method.tex 加定义。\"\n    resolution_round: 24\n\n  - id: \"R24-I3\"\n    summary: \"orphan bib entries 待清理\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 24\n    last_seen_round: 24\n    resolution: \"Paper Agent R24 Patch: 删除 8 条 + xie2023zeroshot 恢复。\"\n    resolution_round: 24\n\n  - id: \"R24-I4\"\n    summary: \"SJ 分母边界情况未讨论\"\n    category: method\n    severity: info\n    status: resolved\n    first_raised_round: 24\n    last_seen_round: 24\n    resolution: \"Paper Agent R24 Patch: footnote 补充。\"\n    resolution_round: 24\n\n  - id: \"R24-I5\"\n    summary: \"Abstract ρ up to 0.45 取自 CoNLL EM（最易数据集）\"\n    category: writing\n    severity: info\n    status: in_progress\n    first_raised_round: 24\n    last_seen_round: 26\n    mentions:\n      - round: 26\n        reviewers: []\n        note: \"本轮未直接提及。\"\n\n  # ===== Round 25 issues (更新状态) =====\n\n  - id: \"R25-N1\"\n    summary: \"Cross-dataset 分析（n=23, ρ=0.052, p=0.81）严重 underpowered，不能支持 null 结论\"\n    category: experiment\n    severity: critical\n    status: in_progress\n    first_raised_round: 25\n    last_seen_round: 25\n    mentions:\n      - round: 25\n        reviewers: [1, 2]\n        note: \"n=23 power 仅约 50% for ρ=0.4。结论过强。\"\n      - round: 26\n        reviewers: []\n        note: \"R26未直接提及此specific null finding。论文§7.3现报告post-hoc power analysis (80% power requires n≈85 for ρ=0.3)。\"\n\n  - id: \"R25-N2\"\n    summary: \"§5.1 Cross-Model SC ('preliminary') 和 §5.3 SCD ('ongoing') 包含未完成工作\"\n    category: framing\n    severity: critical\n    status: in_progress\n    first_raised_round: 25\n    last_seen_round: 26\n    mentions:\n      - round: 25\n        reviewers: [1, 2]\n        note: \"§5.3 完全无实验结果。ARR 提交 incomplete work 会被 AC 视为 premature。\"\n      - round: 26\n        reviewers: [1, 2]\n        note: \"R26-R1-W3: cross-model仅1数据集1对模型，不足以支撑general claim。R2交叉REBUT: 论文标注为exploratory。但R2同意若保留需补实验或缩减为footnote。§5.3 SCD不再出现。\"\n    action_items:\n      - round: 26\n        action: \"§5.1 cross-model内容要么扩展到多数据集多模型，要么缩减为1-2句footnote/future work。确认§5.3已删除。\"\n        assigned_to: research_director\n        status: in_progress\n\n  - id: \"R25-N3\"\n    summary: \"NER-only 实验无法支撑 'structured prediction' framing\"\n    category: framing\n    severity: critical\n    status: in_progress\n    first_raised_round: 25\n    last_seen_round: 26\n    mentions:\n      - round: 25\n        reviewers: [2]\n        note: \"Abstract/Intro 叙事推广到 structured prediction，但仅有 NER 实验。\"\n      - round: 26\n        reviewers: [1, 2]\n        note: \"R26-R2-N3: 'first systematic characterization'过强，应限定为'for NER'或'structured entity extraction'。R1交叉完全同意。共识: scope down overclaim。\"\n    action_items:\n      - round: 26\n        action: \"Abstract/Intro中'first systematic characterization'限定为'for NER'。移除对structured prediction的泛化暗示。\"\n        assigned_to: research_director\n        status: open\n\n  - id: \"R25-W1\"\n    summary: \"SciERC entity construction +1.02pp 未过 Holm-Bonferroni (p_adj=0.20)；4 个数据集仅 1 个显著\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 25\n    last_seen_round: 26\n    mentions:\n      - round: 25\n        reviewers: [1, 2]\n        note: \"CoNLL 增益为负 (−0.29pp)，4 数据集中仅 Few-NERD 显著。\"\n      - round: 26\n        reviewers: [1, 2]\n        note: \"R26-R1-N2: p_adj在§1(0.20)和Table 13(0.038)之间矛盾。R2交叉AGREE。另外CoNLL -0.39pp负面结果。construction作为contribution仅1/3-4数据集显著。共识: 需澄清p_adj矛盾，正文更醒目标注不显著结果。\"\n    action_items:\n      - round: 26\n        action: \"澄清SciERC construction p_adj数值矛盾(0.20 vs 0.038)。正文醒目标注SciERC p_adj=0.20不显著。讨论仅1/4数据集显著的适用范围。\"\n        assigned_to: research_director\n        status: open\n\n  - id: \"R25-W2\"\n    summary: \"Holm-Bonferroni k=57 的 family 定义不透明\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 25\n    last_seen_round: 26\n    mentions:\n      - round: 25\n        reviewers: [1, 2]\n        note: \"57 个检验的具体构成从未说明。\"\n      - round: 26\n        reviewers: [1]\n        note: \"R26-R1-M3: 脚注9报告k=38(19+10+9)但Table 13列出k=57，差异的k=19来源不明。\"\n\n  - id: \"R25-W3\"\n    summary: \"72B zero-shot vs 8B fine-tuned 三因素混淆\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 25\n    last_seen_round: 26\n    mentions:\n      - round: 26\n        reviewers: [1, 2]\n        note: \"R26-R1-W2 + R2-W1: fine-tuning/scale/architecture混淆。共识: 需在正文hedge结论。\"\n\n  - id: \"R25-W4\"\n    summary: \"关键实验 seed 数量偏少\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 25\n    last_seen_round: 26\n    mentions:\n      - round: 26\n        reviewers: [1, 2]\n        note: \"R26-R1-W4: SciERC single-seed用于detailed diagnostic。R2交叉AGREE。bootstrap CI有缓解但不够。\"\n\n  - id: \"R25-W5\"\n    summary: \"Proposition 1 entity-wise independence 假设未经验验证\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 25\n    last_seen_round: 26\n    mentions:\n      - round: 26\n        reviewers: [1]\n        note: \"R26-R1-M2: Proposition 1的entity-wise independence假设何时violated（嵌套NER）未讨论。\"\n\n  - id: \"R25-W6\"\n    summary: \"Degeneracy bound E[ΔF₁] ≤ (1−D)·G_nd 极度松弛\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 25\n    last_seen_round: 26\n    mentions:\n      - round: 26\n        reviewers: [1, 2]\n        note: \"R26-R2-N2: bound仅解释3-12%的gap。R1交叉REBUT: 论文给的是equality非bound。R2在回应中维持批评(3-12%)。分歧点: R1认为decomposition有diagnostic价值(快速判断SC可行性)，R2认为实用性存疑。共识: 可降级为analysis tool。\"\n\n  - id: \"R25-W7\"\n    summary: \"Yao et al. (2026) 差异化不足\"\n    category: writing\n    severity: warning\n    status: in_progress\n    first_raised_round: 25\n    last_seen_round: 25\n    mentions:\n      - round: 26\n        reviewers: []\n        note: \"本轮未直接提及Yao et al.差异化问题。\"\n\n  - id: \"R25-W8\"\n    summary: \"引用质量: 未找到/元数据不匹配/orphan bib\"\n    category: format\n    severity: warning\n    status: in_progress\n    first_raised_round: 25\n    last_seen_round: 26\n    mentions:\n      - round: 26\n        reviewers: [1, 2]\n        note: \"R26-R2-N4: chen2025twofailures年份错(实际2023), feng2025optimal/park2024grammar作者错, hobelsberger2025systematic疑似虚构(similarity=0.236), 17 orphan bib entries。R1交叉AGREE并独立验证确认。共识: hobelsberger2025systematic需立即核实，若虚构是严重学术诚信问题。\"\n    action_items:\n      - round: 26\n        action: \"立即核实hobelsberger2025systematic真实性。修正chen2025twofailures年份。核实feng2025optimal和park2024grammar作者。清理17条orphan bib entries。\"\n        assigned_to: research_director\n        status: open\n\n  - id: \"R25-W9\"\n    summary: \"LP compression 缺与 LLM 校准文献的机制性对接\"\n    category: writing\n    severity: warning\n    status: in_progress\n    first_raised_round: 25\n    last_seen_round: 26\n    mentions:\n      - round: 26\n        reviewers: []\n        note: \"论文§8已有LP compression段落讨论calibration challenges和Yun et al. 2025 diversity collapse。本轮未直接再提。\"\n\n  - id: \"R25-W10\"\n    summary: \"三种故障模式呈 cascade 而非正交关系\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 25\n    last_seen_round: 26\n    mentions:\n      - round: 26\n        reviewers: [1, 2]\n        note: \"R26-R2-W2: diagnostic cascade是描述性分析而非因果链。R1交叉AGREE with nuance: entity construction实验部分建立因果性，epoch confound分析间接支持。共识: 标注为descriptive diagnostic而非causal chain更准确。\"\n\n  - id: \"R25-MR1\"\n    summary: \"缺失引用: EL4NER, Self-Certainty BoN 等\"\n    category: format\n    severity: warning\n    status: in_progress\n    first_raised_round: 25\n    last_seen_round: 26\n    mentions:\n      - round: 26\n        reviewers: [1, 2]\n        note: \"R26-R2-N1: EL4NER (arXiv:2505.23038)必须引用。R2-W4: Beyond Majority Voting, Scalable BoN via Self-Certainty, Optimal Aggregation。R1交叉conditionally AGREE。\"\n    action_items:\n      - round: 26\n        action: \"补引EL4NER (arXiv:2505.23038)并做head-to-head区分。核实并酌情补充R2-W4列出的3篇aggregation工作。\"\n        assigned_to: research_director\n        status: open\n\n  - id: \"R25-VIS1\"\n    summary: \"Appendix Figure 10 (p31) 是文字占位符\"\n    category: format\n    severity: critical\n    status: in_progress\n    first_raised_round: 25\n    last_seen_round: 26\n    mentions:\n      - round: 26\n        reviewers: []\n        note: \"本轮视觉审查未提及此问题（可能已修复——视觉审查发现的是p7密度问题而非占位符）。待Research Director确认。\"\n\n  # ===== Round 26 新发现 =====\n\n  - id: \"R26-N1\"\n    summary: \"N=8/16对test-time compute scaling研究范围过窄\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 26\n    last_seen_round: 26\n    mentions:\n      - round: 26\n        reviewers: [1, 2]\n        note: \"R1-W1 + R2交叉AGREE。相关文献测试到N=64+。Few-NERD N=16 LP仍有+0.30pp gain，存在继续scaling空间。R2补充NER per-sample cost高于reasoning是缓解因素。建议至少补N=32或在Discussion论证N=8的cost-efficiency。\"\n    action_items:\n      - round: 26\n        action: \"补充N=32实验（至少1-2数据集），或在Discussion以cost-efficiency角度论证N=8的合理性。\"\n        assigned_to: research_director\n        status: open\n\n  - id: \"R26-N2\"\n    summary: \"Trained verifier (LightGBM AUC=0.923) 负面结果scope有限\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 26\n    last_seen_round: 26\n    mentions:\n      - round: 26\n        reviewers: [1, 2]\n        note: \"R1-W5: 仅SciERC测试，特征集有限(5个)，cross-dataset负面可能是domain shift。R2交叉部分REBUT: AUC=0.923说明特征够，问题是discrimination→selection转化不了(又一个gap实例)。但R2同意应从'cannot close'改为'do not close in our setting'。共识: soften结论。\"\n    action_items:\n      - round: 26\n        action: \"§5.2结论从'cannot close the gap'改为'do not close the gap in our setting'。讨论feature engineering局限性。\"\n        assigned_to: research_director\n        status: open\n\n  - id: \"R26-W1\"\n    summary: \"论文同时做4件事，每项深度不够\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 26\n    last_seen_round: 26\n    mentions:\n      - round: 26\n        reviewers: [1, 2]\n        note: \"R2-W3: QE benchmark + selection failure + construction + theory，每项0.5-1页。R1交叉REBUT: 四部分构成完整故事，拆分丢失叙事。但R1同意可重新分层为2 core(QE diagnostic + failure mode) + 2 supporting(construction ablation + decomposition tool)。\"\n    action_items:\n      - round: 26\n        action: \"考虑将4 contributions重新组织为2 core + 2 supporting，聚焦深度到QE diagnostic和LP failure mode analysis。\"\n        assigned_to: research_director\n        status: open\n\n  - id: \"R26-VIS1\"\n    summary: \"Page 7 display items严重过密（4表+1图）\"\n    category: format\n    severity: warning\n    status: open\n    first_raised_round: 26\n    last_seen_round: 26\n    mentions:\n      - round: 26\n        reviewers: []\n        note: \"视觉审查发现。Table 2/3/4/5 + Figure 3挤在同一页。相邻p6/p8纯文本。建议移动部分items以平衡视觉节奏。\"\n\n  - id: \"R26-VIS2\"\n    summary: \"Figure 6 heatmap红绿色阶对色盲不友好\"\n    category: format\n    severity: info\n    status: open\n    first_raised_round: 26\n    last_seen_round: 26\n    mentions:\n      - round: 26\n        reviewers: []\n        note: \"视觉审查发现（p18）。建议改用viridis或blue-orange色阶。\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "struct_self_consist_ie",
    "issues_yaml": "issues:\n  # ===== 历史 resolved issues (保留，省略细节) =====\n  - id: \"R1-W1\"\n    summary: \"Few-NERD 3-epoch vs SciERC 5-epoch 训练时长混淆效应\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Reviewer PASS: 脚注+§4.1+appendix epoch data 一致。tab:epoch_confound caption 已注明 5K subsample。\"\n    resolution_round: 19\n\n  - id: \"R1-W2\"\n    summary: \"\\\"Two jointly necessary conditions\\\" 因果性表述过强\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 21\n    resolution: \"全文降级为 empirical pattern/factors。Reviewer 确认正文+appendix 15处+4处残留全部修复，0 因果语言残留。\"\n    resolution_round: 21\n\n  - id: \"R2-N1-old\"\n    summary: \"Contribution 1 'methodological premise' 是定义推论\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Reviewer PASS: 标题改为 'Quality estimation framework'; Abstract 干净。\"\n    resolution_round: 19\n\n  - id: \"R2-N2-old\"\n    summary: \"与 MBR 文献差异化定位不够锐利\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Reviewer PASS: Introduction 区分清晰，ρ=0.52 数据一致。\"\n    resolution_round: 19\n\n  - id: \"R2-N4-old\"\n    summary: \"模型规模 3B-8B，70B+ 未知\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Round 20 检查 PASS: limitations.tex '4B-8B scale; 70B+ untested'。\"\n    resolution_round: 19\n\n  - id: \"R1-W3-old\"\n    summary: \"2-seed 统计效力不足\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Reviewer PASS: tab:fewnerd 脚注 '3-seed mean: +0.04±0.48pp'。\"\n    resolution_round: 19\n\n  - id: \"R1-W4-old\"\n    summary: \"Per-entity-type non-independence\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Reviewer PASS: appendix ICC=-0.004 written。\"\n    resolution_round: 19\n\n  - id: \"R1-W5-old\"\n    summary: \"\\\"Supervised verifier\\\" framing 误导\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Reviewer PASS: 'supervised verifier' 0 matches。\"\n    resolution_round: 19\n\n  - id: \"R1-W6\"\n    summary: \"Degeneracy 定义需区分\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Round 20 检查 PASS: introduction.tex 有完整定义。\"\n    resolution_round: 19\n\n  - id: \"R1-W7\"\n    summary: \"SciERC greedy F1 不一致\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Round 20 检查 PASS: 脚注解释了 3-seed mean 和 epoch 差异。\"\n    resolution_round: 19\n\n  - id: \"R2-W1-old\"\n    summary: \"Abstract 数字过载\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Reviewer PASS: Abstract 含 3 个数字 (≤3)。\"\n    resolution_round: 19\n\n  - id: \"R2-W2-old\"\n    summary: \"Actionable contribution 偏薄\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 21\n    resolution: \"Conclusion 新增 practitioner guidance。\"\n    resolution_round: 21\n\n  - id: \"R2-W3-old\"\n    summary: \"Discussion 过于碎片化\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"5 段合并完成。\"\n    resolution_round: 19\n\n  - id: \"R2-W5-old\"\n    summary: \"核心数字跨 section 重复\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"属正常范围。\"\n    resolution_round: 19\n\n  - id: \"R2-W4-baseline\"\n    summary: \"缺少 baseline signals\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Round 20 检查 PASS。\"\n    resolution_round: 19\n\n  - id: \"R2-W4-re\"\n    summary: \"RE extension preliminary 但引用频繁\"\n    category: framing\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 19\n    resolution: \"Round 20 检查 PASS。\"\n    resolution_round: 19\n\n  - id: \"R1-MR1\"\n    summary: \"缺失引用: Geifman & El-Yaniv 2017, XGrammar 等\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 20\n    resolution: \"Paper Agent 补全 4 篇。\"\n    resolution_round: 20\n\n  - id: \"R19-I8\"\n    summary: \"Table 3 EM/VC 缺 p-values\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    resolution: \"Reviewer PASS。\"\n    resolution_round: 19\n\n  - id: \"R19-I9\"\n    summary: \"Per-type LP selection 异质性\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    resolution: \"Reviewer PASS。\"\n    resolution_round: 19\n\n  - id: \"R19-DATA1\"\n    summary: \"LLaMA CoNLL degeneracy 86.4% vs 89.2%\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    resolution: \"根因修复完成。\"\n    resolution_round: 19\n\n  - id: \"R2-N3-old\"\n    summary: \"Title scope: 'Structured IE' 过宽\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 21\n    resolution: \"Title 已为 NER-specific。Reviewer 确认无需修改。\"\n    resolution_round: 21\n\n  - id: \"R21-C1\"\n    summary: \"正文页数超限 (~9.5 页 vs ACL 8 页限制)\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"Discussion 3段压缩 + Conclusion 压缩。Reviewer PASS: Sections 1-9 + Limitations 在 page 8 结束。\"\n    resolution_round: 21\n\n  - id: \"R21-C2\"\n    summary: \"'两个条件'框架跨数据集经验基础不足（仅 3 数据点）\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"全文 15 处降级 + appendix 4 处残留修复。Reviewer 确认 0 因果语言残留。\"\n    resolution_round: 21\n\n  - id: \"R21-W1\"\n    summary: \"Epoch confound 对 headline result 的影响正文处理不充分\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"experiments.tex 新增 epoch-controlled comparison。\"\n    resolution_round: 21\n\n  - id: \"R21-W2\"\n    summary: \"SciERC 作为 primary test bed 系统性 underpowered\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"Few-NERD 定位为 'definitive test'。\"\n    resolution_round: 21\n\n  - id: \"R21-W3\"\n    summary: \"DALS 定位与诊断性论文冲突 + ε data-snooping\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"DALS 已移入 appendix。\"\n    resolution_round: 21\n\n  - id: \"R21-W4\"\n    summary: \"新颖性增量需更精确定位\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"Intro L8 强化。\"\n    resolution_round: 21\n\n  - id: \"R21-W5\"\n    summary: \"LP ρ 跨表不一致 (0.205 vs 0.215)\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"审计确认论文全文统一使用 0.205。\"\n    resolution_round: 21\n\n  - id: \"R21-W6\"\n    summary: \"Table 3 的 7 个连续脚注\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"7→2 脚注。\"\n    resolution_round: 21\n\n  - id: \"R21-W7\"\n    summary: \"Greedy F1 多表数值不一致 (4 values)\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"Method §3.3 列出 4 值 + 3 类 protocol variants。\"\n    resolution_round: 21\n\n  - id: \"R21-I1\"\n    summary: \"Appendix 残留实验标识\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"全文搜索确认无残留。\"\n    resolution_round: 21\n\n  - id: \"R21-I2\"\n    summary: \"'Capability trap' 措辞过强\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"统一使用 'capability-diversity tension'。\"\n    resolution_round: 21\n\n  - id: \"R21-I3\"\n    summary: \"3 处 -ing 短语残留\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"3 处改写完成。\"\n    resolution_round: 21\n\n  - id: \"R21-MR1\"\n    summary: \"缺失引用: Farquhar et al., Chen et al. pass@k\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"已补入 Related Work。\"\n    resolution_round: 21\n\n  - id: \"R21-Q3\"\n    summary: \"Per-entity-type ρ=-0.881 effective df 问题\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 21\n    resolution: \"Appendix 已有 df=4 adjustment。\"\n    resolution_round: 21\n\n  - id: \"R22-N1\"\n    summary: \"正文再次超页约 2 页\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 23\n    resolution: \"Multiple compression rounds completed. ≤8 pages confirmed.\"\n    resolution_round: 23\n\n  - id: \"R22-N2\"\n    summary: \"标题暗示纯 negative result\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 23\n    resolution: \"Title updated to cover both diagnostic and resolving contributions.\"\n    resolution_round: 23\n\n  - id: \"R22-W1\"\n    summary: \"correlation-selection gap 概念缺乏理论深度\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 24\n    resolution: \"D162: 23-config 回归 R²=-8.53，公式彻底失败。删除公式，改为定性叙述三因素影响。Paper Agent 已执行。\"\n    resolution_round: 24\n\n  - id: \"R22-W2\"\n    summary: \"Abstract 中 LP 和 AUROC 缩写未展开\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 23\n    resolution: \"LP and AUROC expanded in Abstract.\"\n    resolution_round: 23\n\n  - id: \"R22-W3\"\n    summary: \"LP-alignment gating protocol 使用 test set 做 probe\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 23\n    resolution: \"Dev set gating implemented.\"\n    resolution_round: 23\n\n  - id: \"R22-W4\"\n    summary: \"SciERC seed sensitivity 高 (σ=0.48 pp)\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 23\n    resolution: \"Switched to multi-seed reporting throughout.\"\n    resolution_round: 23\n\n  - id: \"R22-W5\"\n    summary: \"Entity construction 阈值 θ 跨数据集不一致\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 24\n    resolution: \"Paper Agent R24 Patch: 正文 'tuning-free' → 'empirically robust default'; Table 5 caption → 'default heuristic'。\"\n    resolution_round: 24\n\n  - id: \"R22-W6\"\n    summary: \"'the correct self-consistency analogy' 措辞过于绝对\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 23\n    resolution: \"Changed to 'a more effective self-consistency analogy'.\"\n    resolution_round: 23\n\n  - id: \"R22-W7\"\n    summary: \"仅测试 LoRA 微调但 claim 范围不限定\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 22\n    last_seen_round: 26\n    mentions:\n      - round: 22\n        reviewers: [1, 2]\n        note: \"所有实验均为 LoRA fine-tuned models。\"\n      - round: 23\n        reviewers: [1, 2]\n        note: \"Introduction qualified with 'fine-tuned 4B-8B models'.\"\n      - round: 24\n        reviewers: [1, 2]\n        note: \"R24：scope 声明在 Introduction 和 Limitations 中已存在。72B zero-shot 实验将直接回应此问题。\"\n      - round: 25\n        reviewers: [1, 2]\n        note: \"72B zero-shot 已加入但 API 模型仍缺。\"\n      - round: 26\n        reviewers: [1, 2]\n        note: \"R26-R1-W2 + R2-W1: 仅2个~8B fine-tuned + 1个72B zero-shot。缺closed-source模型。72B结果仅在Appendix。scale/regime/architecture三因素混淆。\"\n\n  - id: \"R22-I1\"\n    summary: \"实体匹配标准分散在 §3.2 各段落中\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 22\n    last_seen_round: 25\n    mentions:\n      - round: 26\n        reviewers: []\n        note: \"本轮未提及，可能已修复，待 Research Director 确认\"\n\n  - id: \"R22-I2\"\n    summary: \"冠词错误 + 引用格式不一致\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 23\n    resolution: \"Fixed.\"\n    resolution_round: 23\n\n  - id: \"R22-I3\"\n    summary: \"Figure 3 scatter plot 标签在打印尺寸下可能难辨\"\n    category: format\n    severity: info\n    status: open\n    first_raised_round: 22\n    last_seen_round: 26\n    mentions:\n      - round: 25\n        reviewers: [1, 2]\n        note: \"视觉审查确认 Figure 3 过小（p7），R1 提到 Figure 1 面板注释 6-7pt。\"\n      - round: 26\n        reviewers: [1]\n        note: \"R26视觉审查再次确认p7 display items过密，Figure 3可读性差。\"\n\n  - id: \"R22-MR1\"\n    summary: \"缺失引用: ensemble-based IE, Xie et al. 2023\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 24\n    resolution: \"Paper Agent R24 Patch: LLM-Blender + CISC/Self-Certainty 技术差异 + orphan bib 清理。xie2023zeroshot 恢复引用。\"\n    resolution_round: 24\n\n  - id: \"R22-FIG1\"\n    summary: \"fig_overview 缺少 Construction 贡献 + 残留 RE 文字\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 23\n    resolution: \"fig_overview regenerated as three-column layout.\"\n    resolution_round: 23\n\n  - id: \"R22-FIG2\"\n    summary: \"fig_selection_gap caption 仍引用旧双面板格式\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 23\n    resolution: \"Regenerated as single-panel NER-only.\"\n    resolution_round: 23\n\n  - id: \"R23-N1\"\n    summary: \"Entity-level construction 新颖性不足\"\n    category: framing\n    severity: critical\n    status: in_progress\n    first_raised_round: 23\n    last_seen_round: 26\n    mentions:\n      - round: 23\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 独立列为 critical。\"\n      - round: 24\n        reviewers: [1, 2]\n        note: \"降级为 diagnostic-motivated mitigation。R24 Patch 完成。\"\n      - round: 25\n        reviewers: [1, 2]\n        note: \"R2 再次列为 critical。R1 REBUT。Director 判断维持 resolved。\"\n      - round: 26\n        reviewers: [1, 2]\n        note: \"R26再次独立提出。R2-N1: 缺引EL4NER (arXiv:2505.23038)，+1.40pp改进有限，本质是已有entity voting的MBR包装。R1交叉AGREE降级为ablation。共识: construction不应作为standalone contribution。另需补引EL4NER。\"\n    action_items:\n      - round: 26\n        action: \"补引EL4NER并区分(单模型SC vs 多模型ensemble)。确认construction在正文中已降级为diagnostic-motivated ablation而非contribution。\"\n        assigned_to: research_director\n        status: open\n\n  - id: \"R23-N2\"\n    summary: \"Correlation-selection gap 部分 by construction（framing tautology）\"\n    category: framing\n    severity: critical\n    status: in_progress\n    first_raised_round: 23\n    last_seen_round: 26\n    mentions:\n      - round: 23\n        reviewers: [1, 2]\n        note: \"R2 列为 critical，R1 部分同意。\"\n      - round: 24\n        reviewers: [1, 2]\n        note: \"R1 rebuttal 有效——MBR consensus-proximity 确实给不同 sample 赋不同分数。\"\n      - round: 25\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 再次独立提出。\"\n      - round: 26\n        reviewers: [1, 2]\n        note: \"R26两位Reviewer再次独立提出且交叉后完全共识。R1-N1: 4/5信号by construction无法做selection，论文§4自承'design property not empirical finding'，但Abstract/Intro未前置此区分。R2交叉AGREE并加强: 真正empirical surprise是LP compression（0.041 nats），被当前framing淹没。共识: 必须重构Abstract/Intro将structural/empirical二分法前置。\"\n    action_items:\n      - round: 26\n        action: \"重构Abstract和Introduction: (1) 前置4/5信号是instance-level的structural limitation; (2) 聚焦LP compression作为核心empirical finding; (3) 移除对instance-level信号selection failure的'surprising'/'diagnose'措辞。\"\n        assigned_to: research_director\n        status: open\n\n  - id: \"R23-N3\"\n    summary: \"Expected selection gain 'bound' 中 g(·) 未定义\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 23\n    last_seen_round: 23\n    resolution: \"Changed to 'approximately factored as'. Framed as heuristic.\"\n    resolution_round: 23\n\n  - id: \"R23-W1\"\n    summary: \"ε=0.05 non-tied subset 是 post-hoc 最优切点\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 23\n    last_seen_round: 23\n    resolution: \"标记为 exploratory。\"\n    resolution_round: 23\n\n  - id: \"R23-W2\"\n    summary: \"Complementarity claim 仅基于 2 informative data points\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 23\n    last_seen_round: 23\n    resolution: \"Softened scope.\"\n    resolution_round: 23\n\n  - id: \"R23-W3\"\n    summary: \"Abstract 信息密度过高\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 23\n    last_seen_round: 23\n    resolution: \"Reduced to 4 key numbers.\"\n    resolution_round: 23\n\n  - id: \"R23-W4\"\n    summary: \"Table 4 (entity construction) 缺少 multi-seed ±σ\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 23\n    last_seen_round: 23\n    resolution: \"Updated with multi-seed mean±σ.\"\n    resolution_round: 23\n\n  - id: \"R23-I1\"\n    summary: \"Figure 1 caption ρ scope 不一致\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 23\n    last_seen_round: 23\n    resolution: \"Caption updated.\"\n    resolution_round: 23\n\n  - id: \"R23-I2\"\n    summary: \"WNUT-17 正文分析不足\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 23\n    last_seen_round: 26\n    mentions:\n      - round: 26\n        reviewers: []\n        note: \"本轮未提及，可能已修复，待 Research Director 确认\"\n\n  - id: \"R23-MR1\"\n    summary: \"缺失引用: Florian 2003, Luo 2023, Wiher 2022\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 23\n    last_seen_round: 24\n    resolution: \"合并到 R22-MR1 统一处理完成。\"\n    resolution_round: 24\n\n  # ===== Round 24 issues =====\n\n  - id: \"R24-N1\"\n    summary: \"分解公式 E[ΔF1]≈(1-d)·Δ_oracle·g(ρ_within) 仅 3 macro-level data points 验证\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 24\n    last_seen_round: 24\n    resolution: \"D162: 23-config 回归 R²=-8.53，公式完全无预测力。删除公式，改为定性叙述三因素影响。\"\n    resolution_round: 24\n\n  - id: \"R24-N2\"\n    summary: \"Gating protocol 循环性 + 验证不足\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 24\n    last_seen_round: 24\n    resolution: \"Bootstrap CI 完成：τ=0.3 位于稳定区间中心。Paper Agent 已实现三路路由。\"\n    resolution_round: 24\n\n  - id: \"R24-W1\"\n    summary: \"'Resolving' framing 过强：entity construction 仅恢复 8-11% oracle headroom\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 24\n    last_seen_round: 24\n    resolution: \"Paper Agent R24 Patch: Title 'Resolving' → 'Addressing', Contribution 3 降级。\"\n    resolution_round: 24\n\n  - id: \"R24-W2\"\n    summary: \"SciERC selection 结果 underpowered (n=529, MDE≈1.5pp)\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 24\n    last_seen_round: 24\n    resolution: \"Paper Agent R24 Patch: SciERC selection 结果处加 detection threshold caveat。\"\n    resolution_round: 24\n\n  - id: \"R24-W3\"\n    summary: \"Related Work 缺少与 CISC/Self-Certainty 技术差异对比\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 24\n    last_seen_round: 24\n    resolution: \"Paper Agent R24 Patch: RW 增加 2 句技术差异。\"\n    resolution_round: 24\n\n  - id: \"R24-W4\"\n    summary: \"English-only + NER-heavy 泛化局限未在 Limitations 讨论\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 24\n    last_seen_round: 24\n    resolution: \"Paper Agent R24 Patch: Limitations 增加 1 句。\"\n    resolution_round: 24\n\n  - id: \"R24-W5\"\n    summary: \"Self-Certainty (Kang 2025) 和 P(True) (Kadavath 2022) 未测试\"\n    category: experiment\n    severity: warning\n    status: wont_fix\n    first_raised_round: 24\n    last_seen_round: 26\n    resolution: \"DDL 前无法新增 signal 实验。已在 Limitations 列出。\"\n    mentions:\n      - round: 26\n        reviewers: [1, 2]\n        note: \"R26未直接再提，但R2-W3指出缺少PTrue/Self-Certainty等近期信号。论文在Discussion §8已提及作为future direction。\"\n\n  - id: \"R24-W6\"\n    summary: \"Appendix D 'as a reviewer correctly noted' 暗示审稿历史\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 24\n    last_seen_round: 24\n    resolution: \"Paper Agent R24 Patch: 删除，改为直接陈述。\"\n    resolution_round: 24\n\n  - id: \"R24-I1\"\n    summary: \"Table 2 中 EM/VC 的 p 值标 '---'\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 24\n    last_seen_round: 24\n    resolution: \"'---' → 'n/a†' + caption footnote。\"\n    resolution_round: 24\n\n  - id: \"R24-I2\"\n    summary: \"F1 metric 术语不统一\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 24\n    last_seen_round: 24\n    resolution: \"Paper Agent R24 Patch: method.tex 加定义。\"\n    resolution_round: 24\n\n  - id: \"R24-I3\"\n    summary: \"orphan bib entries 待清理\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 24\n    last_seen_round: 24\n    resolution: \"Paper Agent R24 Patch: 删除 8 条 + xie2023zeroshot 恢复。\"\n    resolution_round: 24\n\n  - id: \"R24-I4\"\n    summary: \"SJ 分母边界情况未讨论\"\n    category: method\n    severity: info\n    status: resolved\n    first_raised_round: 24\n    last_seen_round: 24\n    resolution: \"Paper Agent R24 Patch: footnote 补充。\"\n    resolution_round: 24\n\n  - id: \"R24-I5\"\n    summary: \"Abstract ρ up to 0.45 取自 CoNLL EM（最易数据集）\"\n    category: writing\n    severity: info\n    status: in_progress\n    first_raised_round: 24\n    last_seen_round: 26\n    mentions:\n      - round: 26\n        reviewers: []\n        note: \"本轮未直接提及。\"\n\n  # ===== Round 25 issues (更新状态) =====\n\n  - id: \"R25-N1\"\n    summary: \"Cross-dataset 分析（n=23, ρ=0.052, p=0.81）严重 underpowered，不能支持 null 结论\"\n    category: experiment\n    severity: critical\n    status: in_progress\n    first_raised_round: 25\n    last_seen_round: 25\n    mentions:\n      - round: 25\n        reviewers: [1, 2]\n        note: \"n=23 power 仅约 50% for ρ=0.4。结论过强。\"\n      - round: 26\n        reviewers: []\n        note: \"R26未直接提及此specific null finding。论文§7.3现报告post-hoc power analysis (80% power requires n≈85 for ρ=0.3)。\"\n\n  - id: \"R25-N2\"\n    summary: \"§5.1 Cross-Model SC ('preliminary') 和 §5.3 SCD ('ongoing') 包含未完成工作\"\n    category: framing\n    severity: critical\n    status: in_progress\n    first_raised_round: 25\n    last_seen_round: 26\n    mentions:\n      - round: 25\n        reviewers: [1, 2]\n        note: \"§5.3 完全无实验结果。ARR 提交 incomplete work 会被 AC 视为 premature。\"\n      - round: 26\n        reviewers: [1, 2]\n        note: \"R26-R1-W3: cross-model仅1数据集1对模型，不足以支撑general claim。R2交叉REBUT: 论文标注为exploratory。但R2同意若保留需补实验或缩减为footnote。§5.3 SCD不再出现。\"\n    action_items:\n      - round: 26\n        action: \"§5.1 cross-model内容要么扩展到多数据集多模型，要么缩减为1-2句footnote/future work。确认§5.3已删除。\"\n        assigned_to: research_director\n        status: in_progress\n\n  - id: \"R25-N3\"\n    summary: \"NER-only 实验无法支撑 'structured prediction' framing\"\n    category: framing\n    severity: critical\n    status: in_progress\n    first_raised_round: 25\n    last_seen_round: 26\n    mentions:\n      - round: 25\n        reviewers: [2]\n        note: \"Abstract/Intro 叙事推广到 structured prediction，但仅有 NER 实验。\"\n      - round: 26\n        reviewers: [1, 2]\n        note: \"R26-R2-N3: 'first systematic characterization'过强，应限定为'for NER'或'structured entity extraction'。R1交叉完全同意。共识: scope down overclaim。\"\n    action_items:\n      - round: 26\n        action: \"Abstract/Intro中'first systematic characterization'限定为'for NER'。移除对structured prediction的泛化暗示。\"\n        assigned_to: research_director\n        status: open\n\n  - id: \"R25-W1\"\n    summary: \"SciERC entity construction +1.02pp 未过 Holm-Bonferroni (p_adj=0.20)；4 个数据集仅 1 个显著\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 25\n    last_seen_round: 26\n    mentions:\n      - round: 25\n        reviewers: [1, 2]\n        note: \"CoNLL 增益为负 (−0.29pp)，4 数据集中仅 Few-NERD 显著。\"\n      - round: 26\n        reviewers: [1, 2]\n        note: \"R26-R1-N2: p_adj在§1(0.20)和Table 13(0.038)之间矛盾。R2交叉AGREE。另外CoNLL -0.39pp负面结果。construction作为contribution仅1/3-4数据集显著。共识: 需澄清p_adj矛盾，正文更醒目标注不显著结果。\"\n    action_items:\n      - round: 26\n        action: \"澄清SciERC construction p_adj数值矛盾(0.20 vs 0.038)。正文醒目标注SciERC p_adj=0.20不显著。讨论仅1/4数据集显著的适用范围。\"\n        assigned_to: research_director\n        status: open\n\n  - id: \"R25-W2\"\n    summary: \"Holm-Bonferroni k=57 的 family 定义不透明\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 25\n    last_seen_round: 26\n    mentions:\n      - round: 25\n        reviewers: [1, 2]\n        note: \"57 个检验的具体构成从未说明。\"\n      - round: 26\n        reviewers: [1]\n        note: \"R26-R1-M3: 脚注9报告k=38(19+10+9)但Table 13列出k=57，差异的k=19来源不明。\"\n\n  - id: \"R25-W3\"\n    summary: \"72B zero-shot vs 8B fine-tuned 三因素混淆\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 25\n    last_seen_round: 26\n    mentions:\n      - round: 26\n        reviewers: [1, 2]\n        note: \"R26-R1-W2 + R2-W1: fine-tuning/scale/architecture混淆。共识: 需在正文hedge结论。\"\n\n  - id: \"R25-W4\"\n    summary: \"关键实验 seed 数量偏少\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 25\n    last_seen_round: 26\n    mentions:\n      - round: 26\n        reviewers: [1, 2]\n        note: \"R26-R1-W4: SciERC single-seed用于detailed diagnostic。R2交叉AGREE。bootstrap CI有缓解但不够。\"\n\n  - id: \"R25-W5\"\n    summary: \"Proposition 1 entity-wise independence 假设未经验验证\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 25\n    last_seen_round: 26\n    mentions:\n      - round: 26\n        reviewers: [1]\n        note: \"R26-R1-M2: Proposition 1的entity-wise independence假设何时violated（嵌套NER）未讨论。\"\n\n  - id: \"R25-W6\"\n    summary: \"Degeneracy bound E[ΔF₁] ≤ (1−D)·G_nd 极度松弛\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 25\n    last_seen_round: 26\n    mentions:\n      - round: 26\n        reviewers: [1, 2]\n        note: \"R26-R2-N2: bound仅解释3-12%的gap。R1交叉REBUT: 论文给的是equality非bound。R2在回应中维持批评(3-12%)。分歧点: R1认为decomposition有diagnostic价值(快速判断SC可行性)，R2认为实用性存疑。共识: 可降级为analysis tool。\"\n\n  - id: \"R25-W7\"\n    summary: \"Yao et al. (2026) 差异化不足\"\n    category: writing\n    severity: warning\n    status: in_progress\n    first_raised_round: 25\n    last_seen_round: 25\n    mentions:\n      - round: 26\n        reviewers: []\n        note: \"本轮未直接提及Yao et al.差异化问题。\"\n\n  - id: \"R25-W8\"\n    summary: \"引用质量: 未找到/元数据不匹配/orphan bib\"\n    category: format\n    severity: warning\n    status: in_progress\n    first_raised_round: 25\n    last_seen_round: 26\n    mentions:\n      - round: 26\n        reviewers: [1, 2]\n        note: \"R26-R2-N4: chen2025twofailures年份错(实际2023), feng2025optimal/park2024grammar作者错, hobelsberger2025systematic疑似虚构(similarity=0.236), 17 orphan bib entries。R1交叉AGREE并独立验证确认。共识: hobelsberger2025systematic需立即核实，若虚构是严重学术诚信问题。\"\n    action_items:\n      - round: 26\n        action: \"立即核实hobelsberger2025systematic真实性。修正chen2025twofailures年份。核实feng2025optimal和park2024grammar作者。清理17条orphan bib entries。\"\n        assigned_to: research_director\n        status: open\n\n  - id: \"R25-W9\"\n    summary: \"LP compression 缺与 LLM 校准文献的机制性对接\"\n    category: writing\n    severity: warning\n    status: in_progress\n    first_raised_round: 25\n    last_seen_round: 26\n    mentions:\n      - round: 26\n        reviewers: []\n        note: \"论文§8已有LP compression段落讨论calibration challenges和Yun et al. 2025 diversity collapse。本轮未直接再提。\"\n\n  - id: \"R25-W10\"\n    summary: \"三种故障模式呈 cascade 而非正交关系\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 25\n    last_seen_round: 26\n    mentions:\n      - round: 26\n        reviewers: [1, 2]\n        note: \"R26-R2-W2: diagnostic cascade是描述性分析而非因果链。R1交叉AGREE with nuance: entity construction实验部分建立因果性，epoch confound分析间接支持。共识: 标注为descriptive diagnostic而非causal chain更准确。\"\n\n  - id: \"R25-MR1\"\n    summary: \"缺失引用: EL4NER, Self-Certainty BoN 等\"\n    category: format\n    severity: warning\n    status: in_progress\n    first_raised_round: 25\n    last_seen_round: 26\n    mentions:\n      - round: 26\n        reviewers: [1, 2]\n        note: \"R26-R2-N1: EL4NER (arXiv:2505.23038)必须引用。R2-W4: Beyond Majority Voting, Scalable BoN via Self-Certainty, Optimal Aggregation。R1交叉conditionally AGREE。\"\n    action_items:\n      - round: 26\n        action: \"补引EL4NER (arXiv:2505.23038)并做head-to-head区分。核实并酌情补充R2-W4列出的3篇aggregation工作。\"\n        assigned_to: research_director\n        status: open\n\n  - id: \"R25-VIS1\"\n    summary: \"Appendix Figure 10 (p31) 是文字占位符\"\n    category: format\n    severity: critical\n    status: in_progress\n    first_raised_round: 25\n    last_seen_round: 26\n    mentions:\n      - round: 26\n        reviewers: []\n        note: \"本轮视觉审查未提及此问题（可能已修复——视觉审查发现的是p7密度问题而非占位符）。待Research Director确认。\"\n\n  # ===== Round 26 新发现 =====\n\n  - id: \"R26-N1\"\n    summary: \"N=8/16对test-time compute scaling研究范围过窄\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 26\n    last_seen_round: 26\n    mentions:\n      - round: 26\n        reviewers: [1, 2]\n        note: \"R1-W1 + R2交叉AGREE。相关文献测试到N=64+。Few-NERD N=16 LP仍有+0.30pp gain，存在继续scaling空间。R2补充NER per-sample cost高于reasoning是缓解因素。建议至少补N=32或在Discussion论证N=8的cost-efficiency。\"\n    action_items:\n      - round: 26\n        action: \"补充N=32实验（至少1-2数据集），或在Discussion以cost-efficiency角度论证N=8的合理性。\"\n        assigned_to: research_director\n        status: open\n\n  - id: \"R26-N2\"\n    summary: \"Trained verifier (LightGBM AUC=0.923) 负面结果scope有限\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 26\n    last_seen_round: 26\n    mentions:\n      - round: 26\n        reviewers: [1, 2]\n        note: \"R1-W5: 仅SciERC测试，特征集有限(5个)，cross-dataset负面可能是domain shift。R2交叉部分REBUT: AUC=0.923说明特征够，问题是discrimination→selection转化不了(又一个gap实例)。但R2同意应从'cannot close'改为'do not close in our setting'。共识: soften结论。\"\n    action_items:\n      - round: 26\n        action: \"§5.2结论从'cannot close the gap'改为'do not close the gap in our setting'。讨论feature engineering局限性。\"\n        assigned_to: research_director\n        status: open\n\n  - id: \"R26-W1\"\n    summary: \"论文同时做4件事，每项深度不够\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 26\n    last_seen_round: 26\n    mentions:\n      - round: 26\n        reviewers: [1, 2]\n        note: \"R2-W3: QE benchmark + selection failure + construction + theory，每项0.5-1页。R1交叉REBUT: 四部分构成完整故事，拆分丢失叙事。但R1同意可重新分层为2 core(QE diagnostic + failure mode) + 2 supporting(construction ablation + decomposition tool)。\"\n    action_items:\n      - round: 26\n        action: \"考虑将4 contributions重新组织为2 core + 2 supporting，聚焦深度到QE diagnostic和LP failure mode analysis。\"\n        assigned_to: research_director\n        status: open\n\n  - id: \"R26-VIS1\"\n    summary: \"Page 7 display items严重过密（4表+1图）\"\n    category: format\n    severity: warning\n    status: open\n    first_raised_round: 26\n    last_seen_round: 26\n    mentions:\n      - round: 26\n        reviewers: []\n        note: \"视觉审查发现。Table 2/3/4/5 + Figure 3挤在同一页。相邻p6/p8纯文本。建议移动部分items以平衡视觉节奏。\"\n\n  - id: \"R26-VIS2\"\n    summary: \"Figure 6 heatmap红绿色阶对色盲不友好\"\n    category: format\n    severity: info\n    status: open\n    first_raised_round: 26\n    last_seen_round: 26\n    mentions:\n      - round: 26\n        reviewers: []\n        note: \"视觉审查发现（p18）。建议改用viridis或blue-orange色阶。\""
  }
}
```

</details>

---


### Tool result

_source line 2766 · 2026-05-20T14:40:21.667099+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml\", \"bytes\": 31557}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 164
}
```

</details>

---


### Tool call

_source line 2767 · 2026-05-20T14:42:45.973223+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "struct_self_consist_ie",
  "report": "# 审稿报告 — Round 26 (Fresh Review)\n\n**论文**: \"Strong Predictors, Weak Selectors: The Correlation-Selection Gap in Self-Consistency for Named Entity Recognition\"\n**Venue**: EMNLP 2026 Main Conference (via ARR May 2026)\n**Deadline**: 2026-05-25\n**审稿模式**: Fresh（重新审稿，无上轮记忆）\n**Reviewer 编排**: 2 人（R1: 方法严谨性+实验有效性; R2: 新颖性+完整性+写作质量）\n**轮次**: Round 1 独立审稿 → 交叉分享 → 收敛（1 轮即收敛）\n\n---\n\n## Summary\n\n论文研究 test-time compute scaling (self-consistency) 应用于 NER 的效果，评估 5 种 confidence signals（Soft Jaccard, voting confidence, Fleiss' κ, exact match, log-probability）在 4 个 NER benchmark 上的 quality estimation (QE) 和 sample selection 表现。核心发现：所有信号能做可靠的 QE（ρ up to 0.45, AUROC up to 0.82），但无法可靠地选出最优 sample——作者称之为\"correlation-selection gap\"。论文提出 entity-level construction（实体级聚合）作为缓解方案，在 Few-NERD 上获得 +1.40pp（Holm p_adj=0.006），并给出 degeneracy decomposition 的理论分析。\n\n---\n\n## Strengths\n\n1. **统计方法论远超 NLP 社区平均水平** [R1, R2 共识]：Holm-Bonferroni 多重比较校正（family k=10/19/57）、bootstrap CI (B=10,000)、MDE/power analysis、TOST equivalence testing、permutation tests。这种严谨性在 NER/IE 论文中极为罕见，具有示范价值。\n\n2. **Correlation-selection gap 概念清晰、有实际价值** [R1, R2 共识]：核心观察——信号能估质量但选不出最优 sample——对 NER practitioners 直接有用，改变了 test-time scaling 的使用策略。\n\n3. **实验设计系统全面** [R2]：5 signals × 4 datasets × 2 models × 4B-8B fine-tuned + 72B zero-shot，覆盖难度梯度（WNUT-17 ~42% → CoNLL >90% F1）。\n\n4. **Diagnostic cascade 有洞察力** [R1, R2]：degeneracy → headroom → LP compression 的层级分析为理解\"为什么信号选不出最优\"提供了直觉和可复用的诊断协议（Appendix ab）。\n\n5. **极其详尽的附录** [R1, R2 共识]：30+ 页、55 个表格，涵盖 temperature/LoRA rank/free-form decoding ablation、calibration、hidden state probes、per-entity-type 分析。\n\n6. **负面结果的诚实报告** [R1]：trained verifier 失败（§5.2）、cross-model 仅 preliminary（§5.1）、construction 在 CoNLL 无效（§7.5）。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**[W-Critical-1] \"Correlation-selection gap\" 对 4/5 信号是 structural tautology，framing 过度渲染 novelty** [R1-N1 + R2 交叉 AGREE，共识]\n\n论文评估的 5 个信号中，4 个（SJ, VC, FK, EM）是 instance-level aggregates——对同一 instance 的所有 N 个 candidates 赋予相同分数。它们根据定义无法做 within-instance ranking。论文自己在 §4 (p.4) 承认：\"selection failure is a design property, not an empirical finding\"。但 Abstract 和 Introduction 的 framing 没有前置这个关键区分，读者会以为 5 个信号都是 selection 的候选者，产生虚假 surprise。\n\n真正的 empirical 贡献——LP（唯一 per-sample 信号）因 compression 失败（within-instance range ≈0.041 nats, 60% instances; §4, Figure 8）——在当前 framing 下被淹没。\n\n**修改要求**：重构 Abstract/Intro，将 structural（4/5 信号 by construction 不能 select）与 empirical（LP compression failure）明确区分并前置。\n\n**[W-Critical-2] Entity-level construction 新颖性不足，缺少关键引用** [R2-N1 + R1 交叉 AGREE，共识]\n\n- EL4NER (arXiv:2505.23038, May 2025) 已系统实现了基于多 LLM 的 entity-level span extraction + type voting pipeline，在 ICL 设置下取得 SOTA。**未被引用**。\n- Xie et al. (2023a) 已是 entity-level voting 的先驱，论文自己引用但未充分区分。\n- Entity-level construction 本质上是将已有的 entity voting 在 MBR 框架下重新包装（LP-weighted variant 仅额外 +0.30pp over uniform）。\n- +1.40pp (Few-NERD) 和 +1.02pp (SciERC, p_adj=0.20 不显著) 的改进有限。\n\n**修改要求**：补引 EL4NER 并区分（单模型 SC vs. 多模型 ensemble）。将 construction 定位为 diagnostic-motivated ablation 而非 standalone contribution。\n\n**[W-Critical-3] \"First systematic characterization\" overclaim** [R2-N3 + R1 交叉 AGREE，共识]\n\nAbstract 声称\"the first systematic characterization\"，但 Chen et al. (2023) 已研究 SC failure modes、Eikema et al. (2025) 已研究 structured MBR decoding 失效、Kang et al. (2025) 和 Taubenfeld et al. (2025) 已研究 confidence signals 与 SC。论文的\"first\"仅限于 NER + 这 5 个信号的组合。\n\n**修改要求**：限定 scope 为 \"for NER\" 或 \"in the context of structured entity extraction\"。\n\n**[W-Critical-4] 参考文献存在年份错误和疑似虚构引用** [R2-N4 + R1 交叉 AGREE，独立验证确认]\n\n| 问题 | 详情 |\n|------|------|\n| chen2025twofailures | bib 标注 2025，实际发表于 2023 (arXiv:2305.14279) |\n| feng2025optimal | bib 首作 \"Feng\"，API 返回 \"Austin\"——需核实 |\n| park2024grammar | bib 首作 \"Park\"，API 返回 \"Berg-Kirkpatrick\"——可能张冠李戴 |\n| **hobelsberger2025systematic** | **Semantic Scholar/OpenAlex 均无法验证（similarity=0.236），疑似虚构引用** |\n| 17 orphan bib entries | 在 .bib 中但未被 \\cite（包括 openai2024o1, min2022rethinking 等） |\n\n**修改要求**：立即核实 hobelsberger2025systematic 真实性（若虚构是严重学术诚信问题）。修正年份和作者错误。清理 orphan entries。\n\n**[W-Critical-5] Construction 效果跨数据集不一致，p_adj 数值矛盾** [R1-N2 + R2 交叉 AGREE，共识]\n\n- Few-NERD: +1.40pp（Holm p_adj=0.006，显著）✓\n- SciERC: +1.02pp — §1 报告 p_adj=0.20（不显著），但 R1 指出 Table 13 显示 p_adj=0.038——**同一结果在不同位置给出不同 p_adj，属报告失误**\n- CoNLL: -0.39pp（不显著）✗\n\n4 个数据集中仅 Few-NERD 统计显著，construction 作为 contribution 的可靠性受限。\n\n**修改要求**：澄清 p_adj 矛盾。正文醒目标注 SciERC 不显著。讨论仅 1/4 数据集显著的适用范围。\n\n### Should-Fix（影响评分但不一票否决）\n\n**[W-Warning-1] N=8/16 对 test-time compute scaling 研究范围过窄** [R1-W1 + R2 AGREE]\n相关文献测试到 N=64+。Few-NERD N=16 LP 仍有 +0.30pp gain，存在继续 scaling 空间。至少补 N=32 或论证 cost-efficiency。\n\n**[W-Warning-2] Scale/regime confound 未充分控制** [R1-W2 + R2-W1，共识]\nFine-tuned 4B-8B vs. zero-shot 72B 同时变化 fine-tuning、model size、architecture、quantization。需 hedge 结论或补控制实验。\n\n**[W-Warning-3] Cross-model consistency 过于初步** [R1-W3, R2 部分 REBUT]\n仅 1 数据集 1 对模型，但论文标注为 \"exploratory\"。R2 认为定位合理，但若保留在 §5.1 需补实验或缩减为 footnote。\n\n**[W-Warning-4] SciERC 部分关键分析基于 single seed** [R1-W4 + R2 AGREE]\nSciERC 仅 551 instances，用于 detailed diagnostic 但 single seed。bootstrap CI 有缓解但与论文整体统计标准不一致。\n\n**[W-Warning-5] Degeneracy decomposition 过松** [R2-N2, R1 部分 REBUT]\nR2 称 bound 仅解释 3-12% 的 gap。R1 REBUT 称论文给的是 equality 非 bound，但同意可降级为 analysis tool。分歧点在于 \"3-12%\" 的出处和 decomposition 的实用价值。**共识**：降级为 analysis tool 而非独立 contribution。\n\n**[W-Warning-6] Diagnostic cascade 是描述性分析而非因果链** [R2-W2, R1 AGREE with nuance]\n三个因素（degeneracy, headroom, LP compression）是 correlational structure，未排除第三变量。Entity construction 实验部分建立因果性。共识：标注为 \"descriptive diagnostic\" 更准确。\n\n**[W-Warning-7] 论文同时做 4 件事，各自深度不够** [R2-W3, R1 部分 REBUT]\nR2 认为 QE benchmark + selection failure + construction + theory 各 0.5-1 页，深度不够。R1 认为四部分构成完整故事但同意可重新分层为 2 core + 2 supporting。\n\n**[W-Warning-8] Missing related work** [R2-W4, R1 conditionally AGREE]\n缺少：EL4NER (arXiv:2505.23038)、Beyond Majority Voting (arXiv:2510.01499)、Scalable BoN via Self-Certainty (arXiv:2502.18581)、Optimal Aggregation (arXiv:2510.13918)。\n\n**[W-Warning-9] Trained verifier 负面结果 scope 有限** [R1-W5, R2 部分 REBUT]\nLightGBM 仅在 SciERC 上测试。R2 指出 AUC=0.923 说明特征足够，问题在于 discrimination→selection 转化。共识：soften 结论从 \"cannot close\" 到 \"do not close in our setting\"。\n\n---\n\n## Reviewer Consensus [AGREE]\n\n1. **Framing 需重构**：Abstract/Intro 必须前置 structural/empirical 二分法，突出 LP compression 作为核心 empirical finding [R1-N1 + R2 AGREE]\n2. **Construction 应降级**：从 standalone contribution 降为 diagnostic-motivated ablation，补引 EL4NER [R2-N1 + R1 AGREE]\n3. **Overclaim 需限定**：\"first systematic characterization\" 限定到 NER [R2-N3 + R1 AGREE]\n4. **引用必须修复**：hobelsberger2025systematic 疑似虚构需立即核实 [R2-N4 + R1 独立验证 AGREE]\n5. **p_adj 矛盾必须澄清**：SciERC construction 在 §1 和 Table 13 的数值不一致 [R1-N2 + R2 AGREE]\n6. **统计方法论是亮点**：Holm-Bonferroni, bootstrap CI, MDE/power analysis 远超 NLP 社区水准 [R1 + R2 共识]\n7. **论文适合 Findings**：有用的 empirical study + 统计示范价值，但 novelty 和 practical impact 不足以支撑 Main Conference [R1 + R2 共识]\n\n## Reviewer Divergence [REBUT]\n\n1. **Degeneracy decomposition 的性质**：R1 称论文给的是 equality（E[ΔF₁] = (1−D)·G_nd），R2 称是 bound 且仅解释 3-12%。R1 认为有 diagnostic 价值（快速判断 SC 可行性），R2 认为过松无实用性。**双方同意降级为 analysis tool。**\n\n2. **Cross-model experiment scope**：R1 认为过于初步需扩展或降级；R2 认为标注为 exploratory 定位合理，无需过多期待。**双方同意若保留需明确定位。**\n\n3. **Trained verifier 结论**：R1 认为 scope 有限不够 conclusive；R2 认为 AUC=0.923 恰恰说明问题在 discrimination→selection 转化而非特征不足。**双方同意 soften 结论。**\n\n---\n\n## Questions（需作者澄清）\n\n1. SciERC entity construction 的 p_adj 到底是 0.20 还是 0.038？两处不同的数值源于哪个 Holm family 分组？\n2. hobelsberger2025systematic 是否为真实出版物？如果是，请提供具体的出版信息（期刊/会议、DOI）。\n3. 如果 4/5 信号 by construction 不能做 selection，为什么 Abstract 仍将\"5 confidence signals for QE and sample selection\"并列？这是否误导读者？\n4. Cross-model consistency 的 +0.42pp（§5.1）是否在 R1 引用的 CI [0.27, 0.58] 内？还是 R1 看到的是 +0.32pp CI [0.27, 0.38]？数值需确认。\n5. Proposition 1 的 entity-wise independence 假设在何种 NER 场景下会被 violated？嵌套实体是否会导致 bound 失效？\n\n---\n\n## Missing References\n\n以下为两位 Reviewer 共同或独立建议补充的引用：\n\n1. **EL4NER** (arXiv:2505.23038, May 2025) — entity-level span extraction + type voting 的 ensemble NER pipeline [R2 提出, R1 AGREE, **必须引用**]\n2. **Beyond Majority Voting** (arXiv:2510.01499, Oct 2025) — 超越 majority voting 的 aggregation 方法 [R2]\n3. **Scalable Best-of-N Selection via Self-Certainty** (arXiv:2502.18581) — 直接相关的 BoN selection 方法 [R2]\n4. **Optimal Aggregation of LLM and PRM Signals** (arXiv:2510.13918) — 多 signal 聚合理论框架 [R2]\n\n---\n\n## External Review\n\n**外部审稿：未请求**（项目未配置 external_review）\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成（状态: done）。主要发现：\n\n- **[Critical] Page 7 display items 严重过密**：4 个表格（Table 2/3/4/5）+ 1 个 figure（Figure 3）挤在同一页，Figure 3 条形图极小，可读性差。相邻 page 6 和 page 8 均为纯文本——视觉节奏极不均匀。**建议移动部分 items 到 p6/p8**。\n- **[Warning] Pages 6, 8 纯文本**：无任何 figure/table/equation，形成\"文-密-文\"不良节奏。\n- **[Warning] Page 42 末页 ~75% 空白**，Page 34 ~60% 空白。\n- **[Warning] Pages 36-41 附录表格密度极高**：部分字号接近 7pt 可读性边界。\n- **[Info] Figure 6 (p18) heatmap 红绿色阶对色盲不友好**：建议改用 viridis 或 blue-orange。\n- **[Info] 正面**：booktabs 风格统一，公式渲染正确，无 [?] 未解析引用，无 margin 溢出。\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.0 (Findings)**\n\n| 维度 | R1 | R2 | 综合 |\n|------|----|----|------|\n| Soundness | 3.5 | 3.5 | 3.5 |\n| Excitement | 2.5 | 3.0 | 2.5 |\n| Reproducibility | 4.0 | 4.0 | 4.0 |\n| Overall | 3.5 | 3.0 | **3.0** |\n| Confidence | 4 | 4 | 4 |\n\n**评分理由**：\n\n论文是一项扎实的实证研究，core insight（LP compression 作为 NER selection failure 的根本原因）有诊断价值，统计方法论在 NLP 社区具有示范意义。但存在以下主要问题阻碍主会议接收：\n\n1. **Novelty 受限**：核心概念\"correlation-selection gap\"对 80% 的信号（4/5 instance-level）是定义上的必然而非实验发现，framing 制造了虚假 surprise；entity-level construction 是已有方法的迁移应用且效果不一致。\n2. **Contribution 深度不够**：4 个 contributions 各自偏浅——construction 仅 1/4 数据集显著，degeneracy bound 太松（R1/R2 分歧但同意降级），论文试图同时做太多事情。\n3. **引用问题严重**：疑似虚构引用（hobelsberger2025systematic）、年份/作者错误、缺少直接相关工作（EL4NER）。\n4. **实验覆盖有限**：N=8/16 偏小，scale confound 未控制，cross-model 过于初步。\n\n**定位建议**：如果作者 (1) 重构 framing 聚焦 LP compression 作为核心 empirical finding，(2) 将 construction 和 decomposition 降级为 supporting analyses，(3) 修复引用问题，(4) 限定 overclaim scope——论文在 Findings 中将是一篇有价值的诊断性工作。统计方法论值得社区学习。\n\n---\n\n## Detailed Comments\n\n### Section 1 (Introduction)\n- Contribution #2 中 \"That 4/5 signals are instance-level is definitional; the empirical contribution is that LP...\" 这句话应该出现在 Abstract 和 Intro 前几段，而非埋在 contribution list 中。当前读者需要读到 §3-4 才能理解核心概念的 80% 是 trivial 的。\n- \"first systematic characterization\" → \"first systematic characterization for NER\"\n\n### Section 3 (Diagnostic Framework)\n- §3.1 对 instance-level vs. per-sample 的区分是论文最重要的 methodological insight，应 promote 到 Introduction。\n- FK 的 \"inter-rater agreement\" 描述不准确——实际是 type-level agreement across N samples，非标准 inter-rater reliability 场景。\n\n### Section 4 (Why Single-Signal Selection Fails)\n- \"Definitional vs. empirical\" 区分在 §4 首段出现太晚，应在 §1 前置。\n\n### Section 5 (Adaptive Methods)\n- §5.1 Cross-model: 仅 1 数据集 1 对模型，+0.42pp。要么补实验要么缩减为 footnote。\n- §5.2 Trained verifier: AUC=0.923 但 +0.30pp——结论 \"cannot close\" 改为 \"do not close in our setting\"。\n\n### Section 6 (Threshold Regime Analysis)\n- §6.3 Degeneracy decomposition: 论文称 equality，bound ratio 3-12%（争议）。建议明确定位为 diagnostic tool。\n- Proposition 1 的 entity-wise independence 假设未讨论何时 violated。\n\n### Section 7 (Experiments)\n- Table 5 construction results: p_adj 矛盾需修复。\n- CoNLL -0.39pp 负面结果值得更多分析（是 degeneracy 还是 headroom 不足？两者在 CoNLL 上同时成立）。\n- Few-NERD 3 epochs vs 其他 5 epochs: 主文应解释原因。\n\n### Section 8 (Discussion)\n- LP compression 的 mechanistic 解释（exposure bias, constrained decoding 压缩 LP 动态范围）已有但可加深。\n- Diagnostic cascade 应标注为 \"descriptive\" 而非暗示因果关系。\n\n### References\n- 立即核实 hobelsberger2025systematic。\n- 修正 chen2025twofailures 年份（2023 非 2025）。\n- 核实 feng2025optimal 和 park2024grammar 作者信息。\n- 补引 EL4NER。\n- 清理 17 条 orphan bib entries。\n\n### Format/Layout\n- Page 7 过密（4 表 +1 图），建议分散到 p6/p8。\n- Figure 6 heatmap 色阶对色盲不友好。",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.0",
  "review_chat_id": "oc_3897c2857f11615119e277e820eae311"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "project": "struct_self_consist_ie",
    "report": "# 审稿报告 — Round 26 (Fresh Review)\n\n**论文**: \"Strong Predictors, Weak Selectors: The Correlation-Selection Gap in Self-Consistency for Named Entity Recognition\"\n**Venue**: EMNLP 2026 Main Conference (via ARR May 2026)\n**Deadline**: 2026-05-25\n**审稿模式**: Fresh（重新审稿，无上轮记忆）\n**Reviewer 编排**: 2 人（R1: 方法严谨性+实验有效性; R2: 新颖性+完整性+写作质量）\n**轮次**: Round 1 独立审稿 → 交叉分享 → 收敛（1 轮即收敛）\n\n---\n\n## Summary\n\n论文研究 test-time compute scaling (self-consistency) 应用于 NER 的效果，评估 5 种 confidence signals（Soft Jaccard, voting confidence, Fleiss' κ, exact match, log-probability）在 4 个 NER benchmark 上的 quality estimation (QE) 和 sample selection 表现。核心发现：所有信号能做可靠的 QE（ρ up to 0.45, AUROC up to 0.82），但无法可靠地选出最优 sample——作者称之为\"correlation-selection gap\"。论文提出 entity-level construction（实体级聚合）作为缓解方案，在 Few-NERD 上获得 +1.40pp（Holm p_adj=0.006），并给出 degeneracy decomposition 的理论分析。\n\n---\n\n## Strengths\n\n1. **统计方法论远超 NLP 社区平均水平** [R1, R2 共识]：Holm-Bonferroni 多重比较校正（family k=10/19/57）、bootstrap CI (B=10,000)、MDE/power analysis、TOST equivalence testing、permutation tests。这种严谨性在 NER/IE 论文中极为罕见，具有示范价值。\n\n2. **Correlation-selection gap 概念清晰、有实际价值** [R1, R2 共识]：核心观察——信号能估质量但选不出最优 sample——对 NER practitioners 直接有用，改变了 test-time scaling 的使用策略。\n\n3. **实验设计系统全面** [R2]：5 signals × 4 datasets × 2 models × 4B-8B fine-tuned + 72B zero-shot，覆盖难度梯度（WNUT-17 ~42% → CoNLL >90% F1）。\n\n4. **Diagnostic cascade 有洞察力** [R1, R2]：degeneracy → headroom → LP compression 的层级分析为理解\"为什么信号选不出最优\"提供了直觉和可复用的诊断协议（Appendix ab）。\n\n5. **极其详尽的附录** [R1, R2 共识]：30+ 页、55 个表格，涵盖 temperature/LoRA rank/free-form decoding ablation、calibration、hidden state probes、per-entity-type 分析。\n\n6. **负面结果的诚实报告** [R1]：trained verifier 失败（§5.2）、cross-model 仅 preliminary（§5.1）、construction 在 CoNLL 无效（§7.5）。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**[W-Critical-1] \"Correlation-selection gap\" 对 4/5 信号是 structural tautology，framing 过度渲染 novelty** [R1-N1 + R2 交叉 AGREE，共识]\n\n论文评估的 5 个信号中，4 个（SJ, VC, FK, EM）是 instance-level aggregates——对同一 instance 的所有 N 个 candidates 赋予相同分数。它们根据定义无法做 within-instance ranking。论文自己在 §4 (p.4) 承认：\"selection failure is a design property, not an empirical finding\"。但 Abstract 和 Introduction 的 framing 没有前置这个关键区分，读者会以为 5 个信号都是 selection 的候选者，产生虚假 surprise。\n\n真正的 empirical 贡献——LP（唯一 per-sample 信号）因 compression 失败（within-instance range ≈0.041 nats, 60% instances; §4, Figure 8）——在当前 framing 下被淹没。\n\n**修改要求**：重构 Abstract/Intro，将 structural（4/5 信号 by construction 不能 select）与 empirical（LP compression failure）明确区分并前置。\n\n**[W-Critical-2] Entity-level construction 新颖性不足，缺少关键引用** [R2-N1 + R1 交叉 AGREE，共识]\n\n- EL4NER (arXiv:2505.23038, May 2025) 已系统实现了基于多 LLM 的 entity-level span extraction + type voting pipeline，在 ICL 设置下取得 SOTA。**未被引用**。\n- Xie et al. (2023a) 已是 entity-level voting 的先驱，论文自己引用但未充分区分。\n- Entity-level construction 本质上是将已有的 entity voting 在 MBR 框架下重新包装（LP-weighted variant 仅额外 +0.30pp over uniform）。\n- +1.40pp (Few-NERD) 和 +1.02pp (SciERC, p_adj=0.20 不显著) 的改进有限。\n\n**修改要求**：补引 EL4NER 并区分（单模型 SC vs. 多模型 ensemble）。将 construction 定位为 diagnostic-motivated ablation 而非 standalone contribution。\n\n**[W-Critical-3] \"First systematic characterization\" overclaim** [R2-N3 + R1 交叉 AGREE，共识]\n\nAbstract 声称\"the first systematic characterization\"，但 Chen et al. (2023) 已研究 SC failure modes、Eikema et al. (2025) 已研究 structured MBR decoding 失效、Kang et al. (2025) 和 Taubenfeld et al. (2025) 已研究 confidence signals 与 SC。论文的\"first\"仅限于 NER + 这 5 个信号的组合。\n\n**修改要求**：限定 scope 为 \"for NER\" 或 \"in the context of structured entity extraction\"。\n\n**[W-Critical-4] 参考文献存在年份错误和疑似虚构引用** [R2-N4 + R1 交叉 AGREE，独立验证确认]\n\n| 问题 | 详情 |\n|------|------|\n| chen2025twofailures | bib 标注 2025，实际发表于 2023 (arXiv:2305.14279) |\n| feng2025optimal | bib 首作 \"Feng\"，API 返回 \"Austin\"——需核实 |\n| park2024grammar | bib 首作 \"Park\"，API 返回 \"Berg-Kirkpatrick\"——可能张冠李戴 |\n| **hobelsberger2025systematic** | **Semantic Scholar/OpenAlex 均无法验证（similarity=0.236），疑似虚构引用** |\n| 17 orphan bib entries | 在 .bib 中但未被 \\cite（包括 openai2024o1, min2022rethinking 等） |\n\n**修改要求**：立即核实 hobelsberger2025systematic 真实性（若虚构是严重学术诚信问题）。修正年份和作者错误。清理 orphan entries。\n\n**[W-Critical-5] Construction 效果跨数据集不一致，p_adj 数值矛盾** [R1-N2 + R2 交叉 AGREE，共识]\n\n- Few-NERD: +1.40pp（Holm p_adj=0.006，显著）✓\n- SciERC: +1.02pp — §1 报告 p_adj=0.20（不显著），但 R1 指出 Table 13 显示 p_adj=0.038——**同一结果在不同位置给出不同 p_adj，属报告失误**\n- CoNLL: -0.39pp（不显著）✗\n\n4 个数据集中仅 Few-NERD 统计显著，construction 作为 contribution 的可靠性受限。\n\n**修改要求**：澄清 p_adj 矛盾。正文醒目标注 SciERC 不显著。讨论仅 1/4 数据集显著的适用范围。\n\n### Should-Fix（影响评分但不一票否决）\n\n**[W-Warning-1] N=8/16 对 test-time compute scaling 研究范围过窄** [R1-W1 + R2 AGREE]\n相关文献测试到 N=64+。Few-NERD N=16 LP 仍有 +0.30pp gain，存在继续 scaling 空间。至少补 N=32 或论证 cost-efficiency。\n\n**[W-Warning-2] Scale/regime confound 未充分控制** [R1-W2 + R2-W1，共识]\nFine-tuned 4B-8B vs. zero-shot 72B 同时变化 fine-tuning、model size、architecture、quantization。需 hedge 结论或补控制实验。\n\n**[W-Warning-3] Cross-model consistency 过于初步** [R1-W3, R2 部分 REBUT]\n仅 1 数据集 1 对模型，但论文标注为 \"exploratory\"。R2 认为定位合理，但若保留在 §5.1 需补实验或缩减为 footnote。\n\n**[W-Warning-4] SciERC 部分关键分析基于 single seed** [R1-W4 + R2 AGREE]\nSciERC 仅 551 instances，用于 detailed diagnostic 但 single seed。bootstrap CI 有缓解但与论文整体统计标准不一致。\n\n**[W-Warning-5] Degeneracy decomposition 过松** [R2-N2, R1 部分 REBUT]\nR2 称 bound 仅解释 3-12% 的 gap。R1 REBUT 称论文给的是 equality 非 bound，但同意可降级为 analysis tool。分歧点在于 \"3-12%\" 的出处和 decomposition 的实用价值。**共识**：降级为 analysis tool 而非独立 contribution。\n\n**[W-Warning-6] Diagnostic cascade 是描述性分析而非因果链** [R2-W2, R1 AGREE with nuance]\n三个因素（degeneracy, headroom, LP compression）是 correlational structure，未排除第三变量。Entity construction 实验部分建立因果性。共识：标注为 \"descriptive diagnostic\" 更准确。\n\n**[W-Warning-7] 论文同时做 4 件事，各自深度不够** [R2-W3, R1 部分 REBUT]\nR2 认为 QE benchmark + selection failure + construction + theory 各 0.5-1 页，深度不够。R1 认为四部分构成完整故事但同意可重新分层为 2 core + 2 supporting。\n\n**[W-Warning-8] Missing related work** [R2-W4, R1 conditionally AGREE]\n缺少：EL4NER (arXiv:2505.23038)、Beyond Majority Voting (arXiv:2510.01499)、Scalable BoN via Self-Certainty (arXiv:2502.18581)、Optimal Aggregation (arXiv:2510.13918)。\n\n**[W-Warning-9] Trained verifier 负面结果 scope 有限** [R1-W5, R2 部分 REBUT]\nLightGBM 仅在 SciERC 上测试。R2 指出 AUC=0.923 说明特征足够，问题在于 discrimination→selection 转化。共识：soften 结论从 \"cannot close\" 到 \"do not close in our setting\"。\n\n---\n\n## Reviewer Consensus [AGREE]\n\n1. **Framing 需重构**：Abstract/Intro 必须前置 structural/empirical 二分法，突出 LP compression 作为核心 empirical finding [R1-N1 + R2 AGREE]\n2. **Construction 应降级**：从 standalone contribution 降为 diagnostic-motivated ablation，补引 EL4NER [R2-N1 + R1 AGREE]\n3. **Overclaim 需限定**：\"first systematic characterization\" 限定到 NER [R2-N3 + R1 AGREE]\n4. **引用必须修复**：hobelsberger2025systematic 疑似虚构需立即核实 [R2-N4 + R1 独立验证 AGREE]\n5. **p_adj 矛盾必须澄清**：SciERC construction 在 §1 和 Table 13 的数值不一致 [R1-N2 + R2 AGREE]\n6. **统计方法论是亮点**：Holm-Bonferroni, bootstrap CI, MDE/power analysis 远超 NLP 社区水准 [R1 + R2 共识]\n7. **论文适合 Findings**：有用的 empirical study + 统计示范价值，但 novelty 和 practical impact 不足以支撑 Main Conference [R1 + R2 共识]\n\n## Reviewer Divergence [REBUT]\n\n1. **Degeneracy decomposition 的性质**：R1 称论文给的是 equality（E[ΔF₁] = (1−D)·G_nd），R2 称是 bound 且仅解释 3-12%。R1 认为有 diagnostic 价值（快速判断 SC 可行性），R2 认为过松无实用性。**双方同意降级为 analysis tool。**\n\n2. **Cross-model experiment scope**：R1 认为过于初步需扩展或降级；R2 认为标注为 exploratory 定位合理，无需过多期待。**双方同意若保留需明确定位。**\n\n3. **Trained verifier 结论**：R1 认为 scope 有限不够 conclusive；R2 认为 AUC=0.923 恰恰说明问题在 discrimination→selection 转化而非特征不足。**双方同意 soften 结论。**\n\n---\n\n## Questions（需作者澄清）\n\n1. SciERC entity construction 的 p_adj 到底是 0.20 还是 0.038？两处不同的数值源于哪个 Holm family 分组？\n2. hobelsberger2025systematic 是否为真实出版物？如果是，请提供具体的出版信息（期刊/会议、DOI）。\n3. 如果 4/5 信号 by construction 不能做 selection，为什么 Abstract 仍将\"5 confidence signals for QE and sample selection\"并列？这是否误导读者？\n4. Cross-model consistency 的 +0.42pp（§5.1）是否在 R1 引用的 CI [0.27, 0.58] 内？还是 R1 看到的是 +0.32pp CI [0.27, 0.38]？数值需确认。\n5. Proposition 1 的 entity-wise independence 假设在何种 NER 场景下会被 violated？嵌套实体是否会导致 bound 失效？\n\n---\n\n## Missing References\n\n以下为两位 Reviewer 共同或独立建议补充的引用：\n\n1. **EL4NER** (arXiv:2505.23038, May 2025) — entity-level span extraction + type voting 的 ensemble NER pipeline [R2 提出, R1 AGREE, **必须引用**]\n2. **Beyond Majority Voting** (arXiv:2510.01499, Oct 2025) — 超越 majority voting 的 aggregation 方法 [R2]\n3. **Scalable Best-of-N Selection via Self-Certainty** (arXiv:2502.18581) — 直接相关的 BoN selection 方法 [R2]\n4. **Optimal Aggregation of LLM and PRM Signals** (arXiv:2510.13918) — 多 signal 聚合理论框架 [R2]\n\n---\n\n## External Review\n\n**外部审稿：未请求**（项目未配置 external_review）\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成（状态: done）。主要发现：\n\n- **[Critical] Page 7 display items 严重过密**：4 个表格（Table 2/3/4/5）+ 1 个 figure（Figure 3）挤在同一页，Figure 3 条形图极小，可读性差。相邻 page 6 和 page 8 均为纯文本——视觉节奏极不均匀。**建议移动部分 items 到 p6/p8**。\n- **[Warning] Pages 6, 8 纯文本**：无任何 figure/table/equation，形成\"文-密-文\"不良节奏。\n- **[Warning] Page 42 末页 ~75% 空白**，Page 34 ~60% 空白。\n- **[Warning] Pages 36-41 附录表格密度极高**：部分字号接近 7pt 可读性边界。\n- **[Info] Figure 6 (p18) heatmap 红绿色阶对色盲不友好**：建议改用 viridis 或 blue-orange。\n- **[Info] 正面**：booktabs 风格统一，公式渲染正确，无 [?] 未解析引用，无 margin 溢出。\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.0 (Findings)**\n\n| 维度 | R1 | R2 | 综合 |\n|------|----|----|------|\n| Soundness | 3.5 | 3.5 | 3.5 |\n| Excitement | 2.5 | 3.0 | 2.5 |\n| Reproducibility | 4.0 | 4.0 | 4.0 |\n| Overall | 3.5 | 3.0 | **3.0** |\n| Confidence | 4 | 4 | 4 |\n\n**评分理由**：\n\n论文是一项扎实的实证研究，core insight（LP compression 作为 NER selection failure 的根本原因）有诊断价值，统计方法论在 NLP 社区具有示范意义。但存在以下主要问题阻碍主会议接收：\n\n1. **Novelty 受限**：核心概念\"correlation-selection gap\"对 80% 的信号（4/5 instance-level）是定义上的必然而非实验发现，framing 制造了虚假 surprise；entity-level construction 是已有方法的迁移应用且效果不一致。\n2. **Contribution 深度不够**：4 个 contributions 各自偏浅——construction 仅 1/4 数据集显著，degeneracy bound 太松（R1/R2 分歧但同意降级），论文试图同时做太多事情。\n3. **引用问题严重**：疑似虚构引用（hobelsberger2025systematic）、年份/作者错误、缺少直接相关工作（EL4NER）。\n4. **实验覆盖有限**：N=8/16 偏小，scale confound 未控制，cross-model 过于初步。\n\n**定位建议**：如果作者 (1) 重构 framing 聚焦 LP compression 作为核心 empirical finding，(2) 将 construction 和 decomposition 降级为 supporting analyses，(3) 修复引用问题，(4) 限定 overclaim scope——论文在 Findings 中将是一篇有价值的诊断性工作。统计方法论值得社区学习。\n\n---\n\n## Detailed Comments\n\n### Section 1 (Introduction)\n- Contribution #2 中 \"That 4/5 signals are instance-level is definitional; the empirical contribution is that LP...\" 这句话应该出现在 Abstract 和 Intro 前几段，而非埋在 contribution list 中。当前读者需要读到 §3-4 才能理解核心概念的 80% 是 trivial 的。\n- \"first systematic characterization\" → \"first systematic characterization for NER\"\n\n### Section 3 (Diagnostic Framework)\n- §3.1 对 instance-level vs. per-sample 的区分是论文最重要的 methodological insight，应 promote 到 Introduction。\n- FK 的 \"inter-rater agreement\" 描述不准确——实际是 type-level agreement across N samples，非标准 inter-rater reliability 场景。\n\n### Section 4 (Why Single-Signal Selection Fails)\n- \"Definitional vs. empirical\" 区分在 §4 首段出现太晚，应在 §1 前置。\n\n### Section 5 (Adaptive Methods)\n- §5.1 Cross-model: 仅 1 数据集 1 对模型，+0.42pp。要么补实验要么缩减为 footnote。\n- §5.2 Trained verifier: AUC=0.923 但 +0.30pp——结论 \"cannot close\" 改为 \"do not close in our setting\"。\n\n### Section 6 (Threshold Regime Analysis)\n- §6.3 Degeneracy decomposition: 论文称 equality，bound ratio 3-12%（争议）。建议明确定位为 diagnostic tool。\n- Proposition 1 的 entity-wise independence 假设未讨论何时 violated。\n\n### Section 7 (Experiments)\n- Table 5 construction results: p_adj 矛盾需修复。\n- CoNLL -0.39pp 负面结果值得更多分析（是 degeneracy 还是 headroom 不足？两者在 CoNLL 上同时成立）。\n- Few-NERD 3 epochs vs 其他 5 epochs: 主文应解释原因。\n\n### Section 8 (Discussion)\n- LP compression 的 mechanistic 解释（exposure bias, constrained decoding 压缩 LP 动态范围）已有但可加深。\n- Diagnostic cascade 应标注为 \"descriptive\" 而非暗示因果关系。\n\n### References\n- 立即核实 hobelsberger2025systematic。\n- 修正 chen2025twofailures 年份（2023 非 2025）。\n- 核实 feng2025optimal 和 park2024grammar 作者信息。\n- 补引 EL4NER。\n- 清理 17 条 orphan bib entries。\n\n### Format/Layout\n- Page 7 过密（4 表 +1 图），建议分散到 p6/p8。\n- Figure 6 heatmap 色阶对色盲不友好。",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.0",
    "review_chat_id": "oc_3897c2857f11615119e277e820eae311"
  }
}
```

</details>

---


### Tool result

_source line 2768 · 2026-05-20T14:42:50.223698+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_1b56445332d8ca2b4964b30f300f0e00:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4250
}
```

</details>

---


### Tool call

_source line 2769 · 2026-05-20T14:42:56.798431+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': '初始化：获取项目概览 + 检查论文文件', 'status': 'completed', 'activeForm': '获取项目概览和检查论文文件'}, {'content': 'Step 0: Venue 调研（WebSearch EMNLP 2026 CFP）', 'status': 'completed', 'activeForm': '搜索 EMNLP 2026 CFP 和格式要求'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.6/0.7: 派发视觉审查 + 分配 Reviewer 任务', 'status': 'completed', 'activeForm': '派发视觉审查并分配 Reviewer 任务'}, {'content': '收集 R1 + R2 审稿报告', 'status': 'completed', 'activeForm': '收集审稿报告'}, {'content': 'Step 2: 交叉分享', 'status': 'completed', 'activeForm': '交叉分享 Reviewer 意见'}, {'content': 'Step 3: 收敛判断', 'status': 'completed', 'activeForm': '判断是否收敛'}, {'content': 'Step 4: 汇总报告 + 投递', 'status': 'completed', 'activeForm': '汇总审稿报告并投递'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': '初始化：获取项目概览 + 检查论文文件', 'status': 'completed', 'activeForm': '获取项目概览和检查论文文件'}, {'content': 'Step 0: Venue 调研（WebSearch EMNLP 2026 CFP）', 'status': 'completed', 'activeForm': '搜索 EMNLP 2026 CFP 和格式要求'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.6/0.7: 派发视觉审查 + 分配 Reviewer 任务', 'status': 'completed', 'activeForm': '派发视觉审查并分配 Reviewer 任务'}, {'content': '收集 R1 + R2 审稿报告', 'status': 'completed', 'activeForm': '收集审稿报告'}, {'content': 'Step 2: 交叉分享', 'status': 'completed', 'activeForm': '交叉分享 Reviewer 意见'}, {'content': 'Step 3: 收敛判断', 'status': 'completed', 'activeForm': '判断是否收敛'}, {'content': 'Step 4: 汇总报告 + 投递', 'status': 'completed', 'activeForm': '汇总审稿报告并投递'}]"
  }
}
```

</details>

---


### Tool result

_source line 2770 · 2026-05-20T14:42:56.849201+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "TodoWrite",
  "elapsed_ms": 50
}
```

</details>

---


### Assistant

_source line 2771 · 2026-05-20T14:43:06.134772+00:00_

审稿流程完成。

**Round 26 审稿报告已投递至 Research Director。**

核心结论：

| 项目 | 结果 |
|------|------|
| **Overall Score** | **3.0 (Findings)** |
| Soundness | 3.5 |
| Excitement | 2.5 |
| Reproducibility | 4.0 |
| Confidence | 4/5 |

**5 个 Must-Fix 问题**：
1. Framing tautology（4/5 信号 by construction 不能 select，Abstract/Intro 未前置区分）
2. Construction 新颖性不足 + 缺引 EL4NER
3. "First systematic characterization" overclaim
4. 引用问题（hobelsberger2025systematic 疑似虚构、年份/作者错误、17 orphan entries）
5. Construction p_adj 数值矛盾（§1 vs Table 13: 0.20 vs 0.038）

**9 个 Should-Fix 问题**：N 范围窄、scale confound、cross-model 初步、single seed、decomposition 松弛、cascade 非因果、4 contributions 偏浅、missing references、verifier 结论过强

**Issue tracker 已同步更新**（`review_issues.yaml`），含 R26 新发现及历史 issue 状态追踪。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 210

## Round 210

2 recorded events


### User

_source line 2772 · 2026-05-20T14:43:08.784939+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。总结：

- **R1-N1 (structural tautology)**: AGREE — R1 对 4/5 信号 definitional failure 的诊断比我更精准，支持 Abstract/Intro 重构
- **R1-N2 (construction 不一致 + p_adj 矛盾)**: AGREE — 与我的 N1 从不同角度（robustness vs. novelty）叠加
- **R1-W1 (N 范围窄)**: AGREE，但补充了 NER cost-efficiency 的缓解因素
- **R1-W2 (scale confound)**: AGREE
- **R1-W3 (cross-model 初步)**: 部分 REBUT — 论文定位为 exploratory，未 overclaim
- **R1-W4 (single seed)**: AGREE
- **R1-W5 (LightGBM 不 conclusive)**: 部分 REBUT — AUC=0.923 说明特征足够，问题在 discrimination→selection 的转化

关键分歧：R1 认为 degeneracy theory "clean" 且 entity-level construction "novel"，我不同意——bound 太松 (3-12%)，entity-level construction 已有 EL4NER 等先例。这是 R1 给 3.5 vs 我给 3.0 的主要原因。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 2773 · 2026-05-20T14:43:23.255453+00:00_

审稿流程已全部完成。

**最终结果汇总：**

| 项目 | 状态 |
|------|------|
| Overall Score | **3.0 (Findings)** |
| R1 评分 | 3.5 (Borderline Conference) |
| R2 评分 | 3.0 (Findings) |
| 交叉分享 | 1 轮收敛 |
| 视觉审查 | 已完成（1 critical: p7 过密） |
| 外部审稿 | 未配置 |
| Issue Tracker | 已更新（Round 26） |
| 报告投递 | ✓ 已送达 Research Director |

**5 个 Must-Fix 问题：**
1. Framing tautology — 4/5 信号 by construction 不能 select，需重构 Abstract/Intro
2. Construction novelty 不足 — 缺引 EL4NER，应降级为 ablation
3. "First systematic" overclaim — 需限定 scope 为 NER
4. 引用问题 — hobelsberger2025systematic 疑似虚构，多处年份/作者错误
5. Construction p_adj 矛盾 — §1 (0.20) vs Table 13 (0.038) 不一致

**核心判断：** 扎实的 empirical study，统计方法论值得学习，但 novelty 受限（核心概念对多数信号是 tautology）、construction 效果不一致、引用问题严重。定位为 Findings 合适，修复上述问题后可成为该 track 的有价值工作。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 211

## Round 211

46 recorded events


### User

_source line 2774 · 2026-05-21T04:32:42.320952+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: struct_self_consist_ie
- 论文路径: projects/struct_self_consist_ie/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: Main Conference (Long Paper)
- 截止日期: 2026-05-25

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 2775 · 2026-05-21T04:32:48.523063+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 2776 · 2026-05-21T04:32:48.574152+00:00_

1	---
2	name: review-director-session-start
3	description: Review Director session 启动初始化流程——圆桌多轮审稿协议。Review Director 角色 session 启动时自动使用。
4	priority: 9
5	scope: global
6	tags:
7	- workflow
8	- review
9	- session
10	version: 3
11	roles:
12	- review_director
13	---
14	
15	# Review Director Session 启动流程（圆桌会议模式）
16	
17	## 初始化
18	
19	1. `director_get_project_overview(project)` — 了解研究现状（实验状态、最新报告）
20	2. 读取论文文件状态：检查 `projects/{project}/paper/` 或 `main.tex` 是否存在
21	3. 检查是否有来自 Research Director 的论文提交（`[论文提交]` 消息）
22	4. 向用户简要汇报：
23	   - **投稿目标**：venue 和 deadline
24	   - **论文状态**：当前草稿位置和版本
25	   - **资料完整性**：提交的材料是否齐全
26	   - **下一步**：即将开始的圆桌审稿流程
27	
28	## 评审流程（收到论文提交后执行）
29	
30	### Step 0 — 资料检查 + Venue 调研（必须先做，不可跳过）
31	
32	1. 检查提交资料完整性：论文文件是否存在、是否可读、补充材料是否齐全
33	2. 确认目标投稿 venue（从提交消息中获取）
34	3. 用 `web_search` 搜索该 venue 当前轮次的 CFP（Call for Papers），关键词示例：
35	   - `"&lt;venue name> 2026 call for papers" site:aclweb.org`
36	   - `"&lt;venue name> 2026 submission deadline"`
37	   - `"&lt;venue name> 2026 author guidelines"`
38	4. **验证 deadline 未过期**：今天日期与截止日期对比，若已过期立即通知用户，不继续
39	5. 提取当前版本的格式要求：
40	   - 页数限制（正文 / 附录 / 参考文献）
41	   - 模板（ACL / IEEE / NeurIPS / ICML / ...）
42	   - 匿名规则（double-blind / single-blind / open）
43	   - 附录规则（是否允许、是否参与审稿）
44	   - 引用格式（natbib / biblatex / 特定 .bst）
45	6. 将以上信息作为上下文，随任务一起传递给 Reviewer
46	
47	⚠️ 禁止使用训练知识中的 venue 要求——格式标准每年都会更新，必须实时搜索确认。
48	
49	### Step 0.5 — 决定 Reviewer 编排
50	
51	根据 venue 类型和论文特点，决定：
52	- 需要几个 Reviewer（1-5 人）
53	- 每个 Reviewer 的审查侧重
54	
55	参考：
56	- **顶会长文**（NeurIPS/ICML/ACL）：3 人（方法/实验 + novelty/related work + 格式/ethics）
57	- **一般会议**（EMNLP/NAACL）：2 人（方法严谨性 + 新颖性/完整性）
58	- **Workshop / 短文**：1 人（全面审查）
59	
60	向 Group C（即项目配置中的 `feishu.review_chat_id` 审稿群）汇报编排决定。
61	
62	### Step 0.6 — 外部审稿线（与 Step 1 并行）
63	
64	检查项目配置中 `external_review.paperreview_ai.enabled` 是否为 `true`：
65	- 如果启用：调用 `request_external_review(project, paper_pdf_path, venue)` 向用户群发送协助提交卡片
66	- 这一步与 Step 1（内部 Reviewer 分配）**并行执行**，不阻塞内部审稿流程
67	- 外部结果到达后（用户在群里粘贴），纳入 Step 4 最终报告
68	- 如果到 Ste
…[truncated 3286 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 2777 · 2026-05-21T04:32:54.908282+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 2778 · 2026-05-21T04:32:54.958856+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2779 · 2026-05-21T04:32:57.618790+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool call

_source line 2780 · 2026-05-21T04:32:58.270782+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,mcp__agent-ml-research__read_local_file",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,mcp__agent-ml-research__read_local_file",
    "max_results": "2"
  }
}
```

</details>

---


### Tool result

_source line 2781 · 2026-05-21T04:32:58.321543+00:00_

{"result":"# 项目 struct_self_consist_ie 概况\n\n## 实验状态 (249 个)\n\n- **exp_002_ner_conll2003**: DONE (success) — \n- **exp_004_re_diagnostic**: DONE (success) — \n- **exp_005**: DONE (success) — \n- **exp_014_entity_majority_voting**: DONE (success) — \n- **exp_013_exact_match_voting**: DONE (negative) — \n- **exp_012_logprob_baseline**: DONE (success) — \n- **mvp_pilot_005**: DONE (negative) — \n- **e1_component_wise_re_sj**: DONE (negative) — \n- **mvp_pilot_004**: DONE (negative) — \n- **ft_002_v2**: DONE (success) — \n- **mvp_pilot_002**: DONE (failed) — \n- **ft_002**: DONE (killed) — \n- **ft_001**: DONE (success) — \n- **mvp_pilot_003**: DONE (negative) — \n- **mvp_pilot_001**: DONE (negative) — \n\n## 最新报告\n# Handover — 2026-05-21\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| exp_fewnerd_t12_s456 | FewNERD temperature ablation (T=1.2, seed=456): third seed complementing seed=42+123 for 3-seed statistical power. N=8, Qwen3-8B-FT. | — | — | — |\n| exp_fewnerd_t05_s456 | FewNERD temperature ablation (T=0.5, seed=456): third seed complementing seed=42+123 for 3-seed statistical power. N=8, Qwen3-8B-FT. | — | — | — |\n| exp_fewnerd_7b_n16_s42 | FewNERD N=16 with Qwen2.5-7B: extending N-scaling curve to N=16 for 7B model. At N=8 the 7B model shows diminishing oracle gains; N=16 tests whether the plateau continues or breaks, providing a critical data point for the N-scaling law F1(N)=a-b*N^(-c) at the 7B scale. | — | — | — |\n\n## 待处理\n- exp_b1_scd: Self-Consistency Distillation via theta2n construction pseudo-labels can teach Qwen3-8B-FT to internalize SC benefits: after iterative SCD (M0→M1→M2→M3), greedy F1 should approach N=8 construction F1 (FewNERD target: 0.764 vs current greedy 0.748). CoNLL serves as negative control (construction Δ=-0.4pp, SCD should not help). Transductive setting: pseudo-labels from test set SC outputs.（等待人工审批）\n- eval_scd_fewnerd_fallback（准备中）\n- exp_a1_spid
…[truncated 1743 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 702
}
```

</details>

---


### Tool result

_source line 2782 · 2026-05-21T04:32:58.321884+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 2783 · 2026-05-21T04:33:03.843438+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers submission guidelines ARR",
  "allowed_domains": "['aclweb.org', '2026.emnlp.org', 'openreview.net']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission guidelines ARR",
    "allowed_domains": "['aclweb.org', '2026.emnlp.org', 'openreview.net']"
  }
}
```

</details>

---


### Tool call

_source line 2784 · 2026-05-21T04:33:05.463196+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex",
    "limit": "80"
  }
}
```

</details>

---


### Tool result

_source line 2785 · 2026-05-21T04:33:05.714308+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{inconsolata}
11	\usepackage{graphicx}
12	\usepackage{booktabs}
13	\usepackage{amsmath}
14	\usepackage{amssymb}
15	\usepackage{amsthm}
16	\newtheorem{proposition}{Proposition}
17	\newtheorem{theorem}{Theorem}
18	\newtheorem{corollary}{Corollary}
19	\newtheorem{definition}{Definition}
20	\usepackage{multirow}
21	\usepackage{xcolor}
22	\usepackage{subcaption}
23	\usepackage{alphalph}
24	
25	\graphicspath{{figures/}}
26	
27	\title{The Capability Ceiling of Self-Consistency:\\ Why Entity-Level Self-Verification Fails in Structured Generation}
28	
29	\author{Anonymous}
30	
31	\begin{document}
32	\maketitle
33	
34	\input{sections/abstract}
35	\input{sections/introduction}
36	\input{sections/diagnostic}
37	\input{sections/mechanistic}
38	\input{sections/single_signal}
39	\input{sections/adaptive}
40	\input{sections/theory}
41	\input{sections/experiments_main}
42	\input{sections/background}
43	\input{sections/discussion}
44	\input{sections/conclusion}
45	
46	\section*{Limitations}
47	\input{sections/limitations}
48	
49	\section*{Ethics Statement}
50	All experiments use publicly available benchmarks (SciERC, CoNLL-2003, WNUT-17) and open-weight models (Qwen3-8B, Qwen3-4B, LLaMA-3.1-8B).
51	CoNLL-2003 is derived from the Reuters RCV1 corpus, which is available for research purposes under a NIST agreement; we use the standard research distribution.
52	No new human data was collected or annotated for this study.
53	Our findings on signal limitations could inform more reliable deployment of IE systems by guiding practitioners toward appropriate confidence signals for their use case.
54	Code and data will be released upon acceptance at [anonymized URL].
55	
56	\section*{Responsible NLP Research Checklist}
57	\input{sections/checklist}
58	
59	\bibliography{references}
60	
61	\ap
…[truncated 119 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 2786 · 2026-05-21T04:33:05.714664+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_local_file",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_local_file",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 2787 · 2026-05-21T04:33:05.765047+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 2788 · 2026-05-21T04:33:11.384877+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines ARR"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"*SEM 2026: Commitment Link for ARR-Reviewed Papers (Deadline: 10 April 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/sem-2026-commitment-link-arr-reviewed-papers-deadline-10-april-2026"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"5th Workshop on Evaluation and Comparison for NLP systems (Eval4NLP) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/5th-workshop-evaluation-and-comparison-nlp-systems-eval4nlp"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"}]

Based on the search results, here's what I found about EMNLP 2026 call for papers submission guidelines and ARR:

## Main Conference Papers

EMNLP 2026 invites the submission of long and short papers featuring substantial, original, and unpublished research on empirical methods for Natural Language Processing. Papers may contribute negative findings, survey an area, announce the creation of a new resource, argue a position, report novel linguistic insights derived using exi
…[truncated 1138 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "elapsed_ms": 7541
}
```

</details>

---


### Tool call

_source line 2789 · 2026-05-21T04:33:17.063079+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 ARR May cycle submission deadline page limit formatting requirements"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 ARR May cycle submission deadline page limit formatting requirements"
  }
}
```

</details>

---


### Tool call

_source line 2790 · 2026-05-21T04:33:17.965946+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf",
  "pages": "1-9"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf",
    "pages": "1-9"
  }
}
```

</details>

---


### Tool call

_source line 2791 · 2026-05-21T04:33:18.470399+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "struct_self_consist_ie",
  "file": "paper_checklist.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "struct_self_consist_ie",
    "file": "paper_checklist.yaml"
  }
}
```

</details>

---


### Tool result

_source line 2792 · 2026-05-21T04:33:18.672516+00:00_

PDF pages extracted: 9 page(s) from /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf (909.7KB)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 706
}
```

</details>

---


### Tool result

_source line 2793 · 2026-05-21T04:33:23.113099+00:00_

Web search results for query: "EMNLP 2026 ARR May cycle submission deadline page limit formatting requirements"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"EMNLP 2026 LaTeX Template | ACL Style Files & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/emnlp"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"EMNLP 2026 (@emnlpmeeting) / Posts / X","url":"https://x.com/emnlpmeeting?lang=en"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"}]

Based on the web search results, here is the key information about EMNLP 2026 ARR May cycle submission requirements:

## Submission Deadline

The ARR submission deadline for both long and short papers is May 25, 2026.

## Page Limits

The format is two-column with an 8-page limit for long papers and a 4-page limit for short papers.

## Formatting Requirements

EMNLP uses the standard ACL style files, so the LaTeX template is identical to the one used for ACL, NAACL, and other *ACL conferences. The style files are available at github.com/acl-org/acl-style-files.

## Limitations 
…[truncated 540 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "elapsed_ms": 6050
}
```

</details>

---


### Tool result

_source line 2794 · 2026-05-21T04:33:23.163764+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'struct_self_consist_ie'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 4693
}
```

</details>

---


### Tool call

_source line 2795 · 2026-05-21T04:33:43.518284+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "struct_self_consist_ie",
  "file": "decisions.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "struct_self_consist_ie",
    "file": "decisions.yaml"
  }
}
```

</details>

---


### Tool result

_source line 2796 · 2026-05-21T04:33:44.923105+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/decisions.yaml\", \"content\": \"_next_id: 217\\ndecisions:\\n- id: D001\\n  date: 2026-05-14 04:23 UTC\\n  summary: 'MVP 方案: ACE05 上验证 structural consistency vs Fleiss'' Kappa 的 correlation\\n    差异'\\n  rationale: 'PMC12888769 用 surface-level Fleiss'' Kappa 在 zero-shot 模型上得到 ρ=0.20-0.28，我们假设\\n    fine-tuned 模型 + structural consistency (soft Jaccard) 能达到 ρ≥0.40。这是整个论文的基础假设——如果\\n    structural consistency 不能更好地预测准确率，后续的 adaptive gating 无从谈起。Phase 0 pilot 设计: Qwen3-8B\\n    fine-tuned on ACE05, N=8 samples, 200 instances, 对比两种 consistency metric 的 Spearman\\n    ρ。Pass ≥0.40, Fail <0.30。'\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-14 04:27 UTC\\n  summary: 采纳 Reviewer 审查意见，收紧 MVP pass/fail 标准\\n  rationale: 'Reviewer 指出 5 个问题，全部合理采纳：(1) PASS 必须要求 EAE (high-headroom subtask) ρ≥0.40，仅\\n    NER 通过不够（ceiling effect 可能虚高）；(2) MARGINAL 区间加 time-boxed protocol: N=16 追加 +\\n    1天上限；(3) 加 fine-tuning 质量门控 (NER≥73, EAE≥45)，模型不行时先修 fine-tuning；(4) ACE05 今天必须确认；(5)\\n    监控 T=1.0 per-sample F1 分布，>30% F1=0 时追加 T=0.7。'\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-14 04:53 UTC\\n  summary: SciERC RE 替代 ACE05 EAE 作为 MVP high-headroom subtask\\n  rationale: ACE05 需 LDC 许可，用户未确认。SciERC 公开可得，有 NER+RE 两个 subtask。RE base F1 ~47（与\\n    ACE05 EAE ~52 相当），结构复杂度高（entity pair + relation type），headroom 大，是 EAE 的合理替代。PASS\\n    标准更新为 RE ρ≥0.40。需要补实现 RE 的 consistency + evaluation + pipeline 支持。\\n  related_experiments: []\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-14 07:38 UTC\\n  summary: 'Gate 0: NER PASS (60.4%), RE FAIL (33.8%). 执行方案 C——当前模型先跑 pilot + 追训改进版，需修复\\n    RE evaluation'\\n  rationale: RE 33.8% 低于 40% 阈值但不阻塞 pilot：(1) headroom 大，oracle best-of-N 有提升空间；(2)\\n    consistency correlation 不要求高绝对 F1，要求 per-instance variance；(3) 弱模型上验证假设结论更强。但\\n    Reviewer 发
…[truncated 10901 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 1404
}
```

</details>

---


### Tool call

_source line 2797 · 2026-05-21T04:33:45.475193+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
  "description": "Check existing review issues tracker"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
    "description": "Check existing review issues tracker"
  }
}
```

</details>

---


### Tool result

_source line 2798 · 2026-05-21T04:33:45.878523+00:00_

&lt;persisted-output>
Output too large (36.3KB). Full output saved to: /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-director-0161122b/f7203b3b-983c-4259-a341-4288c8b137b9/tool-results/bwaqi26vi.txt

Preview (first 2KB):
issues:
  # ===== 历史 resolved issues (保留，省略细节) =====
  - id: "R1-W1"
    summary: "Few-NERD 3-epoch vs SciERC 5-epoch 训练时长混淆效应"
    category: experiment
    severity: critical
    status: resolved
    first_raised_round: 1
    last_seen_round: 19
    resolution: "Reviewer PASS: 脚注+§4.1+appendix epoch data 一致。tab:epoch_confound caption 已注明 5K subsample。"
    resolution_round: 19

  - id: "R1-W2"
    summary: "\"Two jointly necessary conditions\" 因果性表述过强"
    category: framing
    severity: critical
    status: resolved
    first_raised_round: 1
    last_seen_round: 21
    resolution: "全文降级为 empirical pattern/factors。Reviewer 确认正文+appendix 15处+4处残留全部修复，0 因果语言残留。"
    resolution_round: 21

  - id: "R2-N1-old"
    summary: "Contribution 1 'methodological premise' 是定义推论"
    category: framing
    severity: critical
    status: resolved
    first_raised_round: 1
    last_seen_round: 19
    resolution: "Reviewer PASS: 标题改为 'Quality estimation framework'; Abstract 干净。"
    resolution_round: 19

  - id: "R2-N2-old"
    summary: "与 MBR 文献差异化定位不够锐利"
    category: framing
    severity: warning
    status: resolved
    first_raised_round: 1
    last_seen_round: 19
    resolution: "Reviewer PASS: Introduction 区分清晰，ρ=0.52 数据一致。"
    resolution_round: 19

  - id: "R2-N4-old"
    summary: "模型规模 3B-8B，70B+ 未知"
    category: experiment
    severity: info
    status: resolved
    first_raised_round: 1
    last_seen_round: 19
    resolution: "Round 20 检查 PASS: limitations.tex '4B-8B scale; 70B+ untested'。"
    resolution_round: 19

  - id: "R1-W3-old"
    summary: "2-seed 统计效力不足"
    category: experiment
    severity: warning
    status: resolved
    first_raised_round: 1
    
…[truncated 332 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "elapsed_ms": 403
}
```

</details>

---


### Tool call

_source line 2799 · 2026-05-21T04:33:46.179828+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/agent/config.yaml 2>/dev/null | head -80",
  "description": "Read project config for external review settings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/agent/config.yaml 2>/dev/null | head -80",
    "description": "Read project config for external review settings"
  }
}
```

</details>

---


### Tool result

_source line 2800 · 2026-05-21T04:33:46.280637+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 2801 · 2026-05-21T04:33:52.000325+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie -name \"config.yaml\" -o -name \"config.yml\" 2>/dev/null | head -5",
  "description": "Find project config file"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie -name \"config.yaml\" -o -name \"config.yml\" 2>/dev/null | head -5",
    "description": "Find project config file"
  }
}
```

</details>

---


### Tool result

_source line 2802 · 2026-05-21T04:33:52.452096+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 2803 · 2026-05-21T04:33:52.552885+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml | head -20",
  "description": "Read review issues tracker header"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml | head -20",
    "description": "Read review issues tracker header"
  }
}
```

</details>

---


### Tool result

_source line 2804 · 2026-05-21T04:33:52.603881+00:00_

issues:
  # ===== 历史 resolved issues (保留，省略细节) =====
  - id: "R1-W1"
    summary: "Few-NERD 3-epoch vs SciERC 5-epoch 训练时长混淆效应"
    category: experiment
    severity: critical
    status: resolved
    first_raised_round: 1
    last_seen_round: 19
    resolution: "Reviewer PASS: 脚注+§4.1+appendix epoch data 一致。tab:epoch_confound caption 已注明 5K subsample。"
    resolution_round: 19

  - id: "R1-W2"
    summary: "\"Two jointly necessary conditions\" 因果性表述过强"
    category: framing
    severity: critical
    status: resolved
    first_raised_round: 1
    last_seen_round: 21
    resolution: "全文降级为 empirical pattern/factors。Reviewer 确认正文+appendix 15处+4处残留全部修复，0 因果语言残留。"

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2805 · 2026-05-21T04:33:56.827205+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -n \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/agent/*.yaml /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/*.yaml 2>/dev/null || echo \"NOT_FOUND\"",
  "description": "Search for external review config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -n \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/agent/*.yaml /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/*.yaml 2>/dev/null || echo \"NOT_FOUND\"",
    "description": "Search for external review config"
  }
}
```

</details>

---


### Tool result

_source line 2806 · 2026-05-21T04:33:56.877855+00:00_

NOT_FOUND

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2807 · 2026-05-21T04:34:00.894317+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -rn \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/ 2>/dev/null | head -5 || echo \"NOT_FOUND\"",
  "description": "Search for external review config in project"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -rn \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/ 2>/dev/null | head -5 || echo \"NOT_FOUND\"",
    "description": "Search for external review config in project"
  }
}
```

</details>

---


### Tool result

_source line 2808 · 2026-05-21T04:34:01.446769+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/chats/feishu_group_oc_3897c2857f11615119e277e820eae311_director.jsonl:3:{"ts": "2026-05-14T12:12:02.856172+00:00", "role": "tool_result", "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director", "text": "1\t---\n2\tname: review-director-session-start\n3\tdescription: Review Director session 启动初始化流程——圆桌多轮审稿协议。Review Director 角色 session 启动时自动使用。\n4\tpriority: 9\n5\tscope: global\n6\ttags:\n7\t- workflow\n8\t- review\n9\t- session\n10\tversion: 3\n11\troles:\n12\t- review_director\n13\t---\n14\t\n15\t# Review Director Session 启动流程（圆桌会议模式）\n16\t\n17\t## 初始化\n18\t\n19\t1. `director_get_project_overview(project)` — 了解研究现状（实验状态、最新报告）\n20\t2. 读取论文文件状态：检查 `projects/{project}/paper/` 或 `main.tex` 是否存在\n21\t3. 检查是否有来自 Research Director 的论文提交（`[论文提交]` 消息）\n22\t4. 向用户简要汇报：\n23\t   - **投稿目标**：venue 和 deadline\n24\t   - **论文状态**：当前草稿位置和版本\n25\t   - **资料完整性**：提交的材料是否齐全\n26\t   - **下一步**：即将开始的圆桌审稿流程\n27\t\n28\t## 评审流程（收到论文提交后执行）\n29\t\n30\t### Step 0 — 资料检查 + Venue 调研（必须先做，不可跳过）\n31\t\n32\t1. 检查提交资料完整性：论文文件是否存在、是否可读、补充材料是否齐全\n33\t2. 确认目标投稿 venue（从提交消息中获取）\n34\t3. 用 `web_search` 搜索该 venue 当前轮次的 CFP（Call for Papers），关键词示例：\n35\t   - `\"&lt;venue name> 2026 call for papers\" site:aclweb.org`\n36\t   - `\"&lt;venue name> 2026 submission deadline\"`\n37\t   - `\"&lt;venue name> 2026 author guidelines\"`\n38\t4. **验证 deadline 未过期**：今天日期与截止日期对比，若已过期立即通知用户，不继续\n39\t5. 提取当前版本的格式要求：\n40\t   - 页数限制（正文 / 附录 / 参考文献）\n41\t   - 模板（ACL / IEEE / NeurIPS / ICML / ...）\n42\t   - 匿名规则（double-blind / single-blind / open）\n43\t   - 附录规则（是否允许、是否参与审稿）\n44\t   - 引用格式（natbib / biblatex / 特定 .bst）\n45\t6. 将以上信息作为上下文，随任务一起传递给 Reviewer\n46\t\n47\t⚠️ 禁止使用训练知识中的 venue 要求——格式标准每年都会更新，必须实时搜索确认。\n48\t\n49\t### Step 0.5 — 决定 Reviewer 编排\n50\t\n51\t根据 venue 类型和论文特点，决定：\n52\t- 需要几个 Reviewer（1-5 人）\n53\t- 每个 Reviewer 的审查侧重\n54\t\n55\t参考：\n56\t- **顶会长文**（NeurIPS/ICML/ACL）：3 人（方法/实验 + novelty/related work + 格式/ethics）\n57\t- **一般会议*
…[truncated 4820 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 2809 · 2026-05-21T04:34:24.445782+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "struct_self_consist_ie",
  "review_chat_id": "oc_3897c2857f11615119e277e820eae311"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "struct_self_consist_ie",
    "review_chat_id": "oc_3897c2857f11615119e277e820eae311"
  }
}
```

</details>

---


### Tool call

_source line 2810 · 2026-05-21T04:34:25.852286+00:00_

called mcp__agent-ml-research__request_external_review

<details open><summary>🔧 Tool call — mcp__agent-ml-research__request_external_review</summary>

```json
{
  "project": "struct_self_consist_ie",
  "paper_pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf",
  "venue": "EMNLP 2026",
  "note": "EMNLP 2026 ARR May cycle, Long Paper, deadline 2026-05-25"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__request_external_review",
  "tool_args": {
    "project": "struct_self_consist_ie",
    "paper_pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf",
    "venue": "EMNLP 2026",
    "note": "EMNLP 2026 ARR May cycle, Long Paper, deadline 2026-05-25"
  }
}
```

</details>

---


### Tool result

_source line 2811 · 2026-05-21T04:34:50.483302+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 26037
}
```

</details>

---


### Tool result

_source line 2812 · 2026-05-21T04:34:50.483742+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"pending\", \"message\": \"外部审稿请求已发送到用户群。将在 8 小时后自动提醒。\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__request_external_review",
  "elapsed_ms": 24631
}
```

</details>

---


### Tool call

_source line 2813 · 2026-05-21T04:34:50.684421+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "struct_self_consist_ie",
  "text": "## Round 1 审稿任务 — Reviewer 1（方法严谨性）\n\n### 论文信息\n- **标题**: The Capability Ceiling of Self-Consistency: Why Entity-Level Self-Verification Fails in Structured Generation\n- **路径**: `projects/struct_self_consist_ie/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf`\n\n### Venue 要求\n- **目标**: EMNLP 2026 Main Conference (Long Paper), ARR May cycle\n- **截止日期**: 2026-05-25\n- **正文页数限制**: 8 页（参考文献不限，Limitations/Ethics 不计入）\n- **模板**: ACL style (`\\usepackage[review]{acl}`)\n- **匿名规则**: Double-blind\n- **附录**: 允许，但审稿人不保证阅读\n- **评分标准**: 5=Consider for Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1=Do not resubmit\n\n### 你的审查侧重：方法严谨性\n\n请重点审查以下方面：\n\n1. **Diagnostic Framework（§2, §4）**\n   - 四阶段 cascade（QE → degeneracy → agreement fidelity → LP compression）的逻辑完整性\n   - 形式化定义是否精确，cascade 各阶段之间的因果/关联关系是否过度声称\n   - 信号定义（SJ, VC, FK, EM, LP）是否完整、无歧义\n\n2. **实验设计与统计检验（§7）**\n   - 数据集选择（SciERC, Few-NERD, CoNLL, WNUT-17）是否覆盖足够的任务多样性\n   - 统计方法（Holm-Bonferroni, paired bootstrap, Spearman ρ, AUROC）是否正确应用\n   - 多重比较校正是否充分（k=19 selection, k=10 construction, k=57 global）\n   - 种子数量（3-seed vs 1-seed for SciERC）对统计效力的影响\n   - 效应量是否有实际意义（+1.39 pp on Few-NERD 等）\n\n3. **数学推导（§6.3, Appendix）**\n   - Degeneracy Decomposition: E[ΔF1(A)] ≤ (1-D)·G_nd 的证明是否正确\n   - θ_crit=0.70 的推导是否合理\n   - MBR framework（§6.1）形式化是否自洽\n\n4. **Hidden-state Probe（§3）**\n   - GroupKFold CV 设计是否防止了实体泄漏\n   - AUROC 0.63-0.88 与 F1 改善 +0.30 pp 之间的 gap 解释是否充分\n   - LODO transfer drop (0.56-0.67) 的原因分析\n\n5. **结论可靠性**\n   - 核心 claim \"no entity-level agreement signal reliably improves selection\" 是否过强\n   - \"escape routes\"（construction, ensemble, LP selection）的效果量是否足以支撑 prescriptive 建议\n   - 负面结果的边界条件是否充分讨论\n\n请以 EMNLP 2026 ARR 的标准严格审稿。输出结构：Summary → Strengths → Weaknesses (Must-Fix / Should-Fix / Minor) → Questions → Missing References → Overall Assessment (评分 + 置信度)。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "struct_self_consist_ie",
    "text": "## Round 1 审稿任务 — Reviewer 1（方法严谨性）\n\n### 论文信息\n- **标题**: The Capability Ceiling of Self-Consistency: Why Entity-Level Self-Verification Fails in Structured Generation\n- **路径**: `projects/struct_self_consist_ie/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf`\n\n### Venue 要求\n- **目标**: EMNLP 2026 Main Conference (Long Paper), ARR May cycle\n- **截止日期**: 2026-05-25\n- **正文页数限制**: 8 页（参考文献不限，Limitations/Ethics 不计入）\n- **模板**: ACL style (`\\usepackage[review]{acl}`)\n- **匿名规则**: Double-blind\n- **附录**: 允许，但审稿人不保证阅读\n- **评分标准**: 5=Consider for Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1=Do not resubmit\n\n### 你的审查侧重：方法严谨性\n\n请重点审查以下方面：\n\n1. **Diagnostic Framework（§2, §4）**\n   - 四阶段 cascade（QE → degeneracy → agreement fidelity → LP compression）的逻辑完整性\n   - 形式化定义是否精确，cascade 各阶段之间的因果/关联关系是否过度声称\n   - 信号定义（SJ, VC, FK, EM, LP）是否完整、无歧义\n\n2. **实验设计与统计检验（§7）**\n   - 数据集选择（SciERC, Few-NERD, CoNLL, WNUT-17）是否覆盖足够的任务多样性\n   - 统计方法（Holm-Bonferroni, paired bootstrap, Spearman ρ, AUROC）是否正确应用\n   - 多重比较校正是否充分（k=19 selection, k=10 construction, k=57 global）\n   - 种子数量（3-seed vs 1-seed for SciERC）对统计效力的影响\n   - 效应量是否有实际意义（+1.39 pp on Few-NERD 等）\n\n3. **数学推导（§6.3, Appendix）**\n   - Degeneracy Decomposition: E[ΔF1(A)] ≤ (1-D)·G_nd 的证明是否正确\n   - θ_crit=0.70 的推导是否合理\n   - MBR framework（§6.1）形式化是否自洽\n\n4. **Hidden-state Probe（§3）**\n   - GroupKFold CV 设计是否防止了实体泄漏\n   - AUROC 0.63-0.88 与 F1 改善 +0.30 pp 之间的 gap 解释是否充分\n   - LODO transfer drop (0.56-0.67) 的原因分析\n\n5. **结论可靠性**\n   - 核心 claim \"no entity-level agreement signal reliably improves selection\" 是否过强\n   - \"escape routes\"（construction, ensemble, LP selection）的效果量是否足以支撑 prescriptive 建议\n   - 负面结果的边界条件是否充分讨论\n\n请以 EMNLP 2026 ARR 的标准严格审稿。输出结构：Summary → Strengths → Weaknesses (Must-Fix / Should-Fix / Minor) → Questions → Missing References → Overall Assessment (评分 + 置信度)。"
  }
}
```

</details>

---


### Tool result

_source line 2814 · 2026-05-21T04:35:08.090547+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 17406
}
```

</details>

---


### Tool call

_source line 2815 · 2026-05-21T04:35:08.595179+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "struct_self_consist_ie",
  "text": "## Round 1 审稿任务 — Reviewer 2（新颖性/完整性）\n\n### 论文信息\n- **标题**: The Capability Ceiling of Self-Consistency: Why Entity-Level Self-Verification Fails in Structured Generation\n- **路径**: `projects/struct_self_consist_ie/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf`\n\n### Venue 要求\n- **目标**: EMNLP 2026 Main Conference (Long Paper), ARR May cycle\n- **截止日期**: 2026-05-25\n- **正文页数限制**: 8 页（参考文献不限，Limitations/Ethics 不计入）\n- **模板**: ACL style (`\\usepackage[review]{acl}`)\n- **匿名规则**: Double-blind\n- **附录**: 允许，但审稿人不保证阅读\n- **评分标准**: 5=Consider for Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1=Do not resubmit\n\n### 你的审查侧重：新颖性/完整性\n\n请重点审查以下方面：\n\n1. **新颖性评估**\n   - 核心贡献（correlation-selection gap、diagnostic cascade、entity-level self-verification ceiling）相对于现有工作的增量创新度\n   - 与 Yao et al. (2026) 的差异化是否清晰——他们 show correlation, 本文 diagnose why it breaks at selection\n   - \"Negative result\" 论文的贡献标准：发现本身是否足够 surprising 或 insightful\n   - Prescriptive escape routes (construction, ensemble, LP selection) 是否足够 novel 或只是 engineering\n\n2. **Related Work 覆盖度（§8）**\n   - Test-time compute scaling 文献是否充分\n   - MBR decoding / structured prediction 文献是否遗漏重要工作\n   - Self-consistency 在 NER/IE 之外的应用（code generation, math reasoning）是否充分对比\n   - Calibration 文献（LP compression 相关）\n   - Conformal prediction / selective prediction 文献\n   - Entity-level verification 和 hallucination detection 文献\n\n3. **写作质量**\n   - Abstract 是否准确概括贡献且不过度声称\n   - Introduction 的叙事结构：problem → gap → contribution 是否清晰\n   - 论文章节安排是否合理（Diagnostic Framework §2 → Why Self-Verification Fails §3 → Why Single-Signal Selection Fails §4 → Adaptive §5 → Theory §6 → Experiments §7 → Related Work §8 → Discussion §9 → Conclusion §10）\n   - 信息密度是否合适，8 页内是否遗漏关键信息\n   - 术语一致性（correlation-selection gap, capability ceiling 等是否全文统一）\n\n4. **格式合规性**\n   - 正文是否 ≤8 页\n   - 匿名是否完整（无自引泄露、无致谢、无机构信息）\n   - 图表标注是否规范、可读\n   - 引用格式是否符合 ACL 标准\n\n5. **Limitations & Ethics**\n   - Limitations 是否诚实覆盖主要局限\n   - 是否遗漏关键局限（如 English-only, model scale, closed-source API 未测）\n\n请以 EMNLP 2026 ARR 的标准严格审稿。输出结构：Summary → Strengths → Weaknesses (Must-Fix / Should-Fix / Minor) → Questions → Missing References → Overall Assessment (评分 + 置信度)。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "struct_self_consist_ie",
    "text": "## Round 1 审稿任务 — Reviewer 2（新颖性/完整性）\n\n### 论文信息\n- **标题**: The Capability Ceiling of Self-Consistency: Why Entity-Level Self-Verification Fails in Structured Generation\n- **路径**: `projects/struct_self_consist_ie/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf`\n\n### Venue 要求\n- **目标**: EMNLP 2026 Main Conference (Long Paper), ARR May cycle\n- **截止日期**: 2026-05-25\n- **正文页数限制**: 8 页（参考文献不限，Limitations/Ethics 不计入）\n- **模板**: ACL style (`\\usepackage[review]{acl}`)\n- **匿名规则**: Double-blind\n- **附录**: 允许，但审稿人不保证阅读\n- **评分标准**: 5=Consider for Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1=Do not resubmit\n\n### 你的审查侧重：新颖性/完整性\n\n请重点审查以下方面：\n\n1. **新颖性评估**\n   - 核心贡献（correlation-selection gap、diagnostic cascade、entity-level self-verification ceiling）相对于现有工作的增量创新度\n   - 与 Yao et al. (2026) 的差异化是否清晰——他们 show correlation, 本文 diagnose why it breaks at selection\n   - \"Negative result\" 论文的贡献标准：发现本身是否足够 surprising 或 insightful\n   - Prescriptive escape routes (construction, ensemble, LP selection) 是否足够 novel 或只是 engineering\n\n2. **Related Work 覆盖度（§8）**\n   - Test-time compute scaling 文献是否充分\n   - MBR decoding / structured prediction 文献是否遗漏重要工作\n   - Self-consistency 在 NER/IE 之外的应用（code generation, math reasoning）是否充分对比\n   - Calibration 文献（LP compression 相关）\n   - Conformal prediction / selective prediction 文献\n   - Entity-level verification 和 hallucination detection 文献\n\n3. **写作质量**\n   - Abstract 是否准确概括贡献且不过度声称\n   - Introduction 的叙事结构：problem → gap → contribution 是否清晰\n   - 论文章节安排是否合理（Diagnostic Framework §2 → Why Self-Verification Fails §3 → Why Single-Signal Selection Fails §4 → Adaptive §5 → Theory §6 → Experiments §7 → Related Work §8 → Discussion §9 → Conclusion §10）\n   - 信息密度是否合适，8 页内是否遗漏关键信息\n   - 术语一致性（correlation-selection gap, capability ceiling 等是否全文统一）\n\n4. **格式合规性**\n   - 正文是否 ≤8 页\n   - 匿名是否完整（无自引泄露、无致谢、无机构信息）\n   - 图表标注是否规范、可读\n   - 引用格式是否符合 ACL 标准\n\n5. **Limitations & Ethics**\n   - Limitations 是否诚实覆盖主要局限\n   - 是否遗漏关键局限（如 English-only, model scale, closed-source API 未测）\n\n请以 EMNLP 2026 ARR 的标准严格审稿。输出结构：Summary → Strengths → Weaknesses (Must-Fix / Should-Fix / Minor) → Questions → Missing References → Overall Assessment (评分 + 置信度)。"
  }
}
```

</details>

---


### Tool result

_source line 2816 · 2026-05-21T04:35:10.205789+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1610
}
```

</details>

---


### Tool call

_source line 2817 · 2026-05-21T04:35:21.745585+00:00_

called ScheduleWakeup

<details open><summary>🔧 Tool call — ScheduleWakeup</summary>

```json
{
  "delaySeconds": "270",
  "reason": "等待 Reviewer 1 和 Reviewer 2 完成 Round 1 初审（约 4-5 分钟）",
  "prompt": "系统通知：审稿审批已通过。请开始审稿。\n\n[论文提交]\n- 项目: struct_self_consist_ie\n- 论文路径: projects/struct_self_consist_ie/docs/paper/main.tex\n- 目标 venue: EMNLP 2026\n- 投稿类别: Main Conference (Long Paper)\n- 截止日期: 2026-05-25\n\n请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ScheduleWakeup",
  "tool_args": {
    "delaySeconds": "270",
    "reason": "等待 Reviewer 1 和 Reviewer 2 完成 Round 1 初审（约 4-5 分钟）",
    "prompt": "系统通知：审稿审批已通过。请开始审稿。\n\n[论文提交]\n- 项目: struct_self_consist_ie\n- 论文路径: projects/struct_self_consist_ie/docs/paper/main.tex\n- 目标 venue: EMNLP 2026\n- 投稿类别: Main Conference (Long Paper)\n- 截止日期: 2026-05-25\n\n请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。"
  }
}
```

</details>

---


### Tool result

_source line 2818 · 2026-05-21T04:35:21.796271+00:00_

Next wakeup scheduled for 04:40:00 (in 278s).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ScheduleWakeup",
  "elapsed_ms": 50
}
```

</details>

---


### Assistant

_source line 2819 · 2026-05-21T04:35:25.425042+00:00_

Reviewer 1 和 Reviewer 2 正在独立审稿。预计 4-5 分钟后检查进度。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 212

## Round 212

2 recorded events


### User

_source line 2820 · 2026-05-21T04:42:09.306521+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 — Round 1 审稿完成（方法严谨性）

### 总体评分

**Overall**: 3.5 — Borderline Conference
**Soundness**: 3.5/5 | **Excitement**: 3/5 | **Reproducibility**: 4/5 | **Confidence**: 4/5

**一句话总结**: 一篇方法论严谨、实验规模令人印象深刻的负面结果论文，系统揭示了 self-consistency 在结构化生成中的能力天花板，但范围局限于 NER + 2 个~8B 模型系列，部分核心推导的理论性被夸大，限制了结论的泛化性。

---

### Must-Fix 问题（3 个）

**N1** [critical] θ_crit = 0.70 推导本质是半经验的，但呈现为理论结果
- §6.3, Appendix p.3 (p25), Figure 9
- θ_crit 公式嵌入了 SciERC 经验参数（G_gap=14.8pp, ε=0.068），不是纯理论阈值。CoNLL（D=61.7%<0.70）上 LP 选择也失效的事实进一步说明该阈值非普适。
- 建议：明确标注为 data-dependent 经验近似，增加敏感性分析。

**N2** [critical] 种子数不对称影响统计效力均衡性
- §7.1, Table 1-2
- SciERC 3 seeds vs. 其他数据集 1 seed。Few-NERD（最强正面信号 +1.39pp）无法验证跨 seed 稳定性。核心负面结论在 3/4 数据集上依赖单次运行。
- 建议：至少为 Few-NERD 补做 3-seed 实验。

**N3** [critical] Cascade 四阶段的因果声称缺乏因果干预论证
- §3-4, Figure 1
- 流程箭头和 "Why" 标题暗示因果关系，但实际论证的是描述性诊断和相关性。无干预实验（如人工控制 degeneracy 水平）。
- 建议：将 "Why" 改为 "Where and How"，明确声明 cascade 是诊断工具而非因果模型。

### Should-Fix 问题（4 个）

**W1** "Escape routes" 效果量过于边际（最大 +1.39pp），与标注噪声量级相当，实用价值存疑。
**W2** 标题 "Structured Generation" 范围过宽——实验仅覆盖 NER + 1 个 exploratory RE，RE 结果（Appendix o）显示与 NER 不同模式。
**W3** LODO transfer 分析不充分——未识别 transfer-critical 特征，"introspection boundary" 论证不完整。
**W4** 缺少 NER-specific 或 structured MBR baseline 对比（如 Eikema et al. 2025 已引用未实验）。

### 主要优势

1. 实验规模和统计严谨性令人印象深刻（42页，50+ 表图，Holm-Bonferroni/bootstrap/permutation/TOST）
2. Diagnostic cascade 框架设计优雅，有独立工具价值
3. 诚实报告负面结果并提供 prescriptive protocol
4. MBR 形式化为 entity construction 提供理论基础
5. Degeneracy Decomposition 上界简洁有力

### 引用检查
81 bib entries, 45 cited, 36 orphan (uncited), 0 missing. 所有引用在线验证通过（2 个 OpenAlex 未索引但确认存在，5 个 LaTeX 编码差异）。建议清理 orphan entries。

---

完整审稿意见已在 session 中存档，等待 Director 指示是否需要进一步深入特定问题。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 2821 · 2026-05-21T04:42:14.641235+00:00_

Reviewer 1 已返回。等待 Reviewer 2。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 213

## Round 213

8 recorded events


### User

_source line 2822 · 2026-05-21T04:42:28.220644+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 — Round 1 审稿报告（新颖性/完整性）

**论文**: The Capability Ceiling of Self-Consistency: Why Entity-Level Self-Verification Fails in Structured Generation
**Venue**: EMNLP 2026 Main Conference (Long Paper), ARR May cycle

---

## 总体评分

**Overall**: 3.5 — Borderline Conference
**一句话总结**: 一篇实验极其扎实的 negative result/analysis 论文，diagnostic cascade 框架有用，但核心发现的 novelty 有限——instance degeneracy 作为 SC 失效的主因属于"合理但不够 surprising"的 insight，且 Related Work 覆盖存在明显缺口。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| **Soundness** | 3.5/5 | 实验设计严谨（4 NER 数据集 + 1 RE 扩展、2 模型家族、多 N 值、3 seeds），统计检验完备（Holm-Bonferroni, permutation tests, bootstrap CI），但若干因果性 claim 的支撑仍是相关性而非严格因果推断 |
| **Excitement** | 3/5 | 对 practitioner 有直接 actionable value（"不要在 degenerate regime 用 SC"），但核心 insight（structured output 的 degeneracy 导致 SC 失效）与 Yun et al. (2025) 关于 constrained decoding diversity collapse 的发现高度重叠，增量有限 |
| **Reproducibility** | 4/5 | 超参数、prompt template、训练细节在 Appendix 中充分给出；代码承诺 release；唯一不足是 LoRA 训练的 exact checkpoint 未提供 |
| **Overall Assessment** | 3.5/5 | Borderline Conference — 实验质量足以支撑 Findings，但 novelty 对 Main 会议偏弱 |
| **Confidence** | 4/5 | 我对 test-time compute scaling、NER 和 self-consistency 文献较为熟悉 |

---

## 主要优势

**S1. 实验规模和严谨度出色。** 4 个 NER 数据集（SciERC, Few-NERD, CoNLL, WNUT-17）+ RE 扩展（SciERC RE），2 个模型家族（Qwen3-8B, LLaMA-3.1-8B-Instruct），N∈{2,...,32}，3 seeds，配合 bootstrap CI、permutation tests、Holm-Bonferroni 校正，实验可信度高。42 页附录覆盖了几乎所有合理的 ablation 和 robustness check。

**S2. Diagnostic cascade 框架结构清晰。** 四阶段分解（QE → degeneracy → agreement fidelity → LP compression）将一个模糊的问题（"为什么 SC 不 work"）分解成可操作的诊断步骤。Figure 1 的可视化概括力强。尤其是对 instance degeneracy 的量化（82.9% 的 SciERC 输出完全一致，Table 2）有力解释了 selection 无从下手的根因。

**S3. Entity-level self-verification ceiling 的系统性测试。** 七种方法（ESJ, MRSC, LSC, hidden-state probe, ASB, SCD, supervised classifier）逐一测试并 fail，形成了一个令人信服的 negative result。特别是 supervised hidden-state probe 仅达到 entity-level AUROC 0.63–0.88（§3, Table 1），表明质量信号即使存在也无法有效 operationalize。

**S4. 与 MBR decoding 的理论联系。** §6 和 Appendix p 将 NER SC 形式化为 entity-level MBR decoding（Proposition 1: majority-vote 是 balanced set-overlap utility 下的 MBR optimal），提供了 principled 的理论基础。Degeneracy Decomposition（Definition 2, Corollary 1）给出了 SC 失效的 sufficient condition。

**S5. Prescriptive escape routes 具实用价值。** Entity-level construction bypasses selection entirely（+1.09pp Few-NERD, +1.02pp SciERC），LP-weighted entity construction 在低退化 regime 有效，cross-model ensemble 提供互补信号——对 practitioner 可直接 adopt。

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] **Related Work 存在严重引用缺口——多篇 directly relevant 的论文在 .bib 中但未在正文引用**

- 具体位置：§8 Related Work（仅 ~0.5 page）；.bib 文件中有 36 条 orphan entries
- 问题：引用验证显示以下高度相关的论文存在于 .bib 但从未在正文 cite：
  - **Chen et al. (2024) "Two Failures of Self-Consistency in the Multi-Step Reasoning of LLMs"** (TMLR) — 直接研究 SC 的 failure modes，是本文最直接的 prior work 之一
  - **Chen et al. (2024) "Universal Self-Consistency for Large Language Model Generation"** (ICML Workshop) — 提出不依赖 equivalence class 的 USC 方法，与本文的 structured output 场景直接相关
  - **Aggarwal et al. (2023) "Let's Sample Step by Step: Adaptive-Consistency"** (EMNLP) — 提出 adaptive stopping，与本文 §5 的 prescriptive 方向高度相关
  - **Thirukovalluru et al. (2024) "Atomic Self-Consistency"** (EMNLP) — 将 SC 应用于 atomic claims 的 fine-grained level，与 entity-level 思路直接可比
  - **Farquhar et al. (2024) "Detecting Hallucinations via Semantic Entropy"** (Nature) — semantic entropy 作为 sample-based 信号与本文所测 signals 有直接可比性
- 为什么影响接收：这些遗漏使 Related Work 显得不完整。特别是 Chen et al. (2024) "Two Failures" 已经从 reasoning 角度分析了 SC 的 failure，不讨论它会让审稿人质疑 novelty claim 的准确性。
- 建议：在 §8 中至少用 1-2 段讨论 SC 在 non-IE 场景的已知 failure modes 及 fine-grained SC 变体，明确说明本文在 structured generation 中的差异化贡献。

**N2** [critical] **核心因果 claim "degeneracy causes selection failure" 的支撑仍是相关性证据**

- 具体位置：§4 "Why Single-Signal Selection Fails"；§6.3 "Degeneracy Decomposition"；Figure 3
- 问题：论文主 claim 之一是 degeneracy *导致* selection failure（例如 §4: "degeneracy alone props LP gains across datasets, ρ=0.032, n=25, p=0.81"）。但提供的证据是 Spearman ρ 和 controlled splits（high-degeneracy vs. low-degeneracy subsets），这仅建立了 association。在 §7.3 cross-dataset contrast 中，"degeneracy alone does not predict LP direction"（§7.3），又表明 degeneracy 不是唯一因素。这造成了叙事的内部张力——一边说 degeneracy 是 dominant factor，一边说它不能 predict LP direction。
- 为什么影响接收：如果因果 claim 不成立，那么 diagnostic cascade 的第一层（degeneracy gating）作为 prescriptive 工具的可靠性就存疑。
- 建议：(1) 软化因果语言，用 "strongly associated with" 替代 "causes"；(2) 或者用 instrumental variable 或 natural experiment（如 temperature 变化产生的 degeneracy 变化）做更严格的因果论证。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] **与 Yun et al. (2025) "The Price of Format: Diversity Collapse in LLMs" 的差异化不够清晰**

- 具体位置：§8 第 2 段引用了 Yun et al. (2025)，仅一句带过
- 问题：Yun et al. (2025) 已经证明 constrained decoding 导致 diversity collapse——这与本文发现的 instance degeneracy（82.9% 输出完全一致）高度相关。本文虽引用了 Yun et al.，但没有明确讨论：本文的 degeneracy 发现相比 Yun et al. 的 diversity collapse 有何 *新增 insight*？如果 Yun et al. 已解释了"为什么结构化输出的 diversity 低"，本文的贡献是否仅在于"量化了这对 selection 的影响"？
- 建议：在 §8 或 §9 中用至少 3-4 句明确 delineate：Yun et al. 关注 diversity 本身，本文关注 diversity collapse 对 downstream selection 的功能性影响（correlation-selection gap），这是不同的 research question。

**W2** [warning] **§8 Related Work 过于压缩，缺乏对关键方向的充分覆盖**

- 具体位置：§8 总长约 0.5 页（page 8 上半部分）
- 问题：以下方向覆盖不足或缺失：
  - **Conformal prediction for structured outputs**: 论文在 §8 引用了 Geifman & El-Yaniv (2017) 做 selective prediction，但完全没讨论 conformal prediction 在 NER/IE 上的应用。最新的 PASC (2025) 提出了 pipeline-aware conformal prediction for multi-stage NLP pipelines（直接对标 IE 场景）。Kuleshov & Liang (2015) 的 calibrated structured prediction 在 bib 中但未 cite。
  - **SC 在 code generation 的 failure**: 近期 "Existing LLMs Are Not Self-Consistent For Simple Tasks" (2025) 和 "Evaluating Self-Consistency of Code LLMs" (ICLR 2024) 都研究了 SC 在非 reasoning 场景的 failure——与本文形成互补，应讨论。
  - **Entity-level hallucination detection**: Farquhar et al. (2024) semantic entropy、Min et al. (2023) FActScore 虽已引用，但未在 Related Work 中讨论它们与 entity-level self-verification 的关系。
- 建议：将 Related Work 扩展至至少 0.75 页，增加上述方向的讨论。

**W3** [warning] **RE extension（§7, Appendix o）作为 generalizability 证据说服力不足**

- 具体位置：Appendix o（page 24）；§7 中 RE 结果提及寥寥
- 问题：RE 扩展仅在 SciERC 的一个数据集上做了 exploratory 实验，且仅用 Qwen3-8B 单模型。Table 28 的结果显示 RE 的 selection failure 模式与 NER 不同（RE 的 per-entity-type 分析显示不同 pattern）。论文在 Limitations 中承认 RE 是 "exploratory"，但仍在 abstract 和 introduction 中宣称研究的是 "structured information extraction"——这个 scope claim 大于实际覆盖。
- 建议：将 abstract/intro 中的 scope 从 "information extraction" 缩窄为 "named entity recognition"，或在 RE 上补充至少一个额外数据集和模型。

**W4** [warning] **Entity-level construction 的 +1.09pp 增益虽 statistically significant，但实际影响有限**

- 具体位置：§5, §7.5（Table 5）
- 问题：论文将 entity-level construction（bypass selection entirely，+1.09pp on Few-NERD, +1.02pp on SciERC）作为主要 prescriptive 贡献。但从 practitioner 角度，这个增益的 cost-benefit 需要讨论：生成 N=8 个样本的计算开销是 single-sample 的 8 倍，而回报是 ~1pp F1。Table 5 显示 cross-model ensemble 仅 +0.42pp。在 high-degeneracy regime（占绝大多数 instances），all signals 都无法帮助。
- 建议：在 §9 Discussion 中增加 cost-benefit 分析，帮助 practitioner 判断何时值得使用这些方法。

---

## 小问题（不影响接收）

**M1.** §2.1 中 "per-sample signal" 的定义出现在 Appendix a 而非正文。正文首次使用时（page 3, "produces a single score per input (notation in Appendix a)"）应在正文中给出简要定义，不应完全 defer 到附录。

**M2.** Figure 2 (page 4) 的 bar chart 在灰度打印时 greedy/LP/EM/SJ 的颜色难以区分。建议使用 hatching patterns 增强可读性。

**M3.** Table 1 (page 4) 的 "One score per input" 列缺少解释。reviewer 需要翻到 Appendix a 才能理解 instance-level vs. per-sample 的区别。

**M4.** §6.2 "Scaling and Inverse Scaling" 中引用了 Brown et al. (2024) 和 Snell et al. (2025)，但 inverse scaling 的具体机制（为什么 SciERC converges more slowly）缺乏解释，仅一句 "the ceiling grows, but confidence-based aggregation recovery <1 pp" 带过。

**M5.** Limitations 中承认了 "English-only" 和 "model scale" 局限，但没有提及一个重要局限：所有实验都在 fine-tuned models 上进行，没有测试 closed-source API models（GPT-4, Claude 等）的 zero-shot 表现。这些模型可能有不同的 degeneracy 特征。虽然在 Limitations page 9 有提及 "closed-source APIs where log-probabilities are unavailable"，但这只是关于 LP signal 的可用性，没有讨论这些模型是否会有不同的 degeneracy profile。

**M6.** 36 个 orphan bib entries（在 .bib 中但未被引用）应清理。

---

## Questions for Authors

**Q1.** 在 degeneracy 最高的 SciERC 上（82.9% identical outputs），如果将 temperature 从 T=1.0 提高到 T=1.5 或 T=2.0 以人为增加 diversity，selection 方法是否能 recover 部分 gain？Appendix b 有 temperature robustness 分析但似乎仅测到 T=1.2。

**Q2.** Chen et al. (2024) "Two Failures of Self-Consistency" 识别了 hypothetical consistency 和 compositional consistency 两种 failure mode。本文的 degeneracy-driven failure 是否可以映射到这两类之一，还是属于第三种 failure mode？

**Q3.** Supervised hidden-state probe 的 AUROC 在 entity-level 达到 0.63–0.88，但在 sample-level 转化为 selection gain 有限。这是否暗示 bottleneck 不在 quality estimation 而在 aggregation？如果是，是否有替代 F1 的 aggregation metric 能更好利用 entity-level 信号？

**Q4.** 论文测试了 entity-level construction 和 cross-model ensemble 作为 escape routes。是否考虑过 entity-level *filtering*（即只在 high-consistency entities 上 select，对 low-consistency entities abstain）作为中间方案？

---

## Missing References

1. **Chen et al. (2024)** "Two Failures of Self-Consistency in the Multi-Step Reasoning of LLMs" (TMLR) — 直接分析 SC 失败原因
2. **Chen et al. (2024)** "Universal Self-Consistency for Large Language Model Generation" (ICML Workshop) — 不依赖 equivalence class 的 SC 变体
3. **Aggarwal et al. (2023)** "Let's Sample Step by Step: Adaptive-Consistency" (EMNLP) — 提出 adaptive sample stopping
4. **Thirukovalluru et al. (2024)** "Atomic Self-Consistency for Better Long Form Generations" (EMNLP) — fine-grained SC
5. **Farquhar et al. (2024)** "Detecting Hallucinations in LLMs Using Semantic Entropy" (Nature) — sample-based 不确定性估计
6. PASC (2025) — "Pipeline-Aware Conformal Prediction with Joint Coverage Guarantees for Multi-Stage NLP Pipelines" — conformal prediction for IE pipelines
7. "Existing LLMs Are Not Self-Consistent For Simple Tasks" (2025) — SC failure 在简单任务上的近期分析
8. Kuleshov & Liang (2015) "Calibrated Structured Prediction" (NeurIPS) — calibration for structured outputs（已在 bib 中但未引用）

注：上述 1-5 条已存在于 .bib 文件但未被 cite——这尤其令人困惑，暗示作者知道这些工作但选择不讨论。

---

## 格式合规性检查

| 检查项 | 状态 | 备注 |
|--------|------|------|
| 正文 ≤8 页 | ✅ | §1–§10 在 page 1–8，Limitations 从 page 8 底部开始 |
| 匿名性 | ✅ | "Anonymous ACL submission"，未发现自引泄露或机构信息 |
| ACL style [review] | ✅ | 行号可见，双栏格式正确 |
| 图表标注 | ✅ | Figure 1–3, Table 1–5 编号连续，caption 信息充分 |
| 引用格式 | ⚠️ | 36 个 orphan bib entries 应清理；部分 author name encoding mismatch（如 Müller vs M\"uller）但不影响引用显示 |
| Limitations | ✅ | 覆盖了主要局限（English-only, model scale, RE exploratory） |
| Ethics Statement | ✅ | 存在且合理 |
| Responsible NLP Checklist | ✅ | 完整填写（page 10） |

---

## 引用验证摘要

- 总 bib 条目: 81 | 正文引用 unique keys: 45 | orphan entries: 36
- 在线验证: 74 verified, 2 not found (OpenAlex limitation), 5 minor mismatch (LaTeX encoding)
- 无虚假引用（hallucinated citations）
- 无 missing bib（所有 \cite 都有对应 bib entry）


---

[Reviewer 1 审稿结果]:
Round 1 审稿完成，已提交给 Review Director。

**评分**: Overall 3.5 (Borderline Conference) | Soundness 3.5 | Excitement 3 | Reproducibility 4 | Confidence 4

**3 个 Must-Fix**:
1. θ_crit=0.70 是半经验推导但呈现为理论结果——嵌入了 SciERC 特定参数，非普适阈值
2. 种子数不对称（SciERC 3-seed vs 其他 1-seed）——核心负面结论在 3/4 数据集上依赖单次运行，Few-NERD +1.39pp 的稳定性无法验证
3. Cascade 四阶段的因果声称缺乏干预实验支撑——实际是描述性诊断，标题 "Why" 和流程箭头暗示了过强的因果关系

**4 个 Should-Fix**: escape routes 效果量边际（≤1.4pp）、标题 "Structured Generation" 范围过宽、LODO transfer 分析不充分、缺少 structured MBR baseline 对比。

**主要优势**: 实验规模和统计严谨性出色（42页 50+表图），diagnostic cascade 有独立工具价值，MBR 形式化和 degeneracy decomposition 理论贡献扎实。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 2823 · 2026-05-21T04:43:01.939243+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "struct_self_consist_ie",
  "text": "## Step 2 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见\n\n以下是 Reviewer 2 的完整审稿意见。请逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n# Reviewer 2 — Round 1 审稿报告（新颖性/完整性）\n\n**Overall**: 3.5 — Borderline Conference\n**Soundness**: 3.5/5 | **Excitement**: 3/5 | **Reproducibility**: 4/5 | **Confidence**: 4/5\n\n**一句话总结**: 一篇实验极其扎实的 negative result/analysis 论文，diagnostic cascade 框架有用，但核心发现的 novelty 有限——instance degeneracy 作为 SC 失效的主因属于\"合理但不够 surprising\"的 insight，且 Related Work 覆盖存在明显缺口。\n\n## Must-Fix 问题\n\n**N1** [critical] **Related Work 存在严重引用缺口——多篇 directly relevant 的论文在 .bib 中但未在正文引用**\n- 具体位置：§8 Related Work（仅 ~0.5 page）；.bib 文件中有 36 条 orphan entries\n- 问题：引用验证显示以下高度相关的论文存在于 .bib 但从未在正文 cite：\n  - Chen et al. (2024) \"Two Failures of Self-Consistency\" (TMLR)\n  - Chen et al. (2024) \"Universal Self-Consistency\" (ICML Workshop)\n  - Aggarwal et al. (2023) \"Adaptive-Consistency\" (EMNLP)\n  - Thirukovalluru et al. (2024) \"Atomic Self-Consistency\" (EMNLP)\n  - Farquhar et al. (2024) \"Semantic Entropy\" (Nature)\n- 为什么影响接收：这些遗漏使 Related Work 显得不完整。特别是 Chen et al. (2024) \"Two Failures\" 已经从 reasoning 角度分析了 SC 的 failure，不讨论它会让审稿人质疑 novelty claim。\n\n**N2** [critical] **核心因果 claim \"degeneracy causes selection failure\" 的支撑仍是相关性证据**\n- 具体位置：§4, §6.3, Figure 3\n- 问题：论文主 claim 是 degeneracy *导致* selection failure，但证据是 Spearman ρ 和 controlled splits。在 §7.3 cross-dataset contrast 中，\"degeneracy alone does not predict LP direction\"，又表明 degeneracy 不是唯一因素。这造成叙事内部张力。\n\n## Should-Fix 问题\n\n**W1** 与 Yun et al. (2025) \"The Price of Format: Diversity Collapse in LLMs\" 的差异化不够清晰。\n**W2** §8 Related Work 过于压缩（~0.5页），缺乏对 conformal prediction、SC code generation failure、entity-level hallucination detection 的覆盖。\n**W3** RE extension 作为 generalizability 证据说服力不足（单数据集单模型），但 abstract/intro scope claim \"structured information extraction\" 过宽。\n**W4** Entity-level construction +1.09pp 增益的 cost-benefit 未讨论（8x 推理开销换 ~1pp F1）。\n\n## 小问题\nM1. per-sample signal 定义 defer 到 Appendix 不当。M2. Figure 2 灰度可读性差。M3. Table 1 列缺解释。M4. §6.2 inverse scaling 机制解释不足。M5. Limitations 未提 closed-source API 的 degeneracy profile 差异。M6. 36 orphan bib entries。\n\n## Questions\nQ1. T>1.2 能否 recover diversity 改善 selection？\nQ2. 本文 failure mode 与 Chen et al. (2024) 的两种 failure 的关系？\nQ3. AUROC 0.63-0.88 无法转化为 selection gain，是否 bottleneck 在 aggregation？\nQ4. 是否考虑过 entity-level filtering（high-consistency select, low-consistency abstain）？\n\n## Missing References\n1. Chen et al. (2024) \"Two Failures of SC\" (TMLR)\n2. Chen et al. (2024) \"Universal SC\" (ICML Workshop)\n3. Aggarwal et al. (2023) \"Adaptive-Consistency\" (EMNLP)\n4. Thirukovalluru et al. (2024) \"Atomic SC\" (EMNLP)\n5. Farquhar et al. (2024) \"Semantic Entropy\" (Nature)\n6. PASC (2025) conformal prediction for IE pipelines\n7. \"Existing LLMs Are Not Self-Consistent For Simple Tasks\" (2025)\n8. Kuleshov & Liang (2015) \"Calibrated Structured Prediction\" (NeurIPS)\n\n---\n\n请对以上每个 Must-Fix (N1, N2)、Should-Fix (W1-W4)、Minor (M1-M6) 和 Questions (Q1-Q4) 逐条给出 [AGREE] 或 [REBUT] 回应。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "struct_self_consist_ie",
    "text": "## Step 2 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见\n\n以下是 Reviewer 2 的完整审稿意见。请逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n# Reviewer 2 — Round 1 审稿报告（新颖性/完整性）\n\n**Overall**: 3.5 — Borderline Conference\n**Soundness**: 3.5/5 | **Excitement**: 3/5 | **Reproducibility**: 4/5 | **Confidence**: 4/5\n\n**一句话总结**: 一篇实验极其扎实的 negative result/analysis 论文，diagnostic cascade 框架有用，但核心发现的 novelty 有限——instance degeneracy 作为 SC 失效的主因属于\"合理但不够 surprising\"的 insight，且 Related Work 覆盖存在明显缺口。\n\n## Must-Fix 问题\n\n**N1** [critical] **Related Work 存在严重引用缺口——多篇 directly relevant 的论文在 .bib 中但未在正文引用**\n- 具体位置：§8 Related Work（仅 ~0.5 page）；.bib 文件中有 36 条 orphan entries\n- 问题：引用验证显示以下高度相关的论文存在于 .bib 但从未在正文 cite：\n  - Chen et al. (2024) \"Two Failures of Self-Consistency\" (TMLR)\n  - Chen et al. (2024) \"Universal Self-Consistency\" (ICML Workshop)\n  - Aggarwal et al. (2023) \"Adaptive-Consistency\" (EMNLP)\n  - Thirukovalluru et al. (2024) \"Atomic Self-Consistency\" (EMNLP)\n  - Farquhar et al. (2024) \"Semantic Entropy\" (Nature)\n- 为什么影响接收：这些遗漏使 Related Work 显得不完整。特别是 Chen et al. (2024) \"Two Failures\" 已经从 reasoning 角度分析了 SC 的 failure，不讨论它会让审稿人质疑 novelty claim。\n\n**N2** [critical] **核心因果 claim \"degeneracy causes selection failure\" 的支撑仍是相关性证据**\n- 具体位置：§4, §6.3, Figure 3\n- 问题：论文主 claim 是 degeneracy *导致* selection failure，但证据是 Spearman ρ 和 controlled splits。在 §7.3 cross-dataset contrast 中，\"degeneracy alone does not predict LP direction\"，又表明 degeneracy 不是唯一因素。这造成叙事内部张力。\n\n## Should-Fix 问题\n\n**W1** 与 Yun et al. (2025) \"The Price of Format: Diversity Collapse in LLMs\" 的差异化不够清晰。\n**W2** §8 Related Work 过于压缩（~0.5页），缺乏对 conformal prediction、SC code generation failure、entity-level hallucination detection 的覆盖。\n**W3** RE extension 作为 generalizability 证据说服力不足（单数据集单模型），但 abstract/intro scope claim \"structured information extraction\" 过宽。\n**W4** Entity-level construction +1.09pp 增益的 cost-benefit 未讨论（8x 推理开销换 ~1pp F1）。\n\n## 小问题\nM1. per-sample signal 定义 defer 到 Appendix 不当。M2. Figure 2 灰度可读性差。M3. Table 1 列缺解释。M4. §6.2 inverse scaling 机制解释不足。M5. Limitations 未提 closed-source API 的 degeneracy profile 差异。M6. 36 orphan bib entries。\n\n## Questions\nQ1. T>1.2 能否 recover diversity 改善 selection？\nQ2. 本文 failure mode 与 Chen et al. (2024) 的两种 failure 的关系？\nQ3. AUROC 0.63-0.88 无法转化为 selection gain，是否 bottleneck 在 aggregation？\nQ4. 是否考虑过 entity-level filtering（high-consistency select, low-consistency abstain）？\n\n## Missing References\n1. Chen et al. (2024) \"Two Failures of SC\" (TMLR)\n2. Chen et al. (2024) \"Universal SC\" (ICML Workshop)\n3. Aggarwal et al. (2023) \"Adaptive-Consistency\" (EMNLP)\n4. Thirukovalluru et al. (2024) \"Atomic SC\" (EMNLP)\n5. Farquhar et al. (2024) \"Semantic Entropy\" (Nature)\n6. PASC (2025) conformal prediction for IE pipelines\n7. \"Existing LLMs Are Not Self-Consistent For Simple Tasks\" (2025)\n8. Kuleshov & Liang (2015) \"Calibrated Structured Prediction\" (NeurIPS)\n\n---\n\n请对以上每个 Must-Fix (N1, N2)、Should-Fix (W1-W4)、Minor (M1-M6) 和 Questions (Q1-Q4) 逐条给出 [AGREE] 或 [REBUT] 回应。"
  }
}
```

</details>

---


### Tool result

_source line 2824 · 2026-05-21T04:43:25.023374+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 23084
}
```

</details>

---


### Tool call

_source line 2825 · 2026-05-21T04:43:25.225744+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "struct_self_consist_ie",
  "text": "## Step 2 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见\n\n以下是 Reviewer 1 的完整审稿意见。请逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n# Reviewer 1 — Round 1 审稿报告（方法严谨性）\n\n**Overall**: 3.5 — Borderline Conference\n**Soundness**: 3.5/5 | **Excitement**: 3/5 | **Reproducibility**: 4/5 | **Confidence**: 4/5\n\n**一句话总结**: 一篇方法论严谨、实验规模令人印象深刻的负面结果论文，系统揭示了 self-consistency 在结构化生成中的能力天花板，但范围局限于 NER + 2 个~8B 模型系列，部分核心推导的理论性被夸大，限制了结论的泛化性。\n\n## Must-Fix 问题（3 个）\n\n**N1** [critical] θ_crit = 0.70 推导本质是半经验的，但呈现为理论结果\n- §6.3, Appendix p.3 (p25), Figure 9\n- θ_crit 公式嵌入了 SciERC 经验参数（G_gap=14.8pp, ε=0.068），不是纯理论阈值。CoNLL（D=61.7%<0.70）上 LP 选择也失效的事实进一步说明该阈值非普适。\n- 建议：明确标注为 data-dependent 经验近似，增加敏感性分析。\n\n**N2** [critical] 种子数不对称影响统计效力均衡性\n- §7.1, Table 1-2\n- SciERC 3 seeds vs. 其他数据集 1 seed。Few-NERD（最强正面信号 +1.39pp）无法验证跨 seed 稳定性。核心负面结论在 3/4 数据集上依赖单次运行。\n- 建议：至少为 Few-NERD 补做 3-seed 实验。\n\n**N3** [critical] Cascade 四阶段的因果声称缺乏因果干预论证\n- §3-4, Figure 1\n- 流程箭头和 \"Why\" 标题暗示因果关系，但实际论证的是描述性诊断和相关性。无干预实验（如人工控制 degeneracy 水平）。\n- 建议：将 \"Why\" 改为 \"Where and How\"，明确声明 cascade 是诊断工具而非因果模型。\n\n## Should-Fix 问题（4 个）\n\n**W1** \"Escape routes\" 效果量过于边际（最大 +1.39pp），与标注噪声量级相当，实用价值存疑。\n**W2** 标题 \"Structured Generation\" 范围过宽——实验仅覆盖 NER + 1 个 exploratory RE。\n**W3** LODO transfer 分析不充分——未识别 transfer-critical 特征，\"introspection boundary\" 论证不完整。\n**W4** 缺少 NER-specific 或 structured MBR baseline 对比（如 Eikema et al. 2025 已引用未实验）。\n\n## 主要优势\n1. 实验规模和统计严谨性令人印象深刻（42页，50+ 表图，Holm-Bonferroni/bootstrap/permutation/TOST）\n2. Diagnostic cascade 框架设计优雅，有独立工具价值\n3. 诚实报告负面结果并提供 prescriptive protocol\n4. MBR 形式化为 entity construction 提供理论基础\n5. Degeneracy Decomposition 上界简洁有力\n\n## 引用检查\n81 bib entries, 45 cited, 36 orphan (uncited), 0 missing. 建议清理 orphan entries。\n\n---\n\n请对以上每个 Must-Fix (N1, N2, N3)、Should-Fix (W1-W4) 逐条给出 [AGREE] 或 [REBUT] 回应。如有不同看法，请 cite 论文具体位置作为证据。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "struct_self_consist_ie",
    "text": "## Step 2 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见\n\n以下是 Reviewer 1 的完整审稿意见。请逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n# Reviewer 1 — Round 1 审稿报告（方法严谨性）\n\n**Overall**: 3.5 — Borderline Conference\n**Soundness**: 3.5/5 | **Excitement**: 3/5 | **Reproducibility**: 4/5 | **Confidence**: 4/5\n\n**一句话总结**: 一篇方法论严谨、实验规模令人印象深刻的负面结果论文，系统揭示了 self-consistency 在结构化生成中的能力天花板，但范围局限于 NER + 2 个~8B 模型系列，部分核心推导的理论性被夸大，限制了结论的泛化性。\n\n## Must-Fix 问题（3 个）\n\n**N1** [critical] θ_crit = 0.70 推导本质是半经验的，但呈现为理论结果\n- §6.3, Appendix p.3 (p25), Figure 9\n- θ_crit 公式嵌入了 SciERC 经验参数（G_gap=14.8pp, ε=0.068），不是纯理论阈值。CoNLL（D=61.7%<0.70）上 LP 选择也失效的事实进一步说明该阈值非普适。\n- 建议：明确标注为 data-dependent 经验近似，增加敏感性分析。\n\n**N2** [critical] 种子数不对称影响统计效力均衡性\n- §7.1, Table 1-2\n- SciERC 3 seeds vs. 其他数据集 1 seed。Few-NERD（最强正面信号 +1.39pp）无法验证跨 seed 稳定性。核心负面结论在 3/4 数据集上依赖单次运行。\n- 建议：至少为 Few-NERD 补做 3-seed 实验。\n\n**N3** [critical] Cascade 四阶段的因果声称缺乏因果干预论证\n- §3-4, Figure 1\n- 流程箭头和 \"Why\" 标题暗示因果关系，但实际论证的是描述性诊断和相关性。无干预实验（如人工控制 degeneracy 水平）。\n- 建议：将 \"Why\" 改为 \"Where and How\"，明确声明 cascade 是诊断工具而非因果模型。\n\n## Should-Fix 问题（4 个）\n\n**W1** \"Escape routes\" 效果量过于边际（最大 +1.39pp），与标注噪声量级相当，实用价值存疑。\n**W2** 标题 \"Structured Generation\" 范围过宽——实验仅覆盖 NER + 1 个 exploratory RE。\n**W3** LODO transfer 分析不充分——未识别 transfer-critical 特征，\"introspection boundary\" 论证不完整。\n**W4** 缺少 NER-specific 或 structured MBR baseline 对比（如 Eikema et al. 2025 已引用未实验）。\n\n## 主要优势\n1. 实验规模和统计严谨性令人印象深刻（42页，50+ 表图，Holm-Bonferroni/bootstrap/permutation/TOST）\n2. Diagnostic cascade 框架设计优雅，有独立工具价值\n3. 诚实报告负面结果并提供 prescriptive protocol\n4. MBR 形式化为 entity construction 提供理论基础\n5. Degeneracy Decomposition 上界简洁有力\n\n## 引用检查\n81 bib entries, 45 cited, 36 orphan (uncited), 0 missing. 建议清理 orphan entries。\n\n---\n\n请对以上每个 Must-Fix (N1, N2, N3)、Should-Fix (W1-W4) 逐条给出 [AGREE] 或 [REBUT] 回应。如有不同看法，请 cite 论文具体位置作为证据。"
  }
}
```

</details>

---


### Tool result

_source line 2826 · 2026-05-21T04:43:26.971586+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1745
}
```

</details>

---


### Tool call

_source line 2827 · 2026-05-21T04:43:35.020459+00:00_

called ScheduleWakeup

<details open><summary>🔧 Tool call — ScheduleWakeup</summary>

```json
{
  "delaySeconds": "270",
  "reason": "等待 Reviewer 1 和 Reviewer 2 完成交叉回应（约 4-5 分钟）",
  "prompt": "系统通知：审稿审批已通过。请开始审稿。\n\n[论文提交]\n- 项目: struct_self_consist_ie\n- 论文路径: projects/struct_self_consist_ie/docs/paper/main.tex\n- 目标 venue: EMNLP 2026\n- 投稿类别: Main Conference (Long Paper)\n- 截止日期: 2026-05-25\n\n请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ScheduleWakeup",
  "tool_args": {
    "delaySeconds": "270",
    "reason": "等待 Reviewer 1 和 Reviewer 2 完成交叉回应（约 4-5 分钟）",
    "prompt": "系统通知：审稿审批已通过。请开始审稿。\n\n[论文提交]\n- 项目: struct_self_consist_ie\n- 论文路径: projects/struct_self_consist_ie/docs/paper/main.tex\n- 目标 venue: EMNLP 2026\n- 投稿类别: Main Conference (Long Paper)\n- 截止日期: 2026-05-25\n\n请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。"
  }
}
```

</details>

---


### Tool result

_source line 2828 · 2026-05-21T04:43:35.020858+00:00_

Next wakeup scheduled for 04:48:00 (in 265s).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ScheduleWakeup",
  "elapsed_ms": 0
}
```

</details>

---


### Assistant

_source line 2829 · 2026-05-21T04:43:37.116122+00:00_

交叉分享已发出，等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 214

## Round 214

2 recorded events


### User

_source line 2830 · 2026-05-21T04:43:39.792099+00:00_

[Reviewer 2 审稿结果]:
Round 1 审稿报告已提交给 Review Director。

**审稿摘要：**

- **Overall: 3.5 (Borderline Conference)**
- **Soundness: 3.5/5** — 实验设计严谨（4 数据集、2 模型、统计检验完备），但 degeneracy→selection failure 的因果 claim 仍停留在相关性证据层面
- **Excitement: 3/5** — 对 practitioner 有 actionable value，但核心 insight（degeneracy 导致 SC 失效）与 Yun et al. (2025) diversity collapse 发现高度重叠

**两个 Must-Fix 问题：**
1. Related Work 缺口严重——5 篇直接相关的论文（Chen "Two Failures"、USC、Adaptive-Consistency、Atomic SC、Semantic Entropy）存在于 .bib 但未被引用
2. 核心因果 claim 的支撑不够（§4 说 degeneracy 是 dominant factor，§7.3 又说 degeneracy alone does not predict LP direction）

**四个 Should-Fix：** 与 Yun et al. 差异化不清晰、§8 过于压缩、RE 扩展不足以支撑 "IE" scope claim、escape routes 缺少 cost-benefit 分析。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 2831 · 2026-05-21T04:43:45.637123+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 215

## Round 215

2 recorded events


### User

_source line 2832 · 2026-05-21T04:45:46.003895+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 交叉回应 — 对 Reviewer 1 (Round 1) 的逐条回应

---

## Must-Fix 问题

### [AGREE] R1-N1: θ_crit = 0.70 推导本质是半经验的，但呈现为理论结果

同意。我在阅读 §6.3 和 Appendix p.3（page 25, Corollary 1）时也注意到这个问题。θ_crit 的推导依赖于 G_gap = 14.8pp 和 ε = 0.068 这两个 SciERC 特定的经验参数，而 Corollary 1 的表述（"the degeneracy rate must satisfy D < 1 − γ/(G_gap · n)"）虽然形式上是一个一般性命题，但实际 plugging in 的数值完全来自单个数据集。更关键的是，R1 指出 CoNLL（D=61.7% < 0.70）上 LP 选择同样失效——这直接动摇了 0.70 作为"通用阈值"的地位。

补充一个我自己的观察：Figure 9（page 26）的可视化中 signal-adjusted bound（红线，ε=0.068）和 κ_eff = 0.70 的水平线都是从 SciERC 数据 fit 出来的，但图标题未明确标注这是 data-specific 的。这会误导读者将其理解为 general-purpose 阈值。

R1 的建议（标注为 data-dependent 经验近似 + 敏感性分析）恰当。我进一步建议：如果要保留 θ_crit，至少应在 CoNLL 和 Few-NERD 上各自估算其 dataset-specific θ_crit 值，展示阈值在不同数据分布下的变异范围。

---

### [AGREE] R1-N2: 种子数不对称影响统计效力均衡性

同意，但我认为严重程度略低于 R1 的评估。

R1 正确指出了核心问题：SciERC 用 3 seeds 而 Few-NERD/CoNLL 部分结果依赖 1 seed（Table 3 caption 明确写了 "Few-NERD/CoNLL: 1 seed means"）。这确实造成了不对称——SciERC 的负面结论（SC 失效）有 3-seed 支撑，而 Few-NERD 的正面结论（LP selection +1.39pp，§7.2）仅基于单次运行。

但我要指出几个缓解因素：
1. Appendix 中 Table 11（page 17）标注为 "3-seed mean" 覆盖所有配置，说明 3-seed 数据在附录层面是存在的，只是主文表格选择性地报告了 1-seed 结果。
2. Few-NERD 的 bootstrap confidence intervals（Table 4a, page 7）为 LP gain 提供了单次运行内的统计估计，部分缓解了 cross-seed 不确定性。
3. Table 20（Appendix j, page 21）报告了 multi-seed stability 分析，显示 signal rankings 在 3 seeds 下一致。

尽管如此，R1 要求至少为 Few-NERD 补做 3-seed 实验的建议合理——这是强化 positive signal 可信度的必要步骤。

---

### [AGREE] R1-N3: Cascade 四阶段的因果声称缺乏因果干预论证

强烈同意。这与我自己的 N2（"核心因果 claim 'degeneracy causes selection failure' 的支撑仍是相关性证据"）完全一致。

R1 精确地识别了问题所在：§3 标题 "Why Self-Verification Fails" 和 §4 标题 "Why Single-Signal Selection Fails" 使用了因果语言（"Why"），Figure 1 的箭头流（Quality Estimation → Sample Selection → Entity-Level Construction）暗示了因果链条，但论文提供的全部是：
- Spearman ρ 相关系数（§4, Figure 2）
- Subgroup 对比（high-degeneracy vs. low-degeneracy splits, Figure 3）
- AUROC 区分力（Table 1）

这些都是 **描述性/相关性证据**，不是因果干预。论文自身在 §7.3 承认 "degeneracy alone does not predict LP direction"（page 7），这与 §4 的因果叙事存在内部矛盾。

R1 建议将 "Why" 改为 "Where and How" 是精准的修改建议。我补充：§4 的 "definitional vs. empirical" 分解（page 4, "The first layer is structural... The second layer is empirical"）本身是一个好的框架，但需要更诚实地承认 empirical layer 只建立了 association。

---

## Should-Fix 问题

### [AGREE] R1-W1: "Escape routes" 效果量过于边际

部分同意。最大增益 +1.39pp（Few-NERD LP selection, Table 3）和 entity construction 的 +1.09pp（Few-NERD, Table 5）确实在绝对值上有限。这也是我在 W4 中提出的 cost-benefit 问题——N=8 样本意味着 8 倍推理开销，换取 ~1pp F1 回报。

但我要给出一个 partial rebut：对于 negative result 论文而言，escape routes 的效果量不需要很大。论文的核心贡献是 *诊断*（为什么 SC 不 work），prescriptive protocol 是附加价值。如果 escape routes 效果惊人，那论文的 narrative 反而不一致（"SC 失败" 但 "我们又让它成功了"）。从这个角度看，边际的 escape routes 恰恰强化了 negative result 的结论。

R1 提出与标注噪声量级相当的观察值得考虑，但论文确实做了 permutation tests 来排除 chance-level 解释（§7.5, Appendix f），所以统计上 gain 是 real 的，只是实用意义有限。

---

### [AGREE] R1-W2: 标题 "Structured Generation" 范围过宽

同意。这与我的 W3 一致——论文实验仅覆盖 NER（4 datasets）+ 1 个 exploratory RE extension（SciERC RE, Appendix o, page 24），但标题声称 "Structured Generation"，abstract 说 "structured information extraction"。

"Structured Generation" 在 NLP 社区通常涵盖 code generation、SQL、JSON schema、table generation 等更广泛的场景。论文的结论（degeneracy 导致 SC 失败）是否泛化到这些场景完全未知。标题应缩窄为 "Named Entity Recognition" 或至少 "Structured Information Extraction"。

---

### [REBUT] R1-W3: LODO transfer 分析不充分

部分不同意。R1 认为 LODO 分析未识别 transfer-critical 特征且 "introspection boundary" 论证不完整，但我认为论文在有限篇幅内对此做了合理处理。

具体证据：
1. §4（page 4-5）报告了 LODO AUROC 从 single-dataset 的 0.82 降至 0.550，这本身就是一个信息量丰富的负面结果——它说明 quality signals 是 dataset-specific 的，而非 universal。
2. §9 Discussion（page 8）中 "introspection boundary" 的讨论虽然简短，但结合 §3 的 hidden-state probe 结果（AUROC 0.63-0.88 at entity-level 但无法 translate 到 selection gain），逻辑链条是完整的：即使 latent 信号存在，operationalization 为 selection gain 仍然失败。
3. Appendix h.3（page 21）的 hidden-state probe 分析补充了 cross-dataset 的 asymmetry 细节。

R1 要求识别 "transfer-critical 特征" 属于额外贡献要求（ARR guideline H13: 要求超出 claim 支撑范围的实验）。论文的 claim 不是 "我们能做好 transfer"，而是 "transfer 失败，证明 signals 是 dataset-specific 的"。

---

### [AGREE] R1-W4: 缺少 structured MBR baseline 对比

同意。论文在 §6.1 和 Appendix p.2（page 24-25）将 entity construction 形式化为 entity-level MBR decoding，引用了 Eikema et al. (2025) "Structure-Conditional MBR Decoding" 但未实验对比。既然论文声称 entity construction 是 MBR 的特例（Proposition 1, page 24），那么至少应该：

1. 实现 standard MBR with token-level F1 utility 作为 baseline（概念上并不复杂，论文自己在 Appendix p.2 给出了 formulation）
2. 或者对比不同 utility function 下的 MBR 表现（set-overlap vs. exact match vs. relaxed overlap）

这不仅是方法论完整性的要求，也是验证 Proposition 1 实际有效性的必要步骤。如果 standard MBR 比简单的 entity-level majority vote 表现更好，那论文的 prescriptive protocol 就需要修改。

---

## 总结

R1 的审稿报告质量很高，识别的问题与我的审查有大量重叠（因果 claim、scope overclaim、escape routes 边际性、引用问题）。我与 R1 在 7 条意见中的 6 条上达成一致，仅对 W3（LODO 分析）持不同看法。两位 reviewer 的共识问题集中在：

1. **因果语言与相关性证据的不匹配**（R1-N3 ≈ R2-N2）— 最需要修改
2. **Scope overclaim**（R1-W2 ≈ R2-W3）— 标题和 abstract 需缩窄
3. **Related Work 缺口**（R2-N1）— R1 未特别提及，但 36 orphan bib entries 问题两人都注意到

综合两份审稿，我维持 **Overall 3.5 (Borderline Conference)** 的评分。如果上述 Must-Fix 问题（因果语言修正、θ_crit 标注为经验值、seed 补充）得到解决，论文有潜力达到 Findings 水平。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 2833 · 2026-05-21T04:45:50.306871+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 216

## Round 216

16 recorded events


### User

_source line 2834 · 2026-05-21T04:45:55.557455+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 对 Reviewer 2 的交叉回应

### Must-Fix
- **[AGREE] R2-N1 (Related Work 引用缺口)**: 完全同意。36 orphan bib entries 中至少 5 篇高度相关论文（尤其 Chen et al. 2024 "Two Failures of SC"）未引用是严重遗漏。§8 仅 0.5 页，建议扩充至 ~1 页。
- **[AGREE] R2-N2 (因果 claim 支撑不足)**: 完全同意，与我的 N3 高度重合。补充发现：CoNLL D=61.7%（低于 θ_crit=0.70）但 LP 仍失效，说明 degeneracy 和 LP discriminative power 可能是并行独立约束而非 cascade 所暗示的序列关系。

### Should-Fix
- **[AGREE] R2-W1**: Yun et al. (2025) 差异化不够。
- **[AGREE] R2-W2**: Related Work 过于压缩。
- **[AGREE] R2-W3**: RE extension 不足以支撑 "structured generation" scope claim，与我的 W2 一致。
- **[REBUT] R2-W4 (cost-benefit 未讨论)**: 部分反驳。Entity construction 是 post-hoc aggregation，不需额外推理调用——边际成本为零（已有 N 个样本时）。但同意缺乏显式 cost-efficiency 分析框架。

### Minor
- M1 [AGREE], M2 [AGREE], M3 [REBUT: Table 列标签在 §2.2 已定义，常规做法], M4 [AGREE], M5 [AGREE], M6 [AGREE]

### Questions
- Q1 [AGREE]: T>1.2 未测试，是有价值的诊断方向。
- Q2 [AGREE]: 与 Chen et al. (2024) 的关系是 must-address。
- Q3 [REBUT]: AUROC→selection gap 瓶颈不在 aggregation，论文已解释为 degeneracy 限制了可优化空间（§3-4）。但建议增加显式说明。
- Q4 [AGREE]: Entity-level abstention 是有意义的未探索方向，可能绕过 sample-level degeneracy 限制。

### R1/R2 共识
两位 Reviewer 在以下核心问题上完全一致：
1. **因果声称过强**（R1-N3 = R2-N2）
2. **Scope claim 过宽**（R1-W2 = R2-W3）
3. **Related Work 不足**（R2-N1, R2-W2）
4. **效果量边际**（R1-W1 ≈ R2-W4）

总体判断维持 **3.5 Borderline Conference**。论文实验质量出色但需要在因果措辞、Related Work 覆盖、和 scope 限定上做实质性修改。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 2835 · 2026-05-21T04:46:14.481701+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 2836 · 2026-05-21T04:46:14.938546+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"pending\", \"paper_pdf_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf\", \"venue\": \"EMNLP 2026\", \"requested_at\": \"2026-05-21T04:34:28.851184+00:00\", \"reminder_hours\": 8, \"chat_id\": \"oc_1b56445332d8ca2b4964b30f300f0e00\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 456
}
```

</details>

---


### Tool call

_source line 2837 · 2026-05-21T04:46:15.091699+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 2838 · 2026-05-21T04:46:16.748107+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-21T04:34:27.970869+00:00\", \"completed_at\": \"2026-05-21T04:39:28.175966+00:00\", \"findings\": [{\"severity\": \"info\", \"dimension\": \"agent_error\", \"message\": \"[ERROR] Agent timed out after 300s\"}], \"counts\": {\"critical\": 0, \"warning\": 0, \"info\": 1}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 1656
}
```

</details>

---


### Tool call

_source line 2839 · 2026-05-21T04:46:16.899111+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml 2>/dev/null | grep -E \"^  - id:|status:|summary:\" | head -60",
  "description": "Read current review issues tracker structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml 2>/dev/null | grep -E \"^  - id:|status:|summary:\" | head -60",
    "description": "Read current review issues tracker structure"
  }
}
```

</details>

---


### Tool result

_source line 2840 · 2026-05-21T04:46:18.608248+00:00_

  - id: "R1-W1"
    summary: "Few-NERD 3-epoch vs SciERC 5-epoch 训练时长混淆效应"
    status: resolved
  - id: "R1-W2"
    summary: "\"Two jointly necessary conditions\" 因果性表述过强"
    status: resolved
  - id: "R2-N1-old"
    summary: "Contribution 1 'methodological premise' 是定义推论"
    status: resolved
  - id: "R2-N2-old"
    summary: "与 MBR 文献差异化定位不够锐利"
    status: resolved
  - id: "R2-N4-old"
    summary: "模型规模 3B-8B，70B+ 未知"
    status: resolved
  - id: "R1-W3-old"
    summary: "2-seed 统计效力不足"
    status: resolved
  - id: "R1-W4-old"
    summary: "Per-entity-type non-independence"
    status: resolved
  - id: "R1-W5-old"
    summary: "\"Supervised verifier\" framing 误导"
    status: resolved
  - id: "R1-W6"
    summary: "Degeneracy 定义需区分"
    status: resolved
  - id: "R1-W7"
    summary: "SciERC greedy F1 不一致"
    status: resolved
  - id: "R2-W1-old"
    summary: "Abstract 数字过载"
    status: resolved
  - id: "R2-W2-old"
    summary: "Actionable contribution 偏薄"
    status: resolved
  - id: "R2-W3-old"
    summary: "Discussion 过于碎片化"
    status: resolved
  - id: "R2-W5-old"
    summary: "核心数字跨 section 重复"
    status: resolved
  - id: "R2-W4-baseline"
    summary: "缺少 baseline signals"
    status: resolved
  - id: "R2-W4-re"
    summary: "RE extension preliminary 但引用频繁"
    status: resolved
  - id: "R1-MR1"
    summary: "缺失引用: Geifman & El-Yaniv 2017, XGrammar 等"
    status: resolved
  - id: "R19-I8"
    summary: "Table 3 EM/VC 缺 p-values"
    status: resolved
  - id: "R19-I9"
    summary: "Per-type LP selection 异质性"
    status: resolved
  - id: "R19-DATA1"
    summary: "LLaMA CoNLL degeneracy 86.4% vs 89.2%"
    status: resolved

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "elapsed_ms": 1709
}
```

</details>

---


### Tool call

_source line 2841 · 2026-05-21T04:46:30.738088+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml",
  "description": "Read full review issues YAML for update",
  "timeout": "10000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml",
    "description": "Read full review issues YAML for update",
    "timeout": "10000"
  }
}
```

</details>

---


### Tool result

_source line 2842 · 2026-05-21T04:46:30.789184+00:00_

&lt;persisted-output>
Output too large (36.3KB). Full output saved to: /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-director-0161122b/f7203b3b-983c-4259-a341-4288c8b137b9/tool-results/btbcluqp9.txt

Preview (first 2KB):
issues:
  # ===== 历史 resolved issues (保留，省略细节) =====
  - id: "R1-W1"
    summary: "Few-NERD 3-epoch vs SciERC 5-epoch 训练时长混淆效应"
    category: experiment
    severity: critical
    status: resolved
    first_raised_round: 1
    last_seen_round: 19
    resolution: "Reviewer PASS: 脚注+§4.1+appendix epoch data 一致。tab:epoch_confound caption 已注明 5K subsample。"
    resolution_round: 19

  - id: "R1-W2"
    summary: "\"Two jointly necessary conditions\" 因果性表述过强"
    category: framing
    severity: critical
    status: resolved
    first_raised_round: 1
    last_seen_round: 21
    resolution: "全文降级为 empirical pattern/factors。Reviewer 确认正文+appendix 15处+4处残留全部修复，0 因果语言残留。"
    resolution_round: 21

  - id: "R2-N1-old"
    summary: "Contribution 1 'methodological premise' 是定义推论"
    category: framing
    severity: critical
    status: resolved
    first_raised_round: 1
    last_seen_round: 19
    resolution: "Reviewer PASS: 标题改为 'Quality estimation framework'; Abstract 干净。"
    resolution_round: 19

  - id: "R2-N2-old"
    summary: "与 MBR 文献差异化定位不够锐利"
    category: framing
    severity: warning
    status: resolved
    first_raised_round: 1
    last_seen_round: 19
    resolution: "Reviewer PASS: Introduction 区分清晰，ρ=0.52 数据一致。"
    resolution_round: 19

  - id: "R2-N4-old"
    summary: "模型规模 3B-8B，70B+ 未知"
    category: experiment
    severity: info
    status: resolved
    first_raised_round: 1
    last_seen_round: 19
    resolution: "Round 20 检查 PASS: limitations.tex '4B-8B scale; 70B+ untested'。"
    resolution_round: 19

  - id: "R1-W3-old"
    summary: "2-seed 统计效力不足"
    category: experiment
    severity: warning
    status: resolved
    first_raised_round: 1
    
…[truncated 332 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 2843 · 2026-05-21T04:46:35.503562+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-director-0161122b/f7203b3b-983c-4259-a341-4288c8b137b9/tool-results/btbcluqp9.txt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-director-0161122b/f7203b3b-983c-4259-a341-4288c8b137b9/tool-results/btbcluqp9.txt"
  }
}
```

</details>

---


### Tool result

_source line 2844 · 2026-05-21T04:46:35.757004+00:00_

1	issues:
2	  # ===== 历史 resolved issues (保留，省略细节) =====
3	  - id: "R1-W1"
4	    summary: "Few-NERD 3-epoch vs SciERC 5-epoch 训练时长混淆效应"
5	    category: experiment
6	    severity: critical
7	    status: resolved
8	    first_raised_round: 1
9	    last_seen_round: 19
10	    resolution: "Reviewer PASS: 脚注+§4.1+appendix epoch data 一致。tab:epoch_confound caption 已注明 5K subsample。"
11	    resolution_round: 19
12	
13	  - id: "R1-W2"
14	    summary: "\"Two jointly necessary conditions\" 因果性表述过强"
15	    category: framing
16	    severity: critical
17	    status: resolved
18	    first_raised_round: 1
19	    last_seen_round: 21
20	    resolution: "全文降级为 empirical pattern/factors。Reviewer 确认正文+appendix 15处+4处残留全部修复，0 因果语言残留。"
21	    resolution_round: 21
22	
23	  - id: "R2-N1-old"
24	    summary: "Contribution 1 'methodological premise' 是定义推论"
25	    category: framing
26	    severity: critical
27	    status: resolved
28	    first_raised_round: 1
29	    last_seen_round: 19
30	    resolution: "Reviewer PASS: 标题改为 'Quality estimation framework'; Abstract 干净。"
31	    resolution_round: 19
32	
33	  - id: "R2-N2-old"
34	    summary: "与 MBR 文献差异化定位不够锐利"
35	    category: framing
36	    severity: warning
37	    status: resolved
38	    first_raised_round: 1
39	    last_seen_round: 19
40	    resolution: "Reviewer PASS: Introduction 区分清晰，ρ=0.52 数据一致。"
41	    resolution_round: 19
42	
43	  - id: "R2-N4-old"
44	    summary: "模型规模 3B-8B，70B+ 未知"
45	    category: experiment
46	    severity: info
47	    status: resolved
48	    first_raised_round: 1
49	    last_seen_round: 19
50	    resolution: "Round 20 检查 PASS: limitations.tex '4B-8B scale; 70B+ untested'。"
51	    resolution_round: 19
52	
53	  - id: "R1-W3-old"
54	    summary: "2-seed 统计效力不足"
55	    category: experiment
56	    severity: warning
57	    status: resolved
58	    first_raised_round: 1
59	    last_seen_round: 19
60	    resolution: "Reviewer PASS: tab:fewnerd 脚注 '3-seed mean: +0.04±0.48pp'。"
61	    resolution_round: 19
62	
63	  - id: "R1-W
…[truncated 35072 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 253
}
```

</details>

---
