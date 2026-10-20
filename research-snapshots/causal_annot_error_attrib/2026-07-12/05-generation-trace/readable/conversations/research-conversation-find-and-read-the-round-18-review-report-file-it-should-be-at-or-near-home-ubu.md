# Research conversation: Find and read the Round 18 review report file. It should be at or near /home/ubuntu/.agent-ml-research-prod_0510/project

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 5
- **Recorded user turns:** 1
- **Tool calls:** 1
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a807f85b91f7d7f07.jsonl`
- **Structured JSON:** [`9fc8b333fadb9592b09f.json`](../../sessions/9f/9fc8b333fadb9592b09f.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

5 recorded events

### User

_source line 1 · 2026-05-23T15:49:11.292Z_

Find and read the Round 18 review report file. It should be at or near /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_reports/round_18.md. Read the entire file and return its complete contents.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "353a8574-7b32-433b-9ea2-17e96b7503f1",
  "agentId": "a807f85b91f7d7f07",
  "type": "user",
  "uuid": "adf373bf-2111-4f18-bce1-63fc6a4f48d4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/director_d3562b73",
  "sessionId": "824f3111-42c3-4ec6-b193-944b13769b09",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "wild-enchanting-sphinx"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-23T15:49:13.143Z_

I'll locate and read the Round 18 review report file for you.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "adf373bf-2111-4f18-bce1-63fc6a4f48d4",
  "isSidechain": true,
  "agentId": "a807f85b91f7d7f07",
  "requestId": "req_011CbKmJK9owN13URyhe4v1t",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "7af50d8c-2f21-4d9b-8fdd-3ef0ee66b56a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/director_d3562b73",
  "sessionId": "824f3111-42c3-4ec6-b193-944b13769b09",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "wild-enchanting-sphinx",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01ACnd9j6hSucmuQCL5jb1TX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 37233,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 37233,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-23T15:49:13.379Z_

<details open><summary>🔧 Tool call — Read · `toolu_01PYhYYqf34oVHfSBgoRuJRv`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_reports/round_18.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7af50d8c-2f21-4d9b-8fdd-3ef0ee66b56a",
  "isSidechain": true,
  "agentId": "a807f85b91f7d7f07",
  "requestId": "req_011CbKmJK9owN13URyhe4v1t",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "33b49d55-2f3c-4f44-805c-98501b071853",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/director_d3562b73",
  "sessionId": "824f3111-42c3-4ec6-b193-944b13769b09",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "wild-enchanting-sphinx",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01ACnd9j6hSucmuQCL5jb1TX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 37233,
      "cache_read_input_tokens": 0,
      "output_tokens": 109,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 37233
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 109,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 37233,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 37233,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-23T15:49:13.391Z_

<details><summary>↩ Tool result · `toolu_01PYhYYqf34oVHfSBgoRuJRv`</summary>

```text
1	---
2	round: 18
3	review_mode: fresh
4	overall_score: 3.5 - Borderline Conference
5	timestamp: 2026-05-23T15:44:43.616326+00:00
6	reviewer_ids: [1, 2]
7	cross_response_reviewer_ids: [1, 2]
8	force_resubmit: False
9	---
10	
11	# 审稿报告：Round 18（Fresh Review）
12	
13	**论文**: Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction
14	**Venue**: EMNLP 2026 (ARR Long Paper)
15	**审稿模式**: Fresh（重新审稿）
16	**Reviewer**: R1（方法严谨性）+ R2（新颖性/完整性）
17	**日期**: 2026-05-23
18	
19	---
20	
21	## Summary
22	
23	本文研究 LLM 标注器产生的多类别标注误差（K≥3）如何在 7 种典型因果 DAG 拓扑下传播到下游因果估计。核心贡献包括：(1) 在非差异错分类假设下推导 7 种拓扑的闭式偏差表达式，建立 sign-preservation/reversal 二分法（5 种拓扑保持符号，exposure 和 IV 可逆转）；(2) 定义 Annotation Sensitivity Values (ASV) 框架，包含幅度、显著性和符号翻转三种诊断，揭示从 IV（最脆弱）到 M-bias（免疫）的拓扑依赖脆弱性谱；(3) 证明 FWL 不变性使得矩阵校正方法在四种协变量拓扑下精确无效（0% bias reduction），并评估 5 种校正方法。论文通过 Monte Carlo 模拟（161 场景，grand MAPE 1.6%）和 23 个真实 LLM 配置（HumAID K=10, VAST K=3, CivilComments K=2）进行实证验证。
24	
25	---
26	
27	## Strengths
28	
29	**S1. 真正的统一拓扑分析**: 首次在统一框架内系统比较同一 confusion matrix 在 7 种 DAG 拓扑下产生定性不同的偏差。sign-preservation/reversal 二分法是一个清晰有力的核心发现，填补了流行病学测量误差理论与 NLP 实践之间的缺口。[R1-S1, R2-Strength-1, 共识]
30	
31	**S2. FWL 不变性负面结果**: 证明矩阵校正方法（confusion matrix inversion）对 4 种协变量拓扑的 bias reduction 为精确 0%——这是一个干净、完整的结构性结果（Appendix B.2 列空间论证），对实践者有直接警示意义。[R1-S3, R2-Strength-2, 共识]
32	
33	**S3. 诚实的认知层级**: Proved（K=2, Theorem 1）→ Verified（K≥3, Observation 1）→ Conjectured（Conjecture 1）的三级层次在理论论文中值得赞赏，避免了对 K≥3 结果的过度声称。[R1-S2, R2-Strength-4, 共识]
34	
35	**S4. 全面的实证验证**: 161 scenarios × 23 LLM configurations × 3 NLP tasks；100,000 Dirichlet matrices；theory-MC MAPE 1.6%（per-topology 0.3%-3.7%）。F₁ 与因果 bias 无显著相关性（Spearman ρ = -0.10, p = 0.45）的发现对 CSS 研究者有直接可操作价值。[R1-S4, R2-Strength-3/5, 共识]
36	
37	**S5. 实用决策框架**: ASV 与 E-value 类比设计得当，Algorithm 1 的拓扑感知校正决策树为实践者提供清晰操作指南。[R1-S5]
38	
39	---
40	
41	## Weaknesses
42	
43	### Must-Fix（影响接收决定）
44	
45	**MF-1** [format] **正文页数超出 EMNLP 2026 strict 8-page limit**
46	- Section 5 Conclusion 完整位于第 9 页（约 13-14 行主文内容溢出）。EMNLP 2026 strict 8-page limit 是硬约束，违规可致 desk rejection。
47	- R2 首提为 critical，R1 交叉确认违规存在但建议降级。**Director 裁决 must-fix**：格式合规是硬约束，修复成本极低（压缩 Section 4.5 + 精简 Conclusion）。
48	- 修复方案：(a) 精简 Section 4.5 "Case studies and sensitivity" 段落（细节已在 Appendix）；(b) Conclusion 压缩至 5-6 行；(c) 或将 Figure 4/5 之一移至 Appendix。
49	
50	**MF-2** [soundness] **非差异错分类假设在 LLM 标注器语境下缺乏直接实证检验**
51	- Definition 1 要求 P(A*=j|A=k,Y) = P(A*=j|A=k)。LLM 预训练数据编码 A-Y 关联，可能系统性违反此假设。现有检验不充分：Appendix B.5 VAST topic-stratified 检验仅一个数据集，且 topic 分层 ≠ Y 分层；Appendix B.6/B.8 stress test 显示 ε=0.01 structured departure 即导致 14/16 K≥3 exposure 配置 sign reversal。
52	- R1 首提为 critical，R2 交叉 AGREE（但补充结构性论证——LLM API 不观测 Y——比 R1 承认的更强）。**共识 must-fix**。
53	- 修复方案：在至少一个有 gold labels 的 NLP 数据集上，按 Y 值分层计算 LLM 错分类矩阵，直接检验 P(A*|A,Y=0) ≈ P(A*|A,Y=1)。即使只做一个数据集（如 HumAID），也能为结构性论证提供 empirical backing。
54	
55	### Should-Fix（影响评分但不一票否决）
56	
57	**SF-1** [soundness, 高优先级] **K≥3 ASV monotonicity 仅为 Conjecture，削弱 Contribution 2 的理论定位**
58	- Theorem 1（envelope monotonicity）仅在 K=2 + proportional effects 下证明。K≥3 依赖 Observation 1（数值验证，ε<0.02）和 Conjecture 1。论文核心论点是 K≥3 引入结构性新现象，但其 ASV 框架恰恰无法为 K≥3 提供形式化保证。
59	- R2 首提为 critical，R1 交叉 AGREE with nuance（K≥3 贡献多维——偏差表达式、sign preservation、FWL 均对一般 K 成立，不仅限于 monotonicity；ε<0.02 使 ASV 误差在 2% 以内）。**Director 裁决 should-fix（高优先级）**：R1 论点有力，K≥3 贡献确实不仅限于 monotonicity。
60	- 修复方案：(a) 将 Contribution 2 重新表述为 "empirically validated diagnostic with proved K=2 foundation"；(b) 补充 monotonicity failure 的后果分析（如果 ε 达到极端值，对 ASV ranking 的影响有多大）。
61	
62	**SF-2** [soundness, 高优先级] **比例效应假设 (f=λg) 在 NLP 场景下缺乏具体讨论**
63	- Theorem 1 依赖 f=λg。在 NLP 多类别处理（如 stance detection 的 favor/against/neutral）中，不同类别可能有质性不同的效应，不满足比例关系。论文仅一句话提及 "plausible in NLP tasks with a single quality dimension"。
64	- R1 首提为 critical，R2 REBUT 降为 should-fix（假设仅影响 Theorem 1 monotonicity，Proposition 3 提供 general case fallback，97.3% 实证保持率）。**Director 采纳 should-fix（高优先级）**：R2 论证有力——假设范围比 R1 描述的更窄。
65	- 修复方案：增加 2-3 句具体 NLP 因果推断场景的分析（如 stance detection 3-class 是否接近 proportional）。
66	
67	**SF-3** [scope] **Logistic regression 讨论不充分**
68	- NLP 最常用 logistic regression。主文仅一句话提及 FWL invariance 在 logistic 下的破缺（Section 4.5）。Appendix B.14 显示 FWL 破缺幅度随 accuracy 增大（exposure: -22% to -78%）。Algorithm 1 未区分 OLS/logistic 路径。
69	- R1 首提，R2 强烈同意。**共识 should-fix**。
70	- 修复方案：Section 4.5 增加 1-2 段 logistic regression 指导，引用 Appendix B.2/B.7/B.14；Algorithm 1 增加 OLS/logistic 分支。
71	
72	**SF-4** [presentation, 高优先级] **术语壁垒对 NLP 读者可达性不足**
73	- plim、FWL theorem、Wald estimator、column-stochastic matrix、Birkhoff polytope、Dirichlet prior——对 EMNLP 受众属于高门槛术语，直觉解释不充分。如果多数 reviewer 无法流畅理解 method section，将影响 soundness 和 confidence 打分。
74	- R2 首提，R1 交叉 AGREE。**共识 should-fix**。
75	- 修复方案：每个关键术语首次使用时增加 1-2 句直觉解释（约增 6-8 行，页数压缩后有空间）。
76	
77	**SF-5** [presentation] **Contribution 3（correction guidance）正文深度与"贡献"定位不匹配**
78	- "Topology-aware correction guidance" 被列为三大贡献之一，但正文仅约 0.7 页。Algorithm 1 仅在 Appendix。与 Contribution 1（~3 页 method）和 Contribution 2（~1.5 页 ASV + experiments）相比深度不足。
79	- R2 首提，R1 交叉 AGREE（倾向降级为 practical implication）。**共识 should-fix**。
80	- 修复方案：(a) 将 Algorithm 1 提升至正文（需结合 MF-1 的压缩方案）；或 (b) 降级为 "practical implication" 而非 co-equal contribution。
81	
82	**SF-6** [novelty] **ASV 与 E-value 的比较框架有误导性**
83	- Remark 1 的三点 "structural distinctions from E-values" 本质上是不同工具解决不同问题（annotation error vs. unmeasured confounding）。当前表述暗示 ASV 是 E-values 的改进版。ASV 的真正贡献是将 sensitivity analysis 范式适配到 annotation error + topology dependence。
84	- R2 首提，R1 交叉 AGREE with nuance（distinctions 准确但表述暗含 improvements over）。**共识 should-fix**。
85	- 修复方案：Remark 1 重新框定为互补工具（complementary tools for different sources of bias）。
86	
87	**SF-7** [experiments] **Dirichlet(1,1,...,1) 采样对高维 K 代表性不足**
88	- K=5（20 参数）和 K=7（42 参数）下，均匀 Dirichlet 采样偏离实际 LLM 矩阵分布（对角线期望 1/K vs 实际 >0.6）。R2 补充：23 个经验 LLM 矩阵已验证核心结论，代表性问题不影响最终结论。
89	- R1 首提，R2 交叉 AGREE。**共识 should-fix（低优先级）**。
90	- 修复方案：补充 Dirichlet(α,1,...,1) (α>>1) 采样验证，或报告对角线 >0.6 子空间的 ε 值。
91	
92	**SF-8** [method] **Significance ASV 对样本量 N 的依赖未充分探讨**
93	- δ_sig 通过 SE(N) 依赖于 N，Figure 3 仅展示单一 N 值。不同 N 下 significance ASV 的变化是 practitioners 的关键决策信息。
94	- R1 首提，R2 交叉 AGREE。**共识 should-fix**。
95	- 修复方案：增加不同 N（如 1K, 5K, 10K, 50K）下各拓扑 δ*_sig 变化的可视化（Figure 或 Table）。
96	
97	**SF-9** [soundness] **Conjecture 1 的 ε<0.02 约束缺乏理论直觉**
98	- ε 约束完全来自数值实验，论文未解释为什么 ε 应该很小。R2 补充可能的直觉路径：proportional effects 下精确单调，deviations 来自 non-proportional residual。
99	- R1 首提，R2 交叉 AGREE。**共识 should-fix**。
100	- 修复方案：补充 1 段关于 ε 小的直觉论证（如与列随机矩阵空间的凸体结构或 proportional residual 分析相关）。
101	
102	### Minor（不影响接收）
103	
104	1. **Abstract 信息密度过高**：约 184 words 符合 ≤200 限制，但 7+ 具体数字首次阅读难以消化。建议精简至 2-3 个最具冲击力的数字。[R2-minor-2, R1 AGREE]
105	2. **Figure 2 灰度打印可辨识性**：红色 sign reversal 标识在灰度下难以区分，建议增加 hatching/pattern fill。[R2-W4, R1 AGREE]
106	3. **τ 符号 overloading**：τ 在不同拓扑下含义不同但未充分标注。[R2-minor-1, R1 AGREE]
107	4. **Orphan bib entries**：manski1990 未在正文引用，应移除或添加引用。[R2-minor-3]
108	5. **引用格式不一致**：部分 bib 条目缺 doi 或页码。[R2-minor-4]
109	6. **"First unified analysis" 措辞**：限定词过多，建议简化为 "first systematic topology-specific comparison"。[R2-W5, R1 partial REBUT: claim 有合理基础但措辞可优化]
110	
111	---
112	
113	## Reviewer Consensus
114	
115	以下问题两位 Reviewer 达成共识（[AGREE] 或交叉后无争议）：
116	
117	1. **非差异错分类假设需要 Y-stratified 实证检验** [must-fix] — R1 首提，R2 AGREE
118	2. **页数超限需修复** [must-fix (R2) / should-fix (R1)] — 违规存在无争议，仅严重性有分歧
119	3. **Logistic regression 讨论不充分** [should-fix] — R1 首提，R2 强烈同意
120	4. **NLP 术语壁垒** [should-fix] — R2 首提，R1 AGREE
121	5. **Contribution 3 深度不足** [should-fix] — R2 首提，R1 AGREE
122	6. **ASV vs E-value 框架重新定位** [should-fix] — R2 首提，R1 AGREE with nuance
123	7. **Figure 2 灰度可辨识性** [minor] — R2 首提，R1 AGREE
124	8. **Significance ASV N-dependence** [should-fix] — R1 首提，R2 AGREE
125	9. **Conjecture 1 ε 理论直觉** [should-fix] — R1 首提，R2 AGREE
126	
127	---
128	
129	## Reviewer Divergence
130	
131	以下问题存在严重性分级分歧（**Director 已裁决**）：
132	
133	| 问题 | R1 判断 | R2 判断 | Director 裁决 | 理由 |
134	|------|---------|---------|---------------|------|
135	| 比例效应 f=λg 假设论证 | critical | should-fix (REBUT) | **should-fix（高优先级）** | R2 论证有力：假设仅影响 Theorem 1 monotonicity，Proposition 3 提供 fallback，97.3% 实证保持率 |
136	| 页数超限 | should-fix (M5) | must-fix (N1) | **must-fix** | 格式合规是硬约束，修复成本极低 |
137	| K≥3 monotonicity 理论缺口 | strong should-fix | must-fix (N2) | **should-fix（高优先级）** | K≥3 贡献多维（偏差表达式 + sign preservation + FWL），不应仅以 monotonicity 证明缺口评判 |
138	
139	---
140	
141	## Questions
142	
143	汇总两位 Reviewer 的关键提问（供 author response 参考）：
144	
145	1. **ClinicalBERT case study 中是否检验了 f=λg？** 不同吸烟状态类别对死亡率的效应是否近似成比例？[R1-Q1]
146	2. **2.7% 不满足 Theorem 1 条件的 LLM 配置有什么共同特征？** 是否与特定 LLM 或数据集相关？[R1-Q3]
147	3. **Sign-flip ASV 的实际使用循环**：practitioners 需要先知道真实 τ 的符号才能计算 sign-flip ASV，如何处理这个 bootstrap 循环？[R2-Q3]
148	4. **Logistic regression 下 FWL 破缺幅度对大 K 如何变化？** Table 5 只测试了 K=3。[R1-Q4]
149	5. **多维 ASV 的可能性**：当前沿单一 C(δ) 路径搜索，是否考虑过 per-category sensitivity？[R1-Q5]
150	6. **非差异假设的 stress test 含义**：ε=0.01 即导致 14/16 K≥3 exposure sign reversal，是否意味着论文分析对 differential misclassification 极其脆弱？[R2-Q4]
151	
152	---
153	
154	## Missing References
155	
156	- **Imai and Yamamoto (2010)**, "Causal Inference with Differential Measurement Error" — 与非差异假设形成对比 [R1 建议, R2 AGREE]
157	- **Nguimkeu, Denteh & Tchernis (2019)**, "On the estimation of treatment effects with endogenous misreporting" — treatment misclassification 相关 [R2 建议]
158	- **Ogburn and VanderWeele (2013)** — bias amplification under covariate misclassification 后续工作 [R1 建议, R2 指出 2012 版已引用]
159	
160	---
161	
162	## External Review (Stanford Agentic Reviewer)
163	
164	**状态**: 未请求。本项目未配置外部审稿。
165	
166	---
167	
168	## Visual Layout Check（非评分项）
169	
170	**状态**: error — 视觉审查 Agent 因 rate limit 未能完成检查（"You've hit your limit · resets 4pm (UTC)"）。用户可在 limit 重置后重新触发。
171	
172	---
173	
174	## Overall Assessment
175	
176	**Overall Score: 3.5 / 5 — Borderline Conference**
177	
178	| 维度 | R1 | R2 | 合并 |
179	|------|----|----|------|
180	| Soundness | 3.5 | 3.5 | 3.5 |
181	| Excitement | 3.5 | 3.5 | 3.5 |
182	| Reproducibility | 4.0 | 4.0 | 4.0 |
183	| Confidence | 4 | 4 | 4 |
184	
185	**综合评语**：
186	
187	论文在统一框架内首次系统分析了多类别标注误差在 7 种 DAG 拓扑下的因果偏差传播，贡献真实（bias taxonomy + FWL invariance 负面结果）、验证充分（161 scenarios, 1.6% MAPE）、认知层级诚实。FWL 不变性证明和 F₁ 与因果 bias 无相关性的发现对实践者有直接价值。
188	
189	制约评分的主要因素：
190	
191	1. **Must-fix 阻塞项**：(a) 页数超限需压缩（修复成本低）；(b) 非差异错分类假设缺乏 Y-stratified 实证检验（修复需要实验工作，但在 HumAID 上可行）。
192	
193	2. **理论-应用鸿沟**：核心理论保证（Theorem 1 monotonicity）仅在 K=2 + proportional effects 下成立，而论文的核心卖点是 K≥3 的结构性新现象。虽然偏差表达式和 FWL 不变性对一般 K 成立（不依赖 Theorem 1），ASV 框架的 K≥3 保证仍是 conjectural。Contribution 2 需要更谨慎的定位。
194	
195	3. **受众适配**：面向 EMNLP 的论文使用大量计量经济学术语（plim、FWL、Wald estimator），NLP 读者的可达性不足。Correction guidance（Contribution 3）作为核心贡献之一但正文深度不匹配。
196	
197	**条件上调**：如果作者在 revision/rebuttal 中充分回应 MF-2（Y-stratified 检验）、SF-1（Contribution 2 重新定位）和 SF-4（术语直觉解释），评分可上调至 **4.0（Conference）**。MF-1（页数超限）是纯排版修复，不影响学术评价。
198	
199	---
200	
201	## Detailed Comments
202	
203	### Section-by-Section
204	
205	**Abstract**: 184 words 符合 ≤200 限制（R17 已验证）。信息密度高但主要结论完整。建议减少具体数字（保留 83.4% sign reversal 和 1.6% MAPE 两个核心数字即可）。FWL invariance 声明建议加 "under linear OLS" 限定。
206	
207	**Introduction**: 三大贡献清晰列出。"first unified analysis" claim 在当前文献范围内成立（R1 确认），但限定词过多，建议简化措辞。Contribution 3 的正文深度需与定位匹配。
208	
209	**Related Work**: 覆盖全面，四个关键领域（measurement error、LLM annotation、sensitivity analysis、correction methods）均有充分引用。可考虑补充 Imai & Yamamoto (2010) 和 Nguimkeu et al. (2019)。
210	
211	**Method (Section 3)**: 核心理论贡献所在。Bias expressions (公式 1-5) 推导清晰。Theorem 1 → Observation 1 → Conjecture 1 层次诚实。主要问题：(1) 术语壁垒（plim、FWL、Wald 等需直觉解释）；(2) proportional effects 假设缺 NLP 场景讨论；(3) Remark 1 的 ASV-E-value 比较需重新框定为互补工具。
212	
213	**Experiments (Section 4)**: 验证充分（161 scenarios, 1.6% MAPE）。Empirical validation 使用 3 个真实 NLP 数据集和 23 个 LLM 配置。F₁ 无预测因果 bias 的发现有力。主要问题：(1) Correction guidance (Section 4.5) 深度不足；(2) logistic regression 讨论不充分；(3) Significance ASV 的 N-dependence 需更系统展示。
214	
215	**Conclusion + Limitations**: Conclusion 需压缩（当前导致超页）。Limitations 覆盖三个点（non-differential 假设、linear SEM、C 可估计性），位置正确（正文内）。
216	
217	**Appendix**: 24 页，B.1-B.24 共 24 个子节，验证详尽。FWL 证明（B.2）完整。Logistic regression 验证（B.7, B.14）存在但主文未充分引用。交叉引用密集但结构清晰。
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "33b49d55-2f3c-4f44-805c-98501b071853",
  "isSidechain": true,
  "promptId": "353a8574-7b32-433b-9ea2-17e96b7503f1",
  "agentId": "a807f85b91f7d7f07",
  "type": "user",
  "uuid": "dd19c11d-06e5-4d35-b059-e8b44b466976",
  "sourceToolAssistantUUID": "33b49d55-2f3c-4f44-805c-98501b071853",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/director_d3562b73",
  "sessionId": "824f3111-42c3-4ec6-b193-944b13769b09",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "wild-enchanting-sphinx"
}
```

</details>

---

### Assistant

_source line 5 · 2026-05-23T15:50:19.849Z_

Here is the complete contents of the Round 18 review report file:

---

**round**: 18
**review_mode**: fresh
**overall_score**: 3.5 - Borderline Conference
**timestamp**: 2026-05-23T15:44:43.616326+00:00
**reviewer_ids**: [1, 2]
**cross_response_reviewer_ids**: [1, 2]
**force_resubmit**: False

---

## 审稿报告：Round 18（Fresh Review）

**论文**: Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction
**Venue**: EMNLP 2026 (ARR Long Paper)
**审稿模式**: Fresh（重新审稿）
**Reviewer**: R1（方法严谨性）+ R2（新颖性/完整性）
**日期**: 2026-05-23

---

## Summary

The paper studies how multi-class annotation errors (K≥3) from LLM annotators propagate to downstream causal estimation across 7 typical DAG topologies. Core contributions include: (1) Deriving closed-form bias expressions for 7 topologies under non-differential misclassification assumption, establishing a sign-preservation/reversal dichotomy (5 topologies preserve sign, exposure and IV can reverse); (2) Defining Annotation Sensitivity Values (ASV) framework with three diagnostics (magnitude, significance, sign-flip), revealing a topology-dependent fragility spectrum from IV (most fragile) to M-bias (immune); (3) Proving FWL invariance makes matrix correction methods exactly ineffective (0% bias reduction) under four covariate topologies, evaluating 5 correction methods. Empirically validated via Monte Carlo simulation (161 scenarios, grand MAPE 1.6%) and 23 real LLM configurations (HumAID K=10, VAST K=3, CivilComments K=2).

---

## Strengths

**S1. Truly unified topology analysis**: First systematic comparison within a unified framework of how the same confusion matrix produces qualitatively different biases across 7 DAG topologies. The sign-preservation/reversal dichotomy is a clear and powerful core finding, bridging the gap between epidemiological measurement error theory and NLP practice.

**S2. FWL invariance negative result**: Proves matrix correction methods (confusion matrix inversion) have exactly 0% bias reduction under 4 covariate topologies—a clean, complete structural result with direct practical warnings for practitioners.

**S3. Honest cognitive hierarchy**: The three-level hierarchy Proved (K=2, Theorem 1) → Verified (K≥3, Observation 1) → Conjectured (Conjecture 1) is commendable in a theory paper, avoiding overclaiming of K≥3 results.

**S4. Comprehensive empirical validation**: 161 scenarios × 23 LLM configurations × 3 NLP tasks; 100,000 Dirichlet matrices; theory-MC MAPE 1.6% (per-topology 0.3%-3.7%). The finding that F₁ shows no significant correlation with causal bias (Spearman ρ = -0.10, p = 0.45) has direct operational value for CSS researchers.

**S5. Practical decision framework**: ASV analogy with E-values is well-designed; Algorithm 1's topology-aware correction decision tree provides practitioners with clear operational guidance.

---

## Weaknesses

### Must-Fix

**MF-1** [format] **Body page count exceeds EMNLP 2026 strict 8-page limit**
- Section 5 Conclusion is fully on page 9 (approximately 13-14 lines of main text overflow). EMNLP 2026's strict 8-page limit is a hard constraint; violation can lead to desk rejection.
- R2 first raised as critical; R1 cross-confirmed violation exists but recommended downgrade. **Director ruling: must-fix**—format compliance is a hard constraint with minimal fix cost (compress Section 4.5 + streamline Conclusion).
- Fix approach: (a) streamline Section 4.5 "Case studies and sensitivity" paragraph (details already in Appendix); (b) compress Conclusion to 5-6 lines; (c) or move one of Figure 4/5 to Appendix.

**MF-2** [soundness] **Non-differential misclassification assumption lacks direct empirical validation in LLM annotator context**
- Definition 1 requires P(A*=j|A=k,Y) = P(A*=j|A=k). LLM pretraining data encodes A-Y associations and may systematically violate this assumption. Current validation insufficient: Appendix B.5 VAST topic-stratified test on only one dataset, and topic stratification ≠ Y stratification; Appendix B.6/B.8 stress tests show ε=0.01 structured departure causes sign reversal in 14/16 K≥3 exposure configurations.
- R1 first raised as critical; R2 cross-validates AGREE (with stronger structural argument—LLM API doesn't observe Y—than R1 acknowledged). **Consensus: must-fix**.
- Fix approach: On at least one NLP dataset with gold labels, stratify LLM misclassification matrices by Y value and directly test P(A*|A,Y=0) ≈ P(A*|A,Y=1). Even testing just one dataset (like HumAID) provides empirical backing for structural argument.

### Should-Fix

**SF-1** [soundness, high priority] **K≥3 ASV monotonicity is only Conjecture, weakening Contribution 2's theoretical positioning**
- Theorem 1 (envelope monotonicity) only proved under K=2 + proportional effects. K≥3 depends on Observation 1 (numerical verification, ε<0.02) and Conjecture 1. Paper's core argument is that K≥3 introduces structural new phenomena, yet its ASV framework cannot provide formal guarantees for K≥3.
- R2 first raised as critical; R1 cross-validates AGREE with nuance (K≥3 contribution is multi-dimensional—bias expressions, sign preservation, FWL all hold for general K, not just monotonicity; ε<0.02 bounds ASV error within 2%). **Director ruling: should-fix (high priority)**—R1's argument is strong; K≥3 contributions genuinely extend beyond monotonicity.
- Fix approach: (a) Reframe Contribution 2 as "empirically validated diagnostic with proved K=2 foundation"; (b) supplement analysis of monotonicity failure consequences (if ε reaches extreme values, how much does it impact ASV ranking).

**SF-2** [soundness, high priority] **Proportional effects assumption (f=λg) lacks specific discussion in NLP context**
- Theorem 1 depends on f=λg. In multi-class NLP processing (e.g., stance detection with favor/against/neutral), different classes may have qualitatively different effects, violating proportionality. Paper mentions only one sentence: "plausible in NLP tasks with a single quality dimension".
- R1 first raised as critical; R2 REBUTS downgrade to should-fix (assumption only affects Theorem 1 monotonicity; Proposition 3 provides general case fallback; 97.3% empirical compliance rate). **Director adopts should-fix (high priority)**—R2's argument is persuasive; assumption scope is narrower than R1 described.
- Fix approach: Add 2-3 sentences analyzing specific NLP causal inference scenarios (e.g., whether 3-class stance detection approximates proportionality).

**SF-3** [scope] **Logistic regression discussion insufficient**
- Logistic regression most commonly used in NLP. Main text mentions FWL invariance breakdown under logistic only in one sentence (Section 4.5). Appendix B.14 shows FWL breakdown magnitude increases with accuracy (exposure: -22% to -78%). Algorithm 1 doesn't distinguish OLS/logistic paths.
- R1 first raised; R2 strongly agrees. **Consensus: should-fix**.
- Fix approach: Add 1-2 paragraphs in Section 4.5 guiding logistic regression, citing Appendix B.2/B.7/B.14; add OLS/logistic branch to Algorithm 1.

**SF-4** [presentation, high priority] **Terminology barrier limits accessibility for NLP readers**
- plim, FWL theorem, Wald estimator, column-stochastic matrix, Birkhoff polytope, Dirichlet prior—high-barrier terminology for EMNLP audience; intuitive explanations insufficient. If most reviewers cannot fluently understand Method section, it will impact soundness and confidence scores.
- R2 first raised; R1 cross-validates AGREE. **Consensus: should-fix**.
- Fix approach: Add 1-2 sentences of intuitive explanation at first use of each key term (adds ~6-8 lines; space available after page compression).

**SF-5** [presentation] **Contribution 3 (correction guidance) main text depth mismatched with "contribution" positioning**
- "Topology-aware correction guidance" listed as one of three major contributions, but main text only ~0.7 pages. Algorithm 1 only in Appendix. Lacks depth compared to Contribution 1 (~3 pages method) and Contribution 2 (~1.5 pages ASV + experiments).
- R2 first raised; R1 cross-validates AGREE (inclines to downgrade as practical implication). **Consensus: should-fix**.
- Fix approach: (a) Promote Algorithm 1 to main text (requires combining with MF-1 compression strategy); or (b) downgrade to "practical implication" rather than co-equal contribution.

**SF-6** [novelty] **ASV vs E-value comparison framework misleading**
- Remark 1's three "structural distinctions from E-values" essentially amounts to different tools solving different problems (annotation error vs unmeasured confounding). Current phrasing implies ASV is an improvement over E-values. ASV's true contribution is adapting the sensitivity analysis paradigm to annotation error + topology dependence.
- R2 first raised; R1 cross-validates AGREE with nuance (distinctions accurate but phrasing implies improvements over). **Consensus: should-fix**.
- Fix approach: Reframe Remark 1 as complementary tools (complementary tools for different bias sources).

**SF-7** [experiments] **Dirichlet(1,1,...,1) sampling insufficiently representative for high-dimensional K**
- For K=5 (20 parameters) and K=7 (42 parameters), uniform Dirichlet sampling deviates from actual LLM matrix distribution (diagonal expectation 1/K vs actual >0.6). R2 adds: 23 empirical LLM matrices already validate core conclusions; representativeness issue doesn't affect final conclusions.
- R1 first raised; R2 cross-validates AGREE. **Consensus: should-fix (low priority)**.
- Fix approach: Supplement Dirichlet(α,1,...,1) (α>>1) sampling verification, or report ε values for diagonal >0.6 subspace.

**SF-8** [method] **Significance ASV's N-dependence insufficiently explored**
- δ_sig depends on N through SE(N); Figure 3 shows only single N value. Changes in significance ASV across different N values is critical decision information for practitioners.
- R1 first raised; R2 cross-validates AGREE. **Consensus: should-fix**.
- Fix approach: Add visualization (Figure or Table) of δ*_sig changes across topologies at different N values (e.g., 1K, 5K, 10K, 50K).

**SF-9** [soundness] **Conjecture 1's ε<0.02 constraint lacks theoretical intuition**
- ε constraint entirely from numerical experiments; paper doesn't explain why ε should be small. R2 supplements possible intuition: under proportional effects exact monotonicity; deviations from non-proportional residuals.
- R1 first raised; R2 cross-validates AGREE. **Consensus: should-fix**.
- Fix approach: Supplement 1 paragraph on intuition for small ε (e.g., relation to convex body structure of column-stochastic matrix space or proportional residual analysis).

### Minor

1. **Abstract information density too high**: ~184 words comply with ≤200 limit, but 7+ specific numbers difficult to digest on first read. Recommend simplifying to 2-3 most impactful numbers.
2. **Figure 2 grayscale printability**: Red sign-reversal markers difficult to distinguish in grayscale; recommend hatching/pattern fill.
3. **τ symbol overloading**: τ has different meanings across topologies but insufficiently annotated.
4. **Orphan bib entries**: manski1990 not cited in main text; should remove or add citation.
5. **Reference formatting inconsistency**: Some bib entries lack doi or page numbers.
6. **"First unified analysis" phrasing**: Too many qualifiers; suggest simplifying to "first systematic topology-specific comparison".

---

## Reviewer Consensus

Consensus on the following issues ([AGREE] or cross-validated without dispute):

1. **Non-differential misclassification assumption needs Y-stratified empirical test** [must-fix] — R1 first raised, R2 AGREE
2. **Page limit violation needs fixing** [must-fix (R2) / should-fix (R1)] — violation undisputed; only severity differs
3. **Logistic regression discussion insufficient** [should-fix] — R1 first raised, R2 strongly agrees
4. **NLP terminology barrier** [should-fix] — R2 first raised, R1 AGREE
5. **Contribution 3 depth insufficient** [should-fix] — R2 first raised, R1 AGREE
6. **ASV vs E-value framework reframing** [should-fix] — R2 first raised, R1 AGREE with nuance
7. **Figure 2 grayscale printability** [minor] — R2 first raised, R1 AGREE
8. **Significance ASV N-dependence** [should-fix] — R1 first raised, R2 AGREE
9. **Conjecture 1 ε theoretical intuition** [should-fix] — R1 first raised, R2 AGREE

---

## Reviewer Divergence

Severity classification divergences (**Director already ruled**):

| Issue | R1 Assessment | R2 Assessment | Director Ruling | Rationale |
|------|---------|---------|---------------|------|
| Proportional effects f=λg assumption argumentation | critical | should-fix (REBUT) | **should-fix (high priority)** | R2 argument persuasive: assumption only affects Theorem 1 monotonicity; Proposition 3 provides fallback; 97.3% empirical compliance rate |
| Page limit violation | should-fix (M5) | must-fix (N1) | **must-fix** | Format compliance is hard constraint; fix cost minimal |
| K≥3 monotonicity theory gap | strong should-fix | must-fix (N2) | **should-fix (high priority)** | K≥3 contributions multi-dimensional (bias expressions + sign preservation + FWL); shouldn't judge solely on monotonicity gap |

---

## Questions

Summary of key questions from both Reviewers (for author response):

1. **In ClinicalBERT case study, was f=λg tested?** Are effects across different smoking status classes approximately proportional? [R1-Q1]
2. **What common characteristics among the 2.7% of LLM configurations not satisfying Theorem 1 conditions?** Related to specific LLM or dataset? [R1-Q3]
3. **Practical use cycle for sign-flip ASV**: Practitioners need to know true τ sign beforehand to compute sign-flip ASV; how to handle this bootstrap loop? [R2-Q3]
4. **How does logistic regression FWL breakdown magnitude change with large K?** Table 5 only tests K=3. [R1-Q4]
5. **Possibility of multi-dimensional ASV**: Current approach searches single C(δ) path; considered per-category sensitivity? [R1-Q5]
6. **Meaning of non-differential assumption stress test**: ε=0.01 causes sign reversal in 14/16 K≥3 exposure configurations; does this mean analysis extremely fragile to differential misclassification? [R2-Q4]

---

## Missing References

- **Imai and Yamamoto (2010)**, "Causal Inference with Differential Measurement Error" — contrasts with non-differential assumption [R1 recommendation, R2 AGREE]
- **Nguimkeu, Denteh & Tchernis (2019)**, "On the estimation of treatment effects with endogenous misreporting" — treatment misclassification related [R2 recommendation]
- **Ogburn and VanderWeele (2013)** — bias amplification under covariate misclassification follow-up [R1 recommendation, R2 notes 2012 version already cited]

---

## External Review (Stanford Agentic Reviewer)

**Status**: Not requested. Project not configured for external review.

---

## Visual Layout Check

**Status**: error — Visual review Agent incomplete due to rate limit ("You've hit your limit · resets 4pm (UTC)"). User can re-trigger after limit reset.

---

## Overall Assessment

**Overall Score: 3.5 / 5 — Borderline Conference**

| Dimension | R1 | R2 | Combined |
|------|----|----|------|
| Soundness | 3.5 | 3.5 | 3.5 |
| Excitement | 3.5 | 3.5 | 3.5 |
| Reproducibility | 4.0 | 4.0 | 4.0 |
| Confidence | 4 | 4 | 4 |

**Summary Assessment**:

The paper is the first to systematically analyze multi-class annotation error causal bias propagation across 7 DAG topologies in a unified framework. Contributions are genuine (bias taxonomy + FWL invariance negative result), validation thorough (161 scenarios, 1.6% MAPE), cognitive hierarchy honest. FWL invariance proof and finding that F₁ shows no correlation with causal bias have direct practitioner value.

Main factors constraining the score:

1. **Must-fix blocking issues**: (a) Page limit overrun needs compression (minimal fix cost); (b) Non-differential misclassification assumption lacks Y-stratified empirical test (requires experimental work, but feasible on HumAID).

2. **Theory-application gap**: Core theoretical guarantee (Theorem 1 monotonicity) only holds for K=2 + proportional effects, yet paper's core selling point is K≥3 structural novelty. While bias expressions and FWL invariance hold for general K (independent of Theorem 1), ASV framework's K≥3 guarantee remains conjectural. Contribution 2 needs more cautious positioning.

3. **Audience fit**: Paper for EMNLP uses extensive econometric terminology (plim, FWL, Wald estimator); NLP reader accessibility limited. Correction guidance (Contribution 3) positioned as core contribution but main text depth mismatched. Terminology barrier affects soundness and confidence scoring.

**Conditional upgrade path**: If authors adequately respond to MF-2 (Y-stratified test), SF-1 (Contribution 2 reframing), and SF-4 (terminology intuition), score could upgrade to **4.0 (Conference)**. MF-1 (page limit) is pure formatting fix, doesn't affect academic evaluation.

---

## Detailed Comments

### Section-by-Section

**Abstract**: 184 words comply with ≤200 limit (R17 verified). Information density high but main conclusions complete. Recommend reducing specific numbers (retain 83.4% sign reversal and 1.6% MAPE as core numbers). FWL invariance claim should add "under linear OLS" qualifier.

**Introduction**: Three contributions clearly listed. "First unified analysis" claim valid within current literature scope (R1 confirms), but too many qualifiers; suggest simplifying phrasing. Contribution 3 main text depth needs matching with positioning.

**Related Work**: Coverage comprehensive; four key areas (measurement error, LLM annotation, sensitivity analysis, correction methods) well-cited. Consider supplementing Imai & Yamamoto (2010) and Nguimkeu et al. (2019).

**Method (Section 3)**: Where core theoretical contribution resides. Bias expressions (formulas 1-5) clearly derived. Theorem 1 → Observation 1 → Conjecture 1 hierarchy honest. Main issues: (1) terminology barrier (plim, FWL, Wald need intuitive explanation); (2) proportional effects assumption lacks NLP scenario discussion; (3) Remark 1 ASV-E-value comparison needs reframing as complementary tools.

**Experiments (Section 4)**: Thorough validation (161 scenarios, 1.6% MAPE). Empirical validation uses 3 real NLP datasets and 23 LLM configurations. Strong finding: F₁ cannot predict causal bias. Main issues: (1) Correction guidance (Section 4.5) insufficient depth; (2) logistic regression discussion inadequate; (3) Significance ASV N-dependence needs more systematic presentation.

**Conclusion + Limitations**: Conclusion needs compression (currently causes page overrun). Limitations cover three points (non-differential assumption, linear SEM, C estimability); positioning correct (main text).

**Appendix**: 24 pages, B.1-B.24 totaling 24 subsections with thorough validation. FWL proof (B.2) complete. Logistic regression validation (B.7, B.14) exists but insufficiently referenced in main text. Dense cross-referencing but clear structure.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dd19c11d-06e5-4d35-b059-e8b44b466976",
  "isSidechain": true,
  "agentId": "a807f85b91f7d7f07",
  "requestId": "req_011CbKmJUNwPp7i1NF2Z1HDi",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "4c4175a1-7490-4778-ab47-d8769a0882d3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/director_d3562b73",
  "sessionId": "824f3111-42c3-4ec6-b193-944b13769b09",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "wild-enchanting-sphinx",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01L91D7jRHHz5d1GnADp3gMs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 8571,
      "cache_read_input_tokens": 37233,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8571,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---
