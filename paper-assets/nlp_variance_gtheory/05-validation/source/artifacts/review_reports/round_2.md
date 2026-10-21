---
round: 2
review_mode: fresh
overall_score: 3.5
timestamp: 2026-05-22T08:31:49.401322+00:00
reviewer_ids: ['1', '2', '3']
cross_response_reviewer_ids: ['1', '2', '3']
force_resubmit: False
---


# 审稿报告 — Round 3 (Fresh Review)

**论文**: Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Analysis
**Venue**: EMNLP 2026 (ARR)
**ARR 提交截止**: 2026-05-25（距今 3 天）
**审稿模式**: Fresh（重新审稿）
**Reviewer 编排**: R1（方法严谨性+实验设计）、R2（新颖性+完整性）、R3（独立交叉判断）
**交叉轮次**: 1 轮（初审 + 交叉回应，共识充分，未进第二轮）

---

## Summary

本文将 Generalizability theory (G-theory) 应用于 LLM 评估的多因素方差分解，在 8 个 7-9B 参数开源模型上跨 5 个 benchmark（3 MC + 2 FF）、7 个 facet、共 230 万条记录进行了全交叉设计实验。核心发现：(1) MC benchmark 上 item-related variance (item + model×item DIF) 集中于 68-72%，FF benchmark 分散至 31-41%（"format-associated pattern"）；(2) 多因素设计比单条件设计节省 10× items 达到 G≥0.80；(3) BF16/FP16 在二值评分下功能等价。论文承诺发布 G-theory pipeline 和 D-study 预算计算器。

---

## Strengths

**S1** [三位共识] 实验规模领先——2.3M records、8 模型×5 benchmark×7 facet 的全交叉设计是该领域最大规模 factorial 实验，远超 Messing (2026) 的单 benchmark 设计。

**S2** [三位共识] 二值数据假设的四重验证（simulation, GLMM, accuracy-range stability, Henderson Method I estimator guarantee）在同类文献中属最完善。

**S3** [三位共识] 6 项 robustness checks 系统全面（estimator comparison, CI method, facet specification, LOMO, null calibration, reduced crossing），每项含关键数字。

**S4** [三位共识] Generation-based scoring 避免 log-likelihood 偏差，设计选择有文献支撑（Hua et al., 2025）。

**S5** [三位共识] D-study budget calculator 有直接实用价值。

**S6** [三位共识] 与 Messing (2026) 的差异化定位清晰（fixing judge, multi-benchmark, infrastructure facets）。

**S7** [R3] MMLU subject-level difficulty dispersion 分析（ρ=0.806, p=0.005）为 format-associated pattern 提供了可解释机制。

**S8** [R1] Precision separability 确认性结果对实践有清晰指导。

---

## Weaknesses

### Must-Fix（影响接收决定）

**N1** [三位共识, Critical] **AAAI 2026 模板——Desk Reject 风险**
- main.tex L1-7 使用 `\usepackage[submission]{aaai2026}`，投 EMNLP 2026 (ARR) 必须使用 ACL 模板。字体、margin、section numbering 全部不符。AAAI 排版密度高于 ACL，转换后可能超 8 页限制。
- **必须替换为 ACL 模板并重编译验证 ≤8 页**。

**N2** [三位共识, Critical] **"Format-associated variance pattern" 统计支撑根本不足**
- Permutation test p=0.10 是 n=5、C(5,3)=10 的理论最小 p 值——即使格式效应无穷大也不可能得到 p<0.05。
- Cohen's d=1.73 的 95% CI 约 [-1.93, 5.39]（R3 独立核算），大幅跨越零效应。论文未报告 d 的 CI。
- **R3 新发现**: Mean difference CI [11.44, 21.02] 基于 item-level bootstrap，捕获 item 采样不确定性而非 benchmark 采样不确定性。论文未区分这两个层次的推断。
- 该 claim 贯穿全文，是论文核心，但统计基础薄弱。
- **建议**：(1) 将 "is format-associated" 降级为 "we observe a format-associated pattern across five benchmarks"；(2) 明确区分 item-level CI 和 benchmark-level 推断局限；(3) 报告 Cohen's d bootstrap CI；(4) Limitations 新增 benchmark 样本量限制讨论。

### Should-Fix（影响评分）

**W1** [R1 Critical → R3 Should-Fix, 最终判定 Should-Fix] **"Item-related variance 68-72%" bundling 表述有误导风险**
- σ²_p + σ²_pM 的 bundling 在 G-theory 中方法论合理（Brennan 2001, Ch.4: DIF 是 relative error variance 组成部分）。R3 确认了方法论正当性。
- 但 headline 表述让不熟悉 G-theory 的读者高估 item selection alone 的解释力——unbundled item-only 37.9% vs bundled 68.1%，约一半来自 model×item 交互。
- R1 列 Critical（夸大 item 主导），R2 AGREE Critical，R3 降为 Should-Fix（方法论合理但需透明化）。
- **建议**: 首次使用时注明拆分构成（"item-related variance (item 37.9% + model×item DIF 30.2% = 68.1%)"）；考虑 Table 3 同时报告 unbundled 视角。

**W2** [三位共识] **Model-as-facet 外部效度受限** — 8 个 7-9B instruction-tuned 模型为 purposive selection，LOMO 仅证内部一致性。R3 补充：70B+ 可能 ceiling effects 压缩 item variance；API models infrastructure 完全不同；base models DIF 模式可能不同。Scale validation 仅 Qwen 3B/7B，标题应改 "Preliminary Scale Check"。

**W3** [三位共识] **Ordering facet 在 4/5 benchmark 结构性为零** — "seven facets across five benchmarks" 误导。改为 "up to seven facets" 或注明 ordering 仅适用 MMLU。

**W4** [三位共识] **MATH/GSM8K 残差方差 (43.9%/39.9%) 未讨论来源** — R3 列举可能来源：CoT 路径多样性、生成长度变异、answer extraction noise、未建模高阶交互。至少讨论 1-2 个假设。

**W5** [三位共识] **D-study "10× fewer items" 缺总推理成本对比** — 55 items × 1,296 conditions = 71,280 次推理 vs 552 × 1 = 552 次，总计算成本高 **129×**（R3 独立验证）。"10× fewer items" 技术正确但实践上误导。建议 Table 4 增加 total evaluations 列；Contribution 2 措辞从 "10× fewer items" 转向 "format-dependent efficiency gap"。

**W6** [R2 首提, R1/R3 同意降级] **遗漏重要相关工作** — ATLAS (Li et al., 2025; ICLR 2026) 自适应测试 30-78 items；MetaBench (Kipnis et al., ICLR 2025) 6 benchmark 压缩至 <3% items；Waldis et al. (2024)。R1/R3 均判定 Should-Fix（现有 IRT/compression 定位框架足够）。补充引用并增加定位说明。

**W7** [R1 首提, R2 AGREE] **IRT baseline 对比不公平** — Table 4 将 IRT items G=0.457 与 multi-facet 并列暗示 IRT 劣势，但低 G 完全来自 single-condition protocol。建议增加 "IRT items + multi-facet" 行。

**W8** [R1 首提, R2 Partial REBUT] **ρ=0.732 二值模拟 framing 偏乐观** — 定性结论稳健（item_id 在 100 次模拟保持 dominant），但需补充 top-3 分量排序一致率。

**W9** [三位共识] **代码/数据可用性声明缺失** — Contribution 4 承诺 toolkit 但无 URL/匿名链接。

---

## Reviewer Consensus

三位 Reviewer 完全一致 [AGREE] 的问题：
1. **模板错误**（N1）：desk reject 级别
2. **p=0.10 统计效力不足**（N2）：核心 claim 最大弱点
3. **Model facet 外部效度和 scale validation 受限**（W2）
4. **Ordering facet 描述不精确**（W3）
5. **Residual variance 未讨论**（W4）
6. **总推理成本缺失**（W5）
7. **代码/数据缺失**（W9）

## Reviewer Divergence

1. **Item-related variance bundling 严重性**:
   - R1: Critical（夸大 item 主导地位，headline 依赖定义选择）
   - R2: AGREE Critical
   - R3: Should-Fix（方法论合理，仅需透明化表述）
   → **最终判定: Should-Fix**。G-theory 框架内 bundling 有方法论依据，但需在首次使用时注明拆分构成。

2. **遗漏相关工作严重性**:
   - R2: Critical
   - R1: Should-Fix
   - R3: Should-Fix
   → **最终判定: Should-Fix**（2:1 多数）。

3. **10× efficiency gain 新颖性**:
   - R2/R3: G-theory 标准功能，新颖性有限
   - R1: format-dependent ratio (MC 12× vs FF 21×) 有经验价值
   → 建议 reframe contribution 为 format-dependent efficiency gap。

4. **Excitement 评分**:
   - R1: 3.5/5
   - R2: 3.0/5
   - R3: 3.0/5
   → 综合 3.0/5。R1 认为与 Messing (2026) 有本质区别；R2/R3 认为主要为增量扩展。

5. **Overall 评分**:
   - R1: 3.5 (Borderline Conference)
   - R2: 3.5 (Borderline Conference)
   - R3: 3.0 (Findings)

---

## Questions

1. 若将 σ²_pM 从 "item-related" 中拆出，format-associated pattern 的无重叠结论是否仍然成立？（unbundled item-only: MC ~35-38% vs FF ~17-24%，仍然分离但差距缩小）
2. 增加 code generation (HumanEval) 和 long-form QA benchmark 后，MC/FF 分界是否清晰？
3. Mean difference CI [11.44, 21.02] 的构造方法？是否意识到这是 item-level 而非 benchmark-level 不确定性？
4. MATH 43.9% 残差的进一步分解？
5. vLLM 0.9.2 + enforce_eager 对结论的普适性影响？
6. HellaSwag 是唯一 model×item > item 的 MC benchmark (36.0% vs 34.3%)，对 "MC 统一结构" 的叙述有何影响？

---

## Missing References

1. **ATLAS** (Li et al., 2025; ICLR 2026) — 自适应测试 30-78 items
2. **MetaBench** (Kipnis et al., ICLR 2025) — 6 benchmark 压缩至 <3% items
3. **Waldis et al.** (2024) — LLM evaluation robustness to distributional assumptions

---

## External Review (Stanford Agentic Reviewer)

**状态**: 未返回（pending）。外部审稿请求已发送，截至报告撰写时尚未收到结果。

---

## Visual Layout Check（非评分项）

视觉审查已完成（1 warning, 5 info）：

- ⚠️ **Warning**: 前 3 页无任何 display item，第一个视觉锚点（Figure 1 + Table 1）直到 page 4 才出现。建议将 Figure 1 提前至 page 2-3。
- ℹ️ Page 5 纯文本页（Binary Data / Model-as-Facet），内容密集但可接受。
- ℹ️ Page 7 Figure 2 堆叠柱状图多色可读，建议确认灰度打印辨识度。
- ℹ️ Table 3 列数较多字号偏小但可读，dominant component 加粗为 good practice。
- ℹ️ Figure 3 D-study curves 清晰，Y 轴标签字号略小。
- ℹ️ Appendix 末页仅占约 60%。

---

## Overall Assessment

**Overall Score: 3.5 — Borderline Conference**
**评分范围**: R1 3.5 / R2 3.5 / R3 3.0 → 中位数 3.5
**置信度**: 4/5

### 综合评分理由

| 维度 | R1 | R2 | R3 | 综合 |
|------|----|----|----|----|
| Soundness | 3.5 | 3.5 | 3.0 | 3.5 |
| Excitement | 3.5 | 3.0 | 3.0 | 3.0 |
| Reproducibility | 4.0 | 4.0 | 4.0 | 4.0 |
| Overall | 3.5 | 3.5 | 3.0 | **3.5** |

**综合判断**: 论文在实验规模（2.3M records）、方法论严谨性（6 项 robustness checks、四重二值数据验证）和实用工具价值（D-study calculator）方面表现突出，代表了 LLM 评估方差分析领域的显著推进。

但存在以下核心问题：

1. **模板错误**（N1）是 desk reject 级别，必须立即修复。

2. **核心 claim 统计基础薄弱**（N2）：format-associated pattern 是论文最有区分度的发现，但 p=0.10（理论最小值）、Cohen's d CI 跨零、以及 item-level CI 与 benchmark-level 推断的混淆（R3 新发现），共同削弱了这一 claim 从描述性发现升级为结构性结论的可信度。

3. **实用性 framing 问题**（W5）：10× fewer items 的 claim 遮蔽了 129× 总计算量增加。

4. **Excitement 受限**（R2/R3 共识）：核心方法是 G-theory 的直接应用，与 Messing (2026) 相比主要为 scope 扩展而非方法论创新。

**修改建议优先级**:
1. [阻塞] 换 ACL 模板，验证 ≤8 页
2. [核心] 显著降级 format-associated claim；区分 item-level / benchmark-level 不确定性；报告 d CI
3. [重要] Item-related variance 首次使用时注明拆分构成
4. [重要] 补充 ATLAS/MetaBench 引用
5. [重要] Table 4 增加 total evaluations 列
6. [重要] 讨论 FF benchmark 残差来源
7. [改善] 提供匿名代码链接

**最终判断**: 若 N1-N2 充分解决且 claim 适当降级，论文有 Findings (3.0) 的底线保障，冲 Conference (4.0) 需要补充更多 benchmark 支持核心 claim 或 reframe 为 hypothesis-generating study。当前 3.5（Borderline Conference）反映了扎实的经验贡献与统计局限之间的张力。

---

## Detailed Comments

### Abstract
- "seven facets" → "up to seven facets"（ordering 在 4/5 benchmark 为零）
- "68-72%" 需标注为 bundled item-related variance（item + model×item DIF）
- "format-associated" 需加 hedging

### Introduction (Section 1)
- 前 3 页无 figure/table，建议将 Figure 1 提前
- Contribution 1 的 68-72% 需注明拆分构成
- Contribution 2 "10× fewer items" 需补充总成本 caveat

### Related Work (Section 2)
- 与 Messing (2026) 差异化定位清晰
- 遗漏 ATLAS、MetaBench、Waldis

### Method (Section 3)
- G-theory 解释清晰，ML practitioners 桥接段落有效
- "Item-related variance" 定义处需注明 bundled vs unbundled 视角

### Experiments (Section 4)
- Table 3 prompt 行在 MC/FF 上报告不同 component 易混淆
- Section 4.3 permutation test 限制需更显著呈现；区分 item-level 和 benchmark-level CI
- HellaSwag 是唯一 model×item > item 的 MC benchmark (36.0% vs 34.3%)，未讨论（R3）
- Scale validation 标题应改 "Preliminary Scale Check"
- Table 4 IRT 对比需 fairer comparison

### Conclusion (Section 5)
- "Two extensions are planned" 暗示未完成，可移入 Limitations

### Limitations (Section 6)
- 缺少 residual variance 来源讨论
- 缺少 benchmark 样本量对 format-associated 推断的限制讨论
- 缺少 bundling 选择的局限性讨论

### References
- varannot2025gtheory author 为 Anonymous
- 多处 "and others" 应扩展
- 部分条目缺 volume/pages
