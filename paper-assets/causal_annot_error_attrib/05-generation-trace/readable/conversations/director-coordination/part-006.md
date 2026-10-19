# Director coordination — Part 6 of 8

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction** · Conversation logs

[← Part 5](part-005.md) · [Transcript overview](../director-coordination.md) · [Part 7 →](part-007.md) · [Structured JSON](../../../sessions/1d/1de11abfd142608a2277.json)

## Round 138

### User

_source line 1389 · 2026-05-23T13:54:15.381110+00:00_

[Reviewer 1 审稿结果]:
审稿报告已提交给 Review Director。

**审稿结论：3.5 分（Borderline Conference）**

核心发现：
- 3 个 Must-Fix 问题：(1) K≥3 单调性仅为 conjecture 且 60-97% 矩阵违反严格单调性；(2) 缺乏端到端实证验证 pipeline；(3) 线性 SEM 假设对 EMNLP 读者的适用性讨论不足
- 4 个 Should-Fix 问题：proportional effects 可验证性、non-differential 假设 stress test 局限、23 LLM 配置代表性、collider sign preservation 仅有经验验证
- 5 个 Minor 问题：abstract 词数、Figure 2 可读性、Algorithm 1 阈值来源等

主要优势：首次系统覆盖 7 种 DAG 拓扑的 multi-class bias 分析，K=2 证明严谨，ASV 诊断工具有实用价值。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1390 · 2026-05-23T13:54:21.287919+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 139

## Round 139

2 recorded events


### User

_source line 1391 · 2026-05-23T13:55:53.958097+00:00_

[Reviewer 1 审稿意见]:

## Reviewer 1 交叉审阅：对 Reviewer 2 的逐条回应

### Must-Fix

**[AGREE] R2-N1: Abstract 超过 200 words**
同意升级为 must-fix。我在 M1 中仅列为 minor，是审查疏漏——未执行精确词数统计。R2 确认 245 words，超出 22.5%，构成实质性 desk reject 风险。我修正评估：从 minor 升级为 must-fix。

**[REBUT] R2-N2: Correction Guidance 深度——应为 should-fix 而非 must-fix**
R2 观察准确（Section 4.5 约半页、Algorithm 1 仅在 Appendix page 30），但我认为严重程度应降级：(1) 实质性内容存在——Table 4 提供 7 拓扑 × 5 方法的完整 RMSE 对比，Appendix B.15/B.19 有充分支撑；(2) 修复路径轻量——将 Algorithm 1 移入正文、添加方法选择讨论即可；(3) contribution framing 问题对 acceptance decision 影响有限。综合判断：降级为 should-fix。

### Should-Fix

**[AGREE] R2-W1: ASV vs E-values 创新论证不充分**
ASV 的核心操作（沿 C(δ) 计算 tipping point）确实是标准 sensitivity analysis 方法。但补充：ASV 的 topology-stratification 能力（同一 C(δ) 在不同 DAG 下产生不同 ASV，Figure 3）是 E-value 框架无法自然实现的。论文应增加 worked example 展示此差异。

**[AGREE] R2-W2: Conjecture 1 缺少 K>3 证明**
与我的 N1 高度一致。我认为此问题应为 **must-fix 而非 should-fix**——60-97% 矩阵违反严格单调性（Table 10），ASV ranking 的可靠性直接依赖此单调性。支持 R2 建议标注为 open problem 并描述反例搜索 methodology。

**[AGREE] R2-W3: EMNLP 受众可达性偏低**
plim、FWL、Wald estimator、column-stochastic、Birkhoff polytope 对 NLP 读者壁垒过高。建议首次出现时添加 parenthetical 直觉解释。

**[AGREE] R2-W4: "Secondary coefficient" 定义不清**
与我的 Q5 一致。Abstract 中应明确定义或改用 "non-treatment coefficients"。

**[AGREE] R2-W5: 未引用 bib 条目**
我未检查 bib 清洁度，这是我的遗漏。应移除或引用。

### 新颖性评估

**[AGREE]** "unified 主要指系统覆盖而非统一理论"——准确。
**[AGREE]** "K≥3 Sign Reversal 是最强理论贡献"——同意。
**[REBUT]** "Correction Guidance 纯经验发现"——部分反驳。FWL invariance 的代数证明（Appendix B.2）为 routing 提供了非经验性的 structural foundation。但同意主文展示深度不足。

### Missing References

**[AGREE]** Jurek et al. (2005)——与 "beyond toward-null" 直接相关，应引用。
**[AGREE]** Valeri & VanderWeele (2014)——与 mediation measurement error (A.5) 直接相关。
**[REBUT]** Ogburn & VanderWeele (2012)——论文已通过 Edwards et al. (2021) 等覆盖相关贡献点，缺引严重性较低。

### 关键分歧总结

| 问题 | R2 评级 | R1 评估 | 状态 |
|------|--------|---------|------|
| Abstract 超字数 | Must-fix | 升级为 Must-fix | ✅ 共识 |
| Correction Guidance | Must-fix | Should-fix | ⚠️ 分歧 |
| Conjecture 1 证明缺口 | Should-fix | Must-fix | ⚠️ 分歧（我认为更严重） |
| ASV vs E-values | Should-fix | Should-fix | ✅ 共识 |

核心分歧：我认为 Conjecture 1 理论缺口比 R2 评估的更严重（must-fix），而 Correction Guidance 深度比 R2 评估的较轻（should-fix）。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1392 · 2026-05-23T13:56:01.429497+00:00_

Reviewer 1 交叉回应已收到。等待 Reviewer 2 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 140

## Round 140

2 recorded events


### User

_source line 1393 · 2026-05-23T13:56:04.028864+00:00_

[Reviewer 1 审稿结果]:
交叉审阅已提交。核心结论：

- 与 R2 在 4/7 个主要问题上达成共识（abstract 超字数、ASV 论证、术语可达性、secondary coefficient 定义）
- 两个分歧点：(1) Correction Guidance 我认为 should-fix 而非 must-fix（实质内容存在，问题在 presentation）；(2) Conjecture 1 理论缺口我认为 must-fix 而非 should-fix（ASV ranking 可靠性直接依赖 monotonicity）
- 我升级了 abstract 字数问题从 minor 到 must-fix，承认原审疏漏

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1394 · 2026-05-23T13:56:08.435140+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 141

## Round 141

10 recorded events


### User

_source line 1395 · 2026-05-23T13:56:52.617478+00:00_

[Reviewer 2 审稿意见]:

## Reviewer 2 交叉审阅回应（对 Reviewer 1 意见）

---

### Must-Fix 问题回应

**[AGREE] R1-N1: K≥3 Conjecture 1 的理论缺口**

同意这是论文的核心理论弱点。我在初审中将其列为 W2（should-fix），但经过与 R1 意见的交叉对照，我倾向于提升严重性。R1 补充的论据有效：

- Table 10（Appendix B.12, p.26）显示 60-97% 的随机矩阵违反严格单调性——虽然 worst-case deviation ≤0.013 看似很小，但这意味着 Conjecture 1 实际声称的是 "ε-approximate monotonicity" 而非 monotonicity，这在数学上是显著降级
- R1 指出 K=7 的 42 维参数空间中 10,000 个采样点的覆盖率极低，这一点我初审时未充分考虑
- 论文的 ASV vulnerability ranking（Figure 3, Section 3.3）直接依赖 monotonicity——如果单调性在某些参数区域失败，排序可能局部反转

不过，我与 R1 在"是否升级为 must-fix"上略有犹豫：worst-case deviation ≤0.013 对应的 ASV 扰动极小，实际应用中 ASV 的 decision boundary 通常远大于此。**建议折中为 borderline must-fix / strong should-fix**，取决于 AC 对理论严谨性 vs 实用性的权重。

---

**[PARTIALLY AGREE] R1-N2: 缺乏端到端实证验证**

R1 的论点有一定道理，但我不同意将其列为 must-fix。具体分析：

**R1 说得对的部分：**
- 论文声称 "correction guidance" 为三大贡献之一（Introduction, p.2），但从未展示 Algorithm 1 在真实任务上的完整 pipeline（C estimation → ASV → method selection → improved estimate vs gold-label）
- ClinicalBERT 案例（Section 4.4, p.8）仅覆盖 confounding 单一拓扑，且只是定性验证（"empirical bias ranking matches predictions"），未量化校正效果
- 这与我的 N2（Correction Guidance 深度不足）构成呼应——两个 reviewer 独立发现了同一弱点

**我不完全同意的部分：**
- 本文的核心定位是 **theoretical/analytical contribution**，不是 empirical NLP pipeline 论文。MC 验证（1.6% MAPE across 161 scenarios, Section 4.2）IS the appropriate validation for analytical results
- 要求在 HumAID/VAST 上执行完整 pipeline 涉及 ground-truth causal effect 的获取——这在观察性社会科学数据中几乎不可能（这也是 Limitations 中承认的："end-to-end demonstration with ground-truth causal effects remains future work", p.8）
- EMNLP 接收过大量纯理论/分析性工作（如 Feder et al. 2022 的 causal NLP survey, Keith et al. 2020 的 text-as-treatment framework），并非必须包含端到端实证

**我的判断：should-fix 而非 must-fix。** 但建议与我的 N2 合并处理——要么 (a) 降低 "correction guidance" 的贡献定位 + 承认端到端验证为 future work，要么 (b) 在至少一个拓扑上展示 Algorithm 1 的路由选择和校正效果。

---

**[PARTIALLY AGREE] R1-N3: 线性 SEM 假设对 EMNLP 受众的适用性**

这是一个重要问题，但我认为 should-fix 级别更合适，而非 must-fix。

**同意的部分：**
- NLP 因果推断确实最常用 logistic regression（sentiment → behavior 等二值/多分类 outcome）
- 主文 Limitations 仅一句话提及此限制（"Closed-form bias expressions assume K=3 linear SEMs", p.8），对 EMNLP 读者不够
- R1 提出的"至少对比一个拓扑下 linear vs logistic bias magnitude"是合理的最低要求

**值得注意的是论文已有部分 nonlinear 验证：**
- Appendix B.2（p.21-22）验证了 FWL invariance 在 logistic regression 下同样成立——Table 5 对比了 OLS vs logistic 的 bias breakdown，结论是 "both estimators agree: linear and logistic DGPs produce virtually identical sign-flip patterns across all seven topologies"
- Appendix B.7（p.24）的 robustness-to-nonlinear-DGP 验证中，使用 Bernoulli(C) 和 logistic DGP 估计 via logistic regression，sign-flip rates 在五种拓扑下为零
- Section 4.4 的 ClinicalBERT 案例实际上使用了 logistic regression 的 pipeline

**问题在于这些验证分散在附录中，主文几乎未提及。** 我建议：在 Section 4 正文中增加一段（~3-4句）总结 logistic regression 下的验证结果，引用 Appendix B.2 和 B.7。这比新增实验成本低得多，且能有效回应此concern。

**降级为 should-fix 的理由：** 线性模型是因果推断分析的标准起点（Carroll et al. 2006 全书以线性模型为主），EMNLP 历史上也接收过 linear-only 的因果分析论文。但主文需更显著地讨论此限制及已有的非线性验证结果。

---

### Should-Fix 问题回应

**[AGREE] R1-W1: Proportional effects 假设的可验证性**

同意。Theorem 1 的核心条件 f=λg（proportional effects）在实践中确实难以验证。R1 指出三个有效问题：(1) NLP 场景下何时合理？(2) 研究者如何判断？(3) general case 退化行为如何？

论文在 Appendix B.13（p.27）确实讨论了 proportional effects breakdown——当偏离 proportionality 时 OOB rates 从 0% 升至 ≤40%（K=3, N=50,000）。但这些内容完全在附录，主文未提及。

关于 Director 的问题"是否比 ASV novelty 更重要"——我认为这两个问题性质不同：W1 关乎**理论假设的适用性**（影响 soundness），我的 W1 关乎**方法论创新的定位**（影响 novelty/excitement）。两者都需要处理，但不构成替代关系。

---

**[AGREE] R1-W2: Non-differential misclassification stress test 局限性**

同意。NLP 任务中文本通常同时包含 A（treatment）和 Y（outcome）的信息，LLM 标注 A 时可能隐性地依赖 Y 的文本线索，违反 non-differential 假设。论文的 stress test（Appendix B.5-B.6）：
- 仅用 5 个 VAST topics，per-topic samples ≤29（Table 7, p.23）
- 只检查 uniform perturbation（在对角线上加噪声）
- 没有检查 structured violation（如 Y-dependent misclassification rate）

建议在 Limitations 或 Appendix 中增加讨论：NLP 中哪些场景容易产生 differential misclassification（如 sentiment labels from text that also reveals the outcome），以及这如何影响论文结论。

---

**[PARTIALLY AGREE] R1-W3: 23 LLM 配置的代表性**

R1 指出缺少 GPT-4、Claude 等商业模型。这一观察成立，但我认为严重性较低：
- 论文的核心贡献是理论框架，不是 LLM benchmark。23 个配置用于**验证理论预测**而非**覆盖所有 LLM**
- 实际 confusion matrix 的关键特征是 diagonal dominance 和 off-diagonal structure，论文已覆盖 diagonal 范围 0.45-0.81（Section 4.4），这包括了大多数实用 LLM 的精度区间
- 补充 GPT-4/Claude 矩阵在技术上容易（只需计算 confusion matrix），但不会改变理论结论

建议在讨论中增加一句话说明：配置多样性的关键维度是 confusion matrix 的结构属性（diagonal dominance, off-diagonal symmetry），而非特定 LLM 品牌。

---

**[AGREE] R1-W4: Collider sign preservation 仅有经验验证**

同意，这是我初审时遗漏的一个理论缺口。

Table 2（p.20）明确标注 collider 的 sign preservation 为 "Empirical"（verified across 100,000 random column-stochastic matrices with zero violations），而 confounding 有代数证明（Cauchy-Schwarz, Appendix A.1），mediation 和 front-door 也有 proved 状态。

进一步检查 Appendix A.6（p.17）：collider 的 bias decomposition 是解析推导的（Proposition 5 证明了 proportional case, Proposition 6 证明了 general case 的 bound），但 Proposition 5 条件 h(A)=λg(A) 并非总成立，而 general case（Proposition 6）只证明了 |B(C)| ≤ |B_Berkson|（bias magnitude bounded），sign preservation 的最终结论依赖 100,000 矩阵的数值验证。

这确实削弱了 Proposition 1 的统一性——(a) confounding 有代数证明，(b) collider 仅有经验验证。论文 Proposition 1 的表述将两者并列，可能给读者造成两者同等严谨的印象。

建议：(a) 在 Proposition 1 或 Table 2 中明确区分 proved vs empirically verified；(b) 如果能将 Proposition 6 的 bound 推广为 sign preservation 的充分条件会最佳，否则应标注为 conjecture。

---

### 小问题回应

**[AGREE] R1-M1: Abstract 字数** — 我的初审已将此列为 N1 (must-fix)。实际计数为 245 words，远超 200 限制。R1 说"接近限制"可能是低估了。

**[AGREE] R1-M2: Figure 2 灰度打印** — 与我的小问题#1 一致。

**[AGREE] R1-M3: Algorithm 1 阈值来源** — RMSE reduction < 0.02 和 |ΔSF_c| < 0.02 的阈值确实未说明来源（Appendix C, p.30）。

**[AGREE] R1-M4: Table 1 "Cond." 列** — 与我的小问题#3 一致。

**[PARTIALLY AGREE] R1-M5: Remark 1 定位** — 与我的 W1 一致，但我对此问题的严重性评估更高（should-fix vs minor）。

---

### Missing References 回应

**[AGREE]** R1 建议的三个引用都有参考价值：
- Stefanski & Carroll (1985) 对 logistic regression measurement error 直接相关（回应 R1-N3）
- Oster (2019) 的 coefficient stability 方法与 ASV 有可比性
- Tan et al. (2024) LLM annotation survey 补充 related work 覆盖度

我在初审中建议的 Jurek et al. (2005) 和 Valeri & VanderWeele (2014) 也应补充。

---

### 综合评估

R1 和我在以下方面达成一致：
1. K≥3 理论缺口是主要弱点（R1-N1 / 我的 W2）
2. Correction guidance 深度不足（R1-N2 的 pipeline / 我的 N2 的 depth）
3. Abstract 格式违规（R1-M1 / 我的 N1）
4. 论文在 EMNLP 受众可达性方面有改进空间

主要分歧在于**严重性评估**：
- R1 将端到端验证缺失和线性 SEM 限制列为 must-fix，我认为 should-fix 更合适——本文定位为 theoretical contribution，MC 验证是此类工作的标准验证方式
- 但我承认 R1 的 N2 与我的 N2 联合来看确实构成一个较强的 concern：如果 correction guidance 既缺深度（我的 N2）又缺端到端验证（R1-N2），那么作为"三大贡献之一"的 claim 确实站不住

**修正后的总体评估：维持 3.5 (Borderline Conference)，但对 Soundness 从 4 微降至 3.5**，主要因为 collider sign preservation 的理论缺口（R1-W4，我初审遗漏）和 Conjecture 1 的严重性重新评估。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1396 · 2026-05-23T13:57:31.050309+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "causal_annot_error_attrib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "causal_annot_error_attrib"
  }
}
```

</details>

---


### Tool result

_source line 1397 · 2026-05-23T13:57:31.201374+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-23T13:41:43.708274+00:00\", \"completed_at\": \"2026-05-23T13:41:47.266083+00:00\", \"findings\": [{\"severity\": \"info\", \"dimension\": \"agent_error\", \"message\": \"[ERROR] Agent exited 1: You've hit your limit · resets 4pm (UTC)\"}], \"counts\": {\"critical\": 0, \"warning\": 0, \"info\": 1}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 1398 · 2026-05-23T13:57:31.201920+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "causal_annot_error_attrib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "causal_annot_error_attrib"
  }
}
```

</details>

---


### Tool result

_source line 1399 · 2026-05-23T13:57:31.252797+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1400 · 2026-05-23T14:03:00.557270+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "causal_annot_error_attrib",
  "issues_yaml": "issues:\n  # === Round 1-7 历史 (resolved，保留摘要) ===\n\n  - id: R1-N1\n    category: soundness\n    severity: must-fix\n    summary: \"Theorem 1 适用范围过窄（仅 confounding+proportional effects），K≥3 证明不完整\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 7\n    resolution: \"Theorem 1 现正确限定为 K=2；K≥3 由 Observation 1 和 Conjecture 1 覆盖。\"\n    resolution_round: 7\n\n  - id: R1-N2\n    category: soundness\n    severity: should-fix\n    summary: \"3/5 安全拓扑的符号保持仅有数值验证，Abstract 用 'establish' 暗示已证明\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 3\n    resolution: \"Abstract 已准确区分 prove/verify。\"\n    resolution_round: 4\n\n  - id: R1-N3\n    category: soundness\n    severity: must-fix\n    summary: \"ASV C(δ) 定义域错误\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Section 3.3 已引入 δ_max 约束。\"\n    resolution_round: 2\n\n  - id: R2-N1\n    category: presentation\n    severity: must-fix\n    summary: \"83.4% sign reversal headline framing 过度声称\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    resolution: \"Introduction 已重写。\"\n    resolution_round: 5\n\n  - id: R2-N2\n    category: novelty\n    severity: should-fix\n    summary: \"'first systematic framework' 过度声明\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"已修复。\"\n    resolution_round: 2\n\n  - id: R2-N3\n    category: related_work\n    severity: must-fix\n    summary: \"4 篇关键相关工作未引用\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"已修复。\"\n    resolution_round: 2\n\n  - id: R1-W2\n    category: clarity\n    severity: should-fix\n    summary: \"Sign preservation 的 DGP 条件在实践中难以事前验证\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"Section 3.2 已添加 ASV 替代讨论。\"\n    resolution_round: 3\n\n  - id: R1-W3\n    category: experiments\n    severity: should-fix\n    summary: \"实证验证不完整：缺少商业 LLM\"\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 17\n    mentions:\n      - round: 7\n        reviewers: [R2]\n        note: \"Limitations 中讨论即可。\"\n      - round: 14\n        reviewers: [R1, R2]\n        note: \"R14 共识：minor。\"\n      - round: 15\n        reviewers: [R1, R2]\n        note: \"R15 共识：should-fix（低优先级），Limitations 已覆盖。\"\n      - round: 16\n        reviewers: [R1, R2]\n        note: \"R16 R1-M2 再提为 minor。\"\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"R17 R1-W3 再提（23配置代表性），R2 交叉 PARTIALLY AGREE：核心是理论框架非 LLM benchmark，diagonal 0.45-0.81 已覆盖实用区间，严重性较低。共识 should-fix（低优先级）。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R2-W2\n    category: presentation\n    severity: should-fix\n    summary: \"98 场景 zero sign reversals 与 sign reversal narrative 的 tension\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"已解决。\"\n    resolution_round: 2\n\n  - id: R2-W3\n    category: method\n    severity: should-fix\n    summary: \"ASV 对 C₀ 估计不确定性的敏感性\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"Bootstrap ASV 分析已完成。\"\n    resolution_round: 3\n\n  - id: R2-W4\n    category: scope\n    severity: should-fix\n    summary: \"线性 SEM 假设限制；Algorithm 1 缺 linear-only caveat\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    resolution: \"Section 4.5 FWL 段加 'Under linear OLS' 限定。\"\n    resolution_round: 5\n\n  - id: R1-W4\n    category: experiments\n    severity: should-fix\n    summary: \"MC MAPE 报告不充分\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"已修复。\"\n    resolution_round: 2\n\n  - id: MISC-1\n    category: presentation\n    severity: minor\n    summary: \"符号不统一（τ vs β_T）、Proposition 编号不一致\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    resolution: \"method.tex 添加 τ 在各拓扑下含义的明确说明。\"\n    resolution_round: 5\n\n  - id: NEW-1\n    category: soundness\n    severity: should-fix\n    summary: \"Non-differential misclassification 假设讨论不足\"\n    status: in_progress\n    first_raised_round: 2\n    last_seen_round: 17\n    mentions:\n      - round: 14\n        reviewers: [R1, R2]\n        note: \"R14 共识 minor。\"\n      - round: 15\n        reviewers: [R1, R2]\n        note: \"R15 共识 should-fix。\"\n      - round: 16\n        reviewers: [R1, R2]\n        note: \"R16 R1-W1 + R2-Q2 再提。\"\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"R17 R1-W2 再提：NLP文本中Y经常嵌入A的文本，LLM可能隐性依赖Y信号，stress test仅5个VAST topics且只检查uniform perturbation。R2 交叉 AGREE。共识 should-fix。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: NEW-2\n    category: related_work\n    severity: should-fix\n    summary: \"缺少 Feder et al. (2022) 和 Cheng et al. (2024)\"\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 5\n    resolution: \"已引用。\"\n    resolution_round: 5\n\n  - id: NEW-3\n    category: soundness\n    severity: should-fix\n    summary: \"Conjecture 1 数值验证规模\"\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"210,000 matrices + adversarial + analytic plim。\"\n    resolution_round: 3\n\n  - id: R3-NEW-1\n    category: format\n    severity: must-fix\n    summary: \"正文超出 EMNLP 2026 Long Paper 8 页限制\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 12\n    resolution: \"Conclusion 已压缩。编译后视觉确认 Section 5 完全在 p8 内。\"\n    resolution_round: 13\n\n  - id: R3-NEW-2\n    category: soundness\n    severity: should-fix\n    summary: \"FWL invariance 结论缺乏 precise statement 和推导\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"FWL 证明完整。\"\n    resolution_round: 5\n\n  - id: R3-NEW-3\n    category: scope\n    severity: should-fix\n    summary: \"缺少 outcome misclassification 讨论\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"Limitations 已添加。\"\n    resolution_round: 4\n\n  - id: R3-NEW-4\n    category: presentation\n    severity: should-fix\n    summary: \"Abstract/Introduction 信息过载（数字密度）\"\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 17\n    mentions:\n      - round: 14\n        reviewers: [R1, R2]\n        note: \"R14 共识 minor。\"\n      - round: 15\n        reviewers: [R2]\n        note: \"R15 should-fix（高优先级）。\"\n      - round: 16\n        reviewers: [R1, R2]\n        note: \"R16 R2-W1 再提，R1 交叉 AGREE。\"\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"R17 与 R17-N1（超字数）联合。Abstract 245 words 超出 200 限制，且试图覆盖全部七拓扑和多项数值——需精简到3-4核心信息点。两位共识 must-fix。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R3-NEW-5\n    category: related_work\n    severity: should-fix\n    summary: \"缺少 5 篇相关引用（Round 3 要求的）\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 3\n    resolution: \"全部 5 篇已引用。\"\n    resolution_round: 4\n\n  - id: R3-NEW-6\n    category: reproducibility\n    severity: should-fix\n    summary: \"未承诺代码/数据公开\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"Conclusion 已添加代码公开承诺。\"\n    resolution_round: 4\n\n  - id: R3-NEW-7\n    category: novelty\n    severity: should-fix\n    summary: \"新颖性定位不清：未明确界定已知结果 vs 新贡献\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"确认'首次跨 7 种拓扑系统比较'成立。\"\n    resolution_round: 5\n\n  - id: R3-NEW-8\n    category: experiments\n    severity: should-fix\n    summary: \"经验验证使用模拟 DGP 而非真实因果数据\"\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 17\n    mentions:\n      - round: 14\n        reviewers: []\n        note: \"R14 未单独提出。\"\n      - round: 15\n        reviewers: [R1, R2]\n        note: \"R15 should-fix。\"\n      - round: 16\n        reviewers: [R1, R2]\n        note: \"R16 R1-N2 列为 must-fix，R2 AGREE 但认为 Limitations 承认作为最低修复。\"\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"R17 R1-N2 再列为 must-fix（缺端到端 pipeline：C estimation → ASV → correction → improved estimates）。R2 交叉 PARTIALLY AGREE：本文定位为 theoretical contribution，MC 验证是标准验证方式，ground-truth causal effects 在观察性数据中几乎不可能获取。R2 建议降为 should-fix。Director 采纳 should-fix（高优先级）：理论贡献无需完整 pipeline，但建议降低 correction guidance 贡献定位或至少展示一个拓扑的路由效果。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R4-W3\n    category: soundness\n    severity: should-fix\n    summary: \"Eq.(3) 中 λ(C) ∈ [0,1] 未证明\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 4\n    resolution: \"Eq.(3) 标注 'under proportional effects' + Appendix Proposition 4 证明。\"\n    resolution_round: 5\n\n  - id: R4-W4\n    category: presentation\n    severity: should-fix\n    summary: \"'Empirical Finding 1' 术语误导——应建立 Proved/Verified/Conjectured 三级层次\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    resolution: \"论文已建立三级层次。\"\n    resolution_round: 5\n\n  - id: R4-W6\n    category: novelty\n    severity: should-fix\n    summary: \"ASV 方法论创新有限——E-value 直接移植质疑\"\n    status: in_progress\n    first_raised_round: 4\n    last_seen_round: 17\n    mentions:\n      - round: 14\n        reviewers: [R1, R2]\n        note: \"R14 共识 should-fix。\"\n      - round: 15\n        reviewers: [R2]\n        note: \"R15 Remark 1 三点对比不够充分。\"\n      - round: 16\n        reviewers: [R1, R2]\n        note: \"R16 R2-N1 列为 must-fix，R1 交叉 REBUT 降为 should-fix。\"\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"R17 R2-W1 再提：核心操作（沿 C(δ) 计算 tipping point）是标准 sensitivity analysis 方法，论文未展示 ASV 能得出 E-value 无法得出的定性结论。R1 交叉 AGREE 但补充拓扑分层能力是 E-value 框架无法自然实现的实质贡献，建议增加 worked example。共识 should-fix。\"\n    action_items:\n      - round: 14\n        action: \"正文增加 Remark 形式化说明 ASV 与 E-value 的数学结构区别\"\n        assigned_to: agent\n        status: done\n      - round: 16\n        action: \"Remark 1 增加技术挑战来源说明\"\n        assigned_to: agent\n        status: in_progress\n      - round: 17\n        action: \"增加 worked example 展示 ASV 拓扑分层能力（同一 C 在不同 DAG 下产生不同 ASV）\"\n        assigned_to: agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R4-W7\n    category: presentation\n    severity: should-fix\n    summary: \"论文广度有余深度不足\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 7\n    resolution: \"Appendix pointer 已添加，R8 未再提及。\"\n    resolution_round: 8\n\n  - id: R4-W8\n    category: scope\n    severity: should-fix\n    summary: \"DAG 拓扑必须先验已知——Algorithm 1 依赖正确拓扑输入\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    resolution: \"Limitations 已添加相关讨论。\"\n    resolution_round: 5\n\n  - id: R4-W10\n    category: method\n    severity: minor\n    summary: \"PPI++ 对 M-bias 有害 (-88%) 缺乏机制解释\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 15\n    resolution: \"Section 4.5 已包含完整机制解释。连续两轮未被提出。\"\n    resolution_round: 15\n\n  - id: R4-W12\n    category: presentation\n    severity: minor\n    summary: \"引用格式问题\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 7\n    resolution: \"格式合规检查通过。\"\n    resolution_round: 8\n\n  - id: R5-N1\n    category: presentation\n    severity: must-fix\n    summary: \"Table 1 的 sign-flip guarantee ✓ 掩盖了 DGP 条件性\"\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"Table 1 已实现三级符号 ✓/✓*/✗。\"\n    resolution_round: 5\n\n  - id: R5-N2\n    category: soundness\n    severity: should-fix\n    summary: \"Conjecture 1 的 ε 在极端条件下可达 0.14-0.15\"\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"Conjecture 1 rewritten with per-topology ε bounds。\"\n    resolution_round: 5\n\n  - id: R5-N3\n    category: presentation\n    severity: must-fix\n    summary: \"'Primary coefficient never reverses' 仅为经验发现，缺乏理论保证\"\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 11\n    resolution: \"Abstract 已改为经验事实描述。\"\n    resolution_round: 11\n\n  - id: R5-MR\n    category: related_work\n    severity: should-fix\n    summary: \"Round 5 新发现的缺失引用\"\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"三篇引用已添加。\"\n    resolution_round: 5\n\n  - id: R6-M1\n    category: soundness\n    severity: should-fix\n    summary: \"Theorem 1 对 K≥3 未证明但标记为 Theorem\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: \"Theorem 1 现正确限定为 K=2。\"\n    resolution_round: 7\n\n  - id: R6-M2\n    category: presentation\n    severity: should-fix\n    summary: \"Abstract 将 'primary coefficient never reverses' 称为 'structural property'\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 11\n    resolution: \"与 R5-N3 合并修复。\"\n    resolution_round: 11\n\n  - id: R6-M3\n    category: soundness\n    severity: should-fix\n    summary: \"Proportional effects 假设 (f=λg) 在 NLP 中是强限制\"\n    status: in_progress\n    first_raised_round: 6\n    last_seen_round: 17\n    mentions:\n      - round: 14\n        reviewers: [R1, R2]\n        note: \"R14 降为 should-fix。\"\n      - round: 15\n        reviewers: [R1, R2]\n        note: \"R15 should-fix（minor-to-should-fix）。\"\n      - round: 16\n        reviewers: [R1, R2]\n        note: \"R16 R1-W2 再提。\"\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"R17 R1-W1 再提：f=λg 在实践中不可直接验证，论文未讨论 NLP 场景合理性、研究者判断方法、general case 退化行为。R2 交叉 AGREE。共识 should-fix。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R6-M4\n    category: presentation\n    severity: must-fix\n    summary: \"Abstract sign reversal rate 与 Section 4.2 数值不一致\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: \"Abstract 和 Section 4.2 现均使用 2.1%。\"\n    resolution_round: 7\n\n  - id: R6-W1\n    category: scope\n    severity: should-fix\n    summary: \"线性模型假设与 NLP 实践的 scope mismatch\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: \"EXP-2 FWL N-scaling 完成。R8 未再提及。\"\n    resolution_round: 9\n\n  - id: R6-W2\n    category: novelty\n    severity: should-fix\n    summary: \"ASV 与 E-value 的方法论创新边界不清晰\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 15\n    resolution: \"与 R4-W6 合并。Remark 1 + Table 18 已添加。\"\n    resolution_round: 15\n\n  - id: R6-W3\n    category: related_work\n    severity: minor\n    summary: \"缺失引用\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: \"全部已引用。\"\n    resolution_round: 7\n\n  - id: R6-W4\n    category: soundness\n    severity: minor\n    summary: \"Conjecture 1 与 Theorem 1 覆盖范围关系\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 11\n    resolution: \"三级证据层次被赞为方法论美德。\"\n    resolution_round: 11\n\n  - id: R6-W5\n    category: experiments\n    severity: should-fix\n    summary: \"Non-differential stress test 覆盖不足\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: \"Stress test 已覆盖 ε up to 0.50。\"\n    resolution_round: 8\n\n  - id: R6-D1\n    category: presentation\n    severity: minor\n    summary: \"Table 1 'Amplif.' 列含义\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 11\n    resolution: \"Table 1 caption 已添加脚注解释。\"\n    resolution_round: 11\n\n  - id: R6-D2\n    category: method\n    severity: minor\n    summary: \"Algorithm 1 未显式排除 PPI++ 对 M-bias\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 11\n    resolution: \"Section 4.5 已明确讨论。\"\n    resolution_round: 11\n\n  - id: R7-SF1\n    category: soundness\n    severity: should-fix\n    summary: \"Proposition 2 命名不匹配\"\n    status: resolved\n    first_raised_round: 7\n    last_seen_round: 7\n    resolution: \"已改为 Observation 1。\"\n    resolution_round: 8\n\n  - id: R7-SF5\n    category: method\n    severity: should-fix\n    summary: \"ASV 对 C₀ 敏感性 / 均匀退化假设\"\n    status: in_progress\n    first_raised_round: 7\n    last_seen_round: 16\n    mentions:\n      - round: 15\n        reviewers: [R1]\n        note: \"R15 should-fix（低优先级）。\"\n      - round: 16\n        reviewers: [R1, R2]\n        note: \"R16 R1-W3 再提。\"\n      - round: 17\n        reviewers: []\n        note: \"R17 未单独提出。\"\n\n  - id: R7-SF6\n    category: presentation\n    severity: should-fix\n    summary: \"Section 4.2 sign reversal 呈现顺序\"\n    status: resolved\n    first_raised_round: 7\n    last_seen_round: 7\n    resolution: \"已重排。\"\n    resolution_round: 8\n\n  - id: R7-SF8\n    category: presentation\n    severity: minor\n    summary: \"154× 来源不透明\"\n    status: resolved\n    first_raised_round: 7\n    last_seen_round: 7\n    resolution: \"脚注已添加。\"\n    resolution_round: 8\n\n  - id: R7-MR1\n    category: related_work\n    severity: minor\n    summary: \"缺失引用\"\n    status: resolved\n    first_raised_round: 7\n    last_seen_round: 7\n    resolution: \"已处理。\"\n    resolution_round: 8\n\n  - id: R7-Q7\n    category: method\n    severity: minor\n    summary: \"Algorithm 1 risk threshold 选择依据\"\n    status: resolved\n    first_raised_round: 7\n    last_seen_round: 11\n    resolution: \"Algorithm 1 整体被赞为可操作。\"\n    resolution_round: 11\n\n  # === Round 8+ ===\n\n  - id: R8-C1\n    category: soundness\n    severity: must-fix\n    summary: \"K≥3 ASV 理论基础为 conjectural——Theorem 1 仅 K=2，Conjecture 1 缺理论证明\"\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 17\n    mentions:\n      - round: 14\n        reviewers: [R1, R2]\n        note: \"R14 共识 should-fix。\"\n      - round: 15\n        reviewers: [R1, R2]\n        note: \"R15 两位均列为 critical。\"\n      - round: 16\n        reviewers: [R1, R2]\n        note: \"R16 R1-N1 列为 critical。R2 交叉 AGREE。\"\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"R17 R1-N1 再列为 critical：(1) Table 10 显示 60-97% 矩阵违反严格单调性（magnitude ≤0.013）；(2) K=7 42维空间中10,000采样覆盖率极低；(3) 仅在 default DGP 参数下验证。R2 交叉 AGREE 但认为 worst-case 0.013 对 ASV decision boundary 影响极小，建议 borderline must-fix / strong should-fix。Director 采纳 must-fix：论文标题聚焦 Multi-Class 但 K≥3 核心结论仅为 conjecture，这是最大理论缺口。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R8-C2\n    category: soundness\n    severity: should-fix\n    summary: \"Proportional effects 在 NLP 中不可验证\"\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 17\n    mentions:\n      - round: 15\n        reviewers: [R1, R2]\n        note: \"R15 共识 should-fix。\"\n      - round: 16\n        reviewers: [R1, R2]\n        note: \"R16 与 R6-M3 合并。\"\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"R17 与 R6-M3 合并。\"\n\n  - id: R8-W1\n    category: novelty\n    severity: should-fix\n    summary: \"ASV contribution 定位\"\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 17\n    mentions:\n      - round: 15\n        reviewers: [R2]\n        note: \"R15 与 R4-W6 合并。\"\n      - round: 16\n        reviewers: [R1, R2]\n        note: \"R16 与 R4-W6 合并。\"\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"R17 与 R4-W6 合并。\"\n\n  - id: R8-W2\n    category: soundness\n    severity: should-fix\n    summary: \"Non-differential 假设讨论不足\"\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 17\n    mentions:\n      - round: 15\n        reviewers: [R1, R2]\n        note: \"R15 合并到 NEW-1。\"\n      - round: 16\n        reviewers: [R1, R2]\n        note: \"R16 合并到 NEW-1。\"\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"R17 合并到 NEW-1。\"\n\n  - id: R8-W3\n    category: method\n    severity: minor\n    summary: \"δ* uncertainty bound 过宽\"\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 17\n    mentions:\n      - round: 16\n        reviewers: []\n        note: \"R16 未单独提出。连续三轮未被 Reviewer 提出。\"\n      - round: 17\n        reviewers: []\n        note: \"R17 未提出。连续四轮未提出，考虑降级或关闭。\"\n\n  - id: R8-MR1\n    category: related_work\n    severity: minor\n    summary: \"缺失 Ding & VanderWeele (2016)\"\n    status: resolved\n    first_raised_round: 8\n    last_seen_round: 11\n    resolution: \"已引用。\"\n    resolution_round: 11\n\n  # === Round 9 ===\n\n  - id: R9-C1\n    category: soundness\n    severity: should-fix\n    summary: \"核心假设（non-differential + proportional effects）在 LLM 场景缺乏实证验证\"\n    status: in_progress\n    first_raised_round: 9\n    last_seen_round: 17\n    mentions:\n      - round: 15\n        reviewers: [R1, R2]\n        note: \"R15 合并到 R6-M3 和 NEW-1。\"\n      - round: 16\n        reviewers: [R1, R2]\n        note: \"R16 合并到 R6-M3 和 NEW-1。\"\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"R17 合并到 R6-M3 和 NEW-1。\"\n\n  - id: R9-C2\n    category: scope\n    severity: should-fix\n    summary: \"线性 SEM 假设对 EMNLP 读者可达性和泛化性不足\"\n    status: in_progress\n    first_raised_round: 9\n    last_seen_round: 17\n    mentions:\n      - round: 15\n        reviewers: [R1, R2]\n        note: \"R15 should-fix。\"\n      - round: 16\n        reviewers: [R1]\n        note: \"R16 R1-M1 降为 minor。\"\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"R17 R1-N3 升回 must-fix：NLP 最常用 logistic regression，bias 表达式在非线性模型下有效性未检验。R2 交叉 PARTIALLY AGREE 降为 should-fix：Appendix B.2/B.7 已有 logistic 验证但分散在附录，主文未提及。Director 采纳 should-fix：已有验证材料，问题在 presentation 而非 absence。\"\n    action_items:\n      - round: 17\n        action: \"Section 4 增加 3-4 句总结 logistic regression 验证结果，引用 Appendix B.2 和 B.7\"\n        assigned_to: agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R9-M1\n    category: soundness\n    severity: should-fix\n    summary: \"K≥3 理论不完整——要求讨论证明技术障碍\"\n    status: in_progress\n    first_raised_round: 9\n    last_seen_round: 17\n    mentions:\n      - round: 15\n        reviewers: [R1, R2]\n        note: \"R15 合并到 R8-C1。\"\n      - round: 16\n        reviewers: [R1, R2]\n        note: \"R16 合并到 R8-C1。\"\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"R17 合并到 R8-C1。\"\n\n  - id: R9-S1\n    category: novelty\n    severity: should-fix\n    summary: \"'first to characterize' novelty claim 需限定\"\n    status: in_progress\n    first_raised_round: 9\n    last_seen_round: 17\n    mentions:\n      - round: 12\n        reviewers: [R1]\n        note: \"R1 REBUT 成功。\"\n      - round: 16\n        reviewers: [R1, R2]\n        note: \"R16 R2-N2 再提为 must-fix。Director 采纳 should-fix。\"\n      - round: 17\n        reviewers: [R2]\n        note: \"R17 R2 新颖性评估确认 'first unified analysis' 在当前文献范围内成立，但 'unified' 主要指系统覆盖而非统一理论。R1 未单独提出。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R9-S2\n    category: presentation\n    severity: should-fix\n    summary: \"Abstract 2.1% 聚合数字掩盖拓扑差异\"\n    status: resolved\n    first_raised_round: 9\n    last_seen_round: 11\n    resolution: \"Abstract 已 topology-specific。\"\n    resolution_round: 11\n\n  - id: R9-S3\n    category: experiments\n    severity: should-fix\n    summary: \"LLM 配置多样性有限（缺 <7B, >70B, ordinal）\"\n    status: in_progress\n    first_raised_round: 9\n    last_seen_round: 17\n    mentions:\n      - round: 15\n        reviewers: [R1, R2]\n        note: \"R15 合并到 R1-W3。\"\n      - round: 16\n        reviewers: [R1]\n        note: \"R16 合并到 R1-W3。\"\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"R17 合并到 R1-W3。\"\n\n  - id: R9-M2\n    category: method\n    severity: should-fix\n    summary: \"ASV 可操作性展示不足——Algorithm 1 与主文脱节\"\n    status: resolved\n    first_raised_round: 9\n    last_seen_round: 11\n    resolution: \"Algorithm 1 被赞为可操作。\"\n    resolution_round: 11\n\n  # === Round 11 ===\n\n  - id: R11-W1\n    category: presentation\n    severity: should-fix\n    summary: \"ClinicalBERT case study 应在正文提及\"\n    status: resolved\n    first_raised_round: 11\n    last_seen_round: 15\n    resolution: \"Section 4.5 已引用 ClinicalBERT。连续三轮未被提出。\"\n    resolution_round: 15\n\n  - id: R11-W2\n    category: presentation\n    severity: should-fix\n    summary: \"Section 3.1 缺少 Notation roadmap——plim/FWL 对 NLP 读者不友好\"\n    status: in_progress\n    first_raised_round: 11\n    last_seen_round: 17\n    mentions:\n      - round: 15\n        reviewers: [R1, R2]\n        note: \"R15 should-fix（高优先级）。\"\n      - round: 16\n        reviewers: [R1, R2]\n        note: \"R16 R2-W2 再提。R1 交叉 AGREE。\"\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"R17 R2-W3 + R1-N3 联合再提。plim/FWL/Wald/column-stochastic/Birkhoff polytope/Dirichlet prior 对 NLP 读者壁垒过高。R1 建议首次出现时添加 parenthetical 直觉解释。R2 建议增加 Intuition 段落。两位共识 should-fix（高优先级）。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R11-W3\n    category: experiments\n    severity: should-fix\n    summary: \"校正方法比较固定 K=3，未验证 K 值敏感性\"\n    status: resolved\n    first_raised_round: 11\n    last_seen_round: 12\n    resolution: \"K=3/5/10 × 7 topologies 完成。Spearman ρ=0.80-0.93。\"\n    resolution_round: 13\n\n  - id: R11-W4\n    category: presentation\n    severity: minor\n    summary: \"IV 52.6% denominator sign change 的 NLP 实践含义未讨论\"\n    status: in_progress\n    first_raised_round: 11\n    last_seen_round: 17\n    mentions:\n      - round: 15\n        reviewers: []\n        note: \"Section 4.2 已添加替代方案。\"\n      - round: 16\n        reviewers: []\n        note: \"R16 未单独提出。\"\n      - round: 17\n        reviewers: []\n        note: \"R17 未单独提出。\"\n\n  - id: R11-MI\n    category: presentation\n    severity: minor\n    summary: \"R1 识别的 minor issues\"\n    status: in_progress\n    first_raised_round: 11\n    last_seen_round: 17\n    mentions:\n      - round: 16\n        reviewers: []\n        note: \"R16 未单独提出。\"\n      - round: 17\n        reviewers: []\n        note: \"R17 未单独提出。\"\n\n  - id: R11-MR1\n    category: related_work\n    severity: should-fix\n    summary: \"缺失引用（R11 新发现）\"\n    status: resolved\n    first_raised_round: 11\n    last_seen_round: 12\n    resolution: \"已添加。\"\n    resolution_round: 13\n\n  # === Round 12 ===\n\n  - id: R12-F1\n    category: format\n    severity: must-fix\n    summary: \"正文溢出至 p9\"\n    status: resolved\n    first_raised_round: 12\n    last_seen_round: 12\n    resolution: \"已压缩。\"\n    resolution_round: 13\n\n  - id: R12-W1\n    category: presentation\n    severity: should-fix\n    summary: \"计量经济学术语对 EMNLP 受众可及性不足\"\n    status: in_progress\n    first_raised_round: 12\n    last_seen_round: 17\n    mentions:\n      - round: 15\n        reviewers: [R1, R2]\n        note: \"R15 与 R11-W2 合并。\"\n      - round: 16\n        reviewers: [R1, R2]\n        note: \"R16 与 R11-W2 合并。\"\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"R17 与 R11-W2 合并。\"\n\n  - id: R12-MR1\n    category: related_work\n    severity: should-fix\n    summary: \"R12 缺失引用\"\n    status: resolved\n    first_raised_round: 12\n    last_seen_round: 12\n    resolution: \"已添加。\"\n    resolution_round: 13\n\n  - id: R12-MI1\n    category: presentation\n    severity: should-fix\n    summary: \"Algorithm 1 阈值硬编码自 K=3 结果\"\n    status: in_progress\n    first_raised_round: 12\n    last_seen_round: 17\n    mentions:\n      - round: 15\n        reviewers: [R1, R2]\n        note: \"R15 should-fix。\"\n      - round: 16\n        reviewers: []\n        note: \"R16 未单独提出。\"\n      - round: 17\n        reviewers: [R1]\n        note: \"R17 R1-M3 再提：Algorithm 1 Step 2 RMSE red. < 0.02 阈值来源未说明。\"\n\n  - id: R12-MI2\n    category: presentation\n    severity: should-fix\n    summary: \"Figure 2 视觉问题\"\n    status: in_progress\n    first_raised_round: 12\n    last_seen_round: 17\n    mentions:\n      - round: 15\n        reviewers: [R1, R2]\n        note: \"R15 minor。\"\n      - round: 16\n        reviewers: [R1, R2]\n        note: \"R16 R2-W4 再提。共识 should-fix。\"\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"R17 两位均再提：灰度打印下 red=sign reversal 难区分，建议使用 hatching pattern。共识 minor。\"\n\n  # === Round 13 ===\n\n  - id: R13-W1\n    category: soundness\n    severity: must-fix\n    summary: \"IV sign reversal 表述在 Abstract/Section 4.2/Appendix B.4 之间 factual 不一致\"\n    status: resolved\n    first_raised_round: 13\n    last_seen_round: 13\n    resolution: \"三处统一。\"\n    resolution_round: 14\n\n  - id: R13-W2\n    category: presentation\n    severity: minor\n    summary: \"部分拓扑缺少 NLP 应用场景示例\"\n    status: resolved\n    first_raised_round: 13\n    last_seen_round: 15\n    resolution: \"已添加。连续两轮未被提出。\"\n    resolution_round: 15\n\n  - id: R13-MR1\n    category: related_work\n    severity: minor\n    summary: \"R13 缺失引用\"\n    status: resolved\n    first_raised_round: 13\n    last_seen_round: 15\n    resolution: \"已在 references.bib 和 Related Work 中引用。\"\n    resolution_round: 15\n\n  - id: R13-CRIT1\n    category: soundness\n    severity: critical\n    summary: \"Limitations 中 diagonal accuracy 范围错误\"\n    status: resolved\n    first_raised_round: 13\n    last_seen_round: 13\n    resolution: \"0.45-0.81 与实际数据一致。\"\n    resolution_round: 14\n\n  # === Round 14 ===\n\n  - id: R14-W1\n    category: presentation\n    severity: minor\n    summary: \"Table 1 Yes/Yes*/No 标注不直观\"\n    status: resolved\n    first_raised_round: 14\n    last_seen_round: 14\n    resolution: \"已改为 Cond./Yes/No。\"\n    resolution_round: 15\n\n  - id: R14-W2\n    category: method\n    severity: should-fix\n    summary: \"IV 拓扑 maximally fragile 后缺少积极替代方案\"\n    status: resolved\n    first_raised_round: 14\n    last_seen_round: 15\n    resolution: \"Section 4.2 已添加三种替代方案。\"\n    resolution_round: 15\n\n  - id: R14-W3\n    category: presentation\n    severity: should-fix\n    summary: \"混淆矩阵 C 的可获得性假设\"\n    status: resolved\n    first_raised_round: 14\n    last_seen_round: 15\n    resolution: \"Limitations 已覆盖。\"\n    resolution_round: 15\n\n  # === Round 15 ===\n\n  - id: R15-N1\n    category: soundness\n    severity: must-fix\n    summary: \"Observation 1 声称 worst-case < 0.005 与 Table 10 不一致（confounding 0.011, front-door 0.013）\"\n    status: in_progress\n    first_raised_round: 15\n    last_seen_round: 17\n    mentions:\n      - round: 15\n        reviewers: [R1, R2]\n        note: \"需修正 Observation 1 数值。\"\n      - round: 16\n        reviewers: []\n        note: \"R16 未单独提出。\"\n      - round: 17\n        reviewers: []\n        note: \"R17 未单独提出。连续两轮未提出。\"\n    action_items:\n      - round: 15\n        action: \"修正 Observation 1 数值\"\n        assigned_to: agent\n        status: in_progress\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R15-W1\n    category: presentation\n    severity: should-fix\n    summary: \"Table 1 Violation vs Sign Flip 列定义模糊\"\n    status: in_progress\n    first_raised_round: 15\n    last_seen_round: 17\n    mentions:\n      - round: 15\n        reviewers: [R1, R2]\n        note: \"需在 caption 中精确定义。\"\n      - round: 16\n        reviewers: [R1, R2]\n        note: \"R16 R2-M1 + R1 交叉 AGREE。\"\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"R17 R2 小问题#3 + R1-M4 再提。应明确 Sign Flip 列指什么（任何系数 vs 主效应），增加脚注定义。两位共识。\"\n    action_items:\n      - round: 15\n        action: \"Table 1 caption 增加列定义\"\n        assigned_to: agent\n        status: in_progress\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R15-W2\n    category: presentation\n    severity: should-fix\n    summary: \"Abstract FWL invariance 声明缺少 'under linear OLS' 限定词\"\n    status: in_progress\n    first_raised_round: 15\n    last_seen_round: 17\n    mentions:\n      - round: 15\n        reviewers: [R1, R2]\n        note: \"修复成本极低。\"\n      - round: 16\n        reviewers: []\n        note: \"R16 未单独提出。\"\n      - round: 17\n        reviewers: []\n        note: \"R17 未单独提出。但 R1-N3 关于线性 SEM 讨论不足间接覆盖。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R15-W3\n    category: method\n    severity: should-fix\n    summary: \"Algorithm 1 经验阈值缺乏理论依据和 DGP 敏感性讨论\"\n    status: in_progress\n    first_raised_round: 15\n    last_seen_round: 17\n    mentions:\n      - round: 15\n        reviewers: [R1, R2]\n        note: \"should-fix。\"\n      - round: 16\n        reviewers: []\n        note: \"R16 未单独提出。\"\n      - round: 17\n        reviewers: [R1]\n        note: \"R17 R1-M3 再提。\"\n\n  # === Round 16 ===\n\n  - id: R16-N1\n    category: presentation\n    severity: should-fix\n    summary: \"2.1% sign reversal 限定不清晰——secondary coefficient 还是 primary coefficient？\"\n    status: in_progress\n    first_raised_round: 16\n    last_seen_round: 17\n    mentions:\n      - round: 16\n        reviewers: [R1, R2]\n        note: \"R16 共识。\"\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"R17 R2-W4 + R1-Q5 再提。Abstract 'sign reversal of secondary coefficients' 首次出现时未定义。'Primary coefficient never reverses' 未出现在 abstract。R1 建议改用 'non-treatment coefficients'。两位共识 should-fix。\"\n    action_items:\n      - round: 16\n        action: \"Abstract 改为 'secondary-coefficient sign reversal'；Table 1 增加脚注\"\n        assigned_to: agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R16-N2\n    category: presentation\n    severity: should-fix\n    summary: \"Correction guidance 深度不足——作为三大贡献之一，Section 4.5 仅半页\"\n    status: in_progress\n    first_raised_round: 16\n    last_seen_round: 17\n    mentions:\n      - round: 16\n        reviewers: [R1, R2]\n        note: \"R16 提出。\"\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"R17 R2-N2 列为 must-fix（Algorithm 1 仅在附录 p.30，五种方法选择标准未在主文讨论）。R1 交叉 REBUT 降为 should-fix：实质内容存在（Table 4 完整对比），修复路径轻量（移入 Algorithm 1 + 方法讨论），contribution framing 对 acceptance 影响有限。Director 采纳 should-fix（高优先级）：同意 R1 判断——内容存在，问题在 presentation。但与端到端验证缺失联合看确实削弱第三贡献的说服力。\"\n    action_items:\n      - round: 16\n        action: \"Section 4.5 扩充\"\n        assigned_to: agent\n        status: open\n      - round: 17\n        action: \"选择路径 (a) 将 Algorithm 1 移入正文 + 增加方法选择讨论，或 (b) 降低 correction guidance 贡献定位为 '附带讨论'\"\n        assigned_to: agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R16-N3\n    category: scope\n    severity: should-fix\n    summary: \"FWL invariance 在 logistic regression 下失效的含义未在主文讨论\"\n    status: in_progress\n    first_raised_round: 16\n    last_seen_round: 17\n    mentions:\n      - round: 16\n        reviewers: [R1, R2]\n        note: \"R16 R2-Q3 提出。\"\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"R17 R1-N3 联合覆盖。R2 交叉回应指出 Appendix B.2 已有 logistic 验证但主文未提及。与 R9-C2 合并处理。\"\n\n  - id: R16-N4\n    category: novelty\n    severity: should-fix\n    summary: \"'First unified analysis' claim 需与 Carroll et al. (2006) 和 Schennach (2020) 显式区分\"\n    status: in_progress\n    first_raised_round: 16\n    last_seen_round: 17\n    mentions:\n      - round: 16\n        reviewers: [R1, R2]\n        note: \"R16 R2-N2 提出。Director 采纳 should-fix。\"\n      - round: 17\n        reviewers: [R2]\n        note: \"R17 R2 新颖性评估确认 'first' 声明在当前文献范围内成立，但需注意 'unified' 主要指系统覆盖。R1 未单独提出。\"\n\n  - id: R16-N5\n    category: presentation\n    severity: minor\n    summary: \"Notation table (Table 19) 放在 Appendix C，主文符号引导分散\"\n    status: in_progress\n    first_raised_round: 16\n    last_seen_round: 17\n    mentions:\n      - round: 16\n        reviewers: [R1, R2]\n        note: \"R16 提出。\"\n      - round: 17\n        reviewers: []\n        note: \"R17 未单独提出。与 R11-W2 术语可达性问题合并。\"\n\n  - id: R16-N6\n    category: presentation\n    severity: minor\n    summary: \"τ vs β_T 含义在 mediator/front-door 拓扑下不清晰\"\n    status: in_progress\n    first_raised_round: 16\n    last_seen_round: 17\n    mentions:\n      - round: 16\n        reviewers: [R1]\n        note: \"R16 R1-M4 提出。\"\n      - round: 17\n        reviewers: []\n        note: \"R17 未单独提出。\"\n\n  - id: R16-MR1\n    category: related_work\n    severity: should-fix\n    summary: \"缺失引用：Miles et al. (2024), Wei et al. (2025), Hernán & Robins (2020), Schennach (2020)\"\n    status: in_progress\n    first_raised_round: 16\n    last_seen_round: 17\n    mentions:\n      - round: 16\n        reviewers: [R1, R2]\n        note: \"R16 提出。\"\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"R17 检查：bib 中已有 miles2024measurement, wei2025multiply, hernan2020causal, schennach2020mismeasured，正文 Related Work 已引用 schennach2020mismeasured, miles2024measurement, wei2025multiply。hernan2020causal 仅在 Section 3.1 引用。本轮未单独重提。\"\n\n  # === Round 17 新发现 ===\n\n  - id: R17-N1\n    category: format\n    severity: must-fix\n    summary: \"Abstract 超过 EMNLP 2026 的 200 words 限制（实际约 245 words）\"\n    status: open\n    first_raised_round: 17\n    last_seen_round: 17\n    mentions:\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"R2-N1 首提为 critical：逐字统计 245 words，超出 22.5%，desk reject 风险。R1 初审仅列为 minor (M1)，交叉审阅后升级为 must-fix。两位共识 must-fix。\"\n    action_items:\n      - round: 17\n        action: \"Abstract 精简至 ≤200 words：聚焦 3-4 核心信息点（K≥3 sign reversal, ASV ranking, FWL invariance），删除具体数值和次要拓扑逐一列举\"\n        assigned_to: agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R17-W1\n    category: soundness\n    severity: should-fix\n    summary: \"Collider sign preservation 仅有经验验证，削弱 Proposition 1 统一框架严谨性\"\n    status: open\n    first_raised_round: 17\n    last_seen_round: 17\n    mentions:\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"R1-W4 首提：Table 2 中 collider 标记为 Empirical（Cauchy-Schwarz/Berkson attenuation），而 confounding 有代数证明。Appendix A.6 Proposition 5 仅证明 proportional case，general case（Proposition 6）只给出 magnitude bound，sign preservation 依赖 100,000 矩阵验证。R2 交叉 AGREE：初审遗漏此缺口。建议在 Proposition 1 明确区分 proved vs empirically verified。\"\n    action_items:\n      - round: 17\n        action: \"Proposition 1 或 Table 2 中明确标注 collider sign preservation 为 empirically verified（非 proved）\"\n        assigned_to: agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R17-W2\n    category: format\n    severity: minor\n    summary: \"Bib 含 2 条未引用条目（dawid1979, rosenbaum2002）\"\n    status: open\n    first_raised_round: 17\n    last_seen_round: 17\n    mentions:\n      - round: 17\n        reviewers: [R2]\n        note: \"R2-W5 提出，R1 交叉 AGREE（承认初审遗漏 bib 清洁度检查）。\"\n    action_items:\n      - round: 17\n        action: \"引用或移除 dawid1979 和 rosenbaum2002\"\n        assigned_to: agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R17-MR1\n    category: related_work\n    severity: minor\n    summary: \"R17 建议补充引用\"\n    status: open\n    first_raised_round: 17\n    last_seen_round: 17\n    mentions:\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"R1 建议：Stefanski & Carroll (1985) logistic measurement error, Oster (2019) coefficient stability, Tan et al. (2024) LLM annotation survey。R2 建议：Jurek et al. (2005) beyond toward-null, Valeri & VanderWeele (2014) mediation measurement error。R2 交叉 AGREE R1 建议。\"\n    resolution: \"\"\n    resolution_round: null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "causal_annot_error_attrib",
    "issues_yaml": "issues:\n  # === Round 1-7 历史 (resolved，保留摘要) ===\n\n  - id: R1-N1\n    category: soundness\n    severity: must-fix\n    summary: \"Theorem 1 适用范围过窄（仅 confounding+proportional effects），K≥3 证明不完整\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 7\n    resolution: \"Theorem 1 现正确限定为 K=2；K≥3 由 Observation 1 和 Conjecture 1 覆盖。\"\n    resolution_round: 7\n\n  - id: R1-N2\n    category: soundness\n    severity: should-fix\n    summary: \"3/5 安全拓扑的符号保持仅有数值验证，Abstract 用 'establish' 暗示已证明\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 3\n    resolution: \"Abstract 已准确区分 prove/verify。\"\n    resolution_round: 4\n\n  - id: R1-N3\n    category: soundness\n    severity: must-fix\n    summary: \"ASV C(δ) 定义域错误\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Section 3.3 已引入 δ_max 约束。\"\n    resolution_round: 2\n\n  - id: R2-N1\n    category: presentation\n    severity: must-fix\n    summary: \"83.4% sign reversal headline framing 过度声称\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    resolution: \"Introduction 已重写。\"\n    resolution_round: 5\n\n  - id: R2-N2\n    category: novelty\n    severity: should-fix\n    summary: \"'first systematic framework' 过度声明\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"已修复。\"\n    resolution_round: 2\n\n  - id: R2-N3\n    category: related_work\n    severity: must-fix\n    summary: \"4 篇关键相关工作未引用\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"已修复。\"\n    resolution_round: 2\n\n  - id: R1-W2\n    category: clarity\n    severity: should-fix\n    summary: \"Sign preservation 的 DGP 条件在实践中难以事前验证\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"Section 3.2 已添加 ASV 替代讨论。\"\n    resolution_round: 3\n\n  - id: R1-W3\n    category: experiments\n    severity: should-fix\n    summary: \"实证验证不完整：缺少商业 LLM\"\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 17\n    mentions:\n      - round: 7\n        reviewers: [R2]\n        note: \"Limitations 中讨论即可。\"\n      - round: 14\n        reviewers: [R1, R2]\n        note: \"R14 共识：minor。\"\n      - round: 15\n        reviewers: [R1, R2]\n        note: \"R15 共识：should-fix（低优先级），Limitations 已覆盖。\"\n      - round: 16\n        reviewers: [R1, R2]\n        note: \"R16 R1-M2 再提为 minor。\"\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"R17 R1-W3 再提（23配置代表性），R2 交叉 PARTIALLY AGREE：核心是理论框架非 LLM benchmark，diagonal 0.45-0.81 已覆盖实用区间，严重性较低。共识 should-fix（低优先级）。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R2-W2\n    category: presentation\n    severity: should-fix\n    summary: \"98 场景 zero sign reversals 与 sign reversal narrative 的 tension\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"已解决。\"\n    resolution_round: 2\n\n  - id: R2-W3\n    category: method\n    severity: should-fix\n    summary: \"ASV 对 C₀ 估计不确定性的敏感性\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"Bootstrap ASV 分析已完成。\"\n    resolution_round: 3\n\n  - id: R2-W4\n    category: scope\n    severity: should-fix\n    summary: \"线性 SEM 假设限制；Algorithm 1 缺 linear-only caveat\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    resolution: \"Section 4.5 FWL 段加 'Under linear OLS' 限定。\"\n    resolution_round: 5\n\n  - id: R1-W4\n    category: experiments\n    severity: should-fix\n    summary: \"MC MAPE 报告不充分\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"已修复。\"\n    resolution_round: 2\n\n  - id: MISC-1\n    category: presentation\n    severity: minor\n    summary: \"符号不统一（τ vs β_T）、Proposition 编号不一致\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    resolution: \"method.tex 添加 τ 在各拓扑下含义的明确说明。\"\n    resolution_round: 5\n\n  - id: NEW-1\n    category: soundness\n    severity: should-fix\n    summary: \"Non-differential misclassification 假设讨论不足\"\n    status: in_progress\n    first_raised_round: 2\n    last_seen_round: 17\n    mentions:\n      - round: 14\n        reviewers: [R1, R2]\n        note: \"R14 共识 minor。\"\n      - round: 15\n        reviewers: [R1, R2]\n        note: \"R15 共识 should-fix。\"\n      - round: 16\n        reviewers: [R1, R2]\n        note: \"R16 R1-W1 + R2-Q2 再提。\"\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"R17 R1-W2 再提：NLP文本中Y经常嵌入A的文本，LLM可能隐性依赖Y信号，stress test仅5个VAST topics且只检查uniform perturbation。R2 交叉 AGREE。共识 should-fix。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: NEW-2\n    category: related_work\n    severity: should-fix\n    summary: \"缺少 Feder et al. (2022) 和 Cheng et al. (2024)\"\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 5\n    resolution: \"已引用。\"\n    resolution_round: 5\n\n  - id: NEW-3\n    category: soundness\n    severity: should-fix\n    summary: \"Conjecture 1 数值验证规模\"\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"210,000 matrices + adversarial + analytic plim。\"\n    resolution_round: 3\n\n  - id: R3-NEW-1\n    category: format\n    severity: must-fix\n    summary: \"正文超出 EMNLP 2026 Long Paper 8 页限制\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 12\n    resolution: \"Conclusion 已压缩。编译后视觉确认 Section 5 完全在 p8 内。\"\n    resolution_round: 13\n\n  - id: R3-NEW-2\n    category: soundness\n    severity: should-fix\n    summary: \"FWL invariance 结论缺乏 precise statement 和推导\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"FWL 证明完整。\"\n    resolution_round: 5\n\n  - id: R3-NEW-3\n    category: scope\n    severity: should-fix\n    summary: \"缺少 outcome misclassification 讨论\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"Limitations 已添加。\"\n    resolution_round: 4\n\n  - id: R3-NEW-4\n    category: presentation\n    severity: should-fix\n    summary: \"Abstract/Introduction 信息过载（数字密度）\"\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 17\n    mentions:\n      - round: 14\n        reviewers: [R1, R2]\n        note: \"R14 共识 minor。\"\n      - round: 15\n        reviewers: [R2]\n        note: \"R15 should-fix（高优先级）。\"\n      - round: 16\n        reviewers: [R1, R2]\n        note: \"R16 R2-W1 再提，R1 交叉 AGREE。\"\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"R17 与 R17-N1（超字数）联合。Abstract 245 words 超出 200 限制，且试图覆盖全部七拓扑和多项数值——需精简到3-4核心信息点。两位共识 must-fix。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R3-NEW-5\n    category: related_work\n    severity: should-fix\n    summary: \"缺少 5 篇相关引用（Round 3 要求的）\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 3\n    resolution: \"全部 5 篇已引用。\"\n    resolution_round: 4\n\n  - id: R3-NEW-6\n    category: reproducibility\n    severity: should-fix\n    summary: \"未承诺代码/数据公开\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"Conclusion 已添加代码公开承诺。\"\n    resolution_round: 4\n\n  - id: R3-NEW-7\n    category: novelty\n    severity: should-fix\n    summary: \"新颖性定位不清：未明确界定已知结果 vs 新贡献\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"确认'首次跨 7 种拓扑系统比较'成立。\"\n    resolution_round: 5\n\n  - id: R3-NEW-8\n    category: experiments\n    severity: should-fix\n    summary: \"经验验证使用模拟 DGP 而非真实因果数据\"\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 17\n    mentions:\n      - round: 14\n        reviewers: []\n        note: \"R14 未单独提出。\"\n      - round: 15\n        reviewers: [R1, R2]\n        note: \"R15 should-fix。\"\n      - round: 16\n        reviewers: [R1, R2]\n        note: \"R16 R1-N2 列为 must-fix，R2 AGREE 但认为 Limitations 承认作为最低修复。\"\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"R17 R1-N2 再列为 must-fix（缺端到端 pipeline：C estimation → ASV → correction → improved estimates）。R2 交叉 PARTIALLY AGREE：本文定位为 theoretical contribution，MC 验证是标准验证方式，ground-truth causal effects 在观察性数据中几乎不可能获取。R2 建议降为 should-fix。Director 采纳 should-fix（高优先级）：理论贡献无需完整 pipeline，但建议降低 correction guidance 贡献定位或至少展示一个拓扑的路由效果。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R4-W3\n    category: soundness\n    severity: should-fix\n    summary: \"Eq.(3) 中 λ(C) ∈ [0,1] 未证明\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 4\n    resolution: \"Eq.(3) 标注 'under proportional effects' + Appendix Proposition 4 证明。\"\n    resolution_round: 5\n\n  - id: R4-W4\n    category: presentation\n    severity: should-fix\n    summary: \"'Empirical Finding 1' 术语误导——应建立 Proved/Verified/Conjectured 三级层次\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    resolution: \"论文已建立三级层次。\"\n    resolution_round: 5\n\n  - id: R4-W6\n    category: novelty\n    severity: should-fix\n    summary: \"ASV 方法论创新有限——E-value 直接移植质疑\"\n    status: in_progress\n    first_raised_round: 4\n    last_seen_round: 17\n    mentions:\n      - round: 14\n        reviewers: [R1, R2]\n        note: \"R14 共识 should-fix。\"\n      - round: 15\n        reviewers: [R2]\n        note: \"R15 Remark 1 三点对比不够充分。\"\n      - round: 16\n        reviewers: [R1, R2]\n        note: \"R16 R2-N1 列为 must-fix，R1 交叉 REBUT 降为 should-fix。\"\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"R17 R2-W1 再提：核心操作（沿 C(δ) 计算 tipping point）是标准 sensitivity analysis 方法，论文未展示 ASV 能得出 E-value 无法得出的定性结论。R1 交叉 AGREE 但补充拓扑分层能力是 E-value 框架无法自然实现的实质贡献，建议增加 worked example。共识 should-fix。\"\n    action_items:\n      - round: 14\n        action: \"正文增加 Remark 形式化说明 ASV 与 E-value 的数学结构区别\"\n        assigned_to: agent\n        status: done\n      - round: 16\n        action: \"Remark 1 增加技术挑战来源说明\"\n        assigned_to: agent\n        status: in_progress\n      - round: 17\n        action: \"增加 worked example 展示 ASV 拓扑分层能力（同一 C 在不同 DAG 下产生不同 ASV）\"\n        assigned_to: agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R4-W7\n    category: presentation\n    severity: should-fix\n    summary: \"论文广度有余深度不足\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 7\n    resolution: \"Appendix pointer 已添加，R8 未再提及。\"\n    resolution_round: 8\n\n  - id: R4-W8\n    category: scope\n    severity: should-fix\n    summary: \"DAG 拓扑必须先验已知——Algorithm 1 依赖正确拓扑输入\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    resolution: \"Limitations 已添加相关讨论。\"\n    resolution_round: 5\n\n  - id: R4-W10\n    category: method\n    severity: minor\n    summary: \"PPI++ 对 M-bias 有害 (-88%) 缺乏机制解释\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 15\n    resolution: \"Section 4.5 已包含完整机制解释。连续两轮未被提出。\"\n    resolution_round: 15\n\n  - id: R4-W12\n    category: presentation\n    severity: minor\n    summary: \"引用格式问题\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 7\n    resolution: \"格式合规检查通过。\"\n    resolution_round: 8\n\n  - id: R5-N1\n    category: presentation\n    severity: must-fix\n    summary: \"Table 1 的 sign-flip guarantee ✓ 掩盖了 DGP 条件性\"\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"Table 1 已实现三级符号 ✓/✓*/✗。\"\n    resolution_round: 5\n\n  - id: R5-N2\n    category: soundness\n    severity: should-fix\n    summary: \"Conjecture 1 的 ε 在极端条件下可达 0.14-0.15\"\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"Conjecture 1 rewritten with per-topology ε bounds。\"\n    resolution_round: 5\n\n  - id: R5-N3\n    category: presentation\n    severity: must-fix\n    summary: \"'Primary coefficient never reverses' 仅为经验发现，缺乏理论保证\"\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 11\n    resolution: \"Abstract 已改为经验事实描述。\"\n    resolution_round: 11\n\n  - id: R5-MR\n    category: related_work\n    severity: should-fix\n    summary: \"Round 5 新发现的缺失引用\"\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"三篇引用已添加。\"\n    resolution_round: 5\n\n  - id: R6-M1\n    category: soundness\n    severity: should-fix\n    summary: \"Theorem 1 对 K≥3 未证明但标记为 Theorem\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: \"Theorem 1 现正确限定为 K=2。\"\n    resolution_round: 7\n\n  - id: R6-M2\n    category: presentation\n    severity: should-fix\n    summary: \"Abstract 将 'primary coefficient never reverses' 称为 'structural property'\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 11\n    resolution: \"与 R5-N3 合并修复。\"\n    resolution_round: 11\n\n  - id: R6-M3\n    category: soundness\n    severity: should-fix\n    summary: \"Proportional effects 假设 (f=λg) 在 NLP 中是强限制\"\n    status: in_progress\n    first_raised_round: 6\n    last_seen_round: 17\n    mentions:\n      - round: 14\n        reviewers: [R1, R2]\n        note: \"R14 降为 should-fix。\"\n      - round: 15\n        reviewers: [R1, R2]\n        note: \"R15 should-fix（minor-to-should-fix）。\"\n      - round: 16\n        reviewers: [R1, R2]\n        note: \"R16 R1-W2 再提。\"\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"R17 R1-W1 再提：f=λg 在实践中不可直接验证，论文未讨论 NLP 场景合理性、研究者判断方法、general case 退化行为。R2 交叉 AGREE。共识 should-fix。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R6-M4\n    category: presentation\n    severity: must-fix\n    summary: \"Abstract sign reversal rate 与 Section 4.2 数值不一致\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: \"Abstract 和 Section 4.2 现均使用 2.1%。\"\n    resolution_round: 7\n\n  - id: R6-W1\n    category: scope\n    severity: should-fix\n    summary: \"线性模型假设与 NLP 实践的 scope mismatch\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: \"EXP-2 FWL N-scaling 完成。R8 未再提及。\"\n    resolution_round: 9\n\n  - id: R6-W2\n    category: novelty\n    severity: should-fix\n    summary: \"ASV 与 E-value 的方法论创新边界不清晰\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 15\n    resolution: \"与 R4-W6 合并。Remark 1 + Table 18 已添加。\"\n    resolution_round: 15\n\n  - id: R6-W3\n    category: related_work\n    severity: minor\n    summary: \"缺失引用\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: \"全部已引用。\"\n    resolution_round: 7\n\n  - id: R6-W4\n    category: soundness\n    severity: minor\n    summary: \"Conjecture 1 与 Theorem 1 覆盖范围关系\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 11\n    resolution: \"三级证据层次被赞为方法论美德。\"\n    resolution_round: 11\n\n  - id: R6-W5\n    category: experiments\n    severity: should-fix\n    summary: \"Non-differential stress test 覆盖不足\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: \"Stress test 已覆盖 ε up to 0.50。\"\n    resolution_round: 8\n\n  - id: R6-D1\n    category: presentation\n    severity: minor\n    summary: \"Table 1 'Amplif.' 列含义\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 11\n    resolution: \"Table 1 caption 已添加脚注解释。\"\n    resolution_round: 11\n\n  - id: R6-D2\n    category: method\n    severity: minor\n    summary: \"Algorithm 1 未显式排除 PPI++ 对 M-bias\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 11\n    resolution: \"Section 4.5 已明确讨论。\"\n    resolution_round: 11\n\n  - id: R7-SF1\n    category: soundness\n    severity: should-fix\n    summary: \"Proposition 2 命名不匹配\"\n    status: resolved\n    first_raised_round: 7\n    last_seen_round: 7\n    resolution: \"已改为 Observation 1。\"\n    resolution_round: 8\n\n  - id: R7-SF5\n    category: method\n    severity: should-fix\n    summary: \"ASV 对 C₀ 敏感性 / 均匀退化假设\"\n    status: in_progress\n    first_raised_round: 7\n    last_seen_round: 16\n    mentions:\n      - round: 15\n        reviewers: [R1]\n        note: \"R15 should-fix（低优先级）。\"\n      - round: 16\n        reviewers: [R1, R2]\n        note: \"R16 R1-W3 再提。\"\n      - round: 17\n        reviewers: []\n        note: \"R17 未单独提出。\"\n\n  - id: R7-SF6\n    category: presentation\n    severity: should-fix\n    summary: \"Section 4.2 sign reversal 呈现顺序\"\n    status: resolved\n    first_raised_round: 7\n    last_seen_round: 7\n    resolution: \"已重排。\"\n    resolution_round: 8\n\n  - id: R7-SF8\n    category: presentation\n    severity: minor\n    summary: \"154× 来源不透明\"\n    status: resolved\n    first_raised_round: 7\n    last_seen_round: 7\n    resolution: \"脚注已添加。\"\n    resolution_round: 8\n\n  - id: R7-MR1\n    category: related_work\n    severity: minor\n    summary: \"缺失引用\"\n    status: resolved\n    first_raised_round: 7\n    last_seen_round: 7\n    resolution: \"已处理。\"\n    resolution_round: 8\n\n  - id: R7-Q7\n    category: method\n    severity: minor\n    summary: \"Algorithm 1 risk threshold 选择依据\"\n    status: resolved\n    first_raised_round: 7\n    last_seen_round: 11\n    resolution: \"Algorithm 1 整体被赞为可操作。\"\n    resolution_round: 11\n\n  # === Round 8+ ===\n\n  - id: R8-C1\n    category: soundness\n    severity: must-fix\n    summary: \"K≥3 ASV 理论基础为 conjectural——Theorem 1 仅 K=2，Conjecture 1 缺理论证明\"\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 17\n    mentions:\n      - round: 14\n        reviewers: [R1, R2]\n        note: \"R14 共识 should-fix。\"\n      - round: 15\n        reviewers: [R1, R2]\n        note: \"R15 两位均列为 critical。\"\n      - round: 16\n        reviewers: [R1, R2]\n        note: \"R16 R1-N1 列为 critical。R2 交叉 AGREE。\"\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"R17 R1-N1 再列为 critical：(1) Table 10 显示 60-97% 矩阵违反严格单调性（magnitude ≤0.013）；(2) K=7 42维空间中10,000采样覆盖率极低；(3) 仅在 default DGP 参数下验证。R2 交叉 AGREE 但认为 worst-case 0.013 对 ASV decision boundary 影响极小，建议 borderline must-fix / strong should-fix。Director 采纳 must-fix：论文标题聚焦 Multi-Class 但 K≥3 核心结论仅为 conjecture，这是最大理论缺口。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R8-C2\n    category: soundness\n    severity: should-fix\n    summary: \"Proportional effects 在 NLP 中不可验证\"\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 17\n    mentions:\n      - round: 15\n        reviewers: [R1, R2]\n        note: \"R15 共识 should-fix。\"\n      - round: 16\n        reviewers: [R1, R2]\n        note: \"R16 与 R6-M3 合并。\"\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"R17 与 R6-M3 合并。\"\n\n  - id: R8-W1\n    category: novelty\n    severity: should-fix\n    summary: \"ASV contribution 定位\"\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 17\n    mentions:\n      - round: 15\n        reviewers: [R2]\n        note: \"R15 与 R4-W6 合并。\"\n      - round: 16\n        reviewers: [R1, R2]\n        note: \"R16 与 R4-W6 合并。\"\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"R17 与 R4-W6 合并。\"\n\n  - id: R8-W2\n    category: soundness\n    severity: should-fix\n    summary: \"Non-differential 假设讨论不足\"\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 17\n    mentions:\n      - round: 15\n        reviewers: [R1, R2]\n        note: \"R15 合并到 NEW-1。\"\n      - round: 16\n        reviewers: [R1, R2]\n        note: \"R16 合并到 NEW-1。\"\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"R17 合并到 NEW-1。\"\n\n  - id: R8-W3\n    category: method\n    severity: minor\n    summary: \"δ* uncertainty bound 过宽\"\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 17\n    mentions:\n      - round: 16\n        reviewers: []\n        note: \"R16 未单独提出。连续三轮未被 Reviewer 提出。\"\n      - round: 17\n        reviewers: []\n        note: \"R17 未提出。连续四轮未提出，考虑降级或关闭。\"\n\n  - id: R8-MR1\n    category: related_work\n    severity: minor\n    summary: \"缺失 Ding & VanderWeele (2016)\"\n    status: resolved\n    first_raised_round: 8\n    last_seen_round: 11\n    resolution: \"已引用。\"\n    resolution_round: 11\n\n  # === Round 9 ===\n\n  - id: R9-C1\n    category: soundness\n    severity: should-fix\n    summary: \"核心假设（non-differential + proportional effects）在 LLM 场景缺乏实证验证\"\n    status: in_progress\n    first_raised_round: 9\n    last_seen_round: 17\n    mentions:\n      - round: 15\n        reviewers: [R1, R2]\n        note: \"R15 合并到 R6-M3 和 NEW-1。\"\n      - round: 16\n        reviewers: [R1, R2]\n        note: \"R16 合并到 R6-M3 和 NEW-1。\"\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"R17 合并到 R6-M3 和 NEW-1。\"\n\n  - id: R9-C2\n    category: scope\n    severity: should-fix\n    summary: \"线性 SEM 假设对 EMNLP 读者可达性和泛化性不足\"\n    status: in_progress\n    first_raised_round: 9\n    last_seen_round: 17\n    mentions:\n      - round: 15\n        reviewers: [R1, R2]\n        note: \"R15 should-fix。\"\n      - round: 16\n        reviewers: [R1]\n        note: \"R16 R1-M1 降为 minor。\"\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"R17 R1-N3 升回 must-fix：NLP 最常用 logistic regression，bias 表达式在非线性模型下有效性未检验。R2 交叉 PARTIALLY AGREE 降为 should-fix：Appendix B.2/B.7 已有 logistic 验证但分散在附录，主文未提及。Director 采纳 should-fix：已有验证材料，问题在 presentation 而非 absence。\"\n    action_items:\n      - round: 17\n        action: \"Section 4 增加 3-4 句总结 logistic regression 验证结果，引用 Appendix B.2 和 B.7\"\n        assigned_to: agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R9-M1\n    category: soundness\n    severity: should-fix\n    summary: \"K≥3 理论不完整——要求讨论证明技术障碍\"\n    status: in_progress\n    first_raised_round: 9\n    last_seen_round: 17\n    mentions:\n      - round: 15\n        reviewers: [R1, R2]\n        note: \"R15 合并到 R8-C1。\"\n      - round: 16\n        reviewers: [R1, R2]\n        note: \"R16 合并到 R8-C1。\"\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"R17 合并到 R8-C1。\"\n\n  - id: R9-S1\n    category: novelty\n    severity: should-fix\n    summary: \"'first to characterize' novelty claim 需限定\"\n    status: in_progress\n    first_raised_round: 9\n    last_seen_round: 17\n    mentions:\n      - round: 12\n        reviewers: [R1]\n        note: \"R1 REBUT 成功。\"\n      - round: 16\n        reviewers: [R1, R2]\n        note: \"R16 R2-N2 再提为 must-fix。Director 采纳 should-fix。\"\n      - round: 17\n        reviewers: [R2]\n        note: \"R17 R2 新颖性评估确认 'first unified analysis' 在当前文献范围内成立，但 'unified' 主要指系统覆盖而非统一理论。R1 未单独提出。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R9-S2\n    category: presentation\n    severity: should-fix\n    summary: \"Abstract 2.1% 聚合数字掩盖拓扑差异\"\n    status: resolved\n    first_raised_round: 9\n    last_seen_round: 11\n    resolution: \"Abstract 已 topology-specific。\"\n    resolution_round: 11\n\n  - id: R9-S3\n    category: experiments\n    severity: should-fix\n    summary: \"LLM 配置多样性有限（缺 <7B, >70B, ordinal）\"\n    status: in_progress\n    first_raised_round: 9\n    last_seen_round: 17\n    mentions:\n      - round: 15\n        reviewers: [R1, R2]\n        note: \"R15 合并到 R1-W3。\"\n      - round: 16\n        reviewers: [R1]\n        note: \"R16 合并到 R1-W3。\"\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"R17 合并到 R1-W3。\"\n\n  - id: R9-M2\n    category: method\n    severity: should-fix\n    summary: \"ASV 可操作性展示不足——Algorithm 1 与主文脱节\"\n    status: resolved\n    first_raised_round: 9\n    last_seen_round: 11\n    resolution: \"Algorithm 1 被赞为可操作。\"\n    resolution_round: 11\n\n  # === Round 11 ===\n\n  - id: R11-W1\n    category: presentation\n    severity: should-fix\n    summary: \"ClinicalBERT case study 应在正文提及\"\n    status: resolved\n    first_raised_round: 11\n    last_seen_round: 15\n    resolution: \"Section 4.5 已引用 ClinicalBERT。连续三轮未被提出。\"\n    resolution_round: 15\n\n  - id: R11-W2\n    category: presentation\n    severity: should-fix\n    summary: \"Section 3.1 缺少 Notation roadmap——plim/FWL 对 NLP 读者不友好\"\n    status: in_progress\n    first_raised_round: 11\n    last_seen_round: 17\n    mentions:\n      - round: 15\n        reviewers: [R1, R2]\n        note: \"R15 should-fix（高优先级）。\"\n      - round: 16\n        reviewers: [R1, R2]\n        note: \"R16 R2-W2 再提。R1 交叉 AGREE。\"\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"R17 R2-W3 + R1-N3 联合再提。plim/FWL/Wald/column-stochastic/Birkhoff polytope/Dirichlet prior 对 NLP 读者壁垒过高。R1 建议首次出现时添加 parenthetical 直觉解释。R2 建议增加 Intuition 段落。两位共识 should-fix（高优先级）。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R11-W3\n    category: experiments\n    severity: should-fix\n    summary: \"校正方法比较固定 K=3，未验证 K 值敏感性\"\n    status: resolved\n    first_raised_round: 11\n    last_seen_round: 12\n    resolution: \"K=3/5/10 × 7 topologies 完成。Spearman ρ=0.80-0.93。\"\n    resolution_round: 13\n\n  - id: R11-W4\n    category: presentation\n    severity: minor\n    summary: \"IV 52.6% denominator sign change 的 NLP 实践含义未讨论\"\n    status: in_progress\n    first_raised_round: 11\n    last_seen_round: 17\n    mentions:\n      - round: 15\n        reviewers: []\n        note: \"Section 4.2 已添加替代方案。\"\n      - round: 16\n        reviewers: []\n        note: \"R16 未单独提出。\"\n      - round: 17\n        reviewers: []\n        note: \"R17 未单独提出。\"\n\n  - id: R11-MI\n    category: presentation\n    severity: minor\n    summary: \"R1 识别的 minor issues\"\n    status: in_progress\n    first_raised_round: 11\n    last_seen_round: 17\n    mentions:\n      - round: 16\n        reviewers: []\n        note: \"R16 未单独提出。\"\n      - round: 17\n        reviewers: []\n        note: \"R17 未单独提出。\"\n\n  - id: R11-MR1\n    category: related_work\n    severity: should-fix\n    summary: \"缺失引用（R11 新发现）\"\n    status: resolved\n    first_raised_round: 11\n    last_seen_round: 12\n    resolution: \"已添加。\"\n    resolution_round: 13\n\n  # === Round 12 ===\n\n  - id: R12-F1\n    category: format\n    severity: must-fix\n    summary: \"正文溢出至 p9\"\n    status: resolved\n    first_raised_round: 12\n    last_seen_round: 12\n    resolution: \"已压缩。\"\n    resolution_round: 13\n\n  - id: R12-W1\n    category: presentation\n    severity: should-fix\n    summary: \"计量经济学术语对 EMNLP 受众可及性不足\"\n    status: in_progress\n    first_raised_round: 12\n    last_seen_round: 17\n    mentions:\n      - round: 15\n        reviewers: [R1, R2]\n        note: \"R15 与 R11-W2 合并。\"\n      - round: 16\n        reviewers: [R1, R2]\n        note: \"R16 与 R11-W2 合并。\"\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"R17 与 R11-W2 合并。\"\n\n  - id: R12-MR1\n    category: related_work\n    severity: should-fix\n    summary: \"R12 缺失引用\"\n    status: resolved\n    first_raised_round: 12\n    last_seen_round: 12\n    resolution: \"已添加。\"\n    resolution_round: 13\n\n  - id: R12-MI1\n    category: presentation\n    severity: should-fix\n    summary: \"Algorithm 1 阈值硬编码自 K=3 结果\"\n    status: in_progress\n    first_raised_round: 12\n    last_seen_round: 17\n    mentions:\n      - round: 15\n        reviewers: [R1, R2]\n        note: \"R15 should-fix。\"\n      - round: 16\n        reviewers: []\n        note: \"R16 未单独提出。\"\n      - round: 17\n        reviewers: [R1]\n        note: \"R17 R1-M3 再提：Algorithm 1 Step 2 RMSE red. < 0.02 阈值来源未说明。\"\n\n  - id: R12-MI2\n    category: presentation\n    severity: should-fix\n    summary: \"Figure 2 视觉问题\"\n    status: in_progress\n    first_raised_round: 12\n    last_seen_round: 17\n    mentions:\n      - round: 15\n        reviewers: [R1, R2]\n        note: \"R15 minor。\"\n      - round: 16\n        reviewers: [R1, R2]\n        note: \"R16 R2-W4 再提。共识 should-fix。\"\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"R17 两位均再提：灰度打印下 red=sign reversal 难区分，建议使用 hatching pattern。共识 minor。\"\n\n  # === Round 13 ===\n\n  - id: R13-W1\n    category: soundness\n    severity: must-fix\n    summary: \"IV sign reversal 表述在 Abstract/Section 4.2/Appendix B.4 之间 factual 不一致\"\n    status: resolved\n    first_raised_round: 13\n    last_seen_round: 13\n    resolution: \"三处统一。\"\n    resolution_round: 14\n\n  - id: R13-W2\n    category: presentation\n    severity: minor\n    summary: \"部分拓扑缺少 NLP 应用场景示例\"\n    status: resolved\n    first_raised_round: 13\n    last_seen_round: 15\n    resolution: \"已添加。连续两轮未被提出。\"\n    resolution_round: 15\n\n  - id: R13-MR1\n    category: related_work\n    severity: minor\n    summary: \"R13 缺失引用\"\n    status: resolved\n    first_raised_round: 13\n    last_seen_round: 15\n    resolution: \"已在 references.bib 和 Related Work 中引用。\"\n    resolution_round: 15\n\n  - id: R13-CRIT1\n    category: soundness\n    severity: critical\n    summary: \"Limitations 中 diagonal accuracy 范围错误\"\n    status: resolved\n    first_raised_round: 13\n    last_seen_round: 13\n    resolution: \"0.45-0.81 与实际数据一致。\"\n    resolution_round: 14\n\n  # === Round 14 ===\n\n  - id: R14-W1\n    category: presentation\n    severity: minor\n    summary: \"Table 1 Yes/Yes*/No 标注不直观\"\n    status: resolved\n    first_raised_round: 14\n    last_seen_round: 14\n    resolution: \"已改为 Cond./Yes/No。\"\n    resolution_round: 15\n\n  - id: R14-W2\n    category: method\n    severity: should-fix\n    summary: \"IV 拓扑 maximally fragile 后缺少积极替代方案\"\n    status: resolved\n    first_raised_round: 14\n    last_seen_round: 15\n    resolution: \"Section 4.2 已添加三种替代方案。\"\n    resolution_round: 15\n\n  - id: R14-W3\n    category: presentation\n    severity: should-fix\n    summary: \"混淆矩阵 C 的可获得性假设\"\n    status: resolved\n    first_raised_round: 14\n    last_seen_round: 15\n    resolution: \"Limitations 已覆盖。\"\n    resolution_round: 15\n\n  # === Round 15 ===\n\n  - id: R15-N1\n    category: soundness\n    severity: must-fix\n    summary: \"Observation 1 声称 worst-case < 0.005 与 Table 10 不一致（confounding 0.011, front-door 0.013）\"\n    status: in_progress\n    first_raised_round: 15\n    last_seen_round: 17\n    mentions:\n      - round: 15\n        reviewers: [R1, R2]\n        note: \"需修正 Observation 1 数值。\"\n      - round: 16\n        reviewers: []\n        note: \"R16 未单独提出。\"\n      - round: 17\n        reviewers: []\n        note: \"R17 未单独提出。连续两轮未提出。\"\n    action_items:\n      - round: 15\n        action: \"修正 Observation 1 数值\"\n        assigned_to: agent\n        status: in_progress\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R15-W1\n    category: presentation\n    severity: should-fix\n    summary: \"Table 1 Violation vs Sign Flip 列定义模糊\"\n    status: in_progress\n    first_raised_round: 15\n    last_seen_round: 17\n    mentions:\n      - round: 15\n        reviewers: [R1, R2]\n        note: \"需在 caption 中精确定义。\"\n      - round: 16\n        reviewers: [R1, R2]\n        note: \"R16 R2-M1 + R1 交叉 AGREE。\"\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"R17 R2 小问题#3 + R1-M4 再提。应明确 Sign Flip 列指什么（任何系数 vs 主效应），增加脚注定义。两位共识。\"\n    action_items:\n      - round: 15\n        action: \"Table 1 caption 增加列定义\"\n        assigned_to: agent\n        status: in_progress\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R15-W2\n    category: presentation\n    severity: should-fix\n    summary: \"Abstract FWL invariance 声明缺少 'under linear OLS' 限定词\"\n    status: in_progress\n    first_raised_round: 15\n    last_seen_round: 17\n    mentions:\n      - round: 15\n        reviewers: [R1, R2]\n        note: \"修复成本极低。\"\n      - round: 16\n        reviewers: []\n        note: \"R16 未单独提出。\"\n      - round: 17\n        reviewers: []\n        note: \"R17 未单独提出。但 R1-N3 关于线性 SEM 讨论不足间接覆盖。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R15-W3\n    category: method\n    severity: should-fix\n    summary: \"Algorithm 1 经验阈值缺乏理论依据和 DGP 敏感性讨论\"\n    status: in_progress\n    first_raised_round: 15\n    last_seen_round: 17\n    mentions:\n      - round: 15\n        reviewers: [R1, R2]\n        note: \"should-fix。\"\n      - round: 16\n        reviewers: []\n        note: \"R16 未单独提出。\"\n      - round: 17\n        reviewers: [R1]\n        note: \"R17 R1-M3 再提。\"\n\n  # === Round 16 ===\n\n  - id: R16-N1\n    category: presentation\n    severity: should-fix\n    summary: \"2.1% sign reversal 限定不清晰——secondary coefficient 还是 primary coefficient？\"\n    status: in_progress\n    first_raised_round: 16\n    last_seen_round: 17\n    mentions:\n      - round: 16\n        reviewers: [R1, R2]\n        note: \"R16 共识。\"\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"R17 R2-W4 + R1-Q5 再提。Abstract 'sign reversal of secondary coefficients' 首次出现时未定义。'Primary coefficient never reverses' 未出现在 abstract。R1 建议改用 'non-treatment coefficients'。两位共识 should-fix。\"\n    action_items:\n      - round: 16\n        action: \"Abstract 改为 'secondary-coefficient sign reversal'；Table 1 增加脚注\"\n        assigned_to: agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R16-N2\n    category: presentation\n    severity: should-fix\n    summary: \"Correction guidance 深度不足——作为三大贡献之一，Section 4.5 仅半页\"\n    status: in_progress\n    first_raised_round: 16\n    last_seen_round: 17\n    mentions:\n      - round: 16\n        reviewers: [R1, R2]\n        note: \"R16 提出。\"\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"R17 R2-N2 列为 must-fix（Algorithm 1 仅在附录 p.30，五种方法选择标准未在主文讨论）。R1 交叉 REBUT 降为 should-fix：实质内容存在（Table 4 完整对比），修复路径轻量（移入 Algorithm 1 + 方法讨论），contribution framing 对 acceptance 影响有限。Director 采纳 should-fix（高优先级）：同意 R1 判断——内容存在，问题在 presentation。但与端到端验证缺失联合看确实削弱第三贡献的说服力。\"\n    action_items:\n      - round: 16\n        action: \"Section 4.5 扩充\"\n        assigned_to: agent\n        status: open\n      - round: 17\n        action: \"选择路径 (a) 将 Algorithm 1 移入正文 + 增加方法选择讨论，或 (b) 降低 correction guidance 贡献定位为 '附带讨论'\"\n        assigned_to: agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R16-N3\n    category: scope\n    severity: should-fix\n    summary: \"FWL invariance 在 logistic regression 下失效的含义未在主文讨论\"\n    status: in_progress\n    first_raised_round: 16\n    last_seen_round: 17\n    mentions:\n      - round: 16\n        reviewers: [R1, R2]\n        note: \"R16 R2-Q3 提出。\"\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"R17 R1-N3 联合覆盖。R2 交叉回应指出 Appendix B.2 已有 logistic 验证但主文未提及。与 R9-C2 合并处理。\"\n\n  - id: R16-N4\n    category: novelty\n    severity: should-fix\n    summary: \"'First unified analysis' claim 需与 Carroll et al. (2006) 和 Schennach (2020) 显式区分\"\n    status: in_progress\n    first_raised_round: 16\n    last_seen_round: 17\n    mentions:\n      - round: 16\n        reviewers: [R1, R2]\n        note: \"R16 R2-N2 提出。Director 采纳 should-fix。\"\n      - round: 17\n        reviewers: [R2]\n        note: \"R17 R2 新颖性评估确认 'first' 声明在当前文献范围内成立，但需注意 'unified' 主要指系统覆盖。R1 未单独提出。\"\n\n  - id: R16-N5\n    category: presentation\n    severity: minor\n    summary: \"Notation table (Table 19) 放在 Appendix C，主文符号引导分散\"\n    status: in_progress\n    first_raised_round: 16\n    last_seen_round: 17\n    mentions:\n      - round: 16\n        reviewers: [R1, R2]\n        note: \"R16 提出。\"\n      - round: 17\n        reviewers: []\n        note: \"R17 未单独提出。与 R11-W2 术语可达性问题合并。\"\n\n  - id: R16-N6\n    category: presentation\n    severity: minor\n    summary: \"τ vs β_T 含义在 mediator/front-door 拓扑下不清晰\"\n    status: in_progress\n    first_raised_round: 16\n    last_seen_round: 17\n    mentions:\n      - round: 16\n        reviewers: [R1]\n        note: \"R16 R1-M4 提出。\"\n      - round: 17\n        reviewers: []\n        note: \"R17 未单独提出。\"\n\n  - id: R16-MR1\n    category: related_work\n    severity: should-fix\n    summary: \"缺失引用：Miles et al. (2024), Wei et al. (2025), Hernán & Robins (2020), Schennach (2020)\"\n    status: in_progress\n    first_raised_round: 16\n    last_seen_round: 17\n    mentions:\n      - round: 16\n        reviewers: [R1, R2]\n        note: \"R16 提出。\"\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"R17 检查：bib 中已有 miles2024measurement, wei2025multiply, hernan2020causal, schennach2020mismeasured，正文 Related Work 已引用 schennach2020mismeasured, miles2024measurement, wei2025multiply。hernan2020causal 仅在 Section 3.1 引用。本轮未单独重提。\"\n\n  # === Round 17 新发现 ===\n\n  - id: R17-N1\n    category: format\n    severity: must-fix\n    summary: \"Abstract 超过 EMNLP 2026 的 200 words 限制（实际约 245 words）\"\n    status: open\n    first_raised_round: 17\n    last_seen_round: 17\n    mentions:\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"R2-N1 首提为 critical：逐字统计 245 words，超出 22.5%，desk reject 风险。R1 初审仅列为 minor (M1)，交叉审阅后升级为 must-fix。两位共识 must-fix。\"\n    action_items:\n      - round: 17\n        action: \"Abstract 精简至 ≤200 words：聚焦 3-4 核心信息点（K≥3 sign reversal, ASV ranking, FWL invariance），删除具体数值和次要拓扑逐一列举\"\n        assigned_to: agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R17-W1\n    category: soundness\n    severity: should-fix\n    summary: \"Collider sign preservation 仅有经验验证，削弱 Proposition 1 统一框架严谨性\"\n    status: open\n    first_raised_round: 17\n    last_seen_round: 17\n    mentions:\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"R1-W4 首提：Table 2 中 collider 标记为 Empirical（Cauchy-Schwarz/Berkson attenuation），而 confounding 有代数证明。Appendix A.6 Proposition 5 仅证明 proportional case，general case（Proposition 6）只给出 magnitude bound，sign preservation 依赖 100,000 矩阵验证。R2 交叉 AGREE：初审遗漏此缺口。建议在 Proposition 1 明确区分 proved vs empirically verified。\"\n    action_items:\n      - round: 17\n        action: \"Proposition 1 或 Table 2 中明确标注 collider sign preservation 为 empirically verified（非 proved）\"\n        assigned_to: agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R17-W2\n    category: format\n    severity: minor\n    summary: \"Bib 含 2 条未引用条目（dawid1979, rosenbaum2002）\"\n    status: open\n    first_raised_round: 17\n    last_seen_round: 17\n    mentions:\n      - round: 17\n        reviewers: [R2]\n        note: \"R2-W5 提出，R1 交叉 AGREE（承认初审遗漏 bib 清洁度检查）。\"\n    action_items:\n      - round: 17\n        action: \"引用或移除 dawid1979 和 rosenbaum2002\"\n        assigned_to: agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R17-MR1\n    category: related_work\n    severity: minor\n    summary: \"R17 建议补充引用\"\n    status: open\n    first_raised_round: 17\n    last_seen_round: 17\n    mentions:\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"R1 建议：Stefanski & Carroll (1985) logistic measurement error, Oster (2019) coefficient stability, Tan et al. (2024) LLM annotation survey。R2 建议：Jurek et al. (2005) beyond toward-null, Valeri & VanderWeele (2014) mediation measurement error。R2 交叉 AGREE R1 建议。\"\n    resolution: \"\"\n    resolution_round: null"
  }
}
```

</details>

---


### Tool result

_source line 1401 · 2026-05-23T14:03:00.658519+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_issues.yaml\", \"bytes\": 36820}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 1402 · 2026-05-23T14:05:26.226454+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# Round 17 审稿报告\n\n**论文**: Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction\n**Venue**: EMNLP 2026 (ARR Long Paper)\n**审稿轮次**: Round 17 (Fresh Mode)\n**Reviewer 编排**: 2 人（R1: 方法严谨性 / R2: 新颖性与完整性）\n**交叉审阅**: 完成（1 轮交叉后收敛）\n\n---\n\n## Summary\n\n本文系统分析了 LLM 生成的 K-class（K≥3）标注误差在七种典型因果 DAG 拓扑下对因果估计的偏差传播。在线性 SEM 框架下推导了各拓扑的解析 bias 表达式，证明了 K≥3 混淆矩阵可以产生 sign reversal（K=2 时因代数约束不可能），提出 Annotation Sensitivity Values (ASV) 进行 topology-aware 敏感性分析，并证明 FWL 不变性使矩阵校正方法在四种 covariate 拓扑下可证明无效。验证覆盖 161 个场景（23 LLM 配置 × 7 拓扑），MAPE 1.6%。\n\n---\n\n## Strengths\n\n1. **系统性贡献填补重要空白**：首次统一分析 multi-class annotation error 在 7 种 DAG 拓扑下的传播——先前工作仅覆盖 1-2 种拓扑且多限于 K=2。\"First unified analysis\" 声明经核查在当前文献范围内成立。[R1, R2 共识]\n\n2. **K≥3 sign reversal 是非平凡理论发现**：证明了 K=2 的 toward-null 保证因代数约束在 K≥3 时被打破——83.4% Dirichlet(1,1,1) 矩阵在 exposure 下产生 sign reversal，但 primary coefficient 在所有测试配置中均未反转。这是论文最强的理论贡献。[R1, R2 共识]\n\n3. **K=2 理论严谨**：Theorem 1 使用 perspective function convexity 证明 envelope monotonicity，手法巧妙且正确。Proposition 系列的拓扑特定 sign preservation 证明详尽。[R1]\n\n4. **多层次验证充分**：(a) Theory-MC agreement 1.6% MAPE across 161 scenarios；(b) 100,000 Dirichlet 矩阵的 sign preservation 分析；(c) 23 empirical LLM confusion matrices（HumAID K=10, VAST K=3, CivilComments K=2）验证定性模式。[R1, R2 共识]\n\n5. **ASV 三维分解有实用诊断价值**：magnitude / significance / sign-flip 三种 ASV 提供直观的 topology-dependent 风险评估，vulnerability ranking（IV 最脆弱 → M-bias 免疫）为研究设计提供可操作指导。[R1, R2 共识]\n\n6. **FWL 不变性负面结果有重要价值**：代数证明四种 covariate 拓扑下矩阵校正方法在线性回归中可证明无效，引导实践者避免无效校正策略。[R1 证实 FWL 证明为 structural foundation，非纯经验发现]\n\n7. **附录材料详尽（22页）**：完整证明、扩展实验、robustness checks、bootstrap CI 分析，reproducibility 表现优秀。[R2]\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**MF-1** [format] Abstract 超过 EMNLP 2026 的 200 words 限制（约 245 words）\n- R2 初审发现，R1 交叉审阅后从 minor 升级为 must-fix\n- 超出 22.5%，构成实质性 desk reject 风险\n- 当前 abstract 试图覆盖全部七种拓扑结果和多项数值发现，建议精简到 3-4 核心信息点\n- **两位共识 must-fix**\n\n**MF-2** [soundness] K≥3 理论缺口：Conjecture 1 的 ε-近似单调性是论文最大理论弱点\n- Theorem 1 仅证明 K=2 envelope monotonicity\n- Table 10 显示 **60-97% 的随机矩阵违反严格单调性**（confounding 90%, collider 97%, mediation 83%），worst-case deviation ≤0.013\n- K=7 的 42 维参数空间中 10,000 采样覆盖率极低\n- 仅在 default DGP 参数下验证，β/σ² 偏离后 conjecture 是否成立未知\n- ASV vulnerability ranking 的可靠性直接依赖此单调性\n- R1 列为 critical (must-fix)；R2 初审列为 should-fix，交叉后升级为 borderline must-fix\n- **Director 采纳 must-fix**：论文标题聚焦 Multi-Class 但 K≥3 核心结论仅为 conjecture\n\n### Should-Fix（影响评分但不一票否决）\n\n**SF-1** [presentation] Correction Guidance 深度与\"三大贡献\"定位不匹配\n- Section 4.5 仅约半页正文，Algorithm 1 仅在 Appendix p.30\n- 五种方法选择标准、计算成本对比均缺失\n- R2 列为 must-fix；R1 交叉 REBUT 降为 should-fix（实质内容存在于 Table 4 和 Appendix B.15/B.19）\n- **Director 采纳 should-fix（高优先级）**：同意 R1——内容存在，问题在 presentation；但与端到端验证缺失联合看削弱第三贡献\n\n**SF-2** [experiments] 缺乏端到端实证验证 pipeline\n- 论文从未展示完整链条：C estimation → ASV diagnosis → Algorithm 1 routing → correction → improved estimates vs gold-label\n- ClinicalBERT 案例仅覆盖 confounding 单一拓扑\n- R1 列为 must-fix；R2 交叉 PARTIALLY AGREE 降为 should-fix——本文定位为 theoretical contribution，MC 验证是标准验证方式，ground-truth causal effects 在观察性数据中几乎不可获取\n- **Director 采纳 should-fix（高优先级）**：理论贡献无需完整 pipeline，但建议至少展示一个拓扑的路由效果或降低 correction guidance 贡献定位\n\n**SF-3** [novelty] ASV 相对于 E-values 的方法论创新论证不充分\n- 核心数学操作（沿 C(δ) 计算 tipping point）是标准 sensitivity analysis 方法\n- Remark 1 的三点区分主要是应用域差异和参数化差异，非方法论结构创新\n- 拓扑分层能力（同一 C 在不同 DAG 下产生不同 ASV）是 E-value 框架无法自然实现的实质贡献——但论文未通过 worked example 展示\n- **两位共识 should-fix**\n\n**SF-4** [presentation] EMNLP 受众可达性偏低——计量经济学术语壁垒\n- plim、FWL theorem、Wald estimator、column-stochastic、Birkhoff polytope、Dirichlet prior 对 NLP 读者壁垒过高\n- 首次出现时缺乏 parenthetical 直觉解释\n- Section 3.1 缺少 Intuition 段落用 NLP 例子建立直觉\n- **两位共识 should-fix（高优先级）**\n\n**SF-5** [scope] 线性 SEM 假设对 EMNLP 受众的适用性讨论不足\n- NLP 因果推断最常用 logistic regression，bias 表达式在非线性模型下有效性未在主文检验\n- 附录已有部分验证（Appendix B.2 FWL under logistic, B.7 robustness-to-nonlinear-DGP），但主文几乎未提及\n- R1 列为 must-fix；R2 交叉降为 should-fix（验证材料已存在，问题在 presentation）\n- **Director 采纳 should-fix**：已有验证材料，需在主文 Section 4 增加 3-4 句总结\n\n**SF-6** [soundness] Proportional effects 假设 (f=λg) 的可验证性和适用范围\n- Theorem 1 核心条件在实践中不可直接验证\n- 论文未讨论 NLP 场景下何时合理、研究者如何判断\n- Appendix B.13 检查了 OOB 随 departure from proportionality 的变化，但主文未提及\n- **两位共识 should-fix**\n\n**SF-7** [soundness] Non-differential misclassification 假设的 stress test 局限性\n- NLP 文本中 Y 经常嵌入 A 的文本，LLM 可能隐性依赖 Y 信号\n- Stress test 仅 5 个 VAST topics（≤29 per-topic samples），只检查 uniform perturbation\n- 缺少 structured Y-dependent violation 的检验\n- **两位共识 should-fix**\n\n**SF-8** [soundness] Collider sign preservation 仅有经验验证\n- Table 2 中 collider 标记为 \"Empirical\"，而 confounding 有代数证明\n- Proposition 5 仅证明 proportional case，general case（Proposition 6）只给出 magnitude bound\n- 削弱 Proposition 1 统一框架的严谨性\n- R1 首提，R2 交叉 AGREE（初审遗漏）\n- **两位共识 should-fix**\n\n**SF-9** [presentation] \"Sign reversal\" 的 primary vs secondary coefficient 区分不清晰\n- Abstract \"secondary coefficients\" 首次出现时未定义\n- \"Primary coefficient never reverses\" 这一关键信息未出现在 abstract 中\n- Section 4.2 中 \"2.1% sign reversal\" 易被误解为 primary treatment effect reversal\n- **两位共识 should-fix**\n\n### Minor Issues\n\n1. Figure 2：7 子图在半页内拥挤，灰度打印下 red=sign reversal 难区分，建议使用 hatching pattern [R1, R2]\n2. Table 1 \"Cond.\" 列和 \"Sign Flip\" 列含义在 caption 中解释不够，应增加脚注 [R1, R2]\n3. Algorithm 1 Step 2 \"RMSE red. < 0.02\" 阈值来源未说明 [R1]\n4. 23 LLM 配置代表性有限（缺 GPT-4/Claude 等商业模型），但作为理论验证而非 benchmark 可接受 [R1, R2 near-consensus]\n5. Bib 含 2 条未引用条目（dawid1979, rosenbaum2002），应引用或移除 [R2, R1 AGREE]\n6. Appendix 22 页 vs 正文 8 页比例悬殊——虽不违规，但 Algorithm 1 和 Table 4 arguably 属于正文内容 [R2]\n\n---\n\n## Reviewer Consensus [AGREE]\n\n1. **Abstract 超字数为格式硬伤**，需精简至 ≤200 words [MF-1]\n2. **K≥3 Conjecture 1 是论文最大理论缺口**——ASV ranking 可靠性依赖于此 [MF-2]\n3. **ASV 的拓扑分层能力是对 E-value 框架的实质扩展**，但论文未充分论证 [SF-3]\n4. **术语密度对 EMNLP 读者壁垒过高**，需增加直觉解释 [SF-4]\n5. **Proportional effects 和 non-differential 假设需更多讨论** [SF-6, SF-7]\n6. **K≥3 sign reversal 是论文最强理论贡献** [Strengths]\n7. **MC 验证 1.6% MAPE 充分可信** [Strengths]\n\n---\n\n## Reviewer Divergence [REBUT]\n\n| 问题 | R1 | R2 | Director 裁定 |\n|------|----|----|-------------|\n| Correction Guidance | should-fix | must-fix | **should-fix（高优先级）**——内容存在，presentation 问题 |\n| 端到端验证 | must-fix | should-fix | **should-fix（高优先级）**——理论贡献不要求完整 pipeline |\n| 线性 SEM 讨论 | must-fix | should-fix | **should-fix**——附录已有验证，主文需引用 |\n| Conjecture 1 严重性 | must-fix | borderline must-fix | **must-fix**——标题聚焦 Multi-Class 但 K≥3 仅为 conjecture |\n\n---\n\n## Questions（需作者澄清）\n\n1. Conjecture 1 在非 default DGP 参数下（|β|>5 或接近 0）是否仍成立？是否有反例？\n2. 如果将 linear SEM 替换为 logistic regression，bias 表达式的解析推导是否可能？还是只能依赖 MC？\n3. Algorithm 1 要求研究者已知正确 DAG——对 NLP 新手是否构成使用门槛？\n4. Gold labels 不可用时（LLM 标注的主要使用动机），框架推荐什么校正方法？MC-SIMEX 是否在所有拓扑下足够好？\n5. Sign reversal 是否仅限于 secondary coefficients？Primary treatment coefficient 在 exposure 下是否永远安全？\n\n---\n\n## Missing References\n\n**两位 Reviewer 建议补充：**\n- Jurek et al. (2005) \"Proper interpretation of non-differential misclassification effects\" [R2, R1 AGREE]——与 \"beyond toward-null\" 核心主题直接相关\n- Valeri & VanderWeele (2014) mediation measurement error [R2]——与 mediation topology 相关\n- Stefanski & Carroll (1985) logistic regression measurement error [R1]——支撑 linear assumption 边界讨论\n- Oster (2019) coefficient stability [R1]——与 ASV sensitivity 思路可比\n- Tan et al. (2024) LLM annotation survey [R1]——补充 related work 覆盖度\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：**未启用**（项目配置 `external_review.paperreview_ai.enabled: false`）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查 Agent 已派发但异常退出（rate limit error）。未产生有效 findings。用户可选择重新触发。\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.5 / 5 (Borderline Conference)**\n\n**置信度: 4/5**\n\n| 维度 | R1 | R2 | 综合 |\n|------|----|----|------|\n| Soundness | 3.5 | 3.5 (交叉后从4降至3.5) | 3.5 |\n| Excitement | 3 | 3 | 3 |\n| Reproducibility | 4 | — | 4 |\n| Overall | 3.5 | 3.5 | **3.5** |\n\n**理由**：论文填补了 multi-class annotation error × 因果推断的系统性分析空白，K=2 理论严谨，K≥3 sign reversal 是非平凡发现，MC 验证充分。但存在两个关键弱点：(1) K≥3 核心结论仅为数值 conjecture，与论文标题和定位的理论严谨性预期不符；(2) 一个硬性格式违规（abstract 超字数）需在提交前修复。ASV 框架有实用价值但方法论创新边界需更清晰论证。Correction guidance 作为三大贡献之一深度不足（正文仅半页 + 缺端到端验证），需要调整贡献定位或补充内容。EMNLP 受众可达性需通过增加直觉解释来改善。\n\n**修复后前景**：\n- Abstract 超字数是低成本必修项\n- K≥3 理论缺口是结构性问题，短期内无法通过简单修改解决——建议在正文中更诚实地标注为 open problem，明确 ASV ranking 在 ε≤0.013 近似下的稳定性\n- Correction guidance 可通过 (a) 移入 Algorithm 1 + 扩充讨论或 (b) 降级贡献定位来解决\n- 术语可达性和 logistic regression 讨论是低成本高回报修改\n\n若 MF-1（abstract）和关键 SF 问题（SF-1, SF-4, SF-5）得到处理，论文有望从 3.5 提升至 4.0（Conference-level）。MF-2（K≥3 理论缺口）是结构性限制，需要管理预期而非消除。\n\n---\n\n## Detailed Comments\n\n### Section 1 (Introduction)\n- \"first unified analysis of LLM-generated multi-class annotation error propagation across seven canonical DAG topologies in linear SEMs\" 声明经核查成立，但 \"unified\" 主要指系统覆盖而非统一理论——各拓扑 bias expression 仍逐一推导 [R2]\n- 三大贡献中 correction guidance 的深度需与实际内容匹配 [R1, R2]\n\n### Section 3.1 (Setup and Notation)\n- plim/FWL/Wald 首次出现时需 parenthetical 直觉解释 [R1, R2]\n- \"Notation conventions\" 段落是有益的但不够——需为 NLP 读者增加 Intuition 小段落 [R2]\n- Non-differential misclassification (Definition 1)：\"LLM 分类时不观察 Y\" 辩护在 Y 嵌入文本时可能不成立 [R1]\n\n### Section 3.2 (Bias Expressions)\n- Proposition 1 将 confounding（proved）和 collider（empirical）并列，可能给读者造成同等严谨性印象——应明确区分 [R1, R2]\n- \"Numerical Verification 2: Primary coefficient preservation\" 是重要发现但仅为经验事实，abstract 中的表述应一致 [R2]\n\n### Section 3.3 (ASV)\n- Theorem 1 (K=2) 证明严谨 [R1]\n- Conjecture 1 (K≥3)：10,000 矩阵在高维空间覆盖率极低；建议弱化为 \"Empirical Observation\" 或至少明确标注 DGP 依赖性 [R1]\n- Remark 1 的 ASV vs E-value 区分需增加 worked example 展示拓扑分层的实质差异 [R1, R2]\n\n### Section 4 (Experiments)\n- Theory-MC agreement 1.6% MAPE 充分 [R1, R2]\n- Section 4.2 sign reversal 结果中 primary vs secondary coefficient 区分需更清晰 [R1, R2]\n- Section 4.4 empirical validation 使用真实 LLM CM 有说服力，F1-bias 无相关性（ρ=-0.10, p=0.45）是有力结果 [R2]\n- Section 4.5 需扩充或降级贡献定位 [R1, R2]\n- 建议增加 3-4 句总结 Appendix B.2/B.7 的 logistic regression 验证结果 [R2]\n\n### Limitations\n- 当前覆盖范围合适（non-differential assumption, linear SEMs, C known/estimable, end-to-end as future work）\n- 建议增加 proportional effects 假设的讨论 [R1]",
  "project": "causal_annot_error_attrib",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.5 (Borderline Conference)",
  "review_chat_id": "oc_9f117624057fcf6cb95db4d67f525246"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# Round 17 审稿报告\n\n**论文**: Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction\n**Venue**: EMNLP 2026 (ARR Long Paper)\n**审稿轮次**: Round 17 (Fresh Mode)\n**Reviewer 编排**: 2 人（R1: 方法严谨性 / R2: 新颖性与完整性）\n**交叉审阅**: 完成（1 轮交叉后收敛）\n\n---\n\n## Summary\n\n本文系统分析了 LLM 生成的 K-class（K≥3）标注误差在七种典型因果 DAG 拓扑下对因果估计的偏差传播。在线性 SEM 框架下推导了各拓扑的解析 bias 表达式，证明了 K≥3 混淆矩阵可以产生 sign reversal（K=2 时因代数约束不可能），提出 Annotation Sensitivity Values (ASV) 进行 topology-aware 敏感性分析，并证明 FWL 不变性使矩阵校正方法在四种 covariate 拓扑下可证明无效。验证覆盖 161 个场景（23 LLM 配置 × 7 拓扑），MAPE 1.6%。\n\n---\n\n## Strengths\n\n1. **系统性贡献填补重要空白**：首次统一分析 multi-class annotation error 在 7 种 DAG 拓扑下的传播——先前工作仅覆盖 1-2 种拓扑且多限于 K=2。\"First unified analysis\" 声明经核查在当前文献范围内成立。[R1, R2 共识]\n\n2. **K≥3 sign reversal 是非平凡理论发现**：证明了 K=2 的 toward-null 保证因代数约束在 K≥3 时被打破——83.4% Dirichlet(1,1,1) 矩阵在 exposure 下产生 sign reversal，但 primary coefficient 在所有测试配置中均未反转。这是论文最强的理论贡献。[R1, R2 共识]\n\n3. **K=2 理论严谨**：Theorem 1 使用 perspective function convexity 证明 envelope monotonicity，手法巧妙且正确。Proposition 系列的拓扑特定 sign preservation 证明详尽。[R1]\n\n4. **多层次验证充分**：(a) Theory-MC agreement 1.6% MAPE across 161 scenarios；(b) 100,000 Dirichlet 矩阵的 sign preservation 分析；(c) 23 empirical LLM confusion matrices（HumAID K=10, VAST K=3, CivilComments K=2）验证定性模式。[R1, R2 共识]\n\n5. **ASV 三维分解有实用诊断价值**：magnitude / significance / sign-flip 三种 ASV 提供直观的 topology-dependent 风险评估，vulnerability ranking（IV 最脆弱 → M-bias 免疫）为研究设计提供可操作指导。[R1, R2 共识]\n\n6. **FWL 不变性负面结果有重要价值**：代数证明四种 covariate 拓扑下矩阵校正方法在线性回归中可证明无效，引导实践者避免无效校正策略。[R1 证实 FWL 证明为 structural foundation，非纯经验发现]\n\n7. **附录材料详尽（22页）**：完整证明、扩展实验、robustness checks、bootstrap CI 分析，reproducibility 表现优秀。[R2]\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**MF-1** [format] Abstract 超过 EMNLP 2026 的 200 words 限制（约 245 words）\n- R2 初审发现，R1 交叉审阅后从 minor 升级为 must-fix\n- 超出 22.5%，构成实质性 desk reject 风险\n- 当前 abstract 试图覆盖全部七种拓扑结果和多项数值发现，建议精简到 3-4 核心信息点\n- **两位共识 must-fix**\n\n**MF-2** [soundness] K≥3 理论缺口：Conjecture 1 的 ε-近似单调性是论文最大理论弱点\n- Theorem 1 仅证明 K=2 envelope monotonicity\n- Table 10 显示 **60-97% 的随机矩阵违反严格单调性**（confounding 90%, collider 97%, mediation 83%），worst-case deviation ≤0.013\n- K=7 的 42 维参数空间中 10,000 采样覆盖率极低\n- 仅在 default DGP 参数下验证，β/σ² 偏离后 conjecture 是否成立未知\n- ASV vulnerability ranking 的可靠性直接依赖此单调性\n- R1 列为 critical (must-fix)；R2 初审列为 should-fix，交叉后升级为 borderline must-fix\n- **Director 采纳 must-fix**：论文标题聚焦 Multi-Class 但 K≥3 核心结论仅为 conjecture\n\n### Should-Fix（影响评分但不一票否决）\n\n**SF-1** [presentation] Correction Guidance 深度与\"三大贡献\"定位不匹配\n- Section 4.5 仅约半页正文，Algorithm 1 仅在 Appendix p.30\n- 五种方法选择标准、计算成本对比均缺失\n- R2 列为 must-fix；R1 交叉 REBUT 降为 should-fix（实质内容存在于 Table 4 和 Appendix B.15/B.19）\n- **Director 采纳 should-fix（高优先级）**：同意 R1——内容存在，问题在 presentation；但与端到端验证缺失联合看削弱第三贡献\n\n**SF-2** [experiments] 缺乏端到端实证验证 pipeline\n- 论文从未展示完整链条：C estimation → ASV diagnosis → Algorithm 1 routing → correction → improved estimates vs gold-label\n- ClinicalBERT 案例仅覆盖 confounding 单一拓扑\n- R1 列为 must-fix；R2 交叉 PARTIALLY AGREE 降为 should-fix——本文定位为 theoretical contribution，MC 验证是标准验证方式，ground-truth causal effects 在观察性数据中几乎不可获取\n- **Director 采纳 should-fix（高优先级）**：理论贡献无需完整 pipeline，但建议至少展示一个拓扑的路由效果或降低 correction guidance 贡献定位\n\n**SF-3** [novelty] ASV 相对于 E-values 的方法论创新论证不充分\n- 核心数学操作（沿 C(δ) 计算 tipping point）是标准 sensitivity analysis 方法\n- Remark 1 的三点区分主要是应用域差异和参数化差异，非方法论结构创新\n- 拓扑分层能力（同一 C 在不同 DAG 下产生不同 ASV）是 E-value 框架无法自然实现的实质贡献——但论文未通过 worked example 展示\n- **两位共识 should-fix**\n\n**SF-4** [presentation] EMNLP 受众可达性偏低——计量经济学术语壁垒\n- plim、FWL theorem、Wald estimator、column-stochastic、Birkhoff polytope、Dirichlet prior 对 NLP 读者壁垒过高\n- 首次出现时缺乏 parenthetical 直觉解释\n- Section 3.1 缺少 Intuition 段落用 NLP 例子建立直觉\n- **两位共识 should-fix（高优先级）**\n\n**SF-5** [scope] 线性 SEM 假设对 EMNLP 受众的适用性讨论不足\n- NLP 因果推断最常用 logistic regression，bias 表达式在非线性模型下有效性未在主文检验\n- 附录已有部分验证（Appendix B.2 FWL under logistic, B.7 robustness-to-nonlinear-DGP），但主文几乎未提及\n- R1 列为 must-fix；R2 交叉降为 should-fix（验证材料已存在，问题在 presentation）\n- **Director 采纳 should-fix**：已有验证材料，需在主文 Section 4 增加 3-4 句总结\n\n**SF-6** [soundness] Proportional effects 假设 (f=λg) 的可验证性和适用范围\n- Theorem 1 核心条件在实践中不可直接验证\n- 论文未讨论 NLP 场景下何时合理、研究者如何判断\n- Appendix B.13 检查了 OOB 随 departure from proportionality 的变化，但主文未提及\n- **两位共识 should-fix**\n\n**SF-7** [soundness] Non-differential misclassification 假设的 stress test 局限性\n- NLP 文本中 Y 经常嵌入 A 的文本，LLM 可能隐性依赖 Y 信号\n- Stress test 仅 5 个 VAST topics（≤29 per-topic samples），只检查 uniform perturbation\n- 缺少 structured Y-dependent violation 的检验\n- **两位共识 should-fix**\n\n**SF-8** [soundness] Collider sign preservation 仅有经验验证\n- Table 2 中 collider 标记为 \"Empirical\"，而 confounding 有代数证明\n- Proposition 5 仅证明 proportional case，general case（Proposition 6）只给出 magnitude bound\n- 削弱 Proposition 1 统一框架的严谨性\n- R1 首提，R2 交叉 AGREE（初审遗漏）\n- **两位共识 should-fix**\n\n**SF-9** [presentation] \"Sign reversal\" 的 primary vs secondary coefficient 区分不清晰\n- Abstract \"secondary coefficients\" 首次出现时未定义\n- \"Primary coefficient never reverses\" 这一关键信息未出现在 abstract 中\n- Section 4.2 中 \"2.1% sign reversal\" 易被误解为 primary treatment effect reversal\n- **两位共识 should-fix**\n\n### Minor Issues\n\n1. Figure 2：7 子图在半页内拥挤，灰度打印下 red=sign reversal 难区分，建议使用 hatching pattern [R1, R2]\n2. Table 1 \"Cond.\" 列和 \"Sign Flip\" 列含义在 caption 中解释不够，应增加脚注 [R1, R2]\n3. Algorithm 1 Step 2 \"RMSE red. < 0.02\" 阈值来源未说明 [R1]\n4. 23 LLM 配置代表性有限（缺 GPT-4/Claude 等商业模型），但作为理论验证而非 benchmark 可接受 [R1, R2 near-consensus]\n5. Bib 含 2 条未引用条目（dawid1979, rosenbaum2002），应引用或移除 [R2, R1 AGREE]\n6. Appendix 22 页 vs 正文 8 页比例悬殊——虽不违规，但 Algorithm 1 和 Table 4 arguably 属于正文内容 [R2]\n\n---\n\n## Reviewer Consensus [AGREE]\n\n1. **Abstract 超字数为格式硬伤**，需精简至 ≤200 words [MF-1]\n2. **K≥3 Conjecture 1 是论文最大理论缺口**——ASV ranking 可靠性依赖于此 [MF-2]\n3. **ASV 的拓扑分层能力是对 E-value 框架的实质扩展**，但论文未充分论证 [SF-3]\n4. **术语密度对 EMNLP 读者壁垒过高**，需增加直觉解释 [SF-4]\n5. **Proportional effects 和 non-differential 假设需更多讨论** [SF-6, SF-7]\n6. **K≥3 sign reversal 是论文最强理论贡献** [Strengths]\n7. **MC 验证 1.6% MAPE 充分可信** [Strengths]\n\n---\n\n## Reviewer Divergence [REBUT]\n\n| 问题 | R1 | R2 | Director 裁定 |\n|------|----|----|-------------|\n| Correction Guidance | should-fix | must-fix | **should-fix（高优先级）**——内容存在，presentation 问题 |\n| 端到端验证 | must-fix | should-fix | **should-fix（高优先级）**——理论贡献不要求完整 pipeline |\n| 线性 SEM 讨论 | must-fix | should-fix | **should-fix**——附录已有验证，主文需引用 |\n| Conjecture 1 严重性 | must-fix | borderline must-fix | **must-fix**——标题聚焦 Multi-Class 但 K≥3 仅为 conjecture |\n\n---\n\n## Questions（需作者澄清）\n\n1. Conjecture 1 在非 default DGP 参数下（|β|>5 或接近 0）是否仍成立？是否有反例？\n2. 如果将 linear SEM 替换为 logistic regression，bias 表达式的解析推导是否可能？还是只能依赖 MC？\n3. Algorithm 1 要求研究者已知正确 DAG——对 NLP 新手是否构成使用门槛？\n4. Gold labels 不可用时（LLM 标注的主要使用动机），框架推荐什么校正方法？MC-SIMEX 是否在所有拓扑下足够好？\n5. Sign reversal 是否仅限于 secondary coefficients？Primary treatment coefficient 在 exposure 下是否永远安全？\n\n---\n\n## Missing References\n\n**两位 Reviewer 建议补充：**\n- Jurek et al. (2005) \"Proper interpretation of non-differential misclassification effects\" [R2, R1 AGREE]——与 \"beyond toward-null\" 核心主题直接相关\n- Valeri & VanderWeele (2014) mediation measurement error [R2]——与 mediation topology 相关\n- Stefanski & Carroll (1985) logistic regression measurement error [R1]——支撑 linear assumption 边界讨论\n- Oster (2019) coefficient stability [R1]——与 ASV sensitivity 思路可比\n- Tan et al. (2024) LLM annotation survey [R1]——补充 related work 覆盖度\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：**未启用**（项目配置 `external_review.paperreview_ai.enabled: false`）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查 Agent 已派发但异常退出（rate limit error）。未产生有效 findings。用户可选择重新触发。\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.5 / 5 (Borderline Conference)**\n\n**置信度: 4/5**\n\n| 维度 | R1 | R2 | 综合 |\n|------|----|----|------|\n| Soundness | 3.5 | 3.5 (交叉后从4降至3.5) | 3.5 |\n| Excitement | 3 | 3 | 3 |\n| Reproducibility | 4 | — | 4 |\n| Overall | 3.5 | 3.5 | **3.5** |\n\n**理由**：论文填补了 multi-class annotation error × 因果推断的系统性分析空白，K=2 理论严谨，K≥3 sign reversal 是非平凡发现，MC 验证充分。但存在两个关键弱点：(1) K≥3 核心结论仅为数值 conjecture，与论文标题和定位的理论严谨性预期不符；(2) 一个硬性格式违规（abstract 超字数）需在提交前修复。ASV 框架有实用价值但方法论创新边界需更清晰论证。Correction guidance 作为三大贡献之一深度不足（正文仅半页 + 缺端到端验证），需要调整贡献定位或补充内容。EMNLP 受众可达性需通过增加直觉解释来改善。\n\n**修复后前景**：\n- Abstract 超字数是低成本必修项\n- K≥3 理论缺口是结构性问题，短期内无法通过简单修改解决——建议在正文中更诚实地标注为 open problem，明确 ASV ranking 在 ε≤0.013 近似下的稳定性\n- Correction guidance 可通过 (a) 移入 Algorithm 1 + 扩充讨论或 (b) 降级贡献定位来解决\n- 术语可达性和 logistic regression 讨论是低成本高回报修改\n\n若 MF-1（abstract）和关键 SF 问题（SF-1, SF-4, SF-5）得到处理，论文有望从 3.5 提升至 4.0（Conference-level）。MF-2（K≥3 理论缺口）是结构性限制，需要管理预期而非消除。\n\n---\n\n## Detailed Comments\n\n### Section 1 (Introduction)\n- \"first unified analysis of LLM-generated multi-class annotation error propagation across seven canonical DAG topologies in linear SEMs\" 声明经核查成立，但 \"unified\" 主要指系统覆盖而非统一理论——各拓扑 bias expression 仍逐一推导 [R2]\n- 三大贡献中 correction guidance 的深度需与实际内容匹配 [R1, R2]\n\n### Section 3.1 (Setup and Notation)\n- plim/FWL/Wald 首次出现时需 parenthetical 直觉解释 [R1, R2]\n- \"Notation conventions\" 段落是有益的但不够——需为 NLP 读者增加 Intuition 小段落 [R2]\n- Non-differential misclassification (Definition 1)：\"LLM 分类时不观察 Y\" 辩护在 Y 嵌入文本时可能不成立 [R1]\n\n### Section 3.2 (Bias Expressions)\n- Proposition 1 将 confounding（proved）和 collider（empirical）并列，可能给读者造成同等严谨性印象——应明确区分 [R1, R2]\n- \"Numerical Verification 2: Primary coefficient preservation\" 是重要发现但仅为经验事实，abstract 中的表述应一致 [R2]\n\n### Section 3.3 (ASV)\n- Theorem 1 (K=2) 证明严谨 [R1]\n- Conjecture 1 (K≥3)：10,000 矩阵在高维空间覆盖率极低；建议弱化为 \"Empirical Observation\" 或至少明确标注 DGP 依赖性 [R1]\n- Remark 1 的 ASV vs E-value 区分需增加 worked example 展示拓扑分层的实质差异 [R1, R2]\n\n### Section 4 (Experiments)\n- Theory-MC agreement 1.6% MAPE 充分 [R1, R2]\n- Section 4.2 sign reversal 结果中 primary vs secondary coefficient 区分需更清晰 [R1, R2]\n- Section 4.4 empirical validation 使用真实 LLM CM 有说服力，F1-bias 无相关性（ρ=-0.10, p=0.45）是有力结果 [R2]\n- Section 4.5 需扩充或降级贡献定位 [R1, R2]\n- 建议增加 3-4 句总结 Appendix B.2/B.7 的 logistic regression 验证结果 [R2]\n\n### Limitations\n- 当前覆盖范围合适（non-differential assumption, linear SEMs, C known/estimable, end-to-end as future work）\n- 建议增加 proportional effects 假设的讨论 [R1]",
    "project": "causal_annot_error_attrib",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.5 (Borderline Conference)",
    "review_chat_id": "oc_9f117624057fcf6cb95db4d67f525246"
  }
}
```

</details>

---


### Tool result

_source line 1403 · 2026-05-23T14:05:30.702074+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_ca838cd3ed4c7e2d9c8e3459edd98b90:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4475
}
```

</details>

---


### Assistant

_source line 1404 · 2026-05-23T14:05:46.527246+00:00_

Round 17 审稿完成。报告已投递至 Research Director。

**审稿结果：3.5 / 5（Borderline Conference）**

核心发现：

| 类别 | 数量 | 关键问题 |
|------|------|---------|
| Must-Fix | 2 | Abstract 超 200 词限制（245 词，desk reject 风险）；K≥3 Conjecture 1 理论缺口（60-97% 矩阵违反严格单调性） |
| Should-Fix | 9 | Correction guidance 深度不足、端到端验证缺失、ASV novelty 论证偏弱、术语可达性、线性 SEM 讨论、proportional effects、non-differential stress test、collider sign preservation、secondary coefficient 定义 |
| Minor | 6 | Figure 2 可读性、Table 1 列定义、Algorithm 1 阈值、LLM 配置代表性、bib 孤立条目、appendix 体量 |

**两位 Reviewer 均给出 3.5，交叉后达成实质性共识。** 主要分歧在严重性评级（correction guidance 和端到端验证的 must-fix vs should-fix），Director 采纳了更审慎的 should-fix（高优先级）评级。

**修复前景**：Abstract 超字数和术语可达性是低成本必修项。若处理 MF-1 + 关键 SF（SF-1, SF-4, SF-5），论文有望从 3.5 提升至 4.0。K≥3 理论缺口（MF-2）是结构性限制，需管理预期而非消除。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 142

## Round 142

2 recorded events


### User

_source line 1405 · 2026-05-23T14:05:49.135137+00:00_

[Reviewer 2 审稿结果]:
交叉审阅回应已提交给 Review Director。

总结：与 R1 在核心判断上基本一致（K≥3 理论缺口、correction guidance 深度不足、abstract 超限），主要分歧在严重性——R1 的端到端验证缺失和线性 SEM 限制我降级为 should-fix，但认可 R1-W4（collider 仅有经验验证）是我初审遗漏的有效问题。修正后维持 3.5 分，Soundness 微降至 3.5。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1406 · 2026-05-23T14:06:13.515558+00:00_

Round 17 审稿已完成。报告已投递至 Research Director。

**最终评分：3.5 / 5（Borderline Conference）**

**审稿结论摘要：**

**Must-Fix（2 项）：**
1. Abstract 超 EMNLP 2026 的 200 words 限制（约 245 words）——desk reject 风险
2. K≥3 Conjecture 1 理论缺口——论文标题聚焦 Multi-Class 但核心结论仅为数值 conjecture，60-97% 矩阵违反严格单调性

**Should-Fix（9 项，按优先级）：**
- 高优先级：Correction Guidance 深度不足（半页正文 vs 三大贡献之一）、EMNLP 术语可达性、端到端验证缺失
- 中优先级：ASV vs E-values 创新论证、线性 SEM 讨论、Proportional effects 假设、Non-differential stress test、Collider sign preservation 仅经验验证、Sign reversal primary/secondary 区分

**核心优势**：K≥3 sign reversal 是非平凡理论发现，7 拓扑系统覆盖填补重要空白，MC 验证 1.6% MAPE 充分可信。

**修复后前景**：若 abstract 字数 + 关键 presentation 问题（SF-1/4/5）得到处理，有望从 3.5 提升至 4.0（Conference-level）。K≥3 理论缺口是结构性限制，需管理预期而非消除。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 143

## Round 143

50 recorded events


### User

_source line 1407 · 2026-05-23T15:17:36.939602+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: causal_annot_error_attrib
- 论文路径: projects/causal_annot_error_attrib/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: Long Paper (ARR)
- 截止日期: 2026-05-25
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 1408 · 2026-05-23T15:17:42.206332+00:00_

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
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 1409 · 2026-05-23T15:17:42.257230+00:00_

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
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1410 · 2026-05-23T15:17:53.262114+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_local_file",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_local_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 1411 · 2026-05-23T15:17:53.262584+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1412 · 2026-05-23T15:18:09.567541+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "causal_annot_error_attrib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "causal_annot_error_attrib"
  }
}
```

</details>

---


### Tool result

_source line 1413 · 2026-05-23T15:18:10.924369+00:00_

{"result":"# 项目 causal_annot_error_attrib 概况\n\n## 实验状态 (14 个)\n\n- **plan006_asv_empirical**: DONE (success) — \n- **plan010_annot_sensitivity_toolkit**: DONE (success) — \n- **plan003_empirical_confusion_matrices**: DONE (failed) — \n- **plan007_correction_guidance**: DONE (success) — \n- **plan009_pathological_matrices**: DONE (success) — \n- **plan005_asv_extended**: DONE (success) — \n- **plan002_k57_extension**: DONE (success) — \n- **plan001_dag_taxonomy**: DONE (success) — \n- **plan004_asv_framework**: DONE (success) — \n- **plan_004_asv_v3_fixed**: DONE (success) — \n- **plan008_binarization_collapse**: DONE (success) — \n- **mvp_exposure_dirichlet_subspace**: DONE (success) — \n- **mvp_exposure_dag**: DONE (success) — \n- **mvp_confounding_dag**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-21\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n（无）\n\n## 近期结论\n- **plan006_asv_empirical** (success): 真实 LLM confusion matrices（跨 K=2/3/10，跨 7B/235B 模型）在 7 种 DAG 拓扑下的偏差传播与理论预测一致：(1) F1 高不代表因果估计安全（F1=0.72 但 IV bias>100%），(2) 0 sign flips 确认结构性保证，(3) topology（非 K 或 model size）是 bias 的主要决定因素。\n- **plan010_annot_sensitivity_toolkit** (success): 封装 7-topology bias computation、ASV sensitivity framework 和 5 种 correction 方法为可复用 Python 包，使 practitioners 能用 3 行代码评估 LLM 标注误差对因果推断的影响。验证：(1) API 输出与 plan_001/004/005/007 原始脚本一致，(2) worked example 展示完整工作流，(3) 35 个 pytest 全通过。\n- **plan003_empirical_confusion_matrices** (failed): Different LLMs (Llama-4-Maverick, Qwen3-235B, DeepSeek-Chat) produce systematically different confusion matrices on the same classification tasks, and these empirical confusion matrices can be used to quantify annotation error propagation in downstream causal inference.\n\n## 趋势\n成功 13 / 负向 0 / 失败 1 / 共 14\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nhome-1x5090: 无 GPU 信息\n\n## 告警\n- plan003_empirical_confusion_matrices: 训练失败 — unknown"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1356
}
```

</details>

---


### Tool call

_source line 1414 · 2026-05-23T15:18:11.075492+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 1415 · 2026-05-23T15:18:11.578427+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	
4	\usepackage{graphicx}
5	\usepackage{algorithm}
6	\usepackage{algorithmic}
7	
8	\usepackage{amsmath,amssymb,amsthm}
9	\usepackage{booktabs}
10	\usepackage{pifont}
11	\usepackage{multirow}
12	
13	\newtheorem{definition}{Definition}
14	\newtheorem{proposition}{Proposition}
15	\newtheorem{theorem}{Theorem}
16	\newtheorem{lemma}{Lemma}
17	\newtheorem{conjecture}{Conjecture}
18	\newtheorem{observation}{Observation}
19	\newtheorem{remark}{Remark}
20	
21	\setlength{\textfloatsep}{8pt plus 2pt minus 4pt}
22	\setlength{\dbltextfloatsep}{8pt plus 2pt minus 4pt}
23	\setlength{\floatsep}{8pt plus 2pt minus 4pt}
24	\setlength{\dblfloatsep}{8pt plus 2pt minus 4pt}
25	\graphicspath{{../../figures/paper/}}
26	
27	\title{Multi-Class Annotation Errors in Causal Inference:\\Topology-Dependent Bias, Sensitivity, and Correction}
28	
29	\author{Anonymous}
30	
31	\begin{document}
32	\maketitle
33	
34	\input{abstract}
35	
36	\input{introduction}
37	
38	\begin{figure*}[t]
39	\centering
40	\includegraphics[width=0.92\textwidth,height=0.18\textheight,keepaspectratio]{fig1_dag_taxonomy.pdf}
41	\vspace{-6pt}
42	\caption{Seven canonical DAG topologies with starred-node annotation~\cite{hernan_cole2009}. $A$ (latent) $\to$ $A^*$ (observed) via a dashed measurement edge; the causal role of $A$ varies: treatment (exposure), covariate (confounding, mediation, M-bias, front-door), selection (collider), instrument (IV).}
43	\label{fig:dag_taxonomy}
44	\end{figure*}
45	
46	\input{related_work}
47	
48	\input{method}
49	
50	\input{experiments}
51	
52	\input{conclusion}
53	
54	\bibliography{references}
55	
56	\appendix
57	\input{appendix_proofs}
58	
59	\end{document}
60	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 1416 · 2026-05-23T15:18:11.628990+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "causal_annot_error_attrib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "causal_annot_error_attrib"
  }
}
```

</details>

---


### Tool result

_source line 1417 · 2026-05-23T15:18:11.679515+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1418 · 2026-05-23T15:18:26.402914+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 1419 · 2026-05-23T15:18:26.805627+00:00_

1	\begin{abstract}
2	Large language models are increasingly used as annotators in computational social science, yet annotation errors propagate into downstream causal estimates in ways that depend on both the confusion matrix structure and the causal DAG topology. We derive bias expressions for seven canonical topologies under $K$-class non-differential misclassification and show that $K {\geq} 3$ introduces a structural possibility of sign reversal absent in the binary case. We prove sign preservation for confounding and collider, and verify it numerically for mediation, M-bias, and front-door; exposure and IV topologies can reverse the treatment effect sign. Under realistic LLM accuracy, sign reversal of non-dominant coefficients occurs under exposure; under empirical LLM matrices (diagonal 0.45--0.81), sign reversal is confined to exposure; IV is fragile under uniform Dirichlet priors but exhibits zero reversals under empirical LLM matrices. We introduce Annotation Sensitivity Values (ASVs), with proved ($K{=}2$) and numerically verified ($K{\geq}3$) monotonicity, yielding a vulnerability ranking from IV (maximally fragile) to M-bias (immune), and show that matrix-based corrections are provably ineffective under linear regression for four topologies due to Frisch--Waugh--Lovell invariance. Topology-aware analysis is necessary for valid causal inference with LLM-generated annotations.
3	\end{abstract}
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 1420 · 2026-05-23T15:18:26.805894+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 1421 · 2026-05-23T15:18:27.308567+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Large language models are rapidly replacing human annotators in computational social science, with researchers using LLM-generated labels for tasks ranging from sentiment classification to political stance detection~\cite{gilardi2023chatgpt, ziems2024can, egami_hinck_stewart_wei2023, baumann2025}. Crucially, most of these tasks are inherently multi-class: stance detection uses 3--4 categories, sentiment analysis 5, and disaster response taxonomies 10 or more. This shift promises dramatic cost reduction, but introduces a critical validity gap: annotation errors (equivalently, misclassification) from imperfect classifiers propagate into downstream causal estimates in ways that depend on both the error structure and the causal design. \citet{baumann2025} demonstrate that across 37 annotation tasks, 31\% of hypotheses yield incorrect conclusions with state-of-the-art LLMs, rising to 50\% for smaller models; these errors are highly correlated across models (60\% agreement when both err)~\cite{kim_garg2025}, undermining ensemble-based mitigation. Analyzing the \emph{structure} of annotation error, rather than simply reducing its magnitude, is essential for valid downstream inference.
5	
6	The transition at $K{\geq}3$ is not gradual but structural. For $K{=}2$, the stochastic constraint forces any confusion matrix with positive diagonal to preserve coefficient signs---an algebraic property of the $2{\times}2$ matrix dimension~\cite{brenner1993}. This guarantee \emph{vanishes} at $K{\geq}3$: the higher-dimensional confusion matrix admits negative effective weights on categories with opposite-sign coefficients, enabling sign reversal even under high accuracy~\cite{veirod_laake2001}. Under a uniform Dirichlet prior, 83.4\% of $K{=}3$ exposure confusion matrices produce sign reversal of at least one secondary coefficient; under realistic accuracy (diagonal $\geq 0.7$), 2.1\% still do. The primary treatment coefficient, h
…[truncated 2884 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 1422 · 2026-05-23T15:18:27.309013+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 1423 · 2026-05-23T15:18:27.761353+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Measurement error in causal inference.}
5	The foundations are established in \citet{carroll2006}, \citet{gustafson2004}, \citet{buonaccorsi2010}, and \citet{bound2001measurement}, with starred-node DAGs formalized by \citet{hernan_cole2009} and DAG-based correction theory developed by \citet{kuroki_pearl2014}. For binary variables, non-differential misclassification biases toward the null~\cite{brenner1993, ogburn_vanderweele2012}, with \citet{neuhaus1999} quantifying the attenuation and efficiency loss in binary regression under known misclassification rates; but this fails for polytomous exposures~\cite{dosemeci1990, jurek2005, veirod_laake2001}. \citet{edwards_lessler_naimi2021} showed dependent misclassification can bias in either direction, and \citet{shu_yi2019a, shu_yi2019b} develop weighted estimators that jointly handle mismeasured covariates and misclassified outcomes under IPW---a concern that also drives mediation analyses with mismeasured mediators~\cite{imai_keele_tingley2010, valeri_vanderweele2013, valeri_vanderweele2014}. \citet{schennach2020mismeasured} addresses general nonclassical measurement error in regression; \citet{miles2024measurement} construct instrumental variables for measurement-error-robust estimation; \citet{wei2025multiply} develop multiply robust estimators under misclassified treatment. All analyze a single DAG topology; ours is the first to characterize how the \emph{same} confusion matrix produces qualitatively different bias across seven topologies.
6	
7	\paragraph{Text classifiers and LLM annotation.}
8	\citet{grimmer2022} and \citet{feder_etal2022} provide foundations for text-as-data and causal inference in NLP. \citet{wood_doughty2018} first applied DAG reasoning to classifier error; \citet{teblunthuis2024} gave the most complete binary treatment ($K{=}2$, four DAGs); \citet{lee_wood_doughty2024} extended to categorical LLM classifiers but covered only con
…[truncated 2617 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 1424 · 2026-05-23T15:18:27.761603+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 1425 · 2026-05-23T15:18:28.264754+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Setup and Notation}
5	\label{sec:notation}
6	
7	Let $A$ denote a true $K$-class categorical variable (e.g., sentiment with $K{=}3$ levels) and $A^*$ its observed, potentially misclassified version produced by an LLM annotator. The misclassification process is characterized by a $K{\times}K$ confusion matrix $C$ with entries $C_{jk} = P(A^*{=}j \mid A{=}k)$, where each column sums to one. Following \citet{hernan_cole2009}, we represent this measurement process using \emph{starred-node} DAGs: the true variable $A$ is latent, and the observed $A^*$ is connected to $A$ via a dashed measurement edge.
8	
9	\paragraph{Notation conventions.}
10	Our analysis characterizes systematic bias---the value an estimator converges to as $N \to \infty$ (the probability limit, or plim)---rather than finite-sample variance. The Frisch--Waugh--Lovell (FWL) theorem guarantees that each regression coefficient equals the coefficient from a simple regression after residualizing all other variables; this is why matrix-based corrections fail for covariate topologies (Section~\ref{sec:correction}): replacing the mismeasured variable with a corrected version does not change the residualized relationship. The Wald estimator (ratio of reduced-form to first-stage effects) diverges under weak instruments; Dirichlet priors over probability vectors represent uncertainty over misclassification patterns. Table~\ref{tab:notation} (Appendix~\ref{app:notation_table}) collects all notation.
11	
12	\begin{definition}[Non-differential misclassification]
13	\label{def:nondiff}
14	Misclassification of $A$ is non-differential with respect to outcome $Y$ and covariates $\mathbf{Z}$ if $P(A^*{=}j \mid A{=}k, Y, \mathbf{Z}) = P(A^*{=}j \mid A{=}k) = C_{jk}$ for all $j,k$.
15	\end{definition}
16	
17	This holds when the LLM classifies without observing the outcome---the typical CSS setup~\cite{ziems2024can}; topic-stratified confusion matrices confirm cross-gro
…[truncated 14068 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 503
}
```

</details>

---


### Tool call

_source line 1426 · 2026-05-23T15:18:28.265043+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 1427 · 2026-05-23T15:18:28.717621+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We validate through Monte Carlo simulation ($K{=}3$), cross-$K$ robustness checks ($K{=}5,7$), and empirical validation with real LLM confusion matrices from three NLP tasks ($K{=}2,3,10$).
5	
6	\subsection{Setup}
7	\label{sec:setup}
8	
9	For each topology, we sample 100{,}000 confusion matrices from a Dirichlet$(1,1,1)$ prior, compute analytical probability limits, and validate against Monte Carlo simulation ($N{=}10{,}000$). ASV experiments use $C(\delta) = (1{-}\delta)I + \delta C_0$.
10	
11	\subsection{Bias Taxonomy}
12	\label{sec:taxonomy_results}
13	
14	\paragraph{Theory-MC agreement.}
15	Analytical probability limits match Monte Carlo estimates with grand MAPE of 1.6\% across 161 scenarios (23 LLM configurations $\times$ 7 topologies; per-topology range: 0.3\%--3.7\%).
16	
17	\paragraph{Exposure DAG: sign reversal under multi-class misclassification.}
18	Under realistic LLM accuracy (diagonal $\geq 0.7$), the violation rate is 13.7\% with 2.1\% sign reversal; even at diagonal $\geq 0.9$, violation persists at 11.9\%. Under the full Dirichlet$(1,1,1)$ prior, 85\% of $K{=}3$ confusion matrices violate the binary ``toward-null'' guarantee, and 83.4\% cause sign reversal of at least one coefficient; the minimum diagonal entry $\min_k C_{kk} < 0.55$ predicts sign reversal with 91\% accuracy across empirical matrices (Appendix~\ref{sec:sign_determinants}). The $K{=}2$ control confirms that all tested binary matrices maintain classical attenuation~\cite{brenner1993}, establishing that the multi-class failure is structurally distinct.
19	
20	\paragraph{Structural guarantee for non-exposure topologies.}
21	Five topologies exhibit zero sign-flip rate (Table~\ref{tab:taxonomy}): confounding, mediation, and front-door show 100\% amplification~\cite{brenner1993, dosemeci1990} but never reverse the sign; collider is protective ($|B(C)|$ non-increasing; Conjecture~\ref{conj:monotone}); M-bias shows weakest sensitivity (
…[truncated 7269 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 1428 · 2026-05-23T15:18:28.717890+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1429 · 2026-05-23T15:18:29.723155+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We characterized how multi-class annotation errors interact with causal DAG topology: the binary attenuation guarantee breaks at $K \geq 3$, where exposure and IV can reverse treatment effect signs while five topologies preserve them. ASVs yield a vulnerability ranking from IV (most fragile) to M-bias (immune); matrix-based corrections are provably ineffective for four covariate topologies due to FWL invariance. Practitioners using LLM annotations in causal designs should identify their DAG topology and compute topology-specific ASV before choosing a correction strategy---$F_1$ alone does not predict downstream risk. Proving envelope monotonicity for general $K$ and extending the framework to nonlinear models and differential misclassification are the primary open directions. Code and data will be released.
5	
6	\section*{Limitations}
7	
8	We assume non-differential misclassification (Appendix~\ref{sec:nondiff_stress}). Bias expressions assume $K{=}3$ linear SEMs; proving $K{\geq}3$ envelope monotonicity remains the primary open question~\cite{schennach2020mismeasured}, though rankings are stable across $K{=}3,5,10$. The framework requires estimable $C$; experiments are Monte Carlo without end-to-end causal benchmarks.
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 1005
}
```

</details>

---


### Tool call

_source line 1430 · 2026-05-23T15:18:29.774090+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex"
  }
}
```

</details>

---


### Tool result

_source line 1431 · 2026-05-23T15:18:30.176227+00:00_

File content (44099 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 1432 · 2026-05-23T15:18:30.176562+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 1433 · 2026-05-23T15:18:30.679642+00:00_

1	% Auto-generated from literature_map.yaml — all verified=true entries
2	% Last sync: 2026-05-23
3	
4	@article{valeri_vanderweele2014,
5	  author    = {Valeri, Linda and VanderWeele, Tyler J.},
6	  title     = {The Estimation of Direct and Indirect Causal Effects in the Presence of Misclassified Binary Mediator},
7	  journal   = {Biostatistics},
8	  volume    = {15},
9	  number    = {3},
10	  pages     = {498--512},
11	  year      = {2014},
12	  doi       = {10.1093/biostatistics/kxu007}
13	}
14	
15	@article{stefanski_carroll1985,
16	  author    = {Stefanski, Leonard A. and Carroll, Raymond J.},
17	  title     = {Covariate Measurement Error in Logistic Regression},
18	  journal   = {The Annals of Statistics},
19	  volume    = {13},
20	  number    = {4},
21	  pages     = {1335--1351},
22	  year      = {1985},
23	  doi       = {10.1214/aos/1176349741}
24	}
25	
26	@article{oster2019,
27	  author    = {Oster, Emily},
28	  title     = {Unobservable Selection and Coefficient Stability: Theory and Evidence},
29	  journal   = {Journal of Business \& Economic Statistics},
30	  volume    = {37},
31	  number    = {2},
32	  pages     = {187--204},
33	  year      = {2019},
34	  doi       = {10.1080/07350015.2016.1227711}
35	}
36	
37	@inproceedings{tan2024llm,
38	  author    = {Tan, Zhen and Li, Dawei and Wang, Song and Beigi, Alimohammad and Jiang, Bohan and Bhattacharjee, Amrita and Karami, Mansooreh and Li, Jundong and Cheng, Lu and Liu, Huan},
39	  title     = {Large Language Models for Data Annotation and Synthesis: A Survey},
40	  booktitle = {Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing},
41	  pages     = {930--957},
42	  year      = {2024},
43	}
44	
45	@article{cinelli2020making,
46	  author    = {Cinelli, Carlos and Hazlett, Chad},
47	  title     = {Making Sense of Sensitivity: Extending Omitted Variable Bias},
48	  journal   = {Journal of the Royal Statistical Society: Series B (Statistical Methodology)},
49	  year      = {2020
…[truncated 22698 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 503
}
```

</details>

---


### Tool call

_source line 1434 · 2026-05-23T15:18:30.680031+00:00_

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
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
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

_source line 1435 · 2026-05-23T15:18:30.730436+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1436 · 2026-05-23T15:18:53.792701+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers submission guidelines ARR"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission guidelines ARR"
  }
}
```

</details>

---


### Tool call

_source line 1437 · 2026-05-23T15:18:56.254733+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 1438 · 2026-05-23T15:18:56.456351+00:00_

1	\section{Proofs of Proposition~\ref{prop:signflip} and Theorem~\ref{thm:monotone}}
2	\label{app:proof}
3	
4	We provide algebraic proofs of sign preservation for the confounding and collider topologies (Proposition~\ref{prop:signflip}(a)--(b)), an explicit counterexample for exposure (Proposition~\ref{prop:signflip}(c)), numerical verification for mediation, M-bias, and front-door (Numerical Verification~1), and the monotonicity proof for confounding (Theorem~\ref{thm:monotone}).
5	Throughout, $A\in\{0,1,\dots,K{-}1\}$ with prior $p_k=P(A{=}k)$, and $C$ is a $K{\times}K$ column-stochastic confusion matrix with $C_{jk}=P(A^*{=}j\mid A{=}k)$.
6	We use category~0 as the reference and let $D_j=\mathbf{1}(A{=}j)$, $D_j^*=\mathbf{1}(A^*{=}j)$ for $j=1,\dots,K{-}1$.
7	
8	\subsection{Notation and Key Identities}
9	\label{app:notation}
10	
11	Under non-differential misclassification, the misclassified moments factor linearly through $C$.
12	Define the population vectors:
13	\begin{align}
14	  q_j &= P(A^*{=}j) = \textstyle\sum_k C_{jk}\,p_k, \label{eq:q}\\
15	  \mathrm{ct}_j &= \mathbb{E}[T\cdot D_j^*] = \textstyle\sum_k C_{jk}\,\mathbb{E}[T\cdot D_k], \label{eq:ct}\\
16	  \mathrm{cy}_j &= \mathbb{E}[Y\cdot D_j^*] = \textstyle\sum_k C_{jk}\,\mathbb{E}[Y\cdot D_k]. \label{eq:cy}
17	\end{align}
18	Write $q = Cp$, $\mathrm{ct} = C\,\mathbb{E}[T\cdot D]$, and $\mathrm{cy} = C\,\mathbb{E}[Y\cdot D]$, where $D=(D_0,\dots,D_{K-1})^\top$.
19	
20	\subsection{Frisch--Waugh--Lovell Decomposition}
21	\label{app:fwl}
22	
23	For topologies where $T$ is directly observed (confounding, mediation, collider, M-bias, front-door), the estimator regresses $Y$ on $Z^*=(1,T,D_1^*,\dots,D_{K-1}^*)$.
24	By the Frisch--Waugh--Lovell (FWL) theorem, the coefficient on $T$ satisfies:
25	\begin{equation}
26	  \operatorname{plim}\hat{\tau}(C)
27	  = \frac{\mathbb{E}[\tilde{T}\,\tilde{Y}]}{\mathbb{E}[\tilde{T}^2]},
28	  \label{eq:fwl}
29	\end{equation}
30	where $\tilde{T}=T-\mathbb{E}[T\mid A^*]$ and $\ti
…[truncated 8484 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 1439 · 2026-05-23T15:18:56.506924+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1440 · 2026-05-23T15:18:56.809690+00:00_

1	issues:
2	  # === Round 1-7 历史 (resolved，保留摘要) ===
3	
4	  - id: R1-N1
5	    category: soundness
6	    severity: must-fix
7	    summary: "Theorem 1 适用范围过窄（仅 confounding+proportional effects），K≥3 证明不完整"
8	    status: resolved
9	    first_raised_round: 1
10	    last_seen_round: 7
11	    resolution: "Theorem 1 现正确限定为 K=2；K≥3 由 Observation 1 和 Conjecture 1 覆盖。"
12	    resolution_round: 7
13	
14	  - id: R1-N2
15	    category: soundness
16	    severity: should-fix
17	    summary: "3/5 安全拓扑的符号保持仅有数值验证，Abstract 用 'establish' 暗示已证明"
18	    status: resolved
19	    first_raised_round: 1
20	    last_seen_round: 3
21	    resolution: "Abstract 已准确区分 prove/verify。"
22	    resolution_round: 4
23	
24	  - id: R1-N3
25	    category: soundness
26	    severity: must-fix
27	    summary: "ASV C(δ) 定义域错误"
28	    status: resolved
29	    first_raised_round: 1
30	    last_seen_round: 1
31	    resolution: "Section 3.3 已引入 δ_max 约束。"
32	    resolution_round: 2
33	
34	  - id: R2-N1
35	    category: presentation
36	    severity: must-fix
37	    summary: "83.4% sign reversal headline framing 过度声称"
38	    status: resolved
39	    first_raised_round: 1
40	    last_seen_round: 5
41	    resolution: "Introduction 已重写。"
42	    resolution_round: 5
43	
44	  - id: R2-N2
45	    category: novelty
46	    severity: should-fix
47	    summary: "'first systematic framework' 过度声明"
48	    status: resolved
49	    first_raised_round: 1
50	    last_seen_round: 1
51	    resolution: "已修复。"
52	    resolution_round: 2
53	
54	  - id: R2-N3
55	    category: related_work
56	    severity: must-fix
57	    summary: "4 篇关键相关工作未引用"
58	    status: resolved
59	    first_raised_round: 1
60	    last_seen_round: 1
61	    resolution: "已修复。"
62	    resolution_round: 2
63	
64	  - id: R1-W2
65	    category: clarity
66	    severity: should-fix
67	    summary: "Sign preservation 的 DGP 条件在实践中难以事前验证"
68	    status: resolved
69	    first_raised_round: 1
70	    last_seen_round: 2
71	    resolution: "Section 3.2 已添加 ASV 替代讨论。"
72	    resolution_
…[truncated 41299 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 302
}
```

</details>

---


### Tool result

_source line 1441 · 2026-05-23T15:19:01.691617+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines ARR"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title":"Submission Guide","url":"https://nlp4climate.github.io/submissionguide/"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"AI Conference Deadlines - Jie Cao | Dialogue, NLP, ML","url":"https://mlciv.com/ai-deadlines/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"}]

Based on the search results, here's information about EMNLP 2026 call for papers submission guidelines through ARR:

## Paper Types and Scope

EMNLP 2026 invites the submission of long and short papers featuring substantial, original, and unpublished research on empirical methods for Natural Language Processing. Papers may contribute negative findings, survey an area, announce the creation of a new resource, argue a position, report novel linguistic insights derived using existing computational techniques, and reproduce (or fail to reproduce) previous results.

## ARR Submission Process

The ARR submission deadline for long and short papers is May 25, 2026. Given that the ARR 2026 May cycle is aligned with both EMNLP and A
…[truncated 753 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "WebSearch",
  "elapsed_ms": 7898
}
```

</details>

---


### Tool call

_source line 1442 · 2026-05-23T15:19:43.391735+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "causal_annot_error_attrib",
  "file": "paper_checklist.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "causal_annot_error_attrib",
    "file": "paper_checklist.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1443 · 2026-05-23T15:19:44.296931+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'causal_annot_error_attrib'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 905
}
```

</details>

---


### Tool call

_source line 1444 · 2026-05-23T15:19:44.598934+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex",
  "offset": "200",
  "limit": "300"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex",
    "offset": "200",
    "limit": "300"
  }
}
```

</details>

---


### Tool result

_source line 1445 · 2026-05-23T15:19:44.650116+00:00_

200	  &\leq \mathbb{E}\bigl[\sqrt{\operatorname{Var}(g\mid A^*)\,\operatorname{Var}(f\mid A^*)}\bigr]\\
201	  &\leq \sqrt{\mathbb{E}[\operatorname{Var}(g\mid A^*)]\;\mathbb{E}[\operatorname{Var}(f\mid A^*)]}\\
202	  &\leq \sqrt{\operatorname{Var}(g(A))\;\operatorname{Var}(f(A))},
203	\end{align*}
204	where the last step uses $\mathbb{E}[\operatorname{Var}(X\mid Y)]\leq\operatorname{Var}(X)$ (law of total variance).
205	
206	\emph{Step 2: Conclude.}
207	The bias satisfies
208	\[
209	  |B(C)| = \frac{|R(C)|}{D(C)} \leq \frac{\sqrt{\operatorname{Var}(g)\,\operatorname{Var}(f)}}{\sigma_T^2} = \bar{B}.
210	\]
211	When $|\tau|>\bar{B}$, the bias cannot cancel $\tau$, so $\operatorname{sign}(\operatorname{plim}\hat\tau)=\operatorname{sign}(\tau)$ for all $C$.
212	\end{proof}
213	
214	\paragraph{Relationship to the omitted-variable condition.}
215	A weaker (necessary) condition for sign preservation is $\operatorname{sign}(\tau)=\operatorname{sign}(\tau_{\mathrm{OV}})$ where $\tau_{\mathrm{OV}}=\tau+\operatorname{Cov}(g,f)/\operatorname{Var}(T)$.
216	If this fails, then $C=\frac{1}{K}\mathbf{1}\mathbf{1}^\top$ (uniform noise) already flips the sign.
217	The rigorous sufficient condition $|\tau|>\bar{B}$ implies the weaker condition, since $|B_{\mathrm{OV}}|=|\operatorname{Cov}(g,f)|/\operatorname{Var}(T)\leq\bar{B}$ by Cauchy--Schwarz and $\operatorname{Var}(T)\geq\sigma_T^2$.
218	
219	\paragraph{Verification for paper parameters ($K{=}3$).}
220	With $\tau{=}2.0$, $\boldsymbol{\alpha}{=}(1.5,{-}1.0)$, $\boldsymbol{\beta}^{(A)}{=}(1.0,{-}0.5)$, $\sigma_T{=}1.0$, $\mathbf{p}{=}(0.40,0.35,0.25)$:
221	\begin{align*}
222	  \operatorname{Var}(g) &= \sum_k p_k\alpha_k^2 - \bigl(\textstyle\sum_k p_k\alpha_k\bigr)^2 = 0.962,\\
223	  \operatorname{Var}(f) &= \sum_k p_k(\beta_k^{(A)})^2 - \bigl(\textstyle\sum_k p_k\beta_k^{(A)}\bigr)^2 = 0.362,\\
224	  \bar{B} &= \sqrt{0.962\times 0.362}\;/\;1.0^2 = 0.590.
225	\end{align*}
226	Since $|\tau|{=}2.0 > \bar{B}{=}0.590$, sign preservation 
…[truncated 22412 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1446 · 2026-05-23T15:20:46.385320+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "causal_annot_error_attrib",
  "review_chat_id": "oc_9f117624057fcf6cb95db4d67f525246"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "causal_annot_error_attrib",
    "review_chat_id": "oc_9f117624057fcf6cb95db4d67f525246"
  }
}
```

</details>

---


### Tool result

_source line 1447 · 2026-05-23T15:21:11.713607+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 25328
}
```

</details>

---


### Tool call

_source line 1448 · 2026-05-23T15:21:11.965250+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "你是 Reviewer 1，负责**方法严谨性**审查。\n\n## 论文信息\n- **标题**: Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction\n- **论文路径**: `projects/causal_annot_error_attrib/docs/paper/main.tex`（各章节 abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, conclusion.tex, appendix_proofs.tex）\n- **PDF**: `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_18/submitted.pdf`\n- **目标 Venue**: EMNLP 2026 (ARR Long Paper)\n- **截止日期**: 2026-05-25\n- **格式要求**: ACL 模板 (`\\usepackage[review]{acl}`)，正文 8 页限制（不含参考文献和 Limitations），双盲审稿\n\n## 你的审查侧重\n\n**方法严谨性和理论基础**，重点关注以下方面：\n\n1. **理论证明完整性**：\n   - Theorem 1（Envelope monotonicity）仅证明了 K=2 confounding/mediation。论文对 K≥3 使用 Observation 1 和 Conjecture 1（数值验证）——这个三级层次（Proved → Verified → Conjectured）是否恰当？K≥3 结论的理论支撑是否充分？\n   - Proposition 1 的 sign preservation 条件（confounding: Cauchy-Schwarz, collider: Berkson attenuation）——条件是否充分必要？哪些是解析证明、哪些是经验验证？是否混淆了两者？\n\n2. **核心假设合理性**：\n   - **Non-differential misclassification**（Definition 1）：在 NLP/LLM 场景下是否合理？LLM 预训练数据可能编码了 A-Y 关联，这是否违反该假设？Stress test 覆盖是否充分？\n   - **Proportional effects** (f=λg)：在 NLP 任务中是否可验证？violation 时的退化行为讨论是否充分？\n   - **线性 SEM 假设**：NLP 最常用 logistic regression，论文是否充分讨论了非线性模型下的有效性？（检查 Appendix 中是否有 logistic regression 验证，以及主文是否引用）\n\n3. **FWL invariance 证明**：\n   - 四种 covariate 拓扑下 matrix-based correction 0% bias reduction 的证明——推导是否完整严谨？\n   - 在 logistic regression 下 FWL invariance 打破的含义是否在主文讨论？\n\n4. **实验验证**：\n   - MC 验证：1.6% grand MAPE 是否充分？per-topology 范围如何？\n   - 100,000 Dirichlet 矩阵采样：对 K≥5 的高维空间覆盖率是否足够？\n   - 23 个 LLM 配置的代表性如何？\n\n5. **ASV 框架的理论基础**：\n   - C(δ) 参数化是否合理？δ_max 约束是否充分讨论？\n   - 三种 ASV（magnitude, significance, sign-flip）的定义是否严谨？significance ASV 对 N 的依赖是否充分讨论？\n\n请按 ACL/ARR 审稿标准输出完整审稿报告，包含：Summary, Strengths, Weaknesses（按 must-fix / should-fix / minor 分级），Questions, Missing References, Overall Assessment（使用 EMNLP 2026 ARR 评分标准：5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after, 1=Do not resubmit），Confidence（1-5）。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "你是 Reviewer 1，负责**方法严谨性**审查。\n\n## 论文信息\n- **标题**: Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction\n- **论文路径**: `projects/causal_annot_error_attrib/docs/paper/main.tex`（各章节 abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, conclusion.tex, appendix_proofs.tex）\n- **PDF**: `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_18/submitted.pdf`\n- **目标 Venue**: EMNLP 2026 (ARR Long Paper)\n- **截止日期**: 2026-05-25\n- **格式要求**: ACL 模板 (`\\usepackage[review]{acl}`)，正文 8 页限制（不含参考文献和 Limitations），双盲审稿\n\n## 你的审查侧重\n\n**方法严谨性和理论基础**，重点关注以下方面：\n\n1. **理论证明完整性**：\n   - Theorem 1（Envelope monotonicity）仅证明了 K=2 confounding/mediation。论文对 K≥3 使用 Observation 1 和 Conjecture 1（数值验证）——这个三级层次（Proved → Verified → Conjectured）是否恰当？K≥3 结论的理论支撑是否充分？\n   - Proposition 1 的 sign preservation 条件（confounding: Cauchy-Schwarz, collider: Berkson attenuation）——条件是否充分必要？哪些是解析证明、哪些是经验验证？是否混淆了两者？\n\n2. **核心假设合理性**：\n   - **Non-differential misclassification**（Definition 1）：在 NLP/LLM 场景下是否合理？LLM 预训练数据可能编码了 A-Y 关联，这是否违反该假设？Stress test 覆盖是否充分？\n   - **Proportional effects** (f=λg)：在 NLP 任务中是否可验证？violation 时的退化行为讨论是否充分？\n   - **线性 SEM 假设**：NLP 最常用 logistic regression，论文是否充分讨论了非线性模型下的有效性？（检查 Appendix 中是否有 logistic regression 验证，以及主文是否引用）\n\n3. **FWL invariance 证明**：\n   - 四种 covariate 拓扑下 matrix-based correction 0% bias reduction 的证明——推导是否完整严谨？\n   - 在 logistic regression 下 FWL invariance 打破的含义是否在主文讨论？\n\n4. **实验验证**：\n   - MC 验证：1.6% grand MAPE 是否充分？per-topology 范围如何？\n   - 100,000 Dirichlet 矩阵采样：对 K≥5 的高维空间覆盖率是否足够？\n   - 23 个 LLM 配置的代表性如何？\n\n5. **ASV 框架的理论基础**：\n   - C(δ) 参数化是否合理？δ_max 约束是否充分讨论？\n   - 三种 ASV（magnitude, significance, sign-flip）的定义是否严谨？significance ASV 对 N 的依赖是否充分讨论？\n\n请按 ACL/ARR 审稿标准输出完整审稿报告，包含：Summary, Strengths, Weaknesses（按 must-fix / should-fix / minor 分级），Questions, Missing References, Overall Assessment（使用 EMNLP 2026 ARR 评分标准：5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after, 1=Do not resubmit），Confidence（1-5）。"
  }
}
```

</details>

---


### Tool result

_source line 1449 · 2026-05-23T15:21:39.572738+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_9f117624057fcf6cb95db4d67f525246:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 27607
}
```

</details>

---


### Tool call

_source line 1450 · 2026-05-23T15:21:39.925579+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "你是 Reviewer 2，负责**新颖性和完整性**审查。\n\n## 论文信息\n- **标题**: Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction\n- **论文路径**: `projects/causal_annot_error_attrib/docs/paper/main.tex`（各章节 abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, conclusion.tex, appendix_proofs.tex）\n- **PDF**: `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_18/submitted.pdf`\n- **目标 Venue**: EMNLP 2026 (ARR Long Paper)\n- **截止日期**: 2026-05-25\n- **格式要求**: ACL 模板 (`\\usepackage[review]{acl}`)，正文 8 页限制（不含参考文献和 Limitations），双盲审稿\n\n## 你的审查侧重\n\n**新颖性、完整性和呈现质量**，重点关注以下方面：\n\n1. **新颖性评估**：\n   - **ASV vs E-value**：ASV 框架相比 E-values (VanderWeele & Ding 2017)、partial R² bounds (Cinelli & Hazlett 2020)、coefficient stability (Oster 2019) 等现有 sensitivity analysis 工具的方法论创新边界在哪里？论文是否充分展示了 ASV 能得出而 E-value 无法得出的定性结论？检查 Remark 1 的三点对比是否充分。\n   - **\"First unified analysis\" claim**：Introduction 中声称\"first unified analysis of LLM-generated multi-class annotation error propagation across seven canonical DAG topologies under structural equation models\"——这与 Carroll et al. (2006)、Schennach (2020)、Teblunthuis (2024) 的工作如何区分？是否过度声明？\n   - **三大贡献的均衡性**：(1) Bias taxonomy, (2) ASV, (3) Correction guidance——每个贡献的深度是否对得起\"贡献\"的定位？特别是第三个贡献（correction guidance），Section 4.5 是否足够深入？Algorithm 1 是否在主文中还是仅在附录？\n\n2. **呈现质量（NLP 受众可达性）**：\n   - **术语壁垒**：plim, FWL theorem, Wald estimator, column-stochastic matrix, Birkhoff polytope, Dirichlet prior——这些计量经济学/统计学术语对 EMNLP 读者是否有充分的直觉解释？\n   - **符号系统**：τ 在不同拓扑下的具体含义（confounding=coefficient on X, exposure=category-specific β_j, mediation=direct effect）——是否有清晰的 notation roadmap？\n   - **信息密度**：Abstract 和 Introduction 的数字密度是否过高？（检查 Abstract 是否超过 200 words）\n   - **Section 3.1 Notation paragraph**：是否为 NLP 读者提供了足够的背景？\n\n3. **格式合规性**：\n   - 正文是否在 8 页以内？（需从 PDF 确认）\n   - Abstract 字数是否在 200 words 以内？（去掉 LaTeX 命令后逐字计数）\n   - 双盲要求：是否有泄露作者身份的信息？\n   - Limitations section 是否存在且位置正确（正文中，非 Appendix）？\n   - 引用格式是否一致（natbib/ACL style）？\n\n4. **引用完整性**：\n   - Related Work 是否覆盖了关键相关工作？以下领域是否有遗漏：\n     - Measurement error in causal inference（经典）\n     - LLM annotation quality（近期）\n     - Sensitivity analysis frameworks\n     - Correction/debiasing methods\n   - 检查 bib 文件中是否有未引用的条目（orphan entries）\n\n5. **Figure 和 Table 质量**：\n   - Figure 1 (DAG taxonomy)：是否清晰传达七种拓扑？\n   - Figure 2 (Bias distribution)：灰度打印下红色（sign reversal）是否可区分？\n   - Table 1 (Taxonomy)：列定义是否清晰？Sign Flip 列指的是什么（任何系数 vs 主效应）？caption 是否充分？\n   - Figure 3 (ASV ranking)：信息传达是否有效？\n   - Figure 4 (F1 vs bias)：核心信息是否一目了然？\n\n请按 ACL/ARR 审稿标准输出完整审稿报告，包含：Summary, Strengths, Weaknesses（按 must-fix / should-fix / minor 分级），Questions, Missing References, Overall Assessment（使用 EMNLP 2026 ARR 评分标准：5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after, 1=Do not resubmit），Confidence（1-5）。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "你是 Reviewer 2，负责**新颖性和完整性**审查。\n\n## 论文信息\n- **标题**: Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction\n- **论文路径**: `projects/causal_annot_error_attrib/docs/paper/main.tex`（各章节 abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, conclusion.tex, appendix_proofs.tex）\n- **PDF**: `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_18/submitted.pdf`\n- **目标 Venue**: EMNLP 2026 (ARR Long Paper)\n- **截止日期**: 2026-05-25\n- **格式要求**: ACL 模板 (`\\usepackage[review]{acl}`)，正文 8 页限制（不含参考文献和 Limitations），双盲审稿\n\n## 你的审查侧重\n\n**新颖性、完整性和呈现质量**，重点关注以下方面：\n\n1. **新颖性评估**：\n   - **ASV vs E-value**：ASV 框架相比 E-values (VanderWeele & Ding 2017)、partial R² bounds (Cinelli & Hazlett 2020)、coefficient stability (Oster 2019) 等现有 sensitivity analysis 工具的方法论创新边界在哪里？论文是否充分展示了 ASV 能得出而 E-value 无法得出的定性结论？检查 Remark 1 的三点对比是否充分。\n   - **\"First unified analysis\" claim**：Introduction 中声称\"first unified analysis of LLM-generated multi-class annotation error propagation across seven canonical DAG topologies under structural equation models\"——这与 Carroll et al. (2006)、Schennach (2020)、Teblunthuis (2024) 的工作如何区分？是否过度声明？\n   - **三大贡献的均衡性**：(1) Bias taxonomy, (2) ASV, (3) Correction guidance——每个贡献的深度是否对得起\"贡献\"的定位？特别是第三个贡献（correction guidance），Section 4.5 是否足够深入？Algorithm 1 是否在主文中还是仅在附录？\n\n2. **呈现质量（NLP 受众可达性）**：\n   - **术语壁垒**：plim, FWL theorem, Wald estimator, column-stochastic matrix, Birkhoff polytope, Dirichlet prior——这些计量经济学/统计学术语对 EMNLP 读者是否有充分的直觉解释？\n   - **符号系统**：τ 在不同拓扑下的具体含义（confounding=coefficient on X, exposure=category-specific β_j, mediation=direct effect）——是否有清晰的 notation roadmap？\n   - **信息密度**：Abstract 和 Introduction 的数字密度是否过高？（检查 Abstract 是否超过 200 words）\n   - **Section 3.1 Notation paragraph**：是否为 NLP 读者提供了足够的背景？\n\n3. **格式合规性**：\n   - 正文是否在 8 页以内？（需从 PDF 确认）\n   - Abstract 字数是否在 200 words 以内？（去掉 LaTeX 命令后逐字计数）\n   - 双盲要求：是否有泄露作者身份的信息？\n   - Limitations section 是否存在且位置正确（正文中，非 Appendix）？\n   - 引用格式是否一致（natbib/ACL style）？\n\n4. **引用完整性**：\n   - Related Work 是否覆盖了关键相关工作？以下领域是否有遗漏：\n     - Measurement error in causal inference（经典）\n     - LLM annotation quality（近期）\n     - Sensitivity analysis frameworks\n     - Correction/debiasing methods\n   - 检查 bib 文件中是否有未引用的条目（orphan entries）\n\n5. **Figure 和 Table 质量**：\n   - Figure 1 (DAG taxonomy)：是否清晰传达七种拓扑？\n   - Figure 2 (Bias distribution)：灰度打印下红色（sign reversal）是否可区分？\n   - Table 1 (Taxonomy)：列定义是否清晰？Sign Flip 列指的是什么（任何系数 vs 主效应）？caption 是否充分？\n   - Figure 3 (ASV ranking)：信息传达是否有效？\n   - Figure 4 (F1 vs bias)：核心信息是否一目了然？\n\n请按 ACL/ARR 审稿标准输出完整审稿报告，包含：Summary, Strengths, Weaknesses（按 must-fix / should-fix / minor 分级），Questions, Missing References, Overall Assessment（使用 EMNLP 2026 ARR 评分标准：5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after, 1=Do not resubmit），Confidence（1-5）。"
  }
}
```

</details>

---


### Tool result

_source line 1451 · 2026-05-23T15:21:41.282102+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_9f117624057fcf6cb95db4d67f525246:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1356
}
```

</details>

---


### Tool call

_source line 1452 · 2026-05-23T15:21:48.570852+00:00_

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
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
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

_source line 1453 · 2026-05-23T15:21:48.621316+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1454 · 2026-05-23T15:21:59.880558+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 1: Reviewer 独立初审（R1 方法严谨性 + R2 新颖性完整性）', 'status': 'in_progress', 'activeForm': '等待两位 Reviewer 完成独立初审'}, {'content': 'Step 2: 交叉分享——将每位 Reviewer 原文转发给对方，收集逐条回应', 'status': 'pending', 'activeForm': '执行交叉分享'}, {'content': 'Step 3: 收敛判断——分析共识与分歧', 'status': 'pending', 'activeForm': '判断是否收敛'}, {'content': 'Step 4: 汇总报告——合成审稿报告、同步 Issue Tracker、投递', 'status': 'pending', 'activeForm': '汇总并投递审稿报告'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Step 1: Reviewer 独立初审（R1 方法严谨性 + R2 新颖性完整性）', 'status': 'in_progress', 'activeForm': '等待两位 Reviewer 完成独立初审'}, {'content': 'Step 2: 交叉分享——将每位 Reviewer 原文转发给对方，收集逐条回应', 'status': 'pending', 'activeForm': '执行交叉分享'}, {'content': 'Step 3: 收敛判断——分析共识与分歧', 'status': 'pending', 'activeForm': '判断是否收敛'}, {'content': 'Step 4: 汇总报告——合成审稿报告、同步 Issue Tracker、投递', 'status': 'pending', 'activeForm': '汇总并投递审稿报告'}]"
  }
}
```

</details>

---


### Tool result

_source line 1455 · 2026-05-23T15:21:59.931187+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "TodoWrite",
  "elapsed_ms": 50
}
```

</details>

---


### Assistant

_source line 1456 · 2026-05-23T15:22:09.625246+00:00_

已派发所有任务：
- **视觉审查 Agent**: 已启动（fire-and-forget）
- **Reviewer 1**（方法严谨性）: 已分配，等待回稿
- **Reviewer 2**（新颖性/完整性）: 已分配，等待回稿

等待两位 Reviewer 完成独立初审。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 144

## Round 144

2 recorded events


### User

_source line 1457 · 2026-05-23T15:31:10.655335+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 审稿报告：方法严谨性审查

**论文**: Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction
**Venue**: EMNLP 2026 (ARR Long Paper)
**审查侧重**: 方法严谨性和理论基础

---

## Summary

本文研究多类别标注误差（来自 LLM 标注器）如何在不同因果 DAG 拓扑下传播到下游因果估计。核心贡献包括：(1) 在 K 类非差异错分类假设下，推导 7 种典型 DAG 拓扑的闭式偏差表达式；(2) 证明 K=2 时的包络单调性（Theorem 1），并对 K≥3 提供数值验证（Observation 1）和猜想（Conjecture 1）；(3) 定义标注敏感性值（ASV）框架，包含幅度、显著性和符号翻转三种度量；(4) 证明 Frisch-Waugh-Lovell（FWL）不变性，表明矩阵校正方法在四种协变量拓扑下无效；(5) 通过 Monte Carlo 模拟（161 个场景，grand MAPE 1.6%）和 23 个真实 LLM 配置进行验证。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 核心框架在其假设内严谨；K=2 证明完整，K≥3 诚实地标注为 Observation/Conjecture；但两个关键假设（比例效应 f=λg、非差异错分类）在 NLP 场景下的合理性论证不足 |
| Excitement | 3.5/5 | 问题重要且时效性强（LLM 标注 × 因果推断），理论框架有新意（ASV、FWL 不变性），但受众较窄（因果推断 + NLP + 测量误差理论的交叉领域） |
| Reproducibility | 4/5 | MC 模拟设置描述详细（N=10,000, Dirichlet(1,1,...,1) 采样, 100,000 矩阵），DGP 参数完整，但未提及代码/数据公开计划 |
| Overall Assessment | 3.5/5 | Borderline Conference — 理论贡献真实但假设限制了实用性 |
| Confidence | 4/5 | 熟悉因果推断和测量误差文献，仔细检查了证明结构 |

---

## 主要优势

**S1. 系统性拓扑分类**: 首次在统一框架内分析 7 种典型 DAG 拓扑 × K 类错分类的偏差行为（Section 3.2）。每种拓扑的闭式偏差表达式（plim 公式 (1)-(5)）推导清晰，涵盖 confounding、exposure、mediation、collider、M-bias、front-door 和 IV。这是对先前仅覆盖单一拓扑或二分类工作（Lee and Wood-Doughty 2021, Feder et al. 2022）的实质性扩展。

**S2. 诚实的认知层级**: 论文明确区分三级证明状态 —— Proved（K=2, Theorem 1）→ Verified（K≥3, Observation 1, ε<0.02）→ Conjectured（Conjecture 1）。这种透明度在理论论文中值得赞赏，避免了对 K≥3 结果的过度声称。Remark 1 明确指出 "analytic proofs for general K remain open"。

**S3. FWL 不变性负面结果**: Appendix B.2 的列空间论证（col(D*M) = col(D) for invertible M）证明了在 OLS 下矩阵校正方法对四种协变量拓扑完全无效（0% bias reduction）。这是一个干净、完整的结构性结果，对实践者有重要指导意义。Table 5 进一步验证了在 logistic regression 下不变性的破缺（|Δ bias| < 0.04），增强了结论的完整性。

**S4. 实验验证的深度**: Grand MAPE 1.6%（per-topology 0.3%-3.7%）基于 161 个场景的 MC 验证（Section 4.2）。同时使用 3 个 NLP 数据集（HumanAID K=10, VAST K=5, CivilComments K=2）的 23 个真实 LLM 配置，涵盖 zero-shot 和 few-shot 设置。ClinicalBERT case study（Appendix B.3）提供了端到端应用示例。

**S5. 实用框架**: ASV 与 E-value（VanderWeele and Ding 2017）类比设计得当，C(δ) 参数化提供了沿一维路径的敏感性分析。Algorithm 1 的拓扑感知校正决策树为实践者提供了清晰的操作指南。

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] **比例效应假设 (f=λg) 在 NLP 场景下的合理性论证严重不足**

- 具体位置：Theorem 1（Section 3.2, p.6）、Appendix B.13
- 问题：Theorem 1 的核心单调性保证要求所有类别特异性处理效应成比例（f(j)=λg(j)）。这意味着多类别处理的各类别对结果的效应只是同一函数的缩放版本。在 NLP 因果推断中，多类别处理（如 stance detection: favor/against/neutral/none）的不同类别可能对结果有质性不同的效应（例如 "favor" 和 "against" 可能有相反方向的效应），不满足比例关系。
- Appendix B.13 的敏感性分析表明 A(C) 越界率从 exact proportional 的 0% 快速上升到 r=0.5 时的 10.3% 和 r=0.1 时的 22.1%。论文声称 "NLP-realistic DGP" 仅有 0.07% 违规率，但这依赖于一组特定的 DGP 参数，未充分论证其对典型 NLP 因果设置的代表性。
- 为什么影响接收：如果 f≠λg，Theorem 1 的单调性保证可能失效，直接削弱论文的核心理论贡献。论文需要更具体地讨论：(a) 在哪些 NLP 任务中比例效应成立/不成立；(b) 当假设近似但不精确满足时，保证如何退化。
- 建议修改方向：增加 2-3 个具体 NLP 因果推断场景的讨论，分析比例效应假设的合理性；或者提供更一般性的理论结果（不需要 f=λg 的 relaxed version），即使只能给出更弱的保证。

**N2** [critical] **非差异错分类假设在 LLM 标注器语境下需要更深入的实证检验**

- 具体位置：Definition 1（Section 3.1, p.4）、Appendix B.5-B.6
- 问题：Definition 1 要求 P(A*=j | A=k, Y) = P(A*=j | A=k)，即标注误差与结果变量 Y 独立。然而 LLM 的预训练数据编码了大量 A-Y 关联：例如在情感分析中，LLM 对包含强烈结果信号的文本可能有系统性不同的标注准确率。这与经典的人工标注场景（标注者不知道 Y）有本质区别。
- Appendix B.5 的 VAST topic-stratified 检验（per-topic max deviation 95th percentile 0.18-0.43）表明 topic 层面的错分类率差异与抽样变异一致。但这只是一个数据集（K=5），且 topic 分层不等于按 Y 分层——论文没有直接按 Y 值分层检验错分类率。
- Appendix B.6 的 stress test 使用合成差异扰动（ε 参数），展示了 ε=0.10 时 sign-flip 率增加 7.6 pp、ε=0.50 时达到 34.6%。这证明了违反假设时的脆弱性，但没有回答关键问题：**真实 LLM 标注的 ε 是多少？**
- 为什么影响接收：如果非差异性不成立，所有 7 个拓扑的偏差表达式（公式 (1)-(5)）都无效，论文的全部理论结果失去基础。对于面向 NLP 受众的 EMNLP 投稿，这个假设的实证支撑尤为重要。
- 建议修改方向：(a) 在至少一个有 gold labels 的 NLP 数据集上，按 Y 值分层计算 LLM 错分类矩阵，直接检验 P(A*|A,Y=0) ≈ P(A*|A,Y=1)；(b) 更明确地讨论哪些 LLM 标注流程设计（如只提供文本不提供标签）能增强非差异性假设的合理性。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] **Dirichlet(1,1,...,1) 采样对高维 K 的代表性不足**

- 具体位置：Section 4.1 (p.7), Observation 1, Conjecture 1 verification
- 问题：K≥3 的数值验证使用 100,000 个 Dirichlet(1,1,...,1) 采样矩阵。均匀 Dirichlet 先验产生的矩阵在单纯形中心附近分布密集（对角线条目期望为 1/K），而真实 LLM 混淆矩阵是强对角占优的（对角线条目通常 >0.6）。对于 K=5（20 个自由参数）和 K=7（42 个自由参数），均匀采样可能无法充分覆盖实践中相关的混淆矩阵子空间。
- 论文在 Appendix B.4（diagonal ≥ 0.5 子空间）有部分验证，Conjecture 1 也限定在对角线条件下。但主文没有明确讨论采样分布与真实 LLM 矩阵分布的差异。
- 建议：补充使用集中在对角线附近的 Dirichlet(α,1,...,1)（α>>1）采样的验证结果，或明确报告现有验证中对角线 >0.6 子空间的 ε 值。

**W2** [warning] **Logistic regression 的处理不充分**

- 具体位置：Section 4.5 (p.8), Appendix B.7, B.14, Table 5
- 问题：NLP 因果推断中最常用的是 logistic regression（二元/多类别结果）。论文的核心理论在线性 SEM 下建立，logistic regression 的讨论主要在附录中（B.7: FWL 不变性破缺; B.14: logistic bias reduction negligible < 0.05）。主文只用一句话提及 "Under logistic regression the invariance breaks"（Section 4.5, p.8）。
- Table 5 提供了 OLS vs logistic 的比较（6 个 confusion matrix 配置，K=3），但只有一种 DGP 设置。
- Algorithm 1 的校正决策树没有区分 OLS 和 logistic regression 的不同路径。
- 建议：在主文 Section 4.5 中增加 1-2 段对 logistic regression 用户的明确指导；在 Algorithm 1 中加入 OLS/logistic 分支。

**W3** [warning] **Significance ASV 对样本量 N 的依赖缺乏充分探讨**

- 具体位置：Section 3.3 (p.5), Figure 3 (p.7)
- 问题：Significance ASV δ_sig 通过 SE(N) 依赖于 N，论文提到 "exhibiting a sharp phase transition at a critical N*"，但没有系统展示 N 如何影响拓扑间的脆弱性排名。Figure 3 只展示了一个 N 值的排名。Appendix B.8 的 bootstrap CI convergence 结果（δ=1,000, N*=6,000-10,000）有用但不够系统。
- 建议：增加一个 Figure 展示不同 N（如 500, 1000, 5000, 10000）下各拓扑的 significance ASV 变化，帮助实践者选择适当的样本量。

**W4** [warning] **Conjecture 1 的 ε 约束缺乏理论解释**

- 具体位置：Conjecture 1 (p.6), Appendix B.12
- 问题：Conjecture 1 声称非 IV 拓扑下 |B(C(δ))| 是 ε-近似单调的，ε < 0.02 for |β|≤1。这个 0.02 的约束完全来自数值实验（20,000 random C_0 matrices per K）。论文没有解释为什么 ε 应该很小——是否有结构性原因使得偏差函数在高维混淆矩阵空间中近似凸？没有理论直觉支撑，这个猜想的可信度受限。
- 建议：提供关于为什么 ε 应该很小的直觉论证（即使不是完整证明）——例如，是否与列随机矩阵空间的几何性质（凸体结构，Appendix A.9 提到的 (K-1)-dimensional convex body）有关？

---

## 小问题（不影响接收）

- **M1**: "plim" 符号在 NLP 社区不常见（概率极限，来自计量经济学），首次使用时可加脚注解释。
- **M2**: Figure 2（p.6）仅展示 K=3 的偏差分布，对 K=5 和 K=7 的可视化仅在附录。考虑到论文强调多类别，主文至少应展示一个 K≥5 的示意。
- **M3**: 附录体量巨大（24 页，Appendix A-C），包含 B.1-B.24 共 24 个子节。部分交叉引用密集（如 Section 3.2 连续引用 Appendix A.3, A.4, A.5, A.6, B.1, B.7, B.8），读者需要频繁跳转。建议在主文中增加关键证明的直觉 sketch。
- **M4**: Section 3.3 中 "sign-flip ASV" 定义为 δ_sign = min{δ | sign(f) ≠ sign(τ)} + sign(τ) · sign(f(I)) — 最后的 sign(τ)·sign(f(I)) 项的含义和作用不够清晰，需要额外解释。
- **M5**: 主文页数可能略超 8 页限制（Section 5 Conclusion 起始于第 9 页顶部）。需确认排版是否满足 EMNLP 2026 strict 8-page limit（Limitations 和 References 不计入）。

---

## Questions to Authors

**Q1**: Theorem 1 的比例效应假设 (f=λg) 在论文的 ClinicalBERT case study（Appendix B.3, K=4 smoking status）中是否被检验过？具体来说，不同吸烟状态类别（never/past/current/unknown）对 echocardiography 死亡率的效应是否近似成比例？

**Q2**: 对于 Conjecture 1 中 exposure 拓扑的例外（ε 可以较大），论文指出 "the safe/fragile partition — line fragile" 特性（Section 3.2, p.6）。能否更精确地刻画什么条件下 exposure 的 ε 变大？是否与混淆矩阵的特定谱性质有关？

**Q3**: 论文提到 Appendix B.17 验证了 23 个真实 LLM 混淆矩阵中 97.3% 满足 Theorem 1 条件（Table 17, A(C) ∈ [0,1]）。那 2.7% 不满足的配置有什么共同特征？是否与特定 LLM（如较小的模型）或特定数据集相关？

**Q4**: FWL 不变性在 logistic regression 下破缺（Table 5, |Δ bias| < 0.04）。对于更大的 K 和更偏离线性的 DGP，这个破缺幅度是否会显著增大？Table 5 只测试了 K=3 和一组 DGP。

**Q5**: ASV 的 C(δ) = (1-δ)I + δC_0 参数化沿单一路径搜索。在 K≥3 时，混淆矩阵空间是 (K-1)K 维的。是否考虑过多维 ASV（例如沿不同方向的最小扰动）？如果否，沿单一路径可能遗漏的最坏情况偏差有多大？

---

## Missing References

论文的相关文献覆盖较为充分。建议考虑以下补充引用：

1. **Imai and Yamamoto (2010)**, "Causal Inference with Differential Measurement Error" — 讨论差异性测量误差下的因果推断，与本文的非差异性假设形成对比，可在 Limitations 或 Related Work 中引用。

2. **Ogburn and VanderWeele (2012)**, "On the nondifferential misclassification of a binary confounder" 已被引用，但 **Ogburn and VanderWeele (2013)** 关于 bias amplification under covariate misclassification 的后续工作可考虑引用以加强 exposure 拓扑的讨论。

---

## 总体评分

**Overall**: **3.5/5 — Borderline Conference**

**一句话总结**: 论文在统一框架下首次系统分析了多类别标注误差在 7 种 DAG 拓扑下的因果偏差传播，理论构建（FWL 不变性、ASV）有真实贡献且实验验证充分，但两个核心假设（比例效应 f=λg 和非差异错分类）在 NLP/LLM 场景下的实证支撑不足，制约了理论保证向实践的迁移。

**Confidence**: **4/5** — 熟悉因果推断和测量误差文献，仔细检查了 Theorem 1（Appendix A.4 perspective function convexity 论证）和 FWL 不变性证明（Appendix B.2 列空间论证）的结构。对 NLP 应用场景有足够了解做出判断。

---

**打分依据对照 EMNLP 2026 ARR 量表**:
- 3.5 = Borderline Conference：论文的理论新颖性和框架系统性接近主会议水准，但假设合理性论证的不足（N1, N2）和实用性差距（W2: logistic regression）使我无法给出 4.0（confident conference acceptance）。如果作者能在 camera-ready 或 rebuttal 中充分回应 N1（提供 NLP 场景下 f=λg 的实证检验）和 N2（至少一个按 Y 分层的 LLM 错分类检验），我会倾向将分数上调至 4.0。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1458 · 2026-05-23T15:31:23.852615+00:00_

Reviewer 1 审稿报告已收到。评分 3.5/5 (Borderline Conference)，两个 critical 问题：(1) 比例效应假设 f=λg 在 NLP 场景合理性不足，(2) 非差异错分类假设的 LLM 实证检验不足。等待 Reviewer 2 完成初审后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 145

## Round 145

2 recorded events


### User

_source line 1459 · 2026-05-23T15:31:35.189628+00:00_

[Reviewer 1 审稿结果]:
审稿完成。报告已提交至 Review Director，核心结论：

- **Overall 3.5/5（Borderline Conference）**
- **2 个 Must-Fix**：(N1) 比例效应假设 f=λg 在 NLP 场景下论证不足——Theorem 1 的核心保证依赖此假设但缺少具体 NLP 实证；(N2) 非差异错分类假设对 LLM 标注器的适用性需要更直接的实证检验（按 Y 分层的错分类率比较），而非仅靠 proxy-based 间接检验
- **4 个 Should-Fix**：Dirichlet 采样代表性(W1)、logistic regression 指导不足(W2)、significance ASV 的 N 依赖性(W3)、Conjecture 1 缺少理论直觉(W4)
- **条件上调**：如 rebuttal 充分回应 N1 和 N2，倾向上调至 4.0

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1460 · 2026-05-23T15:31:39.590559+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 146

## Round 146

8 recorded events


### User

_source line 1461 · 2026-05-23T15:31:41.094429+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 审稿报告：新颖性、完整性与呈现质量

### 论文信息
- **标题**: Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction
- **Venue**: EMNLP 2026 (ARR Long Paper)

---

## 总体评分

**Overall**: 3.5 (Borderline Conference)

**一句话总结**: 论文提出了一个重要且新颖的bias taxonomy和FWL invariance结果，但K≥3核心场景的理论基础不完整（仅为Conjecture），正文页数超限，且对NLP读者的可达性不足。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | K=2证明严谨，但核心K≥3场景的ASV monotonicity仅为数值验证+Conjecture；linear SEM假设限制适用范围 |
| Excitement | 3.5/5 | 问题重要且时机恰当（LLM标注×因果推断），FWL invariance结果令人惊讶，但对NLP社区的直接适用性因线性SEM假设而受限 |
| Reproducibility | 4/5 | 参数值明确，Monte Carlo设置详尽，使用标准数据集(HumAID/VAST/CivilComments)，承诺代码开源 |
| Confidence | 4/5 | 仔细检查了核心证明、实验设计和格式合规；measurement error文献较为熟悉 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] 正文页数超限

- 具体位置：PDF 第8-9页
- 问题：正文（Sections 1-5，不含Limitations和References）明确延伸至第9页。Section 4.5末尾约3-4行 + 完整的Section 5 Conclusion约10行位于第9页，总计约13-14行正文内容溢出。EMNLP 2026规则为"strict 8-page limit for main text"（Limitations和References不计入）。
- 为什么影响接收：ARR格式违规可能导致desk rejection。这不是边界情况——Sections 1-5约占8.2-8.3页。
- 建议修改方向：(1) 压缩Section 4.5 Correction Guidance——"Case studies and sensitivity"段落可大幅精简，部分细节（如ClinicalBERT验证、logistic regression robustness）已在Appendix有完整讨论；(2) 将Conclusion精简至5-6行；(3) 考虑将Figure 4或Figure 5之一移至Appendix。

**N2** [critical] K≥3场景的ASV monotonicity缺乏理论保证，削弱Contribution 2

- 具体位置：Section 3.3, Theorem 1 vs. Observation 1 vs. Conjecture 1
- 问题：ASV框架的核心理论基础——bias沿C(δ)插值路径的monotonicity——仅在K=2 + proportional effects条件下有形式化证明（Theorem 1）。对于K≥3（论文声称的核心新发现场景），monotonicity仅有数值证据（20,000 random triples per K, ε < 0.02 for non-exposure），被明确标记为Conjecture 1。论文在Conclusion中也承认"proving envelope monotonicity for general K"是primary open direction。

  这意味着论文第二个声称的贡献（ASV诊断工具）在其最重要的应用场景（K≥3多类别标注）中缺乏理论保证。论文的核心论点是K≥3引入了结构性新现象——但其自身框架恰恰无法为K≥3提供形式化保证。

- 为什么影响接收：Reviewer可以合理质疑："如果K≥3的monotonicity仅是conjecture，ASV vulnerability ranking在实践中有多可靠？" 虽然数值证据（ε < 0.02 for non-exposure, ε < 0.08 for exposure）是令人安心的，但不构成证明。对于一个以"引入ASV"为核心贡献的论文，这个理论缺口是本质性的。
- 建议修改方向：(a) 对K=3特定矩阵子类（如对角占优矩阵）证明monotonicity（降低普遍性要求但提供K>2的形式化结果）；(b) 更谨慎地重新表述Contribution 2——将ASV定位为"empirically validated diagnostic with proved K=2 foundation"而非暗示已有完整理论保证的framework；(c) 补充monotonicity failure的后果分析——如果某个K≥3场景中monotonicity确实失效，对ASV ranking的影响有多大？

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] Contribution 3（correction guidance）在正文中深度不足

- 具体位置：Section 4.5
- 问题："Topology-aware correction guidance"被列为三大贡献之一，但正文处理仅约0.7页散文描述。Algorithm 1（决策流程的形式化伪代码）仅出现在Appendix（appendix_proofs.tex第845行），未在正文中呈现。与Contribution 1（完整的bias derivations + Table 1 + Figure 2）和Contribution 2（Theorem 1 + Conjecture 1 + Remark 1 + Figure 3）相比，Contribution 3更像一个discussion section而非独立贡献。FWL invariance结果本身是有力的，但"guidance"部分的深度不匹配"贡献"的定位。
- 建议：(a) 将Algorithm 1提升至正文（需腾出空间，与N1的压缩联动）；(b) 或将Contribution 3重新表述为"practical implication"而非co-equal contribution。

**W2** [warning] 术语壁垒对NLP读者可达性不足

- 具体位置：Section 3.1 notation paragraph 及全文
- 问题：论文使用大量计量经济学/统计学术语，直觉解释不充分：
  - "plim"（probability limit）——Section 3.1有一句话解释+"脚注重复解释"，但首次出现在正文时没有铺垫其直觉含义
  - "FWL theorem"——仅在Section 3.1一句话解释，但其对correction failure的含义需要更直觉的阐述（"替换被误分类的变量不改变残差化关系"这句话对不熟悉FWL的NLP读者仍然晦涩）
  - "Wald estimator"——仅给出了公式，未解释为何IV场景需要使用它
  - "column-stochastic matrix"、"Birkhoff polytope"、"Dirichlet prior"——对NLP社区而言属于高门槛术语
  - "perspective function convexity"（证明中使用）——即使在appendix中也缺少直觉说明
  
  EMNLP的reviewer pool以NLP/ML背景为主。如果多数reviewer无法流畅理解method section，将影响soundness和confidence打分。
- 建议：在每个关键术语首次使用时增加1-2句直觉解释。例如：在plim前解释"我们关注系统性偏差（随样本量增大持续存在的误差），而非随机波动"；在FWL前用通俗语言解释其含义（"在回归中，一个变量的系数等价于先将其他变量的影响去除后再做简单回归——这意味着仅替换协变量不影响待估参数"）。

**W3** [warning] ASV与E-value的比较框架有误导性

- 具体位置：Section 3.3, Remark 1
- 问题：Remark 1列出三点"structural distinctions from E-values"，但这个比较本质上是不同工具解决不同问题：E-values针对unmeasured confounding（不可观测威胁），ASVs针对annotation error（可观测/可估计的威胁）。它们是互补工具而非竞争框架。当前表述暗示ASVs是E-values的改进版，但读者可以合理反驳："一个为annotation error设计的工具当然能捕捉annotation-specific效应，而一个为unmeasured confounding设计的工具不能——这不算'优势'。"ASV的真正贡献是将sensitivity analysis范式适配到annotation error + topology dependence，这本身就是新颖的，无需通过"beat E-values"来证明。
- 建议：重新框定ASVs为E-values的互补工具（不同威胁来源），而非替代品。Remark 1的(i)和(ii)可以重新表述为"ASVs address a threat that E-values are not designed for"而非暗示E-values有缺陷。

**W4** [warning] Figure 2灰度打印可辨识性

- 具体位置：Figure 2, 第6页
- 问题：图中使用红色标识sign reversal（关键区分信息）。在灰度打印下（审稿常见场景），红色和灰色直方图难以区分。Caption注明"Red = sign reversal"但未提供替代视觉标记。
- 建议：增加hatching/pattern fill来区分sign reversal区域，确保灰度下仍可辨识。

**W5** [warning] "First unified analysis" claim表述

- 具体位置：Introduction第3段
- 问题：原文声明"first unified analysis of LLM-generated multi-class annotation error propagation across seven canonical DAG topologies under structural equation models"——限定词过多（LLM-generated, multi-class, seven topologies, structural equation models），虽然每个限定都使声明准确，但密度过高反而削弱了impact。Carroll et al. (2006)已提供了measurement error in nonlinear models的一般框架；论文的真正新颖之处是topology-specific derivation + multi-class sign reversal analysis，而非一般性measurement error框架。
- 建议：改为更直接的表述，如"We provide the first systematic comparison of how the same confusion matrix produces qualitatively different bias across DAG topologies"。

---

## 小问题（不影响接收）

1. **τ 符号overloading**：τ在不同拓扑下含义不同（confounding=X系数, exposure=category-specific β_j, mediation=direct effect），Section 3.2有注明但容易混淆。建议在主文增加notation summary table或在每个拓扑段落开头明确声明"target parameter τ here denotes..."

2. **Abstract信息密度过高**：约184 words（符合≤200要求），但包含7+具体数字（83.4%, 2.1%, 0.45-0.81, 52.6%, K=2, K≥3等）。首次阅读难以消化。建议精简至最具冲击力的2-3个数字。

3. **Orphan bib entry**：`manski1990`（Manski 1990, "Nonparametric Bounds on Treatment Effects"）存在于references.bib中但似乎未在正文或appendix中引用。应移除或添加引用。

4. **引用格式不一致**：部分bib条目有`doi`字段，部分没有；部分会议论文缺少页码。这是minor polish问题。

5. **2026 arXiv preprints**：`variance_aware_llm2026`和`hidden_measurement_error2026`均已通过web search验证为真实存在的arXiv论文（分别为2601.02370和2604.11581），引用无问题。

---

## 引用完整性评估

论文引用覆盖全面，四个关键领域均有充分引用：

1. **Measurement error in causal inference（经典）**: Carroll (2006), Gustafson (2004), Buonaccorsi (2010), Bound (2001), Hernan & Cole (2009), Kuroki & Pearl (2014), Brenner (1993), Ogburn & VanderWeele (2012), Schennach (2020) — 完整。
2. **LLM annotation quality（近期）**: Gilardi (2023), Ziems (2024), Baumann (2025), Kim & Garg (2025), Pangakis (2023), Tan (2024), Cheng (2024), Messing (2026), Camuffo (2026) — 完整且前沿。
3. **Sensitivity analysis frameworks**: VanderWeele & Ding (2017), Cinelli & Hazlett (2020), Oster (2019), Ding & VanderWeele (2016) — 完整。
4. **Correction/debiasing methods**: PPI++ (Angelopoulos 2023), DSL (Egami 2023), Zrnic & Candes (2024), Cadei (2025), Gligoric (2025) — 完整。

潜在可补充引用（非必须）：Nguimkeu, Denteh & Tchernis (2019) "On the estimation of treatment effects with endogenous misreporting"——涉及treatment misclassification，与exposure topology分析相关。

---

## 主要优势

1. **真正的统一分析**：首次系统比较同一confusion matrix在七种DAG拓扑下产生定性不同的bias，填补了流行病学measurement error理论与NLP实践之间的缺口。sign-preservation/reversal二分法是一个清晰有力的主要发现。

2. **FWL invariance结果令人惊讶且实用**：证明matrix-based corrections对四种covariate拓扑的bias reduction为精确0%——这是一个重要的负面结果，直接警告practitioners不要使用主流correction范式（confusion matrix inversion）。

3. **全面且透明的实证验证**：161 scenarios × 23 LLM configurations × 3 NLP tasks (K=2,3,10)；100,000 Dirichlet matrices；theory-MC MAPE 1.6%。验证规模和agreement都很强。

4. **学术诚信**：Theorem/Observation/Conjecture的层级划分清晰诚实，不overclaim K≥3的理论结果。

5. **核心实用信息**：$F_1$与因果bias无显著相关性（Spearman ρ = -0.10, p = 0.45），拓扑而非标注质量决定下游风险——这对CSS研究者是一个直接可操作的警示。

---

## Questions to Authors

1. Theorem 1要求proportional effects ($f = \lambda g$)。Table 12显示empirical NLP tasks中这个假设的符合程度如何？如果常见NLP场景中proportional effects不成立，对ASV的实际可靠性有何影响？

2. 论文在Section 4.5提到PPI++在M-bias下harmful (-88%)。这个反直觉结果的直觉解释是什么？misclassification的"保护性衰减"是否在其他correction方法中也会被意外移除？

3. Sign-flip ASV的实际使用流程：practitioners需要先知道真实τ的符号才能计算sign-flip ASV，但如果他们已经知道τ的符号，sign flip的风险评估价值在哪里？论文如何处理这个bootstrap/先验知识的循环？

4. Non-differential misclassification假设的stress test（Appendix）显示ε=0.01 structured departure就导致14/16 K≥3 exposure configurations的sign reversal。这是否意味着论文的整个分析对differential misclassification极其脆弱？在LLM标注中，pre-training data encoding A-Y associations（论文自己提到的violation机制）是否是一个系统性而非偶发性的问题？

---

**Reviewer 2 审稿完成。**

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1462 · 2026-05-23T15:32:00.205618+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 1: Reviewer 独立初审（R1 方法严谨性 + R2 新颖性完整性）', 'status': 'completed', 'activeForm': '等待两位 Reviewer 完成独立初审'}, {'content': 'Step 2: 交叉分享——将每位 Reviewer 原文转发给对方，收集逐条回应', 'status': 'in_progress', 'activeForm': '执行交叉分享'}, {'content': 'Step 3: 收敛判断——分析共识与分歧', 'status': 'pending', 'activeForm': '判断是否收敛'}, {'content': 'Step 4: 汇总报告——合成审稿报告、同步 Issue Tracker、投递', 'status': 'pending', 'activeForm': '汇总并投递审稿报告'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Step 1: Reviewer 独立初审（R1 方法严谨性 + R2 新颖性完整性）', 'status': 'completed', 'activeForm': '等待两位 Reviewer 完成独立初审'}, {'content': 'Step 2: 交叉分享——将每位 Reviewer 原文转发给对方，收集逐条回应', 'status': 'in_progress', 'activeForm': '执行交叉分享'}, {'content': 'Step 3: 收敛判断——分析共识与分歧', 'status': 'pending', 'activeForm': '判断是否收敛'}, {'content': 'Step 4: 汇总报告——合成审稿报告、同步 Issue Tracker、投递', 'status': 'pending', 'activeForm': '汇总并投递审稿报告'}]"
  }
}
```

</details>

---


### Tool result

_source line 1463 · 2026-05-23T15:32:00.205973+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1464 · 2026-05-23T15:32:38.062456+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "以下是 Reviewer 2 的完整审稿意见。请逐条回应：对每个 Must-Fix、Should-Fix 和小问题，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure/Appendix）。\n\n---\n\n## Reviewer 2 的审稿报告\n\n**Overall**: 3.5 (Borderline Conference)\n\n### Must-Fix 问题\n\n**N1** [critical] 正文页数超限\n- PDF 第8-9页，正文（Sections 1-5）明确延伸至第9页。Section 4.5末尾约3-4行 + 完整的Section 5 Conclusion约10行位于第9页，总计约13-14行正文内容溢出。EMNLP 2026规则为\"strict 8-page limit for main text\"（Limitations和References不计入）。\n- 建议：压缩Section 4.5、精简Conclusion、或将Figure 4/5之一移至Appendix。\n\n**N2** [critical] K≥3场景的ASV monotonicity缺乏理论保证，削弱Contribution 2\n- ASV框架的核心理论基础（bias沿C(δ)插值路径的monotonicity）仅在K=2 + proportional effects条件下有形式化证明（Theorem 1）。K≥3仅有数值证据（ε < 0.02 for non-exposure），被明确标记为Conjecture 1。\n- 论文核心论点是K≥3引入了结构性新现象——但其自身框架恰恰无法为K≥3提供形式化保证。\n- 建议：(a) 对K=3对角占优矩阵子类证明monotonicity；(b) 更谨慎地重新表述Contribution 2；(c) 补充monotonicity failure的后果分析。\n\n### Should-Fix 问题\n\n**W1** [warning] Contribution 3（correction guidance）在正文中深度不足\n- \"Topology-aware correction guidance\"被列为三大贡献之一，但正文仅约0.7页。Algorithm 1仅在Appendix。与Contribution 1和2相比深度不足。\n- 建议：将Algorithm 1提升至正文，或将Contribution 3重新表述为\"practical implication\"。\n\n**W2** [warning] 术语壁垒对NLP读者可达性不足\n- plim、FWL theorem、Wald estimator、column-stochastic matrix、Birkhoff polytope、Dirichlet prior——对NLP社区属于高门槛术语，直觉解释不充分。\n- 建议：每个关键术语首次使用时增加1-2句直觉解释。\n\n**W3** [warning] ASV与E-value的比较框架有误导性\n- Remark 1的三点\"structural distinctions\"本质上是不同工具解决不同问题。当前表述暗示ASVs是E-values的改进版。ASV的真正贡献是将sensitivity analysis范式适配到annotation error + topology dependence。\n- 建议：重新框定为互补工具而非替代品。\n\n**W4** [warning] Figure 2灰度打印可辨识性\n- 红色标识sign reversal在灰度打印下难以区分。\n- 建议：增加hatching/pattern fill。\n\n**W5** [warning] \"First unified analysis\" claim表述\n- 限定词过多削弱impact。Carroll et al. (2006)已有一般measurement error框架；论文真正新颖处是topology-specific derivation + multi-class sign reversal analysis。\n- 建议：改为更直接的表述。\n\n### 小问题\n1. τ 符号overloading\n2. Abstract信息密度过高（约184 words符合要求，但7+数字难以消化）\n3. Orphan bib entry: `manski1990`\n4. 引用格式不一致（doi字段、页码缺失）\n5. 2026 arXiv preprints已验证存在\n\n### Missing References\nNguimkeu, Denteh & Tchernis (2019) \"On the estimation of treatment effects with endogenous misreporting\"\n\n---\n\n请对以上每个问题逐条回应 [AGREE] 或 [REBUT]。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "以下是 Reviewer 2 的完整审稿意见。请逐条回应：对每个 Must-Fix、Should-Fix 和小问题，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure/Appendix）。\n\n---\n\n## Reviewer 2 的审稿报告\n\n**Overall**: 3.5 (Borderline Conference)\n\n### Must-Fix 问题\n\n**N1** [critical] 正文页数超限\n- PDF 第8-9页，正文（Sections 1-5）明确延伸至第9页。Section 4.5末尾约3-4行 + 完整的Section 5 Conclusion约10行位于第9页，总计约13-14行正文内容溢出。EMNLP 2026规则为\"strict 8-page limit for main text\"（Limitations和References不计入）。\n- 建议：压缩Section 4.5、精简Conclusion、或将Figure 4/5之一移至Appendix。\n\n**N2** [critical] K≥3场景的ASV monotonicity缺乏理论保证，削弱Contribution 2\n- ASV框架的核心理论基础（bias沿C(δ)插值路径的monotonicity）仅在K=2 + proportional effects条件下有形式化证明（Theorem 1）。K≥3仅有数值证据（ε < 0.02 for non-exposure），被明确标记为Conjecture 1。\n- 论文核心论点是K≥3引入了结构性新现象——但其自身框架恰恰无法为K≥3提供形式化保证。\n- 建议：(a) 对K=3对角占优矩阵子类证明monotonicity；(b) 更谨慎地重新表述Contribution 2；(c) 补充monotonicity failure的后果分析。\n\n### Should-Fix 问题\n\n**W1** [warning] Contribution 3（correction guidance）在正文中深度不足\n- \"Topology-aware correction guidance\"被列为三大贡献之一，但正文仅约0.7页。Algorithm 1仅在Appendix。与Contribution 1和2相比深度不足。\n- 建议：将Algorithm 1提升至正文，或将Contribution 3重新表述为\"practical implication\"。\n\n**W2** [warning] 术语壁垒对NLP读者可达性不足\n- plim、FWL theorem、Wald estimator、column-stochastic matrix、Birkhoff polytope、Dirichlet prior——对NLP社区属于高门槛术语，直觉解释不充分。\n- 建议：每个关键术语首次使用时增加1-2句直觉解释。\n\n**W3** [warning] ASV与E-value的比较框架有误导性\n- Remark 1的三点\"structural distinctions\"本质上是不同工具解决不同问题。当前表述暗示ASVs是E-values的改进版。ASV的真正贡献是将sensitivity analysis范式适配到annotation error + topology dependence。\n- 建议：重新框定为互补工具而非替代品。\n\n**W4** [warning] Figure 2灰度打印可辨识性\n- 红色标识sign reversal在灰度打印下难以区分。\n- 建议：增加hatching/pattern fill。\n\n**W5** [warning] \"First unified analysis\" claim表述\n- 限定词过多削弱impact。Carroll et al. (2006)已有一般measurement error框架；论文真正新颖处是topology-specific derivation + multi-class sign reversal analysis。\n- 建议：改为更直接的表述。\n\n### 小问题\n1. τ 符号overloading\n2. Abstract信息密度过高（约184 words符合要求，但7+数字难以消化）\n3. Orphan bib entry: `manski1990`\n4. 引用格式不一致（doi字段、页码缺失）\n5. 2026 arXiv preprints已验证存在\n\n### Missing References\nNguimkeu, Denteh & Tchernis (2019) \"On the estimation of treatment effects with endogenous misreporting\"\n\n---\n\n请对以上每个问题逐条回应 [AGREE] 或 [REBUT]。"
  }
}
```

</details>

---


### Tool result

_source line 1465 · 2026-05-23T15:33:08.804844+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_9f117624057fcf6cb95db4d67f525246:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 30742
}
```

</details>

---


### Tool call

_source line 1466 · 2026-05-23T15:33:12.922342+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "以下是 Reviewer 1 的完整审稿意见。请逐条回应：对每个 Must-Fix、Should-Fix 和小问题，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure/Appendix）。\n\n---\n\n## Reviewer 1 的审稿报告\n\n**Overall**: 3.5 (Borderline Conference)\n\n### Must-Fix 问题\n\n**N1** [critical] 比例效应假设 (f=λg) 在 NLP 场景下的合理性论证严重不足\n- Theorem 1 的核心单调性保证要求 f(j)=λg(j)。在 NLP 因果推断中（如 stance detection），不同类别可能对结果有质性不同的效应，不满足比例关系。\n- Appendix B.13 显示 violation rate 从 exact proportional 的 0% 上升至 r=0.5 时 10.3%、r=0.1 时 22.1%。\n- 论文声称\"NLP-realistic DGP\"仅0.07% 违规率，但未充分论证参数代表性。\n- 建议：增加 2-3 个具体 NLP 因果推断场景的讨论，或提供 relaxed version 的理论结果。\n\n**N2** [critical] 非差异错分类假设在 LLM 标注器语境下需要更深入的实证检验\n- LLM 预训练数据编码了大量 A-Y 关联。Appendix B.5 VAST topic-stratified 检验仅一个数据集，且 topic 分层不等于按 Y 分层。Appendix B.6 stress test 未回答\"真实 LLM 标注的 ε 是多少\"。\n- 建议：在至少一个有 gold labels 的 NLP 数据集上，按 Y 值分层计算 LLM 错分类矩阵。\n\n### Should-Fix 问题\n\n**W1** [warning] Dirichlet(1,1,...,1) 采样对高维 K 的代表性不足\n- K=5 (20参数) 和 K=7 (42参数) 下，均匀 Dirichlet 采样可能无法覆盖实践相关的对角占优子空间。\n- 建议：补充 Dirichlet(α,1,...,1) (α>>1) 采样验证。\n\n**W2** [warning] Logistic regression 的处理不充分\n- NLP 最常用 logistic regression。主文仅一句话提及 FWL invariance 在 logistic 下的破缺。Algorithm 1 未区分 OLS/logistic 路径。\n- 建议：主文 Section 4.5 增加 1-2 段 logistic 指导；Algorithm 1 加 OLS/logistic 分支。\n\n**W3** [warning] Significance ASV 对样本量 N 的依赖缺乏充分探讨\n- δ_sig 通过 SE(N) 依赖于 N。Figure 3 只展示一个 N 值。\n- 建议：增加不同 N 下各拓扑 significance ASV 变化的 Figure。\n\n**W4** [warning] Conjecture 1 的 ε 约束缺乏理论解释\n- ε < 0.02 约束完全来自数值实验。论文没有解释为什么 ε 应该很小。\n- 建议：提供关于 ε 为何小的直觉论证。\n\n### 小问题\n- M1: \"plim\" 对 NLP 社区不常见，需脚注\n- M2: Figure 2 仅展示 K=3\n- M3: 附录24页交叉引用密集\n- M4: sign-flip ASV 定义中 sign(τ)·sign(f(I)) 项不清晰\n- M5: 主文页数可能略超8页（Section 5 Conclusion 起始于第9页顶部）\n\n### Missing References\n1. Imai and Yamamoto (2010), \"Causal Inference with Differential Measurement Error\"\n2. Ogburn and VanderWeele (2013), bias amplification under covariate misclassification\n\n### Questions\nQ1: ClinicalBERT case study 中是否检验了 f=λg？\nQ2: Conjecture 1 中 exposure 的 ε 变大条件？\nQ3: 2.7% 不满足 Theorem 1 条件的 LLM 配置特征？\nQ4: Logistic regression 下 FWL 破缺幅度对大 K 如何变化？\nQ5: 多维 ASV 的可能性？\n\n---\n\n请对以上每个问题逐条回应 [AGREE] 或 [REBUT]。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "以下是 Reviewer 1 的完整审稿意见。请逐条回应：对每个 Must-Fix、Should-Fix 和小问题，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure/Appendix）。\n\n---\n\n## Reviewer 1 的审稿报告\n\n**Overall**: 3.5 (Borderline Conference)\n\n### Must-Fix 问题\n\n**N1** [critical] 比例效应假设 (f=λg) 在 NLP 场景下的合理性论证严重不足\n- Theorem 1 的核心单调性保证要求 f(j)=λg(j)。在 NLP 因果推断中（如 stance detection），不同类别可能对结果有质性不同的效应，不满足比例关系。\n- Appendix B.13 显示 violation rate 从 exact proportional 的 0% 上升至 r=0.5 时 10.3%、r=0.1 时 22.1%。\n- 论文声称\"NLP-realistic DGP\"仅0.07% 违规率，但未充分论证参数代表性。\n- 建议：增加 2-3 个具体 NLP 因果推断场景的讨论，或提供 relaxed version 的理论结果。\n\n**N2** [critical] 非差异错分类假设在 LLM 标注器语境下需要更深入的实证检验\n- LLM 预训练数据编码了大量 A-Y 关联。Appendix B.5 VAST topic-stratified 检验仅一个数据集，且 topic 分层不等于按 Y 分层。Appendix B.6 stress test 未回答\"真实 LLM 标注的 ε 是多少\"。\n- 建议：在至少一个有 gold labels 的 NLP 数据集上，按 Y 值分层计算 LLM 错分类矩阵。\n\n### Should-Fix 问题\n\n**W1** [warning] Dirichlet(1,1,...,1) 采样对高维 K 的代表性不足\n- K=5 (20参数) 和 K=7 (42参数) 下，均匀 Dirichlet 采样可能无法覆盖实践相关的对角占优子空间。\n- 建议：补充 Dirichlet(α,1,...,1) (α>>1) 采样验证。\n\n**W2** [warning] Logistic regression 的处理不充分\n- NLP 最常用 logistic regression。主文仅一句话提及 FWL invariance 在 logistic 下的破缺。Algorithm 1 未区分 OLS/logistic 路径。\n- 建议：主文 Section 4.5 增加 1-2 段 logistic 指导；Algorithm 1 加 OLS/logistic 分支。\n\n**W3** [warning] Significance ASV 对样本量 N 的依赖缺乏充分探讨\n- δ_sig 通过 SE(N) 依赖于 N。Figure 3 只展示一个 N 值。\n- 建议：增加不同 N 下各拓扑 significance ASV 变化的 Figure。\n\n**W4** [warning] Conjecture 1 的 ε 约束缺乏理论解释\n- ε < 0.02 约束完全来自数值实验。论文没有解释为什么 ε 应该很小。\n- 建议：提供关于 ε 为何小的直觉论证。\n\n### 小问题\n- M1: \"plim\" 对 NLP 社区不常见，需脚注\n- M2: Figure 2 仅展示 K=3\n- M3: 附录24页交叉引用密集\n- M4: sign-flip ASV 定义中 sign(τ)·sign(f(I)) 项不清晰\n- M5: 主文页数可能略超8页（Section 5 Conclusion 起始于第9页顶部）\n\n### Missing References\n1. Imai and Yamamoto (2010), \"Causal Inference with Differential Measurement Error\"\n2. Ogburn and VanderWeele (2013), bias amplification under covariate misclassification\n\n### Questions\nQ1: ClinicalBERT case study 中是否检验了 f=λg？\nQ2: Conjecture 1 中 exposure 的 ε 变大条件？\nQ3: 2.7% 不满足 Theorem 1 条件的 LLM 配置特征？\nQ4: Logistic regression 下 FWL 破缺幅度对大 K 如何变化？\nQ5: 多维 ASV 的可能性？\n\n---\n\n请对以上每个问题逐条回应 [AGREE] 或 [REBUT]。"
  }
}
```

</details>

---


### Tool result

_source line 1467 · 2026-05-23T15:33:14.330946+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_9f117624057fcf6cb95db4d67f525246:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1408
}
```

</details>

---


### Assistant

_source line 1468 · 2026-05-23T15:33:20.543573+00:00_

交叉分享已派发。等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 147

## Round 147

2 recorded events


### User

_source line 1469 · 2026-05-23T15:33:23.157022+00:00_

[Reviewer 2 审稿结果]:
审稿报告已提交给 Review Director。

**核心发现摘要**：

- **Overall 3.5 (Borderline Conference)**
- **2个Must-Fix**：(1) 正文超8页限制约0.2-0.3页；(2) K≥3 ASV monotonicity仅为Conjecture，削弱第二个核心贡献的理论基础
- **5个Should-Fix**：Contribution 3正文深度不足（Algorithm 1仅在appendix）、NLP术语壁垒、ASV vs E-value比较框架misleading、Figure 2灰度可辨识性、"first unified analysis"声明措辞
- **主要优势**：bias taxonomy的统一分析真正新颖、FWL invariance负面结果令人惊讶且实用、实证验证全面透明（161 scenarios, 1.6% MAPE）、学术诚信（Theorem/Conjecture层级清晰）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1470 · 2026-05-23T15:33:30.302380+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 148

## Round 148

2 recorded events


### User

_source line 1471 · 2026-05-23T15:35:49.399755+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 对 Reviewer 2 审稿意见的逐条回应

---

## Must-Fix 问题

**[AGREE] R2-N1: 正文页数超限**

同意这是一个格式违规。我在 PDF 第 8-9 页确认：Section 4.5 "Correction Guidance" 的末尾内容延伸至第 8 页底部，而 Section 5 "Conclusion" 完整位于第 9 页顶部（约 10-12 行），随后是 Limitations 和 References。按 EMNLP 2026 "strict 8-page limit for main text"（Limitations 和 References 不计入），主文（Sections 1-5）确实溢出至第 9 页。

不过，我认为这应归为 **should-fix 而非 must-fix**。溢出量约 13-14 行（不到半栏），属于排版层面的问题，不涉及内容质量。R2 提出的压缩方案（精简 Section 4.5 或移 Figure 4 至 Appendix）均可行。这不应影响对论文学术贡献的评价。

**[AGREE with nuance] R2-N2: K≥3 ASV monotonicity 缺乏理论保证**

同意 R2 的核心观察：Theorem 1（envelope monotonicity）仅在 K=2 + proportional effects 下有形式化证明（Appendix A.4-A.5），K≥3 依赖 Observation 1（数值验证，ε < 0.02）和 Conjecture 1。ASV 框架的 δ-path 解释确实隐含依赖 monotonicity 来保证 ASV 值的唯一性和单调可比性。

但我认为 R2 **部分高估了**这个问题的严重程度，理由如下：

1. **论文的 K≥3 贡献不限于 monotonicity**。7 种拓扑的闭式偏差表达式（公式 (1)-(5)，Section 3.2）对一般 K 成立，不依赖 Theorem 1。Sign preservation 条件（Proposition 1, Proposition 3/5/6）对 confounding 和 collider 也有一般 K 的解析证明（Appendix A.3, A.6）。FWL 不变性对一般 K 成立（Appendix B.2）。

2. **论文的认知标注是诚实的**（我在自己的审稿中将此列为优势 S2）。Theorem → Observation → Conjecture 的三级层次明确区分了证明状态。Remark 1 直接声明 "analytic proofs for general K remain open"（Section 3.2, p.6）。

3. **ASV 在没有严格 monotonicity 的情况下仍然可用**。即使偏差函数不严格单调，C(δ) 路径上的 first crossing point（首次超过阈值的 δ 值）仍然给出了一个保守的脆弱性度量。ε < 0.02 的近似单调性意味着 ASV 值的误差在 2% 以内。

4. 但我同意 R2 的建议 (b)：Contribution 2 的表述应更谨慎，明确指出 K≥3 的 ASV 保证是 approximate 的，并在主文中加入 monotonicity failure 的后果讨论（而非仅在 Appendix B.12）。

**综合判断**：将 R2-N2 归类为 **strong should-fix** 而非 must-fix。论文的多类别贡献是多维的（偏差表达式 + sign preservation + FWL + ASV），不应仅以 monotonicity 的证明范围来评判。但 Contribution 2 的表述确需调整。

---

## Should-Fix 问题

**[AGREE] R2-W1: Contribution 3 (correction guidance) 在正文中深度不足**

同意。Section 4.5 "Correction Guidance"（p.8）约占 0.5-0.7 页，Algorithm 1 仅在 Appendix（p.32）。作为论文列出的三大贡献之一（p.2: "Topology-aware correction guidance"），这个深度与 Contribution 1（~3 页 method）和 Contribution 2（~1.5 页 ASV + experiments）不匹配。

R2 的两个建议都合理：(a) 将 Algorithm 1 提至正文（可能需要结合 N1 的页数压缩方案）；或 (b) 降级为 "practical implication" 而非独立贡献。我倾向 (b)——Algorithm 1 本质是对 Section 3-4 理论结果的操作化封装，作为 implication 更恰当。

**[AGREE] R2-W2: 术语壁垒**

同意。我在自己的审稿中也将 plim 符号标注为小问题（M1）。R2 将问题扩展到 FWL theorem、Wald estimator、column-stochastic matrix、Birkhoff polytope、Dirichlet prior，覆盖更全面。对于 EMNLP 受众（主要是 NLP/ML 研究者，非计量经济学或统计学背景），这些术语确实构成理解障碍。

每个术语增加 1-2 句直觉解释不会显著增加篇幅（约 6-8 行），在页数压缩后有空间容纳。

**[AGREE with nuance] R2-W3: ASV 与 E-value 的比较框架**

部分同意。查看 Remark 1（p.6），三点 "structural distinctions from E-values" 分别是：(i) Topology dependence（ASV 区分 confounding/exposure 等不同拓扑），(ii) Sign-flip diagnostic（sign-flip ASV 无 E-value 对应物），(iii) Parametric structure（ASV 搜索 K 维列随机矩阵空间而非标量）。

这三点 distinction 本身是准确的——E-values 确实不区分拓扑、不诊断 sign-flip、不在矩阵空间上操作。但 R2 的批评有道理：当前 "distinctions from" 的表述确实暗含 "improvements over" 的意味。ASV 和 E-values 解决的是不同问题（annotation error vs. unmeasured confounding），比较框架应强调 **互补性**（complementary tools for different sources of bias）而非差异化。

建议改 Remark 1 的开头从 "structural distinctions from E-values" 改为 "key design choices, informed by but distinct from the E-value paradigm" 或类似表述。

**[AGREE] R2-W4: Figure 2 灰度打印可辨识性**

同意。Figure 2（p.6）使用红色标注 sign reversal 区域。ACL/ARR 提交要求考虑灰度和色盲可访问性。增加 hatching 或 pattern fill 是标准做法，改动成本低。

**[REBUT] R2-W5: "First unified analysis" claim 表述**

不完全同意 R2 的判断。查看原文（p.2）：论文声称 "the first unified analysis of LLM-generated multi-class annotation error propagation across seven canonical DAG topologies under structural equation models"。

R2 指出 Carroll et al. (2006) 已有一般 measurement error 框架。但 Carroll et al. 是一部关于 measurement error 的 **教科书**（Chapman & Hall/CRC），覆盖连续变量测量误差、回归校准等广泛主题，并未做过 **拓扑特异性的多类别标注误差偏差推导**。论文的新颖之处恰恰是：

1. **拓扑特异性**：7 种 DAG 拓扑下的偏差表达式各不相同（公式 (1)-(5)），这不是 Carroll et al. 的通用框架能直接给出的；
2. **多类别 sign reversal**：K≥3 的 sign reversal 现象（Section 3.2, 83.4% exposure matrices）是本文首次系统刻画的；
3. **LLM 标注器语境**：将混淆矩阵与 LLM confusion matrix 对接，是之前未有的。

但 R2 建议 "改为更直接的表述" 有一定道理——限定词确实较多。建议将 "first unified" 改为更具体的表述，如 "a systematic topology-specific analysis of..."，既准确又减少争议。

---

## 小问题

**[AGREE] R2-Minor-1: τ 符号 overloading** — 需要检查 τ 是否在不同上下文中有不同含义。如果同时指代 treatment effect 和 other quantities，应使用不同符号。

**[AGREE] R2-Minor-2: Abstract 信息密度** — Abstract 约 184 words，符合 200-word 限制，但确实包含大量数字。考虑减少具体数值（如 "83.4%", "1.6% MAPE", "100,000 matrices"），改用定性描述。

**[AGREE] R2-Minor-3: Orphan bib entry manski1990** — 如果确实未在正文中引用，应删除。

**[AGREE] R2-Minor-4: 引用格式不一致** — 应统一 doi 字段和页码格式。

**[AGREE] R2-Minor-5: 2026 arXiv preprints** — R2 确认已验证存在，无异议。

---

## Missing References

**[AGREE] Nguimkeu, Denteh & Tchernis (2019)** — "On the estimation of treatment effects with endogenous misreporting" 讨论内生性错报下的处理效应估计，与本文的非差异错分类假设形成有用对比。建议在 Related Work（Section 2）或 Limitations 中引用，讨论当 LLM 标注误差不满足非差异性时的理论后果。这也与我自己的 N2（非差异错分类假设的实证支撑不足）呼应。

---

## 与我自己审稿意见的交叉对照

| R2 问题 | R1 对应 | 一致性 |
|--------|--------|--------|
| R2-N1 (页数超限) | R1-M5 (minor) | 同一问题，R2 严重性判断更高；我认为 should-fix 更恰当 |
| R2-N2 (K≥3 monotonicity) | R1-S2/N1 (部分重叠) | R2 聚焦 monotonicity 证明缺口，R1 聚焦 proportional effects 假设；两个问题相关但角度不同 |
| R2-W1 (Contribution 3 深度) | R1 未专门提及 | R2 发现了一个我遗漏的有效问题 |
| R2-W2 (术语壁垒) | R1-M1 (plim) | R2 更全面地覆盖了术语问题 |
| R2-W3 (ASV vs E-value) | R1 未提及 | R2 的观察有价值 |
| R2-W4 (Figure 2 灰度) | R1 未提及 | 有效的可访问性问题 |
| R2-W5 ("first unified") | R1 未提及 | 部分不同意，见 REBUT |

**总体**：R2 的审稿侧重展示质量和受众可达性，与我的方法严谨性审查形成互补。两份审稿的 Overall 评分一致（均为 3.5/5 Borderline Conference），核心分歧在于严重性判断——R2 将格式违规（N1）升为 must-fix，我认为 should-fix 更恰当。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1472 · 2026-05-23T15:35:56.851690+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 149

## Round 149

2 recorded events


### User

_source line 1473 · 2026-05-23T15:36:04.663659+00:00_

[Reviewer 1 审稿结果]:
对 Reviewer 2 的逐条回应已提交。核心判断：

- **N1 (页数超限)**：同意违规存在，但建议降级为 should-fix（排版问题，易修复）
- **N2 (K≥3 monotonicity)**：同意需调整 Contribution 2 表述，但指出论文的 K≥3 贡献不仅限于 monotonicity（偏差表达式、sign preservation、FWL 均对一般 K 成立）
- **W1-W4**：均同意
- **W5 ("first unified")**：部分反驳——Carroll et al. (2006) 是通用测量误差教科书，未做拓扑特异性的多类别偏差推导，论文的 claim 有合理基础，但建议改用更直接的表述

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1474 · 2026-05-23T15:36:09.554867+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 150

## Round 150

14 recorded events


### User

_source line 1475 · 2026-05-23T15:37:09.513452+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 对 Reviewer 1 审稿意见的逐条回应

---

### Must-Fix 问题

**[REBUT] R1-N1: 比例效应假设 (f=λg) 在 NLP 场景下的合理性论证严重不足**

R1 将此问题定为 critical 我认为严重性评估过高，应降级为 should-fix。原因：

1. **假设的作用范围比 R1 描述的更窄。** Proportional effects 仅是 Theorem 1（K=2 monotonicity）和 Proposition 2（confounding proportional case）的条件。论文的核心贡献——bias taxonomy（Contribution 1）和 sign preservation/reversal 二分法——**不依赖此假设**。Proposition 3（Appendix A.3, line 176-212）提供了 general case 的 sign preservation bound（|τ| > B̄），完全不需要 f=λg。Mediation sign preservation（Appendix A.5, Numerical Verification）的条件是 sign(τ_dir) = sign(τ_total)，同样不需要 proportional effects。

2. **论文已提供实质性缓解措施，R1 未充分考虑。** Section 3.3 明确指出：(a) 假设可测试（"testable by regressing f(A) on g(A)"）；(b) 在 NLP-realistic DGP 下 out-of-bound rate 为 0.07%（零 sign failure）；(c) 即使在 non-proportional effects 下，23 个真实 LLM 矩阵的 sign preservation ≥ 97.3%（Tables 11, 12）。这些数据说明，即使 f≠λg，ASV 的 vulnerability ranking 仍然 robust。

3. **但 R1 关于 NLP 场景讨论不足的观点有道理。** 论文仅一句话提及"plausible in NLP tasks with a single quality dimension but weakens under heterogeneous quality"，确实缺乏具体 NLP 因果推断场景的分析。这更适合作为 should-fix：增加 2-3 句具体场景讨论（如 stance detection 的 3-class 是否接近 proportional）即可，不需要新的理论结果。

**结论：严重性应从 critical 降至 should-fix。假设的范围、现有缓解措施和 Proposition 3 的 fallback 使其不影响接收决定。但确实应补充 NLP 场景讨论。**

---

**[AGREE] R1-N2: 非差异错分类假设在 LLM 标注器语境下需要更深入的实证检验**

同意这是 critical 问题，与我的 Question 4 一致。具体评估：

1. **R1 对现有验证的批评是准确的。** Appendix B.5 的 VAST topic-stratified 检验存在两个已被论文自身承认的局限（Section B.5 倒数第二段："topic is not the actual outcome Y, and small per-topic samples reduce statistical power"）。但更关键的是 Appendix B.8（Realistic Epsilon Thresholds, Table）的发现：**14/16 K≥3 配置在 ε=0.01 时就产生 sign reversal**（ε*_safe = 0），表明非差异假设对 multi-class exposure 是 load-bearing 的。

2. **但论文的结构性论证（structural argument）比 R1 承认的更强。** Appendix B.5 首段明确指出：non-differential 假设"holds by design in standard LLM annotation pipelines: the model receives only source text as input and classifies without observing the outcome Y or covariates Z." 这不是统计检验，而是因果论证——如果 LLM API call 的输入不包含 Y，则 A* ⊥ Y | A 是结构性保证的。R1 的担忧（预训练数据编码 A-Y 关联）是合理的，但这是间接路径——通过文本内容中的 A-Y 相关性，不是直接观测 Y。

3. **R1 的建议（Y-stratified CM on gold dataset）可操作性强且有价值。** 论文应在至少一个数据集上做 Y-stratified 检验。即使只做一个数据集（如 HumAID），也能为结构性论证提供 empirical backing。这确实是 critical 级别的改进——如果实际 LLM 标注中 ε > 0.01（而 Appendix B.8 显示 ε*_safe ≈ 0 for K≥3），整个 exposure topology 的 sign preservation 讨论就需要重新 caveat。

---

### Should-Fix 问题

**[AGREE] R1-W1: Dirichlet(1,1,...,1) 采样对高维 K 的代表性不足**

同意。但需要补充一点 R1 可能忽略的上下文：论文在 Section 4.4 Empirical Validation 中**分离了 Dirichlet 采样和经验 LLM 矩阵的结果**。Table 1 的主要发现（sign-flip 二分法、vulnerability ranking）在 23 个真实 LLM 配置下**完全被复现**（Section 4.4："All 23 empirical LLM configurations show zero IV sign reversal"；"14/23 exposure configurations exhibit sign reversal—all secondary"）。所以 Dirichlet 采样的代表性问题不影响论文核心结论的稳健性。R1 建议的 Dirichlet(α,1,...,1) 补充实验是合理的 due diligence，但即使不做，现有经验矩阵验证已经足够支撑结论。

**[AGREE] R1-W2: Logistic regression 的处理不充分**

强烈同意，与我的 W2 一致。Appendix B.7（Table, line 1013-1035）显示 logistic regression 下所有拓扑的 SF_τ 偏差 < 0.02，结构性结论不变。但 Appendix B.14（Table, line 1168-1195）进一步显示 FWL invariance 在 logistic 下的**破缺幅度随 accuracy 增大**（exposure: -22% to -78%）。这个信息对 NLP 实践者很重要，应该出现在主文 Section 4.5 而非仅在附录。Algorithm 1 确实应增加 OLS/logistic 分支。

**[AGREE] R1-W3: Significance ASV 对样本量 N 的依赖缺乏充分探讨**

同意。Section 3.3 提及 "sharp phase transition at a critical N* below which all rejections are blocked" 但 Figure 3 仅展示单一 N 值。对于实际使用 ASV 的 practitioners，不同 N 下 significance ASV 的变化是关键决策信息。建议增加一个 Figure 或 Table 展示 N ∈ {1K, 5K, 10K, 50K} 下各拓扑的 δ*_sig 变化。

**[AGREE] R1-W4: Conjecture 1 的 ε 约束缺乏理论解释**

同意，与我的 N2 assessment 一致。论文给出 ε < 0.02（non-exposure, |β| ≤ 1）和 ε < 0.08（exposure）的数值结果，但没有解释**为什么 ε 应该小**。一个可能的直觉论证路径：在 proportional effects 下 monotonicity 是精确的（Theorem 1, K=2），deviations 来自 f 和 g 的非比例分量（non-proportional residual）。如果 NLP 场景中 f 和 g 的相关性高（单一质量维度），则 non-proportional residual 小，ε 自然小。这个论证在论文中缺失。

---

### 小问题

**[AGREE] R1-M1**: plim 对 NLP 社区不常见——同意，与我的 W2 一致。论文在 Section 3.2 脚注 5 有一句话解释，但应在 Section 3.1 首次出现时就给出直觉说明。

**[REBUT] R1-M2**: Figure 2 仅展示 K=3——论文在 Section 4.2 明确声明"All patterns persist at K=5,7 (Appendix B.9)"，cross-K robustness 在 Appendix B.9 有完整结果。Figure 2 展示 K=3 作为代表性案例是合理的空间选择。如果要改进，可在 Figure 2 caption 中注明"K=5,7 results in Appendix B.9"。

**[AGREE] R1-M3**: 附录 24 页交叉引用密集——同意但这是 appendix 信息量大的必然结果，不是结构问题。

**[REBUT] R1-M4**: sign-flip ASV 定义中 sign(τ)·sign(f(I)) 不清晰——查看 Section 3.3 原文（method.tex line 88），sign-flip ASV 的定义是 δ*_sf = min{δ : sign(τ̂) ≠ sign(τ)}，不涉及 sign(τ)·sign(f(I)) 项。R1 可能引用的是 Appendix 中 mediation 或 confounding 的 specific sign condition（如 Proposition 1(a) 的 sign(τ) = sign(τ + B_OV)），而非 ASV 定义本身。如果 R1 指的是 Appendix 中的某个表达式，需要给出具体位置。

**[AGREE] R1-M5**: 主文页数略超 8 页——**强烈同意**。我在自己的审稿中将此定为 N1 critical。Section 5 Conclusion 明确起始于第 9 页。这不是 "可能" 超限——PDF 第 9 页上有约 13-14 行主文内容（Section 4.5 尾部 + 完整 Section 5），是一个明确的格式违规。建议将 M5 严重性从"小问题"提升至 Must-Fix。

---

### Missing References

**[AGREE] Imai and Yamamoto (2010), "Causal Inference with Differential Measurement Error"**——论文讨论了 non-differential 假设的脆弱性（Appendix B.8 显示 ε*_safe ≈ 0 for K≥3），引用这篇关于 differential measurement error 的方法论工作可以丰富 Limitations 讨论和 Related Work 的 completeness。但这不是一个严重遗漏——论文已经引用了 Edwards, Lessler & Naimi (2021) 关于 dependent misclassification 的工作。

**[REBUT] Ogburn and VanderWeele (2013), bias amplification under covariate misclassification**——论文已引用 Ogburn & VanderWeele (2012)（references.bib line 249-258），该论文专门讨论 "Nondifferential Misclassification of a Binary Confounder"。R1 所指的 2013 年论文需要确认具体引用——如果是指同一系列工作，则已被覆盖。

---

### Questions（供 Director 参考的评论）

R1 提出的 5 个问题质量很高，尤其是：

- **Q1（ClinicalBERT case study 中是否检验 f=λg）**: 这是一个直接可验证的问题，作者应在 revision 中明确回答。

- **Q3（2.7% 不满足 Theorem 1 条件的 LLM 配置特征）**: 这个 2.7% 来自 Section 3.3 的"sign preservation remains ≥97.3%"。了解这 2.7% failure 的特征（哪些 LLM、哪些 task、哪些 confusion matrix 结构）对实际 practitioners 有价值。

- **Q5（多维 ASV 的可能性）**: 这是一个有前瞻性的研究方向问题。当前 ASV 通过 C(δ) 将 K² 维降至 1 维，但实际中不同 off-diagonal 元素的重要性不同。多维 ASV（如 per-category sensitivity）可能是有价值的 future work。

---

### 综合评估

R1 的审稿整体质量高，发现的问题大多有充分依据。主要分歧：

1. **N1 严重性**：我认为应降至 should-fix。Proportional effects 的作用范围比 R1 描述的更窄（仅影响 Theorem 1 monotonicity，不影响 bias taxonomy 或 sign preservation），且现有 fallback（Proposition 3, 97.3% preservation）实质性地缓解了这个问题。

2. **M5 严重性**：我认为应升至 must-fix。页数超限是一个客观格式违规，不是边界情况。

3. **Figure 2 (M2)**：R1 的"仅 K=3"批评忽略了 Appendix B.9 的 cross-K 验证和主文的明确 cross-reference。

其余问题我与 R1 的评估基本一致。

**Reviewer 2 交叉回应完成。**

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1476 · 2026-05-23T15:38:08.178357+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 1: Reviewer 独立初审（R1 方法严谨性 + R2 新颖性完整性）', 'status': 'completed', 'activeForm': '等待两位 Reviewer 完成独立初审'}, {'content': 'Step 2: 交叉分享——将每位 Reviewer 原文转发给对方，收集逐条回应', 'status': 'completed', 'activeForm': '执行交叉分享'}, {'content': 'Step 3: 收敛判断——分析共识与分歧', 'status': 'in_progress', 'activeForm': '判断是否收敛'}, {'content': 'Step 4: 汇总报告——合成审稿报告、同步 Issue Tracker、投递', 'status': 'pending', 'activeForm': '汇总并投递审稿报告'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Step 1: Reviewer 独立初审（R1 方法严谨性 + R2 新颖性完整性）', 'status': 'completed', 'activeForm': '等待两位 Reviewer 完成独立初审'}, {'content': 'Step 2: 交叉分享——将每位 Reviewer 原文转发给对方，收集逐条回应', 'status': 'completed', 'activeForm': '执行交叉分享'}, {'content': 'Step 3: 收敛判断——分析共识与分歧', 'status': 'in_progress', 'activeForm': '判断是否收敛'}, {'content': 'Step 4: 汇总报告——合成审稿报告、同步 Issue Tracker、投递', 'status': 'pending', 'activeForm': '汇总并投递审稿报告'}]"
  }
}
```

</details>

---


### Tool result

_source line 1477 · 2026-05-23T15:38:08.279426+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "TodoWrite",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 1478 · 2026-05-23T15:38:22.096979+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 1: Reviewer 独立初审（R1 方法严谨性 + R2 新颖性完整性）', 'status': 'completed', 'activeForm': '等待两位 Reviewer 完成独立初审'}, {'content': 'Step 2: 交叉分享——将每位 Reviewer 原文转发给对方，收集逐条回应', 'status': 'completed', 'activeForm': '执行交叉分享'}, {'content': 'Step 3: 收敛判断——分析共识与分歧', 'status': 'completed', 'activeForm': '判断是否收敛'}, {'content': 'Step 4: 汇总报告——合成审稿报告、同步 Issue Tracker、投递', 'status': 'in_progress', 'activeForm': '汇总并投递审稿报告'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Step 1: Reviewer 独立初审（R1 方法严谨性 + R2 新颖性完整性）', 'status': 'completed', 'activeForm': '等待两位 Reviewer 完成独立初审'}, {'content': 'Step 2: 交叉分享——将每位 Reviewer 原文转发给对方，收集逐条回应', 'status': 'completed', 'activeForm': '执行交叉分享'}, {'content': 'Step 3: 收敛判断——分析共识与分歧', 'status': 'completed', 'activeForm': '判断是否收敛'}, {'content': 'Step 4: 汇总报告——合成审稿报告、同步 Issue Tracker、投递', 'status': 'in_progress', 'activeForm': '汇总并投递审稿报告'}]"
  }
}
```

</details>

---


### Tool result

_source line 1479 · 2026-05-23T15:38:22.097464+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1480 · 2026-05-23T15:38:29.079494+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "causal_annot_error_attrib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "causal_annot_error_attrib"
  }
}
```

</details>

---


### Tool result

_source line 1481 · 2026-05-23T15:38:29.131333+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-23T15:20:49.587050+00:00\", \"completed_at\": \"2026-05-23T15:20:52.466988+00:00\", \"findings\": [{\"severity\": \"info\", \"dimension\": \"agent_error\", \"message\": \"[ERROR] Agent exited 1: You've hit your limit · resets 4pm (UTC)\"}], \"counts\": {\"critical\": 0, \"warning\": 0, \"info\": 1}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1482 · 2026-05-23T15:41:50.964219+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "causal_annot_error_attrib",
  "issues_yaml": "issues:\n  # === Round 1-7 历史 (resolved，保留摘要) ===\n\n  - id: R1-N1\n    category: soundness\n    severity: must-fix\n    summary: \"Theorem 1 适用范围过窄（仅 confounding+proportional effects），K≥3 证明不完整\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 7\n    resolution: \"Theorem 1 现正确限定为 K=2；K≥3 由 Observation 1 和 Conjecture 1 覆盖。\"\n    resolution_round: 7\n\n  - id: R1-N2\n    category: soundness\n    severity: should-fix\n    summary: \"3/5 安全拓扑的符号保持仅有数值验证，Abstract 用 'establish' 暗示已证明\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 3\n    resolution: \"Abstract 已准确区分 prove/verify。\"\n    resolution_round: 4\n\n  - id: R1-N3\n    category: soundness\n    severity: must-fix\n    summary: \"ASV C(δ) 定义域错误\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Section 3.3 已引入 δ_max 约束。\"\n    resolution_round: 2\n\n  - id: R2-N1\n    category: presentation\n    severity: must-fix\n    summary: \"83.4% sign reversal headline framing 过度声称\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    resolution: \"Introduction 已重写。\"\n    resolution_round: 5\n\n  - id: R2-N2\n    category: novelty\n    severity: should-fix\n    summary: \"'first systematic framework' 过度声明\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"已修复。\"\n    resolution_round: 2\n\n  - id: R2-N3\n    category: related_work\n    severity: must-fix\n    summary: \"4 篇关键相关工作未引用\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"已修复。\"\n    resolution_round: 2\n\n  - id: R1-W2\n    category: clarity\n    severity: should-fix\n    summary: \"Sign preservation 的 DGP 条件在实践中难以事前验证\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"Section 3.2 已添加 ASV 替代讨论。\"\n    resolution_round: 3\n\n  - id: R1-W3\n    category: experiments\n    severity: should-fix\n    summary: \"实证验证不完整：缺少商业 LLM\"\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 18\n    mentions:\n      - round: 7\n        reviewers: [R2]\n        note: \"Limitations 中讨论即可。\"\n      - round: 14\n        reviewers: [R1, R2]\n        note: \"R14 共识：minor。\"\n      - round: 15\n        reviewers: [R1, R2]\n        note: \"R15 共识：should-fix（低优先级），Limitations 已覆盖。\"\n      - round: 16\n        reviewers: [R1, R2]\n        note: \"R16 R1-M2 再提为 minor。\"\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"R17 共识 should-fix（低优先级）。\"\n      - round: 18\n        reviewers: [R1]\n        note: \"R18 R1-W1 再提 Dirichlet 采样代表性（高 K 覆盖率不足），R2 交叉 AGREE 但指出 23 个经验 LLM 矩阵已验证核心结论。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R2-W2\n    category: presentation\n    severity: should-fix\n    summary: \"98 场景 zero sign reversals 与 sign reversal narrative 的 tension\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"已解决。\"\n    resolution_round: 2\n\n  - id: R2-W3\n    category: method\n    severity: should-fix\n    summary: \"ASV 对 C₀ 估计不确定性的敏感性\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"Bootstrap ASV 分析已完成。\"\n    resolution_round: 3\n\n  - id: R2-W4\n    category: scope\n    severity: should-fix\n    summary: \"线性 SEM 假设限制；Algorithm 1 缺 linear-only caveat\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    resolution: \"Section 4.5 FWL 段加 'Under linear OLS' 限定。\"\n    resolution_round: 5\n\n  - id: R1-W4\n    category: experiments\n    severity: should-fix\n    summary: \"MC MAPE 报告不充分\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"已修复。\"\n    resolution_round: 2\n\n  - id: MISC-1\n    category: presentation\n    severity: minor\n    summary: \"符号不统一（τ vs β_T）、Proposition 编号不一致\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    resolution: \"method.tex 添加 τ 在各拓扑下含义的明确说明。\"\n    resolution_round: 5\n\n  - id: NEW-1\n    category: soundness\n    severity: should-fix\n    summary: \"Non-differential misclassification 假设讨论不足\"\n    status: in_progress\n    first_raised_round: 2\n    last_seen_round: 18\n    mentions:\n      - round: 14\n        reviewers: [R1, R2]\n        note: \"R14 共识 minor。\"\n      - round: 15\n        reviewers: [R1, R2]\n        note: \"R15 共识 should-fix。\"\n      - round: 16\n        reviewers: [R1, R2]\n        note: \"R16 R1-W1 + R2-Q2 再提。\"\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"R17 共识 should-fix。\"\n      - round: 18\n        reviewers: [R1, R2]\n        note: \"R18 升级为 must-fix。R1 指出 VAST topic-stratified 检验不等于 Y-stratified 检验，stress test 未回答真实 ε 是多少。R2 交叉 AGREE 但补充结构性论证（LLM API 不观测 Y）比 R1 承认的更强。共识：按 Y 分层验证是 critical 改进。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: NEW-2\n    category: related_work\n    severity: should-fix\n    summary: \"缺少 Feder et al. (2022) 和 Cheng et al. (2024)\"\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 5\n    resolution: \"已引用。\"\n    resolution_round: 5\n\n  - id: NEW-3\n    category: soundness\n    severity: should-fix\n    summary: \"Conjecture 1 数值验证规模\"\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"210,000 matrices + adversarial + analytic plim。\"\n    resolution_round: 3\n\n  - id: R3-NEW-1\n    category: format\n    severity: must-fix\n    summary: \"正文超出 EMNLP 2026 Long Paper 8 页限制\"\n    status: open\n    first_raised_round: 3\n    last_seen_round: 18\n    mentions:\n      - round: 12\n        reviewers: [R1, R2]\n        note: \"R12 再提。\"\n      - round: 13\n        reviewers: []\n        note: \"已修复，Conclusion 已压缩。\"\n      - round: 18\n        reviewers: [R1, R2]\n        note: \"R18 复发。R2 确认 Section 5 Conclusion 完整位于第 9 页（约 13-14 行主文溢出）。R1 交叉 AGREE 违规存在但建议降级为 should-fix。Director 采纳 must-fix：EMNLP strict 8-page limit 是硬约束。\"\n    resolution: \"R13 曾解决但 R18 复发。\"\n    resolution_round: null\n\n  - id: R3-NEW-2\n    category: soundness\n    severity: should-fix\n    summary: \"FWL invariance 结论缺乏 precise statement 和推导\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"FWL 证明完整。\"\n    resolution_round: 5\n\n  - id: R3-NEW-3\n    category: scope\n    severity: should-fix\n    summary: \"缺少 outcome misclassification 讨论\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"Limitations 已添加。\"\n    resolution_round: 4\n\n  - id: R3-NEW-4\n    category: presentation\n    severity: should-fix\n    summary: \"Abstract/Introduction 信息过载（数字密度）\"\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 18\n    mentions:\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"R17 与 R17-N1 联合。\"\n      - round: 18\n        reviewers: [R2]\n        note: \"R18 R2-minor-2 再提：Abstract 约 184 words 符合限制，但 7+ 具体数字难以首次阅读消化。R1 交叉 AGREE。共识 minor。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R3-NEW-5\n    category: related_work\n    severity: should-fix\n    summary: \"缺少 5 篇相关引用（Round 3 要求的）\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 3\n    resolution: \"全部 5 篇已引用。\"\n    resolution_round: 4\n\n  - id: R3-NEW-6\n    category: reproducibility\n    severity: should-fix\n    summary: \"未承诺代码/数据公开\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"Conclusion 已添加代码公开承诺。\"\n    resolution_round: 4\n\n  - id: R3-NEW-7\n    category: novelty\n    severity: should-fix\n    summary: \"新颖性定位不清：未明确界定已知结果 vs 新贡献\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"确认'首次跨 7 种拓扑系统比较'成立。\"\n    resolution_round: 5\n\n  - id: R3-NEW-8\n    category: experiments\n    severity: should-fix\n    summary: \"经验验证使用模拟 DGP 而非真实因果数据\"\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 18\n    mentions:\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"R17 should-fix（高优先级）。\"\n      - round: 18\n        reviewers: []\n        note: \"R18 未单独提出，但 R1-N2 间接覆盖（要求实证验证 non-differential 假设需要 gold-label 数据集）。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R4-W6\n    category: novelty\n    severity: should-fix\n    summary: \"ASV 方法论创新有限——E-value 直接移植质疑\"\n    status: in_progress\n    first_raised_round: 4\n    last_seen_round: 18\n    mentions:\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"R17 共识 should-fix。\"\n      - round: 18\n        reviewers: [R2]\n        note: \"R18 R2-W3 再提：Remark 1 三点对比框架有误导性，暗示 ASV 是 E-value 的改进版而非互补工具。R1 交叉 AGREE with nuance：distinctions 准确但表述暗含 'improvements over'。共识：重新框定为互补工具。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R4-W7\n    category: presentation\n    severity: should-fix\n    summary: \"论文广度有余深度不足\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 7\n    resolution: \"Appendix pointer 已添加。\"\n    resolution_round: 8\n\n  - id: R4-W8\n    category: scope\n    severity: should-fix\n    summary: \"DAG 拓扑必须先验已知——Algorithm 1 依赖正确拓扑输入\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    resolution: \"Limitations 已添加相关讨论。\"\n    resolution_round: 5\n\n  - id: R4-W10\n    category: method\n    severity: minor\n    summary: \"PPI++ 对 M-bias 有害 (-88%) 缺乏机制解释\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 15\n    resolution: \"Section 4.5 已包含完整机制解释。\"\n    resolution_round: 15\n\n  - id: R4-W12\n    category: presentation\n    severity: minor\n    summary: \"引用格式问题\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 7\n    resolution: \"格式合规检查通过。\"\n    resolution_round: 8\n\n  - id: R5-N1\n    category: presentation\n    severity: must-fix\n    summary: \"Table 1 的 sign-flip guarantee ✓ 掩盖了 DGP 条件性\"\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"Table 1 已实现三级符号 ✓/✓*/✗。\"\n    resolution_round: 5\n\n  - id: R5-N2\n    category: soundness\n    severity: should-fix\n    summary: \"Conjecture 1 的 ε 在极端条件下可达 0.14-0.15\"\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"Conjecture 1 rewritten with per-topology ε bounds。\"\n    resolution_round: 5\n\n  - id: R5-N3\n    category: presentation\n    severity: must-fix\n    summary: \"'Primary coefficient never reverses' 仅为经验发现，缺乏理论保证\"\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 11\n    resolution: \"Abstract 已改为经验事实描述。\"\n    resolution_round: 11\n\n  - id: R5-MR\n    category: related_work\n    severity: should-fix\n    summary: \"Round 5 新发现的缺失引用\"\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"三篇引用已添加。\"\n    resolution_round: 5\n\n  - id: R6-M1\n    category: soundness\n    severity: should-fix\n    summary: \"Theorem 1 对 K≥3 未证明但标记为 Theorem\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: \"Theorem 1 现正确限定为 K=2。\"\n    resolution_round: 7\n\n  - id: R6-M3\n    category: soundness\n    severity: should-fix\n    summary: \"Proportional effects 假设 (f=λg) 在 NLP 中是强限制\"\n    status: in_progress\n    first_raised_round: 6\n    last_seen_round: 18\n    mentions:\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"R17 共识 should-fix。\"\n      - round: 18\n        reviewers: [R1, R2]\n        note: \"R18 R1 列为 critical（NLP 场景论证不足）。R2 交叉 REBUT 降为 should-fix：假设仅影响 Theorem 1 monotonicity，Proposition 3 提供 general case fallback，97.3% 实证保持率。Director 采纳 should-fix（高优先级）：需补充 NLP 场景讨论但不阻塞接收。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R6-M4\n    category: presentation\n    severity: must-fix\n    summary: \"Abstract sign reversal rate 与 Section 4.2 数值不一致\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: \"数值统一。\"\n    resolution_round: 7\n\n  - id: R8-C1\n    category: soundness\n    severity: must-fix\n    summary: \"K≥3 ASV 理论基础为 conjectural——Theorem 1 仅 K=2，Conjecture 1 缺理论证明\"\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 18\n    mentions:\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"R17 must-fix。\"\n      - round: 18\n        reviewers: [R1, R2]\n        note: \"R18 R2 列为 critical（ASV 在 K≥3 最重要场景缺形式化保证）。R1 交叉 AGREE with nuance：K≥3 贡献不仅限于 monotonicity（偏差表达式、sign preservation、FWL 均对一般 K 成立），ε<0.02 近似单调使 ASV 误差在 2% 以内。建议 Contribution 2 表述调整为 'empirically validated with proved K=2 foundation'。Director 采纳 should-fix（高优先级）。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R8-C2\n    category: soundness\n    severity: should-fix\n    summary: \"Proportional effects 在 NLP 中不可验证\"\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 18\n    mentions:\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"与 R6-M3 合并。\"\n      - round: 18\n        reviewers: [R1, R2]\n        note: \"与 R6-M3 合并。\"\n\n  - id: R8-W1\n    category: novelty\n    severity: should-fix\n    summary: \"ASV contribution 定位\"\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 18\n    mentions:\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"与 R4-W6 合并。\"\n      - round: 18\n        reviewers: [R1, R2]\n        note: \"与 R4-W6 合并。\"\n\n  - id: R8-W2\n    category: soundness\n    severity: should-fix\n    summary: \"Non-differential 假设讨论不足\"\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 18\n    mentions:\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"合并到 NEW-1。\"\n      - round: 18\n        reviewers: [R1, R2]\n        note: \"合并到 NEW-1。\"\n\n  - id: R8-W3\n    category: method\n    severity: minor\n    summary: \"δ* uncertainty bound 过宽\"\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 18\n    mentions:\n      - round: 17\n        reviewers: []\n        note: \"连续四轮未提出。\"\n      - round: 18\n        reviewers: []\n        note: \"R18 未提出。连续五轮未提出，建议关闭或降级。\"\n\n  - id: R9-C2\n    category: scope\n    severity: should-fix\n    summary: \"线性 SEM 假设对 EMNLP 读者可达性和泛化性不足\"\n    status: in_progress\n    first_raised_round: 9\n    last_seen_round: 18\n    mentions:\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"R17 should-fix。\"\n      - round: 18\n        reviewers: [R1, R2]\n        note: \"R18 R1-W2 再提：主文仅一句话提及 logistic regression 下 FWL 破缺，Algorithm 1 未区分 OLS/logistic 路径。R2 交叉强烈同意：Appendix B.14 显示 FWL 破缺幅度随 accuracy 增大。共识 should-fix。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R9-S1\n    category: novelty\n    severity: should-fix\n    summary: \"'first to characterize' novelty claim 需限定\"\n    status: in_progress\n    first_raised_round: 9\n    last_seen_round: 18\n    mentions:\n      - round: 17\n        reviewers: [R2]\n        note: \"R17 确认 'first unified analysis' 在当前文献范围内成立。\"\n      - round: 18\n        reviewers: [R1, R2]\n        note: \"R18 R2-W5 再提：限定词过多削弱 impact，建议更直接表述。R1 交叉 REBUT：claim 有合理基础（Carroll 2006 是教科书非拓扑特异性推导），但同意简化措辞。Director 采纳 minor。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R9-S3\n    category: experiments\n    severity: should-fix\n    summary: \"LLM 配置多样性有限（缺 <7B, >70B, ordinal）\"\n    status: in_progress\n    first_raised_round: 9\n    last_seen_round: 18\n    mentions:\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"合并到 R1-W3。\"\n      - round: 18\n        reviewers: [R1]\n        note: \"R18 R1-W1 间接覆盖（Dirichlet 采样代表性）。合并到 R1-W3。\"\n\n  - id: R11-W2\n    category: presentation\n    severity: should-fix\n    summary: \"Section 3.1 缺少 Notation roadmap——plim/FWL 对 NLP 读者不友好\"\n    status: in_progress\n    first_raised_round: 11\n    last_seen_round: 18\n    mentions:\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"R17 should-fix（高优先级）。\"\n      - round: 18\n        reviewers: [R1, R2]\n        note: \"R18 R2-W2 全面再提：plim/FWL/Wald/column-stochastic/Birkhoff polytope/Dirichlet prior 均缺直觉解释。R1 交叉 AGREE（自己也标注了 plim 问题）。共识 should-fix。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R11-W4\n    category: presentation\n    severity: minor\n    summary: \"IV 52.6% denominator sign change 的 NLP 实践含义未讨论\"\n    status: in_progress\n    first_raised_round: 11\n    last_seen_round: 18\n    mentions:\n      - round: 17\n        reviewers: []\n        note: \"R17 未提出。\"\n      - round: 18\n        reviewers: []\n        note: \"R18 未提出。连续三轮未提出。\"\n\n  - id: R12-MI2\n    category: presentation\n    severity: should-fix\n    summary: \"Figure 2 视觉问题\"\n    status: in_progress\n    first_raised_round: 12\n    last_seen_round: 18\n    mentions:\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"共识 minor：灰度下 red 难区分，建议 hatching。\"\n      - round: 18\n        reviewers: [R1, R2]\n        note: \"R18 R2-W4 再提。R1 交叉 AGREE。共识 minor。\"\n\n  - id: R15-N1\n    category: soundness\n    severity: must-fix\n    summary: \"Observation 1 声称 worst-case < 0.005 与 Table 10 不一致\"\n    status: in_progress\n    first_raised_round: 15\n    last_seen_round: 18\n    mentions:\n      - round: 17\n        reviewers: []\n        note: \"连续两轮未提出。\"\n      - round: 18\n        reviewers: []\n        note: \"R18 未提出。连续三轮未提出，可能已修复，待确认。\"\n\n  - id: R15-W1\n    category: presentation\n    severity: should-fix\n    summary: \"Table 1 Violation vs Sign Flip 列定义模糊\"\n    status: in_progress\n    first_raised_round: 15\n    last_seen_round: 18\n    mentions:\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"两位共识。\"\n      - round: 18\n        reviewers: []\n        note: \"R18 未单独提出。R2-minor-1 提到 τ overloading 但未重提 Table 1 定义问题。\"\n\n  - id: R15-W2\n    category: presentation\n    severity: should-fix\n    summary: \"Abstract FWL invariance 声明缺少 'under linear OLS' 限定词\"\n    status: in_progress\n    first_raised_round: 15\n    last_seen_round: 18\n    mentions:\n      - round: 17\n        reviewers: []\n        note: \"未单独提出。\"\n      - round: 18\n        reviewers: []\n        note: \"R18 未单独提出。R1-W2 间接覆盖（logistic regression 讨论不足）。\"\n\n  - id: R16-N1\n    category: presentation\n    severity: should-fix\n    summary: \"2.1% sign reversal 限定不清晰——secondary coefficient 还是 primary coefficient？\"\n    status: in_progress\n    first_raised_round: 16\n    last_seen_round: 18\n    mentions:\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"共识 should-fix。\"\n      - round: 18\n        reviewers: []\n        note: \"R18 未单独提出。R2-minor-1 提到 τ overloading 间接相关。\"\n\n  - id: R16-N2\n    category: presentation\n    severity: should-fix\n    summary: \"Correction guidance 深度不足——作为三大贡献之一，Section 4.5 仅半页\"\n    status: in_progress\n    first_raised_round: 16\n    last_seen_round: 18\n    mentions:\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"R17 should-fix（高优先级）。\"\n      - round: 18\n        reviewers: [R1, R2]\n        note: \"R18 R2-W1 再提：Algorithm 1 仅在 Appendix，与 Contribution 1/2 深度不匹配。R1 交叉 AGREE，倾向降级为 practical implication。共识 should-fix。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R17-N1\n    category: format\n    severity: must-fix\n    summary: \"Abstract 超过 EMNLP 2026 的 200 words 限制（实际约 245 words）\"\n    status: wont_fix\n    first_raised_round: 17\n    last_seen_round: 17\n    resolution: \"REBUT: Abstract is 183 words by 3 counting methods. Reviewer count of ~245 includes LaTeX markup.\"\n    resolution_round: 17\n\n  - id: R17-W1\n    category: soundness\n    severity: should-fix\n    summary: \"Collider sign preservation 仅有经验验证\"\n    status: in_progress\n    first_raised_round: 17\n    last_seen_round: 18\n    mentions:\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"R17 共识 should-fix。\"\n      - round: 18\n        reviewers: []\n        note: \"R18 未单独提出。\"\n\n  - id: R17-W2\n    category: format\n    severity: minor\n    summary: \"Bib 含未引用条目\"\n    status: in_progress\n    first_raised_round: 17\n    last_seen_round: 18\n    mentions:\n      - round: 17\n        reviewers: [R2]\n        note: \"dawid1979, rosenbaum2002 未引用。\"\n      - round: 18\n        reviewers: [R2]\n        note: \"R18 R2-minor-3 发现 manski1990 也是 orphan entry。\"\n\n  # === Round 18 新发现 ===\n\n  - id: R18-W1\n    category: experiments\n    severity: should-fix\n    summary: \"Dirichlet(1,1,...,1) 采样对高维 K 代表性不足——K=5/7 的均匀采样偏离实际 LLM 矩阵分布\"\n    status: open\n    first_raised_round: 18\n    last_seen_round: 18\n    mentions:\n      - round: 18\n        reviewers: [R1, R2]\n        note: \"R1 首提。R2 交叉 AGREE 但指出经验 LLM 矩阵已验证核心结论，Dirichlet 代表性不影响最终结论稳健性。共识 should-fix（低优先级）。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R18-W2\n    category: method\n    severity: should-fix\n    summary: \"Significance ASV 对样本量 N 的依赖未充分探讨——Figure 3 仅展示单一 N 值\"\n    status: open\n    first_raised_round: 18\n    last_seen_round: 18\n    mentions:\n      - round: 18\n        reviewers: [R1, R2]\n        note: \"R1 首提，R2 交叉 AGREE。建议增加不同 N 下各拓扑 significance ASV 变化的可视化。共识 should-fix。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R18-W3\n    category: soundness\n    severity: should-fix\n    summary: \"Conjecture 1 的 ε<0.02 约束完全来自数值实验，缺乏为何 ε 应该小的理论直觉\"\n    status: open\n    first_raised_round: 18\n    last_seen_round: 18\n    mentions:\n      - round: 18\n        reviewers: [R1, R2]\n        note: \"R1 首提，R2 交叉 AGREE 并补充可能的直觉论证路径（proportional effects 下精确，deviations 来自 non-proportional residual）。共识 should-fix。\"\n    resolution: \"\"\n    resolution_round: null\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "causal_annot_error_attrib",
    "issues_yaml": "issues:\n  # === Round 1-7 历史 (resolved，保留摘要) ===\n\n  - id: R1-N1\n    category: soundness\n    severity: must-fix\n    summary: \"Theorem 1 适用范围过窄（仅 confounding+proportional effects），K≥3 证明不完整\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 7\n    resolution: \"Theorem 1 现正确限定为 K=2；K≥3 由 Observation 1 和 Conjecture 1 覆盖。\"\n    resolution_round: 7\n\n  - id: R1-N2\n    category: soundness\n    severity: should-fix\n    summary: \"3/5 安全拓扑的符号保持仅有数值验证，Abstract 用 'establish' 暗示已证明\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 3\n    resolution: \"Abstract 已准确区分 prove/verify。\"\n    resolution_round: 4\n\n  - id: R1-N3\n    category: soundness\n    severity: must-fix\n    summary: \"ASV C(δ) 定义域错误\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Section 3.3 已引入 δ_max 约束。\"\n    resolution_round: 2\n\n  - id: R2-N1\n    category: presentation\n    severity: must-fix\n    summary: \"83.4% sign reversal headline framing 过度声称\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    resolution: \"Introduction 已重写。\"\n    resolution_round: 5\n\n  - id: R2-N2\n    category: novelty\n    severity: should-fix\n    summary: \"'first systematic framework' 过度声明\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"已修复。\"\n    resolution_round: 2\n\n  - id: R2-N3\n    category: related_work\n    severity: must-fix\n    summary: \"4 篇关键相关工作未引用\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"已修复。\"\n    resolution_round: 2\n\n  - id: R1-W2\n    category: clarity\n    severity: should-fix\n    summary: \"Sign preservation 的 DGP 条件在实践中难以事前验证\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"Section 3.2 已添加 ASV 替代讨论。\"\n    resolution_round: 3\n\n  - id: R1-W3\n    category: experiments\n    severity: should-fix\n    summary: \"实证验证不完整：缺少商业 LLM\"\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 18\n    mentions:\n      - round: 7\n        reviewers: [R2]\n        note: \"Limitations 中讨论即可。\"\n      - round: 14\n        reviewers: [R1, R2]\n        note: \"R14 共识：minor。\"\n      - round: 15\n        reviewers: [R1, R2]\n        note: \"R15 共识：should-fix（低优先级），Limitations 已覆盖。\"\n      - round: 16\n        reviewers: [R1, R2]\n        note: \"R16 R1-M2 再提为 minor。\"\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"R17 共识 should-fix（低优先级）。\"\n      - round: 18\n        reviewers: [R1]\n        note: \"R18 R1-W1 再提 Dirichlet 采样代表性（高 K 覆盖率不足），R2 交叉 AGREE 但指出 23 个经验 LLM 矩阵已验证核心结论。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R2-W2\n    category: presentation\n    severity: should-fix\n    summary: \"98 场景 zero sign reversals 与 sign reversal narrative 的 tension\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"已解决。\"\n    resolution_round: 2\n\n  - id: R2-W3\n    category: method\n    severity: should-fix\n    summary: \"ASV 对 C₀ 估计不确定性的敏感性\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"Bootstrap ASV 分析已完成。\"\n    resolution_round: 3\n\n  - id: R2-W4\n    category: scope\n    severity: should-fix\n    summary: \"线性 SEM 假设限制；Algorithm 1 缺 linear-only caveat\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    resolution: \"Section 4.5 FWL 段加 'Under linear OLS' 限定。\"\n    resolution_round: 5\n\n  - id: R1-W4\n    category: experiments\n    severity: should-fix\n    summary: \"MC MAPE 报告不充分\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"已修复。\"\n    resolution_round: 2\n\n  - id: MISC-1\n    category: presentation\n    severity: minor\n    summary: \"符号不统一（τ vs β_T）、Proposition 编号不一致\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    resolution: \"method.tex 添加 τ 在各拓扑下含义的明确说明。\"\n    resolution_round: 5\n\n  - id: NEW-1\n    category: soundness\n    severity: should-fix\n    summary: \"Non-differential misclassification 假设讨论不足\"\n    status: in_progress\n    first_raised_round: 2\n    last_seen_round: 18\n    mentions:\n      - round: 14\n        reviewers: [R1, R2]\n        note: \"R14 共识 minor。\"\n      - round: 15\n        reviewers: [R1, R2]\n        note: \"R15 共识 should-fix。\"\n      - round: 16\n        reviewers: [R1, R2]\n        note: \"R16 R1-W1 + R2-Q2 再提。\"\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"R17 共识 should-fix。\"\n      - round: 18\n        reviewers: [R1, R2]\n        note: \"R18 升级为 must-fix。R1 指出 VAST topic-stratified 检验不等于 Y-stratified 检验，stress test 未回答真实 ε 是多少。R2 交叉 AGREE 但补充结构性论证（LLM API 不观测 Y）比 R1 承认的更强。共识：按 Y 分层验证是 critical 改进。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: NEW-2\n    category: related_work\n    severity: should-fix\n    summary: \"缺少 Feder et al. (2022) 和 Cheng et al. (2024)\"\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 5\n    resolution: \"已引用。\"\n    resolution_round: 5\n\n  - id: NEW-3\n    category: soundness\n    severity: should-fix\n    summary: \"Conjecture 1 数值验证规模\"\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"210,000 matrices + adversarial + analytic plim。\"\n    resolution_round: 3\n\n  - id: R3-NEW-1\n    category: format\n    severity: must-fix\n    summary: \"正文超出 EMNLP 2026 Long Paper 8 页限制\"\n    status: open\n    first_raised_round: 3\n    last_seen_round: 18\n    mentions:\n      - round: 12\n        reviewers: [R1, R2]\n        note: \"R12 再提。\"\n      - round: 13\n        reviewers: []\n        note: \"已修复，Conclusion 已压缩。\"\n      - round: 18\n        reviewers: [R1, R2]\n        note: \"R18 复发。R2 确认 Section 5 Conclusion 完整位于第 9 页（约 13-14 行主文溢出）。R1 交叉 AGREE 违规存在但建议降级为 should-fix。Director 采纳 must-fix：EMNLP strict 8-page limit 是硬约束。\"\n    resolution: \"R13 曾解决但 R18 复发。\"\n    resolution_round: null\n\n  - id: R3-NEW-2\n    category: soundness\n    severity: should-fix\n    summary: \"FWL invariance 结论缺乏 precise statement 和推导\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"FWL 证明完整。\"\n    resolution_round: 5\n\n  - id: R3-NEW-3\n    category: scope\n    severity: should-fix\n    summary: \"缺少 outcome misclassification 讨论\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"Limitations 已添加。\"\n    resolution_round: 4\n\n  - id: R3-NEW-4\n    category: presentation\n    severity: should-fix\n    summary: \"Abstract/Introduction 信息过载（数字密度）\"\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 18\n    mentions:\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"R17 与 R17-N1 联合。\"\n      - round: 18\n        reviewers: [R2]\n        note: \"R18 R2-minor-2 再提：Abstract 约 184 words 符合限制，但 7+ 具体数字难以首次阅读消化。R1 交叉 AGREE。共识 minor。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R3-NEW-5\n    category: related_work\n    severity: should-fix\n    summary: \"缺少 5 篇相关引用（Round 3 要求的）\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 3\n    resolution: \"全部 5 篇已引用。\"\n    resolution_round: 4\n\n  - id: R3-NEW-6\n    category: reproducibility\n    severity: should-fix\n    summary: \"未承诺代码/数据公开\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"Conclusion 已添加代码公开承诺。\"\n    resolution_round: 4\n\n  - id: R3-NEW-7\n    category: novelty\n    severity: should-fix\n    summary: \"新颖性定位不清：未明确界定已知结果 vs 新贡献\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"确认'首次跨 7 种拓扑系统比较'成立。\"\n    resolution_round: 5\n\n  - id: R3-NEW-8\n    category: experiments\n    severity: should-fix\n    summary: \"经验验证使用模拟 DGP 而非真实因果数据\"\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 18\n    mentions:\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"R17 should-fix（高优先级）。\"\n      - round: 18\n        reviewers: []\n        note: \"R18 未单独提出，但 R1-N2 间接覆盖（要求实证验证 non-differential 假设需要 gold-label 数据集）。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R4-W6\n    category: novelty\n    severity: should-fix\n    summary: \"ASV 方法论创新有限——E-value 直接移植质疑\"\n    status: in_progress\n    first_raised_round: 4\n    last_seen_round: 18\n    mentions:\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"R17 共识 should-fix。\"\n      - round: 18\n        reviewers: [R2]\n        note: \"R18 R2-W3 再提：Remark 1 三点对比框架有误导性，暗示 ASV 是 E-value 的改进版而非互补工具。R1 交叉 AGREE with nuance：distinctions 准确但表述暗含 'improvements over'。共识：重新框定为互补工具。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R4-W7\n    category: presentation\n    severity: should-fix\n    summary: \"论文广度有余深度不足\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 7\n    resolution: \"Appendix pointer 已添加。\"\n    resolution_round: 8\n\n  - id: R4-W8\n    category: scope\n    severity: should-fix\n    summary: \"DAG 拓扑必须先验已知——Algorithm 1 依赖正确拓扑输入\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    resolution: \"Limitations 已添加相关讨论。\"\n    resolution_round: 5\n\n  - id: R4-W10\n    category: method\n    severity: minor\n    summary: \"PPI++ 对 M-bias 有害 (-88%) 缺乏机制解释\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 15\n    resolution: \"Section 4.5 已包含完整机制解释。\"\n    resolution_round: 15\n\n  - id: R4-W12\n    category: presentation\n    severity: minor\n    summary: \"引用格式问题\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 7\n    resolution: \"格式合规检查通过。\"\n    resolution_round: 8\n\n  - id: R5-N1\n    category: presentation\n    severity: must-fix\n    summary: \"Table 1 的 sign-flip guarantee ✓ 掩盖了 DGP 条件性\"\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"Table 1 已实现三级符号 ✓/✓*/✗。\"\n    resolution_round: 5\n\n  - id: R5-N2\n    category: soundness\n    severity: should-fix\n    summary: \"Conjecture 1 的 ε 在极端条件下可达 0.14-0.15\"\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"Conjecture 1 rewritten with per-topology ε bounds。\"\n    resolution_round: 5\n\n  - id: R5-N3\n    category: presentation\n    severity: must-fix\n    summary: \"'Primary coefficient never reverses' 仅为经验发现，缺乏理论保证\"\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 11\n    resolution: \"Abstract 已改为经验事实描述。\"\n    resolution_round: 11\n\n  - id: R5-MR\n    category: related_work\n    severity: should-fix\n    summary: \"Round 5 新发现的缺失引用\"\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"三篇引用已添加。\"\n    resolution_round: 5\n\n  - id: R6-M1\n    category: soundness\n    severity: should-fix\n    summary: \"Theorem 1 对 K≥3 未证明但标记为 Theorem\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: \"Theorem 1 现正确限定为 K=2。\"\n    resolution_round: 7\n\n  - id: R6-M3\n    category: soundness\n    severity: should-fix\n    summary: \"Proportional effects 假设 (f=λg) 在 NLP 中是强限制\"\n    status: in_progress\n    first_raised_round: 6\n    last_seen_round: 18\n    mentions:\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"R17 共识 should-fix。\"\n      - round: 18\n        reviewers: [R1, R2]\n        note: \"R18 R1 列为 critical（NLP 场景论证不足）。R2 交叉 REBUT 降为 should-fix：假设仅影响 Theorem 1 monotonicity，Proposition 3 提供 general case fallback，97.3% 实证保持率。Director 采纳 should-fix（高优先级）：需补充 NLP 场景讨论但不阻塞接收。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R6-M4\n    category: presentation\n    severity: must-fix\n    summary: \"Abstract sign reversal rate 与 Section 4.2 数值不一致\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: \"数值统一。\"\n    resolution_round: 7\n\n  - id: R8-C1\n    category: soundness\n    severity: must-fix\n    summary: \"K≥3 ASV 理论基础为 conjectural——Theorem 1 仅 K=2，Conjecture 1 缺理论证明\"\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 18\n    mentions:\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"R17 must-fix。\"\n      - round: 18\n        reviewers: [R1, R2]\n        note: \"R18 R2 列为 critical（ASV 在 K≥3 最重要场景缺形式化保证）。R1 交叉 AGREE with nuance：K≥3 贡献不仅限于 monotonicity（偏差表达式、sign preservation、FWL 均对一般 K 成立），ε<0.02 近似单调使 ASV 误差在 2% 以内。建议 Contribution 2 表述调整为 'empirically validated with proved K=2 foundation'。Director 采纳 should-fix（高优先级）。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R8-C2\n    category: soundness\n    severity: should-fix\n    summary: \"Proportional effects 在 NLP 中不可验证\"\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 18\n    mentions:\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"与 R6-M3 合并。\"\n      - round: 18\n        reviewers: [R1, R2]\n        note: \"与 R6-M3 合并。\"\n\n  - id: R8-W1\n    category: novelty\n    severity: should-fix\n    summary: \"ASV contribution 定位\"\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 18\n    mentions:\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"与 R4-W6 合并。\"\n      - round: 18\n        reviewers: [R1, R2]\n        note: \"与 R4-W6 合并。\"\n\n  - id: R8-W2\n    category: soundness\n    severity: should-fix\n    summary: \"Non-differential 假设讨论不足\"\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 18\n    mentions:\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"合并到 NEW-1。\"\n      - round: 18\n        reviewers: [R1, R2]\n        note: \"合并到 NEW-1。\"\n\n  - id: R8-W3\n    category: method\n    severity: minor\n    summary: \"δ* uncertainty bound 过宽\"\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 18\n    mentions:\n      - round: 17\n        reviewers: []\n        note: \"连续四轮未提出。\"\n      - round: 18\n        reviewers: []\n        note: \"R18 未提出。连续五轮未提出，建议关闭或降级。\"\n\n  - id: R9-C2\n    category: scope\n    severity: should-fix\n    summary: \"线性 SEM 假设对 EMNLP 读者可达性和泛化性不足\"\n    status: in_progress\n    first_raised_round: 9\n    last_seen_round: 18\n    mentions:\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"R17 should-fix。\"\n      - round: 18\n        reviewers: [R1, R2]\n        note: \"R18 R1-W2 再提：主文仅一句话提及 logistic regression 下 FWL 破缺，Algorithm 1 未区分 OLS/logistic 路径。R2 交叉强烈同意：Appendix B.14 显示 FWL 破缺幅度随 accuracy 增大。共识 should-fix。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R9-S1\n    category: novelty\n    severity: should-fix\n    summary: \"'first to characterize' novelty claim 需限定\"\n    status: in_progress\n    first_raised_round: 9\n    last_seen_round: 18\n    mentions:\n      - round: 17\n        reviewers: [R2]\n        note: \"R17 确认 'first unified analysis' 在当前文献范围内成立。\"\n      - round: 18\n        reviewers: [R1, R2]\n        note: \"R18 R2-W5 再提：限定词过多削弱 impact，建议更直接表述。R1 交叉 REBUT：claim 有合理基础（Carroll 2006 是教科书非拓扑特异性推导），但同意简化措辞。Director 采纳 minor。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R9-S3\n    category: experiments\n    severity: should-fix\n    summary: \"LLM 配置多样性有限（缺 <7B, >70B, ordinal）\"\n    status: in_progress\n    first_raised_round: 9\n    last_seen_round: 18\n    mentions:\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"合并到 R1-W3。\"\n      - round: 18\n        reviewers: [R1]\n        note: \"R18 R1-W1 间接覆盖（Dirichlet 采样代表性）。合并到 R1-W3。\"\n\n  - id: R11-W2\n    category: presentation\n    severity: should-fix\n    summary: \"Section 3.1 缺少 Notation roadmap——plim/FWL 对 NLP 读者不友好\"\n    status: in_progress\n    first_raised_round: 11\n    last_seen_round: 18\n    mentions:\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"R17 should-fix（高优先级）。\"\n      - round: 18\n        reviewers: [R1, R2]\n        note: \"R18 R2-W2 全面再提：plim/FWL/Wald/column-stochastic/Birkhoff polytope/Dirichlet prior 均缺直觉解释。R1 交叉 AGREE（自己也标注了 plim 问题）。共识 should-fix。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R11-W4\n    category: presentation\n    severity: minor\n    summary: \"IV 52.6% denominator sign change 的 NLP 实践含义未讨论\"\n    status: in_progress\n    first_raised_round: 11\n    last_seen_round: 18\n    mentions:\n      - round: 17\n        reviewers: []\n        note: \"R17 未提出。\"\n      - round: 18\n        reviewers: []\n        note: \"R18 未提出。连续三轮未提出。\"\n\n  - id: R12-MI2\n    category: presentation\n    severity: should-fix\n    summary: \"Figure 2 视觉问题\"\n    status: in_progress\n    first_raised_round: 12\n    last_seen_round: 18\n    mentions:\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"共识 minor：灰度下 red 难区分，建议 hatching。\"\n      - round: 18\n        reviewers: [R1, R2]\n        note: \"R18 R2-W4 再提。R1 交叉 AGREE。共识 minor。\"\n\n  - id: R15-N1\n    category: soundness\n    severity: must-fix\n    summary: \"Observation 1 声称 worst-case < 0.005 与 Table 10 不一致\"\n    status: in_progress\n    first_raised_round: 15\n    last_seen_round: 18\n    mentions:\n      - round: 17\n        reviewers: []\n        note: \"连续两轮未提出。\"\n      - round: 18\n        reviewers: []\n        note: \"R18 未提出。连续三轮未提出，可能已修复，待确认。\"\n\n  - id: R15-W1\n    category: presentation\n    severity: should-fix\n    summary: \"Table 1 Violation vs Sign Flip 列定义模糊\"\n    status: in_progress\n    first_raised_round: 15\n    last_seen_round: 18\n    mentions:\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"两位共识。\"\n      - round: 18\n        reviewers: []\n        note: \"R18 未单独提出。R2-minor-1 提到 τ overloading 但未重提 Table 1 定义问题。\"\n\n  - id: R15-W2\n    category: presentation\n    severity: should-fix\n    summary: \"Abstract FWL invariance 声明缺少 'under linear OLS' 限定词\"\n    status: in_progress\n    first_raised_round: 15\n    last_seen_round: 18\n    mentions:\n      - round: 17\n        reviewers: []\n        note: \"未单独提出。\"\n      - round: 18\n        reviewers: []\n        note: \"R18 未单独提出。R1-W2 间接覆盖（logistic regression 讨论不足）。\"\n\n  - id: R16-N1\n    category: presentation\n    severity: should-fix\n    summary: \"2.1% sign reversal 限定不清晰——secondary coefficient 还是 primary coefficient？\"\n    status: in_progress\n    first_raised_round: 16\n    last_seen_round: 18\n    mentions:\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"共识 should-fix。\"\n      - round: 18\n        reviewers: []\n        note: \"R18 未单独提出。R2-minor-1 提到 τ overloading 间接相关。\"\n\n  - id: R16-N2\n    category: presentation\n    severity: should-fix\n    summary: \"Correction guidance 深度不足——作为三大贡献之一，Section 4.5 仅半页\"\n    status: in_progress\n    first_raised_round: 16\n    last_seen_round: 18\n    mentions:\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"R17 should-fix（高优先级）。\"\n      - round: 18\n        reviewers: [R1, R2]\n        note: \"R18 R2-W1 再提：Algorithm 1 仅在 Appendix，与 Contribution 1/2 深度不匹配。R1 交叉 AGREE，倾向降级为 practical implication。共识 should-fix。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R17-N1\n    category: format\n    severity: must-fix\n    summary: \"Abstract 超过 EMNLP 2026 的 200 words 限制（实际约 245 words）\"\n    status: wont_fix\n    first_raised_round: 17\n    last_seen_round: 17\n    resolution: \"REBUT: Abstract is 183 words by 3 counting methods. Reviewer count of ~245 includes LaTeX markup.\"\n    resolution_round: 17\n\n  - id: R17-W1\n    category: soundness\n    severity: should-fix\n    summary: \"Collider sign preservation 仅有经验验证\"\n    status: in_progress\n    first_raised_round: 17\n    last_seen_round: 18\n    mentions:\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"R17 共识 should-fix。\"\n      - round: 18\n        reviewers: []\n        note: \"R18 未单独提出。\"\n\n  - id: R17-W2\n    category: format\n    severity: minor\n    summary: \"Bib 含未引用条目\"\n    status: in_progress\n    first_raised_round: 17\n    last_seen_round: 18\n    mentions:\n      - round: 17\n        reviewers: [R2]\n        note: \"dawid1979, rosenbaum2002 未引用。\"\n      - round: 18\n        reviewers: [R2]\n        note: \"R18 R2-minor-3 发现 manski1990 也是 orphan entry。\"\n\n  # === Round 18 新发现 ===\n\n  - id: R18-W1\n    category: experiments\n    severity: should-fix\n    summary: \"Dirichlet(1,1,...,1) 采样对高维 K 代表性不足——K=5/7 的均匀采样偏离实际 LLM 矩阵分布\"\n    status: open\n    first_raised_round: 18\n    last_seen_round: 18\n    mentions:\n      - round: 18\n        reviewers: [R1, R2]\n        note: \"R1 首提。R2 交叉 AGREE 但指出经验 LLM 矩阵已验证核心结论，Dirichlet 代表性不影响最终结论稳健性。共识 should-fix（低优先级）。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R18-W2\n    category: method\n    severity: should-fix\n    summary: \"Significance ASV 对样本量 N 的依赖未充分探讨——Figure 3 仅展示单一 N 值\"\n    status: open\n    first_raised_round: 18\n    last_seen_round: 18\n    mentions:\n      - round: 18\n        reviewers: [R1, R2]\n        note: \"R1 首提，R2 交叉 AGREE。建议增加不同 N 下各拓扑 significance ASV 变化的可视化。共识 should-fix。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R18-W3\n    category: soundness\n    severity: should-fix\n    summary: \"Conjecture 1 的 ε<0.02 约束完全来自数值实验，缺乏为何 ε 应该小的理论直觉\"\n    status: open\n    first_raised_round: 18\n    last_seen_round: 18\n    mentions:\n      - round: 18\n        reviewers: [R1, R2]\n        note: \"R1 首提，R2 交叉 AGREE 并补充可能的直觉论证路径（proportional effects 下精确，deviations 来自 non-proportional residual）。共识 should-fix。\"\n    resolution: \"\"\n    resolution_round: null\n"
  }
}
```

</details>

---


### Tool result

_source line 1483 · 2026-05-23T15:41:51.065290+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_issues.yaml\", \"bytes\": 20535}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 1484 · 2026-05-23T15:44:43.598951+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# 审稿报告：Round 18（Fresh Review）\n\n**论文**: Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction\n**Venue**: EMNLP 2026 (ARR Long Paper)\n**审稿模式**: Fresh（重新审稿）\n**Reviewer**: R1（方法严谨性）+ R2（新颖性/完整性）\n**日期**: 2026-05-23\n\n---\n\n## Summary\n\n本文研究 LLM 标注器产生的多类别标注误差（K≥3）如何在 7 种典型因果 DAG 拓扑下传播到下游因果估计。核心贡献包括：(1) 在非差异错分类假设下推导 7 种拓扑的闭式偏差表达式，建立 sign-preservation/reversal 二分法（5 种拓扑保持符号，exposure 和 IV 可逆转）；(2) 定义 Annotation Sensitivity Values (ASV) 框架，包含幅度、显著性和符号翻转三种诊断，揭示从 IV（最脆弱）到 M-bias（免疫）的拓扑依赖脆弱性谱；(3) 证明 FWL 不变性使得矩阵校正方法在四种协变量拓扑下精确无效（0% bias reduction），并评估 5 种校正方法。论文通过 Monte Carlo 模拟（161 场景，grand MAPE 1.6%）和 23 个真实 LLM 配置（HumAID K=10, VAST K=3, CivilComments K=2）进行实证验证。\n\n---\n\n## Strengths\n\n**S1. 真正的统一拓扑分析**: 首次在统一框架内系统比较同一 confusion matrix 在 7 种 DAG 拓扑下产生定性不同的偏差。sign-preservation/reversal 二分法是一个清晰有力的核心发现，填补了流行病学测量误差理论与 NLP 实践之间的缺口。[R1-S1, R2-Strength-1, 共识]\n\n**S2. FWL 不变性负面结果**: 证明矩阵校正方法（confusion matrix inversion）对 4 种协变量拓扑的 bias reduction 为精确 0%——这是一个干净、完整的结构性结果（Appendix B.2 列空间论证），对实践者有直接警示意义。[R1-S3, R2-Strength-2, 共识]\n\n**S3. 诚实的认知层级**: Proved（K=2, Theorem 1）→ Verified（K≥3, Observation 1）→ Conjectured（Conjecture 1）的三级层次在理论论文中值得赞赏，避免了对 K≥3 结果的过度声称。[R1-S2, R2-Strength-4, 共识]\n\n**S4. 全面的实证验证**: 161 scenarios × 23 LLM configurations × 3 NLP tasks；100,000 Dirichlet matrices；theory-MC MAPE 1.6%（per-topology 0.3%-3.7%）。F₁ 与因果 bias 无显著相关性（Spearman ρ = -0.10, p = 0.45）的发现对 CSS 研究者有直接可操作价值。[R1-S4, R2-Strength-3/5, 共识]\n\n**S5. 实用决策框架**: ASV 与 E-value 类比设计得当，Algorithm 1 的拓扑感知校正决策树为实践者提供清晰操作指南。[R1-S5]\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**MF-1** [format] **正文页数超出 EMNLP 2026 strict 8-page limit**\n- Section 5 Conclusion 完整位于第 9 页（约 13-14 行主文内容溢出）。EMNLP 2026 strict 8-page limit 是硬约束，违规可致 desk rejection。\n- R2 首提为 critical，R1 交叉确认违规存在但建议降级。**Director 裁决 must-fix**：格式合规是硬约束，修复成本极低（压缩 Section 4.5 + 精简 Conclusion）。\n- 修复方案：(a) 精简 Section 4.5 \"Case studies and sensitivity\" 段落（细节已在 Appendix）；(b) Conclusion 压缩至 5-6 行；(c) 或将 Figure 4/5 之一移至 Appendix。\n\n**MF-2** [soundness] **非差异错分类假设在 LLM 标注器语境下缺乏直接实证检验**\n- Definition 1 要求 P(A*=j|A=k,Y) = P(A*=j|A=k)。LLM 预训练数据编码 A-Y 关联，可能系统性违反此假设。现有检验不充分：Appendix B.5 VAST topic-stratified 检验仅一个数据集，且 topic 分层 ≠ Y 分层；Appendix B.6/B.8 stress test 显示 ε=0.01 structured departure 即导致 14/16 K≥3 exposure 配置 sign reversal。\n- R1 首提为 critical，R2 交叉 AGREE（但补充结构性论证——LLM API 不观测 Y——比 R1 承认的更强）。**共识 must-fix**。\n- 修复方案：在至少一个有 gold labels 的 NLP 数据集上，按 Y 值分层计算 LLM 错分类矩阵，直接检验 P(A*|A,Y=0) ≈ P(A*|A,Y=1)。即使只做一个数据集（如 HumAID），也能为结构性论证提供 empirical backing。\n\n### Should-Fix（影响评分但不一票否决）\n\n**SF-1** [soundness, 高优先级] **K≥3 ASV monotonicity 仅为 Conjecture，削弱 Contribution 2 的理论定位**\n- Theorem 1（envelope monotonicity）仅在 K=2 + proportional effects 下证明。K≥3 依赖 Observation 1（数值验证，ε<0.02）和 Conjecture 1。论文核心论点是 K≥3 引入结构性新现象，但其 ASV 框架恰恰无法为 K≥3 提供形式化保证。\n- R2 首提为 critical，R1 交叉 AGREE with nuance（K≥3 贡献多维——偏差表达式、sign preservation、FWL 均对一般 K 成立，不仅限于 monotonicity；ε<0.02 使 ASV 误差在 2% 以内）。**Director 裁决 should-fix（高优先级）**：R1 论点有力，K≥3 贡献确实不仅限于 monotonicity。\n- 修复方案：(a) 将 Contribution 2 重新表述为 \"empirically validated diagnostic with proved K=2 foundation\"；(b) 补充 monotonicity failure 的后果分析（如果 ε 达到极端值，对 ASV ranking 的影响有多大）。\n\n**SF-2** [soundness, 高优先级] **比例效应假设 (f=λg) 在 NLP 场景下缺乏具体讨论**\n- Theorem 1 依赖 f=λg。在 NLP 多类别处理（如 stance detection 的 favor/against/neutral）中，不同类别可能有质性不同的效应，不满足比例关系。论文仅一句话提及 \"plausible in NLP tasks with a single quality dimension\"。\n- R1 首提为 critical，R2 REBUT 降为 should-fix（假设仅影响 Theorem 1 monotonicity，Proposition 3 提供 general case fallback，97.3% 实证保持率）。**Director 采纳 should-fix（高优先级）**：R2 论证有力——假设范围比 R1 描述的更窄。\n- 修复方案：增加 2-3 句具体 NLP 因果推断场景的分析（如 stance detection 3-class 是否接近 proportional）。\n\n**SF-3** [scope] **Logistic regression 讨论不充分**\n- NLP 最常用 logistic regression。主文仅一句话提及 FWL invariance 在 logistic 下的破缺（Section 4.5）。Appendix B.14 显示 FWL 破缺幅度随 accuracy 增大（exposure: -22% to -78%）。Algorithm 1 未区分 OLS/logistic 路径。\n- R1 首提，R2 强烈同意。**共识 should-fix**。\n- 修复方案：Section 4.5 增加 1-2 段 logistic regression 指导，引用 Appendix B.2/B.7/B.14；Algorithm 1 增加 OLS/logistic 分支。\n\n**SF-4** [presentation, 高优先级] **术语壁垒对 NLP 读者可达性不足**\n- plim、FWL theorem、Wald estimator、column-stochastic matrix、Birkhoff polytope、Dirichlet prior——对 EMNLP 受众属于高门槛术语，直觉解释不充分。如果多数 reviewer 无法流畅理解 method section，将影响 soundness 和 confidence 打分。\n- R2 首提，R1 交叉 AGREE。**共识 should-fix**。\n- 修复方案：每个关键术语首次使用时增加 1-2 句直觉解释（约增 6-8 行，页数压缩后有空间）。\n\n**SF-5** [presentation] **Contribution 3（correction guidance）正文深度与\"贡献\"定位不匹配**\n- \"Topology-aware correction guidance\" 被列为三大贡献之一，但正文仅约 0.7 页。Algorithm 1 仅在 Appendix。与 Contribution 1（~3 页 method）和 Contribution 2（~1.5 页 ASV + experiments）相比深度不足。\n- R2 首提，R1 交叉 AGREE（倾向降级为 practical implication）。**共识 should-fix**。\n- 修复方案：(a) 将 Algorithm 1 提升至正文（需结合 MF-1 的压缩方案）；或 (b) 降级为 \"practical implication\" 而非 co-equal contribution。\n\n**SF-6** [novelty] **ASV 与 E-value 的比较框架有误导性**\n- Remark 1 的三点 \"structural distinctions from E-values\" 本质上是不同工具解决不同问题（annotation error vs. unmeasured confounding）。当前表述暗示 ASV 是 E-values 的改进版。ASV 的真正贡献是将 sensitivity analysis 范式适配到 annotation error + topology dependence。\n- R2 首提，R1 交叉 AGREE with nuance（distinctions 准确但表述暗含 improvements over）。**共识 should-fix**。\n- 修复方案：Remark 1 重新框定为互补工具（complementary tools for different sources of bias）。\n\n**SF-7** [experiments] **Dirichlet(1,1,...,1) 采样对高维 K 代表性不足**\n- K=5（20 参数）和 K=7（42 参数）下，均匀 Dirichlet 采样偏离实际 LLM 矩阵分布（对角线期望 1/K vs 实际 >0.6）。R2 补充：23 个经验 LLM 矩阵已验证核心结论，代表性问题不影响最终结论。\n- R1 首提，R2 交叉 AGREE。**共识 should-fix（低优先级）**。\n- 修复方案：补充 Dirichlet(α,1,...,1) (α>>1) 采样验证，或报告对角线 >0.6 子空间的 ε 值。\n\n**SF-8** [method] **Significance ASV 对样本量 N 的依赖未充分探讨**\n- δ_sig 通过 SE(N) 依赖于 N，Figure 3 仅展示单一 N 值。不同 N 下 significance ASV 的变化是 practitioners 的关键决策信息。\n- R1 首提，R2 交叉 AGREE。**共识 should-fix**。\n- 修复方案：增加不同 N（如 1K, 5K, 10K, 50K）下各拓扑 δ*_sig 变化的可视化（Figure 或 Table）。\n\n**SF-9** [soundness] **Conjecture 1 的 ε<0.02 约束缺乏理论直觉**\n- ε 约束完全来自数值实验，论文未解释为什么 ε 应该很小。R2 补充可能的直觉路径：proportional effects 下精确单调，deviations 来自 non-proportional residual。\n- R1 首提，R2 交叉 AGREE。**共识 should-fix**。\n- 修复方案：补充 1 段关于 ε 小的直觉论证（如与列随机矩阵空间的凸体结构或 proportional residual 分析相关）。\n\n### Minor（不影响接收）\n\n1. **Abstract 信息密度过高**：约 184 words 符合 ≤200 限制，但 7+ 具体数字首次阅读难以消化。建议精简至 2-3 个最具冲击力的数字。[R2-minor-2, R1 AGREE]\n2. **Figure 2 灰度打印可辨识性**：红色 sign reversal 标识在灰度下难以区分，建议增加 hatching/pattern fill。[R2-W4, R1 AGREE]\n3. **τ 符号 overloading**：τ 在不同拓扑下含义不同但未充分标注。[R2-minor-1, R1 AGREE]\n4. **Orphan bib entries**：manski1990 未在正文引用，应移除或添加引用。[R2-minor-3]\n5. **引用格式不一致**：部分 bib 条目缺 doi 或页码。[R2-minor-4]\n6. **\"First unified analysis\" 措辞**：限定词过多，建议简化为 \"first systematic topology-specific comparison\"。[R2-W5, R1 partial REBUT: claim 有合理基础但措辞可优化]\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 达成共识（[AGREE] 或交叉后无争议）：\n\n1. **非差异错分类假设需要 Y-stratified 实证检验** [must-fix] — R1 首提，R2 AGREE\n2. **页数超限需修复** [must-fix (R2) / should-fix (R1)] — 违规存在无争议，仅严重性有分歧\n3. **Logistic regression 讨论不充分** [should-fix] — R1 首提，R2 强烈同意\n4. **NLP 术语壁垒** [should-fix] — R2 首提，R1 AGREE\n5. **Contribution 3 深度不足** [should-fix] — R2 首提，R1 AGREE\n6. **ASV vs E-value 框架重新定位** [should-fix] — R2 首提，R1 AGREE with nuance\n7. **Figure 2 灰度可辨识性** [minor] — R2 首提，R1 AGREE\n8. **Significance ASV N-dependence** [should-fix] — R1 首提，R2 AGREE\n9. **Conjecture 1 ε 理论直觉** [should-fix] — R1 首提，R2 AGREE\n\n---\n\n## Reviewer Divergence\n\n以下问题存在严重性分级分歧（**Director 已裁决**）：\n\n| 问题 | R1 判断 | R2 判断 | Director 裁决 | 理由 |\n|------|---------|---------|---------------|------|\n| 比例效应 f=λg 假设论证 | critical | should-fix (REBUT) | **should-fix（高优先级）** | R2 论证有力：假设仅影响 Theorem 1 monotonicity，Proposition 3 提供 fallback，97.3% 实证保持率 |\n| 页数超限 | should-fix (M5) | must-fix (N1) | **must-fix** | 格式合规是硬约束，修复成本极低 |\n| K≥3 monotonicity 理论缺口 | strong should-fix | must-fix (N2) | **should-fix（高优先级）** | K≥3 贡献多维（偏差表达式 + sign preservation + FWL），不应仅以 monotonicity 证明缺口评判 |\n\n---\n\n## Questions\n\n汇总两位 Reviewer 的关键提问（供 author response 参考）：\n\n1. **ClinicalBERT case study 中是否检验了 f=λg？** 不同吸烟状态类别对死亡率的效应是否近似成比例？[R1-Q1]\n2. **2.7% 不满足 Theorem 1 条件的 LLM 配置有什么共同特征？** 是否与特定 LLM 或数据集相关？[R1-Q3]\n3. **Sign-flip ASV 的实际使用循环**：practitioners 需要先知道真实 τ 的符号才能计算 sign-flip ASV，如何处理这个 bootstrap 循环？[R2-Q3]\n4. **Logistic regression 下 FWL 破缺幅度对大 K 如何变化？** Table 5 只测试了 K=3。[R1-Q4]\n5. **多维 ASV 的可能性**：当前沿单一 C(δ) 路径搜索，是否考虑过 per-category sensitivity？[R1-Q5]\n6. **非差异假设的 stress test 含义**：ε=0.01 即导致 14/16 K≥3 exposure sign reversal，是否意味着论文分析对 differential misclassification 极其脆弱？[R2-Q4]\n\n---\n\n## Missing References\n\n- **Imai and Yamamoto (2010)**, \"Causal Inference with Differential Measurement Error\" — 与非差异假设形成对比 [R1 建议, R2 AGREE]\n- **Nguimkeu, Denteh & Tchernis (2019)**, \"On the estimation of treatment effects with endogenous misreporting\" — treatment misclassification 相关 [R2 建议]\n- **Ogburn and VanderWeele (2013)** — bias amplification under covariate misclassification 后续工作 [R1 建议, R2 指出 2012 版已引用]\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态**: 未请求。本项目未配置外部审稿。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**: error — 视觉审查 Agent 因 rate limit 未能完成检查（\"You've hit your limit · resets 4pm (UTC)\"）。用户可在 limit 重置后重新触发。\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.5 / 5 — Borderline Conference**\n\n| 维度 | R1 | R2 | 合并 |\n|------|----|----|------|\n| Soundness | 3.5 | 3.5 | 3.5 |\n| Excitement | 3.5 | 3.5 | 3.5 |\n| Reproducibility | 4.0 | 4.0 | 4.0 |\n| Confidence | 4 | 4 | 4 |\n\n**综合评语**：\n\n论文在统一框架内首次系统分析了多类别标注误差在 7 种 DAG 拓扑下的因果偏差传播，贡献真实（bias taxonomy + FWL invariance 负面结果）、验证充分（161 scenarios, 1.6% MAPE）、认知层级诚实。FWL 不变性证明和 F₁ 与因果 bias 无相关性的发现对实践者有直接价值。\n\n制约评分的主要因素：\n\n1. **Must-fix 阻塞项**：(a) 页数超限需压缩（修复成本低）；(b) 非差异错分类假设缺乏 Y-stratified 实证检验（修复需要实验工作，但在 HumAID 上可行）。\n\n2. **理论-应用鸿沟**：核心理论保证（Theorem 1 monotonicity）仅在 K=2 + proportional effects 下成立，而论文的核心卖点是 K≥3 的结构性新现象。虽然偏差表达式和 FWL 不变性对一般 K 成立（不依赖 Theorem 1），ASV 框架的 K≥3 保证仍是 conjectural。Contribution 2 需要更谨慎的定位。\n\n3. **受众适配**：面向 EMNLP 的论文使用大量计量经济学术语（plim、FWL、Wald estimator），NLP 读者的可达性不足。Correction guidance（Contribution 3）作为核心贡献之一但正文深度不匹配。\n\n**条件上调**：如果作者在 revision/rebuttal 中充分回应 MF-2（Y-stratified 检验）、SF-1（Contribution 2 重新定位）和 SF-4（术语直觉解释），评分可上调至 **4.0（Conference）**。MF-1（页数超限）是纯排版修复，不影响学术评价。\n\n---\n\n## Detailed Comments\n\n### Section-by-Section\n\n**Abstract**: 184 words 符合 ≤200 限制（R17 已验证）。信息密度高但主要结论完整。建议减少具体数字（保留 83.4% sign reversal 和 1.6% MAPE 两个核心数字即可）。FWL invariance 声明建议加 \"under linear OLS\" 限定。\n\n**Introduction**: 三大贡献清晰列出。\"first unified analysis\" claim 在当前文献范围内成立（R1 确认），但限定词过多，建议简化措辞。Contribution 3 的正文深度需与定位匹配。\n\n**Related Work**: 覆盖全面，四个关键领域（measurement error、LLM annotation、sensitivity analysis、correction methods）均有充分引用。可考虑补充 Imai & Yamamoto (2010) 和 Nguimkeu et al. (2019)。\n\n**Method (Section 3)**: 核心理论贡献所在。Bias expressions (公式 1-5) 推导清晰。Theorem 1 → Observation 1 → Conjecture 1 层次诚实。主要问题：(1) 术语壁垒（plim、FWL、Wald 等需直觉解释）；(2) proportional effects 假设缺 NLP 场景讨论；(3) Remark 1 的 ASV-E-value 比较需重新框定为互补工具。\n\n**Experiments (Section 4)**: 验证充分（161 scenarios, 1.6% MAPE）。Empirical validation 使用 3 个真实 NLP 数据集和 23 个 LLM 配置。F₁ 无预测因果 bias 的发现有力。主要问题：(1) Correction guidance (Section 4.5) 深度不足；(2) logistic regression 讨论不充分；(3) Significance ASV 的 N-dependence 需更系统展示。\n\n**Conclusion + Limitations**: Conclusion 需压缩（当前导致超页）。Limitations 覆盖三个点（non-differential 假设、linear SEM、C 可估计性），位置正确（正文内）。\n\n**Appendix**: 24 页，B.1-B.24 共 24 个子节，验证详尽。FWL 证明（B.2）完整。Logistic regression 验证（B.7, B.14）存在但主文未充分引用。交叉引用密集但结构清晰。",
  "project": "causal_annot_error_attrib",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.5 - Borderline Conference",
  "review_chat_id": "oc_9f117624057fcf6cb95db4d67f525246"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# 审稿报告：Round 18（Fresh Review）\n\n**论文**: Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction\n**Venue**: EMNLP 2026 (ARR Long Paper)\n**审稿模式**: Fresh（重新审稿）\n**Reviewer**: R1（方法严谨性）+ R2（新颖性/完整性）\n**日期**: 2026-05-23\n\n---\n\n## Summary\n\n本文研究 LLM 标注器产生的多类别标注误差（K≥3）如何在 7 种典型因果 DAG 拓扑下传播到下游因果估计。核心贡献包括：(1) 在非差异错分类假设下推导 7 种拓扑的闭式偏差表达式，建立 sign-preservation/reversal 二分法（5 种拓扑保持符号，exposure 和 IV 可逆转）；(2) 定义 Annotation Sensitivity Values (ASV) 框架，包含幅度、显著性和符号翻转三种诊断，揭示从 IV（最脆弱）到 M-bias（免疫）的拓扑依赖脆弱性谱；(3) 证明 FWL 不变性使得矩阵校正方法在四种协变量拓扑下精确无效（0% bias reduction），并评估 5 种校正方法。论文通过 Monte Carlo 模拟（161 场景，grand MAPE 1.6%）和 23 个真实 LLM 配置（HumAID K=10, VAST K=3, CivilComments K=2）进行实证验证。\n\n---\n\n## Strengths\n\n**S1. 真正的统一拓扑分析**: 首次在统一框架内系统比较同一 confusion matrix 在 7 种 DAG 拓扑下产生定性不同的偏差。sign-preservation/reversal 二分法是一个清晰有力的核心发现，填补了流行病学测量误差理论与 NLP 实践之间的缺口。[R1-S1, R2-Strength-1, 共识]\n\n**S2. FWL 不变性负面结果**: 证明矩阵校正方法（confusion matrix inversion）对 4 种协变量拓扑的 bias reduction 为精确 0%——这是一个干净、完整的结构性结果（Appendix B.2 列空间论证），对实践者有直接警示意义。[R1-S3, R2-Strength-2, 共识]\n\n**S3. 诚实的认知层级**: Proved（K=2, Theorem 1）→ Verified（K≥3, Observation 1）→ Conjectured（Conjecture 1）的三级层次在理论论文中值得赞赏，避免了对 K≥3 结果的过度声称。[R1-S2, R2-Strength-4, 共识]\n\n**S4. 全面的实证验证**: 161 scenarios × 23 LLM configurations × 3 NLP tasks；100,000 Dirichlet matrices；theory-MC MAPE 1.6%（per-topology 0.3%-3.7%）。F₁ 与因果 bias 无显著相关性（Spearman ρ = -0.10, p = 0.45）的发现对 CSS 研究者有直接可操作价值。[R1-S4, R2-Strength-3/5, 共识]\n\n**S5. 实用决策框架**: ASV 与 E-value 类比设计得当，Algorithm 1 的拓扑感知校正决策树为实践者提供清晰操作指南。[R1-S5]\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**MF-1** [format] **正文页数超出 EMNLP 2026 strict 8-page limit**\n- Section 5 Conclusion 完整位于第 9 页（约 13-14 行主文内容溢出）。EMNLP 2026 strict 8-page limit 是硬约束，违规可致 desk rejection。\n- R2 首提为 critical，R1 交叉确认违规存在但建议降级。**Director 裁决 must-fix**：格式合规是硬约束，修复成本极低（压缩 Section 4.5 + 精简 Conclusion）。\n- 修复方案：(a) 精简 Section 4.5 \"Case studies and sensitivity\" 段落（细节已在 Appendix）；(b) Conclusion 压缩至 5-6 行；(c) 或将 Figure 4/5 之一移至 Appendix。\n\n**MF-2** [soundness] **非差异错分类假设在 LLM 标注器语境下缺乏直接实证检验**\n- Definition 1 要求 P(A*=j|A=k,Y) = P(A*=j|A=k)。LLM 预训练数据编码 A-Y 关联，可能系统性违反此假设。现有检验不充分：Appendix B.5 VAST topic-stratified 检验仅一个数据集，且 topic 分层 ≠ Y 分层；Appendix B.6/B.8 stress test 显示 ε=0.01 structured departure 即导致 14/16 K≥3 exposure 配置 sign reversal。\n- R1 首提为 critical，R2 交叉 AGREE（但补充结构性论证——LLM API 不观测 Y——比 R1 承认的更强）。**共识 must-fix**。\n- 修复方案：在至少一个有 gold labels 的 NLP 数据集上，按 Y 值分层计算 LLM 错分类矩阵，直接检验 P(A*|A,Y=0) ≈ P(A*|A,Y=1)。即使只做一个数据集（如 HumAID），也能为结构性论证提供 empirical backing。\n\n### Should-Fix（影响评分但不一票否决）\n\n**SF-1** [soundness, 高优先级] **K≥3 ASV monotonicity 仅为 Conjecture，削弱 Contribution 2 的理论定位**\n- Theorem 1（envelope monotonicity）仅在 K=2 + proportional effects 下证明。K≥3 依赖 Observation 1（数值验证，ε<0.02）和 Conjecture 1。论文核心论点是 K≥3 引入结构性新现象，但其 ASV 框架恰恰无法为 K≥3 提供形式化保证。\n- R2 首提为 critical，R1 交叉 AGREE with nuance（K≥3 贡献多维——偏差表达式、sign preservation、FWL 均对一般 K 成立，不仅限于 monotonicity；ε<0.02 使 ASV 误差在 2% 以内）。**Director 裁决 should-fix（高优先级）**：R1 论点有力，K≥3 贡献确实不仅限于 monotonicity。\n- 修复方案：(a) 将 Contribution 2 重新表述为 \"empirically validated diagnostic with proved K=2 foundation\"；(b) 补充 monotonicity failure 的后果分析（如果 ε 达到极端值，对 ASV ranking 的影响有多大）。\n\n**SF-2** [soundness, 高优先级] **比例效应假设 (f=λg) 在 NLP 场景下缺乏具体讨论**\n- Theorem 1 依赖 f=λg。在 NLP 多类别处理（如 stance detection 的 favor/against/neutral）中，不同类别可能有质性不同的效应，不满足比例关系。论文仅一句话提及 \"plausible in NLP tasks with a single quality dimension\"。\n- R1 首提为 critical，R2 REBUT 降为 should-fix（假设仅影响 Theorem 1 monotonicity，Proposition 3 提供 general case fallback，97.3% 实证保持率）。**Director 采纳 should-fix（高优先级）**：R2 论证有力——假设范围比 R1 描述的更窄。\n- 修复方案：增加 2-3 句具体 NLP 因果推断场景的分析（如 stance detection 3-class 是否接近 proportional）。\n\n**SF-3** [scope] **Logistic regression 讨论不充分**\n- NLP 最常用 logistic regression。主文仅一句话提及 FWL invariance 在 logistic 下的破缺（Section 4.5）。Appendix B.14 显示 FWL 破缺幅度随 accuracy 增大（exposure: -22% to -78%）。Algorithm 1 未区分 OLS/logistic 路径。\n- R1 首提，R2 强烈同意。**共识 should-fix**。\n- 修复方案：Section 4.5 增加 1-2 段 logistic regression 指导，引用 Appendix B.2/B.7/B.14；Algorithm 1 增加 OLS/logistic 分支。\n\n**SF-4** [presentation, 高优先级] **术语壁垒对 NLP 读者可达性不足**\n- plim、FWL theorem、Wald estimator、column-stochastic matrix、Birkhoff polytope、Dirichlet prior——对 EMNLP 受众属于高门槛术语，直觉解释不充分。如果多数 reviewer 无法流畅理解 method section，将影响 soundness 和 confidence 打分。\n- R2 首提，R1 交叉 AGREE。**共识 should-fix**。\n- 修复方案：每个关键术语首次使用时增加 1-2 句直觉解释（约增 6-8 行，页数压缩后有空间）。\n\n**SF-5** [presentation] **Contribution 3（correction guidance）正文深度与\"贡献\"定位不匹配**\n- \"Topology-aware correction guidance\" 被列为三大贡献之一，但正文仅约 0.7 页。Algorithm 1 仅在 Appendix。与 Contribution 1（~3 页 method）和 Contribution 2（~1.5 页 ASV + experiments）相比深度不足。\n- R2 首提，R1 交叉 AGREE（倾向降级为 practical implication）。**共识 should-fix**。\n- 修复方案：(a) 将 Algorithm 1 提升至正文（需结合 MF-1 的压缩方案）；或 (b) 降级为 \"practical implication\" 而非 co-equal contribution。\n\n**SF-6** [novelty] **ASV 与 E-value 的比较框架有误导性**\n- Remark 1 的三点 \"structural distinctions from E-values\" 本质上是不同工具解决不同问题（annotation error vs. unmeasured confounding）。当前表述暗示 ASV 是 E-values 的改进版。ASV 的真正贡献是将 sensitivity analysis 范式适配到 annotation error + topology dependence。\n- R2 首提，R1 交叉 AGREE with nuance（distinctions 准确但表述暗含 improvements over）。**共识 should-fix**。\n- 修复方案：Remark 1 重新框定为互补工具（complementary tools for different sources of bias）。\n\n**SF-7** [experiments] **Dirichlet(1,1,...,1) 采样对高维 K 代表性不足**\n- K=5（20 参数）和 K=7（42 参数）下，均匀 Dirichlet 采样偏离实际 LLM 矩阵分布（对角线期望 1/K vs 实际 >0.6）。R2 补充：23 个经验 LLM 矩阵已验证核心结论，代表性问题不影响最终结论。\n- R1 首提，R2 交叉 AGREE。**共识 should-fix（低优先级）**。\n- 修复方案：补充 Dirichlet(α,1,...,1) (α>>1) 采样验证，或报告对角线 >0.6 子空间的 ε 值。\n\n**SF-8** [method] **Significance ASV 对样本量 N 的依赖未充分探讨**\n- δ_sig 通过 SE(N) 依赖于 N，Figure 3 仅展示单一 N 值。不同 N 下 significance ASV 的变化是 practitioners 的关键决策信息。\n- R1 首提，R2 交叉 AGREE。**共识 should-fix**。\n- 修复方案：增加不同 N（如 1K, 5K, 10K, 50K）下各拓扑 δ*_sig 变化的可视化（Figure 或 Table）。\n\n**SF-9** [soundness] **Conjecture 1 的 ε<0.02 约束缺乏理论直觉**\n- ε 约束完全来自数值实验，论文未解释为什么 ε 应该很小。R2 补充可能的直觉路径：proportional effects 下精确单调，deviations 来自 non-proportional residual。\n- R1 首提，R2 交叉 AGREE。**共识 should-fix**。\n- 修复方案：补充 1 段关于 ε 小的直觉论证（如与列随机矩阵空间的凸体结构或 proportional residual 分析相关）。\n\n### Minor（不影响接收）\n\n1. **Abstract 信息密度过高**：约 184 words 符合 ≤200 限制，但 7+ 具体数字首次阅读难以消化。建议精简至 2-3 个最具冲击力的数字。[R2-minor-2, R1 AGREE]\n2. **Figure 2 灰度打印可辨识性**：红色 sign reversal 标识在灰度下难以区分，建议增加 hatching/pattern fill。[R2-W4, R1 AGREE]\n3. **τ 符号 overloading**：τ 在不同拓扑下含义不同但未充分标注。[R2-minor-1, R1 AGREE]\n4. **Orphan bib entries**：manski1990 未在正文引用，应移除或添加引用。[R2-minor-3]\n5. **引用格式不一致**：部分 bib 条目缺 doi 或页码。[R2-minor-4]\n6. **\"First unified analysis\" 措辞**：限定词过多，建议简化为 \"first systematic topology-specific comparison\"。[R2-W5, R1 partial REBUT: claim 有合理基础但措辞可优化]\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 达成共识（[AGREE] 或交叉后无争议）：\n\n1. **非差异错分类假设需要 Y-stratified 实证检验** [must-fix] — R1 首提，R2 AGREE\n2. **页数超限需修复** [must-fix (R2) / should-fix (R1)] — 违规存在无争议，仅严重性有分歧\n3. **Logistic regression 讨论不充分** [should-fix] — R1 首提，R2 强烈同意\n4. **NLP 术语壁垒** [should-fix] — R2 首提，R1 AGREE\n5. **Contribution 3 深度不足** [should-fix] — R2 首提，R1 AGREE\n6. **ASV vs E-value 框架重新定位** [should-fix] — R2 首提，R1 AGREE with nuance\n7. **Figure 2 灰度可辨识性** [minor] — R2 首提，R1 AGREE\n8. **Significance ASV N-dependence** [should-fix] — R1 首提，R2 AGREE\n9. **Conjecture 1 ε 理论直觉** [should-fix] — R1 首提，R2 AGREE\n\n---\n\n## Reviewer Divergence\n\n以下问题存在严重性分级分歧（**Director 已裁决**）：\n\n| 问题 | R1 判断 | R2 判断 | Director 裁决 | 理由 |\n|------|---------|---------|---------------|------|\n| 比例效应 f=λg 假设论证 | critical | should-fix (REBUT) | **should-fix（高优先级）** | R2 论证有力：假设仅影响 Theorem 1 monotonicity，Proposition 3 提供 fallback，97.3% 实证保持率 |\n| 页数超限 | should-fix (M5) | must-fix (N1) | **must-fix** | 格式合规是硬约束，修复成本极低 |\n| K≥3 monotonicity 理论缺口 | strong should-fix | must-fix (N2) | **should-fix（高优先级）** | K≥3 贡献多维（偏差表达式 + sign preservation + FWL），不应仅以 monotonicity 证明缺口评判 |\n\n---\n\n## Questions\n\n汇总两位 Reviewer 的关键提问（供 author response 参考）：\n\n1. **ClinicalBERT case study 中是否检验了 f=λg？** 不同吸烟状态类别对死亡率的效应是否近似成比例？[R1-Q1]\n2. **2.7% 不满足 Theorem 1 条件的 LLM 配置有什么共同特征？** 是否与特定 LLM 或数据集相关？[R1-Q3]\n3. **Sign-flip ASV 的实际使用循环**：practitioners 需要先知道真实 τ 的符号才能计算 sign-flip ASV，如何处理这个 bootstrap 循环？[R2-Q3]\n4. **Logistic regression 下 FWL 破缺幅度对大 K 如何变化？** Table 5 只测试了 K=3。[R1-Q4]\n5. **多维 ASV 的可能性**：当前沿单一 C(δ) 路径搜索，是否考虑过 per-category sensitivity？[R1-Q5]\n6. **非差异假设的 stress test 含义**：ε=0.01 即导致 14/16 K≥3 exposure sign reversal，是否意味着论文分析对 differential misclassification 极其脆弱？[R2-Q4]\n\n---\n\n## Missing References\n\n- **Imai and Yamamoto (2010)**, \"Causal Inference with Differential Measurement Error\" — 与非差异假设形成对比 [R1 建议, R2 AGREE]\n- **Nguimkeu, Denteh & Tchernis (2019)**, \"On the estimation of treatment effects with endogenous misreporting\" — treatment misclassification 相关 [R2 建议]\n- **Ogburn and VanderWeele (2013)** — bias amplification under covariate misclassification 后续工作 [R1 建议, R2 指出 2012 版已引用]\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态**: 未请求。本项目未配置外部审稿。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**: error — 视觉审查 Agent 因 rate limit 未能完成检查（\"You've hit your limit · resets 4pm (UTC)\"）。用户可在 limit 重置后重新触发。\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.5 / 5 — Borderline Conference**\n\n| 维度 | R1 | R2 | 合并 |\n|------|----|----|------|\n| Soundness | 3.5 | 3.5 | 3.5 |\n| Excitement | 3.5 | 3.5 | 3.5 |\n| Reproducibility | 4.0 | 4.0 | 4.0 |\n| Confidence | 4 | 4 | 4 |\n\n**综合评语**：\n\n论文在统一框架内首次系统分析了多类别标注误差在 7 种 DAG 拓扑下的因果偏差传播，贡献真实（bias taxonomy + FWL invariance 负面结果）、验证充分（161 scenarios, 1.6% MAPE）、认知层级诚实。FWL 不变性证明和 F₁ 与因果 bias 无相关性的发现对实践者有直接价值。\n\n制约评分的主要因素：\n\n1. **Must-fix 阻塞项**：(a) 页数超限需压缩（修复成本低）；(b) 非差异错分类假设缺乏 Y-stratified 实证检验（修复需要实验工作，但在 HumAID 上可行）。\n\n2. **理论-应用鸿沟**：核心理论保证（Theorem 1 monotonicity）仅在 K=2 + proportional effects 下成立，而论文的核心卖点是 K≥3 的结构性新现象。虽然偏差表达式和 FWL 不变性对一般 K 成立（不依赖 Theorem 1），ASV 框架的 K≥3 保证仍是 conjectural。Contribution 2 需要更谨慎的定位。\n\n3. **受众适配**：面向 EMNLP 的论文使用大量计量经济学术语（plim、FWL、Wald estimator），NLP 读者的可达性不足。Correction guidance（Contribution 3）作为核心贡献之一但正文深度不匹配。\n\n**条件上调**：如果作者在 revision/rebuttal 中充分回应 MF-2（Y-stratified 检验）、SF-1（Contribution 2 重新定位）和 SF-4（术语直觉解释），评分可上调至 **4.0（Conference）**。MF-1（页数超限）是纯排版修复，不影响学术评价。\n\n---\n\n## Detailed Comments\n\n### Section-by-Section\n\n**Abstract**: 184 words 符合 ≤200 限制（R17 已验证）。信息密度高但主要结论完整。建议减少具体数字（保留 83.4% sign reversal 和 1.6% MAPE 两个核心数字即可）。FWL invariance 声明建议加 \"under linear OLS\" 限定。\n\n**Introduction**: 三大贡献清晰列出。\"first unified analysis\" claim 在当前文献范围内成立（R1 确认），但限定词过多，建议简化措辞。Contribution 3 的正文深度需与定位匹配。\n\n**Related Work**: 覆盖全面，四个关键领域（measurement error、LLM annotation、sensitivity analysis、correction methods）均有充分引用。可考虑补充 Imai & Yamamoto (2010) 和 Nguimkeu et al. (2019)。\n\n**Method (Section 3)**: 核心理论贡献所在。Bias expressions (公式 1-5) 推导清晰。Theorem 1 → Observation 1 → Conjecture 1 层次诚实。主要问题：(1) 术语壁垒（plim、FWL、Wald 等需直觉解释）；(2) proportional effects 假设缺 NLP 场景讨论；(3) Remark 1 的 ASV-E-value 比较需重新框定为互补工具。\n\n**Experiments (Section 4)**: 验证充分（161 scenarios, 1.6% MAPE）。Empirical validation 使用 3 个真实 NLP 数据集和 23 个 LLM 配置。F₁ 无预测因果 bias 的发现有力。主要问题：(1) Correction guidance (Section 4.5) 深度不足；(2) logistic regression 讨论不充分；(3) Significance ASV 的 N-dependence 需更系统展示。\n\n**Conclusion + Limitations**: Conclusion 需压缩（当前导致超页）。Limitations 覆盖三个点（non-differential 假设、linear SEM、C 可估计性），位置正确（正文内）。\n\n**Appendix**: 24 页，B.1-B.24 共 24 个子节，验证详尽。FWL 证明（B.2）完整。Logistic regression 验证（B.7, B.14）存在但主文未充分引用。交叉引用密集但结构清晰。",
    "project": "causal_annot_error_attrib",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.5 - Borderline Conference",
    "review_chat_id": "oc_9f117624057fcf6cb95db4d67f525246"
  }
}
```

</details>

---


### Tool result

_source line 1485 · 2026-05-23T15:44:47.415044+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_ca838cd3ed4c7e2d9c8e3459edd98b90:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 3816
}
```

</details>

---


### Tool call

_source line 1486 · 2026-05-23T15:45:00.189353+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 1: Reviewer 独立初审（R1 方法严谨性 + R2 新颖性完整性）', 'status': 'completed', 'activeForm': '等待两位 Reviewer 完成独立初审'}, {'content': 'Step 2: 交叉分享——将每位 Reviewer 原文转发给对方，收集逐条回应', 'status': 'completed', 'activeForm': '执行交叉分享'}, {'content': 'Step 3: 收敛判断——分析共识与分歧', 'status': 'completed', 'activeForm': '判断是否收敛'}, {'content': 'Step 4: 汇总报告——合成审稿报告、同步 Issue Tracker、投递', 'status': 'completed', 'activeForm': '汇总并投递审稿报告'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Step 1: Reviewer 独立初审（R1 方法严谨性 + R2 新颖性完整性）', 'status': 'completed', 'activeForm': '等待两位 Reviewer 完成独立初审'}, {'content': 'Step 2: 交叉分享——将每位 Reviewer 原文转发给对方，收集逐条回应', 'status': 'completed', 'activeForm': '执行交叉分享'}, {'content': 'Step 3: 收敛判断——分析共识与分歧', 'status': 'completed', 'activeForm': '判断是否收敛'}, {'content': 'Step 4: 汇总报告——合成审稿报告、同步 Issue Tracker、投递', 'status': 'completed', 'activeForm': '汇总并投递审稿报告'}]"
  }
}
```

</details>

---


### Tool result

_source line 1487 · 2026-05-23T15:45:00.189870+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---


### Assistant

_source line 1488 · 2026-05-23T15:45:14.690020+00:00_

Round 18 审稿完成。报告已投递至 Research Director。

**审稿结论**：**3.5/5 Borderline Conference**

**核心发现**：
- **2 个 Must-Fix**：(1) 正文超 8 页限制（修复成本极低）；(2) 非差异错分类假设缺乏 Y-stratified 实证检验（需在 HumAID 等数据集上做按 Y 分层的 confusion matrix 比较）
- **9 个 Should-Fix**：K≥3 monotonicity 需重新定位 Contribution 2、比例效应假设需 NLP 场景讨论、logistic regression 指导不足、NLP 术语壁垒、Contribution 3 深度不匹配、ASV-E-value 框架重新定位、Dirichlet 采样代表性、significance ASV N-dependence、Conjecture 1 ε 理论直觉
- **6 个 Minor**：Abstract 数字密度、Figure 2 灰度、τ overloading、orphan bib entries、引用格式、novelty claim 措辞
- **条件上调至 4.0**：如 rebuttal 充分回应 MF-2 + SF-1 + SF-4

视觉审查因 rate limit 未完成，结果会在 limit 重置后自动补发到 Group C。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 151

## Round 151

2 recorded events


### User

_source line 1489 · 2026-05-23T15:45:17.305135+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交给 Review Director。

总结：对 R1 的 14 个具体问题，我给出了 **8 个 [AGREE]、4 个 [REBUT]、2 个部分同意**。核心分歧在三点：

1. **R1-N1（proportional effects）应降级**：假设仅影响 Theorem 1 monotonicity，不影响 bias taxonomy 或 sign preservation（Proposition 3 提供 general case fallback），且 97.3% sign preservation 在 non-proportional 下已验证。

2. **R1-M5（页数超限）应升级**：从"小问题"升为 must-fix——Section 5 在第 9 页上有约 13-14 行主文，是明确的格式违规。

3. **R1-M2（Figure 2 仅 K=3）过度批评**：Appendix B.9 有完整 cross-K 验证，主文有明确交叉引用。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1490 · 2026-05-23T15:45:30.463885+00:00_

Round 18 审稿完毕。

**最终结果**：3.5/5 Borderline Conference。报告和 Issue Tracker 已投递至 Research Director。

核心发现：
- **2 个 Must-Fix**：(1) 正文超 8 页需压缩；(2) 非差异错分类假设需 Y-stratified 实证检验
- **9 个 Should-Fix**：K≥3 monotonicity 定位调整、proportional effects NLP 讨论、logistic regression 指导、NLP 术语壁垒、Contribution 3 深度、ASV vs E-value 框架、Dirichlet 采样、Significance ASV N-dependence、Conjecture 1 理论直觉
- **条件上调至 4.0**：如充分回应 MF-2 + SF-1 + SF-4

视觉审查因 rate limit 未完成，完成后会自动补发到 Group C。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 152

## Round 152

72 recorded events


### User

_source line 1491 · 2026-05-23T16:56:33.454041+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: causal_annot_error_attrib
- 论文路径: /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: ARR Long Paper
- 截止日期: 2026-05-25
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 1492 · 2026-05-23T16:56:38.366946+00:00_

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
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 1493 · 2026-05-23T16:56:38.451993+00:00_

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
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 85
}
```

</details>

---


### Tool call

_source line 1494 · 2026-05-23T16:56:49.212784+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__get_visual_check_status",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__get_visual_check_status",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 1495 · 2026-05-23T16:56:49.213396+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1496 · 2026-05-23T16:56:49.464533+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,WebFetch,TodoWrite",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,WebFetch,TodoWrite",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 1497 · 2026-05-23T16:56:49.615555+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "ToolSearch",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 1498 · 2026-05-23T16:57:00.518980+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'in_progress', 'activeForm': '执行资料检查和 Venue 调研'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'pending', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.6/0.7: 派发外部审稿 + 视觉审查', 'status': 'pending', 'activeForm': '派发外部审稿和视觉审查'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'pending', 'activeForm': '等待 Reviewer 独立审稿'}, {'content': 'Step 2: 交叉分享', 'status': 'pending', 'activeForm': '执行交叉分享'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断收敛'}, {'content': 'Step 4: 汇总报告 & 投递', 'status': 'pending', 'activeForm': '汇总报告并投递'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'in_progress', 'activeForm': '执行资料检查和 Venue 调研'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'pending', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.6/0.7: 派发外部审稿 + 视觉审查', 'status': 'pending', 'activeForm': '派发外部审稿和视觉审查'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'pending', 'activeForm': '等待 Reviewer 独立审稿'}, {'content': 'Step 2: 交叉分享', 'status': 'pending', 'activeForm': '执行交叉分享'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断收敛'}, {'content': 'Step 4: 汇总报告 & 投递', 'status': 'pending', 'activeForm': '汇总报告并投递'}]"
  }
}
```

</details>

---


### Tool result

_source line 1499 · 2026-05-23T16:57:00.519418+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1500 · 2026-05-23T16:57:00.971517+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "causal_annot_error_attrib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "causal_annot_error_attrib"
  }
}
```

</details>

---


### Tool result

_source line 1501 · 2026-05-23T16:57:01.926630+00:00_

{"result":"# 项目 causal_annot_error_attrib 概况\n\n## 实验状态 (14 个)\n\n- **plan006_asv_empirical**: DONE (success) — \n- **plan010_annot_sensitivity_toolkit**: DONE (success) — \n- **plan003_empirical_confusion_matrices**: DONE (failed) — \n- **plan007_correction_guidance**: DONE (success) — \n- **plan009_pathological_matrices**: DONE (success) — \n- **plan005_asv_extended**: DONE (success) — \n- **plan002_k57_extension**: DONE (success) — \n- **plan001_dag_taxonomy**: DONE (success) — \n- **plan004_asv_framework**: DONE (success) — \n- **plan_004_asv_v3_fixed**: DONE (success) — \n- **plan008_binarization_collapse**: DONE (success) — \n- **mvp_exposure_dirichlet_subspace**: DONE (success) — \n- **mvp_exposure_dag**: DONE (success) — \n- **mvp_confounding_dag**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-21\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n（无）\n\n## 近期结论\n- **plan006_asv_empirical** (success): 真实 LLM confusion matrices（跨 K=2/3/10，跨 7B/235B 模型）在 7 种 DAG 拓扑下的偏差传播与理论预测一致：(1) F1 高不代表因果估计安全（F1=0.72 但 IV bias>100%），(2) 0 sign flips 确认结构性保证，(3) topology（非 K 或 model size）是 bias 的主要决定因素。\n- **plan010_annot_sensitivity_toolkit** (success): 封装 7-topology bias computation、ASV sensitivity framework 和 5 种 correction 方法为可复用 Python 包，使 practitioners 能用 3 行代码评估 LLM 标注误差对因果推断的影响。验证：(1) API 输出与 plan_001/004/005/007 原始脚本一致，(2) worked example 展示完整工作流，(3) 35 个 pytest 全通过。\n- **plan003_empirical_confusion_matrices** (failed): Different LLMs (Llama-4-Maverick, Qwen3-235B, DeepSeek-Chat) produce systematically different confusion matrices on the same classification tasks, and these empirical confusion matrices can be used to quantify annotation error propagation in downstream causal inference.\n\n## 趋势\n成功 13 / 负向 0 / 失败 1 / 共 14\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nhome-1x5090: 无 GPU 信息\n\n## 告警\n- plan003_empirical_confusion_matrices: 训练失败 — unknown"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 955
}
```

</details>

---


### Tool call

_source line 1502 · 2026-05-23T16:57:02.077672+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers ARR submission guidelines page limit site:aclweb.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers ARR submission guidelines page limit site:aclweb.org"
  }
}
```

</details>

---


### Tool call

_source line 1503 · 2026-05-23T16:57:04.339032+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/main.tex /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_19/submitted.pdf 2>&1",
  "description": "Check paper files exist"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/main.tex /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_19/submitted.pdf 2>&1",
    "description": "Check paper files exist"
  }
}
```

</details>

---


### Tool result

_source line 1504 · 2026-05-23T16:57:04.842307+00:00_

-rw-r--r-- 1 ubuntu ubuntu 937461 May 23 16:52 /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_19/submitted.pdf
-rw-r--r-- 1 ubuntu ubuntu   1551 May 23 13:23 /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/main.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Bash",
  "elapsed_ms": 503
}
```

</details>

---


### Tool call

_source line 1505 · 2026-05-23T16:57:05.044323+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_issues.yaml 2>&1 | head -100",
  "description": "Read existing review issues tracker"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_issues.yaml 2>&1 | head -100",
    "description": "Read existing review issues tracker"
  }
}
```

</details>

---


### Tool result

_source line 1506 · 2026-05-23T16:57:05.145427+00:00_

issues:
  # === Round 1-7 历史 (resolved，保留摘要) ===

  - id: R1-N1
    category: soundness
    severity: must-fix
    summary: "Theorem 1 适用范围过窄（仅 confounding+proportional effects），K≥3 证明不完整"
    status: resolved
    first_raised_round: 1
    last_seen_round: 7
    resolution: "Theorem 1 现正确限定为 K=2；K≥3 由 Observation 1 和 Conjecture 1 覆盖。"
    resolution_round: 7

  - id: R1-N2
    category: soundness
    severity: should-fix
    summary: "3/5 安全拓扑的符号保持仅有数值验证，Abstract 用 'establish' 暗示已证明"
    status: resolved
    first_raised_round: 1
    last_seen_round: 3
    resolution: "Abstract 已准确区分 prove/verify。"
    resolution_round: 4

  - id: R1-N3
    category: soundness
    severity: must-fix
    summary: "ASV C(δ) 定义域错误"
    status: resolved
    first_raised_round: 1
    last_seen_round: 1
    resolution: "Section 3.3 已引入 δ_max 约束。"
    resolution_round: 2

  - id: R2-N1
    category: presentation
    severity: must-fix
    summary: "83.4% sign reversal headline framing 过度声称"
    status: resolved
    first_raised_round: 1
    last_seen_round: 5
    resolution: "Introduction 已重写。"
    resolution_round: 5

  - id: R2-N2
    category: novelty
    severity: should-fix
    summary: "'first systematic framework' 过度声明"
    status: resolved
    first_raised_round: 1
    last_seen_round: 1
    resolution: "已修复。"
    resolution_round: 2

  - id: R2-N3
    category: related_work
    severity: must-fix
    summary: "4 篇关键相关工作未引用"
    status: resolved
    first_raised_round: 1
    last_seen_round: 1
    resolution: "已修复。"
    resolution_round: 2

  - id: R1-W2
    category: clarity
    severity: should-fix
    summary: "Sign preservation 的 DGP 条件在实践中难以事前验证"
    status: resolved
    first_raised_round: 1
    last_seen_round: 2
    resolution: "Section 3.2 已添加 ASV 替代讨论。"
    resolution_round: 3

  - id: R1-W3
    category: experiments
    severity: should-fix
    summary: "实证验证不完整：缺少商业 LLM"
    status: in_progress
    first_raised_round: 1
    last_seen_round: 18
    mentions:
      - roun
…[truncated 567 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Bash",
  "elapsed_ms": 101
}
```

</details>

---


### Tool result

_source line 1507 · 2026-05-23T16:57:06.954794+00:00_

Web search results for query: "EMNLP 2026 call for papers ARR submission guidelines page limit site:aclweb.org"

Links: [{"title":"EMNLP 2025: Call for System Demonstrations | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-call-system-demonstrations"},{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"Call for Papers: The 20th Linguistic Annotation Workshop (LAW XX), co-located with ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-20th-linguistic-annotation-workshop-law-xx-co-located-acl-2026"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"Industry Track — Call for Papers @ EACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/industry-track-call-papers-eacl-2026"},{"title":"First Call for Papers – EACL 2026 Student Research Workshop (SRW) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/first-call-papers-eacl-2026-student-research-workshop-srw"},{"title":"The 64th Annual Meeting of the Association for Computational Linguistics - ACL 2026","url":"https://2026.aclweb.org/"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"}]

I searched for information about EMNLP 2026 call for papers, ARR submission guidelines, and page limits on aclweb.org, but the results primarily return information about EMNLP 2025 and other
…[truncated 970 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "WebSearch",
  "elapsed_ms": 4877
}
```

</details>

---


### Tool call

_source line 1508 · 2026-05-23T16:57:12.732319+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_issues.yaml 2>&1 | tail -n +100",
  "description": "Read rest of review issues tracker"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_issues.yaml 2>&1 | tail -n +100",
    "description": "Read rest of review issues tracker"
  }
}
```

</details>

---


### Tool result

_source line 1509 · 2026-05-23T16:57:13.737873+00:00_

    resolution: ""
    resolution_round: null

  - id: R2-W2
    category: presentation
    severity: should-fix
    summary: "98 场景 zero sign reversals 与 sign reversal narrative 的 tension"
    status: resolved
    first_raised_round: 1
    last_seen_round: 1
    resolution: "已解决。"
    resolution_round: 2

  - id: R2-W3
    category: method
    severity: should-fix
    summary: "ASV 对 C₀ 估计不确定性的敏感性"
    status: resolved
    first_raised_round: 1
    last_seen_round: 2
    resolution: "Bootstrap ASV 分析已完成。"
    resolution_round: 3

  - id: R2-W4
    category: scope
    severity: should-fix
    summary: "线性 SEM 假设限制；Algorithm 1 缺 linear-only caveat"
    status: resolved
    first_raised_round: 1
    last_seen_round: 5
    resolution: "Section 4.5 FWL 段加 'Under linear OLS' 限定。"
    resolution_round: 5

  - id: R1-W4
    category: experiments
    severity: should-fix
    summary: "MC MAPE 报告不充分"
    status: resolved
    first_raised_round: 1
    last_seen_round: 1
    resolution: "已修复。"
    resolution_round: 2

  - id: MISC-1
    category: presentation
    severity: minor
    summary: "符号不统一（τ vs β_T）、Proposition 编号不一致"
    status: resolved
    first_raised_round: 1
    last_seen_round: 5
    resolution: "method.tex 添加 τ 在各拓扑下含义的明确说明。"
    resolution_round: 5

  - id: NEW-1
    category: soundness
    severity: must-fix
    summary: "Non-differential misclassification 假设讨论不足"
    status: in_progress
    first_raised_round: 2
    last_seen_round: 18
    mentions:
      - round: 14
        reviewers: [R1, R2]
        note: "R14 共识 minor。"
      - round: 15
        reviewers: [R1, R2]
        note: "R15 共识 should-fix。"
      - round: 16
        reviewers: [R1, R2]
        note: "R16 R1-W1 + R2-Q2 再提。"
      - round: 17
        reviewers: [R1, R2]
        note: "R17 共识 should-fix。"
      - round: 18
        reviewers: [R1, R2]
        note: "R18 升级为 must-fix。R1 指出 VAST topic-stratified 检验不等于 Y-stratified 检验，stress test 未回答真实 ε 是多少。R2 交叉 AGREE 但补充结构性论证（LLM API 不观测 Y）比 R1 承认的
…[truncated 18286 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Bash",
  "elapsed_ms": 1005
}
```

</details>

---


### Tool call

_source line 1510 · 2026-05-23T16:57:13.738461+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 submission guidelines page limit author instructions"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 submission guidelines page limit author instructions"
  }
}
```

</details>

---


### Tool call

_source line 1511 · 2026-05-23T16:57:13.839420+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 conference date location call for papers"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 conference date location call for papers"
  }
}
```

</details>

---


### Tool result

_source line 1512 · 2026-05-23T16:57:20.469274+00:00_

Web search results for query: "ACL Rolling Review 2026 submission guidelines page limit author instructions"

Links: [{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Author Guidelines for Student Research Workshop Papers -","url":"https://2026.eacl.org/calls/srw/guidelines/"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Paper formatting guidelines - ACLPUB","url":"https://acl-org.github.io/ACLPUB/formatting.html"},{"title":"Instructions for *ACL Proceedings","url":"https://arxiv.org/html/2506.06751v2"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"}]

Based on the search results, here's what I found about ACL Rolling Review 2026 submission guidelines regarding page limits and author instructions:

## Page Limits

Review versions of long papers may have up to eight (8) pages of content plus unlimited pages for references. The search results don't explicitly specify the page limit for short papers in the same context, but this appears to be the standard long paper requirement.

## Limitations Section

Since December 2023, a "Limitati
…[truncated 1156 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "WebSearch",
  "elapsed_ms": 6730
}
```

</details>

---


### Tool result

_source line 1513 · 2026-05-23T16:57:21.022292+00:00_

Web search results for query: "EMNLP 2026 conference date location call for papers"

Links: [{"title":"The 2026 Conference on Empirical Methods in Natural Language Processing - EMNLP 2026","url":"https://2026.emnlp.org/"},{"title":"EMNLP 2026 Call for Papers — Official Deadlines & Important Dates | PaperPilot","url":"https://www.getpaperpilot.com/deadlines/emnlp-2026.html"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"Update EMNLP 2026 conference dates and deadlines · huggingface/ai-deadlines at 2754f67","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/2754f67c0550847973789522a0a082dd5443b5c0"},{"title":"EMNLP 2026 Conference | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FConference"},{"title":"2026 *ACL Conference Dates | Computational Linguistics","url":"https://submissions.cljournal.org/index.php/cljournal/announcement/view/14"},{"title":"emnlp 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=emnlp26"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"AI Conference Deadlines - Jie Cao | Dialogue, NLP, ML","url":"https://mlciv.com/ai-deadlines/"}]

Based on the search results, here is the information about EMNLP 2026:

## Conference Dates and Location
EMNLP 2026 takes place in Budapest, Hungary from October 24 - 29, 2026.

## Call for Papers

EMNLP 2026 invites the submission of long and short papers featuring substantial, original, and unpublished research on empirical methods for Natural Language Processing. The conference aims to curate a diverse technical program—in addition to traditional research results, papers may contribute negative findings, survey an area, an
…[truncated 1041 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "WebSearch",
  "elapsed_ms": 7182
}
```

</details>

---


### Tool call

_source line 1514 · 2026-05-23T16:57:25.341902+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/cfp",
  "prompt": "Extract the complete submission guidelines including: page limits for long and short papers, formatting requirements, anonymity rules, appendix rules, limitations section requirements, and any other submission requirements."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/cfp",
    "prompt": "Extract the complete submission guidelines including: page limits for long and short papers, formatting requirements, anonymity rules, appendix rules, limitations section requirements, and any other submission requirements."
  }
}
```

</details>

---


### Tool call

_source line 1515 · 2026-05-23T16:57:26.497256+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://2026.emnlp.org/",
  "prompt": "Extract the full call for papers details including: submission deadlines, page limits, formatting requirements, review criteria, special theme, and any specific submission guidelines for EMNLP 2026."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://2026.emnlp.org/",
    "prompt": "Extract the full call for papers details including: submission deadlines, page limits, formatting requirements, review criteria, special theme, and any specific submission guidelines for EMNLP 2026."
  }
}
```

</details>

---


### Tool result

_source line 1516 · 2026-05-23T16:57:29.712122+00:00_

# EMNLP 2026 Call for Papers - Available Information

Based on the webpage content provided, I can only offer limited details about the call for papers:

## What's Available

The website confirms that a "First call for papers" was released on **February 27, 2026** and links to the main conference papers submission page. However, the specific submission guidelines are not included in the content excerpt provided.

## Key Deadlines Mentioned

- **ARR submission deadline**: May 25, 2026
- **Reviewer registration**: May 27, 2026
- **Author response period**: July 7-13, 2026
- **Meta review release**: July 30, 2026
- **Acceptance notification**: August 20, 2026
- **Camera-ready deadline**: September 20, 2026

**Important note**: "All deadlines are 11:59PM UTC-12:00 ('anywhere on Earth')"

## Missing Information

The page content does not include details about:
- Page limits
- Formatting requirements
- Review criteria
- Special themes
- Specific submission guidelines

To access complete submission details, you would need to visit the full call for papers at the linked page on the EMNLP 2026 website.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "WebFetch",
  "elapsed_ms": 3214
}
```

</details>

---


### Tool result

_source line 1517 · 2026-05-23T16:57:34.133707+00:00_

# ACL Rolling Review Submission Guidelines

## Page Limits

**Long Papers:**
- "up to eight (8) pages of content"
- Unlimited space for required limitations section and optional ethical considerations
- Unlimited reference pages

**Short Papers:**
- "up to four (4) pages of content"
- Unlimited space for required limitations section and optional ethical considerations
- Unlimited reference pages

Papers exceeding length requirements face desk rejection.

## Formatting Requirements

Submissions must adhere to official ACL style standards:
- Use the official ACL template from the designated GitHub repository
- Follow "*ACL" conference formatting guidelines
- Do not modify style files or use templates from other conferences
- Papers failing to meet style, size, margin, or font specifications are rejected without review

## Anonymity Rules

The review process is two-way anonymous:
- Exclude author names and affiliations from submissions
- Avoid self-references revealing identity (e.g., rephrase "We previously showed" as "Smith previously showed")
- Do not reference materials unavailable to reviewers
- Anonymize supplementary materials and repository links
- Avoid file-sharing services like Dropbox that track downloads

Anonymity violations result in desk rejection.

## Appendix Rules

Supplementary materials may include appendices, software, and data:
- Appendices follow main text after references
- Do not count toward page limits
- Must maintain anonymization
- Should use double-column format (exceptions permitted per ACLPUB guidelines)
- Reviewers are not obligated to review appendix content

Critical technical content should appear in the main paper, not appendices.

## Limitations Section Requirements

A dedicated "Limitations" section is mandatory:
- Position at paper's end before references
- Does not count toward page limits
- Cannot introduce new methods, analysis, or results
- Discusses constraints of presented work only
- Papers lacking this section face desk 
…[truncated 989 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "WebFetch",
  "elapsed_ms": 8791
}
```

</details>

---


### Tool call

_source line 1518 · 2026-05-23T16:57:47.655889+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 1519 · 2026-05-23T16:57:47.958111+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	
4	\usepackage{graphicx}
5	\usepackage{algorithm}
6	\usepackage{algorithmic}
7	
8	\usepackage{amsmath,amssymb,amsthm}
9	\usepackage{booktabs}
10	\usepackage{pifont}
11	\usepackage{multirow}
12	
13	\newtheorem{definition}{Definition}
14	\newtheorem{proposition}{Proposition}
15	\newtheorem{theorem}{Theorem}
16	\newtheorem{lemma}{Lemma}
17	\newtheorem{conjecture}{Conjecture}
18	\newtheorem{observation}{Observation}
19	\newtheorem{remark}{Remark}
20	
21	\setlength{\textfloatsep}{8pt plus 2pt minus 4pt}
22	\setlength{\dbltextfloatsep}{8pt plus 2pt minus 4pt}
23	\setlength{\floatsep}{8pt plus 2pt minus 4pt}
24	\setlength{\dblfloatsep}{8pt plus 2pt minus 4pt}
25	\graphicspath{{../../figures/paper/}}
26	
27	\title{Multi-Class Annotation Errors in Causal Inference:\\Topology-Dependent Bias, Sensitivity, and Correction}
28	
29	\author{Anonymous}
30	
31	\begin{document}
32	\maketitle
33	
34	\input{abstract}
35	
36	\input{introduction}
37	
38	\begin{figure*}[t]
39	\centering
40	\includegraphics[width=0.92\textwidth,height=0.18\textheight,keepaspectratio]{fig1_dag_taxonomy.pdf}
41	\vspace{-6pt}
42	\caption{Seven canonical DAG topologies with starred-node annotation~\cite{hernan_cole2009}. $A$ (latent) $\to$ $A^*$ (observed) via a dashed measurement edge; the causal role of $A$ varies: treatment (exposure), covariate (confounding, mediation, M-bias, front-door), selection (collider), instrument (IV).}
43	\label{fig:dag_taxonomy}
44	\end{figure*}
45	
46	\input{related_work}
47	
48	\input{method}
49	
50	\input{experiments}
51	
52	\input{conclusion}
53	
54	\bibliography{references}
55	
56	\appendix
57	\input{appendix_proofs}
58	
59	\end{document}
60	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 302
}
```

</details>

---


### Tool call

_source line 1520 · 2026-05-23T16:57:48.109427+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_19/submitted.pdf",
  "pages": "1-9"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_19/submitted.pdf",
    "pages": "1-9"
  }
}
```

</details>

---


### Tool result

_source line 1521 · 2026-05-23T16:57:48.616930+00:00_

PDF pages extracted: 9 page(s) from /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_19/submitted.pdf (915.5KB)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 507
}
```

</details>

---


### Tool call

_source line 1522 · 2026-05-23T16:58:49.950426+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '执行资料检查和 Venue 调研'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'in_progress', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.6/0.7: 派发外部审稿 + 视觉审查', 'status': 'pending', 'activeForm': '派发外部审稿和视觉审查'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'pending', 'activeForm': '等待 Reviewer 独立审稿'}, {'content': 'Step 2: 交叉分享', 'status': 'pending', 'activeForm': '执行交叉分享'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断收敛'}, {'content': 'Step 4: 汇总报告 & 投递', 'status': 'pending', 'activeForm': '汇总报告并投递'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '执行资料检查和 Venue 调研'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'in_progress', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.6/0.7: 派发外部审稿 + 视觉审查', 'status': 'pending', 'activeForm': '派发外部审稿和视觉审查'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'pending', 'activeForm': '等待 Reviewer 独立审稿'}, {'content': 'Step 2: 交叉分享', 'status': 'pending', 'activeForm': '执行交叉分享'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断收敛'}, {'content': 'Step 4: 汇总报告 & 投递', 'status': 'pending', 'activeForm': '汇总报告并投递'}]"
  }
}
```

</details>

---


### Tool result

_source line 1523 · 2026-05-23T16:58:49.950924+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1524 · 2026-05-23T16:58:50.855421+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "causal_annot_error_attrib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "causal_annot_error_attrib"
  }
}
```

</details>

---


### Tool result

_source line 1525 · 2026-05-23T16:58:50.905990+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1526 · 2026-05-23T16:58:51.308190+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "causal_annot_error_attrib",
  "file": "paper_checklist.yaml",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "causal_annot_error_attrib",
    "file": "paper_checklist.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 1527 · 2026-05-23T16:58:51.358705+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'causal_annot_error_attrib'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1528 · 2026-05-23T16:59:07.129523+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "causal_annot_error_attrib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "causal_annot_error_attrib"
  }
}
```

</details>

---


### Tool result

_source line 1529 · 2026-05-23T16:59:07.984393+00:00_

{"result":"# 项目 causal_annot_error_attrib 概况\n\n## 实验状态 (14 个)\n\n- **plan006_asv_empirical**: DONE (success) — \n- **plan010_annot_sensitivity_toolkit**: DONE (success) — \n- **plan003_empirical_confusion_matrices**: DONE (failed) — \n- **plan007_correction_guidance**: DONE (success) — \n- **plan009_pathological_matrices**: DONE (success) — \n- **plan005_asv_extended**: DONE (success) — \n- **plan002_k57_extension**: DONE (success) — \n- **plan001_dag_taxonomy**: DONE (success) — \n- **plan004_asv_framework**: DONE (success) — \n- **plan_004_asv_v3_fixed**: DONE (success) — \n- **plan008_binarization_collapse**: DONE (success) — \n- **mvp_exposure_dirichlet_subspace**: DONE (success) — \n- **mvp_exposure_dag**: DONE (success) — \n- **mvp_confounding_dag**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-21\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n（无）\n\n## 近期结论\n- **plan006_asv_empirical** (success): 真实 LLM confusion matrices（跨 K=2/3/10，跨 7B/235B 模型）在 7 种 DAG 拓扑下的偏差传播与理论预测一致：(1) F1 高不代表因果估计安全（F1=0.72 但 IV bias>100%），(2) 0 sign flips 确认结构性保证，(3) topology（非 K 或 model size）是 bias 的主要决定因素。\n- **plan010_annot_sensitivity_toolkit** (success): 封装 7-topology bias computation、ASV sensitivity framework 和 5 种 correction 方法为可复用 Python 包，使 practitioners 能用 3 行代码评估 LLM 标注误差对因果推断的影响。验证：(1) API 输出与 plan_001/004/005/007 原始脚本一致，(2) worked example 展示完整工作流，(3) 35 个 pytest 全通过。\n- **plan003_empirical_confusion_matrices** (failed): Different LLMs (Llama-4-Maverick, Qwen3-235B, DeepSeek-Chat) produce systematically different confusion matrices on the same classification tasks, and these empirical confusion matrices can be used to quantify annotation error propagation in downstream causal inference.\n\n## 趋势\n成功 13 / 负向 0 / 失败 1 / 共 14\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nhome-1x5090: 无 GPU 信息\n\n## 告警\n- plan003_empirical_confusion_matrices: 训练失败 — unknown"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 854
}
```

</details>

---


### Tool call

_source line 1530 · 2026-05-23T16:59:08.135471+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/agent/config.yaml 2>/dev/null | grep -A5 \"external_review\" || echo \"NO_EXTERNAL_REVIEW_CONFIG\"",
  "description": "Check external review config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/agent/config.yaml 2>/dev/null | grep -A5 \"external_review\" || echo \"NO_EXTERNAL_REVIEW_CONFIG\"",
    "description": "Check external review config"
  }
}
```

</details>

---


### Tool result

_source line 1531 · 2026-05-23T16:59:08.186113+00:00_

NO_EXTERNAL_REVIEW_CONFIG

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1532 · 2026-05-23T16:59:28.334337+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '执行资料检查和 Venue 调研'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.6/0.7: 派发视觉审查 + Reviewer', 'status': 'in_progress', 'activeForm': '派发视觉审查和 Reviewer 任务'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'pending', 'activeForm': '等待 Reviewer 独立审稿'}, {'content': 'Step 2: 交叉分享', 'status': 'pending', 'activeForm': '执行交叉分享'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断收敛'}, {'content': 'Step 4: 汇总报告 & 投递', 'status': 'pending', 'activeForm': '汇总报告并投递'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '执行资料检查和 Venue 调研'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.6/0.7: 派发视觉审查 + Reviewer', 'status': 'in_progress', 'activeForm': '派发视觉审查和 Reviewer 任务'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'pending', 'activeForm': '等待 Reviewer 独立审稿'}, {'content': 'Step 2: 交叉分享', 'status': 'pending', 'activeForm': '执行交叉分享'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断收敛'}, {'content': 'Step 4: 汇总报告 & 投递', 'status': 'pending', 'activeForm': '汇总报告并投递'}]"
  }
}
```

</details>

---


### Tool result

_source line 1533 · 2026-05-23T16:59:28.334848+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1534 · 2026-05-23T16:59:30.547299+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "causal_annot_error_attrib",
  "review_chat_id": "oc_9f117624057fcf6cb95db4d67f525246"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "causal_annot_error_attrib",
    "review_chat_id": "oc_9f117624057fcf6cb95db4d67f525246"
  }
}
```

</details>

---


### Tool result

_source line 1535 · 2026-05-23T16:59:54.839928+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 24292
}
```

</details>

---


### Tool call

_source line 1536 · 2026-05-23T16:59:56.498203+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "你负责审查**方法严谨性 + 理论证明 + 实验验证**。\n\n## 投稿信息\n- **Venue**: EMNLP 2026（通过 ARR 统一审稿）\n- **类别**: Long Paper\n- **Deadline**: 2026-05-25\n- **页数限制**: 正文 8 页 + 无限参考文献 + Limitations（不计入页数）\n- **模板**: ACL review 模板\n- **匿名规则**: Double-blind\n\n## 论文文件\n- LaTeX 主文件: `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_19/submitted.pdf`\n\n## 你的审查侧重\n\n### 1. 理论严谨性\n- Theorem 1（K=2 envelope monotonicity）的证明是否完整、条件是否充分？\n- Proposition 1（sign preservation）的条件和证明是否严谨？\n- Conjecture 1（K≥3 ε-approximate monotonicity）的数值验证是否充分？ε<0.02 的声称是否有足够支撑？\n- Observation 1 的表述是否准确？\n- 偏差表达式（Eq. 1-3）的推导是否正确？\n\n### 2. 方法论\n- Non-differential misclassification 假设是否合理？论文是否充分讨论了该假设的合理性和局限性？\n- ASV 框架的三种诊断（magnitude, significance, sign-flip）定义是否清晰、有用？\n- FWL invariance 的证明和含义是否正确阐述？\n- Proportional effects 假设（f=λg）在 NLP 场景中的合理性？\n- 线性 SEM 假设的局限性讨论是否充分？\n\n### 3. 实验验证\n- Monte Carlo 模拟设置是否合理？100,000 confusion matrices 是否足够？\n- Theory-MC MAPE 1.6% 是否可信？\n- 经验验证（HumAID K=10, VAST K=3, CivilComments K=2）是否充分？\n- 23 个 LLM 配置 × 7 拓扑 = 161 场景的覆盖面是否足够？\n- Correction methods 比较（Table 4）是否公平？\n- Dirichlet(1,1,1) 先验的代表性如何？\n\n### 4. 数值一致性\n- Abstract/Introduction 中的数字是否与正文和表格一致？\n- 关键声称（83.4% sign reversal, 2.1% under realistic accuracy, 0% primary coefficient reversal, 1.6% MAPE）是否有充分支撑？\n\n请按以下格式输出审稿意见：\n1. **Summary**（2-3 句）\n2. **Strengths**（逐条）\n3. **Weaknesses**（逐条，标注严重程度：critical / major / minor）\n4. **Questions**（需要作者回答的问题）\n5. **Missing References**（遗漏的重要相关工作）\n6. **Overall Assessment**（评分 + 置信度）\n\n评分标准（EMNLP 2026 ARR）：5=Consider for Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit",
  "project": "causal_annot_error_attrib",
  "chat_id": "oc_9f117624057fcf6cb95db4d67f525246",
  "director_session_key": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "你负责审查**方法严谨性 + 理论证明 + 实验验证**。\n\n## 投稿信息\n- **Venue**: EMNLP 2026（通过 ARR 统一审稿）\n- **类别**: Long Paper\n- **Deadline**: 2026-05-25\n- **页数限制**: 正文 8 页 + 无限参考文献 + Limitations（不计入页数）\n- **模板**: ACL review 模板\n- **匿名规则**: Double-blind\n\n## 论文文件\n- LaTeX 主文件: `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_19/submitted.pdf`\n\n## 你的审查侧重\n\n### 1. 理论严谨性\n- Theorem 1（K=2 envelope monotonicity）的证明是否完整、条件是否充分？\n- Proposition 1（sign preservation）的条件和证明是否严谨？\n- Conjecture 1（K≥3 ε-approximate monotonicity）的数值验证是否充分？ε<0.02 的声称是否有足够支撑？\n- Observation 1 的表述是否准确？\n- 偏差表达式（Eq. 1-3）的推导是否正确？\n\n### 2. 方法论\n- Non-differential misclassification 假设是否合理？论文是否充分讨论了该假设的合理性和局限性？\n- ASV 框架的三种诊断（magnitude, significance, sign-flip）定义是否清晰、有用？\n- FWL invariance 的证明和含义是否正确阐述？\n- Proportional effects 假设（f=λg）在 NLP 场景中的合理性？\n- 线性 SEM 假设的局限性讨论是否充分？\n\n### 3. 实验验证\n- Monte Carlo 模拟设置是否合理？100,000 confusion matrices 是否足够？\n- Theory-MC MAPE 1.6% 是否可信？\n- 经验验证（HumAID K=10, VAST K=3, CivilComments K=2）是否充分？\n- 23 个 LLM 配置 × 7 拓扑 = 161 场景的覆盖面是否足够？\n- Correction methods 比较（Table 4）是否公平？\n- Dirichlet(1,1,1) 先验的代表性如何？\n\n### 4. 数值一致性\n- Abstract/Introduction 中的数字是否与正文和表格一致？\n- 关键声称（83.4% sign reversal, 2.1% under realistic accuracy, 0% primary coefficient reversal, 1.6% MAPE）是否有充分支撑？\n\n请按以下格式输出审稿意见：\n1. **Summary**（2-3 句）\n2. **Strengths**（逐条）\n3. **Weaknesses**（逐条，标注严重程度：critical / major / minor）\n4. **Questions**（需要作者回答的问题）\n5. **Missing References**（遗漏的重要相关工作）\n6. **Overall Assessment**（评分 + 置信度）\n\n评分标准（EMNLP 2026 ARR）：5=Consider for Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit",
    "project": "causal_annot_error_attrib",
    "chat_id": "oc_9f117624057fcf6cb95db4d67f525246",
    "director_session_key": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
  }
}
```

</details>

---


### Tool result

_source line 1537 · 2026-05-23T17:00:16.890303+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_9f117624057fcf6cb95db4d67f525246:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 20392
}
```

</details>

---


### Tool call

_source line 1538 · 2026-05-23T17:00:17.642858+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "你负责审查**新颖性 + 相关工作完整性 + 写作质量 + 格式合规**。\n\n## 投稿信息\n- **Venue**: EMNLP 2026（通过 ARR 统一审稿）\n- **类别**: Long Paper\n- **Deadline**: 2026-05-25\n- **页数限制**: 正文 8 页 + 无限参考文献 + Limitations（不计入页数）\n- **模板**: ACL review 模板\n- **匿名规则**: Double-blind\n\n## 论文文件\n- LaTeX 主文件: `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_19/submitted.pdf`\n\n## 你的审查侧重\n\n### 1. 新颖性评估\n- 三个贡献（multi-class bias taxonomy, ASV framework, FWL invariance + correction routing）的新颖性如何？\n- 与 Brenner (1993), TeBlunthuis et al. (2024), Lee and Wood-Doughty (2024) 等已有工作的区分是否清晰？\n- ASV 与 E-values (VanderWeele and Ding, 2017) 的关系——是否只是简单移植？Remark 1 的对比是否准确？\n- \"first systematic topology-specific comparison\" 声称是否合理？是否存在过度声称？\n- Contribution 3（FWL invariance + correction routing）作为独立贡献是否足够有分量？\n\n### 2. 相关工作完整性\n- Related Work（Section 2）是否全面覆盖了测量误差、因果推断、LLM 标注质量三个领域的关键文献？\n- 是否有重要遗漏？特别关注：\n  - 2024-2025 年的最新工作\n  - measurement error in causal inference 领域的经典文献\n  - LLM annotation quality / CSS 领域的重要工作\n  - sensitivity analysis 和 correction methods 领域\n- 引用格式是否正确（natbib, 括号 vs 文中引用）？\n\n### 3. 写作质量\n- Abstract 是否在 200 words 以内？信息密度是否合适？\n- Introduction 的叙事逻辑是否清晰？三个贡献是否按重要性排列？\n- 术语使用是否一致（τ 的含义在不同拓扑下是否清晰）？\n- 符号系统是否统一？是否有对 NLP 读者不友好的术语（plim, FWL, Wald estimator 等）？\n- 图表标题和说明是否自解释？\n- Limitations 是否充分？\n\n### 4. 格式合规\n- 正文是否严格在 8 页以内？Section 5 Conclusion 和 Limitations 是否在第 8 页内结束？\n- 匿名是否完整？是否有泄露作者身份的线索？\n- 参考文献格式是否统一？是否有 orphan entries（.bib 中有但正文未引用）？\n- Figure/Table 的放置是否合理？是否有 overflow？\n- Appendix 是否在参考文献之后？\n\n### 5. EMNLP 2026 特殊要求\n- Limitations section 是否在正文中（不在 appendix）？\n- 是否只有一个 Limitations section？\n- Abstract 是否不超过 200 words？\n\n请按以下格式输出审稿意见：\n1. **Summary**（2-3 句）\n2. **Strengths**（逐条）\n3. **Weaknesses**（逐条，标注严重程度：critical / major / minor）\n4. **Questions**（需要作者回答的问题）\n5. **Missing References**（遗漏的重要相关工作）\n6. **Overall Assessment**（评分 + 置信度）\n\n评分标准（EMNLP 2026 ARR）：5=Consider for Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit",
  "project": "causal_annot_error_attrib",
  "chat_id": "oc_9f117624057fcf6cb95db4d67f525246",
  "director_session_key": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "你负责审查**新颖性 + 相关工作完整性 + 写作质量 + 格式合规**。\n\n## 投稿信息\n- **Venue**: EMNLP 2026（通过 ARR 统一审稿）\n- **类别**: Long Paper\n- **Deadline**: 2026-05-25\n- **页数限制**: 正文 8 页 + 无限参考文献 + Limitations（不计入页数）\n- **模板**: ACL review 模板\n- **匿名规则**: Double-blind\n\n## 论文文件\n- LaTeX 主文件: `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_19/submitted.pdf`\n\n## 你的审查侧重\n\n### 1. 新颖性评估\n- 三个贡献（multi-class bias taxonomy, ASV framework, FWL invariance + correction routing）的新颖性如何？\n- 与 Brenner (1993), TeBlunthuis et al. (2024), Lee and Wood-Doughty (2024) 等已有工作的区分是否清晰？\n- ASV 与 E-values (VanderWeele and Ding, 2017) 的关系——是否只是简单移植？Remark 1 的对比是否准确？\n- \"first systematic topology-specific comparison\" 声称是否合理？是否存在过度声称？\n- Contribution 3（FWL invariance + correction routing）作为独立贡献是否足够有分量？\n\n### 2. 相关工作完整性\n- Related Work（Section 2）是否全面覆盖了测量误差、因果推断、LLM 标注质量三个领域的关键文献？\n- 是否有重要遗漏？特别关注：\n  - 2024-2025 年的最新工作\n  - measurement error in causal inference 领域的经典文献\n  - LLM annotation quality / CSS 领域的重要工作\n  - sensitivity analysis 和 correction methods 领域\n- 引用格式是否正确（natbib, 括号 vs 文中引用）？\n\n### 3. 写作质量\n- Abstract 是否在 200 words 以内？信息密度是否合适？\n- Introduction 的叙事逻辑是否清晰？三个贡献是否按重要性排列？\n- 术语使用是否一致（τ 的含义在不同拓扑下是否清晰）？\n- 符号系统是否统一？是否有对 NLP 读者不友好的术语（plim, FWL, Wald estimator 等）？\n- 图表标题和说明是否自解释？\n- Limitations 是否充分？\n\n### 4. 格式合规\n- 正文是否严格在 8 页以内？Section 5 Conclusion 和 Limitations 是否在第 8 页内结束？\n- 匿名是否完整？是否有泄露作者身份的线索？\n- 参考文献格式是否统一？是否有 orphan entries（.bib 中有但正文未引用）？\n- Figure/Table 的放置是否合理？是否有 overflow？\n- Appendix 是否在参考文献之后？\n\n### 5. EMNLP 2026 特殊要求\n- Limitations section 是否在正文中（不在 appendix）？\n- 是否只有一个 Limitations section？\n- Abstract 是否不超过 200 words？\n\n请按以下格式输出审稿意见：\n1. **Summary**（2-3 句）\n2. **Strengths**（逐条）\n3. **Weaknesses**（逐条，标注严重程度：critical / major / minor）\n4. **Questions**（需要作者回答的问题）\n5. **Missing References**（遗漏的重要相关工作）\n6. **Overall Assessment**（评分 + 置信度）\n\n评分标准（EMNLP 2026 ARR）：5=Consider for Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit",
    "project": "causal_annot_error_attrib",
    "chat_id": "oc_9f117624057fcf6cb95db4d67f525246",
    "director_session_key": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
  }
}
```

</details>

---


### Tool result

_source line 1539 · 2026-05-23T17:00:19.054399+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_9f117624057fcf6cb95db4d67f525246:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1411
}
```

</details>

---


### Tool call

_source line 1540 · 2026-05-23T17:00:39.394031+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '执行资料检查和 Venue 调研'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.6/0.7: 派发视觉审查 + Reviewer', 'status': 'completed', 'activeForm': '派发视觉审查和 Reviewer 任务'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'in_progress', 'activeForm': '等待 Reviewer 独立审稿'}, {'content': 'Step 2: 交叉分享', 'status': 'pending', 'activeForm': '执行交叉分享'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断收敛'}, {'content': 'Step 4: 汇总报告 & 投递', 'status': 'pending', 'activeForm': '汇总报告并投递'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '执行资料检查和 Venue 调研'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.6/0.7: 派发视觉审查 + Reviewer', 'status': 'completed', 'activeForm': '派发视觉审查和 Reviewer 任务'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'in_progress', 'activeForm': '等待 Reviewer 独立审稿'}, {'content': 'Step 2: 交叉分享', 'status': 'pending', 'activeForm': '执行交叉分享'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断收敛'}, {'content': 'Step 4: 汇总报告 & 投递', 'status': 'pending', 'activeForm': '汇总报告并投递'}]"
  }
}
```

</details>

---


### Tool result

_source line 1541 · 2026-05-23T17:00:39.394516+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1542 · 2026-05-23T17:00:40.098514+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "*.tex",
  "path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "*.tex",
    "path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 1543 · 2026-05-23T17:00:40.149091+00:00_

/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/exp_a_stress_test_table.tex
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/exp_e_asv_stability_table.tex
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/abstract.tex
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/e2e_demo_table.tex
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/conjecture_dgp_sensitivity_table.tex
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/related_work.tex
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/introduction.tex
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/experiments.tex
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/method.tex
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1544 · 2026-05-23T17:00:46.772637+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 1545 · 2026-05-23T17:00:46.924149+00:00_

1	\begin{abstract}
2	Large language models are increasingly used as annotators in computational social science, yet annotation errors propagate into downstream causal estimates in ways that depend on both the confusion matrix structure and the causal DAG topology. We derive bias expressions for seven canonical topologies under $K$-class non-differential misclassification and show that $K {\geq} 3$ introduces a structural possibility of sign reversal absent in the binary case. We prove sign preservation for confounding and collider, and verify it numerically for mediation, M-bias, and front-door; exposure and IV topologies can reverse the treatment effect sign. Under realistic LLM accuracy, sign reversal of non-dominant coefficients occurs under exposure; under empirical LLM matrices (diagonal 0.45--0.81), sign reversal is confined to exposure; IV is fragile under uniform Dirichlet priors but exhibits zero reversals under empirical LLM matrices. We introduce Annotation Sensitivity Values (ASVs), with proved ($K{=}2$) and numerically verified ($K{\geq}3$) monotonicity, yielding a vulnerability ranking from IV (maximally fragile) to M-bias (immune), and show that matrix-based corrections are provably ineffective under linear regression for four topologies due to Frisch--Waugh--Lovell invariance. Topology-aware analysis is necessary for valid causal inference with LLM-generated annotations.
3	\end{abstract}
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 1546 · 2026-05-23T17:00:47.277138+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 1547 · 2026-05-23T17:00:47.731401+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Setup and Notation}
5	\label{sec:notation}
6	
7	Let $A$ denote a true $K$-class categorical variable (e.g., sentiment with $K{=}3$ levels) and $A^*$ its observed, potentially misclassified version produced by an LLM annotator. The misclassification process is characterized by a $K{\times}K$ confusion matrix $C$ with entries $C_{jk} = P(A^*{=}j \mid A{=}k)$, where each column sums to one (column-stochastic: each column gives the distribution of predicted labels for a given true label). Following \citet{hernan_cole2009}, we represent this measurement process using \emph{starred-node} DAGs: the true variable $A$ is latent, and the observed $A^*$ is connected to $A$ via a dashed measurement edge.
8	
9	\paragraph{Notation conventions.}
10	Our analysis characterizes systematic bias---the value an estimator converges to as $N \to \infty$ (the probability limit, or plim)---rather than finite-sample variance. The Frisch--Waugh--Lovell (FWL) theorem guarantees that each regression coefficient equals the coefficient from a simple regression after residualizing all other variables; this is why matrix-based corrections fail for covariate topologies (Section~\ref{sec:correction}): replacing the mismeasured variable with a corrected version does not change the residualized relationship. The Wald estimator (ratio of reduced-form to first-stage effects) diverges under weak instruments; Dirichlet priors over probability vectors represent uncertainty over misclassification patterns. Table~\ref{tab:notation} (Appendix~\ref{app:notation_table}) collects all notation.
11	
12	\begin{definition}[Non-differential misclassification]
13	\label{def:nondiff}
14	Misclassification of $A$ is non-differential with respect to outcome $Y$ and covariates $\mathbf{Z}$ if $P(A^*{=}j \mid A{=}k, Y, \mathbf{Z}) = P(A^*{=}j \mid A{=}k) = C_{jk}$ for all $j,k$.
15	\end{definition}
16	
17	In batch annotation pipelines, the LLM processes each text indep
…[truncated 14161 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 454
}
```

</details>

---


### Tool call

_source line 1548 · 2026-05-23T17:00:47.832320+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 1549 · 2026-05-23T17:00:48.133835+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We validate through Monte Carlo simulation ($K{=}3$), cross-$K$ robustness checks ($K{=}5,7$), and empirical validation with real LLM confusion matrices from three NLP tasks ($K{=}2,3,10$).
5	
6	\subsection{Setup}
7	\label{sec:setup}
8	
9	For each topology, we sample 100{,}000 confusion matrices from a Dirichlet$(1,1,1)$ prior, compute analytical probability limits, and validate against Monte Carlo simulation ($N{=}10{,}000$). ASV experiments use $C(\delta) = (1{-}\delta)I + \delta C_0$.
10	
11	\subsection{Bias Taxonomy}
12	\label{sec:taxonomy_results}
13	
14	\paragraph{Theory-MC agreement.}
15	Analytical probability limits match Monte Carlo estimates with grand MAPE of 1.6\% across 161 scenarios (23 LLM configurations $\times$ 7 topologies; per-topology range: 0.3\%--3.7\%).
16	
17	\paragraph{Exposure DAG: sign reversal under multi-class misclassification.}
18	Under realistic LLM accuracy (diagonal $\geq 0.7$), the violation rate is 13.7\% with 2.1\% sign reversal; even at diagonal $\geq 0.9$, violation persists at 11.9\%. Under the full Dirichlet$(1,1,1)$ prior, 85\% of $K{=}3$ confusion matrices violate the binary ``toward-null'' guarantee, and 83.4\% cause sign reversal of at least one coefficient; the minimum diagonal entry $\min_k C_{kk} < 0.55$ predicts sign reversal with 91\% accuracy across empirical matrices (Appendix~\ref{sec:sign_determinants}). The $K{=}2$ control confirms that all tested binary matrices maintain classical attenuation~\cite{brenner1993}, establishing that the multi-class failure is structurally distinct.
19	
20	\paragraph{Structural guarantee for non-exposure topologies.}
21	Five topologies exhibit zero sign-flip rate (Table~\ref{tab:taxonomy}): confounding, mediation, and front-door show 100\% amplification~\cite{brenner1993, dosemeci1990} but never reverse the sign; collider is protective ($|B(C)|$ non-increasing; Conjecture~\ref{conj:monotone}); M-bias shows weakest sensitivity (
…[truncated 6321 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 1550 · 2026-05-23T17:00:48.335029+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1551 · 2026-05-23T17:00:48.435824+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We characterized how multi-class annotation errors interact with causal DAG topology: the binary attenuation guarantee breaks at $K \geq 3$, where exposure and IV can reverse treatment effect signs while five topologies preserve them. ASVs yield a topology-dependent vulnerability ranking; matrix-based corrections are provably ineffective for four covariate topologies due to FWL invariance. Practitioners should identify their DAG topology and compute topology-specific ASV before choosing a correction strategy. Code and data will be released.
5	
6	\section*{Limitations}
7	
8	We assume non-differential misclassification (Appendix~\ref{sec:nondiff_stress}). Bias expressions assume $K{=}3$ linear SEMs; proving $K{\geq}3$ envelope monotonicity remains the primary open question~\cite{schennach2020mismeasured}, though rankings are stable across $K{=}3,5,10$. The framework requires estimable $C$; experiments are Monte Carlo without end-to-end causal benchmarks.
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1552 · 2026-05-23T17:00:53.658886+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 1553 · 2026-05-23T17:00:53.710228+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Large language models are rapidly replacing human annotators in computational social science, with researchers using LLM-generated labels for tasks ranging from sentiment classification to political stance detection~\cite{gilardi2023chatgpt, ziems2024can, egami_hinck_stewart_wei2023, baumann2025}. Crucially, most of these tasks are inherently multi-class: stance detection uses 3--4 categories, sentiment analysis 5, and disaster response taxonomies 10 or more. This shift promises dramatic cost reduction, but introduces a critical validity gap: annotation errors (equivalently, misclassification) from imperfect classifiers propagate into downstream causal estimates in ways that depend on both the error structure and the causal design. \citet{baumann2025} demonstrate that across 37 annotation tasks, 31\% of hypotheses yield incorrect conclusions with state-of-the-art LLMs, rising to 50\% for smaller models; these errors are highly correlated across models (60\% agreement when both err)~\cite{kim_garg2025}, undermining ensemble-based mitigation. Analyzing the \emph{structure} of annotation error, rather than simply reducing its magnitude, is essential for valid downstream inference.
5	
6	The transition at $K{\geq}3$ is not gradual but structural. For $K{=}2$, the stochastic constraint forces any confusion matrix with positive diagonal to preserve coefficient signs---an algebraic property of the $2{\times}2$ matrix dimension~\cite{brenner1993}. This guarantee \emph{vanishes} at $K{\geq}3$: the higher-dimensional confusion matrix admits negative effective weights on categories with opposite-sign coefficients, enabling sign reversal even under high accuracy~\cite{veirod_laake2001}. Under a uniform Dirichlet prior, 83.4\% of $K{=}3$ exposure confusion matrices produce sign reversal of at least one secondary coefficient; under realistic accuracy (diagonal $\geq 0.7$), 2.1\% still do. The primary treatment coefficient, h
…[truncated 2910 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1554 · 2026-05-23T17:00:53.710675+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 1555 · 2026-05-23T17:00:53.814752+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Measurement error in causal inference.}
5	Foundations appear in \citet{carroll2006, gustafson2004, buonaccorsi2010, bound2001measurement}, with DAG-based formalization by \citet{hernan_cole2009} and \citet{kuroki_pearl2014}. For binary variables, non-differential misclassification biases toward the null~\cite{brenner1993, ogburn_vanderweele2012}, but this fails for polytomous exposures~\cite{dosemeci1990, jurek2005, veirod_laake2001}. Extensions address differential measurement error~\cite{edwards_lessler_naimi2021, imai_yamamoto2010}, endogenous misreporting~\cite{nguimkeu_denteh_tchernis2019}, mismeasured covariates under IPW~\cite{shu_yi2019a, shu_yi2019b}, mediation with mismeasured mediators~\cite{valeri_vanderweele2013}, nonclassical error~\cite{schennach2020mismeasured}, and multiply robust estimation~\cite{wei2025multiply}. All analyze a single DAG topology; ours characterizes how the \emph{same} confusion matrix produces qualitatively different bias across seven topologies.
6	
7	\paragraph{Text classifiers and LLM annotation.}
8	\citet{grimmer2022} and \citet{feder_etal2022} provide foundations for text-as-data and causal inference in NLP. \citet{wood_doughty2018} first applied DAG reasoning to classifier error; \citet{teblunthuis2024} gave the most complete binary treatment ($K{=}2$, four DAGs); \citet{lee_wood_doughty2024} extended to categorical LLM classifiers but covered only confounding. On annotation quality, \citet{gilardi2023chatgpt} and \citet{ziems2024can} document rapid LLM annotator adoption (surveyed by \citealt{tan2024llm}), \citet{baumann2025} found 31\% incorrect conclusions, and \citet{kim_garg2025} showed 60\% error correlation across models~\cite{pangakis_wolken_fasching2023, cheng_mayya_sedoc2024, variance_aware_llm2026, hidden_measurement_error2026}. \citet{audinet2025} benchmark debiasing; \citet{keith_jensen_oconnor2020} survey the landscape. These works either restr
…[truncated 1060 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 104
}
```

</details>

---


### Tool call

_source line 1556 · 2026-05-23T17:01:00.303399+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 1557 · 2026-05-23T17:01:00.303843+00:00_

1	\section{Proofs of Proposition~\ref{prop:signflip} and Theorem~\ref{thm:monotone}}
2	\label{app:proof}
3	
4	We provide algebraic proofs of sign preservation for the confounding and collider topologies (Proposition~\ref{prop:signflip}(a)--(b)), an explicit counterexample for exposure (Proposition~\ref{prop:signflip}(c)), numerical verification for mediation, M-bias, and front-door (Numerical Verification~1), and the monotonicity proof for confounding (Theorem~\ref{thm:monotone}).
5	Throughout, $A\in\{0,1,\dots,K{-}1\}$ with prior $p_k=P(A{=}k)$, and $C$ is a $K{\times}K$ column-stochastic confusion matrix with $C_{jk}=P(A^*{=}j\mid A{=}k)$.
6	We use category~0 as the reference and let $D_j=\mathbf{1}(A{=}j)$, $D_j^*=\mathbf{1}(A^*{=}j)$ for $j=1,\dots,K{-}1$.
7	
8	\subsection{Notation and Key Identities}
9	\label{app:notation}
10	
11	Under non-differential misclassification, the misclassified moments factor linearly through $C$.
12	Define the population vectors:
13	\begin{align}
14	  q_j &= P(A^*{=}j) = \textstyle\sum_k C_{jk}\,p_k, \label{eq:q}\\
15	  \mathrm{ct}_j &= \mathbb{E}[T\cdot D_j^*] = \textstyle\sum_k C_{jk}\,\mathbb{E}[T\cdot D_k], \label{eq:ct}\\
16	  \mathrm{cy}_j &= \mathbb{E}[Y\cdot D_j^*] = \textstyle\sum_k C_{jk}\,\mathbb{E}[Y\cdot D_k]. \label{eq:cy}
17	\end{align}
18	Write $q = Cp$, $\mathrm{ct} = C\,\mathbb{E}[T\cdot D]$, and $\mathrm{cy} = C\,\mathbb{E}[Y\cdot D]$, where $D=(D_0,\dots,D_{K-1})^\top$.
19	
20	\subsection{Frisch--Waugh--Lovell Decomposition}
21	\label{app:fwl}
22	
23	For topologies where $T$ is directly observed (confounding, mediation, collider, M-bias, front-door), the estimator regresses $Y$ on $Z^*=(1,T,D_1^*,\dots,D_{K-1}^*)$.
24	By the Frisch--Waugh--Lovell (FWL) theorem, the coefficient on $T$ satisfies:
25	\begin{equation}
26	  \operatorname{plim}\hat{\tau}(C)
27	  = \frac{\mathbb{E}[\tilde{T}\,\tilde{Y}]}{\mathbb{E}[\tilde{T}^2]},
28	  \label{eq:fwl}
29	\end{equation}
30	where $\tilde{T}=T-\mathbb{E}[T\mid A^*]$ and $\ti
…[truncated 3331 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1558 · 2026-05-23T17:01:07.286332+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "wc -l /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex",
  "description": "Check appendix length"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Bash",
  "tool_args": {
    "command": "wc -l /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex",
    "description": "Check appendix length"
  }
}
```

</details>

---


### Tool result

_source line 1559 · 2026-05-23T17:01:07.639288+00:00_

1469 /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Bash",
  "elapsed_ms": 352
}
```

</details>

---


### Tool call

_source line 1560 · 2026-05-23T17:01:07.940824+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "wc -w /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/abstract.tex",
  "description": "Count abstract words"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Bash",
  "tool_args": {
    "command": "wc -w /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/abstract.tex",
    "description": "Count abstract words"
  }
}
```

</details>

---


### Tool result

_source line 1561 · 2026-05-23T17:01:07.991680+00:00_

187 /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/abstract.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Assistant

_source line 1562 · 2026-05-23T17:01:26.873131+00:00_

论文全文已通读完毕。关键数据点记录：

- **Abstract**: 约 187 words（含 LaTeX 标记），渲染后预计 ~170 words，符合 200 words 限制
- **正文**: Sections 1-5 + Limitations 在第 8 页内结束，符合 8 页限制
- **Appendix**: 1469 行 LaTeX，内容丰富
- **匿名**: "Anonymous ACL submission"，未发现身份泄露

两位 Reviewer 正在独立审阅论文，等待审稿意见返回。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 153

## Round 153

2 recorded events


### User

_source line 1563 · 2026-05-23T17:08:29.366922+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 审稿意见 — Round 1

**论文**: Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction
**Venue**: EMNLP 2026 (ACL ARR)
**审查侧重**: 新颖性 + 相关工作完整性 + 写作质量 + 格式合规

---

## 总体评分
**Overall**: 3.5 / 5 (Borderline Conference)
**一句话总结**: 问题重要、实验扎实、覆盖全面，但核心理论贡献（ASV 单调性）仅对 K=2 有证明，K≥3 停留在 Conjecture；Contribution 3（FWL 不变性）作为独立贡献分量不足。

## 官方维度打分（ACL ARR review form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 实验验证充分（1.6% MAPE, 161 scenarios），但核心 Theorem 1 仅覆盖 K=2 + proportional effects，K≥3 主结果以 Conjecture 形式呈现 |
| Excitement | 3.5/5 | 问题动机清晰（LLM 标注 × 因果推断），safe/fragile 分区实用；但概念框架（ASV）与 E-value 范式相似，方法论新颖性有限 |
| Reproducibility | 4/5 | Monte Carlo 设定、DGP 参数、数据集均有详细描述；承诺释放代码和数据；附录 22 页内容充实 |
| Overall Assessment | 3.5/5 | Borderline Conference — 见下方详细分析 |

**Confidence**: 4/5 — 对测量误差、因果推断和 NLP/CSS 文献有较好了解，仔细阅读了正文和部分附录。

---

## Strengths

**S1. 重要且及时的研究问题。** LLM 标注正在大规模替代人工标注（Gilardi 2023; Ziems 2024; Baumann 2025），但标注误差对因果推断的拓扑依赖性传播此前缺乏系统研究。论文将这一问题定位清晰：F₁ 与因果偏差无显著相关（Spearman ρ = −0.10, p = 0.45; Section 4.4, Figure 4）是一个令人信服的论据。

**S2. 全面的拓扑覆盖和实证验证。** 7 种 DAG 拓扑 × K=3,5,7,10 × 4 个 LLM × 3 个 NLP 数据集（HumAID, VAST, CivilComments）→ 161 个场景，理论预测与 Monte Carlo 估计的 grand MAPE 仅 1.6%（Section 4.2）。实验设计系统性强。

**S3. 清晰的安全/脆弱二分法。** Table 1 将 7 种拓扑分为 sign-preserving（5 种）和 sign-reversing（exposure, IV）两类，为从业者提供了直接可用的风险指引。这种拓扑驱动的分区是论文最有实用价值的贡献。

**S4. F₁ 与偏差脱钩的实证论据。** Section 4.4 中 HumAID K=10 的 56 个场景在 F₁ ∈ [0.614, 0.690] 的窄范围内，偏差却相差 10 倍（IV 42.1% vs. collider <5.6%），令人印象深刻。per-topology 分解揭示了 M-bias 的反常正相关（ρ = 0.87）也是有趣的发现。

**S5. Abstract 信息密度高且在 200 words 以内（约 187 词）。** 格式总体合规。

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] ASV 单调性理论仅覆盖 K=2，与论文核心叙事矛盾

- 具体位置：Section 3.3, Theorem 1 (p.6) vs. Conjecture 1 (p.6)
- 问题：论文的核心叙事建立在"K≥3 引入结构性新现象"之上（Abstract 第 2 句, Introduction 第 2 段），但 ASV 框架的理论基石——envelope monotonicity——仅对 K=2 且在 proportional effects (f = λg) 条件下得到证明（Theorem 1）。K≥3 的结果以 Conjecture 1 形式呈现，依赖 20,000 个随机三元组的数值验证。这意味着论文对最不需要理论支撑的简单情况给出了证明，对最需要理论支撑的核心情况给出了猜想。
- 为什么影响接收：ASV 是三个贡献之一。如果 K≥3 的单调性不成立（即使 ε 很小），ASV 排序的可靠性就会受质疑。Reviewer 需要判断这是一个"接近定理的强猜想"还是一个"留给未来工作的 open problem"——论文目前的表述倾向前者，但证据水平对应后者。
- 建议修改方向：(a) 在正文中更坦诚地标明这一理论空白的严重程度——不是"the primary open question"（Limitations 中的轻描淡写），而是 ASV 框架可靠性的前提条件；(b) 如有可能，提供 K=3 的特殊情况证明（哪怕对称混淆矩阵下的），缩小理论空白；(c) 加强数值验证的对抗性——目前 ε < 0.02 的条件是 |β| ≤ 1，但论文未系统探索 ε 随 |β| 增长的速率。

**N2** [critical] Contribution 3（FWL 不变性 + correction routing）作为独立贡献分量不足

- 具体位置：Introduction 贡献 (3), Section 4.5
- 问题：FWL 定理（Frisch & Waugh 1933; Lovell 1963）本身就意味着：对协变量的任何线性变换不改变处理变量系数。Matrix-based correction（如 C⁻¹ 校正）正是对 dummy 变量的线性变换，因此"对四种协变量拓扑无效"是 FWL 的直接推论，而非新发现。论文在 Section 4.5 第一段以两句话就推导完毕——如果一个"贡献"可以用两句话完成，它可能更适合作为 Observation 而非 Contribution。
- 为什么影响接收：三个贡献中如果有一个分量不足，论文的贡献量级会降级。Correction routing algorithm（Algorithm 1, Appendix）虽然实用，但属于工程指引而非方法论贡献。
- 建议修改方向：(a) 将 FWL 不变性降格为 Observation/Remark，作为 bias taxonomy 的推论；(b) 将 Contribution 3 重新聚焦于实际有区分度的发现（如不同 correction methods 的拓扑依赖性排序，PPI++ 对 M-bias 反而有害等），这些才是非平凡的实证发现。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [major] MC-SIMEX 作为五种校正方法之一被广泛使用但未引用原始论文

- 具体位置：Section 4.5 (experiments.tex:80), Section 4.5 correction decision procedure, Algorithm 1
- 问题：MC-SIMEX 在正文和附录中被多次提及（correction ranking, routing algorithm, case studies），但原始论文 Küchenhoff, Mwalili & Lesaffre (2006, *Biometrics*) "A general method for dealing with misclassification in regression: The misclassification SIMEX" 未被引用。同样，MLA (Maximum Likelihood Adjustment) 也缺少规范引用来源。使用方法不引原始文献是学术规范问题。
- 建议：在 Section 4.5 首次提及时加上 \cite。

**W2** [major] "First systematic topology-specific comparison" 声称需更精确限定

- 具体位置：Introduction 第 4 段 ("We present the first systematic topology-specific comparison...")
- 问题：TeBlunthuis et al. (2024) 已经对 4 种 DAG 拓扑做了系统比较（K=2）；Brenner (1993) 分析了多分类混淆对 confounding 的影响。本文的新颖性在于 (a) 扩展到 K≥3 和 (b) 覆盖 7 种拓扑——这是范围上的扩展，而非方法论上的全新贡献。使用 "first" 可能引发对 overclaiming 的质疑。
- 建议：改为 "the first topology-specific comparison under multi-class (K≥3) misclassification" 或 "the most comprehensive topology-specific comparison to date"，明确限定新颖性所在。

**W3** [major] Proportional effects 假设（Theorem 1）的可验证性和适用性

- 具体位置：Section 3.3, Theorem 1 条件 "f = λg"
- 问题：论文声称"97.3% of empirical LLM configurations satisfy the condition"（method.tex 附近），但未说明如何量化检验 proportional effects。在实践中，confounding function f 和 exposure function g 通常不可观测——如何"test by regressing f(A) on g(A)"？如果 f 和 g 需要事先知道，这个条件就是不可验证的。此外，proportional effects 本质上要求单一潜在因子，这在复杂 NLP 场景中并不普遍。
- 建议：(a) 明确说明 97.3% 的检验方法和标准（R² 阈值？），(b) 讨论该条件在什么情况下可能失败（如多维质量差异）。

**W4** [minor] 符号 τ 的拓扑依赖性定义可能造成混淆

- 具体位置：Section 3.2, method.tex:26
- 问题：τ 在不同拓扑下含义不同（confounding: X 系数; exposure: category-specific β_j; mediation: 直接效应 τ_direct）。虽然论文在首次出现时做了说明（"its precise definition is topology-specific"），但后续 ASV 和 correction 讨论中频繁使用 τ 进行跨拓扑比较（如 Table 1 的 τ_sf=0?），读者需要不断查找每个拓扑下 τ 的具体含义。
- 建议：考虑用下标区分（τ_conf, τ_exp, τ_med 等），或在 Table 1 中增加一列注明每种拓扑下 τ 的具体定义。

**W5** [minor] 对 NLP 读者的可及性

- 具体位置：全文
- 问题：论文大量使用因果推断/计量经济学术语（plim, FWL, Wald estimator, column-stochastic polytope, perspective function convexity）。虽然 plim 有脚注定义（method.tex:26 footnote），FWL 有简短解释，但 NLP/CSS 读者可能仍感不适。EMNLP 的主要读者群是 NLP 研究者，而非计量经济学家。
- 建议：在 Notation 部分增加一个简短的"Background for NLP readers"段落，或在附录中提供术语表。

**W6** [minor] 5 个 orphan bib 条目

- 具体位置：references.bib
- 问题：以下 5 条在 .bib 中存在但在正文+附录中均未被引用：`imai_keele_tingley2010`, `miles2024measurement`, `neuhaus1999`, `richardson1993bayesian`, `valeri_vanderweele2014`。
- 建议：删除或在正文中引用。

---

## 小问题（不影响接收）

- Conjecture 1 的措辞："Conjecture" 在数学中通常指精确的、待证明的命题。但 Conjecture 1 依赖于未具体指定的 ε 和 |β| 阈值，更接近 "Empirical Observation" 或 "Working Hypothesis"。建议统一数学用语。
- Section 4.2 "85% of K=3 confusion matrices violate the binary toward-null guarantee" — "violate" 可能造成误解，建议改为 "do not satisfy"，因为 toward-null 是 K=2 的性质，K≥3 本身就不满足，这不是"违反"。
- Limitations 部分极为简短（3 句话），虽然 EMNLP 2026 规则允许精简 Limitations，但缺少对 (a) linear SEM 局限性的充分讨论和 (b) 无真实因果 benchmark 的明确承认，建议略微扩展。

---

## Questions（需要作者回答）

**Q1.** Theorem 1 能否在 K=3 的任何非平凡条件下（如对称混淆矩阵 C_ij = c for i≠j）给出证明？K=2 到 K≥3 的证明难度本质上来自哪里？

**Q2.** Sign-flip rates（83.4% exposure, 52.6% IV）高度依赖 Dirichlet(1,1,1) 先验。在更现实的先验下（如 diagonal-concentrated Dirichlet(5,1,1)），这些比例如何变化？论文提到 realistic accuracy (diagonal ≥ 0.7) 下降至 2.1%——这个范围很大（83.4% → 2.1%），说明先验选择对结论影响极大。

**Q3.** MC-SIMEX 和 MLA 的原始引用来源是什么？请在修改稿中补充。

**Q4.** Introduction 提到 "binarization amplifies this gap 154×"（Appendix）——请简述 154× 的精确含义：是偏差比值、sign-flip 概率比值、还是其他度量？

**Q5.** 论文选择了 7 种"canonical"拓扑，排除了 regression discontinuity、difference-in-differences 等同样常见的因果设计。这一选择的依据是什么？是否会在附录中讨论扩展到其他设计的可行性？

**Q6.** FWL 不变性在 logistic regression 下"breaks but topology ranking persists with deviations < 0.02"（Section 4.5）。在实际 CSS 研究中，logistic regression 远比 linear OLS 常见——这个 < 0.02 的偏差是否足以保证实用指引的可靠性？

---

## Missing References（遗漏的重要相关工作）

1. **Küchenhoff, H., Mwalili, S. M., & Lesaffre, E. (2006).** "A general method for dealing with misclassification in regression: The misclassification SIMEX." *Biometrics*, 62(1), 85-96. — MC-SIMEX 原始论文，论文中广泛使用但完全未引用。**[必须补充]**

2. **Bross, I. D. J. (1954).** "Misclassification in 2×2 tables." *Biometrics*, 10(4), 478-486. — Non-differential misclassification 导致 bias toward the null 的奠基性论文。论文反复引用这一经典结果但仅追溯到 Brenner (1993)。

3. **Yi, G. Y. (2017).** *Statistical Analysis with Measurement Error or Misclassification: Strategy, Method, Application.* Springer. — 测量误差/误分类的综合专著，已引 Shu & Yi (2019a,b) 但遗漏了这本核心参考书。

4. **Hausman, J. A., Abrevaya, J., & Scott-Morton, F. M. (1998).** "Misclassification of the dependent variable in a discrete-response setting." *Journal of Econometrics*, 87(2), 239-269. — 离散变量误分类的经典文献。

5. 论文引用了 Lovell (1963) 作为 FWL 的来源之一，但 **Frisch, R. & Waugh, F. V. (1933)** "Partial time regressions as compared with individual trends." *Econometrica*, 1(4), 387-401 — FWL 定理的原始来源，建议同时引用。

---

## Overall Assessment

**评分: 3.5 / 5 (Borderline Conference)**

**理由：**
本文解决了一个重要且及时的问题——LLM 标注误差在因果推断中的拓扑依赖性传播。Bias taxonomy（7 种拓扑 × K≥3）和实证验证（161 scenarios, 1.6% MAPE）是扎实的实证贡献。safe/fragile 二分法和 F₁ ↔ bias 脱钩的论证对从业者有直接价值。

但论文存在三个核心短板：(1) ASV 单调性——论文的标志性理论贡献——仅在 K=2 下得到证明，K≥3 以 Conjecture 形式呈现，而整篇论文的叙事都围绕 K≥3 的结构性转变展开，理论与叙事之间存在落差；(2) Contribution 3（FWL 不变性）是 FWL 定理的直接推论，不足以支撑一个独立贡献；(3) MC-SIMEX 未引原始论文属于学术规范疏漏。

如果作者能在修改中 (a) 提供 K=3 特殊情况下的 ASV 单调性证明或更强的理论界，(b) 将 FWL 不变性降格并重构第三个贡献，(c) 补充缺失引用，本文有望达到 Conference 水平 (4.0)。当前状态下，实证工作足以支撑 Findings 接收，但理论深度不足以支撑主会议。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1564 · 2026-05-23T17:08:43.906540+00:00_

Reviewer 2 审稿意见已收到（3.5 / Borderline Conference）。核心问题：ASV K≥3 理论空白、Contribution 3 分量不足、MC-SIMEX 缺引用。

等待 Reviewer 1 返回。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 154

## Round 154

2 recorded events


### User

_source line 1565 · 2026-05-23T17:08:46.453111+00:00_

[Reviewer 2 审稿结果]:
审稿意见已提交给 Review Director。

**核心结论**：评分 3.5/5 (Borderline Conference)。

三个主要问题：
1. **ASV 单调性理论空白**：Theorem 1 仅对 K=2 证明，K≥3 以 Conjecture 呈现——但论文叙事核心恰恰是 K≥3 的结构性转变
2. **Contribution 3 分量不足**：FWL 不变性导致 matrix-based correction 无效是 FWL 定理的直接推论，不足以支撑独立贡献
3. **MC-SIMEX 缺少原始引用**：广泛使用但未引 Küchenhoff et al. (2006)

实证工作扎实（161 scenarios, 1.6% MAPE, 真实 LLM 矩阵验证），safe/fragile 二分法对从业者有直接价值。当前水平可支撑 Findings 接收，但理论深度不足以支撑主会议。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1566 · 2026-05-23T17:08:58.109357+00:00_

Reviewer 2 审稿意见已收到。评分 3.5/5（Borderline Conference），核心问题集中在 K≥3 理论空白、Contribution 3 分量不足、MC-SIMEX 引用缺失。

等待 Reviewer 1 返回审稿意见后进入交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 155

## Round 155

8 recorded events


### User

_source line 1567 · 2026-05-23T17:10:36.407302+00:00_

[Reviewer 1 审稿意见]:

## Reviewer 1 审稿意见 — Round 1（方法严谨性 + 理论证明 + 实验验证）

---

## 总体评分
**Overall**: 3.5 (Borderline Conference)
**一句话总结**: K=2 理论扎实、框架新颖、实验覆盖面广，但 K≥3 的核心贡献（Conjecture 1）缺乏证明，proportional effects 假设在 NLP 场景中未经验证，部分数值声称的统计功效存疑。

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | K=2 Theorem 1 证明完整，但 K≥3 框架依赖未证明的 Conjecture 1；proportional effects (f=λg) 假设限制性强且未在 NLP 数据上验证；"2.1% under diagonal≥0.7"声称的样本量可能不足 |
| Excitement | 3.5/5 | 问题重要且及时——LLM 标注 × 因果推断的系统性分析在 NLP 社区有明确需求；ASV 框架有实用价值；但线性 SEM + proportional effects 假设限制了实际影响力 |
| Overall Assessment | 3.5/5 | Borderline Conference——理论贡献（K=2）和框架设计是优势，但 K≥3 理论空白和关键假设未验证阻止了明确的 conference-level 推荐 |
| Confidence | 4/5 | 对因果推断方法论和测量误差模型有专业背景，仔细检查了证明和数值声称 |

---

## Summary

本文研究 K-class non-differential misclassification 在七种典型 DAG 拓扑下的偏差传播，推导了闭合形式的偏差表达式，证明了 K=2 情况下的 envelope monotonicity（Theorem 1），引入了 Annotation Sensitivity Values（ASV）诊断框架，并在 Monte Carlo 模拟和三个真实数据集上进行了验证。论文解决了一个及时的问题：随着 LLM 标注在计算社会科学中的普及，系统理解标注误差对因果估计的影响至关重要。

---

## Strengths（主要优势）

**S1. 新颖且重要的问题建构。** 将多类 LLM 标注误差与因果推断偏差的拓扑依赖性系统关联，这在现有文献中是首次（Section 1, Table 1）。之前的工作要么只考虑二分类（Ogburn & VanderWeele, 2012），要么只覆盖单一 DAG（Wood-Doughty, 2024），本文同时覆盖了七种拓扑。

**S2. Theorem 1（K=2 monotonicity）证明完整且论证结构清晰。** Appendix A.4 的证明使用 perspective function convexity 建立 V_B(δ) 的凸性，结合 V_B(0)=0 推导单调性。对 proportional case 和 general case 的处理分别给出，K=2 的代数推导每一步可验证（pages 13-14）。

**S3. Proposition 7（Exposure sign reversal counterexample, Appendix A.8）是强力构造性结果。** 直接构造了 C_kk > 0.5 仍能导致符号反转的反例，证明 K≥3 的 sign reversal 不是理论上的 pathological case 而是结构性现象。这个反例明确了 K=2 经典衰减 vs K≥3 新行为的分界线。

**S4. 实验覆盖面广。** 100,000 Monte Carlo confusion matrices + 23 empirical LLM configurations + 3 real datasets（HumAID K=10, VAST K=3, CivilComments K=2）+ 161 scenarios 的 theory-MC 对比。这种多层级验证有说服力。

**S5. ASV 框架的三种诊断（magnitude, significance, sign-flip）定义清晰且 FWL invariance 得到证明。** FWL invariance（Appendix B.2, 证明基于列空间保持论证）使得 ASV 对控制变量选择不敏感，这对实际应用至关重要。

**S6. Algorithm 1 的拓扑→校正方法决策流程（Section 4.5, page 8）是实用贡献。** 从 DAG 识别 → ASV 计算 → 方法选择的流程清晰可操作。

**S7. 文献覆盖全面。** 测量误差文献（Carroll et al., Buonaccorsi, Gustafson）、因果推断（Pearl, VanderWeele）、NLP 标注（Gilardi et al., Ziems et al.）均有充分引用。

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] Conjecture 1（K≥3 ε-approximate monotonicity）未证明，但承载了框架的核心实用性

- 具体位置：Section 3.3 (page 5-6), Observation 1, Conjecture 1; Appendix B.12 (Table 10-12)
- 问题：Conjecture 1 声称对 non-IV 拓扑，|B(C(δ))| 在 |β|≤1 时 ε-approximately monotone（ε<0.02）。ASV 的 vulnerability ranking（Table 3）和 Algorithm 1 的决策逻辑在 K≥3 时的有效性完全依赖此 conjecture。然而该 conjecture 仅通过 Dirichlet(1,...,1) 采样进行数值验证（10,000 matrices per cell, K∈{3,5,7}）。Dirichlet 均匀先验无法保证覆盖 adversarial 矩阵结构（如 near-permutation、block-diagonal），ε<0.02 bound 可能在特定结构化矩阵上失效。
- 为什么影响接收：论文的核心新贡献是 K≥3 multi-class 分析——这恰恰是依赖未证明 conjecture 的部分。K=2 的 Theorem 1 虽然严格，但 K=2 non-differential misclassification 的经典衰减结果（Brenner, 1993）已广为人知。如果 K≥3 只能给出 conjecture 而非 theorem，论文的理论贡献就大打折扣。
- 建议修改方向：(a) 至少对某些特殊拓扑（如 confounding）尝试 K≥3 的严格证明；(b) 补充 adversarial/structured confusion matrix 测试（near-permutation, block-diagonal 等）；(c) 如果无法证明，应在 main text 更显著地标注 K≥3 结果的 conjecture 性质，而非在 Observation 1 中以 "envelope monotonicity—K≥3" 为标题暗示普遍性。

**N2** [critical] "2.1% sign reversal under realistic LLM accuracy (diagonal ≥ 0.7)" 声称的统计功效存疑

- 具体位置：Section 4.2 (page 7)，"Under realistic LLM accuracy (diagonal ≥ 0.7), the violation rate is 13.7% with 2.1% sign reversal"
- 问题：该分析似乎是从 100,000 Dirichlet(1,1,1) 样本中后过滤 min_j C_jj ≥ 0.7 的矩阵。对 K=3 Dirichlet(1,1,1)，每行对角线 ≥ 0.7 的概率约为 P(x₁≥0.7) = (1-0.7)²=0.09（Dirichlet(1,1,1) on 3-simplex）。三行同时满足的概率约 0.09³ ≈ 7.3×10⁻⁴，即 100,000 个矩阵中约 73 个通过过滤。2.1% × 73 ≈ 1.5，意味着仅 1-2 个矩阵观察到 sign reversal，95% CI 极宽。这个数字在统计上不可靠。
- 为什么影响接收：Abstract 和 Introduction 都引用了 "realistic accuracy" 下的行为作为核心 claim 的证据。如果该声称基于 ≤100 个矩阵的后过滤分析，可信度不足。
- 建议修改方向：(a) 明确报告通过 diagonal ≥ 0.7 过滤后的矩阵数量；(b) 如果样本量不足，使用 rejection sampling 或 truncated Dirichlet 生成足够多的 high-accuracy 矩阵（如 100,000 个），重新计算 sign reversal rate 及其 CI；(c) 或者改用 23 个 empirical LLM confusion matrices 的分析结果来支撑 "realistic accuracy" 论述。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [major] Proportional effects 假设 (f=λg) 在 NLP 场景中的合理性缺乏讨论和验证

- 具体位置：Theorem 1 conditions (page 5-6), Appendix A.4 Proportional case, Appendix B.13 (Table 13)
- 问题：f=λg 假设要求 misclassified moments 按单一标量线性缩放。Appendix B.13 (Table 13) 显示当该假设不成立时，OOB (out-of-bound) 率达到 23%（K=3 mediation, non-proportional f）。然而论文未讨论在什么样的 NLP classification 任务中 f=λg 近似成立——是某些特定的混淆模式（如均匀误分类）还是所有 column-stochastic 矩阵？对三个 empirical datasets 也未验证该条件。
- 建议：在 Section 3 或 Limitations 中增加 2-3 句讨论 f=λg 在实际标注任务中的合理条件；在 Appendix B.13 增加对 23 个 empirical confusion matrices 的 proportionality 检验。

**W2** [major] 数值不一致：Section 4.2 的 "21 LLM configurations" 与论文其他位置的 "23" 矛盾

- 具体位置：Section 4.2 (page 6): "21 LLM configurations × 7 topologies" → 161 scenarios; Section 3.2 (page 4): "Across 23 empirical LLM configurations"
- 问题：21×7=147≠161，而 23×7=161。论文在 Section 3.2、Section 4.3、Appendix B.10 等处均使用 "23 configurations"。Section 4.2 的 "21" 应是笔误，但在 theory-MC 对比这一关键结果中出现数字错误会削弱对其他数值声称的信任。
- 建议：统一为正确数字（23 或 21），并确认 161 scenarios 的分解。

**W3** [major] 线性 SEM 假设的适用范围需要更明确的边界

- 具体位置：Section 3.1 (Eq. 1-3), Appendix B.14 (Table 15)
- 问题：所有偏差表达式（Eq. 1-3）在线性 SEM 下推导。Appendix B.14 测试了 logistic regression，显示 FWL invariance 不再精确成立（Table 5: |Δ_mean| ~ 10⁻³），且 RMSE reduction 在 exposure topology 下显著不同。然而 main text 的叙述（特别是 Abstract 和 Conclusion）未明确限定 "linear SEM" 适用条件，可能给读者造成结果普遍适用的印象。
- 建议：在 Abstract 或 Introduction 明确提及 "under linear structural equations" 作为 scope qualifier；在 Conclusion 讨论 nonlinear 扩展作为 future work。

**W4** [minor] ASV 参数化 C(δ)=(1-δ)I+δC₀ 的路径依赖性

- 具体位置：Section 3.3 (page 5), Definition of ASV
- 问题：C(δ) 假设误差沿从完美分类到 C₀ 的线性路径退化。实际 LLM 标注误差可能呈非均匀退化模式（某些类别更容易混淆）。ASV ranking 对 alternative degradation paths 的敏感性未讨论。
- 建议：在 Appendix 增加一个 robustness check——比较线性路径 vs 非均匀退化路径下 ASV ranking 的 Spearman 相关。

**W5** [minor] Table 2 的 sign preservation conditions 涉及不可观测量

- 具体位置：Table 2 (page 5), sign preservation conditions
- 问题：Confounding 的充分条件 sign(r)=sign(r+B_DX) 涉及 r 和 B_DX = Cov(g(A),f(A))/Var(f(A))，这些依赖真实 A（非观测 A*）。论文建议用 A*-stratified bootstrapping 估计，但未验证该估计在 realistic misclassification 下的准确性。对实际决策的可操作性有限。
- 建议：在 Section 5 或 Appendix 提供一个 worked example，展示如何用观测数据近似验证 sign preservation conditions。

---

## 小问题（不影响接收）

- Appendix A.8 (page 19) Proposition 7 的反例使用 K=3、C_kk > 0.5。主文可以更早引用此反例来动机化 K≥3 的特殊行为，增强叙事紧凑性。
- Figure 2 (page 5) 的 histogram 颜色区分（红=sign reversal）有效，但 x 轴标签 "Relative Bias" 在不同拓扑间的 scale 差异较大，建议考虑统一 x 轴范围或使用 normalized scale 以便跨拓扑视觉比较。
- Table 3 (page 7) 的 ASV vulnerability ranking 从正文叙述看是论文的 headline result，但 Table 3 本身较小且在密集文本中不够醒目。
- Section 4.4 (page 7) 提到 "Spearman ρ = −0.10, p = 0.45" 用于 macro F₁ 与 causal bias 的相关性——负面结果（annotation quality ≠ causal validity）是重要 insight，但主文讨论不足。

---

## Questions（需要作者回答）

**Q1.** 对 "diagonal ≥ 0.7" 分析产生 2.1% sign reversal 声称：有多少 Dirichlet 矩阵通过了该过滤？如果 <100 个，2.1% 的 95% CI 是多少？

**Q2.** Conjecture 1 的数值验证是否测试了 adversarial confusion matrix 结构（near-permutation, block-diagonal 等）？ε<0.02 bound 是否在 Dirichlet 之外的结构化矩阵上被验证？

**Q3.** 能否提供 NLP 因果推断任务中 f=λg（proportional effects）近似成立 vs 明显不成立的具体示例？这将帮助实践者判断 Theorem 1 的条件是否适用于其场景。

**Q4.** 论文显示 23 个 empirical LLM configurations 中 0% primary coefficient reversal。这是 β 向量结构（一个 dominant coefficient）的产物，还是对任意系数结构都成立？

**Q5.** Algorithm 1 的拓扑→校正方法推荐（PPI++ for confounding, DSL for others）对 K 的敏感性如何？主要分析使用 K=3，K=10（HumAID）的推荐是否一致？

---

## Missing References

未发现关键遗漏。论文对测量误差（Carroll et al., Buonaccorsi, Gustafson）、因果推断（Pearl, VanderWeele, Cinelli & Hazlett）和 NLP 标注（Gilardi et al., Ziems et al., Tan et al.）文献的覆盖全面。

可考虑补充的边缘相关工作：
- Miao, Geng, and Tchetgen Tchetgen (2018) 关于 proxy variable identification 的工作——与 starred-node framework 有方法论联系但论文采用了不同路径（通过 FWL 分解而非 proxy variable）。

---

## 主要优势总结

1. 首次系统地将多类标注误差与拓扑依赖因果偏差关联，填补了 NLP 和因果推断交叉领域的重要空白
2. K=2 Theorem 1 的证明严格且论证优雅
3. ASV 框架有明确的实用价值（FWL invariance + Algorithm 1）
4. 实验覆盖面广（理论-MC 对比 + 经验验证 + 校正方法比较）
5. Proposition 7 的构造性反例有力地证明了 K≥3 新行为的存在性


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 1568 · 2026-05-23T17:10:47.741094+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '执行资料检查和 Venue 调研'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.6/0.7: 派发视觉审查 + Reviewer', 'status': 'completed', 'activeForm': '派发视觉审查和 Reviewer 任务'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'completed', 'activeForm': '等待 Reviewer 独立审稿'}, {'content': 'Step 2: 交叉分享', 'status': 'in_progress', 'activeForm': '执行交叉分享'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断收敛'}, {'content': 'Step 4: 汇总报告 & 投递', 'status': 'pending', 'activeForm': '汇总报告并投递'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '执行资料检查和 Venue 调研'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.6/0.7: 派发视觉审查 + Reviewer', 'status': 'completed', 'activeForm': '派发视觉审查和 Reviewer 任务'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'completed', 'activeForm': '等待 Reviewer 独立审稿'}, {'content': 'Step 2: 交叉分享', 'status': 'in_progress', 'activeForm': '执行交叉分享'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断收敛'}, {'content': 'Step 4: 汇总报告 & 投递', 'status': 'pending', 'activeForm': '汇总报告并投递'}]"
  }
}
```

</details>

---


### Tool result

_source line 1569 · 2026-05-23T17:10:47.791729+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "TodoWrite",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1570 · 2026-05-23T17:11:26.370376+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应：对每个 Must-Fix、Should-Fix、小问题，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 审稿意见 — Round 1\n\n**总体评分**: 3.5 / 5 (Borderline Conference)\n\n### Must-Fix\n\n**N1** [critical] ASV 单调性理论仅覆盖 K=2，与论文核心叙事矛盾\n- Theorem 1 仅对 K=2 + proportional effects 证明，K≥3 以 Conjecture 1 呈现（20,000 随机三元组数值验证）。论文核心叙事围绕 K≥3 结构性转变，但理论基石仅覆盖 K=2——对最不需要理论支撑的简单情况给出证明，对最需要的核心情况给出猜想。ASV 排序在 K≥3 的可靠性因此受质疑。\n\n**N2** [critical] Contribution 3（FWL 不变性 + correction routing）分量不足\n- FWL 定理本身就意味着对协变量的线性变换不改变处理变量系数。Matrix-based correction 是对 dummy 变量的线性变换，因此\"对四种协变量拓扑无效\"是 FWL 直接推论。Section 4.5 两句话即推导完毕——如果一个\"贡献\"可以两句话完成，可能更适合作为 Observation。\n\n### Should-Fix\n\n**W1** [major] MC-SIMEX 未引原始论文 Küchenhoff et al. (2006, Biometrics)，MLA 也缺规范引用。\n\n**W2** [major] \"First systematic topology-specific comparison\" 声称需限定——TeBlunthuis (2024) 已做 4 种拓扑 K=2 比较。\n\n**W3** [major] Proportional effects (f=λg) 可验证性不清——f 和 g 通常不可观测，97.3% 的检验方法和标准未说明。\n\n**W4** [minor] 符号 τ 拓扑依赖定义可能造成混淆——建议下标区分。\n\n**W5** [minor] NLP 读者可及性不足——plim, FWL, Wald, column-stochastic polytope 等术语。\n\n**W6** [minor] 5 个 orphan bib 条目。\n\n### 小问题\n- Conjecture 1 更像 \"Empirical Observation\" 而非数学 Conjecture\n- \"85% violate\" 用词可能误导\n- Limitations 过于简短\n\n### Missing References\n1. Küchenhoff et al. (2006) — MC-SIMEX 原始论文 [必须补充]\n2. Bross (1954) — non-differential bias toward null 奠基论文\n3. Yi (2017) — 测量误差专著\n4. Hausman et al. (1998) — 离散变量误分类经典文献\n5. Frisch & Waugh (1933) — FWL 原始来源\n\n### Questions\nQ1. K=3 特殊情况（如对称混淆矩阵）能否证明？\nQ2. Sign-flip rates 对 Dirichlet 先验选择极敏感（83.4%→2.1%），如何看待？\nQ3. MC-SIMEX/MLA 原始引用？\nQ4. \"154×\" 的精确含义？\nQ5. 为何排除 RDD、DID 等因果设计？\nQ6. Logistic regression 下 <0.02 偏差是否足够？\n\n---\n\n请逐条回应。",
  "project": "causal_annot_error_attrib",
  "chat_id": "oc_9f117624057fcf6cb95db4d67f525246",
  "director_session_key": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应：对每个 Must-Fix、Should-Fix、小问题，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 审稿意见 — Round 1\n\n**总体评分**: 3.5 / 5 (Borderline Conference)\n\n### Must-Fix\n\n**N1** [critical] ASV 单调性理论仅覆盖 K=2，与论文核心叙事矛盾\n- Theorem 1 仅对 K=2 + proportional effects 证明，K≥3 以 Conjecture 1 呈现（20,000 随机三元组数值验证）。论文核心叙事围绕 K≥3 结构性转变，但理论基石仅覆盖 K=2——对最不需要理论支撑的简单情况给出证明，对最需要的核心情况给出猜想。ASV 排序在 K≥3 的可靠性因此受质疑。\n\n**N2** [critical] Contribution 3（FWL 不变性 + correction routing）分量不足\n- FWL 定理本身就意味着对协变量的线性变换不改变处理变量系数。Matrix-based correction 是对 dummy 变量的线性变换，因此\"对四种协变量拓扑无效\"是 FWL 直接推论。Section 4.5 两句话即推导完毕——如果一个\"贡献\"可以两句话完成，可能更适合作为 Observation。\n\n### Should-Fix\n\n**W1** [major] MC-SIMEX 未引原始论文 Küchenhoff et al. (2006, Biometrics)，MLA 也缺规范引用。\n\n**W2** [major] \"First systematic topology-specific comparison\" 声称需限定——TeBlunthuis (2024) 已做 4 种拓扑 K=2 比较。\n\n**W3** [major] Proportional effects (f=λg) 可验证性不清——f 和 g 通常不可观测，97.3% 的检验方法和标准未说明。\n\n**W4** [minor] 符号 τ 拓扑依赖定义可能造成混淆——建议下标区分。\n\n**W5** [minor] NLP 读者可及性不足——plim, FWL, Wald, column-stochastic polytope 等术语。\n\n**W6** [minor] 5 个 orphan bib 条目。\n\n### 小问题\n- Conjecture 1 更像 \"Empirical Observation\" 而非数学 Conjecture\n- \"85% violate\" 用词可能误导\n- Limitations 过于简短\n\n### Missing References\n1. Küchenhoff et al. (2006) — MC-SIMEX 原始论文 [必须补充]\n2. Bross (1954) — non-differential bias toward null 奠基论文\n3. Yi (2017) — 测量误差专著\n4. Hausman et al. (1998) — 离散变量误分类经典文献\n5. Frisch & Waugh (1933) — FWL 原始来源\n\n### Questions\nQ1. K=3 特殊情况（如对称混淆矩阵）能否证明？\nQ2. Sign-flip rates 对 Dirichlet 先验选择极敏感（83.4%→2.1%），如何看待？\nQ3. MC-SIMEX/MLA 原始引用？\nQ4. \"154×\" 的精确含义？\nQ5. 为何排除 RDD、DID 等因果设计？\nQ6. Logistic regression 下 <0.02 偏差是否足够？\n\n---\n\n请逐条回应。",
    "project": "causal_annot_error_attrib",
    "chat_id": "oc_9f117624057fcf6cb95db4d67f525246",
    "director_session_key": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
  }
}
```

</details>

---


### Tool result

_source line 1571 · 2026-05-23T17:11:51.807955+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_9f117624057fcf6cb95db4d67f525246:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 25437
}
```

</details>

---


### Tool call

_source line 1572 · 2026-05-23T17:11:52.461692+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应：对每个 Must-Fix、Should-Fix、小问题，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 审稿意见 — Round 1\n\n**总体评分**: 3.5 (Borderline Conference)\n\n### Must-Fix\n\n**N1** [critical] Conjecture 1（K≥3 ε-approximate monotonicity）未证明，但承载框架核心实用性\n- ASV vulnerability ranking 和 Algorithm 1 在 K≥3 的有效性完全依赖此 conjecture。数值验证仅用 Dirichlet(1,...,1) 采样（10,000 matrices per cell），无法保证覆盖 adversarial 矩阵结构（near-permutation, block-diagonal）。K=2 Theorem 1 虽严格，但 K=2 non-differential misclassification 经典衰减已广为人知。如果 K≥3 只能给出 conjecture，理论贡献大打折扣。\n\n**N2** [critical] \"2.1% sign reversal under realistic LLM accuracy (diagonal ≥ 0.7)\" 统计功效存疑\n- 从 100,000 Dirichlet(1,1,1) 后过滤 min_j C_jj ≥ 0.7 的矩阵。对 K=3，三行同时 ≥ 0.7 的概率约 7.3×10⁻⁴，即约 73 个矩阵通过过滤。2.1% × 73 ≈ 1.5 个矩阵，95% CI 极宽。Abstract 和 Introduction 都引用此数字作为核心 claim 证据，但统计上不可靠。\n\n### Should-Fix\n\n**W1** [major] Proportional effects (f=λg) 在 NLP 场景中合理性缺讨论和验证。Table 13 显示不成立时 OOB 率达 23%（K=3 mediation）。未在 empirical datasets 上验证该条件。\n\n**W2** [major] 数值不一致：Section 4.2 的 \"21 LLM configurations\" 与其他位置 \"23\" 矛盾。21×7=147≠161。\n\n**W3** [major] 线性 SEM 假设适用范围需更明确边界。Abstract/Conclusion 未限定 \"linear SEM\"，可能给读者普遍适用的印象。Logistic regression 下 FWL invariance 不再精确成立。\n\n**W4** [minor] ASV 参数化 C(δ)=(1-δ)I+δC₀ 的路径依赖性未讨论。\n\n**W5** [minor] Table 2 sign preservation conditions 涉及不可观测量，对实际决策可操作性有限。\n\n### 小问题\n- Proposition 7 反例可更早引用\n- Figure 2 x 轴 scale 差异大\n- Table 3 在密集文本中不够醒目\n- F₁ vs bias 负面结果讨论不足\n\n### Questions\nQ1. diagonal ≥ 0.7 过滤后有多少矩阵？2.1% 的 95% CI？\nQ2. Conjecture 1 是否测试了 adversarial 矩阵结构？\nQ3. NLP 中 f=λg 近似成立 vs 不成立的具体示例？\nQ4. 0% primary coefficient reversal 是 β 结构产物还是普遍成立？\nQ5. Algorithm 1 推荐对 K 的敏感性？\n\n### Missing References\n- Miao, Geng, and Tchetgen Tchetgen (2018) — proxy variable identification（边缘相关）\n\n---\n\n请逐条回应。",
  "project": "causal_annot_error_attrib",
  "chat_id": "oc_9f117624057fcf6cb95db4d67f525246",
  "director_session_key": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应：对每个 Must-Fix、Should-Fix、小问题，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 审稿意见 — Round 1\n\n**总体评分**: 3.5 (Borderline Conference)\n\n### Must-Fix\n\n**N1** [critical] Conjecture 1（K≥3 ε-approximate monotonicity）未证明，但承载框架核心实用性\n- ASV vulnerability ranking 和 Algorithm 1 在 K≥3 的有效性完全依赖此 conjecture。数值验证仅用 Dirichlet(1,...,1) 采样（10,000 matrices per cell），无法保证覆盖 adversarial 矩阵结构（near-permutation, block-diagonal）。K=2 Theorem 1 虽严格，但 K=2 non-differential misclassification 经典衰减已广为人知。如果 K≥3 只能给出 conjecture，理论贡献大打折扣。\n\n**N2** [critical] \"2.1% sign reversal under realistic LLM accuracy (diagonal ≥ 0.7)\" 统计功效存疑\n- 从 100,000 Dirichlet(1,1,1) 后过滤 min_j C_jj ≥ 0.7 的矩阵。对 K=3，三行同时 ≥ 0.7 的概率约 7.3×10⁻⁴，即约 73 个矩阵通过过滤。2.1% × 73 ≈ 1.5 个矩阵，95% CI 极宽。Abstract 和 Introduction 都引用此数字作为核心 claim 证据，但统计上不可靠。\n\n### Should-Fix\n\n**W1** [major] Proportional effects (f=λg) 在 NLP 场景中合理性缺讨论和验证。Table 13 显示不成立时 OOB 率达 23%（K=3 mediation）。未在 empirical datasets 上验证该条件。\n\n**W2** [major] 数值不一致：Section 4.2 的 \"21 LLM configurations\" 与其他位置 \"23\" 矛盾。21×7=147≠161。\n\n**W3** [major] 线性 SEM 假设适用范围需更明确边界。Abstract/Conclusion 未限定 \"linear SEM\"，可能给读者普遍适用的印象。Logistic regression 下 FWL invariance 不再精确成立。\n\n**W4** [minor] ASV 参数化 C(δ)=(1-δ)I+δC₀ 的路径依赖性未讨论。\n\n**W5** [minor] Table 2 sign preservation conditions 涉及不可观测量，对实际决策可操作性有限。\n\n### 小问题\n- Proposition 7 反例可更早引用\n- Figure 2 x 轴 scale 差异大\n- Table 3 在密集文本中不够醒目\n- F₁ vs bias 负面结果讨论不足\n\n### Questions\nQ1. diagonal ≥ 0.7 过滤后有多少矩阵？2.1% 的 95% CI？\nQ2. Conjecture 1 是否测试了 adversarial 矩阵结构？\nQ3. NLP 中 f=λg 近似成立 vs 不成立的具体示例？\nQ4. 0% primary coefficient reversal 是 β 结构产物还是普遍成立？\nQ5. Algorithm 1 推荐对 K 的敏感性？\n\n### Missing References\n- Miao, Geng, and Tchetgen Tchetgen (2018) — proxy variable identification（边缘相关）\n\n---\n\n请逐条回应。",
    "project": "causal_annot_error_attrib",
    "chat_id": "oc_9f117624057fcf6cb95db4d67f525246",
    "director_session_key": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
  }
}
```

</details>

---


### Tool result

_source line 1573 · 2026-05-23T17:11:54.141303+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_9f117624057fcf6cb95db4d67f525246:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1679
}
```

</details>

---


### Assistant

_source line 1574 · 2026-05-23T17:11:57.693744+00:00_

交叉分享已派发，等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 156

## Round 156

2 recorded events


### User

_source line 1575 · 2026-05-23T17:12:00.266514+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

**审稿结论**：Overall 3.5（Borderline Conference）。

核心判断：
- **K=2 理论贡献扎实**（Theorem 1 证明完整，Proposition 7 counterexample 有力）
- **K≥3 是主要理论缺口**——Conjecture 1 未证明但承载了 ASV 框架在 K≥3 时的全部有效性
- **两个数值问题**：Section 4.2 的 "21 vs 23" LLM configurations 不一致；"2.1% under diagonal≥0.7" 声称可能基于极小样本（~73 个矩阵）
- **proportional effects (f=λg) 假设**限制性强，OOB 率达 23%（Appendix B.13），但在 NLP 场景中未验证

标记了 2 个 critical（N1: Conjecture 1 未证明, N2: 2.1% 统计功效）、3 个 major（W1-W3）、2 个 minor（W4-W5）问题，以及 5 个需要作者回答的 questions。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1576 · 2026-05-23T17:12:04.509609+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 157

## Round 157

2 recorded events


### User

_source line 1577 · 2026-05-23T17:14:26.564726+00:00_

[Reviewer 1 审稿意见]:

## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应

---

### Must-Fix

**[AGREE] R2-N1: ASV 单调性理论仅覆盖 K=2，与论文核心叙事矛盾**

同意。这与我的 N1 判断一致。论文的核心新贡献恰恰是 K≥3 的 multi-class 行为（sign reversal, topology-dependent vulnerability），但 Theorem 1 仅覆盖 K=2——而 K=2 的经典衰减（attenuation toward null）已有 Brenner (1993) 等充分讨论。Conjecture 1 的数值验证（Appendix B.12, Table 10-12, K∈{3,5,7}, Dirichlet(1,...,1) 采样）是认真的工作，但 Dirichlet 均匀采样无法覆盖 adversarial matrix structures。这是本文最大的理论空白。

补充我的发现：Appendix A.4 (pages 13-14) 的 K=2 证明使用 perspective function convexity + V_B(0)=0 建立单调性，该论证方法在结构上依赖 2×2 矩阵的代数简化（Step 4 明确 "for K=2 only"），无法直接推广到 K≥3。

**[AGREE with qualification] R2-N2: Contribution 3（FWL invariance + correction routing）分量不足**

部分同意 R2 的观点。FWL invariance 本身确实是 FWL 定理的直接推论：如果 A 作为协变量出现，对其 dummy 变量的线性变换（包括 C⁻¹ 校正）不改变处理变量系数——这从 FWL 的列空间保持性质直接可得。R2 说 "两句话即推导完毕" 准确描述了 FWL invariance result 本身的理论深度。

但我认为 Contribution 3 的价值不仅在于 FWL invariance 这一观察，还包括：
1. **Algorithm 1 (page 32)** 提供了从 DAG 识别到校正方法选择的完整决策流程——这超越了单纯的 FWL 推论
2. **Appendix B.14 (Table 15)** 测试了 logistic regression 下 FWL invariance 的近似有效性——在非线性模型下 FWL 不精确成立，因此验证其近似有效性有实际意义
3. **Table 4** 的五种方法跨拓扑比较（210 configurations）提供了实践指导

建议作者将 FWL invariance 降级为 Observation（如 R2 建议），但保留 correction routing + Algorithm 1 作为 practical contribution 的一部分。

---

### Should-Fix

**[AGREE] R2-W1: MC-SIMEX 未引 Küchenhoff et al. (2006, Biometrics)，MLA 缺规范引用**

同意。MC-SIMEX 的原始方法论文是 Küchenhoff, Mwalili, and Lesaffre (2006, Biometrics)，论文使用了该方法（Section 4.5, Table 4）但未引用原始来源，这是引用规范问题。我在审查参考文献（pages 9-11）时也未找到该引用。

**[AGREE with nuance] R2-W2: "First systematic topology-specific comparison" 声称需限定**

同意需要限定。论文在 Section 2 (page 2) 确实引用了 TeBlunthuis et al. (2024)："extending prior single-topology analyses (Brenner, 1993; TeBlunthuis et al., 2024)"，表明作者知晓该工作。但 "first systematic" 的声称需限定为 "first *multi-class* (K≥3) systematic topology-specific comparison"，因为 TeBlunthuis 已做 K=2 + 4 topologies 的比较。论文的增量贡献在于 K≥3 + 7 topologies + closed-form bias expressions，这些确实是新的。

**[AGREE] R2-W3: Proportional effects (f=λg) 可验证性不清**

同意。这与我的 W1 判断一致。论文在 page 5 声称 "97.3% of empirical LLM configurations satisfy the condition"，但 f 和 g 依赖于真实 A（非观测 A*），其可验证性标准不明确。从 Appendix B.13 (Table 13) 看，论文使用 A(C)∈[0,1]（attenuation coefficient 是否在合理范围内）作为 proxy 检验，但这是 proportional effects 的必要条件而非充分条件。R2 要求说明检验方法和判定标准是合理的。

**[AGREE] R2-W4: 符号 τ 拓扑依赖定义可能造成混淆**

同意。τ 在不同拓扑下代表不同的 total effect（如 confounding 下是 β + omitted variable bias，mediation 下是 total effect through mediator + direct），但论文未用下标区分。对跨拓扑比较（如 Table 3）的读者来说，这确实是可读性障碍。

**[AGREE] R2-W5: NLP 读者可及性不足**

同意。EMNLP 是 NLP venue，目标读者主要是 NLP 研究者，而非统计学家。plim（概率极限）、FWL（Frisch-Waugh-Lovell 分解）、Wald estimator、column-stochastic polytope 等术语在计量经济学/因果推断中常用，但对 NLP 读者可能不熟悉。建议在首次使用时添加简短直觉解释（如 "plim (the value an estimator converges to as N→∞)"）。论文目前在 Definition 1 对 non-differential misclassification 提供了清晰定义，但其他术语的处理不够一致。

**[AGREE] R2-W6: 5 个 orphan bib 条目**

同意。orphan entries 应清理。我未独立验证具体是哪 5 个条目，但 R2 的观察应被接受。

---

### 小问题

**[REBUT] R2: Conjecture 1 更像 "Empirical Observation" 而非数学 Conjecture**

不同意。在数学传统中，conjecture 是一个精确表述的、被认为为真但尚未证明的命题。Conjecture 1 给出了精确的定量声称（ε-approximate monotonicity，ε<0.02 for |β|≤1, non-IV topologies），具有可证伪性——如果有人找到一个 non-IV topology 下 |β|≤1 但 ε>0.02 的反例，即可推翻。"Empirical Observation" 则暗示纯描述性发现，不含可证伪的定量约束。论文选择 "Conjecture" 是诚实且精确的：它承认缺乏证明，同时表明作者相信该结论成立，这比 "Observation" 更有信息量。

**[AGREE] R2: "85% violate" 用词可能误导**

同意。"85% of K=3 confusion matrices violate the binary 'round-off' guarantee"（Section 4.2, page 7）在不加 "under uniform Dirichlet(1,1,1) prior" 限定的情况下，可能被读者误解为 "85% of realistic scenarios have violations"。实际上 Dirichlet(1,1,1) 生成大量极低准确率（E[diagonal]=1/K≈0.33）的矩阵，与实际 LLM 标注器相差甚远。建议在首次提及该数字时立即注明先验分布。

**[REBUT] R2: Limitations 过于简短**

不同意。根据 EMNLP 2026 投稿规则，Limitations 章节只需覆盖 3 个左右核心限制点，不需要写得很长。论文的 Limitations section (page 8) 覆盖了 non-differential misclassification assumption、linear SEM 限制、Monte Carlo vs end-to-end benchmarks——这三个点恰好对应最重要的假设限制。过长的 Limitations 部分在页数限制（8 页正文）下会挤压其他内容。

---

### Missing References

**[AGREE] Küchenhoff et al. (2006)** — MC-SIMEX 原始论文，必须引用。论文使用了该方法但未引原始来源。

**[AGREE] Bross (1954)** — non-differential bias toward the null 的奠基工作。论文引用了 Brenner (1993) 但 Bross (1954) 是更原始的来源，在讨论 non-differential misclassification 的历史背景时应引用。

**[AGREE with reservation] Yi (2017)** — 测量误差综合专著。值得引用但非 critical——论文已引用了 Carroll et al. (2006)、Buonaccorsi (2010)、Gustafson (2004) 三本测量误差专著/教材。

**[AGREE with reservation] Hausman et al. (1998)** — 离散变量误分类经典文献。如果未引用，值得补充。但需确认论文是否已在参考文献中包含该条目（我在 pages 9-11 的引用列表中未确认到）。

**[AGREE] Frisch & Waugh (1933)** — 论文大量使用 "Frisch-Waugh-Lovell" 术语（Section 3.1, 4.5, Appendix B.2），引用了 Lovell (1963) 但似乎未引原始 1933 年论文。对于以 FWL 为核心方法论工具的论文，这是应补充的。

---

### Questions 回应

**R2-Q1: K=3 特殊情况（对称混淆矩阵）能否证明？**
好问题。对称矩阵（C_ij = C_ji）的代数结构更简单，可能允许 K=3 的严格证明。这是我在 N1 建议中提到的 "至少对某些特殊拓扑/矩阵结构尝试 K≥3 的严格证明" 的具体方向之一。

**R2-Q2: Sign-flip rates 对 Dirichlet 先验选择极敏感（83.4%→2.1%）**
同意这是重要 concern。这与我的 N2 一致——83.4% 来自 Dirichlet(1,1,1)（E[diagonal]=1/3），2.1% 来自 diagonal≥0.7 子集。但如我在 N2 中指出，diagonal≥0.7 子集的样本量可能极小（~70/100,000），使 2.1% 的估计不可靠。论文应使用 rejection sampling 生成足够多的 high-accuracy 矩阵来提供可靠估计。

**R2-Q3: MC-SIMEX/MLA 原始引用**
已在 W1 和 Missing References 中 [AGREE]。

**R2-Q4: "154×" 的精确含义**
我在审读全文时未找到 "154×" 这一具体数字。如果 R2 指的是某个特定倍数声称，请提供具体 Section/page 引用以便核实。论文在 page 1-2 提到 "relative bias varies by an order of magnitude across topologies (from 4.1% to 42.1%)"，比例约 10:1，非 154×。

**R2-Q5: 为何排除 RDD、DID 等因果设计**
合理的 scope 选择。RDD 和 DID 是准实验设计，其识别策略不同于 DAG-based SEM（依赖 running variable 或 parallel trends 而非条件独立性）。将标注误差传播分析扩展到这些设计需要不同的数学框架，适合作为 future work 而非当前论文的缺陷。

**R2-Q6: Logistic regression 下 <0.02 偏差是否足够？**
这取决于应用场景。Appendix B.14 (Table 5) 显示 logistic regression 下 |Δ_mean| ~ 10⁻³，是绝对偏差而非相对偏差。对于处理效应估计（通常关注 sign 和 magnitude），<0.02 的绝对偏差通常可忽略。但 R2 的隐含问题是有道理的：多个协变量各有 <0.02 偏差时是否会累积？论文未讨论多变量误差的复合效应。

---

### 总结

R2 的审稿意见总体准确。在 7 个 Should-Fix/Minor 项中，我同意 6 项（W1-W6），对 1 项提出不同看法（Limitations 长度符合 EMNLP 2026 规则）。对 2 个 Must-Fix 项，我同意 N1（K≥3 理论空白）并部分同意 N2（FWL invariance 本身确为 trivial corollary，但 Contribution 3 的完整范围包括 Algorithm 1 和经验比较，不应完全否定）。Missing References 的 5 项建议中，Küchenhoff et al. (2006) 和 Frisch & Waugh (1933) 是 must-add，其余 3 项为 nice-to-have。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1578 · 2026-05-23T17:14:33.107824+00:00_

Reviewer 1 交叉回应已收到，等待 Reviewer 2 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 158

## Round 158

2 recorded events


### User

_source line 1579 · 2026-05-23T17:14:37.268327+00:00_

[Reviewer 1 审稿结果]:
已提交对 Reviewer 2 的逐条回应。主要判断：

- **N1 (K≥3 conjecture)**: [AGREE] — 与我的 N1 一致，这是本文最大理论空白
- **N2 (FWL invariance)**: [AGREE with qualification] — FWL invariance 本身确实 trivial，但 Algorithm 1 + 经验比较有附加价值
- **W1-W6**: 6 项中同意 5 项（W1-W5, W6），仅对 Limitations 长度 [REBUT]（符合 EMNLP 2026 规则）
- **小问题**: 对 Conjecture 1 术语 [REBUT]（conjecture 比 observation 更精确），对 "85% violate" 和 Limitations [AGREE/REBUT] 分别处理
- **Missing References**: Küchenhoff (2006) 和 Frisch & Waugh (1933) 为 must-add

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1580 · 2026-05-23T17:14:43.054505+00:00_

收到 Reviewer 1 的交叉回应。等待 Reviewer 2 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 159

## Round 159

20 recorded events


### User

_source line 1581 · 2026-05-23T17:15:35.766486+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 对 Reviewer 1 意见的逐条回应

---

### Must-Fix

**[AGREE] R1-N1: Conjecture 1 未证明，承载框架核心实用性**

同意。这与我的 N1 完全一致。补充两点：

(a) R1 指出数值验证仅用 Dirichlet(1,...,1) 采样，无 adversarial 矩阵结构——这一点很重要。Appendix Table 10（Conjecture DGP sensitivity）虽然测试了不同 β 配置，但混淆矩阵仍来自 Dirichlet 分布，未测试 near-permutation 或 block-diagonal 等极端结构。Conjecture 1 的 ε < 0.02 边界可能在这些结构下不成立。

(b) 进一步说，即使 K=2 的 Theorem 1 也需要 proportional effects (f = λg) 和 (C₀)_jj ≥ 1/2 两个限定条件。这意味着即使在 K=2 的"已证明"情况下，理论也不是无条件的。论文应更明确地传达这些限制。

**[AGREE] R1-N2: "2.1% sign reversal at diagonal ≥ 0.7" 统计功效存疑**

部分同意，但需修正 R1 的估算。

R1 的计算（从 100K Dirichlet(1,1,1) 后过滤，约 73 个矩阵通过）是合理的*如果*主文确实使用了后过滤法。然而，附录的 IV 子空间分析（Appendix B.4, Table 7, line 944-945）明确说明使用了 truncated Dirichlet sampling："restricting the sample space to {C : min_k C_kk ≥ d} for d ∈ {0, 0.5, 0.7, 0.9} (100,000 random matrices per threshold)"——即每个阈值独立采样 100K 矩阵。同样，非差异假设压力测试（Appendix B.7, Table 8）使用 "min_k C_kk ≥ 0.7, 10,000 random matrices per ε"。

问题在于：主文 Section 4.2 的 2.1% 没有说明是后过滤还是 truncated sampling。如果是后过滤（如 R1 推测），则 R1 的功效担忧完全成立；如果是 truncated sampling（如附录），则样本量充足。论文需要在主文中明确标注采样方法和有效样本量。

综合判断：R1 的核心关切（presentation 不足以支撑 claim 的统计可靠性）是正确的，但 severity 可能从 critical 降为 major——如果作者能证实主文使用了 truncated sampling 或补充实验。

---

### Should-Fix

**[AGREE] R1-W1: Proportional effects 在 NLP 场景中的验证不足**

同意，与我的 W3 一致。补充数据：Appendix Table 13 显示，当 f⊥g（完全独立）时，λ(C) OOB 率达 22.9%。虽然 sign failure rate 仍低于 1%（因为 λ 越界幅度通常较小），但 OOB 率本身说明 Theorem 1 的前提在非平凡场景下确实不满足。论文的 "97.3% satisfy the condition"（Section 3.3）来源不够透明——Appendix Table 14 的 "NLP-realistic DGP" 仅测试了一种 DGP 配置（δ=[0, 0.8, −0.6], β=[0, 1.0, −0.5]），97.3% 可能仅指 "在这一特定 DGP 下 23 个 LLM 配置中有多少满足"，而非一般性结论。

**[REBUT] R1-W2: "21 vs 23 configurations" 数值不一致**

我在论文全文中搜索了所有出现的数字：experiments.tex 中无任何 "21" 的出现（验证：`grep -n '\b21\b' experiments.tex` 返回空结果）。正文始终使用 "23 LLM configurations"（Section 3.2 line 53, Section 4.2 line 15, Section 4.4 line 64-67）。23 × 7 = 161 scenarios，与全文一致。

R1 可能将附录中 Table 21（Within-topology Spearman ρ 表的*表号* 21）误读为 "21 configurations"，或是 Figure 7 caption 中 "8 LLM configurations"（HumAID 子集）的混淆。建议 Director 让 R1 核实具体位置。

**如果 R1 能指出 "21" 出现的具体位置，我愿意修改判断；但基于我的全文检索，这一不一致可能是 R1 的误读。**

**[AGREE] R1-W3: 线性 SEM 假设需更明确边界**

同意，与我的审稿意见一致。Abstract 和 Conclusion 均未限定 "linear SEM"，可能给读者普遍适用的印象。Appendix Table（FWL nonlinear, Section B.9）显示 logistic regression 下 FWL invariance breaks（偏差 < 0.02），但主文对此的讨论仅一句话（Section 4.5: "Under logistic regression, FWL invariance breaks but topology ranking and sign-preservation patterns persist with deviations < 0.02"）。应在 Abstract 或 Contribution 列表中加入 "under linear structural equation models" 限定。

**[AGREE] R1-W4: C(δ) 路径依赖性未讨论**

同意。C(δ) = (1−δ)I + δC₀ 是一条从 I 到 C₀ 的线性路径，但 column-stochastic polytope 中存在无数从 I 到 C₀ 的路径（如经过某个 permutation matrix 的路径）。不同路径上的 ASV 阈值可能不同。论文建议 "bootstrapping C₀"（Section 3.3, method.tex:86）部分缓解了 C₀ 选择的任意性，但路径形状（线性 vs 非线性插值）的影响完全未讨论。这不应是 blocking issue，但值得在 Limitations 或 ASV 定义处简短承认。

**[AGREE] R1-W5: Table 2 sign preservation conditions 涉及不可观测量**

同意。Proposition 1 中 confounding 的条件 sign(τ) = sign(τ + B_OV)（其中 B_OV = Cov(g(A), f(A))/Var(T)）和 collider 的条件 |τ| > √(Var(g)Var(h)) / E[Var(T|A)] 都涉及真实（不可观测）的因果参数。对从业者来说，这些条件的可操作性有限——你需要知道真实效应才能判断 sign preservation 是否成立，但如果你已知真实效应就不需要担心 sign reversal 了。

不过，论文在 Table 1 的 τ_sf=0? 列中用 "Cond." 而非 "Yes" 标注了这些拓扑，并在实证中验证了 0% 违反率（100K 矩阵），所以实际影响有限——实证证据比分析条件更有说服力。

---

### 小问题

**[AGREE] R1: Proposition 7 反例可更早引用** — 同意，早引有助读者理解 K≥3 的结构性差异。

**[AGREE] R1: Figure 2 x 轴 scale 差异大** — 同意，不同拓扑的 bias 分布范围相差数量级，统一 x 轴 scale 有助比较。

**[AGREE] R1: Table 3 在密集文本中不够醒目** — 同意，Table 3（ASV ranking）嵌入在大量文本中，视觉层次不清。

**[REBUT] R1: F₁ vs bias 负面结果讨论不足** — 论文在 Section 4.4 和 Figure 4 中对此有较充分的讨论：(a) 总体 Spearman ρ = −0.10, p = 0.45；(b) per-topology 分解（Appendix Table 21）揭示了 5 种拓扑的负相关和 M-bias 的正相关异常。我认为这一结果的讨论已足够。如果 R1 指的是"为什么 F₁ 不能预测因果偏差"的*机制*讨论，那确实可以加强——但这更多是 interpretation 层面的，不是方法论缺陷。

---

### Questions 回应

**Q1. diagonal ≥ 0.7 过滤后样本量和 CI？** — 如上 N2 回应所述，附录中 IV 和 stress test 使用 truncated sampling（每阈值 100K 或 10K），但主文 Section 4.2 的 2.1% 未明确说明方法。需要作者澄清。

**Q2. Conjecture 1 是否测试了 adversarial 矩阵？** — 同意这是关键问题。据我阅读，Appendix Table 10 仅测试了不同 β 配置和 DGP，混淆矩阵仍来自随机 Dirichlet。Near-permutation 矩阵和 block-diagonal 矩阵是合理的 adversarial cases。

**Q3. f=λg 示例？** — 同意需要具体 NLP 示例。Appendix Table 13 的 "NLP-realistic DGP" 仅一个配置，不足以代表 NLP 任务的多样性。

**Q4. 0% primary coefficient reversal 是 β 结构产物还是普遍成立？** — 有意思的问题。论文 method.tex:53 说"across six beta-ratio conditions (1.0 to 50.0) with 0% primary sign-flip"，但所有测试的 β 似乎都有一个明确的 dominant category。如果 β₁ ≈ β₂（无明确 dominant），primary 的定义模糊化，0% 可能是定义上的 artifact。建议作者测试 β₁ = β₂ 的边界情况。

**Q5. Algorithm 1 推荐对 K 的敏感性？** — Appendix B.13（correction K sensitivity, Table in Section 4.5 reference）报告 Spearman ρ ≥ 0.80 across K=3,5,10，表明排序稳定。我认为论文对此的回答是充分的，虽然 K=10 时 PPI++ 对 IV 的 −124% 有必要引起注意。

---

### Missing References

**[AGREE] R1: Miao, Geng, and Tchetgen Tchetgen (2018) — proximal causal inference** — 边缘相关但值得引用。Proximal causal inference 为 mismeasured variables 提供了 identification 策略（通过 proxy variables），与本文的 starred-node DAG 框架有概念联系。在 Related Work 的 measurement error 段落中简要提及即可。

---

### 总结

R1 和我（R2）对 N1（Conjecture 1 未证明）和线性 SEM 限定有高度共识。R1 的 N2（2.1% 统计功效）是我遗漏的有价值的审稿意见，虽然 severity 可能因 truncated sampling 而从 critical 降为 major。R1 的 W2（21 vs 23 不一致）经我核实后未能复现，可能是误读。

整体上，R1 和我的评分一致（均为 3.5），关注的核心问题高度重叠（理论空白、overclaiming、线性假设限制），说明这些确实是论文需要解决的关键问题。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1582 · 2026-05-23T17:15:47.145915+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '执行资料检查和 Venue 调研'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.6/0.7: 派发视觉审查 + Reviewer', 'status': 'completed', 'activeForm': '派发视觉审查和 Reviewer 任务'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'completed', 'activeForm': '等待 Reviewer 独立审稿'}, {'content': 'Step 2: 交叉分享', 'status': 'completed', 'activeForm': '执行交叉分享'}, {'content': 'Step 3: 收敛判断', 'status': 'in_progress', 'activeForm': '判断收敛'}, {'content': 'Step 4: 汇总报告 & 投递', 'status': 'pending', 'activeForm': '汇总报告并投递'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '执行资料检查和 Venue 调研'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.6/0.7: 派发视觉审查 + Reviewer', 'status': 'completed', 'activeForm': '派发视觉审查和 Reviewer 任务'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'completed', 'activeForm': '等待 Reviewer 独立审稿'}, {'content': 'Step 2: 交叉分享', 'status': 'completed', 'activeForm': '执行交叉分享'}, {'content': 'Step 3: 收敛判断', 'status': 'in_progress', 'activeForm': '判断收敛'}, {'content': 'Step 4: 汇总报告 & 投递', 'status': 'pending', 'activeForm': '汇总报告并投递'}]"
  }
}
```

</details>

---


### Tool result

_source line 1583 · 2026-05-23T17:15:47.196657+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "TodoWrite",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1584 · 2026-05-23T17:16:31.610687+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '执行资料检查和 Venue 调研'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.6/0.7: 派发视觉审查 + Reviewer', 'status': 'completed', 'activeForm': '派发视觉审查和 Reviewer 任务'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'completed', 'activeForm': '等待 Reviewer 独立审稿'}, {'content': 'Step 2: 交叉分享', 'status': 'completed', 'activeForm': '执行交叉分享'}, {'content': 'Step 3: 收敛判断', 'status': 'completed', 'activeForm': '判断收敛'}, {'content': 'Step 4: 汇总报告 & 投递', 'status': 'in_progress', 'activeForm': '汇总报告并投递'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '执行资料检查和 Venue 调研'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.6/0.7: 派发视觉审查 + Reviewer', 'status': 'completed', 'activeForm': '派发视觉审查和 Reviewer 任务'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'completed', 'activeForm': '等待 Reviewer 独立审稿'}, {'content': 'Step 2: 交叉分享', 'status': 'completed', 'activeForm': '执行交叉分享'}, {'content': 'Step 3: 收敛判断', 'status': 'completed', 'activeForm': '判断收敛'}, {'content': 'Step 4: 汇总报告 & 投递', 'status': 'in_progress', 'activeForm': '汇总报告并投递'}]"
  }
}
```

</details>

---


### Tool result

_source line 1585 · 2026-05-23T17:16:31.611053+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1586 · 2026-05-23T17:16:32.514976+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "causal_annot_error_attrib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "causal_annot_error_attrib"
  }
}
```

</details>

---


### Tool result

_source line 1587 · 2026-05-23T17:16:32.615825+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-23T16:59:33.664915+00:00\", \"completed_at\": \"2026-05-23T17:04:33.841388+00:00\", \"findings\": [{\"severity\": \"info\", \"dimension\": \"agent_error\", \"message\": \"[ERROR] Agent timed out after 300s\"}], \"counts\": {\"critical\": 0, \"warning\": 0, \"info\": 1}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1588 · 2026-05-23T17:16:32.616339+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "causal_annot_error_attrib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "causal_annot_error_attrib"
  }
}
```

</details>

---


### Tool result

_source line 1589 · 2026-05-23T17:16:32.666670+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1590 · 2026-05-23T17:17:20.242264+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_issues.yaml 2>&1 | wc -l",
  "description": "Check issues file length"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_issues.yaml 2>&1 | wc -l",
    "description": "Check issues file length"
  }
}
```

</details>

---


### Tool result

_source line 1591 · 2026-05-23T17:17:20.343040+00:00_

806

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1592 · 2026-05-23T17:17:23.507720+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_issues.yaml 2>&1",
  "description": "Read full review issues tracker",
  "timeout": "10000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_issues.yaml 2>&1",
    "description": "Read full review issues tracker",
    "timeout": "10000"
  }
}
```

</details>

---


### Tool result

_source line 1593 · 2026-05-23T17:17:23.559106+00:00_

issues:
  # === Round 1-7 历史 (resolved，保留摘要) ===

  - id: R1-N1
    category: soundness
    severity: must-fix
    summary: "Theorem 1 适用范围过窄（仅 confounding+proportional effects），K≥3 证明不完整"
    status: resolved
    first_raised_round: 1
    last_seen_round: 7
    resolution: "Theorem 1 现正确限定为 K=2；K≥3 由 Observation 1 和 Conjecture 1 覆盖。"
    resolution_round: 7

  - id: R1-N2
    category: soundness
    severity: should-fix
    summary: "3/5 安全拓扑的符号保持仅有数值验证，Abstract 用 'establish' 暗示已证明"
    status: resolved
    first_raised_round: 1
    last_seen_round: 3
    resolution: "Abstract 已准确区分 prove/verify。"
    resolution_round: 4

  - id: R1-N3
    category: soundness
    severity: must-fix
    summary: "ASV C(δ) 定义域错误"
    status: resolved
    first_raised_round: 1
    last_seen_round: 1
    resolution: "Section 3.3 已引入 δ_max 约束。"
    resolution_round: 2

  - id: R2-N1
    category: presentation
    severity: must-fix
    summary: "83.4% sign reversal headline framing 过度声称"
    status: resolved
    first_raised_round: 1
    last_seen_round: 5
    resolution: "Introduction 已重写。"
    resolution_round: 5

  - id: R2-N2
    category: novelty
    severity: should-fix
    summary: "'first systematic framework' 过度声明"
    status: resolved
    first_raised_round: 1
    last_seen_round: 1
    resolution: "已修复。"
    resolution_round: 2

  - id: R2-N3
    category: related_work
    severity: must-fix
    summary: "4 篇关键相关工作未引用"
    status: resolved
    first_raised_round: 1
    last_seen_round: 1
    resolution: "已修复。"
    resolution_round: 2

  - id: R1-W2
    category: clarity
    severity: should-fix
    summary: "Sign preservation 的 DGP 条件在实践中难以事前验证"
    status: resolved
    first_raised_round: 1
    last_seen_round: 2
    resolution: "Section 3.2 已添加 ASV 替代讨论。"
    resolution_round: 3

  - id: R1-W3
    category: experiments
    severity: should-fix
    summary: "实证验证不完整：缺少商业 LLM"
    status: in_progress
    first_raised_round: 1
    last_seen_round: 18
    mentions:
      - roun
…[truncated 20835 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Bash",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1594 · 2026-05-23T17:20:29.697787+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "causal_annot_error_attrib",
  "issues_yaml": "issues:\n  # === Round 1-7 历史 (resolved，保留摘要) ===\n\n  - id: R1-N1\n    category: soundness\n    severity: must-fix\n    summary: \"Theorem 1 适用范围过窄（仅 confounding+proportional effects），K≥3 证明不完整\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 7\n    resolution: \"Theorem 1 现正确限定为 K=2；K≥3 由 Observation 1 和 Conjecture 1 覆盖。\"\n    resolution_round: 7\n\n  - id: R1-N2\n    category: soundness\n    severity: should-fix\n    summary: \"3/5 安全拓扑的符号保持仅有数值验证，Abstract 用 'establish' 暗示已证明\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 3\n    resolution: \"Abstract 已准确区分 prove/verify。\"\n    resolution_round: 4\n\n  - id: R1-N3\n    category: soundness\n    severity: must-fix\n    summary: \"ASV C(δ) 定义域错误\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Section 3.3 已引入 δ_max 约束。\"\n    resolution_round: 2\n\n  - id: R2-N1\n    category: presentation\n    severity: must-fix\n    summary: \"83.4% sign reversal headline framing 过度声称\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    resolution: \"Introduction 已重写。\"\n    resolution_round: 5\n\n  - id: R2-N2\n    category: novelty\n    severity: should-fix\n    summary: \"'first systematic framework' 过度声明\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"已修复。\"\n    resolution_round: 2\n\n  - id: R2-N3\n    category: related_work\n    severity: must-fix\n    summary: \"4 篇关键相关工作未引用\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"已修复。\"\n    resolution_round: 2\n\n  - id: R1-W2\n    category: clarity\n    severity: should-fix\n    summary: \"Sign preservation 的 DGP 条件在实践中难以事前验证\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"Section 3.2 已添加 ASV 替代讨论。\"\n    resolution_round: 3\n\n  - id: R1-W3\n    category: experiments\n    severity: should-fix\n    summary: \"实证验证不完整：缺少商业 LLM\"\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 19\n    mentions:\n      - round: 7\n        reviewers: [R2]\n        note: \"Limitations 中讨论即可。\"\n      - round: 14\n        reviewers: [R1, R2]\n        note: \"R14 共识：minor。\"\n      - round: 15\n        reviewers: [R1, R2]\n        note: \"R15 共识：should-fix（低优先级），Limitations 已覆盖。\"\n      - round: 16\n        reviewers: [R1, R2]\n        note: \"R16 R1-M2 再提为 minor。\"\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"R17 共识 should-fix（低优先级）。\"\n      - round: 18\n        reviewers: [R1]\n        note: \"R18 R1-W1 再提 Dirichlet 采样代表性。\"\n      - round: 19\n        reviewers: []\n        note: \"R19 未单独提出。Limitations 已覆盖。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R2-W2\n    category: presentation\n    severity: should-fix\n    summary: \"98 场景 zero sign reversals 与 sign reversal narrative 的 tension\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"已解决。\"\n    resolution_round: 2\n\n  - id: R2-W3\n    category: method\n    severity: should-fix\n    summary: \"ASV 对 C₀ 估计不确定性的敏感性\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"Bootstrap ASV 分析已完成。\"\n    resolution_round: 3\n\n  - id: R2-W4\n    category: scope\n    severity: should-fix\n    summary: \"线性 SEM 假设限制；Algorithm 1 缺 linear-only caveat\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    resolution: \"Section 4.5 FWL 段加 'Under linear OLS' 限定。\"\n    resolution_round: 5\n\n  - id: R1-W4\n    category: experiments\n    severity: should-fix\n    summary: \"MC MAPE 报告不充分\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"已修复。\"\n    resolution_round: 2\n\n  - id: MISC-1\n    category: presentation\n    severity: minor\n    summary: \"符号不统一（τ vs β_T）、Proposition 编号不一致\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    resolution: \"method.tex 添加 τ 在各拓扑下含义的明确说明。\"\n    resolution_round: 5\n\n  - id: NEW-1\n    category: soundness\n    severity: must-fix\n    summary: \"Non-differential misclassification 假设讨论不足\"\n    status: in_progress\n    first_raised_round: 2\n    last_seen_round: 19\n    mentions:\n      - round: 14\n        reviewers: [R1, R2]\n        note: \"R14 共识 minor。\"\n      - round: 15\n        reviewers: [R1, R2]\n        note: \"R15 共识 should-fix。\"\n      - round: 16\n        reviewers: [R1, R2]\n        note: \"R16 R1-W1 + R2-Q2 再提。\"\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"R17 共识 should-fix。\"\n      - round: 18\n        reviewers: [R1, R2]\n        note: \"R18 升级为 must-fix。R18 fix 完成。\"\n      - round: 19\n        reviewers: []\n        note: \"R19 未单独提出。R18 修复（architectural invariant + Y-stratified permutation test）在 §3.1 中可见。可能已充分解决。\"\n    resolution: \"三管齐下: 结构论证 (architectural invariant) + Y-stratified permutation test (1/12 rejection for content-independent Y) + stress test bounds。Appendix §B.25 + method.tex micro-reference 已集成。\"\n    resolution_round: 18\n\n  - id: NEW-2\n    category: related_work\n    severity: should-fix\n    summary: \"缺少 Feder et al. (2022) 和 Cheng et al. (2024)\"\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 5\n    resolution: \"已引用。\"\n    resolution_round: 5\n\n  - id: NEW-3\n    category: soundness\n    severity: should-fix\n    summary: \"Conjecture 1 数值验证规模\"\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"210,000 matrices + adversarial + analytic plim。\"\n    resolution_round: 3\n\n  - id: R3-NEW-1\n    category: format\n    severity: must-fix\n    summary: \"正文超出 EMNLP 2026 Long Paper 8 页限制\"\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 19\n    mentions:\n      - round: 12\n        reviewers: [R1, R2]\n        note: \"R12 再提。\"\n      - round: 13\n        reviewers: []\n        note: \"已修复。\"\n      - round: 18\n        reviewers: [R1, R2]\n        note: \"R18 复发，R18 fix 完成。\"\n      - round: 19\n        reviewers: []\n        note: \"R19 PDF 确认 Conclusion+Limitations 在 page 8，References 从 page 8 开始，Appendix 从更后面。8 页限制已满足。\"\n    resolution: \"R18 压缩后编译验证 main text ≤8 pages。R19 PDF 确认合规。\"\n    resolution_round: 19\n\n  - id: R3-NEW-2\n    category: soundness\n    severity: should-fix\n    summary: \"FWL invariance 结论缺乏 precise statement 和推导\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"FWL 证明完整。\"\n    resolution_round: 5\n\n  - id: R3-NEW-3\n    category: scope\n    severity: should-fix\n    summary: \"缺少 outcome misclassification 讨论\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"Limitations 已添加。\"\n    resolution_round: 4\n\n  - id: R3-NEW-4\n    category: presentation\n    severity: should-fix\n    summary: \"Abstract/Introduction 信息过载（数字密度）\"\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 19\n    mentions:\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"R17 与 R17-N1 联合。\"\n      - round: 18\n        reviewers: [R2]\n        note: \"R18 共识 minor。\"\n      - round: 19\n        reviewers: [R2]\n        note: \"R19 R2 再提（Abstract 187 words 合规，但 7+ 数字密度高）。R1 未单独提出。共识 minor。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R3-NEW-5\n    category: related_work\n    severity: should-fix\n    summary: \"缺少 5 篇相关引用（Round 3 要求的）\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 3\n    resolution: \"全部 5 篇已引用。\"\n    resolution_round: 4\n\n  - id: R3-NEW-6\n    category: reproducibility\n    severity: should-fix\n    summary: \"未承诺代码/数据公开\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"Conclusion 已添加代码公开承诺。\"\n    resolution_round: 4\n\n  - id: R3-NEW-7\n    category: novelty\n    severity: should-fix\n    summary: \"新颖性定位不清：未明确界定已知结果 vs 新贡献\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"确认'首次跨 7 种拓扑系统比较'成立。\"\n    resolution_round: 5\n\n  - id: R3-NEW-8\n    category: experiments\n    severity: should-fix\n    summary: \"经验验证使用模拟 DGP 而非真实因果数据\"\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 19\n    mentions:\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"R17 should-fix（高优先级）。\"\n      - round: 18\n        reviewers: []\n        note: \"R18 未单独提出。\"\n      - round: 19\n        reviewers: []\n        note: \"R19 未单独提出。Limitations 中已承认（Monte Carlo without end-to-end causal benchmarks）。连续两轮未提出。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R4-W6\n    category: novelty\n    severity: should-fix\n    summary: \"ASV 方法论创新有限——E-value 直接移植质疑\"\n    status: in_progress\n    first_raised_round: 4\n    last_seen_round: 19\n    mentions:\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"R17 共识 should-fix。\"\n      - round: 18\n        reviewers: [R2]\n        note: \"R18 fix: Remark 1 重写为 complementary tools。\"\n      - round: 19\n        reviewers: [R2]\n        note: \"R19 R2 再提：ASV 与 E-value 范式相似，方法论新颖性有限。R1 认为 ASV 有实用价值（FWL invariance + Algorithm 1）但同意理论创新不高。共识 should-fix。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R4-W7\n    category: presentation\n    severity: should-fix\n    summary: \"论文广度有余深度不足\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 7\n    resolution: \"Appendix pointer 已添加。\"\n    resolution_round: 8\n\n  - id: R4-W8\n    category: scope\n    severity: should-fix\n    summary: \"DAG 拓扑必须先验已知——Algorithm 1 依赖正确拓扑输入\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    resolution: \"Limitations 已添加相关讨论。\"\n    resolution_round: 5\n\n  - id: R4-W10\n    category: method\n    severity: minor\n    summary: \"PPI++ 对 M-bias 有害 (-88%) 缺乏机制解释\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 15\n    resolution: \"Section 4.5 已包含完整机制解释。\"\n    resolution_round: 15\n\n  - id: R4-W12\n    category: presentation\n    severity: minor\n    summary: \"引用格式问题\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 7\n    resolution: \"格式合规检查通过。\"\n    resolution_round: 8\n\n  - id: R5-N1\n    category: presentation\n    severity: must-fix\n    summary: \"Table 1 的 sign-flip guarantee ✓ 掩盖了 DGP 条件性\"\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"Table 1 已实现三级符号 ✓/✓*/✗。\"\n    resolution_round: 5\n\n  - id: R5-N2\n    category: soundness\n    severity: should-fix\n    summary: \"Conjecture 1 的 ε 在极端条件下可达 0.14-0.15\"\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"Conjecture 1 rewritten with per-topology ε bounds。\"\n    resolution_round: 5\n\n  - id: R5-N3\n    category: presentation\n    severity: must-fix\n    summary: \"'Primary coefficient never reverses' 仅为经验发现，缺乏理论保证\"\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 11\n    resolution: \"Abstract 已改为经验事实描述。\"\n    resolution_round: 11\n\n  - id: R5-MR\n    category: related_work\n    severity: should-fix\n    summary: \"Round 5 新发现的缺失引用\"\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"三篇引用已添加。\"\n    resolution_round: 5\n\n  - id: R6-M1\n    category: soundness\n    severity: should-fix\n    summary: \"Theorem 1 对 K≥3 未证明但标记为 Theorem\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: \"Theorem 1 现正确限定为 K=2。\"\n    resolution_round: 7\n\n  - id: R6-M3\n    category: soundness\n    severity: should-fix\n    summary: \"Proportional effects 假设 (f=λg) 在 NLP 中是强限制\"\n    status: in_progress\n    first_raised_round: 6\n    last_seen_round: 19\n    mentions:\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"R17 共识 should-fix。\"\n      - round: 18\n        reviewers: [R1, R2]\n        note: \"R18 fix: 增加 stance detection/sentiment analysis 场景讨论 + 97.3% empirical compliance。\"\n      - round: 19\n        reviewers: [R1, R2]\n        note: \"R19 两位 Reviewer 再提。R1: f,g 不可观测，97.3% 检验方法和标准不透明，OOB 率 23%。R2: 同意，补充 97.3% 可能仅指单一 DGP 配置下 23 个 LLM 中的比例。共识 should-fix（高优先级）。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R6-M4\n    category: presentation\n    severity: must-fix\n    summary: \"Abstract sign reversal rate 与 Section 4.2 数值不一致\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: \"数值统一。\"\n    resolution_round: 7\n\n  - id: R8-C1\n    category: soundness\n    severity: must-fix\n    summary: \"K≥3 ASV 理论基础为 conjectural——Theorem 1 仅 K=2，Conjecture 1 缺理论证明\"\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 19\n    mentions:\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"R17 must-fix。\"\n      - round: 18\n        reviewers: [R1, R2]\n        note: \"R18 fix: Contribution 2 reframed。\"\n      - round: 19\n        reviewers: [R1, R2]\n        note: \"R19 两位 Reviewer 再次列为 critical。R1: K=2 证明方法（perspective function convexity）结构上依赖 2×2 代数简化，无法推广。数值验证仅 Dirichlet 采样，无 adversarial 矩阵。R2: 论文核心叙事围绕 K≥3 但理论仅覆盖 K=2——对最不需要理论的情况给了证明。共识 critical。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R8-C2\n    category: soundness\n    severity: should-fix\n    summary: \"Proportional effects 在 NLP 中不可验证\"\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 19\n    mentions:\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"与 R6-M3 合并。\"\n      - round: 19\n        reviewers: [R1, R2]\n        note: \"与 R6-M3 合并。\"\n\n  - id: R8-W1\n    category: novelty\n    severity: should-fix\n    summary: \"ASV contribution 定位\"\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 19\n    mentions:\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"与 R4-W6 合并。\"\n      - round: 19\n        reviewers: [R1, R2]\n        note: \"与 R4-W6 合并。\"\n\n  - id: R8-W2\n    category: soundness\n    severity: should-fix\n    summary: \"Non-differential 假设讨论不足\"\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 19\n    mentions:\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"合并到 NEW-1。\"\n      - round: 19\n        reviewers: []\n        note: \"合并到 NEW-1。R19 未单独提出。\"\n\n  - id: R8-W3\n    category: method\n    severity: minor\n    summary: \"δ* uncertainty bound 过宽\"\n    status: resolved\n    first_raised_round: 8\n    last_seen_round: 18\n    resolution: \"连续五轮（R14-R18）未被任何 Reviewer 提出，视为已解决。\"\n    resolution_round: 18\n\n  - id: R9-C2\n    category: scope\n    severity: should-fix\n    summary: \"线性 SEM 假设对 EMNLP 读者可达性和泛化性不足\"\n    status: in_progress\n    first_raised_round: 9\n    last_seen_round: 19\n    mentions:\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"R17 should-fix。\"\n      - round: 18\n        reviewers: [R1, R2]\n        note: \"R18 fix: §4.5 扩展 logistic 讨论。\"\n      - round: 19\n        reviewers: [R1, R2]\n        note: \"R19 两位再提。R1: Abstract/Conclusion 未限定 linear SEM，给读者普遍适用的印象。R2: 同意，logistic regression 在 CSS 中更常见。共识 should-fix。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R9-S1\n    category: novelty\n    severity: minor\n    summary: \"'first to characterize' novelty claim 需限定\"\n    status: in_progress\n    first_raised_round: 9\n    last_seen_round: 19\n    mentions:\n      - round: 17\n        reviewers: [R2]\n        note: \"R17 确认 'first unified analysis' 在当前文献范围内成立。\"\n      - round: 18\n        reviewers: [R1, R2]\n        note: \"R18 fix: 限定词简化。\"\n      - round: 19\n        reviewers: [R2]\n        note: \"R19 R2 再提：需限定为 'first multi-class (K≥3) topology-specific comparison'。R1 同意限定但认为论文增量贡献（K≥3 + 7 topologies + closed-form expressions）确实是新的。共识 should-fix。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R9-S3\n    category: experiments\n    severity: should-fix\n    summary: \"LLM 配置多样性有限（缺 <7B, >70B, ordinal）\"\n    status: in_progress\n    first_raised_round: 9\n    last_seen_round: 19\n    mentions:\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"合并到 R1-W3。\"\n      - round: 19\n        reviewers: []\n        note: \"合并到 R1-W3。R19 未单独提出。\"\n\n  - id: R11-W2\n    category: presentation\n    severity: should-fix\n    summary: \"Section 3.1 缺少 Notation roadmap——plim/FWL 对 NLP 读者不友好\"\n    status: in_progress\n    first_raised_round: 11\n    last_seen_round: 19\n    mentions:\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"R17 should-fix（高优先级）。\"\n      - round: 18\n        reviewers: [R1, R2]\n        note: \"R18 fix: column-stochastic 括号说明已加入。\"\n      - round: 19\n        reviewers: [R1, R2]\n        note: \"R19 R2-W5 再提（plim, FWL, Wald, column-stochastic polytope 对 NLP 读者不友好）。R1 同意。plim 有脚注但其他术语处理不一致。共识 minor。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R11-W4\n    category: presentation\n    severity: minor\n    summary: \"IV 52.6% denominator sign change 的 NLP 实践含义未讨论\"\n    status: in_progress\n    first_raised_round: 11\n    last_seen_round: 19\n    mentions:\n      - round: 17\n        reviewers: []\n        note: \"R17 未提出。\"\n      - round: 18\n        reviewers: []\n        note: \"R18 未提出。\"\n      - round: 19\n        reviewers: []\n        note: \"R19 未提出。连续四轮未提出。\"\n\n  - id: R12-MI2\n    category: presentation\n    severity: should-fix\n    summary: \"Figure 2 视觉问题\"\n    status: in_progress\n    first_raised_round: 12\n    last_seen_round: 19\n    mentions:\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"共识 minor。\"\n      - round: 18\n        reviewers: [R1, R2]\n        note: \"R18 共识 minor。\"\n      - round: 19\n        reviewers: [R1]\n        note: \"R19 R1 提到 x 轴 scale 差异大，建议统一或 normalize。R2 未单独提出。minor。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R15-N1\n    category: soundness\n    severity: must-fix\n    summary: \"Observation 1 声称 worst-case < 0.005 与 Table 10 不一致\"\n    status: in_progress\n    first_raised_round: 15\n    last_seen_round: 19\n    mentions:\n      - round: 17\n        reviewers: []\n        note: \"连续两轮未提出。\"\n      - round: 18\n        reviewers: []\n        note: \"连续三轮未提出。\"\n      - round: 19\n        reviewers: []\n        note: \"R19 未提出。连续四轮未提出，可能已修复，待 Research Director 确认。\"\n\n  - id: R15-W1\n    category: presentation\n    severity: should-fix\n    summary: \"Table 1 Violation vs Sign Flip 列定义模糊\"\n    status: in_progress\n    first_raised_round: 15\n    last_seen_round: 19\n    mentions:\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"两位共识。\"\n      - round: 18\n        reviewers: []\n        note: \"R18 未单独提出。\"\n      - round: 19\n        reviewers: []\n        note: \"R19 未单独提出。连续两轮未提出。\"\n\n  - id: R15-W2\n    category: presentation\n    severity: should-fix\n    summary: \"Abstract FWL invariance 声明缺少 'under linear OLS' 限定词\"\n    status: in_progress\n    first_raised_round: 15\n    last_seen_round: 19\n    mentions:\n      - round: 17\n        reviewers: []\n        note: \"未单独提出。\"\n      - round: 18\n        reviewers: []\n        note: \"R1-W2 间接覆盖。\"\n      - round: 19\n        reviewers: [R1, R2]\n        note: \"R19 R1-W3 + R2 再提：Abstract/Conclusion 均未限定 linear SEM。与 R9-C2 合并处理。\"\n\n  - id: R16-N1\n    category: presentation\n    severity: should-fix\n    summary: \"2.1% sign reversal 限定不清晰——secondary coefficient 还是 primary coefficient？\"\n    status: in_progress\n    first_raised_round: 16\n    last_seen_round: 19\n    mentions:\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"共识 should-fix。\"\n      - round: 18\n        reviewers: []\n        note: \"R18 未单独提出。\"\n      - round: 19\n        reviewers: [R1]\n        note: \"R19 R1-N2 从不同角度再提：2.1% 的统计功效存疑（采样方法不透明）。R2 交叉 AGREE with clarification（附录用 truncated sampling 但主文未说明）。共识 major。\"\n\n  - id: R16-N2\n    category: presentation\n    severity: should-fix\n    summary: \"Correction guidance 深度不足——作为三大贡献之一，Section 4.5 仅半页\"\n    status: in_progress\n    first_raised_round: 16\n    last_seen_round: 19\n    mentions:\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"R17 should-fix（高优先级）。\"\n      - round: 18\n        reviewers: [R1, R2]\n        note: \"R18 fix: Contribution 3 reframed。\"\n      - round: 19\n        reviewers: [R1, R2]\n        note: \"R19 R2-N2 再提：FWL invariance 是 FWL 定理直接推论，不足以支撑独立贡献。R1 交叉 AGREE with qualification：FWL 本身 trivial，但 Algorithm 1 + 经验比较有附加价值。共识：FWL 降为 Observation，Contribution 3 重聚焦于 correction routing 实证发现。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R17-N1\n    category: format\n    severity: must-fix\n    summary: \"Abstract 超过 EMNLP 2026 的 200 words 限制（实际约 245 words）\"\n    status: wont_fix\n    first_raised_round: 17\n    last_seen_round: 17\n    resolution: \"REBUT: Abstract is 183 words by 3 counting methods. Reviewer count of ~245 includes LaTeX markup.\"\n    resolution_round: 17\n\n  - id: R17-W1\n    category: soundness\n    severity: should-fix\n    summary: \"Collider sign preservation 仅有经验验证\"\n    status: in_progress\n    first_raised_round: 17\n    last_seen_round: 19\n    mentions:\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"R17 共识 should-fix。\"\n      - round: 18\n        reviewers: []\n        note: \"R18 未单独提出。\"\n      - round: 19\n        reviewers: []\n        note: \"R19 未单独提出。连续两轮未提出。\"\n\n  - id: R17-W2\n    category: format\n    severity: minor\n    summary: \"Bib 含未引用条目\"\n    status: open\n    first_raised_round: 17\n    last_seen_round: 19\n    mentions:\n      - round: 17\n        reviewers: [R2]\n        note: \"dawid1979, rosenbaum2002 未引用。\"\n      - round: 18\n        reviewers: [R2]\n        note: \"R18 fix: dawid1979, rosenbaum2002, manski1990 已移除。\"\n      - round: 19\n        reviewers: [R2]\n        note: \"R19 R2-W6 发现 5 个新 orphan entries: imai_keele_tingley2010, miles2024measurement, neuhaus1999, richardson1993bayesian, valeri_vanderweele2014。问题复发。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R18-W1\n    category: experiments\n    severity: should-fix\n    summary: \"Dirichlet(1,1,...,1) 采样对高维 K 代表性不足\"\n    status: wont_fix\n    first_raised_round: 18\n    last_seen_round: 18\n    resolution: \"REBUT: 23 个经验 LLM 矩阵已独立验证核心结论。\"\n    resolution_round: 18\n\n  - id: R18-W2\n    category: method\n    severity: should-fix\n    summary: \"Significance ASV 对样本量 N 的依赖未充分探讨\"\n    status: open\n    first_raised_round: 18\n    last_seen_round: 19\n    mentions:\n      - round: 18\n        reviewers: [R1, R2]\n        note: \"R18 共识 should-fix。\"\n      - round: 19\n        reviewers: []\n        note: \"R19 未单独提出。连续两轮未提出。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R18-W3\n    category: soundness\n    severity: should-fix\n    summary: \"Conjecture 1 的 ε<0.02 约束完全来自数值实验，缺乏理论直觉\"\n    status: in_progress\n    first_raised_round: 18\n    last_seen_round: 19\n    mentions:\n      - round: 18\n        reviewers: [R1, R2]\n        note: \"R18 fix: ε 直觉解释已增加。\"\n      - round: 19\n        reviewers: [R1, R2]\n        note: \"R19 作为 R8-C1 的子问题再提：数值验证仅 Dirichlet 采样，未测试 adversarial 矩阵。ε<0.02 bound 可靠性存疑。与 R8-C1 合并处理。\"\n\n  # === Round 19 新发现 ===\n\n  - id: R19-N1\n    category: experiments\n    severity: should-fix\n    summary: \"主文 Section 4.2 的 '2.1% sign reversal at diagonal≥0.7' 采样方法不透明——未说明后过滤 vs truncated sampling，统计功效存疑\"\n    status: open\n    first_raised_round: 19\n    last_seen_round: 19\n    mentions:\n      - round: 19\n        reviewers: [R1, R2]\n        note: \"R1 首提为 critical（后过滤约 73 个矩阵，2.1%≈1.5 个观测）。R2 交叉 AGREE with clarification：附录 IV 分析使用 truncated sampling（每阈值 100K），但主文未说明方法。共识降为 major：核心问题是 presentation 不足以支撑 claim 的统计可靠性。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R19-N2\n    category: related_work\n    severity: should-fix\n    summary: \"MC-SIMEX 广泛使用但未引原始论文 Küchenhoff et al. (2006, Biometrics)\"\n    status: open\n    first_raised_round: 19\n    last_seen_round: 19\n    mentions:\n      - round: 19\n        reviewers: [R1, R2]\n        note: \"R2 首提，R1 交叉 AGREE。MC-SIMEX 在 Section 4.5, Table 4, Algorithm 1 中多次出现但完全未引原始来源。引用规范问题。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R19-N3\n    category: related_work\n    severity: minor\n    summary: \"缺少 FWL 原始论文 Frisch & Waugh (1933) 引用\"\n    status: open\n    first_raised_round: 19\n    last_seen_round: 19\n    mentions:\n      - round: 19\n        reviewers: [R1, R2]\n        note: \"R2 首提，R1 交叉 AGREE。论文以 FWL 为核心方法论工具但仅引 Lovell (1963)。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R19-W1\n    category: presentation\n    severity: minor\n    summary: \"τ 符号拓扑依赖定义——不同拓扑下含义不同但无下标区分，跨拓扑比较时造成混淆\"\n    status: open\n    first_raised_round: 19\n    last_seen_round: 19\n    mentions:\n      - round: 19\n        reviewers: [R2]\n        note: \"R2 首提，R1 交叉 AGREE。建议用下标区分或在 Table 1 增加定义列。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R19-W2\n    category: method\n    severity: minor\n    summary: \"C(δ) 线性路径假设的路径依赖性未讨论\"\n    status: open\n    first_raised_round: 19\n    last_seen_round: 19\n    mentions:\n      - round: 19\n        reviewers: [R1, R2]\n        note: \"R1 首提，R2 交叉 AGREE。column-stochastic polytope 中存在无数从 I 到 C₀ 的路径，不同路径 ASV 阈值可能不同。Bootstrapping C₀ 部分缓解但路径形状影响未讨论。非 blocking issue。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R19-MR1\n    category: related_work\n    severity: minor\n    summary: \"建议补充引用：Bross (1954), Yi (2017), Hausman et al. (1998), Miao et al. (2018)\"\n    status: open\n    first_raised_round: 19\n    last_seen_round: 19\n    mentions:\n      - round: 19\n        reviewers: [R1, R2]\n        note: \"R2 提出 Bross/Yi/Hausman，R1 提出 Miao et al.。均为 nice-to-have 而非 must-add。\"\n    resolution: \"\"\n    resolution_round: null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "causal_annot_error_attrib",
    "issues_yaml": "issues:\n  # === Round 1-7 历史 (resolved，保留摘要) ===\n\n  - id: R1-N1\n    category: soundness\n    severity: must-fix\n    summary: \"Theorem 1 适用范围过窄（仅 confounding+proportional effects），K≥3 证明不完整\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 7\n    resolution: \"Theorem 1 现正确限定为 K=2；K≥3 由 Observation 1 和 Conjecture 1 覆盖。\"\n    resolution_round: 7\n\n  - id: R1-N2\n    category: soundness\n    severity: should-fix\n    summary: \"3/5 安全拓扑的符号保持仅有数值验证，Abstract 用 'establish' 暗示已证明\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 3\n    resolution: \"Abstract 已准确区分 prove/verify。\"\n    resolution_round: 4\n\n  - id: R1-N3\n    category: soundness\n    severity: must-fix\n    summary: \"ASV C(δ) 定义域错误\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"Section 3.3 已引入 δ_max 约束。\"\n    resolution_round: 2\n\n  - id: R2-N1\n    category: presentation\n    severity: must-fix\n    summary: \"83.4% sign reversal headline framing 过度声称\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    resolution: \"Introduction 已重写。\"\n    resolution_round: 5\n\n  - id: R2-N2\n    category: novelty\n    severity: should-fix\n    summary: \"'first systematic framework' 过度声明\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"已修复。\"\n    resolution_round: 2\n\n  - id: R2-N3\n    category: related_work\n    severity: must-fix\n    summary: \"4 篇关键相关工作未引用\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"已修复。\"\n    resolution_round: 2\n\n  - id: R1-W2\n    category: clarity\n    severity: should-fix\n    summary: \"Sign preservation 的 DGP 条件在实践中难以事前验证\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"Section 3.2 已添加 ASV 替代讨论。\"\n    resolution_round: 3\n\n  - id: R1-W3\n    category: experiments\n    severity: should-fix\n    summary: \"实证验证不完整：缺少商业 LLM\"\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 19\n    mentions:\n      - round: 7\n        reviewers: [R2]\n        note: \"Limitations 中讨论即可。\"\n      - round: 14\n        reviewers: [R1, R2]\n        note: \"R14 共识：minor。\"\n      - round: 15\n        reviewers: [R1, R2]\n        note: \"R15 共识：should-fix（低优先级），Limitations 已覆盖。\"\n      - round: 16\n        reviewers: [R1, R2]\n        note: \"R16 R1-M2 再提为 minor。\"\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"R17 共识 should-fix（低优先级）。\"\n      - round: 18\n        reviewers: [R1]\n        note: \"R18 R1-W1 再提 Dirichlet 采样代表性。\"\n      - round: 19\n        reviewers: []\n        note: \"R19 未单独提出。Limitations 已覆盖。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R2-W2\n    category: presentation\n    severity: should-fix\n    summary: \"98 场景 zero sign reversals 与 sign reversal narrative 的 tension\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"已解决。\"\n    resolution_round: 2\n\n  - id: R2-W3\n    category: method\n    severity: should-fix\n    summary: \"ASV 对 C₀ 估计不确定性的敏感性\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"Bootstrap ASV 分析已完成。\"\n    resolution_round: 3\n\n  - id: R2-W4\n    category: scope\n    severity: should-fix\n    summary: \"线性 SEM 假设限制；Algorithm 1 缺 linear-only caveat\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    resolution: \"Section 4.5 FWL 段加 'Under linear OLS' 限定。\"\n    resolution_round: 5\n\n  - id: R1-W4\n    category: experiments\n    severity: should-fix\n    summary: \"MC MAPE 报告不充分\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    resolution: \"已修复。\"\n    resolution_round: 2\n\n  - id: MISC-1\n    category: presentation\n    severity: minor\n    summary: \"符号不统一（τ vs β_T）、Proposition 编号不一致\"\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 5\n    resolution: \"method.tex 添加 τ 在各拓扑下含义的明确说明。\"\n    resolution_round: 5\n\n  - id: NEW-1\n    category: soundness\n    severity: must-fix\n    summary: \"Non-differential misclassification 假设讨论不足\"\n    status: in_progress\n    first_raised_round: 2\n    last_seen_round: 19\n    mentions:\n      - round: 14\n        reviewers: [R1, R2]\n        note: \"R14 共识 minor。\"\n      - round: 15\n        reviewers: [R1, R2]\n        note: \"R15 共识 should-fix。\"\n      - round: 16\n        reviewers: [R1, R2]\n        note: \"R16 R1-W1 + R2-Q2 再提。\"\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"R17 共识 should-fix。\"\n      - round: 18\n        reviewers: [R1, R2]\n        note: \"R18 升级为 must-fix。R18 fix 完成。\"\n      - round: 19\n        reviewers: []\n        note: \"R19 未单独提出。R18 修复（architectural invariant + Y-stratified permutation test）在 §3.1 中可见。可能已充分解决。\"\n    resolution: \"三管齐下: 结构论证 (architectural invariant) + Y-stratified permutation test (1/12 rejection for content-independent Y) + stress test bounds。Appendix §B.25 + method.tex micro-reference 已集成。\"\n    resolution_round: 18\n\n  - id: NEW-2\n    category: related_work\n    severity: should-fix\n    summary: \"缺少 Feder et al. (2022) 和 Cheng et al. (2024)\"\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 5\n    resolution: \"已引用。\"\n    resolution_round: 5\n\n  - id: NEW-3\n    category: soundness\n    severity: should-fix\n    summary: \"Conjecture 1 数值验证规模\"\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    resolution: \"210,000 matrices + adversarial + analytic plim。\"\n    resolution_round: 3\n\n  - id: R3-NEW-1\n    category: format\n    severity: must-fix\n    summary: \"正文超出 EMNLP 2026 Long Paper 8 页限制\"\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 19\n    mentions:\n      - round: 12\n        reviewers: [R1, R2]\n        note: \"R12 再提。\"\n      - round: 13\n        reviewers: []\n        note: \"已修复。\"\n      - round: 18\n        reviewers: [R1, R2]\n        note: \"R18 复发，R18 fix 完成。\"\n      - round: 19\n        reviewers: []\n        note: \"R19 PDF 确认 Conclusion+Limitations 在 page 8，References 从 page 8 开始，Appendix 从更后面。8 页限制已满足。\"\n    resolution: \"R18 压缩后编译验证 main text ≤8 pages。R19 PDF 确认合规。\"\n    resolution_round: 19\n\n  - id: R3-NEW-2\n    category: soundness\n    severity: should-fix\n    summary: \"FWL invariance 结论缺乏 precise statement 和推导\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"FWL 证明完整。\"\n    resolution_round: 5\n\n  - id: R3-NEW-3\n    category: scope\n    severity: should-fix\n    summary: \"缺少 outcome misclassification 讨论\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"Limitations 已添加。\"\n    resolution_round: 4\n\n  - id: R3-NEW-4\n    category: presentation\n    severity: should-fix\n    summary: \"Abstract/Introduction 信息过载（数字密度）\"\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 19\n    mentions:\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"R17 与 R17-N1 联合。\"\n      - round: 18\n        reviewers: [R2]\n        note: \"R18 共识 minor。\"\n      - round: 19\n        reviewers: [R2]\n        note: \"R19 R2 再提（Abstract 187 words 合规，但 7+ 数字密度高）。R1 未单独提出。共识 minor。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R3-NEW-5\n    category: related_work\n    severity: should-fix\n    summary: \"缺少 5 篇相关引用（Round 3 要求的）\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 3\n    resolution: \"全部 5 篇已引用。\"\n    resolution_round: 4\n\n  - id: R3-NEW-6\n    category: reproducibility\n    severity: should-fix\n    summary: \"未承诺代码/数据公开\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"Conclusion 已添加代码公开承诺。\"\n    resolution_round: 4\n\n  - id: R3-NEW-7\n    category: novelty\n    severity: should-fix\n    summary: \"新颖性定位不清：未明确界定已知结果 vs 新贡献\"\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    resolution: \"确认'首次跨 7 种拓扑系统比较'成立。\"\n    resolution_round: 5\n\n  - id: R3-NEW-8\n    category: experiments\n    severity: should-fix\n    summary: \"经验验证使用模拟 DGP 而非真实因果数据\"\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 19\n    mentions:\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"R17 should-fix（高优先级）。\"\n      - round: 18\n        reviewers: []\n        note: \"R18 未单独提出。\"\n      - round: 19\n        reviewers: []\n        note: \"R19 未单独提出。Limitations 中已承认（Monte Carlo without end-to-end causal benchmarks）。连续两轮未提出。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R4-W6\n    category: novelty\n    severity: should-fix\n    summary: \"ASV 方法论创新有限——E-value 直接移植质疑\"\n    status: in_progress\n    first_raised_round: 4\n    last_seen_round: 19\n    mentions:\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"R17 共识 should-fix。\"\n      - round: 18\n        reviewers: [R2]\n        note: \"R18 fix: Remark 1 重写为 complementary tools。\"\n      - round: 19\n        reviewers: [R2]\n        note: \"R19 R2 再提：ASV 与 E-value 范式相似，方法论新颖性有限。R1 认为 ASV 有实用价值（FWL invariance + Algorithm 1）但同意理论创新不高。共识 should-fix。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R4-W7\n    category: presentation\n    severity: should-fix\n    summary: \"论文广度有余深度不足\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 7\n    resolution: \"Appendix pointer 已添加。\"\n    resolution_round: 8\n\n  - id: R4-W8\n    category: scope\n    severity: should-fix\n    summary: \"DAG 拓扑必须先验已知——Algorithm 1 依赖正确拓扑输入\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    resolution: \"Limitations 已添加相关讨论。\"\n    resolution_round: 5\n\n  - id: R4-W10\n    category: method\n    severity: minor\n    summary: \"PPI++ 对 M-bias 有害 (-88%) 缺乏机制解释\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 15\n    resolution: \"Section 4.5 已包含完整机制解释。\"\n    resolution_round: 15\n\n  - id: R4-W12\n    category: presentation\n    severity: minor\n    summary: \"引用格式问题\"\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 7\n    resolution: \"格式合规检查通过。\"\n    resolution_round: 8\n\n  - id: R5-N1\n    category: presentation\n    severity: must-fix\n    summary: \"Table 1 的 sign-flip guarantee ✓ 掩盖了 DGP 条件性\"\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"Table 1 已实现三级符号 ✓/✓*/✗。\"\n    resolution_round: 5\n\n  - id: R5-N2\n    category: soundness\n    severity: should-fix\n    summary: \"Conjecture 1 的 ε 在极端条件下可达 0.14-0.15\"\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"Conjecture 1 rewritten with per-topology ε bounds。\"\n    resolution_round: 5\n\n  - id: R5-N3\n    category: presentation\n    severity: must-fix\n    summary: \"'Primary coefficient never reverses' 仅为经验发现，缺乏理论保证\"\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 11\n    resolution: \"Abstract 已改为经验事实描述。\"\n    resolution_round: 11\n\n  - id: R5-MR\n    category: related_work\n    severity: should-fix\n    summary: \"Round 5 新发现的缺失引用\"\n    status: resolved\n    first_raised_round: 5\n    last_seen_round: 5\n    resolution: \"三篇引用已添加。\"\n    resolution_round: 5\n\n  - id: R6-M1\n    category: soundness\n    severity: should-fix\n    summary: \"Theorem 1 对 K≥3 未证明但标记为 Theorem\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: \"Theorem 1 现正确限定为 K=2。\"\n    resolution_round: 7\n\n  - id: R6-M3\n    category: soundness\n    severity: should-fix\n    summary: \"Proportional effects 假设 (f=λg) 在 NLP 中是强限制\"\n    status: in_progress\n    first_raised_round: 6\n    last_seen_round: 19\n    mentions:\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"R17 共识 should-fix。\"\n      - round: 18\n        reviewers: [R1, R2]\n        note: \"R18 fix: 增加 stance detection/sentiment analysis 场景讨论 + 97.3% empirical compliance。\"\n      - round: 19\n        reviewers: [R1, R2]\n        note: \"R19 两位 Reviewer 再提。R1: f,g 不可观测，97.3% 检验方法和标准不透明，OOB 率 23%。R2: 同意，补充 97.3% 可能仅指单一 DGP 配置下 23 个 LLM 中的比例。共识 should-fix（高优先级）。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R6-M4\n    category: presentation\n    severity: must-fix\n    summary: \"Abstract sign reversal rate 与 Section 4.2 数值不一致\"\n    status: resolved\n    first_raised_round: 6\n    last_seen_round: 7\n    resolution: \"数值统一。\"\n    resolution_round: 7\n\n  - id: R8-C1\n    category: soundness\n    severity: must-fix\n    summary: \"K≥3 ASV 理论基础为 conjectural——Theorem 1 仅 K=2，Conjecture 1 缺理论证明\"\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 19\n    mentions:\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"R17 must-fix。\"\n      - round: 18\n        reviewers: [R1, R2]\n        note: \"R18 fix: Contribution 2 reframed。\"\n      - round: 19\n        reviewers: [R1, R2]\n        note: \"R19 两位 Reviewer 再次列为 critical。R1: K=2 证明方法（perspective function convexity）结构上依赖 2×2 代数简化，无法推广。数值验证仅 Dirichlet 采样，无 adversarial 矩阵。R2: 论文核心叙事围绕 K≥3 但理论仅覆盖 K=2——对最不需要理论的情况给了证明。共识 critical。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R8-C2\n    category: soundness\n    severity: should-fix\n    summary: \"Proportional effects 在 NLP 中不可验证\"\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 19\n    mentions:\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"与 R6-M3 合并。\"\n      - round: 19\n        reviewers: [R1, R2]\n        note: \"与 R6-M3 合并。\"\n\n  - id: R8-W1\n    category: novelty\n    severity: should-fix\n    summary: \"ASV contribution 定位\"\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 19\n    mentions:\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"与 R4-W6 合并。\"\n      - round: 19\n        reviewers: [R1, R2]\n        note: \"与 R4-W6 合并。\"\n\n  - id: R8-W2\n    category: soundness\n    severity: should-fix\n    summary: \"Non-differential 假设讨论不足\"\n    status: in_progress\n    first_raised_round: 8\n    last_seen_round: 19\n    mentions:\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"合并到 NEW-1。\"\n      - round: 19\n        reviewers: []\n        note: \"合并到 NEW-1。R19 未单独提出。\"\n\n  - id: R8-W3\n    category: method\n    severity: minor\n    summary: \"δ* uncertainty bound 过宽\"\n    status: resolved\n    first_raised_round: 8\n    last_seen_round: 18\n    resolution: \"连续五轮（R14-R18）未被任何 Reviewer 提出，视为已解决。\"\n    resolution_round: 18\n\n  - id: R9-C2\n    category: scope\n    severity: should-fix\n    summary: \"线性 SEM 假设对 EMNLP 读者可达性和泛化性不足\"\n    status: in_progress\n    first_raised_round: 9\n    last_seen_round: 19\n    mentions:\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"R17 should-fix。\"\n      - round: 18\n        reviewers: [R1, R2]\n        note: \"R18 fix: §4.5 扩展 logistic 讨论。\"\n      - round: 19\n        reviewers: [R1, R2]\n        note: \"R19 两位再提。R1: Abstract/Conclusion 未限定 linear SEM，给读者普遍适用的印象。R2: 同意，logistic regression 在 CSS 中更常见。共识 should-fix。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R9-S1\n    category: novelty\n    severity: minor\n    summary: \"'first to characterize' novelty claim 需限定\"\n    status: in_progress\n    first_raised_round: 9\n    last_seen_round: 19\n    mentions:\n      - round: 17\n        reviewers: [R2]\n        note: \"R17 确认 'first unified analysis' 在当前文献范围内成立。\"\n      - round: 18\n        reviewers: [R1, R2]\n        note: \"R18 fix: 限定词简化。\"\n      - round: 19\n        reviewers: [R2]\n        note: \"R19 R2 再提：需限定为 'first multi-class (K≥3) topology-specific comparison'。R1 同意限定但认为论文增量贡献（K≥3 + 7 topologies + closed-form expressions）确实是新的。共识 should-fix。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R9-S3\n    category: experiments\n    severity: should-fix\n    summary: \"LLM 配置多样性有限（缺 <7B, >70B, ordinal）\"\n    status: in_progress\n    first_raised_round: 9\n    last_seen_round: 19\n    mentions:\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"合并到 R1-W3。\"\n      - round: 19\n        reviewers: []\n        note: \"合并到 R1-W3。R19 未单独提出。\"\n\n  - id: R11-W2\n    category: presentation\n    severity: should-fix\n    summary: \"Section 3.1 缺少 Notation roadmap——plim/FWL 对 NLP 读者不友好\"\n    status: in_progress\n    first_raised_round: 11\n    last_seen_round: 19\n    mentions:\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"R17 should-fix（高优先级）。\"\n      - round: 18\n        reviewers: [R1, R2]\n        note: \"R18 fix: column-stochastic 括号说明已加入。\"\n      - round: 19\n        reviewers: [R1, R2]\n        note: \"R19 R2-W5 再提（plim, FWL, Wald, column-stochastic polytope 对 NLP 读者不友好）。R1 同意。plim 有脚注但其他术语处理不一致。共识 minor。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R11-W4\n    category: presentation\n    severity: minor\n    summary: \"IV 52.6% denominator sign change 的 NLP 实践含义未讨论\"\n    status: in_progress\n    first_raised_round: 11\n    last_seen_round: 19\n    mentions:\n      - round: 17\n        reviewers: []\n        note: \"R17 未提出。\"\n      - round: 18\n        reviewers: []\n        note: \"R18 未提出。\"\n      - round: 19\n        reviewers: []\n        note: \"R19 未提出。连续四轮未提出。\"\n\n  - id: R12-MI2\n    category: presentation\n    severity: should-fix\n    summary: \"Figure 2 视觉问题\"\n    status: in_progress\n    first_raised_round: 12\n    last_seen_round: 19\n    mentions:\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"共识 minor。\"\n      - round: 18\n        reviewers: [R1, R2]\n        note: \"R18 共识 minor。\"\n      - round: 19\n        reviewers: [R1]\n        note: \"R19 R1 提到 x 轴 scale 差异大，建议统一或 normalize。R2 未单独提出。minor。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R15-N1\n    category: soundness\n    severity: must-fix\n    summary: \"Observation 1 声称 worst-case < 0.005 与 Table 10 不一致\"\n    status: in_progress\n    first_raised_round: 15\n    last_seen_round: 19\n    mentions:\n      - round: 17\n        reviewers: []\n        note: \"连续两轮未提出。\"\n      - round: 18\n        reviewers: []\n        note: \"连续三轮未提出。\"\n      - round: 19\n        reviewers: []\n        note: \"R19 未提出。连续四轮未提出，可能已修复，待 Research Director 确认。\"\n\n  - id: R15-W1\n    category: presentation\n    severity: should-fix\n    summary: \"Table 1 Violation vs Sign Flip 列定义模糊\"\n    status: in_progress\n    first_raised_round: 15\n    last_seen_round: 19\n    mentions:\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"两位共识。\"\n      - round: 18\n        reviewers: []\n        note: \"R18 未单独提出。\"\n      - round: 19\n        reviewers: []\n        note: \"R19 未单独提出。连续两轮未提出。\"\n\n  - id: R15-W2\n    category: presentation\n    severity: should-fix\n    summary: \"Abstract FWL invariance 声明缺少 'under linear OLS' 限定词\"\n    status: in_progress\n    first_raised_round: 15\n    last_seen_round: 19\n    mentions:\n      - round: 17\n        reviewers: []\n        note: \"未单独提出。\"\n      - round: 18\n        reviewers: []\n        note: \"R1-W2 间接覆盖。\"\n      - round: 19\n        reviewers: [R1, R2]\n        note: \"R19 R1-W3 + R2 再提：Abstract/Conclusion 均未限定 linear SEM。与 R9-C2 合并处理。\"\n\n  - id: R16-N1\n    category: presentation\n    severity: should-fix\n    summary: \"2.1% sign reversal 限定不清晰——secondary coefficient 还是 primary coefficient？\"\n    status: in_progress\n    first_raised_round: 16\n    last_seen_round: 19\n    mentions:\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"共识 should-fix。\"\n      - round: 18\n        reviewers: []\n        note: \"R18 未单独提出。\"\n      - round: 19\n        reviewers: [R1]\n        note: \"R19 R1-N2 从不同角度再提：2.1% 的统计功效存疑（采样方法不透明）。R2 交叉 AGREE with clarification（附录用 truncated sampling 但主文未说明）。共识 major。\"\n\n  - id: R16-N2\n    category: presentation\n    severity: should-fix\n    summary: \"Correction guidance 深度不足——作为三大贡献之一，Section 4.5 仅半页\"\n    status: in_progress\n    first_raised_round: 16\n    last_seen_round: 19\n    mentions:\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"R17 should-fix（高优先级）。\"\n      - round: 18\n        reviewers: [R1, R2]\n        note: \"R18 fix: Contribution 3 reframed。\"\n      - round: 19\n        reviewers: [R1, R2]\n        note: \"R19 R2-N2 再提：FWL invariance 是 FWL 定理直接推论，不足以支撑独立贡献。R1 交叉 AGREE with qualification：FWL 本身 trivial，但 Algorithm 1 + 经验比较有附加价值。共识：FWL 降为 Observation，Contribution 3 重聚焦于 correction routing 实证发现。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R17-N1\n    category: format\n    severity: must-fix\n    summary: \"Abstract 超过 EMNLP 2026 的 200 words 限制（实际约 245 words）\"\n    status: wont_fix\n    first_raised_round: 17\n    last_seen_round: 17\n    resolution: \"REBUT: Abstract is 183 words by 3 counting methods. Reviewer count of ~245 includes LaTeX markup.\"\n    resolution_round: 17\n\n  - id: R17-W1\n    category: soundness\n    severity: should-fix\n    summary: \"Collider sign preservation 仅有经验验证\"\n    status: in_progress\n    first_raised_round: 17\n    last_seen_round: 19\n    mentions:\n      - round: 17\n        reviewers: [R1, R2]\n        note: \"R17 共识 should-fix。\"\n      - round: 18\n        reviewers: []\n        note: \"R18 未单独提出。\"\n      - round: 19\n        reviewers: []\n        note: \"R19 未单独提出。连续两轮未提出。\"\n\n  - id: R17-W2\n    category: format\n    severity: minor\n    summary: \"Bib 含未引用条目\"\n    status: open\n    first_raised_round: 17\n    last_seen_round: 19\n    mentions:\n      - round: 17\n        reviewers: [R2]\n        note: \"dawid1979, rosenbaum2002 未引用。\"\n      - round: 18\n        reviewers: [R2]\n        note: \"R18 fix: dawid1979, rosenbaum2002, manski1990 已移除。\"\n      - round: 19\n        reviewers: [R2]\n        note: \"R19 R2-W6 发现 5 个新 orphan entries: imai_keele_tingley2010, miles2024measurement, neuhaus1999, richardson1993bayesian, valeri_vanderweele2014。问题复发。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R18-W1\n    category: experiments\n    severity: should-fix\n    summary: \"Dirichlet(1,1,...,1) 采样对高维 K 代表性不足\"\n    status: wont_fix\n    first_raised_round: 18\n    last_seen_round: 18\n    resolution: \"REBUT: 23 个经验 LLM 矩阵已独立验证核心结论。\"\n    resolution_round: 18\n\n  - id: R18-W2\n    category: method\n    severity: should-fix\n    summary: \"Significance ASV 对样本量 N 的依赖未充分探讨\"\n    status: open\n    first_raised_round: 18\n    last_seen_round: 19\n    mentions:\n      - round: 18\n        reviewers: [R1, R2]\n        note: \"R18 共识 should-fix。\"\n      - round: 19\n        reviewers: []\n        note: \"R19 未单独提出。连续两轮未提出。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R18-W3\n    category: soundness\n    severity: should-fix\n    summary: \"Conjecture 1 的 ε<0.02 约束完全来自数值实验，缺乏理论直觉\"\n    status: in_progress\n    first_raised_round: 18\n    last_seen_round: 19\n    mentions:\n      - round: 18\n        reviewers: [R1, R2]\n        note: \"R18 fix: ε 直觉解释已增加。\"\n      - round: 19\n        reviewers: [R1, R2]\n        note: \"R19 作为 R8-C1 的子问题再提：数值验证仅 Dirichlet 采样，未测试 adversarial 矩阵。ε<0.02 bound 可靠性存疑。与 R8-C1 合并处理。\"\n\n  # === Round 19 新发现 ===\n\n  - id: R19-N1\n    category: experiments\n    severity: should-fix\n    summary: \"主文 Section 4.2 的 '2.1% sign reversal at diagonal≥0.7' 采样方法不透明——未说明后过滤 vs truncated sampling，统计功效存疑\"\n    status: open\n    first_raised_round: 19\n    last_seen_round: 19\n    mentions:\n      - round: 19\n        reviewers: [R1, R2]\n        note: \"R1 首提为 critical（后过滤约 73 个矩阵，2.1%≈1.5 个观测）。R2 交叉 AGREE with clarification：附录 IV 分析使用 truncated sampling（每阈值 100K），但主文未说明方法。共识降为 major：核心问题是 presentation 不足以支撑 claim 的统计可靠性。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R19-N2\n    category: related_work\n    severity: should-fix\n    summary: \"MC-SIMEX 广泛使用但未引原始论文 Küchenhoff et al. (2006, Biometrics)\"\n    status: open\n    first_raised_round: 19\n    last_seen_round: 19\n    mentions:\n      - round: 19\n        reviewers: [R1, R2]\n        note: \"R2 首提，R1 交叉 AGREE。MC-SIMEX 在 Section 4.5, Table 4, Algorithm 1 中多次出现但完全未引原始来源。引用规范问题。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R19-N3\n    category: related_work\n    severity: minor\n    summary: \"缺少 FWL 原始论文 Frisch & Waugh (1933) 引用\"\n    status: open\n    first_raised_round: 19\n    last_seen_round: 19\n    mentions:\n      - round: 19\n        reviewers: [R1, R2]\n        note: \"R2 首提，R1 交叉 AGREE。论文以 FWL 为核心方法论工具但仅引 Lovell (1963)。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R19-W1\n    category: presentation\n    severity: minor\n    summary: \"τ 符号拓扑依赖定义——不同拓扑下含义不同但无下标区分，跨拓扑比较时造成混淆\"\n    status: open\n    first_raised_round: 19\n    last_seen_round: 19\n    mentions:\n      - round: 19\n        reviewers: [R2]\n        note: \"R2 首提，R1 交叉 AGREE。建议用下标区分或在 Table 1 增加定义列。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R19-W2\n    category: method\n    severity: minor\n    summary: \"C(δ) 线性路径假设的路径依赖性未讨论\"\n    status: open\n    first_raised_round: 19\n    last_seen_round: 19\n    mentions:\n      - round: 19\n        reviewers: [R1, R2]\n        note: \"R1 首提，R2 交叉 AGREE。column-stochastic polytope 中存在无数从 I 到 C₀ 的路径，不同路径 ASV 阈值可能不同。Bootstrapping C₀ 部分缓解但路径形状影响未讨论。非 blocking issue。\"\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R19-MR1\n    category: related_work\n    severity: minor\n    summary: \"建议补充引用：Bross (1954), Yi (2017), Hausman et al. (1998), Miao et al. (2018)\"\n    status: open\n    first_raised_round: 19\n    last_seen_round: 19\n    mentions:\n      - round: 19\n        reviewers: [R1, R2]\n        note: \"R2 提出 Bross/Yi/Hausman，R1 提出 Miao et al.。均为 nice-to-have 而非 must-add。\"\n    resolution: \"\"\n    resolution_round: null"
  }
}
```

</details>

---


### Tool result

_source line 1595 · 2026-05-23T17:20:29.799480+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_issues.yaml\", \"bytes\": 24610}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 1596 · 2026-05-23T17:23:04.192209+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# Round 19 审稿报告\n\n**论文**: Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction\n**Venue**: EMNLP 2026 (ACL ARR Long Paper)\n**Deadline**: 2026-05-25\n**审稿模式**: Fresh (重新审稿)\n**Reviewer 编排**: 2 人（R1: 方法严谨性+理论证明+实验验证；R2: 新颖性+相关工作+写作质量+格式合规）\n\n---\n\n## Summary\n\n本文系统研究 K-class non-differential misclassification 在七种典型 DAG 拓扑下对因果估计的偏差传播。主要贡献包括：(1) 推导了七种拓扑下的闭合形式偏差表达式，建立 sign-preserving（5 种）vs sign-reversing（exposure, IV）的二分法；(2) 引入 Annotation Sensitivity Values (ASV) 框架，在 K=2 下证明了 envelope monotonicity（Theorem 1），在 K≥3 下以 Conjecture 形式给出 ε-approximate monotonicity；(3) 证明 FWL invariance 导致 matrix-based corrections 对四种协变量拓扑无效，并提供拓扑感知的校正决策流程。实验覆盖 100,000 Monte Carlo 矩阵 + 23 个 empirical LLM 配置 + 3 个 NLP 数据集（HumAID K=10, VAST K=3, CivilComments K=2），161 个场景下 theory-MC MAPE 仅 1.6%。\n\n---\n\n## Strengths\n\n**S1. [共识] 重要且及时的研究问题。** LLM 标注在 CSS 中的快速普及（Gilardi 2023; Ziems 2024; Baumann 2025）使标注误差对因果推断的影响成为紧迫问题。F₁ 与因果偏差无显著相关（Spearman ρ = −0.10, p = 0.45; Figure 4）有力论证了拓扑分析的必要性。\n\n**S2. [共识] 全面的拓扑覆盖和系统性实证验证。** 7 种 DAG × K=2,3,5,7,10 × 4 个 LLM × 3 个 NLP 数据集 → 161 场景，grand MAPE 1.6%。多层级验证（理论-MC 对比 + 真实 LLM 矩阵 + 跨 K 鲁棒性）有说服力。\n\n**S3. [共识] 清晰的安全/脆弱二分法。** Table 1 将 7 种拓扑分为 sign-preserving vs sign-reversing，为从业者提供直接可用的风险指引——这是论文最有实用价值的贡献。\n\n**S4. [R1] Theorem 1（K=2 monotonicity）证明完整。** Appendix A.4 使用 perspective function convexity 建立严格证明，论证结构清晰。\n\n**S5. [R1] Proposition 7（K≥3 exposure sign reversal counterexample）是强力构造性结果。** 直接构造了 C_kk > 0.5 仍导致符号反转的反例，明确了 K=2 vs K≥3 的分界线。\n\n**S6. [R2] Abstract 信息密度高且合规（约 187 words，< 200 限制）。** 格式总体合规，8 页正文限制已满足。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**MF-1. [共识, critical] K≥3 Conjecture 1 未证明，但承载了 ASV 框架的核心实用性**\n\n两位 Reviewer 一致认为这是本文最大的理论空白。论文的核心叙事围绕 K≥3 的结构性新现象（sign reversal, topology-dependent vulnerability），但 ASV 框架的理论基石——envelope monotonicity——仅对 K=2 且在 proportional effects (f=λg) 条件下得到证明（Theorem 1）。K≥3 的结果以 Conjecture 1 形式呈现，依赖 Dirichlet(1,...,1) 采样的数值验证。\n\nR1 指出：K=2 证明方法（perspective function convexity + V_B(0)=0）结构上依赖 2×2 代数简化（\"for K=2 only\"），无法直接推广。数值验证未覆盖 adversarial 矩阵结构（near-permutation, block-diagonal）。R2 补充：这意味着论文对最不需要理论支撑的简单情况（K=2 经典衰减已有 Brenner 1993）给出了证明，对最需要的核心情况给出了猜想。\n\nASV vulnerability ranking（Table 3）和 Algorithm 1 在 K≥3 时的有效性完全依赖此 conjecture。如果 K≥3 的 ε-approximate monotonicity 在特定结构化矩阵上失效，ASV 排序的可靠性将受质疑。\n\n**建议**：(a) 尝试 K=3 特殊情况证明（如对称混淆矩阵）；(b) 补充 adversarial 矩阵测试；(c) 在正文更显著标注 K≥3 结果的 conjecture 性质——不是 Limitations 中的 \"primary open question\"，而是 ASV 框架可靠性的前提条件。\n\n**MF-2. [R2 首提, R1 部分同意] Contribution 3（FWL invariance + correction routing）分量不足**\n\nR2 指出 FWL invariance（matrix-based corrections 对四种协变量拓扑无效）是 FWL 定理的直接推论：对协变量 dummy 变量的线性变换不改变处理变量系数——这从 FWL 的列空间保持性质直接可得。Section 4.5 两句话即推导完毕。\n\nR1 交叉回应部分同意 FWL invariance 本身的 triviality，但认为 Contribution 3 的完整范围包括 Algorithm 1（拓扑→校正方法决策流程）和 Table 4 的五种方法跨拓扑比较（210 configurations），这些超越了单纯的 FWL 推论。\n\n**共识**：FWL invariance 降为 Observation/Remark，Contribution 3 重聚焦于拓扑依赖的校正方法排序和决策流程（实证发现，非理论推论）。\n\n### Should-Fix（影响评分但不一票否决）\n\n**SF-1. [共识, major] \"2.1% sign reversal under realistic accuracy (diagonal ≥ 0.7)\" 采样方法不透明**\n\nR1 计算后过滤法下约 73 个矩阵通过 diagonal ≥ 0.7 过滤（2.1% × 73 ≈ 1.5 个矩阵），统计功效极低。R2 核实发现附录 IV 分析使用 truncated sampling（每阈值 100K），但主文 Section 4.2 的 2.1% 未说明采样方法。Abstract 和 Introduction 均引用此数字作为核心 claim 证据。\n\n**共识**：主文需明确标注采样方法和有效样本量。如果使用后过滤，需补充 truncated sampling 实验和 CI。\n\n**SF-2. [共识, major] Proportional effects (f=λg) 在 NLP 场景中验证不足**\n\n两位一致：(a) 97.3% 检验的方法和标准不透明——可能仅指单一 DGP 配置下 23 个 LLM 的比例；(b) f 和 g 依赖真实 A（非观测 A*），可验证性存疑；(c) Appendix Table 13 显示 OOB 率 23%（K=3 mediation, non-proportional f），说明条件在非平凡场景下不满足。\n\n**建议**：明确 97.3% 的检验方法、DGP 数量和判定标准；讨论条件在什么 NLP 任务中合理（单维质量 vs 多维质量）。\n\n**SF-3. [共识, major] Linear SEM 限定不足**\n\n两位一致：Abstract 和 Conclusion 未限定 \"under linear structural equation models\"，可能给读者普遍适用的印象。Appendix B.14 的 logistic regression 验证（偏差 < 0.02）仅在 Section 4.5 一句话提及。CSS 研究中 logistic regression 远比 linear OLS 常见。\n\n**建议**：在 Abstract 或 Contribution 列表加入 \"under linear SEMs\" 限定；Conclusion 讨论 nonlinear 扩展。\n\n**SF-4. [R2 首提, R1 同意, major] MC-SIMEX 未引原始论文**\n\nMC-SIMEX 在 Section 4.5、Table 4、Algorithm 1 中多次使用，但原始论文 Küchenhoff, Mwalili & Lesaffre (2006, *Biometrics*) 完全未引用。MLA 也缺规范引用来源。引用规范问题。\n\n**SF-5. [R2 首提, R1 同意, major] \"First systematic topology-specific comparison\" 声称需限定**\n\nTeBlunthuis et al. (2024) 已做 K=2 + 4 种拓扑的系统比较。本文的增量贡献在于 K≥3 + 7 种拓扑——建议改为 \"the first multi-class (K≥3) topology-specific comparison\"。\n\n**SF-6. [R2 首提, R1 同意, minor] τ 符号拓扑依赖定义可能造成混淆**\n\nτ 在不同拓扑下含义不同（confounding: X 系数; exposure: β_j; mediation: τ_direct），但后续 ASV 和 correction 讨论中频繁用 τ 进行跨拓扑比较。建议用下标区分或在 Table 1 增加定义列。\n\n**SF-7. [共识, minor] NLP 读者可及性**\n\nplim, FWL, Wald estimator, column-stochastic polytope, perspective function convexity 等术语对 EMNLP 读者群不友好。plim 有脚注定义，但其他术语处理不一致。\n\n**SF-8. [R2, minor] 5 个 orphan bib 条目**\n\nimai_keele_tingley2010, miles2024measurement, neuhaus1999, richardson1993bayesian, valeri_vanderweele2014 在 .bib 中存在但未引用。\n\n**SF-9. [R1 首提, R2 同意, minor] C(δ) 线性路径假设的路径依赖性未讨论**\n\nC(δ)=(1−δ)I+δC₀ 是一条线性路径，但 column-stochastic polytope 中存在无数从 I 到 C₀ 的路径。不同路径上 ASV 阈值可能不同。Bootstrapping C₀ 部分缓解但路径形状影响未讨论。\n\n---\n\n## Reviewer Consensus [AGREE]\n\n1. **K≥3 Conjecture 1 未证明**是本文最大理论空白——两位一致标为 critical\n2. **FWL invariance 本身是 trivial corollary**——应降为 Observation，Contribution 3 重聚焦\n3. **Proportional effects 验证不足**——97.3% 声称缺乏透明度\n4. **Linear SEM 限定**——Abstract/Conclusion 需加限定词\n5. **MC-SIMEX 引用缺失**——must-add\n6. **\"First systematic\" overclaiming**——需限定为 K≥3\n7. **实证工作扎实**——161 scenarios, 1.6% MAPE, 3 real datasets\n\n## Reviewer Divergence [REBUT]\n\n1. **Conjecture 1 术语**：R2 建议改为 \"Empirical Observation\"，R1 反驳认为 Conjecture 有可证伪的定量声称，比 Observation 更精确。→ **Director 采纳 R1**：Conjecture 是诚实且精确的数学用语。\n\n2. **Limitations 长度**：R2 认为过短（3 句话），R1 反驳符合 EMNLP 2026 规则（覆盖 3 个核心限制点）。→ **Director 采纳 R1**：格式合规。但建议在 linear SEM 局限性上增加 1-2 句。\n\n3. **F₁ vs bias 讨论充分性**：R1 认为主文讨论不足，R2 反驳 Section 4.4 + Figure 4 + Appendix Table 21 已充分。→ **Director 采纳 R2**：讨论已充分。\n\n4. **R1-W2 \"21 vs 23 configurations\" 不一致**：R1 报告数值矛盾，R2 全文搜索未复现，可能是 R1 误读表号。→ **Director 撤销此项**。\n\n---\n\n## Questions（需要作者澄清）\n\n1. Section 4.2 的 \"2.1% sign reversal at diagonal ≥ 0.7\"：采样方法是后过滤还是 truncated sampling？有效样本量是多少？95% CI？\n2. Conjecture 1 的数值验证是否测试了 adversarial 矩阵结构（near-permutation, block-diagonal）？ε < 0.02 是否在 Dirichlet 之外的结构化矩阵上被验证？\n3. K=3 对称混淆矩阵（C_ij = c for i≠j）能否给出 monotonicity 的严格证明？\n4. \"97.3% of empirical LLM configurations satisfy proportional effects\"——检验方法、DGP 数量和判定标准是什么？\n5. 0% primary coefficient reversal 是 β 向量结构（dominant category）的产物，还是对 β₁ ≈ β₂ 的边界情况也成立？\n6. MC-SIMEX 和 MLA 的原始引用来源？\n7. \"binarization amplifies this gap 154×\"（Introduction）的精确含义：偏差比值还是概率比值？\n\n---\n\n## Missing References\n\n**Must-add:**\n- Küchenhoff, H., Mwalili, S. M., & Lesaffre, E. (2006). \"A general method for dealing with misclassification in regression: The misclassification SIMEX.\" *Biometrics*, 62(1), 85-96. — MC-SIMEX 原始论文\n- Frisch, R. & Waugh, F. V. (1933). \"Partial time regressions as compared with individual trends.\" *Econometrica*, 1(4), 387-401. — FWL 原始来源\n\n**Nice-to-have:**\n- Bross, I. D. J. (1954). \"Misclassification in 2×2 tables.\" *Biometrics*, 10(4), 478-486. — non-differential bias toward null 奠基论文\n- Yi, G. Y. (2017). *Statistical Analysis with Measurement Error or Misclassification.* Springer.\n- Hausman, J. A., Abrevaya, J., & Scott-Morton, F. M. (1998). \"Misclassification of the dependent variable in a discrete-response setting.\" *Journal of Econometrics*, 87(2), 239-269.\n- Miao, W., Geng, Z., & Tchetgen Tchetgen, E. J. (2018). \"Identifying causal effects with proxy variables of an unmeasured confounder.\" *Biometrika*, 105(4), 987-993.\n\n---\n\n## External Review\n\n**状态**：未请求（项目未配置外部审稿）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**：Agent 超时（300s timeout）。视觉审查未能完成，无 findings 可报告。用户可决定是否重新触发。\n\n---\n\n## Overall Assessment\n\n**评分: 3.5 / 5 (Borderline Conference)**\n\n**置信度**: 4/5（两位 Reviewer 均有因果推断和 NLP/CSS 背景，仔细检查了证明和数值声称）\n\n**评分理由**：\n\n本文解决了一个重要且及时的问题——LLM 标注误差在因果推断中的拓扑依赖性传播。Bias taxonomy（7 种拓扑 × K≥3）是扎实的实证贡献，safe/fragile 二分法对从业者有直接价值，F₁ 与偏差脱钩的论证令人信服。实验覆盖面广（161 scenarios, 1.6% MAPE, 3 real datasets），Theorem 1 的 K=2 证明严格，Proposition 7 的构造性反例有力。\n\n但论文存在一个核心结构性矛盾：**整篇叙事围绕 K≥3 的结构性转变展开（Abstract 第 2 句, Introduction 第 2 段），但 ASV 框架的理论基石仅对 K=2 得到证明。** K=2 的结果有成熟的先行文献（Brenner 1993），论文真正的理论增量在 K≥3——但这部分停留在 Conjecture 层面。此外，Contribution 3（FWL invariance）是 FWL 定理的直接推论，作为独立贡献分量不足。\n\n**如果作者能**：(a) 提供 K=3 特殊情况的 monotonicity 证明或更强的理论界；(b) 将 FWL invariance 降格并重构第三个贡献；(c) 明确 \"2.1%\" 的采样方法和 proportional effects 的检验标准；(d) 补充缺失引用——**论文有望达到 Conference 水平 (4.0)**。\n\n当前状态：实证工作足以支撑 **Findings 接收**，但理论深度不足以支撑主会议。\n\n---\n\n## Detailed Comments\n\n### Section 1 (Introduction)\n- \"the first systematic topology-specific comparison\" → 需限定为 K≥3（TeBlunthuis 2024 已做 K=2 + 4 topologies）\n- \"binarization amplifies this gap 154×\" → 需在正文解释 154× 的精确含义\n- 三个贡献的排列合理，但 Contribution 3 建议降级\n\n### Section 3.1 (Setup and Notation)\n- Non-differential misclassification 的 \"architectural invariant\" 论证已较充分（Y-stratified permutation test, stress test），是近期修改的改进点\n- plim 脚注定义有效，但 FWL, Wald, column-stochastic 等术语建议统一添加直觉解释\n\n### Section 3.2 (Multi-Class Bias Expressions)\n- 偏差表达式推导正确，七种拓扑的覆盖系统\n- τ 的拓扑依赖性定义需更清晰标注\n- \"83.4% sign reversal\" 和 \"2.1% under realistic accuracy\" 需注明 Dirichlet 先验和采样方法\n\n### Section 3.3 (ASV)\n- Theorem 1 (K=2) 证明严格\n- Conjecture 1 (K≥3) 是最大理论空白\n- Remark 1 (ASV vs E-values) 已重写为 \"complementary tools\"，定位合理\n- proportional effects (f=λg) 的 97.3% 声称需透明化\n\n### Section 4 (Experiments)\n- Theory-MC 对比（1.6% MAPE, 161 scenarios）有说服力\n- Table 1 的 safe/fragile 分区清晰\n- \"2.1%\" 采样方法需澄清\n- Figure 2 x 轴 scale 差异大，Figure 4 的 F₁ vs bias 讨论充分\n- Table 3 (ASV ranking) 是 headline result 但视觉不够醒目\n\n### Section 4.5 (Correction Guidance)\n- FWL invariance 作为 FWL 定理推论可在两句话内完成——建议降为 Observation\n- PPI++ 对 M-bias 有害 (−88%) 和 MC-SIMEX 对 front-door 有害 (−62.4%) 是非平凡的实证发现\n- Algorithm 1 有实用价值\n\n### Section 5 (Conclusion) + Limitations\n- Conclusion 在 page 8，格式合规\n- Limitations 覆盖 3 个核心限制点（non-differential, linear SEM, Monte Carlo），符合 EMNLP 2026 规则\n- 建议在 linear SEM 限制上增加 1-2 句讨论 logistic regression 的适用性\n\n### 格式合规\n- 正文 ≤ 8 页 ✓\n- Abstract < 200 words (187 words) ✓\n- Double-blind (Anonymous ACL submission) ✓\n- Limitations 在正文中 ✓\n- 5 个 orphan bib entries 需清理\n- MC-SIMEX / FWL 原始引用需补充",
  "project": "causal_annot_error_attrib",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.5 - Borderline Conference",
  "review_chat_id": "oc_9f117624057fcf6cb95db4d67f525246"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# Round 19 审稿报告\n\n**论文**: Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction\n**Venue**: EMNLP 2026 (ACL ARR Long Paper)\n**Deadline**: 2026-05-25\n**审稿模式**: Fresh (重新审稿)\n**Reviewer 编排**: 2 人（R1: 方法严谨性+理论证明+实验验证；R2: 新颖性+相关工作+写作质量+格式合规）\n\n---\n\n## Summary\n\n本文系统研究 K-class non-differential misclassification 在七种典型 DAG 拓扑下对因果估计的偏差传播。主要贡献包括：(1) 推导了七种拓扑下的闭合形式偏差表达式，建立 sign-preserving（5 种）vs sign-reversing（exposure, IV）的二分法；(2) 引入 Annotation Sensitivity Values (ASV) 框架，在 K=2 下证明了 envelope monotonicity（Theorem 1），在 K≥3 下以 Conjecture 形式给出 ε-approximate monotonicity；(3) 证明 FWL invariance 导致 matrix-based corrections 对四种协变量拓扑无效，并提供拓扑感知的校正决策流程。实验覆盖 100,000 Monte Carlo 矩阵 + 23 个 empirical LLM 配置 + 3 个 NLP 数据集（HumAID K=10, VAST K=3, CivilComments K=2），161 个场景下 theory-MC MAPE 仅 1.6%。\n\n---\n\n## Strengths\n\n**S1. [共识] 重要且及时的研究问题。** LLM 标注在 CSS 中的快速普及（Gilardi 2023; Ziems 2024; Baumann 2025）使标注误差对因果推断的影响成为紧迫问题。F₁ 与因果偏差无显著相关（Spearman ρ = −0.10, p = 0.45; Figure 4）有力论证了拓扑分析的必要性。\n\n**S2. [共识] 全面的拓扑覆盖和系统性实证验证。** 7 种 DAG × K=2,3,5,7,10 × 4 个 LLM × 3 个 NLP 数据集 → 161 场景，grand MAPE 1.6%。多层级验证（理论-MC 对比 + 真实 LLM 矩阵 + 跨 K 鲁棒性）有说服力。\n\n**S3. [共识] 清晰的安全/脆弱二分法。** Table 1 将 7 种拓扑分为 sign-preserving vs sign-reversing，为从业者提供直接可用的风险指引——这是论文最有实用价值的贡献。\n\n**S4. [R1] Theorem 1（K=2 monotonicity）证明完整。** Appendix A.4 使用 perspective function convexity 建立严格证明，论证结构清晰。\n\n**S5. [R1] Proposition 7（K≥3 exposure sign reversal counterexample）是强力构造性结果。** 直接构造了 C_kk > 0.5 仍导致符号反转的反例，明确了 K=2 vs K≥3 的分界线。\n\n**S6. [R2] Abstract 信息密度高且合规（约 187 words，< 200 限制）。** 格式总体合规，8 页正文限制已满足。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**MF-1. [共识, critical] K≥3 Conjecture 1 未证明，但承载了 ASV 框架的核心实用性**\n\n两位 Reviewer 一致认为这是本文最大的理论空白。论文的核心叙事围绕 K≥3 的结构性新现象（sign reversal, topology-dependent vulnerability），但 ASV 框架的理论基石——envelope monotonicity——仅对 K=2 且在 proportional effects (f=λg) 条件下得到证明（Theorem 1）。K≥3 的结果以 Conjecture 1 形式呈现，依赖 Dirichlet(1,...,1) 采样的数值验证。\n\nR1 指出：K=2 证明方法（perspective function convexity + V_B(0)=0）结构上依赖 2×2 代数简化（\"for K=2 only\"），无法直接推广。数值验证未覆盖 adversarial 矩阵结构（near-permutation, block-diagonal）。R2 补充：这意味着论文对最不需要理论支撑的简单情况（K=2 经典衰减已有 Brenner 1993）给出了证明，对最需要的核心情况给出了猜想。\n\nASV vulnerability ranking（Table 3）和 Algorithm 1 在 K≥3 时的有效性完全依赖此 conjecture。如果 K≥3 的 ε-approximate monotonicity 在特定结构化矩阵上失效，ASV 排序的可靠性将受质疑。\n\n**建议**：(a) 尝试 K=3 特殊情况证明（如对称混淆矩阵）；(b) 补充 adversarial 矩阵测试；(c) 在正文更显著标注 K≥3 结果的 conjecture 性质——不是 Limitations 中的 \"primary open question\"，而是 ASV 框架可靠性的前提条件。\n\n**MF-2. [R2 首提, R1 部分同意] Contribution 3（FWL invariance + correction routing）分量不足**\n\nR2 指出 FWL invariance（matrix-based corrections 对四种协变量拓扑无效）是 FWL 定理的直接推论：对协变量 dummy 变量的线性变换不改变处理变量系数——这从 FWL 的列空间保持性质直接可得。Section 4.5 两句话即推导完毕。\n\nR1 交叉回应部分同意 FWL invariance 本身的 triviality，但认为 Contribution 3 的完整范围包括 Algorithm 1（拓扑→校正方法决策流程）和 Table 4 的五种方法跨拓扑比较（210 configurations），这些超越了单纯的 FWL 推论。\n\n**共识**：FWL invariance 降为 Observation/Remark，Contribution 3 重聚焦于拓扑依赖的校正方法排序和决策流程（实证发现，非理论推论）。\n\n### Should-Fix（影响评分但不一票否决）\n\n**SF-1. [共识, major] \"2.1% sign reversal under realistic accuracy (diagonal ≥ 0.7)\" 采样方法不透明**\n\nR1 计算后过滤法下约 73 个矩阵通过 diagonal ≥ 0.7 过滤（2.1% × 73 ≈ 1.5 个矩阵），统计功效极低。R2 核实发现附录 IV 分析使用 truncated sampling（每阈值 100K），但主文 Section 4.2 的 2.1% 未说明采样方法。Abstract 和 Introduction 均引用此数字作为核心 claim 证据。\n\n**共识**：主文需明确标注采样方法和有效样本量。如果使用后过滤，需补充 truncated sampling 实验和 CI。\n\n**SF-2. [共识, major] Proportional effects (f=λg) 在 NLP 场景中验证不足**\n\n两位一致：(a) 97.3% 检验的方法和标准不透明——可能仅指单一 DGP 配置下 23 个 LLM 的比例；(b) f 和 g 依赖真实 A（非观测 A*），可验证性存疑；(c) Appendix Table 13 显示 OOB 率 23%（K=3 mediation, non-proportional f），说明条件在非平凡场景下不满足。\n\n**建议**：明确 97.3% 的检验方法、DGP 数量和判定标准；讨论条件在什么 NLP 任务中合理（单维质量 vs 多维质量）。\n\n**SF-3. [共识, major] Linear SEM 限定不足**\n\n两位一致：Abstract 和 Conclusion 未限定 \"under linear structural equation models\"，可能给读者普遍适用的印象。Appendix B.14 的 logistic regression 验证（偏差 < 0.02）仅在 Section 4.5 一句话提及。CSS 研究中 logistic regression 远比 linear OLS 常见。\n\n**建议**：在 Abstract 或 Contribution 列表加入 \"under linear SEMs\" 限定；Conclusion 讨论 nonlinear 扩展。\n\n**SF-4. [R2 首提, R1 同意, major] MC-SIMEX 未引原始论文**\n\nMC-SIMEX 在 Section 4.5、Table 4、Algorithm 1 中多次使用，但原始论文 Küchenhoff, Mwalili & Lesaffre (2006, *Biometrics*) 完全未引用。MLA 也缺规范引用来源。引用规范问题。\n\n**SF-5. [R2 首提, R1 同意, major] \"First systematic topology-specific comparison\" 声称需限定**\n\nTeBlunthuis et al. (2024) 已做 K=2 + 4 种拓扑的系统比较。本文的增量贡献在于 K≥3 + 7 种拓扑——建议改为 \"the first multi-class (K≥3) topology-specific comparison\"。\n\n**SF-6. [R2 首提, R1 同意, minor] τ 符号拓扑依赖定义可能造成混淆**\n\nτ 在不同拓扑下含义不同（confounding: X 系数; exposure: β_j; mediation: τ_direct），但后续 ASV 和 correction 讨论中频繁用 τ 进行跨拓扑比较。建议用下标区分或在 Table 1 增加定义列。\n\n**SF-7. [共识, minor] NLP 读者可及性**\n\nplim, FWL, Wald estimator, column-stochastic polytope, perspective function convexity 等术语对 EMNLP 读者群不友好。plim 有脚注定义，但其他术语处理不一致。\n\n**SF-8. [R2, minor] 5 个 orphan bib 条目**\n\nimai_keele_tingley2010, miles2024measurement, neuhaus1999, richardson1993bayesian, valeri_vanderweele2014 在 .bib 中存在但未引用。\n\n**SF-9. [R1 首提, R2 同意, minor] C(δ) 线性路径假设的路径依赖性未讨论**\n\nC(δ)=(1−δ)I+δC₀ 是一条线性路径，但 column-stochastic polytope 中存在无数从 I 到 C₀ 的路径。不同路径上 ASV 阈值可能不同。Bootstrapping C₀ 部分缓解但路径形状影响未讨论。\n\n---\n\n## Reviewer Consensus [AGREE]\n\n1. **K≥3 Conjecture 1 未证明**是本文最大理论空白——两位一致标为 critical\n2. **FWL invariance 本身是 trivial corollary**——应降为 Observation，Contribution 3 重聚焦\n3. **Proportional effects 验证不足**——97.3% 声称缺乏透明度\n4. **Linear SEM 限定**——Abstract/Conclusion 需加限定词\n5. **MC-SIMEX 引用缺失**——must-add\n6. **\"First systematic\" overclaiming**——需限定为 K≥3\n7. **实证工作扎实**——161 scenarios, 1.6% MAPE, 3 real datasets\n\n## Reviewer Divergence [REBUT]\n\n1. **Conjecture 1 术语**：R2 建议改为 \"Empirical Observation\"，R1 反驳认为 Conjecture 有可证伪的定量声称，比 Observation 更精确。→ **Director 采纳 R1**：Conjecture 是诚实且精确的数学用语。\n\n2. **Limitations 长度**：R2 认为过短（3 句话），R1 反驳符合 EMNLP 2026 规则（覆盖 3 个核心限制点）。→ **Director 采纳 R1**：格式合规。但建议在 linear SEM 局限性上增加 1-2 句。\n\n3. **F₁ vs bias 讨论充分性**：R1 认为主文讨论不足，R2 反驳 Section 4.4 + Figure 4 + Appendix Table 21 已充分。→ **Director 采纳 R2**：讨论已充分。\n\n4. **R1-W2 \"21 vs 23 configurations\" 不一致**：R1 报告数值矛盾，R2 全文搜索未复现，可能是 R1 误读表号。→ **Director 撤销此项**。\n\n---\n\n## Questions（需要作者澄清）\n\n1. Section 4.2 的 \"2.1% sign reversal at diagonal ≥ 0.7\"：采样方法是后过滤还是 truncated sampling？有效样本量是多少？95% CI？\n2. Conjecture 1 的数值验证是否测试了 adversarial 矩阵结构（near-permutation, block-diagonal）？ε < 0.02 是否在 Dirichlet 之外的结构化矩阵上被验证？\n3. K=3 对称混淆矩阵（C_ij = c for i≠j）能否给出 monotonicity 的严格证明？\n4. \"97.3% of empirical LLM configurations satisfy proportional effects\"——检验方法、DGP 数量和判定标准是什么？\n5. 0% primary coefficient reversal 是 β 向量结构（dominant category）的产物，还是对 β₁ ≈ β₂ 的边界情况也成立？\n6. MC-SIMEX 和 MLA 的原始引用来源？\n7. \"binarization amplifies this gap 154×\"（Introduction）的精确含义：偏差比值还是概率比值？\n\n---\n\n## Missing References\n\n**Must-add:**\n- Küchenhoff, H., Mwalili, S. M., & Lesaffre, E. (2006). \"A general method for dealing with misclassification in regression: The misclassification SIMEX.\" *Biometrics*, 62(1), 85-96. — MC-SIMEX 原始论文\n- Frisch, R. & Waugh, F. V. (1933). \"Partial time regressions as compared with individual trends.\" *Econometrica*, 1(4), 387-401. — FWL 原始来源\n\n**Nice-to-have:**\n- Bross, I. D. J. (1954). \"Misclassification in 2×2 tables.\" *Biometrics*, 10(4), 478-486. — non-differential bias toward null 奠基论文\n- Yi, G. Y. (2017). *Statistical Analysis with Measurement Error or Misclassification.* Springer.\n- Hausman, J. A., Abrevaya, J., & Scott-Morton, F. M. (1998). \"Misclassification of the dependent variable in a discrete-response setting.\" *Journal of Econometrics*, 87(2), 239-269.\n- Miao, W., Geng, Z., & Tchetgen Tchetgen, E. J. (2018). \"Identifying causal effects with proxy variables of an unmeasured confounder.\" *Biometrika*, 105(4), 987-993.\n\n---\n\n## External Review\n\n**状态**：未请求（项目未配置外部审稿）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**：Agent 超时（300s timeout）。视觉审查未能完成，无 findings 可报告。用户可决定是否重新触发。\n\n---\n\n## Overall Assessment\n\n**评分: 3.5 / 5 (Borderline Conference)**\n\n**置信度**: 4/5（两位 Reviewer 均有因果推断和 NLP/CSS 背景，仔细检查了证明和数值声称）\n\n**评分理由**：\n\n本文解决了一个重要且及时的问题——LLM 标注误差在因果推断中的拓扑依赖性传播。Bias taxonomy（7 种拓扑 × K≥3）是扎实的实证贡献，safe/fragile 二分法对从业者有直接价值，F₁ 与偏差脱钩的论证令人信服。实验覆盖面广（161 scenarios, 1.6% MAPE, 3 real datasets），Theorem 1 的 K=2 证明严格，Proposition 7 的构造性反例有力。\n\n但论文存在一个核心结构性矛盾：**整篇叙事围绕 K≥3 的结构性转变展开（Abstract 第 2 句, Introduction 第 2 段），但 ASV 框架的理论基石仅对 K=2 得到证明。** K=2 的结果有成熟的先行文献（Brenner 1993），论文真正的理论增量在 K≥3——但这部分停留在 Conjecture 层面。此外，Contribution 3（FWL invariance）是 FWL 定理的直接推论，作为独立贡献分量不足。\n\n**如果作者能**：(a) 提供 K=3 特殊情况的 monotonicity 证明或更强的理论界；(b) 将 FWL invariance 降格并重构第三个贡献；(c) 明确 \"2.1%\" 的采样方法和 proportional effects 的检验标准；(d) 补充缺失引用——**论文有望达到 Conference 水平 (4.0)**。\n\n当前状态：实证工作足以支撑 **Findings 接收**，但理论深度不足以支撑主会议。\n\n---\n\n## Detailed Comments\n\n### Section 1 (Introduction)\n- \"the first systematic topology-specific comparison\" → 需限定为 K≥3（TeBlunthuis 2024 已做 K=2 + 4 topologies）\n- \"binarization amplifies this gap 154×\" → 需在正文解释 154× 的精确含义\n- 三个贡献的排列合理，但 Contribution 3 建议降级\n\n### Section 3.1 (Setup and Notation)\n- Non-differential misclassification 的 \"architectural invariant\" 论证已较充分（Y-stratified permutation test, stress test），是近期修改的改进点\n- plim 脚注定义有效，但 FWL, Wald, column-stochastic 等术语建议统一添加直觉解释\n\n### Section 3.2 (Multi-Class Bias Expressions)\n- 偏差表达式推导正确，七种拓扑的覆盖系统\n- τ 的拓扑依赖性定义需更清晰标注\n- \"83.4% sign reversal\" 和 \"2.1% under realistic accuracy\" 需注明 Dirichlet 先验和采样方法\n\n### Section 3.3 (ASV)\n- Theorem 1 (K=2) 证明严格\n- Conjecture 1 (K≥3) 是最大理论空白\n- Remark 1 (ASV vs E-values) 已重写为 \"complementary tools\"，定位合理\n- proportional effects (f=λg) 的 97.3% 声称需透明化\n\n### Section 4 (Experiments)\n- Theory-MC 对比（1.6% MAPE, 161 scenarios）有说服力\n- Table 1 的 safe/fragile 分区清晰\n- \"2.1%\" 采样方法需澄清\n- Figure 2 x 轴 scale 差异大，Figure 4 的 F₁ vs bias 讨论充分\n- Table 3 (ASV ranking) 是 headline result 但视觉不够醒目\n\n### Section 4.5 (Correction Guidance)\n- FWL invariance 作为 FWL 定理推论可在两句话内完成——建议降为 Observation\n- PPI++ 对 M-bias 有害 (−88%) 和 MC-SIMEX 对 front-door 有害 (−62.4%) 是非平凡的实证发现\n- Algorithm 1 有实用价值\n\n### Section 5 (Conclusion) + Limitations\n- Conclusion 在 page 8，格式合规\n- Limitations 覆盖 3 个核心限制点（non-differential, linear SEM, Monte Carlo），符合 EMNLP 2026 规则\n- 建议在 linear SEM 限制上增加 1-2 句讨论 logistic regression 的适用性\n\n### 格式合规\n- 正文 ≤ 8 页 ✓\n- Abstract < 200 words (187 words) ✓\n- Double-blind (Anonymous ACL submission) ✓\n- Limitations 在正文中 ✓\n- 5 个 orphan bib entries 需清理\n- MC-SIMEX / FWL 原始引用需补充",
    "project": "causal_annot_error_attrib",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.5 - Borderline Conference",
    "review_chat_id": "oc_9f117624057fcf6cb95db4d67f525246"
  }
}
```

</details>

---


### Tool result

_source line 1597 · 2026-05-23T17:23:08.373753+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_ca838cd3ed4c7e2d9c8e3459edd98b90:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4181
}
```

</details>

---


### Tool call

_source line 1598 · 2026-05-23T17:23:19.477787+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '执行资料检查和 Venue 调研'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.6/0.7: 派发视觉审查 + Reviewer', 'status': 'completed', 'activeForm': '派发视觉审查和 Reviewer 任务'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'completed', 'activeForm': '等待 Reviewer 独立审稿'}, {'content': 'Step 2: 交叉分享', 'status': 'completed', 'activeForm': '执行交叉分享'}, {'content': 'Step 3: 收敛判断', 'status': 'completed', 'activeForm': '判断收敛'}, {'content': 'Step 4: 汇总报告 & 投递', 'status': 'completed', 'activeForm': '汇总报告并投递'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '执行资料检查和 Venue 调研'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.6/0.7: 派发视觉审查 + Reviewer', 'status': 'completed', 'activeForm': '派发视觉审查和 Reviewer 任务'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'completed', 'activeForm': '等待 Reviewer 独立审稿'}, {'content': 'Step 2: 交叉分享', 'status': 'completed', 'activeForm': '执行交叉分享'}, {'content': 'Step 3: 收敛判断', 'status': 'completed', 'activeForm': '判断收敛'}, {'content': 'Step 4: 汇总报告 & 投递', 'status': 'completed', 'activeForm': '汇总报告并投递'}]"
  }
}
```

</details>

---


### Tool result

_source line 1599 · 2026-05-23T17:23:19.528681+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "TodoWrite",
  "elapsed_ms": 50
}
```

</details>

---


### Assistant

_source line 1600 · 2026-05-23T17:23:32.426109+00:00_

Round 19 审稿报告已投递至 Research Director。

**审稿结论：3.5 / 5 (Borderline Conference)**

核心发现：
- **MF-1 [critical]**：K≥3 Conjecture 1 未证明——论文核心叙事围绕 K≥3 但理论仅覆盖 K=2，是最大结构性矛盾
- **MF-2 [should-fix]**：FWL invariance 是 FWL 定理直接推论，Contribution 3 需重聚焦
- **SF-1 [major]**：2.1% sign reversal 采样方法不透明
- **SF-2 [major]**：Proportional effects 97.3% 声称缺乏透明度
- **SF-3 [major]**：Linear SEM 限定不足
- **SF-4 [major]**：MC-SIMEX + FWL 原始引用缺失

实证工作足以支撑 Findings 接收，但理论深度不足以支撑主会议。Issue tracker 已同步更新（6 个新 issue，17 个现有 issue 更新）。视觉审查因超时未完成。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 160

## Round 160

2 recorded events


### User

_source line 1601 · 2026-05-23T17:23:34.989951+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。核心结论：

- **R1-N1 (Conjecture 未证明)**: [AGREE]，与我的 N1 一致
- **R1-N2 (2.1% 统计功效)**: [AGREE]，但附录有 truncated sampling 证据，severity 可能从 critical 降为 major
- **R1-W1 (proportional effects)**: [AGREE]
- **R1-W2 (21 vs 23 不一致)**: [REBUT]，全文检索未发现 "21 configurations"，论文始终使用 23
- **R1-W3 (线性 SEM 边界)**: [AGREE]
- **R1-W4 (C(δ) 路径依赖)**: [AGREE]
- **R1-W5 (不可观测条件)**: [AGREE]，但实证 0% 违反率部分缓解
- **小问题**: 3 条 AGREE，1 条 REBUT (F₁ vs bias 讨论已足够)
- **R1 Missing Ref (Miao et al. 2018)**: [AGREE]，边缘相关但值得引用

两位 Reviewer 的核心关切高度重叠，评分一致 (3.5)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1602 · 2026-05-23T17:23:50.891134+00:00_

Round 19 审稿已完成。

**审稿报告已投递至 Research Director。**

**最终评分：3.5 / 5（Borderline Conference）**

核心发现：
1. **[critical] K≥3 Conjecture 1 未证明** — 论文叙事围绕 K≥3 但理论仅覆盖 K=2，ASV 框架在 K≥3 的可靠性依赖未证明的 conjecture
2. **[should-fix] Contribution 3 (FWL invariance) 分量不足** — 共识降为 Observation，重聚焦于 correction routing 实证
3. **[major] "2.1% sign reversal" 采样方法不透明** — 需明确后过滤 vs truncated sampling
4. **[major] Proportional effects 验证不足** — 97.3% 声称缺乏透明度
5. **[major] Linear SEM 限定缺失** — Abstract/Conclusion 需加限定词
6. **[major] MC-SIMEX 未引原始论文** — Küchenhoff et al. (2006) must-add

实证工作扎实，可支撑 Findings 接收；补充 K=3 理论界 + 重构 Contribution 3 + 明确采样方法后有望达 Conference (4.0)。

Issue tracker 和审稿报告均已同步更新。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 161

## Round 161

40 recorded events


### User

_source line 1603 · 2026-05-23T18:32:42.580407+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: causal_annot_error_attrib
- 论文路径: projects/causal_annot_error_attrib/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: ARR Long Paper
- 截止日期: 2026-05-25
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 1604 · 2026-05-23T18:32:49.940888+00:00_

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
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 1605 · 2026-05-23T18:32:50.343562+00:00_

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
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 1606 · 2026-05-23T18:32:55.826995+00:00_

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
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
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

_source line 1607 · 2026-05-23T18:32:55.928013+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "ToolSearch",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 1608 · 2026-05-23T18:33:02.309487+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "causal_annot_error_attrib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "causal_annot_error_attrib"
  }
}
```

</details>

---


### Tool result

_source line 1609 · 2026-05-23T18:33:03.214475+00:00_

{"result":"# 项目 causal_annot_error_attrib 概况\n\n## 实验状态 (14 个)\n\n- **plan006_asv_empirical**: DONE (success) — \n- **plan010_annot_sensitivity_toolkit**: DONE (success) — \n- **plan003_empirical_confusion_matrices**: DONE (failed) — \n- **plan007_correction_guidance**: DONE (success) — \n- **plan009_pathological_matrices**: DONE (success) — \n- **plan005_asv_extended**: DONE (success) — \n- **plan002_k57_extension**: DONE (success) — \n- **plan001_dag_taxonomy**: DONE (success) — \n- **plan004_asv_framework**: DONE (success) — \n- **plan_004_asv_v3_fixed**: DONE (success) — \n- **plan008_binarization_collapse**: DONE (success) — \n- **mvp_exposure_dirichlet_subspace**: DONE (success) — \n- **mvp_exposure_dag**: DONE (success) — \n- **mvp_confounding_dag**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-21\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n（无）\n\n## 近期结论\n- **plan006_asv_empirical** (success): 真实 LLM confusion matrices（跨 K=2/3/10，跨 7B/235B 模型）在 7 种 DAG 拓扑下的偏差传播与理论预测一致：(1) F1 高不代表因果估计安全（F1=0.72 但 IV bias>100%），(2) 0 sign flips 确认结构性保证，(3) topology（非 K 或 model size）是 bias 的主要决定因素。\n- **plan010_annot_sensitivity_toolkit** (success): 封装 7-topology bias computation、ASV sensitivity framework 和 5 种 correction 方法为可复用 Python 包，使 practitioners 能用 3 行代码评估 LLM 标注误差对因果推断的影响。验证：(1) API 输出与 plan_001/004/005/007 原始脚本一致，(2) worked example 展示完整工作流，(3) 35 个 pytest 全通过。\n- **plan003_empirical_confusion_matrices** (failed): Different LLMs (Llama-4-Maverick, Qwen3-235B, DeepSeek-Chat) produce systematically different confusion matrices on the same classification tasks, and these empirical confusion matrices can be used to quantify annotation error propagation in downstream causal inference.\n\n## 趋势\n成功 13 / 负向 0 / 失败 1 / 共 14\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nhome-1x5090: 无 GPU 信息\n\n## 告警\n- plan003_empirical_confusion_matrices: 训练失败 — unknown"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 904
}
```

</details>

---


### Tool call

_source line 1610 · 2026-05-23T18:33:03.365364+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/main.tex",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/main.tex",
    "limit": "80"
  }
}
```

</details>

---


### Tool result

_source line 1611 · 2026-05-23T18:33:03.415921+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	
4	\usepackage{graphicx}
5	\usepackage{algorithm}
6	\usepackage{algorithmic}
7	
8	\usepackage{amsmath,amssymb,amsthm}
9	\usepackage{booktabs}
10	\usepackage{pifont}
11	\usepackage{multirow}
12	
13	\newtheorem{definition}{Definition}
14	\newtheorem{proposition}{Proposition}
15	\newtheorem{theorem}{Theorem}
16	\newtheorem{lemma}{Lemma}
17	\newtheorem{conjecture}{Conjecture}
18	\newtheorem{observation}{Observation}
19	\newtheorem{remark}{Remark}
20	
21	\setlength{\textfloatsep}{8pt plus 2pt minus 4pt}
22	\setlength{\dbltextfloatsep}{8pt plus 2pt minus 4pt}
23	\setlength{\floatsep}{8pt plus 2pt minus 4pt}
24	\setlength{\dblfloatsep}{8pt plus 2pt minus 4pt}
25	\graphicspath{{../../figures/paper/}}
26	
27	\title{Multi-Class Annotation Errors in Causal Inference:\\Topology-Dependent Bias, Sensitivity, and Correction}
28	
29	\author{Anonymous}
30	
31	\begin{document}
32	\maketitle
33	
34	\input{abstract}
35	
36	\input{introduction}
37	
38	\begin{figure*}[t]
39	\centering
40	\includegraphics[width=0.92\textwidth,height=0.18\textheight,keepaspectratio]{fig1_dag_taxonomy.pdf}
41	\vspace{-6pt}
42	\caption{Seven canonical DAG topologies with starred-node annotation~\cite{hernan_cole2009}. $A$ (latent) $\to$ $A^*$ (observed) via a dashed measurement edge; the causal role of $A$ varies: treatment (exposure), covariate (confounding, mediation, M-bias, front-door), selection (collider), instrument (IV).}
43	\label{fig:dag_taxonomy}
44	\end{figure*}
45	
46	\input{related_work}
47	
48	\input{method}
49	
50	\input{experiments}
51	
52	\input{conclusion}
53	
54	\bibliography{references}
55	
56	\appendix
57	\input{appendix_proofs}
58	
59	\end{document}
60	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1612 · 2026-05-23T18:33:09.797711+00:00_

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
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
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

_source line 1613 · 2026-05-23T18:33:09.848576+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1614 · 2026-05-23T18:33:21.705747+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 ARR call for papers submission guidelines author instructions"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 ARR call for papers submission guidelines author instructions"
  }
}
```

</details>

---


### Tool call

_source line 1615 · 2026-05-23T18:33:22.057711+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 1616 · 2026-05-23T18:33:22.108331+00:00_

1	\begin{abstract}
2	Large language models are increasingly used as annotators in computational social science, yet annotation errors propagate into downstream causal estimates in ways that depend on both the confusion matrix structure and the causal DAG topology. We derive bias expressions for seven canonical topologies under $K$-class non-differential misclassification in linear structural equation models and show that $K {\geq} 3$ introduces a structural possibility of sign reversal absent in the binary case. We prove sign preservation for confounding and collider, and verify it numerically for mediation, M-bias, and front-door; exposure and IV topologies can reverse the treatment effect sign. Under realistic LLM accuracy, sign reversal of non-dominant coefficients occurs under exposure; under empirical LLM matrices (diagonal 0.45--0.81), sign reversal is confined to exposure; IV is fragile under uniform Dirichlet priors but exhibits zero reversals under empirical LLM matrices. We introduce Annotation Sensitivity Values (ASVs), with proved ($K{=}2$) and numerically verified ($K{\geq}3$) monotonicity, yielding a vulnerability ranking from IV (maximally fragile) to M-bias (immune), and show that matrix-based corrections are provably ineffective under linear regression for four topologies due to Frisch--Waugh--Lovell invariance. Topology-aware analysis is necessary for valid causal inference with LLM-generated annotations.
3	\end{abstract}
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1617 · 2026-05-23T18:33:22.611002+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 1618 · 2026-05-23T18:33:22.661814+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Large language models are rapidly replacing human annotators in computational social science, with researchers using LLM-generated labels for tasks ranging from sentiment classification to political stance detection~\cite{gilardi2023chatgpt, ziems2024can, egami_hinck_stewart_wei2023, baumann2025}. Crucially, most of these tasks are inherently multi-class: stance detection uses 3--4 categories, sentiment analysis 5, and disaster response taxonomies 10 or more. This shift promises dramatic cost reduction, but introduces a critical validity gap: annotation errors (equivalently, misclassification) from imperfect classifiers propagate into downstream causal estimates in ways that depend on both the error structure and the causal design. \citet{baumann2025} demonstrate that across 37 annotation tasks, 31\% of hypotheses yield incorrect conclusions with state-of-the-art LLMs, rising to 50\% for smaller models; these errors are highly correlated across models (60\% agreement when both err)~\cite{kim_garg2025}, undermining ensemble-based mitigation. Analyzing the \emph{structure} of annotation error, rather than simply reducing its magnitude, is essential for valid downstream inference.
5	
6	The transition at $K{\geq}3$ is not gradual but structural. For $K{=}2$, the stochastic constraint forces any confusion matrix with positive diagonal to preserve coefficient signs---an algebraic property of the $2{\times}2$ matrix dimension~\cite{brenner1993}. This guarantee \emph{vanishes} at $K{\geq}3$: the higher-dimensional confusion matrix admits negative effective weights on categories with opposite-sign coefficients, enabling sign reversal even under high accuracy~\cite{veirod_laake2001}. Under a uniform Dirichlet prior, 83.4\% of $K{=}3$ exposure confusion matrices produce sign reversal of at least one secondary coefficient; under realistic accuracy (diagonal $\geq 0.7$), 2.1\% still do. The primary treatment coefficient is
…[truncated 3162 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 1619 · 2026-05-23T18:33:32.382800+00:00_

Web search results for query: "EMNLP 2026 ARR call for papers submission guidelines author instructions"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Submission Guide","url":"https://nlp4climate.github.io/submissionguide/"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title":"AI Conference Deadlines - Jie Cao | Dialogue, NLP, ML","url":"https://mlciv.com/ai-deadlines/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"}]

Based on the search results, here's a comprehensive summary of the EMNLP 2026 ARR Call for Papers submission guidelines and author instructions:

## Overview

EMNLP 2026 invites the submission of long and short papers featuring substantial, original, and unpublished research on empirical methods for Natural Language Processing. Papers may contribute negative findings, survey an area, announce the creation of a new resource, argue a position, report no
…[truncated 2301 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "WebSearch",
  "elapsed_ms": 10677
}
```

</details>

---


### Tool call

_source line 1620 · 2026-05-23T18:33:43.135709+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/method.tex",
  "limit": "120"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/method.tex",
    "limit": "120"
  }
}
```

</details>

---


### Tool result

_source line 1621 · 2026-05-23T18:33:43.589104+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Setup and Notation}
5	\label{sec:notation}
6	
7	Let $A$ denote a true $K$-class categorical variable (e.g., sentiment with $K{=}3$ levels) and $A^*$ its observed, potentially misclassified version produced by an LLM annotator. The misclassification process is characterized by a $K{\times}K$ confusion matrix $C$ with entries $C_{jk} = P(A^*{=}j \mid A{=}k)$, where each column sums to one (column-stochastic: each column gives the distribution of predicted labels for a given true label). Following \citet{hernan_cole2009}, we represent this measurement process using \emph{starred-node} DAGs: the true variable $A$ is latent, and the observed $A^*$ is connected to $A$ via a dashed measurement edge.
8	
9	\paragraph{Notation conventions.}
10	Our analysis characterizes systematic bias---the value an estimator converges to as $N \to \infty$ (the probability limit, or plim)---rather than finite-sample variance. The Frisch--Waugh--Lovell (FWL) theorem~\cite{frisch1933partial} guarantees that each regression coefficient equals the coefficient from a simple regression after residualizing all other variables; this is why matrix-based corrections fail for covariate topologies (Section~\ref{sec:correction}): replacing the mismeasured variable with a corrected version does not change the residualized relationship. The Wald estimator (ratio of reduced-form to first-stage effects) diverges under weak instruments; Dirichlet priors over probability vectors represent uncertainty over misclassification patterns. Table~\ref{tab:notation} (Appendix~\ref{app:notation_table}) collects all notation.
11	
12	\begin{definition}[Non-differential misclassification]
13	\label{def:nondiff}
14	Misclassification of $A$ is non-differential with respect to outcome $Y$ and covariates $\mathbf{Z}$ if $P(A^*{=}j \mid A{=}k, Y, \mathbf{Z}) = P(A^*{=}j \mid A{=}k) = C_{jk}$ for all $j,k$.
15	\end{definition}
16	
17	In batch annotation pipelines, the LLM 
…[truncated 14028 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 453
}
```

</details>

---


### Tool call

_source line 1622 · 2026-05-23T18:33:44.041878+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/experiments.tex",
  "limit": "120"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/experiments.tex",
    "limit": "120"
  }
}
```

</details>

---


### Tool result

_source line 1623 · 2026-05-23T18:33:45.047502+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We validate through Monte Carlo simulation ($K{=}3$), cross-$K$ robustness checks ($K{=}5,7$), and empirical validation with real LLM confusion matrices from three NLP tasks ($K{=}2,3,10$).
5	
6	\subsection{Setup}
7	\label{sec:setup}
8	
9	For each topology, we sample 100{,}000 confusion matrices from a Dirichlet$(1,1,1)$ prior, compute analytical probability limits, and validate against Monte Carlo simulation ($N{=}10{,}000$). ASV experiments use $C(\delta) = (1{-}\delta)I + \delta C_0$.
10	
11	\subsection{Bias Taxonomy}
12	\label{sec:taxonomy_results}
13	
14	\paragraph{Theory-MC agreement.}
15	Analytical probability limits match Monte Carlo estimates with grand MAPE of 1.6\% across 161 scenarios (23 LLM configurations $\times$ 7 topologies; per-topology range: 0.3\%--3.7\%).
16	
17	\paragraph{Exposure DAG: sign reversal under multi-class misclassification.}
18	Under realistic LLM accuracy (diagonal $\geq 0.7$), the violation rate is 13.7\% with 2.1\% sign reversal (100{,}000 Dirichlet-truncated matrices per diagonal threshold; Appendix~\ref{sec:iv_dirichlet_subspace}); even at diagonal $\geq 0.9$, violation persists at 11.9\%. Under the full Dirichlet$(1,1,1)$ prior, 85\% of $K{=}3$ confusion matrices violate the binary ``toward-null'' guarantee, and 83.4\% cause sign reversal of at least one coefficient; the minimum diagonal entry $\min_k C_{kk} < 0.55$ predicts sign reversal with 91\% accuracy across empirical matrices (Appendix~\ref{sec:sign_determinants}). The $K{=}2$ control confirms that all tested binary matrices maintain classical attenuation~\cite{brenner1993}, establishing that the multi-class failure is structurally distinct.
19	
20	\paragraph{Structural guarantee for non-exposure topologies.}
21	Five topologies exhibit zero sign-flip rate (Table~\ref{tab:taxonomy}): confounding, mediation, and front-door show 100\% amplification~\cite{brenner1993, dosemeci1990} but never reverse the sign; collider i
…[truncated 6312 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 1005
}
```

</details>

---


### Tool call

_source line 1624 · 2026-05-23T18:33:45.098102+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1625 · 2026-05-23T18:33:45.450594+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We characterized how multi-class annotation errors interact with causal DAG topology: at $K{\geq}3$, exposure and IV can reverse treatment effect signs while five topologies preserve them. ASVs yield a topology-dependent vulnerability ranking; matrix-based corrections are provably ineffective for four covariate topologies (FWL invariance). Practitioners should identify their topology and compute ASV before selecting corrections.
5	
6	\section*{Limitations}
7	
8	We assume non-differential misclassification (Appendix~\ref{sec:nondiff_stress}). Closed-form expressions assume linear SEMs (logistic robustness: Appendix~\ref{sec:fwl_nonlinear}). Proving general $K{\geq}3$ envelope monotonicity beyond symmetric matrices (Theorem~\ref{thm:k3_symmetric}) remains open~\cite{schennach2020mismeasured}, though rankings are stable across $K{=}3,5,10$; experiments lack end-to-end causal benchmarks.
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 352
}
```

</details>

---


### Tool call

_source line 1626 · 2026-05-23T18:33:45.450986+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "causal_annot_error_attrib",
  "file": "decisions.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "causal_annot_error_attrib",
    "file": "decisions.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1627 · 2026-05-23T18:33:45.552465+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/decisions.yaml\", \"content\": \"_next_id: 21\\ndecisions:\\n- id: D001\\n  date: 2026-05-20 07:25 UTC\\n  summary: MVP PASS — Confounding DAG K=3 理论框架验证通过，进入 research 阶段\\n  rationale: 三项 pass 标准全部满足：(1) 理论预测 vs MC 95% CI 一致 5/5，(2) 所有非差异性 C 产生远离零偏差 0.20-0.30，(3)\\n    二分类折叠偏差与三分类预测显著不同（最大 Δ=0.089）。附加发现：100k 随机 C 矩阵搜索在 confounding DAG 下未发现方向反转——偏差始终与\\n    OVB 同向。这是有价值的 characterization result：confounding DAG 偏差方向可预测（单调），方向反转假设需要在其他\\n    DAG 拓扑（mediator、collider）中验证，属于 research 阶段的核心任务。\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-20 07:30 UTC\\n  summary: Research 阶段第一优先级：exposure misclassification DAG K=3 验证 bias-toward-null\\n    是否在多分类下打破\\n  rationale: Reviewer 指出 MVP criterion 2 在 confounding DAG 下不具区分力（二分类也 pass）。\\\"Bias\\n    toward null\\\" 保证（Bross 1954）特指 exposure 误分类，正确测试需要 exposure DAG（A→Y，用 A* 替代 A）。若\\n    K=3 下此 DAG 出现方向反转或 bias-away-from-null 结构性差异，则 Claim 1 最强形式成立；若不出现，需重新框定核心 claim。\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-20 07:31 UTC\\n  summary: plan_001 完成后设 checkpoint gate：方向反转拓扑数 → framing 版本选择\\n  rationale: 'Reviewer [severity: critical] 指出 plan_001 是存在性检验但无 kill criterion。当前\\n    core insight 依赖方向反转（\\\"binary guarantee breaks\\\"），但 MVP 已证明 confounding DAG 无反转。若\\n    6 拓扑全无反转，framing 需 pivot。三级响应：(A) ≥2 拓扑有反转 → 当前 framing 成立，方向反转为 lead finding；(B)\\n    1 拓扑有反转 → 该拓扑为 lead case，framing 可调整；(C) 0 拓扑有反转 → pivot 到版本 B：\\\"multi-class 偏差\\n    magnitude 不可由 binary 推算 + binarization 本身有害\\\"，方向反转降为 topology-specific finding。注意：0\\n    反转 ≠ 项目 kill——binarization inequality + magnitude unpredictability + ASVs 本身够一篇论文，但\\n    framing 必须诚实。'\\n  related_experiments:\\n  - exp_id: plan_001\\n    role: gate\\n    result: pending\\n  depends_on:\\n  - D001\\n  - D002\\n- id: D004\\n  date: 2026-05-20 07:39 UTC\\n  summary: D003 checkpoint 
…[truncated 10944 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 1628 · 2026-05-23T18:33:55.300914+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 1629 · 2026-05-23T18:33:55.804105+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Measurement error in causal inference.}
5	Foundations appear in \citet{carroll2006, gustafson2004, buonaccorsi2010, bound2001measurement}, with DAG-based formalization by \citet{hernan_cole2009} and \citet{kuroki_pearl2014}. For binary variables, non-differential misclassification biases toward the null~\cite{bross1954misclassification, brenner1993, ogburn_vanderweele2012}, but this fails for polytomous exposures~\cite{dosemeci1990, jurek2005, veirod_laake2001}. Extensions address differential measurement error~\cite{edwards_lessler_naimi2021, imai_yamamoto2010}, endogenous misreporting~\cite{nguimkeu_denteh_tchernis2019}, mismeasured covariates under IPW~\cite{shu_yi2019a, shu_yi2019b}, mediation with mismeasured mediators~\cite{valeri_vanderweele2013}, nonclassical error~\cite{schennach2020mismeasured}, and multiply robust estimation~\cite{wei2025multiply}. All analyze a single DAG topology; ours characterizes how the \emph{same} confusion matrix produces qualitatively different bias across seven topologies.
6	
7	\paragraph{Text classifiers and LLM annotation.}
8	\citet{grimmer2022} and \citet{feder_etal2022} provide foundations for text-as-data and causal inference in NLP. \citet{wood_doughty2018} first applied DAG reasoning to classifier error; \citet{teblunthuis2024} gave the most complete binary treatment ($K{=}2$, four DAGs); \citet{lee_wood_doughty2024} extended to categorical LLM classifiers but covered only confounding. On annotation quality, \citet{gilardi2023chatgpt} and \citet{ziems2024can} document rapid LLM annotator adoption (surveyed by \citealt{tan2024llm}), \citet{baumann2025} found 31\% incorrect conclusions, and \citet{kim_garg2025} showed 60\% error correlation across models~\cite{pangakis_wolken_fasching2023, cheng_mayya_sedoc2024, variance_aware_llm2026, hidden_measurement_error2026}. \citet{audinet2025} benchmark debiasing; \citet{keith_jensen_oconnor2020} survey the landsca
…[truncated 1088 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 503
}
```

</details>

---


### Tool call

_source line 1630 · 2026-05-23T18:33:56.256776+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex",
    "limit": "80"
  }
}
```

</details>

---


### Tool result

_source line 1631 · 2026-05-23T18:33:57.111892+00:00_

1	\section{Proofs of Proposition~\ref{prop:signflip} and Theorem~\ref{thm:monotone}}
2	\label{app:proof}
3	
4	We provide algebraic proofs of sign preservation for the confounding and collider topologies (Proposition~\ref{prop:signflip}(a)--(b)), an explicit counterexample for exposure (Proposition~\ref{prop:signflip}(c)), numerical verification for mediation, M-bias, and front-door (Numerical Verification~1), and the monotonicity proof for confounding (Theorem~\ref{thm:monotone}).
5	Throughout, $A\in\{0,1,\dots,K{-}1\}$ with prior $p_k=P(A{=}k)$, and $C$ is a $K{\times}K$ column-stochastic confusion matrix with $C_{jk}=P(A^*{=}j\mid A{=}k)$.
6	We use category~0 as the reference and let $D_j=\mathbf{1}(A{=}j)$, $D_j^*=\mathbf{1}(A^*{=}j)$ for $j=1,\dots,K{-}1$.
7	
8	\subsection{Notation and Key Identities}
9	\label{app:notation}
10	
11	Under non-differential misclassification, the misclassified moments factor linearly through $C$.
12	Define the population vectors:
13	\begin{align}
14	  q_j &= P(A^*{=}j) = \textstyle\sum_k C_{jk}\,p_k, \label{eq:q}\\
15	  \mathrm{ct}_j &= \mathbb{E}[T\cdot D_j^*] = \textstyle\sum_k C_{jk}\,\mathbb{E}[T\cdot D_k], \label{eq:ct}\\
16	  \mathrm{cy}_j &= \mathbb{E}[Y\cdot D_j^*] = \textstyle\sum_k C_{jk}\,\mathbb{E}[Y\cdot D_k]. \label{eq:cy}
17	\end{align}
18	Write $q = Cp$, $\mathrm{ct} = C\,\mathbb{E}[T\cdot D]$, and $\mathrm{cy} = C\,\mathbb{E}[Y\cdot D]$, where $D=(D_0,\dots,D_{K-1})^\top$.
19	
20	\subsection{Frisch--Waugh--Lovell Decomposition}
21	\label{app:fwl}
22	
23	For topologies where $T$ is directly observed (confounding, mediation, collider, M-bias, front-door), the estimator regresses $Y$ on $Z^*=(1,T,D_1^*,\dots,D_{K-1}^*)$.
24	By the Frisch--Waugh--Lovell (FWL) theorem, the coefficient on $T$ satisfies:
25	\begin{equation}
26	  \operatorname{plim}\hat{\tau}(C)
27	  = \frac{\mathbb{E}[\tilde{T}\,\tilde{Y}]}{\mathbb{E}[\tilde{T}^2]},
28	  \label{eq:fwl}
29	\end{equation}
30	where $\tilde{T}=T-\mathbb{E}[T\mid A^*]$ and $\ti
…[truncated 2331 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 855
}
```

</details>

---


### Tool call

_source line 1632 · 2026-05-23T18:33:57.112327+00:00_

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
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
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

_source line 1633 · 2026-05-23T18:33:57.162725+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1634 · 2026-05-23T18:34:14.093991+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
  "description": "Check if review_issues.yaml exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
    "description": "Check if review_issues.yaml exists"
  }
}
```

</details>

---


### Tool result

_source line 1635 · 2026-05-23T18:34:14.245630+00:00_

&lt;persisted-output>
Output too large (32.5KB). Full output saved to: /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-prod-0510-projects-causal-annot-error-attrib--claude-sessions-review-director-d2e6d7be/7477bbe1-964b-4c8f-88b7-ba741180dfb6/tool-results/bu5983h00.txt

Preview (first 2KB):
issues:
  # === Round 1-7 历史 (resolved，保留摘要) ===

  - id: R1-N1
    category: soundness
    severity: must-fix
    summary: "Theorem 1 适用范围过窄（仅 confounding+proportional effects），K≥3 证明不完整"
    status: resolved
    first_raised_round: 1
    last_seen_round: 7
    resolution: "Theorem 1 现正确限定为 K=2；K≥3 由 Observation 1 和 Conjecture 1 覆盖。"
    resolution_round: 7

  - id: R1-N2
    category: soundness
    severity: should-fix
    summary: "3/5 安全拓扑的符号保持仅有数值验证，Abstract 用 'establish' 暗示已证明"
    status: resolved
    first_raised_round: 1
    last_seen_round: 3
    resolution: "Abstract 已准确区分 prove/verify。"
    resolution_round: 4

  - id: R1-N3
    category: soundness
    severity: must-fix
    summary: "ASV C(δ) 定义域错误"
    status: resolved
    first_raised_round: 1
    last_seen_round: 1
    resolution: "Section 3.3 已引入 δ_max 约束。"
    resolution_round: 2

  - id: R2-N1
    category: presentation
    severity: must-fix
    summary: "83.4% sign reversal headline framing 过度声称"
    status: resolved
    first_raised_round: 1
    last_seen_round: 5
    resolution: "Introduction 已重写。"
    resolution_round: 5

  - id: R2-N2
    category: novelty
    severity: should-fix
    summary: "'first systematic framework' 过度声明"
    status: resolved
    first_raised_round: 1
    last_seen_round: 1
    resolution: "已修复。"
    resolution_round: 2

  - id: R2-N3
    category: related_work
    severity: must-fix
    summary: "4 篇关键相关工作未引用"
    status: resolved
    first_raised_round: 1
    last_seen_round: 1
    resolution: "已修复。"
    resolution_round: 2

  - id: R1-W2
    category: clarity
    severity: should-fix
    summary: "Sign preservation 的 DGP 条件在实践中难以事前验证"
    status: resolved
  
…[truncated 324 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Bash",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 1636 · 2026-05-23T18:34:29.650697+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "causal_annot_error_attrib",
  "review_chat_id": "oc_9f117624057fcf6cb95db4d67f525246"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "causal_annot_error_attrib",
    "review_chat_id": "oc_9f117624057fcf6cb95db4d67f525246"
  }
}
```

</details>

---


### Tool result

_source line 1637 · 2026-05-23T18:34:45.151320+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 15500
}
```

</details>

---


### Tool call

_source line 1638 · 2026-05-23T18:34:45.252629+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "你是 Reviewer 1，负责**方法严谨性**审查。\n\n## 论文信息\n- 标题：Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction\n- 目标 venue：EMNLP 2026 (ARR Long Paper)\n- Deadline：2026-05-25\n- 格式要求：ACL template, 8页正文 + unlimited references, double-blind, anonymous\n- 论文路径：`projects/causal_annot_error_attrib/docs/paper/main.tex`\n- PDF：`/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_20/submitted.pdf`\n\n## 你的审查侧重\n\n**核心任务：评估理论声称与证据之间的匹配度。**\n\n请重点检查：\n\n1. **定理与证明**：\n   - Theorem 1 (K=2 envelope monotonicity) 和 Theorem 2 (K=3 symmetric) 的证明是否完整、正确\n   - Proposition 1 (sign preservation) 的条件是否充分且正确表述\n   - Conjecture 1 (ε-approximate monotonicity) 的数值支撑是否足够\n   - 定理条件（proportional effects, C₀ diagonal ≥ 1/2）是否过于restrictive\n\n2. **实验设计与统计**：\n   - Monte Carlo 验证是否充分（样本量、重复次数）\n   - MAPE 1.6% 的 theory-MC agreement 是否在合理 CI 内\n   - Dirichlet prior 选择是否合适，是否存在 selection bias\n   - ASV bootstrap CI 方法是否正确\n\n3. **核心声称验证**：\n   - \"5 topologies preserve sign, 2 don't\" — 证明 vs 数值验证的区分是否清晰\n   - \"83.4% sign reversal\" 条件（uniform Dirichlet）是否充分说明\n   - FWL invariance argument 是否正确\n   - PPI++ harm for M-bias 的机制解释\n\n4. **数学表述**：\n   - 符号一致性\n   - 方程推导是否可复现\n   - 是否有隐含假设未说明\n\n请按 Strengths → Weaknesses → Questions → Minor Issues 结构输出审稿意见。对每个 weakness 标注严重程度 [Must-Fix] / [Should-Fix] / [Minor]。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "你是 Reviewer 1，负责**方法严谨性**审查。\n\n## 论文信息\n- 标题：Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction\n- 目标 venue：EMNLP 2026 (ARR Long Paper)\n- Deadline：2026-05-25\n- 格式要求：ACL template, 8页正文 + unlimited references, double-blind, anonymous\n- 论文路径：`projects/causal_annot_error_attrib/docs/paper/main.tex`\n- PDF：`/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_20/submitted.pdf`\n\n## 你的审查侧重\n\n**核心任务：评估理论声称与证据之间的匹配度。**\n\n请重点检查：\n\n1. **定理与证明**：\n   - Theorem 1 (K=2 envelope monotonicity) 和 Theorem 2 (K=3 symmetric) 的证明是否完整、正确\n   - Proposition 1 (sign preservation) 的条件是否充分且正确表述\n   - Conjecture 1 (ε-approximate monotonicity) 的数值支撑是否足够\n   - 定理条件（proportional effects, C₀ diagonal ≥ 1/2）是否过于restrictive\n\n2. **实验设计与统计**：\n   - Monte Carlo 验证是否充分（样本量、重复次数）\n   - MAPE 1.6% 的 theory-MC agreement 是否在合理 CI 内\n   - Dirichlet prior 选择是否合适，是否存在 selection bias\n   - ASV bootstrap CI 方法是否正确\n\n3. **核心声称验证**：\n   - \"5 topologies preserve sign, 2 don't\" — 证明 vs 数值验证的区分是否清晰\n   - \"83.4% sign reversal\" 条件（uniform Dirichlet）是否充分说明\n   - FWL invariance argument 是否正确\n   - PPI++ harm for M-bias 的机制解释\n\n4. **数学表述**：\n   - 符号一致性\n   - 方程推导是否可复现\n   - 是否有隐含假设未说明\n\n请按 Strengths → Weaknesses → Questions → Minor Issues 结构输出审稿意见。对每个 weakness 标注严重程度 [Must-Fix] / [Should-Fix] / [Minor]。"
  }
}
```

</details>

---


### Tool result

_source line 1639 · 2026-05-23T18:34:59.776257+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_9f117624057fcf6cb95db4d67f525246:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 14523
}
```

</details>

---


### Tool call

_source line 1640 · 2026-05-23T18:34:59.927844+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "你是 Reviewer 2，负责**新颖性与完整性**审查。\n\n## 论文信息\n- 标题：Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction\n- 目标 venue：EMNLP 2026 (ARR Long Paper)\n- Deadline：2026-05-25\n- 格式要求：ACL template, 8页正文 + unlimited references, double-blind, anonymous\n- 论文路径：`projects/causal_annot_error_attrib/docs/paper/main.tex`\n- PDF：`/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_20/submitted.pdf`\n\n## 你的审查侧重\n\n**核心任务：评估论文的贡献定位、学术完整性和投稿合规性。**\n\n请重点检查：\n\n1. **新颖性与定位**：\n   - 相对于 Teblunthuis (2024, binary K=2 四拓扑)、Lee/Wood-Doughty (2024, 单拓扑 K≥3)、Brenner (1993, binary confounding) 的增量贡献是否足够\n   - \"first multi-class topology-specific analysis\" 这一声称是否过度\n   - ASV 框架相对于 E-values、partial-R²、Oster 的区分度\n\n2. **Related Work 覆盖**：\n   - 是否遗漏重要相关工作（measurement error in causal inference, LLM annotation quality, sensitivity analysis）\n   - 引用是否存在虚构或年份错误\n   - 对 prior work 的定位是否公允\n\n3. **写作与叙事**：\n   - Abstract 是否 ≤200 words（EMNLP 要求）\n   - Introduction 的 claim-evidence 结构是否清晰\n   - 论文整体叙事是否连贯（7 topologies → ASV → correction routing）\n   - 术语使用是否一致\n\n4. **格式合规**（EMNLP 2026 ARR）：\n   - 正文是否 ≤8 页（不含 references 和 limitations）\n   - Limitations section 是否存在且适当\n   - 匿名性：是否有 self-citation leak 或 deanonymizing information\n   - Appendix 结构是否合理\n\n5. **实践价值**：\n   - Algorithm 1 (correction decision procedure) 是否真正可操作\n   - 对 practitioner 的指导是否具体可行\n   - 缺少什么实践验证（end-to-end case study? real causal question?）\n\n请按 Strengths → Weaknesses → Questions → Minor Issues 结构输出审稿意见。对每个 weakness 标注严重程度 [Must-Fix] / [Should-Fix] / [Minor]。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "你是 Reviewer 2，负责**新颖性与完整性**审查。\n\n## 论文信息\n- 标题：Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction\n- 目标 venue：EMNLP 2026 (ARR Long Paper)\n- Deadline：2026-05-25\n- 格式要求：ACL template, 8页正文 + unlimited references, double-blind, anonymous\n- 论文路径：`projects/causal_annot_error_attrib/docs/paper/main.tex`\n- PDF：`/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_round_20/submitted.pdf`\n\n## 你的审查侧重\n\n**核心任务：评估论文的贡献定位、学术完整性和投稿合规性。**\n\n请重点检查：\n\n1. **新颖性与定位**：\n   - 相对于 Teblunthuis (2024, binary K=2 四拓扑)、Lee/Wood-Doughty (2024, 单拓扑 K≥3)、Brenner (1993, binary confounding) 的增量贡献是否足够\n   - \"first multi-class topology-specific analysis\" 这一声称是否过度\n   - ASV 框架相对于 E-values、partial-R²、Oster 的区分度\n\n2. **Related Work 覆盖**：\n   - 是否遗漏重要相关工作（measurement error in causal inference, LLM annotation quality, sensitivity analysis）\n   - 引用是否存在虚构或年份错误\n   - 对 prior work 的定位是否公允\n\n3. **写作与叙事**：\n   - Abstract 是否 ≤200 words（EMNLP 要求）\n   - Introduction 的 claim-evidence 结构是否清晰\n   - 论文整体叙事是否连贯（7 topologies → ASV → correction routing）\n   - 术语使用是否一致\n\n4. **格式合规**（EMNLP 2026 ARR）：\n   - 正文是否 ≤8 页（不含 references 和 limitations）\n   - Limitations section 是否存在且适当\n   - 匿名性：是否有 self-citation leak 或 deanonymizing information\n   - Appendix 结构是否合理\n\n5. **实践价值**：\n   - Algorithm 1 (correction decision procedure) 是否真正可操作\n   - 对 practitioner 的指导是否具体可行\n   - 缺少什么实践验证（end-to-end case study? real causal question?）\n\n请按 Strengths → Weaknesses → Questions → Minor Issues 结构输出审稿意见。对每个 weakness 标注严重程度 [Must-Fix] / [Should-Fix] / [Minor]。"
  }
}
```

</details>

---


### Tool result

_source line 1641 · 2026-05-23T18:35:01.335202+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_9f117624057fcf6cb95db4d67f525246:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1407
}
```

</details>

---


### Assistant

_source line 1642 · 2026-05-23T18:35:14.087590+00:00_

Round 1 已启动：

- 视觉审查 Agent：已派发（fire-and-forget）
- Reviewer 1（方法严谨性）：已分配
- Reviewer 2（新颖性/完整性）：已分配

等待两位 Reviewer 返回初审意见。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 162

## Round 162

2 recorded events


### User

_source line 1643 · 2026-05-23T18:42:53.878116+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 审稿意见：新颖性与完整性

## 论文信息
- **标题**: Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction
- **Venue**: EMNLP 2026 (ARR Long Paper)

---

## 总体评分
**Overall**: 3.5 / 5 (Borderline Conference)
**一句话总结**: 扎实的理论工作，系统覆盖7种DAG拓扑下K≥3误分类偏差，sign reversal发现有价值，但实际NLP应用验证不足，理论局限于线性SEM。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 4 / 5 | 理论推导严谨，100,000次Monte Carlo验证充分，但ASV单调性对一般K未证明（仅K=2, K=3对称有定理），FWL不变性论证清晰 |
| Excitement | 3 / 5 | K≥3 sign reversal是有意义的新发现，ASV框架实用，但整体偏理论，对NLP社区的直接影响需要更多实证桥接 |
| Reproducibility | 4 / 5 | 所有定理有完整证明（Appendix A），数值实验参数明确，Algorithm 1可操作；但代码未公开（匿名审稿可理解） |
| Confidence | 4 / 5 | 熟悉因果推断中的测量误差文献和NLP中的标注质量问题 |

---

## 主要优势

**S1. 系统性覆盖是真正的贡献。** 将K≥3多类别误分类与7种DAG拓扑的交叉分析做到了前所未有的完整度。Teblunthuis et al. (2024, Comm. Methods & Measures) 仅覆盖K=2、4种拓扑；Lee & Wood-Doughty (2024, ACL-FM Workshop) 仅处理单一confounding拓扑。将两个维度同时推广并发现K≥3的质性新现象（sign reversal），这不是简单的笛卡尔积。

**S2. K≥3 sign reversal 发现具有实际意义。** 二元误分类下非差异性误分类"toward the null"的经典结论（Brenner 1993, J Clin Epidemiol 46:57–63 针对polytomous confounders已有警示）在K≥3下被系统性地打破。Section 4.2 (p7) 显示exposure拓扑下83.4%的随机矩阵产生sign reversal，IV拓扑52.6%。这对使用LLM标注进行因果推断的NLP研究者是重要警示。

**S3. FWL不变性负结果有力。** Section 4.4 (p7-8) 和 Appendix B.2 (p22) 证明了4种协变量拓扑（confounding, mediation, collider, M-bias）下矩阵校正方法（Naive plug-in, MLA）无效，因为FWL分解使得校正后的混淆矩阵被约掉。这是一个优雅的负结果，直接改变了practitioner的方法选择。Table 6 (p23) 的OLS vs. logistic对比清晰有力。

**S4. Appendix 深度卓越。** 26页Appendix涵盖完整证明（A.1-A.9）、对抗性验证（A.11, 545,945条曲线）、非差异性压力测试（B.6）、非线性DGP鲁棒性（B.7）、混淆矩阵估计鲁棒性（B.23）等。Table 2 (p21) 的充分条件汇总和Table 21 (p32) 的ASV参数空间分解展示了成熟的理论架构。

**S5. 实证锚定。** 使用HumAID (K=10), VAST (K=3), CivilComments (K=2) 的23组真实LLM混淆矩阵（Section 4.4, p7-8; Figure 5, p22），将理论预测与实际LLM配置对接。Figure 4 (p8) 的topology-determines-bias ranking图直观有效。

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] **缺少端到端因果应用验证**
- 具体位置：Section 4.4 (p7-8), Appendix B.18 (p31)
- 问题：论文声称"Topology-aware analysis is necessary for valid causal inference with LLM-generated annotations"（Abstract最后一句），但没有任何实验真正回答一个因果问题。Section 4.4的empirical validation仅验证理论violation rate预测与真实混淆矩阵匹配；B.18的ClinicalBERT case study展示ASV诊断流程，但只是回顾性地分析已有混淆矩阵，而非前瞻性地在一个真实因果问题上跑完annotate → estimate → correct的全流程。
- 为什么影响接收：对于EMNLP这样的应用导向venue，一个声称"对practitioner有指导意义"的框架需要至少一个端到端demonstration：(1) 选定一个真实的因果问题（如广告对投票行为的影响），(2) 用LLM标注treatment/outcome/confounder，(3) 观察到偏差，(4) 用Algorithm 1选择校正方法，(5) 报告校正前后的ATE差异。没有这一步，practitioner guidance停留在理论层面。
- 建议修改方向：选择一个现有的text-as-treatment数据集（如Egami et al. 2022的政治广告数据），用至少两个LLM标注，走完全流程。即使结果简单（如"校正后ATE从0.15变为0.12"），也比纯理论推导更有说服力。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] **ASV单调性对一般K是猜想而非定理**
- 具体位置：Conjecture 1 (p6), Theorem 2 (p6, 仅K=3对称), Appendix B.12 (p27)
- 问题：ASV框架的核心卖点是"vulnerability ranking from IV to M-bias"，但这依赖于ASV沿C(δ)路径单调递减的性质。对K=2有Theorem 1（精确证明），对K=3有Theorem 2（对称矩阵），但对一般K≥3（非对称）只有Conjecture 1和数值验证（210,000矩阵, ε<0.016, Table 3, p22; B.12的extended conjecture验证）。
- 影响：如果单调性不成立，ASV排序可能在某些K和C配置下失效，削弱实用性。论文在Limitations中承认（p8），但主文的叙事语气过于确定，如"yielding a vulnerability ranking from IV (maximally fragile) to M-bias (immune)"（Abstract）——读者可能误以为这是已证结论。
- 建议：(1) 在Abstract和Section 3.3中明确标注K≥3非对称情况下排序是"empirically robust conjecture"而非已证结论；(2) 讨论可能的反例构造或证明障碍。

**W2** [warning] **理论限于线性SEM，推广讨论不足**
- 具体位置：Section 3.1 (p3), Limitations (p8), Appendix B.7 (p25)
- 问题：所有定理和ASV表达式都建立在线性SEM假设上。B.7测试了logistic回归下的sign-flip率（Table 15, p29），结果显示所有5种协变量拓扑sign-flip为零，exposure拓扑也保持零——这是一个积极的鲁棒性结果。但B.15的FWL breakdown分析（Table 6, p23）也显示logistic回归下FWL不变性不完全成立（bias reduction非零），这意味着线性SEM的核心负结果（矩阵校正无效）在非线性模型下可能不适用。论文对此讨论不足。
- 建议：在主文Section 5或Limitations中增加一段讨论：线性SEM结论在多大程度上推广到非线性模型？FWL不变性在logistic回归下的部分失效是否意味着矩阵校正方法在非线性场景下可能有效？

**W3** [warning] **"first multi-class topology-specific analysis"声称需要更精确的界定**
- 具体位置：Section 1 (p2, "We present the first multi-class (K≥3) topology-specific analysis")
- 问题：Brenner (1993) 已经分析了polytomous confounder的非差异性误分类（虽然仅限confounding拓扑）。Lee & Wood-Doughty (2024) 处理了K≥3的LLM分类器在confounding设定下的误差。Gustafson (2004) 的"Measurement Error and Misclassification"全书覆盖了多类别情况。严格来说，"first"的声称是在"同时覆盖K≥3和多拓扑"这个交叉点上成立的，但论文表述可能让读者误以为之前没有任何K≥3的工作。
- 建议：将"first multi-class topology-specific analysis"改为更精确的表述，如"first systematic analysis that jointly addresses multi-class (K≥3) misclassification across multiple DAG topologies"，并在紧随其后明确prior work各自覆盖的维度。

**W4** [warning] **非差异性误分类假设的讨论应更前置**
- 具体位置：Definition 1 (p3), Appendix B.5 (p24-25), B.6 (p25)
- 问题：非差异性（non-differential）假设要求误分类概率不依赖于Y和其他协变量。但在实际LLM标注中，误分类往往是差异性的：LLM对不同情感倾向的文本有不同的误差率，且误差可能依赖于文本长度、领域等协变量。Appendix B.5验证了12个LLM配置的非差异性（p<0.05, consistent with expected false positive rate），B.6的stress test显示中等程度违反（ε≤0.05）下violation率仍<3 pp。但这些验证都放在附录中，主文仅在p4脚注和Limitations中简短提及。
- 影响：这个假设的强度和可信度是practitioner最关心的问题之一。
- 建议：在主文Method (Section 3.1) 中增加2-3句讨论非差异性假设的实践合理性和验证策略，并引导读者到Appendix B.5-B.6的详细验证。

**W5** [warning] **ASV与现有sensitivity框架的区分度论证不够锐利**
- 具体位置：Section 2 (p3, "Sensitivity analysis and correction methods"), Section 3.3 (p5-6)
- 问题：ASV被定义为"the ε-approximate envelope along C(δ)"（Conjecture 1, p6），这与E-values（VanderWeele & Ding, 2017）在概念上有相似性——两者都将某种"扰动强度"映射到"效果是否被翻转"的阈值。论文说ASV是"analogous to E-values"（p6），但没有深入解释：如果一个practitioner已经在用E-values，ASV额外提供了什么？E-values的target是未观测混淆强度，ASV的target是标注误差强度——这个区别应该更明确地阐述。
- 建议：在Section 3.3开头增加一段"Why not E-values?"的讨论，明确ASV回答的问题（"多大的标注误差会翻转结论？"）与E-values回答的问题（"多强的未观测混淆会翻转结论？"）的本质区别。

---

## 小问题（不影响接收）

**M1** [minor] **Abstract字数可能接近或超过200词上限。** EMNLP 2026要求abstract≤200 words。经估算，当前abstract约190-200词（取决于连字符词的计数方式，如"non-differential"算1词还是2词）。建议作者自行用venue的官方计数工具验证。

**M2** [minor] **Section 4.2 (p7) "Theory-MC agreement" 措辞。** "Analytical probability limits match Monte Carlo estimates with grand MAPE of 1.6% across 161 scenarios"——"grand MAPE"不是标准统计术语，建议改为"mean absolute percentage error (MAPE) averaged across..."

**M3** [minor] **Figure 2 (p5) 信息密度。** 7个小图展示100,000随机矩阵的bias分布，但在正文尺寸下每个子图非常小。建议考虑将最关键的3个拓扑（confounding, exposure, IV）放主文，其余移至appendix。

**M4** [minor] **Appendix B.18 (p31) 脚本路径引用。** 提及"Script: artifacts/exp.fwl.logistic.breakdown.py"——在double-blind审稿中包含具体文件路径无问题，但建议在camera-ready版本中改为引用代码仓库相对路径。

**M5** [minor] **术语一致性。** 主文中"topology"和"DAG topology"交替使用，建议统一。同样，"confusion matrix"有时简写为"C"，有时用全称，在引入简写后应统一。

**M6** [minor] **Limitations section (p8) 长度适当，** 覆盖了三个核心限制（非差异性假设、线性SEM、单调性证明）。符合EMNLP要求。但"experiments lack real end-to-end causal benchmarks"这一点只在最后一句一笔带过，考虑到这是最大的实践缺陷（见N1），值得多一句展开。

**M7** [minor] **Section D (p34) AI辅助声明。** "We used Claude (Anthropic) as an AI coding and writing assistant throughout this work."——声明存在且适当。

---

## Questions for Authors

**Q1.** Algorithm 1 (p34) 的correction routing假设practitioner已知DAG topology和gold-label availability。在实践中，DAG的选择本身就有不确定性。作者是否考虑过在多个候选DAG上运行ASV并报告sensitivity范围？

**Q2.** Table 5 (p23) 的校正方法比较显示MC-SIMEX在多个拓扑上优于PPI++。但MC-SIMEX需要已知（或估计的）混淆矩阵，而PPI++只需要gold labels。在gold labels昂贵时，两者的trade-off如何？

**Q3.** 论文使用线性SEM推导所有结果。如果underlying DGP是非线性的（如logistic），B.7显示sign-flip率为零，但bias magnitude如何变化？是否仍然可以用线性ASV作为近似？

**Q4.** 对于K=10（如HumAID），混淆矩阵有100个参数。在实践中如何可靠地估计这么大的混淆矩阵？B.23 (p32) 的bootstrap分析显示n_gold=500时ASV排序稳定（Spearman ρ≥0.99），但这对K=10是否也成立？

---

## 格式合规检查

| 检查项 | 结果 | 备注 |
|--------|------|------|
| 正文≤8页 | ✅ | 正文结束于p8 Limitations |
| Limitations存在 | ✅ | p8底部，约15行，覆盖3个点 |
| Appendix无Limitations | ✅ | Appendix只有技术内容 |
| Abstract≤200词 | ⚠️ | 边界情况，约190-200词 |
| 匿名性 | ✅ | "Anonymous ACL submission"，无明显self-citation泄露 |
| 单一Limitations section | ✅ | 仅主文p8有一个 |
| AI辅助声明 | ✅ | Section D (p34) |

---

## 总结

这是一篇理论扎实、验证充分的方法论论文，填补了K≥3多类别误分类在因果DAG拓扑中传播效应的分析空白。核心贡献——sign reversal条件、ASV框架、FWL不变性负结果——都有价值。主要不足在于缺少端到端的NLP因果应用验证（N1），以及ASV单调性对一般K未完成证明（W1）。如果N1能通过增加一个真实case study得到解决，论文可达Conference水平；当前状态处于Borderline Conference / Findings之间。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1644 · 2026-05-23T18:43:01.230218+00:00_

Reviewer 2 审稿意见已收到（3.5/5，Borderline Conference）。等待 Reviewer 1 提交后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 163

## Round 163

6 recorded events


### User

_source line 1645 · 2026-05-23T18:43:06.584506+00:00_

[Reviewer 1 审稿意见]:
## 总体评分
**Overall**: 3.5 / 5 — Borderline Conference
**一句话总结**: 对多类标注错误在因果推断中传播的拓扑依赖分析是新颖且重要的，理论在限定条件下正确，数值验证充分，但核心定理的适用范围受 proportional effects 和 symmetric confusion matrix 假设严重限制，且 Conjecture 1 尚无证明，削弱了对一般 K≥3 场景的理论保障。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 4 / 5 | 在所声明的假设条件下，证明正确、数值验证充分（MAPE 1.6%，545,945 adversarial curves）。但两个核心定理的条件较强（proportional effects + symmetric C₀），一般性存在缺口。 |
| Excitement | 3 / 5 | 问题重要且及时（LLM-as-annotator 场景），ASV 框架有实用价值，但论文偏数学/统计方法论，对 EMNLP 受众的直接 NLP 贡献较薄。 |
| Reproducibility | 3.5 / 5 | 实验参数详细（N=10,000，100,000 Dirichlet 矩阵，bootstrap B=1,000），Algorithm 1 可操作，但未提及代码发布。 |
| Reviewer Confidence | 4 / 5 | 我仔细检查了证明结构（Appendix A.4–A.9）、数值验证设计和统计方法。 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] Proportional effects 假设在 Limitations 中完全缺失
- 具体位置：Section 5 Limitations（p.8）；Theorem 1（p.6）；Theorem 2（p.6）；Appendix B.13（Table 14，p.29）
- 问题：两个核心定理（Theorem 1: K=2 monotonicity；Theorem 2: K=3 symmetric monotonicity）均要求 proportional effects（f = λg），但 Limitations 段落只提到了 non-differential misclassification、linear SEMs、symmetric matrices、general K 开放性——唯独没有提及 proportional effects 这一最关键假设的限制性。更重要的是，Appendix B.13 Table 14 显示，在 non-proportional effects 下 OOB rate 高达 84.6%，sign preservation 降至 75.5%，这意味着在大多数非比例效应场景中 Theorem 1 的预测会被违反。主文将这些定理作为核心贡献展示，但未充分警示其实际适用范围。
- 为什么影响接收：这是论文理论贡献的核心假设，不在 Limitations 中讨论会误导读者高估定理的一般性。审稿人和读者可能认为这些 monotonicity 结果普遍成立，而实际上它们在非比例效应下频繁失效。
- 建议修改方向：(1) 在 Limitations 中明确列出 proportional effects 假设及其限制性；(2) 在主文 Section 3.2 引入定理时加一句关于此假设的 practical scope caveat；(3) 引用 Table 14 的数据说明非比例效应下的退化行为。

**N2** [critical] 从 Theorem 1/2 到 Conjecture 1 的理论缺口在主文中表述不清
- 具体位置：Section 3.2（p.6）Theorem 1 → Theorem 2 → Conjecture 1 的叙述流
- 问题：主文将 Theorem 1（K=2）、Theorem 2（K=3 symmetric）、Conjecture 1（general K≥3, ε-approximate）连续呈现，但未清晰区分"已证明"和"数值猜测"的边界。Conjecture 1 依赖 545,945 adversarial curves 的数值验证（最大违反 ε_abs ≤ 0.016），但 adversarial search 的结构类型（near-permutation, block-diagonal, sparse, near-uniform）是手动选择的，无法排除未覆盖的病态结构。读者容易将 Conjecture 1 误读为已证明的定理。
- 为什么影响接收：从 K=2（Theorem 1）到 K=3 symmetric（Theorem 2）到一般 K≥3（Conjecture 1）的递进是论文的核心叙事弧线。如果读者不能清晰识别哪里是证明终点、哪里是数值验证起点，论文的 soundness 判断会受影响。
- 建议修改方向：(1) 在主文中引入 Conjecture 1 时明确标注"analytic proofs end here; the following is supported by numerical evidence only"；(2) 讨论 adversarial search 的覆盖范围限制；(3) 可考虑用 Table 或 Figure 可视化 proof vs. conjecture 的覆盖范围。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] Theorem 2 的 symmetric C₀ 假设在实际 LLM 混淆矩阵中很少成立
- 具体位置：Theorem 2（p.6）；Appendix A.6（p.17）
- 问题：Theorem 2 要求 K=3 confusion matrix C₀ 是对称的（c_jk = ε for all j≠k）。但真实 LLM 混淆矩阵通常是高度不对称的（例如，情感分析中 positive-neutral 混淆远多于 positive-negative）。论文没有讨论对称假设在实际中的合理性，也没有报告 23 个经验 LLM 混淆矩阵中有多少满足或近似满足对称性。
- 建议：量化经验混淆矩阵的对称性偏离程度（如 Frobenius distance to nearest symmetric matrix），并讨论 Theorem 2 对轻微不对称的鲁棒性。

**W2** [warning] 缺乏已知因果效应的端到端验证
- 具体位置：Section 4.4（p.7-8）
- 问题：经验验证使用真实 LLM 混淆矩阵（HumAID K=10, VAST K=3, CivilComments K=2）但在模拟 DGP 上运行。没有任何实验使用已知 ground-truth causal effect 的真实数据集来验证整个 pipeline（LLM annotation → causal estimation → correction）。Section B.18 的 ClinicalBERT case study 是最接近端到端的演示，但仍基于模拟的 confounding DGP。
- 建议：在至少一个数据集上进行端到端验证，或明确讨论为什么当前实验设计足以支撑论文的 practical claims。

**W3** [warning] Non-differential misclassification 假设的脆弱性未在主文充分讨论
- 具体位置：Definition 1（p.3-4）；Appendix B.25（Table 25，p.33）
- 问题：Appendix B.25 的 Y-stratified 验证显示 content-dependent proxies（topic, sentiment）违反 non-differential 假设（p.17 median p-value, 12/12 rejections for topic），这表明当文本特征同时影响 A 的误分类率和 Y 时，核心假设不成立。但主文仅在 Limitations 中一句带过（"We assume non-differential misclassification"），没有讨论违反后的影响。
- 建议：在主文 Section 3.1 或 Limitations 中增加对 differential misclassification 场景的讨论，说明论文结论在此条件下如何退化。

**W4** [warning] Algorithm 1 的阈值缺乏理论依据
- 具体位置：Algorithm 1（p.34）
- 问题：Algorithm 1 的决策阈值（如 PPI++ RMSE reduction ≈ 47.0%, MC-SIMEX ≈ 16.0%）来自特定模拟设置（K=3, Dirichlet matrices, 7 topologies）的经验平均。这些阈值是否对不同的 K、不同的 DGP 参数、不同的样本量稳定？论文没有 sensitivity analysis 来验证算法的鲁棒性。
- 建议：报告 Algorithm 1 在不同 K（如 K=5,10）和不同 DGP 参数下的性能稳定性，或将其更明确地定位为启发式指南。

---

## 小问题（不影响接收）

1. **Figure 2 caption**（p.5）：红色表示 sign reversal 在图中难以快速识别，建议在 caption 中更显著标注颜色含义。

2. **Notation density**（p.3-4, Section 3.1-3.2）：符号引入密度较高（C, C(δ), τ, plim, β_OV, B(C), f, g, λ 等在不到一页内全部出现）。Table 26（p.33）的符号表有帮助但出现太晚，建议在主文早期引用。

3. **Dirichlet(1,1,1) prior framing**（p.5, Figure 2）：83.4% sign reversal 数字来自 uniform Dirichlet，是最坏情况下的结果。论文在后续（p.7 Section 4.2）给出了 realistic accuracy 下的数字（diagonal ≥ 0.7 时 violation rate 13.7%），但 Figure 2 及其 caption 单独看容易给读者留下过于悲观的印象。建议在 Figure 2 caption 中注明 realistic-accuracy 下的对比数字。

4. **ASV 是渐近量**：ASV 基于 probability limit（plim）定义，反映大样本性质。对于有限样本场景，ASV 的指导意义可能与实际偏差有差距。论文没有讨论 finite-sample 修正。

5. **FWL invariance 的方法范围**：主文 Section 4.4 说"matrix-based corrections are provably ineffective for four covariate topologies"，但 Table 5 显示 PPI++（非 matrix-based 方法）在这些拓扑上实现了 53-54% RMSE reduction。建议主文更精确地限定"matrix-based"修饰语，避免读者误以为所有校正方法对这四种拓扑都无效。

---

## 主要优势

1. **问题定义精准且及时**：LLM annotation → causal inference 的误差传播是一个快速增长的实际问题，论文首次系统性地从拓扑角度分析多类误差，填补了 binary-only 分析的空白。

2. **理论-数值协同验证模式优秀**：每个定理/命题都配有 analytic proof + Monte Carlo verification + adversarial testing 的三层验证，theory-MC agreement MAPE 1.6% 令人信服。

3. **FWL invariance insight 新颖且有实践意义**：证明 matrix-based 校正方法对四种 covariate topology 无效（Table 6），这对实践者选择校正策略有直接指导价值。

4. **ASV 框架设计合理**：将 annotation sensitivity 分解为 magnitude/significance/sign-flip 三个维度，类似于 E-values 的推广，比单一标量更具诊断价值。Bootstrap CI（Appendix B.8）提供了不确定性量化。

5. **写作质量高**：34页中信息密度大但组织清晰，主文 8 页内覆盖了核心贡献，附录结构合理（proofs → experiments → supplementary）。

6. **Sign preservation/reversal 的拓扑分类**（Table 1, Table 2）是高度可操作的实践指南，直接告诉从业者哪些 DAG 结构下可以信任 LLM 标注的方向性。

7. **校正方法对比全面**：5 种方法 × 7 种拓扑 × 210 配置 的系统对比（Table 5），附带清晰的推荐层级（Algorithm 1）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 1646 · 2026-05-23T18:43:51.341378+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应：对每个主要观点标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n# Reviewer 2 审稿意见（新颖性与完整性）\n\n## 总体评分：3.5 / 5 (Borderline Conference)\n\n## Must-Fix 问题\n\n**N1** [critical] **缺少端到端因果应用验证**\n- 具体位置：Section 4.4 (p7-8), Appendix B.18 (p31)\n- 问题：论文声称\"Topology-aware analysis is necessary for valid causal inference with LLM-generated annotations\"（Abstract最后一句），但没有任何实验真正回答一个因果问题。Section 4.4的empirical validation仅验证理论violation rate预测与真实混淆矩阵匹配；B.18的ClinicalBERT case study展示ASV诊断流程，但只是回顾性地分析已有混淆矩阵，而非前瞻性地在一个真实因果问题上跑完annotate → estimate → correct的全流程。\n- 为什么影响接收：对于EMNLP这样的应用导向venue，一个声称\"对practitioner有指导意义\"的框架需要至少一个端到端demonstration。\n- 建议修改方向：选择一个现有的text-as-treatment数据集（如Egami et al. 2022的政治广告数据），用至少两个LLM标注，走完全流程。\n\n## Should-Fix 问题\n\n**W1** [warning] ASV单调性对一般K是猜想而非定理\n- Conjecture 1 (p6), Theorem 2 (p6, 仅K=3对称)\n- 对K=2有Theorem 1，对K=3有Theorem 2（对称矩阵），但对一般K≥3只有Conjecture 1和数值验证（545,945 curves, ε<0.017）。\n- 建议：在Abstract和Section 3.3中明确标注K≥3非对称情况下排序是\"empirically robust conjecture\"而非已证结论。\n\n**W2** [warning] 理论限于线性SEM，推广讨论不足\n- 所有定理建立在线性SEM上。B.7测试了logistic回归下sign-flip率为零（积极），但B.15的FWL breakdown显示logistic下FWL不变性不完全成立。\n- 建议：在主文Limitations中讨论线性→非线性推广问题。\n\n**W3** [warning] \"first multi-class topology-specific analysis\"声称需要更精确界定\n- Brenner (1993)已分析polytomous confounder；Lee & Wood-Doughty (2024)处理了K≥3 LLM分类器在confounding下的误差。\n- 建议：改为\"first systematic analysis that jointly addresses multi-class (K≥3) misclassification across multiple DAG topologies\"。\n\n**W4** [warning] 非差异性误分类假设的讨论应更前置\n- B.25的Y-stratified验证内容应部分前置到主文Section 3.1。\n\n**W5** [warning] ASV与E-values的区分度论证不够锐利\n- 两者都将\"扰动强度\"映射到\"效果是否被翻转\"的阈值。建议增加\"Why not E-values?\"讨论。\n\n## 小问题\n- M1: Abstract字数接近200词上限\n- M2: \"grand MAPE\"非标准术语\n- M3: Figure 2信息密度过高\n- M5: 术语一致性（topology vs DAG topology）\n- M6: Limitations中端到端缺失一笔带过\n\n## Questions\n- Q1: 是否考虑在多个候选DAG上运行ASV并报告sensitivity范围？\n- Q2: MC-SIMEX vs PPI++ 在gold labels昂贵时的trade-off？\n- Q3: 非线性DGP下bias magnitude如何变化？线性ASV能否作为近似？\n- Q4: K=10时100参数的混淆矩阵如何可靠估计？\n\n---\n\n请逐条回应上述 Must-Fix、Should-Fix 和 Questions。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应：对每个主要观点标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n# Reviewer 2 审稿意见（新颖性与完整性）\n\n## 总体评分：3.5 / 5 (Borderline Conference)\n\n## Must-Fix 问题\n\n**N1** [critical] **缺少端到端因果应用验证**\n- 具体位置：Section 4.4 (p7-8), Appendix B.18 (p31)\n- 问题：论文声称\"Topology-aware analysis is necessary for valid causal inference with LLM-generated annotations\"（Abstract最后一句），但没有任何实验真正回答一个因果问题。Section 4.4的empirical validation仅验证理论violation rate预测与真实混淆矩阵匹配；B.18的ClinicalBERT case study展示ASV诊断流程，但只是回顾性地分析已有混淆矩阵，而非前瞻性地在一个真实因果问题上跑完annotate → estimate → correct的全流程。\n- 为什么影响接收：对于EMNLP这样的应用导向venue，一个声称\"对practitioner有指导意义\"的框架需要至少一个端到端demonstration。\n- 建议修改方向：选择一个现有的text-as-treatment数据集（如Egami et al. 2022的政治广告数据），用至少两个LLM标注，走完全流程。\n\n## Should-Fix 问题\n\n**W1** [warning] ASV单调性对一般K是猜想而非定理\n- Conjecture 1 (p6), Theorem 2 (p6, 仅K=3对称)\n- 对K=2有Theorem 1，对K=3有Theorem 2（对称矩阵），但对一般K≥3只有Conjecture 1和数值验证（545,945 curves, ε<0.017）。\n- 建议：在Abstract和Section 3.3中明确标注K≥3非对称情况下排序是\"empirically robust conjecture\"而非已证结论。\n\n**W2** [warning] 理论限于线性SEM，推广讨论不足\n- 所有定理建立在线性SEM上。B.7测试了logistic回归下sign-flip率为零（积极），但B.15的FWL breakdown显示logistic下FWL不变性不完全成立。\n- 建议：在主文Limitations中讨论线性→非线性推广问题。\n\n**W3** [warning] \"first multi-class topology-specific analysis\"声称需要更精确界定\n- Brenner (1993)已分析polytomous confounder；Lee & Wood-Doughty (2024)处理了K≥3 LLM分类器在confounding下的误差。\n- 建议：改为\"first systematic analysis that jointly addresses multi-class (K≥3) misclassification across multiple DAG topologies\"。\n\n**W4** [warning] 非差异性误分类假设的讨论应更前置\n- B.25的Y-stratified验证内容应部分前置到主文Section 3.1。\n\n**W5** [warning] ASV与E-values的区分度论证不够锐利\n- 两者都将\"扰动强度\"映射到\"效果是否被翻转\"的阈值。建议增加\"Why not E-values?\"讨论。\n\n## 小问题\n- M1: Abstract字数接近200词上限\n- M2: \"grand MAPE\"非标准术语\n- M3: Figure 2信息密度过高\n- M5: 术语一致性（topology vs DAG topology）\n- M6: Limitations中端到端缺失一笔带过\n\n## Questions\n- Q1: 是否考虑在多个候选DAG上运行ASV并报告sensitivity范围？\n- Q2: MC-SIMEX vs PPI++ 在gold labels昂贵时的trade-off？\n- Q3: 非线性DGP下bias magnitude如何变化？线性ASV能否作为近似？\n- Q4: K=10时100参数的混淆矩阵如何可靠估计？\n\n---\n\n请逐条回应上述 Must-Fix、Should-Fix 和 Questions。"
  }
}
```

</details>

---


### Tool result

_source line 1647 · 2026-05-23T18:44:10.186304+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_9f117624057fcf6cb95db4d67f525246:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 18844
}
```

</details>

---


### Tool call

_source line 1648 · 2026-05-23T18:44:11.240732+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应：对每个主要观点标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n# Reviewer 1 审稿意见（方法严谨性）\n\n## 总体评分：3.5 / 5 (Borderline Conference)\n\n## Must-Fix 问题\n\n**N1** [critical] Proportional effects 假设在 Limitations 中完全缺失\n- Theorem 1（K=2 monotonicity）和 Theorem 2（K=3 symmetric）均要求 proportional effects（f = λg）\n- Limitations 段落只提到了 non-differential misclassification、linear SEMs、symmetric matrices、general K 开放性——唯独没有提及 proportional effects\n- Appendix B.13 Table 14 显示，在 non-proportional effects 下 OOB rate 高达 84.6%，sign preservation 降至 75.5%\n- 建议：在 Limitations 中明确列出 proportional effects 假设及其限制性；在主文 Section 3.2 引入定理时加 scope caveat\n\n**N2** [critical] 从 Theorem 1/2 到 Conjecture 1 的理论缺口在主文中表述不清\n- 主文将 Theorem 1（K=2）→ Theorem 2（K=3 symmetric）→ Conjecture 1（general K≥3, ε-approximate）连续呈现\n- Conjecture 1 依赖 545,945 adversarial curves 的数值验证，但 adversarial search 的结构类型是手动选择的\n- 读者容易将 Conjecture 1 误读为已证明的定理\n- 建议：明确标注\"analytic proofs end here; the following is supported by numerical evidence only\"\n\n## Should-Fix 问题\n\n**W1** [warning] Theorem 2 的 symmetric C₀ 假设在实际 LLM 混淆矩阵中很少成立\n- 真实 LLM 混淆矩阵通常高度不对称\n- 论文没有报告 23 个经验 LLM 混淆矩阵中有多少满足或近似满足对称性\n- 建议：量化经验混淆矩阵的对称性偏离程度\n\n**W2** [warning] 缺乏已知因果效应的端到端验证\n- 经验验证使用真实 LLM 混淆矩阵但在模拟 DGP 上运行\n- 没有使用已知 ground-truth causal effect 的真实数据集验证整个 pipeline\n- 建议：在至少一个数据集上进行端到端验证，或明确讨论为什么当前实验设计足以支撑 practical claims\n\n**W3** [warning] Non-differential misclassification 假设的脆弱性未在主文充分讨论\n- B.25 的 Y-stratified 验证显示 content-dependent proxies 违反 non-differential 假设（12/12 rejections for topic）\n- 但主文仅在 Limitations 中一句带过\n- 建议：在主文 Section 3.1 增加讨论\n\n**W4** [warning] Algorithm 1 的阈值缺乏理论依据\n- 决策阈值来自特定模拟设置（K=3, Dirichlet matrices）的经验平均\n- 未验证对不同 K、DGP 参数、样本量的稳定性\n- 建议：报告 Algorithm 1 在不同 K 下的性能稳定性\n\n## 主要优势\n1. 问题定义精准且及时\n2. 理论-数值协同验证模式优秀（theory-MC MAPE 1.6%）\n3. FWL invariance insight 新颖且有实践意义\n4. ASV 框架设计合理（三维度）\n5. 写作质量高\n6. Sign preservation/reversal 拓扑分类高度可操作\n7. 校正方法对比全面（5×7×210）\n\n## 小问题\n1. Figure 2 caption 颜色含义不明确\n2. Notation density 高\n3. Dirichlet(1,1,1) prior 83.4% 数字容易给人过于悲观印象\n4. ASV 是渐近量，finite-sample 修正未讨论\n5. \"matrix-based corrections provably ineffective\" 需更精确限定修饰语范围\n\n---\n\n请逐条回应上述 Must-Fix、Should-Fix 和小问题。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应：对每个主要观点标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n# Reviewer 1 审稿意见（方法严谨性）\n\n## 总体评分：3.5 / 5 (Borderline Conference)\n\n## Must-Fix 问题\n\n**N1** [critical] Proportional effects 假设在 Limitations 中完全缺失\n- Theorem 1（K=2 monotonicity）和 Theorem 2（K=3 symmetric）均要求 proportional effects（f = λg）\n- Limitations 段落只提到了 non-differential misclassification、linear SEMs、symmetric matrices、general K 开放性——唯独没有提及 proportional effects\n- Appendix B.13 Table 14 显示，在 non-proportional effects 下 OOB rate 高达 84.6%，sign preservation 降至 75.5%\n- 建议：在 Limitations 中明确列出 proportional effects 假设及其限制性；在主文 Section 3.2 引入定理时加 scope caveat\n\n**N2** [critical] 从 Theorem 1/2 到 Conjecture 1 的理论缺口在主文中表述不清\n- 主文将 Theorem 1（K=2）→ Theorem 2（K=3 symmetric）→ Conjecture 1（general K≥3, ε-approximate）连续呈现\n- Conjecture 1 依赖 545,945 adversarial curves 的数值验证，但 adversarial search 的结构类型是手动选择的\n- 读者容易将 Conjecture 1 误读为已证明的定理\n- 建议：明确标注\"analytic proofs end here; the following is supported by numerical evidence only\"\n\n## Should-Fix 问题\n\n**W1** [warning] Theorem 2 的 symmetric C₀ 假设在实际 LLM 混淆矩阵中很少成立\n- 真实 LLM 混淆矩阵通常高度不对称\n- 论文没有报告 23 个经验 LLM 混淆矩阵中有多少满足或近似满足对称性\n- 建议：量化经验混淆矩阵的对称性偏离程度\n\n**W2** [warning] 缺乏已知因果效应的端到端验证\n- 经验验证使用真实 LLM 混淆矩阵但在模拟 DGP 上运行\n- 没有使用已知 ground-truth causal effect 的真实数据集验证整个 pipeline\n- 建议：在至少一个数据集上进行端到端验证，或明确讨论为什么当前实验设计足以支撑 practical claims\n\n**W3** [warning] Non-differential misclassification 假设的脆弱性未在主文充分讨论\n- B.25 的 Y-stratified 验证显示 content-dependent proxies 违反 non-differential 假设（12/12 rejections for topic）\n- 但主文仅在 Limitations 中一句带过\n- 建议：在主文 Section 3.1 增加讨论\n\n**W4** [warning] Algorithm 1 的阈值缺乏理论依据\n- 决策阈值来自特定模拟设置（K=3, Dirichlet matrices）的经验平均\n- 未验证对不同 K、DGP 参数、样本量的稳定性\n- 建议：报告 Algorithm 1 在不同 K 下的性能稳定性\n\n## 主要优势\n1. 问题定义精准且及时\n2. 理论-数值协同验证模式优秀（theory-MC MAPE 1.6%）\n3. FWL invariance insight 新颖且有实践意义\n4. ASV 框架设计合理（三维度）\n5. 写作质量高\n6. Sign preservation/reversal 拓扑分类高度可操作\n7. 校正方法对比全面（5×7×210）\n\n## 小问题\n1. Figure 2 caption 颜色含义不明确\n2. Notation density 高\n3. Dirichlet(1,1,1) prior 83.4% 数字容易给人过于悲观印象\n4. ASV 是渐近量，finite-sample 修正未讨论\n5. \"matrix-based corrections provably ineffective\" 需更精确限定修饰语范围\n\n---\n\n请逐条回应上述 Must-Fix、Should-Fix 和小问题。"
  }
}
```

</details>

---


### Tool result

_source line 1649 · 2026-05-23T18:44:12.548214+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_9f117624057fcf6cb95db4d67f525246:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1307
}
```

</details>

---


### Assistant

_source line 1650 · 2026-05-23T18:44:15.783493+00:00_

交叉分享已发出，等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director"
}
```

</details>

---


## Round 164

## Round 164

20 recorded events


### User

_source line 1651 · 2026-05-23T18:44:16.882666+00:00_

[Reviewer 2 审稿结果]:
Reviewer 2 审稿完成。

**总评：3.5 / 5（Borderline Conference）**

核心判断：
- **1个 Must-Fix**：缺少端到端 NLP 因果应用验证（N1）——论文声称对 practitioner 有指导意义，但没有任何实验真正回答一个因果问题，从 LLM 标注到因果估计到校正的全流程未展示
- **5个 Should-Fix**：ASV 单调性对一般 K 未证明（W1）、线性 SEM 推广讨论不足（W2）、"first" 声称需更精确界定（W3）、非差异性假设讨论应前置（W4）、ASV 与 E-values 区分度不够锐利（W5）
- **主要优势**：K≥3 sign reversal 发现有实际价值、FWL 不变性负结果优雅、26 页 Appendix 验证充分、真实 LLM 混淆矩阵锚定理论

意见已通过 `review_reviewer_post_to_director` 提交。

---

[Reviewer 1 审稿结果]:
审稿完成。总结：

**Overall: 3.5 / 5（Borderline Conference）**

核心评价：论文对多类标注错误在 7 种 DAG 拓扑下的因果推断偏差传播进行了系统性分析，理论在限定条件下正确，数值验证充分（MAPE 1.6%，545,945 adversarial curves）。

**2 个 Must-Fix**：
- **N1**: Proportional effects 假设是两个核心定理的关键前提，但 Limitations 中完全缺失。Appendix B.13 显示非比例效应下 OOB rate 达 84.6%。
- **N2**: 从 Theorem 1/2（已证明）到 Conjecture 1（数值猜测）的边界在主文中模糊，读者容易将猜想误读为定理。

**4 个 Should-Fix**：Theorem 2 symmetric C₀ 假设的实际合理性（W1）、缺乏 ground-truth 因果效应的端到端验证（W2）、non-differential 假设脆弱性未充分讨论（W3）、Algorithm 1 阈值缺乏理论依据（W4）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1652 · 2026-05-23T18:44:39.891632+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "causal_annot_error_attrib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "causal_annot_error_attrib"
  }
}
```

</details>

---


### Tool result

_source line 1653 · 2026-05-23T18:44:40.042586+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-23T18:34:33.188468+00:00\", \"completed_at\": \"2026-05-23T18:39:21.241246+00:00\", \"findings\": [{\"severity\": \"warning\", \"dimension\": \"page 1-2\", \"message\": \"前两页连续纯文本（Title + Abstract + Introduction），无任何 display item。第一个视觉锚点（Figure 1: 七种 DAG 拓扑图）到第 3 页才出现。审稿人打开论文后前 2 分钟只看到密集文字，无法快速建立视觉认知锚点。建议考虑将 Figure 1 提前到第 2 页（如 Introduction 末尾或 Section 2 开头处引用时就近放置）。\"}, {\"severity\": \"info\", \"dimension\": \"page 1\", \"message\": \"Title / Author / Abstract 排版整洁，符合 ACL 匿名投稿格式。Abstract 长度适中。首页视觉印象专业。\"}, {\"severity\": \"info\", \"dimension\": \"page 3\", \"message\": \"Figure 1（七种 canonical DAG 拓扑，figure* 全宽）作为第一个 display item，有效传达论文核心结构框架。Caption 自包含，仅看图+说明文字即可理解拓扑分类。DAG 内的节点标签（A, A*, X, Y）字号偏小但可读。\"}, {\"severity\": \"info\", \"dimension\": \"page 5\", \"message\": \"Figure 2（bias distribution 直方图面板，figure* 全宽）：红色标记 sign reversal，蓝色为正常分布，颜色对比清晰。各子图标题和轴标签字号较小（约正文 60%），在打印版上可能需要近距离才能阅读。Caption 自包含且信息量充足。\"}, {\"severity\": \"warning\", \"dimension\": \"page 4-6\", \"message\": \"页 4（Method 定义/公式）和页 6（Theorem 1, 2 + Conjecture 1）均为纯文本/公式页，中间仅 page 5 有 Figure 2 打破节奏。三页中仅一个 display item，理论密度高但视觉节奏略显单调。不过考虑到这是理论推导核心区域（定义→定理→推论），属于可接受的例外。\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Table 1 + Figure 3 同页出现，视觉密度良好。Table 1 使用 booktabs 风格（无竖线，toprule/midrule/bottomrule），格式专业。Figure 3（ASV vulnerability ranking）清晰可读。\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"Figure 4（topology determines bias）+ Section 5 Conclusion + Limitations 在同一页，空间利用充分。正文恰好 8 页，符合 EMNLP 2026 长文限制。Limitations 简洁覆盖 3 个关键点，符合要求。\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"主文共 4 个 display items（3 figures + 1 table）across 8 页 = 0.5/页。对于理论+实证混合型论文偏低端但可接受。附录中有大量补充 tables/figures 弥补。\"}, {\"severity\": \"info\", \"dimension\": \"page 5\", \"message\": \"Figure 2 的子图面板较多（7 个拓扑 × 多组参数），单个子图尺寸紧凑。建议检查 300dpi 打印版下轴标签是否清晰可读。\"}, {\"severity\": \
…[truncated 1358 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 1654 · 2026-05-23T18:44:40.042986+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "causal_annot_error_attrib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "causal_annot_error_attrib"
  }
}
```

</details>

---


### Tool result

_source line 1655 · 2026-05-23T18:44:40.093546+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1656 · 2026-05-23T18:44:49.426472+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_issues.yaml",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_issues.yaml",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 1657 · 2026-05-23T18:44:49.577635+00:00_

1	issues:
2	  # === Round 1-7 历史 (resolved，保留摘要) ===
3	
4	  - id: R1-N1
5	    category: soundness
6	    severity: must-fix
7	    summary: "Theorem 1 适用范围过窄（仅 confounding+proportional effects），K≥3 证明不完整"
8	    status: resolved
9	    first_raised_round: 1
10	    last_seen_round: 7
11	    resolution: "Theorem 1 现正确限定为 K=2；K≥3 由 Observation 1 和 Conjecture 1 覆盖。"
12	    resolution_round: 7
13	
14	  - id: R1-N2
15	    category: soundness
16	    severity: should-fix
17	    summary: "3/5 安全拓扑的符号保持仅有数值验证，Abstract 用 'establish' 暗示已证明"
18	    status: resolved
19	    first_raised_round: 1
20	    last_seen_round: 3
21	    resolution: "Abstract 已准确区分 prove/verify。"
22	    resolution_round: 4
23	
24	  - id: R1-N3
25	    category: soundness
26	    severity: must-fix
27	    summary: "ASV C(δ) 定义域错误"
28	    status: resolved
29	    first_raised_round: 1
30	    last_seen_round: 1
31	    resolution: "Section 3.3 已引入 δ_max 约束。"
32	    resolution_round: 2
33	
34	  - id: R2-N1
35	    category: presentation
36	    severity: must-fix
37	    summary: "83.4% sign reversal headline framing 过度声称"
38	    status: resolved
39	    first_raised_round: 1
40	    last_seen_round: 5
41	    resolution: "Introduction 已重写。"
42	    resolution_round: 5
43	
44	  - id: R2-N2
45	    category: novelty
46	    severity: should-fix
47	    summary: "'first systematic framework' 过度声明"
48	    status: resolved
49	    first_raised_round: 1
50	    last_seen_round: 1
51	    resolution: "已修复。"
52	    resolution_round: 2
53	
54	  - id: R2-N3
55	    category: related_work
56	    severity: must-fix
57	    summary: "4 篇关键相关工作未引用"
58	    status: resolved
59	    first_raised_round: 1
60	    last_seen_round: 1
61	    resolution: "已修复。"
62	    resolution_round: 2
63	
64	  - id: R1-W2
65	    category: clarity
66	    severity: should-fix
67	    summary: "Sign preservation 的 DGP 条件在实践中难以事前验证"
68	    status: resolved
69	    first_raised_round: 1
70	    last_seen_round: 2
71	    resolution: "Section 3.2 已添加 ASV 替代讨论。"
72	    resolution_
…[truncated 3867 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 1658 · 2026-05-23T18:44:53.548020+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_issues.yaml",
  "offset": "200",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_issues.yaml",
    "offset": "200",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 1659 · 2026-05-23T18:44:53.699734+00:00_

200	    first_raised_round: 2
201	    last_seen_round: 2
202	    resolution: "210,000 matrices + adversarial + analytic plim。"
203	    resolution_round: 3
204	
205	  - id: R3-NEW-1
206	    category: format
207	    severity: must-fix
208	    summary: "正文超出 EMNLP 2026 Long Paper 8 页限制"
209	    status: resolved
210	    first_raised_round: 3
211	    last_seen_round: 19
212	    mentions:
213	      - round: 12
214	        reviewers: [R1, R2]
215	        note: "R12 再提。"
216	      - round: 13
217	        reviewers: []
218	        note: "已修复。"
219	      - round: 18
220	        reviewers: [R1, R2]
221	        note: "R18 复发，R18 fix 完成。"
222	      - round: 19
223	        reviewers: []
224	        note: "R19 PDF 确认 Conclusion+Limitations 在 page 8，References 从 page 8 开始，Appendix 从更后面。8 页限制已满足。"
225	    resolution: "R18 压缩后编译验证 main text ≤8 pages。R19 PDF 确认合规。连续两轮无复发。"
226	    resolution_round: 19
227	
228	  - id: R3-NEW-2
229	    category: soundness
230	    severity: should-fix
231	    summary: "FWL invariance 结论缺乏 precise statement 和推导"
232	    status: resolved
233	    first_raised_round: 3
234	    last_seen_round: 5
235	    resolution: "FWL 证明完整。"
236	    resolution_round: 5
237	
238	  - id: R3-NEW-3
239	    category: scope
240	    severity: should-fix
241	    summary: "缺少 outcome misclassification 讨论"
242	    status: resolved
243	    first_raised_round: 3
244	    last_seen_round: 5
245	    resolution: "Limitations 已添加。"
246	    resolution_round: 4
247	
248	  - id: R3-NEW-4
249	    category: presentation
250	    severity: should-fix
251	    summary: "Abstract/Introduction 信息过载（数字密度）"
252	    status: in_progress
253	    first_raised_round: 3
254	    last_seen_round: 19
255	    mentions:
256	      - round: 17
257	        reviewers: [R1, R2]
258	        note: "R17 与 R17-N1 联合。"
259	      - round: 18
260	        reviewers: [R2]
261	        note: "R18 共识 minor。"
262	      - round: 19
263	        reviewers: [R2]
264	        note: "R19 R2 再提（Abstract 187 words 合规，但 7+ 数字密度高）。R1 未单独提出。
…[truncated 3867 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 1660 · 2026-05-23T18:44:58.275686+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_issues.yaml",
  "offset": "398",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_issues.yaml",
    "offset": "398",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 1661 · 2026-05-23T18:44:58.276182+00:00_

398	  - id: R5-N3
399	    category: presentation
400	    severity: must-fix
401	    summary: "'Primary coefficient never reverses' 仅为经验发现，缺乏理论保证"
402	    status: resolved
403	    first_raised_round: 5
404	    last_seen_round: 11
405	    resolution: "Abstract 已改为经验事实描述。"
406	    resolution_round: 11
407	
408	  - id: R5-MR
409	    category: related_work
410	    severity: should-fix
411	    summary: "Round 5 新发现的缺失引用"
412	    status: resolved
413	    first_raised_round: 5
414	    last_seen_round: 5
415	    resolution: "三篇引用已添加。"
416	    resolution_round: 5
417	
418	  - id: R6-M1
419	    category: soundness
420	    severity: should-fix
421	    summary: "Theorem 1 对 K≥3 未证明但标记为 Theorem"
422	    status: resolved
423	    first_raised_round: 6
424	    last_seen_round: 7
425	    resolution: "Theorem 1 现正确限定为 K=2。"
426	    resolution_round: 7
427	
428	  - id: R6-M3
429	    category: soundness
430	    severity: should-fix
431	    summary: "Proportional effects 假设 (f=λg) 在 NLP 中是强限制"
432	    status: in_progress
433	    first_raised_round: 6
434	    last_seen_round: 19
435	    mentions:
436	      - round: 17
437	        reviewers: [R1, R2]
438	        note: "R17 共识 should-fix。"
439	      - round: 18
440	        reviewers: [R1, R2]
441	        note: "R18 fix: 增加 stance detection/sentiment analysis 场景讨论 + 97.3% empirical compliance。"
442	      - round: 19
443	        reviewers: [R1, R2]
444	        note: "R19 两位 Reviewer 再提。R1: f,g 不可观测，97.3% 检验方法和标准不透明，OOB 率 23%。R2: 同意，补充 97.3% 可能仅指单一 DGP 配置下 23 个 LLM 中的比例。共识 should-fix（高优先级）。"
445	    action_items:
446	      - round: 19
447	        action: "SF-2 fix: 97.3% wording corrected to distinguish proportional (100% sign preservation) vs non-proportional (97.3% sign preservation rate across 23 empirical LLM confusion matrices)"
448	        assigned_to: paper_agent
449	        status: done
450	    resolution: ""
451	    resolution_round: null
452	
453	  - id: R6-M4
454	    category: presentation
455	    severity: must-fix
456	    summary:
…[truncated 5116 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1662 · 2026-05-23T18:45:04.559319+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_issues.yaml",
  "offset": "597",
  "limit": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_issues.yaml",
    "offset": "597",
    "limit": "150"
  }
}
```

</details>

---


### Tool result

_source line 1663 · 2026-05-23T18:45:04.711273+00:00_

597	        action: "SF-5 fix: introduction.tex 改为 'first multi-class (K≥3) topology-specific analysis'"
598	        assigned_to: paper_agent
599	        status: done
600	    resolution: ""
601	    resolution_round: null
602	
603	  - id: R9-S3
604	    category: experiments
605	    severity: should-fix
606	    summary: "LLM 配置多样性有限（缺 <7B, >70B, ordinal）"
607	    status: in_progress
608	    first_raised_round: 9
609	    last_seen_round: 19
610	    mentions:
611	      - round: 17
612	        reviewers: [R1, R2]
613	        note: "合并到 R1-W3。"
614	      - round: 19
615	        reviewers: []
616	        note: "合并到 R1-W3。R19 未单独提出。"
617	
618	  - id: R11-W2
619	    category: presentation
620	    severity: should-fix
621	    summary: "Section 3.1 缺少 Notation roadmap——plim/FWL 对 NLP 读者不友好"
622	    status: in_progress
623	    first_raised_round: 11
624	    last_seen_round: 19
625	    mentions:
626	      - round: 17
627	        reviewers: [R1, R2]
628	        note: "R17 should-fix（高优先级）。"
629	      - round: 18
630	        reviewers: [R1, R2]
631	        note: "R18 fix: column-stochastic 括号说明已加入。"
632	      - round: 19
633	        reviewers: [R1, R2]
634	        note: "R19 R2-W5 再提（plim, FWL, Wald, column-stochastic polytope 对 NLP 读者不友好）。R1 同意。plim 有脚注但其他术语处理不一致。共识 minor。"
635	    action_items:
636	      - round: 19
637	        action: "SF-7 fix: FWL, Wald inline explanations added in method.tex"
638	        assigned_to: paper_agent
639	        status: done
640	    resolution: ""
641	    resolution_round: null
642	
643	  - id: R11-W4
644	    category: presentation
645	    severity: minor
646	    summary: "IV 52.6% denominator sign change 的 NLP 实践含义未讨论"
647	    status: resolved
648	    first_raised_round: 11
649	    last_seen_round: 19
650	    mentions:
651	      - round: 17
652	        reviewers: []
653	        note: "R17 未提出。"
654	      - round: 18
655	        reviewers: []
656	        note: "R18 未提出。"
657	      - round: 19
658	        reviewers: []
659	        note: "R19 未提出。连
…[truncated 2629 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 1664 · 2026-05-23T18:45:08.533709+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_issues.yaml",
  "offset": "745",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_issues.yaml",
    "offset": "745",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 1665 · 2026-05-23T18:45:08.584403+00:00_

745	    category: presentation
746	    severity: should-fix
747	    summary: "2.1% sign reversal 限定不清晰——secondary coefficient 还是 primary coefficient？"
748	    status: in_progress
749	    first_raised_round: 16
750	    last_seen_round: 19
751	    mentions:
752	      - round: 17
753	        reviewers: [R1, R2]
754	        note: "共识 should-fix。"
755	      - round: 18
756	        reviewers: []
757	        note: "R18 未单独提出。"
758	      - round: 19
759	        reviewers: [R1]
760	        note: "R19 R1-N2 从不同角度再提：2.1% 的统计功效存疑（采样方法不透明）。R2 交叉 AGREE with clarification（附录用 truncated sampling 但主文未说明）。共识 major。"
761	    action_items:
762	      - round: 19
763	        action: "Q5 fix: primary coefficient hedge added in introduction.tex; R19-N1/SF-1: sampling method note '(100,000 Dirichlet-truncated matrices per diagonal threshold; Appendix B.17)' added in experiments.tex"
764	        assigned_to: paper_agent
765	        status: done
766	
767	  - id: R16-N2
768	    category: presentation
769	    severity: should-fix
770	    summary: "Correction guidance 深度不足——作为三大贡献之一，Section 4.5 仅半页"
771	    status: in_progress
772	    first_raised_round: 16
773	    last_seen_round: 19
774	    mentions:
775	      - round: 17
776	        reviewers: [R1, R2]
777	        note: "R17 should-fix（高优先级）。"
778	      - round: 18
779	        reviewers: [R1, R2]
780	        note: "R18 fix: Contribution 3 reframed。"
781	      - round: 19
782	        reviewers: [R1, R2]
783	        note: "R19 R2-N2 再提：FWL invariance 是 FWL 定理直接推论，不足以支撑独立贡献。R1 交叉 AGREE with qualification：FWL 本身 trivial，但 Algorithm 1 + 经验比较有附加价值。共识：FWL 降为 Observation，Contribution 3 重聚焦于 correction routing 实证发现。"
784	    action_items:
785	      - round: 19
786	        action: "Contribution 3 restructured: FWL downgraded to Observation in experiments.tex (L82); introduction.tex Contribution 3 rewritten as 'Topology-aware correction routing' with PPI++ M-bias -88% and MC-SIMEX front-door -62.4% examples."
787	        assigned_to: paper_agent
788	   
…[truncated 2017 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9f117624057fcf6cb95db4d67f525246:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---
