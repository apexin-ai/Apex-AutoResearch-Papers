# Policy Ambiguity & Agent Safety — Writing Skill

蒸馏自 8 篇深度精读论文。

## 叙事策略

**主流故事: 突破局限型** (5/8, 高) — "现有工作假设 X，但现实是 Y"。PhantomPolicy: jailbreaking 之外的 failure mode；AgentPex: outcome≠compliance；PolicyBank: spec≠requirement。关键: 精确命名被忽略的维度。

**开篇钩子: 具体案例** (4/8, 高) — PhantomPolicy 用 HR 文件泄漏；DRIP-R 引用 Claude 利用政策漏洞。不要用 "Recently, LLM agents have..."，用读者 3 秒能理解的具体场景。

**张力: 二元对立** (6/8, 高) — outcome vs process, spec vs requirement, visible vs invisible, single vs dual-control, binary vs ambiguous。找到核心对立做成论文 spine。

**Contribution 排列** (8/8, 高) — 3-4 项，顺序: problem formulation → method → benchmark → findings。第一项放 problem definition 而非方法。

## 图表模式

**Figure 1**: 系统架构/pipeline 图 (3/6)。让读者 30 秒理解系统做什么。PolicyBank 用 motivation 对比图是有效变体。

**结果可视化**: grouped_bar 最常用（per-category/per-metric），radar 用于多维模型对比 (DRIP-R)，line_plot 用于 temporal 分析。主结果用表格放精确数字，图做 pattern 可视化。

**主结果表**: Row=methods, Col=grouped by metric/dataset, bold_best 标准。必须含 no-intervention baseline。PhantomPolicy 按 condition 拆 4 表适合分类论文。

**消融**: full_numbers 主流；渐进式 degradation (100→50→0%) 或 accumulation (None→Reward→Explanation→Oracle) 比开关式更有说服力。

**图表分工**: 图=motivation/architecture/trend；表=数字/对比/ablation；附录=per-model breakdown/统计/示例。

## 可模仿技巧

1. **概念命名**: "policy-invisible violations", "willful disobedience", "specification gap"。2-3 词命名现象使其可引用。
2. **演化轨迹图**: PolicyBank 展示 entry 三阶段演化 (strict→over-general→precise)，一图证非单调性。
3. **意外发现增值**: DRIP-R fairness 分析 (Big Five→outcome bias) 非核心但大增影响力。
4. **形式化框架**: Dec-POMDP 形式化客服场景提升理论深度 (DRIP-R, τ²-bench)。
5. **Benchmark 对比表**: 必有 "我们 vs 现有" feature matrix，读者快速定位入口。
