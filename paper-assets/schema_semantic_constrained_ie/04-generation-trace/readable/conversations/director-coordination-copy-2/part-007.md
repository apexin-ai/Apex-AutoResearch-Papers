# Director coordination — Part 7 of 8

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Conversation logs

[← Part 6](part-006.md) · [Transcript overview](../director-coordination-copy-2.md) · [Part 8 →](part-008.md) · [Structured JSON](../../../sessions/eb/ebac95f2406b6d6dc37e.json)

## Round 157

### Tool call

_source line 2157 · 2026-05-23T02:54:09.501344+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "schema_semantic_constrained_ie",
  "text": "以下是 Reviewer 2 的完整审稿意见。请逐条回应：对每条 Strength/Weakness/Question，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 审稿意见（完整原文）\n\n**审查侧重**: 新颖性 + Related Work 完整性 + 写作质量\n\n### Summary\n本文提出 OntoCoDec，一个将 IE 本体编译为可组合 token 级解码约束的两层框架：grammar layer（CFG，保证 JSON 结构和词汇约束）+ semantic layer（有状态的实体注册表，运行时执行 domain/range 类型检查）。Proposition 1 提供了形式化动机（domain/range 约束非 context-free），实验覆盖 3 个数据集、3 个 8B 模型 + 70B 验证，展示近乎完全的 DR 消除（<0.1%）。论文的分析深度（组合性分析、CF↔DR trade-off 刻画、beam search 探索）令人印象深刻，但核心技术机制（实体注册表 + domain/range 查表）相对直接，且 Abstract 中对 CF 副作用的呈现有选择性偏差。\n\n### Strengths\n**S1.** 形式化分解动机清晰且有价值。Proposition 1（§3, p.3）证明了 domain/range 约束对无界实体集不是 context-free 的，为什么需要 grammar 之上的第二层提供了严谨的理论基础。\n**S2.** 实验评估极为全面。3 个 RE 数据集、3 个 8B 模型 + 70B 验证、zero-shot 与 fine-tuning、5-way ablation、composability 分析、beam search 兼容性、runtime profiling、error taxonomy。\n**S3.** 组合性分析框架有独立价值。双因素定量分析（Figure 2, Appendix D）揭示了 schema tightness (κ̄) 与 DR reduction 的关系，R² = 0.886。\n**S4.** CF↔DR trade-off 的诚实刻画（主要在 Limitations 和 Appendix C）。\n**S5.** 实用性强：无需约束专属训练，从 IE 本体自动编译。\n\n### Weaknesses\n**W1. [Major]** Abstract 对 CF 副作用的呈现存在选择性偏差——报告 \"up to 1.18% under greedy decoding on well-calibrated models\"，但实际范围达 12.02%（Table 1, Limitations）。\n**W2. [Major]** 核心技术新颖性有限——grammar layer 等价于 GCD/BoostCD，semantic layer 本质上是运行时查表。Proposition 1 被自身 Remark 削弱（实际语言是 regular 的，只是 DFA 规模太大）。论文自述 \"systematic engineering contribution with theoretical grounding\" 指出了 novelty ceiling。\n**W3. [Minor]** Abstract 信息密度过高——~150 词中 12+ 数字/百分比，5+ 首次出现缩写。\n**W4. [Minor]** Introduction 中 \"42-99%\" 与 Abstract 中 \"42-90%\" 范围不一致。\n**W5. [Minor]** Proposition 1 的实际意义被 Remark 削弱——理论 barrier 实际是工程可行性问题。\n**W6. [Minor]** WikiEvents 实验过于初步（n=20, zero-shot F1=1.00），但仍列入 contribution。\n\n### Questions\n**Q1.** Beam search 中每个 beam 维护独立 registry 还是共享？k=8 时内存开销？\n**Q2.** 为什么不将 TCR 整合到解码循环中？是否涉及 NP-hardness？\n**Q3.** 是否直接运行过 GCD/BoostCD 作为 baseline？\n**Q4.** κ̄ 与 DR reduction 的 R²=0.886 基于 n=6 是否有 leave-one-out 验证？\n\n### Missing References\n1. Text2Event (Lu et al., 2021, ACL)\n2. DEGREE (Hsu et al., 2022, NAACL)\n3. DCCD (2026) 和 pldi2025_type_constrained_codegen 的 venue/年份需核实\n\n### Overall Assessment\n**3.5 — Borderline Conference**。执行质量很高但方法创新有限，处于 Conference 和 Findings 的交界。\n\n---\n\n请逐条回应上述所有 Strengths、Weaknesses、Questions 和 Missing References。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "schema_semantic_constrained_ie",
    "text": "以下是 Reviewer 2 的完整审稿意见。请逐条回应：对每条 Strength/Weakness/Question，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 审稿意见（完整原文）\n\n**审查侧重**: 新颖性 + Related Work 完整性 + 写作质量\n\n### Summary\n本文提出 OntoCoDec，一个将 IE 本体编译为可组合 token 级解码约束的两层框架：grammar layer（CFG，保证 JSON 结构和词汇约束）+ semantic layer（有状态的实体注册表，运行时执行 domain/range 类型检查）。Proposition 1 提供了形式化动机（domain/range 约束非 context-free），实验覆盖 3 个数据集、3 个 8B 模型 + 70B 验证，展示近乎完全的 DR 消除（<0.1%）。论文的分析深度（组合性分析、CF↔DR trade-off 刻画、beam search 探索）令人印象深刻，但核心技术机制（实体注册表 + domain/range 查表）相对直接，且 Abstract 中对 CF 副作用的呈现有选择性偏差。\n\n### Strengths\n**S1.** 形式化分解动机清晰且有价值。Proposition 1（§3, p.3）证明了 domain/range 约束对无界实体集不是 context-free 的，为什么需要 grammar 之上的第二层提供了严谨的理论基础。\n**S2.** 实验评估极为全面。3 个 RE 数据集、3 个 8B 模型 + 70B 验证、zero-shot 与 fine-tuning、5-way ablation、composability 分析、beam search 兼容性、runtime profiling、error taxonomy。\n**S3.** 组合性分析框架有独立价值。双因素定量分析（Figure 2, Appendix D）揭示了 schema tightness (κ̄) 与 DR reduction 的关系，R² = 0.886。\n**S4.** CF↔DR trade-off 的诚实刻画（主要在 Limitations 和 Appendix C）。\n**S5.** 实用性强：无需约束专属训练，从 IE 本体自动编译。\n\n### Weaknesses\n**W1. [Major]** Abstract 对 CF 副作用的呈现存在选择性偏差——报告 \"up to 1.18% under greedy decoding on well-calibrated models\"，但实际范围达 12.02%（Table 1, Limitations）。\n**W2. [Major]** 核心技术新颖性有限——grammar layer 等价于 GCD/BoostCD，semantic layer 本质上是运行时查表。Proposition 1 被自身 Remark 削弱（实际语言是 regular 的，只是 DFA 规模太大）。论文自述 \"systematic engineering contribution with theoretical grounding\" 指出了 novelty ceiling。\n**W3. [Minor]** Abstract 信息密度过高——~150 词中 12+ 数字/百分比，5+ 首次出现缩写。\n**W4. [Minor]** Introduction 中 \"42-99%\" 与 Abstract 中 \"42-90%\" 范围不一致。\n**W5. [Minor]** Proposition 1 的实际意义被 Remark 削弱——理论 barrier 实际是工程可行性问题。\n**W6. [Minor]** WikiEvents 实验过于初步（n=20, zero-shot F1=1.00），但仍列入 contribution。\n\n### Questions\n**Q1.** Beam search 中每个 beam 维护独立 registry 还是共享？k=8 时内存开销？\n**Q2.** 为什么不将 TCR 整合到解码循环中？是否涉及 NP-hardness？\n**Q3.** 是否直接运行过 GCD/BoostCD 作为 baseline？\n**Q4.** κ̄ 与 DR reduction 的 R²=0.886 基于 n=6 是否有 leave-one-out 验证？\n\n### Missing References\n1. Text2Event (Lu et al., 2021, ACL)\n2. DEGREE (Hsu et al., 2022, NAACL)\n3. DCCD (2026) 和 pldi2025_type_constrained_codegen 的 venue/年份需核实\n\n### Overall Assessment\n**3.5 — Borderline Conference**。执行质量很高但方法创新有限，处于 Conference 和 Findings 的交界。\n\n---\n\n请逐条回应上述所有 Strengths、Weaknesses、Questions 和 Missing References。"
  }
}
```

</details>

---


### Tool result

_source line 2158 · 2026-05-23T02:54:37.178014+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 27676
}
```

</details>

---


### Tool call

_source line 2159 · 2026-05-23T02:54:37.329148+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "schema_semantic_constrained_ie",
  "text": "以下是 Reviewer 1 的完整审稿意见。请逐条回应：对每条 Strength/Weakness/Question，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 审稿意见（完整原文）\n\n**审查侧重**: 方法严谨性 + 实验设计 + 统计检验\n\n### Overall: 3.5 — Borderline Conference\n理论贡献扎实（Proposition 1 + 组合框架）、评估规模罕见地全面（47+ tables），但核心消融的统计检验缺失、F1 实际提升在 Bonferroni 校正后不显著、full fine-tuning 组合性失效未得到充分分析。\n\n### Strengths\n**S1** 理论基础严谨。Proposition 1 使用泵引理正式证明 domain/range 约束不是上下文无关的，Appendix O 证明完整。\n**S2** 约束组合框架设计精巧。§4 Eq. 2 的非对称合取配合 grammar-first fallback 是优雅的工程决策。\n**S3** 评估规模罕见。38 页 47+ 表格。\n**S4** 诊断指标体系设计良好（DR/CF/RoV/ET/RV）。\n**S5** Fine-tuning 统计报告有亮点——Bonferroni 校正 + 诚实报告 R-F1 不显著。\n**S6** 双因子定量分析（κ × baseline violation）有实践指导价值。\n**S7** 错误分析深入且诚实（Appendix J/K/N）。\n\n### Must-Fix（Critical）\n**N1** Zero-shot 核心消融（Table 1）缺乏置信区间和显著性检验。核心主张（grammar 3% vs semantic 24% vs 组合 94% DR reduction）没有统计证据支撑。Appendix G Table 8 仅覆盖 fine-tuning，Table 31 仅提供通用精度估计。建议：为 Table 1 提供 bootstrap CI + 配对检验 + Bonferroni 校正。\n\n**N2** Full fine-tuning 组合性失效未充分分析。Table 42 显示 full FT + S1 的 R-F1（37.89）与 unconstrained 完全相同。如果 full FT 已内化约束，这对 \"decoding-time enforcement is necessary\" 的动机叙事构成反证。建议：报告 full FT unconstrained 的 violation rates，分析原因，限定 composability claim 为 \"parameter-efficient fine-tuning\"。\n\n### Should-Fix（Major/Minor）\n**W1 [Major]** WikiEvents n=20 统计效力不足，CI ±3.0pp，argument F1 shift ±1.1pp 落在 CI 内。\n**W2 [Major]** 70B AWQ INT4 量化混淆因素未控制。\n**W3 [Major]** 缺乏与 training-based 方法（GoLLIE/KnowCoder/ADELIE）的正面 violation rate 对比。\n**W4 [Minor]** Enabling dependency \"empirical enabling dependency\" 术语强度与 n=6 证据基础不匹配。\n**W5 [Minor]** Proposition 1 证明的 position→name indexing 简化论证不够严格。\n\n### 小问题\n- Table 1 caption \"b = beam\" 定义位置不当\n- §3.3 prefix map 正确性未形式化\n- Figure 1 未可视化 grammar-first fallback 路径\n- DocRED dev set 评估应在 Limitations 中提及\n\n### Questions\n**Q1**: 能否为 Table 1 提供 bootstrap CI + Bonferroni 校正？\n**Q2**: AWQ INT4 对约束执行精度的影响？\n**Q3**: Full FT unconstrained 的 violation rates 是多少？\n**Q4**: Table 2 Llama S1 SciERC DR=0% 是否所有种子成立？\n**Q5**: TCR vs OntoCoDec 在 F1 上的对比？TCR 是否是更实用的替代？\n**Q6**: Schema ambiguity σ 值能否提供定量阈值？\n\n### Missing References\n- Huang et al. (2024) \"Planning for Constrained LLM Generation\"\n- PICARD 约束粒度差异讨论\n\n### Overall: 3.5 — Borderline Conference\n\n---\n\n请逐条回应上述所有 Strengths、Must-Fix、Should-Fix、小问题、Questions 和 Missing References。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "schema_semantic_constrained_ie",
    "text": "以下是 Reviewer 1 的完整审稿意见。请逐条回应：对每条 Strength/Weakness/Question，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 审稿意见（完整原文）\n\n**审查侧重**: 方法严谨性 + 实验设计 + 统计检验\n\n### Overall: 3.5 — Borderline Conference\n理论贡献扎实（Proposition 1 + 组合框架）、评估规模罕见地全面（47+ tables），但核心消融的统计检验缺失、F1 实际提升在 Bonferroni 校正后不显著、full fine-tuning 组合性失效未得到充分分析。\n\n### Strengths\n**S1** 理论基础严谨。Proposition 1 使用泵引理正式证明 domain/range 约束不是上下文无关的，Appendix O 证明完整。\n**S2** 约束组合框架设计精巧。§4 Eq. 2 的非对称合取配合 grammar-first fallback 是优雅的工程决策。\n**S3** 评估规模罕见。38 页 47+ 表格。\n**S4** 诊断指标体系设计良好（DR/CF/RoV/ET/RV）。\n**S5** Fine-tuning 统计报告有亮点——Bonferroni 校正 + 诚实报告 R-F1 不显著。\n**S6** 双因子定量分析（κ × baseline violation）有实践指导价值。\n**S7** 错误分析深入且诚实（Appendix J/K/N）。\n\n### Must-Fix（Critical）\n**N1** Zero-shot 核心消融（Table 1）缺乏置信区间和显著性检验。核心主张（grammar 3% vs semantic 24% vs 组合 94% DR reduction）没有统计证据支撑。Appendix G Table 8 仅覆盖 fine-tuning，Table 31 仅提供通用精度估计。建议：为 Table 1 提供 bootstrap CI + 配对检验 + Bonferroni 校正。\n\n**N2** Full fine-tuning 组合性失效未充分分析。Table 42 显示 full FT + S1 的 R-F1（37.89）与 unconstrained 完全相同。如果 full FT 已内化约束，这对 \"decoding-time enforcement is necessary\" 的动机叙事构成反证。建议：报告 full FT unconstrained 的 violation rates，分析原因，限定 composability claim 为 \"parameter-efficient fine-tuning\"。\n\n### Should-Fix（Major/Minor）\n**W1 [Major]** WikiEvents n=20 统计效力不足，CI ±3.0pp，argument F1 shift ±1.1pp 落在 CI 内。\n**W2 [Major]** 70B AWQ INT4 量化混淆因素未控制。\n**W3 [Major]** 缺乏与 training-based 方法（GoLLIE/KnowCoder/ADELIE）的正面 violation rate 对比。\n**W4 [Minor]** Enabling dependency \"empirical enabling dependency\" 术语强度与 n=6 证据基础不匹配。\n**W5 [Minor]** Proposition 1 证明的 position→name indexing 简化论证不够严格。\n\n### 小问题\n- Table 1 caption \"b = beam\" 定义位置不当\n- §3.3 prefix map 正确性未形式化\n- Figure 1 未可视化 grammar-first fallback 路径\n- DocRED dev set 评估应在 Limitations 中提及\n\n### Questions\n**Q1**: 能否为 Table 1 提供 bootstrap CI + Bonferroni 校正？\n**Q2**: AWQ INT4 对约束执行精度的影响？\n**Q3**: Full FT unconstrained 的 violation rates 是多少？\n**Q4**: Table 2 Llama S1 SciERC DR=0% 是否所有种子成立？\n**Q5**: TCR vs OntoCoDec 在 F1 上的对比？TCR 是否是更实用的替代？\n**Q6**: Schema ambiguity σ 值能否提供定量阈值？\n\n### Missing References\n- Huang et al. (2024) \"Planning for Constrained LLM Generation\"\n- PICARD 约束粒度差异讨论\n\n### Overall: 3.5 — Borderline Conference\n\n---\n\n请逐条回应上述所有 Strengths、Must-Fix、Should-Fix、小问题、Questions 和 Missing References。"
  }
}
```

</details>

---


### Tool result

_source line 2160 · 2026-05-23T02:54:38.693896+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1364
}
```

</details>

---


### Assistant

_source line 2161 · 2026-05-23T02:54:41.646094+00:00_

交叉分享已发出。等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director"
}
```

</details>

---


## Round 158

## Round 158

2 recorded events


### User

_source line 2162 · 2026-05-23T02:54:44.213557+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

**评分**: Overall 3.5 (Borderline Conference)

**核心判断**: 理论贡献扎实（Proposition 1 泵引理证明 + Eq. 2 组合框架），评估规模在约束解码论文中罕见（38 页 47+ 表格），但两个 Critical 问题制约接收信心：

1. **Zero-shot 核心消融（Table 1）完全缺乏统计检验** — enabling dependency 主张无 CI/显著性检验支撑，而 fine-tuning 部分（Table 8）已正确使用 Bonferroni 校正，形成不一致
2. **Full fine-tuning 组合性失效（Table 42: R-F1 完全不变）未分析原因** — composability claim 可能仅限于 LoRA，需显著限定

另有 3 个 Major 问题：WikiEvents n=20 统计效力不足、70B AWQ INT4 量化混淆未控制、缺乏与 GoLLIE/KnowCoder 的正面 violation rate 对比。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 2163 · 2026-05-23T02:54:48.991132+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director"
}
```

</details>

---


## Round 159

## Round 159

2 recorded events


### User

_source line 2164 · 2026-05-23T02:57:12.145564+00:00_

[Reviewer 1 审稿意见]:

## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应

---

### Strengths 回应

**[AGREE] R2-S1**: Proposition 1 的形式化价值。同意。我在自己的 S1 中也独立认定这一点——泵引理证明（Appendix O）逻辑链完整，为二层架构提供了不可简化的形式论据。

**[AGREE] R2-S2**: 评估全面性。同意。我在 S3 中做了相同判断——38 页 47+ 表格的规模在约束解码文献中罕见，覆盖度（3 数据集 × 3 模型族 × zero-shot/fine-tuned × 8B/70B + beam search + runtime profiling）足够支撑主要 claims。

**[AGREE] R2-S3**: 双因素定量分析的独立价值。同意。我在 S6 中也独立标注了这一点。但需补充：R²=0.886 基于 n=6 配置（R2 的 Q4 也质疑了这一点），统计可靠性有限。

**[AGREE] R2-S4**: CF↔DR trade-off 的诚实刻画。同意。论文在 Appendix C 和 Limitations 中确实诚实讨论了这一 trade-off。但这恰好与 R2-W1（Abstract 选择性呈现）形成矛盾——诚实在正文/附录中，但 Abstract 中选择性报告了最佳情况。

**[AGREE] R2-S5**: 实用性——无需约束专属训练，从 IE 本体自动编译。同意。这是 decoding-time enforcement 相对于 training-based 方法的核心优势。

---

### Weaknesses 回应

**[AGREE] R2-W1** (Abstract 对 CF 副作用的选择性呈现)

同意这是一个有效的批评。Abstract 报告 "up to 1.18% under greedy decoding on well-calibrated models" 选择了 CF 的最佳情况，而 Table 1 中 CF 的实际范围确实可达 ~12%（如 DocRED S2 配置）。Limitations 和 Appendix C 中虽然诚实地展示了完整范围，但 Abstract 作为论文最高可见度的部分，理应呈现 CF 的完整范围（包括最坏情况）以避免误导。

补充我的观察：论文在 §4 中提到 "fallback triggers on 0.5-3.7% of type-bearing positions (zero-shot)"，这是 fallback 触发率而非 CF violation rate 本身——这两个指标的混用进一步增加了读者的理解负担。建议 Abstract 修改为如 "CF violations range from 0.42–12.02% under greedy decoding, reducible via beam search (§5.4) and fine-tuning (<0.11%)"，呈现完整图景。

**[REBUT] R2-W2** (核心技术新颖性有限)

部分不同意 R2 对新颖性的评判。

1. **Semantic layer 不是简单查表**。R2 将 semantic layer 描述为 "运行时查表"，但实际机制是 *有状态的动态实体注册表*（§3.2-3.3）：在生成过程中实时追踪实体-类型绑定，基于当前生成状态做 continuation masking。这与静态查表有本质区别——它需要解决 greedy commitment 问题（一旦为实体分配类型就锁定）、fallback cascade（§4）、以及跨三元组的类型一致性维护。这些是非平凡的设计决策，不是 "查表" 能概括的。

2. **Proposition 1 的 Remark 不削弱理论贡献**。R2 认为 Remark（"实际语言是 regular 的，DFA 规模 O(|T|^n)"）削弱了 Proposition 1。但 Proposition 1 的目的不是证明 "理论上不可能"，而是证明 *grammar-only 方法（CFG）不充分*。Remark 补充说明虽然 DFA 理论上可行但规模指数爆炸（SciERC 仅 6 entity types + 7 relations 已需 O(7^n) 状态），这恰恰强化了 semantic layer 的工程必要性。论文的论点是 "CFG 不够 + DFA 不可行 → 需要运行时语义层"，这个逻辑链是完整的。

3. **但我同意新颖性的 ceiling 确实存在**。论文自述 "systematic engineering contribution with theoretical grounding" 是诚实的定位。个别组件（CFG 约束 ≈ GCD，类型检查 ≈ 运行时断言）不新，但 *组合框架*（Eq. 2 的非对称合取 + grammar-first fallback + composability with LoRA）作为一个完整的系统贡献是有价值的。这类似于 Transformer 的各组件（attention、FFN、residual connection）都不新，但组合产生了新价值。

**结论**：R2 对 novelty ceiling 的判断有合理成分，但 "运行时查表" 的简化描述低估了 semantic layer 的技术复杂度。建议评估为 "moderate novelty with strong execution"，而非 "limited novelty"。

**[AGREE] R2-W3** (Abstract 信息密度过高)

同意。Abstract ~150 词中塞入 12+ 数字和 5+ 首次出现缩写（DR、CF、RoV、S1/S2 等）确实超出了读者的认知负荷。顶会 Abstract 的最佳实践是 ≤3 个关键数字 + 定性描述，缩写在正文中引入。

**[AGREE] R2-W4** (Introduction "42-99%" 与 Abstract "42-90%" 不一致)

同意。如果数值范围在 Abstract 和 Introduction 之间不一致，这是需要修正的文本错误。无论哪个数字正确，两处必须保持一致。

**[REBUT] R2-W5** (Proposition 1 的实际意义被 Remark 削弱)

部分不同意——与 W2 的回应一致。

Remark 并未将理论 barrier 降级为 "仅仅是工程问题"。关键区分：

- **CFG 不充分**（Proposition 1 的核心结论）是一个 *硬* 理论结果——无论工程投入多少，你不能用 CFG 表达 domain/range 约束。这意味着所有基于 CFG 的约束解码工具（GCD、XGrammar、Outlines、SynCode）在原理上无法执行 IE 的语义约束。
- **DFA 理论上可行但规模爆炸**（Remark 的补充）说明存在一条替代路径，但其 O(|T|^n) 复杂度使之不实用——SciERC 的 6 entity types 已需 O(7^n) 状态，DocRED 的 96 relation types 使之完全不可行。

Proposition 1 的价值在于正式排除了 "用现有 grammar-based 工具就够了" 这一最自然的 baseline 思路。即使 DFA 理论上可行，CFG 不可行这一事实对约束解码社区仍有指导意义，因为当前主流工具全部基于 CFG/PDA。

**[AGREE] R2-W6** (WikiEvents 过于初步)

同意。我在自己的 W1 (Should-Fix) 中也独立标记了这一问题——n=20 文档、CI ±3.0pp，argument F1 shift ±1.1pp 完全在噪声范围内。论文自称 "preliminary" 但仍在 §5 中作为四大实验之一呈现，存在 overclaiming 风险。

---

### Questions 回应

**[AGREE] R2-Q1** (Beam search 中 registry 独立性和内存开销)

有效问题。Appendix F（pages 28-29）的 beam search 分析展示了 beam width 消融（Table 25）和 runtime profiling（Table 26），证实 "each beam independently maintains grammar and semantic state"。但 R2 问的 k=8 内存开销论文未显式量化——Table 26 报告了 latency overhead（beam search 从 10% greedy 增加到 +32% k=4 的开销），但 memory overhead 未给出。这在 GPU memory 紧张的部署场景（如 70B AWQ 模型）中是实际关切。建议补充 peak memory 数据。

**[AGREE] R2-Q2** (为什么不将 TCR 整合到解码循环)

有效问题。TCR（Appendix M, Table 45）是 post-hoc resolution，将其整合到解码循环需要 look-ahead 或回溯，可能引入指数级搜索空间。论文未讨论计算复杂度，但直觉上这类似于 constraint satisfaction problem（CSP），在一般情况下是 NP-hard。论文应至少简要讨论为何选择 greedy commitment + post-hoc resolution 而非 integrated resolution。

**[AGREE] R2-Q3** (是否直接运行 GCD/BoostCD 作为 baseline)

有效问题。Table 16-17 提供了间接对比——Table 16 对比 OntoCoDec grammar-only vs vLLM guided_json（差异 ≤0.5pp），Table 17 对比 grammar-based 方法的 DR 差异。但这些是 *grammar 层* 的对比，不是完整系统的对比。R2 问的是是否直接运行了 GCD/BoostCD 的代码——从论文描述看，Table 16 的 vLLM guided_json 确实是直接运行的对比，但 GCD/BoostCD 似乎是基于文献报告而非重新运行。建议明确说明。

**[AGREE] R2-Q4** (R²=0.886 的 n=6 是否有 leave-one-out 验证)

高度有效的问题。n=6 的线性拟合 R²=0.886 可能严重过拟合——6 个点拟合一条线几乎总是会得到高 R²。Leave-one-out cross-validation 或至少 adjusted R² 是必需的。我在自己的 W4 (Should-Fix) 中也标记了这一点（"n=6 is insufficient for statistical inference"，Appendix C.4 自承）。

---

### Missing References 回应

**[REBUT] Text2Event (Lu et al., 2021, ACL)**

论文的 Related Work（§6 + Appendix B）聚焦于 constrained decoding for RE/EE 和 schema-aware IE。Text2Event 是 sequence-to-structure 的事件抽取方法，使用 constrained decoding 但约束机制基于 trie 结构（词汇级），与 OntoCoDec 的 ontology-level 约束不在同一层次。但考虑到论文在 §5.4 做了 WikiEvents 实验（事件抽取），引用 Text2Event 作为 event extraction with generation 的 prior work 是合理的。**部分同意应补充引用。**

**[REBUT] DEGREE (Hsu et al., 2022, NAACL)**

DEGREE 是 prompt-based event extraction，不涉及 constrained decoding。与论文的技术方法没有直接可比性。论文的 Related Work 已涵盖了更相关的 event extraction 工作（如 TANL、InstructUIE）。**不认为是必要引用。**

**[AGREE] DCCD (2026) 和 pldi2025_type_constrained_codegen 的 venue/年份需核实**

如果这些引用确实出现在论文中，venue 和年份的准确性需要验证。引用中的年份/venue 错误是审稿中的常见问题。

---

### 总体评估回应

**[AGREE] Overall 3.5 的判断**。我给出了相同分数（3.5, Borderline Conference）。

我与 R2 的主要分歧在于 **W2（novelty）的评判**：R2 认为核心技术新颖性有限（"运行时查表"），我认为这低估了 semantic layer 的设计复杂度（动态 entity registry、greedy commitment、fallback cascade、composability）。但我同意新颖性的 ceiling 确实存在——这是一篇 "strong execution on a well-defined problem" 而非 "paradigm-shifting" 的论文。

两位 Reviewer 的共识问题：
1. 统计检验不足（我的 N1 + R2 的 Q4）
2. WikiEvents 过于初步（我的 W1 + R2 的 W6）
3. CF 副作用呈现需要更透明（R2 的 W1，我在 S5/S6 中间接涉及）
4. Abstract 写作质量（R2 的 W3/W4）

如果这些问题得到修正（特别是 zero-shot 统计检验和 Abstract 的 CF 呈现），论文可达 4.0（Conference）。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 2165 · 2026-05-23T02:57:20.646933+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director"
}
```

</details>

---


## Round 160

## Round 160

2 recorded events


### User

_source line 2166 · 2026-05-23T02:57:23.230345+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交。

**与 R2 的主要分歧**: W2（novelty 评判）——R2 将 semantic layer 简化为 "运行时查表"，我认为动态 entity registry + greedy commitment + fallback cascade 的设计复杂度被低估。Proposition 1 的 Remark 不削弱核心结论（CFG 不充分），而是补充说明 DFA 路径的工程不可行性。

**与 R2 的共识**: Abstract 的 CF 选择性报告（W1）、WikiEvents 过于初步（W6）、Abstract 信息过载（W3）、数值不一致（W4）、R²=0.886 基于 n=6 需要交叉验证（Q4）。

**两位 Reviewer 一致判定**: 3.5 Borderline Conference，核心瓶颈是 zero-shot 统计检验缺失和 novelty ceiling 的定位。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 2167 · 2026-05-23T02:57:31.725464+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director"
}
```

</details>

---


## Round 161

## Round 161

12 recorded events


### User

_source line 2168 · 2026-05-23T02:58:44.821207+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 交叉回应 Reviewer 1 审稿意见

---

### Strengths 回应

**[AGREE] R1-S1**: Proposition 1 的泵引理证明严谨。Appendix O 的完整证明是扎实的理论基础。但如我在自己的审稿中指出（R2-W5），其后的 Remark（p.3）承认实际语言是 regular 的，只是 DFA 规模 O(|T|^n) 不可行，这部分削弱了理论 barrier 的份量。

**[AGREE] R1-S2**: §4 Eq.2 的非对称合取设计确实精巧。Grammar-first fallback 在 CF↔DR trade-off 中的行为有详细追踪（Appendix C, Table 6-7）。

**[AGREE] R1-S3**: 38 页 47+ 表格的评估规模在该领域罕见，这一点没有争议。

**[AGREE] R1-S4**: DR/CF/RoV/ET/RV 的诊断指标体系确实设计良好，允许对不同类型的违约进行精确区分，而非笼统的 "violation rate"。

**[AGREE] R1-S5**: Bonferroni 校正 + 诚实报告 R-F1 不显著是论文的一个难得亮点。Table 8（p.21）明确报告 "no comparison reaches significance at α=0.05 after Bonferroni correction (k=4)"，这种统计诚实在该领域论文中不常见。

**[AGREE] R1-S6**: 双因子分析有实践指导价值。Figure 2（Appendix D, p.20）的 κ̄ × baseline violation 关系提供了可预测的框架。

**[AGREE] R1-S7**: 错误分析（Appendix J/K/N）深入且诚实，特别是 Appendix J（p.33-34）的 error taxonomy 覆盖了 false negatives（constraint-blocked vs. model-limited）和 false positives（schema-valid but incorrect），以及 CF 对预测质量的影响分析。

---

### Must-Fix 回应

**[REBUT] R1-N1**: Zero-shot 核心消融（Table 1）缺乏 CI 和显著性检验。

R1 的关切在统计学原理上有合理之处，但在具体情境下需要区分对待：

1. **Zero-shot greedy 解码是确定性的**。给定固定的模型权重和固定的 prompt，temperature=0 的 greedy decoding 产生完全确定的输出。论文在 Appendix G（p.30）明确说明 "Greedy decoding is deterministic"。对于确定性过程，bootstrap CI 在统计学上无意义——没有随机变量可供重采样。

2. **跨模型变异已覆盖**。Table 1 本身报告了 3 个不同模型（Qwen, Llama, Mistral）在 2 个数据集上的结果。核心 claim（grammar 3% vs semantic 24% vs 组合 94%）不是单一配置的点估计，而是在 6 个独立配置（3 models × 2 datasets）上观察到的一致模式。§5.3 Table 3 进一步提供跨模型验证。

3. **Prompt 敏感性已控制**。Appendix H（Table 35, p.31）在 SciERC 上测试了 3 种 prompt 变体（Default, Minimal, Detailed），结果显示约束执行在所有变体下均有效（ET 和 RV 均降至 0%，DR 下降 94.0-94.6%）。这提供了超越单一 prompt 的稳健性证据。

4. **Document-level bootstrapping 确实可以补充**。虽然解码是确定性的，但可以通过 document-level bootstrapping 估计 violation rate 的 CI（将数据集视为文档的抽样）。Table 31（p.31）实际上已提供了这种估计：SciERC 551 文档的 95% CI 为 ±1.8pp，DocRED 998 文档为 ±0.8pp。

**综合判断**：R1 的要求（bootstrap CI + 配对检验 + Bonferroni 校正）对 zero-shot greedy 过度严格——确定性解码无需传统 CI。但论文确实可以更突出地呈现已有的 robustness 证据（Table 31 + Table 35）。建议将 "zero-shot greedy is deterministic" 在方法论中更显式声明，并在 Table 1 caption 中引用 Table 31/35 作为 robustness 参考。

---

**[REBUT] R1-N2**: Full fine-tuning 组合性"失效"。

R1 对 Table 42 的解读有误。仔细查看 Appendix L（p.34-35，appendix_full_ft.tex）的数据：

| 配置 | R-F1 | DR | CF |
|------|------|-----|-----|
| Full FT unconstrained | 37.89 | **2.74%** | 0% |
| Full FT + S1 | 37.89 | **0%** | 1.31% |
| LoRA unconstrained | 43.77 | 1.18% | 0% |
| LoRA + S1 | 43.77 | 0.09% | 1.18% |

关键事实：
1. **Full FT 并未"已内化约束"**。Full FT unconstrained 仍有 2.74% DR——高于 LoRA 的 1.18%。这直接反驳了 R1 "full FT 已内化约束" 的前提。
2. **S1 在 Full FT 上完全有效**。DR 从 2.74% 降至 0%，且 F1 不变（37.89→37.89）。这恰恰是 composability 的证明，而非"失效"。
3. **R-F1 相同不等于约束无效**。R1 将 "F1 不变" 解读为约束无作用，但这混淆了两个独立目标：F1 衡量抽取质量，DR 衡量本体合规性。F1 不变 + DR→0% 正是理想结果——约束消除了违约而不损害质量。
4. **Full FT 的 R-F1 偏低（37.89 vs LoRA 43.77）是因为学习率未调优**（lr=2×10⁻⁴，适合 LoRA 但对 full FT 偏高）。论文在 Table 42 caption 中诚实承认了这一点。

R1 应修改的结论：Table 42 实际上支持了 OntoCoDec 的核心叙事——即使在 full fine-tuning 下，模型仍产生 2.74% DR violations，decoding-time enforcement 仍然必要且有效。

不过，R1 有一个合理的细节建议：论文确实应在 Limitations 中更明确地限定 composability 评估以 LoRA 为主（已在 Limitations p.9 line 101 做了，但可更突出）。

---

### Should-Fix 回应

**[AGREE] R1-W1**: WikiEvents n=20 统计效力不足。CI ±3.0pp 使得 argument F1 的 ±1.1pp 变化确实在 CI 内不可靠。这与我自己的 R2-W6 一致——论文将 WikiEvents 结论纳入 contribution list 但实验基础过于初步。

**[AGREE] R1-W2**: 70B AWQ INT4 量化混淆因素未控制。Limitations（p.9）仅以一句带过（"70B experiments use AWQ INT4 quantization, which may alter logit distributions at mask boundaries; the impact on constraint enforcement precision has not been isolated"），但 70B 的关键发现（semantic-only 独立达到 84% DR reduction）直接依赖量化后的 logit 分布。理想情况下需要 FP16 对照实验。

**[REBUT] R1-W3**: 缺乏与 GoLLIE/KnowCoder/ADELIE 的正面 violation rate 对比。

这个要求在原则上合理，但在实践中存在根本性困难：

1. **方法论不可比性**。GoLLIE、KnowCoder、ADELIE 是 training-based 方法，需要特定训练数据和训练流程。OntoCoDec 是 decoding-time 框架，正交于训练方法。直接对比需要在相同模型、相同数据、相同训练设置下叠加 OntoCoDec 到这些方法之上——这超出了合理的实验范围。

2. **论文已提供间接对比**。§6（p.8）报告 GoLLIE-7B 在 SciERC 上 R-F1=0.0（46% empty output）但消除了 DR，而 OntoCoDec 在 R-F1=45.47 时达到 DR=0.09%。这表明 GoLLIE 的 violation elimination 以牺牲 extraction quality 为代价，而 OntoCoDec 保持了高质量。

3. **更公平的对比是 GCD/BoostCD baseline**。Table 16-17（Appendix）提供了与 GCD-equivalent grammar-only enforcement 的直接对比（grammar-only: DR 减少 15-96%，OntoCoDec full S1: DR 减少 >99%），证明了 semantic layer 超越纯 CFG 方法的增量价值。

**综合判断**：不应要求不可比方法的正面实验对比，但论文可以在 Related Work 中增加一个表格，系统性地对比不同方法的 violation handling 策略（prevention vs. detection vs. training internalization）和已报告的 violation rates（引用原文数据）。

**[AGREE] R1-W4**: "Enabling dependency" 术语与 n=6 证据基础不匹配。"Empirical enabling dependency" 在 §5.1（p.5）中用于描述一个跨 6 个配置观察到的模式。Figure 2（p.20）的 R²=0.886 基于 n=6 点，统计效力确实不足以支撑 "dependency" 这样的因果性术语。建议改为 "empirical co-occurrence pattern" 或 "observed complementarity"。

**[REBUT] R1-W5**: Proposition 1 的 position→name indexing 简化论证。

Proposition 1（p.3）证明的核心是对 *无界实体集* 的 domain/range 约束非 context-free。论证的关键步骤是：一个输出包含 n 个独立类型实体，后跟引用它们的关系三元组，泵引理要求存在 pump decomposition，但 pumping 任何实体会破坏后续类型约束的一致性。position→name indexing 是一个合理的简化——实际系统中实体通过名称引用而非位置，但这不影响证明的核心结论：cross-field type dependency 需要无界状态追踪，CFG 无法提供。Appendix O 的完整证明（我在第一轮审稿中已确认）在该简化下是 sound 的。

---

### 小问题回应

**[AGREE]** Table 1 caption "b = beam" 定义位置不当——应在首次使用 beam 的地方定义。

**[REBUT]** §3.3 prefix map 正确性未形式化——prefix matching 在 BPE tokenizer 上的正确性是一个工程细节，形式化证明不会为论文增加有意义的理论贡献。论文在 Appendix H（p.31）通过 3 种 tokenizer（BPE: Qwen/Llama, SentencePiece: Mistral）的实证验证覆盖了实际正确性。

**[AGREE]** Figure 1 未可视化 grammar-first fallback 路径——Figure 1（p.3）展示了 grammar layer 和 semantic layer 的组合，但 fallback 逻辑（当 S(t)∩G(t)=∅ 时 fallback 到 G(t)）是 §4 Eq.2 的核心设计，应在架构图中体现。

**[AGREE]** DocRED dev set 评估应在 Limitations 中提及——论文使用 DocRED dev set（998 docs）而非 test set 进行评估（§5, p.5 脚注），这是因为 test set annotations 不公开。Limitations 中应显式声明这一限制。

---

### Questions 回应

**[AGREE] R1-Q1**: 如上述 N1 回应，zero-shot greedy 不需要传统 bootstrap CI（确定性过程），但 document-level bootstrap（Table 31）和 prompt sensitivity（Table 35）已提供了 robustness 证据。

**[AGREE] R1-Q2**: AWQ INT4 对 logit 分布的影响确实是一个未控制的混淆因素。70B semantic-only 的 84% DR reduction 这一关键发现的可信度受此影响。

**[REBUT] R1-Q3**: "Full FT unconstrained 的 violation rates 是多少？" 答案已在 Table 42（Appendix L, p.35）：DR=2.74%, CF=0%。R1 可能未注意到这一数据——它直接反驳了 "full FT 已内化约束" 的假设。

**[AGREE] R1-Q4**: Table 2 Llama S1 SciERC DR=0% 是否跨种子成立——这是 fine-tuning 结果，仅报告了 seed 42。虽然 Table 8（p.21）为 fine-tuning 提供了 bootstrap CI，但跨种子的 DR=0% 稳定性未验证（DR 本身是离散计数，单个种子下 0% 可能在其他种子下出现少量 violations）。

**[AGREE] R1-Q5**: TCR（Appendix M）vs OntoCoDec 的 F1 对比是一个好问题。论文报告 TCR 减少 CF 18-92%，但未报告 TCR 对 DR 和 F1 的影响。如果 TCR 是一个更简单的后处理替代方案且效果可比，这会削弱 OntoCoDec 解码时执行的必要性论证。

**[REBUT] R1-Q6**: Schema ambiguity σ 的定量阈值。σ 在 Appendix D（p.36, Table 46）已有具体定义和逐 relation 的值。问题不在于缺乏定量定义，而在于正文中未给出可操作的阈值建议（如 "σ > 0.5 时 DR reduction 受限"）。但这更接近 future work 方向，而非当前论文的缺陷。

---

### Missing References 回应

**[AGREE]** Huang et al. (2024) "Planning for Constrained LLM Generation" 可能相关——如果它讨论了约束规划与解码的关系，与 OntoCoDec 的多层约束组合有交集。但需确认该论文的具体内容和 venue。

**[REBUT]** PICARD 约束粒度差异讨论——§6（p.8, section6_related_work.tex line 9）已讨论了 PICARD 与 OntoCoDec 的关键差异："unlike PICARD's rejection-based pruning, OntoCoDec applies constructive forward masking via a dynamic entity registry"。这一对比涵盖了核心机制差异（rejection vs. constructive masking）。如需更细粒度的对比（如 PICARD 的 incremental parsing vs. OntoCoDec 的 prefix matching），可以在 Appendix B（Extended Related Work, p.13-17）中补充，但不应作为正文的 must-fix。

---

### Overall Assessment 回应

**[AGREE]** R1 的 3.5 评分与我的评估一致。我们的核心判断趋同：

1. **共识**：理论基础扎实、评估全面、但核心技术新颖性有限。论文是高质量的系统工程+分析贡献，处于 Conference/Findings 交界。

2. **分歧**：
   - R1-N2（full FT composability "failure"）——我认为 R1 对 Table 42 的解读有误，数据实际支持 OntoCoDec（见上述详细反驳）。
   - R1-N1（zero-shot CI）——我认为对确定性 greedy decoding 要求 bootstrap CI 在统计学上不恰当，但 document-level bootstrapping 作为补充是合理的。
   - R1-W3（GoLLIE/KnowCoder 正面对比）——我认为跨范式方法的正面实验对比不可行，间接对比（§6）和 GCD-equivalent baseline（Table 16-17）足够。

3. **我的额外关切**（R1 未覆盖）：
   - Abstract 对 CF 的选择性报告（R2-W1）——Abstract 仅报告 "up to 1.18%" 而 Limitations 承认 "up to 12.02%"，这一信任度问题 R1 未提及但同样重要。
   - Abstract 信息密度过高（R2-W3）——12+ 个数字/百分比在 150 词内，影响可读性。

**维持 Overall 3.5, Confidence 4/5。**

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 2169 · 2026-05-23T02:59:16.284724+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "schema_semantic_constrained_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "schema_semantic_constrained_ie"
  }
}
```

</details>

---


### Tool result

_source line 2170 · 2026-05-23T02:59:16.737248+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-23T02:45:29.268786+00:00\", \"completed_at\": \"2026-05-23T02:50:18.642646+00:00\", \"findings\": [{\"severity\": \"warning\", \"dimension\": \"pages 1-8\", \"message\": \"主文 8 页仅 1 个 figure（Figure 1 架构图），其余全为 table。对于实证为主的论文，缺少结果可视化图（如核心指标的 bar chart 或消融趋势图）会削弱审稿人的视觉印象。建议将附录中的 Figure 2（DR vs Schema Restrictiveness）或 Figure 4（Beam width ablation）的关键子图提升到主文\"}, {\"severity\": \"warning\", \"dimension\": \"page 4\", \"message\": \"整页纯文本+公式（Method sections 3.2-3.4 + Section 4），无任何 display item。虽然方法描述中公式提供了一定视觉变化，但在 Figure 1（p.3）和 Table 1（p.5）之间形成了一个视觉空白页\"}, {\"severity\": \"info\", \"dimension\": \"page 3\", \"message\": \"Figure 1 内部分组件标签字号偏小（如 \\\"Schema Compilation\\\" 下方的子步骤文字），打印后可能接近可读性下限。建议检查打印版字号是否 ≥ 8pt\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"单页包含 Table 3 + Table 4，页面较密集。当前排版未溢出，但两个表之间的文字段落空间紧凑\"}, {\"severity\": \"info\", \"dimension\": \"pages 25,31 appendix\", \"message\": \"附录中部分页面极度密集（p.25 四个表、p.31 五个表），虽然附录密度要求较低，但审稿人翻阅时可能感到信息过载\"}, {\"severity\": \"info\", \"dimension\": \"page 38\", \"message\": \"全文最后一页仅填充约 1/3（附录证明尾部），可考虑调整分页使空间更紧凑\"}], \"counts\": {\"critical\": 0, \"warning\": 2, \"info\": 4}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 2171 · 2026-05-23T02:59:16.737749+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "schema_semantic_constrained_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "schema_semantic_constrained_ie"
  }
}
```

</details>

---


### Tool result

_source line 2172 · 2026-05-23T02:59:17.993354+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 1255
}
```

</details>

---


### Tool call

_source line 2173 · 2026-05-23T02:59:18.194667+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 2174 · 2026-05-23T02:59:18.195344+00:00_

1	# Review Issues Tracker — schema_semantic_constrained_ie
2	# Updated: Round 20 Action Matrix dispatched, 2026-05-23
3	
4	# ============================================================
5	# Round 20 Active Issues
6	# ============================================================
7	
8	- id: "R15-MF3"
9	  summary: "正文溢出至第 9 页（§7 末尾约 13 行）"
10	  category: format
11	  severity: critical
12	  status: in_progress
13	  first_raised_round: 13
14	  last_seen_round: 20
15	  mentions:
16	    - round: 15
17	      reviewers: [1, 2]
18	      note: "R15: 正文溢出第 9 页。"
19	    - round: 18
20	      note: "R18 标记为 resolved（正文 ≤ 8 页）。"
21	    - round: 20
22	      reviewers: [2]
23	      note: "R20: R2-N1 重新发现。§7 溢出至 page 9 约 13 行。"
24	  action_items:
25	    - round: 18
26	      action: "压缩正文至 ≤ 8 页"
27	      assigned_to: paper_agent
28	      status: completed
29	    - round: 20
30	      action: "压缩 §7 从~143词到~100词；如不够从 §5.4 beam 段回收空间"
31	      assigned_to: paper_agent
32	      status: in_progress
33	  resolution: ""
34	  resolution_round: null
35	
36	- id: "R16-MF3"
37	  summary: "CF trade-off 在 Abstract/Introduction 中 framing 偏乐观——系统引入的 CF 未充分 acknowledge"
38	  category: framing
39	  severity: critical
40	  status: in_progress
41	  first_raised_round: 15
42	  last_seen_round: 20
43	  mentions:
44	    - round: 17
45	      reviewers: [1, 2]
46	      note: "R17: zero-shot Llama DocRED 12.02% 未在主文叙述出现。"
47	    - round: 18
48	      reviewers: [1, 2]
49	      note: "R18: Abstract 写 'up to 12% zero-shot'，有改善。"
50	    - round: 19
51	      reviewers: [1, 2]
52	      note: "R19: R2-W3 指出 Abstract CF 表述偏乐观。R1 PARTIALLY AGREE。"
53	    - round: 20
54	      reviewers: [1, 2]
55	      note: "R20: R1-N2 + R2-N2 共识。CF framing 从 R15 至今每轮修复被打回。根因：trade-off 始终是 peripheral caveat 而非 structural acknowledgment。"
56	  action_items:
57	    - round: 19
58	      action: "Abstract CF 改为审慎表述"
59	      assigned_to: paper_agent
60	      status: completed
61	    - round: 20
62	      action: "(1) Abstract 核心 claim 后紧跟 C
…[truncated 13069 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2175 · 2026-05-23T03:02:10.087331+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "schema_semantic_constrained_ie",
  "issues_yaml": "\n# Review Issues Tracker — schema_semantic_constrained_ie\n# Updated: Round 21 Report submitted, 2026-05-23\n\n# ============================================================\n# Round 21 Active Issues\n# ============================================================\n\n- id: \"R16-MF3\"\n  summary: \"CF trade-off 在 Abstract 中 framing 偏乐观——仅报告 1.18% 而实际范围达 12.02%\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 15\n  last_seen_round: 21\n  mentions:\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R17: zero-shot Llama DocRED 12.02% 未在主文叙述出现。\"\n    - round: 18\n      reviewers: [1, 2]\n      note: \"R18: Abstract 写 'up to 12% zero-shot'，有改善。\"\n    - round: 19\n      reviewers: [1, 2]\n      note: \"R19: R2-W3 指出 Abstract CF 表述偏乐观。R1 PARTIALLY AGREE。\"\n    - round: 20\n      reviewers: [1, 2]\n      note: \"R20: R1-N2 + R2-N2 共识。CF framing 从 R15 至今每轮修复被打回。\"\n    - round: 21\n      reviewers: [1, 2]\n      note: \"R21: R2-W1 (Major) + R1 AGREE。Abstract 报告 'up to 1.18% under greedy decoding on well-calibrated models' 是 cherry-picking 最优情况。Table 1 显示 CF 实际范围 0.08-12.02%。两位 Reviewer 共识：Abstract 应呈现完整范围。\"\n  action_items:\n    - round: 19\n      action: \"Abstract CF 改为审慎表述\"\n      assigned_to: paper_agent\n      status: completed\n    - round: 20\n      action: \"Abstract 核心 claim 后紧跟 CF trade-off 声明\"\n      assigned_to: paper_agent\n      status: completed\n    - round: 21\n      action: \"Abstract 中 CF 报告改为完整范围（如 '0.46–12.02% depending on model calibration'），不限于 well-calibrated models 最佳值\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R19-M2\"\n  summary: \"Abstract 数值过于精确 + 信息密度过高\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 19\n  last_seen_round: 21\n  mentions:\n    - round: 19\n      reviewers: [1, 2]\n      note: \"R19: R2-W7 + R1 AGREE。\"\n    - round: 20\n      reviewers: [1, 2]\n      note: \"R20: ≥15 数字、6 缩写。\"\n    - round: 21\n      reviewers: [1, 2]\n      note: \"R21: R2-W3 (Minor) + R1 AGREE。~150 词中 12+ 数字/百分比 + 5+ 首次出现缩写。建议三段式结构（问题→方法→关键结果），减至 4-5 个关键数字。\"\n  action_items:\n    - round: 20\n      action: \"精简 Abstract 至 2-3 headline 数字\"\n      assigned_to: paper_agent\n      status: completed\n    - round: 21\n      action: \"继续精简 Abstract：减至 4-5 个关键数字，删除首次出现的未定义缩写\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R21-W1\"\n  summary: \"Abstract/Intro DR 范围不一致：Abstract '42-90%' vs Introduction '42-99%'\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 21\n  last_seen_round: 21\n  mentions:\n    - round: 21\n      reviewers: [1, 2]\n      note: \"R2-W4 (Minor) + R1 AGREE。Abstract 说 '42–90% on DocRED'，Introduction 说 '42–99% across models and datasets'。虽后者是合并范围但并列造成混淆。\"\n  action_items:\n    - round: 21\n      action: \"统一 Abstract 和 Introduction 的 DR 降幅范围表述，或在 Introduction 中明确分数据集报告\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R16-W4\"\n  summary: \"70B AWQ INT4 quantization 对约束效果的影响未隔离\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 14\n  last_seen_round: 21\n  mentions:\n    - round: 19\n      reviewers: [1, 2]\n      note: \"R19: Limitations 已有 disclaimer 但缺实证。\"\n    - round: 20\n      reviewers: [1]\n      note: \"R20: 单模型不足以支撑 70B-class validation 泛化。\"\n    - round: 21\n      reviewers: [1, 2]\n      note: \"R21: R1-W2 (Major) + R2 AGREE。70B semantic-only 84% DR reduction 直接依赖量化后 logit 分布，影响可信度。建议在 8B 上做 FP16 vs INT4 对照。\"\n  action_items:\n    - round: 17\n      action: \"Limitations 加 AWQ INT4 quantization disclaimer\"\n      assigned_to: paper_agent\n      status: completed\n    - round: 20\n      action: \"§5.4 加一句单模型限制说明\"\n      assigned_to: paper_agent\n      status: completed\n    - round: 21\n      action: \"理想：8B FP16 vs INT4 对照实验量化 quantization artifact；最低：Limitations 中更显式声明 70B 结论受量化影响\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R16-W3\"\n  summary: \"WikiEvents fine-tuning composability 仅 n=20 文档，统计效力严重不足\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 21\n  mentions:\n    - round: 19\n      reviewers: [1, 2]\n      note: \"R19: power analysis 已创建，§5.4 加 (Preliminary)。\"\n    - round: 20\n      reviewers: [2]\n      note: \"R20: n=20 基本限制无法根本解决。\"\n    - round: 21\n      reviewers: [1, 2]\n      note: \"R21: R1-W1 (Major) + R2-W6 (Minor) 共识。CI ±3.0pp，argument F1 shift ±1.1pp 在 CI 内不可区分。不应在 Abstract 引用 WikiEvents 结果，不应在 contribution list 中列入。\"\n  action_items:\n    - round: 19\n      action: \"提供 power analysis + preliminary 标注\"\n      assigned_to: paper_agent\n      status: completed\n    - round: 21\n      action: \"降级 WikiEvents：(1) 从 Abstract 删除 WikiEvents 数据；(2) contribution list 中降低强度或标注初步性质；(3) 可保留正文但明确定位为 pilot study\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R16-W5\"\n  summary: \"核心新颖性定位——系统集成而非算法创新，novelty ceiling 有限\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 14\n  last_seen_round: 21\n  mentions:\n    - round: 19\n      reviewers: [1, 2]\n      note: \"R19: 共识定位为 systems contribution。\"\n    - round: 20\n      reviewers: [1, 2]\n      note: \"R20: 论文已正确定位。R1 Excitement 3.5 vs R2 2.5。\"\n    - round: 21\n      reviewers: [1, 2]\n      note: \"R21: R2-W2 (Major) 认为 semantic layer 是运行时查表，novelty 有限。R1 partial REBUT：动态 entity registry + greedy commitment + fallback cascade 非简单查表，但同意 novelty ceiling 存在。分歧：R2 'limited novelty' vs R1 'moderate novelty with strong execution'。\"\n  action_items:\n    - round: 19\n      action: \"§7 Discussion 坦率定位 systems contribution\"\n      assigned_to: paper_agent\n      status: completed\n    - round: 21\n      action: \"更明确论证 semantic layer 的非显而易见设计选择（grammar-first fallback 策略、greedy limitation cascade），凸显 decode-time 执行不可替代性\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R16-W1\"\n  summary: \"κ̄/enabling dependency 统计支撑不足：R²=0.886 基于 n=6\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 21\n  mentions:\n    - round: 19\n      reviewers: [1, 2]\n      note: \"R19: 删除 §5.2/§7/Limitations 中的 κ̄，限制在 §4。\"\n    - round: 20\n      reviewers: [1]\n      note: \"R20: κ̄ 仍在 §4 占一段且在 abstract 出现。\"\n    - round: 21\n      reviewers: [1, 2]\n      note: \"R21: R1-W4 (Minor) + R2-Q4 共识。'Empirical enabling dependency' 术语过强，n=6 无法支撑因果性术语。建议改为 'observed pattern' 或 'consistent trend'。R²=0.886 需 leave-one-out CV 或 adjusted R²。\"\n  action_items:\n    - round: 20\n      action: \"从 abstract 删除 κ̄；§4 段压至 2-3 句标注 preliminary\"\n      assigned_to: paper_agent\n      status: completed\n    - round: 21\n      action: \"'Empirical enabling dependency' 改为 'observed complementarity pattern'；补充 adjusted R² 或 leave-one-out CV\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R20-W1\"\n  summary: \"Proposition 1 证明中 position→name 转换缺乏形式论证\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 20\n  last_seen_round: 21\n  mentions:\n    - round: 20\n      reviewers: [1]\n      note: \"R1-W3。Appendix O 承认 core argument transfers 但未给形式论证。\"\n    - round: 21\n      reviewers: [1]\n      note: \"R21: R1-W5 (Minor)。R2 REBUT 认为简化合理不影响核心结论。分歧存在但 severity 较低。\"\n  action_items:\n    - round: 20\n      action: \"Appendix O 加 2-3 句 informal argument：name-based ⊇ position-based\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R21-N1\"\n  summary: \"Zero-shot 核心消融（Table 1）缺乏统计检验\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 21\n  last_seen_round: 21\n  mentions:\n    - round: 21\n      reviewers: [1, 2]\n      note: \"R1-N1 (Critical)：Table 1 仅有点估计，无 bootstrap CI/配对检验/效应量。R2 REBUT：greedy 解码确定性，传统 CI 无意义；已有 Table 31 (document-level CI) + Table 35 (prompt sensitivity)。分歧：R1 认为缺统计检验削弱 enabling dependency 主张；R2 认为确定性过程不需传统 CI 但 document-level bootstrap 作为补充合理。\"\n  action_items:\n    - round: 21\n      action: \"在 Table 1 caption 或 §5.1 中显式声明 greedy decoding 是确定性过程；引用 Table 31/35 作为 robustness 参考；可选：补充 document-level bootstrap CI\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R21-N2\"\n  summary: \"Full FT 组合性解读分歧——R-F1 不变是否意味约束无效\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 21\n  last_seen_round: 21\n  mentions:\n    - round: 21\n      reviewers: [1, 2]\n      note: \"R1-N2 (Critical)：Table 42 full FT + S1 R-F1=37.89 与 unconstrained 相同，认为约束'失效'。R2 详细 REBUT：full FT unconstrained 仍有 DR=2.74%，S1 使 DR→0% 且 F1 不变——这恰恰是理想结果。R1 的解读将 F1 不变混淆为约束无效，实际约束在 violation reduction 上完全有效。R2 的 rebuttal 有数据支撑。\"\n  action_items:\n    - round: 21\n      action: \"正文或 Appendix L 中更显式报告 full FT unconstrained 的 DR/CF（已有但不够突出），明确 composability 评估以 LoRA 为主\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R21-W2\"\n  summary: \"缺乏与 GoLLIE/KnowCoder/ADELIE 的正面 violation rate 对比\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 21\n  last_seen_round: 21\n  mentions:\n    - round: 21\n      reviewers: [1, 2]\n      note: \"R1-W3 (Major)。R2 REBUT：跨范式方法正面实验对比不可行（不同训练流程/模型/prompt），间接对比（§6 GoLLIE R-F1=0.0）和 GCD-equivalent baseline（Table 16-17）足够。分歧存在。\"\n  action_items:\n    - round: 21\n      action: \"可选：在 Related Work 中增加表格系统对比不同方法的 violation handling 策略和已报告的 violation rates（引用原文数据）\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R15-MF3\"\n  summary: \"正文溢出至第 9 页\"\n  category: format\n  severity: critical\n  status: open\n  first_raised_round: 13\n  last_seen_round: 21\n  mentions:\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R15: 正文溢出第 9 页。\"\n    - round: 18\n      note: \"R18 标记为 resolved（正文 ≤ 8 页）。\"\n    - round: 20\n      reviewers: [2]\n      note: \"R20: §7 溢出至 page 9 约 13 行。\"\n    - round: 21\n      note: \"R21: 本轮未被任何 Reviewer 独立提及，可能已修复，待 Research Director 确认。\"\n  action_items:\n    - round: 20\n      action: \"压缩 §7\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R20-N1\"\n  summary: \"Corollary 标签混淆形式推导与经验观察\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 20\n  last_seen_round: 21\n  mentions:\n    - round: 20\n      reviewers: [1, 2]\n      note: \"R1-N1 + R2-N3 共识。Corollary→Empirical Observation。\"\n    - round: 21\n      note: \"R21: 本轮未被独立提及。与 R16-W1 (enabling dependency terminology) 相关——R21 R1-W4 建议将 'empirical enabling dependency' 改为 'observed pattern'。\"\n  action_items:\n    - round: 20\n      action: \"Corollary→Empirical Observation；§3 加 scale-dependent 限定\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R20-W2\"\n  summary: \"DocRED 评估使用开发集，超参数选择过程未披露\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 20\n  last_seen_round: 21\n  mentions:\n    - round: 20\n      reviewers: [1]\n      note: \"R1-W4。LoRA 超参选择策略未说明。\"\n    - round: 21\n      note: \"R21: R1 小问题重申 DocRED dev set 应在 Limitations 中声明。R2 AGREE。\"\n  action_items:\n    - round: 20\n      action: \"§5 加一句 LoRA 超参说明\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 21\n      action: \"Limitations 中显式声明 DocRED 使用 dev set 评估\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R20-W3\"\n  summary: \"Bonferroni 校正后最小 p=0.014 处于 borderline\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 20\n  last_seen_round: 21\n  mentions:\n    - round: 20\n      reviewers: [1]\n      note: \"R1-W5。补 per-config p-values + Cohen's d。\"\n    - round: 21\n      note: \"R21: 本轮未独立提及，可能已修复，待确认。\"\n  action_items:\n    - round: 20\n      action: \"Appendix bootstrap CI 部分报告各配置独立 p 值和 Cohen's d\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R20-W4\"\n  summary: \"主文 Related Work §6 过于精简，ADELIE 缺失\"\n  category: related_work\n  severity: info\n  status: open\n  first_raised_round: 20\n  last_seen_round: 21\n  mentions:\n    - round: 20\n      reviewers: [2]\n      note: \"R2-W2。ADELIE 缺失；PICARD 对比不足；SGLang 未提及。\"\n    - round: 21\n      note: \"R21: R2 missing references 提及 Text2Event (Lu et al., 2021) 和 DEGREE (Hsu et al., 2022)。R1 认为 Text2Event 部分相关（WikiEvents EE 上下文），DEGREE 非必要。\"\n  action_items:\n    - round: 20\n      action: \"§6 提升 ADELIE 到正文；扩展 PICARD 对比；提及 SGLang\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 21\n      action: \"考虑补充 Text2Event 引用（与 WikiEvents EE 实验相关）\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R18-M2\"\n  summary: \"Figure 1 视觉层次不够分明 + 未可视化 fallback 路径\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 18\n  last_seen_round: 21\n  mentions:\n    - round: 18\n      reviewers: [1, 2]\n      note: \"R18: 小问题。\"\n    - round: 21\n      reviewers: [1, 2]\n      note: \"R21: R1 小问题 + R2 AGREE。Grammar-first fallback 是 §4 Eq.2 核心设计，应在 Figure 1 中体现。\"\n  action_items:\n    - round: 21\n      action: \"Figure 1 中增加 grammar-first fallback 路径可视化\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R20-W5\"\n  summary: \"Running example 仍不充分\"\n  category: writing\n  severity: info\n  status: wont_fix\n  first_raised_round: 20\n  last_seen_round: 21\n  mentions:\n    - round: 20\n      reviewers: [2]\n      note: \"R2-W3。需贯穿 §3-§4 的完整 example。\"\n    - round: 21\n      note: \"R21: 本轮未提及。\"\n  action_items: []\n  resolution: \"空间限制无法在正文加完整 running example。§3.3 有 Used-for 示例，appendix 有 case studies。\"\n  resolution_round: 20\n\n- id: \"R20-W6\"\n  summary: \"Zero-shot 评估实际意义有限（R-F1 仅 4-8%）\"\n  category: experiment\n  severity: info\n  status: wont_fix\n  first_raised_round: 20\n  last_seen_round: 21\n  mentions:\n    - round: 20\n      reviewers: [2]\n      note: \"R2-W4。ZS 定位为 diagnostic probe 合理但篇幅偏多。\"\n    - round: 21\n      note: \"R21: 本轮未提及。\"\n  resolution: \"ZS 已定位为 diagnostic probe，篇幅已压缩。\"\n  resolution_round: 20\n\n# ============================================================\n# Round 20 及更早 Resolved\n# ============================================================\n\n- id: \"R19-W1\"\n  summary: \"遗漏 2026 年初高相关 constrained decoding 工作\"\n  category: related_work\n  severity: warning\n  status: resolved\n  first_raised_round: 19\n  last_seen_round: 20\n  resolution: \"§6 已添加 DCCD 和 Thinking Before Constraining 引用和讨论。\"\n  resolution_round: 19\n\n- id: \"R19-W2\"\n  summary: \"Enabling dependency 验证存在混淆变量\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 19\n  last_seen_round: 19\n  resolution: \"appendix_discussion.tex 已添加 enabling dependency confound analysis。\"\n  resolution_round: 19\n\n- id: \"R19-M1\"\n  summary: \"信息密度极高，缺少 running example\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 19\n  last_seen_round: 20\n  resolution: \"§3.3 已添加 Used-for running example。\"\n  resolution_round: 19\n\n- id: \"R17-W3\"\n  summary: \"Entity registry 顺序依赖未实验量化\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 20\n  resolution: \"entity_order_ablation 完成：shuffle 产生 byte-identical outputs。\"\n  resolution_round: 19\n\n- id: \"R19-W3\"\n  summary: \"主表缺少外部约束解码 baseline 行\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 19\n  last_seen_round: 20\n  resolution: \"vLLM guided_json 实验完成并写入主文。\"\n  resolution_round: 19\n\n- id: \"R19-W4\"\n  summary: \"Proposition 1 实践影响力表述可进一步精确\"\n  category: framing\n  severity: info\n  status: resolved\n  first_raised_round: 19\n  last_seen_round: 19\n  resolution: \"已添加 'for unbounded entity sets' 限定词 + Remark 区分。\"\n  resolution_round: 19\n\n- id: \"R15-MF1\"\n  summary: \"缺少与 GCD/BoostCD/GoLLIE 等同类方法的直接实验对比\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 18\n  resolution: \"vLLM guided_json 实验完成。\"\n  resolution_round: 19\n\n- id: \"R18-MF1\"\n  summary: \"引用错误：Cotti et al. 2025 多处与实际论文不符\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 18\n  resolution: \"4 条 bib 修正 + 全部 60 条引用审计。\"\n  resolution_round: 19\n\n- id: \"R16-MF2\"\n  summary: \"Abstract/Intro DR 降幅范围自相矛盾\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 18\n  resolution: \"DR range 按数据集拆分报告。\"\n  resolution_round: 19\n\n- id: \"R18-W1\"\n  summary: \"'四个模型(7-70B)'声称具有误导性\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 18\n  resolution: \"改为 '3 8B-class models with preliminary 70B validation'。\"\n  resolution_round: 19\n\n- id: \"R18-W2\"\n  summary: \"Zero-shot 实验篇幅占比过大\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 18\n  resolution: \"ZS 压缩至 ~1.65 页，定位为 diagnostic probe。\"\n  resolution_round: 19\n\n- id: \"R18-W3\"\n  summary: \"Abstract 数值密度过高 + DR 42-99% 范围过宽\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 18\n  resolution: \"DR range 按数据集拆分报告。\"\n  resolution_round: 19\n\n- id: \"R18-W4\"\n  summary: \"GCD-equivalent baseline 对比藏在 appendix\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 18\n  resolution: \"主文 §5 新增 vLLM guided_json 段落。\"\n  resolution_round: 19\n\n- id: \"R17-W3-prop1\"\n  summary: \"Proposition 1 有限 entity set caveat 在主文中缺失\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 18\n  resolution: \"§3 新增 Remark (finite entity sets)。\"\n  resolution_round: 19\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "schema_semantic_constrained_ie",
    "issues_yaml": "\n# Review Issues Tracker — schema_semantic_constrained_ie\n# Updated: Round 21 Report submitted, 2026-05-23\n\n# ============================================================\n# Round 21 Active Issues\n# ============================================================\n\n- id: \"R16-MF3\"\n  summary: \"CF trade-off 在 Abstract 中 framing 偏乐观——仅报告 1.18% 而实际范围达 12.02%\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 15\n  last_seen_round: 21\n  mentions:\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R17: zero-shot Llama DocRED 12.02% 未在主文叙述出现。\"\n    - round: 18\n      reviewers: [1, 2]\n      note: \"R18: Abstract 写 'up to 12% zero-shot'，有改善。\"\n    - round: 19\n      reviewers: [1, 2]\n      note: \"R19: R2-W3 指出 Abstract CF 表述偏乐观。R1 PARTIALLY AGREE。\"\n    - round: 20\n      reviewers: [1, 2]\n      note: \"R20: R1-N2 + R2-N2 共识。CF framing 从 R15 至今每轮修复被打回。\"\n    - round: 21\n      reviewers: [1, 2]\n      note: \"R21: R2-W1 (Major) + R1 AGREE。Abstract 报告 'up to 1.18% under greedy decoding on well-calibrated models' 是 cherry-picking 最优情况。Table 1 显示 CF 实际范围 0.08-12.02%。两位 Reviewer 共识：Abstract 应呈现完整范围。\"\n  action_items:\n    - round: 19\n      action: \"Abstract CF 改为审慎表述\"\n      assigned_to: paper_agent\n      status: completed\n    - round: 20\n      action: \"Abstract 核心 claim 后紧跟 CF trade-off 声明\"\n      assigned_to: paper_agent\n      status: completed\n    - round: 21\n      action: \"Abstract 中 CF 报告改为完整范围（如 '0.46–12.02% depending on model calibration'），不限于 well-calibrated models 最佳值\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R19-M2\"\n  summary: \"Abstract 数值过于精确 + 信息密度过高\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 19\n  last_seen_round: 21\n  mentions:\n    - round: 19\n      reviewers: [1, 2]\n      note: \"R19: R2-W7 + R1 AGREE。\"\n    - round: 20\n      reviewers: [1, 2]\n      note: \"R20: ≥15 数字、6 缩写。\"\n    - round: 21\n      reviewers: [1, 2]\n      note: \"R21: R2-W3 (Minor) + R1 AGREE。~150 词中 12+ 数字/百分比 + 5+ 首次出现缩写。建议三段式结构（问题→方法→关键结果），减至 4-5 个关键数字。\"\n  action_items:\n    - round: 20\n      action: \"精简 Abstract 至 2-3 headline 数字\"\n      assigned_to: paper_agent\n      status: completed\n    - round: 21\n      action: \"继续精简 Abstract：减至 4-5 个关键数字，删除首次出现的未定义缩写\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R21-W1\"\n  summary: \"Abstract/Intro DR 范围不一致：Abstract '42-90%' vs Introduction '42-99%'\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 21\n  last_seen_round: 21\n  mentions:\n    - round: 21\n      reviewers: [1, 2]\n      note: \"R2-W4 (Minor) + R1 AGREE。Abstract 说 '42–90% on DocRED'，Introduction 说 '42–99% across models and datasets'。虽后者是合并范围但并列造成混淆。\"\n  action_items:\n    - round: 21\n      action: \"统一 Abstract 和 Introduction 的 DR 降幅范围表述，或在 Introduction 中明确分数据集报告\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R16-W4\"\n  summary: \"70B AWQ INT4 quantization 对约束效果的影响未隔离\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 14\n  last_seen_round: 21\n  mentions:\n    - round: 19\n      reviewers: [1, 2]\n      note: \"R19: Limitations 已有 disclaimer 但缺实证。\"\n    - round: 20\n      reviewers: [1]\n      note: \"R20: 单模型不足以支撑 70B-class validation 泛化。\"\n    - round: 21\n      reviewers: [1, 2]\n      note: \"R21: R1-W2 (Major) + R2 AGREE。70B semantic-only 84% DR reduction 直接依赖量化后 logit 分布，影响可信度。建议在 8B 上做 FP16 vs INT4 对照。\"\n  action_items:\n    - round: 17\n      action: \"Limitations 加 AWQ INT4 quantization disclaimer\"\n      assigned_to: paper_agent\n      status: completed\n    - round: 20\n      action: \"§5.4 加一句单模型限制说明\"\n      assigned_to: paper_agent\n      status: completed\n    - round: 21\n      action: \"理想：8B FP16 vs INT4 对照实验量化 quantization artifact；最低：Limitations 中更显式声明 70B 结论受量化影响\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R16-W3\"\n  summary: \"WikiEvents fine-tuning composability 仅 n=20 文档，统计效力严重不足\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 21\n  mentions:\n    - round: 19\n      reviewers: [1, 2]\n      note: \"R19: power analysis 已创建，§5.4 加 (Preliminary)。\"\n    - round: 20\n      reviewers: [2]\n      note: \"R20: n=20 基本限制无法根本解决。\"\n    - round: 21\n      reviewers: [1, 2]\n      note: \"R21: R1-W1 (Major) + R2-W6 (Minor) 共识。CI ±3.0pp，argument F1 shift ±1.1pp 在 CI 内不可区分。不应在 Abstract 引用 WikiEvents 结果，不应在 contribution list 中列入。\"\n  action_items:\n    - round: 19\n      action: \"提供 power analysis + preliminary 标注\"\n      assigned_to: paper_agent\n      status: completed\n    - round: 21\n      action: \"降级 WikiEvents：(1) 从 Abstract 删除 WikiEvents 数据；(2) contribution list 中降低强度或标注初步性质；(3) 可保留正文但明确定位为 pilot study\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R16-W5\"\n  summary: \"核心新颖性定位——系统集成而非算法创新，novelty ceiling 有限\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 14\n  last_seen_round: 21\n  mentions:\n    - round: 19\n      reviewers: [1, 2]\n      note: \"R19: 共识定位为 systems contribution。\"\n    - round: 20\n      reviewers: [1, 2]\n      note: \"R20: 论文已正确定位。R1 Excitement 3.5 vs R2 2.5。\"\n    - round: 21\n      reviewers: [1, 2]\n      note: \"R21: R2-W2 (Major) 认为 semantic layer 是运行时查表，novelty 有限。R1 partial REBUT：动态 entity registry + greedy commitment + fallback cascade 非简单查表，但同意 novelty ceiling 存在。分歧：R2 'limited novelty' vs R1 'moderate novelty with strong execution'。\"\n  action_items:\n    - round: 19\n      action: \"§7 Discussion 坦率定位 systems contribution\"\n      assigned_to: paper_agent\n      status: completed\n    - round: 21\n      action: \"更明确论证 semantic layer 的非显而易见设计选择（grammar-first fallback 策略、greedy limitation cascade），凸显 decode-time 执行不可替代性\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R16-W1\"\n  summary: \"κ̄/enabling dependency 统计支撑不足：R²=0.886 基于 n=6\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 21\n  mentions:\n    - round: 19\n      reviewers: [1, 2]\n      note: \"R19: 删除 §5.2/§7/Limitations 中的 κ̄，限制在 §4。\"\n    - round: 20\n      reviewers: [1]\n      note: \"R20: κ̄ 仍在 §4 占一段且在 abstract 出现。\"\n    - round: 21\n      reviewers: [1, 2]\n      note: \"R21: R1-W4 (Minor) + R2-Q4 共识。'Empirical enabling dependency' 术语过强，n=6 无法支撑因果性术语。建议改为 'observed pattern' 或 'consistent trend'。R²=0.886 需 leave-one-out CV 或 adjusted R²。\"\n  action_items:\n    - round: 20\n      action: \"从 abstract 删除 κ̄；§4 段压至 2-3 句标注 preliminary\"\n      assigned_to: paper_agent\n      status: completed\n    - round: 21\n      action: \"'Empirical enabling dependency' 改为 'observed complementarity pattern'；补充 adjusted R² 或 leave-one-out CV\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R20-W1\"\n  summary: \"Proposition 1 证明中 position→name 转换缺乏形式论证\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 20\n  last_seen_round: 21\n  mentions:\n    - round: 20\n      reviewers: [1]\n      note: \"R1-W3。Appendix O 承认 core argument transfers 但未给形式论证。\"\n    - round: 21\n      reviewers: [1]\n      note: \"R21: R1-W5 (Minor)。R2 REBUT 认为简化合理不影响核心结论。分歧存在但 severity 较低。\"\n  action_items:\n    - round: 20\n      action: \"Appendix O 加 2-3 句 informal argument：name-based ⊇ position-based\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R21-N1\"\n  summary: \"Zero-shot 核心消融（Table 1）缺乏统计检验\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 21\n  last_seen_round: 21\n  mentions:\n    - round: 21\n      reviewers: [1, 2]\n      note: \"R1-N1 (Critical)：Table 1 仅有点估计，无 bootstrap CI/配对检验/效应量。R2 REBUT：greedy 解码确定性，传统 CI 无意义；已有 Table 31 (document-level CI) + Table 35 (prompt sensitivity)。分歧：R1 认为缺统计检验削弱 enabling dependency 主张；R2 认为确定性过程不需传统 CI 但 document-level bootstrap 作为补充合理。\"\n  action_items:\n    - round: 21\n      action: \"在 Table 1 caption 或 §5.1 中显式声明 greedy decoding 是确定性过程；引用 Table 31/35 作为 robustness 参考；可选：补充 document-level bootstrap CI\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R21-N2\"\n  summary: \"Full FT 组合性解读分歧——R-F1 不变是否意味约束无效\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 21\n  last_seen_round: 21\n  mentions:\n    - round: 21\n      reviewers: [1, 2]\n      note: \"R1-N2 (Critical)：Table 42 full FT + S1 R-F1=37.89 与 unconstrained 相同，认为约束'失效'。R2 详细 REBUT：full FT unconstrained 仍有 DR=2.74%，S1 使 DR→0% 且 F1 不变——这恰恰是理想结果。R1 的解读将 F1 不变混淆为约束无效，实际约束在 violation reduction 上完全有效。R2 的 rebuttal 有数据支撑。\"\n  action_items:\n    - round: 21\n      action: \"正文或 Appendix L 中更显式报告 full FT unconstrained 的 DR/CF（已有但不够突出），明确 composability 评估以 LoRA 为主\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R21-W2\"\n  summary: \"缺乏与 GoLLIE/KnowCoder/ADELIE 的正面 violation rate 对比\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 21\n  last_seen_round: 21\n  mentions:\n    - round: 21\n      reviewers: [1, 2]\n      note: \"R1-W3 (Major)。R2 REBUT：跨范式方法正面实验对比不可行（不同训练流程/模型/prompt），间接对比（§6 GoLLIE R-F1=0.0）和 GCD-equivalent baseline（Table 16-17）足够。分歧存在。\"\n  action_items:\n    - round: 21\n      action: \"可选：在 Related Work 中增加表格系统对比不同方法的 violation handling 策略和已报告的 violation rates（引用原文数据）\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R15-MF3\"\n  summary: \"正文溢出至第 9 页\"\n  category: format\n  severity: critical\n  status: open\n  first_raised_round: 13\n  last_seen_round: 21\n  mentions:\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R15: 正文溢出第 9 页。\"\n    - round: 18\n      note: \"R18 标记为 resolved（正文 ≤ 8 页）。\"\n    - round: 20\n      reviewers: [2]\n      note: \"R20: §7 溢出至 page 9 约 13 行。\"\n    - round: 21\n      note: \"R21: 本轮未被任何 Reviewer 独立提及，可能已修复，待 Research Director 确认。\"\n  action_items:\n    - round: 20\n      action: \"压缩 §7\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R20-N1\"\n  summary: \"Corollary 标签混淆形式推导与经验观察\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 20\n  last_seen_round: 21\n  mentions:\n    - round: 20\n      reviewers: [1, 2]\n      note: \"R1-N1 + R2-N3 共识。Corollary→Empirical Observation。\"\n    - round: 21\n      note: \"R21: 本轮未被独立提及。与 R16-W1 (enabling dependency terminology) 相关——R21 R1-W4 建议将 'empirical enabling dependency' 改为 'observed pattern'。\"\n  action_items:\n    - round: 20\n      action: \"Corollary→Empirical Observation；§3 加 scale-dependent 限定\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R20-W2\"\n  summary: \"DocRED 评估使用开发集，超参数选择过程未披露\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 20\n  last_seen_round: 21\n  mentions:\n    - round: 20\n      reviewers: [1]\n      note: \"R1-W4。LoRA 超参选择策略未说明。\"\n    - round: 21\n      note: \"R21: R1 小问题重申 DocRED dev set 应在 Limitations 中声明。R2 AGREE。\"\n  action_items:\n    - round: 20\n      action: \"§5 加一句 LoRA 超参说明\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 21\n      action: \"Limitations 中显式声明 DocRED 使用 dev set 评估\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R20-W3\"\n  summary: \"Bonferroni 校正后最小 p=0.014 处于 borderline\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 20\n  last_seen_round: 21\n  mentions:\n    - round: 20\n      reviewers: [1]\n      note: \"R1-W5。补 per-config p-values + Cohen's d。\"\n    - round: 21\n      note: \"R21: 本轮未独立提及，可能已修复，待确认。\"\n  action_items:\n    - round: 20\n      action: \"Appendix bootstrap CI 部分报告各配置独立 p 值和 Cohen's d\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R20-W4\"\n  summary: \"主文 Related Work §6 过于精简，ADELIE 缺失\"\n  category: related_work\n  severity: info\n  status: open\n  first_raised_round: 20\n  last_seen_round: 21\n  mentions:\n    - round: 20\n      reviewers: [2]\n      note: \"R2-W2。ADELIE 缺失；PICARD 对比不足；SGLang 未提及。\"\n    - round: 21\n      note: \"R21: R2 missing references 提及 Text2Event (Lu et al., 2021) 和 DEGREE (Hsu et al., 2022)。R1 认为 Text2Event 部分相关（WikiEvents EE 上下文），DEGREE 非必要。\"\n  action_items:\n    - round: 20\n      action: \"§6 提升 ADELIE 到正文；扩展 PICARD 对比；提及 SGLang\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 21\n      action: \"考虑补充 Text2Event 引用（与 WikiEvents EE 实验相关）\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R18-M2\"\n  summary: \"Figure 1 视觉层次不够分明 + 未可视化 fallback 路径\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 18\n  last_seen_round: 21\n  mentions:\n    - round: 18\n      reviewers: [1, 2]\n      note: \"R18: 小问题。\"\n    - round: 21\n      reviewers: [1, 2]\n      note: \"R21: R1 小问题 + R2 AGREE。Grammar-first fallback 是 §4 Eq.2 核心设计，应在 Figure 1 中体现。\"\n  action_items:\n    - round: 21\n      action: \"Figure 1 中增加 grammar-first fallback 路径可视化\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R20-W5\"\n  summary: \"Running example 仍不充分\"\n  category: writing\n  severity: info\n  status: wont_fix\n  first_raised_round: 20\n  last_seen_round: 21\n  mentions:\n    - round: 20\n      reviewers: [2]\n      note: \"R2-W3。需贯穿 §3-§4 的完整 example。\"\n    - round: 21\n      note: \"R21: 本轮未提及。\"\n  action_items: []\n  resolution: \"空间限制无法在正文加完整 running example。§3.3 有 Used-for 示例，appendix 有 case studies。\"\n  resolution_round: 20\n\n- id: \"R20-W6\"\n  summary: \"Zero-shot 评估实际意义有限（R-F1 仅 4-8%）\"\n  category: experiment\n  severity: info\n  status: wont_fix\n  first_raised_round: 20\n  last_seen_round: 21\n  mentions:\n    - round: 20\n      reviewers: [2]\n      note: \"R2-W4。ZS 定位为 diagnostic probe 合理但篇幅偏多。\"\n    - round: 21\n      note: \"R21: 本轮未提及。\"\n  resolution: \"ZS 已定位为 diagnostic probe，篇幅已压缩。\"\n  resolution_round: 20\n\n# ============================================================\n# Round 20 及更早 Resolved\n# ============================================================\n\n- id: \"R19-W1\"\n  summary: \"遗漏 2026 年初高相关 constrained decoding 工作\"\n  category: related_work\n  severity: warning\n  status: resolved\n  first_raised_round: 19\n  last_seen_round: 20\n  resolution: \"§6 已添加 DCCD 和 Thinking Before Constraining 引用和讨论。\"\n  resolution_round: 19\n\n- id: \"R19-W2\"\n  summary: \"Enabling dependency 验证存在混淆变量\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 19\n  last_seen_round: 19\n  resolution: \"appendix_discussion.tex 已添加 enabling dependency confound analysis。\"\n  resolution_round: 19\n\n- id: \"R19-M1\"\n  summary: \"信息密度极高，缺少 running example\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 19\n  last_seen_round: 20\n  resolution: \"§3.3 已添加 Used-for running example。\"\n  resolution_round: 19\n\n- id: \"R17-W3\"\n  summary: \"Entity registry 顺序依赖未实验量化\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 20\n  resolution: \"entity_order_ablation 完成：shuffle 产生 byte-identical outputs。\"\n  resolution_round: 19\n\n- id: \"R19-W3\"\n  summary: \"主表缺少外部约束解码 baseline 行\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 19\n  last_seen_round: 20\n  resolution: \"vLLM guided_json 实验完成并写入主文。\"\n  resolution_round: 19\n\n- id: \"R19-W4\"\n  summary: \"Proposition 1 实践影响力表述可进一步精确\"\n  category: framing\n  severity: info\n  status: resolved\n  first_raised_round: 19\n  last_seen_round: 19\n  resolution: \"已添加 'for unbounded entity sets' 限定词 + Remark 区分。\"\n  resolution_round: 19\n\n- id: \"R15-MF1\"\n  summary: \"缺少与 GCD/BoostCD/GoLLIE 等同类方法的直接实验对比\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 18\n  resolution: \"vLLM guided_json 实验完成。\"\n  resolution_round: 19\n\n- id: \"R18-MF1\"\n  summary: \"引用错误：Cotti et al. 2025 多处与实际论文不符\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 18\n  resolution: \"4 条 bib 修正 + 全部 60 条引用审计。\"\n  resolution_round: 19\n\n- id: \"R16-MF2\"\n  summary: \"Abstract/Intro DR 降幅范围自相矛盾\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 18\n  resolution: \"DR range 按数据集拆分报告。\"\n  resolution_round: 19\n\n- id: \"R18-W1\"\n  summary: \"'四个模型(7-70B)'声称具有误导性\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 18\n  resolution: \"改为 '3 8B-class models with preliminary 70B validation'。\"\n  resolution_round: 19\n\n- id: \"R18-W2\"\n  summary: \"Zero-shot 实验篇幅占比过大\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 18\n  resolution: \"ZS 压缩至 ~1.65 页，定位为 diagnostic probe。\"\n  resolution_round: 19\n\n- id: \"R18-W3\"\n  summary: \"Abstract 数值密度过高 + DR 42-99% 范围过宽\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 18\n  resolution: \"DR range 按数据集拆分报告。\"\n  resolution_round: 19\n\n- id: \"R18-W4\"\n  summary: \"GCD-equivalent baseline 对比藏在 appendix\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 18\n  resolution: \"主文 §5 新增 vLLM guided_json 段落。\"\n  resolution_round: 19\n\n- id: \"R17-W3-prop1\"\n  summary: \"Proposition 1 有限 entity set caveat 在主文中缺失\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 18\n  resolution: \"§3 新增 Remark (finite entity sets)。\"\n  resolution_round: 19\n"
  }
}
```

</details>

---


### Tool result

_source line 2176 · 2026-05-23T03:02:10.239210+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_issues.yaml\", \"bytes\": 17518}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 2177 · 2026-05-23T03:04:52.351197+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "schema_semantic_constrained_ie",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.5 - Borderline Conference",
  "review_chat_id": "oc_01fc90ae186a4ed432770f7601995139",
  "report": "\n# Round 21 审稿报告 — OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints\n\n**Target Venue**: EMNLP 2026 via ARR May 2026\n**Reviewers**: R1（方法严谨性 + 实验设计 + 统计检验）、R2（新颖性 + Related Work + 写作质量）\n**流程**: Round 1 独立审稿 → 交叉分享（逐条 AGREE/REBUT）→ 收敛\n\n---\n\n## Summary\n\n论文提出 OntoCoDec，将 IE 本体编译为可组合的 token 级解码约束。两层架构：grammar layer（CFG，保证 JSON 结构和词汇约束）+ semantic layer（有状态实体注册表，运行时执行 domain/range 类型检查）。Proposition 1 形式化证明 domain/range 约束非 context-free，为二层分离提供理论基础。实验覆盖 3 个数据集（SciERC, DocRED, WikiEvents）、3 个 8B 模型 + 70B 验证、zero-shot 与 fine-tuning，展示 DR 降至 <0.1%（fine-tuned）。评估规模罕见（38 页 47+ 表格），分析深度突出（CF↔DR trade-off、组合性分析、error taxonomy）。\n\n---\n\n## Strengths\n\n**S1. 理论基础严谨** [R1+R2 共识]\nProposition 1 使用泵引理正式证明 domain/range 约束对无界实体集不是 context-free，Appendix O 完整证明逻辑链无可挑剔。这为 grammar 层之上需要第二层提供了不可简化的形式论据，解释了为什么 GCD/BoostCD 等纯 CFG 方法仅能达到 ~3% DR reduction。\n\n**S2. 约束组合框架设计精巧** [R1+R2 共识]\n§4 Eq. 2 的非对称合取 M_final(t) = M_grammar(t) ∩ M_semantic(t)，配合 grammar-first fallback（S(t)∩G(t)=∅ 时 fallback 到 G(t)），在理论完备性和工程可行性之间取得正确平衡。\n\n**S3. 评估规模在约束解码文献中罕见** [R1+R2 共识]\n38 页 47+ 表格，覆盖 5-way zero-shot ablation、4-way fine-tuning composability、跨数据集/跨模型/跨规模验证、beam search 兼容性、runtime profiling、error taxonomy、schema ambiguity analysis 等。\n\n**S4. 诊断指标体系设计良好** [R1]\nDR/CF/RoV/ET/RV 提供了比 F1 更细粒度的约束执行评估，使读者能精确定位各约束层的贡献。\n\n**S5. 统计报告有亮点** [R1+R2 共识]\nFine-tuning 结果正确使用 Bonferroni 校正（k=4, α=0.0125），诚实报告 R-F1 改善在校正后不显著，而 DR reduction 均显著（all p < 0.003）。这种透明度在该领域不常见。\n\n**S6. 组合性分析框架有独立价值** [R1+R2 共识]\n双因素定量分析（Figure 2）揭示 schema tightness (κ̄) × baseline violation rate 共同支配 DR reduction，R²=0.886，为实践者提供可操作指导。（但 n=6 统计可靠性有限——见 W5。）\n\n**S7. 错误分析深入且诚实** [R1]\nAppendix J 的 error taxonomy + Appendix K 的 lucky violation 分析 + Appendix N 的 schema ambiguity 分析展示了对问题的深入理解和科学严谨性。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**MF1. Abstract 对 CF 副作用的选择性报告** [R2-W1, Major; R1 AGREE]\nAbstract 报告 \"up to 1.18% under greedy decoding on well-calibrated models\"，选择了 CF 的最优情况。Table 1 显示 CF 实际范围为 0.08–12.02%（DocRED, Qwen, zero-shot S2 配置可达 ~10%；Limitations 承认 \"up to 12.02%\"）。通过限定 \"well-calibrated models\" 和 \"greedy decoding\" 两个条件选择性报告最低值，误导读者对方法代价的第一印象。\n- **两位 Reviewer 共识**：Abstract 应呈现 CF 的完整范围（如 \"0.46–12.02% depending on model calibration\"），保留 beam search 和 fine-tuning 作为缓解方案的描述。\n- **严重程度**：这是一个信任度问题。从 Round 15 至今（7 轮）反复出现的持续性问题——每轮修改后仍被审稿人标记。\n\n### Should-Fix（影响评分）\n\n**SF1. WikiEvents 评估统计效力不足** [R1-W1, Major; R2-W6, Minor; 共识]\nWikiEvents 仅 20 篇文档（n=246 gold triples），Table 31 CI 为 ±3.0pp，§5.4 报告的 argument F1 shift ±1.1pp 完全在噪声范围内。论文自称 \"preliminary\" 但仍在 §5 中作为四大实验之一呈现，并列入 contribution list。\n- 建议：(1) 从 Abstract 删除 WikiEvents 数据；(2) contribution list 中标注初步性质；(3) 正文中明确定位为 pilot study。\n\n**SF2. 70B AWQ INT4 量化混淆因素未控制** [R1-W2, Major; R2 AGREE]\n所有 70B 实验使用 AWQ INT4 量化（仅 Llama-3.1-70B），约束解码直接操作 logit 分布，量化可能在 mask 边界处扭曲 logits。Limitations 中仅一句带过。70B semantic-only 的 84% DR reduction 这一关键发现的可信度受此影响。\n- 建议：在 8B 上对比 FP16 vs INT4 的 DR/CF 指标，量化 quantization artifact 影响。即使小规模实验也能大幅增强 70B 结论可信度。\n\n**SF3. Abstract 信息密度过高** [R2-W3, Minor; R1 AGREE]\nAbstract ~150 词中包含 12+ 数字/百分比和 5+ 首次出现缩写（DR, CF, RE, R-F1, LoRA），冷读极为困难。顶会 Abstract 最佳实践：≤3-5 个关键数字 + 定性描述。\n- 建议：三段式结构（问题 → 方法 → 关键结果），减至 4-5 个 headline 数字。\n\n**SF4. Abstract/Intro DR 范围不一致** [R2-W4, Minor; R1 AGREE]\nAbstract \"42–90% on DocRED\" vs Introduction \"42–99% across models and datasets\"——虽然后者是跨数据集合并范围，但并列造成不必要混淆。\n\n**SF5. \"Enabling dependency\" 术语过强** [R1-W4, Minor; R2 AGREE]\n\"Empirical enabling dependency\" 在 §5.1 中用于描述 n=6 配置的观察。R²=0.886 基于 6 个点可能严重过拟合。\n- 建议：改为 \"observed complementarity pattern\"；补充 adjusted R² 或 leave-one-out CV。\n\n---\n\n## Reviewer Consensus [AGREE]\n\n以下问题两位 Reviewer 达成完全共识：\n\n1. **Overall 3.5 Borderline Conference**——理论扎实、评估全面，但 novelty ceiling 和统计检验问题制约接收信心\n2. **Abstract CF 选择性报告是信任度问题**（MF1）\n3. **WikiEvents n=20 统计效力不足**（SF1），不应在 Abstract/contribution 中引用\n4. **70B AWQ INT4 是未控制的混淆因素**（SF2）\n5. **Abstract 信息密度过高**（SF3）\n6. **DR 范围数值不一致需修正**（SF4）\n7. **κ̄/enabling dependency 术语过强**（SF5）\n8. **Figure 1 应可视化 grammar-first fallback 路径**\n9. **DocRED dev set 评估应在 Limitations 中声明**\n10. **评估规模和诊断指标体系是论文亮点**\n\n---\n\n## Reviewer Divergence [REBUT]\n\n以下问题存在分歧，各方理由如下：\n\n### D1. Zero-shot 核心消融（Table 1）是否需要统计检验\n- **R1 立场** [Critical Must-Fix]：Table 1 的 5 配置 × 2 模型 × 3 数据集消融仅有点估计，无 CI/显著性检验/效应量。Enabling dependency 主张缺乏统计证据。Fine-tuning 部分（Table 8）已正确使用 Bonferroni 校正，与 zero-shot 部分形成不一致。\n- **R2 立场** [REBUT]：Zero-shot greedy 解码是确定性过程（temperature=0，固定权重+prompt），bootstrap CI 在统计学上无意义。跨模型变异（3 models × 2 datasets）已提供 robustness。Table 31 (document-level CI) + Table 35 (prompt sensitivity) 已覆盖。建议在 Table 1 caption 中声明确定性并引用 robustness 参考。\n- **Director 判断**：R2 的 rebuttal 在统计学原理上有道理——确定性过程确实不需要传统 CI。但 R1 的关切也有效——读者可能期望一致的统计标准。折中方案：声明确定性 + 引用已有 robustness 证据 + 可选补充 document-level bootstrap。降级为 Should-Fix。\n\n### D2. Full FT 组合性是否\"失效\"（Table 42）\n- **R1 立场** [Critical Must-Fix]：Full FT + S1 的 R-F1（37.89）与 unconstrained 完全相同，约束\"零贡献\"。如果 full FT 已内化约束，对 \"decoding-time enforcement is necessary\" 构成反证。\n- **R2 立场** [REBUT with data]：Table 42 数据显示 full FT unconstrained 仍有 DR=2.74%（高于 LoRA 的 1.18%），S1 使 DR→0% 且 F1 不变。R1 将\"F1 不变\"误读为\"约束无效\"，但 DR→0% 恰恰是约束有效的证明。F1 不变 + DR→0% 是理想结果。\n- **Director 判断**：R2 的 rebuttal 有数据支撑，R1 的解读确实混淆了 F1 不变与约束无效。但论文可在 Appendix L 中更显式突出 full FT 的 DR 数据。降级为 info。\n\n### D3. 核心技术新颖性评判\n- **R2 立场** [Major]：Grammar layer 等价于 GCD/BoostCD（Table 17 确认），semantic layer 本质是运行时查表。Proposition 1 被 Remark 削弱（实际语言 regular，只是 DFA 太大）。论文自述 \"systematic engineering contribution with theoretical grounding\"——novelty ceiling 有限，更适合 Findings。\n- **R1 立场** [Partial REBUT]：Semantic layer 非简单查表——动态 entity registry 需解决 greedy commitment、fallback cascade、跨三元组类型一致性。Proposition 1 的 Remark 不削弱核心结论（CFG 不充分），而是补充 DFA 工程不可行性。但同意 novelty ceiling 存在。评价应为 \"moderate novelty with strong execution\"。\n- **Director 判断**：两方均有合理成分。核心技术确实是已知组件的组合（CFG + 运行时类型检查），但组合框架（Eq. 2 + fallback + composability）的设计选择非 trivial。论文自身 \"systematic engineering contribution\" 定位诚实。最终判断：novelty 处于 moderate 水平，不足以独立支撑 Conference acceptance，但强执行和分析深度弥补了部分 novelty 不足。\n\n### D4. 是否需要 GoLLIE/KnowCoder 正面对比\n- **R1 立场** [Major]：应在同一 benchmark 上对比 violation rates 或 F1。GoLLIE 在 SciERC、KnowCoder 在 DocRED 有公开结果。\n- **R2 立场** [REBUT]：跨范式（decoding-time vs training-based）正面实验对比不可行（不同训练流程/模型/prompt）。§6 已有间接对比（GoLLIE R-F1=0.0），Table 16-17 有 GCD-equivalent baseline。\n- **Director 判断**：R2 的可行性论点合理——完整复现 GoLLIE/KnowCoder 超出合理实验范围。但论文可在 Related Work 中增加系统性对比表格（引用原文数据），列出不同方法的 violation handling 策略。降级为可选改进。\n\n---\n\n## Questions\n\n1. **Beam search registry 管理**：k=8 时每个 beam 独立 registry 的内存开销是多少？Appendix F 报告了 latency 但未量化 memory。[R2-Q1, R1 AGREE]\n2. **TCR 整合可行性**：为什么不将 post-hoc TCR 整合到解码循环中？是否涉及 NP-hardness 的搜索空间问题？[R2-Q2, R1 AGREE]\n3. **GCD/BoostCD 运行方式**：Table 16-17 的对比是直接运行 GCD/BoostCD 代码，还是基于等价论证推断？[R2-Q3, R1 AGREE]\n4. **DR=0% 跨种子稳定性**：Table 2 Llama S1 SciERC DR=0% 是否仅 seed=42？其他种子是否仍 0%？[R1-Q4, R2 AGREE]\n5. **TCR vs OntoCoDec F1 对比**：TCR 减少 CF 18-92%，但对 DR 和 F1 影响未报告。TCR 是否是更实用的后处理替代？[R1-Q5, R2 AGREE]\n\n---\n\n## Missing References\n\n两位 Reviewer 提出的参考文献补充建议：\n1. **Text2Event** (Lu et al., 2021, ACL) — 序列生成事件抽取，与 WikiEvents 实验相关 [R2 提出, R1 部分同意]\n2. **Huang et al. (2024)** \"Planning for Constrained LLM Generation\" — look-ahead 约束解码，与 beam search 分析相关 [R1 提出]\n3. **DCCD (2026) 和 pldi2025_type_constrained_codegen** — venue/年份需核实是否已发表 [R2 提出, R1 同意]\n4. DEGREE (Hsu et al., 2022, NAACL) — R2 提出但 R1 认为非必要（不涉及 constrained decoding）\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态**：未配置。项目 config 中 `external_review.paperreview_ai.enabled` 未设置，本轮未请求外部审稿。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**：done（耗时约 5 分钟）\n\n视觉审查发现（2 warning + 4 info）：\n\n**Warning:**\n- 主文 8 页仅 1 个 figure（Figure 1 架构图），其余全为 table。缺少结果可视化图（如核心指标的 bar chart 或消融趋势图），削弱视觉印象。建议将附录中 Figure 2（DR vs Schema Restrictiveness）或 Figure 4（Beam width ablation）的关键子图提升到主文。\n- Page 4 整页纯文本+公式（§3.2-3.4 + §4），在 Figure 1（p.3）和 Table 1（p.5）之间形成视觉空白页。\n\n**Info:**\n- Figure 1 内部分组件标签字号偏小，打印后可能接近可读性下限（建议 ≥ 8pt）\n- Page 7 包含 Table 3 + Table 4，页面密集但未溢出\n- 附录部分页面极度密集（p.25 四表、p.31 五表）\n- 最后一页仅填充约 1/3，可调整分页\n\n---\n\n## Overall Assessment\n\n**Overall: 3.5 — Borderline Conference**\n\n**评分理由**：\n\n论文解决了一个真实且重要的问题——LLM 生成的 IE 输出中 ontological violations 的系统性消除。Proposition 1 提供了严谨的理论基础（CFG 不充分），约束组合框架（Eq. 2）设计精巧，评估规模在约束解码文献中罕见。统计报告的诚实度（Bonferroni + 坦承 R-F1 不显著）是高标准的学术实践。\n\n但以下问题制约了接收信心：\n1. **Abstract CF 选择性报告**是跨 7 轮的持续性信任度问题\n2. **核心技术新颖性处于 moderate 水平**——个别组件不新（CFG ≈ GCD, 类型检查 ≈ 运行时断言），论文自述 \"systematic engineering contribution\" 准确但指出了 novelty ceiling\n3. **WikiEvents 统计效力不足**不应在 Abstract/contribution 中引用\n4. **70B AWQ INT4 混淆未控制**影响 scaling 结论可信度\n\n如果 MF1（Abstract CF framing）得到彻底修正，并补充 SF1-SF5 的改进，论文可推向 4.0（Conference）。当前状态处于 Conference 和 Findings 的交界。\n\n**ARR 维度评分**：\n\n| 维度 | R1 | R2 | 综合 |\n|------|-----|-----|------|\n| Soundness | 3.5/5 | 3.5/5 | 3.5/5 |\n| Excitement | 3.5/5 | 3/5 | 3.25/5 |\n| Reproducibility | 4/5 | 4/5 | 4/5 |\n| Confidence | 4/5 | 4/5 | 4/5 |\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- Contribution list 中 WikiEvents 结论应降级或标注 preliminary\n- \"42-99%\" 范围应与 Abstract 保持一致\n\n### §3 Method\n- Proposition 1 严谨有效；Remark 补充 DFA 工程不可行性合理\n- Semantic layer 的 greedy commitment 和 fallback cascade 设计选择可更显式论证其非显而易见性\n- \"Enabling dependency\"/\"Empirical Observation\" 标签应匹配证据强度\n\n### §4 Constraint Composition\n- κ̄ 分析基于 n=6，需补充 adjusted R² 或 leave-one-out CV\n- 术语从 \"enabling dependency\" 降级为 \"observed complementarity pattern\"\n\n### §5 Experiments\n- Table 1 应在 caption 声明 greedy 确定性并引用 robustness 参考（Table 31/35）\n- WikiEvents 明确定位为 pilot study\n- 70B 结论需加量化 disclaimer\n\n### §6 Related Work\n- 考虑补充 Text2Event 引用\n- PICARD 对比可在 Appendix B 中深化\n- 核实 DCCD/pldi2025 引用的 venue 和年份\n\n### §7 Discussion and Conclusion\n- 论文自述 \"systematic engineering contribution\" 定位准确，无需修改\n\n### Limitations\n- DocRED dev set 评估应显式声明\n- Full FT composability 数据（DR 2.74%→0%）应更突出呈现\n\n### 视觉建议（非评分项）\n- 正文仅 1 figure，建议从附录提升一个结果可视化图\n- Page 4 视觉空白，考虑提前 Table 1 或插入小型示意图\n- Figure 1 组件标签确保 ≥ 8pt\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "project": "schema_semantic_constrained_ie",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.5 - Borderline Conference",
    "review_chat_id": "oc_01fc90ae186a4ed432770f7601995139",
    "report": "\n# Round 21 审稿报告 — OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints\n\n**Target Venue**: EMNLP 2026 via ARR May 2026\n**Reviewers**: R1（方法严谨性 + 实验设计 + 统计检验）、R2（新颖性 + Related Work + 写作质量）\n**流程**: Round 1 独立审稿 → 交叉分享（逐条 AGREE/REBUT）→ 收敛\n\n---\n\n## Summary\n\n论文提出 OntoCoDec，将 IE 本体编译为可组合的 token 级解码约束。两层架构：grammar layer（CFG，保证 JSON 结构和词汇约束）+ semantic layer（有状态实体注册表，运行时执行 domain/range 类型检查）。Proposition 1 形式化证明 domain/range 约束非 context-free，为二层分离提供理论基础。实验覆盖 3 个数据集（SciERC, DocRED, WikiEvents）、3 个 8B 模型 + 70B 验证、zero-shot 与 fine-tuning，展示 DR 降至 <0.1%（fine-tuned）。评估规模罕见（38 页 47+ 表格），分析深度突出（CF↔DR trade-off、组合性分析、error taxonomy）。\n\n---\n\n## Strengths\n\n**S1. 理论基础严谨** [R1+R2 共识]\nProposition 1 使用泵引理正式证明 domain/range 约束对无界实体集不是 context-free，Appendix O 完整证明逻辑链无可挑剔。这为 grammar 层之上需要第二层提供了不可简化的形式论据，解释了为什么 GCD/BoostCD 等纯 CFG 方法仅能达到 ~3% DR reduction。\n\n**S2. 约束组合框架设计精巧** [R1+R2 共识]\n§4 Eq. 2 的非对称合取 M_final(t) = M_grammar(t) ∩ M_semantic(t)，配合 grammar-first fallback（S(t)∩G(t)=∅ 时 fallback 到 G(t)），在理论完备性和工程可行性之间取得正确平衡。\n\n**S3. 评估规模在约束解码文献中罕见** [R1+R2 共识]\n38 页 47+ 表格，覆盖 5-way zero-shot ablation、4-way fine-tuning composability、跨数据集/跨模型/跨规模验证、beam search 兼容性、runtime profiling、error taxonomy、schema ambiguity analysis 等。\n\n**S4. 诊断指标体系设计良好** [R1]\nDR/CF/RoV/ET/RV 提供了比 F1 更细粒度的约束执行评估，使读者能精确定位各约束层的贡献。\n\n**S5. 统计报告有亮点** [R1+R2 共识]\nFine-tuning 结果正确使用 Bonferroni 校正（k=4, α=0.0125），诚实报告 R-F1 改善在校正后不显著，而 DR reduction 均显著（all p < 0.003）。这种透明度在该领域不常见。\n\n**S6. 组合性分析框架有独立价值** [R1+R2 共识]\n双因素定量分析（Figure 2）揭示 schema tightness (κ̄) × baseline violation rate 共同支配 DR reduction，R²=0.886，为实践者提供可操作指导。（但 n=6 统计可靠性有限——见 W5。）\n\n**S7. 错误分析深入且诚实** [R1]\nAppendix J 的 error taxonomy + Appendix K 的 lucky violation 分析 + Appendix N 的 schema ambiguity 分析展示了对问题的深入理解和科学严谨性。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**MF1. Abstract 对 CF 副作用的选择性报告** [R2-W1, Major; R1 AGREE]\nAbstract 报告 \"up to 1.18% under greedy decoding on well-calibrated models\"，选择了 CF 的最优情况。Table 1 显示 CF 实际范围为 0.08–12.02%（DocRED, Qwen, zero-shot S2 配置可达 ~10%；Limitations 承认 \"up to 12.02%\"）。通过限定 \"well-calibrated models\" 和 \"greedy decoding\" 两个条件选择性报告最低值，误导读者对方法代价的第一印象。\n- **两位 Reviewer 共识**：Abstract 应呈现 CF 的完整范围（如 \"0.46–12.02% depending on model calibration\"），保留 beam search 和 fine-tuning 作为缓解方案的描述。\n- **严重程度**：这是一个信任度问题。从 Round 15 至今（7 轮）反复出现的持续性问题——每轮修改后仍被审稿人标记。\n\n### Should-Fix（影响评分）\n\n**SF1. WikiEvents 评估统计效力不足** [R1-W1, Major; R2-W6, Minor; 共识]\nWikiEvents 仅 20 篇文档（n=246 gold triples），Table 31 CI 为 ±3.0pp，§5.4 报告的 argument F1 shift ±1.1pp 完全在噪声范围内。论文自称 \"preliminary\" 但仍在 §5 中作为四大实验之一呈现，并列入 contribution list。\n- 建议：(1) 从 Abstract 删除 WikiEvents 数据；(2) contribution list 中标注初步性质；(3) 正文中明确定位为 pilot study。\n\n**SF2. 70B AWQ INT4 量化混淆因素未控制** [R1-W2, Major; R2 AGREE]\n所有 70B 实验使用 AWQ INT4 量化（仅 Llama-3.1-70B），约束解码直接操作 logit 分布，量化可能在 mask 边界处扭曲 logits。Limitations 中仅一句带过。70B semantic-only 的 84% DR reduction 这一关键发现的可信度受此影响。\n- 建议：在 8B 上对比 FP16 vs INT4 的 DR/CF 指标，量化 quantization artifact 影响。即使小规模实验也能大幅增强 70B 结论可信度。\n\n**SF3. Abstract 信息密度过高** [R2-W3, Minor; R1 AGREE]\nAbstract ~150 词中包含 12+ 数字/百分比和 5+ 首次出现缩写（DR, CF, RE, R-F1, LoRA），冷读极为困难。顶会 Abstract 最佳实践：≤3-5 个关键数字 + 定性描述。\n- 建议：三段式结构（问题 → 方法 → 关键结果），减至 4-5 个 headline 数字。\n\n**SF4. Abstract/Intro DR 范围不一致** [R2-W4, Minor; R1 AGREE]\nAbstract \"42–90% on DocRED\" vs Introduction \"42–99% across models and datasets\"——虽然后者是跨数据集合并范围，但并列造成不必要混淆。\n\n**SF5. \"Enabling dependency\" 术语过强** [R1-W4, Minor; R2 AGREE]\n\"Empirical enabling dependency\" 在 §5.1 中用于描述 n=6 配置的观察。R²=0.886 基于 6 个点可能严重过拟合。\n- 建议：改为 \"observed complementarity pattern\"；补充 adjusted R² 或 leave-one-out CV。\n\n---\n\n## Reviewer Consensus [AGREE]\n\n以下问题两位 Reviewer 达成完全共识：\n\n1. **Overall 3.5 Borderline Conference**——理论扎实、评估全面，但 novelty ceiling 和统计检验问题制约接收信心\n2. **Abstract CF 选择性报告是信任度问题**（MF1）\n3. **WikiEvents n=20 统计效力不足**（SF1），不应在 Abstract/contribution 中引用\n4. **70B AWQ INT4 是未控制的混淆因素**（SF2）\n5. **Abstract 信息密度过高**（SF3）\n6. **DR 范围数值不一致需修正**（SF4）\n7. **κ̄/enabling dependency 术语过强**（SF5）\n8. **Figure 1 应可视化 grammar-first fallback 路径**\n9. **DocRED dev set 评估应在 Limitations 中声明**\n10. **评估规模和诊断指标体系是论文亮点**\n\n---\n\n## Reviewer Divergence [REBUT]\n\n以下问题存在分歧，各方理由如下：\n\n### D1. Zero-shot 核心消融（Table 1）是否需要统计检验\n- **R1 立场** [Critical Must-Fix]：Table 1 的 5 配置 × 2 模型 × 3 数据集消融仅有点估计，无 CI/显著性检验/效应量。Enabling dependency 主张缺乏统计证据。Fine-tuning 部分（Table 8）已正确使用 Bonferroni 校正，与 zero-shot 部分形成不一致。\n- **R2 立场** [REBUT]：Zero-shot greedy 解码是确定性过程（temperature=0，固定权重+prompt），bootstrap CI 在统计学上无意义。跨模型变异（3 models × 2 datasets）已提供 robustness。Table 31 (document-level CI) + Table 35 (prompt sensitivity) 已覆盖。建议在 Table 1 caption 中声明确定性并引用 robustness 参考。\n- **Director 判断**：R2 的 rebuttal 在统计学原理上有道理——确定性过程确实不需要传统 CI。但 R1 的关切也有效——读者可能期望一致的统计标准。折中方案：声明确定性 + 引用已有 robustness 证据 + 可选补充 document-level bootstrap。降级为 Should-Fix。\n\n### D2. Full FT 组合性是否\"失效\"（Table 42）\n- **R1 立场** [Critical Must-Fix]：Full FT + S1 的 R-F1（37.89）与 unconstrained 完全相同，约束\"零贡献\"。如果 full FT 已内化约束，对 \"decoding-time enforcement is necessary\" 构成反证。\n- **R2 立场** [REBUT with data]：Table 42 数据显示 full FT unconstrained 仍有 DR=2.74%（高于 LoRA 的 1.18%），S1 使 DR→0% 且 F1 不变。R1 将\"F1 不变\"误读为\"约束无效\"，但 DR→0% 恰恰是约束有效的证明。F1 不变 + DR→0% 是理想结果。\n- **Director 判断**：R2 的 rebuttal 有数据支撑，R1 的解读确实混淆了 F1 不变与约束无效。但论文可在 Appendix L 中更显式突出 full FT 的 DR 数据。降级为 info。\n\n### D3. 核心技术新颖性评判\n- **R2 立场** [Major]：Grammar layer 等价于 GCD/BoostCD（Table 17 确认），semantic layer 本质是运行时查表。Proposition 1 被 Remark 削弱（实际语言 regular，只是 DFA 太大）。论文自述 \"systematic engineering contribution with theoretical grounding\"——novelty ceiling 有限，更适合 Findings。\n- **R1 立场** [Partial REBUT]：Semantic layer 非简单查表——动态 entity registry 需解决 greedy commitment、fallback cascade、跨三元组类型一致性。Proposition 1 的 Remark 不削弱核心结论（CFG 不充分），而是补充 DFA 工程不可行性。但同意 novelty ceiling 存在。评价应为 \"moderate novelty with strong execution\"。\n- **Director 判断**：两方均有合理成分。核心技术确实是已知组件的组合（CFG + 运行时类型检查），但组合框架（Eq. 2 + fallback + composability）的设计选择非 trivial。论文自身 \"systematic engineering contribution\" 定位诚实。最终判断：novelty 处于 moderate 水平，不足以独立支撑 Conference acceptance，但强执行和分析深度弥补了部分 novelty 不足。\n\n### D4. 是否需要 GoLLIE/KnowCoder 正面对比\n- **R1 立场** [Major]：应在同一 benchmark 上对比 violation rates 或 F1。GoLLIE 在 SciERC、KnowCoder 在 DocRED 有公开结果。\n- **R2 立场** [REBUT]：跨范式（decoding-time vs training-based）正面实验对比不可行（不同训练流程/模型/prompt）。§6 已有间接对比（GoLLIE R-F1=0.0），Table 16-17 有 GCD-equivalent baseline。\n- **Director 判断**：R2 的可行性论点合理——完整复现 GoLLIE/KnowCoder 超出合理实验范围。但论文可在 Related Work 中增加系统性对比表格（引用原文数据），列出不同方法的 violation handling 策略。降级为可选改进。\n\n---\n\n## Questions\n\n1. **Beam search registry 管理**：k=8 时每个 beam 独立 registry 的内存开销是多少？Appendix F 报告了 latency 但未量化 memory。[R2-Q1, R1 AGREE]\n2. **TCR 整合可行性**：为什么不将 post-hoc TCR 整合到解码循环中？是否涉及 NP-hardness 的搜索空间问题？[R2-Q2, R1 AGREE]\n3. **GCD/BoostCD 运行方式**：Table 16-17 的对比是直接运行 GCD/BoostCD 代码，还是基于等价论证推断？[R2-Q3, R1 AGREE]\n4. **DR=0% 跨种子稳定性**：Table 2 Llama S1 SciERC DR=0% 是否仅 seed=42？其他种子是否仍 0%？[R1-Q4, R2 AGREE]\n5. **TCR vs OntoCoDec F1 对比**：TCR 减少 CF 18-92%，但对 DR 和 F1 影响未报告。TCR 是否是更实用的后处理替代？[R1-Q5, R2 AGREE]\n\n---\n\n## Missing References\n\n两位 Reviewer 提出的参考文献补充建议：\n1. **Text2Event** (Lu et al., 2021, ACL) — 序列生成事件抽取，与 WikiEvents 实验相关 [R2 提出, R1 部分同意]\n2. **Huang et al. (2024)** \"Planning for Constrained LLM Generation\" — look-ahead 约束解码，与 beam search 分析相关 [R1 提出]\n3. **DCCD (2026) 和 pldi2025_type_constrained_codegen** — venue/年份需核实是否已发表 [R2 提出, R1 同意]\n4. DEGREE (Hsu et al., 2022, NAACL) — R2 提出但 R1 认为非必要（不涉及 constrained decoding）\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态**：未配置。项目 config 中 `external_review.paperreview_ai.enabled` 未设置，本轮未请求外部审稿。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**：done（耗时约 5 分钟）\n\n视觉审查发现（2 warning + 4 info）：\n\n**Warning:**\n- 主文 8 页仅 1 个 figure（Figure 1 架构图），其余全为 table。缺少结果可视化图（如核心指标的 bar chart 或消融趋势图），削弱视觉印象。建议将附录中 Figure 2（DR vs Schema Restrictiveness）或 Figure 4（Beam width ablation）的关键子图提升到主文。\n- Page 4 整页纯文本+公式（§3.2-3.4 + §4），在 Figure 1（p.3）和 Table 1（p.5）之间形成视觉空白页。\n\n**Info:**\n- Figure 1 内部分组件标签字号偏小，打印后可能接近可读性下限（建议 ≥ 8pt）\n- Page 7 包含 Table 3 + Table 4，页面密集但未溢出\n- 附录部分页面极度密集（p.25 四表、p.31 五表）\n- 最后一页仅填充约 1/3，可调整分页\n\n---\n\n## Overall Assessment\n\n**Overall: 3.5 — Borderline Conference**\n\n**评分理由**：\n\n论文解决了一个真实且重要的问题——LLM 生成的 IE 输出中 ontological violations 的系统性消除。Proposition 1 提供了严谨的理论基础（CFG 不充分），约束组合框架（Eq. 2）设计精巧，评估规模在约束解码文献中罕见。统计报告的诚实度（Bonferroni + 坦承 R-F1 不显著）是高标准的学术实践。\n\n但以下问题制约了接收信心：\n1. **Abstract CF 选择性报告**是跨 7 轮的持续性信任度问题\n2. **核心技术新颖性处于 moderate 水平**——个别组件不新（CFG ≈ GCD, 类型检查 ≈ 运行时断言），论文自述 \"systematic engineering contribution\" 准确但指出了 novelty ceiling\n3. **WikiEvents 统计效力不足**不应在 Abstract/contribution 中引用\n4. **70B AWQ INT4 混淆未控制**影响 scaling 结论可信度\n\n如果 MF1（Abstract CF framing）得到彻底修正，并补充 SF1-SF5 的改进，论文可推向 4.0（Conference）。当前状态处于 Conference 和 Findings 的交界。\n\n**ARR 维度评分**：\n\n| 维度 | R1 | R2 | 综合 |\n|------|-----|-----|------|\n| Soundness | 3.5/5 | 3.5/5 | 3.5/5 |\n| Excitement | 3.5/5 | 3/5 | 3.25/5 |\n| Reproducibility | 4/5 | 4/5 | 4/5 |\n| Confidence | 4/5 | 4/5 | 4/5 |\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- Contribution list 中 WikiEvents 结论应降级或标注 preliminary\n- \"42-99%\" 范围应与 Abstract 保持一致\n\n### §3 Method\n- Proposition 1 严谨有效；Remark 补充 DFA 工程不可行性合理\n- Semantic layer 的 greedy commitment 和 fallback cascade 设计选择可更显式论证其非显而易见性\n- \"Enabling dependency\"/\"Empirical Observation\" 标签应匹配证据强度\n\n### §4 Constraint Composition\n- κ̄ 分析基于 n=6，需补充 adjusted R² 或 leave-one-out CV\n- 术语从 \"enabling dependency\" 降级为 \"observed complementarity pattern\"\n\n### §5 Experiments\n- Table 1 应在 caption 声明 greedy 确定性并引用 robustness 参考（Table 31/35）\n- WikiEvents 明确定位为 pilot study\n- 70B 结论需加量化 disclaimer\n\n### §6 Related Work\n- 考虑补充 Text2Event 引用\n- PICARD 对比可在 Appendix B 中深化\n- 核实 DCCD/pldi2025 引用的 venue 和年份\n\n### §7 Discussion and Conclusion\n- 论文自述 \"systematic engineering contribution\" 定位准确，无需修改\n\n### Limitations\n- DocRED dev set 评估应显式声明\n- Full FT composability 数据（DR 2.74%→0%）应更突出呈现\n\n### 视觉建议（非评分项）\n- 正文仅 1 figure，建议从附录提升一个结果可视化图\n- Page 4 视觉空白，考虑提前 Table 1 或插入小型示意图\n- Figure 1 组件标签确保 ≥ 8pt\n"
  }
}
```

</details>

---


### Tool result

_source line 2178 · 2026-05-23T03:04:57.126747+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_2216d5b8b87a9472ce204aba11481390:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4775
}
```

</details>

---


### Assistant

_source line 2179 · 2026-05-23T03:05:06.148063+00:00_

Round 21 审稿报告已投递。

**结果摘要**：

- **Overall 3.5 — Borderline Conference**（R1=3.5, R2=3.5，完全一致）
- **1 个 Must-Fix**：Abstract CF 选择性报告（跨 7 轮持续性问题）
- **5 个 Should-Fix**：WikiEvents 统计效力、70B 量化混淆、Abstract 信息密度、DR 范围不一致、enabling dependency 术语
- **4 个分歧点**已记录：zero-shot CI 必要性、Full FT 组合性解读、novelty 评判、GoLLIE 对比必要性
- **Issue Tracker** 已同步更新（16 个 active issues，12 个 resolved）
- **视觉审查** 已纳入报告（2 warning + 4 info）
- **外部审稿** 未配置

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director"
}
```

</details>

---


## Round 162

## Round 162

2 recorded events


### User

_source line 2180 · 2026-05-23T03:05:08.236241+00:00_

[Reviewer 2 审稿结果]:
交叉回应要点总结：

- **N1 (zero-shot CI)**: 反驳——greedy decoding 是确定性过程，传统 CI 不适用；论文已有 prompt sensitivity (Table 35) 和 document-level precision (Table 31) 作为 robustness 证据
- **N2 (full FT composability 失效)**: 反驳——R1 对 Table 42 的解读有误。Full FT unconstrained 仍有 2.74% DR，S1 将其降至 0%，这正是 composability 的证明而非失效
- **W1-W2**: 同意（WikiEvents n=20 不足、70B 量化混淆）
- **W3 (GoLLIE 对比)**: 反驳——跨范式正面实验不可行，间接对比+GCD baseline 已足够
- **W4-W5**: 同意术语过强；反驳 Proposition 1 简化问题（不影响核心结论）
- **Overall**: 与 R1 趋同于 3.5，但在 N2 和 N1 两个 Critical 问题上有实质性分歧

---

[飞书用户 贾骁涵 (ou_a4dc71c11b6b25e205bae4bd9a8021b5)]: 目前的审稿得分是什么样

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 2181 · 2026-05-23T03:05:26.509221+00:00_

**Round 21 审稿结果已提交。**

两位 Reviewer 一致评分 **3.5 — Borderline Conference**。

综合维度评分：

| 维度 | R1 | R2 | 综合 |
|---|---|---|---|
| Soundness | 3.5/5 | 3.5/5 | 3.5/5 |
| Excitement | 3.5/5 | 3/5 | 3.25/5 |
| Reproducibility | 4/5 | 4/5 | 4/5 |

**核心瓶颈**（按优先级）：

1. **Abstract CF 选择性报告**（从 R15 至今跨 7 轮未彻底解决）——报告 1.18% 而实际范围达 12.02%
2. **Novelty ceiling**——核心技术是已知组件组合（CFG + 运行时类型检查），R1 评 moderate、R2 评 limited
3. **WikiEvents n=20 统计效力不足**——不应在 Abstract/contribution 中引用
4. **70B AWQ INT4 量化混淆未控制**

**Reviewer 间存在分歧的问题**（已在报告中记录）：
- R1 认为 zero-shot 消融缺统计检验是 Critical，R2 反驳 greedy 是确定性过程不需要 CI
- R1 认为 Full FT composability "失效"是 Critical，R2 用 Table 42 数据反驳（DR 2.74%→0%，约束有效）

**推向 4.0 (Conference) 的路径**：修正 Abstract CF framing + 精简 Abstract 信息密度 + WikiEvents 降级 + 补充 70B quantization disclaimer。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director"
}
```

</details>

---


## Round 163

## Round 163

76 recorded events


### User

_source line 2182 · 2026-05-23T03:33:51.368587+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: schema_semantic_constrained_ie
- 论文路径: /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex
- 目标 venue: EMNLP 2026
- 截止日期: 2026-05-25
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 2183 · 2026-05-23T03:33:56.869056+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 2184 · 2026-05-23T03:33:56.869891+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2185 · 2026-05-23T03:34:02.794916+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,read_project_file,dispatch_visual_check,request_external_review,get_external_review_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,get_visual_check_status,WebSearch,read_local_file",
  "max_results": "15"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,read_project_file,dispatch_visual_check,request_external_review,get_external_review_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,get_visual_check_status,WebSearch,read_local_file",
    "max_results": "15"
  }
}
```

</details>

---


### Tool result

_source line 2186 · 2026-05-23T03:34:02.795430+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2187 · 2026-05-23T03:34:05.858469+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,read_project_file,dispatch_visual_check,request_external_review,get_external_review_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,get_visual_check_status,mcp__agent-ml-research__read_local_file",
  "max_results": "15"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,read_project_file,dispatch_visual_check,request_external_review,get_external_review_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,get_visual_check_status,mcp__agent-ml-research__read_local_file",
    "max_results": "15"
  }
}
```

</details>

---


### Tool result

_source line 2188 · 2026-05-23T03:34:05.909263+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2189 · 2026-05-23T03:34:10.085234+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__read_local_file",
  "max_results": "15"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__read_local_file",
    "max_results": "15"
  }
}
```

</details>

---


### Tool result

_source line 2190 · 2026-05-23T03:34:10.126216+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "ToolSearch",
  "elapsed_ms": 40
}
```

</details>

---


### Tool call

_source line 2191 · 2026-05-23T03:34:14.594283+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "schema_semantic_constrained_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "schema_semantic_constrained_ie"
  }
}
```

</details>

---


### Tool result

_source line 2192 · 2026-05-23T03:34:15.951901+00:00_

{"result":"# 项目 schema_semantic_constrained_ie 概况\n\n## 实验状态 (158 个)\n\n- **llama_scierc_full_s1**: DONE (success) — \n- **llama_scierc_unconstrained**: DONE (success) — \n- **phase2_scierc_full_s1**: DONE (success) — \n- **phase2_scierc_semantic_only**: DONE (success) — \n- **phase2_scierc_grammar_only**: DONE (success) — \n- **phase2_scierc_unconstrained**: DONE (success) — \n- **phase2_docred_full_s1**: DONE (success) — \n- **phase2_docred_semantic_only**: DONE (success) — \n- **phase2_docred_unconstrained**: DONE (success) — \n- **mvp_phase0_docred_schema_r2**: DONE (killed) — \n- **phase2_s2_pilot50**: DONE (success) — \n- **mvp_phase0_docred_schema**: DONE (success) — \n- **mvp_phase0_violation_rate_docred**: DONE (success) — \n- **mvp_phase0_scierc_schema**: DONE (success) — \n- **mvp_phase0_violation_rate**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-23\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| eval_70b_lora_docred_200_full_s2 | Full S2 (grammar+semantic+repair) on 70B LoRA DocRED should achieve near-zero DR while maintaining R_F1 close to beam4_s1 (48.14). The repair layer resolves residual DR violations from S1. This is the strongest constraint configuration for DocRED LoRA. | — | — | — |\n\n## 待处理\n- r16_70b_lora_scierc_eval: 70B AWQ INT4 LoRA fine-tuned on SciERC will achieve higher R-F1 than 8B FT (Qwen 47.15, Llama 46.13) and S1 constraints will maintain DR→0% at 70B scale（准备中）\n- p1_llama_ee_ft（准备中）\n\n## 近期结论\n- **eval_70b_zs_docred_200_full_s1** (success): Full S1 (grammar+semantic) constraints on 70B ZS DocRED should achieve DR close to semantic_only (1.66%) since grammar adds zero DR contribution in ZS setting. R_F1 should remain ~13 (matching unconstrained 13.25). This completes the ZS DocRED ablation matrix. ← 基于 eval_70b_zs_docred_200_unconstrained\n- **eval_70b_lora_docred_200_grammar_only** (negative): Grammar-only constraints on 70B LoRA DocRED will
…[truncated 1408 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1357
}
```

</details>

---


### Tool call

_source line 2193 · 2026-05-23T03:34:16.454117+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 2194 · 2026-05-23T03:34:17.458347+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{graphicx}
11	\usepackage{booktabs}
12	\usepackage{multirow}
13	\usepackage[table]{xcolor}
14	\usepackage{amsmath}
15	\usepackage{amssymb}
16	\usepackage{amsthm}
17	\usepackage{enumitem}
18	\usepackage{pifont}
19	\usepackage{soul}
20	\usepackage{tikz}
21	\usetikzlibrary{arrows.meta,positioning,shapes.geometric,fit,backgrounds,calc}
22	\newcommand{\TBD}[1]{\textcolor{red}{#1}}
23	
24	\title{OntoCoDec: Type-Constrained Information Extraction\\via Compiled Schema Constraints}
25	
26	\author{Anonymous ACL submission}
27	
28	\begin{document}
29	\maketitle
30	
31	% === Abstract ===
32	\input{abstract}
33	
34	% === §1 Introduction ===
35	\input{section1_introduction_draft}
36	
37	% === §2 Background ===
38	\input{section2_background}
39	
40	% === §3 Method ===
41	\input{section3_method_draft}
42	
43	% === §4 Constraint Composition ===
44	\section{Constraint Composition}
45	\label{sec:composition}
46	\input{section4_composition_draft}
47	
48	% === §5 Experiments ===
49	\section{Experiments}
50	\label{sec:experiments}
51	
52	\input{section3_violation_landscape}
53	
54	\input{section5_scierc_draft}
55	\input{section5_docred_draft}
56	\input{section5_crossmodel_draft}
57	\input{section5_wikievents_draft}
58	\input{section5_runtime}
59	
60	% === §6 Related Work ===
61	\input{section6_related_work}
62	
63	% === §7 Discussion and Conclusion ===
64	\section{Discussion and Conclusion}
65	\label{sec:discussion}
66	\input{section7_conclusion_compressed}
67	
68	% === Limitations (ARR requirement: standalone section, does not count toward page limit) ===
69	\clearpage
70	\section*{Limitations}
71	
72	\paragraph{Constraint scope.}
73	CF impact is model-dependent: for well-calibrated models (Qwen, Llama; DR\,$\leq$\,1\% under greedy constrained decoding), S1 introduces CF violations (u
…[truncated 5633 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "elapsed_ms": 1004
}
```

</details>

---


### Tool call

_source line 2195 · 2026-05-23T03:34:17.559278+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers submission guidelines ARR site:aclweb.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission guidelines ARR site:aclweb.org"
  }
}
```

</details>

---


### Tool call

_source line 2196 · 2026-05-23T03:34:17.911354+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "schema_semantic_constrained_ie",
  "file": "paper_checklist.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "schema_semantic_constrained_ie",
    "file": "paper_checklist.yaml"
  }
}
```

</details>

---


### Tool result

_source line 2197 · 2026-05-23T03:34:25.090520+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines ARR site:aclweb.org"

Links: [{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"*SEM 2026: Commitment Link for ARR-Reviewed Papers (Deadline: 10 April 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/sem-2026-commitment-link-arr-reviewed-papers-deadline-10-april-2026"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"The 64th Annual Meeting of the Association for Computational Linguistics - ACL 2026","url":"https://2026.aclweb.org/"},{"title":"The 2nd BabyLM Workshop | ACL Member Portal","url":"https://www.aclweb.org/portal/content/2nd-babylm-workshop"},{"title":"Call for Papers: The 20th Linguistic Annotation Workshop (LAW XX), co-located with ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-20th-linguistic-annotation-workshop-law-xx-co-located-acl-2026"},{"title":"Jan. 2025 ACL Standing Committee on Peer Review (COPR) Report 1","url":"https://www.aclweb.org/adminwiki/images/9/9e/COPR-5-cycle-report-to-publish.pdf"}]

Based on the search results, I found information related to EMNLP 2026, though the main conference call for papers wasn't direc
…[truncated 1355 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "WebSearch",
  "elapsed_ms": 7531
}
```

</details>

---


### Tool result

_source line 2198 · 2026-05-23T03:34:25.091056+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'schema_semantic_constrained_ie'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 7179
}
```

</details>

---


### Tool call

_source line 2199 · 2026-05-23T03:34:30.216746+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 main conference call for papers submission deadline ARR commitment"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 main conference call for papers submission deadline ARR commitment"
  }
}
```

</details>

---


### Tool call

_source line 2200 · 2026-05-23T03:34:31.020562+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 submission guidelines page limit template anonymity"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 submission guidelines page limit template anonymity"
  }
}
```

</details>

---


### Tool call

_source line 2201 · 2026-05-23T03:34:33.430750+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex",
  "offset": "28",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex",
    "offset": "28",
    "limit": "80"
  }
}
```

</details>

---


### Tool result

_source line 2202 · 2026-05-23T03:34:33.782804+00:00_

28	\begin{document}
29	\maketitle
30	
31	% === Abstract ===
32	\input{abstract}
33	
34	% === §1 Introduction ===
35	\input{section1_introduction_draft}
36	
37	% === §2 Background ===
38	\input{section2_background}
39	
40	% === §3 Method ===
41	\input{section3_method_draft}
42	
43	% === §4 Constraint Composition ===
44	\section{Constraint Composition}
45	\label{sec:composition}
46	\input{section4_composition_draft}
47	
48	% === §5 Experiments ===
49	\section{Experiments}
50	\label{sec:experiments}
51	
52	\input{section3_violation_landscape}
53	
54	\input{section5_scierc_draft}
55	\input{section5_docred_draft}
56	\input{section5_crossmodel_draft}
57	\input{section5_wikievents_draft}
58	\input{section5_runtime}
59	
60	% === §6 Related Work ===
61	\input{section6_related_work}
62	
63	% === §7 Discussion and Conclusion ===
64	\section{Discussion and Conclusion}
65	\label{sec:discussion}
66	\input{section7_conclusion_compressed}
67	
68	% === Limitations (ARR requirement: standalone section, does not count toward page limit) ===
69	\clearpage
70	\section*{Limitations}
71	
72	\paragraph{Constraint scope.}
73	CF impact is model-dependent: for well-calibrated models (Qwen, Llama; DR\,$\leq$\,1\% under greedy constrained decoding), S1 introduces CF violations (up to 12.02\%) as a consequence of per-relation independent enforcement; for poorly-calibrated models (Mistral), S1 substantially reduces CF (56.87\%\,$\to$\,1.27\%) by constraining type assignments to schema-valid values.
74	CF fallback ablation shows that eliminating CF re-routes violations to DR ($+$13.85\,pp). CF$\leftrightarrow$DR thus represents a fundamental trade-off in composable constraint systems rather than an independently resolvable limitation (Appendix~\ref{app:cf-dr-tradeoff}).
75	Global entity-level type consensus during decoding offers the most direct path to resolving CF violations.
76	CF type inconsistencies may propagate to downstream tasks that consume extracted triples (e.g., knowledge graph constr
…[truncated 5702 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "elapsed_ms": 352
}
```

</details>

---


### Tool call

_source line 2203 · 2026-05-23T03:34:33.883868+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/",
  "description": "List paper directory contents"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/",
    "description": "List paper directory contents"
  }
}
```

</details>

---


### Tool result

_source line 2204 · 2026-05-23T03:34:34.085486+00:00_

_pdf_images
abstract.tex
abstract_d3264e.tex
abstract_fd4b26.tex
acl.sty
acl_natbib.bst
appendix_70b_ablation.tex
appendix_beam_search.tex
appendix_case_studies.tex
appendix_discussion.tex
appendix_doc_length.tex
appendix_downstream_analysis.tex
appendix_full_ft.tex
appendix_high_kappa_analysis.tex
appendix_kappa_case_study.tex
appendix_llama_per_relation.tex
appendix_order_invariance.tex
appendix_power_analysis.tex
appendix_power_analysis_523cc9.tex
appendix_prompt_sensitivity.tex
appendix_prompts.tex
appendix_pumping_lemma.tex
appendix_related_work.tex
appendix_reproducibility.tex
appendix_sampling_table.tex
appendix_scalability.tex
appendix_tcr.tex
appendix_type_consensus.tex.archived
case_study_kappa_dr.tex
checklist.tex
discussion_paragraphs.tex
discussion_paragraphs_cf83d1.tex
error_analysis_cases.json
fig1_framework.tex
figures
main.aux
main.bbl
main.blg
main.fdb_latexmk
main.fls
main.log
main.out
main.pdf
main.tex
new_citations.bib
ontocodec_paper_r10_final.pdf
ontocodec_paper_r9_final.pdf
p3_case_studies.tex
p3_case_studies_861a0d.tex
paper_tables_draft.tex
r12_fallback_cascade_text.txt
relwork_new_entries.bib
section1_introduction_draft.tex
section2_background.tex
section3_method_draft.tex
section3_violation_landscape.tex
section4_composition_draft.tex
section5_crossmodel_draft.tex
section5_docred_draft.tex
section5_docred_draft_9b84f1.tex
section5_runtime.tex
section5_scierc_draft.tex
section5_scierc_draft_4796e8.tex
section5_wikievents_draft.tex
section6_related_work.tex
section6_relwork_additions.tex
section6_relwork_outline.tex
section7_conclusion_550cbf_DEPRECATED.tex
section7_conclusion_DEPRECATED.tex
section7_conclusion_compressed.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Bash",
  "elapsed_ms": 201
}
```

</details>

---


### Tool result

_source line 2205 · 2026-05-23T03:34:35.189981+00:00_

Web search results for query: "EMNLP 2026 main conference call for papers submission deadline ARR commitment"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"emnlp 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=emnlp26"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"AI Conference Deadlines - Jie Cao | Dialogue, NLP, ML","url":"https://mlciv.com/ai-deadlines/"},{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"}]

Based on the search results, here's the information about EMNLP 2026 main conference call for papers submission deadline and ARR commitment:

## ARR Submission Deadline

The ARR submission deadline for EMNLP 2026 is May 25, 2026.

## ARR Commitment P
…[truncated 900 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "WebSearch",
  "elapsed_ms": 4973
}
```

</details>

---


### Tool result

_source line 2206 · 2026-05-23T03:34:36.947832+00:00_

Web search results for query: "ACL Rolling Review 2026 submission guidelines page limit template anonymity"

Links: [{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"Paper formatting guidelines - ACLPUB","url":"https://acl-org.github.io/ACLPUB/formatting.html"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"},{"title":"ACL ARR 2026 January | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR%2F2026%2FJanuary"}]

Based on my search results, here's information about ACL Rolling Review 2026 submission guidelines:

## Page Limits

Review versions of long papers may have up to eight (8) pages of content plus unlimited pages for references. Review versions of short papers may have up to four (4) pages of content, plus unlimited pages for references.

## Template Requirements

Paper submissions must use the official ACL style template. Additionally, ARR abandons the MS Word Template for conference submissions, and submissions based
…[truncated 845 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "WebSearch",
  "elapsed_ms": 5927
}
```

</details>

---


### Tool call

_source line 2207 · 2026-05-23T03:34:46.246940+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"EMNLP 2026\" \"call for papers\" page limit appendix submission format site:2026.emnlp.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"EMNLP 2026\" \"call for papers\" page limit appendix submission format site:2026.emnlp.org"
  }
}
```

</details>

---


### Tool call

_source line 2208 · 2026-05-23T03:34:48.003788+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 2209 · 2026-05-23T03:34:48.305319+00:00_

1	\begin{abstract}
2	Large language models for information extraction generate structurally valid but ontologically invalid triples---where entity types violate the ontology's domain/range constraints.
3	These violations persist across the capability spectrum and cannot be addressed by grammar-constrained decoding (which lacks cross-field type awareness) or post-hoc filtering (which discards valid predictions).
4	
5	We present \textsc{OntoCoDec}, a framework that compiles information extraction ontologies into composable token-level decoding constraints.
6	A decidability analysis shows that domain/range constraints exceed context-free expressiveness, yielding a two-layer architecture: a grammar layer enforces structural validity and vocabulary membership; a semantic layer enforces type constraints at runtime through stateful masking over a dynamic entity registry, with grammar-first fallback when constraints conflict.
7	
8	% exp_ids: w5_lora_scierc_constrained_eval, w5_qwen_docred_lora_constrained_eval, w5_llama_lora_scierc_constrained_eval, w5_llama_docred_lora_constrained_eval
9	Composed with LoRA fine-tuning across three 8B-class models and two relation extraction datasets (up to 96 relations), \textsc{OntoCoDec} near-eliminates domain/range violations ($<$\,0.1\%) at F1 41--47\%.
10	Under fine-tuning, this enforcement introduces cross-field type inconsistencies ($\leq$1.4\%) as a side effect of per-triple independent enforcement; beam search ($k{=}4$) eliminates all violation types at 1.54$\times$ latency.
11	In zero-shot settings, cross-field rates are higher (up to 12\%) but decrease with model calibration.
12	Zero-shot domain/range reductions span 76--99\% on SciERC and 42--90\% on DocRED, with a scale-dependent empirical relationship between the two layers: the semantic layer alone achieves substantially stronger reduction at larger model scale.
13	\end{abstract}
14	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 2210 · 2026-05-23T03:34:48.406135+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section1_introduction_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section1_introduction_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 2211 · 2026-05-23T03:34:49.259986+00:00_

1	% Section 1: Introduction (compressed, 669→~550 words)
2	
3	\section{Introduction}
4	\label{sec:introduction}
5	
6	Large language models are increasingly used for information extraction~\cite{li2023codeie,sainz2024gollie,wei2023zeroshot}, but when generating relation triples $(h, r, t)$, neither entity necessarily carries a type consistent with the ontology's domain/range constraints for $r$.
7	We call such outputs \emph{domain/range violations}: structurally valid triples that are ontologically invalid.
8	Violations persist across the capability spectrum: 15.4\% of triples on SciERC~\cite{luan2018scierc} and 18.5\% on DocRED~\cite{yao2019docred} under zero-shot decoding, and 0.5--2\% even after LoRA fine-tuning; rates correlate with schema restrictiveness (few valid type pairs per relation) rather than ontology or model scale.
9	At competitive quality (R-F1 41--47\%), even 1--2\% residual violations compound across thousands of documents into systematic knowledge graph corruption, making reliable constraint enforcement necessary.
10	
11	Existing approaches leave a fundamental gap.
12	Schema-informed prompting reduces violations by 62\% on average but is per-relation unreliable (violations for \textsc{Evaluate-for} actually \emph{increase} by 5.8\,pp).
13	Grammar-constrained decoding~\cite{dong2025xgrammar,willard2023outlines,beurer-kellner2023lmql} ensures syntactic well-formedness but cannot encode cross-field semantic constraints.
14	Post-hoc filtering discards up to 48\% of predictions including true positives (\S\ref{sec:cross-model}).
15	Training-based approaches~\cite{sainz2024gollie,lu2022uie} internalize schema knowledge but provide only soft guidance without runtime enforcement.
16	
17	We propose \textbf{OntoCoDec}, a framework that translates IE ontologies into composable layers of decoding-time constraints.
18	A decidability analysis of IE type constraints (\S\ref{sec:decidability}) yields a two-layer architecture: the \emph{grammar layer} compiles ont
…[truncated 2438 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "elapsed_ms": 853
}
```

</details>

---


### Tool call

_source line 2212 · 2026-05-23T03:34:49.360803+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_method_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_method_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 2213 · 2026-05-23T03:34:49.411767+00:00_

1	% Section 3 — Method (Draft)
2	% OntoCoDec: Type-Valid Information Extraction
3	% via Compiled Ontology Constraints
4	
5	\section{Method}
6	\label{sec:method}
7	
8	\input{fig1_framework}
9	
10	We present OntoCoDec, a framework that translates IE ontologies into token-level constraints enforced during autoregressive generation.
11	The design is guided by a decidability analysis of IE type constraints.
12	
13	\paragraph{Constraint decidability taxonomy.}
14	\label{sec:decidability}
15	We classify IE type constraints into three levels: (1)~\emph{context-free}: vocabulary membership and JSON structure; (2)~\emph{prefix-decidable with state}: domain/range type validity, determined at each type-bearing position given the decoded relation type and entity registry; (3)~\emph{non-local}: cross-entity type consistency, which depends on the full output.
16	Unlike code generation where types are statically declared, IE constraints fall into level~2: entity types are inferred from text, the registry is built dynamically, and constraint targets depend on the co-occurring relation.
17	OntoCoDec enforces levels 1--2 (grammar and semantic layers, respectively); level~3 is addressed by beam search or post-hoc resolution (Appendix~\ref{app:tcr}).
18	
19	\smallskip
20	\noindent
21	Existing grammar-constrained decoding frameworks (e.g., XGrammar) enforce level~1 constraints---structural validity and vocabulary membership---but IE domain/range rules require cross-position entity-type state that context-free grammars cannot express.
22	We formalize this gap:
23	
24	\smallskip
25	\noindent\textbf{Proposition 1} (Level 2 $\not\subseteq$ Level 1)\textbf{.}
26	\textit{Domain/range type constraints for IE with unbounded entity sets are not context-free.}
27	
28	\smallskip
29	\noindent\textit{Proof sketch.}
30	Consider $\mathcal{E} = \{\tau_A, \tau_B\}$ and a relation $r$ with $\operatorname{dom}(r) = \{\tau_A\}$.
31	An output contains $n$ entities with independently chosen types, followed by
…[truncated 7839 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 2214 · 2026-05-23T03:34:52.625925+00:00_

Web search results for query: ""EMNLP 2026" "call for papers" page limit appendix submission format site:2026.emnlp.org"

Links: [{"title":"Call for Papers: EMNLP 2026 Industry Track - EMNLP 2026","url":"https://2026.emnlp.org/calls/industry_track/"},{"title":"Call for Workshop Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/workshops/"},{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 Blog - EMNLP 2026","url":"https://2026.emnlp.org/blog/"},{"title":"Call for Tutorials - EMNLP 2026","url":"https://2026.emnlp.org/calls/tutorials/"},{"title":"The 2026 Conference on Empirical Methods in Natural Language Processing - EMNLP 2026","url":"https://2026.emnlp.org/"},{"title":"Physician- and Large Language Model-Generated Hospital Discharge Summaries: A Blinded, Comparative Quality and Safety Study","url":"https://www.medrxiv.org/content/10.1101/2024.09.29.24314562.full.pdf"}]

I found information from the EMNLP 2026 website. Here are the key details about page limits, appendices, and submission format:

## Main Conference Papers

The search results include information about the main conference call for papers at https://2026.emnlp.org/calls/main_conference_papers/, though the full page limit details weren't fully captured in the excerpt.

## Industry Track Papers

For the Industry Track specifically, Industry Track papers cannot exceed 6 pages in length (excluding ethical considerations and references).

Regarding appendices: Paper submissions must be fully self-contained, i.e., supplementary materials, as provided in the appendix, are completely optional, and reviewers are not even asked to review them. Additionally, references and limitations sections do not count toward the page limit, nor do the following optional sections: acknowledgements (only in the final version), ethical considerations, and appendices.

Submissions that do not conform to the required styles, includin
…[truncated 568 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "WebSearch",
  "elapsed_ms": 6378
}
```

</details>

---


### Tool call

_source line 2215 · 2026-05-23T03:34:59.109016+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section2_background.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section2_background.tex"
  }
}
```

</details>

---


### Tool result

_source line 2216 · 2026-05-23T03:34:59.962944+00:00_

1	% Section 2: Background (compressed)
2	
3	\section{Background}
4	\label{sec:background}
5	
6	\paragraph{IE Ontology Structure.}
7	\label{sec:bg:ontology}
8	An IE ontology $\mathcal{O} = (\mathcal{E}, \mathcal{R}, \sigma)$ defines entity types $\mathcal{E}$, relation types $\mathcal{R}$, and a mapping $\sigma: \mathcal{R} \to \mathcal{P}(\mathcal{E} \times \mathcal{E})$, where $\mathcal{P}(\cdot)$ denotes the power set, specifying valid (head type, tail type) pairs per relation.
9	A triple $(h, r, t)$ is \emph{type-valid} if $(\mathrm{type}(h), \mathrm{type}(t)) \in \sigma(r)$.
10	We quantify constraint restrictiveness via \emph{constraint tightness} $\kappa(r)$ (\S\ref{sec:composition}): tighter constraints leave fewer valid type pairs per relation.
11	We define ontology constraints broadly to encompass both formal ontology specifications (e.g., the KAIROS event ontology with explicit role-entity type mappings) and empirically derived type-pair constraints extracted from annotated training data.
12	The latter applies when datasets lack a formal ontology but provide typed annotations (SciERC, DocRED); OntoCoDec compiles both sources into the same constraint representation without modification.
13	Empirical constraints achieve 99\%+ instance-level coverage on held-out data (SciERC 99.0\%, DocRED 99.4\%); uncovered type pairs trigger grammar-first fallback (\S\ref{sec:composition}), ensuring no valid triples are blocked.
14	
15	\paragraph{Grammar-Constrained Decoding.}
16	\label{sec:bg:gcd}
17	Grammar-constrained decoding restricts each token $y_t$ to a mask $M_g \in \{0, 1\}^{|V|}$ derived from a target grammar.
18	XGrammar~\citep{dong2025xgrammar} compiles JSON Schemas into pushdown automata for efficient enforcement of structural constraints; Outlines~\citep{willard2023outlines} and SGLang~\citep{zheng2024sglang} offer similar capabilities.
19	However, these methods are limited to context-free constraints and cannot enforce cross-field semantic rules (e.g., ``if $
…[truncated 886 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "elapsed_ms": 853
}
```

</details>

---


### Tool call

_source line 2217 · 2026-05-23T03:34:59.963344+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 2218 · 2026-05-23T03:35:00.467196+00:00_

1	% Section 5 — SciERC Results (Draft)
2	% Data source: Phase 2 SciERC registry experiments
3	% exp_ids: phase2_scierc_unconstrained, phase2_scierc_grammar_only,
4	%          phase2_scierc_semantic_only, phase2_scierc_full_s1, phase2_scierc_full_s2
5	% All numbers verified against registry 2026-05-14.
6	
7	\subsection{Ablation and Composability with Fine-Tuning}
8	\label{sec:scierc-results}
9	
10	Table~\ref{tab:scierc-ablation} presents the five-way ablation on SciERC (Qwen3-8B, zero-shot, 551 documents); only the active constraint layers differ across rows.
11	
12	% ──────────────────────────────────────────
13	%  Table: SciERC five-way ablation
14	% ──────────────────────────────────────────
15	\begin{table}[t]
16	\centering
17	\small
18	\setlength{\tabcolsep}{3.6pt}
19	\resizebox{\columnwidth}{!}{%
20	\begin{tabular}{@{}l rrrrrr rr@{}}
21	\toprule
22	& \multicolumn{6}{c}{\textbf{Violation Rates (\%)}}
23	& \multicolumn{2}{c}{\textbf{F1}} \\
24	\cmidrule(lr){2-7} \cmidrule(l){8-9}
25	\textbf{Mode}
26	  & DR\,$\downarrow$ & $\Delta$DR
27	  & RV\,$\downarrow$ & ET\,$\downarrow$ & CF & Tot.\,$\downarrow$
28	  & Rel.\,$\uparrow$ & Ent.\,$\uparrow$ \\
29	\midrule
30	Unconstrained
31	  & 15.37 & ---
32	  & 1.39  & 0.40
33	  & 0.08  & 15.45
34	  & 8.23  & 31.01 \\
35	Grammar
36	  & 14.84 & $\downarrow$3\%
37	  & \textbf{0} & \textbf{0}
38	  & 0.08  & 14.92
39	  & 8.23  & 30.98 \\
40	GCD-equiv.$^\dagger$
41	  & 15.26 & $\downarrow$1\%
42	  & \textbf{0} & \textbf{0}
43	  & 0.04  & 15.30
44	  & 8.75  & 30.91 \\
45	Semantic
46	  & 11.65 & $\downarrow$24\%
47	  & 1.51  & 0.40
48	  & 2.71  & 14.36
49	  & 8.15  & 31.01 \\
50	S1
51	  & \textbf{0.93} & $\downarrow$\textbf{94\%}
52	  & \textbf{0} & \textbf{0}
53	  & 9.90  & \textbf{10.83}
54	  & \textbf{8.36} & 30.98 \\
55	S2
56	  & 0.97  & $\downarrow$94\%
57	  & \textbf{0} & \textbf{0}
58	  & 8.03  & \textbf{9.00}
59	  & 8.03  & \textbf{31.90} \\
60	\bottomrule
61	\end{tabular}}%
62	\caption{Five-way ablation on SciERC (551 docs
…[truncated 5804 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "elapsed_ms": 503
}
```

</details>

---


### Tool call

_source line 2219 · 2026-05-23T03:35:00.469249+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 2220 · 2026-05-23T03:35:00.972252+00:00_

1	% Section 5 — DocRED Results (compressed; full ablation in Appendix)
2	% exp_ids: phase2_docred_unconstrained, phase2_docred_grammar_only,
3	%          phase2_docred_semantic_only, phase2_docred_full_s1
4	
5	\subsection{Cross-Dataset Validation on DocRED}
6	\label{sec:docred-results}
7	
8	DocRED (96 relations, 14$\times$ SciERC scale) validates the pattern under a larger, more restrictive ontology (Table~\ref{tab:docred-ablation}).
9	S1 reduces DR from 18.46\% to 10.21\% ($\downarrow$45\%), eliminates RV (29.66\%\,$\to$\,0.03\%) and ET, with R-F1 $+$0.50\,pp ($p < 0.001$).
10	The lower DR reduction (45\% vs.\ 94\% on SciERC) reflects DocRED's tighter constraints, which trigger more grammar-first fallback (\S\ref{sec:greedy-limitation}).
11	Grammar-only \emph{increases} DR (18.46\%\,$\to$\,26.17\%) by exposing latent violations when OOV relations become evaluable---a distinct cross-dataset confirmation of the empirical enabling dependency.
12	Fine-tuning resolves residual DR entirely (Table~\ref{tab:composability}; residual decomposition in Appendix~\ref{app:residual-dr-analysis}).
13	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "elapsed_ms": 503
}
```

</details>

---


### Tool call

_source line 2221 · 2026-05-23T03:35:00.972635+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_crossmodel_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_crossmodel_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 2222 · 2026-05-23T03:35:01.023607+00:00_

1	% Section 5 — Cross-Model Validation (compressed, 830→~400 words)
2	% exp_ids: phase2_scierc_unconstrained, phase2_scierc_full_s1,
3	%          phase2_docred_unconstrained, phase2_docred_full_s1,
4	%          llama_scierc_unconstrained, llama_scierc_full_s1,
5	%          llama_docred_unconstrained, llama_docred_full_s1
6	
7	\subsection{Cross-Model Validation}
8	\label{sec:cross-model}
9	
10	Table~\ref{tab:cross-model} replicates S1 with Llama-3.1-8B and Mistral-7B under identical prompts.
11	
12	\begin{table}[t]
13	\centering
14	\small
15	\setlength{\tabcolsep}{3.4pt}
16	\resizebox{\columnwidth}{!}{%
17	\begin{tabular}{@{}ll rrrr r@{}}
18	\toprule
19	& & \multicolumn{4}{c}{\textbf{Violation Rates (\%)}}
20	& \textbf{R-F1} \\
21	\cmidrule(lr){3-6} \cmidrule(l){7-7}
22	\textbf{Dataset} & \textbf{Model}
23	  & DR\,$\downarrow$ & RV\,$\downarrow$ & ET\,$\downarrow$ & CF
24	  & $\uparrow$ \\
25	\midrule
26	\multirow{6}{*}{SciERC}
27	  & Qwen (U)    & 15.37 & 1.39  & 0.40 & 0.08 & 8.23 \\
28	  & Qwen (S1)   &  0.93 & 0     & 0    & 9.90 & 8.36 \\
29	  \cmidrule(l){2-7}
30	  & Llama (U)   & 13.34 & 0.55  & 0    & 0.24 & 2.68 \\
31	  & Llama (S1)  &  0.08 & 0     & 0    & 6.56 & 2.54 \\
32	  \cmidrule(l){2-7}
33	  & Mistral (U) & 56.94 & 0     & 1.50 & 56.87$^\dagger$ & 3.66 \\
34	  & Mistral (S1)& 13.40 & 0     & 0    & 1.27  & 3.67 \\
35	\midrule
36	\multirow{6}{*}{DocRED}
37	  & Qwen (U)    & 18.46 & 29.66 & 2.48 & 0.10 & 7.74 \\
38	  & Qwen (S1)   & 10.21 &  0.03 & 0    & 2.57 & 8.23 \\
39	  \cmidrule(l){2-7}
40	  & Llama (U)   & 26.07 & 16.03 & 0.13 & 0.17 & 5.98 \\
41	  & Llama (S1)  &  2.55 &  0    & 0    & 12.02& 6.27 \\
42	  \cmidrule(l){2-7}
43	  & Mistral (U) & 57.42 & 42.35 & 7.58 & 24.78 & 4.34 \\
44	  & Mistral (S1)& 33.20 &  0    & 0    & 0.19  & 5.52 \\
45	\bottomrule
46	\end{tabular}}%
47	\caption{Three-model zero-shot validation. U: unconstrained; S1: full two-layer.
48	Parse failures: Llama DocRED 9.1\%; others $\leq$1.1\%.
49	$^\dagger$Mistral: poor ze
…[truncated 778 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2223 · 2026-05-23T03:35:09.007420+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_wikievents_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_wikievents_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 2224 · 2026-05-23T03:35:09.510242+00:00_

1	% Section 5 — Event Extraction on WikiEvents (compact, inline)
2	% exp_ids: ee_qwen_wikievents_unconstrained, ee_llama_wikievents_unconstrained,
3	%          ee_mistral_wikievents_unconstrained, ee_qwen_wikievents_constrained,
4	%          ee_llama_wikievents_constrained, ee_mistral_wikievents_constrained_v2
5	% v3 final data confirmed by Director 2026-05-18.
6	
7	\subsection{Extension to Event Extraction (Preliminary)}
8	\label{sec:wikievents}
9	
10	As a preliminary pilot study, we apply OntoCoDec to event extraction (EE) on WikiEvents~\cite{li2021document,lu2021text2event} (56 event types, 80 roles, 27 entity types, 245 constraints; Appendix~\ref{app:wikievents}) without modification.
11	Violations extend to EV (event vocabulary), RoV (role vocabulary), and AC (argument constraint, analogous to DR).
12	
13	% ──────────────────────────────────────────
14	%  Table: WikiEvents three-model comparison (v3 final)
15	%  exp_ids: ee_{qwen,llama,mistral}_wikievents_{unconstrained,grammar_only,constrained_v3}
16	% ──────────────────────────────────────────
17	\begin{table}[t]
18	\centering
19	\small
20	\setlength{\tabcolsep}{2.8pt}
21	\resizebox{\columnwidth}{!}{%
22	\begin{tabular}{@{}ll rrrr rr@{}}
23	\toprule
24	& & \multicolumn{4}{c}{\textbf{Violation Rates (\%)}}
25	& \multicolumn{2}{c}{\textbf{F1}} \\
26	\cmidrule(lr){3-6} \cmidrule(l){7-8}
27	\textbf{Model} & \textbf{Mode}
28	  & EV\,$\downarrow$ & RoV\,$\downarrow$ & AC & CF
29	  & Trig.\,$\uparrow$ & Ent.\,$\uparrow$ \\
30	\midrule
31	\multirow{3}{*}{Qwen3-8B}
32	  & Unconstr.\ & 24.0 & 74.9 & 0.3 & 0 & 11.8 & 0 \\
33	  & Grammar    & \textbf{0} & 76.1 & 8.2 & --- & --- & --- \\
34	  & S1    & \textbf{0} & \textbf{0} & 2.1 & 21.1 & 13.4 & 14.1 \\
35	\midrule
36	\multirow{3}{*}{\shortstack[l]{Llama\\3.1-8B}}
37	  & Unconstr.\ & 10.5 & 88.8 & 0.1 & 0 & 5.7 & 0 \\
38	  & Grammar    & \textbf{0} & 77.0 & 8.8 & --- & --- & --- \\
39	  & S1    & \textbf{0} & \textbf{0} & 3.8 & 17.2 & 7.5 & 17.6 \\
40	\midrule
41	\multi
…[truncated 2192 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 2225 · 2026-05-23T03:35:09.510668+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_runtime.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_runtime.tex"
  }
}
```

</details>

---


### Tool result

_source line 2226 · 2026-05-23T03:35:09.561241+00:00_

1	% Runtime overhead (inline paragraph, no subsection header to save space)
2	
3	\paragraph{Runtime overhead.}
4	\label{sec:runtime}
5	S1 overhead is $+$13.1\% on SciERC, lower on DocRED due to amortization over longer sequences; under LoRA, $+$10.0\% with 37\% lower absolute latency.
6	Constraint compilation is one-time $<$0.5\,s; scaling benchmarks confirm constant overhead (2--3\%) up to 200 entity types and 1{,}000 relations (Appendix~\ref{app:scalability}).
7	
8	\paragraph{Beam search compatibility.}
9	\label{sec:beam-results}
10	With LoRA, beam search ($k{=}4$)~\cite{anderson2017guided} eliminates all four violation types on both SciERC and DocRED at both 8B and 70B scales (R-F1 43--47; Appendix~\ref{app:beam-search}), yielding two deployment tiers: greedy S1 ($+$10\% latency, DR${<}$0.1\%, CF${\leq}$1.4\%) and beam S1 (1.54$\times$ latency, all violations${\to}$0\%; Table~\ref{tab:beam-latency}).
11	
12	% exp_ids: r16_70b_scierc_zs_s1, r16_70b_docred_zs_s1, 70b_lora_scierc, 70b_lora_docred_200
13	\paragraph{70B-class validation.}
14	\label{sec:70b-results}
15	On Llama-3.1-70B-Instruct (AWQ INT4),\footnote{All 70B experiments use AWQ INT4 quantization; logit-level effects on constraint enforcement are not isolated.} zero-shot S1 eliminates DR on both datasets (SciERC 6.41\%\,$\to$\,0\%, DocRED 14.98\%\,$\to$\,0\%; R-F1 11--13).
16	% exp_ids: r16_70b_scierc_zs_ablation (grammar_only, semantic_only, full_s1)
17	A four-way ablation reveals scale-dependent layer interaction: semantic-only achieves 84\% DR reduction vs.\ 8B's 24\% (Table~\ref{tab:scierc-ablation}), though grammar remains necessary for RV elimination and CF control (semantic-only CF${=}$76).
18	% exp_ids: eval_70b_lora_scierc_s1_constrained, eval_70b_lora_docred_200_s1_constrained
19	LoRA confirms composability: DR\,$\to$\,0\% on both datasets (R-F1 44.53, 43.95; $|\Delta| \leq 0.20$\,pp; CF 0.18--1.33\%); cross-family generalization at 70B scale remains to be verified.
20	% exp_ids: eval_70b_lora_d
…[truncated 923 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2227 · 2026-05-23T03:35:10.063725+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 2228 · 2026-05-23T03:35:10.064127+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	We provide a detailed survey in Appendix~\ref{app:related_work}; here we position OntoCoDec along three axes.
5	
6	\paragraph{Constrained decoding.}
7	XGrammar~\cite{dong2025xgrammar}, Outlines~\cite{willard2023outlines}, SynCode~\cite{ugare2024syncode}, SGLang~\cite{zheng2024sglang}, and related systems~\cite{beurer-kellner2023lmql,park2024grammar,jsonschemabench2025} enforce format validity via CFG-based token masking.
8	NeuroLogic Decoding~\cite{lu2021neurologic} and \citet{huang2024lookahead} enforce constraints via beam-level reranking; OntoCoDec applies per-token masking, avoiding beam-width dependence.
9	PICARD~\cite{scholak2021picard} and \citet{pldi2025_type_constrained_codegen} compile type systems into prefix automata; OntoCoDec applies constructive forward masking via a dynamic entity registry (\S\ref{sec:composition}).
10	DCCD~\cite{dccd2026} and \citet{nguyen2026thinking} decouple reasoning from constrained generation; OntoCoDec enforces schema semantics within a single forward pass.
11	
12	\paragraph{Schema-aware IE.}
13	GoLLIE~\cite{sainz2024gollie}, KnowCoder~\cite{knowcoder_acl2024}, GUIDEX~\cite{guidex2025}, GenIE~\cite{josifoski2022genie}, TANL~\cite{paolini2021tanl}, REBEL~\cite{cabot2021rebel}, InstructUIE~\cite{wang2023instructuie}, ADELIE~\cite{qi2024adelie}, and others~\cite{fei2022lasuie,wang2022deepstruct,lu2022uie,lou2023usm,zhou2024universalner} encode ontology structure or frame IE as structured generation, though schema compliance gaps persist~\cite{wadhwa2023revisiting}.
14	GoLLIE and KnowCoder embed schema knowledge via code-style prompts (training-time internalization without runtime enforcement); GoLLIE-7B eliminates DR at severe coverage cost (R-F1${=}$0.0, 46\% empty output), while OntoCoDec achieves R-F1${=}$45.47 at DR${=}$0.09\%.
15	
16	\paragraph{Constraint enforcement in IE.}
17	\citet{roth_yih_2004} and \citet{riedel2010modeling} formulated hard type constraints via I
…[truncated 619 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2229 · 2026-05-23T03:35:10.671866+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section4_composition_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section4_composition_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 2230 · 2026-05-23T03:35:10.694063+00:00_

1	% Section: Constraint Composition (compressed, 787→~500 words)
2	
3	At each decoding step $t$, let $G(t) \subseteq V$ and $S(t) \subseteq V$ denote the tokens permitted by the grammar and semantic layers, respectively.
4	The final mask is their conjunction:
5	%
6	\begin{equation}\label{eq:composition}
7	  M_{\text{final}}(t) = M_{\text{grammar}}(t) \;\wedge\; M_{\text{semantic}}(t),
8	\end{equation}
9	%
10	where $\wedge$ denotes element-wise AND over the vocabulary $V$; a token is allowed only if it satisfies \emph{both} structural and type-level constraints.
11	The conjunction is asymmetric: $S(t)$ is defined only over $G(t)$. This reflects the empirical enabling dependency (\S\ref{sec:method}): the semantic layer requires the relation type to belong to $\mathcal{R}$, a property enforced only by the grammar layer.
12	This dependency is scale-sensitive: 70B semantic-only achieves 84\% DR reduction (vs.\ 24\% on 8B), though grammar remains necessary for RV elimination (\S\ref{sec:70b-results}).
13	
14	\paragraph{Grammar-First Fallback.}
15	When $S(t) \cap G(t) = \emptyset$ (tight constraints leave no token that is both grammar-valid and semantically valid), na\"{\i}ve masking would force selection of a grammar-invalid token, breaking JSON structure.
16	We enforce a \emph{grammar-first fallback}: semantic masking is skipped and the grammar layer alone controls selection.
17	Structural integrity is a hard constraint; type violations are soft errors detectable by downstream validation, with DR (ontologically invalid type pair) more severe than CF (individually valid triples with cross-triple type inconsistency).
18	Extraction tasks are robust to format-level constraints~\cite{tam2024letmespeak}, supporting this asymmetric treatment.
19	
20	\paragraph{Constraint Tightness.}
21	\label{eq:tightness}
22	Per-relation constraint tightness $\kappa(r) = 1 - |\sigma(r)|/|\mathcal{E}|^2$, with schema mean $\bar{\kappa}$.
23	Across WikiEvents ($\bar{\kappa}{=}0.029$), SciERC ($\
…[truncated 1401 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "elapsed_ms": 22
}
```

</details>

---


### Tool call

_source line 2231 · 2026-05-23T03:35:15.829617+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section7_conclusion_compressed.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section7_conclusion_compressed.tex"
  }
}
```

</details>

---


### Tool result

_source line 2232 · 2026-05-23T03:35:16.382468+00:00_

1	% Section 7 — Discussion and Conclusion
2	
3	OntoCoDec compiles IE ontologies into composable token-level constraints, validated across 3 datasets, 3+ models, and 2 tasks.
4	LoRA + greedy S1 near-eliminates DR ($<$\,0.1\%) at R-F1 41--47\%; beam ($k{=}4$) eliminates all violations at 1.54$\times$ latency.
5	The central insight is that IE type constraints exceed context-free expressiveness (Proposition~1): the semantic layer bridges the gap grammar-only enforcement cannot address (3\% vs.\ 94\% DR reduction) via constructive forward masking over a dynamic entity registry.
6	This empirical enabling dependency is scale-sensitive (\S\ref{sec:70b-results}), suggesting grammar-constrained decoding is necessary but increasingly insufficient as models improve.
7	Extending to global entity-level type consensus during decoding---eliminating CF without beam search overhead---is the primary direction for future work.
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 2233 · 2026-05-23T03:35:16.433272+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_violation_landscape.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_violation_landscape.tex"
  }
}
```

</details>

---


### Tool result

_source line 2234 · 2026-05-23T03:35:17.738927+00:00_

1	% §5 Setup (compressed from Violation Landscape)
2	% exp_ids: mvp_phase0_violation_rate, mvp_phase0_scierc_schema,
3	%          mvp_phase0_violation_rate_docred, mvp_phase0_docred_schema
4	
5	\label{sec:violation_landscape}
6	
7	We evaluate OntoCoDec in two deployment configurations: greedy S1 (DR\,$\leq$\,0.09\%, $+$10\% latency) and beam S1 (all violations\,$\to$\,0\%, 1.54$\times$ latency); zero-shot evaluation (\S\ref{sec:scierc-results}--\S\ref{sec:cross-model}) serves as a diagnostic probe for the fine-tuned setting (R-F1 41--47\%).
8	
9	\paragraph{Setup.}
10	We evaluate on SciERC~\cite{luan2018scierc} (551 test sentences, 7 relations, $\bar{\kappa}{=}0.333$) and DocRED~\cite{yao2019docred} (998 dev documents,\footnote{DocRED test annotations are not publicly available; we evaluate on the development set.} 96 relations, $\bar{\kappa}{=}0.842$).
11	RE type constraints are extracted from observed type pairs in training data (neither dataset provides a formal ontology); EE constraints on WikiEvents (\S\ref{sec:wikievents}) derive from the KAIROS ontology.
12	All constraints are schema-level, independent of evaluation splits.
13	Primary model: Qwen3-8B~\cite{qwen2025qwen3}, zero-shot greedy decoding; cross-model validation in \S\ref{sec:cross-model}, composability with fine-tuning in \S\ref{sec:composability}.
14	LoRA hyperparameters were selected on SciERC development data and transferred to DocRED without further tuning; DocRED development documents were used for evaluation only.
15	Four violation categories: \textbf{DR} (type pair $\notin \sigma(r)$), \textbf{RV} (relation $\notin \mathcal{R}$), \textbf{ET} (entity type $\notin \mathcal{E}$), \textbf{CF} (conflicting types across triples).
16	Baseline DR: 15.37\% (SciERC), 18.46\% (DocRED); schema-informed prompting reduces DR by 62\% but is per-relation unreliable (Appendix~\ref{app:per-relation-landscape}).
17	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "elapsed_ms": 1305
}
```

</details>

---


### Tool call

_source line 2235 · 2026-05-23T03:35:17.739431+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "pdfinfo /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_22/submitted.pdf 2>/dev/null | grep -i pages",
  "description": "Check PDF page count"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Bash",
  "tool_args": {
    "command": "pdfinfo /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_22/submitted.pdf 2>/dev/null | grep -i pages",
    "description": "Check PDF page count"
  }
}
```

</details>

---


### Tool result

_source line 2236 · 2026-05-23T03:35:18.794928+00:00_

Pages:           38

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Bash",
  "elapsed_ms": 1055
}
```

</details>

---


### Tool call

_source line 2237 · 2026-05-23T03:35:19.148718+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_issues.yaml 2>/dev/null && echo \"EXISTS\" || echo \"NOT_FOUND\"",
  "description": "Check if review issues tracker exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_issues.yaml 2>/dev/null && echo \"EXISTS\" || echo \"NOT_FOUND\"",
    "description": "Check if review issues tracker exists"
  }
}
```

</details>

---


### Tool result

_source line 2238 · 2026-05-23T03:35:19.199498+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_issues.yaml
EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2239 · 2026-05-23T03:35:26.841041+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "schema_semantic_constrained_ie",
  "file": "decisions.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "schema_semantic_constrained_ie",
    "file": "decisions.yaml"
  }
}
```

</details>

---


### Tool result

_source line 2240 · 2026-05-23T03:35:26.842043+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/decisions.yaml\", \"content\": \"_next_id: 86\\ndecisions:\\n- id: D001\\n  date: 2026-05-13 17:38 UTC\\n  summary: 主目标调整为 EMNLP 2026 ARR (5/25), AAAI 2027 为后备\\n  rationale: 用户明确指出 EMNLP ARR 5/25 时间不紧、不要保守、资源会给够。12 天 AI 团队速度足够：Phase 0 (1-2天) →\\n    Phase 1 compiler (2-3天) → Phase 2 experiments (2-3天) → Paper (2-3天)。禁止 fallback\\n    思维，冲最高目标。\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-13 19:14 UTC\\n  summary: SciERC Phase 0 结果确认 GO — domain_range violation rate 15.4%，3× 超阈值\\n  rationale: 'SciERC 全量 test set (551 sentences, 1724 triples): domain_range_violation_rate\\n    = 15.4%，远超 5% go/no-go 阈值。违规分布极不均匀 (Feature-of 33.5%, Compare 42.4% vs Used-for\\n    0.76%)，支持\\\"特定 relation types 需要 decoding-time enforcement\\\"的论文 claim。DocRED dry-run\\n    (37 docs) 同样显示 14.4%。两个数据集均为 GO 信号，MVP 核心假设得到强验证。等 schema-informed prompt 结果确认\\n    prompt 级干预不足以解决问题后正式宣布 MVP 通过。'\\n  related_experiments:\\n  - exp_id: mvp_phase0_violation_rate\\n    role: primary\\n    result: domain_range_violation_rate=15.4%, go_nogo=GO\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-13 21:48 UTC\\n  summary: MVP 通过，进入 Research 阶段，立即启动 Phase 2 constrained decoding 实验\\n  rationale: Phase 0 三个实验完成：SciERC 15.4%/5.78%, DocRED 18.7% domain_range violation\\n    rate。两个数据集均远超 5% 阈值，核心假设得到强验证。Phase 1 compiler 代码就绪（36 tests 通过），Phase 2 脚本就绪（S1\\n    路径可用，S2 bug 修复中）。cuda:1 空闲，立即启动 Phase 2 SciERC grammar_only/semantic_only/full_s1\\n    实验。\\n  related_experiments:\\n  - exp_id: mvp_phase0_violation_rate\\n    role: primary\\n    result: SciERC DR=15.4%, GO\\n  - exp_id: mvp_phase0_scierc_schema\\n    role: primary\\n    result: SciERC DR=5.78%, prompt insufficient\\n  - exp_id: mvp_phase0_violation_rate_docred\\n    role: primary\\n    result: DocRED DR=18.7%, GO\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-
…[truncated 11013 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 1
}
```

</details>

---


### Tool call

_source line 2241 · 2026-05-23T03:35:27.193777+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
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

_source line 2242 · 2026-05-23T03:35:27.194139+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2243 · 2026-05-23T03:35:28.399410+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -A5 \"external_review\" /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/agent/config.yaml 2>/dev/null || echo \"NOT_FOUND\"",
  "description": "Check external review config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -A5 \"external_review\" /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/agent/config.yaml 2>/dev/null || echo \"NOT_FOUND\"",
    "description": "Check external review config"
  }
}
```

</details>

---


### Tool result

_source line 2244 · 2026-05-23T03:35:28.450119+00:00_

NOT_FOUND

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2245 · 2026-05-23T03:35:33.822406+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/agent/config.yaml 2>/dev/null | grep -A10 \"external_review\\|paperreview\"",
  "description": "Check external review config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/agent/config.yaml 2>/dev/null | grep -A10 \"external_review\\|paperreview\"",
    "description": "Check external review config"
  }
}
```

</details>

---


### Tool result

_source line 2246 · 2026-05-23T03:35:34.174253+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Bash",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 2247 · 2026-05-23T03:35:34.174756+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 2248 · 2026-05-23T03:35:34.225897+00:00_

1	
2	# Review Issues Tracker — schema_semantic_constrained_ie
3	# Updated: Round 21 Action Matrix locked, 2026-05-23
4	
5	# ============================================================
6	# Round 21 Active Issues
7	# ============================================================
8	
9	- id: "R16-MF3"
10	  summary: "CF trade-off 在 Abstract 中 framing 偏乐观——仅报告 1.18% 而实际范围达 12.02%"
11	  category: framing
12	  severity: critical
13	  status: in_progress
14	  first_raised_round: 15
15	  last_seen_round: 21
16	  mentions:
17	    - round: 17
18	      reviewers: [1, 2]
19	      note: "R17: zero-shot Llama DocRED 12.02% 未在主文叙述出现。"
20	    - round: 18
21	      reviewers: [1, 2]
22	      note: "R18: Abstract 写 'up to 12% zero-shot'，有改善。"
23	    - round: 19
24	      reviewers: [1, 2]
25	      note: "R19: R2-W3 指出 Abstract CF 表述偏乐观。R1 PARTIALLY AGREE。"
26	    - round: 20
27	      reviewers: [1, 2]
28	      note: "R20: R1-N2 + R2-N2 共识。CF framing 从 R15 至今每轮修复被打回。"
29	    - round: 21
30	      reviewers: [1, 2]
31	      note: "R21 MF1: 'up to 1.18% under greedy decoding on well-calibrated models' 是 cherry-picking。两位 Reviewer 共识：呈现完整范围。Reviewer 审查后修正方案：分层报告 FT (≤1.4%) / ZS (up to 12%)，给 CF trade-off 正式叙事地位。"
32	  action_items:
33	    - round: 19
34	      action: "Abstract CF 改为审慎表述"
35	      assigned_to: paper_agent
36	      status: completed
37	    - round: 20
38	      action: "Abstract 核心 claim 后紧跟 CF trade-off 声明"
39	      assigned_to: paper_agent
40	      status: completed
41	    - round: 21
42	      action: "Abstract 完整重写：CF 分层报告（FT: ≤1.4%, beam→0; ZS: up to 12%），CF 作为 DR enforcement 的 acknowledged side effect 获得正式叙事地位"
43	      assigned_to: paper_agent
44	      status: in_progress
45	  resolution: ""
46	  resolution_round: null
47	
48	- id: "R19-M2"
49	  summary: "Abstract 数值过于精确 + 信息密度过高"
50	  category: writing
51	  severity: warning
52	  status: in_progress
53	  first_raised_round: 19
54	  last_seen_round: 21
55	  mentions:
56	    - round: 19
57	      reviewers: [1, 2]
58	      no
…[truncated 19421 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 2249 · 2026-05-23T03:36:20.933268+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "schema_semantic_constrained_ie",
  "review_chat_id": "oc_01fc90ae186a4ed432770f7601995139"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "schema_semantic_constrained_ie",
    "review_chat_id": "oc_01fc90ae186a4ed432770f7601995139"
  }
}
```

</details>

---


### Tool call

_source line 2250 · 2026-05-23T03:36:20.933697+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "schema_semantic_constrained_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "schema_semantic_constrained_ie"
  }
}
```

</details>

---


### Tool result

_source line 2251 · 2026-05-23T03:36:24.754604+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 3821
}
```

</details>

---


### Tool result

_source line 2252 · 2026-05-23T03:36:24.755067+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 3821
}
```

</details>

---


### Tool call

_source line 2253 · 2026-05-23T03:36:53.446561+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "schema_semantic_constrained_ie",
  "text": "你是 Reviewer 1，负责**方法严谨性与实验设计**。\n\n## Venue 信息\n- **目标**: EMNLP 2026（通过 ARR 统一审稿）\n- **Deadline**: 2026-05-25（ARR May cycle）\n- **格式**: ACL 模板，正文 ≤ 8 页，参考文献不限页数，Limitations/Ethics 不计入页数\n- **匿名**: Double-blind\n- **评分标准**: Overall Assessment 5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit\n\n## 论文路径\n- LaTeX: `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_22/submitted.pdf`\n\n## 你的审查侧重\n\n### 1. 理论基础\n- Proposition 1（domain/range constraints ∉ CFL）的证明是否完备？proof sketch 是否有逻辑漏洞？\n- \"Empirical Observation\"（enabling dependency）的 framing 是否恰当——声称从数据观察而非理论推导？\n- Remark（finite entity sets）是否充分处理了理论与实践的 gap？\n\n### 2. 实验设计\n- 五路消融（unconstrained/grammar/semantic/S1/S2）是否完整覆盖因素空间？\n- Fine-tuning composability 的实验设计是否有混淆变量？LoRA 是唯一 fine-tuning 方式——是否讨论了泛化性？\n- 跨模型验证（3 models × 2 datasets）是否足够支撑 \"model-agnostic\" claim？\n- 70B 验证（单模型 AWQ INT4）的可信度？量化对 logit masking 的影响？\n- WikiEvents（n=20 test docs）的统计效力？\n\n### 3. 统计检验\n- Bootstrap CI 和 p-values 的使用是否恰当？Bonferroni 校正是否必要且正确应用？\n- Zero-shot 结果是确定性（greedy T=0）——是否需要多次运行？\n- DocRED 使用 dev set 评估——是否有 data leakage 风险？\n\n### 4. 指标与评估\n- 四类违规（DR/RV/ET/CF）的定义和计算是否清晰无歧义？\n- CF 作为 DR enforcement 的副作用——是否被过度淡化？CF 最高 12.02% 的严重性？\n- Parse failure 的处理方式对 F1 的影响？\n- Post-hoc filtering baseline 的对比是否公平？\n\n### 5. 可复现性\n- 实验细节（超参数、prompt、数据处理）是否足以复现？\n- 代码/数据是否承诺公开？\n\n请输出完整审稿报告，包含 Strengths、Weaknesses（分 Must-Fix / Should-Fix / Minor）、Questions、Missing References、Overall Assessment（含评分和置信度）。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "schema_semantic_constrained_ie",
    "text": "你是 Reviewer 1，负责**方法严谨性与实验设计**。\n\n## Venue 信息\n- **目标**: EMNLP 2026（通过 ARR 统一审稿）\n- **Deadline**: 2026-05-25（ARR May cycle）\n- **格式**: ACL 模板，正文 ≤ 8 页，参考文献不限页数，Limitations/Ethics 不计入页数\n- **匿名**: Double-blind\n- **评分标准**: Overall Assessment 5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit\n\n## 论文路径\n- LaTeX: `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_22/submitted.pdf`\n\n## 你的审查侧重\n\n### 1. 理论基础\n- Proposition 1（domain/range constraints ∉ CFL）的证明是否完备？proof sketch 是否有逻辑漏洞？\n- \"Empirical Observation\"（enabling dependency）的 framing 是否恰当——声称从数据观察而非理论推导？\n- Remark（finite entity sets）是否充分处理了理论与实践的 gap？\n\n### 2. 实验设计\n- 五路消融（unconstrained/grammar/semantic/S1/S2）是否完整覆盖因素空间？\n- Fine-tuning composability 的实验设计是否有混淆变量？LoRA 是唯一 fine-tuning 方式——是否讨论了泛化性？\n- 跨模型验证（3 models × 2 datasets）是否足够支撑 \"model-agnostic\" claim？\n- 70B 验证（单模型 AWQ INT4）的可信度？量化对 logit masking 的影响？\n- WikiEvents（n=20 test docs）的统计效力？\n\n### 3. 统计检验\n- Bootstrap CI 和 p-values 的使用是否恰当？Bonferroni 校正是否必要且正确应用？\n- Zero-shot 结果是确定性（greedy T=0）——是否需要多次运行？\n- DocRED 使用 dev set 评估——是否有 data leakage 风险？\n\n### 4. 指标与评估\n- 四类违规（DR/RV/ET/CF）的定义和计算是否清晰无歧义？\n- CF 作为 DR enforcement 的副作用——是否被过度淡化？CF 最高 12.02% 的严重性？\n- Parse failure 的处理方式对 F1 的影响？\n- Post-hoc filtering baseline 的对比是否公平？\n\n### 5. 可复现性\n- 实验细节（超参数、prompt、数据处理）是否足以复现？\n- 代码/数据是否承诺公开？\n\n请输出完整审稿报告，包含 Strengths、Weaknesses（分 Must-Fix / Should-Fix / Minor）、Questions、Missing References、Overall Assessment（含评分和置信度）。"
  }
}
```

</details>

---


### Tool result

_source line 2254 · 2026-05-23T03:37:13.491250+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 20044
}
```

</details>

---


### Tool call

_source line 2255 · 2026-05-23T03:37:13.653897+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "schema_semantic_constrained_ie",
  "text": "你是 Reviewer 2，负责**新颖性评估与论文完整性**。\n\n## Venue 信息\n- **目标**: EMNLP 2026（通过 ARR 统一审稿）\n- **Deadline**: 2026-05-25（ARR May cycle）\n- **格式**: ACL 模板，正文 ≤ 8 页，参考文献不限页数，Limitations/Ethics 不计入页数\n- **匿名**: Double-blind\n- **评分标准**: Overall Assessment 5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit\n\n## 论文路径\n- LaTeX: `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_22/submitted.pdf`\n\n## 你的审查侧重\n\n### 1. 新颖性与贡献\n- OntoCoDec 的核心贡献是什么？系统集成 vs 算法创新？对 NLP 社区的实际价值？\n- Proposition 1（CF constraints ∉ CFL）是否真正新颖？PDA 无法 random access 是 well-known fact——论文的理论贡献是将此 observation 应用于 IE 还是提出新的理论？\n- 两层约束架构（grammar + semantic）的设计是否有非显而易见的创新？\n- 与 PICARD、GoLLIE、KnowCoder、ADELIE 等方法的本质区别？\n\n### 2. 写作质量\n- Abstract 的信息密度和可读性（数字数量、缩写、结构）\n- Introduction 的问题定义和 motivation 是否清晰有说服力？\n- Method section 的表述是否足够清晰——不熟悉 constrained decoding 的读者能否跟上？\n- 论文整体叙事（diagnostic probe → fine-tuning composability → deployment tiers）是否连贯？\n- Limitations 的覆盖是否充分和诚实？\n\n### 3. Related Work 覆盖\n- 是否遗漏重要相关工作？特别是 2025-2026 年的新工作\n- 与已有方法的比较是否公平？是否存在 straw-man 比较？\n- Constrained decoding for IE 领域的最新进展是否充分覆盖？\n- Schema-aware IE 方法（GoLLIE、KnowCoder、GUIDEX 等）的定位是否准确？\n\n### 4. 格式合规\n- 正文是否 ≤ 8 页（不含 references/limitations/ethics）？\n- 表格/图表编号、引用格式是否一致？\n- 匿名是否彻底（无 GitHub link、作者名、机构信息）？\n- Appendix 的内容是否属于 appendix 而非 main text 遗漏？\n\n### 5. CF Trade-off Framing\n- DR enforcement 引入 CF（≤1.4% fine-tuned，up to 12% zero-shot）的 framing 是否诚实？\n- Abstract 中 CF 的呈现是否存在 cherry-picking（只报告最佳场景）？\n- CF 的严重性是否被充分讨论——对下游应用的影响？\n- Beam search 作为 CF 解决方案是否在 cost（1.54× latency）上得到充分讨论？\n\n请输出完整审稿报告，包含 Strengths、Weaknesses（分 Must-Fix / Should-Fix / Minor）、Questions、Missing References、Overall Assessment（含评分和置信度）。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "schema_semantic_constrained_ie",
    "text": "你是 Reviewer 2，负责**新颖性评估与论文完整性**。\n\n## Venue 信息\n- **目标**: EMNLP 2026（通过 ARR 统一审稿）\n- **Deadline**: 2026-05-25（ARR May cycle）\n- **格式**: ACL 模板，正文 ≤ 8 页，参考文献不限页数，Limitations/Ethics 不计入页数\n- **匿名**: Double-blind\n- **评分标准**: Overall Assessment 5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit\n\n## 论文路径\n- LaTeX: `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_22/submitted.pdf`\n\n## 你的审查侧重\n\n### 1. 新颖性与贡献\n- OntoCoDec 的核心贡献是什么？系统集成 vs 算法创新？对 NLP 社区的实际价值？\n- Proposition 1（CF constraints ∉ CFL）是否真正新颖？PDA 无法 random access 是 well-known fact——论文的理论贡献是将此 observation 应用于 IE 还是提出新的理论？\n- 两层约束架构（grammar + semantic）的设计是否有非显而易见的创新？\n- 与 PICARD、GoLLIE、KnowCoder、ADELIE 等方法的本质区别？\n\n### 2. 写作质量\n- Abstract 的信息密度和可读性（数字数量、缩写、结构）\n- Introduction 的问题定义和 motivation 是否清晰有说服力？\n- Method section 的表述是否足够清晰——不熟悉 constrained decoding 的读者能否跟上？\n- 论文整体叙事（diagnostic probe → fine-tuning composability → deployment tiers）是否连贯？\n- Limitations 的覆盖是否充分和诚实？\n\n### 3. Related Work 覆盖\n- 是否遗漏重要相关工作？特别是 2025-2026 年的新工作\n- 与已有方法的比较是否公平？是否存在 straw-man 比较？\n- Constrained decoding for IE 领域的最新进展是否充分覆盖？\n- Schema-aware IE 方法（GoLLIE、KnowCoder、GUIDEX 等）的定位是否准确？\n\n### 4. 格式合规\n- 正文是否 ≤ 8 页（不含 references/limitations/ethics）？\n- 表格/图表编号、引用格式是否一致？\n- 匿名是否彻底（无 GitHub link、作者名、机构信息）？\n- Appendix 的内容是否属于 appendix 而非 main text 遗漏？\n\n### 5. CF Trade-off Framing\n- DR enforcement 引入 CF（≤1.4% fine-tuned，up to 12% zero-shot）的 framing 是否诚实？\n- Abstract 中 CF 的呈现是否存在 cherry-picking（只报告最佳场景）？\n- CF 的严重性是否被充分讨论——对下游应用的影响？\n- Beam search 作为 CF 解决方案是否在 cost（1.54× latency）上得到充分讨论？\n\n请输出完整审稿报告，包含 Strengths、Weaknesses（分 Must-Fix / Should-Fix / Minor）、Questions、Missing References、Overall Assessment（含评分和置信度）。"
  }
}
```

</details>

---


### Tool result

_source line 2256 · 2026-05-23T03:37:15.309024+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1655
}
```

</details>

---


### Assistant

_source line 2257 · 2026-05-23T03:37:26.048731+00:00_

Round 1 初审已启动：
- **Reviewer 1**（方法严谨性 + 实验设计）：已分配
- **Reviewer 2**（新颖性 + 完整性）：已分配
- **视觉审查 Agent**：已派发（并行执行）
- **外部审稿**：未配置，跳过

等待两位 Reviewer 提交初审报告。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director"
}
```

</details>

---


## Round 164

## Round 164

11 recorded events


### User

_source line 2258 · 2026-05-23T03:38:35.709664+00:00_

[Reviewer 1 审稿结果]:
继续阅读 appendix 页面的视觉内容，检查关键 tables 和 figures。

---

[Reviewer 2 审稿结果]:
Now let me read some key section files for precise details on claims and numbers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 2259 · 2026-05-23T03:38:52.291876+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "schema_semantic_constrained_ie",
  "text": "请完成你的完整审稿报告并提交。你已经有足够的材料进行审稿。\n\n请输出完整审稿报告，包含以下结构：\n1. **Summary**: 论文概述（2-3 句）\n2. **Strengths**: 优点（逐条）\n3. **Weaknesses**: 缺点（分 Must-Fix / Should-Fix / Minor）\n4. **Questions**: 需要作者澄清的问题\n5. **Missing References**: 遗漏的重要相关工作\n6. **Overall Assessment**: 总评 + 评分（对应 EMNLP 2026 ARR 评分标准：5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit）+ 置信度\n\n你的审查侧重是：方法严谨性与实验设计（Proposition 1 证明、消融实验设计、统计检验、70B 验证、可复现性）。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "schema_semantic_constrained_ie",
    "text": "请完成你的完整审稿报告并提交。你已经有足够的材料进行审稿。\n\n请输出完整审稿报告，包含以下结构：\n1. **Summary**: 论文概述（2-3 句）\n2. **Strengths**: 优点（逐条）\n3. **Weaknesses**: 缺点（分 Must-Fix / Should-Fix / Minor）\n4. **Questions**: 需要作者澄清的问题\n5. **Missing References**: 遗漏的重要相关工作\n6. **Overall Assessment**: 总评 + 评分（对应 EMNLP 2026 ARR 评分标准：5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit）+ 置信度\n\n你的审查侧重是：方法严谨性与实验设计（Proposition 1 证明、消融实验设计、统计检验、70B 验证、可复现性）。"
  }
}
```

</details>

---


### Tool call

_source line 2260 · 2026-05-23T03:38:55.807054+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "schema_semantic_constrained_ie",
  "text": "请完成你的完整审稿报告并提交。你已经有足够的材料进行审稿。\n\n请输出完整审稿报告，包含以下结构：\n1. **Summary**: 论文概述（2-3 句）\n2. **Strengths**: 优点（逐条）\n3. **Weaknesses**: 缺点（分 Must-Fix / Should-Fix / Minor）\n4. **Questions**: 需要作者澄清的问题\n5. **Missing References**: 遗漏的重要相关工作\n6. **Overall Assessment**: 总评 + 评分（对应 EMNLP 2026 ARR 评分标准：5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit）+ 置信度\n\n你的审查侧重是：新颖性评估与论文完整性（贡献定位、写作质量、related work 覆盖、格式合规、CF framing）。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "schema_semantic_constrained_ie",
    "text": "请完成你的完整审稿报告并提交。你已经有足够的材料进行审稿。\n\n请输出完整审稿报告，包含以下结构：\n1. **Summary**: 论文概述（2-3 句）\n2. **Strengths**: 优点（逐条）\n3. **Weaknesses**: 缺点（分 Must-Fix / Should-Fix / Minor）\n4. **Questions**: 需要作者澄清的问题\n5. **Missing References**: 遗漏的重要相关工作\n6. **Overall Assessment**: 总评 + 评分（对应 EMNLP 2026 ARR 评分标准：5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit）+ 置信度\n\n你的审查侧重是：新颖性评估与论文完整性（贡献定位、写作质量、related work 覆盖、格式合规、CF framing）。"
  }
}
```

</details>

---


### Tool result

_source line 2261 · 2026-05-23T03:38:57.113641+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"&lt;urlopen error [Errno 111] Connection refused>\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 4821
}
```

</details>

---


### Tool result

_source line 2262 · 2026-05-23T03:38:59.423014+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"&lt;urlopen error [Errno 111] Connection refused>\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 3615
}
```

</details>

---


### Tool call

_source line 2263 · 2026-05-23T03:39:05.196716+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "schema_semantic_constrained_ie",
  "text": "请完成你的完整审稿报告并提交。\n\n请输出完整审稿报告，包含以下结构：\n1. **Summary**: 论文概述（2-3 句）\n2. **Strengths**: 优点（逐条）\n3. **Weaknesses**: 缺点（分 Must-Fix / Should-Fix / Minor）\n4. **Questions**: 需要作者澄清的问题\n5. **Missing References**: 遗漏的重要相关工作\n6. **Overall Assessment**: 总评 + 评分（EMNLP 2026 ARR: 5=Award, 4=Conference, 3=Findings, 2=Resubmit）+ 置信度\n\n你的侧重：方法严谨性与实验设计。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "schema_semantic_constrained_ie",
    "text": "请完成你的完整审稿报告并提交。\n\n请输出完整审稿报告，包含以下结构：\n1. **Summary**: 论文概述（2-3 句）\n2. **Strengths**: 优点（逐条）\n3. **Weaknesses**: 缺点（分 Must-Fix / Should-Fix / Minor）\n4. **Questions**: 需要作者澄清的问题\n5. **Missing References**: 遗漏的重要相关工作\n6. **Overall Assessment**: 总评 + 评分（EMNLP 2026 ARR: 5=Award, 4=Conference, 3=Findings, 2=Resubmit）+ 置信度\n\n你的侧重：方法严谨性与实验设计。"
  }
}
```

</details>

---


### Tool call

_source line 2264 · 2026-05-23T03:39:07.054883+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "schema_semantic_constrained_ie",
  "text": "请完成你的完整审稿报告并提交。\n\n请输出完整审稿报告，包含以下结构：\n1. **Summary**: 论文概述（2-3 句）\n2. **Strengths**: 优点（逐条）\n3. **Weaknesses**: 缺点（分 Must-Fix / Should-Fix / Minor）\n4. **Questions**: 需要作者澄清的问题\n5. **Missing References**: 遗漏的重要相关工作\n6. **Overall Assessment**: 总评 + 评分（EMNLP 2026 ARR: 5=Award, 4=Conference, 3=Findings, 2=Resubmit）+ 置信度\n\n你的侧重：新颖性评估与论文完整性。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "schema_semantic_constrained_ie",
    "text": "请完成你的完整审稿报告并提交。\n\n请输出完整审稿报告，包含以下结构：\n1. **Summary**: 论文概述（2-3 句）\n2. **Strengths**: 优点（逐条）\n3. **Weaknesses**: 缺点（分 Must-Fix / Should-Fix / Minor）\n4. **Questions**: 需要作者澄清的问题\n5. **Missing References**: 遗漏的重要相关工作\n6. **Overall Assessment**: 总评 + 评分（EMNLP 2026 ARR: 5=Award, 4=Conference, 3=Findings, 2=Resubmit）+ 置信度\n\n你的侧重：新颖性评估与论文完整性。"
  }
}
```

</details>

---


### Tool result

_source line 2265 · 2026-05-23T03:39:07.357838+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"&lt;urlopen error [Errno 111] Connection refused>\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 2161
}
```

</details>

---


### Tool result

_source line 2266 · 2026-05-23T03:39:09.667283+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"&lt;urlopen error [Errno 111] Connection refused>\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 2612
}
```

</details>

---


### Tool call

_source line 2267 · 2026-05-23T03:39:24.930156+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "schema_semantic_constrained_ie",
  "chat_id": "oc_01fc90ae186a4ed432770f7601995139",
  "text": "请提交你的完整审稿报告。侧重：方法严谨性与实验设计。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "schema_semantic_constrained_ie",
    "chat_id": "oc_01fc90ae186a4ed432770f7601995139",
    "text": "请提交你的完整审稿报告。侧重：方法严谨性与实验设计。"
  }
}
```

</details>

---


### Tool result

_source line 2268 · 2026-05-23T03:39:27.090111+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"&lt;urlopen error [Errno 111] Connection refused>\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 2159
}
```

</details>

---


## Round 165

## Round 165

58 recorded events


### User

_source line 2269 · 2026-05-23T08:17:24.903718+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: schema_semantic_constrained_ie
- 论文路径: /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: Long Paper
- 截止日期: 2026-05-25
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 2270 · 2026-05-23T08:17:30.653174+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 2271 · 2026-05-23T08:17:30.754619+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 2272 · 2026-05-23T08:17:37.588253+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,director_post_to_reviewer,read_project_file,get_external_review_status,get_visual_check_status,submit_review_report_to_research_director,update_review_issues,read_local_file",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,director_post_to_reviewer,read_project_file,get_external_review_status,get_visual_check_status,submit_review_report_to_research_director,update_review_issues,read_local_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 2273 · 2026-05-23T08:17:37.588771+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2274 · 2026-05-23T08:17:41.053518+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 2275 · 2026-05-23T08:17:41.104915+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "ToolSearch",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 2276 · 2026-05-23T08:17:45.009304+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
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

_source line 2277 · 2026-05-23T08:17:45.160740+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "ToolSearch",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 2278 · 2026-05-23T08:17:47.922185+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "read_local_file",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "read_local_file",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 2279 · 2026-05-23T08:17:47.922740+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2280 · 2026-05-23T08:17:51.989825+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "schema_semantic_constrained_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "schema_semantic_constrained_ie"
  }
}
```

</details>

---


### Tool result

_source line 2281 · 2026-05-23T08:17:53.296027+00:00_

{"result":"# 项目 schema_semantic_constrained_ie 概况\n\n## 实验状态 (164 个)\n\n- **llama_scierc_full_s1**: DONE (success) — \n- **llama_scierc_unconstrained**: DONE (success) — \n- **phase2_scierc_full_s1**: DONE (success) — \n- **phase2_scierc_semantic_only**: DONE (success) — \n- **phase2_scierc_grammar_only**: DONE (success) — \n- **phase2_scierc_unconstrained**: DONE (success) — \n- **phase2_docred_full_s1**: DONE (success) — \n- **phase2_docred_semantic_only**: DONE (success) — \n- **phase2_docred_unconstrained**: DONE (success) — \n- **mvp_phase0_docred_schema_r2**: DONE (killed) — \n- **phase2_s2_pilot50**: DONE (success) — \n- **mvp_phase0_docred_schema**: DONE (success) — \n- **mvp_phase0_violation_rate_docred**: DONE (success) — \n- **mvp_phase0_scierc_schema**: DONE (success) — \n- **mvp_phase0_violation_rate**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-23\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| sf2_70b_prompt_sensitivity | 70B LLaMA-3.1 constrained decoding should show consistent violation reduction across different prompt styles, similar to the 8B result where ΔDR was 94.0-94.6% regardless of prompt variant. | — | — | — |\n\n## 待处理\n- r16_70b_lora_scierc_eval: 70B AWQ INT4 LoRA fine-tuned on SciERC will achieve higher R-F1 than 8B FT (Qwen 47.15, Llama 46.13) and S1 constraints will maintain DR→0% at 70B scale（准备中）\n- p1_llama_ee_ft（准备中）\n\n## 近期结论\n- **eval_70b_lora_docred_200_full_s2** (negative): Full S2 (grammar+semantic+repair) on 70B LoRA DocRED should achieve near-zero DR while maintaining R_F1 close to beam4_s1 (48.14). The repair layer resolves residual DR violations from S1. This is the strongest constraint configuration for DocRED LoRA. ← 基于 eval_70b_lora_docred_200_beam4_s1\n- **sf2_qwen_int4_docred_s1** (success): AWQ INT4 quantization of fine-tuned Qwen3-8B does not significantly affect constraint enforcement or extraction quality on DocRED S1, mainta
…[truncated 1162 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1306
}
```

</details>

---


### Tool call

_source line 2282 · 2026-05-23T08:17:53.848665+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 2283 · 2026-05-23T08:17:54.853490+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{graphicx}
11	\usepackage{booktabs}
12	\usepackage{multirow}
13	\usepackage[table]{xcolor}
14	\usepackage{amsmath}
15	\usepackage{amssymb}
16	\usepackage{amsthm}
17	\usepackage{enumitem}
18	\usepackage{pifont}
19	\usepackage{soul}
20	\usepackage{tikz}
21	\usetikzlibrary{arrows.meta,positioning,shapes.geometric,fit,backgrounds,calc}
22	\newcommand{\TBD}[1]{\textcolor{red}{#1}}
23	
24	\title{OntoCoDec: Type-Constrained Information Extraction\\via Compiled Schema Constraints}
25	
26	\author{Anonymous ACL submission}
27	
28	\begin{document}
29	\maketitle
30	
31	% === Abstract ===
32	\input{abstract}
33	
34	% === §1 Introduction ===
35	\input{section1_introduction_draft}
36	
37	% === §2 Background ===
38	\input{section2_background}
39	
40	% === §3 Method ===
41	\input{section3_method_draft}
42	
43	% === §4 Constraint Composition ===
44	\section{Constraint Composition}
45	\label{sec:composition}
46	\input{section4_composition_draft}
47	
48	% === §5 Experiments ===
49	\section{Experiments}
50	\label{sec:experiments}
51	
52	\input{section3_violation_landscape}
53	
54	\input{section5_scierc_draft}
55	\input{section5_docred_draft}
56	\input{section5_crossmodel_draft}
57	\input{section5_wikievents_draft}
58	\input{section5_runtime}
59	
60	% === §6 Related Work ===
61	\input{section6_related_work}
62	
63	% === §7 Discussion and Conclusion ===
64	\section{Discussion and Conclusion}
65	\label{sec:discussion}
66	\input{section7_conclusion_compressed}
67	
68	% === Limitations (ARR requirement: standalone section, does not count toward page limit) ===
69	\clearpage
70	\section*{Limitations}
71	
72	\paragraph{Constraint scope.}
73	CF impact is model-dependent: for well-calibrated models (Qwen, Llama; DR\,$\leq$\,1\% under greedy constrained decoding), S1 introduces CF violations (u
…[truncated 5727 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "elapsed_ms": 1004
}
```

</details>

---


### Tool call

_source line 2284 · 2026-05-23T08:17:55.305986+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_23/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"PDF_NOT_FOUND\"",
  "description": "Check if submitted PDF exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_23/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"PDF_NOT_FOUND\"",
    "description": "Check if submitted PDF exists"
  }
}
```

</details>

---


### Tool result

_source line 2285 · 2026-05-23T08:17:55.708053+00:00_

-rw-r--r-- 1 ubuntu ubuntu 622732 May 23 08:07 /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_23/submitted.pdf
PDF_EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Bash",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 2286 · 2026-05-23T08:17:55.708414+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 2287 · 2026-05-23T08:17:55.758839+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2288 · 2026-05-23T08:18:08.214542+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:TodoWrite",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:TodoWrite",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 2289 · 2026-05-23T08:18:08.315454+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 2290 · 2026-05-23T08:18:15.557933+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0: 资料检查 + Venue CFP 搜索', 'status': 'in_progress', 'activeForm': '检查资料完整性并搜索 EMNLP 2026 CFP'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'pending', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.6/0.7: 派发外部审稿 + 视觉审查', 'status': 'pending', 'activeForm': '派发外部审稿和视觉审查'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'pending', 'activeForm': '分配 Reviewer 独立审稿'}, {'content': 'Step 2: 交叉分享', 'status': 'pending', 'activeForm': '交叉分享审稿意见'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断审稿是否收敛'}, {'content': 'Step 4: 汇总报告 & 投递', 'status': 'pending', 'activeForm': '汇总审稿报告并投递'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Step 0: 资料检查 + Venue CFP 搜索', 'status': 'in_progress', 'activeForm': '检查资料完整性并搜索 EMNLP 2026 CFP'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'pending', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.6/0.7: 派发外部审稿 + 视觉审查', 'status': 'pending', 'activeForm': '派发外部审稿和视觉审查'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'pending', 'activeForm': '分配 Reviewer 独立审稿'}, {'content': 'Step 2: 交叉分享', 'status': 'pending', 'activeForm': '交叉分享审稿意见'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断审稿是否收敛'}, {'content': 'Step 4: 汇总报告 & 投递', 'status': 'pending', 'activeForm': '汇总审稿报告并投递'}]"
  }
}
```

</details>

---


### Tool result

_source line 2291 · 2026-05-23T08:18:15.558460+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2292 · 2026-05-23T08:18:20.127152+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
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

_source line 2293 · 2026-05-23T08:18:21.081420+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 author guidelines page limit template",
  "allowed_domains": "['aclweb.org', 'aclrollingreview.org']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 author guidelines page limit template",
    "allowed_domains": "['aclweb.org', 'aclrollingreview.org']"
  }
}
```

</details>

---


### Tool result

_source line 2294 · 2026-05-23T08:18:27.606869+00:00_

Web search results for query: "ACL Rolling Review 2026 author guidelines page limit template"

Links: [{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"}]

Based on the search results, I found relevant information about ACL Rolling Review 2026 author guidelines:

## Key Information:

**Page Limits:**
Final versions of accepted papers will be given one additional page of content (up to 9 pages for long papers, up to 5 pages for short papers) to address reviewers' comments.

**Template:**
There is an official Overleaf template, and this template has a [review] setting that must be on for the submission. Additionally, ARR abandons the MS Word Template for conference submissions, and submissions based on the Word templ
…[truncated 672 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "WebSearch",
  "elapsed_ms": 6525
}
```

</details>

---


### Tool result

_source line 2295 · 2026-05-23T08:18:28.059117+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines ARR"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"*SEM 2026: Commitment Link for ARR-Reviewed Papers (Deadline: 10 April 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/sem-2026-commitment-link-arr-reviewed-papers-deadline-10-april-2026"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"5th Workshop on Evaluation and Comparison for NLP systems (Eval4NLP) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/5th-workshop-evaluation-and-comparison-nlp-systems-eval4nlp"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"}]

Based on the search results, here's information about EMNLP 2026's call for papers submission guidelines and ARR policy:

## Main Conference Papers

EMNLP 2026 invites the submission of long and short papers featuring substantial, original, and unpublished research on empirical methods for Natural Language Processing. Papers may contribute negative findings, survey an area, announce the creation of a new resource, argue a position, report novel linguistic insights derived using existing computational techniques, and reproduce (or fail to reproduce) previous results.

## Presentation Requirements

All accepted papers must be presented at the conference to appear in the proceedings, and the conference will include both in-person and virtual presentation options. Papers without at le
…[truncated 910 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "WebSearch",
  "elapsed_ms": 7931
}
```

</details>

---


### Tool call

_source line 2296 · 2026-05-23T08:18:31.657913+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 submission deadline May 2026 ARR cycle commitment"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 submission deadline May 2026 ARR cycle commitment"
  }
}
```

</details>

---


### Tool call

_source line 2297 · 2026-05-23T08:18:32.361260+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review call for papers 2026 long paper 8 pages short paper 4 pages anonymity double blind",
  "allowed_domains": "['aclrollingreview.org']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review call for papers 2026 long paper 8 pages short paper 4 pages anonymity double blind",
    "allowed_domains": "['aclrollingreview.org']"
  }
}
```

</details>

---


### Tool result

_source line 2298 · 2026-05-23T08:18:37.137834+00:00_

Web search results for query: "EMNLP 2026 submission deadline May 2026 ARR cycle commitment"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"AI Conference Deadlines - Jie Cao | Dialogue, NLP, ML","url":"https://mlciv.com/ai-deadlines/"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"emnlp 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=emnlp26"},{"title":"EMNLP 2026 Workshop WiNLP ARR Commitment | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FWorkshop%2FWiNLP_ARR_Commitment"}]

Based on the search results, here's what I found about EMNLP 2026 submission deadlines and ARR cycle commitment:

## Key Deadlines and Information

**ARR Submission Deadline:** The ARR submission deadline for long and short papers is May 25, 2026.

**Reviewer Registration:** The reviewer registration deadline for ALL authors is May 27, 2026.

## Special ARR 2026 May Cycle Policy for EMNLP

There's an important policy specific to the May 2026 ARR cycle: Authors will need to explicitly declare which 
…[truncated 687 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "WebSearch",
  "elapsed_ms": 5479
}
```

</details>

---


### Tool result

_source line 2299 · 2026-05-23T08:18:37.941210+00:00_

Web search results for query: "ACL Rolling Review call for papers 2026 long paper 8 pages short paper 4 pages anonymity double blind"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Update to Anonymity Policy – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/anonymity/"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"}]

Based on the search results, here's what I found about the ACL Rolling Review 2026 call for papers requirements you asked about:

**Paper Length Requirements:**
All ARR submissions are anonymous and in the format of a short paper (up to 4 pages) or long paper (up to 8 pages).

**Anonymity and Double-Blind Review:**
Papers must not include authors' names and affiliations. Furthermore, self-references that reveal the authors' identities, e.g., "We previously showed (Smith, 1991)…" must be avoided. Supplementary materials, including any links to repositories, should also be anonymized.

Ideally, ARR peer review should be fully anony
…[truncated 425 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "WebSearch",
  "elapsed_ms": 5579
}
```

</details>

---


### Tool call

_source line 2300 · 2026-05-23T08:18:49.064938+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "schema_semantic_constrained_ie",
  "file": "decisions.yaml",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "schema_semantic_constrained_ie",
    "file": "decisions.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 2301 · 2026-05-23T08:18:50.421314+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/decisions.yaml\", \"content\": \"_next_id: 86\\ndecisions:\\n- id: D001\\n  date: 2026-05-13 17:38 UTC\\n  summary: 主目标调整为 EMNLP 2026 ARR (5/25), AAAI 2027 为后备\\n  rationale: 用户明确指出 EMNLP ARR 5/25 时间不紧、不要保守、资源会给够。12 天 AI 团队速度足够：Phase 0 (1-2天) →\\n    Phase 1 compiler (2-3天) → Phase 2 experiments (2-3天) → Paper (2-3天)。禁止 fallback\\n    思维，冲最高目标。\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-13 19:14 UTC\\n  summary: SciERC Phase 0 结果确认 GO — domain_range violation rate 15.4%，3× 超阈值\\n  rationale: 'SciERC 全量 test set (551 sentences, 1724 triples): domain_range_violation_rate\\n    = 15.4%，远超 5% go/no-go 阈值。违规分布极不均匀 (Feature-of 33.5%, Compare 42.4% vs Used-for\\n    0.76%)，支持\\\"特定 relation types 需要 decoding-time enforcement\\\"的论文 claim。DocRED dry-run\\n    (37 docs) 同样显示 14.4%。两个数据集均为 GO 信号，MVP 核心假设得到强验证。等 schema-informed prompt 结果确认\\n    prompt 级干预不足以解决问题后正式宣布 MVP 通过。'\\n  related_experiments:\\n  - exp_id: mvp_phase0_violation_rate\\n    role: primary\\n    result: domain_range_violation_rate=15.4%, go_nogo=GO\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-13 21:48 UTC\\n  summary: MVP 通过，进入 Research 阶段，立即启动 Phase 2 constrained decoding 实验\\n  rationale: Phase 0 三个实验完成：SciERC 15.4%/5.78%, DocRED 18.7% domain_range violation\\n    rate。两个数据集均远超 5% 阈值，核心假设得到强验证。Phase 1 compiler 代码就绪（36 tests 通过），Phase 2 脚本就绪（S1\\n    路径可用，S2 bug 修复中）。cuda:1 空闲，立即启动 Phase 2 SciERC grammar_only/semantic_only/full_s1\\n    实验。\\n  related_experiments:\\n  - exp_id: mvp_phase0_violation_rate\\n    role: primary\\n    result: SciERC DR=15.4%, GO\\n  - exp_id: mvp_phase0_scierc_schema\\n    role: primary\\n    result: SciERC DR=5.78%, prompt insufficient\\n  - exp_id: mvp_phase0_violation_rate_docred\\n    role: primary\\n    result: DocRED DR=18.7%, GO\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-
…[truncated 1469 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 1356
}
```

</details>

---


### Tool call

_source line 2302 · 2026-05-23T08:18:50.974011+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
  "description": "Check existing review issues tracker"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
    "description": "Check existing review issues tracker"
  }
}
```

</details>

---


### Tool result

_source line 2303 · 2026-05-23T08:18:51.928537+00:00_

# Review Issues Tracker — schema_semantic_constrained_ie
# Updated: R21 patches verified + new experiments written, 2026-05-23 05:50

# ============================================================
# Round 21 — Resolved by R22 working session
# ============================================================

- id: "R16-MF3"
  summary: "CF trade-off 在 Abstract 中 framing 偏乐观——仅报告 1.18% 而实际范围达 12.02%"
  category: framing
  severity: critical
  status: resolved
  first_raised_round: 15
  last_seen_round: 21
  mentions:
    - round: 17
      reviewers: [1, 2]
      note: "R17: zero-shot Llama DocRED 12.02% 未在主文叙述出现。"
    - round: 18
      reviewers: [1, 2]
      note: "R18: Abstract 写 'up to 12% zero-shot'，有改善。"
    - round: 19
      reviewers: [1, 2]
      note: "R19: R2-W3 指出 Abstract CF 表述偏乐观。R1 PARTIALLY AGREE。"
    - round: 20
      reviewers: [1, 2]
      note: "R20: R1-N2 + R2-N2 共识。CF framing 从 R15 至今每轮修复被打回。"
    - round: 21
      reviewers: [1, 2]
      note: "R21 MF1: cherry-picking。修正：分层报告 FT (≤1.4%) / ZS (up to 12%)。"
  action_items:
    - round: 19
      action: "Abstract CF 改为审慎表述"
      assigned_to: paper_agent
      status: completed
    - round: 20
      action: "Abstract 核心 claim 后紧跟 CF trade-off 声明"
      assigned_to: paper_agent
      status: completed
    - round: 21
      action: "Abstract 完整重写：CF 分层报告"
      assigned_to: paper_agent
      status: completed
  resolution: "Abstract 完整重写为三段式。CF 分层报告：FT ≤1.4% (line 10), ZS up to 12% (line 11)。beam search eliminates all types at 1.54× latency。已验证。"
  resolution_round: 22

- id: "R19-M2"
  summary: "Abstract 数值过于精确 + 信息密度过高"
  category: writing
  severity: warning
  status: resolved
  first_raised_round: 19
  last_seen_round: 21
  mentions:
    - round: 19
      reviewers: [1, 2]
      note: "R19: R2-W7 + R1 AGREE。"
    - round: 20
      reviewers: [1, 2]
      note: "R20: ≥15 数字、6 缩写。"
    - round: 21
      reviewers: [1, 2]
      note: "R21 SF3: ~150 词中 12+ 数字。建议三段式，≤4-5 个关键数字。"
  action_items:
    - roun
…[truncated 17188 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Bash",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 2304 · 2026-05-23T08:18:52.079706+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/config.yaml 2>/dev/null | grep -A 5 \"external_review\" || echo \"NO_EXTERNAL_REVIEW_CONFIG\"",
  "description": "Check external review config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/config.yaml 2>/dev/null | grep -A 5 \"external_review\" || echo \"NO_EXTERNAL_REVIEW_CONFIG\"",
    "description": "Check external review config"
  }
}
```

</details>

---


### Tool result

_source line 2305 · 2026-05-23T08:18:52.883570+00:00_

NO_EXTERNAL_REVIEW_CONFIG

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Bash",
  "elapsed_ms": 803
}
```

</details>

---


### Tool call

_source line 2306 · 2026-05-23T08:18:53.135283+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/*.tex 2>/dev/null",
  "description": "List all tex files in paper directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/*.tex 2>/dev/null",
    "description": "List all tex files in paper directory"
  }
}
```

</details>

---


### Tool result

_source line 2307 · 2026-05-23T08:18:53.236477+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/abstract_d3264e.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/abstract_fd4b26.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_70b_ablation.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_beam_search.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_case_studies.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_doc_length.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_downstream_analysis.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_full_ft.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_gollie_comparison.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_high_kappa_analysis.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_kappa_case_study.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_llama_per_relation.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/sch
…[truncated 5408 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Bash",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 2308 · 2026-05-23T08:19:14.059843+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/config.yaml 2>/dev/null | head -80",
  "description": "Read project config for external review settings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/config.yaml 2>/dev/null | head -80",
    "description": "Read project config for external review settings"
  }
}
```

</details>

---


### Tool result

_source line 2309 · 2026-05-23T08:19:14.160549+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 2310 · 2026-05-23T08:19:16.872112+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie -name \"config*\" -type f 2>/dev/null",
  "description": "Find project config files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie -name \"config*\" -type f 2>/dev/null",
    "description": "Find project config files"
  }
}
```

</details>

---


### Tool result

_source line 2311 · 2026-05-23T08:19:16.922867+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2312 · 2026-05-23T08:19:22.144463+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_6 -maxdepth 2 -name \"config*\" -type f 2>/dev/null; find /home/ubuntu/.agent-ml-research-idea_gen_0509_6 -maxdepth 2 -name \"*.yaml\" -type f 2>/dev/null | head -20",
  "description": "Find config files in project root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_6 -maxdepth 2 -name \"config*\" -type f 2>/dev/null; find /home/ubuntu/.agent-ml-research-idea_gen_0509_6 -maxdepth 2 -name \"*.yaml\" -type f 2>/dev/null | head -20",
    "description": "Find config files in project root"
  }
}
```

</details>

---


### Tool result

_source line 2313 · 2026-05-23T08:19:22.245486+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_6/idea_generator/ideas.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/global/approvals.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/global/registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/config/crons.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/config/approvals.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/config/backend.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/config/feishu.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/config/venue_registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/config/resources.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/config/pending_approval_notifications.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/workspace.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Bash",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 2314 · 2026-05-23T08:19:26.061103+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_6/workspace.yaml 2>/dev/null | grep -A 10 \"external_review\" || echo \"NOT_IN_WORKSPACE\"; cat /home/ubuntu/.agent-ml-research-idea_gen_0509_6/config/venue_registry.yaml 2>/dev/null | grep -A 10 \"external_review\" || echo \"NOT_IN_VENUE\"",
  "description": "Check external review settings in workspace and venue configs"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_6/workspace.yaml 2>/dev/null | grep -A 10 \"external_review\" || echo \"NOT_IN_WORKSPACE\"; cat /home/ubuntu/.agent-ml-research-idea_gen_0509_6/config/venue_registry.yaml 2>/dev/null | grep -A 10 \"external_review\" || echo \"NOT_IN_VENUE\"",
    "description": "Check external review settings in workspace and venue configs"
  }
}
```

</details>

---


### Tool result

_source line 2315 · 2026-05-23T08:19:26.162036+00:00_

NOT_IN_WORKSPACE
NOT_IN_VENUE

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 2316 · 2026-05-23T08:19:44.005813+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0: 资料检查 + Venue CFP 搜索', 'status': 'completed', 'activeForm': '检查资料完整性并搜索 EMNLP 2026 CFP'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'in_progress', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.6/0.7: 派发视觉审查', 'status': 'pending', 'activeForm': '派发视觉审查'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'pending', 'activeForm': '分配 Reviewer 独立审稿'}, {'content': 'Step 2: 交叉分享', 'status': 'pending', 'activeForm': '交叉分享审稿意见'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断审稿是否收敛'}, {'content': 'Step 4: 汇总报告 & 投递', 'status': 'pending', 'activeForm': '汇总审稿报告并投递'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Step 0: 资料检查 + Venue CFP 搜索', 'status': 'completed', 'activeForm': '检查资料完整性并搜索 EMNLP 2026 CFP'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'in_progress', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.6/0.7: 派发视觉审查', 'status': 'pending', 'activeForm': '派发视觉审查'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'pending', 'activeForm': '分配 Reviewer 独立审稿'}, {'content': 'Step 2: 交叉分享', 'status': 'pending', 'activeForm': '交叉分享审稿意见'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断审稿是否收敛'}, {'content': 'Step 4: 汇总报告 & 投递', 'status': 'pending', 'activeForm': '汇总审稿报告并投递'}]"
  }
}
```

</details>

---


### Tool result

_source line 2317 · 2026-05-23T08:19:44.056560+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "TodoWrite",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2318 · 2026-05-23T08:19:59.823690+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0: 资料检查 + Venue CFP 搜索', 'status': 'completed', 'activeForm': '检查资料完整性并搜索 EMNLP 2026 CFP'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.7: 派发视觉审查', 'status': 'in_progress', 'activeForm': '派发视觉审查'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'in_progress', 'activeForm': '分配 Reviewer 独立审稿'}, {'content': 'Step 2: 交叉分享', 'status': 'pending', 'activeForm': '交叉分享审稿意见'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断审稿是否收敛'}, {'content': 'Step 4: 汇总报告 & 投递', 'status': 'pending', 'activeForm': '汇总审稿报告并投递'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Step 0: 资料检查 + Venue CFP 搜索', 'status': 'completed', 'activeForm': '检查资料完整性并搜索 EMNLP 2026 CFP'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.7: 派发视觉审查', 'status': 'in_progress', 'activeForm': '派发视觉审查'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'in_progress', 'activeForm': '分配 Reviewer 独立审稿'}, {'content': 'Step 2: 交叉分享', 'status': 'pending', 'activeForm': '交叉分享审稿意见'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断审稿是否收敛'}, {'content': 'Step 4: 汇总报告 & 投递', 'status': 'pending', 'activeForm': '汇总审稿报告并投递'}]"
  }
}
```

</details>

---


### Tool result

_source line 2319 · 2026-05-23T08:20:00.077369+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "TodoWrite",
  "elapsed_ms": 253
}
```

</details>

---


### Tool call

_source line 2320 · 2026-05-23T08:20:04.756711+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "schema_semantic_constrained_ie",
  "review_chat_id": "oc_01fc90ae186a4ed432770f7601995139"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "schema_semantic_constrained_ie",
    "review_chat_id": "oc_01fc90ae186a4ed432770f7601995139"
  }
}
```

</details>

---


### Tool result

_source line 2321 · 2026-05-23T08:20:28.011155+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 23254
}
```

</details>

---


### Tool call

_source line 2322 · 2026-05-23T08:20:28.162276+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "project": "schema_semantic_constrained_ie",
  "round_number": "1",
  "text": "你是 Reviewer 1，负责**方法严谨性 + 实验设计**。\n\n## Venue 信息\n- **目标**: EMNLP 2026 (via ACL Rolling Review)\n- **类别**: Long Paper\n- **正文页数限制**: ≤8 页（参考文献不限，Limitations/Ethics 不计入）\n- **模板**: ACL style, `\\usepackage[review]{acl}`\n- **匿名规则**: Double-blind\n- **ARR 提交截止**: 2026-05-25\n- **Commitment 截止**: 2026-08-02\n- **Overall Assessment 评分标准**: 5=Consider for Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 论文文件\n- LaTeX 源码: `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_23/submitted.pdf`\n\n## 你的审查侧重\n\n### 1. 方法形式化（§3 Method + §4 Composition）\n- Proposition 1 的形式论证是否严密？假设条件是否合理？\n- 约束编译流程（grammar layer + semantic layer）的技术描述是否清晰、完整、可复现？\n- Continuation masking 的正确性论证是否充分？\n- 约束组合的 enabling dependency 声称是否有足够证据支撑？\n\n### 2. 实验设计与统计严谨性（§5 Experiments）\n- 消融实验是否完整覆盖了所有约束层的贡献？\n- 统计检验（bootstrap CI, Cohen's d 等）是否正确使用？\n- Baseline 选择是否公平、充分？是否有遗漏的重要 baseline？\n- 跨模型（Qwen/Llama/Mistral）和跨数据集（SciERC/DocRED/WikiEvents）的实验覆盖是否足够？\n\n### 3. 结果解读与 Claim 一致性\n- 实验结果是否支持论文声称的 claims？是否有 over-claiming？\n- CF (Cross-Field) trade-off 的讨论是否诚实、充分？\n- WikiEvents (n=20) 的结论是否过度泛化？\n- 70B 实验（AWQ INT4）的限制是否充分披露？\n\n### 4. 可复现性\n- 超参数、prompt 模板、训练细节是否足够详细？\n- 代码/数据/模型的可获取性是否说明？\n\n请按以下结构输出审稿意见：\n1. **Summary**（2-3 句概述）\n2. **Strengths**（逐条，标注 S1, S2, ...）\n3. **Weaknesses**（逐条，标注 W1, W2, ...，区分 Critical / Major / Minor）\n4. **Questions**（标注 Q1, Q2, ...）\n5. **Missing References**（如有）\n6. **Overall Assessment**（评分 + 置信度 + 一句话总结）\n7. **Detailed Comments**（逐节细评，如有）"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "project": "schema_semantic_constrained_ie",
    "round_number": "1",
    "text": "你是 Reviewer 1，负责**方法严谨性 + 实验设计**。\n\n## Venue 信息\n- **目标**: EMNLP 2026 (via ACL Rolling Review)\n- **类别**: Long Paper\n- **正文页数限制**: ≤8 页（参考文献不限，Limitations/Ethics 不计入）\n- **模板**: ACL style, `\\usepackage[review]{acl}`\n- **匿名规则**: Double-blind\n- **ARR 提交截止**: 2026-05-25\n- **Commitment 截止**: 2026-08-02\n- **Overall Assessment 评分标准**: 5=Consider for Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 论文文件\n- LaTeX 源码: `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_23/submitted.pdf`\n\n## 你的审查侧重\n\n### 1. 方法形式化（§3 Method + §4 Composition）\n- Proposition 1 的形式论证是否严密？假设条件是否合理？\n- 约束编译流程（grammar layer + semantic layer）的技术描述是否清晰、完整、可复现？\n- Continuation masking 的正确性论证是否充分？\n- 约束组合的 enabling dependency 声称是否有足够证据支撑？\n\n### 2. 实验设计与统计严谨性（§5 Experiments）\n- 消融实验是否完整覆盖了所有约束层的贡献？\n- 统计检验（bootstrap CI, Cohen's d 等）是否正确使用？\n- Baseline 选择是否公平、充分？是否有遗漏的重要 baseline？\n- 跨模型（Qwen/Llama/Mistral）和跨数据集（SciERC/DocRED/WikiEvents）的实验覆盖是否足够？\n\n### 3. 结果解读与 Claim 一致性\n- 实验结果是否支持论文声称的 claims？是否有 over-claiming？\n- CF (Cross-Field) trade-off 的讨论是否诚实、充分？\n- WikiEvents (n=20) 的结论是否过度泛化？\n- 70B 实验（AWQ INT4）的限制是否充分披露？\n\n### 4. 可复现性\n- 超参数、prompt 模板、训练细节是否足够详细？\n- 代码/数据/模型的可获取性是否说明？\n\n请按以下结构输出审稿意见：\n1. **Summary**（2-3 句概述）\n2. **Strengths**（逐条，标注 S1, S2, ...）\n3. **Weaknesses**（逐条，标注 W1, W2, ...，区分 Critical / Major / Minor）\n4. **Questions**（标注 Q1, Q2, ...）\n5. **Missing References**（如有）\n6. **Overall Assessment**（评分 + 置信度 + 一句话总结）\n7. **Detailed Comments**（逐节细评，如有）"
  }
}
```

</details>

---


### Tool result

_source line 2323 · 2026-05-23T08:20:48.409077+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 20246
}
```

</details>

---


### Tool call

_source line 2324 · 2026-05-23T08:20:48.761927+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "project": "schema_semantic_constrained_ie",
  "round_number": "1",
  "text": "你是 Reviewer 2，负责**新颖性 + 完整性 + 写作质量**。\n\n## Venue 信息\n- **目标**: EMNLP 2026 (via ACL Rolling Review)\n- **类别**: Long Paper\n- **正文页数限制**: ≤8 页（参考文献不限，Limitations/Ethics 不计入）\n- **模板**: ACL style, `\\usepackage[review]{acl}`\n- **匿名规则**: Double-blind\n- **ARR 提交截止**: 2026-05-25\n- **Commitment 截止**: 2026-08-02\n- **Overall Assessment 评分标准**: 5=Consider for Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 论文文件\n- LaTeX 源码: `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_23/submitted.pdf`\n\n## 你的审查侧重\n\n### 1. 新颖性评估\n- 论文的核心贡献（schema-compiled constrained decoding for IE）相对于现有工作（GCD, BoostCD, GoLLIE, KnowCoder, ADELIE, XGrammar, SGLang）的增量贡献有多大？\n- 是算法创新还是系统集成？如果是后者，集成的价值是否通过实验充分展示？\n- §4 Constraint Composition 的理论分析是否构成独立贡献？\n\n### 2. 相关工作覆盖（§6 + 全文）\n- 是否遗漏重要相关工作？特别关注 2025-2026 年的最新工作\n- 与同类方法（特别是 GCD, BoostCD, DCCD, Thinking Before Constraining）的定位和区分是否清晰？\n- Text2Event, UIE, USM 等统一 IE 框架是否需要讨论？\n- Constrained decoding 在 NL-to-SQL / code generation 等领域的工作是否有借鉴价值？\n\n### 3. 写作质量与论文组织\n- Abstract 是否准确反映论文贡献？信息密度是否合适？\n- Introduction 的 motivation 和 contribution list 是否清晰？\n- 各节的篇幅分配是否合理（特别是 zero-shot vs fine-tuned 的比例）？\n- Limitations 是否诚实、全面？\n- 全文叙事是否连贯？术语使用是否一致？\n\n### 4. 格式合规\n- 正文是否 ≤8 页？\n- 匿名规则是否遵守（无作者信息泄露、无自引暴露身份）？\n- 图表质量、标题、标注是否规范？\n- 引用格式是否正确（natbib）？\n- Limitations section 是否在正文中（不在 appendix）？\n\n### 5. 完整性检查\n- Appendix 是否有重要信息应该在主文中？\n- 是否有未完成的 TODO / placeholder？\n- 参考文献是否完整、准确？\n\n请按以下结构输出审稿意见：\n1. **Summary**（2-3 句概述）\n2. **Strengths**（逐条，标注 S1, S2, ...）\n3. **Weaknesses**（逐条，标注 W1, W2, ...，区分 Critical / Major / Minor）\n4. **Questions**（标注 Q1, Q2, ...）\n5. **Missing References**（如有）\n6. **Overall Assessment**（评分 + 置信度 + 一句话总结）\n7. **Detailed Comments**（逐节细评，如有）"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "project": "schema_semantic_constrained_ie",
    "round_number": "1",
    "text": "你是 Reviewer 2，负责**新颖性 + 完整性 + 写作质量**。\n\n## Venue 信息\n- **目标**: EMNLP 2026 (via ACL Rolling Review)\n- **类别**: Long Paper\n- **正文页数限制**: ≤8 页（参考文献不限，Limitations/Ethics 不计入）\n- **模板**: ACL style, `\\usepackage[review]{acl}`\n- **匿名规则**: Double-blind\n- **ARR 提交截止**: 2026-05-25\n- **Commitment 截止**: 2026-08-02\n- **Overall Assessment 评分标准**: 5=Consider for Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 论文文件\n- LaTeX 源码: `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_23/submitted.pdf`\n\n## 你的审查侧重\n\n### 1. 新颖性评估\n- 论文的核心贡献（schema-compiled constrained decoding for IE）相对于现有工作（GCD, BoostCD, GoLLIE, KnowCoder, ADELIE, XGrammar, SGLang）的增量贡献有多大？\n- 是算法创新还是系统集成？如果是后者，集成的价值是否通过实验充分展示？\n- §4 Constraint Composition 的理论分析是否构成独立贡献？\n\n### 2. 相关工作覆盖（§6 + 全文）\n- 是否遗漏重要相关工作？特别关注 2025-2026 年的最新工作\n- 与同类方法（特别是 GCD, BoostCD, DCCD, Thinking Before Constraining）的定位和区分是否清晰？\n- Text2Event, UIE, USM 等统一 IE 框架是否需要讨论？\n- Constrained decoding 在 NL-to-SQL / code generation 等领域的工作是否有借鉴价值？\n\n### 3. 写作质量与论文组织\n- Abstract 是否准确反映论文贡献？信息密度是否合适？\n- Introduction 的 motivation 和 contribution list 是否清晰？\n- 各节的篇幅分配是否合理（特别是 zero-shot vs fine-tuned 的比例）？\n- Limitations 是否诚实、全面？\n- 全文叙事是否连贯？术语使用是否一致？\n\n### 4. 格式合规\n- 正文是否 ≤8 页？\n- 匿名规则是否遵守（无作者信息泄露、无自引暴露身份）？\n- 图表质量、标题、标注是否规范？\n- 引用格式是否正确（natbib）？\n- Limitations section 是否在正文中（不在 appendix）？\n\n### 5. 完整性检查\n- Appendix 是否有重要信息应该在主文中？\n- 是否有未完成的 TODO / placeholder？\n- 参考文献是否完整、准确？\n\n请按以下结构输出审稿意见：\n1. **Summary**（2-3 句概述）\n2. **Strengths**（逐条，标注 S1, S2, ...）\n3. **Weaknesses**（逐条，标注 W1, W2, ...，区分 Critical / Major / Minor）\n4. **Questions**（标注 Q1, Q2, ...）\n5. **Missing References**（如有）\n6. **Overall Assessment**（评分 + 置信度 + 一句话总结）\n7. **Detailed Comments**（逐节细评，如有）"
  }
}
```

</details>

---


### Tool result

_source line 2325 · 2026-05-23T08:20:50.227572+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1465
}
```

</details>

---


### Assistant

_source line 2326 · 2026-05-23T08:20:54.175731+00:00_

视觉审查已派发，Reviewer 1 和 Reviewer 2 已分配任务，均已确认接收。等待两位 Reviewer 返回独立审稿意见。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director"
}
```

</details>

---


## Round 166

## Round 166

4 recorded events


### User

_source line 2327 · 2026-05-23T08:27:09.145732+00:00_

[Reviewer 1 审稿意见]:

## Reviewer 1 审稿意见：OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints

---

## 总体评分
**Overall**: 3.5 / 5 (Borderline Conference)
**一句话总结**: 工程扎实、评估极其详尽的约束解码框架，但跨域实体类型一致性（CF）这一核心遗留问题占残余违规的64%、WikiEvents评估统计效力不足、以及Proposition 1的实际意义论证不够充分，使其介于Conference和Findings之间。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 4 / 5 | 方法形式化严密，Proposition 1证明正确，bootstrap CI和Cohen's d使用规范，但CF gap的影响被低估 |
| Excitement | 3.5 / 5 | 将IE本体编译为可组合约束层的思路新颖且实用，enabling dependency发现有洞察力，但受限于CF未解决和实际ontology规模的scalability疑虑 |
| Reproducibility | 4 / 5 | 超参数、prompt模板、硬件、种子均详尽报告（Appendix G），但代码/数据"upon acceptance"释放，无法当前验证 |
| Confidence | 4 / 5 | 约束解码+结构化IE是本人研究方向，论文技术细节已逐节验证 |

---

## Summary

本文提出OntoCoDec，将IE本体编译为两层可组合的token级解码约束：grammar layer（基于XGrammar的CFG，强制JSON结构和词汇成员关系）和semantic layer（有状态logits处理器，通过动态entity registry强制domain/range类型约束）。论文在SciERC、DocRED、WikiEvents上评估了Qwen3-8B、Llama-3.1-8B、Mistral-7B（含70B AWQ INT4），提供了五路消融、bootstrap统计检验、beam search兼容性验证等极其详尽的实验分析。核心贡献是约束可判定性分类（三级）和两层间的经验性enabling dependency发现。

---

## Strengths

**S1** [方法设计] 约束可判定性分类（Level 1: context-free → Level 2: prefix-decidable with state → Level 3: non-local）概念清晰，精准界定了CFG能做和不能做的边界（§3, p.3）。grammar-first fallback机制（§4, p.5, eq.2）在soundness和availability之间取得了合理平衡。

**S2** [形式化] Proposition 1（p.3, 完整证明Appendix O, p.37-38）的pumping lemma论证结构正确：对于无界entity集合，独立选择的类型对产生cross-serial依赖，PDA无法处理。Remark（p.3）中关于有限集合DFA指数爆炸的补充说明区分了理论不可能性和工程不可行性。

**S3** [评估深度] 实验分析的彻底程度在NLP论文中极为罕见：五路消融（Table 1）、bootstrap CI + Cohen's d（Table 8, Appendix C）、fallback因果追踪（Table 6-7, Appendix C）、cross-field违规分解（Table 9）、document长度分箱分析（Tables 32-34, Appendix H）、prompt敏感性（Table 35, Appendix I）、TCR post-hoc resolution（Tables 43-44, Appendix M）、beam search兼容性（Tables 24-29, Appendix F）。39页附录覆盖了我能想到的几乎所有消融维度。

**S4** [统计规范] Bootstrap CI采用document-level resampling（10,000 iterations, seed=42），报告了MDE（Table 31, Appendix C：SciERC ±1.8pp, DocRED ±0.8pp, WikiEvents ±5.0pp），并诚实承认"n=6 is insufficient for statistical inference on this correlation"（p.20）。这种统计纪律在IE领域论文中少见。

**S5** [Enabling dependency] 两层间的scale-dependent enabling dependency（grammar alone 84% DR at 8B vs. 24% semantic-only, Table 1; 70B时grammar alone达到semantic layer的水平, Table 3/§5.3）是有意义的经验发现，对约束解码系统设计有指导价值。

**S6** [工程贡献] Tokenizer-agnostic continuation masking（§3.3, p.4）通过byte-level BPE分解处理多token类型名，适配Qwen/Llama/SentencePiece三种分词器，实际工程价值高。ontology scalability分析（Appendix K, Table 41）展示了编译时间sub-linearly scaling至XLarge (1000 entity types)。

---

## Weaknesses

**W1** [Critical] **Cross-field (CF) 类型一致性占残余违规的64%，但正文讨论不足**
- 具体位置：Table 9 (p.21-22), §4 (p.5), Limitations (p.9)
- 问题：Table 9显示，在S1配置下SciERC的245个残余违规中，GENERIC↔OtherScientificTerm占34.7%，GENERIC↔Material占12.3%，总计CF违规占63.9%（155/245）。这是方法论的根本缺口——论文标题声称"Type-Constrained IE"，但最主要的类型约束违规（跨triple的实体类型一致性）未被处理。正文§4仅用一句"Level 3 is addressed by beam search or post-hoc resolution"（p.3）带过，但Appendix M的TCR（Tables 43-44）在zero-shot下仅处理0-2%的CF冲突，效果有限。Limitations（p.9）提到CF但未量化其严重程度（64%这个数字只出现在附录）。
- 为什么影响接收：一个声称解决type constraint的系统，其最大残余问题恰好是type constraint，这构成了core claim和实际效果之间的gap。Reviewer和AC会注意到这一点。
- 建议修改方向：(1) 在正文§5.1或§4中明确量化CF占残余违规的比例；(2) 讨论CF问题为何从架构上难以在单pass解码中解决（而非仅说"left to future work"）；(3) 考虑将标题修改为更精确的表述，如"Domain/Range-Constrained"。

**W2** [Major] **Proposition 1的实际意义论证存在gap**
- 具体位置：Proposition 1 (p.3), Remark (p.3), Appendix O (p.37-38)
- 问题：Proposition 1证明的是*无界entity集合*下domain/range约束不是context-free——但所有实际IE场景中entity集合都有界（受文档长度限制）。论文在Remark中提到有限集合的DFA需要O(|T^{|entity|}|)个状态"exceeding 10^10 for DocRED"，但这是一个工程可行性论证（编译DFA不现实），而非形式上不可能。这两个论点——理论上超越CFG vs. 工程上DFA不可行——之间的逻辑跳跃需要更清晰地阐明。当前的表述可能让读者误以为domain/range约束在任何条件下都不可能用CFG强制执行，但实际上对于固定schema的finite entity集合（如SciERC的7个entity types），构造CFG是可行的，只是状态空间庞大。
- 建议：在正文中明确区分"formal impossibility for unbounded sets"和"engineering intractability for bounded sets"，说明OntoCoDec的stateful approach同时解决了这两个层面的问题。

**W3** [Major] **WikiEvents (n=20) 的结论统计效力不足，但在正文中占据整个§5.4**
- 具体位置：§5.4 (p.7), Table 4 (p.7), Table 31 (p.31)
- 问题：WikiEvents评估仅20个文档，MDE为±5.0pp（Table 31），这意味着只有大于5个百分点的F1差异才能被检测到。§5.4报告了"constrained zero-shot settings"下的数字并得出"Compatibility with fine-tuning is preliminary (n=20)"，但同时展示了Tables 4中的详细结果（zero-shot across 3 models + fine-tuning），给人以此结果可靠的印象。更重要的是，§5.4的fine-tuning结果（"CF remains low (0.77-1.18%); per-relation patterns extend"）在n=20下几乎无法得出任何可靠结论。
- 建议：(1) 将§5.4的篇幅大幅缩减，标题改为"Preliminary Event Extraction Pilot"；(2) 在Table 4的caption中注明"n=20, MDE=5.0pp, results are directional only"；(3) 不要在n=20上报告fine-tuning composability结论。

**W4** [Major] **70B实验的INT4量化限制未充分披露**
- 具体位置：§5.3 (p.7-8), Table 48 (p.39, Appendix P)
- 问题：Abstract声称"with 70B-class validation (§5.3)"，但70B实验全部在AWQ INT4上运行。Table 48显示INT4 vs FP16在SciERC上R-F1差异为-0.09，但DocRED的E-F1 drop为-7.07（INT4: 84.87 vs FP16: 91.94）。论文解释这是"parse failure"导致而非约束干扰，但这意味着INT4下的constraint enforcement结果可能被量化噪声污染。正文§5.3说"cross-family generalization at 70B scale remains to be verified"，但这个caveat出现在第8页最后一段，而Abstract的表述让读者以为70B验证是solid的。
- 建议：(1) Abstract中明确标注"70B (AWQ INT4)"；(2) 在§5.3开头而非结尾说明量化限制。

**W5** [Major] **缺少与训练基方法的系统性对比**
- 具体位置：§6 Related Work (p.8), Table 49 (Appendix Q, p.39)
- 问题：论文声称OntoCoDec"is composable with fine-tuning"（§5.1），但缺少与专门训练来满足schema约束的方法（如ADELIE, CodeIE, UIE）在相同benchmark上的直接对比。Appendix Q与GoLLIE的对比仅在SciERC 100 docs上进行，且GoLLIE在其中产生了54%空输出（仅5个有效预测），这个对比的信息量有限——它更多说明GoLLIE在这个prompt设置下不work，而非OntoCoDec更好。论文的核心positioning是"decoding-time enforcement vs. training-based internalization"，但没有fair comparison来支撑这个positioning。
- 建议：(1) 在主要benchmark上与至少一个schema-aware训练方法（如GoLLIE在其原始设置下、或ADELIE）进行完整对比；(2) 如果训练方法在不同evaluation protocol下运行，明确说明为何直接对比不可行。

**W6** [Minor] **Grammar-first fallback频率的模型依赖性未在正文讨论**
- 具体位置：Table 6 (p.19, Appendix C)
- 问题：Qwen3-8B在SciERC上0次fallback，但Llama-3.1-8B触发5,882次fallback（10.7 per document），Llama-3.1-8B在S1下33/36 residual violations来自fallback positions。这意味着框架的行为在不同模型上有质的差异——Qwen基本不需要fallback，而Llama严重依赖它。这个差异只在附录中讨论，但它影响了框架的通用性声称。
- 建议：在正文§5.1或§4中简要讨论fallback频率的模型依赖性及其对实践部署的影响。

**W7** [Minor] **Continuation masking的"distinguishable token-prefix"假设**
- 具体位置：§3.3 (p.4), Limitations (p.9)
- 问题：§3.3假设"each entity type name maps to a distinguishable token-prefix sequence"。Limitations提到"entity types exceed ~200, prefix collisions in the tokenizer vocabulary may require fallback to multi-token disambiguation"。但论文未展示实际prefix collision的frequency或其对masking correctness的影响。对于具有形态学相似类型名的ontology（如Protein vs. Protein_Complex vs. Protein_Domain），collision可能不罕见。
- 建议：在附录中增加一个prefix collision频率分析，至少覆盖所用的三个ontology。

---

## Questions

**Q1** Grammar-first fallback在semantic mask与grammar mask不相交时触发（§4, eq.2: S(t)∩G(t)=∅ → fallback to G(t)）。但fallback本质上放弃了类型约束。是否考虑过替代策略，如backtracking到最近的type-bearing position重新生成？这会引入什么样的latency cost？

**Q2** Table 10（p.22）显示Per-Relation DR elimination under fine-tuning中，EVALUATE-FOR的654+653个token-level masking中，head entity的registered type falls outside EVALUATE-FOR's domain——这意味着semantic mask经常与fine-tuned model的预测冲突。这是否暗示fine-tuning和constraint enforcement在某些relation上学到了不同的type preference？

**Q3** Appendix K（Table 41）的ontology scalability测试最大到XLarge（1000 entity types, 1000 relations）。但real-world知识图谱（如Wikidata有约10,000+ property types）远超此规模。论文是否测试过或估计过在更大规模ontology下的编译时间和runtime overhead？

**Q4** 论文的entity registry（§3.3）假设entity在relation之前生成（由grammar layer强制）。但某些IE任务（如pipeline RE）可能需要先生成relation再填充argument。OntoCoDec是否fundamentally限于entity-first的生成顺序？

**Q5** Cohen's d是从pooled bootstrap SD计算的（Table 8, Appendix C）。这与传统Cohen's d（从样本SD计算）有区别。请clarify这个选择的理由以及它对effect size解读的影响。

---

## Missing References

无明显遗漏。Related Work（§6, p.8 + Appendix B, p.14-17）覆盖了主要方向：grammar-constrained decoding（XGrammar, Outlines, SynCode, SGLang）、schema-aware IE（GoLLIE, KnowCoder, GUIDEX, CodeIE）、vocabulary and type-constrained generation（Roth & Yih 2004, Riedel 2010, UIE, REBEL, InstructUIE, ADELIE）。建议补充：
- Josifoski et al., 2022 (GenIE) 已引用但未在Related Work中充分讨论其constraint enforcement机制
- 如果空间允许，可考虑引用 Paolini et al., 2021 (TANL) 作为另一种structured generation baseline

---

## Overall Assessment

**评分: 3.5 (Borderline Conference)**
**置信度: 4/5**

本文的核心贡献——将IE本体编译为两层可组合解码约束——思路清晰，工程实现扎实，评估在统计规范性上显著优于同领域平均水平。Proposition 1的形式化、enabling dependency的经验发现、以及tokenizer-agnostic continuation masking都是有价值的贡献。

然而，三个问题让我无法给出Conference评分：(1) CF类型一致性占残余违规64%且未被解决，与"Type-Constrained IE"标题形成gap；(2) WikiEvents (n=20) 和70B (INT4) 的评估统计效力不足，但在正文中的呈现方式可能误导读者认为结论比实际更robust；(3) 缺少与训练基方法的fair comparison，削弱了核心positioning。

如果作者能在revision中：(a) 在正文显著讨论CF gap并修正标题/claim；(b) 缩减WikiEvents结论的scope；(c) 补充至少一个training-based baseline的fair comparison，评分可提升至4.0 (Conference)。

---

## Detailed Comments

### §3 Method
- §3.1 Problem Formulation: "context-free; (b) is context-sensitive but prefix-decidable"（p.2）——这个表述暗示domain/range约束是context-sensitive language class，但Proposition 1证明的是"not context-free"，严格来说不等于context-sensitive。建议使用"beyond context-free"的表述。
- §3.3 Semantic Layer: "continuation masking to handle context-dependent tokenizations and prefix-shared types"（p.4）——技术描述清晰，但缺少一个具体的multi-token type masking的worked example（如Protein → "Prot"+"ein" vs. Protein_Complex → "Prot"+"ein"+"_Com"+"plex"的token序列如何被区分）。

### §4 Constraint Composition
- Eq. (2)的conjunction是asymmetric的（"S(t) is defined only over G(t)"），但这个关键设计选择的motivation可以更清晰——为什么不是symmetric？因为semantic layer依赖grammar layer保证的JSON结构来定位type-bearing positions。建议添加一句明确的解释。

### §5 Experiments
- Table 1的五路消融非常informative，但缺少一个条件："S2-only"（fine-tuning composability without grammar/semantic constraints）。当前的"Unconstrained"行 + "S1+S2"行间的差异包含了多个因素，增加S2-only可以更cleanly isolate composability的贡献。
- §5.2 (p.6): "R-F1 improves by +0.7pp; the unchanged DR confirms..."——但Table 3 DocRED行的Llama S1 R-F1是2.53，而Unconstrained是36.07/10.21。这些数字之间的关系需要更清晰地解释（不同行对应不同模型/数据集组合）。
- §5.3的70B-class validation: "beam (k=1) eliminates all violations"（p.7）——但k=1就是greedy decoding，不算beam search。beam search compatibility的claim应基于k>1的结果（Appendix F, Table 24-29）。

### Limitations (p.9)
- 覆盖了CF、continuation masking scalability、evaluation coverage、70B quantization。总体诚实全面。但建议量化CF gap的数字（64%），这是读者最需要知道的。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 2328 · 2026-05-23T08:27:23.444488+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0: 资料检查 + Venue CFP 搜索', 'status': 'completed', 'activeForm': '检查资料完整性并搜索 EMNLP 2026 CFP'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.7: 派发视觉审查', 'status': 'completed', 'activeForm': '派发视觉审查'}, {'content': 'Step 1: Round 1 独立审稿 — Reviewer 1 已返回，等待 Reviewer 2', 'status': 'in_progress', 'activeForm': '等待 Reviewer 2 返回审稿意见'}, {'content': 'Step 2: 交叉分享', 'status': 'pending', 'activeForm': '交叉分享审稿意见'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断审稿是否收敛'}, {'content': 'Step 4: 汇总报告 & 投递', 'status': 'pending', 'activeForm': '汇总审稿报告并投递'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Step 0: 资料检查 + Venue CFP 搜索', 'status': 'completed', 'activeForm': '检查资料完整性并搜索 EMNLP 2026 CFP'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.7: 派发视觉审查', 'status': 'completed', 'activeForm': '派发视觉审查'}, {'content': 'Step 1: Round 1 独立审稿 — Reviewer 1 已返回，等待 Reviewer 2', 'status': 'in_progress', 'activeForm': '等待 Reviewer 2 返回审稿意见'}, {'content': 'Step 2: 交叉分享', 'status': 'pending', 'activeForm': '交叉分享审稿意见'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断审稿是否收敛'}, {'content': 'Step 4: 汇总报告 & 投递', 'status': 'pending', 'activeForm': '汇总审稿报告并投递'}]"
  }
}
```

</details>

---


### Tool result

_source line 2329 · 2026-05-23T08:27:23.445044+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---


### Assistant

_source line 2330 · 2026-05-23T08:27:25.186434+00:00_

Reviewer 1 审稿意见已收到。评分 3.5 (Borderline Conference)，核心问题集中在 CF 残余违规占比 64%、WikiEvents 统计效力不足、缺少训练基方法对比。

等待 Reviewer 2 返回后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director"
}
```

</details>

---


## Round 167

## Round 167

2 recorded events


### User

_source line 2331 · 2026-05-23T08:27:27.752295+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

核心判断：**3.5 / 5 (Borderline Conference)**。

主要发现：
- **优势**：方法形式化严密（Proposition 1证明正确），评估深度在IE领域罕见（39页附录，bootstrap CI + Cohen's d），enabling dependency是有洞察力的经验发现，tokenizer-agnostic continuation masking工程价值高。
- **关键问题**：(1) Cross-field类型一致性占残余违规64%但未解决，与标题"Type-Constrained IE"形成gap；(2) WikiEvents (n=20, MDE=5.0pp) 统计效力不足但结论呈现过于自信；(3) 70B实验全在AWQ INT4上，Abstract未标注；(4) 缺少与训练基方法的系统性对比。

如果作者在revision中显著讨论CF gap、缩减WikiEvents结论scope、补充training-based baseline对比，评分可提升至4.0。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 2332 · 2026-05-23T08:27:34.829911+00:00_

Reviewer 1 审稿意见已记录，等待 Reviewer 2 返回。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director"
}
```

</details>

---


## Round 168

## Round 168

8 recorded events


### User

_source line 2333 · 2026-05-23T08:28:41.512514+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 审稿意见：OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints

---

## Summary

本文提出 OntoCoDec，一个将 IE 本体编译为可组合 token 级解码约束的框架。通过形式化分析（Proposition 1）证明 domain/range 类型约束超越上下文无关文法的表达能力，由此设计两层架构：grammar layer（基于 XGrammar 的 CFG 约束）和 semantic layer（基于动态实体注册表的运行时类型掩码）。在 SciERC、DocRED、WikiEvents 三个数据集上，跨 4 个模型（8B–70B）、2 种精度（FP16/INT4）进行了全面评估。LoRA 微调 + greedy S1 近乎消除 domain/range 违规（DR<0.1%），beam search（k=4）消除所有违规类型，延迟开销 10%–54%。

---

## Strengths

**S1: 全面且严谨的实验评估。** 论文在 3 个数据集、4 个模型（3 种 tokenizer 族）、2 种精度上进行评估，包含五路消融（Table 1）、cross-model 验证（Table 3）、fine-tuning 可组合性（Table 2）、70B 验证、beam search 兼容性。统计报告包含 bootstrap CIs、p 值、Bonferroni 校正。这一评估深度在该领域内较为罕见。

**S2: 诚实透明的呈现方式。** 论文明确承认 DR enforcement 引入 CF 违规、zero-shot 质量低、WikiEvents 结果是初步的。Limitations 部分极为详细，覆盖约束范围、评估覆盖度、工程局限。这种诚实态度值得肯定。

**S3: 实用的系统设计。** 两层架构配合 grammar-first fallback 有清晰的工程动机。延迟开销适度（greedy +10%，beam 1.54×）。编译速度快（<0.5s）。可扩展性测试显示在 200 实体类型 / 1000 关系时保持恒定 2–3% 开销（Appendix M）。

**S4: 充分的相关工作覆盖。** 主文（§6）和扩展附录（Appendix B）全面覆盖 grammar-constrained decoding（XGrammar、Outlines、LMQL）、schema-aware IE（GoLLIE、KnowCoder、ADELIE）、代码领域语义约束解码（PICARD、Synchromesh、MGD）、后验验证（ODKE+、OntoLogX）、约束解码质量影响（CRANE、FormaTTax）。对 DCCD 和 Thinking Before Constraining 的定位也清晰。

**S5: Tokenizer 无关设计的跨模型泛化。** 在三种 tokenizer 族（byte-level BPE: Qwen/Llama, SentencePiece: Mistral）上验证了 continuation masking 的有效性，这是一个重要的工程贡献。

---

## Weaknesses

**W1 [Major]: 算法创新有限，主要是系统集成贡献。** 论文自我定位为"systematic engineering contribution with theoretical grounding"（§1, line 23），这是诚实的，但也暴露了核心问题。Proposition 1（IE 类型约束超越 CFG 表达能力）在形式语言理论社区是 well-known 的结论，对任何了解 PDA 局限性的研究者来说并不意外。证明本身（Appendix G）是严格的，但结论缺乏 surprise value。核心设计决策——XGrammar 处理结构 + stateful logits processor 处理语义——是自然且直觉的组合。§4 Constraint Composition 文档化了设计决策（grammar-first fallback、constraint tightness κ），但不构成独立理论贡献。κ 与 DR reduction 的相关性在 n=3 下 p=0.138（§4），统计不显著，作为分析工具的价值有限。

**W2 [Major]: CF 违规 trade-off 显著削弱核心价值主张。** S1 enforcement 因 per-triple 独立强制执行而创建 CF 违规：zero-shot 高达 12.02%（DocRED Llama，Table 3），fine-tuned 下 ≤1.18%（SciERC Qwen，Table 2）。这意味着系统将一类违规（DR: ontologically invalid）替换为另一类（CF: cross-triple type inconsistency）。虽然论文正确指出 CF 严重性低于 DR（CF 可通过 post-hoc TCR 缓解，Appendix O），但 "编译本体 → 强制约束 → 获得有效输出" 的干净叙事被打破。仅 beam search（k=4, 1.54× latency）完全解决两类违规，使延迟最优的 greedy 部署层成为不完整方案。实际部署中，用户必须在"容忍 CF"和"支付 beam 延迟"之间选择——这个 trade-off 在 abstract 和 introduction 中被低估了。

**W3 [Major]: Zero-shot 结果占据大量主文篇幅但缺乏实用价值。** Zero-shot R-F1 在所有模型上仅 4–8%（Table 3），远低于可用质量。论文将其定位为"diagnostic probe"（§5 开头），但约 3/8 页篇幅用于 zero-shot 实验（§5.1 zero-shot 诊断、§5.2 DocRED、§5.3 cross-model），这些实验展示的是对功能上不可用的提取器的约束执行。相比之下，真正有实用价值的 fine-tuning composability（Table 2）仅获得约 1 页篇幅。建议重新分配：压缩 zero-shot 为 1 个总结段落+1 个表格，扩展 fine-tuning 分析。

**W4 [Minor]: GoLLIE 比较不公平。** Appendix F（Table 8）比较 GoLLIE-7B zero-shot（R-F1=0.0, 5 predictions）vs. OntoCoDec LoRA fine-tuned（R-F1=43–45, ~1100 predictions）。GoLLIE 在未经 fine-tune 的 schema 上近乎 abstain 是预期行为。公平比较应为：(a) 两者都 zero-shot，或 (b) 两者都 fine-tuned on SciERC。当前比较在主文 §6 中被引用（"GoLLIE-7B eliminates DR at severe coverage cost (R-F1=0.0)"），可能误导读者认为 GoLLIE 本质上是低质量的。

**W5 [Minor]: WikiEvents 结果过于初步，不应作为贡献声明。** n=20 测试文档，bootstrap CIs ±3–5 pp（Table 4 caption），统计效力不足以支持可靠结论。论文 power analysis（Appendix I）也承认这点。Introduction contribution list 中 "preliminary pilot study on WikiEvents (n=20 test documents) validates event extraction applicability (§5.4)" 过度推销了一个统计效力很弱的结果。

**W6 [Minor]: Limitations 部分过长。** 约 1.5 页的 Limitations 覆盖三个详细段落。EMNLP 2026 指南规定 Limitations "do not count towards this page limit, provided they do not contain excessive additional content"。当前长度接近"excessive"的边界。部分内容（如 residual DR 分解的具体数字、TCR 讨论、full fine-tuning 对比）可移至 appendix。

**W7 [Minor]: 表述重复。** "empirical enabling dependency"（grammar-only 8B 24% DR reduction, semantic-only 24%, combined 94%）在 abstract、§1、§3 Empirical Observation、§3.4、§4、§5.1 中重复出现至少 6 次。虽然是重要观察，但如此密集的重复消耗了宝贵的主文篇幅。

---

## Questions

**Q1:** 类型约束从训练数据中提取（§5 Setup），覆盖率 99%+。剩余 ~1% 未覆盖的合法类型对会被系统性阻断。是否评估过约束引入的 false negatives 对 recall 的影响？Downstream impact（§5.1 末尾）报告 0.49% 被移除三元组匹配 gold label，但这只是被约束移除的部分。是否存在因约束而根本未被生成的合法三元组？

**Q2:** DocRED 上 grammar-only *增加* DR（18.46%→26.17%，§5.2 "latent violation surfacing"）。这表明 grammar constraints 可以迫使模型进入一个类型错误更多的受限空间。这种效应在 fine-tuning 后是否持续？如果是，是否意味着 grammar layer 在某些 schema 下实际上是有害的？

**Q3:** Beam search (k=4) 消除所有违规。是否探索过 k=2 作为折中？论文仅展示 k=4；理解 k 与违规消除的关系对实际部署指导很重要。

**Q4:** Entity registry 在生成过程中增量构建（§3.3）。当模型对同一实体名生成不同类型时，first-seen type 是否始终被采用？这似乎是 CF 违规的主要来源，但机制在主文中解释不够清晰。§4 "greedy limitation" 段提及但未详细展开。

**Q5:** Constraint tightness κ 的定义（§4）中，SciERC κ̄=0.333, DocRED κ̄=0.842, WikiEvents κ̄=0.029。在 n=3 下无法建立有意义的统计关系（p=0.138）。是否有计划在更多 schema 上验证这一指标？

---

## Missing References

论文的相关工作覆盖已相当全面。以下为非关键性建议：

- **PARSE** (Suri et al., 2025, arXiv:2510.08623): LLM-driven schema optimization for reliable entity extraction，与 schema compilation 方面相关。
- **FormaTTax** (Zhou, 2026) 已被引用，但可考虑更详细讨论其 "structure snowballing" 发现与 IE 任务的差异性——论文目前仅在 appendix 中讨论。

---

## Overall Assessment

**Overall**: 3.5 (Borderline Conference)

**Confidence**: 4 (Quite sure — 我对 constrained decoding 和结构化 IE 领域有扎实的了解，审查了论文的技术细节和实验设计)

**一句话总结**: 一个工程执行出色、实验评估全面的 IE 类型约束解码系统，但核心算法创新有限（主要是现有技术的组合），且 CF 违规 trade-off 部分削弱了中心价值主张。

---

## Detailed Comments（逐节细评）

### Abstract
信息密度高但准确。具体数字（"≤1.4%"、"76–99%"）在未读论文时难以理解。建议提供更直觉的框架化表述（如"在 fine-tuning 下近乎消除类型违规"）。第一句话对问题的定义很好（"ontologically invalid triples"），但后续技术细节（"two-layer architecture"、"grammar-first fallback"）可能过早引入实现细节。

### §1 Introduction
Motivation 清晰，从违规率（15.4% SciERC, 18.5% DocRED）到现有方法的不足（prompting 不可靠、grammar-only 无效、post-hoc 丢弃 48%），论证链完整。Contribution list 结构合理但过长（两个条目各含 4–5 个子句），可考虑拆分为更短的要点。

### §2 Background
简洁且范围适当。Problem statement（§2.3）精确。"prefix-decidable"的引入为后续设计提供了清晰的理论基础。

### §3 Method
Proposition 1 技术上正确，但主文 proof sketch（lines 29–33）依赖对 PDA 栈的非形式化描述（"A PDA's LIFO stack cannot retrieve position k < n without destroying entries above it"）。Appendix G 的完整证明是严格的，但主文 sketch 应更清楚地标注为 informal argument，或收紧论述。

"Empirical Observation"（lines 39–40）的标签形式暗示理论结果，但内容是实验观察。建议重新措辞以区分。

Semantic layer 的设计（§3.3）解释清晰：entity registry + dynamic masking + continuation masking。Running example（Used-for 关系）有助于理解。

### §4 Constraint Composition
Grammar-first fallback 的设计决策有充分的工程动机（结构完整性是硬约束，类型违规是可检测的软错误）。但 constraint tightness κ 在 n=3 数据点上的相关性（p=0.138）不应被呈现为分析工具——这只是描述性统计，论文承认了这点（"descriptive, n=3, p=0.138"），但仍花费段落篇幅讨论。

Non-rectangularity 分析（§4 末尾）是一个有趣的细节，但在主文中的位置可能不太合适——考虑移至 appendix。

### §5 Experiments
**五路消融（Table 1）是论文最强的部分**，清晰展示了各层的独立和组合贡献。违规类别分类法（DR, RV, ET, CF）干净实用。

DocRED 结果（§5.2）不如 SciERC 令人印象深刻（45% vs. 94% DR reduction），论文将其归因于"tighter constraints trigger more fallback"。但这个解释不够深入——是否可以提供 fallback 触发率的数据来支撑这一解释？

70B 结果（§5.5）有趣（semantic-only 在 70B 下达到 84% DR reduction vs. 8B 的 24%），为 scale-dependent enabling dependency 提供了重要证据。但全部 70B 实验使用 AWQ INT4 量化，且论文无法进行直接 FP16 对比——这是可理解的硬件限制，但削弱了 70B claims 的力度。

WikiEvents 扩展（§5.4）展示了框架的泛化能力，但 n=20 的测试集规模严重限制了结论的可靠性。

### §6 Related Work
三段结构（constrained decoding → schema-aware IE → constraint enforcement in IE）清晰有效。与 GCD/BoostCD 的定位（"grammar-only achieves 3% DR reduction"）有直接实验支撑。与 GoLLIE 的对比可改进（见 W4）。

### §7 Discussion and Conclusion
简短但恰当。Future direction（global entity-level type consensus）直接针对 CF 问题，是合理的下一步。

### Limitations
极其详细和诚实，覆盖 constraint scope、evaluation coverage、engineering considerations 三个维度。建议精简至约 1 页，将具体数字分解和边缘讨论移至 appendix。

### Format Compliance
- 正文 8 页 ✓
- 匿名："Anonymous ACL submission" ✓
- `\usepackage[review]{acl}` ✓
- Limitations 在正文中（page 9）✓
- Ethics Statement 存在 ✓
- 引用格式正确（natbib）✓
- Figure 1 清晰，Tables 1–4 格式规范 ✓
- 未发现 TODO/TBD/placeholder 标记 ✓（`\TBD` 命令已定义但未使用；TODOs 仅在未编译的 outline 文件中）
- 未发现匿名违规 ✓

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 2334 · 2026-05-23T08:29:03.255060+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0: 资料检查 + Venue CFP 搜索', 'status': 'completed', 'activeForm': '检查资料完整性并搜索 EMNLP 2026 CFP'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.7: 派发视觉审查', 'status': 'completed', 'activeForm': '派发视觉审查'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'completed', 'activeForm': '收集 Reviewer 独立审稿意见'}, {'content': 'Step 2: 交叉分享 — R1→R2, R2→R1', 'status': 'in_progress', 'activeForm': '交叉分享审稿意见并收集回应'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断审稿是否收敛'}, {'content': 'Step 4: 汇总报告 & 投递', 'status': 'pending', 'activeForm': '汇总审稿报告并投递'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Step 0: 资料检查 + Venue CFP 搜索', 'status': 'completed', 'activeForm': '检查资料完整性并搜索 EMNLP 2026 CFP'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.7: 派发视觉审查', 'status': 'completed', 'activeForm': '派发视觉审查'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'completed', 'activeForm': '收集 Reviewer 独立审稿意见'}, {'content': 'Step 2: 交叉分享 — R1→R2, R2→R1', 'status': 'in_progress', 'activeForm': '交叉分享审稿意见并收集回应'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断审稿是否收敛'}, {'content': 'Step 4: 汇总报告 & 投递', 'status': 'pending', 'activeForm': '汇总审稿报告并投递'}]"
  }
}
```

</details>

---


### Tool result

_source line 2335 · 2026-05-23T08:29:03.305813+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "TodoWrite",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2336 · 2026-05-23T08:30:37.323399+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "project": "schema_semantic_constrained_ie",
  "round_number": "1",
  "text": "## 交叉分享：以下是 Reviewer 2 的完整审稿意见\n\n请逐条回应 Reviewer 2 的每个 Weakness 和 Question：\n- **[AGREE]**：同意并说明理由\n- **[REBUT]**：反驳并提供证据（cite 具体 Section/Table/Figure）\n\n特别关注你们可能存在分歧的点。\n\n---\n\n## Reviewer 2 审稿意见原文\n\n### Summary\n本文提出 OntoCoDec，一个将 IE 本体编译为可组合 token 级解码约束的框架。通过形式化分析（Proposition 1）证明 domain/range 类型约束超越上下文无关文法的表达能力，由此设计两层架构：grammar layer（基于 XGrammar 的 CFG 约束）和 semantic layer（基于动态实体注册表的运行时类型掩码）。在 SciERC、DocRED、WikiEvents 三个数据集上，跨 4 个模型（8B–70B）、2 种精度（FP16/INT4）进行了全面评估。LoRA 微调 + greedy S1 近乎消除 domain/range 违规（DR<0.1%），beam search（k=4）消除所有违规类型，延迟开销 10%–54%。\n\n### Strengths\nS1: 全面且严谨的实验评估。论文在 3 个数据集、4 个模型（3 种 tokenizer 族）、2 种精度上进行评估，包含五路消融（Table 1）、cross-model 验证（Table 3）、fine-tuning 可组合性（Table 2）、70B 验证、beam search 兼容性。统计报告包含 bootstrap CIs、p 值、Bonferroni 校正。这一评估深度在该领域内较为罕见。\n\nS2: 诚实透明的呈现方式。论文明确承认 DR enforcement 引入 CF 违规、zero-shot 质量低、WikiEvents 结果是初步的。Limitations 部分极为详细，覆盖约束范围、评估覆盖度、工程局限。这种诚实态度值得肯定。\n\nS3: 实用的系统设计。两层架构配合 grammar-first fallback 有清晰的工程动机。延迟开销适度（greedy +10%，beam 1.54×）。编译速度快（<0.5s）。可扩展性测试显示在 200 实体类型 / 1000 关系时保持恒定 2–3% 开销（Appendix M）。\n\nS4: 充分的相关工作覆盖。主文（§6）和扩展附录（Appendix B）全面覆盖 grammar-constrained decoding（XGrammar、Outlines、LMQL）、schema-aware IE（GoLLIE、KnowCoder、ADELIE）、代码领域语义约束解码（PICARD、Synchromesh、MGD）、后验验证（ODKE+、OntoLogX）、约束解码质量影响（CRANE、FormaTTax）。对 DCCD 和 Thinking Before Constraining 的定位也清晰。\n\nS5: Tokenizer 无关设计的跨模型泛化。在三种 tokenizer 族（byte-level BPE: Qwen/Llama, SentencePiece: Mistral）上验证了 continuation masking 的有效性，这是一个重要的工程贡献。\n\n### Weaknesses\nW1 [Major]: 算法创新有限，主要是系统集成贡献。论文自我定位为\"systematic engineering contribution with theoretical grounding\"（§1, line 23），这是诚实的，但也暴露了核心问题。Proposition 1（IE 类型约束超越 CFG 表达能力）在形式语言理论社区是 well-known 的结论，对任何了解 PDA 局限性的研究者来说并不意外。证明本身（Appendix G）是严格的，但结论缺乏 surprise value。核心设计决策——XGrammar 处理结构 + stateful logits processor 处理语义——是自然且直觉的组合。§4 Constraint Composition 文档化了设计决策（grammar-first fallback、constraint tightness κ），但不构成独立理论贡献。κ 与 DR reduction 的相关性在 n=3 下 p=0.138（§4），统计不显著，作为分析工具的价值有限。\n\nW2 [Major]: CF 违规 trade-off 显著削弱核心价值主张。S1 enforcement 因 per-triple 独立强制执行而创建 CF 违规：zero-shot 高达 12.02%（DocRED Llama，Table 3），fine-tuned 下 ≤1.18%（SciERC Qwen，Table 2）。这意味着系统将一类违规（DR: ontologically invalid）替换为另一类（CF: cross-triple type inconsistency）。虽然论文正确指出 CF 严重性低于 DR（CF 可通过 post-hoc TCR 缓解，Appendix O），但 \"编译本体 → 强制约束 → 获得有效输出\" 的干净叙事被打破。仅 beam search（k=4, 1.54× latency）完全解决两类违规，使延迟最优的 greedy 部署层成为不完整方案。实际部署中，用户必须在\"容忍 CF\"和\"支付 beam 延迟\"之间选择——这个 trade-off 在 abstract 和 introduction 中被低估了。\n\nW3 [Major]: Zero-shot 结果占据大量主文篇幅但缺乏实用价值。Zero-shot R-F1 在所有模型上仅 4–8%（Table 3），远低于可用质量。论文将其定位为\"diagnostic probe\"（§5 开头），但约 3/8 页篇幅用于 zero-shot 实验（§5.1 zero-shot 诊断、§5.2 DocRED、§5.3 cross-model），这些实验展示的是对功能上不可用的提取器的约束执行。相比之下，真正有实用价值的 fine-tuning composability（Table 2）仅获得约 1 页篇幅。建议重新分配：压缩 zero-shot 为 1 个总结段落+1 个表格，扩展 fine-tuning 分析。\n\nW4 [Minor]: GoLLIE 比较不公平。Appendix F（Table 8）比较 GoLLIE-7B zero-shot（R-F1=0.0, 5 predictions）vs. OntoCoDec LoRA fine-tuned（R-F1=43–45, ~1100 predictions）。GoLLIE 在未经 fine-tune 的 schema 上近乎 abstain 是预期行为。公平比较应为：(a) 两者都 zero-shot，或 (b) 两者都 fine-tuned on SciERC。当前比较在主文 §6 中被引用（\"GoLLIE-7B eliminates DR at severe coverage cost (R-F1=0.0)\"），可能误导读者认为 GoLLIE 本质上是低质量的。\n\nW5 [Minor]: WikiEvents 结果过于初步，不应作为贡献声明。n=20 测试文档，bootstrap CIs ±3–5 pp（Table 4 caption），统计效力不足以支持可靠结论。论文 power analysis（Appendix I）也承认这点。Introduction contribution list 中 \"preliminary pilot study on WikiEvents (n=20 test documents) validates event extraction applicability (§5.4)\" 过度推销了一个统计效力很弱的结果。\n\nW6 [Minor]: Limitations 部分过长。约 1.5 页的 Limitations 覆盖三个详细段落。EMNLP 2026 指南规定 Limitations \"do not count towards this page limit, provided they do not contain excessive additional content\"。当前长度接近\"excessive\"的边界。部分内容（如 residual DR 分解的具体数字、TCR 讨论、full fine-tuning 对比）可移至 appendix。\n\nW7 [Minor]: 表述重复。\"empirical enabling dependency\"（grammar-only 8B 24% DR reduction, semantic-only 24%, combined 94%）在 abstract、§1、§3 Empirical Observation、§3.4、§4、§5.1 中重复出现至少 6 次。虽然是重要观察，但如此密集的重复消耗了宝贵的主文篇幅。\n\n### Questions\nQ1: 类型约束从训练数据中提取（§5 Setup），覆盖率 99%+。剩余 ~1% 未覆盖的合法类型对会被系统性阻断。是否评估过约束引入的 false negatives 对 recall 的影响？Downstream impact（§5.1 末尾）报告 0.49% 被移除三元组匹配 gold label，但这只是被约束移除的部分。是否存在因约束而根本未被生成的合法三元组？\n\nQ2: DocRED 上 grammar-only *增加* DR（18.46%→26.17%，§5.2 \"latent violation surfacing\"）。这表明 grammar constraints 可以迫使模型进入一个类型错误更多的受限空间。这种效应在 fine-tuning 后是否持续？如果是，是否意味着 grammar layer 在某些 schema 下实际上是有害的？\n\nQ3: Beam search (k=4) 消除所有违规。是否探索过 k=2 作为折中？论文仅展示 k=4；理解 k 与违规消除的关系对实际部署指导很重要。\n\nQ4: Entity registry 在生成过程中增量构建（§3.3）。当模型对同一实体名生成不同类型时，first-seen type 是否始终被采用？这似乎是 CF 违规的主要来源，但机制在主文中解释不够清晰。§4 \"greedy limitation\" 段提及但未详细展开。\n\nQ5: Constraint tightness κ 的定义（§4）中，SciERC κ̄=0.333, DocRED κ̄=0.842, WikiEvents κ̄=0.029。在 n=3 下无法建立有意义的统计关系（p=0.138）。是否有计划在更多 schema 上验证这一指标？\n\n### Missing References\nPARSE (Suri et al., 2025, arXiv:2510.08623), FormaTTax (Zhou, 2026) 已引用但可更详细讨论。\n\n### Overall Assessment\nOverall: 3.5 (Borderline Conference)\nConfidence: 4\n一句话总结: 一个工程执行出色、实验评估全面的 IE 类型约束解码系统，但核心算法创新有限（主要是现有技术的组合），且 CF 违规 trade-off 部分削弱了中心价值主张。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "project": "schema_semantic_constrained_ie",
    "round_number": "1",
    "text": "## 交叉分享：以下是 Reviewer 2 的完整审稿意见\n\n请逐条回应 Reviewer 2 的每个 Weakness 和 Question：\n- **[AGREE]**：同意并说明理由\n- **[REBUT]**：反驳并提供证据（cite 具体 Section/Table/Figure）\n\n特别关注你们可能存在分歧的点。\n\n---\n\n## Reviewer 2 审稿意见原文\n\n### Summary\n本文提出 OntoCoDec，一个将 IE 本体编译为可组合 token 级解码约束的框架。通过形式化分析（Proposition 1）证明 domain/range 类型约束超越上下文无关文法的表达能力，由此设计两层架构：grammar layer（基于 XGrammar 的 CFG 约束）和 semantic layer（基于动态实体注册表的运行时类型掩码）。在 SciERC、DocRED、WikiEvents 三个数据集上，跨 4 个模型（8B–70B）、2 种精度（FP16/INT4）进行了全面评估。LoRA 微调 + greedy S1 近乎消除 domain/range 违规（DR<0.1%），beam search（k=4）消除所有违规类型，延迟开销 10%–54%。\n\n### Strengths\nS1: 全面且严谨的实验评估。论文在 3 个数据集、4 个模型（3 种 tokenizer 族）、2 种精度上进行评估，包含五路消融（Table 1）、cross-model 验证（Table 3）、fine-tuning 可组合性（Table 2）、70B 验证、beam search 兼容性。统计报告包含 bootstrap CIs、p 值、Bonferroni 校正。这一评估深度在该领域内较为罕见。\n\nS2: 诚实透明的呈现方式。论文明确承认 DR enforcement 引入 CF 违规、zero-shot 质量低、WikiEvents 结果是初步的。Limitations 部分极为详细，覆盖约束范围、评估覆盖度、工程局限。这种诚实态度值得肯定。\n\nS3: 实用的系统设计。两层架构配合 grammar-first fallback 有清晰的工程动机。延迟开销适度（greedy +10%，beam 1.54×）。编译速度快（<0.5s）。可扩展性测试显示在 200 实体类型 / 1000 关系时保持恒定 2–3% 开销（Appendix M）。\n\nS4: 充分的相关工作覆盖。主文（§6）和扩展附录（Appendix B）全面覆盖 grammar-constrained decoding（XGrammar、Outlines、LMQL）、schema-aware IE（GoLLIE、KnowCoder、ADELIE）、代码领域语义约束解码（PICARD、Synchromesh、MGD）、后验验证（ODKE+、OntoLogX）、约束解码质量影响（CRANE、FormaTTax）。对 DCCD 和 Thinking Before Constraining 的定位也清晰。\n\nS5: Tokenizer 无关设计的跨模型泛化。在三种 tokenizer 族（byte-level BPE: Qwen/Llama, SentencePiece: Mistral）上验证了 continuation masking 的有效性，这是一个重要的工程贡献。\n\n### Weaknesses\nW1 [Major]: 算法创新有限，主要是系统集成贡献。论文自我定位为\"systematic engineering contribution with theoretical grounding\"（§1, line 23），这是诚实的，但也暴露了核心问题。Proposition 1（IE 类型约束超越 CFG 表达能力）在形式语言理论社区是 well-known 的结论，对任何了解 PDA 局限性的研究者来说并不意外。证明本身（Appendix G）是严格的，但结论缺乏 surprise value。核心设计决策——XGrammar 处理结构 + stateful logits processor 处理语义——是自然且直觉的组合。§4 Constraint Composition 文档化了设计决策（grammar-first fallback、constraint tightness κ），但不构成独立理论贡献。κ 与 DR reduction 的相关性在 n=3 下 p=0.138（§4），统计不显著，作为分析工具的价值有限。\n\nW2 [Major]: CF 违规 trade-off 显著削弱核心价值主张。S1 enforcement 因 per-triple 独立强制执行而创建 CF 违规：zero-shot 高达 12.02%（DocRED Llama，Table 3），fine-tuned 下 ≤1.18%（SciERC Qwen，Table 2）。这意味着系统将一类违规（DR: ontologically invalid）替换为另一类（CF: cross-triple type inconsistency）。虽然论文正确指出 CF 严重性低于 DR（CF 可通过 post-hoc TCR 缓解，Appendix O），但 \"编译本体 → 强制约束 → 获得有效输出\" 的干净叙事被打破。仅 beam search（k=4, 1.54× latency）完全解决两类违规，使延迟最优的 greedy 部署层成为不完整方案。实际部署中，用户必须在\"容忍 CF\"和\"支付 beam 延迟\"之间选择——这个 trade-off 在 abstract 和 introduction 中被低估了。\n\nW3 [Major]: Zero-shot 结果占据大量主文篇幅但缺乏实用价值。Zero-shot R-F1 在所有模型上仅 4–8%（Table 3），远低于可用质量。论文将其定位为\"diagnostic probe\"（§5 开头），但约 3/8 页篇幅用于 zero-shot 实验（§5.1 zero-shot 诊断、§5.2 DocRED、§5.3 cross-model），这些实验展示的是对功能上不可用的提取器的约束执行。相比之下，真正有实用价值的 fine-tuning composability（Table 2）仅获得约 1 页篇幅。建议重新分配：压缩 zero-shot 为 1 个总结段落+1 个表格，扩展 fine-tuning 分析。\n\nW4 [Minor]: GoLLIE 比较不公平。Appendix F（Table 8）比较 GoLLIE-7B zero-shot（R-F1=0.0, 5 predictions）vs. OntoCoDec LoRA fine-tuned（R-F1=43–45, ~1100 predictions）。GoLLIE 在未经 fine-tune 的 schema 上近乎 abstain 是预期行为。公平比较应为：(a) 两者都 zero-shot，或 (b) 两者都 fine-tuned on SciERC。当前比较在主文 §6 中被引用（\"GoLLIE-7B eliminates DR at severe coverage cost (R-F1=0.0)\"），可能误导读者认为 GoLLIE 本质上是低质量的。\n\nW5 [Minor]: WikiEvents 结果过于初步，不应作为贡献声明。n=20 测试文档，bootstrap CIs ±3–5 pp（Table 4 caption），统计效力不足以支持可靠结论。论文 power analysis（Appendix I）也承认这点。Introduction contribution list 中 \"preliminary pilot study on WikiEvents (n=20 test documents) validates event extraction applicability (§5.4)\" 过度推销了一个统计效力很弱的结果。\n\nW6 [Minor]: Limitations 部分过长。约 1.5 页的 Limitations 覆盖三个详细段落。EMNLP 2026 指南规定 Limitations \"do not count towards this page limit, provided they do not contain excessive additional content\"。当前长度接近\"excessive\"的边界。部分内容（如 residual DR 分解的具体数字、TCR 讨论、full fine-tuning 对比）可移至 appendix。\n\nW7 [Minor]: 表述重复。\"empirical enabling dependency\"（grammar-only 8B 24% DR reduction, semantic-only 24%, combined 94%）在 abstract、§1、§3 Empirical Observation、§3.4、§4、§5.1 中重复出现至少 6 次。虽然是重要观察，但如此密集的重复消耗了宝贵的主文篇幅。\n\n### Questions\nQ1: 类型约束从训练数据中提取（§5 Setup），覆盖率 99%+。剩余 ~1% 未覆盖的合法类型对会被系统性阻断。是否评估过约束引入的 false negatives 对 recall 的影响？Downstream impact（§5.1 末尾）报告 0.49% 被移除三元组匹配 gold label，但这只是被约束移除的部分。是否存在因约束而根本未被生成的合法三元组？\n\nQ2: DocRED 上 grammar-only *增加* DR（18.46%→26.17%，§5.2 \"latent violation surfacing\"）。这表明 grammar constraints 可以迫使模型进入一个类型错误更多的受限空间。这种效应在 fine-tuning 后是否持续？如果是，是否意味着 grammar layer 在某些 schema 下实际上是有害的？\n\nQ3: Beam search (k=4) 消除所有违规。是否探索过 k=2 作为折中？论文仅展示 k=4；理解 k 与违规消除的关系对实际部署指导很重要。\n\nQ4: Entity registry 在生成过程中增量构建（§3.3）。当模型对同一实体名生成不同类型时，first-seen type 是否始终被采用？这似乎是 CF 违规的主要来源，但机制在主文中解释不够清晰。§4 \"greedy limitation\" 段提及但未详细展开。\n\nQ5: Constraint tightness κ 的定义（§4）中，SciERC κ̄=0.333, DocRED κ̄=0.842, WikiEvents κ̄=0.029。在 n=3 下无法建立有意义的统计关系（p=0.138）。是否有计划在更多 schema 上验证这一指标？\n\n### Missing References\nPARSE (Suri et al., 2025, arXiv:2510.08623), FormaTTax (Zhou, 2026) 已引用但可更详细讨论。\n\n### Overall Assessment\nOverall: 3.5 (Borderline Conference)\nConfidence: 4\n一句话总结: 一个工程执行出色、实验评估全面的 IE 类型约束解码系统，但核心算法创新有限（主要是现有技术的组合），且 CF 违规 trade-off 部分削弱了中心价值主张。"
  }
}
```

</details>

---


### Tool result

_source line 2337 · 2026-05-23T08:31:52.194242+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 74870
}
```

</details>

---


### Tool call

_source line 2338 · 2026-05-23T08:31:52.495843+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "project": "schema_semantic_constrained_ie",
  "round_number": "1",
  "text": "## 交叉分享：以下是 Reviewer 1 的完整审稿意见\n\n请逐条回应 Reviewer 1 的每个 Weakness 和 Question：\n- **[AGREE]**：同意并说明理由\n- **[REBUT]**：反驳并提供证据（cite 具体 Section/Table/Figure）\n  \n特别关注你们可能存在分歧的点。\n\n---\n\n## Reviewer 1 审稿意见原文\n\n### Summary\n本文提出OntoCoDec，将IE本体编译为两层可组合的token级解码约束：grammar layer（基于XGrammar的CFG，强制JSON结构和词汇成员关系）和semantic layer（有状态logits处理器，通过动态entity registry强制domain/range类型约束）。论文在SciERC、DocRED、WikiEvents上评估了Qwen3-8B、Llama-3.1-8B、Mistral-7B（含70B AWQ INT4），提供了五路消融、bootstrap统计检验、beam search兼容性验证等极其详尽的实验分析。核心贡献是约束可判定性分类（三级）和两层间的经验性enabling dependency发现。\n\n### Strengths\nS1 [方法设计] 约束可判定性分类（Level 1: context-free → Level 2: prefix-decidable with state → Level 3: non-local）概念清晰，精准界定了CFG能做和不能做的边界（§3, p.3）。grammar-first fallback机制（§4, p.5, eq.2）在soundness和availability之间取得了合理平衡。\n\nS2 [形式化] Proposition 1（p.3, 完整证明Appendix O, p.37-38）的pumping lemma论证结构正确：对于无界entity集合，独立选择的类型对产生cross-serial依赖，PDA无法处理。Remark（p.3）中关于有限集合DFA指数爆炸的补充说明区分了理论不可能性和工程不可行性。\n\nS3 [评估深度] 实验分析的彻底程度在NLP论文中极为罕见：五路消融（Table 1）、bootstrap CI + Cohen's d（Table 8, Appendix C）、fallback因果追踪（Table 6-7, Appendix C）、cross-field违规分解（Table 9）、document长度分箱分析（Tables 32-34, Appendix H）、prompt敏感性（Table 35, Appendix I）、TCR post-hoc resolution（Tables 43-44, Appendix M）、beam search兼容性（Tables 24-29, Appendix F）。39页附录覆盖了我能想到的几乎所有消融维度。\n\nS4 [统计规范] Bootstrap CI采用document-level resampling（10,000 iterations, seed=42），报告了MDE（Table 31, Appendix C：SciERC ±1.8pp, DocRED ±0.8pp, WikiEvents ±5.0pp），并诚实承认\"n=6 is insufficient for statistical inference on this correlation\"（p.20）。这种统计纪律在IE领域论文中少见。\n\nS5 [Enabling dependency] 两层间的scale-dependent enabling dependency（grammar alone 84% DR at 8B vs. 24% semantic-only, Table 1; 70B时grammar alone达到semantic layer的水平, Table 3/§5.3）是有意义的经验发现，对约束解码系统设计有指导价值。\n\nS6 [工程贡献] Tokenizer-agnostic continuation masking（§3.3, p.4）通过byte-level BPE分解处理多token类型名，适配Qwen/Llama/SentencePiece三种分词器，实际工程价值高。ontology scalability分析（Appendix K, Table 41）展示了编译时间sub-linearly scaling至XLarge (1000 entity types)。\n\n### Weaknesses\nW1 [Critical]: Cross-field (CF) 类型一致性占残余违规的64%，但正文讨论不足。Table 9显示，在S1配置下SciERC的245个残余违规中，GENERIC↔OtherScientificTerm占34.7%，GENERIC↔Material占12.3%，总计CF违规占63.9%（155/245）。这是方法论的根本缺口——论文标题声称\"Type-Constrained IE\"，但最主要的类型约束违规（跨triple的实体类型一致性）未被处理。正文§4仅用一句\"Level 3 is addressed by beam search or post-hoc resolution\"（p.3）带过，但Appendix M的TCR（Tables 43-44）在zero-shot下仅处理0-2%的CF冲突，效果有限。Limitations（p.9）提到CF但未量化其严重程度（64%这个数字只出现在附录）。建议：(1) 在正文§5.1或§4中明确量化CF占残余违规的比例；(2) 讨论CF问题为何从架构上难以在单pass解码中解决；(3) 考虑将标题修改为更精确的表述，如\"Domain/Range-Constrained\"。\n\nW2 [Major]: Proposition 1的实际意义论证存在gap。Proposition 1证明的是*无界entity集合*下domain/range约束不是context-free——但所有实际IE场景中entity集合都有界（受文档长度限制）。论文在Remark中提到有限集合的DFA需要O(|T^{|entity|}|)个状态\"exceeding 10^10 for DocRED\"，但这是一个工程可行性论证（编译DFA不现实），而非形式上不可能。这两个论点——理论上超越CFG vs. 工程上DFA不可行——之间的逻辑跳跃需要更清晰地阐明。建议：在正文中明确区分\"formal impossibility for unbounded sets\"和\"engineering intractability for bounded sets\"。\n\nW3 [Major]: WikiEvents (n=20) 的结论统计效力不足，但在正文中占据整个§5.4。WikiEvents评估仅20个文档，MDE为±5.0pp（Table 31），这意味着只有大于5个百分点的F1差异才能被检测到。建议：(1) 将§5.4的篇幅大幅缩减，标题改为\"Preliminary Event Extraction Pilot\"；(2) 在Table 4的caption中注明\"n=20, MDE=5.0pp, results are directional only\"；(3) 不要在n=20上报告fine-tuning composability结论。\n\nW4 [Major]: 70B实验的INT4量化限制未充分披露。Abstract声称\"with 70B-class validation (§5.3)\"，但70B实验全部在AWQ INT4上运行。Table 48显示INT4 vs FP16在SciERC上R-F1差异为-0.09，但DocRED的E-F1 drop为-7.07（INT4: 84.87 vs FP16: 91.94）。论文解释这是\"parse failure\"导致而非约束干扰，但这意味着INT4下的constraint enforcement结果可能被量化噪声污染。建议：(1) Abstract中明确标注\"70B (AWQ INT4)\"；(2) 在§5.3开头而非结尾说明量化限制。\n\nW5 [Major]: 缺少与训练基方法的系统性对比。论文声称OntoCoDec\"is composable with fine-tuning\"（§5.1），但缺少与专门训练来满足schema约束的方法（如ADELIE, CodeIE, UIE）在相同benchmark上的直接对比。Appendix Q与GoLLIE的对比仅在SciERC 100 docs上进行，且GoLLIE在其中产生了54%空输出（仅5个有效预测），信息量有限。建议：(1) 在主要benchmark上与至少一个schema-aware训练方法进行完整对比；(2) 如果直接对比不可行，明确说明原因。\n\nW6 [Minor]: Grammar-first fallback频率的模型依赖性未在正文讨论。Qwen3-8B在SciERC上0次fallback，但Llama-3.1-8B触发5,882次fallback（10.7 per document）。\n\nW7 [Minor]: Continuation masking的\"distinguishable token-prefix\"假设。论文未展示实际prefix collision的frequency或其对masking correctness的影响。\n\n### Questions\nQ1: Grammar-first fallback在semantic mask与grammar mask不相交时触发。但fallback本质上放弃了类型约束。是否考虑过替代策略，如backtracking到最近的type-bearing position重新生成？\n\nQ2: Table 10显示Per-Relation DR elimination中，head entity的registered type falls outside relation's domain——这是否暗示fine-tuning和constraint enforcement在某些relation上学到了不同的type preference？\n\nQ3: Appendix K的ontology scalability测试最大到XLarge（1000 entity types, 1000 relations）。Real-world知识图谱（如Wikidata有约10,000+ property types）远超此规模。是否测试或估计过更大规模ontology下的表现？\n\nQ4: Entity registry假设entity在relation之前生成。OntoCoDec是否fundamentally限于entity-first的生成顺序？\n\nQ5: Cohen's d是从pooled bootstrap SD计算的。请clarify这个选择的理由。\n\n### Missing References\n建议补充 Josifoski et al., 2022 (GenIE) 在 Related Work 中的 constraint enforcement 讨论，以及 Paolini et al., 2021 (TANL)。\n\n### Overall Assessment\n评分: 3.5 (Borderline Conference)\n置信度: 4/5\n本文的核心贡献思路清晰，工程实现扎实，评估在统计规范性上显著优于同领域平均水平。三个问题阻碍Conference评分：(1) CF类型一致性占残余违规64%且未被解决，与标题形成gap；(2) WikiEvents和70B的评估统计效力不足但呈现方式可能误导；(3) 缺少与训练基方法的fair comparison。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "project": "schema_semantic_constrained_ie",
    "round_number": "1",
    "text": "## 交叉分享：以下是 Reviewer 1 的完整审稿意见\n\n请逐条回应 Reviewer 1 的每个 Weakness 和 Question：\n- **[AGREE]**：同意并说明理由\n- **[REBUT]**：反驳并提供证据（cite 具体 Section/Table/Figure）\n  \n特别关注你们可能存在分歧的点。\n\n---\n\n## Reviewer 1 审稿意见原文\n\n### Summary\n本文提出OntoCoDec，将IE本体编译为两层可组合的token级解码约束：grammar layer（基于XGrammar的CFG，强制JSON结构和词汇成员关系）和semantic layer（有状态logits处理器，通过动态entity registry强制domain/range类型约束）。论文在SciERC、DocRED、WikiEvents上评估了Qwen3-8B、Llama-3.1-8B、Mistral-7B（含70B AWQ INT4），提供了五路消融、bootstrap统计检验、beam search兼容性验证等极其详尽的实验分析。核心贡献是约束可判定性分类（三级）和两层间的经验性enabling dependency发现。\n\n### Strengths\nS1 [方法设计] 约束可判定性分类（Level 1: context-free → Level 2: prefix-decidable with state → Level 3: non-local）概念清晰，精准界定了CFG能做和不能做的边界（§3, p.3）。grammar-first fallback机制（§4, p.5, eq.2）在soundness和availability之间取得了合理平衡。\n\nS2 [形式化] Proposition 1（p.3, 完整证明Appendix O, p.37-38）的pumping lemma论证结构正确：对于无界entity集合，独立选择的类型对产生cross-serial依赖，PDA无法处理。Remark（p.3）中关于有限集合DFA指数爆炸的补充说明区分了理论不可能性和工程不可行性。\n\nS3 [评估深度] 实验分析的彻底程度在NLP论文中极为罕见：五路消融（Table 1）、bootstrap CI + Cohen's d（Table 8, Appendix C）、fallback因果追踪（Table 6-7, Appendix C）、cross-field违规分解（Table 9）、document长度分箱分析（Tables 32-34, Appendix H）、prompt敏感性（Table 35, Appendix I）、TCR post-hoc resolution（Tables 43-44, Appendix M）、beam search兼容性（Tables 24-29, Appendix F）。39页附录覆盖了我能想到的几乎所有消融维度。\n\nS4 [统计规范] Bootstrap CI采用document-level resampling（10,000 iterations, seed=42），报告了MDE（Table 31, Appendix C：SciERC ±1.8pp, DocRED ±0.8pp, WikiEvents ±5.0pp），并诚实承认\"n=6 is insufficient for statistical inference on this correlation\"（p.20）。这种统计纪律在IE领域论文中少见。\n\nS5 [Enabling dependency] 两层间的scale-dependent enabling dependency（grammar alone 84% DR at 8B vs. 24% semantic-only, Table 1; 70B时grammar alone达到semantic layer的水平, Table 3/§5.3）是有意义的经验发现，对约束解码系统设计有指导价值。\n\nS6 [工程贡献] Tokenizer-agnostic continuation masking（§3.3, p.4）通过byte-level BPE分解处理多token类型名，适配Qwen/Llama/SentencePiece三种分词器，实际工程价值高。ontology scalability分析（Appendix K, Table 41）展示了编译时间sub-linearly scaling至XLarge (1000 entity types)。\n\n### Weaknesses\nW1 [Critical]: Cross-field (CF) 类型一致性占残余违规的64%，但正文讨论不足。Table 9显示，在S1配置下SciERC的245个残余违规中，GENERIC↔OtherScientificTerm占34.7%，GENERIC↔Material占12.3%，总计CF违规占63.9%（155/245）。这是方法论的根本缺口——论文标题声称\"Type-Constrained IE\"，但最主要的类型约束违规（跨triple的实体类型一致性）未被处理。正文§4仅用一句\"Level 3 is addressed by beam search or post-hoc resolution\"（p.3）带过，但Appendix M的TCR（Tables 43-44）在zero-shot下仅处理0-2%的CF冲突，效果有限。Limitations（p.9）提到CF但未量化其严重程度（64%这个数字只出现在附录）。建议：(1) 在正文§5.1或§4中明确量化CF占残余违规的比例；(2) 讨论CF问题为何从架构上难以在单pass解码中解决；(3) 考虑将标题修改为更精确的表述，如\"Domain/Range-Constrained\"。\n\nW2 [Major]: Proposition 1的实际意义论证存在gap。Proposition 1证明的是*无界entity集合*下domain/range约束不是context-free——但所有实际IE场景中entity集合都有界（受文档长度限制）。论文在Remark中提到有限集合的DFA需要O(|T^{|entity|}|)个状态\"exceeding 10^10 for DocRED\"，但这是一个工程可行性论证（编译DFA不现实），而非形式上不可能。这两个论点——理论上超越CFG vs. 工程上DFA不可行——之间的逻辑跳跃需要更清晰地阐明。建议：在正文中明确区分\"formal impossibility for unbounded sets\"和\"engineering intractability for bounded sets\"。\n\nW3 [Major]: WikiEvents (n=20) 的结论统计效力不足，但在正文中占据整个§5.4。WikiEvents评估仅20个文档，MDE为±5.0pp（Table 31），这意味着只有大于5个百分点的F1差异才能被检测到。建议：(1) 将§5.4的篇幅大幅缩减，标题改为\"Preliminary Event Extraction Pilot\"；(2) 在Table 4的caption中注明\"n=20, MDE=5.0pp, results are directional only\"；(3) 不要在n=20上报告fine-tuning composability结论。\n\nW4 [Major]: 70B实验的INT4量化限制未充分披露。Abstract声称\"with 70B-class validation (§5.3)\"，但70B实验全部在AWQ INT4上运行。Table 48显示INT4 vs FP16在SciERC上R-F1差异为-0.09，但DocRED的E-F1 drop为-7.07（INT4: 84.87 vs FP16: 91.94）。论文解释这是\"parse failure\"导致而非约束干扰，但这意味着INT4下的constraint enforcement结果可能被量化噪声污染。建议：(1) Abstract中明确标注\"70B (AWQ INT4)\"；(2) 在§5.3开头而非结尾说明量化限制。\n\nW5 [Major]: 缺少与训练基方法的系统性对比。论文声称OntoCoDec\"is composable with fine-tuning\"（§5.1），但缺少与专门训练来满足schema约束的方法（如ADELIE, CodeIE, UIE）在相同benchmark上的直接对比。Appendix Q与GoLLIE的对比仅在SciERC 100 docs上进行，且GoLLIE在其中产生了54%空输出（仅5个有效预测），信息量有限。建议：(1) 在主要benchmark上与至少一个schema-aware训练方法进行完整对比；(2) 如果直接对比不可行，明确说明原因。\n\nW6 [Minor]: Grammar-first fallback频率的模型依赖性未在正文讨论。Qwen3-8B在SciERC上0次fallback，但Llama-3.1-8B触发5,882次fallback（10.7 per document）。\n\nW7 [Minor]: Continuation masking的\"distinguishable token-prefix\"假设。论文未展示实际prefix collision的frequency或其对masking correctness的影响。\n\n### Questions\nQ1: Grammar-first fallback在semantic mask与grammar mask不相交时触发。但fallback本质上放弃了类型约束。是否考虑过替代策略，如backtracking到最近的type-bearing position重新生成？\n\nQ2: Table 10显示Per-Relation DR elimination中，head entity的registered type falls outside relation's domain——这是否暗示fine-tuning和constraint enforcement在某些relation上学到了不同的type preference？\n\nQ3: Appendix K的ontology scalability测试最大到XLarge（1000 entity types, 1000 relations）。Real-world知识图谱（如Wikidata有约10,000+ property types）远超此规模。是否测试或估计过更大规模ontology下的表现？\n\nQ4: Entity registry假设entity在relation之前生成。OntoCoDec是否fundamentally限于entity-first的生成顺序？\n\nQ5: Cohen's d是从pooled bootstrap SD计算的。请clarify这个选择的理由。\n\n### Missing References\n建议补充 Josifoski et al., 2022 (GenIE) 在 Related Work 中的 constraint enforcement 讨论，以及 Paolini et al., 2021 (TANL)。\n\n### Overall Assessment\n评分: 3.5 (Borderline Conference)\n置信度: 4/5\n本文的核心贡献思路清晰，工程实现扎实，评估在统计规范性上显著优于同领域平均水平。三个问题阻碍Conference评分：(1) CF类型一致性占残余违规64%且未被解决，与标题形成gap；(2) WikiEvents和70B的评估统计效力不足但呈现方式可能误导；(3) 缺少与训练基方法的fair comparison。"
  }
}
```

</details>

---


### Tool result

_source line 2339 · 2026-05-23T08:31:53.904894+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1409
}
```

</details>

---


### Assistant

_source line 2340 · 2026-05-23T08:31:57.443237+00:00_

交叉分享已发送给两位 Reviewer。等待 [AGREE]/[REBUT] 回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director"
}
```

</details>

---


## Round 169

## Round 169

2 recorded events


### User

_source line 2341 · 2026-05-23T08:32:00.053115+00:00_

[Reviewer 2 审稿结果]:
审稿完成，已通过 `review_reviewer_post_to_director` 提交给 Review Director。

**核心判断**: Overall 3.5 (Borderline Conference)，置信度 4/5。

**主要发现**:
- **优势**: 实验评估极为全面（3 数据集 × 4 模型 × 2 精度 × 多策略），统计报告严谨（bootstrap CIs + Bonferroni），相关工作覆盖充分，系统设计实用（+10% 延迟）
- **核心问题**: (1) 算法创新有限，主要是 XGrammar + stateful logits processor 的系统集成；(2) CF 违规 trade-off 削弱价值主张（greedy 部署层不完整，beam 才能完全解决）；(3) zero-shot R-F1 仅 4–8%，占主文 ~3 页但缺乏实用价值
- **格式合规**: 全部通过（8 页正文、双盲匿名、Limitations 在正文、无 TODO 残留）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 2342 · 2026-05-23T08:32:05.460114+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director"
}
```

</details>

---


## Round 170

## Round 170

18 recorded events


### User

_source line 2343 · 2026-05-23T08:34:10.381479+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 交叉回应 Reviewer 1

### Weaknesses 逐条回应

**[AGREE] R1-W1: CF 违规占残余违规 64% 但正文讨论不足。**
同意这是核心弱点，我的 W2 也指出了同一问题。R1 提供了更精确的量化（Table 9: 155/245 = 63.9%）。支持建议 (1) 在 §5.1 量化 CF 比例和 (2) 讨论架构限制。**但对建议 (3) 改标题有保留**："Type-Constrained" 并非虚假——grammar layer 执行了 vocabulary membership（Level 1），semantic layer 执行了 domain/range（Level 2），只是 Level 3 (non-local CF) 未被完全解决。更好的方案是在 abstract/introduction 中明确界定 "type-constrained" 的范围，而非改标题。

**[REBUT] R1-W2: Proposition 1 实际意义论证 gap。**
部分反驳。论文 Remark（§3, p.3）已明确区分 "theoretical impossibility (unbounded) and engineering intractability (finite but exponential); OntoCoDec's registry-based approach avoids both"。R1 要求的区分实际上已经做了，只是作为 Remark 不够 prominent。建议提升为正式段落，但不构成 Major weakness。

**[AGREE] R1-W3: WikiEvents n=20 统计效力不足。**
完全同意，与我的 W5 一致。R1 的三条具体建议（缩减篇幅、改标题、Table 4 加注 MDE）都合理。

**[AGREE] R1-W4: 70B INT4 量化限制披露不足。**
同意 presentation issue，但严重程度略低于 R1 评判。关键是 8B 消融已确认 INT4 不影响 constraint enforcement（DR remains 0%; Appendix P）。R1 引用的 DocRED E-F1 drop（-7.07）源于 parse failure 而非量化噪声影响约束。同意 abstract 应标注 "70B (AWQ INT4)"，§5.5 开头应说明量化限制。

**[REBUT] R1-W5: 缺少与训练基方法的系统性对比。**
部分反驳。论文在 Appendix B 明确定位 training-based 和 decoding-time 方法为 "complementary rather than competing"。OntoCoDec 的核心 use case 是与 fine-tuning 组合（Table 2 已展示），而非替代 GoLLIE/ADELIE。要求 OntoCoDec vs. ADELIE 的直接对比面临方法论困难：公平对比应为 "ADELIE alone vs. ADELIE + OntoCoDec"，而非 OntoCoDec vs. ADELIE。不过同意论文应更明确说明为何直接对比不可行。

**[AGREE] R1-W6: Fallback 频率模型依赖性。** 同意，Qwen 0次 vs. Llama 5,882次差异显著，值得正文提及。

**[AGREE] R1-W7: Continuation masking prefix collision 频率。** 同意未提供量化验证。

### Questions 回应

**[AGREE] R1-Q1 (Backtracking):** 好问题，论文应讨论 backtracking 被排除的理由，特别是 IterGen 已探索此方向。
**[AGREE] R1-Q2 (Type preference 冲突):** 有价值的观察，可能是 CF 的另一来源。
**[AGREE] R1-Q3 (大规模 ontology):** 实际部署关键问题，prefix collision 在更大 ontology 下风险增加。
**[AGREE] R1-Q4 (Entity-first 限制):** Entity-before-relation 是根本架构约束，应在 Limitations 中明确说明（当前未提及）。
**[AGREE] R1-Q5 (Cohen's d):** 论文应 clarify。

### Missing References

**[REBUT] R1-Missing References:** GenIE 和 TANL 均已在 §6 被引用（"GenIE (Josifoski et al., 2022), TANL (Paolini et al., 2021)" 在 Schema-aware IE 段落），Appendix B 也详细讨论了 GenIE。这是 R1 的疏忽。

### 与 R1 的核心分歧

| Issue | R1 | R2 | 分歧点 |
|-------|----|----|--------|
| CF severity | Critical (改标题) | Major (界定范围即可) | 标题是否需要修改 |
| Prop. 1 gap | Major | Minor (Remark 已区分) | 论证是否已充分 |
| W5 训练基对比 | Major | Minor (互补定位) | 对比是否 methodologically necessary |
| Missing refs | GenIE/TANL 需补充 | 已被引用 | 事实性分歧（R1 疏忽） |

### 核心共识

CF trade-off（R1-W1/我的 W2）、WikiEvents 统计效力（R1-W3/我的 W5）、70B INT4 披露（R1-W4）是两位 reviewer 一致认为最需要作者 address 的问题。Overall 评分两位均为 3.5 (Borderline Conference)，confidence 均为 4/5。

---

[Reviewer 1 审稿意见]:

## Reviewer 1 对 Reviewer 2 审稿意见的逐条交叉回应

---

### Weaknesses 回应

**[AGREE] R2-W1: 算法创新有限，主要是系统集成贡献**

同意R2的核心判断，但认为需要nuance。R2正确指出Proposition 1（IE类型约束超越CFG）对了解PDA局限性的研究者来说"不意外"——pumping lemma论证是标准的。XGrammar + stateful logits processor的组合确实是自然的设计选择。κ在n=3下p=0.138统计不显著，作为分析工具价值确实有限。

但我认为R2低估了两点贡献：(1) **enabling dependency的经验发现**（grammar alone 84% DR at 8B, semantic alone仅24%, Table 1）——这个定量关系是非显然的，尤其是scale-dependent特性（70B时grammar alone接近semantic layer的水平, §5.3）；(2) **约束可判定性三级分类**（§3, p.3: context-free → prefix-decidable with state → non-local）虽然不是形式理论突破，但为IE约束解码系统设计提供了有用的conceptual framework，比"grammar vs. semantic"的二分法更精确。

总体而言，本文更接近"strong engineering contribution with useful empirical insights"而非"theoretical novelty"——在EMNLP（重视应用和实证的venue）这是可接受的定位，但作者应降低理论贡献的措辞强度。

---

**[AGREE] R2-W2: CF违规trade-off显著削弱核心价值主张**

强烈同意。这与我的W1（Critical）完全一致。补充R2的论点：

我在审查中发现Table 9（p.21-22）的具体数据更能说明问题的严重性——S1配置下SciERC的245个残余违规中，CF违规占**63.9%**（155/245），且主要集中在GENERIC↔OtherScientificTerm（34.7%）和GENERIC↔Material（12.3%）这两个模式。这意味着系统消除了DR violations，但引入的CF violations在数量上构成了新的dominant问题。

R2指出"用户必须在'容忍CF'和'支付beam延迟'之间选择"——我进一步注意到即使beam search（k=4）消除了所有violation类型，这也改变了系统的latency profile（1.54×, Appendix F），对于高吞吐量部署场景是一个real trade-off。论文应在Abstract/Introduction中更诚实地呈现这个tension，而非让读者到§5.1才发现。

---

**[REBUT] R2-W3: Zero-shot结果占据大量主文篇幅但缺乏实用价值**

部分不同意R2的判断。

R2的论点是zero-shot R-F1仅4-8%，"远低于可用质量"，因此这些实验缺乏实用价值。但zero-shot设置的价值不在于提取质量本身，而在于**作为controlled diagnostic isolating约束机制的效果**。Fine-tuning同时改变模型的类型分布和生成质量，无法cleanly isolate约束层的独立贡献。Zero-shot保持模型不变，使得violation rate changes可以直接归因于约束enforcement。

具体证据：
- Table 1的五路消融（zero-shot, p.5）是论文最informative的实验之一，cleanly展示了grammar vs. semantic vs. combined的边际贡献
- §5.2中DocRED的"latent violation surfacing"（grammar-only使DR从18.46%增至26.17%）是一个重要发现，只在zero-shot下可观察到——fine-tuning后效果消失（Table 2, S1配置DR<0.1%）
- Enabling dependency的scale-dependent特性（grammar alone 84% DR at 8B → 接近semantic at 70B）也依赖zero-shot实验

但我**部分同意**R2关于**篇幅分配**的建议。当前fine-tuning composability（Table 2, §5.1后半段）确实deserves more main text空间，尤其是per-relation DR elimination patterns（当前在Appendix C Table 10, p.22，但这是核心insight）。建议将§5.1 zero-shot diagnostic压缩为1段+Table 1保留，将per-relation fine-tuning分析从附录提升到正文。

---

**[AGREE] R2-W4: GoLLIE比较不公平**

完全同意。Table 49（p.39, Appendix Q）明确标注"zero-shot for GoLLIE, LoRA + S1 for OntoCoDec"——这不是fair comparison。GoLLIE是一个schema-conditioned模型，设计上需要与其annotation guidelines格式匹配才能发挥效果。在SciERC上zero-shot且不使用GoLLIE的原始schema format，几乎必然产生低coverage（54%空输出、仅5个有效预测）。

更严重的是，§6（p.8）主文引用了这个结果："GoLLIE-7B eliminates DR at severe coverage cost (R-F1=0.5...46% empty output)"——这给读者留下GoLLIE"本质低质量"的印象，但实际上是evaluation setup不匹配导致的。如果GoLLIE也在SciERC上fine-tuned（或使用其原始schema format），对比结果可能完全不同。

这与我的W5一致——论文缺少与训练基方法的fair comparison，而现有的对比反而是misleading的。

---

**[AGREE] R2-W5: WikiEvents结果过于初步**

与我的W3（Major）一致。n=20、MDE=±5.0pp（Table 31, p.31），Introduction contribution list中"validates event extraction applicability"这个用词过度推销了统计效力极弱的结果。

补充一点：Table 4（p.7）的fine-tuning结果在n=20下尤其不可靠。论文报告的"CF remains low (0.77-1.18%)"基于~20个文档的fine-tuning，bootstrap CI极宽（±3-5pp），任何具体数字都应被视为directional estimates而非reliable conclusions。

---

**[REBUT] R2-W6: Limitations部分过长**

不同意R2的判断。

R2认为~1.5页Limitations接近EMNLP 2026 "excessive additional content"的边界。但查看Limitations内容（p.9），它覆盖了：(1) CF违规的constraint scope及其模型依赖性；(2) continuation masking的scalability限制（prefix collision at ~200 types）；(3) evaluation coverage（WikiEvents n=20、70B INT4）；(4) parse failure confounds。

这些都是**substantive limitations directly affecting the paper's claims**，不是padding。特别是CF违规的讨论和continuation masking的scalability warning——如果这些被移到appendix，读者可能miss关键的caveats。事实上，在我的W1中，我指出CF gap的64%数字**应该**出现在主文而非仅在附录——Limitations是放这个数字的自然位置。

EMNLP 2026规则说"provided they do not contain excessive additional content"——"excessive"指的是不相关的padding，不是substantive technical discussion of genuine limitations。当前Limitations的密度和relevance符合要求。

不过，R2提到的部分具体数字（如residual DR分解、TCR讨论的detailed mechanics）可以精简，我同意有10-15%的压缩空间。

---

**[AGREE] R2-W7: "Empirical enabling dependency"表述重复**

同意。我在通读论文时也注意到这一点——Abstract、§1 Introduction、§3 "Empirical Observation"段落、§4 Constraint Composition、§5.1消融分析中，同一个观察（grammar alone 84% at 8B, semantic alone 24%）至少出现5次且措辞高度相似。在8页主文中，这种重复消耗了宝贵空间。建议在Abstract和§1各保留一次提及，§3定义并首次展示，§5.1消融分析中引用§3——总共3次，释放约0.3页空间给fine-tuning分析。

---

### Questions 回应

**[AGREE] R2-Q1: 约束引入的false negatives对recall的影响**

R2问得好。§5.1末尾的downstream impact分析（p.5）报告0.49%被移除的三元组匹配gold label——但这只衡量了**被约束后验移除**的部分。R2正确指出还存在另一类false negatives：约束mask在生成过程中**阻止模型进入**某些合法但稀有的type combination路径，这些triple从未被生成，因此也无法被downstream analysis捕获。

这是一个genuine gap。论文的constraint tightness分析（§4, κ值）间接触及了这个问题——低κ意味着masking移除的token比例高，更可能阻断合法生成路径。但没有direct quantification。建议至少在附录增加一个experiment：比较constrained vs. unconstrained生成中gold triple的recall差异（不仅是violation-free triples的precision）。

---

**[REBUT] R2-Q2: DocRED grammar-only增加DR的"latent violation surfacing"效应是否在fine-tuning后持续**

R2的关切有道理，但论文数据已回答了这个问题。

Table 2（p.6）显示DocRED fine-tuned S1配置下DR=0.02-0.08%（Qwen/Llama），远低于unconstrained fine-tuned的1-2%。更重要的是，Table 2中grammar-only fine-tuned配置（如有）与S1 fine-tuned的对比应能直接回答"grammar layer在fine-tuning后是否仍surfacing violations"。从Table 1的zero-shot消融看，grammar-only从15.37%→12.55%（SciERC），而在DocRED从18.46%→26.17%——surfacing效应是dataset-specific的（DocRED的96个relation type使grammar-level vocabulary restriction更tight，迫使模型进入更受限空间）。

Fine-tuning后，模型已学习了schema-compliant类型分布，grammar layer的constraining效应大幅减弱，因此surfacing现象不应持续。§5.1（p.5-6）的fine-tuning composability结果支持这一判断：S1 fine-tuned下DR接近0%，说明grammar+semantic层在fine-tuned模型上是complementary而非counterproductive的。

但R2的问题揭示了一个更深的issue：**grammar layer在某些复杂schema下可能over-constrain**，这一点论文确实没有充分讨论。建议在Discussion中增加一段关于"grammar layer对不同schema复杂度的sensitivity"。

---

**[AGREE] R2-Q3: Beam search k=2作为折中**

完全同意R2的关切。Appendix F（Tables 24-29）展示了k=1（greedy）和k=4/8的结果，但**k=2完全缺失**。对于实际部署，k=1→k=4的跳跃太大——k=2可能以更低的latency cost（约1.2-1.3×而非1.54×）消除大部分violations。理解violation elimination与k的关系曲线对部署决策至关重要。

这也与R2-W2相关：如果k=2已足以消除CF violations，那么"容忍CF vs. 支付beam延迟"的trade-off会大幅缓解。

---

**[AGREE] R2-Q4: Entity registry的first-seen type行为**

同意这是CF violations的主要机制来源，且主文解释不够清晰。§4 "greedy limitation"段（p.5）提到"a right constraint: leave only the entity with its first occurrence's type as registered; the relation referencing head r₁ may see a different type than expected"——但具体机制（何时第一次注册、后续出现如何处理、first-seen type是否可被override）需要更explicit的说明。

我在Round 1审稿中的Q4也问了类似问题——entity registry假设entity-first生成顺序，同一实体在不同triple中可能被分配不同类型，但registry只保留first-seen。这是一个**architectural limitation**而非bug，但论文应在§3.3中更清楚地formalize这一行为并讨论其consequences。

---

**[AGREE] R2-Q5: κ在n=3下无法建立有意义的统计关系**

完全同意。p=0.138在任何conventional significance level下都不显著。论文自己在p.20也承认"n=6 is insufficient for statistical inference on this correlation"——但κ仍然在§4中被作为分析工具presented，给读者一种"有一定解释力"的印象。

建议两个修改：(1) 在§4中明确标注κ与DR的correlation"is descriptive only, not statistically significant at any conventional level (p=0.138, n=3)"；(2) 如果作者有更多ontology可以测试（如增加ACE 2005、TACRED等schema），在revision中补充数据点以增强κ的统计效力。否则应将κ的角色降级为"descriptive metric"而非"analytical tool"。

---

### 综合评价

R2和我在三个核心问题上高度一致：
1. **CF violations是未解决的核心缺陷**（R2-W2 ≈ R1-W1）
2. **WikiEvents统计效力不足**（R2-W5 ≈ R1-W3）
3. **GoLLIE/训练基方法对比不公平或缺失**（R2-W4 ≈ R1-W5）

主要分歧在两点：
- **Zero-shot实验的价值**（R2-W3）：R2认为缺乏实用价值应压缩篇幅，我认为其作为diagnostic设置的科学价值是独立于实用性的，但同意篇幅分配应调整。
- **Limitations长度**（R2-W6）：R2认为接近"excessive"，我认为内容substantive且必要，但有少量压缩空间。

两位Reviewer均给出 **3.5 (Borderline Conference)**，confidence 4。这一致性本身说明论文处于Conference和Findings的边界——工程执行和评估深度是clear strengths，但CF gap、overclaiming、以及fair comparison的缺失是需要在revision中解决的blocking issues。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 2344 · 2026-05-23T08:34:36.957254+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0-1: 初始化和独立审稿', 'status': 'completed', 'activeForm': '已完成'}, {'content': 'Step 2: 交叉分享', 'status': 'completed', 'activeForm': '交叉分享审稿意见'}, {'content': 'Step 3: 收敛判断', 'status': 'completed', 'activeForm': '已确认收敛，无需 Round 2'}, {'content': 'Step 4a: 检查视觉审查状态', 'status': 'in_progress', 'activeForm': '检查视觉审查状态'}, {'content': 'Step 4b: 同步 Issue Tracker', 'status': 'pending', 'activeForm': '同步 review_issues.yaml'}, {'content': 'Step 4c: 合成报告并投递', 'status': 'pending', 'activeForm': '合成并投递审稿报告'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Step 0-1: 初始化和独立审稿', 'status': 'completed', 'activeForm': '已完成'}, {'content': 'Step 2: 交叉分享', 'status': 'completed', 'activeForm': '交叉分享审稿意见'}, {'content': 'Step 3: 收敛判断', 'status': 'completed', 'activeForm': '已确认收敛，无需 Round 2'}, {'content': 'Step 4a: 检查视觉审查状态', 'status': 'in_progress', 'activeForm': '检查视觉审查状态'}, {'content': 'Step 4b: 同步 Issue Tracker', 'status': 'pending', 'activeForm': '同步 review_issues.yaml'}, {'content': 'Step 4c: 合成报告并投递', 'status': 'pending', 'activeForm': '合成并投递审稿报告'}]"
  }
}
```

</details>

---


### Tool result

_source line 2345 · 2026-05-23T08:34:37.007955+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "TodoWrite",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2346 · 2026-05-23T08:34:40.673058+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "schema_semantic_constrained_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "schema_semantic_constrained_ie"
  }
}
```

</details>

---


### Tool result

_source line 2347 · 2026-05-23T08:34:40.775104+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-23T08:20:08.363882+00:00\", \"completed_at\": \"2026-05-23T08:24:20.335520+00:00\", \"findings\": [{\"severity\": \"info\", \"dimension\": \"page 1-2\", \"message\": \"前两页为纯文本（Abstract + Introduction + Background 开头），无 display item。ACL 双栏格式下属正常现象，但审稿人的视觉锚定被推迟到第 3 页\"}, {\"severity\": \"info\", \"dimension\": \"page 3\", \"message\": \"第一个 display item 为 Figure 1（全宽 figure*，架构概览图），出现在第 3 页，位置合理。图示两层约束架构（Grammar Layer + Semantic Layer），caption 自包含，能传达核心 idea。图内部分文字标签偏小（如 JSON structure 框内的字段名），但整体可读\"}, {\"severity\": \"warning\", \"dimension\": \"page 4-5\", \"message\": \"连续两页纯文本（Method §3.1-3.4 + Constraint Composition §4），仅有行内公式和少量 display math 打破文字密度。方法论述段落有公式穿插可接受，但缺少 method 阶段的 illustrative figure（如约束组合的可视化示例）\"}, {\"severity\": \"info\", \"dimension\": \"page 6\", \"message\": \"Table 1（五路消融）+ Table 2（跨数据集验证）排布合理，booktabs 风格，最优值加粗，小数精度一致（2 位）。双表占据大部分页面面积，与上方结果文字紧密衔接\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Table 3（三模型零样本验证）+ Table 4（WikiEvents EE 结果）排布得当。表格格式与第 6 页一致。Section 5.4 标题后有足够正文，无孤悬\"}, {\"severity\": \"warning\", \"dimension\": \"page 8-9\", \"message\": \"连续两页纯文本：第 8 页包含 §6 Related Work + §7 Discussion and Conclusion，第 9 页整页为 Limitations。无任何 display item 穿插，阅读体验单调。Limitations 段落非常长（占满整页），对 EMNLP 2026 的要求而言内容偏多（建议约 3 个要点、简短覆盖即可）\"}, {\"severity\": \"info\", \"dimension\": \"page 9\", \"message\": \"Limitations 内容虽长但条理清晰，覆盖了 constraint scope、evaluation coverage、CF tradeoff 等维度。从排版角度看无溢出或格式问题\"}, {\"severity\": \"info\", \"dimension\": \"page 10\", \"message\": \"Ethics Statement 简洁（约 1/4 页），References 紧随其后开始，排版正常。页眉页脚符合 ACL 模板\"}, {\"severity\": \"info\", \"dimension\": \"page 10-13\", \"message\": \"References 共约 3.5 页，格式统一（author 缩写一致、年份格式一致），未见 [?] 未解析引用或跳号。无 overfull hbox 溢出\"}, {\"severity\": \"info\", \"dimension\": \"page 14\", \"message\": \"Table 5（Extraction prompts）为全宽表格，包含 SciERC 和 DocRED 的 system/user prompt 模板。等宽字体排版清晰，
…[truncated 1890 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 102
}
```

</details>

---


### Tool call

_source line 2348 · 2026-05-23T08:34:40.775583+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "schema_semantic_constrained_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "schema_semantic_constrained_ie"
  }
}
```

</details>

---


### Tool result

_source line 2349 · 2026-05-23T08:34:40.826152+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2350 · 2026-05-23T08:35:25.640570+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0-3: 初始化到收敛判断', 'status': 'completed', 'activeForm': '已完成'}, {'content': 'Step 4a: 检查视觉审查状态', 'status': 'completed', 'activeForm': '检查视觉审查状态'}, {'content': 'Step 4b: 同步 Issue Tracker', 'status': 'in_progress', 'activeForm': '同步 review_issues.yaml'}, {'content': 'Step 4c: 合成报告并投递', 'status': 'pending', 'activeForm': '合成并投递审稿报告'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Step 0-3: 初始化到收敛判断', 'status': 'completed', 'activeForm': '已完成'}, {'content': 'Step 4a: 检查视觉审查状态', 'status': 'completed', 'activeForm': '检查视觉审查状态'}, {'content': 'Step 4b: 同步 Issue Tracker', 'status': 'in_progress', 'activeForm': '同步 review_issues.yaml'}, {'content': 'Step 4c: 合成报告并投递', 'status': 'pending', 'activeForm': '合成并投递审稿报告'}]"
  }
}
```

</details>

---


### Tool result

_source line 2351 · 2026-05-23T08:35:25.641205+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2352 · 2026-05-23T08:37:18.326475+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "schema_semantic_constrained_ie",
  "issues_yaml": "# Review Issues Tracker — schema_semantic_constrained_ie\n# Updated: Round 23 fresh review, 2026-05-23\n\n# ============================================================\n# Round 23 — New Issues\n# ============================================================\n\n- id: \"R23-W1\"\n  summary: \"CF 违规占残余违规 64%，与标题 'Type-Constrained IE' 形成 gap，正文讨论不足\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 23\n  last_seen_round: 23\n  mentions:\n    - round: 23\n      reviewers: [1, 2]\n      note: \"R1-W1 (Critical) + R2-W2 (Major)。Table 9: S1 SciERC 245 残余违规中 CF=155 (63.9%)。两位 Reviewer 共识：正文应量化 CF 比例、讨论架构限制。R1 建议改标题；R2 建议界定 'type-constrained' 范围即可。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R23-W2\"\n  summary: \"算法创新有限——主要是 XGrammar + stateful logits processor 的系统集成\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 23\n  last_seen_round: 23\n  mentions:\n    - round: 23\n      reviewers: [1, 2]\n      note: \"R2-W1 (Major)。R1 交叉回应 AGREE 但 nuance: enabling dependency 和三级分类有独立价值。共识：定位为 strong engineering contribution，降低理论贡献措辞强度。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R23-W3\"\n  summary: \"GoLLIE 对比不公平 + 缺少与训练基方法的系统性对比\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 23\n  last_seen_round: 23\n  mentions:\n    - round: 23\n      reviewers: [1, 2]\n      note: \"R1-W5 (Major) + R2-W4 (Minor)。Appendix Q GoLLIE ZS vs OntoCoDec FT 不公平。§6 引用可能误导。R2 REBUT R1: 互补定位使直接对比 methodologically difficult，但需说明原因。共识：至少解释为何直接对比不可行。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R23-W4\"\n  summary: \"WikiEvents n=20 统计效力不足但结论呈现过度自信\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 23\n  last_seen_round: 23\n  mentions:\n    - round: 23\n      reviewers: [1, 2]\n      note: \"R1-W3 (Major) + R2-W5 (Minor)。共识：MDE=±5.0pp，不应在 n=20 上报告 fine-tuning composability 结论。Introduction contribution list 'validates event extraction applicability' 过度推销。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R23-W5\"\n  summary: \"70B 实验全在 AWQ INT4 上，Abstract 未标注，§5.3 量化限制披露过晚\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 23\n  last_seen_round: 23\n  mentions:\n    - round: 23\n      reviewers: [1, 2]\n      note: \"R1-W4 (Major)。R2 交叉 AGREE 但降低严重性（8B 消融已确认 INT4 不影响 DR）。共识：Abstract 标注 '70B (AWQ INT4)'，§5.3 开头说明量化限制。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R23-W6\"\n  summary: \"Zero-shot 实验占主文 ~3 页但 R-F1 仅 4-8%，篇幅分配失衡\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 23\n  last_seen_round: 23\n  mentions:\n    - round: 23\n      reviewers: [1, 2]\n      note: \"R2-W3 (Major)。R1 交叉 REBUT: ZS 作为 diagnostic probe 有科学价值（消融隔离约束效果），但 AGREE 篇幅分配应调整——压缩 ZS 为 1 段+Table 1，扩展 fine-tuning 分析。分歧：价值判断不同，但篇幅调整共识。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R23-W7\"\n  summary: \"Proposition 1 实际意义论证 gap: unbounded 理论 vs bounded 工程之间逻辑跳跃\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 23\n  last_seen_round: 23\n  mentions:\n    - round: 23\n      reviewers: [1, 2]\n      note: \"R1-W2 (Major)。R2 交叉 REBUT: Remark 已区分但不够 prominent。分歧：R1 Major vs R2 Minor。Director 判定 info (Remark 已覆盖，需提升 prominence)。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R23-W8\"\n  summary: \"'Empirical enabling dependency' 在主文中重复出现 ≥6 次\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 23\n  last_seen_round: 23\n  mentions:\n    - round: 23\n      reviewers: [1, 2]\n      note: \"R2-W7 (Minor)。R1 交叉 AGREE。共识：保留 3 次（Abstract、§3 定义、§5.1 引用），释放 ~0.3 页空间。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R23-W9\"\n  summary: \"Fallback 频率模型依赖性未在正文讨论 (Qwen 0 vs Llama 5882)\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 23\n  last_seen_round: 23\n  mentions:\n    - round: 23\n      reviewers: [1, 2]\n      note: \"R1-W6 (Minor)。R2 交叉 AGREE。Table 6: Qwen 0 vs Llama 5882 次 fallback。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R23-W10\"\n  summary: \"Continuation masking prefix collision 频率未量化\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 23\n  last_seen_round: 23\n  mentions:\n    - round: 23\n      reviewers: [1, 2]\n      note: \"R1-W7 (Minor)。R2 交叉 AGREE。建议附录增加 prefix collision 频率分析。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R23-W11\"\n  summary: \"Beam k=2 中间值缺失，k 与违规消除关系不明\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 23\n  last_seen_round: 23\n  mentions:\n    - round: 23\n      reviewers: [1, 2]\n      note: \"R2-Q3。R1 交叉 AGREE。Appendix F 仅展示 k=1 和 k=4/8，k=2 完全缺失。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R23-W12\"\n  summary: \"Entity registry first-seen type 行为主文解释不够清晰\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 23\n  last_seen_round: 23\n  mentions:\n    - round: 23\n      reviewers: [1, 2]\n      note: \"R2-Q4 + R1-Q4。共识：CF 主要来源于 first-seen 注册机制，§3.3 应更显式 formalize。entity-first 生成顺序是架构约束，应在 Limitations 中明确。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R23-D1\"\n  summary: \"Limitations 长度是否 'excessive'：R2 认为偏长，R1 认为内容 substantive\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 23\n  last_seen_round: 23\n  mentions:\n    - round: 23\n      reviewers: [1, 2]\n      note: \"R2-W6 (Minor) vs R1 REBUT。R1 认为内容有实质性，不是 padding，但同意有 10-15% 压缩空间。Director 判定: info，可适度精简。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# Prior Rounds — in_progress (R23 status update)\n# ============================================================\n\n- id: \"R16-W5\"\n  summary: \"核心新颖性定位——系统集成而非算法创新，novelty ceiling 有限\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 23\n  mentions:\n    - round: 19\n      reviewers: [1, 2]\n      note: \"R19: 共识定位为 systems contribution。\"\n    - round: 20\n      reviewers: [1, 2]\n      note: \"R20: 论文已正确定位。\"\n    - round: 21\n      reviewers: [1, 2]\n      note: \"R21 D3: R2 'limited novelty' vs R1 'moderate novelty with strong execution'。\"\n    - round: 23\n      reviewers: [1, 2]\n      note: \"R23: 与 R23-W2 合并。R2-W1 再次指出 Prop 1 缺乏 surprise value，XGrammar+logits processor 组合自然。R1 nuance: enabling dependency 有独立价值。\"\n  action_items:\n    - round: 19\n      action: \"§7 Discussion 坦率定位 systems contribution\"\n      assigned_to: paper_agent\n      status: completed\n    - round: 21\n      action: \"§3 method 段落论证 semantic layer 非显而易见设计选择\"\n      assigned_to: paper_agent\n      status: completed\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R20-W1\"\n  summary: \"Proposition 1 证明中 position→name 转换缺乏形式论证\"\n  category: method\n  severity: info\n  status: in_progress\n  first_raised_round: 20\n  last_seen_round: 23\n  mentions:\n    - round: 20\n      reviewers: [1]\n      note: \"R1-W3。\"\n    - round: 21\n      reviewers: [1]\n      note: \"R21 R1-W5 (Minor)。R2 REBUT 认为简化合理。\"\n    - round: 23\n      reviewers: [1, 2]\n      note: \"R23: R1-W2 扩展为 unbounded vs bounded gap。R2 REBUT 称 Remark 已区分。Director: 需提升 prominence 但非 Major。\"\n  action_items:\n    - round: 20\n      action: \"Appendix O 加 informal argument\"\n      assigned_to: paper_agent\n      status: completed\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R20-W4\"\n  summary: \"主文 Related Work §6 过于精简，ADELIE 缺失\"\n  category: related_work\n  severity: info\n  status: in_progress\n  first_raised_round: 20\n  last_seen_round: 23\n  mentions:\n    - round: 20\n      reviewers: [2]\n      note: \"R2-W2。ADELIE 缺失；PICARD 对比不足；SGLang 未提及。\"\n    - round: 21\n      note: \"R21 R16: 补 Text2Event + Huang et al. 2024。\"\n    - round: 23\n      reviewers: [1, 2]\n      note: \"R23: R2-S4 评价相关工作覆盖 '充分'。R1 未提出新遗漏。本轮未被独立提及为 weakness。可能已修复。\"\n  action_items:\n    - round: 20\n      action: \"§6 提升 ADELIE；扩展 PICARD；提及 SGLang\"\n      assigned_to: paper_agent\n      status: completed\n    - round: 21\n      action: \"补 Text2Event + Huang et al. 2024 引用\"\n      assigned_to: paper_agent\n      status: completed\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R18-M2\"\n  summary: \"Figure 1 视觉层次不够分明 + 未可视化 fallback 路径\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 18\n  last_seen_round: 23\n  mentions:\n    - round: 18\n      reviewers: [1, 2]\n      note: \"R18: 小问题。\"\n    - round: 21\n      reviewers: [1, 2]\n      note: \"R21: Grammar-first fallback 应在 Figure 1 中体现。\"\n    - round: 23\n      note: \"R23: 视觉审查 info——Figure 1 caption 自包含，能传达核心 idea，部分文字标签偏小。本轮 Reviewer 未独立提及。\"\n  action_items:\n    - round: 21\n      action: \"Figure 1 重新生成（Paper Banana 失败，保留当前版本）\"\n      assigned_to: main_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R21-N2\"\n  summary: \"Full FT 组合性解读分歧——R-F1 不变是否意味约束无效\"\n  category: experiment\n  severity: info\n  status: in_progress\n  first_raised_round: 21\n  last_seen_round: 23\n  mentions:\n    - round: 21\n      reviewers: [1, 2]\n      note: \"D2: R1 误读 F1 不变=约束无效。R2 data rebuttal。Director 降级为 info。\"\n    - round: 23\n      note: \"R23 本轮未提及，可能已修复。\"\n  action_items:\n    - round: 21\n      action: \"Appendix L 更显式突出 full FT unconstrained DR=2.74%, S1→0%, F1 不变\"\n      assigned_to: paper_agent\n      status: completed\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R21-Q1\"\n  summary: \"Beam search k=8 时 per-beam registry 内存开销未量化\"\n  category: experiment\n  severity: info\n  status: in_progress\n  first_raised_round: 21\n  last_seen_round: 23\n  mentions:\n    - round: 21\n      reviewers: [1, 2]\n      note: \"Q1: Appendix F 报告了 latency 但未量化 memory。\"\n    - round: 23\n      note: \"R23 本轮未提及。与 R23-W11 (beam k=2 缺失) 相关。\"\n  action_items:\n    - round: 21\n      action: \"Appendix F 补充 beam registry 内存估算\"\n      assigned_to: paper_agent\n      status: completed\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R21-Q2\"\n  summary: \"TCR 整合到解码循环的可行性\"\n  category: method\n  severity: info\n  status: in_progress\n  first_raised_round: 21\n  last_seen_round: 23\n  mentions:\n    - round: 21\n      reviewers: [1, 2]\n      note: \"Q2: TCR 是 post-hoc 全局优化，不可嵌入 autoregressive loop。\"\n    - round: 23\n      note: \"R23 本轮未独立提及。CF 讨论中隐含（TCR 作为 CF 缓解方案效果有限）。\"\n  action_items:\n    - round: 21\n      action: \"Discussion/Appendix N 解释 TCR 不可嵌入 autoregressive 解码\"\n      assigned_to: paper_agent\n      status: completed\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R21-Q3\"\n  summary: \"GCD/BoostCD 对比是直接运行还是等价论证\"\n  category: experiment\n  severity: info\n  status: in_progress\n  first_raised_round: 21\n  last_seen_round: 23\n  mentions:\n    - round: 21\n      reviewers: [1, 2]\n      note: \"Q3: Table 16-17 基于等价论证推断。\"\n    - round: 23\n      note: \"R23 本轮未提及。\"\n  action_items:\n    - round: 21\n      action: \"Table 16-17 caption 显式声明基于等价论证\"\n      assigned_to: paper_agent\n      status: completed\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R21-Q5\"\n  summary: \"TCR vs OntoCoDec 定位不清——互补还是替代\"\n  category: method\n  severity: info\n  status: in_progress\n  first_raised_round: 21\n  last_seen_round: 23\n  mentions:\n    - round: 21\n      reviewers: [1, 2]\n      note: \"Q5: TCR 减少 CF 但不解决 DR。应定位为互补。\"\n    - round: 23\n      note: \"R23 本轮未独立提及。\"\n  action_items:\n    - round: 21\n      action: \"Appendix N 明确 TCR 互补定位\"\n      assigned_to: paper_agent\n      status: completed\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# Prior Rounds — Resolved (保留关键条目供参考)\n# ============================================================\n\n- id: \"R16-MF3\"\n  summary: \"CF trade-off 在 Abstract 中 framing 偏乐观——仅报告 1.18% 而实际范围达 12.02%\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 21\n  resolution: \"Abstract 完整重写为三段式。CF 分层报告：FT ≤1.4% (line 10), ZS up to 12% (line 11)。\"\n  resolution_round: 22\n\n- id: \"R16-W4\"\n  summary: \"70B AWQ INT4 quantization 对约束效果的影响未隔离\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 21\n  resolution: \"8B FP16 vs INT4 实验完成。DR 不受 INT4 影响（0%→0%）。新增 Appendix P。\"\n  resolution_round: 22\n\n- id: \"R16-W3\"\n  summary: \"WikiEvents fine-tuning composability 仅 n=20 文档，统计效力严重不足\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 21\n  resolution: \"Abstract 无 WikiEvents 引用。§1 标 'preliminary pilot study'。\"\n  resolution_round: 22\n\n- id: \"R16-W1\"\n  summary: \"κ̄/enabling dependency 统计支撑不足：R²=0.886 基于 n=6\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 21\n  resolution: \"全文加 'empirical' + 'scale-dependent' qualifier。§3 Corollary→Empirical Observation。\"\n  resolution_round: 22\n\n- id: \"R15-MF3\"\n  summary: \"正文溢出至第 9 页\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 21\n  resolution: \"主文 §1-§7 在 page 1-8。\"\n  resolution_round: 22\n\n# ============================================================\n# Won't Fix\n# ============================================================\n\n- id: \"R20-W5\"\n  summary: \"Running example 仍不充分\"\n  category: writing\n  severity: info\n  status: wont_fix\n  first_raised_round: 20\n  last_seen_round: 21\n  resolution: \"空间限制无法在正文加完整 running example。§3.3 有 Used-for 示例。\"\n  resolution_round: 20\n\n- id: \"R20-W6\"\n  summary: \"Zero-shot 评估实际意义有限（R-F1 仅 4-8%）\"\n  category: experiment\n  severity: info\n  status: wont_fix\n  first_raised_round: 20\n  last_seen_round: 21\n  resolution: \"ZS 已定位为 diagnostic probe。\"\n  resolution_round: 20\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "schema_semantic_constrained_ie",
    "issues_yaml": "# Review Issues Tracker — schema_semantic_constrained_ie\n# Updated: Round 23 fresh review, 2026-05-23\n\n# ============================================================\n# Round 23 — New Issues\n# ============================================================\n\n- id: \"R23-W1\"\n  summary: \"CF 违规占残余违规 64%，与标题 'Type-Constrained IE' 形成 gap，正文讨论不足\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 23\n  last_seen_round: 23\n  mentions:\n    - round: 23\n      reviewers: [1, 2]\n      note: \"R1-W1 (Critical) + R2-W2 (Major)。Table 9: S1 SciERC 245 残余违规中 CF=155 (63.9%)。两位 Reviewer 共识：正文应量化 CF 比例、讨论架构限制。R1 建议改标题；R2 建议界定 'type-constrained' 范围即可。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R23-W2\"\n  summary: \"算法创新有限——主要是 XGrammar + stateful logits processor 的系统集成\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 23\n  last_seen_round: 23\n  mentions:\n    - round: 23\n      reviewers: [1, 2]\n      note: \"R2-W1 (Major)。R1 交叉回应 AGREE 但 nuance: enabling dependency 和三级分类有独立价值。共识：定位为 strong engineering contribution，降低理论贡献措辞强度。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R23-W3\"\n  summary: \"GoLLIE 对比不公平 + 缺少与训练基方法的系统性对比\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 23\n  last_seen_round: 23\n  mentions:\n    - round: 23\n      reviewers: [1, 2]\n      note: \"R1-W5 (Major) + R2-W4 (Minor)。Appendix Q GoLLIE ZS vs OntoCoDec FT 不公平。§6 引用可能误导。R2 REBUT R1: 互补定位使直接对比 methodologically difficult，但需说明原因。共识：至少解释为何直接对比不可行。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R23-W4\"\n  summary: \"WikiEvents n=20 统计效力不足但结论呈现过度自信\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 23\n  last_seen_round: 23\n  mentions:\n    - round: 23\n      reviewers: [1, 2]\n      note: \"R1-W3 (Major) + R2-W5 (Minor)。共识：MDE=±5.0pp，不应在 n=20 上报告 fine-tuning composability 结论。Introduction contribution list 'validates event extraction applicability' 过度推销。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R23-W5\"\n  summary: \"70B 实验全在 AWQ INT4 上，Abstract 未标注，§5.3 量化限制披露过晚\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 23\n  last_seen_round: 23\n  mentions:\n    - round: 23\n      reviewers: [1, 2]\n      note: \"R1-W4 (Major)。R2 交叉 AGREE 但降低严重性（8B 消融已确认 INT4 不影响 DR）。共识：Abstract 标注 '70B (AWQ INT4)'，§5.3 开头说明量化限制。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R23-W6\"\n  summary: \"Zero-shot 实验占主文 ~3 页但 R-F1 仅 4-8%，篇幅分配失衡\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 23\n  last_seen_round: 23\n  mentions:\n    - round: 23\n      reviewers: [1, 2]\n      note: \"R2-W3 (Major)。R1 交叉 REBUT: ZS 作为 diagnostic probe 有科学价值（消融隔离约束效果），但 AGREE 篇幅分配应调整——压缩 ZS 为 1 段+Table 1，扩展 fine-tuning 分析。分歧：价值判断不同，但篇幅调整共识。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R23-W7\"\n  summary: \"Proposition 1 实际意义论证 gap: unbounded 理论 vs bounded 工程之间逻辑跳跃\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 23\n  last_seen_round: 23\n  mentions:\n    - round: 23\n      reviewers: [1, 2]\n      note: \"R1-W2 (Major)。R2 交叉 REBUT: Remark 已区分但不够 prominent。分歧：R1 Major vs R2 Minor。Director 判定 info (Remark 已覆盖，需提升 prominence)。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R23-W8\"\n  summary: \"'Empirical enabling dependency' 在主文中重复出现 ≥6 次\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 23\n  last_seen_round: 23\n  mentions:\n    - round: 23\n      reviewers: [1, 2]\n      note: \"R2-W7 (Minor)。R1 交叉 AGREE。共识：保留 3 次（Abstract、§3 定义、§5.1 引用），释放 ~0.3 页空间。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R23-W9\"\n  summary: \"Fallback 频率模型依赖性未在正文讨论 (Qwen 0 vs Llama 5882)\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 23\n  last_seen_round: 23\n  mentions:\n    - round: 23\n      reviewers: [1, 2]\n      note: \"R1-W6 (Minor)。R2 交叉 AGREE。Table 6: Qwen 0 vs Llama 5882 次 fallback。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R23-W10\"\n  summary: \"Continuation masking prefix collision 频率未量化\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 23\n  last_seen_round: 23\n  mentions:\n    - round: 23\n      reviewers: [1, 2]\n      note: \"R1-W7 (Minor)。R2 交叉 AGREE。建议附录增加 prefix collision 频率分析。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R23-W11\"\n  summary: \"Beam k=2 中间值缺失，k 与违规消除关系不明\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 23\n  last_seen_round: 23\n  mentions:\n    - round: 23\n      reviewers: [1, 2]\n      note: \"R2-Q3。R1 交叉 AGREE。Appendix F 仅展示 k=1 和 k=4/8，k=2 完全缺失。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R23-W12\"\n  summary: \"Entity registry first-seen type 行为主文解释不够清晰\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 23\n  last_seen_round: 23\n  mentions:\n    - round: 23\n      reviewers: [1, 2]\n      note: \"R2-Q4 + R1-Q4。共识：CF 主要来源于 first-seen 注册机制，§3.3 应更显式 formalize。entity-first 生成顺序是架构约束，应在 Limitations 中明确。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R23-D1\"\n  summary: \"Limitations 长度是否 'excessive'：R2 认为偏长，R1 认为内容 substantive\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 23\n  last_seen_round: 23\n  mentions:\n    - round: 23\n      reviewers: [1, 2]\n      note: \"R2-W6 (Minor) vs R1 REBUT。R1 认为内容有实质性，不是 padding，但同意有 10-15% 压缩空间。Director 判定: info，可适度精简。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# Prior Rounds — in_progress (R23 status update)\n# ============================================================\n\n- id: \"R16-W5\"\n  summary: \"核心新颖性定位——系统集成而非算法创新，novelty ceiling 有限\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 23\n  mentions:\n    - round: 19\n      reviewers: [1, 2]\n      note: \"R19: 共识定位为 systems contribution。\"\n    - round: 20\n      reviewers: [1, 2]\n      note: \"R20: 论文已正确定位。\"\n    - round: 21\n      reviewers: [1, 2]\n      note: \"R21 D3: R2 'limited novelty' vs R1 'moderate novelty with strong execution'。\"\n    - round: 23\n      reviewers: [1, 2]\n      note: \"R23: 与 R23-W2 合并。R2-W1 再次指出 Prop 1 缺乏 surprise value，XGrammar+logits processor 组合自然。R1 nuance: enabling dependency 有独立价值。\"\n  action_items:\n    - round: 19\n      action: \"§7 Discussion 坦率定位 systems contribution\"\n      assigned_to: paper_agent\n      status: completed\n    - round: 21\n      action: \"§3 method 段落论证 semantic layer 非显而易见设计选择\"\n      assigned_to: paper_agent\n      status: completed\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R20-W1\"\n  summary: \"Proposition 1 证明中 position→name 转换缺乏形式论证\"\n  category: method\n  severity: info\n  status: in_progress\n  first_raised_round: 20\n  last_seen_round: 23\n  mentions:\n    - round: 20\n      reviewers: [1]\n      note: \"R1-W3。\"\n    - round: 21\n      reviewers: [1]\n      note: \"R21 R1-W5 (Minor)。R2 REBUT 认为简化合理。\"\n    - round: 23\n      reviewers: [1, 2]\n      note: \"R23: R1-W2 扩展为 unbounded vs bounded gap。R2 REBUT 称 Remark 已区分。Director: 需提升 prominence 但非 Major。\"\n  action_items:\n    - round: 20\n      action: \"Appendix O 加 informal argument\"\n      assigned_to: paper_agent\n      status: completed\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R20-W4\"\n  summary: \"主文 Related Work §6 过于精简，ADELIE 缺失\"\n  category: related_work\n  severity: info\n  status: in_progress\n  first_raised_round: 20\n  last_seen_round: 23\n  mentions:\n    - round: 20\n      reviewers: [2]\n      note: \"R2-W2。ADELIE 缺失；PICARD 对比不足；SGLang 未提及。\"\n    - round: 21\n      note: \"R21 R16: 补 Text2Event + Huang et al. 2024。\"\n    - round: 23\n      reviewers: [1, 2]\n      note: \"R23: R2-S4 评价相关工作覆盖 '充分'。R1 未提出新遗漏。本轮未被独立提及为 weakness。可能已修复。\"\n  action_items:\n    - round: 20\n      action: \"§6 提升 ADELIE；扩展 PICARD；提及 SGLang\"\n      assigned_to: paper_agent\n      status: completed\n    - round: 21\n      action: \"补 Text2Event + Huang et al. 2024 引用\"\n      assigned_to: paper_agent\n      status: completed\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R18-M2\"\n  summary: \"Figure 1 视觉层次不够分明 + 未可视化 fallback 路径\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 18\n  last_seen_round: 23\n  mentions:\n    - round: 18\n      reviewers: [1, 2]\n      note: \"R18: 小问题。\"\n    - round: 21\n      reviewers: [1, 2]\n      note: \"R21: Grammar-first fallback 应在 Figure 1 中体现。\"\n    - round: 23\n      note: \"R23: 视觉审查 info——Figure 1 caption 自包含，能传达核心 idea，部分文字标签偏小。本轮 Reviewer 未独立提及。\"\n  action_items:\n    - round: 21\n      action: \"Figure 1 重新生成（Paper Banana 失败，保留当前版本）\"\n      assigned_to: main_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R21-N2\"\n  summary: \"Full FT 组合性解读分歧——R-F1 不变是否意味约束无效\"\n  category: experiment\n  severity: info\n  status: in_progress\n  first_raised_round: 21\n  last_seen_round: 23\n  mentions:\n    - round: 21\n      reviewers: [1, 2]\n      note: \"D2: R1 误读 F1 不变=约束无效。R2 data rebuttal。Director 降级为 info。\"\n    - round: 23\n      note: \"R23 本轮未提及，可能已修复。\"\n  action_items:\n    - round: 21\n      action: \"Appendix L 更显式突出 full FT unconstrained DR=2.74%, S1→0%, F1 不变\"\n      assigned_to: paper_agent\n      status: completed\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R21-Q1\"\n  summary: \"Beam search k=8 时 per-beam registry 内存开销未量化\"\n  category: experiment\n  severity: info\n  status: in_progress\n  first_raised_round: 21\n  last_seen_round: 23\n  mentions:\n    - round: 21\n      reviewers: [1, 2]\n      note: \"Q1: Appendix F 报告了 latency 但未量化 memory。\"\n    - round: 23\n      note: \"R23 本轮未提及。与 R23-W11 (beam k=2 缺失) 相关。\"\n  action_items:\n    - round: 21\n      action: \"Appendix F 补充 beam registry 内存估算\"\n      assigned_to: paper_agent\n      status: completed\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R21-Q2\"\n  summary: \"TCR 整合到解码循环的可行性\"\n  category: method\n  severity: info\n  status: in_progress\n  first_raised_round: 21\n  last_seen_round: 23\n  mentions:\n    - round: 21\n      reviewers: [1, 2]\n      note: \"Q2: TCR 是 post-hoc 全局优化，不可嵌入 autoregressive loop。\"\n    - round: 23\n      note: \"R23 本轮未独立提及。CF 讨论中隐含（TCR 作为 CF 缓解方案效果有限）。\"\n  action_items:\n    - round: 21\n      action: \"Discussion/Appendix N 解释 TCR 不可嵌入 autoregressive 解码\"\n      assigned_to: paper_agent\n      status: completed\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R21-Q3\"\n  summary: \"GCD/BoostCD 对比是直接运行还是等价论证\"\n  category: experiment\n  severity: info\n  status: in_progress\n  first_raised_round: 21\n  last_seen_round: 23\n  mentions:\n    - round: 21\n      reviewers: [1, 2]\n      note: \"Q3: Table 16-17 基于等价论证推断。\"\n    - round: 23\n      note: \"R23 本轮未提及。\"\n  action_items:\n    - round: 21\n      action: \"Table 16-17 caption 显式声明基于等价论证\"\n      assigned_to: paper_agent\n      status: completed\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R21-Q5\"\n  summary: \"TCR vs OntoCoDec 定位不清——互补还是替代\"\n  category: method\n  severity: info\n  status: in_progress\n  first_raised_round: 21\n  last_seen_round: 23\n  mentions:\n    - round: 21\n      reviewers: [1, 2]\n      note: \"Q5: TCR 减少 CF 但不解决 DR。应定位为互补。\"\n    - round: 23\n      note: \"R23 本轮未独立提及。\"\n  action_items:\n    - round: 21\n      action: \"Appendix N 明确 TCR 互补定位\"\n      assigned_to: paper_agent\n      status: completed\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# Prior Rounds — Resolved (保留关键条目供参考)\n# ============================================================\n\n- id: \"R16-MF3\"\n  summary: \"CF trade-off 在 Abstract 中 framing 偏乐观——仅报告 1.18% 而实际范围达 12.02%\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 21\n  resolution: \"Abstract 完整重写为三段式。CF 分层报告：FT ≤1.4% (line 10), ZS up to 12% (line 11)。\"\n  resolution_round: 22\n\n- id: \"R16-W4\"\n  summary: \"70B AWQ INT4 quantization 对约束效果的影响未隔离\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 21\n  resolution: \"8B FP16 vs INT4 实验完成。DR 不受 INT4 影响（0%→0%）。新增 Appendix P。\"\n  resolution_round: 22\n\n- id: \"R16-W3\"\n  summary: \"WikiEvents fine-tuning composability 仅 n=20 文档，统计效力严重不足\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 21\n  resolution: \"Abstract 无 WikiEvents 引用。§1 标 'preliminary pilot study'。\"\n  resolution_round: 22\n\n- id: \"R16-W1\"\n  summary: \"κ̄/enabling dependency 统计支撑不足：R²=0.886 基于 n=6\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 21\n  resolution: \"全文加 'empirical' + 'scale-dependent' qualifier。§3 Corollary→Empirical Observation。\"\n  resolution_round: 22\n\n- id: \"R15-MF3\"\n  summary: \"正文溢出至第 9 页\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 21\n  resolution: \"主文 §1-§7 在 page 1-8。\"\n  resolution_round: 22\n\n# ============================================================\n# Won't Fix\n# ============================================================\n\n- id: \"R20-W5\"\n  summary: \"Running example 仍不充分\"\n  category: writing\n  severity: info\n  status: wont_fix\n  first_raised_round: 20\n  last_seen_round: 21\n  resolution: \"空间限制无法在正文加完整 running example。§3.3 有 Used-for 示例。\"\n  resolution_round: 20\n\n- id: \"R20-W6\"\n  summary: \"Zero-shot 评估实际意义有限（R-F1 仅 4-8%）\"\n  category: experiment\n  severity: info\n  status: wont_fix\n  first_raised_round: 20\n  last_seen_round: 21\n  resolution: \"ZS 已定位为 diagnostic probe。\"\n  resolution_round: 20\n"
  }
}
```

</details>

---


### Tool result

_source line 2353 · 2026-05-23T08:37:18.427625+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_issues.yaml\", \"bytes\": 13507}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 2354 · 2026-05-23T08:37:27.064337+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0-3: 初始化到收敛判断', 'status': 'completed', 'activeForm': '已完成'}, {'content': 'Step 4a: 检查视觉审查状态', 'status': 'completed', 'activeForm': '检查视觉审查状态'}, {'content': 'Step 4b: 同步 Issue Tracker', 'status': 'completed', 'activeForm': '同步 review_issues.yaml'}, {'content': 'Step 4c: 合成报告并投递', 'status': 'in_progress', 'activeForm': '合成并投递审稿报告'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Step 0-3: 初始化到收敛判断', 'status': 'completed', 'activeForm': '已完成'}, {'content': 'Step 4a: 检查视觉审查状态', 'status': 'completed', 'activeForm': '检查视觉审查状态'}, {'content': 'Step 4b: 同步 Issue Tracker', 'status': 'completed', 'activeForm': '同步 review_issues.yaml'}, {'content': 'Step 4c: 合成报告并投递', 'status': 'in_progress', 'activeForm': '合成并投递审稿报告'}]"
  }
}
```

</details>

---


### Tool result

_source line 2355 · 2026-05-23T08:37:27.064966+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2356 · 2026-05-23T08:40:20.141340+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# Round 23 审稿报告 — OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints\n\n**目标 Venue**: EMNLP 2026 (via ACL Rolling Review)  \n**类别**: Long Paper  \n**审稿模式**: Fresh（无上轮记忆）  \n**Reviewer 配置**: 2 人（R1: 方法严谨性+实验设计; R2: 新颖性+完整性+写作质量）  \n**交叉分享**: 完成（R1↔R2 逐条回应）  \n**轮次**: 1 轮收敛（核心问题达成共识，无需 Round 2）\n\n---\n\n## Summary\n\n本文提出 OntoCoDec，将 IE 本体编译为两层可组合 token 级解码约束：grammar layer（基于 XGrammar 的 CFG，强制 JSON 结构和词汇成员关系）和 semantic layer（有状态 logits 处理器，通过动态 entity registry 强制 domain/range 类型约束）。论文在 SciERC、DocRED、WikiEvents 上评估了 Qwen3-8B、Llama-3.1-8B、Mistral-7B 及 Llama-3.1-70B (AWQ INT4)，提供了五路消融、bootstrap CI + Cohen's d、beam search 兼容性验证等极其详尽的实验分析。LoRA 微调 + greedy S1 近乎消除 domain/range 违规（DR<0.1%），beam search (k=4) 消除所有违规类型（1.54× 延迟）。\n\n---\n\n## Strengths\n\n**S1: 评估深度在 IE 领域极为罕见。** 39 页附录覆盖五路消融（Table 1）、bootstrap CI + Cohen's d（Appendix C）、fallback 因果追踪（Table 6-7）、cross-field 违规分解（Table 9）、document 长度分箱分析（Appendix H）、prompt 敏感性（Appendix I）、TCR post-hoc resolution（Appendix M）、beam search 兼容性（Appendix F）、8B FP16 vs INT4 消融（Appendix P）。统计报告采用 document-level bootstrap resampling（10,000 iterations），报告 MDE，诚实承认 n=6 不足以进行相关性统计推断。[R1-S3/S4, R2-S1 共识]\n\n**S2: 方法形式化严密。** Proposition 1 的 pumping lemma 论证结构正确，完整证明（Appendix O）严格。约束可判定性三级分类（context-free → prefix-decidable with state → non-local）概念清晰，精准界定了 CFG 的能力边界。Grammar-first fallback（§4, eq.2）在 soundness 和 availability 之间取得了合理平衡。[R1-S1/S2, R2 acknowledges]\n\n**S3: 诚实透明的呈现方式。** 论文明确承认 DR enforcement 引入 CF 违规、zero-shot 质量低、WikiEvents 结果是 preliminary 的。Limitations 部分极为详细，覆盖约束范围、评估覆盖度、工程局限。[R2-S2]\n\n**S4: 实用的系统设计 + Tokenizer 无关的跨模型泛化。** 延迟开销适度（greedy +10%，beam 1.54×），编译速度快（<0.5s），可扩展性测试显示 200 实体类型/1000 关系时保持恒定 2-3% 开销。Continuation masking 在三种 tokenizer 族（byte-level BPE: Qwen/Llama, SentencePiece: Mistral）上验证有效。[R1-S6, R2-S3/S5]\n\n**S5: Enabling dependency 是有价值的经验发现。** Grammar alone 84% DR at 8B vs semantic-only 24%（Table 1），但 70B 时 grammar alone 接近 semantic layer 的水平（§5.3）。Scale-dependent 特性对约束解码系统设计有指导价值。[R1-S5]\n\n---\n\n## Weaknesses\n\n### Must Fix（阻碍接收）\n\n**MF1 [Critical]: CF 违规占残余违规 64%，与标题 \"Type-Constrained IE\" 形成 gap，正文讨论严重不足。**\nTable 9（Appendix）显示 S1 配置下 SciERC 245 个残余违规中 CF=155（63.9%），集中在 GENERIC↔OtherScientificTerm（34.7%）和 GENERIC↔Material（12.3%）。系统消除了 DR violations 但引入了 CF violations 作为新的 dominant 问题。正文 §4 仅一句 \"Level 3 is addressed by beam search or post-hoc resolution\" 带过，64% 这个关键数字仅在附录出现。Greedy 部署层成为不完整方案，用户必须在\"容忍 CF\"和\"支付 beam 延迟\"之间选择——这个 trade-off 在 Abstract/Introduction 中被低估。\n**两位 Reviewer 共识**（R1-W1 Critical + R2-W2 Major）。分歧仅在标题是否需要修改（R1 建议改为 \"Domain/Range-Constrained\"；R2 建议界定 \"type-constrained\" 范围即可）。\n→ 建议：(1) §5.1 或 §4 量化 CF 占残余违规比例；(2) 讨论 CF 从架构上为何难以在单 pass 解码中解决；(3) Abstract/Introduction 诚实呈现 greedy vs beam 的 trade-off。\n\n### Should Fix（显著影响评分）\n\n**SF1 [Major]: 算法创新有限，主要是系统集成贡献。**\nProposition 1 结论对了解 PDA 局限性的研究者来说不意外。XGrammar + stateful logits processor 的组合是自然的设计选择。κ 在 n=3 下 p=0.138 统计不显著。论文自我定位为 \"systematic engineering contribution\" 是诚实的，但在 EMNLP 审稿中 novelty 仍是重要维度。\n**R2-W1 (Major)，R1 交叉 AGREE 但 nuance**：enabling dependency 和三级分类有独立价值，定位为 \"strong engineering contribution with useful empirical insights\" 在 EMNLP 可接受，但应降低理论贡献措辞强度。\n→ 建议：降低 Proposition 1 和 κ 的呈现强度，突出 enabling dependency 的实证价值和系统可复用性。\n\n**SF2 [Major]: GoLLIE 对比不公平 + 缺少与训练基方法的系统性对比。**\nAppendix Q 比较 GoLLIE-7B zero-shot（R-F1=0.0, 5 predictions）vs OntoCoDec LoRA fine-tuned——evaluation setup 不匹配。§6 主文引用该结果可能误导读者。论文定位 training-based 和 decoding-time 方法为互补，但现有对比反而是 misleading 的。\n**R1-W5 (Major) + R2-W4 (Minor) 共识**。R2 REBUT 指出互补定位使直接对比 methodologically difficult，但同意需说明原因。\n→ 建议：(1) §6 修正 GoLLIE 引用措辞，明确标注 setup 差异；(2) 解释为何与 ADELIE/GoLLIE 的公平对比不可行（不同 schema format、不同 evaluation protocol）。\n\n**SF3 [Major]: WikiEvents n=20 结论呈现过度自信。**\nMDE=±5.0pp（Table 31），n=20 下 fine-tuning composability 结论几乎无法可靠。Introduction contribution list \"validates event extraction applicability\" 过度推销。\n**R1-W3 (Major) + R2-W5 (Minor) 共识**。\n→ 建议：(1) §5.4 大幅缩减，标题改为 \"Preliminary Event Extraction Pilot\"；(2) Table 4 caption 注明 \"n=20, MDE=5.0pp, results are directional only\"；(3) Introduction 贡献列表降低 WikiEvents 措辞。\n\n**SF4 [Major]: 70B 实验全在 AWQ INT4 上，Abstract 未标注。**\nAbstract \"with 70B-class validation\" 让读者以为 70B 验证是 solid 的。DocRED E-F1 drop -7.07（INT4: 84.87 vs FP16: 91.94）源于 parse failure。量化限制 caveat 出现在 §5.3 最后一段，过晚。\n**R1-W4 (Major)，R2 AGREE 但降低严重性**（8B 消融已确认 INT4 不影响 DR）。\n→ 建议：(1) Abstract 标注 \"70B (AWQ INT4)\"；(2) §5.3 开头说明量化限制。\n\n**SF5 [Major]: Zero-shot 实验占主文 ~3 页但 R-F1 仅 4-8%，篇幅分配失衡。**\nFine-tuning composability（Table 2）仅获约 1 页篇幅，是真正有实用价值的结果。\n**分歧点**：R2-W3 认为 zero-shot 缺乏实用价值应大幅压缩；R1 REBUT 认为 zero-shot 作为 diagnostic probe 有独立科学价值（消融隔离约束效果、latent violation surfacing 仅在 ZS 下可观察）。**Director 判定**：两者均有道理。保留 zero-shot 的 diagnostic 定位和 Table 1 消融，但压缩篇幅（~1 段+1 表），释放空间给 fine-tuning per-relation 分析。\n\n### Nice to Have（不影响接收决策）\n\n**NF1 [Minor]: Proposition 1 unbounded vs bounded 论证之间逻辑跳跃。**\nRemark（§3）已区分理论不可能性和工程不可行性，但作为 Remark 不够 prominent。R1 评为 Major，R2 REBUT 评为 Minor。**Director 判定**：Minor——提升 Remark 为正式段落即可。\n\n**NF2 [Minor]: \"Empirical enabling dependency\" 重复 ≥6 次。**\n建议保留 3 次（Abstract、§3 定义、§5.1 引用），释放 ~0.3 页空间。[R2-W7, R1 AGREE]\n\n**NF3 [Minor]: Fallback 频率模型依赖性（Qwen 0 vs Llama 5882）未在正文讨论。**\n影响框架通用性声称。[R1-W6, R2 AGREE]\n\n**NF4 [Minor]: Continuation masking prefix collision 频率未量化。**\n建议附录增加 prefix collision 频率分析。[R1-W7, R2 AGREE]\n\n**NF5 [Minor]: Beam k=2 中间值缺失。**\nk=1 → k=4 跳跃太大，k=2 可能以更低延迟消除大部分 violations。[R2-Q3, R1 AGREE]\n\n**NF6 [Minor]: Entity registry first-seen type 行为主文解释不清。**\nCF 主要来源于 first-seen 注册机制，§3.3 应更显式 formalize。Entity-first 生成顺序是架构约束，应在 Limitations 中明确。[R2-Q4, R1-Q4 共识]\n\n**NF7 [Minor]: Limitations 可适度精简。**\nR2 认为 ~1.5 页接近 \"excessive\"，R1 REBUT 认为内容 substantive。**Director 判定**：有 10-15% 压缩空间，将具体数字分解移至 appendix。\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 达成 [AGREE]：\n1. CF 违规是核心未解决缺陷，正文必须量化讨论 [R1-W1 + R2-W2]\n2. WikiEvents n=20 统计效力不足，不应作为可靠结论 [R1-W3 + R2-W5]\n3. GoLLIE 对比不公平，训练基方法对比缺失或 misleading [R1-W5 + R2-W4]\n4. 70B INT4 披露不足 [R1-W4 + R2 AGREE]\n5. Enabling dependency 重复过多 [R2-W7 + R1 AGREE]\n6. Fallback 模型依赖性值得正文讨论 [R1-W6 + R2 AGREE]\n7. Prefix collision 未量化 [R1-W7 + R2 AGREE]\n8. Beam k=2 缺失 [R2-Q3 + R1 AGREE]\n9. Entity registry first-seen 行为需更清晰解释 [R2-Q4 + R1-Q4]\n\n---\n\n## Reviewer Divergence\n\n| Issue | R1 | R2 | Director 判定 |\n|-------|----|----|--------------|\n| CF → 改标题？ | 建议改为 \"Domain/Range-Constrained\" | 界定范围即可，不改标题 | 不强制改标题，但 Abstract/§1 必须界定 \"type-constrained\" 覆盖范围 |\n| Proposition 1 gap | Major | Minor (Remark 已区分) | Minor：提升 Remark prominence |\n| 训练基方法对比 | Major: 需补实验 | Minor: 互补定位合理 | Should Fix：至少解释为何直接对比不可行 |\n| Zero-shot 篇幅 | 有 diagnostic 价值保留 | 缺乏实用价值应压缩 | 折中：保留 Table 1 + 1 段，释放空间给 FT |\n| Limitations 长度 | Substantive，不需删 | 接近 excessive | 10-15% 精简空间 |\n\n---\n\n## Questions（需要作者澄清）\n\n**Q1** [R1-Q1]: Grammar-first fallback 放弃类型约束，是否考虑过 backtracking 替代策略？Latency cost 估算？\n\n**Q2** [R2-Q1]: 约束引入的 false negatives 对 recall 的影响——被约束阻断的合法三元组（从未生成的部分）是否被量化？0.49% downstream impact 仅衡量被后验移除的部分。\n\n**Q3** [R2-Q2]: DocRED grammar-only 增加 DR（18.46%→26.17% \"latent violation surfacing\"）。Fine-tuning 后是否持续？Grammar layer 在复杂 schema 下是否可能 over-constrain？\n\n**Q4** [R1-Q3]: Ontology scalability 测试最大到 1000 entity types。Real-world KG（Wikidata 10,000+ properties）下的编译时间和 runtime overhead 估算？\n\n**Q5** [R1-Q5]: Cohen's d 从 pooled bootstrap SD 计算，与传统 Cohen's d（样本 SD）的区别及理由？\n\n---\n\n## Missing References\n\n两位 Reviewer 均认为相关工作覆盖**充分**（R2-S4 明确肯定）。非关键性建议：\n- PARSE (Suri et al., 2025): LLM-driven schema optimization，与 schema compilation 相关\n- GenIE (Josifoski et al., 2022): 已引用但 §6 可更详细讨论其 constraint enforcement 机制\n- TANL (Paolini et al., 2021): 已引用（R2 指出 R1 遗漏检查）\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n未请求（项目未配置 external_review）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**: ✅ 完成（2026-05-23 08:20–08:24 UTC）\n\n**Findings (3 warnings, 19 info)**:\n- ⚠️ Page 4-5：连续两页纯文本（Method §3.1-3.4 + §4），缺少 illustrative figure\n- ⚠️ Page 8-9：连续两页纯文本（§6 + §7 + Limitations），Limitations 占满整页，内容偏多\n- ⚠️ Page 39：最后一页 Appendix Q 后有 ~40% 空白\n- ℹ️ 主文 8 页含 1 figure + 4 tables = 5 个 display items（密度 0.625/页，偏低端但可接受）\n- ℹ️ Appendix 极其丰富（27 页，~45+ tables + 4 figures），主文/附录比约 1:3\n- ℹ️ 全文无 margin 溢出、LaTeX 渲染错误、公式乱码，排版专业\n- ℹ️ Table 36 色盲友好设计（shape markers + color）\n- ℹ️ References 3.5 页，格式统一，无未解析引用\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.5 (Borderline Conference)**\n\n**置信度**: 4/5（两位 Reviewer 均为该领域活跃研究者，逐节验证了技术细节）\n\n**评分理由**:\n\n论文的工程执行和评估深度是显著优势——39 页附录、bootstrap CI + Cohen's d + MDE 报告、五路消融、三种 tokenizer 族跨模型验证，统计规范性显著优于 IE 领域平均水平。系统设计实用（+10% 延迟、<0.5s 编译、tokenizer 无关），enabling dependency 是有价值的经验发现。\n\n阻碍 Conference (4.0) 评分的核心问题：\n\n1. **CF gap 是根本性的**：系统将 DR violations 转化为 CF violations，后者占残余违规的 64%。\"Type-Constrained IE\" 标题与实际能力之间存在 gap。仅 beam search 完全解决，greedy 部署层不完整。\n2. **Novelty ceiling**：核心贡献是 XGrammar + stateful logits processor 的系统集成。Proposition 1 结论对形式语言理论研究者来说不意外。在 EMNLP 审稿中 novelty 是重要维度。\n3. **评估完整性存在盲区**：WikiEvents n=20 统计效力不足但结论呈现过度自信；70B 全在 INT4 上但 Abstract 未标注；GoLLIE 对比不公平。\n\n**如果作者在 revision 中**：\n(a) 在正文显著讨论 CF gap 并在 Abstract/§1 界定 \"type-constrained\" 范围；\n(b) 修正 WikiEvents/70B 的结论 scope；\n(c) 修正 GoLLIE 对比或解释为何公平对比不可行；\n(d) 压缩 zero-shot 篇幅，扩展 fine-tuning 分析——\n评分可提升至 **4.0 (Conference)**。当前状态介于 Conference 和 Findings 之间。\n\n---\n\n## Detailed Comments\n\n### Abstract\n- 信息密度高但准确。CF 分层报告（FT ≤1.4%, ZS up to 12%）较前版本有改善\n- 建议标注 \"70B (AWQ INT4)\"\n- \"empirical enabling dependency\" 术语可能对非专业读者不够直觉\n\n### §1 Introduction\n- Motivation 论证链完整（违规率 → 现有方法不足 → OntoCoDec）\n- Contribution list 过长（两个条目各含 4-5 个子句），建议拆分为更短要点\n- WikiEvents 贡献措辞需降级\n\n### §3 Method\n- 三级可判定性分类是有用的 conceptual framework\n- Proposition 1 proof sketch 应更清楚标注为 informal argument\n- Semantic layer 设计（§3.3）解释清晰，running example 有助理解\n- Remark（有限集合）需提升 prominence\n\n### §4 Constraint Composition\n- Grammar-first fallback 有充分工程动机\n- κ 在 n=3 下应明确标注 \"descriptive only, not statistically significant\"\n- Non-rectangularity 分析可考虑移至 appendix\n\n### §5 Experiments\n- Table 1 五路消融是论文最强部分\n- Zero-shot 篇幅过大，fine-tuning composability 篇幅不足\n- §5.3 的 \"beam (k=1) eliminates all violations\" 中 k=1 就是 greedy，不算 beam search\n- §5.4 WikiEvents 需标注 preliminary\n- Fallback 频率模型依赖性应在正文提及\n\n### §6 Related Work\n- 覆盖充分（R2-S4 明确肯定）\n- GoLLIE 引用需修正措辞\n\n### §7 Discussion and Conclusion\n- 简短恰当。Future direction（global entity-level type consensus）直接针对 CF\n\n### Limitations\n- 内容 substantive 但可精简 10-15%\n- 应量化 CF gap 的 64% 数字\n- Entity-first 生成顺序作为架构约束应明确说明\n\n### Format Compliance\n- ✅ 正文 8 页\n- ✅ 匿名：\"Anonymous ACL submission\"\n- ✅ `\\usepackage[review]{acl}`\n- ✅ Limitations 在正文中\n- ✅ Ethics Statement 存在\n- ✅ 引用格式正确（natbib）\n- ✅ 无 TODO/TBD/placeholder\n- ✅ 无匿名违规",
  "project": "schema_semantic_constrained_ie",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.5 (Borderline Conference)",
  "review_chat_id": "oc_01fc90ae186a4ed432770f7601995139"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# Round 23 审稿报告 — OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints\n\n**目标 Venue**: EMNLP 2026 (via ACL Rolling Review)  \n**类别**: Long Paper  \n**审稿模式**: Fresh（无上轮记忆）  \n**Reviewer 配置**: 2 人（R1: 方法严谨性+实验设计; R2: 新颖性+完整性+写作质量）  \n**交叉分享**: 完成（R1↔R2 逐条回应）  \n**轮次**: 1 轮收敛（核心问题达成共识，无需 Round 2）\n\n---\n\n## Summary\n\n本文提出 OntoCoDec，将 IE 本体编译为两层可组合 token 级解码约束：grammar layer（基于 XGrammar 的 CFG，强制 JSON 结构和词汇成员关系）和 semantic layer（有状态 logits 处理器，通过动态 entity registry 强制 domain/range 类型约束）。论文在 SciERC、DocRED、WikiEvents 上评估了 Qwen3-8B、Llama-3.1-8B、Mistral-7B 及 Llama-3.1-70B (AWQ INT4)，提供了五路消融、bootstrap CI + Cohen's d、beam search 兼容性验证等极其详尽的实验分析。LoRA 微调 + greedy S1 近乎消除 domain/range 违规（DR<0.1%），beam search (k=4) 消除所有违规类型（1.54× 延迟）。\n\n---\n\n## Strengths\n\n**S1: 评估深度在 IE 领域极为罕见。** 39 页附录覆盖五路消融（Table 1）、bootstrap CI + Cohen's d（Appendix C）、fallback 因果追踪（Table 6-7）、cross-field 违规分解（Table 9）、document 长度分箱分析（Appendix H）、prompt 敏感性（Appendix I）、TCR post-hoc resolution（Appendix M）、beam search 兼容性（Appendix F）、8B FP16 vs INT4 消融（Appendix P）。统计报告采用 document-level bootstrap resampling（10,000 iterations），报告 MDE，诚实承认 n=6 不足以进行相关性统计推断。[R1-S3/S4, R2-S1 共识]\n\n**S2: 方法形式化严密。** Proposition 1 的 pumping lemma 论证结构正确，完整证明（Appendix O）严格。约束可判定性三级分类（context-free → prefix-decidable with state → non-local）概念清晰，精准界定了 CFG 的能力边界。Grammar-first fallback（§4, eq.2）在 soundness 和 availability 之间取得了合理平衡。[R1-S1/S2, R2 acknowledges]\n\n**S3: 诚实透明的呈现方式。** 论文明确承认 DR enforcement 引入 CF 违规、zero-shot 质量低、WikiEvents 结果是 preliminary 的。Limitations 部分极为详细，覆盖约束范围、评估覆盖度、工程局限。[R2-S2]\n\n**S4: 实用的系统设计 + Tokenizer 无关的跨模型泛化。** 延迟开销适度（greedy +10%，beam 1.54×），编译速度快（<0.5s），可扩展性测试显示 200 实体类型/1000 关系时保持恒定 2-3% 开销。Continuation masking 在三种 tokenizer 族（byte-level BPE: Qwen/Llama, SentencePiece: Mistral）上验证有效。[R1-S6, R2-S3/S5]\n\n**S5: Enabling dependency 是有价值的经验发现。** Grammar alone 84% DR at 8B vs semantic-only 24%（Table 1），但 70B 时 grammar alone 接近 semantic layer 的水平（§5.3）。Scale-dependent 特性对约束解码系统设计有指导价值。[R1-S5]\n\n---\n\n## Weaknesses\n\n### Must Fix（阻碍接收）\n\n**MF1 [Critical]: CF 违规占残余违规 64%，与标题 \"Type-Constrained IE\" 形成 gap，正文讨论严重不足。**\nTable 9（Appendix）显示 S1 配置下 SciERC 245 个残余违规中 CF=155（63.9%），集中在 GENERIC↔OtherScientificTerm（34.7%）和 GENERIC↔Material（12.3%）。系统消除了 DR violations 但引入了 CF violations 作为新的 dominant 问题。正文 §4 仅一句 \"Level 3 is addressed by beam search or post-hoc resolution\" 带过，64% 这个关键数字仅在附录出现。Greedy 部署层成为不完整方案，用户必须在\"容忍 CF\"和\"支付 beam 延迟\"之间选择——这个 trade-off 在 Abstract/Introduction 中被低估。\n**两位 Reviewer 共识**（R1-W1 Critical + R2-W2 Major）。分歧仅在标题是否需要修改（R1 建议改为 \"Domain/Range-Constrained\"；R2 建议界定 \"type-constrained\" 范围即可）。\n→ 建议：(1) §5.1 或 §4 量化 CF 占残余违规比例；(2) 讨论 CF 从架构上为何难以在单 pass 解码中解决；(3) Abstract/Introduction 诚实呈现 greedy vs beam 的 trade-off。\n\n### Should Fix（显著影响评分）\n\n**SF1 [Major]: 算法创新有限，主要是系统集成贡献。**\nProposition 1 结论对了解 PDA 局限性的研究者来说不意外。XGrammar + stateful logits processor 的组合是自然的设计选择。κ 在 n=3 下 p=0.138 统计不显著。论文自我定位为 \"systematic engineering contribution\" 是诚实的，但在 EMNLP 审稿中 novelty 仍是重要维度。\n**R2-W1 (Major)，R1 交叉 AGREE 但 nuance**：enabling dependency 和三级分类有独立价值，定位为 \"strong engineering contribution with useful empirical insights\" 在 EMNLP 可接受，但应降低理论贡献措辞强度。\n→ 建议：降低 Proposition 1 和 κ 的呈现强度，突出 enabling dependency 的实证价值和系统可复用性。\n\n**SF2 [Major]: GoLLIE 对比不公平 + 缺少与训练基方法的系统性对比。**\nAppendix Q 比较 GoLLIE-7B zero-shot（R-F1=0.0, 5 predictions）vs OntoCoDec LoRA fine-tuned——evaluation setup 不匹配。§6 主文引用该结果可能误导读者。论文定位 training-based 和 decoding-time 方法为互补，但现有对比反而是 misleading 的。\n**R1-W5 (Major) + R2-W4 (Minor) 共识**。R2 REBUT 指出互补定位使直接对比 methodologically difficult，但同意需说明原因。\n→ 建议：(1) §6 修正 GoLLIE 引用措辞，明确标注 setup 差异；(2) 解释为何与 ADELIE/GoLLIE 的公平对比不可行（不同 schema format、不同 evaluation protocol）。\n\n**SF3 [Major]: WikiEvents n=20 结论呈现过度自信。**\nMDE=±5.0pp（Table 31），n=20 下 fine-tuning composability 结论几乎无法可靠。Introduction contribution list \"validates event extraction applicability\" 过度推销。\n**R1-W3 (Major) + R2-W5 (Minor) 共识**。\n→ 建议：(1) §5.4 大幅缩减，标题改为 \"Preliminary Event Extraction Pilot\"；(2) Table 4 caption 注明 \"n=20, MDE=5.0pp, results are directional only\"；(3) Introduction 贡献列表降低 WikiEvents 措辞。\n\n**SF4 [Major]: 70B 实验全在 AWQ INT4 上，Abstract 未标注。**\nAbstract \"with 70B-class validation\" 让读者以为 70B 验证是 solid 的。DocRED E-F1 drop -7.07（INT4: 84.87 vs FP16: 91.94）源于 parse failure。量化限制 caveat 出现在 §5.3 最后一段，过晚。\n**R1-W4 (Major)，R2 AGREE 但降低严重性**（8B 消融已确认 INT4 不影响 DR）。\n→ 建议：(1) Abstract 标注 \"70B (AWQ INT4)\"；(2) §5.3 开头说明量化限制。\n\n**SF5 [Major]: Zero-shot 实验占主文 ~3 页但 R-F1 仅 4-8%，篇幅分配失衡。**\nFine-tuning composability（Table 2）仅获约 1 页篇幅，是真正有实用价值的结果。\n**分歧点**：R2-W3 认为 zero-shot 缺乏实用价值应大幅压缩；R1 REBUT 认为 zero-shot 作为 diagnostic probe 有独立科学价值（消融隔离约束效果、latent violation surfacing 仅在 ZS 下可观察）。**Director 判定**：两者均有道理。保留 zero-shot 的 diagnostic 定位和 Table 1 消融，但压缩篇幅（~1 段+1 表），释放空间给 fine-tuning per-relation 分析。\n\n### Nice to Have（不影响接收决策）\n\n**NF1 [Minor]: Proposition 1 unbounded vs bounded 论证之间逻辑跳跃。**\nRemark（§3）已区分理论不可能性和工程不可行性，但作为 Remark 不够 prominent。R1 评为 Major，R2 REBUT 评为 Minor。**Director 判定**：Minor——提升 Remark 为正式段落即可。\n\n**NF2 [Minor]: \"Empirical enabling dependency\" 重复 ≥6 次。**\n建议保留 3 次（Abstract、§3 定义、§5.1 引用），释放 ~0.3 页空间。[R2-W7, R1 AGREE]\n\n**NF3 [Minor]: Fallback 频率模型依赖性（Qwen 0 vs Llama 5882）未在正文讨论。**\n影响框架通用性声称。[R1-W6, R2 AGREE]\n\n**NF4 [Minor]: Continuation masking prefix collision 频率未量化。**\n建议附录增加 prefix collision 频率分析。[R1-W7, R2 AGREE]\n\n**NF5 [Minor]: Beam k=2 中间值缺失。**\nk=1 → k=4 跳跃太大，k=2 可能以更低延迟消除大部分 violations。[R2-Q3, R1 AGREE]\n\n**NF6 [Minor]: Entity registry first-seen type 行为主文解释不清。**\nCF 主要来源于 first-seen 注册机制，§3.3 应更显式 formalize。Entity-first 生成顺序是架构约束，应在 Limitations 中明确。[R2-Q4, R1-Q4 共识]\n\n**NF7 [Minor]: Limitations 可适度精简。**\nR2 认为 ~1.5 页接近 \"excessive\"，R1 REBUT 认为内容 substantive。**Director 判定**：有 10-15% 压缩空间，将具体数字分解移至 appendix。\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 达成 [AGREE]：\n1. CF 违规是核心未解决缺陷，正文必须量化讨论 [R1-W1 + R2-W2]\n2. WikiEvents n=20 统计效力不足，不应作为可靠结论 [R1-W3 + R2-W5]\n3. GoLLIE 对比不公平，训练基方法对比缺失或 misleading [R1-W5 + R2-W4]\n4. 70B INT4 披露不足 [R1-W4 + R2 AGREE]\n5. Enabling dependency 重复过多 [R2-W7 + R1 AGREE]\n6. Fallback 模型依赖性值得正文讨论 [R1-W6 + R2 AGREE]\n7. Prefix collision 未量化 [R1-W7 + R2 AGREE]\n8. Beam k=2 缺失 [R2-Q3 + R1 AGREE]\n9. Entity registry first-seen 行为需更清晰解释 [R2-Q4 + R1-Q4]\n\n---\n\n## Reviewer Divergence\n\n| Issue | R1 | R2 | Director 判定 |\n|-------|----|----|--------------|\n| CF → 改标题？ | 建议改为 \"Domain/Range-Constrained\" | 界定范围即可，不改标题 | 不强制改标题，但 Abstract/§1 必须界定 \"type-constrained\" 覆盖范围 |\n| Proposition 1 gap | Major | Minor (Remark 已区分) | Minor：提升 Remark prominence |\n| 训练基方法对比 | Major: 需补实验 | Minor: 互补定位合理 | Should Fix：至少解释为何直接对比不可行 |\n| Zero-shot 篇幅 | 有 diagnostic 价值保留 | 缺乏实用价值应压缩 | 折中：保留 Table 1 + 1 段，释放空间给 FT |\n| Limitations 长度 | Substantive，不需删 | 接近 excessive | 10-15% 精简空间 |\n\n---\n\n## Questions（需要作者澄清）\n\n**Q1** [R1-Q1]: Grammar-first fallback 放弃类型约束，是否考虑过 backtracking 替代策略？Latency cost 估算？\n\n**Q2** [R2-Q1]: 约束引入的 false negatives 对 recall 的影响——被约束阻断的合法三元组（从未生成的部分）是否被量化？0.49% downstream impact 仅衡量被后验移除的部分。\n\n**Q3** [R2-Q2]: DocRED grammar-only 增加 DR（18.46%→26.17% \"latent violation surfacing\"）。Fine-tuning 后是否持续？Grammar layer 在复杂 schema 下是否可能 over-constrain？\n\n**Q4** [R1-Q3]: Ontology scalability 测试最大到 1000 entity types。Real-world KG（Wikidata 10,000+ properties）下的编译时间和 runtime overhead 估算？\n\n**Q5** [R1-Q5]: Cohen's d 从 pooled bootstrap SD 计算，与传统 Cohen's d（样本 SD）的区别及理由？\n\n---\n\n## Missing References\n\n两位 Reviewer 均认为相关工作覆盖**充分**（R2-S4 明确肯定）。非关键性建议：\n- PARSE (Suri et al., 2025): LLM-driven schema optimization，与 schema compilation 相关\n- GenIE (Josifoski et al., 2022): 已引用但 §6 可更详细讨论其 constraint enforcement 机制\n- TANL (Paolini et al., 2021): 已引用（R2 指出 R1 遗漏检查）\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n未请求（项目未配置 external_review）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**: ✅ 完成（2026-05-23 08:20–08:24 UTC）\n\n**Findings (3 warnings, 19 info)**:\n- ⚠️ Page 4-5：连续两页纯文本（Method §3.1-3.4 + §4），缺少 illustrative figure\n- ⚠️ Page 8-9：连续两页纯文本（§6 + §7 + Limitations），Limitations 占满整页，内容偏多\n- ⚠️ Page 39：最后一页 Appendix Q 后有 ~40% 空白\n- ℹ️ 主文 8 页含 1 figure + 4 tables = 5 个 display items（密度 0.625/页，偏低端但可接受）\n- ℹ️ Appendix 极其丰富（27 页，~45+ tables + 4 figures），主文/附录比约 1:3\n- ℹ️ 全文无 margin 溢出、LaTeX 渲染错误、公式乱码，排版专业\n- ℹ️ Table 36 色盲友好设计（shape markers + color）\n- ℹ️ References 3.5 页，格式统一，无未解析引用\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.5 (Borderline Conference)**\n\n**置信度**: 4/5（两位 Reviewer 均为该领域活跃研究者，逐节验证了技术细节）\n\n**评分理由**:\n\n论文的工程执行和评估深度是显著优势——39 页附录、bootstrap CI + Cohen's d + MDE 报告、五路消融、三种 tokenizer 族跨模型验证，统计规范性显著优于 IE 领域平均水平。系统设计实用（+10% 延迟、<0.5s 编译、tokenizer 无关），enabling dependency 是有价值的经验发现。\n\n阻碍 Conference (4.0) 评分的核心问题：\n\n1. **CF gap 是根本性的**：系统将 DR violations 转化为 CF violations，后者占残余违规的 64%。\"Type-Constrained IE\" 标题与实际能力之间存在 gap。仅 beam search 完全解决，greedy 部署层不完整。\n2. **Novelty ceiling**：核心贡献是 XGrammar + stateful logits processor 的系统集成。Proposition 1 结论对形式语言理论研究者来说不意外。在 EMNLP 审稿中 novelty 是重要维度。\n3. **评估完整性存在盲区**：WikiEvents n=20 统计效力不足但结论呈现过度自信；70B 全在 INT4 上但 Abstract 未标注；GoLLIE 对比不公平。\n\n**如果作者在 revision 中**：\n(a) 在正文显著讨论 CF gap 并在 Abstract/§1 界定 \"type-constrained\" 范围；\n(b) 修正 WikiEvents/70B 的结论 scope；\n(c) 修正 GoLLIE 对比或解释为何公平对比不可行；\n(d) 压缩 zero-shot 篇幅，扩展 fine-tuning 分析——\n评分可提升至 **4.0 (Conference)**。当前状态介于 Conference 和 Findings 之间。\n\n---\n\n## Detailed Comments\n\n### Abstract\n- 信息密度高但准确。CF 分层报告（FT ≤1.4%, ZS up to 12%）较前版本有改善\n- 建议标注 \"70B (AWQ INT4)\"\n- \"empirical enabling dependency\" 术语可能对非专业读者不够直觉\n\n### §1 Introduction\n- Motivation 论证链完整（违规率 → 现有方法不足 → OntoCoDec）\n- Contribution list 过长（两个条目各含 4-5 个子句），建议拆分为更短要点\n- WikiEvents 贡献措辞需降级\n\n### §3 Method\n- 三级可判定性分类是有用的 conceptual framework\n- Proposition 1 proof sketch 应更清楚标注为 informal argument\n- Semantic layer 设计（§3.3）解释清晰，running example 有助理解\n- Remark（有限集合）需提升 prominence\n\n### §4 Constraint Composition\n- Grammar-first fallback 有充分工程动机\n- κ 在 n=3 下应明确标注 \"descriptive only, not statistically significant\"\n- Non-rectangularity 分析可考虑移至 appendix\n\n### §5 Experiments\n- Table 1 五路消融是论文最强部分\n- Zero-shot 篇幅过大，fine-tuning composability 篇幅不足\n- §5.3 的 \"beam (k=1) eliminates all violations\" 中 k=1 就是 greedy，不算 beam search\n- §5.4 WikiEvents 需标注 preliminary\n- Fallback 频率模型依赖性应在正文提及\n\n### §6 Related Work\n- 覆盖充分（R2-S4 明确肯定）\n- GoLLIE 引用需修正措辞\n\n### §7 Discussion and Conclusion\n- 简短恰当。Future direction（global entity-level type consensus）直接针对 CF\n\n### Limitations\n- 内容 substantive 但可精简 10-15%\n- 应量化 CF gap 的 64% 数字\n- Entity-first 生成顺序作为架构约束应明确说明\n\n### Format Compliance\n- ✅ 正文 8 页\n- ✅ 匿名：\"Anonymous ACL submission\"\n- ✅ `\\usepackage[review]{acl}`\n- ✅ Limitations 在正文中\n- ✅ Ethics Statement 存在\n- ✅ 引用格式正确（natbib）\n- ✅ 无 TODO/TBD/placeholder\n- ✅ 无匿名违规",
    "project": "schema_semantic_constrained_ie",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.5 (Borderline Conference)",
    "review_chat_id": "oc_01fc90ae186a4ed432770f7601995139"
  }
}
```

</details>

---


### Tool result

_source line 2357 · 2026-05-23T08:40:24.673879+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_2216d5b8b87a9472ce204aba11481390:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4532
}
```

</details>

---


### Tool call

_source line 2358 · 2026-05-23T08:40:35.382318+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0-3: 初始化到收敛判断', 'status': 'completed', 'activeForm': '已完成'}, {'content': 'Step 4a: 检查视觉审查状态', 'status': 'completed', 'activeForm': '检查视觉审查状态'}, {'content': 'Step 4b: 同步 Issue Tracker', 'status': 'completed', 'activeForm': '同步 review_issues.yaml'}, {'content': 'Step 4c: 合成报告并投递', 'status': 'completed', 'activeForm': '合成并投递审稿报告'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Step 0-3: 初始化到收敛判断', 'status': 'completed', 'activeForm': '已完成'}, {'content': 'Step 4a: 检查视觉审查状态', 'status': 'completed', 'activeForm': '检查视觉审查状态'}, {'content': 'Step 4b: 同步 Issue Tracker', 'status': 'completed', 'activeForm': '同步 review_issues.yaml'}, {'content': 'Step 4c: 合成报告并投递', 'status': 'completed', 'activeForm': '合成并投递审稿报告'}]"
  }
}
```

</details>

---


### Tool result

_source line 2359 · 2026-05-23T08:40:35.483387+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "TodoWrite",
  "elapsed_ms": 101
}
```

</details>

---


### Assistant

_source line 2360 · 2026-05-23T08:40:48.526331+00:00_

**Round 23 审稿完成，报告已投递至 Research Director。**

**审稿结果摘要：**
- **Overall: 3.5 (Borderline Conference)**，两位 Reviewer 评分一致，置信度 4/5
- **1 轮收敛**，核心问题达成共识无需 Round 2

**关键发现：**
- **Must Fix (1)**：CF 违规占残余 64%，与 "Type-Constrained IE" 标题形成 gap，正文讨论严重不足
- **Should Fix (5)**：算法创新有限（系统集成）、GoLLIE 对比不公平、WikiEvents n=20 过度推销、70B INT4 未标注、zero-shot 篇幅过大
- **Nice to Have (7)**：Prop 1 prominence、重复表述、fallback 模型依赖性、prefix collision、beam k=2、entity registry 解释、Limitations 精简

**提升路径**：修正 CF gap 讨论 + WikiEvents/70B scope + GoLLIE 对比 + 压缩 ZS 篇幅 → 可从 3.5 提升至 4.0 (Conference)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director"
}
```

</details>

---


## Round 171

## Round 171

2 recorded events


### User

_source line 2361 · 2026-05-23T08:40:49.607475+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交给 Review Director。

核心结论：与R2在三个关键问题上高度一致（CF violations未解决、WikiEvents统计效力不足、GoLLIE对比不公平），两位Reviewer均给出3.5分。

主要分歧两点：
1. **Zero-shot实验价值**（R2-W3）：我反驳了R2"缺乏实用价值"的判断——zero-shot作为isolating约束机制的diagnostic设置有独立科学价值（Table 1消融、surfacing效应），但同意篇幅分配应向fine-tuning倾斜。
2. **Limitations长度**（R2-W6）：我反驳了R2"接近excessive"的判断——内容是substantive limitations而非padding，CF gap数据反而应该出现在Limitations中。

---

[Reviewer 2 审稿结果]:
交叉回应已提交给 Review Director。

核心结论：R1 和 R2 在三个主要问题上达成共识——CF trade-off 正文讨论不足、WikiEvents n=20 统计效力不足、70B INT4 限制披露不够显著。两位 reviewer 均评 3.5 (Borderline Conference)。

主要分歧在四点：(1) 标题是否需要修改（R1 主张改，R2 认为界定范围即可）；(2) Proposition 1 的论证是否充分（R1 认为有 gap，R2 认为 Remark 已覆盖）；(3) 是否需要与训练基方法直接对比（R1 认为必要，R2 认为方法论上不合适）；(4) GenIE/TANL 是否缺失（R1 疏忽，两者已被引用）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 2362 · 2026-05-23T08:41:03.729353+00:00_

Round 23 审稿流程已全部完成。

**最终结果：3.5 (Borderline Conference)**

审稿报告已投递给 Research Director。核心发现：

**阻碍 Conference 的 3 个关键问题（两位 Reviewer 共识）：**
1. CF 违规占残余违规 64%，正文未量化讨论，与 "Type-Constrained IE" 标题形成 gap
2. WikiEvents n=20 / 70B INT4 的结论呈现过度自信
3. GoLLIE 对比不公平，缺少与训练基方法的公平对比或不可行性说明

**主要分歧（已在报告中标注 Director 判定）：**
- 标题是否需改 → 不强制，但必须界定范围
- Zero-shot 篇幅 → 保留 diagnostic 价值但压缩篇幅
- Proposition 1 gap → Minor，提升 Remark prominence 即可

Issue Tracker 已更新（12 个新 issue + 9 个历史 in_progress 状态更新），视觉审查结果已拼入报告。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director"
}
```

</details>

---


## Round 172

## Round 172

74 recorded events


### User

_source line 2363 · 2026-05-23T09:16:37.753850+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: schema_semantic_constrained_ie
- 论文路径: /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: Long Paper
- 截止日期: 2026-05-25
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 2364 · 2026-05-23T09:16:43.298847+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 2365 · 2026-05-23T09:16:43.354021+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "elapsed_ms": 55
}
```

</details>

---


### Tool call

_source line 2366 · 2026-05-23T09:16:50.686652+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 2367 · 2026-05-23T09:16:50.787577+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 2368 · 2026-05-23T09:16:55.111858+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "schema_semantic_constrained_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "schema_semantic_constrained_ie"
  }
}
```

</details>

---


### Tool result

_source line 2369 · 2026-05-23T09:16:57.017946+00:00_

{"result":"# 项目 schema_semantic_constrained_ie 概况\n\n## 实验状态 (164 个)\n\n- **llama_scierc_full_s1**: DONE (success) — \n- **llama_scierc_unconstrained**: DONE (success) — \n- **phase2_scierc_full_s1**: DONE (success) — \n- **phase2_scierc_semantic_only**: DONE (success) — \n- **phase2_scierc_grammar_only**: DONE (success) — \n- **phase2_scierc_unconstrained**: DONE (success) — \n- **phase2_docred_full_s1**: DONE (success) — \n- **phase2_docred_semantic_only**: DONE (success) — \n- **phase2_docred_unconstrained**: DONE (success) — \n- **mvp_phase0_docred_schema_r2**: DONE (killed) — \n- **phase2_s2_pilot50**: DONE (success) — \n- **mvp_phase0_docred_schema**: DONE (success) — \n- **mvp_phase0_violation_rate_docred**: DONE (success) — \n- **mvp_phase0_scierc_schema**: DONE (success) — \n- **mvp_phase0_violation_rate**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-23\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| sf2_70b_prompt_sensitivity | 70B LLaMA-3.1 constrained decoding should show consistent violation reduction across different prompt styles, similar to the 8B result where ΔDR was 94.0-94.6% regardless of prompt variant. | — | — | — |\n\n## 待处理\n- r16_70b_lora_scierc_eval: 70B AWQ INT4 LoRA fine-tuned on SciERC will achieve higher R-F1 than 8B FT (Qwen 47.15, Llama 46.13) and S1 constraints will maintain DR→0% at 70B scale（准备中）\n- p1_llama_ee_ft（准备中）\n\n## 近期结论\n- **eval_70b_lora_docred_200_full_s2** (negative): Full S2 (grammar+semantic+repair) on 70B LoRA DocRED should achieve near-zero DR while maintaining R_F1 close to beam4_s1 (48.14). The repair layer resolves residual DR violations from S1. This is the strongest constraint configuration for DocRED LoRA. ← 基于 eval_70b_lora_docred_200_beam4_s1\n- **sf2_qwen_int4_docred_s1** (success): AWQ INT4 quantization of fine-tuned Qwen3-8B does not significantly affect constraint enforcement or extraction quality on DocRED S1, mainta
…[truncated 1162 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1906
}
```

</details>

---


### Tool call

_source line 2370 · 2026-05-23T09:16:57.018459+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 2371 · 2026-05-23T09:16:57.822297+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{graphicx}
11	\usepackage{booktabs}
12	\usepackage{multirow}
13	\usepackage[table]{xcolor}
14	\usepackage{amsmath}
15	\usepackage{amssymb}
16	\usepackage{amsthm}
17	\usepackage{enumitem}
18	\usepackage{pifont}
19	\usepackage{soul}
20	\usepackage{tikz}
21	\usetikzlibrary{arrows.meta,positioning,shapes.geometric,fit,backgrounds,calc}
22	\newcommand{\TBD}[1]{\textcolor{red}{#1}}
23	
24	\title{OntoCoDec: Type-Constrained Information Extraction\\via Compiled Schema Constraints}
25	
26	\author{Anonymous ACL submission}
27	
28	\begin{document}
29	\maketitle
30	
31	% === Abstract ===
32	\input{abstract}
33	
34	% === §1 Introduction ===
35	\input{section1_introduction_draft}
36	
37	% === §2 Background ===
38	\input{section2_background}
39	
40	% === §3 Method ===
41	\input{section3_method_draft}
42	
43	% === §4 Constraint Composition ===
44	\section{Constraint Composition}
45	\label{sec:composition}
46	\input{section4_composition_draft}
47	
48	% === §5 Experiments ===
49	\section{Experiments}
50	\label{sec:experiments}
51	
52	\input{section3_violation_landscape}
53	
54	\input{section5_scierc_draft}
55	\input{section5_wikievents_draft}
56	\input{section5_runtime}
57	
58	% === §6 Related Work ===
59	\input{section6_related_work}
60	
61	% === §7 Discussion and Conclusion ===
62	\section{Discussion and Conclusion}
63	\label{sec:discussion}
64	\input{section7_conclusion_compressed}
65	
66	% === Limitations (ARR requirement: standalone section, does not count toward page limit) ===
67	\clearpage
68	\section*{Limitations}
69	
70	\paragraph{Constraint scope.}
71	CF is an architectural consequence of per-triple independent enforcement: CF$\leftrightarrow$DR represents a fundamental trade-off (eliminating CF re-routes violations to DR; Appendix~\ref{app:cf-dr-tradeoff}), and its impa
…[truncated 4263 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "elapsed_ms": 803
}
```

</details>

---


### Tool call

_source line 2372 · 2026-05-23T09:16:57.973869+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_local_file,WebSearch",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_local_file,WebSearch",
    "max_results": "2"
  }
}
```

</details>

---


### Tool result

_source line 2373 · 2026-05-23T09:16:57.974327+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2374 · 2026-05-23T09:17:05.675662+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
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

_source line 2375 · 2026-05-23T09:17:06.730457+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "schema_semantic_constrained_ie",
  "file": "paper_checklist.yaml",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "schema_semantic_constrained_ie",
    "file": "paper_checklist.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool call

_source line 2376 · 2026-05-23T09:17:08.739609+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
  "description": "Check if review_issues.yaml exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
    "description": "Check if review_issues.yaml exists"
  }
}
```

</details>

---


### Tool result

_source line 2377 · 2026-05-23T09:17:13.157494+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines ARR"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"*SEM 2026: Commitment Link for ARR-Reviewed Papers (Deadline: 10 April 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/sem-2026-commitment-link-arr-reviewed-papers-deadline-10-april-2026"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"5th Workshop on Evaluation and Comparison for NLP systems (Eval4NLP) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/5th-workshop-evaluation-and-comparison-nlp-systems-eval4nlp"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"}]

Based on the search results, here are the key submission guidelines for EMNLP 2026 papers, including information about ARR:

## Main Submission Guidelines

EMNLP 2026 invites the submission of long and short papers featuring substantial, original, and unpublished research on empirical methods for Natural Language Processing. Papers may contribute negative findings, survey an area, announce the creation of a new resource, argue a position, report novel linguistic insights derived using existing computational techniques, and reproduce (or fail to reproduce) previous results.

## ARR Integration Policy

Given that the ARR 2026 May cycle is aligned with two conferences (EMNLP and AACL), authors will need to explicitly declare which conference they intend to commit to at submission tim
…[truncated 749 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "WebSearch",
  "elapsed_ms": 7481
}
```

</details>

---


### Tool result

_source line 2378 · 2026-05-23T09:17:13.209882+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'schema_semantic_constrained_ie'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 6479
}
```

</details>

---


### Tool result

_source line 2379 · 2026-05-23T09:17:13.361325+00:00_

# Review Issues Tracker — schema_semantic_constrained_ie
# Updated: R23 Action Matrix dispatched, 2026-05-23

# ============================================================
# Round 23 — Issues with actions dispatched
# ============================================================

- id: "R23-W1"
  summary: "CF 违规占残余违规 64%，与标题 'Type-Constrained IE' 形成 gap，正文讨论不足"
  category: framing
  severity: critical
  status: in_progress
  first_raised_round: 23
  last_seen_round: 23
  mentions:
    - round: 23
      reviewers: [1, 2]
      note: "R1-W1 (Critical) + R2-W2 (Major)。两位共识：正文应量化 CF 比例、讨论架构限制。"
  action_items:
    - round: 23
      action: "§5.1 加 CF 量化段落(63.9%, GENERIC↔OtherScientificTerm 34.7%) + §4 加架构根因1句 + Abstract 加 trade-off"
      assigned_to: paper_agent
      status: completed
  resolution: ""
  resolution_round: null

- id: "R23-W2"
  summary: "算法创新有限——主要是 XGrammar + stateful logits processor 的系统集成"
  category: framing
  severity: warning
  status: in_progress
  first_raised_round: 23
  last_seen_round: 23
  mentions:
    - round: 23
      reviewers: [1, 2]
      note: "R2-W1 (Major)。共识：定位为 strong engineering contribution，降低理论贡献措辞强度。"
  action_items:
    - round: 23
      action: "降低 Proposition 1 呈现强度 + κ 加 descriptive only (n=3, p=0.138)"
      assigned_to: paper_agent
      status: completed
  resolution: ""
  resolution_round: null

- id: "R23-W3"
  summary: "GoLLIE 对比不公平 + 缺少与训练基方法的系统性对比"
  category: experiment
  severity: warning
  status: in_progress
  first_raised_round: 23
  last_seen_round: 23
  mentions:
    - round: 23
      reviewers: [1, 2]
      note: "R1-W5 (Major) + R2-W4 (Minor)。共识：至少解释为何直接对比不可行。"
  action_items:
    - round: 23
      action: "§6 GoLLIE 段重写：标注 setup 差异 + 解释不可比性(schema format差异, 无公开LoRA checkpoint)"
      assigned_to: paper_agent
      status: completed
  resolution: ""
  resolution_round: null

- id: "R23-W4"
  summary: "WikiEvents n=20 统计效力不足但结论呈现过度自信"
  category: experiment
  severity: warning
  status: in_progress
  first
…[truncated 9837 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Bash",
  "elapsed_ms": 4621
}
```

</details>

---


### Tool call

_source line 2380 · 2026-05-23T09:17:19.086117+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 ARR submission format page limit anonymity template guidelines"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 ARR submission format page limit anonymity template guidelines"
  }
}
```

</details>

---


### Tool call

_source line 2381 · 2026-05-23T09:17:21.245452+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/",
  "description": "List paper directory files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/",
    "description": "List paper directory files"
  }
}
```

</details>

---


### Tool result

_source line 2382 · 2026-05-23T09:17:21.296255+00:00_

_pdf_images
abstract.tex
abstract_d3264e.tex
abstract_fd4b26.tex
acl.sty
acl_natbib.bst
appendix_70b_ablation.tex
appendix_beam_search.tex
appendix_case_studies.tex
appendix_discussion.tex
appendix_doc_length.tex
appendix_downstream_analysis.tex
appendix_full_ft.tex
appendix_gollie_comparison.tex
appendix_high_kappa_analysis.tex
appendix_kappa_case_study.tex
appendix_llama_per_relation.tex
appendix_order_invariance.tex
appendix_power_analysis.tex
appendix_power_analysis_523cc9.tex
appendix_prompt_sensitivity.tex
appendix_prompts.tex
appendix_pumping_lemma.tex
appendix_quantization.tex
appendix_related_work.tex
appendix_reproducibility.tex
appendix_sampling_table.tex
appendix_scalability.tex
appendix_tcr.tex
appendix_type_consensus.tex.archived
appendix_zs_crossmodel.tex
case_study_kappa_dr.tex
checklist.tex
discussion_paragraphs.tex
discussion_paragraphs_cf83d1.tex
error_analysis_cases.json
fig1_framework.tex
figures
main.aux
main.bbl
main.blg
main.fdb_latexmk
main.fls
main.log
main.out
main.pdf
main.tex
new_citations.bib
ontocodec_paper_r10_final.pdf
ontocodec_paper_r9_final.pdf
p3_case_studies.tex
p3_case_studies_861a0d.tex
paper_tables_draft.tex
r12_fallback_cascade_text.txt
relwork_new_entries.bib
section1_introduction_draft.tex
section2_background.tex
section3_method_draft.tex
section3_violation_landscape.tex
section4_composition_draft.tex
section5_crossmodel_draft.tex
section5_docred_draft.tex
section5_docred_draft_9b84f1.tex
section5_runtime.tex
section5_scierc_draft.tex
section5_scierc_draft_4796e8.tex
section5_wikievents_draft.tex
section6_related_work.tex
section6_relwork_additions.tex
section6_relwork_outline.tex
section7_conclusion_550cbf_DEPRECATED.tex
section7_conclusion_DEPRECATED.tex
section7_conclusion_compressed.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 2383 · 2026-05-23T09:17:25.932932+00:00_

Web search results for query: "EMNLP 2026 ARR submission format page limit anonymity template guidelines"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"EMNLP 2026 LaTeX Template | ACL Style Files & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/emnlp"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Authors Guidelines","url":"http://aclrollingreview.org/authors"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"Submission Guide","url":"https://nlp4climate.github.io/submissionguide/"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"Authors Beware: Common Submission Problems","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Submissions | Transactions of the Association for Computational Linguistics","url":"https://transacl.org/index.php/tacl/about/submissions"}]

Based on the search results for EMNLP 2026 ARR submission guidelines, here's the key information:

## Page Limits

The format is two-column with an 8-page limit for long papers and a 4-page limit for short papers. The mandatory Limitations section is required, placed after the conclusion.

## Anonymity Requirements

Following the ACL and ARR policies, there is no anonymity period requirement. However, beginning with the February 15, 2024 ARR deadlines, there is no anonymity period or limitation on posting or discussing non-anonymous preprints while the work is under peer review. That said, the new policy incentivizes anonymous submissions by special paper awards and priority in acceptance decisions for borderline papers.

For submission itself, papers must not in
…[truncated 808 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "WebSearch",
  "elapsed_ms": 6846
}
```

</details>

---


### Tool call

_source line 2384 · 2026-05-23T09:17:34.229071+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 2385 · 2026-05-23T09:17:34.731386+00:00_

1	\begin{abstract}
2	Large language models for information extraction generate structurally valid but ontologically invalid triples---where entity types violate the ontology's domain/range constraints.
3	These violations persist across the capability spectrum and cannot be addressed by grammar-constrained decoding (which lacks cross-field type awareness) or post-hoc filtering (which discards valid predictions).
4	
5	We present \textsc{OntoCoDec}, a framework that compiles information extraction ontologies into composable token-level decoding constraints.
6	A decidability analysis shows that domain/range constraints exceed context-free expressiveness, yielding a two-layer architecture: a grammar layer enforces structural validity and vocabulary membership; a semantic layer enforces type constraints at runtime through stateful masking over a dynamic entity registry, with grammar-first fallback when constraints conflict.
7	
8	% exp_ids: w5_lora_scierc_constrained_eval, w5_qwen_docred_lora_constrained_eval, w5_llama_lora_scierc_constrained_eval, w5_llama_docred_lora_constrained_eval
9	Composed with LoRA fine-tuning across three 8B-class models and two relation extraction datasets (up to 96 relations), greedy S1 near-eliminates domain/range violations ($<$\,0.1\%) at F1 41--47\%, but introduces cross-field type inconsistencies ($\leq$1.4\%) as the dominant residual---an architectural consequence of per-triple independent enforcement.
10	Beam search ($k{=}4$) eliminates all violation types at 1.54$\times$ latency.
11	In zero-shot settings, cross-field rates are higher (up to 12\%) but decrease with model calibration.
12	Zero-shot domain/range reductions span 76--99\% on SciERC and 42--90\% on DocRED, with a scale-dependent empirical relationship between the two layers: the semantic layer alone achieves substantially stronger reduction at larger model scale.
13	\end{abstract}
14	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 2386 · 2026-05-23T09:17:34.731821+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section1_introduction_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section1_introduction_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 2387 · 2026-05-23T09:17:36.137870+00:00_

1	% Section 1: Introduction (compressed, 669→~550 words)
2	
3	\section{Introduction}
4	\label{sec:introduction}
5	
6	Large language models are increasingly used for information extraction~\cite{li2023codeie,sainz2024gollie,wei2023zeroshot}, but when generating relation triples $(h, r, t)$, neither entity necessarily carries a type consistent with the ontology's domain/range constraints for $r$.
7	We call such outputs \emph{domain/range violations}: structurally valid triples that are ontologically invalid.
8	Violations persist across the capability spectrum: 15.4\% of triples on SciERC~\cite{luan2018scierc} and 18.5\% on DocRED~\cite{yao2019docred} under zero-shot decoding, and 0.5--2\% even after LoRA fine-tuning; rates correlate with schema restrictiveness (few valid type pairs per relation) rather than ontology or model scale.
9	At competitive quality (R-F1 41--47\%), even 1--2\% residual violations compound across thousands of documents into systematic knowledge graph corruption, making reliable constraint enforcement necessary.
10	
11	Existing approaches leave a fundamental gap.
12	Schema-informed prompting reduces violations by 62\% on average but is per-relation unreliable (violations for \textsc{Evaluate-for} actually \emph{increase} by 5.8\,pp).
13	Grammar-constrained decoding~\cite{dong2025xgrammar,willard2023outlines,beurer-kellner2023lmql} ensures syntactic well-formedness but cannot encode cross-field semantic constraints.
14	Post-hoc filtering discards up to 48\% of predictions including true positives (Appendix~\ref{app:cross-model-zs}).
15	Training-based approaches~\cite{sainz2024gollie,lu2022uie} internalize schema knowledge but provide only soft guidance without runtime enforcement.
16	
17	We propose \textbf{OntoCoDec}, a framework that translates IE ontologies into composable layers of decoding-time constraints.
18	A decidability analysis of IE type constraints (\S\ref{sec:decidability}) yields a two-layer architecture: the \emph{grammar layer} co
…[truncated 2492 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "elapsed_ms": 1406
}
```

</details>

---


### Tool call

_source line 2388 · 2026-05-23T09:17:36.138251+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_method_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_method_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 2389 · 2026-05-23T09:17:36.339502+00:00_

1	% Section 3 — Method (Draft)
2	% OntoCoDec: Type-Valid Information Extraction
3	% via Compiled Ontology Constraints
4	
5	\section{Method}
6	\label{sec:method}
7	
8	\input{fig1_framework}
9	
10	We present OntoCoDec, a framework that translates IE ontologies into token-level constraints enforced during autoregressive generation.
11	The design is guided by a decidability analysis of IE type constraints.
12	
13	\paragraph{Constraint decidability taxonomy.}
14	\label{sec:decidability}
15	We classify IE type constraints into three levels: (1)~\emph{context-free}: vocabulary membership and JSON structure; (2)~\emph{prefix-decidable with state}: domain/range type validity, determined at each type-bearing position given the decoded relation type and entity registry; (3)~\emph{non-local}: cross-entity type consistency, which depends on the full output.
16	Unlike code generation where types are statically declared, IE constraints fall into level~2: entity types are inferred from text, the registry is built dynamically, and constraint targets depend on the co-occurring relation.
17	OntoCoDec enforces levels 1--2 (grammar and semantic layers, respectively); level~3 is addressed by beam search or post-hoc resolution (Appendix~\ref{app:tcr}).
18	
19	\smallskip
20	\noindent
21	Existing grammar-constrained decoding frameworks (e.g., XGrammar) enforce level~1 constraints---structural validity and vocabulary membership---but IE domain/range rules require cross-position entity-type state that context-free grammars cannot express.
22	We formalize this gap:
23	
24	\smallskip
25	\noindent\textbf{Proposition 1} (Level 2 $\not\subseteq$ Level 1)\textbf{.}
26	\textit{Domain/range type constraints for IE with unbounded entity sets are not context-free.}
27	
28	\smallskip
29	\noindent\textit{Proof sketch.}
30	Consider $\mathcal{E} = \{\tau_A, \tau_B\}$ and a relation $r$ with $\operatorname{dom}(r) = \{\tau_A\}$.
31	An output contains $n$ entities with independently chosen types, followed by
…[truncated 8034 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 2390 · 2026-05-23T09:17:36.340028+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "schema_semantic_constrained_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "schema_semantic_constrained_ie"
  }
}
```

</details>

---


### Tool result

_source line 2391 · 2026-05-23T09:17:36.791989+00:00_

{"result":"# 项目 schema_semantic_constrained_ie 概况\n\n## 实验状态 (164 个)\n\n- **llama_scierc_full_s1**: DONE (success) — \n- **llama_scierc_unconstrained**: DONE (success) — \n- **phase2_scierc_full_s1**: DONE (success) — \n- **phase2_scierc_semantic_only**: DONE (success) — \n- **phase2_scierc_grammar_only**: DONE (success) — \n- **phase2_scierc_unconstrained**: DONE (success) — \n- **phase2_docred_full_s1**: DONE (success) — \n- **phase2_docred_semantic_only**: DONE (success) — \n- **phase2_docred_unconstrained**: DONE (success) — \n- **mvp_phase0_docred_schema_r2**: DONE (killed) — \n- **phase2_s2_pilot50**: DONE (success) — \n- **mvp_phase0_docred_schema**: DONE (success) — \n- **mvp_phase0_violation_rate_docred**: DONE (success) — \n- **mvp_phase0_scierc_schema**: DONE (success) — \n- **mvp_phase0_violation_rate**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-23\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| sf2_70b_prompt_sensitivity | 70B LLaMA-3.1 constrained decoding should show consistent violation reduction across different prompt styles, similar to the 8B result where ΔDR was 94.0-94.6% regardless of prompt variant. | — | — | — |\n\n## 待处理\n- r16_70b_lora_scierc_eval: 70B AWQ INT4 LoRA fine-tuned on SciERC will achieve higher R-F1 than 8B FT (Qwen 47.15, Llama 46.13) and S1 constraints will maintain DR→0% at 70B scale（准备中）\n- p1_llama_ee_ft（准备中）\n\n## 近期结论\n- **eval_70b_lora_docred_200_full_s2** (negative): Full S2 (grammar+semantic+repair) on 70B LoRA DocRED should achieve near-zero DR while maintaining R_F1 close to beam4_s1 (48.14). The repair layer resolves residual DR violations from S1. This is the strongest constraint configuration for DocRED LoRA. ← 基于 eval_70b_lora_docred_200_beam4_s1\n- **sf2_qwen_int4_docred_s1** (success): AWQ INT4 quantization of fine-tuned Qwen3-8B does not significantly affect constraint enforcement or extraction quality on DocRED S1, mainta
…[truncated 1162 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 2392 · 2026-05-23T09:17:43.720281+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 2393 · 2026-05-23T09:17:43.721157+00:00_

1	% Section 5 — SciERC Results (Draft)
2	% Data source: Phase 2 SciERC registry experiments
3	% exp_ids: phase2_scierc_unconstrained, phase2_scierc_grammar_only,
4	%          phase2_scierc_semantic_only, phase2_scierc_full_s1, phase2_scierc_full_s2
5	% All numbers verified against registry 2026-05-14.
6	
7	\subsection{Ablation and Composability with Fine-Tuning}
8	\label{sec:scierc-results}
9	
10	Table~\ref{tab:scierc-ablation} presents the five-way ablation on SciERC (Qwen3-8B, zero-shot, 551 documents); only the active constraint layers differ across rows.
11	
12	% ──────────────────────────────────────────
13	%  Table: SciERC five-way ablation
14	% ──────────────────────────────────────────
15	\begin{table}[t]
16	\centering
17	\small
18	\setlength{\tabcolsep}{3.6pt}
19	\resizebox{\columnwidth}{!}{%
20	\begin{tabular}{@{}l rrrrrr rr@{}}
21	\toprule
22	& \multicolumn{6}{c}{\textbf{Violation Rates (\%)}}
23	& \multicolumn{2}{c}{\textbf{F1}} \\
24	\cmidrule(lr){2-7} \cmidrule(l){8-9}
25	\textbf{Mode}
26	  & DR\,$\downarrow$ & $\Delta$DR
27	  & RV\,$\downarrow$ & ET\,$\downarrow$ & CF & Tot.\,$\downarrow$
28	  & Rel.\,$\uparrow$ & Ent.\,$\uparrow$ \\
29	\midrule
30	Unconstrained
31	  & 15.37 & ---
32	  & 1.39  & 0.40
33	  & 0.08  & 15.45
34	  & 8.23  & 31.01 \\
35	Grammar
36	  & 14.84 & $\downarrow$3\%
37	  & \textbf{0} & \textbf{0}
38	  & 0.08  & 14.92
39	  & 8.23  & 30.98 \\
40	GCD-equiv.$^\dagger$
41	  & 15.26 & $\downarrow$1\%
42	  & \textbf{0} & \textbf{0}
43	  & 0.04  & 15.30
44	  & 8.75  & 30.91 \\
45	Semantic
46	  & 11.65 & $\downarrow$24\%
47	  & 1.51  & 0.40
48	  & 2.71  & 14.36
49	  & 8.15  & 31.01 \\
50	S1
51	  & \textbf{0.93} & $\downarrow$\textbf{94\%}
52	  & \textbf{0} & \textbf{0}
53	  & 9.90  & \textbf{10.83}
54	  & \textbf{8.36} & 30.98 \\
55	S2
56	  & 0.97  & $\downarrow$94\%
57	  & \textbf{0} & \textbf{0}
58	  & 8.03  & \textbf{9.00}
59	  & 8.03  & \textbf{31.90} \\
60	\bottomrule
61	\end{tabular}}%
62	\caption{Five-way ablation on SciERC (551 docs
…[truncated 7019 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2394 · 2026-05-23T09:17:44.424355+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_violation_landscape.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_violation_landscape.tex"
  }
}
```

</details>

---


### Tool result

_source line 2395 · 2026-05-23T09:17:44.826457+00:00_

1	% §5 Setup (compressed from Violation Landscape)
2	% exp_ids: mvp_phase0_violation_rate, mvp_phase0_scierc_schema,
3	%          mvp_phase0_violation_rate_docred, mvp_phase0_docred_schema
4	
5	\label{sec:violation_landscape}
6	
7	We evaluate OntoCoDec in two deployment configurations: greedy S1 (DR\,$\leq$\,0.09\%, $+$10\% latency) and beam S1 (all violations\,$\to$\,0\%, 1.54$\times$ latency); zero-shot evaluation (\S\ref{sec:scierc-results}; Appendix~\ref{app:cross-model-zs}) serves as a diagnostic probe for the fine-tuned setting (R-F1 41--47\%).
8	
9	\paragraph{Setup.}
10	We evaluate on SciERC~\cite{luan2018scierc} (551 test sentences, 7 relations, $\bar{\kappa}{=}0.333$) and DocRED~\cite{yao2019docred} (998 dev documents,\footnote{DocRED test annotations are not publicly available; we evaluate on the development set.} 96 relations, $\bar{\kappa}{=}0.842$).
11	RE type constraints are extracted from observed type pairs in training data (neither dataset provides a formal ontology); EE constraints on WikiEvents (\S\ref{sec:wikievents}) derive from the KAIROS ontology.
12	All constraints are schema-level, independent of evaluation splits.
13	Primary model: Qwen3-8B~\cite{qwen2025qwen3}, zero-shot greedy decoding; cross-model validation in Appendix~\ref{app:cross-model-zs}, composability with fine-tuning in \S\ref{sec:composability}.
14	LoRA hyperparameters were selected on SciERC development data and transferred to DocRED without further tuning; DocRED development documents were used for evaluation only.
15	Four violation categories: \textbf{DR} (type pair $\notin \sigma(r)$), \textbf{RV} (relation $\notin \mathcal{R}$), \textbf{ET} (entity type $\notin \mathcal{E}$), \textbf{CF} (conflicting types across triples).
16	Baseline DR: 15.37\% (SciERC), 18.46\% (DocRED); schema-informed prompting reduces DR by 62\% but is per-relation unreliable (Appendix~\ref{app:per-relation-landscape}).
17	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 2396 · 2026-05-23T09:17:44.927311+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section2_background.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section2_background.tex"
  }
}
```

</details>

---


### Tool result

_source line 2397 · 2026-05-23T09:17:45.580485+00:00_

1	% Section 2: Background (compressed)
2	
3	\section{Background}
4	\label{sec:background}
5	
6	\paragraph{IE Ontology Structure.}
7	\label{sec:bg:ontology}
8	An IE ontology $\mathcal{O} = (\mathcal{E}, \mathcal{R}, \sigma)$ defines entity types $\mathcal{E}$, relation types $\mathcal{R}$, and a mapping $\sigma: \mathcal{R} \to \mathcal{P}(\mathcal{E} \times \mathcal{E})$, where $\mathcal{P}(\cdot)$ denotes the power set, specifying valid (head type, tail type) pairs per relation.
9	A triple $(h, r, t)$ is \emph{type-valid} if $(\mathrm{type}(h), \mathrm{type}(t)) \in \sigma(r)$.
10	We quantify constraint restrictiveness via \emph{constraint tightness} $\kappa(r)$ (\S\ref{sec:composition}): tighter constraints leave fewer valid type pairs per relation.
11	We define ontology constraints broadly to encompass both formal ontology specifications (e.g., the KAIROS event ontology with explicit role-entity type mappings) and empirically derived type-pair constraints extracted from annotated training data.
12	The latter applies when datasets lack a formal ontology but provide typed annotations (SciERC, DocRED); OntoCoDec compiles both sources into the same constraint representation without modification.
13	Empirical constraints achieve 99\%+ instance-level coverage on held-out data (SciERC 99.0\%, DocRED 99.4\%); uncovered type pairs trigger grammar-first fallback (\S\ref{sec:composition}), ensuring no valid triples are blocked.
14	
15	\paragraph{Grammar-Constrained Decoding.}
16	\label{sec:bg:gcd}
17	Grammar-constrained decoding restricts each token $y_t$ to a mask $M_g \in \{0, 1\}^{|V|}$ derived from a target grammar.
18	XGrammar~\citep{dong2025xgrammar} compiles JSON Schemas into pushdown automata for efficient enforcement of structural constraints; Outlines~\citep{willard2023outlines} and SGLang~\citep{zheng2024sglang} offer similar capabilities.
19	However, these methods are limited to context-free constraints and cannot enforce cross-field semantic rules (e.g., ``if $
…[truncated 886 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "elapsed_ms": 653
}
```

</details>

---


### Tool call

_source line 2398 · 2026-05-23T09:17:45.731617+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section4_composition_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section4_composition_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 2399 · 2026-05-23T09:17:45.782358+00:00_

1	% Section: Constraint Composition (compressed, 787→~500 words)
2	
3	At each decoding step $t$, let $G(t) \subseteq V$ and $S(t) \subseteq V$ denote the tokens permitted by the grammar and semantic layers, respectively.
4	The final mask is their conjunction:
5	%
6	\begin{equation}\label{eq:composition}
7	  M_{\text{final}}(t) = M_{\text{grammar}}(t) \;\wedge\; M_{\text{semantic}}(t),
8	\end{equation}
9	%
10	where $\wedge$ denotes element-wise AND over the vocabulary $V$; a token is allowed only if it satisfies \emph{both} structural and type-level constraints.
11	The conjunction is asymmetric: $S(t)$ is defined only over $G(t)$. This reflects the scale-dependent layer interaction (\S\ref{sec:method}): the semantic layer requires the relation type to belong to $\mathcal{R}$, a property enforced only by the grammar layer.
12	This dependency is scale-sensitive: 70B semantic-only achieves 84\% DR reduction (vs.\ 24\% on 8B), though grammar remains necessary for RV elimination (\S\ref{sec:70b-results}).
13	
14	\paragraph{Grammar-First Fallback.}
15	When $S(t) \cap G(t) = \emptyset$ (tight constraints leave no token that is both grammar-valid and semantically valid), na\"{\i}ve masking would force selection of a grammar-invalid token, breaking JSON structure.
16	We enforce a \emph{grammar-first fallback}: semantic masking is skipped and the grammar layer alone controls selection.
17	Structural integrity is a hard constraint; type violations are soft errors detectable by downstream validation, with DR (ontologically invalid type pair) more severe than CF (individually valid triples with cross-triple type inconsistency).
18	Extraction tasks are robust to format-level constraints~\cite{tam2024letmespeak}, supporting this asymmetric treatment.
19	
20	\paragraph{Constraint Tightness.}
21	\label{eq:tightness}
22	Per-relation constraint tightness $\kappa(r) = 1 - |\sigma(r)|/|\mathcal{E}|^2$, with schema mean $\bar{\kappa}$.
23	Across WikiEvents ($\bar{\kappa}{=}0.029$), SciERC
…[truncated 1621 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2400 · 2026-05-23T09:17:51.709200+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_wikievents_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_wikievents_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 2401 · 2026-05-23T09:17:52.011834+00:00_

1	% Section 5 — Event Extraction on WikiEvents (compact, inline)
2	% exp_ids: ee_qwen_wikievents_unconstrained, ee_llama_wikievents_unconstrained,
3	%          ee_mistral_wikievents_unconstrained, ee_qwen_wikievents_constrained,
4	%          ee_llama_wikievents_constrained, ee_mistral_wikievents_constrained_v2
5	% v3 final data confirmed by Director 2026-05-18.
6	
7	\subsection{Preliminary Event Extraction Pilot}
8	\label{sec:wikievents}
9	
10	As a preliminary pilot study, we apply OntoCoDec to event extraction (EE) on WikiEvents~\cite{li2021document,lu2021text2event} (56 event types, 80 roles, 27 entity types, 245 constraints; Appendix~\ref{app:wikievents}) without modification.
11	Violations extend to EV (event vocabulary), RoV (role vocabulary), and AC (argument constraint, analogous to DR).
12	
13	% ──────────────────────────────────────────
14	%  Table: WikiEvents three-model comparison (v3 final)
15	%  exp_ids: ee_{qwen,llama,mistral}_wikievents_{unconstrained,grammar_only,constrained_v3}
16	% ──────────────────────────────────────────
17	\begin{table}[t]
18	\centering
19	\small
20	\setlength{\tabcolsep}{2.8pt}
21	\resizebox{\columnwidth}{!}{%
22	\begin{tabular}{@{}ll rrrr rr@{}}
23	\toprule
24	& & \multicolumn{4}{c}{\textbf{Violation Rates (\%)}}
25	& \multicolumn{2}{c}{\textbf{F1}} \\
26	\cmidrule(lr){3-6} \cmidrule(l){7-8}
27	\textbf{Model} & \textbf{Mode}
28	  & EV\,$\downarrow$ & RoV\,$\downarrow$ & AC & CF
29	  & Trig.\,$\uparrow$ & Ent.\,$\uparrow$ \\
30	\midrule
31	\multirow{3}{*}{Qwen3-8B}
32	  & Unconstr.\ & 24.0 & 74.9 & 0.3 & 0 & 11.8 & 0 \\
33	  & Grammar    & \textbf{0} & 76.1 & 8.2 & --- & --- & --- \\
34	  & S1    & \textbf{0} & \textbf{0} & 2.1 & 21.1 & 13.4 & 14.1 \\
35	\midrule
36	\multirow{3}{*}{\shortstack[l]{Llama\\3.1-8B}}
37	  & Unconstr.\ & 10.5 & 88.8 & 0.1 & 0 & 5.7 & 0 \\
38	  & Grammar    & \textbf{0} & 77.0 & 8.8 & --- & --- & --- \\
39	  & S1    & \textbf{0} & \textbf{0} & 3.8 & 17.2 & 7.5 & 17.6 \\
40	\midrule
41	\multirow{3}{*}
…[truncated 2122 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "elapsed_ms": 302
}
```

</details>

---


### Tool call

_source line 2402 · 2026-05-23T09:17:52.213223+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_runtime.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_runtime.tex"
  }
}
```

</details>

---


### Tool result

_source line 2403 · 2026-05-23T09:17:53.017152+00:00_

1	% Runtime overhead (inline paragraph, no subsection header to save space)
2	
3	\paragraph{Runtime overhead.}
4	\label{sec:runtime}
5	S1 overhead is $+$13.1\% on SciERC, lower on DocRED due to amortization over longer sequences; under LoRA, $+$10.0\% with 37\% lower absolute latency.
6	Constraint compilation is one-time $<$0.5\,s; scaling benchmarks confirm constant overhead (2--3\%) up to 200 entity types and 1{,}000 relations (Appendix~\ref{app:scalability}).
7	
8	\paragraph{Beam search compatibility.}
9	\label{sec:beam-results}
10	With LoRA, beam search ($k{=}4$)~\cite{anderson2017guided} eliminates all four violation types on both SciERC and DocRED at both 8B and 70B scales (R-F1 43--47; Appendix~\ref{app:beam-search}), yielding two deployment tiers: greedy S1 ($+$10\% latency, DR${<}$0.1\%, CF${\leq}$1.4\%) and beam S1 (1.54$\times$ latency, all violations${\to}$0\%; Table~\ref{tab:beam-latency}).
11	
12	% exp_ids: r16_70b_scierc_zs_s1, r16_70b_docred_zs_s1, 70b_lora_scierc, 70b_lora_docred_200
13	\paragraph{70B-class validation.}
14	\label{sec:70b-results}
15	All 70B experiments use Llama-3.1-70B-Instruct under AWQ INT4 quantization; an 8B ablation confirms constraint enforcement is unaffected by quantization (Appendix~\ref{app:quantization}).
16	Zero-shot S1 eliminates DR on both datasets (SciERC 6.41\%\,$\to$\,0\%, DocRED 14.98\%\,$\to$\,0\%; R-F1 11--13).
17	% exp_ids: r16_70b_scierc_zs_ablation (grammar_only, semantic_only, full_s1)
18	A four-way ablation reveals scale-dependent layer interaction: semantic-only achieves 84\% DR reduction vs.\ 8B's 24\% (Table~\ref{tab:scierc-ablation}), though grammar remains necessary for RV elimination and CF control (semantic-only CF${=}$76).
19	% exp_ids: eval_70b_lora_scierc_s1_constrained, eval_70b_lora_docred_200_s1_constrained
20	LoRA confirms composability: DR\,$\to$\,0\% on both datasets (R-F1 44.53, 43.95; $|\Delta| \leq 0.20$\,pp; CF 0.18--1.33\%); cross-family generalization at 70B scale remains to be verifie
…[truncated 955 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "elapsed_ms": 803
}
```

</details>

---


### Tool call

_source line 2404 · 2026-05-23T09:17:53.017643+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 2405 · 2026-05-23T09:17:53.419668+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	We provide a detailed survey in Appendix~\ref{app:related_work}; here we position OntoCoDec along three axes.
5	
6	\paragraph{Constrained decoding.}
7	XGrammar~\cite{dong2025xgrammar}, Outlines~\cite{willard2023outlines}, SynCode~\cite{ugare2024syncode}, SGLang~\cite{zheng2024sglang}, and related systems~\cite{beurer-kellner2023lmql,park2024grammar,jsonschemabench2025} enforce format validity via CFG-based token masking.
8	NeuroLogic Decoding~\cite{lu2021neurologic} and \citet{huang2024lookahead} enforce constraints via beam-level reranking; OntoCoDec applies per-token masking, avoiding beam-width dependence.
9	PICARD~\cite{scholak2021picard} and \citet{pldi2025_type_constrained_codegen} compile type systems into prefix automata; OntoCoDec applies constructive forward masking via a dynamic entity registry (\S\ref{sec:composition}).
10	DCCD~\cite{dccd2026} and \citet{nguyen2026thinking} decouple reasoning from constrained generation; OntoCoDec enforces schema semantics within a single forward pass.
11	
12	\paragraph{Schema-aware IE.}
13	GoLLIE~\cite{sainz2024gollie}, KnowCoder~\cite{knowcoder_acl2024}, GUIDEX~\cite{guidex2025}, GenIE~\cite{josifoski2022genie}, TANL~\cite{paolini2021tanl}, REBEL~\cite{cabot2021rebel}, InstructUIE~\cite{wang2023instructuie}, ADELIE~\cite{qi2024adelie}, and others~\cite{fei2022lasuie,wang2022deepstruct,lu2022uie,lou2023usm,zhou2024universalner} encode ontology structure or frame IE as structured generation, though schema compliance gaps persist~\cite{wadhwa2023revisiting}.
14	GoLLIE and KnowCoder embed schema knowledge via code-style prompts (training-time internalization without runtime enforcement).
15	GoLLIE-7B achieves zero DR under zero-shot evaluation, but at the cost of near-complete output suppression (5 predicted relations vs.\ ${>}$1{,}100 for OntoCoDec under LoRA fine-tuning, 46\% empty output; Appendix~\ref{app:gollie-comparison}).
16	Direct comparison is methodologica
…[truncated 1017 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 2406 · 2026-05-23T09:17:53.420204+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section7_conclusion_compressed.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section7_conclusion_compressed.tex"
  }
}
```

</details>

---


### Tool result

_source line 2407 · 2026-05-23T09:17:53.571218+00:00_

1	% Section 7 — Discussion and Conclusion
2	
3	OntoCoDec compiles IE ontologies into composable token-level constraints, validated across 3 datasets, 3+ models, and 2 tasks.
4	LoRA + greedy S1 near-eliminates DR ($<$\,0.1\%) at R-F1 41--47\%; beam ($k{=}4$) eliminates all violations at 1.54$\times$ latency.
5	Because IE type constraints exceed context-free expressiveness (Proposition~1), the semantic layer is necessary to bridge the gap grammar-only enforcement cannot address (3\% vs.\ 94\% DR reduction), using constructive forward masking over a dynamic entity registry.
6	This scale-dependent interaction (\S\ref{sec:70b-results}) suggests grammar-constrained decoding is necessary but increasingly insufficient as models improve.
7	Constraint enforcement is preserved under INT4 quantization (4$\times$ compression; Appendix~\ref{app:quantization}), confirming deployment viability without precision-dependent calibration.
8	Global entity-level type consensus during decoding---eliminating CF without beam search overhead---is the primary direction for future work.
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 2408 · 2026-05-23T09:18:04.602261+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_24/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"PDF_NOT_FOUND\"",
  "description": "Check PDF existence"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_24/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"PDF_NOT_FOUND\"",
    "description": "Check PDF existence"
  }
}
```

</details>

---


### Tool result

_source line 2409 · 2026-05-23T09:18:05.356375+00:00_

-rw-r--r-- 1 ubuntu ubuntu 620779 May 23 09:10 /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_24/submitted.pdf
PDF_EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Bash",
  "elapsed_ms": 754
}
```

</details>

---


### Tool call

_source line 2410 · 2026-05-23T09:18:05.859782+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/agent/config.yaml 2>/dev/null | head -100",
  "description": "Check project config for external review settings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/agent/config.yaml 2>/dev/null | head -100",
    "description": "Check project config for external review settings"
  }
}
```

</details>

---


### Tool result

_source line 2411 · 2026-05-23T09:18:06.814202+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Bash",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 2412 · 2026-05-23T09:18:06.965236+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_70b_ablation.tex",
  "limit": "60"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_70b_ablation.tex",
    "limit": "60"
  }
}
```

</details>

---


### Tool result

_source line 2413 · 2026-05-23T09:18:06.965824+00:00_

1	% Appendix: 70B-Class LoRA Ablation on SciERC
2	% exp_ids: eval_70b_lora_scierc_unconstrained, eval_70b_lora_scierc_grammar_only,
3	%          eval_70b_lora_scierc_semantic_only, eval_70b_lora_scierc_s1_constrained,
4	%          eval_70b_lora_scierc_s2_constrained, eval_70b_lora_scierc_beam4_s1
5	
6	\paragraph{70B-class fine-tuned ablation.}
7	\label{app:70b-ablation}
8	
9	Table~\ref{tab:70b-ft-ablation} presents the constraint ablation on Llama-3.1-70B-Instruct (AWQ INT4) with LoRA fine-tuning on SciERC (551 documents).
10	
11	\begin{table}[h]
12	\centering
13	\small
14	\setlength{\tabcolsep}{3.6pt}
15	\begin{tabular}{@{}l rrrr rr@{}}
16	\toprule
17	\textbf{Mode}
18	  & \textbf{DR\,$\downarrow$} & \textbf{RV\,$\downarrow$} & \textbf{ET\,$\downarrow$} & \textbf{CF}
19	  & \textbf{R-F1\,$\uparrow$} & \textbf{E-F1\,$\uparrow$} \\
20	\midrule
21	Unconstrained & 1.50 & 0 & 0 & 0    & 44.73 & 64.86 \\
22	Grammar       & 1.50 & 0 & 0 & 0    & 44.63 & 64.82 \\
23	Semantic      & 0.60 & 0 & 0 & 9    & 44.73 & 64.86 \\
24	S1            & \textbf{0} & 0 & 0 & 15 & 44.53 & 64.76 \\
25	S2            & \textbf{0} & 0 & 0 & 18 & 36.28 & 62.35 \\
26	Beam4 S1      & \textbf{0} & 0 & 0 & \textbf{1} & \textbf{44.81} & \textbf{64.89} \\
27	\bottomrule
28	\end{tabular}
29	\caption{70B-class (Llama-3.1-70B-Instruct (AWQ INT4)) LoRA ablation on SciERC (551 docs).
30	CF: violation count. F1 $\times$100.}
31	\label{tab:70b-ft-ablation}
32	\end{table}
33	
34	The grammar layer provides no independent DR benefit at 70B (1.50\%\,$\to$\,1.50\% on SciERC; on DocRED zero-shot, DR actually increases $+$3.58\,pp due to RV$\to$DR conversion in the high-$\bar{\kappa}$ schema; Table~\ref{tab:70b-docred-zs-ablation}).
35	The semantic layer is the sole effective defense (1.50\%\,$\to$\,0.60\%, 60\% reduction) with no R-F1 cost ($\Delta{=}$0\,pp), and full S1 eliminates all DR.
36	S2 eliminates DR but causes severe R-F1 degradation ($-$8.45\,pp), indicating that optimal constraint granularity is scale-
…[truncated 1467 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2414 · 2026-05-23T09:18:15.652539+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/ -name \"config.yaml\" -o -name \"config.yml\" 2>/dev/null | head -5",
  "description": "Find project config files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/ -name \"config.yaml\" -o -name \"config.yml\" 2>/dev/null | head -5",
    "description": "Find project config files"
  }
}
```

</details>

---


### Tool result

_source line 2415 · 2026-05-23T09:18:17.058768+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Bash",
  "elapsed_ms": 1406
}
```

</details>

---


### Tool call

_source line 2416 · 2026-05-23T09:18:17.159573+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "pdfinfo /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_24/submitted.pdf 2>/dev/null | grep -i pages",
  "description": "Check PDF page count"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Bash",
  "tool_args": {
    "command": "pdfinfo /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_24/submitted.pdf 2>/dev/null | grep -i pages",
    "description": "Check PDF page count"
  }
}
```

</details>

---


### Tool result

_source line 2417 · 2026-05-23T09:18:17.260460+00:00_

Pages:           39

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 2418 · 2026-05-23T09:18:21.780930+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_24/submitted.pdf",
  "pages": "1-9"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_24/submitted.pdf",
    "pages": "1-9"
  }
}
```

</details>

---


### Tool result

_source line 2419 · 2026-05-23T09:18:22.384031+00:00_

PDF pages extracted: 9 page(s) from /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_24/submitted.pdf (606.2KB)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "elapsed_ms": 603
}
```

</details>

---


### Tool call

_source line 2420 · 2026-05-23T09:19:07.463740+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "schema_semantic_constrained_ie",
  "review_chat_id": "oc_01fc90ae186a4ed432770f7601995139"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "schema_semantic_constrained_ie",
    "review_chat_id": "oc_01fc90ae186a4ed432770f7601995139"
  }
}
```

</details>

---


### Tool call

_source line 2421 · 2026-05-23T09:19:07.765144+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "schema_semantic_constrained_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "schema_semantic_constrained_ie"
  }
}
```

</details>

---


### Tool result

_source line 2422 · 2026-05-23T09:19:11.431758+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 3968
}
```

</details>

---


### Tool result

_source line 2423 · 2026-05-23T09:19:11.432195+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 3667
}
```

</details>

---


### Tool call

_source line 2424 · 2026-05-23T09:19:16.406191+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "schema_semantic_constrained_ie",
  "file": "decisions.yaml",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "schema_semantic_constrained_ie",
    "file": "decisions.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 2425 · 2026-05-23T09:19:17.912579+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/decisions.yaml\", \"content\": \"_next_id: 86\\ndecisions:\\n- id: D001\\n  date: 2026-05-13 17:38 UTC\\n  summary: 主目标调整为 EMNLP 2026 ARR (5/25), AAAI 2027 为后备\\n  rationale: 用户明确指出 EMNLP ARR 5/25 时间不紧、不要保守、资源会给够。12 天 AI 团队速度足够：Phase 0 (1-2天) →\\n    Phase 1 compiler (2-3天) → Phase 2 experiments (2-3天) → Paper (2-3天)。禁止 fallback\\n    思维，冲最高目标。\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-13 19:14 UTC\\n  summary: SciERC Phase 0 结果确认 GO — domain_range violation rate 15.4%，3× 超阈值\\n  rationale: 'SciERC 全量 test set (551 sentences, 1724 triples): domain_range_violation_rate\\n    = 15.4%，远超 5% go/no-go 阈值。违规分布极不均匀 (Feature-of 33.5%, Compare 42.4% vs Used-for\\n    0.76%)，支持\\\"特定 relation types 需要 decoding-time enforcement\\\"的论文 claim。DocRED dry-run\\n    (37 docs) 同样显示 14.4%。两个数据集均为 GO 信号，MVP 核心假设得到强验证。等 schema-informed prompt 结果确认\\n    prompt 级干预不足以解决问题后正式宣布 MVP 通过。'\\n  related_experiments:\\n  - exp_id: mvp_phase0_violation_rate\\n    role: primary\\n    result: domain_range_violation_rate=15.4%, go_nogo=GO\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-13 21:48 UTC\\n  summary: MVP 通过，进入 Research 阶段，立即启动 Phase 2 constrained decoding 实验\\n  rationale: Phase 0 三个实验完成：SciERC 15.4%/5.78%, DocRED 18.7% domain_range violation\\n    rate。两个数据集均远超 5% 阈值，核心假设得到强验证。Phase 1 compiler 代码就绪（36 tests 通过），Phase 2 脚本就绪（S1\\n    路径可用，S2 bug 修复中）。cuda:1 空闲，立即启动 Phase 2 SciERC grammar_only/semantic_only/full_s1\\n    实验。\\n  related_experiments:\\n  - exp_id: mvp_phase0_violation_rate\\n    role: primary\\n    result: SciERC DR=15.4%, GO\\n  - exp_id: mvp_phase0_scierc_schema\\n    role: primary\\n    result: SciERC DR=5.78%, prompt insufficient\\n  - exp_id: mvp_phase0_violation_rate_docred\\n    role: primary\\n    result: DocRED DR=18.7%, GO\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-
…[truncated 1469 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 1506
}
```

</details>

---


### Tool call

_source line 2426 · 2026-05-23T09:19:18.113893+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_6 -maxdepth 3 -name \"*.yaml\" -path \"*/schema_semantic*\" 2>/dev/null | head -10",
  "description": "Find project YAML config files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_6 -maxdepth 3 -name \"*.yaml\" -path \"*/schema_semantic*\" 2>/dev/null | head -10",
    "description": "Find project YAML config files"
  }
}
```

</details>

---


### Tool result

_source line 2427 · 2026-05-23T09:19:18.164591+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/dream_registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/writing_plan.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/literature_map.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/mistakes.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/decisions.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/experiment_plan.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/config/projects/schema_semantic_constrained_ie.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2428 · 2026-05-23T09:19:21.480158+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -A5 \"external_review\" /home/ubuntu/.agent-ml-research-idea_gen_0509_6/config/projects/schema_semantic_constrained_ie.yaml 2>/dev/null || echo \"NOT_FOUND\"",
  "description": "Check external review config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -A5 \"external_review\" /home/ubuntu/.agent-ml-research-idea_gen_0509_6/config/projects/schema_semantic_constrained_ie.yaml 2>/dev/null || echo \"NOT_FOUND\"",
    "description": "Check external review config"
  }
}
```

</details>

---


### Tool result

_source line 2429 · 2026-05-23T09:19:21.530854+00:00_

NOT_FOUND

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2430 · 2026-05-23T09:19:25.026040+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -i \"external\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0509_6/config/projects/schema_semantic_constrained_ie.yaml 2>/dev/null || echo \"NO_EXTERNAL_REVIEW_CONFIG\"",
  "description": "Search for external review config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -i \"external\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0509_6/config/projects/schema_semantic_constrained_ie.yaml 2>/dev/null || echo \"NO_EXTERNAL_REVIEW_CONFIG\"",
    "description": "Search for external review config"
  }
}
```

</details>

---


### Tool result

_source line 2431 · 2026-05-23T09:19:25.076886+00:00_

NO_EXTERNAL_REVIEW_CONFIG

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2432 · 2026-05-23T09:20:09.573942+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "## 审稿任务 — Round 24, Reviewer 1\n\n**论文**: OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints\n**Venue**: EMNLP 2026 (via ARR)\n**截止日期**: 2026-05-25\n**类型**: Long Paper (8 页正文限制，附录/参考文献不限)\n**模板**: ACL style (`\\usepackage[review]{acl}`)\n**匿名**: double-blind\n**评分标准**: ARR Overall Assessment (5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit)\n\n**论文文件**:\n- LaTeX: `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_24/submitted.pdf`\n\n**你的审查侧重：方法严谨性 + 实验设计**\n\n请重点评估以下方面：\n\n1. **Proposition 1 (Level 2 ⊄ Level 1)**: 证明的形式严谨性——proof sketch 是否充分？unbounded vs finite entity set 的论证跳跃是否合理？Engineering applicability paragraph 是否弥合了理论与实践的 gap？\n\n2. **两层架构设计**: grammar layer + semantic layer 的组合是否有设计上的盲点？grammar-first fallback 的正确性和完备性论证是否充分？entity registry first-seen semantics 是否有未讨论的 corner case？\n\n3. **Ablation 设计**: 五路消融（Table 1）是否充分？各 ablation 配置之间的比较是否公平？\"empirical enabling dependency\" 的声明是否被数据充分支撑？GCD-equiv 行的等价性论证是否可信？\n\n4. **统计声明**: Bonferroni-corrected CI、p 值、effect size 的使用是否正确？WikiEvents n=20 的 power analysis 是否恰当？κ 与 DR reduction 的相关性声明 (n=3, p=0.138) 的呈现方式是否合适？\n\n5. **Fine-tuning composability**: LoRA 超参从 SciERC 转移到 DocRED 不做调优是否合理？DR elimination 在 70B AWQ INT4 下的验证是否充分（无 FP16 对比）？S2 在 70B 的退化（-8.45pp）是否有令人信服的解释？\n\n6. **CF 分析**: 63.3% Generic↔X 集中度意味着什么？per-triple independent enforcement 的 architectural limitation 是否被充分量化和讨论？beam search 作为 CF 解决方案是否实际可行（latency trade-off）？\n\n7. **Cross-model 验证**: 3 模型 × 2 数据集的覆盖是否足够？70B 仅验证了 1 个模型族（Llama），这个限制是否被充分讨论？\n\n请按 Summary → Strengths → Weaknesses (Must-Fix / Should-Fix / Minor) → Questions → Missing References → Overall Assessment 格式输出审稿意见。Weakness 是重点，必须严格、具体、引用具体 Section/Table/Figure。",
  "project": "schema_semantic_constrained_ie",
  "chat_id": "oc_01fc90ae186a4ed432770f7601995139",
  "director_session_key": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "## 审稿任务 — Round 24, Reviewer 1\n\n**论文**: OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints\n**Venue**: EMNLP 2026 (via ARR)\n**截止日期**: 2026-05-25\n**类型**: Long Paper (8 页正文限制，附录/参考文献不限)\n**模板**: ACL style (`\\usepackage[review]{acl}`)\n**匿名**: double-blind\n**评分标准**: ARR Overall Assessment (5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit)\n\n**论文文件**:\n- LaTeX: `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_24/submitted.pdf`\n\n**你的审查侧重：方法严谨性 + 实验设计**\n\n请重点评估以下方面：\n\n1. **Proposition 1 (Level 2 ⊄ Level 1)**: 证明的形式严谨性——proof sketch 是否充分？unbounded vs finite entity set 的论证跳跃是否合理？Engineering applicability paragraph 是否弥合了理论与实践的 gap？\n\n2. **两层架构设计**: grammar layer + semantic layer 的组合是否有设计上的盲点？grammar-first fallback 的正确性和完备性论证是否充分？entity registry first-seen semantics 是否有未讨论的 corner case？\n\n3. **Ablation 设计**: 五路消融（Table 1）是否充分？各 ablation 配置之间的比较是否公平？\"empirical enabling dependency\" 的声明是否被数据充分支撑？GCD-equiv 行的等价性论证是否可信？\n\n4. **统计声明**: Bonferroni-corrected CI、p 值、effect size 的使用是否正确？WikiEvents n=20 的 power analysis 是否恰当？κ 与 DR reduction 的相关性声明 (n=3, p=0.138) 的呈现方式是否合适？\n\n5. **Fine-tuning composability**: LoRA 超参从 SciERC 转移到 DocRED 不做调优是否合理？DR elimination 在 70B AWQ INT4 下的验证是否充分（无 FP16 对比）？S2 在 70B 的退化（-8.45pp）是否有令人信服的解释？\n\n6. **CF 分析**: 63.3% Generic↔X 集中度意味着什么？per-triple independent enforcement 的 architectural limitation 是否被充分量化和讨论？beam search 作为 CF 解决方案是否实际可行（latency trade-off）？\n\n7. **Cross-model 验证**: 3 模型 × 2 数据集的覆盖是否足够？70B 仅验证了 1 个模型族（Llama），这个限制是否被充分讨论？\n\n请按 Summary → Strengths → Weaknesses (Must-Fix / Should-Fix / Minor) → Questions → Missing References → Overall Assessment 格式输出审稿意见。Weakness 是重点，必须严格、具体、引用具体 Section/Table/Figure。",
    "project": "schema_semantic_constrained_ie",
    "chat_id": "oc_01fc90ae186a4ed432770f7601995139",
    "director_session_key": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director"
  }
}
```

</details>

---


### Tool result

_source line 2433 · 2026-05-23T09:20:30.046759+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 20472
}
```

</details>

---


### Tool call

_source line 2434 · 2026-05-23T09:20:30.549909+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "## 审稿任务 — Round 24, Reviewer 2\n\n**论文**: OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints\n**Venue**: EMNLP 2026 (via ARR)\n**截止日期**: 2026-05-25\n**类型**: Long Paper (8 页正文限制，附录/参考文献不限)\n**模板**: ACL style (`\\usepackage[review]{acl}`)\n**匿名**: double-blind\n**评分标准**: ARR Overall Assessment (5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit)\n\n**论文文件**:\n- LaTeX: `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_24/submitted.pdf`\n\n**你的审查侧重：新颖性 + 完整性 + 写作质量**\n\n请重点评估以下方面：\n\n1. **贡献新颖性**: 论文自称 \"systematic engineering contribution with theoretical grounding\"。核心方法本质上是 XGrammar + stateful logits processor 的系统集成——这对 EMNLP 2026 是否足够？Proposition 1 的理论贡献是否提升了整体 novelty ceiling？与 PICARD、SynCode、IterGen 等的差异化是否清晰？\n\n2. **Related Work 覆盖**: §6 是否遗漏了重要的相关工作？特别关注：(a) 2025-2026 年的 constrained decoding 新进展（DCCD、FormaTax、CRANE 等已引用，还有遗漏吗？）；(b) IE 领域的 type constraint enforcement 历史（ILP-based、ASP-based）是否覆盖充分？(c) 是否有直接对标但未引用的工作？用 web_search 验证。\n\n3. **叙事结构**: Abstract→Introduction→Method→Experiments 的故事线是否连贯？\"problem → gap → solution → validation\" 的逻辑链是否有断裂？zero-shot 作为 \"diagnostic probe\" 与 fine-tuning 作为 \"practical setting\" 的双轨叙事是否清晰？\n\n4. **贡献声明**: §1 的两条 contribution 是否准确反映论文实际内容？WikiEvents \"preliminary pilot\" 和 \"directional evidence\" 的措辞是否合适？是否存在过度声称或不足声称？\n\n5. **篇幅分配**: 主文 8 页的空间分配是否合理？§5.1 ablation + composability + CF analysis 的密度是否过高？§5.2 WikiEvents n=20 pilot 占的篇幅是否与其 contribution 匹配？§7 Discussion 是否过于简短？\n\n6. **写作质量**: 术语一致性（DR/CF/RV/ET 定义是否首次出现时足够清楚？）；notation 密度是否影响可读性？Figure 1 是否有效传达架构？表格 caption 是否包含足够信息？\n\n7. **格式合规**: \n   - 主文是否在 8 页以内？\n   - Limitations section 是否存在且位置正确（正文内，不在 appendix）？\n   - Ethics Statement 是否存在？\n   - 匿名性是否保持（无作者身份泄露）？\n   - 参考文献格式是否一致？\n\n请按 Summary → Strengths → Weaknesses (Must-Fix / Should-Fix / Minor) → Questions → Missing References → Overall Assessment 格式输出审稿意见。Weakness 是重点，必须严格、具体、引用具体 Section/Table/Figure。",
  "project": "schema_semantic_constrained_ie",
  "chat_id": "oc_01fc90ae186a4ed432770f7601995139",
  "director_session_key": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "## 审稿任务 — Round 24, Reviewer 2\n\n**论文**: OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints\n**Venue**: EMNLP 2026 (via ARR)\n**截止日期**: 2026-05-25\n**类型**: Long Paper (8 页正文限制，附录/参考文献不限)\n**模板**: ACL style (`\\usepackage[review]{acl}`)\n**匿名**: double-blind\n**评分标准**: ARR Overall Assessment (5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit)\n\n**论文文件**:\n- LaTeX: `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_24/submitted.pdf`\n\n**你的审查侧重：新颖性 + 完整性 + 写作质量**\n\n请重点评估以下方面：\n\n1. **贡献新颖性**: 论文自称 \"systematic engineering contribution with theoretical grounding\"。核心方法本质上是 XGrammar + stateful logits processor 的系统集成——这对 EMNLP 2026 是否足够？Proposition 1 的理论贡献是否提升了整体 novelty ceiling？与 PICARD、SynCode、IterGen 等的差异化是否清晰？\n\n2. **Related Work 覆盖**: §6 是否遗漏了重要的相关工作？特别关注：(a) 2025-2026 年的 constrained decoding 新进展（DCCD、FormaTax、CRANE 等已引用，还有遗漏吗？）；(b) IE 领域的 type constraint enforcement 历史（ILP-based、ASP-based）是否覆盖充分？(c) 是否有直接对标但未引用的工作？用 web_search 验证。\n\n3. **叙事结构**: Abstract→Introduction→Method→Experiments 的故事线是否连贯？\"problem → gap → solution → validation\" 的逻辑链是否有断裂？zero-shot 作为 \"diagnostic probe\" 与 fine-tuning 作为 \"practical setting\" 的双轨叙事是否清晰？\n\n4. **贡献声明**: §1 的两条 contribution 是否准确反映论文实际内容？WikiEvents \"preliminary pilot\" 和 \"directional evidence\" 的措辞是否合适？是否存在过度声称或不足声称？\n\n5. **篇幅分配**: 主文 8 页的空间分配是否合理？§5.1 ablation + composability + CF analysis 的密度是否过高？§5.2 WikiEvents n=20 pilot 占的篇幅是否与其 contribution 匹配？§7 Discussion 是否过于简短？\n\n6. **写作质量**: 术语一致性（DR/CF/RV/ET 定义是否首次出现时足够清楚？）；notation 密度是否影响可读性？Figure 1 是否有效传达架构？表格 caption 是否包含足够信息？\n\n7. **格式合规**: \n   - 主文是否在 8 页以内？\n   - Limitations section 是否存在且位置正确（正文内，不在 appendix）？\n   - Ethics Statement 是否存在？\n   - 匿名性是否保持（无作者身份泄露）？\n   - 参考文献格式是否一致？\n\n请按 Summary → Strengths → Weaknesses (Must-Fix / Should-Fix / Minor) → Questions → Missing References → Overall Assessment 格式输出审稿意见。Weakness 是重点，必须严格、具体、引用具体 Section/Table/Figure。",
    "project": "schema_semantic_constrained_ie",
    "chat_id": "oc_01fc90ae186a4ed432770f7601995139",
    "director_session_key": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director"
  }
}
```

</details>

---


### Tool result

_source line 2435 · 2026-05-23T09:20:31.963134+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1413
}
```

</details>

---


### Assistant

_source line 2436 · 2026-05-23T09:20:46.240604+00:00_

**Round 24 审稿已启动。**

当前状态：
- **Reviewer 1**（方法严谨性 + 实验设计）：已派发，等待返回
- **Reviewer 2**（新颖性 + 完整性 + 写作）：已派发，等待返回
- **视觉审查 Agent**：已派发，后台并行执行
- **外部审稿**：未配置，跳过

Venue 确认：
- EMNLP 2026 via ARR，Long Paper，8 页正文限制
- Deadline 2026-05-25（距今 2 天）
- Double-blind，ACL template
- 主文 8 页 ✓，Limitations/Ethics ✓，匿名 ✓

等待两位 Reviewer 返回初审意见后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director"
}
```

</details>

---


## Round 173

## Round 173

2 recorded events


### User

_source line 2437 · 2026-05-23T09:27:23.658985+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 审稿意见 — Round 24

**论文**: OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints
**审查侧重**: 新颖性 + 完整性 + 写作质量

---

## 总体评分
**Overall**: 3.0 (Findings)
**一句话总结**: 一篇执行扎实的系统工程工作，通过两层约束解码近乎消除 IE 类型违规，但理论贡献浅薄、缺乏强 baseline 对比、WikiEvents pilot 过于初步，整体新颖性不足以支撑 main conference。

## 官方维度打分（ACL ARR review form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 方法论正确，消融实验设计合理；但 Proposition 1 理论贡献被高估，强 baseline 缺失，WikiEvents n=20 无统计意义 |
| Excitement | 2.5/5 | 解决了真实问题，但方案是现有组件（XGrammar + stateful logits processor）的集成，对熟悉 constrained decoding 的读者缺乏惊喜 |
| Overall Assessment | 3.0/5 | Findings 水平：工程质量高、分析诚实，但新颖性天花板低 |
| Reproducibility | 4/5 | 详细实验配置、承诺开源、27 个附录；代码未公开（acceptance 后释放） |
| Confidence | 4/5 | 熟悉 constrained decoding 和 IE 文献 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] Proposition 1 的理论贡献被高估，不构成实质性 novelty

- 具体位置：§3 Method, Proposition 1 (Page 3)
- 问题：论文声称 "we formalize a well-known intuition that cross-field type constraints require runtime state beyond context-free expressiveness"（§1, Contribution 1）。然而 Proposition 1 证明的内容——PDA 无法对无界序列进行随机访问——是自动机理论的基础知识。任何需要 cross-position dependency 的约束都超出 CFG 表达能力，这在形式语言理论中是 trivial 的。论文自身也承认这是 "well-known intuition" 的形式化，但将其包装为核心理论贡献（"theoretical grounding"）并作为 Contribution 1 的一部分呈现，夸大了其学术新颖性。
- 为什么影响接收：论文自我定位为 "systematic engineering contribution with theoretical grounding"——如果 theoretical grounding 部分是 trivial 的，那么整体贡献降级为纯工程贡献。对于 EMNLP main conference，纯系统集成工作（XGrammar + stateful logits processor）的 novelty bar 更难满足。
- 建议修改方向：诚实地将 Proposition 1 定位为 motivating observation 而非 theoretical contribution；将重心转移到 empirical findings（如 scale-dependent layer interaction）作为核心贡献。

**N2** [critical] 缺乏与强 baseline 的公平对比

- 具体位置：§5.1, §6 Related Work (Pages 6, 8)
- 问题：论文的 "constrained baseline" 比较仅限于 grammar-only 方法（GCD、vLLM guided_json），这些方法被论文自身证明只能减少 3% DR——本质上是 strawman comparison。与真正相关的强 baseline 缺乏可比对比：(a) GoLLIE：论文承认 "Direct comparison is methodologically constrained"（§6），但未解决这一问题；(b) KnowCoder（ACL 2024）被引用但无实验对比；(c) 未对比 post-hoc type repair 方法（修复违规而非丢弃）。
- 为什么影响接收：无法判断 OntoCoDec 相对于 SOTA schema-aware IE 系统的实际优势。
- 建议修改方向：至少实现一个 post-hoc type repair baseline；或用 GoLLIE 在相同数据上做可比评估。

**N3** [critical] R-F1 41–47% 的绝对质量缺乏上下文定位

- 具体位置：§5.1 Table 2, Abstract (Pages 1, 6)
- 问题：R-F1 41–47% 未与 SciERC/DocRED 上的 SOTA（SpanBERT/PL-Marker 50%+, DocRED 60%+）对比。在如此低的 F1 下讨论 0.09% DR 的实际意义需要更多论证。
- 为什么影响接收：如果提取质量本身不具竞争力，类型约束的实际价值被削弱。
- 建议修改方向：在 §5 Setup 中增加 LLM-based generative RE 在这些数据集上的典型 F1 范围讨论。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] WikiEvents pilot (§5.2) 篇幅与贡献不匹配
- n=20 test docs, MDE≈±5pp, "directional only"。在 8 页限制下用 ~半页呈现无法得出统计结论的 pilot study 是空间浪费。建议缩减释放空间给 §7。

**W2** [warning] CF 违规作为 "可修正副作用" 的叙事过于乐观
- Greedy S1 引入 CF（zero-shot: 0→9.82pp）。TCR 减少 18–92%（范围极大），beam search 1.54× latency。在 zero-shot 下 CF 高达 12%，OntoCoDec 可能增加总体错误率。建议更审慎讨论 CF 代价。

**W3** [warning] §7 Discussion 仅 8 行，过于压缩
- 未讨论：何时选择 grammar-only vs. full two-layer；对其他结构化生成任务的启示；per-triple vs. global enforcement 的根本张力。

**W4** [warning] 约束来源模糊削弱 "ontology-compiled" 框架
- SciERC/DocRED 约束来自训练数据观测值，非形式本体。99% coverage 意味着 ~1% valid pairs 未覆盖。标题 "OntoCoDec" 暗示形式化本体，与实际不完全匹配。

**W5** [warning] Contribution 2 过度打包
- 一个 bullet 包含 4 models × 2 precisions × 2 datasets、scale-dependent interaction、CF side effect、beam search、WikiEvents pilot。应拆分为 2-3 条更聚焦的贡献。

---

## 小问题

- Abstract 第三段 "Composed with LoRA fine-tuning" 在解释框架前出现，认知负担高
- 违规减少报告方式不一致（绝对值 vs. 相对值），应统一
- Table 1 caption "F1 ×100" 容易被忽略，建议表头直接标注 "F1 (%)"
- "First-seen semantics" 在 beam search 下的行为未讨论
- §4 κ 相关性基于 n=3（p=0.138），不应过度解读

---

## 遗漏的相关工作

1. SciDC (arXiv:2604.06603, Apr 2026)——将领域知识编译为多层约束指导生成
2. Dialogue Ontology RE via Constrained CoT (arXiv:2408.02361)——ontology 约束 + CoT 用于关系抽取
3. Graph-Constrained Reasoning / KG-Trie (arXiv:2410.13080)——Trie 编码 KG 约束到解码过程
4. Format Tax 原始论文 (arXiv:2604.03616, 2026) 需核实是否与已引用的 FormaTax 为同一工作

---

## 主要优势

1. 问题定义清晰：DR/CF/RV/ET 违规分类体系化，violation landscape 量化分析有价值
2. 消融实验设计出色：5-way ablation 清晰展示各层效果；scale-dependent layer interaction 是有趣的 empirical finding
3. 分析诚实度高：坦诚 CF 引入、WikiEvents 局限、GoLLIE 对比限制、κ 统计效力不足
4. 附录极详尽：27 个附录覆盖几乎所有 reviewer concern
5. Tokenizer-agnostic continuation masking 具实际工程价值
6. Runtime overhead 合理（fine-tuned S1 仅 +10% latency）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 2438 · 2026-05-23T09:27:30.256092+00:00_

Reviewer 2 审稿意见已收到。等待 Reviewer 1 提交。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director"
}
```

</details>

---


## Round 174

## Round 174

2 recorded events


### User

_source line 2439 · 2026-05-23T09:27:41.293951+00:00_

[Reviewer 2 审稿结果]:
审稿意见已提交给 Review Director。

核心判断：**Overall 3.0 (Findings)**。论文工程执行扎实（5-way ablation、3 模型 × 2 数据集验证、27 个附录），但三个 critical 问题制约了 main conference 接收：

1. **Proposition 1 是 trivial 的**——PDA 无法随机访问是自动机理论基础知识，不构成 "theoretical grounding"
2. **缺强 baseline 对比**——仅与 grammar-only（3% DR reduction 的 strawman）比较，未与 GoLLIE/KnowCoder/post-hoc repair 做可比实验
3. **R-F1 41–47% 未定位**——未说明这在 LLM-based RE 中处于什么水平，削弱 constraint enforcement 的实际意义论证

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 2440 · 2026-05-23T09:27:48.932106+00:00_

Reviewer 2 审稿已收到（Overall 3.0 Findings）。等待 Reviewer 1 完成初审后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director"
}
```

</details>

---


## Round 175

## Round 175

6 recorded events


### User

_source line 2441 · 2026-05-23T09:27:55.895544+00:00_

[Reviewer 1 审稿意见]:

## Reviewer 1 审稿意见 — OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints

**审稿侧重：方法严谨性 + 实验设计**

---

## 总体评分

**Overall**: 3.5 / 5 (Borderline Conference)

**一句话总结**: 论文提出了一个形式化良好、实验全面的两层约束解码框架，核心贡献（将 IE 本体编译为 token 级解码约束）清晰且新颖，但若干统计声明建立在 underpowered 数据上（n=3 相关性、n=20 WikiEvents），70B 验证仅覆盖单一模型族且缺少 FP16 基线，这些缺陷限制了部分 claim 的可信度。

---

## 官方维度打分（来自 ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5 / 5 | 核心方法设计严谨，Proposition 1 形式证明充分（Appendix O），但有限/无限实体集 gap 依赖工程论证而非形式不可能性；部分统计声明（κ-DR 相关性 n=3, p=0.138）在 underpowered 数据上做出 |
| Excitement | 3.5 / 5 | 将 IE 本体约束编译为 token 级解码 mask 的思路新颖且有实践价值，但范围限于 IE + autoregressive LM，cross-field 一致性未解决是根本性限制 |
| Reproducibility | 4 / 5 | 30 页附录覆盖超参、种子、推理细节、统计检验方法；但代码未公开（"upon acceptance"），且部分关键实现细节（XGrammar API 适配、beam search 状态管理）分散在附录各处 |
| Datasets | 3 / 5 | 使用公开数据集 SciERC/DocRED/WikiEvents，未贡献新数据集 |
| Software | 3 / 5 | 承诺发布但尚未公开 |
| Reviewer Confidence | 4 / 5 | 对约束解码、结构化 IE、形式语言理论较为熟悉，仔细审查了证明和统计方法 |

---

## 主要优势

1. **形式化贡献扎实**：三级类型约束可判定性分类（context-free / prefix-decidable with state / non-local, Section 3）清晰且有指导意义。Proposition 1 的完整证明（Appendix O, pages 36-37）使用 pumping lemma 论证了 domain/range 约束不属于 context-free，为两层架构提供了严格的理论基础。

2. **消融设计系统且信息量大**：五路消融（Table 1, Section 5.1）系统地隔离了各组件贡献——grammar-only 24% DR reduction vs. S1 84% 充分展示了语义层的必要性。"Empirical enabling dependency"（非加性交互效应）的发现是有意义的，Figure 2（Appendix C）的 dual-factor 分析提供了可视化支撑。

3. **统计方法论在多数场景下严谨**：Bootstrap CIs（10,000 iterations, document-level resampling, Table 7）、Bonferroni 校正（k=4, α_adj=0.0125）、Cohen's d（all δ ≥ 3.0）的使用方法论正确。交叉硬件验证（seed 42 跨不同 CUDA 驱动，Appendix G page 30）和 vLLM 外部验证（Table 17, Appendix）增强了可信度。

4. **错误分析深入**：CF 违规分布（Table 8）、per-relation DR 消除（Table 9-10）、lucky violation 分析（Table 14）、schema ambiguity 分析（Table 45-46）、下游 F1 影响量化（Table 39）均体现了对方法边界的诚实理解。

5. **工程贡献实用**：grammar-first fallback（§4）在约束冲突时保持 JSON 完整性；entity registry 的 first-seen semantics（§3.3）提供了 O(1) 的类型查找；beam search 兼容性（Appendix E）扩展了部署选项。

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] Proposition 1 的理论-实践 gap 处理不够清晰

- 具体位置：Section 3, page 3（proof sketch）; Appendix O, pages 36-37（full proof）; page 3 "Engineering applicability" paragraph
- 问题：Proposition 1 证明了当实体集 **无界** 时 domain/range 约束不属于 context-free。但在实际 IE 中实体集是 **有限** 的（虽然可能很大）。论文用"Engineering applicability"段落（page 3）桥接这一 gap，论证 DFA 状态数 O(|T|^{|states|}) 使直接构造不可行（DocRED: >10^{17}）。然而：(a) 这是一个 **计算复杂度** 论证，不是 **形式不可能性**——对于小本体（少量实体类型、少量实体），DFA 是可行的；(b) 论文未讨论这个边界在哪里（多少实体类型/实体数时 DFA 变得不可行？）；(c) proof sketch 在正文中过于简略（3 行），读者需翻 Appendix 才能评估证明的完整性。
- 为什么影响接收：Proposition 1 是整个两层架构的理论动机。如果读者认为证明未覆盖实际场景（有限实体集），论文的核心论证链条被削弱。
- 建议修改方向：(1) 在正文中明确区分理论不可能性（无界）和实际不可行性（有界但指数级状态空间）；(2) 给出 DFA 变得可行的边界条件（例如实体类型数 ≤ 3 且每文档实体数 ≤ 5 时 DFA 状态数为多少）；(3) 将 proof sketch 扩展到至少引用 pumping lemma 的核心直觉。

**N2** [critical] κ-DR 相关性声明在统计上无效（n=3, p=0.138）

- 具体位置：Section 5, page 5（"schema restrictiveness–enforcement difficulty relationship is based on three schemas"）; Appendix C, Figure 2, page 19-20
- 问题：论文声称 constraint tightness κ 与 DR reduction 存在相关关系，但这基于 **仅 3 个数据点**（SciERC κ=0.0201, DocRED κ=0.6×, WikiEvents），p=0.138 远未达到显著性。论文在 page 5 称其为"descriptive characterization rather than a confirmatory statistical test"，但仍将其作为 Section 5 正文的核心观察呈现，且在 Figure 2（Appendix C）中用回归线拟合 3 个点。3 个点的回归本质上是过拟合（2 个参数拟合 3 个点），没有统计意义。
- 为什么影响接收：在正文中呈现 underpowered 的统计关系，即使附带 caveat，也容易被读者误解为有证据支撑的结论。这降低了论文统计方法论的整体可信度。
- 建议修改方向：(1) 将 κ-DR 关系明确定性为"observation on three schemas, insufficient for statistical inference"；(2) 移除 Figure 2 的回归线或标注"illustrative only, n=3"；(3) 在 Limitations 中明确承认 schema 数量不足以建立 κ-DR 的定量关系。

**N3** [critical] 70B 验证存在双重缺陷：单一模型族 + 无 FP16 基线

- 具体位置：Table 2 (page 6); Table 18-20 (Appendix D, pages 25-26); Limitations page 9 line "70B experiments use AWQ INT4 quantization"
- 问题：(a) 70B 实验仅使用 Llama-3.1-70B-Instruct（AWQ INT4），无 Qwen-70B 或其他模型族。论文在 Section 2（page 2, contribution 2）声称"comprehensive evaluation across 4 models"，但 70B 仅有 1 个模型，且与 8B 模型属于不同量化精度，严格来说是 3 个 FP16 8B 模型 + 1 个 INT4 70B 模型。(b) 70B 无 FP16 对比——论文在 Limitations（page 9）承认"a direct 70B FP16 comparison exceeds our hardware capacity"，但 Appendix Q（Table 48, page 38）仅对 8B 模型做了 FP16 vs INT4 对比。这意味着我们无法分离 70B 结果中量化伪影与模型规模效应。(c) S2 在 70B 上退化 -8.45pp（Table 2），论文归因于"over-constraining inducing cascading generation degradation"，但这是 post-hoc 解释，未提供消融证据说明为什么过约束在 70B 上比 8B 更严重。
- 为什么影响接收：70B 是论文"scale 鲁棒性"claim 的关键支撑。单一模型族 + 单一量化精度使该 claim 仅是一个初步观察，而非经过验证的结论。S2 退化的 ad hoc 解释进一步削弱可信度。
- 建议修改方向：(1) 将 70B 结果明确定位为 preliminary/pilot（类似 WikiEvents 的处理方式），而非作为主要 claim 的支撑；(2) 至少提供一个替代模型族（Qwen2.5-72B）或明确解释为何不可行；(3) 为 S2 在 70B 退化提供更具机制性的解释（例如，70B 的 tokenizer 分辨率与 8B 不同导致过约束？）。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] First-seen semantics 的级联错误影响未被量化

- 具体位置：Section 3.3 (page 4, "Entity registry"); Section 5.1 (page 6, "CF is the sole residual violation type"); Table 5 (Appendix C, page 18, "Fallback causal tracing")
- 问题：Entity registry 的 first-seen semantics 意味着如果模型首次为某实体分配了错误类型，后续所有引用该实体的 triple 都会被约束到错误类型。论文在多处承认了这一限制（CF 分析、fallback 分析），但未直接量化：(a) first assignment 的错误率是多少？(b) 错误的 first assignment 导致了多少后续 violation？Table 5 给出了 fallback 触发率（0.46%），但这与 first-seen 错误不完全对应。
- 建议：在错误分析中增加一个统计：在所有多次出现的实体中，first-seen type 与 gold type 不一致的比例。

**W2** [warning] WikiEvents n=20 结果的呈现方式可能误导

- 具体位置：Section 5.2, page 7 (Table 3); Appendix G, page 30 (power analysis)
- 问题：WikiEvents 评估仅用 20 个测试文档，MDE=5.8pp。论文在 page 7 承认"wide CIs consistent with no comparison reaching significance"，但 Table 3 仍在正文中占据与 SciERC/DocRED 同等位置，且 Section 5.2 标题为"Preliminary Event Extraction Pilot"。读者可能仍会将 Table 3 的数字视为可靠估计。此外 page 30 的 200-document power analysis 使用的是不同子集，而非实际评估集。
- 建议：(1) 在 Table 3 标题或脚注中明确标注"underpowered; all comparisons are non-significant"；(2) 考虑将 WikiEvents 结果完全移至 Appendix，正文仅用一句话概述。

**W3** [warning] GCD-equiv 等价性验证仅在单一模型上进行

- 具体位置：Appendix (Table 15-17, page 24); Section 5.1, page 6 ("GCD-equiv row")
- 问题：论文声称 trie-only baseline 功能等价于 GCD (Geng et al., 2022)，但等价性验证仅在 Qwen3-8B 上进行（Table 15-17, all metrics differ <0.5pp vs vLLM CFG enforcement）。未在 Llama-3.1-8B 或 70B 上验证。如果不同模型的 tokenizer 导致 trie 匹配行为差异，等价性可能不成立。
- 建议：至少在一个额外模型上验证 GCD-equiv 行为一致性，或明确标注"equivalence validated on Qwen3-8B only"。

**W4** [warning] LoRA 超参从 SciERC 直接转移到 DocRED 缺乏论证

- 具体位置：Section 5 setup (page 5, "LoRA fine-tuning on §1"); Appendix G (page 29, "rank=16, α=32, dropout 0.05")
- 问题：LoRA 超参（rank=16, α=32, dropout 0.05）在 SciERC 上选定后直接用于 DocRED，未进行任何超参搜索或敏感性分析。SciERC（7 entity types, 96 relation types, 551 docs）和 DocRED（6 entity types, 96 relations, 998 docs）在 schema 复杂度和数据规模上不同，最优超参可能不同。论文的 fine-tuning 比较（Table 2）中 DocRED 的结果可能受次优超参影响。
- 建议：(1) 在 Appendix 中增加 DocRED 上的 LoRA rank/α 敏感性分析（即使只测 2-3 个配置）；(2) 或在正文中承认超参转移可能低估 DocRED fine-tuning 的潜力。

**W5** [warning] Beam search 作为 CF 解决方案的实用性讨论不足

- 具体位置：Section 5.2, page 7; Appendix E, pages 26-28 (Figure 4, Table 23-27)
- 问题：Beam search 被提出作为 CF 的部分解决方案（CF reduction 74-86%），但伴随显著延迟开销（constrained beam k=4: 1.54× latency, Table 28/page 29）。对于生产环境中的 IE pipeline，这个 trade-off 的实用性未被讨论。此外，beam search 的 CF 改善在 fine-tuning 后（CF 已降至 0.11%）是否仍有价值？论文未讨论 beam search + fine-tuning 的组合效果。
- 建议：在讨论 beam search 时明确指出其最佳使用场景（zero-shot + 高 CF 率），以及 fine-tuning 后 beam search 的边际收益可能不值得延迟代价。

---

## 小问题（不影响接收）

1. **Abstract 表述略有 overstate**：Abstract 称"near-complete DR elimination"（DR < 0.19%），但这仅在 LoRA fine-tuning 下成立（Table 1, S1 配置）。Zero-shot 下 DR 从 15.4% 降至 2.4%（SciERC, Table 1），虽然显著但非"near-complete"。建议在 Abstract 中区分 zero-shot 和 fine-tuning 结果。

2. **Figure 1 信息密度高但标注略拥挤**：Figure 1（page 3）同时展示了三级类型约束、两层架构、mask 组合逻辑，对首次阅读的读者来说可能难以消化。建议考虑拆分为两个图或增加子图标签。

3. **Appendix 结构可改善**：39 页附录包含 Appendix A-R，部分附录的交叉引用关系复杂（如 Appendix C 同时引用 Table 5, 6, 8, 9, 10 和 Figure 2），建议在附录开头增加一个导航索引。

4. **"Engineering applicability" 段落位置突兀**：该段紧接 Proposition 1 proof sketch 后出现（page 3），但在形式论证和工程论证之间缺少过渡，读者可能不清楚这段是证明的一部分还是独立的讨论。

5. **Table 2 的 CF 列含义需要更早解释**：Table 2（page 6）中 CF 列在 Section 5.1 第二段才被解释，但读者在看到 Table 2 时已需要理解 CF 的含义。

---

## 需要作者回答的问题

**Q1**: Proposition 1 的证明依赖于 position-based entity indexing（Appendix O, page 37, "Position indexing vs. name referencing"）。论文承认这是一个简化，但声称不影响结论。能否提供更正式的论证说明 name-based referencing 不会使语言变为 context-free？

**Q2**: Table 1 的 Semantic-only 行显示 grammar 层缺失时 DR 仍有 24% 独立降低，但 RV（relation vocabulary violations）从 1.76 增至 4.76。这意味着语义层在没有 grammar 层时引入了更多词汇违规？如果是，这对"enabling dependency" claim 有什么影响？

**Q3**: 70B S2 退化 -8.45pp 的根本原因是什么？论文归因于"over-constraining"，但 8B 模型上 S2 表现与 S1 相当（Table 1）。是否有证据表明 70B 的 tokenizer 粒度或 INT4 量化加剧了过约束效应？

**Q4**: Grammar-first fallback 在 0.46% 的 first-token positions 触发（Table 5），但论文未报告 fallback 对最终 F1 的影响。Fallback 触发的 triple 中有多少最终产生了正确输出？如果 fallback 总是导致错误输出，0.46% 的触发率在 SciERC（平均 ~13 triples/doc）中意味着约 6% 的文档受影响。

**Q5**: Per-relation DR elimination（Table 9-10）显示 fine-tuning 后 EVALUATE-FOR 仍有非零 violation（κ=0.361）。这是否说明当 relation 的 domain/range 约束特别松（κ 低）时，语义层的优势被削弱？

---

## Missing References

1. **Willard and Louf (2023)** 和 **Beurer-Kellner et al. (2023)** 已被引用，但论文未讨论 **Outlines** 近期的 structured generation 改进（如 regex-based 约束 + jump-forward optimization），这与 OntoCoDec 的 grammar layer 在技术路线上高度相关。

2. 论文在 Related Work（Section 6, page 8）中讨论了 GoLLIE 但未提及 **NuneroPlan (Zhu et al., 2024)** 等使用 planning-based 方法实现结构化 IE 的工作，这类方法提供了约束执行的替代范式。

3. **Dong et al. (2024), "Generative IE with grounded generation"** 等使用 retrieval-augmented generation 实现 schema-compliant IE 的工作未被讨论，这些方法通过 grounding 而非 constrained decoding 实现类型约束，提供了有价值的对比视角。

---

## Overall Assessment

**评分**: 3.5 / 5 (Borderline Conference)

**理由**：论文提出了一个有清晰理论动机（Proposition 1）和系统实验验证的两层约束解码框架，核心贡献（编译 IE 本体为 token 级解码约束）新颖且有实践意义。五路消融设计系统，统计方法论在主要实验上严谨（Bonferroni CI、bootstrap、effect size），30 页附录展现了高度的科学诚实度。

主要顾虑集中在三点：(1) 若干统计声明建立在 underpowered 数据上（κ-DR n=3 相关性在正文中的呈现方式不当），(2) 70B 验证的覆盖度不足以支撑论文关于规模鲁棒性的 claim，(3) Proposition 1 在有限实体集场景下的适用性依赖工程论证而非形式结果，正文 proof sketch 过于简略。这些问题均可在修改中解决，但在当前版本中限制了论文的说服力。

如果 N1-N3 的 must-fix 问题在 revision 中得到充分回应（特别是明确 Proposition 1 的适用边界、修正 κ-DR 声明的呈现方式、将 70B 结果定位为 preliminary），评分可上调至 4.0。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 2442 · 2026-05-23T09:28:37.887239+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "## 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见\n\n以下是 Reviewer 2 的完整审稿意见。请逐条回应：对每个 Must-Fix 和 Should-Fix 问题，标注 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 审稿意见（Overall: 3.0 Findings）\n\n### Must-Fix\n\n**N1** [critical] Proposition 1 的理论贡献被高估，不构成实质性 novelty\n- PDA 无法对无界序列进行随机访问是自动机理论基础知识。论文自身承认这是 \"well-known intuition\" 的形式化，但将其包装为核心理论贡献（\"theoretical grounding\"）并作为 Contribution 1 的一部分呈现，夸大了其学术新颖性。\n- 如果 theoretical grounding 是 trivial 的，整体贡献降级为纯工程贡献。对于 EMNLP main，纯系统集成工作（XGrammar + stateful logits processor）的 novelty bar 更难满足。\n\n**N2** [critical] 缺乏与强 baseline 的公平对比\n- \"constrained baseline\" 比较仅限于 grammar-only（3% DR reduction 的 strawman）。未与 GoLLIE、KnowCoder、post-hoc type repair 做可比实验。无法判断 OntoCoDec 相对于 SOTA schema-aware IE 系统的实际优势。\n\n**N3** [critical] R-F1 41–47% 的绝对质量缺乏上下文定位\n- R-F1 41–47% 未与 SciERC/DocRED 上的 SOTA（SpanBERT/PL-Marker 50%+, DocRED 60%+）对比。在如此低的 F1 下讨论 0.09% DR 的实际意义需要更多论证。\n\n### Should-Fix\n\n**W1** WikiEvents pilot 篇幅与贡献不匹配（n=20, MDE≈±5pp, \"directional only\"，半页空间浪费）\n**W2** CF 违规作为 \"可修正副作用\" 的叙事过于乐观（zero-shot CF 高达 12%，可能增加总体错误率）\n**W3** §7 Discussion 仅 8 行，过于压缩\n**W4** 约束来源模糊（SciERC/DocRED 约束来自训练数据，非形式本体）削弱 \"ontology-compiled\" 框架\n**W5** Contribution 2 过度打包（一个 bullet 包含过多内容）\n\n### Missing References\n1. SciDC (arXiv:2604.06603, Apr 2026)\n2. Dialogue Ontology RE via Constrained CoT (arXiv:2408.02361)\n3. KG-Trie (arXiv:2410.13080)\n4. Format Tax 原始论文 (arXiv:2604.03616, 2026) 需核实是否与已引用的 FormaTax 为同一工作\n\n---\n\n**请逐条回应每个 N 和 W 问题，以及 Missing References。**",
  "project": "schema_semantic_constrained_ie",
  "chat_id": "oc_01fc90ae186a4ed432770f7601995139",
  "director_session_key": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "## 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见\n\n以下是 Reviewer 2 的完整审稿意见。请逐条回应：对每个 Must-Fix 和 Should-Fix 问题，标注 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 审稿意见（Overall: 3.0 Findings）\n\n### Must-Fix\n\n**N1** [critical] Proposition 1 的理论贡献被高估，不构成实质性 novelty\n- PDA 无法对无界序列进行随机访问是自动机理论基础知识。论文自身承认这是 \"well-known intuition\" 的形式化，但将其包装为核心理论贡献（\"theoretical grounding\"）并作为 Contribution 1 的一部分呈现，夸大了其学术新颖性。\n- 如果 theoretical grounding 是 trivial 的，整体贡献降级为纯工程贡献。对于 EMNLP main，纯系统集成工作（XGrammar + stateful logits processor）的 novelty bar 更难满足。\n\n**N2** [critical] 缺乏与强 baseline 的公平对比\n- \"constrained baseline\" 比较仅限于 grammar-only（3% DR reduction 的 strawman）。未与 GoLLIE、KnowCoder、post-hoc type repair 做可比实验。无法判断 OntoCoDec 相对于 SOTA schema-aware IE 系统的实际优势。\n\n**N3** [critical] R-F1 41–47% 的绝对质量缺乏上下文定位\n- R-F1 41–47% 未与 SciERC/DocRED 上的 SOTA（SpanBERT/PL-Marker 50%+, DocRED 60%+）对比。在如此低的 F1 下讨论 0.09% DR 的实际意义需要更多论证。\n\n### Should-Fix\n\n**W1** WikiEvents pilot 篇幅与贡献不匹配（n=20, MDE≈±5pp, \"directional only\"，半页空间浪费）\n**W2** CF 违规作为 \"可修正副作用\" 的叙事过于乐观（zero-shot CF 高达 12%，可能增加总体错误率）\n**W3** §7 Discussion 仅 8 行，过于压缩\n**W4** 约束来源模糊（SciERC/DocRED 约束来自训练数据，非形式本体）削弱 \"ontology-compiled\" 框架\n**W5** Contribution 2 过度打包（一个 bullet 包含过多内容）\n\n### Missing References\n1. SciDC (arXiv:2604.06603, Apr 2026)\n2. Dialogue Ontology RE via Constrained CoT (arXiv:2408.02361)\n3. KG-Trie (arXiv:2410.13080)\n4. Format Tax 原始论文 (arXiv:2604.03616, 2026) 需核实是否与已引用的 FormaTax 为同一工作\n\n---\n\n**请逐条回应每个 N 和 W 问题，以及 Missing References。**",
    "project": "schema_semantic_constrained_ie",
    "chat_id": "oc_01fc90ae186a4ed432770f7601995139",
    "director_session_key": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director"
  }
}
```

</details>

---


### Tool result

_source line 2443 · 2026-05-23T09:29:01.048701+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 23161
}
```

</details>

---


### Tool call

_source line 2444 · 2026-05-23T09:29:01.451214+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "## 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见\n\n以下是 Reviewer 1 的完整审稿意见。请逐条回应：对每个 Must-Fix 和 Should-Fix 问题，标注 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 审稿意见（Overall: 3.5 Borderline Conference）\n\n### Must-Fix\n\n**N1** [critical] Proposition 1 的理论-实践 gap 处理不够清晰\n- Proposition 1 证明无界实体集时 domain/range 约束非 context-free。但实际 IE 中实体集有限。\"Engineering applicability\" 段落用计算复杂度论证（DFA >10^17 states）桥接，但这是复杂度论证而非形式不可能性。论文未讨论 DFA 变得可行的边界条件。\n- 建议：正文中明确区分理论不可能性（无界）和实际不可行性（有界但指数级）；给出 DFA 可行的边界条件。\n\n**N2** [critical] κ-DR 相关性声明在统计上无效（n=3, p=0.138）\n- 仅 3 个数据点，p=0.138 远未达显著性。虽标注 \"descriptive\"，但仍在正文中作为核心观察呈现，Figure 2 用回归线拟合 3 个点本质上是过拟合。\n- 建议：明确定性为 insufficient for statistical inference；移除回归线或标注 illustrative only。\n\n**N3** [critical] 70B 验证：单一模型族 + 无 FP16 基线\n- 70B 仅 Llama-3.1-70B-Instruct (AWQ INT4)，无 Qwen-70B。S2 退化 -8.45pp 的解释是 post-hoc 的。Contribution 2 声称 \"4 models\" 但 70B 仅 1 个且不同精度。\n- 建议：将 70B 定位为 preliminary；为 S2 退化提供机制性解释。\n\n### Should-Fix\n\n**W1** First-seen semantics 的级联错误影响未量化（first assignment 错误率？导致多少后续 violation？）\n**W2** WikiEvents n=20 结果呈现方式可能误导（Table 3 在正文中占据与 SciERC/DocRED 同等位置）\n**W3** GCD-equiv 等价性验证仅在单一模型上进行\n**W4** LoRA 超参从 SciERC 直接转移到 DocRED 缺乏论证\n**W5** Beam search 作为 CF 解决方案的实用性讨论不足\n\n### Questions\n**Q1**: Name-based referencing 是否使语言变为 context-free？\n**Q2**: Semantic-only 行中 RV 从 1.76 增至 4.76，语义层引入更多词汇违规？\n**Q3**: 70B S2 退化根本原因？\n**Q4**: Fallback 触发的 triple 中有多少产生正确输出？\n**Q5**: EVALUATE-FOR 非零 violation（κ=0.361）是否说明低 κ 时语义层优势被削弱？\n\n### Missing References\n1. Outlines 近期 structured generation 改进（regex-based + jump-forward optimization）\n2. NuneroPlan (Zhu et al., 2024) planning-based 结构化 IE\n3. Dong et al. (2024) retrieval-augmented generation 实现 schema-compliant IE\n\n---\n\n**请逐条回应每个 N 和 W 问题，以及 Questions 和 Missing References。**",
  "project": "schema_semantic_constrained_ie",
  "chat_id": "oc_01fc90ae186a4ed432770f7601995139",
  "director_session_key": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "## 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见\n\n以下是 Reviewer 1 的完整审稿意见。请逐条回应：对每个 Must-Fix 和 Should-Fix 问题，标注 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 审稿意见（Overall: 3.5 Borderline Conference）\n\n### Must-Fix\n\n**N1** [critical] Proposition 1 的理论-实践 gap 处理不够清晰\n- Proposition 1 证明无界实体集时 domain/range 约束非 context-free。但实际 IE 中实体集有限。\"Engineering applicability\" 段落用计算复杂度论证（DFA >10^17 states）桥接，但这是复杂度论证而非形式不可能性。论文未讨论 DFA 变得可行的边界条件。\n- 建议：正文中明确区分理论不可能性（无界）和实际不可行性（有界但指数级）；给出 DFA 可行的边界条件。\n\n**N2** [critical] κ-DR 相关性声明在统计上无效（n=3, p=0.138）\n- 仅 3 个数据点，p=0.138 远未达显著性。虽标注 \"descriptive\"，但仍在正文中作为核心观察呈现，Figure 2 用回归线拟合 3 个点本质上是过拟合。\n- 建议：明确定性为 insufficient for statistical inference；移除回归线或标注 illustrative only。\n\n**N3** [critical] 70B 验证：单一模型族 + 无 FP16 基线\n- 70B 仅 Llama-3.1-70B-Instruct (AWQ INT4)，无 Qwen-70B。S2 退化 -8.45pp 的解释是 post-hoc 的。Contribution 2 声称 \"4 models\" 但 70B 仅 1 个且不同精度。\n- 建议：将 70B 定位为 preliminary；为 S2 退化提供机制性解释。\n\n### Should-Fix\n\n**W1** First-seen semantics 的级联错误影响未量化（first assignment 错误率？导致多少后续 violation？）\n**W2** WikiEvents n=20 结果呈现方式可能误导（Table 3 在正文中占据与 SciERC/DocRED 同等位置）\n**W3** GCD-equiv 等价性验证仅在单一模型上进行\n**W4** LoRA 超参从 SciERC 直接转移到 DocRED 缺乏论证\n**W5** Beam search 作为 CF 解决方案的实用性讨论不足\n\n### Questions\n**Q1**: Name-based referencing 是否使语言变为 context-free？\n**Q2**: Semantic-only 行中 RV 从 1.76 增至 4.76，语义层引入更多词汇违规？\n**Q3**: 70B S2 退化根本原因？\n**Q4**: Fallback 触发的 triple 中有多少产生正确输出？\n**Q5**: EVALUATE-FOR 非零 violation（κ=0.361）是否说明低 κ 时语义层优势被削弱？\n\n### Missing References\n1. Outlines 近期 structured generation 改进（regex-based + jump-forward optimization）\n2. NuneroPlan (Zhu et al., 2024) planning-based 结构化 IE\n3. Dong et al. (2024) retrieval-augmented generation 实现 schema-compliant IE\n\n---\n\n**请逐条回应每个 N 和 W 问题，以及 Questions 和 Missing References。**",
    "project": "schema_semantic_constrained_ie",
    "chat_id": "oc_01fc90ae186a4ed432770f7601995139",
    "director_session_key": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director"
  }
}
```

</details>

---


### Tool result

_source line 2445 · 2026-05-23T09:29:02.873083+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1421
}
```

</details>

---


### Assistant

_source line 2446 · 2026-05-23T09:29:12.342422+00:00_

交叉分享已发送。等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director"
}
```

</details>

---


## Round 176

## Round 176

2 recorded events


### User

_source line 2447 · 2026-05-23T09:29:14.966576+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

**审稿摘要**：

- **Overall: 3.5 / 5 (Borderline Conference)**
- 论文核心贡献（两层约束解码框架 + Proposition 1 形式化）新颖且有价值，五路消融设计系统，统计方法论在主要实验上严谨
- **3 个 Must-Fix 问题**：(1) Proposition 1 在有限实体集下的 gap 处理不够清晰——正文 proof sketch 过于简略，理论不可能性与工程不可行性需明确区分；(2) κ-DR 相关性 n=3, p=0.138 在正文中的呈现方式不当，统计上无效；(3) 70B 验证仅覆盖 Llama 单一模型族且无 FP16 基线，S2 退化 -8.45pp 的解释是 post-hoc 的
- **5 个 Should-Fix 问题**：first-seen semantics 级联错误未量化、WikiEvents n=20 呈现方式可能误导、GCD-equiv 等价性验证仅单模型、LoRA 超参跨数据集转移缺乏论证、beam search 实用性讨论不足
- 如果 N1-N3 在 revision 中充分回应，评分可上调至 4.0

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 2448 · 2026-05-23T09:29:19.549017+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director"
}
```

</details>

---


## Round 177

## Round 177

2 recorded events


### User

_source line 2449 · 2026-05-23T09:32:48.938988+00:00_

[Reviewer 1 审稿意见]:

## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应

---

### Must-Fix 问题

---

**[REBUT] R2-N1: Proposition 1 的理论贡献被高估，不构成实质性 novelty**

R2 认为 PDA 无法做随机访问是"自动机理论基础知识"，因此 Proposition 1 trivial。我不完全同意这个判断。

理由：

1. **贡献不仅是 Proposition 1 本身，而是三级可判定性分类**。Section 3（page 3）将 IE 类型约束分为三级：(1) context-free（词汇+结构），(2) prefix-decidable with state（domain/range），(3) non-local（cross-field consistency）。这个分类法为 IE 约束解码的架构设计提供了系统性指导——哪些约束用 CFG 层处理、哪些需要有状态运行时、哪些无法在线解决。我不认为这在现有文献中已被明确建立。

2. **Engineering applicability 段落（page 3）提供了有价值的桥接**。论文不仅证明了无界情况的不可能性，还量化了有界情况的不可行性（DocRED: O(|T|^{|states|}) > 10^{17}），这超出了"基础知识"范畴——它将理论结果连接到了实际系统设计决策。

3. **但我同意 proof sketch 在正文中确实过于简略**（我在 R1-N1 中已指出），且论文对 Proposition 1 的定位可以更谦虚。建议将其明确定位为"formalizing a known intuition for the specific IE setting"，而非暗示它是全新的理论发现。

4. **"纯工程贡献"的判断过于严厉**。论文的核心贡献包含三个层面：形式分析（分类法）、系统设计（两层架构）、和实证验证（五路消融+统计检验）。即使 Proposition 1 的证明技术本身是标准的，将其应用于 IE 约束解码并据此设计出可工作的系统，仍然是有意义的科学贡献。EMNLP 并不要求理论证明必须是全新的形式技术——关键是理论分析是否指导了有效的系统设计。

**结论**：Proposition 1 的 novelty 确实不应被过度宣传，但 R2 将论文降格为"纯系统集成"忽略了可判定性分类法和形式化分析对架构设计的指导作用。

---

**[REBUT] R2-N2: 缺乏与强 baseline 的公平对比**

R2 声称论文仅与 grammar-only strawman 比较。这不准确——论文实际提供了多层次对比，只是分散在正文和附录中。

论文中已有的对比：

1. **GCD-equiv baseline（Table 15-17, Appendix, page 24）**：论文实现了 trie-only baseline 并与 vLLM 的 CFG enforcement 进行外部验证（all metrics differ < 0.5pp），证明 grammar-only 约束等价于 GCD（Geng et al., 2022）的效果。这不是 strawman——GCD 是该领域的代表性方法。

2. **Post-hoc filtering 完整对比（Table 12, page 22）**：论文在 6 个模型-数据集配置上对比了 constrained decoding vs. post-hoc filtering，显示 post-hoc 在 zero-shot 下 reject >70% 的预测（过于激进），在 fine-tuned 下 recall drops from 0.46 to 0.20（Table 12）。这是与 post-hoc type repair 的公平对比。

3. **GoLLIE-7B 直接对比（Appendix R, Table 49, page 38-39）**：论文在 SciERC 100 docs 上对比了 GoLLIE-7B 与 OntoCoDec。GoLLIE-7B 仅生成 5 个 predicted relations（54% 文档产生空输出），而 OntoCoDec 产出 ~200× 更多预测且 DR=0%。论文正确指出 GoLLIE 的 code-style schema encoding 与 JSON evaluation protocol 不兼容，且无公开 LoRA checkpoint——这是方法论上的不可比性，不是论文回避比较。

4. **Schema-informed prompting baseline（Section 5, page 5）**：论文报告 schema-informed prompting reduces DR by 62% on average（Table C），但 per-relation 不可靠。

R2 的核心关切——"无法判断 OntoCoDec 相对于 SOTA schema-aware IE 系统的实际优势"——混淆了两类工作的目标。OntoCoDec 是一个 **约束执行方法**（decoding-time enforcement），不是一个 **IE 系统**。它与 GoLLIE/KnowCoder 的区别在于：后者通过 training-time schema internalization 实现约束，前者通过 decoding-time mask 实现约束。两者是互补的（Section 7, page 8："Constraint enforcement is preserved under INT4 quantization"）。要求 OntoCoDec 在 R-F1 上击败 GoLLIE 相当于要求一个 type checker 在代码质量上击败一个 code generator。

**但我同意论文可以更清晰地框定这个定位**。正文应在 Section 1 或 5 中明确声明："OntoCoDec is a constraint enforcement method, not an IE system; it is complementary to, not competitive with, training-based schema-aware methods."

---

**[REBUT] R2-N3: R-F1 41–47% 的绝对质量缺乏上下文定位**

R2 将 OntoCoDec 的 R-F1 与 SpanBERT/PL-Marker (50%+) 对比并质疑实际意义。我认为这个对比不恰当。

1. **论文已提供上下文**（Appendix C, page 20）："For reference, supervised state-of-the-art systems on SciERC achieve approximately 49–53% relation F1." 这表明作者有意识地定位了绝对质量。

2. **任务设置根本不同**。SpanBERT/PL-Marker 是 supervised span-based 方法，使用 task-specific 架构和完整训练集。OntoCoDec 评估的是 generative LM 在 zero-shot/few-shot 设置下的 IE 能力——R-F1 41-47% 在 zero-shot generative IE 中是合理的水平。论文的 fine-tuned 结果（LoRA, Table 2）达到 R-F1 45.47%（SciERC）和 43.95%（DocRED），已接近 supervised 方法。

3. **约束执行的价值与绝对 F1 独立**。即使 R-F1 是 30%，如果其中 15% 的预测有 domain/range violation，约束执行仍然有价值——它确保输出是 schema-valid 的，可以直接导入知识图谱。论文在 Appendix F（page 29-30, Table 39）量化了下游影响：constraint-removed triples 仅 0.49% match gold labels，说明 DR violations 几乎全是错误预测。

4. **R2 引用的 DocRED 60%+ 是 development set 的 supervised 结果**，与论文的生成式 zero-shot 设置完全不可比。

**结论**：R-F1 41-47% 在论文的 zero-shot/LoRA fine-tuning 设置下是合理的。要求与 supervised span-based 方法对标是不恰当的。但我同意论文应在正文（而非仅在 Appendix）中明确定位这个绝对质量水平。

---

### Should-Fix 问题

---

**[AGREE] R2-W1: WikiEvents pilot 篇幅与贡献不匹配**

同意。我在 R1-W2 中已提出相同关切。n=20, MDE≈±5pp, 所有对比均未达显著性——半页正文空间用于呈现 underpowered 的结果是不经济的。建议将 Table 3 移至 Appendix，正文用 1-2 句话概述 pilot 结论。

---

**[AGREE] R2-W2: CF 违规作为"可修正副作用"的叙事过于乐观，但需要修正 R2 的部分表述**

R2 指出 zero-shot CF 高达 12%。这个数字需要核实——查看 Table 1（page 6），S1 zero-shot 的 CF 是 4.23%（不是 12%）。unconstrained 的 CF 是 3.06%，S1 将 CF 从 3.06% 增至 4.23%，增加约 1.17pp。这确实表明 S1 引入了额外的 CF 违规（因为 DR 被消除后，部分冲突重新路由为 CF），但幅度远没有 12% 那么大。

然而，我同意论文对 CF 的叙事可以更平衡。Section 5.1（page 6）的 "cross-field violation analysis" 虽然详细讨论了 CF，但 §7 Discussion（page 8）总结时仍以正面 framing 为主（"near-complete DR elimination"），对 CF trade-off 的提及仅一句话。建议在 Discussion 中增加一段明确讨论 DR↔CF trade-off 的定量影响。

---

**[AGREE] R2-W3: §7 Discussion 仅 8 行过于压缩**

同意。在 8 页限制下压缩是可以理解的，但 Discussion 应至少覆盖：(1) DR↔CF trade-off 的含义，(2) 约束执行对下游 KG 质量的影响，(3) 与 training-based schema enforcement 的互补关系。当前的 8 行缺乏深度。如果空间不足，可以压缩 Related Work（当前 page 7-8 占约 1.5 页，偏长）来为 Discussion 腾出空间。

---

**[REBUT] R2-W4: 约束来源模糊削弱"ontology-compiled"框架**

R2 认为 SciERC/DocRED 约束来自训练数据而非形式本体，因此"ontology-compiled"措辞不当。我部分不同意。

1. **SciERC 的类型系统确实来自形式定义**——SciERC 的 7 entity types 和 relation types 有明确的 domain/range 定义（Section 5, page 5："RE type constraints are extracted from observed type pairs in training data"），但这些 type pairs 反映的是 SciERC 标注规范中的本体结构，不是任意统计共现。

2. **WikiEvents 明确使用形式本体**——Section 5, page 5："IE constraints on WikiEvents (§5.2) derive from the KAIROS ontology." KAIROS 是 LDC 定义的形式事件本体。

3. **但 R2 确实指出了一个合理关切**：从 training data 提取的约束可能不完整——Limitations（page 9, line 74）承认"schema gaps arise from training-data-derived constraints that may not cover all valid type pairs"。这确实与"ontology-compiled"的强措辞存在张力。

**建议**：论文应在 Section 3 中更明确地区分两种约束来源：(a) 形式本体（如 KAIROS），(b) 从标注数据推导的 schema（如 SciERC/DocRED），并讨论后者的不完整性风险。但将整个框架改名似乎不必要——"ontology"在 IE 文献中常用来指代类型系统，即使其来源不是形式本体。

---

**[AGREE] R2-W5: Contribution 2 过度打包**

同意。page 2 的 Contribution 2 将"4 models, 2 precisions, 2 datasets, up to 96 relations, preliminary event extraction pilot, comprehensive evaluation"打包在一个 bullet 中，读者难以解析。建议拆分为 2-3 个子项，分别覆盖：(a) 消融设计，(b) cross-model/cross-dataset 验证，(c) 统计方法论。这是纯呈现问题，不影响实质贡献。

---

### Missing References

---

**SciDC (arXiv:2604.06603, Apr 2026)**：我无法验证此引用的真实性（2026 年 4 月 arXiv 论文）。如果该工作确实存在且涉及 schema-constrained decoding for IE，则应被讨论。建议 Director 要求 R2 提供更完整的引用信息（标题、作者）以便验证。

**Dialogue Ontology RE via Constrained CoT (arXiv:2408.02361)**：如果此工作将 constrained chain-of-thought 应用于 ontology-guided RE，则与 OntoCoDec 的 decoding-time enforcement 形成方法论对比，值得在 Related Work 中讨论。

**KG-Trie (arXiv:2410.13080)**：如果此工作使用 trie 结构进行 KG completion 的约束解码，则与 OntoCoDec 的 grammar layer（同样基于 trie/CFG）技术路线相关，应被引用。

**Format Tax (arXiv:2604.03616, 2026)**：R2 要求核实是否与已引用的 FormaTax 为同一工作。论文确实引用了 "FormaTax"（page 7, Related Work 区域提到 format tax 概念），但 2026 年 4 月的 arXiv 编号需要验证。如果是不同工作，应分别引用。

**总体评价**：R2 的 Missing References 中有 2 个是 2026 年 4 月的 arXiv 论文。考虑到论文的投稿时间线，这些工作可能在论文完成后才发表，属于 concurrent work 而非遗漏。建议 Director 验证这些引用的时间线。

---

### 对 R2 Overall 评分（3.0 Findings）的看法

R2 给出 3.0 的主要理由是：(1) Proposition 1 trivial，(2) 缺强 baseline，(3) 绝对 F1 低。我认为这三个理由均部分站不住脚：

- Proposition 1 的价值不在于证明技术本身的新颖性，而在于可判定性分类法对系统设计的指导
- 论文已提供 GCD-equiv、post-hoc filtering、GoLLIE 三类对比，R2 的"仅与 strawman 比较"不准确
- 绝对 F1 的对比标准不恰当——论文是约束执行方法，不是 IE 系统

我维持 R1 的 3.5 评分（Borderline Conference），认为 R2 的 3.0 偏低。论文的核心贡献——将 IE 本体约束编译为可组合的 token 级解码约束并提供系统实证验证——在方法论贡献上超过了 Findings 门槛。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 2450 · 2026-05-23T09:32:54.735227+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director"
}
```

</details>

---


## Round 178

## Round 178

10 recorded events


### User

_source line 2451 · 2026-05-23T09:33:01.291457+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 对 Reviewer 1 审稿意见的逐条回应

---

### Must-Fix 问题

**[AGREE] R1-N1: Proposition 1 的理论-实践 gap 处理不够清晰**

同意，且与我的 N1 互补。R1 的角度更精准：问题不仅是 Proposition 1 本身 trivial（我的 N1），而是论文未能妥善桥接理论结果（无界→非 CF）和实际场景（有界→技术上 regular 但 DFA 指数爆炸）。

具体补充：§3 "Engineering applicability" 段（Page 3）声称 DocRED 的 DFA 需要 $O(|\mathcal{E}|^{|\text{entities}|}) > 10^{17}$ states，但未讨论边界条件——当 $|\mathcal{E}|$ 较小且文档实体数有限时（如 SciERC: 6 entity types, 平均约 5-10 entities/sentence），DFA 规模可能是可行的（$6^{10} \approx 6 \times 10^7$）。论文回避了 "在什么条件下简单 DFA 即可替代整个 semantic layer" 这一关键问题，这削弱了两层架构的必要性论证。

R1 的建议（明确区分理论不可能性 vs. 实际不可行性 + 给出 DFA 可行边界）是可操作的，值得采纳。

---

**[AGREE] R1-N2: κ-DR 相关性声明统计无效（n=3, p=0.138）**

同意。我在小问题中也标注了同一 concern（"§4 κ 相关性基于 n=3, p=0.138，不应过度解读"），R1 将其升级为 Must-Fix 是合理的。

补充核实：R1 提到 "Figure 2 用回归线拟合 3 个点"——经检查，主文中仅有 Figure 1（架构图，fig:framework），无 Figure 2。κ 相关的可视化位于附录（fig:dual-factor-scatter, Appendix C Discussion）。**R1 此处引用的图号有误**，但其核心论点成立：用任何形式的回归线/趋势线拟合 3 个数据点都是统计学上无意义的。

论文在 §4 中虽标注了 "descriptive (n=3, p=0.138)"，但仍在 §1 Contribution 2 和 Abstract 中使用 "rates correlate with schema restrictiveness" 的表述（Page 1, Abstract 第 3 段），暗示因果关联。建议：全文统一使用 "observed pattern across three schemas" 而非 "correlation"。

---

**[AGREE] R1-N3: 70B 验证单一模型族 + 无 FP16 基线**

同意。§5 (Page 8) 明确承认 "cross-family generalization at 70B scale remains to be verified"，Limitations (Page 9) 承认 "direct 70B FP16 comparison exceeds our hardware capacity"。论文的诚实性值得肯定，但 Contribution 2 中 "4 models spanning 8B–70B" 的表述确实具有误导性——实际是 "3 个 8B 模型 + 1 个 70B 模型（单一模型族、不同精度）"。

关于 S2 退化：Limitations (Page 9) 给出的解释是 "optimal constraint granularity varies with model capacity"，这是描述性的而非机制性的。R1 要求的 "机制性解释" 合理——一个可能的假设是：70B 模型在单 pass 中已能有效利用 entity-relation 上下文来推断类型，而 S2 的 pipeline 切割人为破坏了这一上下文依赖，导致第二 pass 的类型推断退化。但这需要实验验证（如分析 S2 第二 pass 中 fallback 触发率是否显著上升）。

建议：将 70B 结果明确标注为 "preliminary single-family validation"；拆分 Contribution 2 中 8B 和 70B 的声明层级。

---

### Should-Fix 问题

**[AGREE] R1-W1: First-seen semantics 的级联错误未量化**

这是一个我未充分关注的好问题。§3.3 Entity Registry（Page 4）描述了 first-seen semantics：当实体名首次出现时注册类型，后续所有引用均使用此类型。§5.1 Cross-field violation analysis（Page 6）量化了 CF 违规总数（245 violations, fine-tuned SciERC），但未回答 R1 的核心问题：**第一次类型赋值本身的错误率是多少？每个错误的首次赋值导致多少后续 CF 违规？**

如果首次赋值错误率很低（如 <1%），那么 CF 主要由合法类型歧义驱动（如 Generic↔OtherScientificTerm），first-seen 机制本身不是主要问题；但如果错误率较高，则说明 first-seen 是一个系统性缺陷而非边际效应。论文缺少这一分析。

---

**[AGREE] R1-W2: WikiEvents Table 3 在正文中的位置可能误导**

与我的 W1 一致。Table 3 与 Table 1/2（SciERC/DocRED, 551/998 docs, 完整评估）并列呈现于正文中，但 n=20, MDE≈±5pp 的统计效力完全不在同一量级。视觉上的等同位置暗示证据力度相当，这对读者具有误导性。

---

**[AGREE] R1-W3: GCD-equiv 等价性仅单一模型验证**

同意但认为严重性较低。Table 1 的 GCD-equiv 行（vLLM guided_json）仅用 Qwen3-8B 验证（DR=15.26% vs. Grammar row DR=14.84%）。但 grammar-only row 本身在 cross-model table（Table in Appendix）中跨 3 个模型验证了一致的低 DR 减少（≤3%），间接支持了 GCD-equiv 等价性的 generalizability。建议在脚注中说明。

---

**[AGREE] R1-W4: LoRA 超参从 SciERC 直接转移到 DocRED 缺乏论证**

同意。§5 Setup（Page 5）仅声明 "LoRA hyperparameters were selected on SciERC development data and transferred to DocRED without further tuning"，但 SciERC（7 relations, 551 短句子）与 DocRED（96 relations, 998 长文档）在 schema 复杂度和文本长度上差异巨大。论文未论证为何相同的 LoRA rank/lr/epochs 在两个截然不同的数据集上均适用。R-F1 41–47% 的结果是否部分受限于未针对 DocRED 调优？这影响了对 "constraint enforcement 与 fine-tuning composability" 结论的可靠性。

---

**[AGREE] R1-W5: Beam search 作为 CF 解决方案的实用性讨论不足**

与我的 W2 一致。§5（Page 8）给出 beam S1 的 latency 为 1.54×，但未讨论：(a) beam search 的内存开销（对 70B 模型尤其关键）；(b) 在 production deployment 中是否有比 k=4 beam search 更轻量的 CF 缓解方案（如 TCR post-hoc，但 TCR 效果波动大 18–92%）；(c) beam width 与 CF 消除率的关系（是否 k=2 已足够？）。论文仅呈现 k=4 的结果，缺少 beam width sensitivity analysis。

---

### Questions

**Q1: Name-based referencing 是否使语言变为 context-free？**

[REBUT on behalf of paper] 不会。即使使用 name-based referencing（relation 通过实体名引用 head/tail），enforcement 仍需在生成 head_type token 时查询 "当前 head name 在 entity registry 中注册的类型是什么"——这需要对先前生成的 entity 列表进行随机访问。PDA 的 LIFO stack 无法实现这一操作（需要 pop 到目标 entry，破坏中间状态）。唯一能使语言 context-free 的条件是：entity name 集合和 type assignment 在解码前已知且固定——但这恰好是 IE 中不成立的前提（entities 从文本中动态提取）。论文 §3 Proposition 1 的论证在 name-based referencing 下仍然成立。

**Q2: Semantic-only 行中 RV 增加**

[注意] R1 引用的数据（RV 从 1.76 增至 4.76）与我在 Table 1（Page 6）中读到的数据不符。Table 1 显示：Unconstrained RV=1.39, Semantic RV=1.51——增幅仅 0.12pp。R1 可能引用了附录 cross-model table 中的某个模型数据或记忆有误。

但 R1 的核心问题有效：为什么 semantic layer 不减少反而略增 RV？解释：semantic layer 仅在 type-bearing positions (HeadType, TailType) 施加约束（§3.3, Page 4），不约束 relation/entity vocabulary。RV（relation vocabulary violation, r∉R）完全由 grammar layer 负责（Table 1: Grammar row RV→0）。Semantic-only 模式下 grammar layer 关闭，模型无 vocabulary 约束，RV 略增是可预期的副作用——semantic masking 改变了 token probability distribution，可能微弱地推动模型在 relation position 选择 OOV tokens。这不是一个实质问题，因为实际部署总是 S1（两层联合）。

**Q3: 70B S2 退化根本原因？**

同意 R1 的关切——见我对 R1-N3 的回应。论文缺少机制性解释。

**Q4: Fallback 触发的 triple 中有多少产生正确输出？**

好问题。§4（Page 5）指出 "all residual DR occurs at fallback positions"，§5.1（Page 6）指出 "removed triples are 97.6–100% false positives"。但这两个数据点分别描述不同的东西：前者说 fallback 是 DR 的唯一来源；后者说被约束移除的 triples 几乎都是 false positives。论文未直接回答 "fallback triple 中有多少最终产生了正确抽取"——这需要交叉分析 fallback events 与 gold labels 的重合度。如果 fallback triples 的 precision 很低，则 fallback 机制的代价可接受；反之则说明 grammar-first fallback 过于激进。这一分析缺失。

**Q5: EVALUATE-FOR（κ=0.361）是否说明低 κ 时语义层优势被削弱？**

[AGREE] 逻辑上成立。当 κ 较低时（约束松散，多数 type pairs 合法），semantic masking 过滤掉的 candidate types 更少，enforcement 的边际效果降低。§1（Page 1）中 EVALUATE-FOR 在 schema-informed prompting 下 violations 增加 5.8pp 的例子间接支持了这一点——但这是 prompting 的问题，不是 semantic layer 的问题。

需要区分两个层面：(a) 低 κ 时 semantic layer 的 DR 减少幅度确实更小（因为过滤空间更小）；(b) 但低 κ 时 DR 本身也更低（约束松散→违规机会更少）。所以低 κ 时 semantic layer "看起来" 效果弱，部分是因为 base rate 本身就低。论文缺少按 per-relation κ 分层的 DR reduction 分析来拆解这两个效应。

---

### Missing References

**R1-Ref1: Outlines 近期 structured generation 改进（regex-based + jump-forward optimization）**

[AGREE] 论文引用了 Outlines (Willard and Louf, 2023) 作为 grammar-constrained decoding 的基础工作（§6, Page 8），但 Outlines 在 2024-2025 有重要更新（regex-based constraints, jump-forward token optimization）。如果这些更新改变了 Outlines 处理 cross-field constraints 的能力，则需要更新讨论。但据我了解，Outlines 的核心仍是 CFG/regex-based，无法处理论文定义的 Level 2 constraints，所以遗漏的影响较小。

**R1-Ref2: NuneroPlan (Zhu et al., 2024)**

[REBUT] 经 web search 验证，未找到名为 "NuneroPlan" 的论文（搜索 "NuneroPlan Zhu et al 2024 planning structured information extraction" 无结果）。**R1 此条引用可能是幻觉（hallucinated reference）**，建议 Director 向 R1 确认论文全称和出处。

**R1-Ref3: Dong et al. (2024) retrieval-augmented generation 实现 schema-compliant IE**

[REBUT] 经搜索，最接近的匹配是 "Adaptive Schema-aware Event Extraction with Retrieval-Augmented Generation"（arXiv:2505.08690, 2025），但这不是 Dong et al. 且发表于 2025 而非 2024。论文已引用 Dong et al. (2025) 的 XGrammar 工作。**R1 此条引用同样无法验证具体出处**，建议 Director 要求 R1 提供完整 citation。

---

### 总结

R1 的 3 个 Must-Fix 和 5 个 Should-Fix 中，我 **全部 AGREE**（但 R1-N2 中 "Figure 2" 引用有误，应为附录图）。R1 的分析角度与我的审稿互补：

- R1 聚焦 **理论-实践 gap**（N1）、**统计有效性**（N2）、**70B 验证深度**（N3）
- 我聚焦 **novelty 天花板**（my N1）、**强 baseline 缺失**（my N2）、**R-F1 竞争力**（my N3）

两人共同指出的问题：WikiEvents pilot 过于初步（R1-W2 ≈ my W1）、CF 叙事过于乐观（R1-W5 ≈ my W2）、§7 Discussion 压缩（隐含于 R1 对 S2 退化解释的需求 ≈ my W3）。

R1 的 3 个 Missing References 中 2 个无法验证（NuneroPlan、Dong et al. 2024），建议 Director 核实。

综合两位 Reviewer 的意见，我维持 **Overall: 3.0 (Findings)** 的判断。论文的工程质量和分析诚实性支撑 Findings 接收，但 novelty 不足以进入 main conference。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 2452 · 2026-05-23T09:33:38.462195+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "schema_semantic_constrained_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "schema_semantic_constrained_ie"
  }
}
```

</details>

---


### Tool result

_source line 2453 · 2026-05-23T09:33:38.613281+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-23T09:19:11.170914+00:00\", \"completed_at\": \"2026-05-23T09:23:35.851574+00:00\", \"findings\": [{\"severity\": \"warning\", \"dimension\": \"page 1-2\", \"message\": \"前两页为纯文本（Title/Abstract/Introduction/Background），无任何 display item。第一个视觉锚点（Figure 1 架构图）直到第 3 页才出现。审稿人在前 2 分钟内缺乏视觉抓手，建议将 Figure 1 提前至第 2 页（如 Background 段末或 Method 开头处）以加速认知锚定\"}, {\"severity\": \"warning\", \"dimension\": \"page 1-8\", \"message\": \"主文 8 页仅含 4 个 display items（1 figure + 3 tables），对于实证为主的论文偏少（推荐 5-8 个）。所有实验结果均以表格呈现，缺少一个主结果的可视化图表（如 bar chart 对比各配置的 DR/F1 trade-off），这会削弱审稿人对核心结果的直观印象\"}, {\"severity\": \"warning\", \"dimension\": \"page 4-5\", \"message\": \"连续两页纯文本（Method §3.2-3.4 + Constraint Composition §4），无 figure/table/display equation 穿插。虽有行内公式，但整体视觉节奏单调。建议在 §3 或 §4 中插入一个约束组合的示例图或伪代码 figure 来打破文本墙\"}, {\"severity\": \"warning\", \"dimension\": \"page 8\", \"message\": \"主文最后一页（Related Work + Discussion/Conclusion）为纯文本，视觉上较为平淡。Related Work 段密度高、缺乏结构化分组（如用 paragraph headings 已做但无视觉分隔），审稿人快速扫描时易疲劳\"}, {\"severity\": \"info\", \"dimension\": \"page 3\", \"message\": \"Figure 1 架构图整体清晰，三面板设计（Grammar Layer / Constraint Logic / Token Masking）传达核心 message。颜色区分度尚可（蓝/绿/橙），字号可读。Caption 基本自包含。建议：图内文字可适当加大，确保打印后仍清晰\"}, {\"severity\": \"info\", \"dimension\": \"page 6\", \"message\": \"Table 1 和 Table 2 并排呈现，booktabs 风格，最优结果加粗。排版紧凑但可读。小数位数一致。表格质量良好\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Table 3（WikiEvents 结果）格式规范，booktabs 风格，加粗标记正确。但该表较小，页面下方留有约 1/4 空白区域\"}, {\"severity\": \"info\", \"dimension\": \"page 9\", \"message\": \"Limitations 段长度适中（约覆盖 3-4 个点），符合 EMNLP 规范。Ethics Statement 简洁。References 从本页底部开始，过渡自然\"}, {\"severity\": \"info\", \"dimension\": \"page 13\", \"message\": \"Table 4（Prompt Templates）包含大段 monospace 代码文本，字号偏小但仍可读。该表占据整页上半部分，是必要的信息呈现\"}, {\"severity\": \"info\", \"dimension\": \"page 14-16\", \"message\": \"Appendix B（Extended Related Work）连续 3 页纯文本，无任何 d
…[truncated 1062 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 2454 · 2026-05-23T09:33:38.613819+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "schema_semantic_constrained_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "schema_semantic_constrained_ie"
  }
}
```

</details>

---


### Tool result

_source line 2455 · 2026-05-23T09:33:38.665899+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 52
}
```

</details>

---


### Tool call

_source line 2456 · 2026-05-23T09:36:52.889312+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "schema_semantic_constrained_ie",
  "issues_yaml": "# Review Issues Tracker — schema_semantic_constrained_ie\n# Updated: Round 24 review completed, 2026-05-23\n\n# ============================================================\n# Round 24 — New/Recurring Issues\n# ============================================================\n\n- id: \"R24-N1\"\n  summary: \"Proposition 1 理论-实践 gap：无界证明 vs 有界场景的桥接不够清晰，呈现定位过高\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 14\n  last_seen_round: 24\n  mentions:\n    - round: 23\n      reviewers: [1, 2]\n      note: \"R23-W2/R23-W7 合并。降低 Proposition 1 强度 + Remark 提升。\"\n    - round: 24\n      reviewers: [1, 2]\n      note: \"R1-N1: 理论不可能性(无界)与工程不可行性(有界指数级)需明确区分，proof sketch 过简，缺 DFA 可行边界条件。R2-N1: Prop 1 trivial，应定位为 motivating observation。R1 rebut R2 认为三级分类法有架构指导价值。Director 判定：呈现问题而非实质缺陷，降为 Should-Fix。\"\n  action_items:\n    - round: 23\n      action: \"降低 Proposition 1 呈现强度 + κ 加 descriptive only\"\n      assigned_to: paper_agent\n      status: completed\n    - round: 24\n      action: \"§3 明确区分理论不可能性(无界)与工程不可行性(有界指数级)；给出 DFA 可行边界条件(如 |E|≤3, entities≤5)；将 Prop 1 定位为 'formalizing a known intuition for the IE setting'；扩展 proof sketch 至少引用 pumping lemma 核心直觉\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R24-N2\"\n  summary: \"κ-DR 相关性 n=3 p=0.138 在正文中呈现方式不当，Abstract/§1 仍用 'correlate' 措辞\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 12\n  last_seen_round: 24\n  mentions:\n    - round: 23\n      reviewers: [1, 2]\n      note: \"R23-W2。加 descriptive only (n=3, p=0.138)。\"\n    - round: 24\n      reviewers: [1, 2]\n      note: \"R1-N2 + R2 AGREE。§4 标注了 descriptive，但 Abstract 第3段和 §1 Contribution 2 仍用 'rates correlate with schema restrictiveness'。附录回归线拟合3点无统计意义。全文需统一为 'observed pattern across three schemas'。\"\n  action_items:\n    - round: 23\n      action: \"κ 加 descriptive only (n=3, p=0.138)\"\n      assigned_to: paper_agent\n      status: completed\n    - round: 24\n      action: \"Abstract/§1 将 'correlate' 替换为 'observed pattern across three schemas, insufficient for statistical inference'；附录回归线标注 'illustrative only, n=3' 或移除\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R24-N3\"\n  summary: \"70B 验证仅 Llama 单一模型族 + AWQ INT4 无 FP16 基线，Contribution 2 '4 models' 表述误导\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 14\n  last_seen_round: 24\n  mentions:\n    - round: 23\n      reviewers: [1, 2]\n      note: \"R23-W5。Abstract 加 '(AWQ INT4)'，§5.3 开头加量化限制声明。\"\n    - round: 24\n      reviewers: [1, 2]\n      note: \"R1-N3 + R2 AGREE。70B 仅 1 模型族 1 精度。S2 退化 -8.45pp 解释 post-hoc。Contribution 2 '4 models spanning 8B-70B' 实为 3×8B FP16 + 1×70B INT4。建议：70B 定位为 preliminary；拆分 8B/70B 声明层级。\"\n  action_items:\n    - round: 23\n      action: \"Abstract 加 '(AWQ INT4)' + §5.3 开头加量化限制声明 + 引用 Appendix P\"\n      assigned_to: paper_agent\n      status: completed\n    - round: 24\n      action: \"Contribution 2 拆分 8B/70B 声明(3 8B FP16 + 1 70B INT4 preliminary)；70B 段标注 'preliminary single-family validation'；为 S2 70B 退化提供机制性解释或标注 requires further investigation\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R24-W1\"\n  summary: \"缺乏与强 baseline (GoLLIE/KnowCoder/post-hoc repair) 的公平对比——论文定位为约束执行方法但未在正文明确\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 23\n  last_seen_round: 24\n  mentions:\n    - round: 23\n      reviewers: [1, 2]\n      note: \"R23-W3。GoLLIE 段重写标注 setup 差异。\"\n    - round: 24\n      reviewers: [2]\n      note: \"R2-N2。R1 rebut 认为已有 GCD-equiv/post-hoc filtering/GoLLIE 三类对比，且 OntoCoDec 是约束执行方法非 IE 系统。Director 判定 R1 rebuttal 部分成立，降为 Should-Fix。正文应明确声明定位。\"\n  action_items:\n    - round: 23\n      action: \"§6 GoLLIE 段重写\"\n      assigned_to: paper_agent\n      status: completed\n    - round: 24\n      action: \"§1 或 §5 开头增加明确定位声明：'OntoCoDec is a constraint enforcement method, complementary to training-based schema-aware approaches'；考虑增加 post-hoc type repair baseline\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R24-W2\"\n  summary: \"R-F1 41-47% 在正文中缺乏上下文定位（LLM-based generative RE 典型范围）\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 24\n  last_seen_round: 24\n  mentions:\n    - round: 24\n      reviewers: [2]\n      note: \"R2-N3。R1 rebut 认为 task setting 不同、约束价值独立于 F1。Director 判定：rebuttal 成立但正文应提供上下文。Appendix 已有 SOTA 数据但正文缺失。\"\n  action_items:\n    - round: 24\n      action: \"§5 Setup 增加 1-2 句 LLM-based generative RE 的典型 F1 范围说明\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R24-W3\"\n  summary: \"WikiEvents n=20 pilot 在正文中占半页但无统计结论，Table 3 与 Table 1/2 等位呈现具误导性\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 24\n  mentions:\n    - round: 23\n      reviewers: [1, 2]\n      note: \"R23-W4。降级 contribution + 标注 directional only。\"\n    - round: 24\n      reviewers: [1, 2]\n      note: \"R1-W2 + R2-W1 共识：Table 3 应移至 Appendix 或在 caption 标注 'underpowered; all comparisons non-significant'。\"\n  action_items:\n    - round: 23\n      action: \"§1 contribution 降级 + §5.4 标题改 Preliminary Pilot + Table 4 caption 加 n=20,MDE±5.0pp\"\n      assigned_to: paper_agent\n      status: completed\n    - round: 24\n      action: \"将 Table 3 移至 Appendix，正文仅用 1-2 句概述 pilot 结论；或在 Table 3 caption 增加 'underpowered; no comparison reaches statistical significance'\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R24-W4\"\n  summary: \"First-seen semantics 级联错误影响未量化：首次类型赋值错误率及其后续 CF 影响未报告\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 24\n  last_seen_round: 24\n  mentions:\n    - round: 24\n      reviewers: [1, 2]\n      note: \"R1-W1 + R2 AGREE。245 CF violations 中多少源于 first-seen 错误 vs 合法类型歧义？缺少分析。\"\n  action_items:\n    - round: 24\n      action: \"增加统计：多次出现实体中 first-seen type 与 gold type 不一致的比例；分析这些不一致导致的 CF 违规数\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R24-W5\"\n  summary: \"§7 Discussion 仅 8 行过于压缩，缺少 DR↔CF trade-off、约束执行与 training-based 方法互补性讨论\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 24\n  last_seen_round: 24\n  mentions:\n    - round: 24\n      reviewers: [1, 2]\n      note: \"R2-W3 + R1 隐含同意。建议压缩 Related Work 释放空间。\"\n  action_items:\n    - round: 24\n      action: \"§7 扩展至少 3 段：DR↔CF trade-off 定量含义、与 training-based enforcement 互补关系、per-triple vs global enforcement 根本张力\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R24-W6\"\n  summary: \"Contribution 2 过度打包（4 models × 2 precisions × 2 datasets + pilot + scale interaction 全塞一个 bullet）\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 24\n  last_seen_round: 24\n  mentions:\n    - round: 24\n      reviewers: [1, 2]\n      note: \"R2-W5 + R1 AGREE。纯呈现问题。\"\n  action_items:\n    - round: 24\n      action: \"拆分 Contribution 2 为 2-3 条：消融设计 + cross-model 验证 + 统计方法论/pilot\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R24-W7\"\n  summary: \"LoRA 超参从 SciERC 直接转移到 DocRED 未做调优，可能低估 DocRED fine-tuning 潜力\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 24\n  last_seen_round: 24\n  mentions:\n    - round: 24\n      reviewers: [1, 2]\n      note: \"R1-W4 + R2 AGREE。SciERC(7 rels, 551 短句) vs DocRED(96 rels, 998 长文档) 差异大。\"\n  action_items:\n    - round: 24\n      action: \"Appendix 增加 DocRED LoRA rank/α 敏感性分析(至少 2-3 配置)；或正文承认超参转移可能低估 DocRED 潜力\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R24-W8\"\n  summary: \"Beam search 作为 CF 解决方案的实用性讨论不足（内存开销、beam width sensitivity、fine-tuned 下边际收益）\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 24\n  last_seen_round: 24\n  mentions:\n    - round: 24\n      reviewers: [1, 2]\n      note: \"R1-W5 + R2-W2 共识。k=4 1.54× latency，但未讨论 k=2 是否足够、70B 内存开销、fine-tuned 下 CF 已低至 0.11% 时 beam 边际价值。\"\n  action_items:\n    - round: 24\n      action: \"§5 beam search 段增加 beam width sensitivity 讨论(k=2 vs k=4)、fine-tuned 下 beam 边际收益评估\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R24-M1\"\n  summary: \"GCD-equiv 等价性验证仅在 Qwen3-8B 单一模型上进行\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 24\n  last_seen_round: 24\n  mentions:\n    - round: 24\n      reviewers: [1, 2]\n      note: \"R1-W3 + R2 AGREE (severity 较低)。cross-model grammar-only 间接支持 generalizability。\"\n  action_items:\n    - round: 24\n      action: \"脚注说明 GCD-equiv 仅在 Qwen3-8B 验证，或增加一个额外模型验证\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R24-M2\"\n  summary: \"约束来源(训练数据 vs 形式本体)的区分在 §3 中不够明确\"\n  category: framing\n  severity: info\n  status: open\n  first_raised_round: 24\n  last_seen_round: 24\n  mentions:\n    - round: 24\n      reviewers: [2]\n      note: \"R2-W4。R1 部分 rebut(SciERC 类型系统有形式定义、WikiEvents 用 KAIROS)。\"\n  action_items:\n    - round: 24\n      action: \"§2 或 §5 Setup 更明确区分两种约束来源：形式本体(KAIROS) vs 训练数据推导 schema(SciERC/DocRED)及后者不完整性风险\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# Round 23 — Status Update\n# ============================================================\n\n- id: \"R23-W1\"\n  summary: \"CF 违规占残余违规 64%，与标题 'Type-Constrained IE' 形成 gap，正文讨论不足\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 23\n  last_seen_round: 24\n  mentions:\n    - round: 23\n      reviewers: [1, 2]\n      note: \"R1-W1 (Critical) + R2-W2 (Major)。两位共识：正文应量化 CF 比例、讨论架构限制。\"\n    - round: 24\n      reviewers: [1, 2]\n      note: \"本轮 CF 讨论已大幅改善(§5.1 Cross-field violation analysis 段)，但 R1-W5/R2-W2 指出 CF 叙事仍偏乐观、beam search 实用性讨论不足。部分改善但未完全解决。\"\n  action_items:\n    - round: 23\n      action: \"§5.1 加 CF 量化段落(63.9%, GENERIC↔OtherScientificTerm 34.7%) + §4 加架构根因1句 + Abstract 加 trade-off\"\n      assigned_to: paper_agent\n      status: completed\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R23-W2\"\n  summary: \"算法创新有限——主要是 XGrammar + stateful logits processor 的系统集成\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 23\n  last_seen_round: 24\n  mentions:\n    - round: 23\n      reviewers: [1, 2]\n      note: \"R2-W1 (Major)。共识：定位为 strong engineering contribution。\"\n    - round: 24\n      reviewers: [1, 2]\n      note: \"R2 维持 novelty 不足判断(Overall 3.0)。R1 rebut 认为三级分类法 + 系统验证超过 Findings。分歧未解决。\"\n  action_items:\n    - round: 23\n      action: \"降低 Proposition 1 呈现强度 + κ 加 descriptive only\"\n      assigned_to: paper_agent\n      status: completed\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R23-W3\"\n  summary: \"GoLLIE 对比不公平 + 缺少与训练基方法的系统性对比\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 23\n  last_seen_round: 24\n  mentions:\n    - round: 23\n      reviewers: [1, 2]\n      note: \"R1-W5 + R2-W4。标注 setup 差异。\"\n    - round: 24\n      reviewers: [1, 2]\n      note: \"R2 维持 baseline 不足。R1 rebut 认为已有足够多层对比，核心是定位声明缺失。合并为 R24-W1。\"\n  action_items:\n    - round: 23\n      action: \"§6 GoLLIE 段重写\"\n      assigned_to: paper_agent\n      status: completed\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R23-W4\"\n  summary: \"WikiEvents n=20 统计效力不足但结论呈现过度自信\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 23\n  last_seen_round: 24\n  mentions:\n    - round: 23\n      reviewers: [1, 2]\n      note: \"降级 contribution + directional only。\"\n    - round: 24\n      reviewers: [1, 2]\n      note: \"改善但不足。Table 3 仍在正文中与 Table 1/2 等位。合并为 R24-W3。\"\n  action_items:\n    - round: 23\n      action: \"§1 contribution 降级 + §5.4 标题改 Preliminary Pilot\"\n      assigned_to: paper_agent\n      status: completed\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R23-W5\"\n  summary: \"70B 实验全在 AWQ INT4 上，Abstract 未标注，§5.3 量化限制披露过晚\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 23\n  last_seen_round: 24\n  mentions:\n    - round: 23\n      reviewers: [1, 2]\n      note: \"Abstract 加 (AWQ INT4)。\"\n    - round: 24\n      reviewers: [1, 2]\n      note: \"已改善(AWQ INT4 标注)。但 R24-N3 进一步指出单模型族 + Contribution 2 措辞问题。合并为 R24-N3。\"\n  action_items:\n    - round: 23\n      action: \"Abstract 加 '(AWQ INT4)' + §5.3 开头加量化限制声明\"\n      assigned_to: paper_agent\n      status: completed\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R23-W6\"\n  summary: \"Zero-shot 实验占主文 ~3 页但 R-F1 仅 4-8%，篇幅分配失衡\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 23\n  last_seen_round: 24\n  mentions:\n    - round: 23\n      reviewers: [1, 2]\n      note: \"压缩 ZS 为1段+Table 1。\"\n    - round: 24\n      note: \"本轮未被独立提及为 weakness。ZS 压缩有效。\"\n  action_items:\n    - round: 23\n      action: \"ZS 从3 subsection压缩为1段+Table 1\"\n      assigned_to: paper_agent\n      status: completed\n  resolution: \"R24 本轮未提及。压缩有效。\"\n  resolution_round: 24\n\n- id: \"R23-W7\"\n  summary: \"Proposition 1 实际意义论证 gap\"\n  category: method\n  severity: info\n  status: in_progress\n  first_raised_round: 23\n  last_seen_round: 24\n  mentions:\n    - round: 23\n      reviewers: [1, 2]\n      note: \"Remark 提升为 paragraph。\"\n    - round: 24\n      reviewers: [1, 2]\n      note: \"合并为 R24-N1。Engineering applicability 段存在但仍需改进。\"\n  action_items:\n    - round: 23\n      action: \"§3 Remark 提升为 paragraph{Engineering applicability.}\"\n      assigned_to: paper_agent\n      status: completed\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R23-W8\"\n  summary: \"'Empirical enabling dependency' 在主文中重复出现 ≥6 次\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 23\n  last_seen_round: 24\n  mentions:\n    - round: 23\n      reviewers: [1, 2]\n      note: \"保留 3 处，其余替换。\"\n    - round: 24\n      note: \"本轮未被提及。替换有效。\"\n  action_items:\n    - round: 23\n      action: \"全文保留3处(Abstract/§3/§5.1)，其余替换\"\n      assigned_to: paper_agent\n      status: completed\n  resolution: \"R24 本轮未提及。替换有效。\"\n  resolution_round: 24\n\n- id: \"R23-W9\"\n  summary: \"Fallback 频率模型依赖性未在正文讨论\"\n  category: experiment\n  severity: info\n  status: in_progress\n  first_raised_round: 23\n  last_seen_round: 24\n  mentions:\n    - round: 23\n      reviewers: [1, 2]\n      note: \"加 fallback frequency 讨论。\"\n    - round: 24\n      note: \"本轮未被独立提及。Fallback 频率已在正文讨论(§5.1 Composability 段)。\"\n  action_items:\n    - round: 23\n      action: \"FT 分析扩展段中加 fallback frequency 讨论\"\n      assigned_to: paper_agent\n      status: completed\n  resolution: \"R24 本轮未提及。讨论有效。\"\n  resolution_round: 24\n\n- id: \"R23-W10\"\n  summary: \"Continuation masking prefix collision 频率未量化\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 23\n  last_seen_round: 23\n  mentions:\n    - round: 23\n      reviewers: [1, 2]\n      note: \"需数据提取，DDL前跳过。\"\n    - round: 24\n      note: \"本轮未提及。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R23-W11\"\n  summary: \"Beam k=2 中间值缺失，k 与违规消除关系不明\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 23\n  last_seen_round: 24\n  mentions:\n    - round: 23\n      reviewers: [1, 2]\n      note: \"需新实验，DDL前跳过。\"\n    - round: 24\n      reviewers: [1, 2]\n      note: \"R1-W5/R2-W2 再次提及 beam width sensitivity 缺失。合并为 R24-W8。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R23-W12\"\n  summary: \"Entity registry first-seen type 行为主文解释不够清晰\"\n  category: method\n  severity: info\n  status: in_progress\n  first_raised_round: 23\n  last_seen_round: 24\n  mentions:\n    - round: 23\n      reviewers: [1, 2]\n      note: \"§3.3 formalize + Limitations 加 entity-first 约束。\"\n    - round: 24\n      reviewers: [1, 2]\n      note: \"R24-W4 进一步要求量化 first-seen 错误影响。§3.3 描述已改善，但量化分析缺失。\"\n  action_items:\n    - round: 23\n      action: \"§3.3 加 first-seen registration formalization\"\n      assigned_to: paper_agent\n      status: completed\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R23-D1\"\n  summary: \"Limitations 长度是否 'excessive'\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 23\n  last_seen_round: 24\n  mentions:\n    - round: 23\n      reviewers: [1, 2]\n      note: \"精简 37%。\"\n    - round: 24\n      note: \"视觉审查确认 Limitations 长度适中(~3-4 个点)，符合 EMNLP 规范。\"\n  action_items:\n    - round: 23\n      action: \"Limitations 精简\"\n      assigned_to: paper_agent\n      status: completed\n  resolution: \"R24 视觉审查确认长度适中。\"\n  resolution_round: 24\n\n# ============================================================\n# Prior Rounds — Resolved\n# ============================================================\n\n- id: \"R16-W5\"\n  summary: \"核心新颖性定位——系统集成而非算法创新\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 24\n  mentions:\n    - round: 19\n      reviewers: [1, 2]\n      note: \"共识定位为 systems contribution。\"\n    - round: 23\n      reviewers: [1, 2]\n      note: \"降低理论贡献措辞。\"\n    - round: 24\n      reviewers: [1, 2]\n      note: \"R2 维持 novelty 不足(3.0 Findings)。R1 认为超过 Findings(3.5)。分歧未解决。合并为 R23-W2。\"\n  action_items:\n    - round: 19\n      action: \"§7 定位 systems contribution\"\n      assigned_to: paper_agent\n      status: completed\n    - round: 23\n      action: \"降低 Proposition 1 强度\"\n      assigned_to: paper_agent\n      status: completed\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R20-W1\"\n  summary: \"Proposition 1 证明中 position→name 转换缺乏形式论证\"\n  category: method\n  severity: info\n  status: in_progress\n  first_raised_round: 20\n  last_seen_round: 24\n  mentions:\n    - round: 23\n      reviewers: [1, 2]\n      note: \"Remark 提升。\"\n    - round: 24\n      reviewers: [1]\n      note: \"R1-Q1 再次提问。R2 代论文 rebut(name-based 不改变结论)。合并为 R24-N1。\"\n  action_items:\n    - round: 20\n      action: \"Appendix O 加 informal argument\"\n      assigned_to: paper_agent\n      status: completed\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R20-W4\"\n  summary: \"主文 Related Work §6 过于精简\"\n  category: related_work\n  severity: info\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 24\n  resolution: \"R23 R2-S4 评价 '充分'。R24 未被提及为 weakness。\"\n  resolution_round: 23\n\n- id: \"R18-M2\"\n  summary: \"Figure 1 视觉层次不够分明\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 24\n  resolution: \"R24 视觉审查评价 'Figure 1 整体清晰，三面板设计传达核心 message'。R1 'Information density high but readable'。\"\n  resolution_round: 24\n\n# ============================================================\n# Resolved (prior rounds, unchanged)\n# ============================================================\n\n- id: \"R16-MF3\"\n  summary: \"CF trade-off 在 Abstract 中 framing 偏乐观\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 21\n  resolution: \"Abstract CF 分层报告。R23 进一步加 trade-off 表述。\"\n  resolution_round: 22\n\n- id: \"R16-W4\"\n  summary: \"70B AWQ INT4 quantization 对约束效果的影响未隔离\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 21\n  resolution: \"8B INT4 ablation 完成。新增 Appendix P。\"\n  resolution_round: 22\n\n- id: \"R16-W3\"\n  summary: \"WikiEvents fine-tuning composability 仅 n=20 文档\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 21\n  resolution: \"降级 contribution。R23 进一步降级。\"\n  resolution_round: 22\n\n- id: \"R16-W1\"\n  summary: \"κ̄/enabling dependency 统计支撑不足\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 21\n  resolution: \"全文加 empirical + scale-dependent qualifier。\"\n  resolution_round: 22\n\n- id: \"R15-MF3\"\n  summary: \"正文溢出至第 9 页\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 21\n  resolution: \"主文 §1-§7 在 page 1-8。\"\n  resolution_round: 22\n\n- id: \"R21-N2\"\n  summary: \"Full FT 组合性解读分歧\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 21\n  last_seen_round: 23\n  resolution: \"Appendix L 修复。\"\n  resolution_round: 23\n\n- id: \"R21-Q1\"\n  summary: \"Beam search k=8 时 per-beam registry 内存开销未量化\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 21\n  last_seen_round: 23\n  resolution: \"Appendix F 补充。\"\n  resolution_round: 23\n\n- id: \"R21-Q2\"\n  summary: \"TCR 整合到解码循环的可行性\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 21\n  last_seen_round: 23\n  resolution: \"Discussion/Appendix N 修复。\"\n  resolution_round: 23\n\n- id: \"R21-Q3\"\n  summary: \"GCD/BoostCD 对比是直接运行还是等价论证\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 21\n  last_seen_round: 23\n  resolution: \"Table 16-17 caption 修复。\"\n  resolution_round: 23\n\n- id: \"R21-Q5\"\n  summary: \"TCR vs OntoCoDec 定位不清\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 21\n  last_seen_round: 23\n  resolution: \"Appendix N 互补定位。\"\n  resolution_round: 23\n\n# ============================================================\n# Won't Fix\n# ============================================================\n\n- id: \"R20-W5\"\n  summary: \"Running example 仍不充分\"\n  category: writing\n  severity: info\n  status: wont_fix\n  first_raised_round: 20\n  last_seen_round: 21\n  resolution: \"空间限制。§3.3 有 Used-for 示例。\"\n  resolution_round: 20\n\n- id: \"R20-W6\"\n  summary: \"Zero-shot 评估实际意义有限\"\n  category: experiment\n  severity: info\n  status: wont_fix\n  first_raised_round: 20\n  last_seen_round: 23\n  resolution: \"ZS 定位为 diagnostic probe。R23 压缩篇幅。\"\n  resolution_round: 23"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "schema_semantic_constrained_ie",
    "issues_yaml": "# Review Issues Tracker — schema_semantic_constrained_ie\n# Updated: Round 24 review completed, 2026-05-23\n\n# ============================================================\n# Round 24 — New/Recurring Issues\n# ============================================================\n\n- id: \"R24-N1\"\n  summary: \"Proposition 1 理论-实践 gap：无界证明 vs 有界场景的桥接不够清晰，呈现定位过高\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 14\n  last_seen_round: 24\n  mentions:\n    - round: 23\n      reviewers: [1, 2]\n      note: \"R23-W2/R23-W7 合并。降低 Proposition 1 强度 + Remark 提升。\"\n    - round: 24\n      reviewers: [1, 2]\n      note: \"R1-N1: 理论不可能性(无界)与工程不可行性(有界指数级)需明确区分，proof sketch 过简，缺 DFA 可行边界条件。R2-N1: Prop 1 trivial，应定位为 motivating observation。R1 rebut R2 认为三级分类法有架构指导价值。Director 判定：呈现问题而非实质缺陷，降为 Should-Fix。\"\n  action_items:\n    - round: 23\n      action: \"降低 Proposition 1 呈现强度 + κ 加 descriptive only\"\n      assigned_to: paper_agent\n      status: completed\n    - round: 24\n      action: \"§3 明确区分理论不可能性(无界)与工程不可行性(有界指数级)；给出 DFA 可行边界条件(如 |E|≤3, entities≤5)；将 Prop 1 定位为 'formalizing a known intuition for the IE setting'；扩展 proof sketch 至少引用 pumping lemma 核心直觉\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R24-N2\"\n  summary: \"κ-DR 相关性 n=3 p=0.138 在正文中呈现方式不当，Abstract/§1 仍用 'correlate' 措辞\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 12\n  last_seen_round: 24\n  mentions:\n    - round: 23\n      reviewers: [1, 2]\n      note: \"R23-W2。加 descriptive only (n=3, p=0.138)。\"\n    - round: 24\n      reviewers: [1, 2]\n      note: \"R1-N2 + R2 AGREE。§4 标注了 descriptive，但 Abstract 第3段和 §1 Contribution 2 仍用 'rates correlate with schema restrictiveness'。附录回归线拟合3点无统计意义。全文需统一为 'observed pattern across three schemas'。\"\n  action_items:\n    - round: 23\n      action: \"κ 加 descriptive only (n=3, p=0.138)\"\n      assigned_to: paper_agent\n      status: completed\n    - round: 24\n      action: \"Abstract/§1 将 'correlate' 替换为 'observed pattern across three schemas, insufficient for statistical inference'；附录回归线标注 'illustrative only, n=3' 或移除\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R24-N3\"\n  summary: \"70B 验证仅 Llama 单一模型族 + AWQ INT4 无 FP16 基线，Contribution 2 '4 models' 表述误导\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 14\n  last_seen_round: 24\n  mentions:\n    - round: 23\n      reviewers: [1, 2]\n      note: \"R23-W5。Abstract 加 '(AWQ INT4)'，§5.3 开头加量化限制声明。\"\n    - round: 24\n      reviewers: [1, 2]\n      note: \"R1-N3 + R2 AGREE。70B 仅 1 模型族 1 精度。S2 退化 -8.45pp 解释 post-hoc。Contribution 2 '4 models spanning 8B-70B' 实为 3×8B FP16 + 1×70B INT4。建议：70B 定位为 preliminary；拆分 8B/70B 声明层级。\"\n  action_items:\n    - round: 23\n      action: \"Abstract 加 '(AWQ INT4)' + §5.3 开头加量化限制声明 + 引用 Appendix P\"\n      assigned_to: paper_agent\n      status: completed\n    - round: 24\n      action: \"Contribution 2 拆分 8B/70B 声明(3 8B FP16 + 1 70B INT4 preliminary)；70B 段标注 'preliminary single-family validation'；为 S2 70B 退化提供机制性解释或标注 requires further investigation\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R24-W1\"\n  summary: \"缺乏与强 baseline (GoLLIE/KnowCoder/post-hoc repair) 的公平对比——论文定位为约束执行方法但未在正文明确\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 23\n  last_seen_round: 24\n  mentions:\n    - round: 23\n      reviewers: [1, 2]\n      note: \"R23-W3。GoLLIE 段重写标注 setup 差异。\"\n    - round: 24\n      reviewers: [2]\n      note: \"R2-N2。R1 rebut 认为已有 GCD-equiv/post-hoc filtering/GoLLIE 三类对比，且 OntoCoDec 是约束执行方法非 IE 系统。Director 判定 R1 rebuttal 部分成立，降为 Should-Fix。正文应明确声明定位。\"\n  action_items:\n    - round: 23\n      action: \"§6 GoLLIE 段重写\"\n      assigned_to: paper_agent\n      status: completed\n    - round: 24\n      action: \"§1 或 §5 开头增加明确定位声明：'OntoCoDec is a constraint enforcement method, complementary to training-based schema-aware approaches'；考虑增加 post-hoc type repair baseline\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R24-W2\"\n  summary: \"R-F1 41-47% 在正文中缺乏上下文定位（LLM-based generative RE 典型范围）\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 24\n  last_seen_round: 24\n  mentions:\n    - round: 24\n      reviewers: [2]\n      note: \"R2-N3。R1 rebut 认为 task setting 不同、约束价值独立于 F1。Director 判定：rebuttal 成立但正文应提供上下文。Appendix 已有 SOTA 数据但正文缺失。\"\n  action_items:\n    - round: 24\n      action: \"§5 Setup 增加 1-2 句 LLM-based generative RE 的典型 F1 范围说明\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R24-W3\"\n  summary: \"WikiEvents n=20 pilot 在正文中占半页但无统计结论，Table 3 与 Table 1/2 等位呈现具误导性\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 24\n  mentions:\n    - round: 23\n      reviewers: [1, 2]\n      note: \"R23-W4。降级 contribution + 标注 directional only。\"\n    - round: 24\n      reviewers: [1, 2]\n      note: \"R1-W2 + R2-W1 共识：Table 3 应移至 Appendix 或在 caption 标注 'underpowered; all comparisons non-significant'。\"\n  action_items:\n    - round: 23\n      action: \"§1 contribution 降级 + §5.4 标题改 Preliminary Pilot + Table 4 caption 加 n=20,MDE±5.0pp\"\n      assigned_to: paper_agent\n      status: completed\n    - round: 24\n      action: \"将 Table 3 移至 Appendix，正文仅用 1-2 句概述 pilot 结论；或在 Table 3 caption 增加 'underpowered; no comparison reaches statistical significance'\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R24-W4\"\n  summary: \"First-seen semantics 级联错误影响未量化：首次类型赋值错误率及其后续 CF 影响未报告\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 24\n  last_seen_round: 24\n  mentions:\n    - round: 24\n      reviewers: [1, 2]\n      note: \"R1-W1 + R2 AGREE。245 CF violations 中多少源于 first-seen 错误 vs 合法类型歧义？缺少分析。\"\n  action_items:\n    - round: 24\n      action: \"增加统计：多次出现实体中 first-seen type 与 gold type 不一致的比例；分析这些不一致导致的 CF 违规数\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R24-W5\"\n  summary: \"§7 Discussion 仅 8 行过于压缩，缺少 DR↔CF trade-off、约束执行与 training-based 方法互补性讨论\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 24\n  last_seen_round: 24\n  mentions:\n    - round: 24\n      reviewers: [1, 2]\n      note: \"R2-W3 + R1 隐含同意。建议压缩 Related Work 释放空间。\"\n  action_items:\n    - round: 24\n      action: \"§7 扩展至少 3 段：DR↔CF trade-off 定量含义、与 training-based enforcement 互补关系、per-triple vs global enforcement 根本张力\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R24-W6\"\n  summary: \"Contribution 2 过度打包（4 models × 2 precisions × 2 datasets + pilot + scale interaction 全塞一个 bullet）\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 24\n  last_seen_round: 24\n  mentions:\n    - round: 24\n      reviewers: [1, 2]\n      note: \"R2-W5 + R1 AGREE。纯呈现问题。\"\n  action_items:\n    - round: 24\n      action: \"拆分 Contribution 2 为 2-3 条：消融设计 + cross-model 验证 + 统计方法论/pilot\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R24-W7\"\n  summary: \"LoRA 超参从 SciERC 直接转移到 DocRED 未做调优，可能低估 DocRED fine-tuning 潜力\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 24\n  last_seen_round: 24\n  mentions:\n    - round: 24\n      reviewers: [1, 2]\n      note: \"R1-W4 + R2 AGREE。SciERC(7 rels, 551 短句) vs DocRED(96 rels, 998 长文档) 差异大。\"\n  action_items:\n    - round: 24\n      action: \"Appendix 增加 DocRED LoRA rank/α 敏感性分析(至少 2-3 配置)；或正文承认超参转移可能低估 DocRED 潜力\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R24-W8\"\n  summary: \"Beam search 作为 CF 解决方案的实用性讨论不足（内存开销、beam width sensitivity、fine-tuned 下边际收益）\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 24\n  last_seen_round: 24\n  mentions:\n    - round: 24\n      reviewers: [1, 2]\n      note: \"R1-W5 + R2-W2 共识。k=4 1.54× latency，但未讨论 k=2 是否足够、70B 内存开销、fine-tuned 下 CF 已低至 0.11% 时 beam 边际价值。\"\n  action_items:\n    - round: 24\n      action: \"§5 beam search 段增加 beam width sensitivity 讨论(k=2 vs k=4)、fine-tuned 下 beam 边际收益评估\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R24-M1\"\n  summary: \"GCD-equiv 等价性验证仅在 Qwen3-8B 单一模型上进行\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 24\n  last_seen_round: 24\n  mentions:\n    - round: 24\n      reviewers: [1, 2]\n      note: \"R1-W3 + R2 AGREE (severity 较低)。cross-model grammar-only 间接支持 generalizability。\"\n  action_items:\n    - round: 24\n      action: \"脚注说明 GCD-equiv 仅在 Qwen3-8B 验证，或增加一个额外模型验证\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R24-M2\"\n  summary: \"约束来源(训练数据 vs 形式本体)的区分在 §3 中不够明确\"\n  category: framing\n  severity: info\n  status: open\n  first_raised_round: 24\n  last_seen_round: 24\n  mentions:\n    - round: 24\n      reviewers: [2]\n      note: \"R2-W4。R1 部分 rebut(SciERC 类型系统有形式定义、WikiEvents 用 KAIROS)。\"\n  action_items:\n    - round: 24\n      action: \"§2 或 §5 Setup 更明确区分两种约束来源：形式本体(KAIROS) vs 训练数据推导 schema(SciERC/DocRED)及后者不完整性风险\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# Round 23 — Status Update\n# ============================================================\n\n- id: \"R23-W1\"\n  summary: \"CF 违规占残余违规 64%，与标题 'Type-Constrained IE' 形成 gap，正文讨论不足\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 23\n  last_seen_round: 24\n  mentions:\n    - round: 23\n      reviewers: [1, 2]\n      note: \"R1-W1 (Critical) + R2-W2 (Major)。两位共识：正文应量化 CF 比例、讨论架构限制。\"\n    - round: 24\n      reviewers: [1, 2]\n      note: \"本轮 CF 讨论已大幅改善(§5.1 Cross-field violation analysis 段)，但 R1-W5/R2-W2 指出 CF 叙事仍偏乐观、beam search 实用性讨论不足。部分改善但未完全解决。\"\n  action_items:\n    - round: 23\n      action: \"§5.1 加 CF 量化段落(63.9%, GENERIC↔OtherScientificTerm 34.7%) + §4 加架构根因1句 + Abstract 加 trade-off\"\n      assigned_to: paper_agent\n      status: completed\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R23-W2\"\n  summary: \"算法创新有限——主要是 XGrammar + stateful logits processor 的系统集成\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 23\n  last_seen_round: 24\n  mentions:\n    - round: 23\n      reviewers: [1, 2]\n      note: \"R2-W1 (Major)。共识：定位为 strong engineering contribution。\"\n    - round: 24\n      reviewers: [1, 2]\n      note: \"R2 维持 novelty 不足判断(Overall 3.0)。R1 rebut 认为三级分类法 + 系统验证超过 Findings。分歧未解决。\"\n  action_items:\n    - round: 23\n      action: \"降低 Proposition 1 呈现强度 + κ 加 descriptive only\"\n      assigned_to: paper_agent\n      status: completed\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R23-W3\"\n  summary: \"GoLLIE 对比不公平 + 缺少与训练基方法的系统性对比\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 23\n  last_seen_round: 24\n  mentions:\n    - round: 23\n      reviewers: [1, 2]\n      note: \"R1-W5 + R2-W4。标注 setup 差异。\"\n    - round: 24\n      reviewers: [1, 2]\n      note: \"R2 维持 baseline 不足。R1 rebut 认为已有足够多层对比，核心是定位声明缺失。合并为 R24-W1。\"\n  action_items:\n    - round: 23\n      action: \"§6 GoLLIE 段重写\"\n      assigned_to: paper_agent\n      status: completed\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R23-W4\"\n  summary: \"WikiEvents n=20 统计效力不足但结论呈现过度自信\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 23\n  last_seen_round: 24\n  mentions:\n    - round: 23\n      reviewers: [1, 2]\n      note: \"降级 contribution + directional only。\"\n    - round: 24\n      reviewers: [1, 2]\n      note: \"改善但不足。Table 3 仍在正文中与 Table 1/2 等位。合并为 R24-W3。\"\n  action_items:\n    - round: 23\n      action: \"§1 contribution 降级 + §5.4 标题改 Preliminary Pilot\"\n      assigned_to: paper_agent\n      status: completed\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R23-W5\"\n  summary: \"70B 实验全在 AWQ INT4 上，Abstract 未标注，§5.3 量化限制披露过晚\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 23\n  last_seen_round: 24\n  mentions:\n    - round: 23\n      reviewers: [1, 2]\n      note: \"Abstract 加 (AWQ INT4)。\"\n    - round: 24\n      reviewers: [1, 2]\n      note: \"已改善(AWQ INT4 标注)。但 R24-N3 进一步指出单模型族 + Contribution 2 措辞问题。合并为 R24-N3。\"\n  action_items:\n    - round: 23\n      action: \"Abstract 加 '(AWQ INT4)' + §5.3 开头加量化限制声明\"\n      assigned_to: paper_agent\n      status: completed\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R23-W6\"\n  summary: \"Zero-shot 实验占主文 ~3 页但 R-F1 仅 4-8%，篇幅分配失衡\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 23\n  last_seen_round: 24\n  mentions:\n    - round: 23\n      reviewers: [1, 2]\n      note: \"压缩 ZS 为1段+Table 1。\"\n    - round: 24\n      note: \"本轮未被独立提及为 weakness。ZS 压缩有效。\"\n  action_items:\n    - round: 23\n      action: \"ZS 从3 subsection压缩为1段+Table 1\"\n      assigned_to: paper_agent\n      status: completed\n  resolution: \"R24 本轮未提及。压缩有效。\"\n  resolution_round: 24\n\n- id: \"R23-W7\"\n  summary: \"Proposition 1 实际意义论证 gap\"\n  category: method\n  severity: info\n  status: in_progress\n  first_raised_round: 23\n  last_seen_round: 24\n  mentions:\n    - round: 23\n      reviewers: [1, 2]\n      note: \"Remark 提升为 paragraph。\"\n    - round: 24\n      reviewers: [1, 2]\n      note: \"合并为 R24-N1。Engineering applicability 段存在但仍需改进。\"\n  action_items:\n    - round: 23\n      action: \"§3 Remark 提升为 paragraph{Engineering applicability.}\"\n      assigned_to: paper_agent\n      status: completed\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R23-W8\"\n  summary: \"'Empirical enabling dependency' 在主文中重复出现 ≥6 次\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 23\n  last_seen_round: 24\n  mentions:\n    - round: 23\n      reviewers: [1, 2]\n      note: \"保留 3 处，其余替换。\"\n    - round: 24\n      note: \"本轮未被提及。替换有效。\"\n  action_items:\n    - round: 23\n      action: \"全文保留3处(Abstract/§3/§5.1)，其余替换\"\n      assigned_to: paper_agent\n      status: completed\n  resolution: \"R24 本轮未提及。替换有效。\"\n  resolution_round: 24\n\n- id: \"R23-W9\"\n  summary: \"Fallback 频率模型依赖性未在正文讨论\"\n  category: experiment\n  severity: info\n  status: in_progress\n  first_raised_round: 23\n  last_seen_round: 24\n  mentions:\n    - round: 23\n      reviewers: [1, 2]\n      note: \"加 fallback frequency 讨论。\"\n    - round: 24\n      note: \"本轮未被独立提及。Fallback 频率已在正文讨论(§5.1 Composability 段)。\"\n  action_items:\n    - round: 23\n      action: \"FT 分析扩展段中加 fallback frequency 讨论\"\n      assigned_to: paper_agent\n      status: completed\n  resolution: \"R24 本轮未提及。讨论有效。\"\n  resolution_round: 24\n\n- id: \"R23-W10\"\n  summary: \"Continuation masking prefix collision 频率未量化\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 23\n  last_seen_round: 23\n  mentions:\n    - round: 23\n      reviewers: [1, 2]\n      note: \"需数据提取，DDL前跳过。\"\n    - round: 24\n      note: \"本轮未提及。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R23-W11\"\n  summary: \"Beam k=2 中间值缺失，k 与违规消除关系不明\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 23\n  last_seen_round: 24\n  mentions:\n    - round: 23\n      reviewers: [1, 2]\n      note: \"需新实验，DDL前跳过。\"\n    - round: 24\n      reviewers: [1, 2]\n      note: \"R1-W5/R2-W2 再次提及 beam width sensitivity 缺失。合并为 R24-W8。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R23-W12\"\n  summary: \"Entity registry first-seen type 行为主文解释不够清晰\"\n  category: method\n  severity: info\n  status: in_progress\n  first_raised_round: 23\n  last_seen_round: 24\n  mentions:\n    - round: 23\n      reviewers: [1, 2]\n      note: \"§3.3 formalize + Limitations 加 entity-first 约束。\"\n    - round: 24\n      reviewers: [1, 2]\n      note: \"R24-W4 进一步要求量化 first-seen 错误影响。§3.3 描述已改善，但量化分析缺失。\"\n  action_items:\n    - round: 23\n      action: \"§3.3 加 first-seen registration formalization\"\n      assigned_to: paper_agent\n      status: completed\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R23-D1\"\n  summary: \"Limitations 长度是否 'excessive'\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 23\n  last_seen_round: 24\n  mentions:\n    - round: 23\n      reviewers: [1, 2]\n      note: \"精简 37%。\"\n    - round: 24\n      note: \"视觉审查确认 Limitations 长度适中(~3-4 个点)，符合 EMNLP 规范。\"\n  action_items:\n    - round: 23\n      action: \"Limitations 精简\"\n      assigned_to: paper_agent\n      status: completed\n  resolution: \"R24 视觉审查确认长度适中。\"\n  resolution_round: 24\n\n# ============================================================\n# Prior Rounds — Resolved\n# ============================================================\n\n- id: \"R16-W5\"\n  summary: \"核心新颖性定位——系统集成而非算法创新\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 24\n  mentions:\n    - round: 19\n      reviewers: [1, 2]\n      note: \"共识定位为 systems contribution。\"\n    - round: 23\n      reviewers: [1, 2]\n      note: \"降低理论贡献措辞。\"\n    - round: 24\n      reviewers: [1, 2]\n      note: \"R2 维持 novelty 不足(3.0 Findings)。R1 认为超过 Findings(3.5)。分歧未解决。合并为 R23-W2。\"\n  action_items:\n    - round: 19\n      action: \"§7 定位 systems contribution\"\n      assigned_to: paper_agent\n      status: completed\n    - round: 23\n      action: \"降低 Proposition 1 强度\"\n      assigned_to: paper_agent\n      status: completed\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R20-W1\"\n  summary: \"Proposition 1 证明中 position→name 转换缺乏形式论证\"\n  category: method\n  severity: info\n  status: in_progress\n  first_raised_round: 20\n  last_seen_round: 24\n  mentions:\n    - round: 23\n      reviewers: [1, 2]\n      note: \"Remark 提升。\"\n    - round: 24\n      reviewers: [1]\n      note: \"R1-Q1 再次提问。R2 代论文 rebut(name-based 不改变结论)。合并为 R24-N1。\"\n  action_items:\n    - round: 20\n      action: \"Appendix O 加 informal argument\"\n      assigned_to: paper_agent\n      status: completed\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R20-W4\"\n  summary: \"主文 Related Work §6 过于精简\"\n  category: related_work\n  severity: info\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 24\n  resolution: \"R23 R2-S4 评价 '充分'。R24 未被提及为 weakness。\"\n  resolution_round: 23\n\n- id: \"R18-M2\"\n  summary: \"Figure 1 视觉层次不够分明\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 24\n  resolution: \"R24 视觉审查评价 'Figure 1 整体清晰，三面板设计传达核心 message'。R1 'Information density high but readable'。\"\n  resolution_round: 24\n\n# ============================================================\n# Resolved (prior rounds, unchanged)\n# ============================================================\n\n- id: \"R16-MF3\"\n  summary: \"CF trade-off 在 Abstract 中 framing 偏乐观\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 21\n  resolution: \"Abstract CF 分层报告。R23 进一步加 trade-off 表述。\"\n  resolution_round: 22\n\n- id: \"R16-W4\"\n  summary: \"70B AWQ INT4 quantization 对约束效果的影响未隔离\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 21\n  resolution: \"8B INT4 ablation 完成。新增 Appendix P。\"\n  resolution_round: 22\n\n- id: \"R16-W3\"\n  summary: \"WikiEvents fine-tuning composability 仅 n=20 文档\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 21\n  resolution: \"降级 contribution。R23 进一步降级。\"\n  resolution_round: 22\n\n- id: \"R16-W1\"\n  summary: \"κ̄/enabling dependency 统计支撑不足\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 21\n  resolution: \"全文加 empirical + scale-dependent qualifier。\"\n  resolution_round: 22\n\n- id: \"R15-MF3\"\n  summary: \"正文溢出至第 9 页\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 21\n  resolution: \"主文 §1-§7 在 page 1-8。\"\n  resolution_round: 22\n\n- id: \"R21-N2\"\n  summary: \"Full FT 组合性解读分歧\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 21\n  last_seen_round: 23\n  resolution: \"Appendix L 修复。\"\n  resolution_round: 23\n\n- id: \"R21-Q1\"\n  summary: \"Beam search k=8 时 per-beam registry 内存开销未量化\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 21\n  last_seen_round: 23\n  resolution: \"Appendix F 补充。\"\n  resolution_round: 23\n\n- id: \"R21-Q2\"\n  summary: \"TCR 整合到解码循环的可行性\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 21\n  last_seen_round: 23\n  resolution: \"Discussion/Appendix N 修复。\"\n  resolution_round: 23\n\n- id: \"R21-Q3\"\n  summary: \"GCD/BoostCD 对比是直接运行还是等价论证\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 21\n  last_seen_round: 23\n  resolution: \"Table 16-17 caption 修复。\"\n  resolution_round: 23\n\n- id: \"R21-Q5\"\n  summary: \"TCR vs OntoCoDec 定位不清\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 21\n  last_seen_round: 23\n  resolution: \"Appendix N 互补定位。\"\n  resolution_round: 23\n\n# ============================================================\n# Won't Fix\n# ============================================================\n\n- id: \"R20-W5\"\n  summary: \"Running example 仍不充分\"\n  category: writing\n  severity: info\n  status: wont_fix\n  first_raised_round: 20\n  last_seen_round: 21\n  resolution: \"空间限制。§3.3 有 Used-for 示例。\"\n  resolution_round: 20\n\n- id: \"R20-W6\"\n  summary: \"Zero-shot 评估实际意义有限\"\n  category: experiment\n  severity: info\n  status: wont_fix\n  first_raised_round: 20\n  last_seen_round: 23\n  resolution: \"ZS 定位为 diagnostic probe。R23 压缩篇幅。\"\n  resolution_round: 23"
  }
}
```

</details>

---


### Tool result

_source line 2457 · 2026-05-23T09:36:52.992331+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_issues.yaml\", \"bytes\": 21324}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 103
}
```

</details>

---


### Tool call

_source line 2458 · 2026-05-23T09:39:48.829211+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# Round 24 审稿报告 — OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints\n\n**Venue**: EMNLP 2026 (ARR) · Long Paper · Deadline 2026-05-25\n**Reviewer 编排**: R1 (方法严谨性+实验设计) · R2 (新颖性+完整性+写作)\n**流程**: Round 1 独立初审 → 交叉分享 [AGREE]/[REBUT] → 收敛 → 报告\n\n---\n\n## Summary\n\n论文提出 OntoCoDec，将 IE 本体约束编译为两层 token 级解码约束：grammar 层（CFG/XGrammar）强制结构和词汇有效性，semantic 层通过动态 entity registry 运行时 logit masking 强制 domain/range 类型约束。评估涵盖 SciERC (7 rels)、DocRED (96 rels)、WikiEvents (EE pilot)，3 个 8B 模型 + 1 个 70B 模型。核心结果：LoRA + greedy S1 将 DR 降至 <0.1% (R-F1 41–47%)，beam k=4 消除所有违规类型 (1.54× latency)。论文提供了三级类型约束可判定性分类和系统消融。\n\n---\n\n## Strengths\n\n1. **问题定义清晰且有实践价值**：DR/CF/RV/ET 四类违规分类体系化，violation landscape 量化分析（SciERC 15.4%, DocRED 18.5% baseline DR）直接motivate了约束解码的必要性。\n\n2. **五路消融设计系统**：Table 1 的 unconstrained / grammar-only / GCD-equiv / semantic-only / S1 / S2 清晰隔离了各层贡献。\"Empirical enabling dependency\"（grammar 3% + semantic 24% → 组合 94%）是有信息量的 empirical finding。\n\n3. **三级可判定性分类有架构指导意义**：context-free / prefix-decidable with state / non-local 的分类为约束解码系统设计提供了概念框架——明确了哪些约束用 CFG、哪些需有状态运行时、哪些无法在线解决。[R1-S1]\n\n4. **统计方法论在核心实验上严谨**：Bootstrap CIs (10,000 iterations, document-level resampling)、Bonferroni 校正 (k=4, α_adj=0.0125)、Cohen's d (all δ≥3.0)、vLLM 外部验证。[R1-S3]\n\n5. **分析诚实度高**：坦诚 CF 引入（zero-shot 0→9.82pp, fine-tuned +1.18pp）、WikiEvents pilot 限制（n=20, MDE≈±5pp）、GoLLIE 对比不可行原因、κ 统计效力不足。30 页附录覆盖近乎所有 reviewer concern。[R1-S4, R2-S3]\n\n6. **工程贡献实用**：grammar-first fallback 保持 JSON 完整性；continuation masking 跨 3 个 tokenizer family 工作；runtime overhead 合理（fine-tuned S1 仅 +10%）；INT4 quantization 不影响 enforcement。[R1-S5, R2-S5-6]\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**MF1** [critical] **Proposition 1 的呈现定位过高，理论-实践 gap 桥接不充分**\n- R1-N1 + R2-N1，交叉回应后达成部分共识。\n- Proposition 1 证明无界实体集下 domain/range 约束非 context-free——证明技术本身是标准的（pumping lemma），论文自称 \"well-known intuition\" 的形式化。\"Engineering applicability\" 段用 DFA 状态数 $O(|\\mathcal{E}|^{|\\text{entities}|}) > 10^{17}$ 桥接有界场景，但 (a) 这是复杂度论证而非形式不可能性；(b) 未给出 DFA 可行的边界条件（如 SciERC: 6 types, ~10 entities → $6^{10} \\approx 6 \\times 10^7$，可能可行）；(c) proof sketch 在正文中仅 3 行，读者需翻 Appendix O 才能评估。\n- **R1 与 R2 分歧**：R2 认为 Prop 1 trivial，整体降格为纯工程贡献；R1 认为三级分类法有架构指导价值，Prop 1 的应用意义超过证明技术本身。\n- **Director 判定**：R1 的 rebuttal 有说服力——三级分类法确实为约束解码架构设计提供了有用的概念框架，论文贡献并非仅 Proposition 1 一个定理。但当前呈现方式确实将 Prop 1 过度包装为 \"theoretical grounding\"（§1 Contribution 1）。此问题属于 **framing/呈现**，非实质缺陷。\n- **建议**：(1) §3 明确区分理论不可能性（无界）与工程不可行性（有界指数级），给出 DFA 可行边界；(2) 将 Prop 1 定位为 \"formalizing a known intuition for the IE setting\" 而非暗示全新理论发现；(3) 扩展 proof sketch 引用 pumping lemma 核心直觉。\n\n**MF2** [critical] **κ-DR 相关性 n=3, p=0.138 在正文和 Abstract 中呈现不当**\n- R1-N2 + R2 AGREE（完全共识）。\n- §4 标注了 \"descriptive (n=3, p=0.138)\"，但 Abstract 第 3 段仍用 \"rates correlate with schema restrictiveness\"，§1 Contribution 2 同样暗示因果关联。附录回归线拟合 3 个点无统计意义。\n- **建议**：Abstract/§1 将 \"correlate\" 统一替换为 \"observed pattern across three schemas, insufficient for statistical inference\"；附录回归线标注 \"illustrative only, n=3\" 或移除。\n\n**MF3** [critical] **70B 验证单一模型族 + 无 FP16 基线，Contribution 2 \"4 models\" 表述误导**\n- R1-N3 + R2 AGREE（完全共识）。\n- 70B 仅 Llama-3.1-70B-Instruct (AWQ INT4)。无 Qwen-70B 或其他族验证。S2 在 70B 退化 -8.45pp 的解释（\"over-constraining\"）是 post-hoc 的，缺乏机制性证据。Contribution 2 声称 \"4 models spanning 8B–70B\" 实为 3×8B FP16 + 1×70B INT4，misrepresent 了验证范围。\n- **建议**：(1) 将 70B 定位为 \"preliminary single-family validation\"；(2) Contribution 2 拆分 8B/70B 声明层级；(3) 为 S2 退化提供机制性解释或标注 \"requires further investigation\"。\n\n### Should-Fix（影响评分但不一票否决）\n\n**SF1** [warning] **缺乏与强 baseline 的明确定位声明**\n- R2-N2，R1 rebut 认为已有 GCD-equiv/post-hoc filtering/GoLLIE 三类对比。Director 判定 R1 rebuttal 部分成立——论文确实提供了多层对比，但正文未明确声明 OntoCoDec 是约束执行方法而非 IE 系统。\n- **建议**：§1 或 §5 增加定位声明：\"OntoCoDec is a constraint enforcement method, complementary to training-based schema-aware approaches\"；考虑增加 post-hoc type repair（修复而非丢弃）baseline。\n\n**SF2** [warning] **R-F1 41–47% 在正文中缺乏上下文**\n- R2-N3，R1 rebut 有效（task setting 不同，supervised span-based 方法不可比）。但正文（§5 Setup）完全未提及 LLM-based generative RE 的典型 F1 范围，仅在 Appendix 有 SOTA 参考。\n- **建议**：§5 Setup 增加 1-2 句定位说明。\n\n**SF3** [warning] **WikiEvents pilot Table 3 正文位置具误导性**\n- R1-W2 + R2-W1（完全共识）。n=20, MDE≈±5pp, 所有对比未达显著性。Table 3 在正文中与 Table 1/2（551/998 docs 完整评估）等位呈现。\n- **建议**：Table 3 移至 Appendix，正文用 1-2 句概述 pilot 结论。\n\n**SF4** [warning] **First-seen semantics 级联错误影响未量化**\n- R1-W1 + R2 AGREE（完全共识）。245 CF violations 中多少源于 first-seen 错误 vs 合法类型歧义（Generic↔X）未分离。\n- **建议**：增加统计——多次出现实体中 first-seen type 与 gold type 不一致比例及其导致的 CF 数。\n\n**SF5** [warning] **§7 Discussion 仅 8 行过于压缩**\n- R2-W3 + R1 隐含同意。缺少 DR↔CF trade-off 定量讨论、与 training-based enforcement 互补关系、per-triple vs global enforcement 根本张力。\n- **建议**：压缩 §6 Related Work（当前约 1.5 页偏长）释放空间，§7 扩展至少 3 段。\n\n**SF6** [warning] **Contribution 2 过度打包**\n- R2-W5 + R1 AGREE（完全共识）。一个 bullet 包含 4 models × 2 precisions × 2 datasets + pilot + scale interaction。\n- **建议**：拆分为 2-3 条聚焦的贡献。\n\n**SF7** [warning] **LoRA 超参从 SciERC 直接转移到 DocRED 缺乏论证**\n- R1-W4 + R2 AGREE（完全共识）。SciERC (7 rels, 551 短句) vs DocRED (96 rels, 998 长文档) 差异大。\n- **建议**：Appendix 增加 DocRED LoRA rank/α 敏感性分析（至少 2-3 配置）；或正文承认超参转移可能低估 DocRED 潜力。\n\n**SF8** [warning] **Beam search 作为 CF 解决方案的实用性讨论不足**\n- R1-W5 + R2-W2（共识）。k=4 1.54× latency，但未讨论 k=2 是否足够、70B 内存开销、fine-tuned 下 CF 已低时 beam 边际收益。\n- **建议**：增加 beam width sensitivity 讨论和 fine-tuned 下边际收益评估。\n\n### Minor（不影响接收）\n\n- GCD-equiv 等价性仅 Qwen3-8B 验证（R1-W3, R2 AGREE severity 低）——建议脚注说明\n- 约束来源（训练数据 vs 形式本体）在 §2/§5 区分不够明确（R2-W4, R1 部分 rebut）——建议增加区分说明\n- Abstract \"Composed with LoRA fine-tuning\" 认知负担高——建议调整语序\n- Table 1 caption \"F1 ×100\" 易被忽略——建议表头标注 \"F1 (%)\"\n- \"Engineering applicability\" 段与 proof sketch 之间缺过渡（R1 minor 4）\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 达成完全共识 [AGREE]：\n1. κ-DR n=3 相关性在正文中呈现方式不当（MF2）\n2. 70B 验证范围不足以支撑 \"scale robustness\" claim（MF3）\n3. WikiEvents pilot Table 3 应移出正文或加强 caveat（SF3）\n4. First-seen semantics 级联错误缺乏量化（SF4）\n5. §7 Discussion 过于压缩（SF5）\n6. Contribution 2 过度打包（SF6）\n7. LoRA 超参跨数据集转移缺乏论证（SF7）\n8. Beam search CF 缓解实用性讨论不足（SF8）\n\n## Reviewer Divergence\n\n以下问题存在分歧，各方理由记录：\n\n**D1: Proposition 1 的 novelty 价值**\n- R2 (3.0): Trivial——PDA 无法随机访问是基础知识，论文降格为纯工程贡献\n- R1 (3.5): 三级分类法有架构指导价值——Prop 1 在 IE 设定下的应用意义超过证明技术本身\n- Director：R1 rebuttal 部分有效。分类法确有贡献，但呈现定位过高。纳入 MF1 但核心是呈现问题。\n\n**D2: 强 baseline 是否充分**\n- R2: 仅与 grammar-only strawman 比较，缺 GoLLIE/KnowCoder 可比实验\n- R1: 论文已有 GCD-equiv + post-hoc filtering + GoLLIE 三层对比；OntoCoDec 是约束执行方法非 IE 系统，要求 R-F1 对标是范畴错误\n- Director：R1 rebuttal 大部分有效。论文定位声明缺失是主因，非实质缺少对比。降为 SF1。\n\n**D3: R-F1 41–47% 的绝对质量**\n- R2: 与 SOTA (50%+/60%+) 差距大，削弱约束执行的实际意义\n- R1: Task setting 完全不同（generative LLM vs supervised span-based），41–47% 在 LLM-based generative RE 中合理\n- Director：R1 rebuttal 有效。Supervised 对标不恰当。但正文确需上下文定位。降为 SF2。\n\n---\n\n## Questions（需作者澄清）\n\n1. **Q1**: Proposition 1 proof sketch 中 position-based indexing 的简化不影响结论——能否提供更正式的论证说明 name-based referencing 不会使语言变为 context-free？[R1-Q1; R2 代论文 rebut 但应由作者确认]\n\n2. **Q2**: Fine-tuned 设置下 fallback triple 的 precision 是多少？如果 fallback 总导致错误输出，0.46% 触发率意味着 ~6% 文档受影响。[R1-Q4]\n\n3. **Q3**: 70B S2 退化 -8.45pp 的机制性原因？是否与 INT4 量化加剧过约束有关？8B 上 FP16 vs INT4 的 S2 表现是否有差异？[R1-Q3, R2 AGREE]\n\n4. **Q4**: Per-relation κ 分层 DR reduction 分析——低 κ 时 semantic layer 的边际效果是否系统性减弱？EVALUATE-FOR (κ=0.361) 的非零 violation 是否代表了一个系统性边界？[R1-Q5, R2 AGREE]\n\n---\n\n## Missing References\n\n两位 Reviewer 共提出 7 条 missing reference，经交叉验证后：\n\n**需要验证并考虑引用的**：\n1. KG-Trie (arXiv:2410.13080) — Trie 编码 KG 约束到解码过程 [R2]\n2. Dialogue Ontology RE via Constrained CoT (arXiv:2408.02361) — ontology 约束 + CoT [R2]\n3. Outlines 2024-2025 更新 — regex-based constraints + jump-forward optimization [R1; R2 认为核心仍是 CFG，影响较小]\n\n**可能不存在/需进一步确认的**：\n4. SciDC (arXiv:2604.06603, Apr 2026) — 2026 年 4 月论文，可能是 concurrent work [R2; 需验证真实性]\n5. Format Tax (arXiv:2604.03616, 2026) — 需核实是否与已引用 FormaTax 为同一工作 [R2]\n6. NuneroPlan (Zhu et al., 2024) — R2 搜索未找到，**可能是 R1 hallucinated reference** [R1; R2 REBUT]\n7. Dong et al. (2024) RAG schema-compliant IE — R2 找到最接近匹配为 arXiv:2505.08690 (2025)，**出处无法验证** [R1; R2 REBUT]\n\n---\n\n## External Review\n\n**状态**：未配置。项目未启用 paperreview.ai 外部审稿。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**：已完成（4 warnings, 0 critical, 12 info）\n\n**Warnings**：\n1. 前两页纯文本无 display item，Figure 1 到第 3 页才出现——建议提前至第 2 页加速认知锚定\n2. 主文 8 页仅 4 个 display items（1 fig + 3 tables），对实证论文偏少（推荐 5-8 个）——缺少主结果可视化图表（如 DR/F1 trade-off bar chart）\n3. Page 4-5 连续两页纯文本（Method §3.2-3.4 + §4），视觉节奏单调——建议插入约束组合示例图或伪代码\n4. Page 8 Related Work + Discussion 纯文本，审稿人快速扫描易疲劳\n\n**Info highlights**：Table 1/2 排版质量良好；Figure 1 架构图清晰；Limitations 长度适中符合 EMNLP 规范；无 LaTeX 错误残留或未解析引用。\n\n---\n\n## Overall Assessment\n\n**评分**: 3.5 / 5 (Borderline Conference)\n**置信度**: 4 / 5\n\n**评分理由**：\n\n论文提出了一个有清晰理论动机和系统实验验证的两层约束解码框架。核心贡献——将 IE 本体约束编译为可组合的 token 级解码约束——新颖且有实践价值。三级可判定性分类为 IE 约束解码架构提供了有用的概念框架。五路消融设计系统，统计方法论在核心实验上严谨，30 页附录展现高度科学诚实度。\n\n主要顾虑：\n1. **Novelty 天花板**（R1/R2 分歧焦点）：核心方法是 XGrammar + stateful logits processor 的系统集成。Proposition 1 的证明技术标准，分类法有指导价值但不构成深层理论创新。R2 认为不足以进入 main conference (3.0)，R1 认为系统贡献 + 分类法超过 Findings (3.5)。Director 认为整体贡献（分类法 + 系统设计 + 全面实证）在 Borderline Conference 水平。\n2. **统计声明**：κ-DR n=3 相关性呈现不当（MF2）；WikiEvents n=20 underpowered（SF3）。\n3. **验证覆盖度**：70B 单一模型族 + 单一精度（MF3）；LoRA 超参未跨数据集调优（SF7）。\n4. **CF trade-off 讨论不足**：greedy S1 引入 CF 作为 DR elimination 的副作用，Discussion 中讨论不充分（SF5/SF8）。\n\n**可修改性**：所有 Must-Fix 和 Should-Fix 均为呈现/分析/定位问题，无需新实验（除 SF7 LoRA 敏感性）。如果 MF1-MF3 + SF1-SF2 在 revision 中得到充分回应，评分可上调至 **4.0 (Conference)**。\n\n**R1 vs R2 评分差异说明**：R1 (3.5) 认为方法论贡献超过 Findings 门槛，R2 (3.0) 认为 novelty 不足。核心分歧在于对 \"系统集成 + 形式化分析\" 的 novelty 判断标准。Director 倾向 R1 立场——三级分类法对领域有概念指导价值，全面消融和诚实的局限性分析体现了高标准的实证研究，整体超过 Findings 但尚未稳定进入 Conference 水平。\n\n---\n\n## Detailed Comments（逐节）\n\n### Abstract\n- \"rates correlate with schema restrictiveness\" → 替换为 \"observed pattern\" (MF2)\n- \"Composed with LoRA fine-tuning\" 在框架解释前出现，认知负担高 → 调整语序\n\n### §1 Introduction\n- Contribution 1：\"theoretical grounding\" 定位过高 → 改为 \"formalizing a known intuition\" (MF1)\n- Contribution 2：过度打包 → 拆分 2-3 条 (SF6)\n- 增加明确定位声明：\"constraint enforcement method, complementary to training-based approaches\" (SF1)\n\n### §2 Background\n- 更明确区分形式本体 (KAIROS) vs 训练数据推导 schema (SciERC/DocRED) (Minor)\n\n### §3 Method\n- Proposition 1 proof sketch 扩展：引用 pumping lemma 核心直觉 (MF1)\n- \"Engineering applicability\" 给出 DFA 可行边界条件 (MF1)\n- First-seen semantics：增加级联错误量化 (SF4)\n\n### §4 Constraint Composition\n- κ 相关性：统一 \"observed pattern\" 措辞 (MF2)\n- 附录回归线标注 \"illustrative only\" (MF2)\n\n### §5 Experiments\n- Setup：增加 LLM-based generative RE 典型 F1 范围 (SF2)\n- §5.1：R-F1 上下文定位 (SF2)\n- §5.2 WikiEvents：Table 3 移至 Appendix (SF3)\n- 70B：标注 \"preliminary single-family validation\" (MF3)\n- Beam search：增加 beam width sensitivity + fine-tuned 边际收益讨论 (SF8)\n\n### §6 Related Work\n- 考虑检查 KG-Trie、Dialogue Ontology RE via Constrained CoT 是否需要引用\n- 可适当压缩释放空间给 §7\n\n### §7 Discussion\n- 扩展至少 3 段：DR↔CF trade-off 定量 + training-based 互补 + per-triple vs global (SF5)",
  "project": "schema_semantic_constrained_ie",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.5 (Borderline Conference)",
  "review_chat_id": "oc_01fc90ae186a4ed432770f7601995139"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# Round 24 审稿报告 — OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints\n\n**Venue**: EMNLP 2026 (ARR) · Long Paper · Deadline 2026-05-25\n**Reviewer 编排**: R1 (方法严谨性+实验设计) · R2 (新颖性+完整性+写作)\n**流程**: Round 1 独立初审 → 交叉分享 [AGREE]/[REBUT] → 收敛 → 报告\n\n---\n\n## Summary\n\n论文提出 OntoCoDec，将 IE 本体约束编译为两层 token 级解码约束：grammar 层（CFG/XGrammar）强制结构和词汇有效性，semantic 层通过动态 entity registry 运行时 logit masking 强制 domain/range 类型约束。评估涵盖 SciERC (7 rels)、DocRED (96 rels)、WikiEvents (EE pilot)，3 个 8B 模型 + 1 个 70B 模型。核心结果：LoRA + greedy S1 将 DR 降至 <0.1% (R-F1 41–47%)，beam k=4 消除所有违规类型 (1.54× latency)。论文提供了三级类型约束可判定性分类和系统消融。\n\n---\n\n## Strengths\n\n1. **问题定义清晰且有实践价值**：DR/CF/RV/ET 四类违规分类体系化，violation landscape 量化分析（SciERC 15.4%, DocRED 18.5% baseline DR）直接motivate了约束解码的必要性。\n\n2. **五路消融设计系统**：Table 1 的 unconstrained / grammar-only / GCD-equiv / semantic-only / S1 / S2 清晰隔离了各层贡献。\"Empirical enabling dependency\"（grammar 3% + semantic 24% → 组合 94%）是有信息量的 empirical finding。\n\n3. **三级可判定性分类有架构指导意义**：context-free / prefix-decidable with state / non-local 的分类为约束解码系统设计提供了概念框架——明确了哪些约束用 CFG、哪些需有状态运行时、哪些无法在线解决。[R1-S1]\n\n4. **统计方法论在核心实验上严谨**：Bootstrap CIs (10,000 iterations, document-level resampling)、Bonferroni 校正 (k=4, α_adj=0.0125)、Cohen's d (all δ≥3.0)、vLLM 外部验证。[R1-S3]\n\n5. **分析诚实度高**：坦诚 CF 引入（zero-shot 0→9.82pp, fine-tuned +1.18pp）、WikiEvents pilot 限制（n=20, MDE≈±5pp）、GoLLIE 对比不可行原因、κ 统计效力不足。30 页附录覆盖近乎所有 reviewer concern。[R1-S4, R2-S3]\n\n6. **工程贡献实用**：grammar-first fallback 保持 JSON 完整性；continuation masking 跨 3 个 tokenizer family 工作；runtime overhead 合理（fine-tuned S1 仅 +10%）；INT4 quantization 不影响 enforcement。[R1-S5, R2-S5-6]\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**MF1** [critical] **Proposition 1 的呈现定位过高，理论-实践 gap 桥接不充分**\n- R1-N1 + R2-N1，交叉回应后达成部分共识。\n- Proposition 1 证明无界实体集下 domain/range 约束非 context-free——证明技术本身是标准的（pumping lemma），论文自称 \"well-known intuition\" 的形式化。\"Engineering applicability\" 段用 DFA 状态数 $O(|\\mathcal{E}|^{|\\text{entities}|}) > 10^{17}$ 桥接有界场景，但 (a) 这是复杂度论证而非形式不可能性；(b) 未给出 DFA 可行的边界条件（如 SciERC: 6 types, ~10 entities → $6^{10} \\approx 6 \\times 10^7$，可能可行）；(c) proof sketch 在正文中仅 3 行，读者需翻 Appendix O 才能评估。\n- **R1 与 R2 分歧**：R2 认为 Prop 1 trivial，整体降格为纯工程贡献；R1 认为三级分类法有架构指导价值，Prop 1 的应用意义超过证明技术本身。\n- **Director 判定**：R1 的 rebuttal 有说服力——三级分类法确实为约束解码架构设计提供了有用的概念框架，论文贡献并非仅 Proposition 1 一个定理。但当前呈现方式确实将 Prop 1 过度包装为 \"theoretical grounding\"（§1 Contribution 1）。此问题属于 **framing/呈现**，非实质缺陷。\n- **建议**：(1) §3 明确区分理论不可能性（无界）与工程不可行性（有界指数级），给出 DFA 可行边界；(2) 将 Prop 1 定位为 \"formalizing a known intuition for the IE setting\" 而非暗示全新理论发现；(3) 扩展 proof sketch 引用 pumping lemma 核心直觉。\n\n**MF2** [critical] **κ-DR 相关性 n=3, p=0.138 在正文和 Abstract 中呈现不当**\n- R1-N2 + R2 AGREE（完全共识）。\n- §4 标注了 \"descriptive (n=3, p=0.138)\"，但 Abstract 第 3 段仍用 \"rates correlate with schema restrictiveness\"，§1 Contribution 2 同样暗示因果关联。附录回归线拟合 3 个点无统计意义。\n- **建议**：Abstract/§1 将 \"correlate\" 统一替换为 \"observed pattern across three schemas, insufficient for statistical inference\"；附录回归线标注 \"illustrative only, n=3\" 或移除。\n\n**MF3** [critical] **70B 验证单一模型族 + 无 FP16 基线，Contribution 2 \"4 models\" 表述误导**\n- R1-N3 + R2 AGREE（完全共识）。\n- 70B 仅 Llama-3.1-70B-Instruct (AWQ INT4)。无 Qwen-70B 或其他族验证。S2 在 70B 退化 -8.45pp 的解释（\"over-constraining\"）是 post-hoc 的，缺乏机制性证据。Contribution 2 声称 \"4 models spanning 8B–70B\" 实为 3×8B FP16 + 1×70B INT4，misrepresent 了验证范围。\n- **建议**：(1) 将 70B 定位为 \"preliminary single-family validation\"；(2) Contribution 2 拆分 8B/70B 声明层级；(3) 为 S2 退化提供机制性解释或标注 \"requires further investigation\"。\n\n### Should-Fix（影响评分但不一票否决）\n\n**SF1** [warning] **缺乏与强 baseline 的明确定位声明**\n- R2-N2，R1 rebut 认为已有 GCD-equiv/post-hoc filtering/GoLLIE 三类对比。Director 判定 R1 rebuttal 部分成立——论文确实提供了多层对比，但正文未明确声明 OntoCoDec 是约束执行方法而非 IE 系统。\n- **建议**：§1 或 §5 增加定位声明：\"OntoCoDec is a constraint enforcement method, complementary to training-based schema-aware approaches\"；考虑增加 post-hoc type repair（修复而非丢弃）baseline。\n\n**SF2** [warning] **R-F1 41–47% 在正文中缺乏上下文**\n- R2-N3，R1 rebut 有效（task setting 不同，supervised span-based 方法不可比）。但正文（§5 Setup）完全未提及 LLM-based generative RE 的典型 F1 范围，仅在 Appendix 有 SOTA 参考。\n- **建议**：§5 Setup 增加 1-2 句定位说明。\n\n**SF3** [warning] **WikiEvents pilot Table 3 正文位置具误导性**\n- R1-W2 + R2-W1（完全共识）。n=20, MDE≈±5pp, 所有对比未达显著性。Table 3 在正文中与 Table 1/2（551/998 docs 完整评估）等位呈现。\n- **建议**：Table 3 移至 Appendix，正文用 1-2 句概述 pilot 结论。\n\n**SF4** [warning] **First-seen semantics 级联错误影响未量化**\n- R1-W1 + R2 AGREE（完全共识）。245 CF violations 中多少源于 first-seen 错误 vs 合法类型歧义（Generic↔X）未分离。\n- **建议**：增加统计——多次出现实体中 first-seen type 与 gold type 不一致比例及其导致的 CF 数。\n\n**SF5** [warning] **§7 Discussion 仅 8 行过于压缩**\n- R2-W3 + R1 隐含同意。缺少 DR↔CF trade-off 定量讨论、与 training-based enforcement 互补关系、per-triple vs global enforcement 根本张力。\n- **建议**：压缩 §6 Related Work（当前约 1.5 页偏长）释放空间，§7 扩展至少 3 段。\n\n**SF6** [warning] **Contribution 2 过度打包**\n- R2-W5 + R1 AGREE（完全共识）。一个 bullet 包含 4 models × 2 precisions × 2 datasets + pilot + scale interaction。\n- **建议**：拆分为 2-3 条聚焦的贡献。\n\n**SF7** [warning] **LoRA 超参从 SciERC 直接转移到 DocRED 缺乏论证**\n- R1-W4 + R2 AGREE（完全共识）。SciERC (7 rels, 551 短句) vs DocRED (96 rels, 998 长文档) 差异大。\n- **建议**：Appendix 增加 DocRED LoRA rank/α 敏感性分析（至少 2-3 配置）；或正文承认超参转移可能低估 DocRED 潜力。\n\n**SF8** [warning] **Beam search 作为 CF 解决方案的实用性讨论不足**\n- R1-W5 + R2-W2（共识）。k=4 1.54× latency，但未讨论 k=2 是否足够、70B 内存开销、fine-tuned 下 CF 已低时 beam 边际收益。\n- **建议**：增加 beam width sensitivity 讨论和 fine-tuned 下边际收益评估。\n\n### Minor（不影响接收）\n\n- GCD-equiv 等价性仅 Qwen3-8B 验证（R1-W3, R2 AGREE severity 低）——建议脚注说明\n- 约束来源（训练数据 vs 形式本体）在 §2/§5 区分不够明确（R2-W4, R1 部分 rebut）——建议增加区分说明\n- Abstract \"Composed with LoRA fine-tuning\" 认知负担高——建议调整语序\n- Table 1 caption \"F1 ×100\" 易被忽略——建议表头标注 \"F1 (%)\"\n- \"Engineering applicability\" 段与 proof sketch 之间缺过渡（R1 minor 4）\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 达成完全共识 [AGREE]：\n1. κ-DR n=3 相关性在正文中呈现方式不当（MF2）\n2. 70B 验证范围不足以支撑 \"scale robustness\" claim（MF3）\n3. WikiEvents pilot Table 3 应移出正文或加强 caveat（SF3）\n4. First-seen semantics 级联错误缺乏量化（SF4）\n5. §7 Discussion 过于压缩（SF5）\n6. Contribution 2 过度打包（SF6）\n7. LoRA 超参跨数据集转移缺乏论证（SF7）\n8. Beam search CF 缓解实用性讨论不足（SF8）\n\n## Reviewer Divergence\n\n以下问题存在分歧，各方理由记录：\n\n**D1: Proposition 1 的 novelty 价值**\n- R2 (3.0): Trivial——PDA 无法随机访问是基础知识，论文降格为纯工程贡献\n- R1 (3.5): 三级分类法有架构指导价值——Prop 1 在 IE 设定下的应用意义超过证明技术本身\n- Director：R1 rebuttal 部分有效。分类法确有贡献，但呈现定位过高。纳入 MF1 但核心是呈现问题。\n\n**D2: 强 baseline 是否充分**\n- R2: 仅与 grammar-only strawman 比较，缺 GoLLIE/KnowCoder 可比实验\n- R1: 论文已有 GCD-equiv + post-hoc filtering + GoLLIE 三层对比；OntoCoDec 是约束执行方法非 IE 系统，要求 R-F1 对标是范畴错误\n- Director：R1 rebuttal 大部分有效。论文定位声明缺失是主因，非实质缺少对比。降为 SF1。\n\n**D3: R-F1 41–47% 的绝对质量**\n- R2: 与 SOTA (50%+/60%+) 差距大，削弱约束执行的实际意义\n- R1: Task setting 完全不同（generative LLM vs supervised span-based），41–47% 在 LLM-based generative RE 中合理\n- Director：R1 rebuttal 有效。Supervised 对标不恰当。但正文确需上下文定位。降为 SF2。\n\n---\n\n## Questions（需作者澄清）\n\n1. **Q1**: Proposition 1 proof sketch 中 position-based indexing 的简化不影响结论——能否提供更正式的论证说明 name-based referencing 不会使语言变为 context-free？[R1-Q1; R2 代论文 rebut 但应由作者确认]\n\n2. **Q2**: Fine-tuned 设置下 fallback triple 的 precision 是多少？如果 fallback 总导致错误输出，0.46% 触发率意味着 ~6% 文档受影响。[R1-Q4]\n\n3. **Q3**: 70B S2 退化 -8.45pp 的机制性原因？是否与 INT4 量化加剧过约束有关？8B 上 FP16 vs INT4 的 S2 表现是否有差异？[R1-Q3, R2 AGREE]\n\n4. **Q4**: Per-relation κ 分层 DR reduction 分析——低 κ 时 semantic layer 的边际效果是否系统性减弱？EVALUATE-FOR (κ=0.361) 的非零 violation 是否代表了一个系统性边界？[R1-Q5, R2 AGREE]\n\n---\n\n## Missing References\n\n两位 Reviewer 共提出 7 条 missing reference，经交叉验证后：\n\n**需要验证并考虑引用的**：\n1. KG-Trie (arXiv:2410.13080) — Trie 编码 KG 约束到解码过程 [R2]\n2. Dialogue Ontology RE via Constrained CoT (arXiv:2408.02361) — ontology 约束 + CoT [R2]\n3. Outlines 2024-2025 更新 — regex-based constraints + jump-forward optimization [R1; R2 认为核心仍是 CFG，影响较小]\n\n**可能不存在/需进一步确认的**：\n4. SciDC (arXiv:2604.06603, Apr 2026) — 2026 年 4 月论文，可能是 concurrent work [R2; 需验证真实性]\n5. Format Tax (arXiv:2604.03616, 2026) — 需核实是否与已引用 FormaTax 为同一工作 [R2]\n6. NuneroPlan (Zhu et al., 2024) — R2 搜索未找到，**可能是 R1 hallucinated reference** [R1; R2 REBUT]\n7. Dong et al. (2024) RAG schema-compliant IE — R2 找到最接近匹配为 arXiv:2505.08690 (2025)，**出处无法验证** [R1; R2 REBUT]\n\n---\n\n## External Review\n\n**状态**：未配置。项目未启用 paperreview.ai 外部审稿。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**：已完成（4 warnings, 0 critical, 12 info）\n\n**Warnings**：\n1. 前两页纯文本无 display item，Figure 1 到第 3 页才出现——建议提前至第 2 页加速认知锚定\n2. 主文 8 页仅 4 个 display items（1 fig + 3 tables），对实证论文偏少（推荐 5-8 个）——缺少主结果可视化图表（如 DR/F1 trade-off bar chart）\n3. Page 4-5 连续两页纯文本（Method §3.2-3.4 + §4），视觉节奏单调——建议插入约束组合示例图或伪代码\n4. Page 8 Related Work + Discussion 纯文本，审稿人快速扫描易疲劳\n\n**Info highlights**：Table 1/2 排版质量良好；Figure 1 架构图清晰；Limitations 长度适中符合 EMNLP 规范；无 LaTeX 错误残留或未解析引用。\n\n---\n\n## Overall Assessment\n\n**评分**: 3.5 / 5 (Borderline Conference)\n**置信度**: 4 / 5\n\n**评分理由**：\n\n论文提出了一个有清晰理论动机和系统实验验证的两层约束解码框架。核心贡献——将 IE 本体约束编译为可组合的 token 级解码约束——新颖且有实践价值。三级可判定性分类为 IE 约束解码架构提供了有用的概念框架。五路消融设计系统，统计方法论在核心实验上严谨，30 页附录展现高度科学诚实度。\n\n主要顾虑：\n1. **Novelty 天花板**（R1/R2 分歧焦点）：核心方法是 XGrammar + stateful logits processor 的系统集成。Proposition 1 的证明技术标准，分类法有指导价值但不构成深层理论创新。R2 认为不足以进入 main conference (3.0)，R1 认为系统贡献 + 分类法超过 Findings (3.5)。Director 认为整体贡献（分类法 + 系统设计 + 全面实证）在 Borderline Conference 水平。\n2. **统计声明**：κ-DR n=3 相关性呈现不当（MF2）；WikiEvents n=20 underpowered（SF3）。\n3. **验证覆盖度**：70B 单一模型族 + 单一精度（MF3）；LoRA 超参未跨数据集调优（SF7）。\n4. **CF trade-off 讨论不足**：greedy S1 引入 CF 作为 DR elimination 的副作用，Discussion 中讨论不充分（SF5/SF8）。\n\n**可修改性**：所有 Must-Fix 和 Should-Fix 均为呈现/分析/定位问题，无需新实验（除 SF7 LoRA 敏感性）。如果 MF1-MF3 + SF1-SF2 在 revision 中得到充分回应，评分可上调至 **4.0 (Conference)**。\n\n**R1 vs R2 评分差异说明**：R1 (3.5) 认为方法论贡献超过 Findings 门槛，R2 (3.0) 认为 novelty 不足。核心分歧在于对 \"系统集成 + 形式化分析\" 的 novelty 判断标准。Director 倾向 R1 立场——三级分类法对领域有概念指导价值，全面消融和诚实的局限性分析体现了高标准的实证研究，整体超过 Findings 但尚未稳定进入 Conference 水平。\n\n---\n\n## Detailed Comments（逐节）\n\n### Abstract\n- \"rates correlate with schema restrictiveness\" → 替换为 \"observed pattern\" (MF2)\n- \"Composed with LoRA fine-tuning\" 在框架解释前出现，认知负担高 → 调整语序\n\n### §1 Introduction\n- Contribution 1：\"theoretical grounding\" 定位过高 → 改为 \"formalizing a known intuition\" (MF1)\n- Contribution 2：过度打包 → 拆分 2-3 条 (SF6)\n- 增加明确定位声明：\"constraint enforcement method, complementary to training-based approaches\" (SF1)\n\n### §2 Background\n- 更明确区分形式本体 (KAIROS) vs 训练数据推导 schema (SciERC/DocRED) (Minor)\n\n### §3 Method\n- Proposition 1 proof sketch 扩展：引用 pumping lemma 核心直觉 (MF1)\n- \"Engineering applicability\" 给出 DFA 可行边界条件 (MF1)\n- First-seen semantics：增加级联错误量化 (SF4)\n\n### §4 Constraint Composition\n- κ 相关性：统一 \"observed pattern\" 措辞 (MF2)\n- 附录回归线标注 \"illustrative only\" (MF2)\n\n### §5 Experiments\n- Setup：增加 LLM-based generative RE 典型 F1 范围 (SF2)\n- §5.1：R-F1 上下文定位 (SF2)\n- §5.2 WikiEvents：Table 3 移至 Appendix (SF3)\n- 70B：标注 \"preliminary single-family validation\" (MF3)\n- Beam search：增加 beam width sensitivity + fine-tuned 边际收益讨论 (SF8)\n\n### §6 Related Work\n- 考虑检查 KG-Trie、Dialogue Ontology RE via Constrained CoT 是否需要引用\n- 可适当压缩释放空间给 §7\n\n### §7 Discussion\n- 扩展至少 3 段：DR↔CF trade-off 定量 + training-based 互补 + per-triple vs global (SF5)",
    "project": "schema_semantic_constrained_ie",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.5 (Borderline Conference)",
    "review_chat_id": "oc_01fc90ae186a4ed432770f7601995139"
  }
}
```

</details>

---


### Tool result

_source line 2459 · 2026-05-23T09:39:53.048605+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_2216d5b8b87a9472ce204aba11481390:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4219
}
```

</details>

---


### Assistant

_source line 2460 · 2026-05-23T09:40:04.917788+00:00_

Round 24 审稿完成。报告已投递给 Research Director。

**审稿结果摘要**：

**Overall: 3.5 (Borderline Conference)** · R1: 3.5 / R2: 3.0

**3 个 Must-Fix**：
1. Proposition 1 呈现定位过高——proof sketch 过简，理论/工程 gap 桥接不充分，需重新定位为 "formalizing a known intuition"
2. κ-DR 相关性 n=3 p=0.138——Abstract/§1 仍用 "correlate"，需统一为 "observed pattern"
3. 70B 验证单一模型族——Contribution 2 "4 models" 误导，需拆分声明层级并标注 preliminary

**8 个 Should-Fix**：定位声明缺失、R-F1 上下文缺失、WikiEvents Table 移 appendix、first-seen 级联量化、Discussion 扩展、Contribution 打包、LoRA 超参论证、beam search 实用性

**核心判断**：所有问题均为呈现/分析/定位问题，无需新实验。如 MF1-3 + SF1-2 在 revision 中充分回应，评分可上调至 **4.0 (Conference)**。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director"
}
```

</details>

---


## Round 179

## Round 179

2 recorded events


### User

_source line 2461 · 2026-05-23T09:40:06.055798+00:00_

[Reviewer 1 审稿结果]:
已完成对 R2 所有 Must-Fix（N1-N3）和 Should-Fix（W1-W5）问题的逐条回应，以及 Missing References 的评估。回应已提交给 Review Director。

要点总结：
- **R2-N1**（Proposition 1 trivial）：[REBUT] — 证明技术虽标准，但三级可判定性分类法是非平凡的架构设计指导
- **R2-N2**（缺强 baseline）：[REBUT] — 论文已有 GCD-equiv + post-hoc filtering + GoLLIE 三类对比，R2 的"仅 strawman"描述不准确
- **R2-N3**（R-F1 绝对值低）：[REBUT] — 与 supervised span-based 方法对标不恰当，论文是约束执行方法而非 IE 系统
- **R2-W1/W3/W5**：[AGREE]
- **R2-W2**：[AGREE]，但指出 R2 的 12% CF 数据可能有误（Table 1 显示 S1 CF=4.23%）
- **R2-W4**：[REBUT]，WikiEvents 确实使用形式本体（KAIROS），但同意 SciERC/DocRED 的约束来源应更清晰区分
- 维持 R1 评分 3.5，认为 R2 的 3.0 偏低

---

[Reviewer 2 审稿结果]:
交叉回应已发送给 Review Director。

核心结论：R1 的 3 个 Must-Fix 和 5 个 Should-Fix **全部 AGREE**，但指出 R1 的两处事实错误：
1. "Figure 2 回归线" 应为附录图（主文仅有 Figure 1）
2. R1-Q2 引用的 RV 数据（1.76→4.76）与 Table 1 不符（实为 1.39→1.51）

R1 的 3 个 Missing References 中 2 个（NuneroPlan、Dong et al. 2024）经 web search 无法验证，可能是幻觉引用，建议 Director 核实。

两位 Reviewer 的分析角度互补——R1 偏理论严谨性和统计有效性，我偏 novelty 和 baseline 对比——共同指向同一结论：**Findings 水平（3.0），不足以支撑 main conference**。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 2462 · 2026-05-23T09:40:21.151176+00:00_

Round 24 审稿报告已提交至 Research Director。

**汇总**：

| 维度 | 结果 |
|------|------|
| Overall | **3.5 (Borderline Conference)** |
| R1 评分 | 3.5 (Borderline Conference) |
| R2 评分 | 3.0 (Findings) |
| Must-Fix | 3 条（Prop 1 呈现、κ-DR n=3 措辞、70B 单模型族） |
| Should-Fix | 8 条 |
| 共识问题 | 8 条完全共识 |
| 分歧问题 | 3 条（novelty 判断、baseline 充分性、R-F1 定位）——均已记录各方理由 |

**核心判断**：论文工程质量高、分析诚实，三级分类法有概念贡献，整体超过 Findings 但未稳定进入 Conference。所有 Must-Fix 均为呈现/定位问题，无需新实验，修改后评分可上调至 4.0。

Issue Tracker 已同步更新（12 条 open issues）。视觉审查结果已纳入报告（4 warnings, 0 critical）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director"
}
```

</details>

---


## Round 180

## Round 180

40 recorded events


### User

_source line 2463 · 2026-05-23T10:25:19.024115+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: schema_semantic_constrained_ie
- 论文路径: artifacts/_project/paper/main.tex
- 目标 venue: EMNLP 2026
- 截止日期: 2026-05-25
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 2464 · 2026-05-23T10:25:24.868214+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 2465 · 2026-05-23T10:25:24.919529+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 2466 · 2026-05-23T10:25:34.057987+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__get_visual_check_status",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__get_visual_check_status",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 2467 · 2026-05-23T10:25:34.058347+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2468 · 2026-05-23T10:25:43.772538+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "schema_semantic_constrained_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "schema_semantic_constrained_ie"
  }
}
```

</details>

---


### Tool call

_source line 2469 · 2026-05-23T10:25:44.325902+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
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

_source line 2470 · 2026-05-23T10:25:44.376698+00:00_

{"result":"# 项目 schema_semantic_constrained_ie 概况\n\n## 实验状态 (164 个)\n\n- **llama_scierc_full_s1**: DONE (success) — \n- **llama_scierc_unconstrained**: DONE (success) — \n- **phase2_scierc_full_s1**: DONE (success) — \n- **phase2_scierc_semantic_only**: DONE (success) — \n- **phase2_scierc_grammar_only**: DONE (success) — \n- **phase2_scierc_unconstrained**: DONE (success) — \n- **phase2_docred_full_s1**: DONE (success) — \n- **phase2_docred_semantic_only**: DONE (success) — \n- **phase2_docred_unconstrained**: DONE (success) — \n- **mvp_phase0_docred_schema_r2**: DONE (killed) — \n- **phase2_s2_pilot50**: DONE (success) — \n- **mvp_phase0_docred_schema**: DONE (success) — \n- **mvp_phase0_violation_rate_docred**: DONE (success) — \n- **mvp_phase0_scierc_schema**: DONE (success) — \n- **mvp_phase0_violation_rate**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-23\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| sf2_70b_prompt_sensitivity | 70B LLaMA-3.1 constrained decoding should show consistent violation reduction across different prompt styles, similar to the 8B result where ΔDR was 94.0-94.6% regardless of prompt variant. | — | — | — |\n\n## 待处理\n- r16_70b_lora_scierc_eval: 70B AWQ INT4 LoRA fine-tuned on SciERC will achieve higher R-F1 than 8B FT (Qwen 47.15, Llama 46.13) and S1 constraints will maintain DR→0% at 70B scale（准备中）\n- p1_llama_ee_ft（准备中）\n\n## 近期结论\n- **eval_70b_lora_docred_200_full_s2** (negative): Full S2 (grammar+semantic+repair) on 70B LoRA DocRED should achieve near-zero DR while maintaining R_F1 close to beam4_s1 (48.14). The repair layer resolves residual DR violations from S1. This is the strongest constraint configuration for DocRED LoRA. ← 基于 eval_70b_lora_docred_200_beam4_s1\n- **sf2_qwen_int4_docred_s1** (success): AWQ INT4 quantization of fine-tuned Qwen3-8B does not significantly affect constraint enforcement or extraction quality on DocRED S1, mainta
…[truncated 1162 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 604
}
```

</details>

---


### Tool result

_source line 2471 · 2026-05-23T10:25:44.377255+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "ToolSearch",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 2472 · 2026-05-23T10:25:49.047330+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
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

_source line 2473 · 2026-05-23T10:25:52.262316+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex",
  "limit": "120"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex",
    "limit": "120"
  }
}
```

</details>

---


### Tool result

_source line 2474 · 2026-05-23T10:25:52.764639+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{graphicx}
11	\usepackage{booktabs}
12	\usepackage{multirow}
13	\usepackage[table]{xcolor}
14	\usepackage{amsmath}
15	\usepackage{amssymb}
16	\usepackage{amsthm}
17	\usepackage{enumitem}
18	\usepackage{pifont}
19	\usepackage{soul}
20	\usepackage{tikz}
21	\usetikzlibrary{arrows.meta,positioning,shapes.geometric,fit,backgrounds,calc}
22	\newcommand{\TBD}[1]{\textcolor{red}{#1}}
23	
24	\title{OntoCoDec: Type-Constrained Information Extraction\\via Compiled Schema Constraints}
25	
26	\author{Anonymous ACL submission}
27	
28	\begin{document}
29	\maketitle
30	
31	% === Abstract ===
32	\input{abstract}
33	
34	% === §1 Introduction ===
35	\input{section1_introduction_draft}
36	
37	% === §2 Background ===
38	\input{section2_background}
39	
40	% === §3 Method ===
41	\input{section3_method_draft}
42	
43	% === §4 Constraint Composition ===
44	\section{Constraint Composition}
45	\label{sec:composition}
46	\input{section4_composition_draft}
47	
48	% === §5 Experiments ===
49	\section{Experiments}
50	\label{sec:experiments}
51	
52	\input{section3_violation_landscape}
53	
54	\input{section5_scierc_draft}
55	\input{section5_wikievents_draft}
56	\input{section5_runtime}
57	
58	% === §6 Related Work ===
59	\input{section6_related_work}
60	
61	% === §7 Discussion and Conclusion ===
62	\section{Discussion and Conclusion}
63	\label{sec:discussion}
64	\input{section7_conclusion_compressed}
65	
66	% === Limitations (ARR requirement: standalone section, does not count toward page limit) ===
67	\clearpage
68	\section*{Limitations}
69	
70	\paragraph{Constraint scope.}
71	CF is an architectural consequence of per-triple independent enforcement: CF$\leftrightarrow$DR represents a fundamental trade-off (eliminating CF re-routes violations to DR; Appendix~\ref{app:cf-dr-tradeoff}), and its impa
…[truncated 4305 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 2475 · 2026-05-23T10:25:52.765293+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "schema_semantic_constrained_ie",
  "file": "paper_checklist.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "schema_semantic_constrained_ie",
    "file": "paper_checklist.yaml"
  }
}
```

</details>

---


### Tool call

_source line 2476 · 2026-05-23T10:25:54.220639+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_25/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"NO_PDF\"",
  "description": "Check if submitted PDF exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_25/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"NO_PDF\"",
    "description": "Check if submitted PDF exists"
  }
}
```

</details>

---


### Tool result

_source line 2477 · 2026-05-23T10:25:57.238087+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines ARR"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"*SEM 2026: Commitment Link for ARR-Reviewed Papers (Deadline: 10 April 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/sem-2026-commitment-link-arr-reviewed-papers-deadline-10-april-2026"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"5th Workshop on Evaluation and Comparison for NLP systems (Eval4NLP) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/5th-workshop-evaluation-and-comparison-nlp-systems-eval4nlp"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"}]

Based on the search results, here are the key submission guidelines for EMNLP 2026 papers related to ARR:

## Main Conference Paper Submissions

EMNLP 2026 invites submissions of long and short papers featuring substantial, original, and unpublished research on empirical methods for Natural Language Processing. Papers may contribute negative findings, survey an area, announce the creation of a new resource, argue a position, report novel linguistic insights derived using existing computational techniques, and reproduce (or fail to reproduce) previous results.

## ARR-Specific Policy for EMNLP 2026

For the ARR 2026 May cycle (which is aligned with both EMNLP and AACL), authors must explicitly declare which conference they intend to commit to at submission time. ARR 2026 May submis
…[truncated 677 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "WebSearch",
  "elapsed_ms": 8190
}
```

</details>

---


### Tool result

_source line 2478 · 2026-05-23T10:25:57.238572+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'schema_semantic_constrained_ie'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 4473
}
```

</details>

---


### Tool result

_source line 2479 · 2026-05-23T10:25:57.389931+00:00_

-rw-r--r-- 1 ubuntu ubuntu 625083 May 23 10:17 /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_25/submitted.pdf
PDF_EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Bash",
  "elapsed_ms": 3169
}
```

</details>

---


### Tool call

_source line 2480 · 2026-05-23T10:26:05.327295+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 submission format page limit anonymity guidelines ARR May cycle deadline"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 submission format page limit anonymity guidelines ARR May cycle deadline"
  }
}
```

</details>

---


### Tool call

_source line 2481 · 2026-05-23T10:26:05.729285+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "schema_semantic_constrained_ie",
  "file": "decisions.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "schema_semantic_constrained_ie",
    "file": "decisions.yaml"
  }
}
```

</details>

---


### Tool call

_source line 2482 · 2026-05-23T10:26:06.984779+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_issues.yaml 2>/dev/null && echo \"EXISTS\" || echo \"NO_FILE\"",
  "description": "Check if review_issues.yaml exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_issues.yaml 2>/dev/null && echo \"EXISTS\" || echo \"NO_FILE\"",
    "description": "Check if review_issues.yaml exists"
  }
}
```

</details>

---


### Tool result

_source line 2483 · 2026-05-23T10:26:15.822774+00:00_

Web search results for query: "EMNLP 2026 submission format page limit anonymity guidelines ARR May cycle deadline"

Links: [{"title":"Call for Papers: EMNLP 2026 Industry Track - EMNLP 2026","url":"https://2026.emnlp.org/calls/industry_track/"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"Confs: 2026 Conference on Empirical Methods in Natural ...","url":"https://www.facebook.com/linguistlist/posts/confs-2026-conference-on-empirical-methods-in-natural-language-processing-emnlp-/1351983883622556/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"EMNLP 2026 LaTeX Template | ACL Style Files & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/emnlp"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"EMNLP 2026 on X: \"Here is more precise submission policy. For full details, please check the latest CFP on our website! https://t.co/6dttoXBIT9 https://t.co/ta6IuAjIVm\" / X","url":"https://x.com/emnlpmeeting/status/2047977818928320807"},{"title":"Industry Track — Call for Papers -","url":"https://2026.eacl.org/calls/industry/"},{"title":"EMNLP: Empirical Methods in Natural Language Processing 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=883"},{"title":"Submissions | Transactions of the Association for Computational Linguistics","url":"https://transacl.org/index.php/tacl/about/submissions"}]

Based on the search results, here's information about EMNLP 2026 submission guidelines:

## Page Limits and Submission Format

The format is two-column with an 8-page limit for long papers and a 4-page limit for short papers. EMNLP uses the standard ACL style files, so the LaTeX template is identical to the one used for ACL, NAACL, and other *ACL conferences.

## Anonymity Guidelines

Papers must not include aut
…[truncated 1139 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "WebSearch",
  "elapsed_ms": 10495
}
```

</details>

---


### Tool result

_source line 2484 · 2026-05-23T10:26:15.874087+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/decisions.yaml\", \"content\": \"_next_id: 86\\ndecisions:\\n- id: D001\\n  date: 2026-05-13 17:38 UTC\\n  summary: 主目标调整为 EMNLP 2026 ARR (5/25), AAAI 2027 为后备\\n  rationale: 用户明确指出 EMNLP ARR 5/25 时间不紧、不要保守、资源会给够。12 天 AI 团队速度足够：Phase 0 (1-2天) →\\n    Phase 1 compiler (2-3天) → Phase 2 experiments (2-3天) → Paper (2-3天)。禁止 fallback\\n    思维，冲最高目标。\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-13 19:14 UTC\\n  summary: SciERC Phase 0 结果确认 GO — domain_range violation rate 15.4%，3× 超阈值\\n  rationale: 'SciERC 全量 test set (551 sentences, 1724 triples): domain_range_violation_rate\\n    = 15.4%，远超 5% go/no-go 阈值。违规分布极不均匀 (Feature-of 33.5%, Compare 42.4% vs Used-for\\n    0.76%)，支持\\\"特定 relation types 需要 decoding-time enforcement\\\"的论文 claim。DocRED dry-run\\n    (37 docs) 同样显示 14.4%。两个数据集均为 GO 信号，MVP 核心假设得到强验证。等 schema-informed prompt 结果确认\\n    prompt 级干预不足以解决问题后正式宣布 MVP 通过。'\\n  related_experiments:\\n  - exp_id: mvp_phase0_violation_rate\\n    role: primary\\n    result: domain_range_violation_rate=15.4%, go_nogo=GO\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-13 21:48 UTC\\n  summary: MVP 通过，进入 Research 阶段，立即启动 Phase 2 constrained decoding 实验\\n  rationale: Phase 0 三个实验完成：SciERC 15.4%/5.78%, DocRED 18.7% domain_range violation\\n    rate。两个数据集均远超 5% 阈值，核心假设得到强验证。Phase 1 compiler 代码就绪（36 tests 通过），Phase 2 脚本就绪（S1\\n    路径可用，S2 bug 修复中）。cuda:1 空闲，立即启动 Phase 2 SciERC grammar_only/semantic_only/full_s1\\n    实验。\\n  related_experiments:\\n  - exp_id: mvp_phase0_violation_rate\\n    role: primary\\n    result: SciERC DR=15.4%, GO\\n  - exp_id: mvp_phase0_scierc_schema\\n    role: primary\\n    result: SciERC DR=5.78%, prompt insufficient\\n  - exp_id: mvp_phase0_violation_rate_docred\\n    role: primary\\n    result: DocRED DR=18.7%, GO\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-
…[truncated 11013 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 10144
}
```

</details>

---


### Tool result

_source line 2485 · 2026-05-23T10:26:15.924974+00:00_

-rw-r--r-- 1 ubuntu ubuntu 18269 May 23 09:49 /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_issues.yaml
EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Bash",
  "elapsed_ms": 8940
}
```

</details>

---


### Tool call

_source line 2486 · 2026-05-23T10:26:21.899697+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "pdfinfo /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_25/submitted.pdf 2>/dev/null | grep -E \"Pages|Title|Author\"",
  "description": "Get PDF page count and metadata"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Bash",
  "tool_args": {
    "command": "pdfinfo /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_25/submitted.pdf 2>/dev/null | grep -E \"Pages|Title|Author\"",
    "description": "Get PDF page count and metadata"
  }
}
```

</details>

---


### Tool result

_source line 2487 · 2026-05-23T10:26:22.402636+00:00_

Title:           
Author:          
Pages:           39

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Bash",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 2488 · 2026-05-23T10:26:22.503457+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
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

_source line 2489 · 2026-05-23T10:26:22.554398+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2490 · 2026-05-23T10:26:32.047796+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_issues.yaml",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_issues.yaml",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 2491 · 2026-05-23T10:26:32.048388+00:00_

1	# Review Issues Tracker — schema_semantic_constrained_ie
2	# Updated: R24 Action Matrix dispatched, 2026-05-23
3	
4	# ============================================================
5	# Round 24 — Issues with actions dispatched
6	# ============================================================
7	
8	- id: "R16-W5"
9	  summary: "Proposition 1 定位过高 + 理论-实践 gap 桥接不充分"
10	  category: framing
11	  severity: critical
12	  status: in_progress
13	  first_raised_round: 14
14	  last_seen_round: 24
15	  mentions:
16	    - round: 19
17	      reviewers: [1, 2]
18	      note: "共识定位为 systems contribution。"
19	    - round: 23
20	      reviewers: [1, 2]
21	      note: "与 R23-W2/W7 合并。降低理论贡献措辞。"
22	    - round: 24
23	      reviewers: [1, 2]
24	      note: "R24-MF1 (critical)。R23 写作降级不够——需重写定位为 formalizing known intuition + DFA 可行边界 + proof sketch 扩展。R1/R2 分歧：R2 认为 trivial, R1 认为分类法有架构指导价值。"
25	  action_items:
26	    - round: 19
27	      action: "§7 Discussion 定位 systems contribution"
28	      assigned_to: paper_agent
29	      status: completed
30	    - round: 21
31	      action: "§3 论证 semantic layer 非显而易见"
32	      assigned_to: paper_agent
33	      status: completed
34	    - round: 23
35	      action: "降低 Proposition 1 强度 + κ 统计限定"
36	      assigned_to: paper_agent
37	      status: completed
38	    - round: 24
39	      action: "§1 C1 重写 'formalizing known intuition' + §3 DFA 可行边界(SciERC 6^10, DocRED 6^30) + proof sketch 4-5行 + 区分 theoretical impossibility vs engineering impracticality"
40	      assigned_to: paper_agent
41	      status: in_progress
42	  resolution: ""
43	  resolution_round: null
44	
45	- id: "R16-W1"
46	  summary: "κ-DR 相关性 n=3 呈现不当——Abstract/§1 仍用 correlate"
47	  category: framing
48	  severity: critical
49	  status: in_progress
50	  first_raised_round: 12
51	  last_seen_round: 24
52	  mentions:
53	    - round: 22
54	      reviewers: [1, 2]
55	      note: "R22 解决：加 empirical + scale-dependent qualifier + descriptive only。"
56	    - round: 24
57	      reviewers: [1, 2]
5
…[truncated 1638 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2492 · 2026-05-23T10:26:33.052376+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_25/submitted.pdf",
  "pages": "1-9"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_25/submitted.pdf",
    "pages": "1-9"
  }
}
```

</details>

---


### Tool result

_source line 2493 · 2026-05-23T10:26:34.059714+00:00_

PDF pages extracted: 9 page(s) from /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_25/submitted.pdf (610.4KB)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Read",
  "elapsed_ms": 1007
}
```

</details>

---


### Tool call

_source line 2494 · 2026-05-23T10:26:34.176630+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/config.yaml 2>/dev/null | grep -A 5 \"external_review\" || echo \"NO_EXTERNAL_REVIEW_CONFIG\"",
  "description": "Check external review config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/config.yaml 2>/dev/null | grep -A 5 \"external_review\" || echo \"NO_EXTERNAL_REVIEW_CONFIG\"",
    "description": "Check external review config"
  }
}
```

</details>

---


### Tool result

_source line 2495 · 2026-05-23T10:26:34.227448+00:00_

NO_EXTERNAL_REVIEW_CONFIG

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2496 · 2026-05-23T10:27:19.507113+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "schema_semantic_constrained_ie",
  "review_chat_id": "oc_01fc90ae186a4ed432770f7601995139"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "schema_semantic_constrained_ie",
    "review_chat_id": "oc_01fc90ae186a4ed432770f7601995139"
  }
}
```

</details>

---


### Tool result

_source line 2497 · 2026-05-23T10:27:43.345050+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 23837
}
```

</details>

---


### Tool call

_source line 2498 · 2026-05-23T10:27:43.395696+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "schema_semantic_constrained_ie",
  "text": "你是 Reviewer 1，负责审查 **方法严谨性 + 实验设计**。\n\n## 论文信息\n- 标题：OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints\n- Venue：EMNLP 2026（通过 ARR 统一审稿）\n- Deadline：2026-05-25\n- 格式：ACL 长文，正文 8 页限制（不含 references、limitations、ethics）\n- 匿名：double-blind\n- 论文路径：artifacts/_project/paper/main.tex\n- PDF 路径：/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_25/submitted.pdf\n\n## Overall Assessment 评分标准（EMNLP 2026 ARR）\n5 = Consider for Award（约前2.5%），4.5 = Borderline Award，4 = Conference（可被主会议接收），3.5 = Borderline Conference，3 = Findings（可被Findings接收），2.5 = Borderline Findings，2 = Resubmit next cycle，1.5 = Resubmit after next cycle，1 = Do not resubmit\n\n## 你的审查侧重\n\n### 1. 理论贡献\n- Proposition 1（Level 2 ⊄ Level 1）的证明质量：proof sketch 是否完备、是否有明显漏洞\n- 三级约束分类法（context-free / prefix-decidable with state / non-local）的定义严谨性\n- 该理论贡献的实际价值——是 formalizing known intuition 还是真正的新发现？\n\n### 2. 两层架构设计\n- Grammar layer（XGrammar）和 Semantic layer（entity registry + dynamic masking）的技术设计是否合理\n- Grammar-first fallback 机制的正确性\n- Continuation masking 的鲁棒性（对不同 tokenizer 的适应性）\n- S1 vs S2 两种解码策略的比较是否公平\n\n### 3. 实验设计\n- 消融实验的充分性（5-way ablation on SciERC, 4-way on DocRED）\n- 统计检验（bootstrap CI）的正确性和报告方式\n- κ-DR 相关性（n=3）的呈现是否恰当（是否 overclaim）\n- Baseline 选择的公平性（unconstrained、grammar-only、GCD-equiv、semantic-only、post-hoc filtering）\n- 跨模型验证的充分性（3 × 8B + 1 × 70B AWQ INT4）\n- Fine-tuning composability 的验证范围（2 × 8B full, 1 × 70B subset）\n- WikiEvents pilot（n=20）的统计效力和价值\n\n### 4. 评估指标\n- DR/RV/ET/CF 四类违规的定义和计算是否正确\n- R-F1 和 E-F1 的定义和适用性\n- violation rate 的计算口径是否一致\n\n### 5. 可重现性\n- 是否提供足够的实现细节\n- 超参数报告是否完整\n\n请给出完整的审稿意见，包含：Summary、Strengths（逐条）、Weaknesses（逐条，标注严重程度 [Critical/Major/Minor]）、Questions、Missing References、Overall Assessment（评分+置信度）。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "schema_semantic_constrained_ie",
    "text": "你是 Reviewer 1，负责审查 **方法严谨性 + 实验设计**。\n\n## 论文信息\n- 标题：OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints\n- Venue：EMNLP 2026（通过 ARR 统一审稿）\n- Deadline：2026-05-25\n- 格式：ACL 长文，正文 8 页限制（不含 references、limitations、ethics）\n- 匿名：double-blind\n- 论文路径：artifacts/_project/paper/main.tex\n- PDF 路径：/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_25/submitted.pdf\n\n## Overall Assessment 评分标准（EMNLP 2026 ARR）\n5 = Consider for Award（约前2.5%），4.5 = Borderline Award，4 = Conference（可被主会议接收），3.5 = Borderline Conference，3 = Findings（可被Findings接收），2.5 = Borderline Findings，2 = Resubmit next cycle，1.5 = Resubmit after next cycle，1 = Do not resubmit\n\n## 你的审查侧重\n\n### 1. 理论贡献\n- Proposition 1（Level 2 ⊄ Level 1）的证明质量：proof sketch 是否完备、是否有明显漏洞\n- 三级约束分类法（context-free / prefix-decidable with state / non-local）的定义严谨性\n- 该理论贡献的实际价值——是 formalizing known intuition 还是真正的新发现？\n\n### 2. 两层架构设计\n- Grammar layer（XGrammar）和 Semantic layer（entity registry + dynamic masking）的技术设计是否合理\n- Grammar-first fallback 机制的正确性\n- Continuation masking 的鲁棒性（对不同 tokenizer 的适应性）\n- S1 vs S2 两种解码策略的比较是否公平\n\n### 3. 实验设计\n- 消融实验的充分性（5-way ablation on SciERC, 4-way on DocRED）\n- 统计检验（bootstrap CI）的正确性和报告方式\n- κ-DR 相关性（n=3）的呈现是否恰当（是否 overclaim）\n- Baseline 选择的公平性（unconstrained、grammar-only、GCD-equiv、semantic-only、post-hoc filtering）\n- 跨模型验证的充分性（3 × 8B + 1 × 70B AWQ INT4）\n- Fine-tuning composability 的验证范围（2 × 8B full, 1 × 70B subset）\n- WikiEvents pilot（n=20）的统计效力和价值\n\n### 4. 评估指标\n- DR/RV/ET/CF 四类违规的定义和计算是否正确\n- R-F1 和 E-F1 的定义和适用性\n- violation rate 的计算口径是否一致\n\n### 5. 可重现性\n- 是否提供足够的实现细节\n- 超参数报告是否完整\n\n请给出完整的审稿意见，包含：Summary、Strengths（逐条）、Weaknesses（逐条，标注严重程度 [Critical/Major/Minor]）、Questions、Missing References、Overall Assessment（评分+置信度）。"
  }
}
```

</details>

---


### Tool result

_source line 2499 · 2026-05-23T10:28:01.062808+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 17667
}
```

</details>

---
