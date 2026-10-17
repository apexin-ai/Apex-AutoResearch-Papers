## 附录引用完整性审计

### (a) 附录盘点
共 27 个 section/subsection（含 1 个 unnumbered section），23 个 table，0 个 figure，0 个 algorithm。

| # | 类型 | 标签 | 内容摘要 |
|---|------|------|----------|
| 1 | section | `app:design_rationale` | 因果设计理据：DAG 解释、操作假设 |
| 2 | section | `app:direction` | 方向不对称与质量混淆：formality 方向效应、GEE 分析 |
| 3 | section | `sec:consistency` | 一致性过滤鲁棒性：position-consistency filter 验证 |
| 4 | section | `app:gee_diagnostics` | GEE 模型诊断：相关结构鲁棒性、交互项检验 |
| 5 | table | `tab:gee_corr` | GEE 相关结构对比（9 个 judge×axis 单元） |
| 6 | table | `tab:gee-interaction` | GEE Style×Originality 交互项（均不显著） |
| 7 | table | `tab:gee_ci` | GEE 条件分解的 95% CI |
| 8 | section | `app:rewriter_indep` | 改写器独立性检验：GPT-4o vs Qwen3 改写器 |
| 9 | table | `tab:rewriter_indep` | 改写器独立性：verbosity 轴 |
| 10 | table | `tab:rewriter_indep_form` | 改写器独立性：formality 轴 |
| 11 | section | `app:nli_sweep` | NLI 阈值敏感性扫描：11 个阈值，44 个组合 |
| 12 | table | `tab:nli_sweep` | BT win probability across NLI thresholds |
| 13 | section | `app:gate_validation` | 方向感知门控验证：bidirectional vs DA 对比 |
| 14 | section | `app:claude_tost` | Claude Sonnet 4 等价性检验（TOST + Bayesian） |
| 15 | table | `tab:tost_sensitivity` | TOST 等价性敏感性分析 |
| 16 | table | `tab:bayesian_equiv` | Bayesian 等价性（BF₀₁） |
| 17 | section | `app:bt_gof` | BT 拟合优度与分层分析 |
| 18 | section | `app:bt_ci` | BT 置信区间 |
| 19 | table | `tab:bt_ci` | 所有 BT 估计的 bootstrap 95% CI |
| 20 | section | `app:bootstrap_attenuation` | Bootstrap 衰减分析：d→0 随 n 增大 |
| 21 | table | `tab:attenuation` | 衰减分析：7 个样本量下的 Likert d |
| 22 | section | `app:power_analysis` | 形式化功效分析 |
| 23 | table | `tab:power` | 80% power 所需 Likert 样本量 |
| 24 | section | `app:sensitivity` | Formality 敏感性层次：7 种测量方法 |
| 25 | table | `tab:sensitivity` | 7 种方法对 formality 数据的结果 |
| 26 | section | `app:verb_sensitivity` | Verbosity 敏感性层次 |
| 27 | table | `tab:verb_sensitivity` | 7 种方法对 verbosity 数据的结果 |
| 28 | subsection | `app:verb_n355` | Verbosity 放大复制（n=330，4 个 judge） |
| 29 | table | `tab:verb_n355` | Verbosity n=330 复制结果 |
| 30 | section | `app:likert100` | 100 分连续 Likert 量表实验 |
| 31 | table | `tab:likert100` | 1-10 vs 1-100 量表对比 |
| 32 | section | `app:nli_ablation` | NLI 门控消融：pass/fail/all 对比 |
| 33 | table | `tab:nli_ablation` | BT by NLI subset |
| 34 | section | `app:artifact_control` | 改写伪影控制：same-style double-rewrite |
| 35 | table | `tab:artifact` | BT P(orig) vs same-style DR |
| 36 | section | `app:implementation` | 实现细节：模型、API、统计方法、基准 |
| 37 | section | `app:holm8` | Holm-Bonferroni 8-test 敏感性分析 |
| 38 | table | `tab:holm8` | 8-test family 校正后 p 值 |
| 39 | section | `app:cross_axis_contamination` | 跨轴污染分析 |
| 40 | table | `tab:cross_axis` | 跨轴污染表面代理指标 |
| 41 | section | `app:fk_length` | FK 长度控制分析：中介分析 |
| 42 | table | `tab:fk_desc` | FK grade 和句长变化描述统计 |
| 43 | section | `app:annotation_agreement` | 人工标注一致性统计 |
| 44 | section | `app:cross_bench` | 跨基准复制（AlpacaEval, MT-Bench） |
| 45 | table | `tab:cross_bench` | 跨基准复制结果 |
| 46 | section | `app:claude_crossbench` | Claude 跨基准分析 |
| 47 | table | `tab:claude_crossbench` | Claude 5 配置 GEE 分解 |
| 48 | section | `app:rewriting_prompts` | 改写 prompt 模板 |
| 49 | section | `app:concordance` | Non-tie 一致性分析 |
| 50 | table | `tab:concordance` | Non-tie concordance 表 |
| 51 | section* | `app:ai-assistants` | AI 辅助声明（unnumbered，无需正文引用） |

### (b) 引用状态
| # | 附录项 | 原引用状态 | 修复操作 | 修复位置（文件:行号附近） |
|---|--------|-----------|----------|--------------------------|
| 1 | `app:design_rationale` | ✅ method.tex:62 | 无需修复 | — |
| 2 | `app:direction` | ✅ experiments.tex:53,105 | 无需修复 | — |
| 3 | `sec:consistency` | ✅ experiments.tex:10 | 无需修复 | — |
| 4 | `app:gee_diagnostics` | ✅ experiments.tex:15,105 | 无需修复 | — |
| 5 | `app:rewriter_indep` | ✅ experiments.tex:52,165; limitations:48 | 无需修复 | — |
| 6 | `app:nli_sweep` | ✅ method.tex:18; experiments.tex:184 | 无需修复 | — |
| 7 | `app:gate_validation` | ✅ method.tex:22 | 无需修复 | — |
| 8 | `app:claude_tost` | ✅ experiments.tex:91 | 无需修复 | — |
| 9 | `app:bt_gof` | ✅ experiments.tex:13 | 无需修复 | — |
| 10 | `app:bt_ci` | ✅ experiments.tex:26 (table caption) | 无需修复 | — |
| 11 | `app:bootstrap_attenuation` | ✅ experiments.tex:76 | 无需修复 | — |
| 12 | `app:power_analysis` | ✅ experiments.tex:16,85 | 无需修复 | — |
| 13 | `app:sensitivity` | ✅ experiments.tex:83 | 无需修复 | — |
| 14 | `app:verb_sensitivity` | ✅ experiments.tex:83 | 无需修复 | — |
| 15 | `app:likert100` | ✅ experiments.tex:79 | 无需修复 | — |
| 16 | `app:nli_ablation` | ❌ 正文讨论了 NLI ablation 结果但未引用附录 | **已修复**：添加 `Appendix~\ref{app:nli_ablation}` | experiments.tex:190 |
| 17 | `app:artifact_control` | ✅ experiments.tex:141 | 无需修复 | — |
| 18 | `app:implementation` | ✅ method.tex:53 | 无需修复 | — |
| 19 | `app:holm8` | ✅ experiments.tex:8 | 无需修复 | — |
| 20 | `app:cross_axis_contamination` | ✅ method.tex:11 | 无需修复 | — |
| 21 | `app:fk_length` | ✅ experiments.tex:166 | 无需修复 | — |
| 22 | `app:annotation_agreement` | ✅ experiments.tex:182 | 无需修复 | — |
| 23 | `app:cross_bench` | ✅ experiments.tex:26,77,174 | 无需修复 | — |
| 24 | `app:claude_crossbench` | ✅ experiments.tex:91,174 | 无需修复 | — |
| 25 | `app:rewriting_prompts` | ✅ method.tex:9 | 无需修复 | — |
| 26 | `app:concordance` | ✅ experiments.tex:90 | 无需修复 | — |
| 27 | `app:verb_n355` | ✅ experiments.tex:153 | 无需修复 | — |
| 28 | `app:ai-assistants` | ✅ unnumbered disclosure section，无需正文引用 | 无需修复 | — |

### (c) 删除项
无删除。所有附录内容均为主文 claims 提供必要的统计细节或鲁棒性检验。

### (d) 新增引用的具体文本
1 条修复：

**文件**: `sections/experiments.tex`，第 190 行附近
**原文**:
```
(i)~NLI ablation reverses NLI-fail pairs (BT 41.7\%)
```
**修改为**:
```
(i)~NLI ablation reverses NLI-fail pairs (BT 41.7\%; Appendix~\ref{app:nli_ablation})
```
**理由**: 正文在 §4.4 Robustness 的 amplification controls 列表中引用了 NLI ablation 的具体数字（BT 41.7%），但缺少指向附录完整消融表（Table 14, `tab:nli_ablation`）的 `\ref`。读者需要该引用来查看 pass/fail/all 三组的完整对比。
