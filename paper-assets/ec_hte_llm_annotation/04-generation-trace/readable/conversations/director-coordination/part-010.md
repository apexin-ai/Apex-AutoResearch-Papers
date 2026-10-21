# Director coordination — Part 10 of 10

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects** · Conversation logs

[← Part 9](part-009.md) · [Transcript overview](../director-coordination.md) · [Structured JSON](../../../sessions/fb/fb462ae0cd5c4c630c34.json)

## Round 195

### Tool call

_source line 2518 · 2026-05-25T06:31:36.578052+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "ec_hte_llm_annotation",
  "issues_yaml": "issues:\n  # === RESOLVED (prior rounds — abbreviated) ===\n  - id: \"R1-N1\"\n    summary: \"Proposition 1 以 formal bound 呈现但仅有 97% MC 经验验证\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 2\n    action_items: []\n    resolution: \"重新推导为精确恒等式\"\n    resolution_round: 0\n\n  - id: \"R2-W8\"\n    summary: \"Proposition 1 限于 K=2\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    action_items: []\n    resolution: \"Theorem 1 适用一般 K\"\n    resolution_round: 0\n\n  - id: \"R1-N2\"\n    summary: \"Real data ground truth CATE 来源不明\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    action_items: []\n    resolution: \"恰当定位为 illustrative application\"\n    resolution_round: 0\n\n  - id: \"R1-N3\"\n    summary: \"HB 模型规格严重不完整\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    action_items: []\n    resolution: \"完整 MCMC 规格\"\n    resolution_round: 0\n\n  - id: \"JOINT-W4\"\n    summary: \"相关工作严重遗漏\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    action_items: []\n    resolution: \"30+ 引用覆盖\"\n    resolution_round: 0\n\n  - id: \"JOINT-W3\"\n    summary: \"信息密度过高\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    action_items: []\n    resolution: \"主文精简至合理密度\"\n    resolution_round: 0\n\n  - id: \"R2-W7\"\n    summary: \"真实数据验证单薄\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    action_items: []\n    resolution: \"恰当定位 + 公开数据集\"\n    resolution_round: 0\n\n  - id: \"R1-W5\"\n    summary: \"Pages 9-10 缺 Appendix 标签\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 0\n    action_items: []\n    resolution: \"附录结构重组\"\n    resolution_round: 0\n\n  - id: \"R19-C1\"\n    summary: \"Abstract 'R²≥0.97 across synthetic grids and 11 empirical LLM CMs' 事实性错误\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    action_items: []\n    resolution: \"已修正 Abstract L4, Intro L17/L31, Conclusion L4——区分合成 vs 真实 LLM 的 R² 范围\"\n    resolution_round: 19\n\n  - id: \"R19-C2\"\n    summary: \"诊断工具 (Proposition 5) AUC=0.63 但 Abstract/Intro 呈现为核心贡献无性能限定\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    action_items: []\n    resolution: \"AUC 数字从 Abstract 完全移除\"\n    resolution_round: 19\n\n  - id: \"R19-C3\"\n    summary: \"核心量化 claims (7.4×) 在假设完全满足的合成数据上得出，moderate 配置下无改善\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    action_items: []\n    resolution: \"Abstract L6 修正为 'reducing |bias| by 7.4× under extreme heterogeneity'\"\n    resolution_round: 19\n\n  - id: \"R19-W1\"\n    summary: \"操作条件过窄——无真实 LLM-dataset pair 通过全部 5 个筛选条件\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    action_items: []\n    resolution: \"Conclusion 扩展含 relaxed screening adoption guideline\"\n    resolution_round: 19\n\n  - id: \"R19-W2\"\n    summary: \"DGP 缺乏 observational/confounding 场景验证\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    action_items: []\n    resolution: \"Limitations 已补充 confounded DGP scope\"\n    resolution_round: 19\n\n  - id: \"R19-M4\"\n    summary: \"Conclusion 过短（仅两句话）\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    action_items: []\n    resolution: \"Conclusion 从 2 句扩展到 3 句含 adoption guideline\"\n    resolution_round: 19\n\n  - id: \"R19-DATA1\"\n    summary: \"experiments.tex L19 'EC-HTE eliminates sign reversal entirely' 与 stance/AG News 数据矛盾\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    action_items: []\n    resolution: \"已限定为 primary K=2 configuration\"\n    resolution_round: 19\n\n  - id: \"R19-DATA2\"\n    summary: \"task-agnosticity 段 '16 real LLM CMs span four tasks' 与 L11 '8×2=16' 计数不一致\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    action_items: []\n    resolution: \"区分 16 core CMs 和独立 cross-task validations\"\n    resolution_round: 19\n\n  - id: \"R19-DATA3\"\n    summary: \"AG News appendix 引用 GPT-4/~85% 与源论文不符\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    action_items: []\n    resolution: \"引用细节修正完成\"\n    resolution_round: 19\n\n  - id: \"R20-M1\"\n    summary: \"Abstract 'per-model range 0.26-0.09' 数值排序应为 0.09-0.26（从小到大）\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 20\n    last_seen_round: 21\n    action_items: []\n    resolution: \"确认 Abstract 已是 '0.76--0.99'（升序），非问题\"\n    resolution_round: 21\n\n  - id: \"R19-W3\"\n    summary: \"Theorem 1→Proposition 3 呈现顺序：A5 排除目标场景但未充分强调\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 21\n    action_items: []\n    resolution: \"Proposition 3 已在主文 Section 3, 含完整公式和 Δτ_s\"\n    resolution_round: 21\n\n  - id: \"R19-M1\"\n    summary: \"Assumption (A5) 实践限制被轻描淡写\"\n    category: method\n    severity: info\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 21\n    action_items: []\n    resolution: \"Proposition 3 已在主文充分展示 A5 relaxation\"\n    resolution_round: 21\n\n  - id: \"R19-W6\"\n    summary: \"Finite-sample 传播保证缺失——Theorem 1 到 plug-in estimator 仅有 O_p notation\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 19\n    last_seen_round: 23\n    mentions:\n      - round: 22\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 共识确认技术错误：O_p(κ·n^{-1/2}) 应为 O_p(κ²·n^{-1/2})。\"\n      - round: 22\n        reviewers: [1, 2]\n        note: \"theory.tex L92 修正为 κ²。\"\n      - round: 23\n        reviewers: [1, 2]\n        note: \"主文已修正为 κ²，但 appendix.tex L103 仍用 κ(M_global)（单次幂），且作用于不同对象（Ĉ_s^{-1} vs M_global^{-1} M_s）。论文未解释两个 bound 的区别。Presentation 不一致。\"\n    action_items:\n      - round: 22\n        action: \"theory.tex L92 修正 κ→κ²，含 Neumann expansion 解释\"\n        assigned_to: agent\n        status: done\n      - round: 23\n        action: \"appendix.tex L103 统一为 κ² 或明确说明两个 bound 的适用范围差异\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R19-M6\"\n    summary: \"Algorithm 1 缺收敛标准/最大迭代次数\"\n    category: method\n    severity: info\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 22\n    mentions:\n      - round: 22\n        reviewers: [1, 2]\n        note: \"通过 EB vs Gibbs 不一致问题暴露：Algorithm 1 描述 Gibbs 但代码用 EB。\"\n    action_items:\n      - round: 22\n        action: \"Algorithm 1 改为 EB 流程，Gibbs 降为 appendix 替代方案\"\n        assigned_to: agent\n        status: done\n    resolution: \"Algorithm 1 已改为 EB point estimates (closed-form Dirichlet update)，MCMC 保留为 appendix 验证方案。与 method.tex (<5ms) 和代码一致。\"\n    resolution_round: 22\n\n  - id: \"R22-Q1\"\n    summary: \"Method 说 empirical Bayes (<5ms) 但 Algorithm 1 描述 Gibbs sampler——不一致\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 22\n    mentions:\n      - round: 22\n        reviewers: [1, 2]\n        note: \"代码确认主实验用 EB (estimate_cm_hb_map_eb)，零 Gibbs 代码。\"\n    action_items:\n      - round: 22\n        action: \"Algorithm 1 EB 化 + appendix MCMC 描述统一\"\n        assigned_to: agent\n        status: done\n    resolution: \"Algorithm 1 改为 EB，与 method.tex 和代码一致。Reviewer 验证通过。\"\n    resolution_round: 22\n\n  - id: \"R22-Q2\"\n    summary: \"A3 放松时 'identity remains exact with modified coefficients' 但未给出显式形式\"\n    category: method\n    severity: info\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 22\n    mentions:\n      - round: 22\n        reviewers: [1, 2]\n        note: \"theory.tex L84 声称修正系数存在但未展示。\"\n    action_items:\n      - round: 22\n        action: \"Appendix D 补充 A3 放松显式推导 (M_s Bayes rule form + B_s·1=0 证明)\"\n        assigned_to: agent\n        status: done\n    resolution: \"appendix classimbalance 节新增 eq:ms_imbalanced 显式形式，证明 product form 对任意 p₀ 成立。\"\n    resolution_round: 22\n\n  - id: \"R22-Q3\"\n    summary: \"Cov(π_s, Δτ_s) 在实验中未报告——Corollary 4 实际可用性的关键\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 22\n    mentions:\n      - round: 22\n        reviewers: [1, 2]\n        note: \"应在 semi-synthetic 实验中报告此协方差值。\"\n    action_items:\n      - round: 22\n        action: \"从现有数据提取 Cov(π_s, Δτ_s) 并加入 appendix\"\n        assigned_to: agent\n        status: done\n    resolution: \"appendix A5 violation 节新增 Corollary 4 实证验证：主 grid Cov=0（aggregate bias 抵消），A5 violation Cov=±0.020（predicted ±0.029 与 MC 吻合）。\"\n    resolution_round: 22\n\n  - id: \"R22-Q4\"\n    summary: \"EC-HTE + PPCI 理论兼容性条件不明\"\n    category: method\n    severity: info\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 22\n    mentions:\n      - round: 22\n        reviewers: [1, 2]\n        note: \"LLM 同时标注 covariate 和 outcome 时独立性可能失效。\"\n    action_items:\n      - round: 22\n        action: \"Limitations 补充 PPCI 兼容性讨论\"\n        assigned_to: agent\n        status: done\n    resolution: \"limitations.tex 新增 PPCI 独立性讨论段落。Reviewer 验证通过。\"\n    resolution_round: 22\n\n  - id: \"R20-C1\"\n    summary: \"对称误分类假设 (A2) 限制标题级 'Exact Identity' 声称——非对称情形诊断退化\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 20\n    last_seen_round: 22\n    mentions:\n      - round: 20\n        reviewers: [1, 2]\n        note: \"首次提出。非对称下 R² 降至 0.73。\"\n      - round: 21\n        reviewers: [1, 2]\n        note: \"再次关注。§5.4 添加 matrix vs scalar 区分。\"\n      - round: 22\n        reviewers: [1, 2]\n        note: \"R22 R2 clarified: 恒等式在非对称下仍精确，降级的是诊断 AUC。但 Worker 分析发现 AUC 0.66 来自错误指标（未归一化 matrix score），标量公式实际 AUC=0.96。\"\n    action_items:\n      - round: 20\n        action: \"主文给出 2×2 非对称精确偏差 closed-form\"\n        assigned_to: author\n        status: done\n      - round: 21\n        action: \"experiments.tex §5.4 添加 matrix vs scalar 区分\"\n        assigned_to: director\n        status: done\n      - round: 22\n        action: \"修正 AUC 0.66→0.96（3处），因 0.66 来自错误指标\"\n        assigned_to: agent\n        status: done\n    resolution: \"AUC 0.66 来自未归一化的 raw matrix score，非 Prop 5 标量诊断。标量诊断在非对称下实际 AUC=0.96（48 configs）/ 正确识别全部 harmed subgroups（8 semi-real LLMs, 32 subgroups）。论文 3 处已更新。Reviewer 验证一致性通过。\"\n    resolution_round: 22\n\n  - id: \"R12-M2\"\n    summary: \"Remark 2 与 Theorem 1 假设列表表面矛盾 (A2 地位)\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 12\n    last_seen_round: 22\n    mentions:\n      - round: 22\n        reviewers: [1, 2]\n        note: \"R22 clarified: 恒等式不依赖 A2，标量简化依赖 A2 但 AUC 不降级（0.96）。问题根源已消除。\"\n    action_items:\n      - round: 20\n        action: \"主文给出 2×2 非对称精确偏差 closed-form\"\n        assigned_to: author\n        status: done\n    resolution: \"AUC 0.66→0.96 修正消除了 A2 限制诊断的核心论据。Remark 2 准确描述 A2 仅简化标量形式。\"\n    resolution_round: 22\n\n  - id: \"R21-N1\"\n    summary: \"非对称误分类下诊断准则 AUC 从 0.86 降至 0.65\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 22\n    mentions:\n      - round: 22\n        reviewers: [1, 2]\n        note: \"AUC 0.66 来自错误指标。实际标量诊断 AUC=0.96。4 轮复发问题的根因已消除。\"\n    action_items:\n      - round: 21\n        action: \"experiments.tex §5.4 增加 matrix vs scalar 区分 + 非对称 AUC 数字\"\n        assigned_to: director\n        status: done\n      - round: 22\n        action: \"修正 AUC 0.66→0.96\"\n        assigned_to: agent\n        status: done\n    resolution: \"AUC 0.66 来自错误指标，标量诊断实际 AUC=0.96。论文已更新。\"\n    resolution_round: 22\n\n  # === OPEN / IN_PROGRESS ===\n\n  - id: \"R16-W7\"\n    summary: \"Figure 2 红绿配色色盲不友好\"\n    category: format\n    severity: info\n    status: in_progress\n    first_raised_round: 16\n    last_seen_round: 22\n    mentions:\n      - round: 22\n        reviewers: []\n        note: \"R22 视觉审查仍检测到残留红绿对比。Camera-ready 修复。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R19-C4\"\n    summary: \"CausalForest 集成验证不足——缺 X-learner/BART\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 19\n    last_seen_round: 22\n    mentions:\n      - round: 22\n        reviewers: []\n        note: \"R22 未直接再提。跨估计器（CF + R-learner）是加分项。X-learner/BART 为 rebuttal 准备。\"\n    action_items:\n      - round: 19\n        action: \"Rebuttal 准备: X-learner/BART 跨估计器验证\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R19-W4\"\n    summary: \"HB 优势在 n_expert≥250 时消失但未讨论上限\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 19\n    last_seen_round: 22\n    mentions:\n      - round: 22\n        reviewers: []\n        note: \"R22 未再提及。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R19-W5\"\n    summary: \"缺乏 fully real-data validation (所有实验为 semi-synthetic)\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 19\n    last_seen_round: 23\n    mentions:\n      - round: 22\n        reviewers: [2]\n        note: \"R22 R2 再次强调。R1 REBUT 有力（半合成是因果推断标准范式）。降级为 moderate weakness。Rebuttal 备弹。\"\n      - round: 23\n        reviewers: [1, 2]\n        note: \"R23 两位 Reviewer 共识。R1 指出 A1 by construction 无法验证实际鲁棒性，sensitivity analysis γ_T=0.10 致 coverage 75% 暴露脆弱性。R2 同意并补充：real-data case study 可间接评估 A1 合理性。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R18-SF6\"\n    summary: \"Plugin SE 欠覆盖 93.8%\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 17\n    last_seen_round: 23\n    mentions:\n      - round: 23\n        reviewers: [1, 2]\n        note: \"R1 指出 plug-in SE 不 propagate CM posterior uncertainty。R2 rebuts：bootstrap (B=100) 恢复 ≥95% coverage，HB partial pooling 隐式 regularize。分歧：R2 认为是 implementation choice with empirical justification，非 gap。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R18-M1\"\n    summary: \"EC-HTE wall-clock time 未报告\"\n    category: experiment\n    severity: info\n    status: open\n    first_raised_round: 18\n    last_seen_round: 22\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R17-NLP2\"\n    summary: \"论文对 NLP 社区的价值定位不清\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 17\n    last_seen_round: 23\n    mentions:\n      - round: 22\n        reviewers: [2]\n        note: \"R22 R2 维持。EMNLP 受众适配性是结构性问题。R1 认为时效性足够。评分分歧核心因素。\"\n      - round: 23\n        reviewers: [2]\n        note: \"R2 再次提出 venue fit 问题：论文本质是 causal inference methodology，NLP 内容作为 application domain 而非方法论贡献。R1 未直接讨论 venue fit。\"\n    action_items:\n      - round: 21\n        action: \"experiments.tex §5.2 增加 CivilComments NLP insight 段落\"\n        assigned_to: director\n        status: done\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R17-W2\"\n    summary: \"Scalability to K>>4 未充分讨论\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 17\n    last_seen_round: 23\n    mentions:\n      - round: 22\n        reviewers: []\n        note: \"R22 未再提及。Intro 限定和 Section 5.4 已覆盖。\"\n      - round: 23\n        reviewers: [1, 2]\n        note: \"R1 将 K≤4 作为 applicability limitation 提出。R2 同意并指出 K>4 是否为 estimation noise 还是 structural limitation 不清。但 Intro K≤4 限定和 Section 5.4 已有覆盖，维持 resolved。\"\n    action_items:\n      - round: 21\n        action: \"Intro Contribution 2 增加 K ≤ 4 限定\"\n        assigned_to: director\n        status: done\n    resolution: \"Intro K≤4 限定 + Section 5.4 operating conditions 覆盖。已诚实声明。\"\n    resolution_round: 22\n\n  - id: \"R10-W2\"\n    summary: \"DGP 较简单，无混杂变量\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 10\n    last_seen_round: 22\n    action_items: []\n    resolution: \"Limitations 已补充 confounded DGP scope。R22 未再提及。\"\n    resolution_round: 22\n\n  - id: \"R19-M2\"\n    summary: \"HB 先验敏感性分析不充分\"\n    category: method\n    severity: info\n    status: open\n    first_raised_round: 19\n    last_seen_round: 22\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R19-M3\"\n    summary: \"Bootstrap SE (B=100) 计算成本未讨论\"\n    category: experiment\n    severity: info\n    status: open\n    first_raised_round: 19\n    last_seen_round: 22\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R19-M5\"\n    summary: \"'Semi-synthetic' 术语在 Section 5.1 和 5.3 含义不同\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 19\n    last_seen_round: 22\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R20-C2\"\n    summary: \"相对 Frazis-Loewenstein (2003) 增量贡献未界定\"\n    category: framing\n    severity: critical\n    status: in_progress\n    first_raised_round: 20\n    last_seen_round: 23\n    mentions:\n      - round: 22\n        reviewers: [2]\n        note: \"R22 R2 通过 novelty depth 间接涉及。R1 用 FWL 类比反驳。评分分歧核心因素。\"\n      - round: 23\n        reviewers: [1, 2]\n        note: \"R2 维持 novelty depth concern。R1 提出 FWL 类比进一步限制 novelty 声称。R2 rebuts R1-W6（F-L strawman）认为比较公平——F-L 确实是 practitioners 在异质场景下 naively 使用的标准方法。评分分歧核心。\"\n    action_items:\n      - round: 20\n        action: \"Section 3 明确声明与 F-L 的 nesting 关系\"\n        assigned_to: director\n        status: done\n      - round: 21\n        action: \"Section 3 增加 sign reversal novelty statement\"\n        assigned_to: director\n        status: done\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R20-C3\"\n    summary: \"缺失噪声标签学习核心文献\"\n    category: writing\n    severity: critical\n    status: in_progress\n    first_raised_round: 20\n    last_seen_round: 23\n    mentions:\n      - round: 22\n        reviewers: []\n        note: \"R22 未直接再提。subgroup-dependent vs instance-dependent noise 联系仍为 open action。\"\n      - round: 23\n        reviewers: [2]\n        note: \"R2 指出 subgroup-dependent vs instance-dependent noise 定位仍未充分讨论。Related work 已增加噪声标签段落但深度不足。\"\n    action_items:\n      - round: 20\n        action: \"Related Work 增加噪声标签学习段落\"\n        assigned_to: director\n        status: done\n      - round: 21\n        action: \"深化 subgroup-dependent vs instance-dependent noise 联系\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R20-W1\"\n    summary: \"MC=100 不足以支撑 coverage 声称\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 20\n    last_seen_round: 23\n    mentions:\n      - round: 22\n        reviewers: []\n        note: \"R22 未直接再提。Table 1 caption SE 注释已添加。\"\n      - round: 23\n        reviewers: [1, 2]\n        note: \"R1 重新提出：SE≈2.2pp 使 93% vs 95% coverage 不可区分。R2 同意但认为核心 claims (bias reduction, sign reversal) 不依赖精确 coverage，可降级为 info。\"\n    action_items:\n      - round: 20\n        action: \"关键配置增加至 ≥500 MC runs（rebuttal/camera-ready）\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R20-W2\"\n    summary: \"方法论技术新颖性偏浅\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 20\n    last_seen_round: 23\n    mentions:\n      - round: 22\n        reviewers: [2]\n        note: \"R22 R2 核心论据。R1 用 FWL 类比 REBUT。结构性分歧，rebuttal 论点。\"\n      - round: 23\n        reviewers: [1, 2]\n        note: \"R2 核心 concern：mathematical machinery (matrix CM inversion, subgroup stratification) 是 standard measurement error econometrics。R1 通过 FWL 类比间接支持此观点。两位 Reviewer 共识：贡献是 'careful application of known techniques to important new context'，非 methodological breakthrough。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R20-W3\"\n    summary: \"假设 (A1) 灵敏度分析形式单一\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 20\n    last_seen_round: 23\n    mentions:\n      - round: 23\n        reviewers: [1, 2]\n        note: \"R1 指出 γ_T=0.10 致 coverage 75%，sensitivity analysis 暴露脆弱性而非证明鲁棒性。R2 同意并关联 real-data validation 缺失。\"\n    action_items:\n      - round: 20\n        action: \"增加文本特征 confounding 灵敏度分析（rebuttal/camera-ready）\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R20-M2\"\n    summary: \"Theorem 1 中 'effect-modifier level z' 措辞对 NLP 读者不友好\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 20\n    last_seen_round: 22\n    action_items:\n      - round: 21\n        action: \"theory.tex Theorem 1 后增加 K=2 数值示例\"\n        assigned_to: director\n        status: done\n    resolution: \"数值示例已添加。R22 未再提及。\"\n    resolution_round: 22\n\n  - id: \"R20-M3\"\n    summary: \"Figure 2 'ε-guard' 标注字号偏小\"\n    category: format\n    severity: info\n    status: open\n    first_raised_round: 20\n    last_seen_round: 22\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R21-FIX1\"\n    summary: \"Remark 交叉引用统一\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 22\n    action_items:\n      - round: 21\n        action: \"统一为 \\\\ref{rem:asymmetric}\"\n        assigned_to: director\n        status: done\n    resolution: \"所有引用统一。R22 未再提及。\"\n    resolution_round: 21\n\n  - id: \"R21-N2\"\n    summary: \"NLP 社区适配性不足\"\n    category: framing\n    severity: critical\n    status: in_progress\n    first_raised_round: 21\n    last_seen_round: 23\n    mentions:\n      - round: 22\n        reviewers: [2]\n        note: \"R22 R2 维持。结构性问题。R1 认为时效性足够。\"\n      - round: 23\n        reviewers: [2]\n        note: \"R2 维持：论文本质是 causal inference methodology，NLP 作为 application domain。更适合 JCI/UAI/AISTATS。R1 未直接讨论但同意 novelty 对 EMNLP 偏弱。\"\n    action_items:\n      - round: 21\n        action: \"experiments.tex §5.2 增加 CivilComments NLP insight\"\n        assigned_to: director\n        status: done\n      - round: 21\n        action: \"将 Appendix M 关键发现移入正文（rebuttal/camera-ready）\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R21-W1\"\n    summary: \"Proposition 5 诊断 vs 直接运行 EC-HTE 的增量价值不明\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 21\n    last_seen_round: 22\n    action_items:\n      - round: 21\n        action: \"明确诊断准则的使用场景（rebuttal）\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R21-W2\"\n    summary: \"A3 (P(Z=0)=0.5) 限制性在正文中讨论不足\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 22\n    mentions:\n      - round: 22\n        reviewers: []\n        note: \"R22 未直接再提。limitations.tex 讨论 + appendix A3 显式推导已完成。\"\n    action_items:\n      - round: 21\n        action: \"Limitations 补充 A3 class imbalance 影响讨论\"\n        assigned_to: director\n        status: done\n      - round: 22\n        action: \"Appendix 补充 A3 放松显式推导\"\n        assigned_to: agent\n        status: done\n    resolution: \"Limitations 讨论 + Appendix 显式推导均已完成。\"\n    resolution_round: 22\n\n  - id: \"R21-W3\"\n    summary: \"操作条件称 'framework' 轻微过度声称\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 22\n    action_items:\n      - round: 21\n        action: \"Contribution 2 措辞调整为 'empirical operating guidelines'\"\n        assigned_to: director\n        status: done\n    resolution: \"已调整措辞。R22 确认展示透明。\"\n    resolution_round: 22\n\n  - id: \"R21-W4\"\n    summary: \"Section 3 符号密度对 NLP 读者偏高\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 22\n    action_items:\n      - round: 21\n        action: \"Theorem 1 后增加 K=2 数值示例\"\n        assigned_to: director\n        status: done\n    resolution: \"数值示例已添加。R22 未再提及。\"\n    resolution_round: 22\n\n  - id: \"R21-REF1\"\n    summary: \"遗漏相关工作: Veitch 2020, Wood-Doughty 2018\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 22\n    action_items:\n      - round: 21\n        action: \"Related Work 增加引用\"\n        assigned_to: director\n        status: done\n    resolution: \"引用已添加。R22 未再提及。\"\n    resolution_round: 22\n\n  # === R22 ISSUES (updated for R23) ===\n\n  - id: \"R22-W1\"\n    summary: \"κ-guard 阈值 100 缺乏与 O_p(κ²·n^{-1/2}) 的理论连接\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 22\n    last_seen_round: 23\n    mentions:\n      - round: 22\n        reviewers: [1, 2]\n        note: \"Minor warning。κ 余项已修正为 κ²，但最优阈值推导仍待 rebuttal。\"\n      - round: 23\n        reviewers: [2]\n        note: \"R2 Q3 问 Δπ>0.15 阈值是否有理论推导。R1 认为有理论依据但 REBUT 程度不一。\"\n    action_items:\n      - round: 22\n        action: \"基于 O_p(κ²·n^{-1/2}) 推导理论最优 κ 阈值（rebuttal）\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R22-W2\"\n    summary: \"EB 两阶段低估后验不确定性\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 22\n    last_seen_round: 23\n    mentions:\n      - round: 22\n        reviewers: [1, 2]\n        note: \"Coverage ≥93% 缓解。EB vs full-Bayes coverage 对比为 rebuttal 备弹。\"\n      - round: 23\n        reviewers: [1, 2]\n        note: \"R1 W4 提出 SE 不 propagate CM uncertainty。R2 rebuts 认为 bootstrap 已解决。分歧。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R22-W8\"\n    summary: \"Abstract 信息密度过高（12+ 具体数字）\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 22\n    last_seen_round: 23\n    mentions:\n      - round: 22\n        reviewers: [1, 2]\n        note: \"Minor 共识。Camera-ready 处理。\"\n      - round: 23\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 再次共识。Abstract 读起来像 results table 而非 narrative summary。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R22-W9\"\n    summary: \"Debiasing 术语歧义（fairness vs measurement-error）\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 22\n    last_seen_round: 23\n    mentions:\n      - round: 22\n        reviewers: [1, 2]\n        note: \"Minor 共识。Footnote 1 已有澄清。\"\n      - round: 23\n        reviewers: [2]\n        note: \"R2 再次提出。标题中 'debiasing' 在 NLP 社区有 fairness 歧义。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R22-W10\"\n    summary: \"Per-model R² 低端讨论不足（GPT-4o-mini R²=0.893）\"\n    category: experiment\n    severity: info\n    status: open\n    first_raised_round: 22\n    last_seen_round: 23\n    mentions:\n      - round: 22\n        reviewers: [1, 2]\n        note: \"R1 建议增加回归分析 R² ~ f(FPR, FNR, |FPR-FNR|, n)。Rebuttal 准备。\"\n      - round: 23\n        reviewers: [1, 2]\n        note: \"R1 指出 R²=0.76 削弱 'exact' 说服力（24% 未解释方差）。R2 同意。论文未对低 R² case 做 failure analysis。升级至 warning。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R22-REF1\"\n    summary: \"缺 Filtered PPI 引用 (arXiv:2602.10464)\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 22\n    last_seen_round: 23\n    mentions:\n      - round: 22\n        reviewers: [1, 2]\n        note: \"真实论文，高度相关。Camera-ready 添加。\"\n      - round: 23\n        reviewers: [1, 2]\n        note: \"R2 再次指出。R1 表示无法独立验证但认为 plausible。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  # === R23 NEW ISSUES ===\n\n  - id: \"R23-W1\"\n    summary: \"诊断 AUC=0.86 (symmetric case) 缺乏 decision-consequence 分析\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 23\n    last_seen_round: 23\n    mentions:\n      - round: 23\n        reviewers: [1, 2]\n        note: \"R1 提出：AUC=0.86 在 symmetric case 下有非平凡误判率，但论文未讨论 FP/FN 不对称代价。在 causal inference 中 false negative（遗漏有害 correction）后果远重于 false positive（不必要的 variance 增加）。建议提供 precision/recall breakdown 和 decision threshold tradeoff。R2 同意。\"\n    action_items:\n      - round: 23\n        action: \"补充诊断 AUC 的 precision/recall breakdown 和 decision-theoretic framing（rebuttal）\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R23-W2\"\n    summary: \"'Debiasing hurts' framing 在 moderate heterogeneity 下不成立\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 23\n    last_seen_round: 23\n    mentions:\n      - round: 23\n        reviewers: [1, 2]\n        note: \"R2 提出：标题暗示 debiasing 普遍有害，但论文表明仅在 extreme heterogeneity 下成立。Moderate 配置下 global correction 仍有益。R1 同意 headline claims (7.4×) 仅限 extreme DGP。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R23-Q1\"\n    summary: \"Propensity score estimation error 与 CM estimation error 的交互效应未讨论\"\n    category: method\n    severity: info\n    status: open\n    first_raised_round: 23\n    last_seen_round: 23\n    mentions:\n      - round: 23\n        reviewers: [1, 2]\n        note: \"R2 提出：观察性研究中 treatment assignment 和 outcome measurement 同时含噪。Identity 在 joint estimation error 下是否成立？R1 AGREE。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "ec_hte_llm_annotation",
    "issues_yaml": "issues:\n  # === RESOLVED (prior rounds — abbreviated) ===\n  - id: \"R1-N1\"\n    summary: \"Proposition 1 以 formal bound 呈现但仅有 97% MC 经验验证\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 2\n    action_items: []\n    resolution: \"重新推导为精确恒等式\"\n    resolution_round: 0\n\n  - id: \"R2-W8\"\n    summary: \"Proposition 1 限于 K=2\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    action_items: []\n    resolution: \"Theorem 1 适用一般 K\"\n    resolution_round: 0\n\n  - id: \"R1-N2\"\n    summary: \"Real data ground truth CATE 来源不明\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    action_items: []\n    resolution: \"恰当定位为 illustrative application\"\n    resolution_round: 0\n\n  - id: \"R1-N3\"\n    summary: \"HB 模型规格严重不完整\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    action_items: []\n    resolution: \"完整 MCMC 规格\"\n    resolution_round: 0\n\n  - id: \"JOINT-W4\"\n    summary: \"相关工作严重遗漏\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    action_items: []\n    resolution: \"30+ 引用覆盖\"\n    resolution_round: 0\n\n  - id: \"JOINT-W3\"\n    summary: \"信息密度过高\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    action_items: []\n    resolution: \"主文精简至合理密度\"\n    resolution_round: 0\n\n  - id: \"R2-W7\"\n    summary: \"真实数据验证单薄\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    action_items: []\n    resolution: \"恰当定位 + 公开数据集\"\n    resolution_round: 0\n\n  - id: \"R1-W5\"\n    summary: \"Pages 9-10 缺 Appendix 标签\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 0\n    action_items: []\n    resolution: \"附录结构重组\"\n    resolution_round: 0\n\n  - id: \"R19-C1\"\n    summary: \"Abstract 'R²≥0.97 across synthetic grids and 11 empirical LLM CMs' 事实性错误\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    action_items: []\n    resolution: \"已修正 Abstract L4, Intro L17/L31, Conclusion L4——区分合成 vs 真实 LLM 的 R² 范围\"\n    resolution_round: 19\n\n  - id: \"R19-C2\"\n    summary: \"诊断工具 (Proposition 5) AUC=0.63 但 Abstract/Intro 呈现为核心贡献无性能限定\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    action_items: []\n    resolution: \"AUC 数字从 Abstract 完全移除\"\n    resolution_round: 19\n\n  - id: \"R19-C3\"\n    summary: \"核心量化 claims (7.4×) 在假设完全满足的合成数据上得出，moderate 配置下无改善\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    action_items: []\n    resolution: \"Abstract L6 修正为 'reducing |bias| by 7.4× under extreme heterogeneity'\"\n    resolution_round: 19\n\n  - id: \"R19-W1\"\n    summary: \"操作条件过窄——无真实 LLM-dataset pair 通过全部 5 个筛选条件\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    action_items: []\n    resolution: \"Conclusion 扩展含 relaxed screening adoption guideline\"\n    resolution_round: 19\n\n  - id: \"R19-W2\"\n    summary: \"DGP 缺乏 observational/confounding 场景验证\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    action_items: []\n    resolution: \"Limitations 已补充 confounded DGP scope\"\n    resolution_round: 19\n\n  - id: \"R19-M4\"\n    summary: \"Conclusion 过短（仅两句话）\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    action_items: []\n    resolution: \"Conclusion 从 2 句扩展到 3 句含 adoption guideline\"\n    resolution_round: 19\n\n  - id: \"R19-DATA1\"\n    summary: \"experiments.tex L19 'EC-HTE eliminates sign reversal entirely' 与 stance/AG News 数据矛盾\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    action_items: []\n    resolution: \"已限定为 primary K=2 configuration\"\n    resolution_round: 19\n\n  - id: \"R19-DATA2\"\n    summary: \"task-agnosticity 段 '16 real LLM CMs span four tasks' 与 L11 '8×2=16' 计数不一致\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    action_items: []\n    resolution: \"区分 16 core CMs 和独立 cross-task validations\"\n    resolution_round: 19\n\n  - id: \"R19-DATA3\"\n    summary: \"AG News appendix 引用 GPT-4/~85% 与源论文不符\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    action_items: []\n    resolution: \"引用细节修正完成\"\n    resolution_round: 19\n\n  - id: \"R20-M1\"\n    summary: \"Abstract 'per-model range 0.26-0.09' 数值排序应为 0.09-0.26（从小到大）\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 20\n    last_seen_round: 21\n    action_items: []\n    resolution: \"确认 Abstract 已是 '0.76--0.99'（升序），非问题\"\n    resolution_round: 21\n\n  - id: \"R19-W3\"\n    summary: \"Theorem 1→Proposition 3 呈现顺序：A5 排除目标场景但未充分强调\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 21\n    action_items: []\n    resolution: \"Proposition 3 已在主文 Section 3, 含完整公式和 Δτ_s\"\n    resolution_round: 21\n\n  - id: \"R19-M1\"\n    summary: \"Assumption (A5) 实践限制被轻描淡写\"\n    category: method\n    severity: info\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 21\n    action_items: []\n    resolution: \"Proposition 3 已在主文充分展示 A5 relaxation\"\n    resolution_round: 21\n\n  - id: \"R19-W6\"\n    summary: \"Finite-sample 传播保证缺失——Theorem 1 到 plug-in estimator 仅有 O_p notation\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 19\n    last_seen_round: 23\n    mentions:\n      - round: 22\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 共识确认技术错误：O_p(κ·n^{-1/2}) 应为 O_p(κ²·n^{-1/2})。\"\n      - round: 22\n        reviewers: [1, 2]\n        note: \"theory.tex L92 修正为 κ²。\"\n      - round: 23\n        reviewers: [1, 2]\n        note: \"主文已修正为 κ²，但 appendix.tex L103 仍用 κ(M_global)（单次幂），且作用于不同对象（Ĉ_s^{-1} vs M_global^{-1} M_s）。论文未解释两个 bound 的区别。Presentation 不一致。\"\n    action_items:\n      - round: 22\n        action: \"theory.tex L92 修正 κ→κ²，含 Neumann expansion 解释\"\n        assigned_to: agent\n        status: done\n      - round: 23\n        action: \"appendix.tex L103 统一为 κ² 或明确说明两个 bound 的适用范围差异\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R19-M6\"\n    summary: \"Algorithm 1 缺收敛标准/最大迭代次数\"\n    category: method\n    severity: info\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 22\n    mentions:\n      - round: 22\n        reviewers: [1, 2]\n        note: \"通过 EB vs Gibbs 不一致问题暴露：Algorithm 1 描述 Gibbs 但代码用 EB。\"\n    action_items:\n      - round: 22\n        action: \"Algorithm 1 改为 EB 流程，Gibbs 降为 appendix 替代方案\"\n        assigned_to: agent\n        status: done\n    resolution: \"Algorithm 1 已改为 EB point estimates (closed-form Dirichlet update)，MCMC 保留为 appendix 验证方案。与 method.tex (<5ms) 和代码一致。\"\n    resolution_round: 22\n\n  - id: \"R22-Q1\"\n    summary: \"Method 说 empirical Bayes (<5ms) 但 Algorithm 1 描述 Gibbs sampler——不一致\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 22\n    mentions:\n      - round: 22\n        reviewers: [1, 2]\n        note: \"代码确认主实验用 EB (estimate_cm_hb_map_eb)，零 Gibbs 代码。\"\n    action_items:\n      - round: 22\n        action: \"Algorithm 1 EB 化 + appendix MCMC 描述统一\"\n        assigned_to: agent\n        status: done\n    resolution: \"Algorithm 1 改为 EB，与 method.tex 和代码一致。Reviewer 验证通过。\"\n    resolution_round: 22\n\n  - id: \"R22-Q2\"\n    summary: \"A3 放松时 'identity remains exact with modified coefficients' 但未给出显式形式\"\n    category: method\n    severity: info\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 22\n    mentions:\n      - round: 22\n        reviewers: [1, 2]\n        note: \"theory.tex L84 声称修正系数存在但未展示。\"\n    action_items:\n      - round: 22\n        action: \"Appendix D 补充 A3 放松显式推导 (M_s Bayes rule form + B_s·1=0 证明)\"\n        assigned_to: agent\n        status: done\n    resolution: \"appendix classimbalance 节新增 eq:ms_imbalanced 显式形式，证明 product form 对任意 p₀ 成立。\"\n    resolution_round: 22\n\n  - id: \"R22-Q3\"\n    summary: \"Cov(π_s, Δτ_s) 在实验中未报告——Corollary 4 实际可用性的关键\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 22\n    mentions:\n      - round: 22\n        reviewers: [1, 2]\n        note: \"应在 semi-synthetic 实验中报告此协方差值。\"\n    action_items:\n      - round: 22\n        action: \"从现有数据提取 Cov(π_s, Δτ_s) 并加入 appendix\"\n        assigned_to: agent\n        status: done\n    resolution: \"appendix A5 violation 节新增 Corollary 4 实证验证：主 grid Cov=0（aggregate bias 抵消），A5 violation Cov=±0.020（predicted ±0.029 与 MC 吻合）。\"\n    resolution_round: 22\n\n  - id: \"R22-Q4\"\n    summary: \"EC-HTE + PPCI 理论兼容性条件不明\"\n    category: method\n    severity: info\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 22\n    mentions:\n      - round: 22\n        reviewers: [1, 2]\n        note: \"LLM 同时标注 covariate 和 outcome 时独立性可能失效。\"\n    action_items:\n      - round: 22\n        action: \"Limitations 补充 PPCI 兼容性讨论\"\n        assigned_to: agent\n        status: done\n    resolution: \"limitations.tex 新增 PPCI 独立性讨论段落。Reviewer 验证通过。\"\n    resolution_round: 22\n\n  - id: \"R20-C1\"\n    summary: \"对称误分类假设 (A2) 限制标题级 'Exact Identity' 声称——非对称情形诊断退化\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 20\n    last_seen_round: 22\n    mentions:\n      - round: 20\n        reviewers: [1, 2]\n        note: \"首次提出。非对称下 R² 降至 0.73。\"\n      - round: 21\n        reviewers: [1, 2]\n        note: \"再次关注。§5.4 添加 matrix vs scalar 区分。\"\n      - round: 22\n        reviewers: [1, 2]\n        note: \"R22 R2 clarified: 恒等式在非对称下仍精确，降级的是诊断 AUC。但 Worker 分析发现 AUC 0.66 来自错误指标（未归一化 matrix score），标量公式实际 AUC=0.96。\"\n    action_items:\n      - round: 20\n        action: \"主文给出 2×2 非对称精确偏差 closed-form\"\n        assigned_to: author\n        status: done\n      - round: 21\n        action: \"experiments.tex §5.4 添加 matrix vs scalar 区分\"\n        assigned_to: director\n        status: done\n      - round: 22\n        action: \"修正 AUC 0.66→0.96（3处），因 0.66 来自错误指标\"\n        assigned_to: agent\n        status: done\n    resolution: \"AUC 0.66 来自未归一化的 raw matrix score，非 Prop 5 标量诊断。标量诊断在非对称下实际 AUC=0.96（48 configs）/ 正确识别全部 harmed subgroups（8 semi-real LLMs, 32 subgroups）。论文 3 处已更新。Reviewer 验证一致性通过。\"\n    resolution_round: 22\n\n  - id: \"R12-M2\"\n    summary: \"Remark 2 与 Theorem 1 假设列表表面矛盾 (A2 地位)\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 12\n    last_seen_round: 22\n    mentions:\n      - round: 22\n        reviewers: [1, 2]\n        note: \"R22 clarified: 恒等式不依赖 A2，标量简化依赖 A2 但 AUC 不降级（0.96）。问题根源已消除。\"\n    action_items:\n      - round: 20\n        action: \"主文给出 2×2 非对称精确偏差 closed-form\"\n        assigned_to: author\n        status: done\n    resolution: \"AUC 0.66→0.96 修正消除了 A2 限制诊断的核心论据。Remark 2 准确描述 A2 仅简化标量形式。\"\n    resolution_round: 22\n\n  - id: \"R21-N1\"\n    summary: \"非对称误分类下诊断准则 AUC 从 0.86 降至 0.65\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 22\n    mentions:\n      - round: 22\n        reviewers: [1, 2]\n        note: \"AUC 0.66 来自错误指标。实际标量诊断 AUC=0.96。4 轮复发问题的根因已消除。\"\n    action_items:\n      - round: 21\n        action: \"experiments.tex §5.4 增加 matrix vs scalar 区分 + 非对称 AUC 数字\"\n        assigned_to: director\n        status: done\n      - round: 22\n        action: \"修正 AUC 0.66→0.96\"\n        assigned_to: agent\n        status: done\n    resolution: \"AUC 0.66 来自错误指标，标量诊断实际 AUC=0.96。论文已更新。\"\n    resolution_round: 22\n\n  # === OPEN / IN_PROGRESS ===\n\n  - id: \"R16-W7\"\n    summary: \"Figure 2 红绿配色色盲不友好\"\n    category: format\n    severity: info\n    status: in_progress\n    first_raised_round: 16\n    last_seen_round: 22\n    mentions:\n      - round: 22\n        reviewers: []\n        note: \"R22 视觉审查仍检测到残留红绿对比。Camera-ready 修复。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R19-C4\"\n    summary: \"CausalForest 集成验证不足——缺 X-learner/BART\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 19\n    last_seen_round: 22\n    mentions:\n      - round: 22\n        reviewers: []\n        note: \"R22 未直接再提。跨估计器（CF + R-learner）是加分项。X-learner/BART 为 rebuttal 准备。\"\n    action_items:\n      - round: 19\n        action: \"Rebuttal 准备: X-learner/BART 跨估计器验证\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R19-W4\"\n    summary: \"HB 优势在 n_expert≥250 时消失但未讨论上限\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 19\n    last_seen_round: 22\n    mentions:\n      - round: 22\n        reviewers: []\n        note: \"R22 未再提及。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R19-W5\"\n    summary: \"缺乏 fully real-data validation (所有实验为 semi-synthetic)\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 19\n    last_seen_round: 23\n    mentions:\n      - round: 22\n        reviewers: [2]\n        note: \"R22 R2 再次强调。R1 REBUT 有力（半合成是因果推断标准范式）。降级为 moderate weakness。Rebuttal 备弹。\"\n      - round: 23\n        reviewers: [1, 2]\n        note: \"R23 两位 Reviewer 共识。R1 指出 A1 by construction 无法验证实际鲁棒性，sensitivity analysis γ_T=0.10 致 coverage 75% 暴露脆弱性。R2 同意并补充：real-data case study 可间接评估 A1 合理性。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R18-SF6\"\n    summary: \"Plugin SE 欠覆盖 93.8%\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 17\n    last_seen_round: 23\n    mentions:\n      - round: 23\n        reviewers: [1, 2]\n        note: \"R1 指出 plug-in SE 不 propagate CM posterior uncertainty。R2 rebuts：bootstrap (B=100) 恢复 ≥95% coverage，HB partial pooling 隐式 regularize。分歧：R2 认为是 implementation choice with empirical justification，非 gap。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R18-M1\"\n    summary: \"EC-HTE wall-clock time 未报告\"\n    category: experiment\n    severity: info\n    status: open\n    first_raised_round: 18\n    last_seen_round: 22\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R17-NLP2\"\n    summary: \"论文对 NLP 社区的价值定位不清\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 17\n    last_seen_round: 23\n    mentions:\n      - round: 22\n        reviewers: [2]\n        note: \"R22 R2 维持。EMNLP 受众适配性是结构性问题。R1 认为时效性足够。评分分歧核心因素。\"\n      - round: 23\n        reviewers: [2]\n        note: \"R2 再次提出 venue fit 问题：论文本质是 causal inference methodology，NLP 内容作为 application domain 而非方法论贡献。R1 未直接讨论 venue fit。\"\n    action_items:\n      - round: 21\n        action: \"experiments.tex §5.2 增加 CivilComments NLP insight 段落\"\n        assigned_to: director\n        status: done\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R17-W2\"\n    summary: \"Scalability to K>>4 未充分讨论\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 17\n    last_seen_round: 23\n    mentions:\n      - round: 22\n        reviewers: []\n        note: \"R22 未再提及。Intro 限定和 Section 5.4 已覆盖。\"\n      - round: 23\n        reviewers: [1, 2]\n        note: \"R1 将 K≤4 作为 applicability limitation 提出。R2 同意并指出 K>4 是否为 estimation noise 还是 structural limitation 不清。但 Intro K≤4 限定和 Section 5.4 已有覆盖，维持 resolved。\"\n    action_items:\n      - round: 21\n        action: \"Intro Contribution 2 增加 K ≤ 4 限定\"\n        assigned_to: director\n        status: done\n    resolution: \"Intro K≤4 限定 + Section 5.4 operating conditions 覆盖。已诚实声明。\"\n    resolution_round: 22\n\n  - id: \"R10-W2\"\n    summary: \"DGP 较简单，无混杂变量\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 10\n    last_seen_round: 22\n    action_items: []\n    resolution: \"Limitations 已补充 confounded DGP scope。R22 未再提及。\"\n    resolution_round: 22\n\n  - id: \"R19-M2\"\n    summary: \"HB 先验敏感性分析不充分\"\n    category: method\n    severity: info\n    status: open\n    first_raised_round: 19\n    last_seen_round: 22\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R19-M3\"\n    summary: \"Bootstrap SE (B=100) 计算成本未讨论\"\n    category: experiment\n    severity: info\n    status: open\n    first_raised_round: 19\n    last_seen_round: 22\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R19-M5\"\n    summary: \"'Semi-synthetic' 术语在 Section 5.1 和 5.3 含义不同\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 19\n    last_seen_round: 22\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R20-C2\"\n    summary: \"相对 Frazis-Loewenstein (2003) 增量贡献未界定\"\n    category: framing\n    severity: critical\n    status: in_progress\n    first_raised_round: 20\n    last_seen_round: 23\n    mentions:\n      - round: 22\n        reviewers: [2]\n        note: \"R22 R2 通过 novelty depth 间接涉及。R1 用 FWL 类比反驳。评分分歧核心因素。\"\n      - round: 23\n        reviewers: [1, 2]\n        note: \"R2 维持 novelty depth concern。R1 提出 FWL 类比进一步限制 novelty 声称。R2 rebuts R1-W6（F-L strawman）认为比较公平——F-L 确实是 practitioners 在异质场景下 naively 使用的标准方法。评分分歧核心。\"\n    action_items:\n      - round: 20\n        action: \"Section 3 明确声明与 F-L 的 nesting 关系\"\n        assigned_to: director\n        status: done\n      - round: 21\n        action: \"Section 3 增加 sign reversal novelty statement\"\n        assigned_to: director\n        status: done\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R20-C3\"\n    summary: \"缺失噪声标签学习核心文献\"\n    category: writing\n    severity: critical\n    status: in_progress\n    first_raised_round: 20\n    last_seen_round: 23\n    mentions:\n      - round: 22\n        reviewers: []\n        note: \"R22 未直接再提。subgroup-dependent vs instance-dependent noise 联系仍为 open action。\"\n      - round: 23\n        reviewers: [2]\n        note: \"R2 指出 subgroup-dependent vs instance-dependent noise 定位仍未充分讨论。Related work 已增加噪声标签段落但深度不足。\"\n    action_items:\n      - round: 20\n        action: \"Related Work 增加噪声标签学习段落\"\n        assigned_to: director\n        status: done\n      - round: 21\n        action: \"深化 subgroup-dependent vs instance-dependent noise 联系\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R20-W1\"\n    summary: \"MC=100 不足以支撑 coverage 声称\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 20\n    last_seen_round: 23\n    mentions:\n      - round: 22\n        reviewers: []\n        note: \"R22 未直接再提。Table 1 caption SE 注释已添加。\"\n      - round: 23\n        reviewers: [1, 2]\n        note: \"R1 重新提出：SE≈2.2pp 使 93% vs 95% coverage 不可区分。R2 同意但认为核心 claims (bias reduction, sign reversal) 不依赖精确 coverage，可降级为 info。\"\n    action_items:\n      - round: 20\n        action: \"关键配置增加至 ≥500 MC runs（rebuttal/camera-ready）\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R20-W2\"\n    summary: \"方法论技术新颖性偏浅\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 20\n    last_seen_round: 23\n    mentions:\n      - round: 22\n        reviewers: [2]\n        note: \"R22 R2 核心论据。R1 用 FWL 类比 REBUT。结构性分歧，rebuttal 论点。\"\n      - round: 23\n        reviewers: [1, 2]\n        note: \"R2 核心 concern：mathematical machinery (matrix CM inversion, subgroup stratification) 是 standard measurement error econometrics。R1 通过 FWL 类比间接支持此观点。两位 Reviewer 共识：贡献是 'careful application of known techniques to important new context'，非 methodological breakthrough。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R20-W3\"\n    summary: \"假设 (A1) 灵敏度分析形式单一\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 20\n    last_seen_round: 23\n    mentions:\n      - round: 23\n        reviewers: [1, 2]\n        note: \"R1 指出 γ_T=0.10 致 coverage 75%，sensitivity analysis 暴露脆弱性而非证明鲁棒性。R2 同意并关联 real-data validation 缺失。\"\n    action_items:\n      - round: 20\n        action: \"增加文本特征 confounding 灵敏度分析（rebuttal/camera-ready）\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R20-M2\"\n    summary: \"Theorem 1 中 'effect-modifier level z' 措辞对 NLP 读者不友好\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 20\n    last_seen_round: 22\n    action_items:\n      - round: 21\n        action: \"theory.tex Theorem 1 后增加 K=2 数值示例\"\n        assigned_to: director\n        status: done\n    resolution: \"数值示例已添加。R22 未再提及。\"\n    resolution_round: 22\n\n  - id: \"R20-M3\"\n    summary: \"Figure 2 'ε-guard' 标注字号偏小\"\n    category: format\n    severity: info\n    status: open\n    first_raised_round: 20\n    last_seen_round: 22\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R21-FIX1\"\n    summary: \"Remark 交叉引用统一\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 22\n    action_items:\n      - round: 21\n        action: \"统一为 \\\\ref{rem:asymmetric}\"\n        assigned_to: director\n        status: done\n    resolution: \"所有引用统一。R22 未再提及。\"\n    resolution_round: 21\n\n  - id: \"R21-N2\"\n    summary: \"NLP 社区适配性不足\"\n    category: framing\n    severity: critical\n    status: in_progress\n    first_raised_round: 21\n    last_seen_round: 23\n    mentions:\n      - round: 22\n        reviewers: [2]\n        note: \"R22 R2 维持。结构性问题。R1 认为时效性足够。\"\n      - round: 23\n        reviewers: [2]\n        note: \"R2 维持：论文本质是 causal inference methodology，NLP 作为 application domain。更适合 JCI/UAI/AISTATS。R1 未直接讨论但同意 novelty 对 EMNLP 偏弱。\"\n    action_items:\n      - round: 21\n        action: \"experiments.tex §5.2 增加 CivilComments NLP insight\"\n        assigned_to: director\n        status: done\n      - round: 21\n        action: \"将 Appendix M 关键发现移入正文（rebuttal/camera-ready）\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R21-W1\"\n    summary: \"Proposition 5 诊断 vs 直接运行 EC-HTE 的增量价值不明\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 21\n    last_seen_round: 22\n    action_items:\n      - round: 21\n        action: \"明确诊断准则的使用场景（rebuttal）\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R21-W2\"\n    summary: \"A3 (P(Z=0)=0.5) 限制性在正文中讨论不足\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 22\n    mentions:\n      - round: 22\n        reviewers: []\n        note: \"R22 未直接再提。limitations.tex 讨论 + appendix A3 显式推导已完成。\"\n    action_items:\n      - round: 21\n        action: \"Limitations 补充 A3 class imbalance 影响讨论\"\n        assigned_to: director\n        status: done\n      - round: 22\n        action: \"Appendix 补充 A3 放松显式推导\"\n        assigned_to: agent\n        status: done\n    resolution: \"Limitations 讨论 + Appendix 显式推导均已完成。\"\n    resolution_round: 22\n\n  - id: \"R21-W3\"\n    summary: \"操作条件称 'framework' 轻微过度声称\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 22\n    action_items:\n      - round: 21\n        action: \"Contribution 2 措辞调整为 'empirical operating guidelines'\"\n        assigned_to: director\n        status: done\n    resolution: \"已调整措辞。R22 确认展示透明。\"\n    resolution_round: 22\n\n  - id: \"R21-W4\"\n    summary: \"Section 3 符号密度对 NLP 读者偏高\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 22\n    action_items:\n      - round: 21\n        action: \"Theorem 1 后增加 K=2 数值示例\"\n        assigned_to: director\n        status: done\n    resolution: \"数值示例已添加。R22 未再提及。\"\n    resolution_round: 22\n\n  - id: \"R21-REF1\"\n    summary: \"遗漏相关工作: Veitch 2020, Wood-Doughty 2018\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 22\n    action_items:\n      - round: 21\n        action: \"Related Work 增加引用\"\n        assigned_to: director\n        status: done\n    resolution: \"引用已添加。R22 未再提及。\"\n    resolution_round: 22\n\n  # === R22 ISSUES (updated for R23) ===\n\n  - id: \"R22-W1\"\n    summary: \"κ-guard 阈值 100 缺乏与 O_p(κ²·n^{-1/2}) 的理论连接\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 22\n    last_seen_round: 23\n    mentions:\n      - round: 22\n        reviewers: [1, 2]\n        note: \"Minor warning。κ 余项已修正为 κ²，但最优阈值推导仍待 rebuttal。\"\n      - round: 23\n        reviewers: [2]\n        note: \"R2 Q3 问 Δπ>0.15 阈值是否有理论推导。R1 认为有理论依据但 REBUT 程度不一。\"\n    action_items:\n      - round: 22\n        action: \"基于 O_p(κ²·n^{-1/2}) 推导理论最优 κ 阈值（rebuttal）\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R22-W2\"\n    summary: \"EB 两阶段低估后验不确定性\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 22\n    last_seen_round: 23\n    mentions:\n      - round: 22\n        reviewers: [1, 2]\n        note: \"Coverage ≥93% 缓解。EB vs full-Bayes coverage 对比为 rebuttal 备弹。\"\n      - round: 23\n        reviewers: [1, 2]\n        note: \"R1 W4 提出 SE 不 propagate CM uncertainty。R2 rebuts 认为 bootstrap 已解决。分歧。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R22-W8\"\n    summary: \"Abstract 信息密度过高（12+ 具体数字）\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 22\n    last_seen_round: 23\n    mentions:\n      - round: 22\n        reviewers: [1, 2]\n        note: \"Minor 共识。Camera-ready 处理。\"\n      - round: 23\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 再次共识。Abstract 读起来像 results table 而非 narrative summary。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R22-W9\"\n    summary: \"Debiasing 术语歧义（fairness vs measurement-error）\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 22\n    last_seen_round: 23\n    mentions:\n      - round: 22\n        reviewers: [1, 2]\n        note: \"Minor 共识。Footnote 1 已有澄清。\"\n      - round: 23\n        reviewers: [2]\n        note: \"R2 再次提出。标题中 'debiasing' 在 NLP 社区有 fairness 歧义。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R22-W10\"\n    summary: \"Per-model R² 低端讨论不足（GPT-4o-mini R²=0.893）\"\n    category: experiment\n    severity: info\n    status: open\n    first_raised_round: 22\n    last_seen_round: 23\n    mentions:\n      - round: 22\n        reviewers: [1, 2]\n        note: \"R1 建议增加回归分析 R² ~ f(FPR, FNR, |FPR-FNR|, n)。Rebuttal 准备。\"\n      - round: 23\n        reviewers: [1, 2]\n        note: \"R1 指出 R²=0.76 削弱 'exact' 说服力（24% 未解释方差）。R2 同意。论文未对低 R² case 做 failure analysis。升级至 warning。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R22-REF1\"\n    summary: \"缺 Filtered PPI 引用 (arXiv:2602.10464)\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 22\n    last_seen_round: 23\n    mentions:\n      - round: 22\n        reviewers: [1, 2]\n        note: \"真实论文，高度相关。Camera-ready 添加。\"\n      - round: 23\n        reviewers: [1, 2]\n        note: \"R2 再次指出。R1 表示无法独立验证但认为 plausible。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  # === R23 NEW ISSUES ===\n\n  - id: \"R23-W1\"\n    summary: \"诊断 AUC=0.86 (symmetric case) 缺乏 decision-consequence 分析\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 23\n    last_seen_round: 23\n    mentions:\n      - round: 23\n        reviewers: [1, 2]\n        note: \"R1 提出：AUC=0.86 在 symmetric case 下有非平凡误判率，但论文未讨论 FP/FN 不对称代价。在 causal inference 中 false negative（遗漏有害 correction）后果远重于 false positive（不必要的 variance 增加）。建议提供 precision/recall breakdown 和 decision threshold tradeoff。R2 同意。\"\n    action_items:\n      - round: 23\n        action: \"补充诊断 AUC 的 precision/recall breakdown 和 decision-theoretic framing（rebuttal）\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R23-W2\"\n    summary: \"'Debiasing hurts' framing 在 moderate heterogeneity 下不成立\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 23\n    last_seen_round: 23\n    mentions:\n      - round: 23\n        reviewers: [1, 2]\n        note: \"R2 提出：标题暗示 debiasing 普遍有害，但论文表明仅在 extreme heterogeneity 下成立。Moderate 配置下 global correction 仍有益。R1 同意 headline claims (7.4×) 仅限 extreme DGP。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R23-Q1\"\n    summary: \"Propensity score estimation error 与 CM estimation error 的交互效应未讨论\"\n    category: method\n    severity: info\n    status: open\n    first_raised_round: 23\n    last_seen_round: 23\n    mentions:\n      - round: 23\n        reviewers: [1, 2]\n        note: \"R2 提出：观察性研究中 treatment assignment 和 outcome measurement 同时含噪。Identity 在 joint estimation error 下是否成立？R1 AGREE。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null"
  }
}
```

</details>

---


### Tool result

_source line 2519 · 2026-05-25T06:31:36.730223+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/review_issues.yaml\", \"bytes\": 28867}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 152
}
```

</details>

---


### Tool call

_source line 2520 · 2026-05-25T06:34:06.239332+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# Round 23 审稿报告\n\n**Venue**: EMNLP 2026 (ARR)  \n**论文**: \"When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects\"  \n**Reviewer**: R1 (技术严谨性 + 实验设计) + R2 (新颖性 + 社区适配性)  \n**交叉回应**: 完成。R1 对 R2 的 11 点：AGREE 8 / REBUT 3。R2 对 R1 的 8 点：AGREE 6 / REBUT 2。  \n**收敛**: 第 1 轮达成。两位 Reviewer 评分一致（3.5），核心关切高度重叠，分歧仅在 2 个 minor 点上（SE propagation 和 F-L 比较 fairness）。\n\n---\n\n## Summary\n\n论文推导了 LLM 标注异质处理效应 (HTE) 中的精确偏差恒等式：当 LLM 分类器的误差率在子群间不均匀时，标准的 global confusion-matrix correction 会引入 δ_s·Δτ/(1−2π̄) 形式的子群偏差，甚至可能反转 CATE 的符号方向。论文提供了层级贝叶斯 per-subgroup 校正方法，刻画了操作条件（Δπ>0.15, n_expert/K≥50, K≤4），并提出了仅基于误差率即可判断 global correction 是否有害的诊断准则。实验覆盖 192 个合成配置和 11 个真实 LLM confusion matrix。\n\n---\n\n## Strengths\n\n**S1: 数学严谨性 [R1+R2]**  \nTheorem 1 的 exact bias identity 提供了 closed-form 分解，无渐近余项，在 symmetric case 下形式优美（δ_s·Δτ/(1−2π̄)），且推广到了任意非对称 confusion matrix 的 full-matrix 形式。合成验证 R²=0.994 (K=2) / 0.97 (K=4)。\n\n**S2: 全面的模拟实验 [R1+R2]**  \n6 Δπ × 8 n_expert × 2 K × 2 DGP = 192 synthetic configs + 16 empirical LLM CMs (8 LLMs × 2 datasets) + 4 NLP tasks (sentiment, hate speech, stance, topic)。Robustness validations 覆盖 8 个条件（asymmetric errors, subgroup misspecification, treatment-dependent misclassification 等），均 ≥89.5% coverage。\n\n**S3: 诚实的操作条件 [R1+R2]**  \nSection 5.4 坦率声明方法局限（K>4 退化、n_expert/K<50 RMSE 超过 global、Δπ<0.15 时无优势），在 ML 论文中少见。Figure budget_compact 清晰展示 crossover point。\n\n**S4: 实用的诊断准则 [R1]**  \nProposition 5 的 Δτ-free diagnostic 允许仅从误差率判断 global correction 是否有害，无需估计处理效应本身。对应用研究者有直接价值。\n\n**S5: 时效性 [R1+R2]**  \nLLM-as-annotator 正快速普及，异质误差率下 global correction 的隐患是一个真实且被低估的风险。Sign-reversal insight 对政策评估、A/B 测试等场景有实际警示作用。\n\n---\n\n## Weaknesses\n\n### Critical\n\n**W1 [R1+R2 共识]: 缺乏 fully real-data validation——所有实验 semi-synthetic，核心假设 A1 由构造满足**\n\n所有实验的 DGP 构造性地满足核心假设（特别是 A1: treatment-independent misclassification），使得论文无法验证方法在假设近似（而非精确）满足时的鲁棒性。Sensitivity analysis (γ_T=0.10 致 coverage 从 95% 降至 75%, Appendix Z.3) 实际上暴露了方法的脆弱性而非证明了鲁棒性——真实 NLP 场景（如 hate speech detection 中 toxic content 系统性影响 LLM accuracy）完全可能达到此量级的 A1 violation。\n\nR2 补充：一个 real-data case study 可间接评估 A1 在实践中的合理性。两位 Reviewer 均认为此为论文的核心缺陷。\n\n**W2 [R1+R2 共识]: 有限样本余项 κ²/κ 在主文与附录间不一致**\n\n- theory.tex L92: \"R_n = O_p(n_expert^{-1/2} · κ(C_s)²)\" —— κ 平方，基于 Neumann expansion\n- appendix.tex L103: \"||M̂_global^{-1} M̂_s − M_global^{-1} M_s|| ≤ κ(M_global) · O_p(n_expert^{-1/2})\" —— κ 一次幂\n\nR2 指出：两个 bound 作用于不同对象（主文 bound Ĉ_s^{-1} perturbation vs 附录 bound M_global^{-1} M_s 乘积 perturbation），所以不是直接数学矛盾。但论文未解释这个区别。在一篇以理论严谨性为核心卖点的论文中，这是明显的 presentation 缺陷。\n\n**W3 [R2 主张, R1 间接支持]: 理论新颖性深度有限**\n\n核心数学 machinery（confusion matrix 的矩阵求逆、子群分层）是 measurement error econometrics 的标准工具。从 Frazis-Loewenstein (2003) scalar attenuation 到 Theorem 1 subgroup-heterogeneous bias identity 的推广在技术上是 relatively straightforward（matrix generalization of scalar case）。Sign-reversal insight 是新的 practical contribution，但数学创新有限。两位 Reviewer 共识：贡献定位为 \"careful application of known techniques to an important new context\"，而非 methodological breakthrough。\n\nR1 通过 Frisch-Waugh-Lovell 类比进一步限制了 novelty 声称——子群分解可视为 FWL partialing 的特例。\n\n### Warning\n\n**W4 [R2 主张, R1 未直接讨论]: EMNLP venue fit 可疑**\n\n论文本质是 causal inference methodology paper。NLP 内容（LLM confusion matrices, text classification tasks）作为 application domain 而非方法论贡献。EMNLP 审稿人可能缺乏 econometrics 背景来充分评估理论贡献，且论文未提供推进 NLP 方法本身的 insight。更适合 JCI / UAI / AISTATS。\n\nR1 未直接讨论 venue fit 但同意 novelty 对 EMNLP 偏弱。CivilComments NLP insight 段落（§5.2）是正面尝试但不改变论文的根本定位。\n\n**W5 [R1 主张, R2 同意]: R²=0.76 lower bound 削弱 \"exact\" framing**\n\nAbstract 声称 R²≥0.97 但括号内即承认 per-model range 0.76–0.99。R²=0.76 意味着 identity 仅解释 76% 的 observed bias variance——对一个 \"exact identity\" 来说，24% 的未解释方差不可忽略。论文未对低 R² 的 LLM 做 failure analysis（是 finite-sample noise 还是 assumption violation？）。\n\n**W6 [R1 主张, R2 同意]: 诊断 AUC=0.86 (symmetric) 缺乏 decision-consequence 分析**\n\nSymmetric case 下 AUC=0.86 意味着非平凡的误判率。更关键的是，论文未讨论 FP/FN 的不对称代价：在 causal inference 中，false negative（诊断说 global correction 安全但实际导致 sign reversal）的后果远重于 false positive（不必要的 variance 增加）。建议提供 precision/recall breakdown 和不同 decision threshold 下的 tradeoff 分析。\n\n**W7 [R1 主张, R2 同意但建议降级]: MC=100 不足以支撑 coverage 声称**\n\nSE≈2.2pp 使得 93% vs 95% coverage 的区分变得模糊。R2 认为核心 claims (bias reduction 7.4×, sign reversal elimination) 不依赖精确 coverage，可降级为 info。但论文确实做出了显式 coverage claims（Table 1, Section 5.3），在 MC=100 的精度下这些 claims 不 well-supported。\n\n**W8 [R2 主张, R1 同意]: \"Debiasing hurts\" framing 有过度声称风险**\n\n标题和整体 framing 暗示 debiasing 普遍有害，但论文表明这仅在 extreme heterogeneity 下成立。Moderate heterogeneity 下 global correction 仍有益（\"methods converge, p>0.05\", experiments.tex L43）。Headline claim 7.4× bias reduction 仅限 extreme DGP。Framing 应更精确地限定适用条件。\n\n**W9 [R2 主张]: Subgroup-dependent vs instance-dependent noise 定位不足**\n\n论文的噪声模型（subgroup-dependent misclassification）介于标准 class-conditional noise 和更一般的 instance-dependent noise 之间，但未在 noisy label learning 文献中定位此关系。Related work 已增加噪声标签段落但深度不足。\n\n### Minor\n\n**W10 [R1 主张, R2 REBUT]: SE 不 propagate CM 估计不确定性**\n\nPlug-in SE 公式 (method.tex L34) 将 Ĉ_s 视为已知量。R2 反驳：bootstrap (B=100) 恢复 ≥95% coverage，HB partial pooling 隐式 regularize CM uncertainty，是 pragmatic implementation choice with empirical justification。两位 Reviewer 分歧——R1 认为 delta method 或 full posterior propagation 更 principled，R2 认为 bootstrap 已足够。\n\n**W11 [R1+R2 共识]: Abstract 信息密度过高**\n\n12+ 具体数字在 6 句话中。Abstract 读起来像 results table 而非 narrative summary。Camera-ready 应精简。\n\n**W12 [R2]: \"Debiasing\" 术语歧义**\n\n标题中 \"debiasing\" 在 NLP 社区有 fairness 歧义。Footnote 1 已澄清但标题仍易误读。\n\n---\n\n## Questions for Authors\n\n**Q1 [R2→R1 AGREE]**: Theorem 1 的 bias identity 与 Frisch-Waugh-Lovell decomposition 的关系？如果子群分解可视为 FWL partialing 的特例，请阐明增量贡献。\n\n**Q2 [R2]**: 在观察性研究中，propensity score estimation error 与 CM estimation error 如何交互？Identity 在 joint estimation error 下是否仍然成立？\n\n**Q3 [R2→R1 REBUT]**: Δπ>0.15 阈值是否有理论推导（例如可从 identity + decision theory 导出），还是纯粹来自模拟网格的经验发现？R1 认为有理论依据。\n\n**Q4 [R1→R2 AGREE]**: Headline claims (7.4× bias reduction, 14.9% sign reversal) 在 moderate heterogeneity 下对应什么数字？如果 moderate 下改善甚微，practitioners 应如何解读贡献的实际影响范围？\n\n---\n\n## Missing References\n\n1. **Filtered PPI** (arXiv:2602.10464) — selective prediction-powered inference with noisy LLM annotations，高度相关。R2 识别；R1 表示无法独立验证但认为 plausible。\n2. **Subgroup-dependent noise 文献** — 论文介于 class-conditional 和 instance-dependent noise 之间，应引用该中间地带的关键工作。\n\n---\n\n## External Review\n\n**状态：未请求。** 本轮未启用 Stanford Agentic Reviewer。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查 Agent 已完成（2026-05-25 06:10–06:14, 耗时 ~4min）。0 critical, **4 warning**, 9 info。\n\n**Warnings:**\n1. **p.9**: Figure 4（bias amplification heatmaps）漂移到 References 页——正文 Section 5.3 引用但 float 越界。建议缩小 Figure 3 或 Table 1 空间，将 Figure 4 拉回 p.8，或移入 Appendix。\n2. **pp.4-6**: 连续 3 页纯文本+公式（理论推导核心段落可豁免但跨度偏长）。建议在 Section 4 前插入概念性小图。\n3. **p.8**: 极度拥挤——Figure 3 + Table 1 + §5.4 + Conclusion + Limitations 全挤一页。Conclusion 仅 ~12 行，Limitations 被压到页底。\n4. **pp.1-8**: 正文仅 4 display items（推荐 5-8），Figure 4 已漂出正文。\n\n**Positive notes**: Figure 2 pipeline 对比图设计清晰（全文最佳 display item）、Table 1 booktabs 格式专业、无 margin 溢出/公式渲染错误/LaTeX 残留、Appendix 22 页排版整洁。\n\n---\n\n## Overall Assessment\n\n**评分：3.5 — Borderline Conference**\n\n| 维度 | 评价 |\n|------|------|\n| Soundness | 强。Exact identity 数学正确，实验全面，操作条件诚实声明。 |\n| Significance | 中。解决真实问题（LLM 异质误差下 global correction 危害），但核心受益群体是 causal inference 应用研究者，非 NLP 方法论研究者。 |\n| Novelty | 弱-中。F-L scalar → subgroup-heterogeneous matrix 推广技术上 straightforward。Sign-reversal practical insight 新颖但数学创新有限。 |\n| Clarity | 中。理论展开清晰，但 κ²/κ 不一致、Abstract 过密、\"debiasing\" 歧义等 presentation 问题存在。 |\n| Venue fit | 弱-中。本质为 causal inference methodology，NLP 内容为 application domain。EMNLP 可行但非最优 venue。 |\n\n**核心判断**：论文在 soundness 上无重大缺陷（R22 修正 AUC 0.66→0.96 消除了最大技术隐患），实验设计全面且操作条件声明透明。但三个结构性问题限制了评分上升空间：(1) 所有实验 semi-synthetic 且 A1 by construction——sensitivity analysis 暴露脆弱性而非鲁棒性；(2) 理论新颖性对 EMNLP 偏浅；(3) venue fit 可疑。论文有被 Findings 接收的潜力，Conference (main) 接收需要在 rebuttal 中有力回应 novelty depth 和 real-data validation。\n\n**Rebuttal 关键问题（按优先级）**：\n1. 是否有 real-data case study 或 A1 violation 的实证证据说明方法在实践中的适用性？\n2. 相对 F-L (2003) 和 standard measurement error correction 的数学增量贡献是什么？FWL 类比如何回应？\n3. R²=0.76 的 failure analysis：原因是什么，是否可预测哪些 LLM 的 identity 拟合较差？\n4. 诊断 AUC=0.86 在 decision-theoretic framework 下的推荐 threshold 是什么？\n\n**两位 Reviewer 一致评分 3.5 (Borderline Conference)**，核心分歧仅在 SE propagation（R1 认为不充分 vs R2 认为 bootstrap 已解决）和 F-L 比较 fairness（R1 认为 strawman vs R2 认为比较合理）两个 minor 点上，不影响 overall assessment。\n\n---\n\n## Detailed Comments\n\n**[theory.tex L92 vs appendix.tex L103]** κ²/κ 不一致。主文正确使用 κ² (Neumann expansion)，附录使用 κ (perturbation bound on M_global^{-1} M_s)。两者作用于不同对象，但论文未说明区别。统一表述或增加解释。\n\n**[abstract.tex L4]** \"R² ≥ 0.97 on synthetic grids (R² = 0.975 in aggregate across 11 real LLM confusion matrices; per-model range 0.76–0.99)\"——括号内的 0.76 下界与 \"exact\" 声称张力过大。建议：(a) 对 R²<0.90 的 LLM 做 failure analysis，(b) 将 per-model range 移至正文 §5.2 讨论而非 abstract。\n\n**[experiments.tex L43]** \"Under moderate heterogeneity, methods converge (p > 0.05)\"——这句话实际上削弱了标题 \"When Debiasing Hurts\" 的普遍性。建议在 Abstract 或 Introduction 中更明确地限定：debiasing hurts **only under extreme subgroup heterogeneity**。\n\n**[method.tex L34]** Plug-in SE formula se_corrected = √(diag(Ĉ_s^{-1} diag(se²) Ĉ_s^{-T}))。虽然 bootstrap 恢复 coverage，但应在方法描述中明确 plug-in SE 的局限性和 bootstrap 的必要性条件（n_expert/K < 50 时）。\n\n**[Proposition 5 诊断]** AUC=0.86 (symmetric) 有实用价值但需 decision-theoretic framing。建议补充：precision@recall=0.95 是多少？推荐的保守 threshold（偏向低 FNR）是什么？\n\n**[Section 5.4 operating conditions]** K≤4 限制。R2 的问题有建设性价值：K>4 退化是因为 n_expert/K 不足（给定足够 expert budget 可解决）还是 hierarchical prior 的结构性局限？答案决定了方法的可扩展性前景。建议在 Limitations 中区分。\n\n**[Layout]** Figure 4 漂出正文是 camera-ready 必须修复的排版问题。p.8 的拥挤程度（Conclusion 仅 ~12 行）给审稿人 \"草率收尾\" 的印象。建议将 Figure 3 或 Table 1 的部分细节移入 Appendix。",
  "project": "ec_hte_llm_annotation",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.5 - Borderline Conference",
  "review_chat_id": "oc_489afd65980834a91024fd48e21d984f"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# Round 23 审稿报告\n\n**Venue**: EMNLP 2026 (ARR)  \n**论文**: \"When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects\"  \n**Reviewer**: R1 (技术严谨性 + 实验设计) + R2 (新颖性 + 社区适配性)  \n**交叉回应**: 完成。R1 对 R2 的 11 点：AGREE 8 / REBUT 3。R2 对 R1 的 8 点：AGREE 6 / REBUT 2。  \n**收敛**: 第 1 轮达成。两位 Reviewer 评分一致（3.5），核心关切高度重叠，分歧仅在 2 个 minor 点上（SE propagation 和 F-L 比较 fairness）。\n\n---\n\n## Summary\n\n论文推导了 LLM 标注异质处理效应 (HTE) 中的精确偏差恒等式：当 LLM 分类器的误差率在子群间不均匀时，标准的 global confusion-matrix correction 会引入 δ_s·Δτ/(1−2π̄) 形式的子群偏差，甚至可能反转 CATE 的符号方向。论文提供了层级贝叶斯 per-subgroup 校正方法，刻画了操作条件（Δπ>0.15, n_expert/K≥50, K≤4），并提出了仅基于误差率即可判断 global correction 是否有害的诊断准则。实验覆盖 192 个合成配置和 11 个真实 LLM confusion matrix。\n\n---\n\n## Strengths\n\n**S1: 数学严谨性 [R1+R2]**  \nTheorem 1 的 exact bias identity 提供了 closed-form 分解，无渐近余项，在 symmetric case 下形式优美（δ_s·Δτ/(1−2π̄)），且推广到了任意非对称 confusion matrix 的 full-matrix 形式。合成验证 R²=0.994 (K=2) / 0.97 (K=4)。\n\n**S2: 全面的模拟实验 [R1+R2]**  \n6 Δπ × 8 n_expert × 2 K × 2 DGP = 192 synthetic configs + 16 empirical LLM CMs (8 LLMs × 2 datasets) + 4 NLP tasks (sentiment, hate speech, stance, topic)。Robustness validations 覆盖 8 个条件（asymmetric errors, subgroup misspecification, treatment-dependent misclassification 等），均 ≥89.5% coverage。\n\n**S3: 诚实的操作条件 [R1+R2]**  \nSection 5.4 坦率声明方法局限（K>4 退化、n_expert/K<50 RMSE 超过 global、Δπ<0.15 时无优势），在 ML 论文中少见。Figure budget_compact 清晰展示 crossover point。\n\n**S4: 实用的诊断准则 [R1]**  \nProposition 5 的 Δτ-free diagnostic 允许仅从误差率判断 global correction 是否有害，无需估计处理效应本身。对应用研究者有直接价值。\n\n**S5: 时效性 [R1+R2]**  \nLLM-as-annotator 正快速普及，异质误差率下 global correction 的隐患是一个真实且被低估的风险。Sign-reversal insight 对政策评估、A/B 测试等场景有实际警示作用。\n\n---\n\n## Weaknesses\n\n### Critical\n\n**W1 [R1+R2 共识]: 缺乏 fully real-data validation——所有实验 semi-synthetic，核心假设 A1 由构造满足**\n\n所有实验的 DGP 构造性地满足核心假设（特别是 A1: treatment-independent misclassification），使得论文无法验证方法在假设近似（而非精确）满足时的鲁棒性。Sensitivity analysis (γ_T=0.10 致 coverage 从 95% 降至 75%, Appendix Z.3) 实际上暴露了方法的脆弱性而非证明了鲁棒性——真实 NLP 场景（如 hate speech detection 中 toxic content 系统性影响 LLM accuracy）完全可能达到此量级的 A1 violation。\n\nR2 补充：一个 real-data case study 可间接评估 A1 在实践中的合理性。两位 Reviewer 均认为此为论文的核心缺陷。\n\n**W2 [R1+R2 共识]: 有限样本余项 κ²/κ 在主文与附录间不一致**\n\n- theory.tex L92: \"R_n = O_p(n_expert^{-1/2} · κ(C_s)²)\" —— κ 平方，基于 Neumann expansion\n- appendix.tex L103: \"||M̂_global^{-1} M̂_s − M_global^{-1} M_s|| ≤ κ(M_global) · O_p(n_expert^{-1/2})\" —— κ 一次幂\n\nR2 指出：两个 bound 作用于不同对象（主文 bound Ĉ_s^{-1} perturbation vs 附录 bound M_global^{-1} M_s 乘积 perturbation），所以不是直接数学矛盾。但论文未解释这个区别。在一篇以理论严谨性为核心卖点的论文中，这是明显的 presentation 缺陷。\n\n**W3 [R2 主张, R1 间接支持]: 理论新颖性深度有限**\n\n核心数学 machinery（confusion matrix 的矩阵求逆、子群分层）是 measurement error econometrics 的标准工具。从 Frazis-Loewenstein (2003) scalar attenuation 到 Theorem 1 subgroup-heterogeneous bias identity 的推广在技术上是 relatively straightforward（matrix generalization of scalar case）。Sign-reversal insight 是新的 practical contribution，但数学创新有限。两位 Reviewer 共识：贡献定位为 \"careful application of known techniques to an important new context\"，而非 methodological breakthrough。\n\nR1 通过 Frisch-Waugh-Lovell 类比进一步限制了 novelty 声称——子群分解可视为 FWL partialing 的特例。\n\n### Warning\n\n**W4 [R2 主张, R1 未直接讨论]: EMNLP venue fit 可疑**\n\n论文本质是 causal inference methodology paper。NLP 内容（LLM confusion matrices, text classification tasks）作为 application domain 而非方法论贡献。EMNLP 审稿人可能缺乏 econometrics 背景来充分评估理论贡献，且论文未提供推进 NLP 方法本身的 insight。更适合 JCI / UAI / AISTATS。\n\nR1 未直接讨论 venue fit 但同意 novelty 对 EMNLP 偏弱。CivilComments NLP insight 段落（§5.2）是正面尝试但不改变论文的根本定位。\n\n**W5 [R1 主张, R2 同意]: R²=0.76 lower bound 削弱 \"exact\" framing**\n\nAbstract 声称 R²≥0.97 但括号内即承认 per-model range 0.76–0.99。R²=0.76 意味着 identity 仅解释 76% 的 observed bias variance——对一个 \"exact identity\" 来说，24% 的未解释方差不可忽略。论文未对低 R² 的 LLM 做 failure analysis（是 finite-sample noise 还是 assumption violation？）。\n\n**W6 [R1 主张, R2 同意]: 诊断 AUC=0.86 (symmetric) 缺乏 decision-consequence 分析**\n\nSymmetric case 下 AUC=0.86 意味着非平凡的误判率。更关键的是，论文未讨论 FP/FN 的不对称代价：在 causal inference 中，false negative（诊断说 global correction 安全但实际导致 sign reversal）的后果远重于 false positive（不必要的 variance 增加）。建议提供 precision/recall breakdown 和不同 decision threshold 下的 tradeoff 分析。\n\n**W7 [R1 主张, R2 同意但建议降级]: MC=100 不足以支撑 coverage 声称**\n\nSE≈2.2pp 使得 93% vs 95% coverage 的区分变得模糊。R2 认为核心 claims (bias reduction 7.4×, sign reversal elimination) 不依赖精确 coverage，可降级为 info。但论文确实做出了显式 coverage claims（Table 1, Section 5.3），在 MC=100 的精度下这些 claims 不 well-supported。\n\n**W8 [R2 主张, R1 同意]: \"Debiasing hurts\" framing 有过度声称风险**\n\n标题和整体 framing 暗示 debiasing 普遍有害，但论文表明这仅在 extreme heterogeneity 下成立。Moderate heterogeneity 下 global correction 仍有益（\"methods converge, p>0.05\", experiments.tex L43）。Headline claim 7.4× bias reduction 仅限 extreme DGP。Framing 应更精确地限定适用条件。\n\n**W9 [R2 主张]: Subgroup-dependent vs instance-dependent noise 定位不足**\n\n论文的噪声模型（subgroup-dependent misclassification）介于标准 class-conditional noise 和更一般的 instance-dependent noise 之间，但未在 noisy label learning 文献中定位此关系。Related work 已增加噪声标签段落但深度不足。\n\n### Minor\n\n**W10 [R1 主张, R2 REBUT]: SE 不 propagate CM 估计不确定性**\n\nPlug-in SE 公式 (method.tex L34) 将 Ĉ_s 视为已知量。R2 反驳：bootstrap (B=100) 恢复 ≥95% coverage，HB partial pooling 隐式 regularize CM uncertainty，是 pragmatic implementation choice with empirical justification。两位 Reviewer 分歧——R1 认为 delta method 或 full posterior propagation 更 principled，R2 认为 bootstrap 已足够。\n\n**W11 [R1+R2 共识]: Abstract 信息密度过高**\n\n12+ 具体数字在 6 句话中。Abstract 读起来像 results table 而非 narrative summary。Camera-ready 应精简。\n\n**W12 [R2]: \"Debiasing\" 术语歧义**\n\n标题中 \"debiasing\" 在 NLP 社区有 fairness 歧义。Footnote 1 已澄清但标题仍易误读。\n\n---\n\n## Questions for Authors\n\n**Q1 [R2→R1 AGREE]**: Theorem 1 的 bias identity 与 Frisch-Waugh-Lovell decomposition 的关系？如果子群分解可视为 FWL partialing 的特例，请阐明增量贡献。\n\n**Q2 [R2]**: 在观察性研究中，propensity score estimation error 与 CM estimation error 如何交互？Identity 在 joint estimation error 下是否仍然成立？\n\n**Q3 [R2→R1 REBUT]**: Δπ>0.15 阈值是否有理论推导（例如可从 identity + decision theory 导出），还是纯粹来自模拟网格的经验发现？R1 认为有理论依据。\n\n**Q4 [R1→R2 AGREE]**: Headline claims (7.4× bias reduction, 14.9% sign reversal) 在 moderate heterogeneity 下对应什么数字？如果 moderate 下改善甚微，practitioners 应如何解读贡献的实际影响范围？\n\n---\n\n## Missing References\n\n1. **Filtered PPI** (arXiv:2602.10464) — selective prediction-powered inference with noisy LLM annotations，高度相关。R2 识别；R1 表示无法独立验证但认为 plausible。\n2. **Subgroup-dependent noise 文献** — 论文介于 class-conditional 和 instance-dependent noise 之间，应引用该中间地带的关键工作。\n\n---\n\n## External Review\n\n**状态：未请求。** 本轮未启用 Stanford Agentic Reviewer。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查 Agent 已完成（2026-05-25 06:10–06:14, 耗时 ~4min）。0 critical, **4 warning**, 9 info。\n\n**Warnings:**\n1. **p.9**: Figure 4（bias amplification heatmaps）漂移到 References 页——正文 Section 5.3 引用但 float 越界。建议缩小 Figure 3 或 Table 1 空间，将 Figure 4 拉回 p.8，或移入 Appendix。\n2. **pp.4-6**: 连续 3 页纯文本+公式（理论推导核心段落可豁免但跨度偏长）。建议在 Section 4 前插入概念性小图。\n3. **p.8**: 极度拥挤——Figure 3 + Table 1 + §5.4 + Conclusion + Limitations 全挤一页。Conclusion 仅 ~12 行，Limitations 被压到页底。\n4. **pp.1-8**: 正文仅 4 display items（推荐 5-8），Figure 4 已漂出正文。\n\n**Positive notes**: Figure 2 pipeline 对比图设计清晰（全文最佳 display item）、Table 1 booktabs 格式专业、无 margin 溢出/公式渲染错误/LaTeX 残留、Appendix 22 页排版整洁。\n\n---\n\n## Overall Assessment\n\n**评分：3.5 — Borderline Conference**\n\n| 维度 | 评价 |\n|------|------|\n| Soundness | 强。Exact identity 数学正确，实验全面，操作条件诚实声明。 |\n| Significance | 中。解决真实问题（LLM 异质误差下 global correction 危害），但核心受益群体是 causal inference 应用研究者，非 NLP 方法论研究者。 |\n| Novelty | 弱-中。F-L scalar → subgroup-heterogeneous matrix 推广技术上 straightforward。Sign-reversal practical insight 新颖但数学创新有限。 |\n| Clarity | 中。理论展开清晰，但 κ²/κ 不一致、Abstract 过密、\"debiasing\" 歧义等 presentation 问题存在。 |\n| Venue fit | 弱-中。本质为 causal inference methodology，NLP 内容为 application domain。EMNLP 可行但非最优 venue。 |\n\n**核心判断**：论文在 soundness 上无重大缺陷（R22 修正 AUC 0.66→0.96 消除了最大技术隐患），实验设计全面且操作条件声明透明。但三个结构性问题限制了评分上升空间：(1) 所有实验 semi-synthetic 且 A1 by construction——sensitivity analysis 暴露脆弱性而非鲁棒性；(2) 理论新颖性对 EMNLP 偏浅；(3) venue fit 可疑。论文有被 Findings 接收的潜力，Conference (main) 接收需要在 rebuttal 中有力回应 novelty depth 和 real-data validation。\n\n**Rebuttal 关键问题（按优先级）**：\n1. 是否有 real-data case study 或 A1 violation 的实证证据说明方法在实践中的适用性？\n2. 相对 F-L (2003) 和 standard measurement error correction 的数学增量贡献是什么？FWL 类比如何回应？\n3. R²=0.76 的 failure analysis：原因是什么，是否可预测哪些 LLM 的 identity 拟合较差？\n4. 诊断 AUC=0.86 在 decision-theoretic framework 下的推荐 threshold 是什么？\n\n**两位 Reviewer 一致评分 3.5 (Borderline Conference)**，核心分歧仅在 SE propagation（R1 认为不充分 vs R2 认为 bootstrap 已解决）和 F-L 比较 fairness（R1 认为 strawman vs R2 认为比较合理）两个 minor 点上，不影响 overall assessment。\n\n---\n\n## Detailed Comments\n\n**[theory.tex L92 vs appendix.tex L103]** κ²/κ 不一致。主文正确使用 κ² (Neumann expansion)，附录使用 κ (perturbation bound on M_global^{-1} M_s)。两者作用于不同对象，但论文未说明区别。统一表述或增加解释。\n\n**[abstract.tex L4]** \"R² ≥ 0.97 on synthetic grids (R² = 0.975 in aggregate across 11 real LLM confusion matrices; per-model range 0.76–0.99)\"——括号内的 0.76 下界与 \"exact\" 声称张力过大。建议：(a) 对 R²<0.90 的 LLM 做 failure analysis，(b) 将 per-model range 移至正文 §5.2 讨论而非 abstract。\n\n**[experiments.tex L43]** \"Under moderate heterogeneity, methods converge (p > 0.05)\"——这句话实际上削弱了标题 \"When Debiasing Hurts\" 的普遍性。建议在 Abstract 或 Introduction 中更明确地限定：debiasing hurts **only under extreme subgroup heterogeneity**。\n\n**[method.tex L34]** Plug-in SE formula se_corrected = √(diag(Ĉ_s^{-1} diag(se²) Ĉ_s^{-T}))。虽然 bootstrap 恢复 coverage，但应在方法描述中明确 plug-in SE 的局限性和 bootstrap 的必要性条件（n_expert/K < 50 时）。\n\n**[Proposition 5 诊断]** AUC=0.86 (symmetric) 有实用价值但需 decision-theoretic framing。建议补充：precision@recall=0.95 是多少？推荐的保守 threshold（偏向低 FNR）是什么？\n\n**[Section 5.4 operating conditions]** K≤4 限制。R2 的问题有建设性价值：K>4 退化是因为 n_expert/K 不足（给定足够 expert budget 可解决）还是 hierarchical prior 的结构性局限？答案决定了方法的可扩展性前景。建议在 Limitations 中区分。\n\n**[Layout]** Figure 4 漂出正文是 camera-ready 必须修复的排版问题。p.8 的拥挤程度（Conclusion 仅 ~12 行）给审稿人 \"草率收尾\" 的印象。建议将 Figure 3 或 Table 1 的部分细节移入 Appendix。",
    "project": "ec_hte_llm_annotation",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.5 - Borderline Conference",
    "review_chat_id": "oc_489afd65980834a91024fd48e21d984f"
  }
}
```

</details>

---


### Tool result

_source line 2521 · 2026-05-25T06:34:10.758929+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_6b114d432b35fe7a1c2143457ae85b08:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4519
}
```

</details>

---


### Assistant

_source line 2522 · 2026-05-25T06:34:25.713378+00:00_

Round 23 审稿报告已投递。

**汇总**：
- **评分**：3.5 (Borderline Conference)，两位 Reviewer 一致
- **核心共识**：(1) 缺乏 real-data validation + A1 sensitivity 暴露脆弱性；(2) 理论新颖性对 EMNLP 偏浅（F-L → subgroup 推广技术上 straightforward）；(3) R²=0.76 削弱 "exact" framing
- **交叉分歧**（minor）：SE propagation（R2 认为 bootstrap 已解决）、F-L 比较公平性（R2 认为合理）
- **新增 issues**：R23-W1（诊断 AUC 缺 decision-consequence）、R23-W2（framing 过度声称）、R23-Q1（propensity × CM error 交互）
- **重开 issue**：R19-W6（κ²/κ 不一致，主文已修但附录未同步）
- **外部审稿**：未请求
- **视觉审查**：已完成，4 warnings（Figure 4 漂移、pp.4-6 无图、p.8 拥挤、display item 密度低）

Issue tracker 已同步更新至 R23。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director"
}
```

</details>

---


## Round 196

## Round 196

66 recorded events


### User

_source line 2523 · 2026-05-25T21:14:10.738418+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: ec_hte_llm_annotation
- 论文路径: /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: Main
- 截止日期: 2026-06-15
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 2524 · 2026-05-25T21:14:16.076948+00:00_

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
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 2525 · 2026-05-25T21:14:16.127953+00:00_

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
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 2526 · 2026-05-25T21:14:23.070343+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,read_project_file,dispatch_visual_check,request_external_review,get_external_review_status,director_post_to_reviewer,submit_review_report_to_research_director,get_visual_check_status,update_review_issues,read_local_file",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,read_project_file,dispatch_visual_check,request_external_review,get_external_review_status,director_post_to_reviewer,submit_review_report_to_research_director,get_visual_check_status,update_review_issues,read_local_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 2527 · 2026-05-25T21:14:23.120951+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2528 · 2026-05-25T21:14:26.484080+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_local_file",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_local_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 2529 · 2026-05-25T21:14:26.534687+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2530 · 2026-05-25T21:14:31.604019+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "ec_hte_llm_annotation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "ec_hte_llm_annotation"
  }
}
```

</details>

---


### Tool result

_source line 2531 · 2026-05-25T21:14:33.060144+00:00_

{"result":"# 项目 ec_hte_llm_annotation 概况\n\n## 实验状态 (43 个)\n\n- **exp-015**: DONE (negative) — \n- **exp-008**: DONE (success) — \n- **exp-004**: DONE (success) — \n- **exp-010**: DONE (success) — \n- **exp-014**: DONE (success) — \n- **exp-013**: DONE (success) — \n- **exp-012**: DONE (success) — \n- **exp-006**: DONE (success) — \n- **exp-007b**: DONE (killed) — \n- **exp-003**: DONE (success) — \n- **exp-011**: DONE (success) — \n- **exp-005**: DONE (success) — \n- **exp-007**: DONE (success) — \n- **exp-001**: DONE (success) — \n- **exp-002**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-24\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- exp-027b: Under K=2 extreme (π=[0.05,0.25], n_expert=250) — the exact configuration producing 83-85% coverage in the paper — CausalForest oracle coverage with true C_s will determine whether the gap is from CF inherent SE under-calibration or M⁻¹ amplification of CM estimation error（准备中）\n- exp-027: CausalForest coverage gap (83-85% vs nominal 95%) is attributable to CF's inherent SE calibration, not CM estimation error: using true C_s (oracle CM) will produce similar ~83-85% coverage as estimated Ĉ_s, while the DIM estimator with true C_s achieves ~95% — isolating the source of under-coverage（准备中）\n\n## 近期结论\n- **exp-041** (negative): Under asymmetric misclassification (FPR≠FNR, ratio 1:2 to 1:5 and reverse), the bias identity retains R²≥0.95 and EC-HTE maintains coverage ≥93% across 48 configurations (6 FPR/FNR ratios × 2 K × 4 Δπ), while the symmetric diagnostic AUC degrades monotonically with FPR/FNR ratio — quantifying the exact diagnostic accuracy loss curve under asymmetry.\n  [exp041_asymmetric_grid](/api/workspace-files/projects/ec_hte_llm_annotation/artifacts/exp-041/data/exp041_asymmetric_grid.csv) | [exp041_asymmetric_summary](/api/workspace-files/projects/ec_hte_llm_annotation/artifacts/exp-041/data/exp041_asymmetric_summary.csv) | [exp041_asymmetric_mc_script](/api/workspace-files/projects/e
…[truncated 751 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1456
}
```

</details>

---


### Tool call

_source line 2532 · 2026-05-25T21:14:33.512124+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/main.tex",
  "limit": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/main.tex",
    "limit": "150"
  }
}
```

</details>

---


### Tool result

_source line 2533 · 2026-05-25T21:14:34.014623+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	\usepackage{inconsolata}
9	
10	\usepackage{amsmath,amssymb,amsthm}
11	\usepackage{graphicx}
12	\usepackage{booktabs}
13	\usepackage{multirow}
14	\usepackage{makecell}
15	\usepackage{enumitem}
16	\usepackage{algorithm}
17	\usepackage{algpseudocode}
18	
19	\newtheorem{theorem}{Theorem}
20	\newtheorem{corollary}[theorem]{Corollary}
21	\newtheorem{proposition}[theorem]{Proposition}
22	\newtheorem{remark}[theorem]{Remark}
23	
24	\title{When Debiasing Hurts: An Exact Bias Identity\\for LLM-Annotated Treatment Effects}
25	
26	\author{Anonymous}
27	
28	\begin{document}
29	\maketitle
30	
31	\input{abstract}
32	
33	\input{introduction}
34	
35	\input{related_work}
36	
37	\input{theory}
38	
39	\input{method}
40	
41	\input{experiments}
42	
43	\input{conclusion}
44	
45	\input{limitations}
46	
47	\bibliography{references}
48	
49	\appendix
50	\input{appendix}
51	
52	%\input{checklist}
53	
54	\end{document}
55	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 2534 · 2026-05-25T21:14:34.466653+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "ec_hte_llm_annotation",
  "file": "paper_checklist.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "ec_hte_llm_annotation",
    "file": "paper_checklist.yaml"
  }
}
```

</details>

---


### Tool result

_source line 2535 · 2026-05-25T21:14:34.818403+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'ec_hte_llm_annotation'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 2536 · 2026-05-25T21:14:34.818876+00:00_

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
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
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

_source line 2537 · 2026-05-25T21:14:34.920257+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "ToolSearch",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 2538 · 2026-05-25T21:14:41.545134+00:00_

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
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission guidelines ARR"
  }
}
```

</details>

---


### Tool call

_source line 2539 · 2026-05-25T21:14:43.001372+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 2540 · 2026-05-25T21:14:43.503650+00:00_

1	\begin{abstract}
2	Large language models increasingly replace human annotators in computational social science, yet their error rates can vary by up to $5\times$ across demographic and text-feature subgroups.
3	When these noisy labels serve as effect modifiers in heterogeneous treatment effect (HTE) analysis, the standard remedy---estimating a single confusion matrix and applying its inverse uniformly---is widely trusted to remove bias.
4	We prove it can do the opposite.
5	We derive an exact bias identity showing that global correction introduces a subgroup-level bias proportional to the interaction of error-rate deviation and effect heterogeneity, a product structure invisible to any pooled analysis.
6	This identity reveals that correction reverses estimated causal effect signs in 14.9\% of configurations and amplifies bias across all eight real LLMs tested.
7	A diagnostic corollary flags harmful correction from error rates alone, without estimating treatment effects.
8	Guided by the identity, we propose EC-HTE, a per-subgroup correction via hierarchical Bayesian confusion matrix estimation that reduces bias by $7.4\times$ under extreme heterogeneity, with clear operating conditions ($\Delta\pi > 0.15$, $n_{\text{expert}} \geq 250$, $K \leq 4$) and validated across 11 LLM--dataset combinations spanning four NLP tasks\footnote{Code and data: \url{https://anonymous.4open.science/r/ec_hte_llm_annotation-4CC8/}.}.
9	\end{abstract}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 2541 · 2026-05-25T21:14:43.504191+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 2542 · 2026-05-25T21:14:44.415463+00:00_

1	\begin{figure*}[t]
2	\centering
3	\includegraphics[width=\textwidth]{figures/fig_combined_overview.pdf}
4	\caption{Overview. (a)~Global correction over/under-corrects subgroups with heterogeneous error rates, introducing bias $\delta_s \cdot \Delta\tau / (1{-}2\bar{\pi})$ that reverses CATE sign in 14.9\% of configurations. (b)~\textit{Top (rose):} standard pipeline applies a pooled confusion matrix uniformly; \textit{bottom (teal):} EC-HTE estimates per-subgroup matrices via hierarchical Bayes, applies stratified inversion with a $\kappa$-guard, and propagates uncertainty.}
5	\label{fig:method_overview}
6	\end{figure*}
7	
8	\section{Introduction}
9	\label{sec:intro}
10	
11	Consider estimating whether a content moderation policy reduces hate speech differently across demographic groups, using GPT-4 to classify thousands of posts.
12	After standard confusion-matrix correction, the analysis concludes the policy \emph{increases} hate speech among younger users, but the true effect is protective.
13	This sign reversal is not an edge case.
14	
15	Large language models (LLMs) now routinely replace human annotators in computational social science, producing labels for sentiment, hate speech, stance, and political discourse at costs orders of magnitude below manual coding~\cite{gilardi2023chatgpt,tornberg2024chatgpt,ziems2024nlp,tan2024llm}.
16	When these labels serve as effect modifiers in heterogeneous treatment effect (HTE) analysis, the standard correction protocol\footnote{Throughout, ``debiasing'' refers to correction of annotation measurement-error bias, not algorithmic fairness debiasing.} is straightforward: validate a sample against expert annotations, estimate a confusion matrix, and apply its inverse uniformly to correct conditional average treatment effect (CATE) estimates.
17	Yet LLM annotations are not uniformly accurate: \citet{ashwin2025bias} document error rates varying by up to 5$\times$ across demographic subgroups; in our pilot, GPT-4.1 error rates ra
…[truncated 2494 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "elapsed_ms": 911
}
```

</details>

---


### Tool call

_source line 2543 · 2026-05-25T21:14:44.416742+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool call

_source line 2544 · 2026-05-25T21:14:44.417134+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "ec_hte_llm_annotation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "ec_hte_llm_annotation"
  }
}
```

</details>

---


### Tool result

_source line 2545 · 2026-05-25T21:14:44.467563+00:00_

1	\section{Related Work}
2	\label{sec:related}
3	
4	Classical measurement error correction can amplify MSE under misspecification~\cite{fuller1987measurement,carroll2006measurement}; \citet{frazis2003estimating} derive scalar attenuation for homogeneous errors, which Theorem~\ref{thm:bias_identity} generalizes to heterogeneous settings.
5	HTE estimators~\cite{athey2016recursive,wager2018causal,chernozhukov2018dml} assume error-free covariates; LLM error rates vary by up to $5\times$ across subgroups~\cite{ashwin2025bias}.
6	PPI~\cite{angelopoulos2023ppi}, DSL~\cite{egami2023dsl}, PPCI~\cite{sui2026ppci}, and ForestIV~\cite{bu2023forestiv} correct population-level or outcome-side error assuming homogeneous prediction quality; none addresses effect modifier misclassification.
7	Extended discussion appears in Appendix~\ref{app:related}.
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 2546 · 2026-05-25T21:14:57.068608+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines ARR"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"Submission Guide","url":"https://nlp4climate.github.io/submissionguide/"},{"title":"EMNLP 2026 LaTeX Template | ACL Style Files & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/emnlp"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"}]

Based on the search results, here are the key submission guidelines for EMNLP 2026 regarding ARR:

## Submission Overview
EMNLP 2026 invites the submission of long and short papers featuring substantial, original, and unpublished research on empirical methods for Natural Language Processing.

## Important Dates
The ARR submission deadline for long and short papers is May 25, 2026, with the reviewer registration deadline for all authors on May 27, 2026, author response and author-reviewer discussion from July 7-13, 2026, meta review released July 30, 2026, and the EMNLP commitment deadline on August 2, 2026.

## ARR Submission Policy
All submissions go through ACL Rolling Review (ARR), with the ARR submission deadline of May 25, 2026. Given that the ARR 2026 May cycle is aligned with two conferences (EMNLP and AACL), authors will need to explicitly declare which conference they intend to commit to at submission time, and this choice will be binding for EMNLP 2026.

## Paper Format and Requirements
The format is two-column with an 8-page limit for long papers and a 4-page limit for s
…[truncated 548 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "WebSearch",
  "elapsed_ms": 15523
}
```

</details>

---


### Tool result

_source line 2547 · 2026-05-25T21:14:57.220113+00:00_

{"result":"# 项目 ec_hte_llm_annotation 概况\n\n## 实验状态 (43 个)\n\n- **exp-015**: DONE (negative) — \n- **exp-008**: DONE (success) — \n- **exp-004**: DONE (success) — \n- **exp-010**: DONE (success) — \n- **exp-014**: DONE (success) — \n- **exp-013**: DONE (success) — \n- **exp-012**: DONE (success) — \n- **exp-006**: DONE (success) — \n- **exp-007b**: DONE (killed) — \n- **exp-003**: DONE (success) — \n- **exp-011**: DONE (success) — \n- **exp-005**: DONE (success) — \n- **exp-007**: DONE (success) — \n- **exp-001**: DONE (success) — \n- **exp-002**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-24\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- exp-027b: Under K=2 extreme (π=[0.05,0.25], n_expert=250) — the exact configuration producing 83-85% coverage in the paper — CausalForest oracle coverage with true C_s will determine whether the gap is from CF inherent SE under-calibration or M⁻¹ amplification of CM estimation error（准备中）\n- exp-027: CausalForest coverage gap (83-85% vs nominal 95%) is attributable to CF's inherent SE calibration, not CM estimation error: using true C_s (oracle CM) will produce similar ~83-85% coverage as estimated Ĉ_s, while the DIM estimator with true C_s achieves ~95% — isolating the source of under-coverage（准备中）\n\n## 近期结论\n- **exp-041** (negative): Under asymmetric misclassification (FPR≠FNR, ratio 1:2 to 1:5 and reverse), the bias identity retains R²≥0.95 and EC-HTE maintains coverage ≥93% across 48 configurations (6 FPR/FNR ratios × 2 K × 4 Δπ), while the symmetric diagnostic AUC degrades monotonically with FPR/FNR ratio — quantifying the exact diagnostic accuracy loss curve under asymmetry.\n  [exp041_asymmetric_grid](/api/workspace-files/projects/ec_hte_llm_annotation/artifacts/exp-041/data/exp041_asymmetric_grid.csv) | [exp041_asymmetric_summary](/api/workspace-files/projects/ec_hte_llm_annotation/artifacts/exp-041/data/exp041_asymmetric_summary.csv) | [exp041_asymmetric_mc_script](/api/workspace-files/projects/e
…[truncated 751 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 12802
}
```

</details>

---


### Tool call

_source line 2548 · 2026-05-25T21:15:02.892483+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/theory.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/theory.tex"
  }
}
```

</details>

---


### Tool result

_source line 2549 · 2026-05-25T21:15:03.344650+00:00_

1	% Requires preamble: \usepackage{amsthm,amsmath,amssymb}
2	% and: \newtheorem{theorem}{Theorem}
3	%      \newtheorem{corollary}[theorem]{Corollary}
4	%      \newtheorem{proposition}[theorem]{Proposition}
5	
6	\section{Bias Decomposition: When Debiasing Hurts}
7	\label{sec:theory}
8	
9	We formalize the bias that global misclassification correction introduces when subgroup error rates are heterogeneous.
10	Consider estimating the conditional average treatment effect (CATE) $\tau(z) = \mathbb{E}[Y(1) - Y(0) \mid Z = z]$, where $Z \in \{0, 1\}$ is a binary effect modifier observed only through a noisy annotation $\hat{Z}$.
11	The population consists of $K$ subgroups $S \in \{1, \ldots, K\}$ with weights $w_s = P(S{=}s)$, each characterized by a $2 \times 2$ confusion matrix $C_s$ with symmetric error rate $\pi_s = P(\hat{Z} \neq Z \mid S{=}s)$.
12	Standard practice estimates a single confusion matrix $\bar{C} = \sum_s w_s C_s$ from expert annotations and applies its inverse uniformly to all observations, with pooled error rate $\bar{\pi} = \sum_s w_s \pi_s$.
13	We show that when error rates vary across subgroups, this global procedure introduces a bias with an exact product form.
14	
15	We state five assumptions maintained throughout.
16	%
17	\begin{itemize}
18	\item[\textbf{(A1)}] \textit{Conditional independence:} misclassification depends only on the true label $Z$ and subgroup $S$, not on potential outcomes $Y(0), Y(1)$.
19	\item[\textbf{(A2)}] \textit{Symmetric misclassification (expository simplification):} $P(\hat{Z}{=}1 \mid Z{=}0, S{=}s) = P(\hat{Z}{=}0 \mid Z{=}1, S{=}s) = \pi_s$ for all $s$. Used only to reduce $[B_s]_{z,1}$ to the scalar $\pm\delta_s/(1{-}2\bar{\pi})$; the product-form identity holds for arbitrary asymmetric matrices without~(A2) (Remark~\ref{rem:asymmetric}).
20	\item[\textbf{(A3)}] \textit{Balanced effect modifier:} $P(Z{=}0) = P(Z{=}1) = 0.5$. This simplifies the exposition; we discuss relaxation below.
21	\item[\textbf{(A4)}] \textit{N
…[truncated 7615 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 2550 · 2026-05-25T21:15:03.345025+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 2551 · 2026-05-25T21:15:03.847235+00:00_

1	\section{Correction Prescribed by the Identity}
2	\label{sec:method}
3	
4	Theorem~\ref{thm:bias_identity} identifies per-subgroup misclassification deviation as the bias source; the natural correction is per-subgroup confusion matrix inversion.
5	This correction (EC-HTE) proceeds in three stages: estimate per-subgroup confusion matrices via hierarchical Bayes, invert them to correct observed outcome moments, and propagate correction uncertainty into downstream causal estimators.
6	The complete procedure is summarized in Algorithm~\ref{alg:echte} and illustrated in Figure~\ref{fig:method_overview}.
7	
8	\begin{algorithm}[t]
9	\caption{EC-HTE: Error-Corrected HTE}
10	\label{alg:echte}
11	\begin{algorithmic}[1]
12	\Require $\{(Y_i, W_i, \hat{Z}_i, X_i)\}_{i=1}^N$; expert labels $\{Z_j^*\}_{j=1}^{n_{\text{expert}}}$; subgroup map $S$
13	\Ensure Corrected CATE estimates $\hat{\tau}(z)$ with CIs
14	\Statex
15	\State \textbf{Check:} $n_{\text{expert}} \cdot P(Z_{\min}) / K \geq 25$ and $\max_s \pi_s < 0.5$
16	\Statex
17	\State \textbf{Step 1: Per-subgroup CMs (hierarchical Bayes)}
18	\State $\alpha_0 \gets \arg\max_\alpha \prod_s p(\text{data}_s \mid \alpha, \hat{C}_{\text{global}})$
19	\For{$s = 1, \ldots, K$}
20	    \State $\hat{C}_s[j,k] \gets (n_{s,jk} + \alpha_0 \hat{C}_{\text{global},j,k}) / (n_{s,j\cdot} + \alpha_0)$
21	\EndFor
22	\State \textbf{Step 2: Stratified inversion}
23	\For{$s = 1, \ldots, K$}
24	    \If{$\kappa(\hat{C}_s) > 100$} $\hat{C}_s \gets \bar{C}$ \Comment{$\kappa$-guard}
25	    \EndIf
26	    \State $\tilde{\boldsymbol{\mu}}_s \gets \hat{C}_s^{-1} \hat{\boldsymbol{\mu}}_s$
27	\EndFor
28	\State \textbf{Step 3: Downstream estimation}
29	\State Feed $\tilde{\boldsymbol{\mu}}_s$ into CausalForestDML (honest splitting)
30	\State $\mathrm{se}_{\mathrm{adj},i} \gets \sqrt{\mathrm{diag}(\hat{C}_{S_i}^{-1}\, \mathrm{diag}(\mathrm{se}_i^2)\, \hat{C}_{S_i}^{-\top})}$
31	\end{algorithmic}
32	\end{algorithm}
33	
34	\begin{figure*}[t]
35	\centering
36	\include
…[truncated 3533 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 2552 · 2026-05-25T21:15:03.847618+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 2553 · 2026-05-25T21:15:04.801770+00:00_

1	\section{Experiments}
2	
3	\subsection{Setup}
4	
5	We test on synthetic ($N{=}5{,}000$, $K \in \{2, 4\}$, controlled $\Delta\tau$ and $\Delta\pi$, 100 Monte Carlo (MC) runs) and semi-synthetic data-generating processes (DGPs) spanning four NLP tasks: sentiment analysis (TweetEval~\cite{barbieri2020tweeteval}, $K{=}4$), hate speech detection (CivilComments, $K{=}4$), stance detection ($K{=}5$; Appendix~\ref{app:stance}), and topic classification (AG News, $K{=}4$; Appendix~\ref{app:agnews}), with full specifications in Appendix~\ref{app:dgp}.
6	
7	We compare: (1) \textit{Naive} (no correction), (2) \textit{Global} (pooled confusion matrix, equivalent to PPI/DSL~\cite{angelopoulos2023ppi,egami2023dsl} with homogeneous error), (3) \textit{Stratified MLE} (per-subgroup DSL without shrinkage), (4) \textit{HB EC-HTE} (per-subgroup correction), (5) \textit{PPCI}~\cite{sui2026ppci}, and (6) \textit{EC-HTE+PPCI}.
8	For CausalForest~\cite{wager2018causal}, we compare naive, global, and EC-HTE variants.
9	Primary metrics are $|\text{bias}|$, root mean squared error (RMSE), and 95\% confidence interval (CI) coverage, averaged across subgroups and 100 MC runs.
10	Robustness validations cover eight conditions including asymmetric errors, subgroup misspecification, and treatment-dependent misclassification (all $\geq$89.5\% coverage; Appendices~\ref{app:hatespeech}--\ref{app:treatment_dep}).
11	Semi-synthetic evaluation uses empirical confusion matrices from 11 LLM--dataset combinations (eight LLMs across two datasets; Appendix~\ref{app:realcm_bias}; semi-real CM validation in Appendix~\ref{app:semireal}; open-source LLM validation in Appendix~\ref{app:multilm_opensource}).
12	
13	\subsection{Empirical Validation of the Bias Identity}
14	\label{sec:bias_mechanism}
15	
16	\begin{table}[t]
17	\centering
18	\caption{Results under moderate heterogeneity and semi-synthetic data. Moderate: $\Delta\pi \leq 0.10$; TweetEval: empirical subgroup structure ($K{=}4$). Metrics averaged over 
…[truncated 9141 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 2554 · 2026-05-25T21:15:04.802198+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 2555 · 2026-05-25T21:15:05.304479+00:00_

1	\section{Conclusion}\label{sec:conclusion}
2	
3	Standard confusion-matrix correction can reverse causal conclusions when misclassification rates vary across subgroups.
4	We derived an exact bias identity ($R^2 \geq 0.97$) that yields a diagnostic for flagging harmful correction and prescribes per-subgroup correction when $\Delta\pi > 0.15$ and $n_{\text{expert}} \geq 250$, validated across 11 LLM--dataset combinations spanning eight LLMs and four NLP tasks.
5	For practitioners, we recommend a three-step protocol: (1)~estimate per-subgroup error rates from a pilot sample; (2)~apply the diagnostic (Proposition~\ref{prop:debiasing_hurts}) to identify subgroups where global correction would increase bias; (3)~if $\Delta\pi > 0.15$ and the expert budget exceeds 250 labels, apply per-subgroup correction via EC-HTE.
6	When these conditions are not met, global correction remains appropriate; the diagnostic explicitly guards against inappropriate application.
7	The framework is task-agnostic and composes with prediction-powered inference.
8	
9	More broadly, as LLM annotation becomes standard practice in computational social science, the gap between average accuracy and subgroup-level reliability will grow with the diversity of populations studied.
10	Our bias identity provides a principled lens for auditing any pipeline that feeds machine-generated labels into downstream causal analysis.
11	Future directions include continuous covariates, larger $K$, and joint covariate--outcome correction.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 2556 · 2026-05-25T21:15:05.304875+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 2557 · 2026-05-25T21:15:05.807407+00:00_

1	\section*{Limitations}
2	\label{sec:limitations}
3	
4	Per-subgroup correction requires sufficient expert labels ($n_{\text{expert}} \geq 250$ for $K{=}2$, $\geq 500$ for $K{=}4$) and moderate classifier accuracy ($\text{FPR}_s, \text{FNR}_s < 0.5$); at $K{=}8$, RMSE exceeds global correction under fixed expert budget (Appendix~\ref{app:k8_subgroups}).
5	Assumption~(A3) requires balanced effect modifier prevalence; under class imbalance ($P(Z{=}1) = 0.1$), the identity remains exact ($R^2 \geq 0.976$) but EC-HTE's RMSE advantage narrows (ratio 1.06--1.68; Appendix~\ref{app:classimbalance}).
6	Assumption~(A1), conditional independence of misclassification and potential outcomes, is not empirically testable; sensitivity analysis shows robustness up to $\gamma_T \leq 0.05$ for treatment-dependent misclassification (coverage $\geq$89.7\%; Appendix~\ref{app:treatment_dep}).
7	Ground-truth subgroup CATEs are unavailable in public datasets because classic causal inference benchmarks lack the LLM annotation step that creates the measurement error we address, so all evaluations use synthetic CATE injection on real text features and real LLM annotations (Appendices~\ref{app:dgp},~\ref{app:multilm}).
8	When LLMs annotate both the effect modifier and the outcome variable, covariate-side and outcome-side misclassification errors may be correlated, violating the independence structure assumed by combining EC-HTE with post-prediction causal inference (PPCI) frameworks~\cite{sui2026ppci}; practitioners should verify error independence or apply joint correction when both variables are LLM-annotated.
9	
10	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 2558 · 2026-05-25T21:15:05.858262+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 2559 · 2026-05-25T21:15:06.812670+00:00_

File content (41683 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 2560 · 2026-05-25T21:15:07.816910+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/review_round_24/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"PDF_NOT_FOUND\"",
  "description": "Check if submitted PDF exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/review_round_24/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"PDF_NOT_FOUND\"",
    "description": "Check if submitted PDF exists"
  }
}
```

</details>

---


### Tool result

_source line 2561 · 2026-05-25T21:15:08.320453+00:00_

-rw-r--r-- 1 ubuntu ubuntu 1258881 May 25 21:11 /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/review_round_24/submitted.pdf
PDF_EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Bash",
  "elapsed_ms": 503
}
```

</details>

---


### Tool call

_source line 2562 · 2026-05-25T21:15:08.471532+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "ec_hte_llm_annotation",
  "file": "decisions.yaml",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "ec_hte_llm_annotation",
    "file": "decisions.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 2563 · 2026-05-25T21:15:08.522519+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/decisions.yaml\", \"content\": \"_next_id: 28\\ndecisions:\\n- id: D001\\n  date: 2026-05-20 18:52 UTC\\n  summary: MVP PASS：核心假设验证通过，评估框架修正为子群水平\\n  rationale: 三轮模拟（v1 CausalForest + v2 差分估计 + v3 子群分析）完成。核心发现：(1) 全局校正在低误差子群造成系统性伤害（bias\\n    恶化 7.8x），EC-HTE 分层校正修复此问题（|bias|<0.015）；(2) 边际 CATE 评估掩盖此效应（正负偏差抵消），子群水平才是正确评估维度；(3)\\n    EC-HTE 在高误差子群方差偏高→层级贝叶斯 partial pooling 是 research 阶段核心优先级。Pass 标准 1 修正为子群水平后\\n    PASS（子群 B EC-HTE RMSE 0.063 vs Global 0.100），标准 2/3/4 均 PASS。\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-20 19:44 UTC\\n  summary: Dream Round 1 分析完成：best=4 (Weak Accept), median=3.5 (Borderline Conference),\\n    worst=2.5 (Borderline Reject)。达到启动门槛（best≥weak accept, median≥borderline）。识别6项确认行动项、4项观察项。更新\\n    framing 和 plan 后批准 P0 CPU 实验（exp-001, exp-002）立即启动。exp-007 (PPCI comparison) 升级为\\n    P0。\\n  rationale: 三档一致的结构性问题：(1) 薄弱文献（11 refs vs 40+ expected），(2) MCMC 实现细节缺失，(3) 方法新颖性定位需明确为\\\"问题发现\\\"而非\\\"新技术\\\"，(4)\\n    信息密度过高需增加图表减少表格，(5) K=2 理论 vs K>2 实验的 gap，(6) 真实数据验证缺失。数据依赖性问题（coverage undercoverage,\\n    diagnostic AUROC, PPCI dominance）仅在2档或单档出现，记录为观察项待真实实验验证。framing/plan 改动为渐进式改善（sharpening\\n    novelty positioning, adding requirements），不构成重大方向转变，当前 Dream 评分已达标。\\n  related_experiments: []\\n  depends_on: []\\n- id: D003\\n  date: 2026-05-20 21:32 UTC\\n  summary: 'Dream Round 2 analysis: proceed with P0 experiments, 10 writing requirements\\n    codified'\\n  rationale: 'Dream Round 2 (dream_20260520T194535): best=4/6, median=3.5/6, worst=3/6.\\n    Worst improved +0.5 from Round 1 (was 2.5). Three-tier consistent issues all addressable\\n    in writing phase: (1) bibliography 9→30-35 refs, (2) \\\"bias bound\\\"→\\\"bias decomposition\\n    identity\\\", (3) DGP specification, (4) figures, (5) Fuller 1987 contextualization,\\n    (6) \\\"never worse\\\" qualification, (7) inve
…[truncated 1453 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2564 · 2026-05-25T21:15:24.802965+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "ec_hte_llm_annotation",
  "file": "memory.md",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "ec_hte_llm_annotation",
    "file": "memory.md",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 2565 · 2026-05-25T21:15:26.259643+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/memory.md\", \"content\": \"# Memory — ec_hte_llm_annotation\\n\\n## 研究发现\\n\\n### 非对称诊断等价性 (2026-05-23, Worker A)\\n对 K_Z=2（二值标签），非对称诊断公式 |B_s[1,1] - B_s[1,0]| / (FPR_s + FNR_s) 恒等于对称公式 |δ_s| / ((1-2π̄)·π_s)。FPR/FNR 不对称性在行差中完全抵消。AUC=0.63 的真正原因是 τ_s=0 子组的 MC 噪声，排除后 AUC=1.0。\\n\\n### Centered EB 优于 Dir(α/2, α/2) (2026-05-23, Worker C)\\n原始 HB 用 Dir(α/2, α/2) 向 (0.5, 0.5) 收缩是错误目标。Centered EB 向 global CM 收缩，在 moderate heterogeneity 下 RMSE ≈ Global（消除弱点），在 extreme 下 RMSE < Global < original HB。K4 extreme 下 original HB RMSE > Global 的问题也被修复。\\n\\n### Bootstrap SE 在小 n_expert 下的表现 (2026-05-23, Task G)\\nDIM + Centered EB, K=2 extreme (π=[0.05,0.25]), 20 MC × B=100。Bootstrap coverage 在所有 n_expert ≥25 下均达 nominal (≥95%): n=25→100%, n=50→98.8%, n=75→97.5%, n=100→96.3%, n=200→95.0%。Plug-in SE 在 n≥50 时 ≥92.5%，最弱点 n=75 (91.2%)。高误差子群 s1 (π=0.25) 是 bootstrap 的主要受益者。数据: results/exp_bootstrap_small_n_summary.csv\\n\\n### UCB Annotator Demographics Δπ 不足 (2026-05-24)\\nUCB Hate Speech 135K行数据，7个 annotator demographic features + 交互特征。最大 Δπ = 0.117（race × ideology），单一特征最大 0.084（education）。根因：GPT-4.1 的主要错误模式是 FNR ≈ 0.55（漏检 hate speech），这在所有 demographic 组中高度一致。Δπ 来自次要效应（如保守派 π≈0.39 vs 自由派 π≈0.35），幅度不够。即使用虚高 Δπ=0.23 跑 semi-synthetic，correction 因 1-FPR-FNR ≈ 0.28 放大噪声，全面劣于 naive。**结论：annotator demographics 维度的异质性不足以支撑 EC-HTE real-data 成功案例，且高 FNR 使 CM inversion 本身不稳定。这是 task-level 的结构性限制，非 subgroup 选择问题。**\\n\\n## 决策记录\\n\\n### API 模型版本 (已验证)\\n- GPT-4.1: `gpt-4.1-2025-04-14`\\n- GPT-5.4: `gpt-5.4` (reasoning model, 慢, ~1min/call)\\n- GPT-5.5 不可用（reasoning tokens 消耗 max_tokens budget）\\n\\n### 论文写作\\n- EMNLP 2026 DDL: 2026-05-25 (ARR)\\n- 8 页主文限制，Limitations/References 不计入\\n- R15 审稿修复已全部完成（8 项，2026-05-23）\\n- Messing (2026) 已加入 Related Work\\n- 数据完整性审计完成：AUC=0.86 确认正确（Δπ-only diagnostic），AUC=0.82→0.66 已修复（3处），74-82% coverage 确认正确\\n- 匿名代码仓库已推送: https://github
…[truncated 454 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 1456
}
```

</details>

---


### Tool call

_source line 2566 · 2026-05-25T21:15:26.812991+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
  "description": "Check existing review issues tracker"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
    "description": "Check existing review issues tracker"
  }
}
```

</details>

---


### Tool result

_source line 2567 · 2026-05-25T21:15:27.667464+00:00_

&lt;persisted-output>
Output too large (29.3KB). Full output saved to: /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0520-projects-ec-hte-llm-annotation--claude-sessions-review-director-2cf1d8af/a791ee5f-6e76-4741-a9b2-fdbbd511a98d/tool-results/bgbwxs1w6.txt

Preview (first 2KB):
issues:
  # === RESOLVED (prior rounds — abbreviated) ===
  - id: "R1-N1"
    summary: "Proposition 1 以 formal bound 呈现但仅有 97% MC 经验验证"
    category: method
    severity: critical
    status: resolved
    first_raised_round: 0
    last_seen_round: 2
    action_items: []
    resolution: "重新推导为精确恒等式"
    resolution_round: 0

  - id: "R2-W8"
    summary: "Proposition 1 限于 K=2"
    category: method
    severity: critical
    status: resolved
    first_raised_round: 0
    last_seen_round: 1
    action_items: []
    resolution: "Theorem 1 适用一般 K"
    resolution_round: 0

  - id: "R1-N2"
    summary: "Real data ground truth CATE 来源不明"
    category: experiment
    severity: critical
    status: resolved
    first_raised_round: 0
    last_seen_round: 1
    action_items: []
    resolution: "恰当定位为 illustrative application"
    resolution_round: 0

  - id: "R1-N3"
    summary: "HB 模型规格严重不完整"
    category: method
    severity: critical
    status: resolved
    first_raised_round: 0
    last_seen_round: 1
    action_items: []
    resolution: "完整 MCMC 规格"
    resolution_round: 0

  - id: "JOINT-W4"
    summary: "相关工作严重遗漏"
    category: writing
    severity: warning
    status: resolved
    first_raised_round: 0
    last_seen_round: 1
    action_items: []
    resolution: "30+ 引用覆盖"
    resolution_round: 0

  - id: "JOINT-W3"
    summary: "信息密度过高"
    category: writing
    severity: warning
    status: resolved
    first_raised_round: 0
    last_seen_round: 1
    action_items: []
    resolution: "主文精简至合理密度"
    resolution_round: 0

  - id: "R2-W7"
    summary: "真实数据验证单薄"
    category: experiment
    severity: warning
    status: resolved
    first_raised_round: 0
    last_see
…[truncated 323 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Bash",
  "elapsed_ms": 854
}
```

</details>

---


### Tool call

_source line 2568 · 2026-05-25T21:15:27.667932+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/references.bib",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/references.bib",
    "limit": "50"
  }
}
```

</details>

---


### Tool result

_source line 2569 · 2026-05-25T21:15:28.170350+00:00_

1	% === Proximal / Sensitivity ===
2	
3	@article{miao2018identifying,
4	  title={Identifying Causal Effects with Proxy Variables of an Unmeasured Confounder},
5	  author={Miao, Wang and Geng, Zhi and Tchetgen Tchetgen, Eric J.},
6	  journal={Biometrika},
7	  volume={105},
8	  number={4},
9	  pages={987--993},
10	  year={2018}
11	}
12	
13	@article{cinelli2020making,
14	  title={Making Sense of Sensitivity: Extending Omitted Variable Bias},
15	  author={Cinelli, Carlos and Hazlett, Chad},
16	  journal={Journal of the Royal Statistical Society: Series B},
17	  volume={82},
18	  number={1},
19	  pages={39--67},
20	  year={2020}
21	}
22	
23	% === Datasets ===
24	
25	@inproceedings{borkan2019nuanced,
26	  title={Nuanced Metrics for Measuring Unintended Bias with Real Data for Text Classification},
27	  author={Borkan, Daniel and Dixon, Lucas and Sorensen, Jeffrey and Thain, Nithum and Vasserman, Lucy},
28	  booktitle={Companion Proceedings of The 2019 World Wide Web Conference},
29	  pages={491--500},
30	  year={2019}
31	}
32	
33	% === Econometrics of Binary Misclassification ===
34	
35	@incollection{bound2001measurement,
36	  title={Measurement Error in Survey Data},
37	  author={Bound, John and Brown, Charles and Mathiowetz, Nancy},
38	  booktitle={Handbook of Econometrics},
39	  volume={5},
40	  pages={3705--3843},
41	  year={2001},
42	  publisher={Elsevier}
43	}
44	
45	@article{greenland1980effect,
46	  title={The Effect of Misclassification in the Presence of Covariates},
47	  author={Greenland, Sander},
48	  journal={American Journal of Epidemiology},
49	  volume={112},
50	  number={4},

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 2570 · 2026-05-25T21:15:28.421708+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "wc -l /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/*.tex",
  "description": "Count lines per tex file"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Bash",
  "tool_args": {
    "command": "wc -l /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/*.tex",
    "description": "Count lines per tex file"
  }
}
```

</details>

---


### Tool result

_source line 2571 · 2026-05-25T21:15:28.522564+00:00_

     8 /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/abstract.tex
  1581 /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex
    43 /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix_agnews.tex
    38 /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix_stance.tex
    46 /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/checklist.tex
    10 /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/conclusion.tex
   129 /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/experiments.tex
    38 /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/introduction.tex
     9 /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/limitations.tex
    54 /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/main.tex
    66 /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/method.tex
     7 /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/related_work.tex
   102 /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/theory.tex
  2131 total

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 2572 · 2026-05-25T21:15:45.892644+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper && cat abstract.tex | sed 's/\\\\[a-zA-Z]*{[^}]*}//g; s/\\\\[a-zA-Z]*//g; s/[{}$~]//g; s/\\\\\\\\//g' | wc -w",
  "description": "Count abstract word count (approximate)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper && cat abstract.tex | sed 's/\\\\[a-zA-Z]*{[^}]*}//g; s/\\\\[a-zA-Z]*//g; s/[{}$~]//g; s/\\\\\\\\//g' | wc -w",
    "description": "Count abstract word count (approximate)"
  }
}
```

</details>

---


### Tool result

_source line 2573 · 2026-05-25T21:15:46.850560+00:00_

178
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/review_director_2cf1d8af

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Bash",
  "elapsed_ms": 957
}
```

</details>

---


### Tool call

_source line 2574 · 2026-05-25T21:15:46.851070+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -c '^@' /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/references.bib",
  "description": "Count bib entries"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -c '^@' /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/references.bib",
    "description": "Count bib entries"
  }
}
```

</details>

---


### Tool result

_source line 2575 · 2026-05-25T21:15:48.256982+00:00_

71

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Bash",
  "elapsed_ms": 1405
}
```

</details>

---


### Tool call

_source line 2576 · 2026-05-25T21:15:48.257406+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/agent/config.yaml 2>/dev/null | grep -A5 \"external_review\" || echo \"NO_EXTERNAL_REVIEW_CONFIG\"",
  "description": "Check external review config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/agent/config.yaml 2>/dev/null | grep -A5 \"external_review\" || echo \"NO_EXTERNAL_REVIEW_CONFIG\"",
    "description": "Check external review config"
  }
}
```

</details>

---


### Tool result

_source line 2577 · 2026-05-25T21:15:49.211389+00:00_

NO_EXTERNAL_REVIEW_CONFIG

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Bash",
  "elapsed_ms": 953
}
```

</details>

---


### Tool call

_source line 2578 · 2026-05-25T21:15:49.412996+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/review_issues.yaml 2>/dev/null | head -200",
  "description": "Read existing review issues (first 200 lines)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/review_issues.yaml 2>/dev/null | head -200",
    "description": "Read existing review issues (first 200 lines)"
  }
}
```

</details>

---


### Tool result

_source line 2579 · 2026-05-25T21:15:49.513953+00:00_

issues:
  # === RESOLVED (prior rounds — abbreviated) ===
  - id: "R1-N1"
    summary: "Proposition 1 以 formal bound 呈现但仅有 97% MC 经验验证"
    category: method
    severity: critical
    status: resolved
    first_raised_round: 0
    last_seen_round: 2
    action_items: []
    resolution: "重新推导为精确恒等式"
    resolution_round: 0

  - id: "R2-W8"
    summary: "Proposition 1 限于 K=2"
    category: method
    severity: critical
    status: resolved
    first_raised_round: 0
    last_seen_round: 1
    action_items: []
    resolution: "Theorem 1 适用一般 K"
    resolution_round: 0

  - id: "R1-N2"
    summary: "Real data ground truth CATE 来源不明"
    category: experiment
    severity: critical
    status: resolved
    first_raised_round: 0
    last_seen_round: 1
    action_items: []
    resolution: "恰当定位为 illustrative application"
    resolution_round: 0

  - id: "R1-N3"
    summary: "HB 模型规格严重不完整"
    category: method
    severity: critical
    status: resolved
    first_raised_round: 0
    last_seen_round: 1
    action_items: []
    resolution: "完整 MCMC 规格"
    resolution_round: 0

  - id: "JOINT-W4"
    summary: "相关工作严重遗漏"
    category: writing
    severity: warning
    status: resolved
    first_raised_round: 0
    last_seen_round: 1
    action_items: []
    resolution: "30+ 引用覆盖"
    resolution_round: 0

  - id: "JOINT-W3"
    summary: "信息密度过高"
    category: writing
    severity: warning
    status: resolved
    first_raised_round: 0
    last_seen_round: 1
    action_items: []
    resolution: "主文精简至合理密度"
    resolution_round: 0

  - id: "R2-W7"
    summary: "真实数据验证单薄"
    category: experiment
    severity: warning
    status: resolved
    first_raised_round: 0
    last_seen_round: 1
    action_items: []
    resolution: "恰当定位 + 公开数据集"
    resolution_round: 0

  - id: "R1-W5"
    summary: "Pages 9-10 缺 Appendix 标签"
    category: format
    severity: info
    status: resolved
    first_raised_round: 0
    last_seen_round: 0
    action_items: []
    resolution: "附录结构重组"
    resolutio
…[truncated 3102 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 2580 · 2026-05-25T21:15:54.334042+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/review_issues.yaml 2>/dev/null | tail -n +200",
  "description": "Read remaining review issues"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/review_issues.yaml 2>/dev/null | tail -n +200",
    "description": "Read remaining review issues"
  }
}
```

</details>

---


### Tool result

_source line 2581 · 2026-05-25T21:15:54.385214+00:00_

  - id: "R19-W3"
    summary: "Theorem 1→Proposition 3 呈现顺序：A5 排除目标场景但未充分强调"
    category: writing
    severity: warning
    status: resolved
    first_raised_round: 19
    last_seen_round: 21
    action_items: []
    resolution: "Proposition 3 已在主文 Section 3, 含完整公式和 Δτ_s"
    resolution_round: 21

  - id: "R19-M1"
    summary: "Assumption (A5) 实践限制被轻描淡写"
    category: method
    severity: info
    status: resolved
    first_raised_round: 19
    last_seen_round: 21
    action_items: []
    resolution: "Proposition 3 已在主文充分展示 A5 relaxation"
    resolution_round: 21

  - id: "R19-M6"
    summary: "Algorithm 1 缺收敛标准/最大迭代次数"
    category: method
    severity: info
    status: resolved
    first_raised_round: 19
    last_seen_round: 22
    action_items:
      - round: 22
        action: "Algorithm 1 改为 EB 流程，Gibbs 降为 appendix 替代方案"
        assigned_to: agent
        status: done
    resolution: "Algorithm 1 已改为 EB point estimates (closed-form Dirichlet update)，MCMC 保留为 appendix 验证方案。与 method.tex (<5ms) 和代码一致。"
    resolution_round: 22

  - id: "R22-Q1"
    summary: "Method 说 empirical Bayes (<5ms) 但 Algorithm 1 描述 Gibbs sampler——不一致"
    category: writing
    severity: warning
    status: resolved
    first_raised_round: 22
    last_seen_round: 22
    action_items:
      - round: 22
        action: "Algorithm 1 EB 化 + appendix MCMC 描述统一"
        assigned_to: agent
        status: done
    resolution: "Algorithm 1 改为 EB，与 method.tex 和代码一致。Reviewer 验证通过。"
    resolution_round: 22

  - id: "R22-Q2"
    summary: "A3 放松时 'identity remains exact with modified coefficients' 但未给出显式形式"
    category: method
    severity: info
    status: resolved
    first_raised_round: 22
    last_seen_round: 22
    action_items:
      - round: 22
        action: "Appendix D 补充 A3 放松显式推导 (M_s Bayes rule form + B_s·1=0 证明)"
        assigned_to: agent
        status: done
    resolution: "appendix classimbalance 节新增 eq:ms_imbalanced 显式形式，证明 product form 对任意 p₀ 成立。"
    resolution_round: 22

  - id:
…[truncated 19160 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Bash",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 2582 · 2026-05-25T21:16:22.524711+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "ec_hte_llm_annotation",
  "review_chat_id": "oc_489afd65980834a91024fd48e21d984f"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "ec_hte_llm_annotation",
    "review_chat_id": "oc_489afd65980834a91024fd48e21d984f"
  }
}
```

</details>

---


### Tool result

_source line 2583 · 2026-05-25T21:16:47.482946+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 24958
}
```

</details>

---


### Tool call

_source line 2584 · 2026-05-25T21:16:48.939012+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "你是 Reviewer 1，负责 **方法严谨性** 审查。\n\n## 论文信息\n- 标题: \"When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects\"\n- 论文路径: `/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/review_round_24/submitted.pdf`\n\n## Venue 要求（EMNLP 2026, via ARR）\n- **格式**: ACL 双栏模板，`\\usepackage[review]{acl}`\n- **页数**: 正文严格 8 页限制，参考文献无限制\n- **Limitations**: 必须有，放在 Conclusion 之后，不计入页数（但不能含过多额外内容）\n- **匿名**: Double-blind\n- **Abstract**: 不超过 200 words\n- **评分标准**: 5=Award, 4.5=Borderline Award, 4=Conference (主会议), 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 你的审查侧重\n\n### 1. 理论推导（重点）\n- Theorem 1 (Bias Decomposition Identity) 的证明是否完整、严密？假设 (A1)-(A5) 是否合理？\n- Proposition 3 (A5 relaxation) 推导是否正确？\n- Proposition 5 (debiasing can increase bias) 条件推导是否严谨？\n- Remark 2 (asymmetric case) 声称是否有充分支撑？\n- 有限样本余项 O_p(κ²·n^{-1/2}) 是否正确？\n- Corollary 4 (aggregate bias) 是否 trivial？\n\n### 2. 方法设计\n- Hierarchical Bayes CM estimation: 先验选择是否合理？empirical Bayes vs MCMC 选择是否有讨论？\n- κ-guard (阈值 100): 是否有理论依据？与 O_p remainder 的关系？\n- SE adjustment 公式的正确性\n- Algorithm 1 是否完整、可复现？\n\n### 3. 实验严谨性\n- DGP 设计是否合理？参数范围覆盖是否充分？\n- MC=100 runs 是否足够支撑 coverage 声称？\n- 评价指标 (|bias|, RMSE, coverage) 选择是否合适？\n- Semi-synthetic 与 fully synthetic 结果的一致性\n- CausalForest / R-learner 集成验证的充分性\n- 操作条件 (Δπ>0.15, n_expert≥250, K≤4) 的实证支撑\n\n### 4. 假设合理性\n- (A1) conditional independence: 实际场景中是否可能被违反？sensitivity analysis 是否充分？\n- (A2) symmetric misclassification: 即使有 Remark 说不需要，论文结构是否过度依赖此假设？\n- (A3) balanced effect modifier: 放松后 R²≥0.976 但 RMSE advantage narrows — 是否充分讨论？\n- (A5) homogeneous treatment effects: Proposition 3 是否充分解决了这个限制？\n\n请按标准审稿格式输出：Summary → Strengths → Weaknesses (逐条编号，标注 severity: Must-Fix / Should-Fix / Minor) → Questions → Missing References → Overall Assessment (含评分和置信度)。",
  "project": "ec_hte_llm_annotation",
  "chat_id": "oc_489afd65980834a91024fd48e21d984f",
  "director_session_key": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "你是 Reviewer 1，负责 **方法严谨性** 审查。\n\n## 论文信息\n- 标题: \"When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects\"\n- 论文路径: `/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/review_round_24/submitted.pdf`\n\n## Venue 要求（EMNLP 2026, via ARR）\n- **格式**: ACL 双栏模板，`\\usepackage[review]{acl}`\n- **页数**: 正文严格 8 页限制，参考文献无限制\n- **Limitations**: 必须有，放在 Conclusion 之后，不计入页数（但不能含过多额外内容）\n- **匿名**: Double-blind\n- **Abstract**: 不超过 200 words\n- **评分标准**: 5=Award, 4.5=Borderline Award, 4=Conference (主会议), 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 你的审查侧重\n\n### 1. 理论推导（重点）\n- Theorem 1 (Bias Decomposition Identity) 的证明是否完整、严密？假设 (A1)-(A5) 是否合理？\n- Proposition 3 (A5 relaxation) 推导是否正确？\n- Proposition 5 (debiasing can increase bias) 条件推导是否严谨？\n- Remark 2 (asymmetric case) 声称是否有充分支撑？\n- 有限样本余项 O_p(κ²·n^{-1/2}) 是否正确？\n- Corollary 4 (aggregate bias) 是否 trivial？\n\n### 2. 方法设计\n- Hierarchical Bayes CM estimation: 先验选择是否合理？empirical Bayes vs MCMC 选择是否有讨论？\n- κ-guard (阈值 100): 是否有理论依据？与 O_p remainder 的关系？\n- SE adjustment 公式的正确性\n- Algorithm 1 是否完整、可复现？\n\n### 3. 实验严谨性\n- DGP 设计是否合理？参数范围覆盖是否充分？\n- MC=100 runs 是否足够支撑 coverage 声称？\n- 评价指标 (|bias|, RMSE, coverage) 选择是否合适？\n- Semi-synthetic 与 fully synthetic 结果的一致性\n- CausalForest / R-learner 集成验证的充分性\n- 操作条件 (Δπ>0.15, n_expert≥250, K≤4) 的实证支撑\n\n### 4. 假设合理性\n- (A1) conditional independence: 实际场景中是否可能被违反？sensitivity analysis 是否充分？\n- (A2) symmetric misclassification: 即使有 Remark 说不需要，论文结构是否过度依赖此假设？\n- (A3) balanced effect modifier: 放松后 R²≥0.976 但 RMSE advantage narrows — 是否充分讨论？\n- (A5) homogeneous treatment effects: Proposition 3 是否充分解决了这个限制？\n\n请按标准审稿格式输出：Summary → Strengths → Weaknesses (逐条编号，标注 severity: Must-Fix / Should-Fix / Minor) → Questions → Missing References → Overall Assessment (含评分和置信度)。",
    "project": "ec_hte_llm_annotation",
    "chat_id": "oc_489afd65980834a91024fd48e21d984f",
    "director_session_key": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director"
  }
}
```

</details>

---


### Tool result

_source line 2585 · 2026-05-25T21:17:11.204040+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_489afd65980834a91024fd48e21d984f:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 22265
}
```

</details>

---


### Tool call

_source line 2586 · 2026-05-25T21:17:11.756522+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "你是 Reviewer 2，负责 **新颖性与完整性** 审查。\n\n## 论文信息\n- 标题: \"When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects\"\n- 论文路径: `/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/review_round_24/submitted.pdf`\n\n## Venue 要求（EMNLP 2026, via ARR）\n- **格式**: ACL 双栏模板，`\\usepackage[review]{acl}`\n- **页数**: 正文严格 8 页限制，参考文献无限制\n- **Limitations**: 必须有，放在 Conclusion 之后，不计入页数（但不能含过多额外内容）\n- **匿名**: Double-blind\n- **Abstract**: 不超过 200 words\n- **评分标准**: 5=Award, 4.5=Borderline Award, 4=Conference (主会议), 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 你的审查侧重\n\n### 1. 新颖性评估（重点）\n- 相对 Frazis-Loewenstein (2003) scalar attenuation 的增量贡献有多大？是 K=1→K>1 的直接推广还是本质新见解？\n- Bias identity 的 product form δ_s·Δτ/(1-2π̄) 从技术角度看是否 trivial（矩阵代数的直接计算）？\n- EC-HTE 的技术贡献（HB + stratified inversion + κ-guard）vs 已有文献（PPI, DSL, PPCI）的增量\n- \"Sign reversal\" 现象的新颖性 — 是否已被其他文献暗示？\n- 诊断准则 (Proposition 5) 的实际增量价值 vs 直接运行 EC-HTE\n\n### 2. 相关工作覆盖\n- PPI / DSL / PPCI / ForestIV 的定位是否准确？\n- 噪声标签学习 (noisy label learning) 文献是否充分覆盖？特别是 subgroup-dependent vs instance-dependent noise\n- 测量误差校正 (measurement error correction) 经典文献是否遗漏？\n- 因果推断 + NLP 交叉领域是否有遗漏的近期工作？\n- 检查是否有 fabricated/non-existent references（特别关注 2025-2026 年份的引用）\n\n### 3. 写作质量与可读性\n- Abstract 信息密度是否过高？数字是否太多？\n- Introduction 的叙事结构（问题→发现→贡献）是否清晰？\n- Section 3 (Theory) 的符号密度对 NLP 读者是否友好？\n- Related Work 是否过于简略（仅 7 行）？\n- Conclusion 是否充实？\n- \"Debiasing\" 术语是否有歧义（fairness vs measurement-error）？标题中的 \"When Debiasing Hurts\" 是否准确反映论文内容？\n\n### 4. Venue 适配性\n- 论文本质是 causal inference methodology 还是 NLP contribution？\n- 对 NLP 社区的实际价值是什么？\n- EMNLP 近年是否接收类似的因果推断方法论文？\n- 论文是否更适合其他 venue（如 UAI, AISTATS, JMLR）？\n\n### 5. 格式规范\n- 8 页限制是否满足？\n- Limitations section 是否存在且内容适当？\n- 匿名性是否完整（无作者名、致谢、机构信息泄露）？\n- 图表质量、可读性、标注\n\n请按标准审稿格式输出：Summary → Strengths → Weaknesses (逐条编号，标注 severity: Must-Fix / Should-Fix / Minor) → Questions → Missing References → Overall Assessment (含评分和置信度)。",
  "project": "ec_hte_llm_annotation",
  "chat_id": "oc_489afd65980834a91024fd48e21d984f",
  "director_session_key": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "你是 Reviewer 2，负责 **新颖性与完整性** 审查。\n\n## 论文信息\n- 标题: \"When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects\"\n- 论文路径: `/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/review_round_24/submitted.pdf`\n\n## Venue 要求（EMNLP 2026, via ARR）\n- **格式**: ACL 双栏模板，`\\usepackage[review]{acl}`\n- **页数**: 正文严格 8 页限制，参考文献无限制\n- **Limitations**: 必须有，放在 Conclusion 之后，不计入页数（但不能含过多额外内容）\n- **匿名**: Double-blind\n- **Abstract**: 不超过 200 words\n- **评分标准**: 5=Award, 4.5=Borderline Award, 4=Conference (主会议), 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 你的审查侧重\n\n### 1. 新颖性评估（重点）\n- 相对 Frazis-Loewenstein (2003) scalar attenuation 的增量贡献有多大？是 K=1→K>1 的直接推广还是本质新见解？\n- Bias identity 的 product form δ_s·Δτ/(1-2π̄) 从技术角度看是否 trivial（矩阵代数的直接计算）？\n- EC-HTE 的技术贡献（HB + stratified inversion + κ-guard）vs 已有文献（PPI, DSL, PPCI）的增量\n- \"Sign reversal\" 现象的新颖性 — 是否已被其他文献暗示？\n- 诊断准则 (Proposition 5) 的实际增量价值 vs 直接运行 EC-HTE\n\n### 2. 相关工作覆盖\n- PPI / DSL / PPCI / ForestIV 的定位是否准确？\n- 噪声标签学习 (noisy label learning) 文献是否充分覆盖？特别是 subgroup-dependent vs instance-dependent noise\n- 测量误差校正 (measurement error correction) 经典文献是否遗漏？\n- 因果推断 + NLP 交叉领域是否有遗漏的近期工作？\n- 检查是否有 fabricated/non-existent references（特别关注 2025-2026 年份的引用）\n\n### 3. 写作质量与可读性\n- Abstract 信息密度是否过高？数字是否太多？\n- Introduction 的叙事结构（问题→发现→贡献）是否清晰？\n- Section 3 (Theory) 的符号密度对 NLP 读者是否友好？\n- Related Work 是否过于简略（仅 7 行）？\n- Conclusion 是否充实？\n- \"Debiasing\" 术语是否有歧义（fairness vs measurement-error）？标题中的 \"When Debiasing Hurts\" 是否准确反映论文内容？\n\n### 4. Venue 适配性\n- 论文本质是 causal inference methodology 还是 NLP contribution？\n- 对 NLP 社区的实际价值是什么？\n- EMNLP 近年是否接收类似的因果推断方法论文？\n- 论文是否更适合其他 venue（如 UAI, AISTATS, JMLR）？\n\n### 5. 格式规范\n- 8 页限制是否满足？\n- Limitations section 是否存在且内容适当？\n- 匿名性是否完整（无作者名、致谢、机构信息泄露）？\n- 图表质量、可读性、标注\n\n请按标准审稿格式输出：Summary → Strengths → Weaknesses (逐条编号，标注 severity: Must-Fix / Should-Fix / Minor) → Questions → Missing References → Overall Assessment (含评分和置信度)。",
    "project": "ec_hte_llm_annotation",
    "chat_id": "oc_489afd65980834a91024fd48e21d984f",
    "director_session_key": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director"
  }
}
```

</details>

---


### Tool result

_source line 2587 · 2026-05-25T21:17:13.120852+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_489afd65980834a91024fd48e21d984f:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1364
}
```

</details>

---


### Assistant

_source line 2588 · 2026-05-25T21:17:19.140176+00:00_

已派发：
- ✅ 视觉审查 Agent（fire-and-forget，与审稿并行）
- ✅ Reviewer 1（方法严谨性）
- ✅ Reviewer 2（新颖性/完整性）

等待两位 Reviewer 独立初审返回。外部审稿未配置，跳过。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director"
}
```

</details>

---


## Round 197

## Round 197

2 recorded events


### User

_source line 2589 · 2026-05-25T21:25:36.661272+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 审稿意见（方法严谨性审查）

**论文**: "When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects"
**Venue**: EMNLP 2026 via ARR

---

## 总体评分
**Overall**: 3.5 (Borderline Conference)
**一句话总结**: 理论贡献干净且正确，揭示了 global confusion-matrix 校正在异质误分类下引入 subgroup-level 偏差的新现象；实验极其充分。但部分声明精确性不足，方法适用范围偏窄（K≤4, n_expert≥250），削弱了实际影响力。

## 官方维度打分（ACL ARR review form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 4/5 | Theorem 1 证明完整正确；Proposition 3/5 推导严密；但 A3 松弛下的 "exact" 声明不准确，SE 公式忽略 CM 估计不确定性 |
| Excitement | 3.5/5 | 问题真实且日益重要（LLM annotation for CSS）；bias identity 有洞见但适用场景偏窄 |
| Reproducibility | 4/5 | Algorithm 1 描述基本完整，DGP 参数齐全，匿名代码已提供 |
| Confidence | 4/5 | 我仔细检查了核心证明的每一步代数推导，熟悉 measurement error 和 causal inference 文献 |

---

## Summary

本文推导了一个精确的偏差恒等式（Theorem 1），表明当 LLM 标注的误分类率在 subgroup 间异质时，标准的全局 confusion matrix 校正会引入与 δ_s·Δτ/(1−2π̄) 成正比的 subgroup-level 偏差。基于此，作者提出 EC-HTE：用层次贝叶斯估计 per-subgroup confusion matrix，再做分层校正。论文在 520+ synthetic 配置、11 个 LLM-dataset 组合、4 个 NLP 任务上验证了理论和方法。

---

## 主要优势

**S1. 理论贡献新颖且严密。** Theorem 1 的乘积形式 δ_s·Δτ/(1−2π̄) 清晰揭示了三个因素的交互：error-rate deviation、treatment effect heterogeneity、pooled-error amplification。Appendix B 的逐步推导（Eq. 7–13）代数正确，我手动验证了 (1,1) entry 的化简和 δ_s 代入步骤。

**S2. Proposition 5 的 Δτ-free diagnostic 具有独特实用价值。** 条件 |δ_s|/((1−2π̄)·π_s)>1 仅需误分类率即可判断 global correction 是否有害，打破了需要先估计 treatment effects 的循环依赖。AUC=0.86（symmetric）/0.96（asymmetric）在 48 个配置上验证（Figure 6）。

**S3. 实验极其充分，诚实报告局限。** 520 个 synthetic 配置 + 48 个 asymmetric 配置 + K=8 边界分析 + 11 个 real LLM CM + robustness checks（8 个条件）。Table 1 supplementary 中 EC-HTE 在 moderate heterogeneity 下 RMSE 劣于 Global 的结果被如实报告，operating conditions 清晰列出。

**S4. 方法设计有理论指导。** EC-HTE 的三阶段流程（HB CM estimation → stratified inversion → downstream integration）直接由 Theorem 1 驱动：identity 指出偏差来源是 per-subgroup CM deviation，自然解是 per-subgroup 校正。

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] **A3 松弛下 "identity remains exact" 的声明不准确**
- 具体位置：Section 3 倒数第二段；theory.tex line 85
- 问题：论文称 "Under class imbalance (relaxing A3), the identity remains exact (R²≥0.976 at P(Z=1)=0.1)"。但 Theorem 1 的简化乘积形式 δ_s·Δτ/(1−2π̄) 依赖 A3（P(Z=0)=P(Z=1)=0.5 使 M_s=C_s）。松弛 A3 后 mixing matrix M_s≠C_s，简化形式不再精确成立。R²=0.994（balanced）→ 0.976（imbalanced）的下降正好说明存在近似误差。"exact" 一词在此处具有误导性。
- 为什么影响接收：这是论文理论贡献的核心声明之一。"exact identity" 是标题和 abstract 的卖点。如果在常见的 class imbalance 场景下 identity 只是近似成立，读者对方法的信心会受影响。
- 建议修改方向：(a) 明确区分 general matrix form bias(z,s)=[(M_global^{-1} M_s − I)τ]_z（总是精确的）和 simplified scalar form δ_s·Δτ/(1−2π̄)（仅在 A2+A3 下精确）；(b) 将 "remains exact" 改为 "remains a close approximation (R²≥0.976)" 或证明 general form 在松弛 A3 后仍以某种closed-form 精确成立。

**N2** [critical] **Plug-in SE 公式忽略 confusion matrix 估计不确定性，且论文未充分讨论**
- 具体位置：Algorithm 1 line 11; method.tex line 30
- 问题：SE 公式 se_adj = √(diag(Ĉ_s^{-1} diag(se²) Ĉ_s^{-⊤})) 仅传播 outcome moment 的抽样方差，不含 Ĉ_s 本身的估计误差。在 n_expert=250, K=4 时，每个 subgroup 仅 ~62 个 expert labels，CM 估计不确定性非平凡。CausalForest 的 footnote（p.7）承认 plug-in SE 仅达 93.8% coverage，bootstrap 恢复到 ≥95%——说明 CM uncertainty 确实导致了 under-coverage。
- 为什么影响接收：论文反复引用 "coverage≥93-95%" 作为方法可靠性的核心证据。如果 plug-in SE 系统性 under-cover，而 bootstrap 才是正确方案，论文应以 bootstrap 为默认推荐，并在正文（非 footnote）讨论此问题。
- 建议修改方向：(a) 在 Section 4.3 明确讨论 plug-in vs bootstrap SE 的区别；(b) 将 bootstrap 提升为默认推荐（尤其在 n_expert/K < 100 时）；(c) 在 Table 2 中同时报告 plug-in 和 bootstrap coverage。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] **Algorithm 1 中 Ĉ_s^{-1} 在 asymmetric case 下不正确**
- 具体位置：Algorithm 1 line 10-11; method.tex Eq. (6)
- 问题：τ_obs = M_s · τ_true，恢复需要 M_s^{-1}（mixing matrix 的逆），不是 C_s^{-1}（forward confusion matrix 的逆）。A2+A3 下 M_s=C_s 所以无区别。但论文 Remark 2 声称 A2 不必要，Appendix J 做了 asymmetric 实验——这些场景下 Algorithm 1 应使用 M_s^{-1}（通过 Bayes rule 从 C_s 计算），而非直接 C_s^{-1}。
- 建议：在 Algorithm 1 和 Section 4.2 中明确：asymmetric case 下先从 Ĉ_s 和 class prior 计算 M̂_s，再求逆。Appendix J 的实验可能已经这样做了（从结果看是正确的），但算法描述需要修正。

**W2** [warning] **finite-sample remainder O_p(κ²·n^{-1/2}) 中的 κ 指代不一致**
- 具体位置：Section 3 最后一段 vs Appendix B 最后一段
- 问题：正文写 "O_p(n_expert^{-1/2}·κ(C_s)²)"，附录写 "κ(M_global)²"。κ-guard 检查的是 κ(Ĉ_s)>100。三处引用了不同的 condition number，读者无法确定哪个才是 bound 中的正确量。
- 建议：统一符号。实际 bound 涉及 κ(M_global) 和 ||M_s||（见附录推导），应明确写出。

**W3** [warning] **Operating conditions 偏窄，限制实际适用性**
- 具体位置：Section 5.4; experiments.tex lines 125-128
- 问题：K≤4, n_expert≥250（K=2）或 ≥500（K=4），Δπ>0.15, FNR<0.50。在很多 NLP 场景中 subgroup 数量 K>4（如按人口统计交叉分组），且获取 250+ expert labels 代价高昂。K=8 时 EC-HTE RMSE (0.340) 远超 Global (0.168)（Appendix I, Table 6）。
- 建议：讨论如何通过 adaptive grouping 或 hierarchical subgroup structure 扩展到 K>4。Table 6 中 adaptive shrinkage 将 RMSE 从 0.340 降到 0.216，值得在正文提及。

**W4** [warning] **Corollary 4 (Aggregate Bias) 贡献度偏低**
- 具体位置：Section 3, Corollary 4
- 问题：Cov_w(π_s, Δτ_s)/(1−2π̄) 是 Proposition 3 的直接加权平均，推导仅需一行。作为 Corollary 列出可以，但论文正文说 "The proof is immediate"，占据的篇幅和编号空间与贡献不匹配。
- 建议：可以保留编号但不单独写 proof paragraph（仅说 "follows by weighted averaging"）。释放的空间可用于讨论 W1 或 W3。

---

## 小问题（不影响接收）

- **M1**: Abstract word count 应确认不超过 200 words（EMNLP 2026 硬约束）。当前 abstract 约 140 words，合规。
- **M2**: Figure 3 (p.4) 的 heatmap 标注 "debiasing helps" / "debiasing hurts" 分区线与 Proposition 5 的 threshold 条件吻合度可以更明确标出。
- **M3**: Table 2 caption 中 "Frazis and Loewenstein (2003)" 缩写为 "F-L Scalar/Per-sub." 但正文首次出现在 Table 2 本身——应在 Section 5.1 的 baselines 描述中引入。
- **M4**: Appendix J Table 10 中 EC-HTE 在 48 个 asymmetric 配置的 **所有** 情况下均劣于 Global (RMSE 0.125 vs 0.109)，但正文 Section 3 Remark 2 仅引用了 3 个 cherry-picked 配置的优势结果 (Table 8)。建议在 Remark 2 或相关段落引用 Table 10 的全面结果以避免误导。

---

## Questions

**Q1**: Proposition 3 relaxes A5 允许 subgroup-specific Δτ_s，但 B_s = M_global^{-1} M_s − I 不依赖 treatment effects。是否意味着 A5 从一开始就不是必要假设，Theorem 1 可以直接用 Δτ_s 表述？如果是，为什么在 Theorem 1 中设 A5 再在 Proposition 3 松弛？

**Q2**: 在 CivilComments case study (Section 5.2) 中，FNR=53.3% 接近 singularity。如果 practitioner 的某些 subgroup FNR>50% 但其他 subgroup 正常，EC-HTE 的 κ-guard 会对该 subgroup fallback to global correction——这是否会引入一种新的异质性偏差（部分 subgroup per-subgroup 校正，部分 global 校正）？

**Q3**: 论文假设 subgroup membership S 是已知的。在实际应用中 S 通常也需要估计或定义（如通过 text features 聚类）。S 的 misspecification 对 EC-HTE 的影响是否有分析？（Appendix O 提到了 robustness to misspecification 但我没找到详细结果。）

---

## Missing References

- Egami et al. (2023) "Using Imperfect Surrogates for Downstream Inference" — 已引用
- Angelopoulos et al. (2023) PPI — 已引用
- Zhan, Zhao, and Dai (2024) prediction-powered confidence — 已引用
- 无明显遗漏，参考文献覆盖了 measurement error, causal inference, NLP annotation 三个方向。

---

## 格式合规检查
- ✅ `\usepackage[review]{acl}` 匿名格式
- ✅ 正文 8 页（content ends on p.8）
- ✅ Limitations section 在 Conclusion 之后，篇幅适当
- ✅ Abstract ~140 words（<200 限制）
- ✅ References 从 p.9 开始，不计入页数限制

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 2590 · 2026-05-25T21:25:47.409202+00:00_

Reviewer 1 审稿意见已收到（3.5 Borderline Conference）。2 个 Must-Fix（A3 松弛下 "exact" 声明精确性、plug-in SE 忽略 CM 不确定性）、4 个 Should-Fix。等待 Reviewer 2 完成后进入交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director"
}
```

</details>

---


## Round 198

## Round 198

2 recorded events


### User

_source line 2591 · 2026-05-25T21:26:00.805406+00:00_

[Reviewer 1 审稿结果]:
审稿完成。核心结论：

- **Overall 3.5 (Borderline Conference)**，Soundness 4/5，Excitement 3.5/5
- **理论正确**：Theorem 1 证明完整，代数推导逐步验证无误；Proposition 3/5 推导严密
- **两个 Must-Fix**：(1) A3 松弛下 "identity remains exact" 声明不准确（R²=0.976 说明简化形式只是近似）；(2) plug-in SE 忽略 CM 估计不确定性，bootstrap 应为默认推荐
- **四个 Should-Fix**：Algorithm 1 中 C_s^{-1} vs M_s^{-1} 在 asymmetric case 下的区别未说明；κ² remainder 中 κ 指代不一致；operating conditions 偏窄（K≤4）；Corollary 4 贡献度偏低
- **实验极其充分**，520+ 配置 + 11 个 real LLM CM + 8 种 robustness check，且诚实报告了方法不适用的场景

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 2592 · 2026-05-25T21:26:09.437152+00:00_

Reviewer 1 审稿已收到。等待 Reviewer 2 返回后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director"
}
```

</details>

---


## Round 199

## Round 199

6 recorded events


### User

_source line 2593 · 2026-05-25T21:27:45.028258+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 审稿报告：新颖性与完整性

**论文**: "When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects"
**Venue**: EMNLP 2026 (via ARR)
**审查侧重**: 新颖性、相关工作覆盖、写作质量、Venue 适配性、格式规范

---

## 总体评分
**Overall**: 3.5 — Borderline Conference
**一句话总结**: 论文提出了一个关于 LLM 标注异质误差导致因果效应估计偏差的 exact bias identity，理论洞察有价值（sign reversal 现象），实验设计全面，但新颖性相对 Frazis-Loewenstein (2003) 的增量需更强论证，Related Work 严重不足，且有一条引用无法验证。

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 数学推导正确，实验设计全面（520 synthetic configs × 100 MC runs），但核心假设 A1（misclassification 与 potential outcomes 条件独立）较强且不可检验，sensitivity analysis 仅覆盖 γ_γ ≤ 0.05（Appendix Y.1），范围偏窄 |
| Excitement | 3/5 | Sign reversal 现象对实践有警示意义，但目标受众较窄（做 causal inference + LLM annotation 的研究者）；核心理论是 2×2 confusion matrix 代数的直接计算，技术深度有限 |
| Overall | 3.5/5 | 有价值的理论洞察 + 扎实实验，但新颖性增量和 Related Work 覆盖不足制约了评分 |
| Confidence | 4/5 | 熟悉 measurement error correction、causal inference 和 NLP annotation 文献 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] 引用 "Sui et al., 2026" (PPCI) 无法验证
- 具体位置：Section 4.3 (p5), Section 5.3 (p7), Limitations (p8), Appendix K (p17)
- 问题：论文多次引用 "PPCI (Sui et al., 2026)" 作为 outcome-side misclassification 的校正方法，并在 Section 4.3 和 Appendix K 中将其与 EC-HTE 组合使用。然而，我通过多次 web search 均无法找到此引用。已知的 PPCI 论文 "Prediction-Powered Causal Inferences" (arxiv:2502.06343) 作者为 Cadei, Demirel, De Bartolomeis 等人，并非 "Sui et al."。
- 为什么影响接收：如果该引用不存在或被错误归因，这涉及学术诚信问题，也影响论文中 EC-HTE+PPCI 组合结果的可信度。请作者在 rebuttal 中提供该引用的完整信息（DOI、arxiv ID 或会议/期刊信息）。

**N2** [critical] Related Work 严重不足
- 具体位置：Section 2 (p2), 仅约 7 行正文
- 问题：对于一篇连接 measurement error correction、causal inference、LLM annotation 三个领域的论文，Related Work 仅有 ~7 行文本（不含 Appendix F 的 Extended Related Work），远低于 EMNLP 论文的正常标准。虽然 Appendix F (p13) 提供了 Extended Related Work，但主文中的 Related Work 甚至没有提及以下关键领域：
  - (a) **Noisy label learning**：论文的 setup（subgroup-dependent misclassification rates）本质上是 subgroup/feature-dependent label noise，但完全未讨论该领域。instance-dependent label noise (Xia et al., 2020; Cheng et al., 2022) 和 feature-dependent label noise (ICLR 2022) 文献与本文高度相关。
  - (b) **Measurement error in regression**：虽然引用了 Fuller (1987) 和 Carroll et al. (2006)，但未讨论 He and Schennach (2008) 的 nonparametric identification results 或 Mahajan (2006) 的 binary misclassification identification 在本文 framework 中的定位关系。
  - (c) 主文应至少概述 PPI/DSL/PPCI/ForestIV 各自解决什么问题以及本文如何与之互补，而非只在 Appendix F 展开。
- 为什么影响接收：Related Work 不充分会让 reviewer 和读者质疑作者是否充分了解相关文献，也使论文的 novelty claim 难以评估。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] 新颖性相对 Frazis-Loewenstein (2003) 的增量论证不够清晰
- 具体位置：Section 3, Theorem 1 (p3), Remark 2 (p4)
- 问题：论文的核心理论贡献是将 F-L (2003) 的 scalar attenuation 从 K=1（同质误差）推广到 K>1（异质子群）。Theorem 1 的 product form δ_s·Δτ/(1−2π̄) 确实揭示了 sign reversal 这一定性新现象，但从技术角度看，推导过程是 2×2 混淆矩阵的直接矩阵代数（Appendix B, p11: M_global^{-1}·M_s − I 的 (1,1) entry 展开）。论文应更明确地论证：(1) 为什么 product form 不是"显然的"推广？(2) Corollary 6 (multi-class extension, p11) 的 closed-form amplification factor g(ε) 是否存在？论文承认 "no closed-form amplification factor does not exist" for K>2，这限制了理论结果的实用性。
- 建议：在 Section 3 或 Introduction 中加入一段明确的 "our contribution beyond F-L" 论述，强调 sign reversal 是 qualitatively new（F-L 只能 attenuate，不能 reverse），且 product structure 使得 diagnostic without estimating treatment effects 成为可能。

**W2** [warning] Proposition 5 (Diagnostic) 的增量价值需论证
- 具体位置：Proposition 5 (p4), Figure 6 (p8)
- 问题：Proposition 5 给出了 global correction 何时增加 bias 的 sufficient condition（π_s < ε_s/(2(1−ε_s))），但这个 diagnostic 的实际价值 vs 直接运行 EC-HTE 需要更清楚的论证。如果已经有了 per-subgroup error rates π_s，为什么不直接运行 EC-HTE 而要先做 diagnostic？论文在 Section 5.4 (p7-8) 给出了 operating conditions（Δτ > 0.15, n_expert ≥ 250, K ≤ 4），但 Proposition 5 的 diagnostic 需要 Δτ 的信息，而 Δτ 本身需要先估计 treatment effects。
- 建议：明确 Proposition 5 的实际使用场景——如果是一个"无需估计 treatment effects 就能 flag harmful correction"的工具，需要更清楚地说明如何获取 Δτ 的先验信息。论文确实说"from error rates alone, without estimating treatment effects"，但 Equation (5) 的条件涉及 π_s 和 ε_s/(2(1−ε_s))，并不涉及 Δτ？请澄清。

**W3** [warning] Venue 适配性 — 核心贡献更偏 causal inference methodology
- 具体位置：全文
- 问题：论文的核心理论贡献（bias identity, Proposition 5）本质上是 measurement error correction 在 causal inference 中的应用，技术工具（混淆矩阵代数、hierarchical Bayes、stratified inversion）来自统计学/计量经济学。虽然动机和实验涉及 NLP tasks（sentiment, hate speech, stance detection, topic classification），但论文对 NLP 社区的贡献主要是"警示 + 实践指南"，而非方法论创新。
- 缓解因素：(1) Audinet de Pieuchon et al. (2025) 的 Benchmarking 论文被 EMNLP 2025 接收，说明 EMNLP 接收此类论文有先例；(2) 论文的 practical guidelines 对 NLP practitioners 有直接价值。
- 建议：在 Introduction 中更突出对 NLP 社区的具体 takeaway（e.g., 何时该用 per-subgroup correction、何时 global correction 足够），减少纯统计理论的篇幅。

**W4** [warning] "Debiasing" 术语歧义
- 具体位置：标题、Abstract, footnote 2 (p1)
- 问题：标题 "When Debiasing Hurts" 中的 "debiasing" 在 NLP 社区通常指 fairness debiasing（消除对特定人群的歧视性偏见），而本文指 measurement-error correction（校正标注误差引入的统计偏差）。虽然 footnote 2 做了澄清，但标题是论文最先被看到的部分，容易引起误导。EMNLP 的搜索和分类系统中，"debiasing" 关键词会将本文与 fairness 论文混在一起。
- 建议：考虑将标题改为更精确的表述，如 "When Error Correction Hurts" 或在标题中加入 "Measurement-Error" 限定词。

**W5** [warning] Abstract 数字密度过高
- 具体位置：Abstract (p1)
- 问题：Abstract 在 ~185 words 中包含了 5×, 14.9%, 7.4×, Δτ=0.098, 0.15, 250, K≤4 等大量数字。虽然信息丰富，但对首次阅读的 reviewer 来说解析负担较重。特别是 "Δτ=0.098" 和 "n_expert ≥ 250, K ≤ 4" 这样的 operating conditions 在 Abstract 中缺乏上下文。
- 建议：Abstract 保留最关键的 1-2 个数字（如 sign reversal 的 14.9% 和 bias reduction 的 7.4×），其余移至正文。

---

## 小问题（不影响接收）

1. **作者姓名拼写**：Reference 中 "Audinet de Pieuchon" 的姓名可能有误。ACL Anthology 显示第一作者为 "Nicolas Audinet de Pieuchon"，请核实论文中的拼写是否为 "Audinet de Peachon"（如果是，需修正）。

2. **Table 1 & Table 2 对比**：Table 1 (moderate heterogeneity, p6) 和 Table 2 (extreme heterogeneity, p7) 使用不同的 DGP 设置，但正文中对两个 table 之间 RMSE 差异的讨论较少。建议加一句说明从 moderate 到 extreme heterogeneity 时各方法性能变化的趋势。

3. **Figure 3 (p4)**：图标题说 "Bias amplification under global correction"，但 y 轴标签 "|CATE bias|" 的字体偏小，在打印版本中可能难以辨认。建议增大字体。

4. **Appendix 数量**：论文有 25 个 appendix（A-Y），结构可以更精简。部分 appendix（如 G "MCMC Convergence Diagnostics"）可以合并。

5. **Conclusion (p8)**：结论部分偏短（约 15 行），主要重述贡献和 operating conditions，缺少对更广泛影响的讨论（e.g., 该 framework 是否适用于 LLM-as-judge 等新兴场景？）。

---

## Missing References / 遗漏的相关工作

1. **Noisy label learning 文献**（完全缺失）：
   - Xia et al. (2020). "Part-dependent label noise: Towards instance-dependent label noise." NeurIPS 2020.
   - Cheng et al. (2022). "Instance-dependent label-noise learning with manifold-regularized transition matrix estimation." CVPR 2022.
   - Zhu et al. (2022). "Beyond images: Label noise transition matrix estimation for tasks with lower-quality features." ICML 2022.
   这些工作处理 feature/instance-dependent 噪声，与本文的 subgroup-dependent misclassification 直接相关。

2. **Measurement error identification**：
   - Mahajan (2006). "Identification and estimation of regression models with misclassification." Econometrica.
   - Lewbel (2007). "Estimation of average treatment effects with misclassification." Econometrica.
   论文引用了 Lewbel (2007)（page 9 references），但 Mahajan (2006) 的 nonparametric identification results 在 Appendix F 提及，应在主文中讨论定位关系。

3. **LLM annotation quality 的系统性研究**：
   - Ziems et al. (2024). "Can Large Language Models Transform Computational Social Science?" Computational Linguistics.（已引用，但在 Related Work 中未讨论）

4. **Causal inference + text 的近期工作**：
   - Keith et al. (2020). "Text and Causal Inference: A Review of Using Text to Remove Confounding from Causal Estimates."
   - Fong and Tyler (2021). "Machine Learning Predictions as Regression Covariates."

---

## 主要优势

1. **理论洞察的实践价值**：Theorem 1 的 product form 清晰地揭示了 sign reversal 的条件（δ_s 和 Δτ 同号时），这是 F-L scalar attenuation 无法捕捉的定性新现象。14.9% 的 sign reversal rate 在 520 个 synthetic configurations 中被稳定复现，且在所有 8 个真实 LLM-dataset pairs 中 global correction 均 amplify bias（Table 2, p7），实验证据充分。

2. **实验设计的全面性**：覆盖 4 个 NLP tasks × 8 个 LLM-dataset combinations × 520 synthetic configs × 100 MC runs。Semi-synthetic evaluation 使用真实 LLM confusion matrices，既保证了可控性又提高了生态效度。Real case study (CivilComments, p7) 和 cross-task validation (Appendix Y.9-Y.10, p30-31) 进一步增强了可信度。

3. **Diagnostic 的实用性**：Proposition 5 + Figure 6 (p8) 的 ROC 曲线（AUC = 0.89-0.97）表明 diagnostic 在实际中确实能有效筛选出被 global correction 伤害的子群，且只需 per-subgroup error rates 而不需估计 treatment effects。

4. **Operating conditions 的诚实报告**：论文明确给出了 EC-HTE 优于 global correction 的 boundary conditions（Δτ > 0.15, n_expert ≥ 250, K ≤ 4, p7），并在 Limitations 中坦诚报告了方法的局限性，展现了良好的科学态度。

5. **写作的信息密度**：虽然 Section 3 符号密度高，但 notation 一致且 assumptions 列举清晰（A1-A5, p3）。Figure 1 (p2) 有效地概括了 global correction vs EC-HTE pipeline 的区别。

---

## Questions for Authors

Q1. 请提供 "Sui et al., 2026" (PPCI) 引用的完整信息。如果该论文尚未公开，请说明其状态（under review / in preparation），并提供 anonymous 版本的链接。

Q2. Proposition 5 声称可以 "from error rates alone, without estimating treatment effects" 判断 global correction 是否有害。但 Equation (5) 的条件涉及 π_s（per-subgroup error rate）。在实践中，获取 per-subgroup π_s 通常需要 per-subgroup expert labels（与运行 EC-HTE 所需的资源相同）。能否澄清 Proposition 5 的实际使用场景？它相对于直接运行 EC-HTE 的 marginal value 是什么？

Q3. Assumption A1（conditional independence of misclassification and potential outcomes）在 LLM annotation 中是否现实？例如，LLM 对极端文本（strongly hateful text）的分类准确率可能更高，而这些极端文本的 treatment effect 也可能更大。Appendix Y.1 的 sensitivity analysis 仅覆盖 γ_γ ≤ 0.05，这是一个很窄的范围。是否有更强的 robustness 证据？

Q4. 论文是否考虑过 LLM annotation 的 calibration（如 Platt scaling）作为 EC-HTE 的替代或补充？Appendix Y.7 似乎提到了 calibration，但主文中未讨论。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 2594 · 2026-05-25T21:28:26.179534+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "## 交叉审查：请逐条回应 Reviewer 1 的审稿意见\n\n以下是 Reviewer 1 的完整审稿意见（方法严谨性审查）。请逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n### Reviewer 1 的 Must-Fix 问题\n\n**N1** [critical] **A3 松弛下 \"identity remains exact\" 的声明不准确**\n- Section 3 倒数第二段 (theory.tex line 85) 称 \"Under class imbalance (relaxing A3), the identity remains exact (R²≥0.976 at P(Z=1)=0.1)\"\n- R1 论点：Theorem 1 的简化乘积形式 δ_s·Δτ/(1−2π̄) 依赖 A3（P(Z=0)=P(Z=1)=0.5 使 M_s=C_s）。松弛 A3 后 M_s≠C_s，简化形式不再精确成立。R²=0.994→0.976 的下降说明存在近似误差。\n- R1 建议：区分 general matrix form（总是精确的）和 simplified scalar form（仅在 A2+A3 下精确）。\n\n**N2** [critical] **Plug-in SE 公式忽略 CM 估计不确定性**\n- Algorithm 1 line 11 的 SE 公式仅传播 outcome moment 的抽样方差，不含 Ĉ_s 本身的估计误差\n- CausalForest footnote (p.7) 承认 plug-in SE 仅 93.8% coverage，bootstrap 恢复到 ≥95%\n- R1 建议：bootstrap 应为默认推荐，在正文（非 footnote）讨论\n\n### Reviewer 1 的 Should-Fix 问题\n\n**W1** Algorithm 1 中 Ĉ_s^{-1} 在 asymmetric case 下应为 M_s^{-1}\n**W2** O_p(κ²·n^{-1/2}) 中 κ 指代不一致（C_s vs M_global）\n**W3** Operating conditions 偏窄（K≤4, n_expert≥250），限制实际适用性\n**W4** Corollary 4 贡献度偏低\n\n### Reviewer 1 的 Minor Issues\n- M1: Abstract word count 合规\n- M2: Figure 3 分区线与 Proposition 5 threshold 吻合度可更明确\n- M3: F-L baseline 缩写首次出现在 Table 2 而非正文\n- M4: Appendix J Table 10 中 EC-HTE 在所有 48 个 asymmetric 配置下 RMSE 均劣于 Global，但 Remark 2 仅引用 cherry-picked 优势结果\n\n### Reviewer 1 的 Questions\nQ1: A5 是否从一开始就不必要？\nQ2: κ-guard fallback 到 global correction 是否引入新的异质性偏差？\nQ3: Subgroup membership S 的 misspecification 影响？\n\n### Reviewer 1 的总体评分\nOverall 3.5, Soundness 4/5, Excitement 3.5/5, Confidence 4/5\n\n---\n\n请对以上每一条（N1, N2, W1-W4, M1-M4, Q1-Q3）逐条给出 [AGREE] 或 [REBUT]，并说明理由。",
  "project": "ec_hte_llm_annotation",
  "chat_id": "oc_489afd65980834a91024fd48e21d984f",
  "director_session_key": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "## 交叉审查：请逐条回应 Reviewer 1 的审稿意见\n\n以下是 Reviewer 1 的完整审稿意见（方法严谨性审查）。请逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n### Reviewer 1 的 Must-Fix 问题\n\n**N1** [critical] **A3 松弛下 \"identity remains exact\" 的声明不准确**\n- Section 3 倒数第二段 (theory.tex line 85) 称 \"Under class imbalance (relaxing A3), the identity remains exact (R²≥0.976 at P(Z=1)=0.1)\"\n- R1 论点：Theorem 1 的简化乘积形式 δ_s·Δτ/(1−2π̄) 依赖 A3（P(Z=0)=P(Z=1)=0.5 使 M_s=C_s）。松弛 A3 后 M_s≠C_s，简化形式不再精确成立。R²=0.994→0.976 的下降说明存在近似误差。\n- R1 建议：区分 general matrix form（总是精确的）和 simplified scalar form（仅在 A2+A3 下精确）。\n\n**N2** [critical] **Plug-in SE 公式忽略 CM 估计不确定性**\n- Algorithm 1 line 11 的 SE 公式仅传播 outcome moment 的抽样方差，不含 Ĉ_s 本身的估计误差\n- CausalForest footnote (p.7) 承认 plug-in SE 仅 93.8% coverage，bootstrap 恢复到 ≥95%\n- R1 建议：bootstrap 应为默认推荐，在正文（非 footnote）讨论\n\n### Reviewer 1 的 Should-Fix 问题\n\n**W1** Algorithm 1 中 Ĉ_s^{-1} 在 asymmetric case 下应为 M_s^{-1}\n**W2** O_p(κ²·n^{-1/2}) 中 κ 指代不一致（C_s vs M_global）\n**W3** Operating conditions 偏窄（K≤4, n_expert≥250），限制实际适用性\n**W4** Corollary 4 贡献度偏低\n\n### Reviewer 1 的 Minor Issues\n- M1: Abstract word count 合规\n- M2: Figure 3 分区线与 Proposition 5 threshold 吻合度可更明确\n- M3: F-L baseline 缩写首次出现在 Table 2 而非正文\n- M4: Appendix J Table 10 中 EC-HTE 在所有 48 个 asymmetric 配置下 RMSE 均劣于 Global，但 Remark 2 仅引用 cherry-picked 优势结果\n\n### Reviewer 1 的 Questions\nQ1: A5 是否从一开始就不必要？\nQ2: κ-guard fallback 到 global correction 是否引入新的异质性偏差？\nQ3: Subgroup membership S 的 misspecification 影响？\n\n### Reviewer 1 的总体评分\nOverall 3.5, Soundness 4/5, Excitement 3.5/5, Confidence 4/5\n\n---\n\n请对以上每一条（N1, N2, W1-W4, M1-M4, Q1-Q3）逐条给出 [AGREE] 或 [REBUT]，并说明理由。",
    "project": "ec_hte_llm_annotation",
    "chat_id": "oc_489afd65980834a91024fd48e21d984f",
    "director_session_key": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director"
  }
}
```

</details>

---


### Tool result

_source line 2595 · 2026-05-25T21:28:48.478269+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_489afd65980834a91024fd48e21d984f:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 22298
}
```

</details>

---


### Tool call

_source line 2596 · 2026-05-25T21:28:49.231141+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "## 交叉审查：请逐条回应 Reviewer 2 的审稿意见\n\n以下是 Reviewer 2 的完整审稿意见（新颖性与完整性审查）。请逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n### Reviewer 2 的 Must-Fix 问题\n\n**N1** [critical] **引用 \"Sui et al., 2026\" (PPCI) 无法验证**\n- Section 4.3, Section 5.3, Limitations, Appendix K 多次引用\n- R2 论点：多次 web search 无法找到此引用。已知的 PPCI 论文 (arxiv:2502.06343) 作者为 Cadei, Demirel, De Bartolomeis 等人，并非 \"Sui et al.\"。如果引用不存在或被错误归因，涉及学术诚信。\n\n**N2** [critical] **Related Work 严重不足**\n- Section 2 仅约 7 行正文\n- 缺失领域：(a) Noisy label learning（Xia et al. 2020, Cheng et al. 2022）；(b) Measurement error identification（Mahajan 2006, He & Schennach 2008）；(c) PPI/DSL/PPCI/ForestIV 在主文中未概述各自解决的问题\n\n### Reviewer 2 的 Should-Fix 问题\n\n**W1** 新颖性相对 F-L (2003) 的增量论证不够清晰——推导本质是 2×2 矩阵代数的直接计算\n**W2** Proposition 5 的增量价值需论证——已有 per-subgroup error rates 为什么不直接运行 EC-HTE？\n**W3** Venue 适配性——核心贡献更偏 causal inference methodology 而非 NLP\n**W4** \"Debiasing\" 术语歧义——NLP 社区通常指 fairness debiasing\n**W5** Abstract 数字密度过高\n\n### Reviewer 2 的 Minor Issues\n1. Reference 中 \"Audinet de Pieuchon\" 姓名拼写可能有误\n2. Table 1 与 Table 2 之间 RMSE 差异讨论不足\n3. Figure 3 y 轴标签字体偏小\n4. 25 个 Appendix 结构可精简\n5. Conclusion 偏短，缺少更广泛影响讨论\n\n### Reviewer 2 的 Missing References\n- Xia et al. (2020) instance-dependent label noise, NeurIPS\n- Cheng et al. (2022) manifold-regularized transition matrix, CVPR\n- Zhu et al. (2022) label noise for lower-quality features, ICML\n- Mahajan (2006) misclassification identification, Econometrica\n- Keith et al. (2020) text and causal inference\n- Fong & Tyler (2021) ML predictions as regression covariates\n\n### Reviewer 2 的 Questions\nQ1: 请提供 Sui et al. 2026 PPCI 引用的完整信息\nQ2: Proposition 5 相对于直接运行 EC-HTE 的 marginal value？\nQ3: A1 在 LLM annotation 中是否现实？sensitivity analysis 范围 γ_T≤0.05 偏窄\nQ4: 是否考虑过 LLM calibration (Platt scaling) 作为替代？\n\n### Reviewer 2 的总体评分\nOverall 3.5, Soundness 3.5/5, Excitement 3/5, Confidence 4/5\n\n---\n\n请对以上每一条（N1, N2, W1-W5, Minor 1-5, Q1-Q4）逐条给出 [AGREE] 或 [REBUT]，并说明理由。",
  "project": "ec_hte_llm_annotation",
  "chat_id": "oc_489afd65980834a91024fd48e21d984f",
  "director_session_key": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "## 交叉审查：请逐条回应 Reviewer 2 的审稿意见\n\n以下是 Reviewer 2 的完整审稿意见（新颖性与完整性审查）。请逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n### Reviewer 2 的 Must-Fix 问题\n\n**N1** [critical] **引用 \"Sui et al., 2026\" (PPCI) 无法验证**\n- Section 4.3, Section 5.3, Limitations, Appendix K 多次引用\n- R2 论点：多次 web search 无法找到此引用。已知的 PPCI 论文 (arxiv:2502.06343) 作者为 Cadei, Demirel, De Bartolomeis 等人，并非 \"Sui et al.\"。如果引用不存在或被错误归因，涉及学术诚信。\n\n**N2** [critical] **Related Work 严重不足**\n- Section 2 仅约 7 行正文\n- 缺失领域：(a) Noisy label learning（Xia et al. 2020, Cheng et al. 2022）；(b) Measurement error identification（Mahajan 2006, He & Schennach 2008）；(c) PPI/DSL/PPCI/ForestIV 在主文中未概述各自解决的问题\n\n### Reviewer 2 的 Should-Fix 问题\n\n**W1** 新颖性相对 F-L (2003) 的增量论证不够清晰——推导本质是 2×2 矩阵代数的直接计算\n**W2** Proposition 5 的增量价值需论证——已有 per-subgroup error rates 为什么不直接运行 EC-HTE？\n**W3** Venue 适配性——核心贡献更偏 causal inference methodology 而非 NLP\n**W4** \"Debiasing\" 术语歧义——NLP 社区通常指 fairness debiasing\n**W5** Abstract 数字密度过高\n\n### Reviewer 2 的 Minor Issues\n1. Reference 中 \"Audinet de Pieuchon\" 姓名拼写可能有误\n2. Table 1 与 Table 2 之间 RMSE 差异讨论不足\n3. Figure 3 y 轴标签字体偏小\n4. 25 个 Appendix 结构可精简\n5. Conclusion 偏短，缺少更广泛影响讨论\n\n### Reviewer 2 的 Missing References\n- Xia et al. (2020) instance-dependent label noise, NeurIPS\n- Cheng et al. (2022) manifold-regularized transition matrix, CVPR\n- Zhu et al. (2022) label noise for lower-quality features, ICML\n- Mahajan (2006) misclassification identification, Econometrica\n- Keith et al. (2020) text and causal inference\n- Fong & Tyler (2021) ML predictions as regression covariates\n\n### Reviewer 2 的 Questions\nQ1: 请提供 Sui et al. 2026 PPCI 引用的完整信息\nQ2: Proposition 5 相对于直接运行 EC-HTE 的 marginal value？\nQ3: A1 在 LLM annotation 中是否现实？sensitivity analysis 范围 γ_T≤0.05 偏窄\nQ4: 是否考虑过 LLM calibration (Platt scaling) 作为替代？\n\n### Reviewer 2 的总体评分\nOverall 3.5, Soundness 3.5/5, Excitement 3/5, Confidence 4/5\n\n---\n\n请对以上每一条（N1, N2, W1-W5, Minor 1-5, Q1-Q4）逐条给出 [AGREE] 或 [REBUT]，并说明理由。",
    "project": "ec_hte_llm_annotation",
    "chat_id": "oc_489afd65980834a91024fd48e21d984f",
    "director_session_key": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director"
  }
}
```

</details>

---


### Tool result

_source line 2597 · 2026-05-25T21:28:50.540998+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_489afd65980834a91024fd48e21d984f:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1309
}
```

</details>

---


### Assistant

_source line 2598 · 2026-05-25T21:28:52.989009+00:00_

交叉分享已发出。等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director"
}
```

</details>

---


## Round 200

## Round 200

2 recorded events


### User

_source line 2599 · 2026-05-25T21:28:55.757398+00:00_

[Reviewer 2 审稿结果]:
审稿报告已提交给 Review Director。

**核心判断**：Overall 3.5（Borderline Conference）。论文的 bias identity（Theorem 1）揭示了 global correction 在异质误差下的 sign reversal 现象，是超越 Frazis-Loewenstein scalar attenuation 的定性新发现，实验设计全面（520 configs × 100 MC × 8 real LLM pairs）。

**主要问题**：
1. "Sui et al., 2026" (PPCI) 引用经多次搜索无法找到——已知 PPCI 论文(arxiv:2502.06343)作者为 Cadei et al.，非 Sui et al.
2. Related Work 仅 ~7 行，严重不足，noisy label learning 文献完全缺失
3. 新颖性相对 F-L (2003) 的增量需更强论证（推导本质是 2×2 矩阵代数）
4. 标题 "Debiasing" 在 NLP 社区易与 fairness debiasing 混淆

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 2600 · 2026-05-25T21:29:00.572365+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director"
}
```

</details>

---


## Round 201

## Round 201

18 recorded events


### User

_source line 2601 · 2026-05-25T21:30:52.701115+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 交叉审查：逐条回应 Reviewer 1

---

### Must-Fix 问题

**[AGREE] R1-N1: A3 松弛下 "identity remains exact" 的声明不准确**

同意 R1 的判断。Theorem 1 的 simplified product form δ_s·Δτ/(1−2π̄) 明确依赖 A3（P(Z=0)=P(Z=1)=0.5），因为只有在 balanced classes 下 mixing matrix M_s 才等于 confusion matrix C_s，使得 M_global^{-1}·M_s 的 (1,1) entry 简化为 scalar product form。

论文在 Section 3 (p3-4) 说 "Under class imbalance (relaxing A3), the identity remains exact (R²≥0.976 at P(Z=1)=0.1)"——但 R²=0.976 ≠ 1.0 恰恰说明 simplified form 不再精确。R1 提出的区分——general matrix form（always exact）vs simplified scalar form（exact only under A2+A3）——是正确的，且对读者理解 Theorem 1 的适用范围至关重要。

补充：Appendix S (p22) 的 class imbalance 实验进一步支持了 R1 的论点。Table 21 显示在 P(Z=1) 从 0.5 偏离到 0.1-0.4 时，R² 从接近 1.0 降至 0.976，EC-HTE 的 RMSE 优势也从 ratio 1.54 收窄。这说明 product form 是一个 good approximation 但不是 exact identity。论文应如实表述。

---

**[AGREE] R1-N2: Plug-in SE 忽略 CM 估计不确定性**

同意，且我认为这个问题比 R1 描述的更严重。

(1) Algorithm 1 line 11 的 SE = sqrt(diag(Ĉ_s^{-1} · V̂)) 将 Ĉ_s 当作固定已知量处理，完全忽略了 Ĉ_s 本身的 posterior uncertainty（来自 hierarchical Bayes estimation, Section 4.1）。这等于假设 confusion matrix 已知而非估计，在 n_expert 较小时（如 n_expert=50-100）会严重低估 CI 宽度。

(2) 论文在 p7 CausalForest 段落的一个 footnote 中提到 plug-in SE 仅 93.8% coverage，bootstrap 恢复到 ≥95%——但这个关键信息不应藏在 footnote 里。Appendix X (p26) 详细讨论了 bootstrap SE，表明 bootstrap 在所有 budget levels 下均能实现 near-nominal coverage，但主文中 Algorithm 1 给出的默认流程仍是 plug-in SE。

(3) 建议同 R1：bootstrap 应成为默认推荐方案，至少在 n_expert < 250 时。Algorithm 1 应注明 plug-in SE 的 under-coverage 风险。

---

### Should-Fix 问题

**[AGREE] R1-W1: Ĉ_s^{-1} 在 asymmetric case 下应为 M̂_s^{-1}**

同意。在 A2（symmetric misclassification）下 C_s = M_s，所以 Algorithm 1 用 Ĉ_s^{-1} 在 symmetric case 下没问题。但论文 Remark 2 (p4) 明确声称结果推广到 asymmetric CMs，Appendix C (p11) 给出了 general form M_s = [[1-ε_s, ε_s], [ε'_s, 1-ε'_s]]。如果读者想在 asymmetric case 下使用 Algorithm 1，需要知道应该 invert M̂_s 而非 Ĉ_s。这是一个 notation 不一致问题，容易导致实现错误。

---

**[AGREE] R1-W2: κ 指代不一致**

同意。我在阅读时也注意到 κ 在不同上下文中指代不同矩阵的 condition number：Algorithm 1 中 κ(Ĉ_s^{-1}) 用于 guard threshold，但 Section 4 (p4-5) 的 finite-sample remainder O_p(κ²·n^{-1/2}) 中的 κ 似乎指 C_s 或 M_global 的 condition number。论文应统一 notation 或用下标区分（e.g., κ_s vs κ_global）。

---

**[AGREE with nuance] R1-W3: Operating conditions 偏窄（K≤4, n_expert≥250）**

部分同意。K≤4 和 n_expert≥250 确实限制了适用范围。特别是：
- K=8 时 EC-HTE 在固定 expert budget 下 RMSE 劣于 global correction（Appendix I.2, p15, Figure 8 右下角图），这意味着论文的方法在 fine-grained subgroups 场景下无优势。
- n_expert≥250（per subgroup）意味着 K=4 时需要 ≥1000 expert labels，这对许多 NLP 应用来说是不小的成本。

但我要补充：论文在 Section 5.4 和 Limitations (p8) 中诚实地报告了这些限制，没有回避。问题不在于方法有局限（所有方法都有），而在于论文的 framing 有时暗示 EC-HTE 是一个通用解决方案（e.g., Abstract 的 "7.4× bias reduction" 仅在 extreme heterogeneity + K=2 设置下成立）。建议在 Abstract/Introduction 中更明确地限定适用条件。

---

**[REBUT] R1-W4: Corollary 4 贡献度偏低**

不完全同意 R1 的判断。Corollary 4（population-weighted aggregate bias 为零）虽然在数学上是 Theorem 1 product structure 的直接推论，但它回答了一个重要的实践问题：**为什么 practitioners 长期使用 global correction 而没有发现问题？** 答案是 aggregate metrics 掩盖了 subgroup-level bias——biases across subgroups cancel out in expectation。

这个 insight 构成了论文叙事的关键环节：(1) Theorem 1 说 global correction 在 subgroup level 有害；(2) Corollary 4 解释了为什么这个问题一直被忽略（aggregate 看起来没问题）；(3) Proposition 5 提供了检测工具。如果移除 Corollary 4，叙事链就断了。

不过同意 R1 的隐含建议：Corollary 4 不应单独作为一个 "contribution" 列出，而应作为 Theorem 1 的自然推论在同一段内讨论。

---

### Minor Issues

**[AGREE] R1-M1: Abstract word count 合规**
确认，约 185 words，符合 ≤200 的要求。

**[AGREE] R1-M2: Figure 3 分区线与 Proposition 5 threshold 的对应关系可更明确**
同意。Figure 3 (p4) 的 "debiasing helps" / "debiasing hurts" 分区线应标注其对应的 Proposition 5 threshold 公式 π_s < ε_s/(2(1−ε_s))，便于读者直接关联理论与可视化。

**[AGREE] R1-M3: F-L 缩写首次出现在 Table 2 而非正文**
同意，Table 2 (p7) 中 "F-L" 缩写应在正文首次引用 Frazis-Loewenstein 时定义。

**[AGREE with significant reinforcement] R1-M4: Appendix J Table 10 cherry-picking 问题**

强烈同意，且我认为这个问题的严重性应升级到 Should-Fix 级别。

Remark 2 (p4) 声称 "Under asymmetric matrices, the diagnostic (Proposition 5) with r_s = (FPR_s + FNR_s)/2 achieves AUC = 0.96 across all configurations and correctly identifies all harmed subgroups across 8 semi-real LLM CMs"——但完全没有提及 Table 10 (p17) 显示 **EC-HTE 在所有 48 个 asymmetric 配置下 RMSE 均劣于 Global correction**。

这意味着：(1) diagnostic 在 asymmetric case 下能正确识别被 global correction 伤害的子群（AUC 高）；但 (2) EC-HTE 的修正本身在 asymmetric case 下反而比 global correction 更差。这是一个 critical gap：论文的 diagnostic tool 能发现问题，但提出的 correction method 在这种情况下无法解决问题。Remark 2 只报告了 (1) 而隐瞒了 (2)，属于选择性报告。

论文应在 Remark 2 中明确说明：在 asymmetric misclassification 下，EC-HTE 的 per-subgroup inversion 因需要估计两倍参数（FPR 和 FNR separately）而增加 variance，导致整体 RMSE 劣于 global correction（在 n_expert=250 时）。这不影响理论贡献的价值，但影响方法的实际推荐范围。

---

### Questions

**[AGREE] R1-Q1: A5 是否从一开始就不必要？**

有效问题。A5 要求 balanced effect modifier（P(Z=1|S=s) = 0.5 for all s）。据我阅读，Theorem 1 的证明（Appendix B, p11）在推导 τ_obs 时使用了 M_s 的结构，而 A5 确保 τ(z, s) 的权重对称。如果 A5 可以放松而 Theorem 1 仍然（至少近似地）成立，那么列出 A5 作为必要假设是误导性的。作者应在 rebuttal 中明确 A5 在证明中的确切角色。

**[AGREE] R1-Q2: κ-guard fallback 到 global correction 是否引入新的异质性偏差？**

有效且重要的问题。当部分子群使用 per-subgroup correction 而其他子群 fallback 到 global correction 时，resulting estimator 是一个 hybrid，可能比纯粹使用任一策略都更差。特别是，如果 κ-guard 触发的子群恰好是高误差子群（near-random classifier → 高 κ），那么这些子群用 global correction 会引入 Theorem 1 描述的偏差，而其他子群用 per-subgroup correction——两种修正策略的不一致可能导致 downstream CausalForest 的 splitting behavior 异常。

Appendix A.1 (p10) 讨论了 κ-guard 的设计，称 κ > 100 的阈值 "is not load-bearing"，但没有分析 hybrid correction 的理论性质。建议作者分析或至少讨论 hybrid estimator 的 bias properties。

**[AGREE] R1-Q3: Subgroup membership S 的 misspecification 影响？**

有效问题。论文假设 S 是正确观测的（已知且无误差），但在实际应用中：
- 子群定义可能不捕捉真正的 error rate heterogeneity（e.g., 按 platform 分组但真正的异质性在 text length 维度）
- S 本身可能有 measurement error（e.g., demographic subgroups 基于 self-report）
- 论文在 Appendix Y.5 (p27) 讨论了 A5 violation，但没有直接讨论 S 的 misspecification

这是一个实际部署中的重要问题，论文应至少在 Limitations 中提及。

---

### 总体评价

R1 的审稿质量很高，对方法严谨性的审查细致且有理有据。我与 R1 在大多数问题上观点一致，特别是：

1. **N1 (A3 relaxation claim)** 和 **N2 (plug-in SE)** 是实质性的技术问题，需要修正
2. **M4 (Table 10 cherry-picking)** 我认为应升级为 Should-Fix——这涉及选择性报告问题
3. **W4 (Corollary 4)** 是我唯一部分不同意的点——Corollary 4 虽然技术贡献有限，但在叙事上有不可替代的作用

两位 Reviewer 综合来看：论文理论洞察有价值，实验设计全面，但存在若干需要修正的技术表述问题和选择性报告倾向。我的 Overall 3.5 与 R1 一致。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 2602 · 2026-05-25T21:31:43.532127+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:get_visual_check_status,get_external_review_status,read_project_file,update_review_issues,submit_review_report_to_research_director",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:get_visual_check_status,get_external_review_status,read_project_file,update_review_issues,submit_review_report_to_research_director",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 2603 · 2026-05-25T21:31:43.532594+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2604 · 2026-05-25T21:31:47.096771+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__submit_review_report_to_research_director",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__submit_review_report_to_research_director",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 2605 · 2026-05-25T21:31:47.197564+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 2606 · 2026-05-25T21:31:50.962262+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "ec_hte_llm_annotation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "ec_hte_llm_annotation"
  }
}
```

</details>

---


### Tool call

_source line 2607 · 2026-05-25T21:31:50.962684+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "ec_hte_llm_annotation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "ec_hte_llm_annotation"
  }
}
```

</details>

---


### Tool result

_source line 2608 · 2026-05-25T21:31:51.414726+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-25T21:16:25.874734+00:00\", \"completed_at\": \"2026-05-25T21:20:25.257490+00:00\", \"findings\": [{\"severity\": \"info\", \"dimension\": \"page 1\", \"message\": \"首页为纯文本（Title/Abstract/Intro），无视觉锚点。Figure 1 出现在 page 2 顶部，位置优秀，锚定效应及时——审稿人翻到第二页即看到完整的 pipeline 概览图，能快速理解核心 idea。不构成问题，仅记录。\"}, {\"severity\": \"info\", \"dimension\": \"page 2\", \"message\": \"Figure 1 的 pipeline 图使用红色文字标注 \\\"Sign Reversal: 14.9% of configs\\\" 并用绿色/蓝色区分标准流程与 EC-HTE 流程。红-绿对比对红绿色盲用户存在辨识风险。建议改用 orange/blue 或添加纹理/图案区分。\"}, {\"severity\": \"info\", \"dimension\": \"page 4\", \"message\": \"Figure 3（bias amplification heatmap）内部注释文字 \\\"debiasing helps\\\" / \\\"debiasing hurts\\\" 字号偏小（约为正文 60%），在打印或缩放阅读时可能不易辨认。建议将注释文字放大至正文 70% 以上。\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Figure 5 中 \\\"Max Direct = 0.003\\\" 注释和虚线标签较密集，整体略显拥挤。Sign reversal rate 曲线的注释可考虑精简或移至 caption。\"}, {\"severity\": \"info\", \"dimension\": \"page 17\", \"message\": \"附录 Table 9（bias identity predictions under asymmetric misclassification）行列数多、字号较小，阅读体验偏密。作为附录可接受，但若审稿人需要细看会有些吃力。\"}, {\"severity\": \"info\", \"dimension\": \"page 31\", \"message\": \"末页（最后一页附录）内容约占页面 2/3，底部约 1/3 空白。包含 \\\"Use of AI Assistants\\\" 声明段落。作为附录最后一页可接受。\"}], \"counts\": {\"critical\": 0, \"warning\": 0, \"info\": 6}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 452
}
```

</details>

---


### Tool result

_source line 2609 · 2026-05-25T21:31:51.415244+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 2610 · 2026-05-25T21:31:51.566558+00:00_

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
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
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

_source line 2611 · 2026-05-25T21:31:51.667367+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 2612 · 2026-05-25T21:31:57.889660+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 2613 · 2026-05-25T21:31:58.143912+00:00_

1	issues:
2	  # === RESOLVED (prior rounds — abbreviated) ===
3	  - id: "R1-N1"
4	    summary: "Proposition 1 以 formal bound 呈现但仅有 97% MC 经验验证"
5	    category: method
6	    severity: critical
7	    status: resolved
8	    first_raised_round: 0
9	    last_seen_round: 2
10	    action_items: []
11	    resolution: "重新推导为精确恒等式"
12	    resolution_round: 0
13	
14	  - id: "R2-W8"
15	    summary: "Proposition 1 限于 K=2"
16	    category: method
17	    severity: critical
18	    status: resolved
19	    first_raised_round: 0
20	    last_seen_round: 1
21	    action_items: []
22	    resolution: "Theorem 1 适用一般 K"
23	    resolution_round: 0
24	
25	  - id: "R1-N2"
26	    summary: "Real data ground truth CATE 来源不明"
27	    category: experiment
28	    severity: critical
29	    status: resolved
30	    first_raised_round: 0
31	    last_seen_round: 1
32	    action_items: []
33	    resolution: "恰当定位为 illustrative application"
34	    resolution_round: 0
35	
36	  - id: "R1-N3"
37	    summary: "HB 模型规格严重不完整"
38	    category: method
39	    severity: critical
40	    status: resolved
41	    first_raised_round: 0
42	    last_seen_round: 1
43	    action_items: []
44	    resolution: "完整 MCMC 规格"
45	    resolution_round: 0
46	
47	  - id: "JOINT-W4"
48	    summary: "相关工作严重遗漏"
49	    category: writing
50	    severity: warning
51	    status: resolved
52	    first_raised_round: 0
53	    last_seen_round: 1
54	    action_items: []
55	    resolution: "30+ 引用覆盖"
56	    resolution_round: 0
57	
58	  - id: "JOINT-W3"
59	    summary: "信息密度过高"
60	    category: writing
61	    severity: warning
62	    status: resolved
63	    first_raised_round: 0
64	    last_seen_round: 1
65	    action_items: []
66	    resolution: "主文精简至合理密度"
67	    resolution_round: 0
68	
69	  - id: "R2-W7"
70	    summary: "真实数据验证单薄"
71	    category: experiment
72	    severity: warning
73	    status: resolved
74	    first_raised_round: 0
75	    last_seen_round: 1
76	    action_items: []
77	    resolution: "恰当定位 + 公开数据集"
78	    resolution_round: 0
7
…[truncated 27968 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "elapsed_ms": 254
}
```

</details>

---


### Tool call

_source line 2614 · 2026-05-25T21:37:03.712794+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "ec_hte_llm_annotation",
  "issues_yaml": "issues:\n  # === RESOLVED (prior rounds — abbreviated) ===\n  - id: \"R1-N1\"\n    summary: \"Proposition 1 以 formal bound 呈现但仅有 97% MC 经验验证\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 2\n    action_items: []\n    resolution: \"重新推导为精确恒等式\"\n    resolution_round: 0\n\n  - id: \"R2-W8\"\n    summary: \"Proposition 1 限于 K=2\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    action_items: []\n    resolution: \"Theorem 1 适用一般 K\"\n    resolution_round: 0\n\n  - id: \"R1-N2\"\n    summary: \"Real data ground truth CATE 来源不明\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    action_items: []\n    resolution: \"恰当定位为 illustrative application\"\n    resolution_round: 0\n\n  - id: \"R1-N3\"\n    summary: \"HB 模型规格严重不完整\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    action_items: []\n    resolution: \"完整 MCMC 规格\"\n    resolution_round: 0\n\n  - id: \"JOINT-W4\"\n    summary: \"相关工作严重遗漏\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    action_items: []\n    resolution: \"30+ 引用覆盖\"\n    resolution_round: 0\n\n  - id: \"JOINT-W3\"\n    summary: \"信息密度过高\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    action_items: []\n    resolution: \"主文精简至合理密度\"\n    resolution_round: 0\n\n  - id: \"R2-W7\"\n    summary: \"真实数据验证单薄\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    action_items: []\n    resolution: \"恰当定位 + 公开数据集\"\n    resolution_round: 0\n\n  - id: \"R1-W5\"\n    summary: \"Pages 9-10 缺 Appendix 标签\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 0\n    action_items: []\n    resolution: \"附录结构重组\"\n    resolution_round: 0\n\n  - id: \"R19-C1\"\n    summary: \"Abstract 'R²≥0.97 across synthetic grids and 11 empirical LLM CMs' 事实性错误\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    action_items: []\n    resolution: \"已修正 Abstract L4, Intro L17/L31, Conclusion L4——区分合成 vs 真实 LLM 的 R² 范围\"\n    resolution_round: 19\n\n  - id: \"R19-C2\"\n    summary: \"诊断工具 (Proposition 5) AUC=0.63 但 Abstract/Intro 呈现为核心贡献无性能限定\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    action_items: []\n    resolution: \"AUC 数字从 Abstract 完全移除\"\n    resolution_round: 19\n\n  - id: \"R19-C3\"\n    summary: \"核心量化 claims (7.4×) 在假设完全满足的合成数据上得出，moderate 配置下无改善\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    action_items: []\n    resolution: \"Abstract L6 修正为 'reducing |bias| by 7.4× under extreme heterogeneity'\"\n    resolution_round: 19\n\n  - id: \"R19-W1\"\n    summary: \"操作条件过窄——无真实 LLM-dataset pair 通过全部 5 个筛选条件\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    action_items: []\n    resolution: \"Conclusion 扩展含 relaxed screening adoption guideline\"\n    resolution_round: 19\n\n  - id: \"R19-W2\"\n    summary: \"DGP 缺乏 observational/confounding 场景验证\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    action_items: []\n    resolution: \"Limitations 已补充 confounded DGP scope\"\n    resolution_round: 19\n\n  - id: \"R19-M4\"\n    summary: \"Conclusion 过短（仅两句话）\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    action_items: []\n    resolution: \"Conclusion 从 2 句扩展到 3 句含 adoption guideline\"\n    resolution_round: 19\n\n  - id: \"R19-DATA1\"\n    summary: \"experiments.tex L19 'EC-HTE eliminates sign reversal entirely' 与 stance/AG News 数据矛盾\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    action_items: []\n    resolution: \"已限定为 primary K=2 configuration\"\n    resolution_round: 19\n\n  - id: \"R19-DATA2\"\n    summary: \"task-agnosticity 段 '16 real LLM CMs span four tasks' 与 L11 '8×2=16' 计数不一致\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    action_items: []\n    resolution: \"区分 16 core CMs 和独立 cross-task validations\"\n    resolution_round: 19\n\n  - id: \"R19-DATA3\"\n    summary: \"AG News appendix 引用 GPT-4/~85% 与源论文不符\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    action_items: []\n    resolution: \"引用细节修正完成\"\n    resolution_round: 19\n\n  - id: \"R20-M1\"\n    summary: \"Abstract 'per-model range 0.26-0.09' 数值排序应为 0.09-0.26（从小到大）\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 20\n    last_seen_round: 21\n    action_items: []\n    resolution: \"确认 Abstract 已是 '0.76--0.99'（升序），非问题\"\n    resolution_round: 21\n\n  - id: \"R19-W3\"\n    summary: \"Theorem 1→Proposition 3 呈现顺序：A5 排除目标场景但未充分强调\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 21\n    action_items: []\n    resolution: \"Proposition 3 已在主文 Section 3, 含完整公式和 Δτ_s\"\n    resolution_round: 21\n\n  - id: \"R19-M1\"\n    summary: \"Assumption (A5) 实践限制被轻描淡写\"\n    category: method\n    severity: info\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 21\n    action_items: []\n    resolution: \"Proposition 3 已在主文充分展示 A5 relaxation\"\n    resolution_round: 21\n\n  - id: \"R19-M6\"\n    summary: \"Algorithm 1 缺收敛标准/最大迭代次数\"\n    category: method\n    severity: info\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 22\n    action_items:\n      - round: 22\n        action: \"Algorithm 1 改为 EB 流程，Gibbs 降为 appendix 替代方案\"\n        assigned_to: agent\n        status: done\n    resolution: \"Algorithm 1 已改为 EB point estimates (closed-form Dirichlet update)，MCMC 保留为 appendix 验证方案。与 method.tex (<5ms) 和代码一致。\"\n    resolution_round: 22\n\n  - id: \"R22-Q1\"\n    summary: \"Method 说 empirical Bayes (<5ms) 但 Algorithm 1 描述 Gibbs sampler——不一致\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 22\n    action_items:\n      - round: 22\n        action: \"Algorithm 1 EB 化 + appendix MCMC 描述统一\"\n        assigned_to: agent\n        status: done\n    resolution: \"Algorithm 1 改为 EB，与 method.tex 和代码一致。Reviewer 验证通过。\"\n    resolution_round: 22\n\n  - id: \"R22-Q2\"\n    summary: \"A3 放松时 'identity remains exact with modified coefficients' 但未给出显式形式\"\n    category: method\n    severity: info\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 22\n    action_items:\n      - round: 22\n        action: \"Appendix D 补充 A3 放松显式推导 (M_s Bayes rule form + B_s·1=0 证明)\"\n        assigned_to: agent\n        status: done\n    resolution: \"appendix classimbalance 节新增 eq:ms_imbalanced 显式形式，证明 product form 对任意 p₀ 成立。\"\n    resolution_round: 22\n\n  - id: \"R22-Q3\"\n    summary: \"Cov(π_s, Δτ_s) 在实验中未报告——Corollary 4 实际可用性的关键\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 22\n    action_items:\n      - round: 22\n        action: \"从现有数据提取 Cov(π_s, Δτ_s) 并加入 appendix\"\n        assigned_to: agent\n        status: done\n    resolution: \"appendix A5 violation 节新增 Corollary 4 实证验证：主 grid Cov=0（aggregate bias 抵消），A5 violation Cov=±0.020（predicted ±0.029 与 MC 吻合）。\"\n    resolution_round: 22\n\n  - id: \"R22-Q4\"\n    summary: \"EC-HTE + PPCI 理论兼容性条件不明\"\n    category: method\n    severity: info\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 22\n    action_items:\n      - round: 22\n        action: \"Limitations 补充 PPCI 兼容性讨论\"\n        assigned_to: agent\n        status: done\n    resolution: \"limitations.tex 新增 PPCI 独立性讨论段落。Reviewer 验证通过。\"\n    resolution_round: 22\n\n  - id: \"R20-C1\"\n    summary: \"对称误分类假设 (A2) 限制标题级 'Exact Identity' 声称——非对称情形诊断退化\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 20\n    last_seen_round: 22\n    action_items:\n      - round: 22\n        action: \"修正 AUC 0.66→0.96（3处），因 0.66 来自错误指标\"\n        assigned_to: agent\n        status: done\n    resolution: \"AUC 0.66 来自未归一化的 raw matrix score，非 Prop 5 标量诊断。标量诊断在非对称下实际 AUC=0.96（48 configs）/ 正确识别全部 harmed subgroups（8 semi-real LLMs, 32 subgroups）。论文 3 处已更新。\"\n    resolution_round: 22\n\n  - id: \"R12-M2\"\n    summary: \"Remark 2 与 Theorem 1 假设列表表面矛盾 (A2 地位)\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 12\n    last_seen_round: 22\n    action_items: []\n    resolution: \"AUC 0.66→0.96 修正消除了 A2 限制诊断的核心论据。Remark 2 准确描述 A2 仅简化标量形式。\"\n    resolution_round: 22\n\n  - id: \"R21-N1\"\n    summary: \"非对称误分类下诊断准则 AUC 从 0.86 降至 0.65\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 22\n    action_items:\n      - round: 22\n        action: \"修正 AUC 0.66→0.96\"\n        assigned_to: agent\n        status: done\n    resolution: \"AUC 0.66 来自错误指标，标量诊断实际 AUC=0.96。论文已更新。\"\n    resolution_round: 22\n\n  - id: \"R10-W2\"\n    summary: \"DGP 较简单，无混杂变量\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 10\n    last_seen_round: 22\n    action_items: []\n    resolution: \"Limitations 已补充 confounded DGP scope。R22 未再提及。\"\n    resolution_round: 22\n\n  - id: \"R20-M2\"\n    summary: \"Theorem 1 中 'effect-modifier level z' 措辞对 NLP 读者不友好\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 20\n    last_seen_round: 22\n    action_items:\n      - round: 21\n        action: \"theory.tex Theorem 1 后增加 K=2 数值示例\"\n        assigned_to: director\n        status: done\n    resolution: \"数值示例已添加。R22 未再提及。\"\n    resolution_round: 22\n\n  - id: \"R21-FIX1\"\n    summary: \"Remark 交叉引用统一\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 22\n    action_items: []\n    resolution: \"所有引用统一。R22 未再提及。\"\n    resolution_round: 21\n\n  - id: \"R21-W2\"\n    summary: \"A3 (P(Z=0)=0.5) 限制性在正文中讨论不足\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 22\n    action_items: []\n    resolution: \"Limitations 讨论 + Appendix 显式推导均已完成。\"\n    resolution_round: 22\n\n  - id: \"R21-W3\"\n    summary: \"操作条件称 'framework' 轻微过度声称\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 22\n    action_items: []\n    resolution: \"已调整措辞。R22 确认展示透明。\"\n    resolution_round: 22\n\n  - id: \"R21-W4\"\n    summary: \"Section 3 符号密度对 NLP 读者偏高\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 22\n    action_items: []\n    resolution: \"数值示例已添加。R22 未再提及。\"\n    resolution_round: 22\n\n  - id: \"R21-REF1\"\n    summary: \"遗漏相关工作: Veitch 2020, Wood-Doughty 2018\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 22\n    action_items: []\n    resolution: \"引用已添加。R22 未再提及。\"\n    resolution_round: 21\n\n  - id: \"R17-W2\"\n    summary: \"Scalability to K>>4 未充分讨论\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 17\n    last_seen_round: 23\n    action_items: []\n    resolution: \"Intro K≤4 限定 + Section 5.4 operating conditions 覆盖。已诚实声明。\"\n    resolution_round: 22\n\n  - id: \"R19-W6\"\n    summary: \"Finite-sample 传播保证缺失——Theorem 1 到 plug-in estimator 仅有 O_p notation\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 23\n    mentions:\n      - round: 22\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 共识确认技术错误：O_p(κ·n^{-1/2}) 应为 O_p(κ²·n^{-1/2})。\"\n      - round: 23\n        reviewers: [1, 2]\n        note: \"主文已修正为 κ²，但 appendix.tex L103 仍用 κ(M_global)（单次幂），且 L1250 有链式错误。论文未解释两个 bound 的区别。\"\n    action_items:\n      - round: 22\n        action: \"theory.tex L92 修正 κ→κ²，含 Neumann expansion 解释\"\n        assigned_to: agent\n        status: done\n      - round: 23\n        action: \"appendix.tex L103 修正 κ(M_global)→κ(M_global)²，增加 Neumann expansion 解释\"\n        assigned_to: director\n        status: done\n      - round: 23\n        action: \"appendix.tex L1250 修正 κ(C_s)→κ(C_s)²\"\n        assigned_to: director\n        status: done\n    resolution: \"主文 theory.tex + appendix.tex L103 + L1250 全部统一为 κ²。L103 增加 Neumann expansion 解释。3 轮复发根因（appendix 残留 κ）已彻底消除。\"\n    resolution_round: 23\n\n  - id: \"R16-W7\"\n    summary: \"Figure 2 红绿配色色盲不友好\"\n    category: format\n    severity: info\n    status: in_progress\n    first_raised_round: 16\n    last_seen_round: 24\n    mentions:\n      - round: 24\n        reviewers: []\n        note: \"视觉审查再次检测到 Figure 1 红绿对比色盲风险。建议改用 orange/blue 或添加纹理。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R19-C4\"\n    summary: \"CausalForest 集成验证不足——缺 X-learner/BART\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 19\n    last_seen_round: 22\n    mentions:\n      - round: 22\n        reviewers: []\n        note: \"R22 未直接再提。跨估计器（CF + R-learner）是加分项。X-learner/BART 为 rebuttal 准备。\"\n    action_items:\n      - round: 19\n        action: \"Rebuttal 准备: X-learner/BART 跨估计器验证\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R19-W4\"\n    summary: \"HB 优势在 n_expert≥250 时消失但未讨论上限\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 19\n    last_seen_round: 22\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R19-W5\"\n    summary: \"缺乏 fully real-data validation (所有实验为 semi-synthetic)\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 19\n    last_seen_round: 23\n    mentions:\n      - round: 22\n        reviewers: [2]\n        note: \"R22 R2 再次强调。R1 REBUT 有力（半合成是因果推断标准范式）。降级为 moderate weakness。Rebuttal 备弹。\"\n      - round: 23\n        reviewers: [1, 2]\n        note: \"R23 两位 Reviewer 共识。R1 指出 A1 by construction 无法验证实际鲁棒性，sensitivity analysis γ_T=0.10 致 coverage 75% 暴露脆弱性。R2 同意并补充：real-data case study 可间接评估 A1 合理性。\"\n    action_items:\n      - round: 23\n        action: \"Rebuttal 论点：(a) Catch-22 论证——有 ground-truth CATE 就不需要 correction; (b) AUC 0.96 on 8 real LLMs 是真实数据验证 diagnostic; (c) semi-synthetic 是 causal inference 标准范式; (d) sensitivity analysis 诚实展示边界\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R18-SF6\"\n    summary: \"Plugin SE 欠覆盖 93.8%\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 17\n    last_seen_round: 24\n    mentions:\n      - round: 23\n        reviewers: [1, 2]\n        note: \"R1 指出 plug-in SE 不 propagate CM posterior uncertainty。R2 rebuts：bootstrap (B=100) 恢复 ≥95% coverage，HB partial pooling 隐式 regularize。分歧：R2 认为是 implementation choice with empirical justification，非 gap。\"\n      - round: 24\n        reviewers: [1, 2]\n        note: \"R24 两位 Reviewer 升级为 Must-Fix。R1 明确指出 Algorithm 1 默认 plug-in 将 Ĉ_s 当固定量，93.8% coverage 不应藏在 footnote。R2 强化：n_expert<250 时严重低估 CI 宽度。共识：bootstrap 应为默认推荐。\"\n    action_items:\n      - round: 24\n        action: \"Algorithm 1 注明 plug-in SE under-coverage 风险；bootstrap 应为 n_expert<250 默认推荐\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R18-M1\"\n    summary: \"EC-HTE wall-clock time 未报告\"\n    category: experiment\n    severity: info\n    status: open\n    first_raised_round: 18\n    last_seen_round: 22\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R17-NLP2\"\n    summary: \"论文对 NLP 社区的价值定位不清\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 17\n    last_seen_round: 23\n    mentions:\n      - round: 23\n        reviewers: [2]\n        note: \"R2 再次提出 venue fit 问题：论文本质是 causal inference methodology，NLP 作为 application domain。R1 未直接讨论 venue fit。\"\n    action_items:\n      - round: 21\n        action: \"experiments.tex §5.2 增加 CivilComments NLP insight 段落\"\n        assigned_to: director\n        status: done\n      - round: 23\n        action: \"Rebuttal 准备 venue-fit 论据：EMNLP 近年接收多篇 causal inference for NLP 论文 + LLM annotation 是 NLP 核心趋势\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R19-M2\"\n    summary: \"HB 先验敏感性分析不充分\"\n    category: method\n    severity: info\n    status: open\n    first_raised_round: 19\n    last_seen_round: 22\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R19-M3\"\n    summary: \"Bootstrap SE (B=100) 计算成本未讨论\"\n    category: experiment\n    severity: info\n    status: open\n    first_raised_round: 19\n    last_seen_round: 22\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R19-M5\"\n    summary: \"'Semi-synthetic' 术语在 Section 5.1 和 5.3 含义不同\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 19\n    last_seen_round: 22\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R20-C2\"\n    summary: \"相对 Frazis-Loewenstein (2003) 增量贡献未界定\"\n    category: framing\n    severity: critical\n    status: in_progress\n    first_raised_round: 20\n    last_seen_round: 23\n    mentions:\n      - round: 23\n        reviewers: [1, 2]\n        note: \"R2 维持 novelty depth concern。R1 提出 FWL 类比进一步限制 novelty 声称。两人共识：'careful application of known techniques to important new context'。\"\n    action_items:\n      - round: 20\n        action: \"Section 3 明确声明与 F-L 的 nesting 关系\"\n        assigned_to: director\n        status: done\n      - round: 21\n        action: \"Section 3 增加 sign reversal novelty statement\"\n        assigned_to: director\n        status: done\n      - round: 23\n        action: \"Rebuttal 论点：sign reversal 14.9% 是文献首次报告 + CivilComments 3.2× effect-size gap 改变实质结论 = impact 论据绕过 depth 争论\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R20-C3\"\n    summary: \"缺失噪声标签学习核心文献\"\n    category: writing\n    severity: warning\n    status: in_progress\n    first_raised_round: 20\n    last_seen_round: 23\n    mentions:\n      - round: 23\n        reviewers: [2]\n        note: \"R2 指出 subgroup-dependent vs instance-dependent noise 定位仍未充分讨论。\"\n    action_items:\n      - round: 20\n        action: \"Related Work 增加噪声标签学习段落\"\n        assigned_to: director\n        status: done\n      - round: 23\n        action: \"Related Work 加深 subgroup-dependent noise 定位，引用 Xia et al. 2020 instance-dependent noise\"\n        assigned_to: director\n        status: done\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R20-W1\"\n    summary: \"MC=100 不足以支撑 coverage 声称\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 20\n    last_seen_round: 23\n    mentions:\n      - round: 23\n        reviewers: [1, 2]\n        note: \"R1 重新提出：SE≈2.2pp 使 93% vs 95% coverage 不可区分。R2 同意但认为核心 claims (bias reduction, sign reversal) 不依赖精确 coverage，可降级为 info。\"\n    action_items:\n      - round: 20\n        action: \"关键配置增加至 ≥500 MC runs（rebuttal/camera-ready）\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R20-W2\"\n    summary: \"方法论技术新颖性偏浅\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 20\n    last_seen_round: 23\n    mentions:\n      - round: 23\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 共识：贡献是 'careful application of known techniques to important new context'，非 methodological breakthrough。\"\n    action_items:\n      - round: 23\n        action: \"Rebuttal 论点：不辩护 math depth，强调 problem discovery + CivilComments impact\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R20-W3\"\n    summary: \"假设 (A1) 灵敏度分析形式单一\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 20\n    last_seen_round: 23\n    mentions:\n      - round: 23\n        reviewers: [1, 2]\n        note: \"R1 指出 γ_T=0.10 致 coverage 75%，sensitivity analysis 暴露脆弱性而非证明鲁棒性。R2 同意并关联 real-data validation 缺失。\"\n    action_items:\n      - round: 20\n        action: \"增加文本特征 confounding 灵敏度分析（rebuttal/camera-ready）\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R20-M3\"\n    summary: \"Figure 2 'ε-guard' 标注字号偏小\"\n    category: format\n    severity: info\n    status: open\n    first_raised_round: 20\n    last_seen_round: 22\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R21-N2\"\n    summary: \"NLP 社区适配性不足\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 21\n    last_seen_round: 23\n    mentions:\n      - round: 23\n        reviewers: [2]\n        note: \"R2 维持：论文本质是 causal inference methodology，NLP 作为 application domain。更适合 JCI/UAI/AISTATS。R1 未直接讨论但同意 novelty 对 EMNLP 偏弱。\"\n    action_items:\n      - round: 21\n        action: \"experiments.tex §5.2 增加 CivilComments NLP insight\"\n        assigned_to: director\n        status: done\n      - round: 23\n        action: \"Rebuttal 准备 venue-fit 论据\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R21-W1\"\n    summary: \"Proposition 5 诊断 vs 直接运行 EC-HTE 的增量价值不明\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 21\n    last_seen_round: 22\n    action_items:\n      - round: 21\n        action: \"明确诊断准则的使用场景（rebuttal）\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R22-W1\"\n    summary: \"κ-guard 阈值 100 缺乏与 O_p(κ²·n^{-1/2}) 的理论连接\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 22\n    last_seen_round: 24\n    mentions:\n      - round: 23\n        reviewers: [2]\n        note: \"R2 Q3 问 Δπ>0.15 阈值是否有理论推导。R1 认为有理论依据但 REBUT 程度不一。\"\n      - round: 24\n        reviewers: [1, 2]\n        note: \"R24 Q2 追问 κ-guard fallback 到 global correction 是否引入新的异质性偏差。hybrid estimator 理论性质未分析。\"\n    action_items:\n      - round: 22\n        action: \"基于 O_p(κ²·n^{-1/2}) 推导理论最优 κ 阈值（rebuttal）\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R22-W2\"\n    summary: \"EB 两阶段低估后验不确定性\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 22\n    last_seen_round: 24\n    mentions:\n      - round: 23\n        reviewers: [1, 2]\n        note: \"R1 W10 提出 SE 不 propagate CM uncertainty。R2 rebuts 认为 bootstrap 已解决。分歧。\"\n      - round: 24\n        reviewers: [1, 2]\n        note: \"R24 升级为 Must-Fix N2。共识：plug-in SE 将 Ĉ_s 当固定量是技术缺陷。bootstrap 应为默认。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R22-W8\"\n    summary: \"Abstract 信息密度过高（12+ 具体数字）\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 22\n    last_seen_round: 23\n    mentions:\n      - round: 23\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 再次共识。Camera-ready 处理。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R22-W9\"\n    summary: \"Debiasing 术语歧义（fairness vs measurement-error）\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 22\n    last_seen_round: 23\n    mentions:\n      - round: 23\n        reviewers: [2]\n        note: \"R2 再次提出。标题中 'debiasing' 在 NLP 社区有 fairness 歧义。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R22-W10\"\n    summary: \"Per-model R² 低端讨论不足（R²=0.76 削弱 exact framing）\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 22\n    last_seen_round: 24\n    mentions:\n      - round: 23\n        reviewers: [1, 2]\n        note: \"R1 指出 R²=0.76 削弱 'exact' 说服力（24% 未解释方差）。R2 同意。升级至 warning。论文未对低 R² case 做 failure analysis。\"\n      - round: 24\n        reviewers: [1, 2]\n        note: \"R24 N1 直接引用 R²=0.976 at P(Z=1)=0.1 作为 simplified form 不精确的证据。与 per-model R²=0.76 共同削弱 'exact identity' 叙事。\"\n    action_items:\n      - round: 23\n        action: \"Rebuttal 准备：per-model R² 回归分析 (R² ~ FPR, FNR, |FPR-FNR|, κ, P(Z=1), n)\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R22-REF1\"\n    summary: \"缺 Filtered PPI 引用 (arXiv:2602.10464)\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 22\n    last_seen_round: 23\n    mentions:\n      - round: 23\n        reviewers: [1, 2]\n        note: \"R2 再次指出。R1 表示无法独立验证但认为 plausible。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R23-W1\"\n    summary: \"诊断 AUC=0.86 (symmetric case) 缺乏 decision-consequence 分析\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 23\n    last_seen_round: 23\n    mentions:\n      - round: 23\n        reviewers: [1, 2]\n        note: \"AUC=0.86 在 symmetric case 下有非平凡误判率。论文未讨论 FP/FN 不对称代价（false negative 后果远重于 false positive）。建议 precision/recall breakdown 和 decision threshold tradeoff。\"\n    action_items:\n      - round: 23\n        action: \"Rebuttal 准备：从现有数据提取 precision/recall curve + 推荐保守 threshold\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R23-W2\"\n    summary: \"'Debiasing hurts' framing 在 moderate heterogeneity 下不成立\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 23\n    last_seen_round: 24\n    mentions:\n      - round: 23\n        reviewers: [1, 2]\n        note: \"标题暗示 debiasing 普遍有害，但论文表明仅在 extreme heterogeneity 下成立。\"\n      - round: 24\n        reviewers: [1, 2]\n        note: \"R24 W3 再次指出 Abstract '7.4× bias reduction' 仅在 extreme heterogeneity + K=2 下成立。要求 Abstract/Intro 更明确限定适用条件。\"\n    action_items:\n      - round: 23\n        action: \"Intro L12 增加 'when error rates vary across subgroups' 限定\"\n        assigned_to: director\n        status: done\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R23-Q1\"\n    summary: \"Propensity score estimation error 与 CM estimation error 的交互效应未讨论\"\n    category: method\n    severity: info\n    status: open\n    first_raised_round: 23\n    last_seen_round: 23\n    mentions:\n      - round: 23\n        reviewers: [1, 2]\n        note: \"观察性研究中 treatment assignment 和 outcome measurement 同时含噪。Identity 在 joint estimation error 下是否成立？\"\n    action_items:\n      - round: 23\n        action: \"Rebuttal 论点：Identity 作用于 correction layer 独立于下游估计器\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R23-L1\"\n    summary: \"Figure 4 漂出正文到 References 页\"\n    category: format\n    severity: warning\n    status: open\n    first_raised_round: 23\n    last_seen_round: 23\n    mentions:\n      - round: 23\n        reviewers: []\n        note: \"视觉审查检测。正文 Section 5.3 引用但 float 越界到 p.9。\"\n    action_items:\n      - round: 23\n        action: \"调整 float placement 或缩小 Figure 3/Table 1\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R23-L2\"\n    summary: \"p.8 极度拥挤（Figure 3 + Table 1 + §5.4 + Conclusion + Limitations）\"\n    category: format\n    severity: info\n    status: open\n    first_raised_round: 23\n    last_seen_round: 23\n    mentions:\n      - round: 23\n        reviewers: []\n        note: \"视觉审查检测。Conclusion 仅 ~12 行。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  # === R24 NEW ISSUES ===\n\n  - id: \"R24-N1\"\n    summary: \"A3 松弛下 'identity remains exact' 声称不准确——simplified product form 是近似非精确\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 24\n    last_seen_round: 24\n    mentions:\n      - round: 24\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 共识。Theorem 1 simplified form δ_s·Δτ/(1−2π̄) 依赖 A3 (balanced classes)。R²=0.976 at P(Z=1)=0.1 证明 simplified form 非 exact。需区分 general matrix form (always exact) vs simplified scalar form (exact only under A2+A3)。Section 3 p3-4 和 Appendix S p22 的措辞应如实表述。\"\n    action_items:\n      - round: 24\n        action: \"Section 3 修正：区分 general matrix form (exact for any class balance) 和 simplified scalar product form (exact under A3)。将 'identity remains exact' 改为 'matrix form remains exact; scalar approximation achieves R²≥0.976'\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R24-N2\"\n    summary: \"Algorithm 1 plug-in SE 忽略 CM 估计不确定性——bootstrap 应为默认\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 24\n    last_seen_round: 24\n    mentions:\n      - round: 24\n        reviewers: [1, 2]\n        note: \"共识。Algorithm 1 L11 SE=sqrt(diag(Ĉ_s^{-1}·V̂)) 将 Ĉ_s 当固定已知量。93.8% coverage 信息藏在 footnote。Appendix X 证明 bootstrap 恢复 ≥95% coverage。R2 强化：n_expert<250 时严重低估 CI。两位要求 bootstrap 成为默认推荐，Algorithm 1 须注明风险。\"\n    action_items:\n      - round: 24\n        action: \"Algorithm 1 注明 plug-in SE 的 under-coverage 风险，推荐 n_expert<250 时用 bootstrap\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R24-W1\"\n    summary: \"Ĉ_s^{-1} 在 asymmetric case 应为 M̂_s^{-1}——notation 不一致易致实现错误\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 24\n    last_seen_round: 24\n    mentions:\n      - round: 24\n        reviewers: [1, 2]\n        note: \"共识。A2 下 C_s=M_s 无碍，但 Remark 2 声称推广到 asymmetric，Appendix C 给出 general M_s。Algorithm 1 应说明 asymmetric case 需 invert M̂_s 而非 Ĉ_s。\"\n    action_items:\n      - round: 24\n        action: \"Algorithm 1 或 Remark 2 注明：asymmetric case 用 M̂_s^{-1} 替代 Ĉ_s^{-1}\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R24-W2\"\n    summary: \"κ 指代不一致——Algorithm 1 κ(Ĉ_s^{-1}) vs Section 4 O_p(κ²·n^{-1/2}) 中的 κ\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 24\n    last_seen_round: 24\n    mentions:\n      - round: 24\n        reviewers: [1, 2]\n        note: \"共识。κ 在不同上下文指代不同矩阵的 condition number。需用下标区分（κ_s vs κ_global）或统一说明。\"\n    action_items:\n      - round: 24\n        action: \"统一 κ 符号，用下标区分 κ_s (per-subgroup) 和 κ_global\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R24-W3\"\n    summary: \"Operating conditions (K≤4, n_expert≥250) 在 Abstract/Intro 限定不足\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 24\n    last_seen_round: 24\n    mentions:\n      - round: 24\n        reviewers: [1, 2]\n        note: \"K=8 时 EC-HTE RMSE 劣于 global (Appendix I.2 Figure 8)。n_expert≥250 per subgroup → K=4 需 ≥1000 expert labels。Abstract '7.4×' 仅 extreme heterogeneity + K=2。Section 5.4/Limitations 诚实但 Abstract/Intro framing 暗示通用性。R2 认为需更明确限定。\"\n    action_items:\n      - round: 24\n        action: \"Abstract/Intro 加入 K≤4 / n_expert≥250 适用条件的明确限定\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R24-W4\"\n    summary: \"Corollary 4 贡献度：数学贡献有限但叙事价值有争议\"\n    category: framing\n    severity: info\n    status: open\n    first_raised_round: 24\n    last_seen_round: 24\n    mentions:\n      - round: 24\n        reviewers: [1, 2]\n        note: \"R1 认为 Corollary 4 是 Theorem 1 的 trivial 推论，不应单列贡献。R2 部分 REBUT：Corollary 4 回答了 'why practitioners missed the problem'，叙事不可替代。共识：不应单独作为 contribution 列出，应作为 Theorem 1 段内推论。\"\n    action_items:\n      - round: 24\n        action: \"Corollary 4 从独立贡献降级为 Theorem 1 段内自然推论\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R24-W5\"\n    summary: \"Remark 2 选择性报告——报 diagnostic AUC=0.96 但隐瞒 EC-HTE 在 asymmetric case RMSE 全劣\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 24\n    last_seen_round: 24\n    mentions:\n      - round: 24\n        reviewers: [1, 2]\n        note: \"R2 升级为 Should-Fix（R1 原为 Minor M4）。Table 10 (p17) 显示 EC-HTE 在所有 48 个 asymmetric 配置下 RMSE 均劣于 Global。Remark 2 只报告诊断 AUC=0.96 而隐瞒校正方法本身在此场景下失效。这是选择性报告问题——diagnostic 能发现问题但 correction 无法解决。论文应在 Remark 2 明确说明。\"\n    action_items:\n      - round: 24\n        action: \"Remark 2 补充：asymmetric case 下 EC-HTE per-subgroup inversion 因估计两倍参数增加 variance，RMSE 劣于 global correction。影响方法推荐范围。\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R24-Q1\"\n    summary: \"A5 (balanced effect modifier) 是否从一开始就不必要？\"\n    category: method\n    severity: info\n    status: open\n    first_raised_round: 24\n    last_seen_round: 24\n    mentions:\n      - round: 24\n        reviewers: [1, 2]\n        note: \"A5 要求 P(Z=1|S=s)=0.5。若 Theorem 1 无需 A5 即可成立（至少近似），则列出 A5 为必要假设是误导。Appendix B 证明中 A5 的确切角色需明确。\"\n    action_items:\n      - round: 24\n        action: \"Rebuttal 明确 A5 在 Theorem 1 证明中的确切角色\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R24-Q2\"\n    summary: \"κ-guard fallback 到 global correction 的 hybrid estimator 理论性质未分析\"\n    category: method\n    severity: info\n    status: open\n    first_raised_round: 24\n    last_seen_round: 24\n    mentions:\n      - round: 24\n        reviewers: [1, 2]\n        note: \"部分子群 per-subgroup + 部分子群 global = hybrid estimator。高 κ 子群恰好是高误差子群，fallback 到 global 引入 Theorem 1 描述的偏差。两种策略不一致可能致 CausalForest splitting 异常。Appendix A.1 称 κ>100 'not load-bearing' 但未分析 hybrid 性质。\"\n    action_items:\n      - round: 24\n        action: \"Rebuttal/Discussion 补充 hybrid estimator bias properties 分析\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R24-Q3\"\n    summary: \"Subgroup membership S 的 misspecification 影响未讨论\"\n    category: method\n    severity: info\n    status: open\n    first_raised_round: 24\n    last_seen_round: 24\n    mentions:\n      - round: 24\n        reviewers: [1, 2]\n        note: \"论文假设 S 正确观测。实际中：(1) 子群定义可能不捕捉真正的 error rate heterogeneity；(2) S 本身可能有 measurement error；(3) Appendix Y.5 讨论 A5 violation 但不含 S misspecification。应至少在 Limitations 提及。\"\n    action_items:\n      - round: 24\n        action: \"Limitations 补充 subgroup membership misspecification 讨论\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R24-M1\"\n    summary: \"Figure 3 分区线应标注 Proposition 5 threshold 公式\"\n    category: format\n    severity: info\n    status: open\n    first_raised_round: 24\n    last_seen_round: 24\n    mentions:\n      - round: 24\n        reviewers: [1, 2]\n        note: \"Figure 3 'debiasing helps'/'debiasing hurts' 分区线应标注对应 π_s < ε_s/(2(1−ε_s))。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R24-M2\"\n    summary: \"F-L 缩写首次出现在 Table 2 而非正文\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 24\n    last_seen_round: 24\n    mentions:\n      - round: 24\n        reviewers: [1, 2]\n        note: \"Table 2 中 'F-L' 应在正文首次引用 Frazis-Loewenstein 时定义。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "ec_hte_llm_annotation",
    "issues_yaml": "issues:\n  # === RESOLVED (prior rounds — abbreviated) ===\n  - id: \"R1-N1\"\n    summary: \"Proposition 1 以 formal bound 呈现但仅有 97% MC 经验验证\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 2\n    action_items: []\n    resolution: \"重新推导为精确恒等式\"\n    resolution_round: 0\n\n  - id: \"R2-W8\"\n    summary: \"Proposition 1 限于 K=2\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    action_items: []\n    resolution: \"Theorem 1 适用一般 K\"\n    resolution_round: 0\n\n  - id: \"R1-N2\"\n    summary: \"Real data ground truth CATE 来源不明\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    action_items: []\n    resolution: \"恰当定位为 illustrative application\"\n    resolution_round: 0\n\n  - id: \"R1-N3\"\n    summary: \"HB 模型规格严重不完整\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    action_items: []\n    resolution: \"完整 MCMC 规格\"\n    resolution_round: 0\n\n  - id: \"JOINT-W4\"\n    summary: \"相关工作严重遗漏\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    action_items: []\n    resolution: \"30+ 引用覆盖\"\n    resolution_round: 0\n\n  - id: \"JOINT-W3\"\n    summary: \"信息密度过高\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    action_items: []\n    resolution: \"主文精简至合理密度\"\n    resolution_round: 0\n\n  - id: \"R2-W7\"\n    summary: \"真实数据验证单薄\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    action_items: []\n    resolution: \"恰当定位 + 公开数据集\"\n    resolution_round: 0\n\n  - id: \"R1-W5\"\n    summary: \"Pages 9-10 缺 Appendix 标签\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 0\n    action_items: []\n    resolution: \"附录结构重组\"\n    resolution_round: 0\n\n  - id: \"R19-C1\"\n    summary: \"Abstract 'R²≥0.97 across synthetic grids and 11 empirical LLM CMs' 事实性错误\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    action_items: []\n    resolution: \"已修正 Abstract L4, Intro L17/L31, Conclusion L4——区分合成 vs 真实 LLM 的 R² 范围\"\n    resolution_round: 19\n\n  - id: \"R19-C2\"\n    summary: \"诊断工具 (Proposition 5) AUC=0.63 但 Abstract/Intro 呈现为核心贡献无性能限定\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    action_items: []\n    resolution: \"AUC 数字从 Abstract 完全移除\"\n    resolution_round: 19\n\n  - id: \"R19-C3\"\n    summary: \"核心量化 claims (7.4×) 在假设完全满足的合成数据上得出，moderate 配置下无改善\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    action_items: []\n    resolution: \"Abstract L6 修正为 'reducing |bias| by 7.4× under extreme heterogeneity'\"\n    resolution_round: 19\n\n  - id: \"R19-W1\"\n    summary: \"操作条件过窄——无真实 LLM-dataset pair 通过全部 5 个筛选条件\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    action_items: []\n    resolution: \"Conclusion 扩展含 relaxed screening adoption guideline\"\n    resolution_round: 19\n\n  - id: \"R19-W2\"\n    summary: \"DGP 缺乏 observational/confounding 场景验证\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    action_items: []\n    resolution: \"Limitations 已补充 confounded DGP scope\"\n    resolution_round: 19\n\n  - id: \"R19-M4\"\n    summary: \"Conclusion 过短（仅两句话）\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    action_items: []\n    resolution: \"Conclusion 从 2 句扩展到 3 句含 adoption guideline\"\n    resolution_round: 19\n\n  - id: \"R19-DATA1\"\n    summary: \"experiments.tex L19 'EC-HTE eliminates sign reversal entirely' 与 stance/AG News 数据矛盾\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    action_items: []\n    resolution: \"已限定为 primary K=2 configuration\"\n    resolution_round: 19\n\n  - id: \"R19-DATA2\"\n    summary: \"task-agnosticity 段 '16 real LLM CMs span four tasks' 与 L11 '8×2=16' 计数不一致\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    action_items: []\n    resolution: \"区分 16 core CMs 和独立 cross-task validations\"\n    resolution_round: 19\n\n  - id: \"R19-DATA3\"\n    summary: \"AG News appendix 引用 GPT-4/~85% 与源论文不符\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    action_items: []\n    resolution: \"引用细节修正完成\"\n    resolution_round: 19\n\n  - id: \"R20-M1\"\n    summary: \"Abstract 'per-model range 0.26-0.09' 数值排序应为 0.09-0.26（从小到大）\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 20\n    last_seen_round: 21\n    action_items: []\n    resolution: \"确认 Abstract 已是 '0.76--0.99'（升序），非问题\"\n    resolution_round: 21\n\n  - id: \"R19-W3\"\n    summary: \"Theorem 1→Proposition 3 呈现顺序：A5 排除目标场景但未充分强调\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 21\n    action_items: []\n    resolution: \"Proposition 3 已在主文 Section 3, 含完整公式和 Δτ_s\"\n    resolution_round: 21\n\n  - id: \"R19-M1\"\n    summary: \"Assumption (A5) 实践限制被轻描淡写\"\n    category: method\n    severity: info\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 21\n    action_items: []\n    resolution: \"Proposition 3 已在主文充分展示 A5 relaxation\"\n    resolution_round: 21\n\n  - id: \"R19-M6\"\n    summary: \"Algorithm 1 缺收敛标准/最大迭代次数\"\n    category: method\n    severity: info\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 22\n    action_items:\n      - round: 22\n        action: \"Algorithm 1 改为 EB 流程，Gibbs 降为 appendix 替代方案\"\n        assigned_to: agent\n        status: done\n    resolution: \"Algorithm 1 已改为 EB point estimates (closed-form Dirichlet update)，MCMC 保留为 appendix 验证方案。与 method.tex (<5ms) 和代码一致。\"\n    resolution_round: 22\n\n  - id: \"R22-Q1\"\n    summary: \"Method 说 empirical Bayes (<5ms) 但 Algorithm 1 描述 Gibbs sampler——不一致\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 22\n    action_items:\n      - round: 22\n        action: \"Algorithm 1 EB 化 + appendix MCMC 描述统一\"\n        assigned_to: agent\n        status: done\n    resolution: \"Algorithm 1 改为 EB，与 method.tex 和代码一致。Reviewer 验证通过。\"\n    resolution_round: 22\n\n  - id: \"R22-Q2\"\n    summary: \"A3 放松时 'identity remains exact with modified coefficients' 但未给出显式形式\"\n    category: method\n    severity: info\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 22\n    action_items:\n      - round: 22\n        action: \"Appendix D 补充 A3 放松显式推导 (M_s Bayes rule form + B_s·1=0 证明)\"\n        assigned_to: agent\n        status: done\n    resolution: \"appendix classimbalance 节新增 eq:ms_imbalanced 显式形式，证明 product form 对任意 p₀ 成立。\"\n    resolution_round: 22\n\n  - id: \"R22-Q3\"\n    summary: \"Cov(π_s, Δτ_s) 在实验中未报告——Corollary 4 实际可用性的关键\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 22\n    action_items:\n      - round: 22\n        action: \"从现有数据提取 Cov(π_s, Δτ_s) 并加入 appendix\"\n        assigned_to: agent\n        status: done\n    resolution: \"appendix A5 violation 节新增 Corollary 4 实证验证：主 grid Cov=0（aggregate bias 抵消），A5 violation Cov=±0.020（predicted ±0.029 与 MC 吻合）。\"\n    resolution_round: 22\n\n  - id: \"R22-Q4\"\n    summary: \"EC-HTE + PPCI 理论兼容性条件不明\"\n    category: method\n    severity: info\n    status: resolved\n    first_raised_round: 22\n    last_seen_round: 22\n    action_items:\n      - round: 22\n        action: \"Limitations 补充 PPCI 兼容性讨论\"\n        assigned_to: agent\n        status: done\n    resolution: \"limitations.tex 新增 PPCI 独立性讨论段落。Reviewer 验证通过。\"\n    resolution_round: 22\n\n  - id: \"R20-C1\"\n    summary: \"对称误分类假设 (A2) 限制标题级 'Exact Identity' 声称——非对称情形诊断退化\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 20\n    last_seen_round: 22\n    action_items:\n      - round: 22\n        action: \"修正 AUC 0.66→0.96（3处），因 0.66 来自错误指标\"\n        assigned_to: agent\n        status: done\n    resolution: \"AUC 0.66 来自未归一化的 raw matrix score，非 Prop 5 标量诊断。标量诊断在非对称下实际 AUC=0.96（48 configs）/ 正确识别全部 harmed subgroups（8 semi-real LLMs, 32 subgroups）。论文 3 处已更新。\"\n    resolution_round: 22\n\n  - id: \"R12-M2\"\n    summary: \"Remark 2 与 Theorem 1 假设列表表面矛盾 (A2 地位)\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 12\n    last_seen_round: 22\n    action_items: []\n    resolution: \"AUC 0.66→0.96 修正消除了 A2 限制诊断的核心论据。Remark 2 准确描述 A2 仅简化标量形式。\"\n    resolution_round: 22\n\n  - id: \"R21-N1\"\n    summary: \"非对称误分类下诊断准则 AUC 从 0.86 降至 0.65\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 22\n    action_items:\n      - round: 22\n        action: \"修正 AUC 0.66→0.96\"\n        assigned_to: agent\n        status: done\n    resolution: \"AUC 0.66 来自错误指标，标量诊断实际 AUC=0.96。论文已更新。\"\n    resolution_round: 22\n\n  - id: \"R10-W2\"\n    summary: \"DGP 较简单，无混杂变量\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 10\n    last_seen_round: 22\n    action_items: []\n    resolution: \"Limitations 已补充 confounded DGP scope。R22 未再提及。\"\n    resolution_round: 22\n\n  - id: \"R20-M2\"\n    summary: \"Theorem 1 中 'effect-modifier level z' 措辞对 NLP 读者不友好\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 20\n    last_seen_round: 22\n    action_items:\n      - round: 21\n        action: \"theory.tex Theorem 1 后增加 K=2 数值示例\"\n        assigned_to: director\n        status: done\n    resolution: \"数值示例已添加。R22 未再提及。\"\n    resolution_round: 22\n\n  - id: \"R21-FIX1\"\n    summary: \"Remark 交叉引用统一\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 22\n    action_items: []\n    resolution: \"所有引用统一。R22 未再提及。\"\n    resolution_round: 21\n\n  - id: \"R21-W2\"\n    summary: \"A3 (P(Z=0)=0.5) 限制性在正文中讨论不足\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 22\n    action_items: []\n    resolution: \"Limitations 讨论 + Appendix 显式推导均已完成。\"\n    resolution_round: 22\n\n  - id: \"R21-W3\"\n    summary: \"操作条件称 'framework' 轻微过度声称\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 22\n    action_items: []\n    resolution: \"已调整措辞。R22 确认展示透明。\"\n    resolution_round: 22\n\n  - id: \"R21-W4\"\n    summary: \"Section 3 符号密度对 NLP 读者偏高\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 22\n    action_items: []\n    resolution: \"数值示例已添加。R22 未再提及。\"\n    resolution_round: 22\n\n  - id: \"R21-REF1\"\n    summary: \"遗漏相关工作: Veitch 2020, Wood-Doughty 2018\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 21\n    last_seen_round: 22\n    action_items: []\n    resolution: \"引用已添加。R22 未再提及。\"\n    resolution_round: 21\n\n  - id: \"R17-W2\"\n    summary: \"Scalability to K>>4 未充分讨论\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 17\n    last_seen_round: 23\n    action_items: []\n    resolution: \"Intro K≤4 限定 + Section 5.4 operating conditions 覆盖。已诚实声明。\"\n    resolution_round: 22\n\n  - id: \"R19-W6\"\n    summary: \"Finite-sample 传播保证缺失——Theorem 1 到 plug-in estimator 仅有 O_p notation\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 23\n    mentions:\n      - round: 22\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 共识确认技术错误：O_p(κ·n^{-1/2}) 应为 O_p(κ²·n^{-1/2})。\"\n      - round: 23\n        reviewers: [1, 2]\n        note: \"主文已修正为 κ²，但 appendix.tex L103 仍用 κ(M_global)（单次幂），且 L1250 有链式错误。论文未解释两个 bound 的区别。\"\n    action_items:\n      - round: 22\n        action: \"theory.tex L92 修正 κ→κ²，含 Neumann expansion 解释\"\n        assigned_to: agent\n        status: done\n      - round: 23\n        action: \"appendix.tex L103 修正 κ(M_global)→κ(M_global)²，增加 Neumann expansion 解释\"\n        assigned_to: director\n        status: done\n      - round: 23\n        action: \"appendix.tex L1250 修正 κ(C_s)→κ(C_s)²\"\n        assigned_to: director\n        status: done\n    resolution: \"主文 theory.tex + appendix.tex L103 + L1250 全部统一为 κ²。L103 增加 Neumann expansion 解释。3 轮复发根因（appendix 残留 κ）已彻底消除。\"\n    resolution_round: 23\n\n  - id: \"R16-W7\"\n    summary: \"Figure 2 红绿配色色盲不友好\"\n    category: format\n    severity: info\n    status: in_progress\n    first_raised_round: 16\n    last_seen_round: 24\n    mentions:\n      - round: 24\n        reviewers: []\n        note: \"视觉审查再次检测到 Figure 1 红绿对比色盲风险。建议改用 orange/blue 或添加纹理。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R19-C4\"\n    summary: \"CausalForest 集成验证不足——缺 X-learner/BART\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 19\n    last_seen_round: 22\n    mentions:\n      - round: 22\n        reviewers: []\n        note: \"R22 未直接再提。跨估计器（CF + R-learner）是加分项。X-learner/BART 为 rebuttal 准备。\"\n    action_items:\n      - round: 19\n        action: \"Rebuttal 准备: X-learner/BART 跨估计器验证\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R19-W4\"\n    summary: \"HB 优势在 n_expert≥250 时消失但未讨论上限\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 19\n    last_seen_round: 22\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R19-W5\"\n    summary: \"缺乏 fully real-data validation (所有实验为 semi-synthetic)\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 19\n    last_seen_round: 23\n    mentions:\n      - round: 22\n        reviewers: [2]\n        note: \"R22 R2 再次强调。R1 REBUT 有力（半合成是因果推断标准范式）。降级为 moderate weakness。Rebuttal 备弹。\"\n      - round: 23\n        reviewers: [1, 2]\n        note: \"R23 两位 Reviewer 共识。R1 指出 A1 by construction 无法验证实际鲁棒性，sensitivity analysis γ_T=0.10 致 coverage 75% 暴露脆弱性。R2 同意并补充：real-data case study 可间接评估 A1 合理性。\"\n    action_items:\n      - round: 23\n        action: \"Rebuttal 论点：(a) Catch-22 论证——有 ground-truth CATE 就不需要 correction; (b) AUC 0.96 on 8 real LLMs 是真实数据验证 diagnostic; (c) semi-synthetic 是 causal inference 标准范式; (d) sensitivity analysis 诚实展示边界\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R18-SF6\"\n    summary: \"Plugin SE 欠覆盖 93.8%\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 17\n    last_seen_round: 24\n    mentions:\n      - round: 23\n        reviewers: [1, 2]\n        note: \"R1 指出 plug-in SE 不 propagate CM posterior uncertainty。R2 rebuts：bootstrap (B=100) 恢复 ≥95% coverage，HB partial pooling 隐式 regularize。分歧：R2 认为是 implementation choice with empirical justification，非 gap。\"\n      - round: 24\n        reviewers: [1, 2]\n        note: \"R24 两位 Reviewer 升级为 Must-Fix。R1 明确指出 Algorithm 1 默认 plug-in 将 Ĉ_s 当固定量，93.8% coverage 不应藏在 footnote。R2 强化：n_expert<250 时严重低估 CI 宽度。共识：bootstrap 应为默认推荐。\"\n    action_items:\n      - round: 24\n        action: \"Algorithm 1 注明 plug-in SE under-coverage 风险；bootstrap 应为 n_expert<250 默认推荐\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R18-M1\"\n    summary: \"EC-HTE wall-clock time 未报告\"\n    category: experiment\n    severity: info\n    status: open\n    first_raised_round: 18\n    last_seen_round: 22\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R17-NLP2\"\n    summary: \"论文对 NLP 社区的价值定位不清\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 17\n    last_seen_round: 23\n    mentions:\n      - round: 23\n        reviewers: [2]\n        note: \"R2 再次提出 venue fit 问题：论文本质是 causal inference methodology，NLP 作为 application domain。R1 未直接讨论 venue fit。\"\n    action_items:\n      - round: 21\n        action: \"experiments.tex §5.2 增加 CivilComments NLP insight 段落\"\n        assigned_to: director\n        status: done\n      - round: 23\n        action: \"Rebuttal 准备 venue-fit 论据：EMNLP 近年接收多篇 causal inference for NLP 论文 + LLM annotation 是 NLP 核心趋势\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R19-M2\"\n    summary: \"HB 先验敏感性分析不充分\"\n    category: method\n    severity: info\n    status: open\n    first_raised_round: 19\n    last_seen_round: 22\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R19-M3\"\n    summary: \"Bootstrap SE (B=100) 计算成本未讨论\"\n    category: experiment\n    severity: info\n    status: open\n    first_raised_round: 19\n    last_seen_round: 22\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R19-M5\"\n    summary: \"'Semi-synthetic' 术语在 Section 5.1 和 5.3 含义不同\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 19\n    last_seen_round: 22\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R20-C2\"\n    summary: \"相对 Frazis-Loewenstein (2003) 增量贡献未界定\"\n    category: framing\n    severity: critical\n    status: in_progress\n    first_raised_round: 20\n    last_seen_round: 23\n    mentions:\n      - round: 23\n        reviewers: [1, 2]\n        note: \"R2 维持 novelty depth concern。R1 提出 FWL 类比进一步限制 novelty 声称。两人共识：'careful application of known techniques to important new context'。\"\n    action_items:\n      - round: 20\n        action: \"Section 3 明确声明与 F-L 的 nesting 关系\"\n        assigned_to: director\n        status: done\n      - round: 21\n        action: \"Section 3 增加 sign reversal novelty statement\"\n        assigned_to: director\n        status: done\n      - round: 23\n        action: \"Rebuttal 论点：sign reversal 14.9% 是文献首次报告 + CivilComments 3.2× effect-size gap 改变实质结论 = impact 论据绕过 depth 争论\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R20-C3\"\n    summary: \"缺失噪声标签学习核心文献\"\n    category: writing\n    severity: warning\n    status: in_progress\n    first_raised_round: 20\n    last_seen_round: 23\n    mentions:\n      - round: 23\n        reviewers: [2]\n        note: \"R2 指出 subgroup-dependent vs instance-dependent noise 定位仍未充分讨论。\"\n    action_items:\n      - round: 20\n        action: \"Related Work 增加噪声标签学习段落\"\n        assigned_to: director\n        status: done\n      - round: 23\n        action: \"Related Work 加深 subgroup-dependent noise 定位，引用 Xia et al. 2020 instance-dependent noise\"\n        assigned_to: director\n        status: done\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R20-W1\"\n    summary: \"MC=100 不足以支撑 coverage 声称\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 20\n    last_seen_round: 23\n    mentions:\n      - round: 23\n        reviewers: [1, 2]\n        note: \"R1 重新提出：SE≈2.2pp 使 93% vs 95% coverage 不可区分。R2 同意但认为核心 claims (bias reduction, sign reversal) 不依赖精确 coverage，可降级为 info。\"\n    action_items:\n      - round: 20\n        action: \"关键配置增加至 ≥500 MC runs（rebuttal/camera-ready）\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R20-W2\"\n    summary: \"方法论技术新颖性偏浅\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 20\n    last_seen_round: 23\n    mentions:\n      - round: 23\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 共识：贡献是 'careful application of known techniques to important new context'，非 methodological breakthrough。\"\n    action_items:\n      - round: 23\n        action: \"Rebuttal 论点：不辩护 math depth，强调 problem discovery + CivilComments impact\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R20-W3\"\n    summary: \"假设 (A1) 灵敏度分析形式单一\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 20\n    last_seen_round: 23\n    mentions:\n      - round: 23\n        reviewers: [1, 2]\n        note: \"R1 指出 γ_T=0.10 致 coverage 75%，sensitivity analysis 暴露脆弱性而非证明鲁棒性。R2 同意并关联 real-data validation 缺失。\"\n    action_items:\n      - round: 20\n        action: \"增加文本特征 confounding 灵敏度分析（rebuttal/camera-ready）\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R20-M3\"\n    summary: \"Figure 2 'ε-guard' 标注字号偏小\"\n    category: format\n    severity: info\n    status: open\n    first_raised_round: 20\n    last_seen_round: 22\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R21-N2\"\n    summary: \"NLP 社区适配性不足\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 21\n    last_seen_round: 23\n    mentions:\n      - round: 23\n        reviewers: [2]\n        note: \"R2 维持：论文本质是 causal inference methodology，NLP 作为 application domain。更适合 JCI/UAI/AISTATS。R1 未直接讨论但同意 novelty 对 EMNLP 偏弱。\"\n    action_items:\n      - round: 21\n        action: \"experiments.tex §5.2 增加 CivilComments NLP insight\"\n        assigned_to: director\n        status: done\n      - round: 23\n        action: \"Rebuttal 准备 venue-fit 论据\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R21-W1\"\n    summary: \"Proposition 5 诊断 vs 直接运行 EC-HTE 的增量价值不明\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 21\n    last_seen_round: 22\n    action_items:\n      - round: 21\n        action: \"明确诊断准则的使用场景（rebuttal）\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R22-W1\"\n    summary: \"κ-guard 阈值 100 缺乏与 O_p(κ²·n^{-1/2}) 的理论连接\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 22\n    last_seen_round: 24\n    mentions:\n      - round: 23\n        reviewers: [2]\n        note: \"R2 Q3 问 Δπ>0.15 阈值是否有理论推导。R1 认为有理论依据但 REBUT 程度不一。\"\n      - round: 24\n        reviewers: [1, 2]\n        note: \"R24 Q2 追问 κ-guard fallback 到 global correction 是否引入新的异质性偏差。hybrid estimator 理论性质未分析。\"\n    action_items:\n      - round: 22\n        action: \"基于 O_p(κ²·n^{-1/2}) 推导理论最优 κ 阈值（rebuttal）\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R22-W2\"\n    summary: \"EB 两阶段低估后验不确定性\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 22\n    last_seen_round: 24\n    mentions:\n      - round: 23\n        reviewers: [1, 2]\n        note: \"R1 W10 提出 SE 不 propagate CM uncertainty。R2 rebuts 认为 bootstrap 已解决。分歧。\"\n      - round: 24\n        reviewers: [1, 2]\n        note: \"R24 升级为 Must-Fix N2。共识：plug-in SE 将 Ĉ_s 当固定量是技术缺陷。bootstrap 应为默认。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R22-W8\"\n    summary: \"Abstract 信息密度过高（12+ 具体数字）\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 22\n    last_seen_round: 23\n    mentions:\n      - round: 23\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 再次共识。Camera-ready 处理。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R22-W9\"\n    summary: \"Debiasing 术语歧义（fairness vs measurement-error）\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 22\n    last_seen_round: 23\n    mentions:\n      - round: 23\n        reviewers: [2]\n        note: \"R2 再次提出。标题中 'debiasing' 在 NLP 社区有 fairness 歧义。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R22-W10\"\n    summary: \"Per-model R² 低端讨论不足（R²=0.76 削弱 exact framing）\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 22\n    last_seen_round: 24\n    mentions:\n      - round: 23\n        reviewers: [1, 2]\n        note: \"R1 指出 R²=0.76 削弱 'exact' 说服力（24% 未解释方差）。R2 同意。升级至 warning。论文未对低 R² case 做 failure analysis。\"\n      - round: 24\n        reviewers: [1, 2]\n        note: \"R24 N1 直接引用 R²=0.976 at P(Z=1)=0.1 作为 simplified form 不精确的证据。与 per-model R²=0.76 共同削弱 'exact identity' 叙事。\"\n    action_items:\n      - round: 23\n        action: \"Rebuttal 准备：per-model R² 回归分析 (R² ~ FPR, FNR, |FPR-FNR|, κ, P(Z=1), n)\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R22-REF1\"\n    summary: \"缺 Filtered PPI 引用 (arXiv:2602.10464)\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 22\n    last_seen_round: 23\n    mentions:\n      - round: 23\n        reviewers: [1, 2]\n        note: \"R2 再次指出。R1 表示无法独立验证但认为 plausible。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R23-W1\"\n    summary: \"诊断 AUC=0.86 (symmetric case) 缺乏 decision-consequence 分析\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 23\n    last_seen_round: 23\n    mentions:\n      - round: 23\n        reviewers: [1, 2]\n        note: \"AUC=0.86 在 symmetric case 下有非平凡误判率。论文未讨论 FP/FN 不对称代价（false negative 后果远重于 false positive）。建议 precision/recall breakdown 和 decision threshold tradeoff。\"\n    action_items:\n      - round: 23\n        action: \"Rebuttal 准备：从现有数据提取 precision/recall curve + 推荐保守 threshold\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R23-W2\"\n    summary: \"'Debiasing hurts' framing 在 moderate heterogeneity 下不成立\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 23\n    last_seen_round: 24\n    mentions:\n      - round: 23\n        reviewers: [1, 2]\n        note: \"标题暗示 debiasing 普遍有害，但论文表明仅在 extreme heterogeneity 下成立。\"\n      - round: 24\n        reviewers: [1, 2]\n        note: \"R24 W3 再次指出 Abstract '7.4× bias reduction' 仅在 extreme heterogeneity + K=2 下成立。要求 Abstract/Intro 更明确限定适用条件。\"\n    action_items:\n      - round: 23\n        action: \"Intro L12 增加 'when error rates vary across subgroups' 限定\"\n        assigned_to: director\n        status: done\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R23-Q1\"\n    summary: \"Propensity score estimation error 与 CM estimation error 的交互效应未讨论\"\n    category: method\n    severity: info\n    status: open\n    first_raised_round: 23\n    last_seen_round: 23\n    mentions:\n      - round: 23\n        reviewers: [1, 2]\n        note: \"观察性研究中 treatment assignment 和 outcome measurement 同时含噪。Identity 在 joint estimation error 下是否成立？\"\n    action_items:\n      - round: 23\n        action: \"Rebuttal 论点：Identity 作用于 correction layer 独立于下游估计器\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R23-L1\"\n    summary: \"Figure 4 漂出正文到 References 页\"\n    category: format\n    severity: warning\n    status: open\n    first_raised_round: 23\n    last_seen_round: 23\n    mentions:\n      - round: 23\n        reviewers: []\n        note: \"视觉审查检测。正文 Section 5.3 引用但 float 越界到 p.9。\"\n    action_items:\n      - round: 23\n        action: \"调整 float placement 或缩小 Figure 3/Table 1\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R23-L2\"\n    summary: \"p.8 极度拥挤（Figure 3 + Table 1 + §5.4 + Conclusion + Limitations）\"\n    category: format\n    severity: info\n    status: open\n    first_raised_round: 23\n    last_seen_round: 23\n    mentions:\n      - round: 23\n        reviewers: []\n        note: \"视觉审查检测。Conclusion 仅 ~12 行。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  # === R24 NEW ISSUES ===\n\n  - id: \"R24-N1\"\n    summary: \"A3 松弛下 'identity remains exact' 声称不准确——simplified product form 是近似非精确\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 24\n    last_seen_round: 24\n    mentions:\n      - round: 24\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 共识。Theorem 1 simplified form δ_s·Δτ/(1−2π̄) 依赖 A3 (balanced classes)。R²=0.976 at P(Z=1)=0.1 证明 simplified form 非 exact。需区分 general matrix form (always exact) vs simplified scalar form (exact only under A2+A3)。Section 3 p3-4 和 Appendix S p22 的措辞应如实表述。\"\n    action_items:\n      - round: 24\n        action: \"Section 3 修正：区分 general matrix form (exact for any class balance) 和 simplified scalar product form (exact under A3)。将 'identity remains exact' 改为 'matrix form remains exact; scalar approximation achieves R²≥0.976'\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R24-N2\"\n    summary: \"Algorithm 1 plug-in SE 忽略 CM 估计不确定性——bootstrap 应为默认\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 24\n    last_seen_round: 24\n    mentions:\n      - round: 24\n        reviewers: [1, 2]\n        note: \"共识。Algorithm 1 L11 SE=sqrt(diag(Ĉ_s^{-1}·V̂)) 将 Ĉ_s 当固定已知量。93.8% coverage 信息藏在 footnote。Appendix X 证明 bootstrap 恢复 ≥95% coverage。R2 强化：n_expert<250 时严重低估 CI。两位要求 bootstrap 成为默认推荐，Algorithm 1 须注明风险。\"\n    action_items:\n      - round: 24\n        action: \"Algorithm 1 注明 plug-in SE 的 under-coverage 风险，推荐 n_expert<250 时用 bootstrap\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R24-W1\"\n    summary: \"Ĉ_s^{-1} 在 asymmetric case 应为 M̂_s^{-1}——notation 不一致易致实现错误\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 24\n    last_seen_round: 24\n    mentions:\n      - round: 24\n        reviewers: [1, 2]\n        note: \"共识。A2 下 C_s=M_s 无碍，但 Remark 2 声称推广到 asymmetric，Appendix C 给出 general M_s。Algorithm 1 应说明 asymmetric case 需 invert M̂_s 而非 Ĉ_s。\"\n    action_items:\n      - round: 24\n        action: \"Algorithm 1 或 Remark 2 注明：asymmetric case 用 M̂_s^{-1} 替代 Ĉ_s^{-1}\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R24-W2\"\n    summary: \"κ 指代不一致——Algorithm 1 κ(Ĉ_s^{-1}) vs Section 4 O_p(κ²·n^{-1/2}) 中的 κ\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 24\n    last_seen_round: 24\n    mentions:\n      - round: 24\n        reviewers: [1, 2]\n        note: \"共识。κ 在不同上下文指代不同矩阵的 condition number。需用下标区分（κ_s vs κ_global）或统一说明。\"\n    action_items:\n      - round: 24\n        action: \"统一 κ 符号，用下标区分 κ_s (per-subgroup) 和 κ_global\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R24-W3\"\n    summary: \"Operating conditions (K≤4, n_expert≥250) 在 Abstract/Intro 限定不足\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 24\n    last_seen_round: 24\n    mentions:\n      - round: 24\n        reviewers: [1, 2]\n        note: \"K=8 时 EC-HTE RMSE 劣于 global (Appendix I.2 Figure 8)。n_expert≥250 per subgroup → K=4 需 ≥1000 expert labels。Abstract '7.4×' 仅 extreme heterogeneity + K=2。Section 5.4/Limitations 诚实但 Abstract/Intro framing 暗示通用性。R2 认为需更明确限定。\"\n    action_items:\n      - round: 24\n        action: \"Abstract/Intro 加入 K≤4 / n_expert≥250 适用条件的明确限定\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R24-W4\"\n    summary: \"Corollary 4 贡献度：数学贡献有限但叙事价值有争议\"\n    category: framing\n    severity: info\n    status: open\n    first_raised_round: 24\n    last_seen_round: 24\n    mentions:\n      - round: 24\n        reviewers: [1, 2]\n        note: \"R1 认为 Corollary 4 是 Theorem 1 的 trivial 推论，不应单列贡献。R2 部分 REBUT：Corollary 4 回答了 'why practitioners missed the problem'，叙事不可替代。共识：不应单独作为 contribution 列出，应作为 Theorem 1 段内推论。\"\n    action_items:\n      - round: 24\n        action: \"Corollary 4 从独立贡献降级为 Theorem 1 段内自然推论\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R24-W5\"\n    summary: \"Remark 2 选择性报告——报 diagnostic AUC=0.96 但隐瞒 EC-HTE 在 asymmetric case RMSE 全劣\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 24\n    last_seen_round: 24\n    mentions:\n      - round: 24\n        reviewers: [1, 2]\n        note: \"R2 升级为 Should-Fix（R1 原为 Minor M4）。Table 10 (p17) 显示 EC-HTE 在所有 48 个 asymmetric 配置下 RMSE 均劣于 Global。Remark 2 只报告诊断 AUC=0.96 而隐瞒校正方法本身在此场景下失效。这是选择性报告问题——diagnostic 能发现问题但 correction 无法解决。论文应在 Remark 2 明确说明。\"\n    action_items:\n      - round: 24\n        action: \"Remark 2 补充：asymmetric case 下 EC-HTE per-subgroup inversion 因估计两倍参数增加 variance，RMSE 劣于 global correction。影响方法推荐范围。\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R24-Q1\"\n    summary: \"A5 (balanced effect modifier) 是否从一开始就不必要？\"\n    category: method\n    severity: info\n    status: open\n    first_raised_round: 24\n    last_seen_round: 24\n    mentions:\n      - round: 24\n        reviewers: [1, 2]\n        note: \"A5 要求 P(Z=1|S=s)=0.5。若 Theorem 1 无需 A5 即可成立（至少近似），则列出 A5 为必要假设是误导。Appendix B 证明中 A5 的确切角色需明确。\"\n    action_items:\n      - round: 24\n        action: \"Rebuttal 明确 A5 在 Theorem 1 证明中的确切角色\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R24-Q2\"\n    summary: \"κ-guard fallback 到 global correction 的 hybrid estimator 理论性质未分析\"\n    category: method\n    severity: info\n    status: open\n    first_raised_round: 24\n    last_seen_round: 24\n    mentions:\n      - round: 24\n        reviewers: [1, 2]\n        note: \"部分子群 per-subgroup + 部分子群 global = hybrid estimator。高 κ 子群恰好是高误差子群，fallback 到 global 引入 Theorem 1 描述的偏差。两种策略不一致可能致 CausalForest splitting 异常。Appendix A.1 称 κ>100 'not load-bearing' 但未分析 hybrid 性质。\"\n    action_items:\n      - round: 24\n        action: \"Rebuttal/Discussion 补充 hybrid estimator bias properties 分析\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R24-Q3\"\n    summary: \"Subgroup membership S 的 misspecification 影响未讨论\"\n    category: method\n    severity: info\n    status: open\n    first_raised_round: 24\n    last_seen_round: 24\n    mentions:\n      - round: 24\n        reviewers: [1, 2]\n        note: \"论文假设 S 正确观测。实际中：(1) 子群定义可能不捕捉真正的 error rate heterogeneity；(2) S 本身可能有 measurement error；(3) Appendix Y.5 讨论 A5 violation 但不含 S misspecification。应至少在 Limitations 提及。\"\n    action_items:\n      - round: 24\n        action: \"Limitations 补充 subgroup membership misspecification 讨论\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R24-M1\"\n    summary: \"Figure 3 分区线应标注 Proposition 5 threshold 公式\"\n    category: format\n    severity: info\n    status: open\n    first_raised_round: 24\n    last_seen_round: 24\n    mentions:\n      - round: 24\n        reviewers: [1, 2]\n        note: \"Figure 3 'debiasing helps'/'debiasing hurts' 分区线应标注对应 π_s < ε_s/(2(1−ε_s))。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R24-M2\"\n    summary: \"F-L 缩写首次出现在 Table 2 而非正文\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 24\n    last_seen_round: 24\n    mentions:\n      - round: 24\n        reviewers: [1, 2]\n        note: \"Table 2 中 'F-L' 应在正文首次引用 Frazis-Loewenstein 时定义。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null"
  }
}
```

</details>

---


### Tool result

_source line 2615 · 2026-05-25T21:37:03.866587+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/review_issues.yaml\", \"bytes\": 34778}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 153
}
```

</details>

---


### Tool call

_source line 2616 · 2026-05-25T21:38:44.851090+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# Consolidated Review Report — Round 24\n\n**Venue**: EMNLP 2026 (via ARR)  \n**Paper**: EC-HTE: Error-Corrected Heterogeneous Treatment Effect Estimation with LLM Annotations  \n**Reviewers**: R1 (方法严谨性 + 实验设计), R2 (新颖性 + 完整性 + 实践适用性)  \n**Rounds**: 1 (converged after cross-sharing; no Round 2 needed)  \n**Cross-sharing status**: Both reviewers completed [AGREE]/[REBUT] responses. High convergence — only minor nuance on W4.\n\n---\n\n## Summary\n\n本文证明了一个精确恒等式（Theorem 1），揭示全局误分类校正（global debiasing）在子群误差率异质的条件下如何在子群层面引入偏差——甚至可能反转因果效应的方向。论文提出 EC-HTE 方法（per-subgroup confusion matrix inversion + hierarchical Bayes estimation）和诊断准则（Proposition 5）来检测和修正这一问题。实验覆盖 2304 个合成配置和 8 个真实 LLM confusion matrices。\n\n论文理论洞察有价值（首次报告 14.9% 配置出现 sign reversal），实验设计全面（消融、sensitivity analysis、operating conditions 诚实报告），但存在若干需修正的技术表述问题、选择性报告倾向、以及方法论技术新颖性有限的固有约束。\n\n---\n\n## Strengths\n\n**S1. 具有实际影响的问题发现** — 首次严格证明 global debiasing 在子群层面可引入 sign reversal（14.9% configs），且通过 CivilComments 应用展示 3.2× effect-size gap 改变实质研究结论。这对使用 LLM annotation 做因果推断的研究者是重要警示。\n\n**S2. 理论结果清晰且可操作** — Theorem 1 的 product form δ_s·Δτ/(1−2π̄) 提供了直观的偏差分解：方向由 δ_s（子群误差率偏离全局）决定，幅度由 Δτ（效应异质性）放大。Proposition 5 的诊断准则可在无需运行完整 EC-HTE 的前提下判断 debiasing 是否有害。\n\n**S3. 全面且诚实的实验设计** — 2304 configuration grid 的系统性消融、8 个真实 LLM CMs 的 semi-real validation、明确报告操作条件（K≤4, n_expert≥250）、sensitivity analysis 展示方法边界（γ_T=0.10 → coverage 75%）。论文在 Section 5.4 和 Limitations 中没有回避方法局限。\n\n**S4. HB estimation 的 practical value** — Hierarchical Bayes 的 partial pooling 在小样本（n_expert=50-100）下显著优于 MLE，这是一个对 practitioners 有实用价值的工程贡献。\n\n---\n\n## Weaknesses\n\n### Must-Fix (阻碍接收)\n\n**N1. A3 松弛下 \"identity remains exact\" 声称不准确** [R1 提出, R2 同意]\n\nSection 3 (p3-4) 称 \"Under class imbalance (relaxing A3), the identity remains exact (R²≥0.976 at P(Z=1)=0.1)\"。但这混淆了两个层次：\n- **General matrix form** M_global^{-1}·M_s（始终精确，无需 A3）\n- **Simplified scalar product form** δ_s·Δτ/(1−2π̄)（仅在 A2+A3 下精确）\n\nR²=0.976 ≠ 1.0 恰恰证明 simplified form 在 class imbalance 下是 approximation 而非 identity。Table 21 (Appendix S, p22) 进一步显示 R² 随 P(Z=1) 偏离 0.5 而下降，EC-HTE RMSE 优势从 ratio 1.54 收窄。\n\n**修正要求**：区分 general matrix form（always exact）和 simplified scalar product form（A3-dependent approximation）。将 \"identity remains exact\" 改为 \"matrix form remains exact; scalar approximation achieves R²≥0.976\"。\n\n**N2. Plug-in SE 忽略 CM 估计不确定性** [R1 提出, R2 强化]\n\nAlgorithm 1 line 11 的 SE = sqrt(diag(Ĉ_s^{-1}·V̂)) 将 Ĉ_s 当作固定已知量，完全忽略 Ĉ_s 的后验不确定性。这导致：\n- n_expert 较小时（50-100）CI 宽度严重低估\n- 论文自身在 footnote (p7) 报告仅 93.8% coverage（低于 nominal 95%），bootstrap 恢复 ≥95%\n- 关键信息不应藏在 footnote——这是方法的 systematic deficiency\n\n**修正要求**：(1) Algorithm 1 主体流程应注明 plug-in SE 的 under-coverage 风险；(2) n_expert < 250 时 bootstrap 应为默认推荐方案。\n\n---\n\n### Should-Fix (需修正但非阻断)\n\n**W1. Ĉ_s^{-1} 在 asymmetric case 应为 M̂_s^{-1}** [R1 提出, R2 同意]\n\nRemark 2 声称结果推广到 asymmetric CMs，Appendix C 给出 general M_s 形式。但 Algorithm 1 始终使用 Ĉ_s^{-1}。在 A2 下 C_s=M_s 故无碍，但任何读者想在 asymmetric case 实现时会困惑。这是 notation 不一致，易致实现错误。\n\n**W2. κ 符号指代不一致** [R1 提出, R2 同意]\n\nAlgorithm 1 中 κ(Ĉ_s^{-1}) 用于 guard threshold，但 Section 4 的 O_p(κ²·n^{-1/2}) 中 κ 指向不同矩阵。需统一 notation（κ_s vs κ_global）。\n\n**W3. Operating conditions 在 Abstract/Intro 限定不足** [R1 提出, R2 同意并补充]\n\nAbstract 的 \"7.4× bias reduction\" 仅在 extreme heterogeneity + K=2 设置下成立。K=8 时 EC-HTE RMSE 劣于 global correction (Appendix I.2, Figure 8)。n_expert≥250 per subgroup 意味着 K=4 需 ≥1000 expert labels。尽管 Section 5.4/Limitations 诚实报告了这些限制，但 Abstract/Intro 的 framing 暗示更广泛适用性。\n\n**W4. Corollary 4 贡献呈现** [R1 提出, R2 部分 REBUT]\n\nR1 认为 Corollary 4 是 Theorem 1 的 trivial 推论。R2 反驳其叙事价值不可替代（解释为何问题长期未被发现）。**共识**：Corollary 4 不应单独列为 contribution，应作为 Theorem 1 段内自然推论讨论。\n\n**W5. Remark 2 选择性报告——Table 10 cherry-picking** [R1 Minor 提出, R2 升级为 Should-Fix]\n\nRemark 2 报告 diagnostic AUC=0.96 in asymmetric case，但**完全隐瞒** Table 10 (p17) 显示 EC-HTE 在所有 48 个 asymmetric 配置下 RMSE 均劣于 Global correction。这意味着 diagnostic 能发现问题但 correction 无法解决——这是 critical gap，属于选择性报告。EC-HTE per-subgroup inversion 在 asymmetric case 下需估计两倍参数（FPR/FNR separately），增加 variance。论文应在 Remark 2 明确说明。\n\n---\n\n### Minor Issues\n\n**M1.** Abstract 约 185 words，符合 ≤200 要求。[确认合规]\n\n**M2.** Figure 3 (p4) 的 \"debiasing helps\"/\"debiasing hurts\" 分区线应标注对应的 Proposition 5 threshold 公式 π_s < ε_s/(2(1−ε_s))。\n\n**M3.** \"F-L\" 缩写首次出现在 Table 2 而非正文。应在正文首次引用 Frazis-Loewenstein 时定义。\n\n---\n\n## Questions for Authors\n\n**Q1. A5 (balanced effect modifier) 是否从一开始就不必要？** A5 要求 P(Z=1|S=s)=0.5 for all s。如果 Theorem 1 无需 A5 即可成立（至少近似），则列出 A5 为必要假设是误导。请明确 A5 在 Theorem 1 证明（Appendix B）中的确切角色——哪一步推导需要它？\n\n**Q2. κ-guard fallback 到 global correction 是否引入新偏差？** 当部分子群用 per-subgroup correction、其他子群 fallback 到 global correction 时，resulting hybrid estimator 可能比纯粹使用任一策略更差。高 κ 子群恰好是高误差子群，fallback 到 global 引入 Theorem 1 描述的偏差。两种策略不一致是否导致 CausalForest splitting 异常？Appendix A.1 称 κ>100 \"not load-bearing\" 但未分析 hybrid estimator 的理论性质。\n\n**Q3. Subgroup membership S 的 misspecification 影响？** 论文假设 S 正确观测。但实际中：(1) 子群定义可能不捕捉真正的 error rate heterogeneity（e.g., 按 platform 分组但真正异质性在 text length）；(2) S 本身可能有 measurement error。应至少在 Limitations 讨论。\n\n---\n\n## Missing References\n\n- **Filtered PPI** (arXiv:2602.10464) — R22 首次提出，R23 再次指出。与 EC-HTE 的 selective expert labeling 策略高度相关。\n- 已确认无其他新的遗漏。\n\n---\n\n## External Review\n\n**状态**: 未请求（项目配置未启用外部审稿）。\n\n---\n\n## Visual Layout Check (非评分项)\n\n**状态**: ✅ 完成 (2026-05-25T21:16–21:20 UTC)  \n**统计**: 0 critical, 0 warning, 6 info\n\n| Page | Finding |\n|------|---------|\n| p1 | 首页纯文本，Figure 1 在 p2 顶部位置优秀，锚定效应及时 |\n| p2 | Figure 1 红/绿配色对红绿色盲有辨识风险，建议改用 orange/blue 或添加纹理 |\n| p4 | Figure 3 内部注释 \"debiasing helps\"/\"hurts\" 字号偏小（约正文 60%），建议 ≥70% |\n| p7 | Figure 5 注释/虚线标签略密集 |\n| p17 | Table 9 行列数多、字号小，附录可接受 |\n| p31 | 末页约 1/3 空白（AI Assistants 声明），可接受 |\n\n**红绿配色问题**与 R16-W7 (in_progress) 一致，持续跟踪。\n\n---\n\n## Overall Assessment\n\n**Score: 3.5 — Borderline Conference** (R1: 3.5, R2: 3.5, 共识)\n\n### 评分理由\n\n**支撑 Conference 的因素**：\n- 首次严格证明 global debiasing 的子群偏差 + sign reversal 14.9%——问题发现有实际价值\n- CivilComments 应用中 3.2× effect-size gap 改变实质研究结论——impact 明确\n- 实验设计全面诚实，包含 operating conditions 和 sensitivity analysis\n- 方法可操作（Algorithm 1 + diagnostic 准则 + open-source code）\n\n**限制 Conference 的因素**：\n- 方法论技术新颖性有限——核心是 Frazis-Loewenstein (2003) confusion matrix inversion 从 global 到 per-subgroup 的扩展，属 \"careful application of known techniques to important new context\"\n- N1 (exact identity claim) 和 N2 (plug-in SE) 需文本修正才能达到技术表述严谨标准\n- W5 (selective reporting in Remark 2) 暴露 framing 倾向，降低审稿人信任\n- 所有实验为 semi-synthetic，无 fully real-data validation（尽管有 Catch-22 论证辩护）\n- NLP venue fit 存疑——论文本质是 causal inference methodology，NLP 为 application domain\n\n**总结**：论文的问题发现和实践影响足够支撑 EMNLP 接收，但技术深度与 framing 严谨性需要提升。如果 N1/N2 修正到位且 W5 选择性报告问题解决，score 可升至 4.0。当前状态介于 Findings 和 Conference 之间。\n\n---\n\n## Detailed Comments (按优先级排序的 Action Items)\n\n### 必须修正（阻碍接收）\n\n1. **Section 3 p3-4**: 区分 general matrix form (exact) 和 simplified scalar form (A3-dependent approximation)。\"identity remains exact\" → \"matrix form remains exact; scalar approximation R²≥0.976\"\n2. **Algorithm 1**: 注明 plug-in SE under-coverage 风险 + 推荐 n_expert<250 时用 bootstrap\n\n### 应该修正（显著改善质量）\n\n3. **Algorithm 1 / Remark 2**: asymmetric case 须说明用 M̂_s^{-1} 替代 Ĉ_s^{-1}\n4. **全文**: 统一 κ 符号（κ_s vs κ_global 下标）\n5. **Abstract/Intro**: 明确限定 \"7.4×\" 的适用条件（extreme heterogeneity, K=2）\n6. **Remark 2**: 补充 EC-HTE 在 asymmetric case RMSE 劣于 global 的事实及原因\n7. **Contribution list**: Corollary 4 降级为 Theorem 1 段内推论\n\n### 建议修正（锦上添花）\n\n8. **Figure 3**: 分区线标注 Proposition 5 threshold 公式\n9. **正文**: F-L 缩写定义前移\n10. **Limitations**: 补充 S misspecification 讨论\n\n### Rebuttal 重点准备\n\n- A5 在证明中的确切角色（Q1）\n- κ-guard hybrid estimator 理论性质（Q2）\n- 方法论新颖性的 impact-based 辩护（sign reversal 首次报告 + CivilComments 实质结论变化）\n- Venue fit 论据（EMNLP 近年接收 causal inference for NLP 论文 + LLM annotation 核心趋势）",
  "project": "ec_hte_llm_annotation",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.5 - Borderline Conference",
  "review_chat_id": "oc_489afd65980834a91024fd48e21d984f"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# Consolidated Review Report — Round 24\n\n**Venue**: EMNLP 2026 (via ARR)  \n**Paper**: EC-HTE: Error-Corrected Heterogeneous Treatment Effect Estimation with LLM Annotations  \n**Reviewers**: R1 (方法严谨性 + 实验设计), R2 (新颖性 + 完整性 + 实践适用性)  \n**Rounds**: 1 (converged after cross-sharing; no Round 2 needed)  \n**Cross-sharing status**: Both reviewers completed [AGREE]/[REBUT] responses. High convergence — only minor nuance on W4.\n\n---\n\n## Summary\n\n本文证明了一个精确恒等式（Theorem 1），揭示全局误分类校正（global debiasing）在子群误差率异质的条件下如何在子群层面引入偏差——甚至可能反转因果效应的方向。论文提出 EC-HTE 方法（per-subgroup confusion matrix inversion + hierarchical Bayes estimation）和诊断准则（Proposition 5）来检测和修正这一问题。实验覆盖 2304 个合成配置和 8 个真实 LLM confusion matrices。\n\n论文理论洞察有价值（首次报告 14.9% 配置出现 sign reversal），实验设计全面（消融、sensitivity analysis、operating conditions 诚实报告），但存在若干需修正的技术表述问题、选择性报告倾向、以及方法论技术新颖性有限的固有约束。\n\n---\n\n## Strengths\n\n**S1. 具有实际影响的问题发现** — 首次严格证明 global debiasing 在子群层面可引入 sign reversal（14.9% configs），且通过 CivilComments 应用展示 3.2× effect-size gap 改变实质研究结论。这对使用 LLM annotation 做因果推断的研究者是重要警示。\n\n**S2. 理论结果清晰且可操作** — Theorem 1 的 product form δ_s·Δτ/(1−2π̄) 提供了直观的偏差分解：方向由 δ_s（子群误差率偏离全局）决定，幅度由 Δτ（效应异质性）放大。Proposition 5 的诊断准则可在无需运行完整 EC-HTE 的前提下判断 debiasing 是否有害。\n\n**S3. 全面且诚实的实验设计** — 2304 configuration grid 的系统性消融、8 个真实 LLM CMs 的 semi-real validation、明确报告操作条件（K≤4, n_expert≥250）、sensitivity analysis 展示方法边界（γ_T=0.10 → coverage 75%）。论文在 Section 5.4 和 Limitations 中没有回避方法局限。\n\n**S4. HB estimation 的 practical value** — Hierarchical Bayes 的 partial pooling 在小样本（n_expert=50-100）下显著优于 MLE，这是一个对 practitioners 有实用价值的工程贡献。\n\n---\n\n## Weaknesses\n\n### Must-Fix (阻碍接收)\n\n**N1. A3 松弛下 \"identity remains exact\" 声称不准确** [R1 提出, R2 同意]\n\nSection 3 (p3-4) 称 \"Under class imbalance (relaxing A3), the identity remains exact (R²≥0.976 at P(Z=1)=0.1)\"。但这混淆了两个层次：\n- **General matrix form** M_global^{-1}·M_s（始终精确，无需 A3）\n- **Simplified scalar product form** δ_s·Δτ/(1−2π̄)（仅在 A2+A3 下精确）\n\nR²=0.976 ≠ 1.0 恰恰证明 simplified form 在 class imbalance 下是 approximation 而非 identity。Table 21 (Appendix S, p22) 进一步显示 R² 随 P(Z=1) 偏离 0.5 而下降，EC-HTE RMSE 优势从 ratio 1.54 收窄。\n\n**修正要求**：区分 general matrix form（always exact）和 simplified scalar product form（A3-dependent approximation）。将 \"identity remains exact\" 改为 \"matrix form remains exact; scalar approximation achieves R²≥0.976\"。\n\n**N2. Plug-in SE 忽略 CM 估计不确定性** [R1 提出, R2 强化]\n\nAlgorithm 1 line 11 的 SE = sqrt(diag(Ĉ_s^{-1}·V̂)) 将 Ĉ_s 当作固定已知量，完全忽略 Ĉ_s 的后验不确定性。这导致：\n- n_expert 较小时（50-100）CI 宽度严重低估\n- 论文自身在 footnote (p7) 报告仅 93.8% coverage（低于 nominal 95%），bootstrap 恢复 ≥95%\n- 关键信息不应藏在 footnote——这是方法的 systematic deficiency\n\n**修正要求**：(1) Algorithm 1 主体流程应注明 plug-in SE 的 under-coverage 风险；(2) n_expert < 250 时 bootstrap 应为默认推荐方案。\n\n---\n\n### Should-Fix (需修正但非阻断)\n\n**W1. Ĉ_s^{-1} 在 asymmetric case 应为 M̂_s^{-1}** [R1 提出, R2 同意]\n\nRemark 2 声称结果推广到 asymmetric CMs，Appendix C 给出 general M_s 形式。但 Algorithm 1 始终使用 Ĉ_s^{-1}。在 A2 下 C_s=M_s 故无碍，但任何读者想在 asymmetric case 实现时会困惑。这是 notation 不一致，易致实现错误。\n\n**W2. κ 符号指代不一致** [R1 提出, R2 同意]\n\nAlgorithm 1 中 κ(Ĉ_s^{-1}) 用于 guard threshold，但 Section 4 的 O_p(κ²·n^{-1/2}) 中 κ 指向不同矩阵。需统一 notation（κ_s vs κ_global）。\n\n**W3. Operating conditions 在 Abstract/Intro 限定不足** [R1 提出, R2 同意并补充]\n\nAbstract 的 \"7.4× bias reduction\" 仅在 extreme heterogeneity + K=2 设置下成立。K=8 时 EC-HTE RMSE 劣于 global correction (Appendix I.2, Figure 8)。n_expert≥250 per subgroup 意味着 K=4 需 ≥1000 expert labels。尽管 Section 5.4/Limitations 诚实报告了这些限制，但 Abstract/Intro 的 framing 暗示更广泛适用性。\n\n**W4. Corollary 4 贡献呈现** [R1 提出, R2 部分 REBUT]\n\nR1 认为 Corollary 4 是 Theorem 1 的 trivial 推论。R2 反驳其叙事价值不可替代（解释为何问题长期未被发现）。**共识**：Corollary 4 不应单独列为 contribution，应作为 Theorem 1 段内自然推论讨论。\n\n**W5. Remark 2 选择性报告——Table 10 cherry-picking** [R1 Minor 提出, R2 升级为 Should-Fix]\n\nRemark 2 报告 diagnostic AUC=0.96 in asymmetric case，但**完全隐瞒** Table 10 (p17) 显示 EC-HTE 在所有 48 个 asymmetric 配置下 RMSE 均劣于 Global correction。这意味着 diagnostic 能发现问题但 correction 无法解决——这是 critical gap，属于选择性报告。EC-HTE per-subgroup inversion 在 asymmetric case 下需估计两倍参数（FPR/FNR separately），增加 variance。论文应在 Remark 2 明确说明。\n\n---\n\n### Minor Issues\n\n**M1.** Abstract 约 185 words，符合 ≤200 要求。[确认合规]\n\n**M2.** Figure 3 (p4) 的 \"debiasing helps\"/\"debiasing hurts\" 分区线应标注对应的 Proposition 5 threshold 公式 π_s < ε_s/(2(1−ε_s))。\n\n**M3.** \"F-L\" 缩写首次出现在 Table 2 而非正文。应在正文首次引用 Frazis-Loewenstein 时定义。\n\n---\n\n## Questions for Authors\n\n**Q1. A5 (balanced effect modifier) 是否从一开始就不必要？** A5 要求 P(Z=1|S=s)=0.5 for all s。如果 Theorem 1 无需 A5 即可成立（至少近似），则列出 A5 为必要假设是误导。请明确 A5 在 Theorem 1 证明（Appendix B）中的确切角色——哪一步推导需要它？\n\n**Q2. κ-guard fallback 到 global correction 是否引入新偏差？** 当部分子群用 per-subgroup correction、其他子群 fallback 到 global correction 时，resulting hybrid estimator 可能比纯粹使用任一策略更差。高 κ 子群恰好是高误差子群，fallback 到 global 引入 Theorem 1 描述的偏差。两种策略不一致是否导致 CausalForest splitting 异常？Appendix A.1 称 κ>100 \"not load-bearing\" 但未分析 hybrid estimator 的理论性质。\n\n**Q3. Subgroup membership S 的 misspecification 影响？** 论文假设 S 正确观测。但实际中：(1) 子群定义可能不捕捉真正的 error rate heterogeneity（e.g., 按 platform 分组但真正异质性在 text length）；(2) S 本身可能有 measurement error。应至少在 Limitations 讨论。\n\n---\n\n## Missing References\n\n- **Filtered PPI** (arXiv:2602.10464) — R22 首次提出，R23 再次指出。与 EC-HTE 的 selective expert labeling 策略高度相关。\n- 已确认无其他新的遗漏。\n\n---\n\n## External Review\n\n**状态**: 未请求（项目配置未启用外部审稿）。\n\n---\n\n## Visual Layout Check (非评分项)\n\n**状态**: ✅ 完成 (2026-05-25T21:16–21:20 UTC)  \n**统计**: 0 critical, 0 warning, 6 info\n\n| Page | Finding |\n|------|---------|\n| p1 | 首页纯文本，Figure 1 在 p2 顶部位置优秀，锚定效应及时 |\n| p2 | Figure 1 红/绿配色对红绿色盲有辨识风险，建议改用 orange/blue 或添加纹理 |\n| p4 | Figure 3 内部注释 \"debiasing helps\"/\"hurts\" 字号偏小（约正文 60%），建议 ≥70% |\n| p7 | Figure 5 注释/虚线标签略密集 |\n| p17 | Table 9 行列数多、字号小，附录可接受 |\n| p31 | 末页约 1/3 空白（AI Assistants 声明），可接受 |\n\n**红绿配色问题**与 R16-W7 (in_progress) 一致，持续跟踪。\n\n---\n\n## Overall Assessment\n\n**Score: 3.5 — Borderline Conference** (R1: 3.5, R2: 3.5, 共识)\n\n### 评分理由\n\n**支撑 Conference 的因素**：\n- 首次严格证明 global debiasing 的子群偏差 + sign reversal 14.9%——问题发现有实际价值\n- CivilComments 应用中 3.2× effect-size gap 改变实质研究结论——impact 明确\n- 实验设计全面诚实，包含 operating conditions 和 sensitivity analysis\n- 方法可操作（Algorithm 1 + diagnostic 准则 + open-source code）\n\n**限制 Conference 的因素**：\n- 方法论技术新颖性有限——核心是 Frazis-Loewenstein (2003) confusion matrix inversion 从 global 到 per-subgroup 的扩展，属 \"careful application of known techniques to important new context\"\n- N1 (exact identity claim) 和 N2 (plug-in SE) 需文本修正才能达到技术表述严谨标准\n- W5 (selective reporting in Remark 2) 暴露 framing 倾向，降低审稿人信任\n- 所有实验为 semi-synthetic，无 fully real-data validation（尽管有 Catch-22 论证辩护）\n- NLP venue fit 存疑——论文本质是 causal inference methodology，NLP 为 application domain\n\n**总结**：论文的问题发现和实践影响足够支撑 EMNLP 接收，但技术深度与 framing 严谨性需要提升。如果 N1/N2 修正到位且 W5 选择性报告问题解决，score 可升至 4.0。当前状态介于 Findings 和 Conference 之间。\n\n---\n\n## Detailed Comments (按优先级排序的 Action Items)\n\n### 必须修正（阻碍接收）\n\n1. **Section 3 p3-4**: 区分 general matrix form (exact) 和 simplified scalar form (A3-dependent approximation)。\"identity remains exact\" → \"matrix form remains exact; scalar approximation R²≥0.976\"\n2. **Algorithm 1**: 注明 plug-in SE under-coverage 风险 + 推荐 n_expert<250 时用 bootstrap\n\n### 应该修正（显著改善质量）\n\n3. **Algorithm 1 / Remark 2**: asymmetric case 须说明用 M̂_s^{-1} 替代 Ĉ_s^{-1}\n4. **全文**: 统一 κ 符号（κ_s vs κ_global 下标）\n5. **Abstract/Intro**: 明确限定 \"7.4×\" 的适用条件（extreme heterogeneity, K=2）\n6. **Remark 2**: 补充 EC-HTE 在 asymmetric case RMSE 劣于 global 的事实及原因\n7. **Contribution list**: Corollary 4 降级为 Theorem 1 段内推论\n\n### 建议修正（锦上添花）\n\n8. **Figure 3**: 分区线标注 Proposition 5 threshold 公式\n9. **正文**: F-L 缩写定义前移\n10. **Limitations**: 补充 S misspecification 讨论\n\n### Rebuttal 重点准备\n\n- A5 在证明中的确切角色（Q1）\n- κ-guard hybrid estimator 理论性质（Q2）\n- 方法论新颖性的 impact-based 辩护（sign reversal 首次报告 + CivilComments 实质结论变化）\n- Venue fit 论据（EMNLP 近年接收 causal inference for NLP 论文 + LLM annotation 核心趋势）",
    "project": "ec_hte_llm_annotation",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.5 - Borderline Conference",
    "review_chat_id": "oc_489afd65980834a91024fd48e21d984f"
  }
}
```

</details>

---


### Tool result

_source line 2617 · 2026-05-25T21:38:48.668937+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_6b114d432b35fe7a1c2143457ae85b08:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 3817
}
```

</details>

---


### Assistant

_source line 2618 · 2026-05-25T21:38:57.655573+00:00_

**Round 24 审稿完成。**

两位 Reviewer 高度收敛（仅 W4 Corollary 4 叙事价值有细微分歧），无需进入 Round 2。

**报告已投递** — Overall 3.5 (Borderline Conference)。核心发现：

| 级别 | ID | 问题 |
|------|----|------|
| Must-Fix | N1 | A3 松弛下 "identity remains exact" 混淆 matrix form 与 scalar form |
| Must-Fix | N2 | Plug-in SE 忽略 CM 不确定性，93.8% coverage 藏在 footnote |
| Should-Fix | W5 | Remark 2 选择性报告：报 AUC=0.96 隐瞒 EC-HTE 全劣 |
| Should-Fix | W1-W4 | Notation 不一致 + Abstract framing 过宽 + Corollary 4 呈现 |

N1/N2 均为文本修正级别（非根本性方法缺陷），修正后 score 可升至 4.0。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director"
}
```

</details>

---


## Round 202

## Round 202

2 recorded events


### User

_source line 2619 · 2026-05-25T21:38:58.646670+00:00_

[Reviewer 2 审稿结果]:
交叉审查已提交。

要点：在 R1 的 14 条意见中，我同意 12 条（含 2 条 Must-Fix），对 1 条（W4 Corollary 4）部分反驳，并将 R1 的 M4（Appendix J Table 10 选择性报告）升级为 Should-Fix。两位 Reviewer Overall 均为 3.5。

---

[Reviewer 1 审稿意见]:
## Reviewer 1 交叉回应 Reviewer 2 的审稿意见

---

### Must-Fix 问题

**[REBUT] R2-N1: 引用 "Sui et al., 2026" (PPCI) 无法验证**

该引用在 references.bib 中有完整条目：Sui, Yang; Zhou, Jin; Zhou, Hua; Dai, Xiaowu. "Prediction-Powered Conditional Inference." arXiv:2603.05575, 2026。arxiv ID 2603.05575 指向 2026 年 3 月的预印本，距今仅两个月。R2 提到的 arxiv:2502.06343（Cadei, Demirel 等人）是另一篇不同的论文，两者并非同一工作。

R2 通过 web search 未找到可能因为：(a) 该预印本较新（3 月发布），搜索引擎索引延迟；(b) 搜索关键词不匹配。建议 R2 或 AC 直接访问 arxiv.org/abs/2603.05575 验证，而非依赖 web search。在确认该 arxiv ID 不存在之前，不应将此标记为学术诚信问题。

**[AGREE] R2-N2: Related Work 严重不足——但需补充上下文**

同意 Section 2 正文仅 ~7 行确实过于简略。但需指出几个事实：

(a) Appendix F（Extended Related Work，p.13-14）包含约 1.5 页的详细讨论，涵盖 measurement error details (Fuller 1987, Carroll 2006)、annotation model extensions (Dawid 1979, Passonneau 2014, Hovy 2013, Paun 2018)、PPI extensions (Zrnic 2024)、treatment vs. effect-modifier misclassification (Imai 2010, Knox 2020)、econometrics of binary misclassification (Bound 2001, Frazis 2003, Black 2000, Mahajan 2006, Lewbel 2007)。

(b) R2 声称 Mahajan (2006) 缺失——实际已在 Appendix F (appendix.tex line 214) 引用并讨论。

(c) 8 页限制下将 Related Work 压缩并指向 appendix 是常见策略。

不过我同意以下改进是必要的：正文应至少用 2-3 句话概述 PPI/DSL/PPCI 各自解决什么问题以及与本文的区别，而非只列举引用。R2 建议的 noisy label learning 文献 (Xia 2020, Cheng 2022) 虽然相关，但这些工作主要解决训练阶段的 label noise（学习一个鲁棒的分类器），而本文关注推理阶段的 measurement error correction（用 noisy labels 做因果推断），目标场景不同。建议在正文补充一句区分即可，无需大段引用。

---

### Should-Fix 问题

**[REBUT] R2-W1: 新颖性相对 F-L (2003) 为增量，"只是 2×2 矩阵代数"**

不同意。理由：

1. **质变而非量变**：F-L (2003) 推导的是 homogeneous error 下的 scalar attenuation β̂ = (1−2π)β——估计值被均匀缩小。Theorem 1 揭示的是 heterogeneous error 下的 product structure δ_s·Δτ/(1−2π̄)——correction 可以在 low-error subgroups **反转** 因果效应符号（Section 5.2: 14.9% 配置出现 sign reversal，Figure 5）。Sign reversal 是 F-L 框架完全不可见的定性新现象。

2. **证明简洁不等于贡献简单**。Shannon 信息论的核心定理推导也是"直接计算"，但 insight 是新颖的。本文的 insight 在于发现 global correction 在 subgroup 层面可以比不校正更差（Proposition 5），这对当前广泛使用 global confusion matrix correction 的 CSS 实践有直接警示意义。

3. **推广维度非平凡**：F-L 只处理单一 regressor 的 scalar attenuation，不涉及 subgroup heterogeneity、effect modifier structure、或 confusion matrix inversion。Theorem 1 处理的是 K 个 subgroup 的 matrix product structure，并扩展到 multi-class (Corollary 6, Appendix C)、asymmetric CM (Remark 2, Appendix J)、heterogeneous treatment effects (Proposition 3)。

**[AGREE] R2-W2: Proposition 5 增量价值需论证——部分同意**

R2 的核心质疑有道理：如果已有 per-subgroup error rates（diagnostic 的输入），离 EC-HTE 的输入（per-subgroup CMs）已经很近。但 Proposition 5 的价值不仅在于 "判断是否运行 EC-HTE"：

- **资源分配决策**：在 pilot study 阶段，practitioner 可能只有粗略的 per-subgroup accuracy（如从小样本或文献报告中获得），还未收集足够的 expert labels 做 full CM estimation。Diagnostic 帮助决定是否值得投入 n_expert≥250 的标注预算。
- **理论理解**：条件 |δ_s|/((1−2π̄)·π_s)>1 将 "何时 correction 有害" 的边界以 closed-form 刻画，帮助理解机制而非仅作为工程工具。

但我同意论文应更明确说明 Proposition 5 的 use case 场景，目前论述确实不充分。

**[REBUT] R2-W3: Venue 适配性——核心贡献更偏 causal inference 而非 NLP**

不同意。本文的：
- 动机来自 NLP：LLM annotations 替代人工标注（Section 1 line 1-5）
- 实验在 NLP 任务上：TweetEval (sentiment), CivilComments (hate speech), AG News (topic), stance detection，使用 8 个真实 LLM 的 confusion matrices
- 目标读者是 CSS+NLP 交叉社区——这正是 EMNLP 近年增长最快的投稿领域之一
- PPI/DSL 等同类工作已在 EMNLP/ACL 发表

EMNLP CFP 明确包含 "Computational Social Science" 和 "NLP Applications" 作为 topics。方法论的数学基础在 measurement error / causal inference，但应用场景和验证完全在 NLP 范围内。

**[AGREE] R2-W4: "Debiasing" 术语歧义**

同意。在 NLP 社区，"debiasing" 最常见的含义是 fairness debiasing (removing demographic bias from word embeddings/LLMs)。本文使用 "debiasing" 指 measurement error correction，可能造成误导。建议在 Introduction 第一段明确区分："debiasing" in this paper refers to confusion-matrix-based error correction, not fairness debiasing。标题 "When Debiasing Hurts" 本身是好的（有传播力），但正文需要一句话消歧。

**[REBUT] R2-W5: Abstract 数字密度过高**

Abstract 140 words 包含约 6 个关键数字（5×, 14.9%, 7.4×, Δπ>0.15, n_expert≥250, K≤4）。对于一篇同时有理论和实验贡献的论文，这些数字每个都对应一个核心 claim：
- 5× 量化问题规模
- 14.9% 量化 sign reversal 频率（核心 negative result）
- 7.4× 量化方法改进幅度
- operating conditions 量化适用边界

去掉任何一个都会削弱 abstract 的信息量。这是风格偏好，不是质量问题。ACL/EMNLP 的高分论文中数字密集的 abstract 并不少见。

---

### Minor Issues

**[AGREE] R2-Minor-1: "Audinet de Pieuchon" 拼写可能有误**
无法独立验证，合理建议。

**[REBUT] R2-Minor-2: Table 1 与 Table 2 RMSE 差异讨论不足**
Table 1 (supplementary, moderate heterogeneity) 和 Table 2 (main, extreme heterogeneity) 的差异在 Section 5.3 末段已有明确讨论（experiments.tex lines 63-66）："Under moderate heterogeneity (Δπ≤0.10), methods converge: HB EC-HTE and global correction yield indistinguishable |bias| (0.005 vs. 0.009) and RMSE (0.075 vs. 0.074), confirming the diagnostic's guidance (Table 1)."

**[AGREE] R2-Minor-3: Figure 3 y 轴标签字体偏小**
同意，我在阅读 PDF 时也注意到 Figure 3 (heatmap) 的标注密度偏高。

**[REBUT] R2-Minor-4: 25 个 Appendix 可精简**
附录数量多是因为实验覆盖面极广（这也是本文的优势之一）。每个 appendix section 回答一个具体的可预见质疑（K=8? asymmetric? class imbalance? calibration? A1 violation? confounded assignment?）。精简附录会削弱论文的 robustness 叙事。我在自己的审稿中将 "实验极其充分" 列为 S3 优势。

**[AGREE] R2-Minor-5: Conclusion 偏短，缺少更广泛影响讨论**
同意。Conclusion (conclusion.tex) 约 11 行，列出了 three-step protocol 但缺少对更广泛影响的讨论（如：其他 measurement error 场景、与 active learning 的结合、policy implications）。最后一句 "Future directions include continuous covariates, larger K, and joint covariate-outcome correction" 过于简略。

---

### Missing References

**[REBUT] Mahajan (2006)**: 已在 Appendix F (appendix.tex line 214) 引用并讨论。R2 可能未读到附录。

**[AGREE] Xia et al. (2020), Cheng et al. (2022), Zhu et al. (2022)**: 这些 noisy label learning 文献值得在 Related Work 中提及并区分——它们解决 training-time noise（学鲁棒分类器），而本文解决 inference-time measurement error（用 noisy labels 做因果推断）。一句话区分即可。

**[AGREE] Keith et al. (2020)**: Text and causal inference 的综述，与本文高度相关，应引用。

**[REBUT] Fong & Tyler (2021)**: 需要具体论文信息。如果指 Fong & Tyler "Machine Learning Predictions as Regression Covariates"，这与 PPI 框架类似但早于 PPI 的形式化。已有 PPI/DSL 引用覆盖此方向。

---

### Questions

**[REBUT] R2-Q1: Sui et al. 2026 PPCI 引用完整信息**
已在 bib 中确认：Sui, Yang; Zhou, Jin; Zhou, Hua; Dai, Xiaowu. "Prediction-Powered Conditional Inference." arXiv:2603.05575. 2026. 建议 AC 直接验证此 arxiv ID。

**[AGREE] R2-Q2: Proposition 5 的 marginal value**
见上述 W2 回应。同意需要更好的 use-case 论证。

**[REBUT] R2-Q3: A1 sensitivity range γ_T≤0.05 偏窄**
论文实际测试范围到 γ_T=0.20（Appendix Y.3, Figure 10），覆盖 degradation 在 γ_T=0.10 时 coverage 降至 75%。论文保守地声称 robustness 仅到 γ_T≤0.05（coverage≥89.7%）。测试范围并不窄，只是 "claim robustness" 的范围保守——这恰恰是好的科学实践。

**[REBUT] R2-Q4: LLM calibration (Platt scaling) 作为替代**
已在 Appendix Y.7 (appendix.tex lines 1503-1531, Table 17) 实验验证。结论：calibration 将 naive coverage 从 84% 提升到 91.3%，但不达标（<95%）。Calibrated + EC-HTE 达到 96.5%。两者互补——calibration 降低 π_s，EC-HTE 修正残余的 δ_s 异质性。R2 可能未读到此 appendix。

---

[Reviewer 1 审稿结果]:
交叉审查回应已提交。

汇总：对 R2 的 23 个具体意见中，我给出 8 个 [AGREE]、12 个 [REBUT]、3 个部分同意。关键分歧集中在：

- **N1 (PPCI 引用)**：REBUT — bib 中有完整 arxiv ID (2603.05575)，R2 可能搜索关键词不匹配，建议 AC 直接验证
- **W1 (F-L 增量性)**：REBUT — sign reversal 是 F-L 不可见的定性新现象，证明简洁不等于贡献简单
- **W3 (venue 适配)**：REBUT — 动机、实验、目标读者全在 NLP/CSS 范围内
- **Q3/Q4**：REBUT — 论文附录已有对应实验（Y.3 测到 γ_T=0.20, Y.7 测了 calibration 互补性），R2 可能未阅读完整附录

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 2620 · 2026-05-25T21:39:49.469382+00:00_

收到 Reviewer 1 的交叉回应。综合两位 Reviewer 的交叉审查结果：

**收敛分析**：

| 维度 | R2 对 R1 | R1 对 R2 |
|------|----------|----------|
| 同意率 | 12/14 (86%) | 8/23 (35%) |
| 关键分歧 | W4 (Corollary 4 叙事价值) | N1 (PPCI 引用)、W1 (novelty)、W3 (venue fit) |

**核心共识（已锁定）**：
- ✅ N1 (A3 exact claim) + N2 (plug-in SE) = 两个 Must-Fix 无争议
- ✅ W5 (Table 10 选择性报告) 两位认可
- ✅ W1 (notation)、W2 (κ 符号) 两位认可
- ✅ Overall 3.5 两位一致

**分歧处理**：

R1 对 R2 的多条 REBUT 主要集中在三个方向：
1. **Novelty** — R1 辩护 sign reversal 是定性新现象。R2 维持 "known techniques to new context"。此分歧在报告中已如实记录为持续性争论（R20-C2, R20-W2），不改变评分。
2. **Venue fit** — R1 辩护 NLP 动机+实验+目标读者。R2 维持本质是 causal inference methodology。报告已记录（R21-N2）。
3. **R2 遗漏附录内容** — R1 指出 R2 多条质疑（PPCI 引用、calibration 替代、sensitivity range、Mahajan 引用）已在附录中有对应实验/讨论。这说明论文的 **主文可发现性** 存在问题——关键信息散落在 25 个附录中，审稿人实际审稿时未能完整阅读。

**结论**：R1 的交叉回应不改变报告核心结论和评分（3.5）。两个 Must-Fix + 五个 Should-Fix 的优先级排序不变。报告已投递，不需要 force_resubmit。

审稿圆桌会议结束。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director"
}
```

</details>

---
