# Policy Ambiguity & Agent Safety — Research Skill

蒸馏自 13 篇论文（8 深度 + 5 摘要），2003-2026。

## 评估范式共识

**从 binary outcome 到 multi-dimensional compliance** (7/8, 高) — AgentPex 发现 83% perfect-outcome traces 有 procedural violations；DRIP-R 用 5 维 Likert 替代 binary reward。设计 evaluation 必须分离 policy adherence、procedural compliance、outcome correctness。

**必用 Baseline**: GPT-5 系列 (6/8) + Claude (4/8) + ≥1 开源模型。τ-bench/τ²-bench 是 customer service agent 事实标准（被 4/8 篇引用/扩展）。5/8 篇创建新 benchmark → 新 benchmark 本身即贡献。

**LLM-as-judge 标准做法** (5/8, 高) — 多 judge 并行 + calibration (DRIP-R)，需报告 human agreement (κ 或 adjacent agreement)，按 risk/violation type 分别报告。

## Policy Ambiguity 三种操作化

1. **Taxonomy-driven** (4/13): 从 linguistics/RE 引入分类（11 NLP 类型；Massey regulatory ambiguity；DRIP-R 用 vagueness/semantic/coordination/incompleteness/missing condition）
2. **Gap-driven** (2/13): 识别 spec↔requirement divergence（PolicyBank: Ambiguous Scope / Under-Specified Exceptions / Logical Contradiction）
3. **Violation-driven** (2/13): 定义不可检测违规（PhantomPolicy 8 类 violation categories）

## Enforcement 方法谱 (4/8, 中)

- **Formal**: ShieldAgent (LTL + MLN), PhantomPolicy (graph invariants), MANTRA (SMT)
- **Spec extraction**: AgentPex (prompt→spec→evaluator)
- **Memory refinement**: PolicyBank (iterative policy entry evolution)
- 趋势: formal methods + LLM reasoning 混合上升。

## 竞品核心数字

| 论文 | Claim | 数字 |
|------|-------|------|
| ShieldAgent | 首个 agent guardrail | 90.1% recall, +11.3% |
| PhantomPolicy | Policy-invisible violations | 90-98% violation rate |
| DRIP-R | 模型间 fundamental disagreement | 95.8% 有分歧 |
| PolicyBank | Iterative refinement 闭合 spec gap | 0.01→0.74 pass^1 |
| AgentPex | Outcome≠compliance | 83% 完美 traces 有违规 |

## 研究空白

1. **跨域**: 6/8 局限 retail/airline/telecom；healthcare/legal 未测
2. **Resolution**: 检测歧义但不帮 agent 解决
3. **Taxonomy↔Safety 连接**: NLP ambiguity 分类未与 agent compliance 整合
4. **多利益方冲突**: fairness 分析初步但未形式化
5. **开源模型**: 几乎全是闭源 API
