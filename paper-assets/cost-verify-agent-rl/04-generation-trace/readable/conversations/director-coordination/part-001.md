# Director coordination — Part 1 of 3

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Conversation logs

[Transcript overview](../director-coordination.md) · [Part 2 →](part-002.md) · [Structured JSON](../../../sessions/6c/6ce03c48b9fdbb7a447a.json)

## Round 1

## Round 1

26 recorded events


### User

_source line 1 · 2026-05-17T00:30:17.651028+00:00_

[Reviewer 2 审稿意见]:
## 总体评分
**Overall**: 4/10 (Reject)
**一句话总结**: 核心贡献是对已知 RL 原理在特定框架中的应用修正，新颖性不足以支撑顶会独立论文；相关工作严重欠缺，story 存在多处自相矛盾。

## 官方维度打分（NeurIPS/ICML 标准）
| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Novelty | 2/4 | 核心洞察是教科书级 RL 知识在特定实现中的 rediscovery |
| Soundness | 2/4 | 方法本身 sound，但 claim 与证据不匹配 |
| Significance | 2/4 | 对 RAGEN 用户有实用价值，但 scope 过窄 |
| Clarity | 3/4 | 论证逻辑清晰，但 positioning 有误导性 |

## Must-Fix 问题（影响接收决定）

**N1** [critical] 核心新颖性不足：episode-level reward 是传统 RL 的 default，非 contribution
- 具体位置：§3 Method, Contribution (1) "identify credit assignment decay"
- 问题：γ^(T-h) → 0 当 T 大时奖励信号衰减，这是 Sutton & Barto (2018) [10] 第 13 章 eligibility traces 的基础内容。论文自己引用了这本教科书，却将教科书内容包装为"识别了根本失败模式"。在传统 RL 中，episode-level return（即 REINFORCE）一直是 default 做法，不使用 per-step discounting 来处理 sparse terminal reward 是标准实践。本文的实际贡献是：**发现 RAGEN 框架的默认配置在 multi-turn 场景下有 bug-like behavior**，并通过使用 episode-level aggregation 修复。这更接近一个 technical report 或 workshop paper 级别的贡献，而非顶会的方法论创新。
- 为什么影响接收：如果核心 contribution 是将已知原理应用到特定框架，审稿人会质疑 intellectual novelty。论文需要论证为什么这个"已知问题"在 LLM agent RL 这个新 context 下有 non-trivial 的新洞察。
- 建议修改方向：(a) 深入分析为什么 LLM agent 社区默认采用了 step-independent training（是框架设计问题？是对 chat-level RL 的错误类比？），提供 community-level 的 root cause analysis；(b) 提出超越简单 episode-level aggregation 的方法（如 adaptive discounting, learned credit assignment）来增加方法贡献。

**N2** [critical] 相关工作严重不足：10 篇引用无法支撑顶会论文
- 具体位置：§2 Related Work, References 列表
- 问题：顶会论文通常有 30-50+ 引用。10 篇引用意味着文献调研严重不充分。关键缺失包括：
  - **基础 RL 算法**：未引用 PPO (Schulman et al. 2017)、REINFORCE (Williams 1992)、A2C/A3C——这些是 GRPO 的对比基础
  - **GAE** (Schulman et al. 2015)：本文核心问题是 credit assignment，GAE 是该领域最直接相关的方法，完全未提及
  - **HER** (Andrychowicz et al. 2017)：§2 提到 hindsight experience replay 但未给出具体引用
  - **AgentQ**：正文提到名字但无引用条目
  - **Multi-turn LLM agent training**：WebAgent (Gur et al. 2023), AgentTuning (Zeng et al. 2023), FireAct (Chen et al. 2023), Reflexion (Shinn et al. 2023) 等重要工作未引用
  - **GRPO 原始论文**：DeepSeekMath [8] 可能不是 GRPO 的首次提出，需要确认引用链
  - **Reward shaping / potential-based shaping** (Ng et al. 1999)：与 credit assignment 直接相关
- 为什么影响接收：审稿人会认为作者对领域了解不够深入，无法判断贡献的真实增量。特别是缺少 GAE 引用是致命的——GAE 本身就是解决 credit assignment 和 variance 的标准方法，论文需要解释为什么不直接用 GAE。
- 建议修改方向：系统补充上述引用，并在 §2 中增加至少两个 subsection：(a) "Credit Assignment in RL" 覆盖 GAE/eligibility traces/reward shaping；(b) "LLM Agent Training" 覆盖 WebAgent/AgentTuning/FireAct/Reflexion 等。

**N3** [critical] 与 Self-Guide 的对比逻辑自相矛盾
- 具体位置：§2 (Self-Guide 72.7%), §5 Discussion ("model capacity is separate bottleneck")
- 问题：Self-Guide 使用 Qwen-1.7B 在 ALFWorld 上达到 72.7%，而本文 episode-level GRPO 用同样模型只达到 24.3%。论文在 Discussion 中用 "model capacity as separate bottleneck" 来解释低性能，但这个论点被 Self-Guide 的存在直接反驳——**同样大小的模型在同样的环境上可以达到 3 倍的性能**。这说明：
  - 要么本文方法不如 Self-Guide 有效（positioning 问题）
  - 要么两者解决不同子问题，需要明确说明差异（如 Self-Guide 可能用了不同的 training data/episodes/curriculum）
  - 要么 model capacity 论点不成立
  无论哪种情况，当前论文的 framing 都有问题。
- 为什么影响接收：审稿人会直接质疑：如果同模型已有 72.7% 的方法，为什么我要关注一个 24.3% 的方法？论文必须回答这个问题。
- 建议修改方向：(a) 详细分析 Self-Guide 和本文方法的本质区别（training paradigm? data requirement? supervision signal?）；(b) 如果 Self-Guide 需要额外监督/数据，明确说明本文方法的 advantage 在于更低的监督需求；(c) 考虑在 Self-Guide 的 training pipeline 中加入 episode-level GRPO 作为 complementary experiment。

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] Claim overclaiming："eliminates this bottleneck" vs 25% success
- 具体位置：§1 Introduction
- 问题：Introduction claim "episode-level GRPO eliminates this bottleneck"，但 24.3% success rate 表明 75% 的情况下 agent 仍然失败。"Eliminates" 暗示问题被解决，实际上只是从 0% → 25%。更准确的表述应该是 "addresses" 或 "mitigates"。此外，如果 bottleneck 被 "eliminated"，那 75% 失败的原因是什么？论文需要明确区分 credit assignment bottleneck 和其他 bottlenecks（exploration, model capacity, task complexity）。
- 建议：将 "eliminates" 改为 "mitigates" 或 "addresses"；增加对剩余 failure modes 的分析。

**W2** [warning] Contribution (1) 与 Contribution (3) 存在冗余/循环论证
- 具体位置：§1 Contributions list
- 问题：Contribution (1) 是 "identify credit assignment decay"，Contribution (3) 是 "h-sweep with cliff at h=5"。但 h-sweep 本身就是 credit assignment decay 的实验验证——当 h 小于某阈值时，γ^(T-h) 衰减到 0。这两个 contribution 本质上是同一个发现的理论表述和实验验证，不应计为两个独立贡献。
- 建议：合并为一个 contribution "We identify and empirically characterize credit assignment decay, showing a sharp performance cliff at h<5"。

**W3** [warning] Future directions 暴露当前工作的 stepping-stone 定位
- 具体位置：§5 Discussion, future directions
- 问题：提到 "selective verification 需要 >40% base agent"，暗示当前工作是为后续研究铺路。顶会论文应该是 self-contained 的 contribution。如果作者自己都认为这是一个 stepping stone，审稿人会问：为什么不等到有更完整的 story 再投稿？
- 建议：重新 frame future directions，强调当前工作的独立价值（如 training methodology insight 对社区的直接贡献），而非暗示"真正的贡献在下一篇论文"。

**W4** [warning] 论文叙事转型痕迹可能残留
- 具体位置：全文（基于 review_context.yaml 信息）
- 问题：论文从 "selective verification" 转型为 "pure training methodology"，需要确认：(a) Abstract/Introduction 是否还有 verification 相关的 framing 残留；(b) 实验设计是否有为 verification 准备但对当前 story 不必要的内容；(c) future directions 中提到 selective verification 是否过于突兀（读者没有前文铺垫）。
- 建议：全文审查是否有叙事不一致的痕迹。

## 小问题（不影响接收）
- AgentQ 在正文中被提及但 References 中无对应条目，属于引用错误
- §2 提到 "HER" 但未引 Andrychowicz et al. 2017 原始论文

## 主要优势
- 问题定义清晰：step-independent training 在 long-horizon 任务中失败的现象被清楚展示
- 实验设计系统：h-sweep 提供了 controlled comparison，multi-seed 提供了统计可靠性
- 实用价值：对使用 RAGEN/GRPO 训练 multi-turn agent 的研究者有直接指导意义
- 跨环境和跨规模验证增强了发现的普适性

## 总结判断

本文的核心问题在于 **novelty bar**：将教科书级的 RL 知识（episode-level return 优于 step-level discounted reward for sparse terminal reward）应用到一个特定框架（RAGEN + GRPO）中，虽然有实用价值，但不构成顶会级别的方法论贡献。相关工作的严重欠缺（10 引用，缺少 GAE/PPO/REINFORCE/HER 等核心引用）进一步削弱了论文的学术 rigor。与 Self-Guide (72.7%) 的性能差距未被充分解释，使得论文的 positioning 存在根本性漏洞。

建议：(a) 大幅扩充 related work；(b) 增加与 Self-Guide 的深度对比分析；(c) 考虑将论文 reposition 为 empirical study/analysis paper 而非 method paper；(d) 或者在方法层面增加超越简单 episode-level aggregation 的贡献（如 learned credit assignment, adaptive horizon）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 2 · 2026-05-17T00:30:35.106806+00:00_

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
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 3 · 2026-05-17T00:30:36.424855+00:00_

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
…[truncated 2458 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "Read",
  "elapsed_ms": 1318
}
```

</details>

---


### Tool call

_source line 4 · 2026-05-17T00:30:36.575733+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__get_external_review_status",
  "max_results": "6"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__get_external_review_status",
    "max_results": "6"
  }
}
```

</details>

---


### Tool result

_source line 5 · 2026-05-17T00:30:36.626266+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 6 · 2026-05-17T00:30:42.902790+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "cost-verify-agent-rl"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "cost-verify-agent-rl"
  }
}
```

</details>

---


### Tool call

_source line 7 · 2026-05-17T00:30:43.104642+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "cost-verify-agent-rl"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "cost-verify-agent-rl"
  }
}
```

</details>

---


### Tool result

_source line 8 · 2026-05-17T00:30:43.155481+00:00_

{"result":"# 项目 cost-verify-agent-rl 概况\n\n## 实验状态 (56 个)\n\n- **exp009**: DONE (failed) — \n- **exp008_sft**: DONE (success) — \n- **exp008**: PREPARING (killed) — \n- **exp007**: DONE (failed) — \n- **exp007_dryrun**: PREPARING — \n- **exp003**: DONE (failed) — \n- **exp005**: PREPARING — \n- **exp_003**: PREPARING (failed) — \n- **exp_003_dryrun**: PREPARING (failed) — \n- **exp_003_dryrun2**: PREPARING (failed) — \n- **exp003_dryrun3**: PREPARING (failed) — \n- **exp_003_dryrun3**: PREPARING (failed) — \n- **exp_002**: DONE (failed) — \n- **exp_001b**: DONE (failed) — \n- **exp_001**: DONE (failed) — \n\n## 最新报告\n&lt;!-- AUTO-FACTS-BEGIN (generated 2026-05-16T19:20:34Z; do not edit — regenerated by auto_build_report_facts) -->\n## 📊 当前状态（auto-derived from registry）\n\n**总计**: 54 个实验 — DONE 36, PENDING 1, PREPARING 17\n**DONE 分布**: failed 19, killed 9, negative 5, success 3\n\n### GPU 占用\n- **分配**: 2 张 — bjb1-17606:cuda:0, bjb1-17606:cuda:1\n- **空闲（分配了没跑）**: bjb1-17606:cuda:0, bjb1-17606:cuda:1\n\n### 🏃 RUNNING\n_（无）_\n\n### 📌 最近完成 (top 5)\n- `exp029_episode_level` [failed] — 2026-05-16T19:20:33 — process dead 5× with no sentinel/W&B — auto-resolved as failed\n- `exp028c_selfguide_recipe` [failed] — 2026-05-16T08:29:53 — process dead 5× with no sentinel/W&B — auto-resolved as failed\n- `exp028a_recipe_fix` [killed] — 2026-05-15T21:25:46\n- `exp028_prereq_zeroshot` [negative] — 2026-05-15T21:11:42\n- `exp027_stable_grpo` [failed] — 2026-05-15T20:44:26 — EXIT_CODE=1 (generic error — check log tail)\n\n### 🔴 最近失败原因 (top 3)\n- `exp029_episode_level`: process dead 5× with no sentinel/W&B — auto-resolved as failed\n- `exp028c_selfguide_recipe`: process dead 5× with no sentinel/W&B — auto-resolved as failed\n- `exp028a_recipe_fix`: _(no failure_reason — pre-2026-04-24 entry)_\n\n&lt;!-- AUTO-FACTS-END -->\n\n---\n\n# Handover — 2026-05-16\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- exp025c（等待人工审批）\n- exp028_prereq_zeroshot_instruct: Qwen3-1.7B-Instruct 零
…[truncated 1674 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 252
}
```

</details>

---


### Tool result

_source line 9 · 2026-05-17T00:30:43.156226+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 10 · 2026-05-17T00:30:50.786835+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review_reports/round_*.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review_reports/round_*.md",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts"
  }
}
```

</details>

---


### Tool result

_source line 11 · 2026-05-17T00:30:51.037846+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "Glob",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 12 · 2026-05-17T00:30:51.038335+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review_issues.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review_issues.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts"
  }
}
```

</details>

---


### Tool result

_source line 13 · 2026-05-17T00:30:51.088769+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 14 · 2026-05-17T00:31:05.809527+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*review*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*review*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl"
  }
}
```

</details>

---


### Tool result

_source line 15 · 2026-05-17T00:31:06.060753+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/logs/chats/feishu_group_oc_733b284b383121720ce3d07c5c4a6bb2_reviewer.lock
/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/logs/chats/archive/feishu_group_oc_733b284b383121720ce3d07c5c4a6bb2_reviewer_20260513T214302_465362.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/logs/chats/archive/feishu_group_oc_733b284b383121720ce3d07c5c4a6bb2_reviewer_20260514T031709_659468.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/logs/chats/archive/feishu_group_oc_733b284b383121720ce3d07c5c4a6bb2_reviewer_20260514T081231_258347.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/logs/chats/archive/feishu_group_oc_733b284b383121720ce3d07c5c4a6bb2_reviewer_20260514T125735_537907.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/logs/chats/archive/feishu_group_oc_733b284b383121720ce3d07c5c4a6bb2_reviewer_20260515T005452_642144.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/logs/chats/archive/feishu_group_oc_733b284b383121720ce3d07c5c4a6bb2_reviewer_20260515T051902_073757.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/logs/chats/archive/feishu_group_oc_733b284b383121720ce3d07c5c4a6bb2_reviewer_20260515T103817_691881.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/logs/chats/archive/feishu_group_oc_733b284b383121720ce3d07c5c4a6bb2_reviewer_20260515T152603_752711.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/logs/chats/archive/feishu_group_oc_733b284b383121720ce3d07c5c4a6bb2_reviewer_20260515T201746_036071.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/logs/chats/archive/feishu_group_oc_733b284b383121720ce3d07c5c4a6bb2_reviewer_20260516T023103_172535.jsonl
/home/ub
…[truncated 2529 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "Glob",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 16 · 2026-05-17T00:31:06.061241+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review_context*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review_context*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl"
  }
}
```

</details>

---


### Tool result

_source line 17 · 2026-05-17T00:31:06.111734+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/dream_reports/dream_20260516T235255/best/review_context.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/dream_reports/dream_20260516T235255/median/review_context.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/dream_reports/dream_20260516T235255/worst/review_context.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 18 · 2026-05-17T00:31:12.488990+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/logs/chats/feishu_group_oc_648eaf83d2b24d445764257cf6a55525_reviewer_1.jsonl",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/logs/chats/feishu_group_oc_648eaf83d2b24d445764257cf6a55525_reviewer_1.jsonl",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 19 · 2026-05-17T00:31:12.991251+00:00_

1	{"ts": "2026-05-17T00:27:54.689565+00:00", "role": "user", "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:reviewer_1", "text": "[Round 1 审稿请求]:\n[Dream 审稿任务 — Reviewer 1：方法 + 实验]\n\n论文标题：Episode-Level RL for Multi-Turn Agents: Why Step-Independent Training Fails and How to Fix It\n\n论文摘要：本文识别了 step-independent reward assignment 在 multi-turn agent RL 训练中的根本失败模式——credit assignment decay（γ^(T-h) → 0），提出 episode-level GRPO 作为解决方案。在 ALFWorld 和 ScienceWorld 上用 Qwen3-1.7B 实验，episode-level 训练达到 24.3%±6.0% success vs step-independent 的 0%。h-sweep 揭示 h<5 时存在 sharp cliff。优势泛化到 ScienceWorld (15% vs 2%) 和 Qwen3-7B (38% vs 5%)。\n\n论文结构概览（8页）：\n- §1 Introduction：识别 credit assignment decay 问题，提出 episode-level GRPO\n- §2 Related Work：RL for LM agents、multi-turn frameworks、credit assignment in RL、adaptive computation\n- §3 Method：问题公式化（Eq.1 gradient signal decay）、credit assignment decay analysis（Eq.2）、episode-level GRPO（Eq.3）\n- §4 Experiments：\n  - 4.1 Setup：ALFWorld (T=48)、ScienceWorld (T=35)、Qwen3-1.7B/7B、GRPO with KL=0.01, G=8, lr=5e-6\n  - 4.2 Context Window Sweep (Table 1)：h∈{1,2,3,5,8,10,15,20,full}，h≤2 collapse，h<5 sharp cliff\n  - 4.3 Multi-Seed (Table 2)：3 seeds，24.3%±6.0%\n  - 4.4 Credit Assignment Mechanism (Table 3)：γ^(T-h) vs observed success correlation\n  - 4.5 Verification Value (Table 4)：episode-level+verify 25%, no-verify 15%, step-indep+verify 0%\n  - 4.6 Cross-Environment (Table 5)：ALFWorld 25/0, ScienceWorld 15/2\n  - 4.7 Model Scale (Table 6)：1.7B 25/0, 7B 38/5\n  - 4.8 Per-Task Breakdown (Table 7)：6 task types, r=-0.42 correlation with episode length\n- §5 Discussion：relationship to RAGEN, model capacity bottleneck, practical guidance, limitations, future work\n- §6 Conclusion\n- References：10 entries\n\n实验设计参考（review_context.yaml 中的完整实验列表）：\n共 16 个 imagined experiments：\n1. h-sweep (plan_002) — 已在 Table 1 报告\n2. Multi-seed 3 seeds (plan_003) — 已在 Table 2 报告\n3. Credit assignment mechanism analysis (plan_004) — 已在 Table 3 报告\n4. Action-change s
…[truncated 18456 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 20 · 2026-05-17T00:31:13.142118+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/logs/chats/feishu_group_oc_648eaf83d2b24d445764257cf6a55525_reviewer_2.jsonl",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/logs/chats/feishu_group_oc_648eaf83d2b24d445764257cf6a55525_reviewer_2.jsonl",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 21 · 2026-05-17T00:31:13.142842+00:00_

1	{"ts": "2026-05-17T00:28:21.217901+00:00", "role": "user", "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:reviewer_2", "text": "[Round 1 审稿请求]:\n[Dream 审稿任务 — Reviewer 2：新颖性 + 相关工作]\n\n论文标题：Episode-Level RL for Multi-Turn Agents: Why Step-Independent Training Fails and How to Fix It\n\n论文摘要：本文识别了 step-independent reward assignment 在 multi-turn agent RL 训练中的根本失败模式——credit assignment decay（γ^(T-h) → 0），提出 episode-level GRPO 作为解决方案。在 ALFWorld 和 ScienceWorld 上用 Qwen3-1.7B 实验，episode-level 训练达到 24.3%±6.0% success vs step-independent 的 0%。h-sweep 揭示 h<5 时存在 sharp cliff。优势泛化到 ScienceWorld (15% vs 2%) 和 Qwen3-7B (38% vs 5%)。\n\n论文结构概览（8页）：\n- §1 Introduction：4 contributions listed — (1) identify credit assignment decay, (2) episode-level GRPO achieves 24.3%, (3) h-sweep with cliff at h=5, (4) cross-env and cross-scale validation\n- §2 Related Work：4 paragraphs covering RL for LM agents (RAGEN, AgentQ), multi-turn frameworks (Self-Guide 72.7%, ReflAct, ARES), credit assignment in RL (TD, eligibility traces, HER), adaptive computation (Thinkless)\n- §3 Method：problem formulation, credit assignment decay analysis (γ^(T-h)), episode-level GRPO (Eq.3)\n- §4 Experiments：7 tables covering h-sweep, multi-seed, mechanism analysis, verification ablation, cross-env, model scale, per-task breakdown\n- §5 Discussion：relationship to RAGEN, model capacity as separate bottleneck, practical guidance, limitations, future directions\n- §6 Conclusion\n- References：10 entries total — [1] RAGEN 2025, [2] Self-Guide 2026, [3] ARES 2026, [4] Thinkless NeurIPS 2025, [5] ReflAct EMNLP 2025, [6] ALFWorld ICLR 2021, [7] ScienceWorld EMNLP 2022, [8] DeepSeekMath 2024, [9] Qwen 2024, [10] Sutton & Barto 2018\n\n实验设计参考（review_context.yaml）：\n论文原本计划 16 个实验，但最终放弃了 selective verification 方向的多个实验（plan_005 到 plan_013 中大部分），因为统计结果不支持。论文叙事从 \"selective verification\" 转型为 \"pure training methodology\"。\n\n你的审查侧重：\n- **新颖性**：与现有工作的差异化是否清晰、贡献点是否独立成立\n- **相关工作**：文献覆盖是否充分、重要 baseline 是否漏引、定位是否准确\n- *
…[truncated 9019 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 22 · 2026-05-17T00:31:23.689187+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/logs/chats/feishu_group_oc_648eaf83d2b24d445764257cf6a55525_reviewer_1.jsonl",
  "offset": "20",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/logs/chats/feishu_group_oc_648eaf83d2b24d445764257cf6a55525_reviewer_1.jsonl",
    "offset": "20",
    "limit": "80"
  }
}
```

</details>

---


### Tool result

_source line 23 · 2026-05-17T00:31:23.689531+00:00_

&lt;system-reminder>Warning: the file exists but is shorter than the provided offset (20). The file has 20 lines.&lt;/system-reminder>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 24 · 2026-05-17T00:32:28.895317+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "[Round 1 审稿请求 - 重新触发]\n\nReviewer 1，你的上一个 session 在 venue 调研阶段中断，未提交审稿意见。请立即完成审稿。\n\n论文标题：Episode-Level RL for Multi-Turn Agents: Why Step-Independent Training Fails and How to Fix It\n\n论文摘要：本文识别了 step-independent reward assignment 在 multi-turn agent RL 训练中的根本失败模式——credit assignment decay（γ^(T-h) → 0），提出 episode-level GRPO 作为解决方案。在 ALFWorld 和 ScienceWorld 上用 Qwen3-1.7B 实验，episode-level 训练达到 24.3%±6.0% success vs step-independent 的 0%。h-sweep 揭示 h<5 时存在 sharp cliff。优势泛化到 ScienceWorld (15% vs 2%) 和 Qwen3-7B (38% vs 5%)。\n\n论文结构（8页）：\n- §1 Introduction：4 contributions — (1) identify credit assignment decay, (2) episode-level GRPO 24.3%, (3) h-sweep cliff at h=5, (4) cross-env/scale validation\n- §2 Related Work：4 paragraphs, 10 references total\n- §3 Method：problem formulation, credit assignment decay (γ^(T-h)), episode-level GRPO (Eq.3)\n- §4 Experiments：7 tables — h-sweep, multi-seed, mechanism analysis, verification ablation, cross-env, model scale, per-task breakdown\n- §5 Discussion：RAGEN relationship, model capacity bottleneck, limitations, future directions\n- §6 Conclusion\n- References：[1] RAGEN 2025, [2] Self-Guide 2026, [3] ARES 2026, [4] Thinkless NeurIPS 2025, [5] ReflAct EMNLP 2025, [6] ALFWorld ICLR 2021, [7] ScienceWorld EMNLP 2022, [8] DeepSeekMath 2024, [9] Qwen 2024, [10] Sutton & Barto 2018\n\n实验补充信息（review_context.yaml）：\n论文原计划 16 个实验，最终放弃 selective verification 方向（结果 negative/inconclusive），转型为 pure training methodology 论文。未报告的实验包括：\n- B-IAVR selective verification（success 从 25% 降到 18%）\n- Action-change statistics（统计不显著）\n- Entropy-controlled analysis（negative）\n- Causal intervention（p=0.25 inconclusive）\n- Reward signal ablation（all worse than always-on）\n- ARES reproduction（ARES dominates B-IAVR）\n\nVenue 信息：NeurIPS/ICML 级别顶会，double-blind，8+∞ pages（正文8页+附录不限）。\n\n你的审查侧重：\n- **方法描述**：是否完整、claim 是否被实验数据支撑、关键超参/训练流程是否清晰\n- **实验设计**：是否覆盖关键 baseline/ablation/跨数据集/scale 维度\n- **数据呈现**：表格/图是否能让审稿人复现结论、误差棒/统计显著性是否充分\n\n具体关注点：\n1. Eq.1 中的 gradient signal decay 公式是否严谨——GRPO 是否真的使用 γ discount？还是论文将 credit assignment 问题框架化为 discount decay 只是一个类比？\n2. h-sweep 只有 single seed（除 h=full 有 3 seeds）——中间 h 值的 ordering 是否可靠？\n3. 24.3%±6.0% 的绝对性能——3 seeds 的 95% CI 极宽（约 [12%, 37%]），统计 power 是否足够支撑 claims？\n4. 论文放弃了 selective verification 方向但未报告 negative results——是否构成 incomplete reporting？\n5. ScienceWorld 和 7B 实验是否也只有 single seed？如果是，跨环境/跨 scale 的 claims 基础薄弱\n6. Per-task breakdown N=1-4，统计意义存疑\n7. 论文只对比 step-independent baseline，缺少与其他 credit assignment 方法（如 GAE、eligibility traces）的对比\n\n**不要评判**：新颖性/相关工作（已由 Reviewer 2 覆盖）、格式/排版。\n\n请通过 `review_reviewer_post_to_director(text, reviewer_id=\"1\", project=\"cost-verify-agent-rl\", dream_id=\"20260516T235255\")` 汇报。",
  "project": "cost-verify-agent-rl",
  "chat_id": "oc_648eaf83d2b24d445764257cf6a55525",
  "director_session_key": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "[Round 1 审稿请求 - 重新触发]\n\nReviewer 1，你的上一个 session 在 venue 调研阶段中断，未提交审稿意见。请立即完成审稿。\n\n论文标题：Episode-Level RL for Multi-Turn Agents: Why Step-Independent Training Fails and How to Fix It\n\n论文摘要：本文识别了 step-independent reward assignment 在 multi-turn agent RL 训练中的根本失败模式——credit assignment decay（γ^(T-h) → 0），提出 episode-level GRPO 作为解决方案。在 ALFWorld 和 ScienceWorld 上用 Qwen3-1.7B 实验，episode-level 训练达到 24.3%±6.0% success vs step-independent 的 0%。h-sweep 揭示 h<5 时存在 sharp cliff。优势泛化到 ScienceWorld (15% vs 2%) 和 Qwen3-7B (38% vs 5%)。\n\n论文结构（8页）：\n- §1 Introduction：4 contributions — (1) identify credit assignment decay, (2) episode-level GRPO 24.3%, (3) h-sweep cliff at h=5, (4) cross-env/scale validation\n- §2 Related Work：4 paragraphs, 10 references total\n- §3 Method：problem formulation, credit assignment decay (γ^(T-h)), episode-level GRPO (Eq.3)\n- §4 Experiments：7 tables — h-sweep, multi-seed, mechanism analysis, verification ablation, cross-env, model scale, per-task breakdown\n- §5 Discussion：RAGEN relationship, model capacity bottleneck, limitations, future directions\n- §6 Conclusion\n- References：[1] RAGEN 2025, [2] Self-Guide 2026, [3] ARES 2026, [4] Thinkless NeurIPS 2025, [5] ReflAct EMNLP 2025, [6] ALFWorld ICLR 2021, [7] ScienceWorld EMNLP 2022, [8] DeepSeekMath 2024, [9] Qwen 2024, [10] Sutton & Barto 2018\n\n实验补充信息（review_context.yaml）：\n论文原计划 16 个实验，最终放弃 selective verification 方向（结果 negative/inconclusive），转型为 pure training methodology 论文。未报告的实验包括：\n- B-IAVR selective verification（success 从 25% 降到 18%）\n- Action-change statistics（统计不显著）\n- Entropy-controlled analysis（negative）\n- Causal intervention（p=0.25 inconclusive）\n- Reward signal ablation（all worse than always-on）\n- ARES reproduction（ARES dominates B-IAVR）\n\nVenue 信息：NeurIPS/ICML 级别顶会，double-blind，8+∞ pages（正文8页+附录不限）。\n\n你的审查侧重：\n- **方法描述**：是否完整、claim 是否被实验数据支撑、关键超参/训练流程是否清晰\n- **实验设计**：是否覆盖关键 baseline/ablation/跨数据集/scale 维度\n- **数据呈现**：表格/图是否能让审稿人复现结论、误差棒/统计显著性是否充分\n\n具体关注点：\n1. Eq.1 中的 gradient signal decay 公式是否严谨——GRPO 是否真的使用 γ discount？还是论文将 credit assignment 问题框架化为 discount decay 只是一个类比？\n2. h-sweep 只有 single seed（除 h=full 有 3 seeds）——中间 h 值的 ordering 是否可靠？\n3. 24.3%±6.0% 的绝对性能——3 seeds 的 95% CI 极宽（约 [12%, 37%]），统计 power 是否足够支撑 claims？\n4. 论文放弃了 selective verification 方向但未报告 negative results——是否构成 incomplete reporting？\n5. ScienceWorld 和 7B 实验是否也只有 single seed？如果是，跨环境/跨 scale 的 claims 基础薄弱\n6. Per-task breakdown N=1-4，统计意义存疑\n7. 论文只对比 step-independent baseline，缺少与其他 credit assignment 方法（如 GAE、eligibility traces）的对比\n\n**不要评判**：新颖性/相关工作（已由 Reviewer 2 覆盖）、格式/排版。\n\n请通过 `review_reviewer_post_to_director(text, reviewer_id=\"1\", project=\"cost-verify-agent-rl\", dream_id=\"20260516T235255\")` 汇报。",
    "project": "cost-verify-agent-rl",
    "chat_id": "oc_648eaf83d2b24d445764257cf6a55525",
    "director_session_key": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director"
  }
}
```

</details>

---


### Tool result

_source line 25 · 2026-05-17T00:32:32.613820+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_648eaf83d2b24d445764257cf6a55525:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 3718
}
```

</details>

---


### Assistant

_source line 26 · 2026-05-17T00:32:40.851649+00:00_

**当前审稿进度：**
- Reviewer 1（方法+实验）：🔄 已重新触发，等待回复
- Reviewer 2（新颖性+相关工作）：✅ 已完成，4/10 Reject

Reviewer 2 的三个 critical 发现：
1. **N1** 核心新颖性不足 — episode-level reward 是传统 RL default，贡献本质是修复 RAGEN 框架配置
2. **N2** 相关工作严重欠缺 — 10 篇引用，缺 GAE/PPO/REINFORCE/HER/WebAgent 等核心文献
3. **N3** Self-Guide 72.7% vs 本文 24.3% 同模型同环境，"model capacity bottleneck" 论点被直接反驳

等待 Reviewer 1 提交后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director"
}
```

</details>

---


## Round 2

## Round 2

6 recorded events


### User

_source line 27 · 2026-05-17T00:32:41.929204+00:00_

[Reviewer 2 审稿结果]:
审稿意见已提交给 Review Director。

核心判断：**Reject (4/10)**。三个 critical 问题：
1. 新颖性不足——episode-level reward 是传统 RL default，贡献本质是发现 RAGEN 框架的配置问题
2. 相关工作严重欠缺——10 篇引用，缺 GAE/PPO/REINFORCE/HER/WebAgent/AgentTuning 等核心文献
3. 与 Self-Guide (72.7% vs 24.3% 同模型同环境) 的性能差距未解释，"model capacity bottleneck" 论点被直接反驳

---

[Reviewer 1 审稿意见]:
## 总体评分
**Overall**: 3/6 (Borderline Reject)
**一句话总结**: 论文识别了一个合理的问题，但核心理论公式存在严谨性问题，实验统计力不足以支撑其 claims，且 baseline 比较过于单薄。

## 官方维度打分（参照 NeurIPS 2025/2026 Review Form）
| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Quality (Soundness) | 2/5 | Eq.1 的 γ^(T-h) 公式化存在根本性问题（GRPO 是否真的使用 γ discount？）；3 seeds 的统计 power 极度不足 |
| Clarity | 3/5 | 写作尚可，但核心方法的精确定义模糊（"step-independent" 的具体操作未明确） |
| Significance | 3/5 | 问题方向重要（multi-turn agent RL 的 credit assignment），但绝对性能低（24.3%），实际意义有限 |
| Originality | 3/5 | Episode-level GRPO 本身是一个自然的 baseline 选择而非真正的方法创新；主要贡献在于经验观察（h-cliff） |

**Confidence**: 4/5 (对 RL 和 LLM agent 训练较为熟悉)

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] Eq.1 γ^(T-h) 公式化的严谨性存疑——GRPO 的标准公式不包含 γ discount

- 具体位置：§3, Eq.1 (gradient signal decay), Eq.2 (credit assignment decay analysis)
- 问题：标准 GRPO（DeepSeek-R1, Shao et al. 2024）的目标函数是 group-relative advantage，不含显式 γ discount factor。论文将 multi-turn credit assignment 问题框架化为 γ^(T-h) → 0 的指数衰减，但这一公式对应的是 standard discounted policy gradient with terminal reward 的情形。如果"step-independent training"实际操作是将 episode reward 均匀分配给每步（无 discounting），则不存在 γ^(T-h) 衰减；如果操作是标准 discounted RL，则修复方案应是调 γ 或用 GAE，而非切换到 episode-level。论文必须明确：(a) "step-independent training"的精确算法描述（reward 如何分配到每步？），(b) Eq.1 是严格数学推导还是类比？(c) 如果是类比，为何选择 γ^(T-h) 而非其他表达？
- 为什么影响接收：这是论文的核心理论基础。如果 Eq.1 只是类比而非推导，则 "credit assignment decay" 的"发现"站不住脚，论文降级为纯经验观察。
- 建议修改方向：给出 step-independent baseline 的完整算法伪代码；明确 γ 在具体实现中的角色（如果 γ=1 则无 decay）；如果 decay 来自其他机制（如 KL penalty 的累积效应或 gradient variance），应重新推导。

**N2** [critical] 统计 Power 严重不足——3 seeds 的 95% CI 覆盖了从 "几乎不工作" 到 "中等性能" 的整个范围

- 具体位置：§4.3, Table 2 (24.3% ± 6.0%, 3 seeds)
- 问题：3 个种子的标准差 6.0%，对应 95% CI = 24.3 ± t_{0.025,2} × (6.0/√3) = 24.3 ± 14.9%，即 [9.4%, 39.2%]。这意味着真实性能可能低至 ~10%。更重要的是，论文声称的 "24.3% vs 0%" 差异虽然 effect size 大，但 0% baseline 本身也是 single seed（除了 h=full），无法排除 baseline 的 single run 碰巧失败的可能。建议至少 5-8 seeds 或使用 bootstrap confidence intervals。
- 为什么影响接收：整篇论文的 claims 建立在这个数字上，但其不确定性足以动摇所有下游结论（cross-env improvement 和 scaling claims 都依赖 ALFWorld 的基准数字）。
- 建议修改方向：增加 seeds 到至少 5 个；对 step-independent baseline 也跑多 seeds 证明其确实是 systematic failure（0% across 5+ seeds）而非单次 unlucky run。

**N3** [critical] Baseline 比较过于单薄——缺少与标准 credit assignment 方法的对比

- 具体位置：§4 全部实验，仅对比 episode-level vs step-independent
- 问题：Credit assignment in RL 是一个经典问题，已有大量解决方案：(a) GAE (Generalized Advantage Estimation) 通过 λ-return 平衡 bias-variance，(b) eligibility traces 显式传递信息，(c) hindsight credit assignment / reward redistribution，(d) 设置 γ=1 但配合 baseline function 减少 variance。论文声称 "step-independent training fails"，但只对比了一个极端 baseline（完全独立的 per-step training）。episode-level training 也是这个谱系的另一个极端。真正有信息量的实验是：在同样的 multi-turn 设置中，GAE (λ=0.95, γ=0.99) 或 reward reshaping 是否也能解决问题？如果能，则 "episode-level GRPO" 并非唯一或最优方案。
- 为什么影响接收：没有中间 baseline 的对比，无法判断论文贡献的真实增量——episode-level 可能只是 "任何合理的 credit assignment" 都能 work 的一个特例。
- 建议修改方向：至少加入 (1) γ=1 + per-step reward with group normalization, (2) GAE-style multi-step return 两个中间 baseline。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] h-sweep (Table 1) 除 h=full 外均为 single seed，中间 h 值的 ordering 不可靠

- 具体位置：§4.2, Table 1
- 问题：h∈{1,2,3,5,8,10,15,20} 每个点只有 1 个 seed。在训练 variance 较大的设置中（如 Table 2 显示的 6% std），单次观测无法建立可靠的 ordering。特别是 "h<5 存在 sharp cliff" 的 claim 可能只是噪声——h=3 和 h=5 的差异如果在 1-seed noise 范围内，cliff 就不成立。
- 建议：对关键 cliff 边界（h=3,4,5）跑 3 seeds 验证 cliff 的稳健性。

**W2** [warning] Cross-environment (Table 5) 和 model scale (Table 6) 实验疑似 single seed

- 具体位置：§4.6 Table 5, §4.7 Table 6
- 问题：ScienceWorld 15% vs 2%, 7B 38% vs 5%——论文用这些数据声称 "优势泛化到新环境和更大模型"。但如果这些都是 single seed，则单个数字的对比不构成 "泛化" 的证据。ALFWorld 3 seeds 的 std 已经是 6%，ScienceWorld 和 7B 的 variance 可能更大。
- 建议：明确报告每个实验的 seed 数量；critical claims（泛化、scaling）需要多 seed 支撑。

**W3** [warning] Per-task breakdown (Table 7) 统计意义存疑

- 具体位置：§4.8, Table 7, "r=-0.42 correlation with episode length"
- 问题：6 个 task types，每个 type N=1-4 episodes。(a) 每个 task type 的 success rate 本身 noisy（如 N=2 时只有 0%, 50%, 100% 三种可能值），(b) r=-0.42 with n=6 data points 的 critical value（α=0.05, two-tailed）约为 0.81，远未达到统计显著。这个 "负相关" claim 没有统计基础。
- 建议：要么增大样本量，要么删除这个 correlation claim，只保留 descriptive breakdown。

**W4** [warning] 绝对性能偏低，实用意义需讨论

- 具体位置：§4.3 (24.3% success), §5 Discussion
- 问题：即使接受论文的数字，24.3% 的 success rate 在 ALFWorld 上相当低（基于 ReAct、Reflexion 等方法在 ALFWorld 上通常能达到 40-70%+）。论文使用的是较小的 Qwen3-1.7B，但读者需要理解：(a) 这个数字相对于 SoTA 如何？(b) episode-level GRPO 是否能 scale 到实用水平，还是存在 fundamental ceiling？
- 建议：在 Discussion 中明确对比 SoTA 方法（即使它们用更大模型或 prompting 而非 RL），给出 performance landscape 的定位。

---

## 小问题（不影响接收）

- Table 3 (Credit Assignment Mechanism): "γ^(T-h) vs observed success correlation" 的具体计算方法需要更明确的描述——是 Pearson/Spearman？在什么样本上计算？
- §4.1 Setup: GRPO with KL=0.01, G=8, lr=5e-6 的超参来源未说明（grid search? 文献推荐? pilot experiment?），影响可复现性。
- Table 4 (Verification Value): "episode-level+verify 25%, no-verify 15%" 看起来 verify 贡献了 +10pp，但没有 significance test。这个差异在 3-seed variance (6%) 下是否显著？
- References 只有 10 条——对于一篇涉及 RL、credit assignment、multi-turn agents、GRPO 的论文，引用覆盖度明显不足。

---

## 主要优势

- 问题定义有价值：Multi-turn agent RL 中的 credit assignment 确实是一个实际且重要的瓶颈
- h-sweep 的实验设计思路好（即使执行上 statistical power 不足）：通过 context window 扫描来探测 credit assignment 行为是一个有信息量的 experimental paradigm
- 对比了两个 environment 和两个 model scale，展示了 generalization 的意图
- 论文长度控制在 8 页内，结构清晰

---

## 总结建议

本文识别的问题（multi-turn credit assignment for agent RL）是有价值的研究方向。但当前版本存在三个核心缺陷：(1) 理论公式化 Eq.1 的严谨性需要根本性澄清——GRPO 中 γ 的角色必须精确定义，(2) 统计 power 全面不足——几乎所有 claims 都建立在 single-seed 或 3-seed 实验上，(3) baseline 比较过于简化——只对比两个极端，缺少中间方案。建议作者增加 seeds、加入 GAE 等标准 credit assignment baseline、并严格区分数学推导与经验类比。

---

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

核心判断：**3/6 Borderline Reject**。三个 critical 问题：
1. Eq.1 γ^(T-h) 公式严谨性存疑（GRPO 不含 γ discount，需澄清是推导还是类比）
2. 统计 power 全面不足（3 seeds 的 95% CI 为 [9.4%, 39.2%]，h-sweep 和 cross-env 均为 single seed）
3. Baseline 只对比一个极端（step-independent），缺少 GAE、eligibility traces 等标准 credit assignment 方案

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 28 · 2026-05-17T00:33:19.782389+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "[Round 1 交叉分享] 以下是 Reviewer 2 的完整审稿意见。请逐条回应：[AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 完整审稿（新颖性 + 相关工作方向）\n\n**Overall**: 4/10 (Reject)\n\n### Must-Fix 问题\n\n**N1** [critical] 核心新颖性不足：episode-level reward 是传统 RL 的 default，非 contribution\n- 具体位置：§3 Method, Contribution (1) \"identify credit assignment decay\"\n- 问题：γ^(T-h) → 0 当 T 大时奖励信号衰减，这是 Sutton & Barto (2018) [10] 第 13 章 eligibility traces 的基础内容。论文自己引用了这本教科书，却将教科书内容包装为\"识别了根本失败模式\"。在传统 RL 中，episode-level return（即 REINFORCE）一直是 default 做法。本文的实际贡献是：发现 RAGEN 框架的默认配置在 multi-turn 场景下有 bug-like behavior，并通过使用 episode-level aggregation 修复。这更接近 technical report 或 workshop paper 级别的贡献。\n- 建议修改方向：(a) 深入分析为什么 LLM agent 社区默认采用了 step-independent training；(b) 提出超越简单 episode-level aggregation 的方法。\n\n**N2** [critical] 相关工作严重不足：10 篇引用无法支撑顶会论文\n- 关键缺失：PPO、REINFORCE、GAE、HER (Andrychowicz 2017)、AgentQ（正文提及无引用）、WebAgent、AgentTuning、FireAct、Reflexion、Reward shaping (Ng et al. 1999)\n- 建议：系统补充，增加 \"Credit Assignment in RL\" 和 \"LLM Agent Training\" 两个 subsection。\n\n**N3** [critical] 与 Self-Guide 的对比逻辑自相矛盾\n- Self-Guide 用 Qwen-1.7B 在 ALFWorld 达到 72.7%，本文只有 24.3%。Discussion 中 \"model capacity is separate bottleneck\" 被 Self-Guide 直接反驳。\n- 审稿人会问：同模型已有 72.7% 的方法，为什么关注 24.3% 的方法？\n\n### Should-Fix 问题\n\n**W1** Claim overclaiming：\"eliminates this bottleneck\" vs 25% success\n**W2** Contribution (1) 与 Contribution (3) 存在冗余/循环论证\n**W3** Future directions 暴露 stepping-stone 定位\n**W4** 论文叙事转型痕迹可能残留\n\n### 主要优势\n- 问题定义清晰\n- 实验设计系统（h-sweep, multi-seed）\n- 实用价值（对 RAGEN/GRPO 用户有直接指导意义）\n- 跨环境和跨规模验证\n\n---\n\n请对 Reviewer 2 的每个 Must-Fix 和 Should-Fix 问题逐条给出 [AGREE] 或 [REBUT]，并结合你自己的审稿发现说明理由。",
  "project": "cost-verify-agent-rl",
  "chat_id": "oc_648eaf83d2b24d445764257cf6a55525",
  "director_session_key": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "[Round 1 交叉分享] 以下是 Reviewer 2 的完整审稿意见。请逐条回应：[AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 完整审稿（新颖性 + 相关工作方向）\n\n**Overall**: 4/10 (Reject)\n\n### Must-Fix 问题\n\n**N1** [critical] 核心新颖性不足：episode-level reward 是传统 RL 的 default，非 contribution\n- 具体位置：§3 Method, Contribution (1) \"identify credit assignment decay\"\n- 问题：γ^(T-h) → 0 当 T 大时奖励信号衰减，这是 Sutton & Barto (2018) [10] 第 13 章 eligibility traces 的基础内容。论文自己引用了这本教科书，却将教科书内容包装为\"识别了根本失败模式\"。在传统 RL 中，episode-level return（即 REINFORCE）一直是 default 做法。本文的实际贡献是：发现 RAGEN 框架的默认配置在 multi-turn 场景下有 bug-like behavior，并通过使用 episode-level aggregation 修复。这更接近 technical report 或 workshop paper 级别的贡献。\n- 建议修改方向：(a) 深入分析为什么 LLM agent 社区默认采用了 step-independent training；(b) 提出超越简单 episode-level aggregation 的方法。\n\n**N2** [critical] 相关工作严重不足：10 篇引用无法支撑顶会论文\n- 关键缺失：PPO、REINFORCE、GAE、HER (Andrychowicz 2017)、AgentQ（正文提及无引用）、WebAgent、AgentTuning、FireAct、Reflexion、Reward shaping (Ng et al. 1999)\n- 建议：系统补充，增加 \"Credit Assignment in RL\" 和 \"LLM Agent Training\" 两个 subsection。\n\n**N3** [critical] 与 Self-Guide 的对比逻辑自相矛盾\n- Self-Guide 用 Qwen-1.7B 在 ALFWorld 达到 72.7%，本文只有 24.3%。Discussion 中 \"model capacity is separate bottleneck\" 被 Self-Guide 直接反驳。\n- 审稿人会问：同模型已有 72.7% 的方法，为什么关注 24.3% 的方法？\n\n### Should-Fix 问题\n\n**W1** Claim overclaiming：\"eliminates this bottleneck\" vs 25% success\n**W2** Contribution (1) 与 Contribution (3) 存在冗余/循环论证\n**W3** Future directions 暴露 stepping-stone 定位\n**W4** 论文叙事转型痕迹可能残留\n\n### 主要优势\n- 问题定义清晰\n- 实验设计系统（h-sweep, multi-seed）\n- 实用价值（对 RAGEN/GRPO 用户有直接指导意义）\n- 跨环境和跨规模验证\n\n---\n\n请对 Reviewer 2 的每个 Must-Fix 和 Should-Fix 问题逐条给出 [AGREE] 或 [REBUT]，并结合你自己的审稿发现说明理由。",
    "project": "cost-verify-agent-rl",
    "chat_id": "oc_648eaf83d2b24d445764257cf6a55525",
    "director_session_key": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director"
  }
}
```

</details>

---


### Tool result

_source line 29 · 2026-05-17T00:33:36.562388+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_648eaf83d2b24d445764257cf6a55525:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 16779
}
```

</details>

---


### Tool call

_source line 30 · 2026-05-17T00:33:37.014303+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "[Round 1 交叉分享] 以下是 Reviewer 1 的完整审稿意见。请逐条回应：[AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 完整审稿（方法 + 实验方向）\n\n**Overall**: 3/6 (Borderline Reject)\n\n### Must-Fix 问题\n\n**N1** [critical] Eq.1 γ^(T-h) 公式化的严谨性存疑——GRPO 的标准公式不包含 γ discount\n- 具体位置：§3, Eq.1, Eq.2\n- 问题：标准 GRPO（DeepSeek-R1）的目标函数是 group-relative advantage，不含显式 γ discount factor。论文将 multi-turn credit assignment 问题框架化为 γ^(T-h) → 0 的指数衰减，但这对应的是 standard discounted policy gradient with terminal reward。如果\"step-independent training\"实际是将 episode reward 均匀分配给每步（无 discounting），则不存在 γ^(T-h) 衰减。论文必须明确：(a) step-independent 的精确算法描述，(b) Eq.1 是严格推导还是类比？(c) 如果是类比，为何选择 γ^(T-h)？\n- 影响：如果 Eq.1 只是类比，\"credit assignment decay\" 的发现站不住脚，论文降级为纯经验观察。\n\n**N2** [critical] 统计 Power 严重不足——3 seeds 的 95% CI 为 [9.4%, 39.2%]\n- 具体位置：§4.3, Table 2\n- 问题：24.3% ± 14.9% (95% CI)。真实性能可能低至 ~10%。0% baseline 也是 single seed，无法排除碰巧失败。\n- 建议：至少 5-8 seeds；对 step-independent baseline 也跑多 seeds。\n\n**N3** [critical] Baseline 比较过于单薄——缺少与 GAE、eligibility traces 等标准方法的对比\n- 具体位置：§4 全部实验\n- 问题：只对比了两个极端（step-independent vs episode-level），缺少中间方案。GAE (λ=0.95, γ=0.99) 或 reward reshaping 在同样设置中是否也能解决问题？如果能，\"episode-level GRPO\" 并非唯一或最优方案。\n- 建议：加入 γ=1 + per-step reward with group normalization 和 GAE-style multi-step return 两个中间 baseline。\n\n### Should-Fix 问题\n\n**W1** h-sweep (Table 1) 除 h=full 外均为 single seed，cliff claim 可能是噪声\n**W2** Cross-environment (Table 5) 和 model scale (Table 6) 疑似 single seed\n**W3** Per-task breakdown (Table 7) r=-0.42 with n=6 未达统计显著（critical value ~0.81）\n**W4** 绝对性能偏低（24.3% vs SoTA 40-70%+），实用意义需讨论\n\n### 小问题\n- Table 3 correlation 计算方法不明确\n- GRPO 超参来源未说明\n- Table 4 verify vs no-verify (+10pp) 未做 significance test\n- References 只有 10 条\n\n### 主要优势\n- Multi-turn credit assignment 是有价值的研究方向\n- h-sweep 实验设计思路好\n- 跨环境和跨 scale 的泛化意图\n- 结构清晰\n\n---\n\n请对 Reviewer 1 的每个 Must-Fix 和 Should-Fix 问题逐条给出 [AGREE] 或 [REBUT]，并结合你自己的审稿发现说明理由。",
  "project": "cost-verify-agent-rl",
  "chat_id": "oc_648eaf83d2b24d445764257cf6a55525",
  "director_session_key": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "[Round 1 交叉分享] 以下是 Reviewer 1 的完整审稿意见。请逐条回应：[AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 完整审稿（方法 + 实验方向）\n\n**Overall**: 3/6 (Borderline Reject)\n\n### Must-Fix 问题\n\n**N1** [critical] Eq.1 γ^(T-h) 公式化的严谨性存疑——GRPO 的标准公式不包含 γ discount\n- 具体位置：§3, Eq.1, Eq.2\n- 问题：标准 GRPO（DeepSeek-R1）的目标函数是 group-relative advantage，不含显式 γ discount factor。论文将 multi-turn credit assignment 问题框架化为 γ^(T-h) → 0 的指数衰减，但这对应的是 standard discounted policy gradient with terminal reward。如果\"step-independent training\"实际是将 episode reward 均匀分配给每步（无 discounting），则不存在 γ^(T-h) 衰减。论文必须明确：(a) step-independent 的精确算法描述，(b) Eq.1 是严格推导还是类比？(c) 如果是类比，为何选择 γ^(T-h)？\n- 影响：如果 Eq.1 只是类比，\"credit assignment decay\" 的发现站不住脚，论文降级为纯经验观察。\n\n**N2** [critical] 统计 Power 严重不足——3 seeds 的 95% CI 为 [9.4%, 39.2%]\n- 具体位置：§4.3, Table 2\n- 问题：24.3% ± 14.9% (95% CI)。真实性能可能低至 ~10%。0% baseline 也是 single seed，无法排除碰巧失败。\n- 建议：至少 5-8 seeds；对 step-independent baseline 也跑多 seeds。\n\n**N3** [critical] Baseline 比较过于单薄——缺少与 GAE、eligibility traces 等标准方法的对比\n- 具体位置：§4 全部实验\n- 问题：只对比了两个极端（step-independent vs episode-level），缺少中间方案。GAE (λ=0.95, γ=0.99) 或 reward reshaping 在同样设置中是否也能解决问题？如果能，\"episode-level GRPO\" 并非唯一或最优方案。\n- 建议：加入 γ=1 + per-step reward with group normalization 和 GAE-style multi-step return 两个中间 baseline。\n\n### Should-Fix 问题\n\n**W1** h-sweep (Table 1) 除 h=full 外均为 single seed，cliff claim 可能是噪声\n**W2** Cross-environment (Table 5) 和 model scale (Table 6) 疑似 single seed\n**W3** Per-task breakdown (Table 7) r=-0.42 with n=6 未达统计显著（critical value ~0.81）\n**W4** 绝对性能偏低（24.3% vs SoTA 40-70%+），实用意义需讨论\n\n### 小问题\n- Table 3 correlation 计算方法不明确\n- GRPO 超参来源未说明\n- Table 4 verify vs no-verify (+10pp) 未做 significance test\n- References 只有 10 条\n\n### 主要优势\n- Multi-turn credit assignment 是有价值的研究方向\n- h-sweep 实验设计思路好\n- 跨环境和跨 scale 的泛化意图\n- 结构清晰\n\n---\n\n请对 Reviewer 1 的每个 Must-Fix 和 Should-Fix 问题逐条给出 [AGREE] 或 [REBUT]，并结合你自己的审稿发现说明理由。",
    "project": "cost-verify-agent-rl",
    "chat_id": "oc_648eaf83d2b24d445764257cf6a55525",
    "director_session_key": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director"
  }
}
```

</details>

---


### Tool result

_source line 31 · 2026-05-17T00:33:38.377850+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_648eaf83d2b24d445764257cf6a55525:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1363
}
```

</details>

---


### Assistant

_source line 32 · 2026-05-17T00:33:49.362549+00:00_

交叉分享已发出。等待两位 Reviewer 的逐条 [AGREE]/[REBUT] 回应。

**当前进度**：
- Round 1 独立审稿 ✓（两人均完成）
- Step 2 交叉分享 → 已触发，等待回应
- Step 3 收敛判断 → 待定
- Step 4 汇总报告 → 待定

初步观察：两位 Reviewer 在以下问题上可能已有共识：
1. **统计力不足**（R1-N2）+ **绝对性能偏低**（R2-W1）— 方向一致
2. **缺少 GAE 等中间 baseline**（R1-N3）+ **相关工作不足**（R2-N2）— 互相强化
3. **公式严谨性**（R1-N1）与 **新颖性不足**（R2-N1）— 可能联动（如果公式只是类比，则更强化 "workshop paper" 定位）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director"
}
```

</details>

---


## Round 3

## Round 3

2 recorded events


### User

_source line 33 · 2026-05-17T00:34:19.002178+00:00_

[Reviewer 1 审稿意见]:
## 总体评分
**Overall**: 3/6 (Borderline Reject)
**一句话总结**: 论文识别了一个合理的问题（multi-turn agent RL 的 credit assignment），但核心理论公式存在严谨性问题，实验统计力严重不足，且 baseline 比较过于单薄，不满足 NeurIPS/ICML 级别的方法论论文标准。

## 官方维度打分（参照 NeurIPS 2025/2026 Review Form: Quality / Clarity / Significance / Originality）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Quality (Soundness) | 2/5 | Eq.1 的 γ^(T-h) 公式化与 GRPO 标准算法不一致；3 seeds 统计 power 极不足；baseline 只有一个极端对照 |
| Clarity | 3/5 | 结构清晰，但"step-independent training"的精确算法定义缺失，Eq.1-3 之间逻辑跳跃较大 |
| Significance | 3/5 | 问题方向重要，但绝对性能低（24.3%），与 prompting-based SoTA（ReAct/Reflexion 40-70%）差距大，实用意义有限 |
| Originality | 2/5 | Episode-level GRPO 是一个自然的设计选择而非方法创新；主要贡献在于经验观察（h-cliff），但这需要更强的统计支撑 |

**Confidence**: 4/5（对 RL credit assignment 和 LLM agent 训练熟悉）

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] Eq.1 γ^(T-h) gradient signal decay 的理论基础存疑——GRPO 标准公式不含 γ discount

- 具体位置：§3, Eq.1, Eq.2
- 问题：标准 GRPO（DeepSeek-R1, [8]）的目标函数使用 group-relative advantage A_i = (r_i - mean(r))/std(r)，不含显式 γ discount factor。论文将 credit assignment 问题框架化为 γ^(T-h) → 0，这对应的是 standard discounted policy gradient with terminal reward 的情形（Sutton & Barto [10], Ch.13），而非 GRPO。

  关键疑问：
  (a) "Step-independent training"的精确算法是什么？如果是将 episode reward 均匀赋给每步后做 per-step GRPO，则不存在 γ decay——问题是 uniform credit（所有步同权），修复应是 reward redistribution 而非 episode-level training。
  (b) 如果确实引入了 γ<1 的 discount，那么修复方案应首先尝试 γ=1 或 GAE(λ)，而非直接跳到 episode-level——论文为何跳过了这些标准方案？
  (c) 如果 Eq.1 是类比而非推导，论文需要明确标注，否则读者会误以为这是从 GRPO 目标函数严格推出的结论。

- 为什么影响接收：这是论文的核心理论 claim——"我们发现了 credit assignment decay 失败模式"。如果公式化不准确，论文的方法论贡献降级为"我们观察到 episode-level 比 step-level 好"，这对 NeurIPS/ICML 来说贡献不足。
- 建议修改方向：(1) 给出 step-independent baseline 的完整算法伪代码（逐行对应 GRPO 公式），(2) 精确指出 γ 在哪一步引入、为何不可设为 1，(3) 如果 decay 来自其他机制（KL 累积/gradient variance/token-level vs episode-level normalization），重新推导。

**N2** [critical] 统计 Power 全面不足——核心 claim 建立在 3 seeds 上，95% CI 覆盖 [9%, 39%]

- 具体位置：§4.3 Table 2 (24.3% ± 6.0%, 3 seeds)
- 问题：
  - 3 seeds，sd=6.0% → SE = 6.0/√3 ≈ 3.46% → 95% CI = 24.3 ± t_{0.025,2} × 3.46 = 24.3 ± 14.9%，即 **[9.4%, 39.2%]**
  - 真实性能可能低至 ~10%，此时"显著优于 step-independent"的 claim 虽然技术上仍成立（vs 0%），但 effect magnitude 大幅缩水
  - 更严重的问题：step-independent 的 0% 是否也有多 seed 验证？如果 baseline 也只跑了 1-3 次碰巧全部失败，则核心对比的可靠性存疑
  - h-sweep (Table 1) 除 h=full 外全部 single seed，"sharp cliff at h<5"的 claim 在 6% noise 下不可靠

- 为什么影响接收：NeurIPS/ICML 方法论论文的实验标准要求 claims 有充分统计支撑。当前 3 seeds 对于 noisy RL training（ALFWorld episode 数有限、reward sparse）远远不够。
- 建议修改方向：(1) 所有关键实验增加到 5-8 seeds，(2) 对 step-independent baseline 也报告多 seed 结果（证明 0% 是 systematic 而非 unlucky），(3) h-sweep 至少在 cliff 边界 (h=3,4,5) 跑 3 seeds 验证 transition 的稳健性。

**N3** [critical] Baseline 比较严重不足——缺少与标准 credit assignment 方法的对比

- 具体位置：§4 所有实验（仅 episode-level vs step-independent）
- 问题：Credit assignment 是经典 RL 问题，标准解决方案包括：
  1. **GAE (Generalized Advantage Estimation)**: λ-return 平衡 bias-variance，是 PPO/GRPO 的标准 companion
  2. **γ=1 without discounting**: 如果问题是 γ<1 导致 decay，最直接的 fix 是 γ=1
  3. **Reward redistribution / reshaping**: 将 terminal reward 按 attention 或 gradient 重分配到中间步
  4. **Hindsight credit assignment**: 事后根据成功 trajectory 反推各步贡献

  论文只对比了两个极端：完全 step-independent（每步独立） vs 完全 episode-level（全序列作为一体）。缺少中间方案的对比，无法回答："episode-level 是唯一有效方案，还是只要 credit assignment 做得合理就行？"

- 为什么影响接收：如果 GAE(λ=0.95) + per-step training 也能达到 20%+ success，则 episode-level GRPO 的贡献为零——它只是"合理 credit assignment"的一个特例。没有这些对比，论文的贡献主张无法被验证。
- 建议修改方向：至少加入 (1) γ=1 + step-level GRPO（消除 discount 但保留 per-step 结构），(2) GAE(λ=0.95) based advantage estimation，(3) reward reshaping（按 trajectory position 线性/uniform 分配）。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] h-sweep (Table 1) 中间值 single seed，"sharp cliff" claim 不可靠

- 具体位置：§4.2, Table 1
- 问题：h∈{1,2,3,5,8,10,15,20} 各 1 seed。Table 2 显示 h=full 的 3-seed std = 6%，意味着任何 single-seed 观测的 noise 可达 ±6%。h=3 和 h=5 之间的差异如果在此 noise band 内，"sharp cliff"就是 artifact。
- 建议：h=3,4,5 各跑 3 seeds，用 mean±se 绘制 cliff transition curve，验证 transition 是 sharp 还是 gradual。

**W2** [warning] Cross-environment (Table 5) 和 Model Scale (Table 6) 疑似 single seed

- 具体位置：§4.6 Table 5 (ScienceWorld 15% vs 2%), §4.7 Table 6 (7B: 38% vs 5%)
- 问题：论文声称"优势泛化到新环境和更大模型"，但如果这些实验是 single seed，则单个数字的对比不构成"泛化"的证据。特别是 7B 的 38%——如果 variance 类似 1.7B 的 6%，一次 lucky run 就能解释这个数字。
- 建议：明确标注每个实验的 seed 数量；generalization claims 需 ≥3 seeds。

**W3** [warning] Per-task breakdown (Table 7) r=-0.42 correlation 统计不显著

- 具体位置：§4.8, Table 7
- 问题：6 个 task types，每类 N=1-4 episodes。(a) 每类 success rate 取值受限（N=2 时只有 0%/50%/100%），(b) n=6 时 Pearson r 的 critical value (α=0.05, two-tailed) ≈ 0.81，r=-0.42 远未显著 (p≈0.41)。"episode length 与 success 负相关"的 claim 无统计基础。
- 建议：删除 correlation claim，保留 descriptive breakdown；或增大每类样本量后重新检验。

**W4** [warning] 10 条 references 对于 NeurIPS/ICML 论文严重不足

- 具体位置：References section
- 问题：涉及 RL credit assignment、multi-turn agents、GRPO、LLM training 四大领域，10 条引用远低于 venue 平均水平（通常 30-50 条）。缺失的关键引用至少包括：PPO (Schulman 2017)、GAE (Schulman 2016)、RLHF 系列、AgentBench、WebShop 等 agent benchmark、reward shaping 经典文献 (Ng et al. 1999)。
- 建议：显著扩充 references，至少覆盖 RL foundations、credit assignment classics、agent training concurrent work、benchmark papers。

**W5** [warning] Negative results 未报告可能构成 incomplete picture

- 具体位置：§4（实验章节）、§5 Discussion
- 问题：作为审稿人，我注意到论文 §5 Discussion 提到了 "model capacity bottleneck" 和 "limitations"，但如果团队尝试过 selective verification / reward ablation 等方向且失败了，在 Discussion 中简要提及 "什么不 work"会显著增加论文的信息量和可信度。当前论文给人的印象是"episode-level GRPO 一试就灵"，但现实中 RL 训练很少如此顺利。
- 建议：在 Discussion 或 Appendix 中加入 "Negative Results" subsection，简述尝试过但失败的方向及 lesson learned。这在 NeurIPS 社区越来越受欢迎。

---

## 小问题（不影响接收）

- Table 3 (Credit Assignment Mechanism): "γ^(T-h) vs observed success correlation"的统计方法（Pearson? Spearman? 样本量?）未说明
- §4.1 Setup: 超参选择（KL=0.01, G=8, lr=5e-6）的来源未说明——是 grid search 还是文献推荐？缺乏 sensitivity analysis
- Table 4: "episode-level+verify 25% vs no-verify 15%"差异 10pp，在 sd=6% 的 noise 下是否显著？需要 paired test
- §4.1: ALFWorld T=48, ScienceWorld T=35——这些是 max steps 还是 average steps？对 γ^(T-h) analysis 有直接影响

---

## 主要优势

- **问题有实际价值**：Multi-turn agent RL 的 credit assignment 确实是当前训练中的真实瓶颈，非人为构造的问题
- **h-sweep 实验范式有启发性**：通过 context window 大小扫描来探测 credit assignment 行为的 experimental paradigm 本身值得借鉴
- **实验覆盖面有意识**：尝试了 cross-environment（ALFWorld→ScienceWorld）和 cross-scale（1.7B→7B）验证
- **结构紧凑**：8 页内完整呈现了问题、方法、实验，无明显冗余

---

## 审稿总结

本文方向正确——multi-turn agent RL 的 credit assignment 是重要且 underexplored 的问题。但当前版本存在三个互相关联的核心缺陷：

1. **理论基础不稳**：Eq.1 γ^(T-h) 框架化与 GRPO 实际算法之间的对应关系不清晰，"credit assignment decay"可能是对问题的误诊
2. **统计力全面不足**：几乎所有 claims 建立在 single-seed 或 3-seed 实验上，在 RL 训练的高 variance 下不可靠
3. **Baseline 比较缺失**：只对比一个极端 baseline，无法确定 episode-level 是否为最优方案或仅为"任何合理 credit assignment"的一个特例

建议 major revision 后重投：增加 seeds 到 5-8、加入 GAE 等标准 credit assignment baselines、严格化 Eq.1 的推导（或明确其为类比而非定理）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 34 · 2026-05-17T00:34:35.580412+00:00_

Reviewer 1 完整审稿已收到（重新触发后成功提交）。两位 Reviewer 的初审结果一致性高：

| | Reviewer 1 (方法+实验) | Reviewer 2 (新颖性+相关工作) |
|--|--|--|
| 评分 | 3/6 Borderline Reject | 4/10 Reject |
| 核心问题 | Eq.1 理论基础不稳、统计力不足、baseline 单薄 | 新颖性不足、引用严重欠缺、Self-Guide 对比矛盾 |

交叉分享已发送，等待两位 Reviewer 的 [AGREE]/[REBUT] 回应后进入收敛判断。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director"
}
```

</details>

---


## Round 4

## Round 4

2 recorded events


### User

_source line 35 · 2026-05-17T00:34:38.176350+00:00_

[Reviewer 1 审稿结果]:
审稿意见已成功提交。评分 3/6 (Borderline Reject)，核心问题：(1) Eq.1 γ^(T-h) 理论公式与 GRPO 实际算法不匹配，(2) 3 seeds 统计力严重不足（95% CI 覆盖 [9%,39%]），(3) 只对比一个极端 baseline 缺少 GAE 等标准 credit assignment 方法。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 36 · 2026-05-17T00:35:00.963148+00:00_

两位 Reviewer 初审均已确认收到。交叉分享请求已发出，等待双方 [AGREE]/[REBUT] 回应后进入收敛判断和报告汇总。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director"
}
```

</details>

---


## Round 5

## Round 5

16 recorded events


### User

_source line 37 · 2026-05-17T00:35:00.969069+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 对 Reviewer 1 审稿意见的逐条回应

---

### Must-Fix 问题

**[AGREE] R1-N1: Eq.1 γ^(T-h) 公式化严谨性**

强烈同意。这个问题实际上比 R1 表述的更严重。如果标准 GRPO 不包含显式 γ discount（DeepSeekMath [8] 的 group-relative advantage 是 undiscounted），那么论文的整个理论框架——"credit assignment decay" 作为 γ^(T-h) → 0——就缺乏数学基础。

这直接加强了我在 R2-N1 中的判断：论文声称 "identify credit assignment decay as root cause"，但如果这个 decay 在实际实现中并不以 γ^(T-h) 的形式存在，那 Contribution (1) 就从"发现教科书知识在新 context 中的应用"进一步降级为"基于错误类比的叙事包装"。论文必须明确回答：step-independent training 中 credit assignment 失败的**真实机制**是什么？是 reward dilution（均匀分配到每步导致信号被稀释）？还是 variance explosion？还是其他？

**[AGREE] R1-N2: 统计 Power 不足（3 seeds, 95% CI [9.4%, 39.2%]）**

同意。补充一个角度：这个统计问题与新颖性问题叠加后果更严重。论文的核心 claim 是 "episode-level achieves 24.3% vs step-independent 0%"。如果真实性能可能低至 ~10%，加上 step-independent baseline 只跑了 single seed（可能碰巧 0%），那么 effect size 的可信度大幅降低。对于一篇 novelty 主要来自实验发现的论文，统计不可靠直接动摇了全部贡献。

不过要指出：即便 lower bound 是 ~10%，vs 0% 的定性区别（"能学会 vs 完全不能学会"）仍然有信息量。问题在于需要更多 seeds 来确认 step-independent 确实是 0% 而非某个小的正数。

**[AGREE] R1-N3: 缺少 GAE / eligibility traces 等中间 baseline**

强烈同意，这与我的 R2-N2 发现完全一致。我在引用层面指出缺少 GAE 引用，R1 在实验层面指出缺少 GAE baseline。两个问题指向同一个根本缺陷：**论文声称解决 credit assignment 问题，却完全忽略了 RL 社区 30 年来为此开发的标准工具**。

具体而言，论文只对比了两个极端：
- Step-independent（完全不考虑时序结构）→ 0%
- Episode-level（完全抹平时序结构）→ 24.3%

但中间存在大量标准方法：
- GAE (λ=0.95)：保留时序结构但 bias-variance tradeoff
- Reward shaping：在 intermediate steps 提供 potential-based shaping
- n-step returns：可变 horizon 的 bootstrapping

如果 GAE 在同样设置下也能解决问题（甚至效果更好），"episode-level GRPO" 就不是一个有价值的 contribution，而只是已有方法的一个特例（GAE with λ=1, γ=1）。

---

### Should-Fix 问题

**[AGREE] R1-W1: h-sweep 除 h=full 外均为 single seed**

同意。h-sweep 是论文的重要实验贡献之一（我列为 Contribution 3），但如果只有 single seed，"sharp cliff at h<5" 可能只是单次实验的噪声。特别是 h=5 和 h=6 之间如果差异不大，cliff 的位置就不确定。需要至少 3 seeds per h value 才能确认 cliff 的存在和位置。

**[AGREE] R1-W2: Cross-env 和 model scale 疑似 single seed**

同意。跨环境泛化（ScienceWorld 15% vs 2%）和跨规模泛化（Qwen3-7B 38% vs 5%）是论文 Contribution (4) 的支撑。Single seed 下这些数字缺乏统计意义。这进一步削弱了论文的 generalization claim。

**[AGREE] R1-W3: Per-task r=-0.42 with n=6 未达显著**

同意。n=6 时 Pearson r 的双尾 critical value (α=0.05) 约为 0.81。r=-0.42 远未达到。论文如果基于这个 correlation 做任何 claim，都是统计上不成立的。这个问题属于方法论疏忽——作者应该知道小样本 correlation 的 power 极低。

**[AGREE] R1-W4: 绝对性能偏低（24.3% vs SoTA 40-70%+）**

强烈同意，这与我的 R2-N3 完全对应。我指出 Self-Guide 用同样的 Qwen-1.7B 在 ALFWorld 达到 72.7%，是本文的 3 倍。R1 也独立发现了这个问题。两位 reviewer 都认为绝对性能差距需要解释，特别是当论文 claim "eliminates the bottleneck" 时。

补充：如果论文能诚实地 position 为 "analysis paper that identifies why naive GRPO fails in multi-turn setting, and shows episode-level aggregation as necessary (though not sufficient) condition"，这个问题会大幅缓解。但当前 framing 暗示 episode-level GRPO 是一个 solution，而非一个 necessary condition。

---

### 小问题

**[AGREE]** "References 只有 10 条" — 与我的 R2-N2 一致，不再赘述。

**[AGREE]** Table 3 correlation 计算方法和 GRPO 超参来源 — 属于 reproducibility 问题，合理关注。

---

### 总结

两位 Reviewer 的核心判断高度一致：

1. **理论贡献站不住**：R1 从公式严谨性角度质疑 γ^(T-h) 框架，我从新颖性角度指出这是教科书内容。两个批评叠加后，Contribution (1) "identify credit assignment decay" 基本不成立。

2. **实验贡献不充分**：R1 指出统计 power 不足和缺少中间 baseline，我指出与 Self-Guide 的巨大性能差距。论文的实验 story 既不 robust（统计）也不 competitive（绝对性能）。

3. **相关工作严重缺失**：两位 reviewer 都独立指出 10 引用过少，缺少 GAE 等核心方法。

综合两份审稿，我维持 **Reject** 的判断。论文需要：(a) 修正理论框架（搞清楚 step-independent training 的真实失败机制），(b) 加入 GAE 等标准 baseline，(c) 与 Self-Guide 进行 head-to-head 对比或清晰 differentiation，(d) 增加 seeds 到至少 5-8 个。这些修改的规模已超出 revision，更适合 resubmission。

---

[Reviewer 2 审稿结果]:
已提交交叉回应。对 Reviewer 1 的 3 个 Must-Fix 和 4 个 Should-Fix 全部 [AGREE]，核心判断一致：理论框架严谨性不足、统计 power 弱、缺少标准 baseline（GAE）、绝对性能与 Self-Guide 差距未解释。维持 Reject 判断。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 38 · 2026-05-17T00:35:16.287983+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/logs/chats/feishu_group_oc_648eaf83d2b24d445764257cf6a55525_reviewer_1.jsonl",
  "offset": "20",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/logs/chats/feishu_group_oc_648eaf83d2b24d445764257cf6a55525_reviewer_1.jsonl",
    "offset": "20",
    "limit": "50"
  }
}
```

</details>

---


### Tool result

_source line 39 · 2026-05-17T00:35:16.589963+00:00_

20	{"ts": "2026-05-17T00:32:01.593616+00:00", "role": "tool", "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:reviewer_1", "text": "called mcp__agent-ml-research__review_reviewer_post_to_director", "tool": "mcp__agent-ml-research__review_reviewer_post_to_director", "tool_args": {"text": "## 总体评分\n**Overall**: 3/6 (Borderline Reject)\n**一句话总结**: 论文识别了一个合理的问题，但核心理论公式存在严谨性问题，实验统计力不足以支撑其 claims，且 baseline 比较过于单薄。\n\n## 官方维度打分（参照 NeurIPS 2025/2026 Review Form）\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Quality (Soundness) | 2/5 | Eq.1 的 γ^(T-h) 公式化存在根本性问题（GRPO 是否真的使用 γ discount？）；3 seeds 的统计 power 极度不足 |\n| Clarity | 3/5 | 写作尚可，但核心方法的精确定义模糊（\"step-independent\" 的具体操作未明确） |\n| Significance | 3/5 | 问题方向重要（multi-turn agent RL 的 credit assignment），但绝对性能低（24.3%），实际意义有限 |\n| Originality | 3/5 | Episode-level GRPO 本身是一个自然的 baseline 选择而非真正的方法创新；主要贡献在于经验观察（h-cliff） |\n\n**Confidence**: 4/5 (对 RL 和 LLM agent 训练较为熟悉)\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] Eq.1 γ^(T-h) 公式化的严谨性存疑——GRPO 的标准公式不包含 γ discount\n\n- 具体位置：§3, Eq.1 (gradient signal decay), Eq.2 (credit assignment decay analysis)\n- 问题：标准 GRPO（DeepSeek-R1, Shao et al. 2024）的目标函数是 group-relative advantage，不含显式 γ discount factor。论文将 multi-turn credit assignment 问题框架化为 γ^(T-h) → 0 的指数衰减，但这一公式对应的是 standard discounted policy gradient with terminal reward 的情形。如果\"step-independent training\"实际操作是将 episode reward 均匀分配给每步（无 discounting），则不存在 γ^(T-h) 衰减；如果操作是标准 discounted RL，则修复方案应是调 γ 或用 GAE，而非切换到 episode-level。论文必须明确：(a) \"step-independent training\"的精确算法描述（reward 如何分配到每步？），(b) Eq.1 是严格数学推导还是类比？(c) 如果是类比，为何选择 γ^(T-h) 而非其他表达？\n- 为什么影响接收：这是论文的核心理论基础。如果 Eq.1 只是类比而非推导，则 \"credit assignment decay\" 的\"发现\"站不住脚，论文降级为纯经验观察。\n- 建议修改方向：给出 step-independent baseline 的完整算法伪代码；明确 γ 在具体实现中的角色（如果 γ=1 则无 decay）；如果 decay 来自其他机制（如 KL penalty 的累积效应或 gradient variance），应重新推导。\n\n**N2** [critical] 统计 Power 严重不足——3 seeds 的 95% CI 覆盖了从 \"几乎不工作\" 到 \"中等性能\" 的整个范围\n\n- 具体位置：§4.3, Table 2 (24.3% ± 6.0%, 3 seeds)\n- 问题：3 个种子
…[truncated 17804 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 40 · 2026-05-17T00:35:23.114753+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/logs/chats/feishu_group_oc_648eaf83d2b24d445764257cf6a55525_reviewer_1.jsonl",
  "offset": "28",
  "limit": "30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/logs/chats/feishu_group_oc_648eaf83d2b24d445764257cf6a55525_reviewer_1.jsonl",
    "offset": "28",
    "limit": "30"
  }
}
```

</details>

---


### Tool result

_source line 41 · 2026-05-17T00:35:23.165330+00:00_

&lt;system-reminder>Warning: the file exists but is shorter than the provided offset (28). The file has 28 lines.&lt;/system-reminder>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 42 · 2026-05-17T00:36:00.421752+00:00_

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
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
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

_source line 43 · 2026-05-17T00:36:00.472302+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 44 · 2026-05-17T00:36:06.758958+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
  "description": "Check if review_issues.yaml exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
    "description": "Check if review_issues.yaml exists"
  }
}
```

</details>

---


### Tool result

_source line 45 · 2026-05-17T00:36:06.961795+00:00_

FILE_NOT_FOUND

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "Bash",
  "elapsed_ms": 202
}
```

</details>

---


### Tool call

_source line 46 · 2026-05-17T00:36:56.273882+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "cost-verify-agent-rl",
  "issues_yaml": "## Review Issues Tracker — cost-verify-agent-rl\n## Round 1 (Dream Review, 2026-05-17)\n\n- id: \"R1-N1\"\n  summary: \"Eq.1 γ^(T-h) 理论公式与 GRPO 实际算法不匹配——GRPO 不含 γ discount\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R1 首先指出公式严谨性问题；R2 在交叉回应中 AGREE 并补充：如果 decay 机制不存在，Contribution (1) 从 '教科书知识应用' 进一步降级为 '错误类比的叙事包装'\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-N2\"\n  summary: \"统计 Power 全面不足——核心 claim 建立在 3 seeds (95% CI [9%,39%])，h-sweep/cross-env 均 single seed\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R1 计算 CI=[9.4%,39.2%]；R2 AGREE 并补充对 novelty 主要靠实验的论文，统计不可靠直接动摇全部贡献\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-N3\"\n  summary: \"Baseline 比较严重不足——缺少 GAE、γ=1、reward reshaping 等标准 credit assignment 方法\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R1 从实验层面指出缺少中间 baseline；R2 从引用层面指出缺少 GAE 文献。两者指向同一根本缺陷\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-N1\"\n  summary: \"核心新颖性不足——episode-level reward 是传统 RL default，贡献本质是发现 RAGEN 框架配置问题\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [2]\n      note: \"R2 指出 γ^(T-h) decay 是 Sutton & Barto Ch.13 基础内容，episode-level return (REINFORCE) 一直是 default。贡献更接近 technical report 级别\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-N2\"\n  summary: \"相关工作严重不足——10 篇引用缺 PPO/REINFORCE/GAE/HER/WebAgent/AgentTuning/FireAct/Reflexion 等\"\n  category: writing\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R2 详列缺失引用；R1 在 W4 中独立指出同一问题\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-N3\"\n  summary: \"与 Self-Guide (72.7% vs 24.3% 同模型同环境) 的性能差距未解释，model capacity 论点被反驳\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R2 指出 Self-Guide 直接反驳 model capacity bottleneck 论点；R1 在 W4 中独立指出绝对性能偏低\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W1\"\n  summary: \"Overclaiming: Introduction 说 'eliminates this bottleneck' 但只有 25% success\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [2]\n      note: \"应改为 mitigates/addresses；需区分 credit assignment bottleneck 与其他 bottlenecks\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W2\"\n  summary: \"Contribution (1) 与 Contribution (3) 冗余——h-sweep 是 credit assignment decay 的实验验证\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [2]\n      note: \"建议合并为一个 contribution\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W3\"\n  summary: \"Future directions 暴露 stepping-stone 定位——顶会论文应 self-contained\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [2]\n      note: \"提到 selective verification 需要 >40% base agent 暗示当前工作非 standalone contribution\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W1\"\n  summary: \"h-sweep 除 h=full 外均为 single seed，sharp cliff claim 不可靠\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R1 指出 6% noise 下 single seed 不足以确认 cliff；R2 AGREE\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W2\"\n  summary: \"Cross-env (Table 5) 和 model scale (Table 6) 疑似 single seed，泛化 claim 基础薄弱\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R2 AGREE\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W3\"\n  summary: \"Per-task r=-0.42 (n=6) 远未达统计显著 (critical ~0.81)\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R2 AGREE\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W5\"\n  summary: \"Negative results 未报告——selective verification/reward ablation 等方向的失败经验有信息量\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1]\n      note: \"NeurIPS 社区越来越欢迎 negative results reporting\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W4\"\n  summary: \"论文叙事从 selective verification 转型，可能有残留痕迹\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [2]\n      note: \"需检查 Abstract/Introduction 是否有 verification framing 残留\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "cost-verify-agent-rl",
    "issues_yaml": "## Review Issues Tracker — cost-verify-agent-rl\n## Round 1 (Dream Review, 2026-05-17)\n\n- id: \"R1-N1\"\n  summary: \"Eq.1 γ^(T-h) 理论公式与 GRPO 实际算法不匹配——GRPO 不含 γ discount\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R1 首先指出公式严谨性问题；R2 在交叉回应中 AGREE 并补充：如果 decay 机制不存在，Contribution (1) 从 '教科书知识应用' 进一步降级为 '错误类比的叙事包装'\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-N2\"\n  summary: \"统计 Power 全面不足——核心 claim 建立在 3 seeds (95% CI [9%,39%])，h-sweep/cross-env 均 single seed\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R1 计算 CI=[9.4%,39.2%]；R2 AGREE 并补充对 novelty 主要靠实验的论文，统计不可靠直接动摇全部贡献\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-N3\"\n  summary: \"Baseline 比较严重不足——缺少 GAE、γ=1、reward reshaping 等标准 credit assignment 方法\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R1 从实验层面指出缺少中间 baseline；R2 从引用层面指出缺少 GAE 文献。两者指向同一根本缺陷\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-N1\"\n  summary: \"核心新颖性不足——episode-level reward 是传统 RL default，贡献本质是发现 RAGEN 框架配置问题\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [2]\n      note: \"R2 指出 γ^(T-h) decay 是 Sutton & Barto Ch.13 基础内容，episode-level return (REINFORCE) 一直是 default。贡献更接近 technical report 级别\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-N2\"\n  summary: \"相关工作严重不足——10 篇引用缺 PPO/REINFORCE/GAE/HER/WebAgent/AgentTuning/FireAct/Reflexion 等\"\n  category: writing\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R2 详列缺失引用；R1 在 W4 中独立指出同一问题\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-N3\"\n  summary: \"与 Self-Guide (72.7% vs 24.3% 同模型同环境) 的性能差距未解释，model capacity 论点被反驳\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R2 指出 Self-Guide 直接反驳 model capacity bottleneck 论点；R1 在 W4 中独立指出绝对性能偏低\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W1\"\n  summary: \"Overclaiming: Introduction 说 'eliminates this bottleneck' 但只有 25% success\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [2]\n      note: \"应改为 mitigates/addresses；需区分 credit assignment bottleneck 与其他 bottlenecks\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W2\"\n  summary: \"Contribution (1) 与 Contribution (3) 冗余——h-sweep 是 credit assignment decay 的实验验证\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [2]\n      note: \"建议合并为一个 contribution\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W3\"\n  summary: \"Future directions 暴露 stepping-stone 定位——顶会论文应 self-contained\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [2]\n      note: \"提到 selective verification 需要 >40% base agent 暗示当前工作非 standalone contribution\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W1\"\n  summary: \"h-sweep 除 h=full 外均为 single seed，sharp cliff claim 不可靠\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R1 指出 6% noise 下 single seed 不足以确认 cliff；R2 AGREE\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W2\"\n  summary: \"Cross-env (Table 5) 和 model scale (Table 6) 疑似 single seed，泛化 claim 基础薄弱\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R2 AGREE\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W3\"\n  summary: \"Per-task r=-0.42 (n=6) 远未达统计显著 (critical ~0.81)\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R2 AGREE\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W5\"\n  summary: \"Negative results 未报告——selective verification/reward ablation 等方向的失败经验有信息量\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1]\n      note: \"NeurIPS 社区越来越欢迎 negative results reporting\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W4\"\n  summary: \"论文叙事从 selective verification 转型，可能有残留痕迹\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [2]\n      note: \"需检查 Abstract/Introduction 是否有 verification framing 残留\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n"
  }
}
```

</details>

---


### Tool result

_source line 47 · 2026-05-17T00:36:56.324696+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/review_issues.yaml\", \"bytes\": 5348}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 48 · 2026-05-17T00:38:23.533886+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# 合并审稿报告 — Round 1 (Dream Review)\n\n**论文**：Episode-Level RL for Multi-Turn Agents: Why Step-Independent Training Fails and How to Fix It\n**日期**：2026-05-17\n**Reviewers**：R1（方法+实验）3/6 Borderline Reject, R2（新颖性+相关工作）4/10 Reject\n\n---\n\n## Summary\n\n论文识别了 multi-turn agent RL 训练中 step-independent reward assignment 的失败现象，提出 episode-level GRPO 作为替代方案。在 ALFWorld 和 ScienceWorld 上通过 h-sweep 和多 seed 实验验证了 episode-level 训练的优势（24.3% vs 0%）。跨环境和跨规模实验进一步验证泛化性。\n\n---\n\n## Strengths\n\n1. **问题方向有价值**：Multi-turn agent RL 的 credit assignment 是实际且重要的瓶颈 [R1, R2 共识]\n2. **h-sweep 实验范式有启发性**：通过 context window 大小扫描探测 credit assignment 行为是一个有信息量的实验设计 [R1, R2]\n3. **实验覆盖面有意识**：跨环境（ALFWorld→ScienceWorld）、跨规模（1.7B→7B）验证 [R1, R2]\n4. **结构紧凑**：8 页内完整呈现问题-方法-实验，无明显冗余 [R1]\n5. **实用价值**：对使用 RAGEN/GRPO 训练 multi-turn agent 的研究者有直接指导意义 [R2]\n\n---\n\n## Weaknesses（按严重性排序）\n\n### Critical（影响接收决定）\n\n**C1. Eq.1 γ^(T-h) 理论框架与 GRPO 实际算法不匹配** [R1-N1, R2 AGREE]\n- 标准 GRPO 使用 group-relative advantage A_i = (r_i - mean(r))/std(r)，不含显式 γ discount\n- 论文将问题框架化为 γ^(T-h) → 0 指数衰减，但这对应 standard discounted policy gradient，非 GRPO\n- 如果 Eq.1 只是类比而非推导，\"credit assignment decay\" 的\"发现\"不成立，论文核心理论贡献坍塌\n- **必须明确**：step-independent training 的精确算法伪代码 + γ 在实现中的角色 + Eq.1 是推导还是类比\n\n**C2. 核心新颖性不足** [R2-N1, R1 alignment]\n- Episode-level return 是 REINFORCE 的 default，非新方法\n- γ^(T-h) decay 是 Sutton & Barto Ch.13 eligibility traces 的基础内容\n- 实际贡献降级为\"发现 RAGEN 框架在 multi-turn 场景下有 bug-like behavior 并用标准方法修复\"\n- 更接近 technical report / workshop paper 级别\n\n**C3. 统计 Power 全面不足** [R1-N2, R2 AGREE]\n- 核心结果 24.3%±6.0% (3 seeds) → 95% CI = [9.4%, 39.2%]\n- h-sweep (Table 1) 除 h=full 外全部 single seed\n- Cross-env (Table 5) 和 model scale (Table 6) 疑似 single seed\n- Step-independent baseline 0% 未经多 seed 验证（可能是 single unlucky run）\n- Per-task r=-0.42 (n=6) 远未达统计显著 (critical value ~0.81)\n\n**C4. Baseline 比较严重不足** [R1-N3, R2 AGREE]\n- 只对比两个极端：step-independent vs episode-level\n- 缺少：GAE (λ=0.95)、γ=1 step-level GRPO、reward reshaping、hindsight credit assignment\n- 无法判断 episode-level 是否为唯一方案或仅为\"任何合理 credit assignment\"的特例\n\n**C5. 相关工作严重不足（10 引用）** [R2-N2, R1-W4]\n- 缺失：PPO、REINFORCE、GAE、HER (Andrychowicz 2017)、AgentQ（正文提及无引用条目）、WebAgent、AgentTuning、FireAct、Reflexion、Reward shaping (Ng 1999)\n- 对于涉及 RL + credit assignment + multi-turn agents + GRPO 的论文，引用覆盖度严重不足\n\n**C6. 与 Self-Guide 的性能差距未解释** [R2-N3, R1-W4]\n- Self-Guide 用同样的 Qwen-1.7B 在 ALFWorld 达到 72.7%（本文 24.3%，差 3 倍）\n- Discussion 中 \"model capacity is separate bottleneck\" 被 Self-Guide 直接反驳\n- 论文必须回答：同模型已有 72.7% 的方法存在时，为什么读者要关注 24.3% 的方法？\n\n### Warning（影响评分）\n\n**W1. Overclaiming**：\"eliminates this bottleneck\" 但只有 25% success [R2-W1]\n**W2. Contribution (1) 与 (3) 冗余**：h-sweep 本身就是 credit assignment decay 的验证 [R2-W2]\n**W3. Future directions 暴露 stepping-stone 定位**：提到 selective verification 需要 >40% base agent [R2-W3]\n**W4. h-sweep cliff claim 不可靠**：single seed + 6% noise band [R1-W1]\n**W5. 跨环境/跨规模泛化 claim 基础薄弱**：疑似 single seed [R1-W2]\n**W6. Negative results 未报告**：selective verification 等方向失败的信息未呈现 [R1-W5]\n**W7. 叙事转型痕迹可能残留**：从 selective verification 转为 pure training methodology [R2-W4]\n\n---\n\n## Reviewer Consensus\n\n两位 Reviewer 在所有关键问题上完全一致（R2 对 R1 全部 [AGREE]，无任何 [REBUT]）：\n\n| 问题 | R1 | R2 | 共识 |\n|------|----|----|------|\n| Eq.1 理论严谨性 | N1 (critical) | AGREE + 加强 | ✓ |\n| 统计 power 不足 | N2 (critical) | AGREE | ✓ |\n| 缺少标准 baseline | N3 (critical) | AGREE | ✓ |\n| 新颖性不足 | alignment | N1 (critical) | ✓ |\n| 引用不足 | W4 | N2 (critical) | ✓ |\n| Self-Guide 差距 | W4 | N3 (critical) | ✓ |\n| h-sweep single seed | W1 | AGREE | ✓ |\n| Per-task correlation | W3 | AGREE | ✓ |\n| 绝对性能低 | W4 | AGREE | ✓ |\n\n---\n\n## Reviewer Divergence\n\n无。两位 Reviewer 判断完全对齐。\n\n---\n\n## Questions（需作者澄清）\n\n1. \"Step-independent training\"的精确算法是什么？Reward 如何分配到每步？γ 的值是多少？\n2. Eq.1 是从 GRPO 目标函数严格推导，还是对 standard discounted PG 的类比？\n3. Step-independent baseline 的 0% 是在多少 seeds 上验证的？\n4. Self-Guide 与本文方法的本质区别是什么？为什么同模型性能差 3 倍？\n5. 为什么不尝试 GAE 或 γ=1 作为中间 baseline？\n6. h-sweep 的 cliff boundary (h=3-5) 是否在 multi-seed 下仍然 sharp？\n\n---\n\n## Missing References\n\n- PPO (Schulman et al. 2017)\n- REINFORCE (Williams 1992)\n- GAE (Schulman et al. 2015/2016)\n- HER (Andrychowicz et al. 2017)\n- AgentQ (具体引用缺失)\n- WebAgent (Gur et al. 2023)\n- AgentTuning (Zeng et al. 2023)\n- FireAct (Chen et al. 2023)\n- Reflexion (Shinn et al. 2023)\n- Reward Shaping (Ng et al. 1999)\n- AgentBench (Liu et al. 2023)\n- RLHF 基础文献 (Ouyang et al. 2022 / Ziegler et al. 2019)\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未请求。\n\n---\n\n## Overall Assessment\n\n**评分：Weak Reject**\n**置信度：High（两位 Reviewer 完全一致，confidence 均 4/5）**\n\n论文识别的问题方向有价值（multi-turn agent RL 的 credit assignment），但当前版本存在多个互相叠加的根本性缺陷：\n\n1. **理论贡献不成立**：Eq.1 公式化与 GRPO 实际算法不匹配 + episode-level return 是传统 RL default = 无 novelty\n2. **实验贡献不可靠**：统计 power 全面不足（3 seeds / single seed），claims 的置信区间过宽\n3. **对比不充分**：只比两个极端，缺标准方法；与 Self-Guide 的 3 倍性能差距未解释\n4. **学术规范不足**：10 引用远低于顶会标准，核心相关工作（GAE）完全缺失\n\n**建议**：(a) 搞清楚 step-independent training 失败的真实机制（可能不是 γ decay）；(b) 加入 GAE/γ=1 等标准 baseline 证明 episode-level 的独特价值；(c) 与 Self-Guide 做 head-to-head differentiation；(d) 所有关键实验增至 5-8 seeds；(e) 扩充引用至 30+ 篇。修改规模已超出 revision，建议 resubmission。\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- \"eliminates this bottleneck\" overclaims，改为 \"mitigates\"\n- Contribution (1) 和 (3) 可合并\n- 4 contributions 中 (1) 和 (2) 的独立性需重新审视\n\n### §2 Related Work\n- 需增加至少两个 subsection：Credit Assignment in RL + LLM Agent Training\n- AgentQ 提及但无引用条目\n- HER 提及但无 Andrychowicz 2017 引用\n\n### §3 Method\n- Eq.1: 必须明确是推导还是类比；给出 step-independent 的完整算法伪代码\n- Eq.2: γ^(T-h) decay analysis 需连接到 GRPO 的实际 advantage computation\n- Eq.3: Episode-level GRPO 的描述需与标准 REINFORCE 做差异化\n\n### §4 Experiments\n- Table 1: h-sweep cliff boundary 需 multi-seed 验证\n- Table 2: 3 seeds 不够，CI 过宽\n- Table 3: Correlation 统计方法不明\n- Table 4: verify vs no-verify +10pp 未做 significance test\n- Table 5-6: 需标注 seed 数量\n- Table 7: r=-0.42 (n=6) 不显著，删除 correlation claim\n- 整体缺少 GAE/γ=1 等中间 baseline\n\n### §5 Discussion\n- \"Model capacity is separate bottleneck\" 被 Self-Guide 反驳，需修改或删除\n- Negative results (selective verification 失败) 应简要报告\n- Future directions 不应暗示当前工作是 stepping stone\n\n### References\n- 10 → 至少 30-40，系统补充 RL foundations + agent training + benchmarks",
  "project": "cost-verify-agent-rl",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[2]",
  "overall_score": "weak reject",
  "review_chat_id": "oc_648eaf83d2b24d445764257cf6a55525"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# 合并审稿报告 — Round 1 (Dream Review)\n\n**论文**：Episode-Level RL for Multi-Turn Agents: Why Step-Independent Training Fails and How to Fix It\n**日期**：2026-05-17\n**Reviewers**：R1（方法+实验）3/6 Borderline Reject, R2（新颖性+相关工作）4/10 Reject\n\n---\n\n## Summary\n\n论文识别了 multi-turn agent RL 训练中 step-independent reward assignment 的失败现象，提出 episode-level GRPO 作为替代方案。在 ALFWorld 和 ScienceWorld 上通过 h-sweep 和多 seed 实验验证了 episode-level 训练的优势（24.3% vs 0%）。跨环境和跨规模实验进一步验证泛化性。\n\n---\n\n## Strengths\n\n1. **问题方向有价值**：Multi-turn agent RL 的 credit assignment 是实际且重要的瓶颈 [R1, R2 共识]\n2. **h-sweep 实验范式有启发性**：通过 context window 大小扫描探测 credit assignment 行为是一个有信息量的实验设计 [R1, R2]\n3. **实验覆盖面有意识**：跨环境（ALFWorld→ScienceWorld）、跨规模（1.7B→7B）验证 [R1, R2]\n4. **结构紧凑**：8 页内完整呈现问题-方法-实验，无明显冗余 [R1]\n5. **实用价值**：对使用 RAGEN/GRPO 训练 multi-turn agent 的研究者有直接指导意义 [R2]\n\n---\n\n## Weaknesses（按严重性排序）\n\n### Critical（影响接收决定）\n\n**C1. Eq.1 γ^(T-h) 理论框架与 GRPO 实际算法不匹配** [R1-N1, R2 AGREE]\n- 标准 GRPO 使用 group-relative advantage A_i = (r_i - mean(r))/std(r)，不含显式 γ discount\n- 论文将问题框架化为 γ^(T-h) → 0 指数衰减，但这对应 standard discounted policy gradient，非 GRPO\n- 如果 Eq.1 只是类比而非推导，\"credit assignment decay\" 的\"发现\"不成立，论文核心理论贡献坍塌\n- **必须明确**：step-independent training 的精确算法伪代码 + γ 在实现中的角色 + Eq.1 是推导还是类比\n\n**C2. 核心新颖性不足** [R2-N1, R1 alignment]\n- Episode-level return 是 REINFORCE 的 default，非新方法\n- γ^(T-h) decay 是 Sutton & Barto Ch.13 eligibility traces 的基础内容\n- 实际贡献降级为\"发现 RAGEN 框架在 multi-turn 场景下有 bug-like behavior 并用标准方法修复\"\n- 更接近 technical report / workshop paper 级别\n\n**C3. 统计 Power 全面不足** [R1-N2, R2 AGREE]\n- 核心结果 24.3%±6.0% (3 seeds) → 95% CI = [9.4%, 39.2%]\n- h-sweep (Table 1) 除 h=full 外全部 single seed\n- Cross-env (Table 5) 和 model scale (Table 6) 疑似 single seed\n- Step-independent baseline 0% 未经多 seed 验证（可能是 single unlucky run）\n- Per-task r=-0.42 (n=6) 远未达统计显著 (critical value ~0.81)\n\n**C4. Baseline 比较严重不足** [R1-N3, R2 AGREE]\n- 只对比两个极端：step-independent vs episode-level\n- 缺少：GAE (λ=0.95)、γ=1 step-level GRPO、reward reshaping、hindsight credit assignment\n- 无法判断 episode-level 是否为唯一方案或仅为\"任何合理 credit assignment\"的特例\n\n**C5. 相关工作严重不足（10 引用）** [R2-N2, R1-W4]\n- 缺失：PPO、REINFORCE、GAE、HER (Andrychowicz 2017)、AgentQ（正文提及无引用条目）、WebAgent、AgentTuning、FireAct、Reflexion、Reward shaping (Ng 1999)\n- 对于涉及 RL + credit assignment + multi-turn agents + GRPO 的论文，引用覆盖度严重不足\n\n**C6. 与 Self-Guide 的性能差距未解释** [R2-N3, R1-W4]\n- Self-Guide 用同样的 Qwen-1.7B 在 ALFWorld 达到 72.7%（本文 24.3%，差 3 倍）\n- Discussion 中 \"model capacity is separate bottleneck\" 被 Self-Guide 直接反驳\n- 论文必须回答：同模型已有 72.7% 的方法存在时，为什么读者要关注 24.3% 的方法？\n\n### Warning（影响评分）\n\n**W1. Overclaiming**：\"eliminates this bottleneck\" 但只有 25% success [R2-W1]\n**W2. Contribution (1) 与 (3) 冗余**：h-sweep 本身就是 credit assignment decay 的验证 [R2-W2]\n**W3. Future directions 暴露 stepping-stone 定位**：提到 selective verification 需要 >40% base agent [R2-W3]\n**W4. h-sweep cliff claim 不可靠**：single seed + 6% noise band [R1-W1]\n**W5. 跨环境/跨规模泛化 claim 基础薄弱**：疑似 single seed [R1-W2]\n**W6. Negative results 未报告**：selective verification 等方向失败的信息未呈现 [R1-W5]\n**W7. 叙事转型痕迹可能残留**：从 selective verification 转为 pure training methodology [R2-W4]\n\n---\n\n## Reviewer Consensus\n\n两位 Reviewer 在所有关键问题上完全一致（R2 对 R1 全部 [AGREE]，无任何 [REBUT]）：\n\n| 问题 | R1 | R2 | 共识 |\n|------|----|----|------|\n| Eq.1 理论严谨性 | N1 (critical) | AGREE + 加强 | ✓ |\n| 统计 power 不足 | N2 (critical) | AGREE | ✓ |\n| 缺少标准 baseline | N3 (critical) | AGREE | ✓ |\n| 新颖性不足 | alignment | N1 (critical) | ✓ |\n| 引用不足 | W4 | N2 (critical) | ✓ |\n| Self-Guide 差距 | W4 | N3 (critical) | ✓ |\n| h-sweep single seed | W1 | AGREE | ✓ |\n| Per-task correlation | W3 | AGREE | ✓ |\n| 绝对性能低 | W4 | AGREE | ✓ |\n\n---\n\n## Reviewer Divergence\n\n无。两位 Reviewer 判断完全对齐。\n\n---\n\n## Questions（需作者澄清）\n\n1. \"Step-independent training\"的精确算法是什么？Reward 如何分配到每步？γ 的值是多少？\n2. Eq.1 是从 GRPO 目标函数严格推导，还是对 standard discounted PG 的类比？\n3. Step-independent baseline 的 0% 是在多少 seeds 上验证的？\n4. Self-Guide 与本文方法的本质区别是什么？为什么同模型性能差 3 倍？\n5. 为什么不尝试 GAE 或 γ=1 作为中间 baseline？\n6. h-sweep 的 cliff boundary (h=3-5) 是否在 multi-seed 下仍然 sharp？\n\n---\n\n## Missing References\n\n- PPO (Schulman et al. 2017)\n- REINFORCE (Williams 1992)\n- GAE (Schulman et al. 2015/2016)\n- HER (Andrychowicz et al. 2017)\n- AgentQ (具体引用缺失)\n- WebAgent (Gur et al. 2023)\n- AgentTuning (Zeng et al. 2023)\n- FireAct (Chen et al. 2023)\n- Reflexion (Shinn et al. 2023)\n- Reward Shaping (Ng et al. 1999)\n- AgentBench (Liu et al. 2023)\n- RLHF 基础文献 (Ouyang et al. 2022 / Ziegler et al. 2019)\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未请求。\n\n---\n\n## Overall Assessment\n\n**评分：Weak Reject**\n**置信度：High（两位 Reviewer 完全一致，confidence 均 4/5）**\n\n论文识别的问题方向有价值（multi-turn agent RL 的 credit assignment），但当前版本存在多个互相叠加的根本性缺陷：\n\n1. **理论贡献不成立**：Eq.1 公式化与 GRPO 实际算法不匹配 + episode-level return 是传统 RL default = 无 novelty\n2. **实验贡献不可靠**：统计 power 全面不足（3 seeds / single seed），claims 的置信区间过宽\n3. **对比不充分**：只比两个极端，缺标准方法；与 Self-Guide 的 3 倍性能差距未解释\n4. **学术规范不足**：10 引用远低于顶会标准，核心相关工作（GAE）完全缺失\n\n**建议**：(a) 搞清楚 step-independent training 失败的真实机制（可能不是 γ decay）；(b) 加入 GAE/γ=1 等标准 baseline 证明 episode-level 的独特价值；(c) 与 Self-Guide 做 head-to-head differentiation；(d) 所有关键实验增至 5-8 seeds；(e) 扩充引用至 30+ 篇。修改规模已超出 revision，建议 resubmission。\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- \"eliminates this bottleneck\" overclaims，改为 \"mitigates\"\n- Contribution (1) 和 (3) 可合并\n- 4 contributions 中 (1) 和 (2) 的独立性需重新审视\n\n### §2 Related Work\n- 需增加至少两个 subsection：Credit Assignment in RL + LLM Agent Training\n- AgentQ 提及但无引用条目\n- HER 提及但无 Andrychowicz 2017 引用\n\n### §3 Method\n- Eq.1: 必须明确是推导还是类比；给出 step-independent 的完整算法伪代码\n- Eq.2: γ^(T-h) decay analysis 需连接到 GRPO 的实际 advantage computation\n- Eq.3: Episode-level GRPO 的描述需与标准 REINFORCE 做差异化\n\n### §4 Experiments\n- Table 1: h-sweep cliff boundary 需 multi-seed 验证\n- Table 2: 3 seeds 不够，CI 过宽\n- Table 3: Correlation 统计方法不明\n- Table 4: verify vs no-verify +10pp 未做 significance test\n- Table 5-6: 需标注 seed 数量\n- Table 7: r=-0.42 (n=6) 不显著，删除 correlation claim\n- 整体缺少 GAE/γ=1 等中间 baseline\n\n### §5 Discussion\n- \"Model capacity is separate bottleneck\" 被 Self-Guide 反驳，需修改或删除\n- Negative results (selective verification 失败) 应简要报告\n- Future directions 不应暗示当前工作是 stepping stone\n\n### References\n- 10 → 至少 30-40，系统补充 RL foundations + agent training + benchmarks",
    "project": "cost-verify-agent-rl",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[2]",
    "overall_score": "weak reject",
    "review_chat_id": "oc_648eaf83d2b24d445764257cf6a55525"
  }
}
```

</details>

---


### Tool result

_source line 49 · 2026-05-17T00:38:23.584802+00:00_

{"result":"{\"success\": false, \"data\": {\"expected_reviewer_ids\": [1, 2], \"cross_missing\": [1]}, \"error\": \"cross-sharing incomplete — reviewer(s) [1] have NOT submitted cross-responses. Before submitting the report, you must complete Step 2: send each reviewer's original report to all other reviewers via director_post_to_reviewer, then wait for every reviewer to respond with [AGREE]/[REBUT] via review_reviewer_post_to_director. All 2 reviewers ([1, 2]) must have cross-responded.\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 50 · 2026-05-17T00:38:42.704815+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "[Step 2 交叉回应 — 紧急催促]\n\nReviewer 1，你已收到 Reviewer 2 的审稿意见但尚未提交交叉回应。请立即完成。\n\nReviewer 2 的核心判断（4/10 Reject）：\n- N1: 核心新颖性不足——episode-level reward 是传统 RL default，Contribution (1) \"identify credit assignment decay\" 是教科书内容 (Sutton & Barto Ch.13)\n- N2: 相关工作严重不足——10 引用缺 PPO/GAE/REINFORCE/HER/WebAgent/AgentTuning/FireAct/Reflexion\n- N3: 与 Self-Guide (72.7% vs 24.3% 同模型同环境) 性能差距未解释，\"model capacity bottleneck\" 论点被直接反驳\n- W1: Overclaiming \"eliminates this bottleneck\" vs 25% success\n- W2: Contribution (1) 与 (3) 冗余\n- W3: Future directions 暴露 stepping-stone 定位\n- W4: 论文叙事转型痕迹\n\n请对每个问题逐条给出 [AGREE] 或 [REBUT]。结合你自己的审稿发现说明理由。你的初审已指出 Eq.1 理论问题 + 统计 power 不足 + baseline 单薄——这些与 R2 的发现如何互相支撑或矛盾？\n\n通过 `review_reviewer_post_to_director(text, reviewer_id=\"1\", project=\"cost-verify-agent-rl\", dream_id=\"20260516T235255\")` 提交。",
  "project": "cost-verify-agent-rl",
  "chat_id": "oc_648eaf83d2b24d445764257cf6a55525",
  "director_session_key": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "[Step 2 交叉回应 — 紧急催促]\n\nReviewer 1，你已收到 Reviewer 2 的审稿意见但尚未提交交叉回应。请立即完成。\n\nReviewer 2 的核心判断（4/10 Reject）：\n- N1: 核心新颖性不足——episode-level reward 是传统 RL default，Contribution (1) \"identify credit assignment decay\" 是教科书内容 (Sutton & Barto Ch.13)\n- N2: 相关工作严重不足——10 引用缺 PPO/GAE/REINFORCE/HER/WebAgent/AgentTuning/FireAct/Reflexion\n- N3: 与 Self-Guide (72.7% vs 24.3% 同模型同环境) 性能差距未解释，\"model capacity bottleneck\" 论点被直接反驳\n- W1: Overclaiming \"eliminates this bottleneck\" vs 25% success\n- W2: Contribution (1) 与 (3) 冗余\n- W3: Future directions 暴露 stepping-stone 定位\n- W4: 论文叙事转型痕迹\n\n请对每个问题逐条给出 [AGREE] 或 [REBUT]。结合你自己的审稿发现说明理由。你的初审已指出 Eq.1 理论问题 + 统计 power 不足 + baseline 单薄——这些与 R2 的发现如何互相支撑或矛盾？\n\n通过 `review_reviewer_post_to_director(text, reviewer_id=\"1\", project=\"cost-verify-agent-rl\", dream_id=\"20260516T235255\")` 提交。",
    "project": "cost-verify-agent-rl",
    "chat_id": "oc_648eaf83d2b24d445764257cf6a55525",
    "director_session_key": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director"
  }
}
```

</details>

---


### Tool result

_source line 51 · 2026-05-17T00:38:46.424200+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_648eaf83d2b24d445764257cf6a55525:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 3719
}
```

</details>

---


### Assistant

_source line 52 · 2026-05-17T00:38:50.659985+00:00_

等待 Reviewer 1 完成交叉回应后即可提交最终报告。报告已准备就绪，Issue Tracker 已更新。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director"
}
```

</details>

---


## Round 6

## Round 6

4 recorded events


### User

_source line 53 · 2026-05-17T00:38:51.729235+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应

---

### Must-Fix 问题

**[AGREE] R2-N1: 核心新颖性不足——episode-level reward 是传统 RL default**

同意，且与我的 N1 形成互补打击。我的 N1 指出 Eq.1 γ^(T-h) 公式化与 GRPO 标准算法不一致（GRPO 无显式 γ discount）；R2-N1 进一步指出，即使该公式成立，这也是 Sutton & Barto [10] Ch.13 的教科书内容。两个问题叠加后结论更强：

1. 如果 GRPO 不使用 γ → Eq.1 的 "发现" 是对算法的误读
2. 如果确实存在 γ decay → 这是 1988 年就已知的现象，不构成 contribution

论文真正的贡献应诚实定位为：**在 LLM agent RL 的具体工程实践中（如 RAGEN 框架），step-level training 的默认配置会导致失败，episode-level 是一个简单有效的修复**。这确实更接近 technical report / workshop paper 级别。

补充一点：论文如果能深入回答"为什么 LLM agent 社区会默认走向 step-independent training（而传统 RL 不会）"——例如是因为 LLM 的 context window 限制、token-level loss 的惯性、或框架设计的偶然选择——这个分析本身可能构成更有价值的贡献。

---

**[AGREE] R2-N2: 10 篇引用严重不足**

完全同意。我在 W4 中已独立提出相同问题。补充 R2 列出的缺失引用清单：

- RL foundations: PPO (Schulman 2017), REINFORCE (Williams 1992), GAE (Schulman 2016)
- Credit assignment classics: Reward shaping (Ng et al. 1999), Hindsight Experience Replay (Andrychowicz 2017)
- Agent training: AgentTuning, FireAct, Reflexion (Shinn 2023), AgentQ
- Agent benchmarks: WebShop, AgentBench, InterCode

对于声称解决 "credit assignment" 问题的论文，不引用 GAE 和 reward shaping 经典文献是不可接受的。

---

**[AGREE with nuance] R2-N3: Self-Guide 72.7% vs 本文 24.3% 的对比**

大体同意这是一个严重问题，但需要区分两种可能情况：

**如果 Self-Guide 使用纯 RL（无 expert demonstrations）**：则本文的方法在相同模型上性能差 3 倍，"model capacity bottleneck" 的辩护被直接推翻，论文的实用意义归零。

**如果 Self-Guide 使用 SFT + expert trajectories**：则对比不完全公平——expert-guided training vs from-scratch RL 是不同 paradigm。但即便如此，论文必须在 §5 Discussion 中正面回应：(a) 明确两种方法的训练 paradigm 差异，(b) 解释为什么读者应该关注 from-scratch RL 的 24.3% 而非 expert-guided 的 72.7%，(c) 是否有场景下 expert demonstrations 不可得而纯 RL 是唯一选择。

无论哪种情况，论文当前 §5 的 "model capacity is separate bottleneck" 说法至少是 incomplete——Self-Guide [2] 用相同模型证明 capacity 够用，论文必须正面回应而非回避。这与我的 W4（绝对性能偏低需定位）直接相关。

---

### Should-Fix 问题

**[AGREE] R2-W1: "eliminates this bottleneck" overclaiming vs 25% success**

完全同意。与我的 N2（统计 CI 极宽 [9%, 39%]）联合来看更严重：论文不仅 success rate 低，且对这个低数字的估计还极不确定。"eliminates"暗示问题完全解决，但 25% success + wide CI 说明 bottleneck 只是部分缓解。

建议措辞改为 "significantly alleviates" 或 "enables non-zero learning"。

---

**[PARTIALLY AGREE] R2-W2: Contribution (1) 与 (3) 冗余/循环**

部分同意。Contribution (1) = "identify credit assignment decay"，Contribution (3) = "h-sweep reveals cliff at h<5"。(3) 确实是 (1) 的实验证据而非独立贡献，将证据和结论分列为两条 contribution 有凑数嫌疑。

但我认为 h-sweep 作为 experimental methodology（用 context window 大小扫描来诊断 credit assignment 行为）本身有独立价值——前提是它有足够的统计支撑（回到我的 W1：single seed 不够）。如果增加 seeds 后 cliff 稳健存在，(3) 可以独立成立为 "empirical characterization contribution"。

---

**[AGREE] R2-W3: Future directions 暴露 stepping-stone 定位**

同意。如果 §5 Future Work 列出了大量 "下一步应该做" 的方向（如 more sophisticated credit assignment、reward redistribution、larger scale），这实际上是在告诉审稿人：当前论文只完成了一个最简方案（episode-level），真正有意义的工作还没做。对于 NeurIPS/ICML 正文论文，读者期望的是一个相对完整的解决方案，而非一个 preliminary observation + 最简 fix。

---

**[PARTIALLY AGREE] R2-W4: 叙事转型痕迹**

我无法从论文摘要/结构描述中直接验证这一点（需要阅读 PDF 全文）。但基于 review_context.yaml 显示论文确实经历了从 selective verification 到 pure training methodology 的重大转型，残留不一致是高概率事件。如果 §4.5 Table 4 (Verification Value) 仍然存在但与当前 "纯 training methodology" 定位不完全匹配，这可能是转型痕迹。

建议 Director 关注 §4.5 与整体叙事的一致性。

---

## 综合判断

R2 和我（R1）的意见高度一致，形成互补：
- **理论基础**：R1 从技术角度质疑 Eq.1 与 GRPO 的对应关系，R2 从新颖性角度指出即使正确也是教科书内容 → 两者叠加，论文的理论贡献几乎归零
- **实验说服力**：R1 质疑统计 power 和 baseline 不足，R2 质疑与 Self-Guide 72.7% 的 performance gap → 两者叠加，论文的实验贡献也大幅削弱
- **定位问题**：R2 明确指出 workshop/technical report 级别，与 R1 的 3/6 Borderline Reject 一致

**共识建议**：论文需要 (1) 诚实重新定位贡献——不是"发现了新问题"而是"在 LLM agent RL 工程中验证了经典解决方案的有效性"，(2) 大幅增加实验规模和 baselines，(3) 正面回应 Self-Guide 的 performance gap。

---

[Reviewer 1 审稿结果]:
交叉回应已提交。R1 和 R2 在核心问题上高度一致：理论基础薄弱（Eq.1 严谨性 + 教科书内容）、统计力不足、baseline 缺失、Self-Guide 72.7% 的性能差距未回应。综合判断维持 Borderline Reject。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 54 · 2026-05-17T00:40:43.103899+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# 合并审稿报告 — Round 1 (Dream Review)\n\n**论文**：Episode-Level RL for Multi-Turn Agents: Why Step-Independent Training Fails and How to Fix It\n**日期**：2026-05-17\n**Reviewers**：R1（方法+实验）3/6 Borderline Reject, R2（新颖性+相关工作）4/10 Reject\n\n---\n\n## Summary\n\n论文识别了 multi-turn agent RL 训练中 step-independent reward assignment 的失败现象，提出 episode-level GRPO 作为替代方案。在 ALFWorld 和 ScienceWorld 上通过 h-sweep 和多 seed 实验验证了 episode-level 训练的优势（24.3% vs 0%）。跨环境和跨规模实验进一步验证泛化性。\n\n---\n\n## Strengths\n\n1. **问题方向有价值**：Multi-turn agent RL 的 credit assignment 是实际且重要的瓶颈 [R1, R2 共识]\n2. **h-sweep 实验范式有启发性**：通过 context window 大小扫描探测 credit assignment 行为是一个有信息量的实验设计 [R1, R2]\n3. **实验覆盖面有意识**：跨环境（ALFWorld→ScienceWorld）、跨规模（1.7B→7B）验证 [R1, R2]\n4. **结构紧凑**：8 页内完整呈现问题-方法-实验，无明显冗余 [R1]\n5. **实用价值**：对使用 RAGEN/GRPO 训练 multi-turn agent 的研究者有直接指导意义 [R2]\n\n---\n\n## Weaknesses（按严重性排序）\n\n### Critical（影响接收决定）\n\n**C1. Eq.1 γ^(T-h) 理论框架与 GRPO 实际算法不匹配** [R1-N1, R2 AGREE]\n- 标准 GRPO 使用 group-relative advantage A_i = (r_i - mean(r))/std(r)，不含显式 γ discount\n- 论文将问题框架化为 γ^(T-h) → 0 指数衰减，但这对应 standard discounted policy gradient，非 GRPO\n- 如果 Eq.1 只是类比而非推导，\"credit assignment decay\" 的\"发现\"不成立，论文核心理论贡献坍塌\n- **必须明确**：step-independent training 的精确算法伪代码 + γ 在实现中的角色 + Eq.1 是推导还是类比\n\n**C2. 核心新颖性不足** [R2-N1, R1 AGREE]\n- Episode-level return 是 REINFORCE 的 default，非新方法\n- γ^(T-h) decay 是 Sutton & Barto Ch.13 eligibility traces 的基础内容\n- 实际贡献降级为\"发现 RAGEN 框架在 multi-turn 场景下有 bug-like behavior 并用标准方法修复\"\n- R1 补充：如果论文能深入分析\"为什么 LLM agent 社区默认走向 step-independent training\"（context window 限制？token-level loss 惯性？框架设计偶然？），该分析本身可能构成更有价值的贡献\n\n**C3. 统计 Power 全面不足** [R1-N2, R2 AGREE]\n- 核心结果 24.3%±6.0% (3 seeds) → 95% CI = [9.4%, 39.2%]\n- h-sweep (Table 1) 除 h=full 外全部 single seed\n- Cross-env (Table 5) 和 model scale (Table 6) 疑似 single seed\n- Step-independent baseline 0% 未经多 seed 验证（可能是 single unlucky run）\n- Per-task r=-0.42 (n=6) 远未达统计显著 (critical value ~0.81, p≈0.41)\n\n**C4. Baseline 比较严重不足** [R1-N3, R2 AGREE]\n- 只对比两个极端：step-independent vs episode-level\n- 缺少：GAE (λ=0.95)、γ=1 step-level GRPO、reward reshaping、hindsight credit assignment\n- 无法判断 episode-level 是否为唯一方案或仅为\"任何合理 credit assignment\"的特例（即 GAE with λ=1, γ=1）\n\n**C5. 相关工作严重不足（10 引用）** [R2-N2, R1 AGREE]\n- 缺失：PPO、REINFORCE、GAE、HER (Andrychowicz 2017)、AgentQ（正文提及无引用条目）、WebAgent、AgentTuning、FireAct、Reflexion、Reward shaping (Ng 1999)、AgentBench、WebShop、InterCode\n- 对于声称解决\"credit assignment\"问题的论文，不引用 GAE 和 reward shaping 经典文献不可接受\n\n**C6. 与 Self-Guide 的性能差距未解释** [R2-N3, R1 AGREE with nuance]\n- Self-Guide 用同样的 Qwen-1.7B 在 ALFWorld 达到 72.7%（本文 24.3%，差 3 倍）\n- Discussion 中 \"model capacity is separate bottleneck\" 被 Self-Guide 直接反驳\n- R1 补充：即使 Self-Guide 用了 expert demonstrations（不同 paradigm），论文仍必须正面回应——解释读者为何应关注 from-scratch RL 的 24.3%，以及何种场景下纯 RL 是唯一选择\n\n### Warning（影响评分）\n\n**W1. Overclaiming**：\"eliminates this bottleneck\" 但只有 25% success [R2-W1, R1 AGREE]\n- 叠加 CI [9%, 39%] 更严重——不仅 success rate 低，估计还极不确定\n- 建议改为 \"significantly alleviates\" 或 \"enables non-zero learning\"\n\n**W2. Contribution (1) 与 (3) 冗余** [R2-W2, R1 PARTIALLY AGREE]\n- (3) h-sweep 是 (1) credit assignment decay 的实验验证，分列有凑数嫌疑\n- R1 指出：如果增加 seeds 后 cliff 稳健存在，(3) 可独立为 \"empirical characterization contribution\"——前提是统计支撑到位\n\n**W3. Future directions 暴露 stepping-stone 定位** [R2-W3, R1 AGREE]\n- 列出大量\"下一步应该做\"的方向 = 告诉审稿人当前只完成最简方案\n\n**W4. h-sweep cliff claim 不可靠** [R1-W1, R2 AGREE]\n- Single seed + 6% noise band，cliff 可能是 artifact\n- 需 h=3,4,5 各跑 3 seeds 验证\n\n**W5. 跨环境/跨规模泛化 claim 基础薄弱** [R1-W2, R2 AGREE]\n- 疑似 single seed，single-number 对比不构成\"泛化\"证据\n\n**W6. Negative results 未报告** [R1-W5]\n- Selective verification/reward ablation 等方向的失败经验有信息量\n- NeurIPS 社区越来越欢迎 negative results reporting\n\n**W7. 叙事转型痕迹可能残留** [R2-W4, R1 PARTIALLY AGREE]\n- §4.5 Table 4 (Verification Value) 与当前\"纯 training methodology\"定位是否一致需审查\n\n---\n\n## Reviewer Consensus\n\n两位 Reviewer 在所有关键问题上完全一致（R2 对 R1 全部 [AGREE]，R1 对 R2 全部 [AGREE]/[PARTIALLY AGREE]，无任何 [REBUT]）：\n\n| 问题 | R1 | R2 | 交叉验证 |\n|------|----|----|----------|\n| Eq.1 理论严谨性 | N1 (critical) | AGREE + 加强 | 互补打击：技术+新颖性 |\n| 新颖性不足 | AGREE + 补充 | N1 (critical) | 教科书内容 + 框架 bug 修复 |\n| 统计 power 不足 | N2 (critical) | AGREE | CI [9%,39%] |\n| 缺少标准 baseline | N3 (critical) | AGREE | GAE 既缺引用也缺实验 |\n| 引用不足 | W4→AGREE | N2 (critical) | 10 vs 需要 30-50 |\n| Self-Guide 差距 | AGREE with nuance | N3 (critical) | 需正面回应 |\n| Overclaiming | AGREE | W1 | \"eliminates\" → \"alleviates\" |\n| h-sweep single seed | W1 | AGREE | cliff 可能 artifact |\n| Per-task correlation | W3 | AGREE | n=6, p≈0.41 |\n\n---\n\n## Reviewer Divergence\n\n无实质性分歧。R1 对 R2-N3 (Self-Guide) 有 nuance（区分了 expert-guided vs from-scratch RL 两种场景），但结论一致：论文必须正面回应。R1 对 R2-W2 (Contribution 冗余) 持部分异议：认为如果 h-sweep 统计支撑到位，可独立成立——但当前 single seed 下确实不成立。\n\n---\n\n## Questions（需作者澄清）\n\n1. \"Step-independent training\"的精确算法是什么？Reward 如何分配到每步？γ 的值是多少？请给出伪代码。\n2. Eq.1 是从 GRPO 目标函数严格推导，还是对 standard discounted PG 的类比？\n3. Step-independent baseline 的 0% 是在多少 seeds 上验证的？是 systematic failure 还是 single unlucky run？\n4. Self-Guide 与本文方法的本质区别是什么（training paradigm? data requirement?）？为什么同模型性能差 3 倍？\n5. 为什么不尝试 GAE (λ=0.95) 或 γ=1 作为中间 baseline？Episode-level GRPO 是否等价于 GAE(λ=1, γ=1)？\n6. h-sweep 的 cliff boundary (h=3-5) 是否在 multi-seed 下仍然 sharp？\n7. \"为什么 LLM agent 社区默认走向 step-independent training 而传统 RL 不会？\" 能否深入分析其 root cause？\n\n---\n\n## Missing References\n\n**RL Foundations**:\n- PPO (Schulman et al. 2017)\n- REINFORCE (Williams 1992)\n- GAE (Schulman et al. 2015/2016)\n\n**Credit Assignment Classics**:\n- Reward Shaping (Ng et al. 1999)\n- HER (Andrychowicz et al. 2017)\n\n**LLM Agent Training**:\n- AgentQ (具体引用缺失)\n- WebAgent (Gur et al. 2023)\n- AgentTuning (Zeng et al. 2023)\n- FireAct (Chen et al. 2023)\n- Reflexion (Shinn et al. 2023)\n\n**Agent Benchmarks**:\n- AgentBench (Liu et al. 2023)\n- WebShop (Yao et al. 2022)\n- InterCode (Yang et al. 2023)\n\n**RLHF**:\n- Ouyang et al. 2022 / Ziegler et al. 2019\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未请求。\n\n---\n\n## Overall Assessment\n\n**评分：Weak Reject**\n**置信度：High（两位 Reviewer 完全一致，confidence 均 4/5，交叉回应零 REBUT）**\n\n论文识别的问题方向有价值（multi-turn agent RL 的 credit assignment），但当前版本存在多个互相叠加的根本性缺陷：\n\n1. **理论贡献不成立**：Eq.1 公式化与 GRPO 不匹配（R1）+ 即使正确也是教科书内容（R2）= 理论 contribution 归零\n2. **实验贡献不可靠**：统计 power 全面不足，claims 的 CI 过宽，无法确认效果的稳健性\n3. **对比不充分**：只比两个极端缺标准方法（GAE）+ 与 Self-Guide 的 3 倍性能差距未解释\n4. **学术规范不足**：10 引用远低于顶会标准，核心相关工作完全缺失\n\n**两位 Reviewer 共识建议**：\n- 诚实重新定位贡献——不是\"发现了新问题\"而是\"在 LLM agent RL 工程实践中验证了经典解决方案的有效性\"\n- 深入分析\"为什么 LLM agent 社区默认采用 step-independent training\"作为真正有价值的贡献\n- 加入 GAE/γ=1 等标准 baseline 证明 episode-level 的独特价值\n- 与 Self-Guide 做 head-to-head differentiation 或明确 paradigm 差异\n- 所有关键实验增至 5-8 seeds\n- 扩充引用至 30+ 篇\n- 修改规模已超出 revision，建议 resubmission\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- \"eliminates this bottleneck\" overclaims，改为 \"alleviates\" / \"enables non-zero learning\"\n- Contribution (1) 和 (3) 建议合并（除非 h-sweep 获得多 seed 统计支撑）\n- 需铺垫\"为什么 LLM agent 社区默认 step-independent\"的分析\n\n### §2 Related Work\n- 需增加至少两个 subsection：Credit Assignment in RL (GAE/eligibility traces/reward shaping) + LLM Agent Training (WebAgent/AgentTuning/FireAct/Reflexion)\n- AgentQ 提及但无引用条目——引用错误\n- HER 提及但无 Andrychowicz 2017 引用\n- 需解释 episode-level GRPO 与 GAE(λ=1, γ=1) 的关系\n\n### §3 Method\n- Eq.1: 必须明确是推导还是类比；给出 step-independent 的完整算法伪代码\n- Eq.2: γ^(T-h) decay analysis 需连接到 GRPO 的实际 advantage computation——如果 GRPO 无 γ，decay 来自何处？\n- Eq.3: Episode-level GRPO 需与标准 REINFORCE 做差异化——否则\"贡献\"是\"用了 REINFORCE\"\n- 如果 decay 来自其他机制（reward dilution? KL 累积? gradient variance?），需重新推导并更新叙事\n\n### §4 Experiments\n- Table 1: h-sweep cliff boundary (h=3,4,5) 需 ≥3 seeds 验证\n- Table 2: 3 seeds → 5-8 seeds；step-independent 0% 也需多 seed 证明 systematic\n- Table 3: Correlation 统计方法未说明（Pearson/Spearman? 样本量?）\n- Table 4: verify vs no-verify +10pp 在 sd=6% noise 下需 significance test；§4.5 与\"纯 training methodology\"定位的一致性需审查\n- Table 5-6: 需标注 seed 数量；generalization claims 需 ≥3 seeds\n- Table 7: r=-0.42 (n=6) 不显著——删除 correlation claim 或增大样本量\n- 整体缺少 GAE(λ=0.95)/γ=1 step-level/reward reshaping 中间 baseline\n- 建议增加 \"Negative Results\" subsection 报告 selective verification 等失败方向\n\n### §5 Discussion\n- \"Model capacity is separate bottleneck\" 被 Self-Guide 反驳——需修改或删除，正面回应 performance gap\n- 如果 Self-Guide 用了 expert data，需明确本文方法的优势场景（何时 expert demonstrations 不可得）\n- Future directions 不应暗示当前工作是 stepping stone——强调独立价值\n- 建议加入 negative results 简述\n\n### References\n- 10 → 至少 30-40，系统补充 RL foundations + credit assignment classics + agent training concurrent work + benchmarks",
  "project": "cost-verify-agent-rl",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "weak reject",
  "review_chat_id": "oc_648eaf83d2b24d445764257cf6a55525"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# 合并审稿报告 — Round 1 (Dream Review)\n\n**论文**：Episode-Level RL for Multi-Turn Agents: Why Step-Independent Training Fails and How to Fix It\n**日期**：2026-05-17\n**Reviewers**：R1（方法+实验）3/6 Borderline Reject, R2（新颖性+相关工作）4/10 Reject\n\n---\n\n## Summary\n\n论文识别了 multi-turn agent RL 训练中 step-independent reward assignment 的失败现象，提出 episode-level GRPO 作为替代方案。在 ALFWorld 和 ScienceWorld 上通过 h-sweep 和多 seed 实验验证了 episode-level 训练的优势（24.3% vs 0%）。跨环境和跨规模实验进一步验证泛化性。\n\n---\n\n## Strengths\n\n1. **问题方向有价值**：Multi-turn agent RL 的 credit assignment 是实际且重要的瓶颈 [R1, R2 共识]\n2. **h-sweep 实验范式有启发性**：通过 context window 大小扫描探测 credit assignment 行为是一个有信息量的实验设计 [R1, R2]\n3. **实验覆盖面有意识**：跨环境（ALFWorld→ScienceWorld）、跨规模（1.7B→7B）验证 [R1, R2]\n4. **结构紧凑**：8 页内完整呈现问题-方法-实验，无明显冗余 [R1]\n5. **实用价值**：对使用 RAGEN/GRPO 训练 multi-turn agent 的研究者有直接指导意义 [R2]\n\n---\n\n## Weaknesses（按严重性排序）\n\n### Critical（影响接收决定）\n\n**C1. Eq.1 γ^(T-h) 理论框架与 GRPO 实际算法不匹配** [R1-N1, R2 AGREE]\n- 标准 GRPO 使用 group-relative advantage A_i = (r_i - mean(r))/std(r)，不含显式 γ discount\n- 论文将问题框架化为 γ^(T-h) → 0 指数衰减，但这对应 standard discounted policy gradient，非 GRPO\n- 如果 Eq.1 只是类比而非推导，\"credit assignment decay\" 的\"发现\"不成立，论文核心理论贡献坍塌\n- **必须明确**：step-independent training 的精确算法伪代码 + γ 在实现中的角色 + Eq.1 是推导还是类比\n\n**C2. 核心新颖性不足** [R2-N1, R1 AGREE]\n- Episode-level return 是 REINFORCE 的 default，非新方法\n- γ^(T-h) decay 是 Sutton & Barto Ch.13 eligibility traces 的基础内容\n- 实际贡献降级为\"发现 RAGEN 框架在 multi-turn 场景下有 bug-like behavior 并用标准方法修复\"\n- R1 补充：如果论文能深入分析\"为什么 LLM agent 社区默认走向 step-independent training\"（context window 限制？token-level loss 惯性？框架设计偶然？），该分析本身可能构成更有价值的贡献\n\n**C3. 统计 Power 全面不足** [R1-N2, R2 AGREE]\n- 核心结果 24.3%±6.0% (3 seeds) → 95% CI = [9.4%, 39.2%]\n- h-sweep (Table 1) 除 h=full 外全部 single seed\n- Cross-env (Table 5) 和 model scale (Table 6) 疑似 single seed\n- Step-independent baseline 0% 未经多 seed 验证（可能是 single unlucky run）\n- Per-task r=-0.42 (n=6) 远未达统计显著 (critical value ~0.81, p≈0.41)\n\n**C4. Baseline 比较严重不足** [R1-N3, R2 AGREE]\n- 只对比两个极端：step-independent vs episode-level\n- 缺少：GAE (λ=0.95)、γ=1 step-level GRPO、reward reshaping、hindsight credit assignment\n- 无法判断 episode-level 是否为唯一方案或仅为\"任何合理 credit assignment\"的特例（即 GAE with λ=1, γ=1）\n\n**C5. 相关工作严重不足（10 引用）** [R2-N2, R1 AGREE]\n- 缺失：PPO、REINFORCE、GAE、HER (Andrychowicz 2017)、AgentQ（正文提及无引用条目）、WebAgent、AgentTuning、FireAct、Reflexion、Reward shaping (Ng 1999)、AgentBench、WebShop、InterCode\n- 对于声称解决\"credit assignment\"问题的论文，不引用 GAE 和 reward shaping 经典文献不可接受\n\n**C6. 与 Self-Guide 的性能差距未解释** [R2-N3, R1 AGREE with nuance]\n- Self-Guide 用同样的 Qwen-1.7B 在 ALFWorld 达到 72.7%（本文 24.3%，差 3 倍）\n- Discussion 中 \"model capacity is separate bottleneck\" 被 Self-Guide 直接反驳\n- R1 补充：即使 Self-Guide 用了 expert demonstrations（不同 paradigm），论文仍必须正面回应——解释读者为何应关注 from-scratch RL 的 24.3%，以及何种场景下纯 RL 是唯一选择\n\n### Warning（影响评分）\n\n**W1. Overclaiming**：\"eliminates this bottleneck\" 但只有 25% success [R2-W1, R1 AGREE]\n- 叠加 CI [9%, 39%] 更严重——不仅 success rate 低，估计还极不确定\n- 建议改为 \"significantly alleviates\" 或 \"enables non-zero learning\"\n\n**W2. Contribution (1) 与 (3) 冗余** [R2-W2, R1 PARTIALLY AGREE]\n- (3) h-sweep 是 (1) credit assignment decay 的实验验证，分列有凑数嫌疑\n- R1 指出：如果增加 seeds 后 cliff 稳健存在，(3) 可独立为 \"empirical characterization contribution\"——前提是统计支撑到位\n\n**W3. Future directions 暴露 stepping-stone 定位** [R2-W3, R1 AGREE]\n- 列出大量\"下一步应该做\"的方向 = 告诉审稿人当前只完成最简方案\n\n**W4. h-sweep cliff claim 不可靠** [R1-W1, R2 AGREE]\n- Single seed + 6% noise band，cliff 可能是 artifact\n- 需 h=3,4,5 各跑 3 seeds 验证\n\n**W5. 跨环境/跨规模泛化 claim 基础薄弱** [R1-W2, R2 AGREE]\n- 疑似 single seed，single-number 对比不构成\"泛化\"证据\n\n**W6. Negative results 未报告** [R1-W5]\n- Selective verification/reward ablation 等方向的失败经验有信息量\n- NeurIPS 社区越来越欢迎 negative results reporting\n\n**W7. 叙事转型痕迹可能残留** [R2-W4, R1 PARTIALLY AGREE]\n- §4.5 Table 4 (Verification Value) 与当前\"纯 training methodology\"定位是否一致需审查\n\n---\n\n## Reviewer Consensus\n\n两位 Reviewer 在所有关键问题上完全一致（R2 对 R1 全部 [AGREE]，R1 对 R2 全部 [AGREE]/[PARTIALLY AGREE]，无任何 [REBUT]）：\n\n| 问题 | R1 | R2 | 交叉验证 |\n|------|----|----|----------|\n| Eq.1 理论严谨性 | N1 (critical) | AGREE + 加强 | 互补打击：技术+新颖性 |\n| 新颖性不足 | AGREE + 补充 | N1 (critical) | 教科书内容 + 框架 bug 修复 |\n| 统计 power 不足 | N2 (critical) | AGREE | CI [9%,39%] |\n| 缺少标准 baseline | N3 (critical) | AGREE | GAE 既缺引用也缺实验 |\n| 引用不足 | W4→AGREE | N2 (critical) | 10 vs 需要 30-50 |\n| Self-Guide 差距 | AGREE with nuance | N3 (critical) | 需正面回应 |\n| Overclaiming | AGREE | W1 | \"eliminates\" → \"alleviates\" |\n| h-sweep single seed | W1 | AGREE | cliff 可能 artifact |\n| Per-task correlation | W3 | AGREE | n=6, p≈0.41 |\n\n---\n\n## Reviewer Divergence\n\n无实质性分歧。R1 对 R2-N3 (Self-Guide) 有 nuance（区分了 expert-guided vs from-scratch RL 两种场景），但结论一致：论文必须正面回应。R1 对 R2-W2 (Contribution 冗余) 持部分异议：认为如果 h-sweep 统计支撑到位，可独立成立——但当前 single seed 下确实不成立。\n\n---\n\n## Questions（需作者澄清）\n\n1. \"Step-independent training\"的精确算法是什么？Reward 如何分配到每步？γ 的值是多少？请给出伪代码。\n2. Eq.1 是从 GRPO 目标函数严格推导，还是对 standard discounted PG 的类比？\n3. Step-independent baseline 的 0% 是在多少 seeds 上验证的？是 systematic failure 还是 single unlucky run？\n4. Self-Guide 与本文方法的本质区别是什么（training paradigm? data requirement?）？为什么同模型性能差 3 倍？\n5. 为什么不尝试 GAE (λ=0.95) 或 γ=1 作为中间 baseline？Episode-level GRPO 是否等价于 GAE(λ=1, γ=1)？\n6. h-sweep 的 cliff boundary (h=3-5) 是否在 multi-seed 下仍然 sharp？\n7. \"为什么 LLM agent 社区默认走向 step-independent training 而传统 RL 不会？\" 能否深入分析其 root cause？\n\n---\n\n## Missing References\n\n**RL Foundations**:\n- PPO (Schulman et al. 2017)\n- REINFORCE (Williams 1992)\n- GAE (Schulman et al. 2015/2016)\n\n**Credit Assignment Classics**:\n- Reward Shaping (Ng et al. 1999)\n- HER (Andrychowicz et al. 2017)\n\n**LLM Agent Training**:\n- AgentQ (具体引用缺失)\n- WebAgent (Gur et al. 2023)\n- AgentTuning (Zeng et al. 2023)\n- FireAct (Chen et al. 2023)\n- Reflexion (Shinn et al. 2023)\n\n**Agent Benchmarks**:\n- AgentBench (Liu et al. 2023)\n- WebShop (Yao et al. 2022)\n- InterCode (Yang et al. 2023)\n\n**RLHF**:\n- Ouyang et al. 2022 / Ziegler et al. 2019\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未请求。\n\n---\n\n## Overall Assessment\n\n**评分：Weak Reject**\n**置信度：High（两位 Reviewer 完全一致，confidence 均 4/5，交叉回应零 REBUT）**\n\n论文识别的问题方向有价值（multi-turn agent RL 的 credit assignment），但当前版本存在多个互相叠加的根本性缺陷：\n\n1. **理论贡献不成立**：Eq.1 公式化与 GRPO 不匹配（R1）+ 即使正确也是教科书内容（R2）= 理论 contribution 归零\n2. **实验贡献不可靠**：统计 power 全面不足，claims 的 CI 过宽，无法确认效果的稳健性\n3. **对比不充分**：只比两个极端缺标准方法（GAE）+ 与 Self-Guide 的 3 倍性能差距未解释\n4. **学术规范不足**：10 引用远低于顶会标准，核心相关工作完全缺失\n\n**两位 Reviewer 共识建议**：\n- 诚实重新定位贡献——不是\"发现了新问题\"而是\"在 LLM agent RL 工程实践中验证了经典解决方案的有效性\"\n- 深入分析\"为什么 LLM agent 社区默认采用 step-independent training\"作为真正有价值的贡献\n- 加入 GAE/γ=1 等标准 baseline 证明 episode-level 的独特价值\n- 与 Self-Guide 做 head-to-head differentiation 或明确 paradigm 差异\n- 所有关键实验增至 5-8 seeds\n- 扩充引用至 30+ 篇\n- 修改规模已超出 revision，建议 resubmission\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- \"eliminates this bottleneck\" overclaims，改为 \"alleviates\" / \"enables non-zero learning\"\n- Contribution (1) 和 (3) 建议合并（除非 h-sweep 获得多 seed 统计支撑）\n- 需铺垫\"为什么 LLM agent 社区默认 step-independent\"的分析\n\n### §2 Related Work\n- 需增加至少两个 subsection：Credit Assignment in RL (GAE/eligibility traces/reward shaping) + LLM Agent Training (WebAgent/AgentTuning/FireAct/Reflexion)\n- AgentQ 提及但无引用条目——引用错误\n- HER 提及但无 Andrychowicz 2017 引用\n- 需解释 episode-level GRPO 与 GAE(λ=1, γ=1) 的关系\n\n### §3 Method\n- Eq.1: 必须明确是推导还是类比；给出 step-independent 的完整算法伪代码\n- Eq.2: γ^(T-h) decay analysis 需连接到 GRPO 的实际 advantage computation——如果 GRPO 无 γ，decay 来自何处？\n- Eq.3: Episode-level GRPO 需与标准 REINFORCE 做差异化——否则\"贡献\"是\"用了 REINFORCE\"\n- 如果 decay 来自其他机制（reward dilution? KL 累积? gradient variance?），需重新推导并更新叙事\n\n### §4 Experiments\n- Table 1: h-sweep cliff boundary (h=3,4,5) 需 ≥3 seeds 验证\n- Table 2: 3 seeds → 5-8 seeds；step-independent 0% 也需多 seed 证明 systematic\n- Table 3: Correlation 统计方法未说明（Pearson/Spearman? 样本量?）\n- Table 4: verify vs no-verify +10pp 在 sd=6% noise 下需 significance test；§4.5 与\"纯 training methodology\"定位的一致性需审查\n- Table 5-6: 需标注 seed 数量；generalization claims 需 ≥3 seeds\n- Table 7: r=-0.42 (n=6) 不显著——删除 correlation claim 或增大样本量\n- 整体缺少 GAE(λ=0.95)/γ=1 step-level/reward reshaping 中间 baseline\n- 建议增加 \"Negative Results\" subsection 报告 selective verification 等失败方向\n\n### §5 Discussion\n- \"Model capacity is separate bottleneck\" 被 Self-Guide 反驳——需修改或删除，正面回应 performance gap\n- 如果 Self-Guide 用了 expert data，需明确本文方法的优势场景（何时 expert demonstrations 不可得）\n- Future directions 不应暗示当前工作是 stepping stone——强调独立价值\n- 建议加入 negative results 简述\n\n### References\n- 10 → 至少 30-40，系统补充 RL foundations + credit assignment classics + agent training concurrent work + benchmarks",
    "project": "cost-verify-agent-rl",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "weak reject",
    "review_chat_id": "oc_648eaf83d2b24d445764257cf6a55525"
  }
}
```

</details>

---


### Tool result

_source line 55 · 2026-05-17T00:40:47.221195+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_4ebf0fb2d0159caa355a1a855f5ac59f:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4117
}
```

</details>

---


### Assistant

_source line 56 · 2026-05-17T00:40:55.402271+00:00_

圆桌审稿完成。

**最终判断：Weak Reject**（两位 Reviewer 完全共识，零分歧）

6 个 Critical 问题：
1. Eq.1 γ^(T-h) 与 GRPO 算法不匹配——理论基础不成立
2. 核心新颖性不足——episode-level return 是传统 RL default
3. 统计 power 全面不足——3 seeds CI [9%,39%]
4. 缺少 GAE 等标准 credit assignment baseline
5. 10 引用严重不足
6. Self-Guide 72.7% vs 24.3% 的性能差距未解释

报告已投递给 Research Director。Issue Tracker 已同步更新（13 条 open issues）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director"
}
```

</details>

---


## Round 7

## Round 7

2 recorded events


### User

_source line 57 · 2026-05-17T00:40:56.464538+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 交叉回应：逐条回应 Reviewer 2 意见

---

### Must-Fix 问题

**[AGREE] R2-N1: episode-level reward 是传统 RL default，非 contribution**

强烈同意，且与我的 N1 形成双重打击：
- 我的 N1：Eq.1 γ^(T-h) 与 GRPO 标准算法不一致——GRPO 无显式 γ discount，公式可能是对算法的误读
- R2-N1：即使公式成立，γ decay 也是 Sutton & Barto [10] Ch.13 教科书内容

两者叠加结论：论文的 Contribution (1) "identify credit assignment decay" 要么是错的（GRPO 无 γ），要么是旧的（教科书知识），均不构成顶会 contribution。

论文的真实贡献应重新定位为：**在 LLM agent RL 框架（如 RAGEN）的具体工程实践中，step-level 默认配置会失败，episode-level 是有效修复。** 这一定位下的有价值延伸问题是"为什么 LLM 社区会默认走向 step-independent（而传统 RL 不会）"，但当前论文未回答。

---

**[AGREE] R2-N2: 10 篇引用严重不足**

完全同意。我在初审 W4 中已独立提出。补充关键缺失：
- RL foundations: PPO, REINFORCE, GAE（论文声称解决 credit assignment 却不引 GAE，不可接受）
- Credit assignment: Reward shaping (Ng 1999), HER (Andrychowicz 2017)
- Agent training: Reflexion, AgentTuning, FireAct, AgentQ
- Benchmarks: WebShop, AgentBench

---

**[AGREE with nuance] R2-N3: Self-Guide 72.7% vs 本文 24.3%**

大体同意这是严重问题，但需区分：

**如果 Self-Guide 是纯 RL 无 expert data**：论文彻底无法自洽，"model capacity bottleneck"被直接反驳，意义归零。

**如果 Self-Guide 用 SFT + expert trajectories**：对比不完全公平（paradigm 不同），但论文仍必须正面回应：(a) 两种 paradigm 差异是什么，(b) 为什么读者应关注 from-scratch RL 的 24.3%，(c) 是否存在 expert data 不可得的场景。

无论哪种情况，§5 "model capacity is separate bottleneck"的说法 incomplete——Self-Guide [2] 用相同 Qwen-1.7B 证明 capacity 足够。这也与我的 W4（绝对性能需定位）直接相关。

---

### Should-Fix 问题

**[AGREE] R2-W1: "eliminates this bottleneck" overclaiming**

完全同意。结合我的 N2（95% CI = [9.4%, 39.2%]），论文不仅 success rate 低，且估计极不确定。"Eliminates"应改为 "enables non-zero learning" 或 "significantly alleviates"。

---

**[PARTIALLY AGREE] R2-W2: Contribution (1) 与 (3) 冗余**

部分同意。(3) h-sweep cliff 是 (1) credit assignment decay 的实验证据，分列两条有凑数嫌疑。但 h-sweep 作为 diagnostic methodology 本身有独立价值——前提是统计支撑充分（回到我的 W1：目前 single seed 不够）。

---

**[AGREE] R2-W3: Future directions 暴露 stepping-stone 定位**

同意。大量 future work = 承认当前只是最简方案。NeurIPS/ICML 正文期望相对完整的解决方案，非 preliminary observation + minimal fix。

---

**[PARTIALLY AGREE] R2-W4: 叙事转型痕迹**

无法从摘要/结构直接验证（需读 PDF 全文）。但论文确实经历了从 selective verification 到 pure training methodology 的转型（§4.5 Table 4 "Verification Value" 可能是残留）。建议 Director 重点检查 §4.5 与整体定位的一致性。

---

## R1 与 R2 意见互补关系总结

| 维度 | R1 发现 | R2 发现 | 叠加效应 |
|------|---------|---------|----------|
| 理论基础 | Eq.1 与 GRPO 算法不一致 | 即使正确也是教科书内容 | 理论贡献归零 |
| 实验力度 | 统计 power 不足 (3 seeds, CI极宽) | 与 Self-Guide 72.7% 的巨大差距 | 实验说服力大幅削弱 |
| Baselines | 缺 GAE/reward shaping 对比 | 缺与更多 agent training 方法对比 | Baseline 全面不足 |
| 引用 | 10条太少 (我的W4) | 缺关键领域覆盖 (R2-N2) | 完全一致 |
| 定位 | Borderline Reject (3/6) | Reject (4/10) | 共识：当前版本不达标 |

**最终共识判断**：论文方向有价值，但当前版本在理论严谨性、实验规模、baseline 完备性三个维度均不满足 NeurIPS/ICML 标准。建议：(1) 诚实重定位贡献为工程实践验证而非理论发现，(2) 大幅增加 seeds 和 baselines（含 GAE、γ=1 等中间方案），(3) 正面回应 Self-Guide performance gap，(4) 扩充 references 至 30+ 条。

---

[Reviewer 1 审稿结果]:
交叉回应已提交。核心结论：R1 与 R2 意见高度一致且互补——理论基础（Eq.1 误读 + 教科书知识）、实验力度（统计不足 + Self-Guide gap）、baseline 缺失三个维度共同指向当前版本不达标。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 58 · 2026-05-17T00:41:08.675759+00:00_

审稿报告已在上一轮成功提交给 Research Director。Reviewer 1 的交叉回应已被纳入最终报告。

**Round 1 审稿流程完毕。**

最终结论：**Weak Reject**（两位 Reviewer 完全共识，零 REBUT）。6 个 Critical 问题 + 7 个 Warning，核心缺陷：理论公式与 GRPO 不匹配、新颖性不足（教科书内容）、统计力全面不足、缺标准 baseline、Self-Guide 性能差距未解释、引用严重不足。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director"
}
```

</details>

---


## Round 8

## Round 8

78 recorded events


### User

_source line 59 · 2026-05-23T06:21:52.833375+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: cost-verify-agent-rl
- 论文路径: projects/cost-verify-agent-rl/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: ARR (Main + Findings unified)
- 截止日期: 未提供，请自行调研
- **引用验证**: ✅ 后台自动运行中，完成后你会收到 [引用验证结果] 消息，请在合成报告时纳入

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 60 · 2026-05-23T06:21:58.929386+00:00_

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
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 61 · 2026-05-23T06:21:58.980309+00:00_

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
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 62 · 2026-05-23T06:22:03.949194+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 63 · 2026-05-23T06:22:03.949672+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 64 · 2026-05-23T06:22:08.265721+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "cost-verify-agent-rl"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "cost-verify-agent-rl"
  }
}
```

</details>

---


### Tool result

_source line 65 · 2026-05-23T06:22:09.621263+00:00_

{"result":"# 项目 cost-verify-agent-rl 概况\n\n## 实验状态 (183 个)\n\n- **exp010**: DONE (failed) — \n- **exp009**: DONE (failed) — \n- **exp008**: PREPARING (killed) — \n- **exp007**: DONE (failed) — \n- **exp007_dryrun**: PREPARING — \n- **exp003**: DONE (failed) — \n- **exp005**: PREPARING — \n- **exp_003**: PREPARING (failed) — \n- **exp_003_dryrun**: PREPARING (failed) — \n- **exp_003_dryrun2**: PREPARING (failed) — \n- **exp003_dryrun3**: PREPARING (failed) — \n- **exp_003_dryrun3**: PREPARING (failed) — \n- **exp_002**: DONE (failed) — \n- **exp_001b**: DONE (failed) — \n- **exp_001**: DONE (failed) — \n\n## 最新报告\n&lt;!-- AUTO-FACTS-BEGIN (generated 2026-05-23T01:08:36Z; do not edit — regenerated by auto_build_report_facts) -->\n## 📊 当前状态（auto-derived from registry）\n\n**总计**: 180 个实验 — ANALYZING 1, DONE 147, PREPARING 32\n**DONE 分布**: failed 62, killed 20, negative 23, success 42\n\n### 💾 磁盘余量\n- **bjb1-17606**:\n  - `/init`: 150M/150M 可用（已用 0%）\n  - `/autodl-pub/data`: 5.7T/10T 可用（已用 44%）\n  - `/usr/bin/nvidia-smi`: 817G/879G 可用（已用 3%）\n- **westd-47453**:\n  - `/autodl-pub`: 5.3T/7.3T 可用（已用 24%）\n  - `/init`: 150M/150M 可用（已用 1%）\n  - `/usr/bin/nvidia-smi`: 813G/879G 可用（已用 3%）\n\n### 🏃 RUNNING\n_（无）_\n\n### 📌 最近完成 (top 5)\n- `exp029_seed7_high_kl_step7_ood_v2` [failed] — 2026-05-23T00:28:57\n- `exp029_seed7_high_kl_step5_ood_v2` [failed] — 2026-05-23T00:28:55\n- `exp029_seed100_resume_step10` [success] — 2026-05-23T00:17:50\n- `exp029_seed7_ood_precollapse` [killed] — 2026-05-22T22:33:47\n- `exp029_seed300_step5_ood_eval_v4` [success] — 2026-05-22T22:26:20\n\n### 🔴 最近失败原因 (top 3)\n- `exp029_seed7_high_kl_step7_ood_v2`: _(no failure_reason — pre-2026-04-24 entry)_\n- `exp029_seed7_high_kl_step5_ood_v2`: _(no failure_reason — pre-2026-04-24 entry)_\n- `exp029_seed7_ood_precollapse`: _(no failure_reason — pre-2026-04-24 entry)_\n\n&lt;!-- AUTO-FACTS-END -->\n\n---\n\n# Handover — 2026-05-23\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|
…[truncated 1681 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1355
}
```

</details>

---


### Tool call

_source line 66 · 2026-05-23T06:22:10.123600+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/main.tex",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/main.tex",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 67 · 2026-05-23T06:22:10.475380+00:00_

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
12	\usepackage{amsmath}
13	\usepackage{amssymb}
14	\usepackage{amsthm}
15	\usepackage{enumitem}
16	
17	\title{Sign Misattribution in Step-Independent Agent RL:\\Dual Mechanism Diagnosis and Episode-Level Fix}
18	
19	\author{Anonymous}
20	
21	\begin{document}
22	\maketitle
23	
24	\begin{abstract}
25	Multi-turn agent reinforcement learning requires credit assignment across long interaction trajectories, yet current frameworks default to step-independent windowing that decomposes trajectories into independently optimized windows. This introduces a fundamental credit assignment pathology driven by two mechanisms: \textit{policy information loss}, which truncates context and imposes a constant performance ceiling, and \textit{advantage sign misattribution}, which causes gradient updates to reflect episode outcomes rather than local action quality, producing cumulative degradation. At $p{=}12.5\%$ with group size $K{=}8$, 80.9\% of gradient updates for locally correct actions carry incorrect sign---consistent with an empirically measured 52\% credit agreement rate indistinguishable from random chance. A $2{\times}2$ factorial separates the mechanisms: eliminating sign misattribution converts catastrophic collapse into bounded learning; removing information loss enables generalization. Episode-level Group Relative Policy Optimization (GRPO), treating the full trajectory as a single optimization sample, resolves both mechanisms. A systematic 11-seed evaluation reveals that stable training is necessary but not sufficient: 73\% of seeds avoid collapse, but only 27\% achieve statistically significant OOD generalization ($p{<}0.01$; 25--31\% OOD vs.\ 6.7\% SFT baseline). Cross-scale verification at 8B confirms both failure and fix (90.3\% O
…[truncated 1240 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 68 · 2026-05-23T06:22:10.475792+00:00_

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
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
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

_source line 69 · 2026-05-23T06:22:10.526189+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 70 · 2026-05-23T06:22:17.407886+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers ARR submission deadline"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers ARR submission deadline"
  }
}
```

</details>

---


### Tool call

_source line 71 · 2026-05-23T06:22:17.709478+00:00_

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
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 author guidelines submission format page limit"
  }
}
```

</details>

---


### Tool result

_source line 72 · 2026-05-23T06:22:23.113000+00:00_

Web search results for query: "EMNLP 2026 call for papers ARR submission deadline"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"AI Conference Deadlines - Jie Cao | Dialogue, NLP, ML","url":"https://mlciv.com/ai-deadlines/"},{"title":"emnlp 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=emnlp26"}]

Based on the search results, here's the information about EMNLP 2026's call for papers and ARR submission deadline:

## Key Deadline

The ARR submission deadline for EMNLP 2026 is Ma
…[truncated 799 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "WebSearch",
  "elapsed_ms": 5705
}
```

</details>

---


### Tool result

_source line 73 · 2026-05-23T06:22:26.325101+00:00_

Web search results for query: "ACL Rolling Review 2026 author guidelines submission format page limit"

Links: [{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"Author Guidelines for Student Research Workshop Papers -","url":"https://2026.eacl.org/calls/srw/guidelines/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Paper formatting guidelines - ACLPUB","url":"https://acl-org.github.io/ACLPUB/formatting.html"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"}]

Based on the search results, here's what I found about ACL Rolling Review 2026 author guidelines:

## Submission Format & Requirements

Papers must follow ACL formatting, and authors are encouraged to use the ACL pubcheck tool to check for common problems. There is an official Overleaf template with a [review] setting that must be on for submission.

Submissions based on the MS Word template will be desk-rejected starting from March 2026.

## Page Limits

Final versions of accepted papers will be given one additional page of content (up to 9 pages for long papers, up to 5 pages for short papers) to address reviewers' comments.

## Key Formatting Guidelines

ACL r
…[truncated 478 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "WebSearch",
  "elapsed_ms": 8615
}
```

</details>

---


### Tool call

_source line 74 · 2026-05-23T06:22:39.373558+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 75 · 2026-05-23T06:22:39.875949+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/theoretical_analysis.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/appendix.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "Glob",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 76 · 2026-05-23T06:22:40.829842+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "cost-verify-agent-rl",
  "file": "paper_checklist.yaml",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "cost-verify-agent-rl",
    "file": "paper_checklist.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 77 · 2026-05-23T06:22:41.081728+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'cost-verify-agent-rl'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 78 · 2026-05-23T06:22:41.132393+00:00_

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
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
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

_source line 79 · 2026-05-23T06:22:41.233176+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 80 · 2026-05-23T06:22:46.230430+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 81 · 2026-05-23T06:22:46.833198+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Reinforcement learning from sparse terminal reward has emerged as a promising paradigm for training LLM agents on multi-turn interactive tasks spanning 30--50 interaction steps~\cite{kim2025reflact,digiRL2024,wang2022scienceworld}. Group Relative Policy Optimization (GRPO)~\cite{shao2024deepseekmath}, with its critic-free design, has become the algorithm of choice. Yet a gap persists between the promise of RL-driven agent improvement and the reality of training outcomes: recent agent RL systems~\cite{ragen2025,selfguide2026,spear2025,feng2025gigpo} share a common, unscrutinized implementation pattern---decomposing trajectories into fixed-size windows, each optimized independently---and frequently report training instability without diagnosing its root cause.
5	
6	We show this \textit{step-independent} default introduces a fundamental credit assignment pathology. Step-independent training partitions trajectories into non-overlapping $h$-step windows, each optimized via GRPO. This produces a two-phase collapse: task success drops to 0\% while action validity initially remains high, then continued training destroys even basic formatting. Standard remedies---dense reward shaping, discount tuning---fail. Concurrent methods that improve per-step credit quality (GiGPO~\cite{feng2025gigpo}, GAGPO~\cite{gagpo2026}, Turn-PPO~\cite{turnppo2026}) address symptoms but not the structural root cause: the windowing itself.
7	
8	We trace the collapse to two mechanisms at different layers. \textit{\textbf{Policy information loss}} (M1) operates at the inference layer: each window lacks access to earlier observations, imposing a constant performance ceiling. \textit{\textbf{Advantage sign misattribution}} (M2) operates at the training layer: under binary reward, the advantage sign reflects episode success rather than local action quality. At $p{=}12.5\%$ with $K{=}8$, 80.9\% of gradient updates for locally correct windows point 
…[truncated 1489 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "Read",
  "elapsed_ms": 602
}
```

</details>

---


### Tool call

_source line 82 · 2026-05-23T06:22:46.833615+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 83 · 2026-05-23T06:22:47.285625+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Problem Formulation and GRPO}
5	\label{sec:problem_formulation}
6	
7	We model the multi-turn agent as a partially observable Markov decision process (POMDP) where the policy $\pi_\phi(a_t \mid h_t)$ generates actions conditioned on interaction history $h_t = (o_1, a_1, \ldots, o_t)$. Episodes of $T$ steps terminate with binary reward $R \in \{0, r_+\}$. GRPO~\cite{shao2024deepseekmath} samples $K$ rollouts per task and computes group-relative advantages:
8	\begin{align}
9	\hat{A}_k &= \frac{R_k - \mu}{\sigma + \epsilon}, \notag \\
10	\mu &= \frac{1}{K}\sum_{j=1}^K R_j, \quad \sigma = \sqrt{\frac{1}{K}\sum_{j=1}^K (R_j - \mu)^2}
11	\label{eq:grpo_advantage}
12	\end{align}
13	GRPO is episode-level by design: each rollout receives one return and one advantage, with no inherent temporal discounting.
14	
15	\subsection{Step-Independent Windowing}
16	\label{sec:step_independent}
17	
18	Agent RL frameworks must reconcile GRPO's episode-level design with the memory constraints of long trajectories. RAGEN~\cite{ragen2025} introduces \textbf{step-independent training}: the trajectory is partitioned into non-overlapping $h$-step windows, each receiving a discounted return:
19	\begin{equation}
20	R_k = \gamma^{(N - k)} \cdot R_{\text{episode}}
21	\label{eq:step_return}
22	\end{equation}
23	where $N = \lceil T/h \rceil$ is the number of windows. Each window is optimized as an independent GRPO sample. This reduces sequence length from $O(T)$ to $O(h)$ and multiplies the effective batch size, but fundamentally alters credit assignment.
24	
25	\subsection{Dual Mechanism Analysis}
26	\label{sec:dual_mechanism}
27	
28	Two mechanisms jointly cause training failure under step-independent optimization.
29	
30	\subsubsection{Mechanism 1: Policy Information Loss}
31	\label{sec:m1_information_loss}
32	
33	Step-independent training truncates context at both inference and training time. The policy $\pi_\phi(a_t \mid h_{\text{window}_k}
…[truncated 2575 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 84 · 2026-05-23T06:22:47.285986+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/theoretical_analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/theoretical_analysis.tex"
  }
}
```

</details>

---


### Tool result

_source line 85 · 2026-05-23T06:22:47.788091+00:00_

1	\section{Theoretical Analysis}
2	\label{sec:theory}
3	
4	Sign misattribution is the more fundamental failure mechanism because it causes active divergence, not merely slow convergence. We derive the probability of incorrect gradient direction below; full proofs appear in Appendix~\ref{app:theory_full}.
5	
6	\textbf{Proposition 1.} \textit{Under step-independent training with binary episode reward $R_{\text{episode}} \in \{0, r_+\}$, the probability that window $k$'s advantage $\hat{A}_k$ has the correct sign (aligned with local action quality) approaches the base success rate $p$ as the number of rollouts $K$ per group increases.}
7	
8	\textit{Proof sketch.} In a failed episode ($R_{\text{episode}} = 0$), all windows receive $R_k = 0$. If any rollout in the group succeeded, $\mu > 0$, so every window in the failed episode receives $\hat{A}_k < 0$---including windows with locally correct actions. The probability of receiving the wrong sign in a failed episode is $1 - (1-p)^{K-1}$ (at least one group member succeeded). As $K$ grows, this approaches $1-p$, and the overall probability of correct sign approaches $p$. \hfill$\square$
9	
10	The key distinction is temporal. Information loss (M1) imposes a constant ceiling determined by $h$; sign misattribution (M2) is cumulative---each wrong-sign gradient step erodes policy competence below that ceiling. A wrong-sign gradient moves the optimizer \textit{away} from good policies; a reduced-magnitude gradient from discounting ($\gamma^{(N-k)}$) still points toward good policies. Sign errors produce active divergence; magnitude errors merely slow convergence (Appendix~\ref{app:sign_fundamental}).
11	
12	\textbf{Proposition 2.}\label{prop:correct_sign} \textit{Let $p$ denote the episode success rate and $K$ the number of rollouts per group. Under step-independent training with binary episode reward, the fraction of gradient updates with correct sign is:}
13	\begin{equation}
14	P(\text{correct} \mid \text{update}) = \frac{p}{1
…[truncated 1991 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 86 · 2026-05-23T06:22:47.788519+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 87 · 2026-05-23T06:22:48.240824+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	Step-independent training collapses while episode-level training succeeds; a factorial design separates the two mechanisms; and window size $h$ modulates severity.
5	
6	\subsection{Setup}
7	\label{sec:setup}
8	
9	We evaluate on ALFWorld~\cite{shridhar2021alfworld}, a text-based household environment with six task types requiring sequential reasoning over up to 50 steps. Reward is binary: $R \in \{0, r_+\}$. The base policy is Qwen3-1.7B fine-tuned on 2{,}546 expert demonstrations (SFT baseline: 12.5\% in-distribution, 0\% pre-SFT). At $p{=}0.125$ with $K{=}8$, Proposition~2 predicts ${\sim}80.9\%$ of gradient updates for locally correct windows carry incorrect sign. All conditions use RAGEN~\cite{ragen2025} with GRPO~\cite{shao2024deepseekmath} ($K{=}8$, lr$=10^{-6}$, $\beta{=}0.01$, $\gamma{=}0.95$, 15 steps; full hyperparameters in Appendix~\ref{app:hyperparameters}). We report success rate on a 134-task OOD set (primary) and 32-task in-distribution set (secondary). Seed counts are noted per condition.
10	
11	\subsection{Factorial Mechanism Separation}
12	\label{sec:factorial_experiments}
13	
14	We implement the $2 \times 2$ factorial (Section~\ref{sec:factorial_design}): \textbf{Cell~A} (both mechanisms active; $h{=}2$, step-level advantage), \textbf{Cell~B} (M1 only; $h{=}2$, episode-level advantage), and \textbf{Cell~D} (neither; full trajectory, episode-level advantage). Two seeds each.
15	
16	\subsection{Results}
17	\label{sec:results}
18	
19	Cell~A collapses in two phases (Table~\ref{tab:main_results}): task success drops to 0\% within 3--9 steps while action validity initially remains above 80\%, then continued sign misattribution destroys formatting (validity: 89.3\% $\to$ 43.1\% between steps 2--4, reaching 0.06\% by step~15).% exp_id: hsweep_h2_seed1, hsweep_h2_seed2
20	Cell~B eliminates sign misattribution while retaining information loss: training success reaches 55\% (seed~2), but OOD generalizati
…[truncated 10093 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 88 · 2026-05-23T06:22:48.241343+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 89 · 2026-05-23T06:22:52.357429+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{RL for multi-turn LLM agents.}
5	GRPO~\cite{shao2024deepseekmath}, originally designed for mathematical reasoning, has been adapted to multi-turn agents through step-independent windowing~\cite{ragen2025}. Subsequent work improves algorithms (GiGPO~\cite{feng2025gigpo}), reward design (Self-Guide~\cite{selfguide2026}), or training pipelines (SPEAR~\cite{spear2025}, DigiRL~\cite{digiRL2024}), but all share a common assumption: trajectory decomposition into fixed windows is benign. We show this assumption is false---the windowing introduces a structural credit assignment pathology that no algorithmic improvement within the paradigm can fix.
6	
7	\paragraph{Credit assignment in reinforcement learning.}
8	TD($\lambda$)~\cite{sutton1988td} and GAE~\cite{schulman2016gae} interpolate between bootstrapping and Monte Carlo returns; REINFORCE~\cite{williams1992reinforce} uses full episode returns. In the low-success-rate regime ($p < 0.2$) typical of agent tasks, the classical bias-variance tradeoff breaks down: Proposition~2 shows sign errors under windowing grow as $1{-}p$, dominating any variance reduction that windowing provides.
9	
10	\paragraph{Credit assignment and sign misattribution evidence.}
11	Several independent studies corroborate our diagnosis. IRC~\cite{irc2026} reports per-turn advantages frequently disagree in sign with outcome advantages. MC-GRPO~\cite{mcgrpo2025} measures a 5\% sign-flip rate. GRPO-$\lambda$~\cite{grpolambda2025} proves value estimation error grows with position. OAR~\cite{oar2026} identifies ``reward aliasing'' from coarse credit. Our contribution is to formalize this as a structural property of the training paradigm and to show it interacts with information loss in a vicious cycle.
12	
13	\paragraph{Multi-turn credit assignment methods.}
14	Turn-PPO~\cite{turnppo2026} introduces per-turn value estimation, GAGPO~\cite{gagpo2026} uses generalized advantage with a turn-leve
…[truncated 956 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "Read",
  "elapsed_ms": 4116
}
```

</details>

---


### Tool call

_source line 90 · 2026-05-23T06:22:52.558647+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 91 · 2026-05-23T06:22:52.609293+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Generality beyond ALFWorld.}
5	Sign misattribution is not specific to RAGEN, ALFWorld, or GRPO. It arises whenever three structural properties co-occur: (a) step-level windowing, (b) sparse binary reward, and (c) group-relative normalization. Under these conditions, the advantage sign collapses to a proxy for episode outcome regardless of local quality (Equation~\ref{eq:sign_correlation}). Severity scales with task difficulty: as $p$ decreases, $P(\text{correct} \mid \text{update}) \to p$, so sign misattribution is worst precisely where credit assignment matters most. ScienceWorld validation (Section~\ref{sec:cross_env}) provides initial cross-environment evidence; the mechanism should operate in any environment satisfying (a)--(c).
6	
7	\paragraph{Mechanism interaction.}
8	M1 and M2 form a vicious cycle: M1 lowers $p$ by preventing multi-step strategies, increasing wrong-sign updates under M2 ($P(\text{correct} \mid \text{update}) \to p$), which further degrades $p$. This positive feedback explains why step-independent training produces active collapse rather than slow convergence.
9	
10	\paragraph{Direction correctness vs.\ credit granularity.}
11	At low success rates ($p{=}12.5\%$), direction correctness dominates: coarse-but-correct gradients converge slowly; fine-but-wrong gradients diverge. As $p$ increases, per-step credit becomes more valuable. Annealing $\lambda$ from 1 to $\lambda{<}1$---combining episode-level direction with finer credit---is a natural extension.
12	
13	\paragraph{Why step-independent became the default.}
14	Six factors contributed (Appendix~\ref{app:why_defaults}): (1)~context length constraints force windowing; (2)~token-level training inertia; (3)~framework design accident---RAGEN's default propagates silently; (4)~$O(h)$ vs.\ $O(T)$ memory savings provide immediate benefits while credit assignment failure is deferred; (5)~dense reward creates gaming targets (Section~\ref{
…[truncated 980 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 92 · 2026-05-23T06:22:52.760463+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 93 · 2026-05-23T06:22:52.760920+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	Step-independent training in multi-turn agent RL fails through two mechanisms: policy information loss imposes a performance ceiling, while advantage sign misattribution causes cumulative degradation---at $p{=}12.5\%$ with $K{=}8$, ${\sim}$80.9\% of gradient updates carry incorrect sign. A $2{\times}2$ factorial separates the mechanisms; episode-level GRPO resolves both (17.2\% mean OOD at 1.7B, 90.3\% at 8B). A systematic 11-seed evaluation reveals that stable training is necessary but not sufficient: 73\% avoid collapse, but only 27\% generalize ($p{<}0.01$). The central insight---sign errors are more destructive than magnitude imprecision---applies to any agent RL method combining step-level windowing, sparse binary reward, and group-relative normalization.
5	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 94 · 2026-05-23T06:22:52.911787+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 95 · 2026-05-23T06:22:52.962471+00:00_

1	\appendix
2	
3	\section{Theoretical Analysis: Full Derivations}
4	\label{app:theory_full}
5	
6	\subsection{Why Sign Misattribution is Fundamental}
7	\label{app:sign_fundamental}
8	
9	The two mechanisms identified in Section~\ref{sec:dual_mechanism} operate at different layers and produce qualitatively different failures. Policy information loss (Mechanism 1) operates at the inference layer, restricting the observable context and establishing a structural performance ceiling that is constant across training. Sign misattribution (Mechanism 2) operates at the training layer, corrupting gradient directions and progressively degrading performance below this ceiling.
10	
11	\textit{Proof of Proposition 1.} Define ``correct sign'' as follows: for a window containing locally beneficial actions, the correct sign of $\hat{A}_k$ is positive (reinforcement); for a window containing locally detrimental actions, the correct sign is negative (suppression). Under binary reward, the return for window $k$ is $R_k = \gamma^{(N-k)} \cdot R_{\text{episode}}$ (Equation~\ref{eq:step_return}). In a failed episode ($R_{\text{episode}} = 0$), all windows receive $R_k = 0$ regardless of their local action quality. If the group contains at least one successful rollout, the group mean $\mu > 0$, and all windows in the failed episode receive negative advantages after normalization via Equation~\ref{eq:grpo_advantage}. This includes windows where the agent took locally correct actions. Now consider a window with good local actions. In a successful episode (probability $p$), the window receives positive $\hat{A}_k$, which is the correct sign. In a failed episode (probability $1 - p$), the window receives negative $\hat{A}_k$ whenever $\mu > 0$, which is the wrong sign. The probability that $\mu = 0$ (all $K$ rollouts in the group failed) is $(1-p)^K$, which shrinks exponentially with $K$. As $K$ grows, nearly every failed episode produces a non-zero group mean, and the window receives the wrong 
…[truncated 10845 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 96 · 2026-05-23T06:22:59.939086+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "*.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "*.bib",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 97 · 2026-05-23T06:23:00.290887+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/references.bib

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "Glob",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 98 · 2026-05-23T06:23:00.441826+00:00_

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
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
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

_source line 99 · 2026-05-23T06:23:00.492684+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 100 · 2026-05-23T06:23:03.705754+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 101 · 2026-05-23T06:23:04.108001+00:00_

1	@inproceedings{shridhar2021alfworld,
2	  title     = {{ALFWorld}: Aligning Text and Embodied Environments for Interactive Learning},
3	  author    = {Shridhar, Mohit and Yuan, Xingdi and C\^{o}t\'{e}, Marc-Alexandre and Bisk, Yonatan and Trischler, Adam and Hausknecht, Matthew},
4	  booktitle = {International Conference on Learning Representations},
5	  year      = {2021},
6	}
7	
8	
9	@inproceedings{digiRL2024,
10	  title     = {{DigiRL}: Training In-The-Wild Device-Control Agents with Autonomous Reinforcement Learning},
11	  author    = {Bai, Hao and Zhou, Yifei and Cemri, Mert and Pan, Jiayi and Suhr, Alane and Levine, Sergey and Kumar, Aviral},
12	  booktitle = {Advances in Neural Information Processing Systems},
13	  year      = {2024},
14	}
15	
16	@inproceedings{feng2025gigpo,
17	  title     = {{GiGPO}: Group-in-Group Policy Optimization for {LLM} Agent Training},
18	  author    = {Feng, Lang and Xue, Zhenghai and Liu, Tingcong and An, Bo},
19	  booktitle = {Advances in Neural Information Processing Systems},
20	  year      = {2025},
21	}
22	
23	@inproceedings{kim2025reflact,
24	  title     = {{ReflAct}: World-Grounded Decision Making in {LLM} Agents via Goal-State Reflection},
25	  author    = {Kim, Jeonghye and Rhee, Sojeong and Kim, Minbeom and Kim, Dohyung and Lee, Sangmook and Sung, Youngchul and Jung, Kyomin},
26	  booktitle = {Proceedings of the Conference on Empirical Methods in Natural Language Processing},
27	  year      = {2025},
28	}
29	
30	
31	@article{ragen2025,
32	  title   = {{RAGEN}: Understanding Self-Evolution in {LLM} Agents via Multi-Turn Reinforcement Learning},
33	  author  = {Wang, Zihan and Wang, Kangrui and Wang, Qineng and Zhang, Pingyue and Li, Linjie and Yang, Zhengyuan and Jin, Xing and Yu, Kefan and Nguyen, Minh Nhat and Liu, Licheng and Gottlieb, Eli and Lu, Yiping and Cho, Kyunghyun and Wu, Jiajun and Li, Fei-Fei and Wang, Lijuan and Choi, Yejin and Li, Manling},
34	  journal = {arXiv preprint arXiv:2504.20073},
35	  year    =
…[truncated 5295 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 102 · 2026-05-23T06:23:04.259089+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/agent/config.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/agent/config.yaml"
  }
}
```

</details>

---


### Tool result

_source line 103 · 2026-05-23T06:23:04.259619+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/.claude/sessions/review_director_e87609d6.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 104 · 2026-05-23T06:23:12.742222+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/config.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/config.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl"
  }
}
```

</details>

---


### Tool result

_source line 105 · 2026-05-23T06:23:12.742652+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 106 · 2026-05-23T06:23:15.745179+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/config.*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/config.*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl"
  }
}
```

</details>

---


### Tool result

_source line 107 · 2026-05-23T06:23:15.845961+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "Glob",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 108 · 2026-05-23T06:23:19.509225+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "cost-verify-agent-rl",
  "file": "decisions.yaml",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "cost-verify-agent-rl",
    "file": "decisions.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 109 · 2026-05-23T06:23:19.559917+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/decisions.yaml\", \"content\": \"_next_id: 139\\ndecisions:\\n- id: D001\\n  date: 2026-05-13 17:33 UTC\\n  summary: MVP 选择 ALFWorld + Qwen3-1.7B 单环境验证 B-IAVR 核心假设\\n  rationale: ALFWorld 离散动作空间使 action_changed 信号最清晰，semantic canonicalization 简单（verb,object,receptacle三元组）。Qwen3-1.7B\\n    有充分 headroom（+8.6pp on ALFWorld）。MVP 只需验证\\\"agent 能学会选择性验证\\\"这一核心假设，不需要跨环境/跨模型。2×GPU\\n    足够 1.7B+LoRA 训练。\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-13 18:39 UTC\\n  summary: Phase A 使用全量微调（非 LoRA），匹配 Self-Guide 原始论文设置\\n  rationale: Self-Guide 原文用全量微调 GRPO。1.7B 模型在 94GB VRAM 下全量微调显存仅 38.5GB，完全可行。匹配 baseline\\n    设置确保公平对比。IDEA_BRIEF 提及 LoRA 是基于 H100 80GB 的资源估算，RTX PRO 6000 94GB 无需节省。\\n  related_experiments:\\n  - exp_id: exp_001\\n    role: Phase A baseline\\n    result: running\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-13 23:55 UTC\\n  summary: Kill exp003，Phase A bootstrap 失败确认，等待 invalid action 根因诊断后决定修复方向\\n  rationale: 'exp003 step 1: invalid_action=95.3%, pg_loss≈0, 每步 1.6h（100步=160h）。GRPO\\n    从 0.125% valid action 中无法获得有效学习信号。Qwen3 无独立 Instruct 版，Plan B 失效。需先诊断 invalid\\n    action 根因（格式冲突 / token 问题 / prompt 不兼容）再选修复路径。'\\n  related_experiments:\\n  - exp_id: exp003\\n    role: primary\\n    result: failed - bootstrap failure, 95% invalid actions, pg_loss≈0\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-14 00:10 UTC\\n  summary: 采用方案 A（修改解析器适配 Qwen3 格式）+ prompt 增强 + 速度优化，解决 bootstrap 失败\\n  rationale: 根因确认：Qwen3-1.7B 原生输出 &lt;think>...&lt;/think> 后直接跟自然语言，不生成 &lt;answer> 标签。RAGEN\\n    解析器正则要求 &lt;answer> 导致 95% invalid。方案 A 最快（1-2h 改代码）、最低风险（不换模型不加训练阶段），同时优化速度（关闭 collapse\\n    multi_turn 省 35% 步耗时 + 减 traj/step）。\\n  related_experiments:\\n  - exp_id: exp003\\n    role: diagnostic\\n    result: '32/32 samples confirm: no &lt;answer> tag in Qwen3 output'\\n  depends_on:\\n  - D003\\n- id: 
…[truncated 1451 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 110 · 2026-05-23T06:23:23.453393+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/config.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/config.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1"
  }
}
```

</details>

---


### Tool result

_source line 111 · 2026-05-23T06:23:23.554200+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "Glob",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 112 · 2026-05-23T06:23:26.615601+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/project_config*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/project_config*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1"
  }
}
```

</details>

---


### Tool result

_source line 113 · 2026-05-23T06:23:26.716459+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "Glob",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 114 · 2026-05-23T06:23:29.677888+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/",
  "description": "List project root directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/",
    "description": "List project root directory"
  }
}
```

</details>

---


### Tool result

_source line 115 · 2026-05-23T06:23:29.828929+00:00_

AGENTS.md
RAGEN
ROADMAP.lock
ROADMAP.md
_last_visual_review.json
_paper_audit_result.json
artifacts
checkpoints
constraints.lock
constraints.yaml
decisions.lock
decisions.yaml
distill_tmp
docs
dream_registry.lock
dream_registry.yaml
dream_registry.yaml.bak
dream_registry.yaml.bak.130710
experiment_plan.lock
experiment_plan.yaml
figures
literature_map.yaml
logs
memory.md
mistakes.lock
mistakes.yaml
paper_framing.md
paper_provenance.lock
paper_provenance.yaml
registry.lock
registry.yaml
report.md
scripts
study_status.lock
task_context
worker_outputs
writing_plan.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "Bash",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 116 · 2026-05-23T06:23:33.997937+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/review_reports/ 2>/dev/null; ls /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/review_issues.yaml 2>/dev/null",
  "description": "Check existing review reports and issues"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/review_reports/ 2>/dev/null; ls /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/review_issues.yaml 2>/dev/null",
    "description": "Check existing review reports and issues"
  }
}
```

</details>

---


### Tool result

_source line 117 · 2026-05-23T06:23:34.048487+00:00_

round_0.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/review_issues.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 118 · 2026-05-23T06:23:47.094291+00:00_

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
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
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

_source line 119 · 2026-05-23T06:23:47.144890+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 120 · 2026-05-23T06:23:51.962197+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 121 · 2026-05-23T06:23:53.267534+00:00_

1	
2	# Review Issues Tracker — cost-verify-agent-rl
3	# Source: Dream Review Round 1 (dream_20260516T235255)
4	# Date: 2026-05-17
5	
6	- id: "DR1-C1"
7	  summary: "Theory framework must match actual GRPO implementation (not algorithm-level abstraction)"
8	  category: method
9	  severity: critical
10	  status: in_progress
11	  first_raised_round: 0
12	  last_seen_round: 0
13	  mentions:
14	    - {round: 0, reviewers: [R1, R2], note: "Dream review — both reviewers agree theory contribution collapses if Eq.1 is analogy not derivation"}
15	  action_items:
16	    - {round: 0, action: "Reframe theory as dual mechanism: policy information loss + gradient signal dilution. Update paper_framing.md.", assigned_to: director, status: done}
17	    - {round: 0, action: "D058 second correction: source audit found RAGEN step_independent DOES use γ in compute_step_discounted_returns(). Theory corrected to 'Credit Assignment Decay' (γ-attenuated success + undifferentiated failure). Distinguishes algorithm-level GRPO (no γ) from implementation-level step_independent (has γ).", assigned_to: director, status: done}
18	    - {round: 0, action: "plan_004: per-window advantage logging on h=2 seed 2 to empirically verify γ^k decay curve", assigned_to: agent, status: in_progress}
19	  resolution: ""
20	  resolution_round: null
21	
22	- id: "DR1-C2"
23	  summary: "Core novelty insufficient — episode-level RL is REINFORCE default"
24	  category: framing
25	  severity: critical
26	  status: in_progress
27	  first_raised_round: 0
28	  last_seen_round: 0
29	  mentions:
30	    - {round: 0, reviewers: [R1, R2], note: "Dream review — contribution reduces to 'discovered RAGEN has bug-like behavior and used standard method to fix'"}
31	  action_items:
32	    - {round: 0, action: "Reposition: 'diagnose LLM agent community default step-independent + dual mechanism analysis' not 'invented episode-level'", assigned_to: director, status: done}
33	    - {round: 0, action: "Add 'why community defaults to step
…[truncated 3999 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "Read",
  "elapsed_ms": 1305
}
```

</details>

---


### Tool call

_source line 122 · 2026-05-23T06:23:53.419071+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/agent-ml-research/config/projects/cost-verify-agent-rl.yaml 2>/dev/null || find /home/ubuntu/agent-ml-research -name \"*.yaml\" -path \"*cost-verify*\" 2>/dev/null | head -5",
  "description": "Find project config for external review settings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/agent-ml-research/config/projects/cost-verify-agent-rl.yaml 2>/dev/null || find /home/ubuntu/agent-ml-research -name \"*.yaml\" -path \"*cost-verify*\" 2>/dev/null | head -5",
    "description": "Find project config for external review settings"
  }
}
```

</details>

---


### Tool result

_source line 123 · 2026-05-23T06:23:53.620212+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "Bash",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 124 · 2026-05-23T06:24:03.309024+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/agent-ml-research -name \"*.yaml\" -path \"*project*\" 2>/dev/null | head -10; find /home/ubuntu/agent-ml-research -name \"config*\" -type f 2>/dev/null | head -10",
  "description": "Search for project config files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/agent-ml-research -name \"*.yaml\" -path \"*project*\" 2>/dev/null | head -10; find /home/ubuntu/agent-ml-research -name \"config*\" -type f 2>/dev/null | head -10",
    "description": "Search for project config files"
  }
}
```

</details>

---


### Tool result

_source line 125 · 2026-05-23T06:24:03.612022+00:00_

/home/ubuntu/agent-ml-research/workspace/config/projects/LLM-Calibration.yaml
/home/ubuntu/agent-ml-research/.git/config
/home/ubuntu/agent-ml-research/.venv/lib/python3.14/site-packages/ldap3/utils/__pycache__/config.cpython-314.pyc
/home/ubuntu/agent-ml-research/.venv/lib/python3.14/site-packages/ldap3/utils/config.py
/home/ubuntu/agent-ml-research/.venv/lib/python3.14/site-packages/fontTools/misc/configTools.py
/home/ubuntu/agent-ml-research/.venv/lib/python3.14/site-packages/fontTools/misc/__pycache__/configTools.cpython-314.pyc
/home/ubuntu/agent-ml-research/.venv/lib/python3.14/site-packages/wandb/integration/sagemaker/__pycache__/config.cpython-314.pyc
/home/ubuntu/agent-ml-research/.venv/lib/python3.14/site-packages/wandb/integration/sagemaker/config.py
/home/ubuntu/agent-ml-research/.venv/lib/python3.14/site-packages/wandb/sdk/launch/agent/config.py
/home/ubuntu/agent-ml-research/.venv/lib/python3.14/site-packages/wandb/sdk/lib/__pycache__/config_util.cpython-314.pyc
/home/ubuntu/agent-ml-research/.venv/lib/python3.14/site-packages/wandb/sdk/lib/config_util.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "Bash",
  "elapsed_ms": 302
}
```

</details>

---


### Tool call

_source line 126 · 2026-05-23T06:24:06.826759+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu -maxdepth 4 -name \"*.yaml\" -path \"*cost-verify*\" -not -path \"*.venv*\" 2>/dev/null | head -20",
  "description": "Find cost-verify project config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu -maxdepth 4 -name \"*.yaml\" -path \"*cost-verify*\" -not -path \"*.venv*\" 2>/dev/null | head -20",
    "description": "Find cost-verify project config"
  }
}
```

</details>

---


### Tool result

_source line 127 · 2026-05-23T06:24:06.927624+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/dream_registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/writing_plan.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/paper_provenance.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/literature_map.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/constraints.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/mistakes.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/decisions.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/experiment_plan.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_1/config/projects/cost-verify-agent-rl.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 128 · 2026-05-23T06:24:12.402742+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/config/projects/cost-verify-agent-rl.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/config/projects/cost-verify-agent-rl.yaml"
  }
}
```

</details>

---


### Tool result

_source line 129 · 2026-05-23T06:24:12.403090+00:00_

1	execution:
2	  gpu_ids:
3	    bjb1-17606:
4	    - cuda:0
5	  project_path: /root/cost-verify-agent-rl
6	  servers:
7	  - account: root
8	    server: bjb1-17606
9	feishu:
10	  chat_id: oc_4ebf0fb2d0159caa355a1a855f5ac59f
11	  check_references: true
12	  operational_chat_id: oc_733b284b383121720ce3d07c5c4a6bb2
13	  review_mode: fresh
14	  review_paper_path: projects/cost-verify-agent-rl/docs/paper/main.tex
15	  review_paper_pdf_path: /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/review_round_1/submitted.pdf
16	  review_round: 1
17	  review_supplementary_paths: ''
18	  submission_chat_id: oc_648eaf83d2b24d445764257cf6a55525
19	project:
20	  created_at: '2026-05-13T17:31:30.051Z'
21	  description: 'Verify When It Matters: Behaviorally-Grounded Selective Verification
22	    for Interactive Agents'
23	  name: cost-verify-agent-rl
24	  phase: research
25	  source_idea_id: idea_009
26	venue: emnlp-2026
27	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 130 · 2026-05-23T06:24:46.418125+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "cost-verify-agent-rl",
  "review_chat_id": "oc_648eaf83d2b24d445764257cf6a55525"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "cost-verify-agent-rl",
    "review_chat_id": "oc_648eaf83d2b24d445764257cf6a55525"
  }
}
```

</details>

---


### Tool result

_source line 131 · 2026-05-23T06:25:09.418868+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 23000
}
```

</details>

---


### Tool call

_source line 132 · 2026-05-23T06:25:10.322381+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "你是 Reviewer 1，负责**方法严谨性**审查。\n\n## Venue 信息\n- **目标**: EMNLP 2026 via ARR（Main + Findings 统一审稿）\n- **截止日期**: 2026-05-25\n- **页数限制**: Long paper 8 页正文，参考文献不限\n- **模板**: ACL template with `[review]` option\n- **匿名**: Double-blind\n- **Limitations**: 必须，在 conclusion 后 references 前，不计入页数\n- **评分标准**: 5=Consider for Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 论文路径\n- LaTeX: `projects/cost-verify-agent-rl/docs/paper/main.tex`（各章节为独立 .tex 文件在同目录）\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/review_round_1/submitted.pdf`\n\n## 你的审查侧重\n\n### 1. 理论推导\n- Proposition 1 和 Proposition 2 的推导是否严格？假设是否过强？\n- \"sign misattribution\" 在非 binary reward、连续 reward 下是否仍然成立？论文对此的讨论是否充分？\n- \"80.9% 的梯度方向错误\"这一核心 claim 的推导链是否有漏洞？\n- 理论分析假设 \"locally correct actions\" 但未定义什么是 locally correct——这是否是循环论证？\n\n### 2. 实验设计\n- 2×2 factorial design 是否真正隔离了两个 mechanism？Cell C（full observation + step-level advantage）的缺失是否是设计缺陷？\n- SFT baseline 12.5% in-distribution, 0% pre-SFT——这个 baseline 强度是否足以支撑结论？\n- 11-seed evaluation 的统计方法是否恰当？Fisher exact test 的使用条件是否满足？\n- seed variability 的分析（27% generalize）——是否有足够证据排除这只是随机波动？\n\n### 3. 统计可靠性\n- h-sweep 是单 seed——cliff claim 可靠性如何？\n- 8B 和 ScienceWorld 都是 single-seed——cross-scale/cross-env claim 的 evidence 是否太弱？\n- 置信区间宽度（如 seed1: [17.4, 31.8]）是否足以支持 \"statistically significant\" 的 claim？\n- OOD test set 仅 134 tasks——是否有 power 检测 5-10pp 差异？\n\n### 4. 可复现性\n- 超参数报告是否完整？\n- 训练步数仅 15 步——这是否足够？是否人为限制了其他 baseline 的表现？\n- RAGEN 框架的具体版本/commit 是否可追溯？\n\n### 输出格式\n请按以下结构输出审稿意见：\n1. **Summary**（2-3 句概括论文）\n2. **Strengths**（逐条）\n3. **Weaknesses**（逐条，标注 severity: Critical/Major/Minor）\n4. **Questions**（需要作者澄清的问题）\n5. **Missing References**（遗漏的重要相关工作）\n6. **Overall Assessment**（使用 EMNLP 2026 评分标准，给出分数 + 置信度 1-5）\n7. **Detailed Comments**（逐节意见）",
  "project": "cost-verify-agent-rl",
  "chat_id": "oc_648eaf83d2b24d445764257cf6a55525"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "你是 Reviewer 1，负责**方法严谨性**审查。\n\n## Venue 信息\n- **目标**: EMNLP 2026 via ARR（Main + Findings 统一审稿）\n- **截止日期**: 2026-05-25\n- **页数限制**: Long paper 8 页正文，参考文献不限\n- **模板**: ACL template with `[review]` option\n- **匿名**: Double-blind\n- **Limitations**: 必须，在 conclusion 后 references 前，不计入页数\n- **评分标准**: 5=Consider for Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 论文路径\n- LaTeX: `projects/cost-verify-agent-rl/docs/paper/main.tex`（各章节为独立 .tex 文件在同目录）\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/review_round_1/submitted.pdf`\n\n## 你的审查侧重\n\n### 1. 理论推导\n- Proposition 1 和 Proposition 2 的推导是否严格？假设是否过强？\n- \"sign misattribution\" 在非 binary reward、连续 reward 下是否仍然成立？论文对此的讨论是否充分？\n- \"80.9% 的梯度方向错误\"这一核心 claim 的推导链是否有漏洞？\n- 理论分析假设 \"locally correct actions\" 但未定义什么是 locally correct——这是否是循环论证？\n\n### 2. 实验设计\n- 2×2 factorial design 是否真正隔离了两个 mechanism？Cell C（full observation + step-level advantage）的缺失是否是设计缺陷？\n- SFT baseline 12.5% in-distribution, 0% pre-SFT——这个 baseline 强度是否足以支撑结论？\n- 11-seed evaluation 的统计方法是否恰当？Fisher exact test 的使用条件是否满足？\n- seed variability 的分析（27% generalize）——是否有足够证据排除这只是随机波动？\n\n### 3. 统计可靠性\n- h-sweep 是单 seed——cliff claim 可靠性如何？\n- 8B 和 ScienceWorld 都是 single-seed——cross-scale/cross-env claim 的 evidence 是否太弱？\n- 置信区间宽度（如 seed1: [17.4, 31.8]）是否足以支持 \"statistically significant\" 的 claim？\n- OOD test set 仅 134 tasks——是否有 power 检测 5-10pp 差异？\n\n### 4. 可复现性\n- 超参数报告是否完整？\n- 训练步数仅 15 步——这是否足够？是否人为限制了其他 baseline 的表现？\n- RAGEN 框架的具体版本/commit 是否可追溯？\n\n### 输出格式\n请按以下结构输出审稿意见：\n1. **Summary**（2-3 句概括论文）\n2. **Strengths**（逐条）\n3. **Weaknesses**（逐条，标注 severity: Critical/Major/Minor）\n4. **Questions**（需要作者澄清的问题）\n5. **Missing References**（遗漏的重要相关工作）\n6. **Overall Assessment**（使用 EMNLP 2026 评分标准，给出分数 + 置信度 1-5）\n7. **Detailed Comments**（逐节意见）",
    "project": "cost-verify-agent-rl",
    "chat_id": "oc_648eaf83d2b24d445764257cf6a55525"
  }
}
```

</details>

---


### Tool result

_source line 133 · 2026-05-23T06:25:34.511899+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_648eaf83d2b24d445764257cf6a55525:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 24189
}
```

</details>

---


### Tool call

_source line 134 · 2026-05-23T06:25:35.013955+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "你是 Reviewer 2，负责**新颖性与完整性**审查。\n\n## Venue 信息\n- **目标**: EMNLP 2026 via ARR（Main + Findings 统一审稿）\n- **截止日期**: 2026-05-25\n- **页数限制**: Long paper 8 页正文，参考文献不限\n- **模板**: ACL template with `[review]` option\n- **匿名**: Double-blind\n- **Limitations**: 必须，在 conclusion 后 references 前，不计入页数\n- **评分标准**: 5=Consider for Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 论文路径\n- LaTeX: `projects/cost-verify-agent-rl/docs/paper/main.tex`（各章节为独立 .tex 文件在同目录）\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/review_round_1/submitted.pdf`\n\n## 你的审查侧重\n\n### 1. 贡献新颖性\n- 核心贡献是\"诊断 step-independent training 的问题 + 回归 episode-level\"——这在多大程度上是 novel？Episode-level GRPO 本就是 GRPO 原始设计，论文是否在重新发现一个已知问题？\n- \"dual mechanism\" 分解（information loss + sign misattribution）是否是真正的新见解，还是已知 credit assignment 问题的重新包装？\n- 与 IRC、MC-GRPO、GRPO-λ、OAR 等同期工作的区分是否清晰充分？\n- 与 Turn-PPO、GAGPO、MT-GRPO、SWEET-RL 等方法的定位是否准确？\n\n### 2. Related Work 覆盖\n- 仅 20 篇引用——对 EMNLP 长文是否足够？\n- 是否遗漏了重要的 RL 基础工作（PPO、HER、reward shaping classics）？\n- 是否遗漏了 LLM agent 训练的重要工作（WebAgent、AgentTuning、FireAct、Reflexion、AgentBench、WebShop、InterCode）？\n- 是否遗漏了 multi-turn RL 的最新工作？用 web search 验证。\n- 引用格式是否规范（arXiv preprint vs 正式发表）？是否有 \"Author = Anonymous\" 的引用（不应出现在正式提交中）？\n\n### 3. 写作质量\n- Abstract 是否准确反映了论文贡献？是否有 overclaim？\n- Introduction 的 narrative 是否清晰？contribution list 是否准确？\n- 各章节之间的逻辑过渡是否流畅？\n- 术语使用是否一致（如 \"step-independent\" vs \"window-level\" vs \"step-level\"）？\n- Limitations 部分是否充分覆盖了关键局限性？\n- 是否有 AI 生成文本的痕迹（如过度使用 \"crucial\", \"fundamental\", \"novel\", \"comprehensive\"）？\n\n### 4. 格式合规（EMNLP 2026 / ARR）\n- 正文是否在 8 页内？（检查各 section 长度估算）\n- Limitations section 位置是否正确（正文中，conclusion 后 references 前）？\n- 匿名是否完整（无自引泄漏身份）？\n- 附录内容是否适当？是否有应在正文中的关键信息被放到了附录？\n- 是否有且只有一个 Limitations section？\n\n### 5. 论文 framing 与 claim 强度\n- \"necessary but not sufficient\" 的 claim 是否得到了充分支持？\n- 27% generalization rate 下，论文是否 undersell 了这个负面结果？还是 oversell 了 episode-level fix？\n- Discussion 中的 \"practitioner guidance\" 是否过于 prescriptive（考虑到有限的实验支持）？\n\n### 输出格式\n请按以下结构输出审稿意见：\n1. **Summary**（2-3 句概括论文）\n2. **Strengths**（逐条）\n3. **Weaknesses**（逐条，标注 severity: Critical/Major/Minor）\n4. **Questions**（需要作者澄清的问题）\n5. **Missing References**（遗漏的重要相关工作）\n6. **Overall Assessment**（使用 EMNLP 2026 评分标准，给出分数 + 置信度 1-5）\n7. **Detailed Comments**（逐节意见）",
  "project": "cost-verify-agent-rl",
  "chat_id": "oc_648eaf83d2b24d445764257cf6a55525"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "你是 Reviewer 2，负责**新颖性与完整性**审查。\n\n## Venue 信息\n- **目标**: EMNLP 2026 via ARR（Main + Findings 统一审稿）\n- **截止日期**: 2026-05-25\n- **页数限制**: Long paper 8 页正文，参考文献不限\n- **模板**: ACL template with `[review]` option\n- **匿名**: Double-blind\n- **Limitations**: 必须，在 conclusion 后 references 前，不计入页数\n- **评分标准**: 5=Consider for Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 论文路径\n- LaTeX: `projects/cost-verify-agent-rl/docs/paper/main.tex`（各章节为独立 .tex 文件在同目录）\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/review_round_1/submitted.pdf`\n\n## 你的审查侧重\n\n### 1. 贡献新颖性\n- 核心贡献是\"诊断 step-independent training 的问题 + 回归 episode-level\"——这在多大程度上是 novel？Episode-level GRPO 本就是 GRPO 原始设计，论文是否在重新发现一个已知问题？\n- \"dual mechanism\" 分解（information loss + sign misattribution）是否是真正的新见解，还是已知 credit assignment 问题的重新包装？\n- 与 IRC、MC-GRPO、GRPO-λ、OAR 等同期工作的区分是否清晰充分？\n- 与 Turn-PPO、GAGPO、MT-GRPO、SWEET-RL 等方法的定位是否准确？\n\n### 2. Related Work 覆盖\n- 仅 20 篇引用——对 EMNLP 长文是否足够？\n- 是否遗漏了重要的 RL 基础工作（PPO、HER、reward shaping classics）？\n- 是否遗漏了 LLM agent 训练的重要工作（WebAgent、AgentTuning、FireAct、Reflexion、AgentBench、WebShop、InterCode）？\n- 是否遗漏了 multi-turn RL 的最新工作？用 web search 验证。\n- 引用格式是否规范（arXiv preprint vs 正式发表）？是否有 \"Author = Anonymous\" 的引用（不应出现在正式提交中）？\n\n### 3. 写作质量\n- Abstract 是否准确反映了论文贡献？是否有 overclaim？\n- Introduction 的 narrative 是否清晰？contribution list 是否准确？\n- 各章节之间的逻辑过渡是否流畅？\n- 术语使用是否一致（如 \"step-independent\" vs \"window-level\" vs \"step-level\"）？\n- Limitations 部分是否充分覆盖了关键局限性？\n- 是否有 AI 生成文本的痕迹（如过度使用 \"crucial\", \"fundamental\", \"novel\", \"comprehensive\"）？\n\n### 4. 格式合规（EMNLP 2026 / ARR）\n- 正文是否在 8 页内？（检查各 section 长度估算）\n- Limitations section 位置是否正确（正文中，conclusion 后 references 前）？\n- 匿名是否完整（无自引泄漏身份）？\n- 附录内容是否适当？是否有应在正文中的关键信息被放到了附录？\n- 是否有且只有一个 Limitations section？\n\n### 5. 论文 framing 与 claim 强度\n- \"necessary but not sufficient\" 的 claim 是否得到了充分支持？\n- 27% generalization rate 下，论文是否 undersell 了这个负面结果？还是 oversell 了 episode-level fix？\n- Discussion 中的 \"practitioner guidance\" 是否过于 prescriptive（考虑到有限的实验支持）？\n\n### 输出格式\n请按以下结构输出审稿意见：\n1. **Summary**（2-3 句概括论文）\n2. **Strengths**（逐条）\n3. **Weaknesses**（逐条，标注 severity: Critical/Major/Minor）\n4. **Questions**（需要作者澄清的问题）\n5. **Missing References**（遗漏的重要相关工作）\n6. **Overall Assessment**（使用 EMNLP 2026 评分标准，给出分数 + 置信度 1-5）\n7. **Detailed Comments**（逐节意见）",
    "project": "cost-verify-agent-rl",
    "chat_id": "oc_648eaf83d2b24d445764257cf6a55525"
  }
}
```

</details>

---


### Tool result

_source line 135 · 2026-05-23T06:25:37.201773+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_648eaf83d2b24d445764257cf6a55525:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 2187
}
```

</details>

---


### Assistant

_source line 136 · 2026-05-23T06:25:46.512206+00:00_

Round 1 已派发：

- ✅ **视觉审查 Agent** — 已启动（fire-and-forget）
- ✅ **Reviewer 1**（方法严谨性）— 理论推导、实验设计、统计可靠性、可复现性
- ✅ **Reviewer 2**（新颖性/完整性）— 贡献新颖性、Related Work 覆盖、写作质量、格式合规

等待两位 Reviewer 返回初审意见，之后进入 Step 2（交叉分享）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director"
}
```

</details>

---


## Round 9

## Round 9

6 recorded events


### User

_source line 137 · 2026-05-23T06:31:54.238464+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1: 方法严谨性审查

## Summary

本文诊断了多轮 agent RL 中 step-independent windowing 的一个基本缺陷：advantage sign misattribution。论文识别了两个机制——policy information loss (M1) 和 sign misattribution (M2)——并通过 2×2 factorial 设计实验分离验证。在 ALFWorld 上，episode-level GRPO 被提出作为修复方案，并在 1.7B/8B 两个规模和 ScienceWorld 上进行了交叉验证。11-seed 评估揭示了即使修复后仍存在的 seed 依赖性。

---

## Strengths

**S1. 精准的问题诊断。** 论文识别出一个实践中广泛存在但未被形式化的 failure mode。将"step-independent training 崩溃"分解为两个可分离的机制（M1: information loss 造成 ceiling, M2: sign misattribution 造成 divergence），这种结构化分析对社区有明确价值。

**S2. Factorial 实验设计结构合理。** A→B 去除 M2（collapse → bounded learning），B→D 去除 M1（bounded → generalization），加上 dense reward、γ sweep、REINFORCE++ 等控制实验系统地排除了替代解释。这种实验方法论值得肯定。

**S3. 坦诚的 seed variability 分析。** 11-seed 评估（Table 2）是本文的亮点之一。论文诚实报告了只有 27% 的 seed generalize 的结果，而非 cherry-pick 最好的 seed。这种负面结果的透明报告是学术诚实的体现。

**S4. 多层次验证。** Sign misattribution verification (Section 4.4) 通过 credit agreement rate (52.07% ≈ random) 和 advantage sign 与 episode outcome 的高相关 (r>0.99) vs. local quality 的低相关 (r=0.068) 提供了经验支撑。γ=1.0 同样崩溃的实验排除了 discounting 的替代假说。

**S5. 写作清晰。** 论文结构紧凑，narrative 逻辑清楚，从问题诊断到实验验证到 fix 的推进自然。

---

## Weaknesses

### Critical

**C1 [critical] Proposition 1-2 的核心概念 "locally correct actions" 缺乏形式定义——存在循环论证风险**

- 具体位置：Section 3 (Proposition 1, line 6), Appendix A.1 (Proof of Proposition 1, line 11)
- 问题：整个理论框架建立在 "locally correct actions" 的概念上，但论文从未给出形式定义。Proof of Proposition 1 定义 "correct sign" 为 "for a window containing locally beneficial actions, the correct sign of Â_k is positive"，但 "locally beneficial" 本身未定义。如果定义为 "好的 policy 会采取的行动"，则论证是循环的——我们用尚不存在的好 policy 来判断当前 gradient 方向是否正确。如果定义为 "增加 episode 成功概率的行动"，则需要因果推断（反事实），单窗口内无法确定。
- 为什么影响接收：这不是 notation 问题，而是理论贡献的逻辑基础。Proposition 2 的 "80.9% incorrect sign" 这一核心 claim 的含义完全取决于 "correct" 的定义。
- 建议修改方向：(a) 给出 "locally correct" 的操作性定义（例如基于 oracle policy 或 expert demonstrations 的行为匹配）；(b) 在 Section 4.4 的 credit agreement rate 实验中明确说明 "local action quality" 的度量方式（是 action validity？expert action match？还是其他 proxy？）；(c) 讨论定义选择对理论结论的敏感性。

**C2 [critical] 理论分析仅限 binary reward，non-binary 扩展缺乏严格性**

- 具体位置：Proposition 1-2 (Section 3), Appendix A.2 Remark
- 问题：Propositions 1-2 的推导严格依赖 binary reward (R ∈ {0, r+})。对于 non-binary reward（如 per-step penalty for invalid actions），Appendix Remark 仅给出定性论述 "the qualitative conclusion is preserved" 而无证明。但论文的实验设置实际上使用了 non-binary reward structure（invalid action penalty = 0.1, Appendix B），理论与实验之间存在 gap。当 reward 非 binary 时，即使 episode 失败，不同 window 的 return 可能不同（因为 invalid action penalty），group normalization 下 advantage sign 不再简单由 episode outcome 决定。
- 为什么影响接收：理论与实验使用了不同的 reward structure，削弱了理论对实验的解释力。
- 建议修改方向：(a) 要么在 pure binary reward 下重做实验以完全匹配理论假设；(b) 要么将 Proposition 2 扩展到包含 per-step penalties 的情况，至少给出 bound；(c) 或者明确讨论 invalid action penalty 对理论预测的定量影响。

### Major

**M1 [major] 2×2 Factorial 的 Cell C 缺失使 M2 无法独立验证**

- 具体位置：Section 2.5, Section 4.2
- 问题：论文声称 2×2 factorial，但只实现了 3 个 cell。Cell C (full observation + step-level advantage) 被论述为 "degenerate"——理由是 full observation 只有一个 window，step-level 和 episode-level advantage 相同。这个 degeneracy argument 在逻辑上成立，但它意味着 M2 的效果永远无法在没有 M1 的条件下被独立测量。A→B 比较确实去除了 M2，但这只证明了 M2 在 M1 存在时的破坏性，不能排除 M1+M2 的交互效应。论文 Discussion 部分也承认了 M1 与 M2 的 "vicious cycle"（M1 降低 p，加剧 M2），这正是交互效应的体现。
- 建议：(a) 明确承认 Cell C 的缺失是设计限制而非 degeneracy 的自然结果；(b) 考虑一个中间方案：full observation + 多个 window（每个 window 看到全部 history 但分别计算 advantage），这可以在不引入 M1 的情况下测试 M2；(c) 至少在 discussion 中更充分地讨论交互效应对结论的影响。

**M2 [major] h-sweep cliff claim 基于 single seed，统计证据不足**

- 具体位置：Section 4.3 ("Window-size sweep"), Figure 1(b)
- 问题：Figure 1(b) 的 caption 和 Section 4.3 明确说明 h-sweep 是 "seed 1" 的单 seed 结果。从 h=10 (6.25%) 到 h=20 (15.6%) 的 "credit assignment cliff" claim 基于 n=1，无法排除 seed-specific 噪声。结合 Table 2 显示的高 seed variability（同一方法下 OOD 从 8.21% 到 30.60%），单 seed 的 h-sweep 结果的可信度很低。
- 为什么影响评分：这个 cliff 是论文的 key empirical insight 之一（呼应 Proposition 2 的理论预测），但 evidence 太弱。
- 建议：至少在 h=5, h=10, h=20 这三个关键点各跑 2-3 seeds，报告均值和范围。

**M3 [major] 8B 和 ScienceWorld 的 cross-scale/cross-environment claims 均基于 single seed**

- 具体位置：Section 4.6 (Table 3), Section 4.7
- 问题：论文声称 cross-scale (1.7B→8B) 和 cross-environment (ALFWorld→ScienceWorld) generality，但两者均为 single seed。Table 3 caption 未提及 seed 数量，Limitations 才承认 "single-seed runs due to computational constraints"。考虑到 1.7B 的 11-seed 评估中 27% collapse 率，单 seed 的 8B 结果可能恰好是 lucky seed。ScienceWorld 同理。这些 single-seed 结果可以作为 preliminary evidence，但论文的写法（"Both mechanisms operate across environments, confirming the dual-mechanism failure is not ALFWorld-specific"）将其呈现为 confirmatory evidence，这与实际 statistical power 不符。
- 建议：(a) 将 cross-scale/cross-environment 结论的语气降级为 "preliminary evidence" 或 "suggestive"；(b) 或增加 seeds。

**M4 [major] "80.9% 梯度方向错误" 的 claim 是 upper bound 而非精确值，但论文呈现为精确数字**

- 具体位置：Abstract, Section 3, Section 7 (Conclusion)
- 问题：Proposition 2 的推导隐含假设所有 window 都包含 "locally correct actions"。但在实际 failed episode 中，部分 window 可能确实包含差的行动（应该被 penalize）。因此 80.9% 是"对 locally correct windows 的错误 gradient 比例"而非"所有 gradient 的错误比例"。但 Abstract ("80.9% of gradient updates for locally correct actions carry incorrect sign") 和 Conclusion ("~80.9% of gradient updates carry incorrect sign") 的措辞有差异——Abstract 有 qualifier "for locally correct actions"，但 Conclusion 省略了，有误导性。
- 建议：(a) 统一措辞，全文保持 "for windows with locally correct actions" 的 qualifier；(b) 估计实际 trajectory 中 "locally correct windows" 的比例，给出 overall incorrect gradient rate。

**M5 [major] 15 步训练——步数极少，可能系统性不利于 baseline 方法**

- 具体位置：Section 4.1, Appendix B (Table 4: Training steps = 15)
- 问题：15 个 training step 对于 RL 训练来说极少。虽然 Cell A 在 3-9 步内崩溃，Cell D 在 15 步内单调改善，但 dense reward 和 REINFORCE++ 的 "失败" 可能部分归因于训练不足。特别是 REINFORCE++ 12.5%（等于 SFT baseline）可能只是还没开始学习。Paper 的 Discussion 承认 seed100 在 step 5→10 只增加 1.5pp，但这是 episode-level 的结果——step-independent 或 REINFORCE++ 的收敛速度可能完全不同。
- 建议：(a) 至少对 Cell D（主方法）跑更多步数观察是否还能继续提升；(b) 对 REINFORCE++ 这样的竞争方法，考虑给予更多训练步数确认它确实不工作。

### Minor

**m1 [minor]** Table 1 对不同 cell 使用了不同的报告标准：Cell A "reports best seed"，Cell B "reports best checkpoint (step 5)"，Cell D "reports mean of two seeds"。应统一标准（全部报告 mean 或 both seeds）。

**m2 [minor]** Equation 3 使用 ≈ 号（sign(Â_k) ≈ sign(R_episode − μ)）但未明确在什么条件下这是精确的 vs. 近似的。如果 invalid action penalty 使不同 window 的 return 不同，这个近似的误差是多大？

**m3 [minor]** Section 4.4 的 "credit agreement rate" 和 "local action quality" 的 operationalization 未在正文或附录中描述。如何度量 "local action quality"？是对比 expert action？还是使用 oracle reward？

**m4 [minor]** Appendix A.3 讨论了 "Why the Community Defaults to Step-Independent Training"，列出 6 个因素。这部分偏 editorial/opinion，缺乏文献支撑。特别是 Factor 3 ("Framework design accident") 对 RAGEN 的描述接近 blame，可能不适合 blind review。

**m5 [minor]** RAGEN 框架的具体 version/commit hash 未报告。鉴于论文的核心论点之一是 RAGEN 的默认配置导致问题，可复现性要求知道确切版本。

---

## Questions（需要作者澄清）

**Q1.** Section 4.4 中 "local action quality" 具体如何度量？是 action validity (format correctness)，还是与 expert demonstration 的匹配度，还是其他 metric？

**Q2.** Proposition 2 的推导假设 binary reward，但实验使用了 invalid action penalty (0.1)。你们是否在 pure binary reward（无 invalid action penalty）的条件下验证了 credit agreement rate？如果有，结果与 52.07% 有多大差异？

**Q3.** Table 2 中 seed1 标记为 "RAGEN built-in eval; checkpoint unavailable for re-evaluation"——这意味着 seed1 的结果无法用统一的评估 pipeline 复现。其他 seed 的 evaluation protocol 是否完全一致？如果 seed1 使用了不同的 eval 方式，其结果是否与其他 seed 可比？

**Q4.** 论文声称 "episode-level GRPO resolves both mechanisms"，但 11 seed 中只有 27% generalize。这是否说明 sign misattribution 只是训练失败的 necessary condition 之一，而非 sufficient explanation？

**Q5.** Figure 2(b) 显示 collapse 伴随 response length inflation（14,000-16,000 tokens）。这是否暗示 collapse 可能与 KL penalty (β=0.01) 太弱有关，而非完全归因于 sign misattribution？

---

## Missing References

1. **Process Reward Models (PRMs)**: Lightman et al. (2023), "Let's Verify Step by Step" — 这是 step-level credit assignment 的重要参考，与本文的 "step-level vs episode-level" 框架直接相关。
2. **Math-Shepherd** (Wang et al., 2023) — process reward model for math reasoning，也涉及 step-level credit 的自动标注。
3. **COMA** (Foerster et al., 2018) — Counterfactual Multi-Agent Policy Gradients, 在 Appendix A.4 提及了 multi-agent analogy 但未引用 COMA。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| **Soundness** | 3/5 | 理论推导在 binary reward 下数学正确，但 "locally correct actions" 缺乏形式定义构成逻辑漏洞。实验设计整体合理（factorial, controls），但关键 claims（h-sweep cliff, cross-scale, cross-env）基于 single seed，统计 power 不足。理论与实验的 reward structure 不一致（binary vs. binary+penalty）削弱解释力。 |
| **Excitement** | 3.5/5 | 问题识别有价值——step-independent windowing 的 sign misattribution 是一个实践中广泛存在且未被充分理解的 failure mode。诊断框架（M1/M2 分离）对社区有指导意义。但 fix（episode-level GRPO）本身是已知方法，且只有 27% seed generalize，实用性有限。 |
| **Reproducibility** | 3/5 | 超参数报告基本完整（Table 4），但 RAGEN 版本未指定；seed1 的 eval 与其他 seed 不一致；"local action quality" 的度量未描述。 |
| **Reviewer Confidence** | 4/5 | 我对 RL credit assignment 和 GRPO 有充分了解，仔细阅读了理论推导和实验细节。可能遗漏了 ALFWorld/ScienceWorld 的领域特定细节。 |

---

## Overall Assessment

**Overall: 3.0 — Findings**

**一句话总结：** 论文精准诊断了一个重要的 failure mode（sign misattribution），实验设计思路清晰，但理论框架的核心概念（"locally correct actions"）缺乏形式定义，关键跨规模/跨环境 claims 的 statistical evidence 过弱（single seed），fix 的实用性受限于仅 27% 的 seed 能 generalize。

本文的贡献主要在于诊断和分析（负面结果的价值），而非方法创新。理论部分虽然数学推导在其假设下正确，但假设本身的形式化不足使其更接近 "insightful empirical observation + back-of-envelope calculation" 而非严格的理论贡献。如果能 (1) 形式化 "locally correct" 的定义并讨论敏感性，(2) 为 h-sweep cliff 和 cross-scale claims 补充多 seed 证据，(3) 统一理论与实验的 reward structure，本文将是一篇强有力的 Findings 到 Conference 级别的工作。

---

## 主要优势（总结）

1. 问题识别精准——sign misattribution 是一个 real problem，对 multi-turn agent RL 社区有明确指导意义
2. 实验设计思路好——factorial design + 系统排除替代假说（dense reward, γ, REINFORCE++）
3. 坦诚的 seed variability 分析——负面结果的透明报告提升了可信度
4. 清晰的写作和论证结构


---

[Reviewer 2 审稿意见]:

# Reviewer 2 审稿意见：新颖性与完整性

## 1. Summary

本文诊断了多轮 agent RL 中 step-independent windowing 导致训练崩溃的原因，将其分解为两个机制：(1) policy information loss（截断上下文导致性能天花板）和 (2) advantage sign misattribution（梯度方向错误导致累积退化）。通过 2×2 factorial 实验分离两个机制的贡献，并展示 episode-level GRPO（即 GRPO 原始设计）可解决两者，但 11-seed 评估显示仅 27% 的 seed 实现显著 OOD 泛化。

## 2. Strengths

**S1. 干净的实验方法论。** 2×2 factorial design（Cell A/B/D）是诊断性研究的典范做法，清晰分离了两个机制的独立贡献：A→B 消除 sign misattribution 将崩溃转为有界学习，B→D 消除 information loss 开启泛化。这种控制变量的严谨性在同期工作中少见。

**S2. 诚实的负面结果报告。** 11-seed 评估揭示仅 27% 泛化率，论文没有回避这个事实，并明确将 episode-level fix 定义为 "necessary but not sufficient"。这种坦诚在投稿论文中难得，也增加了可信度。

**S3. 跨尺度和跨环境验证。** 1.7B→8B（ALFWorld）和 ALFWorld→ScienceWorld 的验证增强了机制诊断的普适性。8B 结果（90.3% OOD）特别有说服力。

**S4. 理论预测与实验验证的闭环。** Proposition 2 预测 ~19.1% correct sign rate，实测 52% credit agreement ≈ random chance（二元环境下两者等价），形成了预测-验证的完整链条。

**S5. 实用的 practitioner guidance。** Discussion 中的具体建议（episode-level first, h≥20, 先建立正确梯度方向再用细粒度 credit）对实践者有直接价值。

## 3. Weaknesses

### Critical

**W1. [Critical] 引用格式严重违规：10/20 引用使用 "Anonymous" 作为作者**
- 具体位置：references.bib 中的 irc2026, grpolambda2025, oar2026, ragen2_2026, grpocollapse2025, gradientcoupling2025, turnppo2026, gagpo2026, mtgrpo2025, sweetrl2025
- 问题：这些均为已公开在 arXiv 的预印本，有可查的真实作者信息。例如 IRC (arXiv:2604.02869) 有明确作者列表，GRPO-λ (arXiv:2510.00194)、OAR (arXiv:2601.07408)、MT-GRPO (arXiv:2505.11821)、SWEET-RL (arXiv:2503.15478) 均如此。在 ACL ARR double-blind 审稿中，仅需匿名化**自己**的在审稿件，不应将**他人**已公开发表的工作标为 "Anonymous"。
- 两种可能的解读都有问题：(a) 如果这些是自引——50% 自引率极不正常，且构成匿名泄露风险；(b) 如果不是自引——错误地匿名化他人工作违反学术引用规范。
- 影响：这是 ARR desk-rejection checklist 中会被标记的格式问题。

**W2. [Critical] 核心贡献的新颖性存疑**
- 具体位置：Section 2.4, Section 7, Contribution list (Section 1)
- 问题：论文的 "fix" 是回归 GRPO 的**原始设计**（episode-level），论文自己在 Section 2.4 也承认 "This is GRPO's original design—step-independent windowing is the deviation"。这意味着论文本质上是在诊断**为什么一个已知的坏实践是坏的**，而非提出新方法。
- Dual mechanism 分解（M1+M2）的框架虽然整洁，但：
  - M1（information loss from context truncation）是截断上下文必然导致的后果，几乎是 trivial observation
  - M2（sign misattribution）本质上是 sparse reward 下 credit assignment 问题的重新表述——这是 RL 领域数十年的经典问题
- 同期大量工作已独立发现类似问题：IRC 报告 per-turn advantage 与 outcome advantage 符号不一致，MC-GRPO 测量 5% sign-flip rate，GRPO-λ 证明 value estimation error 随位置增长，OAR 识别 "reward aliasing"，RAGEN-2 证明 advantage collapse。论文虽然引用了这些工作（Section 5），但没有充分论证自身的**增量贡献**超越这些并行发现。
- 为什么影响接收：ARR Excitement 维度要求 "new understanding"。如果社区已经通过多个独立工作收敛到相同诊断，本文的边际贡献需要更有力的论证。

### Major

**W3. [Major] 引用数量严重不足：仅 20 篇引用**
- 具体位置：References (page 8-9)
- 问题：对于 EMNLP long paper（8 页正文），20 篇引用远低于领域惯例（通常 40-60 篇）。以下重要类别的工作完全缺失：
  - **RL 基础**：PPO (Schulman et al., 2017) 未引用——这是论文多次提到 "PPO" 的前提；TRPO、Hindsight Experience Replay (HER)、经典 reward shaping (Ng et al., 1999) 均缺失
  - **LLM Agent 训练/评估基础工作**：WebAgent, AgentTuning (Zeng et al., 2023), FireAct (Chen et al., 2023), Reflexion (Shinn et al., 2023), AgentBench (Liu et al., 2023), WebShop (Yao et al., 2022), InterCode 均未引用
  - **近期同方向工作**：RC-GRPO (arXiv:2602.03025), TSR (arXiv:2602.11767, ICLR 2026 Workshop) 未引用
  - **多智能体 credit assignment**：论文在 Appendix A.4 画了多智能体类比，但未引用 COMA, QMIX, VDN 等经典方法
- 影响：引用不足会被 reviewer 视为对领域了解不充分的信号，也使 Related Work 的覆盖面论证不可信。

**W4. [Major] 8B 和 ScienceWorld 实验仅单 seed**
- 具体位置：Section 4.6, Section 4.7, Limitations
- 问题：论文在 1.7B 上用了 11 seeds 并发现巨大的 seed 依赖性（27% 崩溃、36% 停滞、27% 泛化），但 8B 和 ScienceWorld 实验仅用单 seed。鉴于论文自身证明了 seed 选择对结果的决定性影响，单 seed 结果的可靠性严重存疑。8B 的 90.3% OOD 可能是幸运的 seed。
- Limitations 中虽然提到了 "computational constraints"，但这不构成充分辩护——如果 seed 依赖性是论文的核心发现之一，那么对所有关键实验都应有多 seed 验证。

**W5. [Major] 理论分析深度有限**
- 具体位置：Section 3, Appendix A
- 问题：Proposition 1 和 2 是在 binary reward + GRPO group normalization 假设下的直接概率计算，推导过程约 1 页即可完成。论文将其包装为 "theoretical analysis"，但：
  - 核心结论 P(correct | update) = p / [1-(1-p)^K] 是一个简单的条件概率公式
  - 仅在 binary reward 下成立（Remark 已承认），对连续 reward 的推广仅是定性断言
  - 没有收敛/发散的形式化分析——"sign errors cause active divergence" 仅是直觉论证，缺乏梯度动态系统的严格分析
- 如果论文将理论贡献作为三大贡献之一，应有更深的分析（例如，在什么条件下 sign error 导致发散的收敛率分析）。

### Minor

**W6. [Minor] "fundamental" 一词过度使用**
- 出现位置：Abstract ("fundamental credit assignment pathology"), Section 1 ("fundamental credit assignment pathology"), Section 2.3 ("the more fundamental failure mechanism"), Appendix A.1 ("fundamentally more harmful", "fundamentally flawed")
- 至少出现 5 次以上，在学术写作中显得夸大且有 AI 生成文本的痕迹。

**W7. [Minor] 部分实验条件缺少消融细节**
- 具体位置：Section 4.4 (Dense reward, Figure 4)
- Dense reward 实验的 reward 设计（+0.15 per valid action）仅在 Appendix C 一句话描述，main text 中引用但未充分解释。这个实验是支持 M2 诊断的关键证据之一，应在正文中给出更多细节。

**W8. [Minor] Figure 1(a) 的 y 轴标签和图例可读性**
- 具体位置：Figure 1(a), page 5
- Training dynamics 图的 y 轴同时展示两种 metric（OOD success rate 和其他 metric types），但图例中仅用颜色区分 Cell A/B/D，metric type 的区分不够直观。

## 4. Questions

**Q1.** 论文声称 "step-independent windowing is the deviation" from GRPO's original design。但 RAGEN 之所以引入 windowing，是因为长序列的内存约束。论文是否在 1.7B 实验中实际遇到了内存问题？如果 episode-level training 在 1.7B 上没有内存问题，那 RAGEN 引入 windowing 的动机需要更仔细的分析。如果有内存问题，论文应量化 episode-level 的额外计算成本。

**Q2.** 11-seed 评估中 27% 泛化率——是否有分析哪些 seed 的初始化特征（例如 SFT checkpoint 的局部性质）导致了泛化 vs 停滞？这对论文的实际价值至关重要：如果无法预测哪些 seed 会泛化，practitioner guidance 的实用性大打折扣。

**Q3.** Proposition 2 的推导假设 binary reward。在 ALFWorld 实验中，实际使用了 invalid action penalty (0.1)，这意味着 reward 不是严格 binary 的。这如何影响理论预测的准确性？论文仅在 Remark 中定性提到 "qualitative conclusion is preserved"，但没有量化分析。

**Q4.** Cell B（h=2 + episode-level advantage）最好成绩 5.97% OOD 并逐步收敛到 0.75%。这个衰减的机制是什么？如果 sign misattribution 已被消除，为什么还会出现性能下降？这似乎暗示还有第三个未被分析的机制。

**Q5.** 论文将 GiGPO、GAGPO、Turn-PPO 等定位为 "address symptoms but not the structural root cause"。但这些方法中有些（如 GAGPO 使用 turn-level critic）在原理上直接解决了 credit assignment 问题。论文是否有与这些方法的直接实验对比？

## 5. Missing References

### 必须补充的基础工作
- **Schulman et al., 2017** — PPO（论文多处提到 PPO 但未引用原始论文）
- **Ng et al., 1999** — Policy invariance under reward transformations / reward shaping theory
- **Yao et al., 2023** — ReAct（agent 推理范式的奠基工作）

### 应该补充的 Agent 训练/评估工作
- **Zeng et al., 2023** — AgentTuning
- **Shinn et al., 2023** — Reflexion
- **Yao et al., 2022** — WebShop
- **Liu et al., 2023** — AgentBench
- **Chen et al., 2023** — FireAct

### 应该讨论的近期同方向工作
- **RC-GRPO** (arXiv:2602.03025, 2026) — Reward-Conditioned GRPO for multi-turn tool calling
- **TSR** (arXiv:2602.11767, ICLR 2026 Workshop) — Trajectory-Search Rollouts for multi-turn RL
- **"From Reasoning to Agentic: Credit Assignment in RL for LLMs"** (arXiv:2604.09459, 2026) — 综述性工作，直接覆盖本文主题

### 多智能体 credit assignment（论文 Appendix 中画了类比但未引用）
- **Foerster et al., 2018** — COMA
- **Rashid et al., 2018** — QMIX

## 6. Overall Assessment

**Overall**: 2.5 (Borderline Findings)

**Soundness**: 3.5/5 — 实验方法论（factorial design）扎实，但理论分析偏浅，10/20 引用使用 "Anonymous" 是严重格式问题。

**Excitement**: 2.5/5 — 诊断框架整洁但增量贡献有限：(a) "fix" 是回归原始算法，(b) 同期多个独立工作已收敛到类似诊断，(c) 27% 泛化率+无法解释的 seed 依赖性限制了实际影响力。

**Reproducibility**: 3.5/5 — 超参数公开（Appendix B），使用已有框架（RAGEN），但 8B 和 ScienceWorld 仅单 seed。

**Reviewer Confidence**: 4/5 — 对 agent RL credit assignment 领域较为熟悉，已验证主要 related work 覆盖。

**一句话总结**: 实验方法论干净（factorial design 值得学习），诊断有价值但边际贡献有限——核心 "fix" 是回归原始算法，引用格式问题严重（50% Anonymous），20 篇引用对 EMNLP long paper 明显不足。

## 7. Detailed Comments

### Section 1 (Introduction)
- "fundamental credit assignment pathology" 在 abstract 和 intro 中重复出现，措辞过重。建议弱化为 "systematic" 或 "structural"。
- Contribution 3 "necessary but not sufficient" 虽然诚实，但从审稿角度看，这意味着论文提出的方案在 73% 的情况下无法实现目标（仅 27% generalize）。这削弱了整体贡献的 impact。

### Section 2 (Method)
- Section 2.1 的 POMDP 形式化是标准的，没有问题。
- Section 2.3 的 dual mechanism analysis 写得清晰，M1 和 M2 的区分（constant ceiling vs cumulative degradation）是论文最有价值的概念贡献。
- Eq. 3 的推导 sign(Â_k) ≈ sign(R_episode - μ) 是直觉层面的近似，缺乏正式的误差界。

### Section 3 (Theoretical Analysis)
- Proposition 1 的 "proof sketch" 实际上就是完整证明的简化版，标记为 sketch 有些过谦。
- Proposition 2 的公式 P(correct | update) = p/[1-(1-p)^K] 是论文最核心的理论贡献，推导清晰。但应讨论当 p 随训练变化时（即 p 不是常数）公式的适用性——实际上 p 在训练过程中会下降（因为 sign error 导致策略退化），这会产生正反馈循环。论文在 Discussion 的 "mechanism interaction" 段落定性提到了这点，但理论部分没有形式化。

### Section 4 (Experiments)
- Table 1 的实验设计干净，但 Cell A 报告的是 "best seed" 而非 mean，Cell B 报告的是 "best checkpoint (step 5)"——这种 cherry-picking 最佳结果的做法与 Cell D 报告 mean 不一致。建议统一报告标准。
- Section 4.4 的 sign verification（52% credit agreement）是论文的亮点实验，直接验证了理论预测。
- Section 4.5 的 11-seed 评估非常有价值，但 "collapsed" 的定义（>50% decline from peak for ≥3 steps）是否过于宽松？sensitivity analysis 会加强可信度。
- Table 3 (8B results) 使用不同的解码温度（SFT 用 τ=0, RL 用 τ=0.4），这引入了额外变量。虽然在 agent 任务中常见，但应讨论温度差异对公平比较的影响。

### Section 5 (Related Work)
- 结构合理（5 段落覆盖 4 个子领域），但每段仅 3-5 句，覆盖面不足。
- "but all share a common assumption: trajectory decomposition into fixed windows is benign. We show this assumption is false" — 这个 claim 过强。GiGPO 和 GAGPO 等工作并非假设 windowing is benign，而是明确在 windowing 框架内改进 credit assignment。

### Section 6 (Discussion)
- "Mechanism interaction" 段落描述了 M1-M2 正反馈循环，这是论文最有洞察力的观察之一，但仅有定性描述。
- "Practitioner guidance" 的建议具体且有用，但基于仅两个环境的实验，generalizability 有限。

### Section 7 (Conclusion)
- 准确总结了论文贡献，没有 overclaim。

### Limitations
- 位置正确（Section 7 后，references 前）。
- 内容覆盖了关键局限（环境数量、scale 数量、seed 依赖性、长 episode 的局限），篇幅适当。
- 建议补充：理论分析仅适用于 binary reward 的局限性。

### Appendix
- A.3 (Why the Community Defaults to Step-Independent Training) 是有趣的分析，有一定独立价值。
- A.4 (Connection to Classical Credit Assignment) 画了有用的联系但过于简略。
- Appendix 中没有出现第二个 Limitations section，符合规定。

### 格式合规检查
- ✅ 正文 ≤ 8 页（Sections 1-7 + Limitations 在 page 8 内完成）
- ✅ Limitations 位置正确
- ✅ 使用 `[review]` 选项
- ✅ 匿名提交（"Anonymous ACL submission"）
- ✅ 仅一个 Limitations section
- ❌ 10/20 引用使用 "Anonymous" 作者——严重格式问题
- ⚠️ 仅 20 篇引用，偏少


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 138 · 2026-05-23T06:32:58.467002+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "以下是 Reviewer 2 的完整审稿意见。请逐条回应：对每个 Weakness 和 Question，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。对 Strengths 和 Missing References 也请简要评论是否认同。\n\n---\n\n# Reviewer 2 审稿意见：新颖性与完整性\n\n## 1. Summary\n\n本文诊断了多轮 agent RL 中 step-independent windowing 导致训练崩溃的原因，将其分解为两个机制：(1) policy information loss（截断上下文导致性能天花板）和 (2) advantage sign misattribution（梯度方向错误导致累积退化）。通过 2×2 factorial 实验分离两个机制的贡献，并展示 episode-level GRPO（即 GRPO 原始设计）可解决两者，但 11-seed 评估显示仅 27% 的 seed 实现显著 OOD 泛化。\n\n## 2. Strengths\n\n**S1. 干净的实验方法论。** 2×2 factorial design（Cell A/B/D）是诊断性研究的典范做法，清晰分离了两个机制的独立贡献：A→B 消除 sign misattribution 将崩溃转为有界学习，B→D 消除 information loss 开启泛化。这种控制变量的严谨性在同期工作中少见。\n\n**S2. 诚实的负面结果报告。** 11-seed 评估揭示仅 27% 泛化率，论文没有回避这个事实，并明确将 episode-level fix 定义为 \"necessary but not sufficient\"。这种坦诚在投稿论文中难得，也增加了可信度。\n\n**S3. 跨尺度和跨环境验证。** 1.7B→8B（ALFWorld）和 ALFWorld→ScienceWorld 的验证增强了机制诊断的普适性。8B 结果（90.3% OOD）特别有说服力。\n\n**S4. 理论预测与实验验证的闭环。** Proposition 2 预测 ~19.1% correct sign rate，实测 52% credit agreement ≈ random chance（二元环境下两者等价），形成了预测-验证的完整链条。\n\n**S5. 实用的 practitioner guidance。** Discussion 中的具体建议（episode-level first, h≥20, 先建立正确梯度方向再用细粒度 credit）对实践者有直接价值。\n\n## 3. Weaknesses\n\n### Critical\n\n**W1. [Critical] 引用格式严重违规：10/20 引用使用 \"Anonymous\" 作为作者**\n- 具体位置：references.bib 中的 irc2026, grpolambda2025, oar2026, ragen2_2026, grpocollapse2025, gradientcoupling2025, turnppo2026, gagpo2026, mtgrpo2025, sweetrl2025\n- 问题：这些均为已公开在 arXiv 的预印本，有可查的真实作者信息。在 ACL ARR double-blind 审稿中，仅需匿名化自己的在审稿件，不应将他人已公开发表的工作标为 \"Anonymous\"。\n- 两种可能的解读都有问题：(a) 如果这些是自引——50% 自引率极不正常，且构成匿名泄露风险；(b) 如果不是自引——错误地匿名化他人工作违反学术引用规范。\n- 影响：这是 ARR desk-rejection checklist 中会被标记的格式问题。\n\n**W2. [Critical] 核心贡献的新颖性存疑**\n- 论文的 \"fix\" 是回归 GRPO 的原始设计（episode-level），论文自己也承认。\n- M1（information loss from context truncation）几乎是 trivial observation。\n- M2（sign misattribution）本质上是 sparse reward 下 credit assignment 问题的重新表述。\n- 同期大量工作已独立发现类似问题（IRC, MC-GRPO, GRPO-λ, OAR, RAGEN-2）。\n\n### Major\n\n**W3. [Major] 引用数量严重不足：仅 20 篇引用**\n- 缺失类别：RL 基础（PPO, TRPO, HER, reward shaping classics）、LLM Agent 训练/评估（WebAgent, AgentTuning, FireAct, Reflexion, AgentBench, WebShop, InterCode）、近期同方向工作（RC-GRPO, TSR）、多智能体 credit assignment（COMA, QMIX）。\n\n**W4. [Major] 8B 和 ScienceWorld 实验仅单 seed**\n- 与 W4 from R1 一致。\n\n**W5. [Major] 理论分析深度有限**\n- P(correct | update) = p/[1-(1-p)^K] 是简单条件概率公式。\n- 缺乏收敛/发散的形式化分析。\n\n### Minor\n\n**W6. [Minor] \"fundamental\" 一词过度使用（5次+），有 AI 生成文本痕迹。**\n\n**W7. [Minor] Dense reward 实验细节不足。**\n\n**W8. [Minor] Figure 1(a) 可读性问题。**\n\n## 4. Questions\n\n**Q1.** RAGEN 引入 windowing 的动机是内存约束。论文在 1.7B 上是否遇到了内存问题？episode-level 的额外计算成本？\n\n**Q2.** 11-seed 中 27% 泛化率——是否分析了哪些 seed 的初始化特征导致泛化 vs 停滞？\n\n**Q3.** Proposition 2 假设 binary reward，但实验用了 invalid action penalty (0.1)，如何影响理论预测？\n\n**Q4.** Cell B 最好成绩 5.97% OOD 后逐步收敛到 0.75%，sign misattribution 已被消除，为什么还会下降？是否暗示第三个未分析的机制？\n\n**Q5.** 是否有与 GiGPO、GAGPO、Turn-PPO 的直接实验对比？\n\n## 5. Missing References\n（同上列出的 PPO, ReAct, AgentTuning, Reflexion, WebShop, AgentBench, FireAct, RC-GRPO, TSR, COMA, QMIX 等）\n\n## 6. Overall Assessment\n**Overall**: 2.5 (Borderline Findings)\nSoundness 3.5/5, Excitement 2.5/5, Reproducibility 3.5/5, Confidence 4/5\n\n## 7. Detailed Comments\n（见上文各节详细评论）",
  "project": "cost-verify-agent-rl",
  "chat_id": "oc_648eaf83d2b24d445764257cf6a55525"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "以下是 Reviewer 2 的完整审稿意见。请逐条回应：对每个 Weakness 和 Question，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。对 Strengths 和 Missing References 也请简要评论是否认同。\n\n---\n\n# Reviewer 2 审稿意见：新颖性与完整性\n\n## 1. Summary\n\n本文诊断了多轮 agent RL 中 step-independent windowing 导致训练崩溃的原因，将其分解为两个机制：(1) policy information loss（截断上下文导致性能天花板）和 (2) advantage sign misattribution（梯度方向错误导致累积退化）。通过 2×2 factorial 实验分离两个机制的贡献，并展示 episode-level GRPO（即 GRPO 原始设计）可解决两者，但 11-seed 评估显示仅 27% 的 seed 实现显著 OOD 泛化。\n\n## 2. Strengths\n\n**S1. 干净的实验方法论。** 2×2 factorial design（Cell A/B/D）是诊断性研究的典范做法，清晰分离了两个机制的独立贡献：A→B 消除 sign misattribution 将崩溃转为有界学习，B→D 消除 information loss 开启泛化。这种控制变量的严谨性在同期工作中少见。\n\n**S2. 诚实的负面结果报告。** 11-seed 评估揭示仅 27% 泛化率，论文没有回避这个事实，并明确将 episode-level fix 定义为 \"necessary but not sufficient\"。这种坦诚在投稿论文中难得，也增加了可信度。\n\n**S3. 跨尺度和跨环境验证。** 1.7B→8B（ALFWorld）和 ALFWorld→ScienceWorld 的验证增强了机制诊断的普适性。8B 结果（90.3% OOD）特别有说服力。\n\n**S4. 理论预测与实验验证的闭环。** Proposition 2 预测 ~19.1% correct sign rate，实测 52% credit agreement ≈ random chance（二元环境下两者等价），形成了预测-验证的完整链条。\n\n**S5. 实用的 practitioner guidance。** Discussion 中的具体建议（episode-level first, h≥20, 先建立正确梯度方向再用细粒度 credit）对实践者有直接价值。\n\n## 3. Weaknesses\n\n### Critical\n\n**W1. [Critical] 引用格式严重违规：10/20 引用使用 \"Anonymous\" 作为作者**\n- 具体位置：references.bib 中的 irc2026, grpolambda2025, oar2026, ragen2_2026, grpocollapse2025, gradientcoupling2025, turnppo2026, gagpo2026, mtgrpo2025, sweetrl2025\n- 问题：这些均为已公开在 arXiv 的预印本，有可查的真实作者信息。在 ACL ARR double-blind 审稿中，仅需匿名化自己的在审稿件，不应将他人已公开发表的工作标为 \"Anonymous\"。\n- 两种可能的解读都有问题：(a) 如果这些是自引——50% 自引率极不正常，且构成匿名泄露风险；(b) 如果不是自引——错误地匿名化他人工作违反学术引用规范。\n- 影响：这是 ARR desk-rejection checklist 中会被标记的格式问题。\n\n**W2. [Critical] 核心贡献的新颖性存疑**\n- 论文的 \"fix\" 是回归 GRPO 的原始设计（episode-level），论文自己也承认。\n- M1（information loss from context truncation）几乎是 trivial observation。\n- M2（sign misattribution）本质上是 sparse reward 下 credit assignment 问题的重新表述。\n- 同期大量工作已独立发现类似问题（IRC, MC-GRPO, GRPO-λ, OAR, RAGEN-2）。\n\n### Major\n\n**W3. [Major] 引用数量严重不足：仅 20 篇引用**\n- 缺失类别：RL 基础（PPO, TRPO, HER, reward shaping classics）、LLM Agent 训练/评估（WebAgent, AgentTuning, FireAct, Reflexion, AgentBench, WebShop, InterCode）、近期同方向工作（RC-GRPO, TSR）、多智能体 credit assignment（COMA, QMIX）。\n\n**W4. [Major] 8B 和 ScienceWorld 实验仅单 seed**\n- 与 W4 from R1 一致。\n\n**W5. [Major] 理论分析深度有限**\n- P(correct | update) = p/[1-(1-p)^K] 是简单条件概率公式。\n- 缺乏收敛/发散的形式化分析。\n\n### Minor\n\n**W6. [Minor] \"fundamental\" 一词过度使用（5次+），有 AI 生成文本痕迹。**\n\n**W7. [Minor] Dense reward 实验细节不足。**\n\n**W8. [Minor] Figure 1(a) 可读性问题。**\n\n## 4. Questions\n\n**Q1.** RAGEN 引入 windowing 的动机是内存约束。论文在 1.7B 上是否遇到了内存问题？episode-level 的额外计算成本？\n\n**Q2.** 11-seed 中 27% 泛化率——是否分析了哪些 seed 的初始化特征导致泛化 vs 停滞？\n\n**Q3.** Proposition 2 假设 binary reward，但实验用了 invalid action penalty (0.1)，如何影响理论预测？\n\n**Q4.** Cell B 最好成绩 5.97% OOD 后逐步收敛到 0.75%，sign misattribution 已被消除，为什么还会下降？是否暗示第三个未分析的机制？\n\n**Q5.** 是否有与 GiGPO、GAGPO、Turn-PPO 的直接实验对比？\n\n## 5. Missing References\n（同上列出的 PPO, ReAct, AgentTuning, Reflexion, WebShop, AgentBench, FireAct, RC-GRPO, TSR, COMA, QMIX 等）\n\n## 6. Overall Assessment\n**Overall**: 2.5 (Borderline Findings)\nSoundness 3.5/5, Excitement 2.5/5, Reproducibility 3.5/5, Confidence 4/5\n\n## 7. Detailed Comments\n（见上文各节详细评论）",
    "project": "cost-verify-agent-rl",
    "chat_id": "oc_648eaf83d2b24d445764257cf6a55525"
  }
}
```

</details>

---


### Tool result

_source line 139 · 2026-05-23T06:33:33.234055+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_648eaf83d2b24d445764257cf6a55525:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 34767
}
```

</details>

---


### Tool call

_source line 140 · 2026-05-23T06:33:33.936609+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "以下是 Reviewer 1 的完整审稿意见。请逐条回应：对每个 Weakness 和 Question，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。对 Strengths 和 Missing References 也请简要评论是否认同。\n\n---\n\n# Reviewer 1: 方法严谨性审查\n\n## Summary\n本文诊断了多轮 agent RL 中 step-independent windowing 的一个基本缺陷：advantage sign misattribution。论文识别了两个机制——policy information loss (M1) 和 sign misattribution (M2)——并通过 2×2 factorial 设计实验分离验证。在 ALFWorld 上，episode-level GRPO 被提出作为修复方案，并在 1.7B/8B 两个规模和 ScienceWorld 上进行了交叉验证。11-seed 评估揭示了即使修复后仍存在的 seed 依赖性。\n\n## Strengths\n\n**S1. 精准的问题诊断。** 将\"step-independent training 崩溃\"分解为两个可分离的机制（M1: ceiling, M2: divergence），结构化分析对社区有明确价值。\n\n**S2. Factorial 实验设计结构合理。** A→B 去除 M2，B→D 去除 M1，加上控制实验排除替代解释。\n\n**S3. 坦诚的 seed variability 分析。** 11-seed 评估，诚实报告 27% generalize。\n\n**S4. 多层次验证。** Credit agreement rate (52.07% ≈ random), advantage sign 与 episode outcome 高相关 (r>0.99) vs local quality 低相关 (r=0.068), γ=1.0 同样崩溃。\n\n**S5. 写作清晰。** 论文结构紧凑，narrative 清楚。\n\n## Weaknesses\n\n### Critical\n\n**C1 [critical] \"locally correct actions\" 缺乏形式定义——存在循环论证风险**\n- Proof of Proposition 1 定义 \"correct sign\" 依赖 \"locally beneficial actions\"，但 \"locally beneficial\" 未定义。\n- 80.9% incorrect sign claim 的含义完全取决于 \"correct\" 的定义。\n\n**C2 [critical] 理论分析仅限 binary reward，non-binary 扩展缺乏严格性**\n- Propositions 1-2 严格依赖 binary reward，但实验使用了 invalid action penalty (0.1)。\n- Appendix Remark 仅定性论述 \"qualitative conclusion is preserved\" 无证明。\n\n### Major\n\n**M1 [major] 2×2 Factorial 的 Cell C 缺失使 M2 无法独立验证**\n- Cell C (full observation + step-level advantage) 被论述为 \"degenerate\"，但这意味着 M2 无法在没有 M1 的条件下独立测量。\n\n**M2 [major] h-sweep cliff claim 基于 single seed，统计证据不足**\n- Figure 1(b) 是 seed 1 的单 seed 结果，从 h=10 (6.25%) 到 h=20 (15.6%) 的 \"cliff\" 无法排除 seed-specific 噪声。\n\n**M3 [major] 8B 和 ScienceWorld 的 cross-scale/cross-env claims 基于 single seed**\n- 与 11-seed 评估中 27% collapse 率对比，单 seed 可靠性存疑。Confirmatory language 与 statistical power 不匹配。\n\n**M4 [major] \"80.9% 梯度方向错误\" 的 claim 是 upper bound 而非精确值**\n- Abstract 有 qualifier \"for locally correct actions\"，但 Conclusion 省略了。\n\n**M5 [major] 15 步训练可能系统性不利于 baseline 方法**\n- REINFORCE++ 12.5% 可能只是还没开始学习。\n\n### Minor\n\n**m1 [minor]** Table 1 对不同 cell 使用了不同的报告标准。\n\n**m2 [minor]** Equation 3 的近似条件未明确。\n\n**m3 [minor]** Section 4.4 的 \"local action quality\" 度量方式未描述。\n\n**m4 [minor]** Appendix A.3 的 6 因素分析偏 editorial，Factor 3 对 RAGEN 的描述接近 blame。\n\n**m5 [minor]** RAGEN 版本/commit hash 未报告。\n\n## Questions\n\n**Q1.** \"local action quality\" 具体如何度量？\n\n**Q2.** 是否在 pure binary reward 下验证了 credit agreement rate？与 52.07% 差异多大？\n\n**Q3.** seed1 标记为 \"RAGEN built-in eval; checkpoint unavailable for re-evaluation\"——其他 seed 的 eval protocol 是否完全一致？\n\n**Q4.** 27% generalize 是否说明 sign misattribution 只是 necessary condition 之一？\n\n**Q5.** Collapse 伴随 response length inflation 是否暗示与 KL penalty 太弱有关？\n\n## Missing References\n1. Lightman et al. (2023) — Let's Verify Step by Step (PRMs)\n2. Wang et al. (2023) — Math-Shepherd\n3. Foerster et al. (2018) — COMA\n\n## Overall Assessment\n**Overall: 3.0 — Findings**\nSoundness 3/5, Excitement 3.5/5, Reproducibility 3/5, Confidence 4/5",
  "project": "cost-verify-agent-rl",
  "chat_id": "oc_648eaf83d2b24d445764257cf6a55525"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "以下是 Reviewer 1 的完整审稿意见。请逐条回应：对每个 Weakness 和 Question，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。对 Strengths 和 Missing References 也请简要评论是否认同。\n\n---\n\n# Reviewer 1: 方法严谨性审查\n\n## Summary\n本文诊断了多轮 agent RL 中 step-independent windowing 的一个基本缺陷：advantage sign misattribution。论文识别了两个机制——policy information loss (M1) 和 sign misattribution (M2)——并通过 2×2 factorial 设计实验分离验证。在 ALFWorld 上，episode-level GRPO 被提出作为修复方案，并在 1.7B/8B 两个规模和 ScienceWorld 上进行了交叉验证。11-seed 评估揭示了即使修复后仍存在的 seed 依赖性。\n\n## Strengths\n\n**S1. 精准的问题诊断。** 将\"step-independent training 崩溃\"分解为两个可分离的机制（M1: ceiling, M2: divergence），结构化分析对社区有明确价值。\n\n**S2. Factorial 实验设计结构合理。** A→B 去除 M2，B→D 去除 M1，加上控制实验排除替代解释。\n\n**S3. 坦诚的 seed variability 分析。** 11-seed 评估，诚实报告 27% generalize。\n\n**S4. 多层次验证。** Credit agreement rate (52.07% ≈ random), advantage sign 与 episode outcome 高相关 (r>0.99) vs local quality 低相关 (r=0.068), γ=1.0 同样崩溃。\n\n**S5. 写作清晰。** 论文结构紧凑，narrative 清楚。\n\n## Weaknesses\n\n### Critical\n\n**C1 [critical] \"locally correct actions\" 缺乏形式定义——存在循环论证风险**\n- Proof of Proposition 1 定义 \"correct sign\" 依赖 \"locally beneficial actions\"，但 \"locally beneficial\" 未定义。\n- 80.9% incorrect sign claim 的含义完全取决于 \"correct\" 的定义。\n\n**C2 [critical] 理论分析仅限 binary reward，non-binary 扩展缺乏严格性**\n- Propositions 1-2 严格依赖 binary reward，但实验使用了 invalid action penalty (0.1)。\n- Appendix Remark 仅定性论述 \"qualitative conclusion is preserved\" 无证明。\n\n### Major\n\n**M1 [major] 2×2 Factorial 的 Cell C 缺失使 M2 无法独立验证**\n- Cell C (full observation + step-level advantage) 被论述为 \"degenerate\"，但这意味着 M2 无法在没有 M1 的条件下独立测量。\n\n**M2 [major] h-sweep cliff claim 基于 single seed，统计证据不足**\n- Figure 1(b) 是 seed 1 的单 seed 结果，从 h=10 (6.25%) 到 h=20 (15.6%) 的 \"cliff\" 无法排除 seed-specific 噪声。\n\n**M3 [major] 8B 和 ScienceWorld 的 cross-scale/cross-env claims 基于 single seed**\n- 与 11-seed 评估中 27% collapse 率对比，单 seed 可靠性存疑。Confirmatory language 与 statistical power 不匹配。\n\n**M4 [major] \"80.9% 梯度方向错误\" 的 claim 是 upper bound 而非精确值**\n- Abstract 有 qualifier \"for locally correct actions\"，但 Conclusion 省略了。\n\n**M5 [major] 15 步训练可能系统性不利于 baseline 方法**\n- REINFORCE++ 12.5% 可能只是还没开始学习。\n\n### Minor\n\n**m1 [minor]** Table 1 对不同 cell 使用了不同的报告标准。\n\n**m2 [minor]** Equation 3 的近似条件未明确。\n\n**m3 [minor]** Section 4.4 的 \"local action quality\" 度量方式未描述。\n\n**m4 [minor]** Appendix A.3 的 6 因素分析偏 editorial，Factor 3 对 RAGEN 的描述接近 blame。\n\n**m5 [minor]** RAGEN 版本/commit hash 未报告。\n\n## Questions\n\n**Q1.** \"local action quality\" 具体如何度量？\n\n**Q2.** 是否在 pure binary reward 下验证了 credit agreement rate？与 52.07% 差异多大？\n\n**Q3.** seed1 标记为 \"RAGEN built-in eval; checkpoint unavailable for re-evaluation\"——其他 seed 的 eval protocol 是否完全一致？\n\n**Q4.** 27% generalize 是否说明 sign misattribution 只是 necessary condition 之一？\n\n**Q5.** Collapse 伴随 response length inflation 是否暗示与 KL penalty 太弱有关？\n\n## Missing References\n1. Lightman et al. (2023) — Let's Verify Step by Step (PRMs)\n2. Wang et al. (2023) — Math-Shepherd\n3. Foerster et al. (2018) — COMA\n\n## Overall Assessment\n**Overall: 3.0 — Findings**\nSoundness 3/5, Excitement 3.5/5, Reproducibility 3/5, Confidence 4/5",
    "project": "cost-verify-agent-rl",
    "chat_id": "oc_648eaf83d2b24d445764257cf6a55525"
  }
}
```

</details>

---


### Tool result

_source line 141 · 2026-05-23T06:33:35.447782+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_648eaf83d2b24d445764257cf6a55525:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1511
}
```

</details>

---


### Assistant

_source line 142 · 2026-05-23T06:33:38.749736+00:00_

交叉分享已派发，等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director"
}
```

</details>

---


## Round 10

## Round 10

2 recorded events


### User

_source line 143 · 2026-05-23T06:33:39.904660+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

总结：本文识别了 step-independent agent RL 中 sign misattribution 的重要 failure mode，实验设计整体合理。主要问题集中在三个方面：(1) 理论核心概念 "locally correct actions" 缺乏形式定义，存在循环论证风险；(2) h-sweep cliff、8B、ScienceWorld 等关键 claims 均为 single-seed，statistical power 不足；(3) 理论（binary reward）与实验（binary + invalid action penalty）的 reward structure 不一致。给出 Overall 3.0 (Findings) 评分，Soundness 3/5，Excitement 3.5/5，Confidence 4/5。

---

[Reviewer 2 审稿结果]:
审稿意见已提交给 Review Director。

总结：
- **Overall: 2.5 (Borderline Findings)**
- 两个 Critical 问题：(1) 50% 引用使用 "Anonymous" 作者，违反 ARR 引用规范；(2) 核心 "fix" 是回归 GRPO 原始设计，新颖性有限
- 两个 Major 问题：仅 20 篇引用远低于 EMNLP long paper 惯例；8B/ScienceWorld 单 seed 与论文自身的 seed 依赖性发现矛盾
- 主要优势：2×2 factorial 实验设计干净、负面结果报告诚实、跨尺度/跨环境验证增强可信度

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 144 · 2026-05-23T06:33:57.737954+00:00_

交叉分享请求已发出，等待两位 Reviewer 的 [AGREE]/[REBUT] 逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director"
}
```

</details>

---


## Round 11

## Round 11

2 recorded events


### User

_source line 145 · 2026-05-23T06:35:18.625559+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 对 Reviewer 2 审稿意见的逐条回应

---

## Strengths 回应

**[AGREE] S1（Factorial 设计）。** 与我 S2 一致，这是论文最强的方法论贡献。

**[AGREE] S2（负面结果报告）。** 与我 S3 一致。27% 泛化率的坦诚报告确实增加可信度。

**[AGREE] S3（跨尺度/跨环境验证）。** 方向正确，但我在 M3 中指出两者均为 single seed，R2 在 W4 中也同意这一问题。所以 S3 和 W4 之间存在张力——验证存在但 evidence 不充分。

**[REBUT] S4（理论预测与实验闭环）。** R2 说 "Proposition 2 预测 ~19.1% correct sign rate，实测 52% credit agreement ≈ random chance（二元环境下两者等价）"——这个 "等价" 的论述有问题。Proposition 2 预测的是 P(correct | update) = 19.1%（即在产生梯度更新的 batch 中，correct sign 的比例），而实测的 credit agreement rate 52.07% 度量的是 advantage sign 与 "local action quality" 匹配的频率。这两个量的分母不同（前者条件在 non-zero gradient，后者是所有 window）。论文没有清晰说明两者的关系，这正是我在 C1 和 m3 中指出的问题——"local action quality" 的操作化定义不明，所以无法判断理论预测与实验度量是否真正构成"闭环"。

**[AGREE] S5（Practitioner guidance）。** Discussion 中的建议确实有实践价值。

---

## Weaknesses 回应

**[AGREE] W1（Anonymous 引用格式违规）。**
我在审稿时注意到 references 中大量 "Anonymous" 条目（page 9: Anonymous 2025a-e, 2026a-c），但因其偏向格式合规而非方法严谨性，未作为主要 weakness 提出。R2 的分析完全正确：ACL ARR double-blind 要求匿名化自己的在审稿件，不应匿名化他人已公开的 arXiv 预印本。10/20 引用为 Anonymous 确实异常。补充一点：即使部分为自引，按 ARR 政策，自引应以第三人称正常引用（"X et al. (2025) proposed..."），而非匿名化，否则反而可能泄露身份（只有作者才会特意匿名化自己的工作）。这是需要在 camera-ready 前修正的合规问题。

**[REBUT] W2（核心贡献新颖性存疑）——部分反驳。**
R2 的论点有三层，我逐层回应：

(a) "Fix 是回归 GRPO 原始设计" → **AGREE**。Episode-level GRPO 确实不是新方法，论文自己也承认（Section 2.4: "This is GRPO's original design—step-independent windowing is the deviation"）。如果论文的贡献被定义为"提出了一种新方法"，那确实新颖性不足。

(b) "M1 是 trivial observation" → **AGREE**。截断上下文导致性能下降确实是直觉可预期的。但 M1 的价值在于它与 M2 的交互（Discussion: "M1 lowers p by preventing multi-step strategies, increasing wrong-sign updates under M2"），而非 M1 本身。

(c) "M2 是 credit assignment 问题的重新表述" + "同期工作已独立发现" → **REBUT**。R2 引用的同期工作（IRC, MC-GRPO, GRPO-λ, OAR, RAGEN-2）确实涉及类似问题域，但本文的特定贡献——将 failure 分解为 M1/M2 并通过 factorial 实验定量分离——在这些同期工作中据我了解并未出现。同期工作的存在说明问题重要（多组独立发现），不直接否定本文的分析框架的新颖性。当然，这些同期工作的具体内容因 Anonymous 引用而难以核实（与 W1 关联），这本身也削弱了本文 positioning 的说服力。

总体判断：我认为 R2 将新颖性评为 Critical weakness 略重。本文的主要贡献是诊断性分析而非方法创新，在 Findings 定位下这种贡献是合适的，但确实不足以支撑 main conference。这与我给出的 Overall 3.0 (Findings) 评分一致。

**[AGREE] W3（引用数量不足）。**
20 篇引用确实偏少。但我对 R2 列出的 "missing" 清单有不同的优先级判断：

- **高优先级缺失**（与论文主题直接相关）：COMA（counterfactual credit assignment, Foerster et al. 2018）、Process Reward Models（Lightman et al. 2023）、Math-Shepherd（Wang et al. 2023）——这些直接涉及 step-level vs episode-level credit assignment。我在自己的审稿中也指出了这些。
- **中优先级**：PPO（Schulman et al. 2017）、HER（Andrychowicz et al. 2017）——经典 RL 方法，应作为 background 引用。
- **低优先级**：WebAgent, AgentTuning, FireAct, Reflexion, AgentBench, WebShop——这些是 LLM agent 的训练/评估工作，与本文的 credit assignment 焦点关系间接。要求全部引用有 "H3: demanding unrelated experiments/references" 的嫌疑（参考 ARR reviewer guidelines 中的 problematic heuristics）。

**[AGREE] W4（8B/ScienceWorld 单 seed）。**
与我 M3 完全一致。不再赘述。

**[AGREE] W5（理论深度有限）——部分同意。**
P(correct | update) = p/[1-(1-p)^K] 确实是简单条件概率，这一点 R2 说得对。但我不完全同意 R2 的 framing——理论贡献的价值不仅在于公式复杂度，也在于 (a) 识别出正确的量来分析，(b) 由此衍生的定量预测。问题在于缺乏下一步：从 "80.9% wrong sign" 到 "training will diverge" 的形式化连接缺失。论文在 Appendix A.1 定性论述了 sign error 比 magnitude error 更有害，但没有收敛/发散的 formal bound。如果补充一个简化设定下的发散证明（例如 showing expected gradient points away from optimal policy under the computed sign error rate），理论贡献将显著增强。

**[AGREE] W6（"fundamental" 过度使用）。** 风格问题，minor。我注意到 Section 3 第一句、Appendix A.1、Abstract 等多处使用。减少到 1-2 处即可。至于 "AI 生成痕迹"——这是主观判断，不应作为 review concern（ARR guidelines 未禁止使用写作辅助工具）。

**[AGREE] W7（Dense reward 细节不足）。** Appendix C 仅用两句话描述 dense reward 设置（"+0.15 per valid action"），格式信息不足以复现。应报告 dense reward 的 value function 形式、给分规则的完整定义、以及是否叠加 binary episode reward。

**[AGREE] W8（Figure 1a 可读性）。** 同意。四条线在小尺寸图中区分度有限，建议区分 line style 或分成 sub-panels。

---

## Questions 回应

**[AGREE] Q1（Episode-level 的内存/计算开销）。**
重要的实践问题。论文在 Appendix A.3 Factor 4 提到 "O(T) vs O(h) memory"，但没有报告实际 GPU 内存使用或训练时间对比。作为 "practitioner guidance" 的论文，应至少报告 episode-level 在 1.7B 上是否 fit 单 GPU、batch size 受限多少。

**[AGREE] Q2（Seed 初始化特征分析）。**
论文在 Discussion 中承认这是 open question，但完全没有尝试分析（如比较 generalized vs stagnant seeds 的 early training gradient norm、loss landscape 等）。这限制了 seed variability 结果的 actionability。

**[AGREE] Q3（Binary vs non-binary reward gap）。**
与我 C2 一致。核心矛盾：理论假设 binary，实验用了 invalid action penalty (0.1)，需要作者解释或修正。

**[REBUT] Q4（Cell B 的 OOD 下降是否暗示第三机制）。**
R2 提出了一个有趣的观察，但我不认为需要第三机制来解释。Cell B 中 M1 仍然存在（h=2 truncation），模型只能看到局部 2 步 context。在这种极度受限的 observation 下，模型最可能的学习路径是 memorize in-distribution 的局部 pattern（training success 达 55%），但这些 pattern 无法迁移到 OOD（不同任务类型有不同的局部 pattern）。OOD 从 5.97% 下降到 0.75% 可解释为 overfitting to in-distribution local patterns——这正是 M1 的预期后果，不需要第三机制。

支撑证据：(a) Cell B 的 in-distribution 成绩持续上升（55%），同时 OOD 下降，符合 overfitting 的特征；(b) Section 4.2 说两个 seed "converge to the same OOD ceiling (0.75% at step 15)"，ceiling 的一致性说明这是结构性限制（M1）而非随机波动。

**[AGREE] Q5（与 GiGPO/GAGPO/Turn-PPO 的对比）。**
论文在 Discussion 中提到这些方法并建议 "先建立 episode-level baseline 再用细粒度 credit"，但没有直接实验对比。至少应与 Turn-PPO（也处理 multi-turn credit assignment）对比，否则 "episode-level is better" 的 claim 缺乏竞争性 baseline。

---

## Missing References 回应

R2 列出的缺失引用可分三类：

**直接相关（应补充）：** COMA、Process Reward Models、PPO（我在自己的审稿中也指出了前两个）。

**间接相关（可选补充）：** TRPO, HER, QMIX——RL 基础方法，作为 background 引用合理但不 critical。

**关系较远（不必全部引用）：** WebAgent, AgentTuning, FireAct, Reflexion, AgentBench, WebShop, InterCode——这些是 LLM agent 系统/benchmark 工作，与本文的 credit assignment 机制分析焦点不同。全部要求引用有过度扩大 scope 的嫌疑。RC-GRPO 和 TSR 如果确实涉及类似问题则应引用，但 R2 未提供足够信息判断。

---

## Overall Assessment 回应

R2 给出 2.5 (Borderline Findings)，我给出 3.0 (Findings)。差异主要来自两点：

1. **新颖性权重**：R2 将 "fix 不新" 和 "同期工作多" 作为 critical weakness。我认为诊断性分析本身（M1/M2 分离 + factorial 验证）是 contribution，即使 fix 不新颖。Findings 接收标准侧重 soundness 和 reproducibility，不要求方法新颖性。

2. **引用格式问题的严重性**：R2 将 Anonymous 引用列为 critical。我同意这是必须修正的合规问题，但在技术内容评估中它不应影响 soundness 或 excitement 评分——这是可在 revision 中修正的格式问题。

综合 R2 的意见后，我维持 **Overall 3.0 (Findings)** 的评分。W1（引用格式）是严重的合规问题但可修复；W2（新颖性）在 Findings 定位下可接受；W3-W5 与我自己的 concerns 一致但不足以降到 2.5。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 146 · 2026-05-23T06:35:28.371819+00:00_

Reviewer 1 的交叉回应已收到，等待 Reviewer 2 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director"
}
```

</details>

---


## Round 12

## Round 12

2 recorded events


### User

_source line 147 · 2026-05-23T06:35:32.866896+00:00_

[Reviewer 1 审稿结果]:
已提交对 R2 的逐条回应。关键判断：

- **W1（Anonymous 引用）**：[AGREE]，合规问题，需修正
- **W2（新颖性）**：部分 [REBUT]——诊断框架（M1/M2 分离 + factorial）有独立价值，但 fix 确实不新
- **W3（引用不足）**：[AGREE]，但优先级排序与 R2 不同（COMA/PRM 高优先，agent benchmark 低优先）
- **W4/W5**：[AGREE]，与我自己的 review 一致
- **Q4（Cell B 下降=第三机制？）**：[REBUT]——M1 下的 overfitting 足以解释

维持 Overall 3.0 (Findings)，认为 R2 的 2.5 略偏低。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 148 · 2026-05-23T06:35:37.137069+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director"
}
```

</details>

---


## Round 13

## Round 13

10 recorded events


### User

_source line 149 · 2026-05-23T06:36:25.108844+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 对 Reviewer 1 审稿意见的交叉回应

---

## Strengths 回应

**S1 (精准的问题诊断)**: [AGREE] 认同。M1(ceiling) vs M2(divergence) 的分离是论文最有价值的概念贡献，我在自己的审稿中也列为 S1。

**S2 (Factorial 设计)**: [AGREE] 认同。但需注意 R1 自己在 M1 中指出 Cell C 缺失——这实际上削弱了 factorial 的完备性。

**S3 (Seed variability 分析)**: [AGREE] 强烈认同。这是本文区别于同期工作的主要优势之一。

**S4 (多层次验证)**: [AGREE] 认同。52.07% credit agreement 是扎实的实证贡献。

**S5 (写作清晰)**: [AGREE] 部分认同。整体结构清晰，但我在自己的审稿中指出 "fundamental" 过度使用（5+ 次）以及部分 AI 生成文本痕迹。

---

## Weaknesses 回应

### Critical

**[AGREE] R1-C1: "locally correct actions" 缺乏形式定义**
同意这是理论部分的核心缺陷。Proposition 1 的 proof sketch 依赖 "locally beneficial actions" 概念，但全文没有给出形式定义。这个问题在两个层面上有影响：
1. **理论层面**：80.9% 这个数字的含义完全取决于 "correct" 的定义——如果定义过于宽泛（比如任何在某个 oracle 评估下是正确格式的 action），数字可能不同。
2. **实证层面**：Section 4.4 的 credit agreement rate 测量（52.07%）同样依赖对 "local action quality" 的操作化定义，但 Section 4.4 没有描述这个度量的具体计算方式（R1 的 m3 和 Q1 也指出了这一点）。

不过我认为这不构成**循环论证**。论文的核心论点——"advantage sign 由 episode outcome 决定而非 local quality"——不依赖 "local quality" 的精确定义。无论如何定义 local quality，只要它不完全等于 episode outcome，sign misattribution 就存在。Section 4.4 的 r > 0.99（advantage sign vs episode outcome）vs r = 0.068（vs local quality）的对比在定性层面是稳健的。所以我同意**形式定义缺失是问题**，但不同意**循环论证**的判断。

**[AGREE] R1-C2: Binary reward 假设与实验不匹配**
完全同意。这与我自己的 Q3 一致。实验中使用了 invalid action penalty = 0.1（Appendix B, Table 4），因此 reward 不是严格 binary 的。Appendix A.2 的 Remark 仅声称 "qualitative conclusion is preserved"，没有给出非 binary 情况下的定量分析。这造成了理论（binary 假设）和实验（non-binary 实际）之间的 gap。

补充一点 R1 未提及的：Proposition 2 推导的 P(correct|update) = 19.1%，但实测 credit agreement rate 是 52.07%。这两个数字之间的巨大差异（19.1% vs 52.07%）可能正是 non-binary reward 导致的偏差，但论文没有讨论这一 discrepancy。

### Major

**[AGREE] R1-M1: Cell C 缺失**
同意这是 factorial 设计的一个实质性缺陷。论文声称 Cell C "degenerate"（Section 2.5: "full observation with one window makes step- and episode-level advantage identical"），但这个论证混淆了**实现方式**和**概念区分**：
- 论文的实现中，"full observation" = 一个覆盖全 trajectory 的 window → 只有一个 advantage → step/episode 等价
- 但概念上，完全可以实现：每个 step 看到完整 history（消除 M1），但 advantage 仍然 per-window 计算（保留 M2）

如果 Cell C 存在且表现类似 Cell A（崩溃），就能独立证明 M2 是 sufficient for collapse；如果表现类似 Cell D（成功），则说明 M1 是关键而非 M2。缺少 Cell C 使得论文无法区分 "M2 alone causes collapse" 和 "M2 only causes collapse when combined with M1"。

**[AGREE] R1-M2: h-sweep cliff 单 seed**
同意。我在自己的审稿 W4 中也指出了类似问题。Figure 1(b) 的 cliff（h=10: 6.25% → h=20: 15.6%）基于 seed 1。鉴于论文在 Section 4.5 自己展示了极大的 seed 方差（同一条件下从 10.45% 到 30.60%），单 seed 的 h-sweep 无法支持 "cliff" 这样的强 claim。Table 1 提到 "seed 1; cf. Table 1 for two-seed mean"，但 caption 说 h-sweep 只有 seed 1 的数据。

**[AGREE] R1-M3: 8B/ScienceWorld 单 seed**
完全同意，与我的 W4 一致。不再赘述。

**[REBUT] R1-M4: "80.9%" 是 upper bound 而非精确值**
部分不同意。80.9% = 1 - P(correct|update) = 1 - p/[1-(1-p)^K] 在 binary reward 模型下是**精确值**（在给定 p=12.5%, K=8 的条件下），不是 upper bound。它不是 "worst case" 或 "at most"——它是条件概率的精确计算。

但 R1 指出的**另一个问题**是成立的：Conclusion (Section 7) 写 "~80.9% of gradient updates carry incorrect sign"，省略了 Abstract 中的 qualifier "for locally correct actions"。这确实是 overclaim——80.9% 是对 "locally correct windows" 子集的条件概率，不是所有 gradient updates 的总体概率。这个遗漏应当修正。

**[AGREE] R1-M5: 15 步训练可能不利于 baseline**
部分同意。15 个 training steps（每步 16 tasks × 8 rollouts = 128 trajectories per step）总共只有约 1920 个 trajectories，对于 RL 训练确实偏少。特别是：
- REINFORCE++ 停留在 SFT baseline (12.5%) 可能是因为训练不足而非方法本身无效
- 论文未报告 REINFORCE++ 的 loss curve 或 gradient norm 来排除"还没开始学习"的可能

但对于 Cell A（step-independent GRPO），这个 concern 较弱——因为 Cell A 是**主动崩溃**（从 12.5% → 0%），不是"还没学会"，而是"越学越差"。15 步足够展示崩溃模式。对 Cell D（episode-level）, 11-seed 评估中 seed5 在 step 10 达到 25.37%，seed4 在 step 15 达到 30.60%，说明学习在发生。所以训练步数的 concern 主要针对 REINFORCE++ 和其他替代方法，不影响核心的 A vs D 比较。

### Minor

**[AGREE] R1-m1 (Table 1 报告标准不一致)**: 同意。我在自己的 Detailed Comments Section 4 中也指出了这一点——Cell A 报告 best seed, Cell B 报告 best checkpoint (step 5), Cell D 报告 mean。应统一为 mean ± std 或至少报告所有 seeds。

**[AGREE] R1-m2 (Eq. 3 近似条件)**: 同意。sign(Â_k) ≈ sign(R_episode - μ) 是直觉近似，缺乏误差界或成立条件。

**[AGREE] R1-m3 (local action quality 度量未描述)**: 同意，与 R1-C1 和 Q1 关联。Section 4.4 的 credit agreement rate 度量缺乏可复现的操作定义。

**[REBUT] R1-m4 (Appendix A.3 偏 editorial / blame RAGEN)**: 部分不同意。A.3 的 6 因素分析（为什么 step-independent 成为默认）是有价值的贡献，因为它解释了一个 paradox：为什么社区长期使用有缺陷的方法。Factor 3 提到 "RAGEN framework implements step-independent mode as its default configuration, not as one option among alternatives" 是事实陈述，不是 blame。不过措辞可以更中性——改为 "inherited default configuration" 比暗示 "design accident" 更好。

**[AGREE] R1-m5 (RAGEN 版本未报告)**: 同意。可复现性需要框架版本/commit hash。

---

## Questions 回应

**Q1 (local action quality 度量)**: 同意这是需要作者回答的关键问题。如果 "local quality" 是用 oracle 判断（如 admissible action set），则度量有意义但引入了 oracle 假设；如果是用某种 proxy，则需要讨论 proxy 的准确性。

**Q2 (pure binary reward 下的 credit agreement)**: 好问题。理论预测是基于 binary reward 的 ~19.1%，实测是 52.07%（包含 invalid action penalty）。如果在 pure binary reward 下测量，数字可能更接近理论预测。这个实验缺失削弱了理论-实验闭环。

**Q3 (seed1 的 eval protocol 差异)**: 重要的 reproducibility concern。Table 2 脚注标注 seed1 使用 "RAGEN built-in eval; checkpoint unavailable for re-evaluation"，这意味着 seed1 (23.88% OOD) 可能与其他 seeds 的评估不完全可比。鉴于 seed1 是 generalized 组中表现最低的，影响可能有限，但仍应标注清楚。

**Q4 (27% generalize 是否说明 sign misattribution 只是 necessary condition)**: 同意这是论文的核心 tension。论文将 episode-level fix 定义为 "necessary but not sufficient"（Contribution 3），逻辑上是一致的。但这也意味着论文诊断的问题（sign misattribution）只解释了崩溃现象的一部分——修复 sign misattribution 后仍有 73% 无法 generalize，说明还有其他更根本的因素在起作用。论文对此没有深入分析。

**Q5 (Collapse + response length inflation vs KL penalty)**: 有意思的观察。Figure 2(b) 显示崩溃的 seed 伴随 response length 膨胀到 14,000-16,000 tokens。KL penalty β=0.01 可能确实太弱——如果增大 β，是否能减少 collapse 率（从 27% 降低）？论文没有做 β sweep，这本可以部分回答 seed 依赖性的问题。不过，这更像是一个未来工作方向，而非对当前论文的致命批评。

---

## Missing References 回应

**Lightman et al., 2023 — Let's Verify Step by Step (PRMs)**: [AGREE] 应引用。PRM 是 step-level credit assignment 的重要相关工作，虽然在 math reasoning 而非 agent 领域，但与论文的 credit assignment 主题直接相关。

**Wang et al., 2023 — Math-Shepherd**: [AGREE] 应引用。与 PRM 类似，提供了 step-level verification 的方法论。

**Foerster et al., 2018 — COMA**: [AGREE] 应引用。我在自己的审稿中也独立指出了这个缺失。论文 Appendix A.4 明确画了多智能体 credit assignment 的类比，但没有引用 COMA/QMIX 等经典方法，是明显疏漏。

补充：我认为还应引用 **PPO (Schulman et al., 2017)**（论文多处提到 PPO 但未引用原始文献）、**ReAct (Yao et al., 2023)**（agent 推理范式基础工作）、以及多个 agent training/benchmark 工作（AgentTuning, Reflexion, WebShop, AgentBench）。详见我的审稿意见 Section 5。

---

## Overall Assessment 回应

R1 给出 **3.0 (Findings)**，Soundness 3/5, Excitement 3.5/5。

我给出 **2.5 (Borderline Findings)**，Soundness 3.5/5, Excitement 2.5/5。

**共识点**：
- 实验方法论（factorial design）有价值
- 理论深度有限（binary reward 假设、"locally correct" 未定义）
- 8B/ScienceWorld 单 seed 削弱 generality claims
- 引用不足

**分歧点**：
- **Excitement**：R1 给 3.5, 我给 2.5。我更担心新颖性问题——核心 "fix" 是回归 GRPO 原始设计，且同期 5+ 个独立工作收敛到类似诊断（IRC, MC-GRPO, GRPO-λ, OAR, RAGEN-2）。R1 没有深入讨论这些同期工作对新颖性的影响。
- **Soundness**：R1 给 3, 我给 3.5。我认为 factorial design 在方法论上是扎实的，Cell C 缺失是缺陷但不致命（A→B 和 B→D 的对比仍然 informative）。
- **引用格式**：R1 未提到 10/20 引用使用 "Anonymous" 的问题。这是我认为的一个 critical 格式违规，50% 引用缺少真实作者信息（这些 arXiv 预印本有公开作者）。这个问题可能触发 ARR desk-rejection checklist 的格式检查。

**综合判断**：结合两份审稿意见，我认为论文整体在 **2.5-3.0** 区间（Borderline Findings 到 Findings）。诊断框架有价值但增量贡献有限，关键实验缺乏统计 power（单 seed），理论偏浅。如果作者能解决引用格式、补充 Cell C 实验、增加 8B 多 seed、并明确 "locally correct" 的定义，论文可以达到 solid Findings 水平。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 150 · 2026-05-23T06:36:51.852581+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "cost-verify-agent-rl"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "cost-verify-agent-rl"
  }
}
```

</details>

---


### Tool call

_source line 151 · 2026-05-23T06:36:51.853561+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "cost-verify-agent-rl"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "cost-verify-agent-rl"
  }
}
```

</details>

---


### Tool result

_source line 152 · 2026-05-23T06:36:51.904113+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-23T06:24:49.994311+00:00\", \"completed_at\": \"2026-05-23T06:27:45.796613+00:00\", \"findings\": [{\"severity\": \"warning\", \"dimension\": \"page 1-3\", \"message\": \"前 3 页无任何 display item（figure/table），审稿人前 4 页只见纯文本+数学推导，缺乏视觉锚点建立第一印象。建议将 Figure 1 或一个概念图/架构图提前到 page 1-2\"}, {\"severity\": \"warning\", \"dimension\": \"page 5\", \"message\": \"单页承载 1 figure + 2 tables，视觉密度过高，与前 3 页纯文本形成强烈反差。考虑将 Table 2 或 Table 3 移至 page 4 以平衡节奏\"}, {\"severity\": \"critical\", \"dimension\": \"page 12\", \"message\": \"仅 ~10 行文字后整页空白（>80%），LaTeX float 排版问题——Figure 4 被推到 page 13 留下空页。应调整 float placement 或合并内容消除空页\"}, {\"severity\": \"warning\", \"dimension\": \"page 13\", \"message\": \"Figure 4 位于页面下半部分，上方约 40% 为空白。与 page 12 的空白合计，附录末尾 2 页空间利用率极低\"}, {\"severity\": \"info\", \"dimension\": \"page 5\", \"message\": \"Figure 1 的 legend 字号偏小（约正文 60%），多条目密集排列在底部，建议适当增大或简化 legend\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Figure 3(a) 中部分 bar 上的数值标注（\\\"0%\\\"、\\\"1.5\\\"）字号较小，打印阅读可能吃力\"}, {\"severity\": \"info\", \"dimension\": \"page 4\", \"message\": \"论文第一个 display item（Table 1）出现在 page 4，对于实证为主的论文偏晚。一个概念图/方法 overview 放在 page 2 能显著改善审稿人第一印象\"}], \"counts\": {\"critical\": 1, \"warning\": 3, \"info\": 3}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 51
}
```

</details>

---


### Tool result

_source line 153 · 2026-05-23T06:36:51.904471+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 154 · 2026-05-23T06:38:43.312852+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "cost-verify-agent-rl",
  "issues_yaml": "# Review Issues Tracker — cost-verify-agent-rl\n# Updated: Round 1 (2026-05-23)\n\n# === Recurring from Round 0 (Dream Review) ===\n\n- id: \"DR1-C1\"\n  summary: \"Theory framework must match actual GRPO implementation (not algorithm-level abstraction)\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 0\n  last_seen_round: 1\n  mentions:\n    - {round: 0, reviewers: [R1, R2], note: \"Dream review — both reviewers agree theory contribution collapses if Eq.1 is analogy not derivation\"}\n    - {round: 1, reviewers: [R1, R2], note: \"Evolved into R1-C2: theory assumes binary reward but experiments use invalid action penalty 0.1. Proposition 2 predicts 19.1% but measured 52.07% — gap unexplained.\"}\n  action_items:\n    - {round: 0, action: \"Reframe theory as dual mechanism: policy information loss + gradient signal dilution.\", assigned_to: director, status: done}\n    - {round: 0, action: \"D058 second correction: source audit found RAGEN step_independent DOES use γ.\", assigned_to: director, status: done}\n    - {round: 1, action: \"Either re-run credit agreement rate under pure binary reward, or extend Proposition 2 to cover invalid action penalty.\", assigned_to: agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"DR1-C2\"\n  summary: \"Core novelty insufficient — episode-level RL is REINFORCE default\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 0\n  last_seen_round: 1\n  mentions:\n    - {round: 0, reviewers: [R1, R2], note: \"Dream review — contribution reduces to 'discovered RAGEN has bug-like behavior and used standard method to fix'\"}\n    - {round: 1, reviewers: [R2], note: \"R2-W2 critical: fix is returning to GRPO original design. 5+ concurrent works (IRC, MC-GRPO, GRPO-λ, OAR, RAGEN-2) converge to similar diagnosis. R1 partially rebuts: M1/M2 factorial separation has independent value.\"}\n  action_items:\n    - {round: 0, action: \"Reposition: 'diagnose LLM agent community default step-independent + dual mechanism analysis'\", assigned_to: director, status: done}\n    - {round: 1, action: \"Strengthen differentiation from concurrent works — clearly articulate what M1/M2 factorial separation adds beyond individual diagnoses from IRC/GRPO-λ/OAR/etc.\", assigned_to: paper_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"DR1-C3\"\n  summary: \"Statistical power insufficient — single seed on key claims\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 0\n  last_seen_round: 1\n  mentions:\n    - {round: 0, reviewers: [R1, R2], note: \"Dream review — 95% CI too wide, cliff may be artifact\"}\n    - {round: 1, reviewers: [R1, R2], note: \"1.7B upgraded to 11 seeds [IMPROVED]. But h-sweep cliff (R1-M2), 8B (R1-M3/R2-W4), ScienceWorld still single seed. Both reviewers AGREE this weakens generality claims.\"}\n  action_items:\n    - {round: 0, action: \"plan_003 upgraded to 5 seeds (from 3); plan_002 h-sweep to 3 seeds per h\", assigned_to: director, status: done}\n    - {round: 1, action: \"Add 2-3 seeds for h=5,10,20 sweep. Add at least 1 more 8B seed. Downgrade cross-env language to 'preliminary evidence'.\", assigned_to: agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"DR1-C4\"\n  summary: \"Missing standard RL baselines (GAE, reward shaping)\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 0\n  last_seen_round: 1\n  mentions:\n    - {round: 0, reviewers: [R1, R2], note: \"Dream review — cannot judge if episode-level is unique solution\"}\n    - {round: 1, reviewers: [R1, R2], note: \"REINFORCE++ added but result ambiguous (12.5%, may need more steps — R1-M5). Dense reward and γ sweep added. Still missing direct comparison with Turn-PPO/GAGPO (R2-Q5). R1-M5 flags 15 training steps may be unfair to baselines.\"}\n  action_items:\n    - {round: 0, action: \"plan_003b added: GAE + baselines\", assigned_to: director, status: done}\n    - {round: 1, action: \"Run REINFORCE++ for more steps (30+) to confirm it genuinely doesn't improve. Consider adding Turn-PPO or GAGPO comparison.\", assigned_to: agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"DR1-C5\"\n  summary: \"Related work severely insufficient\"\n  category: writing\n  severity: critical\n  status: in_progress\n  first_raised_round: 0\n  last_seen_round: 1\n  mentions:\n    - {round: 0, reviewers: [R1, R2], note: \"Dream review — 10 citations, need 30+\"}\n    - {round: 1, reviewers: [R1, R2], note: \"Improved to 20 citations but still insufficient for EMNLP long paper (expect 40-60). Missing: PPO, COMA, PRM, Math-Shepherd, ReAct, AgentTuning, Reflexion, etc. R2-W3 major.\"}\n  action_items:\n    - {round: 0, action: \"Expand references to 30-40\", assigned_to: paper_agent, status: open}\n    - {round: 1, action: \"Priority additions: PPO (Schulman 2017), COMA (Foerster 2018), PRM (Lightman 2023), Math-Shepherd (Wang 2023), ReAct (Yao 2023). Also fix Anonymous citations (see R1-W1-new).\", assigned_to: paper_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"DR1-C6\"\n  summary: \"3x performance gap with Self-Guide (24% vs 72.7%) unexplained\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 0\n  last_seen_round: 1\n  mentions:\n    - {round: 0, reviewers: [R1, R2], note: \"Dream review — same model, same env, 3x gap\"}\n    - {round: 1, reviewers: [], note: \"Round 1 reviewers did not raise this issue. Paper now reports 30.60% best seed OOD, gap reduced but still significant vs Self-Guide's 72.7%.\"}\n  action_items:\n    - {round: 0, action: \"Position as different paradigm\", assigned_to: director, status: done}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"DR1-W1\"\n  summary: \"Overclaiming: 'eliminates this bottleneck' with only 25% success\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 0\n  last_seen_round: 1\n  mentions:\n    - {round: 0, reviewers: [R1, R2], note: \"Dream review\"}\n    - {round: 1, reviewers: [R1], note: \"R1-M4: Conclusion drops 'for locally correct actions' qualifier for 80.9% claim. Abstract has qualifier but Conclusion omits it. R2 confirms: overclaim via omission.\"}\n  action_items:\n    - {round: 0, action: \"Change to 'significantly alleviates' or 'enables non-zero learning'\", assigned_to: paper_agent, status: open}\n    - {round: 1, action: \"Unify '80.9%' claim wording — always include 'for windows with locally correct actions' qualifier.\", assigned_to: paper_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"DR1-W4\"\n  summary: \"h-sweep cliff claim unreliable (single seed)\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 0\n  last_seen_round: 1\n  mentions:\n    - {round: 0, reviewers: [R1, R2], note: \"Dream review — needs multi-seed\"}\n    - {round: 1, reviewers: [R1, R2], note: \"R1-M2 major, R2 AGREE. Still single seed (seed 1). Both reviewers agree cliff claim not supported.\"}\n  action_items:\n    - {round: 0, action: \"Covered by plan_002 upgrade (3 seeds per h value)\", assigned_to: director, status: done}\n    - {round: 1, action: \"Run h=5,10,20 with 2-3 seeds each. Report mean and range.\", assigned_to: agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n# === New issues from Round 1 ===\n\n- id: \"R1-C1\"\n  summary: \"'Locally correct actions' lacks formal definition — circular reasoning risk\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 1, reviewers: [R1, R2], note: \"R1 critical, R2 AGREE on definition gap but REBUT on circular reasoning — argues core argument (sign determined by episode outcome) is robust regardless of local quality definition. Consensus: formal definition needed, but not circular.\"}\n  action_items:\n    - {round: 1, action: \"Add operational definition of 'locally correct' (e.g., expert action match or oracle-based). Describe Section 4.4 credit agreement rate computation explicitly.\", assigned_to: paper_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-C2\"\n  summary: \"Theory (binary reward) vs experiment (binary + invalid action penalty) gap\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 1, reviewers: [R1, R2], note: \"Both AGREE. Proposition 2 predicts 19.1% correct sign, measured 52.07% — discrepancy likely from non-binary reward but undiscussed. R2 adds: this discrepancy undermines theory-experiment 'closed loop' claim.\"}\n  action_items:\n    - {round: 1, action: \"Option A: Re-run credit agreement rate under pure binary reward (no invalid action penalty). Option B: Extend Proposition 2 to include per-step penalties. Option C: At minimum, discuss the 19.1% vs 52.07% discrepancy.\", assigned_to: agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W1\"\n  summary: \"10/20 citations use 'Anonymous' author — ARR format violation\"\n  category: format\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 1, reviewers: [R1, R2], note: \"R2 critical, R1 AGREE. arXiv preprints with public author lists should not be anonymized. Potential desk-rejection risk. If self-citations, should use third-person per ARR policy.\"}\n  action_items:\n    - {round: 1, action: \"Replace all 'Anonymous' in references.bib with actual arXiv authors for non-self works. For self-citations, use third-person normal citation.\", assigned_to: paper_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-M1\"\n  summary: \"Cell C missing from 2x2 factorial — M2 cannot be independently verified\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 1, reviewers: [R1, R2], note: \"R1 major, R2 AGREE. Paper claims Cell C is 'degenerate' but R2 points out conceptually possible implementation (full history per step, advantage per window). Acknowledging as limitation rather than degeneracy.\"}\n  action_items:\n    - {round: 1, action: \"Either implement Cell C (full obs + per-window advantage) or reframe as acknowledged limitation in Discussion.\", assigned_to: paper_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-M5\"\n  summary: \"15 training steps may be unfair to baseline methods\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 1, reviewers: [R1, R2], note: \"R1 major, R2 partial AGREE. REINFORCE++ at 12.5% (=SFT) may just need more training. R2 notes concern is weaker for Cell A (active collapse) but valid for REINFORCE++.\"}\n  action_items:\n    - {round: 1, action: \"Run REINFORCE++ for 30+ steps. Report loss curve and gradient norms to confirm whether it has converged or is still learning.\", assigned_to: agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-m1\"\n  summary: \"Table 1 uses inconsistent reporting standards across cells\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 1, reviewers: [R1, R2], note: \"Both AGREE. Cell A: best seed, Cell B: best checkpoint, Cell D: mean. Should unify to mean ± std.\"}\n  action_items:\n    - {round: 1, action: \"Unify Table 1 reporting to mean (range) or mean ± std for all conditions.\", assigned_to: paper_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-m5\"\n  summary: \"RAGEN framework version/commit hash not reported\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 1, reviewers: [R1, R2], note: \"Both AGREE. Core claim is about RAGEN's default config — reproducibility requires exact version.\"}\n  action_items:\n    - {round: 1, action: \"Add RAGEN version/commit hash to Appendix B.\", assigned_to: paper_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W6\"\n  summary: \"'fundamental' overused (5+ times), minor writing polish needed\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 1, reviewers: [R2], note: \"R1 AGREE as style issue. Reduce to 1-2 uses.\"}\n  action_items:\n    - {round: 1, action: \"Replace most 'fundamental' with 'structural' or 'systematic'.\", assigned_to: paper_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "cost-verify-agent-rl",
    "issues_yaml": "# Review Issues Tracker — cost-verify-agent-rl\n# Updated: Round 1 (2026-05-23)\n\n# === Recurring from Round 0 (Dream Review) ===\n\n- id: \"DR1-C1\"\n  summary: \"Theory framework must match actual GRPO implementation (not algorithm-level abstraction)\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 0\n  last_seen_round: 1\n  mentions:\n    - {round: 0, reviewers: [R1, R2], note: \"Dream review — both reviewers agree theory contribution collapses if Eq.1 is analogy not derivation\"}\n    - {round: 1, reviewers: [R1, R2], note: \"Evolved into R1-C2: theory assumes binary reward but experiments use invalid action penalty 0.1. Proposition 2 predicts 19.1% but measured 52.07% — gap unexplained.\"}\n  action_items:\n    - {round: 0, action: \"Reframe theory as dual mechanism: policy information loss + gradient signal dilution.\", assigned_to: director, status: done}\n    - {round: 0, action: \"D058 second correction: source audit found RAGEN step_independent DOES use γ.\", assigned_to: director, status: done}\n    - {round: 1, action: \"Either re-run credit agreement rate under pure binary reward, or extend Proposition 2 to cover invalid action penalty.\", assigned_to: agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"DR1-C2\"\n  summary: \"Core novelty insufficient — episode-level RL is REINFORCE default\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 0\n  last_seen_round: 1\n  mentions:\n    - {round: 0, reviewers: [R1, R2], note: \"Dream review — contribution reduces to 'discovered RAGEN has bug-like behavior and used standard method to fix'\"}\n    - {round: 1, reviewers: [R2], note: \"R2-W2 critical: fix is returning to GRPO original design. 5+ concurrent works (IRC, MC-GRPO, GRPO-λ, OAR, RAGEN-2) converge to similar diagnosis. R1 partially rebuts: M1/M2 factorial separation has independent value.\"}\n  action_items:\n    - {round: 0, action: \"Reposition: 'diagnose LLM agent community default step-independent + dual mechanism analysis'\", assigned_to: director, status: done}\n    - {round: 1, action: \"Strengthen differentiation from concurrent works — clearly articulate what M1/M2 factorial separation adds beyond individual diagnoses from IRC/GRPO-λ/OAR/etc.\", assigned_to: paper_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"DR1-C3\"\n  summary: \"Statistical power insufficient — single seed on key claims\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 0\n  last_seen_round: 1\n  mentions:\n    - {round: 0, reviewers: [R1, R2], note: \"Dream review — 95% CI too wide, cliff may be artifact\"}\n    - {round: 1, reviewers: [R1, R2], note: \"1.7B upgraded to 11 seeds [IMPROVED]. But h-sweep cliff (R1-M2), 8B (R1-M3/R2-W4), ScienceWorld still single seed. Both reviewers AGREE this weakens generality claims.\"}\n  action_items:\n    - {round: 0, action: \"plan_003 upgraded to 5 seeds (from 3); plan_002 h-sweep to 3 seeds per h\", assigned_to: director, status: done}\n    - {round: 1, action: \"Add 2-3 seeds for h=5,10,20 sweep. Add at least 1 more 8B seed. Downgrade cross-env language to 'preliminary evidence'.\", assigned_to: agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"DR1-C4\"\n  summary: \"Missing standard RL baselines (GAE, reward shaping)\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 0\n  last_seen_round: 1\n  mentions:\n    - {round: 0, reviewers: [R1, R2], note: \"Dream review — cannot judge if episode-level is unique solution\"}\n    - {round: 1, reviewers: [R1, R2], note: \"REINFORCE++ added but result ambiguous (12.5%, may need more steps — R1-M5). Dense reward and γ sweep added. Still missing direct comparison with Turn-PPO/GAGPO (R2-Q5). R1-M5 flags 15 training steps may be unfair to baselines.\"}\n  action_items:\n    - {round: 0, action: \"plan_003b added: GAE + baselines\", assigned_to: director, status: done}\n    - {round: 1, action: \"Run REINFORCE++ for more steps (30+) to confirm it genuinely doesn't improve. Consider adding Turn-PPO or GAGPO comparison.\", assigned_to: agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"DR1-C5\"\n  summary: \"Related work severely insufficient\"\n  category: writing\n  severity: critical\n  status: in_progress\n  first_raised_round: 0\n  last_seen_round: 1\n  mentions:\n    - {round: 0, reviewers: [R1, R2], note: \"Dream review — 10 citations, need 30+\"}\n    - {round: 1, reviewers: [R1, R2], note: \"Improved to 20 citations but still insufficient for EMNLP long paper (expect 40-60). Missing: PPO, COMA, PRM, Math-Shepherd, ReAct, AgentTuning, Reflexion, etc. R2-W3 major.\"}\n  action_items:\n    - {round: 0, action: \"Expand references to 30-40\", assigned_to: paper_agent, status: open}\n    - {round: 1, action: \"Priority additions: PPO (Schulman 2017), COMA (Foerster 2018), PRM (Lightman 2023), Math-Shepherd (Wang 2023), ReAct (Yao 2023). Also fix Anonymous citations (see R1-W1-new).\", assigned_to: paper_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"DR1-C6\"\n  summary: \"3x performance gap with Self-Guide (24% vs 72.7%) unexplained\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 0\n  last_seen_round: 1\n  mentions:\n    - {round: 0, reviewers: [R1, R2], note: \"Dream review — same model, same env, 3x gap\"}\n    - {round: 1, reviewers: [], note: \"Round 1 reviewers did not raise this issue. Paper now reports 30.60% best seed OOD, gap reduced but still significant vs Self-Guide's 72.7%.\"}\n  action_items:\n    - {round: 0, action: \"Position as different paradigm\", assigned_to: director, status: done}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"DR1-W1\"\n  summary: \"Overclaiming: 'eliminates this bottleneck' with only 25% success\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 0\n  last_seen_round: 1\n  mentions:\n    - {round: 0, reviewers: [R1, R2], note: \"Dream review\"}\n    - {round: 1, reviewers: [R1], note: \"R1-M4: Conclusion drops 'for locally correct actions' qualifier for 80.9% claim. Abstract has qualifier but Conclusion omits it. R2 confirms: overclaim via omission.\"}\n  action_items:\n    - {round: 0, action: \"Change to 'significantly alleviates' or 'enables non-zero learning'\", assigned_to: paper_agent, status: open}\n    - {round: 1, action: \"Unify '80.9%' claim wording — always include 'for windows with locally correct actions' qualifier.\", assigned_to: paper_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"DR1-W4\"\n  summary: \"h-sweep cliff claim unreliable (single seed)\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 0\n  last_seen_round: 1\n  mentions:\n    - {round: 0, reviewers: [R1, R2], note: \"Dream review — needs multi-seed\"}\n    - {round: 1, reviewers: [R1, R2], note: \"R1-M2 major, R2 AGREE. Still single seed (seed 1). Both reviewers agree cliff claim not supported.\"}\n  action_items:\n    - {round: 0, action: \"Covered by plan_002 upgrade (3 seeds per h value)\", assigned_to: director, status: done}\n    - {round: 1, action: \"Run h=5,10,20 with 2-3 seeds each. Report mean and range.\", assigned_to: agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n# === New issues from Round 1 ===\n\n- id: \"R1-C1\"\n  summary: \"'Locally correct actions' lacks formal definition — circular reasoning risk\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 1, reviewers: [R1, R2], note: \"R1 critical, R2 AGREE on definition gap but REBUT on circular reasoning — argues core argument (sign determined by episode outcome) is robust regardless of local quality definition. Consensus: formal definition needed, but not circular.\"}\n  action_items:\n    - {round: 1, action: \"Add operational definition of 'locally correct' (e.g., expert action match or oracle-based). Describe Section 4.4 credit agreement rate computation explicitly.\", assigned_to: paper_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-C2\"\n  summary: \"Theory (binary reward) vs experiment (binary + invalid action penalty) gap\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 1, reviewers: [R1, R2], note: \"Both AGREE. Proposition 2 predicts 19.1% correct sign, measured 52.07% — discrepancy likely from non-binary reward but undiscussed. R2 adds: this discrepancy undermines theory-experiment 'closed loop' claim.\"}\n  action_items:\n    - {round: 1, action: \"Option A: Re-run credit agreement rate under pure binary reward (no invalid action penalty). Option B: Extend Proposition 2 to include per-step penalties. Option C: At minimum, discuss the 19.1% vs 52.07% discrepancy.\", assigned_to: agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W1\"\n  summary: \"10/20 citations use 'Anonymous' author — ARR format violation\"\n  category: format\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 1, reviewers: [R1, R2], note: \"R2 critical, R1 AGREE. arXiv preprints with public author lists should not be anonymized. Potential desk-rejection risk. If self-citations, should use third-person per ARR policy.\"}\n  action_items:\n    - {round: 1, action: \"Replace all 'Anonymous' in references.bib with actual arXiv authors for non-self works. For self-citations, use third-person normal citation.\", assigned_to: paper_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-M1\"\n  summary: \"Cell C missing from 2x2 factorial — M2 cannot be independently verified\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 1, reviewers: [R1, R2], note: \"R1 major, R2 AGREE. Paper claims Cell C is 'degenerate' but R2 points out conceptually possible implementation (full history per step, advantage per window). Acknowledging as limitation rather than degeneracy.\"}\n  action_items:\n    - {round: 1, action: \"Either implement Cell C (full obs + per-window advantage) or reframe as acknowledged limitation in Discussion.\", assigned_to: paper_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-M5\"\n  summary: \"15 training steps may be unfair to baseline methods\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 1, reviewers: [R1, R2], note: \"R1 major, R2 partial AGREE. REINFORCE++ at 12.5% (=SFT) may just need more training. R2 notes concern is weaker for Cell A (active collapse) but valid for REINFORCE++.\"}\n  action_items:\n    - {round: 1, action: \"Run REINFORCE++ for 30+ steps. Report loss curve and gradient norms to confirm whether it has converged or is still learning.\", assigned_to: agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-m1\"\n  summary: \"Table 1 uses inconsistent reporting standards across cells\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 1, reviewers: [R1, R2], note: \"Both AGREE. Cell A: best seed, Cell B: best checkpoint, Cell D: mean. Should unify to mean ± std.\"}\n  action_items:\n    - {round: 1, action: \"Unify Table 1 reporting to mean (range) or mean ± std for all conditions.\", assigned_to: paper_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-m5\"\n  summary: \"RAGEN framework version/commit hash not reported\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 1, reviewers: [R1, R2], note: \"Both AGREE. Core claim is about RAGEN's default config — reproducibility requires exact version.\"}\n  action_items:\n    - {round: 1, action: \"Add RAGEN version/commit hash to Appendix B.\", assigned_to: paper_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W6\"\n  summary: \"'fundamental' overused (5+ times), minor writing polish needed\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 1, reviewers: [R2], note: \"R1 AGREE as style issue. Reduce to 1-2 uses.\"}\n  action_items:\n    - {round: 1, action: \"Replace most 'fundamental' with 'structural' or 'systematic'.\", assigned_to: paper_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n"
  }
}
```

</details>

---


### Tool result

_source line 155 · 2026-05-23T06:38:43.363756+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/review_issues.yaml\", \"bytes\": 12457}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 156 · 2026-05-23T06:41:15.216700+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# 审稿报告 — Round 1\n\n**论文**: Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Fix\n**目标 Venue**: EMNLP 2026 via ARR\n**截止日期**: 2026-05-25\n**审稿日期**: 2026-05-23\n**Reviewer 编排**: R1（方法严谨性）+ R2（新颖性/完整性）\n**交叉轮次**: 1 轮交叉分享，关键问题全部收敛\n\n---\n\n## Summary\n\n本文诊断了多轮 agent RL 中 step-independent windowing 的两个失败机制：policy information loss (M1，截断上下文造成恒定性能天花板) 和 advantage sign misattribution (M2，梯度方向错误造成累积退化)。通过 2×2 factorial 实验分离两个机制的贡献，并展示 episode-level GRPO（GRPO 的原始设计）可解决两者。11-seed 系统评估表明 73% 的 seed 避免崩溃，但仅 27% 实现 OOD 泛化。跨尺度 (8B) 和跨环境 (ScienceWorld) 验证提供了初步 generality 证据。\n\n---\n\n## Strengths\n\n**S1. 精准的问题诊断与结构化分析框架 [R1-S1, R2-S1, 共识]。** 将 step-independent training 崩溃分解为 M1 (constant ceiling) 和 M2 (cumulative divergence) 两个可分离机制，对社区理解此类 failure mode 有明确价值。这种诊断性贡献在同期工作中独特。\n\n**S2. 干净的 factorial 实验设计 [R1-S2, R2-S1, 共识]。** A→B 消除 M2（collapse → bounded learning），B→D 消除 M1（bounded → generalization），辅以 dense reward、γ sweep、REINFORCE++ 等控制实验系统排除替代假说。\n\n**S3. 坦诚的负面结果报告 [R1-S3, R2-S2, 共识]。** 11-seed 评估的 27% 泛化率透明报告，\"necessary but not sufficient\" 的 claim 定位准确。\n\n**S4. 多层次实证验证 [R1-S4, 共识]。** Credit agreement rate (52.07% ≈ random)、advantage sign 与 episode outcome 高相关 (r>0.99) vs local quality 低相关 (r=0.068)、γ=1.0 同样崩溃——系统排除了 discounting 假说。\n\n**S5. 跨尺度/跨环境验证方向正确 [R2-S3, 部分共识]。** 1.7B→8B 和 ALFWorld→ScienceWorld 的验证思路正确，但均为 single seed（见 W4）。\n\n---\n\n## Weaknesses\n\n### Must-Fix (Critical)\n\n**W1. \"Locally correct actions\" 缺乏形式定义 [R1-C1, R2 AGREE]。**\n整个理论框架建立在 \"locally correct actions\" 上，但全文未给出形式定义。Proposition 2 的 \"80.9% incorrect sign\" 含义完全取决于 \"correct\" 的定义。Section 4.4 的 credit agreement rate 度量的操作化方式（如何度量 \"local action quality\"）也未描述。两位 Reviewer 共识：需要形式定义，但非循环论证（R2 的修正判断——核心论点 \"sign 由 episode outcome 决定\" 不依赖 local quality 的精确定义）。\n\n**W2. 理论 (binary reward) 与实验 (binary + invalid action penalty) 不一致 [R1-C2, R2 AGREE]。**\nPropositions 1-2 严格依赖 binary reward (R ∈ {0, r+})，但实验使用了 invalid action penalty = 0.1。Appendix Remark 仅定性声称 \"qualitative conclusion is preserved\"，无定量分析。R2 补充：Proposition 2 预测 19.1% correct sign rate，实测 52.07%，discrepancy 可能正是 non-binary reward 导致，但论文未讨论。\n\n**W3. 10/20 引用使用 \"Anonymous\" 作者——ARR 格式违规 [R2-W1, R1 AGREE]。**\nirc2026, grpolambda2025, oar2026, ragen2_2026, grpocollapse2025, gradientcoupling2025, turnppo2026, gagpo2026, mtgrpo2025, sweetrl2025——这些均为已公开 arXiv 预印本，有可查的真实作者信息。ACL ARR 仅要求匿名化自己的在审稿件，不应匿名化他人已公开工作。50% 引用缺少真实作者是严重合规问题，可能触发 desk-rejection checklist。\n\n### Should-Fix (Major)\n\n**W4. 8B 和 ScienceWorld claims 基于 single seed [R1-M3, R2-W4, 共识]。**\n论文在 1.7B 上用 11 seeds 发现 27% collapse、36% stagnant、27% generalize，但 8B 和 ScienceWorld 均为 single seed。\"Both mechanisms operate across environments, confirming...\" 的 confirmatory language 与实际 statistical power 不匹配。应降级为 \"preliminary evidence\"。\n\n**W5. h-sweep cliff claim 基于 single seed [R1-M2, R2 AGREE]。**\nFigure 1(b) 的 h=10→h=20 \"credit assignment cliff\" 基于 seed 1 的单次结果。结合 Table 2 的高 seed variability（同条件下 8.21%–30.60%），无法排除 seed-specific 噪声。\n\n**W6. 核心贡献新颖性有限 [R2-W2, R1 部分 REBUT]。**\nFix 是回归 GRPO 原始设计（论文自己承认 \"This is GRPO's original design\"）。同期 5+ 独立工作（IRC, MC-GRPO, GRPO-λ, OAR, RAGEN-2）收敛到类似诊断。R1 反驳：M1/M2 factorial 分离框架有独立价值，但同意在 Findings 定位下合适，不足以支撑 main conference。**分歧记录**：R2 认为 critical（Excitement 2.5），R1 认为 major（Excitement 3.5）。\n\n**W7. 引用数量不足：仅 20 篇 [R2-W3, R1 AGREE]。**\nEMNLP long paper 通常 40-60 篇引用。缺失类别：RL 基础（PPO、reward shaping classics）、LLM agent 训练/评估（AgentTuning, Reflexion, ReAct）、credit assignment 相关（COMA, PRM, Math-Shepherd）。R1 对 agent benchmark 类引用的优先级低于 R2。\n\n**W8. Cell C 缺失使 factorial 不完整 [R1-M1, R2 AGREE]。**\nCell C (full observation + step-level advantage) 被论述为 \"degenerate\"，但概念上可实现（每步看全 history，advantage 仍 per-window）。缺失意味着 M2 无法在无 M1 条件下独立验证。\n\n**W9. 15 步训练可能不利于 baseline 方法 [R1-M5, R2 部分 AGREE]。**\nREINFORCE++ 停留在 SFT baseline (12.5%) 可能因训练不足而非方法无效。R2 补充：Cell A 的崩溃不受此影响（主动退化），concern 主要针对 REINFORCE++ 等替代方法。\n\n**W10. Conclusion 对 \"80.9%\" claim 省略 qualifier [R1-M4, R2 AGREE on wording]。**\nAbstract 写 \"for locally correct actions\" 但 Conclusion 省略为 \"~80.9% of gradient updates carry incorrect sign\"——扩大了 claim 范围。R2 修正：在 binary reward 假设下 80.9% 是精确值而非 upper bound，但 qualifier 省略确实是 overclaim。\n\n**W11. 理论分析深度有限 [R2-W5, R1 部分 AGREE]。**\nP(correct|update) = p/[1-(1-p)^K] 是简单条件概率。缺乏从 \"80.9% wrong sign\" 到 \"training will diverge\" 的形式化连接。R1 建议：简化设定下的发散证明可显著增强理论贡献。\n\n### Nice-to-Fix (Minor)\n\n**W12.** Table 1 对不同 cell 使用不同报告标准（best seed / best checkpoint / mean）[R1-m1, R2 AGREE]\n**W13.** Eq. 3 近似条件不明确 [R1-m2, R2 AGREE]\n**W14.** Section 4.4 \"local action quality\" 操作化定义未描述 [R1-m3, R2 AGREE]\n**W15.** Appendix A.3 \"Why Defaults\" 部分 Factor 3 措辞偏 editorial，\"design accident\" 建议改为 \"inherited default\" [R1-m4, R2 部分 REBUT]\n**W16.** RAGEN 版本/commit hash 未报告 [R1-m5, R2 AGREE]\n**W17.** \"fundamental\" 一词过度使用（5+ 次）[R2-W6, R1 AGREE]\n**W18.** Dense reward 实验细节不足（Appendix 仅两句话）[R2-W7, R1 AGREE]\n**W19.** Figure 1(a) 图例字号偏小、多线区分度有限 [R2-W8, R1 AGREE]\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 一致同意（`[AGREE]`）：\n1. \"locally correct actions\" 需要形式定义（但非循环论证）\n2. Binary reward 理论与 non-binary 实验存在 gap\n3. Anonymous 引用是严重格式违规\n4. 8B/ScienceWorld/h-sweep 的 single-seed claims 统计 power 不足\n5. 引用总量不足\n6. Table 1 报告标准应统一\n7. RAGEN 版本需报告\n8. COMA、PRM、PPO 等为高优先级缺失引用\n\n## Reviewer Divergence\n\n| 议题 | R1 | R2 | 说明 |\n|------|----|----|------|\n| **新颖性严重性** | Major（Findings 可接受） | Critical（影响 Excitement） | R1 认为 M1/M2 factorial 分离有独立值；R2 更重视 fix 非新方法+同期工作多 |\n| **Excitement** | 3.5/5 | 2.5/5 | 0.5 分差——R1 偏重诊断价值，R2 偏重方法创新 |\n| **Soundness** | 3/5 | 3.5/5 | R2 认为 factorial 方法论扎实抵消了理论缺陷 |\n| **R1-M4 (80.9% 性质)** | Upper bound | 精确值（under assumptions） | R2 修正：在 binary reward 假设下是精确计算 |\n| **Cell B 下降原因** | M1 下 overfitting（不需要第三机制） | 可能暗示第三机制 | R1 反驳成立——overfitting 解释与 evidence 一致 |\n\n---\n\n## Questions（需要作者澄清）\n\n**Q1.** Section 4.4 中 \"local action quality\" 具体如何度量？操作化定义是什么？\n\n**Q2.** 是否在 pure binary reward（无 invalid action penalty）下验证了 credit agreement rate？如果有，结果与 52.07% 差异多大？19.1% vs 52.07% 的 discrepancy 如何解释？\n\n**Q3.** seed1 使用 \"RAGEN built-in eval; checkpoint unavailable for re-evaluation\"——与其他 seed 的 eval protocol 是否完全一致？\n\n**Q4.** Episode-level training 在 1.7B 上的实际 GPU 内存使用和训练时间 vs step-independent？\n\n**Q5.** 11-seed 中是否分析了 generalized vs stagnant seeds 的初始化特征差异？\n\n**Q6.** 是否有与 Turn-PPO 或 GAGPO 的直接实验对比？\n\n---\n\n## Missing References\n\n**高优先级**（与论文主题直接相关，两位 Reviewer 共识）：\n- PPO (Schulman et al., 2017) — 论文多处提及但未引用原始文献\n- COMA (Foerster et al., 2018) — 论文 Appendix A.4 画了多智能体类比但未引用\n- Process Reward Models / Let's Verify Step by Step (Lightman et al., 2023)\n- Math-Shepherd (Wang et al., 2023)\n- ReAct (Yao et al., 2023)\n\n**中优先级**（领域 background）：\n- TRPO (Schulman et al., 2015)\n- Hindsight Experience Replay (Andrychowicz et al., 2017)\n- Reward shaping theory (Ng et al., 1999)\n- QMIX (Rashid et al., 2018)\n\n**可选**（R1/R2 优先级有分歧）：\n- AgentTuning, Reflexion, WebShop, AgentBench, FireAct\n- RC-GRPO (arXiv:2602.03025)\n- TSR (arXiv:2602.11767)\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未配置。\n\n---\n\n## Visual Layout Check（非评分项）\n\n状态：**done**（2026-05-23T06:24 → 06:27，耗时约 3 分钟）\n\n| 严重性 | 位置 | 发现 |\n|--------|------|------|\n| **critical** | page 12 | 仅 ~10 行文字后整页空白（>80%），LaTeX float 问题——Figure 4 被推到 page 13 留下空页。需调整 float placement。 |\n| warning | page 1-3 | 前 3 页无任何 display item（figure/table），审稿人前 4 页只见纯文本+数学推导。建议将 Figure 1 或概念图提前到 page 1-2。 |\n| warning | page 5 | 单页承载 1 figure + 2 tables，视觉密度过高，与前 3 页纯文本形成强反差。考虑平衡分布。 |\n| warning | page 13 | Figure 4 位于页面下半部，上方 ~40% 空白。与 page 12 合计附录末尾 2 页空间利用率极低。 |\n| info | page 5 | Figure 1 legend 字号偏小（约正文 60%），多条目密集排列。 |\n| info | page 7 | Figure 3(a) 部分 bar 上数值标注字号较小，打印阅读可能吃力。 |\n| info | page 4 | 论文第一个 display item（Table 1）出现在 page 4，对实证论文偏晚。 |\n\n---\n\n## Overall Assessment\n\n**Overall: 3.0 — Findings**\n\n| 维度 | R1 | R2 | 综合 |\n|------|----|----|------|\n| Soundness | 3/5 | 3.5/5 | 3/5 |\n| Excitement | 3.5/5 | 2.5/5 | 3/5 |\n| Reproducibility | 3/5 | 3.5/5 | 3/5 |\n| Confidence | 4/5 | 4/5 | 4/5 |\n\n**评分理由**：\n\n论文精准识别了 step-independent agent RL 中一个重要且广泛存在的 failure mode，M1/M2 dual mechanism 分离框架和 factorial 实验设计是扎实的诊断性贡献。坦诚的 11-seed 负面结果报告增强了可信度。\n\n但存在以下限制：(1) 理论核心概念 \"locally correct actions\" 缺乏形式定义，理论与实验的 reward structure 不一致（binary vs binary+penalty），削弱了理论-实验闭环；(2) 关键 generality claims（8B、ScienceWorld、h-sweep cliff）均基于 single seed，与论文自身展示的高 seed 方差矛盾；(3) 核心 fix 是回归 GRPO 原始设计，方法新颖性有限；(4) 50% 引用使用 Anonymous 作者，存在 ARR 合规风险。\n\n在 Findings 定位下，诊断性贡献（M1/M2 分离 + factorial 验证 + seed variability 分析）达到接收门槛。升级到 Conference 需要：形式化 \"locally correct\" 定义、补充 multi-seed 8B 验证、修复引用格式、增加引用覆盖。\n\n---\n\n## Detailed Comments\n\n### Abstract\n- \"fundamental credit assignment pathology\" 措辞过重，建议改为 \"structural\"\n- \"80.9% of gradient updates for locally correct actions carry incorrect sign\" — qualifier 正确，但需在全文保持一致（Conclusion 省略了 qualifier）\n- \"consistent with an empirically measured 52% credit agreement rate\" — 理论预测 19.1% vs 实测 52%，两者关系未解释\n\n### Section 1 (Introduction)\n- Contribution 3 \"necessary but not sufficient\" 定位准确，但意味着 73% 的情况下方案不达目标，实际影响力存疑\n- 第一段对同期工作的定位（\"share a common, unscrutinized implementation pattern\"）需加入更多具体引用\n\n### Section 2 (Method)\n- POMDP 形式化标准，无问题\n- M1/M2 分离是论文最有价值的概念贡献\n- Eq. 3 的 ≈ 号缺乏成立条件说明\n- Cell C \"degenerate\" 论述混淆了实现方式与概念区分\n\n### Section 3 (Theoretical Analysis)\n- Proposition 2 推导在 binary reward 假设下数学正确\n- 缺少 p 随训练动态变化时的分析（正反馈循环仅在 Discussion 定性提及）\n- \"sign errors cause active divergence\" 缺乏梯度动态系统的形式化分析\n\n### Section 4 (Experiments)\n- Table 1 报告标准不一致（best seed / best checkpoint / mean）\n- Section 4.4 sign verification 是亮点实验，但 \"local action quality\" 操作化未描述\n- Section 4.5 的 11-seed 分析有价值，\"collapsed\" 定义（>50% decline for ≥3 steps）可做 sensitivity analysis\n- Table 3 (8B) 使用不同解码温度（SFT: τ=0, RL: τ=0.4），引入额外变量\n- Section 4.7 ScienceWorld 仅展示 Cell A 崩溃，未报告 episode-level 的正面结果\n\n### Section 5 (Related Work)\n- 结构合理但覆盖面不足（20 篇引用）\n- \"but all share a common assumption: trajectory decomposition into fixed windows is benign\" 过强——GiGPO/GAGPO 明确在 windowing 框架内改进 credit assignment\n\n### Section 6 (Discussion)\n- M1-M2 interaction（正反馈循环）是有洞察力的观察，建议在理论部分形式化\n- Practitioner guidance 基于仅两个环境，generalizability 注明\n\n### Section 7 (Conclusion)\n- \"~80.9% of gradient updates carry incorrect sign\" 缺少 \"for locally correct actions\" qualifier\n\n### Limitations\n- 位置正确（conclusion 后 references 前），仅一个 section，符合 EMNLP 规定\n- 覆盖面适当\n- 建议补充：理论分析仅适用于 binary reward 的局限性\n\n### Appendix\n- A.3 (Why Defaults) 有独立价值但 Factor 3 措辞可更中性\n- A.4 (Classical Connection) 缺少 COMA/QMIX 引用\n- Page 12 有严重排版空白问题（LaTeX float）\n",
  "project": "cost-verify-agent-rl",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.0 — Findings",
  "review_chat_id": "oc_648eaf83d2b24d445764257cf6a55525"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# 审稿报告 — Round 1\n\n**论文**: Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Fix\n**目标 Venue**: EMNLP 2026 via ARR\n**截止日期**: 2026-05-25\n**审稿日期**: 2026-05-23\n**Reviewer 编排**: R1（方法严谨性）+ R2（新颖性/完整性）\n**交叉轮次**: 1 轮交叉分享，关键问题全部收敛\n\n---\n\n## Summary\n\n本文诊断了多轮 agent RL 中 step-independent windowing 的两个失败机制：policy information loss (M1，截断上下文造成恒定性能天花板) 和 advantage sign misattribution (M2，梯度方向错误造成累积退化)。通过 2×2 factorial 实验分离两个机制的贡献，并展示 episode-level GRPO（GRPO 的原始设计）可解决两者。11-seed 系统评估表明 73% 的 seed 避免崩溃，但仅 27% 实现 OOD 泛化。跨尺度 (8B) 和跨环境 (ScienceWorld) 验证提供了初步 generality 证据。\n\n---\n\n## Strengths\n\n**S1. 精准的问题诊断与结构化分析框架 [R1-S1, R2-S1, 共识]。** 将 step-independent training 崩溃分解为 M1 (constant ceiling) 和 M2 (cumulative divergence) 两个可分离机制，对社区理解此类 failure mode 有明确价值。这种诊断性贡献在同期工作中独特。\n\n**S2. 干净的 factorial 实验设计 [R1-S2, R2-S1, 共识]。** A→B 消除 M2（collapse → bounded learning），B→D 消除 M1（bounded → generalization），辅以 dense reward、γ sweep、REINFORCE++ 等控制实验系统排除替代假说。\n\n**S3. 坦诚的负面结果报告 [R1-S3, R2-S2, 共识]。** 11-seed 评估的 27% 泛化率透明报告，\"necessary but not sufficient\" 的 claim 定位准确。\n\n**S4. 多层次实证验证 [R1-S4, 共识]。** Credit agreement rate (52.07% ≈ random)、advantage sign 与 episode outcome 高相关 (r>0.99) vs local quality 低相关 (r=0.068)、γ=1.0 同样崩溃——系统排除了 discounting 假说。\n\n**S5. 跨尺度/跨环境验证方向正确 [R2-S3, 部分共识]。** 1.7B→8B 和 ALFWorld→ScienceWorld 的验证思路正确，但均为 single seed（见 W4）。\n\n---\n\n## Weaknesses\n\n### Must-Fix (Critical)\n\n**W1. \"Locally correct actions\" 缺乏形式定义 [R1-C1, R2 AGREE]。**\n整个理论框架建立在 \"locally correct actions\" 上，但全文未给出形式定义。Proposition 2 的 \"80.9% incorrect sign\" 含义完全取决于 \"correct\" 的定义。Section 4.4 的 credit agreement rate 度量的操作化方式（如何度量 \"local action quality\"）也未描述。两位 Reviewer 共识：需要形式定义，但非循环论证（R2 的修正判断——核心论点 \"sign 由 episode outcome 决定\" 不依赖 local quality 的精确定义）。\n\n**W2. 理论 (binary reward) 与实验 (binary + invalid action penalty) 不一致 [R1-C2, R2 AGREE]。**\nPropositions 1-2 严格依赖 binary reward (R ∈ {0, r+})，但实验使用了 invalid action penalty = 0.1。Appendix Remark 仅定性声称 \"qualitative conclusion is preserved\"，无定量分析。R2 补充：Proposition 2 预测 19.1% correct sign rate，实测 52.07%，discrepancy 可能正是 non-binary reward 导致，但论文未讨论。\n\n**W3. 10/20 引用使用 \"Anonymous\" 作者——ARR 格式违规 [R2-W1, R1 AGREE]。**\nirc2026, grpolambda2025, oar2026, ragen2_2026, grpocollapse2025, gradientcoupling2025, turnppo2026, gagpo2026, mtgrpo2025, sweetrl2025——这些均为已公开 arXiv 预印本，有可查的真实作者信息。ACL ARR 仅要求匿名化自己的在审稿件，不应匿名化他人已公开工作。50% 引用缺少真实作者是严重合规问题，可能触发 desk-rejection checklist。\n\n### Should-Fix (Major)\n\n**W4. 8B 和 ScienceWorld claims 基于 single seed [R1-M3, R2-W4, 共识]。**\n论文在 1.7B 上用 11 seeds 发现 27% collapse、36% stagnant、27% generalize，但 8B 和 ScienceWorld 均为 single seed。\"Both mechanisms operate across environments, confirming...\" 的 confirmatory language 与实际 statistical power 不匹配。应降级为 \"preliminary evidence\"。\n\n**W5. h-sweep cliff claim 基于 single seed [R1-M2, R2 AGREE]。**\nFigure 1(b) 的 h=10→h=20 \"credit assignment cliff\" 基于 seed 1 的单次结果。结合 Table 2 的高 seed variability（同条件下 8.21%–30.60%），无法排除 seed-specific 噪声。\n\n**W6. 核心贡献新颖性有限 [R2-W2, R1 部分 REBUT]。**\nFix 是回归 GRPO 原始设计（论文自己承认 \"This is GRPO's original design\"）。同期 5+ 独立工作（IRC, MC-GRPO, GRPO-λ, OAR, RAGEN-2）收敛到类似诊断。R1 反驳：M1/M2 factorial 分离框架有独立价值，但同意在 Findings 定位下合适，不足以支撑 main conference。**分歧记录**：R2 认为 critical（Excitement 2.5），R1 认为 major（Excitement 3.5）。\n\n**W7. 引用数量不足：仅 20 篇 [R2-W3, R1 AGREE]。**\nEMNLP long paper 通常 40-60 篇引用。缺失类别：RL 基础（PPO、reward shaping classics）、LLM agent 训练/评估（AgentTuning, Reflexion, ReAct）、credit assignment 相关（COMA, PRM, Math-Shepherd）。R1 对 agent benchmark 类引用的优先级低于 R2。\n\n**W8. Cell C 缺失使 factorial 不完整 [R1-M1, R2 AGREE]。**\nCell C (full observation + step-level advantage) 被论述为 \"degenerate\"，但概念上可实现（每步看全 history，advantage 仍 per-window）。缺失意味着 M2 无法在无 M1 条件下独立验证。\n\n**W9. 15 步训练可能不利于 baseline 方法 [R1-M5, R2 部分 AGREE]。**\nREINFORCE++ 停留在 SFT baseline (12.5%) 可能因训练不足而非方法无效。R2 补充：Cell A 的崩溃不受此影响（主动退化），concern 主要针对 REINFORCE++ 等替代方法。\n\n**W10. Conclusion 对 \"80.9%\" claim 省略 qualifier [R1-M4, R2 AGREE on wording]。**\nAbstract 写 \"for locally correct actions\" 但 Conclusion 省略为 \"~80.9% of gradient updates carry incorrect sign\"——扩大了 claim 范围。R2 修正：在 binary reward 假设下 80.9% 是精确值而非 upper bound，但 qualifier 省略确实是 overclaim。\n\n**W11. 理论分析深度有限 [R2-W5, R1 部分 AGREE]。**\nP(correct|update) = p/[1-(1-p)^K] 是简单条件概率。缺乏从 \"80.9% wrong sign\" 到 \"training will diverge\" 的形式化连接。R1 建议：简化设定下的发散证明可显著增强理论贡献。\n\n### Nice-to-Fix (Minor)\n\n**W12.** Table 1 对不同 cell 使用不同报告标准（best seed / best checkpoint / mean）[R1-m1, R2 AGREE]\n**W13.** Eq. 3 近似条件不明确 [R1-m2, R2 AGREE]\n**W14.** Section 4.4 \"local action quality\" 操作化定义未描述 [R1-m3, R2 AGREE]\n**W15.** Appendix A.3 \"Why Defaults\" 部分 Factor 3 措辞偏 editorial，\"design accident\" 建议改为 \"inherited default\" [R1-m4, R2 部分 REBUT]\n**W16.** RAGEN 版本/commit hash 未报告 [R1-m5, R2 AGREE]\n**W17.** \"fundamental\" 一词过度使用（5+ 次）[R2-W6, R1 AGREE]\n**W18.** Dense reward 实验细节不足（Appendix 仅两句话）[R2-W7, R1 AGREE]\n**W19.** Figure 1(a) 图例字号偏小、多线区分度有限 [R2-W8, R1 AGREE]\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 一致同意（`[AGREE]`）：\n1. \"locally correct actions\" 需要形式定义（但非循环论证）\n2. Binary reward 理论与 non-binary 实验存在 gap\n3. Anonymous 引用是严重格式违规\n4. 8B/ScienceWorld/h-sweep 的 single-seed claims 统计 power 不足\n5. 引用总量不足\n6. Table 1 报告标准应统一\n7. RAGEN 版本需报告\n8. COMA、PRM、PPO 等为高优先级缺失引用\n\n## Reviewer Divergence\n\n| 议题 | R1 | R2 | 说明 |\n|------|----|----|------|\n| **新颖性严重性** | Major（Findings 可接受） | Critical（影响 Excitement） | R1 认为 M1/M2 factorial 分离有独立值；R2 更重视 fix 非新方法+同期工作多 |\n| **Excitement** | 3.5/5 | 2.5/5 | 0.5 分差——R1 偏重诊断价值，R2 偏重方法创新 |\n| **Soundness** | 3/5 | 3.5/5 | R2 认为 factorial 方法论扎实抵消了理论缺陷 |\n| **R1-M4 (80.9% 性质)** | Upper bound | 精确值（under assumptions） | R2 修正：在 binary reward 假设下是精确计算 |\n| **Cell B 下降原因** | M1 下 overfitting（不需要第三机制） | 可能暗示第三机制 | R1 反驳成立——overfitting 解释与 evidence 一致 |\n\n---\n\n## Questions（需要作者澄清）\n\n**Q1.** Section 4.4 中 \"local action quality\" 具体如何度量？操作化定义是什么？\n\n**Q2.** 是否在 pure binary reward（无 invalid action penalty）下验证了 credit agreement rate？如果有，结果与 52.07% 差异多大？19.1% vs 52.07% 的 discrepancy 如何解释？\n\n**Q3.** seed1 使用 \"RAGEN built-in eval; checkpoint unavailable for re-evaluation\"——与其他 seed 的 eval protocol 是否完全一致？\n\n**Q4.** Episode-level training 在 1.7B 上的实际 GPU 内存使用和训练时间 vs step-independent？\n\n**Q5.** 11-seed 中是否分析了 generalized vs stagnant seeds 的初始化特征差异？\n\n**Q6.** 是否有与 Turn-PPO 或 GAGPO 的直接实验对比？\n\n---\n\n## Missing References\n\n**高优先级**（与论文主题直接相关，两位 Reviewer 共识）：\n- PPO (Schulman et al., 2017) — 论文多处提及但未引用原始文献\n- COMA (Foerster et al., 2018) — 论文 Appendix A.4 画了多智能体类比但未引用\n- Process Reward Models / Let's Verify Step by Step (Lightman et al., 2023)\n- Math-Shepherd (Wang et al., 2023)\n- ReAct (Yao et al., 2023)\n\n**中优先级**（领域 background）：\n- TRPO (Schulman et al., 2015)\n- Hindsight Experience Replay (Andrychowicz et al., 2017)\n- Reward shaping theory (Ng et al., 1999)\n- QMIX (Rashid et al., 2018)\n\n**可选**（R1/R2 优先级有分歧）：\n- AgentTuning, Reflexion, WebShop, AgentBench, FireAct\n- RC-GRPO (arXiv:2602.03025)\n- TSR (arXiv:2602.11767)\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未配置。\n\n---\n\n## Visual Layout Check（非评分项）\n\n状态：**done**（2026-05-23T06:24 → 06:27，耗时约 3 分钟）\n\n| 严重性 | 位置 | 发现 |\n|--------|------|------|\n| **critical** | page 12 | 仅 ~10 行文字后整页空白（>80%），LaTeX float 问题——Figure 4 被推到 page 13 留下空页。需调整 float placement。 |\n| warning | page 1-3 | 前 3 页无任何 display item（figure/table），审稿人前 4 页只见纯文本+数学推导。建议将 Figure 1 或概念图提前到 page 1-2。 |\n| warning | page 5 | 单页承载 1 figure + 2 tables，视觉密度过高，与前 3 页纯文本形成强反差。考虑平衡分布。 |\n| warning | page 13 | Figure 4 位于页面下半部，上方 ~40% 空白。与 page 12 合计附录末尾 2 页空间利用率极低。 |\n| info | page 5 | Figure 1 legend 字号偏小（约正文 60%），多条目密集排列。 |\n| info | page 7 | Figure 3(a) 部分 bar 上数值标注字号较小，打印阅读可能吃力。 |\n| info | page 4 | 论文第一个 display item（Table 1）出现在 page 4，对实证论文偏晚。 |\n\n---\n\n## Overall Assessment\n\n**Overall: 3.0 — Findings**\n\n| 维度 | R1 | R2 | 综合 |\n|------|----|----|------|\n| Soundness | 3/5 | 3.5/5 | 3/5 |\n| Excitement | 3.5/5 | 2.5/5 | 3/5 |\n| Reproducibility | 3/5 | 3.5/5 | 3/5 |\n| Confidence | 4/5 | 4/5 | 4/5 |\n\n**评分理由**：\n\n论文精准识别了 step-independent agent RL 中一个重要且广泛存在的 failure mode，M1/M2 dual mechanism 分离框架和 factorial 实验设计是扎实的诊断性贡献。坦诚的 11-seed 负面结果报告增强了可信度。\n\n但存在以下限制：(1) 理论核心概念 \"locally correct actions\" 缺乏形式定义，理论与实验的 reward structure 不一致（binary vs binary+penalty），削弱了理论-实验闭环；(2) 关键 generality claims（8B、ScienceWorld、h-sweep cliff）均基于 single seed，与论文自身展示的高 seed 方差矛盾；(3) 核心 fix 是回归 GRPO 原始设计，方法新颖性有限；(4) 50% 引用使用 Anonymous 作者，存在 ARR 合规风险。\n\n在 Findings 定位下，诊断性贡献（M1/M2 分离 + factorial 验证 + seed variability 分析）达到接收门槛。升级到 Conference 需要：形式化 \"locally correct\" 定义、补充 multi-seed 8B 验证、修复引用格式、增加引用覆盖。\n\n---\n\n## Detailed Comments\n\n### Abstract\n- \"fundamental credit assignment pathology\" 措辞过重，建议改为 \"structural\"\n- \"80.9% of gradient updates for locally correct actions carry incorrect sign\" — qualifier 正确，但需在全文保持一致（Conclusion 省略了 qualifier）\n- \"consistent with an empirically measured 52% credit agreement rate\" — 理论预测 19.1% vs 实测 52%，两者关系未解释\n\n### Section 1 (Introduction)\n- Contribution 3 \"necessary but not sufficient\" 定位准确，但意味着 73% 的情况下方案不达目标，实际影响力存疑\n- 第一段对同期工作的定位（\"share a common, unscrutinized implementation pattern\"）需加入更多具体引用\n\n### Section 2 (Method)\n- POMDP 形式化标准，无问题\n- M1/M2 分离是论文最有价值的概念贡献\n- Eq. 3 的 ≈ 号缺乏成立条件说明\n- Cell C \"degenerate\" 论述混淆了实现方式与概念区分\n\n### Section 3 (Theoretical Analysis)\n- Proposition 2 推导在 binary reward 假设下数学正确\n- 缺少 p 随训练动态变化时的分析（正反馈循环仅在 Discussion 定性提及）\n- \"sign errors cause active divergence\" 缺乏梯度动态系统的形式化分析\n\n### Section 4 (Experiments)\n- Table 1 报告标准不一致（best seed / best checkpoint / mean）\n- Section 4.4 sign verification 是亮点实验，但 \"local action quality\" 操作化未描述\n- Section 4.5 的 11-seed 分析有价值，\"collapsed\" 定义（>50% decline for ≥3 steps）可做 sensitivity analysis\n- Table 3 (8B) 使用不同解码温度（SFT: τ=0, RL: τ=0.4），引入额外变量\n- Section 4.7 ScienceWorld 仅展示 Cell A 崩溃，未报告 episode-level 的正面结果\n\n### Section 5 (Related Work)\n- 结构合理但覆盖面不足（20 篇引用）\n- \"but all share a common assumption: trajectory decomposition into fixed windows is benign\" 过强——GiGPO/GAGPO 明确在 windowing 框架内改进 credit assignment\n\n### Section 6 (Discussion)\n- M1-M2 interaction（正反馈循环）是有洞察力的观察，建议在理论部分形式化\n- Practitioner guidance 基于仅两个环境，generalizability 注明\n\n### Section 7 (Conclusion)\n- \"~80.9% of gradient updates carry incorrect sign\" 缺少 \"for locally correct actions\" qualifier\n\n### Limitations\n- 位置正确（conclusion 后 references 前），仅一个 section，符合 EMNLP 规定\n- 覆盖面适当\n- 建议补充：理论分析仅适用于 binary reward 的局限性\n\n### Appendix\n- A.3 (Why Defaults) 有独立价值但 Factor 3 措辞可更中性\n- A.4 (Classical Connection) 缺少 COMA/QMIX 引用\n- Page 12 有严重排版空白问题（LaTeX float）\n",
    "project": "cost-verify-agent-rl",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.0 — Findings",
    "review_chat_id": "oc_648eaf83d2b24d445764257cf6a55525"
  }
}
```

</details>

---


### Tool result

_source line 157 · 2026-05-23T06:41:19.431912+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_4ebf0fb2d0159caa355a1a855f5ac59f:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4215
}
```

</details>

---


### Assistant

_source line 158 · 2026-05-23T06:41:31.806977+00:00_

**审稿完成。**

Round 1 审稿报告已投递给 Research Director。

**结果概要**：
- **Overall: 3.0 (Findings)**，R1: 3.0, R2: 2.5，综合取 3.0
- **3 个 Must-Fix**：(1) "locally correct actions" 需形式定义；(2) 理论 binary reward 与实验 non-binary gap（19.1% vs 52.07% 未解释）；(3) 10/20 引用用 Anonymous——ARR 合规风险
- **8 个 Should-Fix**：single-seed claims（8B/ScienceWorld/h-sweep）、新颖性有限（fix = 原始 GRPO）、引用仅 20 篇、Cell C 缺失、15 步训练步数、Conclusion 省略 qualifier、理论深度有限
- **8 个 Nice-to-Fix**：Table 1 报告标准、Eq.3 近似条件、排版空白等
- **视觉审查**：1 critical（page 12 整页空白）+ 3 warning + 3 info
- **Issue Tracker**：已同步更新，含 Round 0 遗留 + Round 1 新发现共 18 条

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director"
}
```

</details>

---


## Round 14

## Round 14

2 recorded events


### User

_source line 159 · 2026-05-23T06:41:34.422082+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交给 Review Director。

主要判断：
- 与 R1 在 12/17 个具体 issue 上达成共识（C1 形式定义缺失、C2 binary reward gap、M1 Cell C 缺失、M2-M3 单 seed、m1 报告标准不一致等）
- 在 M4 上部分反驳：80.9% 在模型假设下是精确值而非 upper bound，但同意 Conclusion 省略 qualifier 构成 overclaim
- 在 m4 上部分反驳：Appendix A.3 的 6 因素分析有独立价值，Factor 3 是事实陈述非 blame
- 与 R1 的主要分歧在 Excitement 评分：我因同期工作收敛和引用格式问题给出更低分（2.5 vs R1 的 3.5）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 160 · 2026-05-23T06:41:48.078953+00:00_

审稿报告已成功投递至 Research Director。

**Round 1 审稿完成总结**：

- **Overall: 3.0 (Findings)**
- 2 位 Reviewer 独立初审 → 交叉分享 → 1 轮收敛
- R1 给 3.0，R2 给 2.5，综合 3.0
- **3 个 Critical**：(1) "locally correct actions" 缺形式定义，(2) 理论(binary)与实验(non-binary) reward 不一致，(3) 50% 引用使用 Anonymous 作者
- **8 个 Major**：single-seed claims、新颖性有限、引用不足、Cell C 缺失、训练步数可能不公平等
- **8 个 Minor**：报告标准不一致、用词等
- Issue Tracker 已同步更新（`review_issues.yaml`）
- 视觉审查已完成并纳入报告（1 critical 排版问题：page 12 空白页）
- 外部审稿：未配置

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director"
}
```

</details>

---


## Round 15

## Round 15

58 recorded events


### User

_source line 161 · 2026-05-23T09:02:06.111031+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: cost-verify-agent-rl
- 论文路径: /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: ARR
- 截止日期: 未提供，请自行调研
- **引用验证**: ✅ 后台自动运行中，完成后你会收到 [引用验证结果] 消息，请在合成报告时纳入

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 162 · 2026-05-23T09:02:13.857288+00:00_

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
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 163 · 2026-05-23T09:02:13.857937+00:00_

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
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 164 · 2026-05-23T09:02:21.058233+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,director_post_to_reviewer,get_external_review_status,get_visual_check_status,submit_review_report_to_research_director,update_review_issues,read_project_file,WebSearch",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,director_post_to_reviewer,get_external_review_status,get_visual_check_status,submit_review_report_to_research_director,update_review_issues,read_project_file,WebSearch",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 165 · 2026-05-23T09:02:21.108788+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 166 · 2026-05-23T09:02:23.215952+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,director_post_to_reviewer,get_external_review_status,get_visual_check_status,submit_review_report_to_research_director,update_review_issues,read_project_file",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,director_post_to_reviewer,get_external_review_status,get_visual_check_status,submit_review_report_to_research_director,update_review_issues,read_project_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 167 · 2026-05-23T09:02:23.266526+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 168 · 2026-05-23T09:02:27.381730+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "cost-verify-agent-rl"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "cost-verify-agent-rl"
  }
}
```

</details>

---


### Tool result

_source line 169 · 2026-05-23T09:02:28.787187+00:00_

{"result":"# 项目 cost-verify-agent-rl 概况\n\n## 实验状态 (183 个)\n\n- **exp010**: DONE (failed) — \n- **exp009**: DONE (failed) — \n- **exp008**: PREPARING (killed) — \n- **exp007**: DONE (failed) — \n- **exp007_dryrun**: PREPARING — \n- **exp003**: DONE (failed) — \n- **exp005**: PREPARING — \n- **exp_003**: PREPARING (failed) — \n- **exp_003_dryrun**: PREPARING (failed) — \n- **exp_003_dryrun2**: PREPARING (failed) — \n- **exp003_dryrun3**: PREPARING (failed) — \n- **exp_003_dryrun3**: PREPARING (failed) — \n- **exp_002**: DONE (failed) — \n- **exp_001b**: DONE (failed) — \n- **exp_001**: DONE (failed) — \n\n## 最新报告\n&lt;!-- AUTO-FACTS-BEGIN (generated 2026-05-23T01:08:36Z; do not edit — regenerated by auto_build_report_facts) -->\n## 📊 当前状态（auto-derived from registry）\n\n**总计**: 180 个实验 — ANALYZING 1, DONE 147, PREPARING 32\n**DONE 分布**: failed 62, killed 20, negative 23, success 42\n\n### 💾 磁盘余量\n- **bjb1-17606**:\n  - `/init`: 150M/150M 可用（已用 0%）\n  - `/autodl-pub/data`: 5.7T/10T 可用（已用 44%）\n  - `/usr/bin/nvidia-smi`: 817G/879G 可用（已用 3%）\n- **westd-47453**:\n  - `/autodl-pub`: 5.3T/7.3T 可用（已用 24%）\n  - `/init`: 150M/150M 可用（已用 1%）\n  - `/usr/bin/nvidia-smi`: 813G/879G 可用（已用 3%）\n\n### 🏃 RUNNING\n_（无）_\n\n### 📌 最近完成 (top 5)\n- `exp029_seed7_high_kl_step7_ood_v2` [failed] — 2026-05-23T00:28:57\n- `exp029_seed7_high_kl_step5_ood_v2` [failed] — 2026-05-23T00:28:55\n- `exp029_seed100_resume_step10` [success] — 2026-05-23T00:17:50\n- `exp029_seed7_ood_precollapse` [killed] — 2026-05-22T22:33:47\n- `exp029_seed300_step5_ood_eval_v4` [success] — 2026-05-22T22:26:20\n\n### 🔴 最近失败原因 (top 3)\n- `exp029_seed7_high_kl_step7_ood_v2`: _(no failure_reason — pre-2026-04-24 entry)_\n- `exp029_seed7_high_kl_step5_ood_v2`: _(no failure_reason — pre-2026-04-24 entry)_\n- `exp029_seed7_ood_precollapse`: _(no failure_reason — pre-2026-04-24 entry)_\n\n&lt;!-- AUTO-FACTS-END -->\n\n---\n\n# Handover — 2026-05-23\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|
…[truncated 1681 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1405
}
```

</details>

---


### Tool call

_source line 170 · 2026-05-23T09:02:28.787765+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 171 · 2026-05-23T09:02:29.842622+00:00_

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
12	\usepackage{amsmath}
13	\usepackage{amssymb}
14	\usepackage{amsthm}
15	\usepackage{enumitem}
16	
17	\title{Sign Misattribution in Step-Independent Agent RL:\\Dual Mechanism Diagnosis and Episode-Level Fix}
18	
19	\author{Anonymous}
20	
21	\begin{document}
22	\maketitle
23	
24	\begin{abstract}
25	Multi-turn agent reinforcement learning requires credit assignment across long interaction trajectories, yet current frameworks default to step-independent windowing that decomposes trajectories into independently optimized windows. This introduces a structural credit assignment pathology driven by two mechanisms: \textit{policy information loss}, which truncates context and imposes a constant performance ceiling, and \textit{advantage sign misattribution}, which causes gradient updates to reflect episode outcomes rather than local action quality, producing cumulative degradation. At $p{=}12.5\%$ with group size $K{=}8$, theory predicts 80.9\% of gradient updates for locally correct actions carry incorrect sign under binary reward; empirical measurement under penalty reward yields a 52\% credit agreement rate, indistinguishable from random chance. A $2{\times}2$ factorial separates the mechanisms: eliminating sign misattribution converts catastrophic collapse into bounded learning; removing information loss enables generalization. Episode-level Group Relative Policy Optimization (GRPO), treating the full trajectory as a single optimization sample, resolves both mechanisms. A systematic 11-seed evaluation reveals that stable training is necessary but not sufficient: 73\% of seeds avoid collapse, but only 36\% achieve statistically significant out-of-distribution (OOD) generalization ($p{<}0.01$; 24--31\% OOD vs.\ 6.7\% supervised fine-
…[truncated 1360 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "Read",
  "elapsed_ms": 1054
}
```

</details>

---


### Tool call

_source line 172 · 2026-05-23T09:02:29.843117+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 ARR call for papers submission deadline 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 ARR call for papers submission deadline 2026"
  }
}
```

</details>

---


### Tool call

_source line 173 · 2026-05-23T09:02:30.044313+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "cost-verify-agent-rl",
  "file": "artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "cost-verify-agent-rl",
    "file": "artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 174 · 2026-05-23T09:02:35.264544+00:00_

Web search results for query: "EMNLP 2026 ARR call for papers submission deadline 2026"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"EMNLP 2026 Call for Papers — Official Deadlines & Important Dates | PaperPilot","url":"https://www.getpaperpilot.com/deadlines/emnlp-2026.html"},{"title":"AI Conference Deadlines - Jie Cao | Dialogue, NLP, ML","url":"https://mlciv.com/ai-deadlines/"}]

Based on the search results, here's the information about EMNLP 2026 ARR call for papers submission deadline:

## EMNLP 2026 ARR Subm
…[truncated 751 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "WebSearch",
  "elapsed_ms": 5421
}
```

</details>

---


### Tool result

_source line 175 · 2026-05-23T09:02:35.265040+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'mistakes.yaml', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'artifacts/review_issues.yaml'\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 5220
}
```

</details>

---


### Tool call

_source line 176 · 2026-05-23T09:02:46.254926+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 177 · 2026-05-23T09:02:46.707151+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Reinforcement learning from sparse terminal reward has emerged as a promising paradigm for training LLM agents on multi-turn interactive tasks spanning 30--50 interaction steps~\cite{kim2025reflact,digiRL2024,wang2022scienceworld}. Group Relative Policy Optimization (GRPO)~\cite{shao2024deepseekmath}, with its critic-free design, has become the algorithm of choice. Yet a gap persists between the promise of RL-driven agent improvement and the reality of training outcomes: recent agent RL systems~\cite{ragen2025,selfguide2026,spear2025,feng2025gigpo} share a common, unscrutinized implementation pattern---decomposing trajectories into fixed-size windows, each optimized independently---and frequently report training instability without diagnosing its root cause.
5	
6	We show this \textit{step-independent} default introduces a fundamental credit assignment pathology. Step-independent training partitions trajectories into non-overlapping $h$-step windows, each optimized via GRPO. This produces a two-phase collapse: task success drops to 0\% while action validity initially remains high, then continued training destroys even basic formatting. Standard remedies---dense reward shaping, discount tuning---fail. Concurrent methods that improve per-step credit quality (GiGPO~\cite{feng2025gigpo}, GAGPO~\cite{gagpo2026}, Turn-PPO~\cite{turnppo2026}) address symptoms but not the structural root cause: the windowing itself.
7	
8	We trace the collapse to two mechanisms at different layers. \textit{\textbf{Policy information loss}} (M1) operates at the inference layer: each window lacks access to earlier observations, imposing a constant performance ceiling. \textit{\textbf{Advantage sign misattribution}} (M2) operates at the training layer: under binary reward, the advantage sign reflects episode success rather than local action quality. At $p{=}12.5\%$ with $K{=}8$, Proposition~2 predicts 80.9\% of gradient updates for locally
…[truncated 1867 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 178 · 2026-05-23T09:02:46.707613+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 179 · 2026-05-23T09:02:47.195779+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Problem Formulation and GRPO}
5	\label{sec:problem_formulation}
6	
7	We model the multi-turn agent as a partially observable Markov decision process (POMDP) where the policy $\pi_\phi(a_t \mid h_t)$ generates actions conditioned on interaction history $h_t = (o_1, a_1, \ldots, o_t)$. Episodes of $T$ steps terminate with binary reward $R \in \{0, r_+\}$. GRPO~\cite{shao2024deepseekmath} samples $K$ rollouts per task and computes group-relative advantages:
8	\begin{align}
9	\hat{A}_k &= \frac{R_k - \mu}{\sigma + \epsilon}, \notag \\
10	\mu &= \frac{1}{K}\sum_{j=1}^K R_j, \quad \sigma = \sqrt{\frac{1}{K}\sum_{j=1}^K (R_j - \mu)^2}
11	\label{eq:grpo_advantage}
12	\end{align}
13	GRPO is episode-level by design: each rollout receives one return and one advantage, with no inherent temporal discounting.
14	
15	\subsection{Step-Independent Windowing}
16	\label{sec:step_independent}
17	
18	Agent RL frameworks must reconcile GRPO's episode-level design with the memory constraints of long trajectories. RAGEN~\cite{ragen2025} introduces \textbf{step-independent training}: the trajectory is partitioned into non-overlapping $h$-step windows, each receiving a discounted return:
19	\begin{equation}
20	R_k = \gamma^{(N - k)} \cdot R_{\text{episode}}
21	\label{eq:step_return}
22	\end{equation}
23	where $N = \lceil T/h \rceil$ is the number of windows. Each window is optimized as an independent GRPO sample. This reduces sequence length from $O(T)$ to $O(h)$ and multiplies the effective batch size, but structurally alters credit assignment.
24	
25	\subsection{Dual Mechanism Analysis}
26	\label{sec:dual_mechanism}
27	
28	Two mechanisms jointly cause training failure under step-independent optimization.
29	
30	\subsubsection{Mechanism 1: Policy Information Loss}
31	\label{sec:m1_information_loss}
32	
33	Step-independent training truncates context at both inference and training time. The policy $\pi_\phi(a_t \mid h_{\text{window}_k})
…[truncated 2757 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "Read",
  "elapsed_ms": 488
}
```

</details>

---


### Tool call

_source line 180 · 2026-05-23T09:02:47.196129+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/theoretical_analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/theoretical_analysis.tex"
  }
}
```

</details>

---


### Tool result

_source line 181 · 2026-05-23T09:02:47.641455+00:00_

1	\section{Theoretical Analysis}
2	\label{sec:theory}
3	
4	Sign misattribution is the more fundamental failure mechanism because it causes active divergence, not merely slow convergence. We derive the probability of incorrect gradient direction below; full proofs appear in Appendix~\ref{app:theory_full}.
5	
6	\textbf{Definition 1} (Locally correct action). \textit{An action $a_t$ is \textbf{locally correct} if it would receive positive advantage under an oracle that observes the full episode history $h_t$ and has access to the true action-value function. Equivalently, window $k$ contains locally correct actions if replacing them (holding all other windows fixed) would decrease the probability of episode success.}
7	
8	\textbf{Proposition 1.} \textit{Under step-independent training with binary episode reward $R_{\text{episode}} \in \{0, r_+\}$, the probability that window $k$'s advantage $\hat{A}_k$ has the correct sign (aligned with local action quality) approaches the base success rate $p$ as the number of rollouts $K$ per group increases.}
9	
10	\textit{Proof sketch.} In a failed episode ($R_{\text{episode}} = 0$), all windows receive $R_k = 0$. If any rollout in the group succeeded, $\mu > 0$, so every window in the failed episode receives $\hat{A}_k < 0$---including windows with locally correct actions. The probability of receiving the wrong sign in a failed episode is $1 - (1-p)^{K-1}$ (at least one group member succeeded). As $K$ grows, this approaches $1-p$, and the overall probability of correct sign approaches $p$. \hfill$\square$
11	
12	The key distinction is temporal. Information loss (M1) imposes a constant ceiling determined by $h$; sign misattribution (M2) is cumulative---each wrong-sign gradient step erodes policy competence below that ceiling. A wrong-sign gradient moves the optimizer \textit{away} from good policies; a reduced-magnitude gradient from discounting ($\gamma^{(N-k)}$) still points toward good policies. Sign errors produce active diverge
…[truncated 4041 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "Read",
  "elapsed_ms": 445
}
```

</details>

---


### Tool call

_source line 182 · 2026-05-23T09:02:47.641870+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 183 · 2026-05-23T09:02:48.144083+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	Step-independent training collapses while episode-level training succeeds; a factorial design separates the two mechanisms; and window size $h$ modulates severity.
5	
6	\subsection{Setup}
7	\label{sec:setup}
8	
9	We evaluate on ALFWorld~\cite{shridhar2021alfworld}, a text-based household environment with six task types requiring sequential reasoning over up to 50 steps. Reward is binary: $R \in \{0, r_+\}$. The base policy is Qwen3-1.7B fine-tuned on 2{,}546 expert demonstrations (SFT baseline: 12.5\% in-distribution, 0\% pre-SFT). At $p{=}0.125$ with $K{=}8$, Proposition~2 predicts ${\sim}80.9\%$ of gradient updates for locally correct windows carry incorrect sign. All conditions use RAGEN~\cite{ragen2025} (v0.1, accessed May 2026)\footnote{Code available at \url{https://github.com/RAGEN-AI/RAGEN}.} with GRPO~\cite{shao2024deepseekmath} ($K{=}8$, lr$=10^{-6}$, $\beta{=}0.01$, $\gamma{=}0.95$, 15 steps; full hyperparameters in Appendix~\ref{app:hyperparameters}). We report success rate on a 134-task OOD set (primary) and 32-task in-distribution set (secondary). Seed counts are noted per condition.
10	
11	\subsection{Factorial Mechanism Separation}
12	\label{sec:factorial_experiments}
13	
14	We implement the $2 \times 2$ factorial (Section~\ref{sec:factorial_design}): \textbf{Cell~A} (both mechanisms active; $h{=}2$, step-level advantage), \textbf{Cell~B} (M1 only; $h{=}2$, episode-level advantage), and \textbf{Cell~D} (neither; full trajectory, episode-level advantage). Two seeds each. The fourth cell---\textbf{Cell~C} (full observation, step-level advantage)---would isolate M2 without M1; we predict partial improvement over Cell~A, since removing information loss enables gradient alignment but step-level advantage may still introduce noise. We attempted this configuration but encountered persistent training instability (Appendix~\ref{app:cell_c}).
15	
16	\subsection{Results}
17	\label{sec:results}
18	
19	Cell~A
…[truncated 10751 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 184 · 2026-05-23T09:02:48.144424+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 185 · 2026-05-23T09:02:48.596393+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{RL for multi-turn LLM agents.}
5	Policy gradient methods---PPO~\cite{schulman2017ppo}, GRPO~\cite{shao2024deepseekmath}, DPO~\cite{rafailov2023dpo}---underpin RLHF~\cite{ouyang2022instructgpt} and have been extended to multi-turn agents~\cite{yao2023react} through step-independent windowing~\cite{ragen2025}. Subsequent work improves algorithms (GiGPO~\cite{feng2025gigpo}), reward design (Self-Guide~\cite{selfguide2026}), or training pipelines (SPEAR~\cite{spear2025}, DigiRL~\cite{digiRL2024}), but all share a common assumption: trajectory decomposition into fixed windows is benign. We show this assumption is false---the windowing introduces a structural credit assignment pathology that no algorithmic improvement within the paradigm can fix.
6	
7	\paragraph{Credit assignment in reinforcement learning.}
8	TD($\lambda$)~\cite{sutton1988td}, GAE~\cite{schulman2016gae}, and TRPO~\cite{schulman2015trpo} interpolate between bootstrapping and Monte Carlo returns; REINFORCE~\cite{williams1992reinforce} uses full episode returns. Reward shaping~\cite{ng1999shaping} and hindsight experience replay~\cite{andrychowicz2017her} address sparse reward in classical RL; counterfactual baselines~\cite{foerster2018coma} handle team reward credit assignment. Process reward models~\cite{lightman2024lets,wang2024mathshepherd} provide step-level supervision for reasoning tasks. In the low-success-rate regime ($p < 0.2$) typical of agent tasks, the classical bias-variance tradeoff breaks down: Proposition~2 shows sign errors under windowing grow as $1{-}p$, dominating any variance reduction that windowing provides.
9	
10	\paragraph{Credit assignment and sign misattribution evidence.}
11	Several independent studies corroborate our diagnosis. IRC~\cite{irc2026} reports per-turn advantages frequently disagree in sign with outcome advantages. MC-GRPO~\cite{mcgrpo2025} measures a 5\% sign-flip rate. GRPO-$\lambda$~\cite{grpolambd
…[truncated 1431 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 186 · 2026-05-23T09:02:48.597493+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 187 · 2026-05-23T09:02:49.500750+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Generality and mechanism interaction.}
5	Sign misattribution arises whenever three structural properties co-occur: (a) step-level windowing, (b) sparse binary reward, and (c) group-relative normalization. Under these conditions, the advantage sign collapses to a proxy for episode outcome regardless of local quality, and severity scales with task difficulty ($P(\text{correct} \mid \text{update}) \to p$). M1 and M2 interact in a vicious cycle: M1 lowers $p$ by preventing multi-step strategies, increasing wrong-sign updates under M2, which further degrades $p$---explaining why step-independent training produces active collapse rather than slow convergence.
6	
7	\paragraph{Why step-independent became the default.}
8	Six contributing factors, from context length constraints to framework design inertia, are detailed in Appendix~\ref{app:why_defaults}.
9	
10	\paragraph{Seed-dependent OOD generalization.}
11	The multi-seed evaluation (Section~\ref{sec:seed_variability}) reveals a bimodal distribution: a stagnant cluster (10--16\% OOD, NS vs.\ SFT) and a generalized cluster (25--31\%, $p{<}0.001$). Training duration does not explain the gap (seed100: $+$1.50pp from step~5 to~10; seed5: 25.37\% at step~10), pointing to early training dynamics or initialization sensitivity. Identifying this mechanism is an important open question.
12	
13	\paragraph{Practitioner guidance.}
14	Use episode-level credit when the full episode fits in context; otherwise use the largest feasible $h$ ($h{\geq}20$; $h{\leq}10$ collapses). Finer-grained methods (Turn-PPO, GAGPO) should be applied only after establishing an episode-level baseline, as they assume correct gradient direction.
15	
16	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "Read",
  "elapsed_ms": 903
}
```

</details>

---


### Tool call

_source line 188 · 2026-05-23T09:02:49.501097+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 189 · 2026-05-23T09:02:50.003079+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	Step-independent training in multi-turn agent RL fails through two mechanisms: policy information loss imposes a performance ceiling, while advantage sign misattribution causes cumulative degradation: at $p{=}12.5\%$ with $K{=}8$, Proposition~2 predicts ${\sim}$80.9\% incorrect-sign updates under binary reward (52\% measured under penalty reward, consistent with near-random credit assignment). A $2{\times}2$ factorial separates the mechanisms; episode-level GRPO resolves both (17.2\% mean OOD at 1.7B; preliminary single-seed 8B evidence shows 90.3\% OOD). A systematic 11-seed evaluation reveals that stable training is necessary but not sufficient: 73\% avoid collapse, but only 36\% generalize ($p{<}0.01$). The central insight---sign errors are more destructive than magnitude imprecision---applies to any agent RL method combining step-level windowing, sparse binary reward, and group-relative normalization.
5	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "Read",
  "elapsed_ms": 501
}
```

</details>

---


### Tool call

_source line 190 · 2026-05-23T09:02:50.003514+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 191 · 2026-05-23T09:02:50.505846+00:00_

1	\appendix
2	
3	\section{Theoretical Analysis: Full Derivations}
4	\label{app:theory_full}
5	
6	\subsection{Why Sign Misattribution is the Core Mechanism}
7	\label{app:sign_fundamental}
8	
9	The two mechanisms identified in Section~\ref{sec:dual_mechanism} operate at different layers and produce qualitatively different failures. Policy information loss (Mechanism 1) operates at the inference layer, restricting the observable context and establishing a structural performance ceiling that is constant across training. Sign misattribution (Mechanism 2) operates at the training layer, corrupting gradient directions and progressively degrading performance below this ceiling.
10	
11	\textit{Proof of Proposition 1.} Define ``correct sign'' as follows: for a window containing locally beneficial actions, the correct sign of $\hat{A}_k$ is positive (reinforcement); for a window containing locally detrimental actions, the correct sign is negative (suppression). Under binary reward, the return for window $k$ is $R_k = \gamma^{(N-k)} \cdot R_{\text{episode}}$ (Equation~\ref{eq:step_return}). In a failed episode ($R_{\text{episode}} = 0$), all windows receive $R_k = 0$ regardless of their local action quality. If the group contains at least one successful rollout, the group mean $\mu > 0$, and all windows in the failed episode receive negative advantages after normalization via Equation~\ref{eq:grpo_advantage}. This includes windows where the agent took locally correct actions. Now consider a window with good local actions. In a successful episode (probability $p$), the window receives positive $\hat{A}_k$, which is the correct sign. In a failed episode (probability $1 - p$), the window receives negative $\hat{A}_k$ whenever $\mu > 0$, which is the wrong sign. The probability that $\mu = 0$ (all $K$ rollouts in the group failed) is $(1-p)^K$, which shrinks exponentially with $K$. As $K$ grows, nearly every failed episode produces a non-zero group mean, and the window receives the
…[truncated 15608 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 192 · 2026-05-23T09:02:50.556496+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 193 · 2026-05-23T09:02:51.460942+00:00_

1	@inproceedings{shridhar2021alfworld,
2	  title     = {{ALFWorld}: Aligning Text and Embodied Environments for Interactive Learning},
3	  author    = {Shridhar, Mohit and Yuan, Xingdi and C\^{o}t\'{e}, Marc-Alexandre and Bisk, Yonatan and Trischler, Adam and Hausknecht, Matthew},
4	  booktitle = {International Conference on Learning Representations},
5	  year      = {2021},
6	}
7	
8	
9	@inproceedings{digiRL2024,
10	  title     = {{DigiRL}: Training In-The-Wild Device-Control Agents with Autonomous Reinforcement Learning},
11	  author    = {Bai, Hao and Zhou, Yifei and Cemri, Mert and Pan, Jiayi and Suhr, Alane and Levine, Sergey and Kumar, Aviral},
12	  booktitle = {Advances in Neural Information Processing Systems},
13	  year      = {2024},
14	}
15	
16	@inproceedings{feng2025gigpo,
17	  title     = {{GiGPO}: Group-in-Group Policy Optimization for {LLM} Agent Training},
18	  author    = {Feng, Lang and Xue, Zhenghai and Liu, Tingcong and An, Bo},
19	  booktitle = {Advances in Neural Information Processing Systems},
20	  year      = {2025},
21	}
22	
23	@inproceedings{kim2025reflact,
24	  title     = {{ReflAct}: World-Grounded Decision Making in {LLM} Agents via Goal-State Reflection},
25	  author    = {Kim, Jeonghye and Rhee, Sojeong and Kim, Minbeom and Kim, Dohyung and Lee, Sangmook and Sung, Youngchul and Jung, Kyomin},
26	  booktitle = {Proceedings of the Conference on Empirical Methods in Natural Language Processing},
27	  year      = {2025},
28	}
29	
30	
31	@article{ragen2025,
32	  title   = {{RAGEN}: Understanding Self-Evolution in {LLM} Agents via Multi-Turn Reinforcement Learning},
33	  author  = {Wang, Zihan and Wang, Kangrui and Wang, Qineng and Zhang, Pingyue and Li, Linjie and Yang, Zhengyuan and Jin, Xing and Yu, Kefan and Nguyen, Minh Nhat and Liu, Licheng and Gottlieb, Eli and Lu, Yiping and Cho, Kyunghyun and Wu, Jiajun and Li, Fei-Fei and Wang, Lijuan and Choi, Yejin and Li, Manling},
34	  journal = {arXiv preprint arXiv:2504.20073},
35	  year    =
…[truncated 10611 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "Read",
  "elapsed_ms": 904
}
```

</details>

---


### Tool call

_source line 194 · 2026-05-23T09:02:51.461294+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 author guidelines page limit formatting template anonymous review policy"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 author guidelines page limit formatting template anonymous review policy"
  }
}
```

</details>

---


### Tool call

_source line 195 · 2026-05-23T09:02:52.866750+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
  "description": "Check if review_issues.yaml exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
    "description": "Check if review_issues.yaml exists"
  }
}
```

</details>

---


### Tool result

_source line 196 · 2026-05-23T09:02:53.320114+00:00_

- id: W1
  summary: '"Locally correct actions" lacks formal definition'
  category: method
  severity: critical
  status: resolved
  first_raised_round: 1
  last_seen_round: 1
  mentions:
    - {round: 1, reviewers: [R1, R2], note: "Entire theoretical framework depends on this undefined concept"}
  action_items:
    - {round: 1, action: "Add formal definition in Section 3 + operationalize in Section 4.4", assigned_to: main_agent, status: done}
  resolution: "Definition 1 added in theoretical_analysis.tex; operationalized in experiments.tex Section 4.4"
  resolution_round: 1

- id: W2
  summary: "Theory (binary reward) vs experiment (binary+penalty) inconsistency; 80.9% vs 52% discrepancy"
  category: method
  severity: critical
  status: resolved
  first_raised_round: 1
  last_seen_round: 1
  mentions:
    - {round: 1, reviewers: [R1, R2], note: "Prop 2 predicts 19.1%, measured 52.07%. Intro/Conclusion use 80.9% but experiments show 52%"}
  action_items:
    - {round: 1, action: "Appendix: extend Remark with penalty analysis. Main text: unify 80.9% and 52% presentation in Intro/Conclusion", assigned_to: main_agent, status: done}
  resolution: "Penalty reward analysis added to appendix. Intro/Conclusion/Abstract all present 80.9% qualified with '(52% under penalty reward)'"
  resolution_round: 1

- id: W3
  summary: "10/20 citations use Anonymous authors — ARR compliance violation"
  category: format
  severity: critical
  status: resolved
  first_raised_round: 1
  last_seen_round: 1
  mentions:
    - {round: 1, reviewers: [R1, R2], note: "irc2026, grpolambda2025, oar2026, ragen2_2026, grpocollapse2025, gradientcoupling2025, turnppo2026, gagpo2026, mtgrpo2025, sweetrl2025"}
  action_items:
    - {round: 1, action: "Search real author names for all 10 entries, update references.bib", assigned_to: main_agent, status: done}
  resolution: "All 10 entries updated with real authors. 10 new references added (PPO, COMA, TRPO, etc). Total 33 citations, all verified."
  resolu
…[truncated 8127 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "Bash",
  "elapsed_ms": 453
}
```

</details>

---


### Tool call

_source line 197 · 2026-05-23T09:02:53.420919+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "cost-verify-agent-rl",
  "section": "external_review"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "cost-verify-agent-rl",
    "section": "external_review"
  }
}
```

</details>

---


### Tool result

_source line 198 · 2026-05-23T09:02:59.392360+00:00_

Web search results for query: "EMNLP 2026 author guidelines page limit formatting template anonymous review policy"

Links: [{"title":"EMNLP 2026 LaTeX Template | ACL Style Files & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/emnlp"},{"title":"Call for Papers: EMNLP 2026 Industry Track - EMNLP 2026","url":"https://2026.emnlp.org/calls/industry_track/"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"Information For Authors | Computational Linguistics","url":"https://submissions.cljournal.org/index.php/cljournal/information/authors"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"GitHub - acl-org/emnlp-2026: Repository for the EMNLP 2026 conference · GitHub","url":"https://github.com/acl-org/emnlp-2026"},{"title":"EMNLP: Empirical Methods in Natural Language Processing Template - ACM Conference","url":"https://scispace.com/formats/acm-conference/emnlp-empirical-methods-in-natural-language-processing/9660af2f47424125a400febdfef4f76f"},{"title":"EMNLP: Empirical Methods in Natural Language Processing 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=883"},{"title":"Authors Guidelines","url":"http://aclrollingreview.org/authors"},{"title":"EMNLP 2026 Conference | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FConference"}]

Based on the search results, here's the information about EMNLP 2026 author guidelines:

## Page Limits

The format is two-column with an 8-page limit for long papers and a 4-page limit for short papers.

## Formatting and Template

EMNLP uses the standard ACL style files, so the LaTeX template is identical to the one used for ACL, NAACL, and other *ACL conferences. EMNLP uses the ACL style files available at github.com/acl-org/acl-style-files.

## Mandatory Sections

The mandatory Limitations secti
…[truncated 729 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "WebSearch",
  "elapsed_ms": 7931
}
```

</details>

---


### Tool result

_source line 199 · 2026-05-23T09:02:59.894830+00:00_

{"result":"# 项目 cost-verify-agent-rl 概况\n\n## 实验状态 (183 个)\n\n- **exp010**: DONE (failed) — \n- **exp009**: DONE (failed) — \n- **exp008**: PREPARING (killed) — \n- **exp007**: DONE (failed) — \n- **exp007_dryrun**: PREPARING — \n- **exp003**: DONE (failed) — \n- **exp005**: PREPARING — \n- **exp_003**: PREPARING (failed) — \n- **exp_003_dryrun**: PREPARING (failed) — \n- **exp_003_dryrun2**: PREPARING (failed) — \n- **exp003_dryrun3**: PREPARING (failed) — \n- **exp_003_dryrun3**: PREPARING (failed) — \n- **exp_002**: DONE (failed) — \n- **exp_001b**: DONE (failed) — \n- **exp_001**: DONE (failed) — \n\n## 最新报告\n&lt;!-- AUTO-FACTS-BEGIN (generated 2026-05-23T01:08:36Z; do not edit — regenerated by auto_build_report_facts) -->\n## 📊 当前状态（auto-derived from registry）\n\n**总计**: 180 个实验 — ANALYZING 1, DONE 147, PREPARING 32\n**DONE 分布**: failed 62, killed 20, negative 23, success 42\n\n### 💾 磁盘余量\n- **bjb1-17606**:\n  - `/init`: 150M/150M 可用（已用 0%）\n  - `/autodl-pub/data`: 5.7T/10T 可用（已用 44%）\n  - `/usr/bin/nvidia-smi`: 817G/879G 可用（已用 3%）\n- **westd-47453**:\n  - `/autodl-pub`: 5.3T/7.3T 可用（已用 24%）\n  - `/init`: 150M/150M 可用（已用 1%）\n  - `/usr/bin/nvidia-smi`: 813G/879G 可用（已用 3%）\n\n### 🏃 RUNNING\n_（无）_\n\n### 📌 最近完成 (top 5)\n- `exp029_seed7_high_kl_step7_ood_v2` [failed] — 2026-05-23T00:28:57\n- `exp029_seed7_high_kl_step5_ood_v2` [failed] — 2026-05-23T00:28:55\n- `exp029_seed100_resume_step10` [success] — 2026-05-23T00:17:50\n- `exp029_seed7_ood_precollapse` [killed] — 2026-05-22T22:33:47\n- `exp029_seed300_step5_ood_eval_v4` [success] — 2026-05-22T22:26:20\n\n### 🔴 最近失败原因 (top 3)\n- `exp029_seed7_high_kl_step7_ood_v2`: _(no failure_reason — pre-2026-04-24 entry)_\n- `exp029_seed7_high_kl_step5_ood_v2`: _(no failure_reason — pre-2026-04-24 entry)_\n- `exp029_seed7_ood_precollapse`: _(no failure_reason — pre-2026-04-24 entry)_\n\n&lt;!-- AUTO-FACTS-END -->\n\n---\n\n# Handover — 2026-05-23\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|
…[truncated 1681 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 6473
}
```

</details>

---


### Tool call

_source line 200 · 2026-05-23T09:03:24.103971+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/review_round_2/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"PDF_NOT_FOUND\"",
  "description": "Check if submitted PDF exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/review_round_2/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"PDF_NOT_FOUND\"",
    "description": "Check if submitted PDF exists"
  }
}
```

</details>

---


### Tool result

_source line 201 · 2026-05-23T09:03:24.957303+00:00_

-rw-r--r-- 1 ubuntu ubuntu 408839 May 23 09:01 /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/review_round_2/submitted.pdf
PDF_EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "Bash",
  "elapsed_ms": 853
}
```

</details>

---


### Tool call

_source line 202 · 2026-05-23T09:03:25.208613+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/agent/config.yaml 2>/dev/null || cat /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/config.yaml 2>/dev/null || echo \"CONFIG_NOT_FOUND\"",
  "description": "Check project config for external review settings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/agent/config.yaml 2>/dev/null || cat /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/config.yaml 2>/dev/null || echo \"CONFIG_NOT_FOUND\"",
    "description": "Check project config for external review settings"
  }
}
```

</details>

---


### Tool result

_source line 203 · 2026-05-23T09:03:25.259285+00:00_

CONFIG_NOT_FOUND

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 204 · 2026-05-23T09:03:27.618498+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/config*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/config*.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl"
  }
}
```

</details>

---


### Tool result

_source line 205 · 2026-05-23T09:03:27.669148+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 206 · 2026-05-23T09:03:29.627215+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/config*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/config*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1"
  }
}
```

</details>

---


### Tool result

_source line 207 · 2026-05-23T09:03:29.677898+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 208 · 2026-05-23T09:03:31.987285+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_1 -maxdepth 3 -name \"*.yaml\" -o -name \"*.yml\" | head -20",
  "description": "Find YAML config files in project"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_1 -maxdepth 3 -name \"*.yaml\" -o -name \"*.yml\" | head -20",
    "description": "Find YAML config files in project"
  }
}
```

</details>

---


### Tool result

_source line 209 · 2026-05-23T09:03:32.088191+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_1/idea_generator/ideas.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_1/global/approvals.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_1/global/registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/dream_registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/writing_plan.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/paper_provenance.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/literature_map.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/constraints.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/mistakes.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/decisions.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/experiment_plan.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/error_diag_dpo_recovery/registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/error_diag_dpo_recovery/decisions.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_1/config/crons.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_1/config/approvals.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_1/config/backend.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_1/config/projects/cost-verify-agent-rl.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_1/config/projects/error_diag_dpo_recovery.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_1/config/venue_rules/corl-2026.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 210 · 2026-05-23T09:03:34.647923+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/config/projects/cost-verify-agent-rl.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/config/projects/cost-verify-agent-rl.yaml"
  }
}
```

</details>

---


### Tool result

_source line 211 · 2026-05-23T09:03:34.698628+00:00_

1	execution:
2	  gpu_ids:
3	    bjb1-17606:
4	    - cuda:0
5	  project_path: /root/cost-verify-agent-rl
6	  servers:
7	  - account: root
8	    server: bjb1-17606
9	feishu:
10	  chat_id: oc_4ebf0fb2d0159caa355a1a855f5ac59f
11	  check_references: true
12	  operational_chat_id: oc_733b284b383121720ce3d07c5c4a6bb2
13	  review_mode: fresh
14	  review_paper_path: /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/main.tex
15	  review_paper_pdf_path: /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/review_round_2/submitted.pdf
16	  review_round: 2
17	  review_supplementary_paths: ''
18	  submission_chat_id: oc_648eaf83d2b24d445764257cf6a55525
19	project:
20	  created_at: '2026-05-13T17:31:30.051Z'
21	  description: 'Verify When It Matters: Behaviorally-Grounded Selective Verification
22	    for Interactive Agents'
23	  name: cost-verify-agent-rl
24	  phase: research
25	  source_idea_id: idea_009
26	venue: emnlp-2026
27	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 212 · 2026-05-23T09:04:04.139317+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "cost-verify-agent-rl",
  "review_chat_id": "oc_648eaf83d2b24d445764257cf6a55525"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "cost-verify-agent-rl",
    "review_chat_id": "oc_648eaf83d2b24d445764257cf6a55525"
  }
}
```

</details>

---


### Tool result

_source line 213 · 2026-05-23T09:04:27.189924+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 23050
}
```

</details>

---


### Tool call

_source line 214 · 2026-05-23T09:04:27.345711+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "project": "cost-verify-agent-rl",
  "reviewer_id": "1",
  "round_number": "1",
  "text": "你是 Reviewer 1，负责**方法严谨性**审查。\n\n## Venue 信息\n- **目标会议**: EMNLP 2026（通过 ARR 统一审稿）\n- **投稿截止**: 2026-05-25（ARR May cycle）\n- **页数限制**: 正文 8 页（long paper），参考文献不限页数，Limitations 不计入页数限制\n- **模板**: ACL style (`\\usepackage[review]{acl}`)\n- **匿名规则**: Double-blind\n- **评分标准**: Overall Assessment 1-5 分制（5=Consider for Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit）\n\n## 论文文件\n- LaTeX 源码: `/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/main.tex`（含 `\\input{introduction}`, `\\input{method}`, `\\input{theoretical_analysis}`, `\\input{experiments}`, `\\input{related_work}`, `\\input{discussion}`, `\\input{conclusion}`, `\\input{appendix}`）\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/review_round_2/submitted.pdf`\n\n## 你的审查侧重\n\n### 1. 理论分析严谨性\n- Proposition 1 和 Proposition 2 的证明是否完备？假设是否合理？\n- Definition 1（locally correct action）的形式化是否充分？是否可操作？\n- 理论预测（binary reward 下 80.9% incorrect sign）与实验测量（penalty reward 下 52% credit agreement）之间的差距，解释是否令人信服？\n- Eq. 6（cumulative divergence）的推导是否严谨？\"simplifying assumption that correct and incorrect gradient components have comparable magnitude\"是否过强？\n\n### 2. 实验设计与统计\n- 2×2 factorial 设计是否严谨？Cell C 缺失（6 次尝试均 KL 崩溃）对结论的影响？\n- 11-seed 评估的统计功效是否充足？Fisher exact test 的使用是否恰当？\n- 8B 和 ScienceWorld 结果均为单 seed——声明是否与统计证据匹配？\n- Window-size sweep 基于单 seed 的 cliff claim 是否可靠？\n- Table 1 的报告标准是否一致（best seed / best checkpoint / mean 混用）？\n- REINFORCE++ 仅训练 15 步是否公平？\n\n### 3. 可复现性\n- 超参数报告是否完整？\n- 代码/数据/checkpoint 可用性？\n- SFT baseline 的细节（2,546 demonstrations 来源、训练设置）？\n\n### 4. 数学正确性\n- 检查所有公式推导的正确性\n- 检查数字一致性（abstract/intro/experiments/conclusion 中的数字是否匹配）\n\n请按 ARR 审稿格式输出：Summary → Strengths → Weaknesses（分 Must-Fix / Should-Fix / Minor） → Questions → Overall Assessment（含评分和置信度）。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "project": "cost-verify-agent-rl",
    "reviewer_id": "1",
    "round_number": "1",
    "text": "你是 Reviewer 1，负责**方法严谨性**审查。\n\n## Venue 信息\n- **目标会议**: EMNLP 2026（通过 ARR 统一审稿）\n- **投稿截止**: 2026-05-25（ARR May cycle）\n- **页数限制**: 正文 8 页（long paper），参考文献不限页数，Limitations 不计入页数限制\n- **模板**: ACL style (`\\usepackage[review]{acl}`)\n- **匿名规则**: Double-blind\n- **评分标准**: Overall Assessment 1-5 分制（5=Consider for Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit）\n\n## 论文文件\n- LaTeX 源码: `/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/main.tex`（含 `\\input{introduction}`, `\\input{method}`, `\\input{theoretical_analysis}`, `\\input{experiments}`, `\\input{related_work}`, `\\input{discussion}`, `\\input{conclusion}`, `\\input{appendix}`）\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/review_round_2/submitted.pdf`\n\n## 你的审查侧重\n\n### 1. 理论分析严谨性\n- Proposition 1 和 Proposition 2 的证明是否完备？假设是否合理？\n- Definition 1（locally correct action）的形式化是否充分？是否可操作？\n- 理论预测（binary reward 下 80.9% incorrect sign）与实验测量（penalty reward 下 52% credit agreement）之间的差距，解释是否令人信服？\n- Eq. 6（cumulative divergence）的推导是否严谨？\"simplifying assumption that correct and incorrect gradient components have comparable magnitude\"是否过强？\n\n### 2. 实验设计与统计\n- 2×2 factorial 设计是否严谨？Cell C 缺失（6 次尝试均 KL 崩溃）对结论的影响？\n- 11-seed 评估的统计功效是否充足？Fisher exact test 的使用是否恰当？\n- 8B 和 ScienceWorld 结果均为单 seed——声明是否与统计证据匹配？\n- Window-size sweep 基于单 seed 的 cliff claim 是否可靠？\n- Table 1 的报告标准是否一致（best seed / best checkpoint / mean 混用）？\n- REINFORCE++ 仅训练 15 步是否公平？\n\n### 3. 可复现性\n- 超参数报告是否完整？\n- 代码/数据/checkpoint 可用性？\n- SFT baseline 的细节（2,546 demonstrations 来源、训练设置）？\n\n### 4. 数学正确性\n- 检查所有公式推导的正确性\n- 检查数字一致性（abstract/intro/experiments/conclusion 中的数字是否匹配）\n\n请按 ARR 审稿格式输出：Summary → Strengths → Weaknesses（分 Must-Fix / Should-Fix / Minor） → Questions → Overall Assessment（含评分和置信度）。"
  }
}
```

</details>

---


### Tool result

_source line 215 · 2026-05-23T09:04:46.742922+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_648eaf83d2b24d445764257cf6a55525:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 19397
}
```

</details>

---


### Tool call

_source line 216 · 2026-05-23T09:04:46.843702+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "project": "cost-verify-agent-rl",
  "reviewer_id": "2",
  "round_number": "1",
  "text": "你是 Reviewer 2，负责**新颖性与完整性**审查。\n\n## Venue 信息\n- **目标会议**: EMNLP 2026（通过 ARR 统一审稿）\n- **投稿截止**: 2026-05-25（ARR May cycle）\n- **页数限制**: 正文 8 页（long paper），参考文献不限页数，Limitations 不计入页数限制\n- **模板**: ACL style (`\\usepackage[review]{acl}`)\n- **匿名规则**: Double-blind\n- **评分标准**: Overall Assessment 1-5 分制（5=Consider for Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit）\n\n## 论文文件\n- LaTeX 源码: `/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/main.tex`（含 `\\input{introduction}`, `\\input{method}`, `\\input{theoretical_analysis}`, `\\input{experiments}`, `\\input{related_work}`, `\\input{discussion}`, `\\input{conclusion}`, `\\input{appendix}`）\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/review_round_2/submitted.pdf`\n\n## 你的审查侧重\n\n### 1. 新颖性评估\n- 核心贡献是\"诊断性\"的（formalize + empirically validate sign misattribution），fix 是回归 GRPO 原始设计。这在 EMNLP Findings 级别是否足够？\n- 与已有相关工作（IRC, MC-GRPO, GRPO-λ, OAR, Turn-PPO, GAGPO, MT-GRPO, SWEET-RL）的区分是否清晰？\n- 是否有遗漏的重要相关工作？特别关注 2025-2026 年 agent RL / credit assignment 领域的最新论文\n- \"step-independent training is broken\" 的 insight 是否足够 non-trivial？\n\n### 2. 写作质量\n- 论文的叙事结构是否清晰？Introduction 的问题引出是否有效？\n- Abstract 是否准确概括了论文贡献？是否有 overclaim？\n- Contribution list 是否与正文内容匹配？\n- 术语使用是否一致？（如 \"step-independent\" vs \"window-level\" vs \"turn-level\"）\n- 论文长度是否在 8 页限制内？（检查 PDF）\n\n### 3. 格式合规\n- 引用格式是否符合 ACL/ARR 要求？\n- 所有引用是否有完整的 author、title、venue/journal、year？\n- 是否有 Anonymous / arXiv-only 引用？（ARR 允许引用 arXiv preprints，但必须有完整作者信息）\n- Figure/Table 标注是否完整？\n- Limitations section 是否存在且内容充分？（EMNLP 要求：正文中，结论之后，覆盖 ~3 个点即可）\n- 是否泄露作者身份？（检查 self-citation、acknowledgment、代码 URL 等）\n\n### 4. Related Work 完整性\n- 用 web_search 搜索 2025-2026 年 multi-turn agent RL 和 credit assignment 的最新论文，检查是否有重要遗漏\n- 特别关注：是否有直接竞争性工作（同时期诊断同一问题的论文）\n\n### 5. Limitations 与 Ethics\n- Limitations section 是否充分覆盖关键局限？\n- 是否存在潜在的 ethical concerns？\n\n请按 ARR 审稿格式输出：Summary → Strengths → Weaknesses（分 Must-Fix / Should-Fix / Minor） → Questions → Missing References → Overall Assessment（含评分和置信度）。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "project": "cost-verify-agent-rl",
    "reviewer_id": "2",
    "round_number": "1",
    "text": "你是 Reviewer 2，负责**新颖性与完整性**审查。\n\n## Venue 信息\n- **目标会议**: EMNLP 2026（通过 ARR 统一审稿）\n- **投稿截止**: 2026-05-25（ARR May cycle）\n- **页数限制**: 正文 8 页（long paper），参考文献不限页数，Limitations 不计入页数限制\n- **模板**: ACL style (`\\usepackage[review]{acl}`)\n- **匿名规则**: Double-blind\n- **评分标准**: Overall Assessment 1-5 分制（5=Consider for Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit）\n\n## 论文文件\n- LaTeX 源码: `/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/main.tex`（含 `\\input{introduction}`, `\\input{method}`, `\\input{theoretical_analysis}`, `\\input{experiments}`, `\\input{related_work}`, `\\input{discussion}`, `\\input{conclusion}`, `\\input{appendix}`）\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/review_round_2/submitted.pdf`\n\n## 你的审查侧重\n\n### 1. 新颖性评估\n- 核心贡献是\"诊断性\"的（formalize + empirically validate sign misattribution），fix 是回归 GRPO 原始设计。这在 EMNLP Findings 级别是否足够？\n- 与已有相关工作（IRC, MC-GRPO, GRPO-λ, OAR, Turn-PPO, GAGPO, MT-GRPO, SWEET-RL）的区分是否清晰？\n- 是否有遗漏的重要相关工作？特别关注 2025-2026 年 agent RL / credit assignment 领域的最新论文\n- \"step-independent training is broken\" 的 insight 是否足够 non-trivial？\n\n### 2. 写作质量\n- 论文的叙事结构是否清晰？Introduction 的问题引出是否有效？\n- Abstract 是否准确概括了论文贡献？是否有 overclaim？\n- Contribution list 是否与正文内容匹配？\n- 术语使用是否一致？（如 \"step-independent\" vs \"window-level\" vs \"turn-level\"）\n- 论文长度是否在 8 页限制内？（检查 PDF）\n\n### 3. 格式合规\n- 引用格式是否符合 ACL/ARR 要求？\n- 所有引用是否有完整的 author、title、venue/journal、year？\n- 是否有 Anonymous / arXiv-only 引用？（ARR 允许引用 arXiv preprints，但必须有完整作者信息）\n- Figure/Table 标注是否完整？\n- Limitations section 是否存在且内容充分？（EMNLP 要求：正文中，结论之后，覆盖 ~3 个点即可）\n- 是否泄露作者身份？（检查 self-citation、acknowledgment、代码 URL 等）\n\n### 4. Related Work 完整性\n- 用 web_search 搜索 2025-2026 年 multi-turn agent RL 和 credit assignment 的最新论文，检查是否有重要遗漏\n- 特别关注：是否有直接竞争性工作（同时期诊断同一问题的论文）\n\n### 5. Limitations 与 Ethics\n- Limitations section 是否充分覆盖关键局限？\n- 是否存在潜在的 ethical concerns？\n\n请按 ARR 审稿格式输出：Summary → Strengths → Weaknesses（分 Must-Fix / Should-Fix / Minor） → Questions → Missing References → Overall Assessment（含评分和置信度）。"
  }
}
```

</details>

---


### Tool result

_source line 217 · 2026-05-23T09:04:48.392461+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_648eaf83d2b24d445764257cf6a55525:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1548
}
```

</details>

---


### Assistant

_source line 218 · 2026-05-23T09:04:59.786364+00:00_

Round 2 审稿流程已启动。

**当前状态**：
- **Reviewer 1**（方法严谨性）：已派发，审稿中
- **Reviewer 2**（新颖性/完整性）：已派发，审稿中
- **视觉审查 Agent**：已派发，与 Reviewer 并行执行
- **外部审稿**：项目未配置，跳过
- **引用验证**：后台自动运行中

**Venue 确认**：
- EMNLP 2026 via ARR，deadline **2026-05-25**（距今 2 天）
- Long paper 8 页正文 + 无限参考文献
- Double-blind，ACL 模板
- 论文使用 `\usepackage[review]{acl}`，作者 "Anonymous"，格式初步合规

等待 Reviewer 返回初审结果后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director"
}
```

</details>

---


## Round 16

## Round 16

2 recorded events


### User

_source line 219 · 2026-05-23T09:10:06.822801+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1: 方法严谨性审查

## Summary

本文诊断了多轮 agent RL 中 step-independent windowing 的两个失败机制：(1) policy information loss（截断上下文导致性能上限）和 (2) advantage sign misattribution（梯度方向与局部动作质量脱钩）。作者通过 2×2 factorial 实验分离两个机制，提出回到 GRPO 原始的 episode-level 设计作为修复，并在 ALFWorld 上进行了 11-seed 评估和初步的跨规模（8B）/跨环境（ScienceWorld）验证。

论文的核心贡献是诊断性的而非方法性的——这既是优势（聚焦根因分析）也是限制（修复方案本身并不新颖）。理论分析的主要结论（Proposition 2）在 binary reward 假设下是正确的，但论文在 abstract/intro 中以 "80.9% incorrect sign" 作为标题数字，而实际实验（含 penalty reward）测得的是 52% credit agreement，理论与实验之间的 28.9pp 差距的解释仅在 Appendix 中展开，这对读者构成误导。实验设计存在多处统计功效不足的问题，特别是 factorial 仅 2 seeds、window-size cliff 和跨规模/跨环境验证均为 single seed。

---

## Strengths

**S1. 问题定位精准且有实际意义。** Step-independent windowing 是 RAGEN 等框架的默认配置，广泛使用但缺乏理论审视。论文将训练崩溃追溯到信用分配结构性缺陷而非超参数调优问题，对从业者有直接指导价值。

**S2. Proposition 2 的推导在 binary reward 假设下正确且优雅。** P(correct | update) = p / [1 − (1−p)^K] 的推导逻辑清晰（三种互斥情况的条件概率），数值验证一致（p=0.125, K=8 → 19.1%）。Figure 1 的可视化直观展示了 sign error 随任务难度恶化的趋势。

**S3. Factorial 设计的思路值得肯定。** 用 2×2 分离 observation scope 和 advantage granularity 的想法在概念上合理，A→B 和 B→D 的对比逻辑清晰。

**S4. 11-seed 评估揭示了有价值的现象。** Collapsed/Stagnant/Generalized 三类结果的发现是重要的实证贡献，response length inflation 作为 collapse 的伴随指标也有诊断价值。

**S5. 诚实的局限性讨论。** 论文在多处主动标注 single-seed 限制、Cell C 缺失、seed-dependent transfer 为 open question，这种学术诚实值得认可。

---

## Weaknesses

### Must-Fix（影响接收决定）

**N1 [critical] 理论预测与实验测量之间的 28.9pp 差距在主文中处理不当**

- 具体位置：Abstract (line "theory predicts 80.9%...empirical measurement...yields a 52% credit agreement rate"), Introduction (同样并列), Section 3 (Proposition 2 推导), Section 4.4 (实测 52.07%), Appendix A.2 (gap 解释)
- 问题：论文的标题数字是 Proposition 2 在 **binary reward** 假设下推导的 "80.9% incorrect sign"，但所有实验使用的是含 −0.1 invalid action penalty 的 **non-binary reward**。实际测量的 credit agreement rate 是 52.07%——与 50% random chance 基本无差别，但与理论预测的 19.1% correct sign 相差 33pp。论文将这个巨大差距的解释放在 Appendix A.2（"penalty-induced variance can occasionally produce positive Â_k for windows with valid actions"），但 Abstract 和 Introduction 都将两个数字简单并列呈现（"theory predicts 80.9%...52% credit agreement rate"），给读者造成两者互相支持的印象，实际上它们之间存在实质性矛盾。
- 为什么影响接收：如果 penalty reward 将理论预测的 80.9% incorrect sign 大幅修正到接近 random (52%)，那么 Proposition 2 的定量预测在实际使用的 reward 结构下不再适用。读者无法评估 sign misattribution 在 penalty reward 下的实际严重程度——52% agreement 虽然差，但远不如 80.9% incorrect 那么灾难性。
- 建议修改方向：(a) 在主文 Section 3 或 4.4 中明确讨论 binary vs. penalty reward 下的预测差异，而非仅放在 Appendix; (b) 要么推导 penalty reward 下的理论预测，要么将 Abstract/Intro 中的标题数字改为实验测量值 52%，将 80.9% 作为理论上界。

**N2 [critical] Eq. 6 累积发散论证依赖过强假设，结论超出前提支撑范围**

- 具体位置：Section 3, Eq. 6 及后续 "monotonic divergence" 声明
- 问题：Eq. 6 的推导显式假设 "correct and incorrect gradient components have comparable magnitude"（g+ 和 g− 量级相当），但在 GRPO 的 group normalization 下这个假设几乎必然不成立。考虑 p=0.125, K=8 的典型场景：一个成功 episode 的 window 在 group 中属于少数，其 advantage = (r+ − μ)/σ 会相当大（因为 μ 较小，r+ 远大于 μ）；而失败 episode 中的 window 的 advantage = (0 − μ)/σ 量级较小（μ 本身就小）。这意味着 correct-sign gradients 的量级可能系统性地大于 incorrect-sign gradients，部分补偿频率上的劣势。极端情况下，一个大的 correct gradient 可能抵消多个小的 incorrect gradients，使 "monotonic divergence" 结论不成立。
- 为什么影响接收：论文用 "monotonic divergence" 和 "explaining the two-phase collapse" 将 Eq. 6 的结论作为因果解释的关键环节。如果量级不可比，则 sign misattribution 的实际影响可能远小于理论预测，从 "active divergence" 降级为 "noisy convergence"——这从根本上改变了论文的叙事。
- 建议修改方向：(a) 分析 GRPO normalization 下 correct vs. incorrect gradients 的实际量级比（可以从实验日志中提取 advantage 分布）; (b) 如果无法证明量级可比，应将 Eq. 6 降级为 "worst-case analysis" 而非实际行为的描述; (c) 用 "net gradient direction" 的实证测量替代理论论证。

**N3 [critical] Factorial 设计有结构性缺陷：Cell C 缺失且种子数不足**

- 具体位置：Section 2.5, Section 4.2, Appendix C (Cell C attempt)
- 问题有两方面：
  - (a) **Cell C 缺失**：2×2 factorial 缺少 Cell C（full context + step-level advantage），无法独立隔离 M2 的效果。A→B 的对比只能说明 "在 M1 存在的条件下消除 M2 的效果"，不能证明 M2 独立于 M1 也会导致崩溃。Cell C 的 6 次尝试均因 KL 崩溃失败，论文将其归因于 "extreme advantage magnitudes at early window positions"，但这个归因本身就说明 step-level advantage 在 full context 下的行为可能与在 truncated context 下质性不同——这直接影响对 M2 机制的理解。
  - (b) **种子数不足**：每个 factorial condition 仅 2 seeds。论文自己的 11-seed 分析显示 27% collapse、36% stagnate、36% generalize。在如此高的 seed variability 下，2 seeds 可能恰好落入不同类别，产生误导性结论。Cell D 的 OOD 范围是 10.4%–23.9%（2.3x 差异），说明 2 seeds 远不足以稳定估计均值。
- 为什么影响接收：Factorial 分离是论文的第二个核心贡献（Contribution 2）。Cell C 缺失使得论文无法完成声称的 "empirical separation"；2 seeds 使得 factorial 结果的可靠性存疑。
- 建议修改方向：(a) 在主文中明确承认 factorial 实际上是 incomplete design（3/4 cells）而非 2×2; (b) 增加 factorial conditions 的种子数至少到 5; (c) 讨论 Cell C 失败对结论的具体影响——是否可能 M2 在 full context 下根本不是问题（因为 window normalization 在 full context 下行为不同）？

### Should-Fix（影响评分但不一票否决）

**W1 [warning] Definition 1 的操作化存在逻辑循环**

- 具体位置：Section 3 (Definition 1), Section 4.4 (operationalization)
- 问题：Definition 1 将 "locally correct action" 定义为 "在拥有完整历史和真实 Q 函数的 oracle 下会获得正 advantage 的动作"。但 Section 4.4 将其操作化为 "成功 episode 中所有 valid action 的 windows"。这个操作化恰好犯了论文所批评的错误——用 episode outcome 替代 local quality。一个成功 episode 中可能包含局部次优但不致命的动作（例如走了弯路但最终完成任务），这些 windows 在操作化定义下被标记为 "locally correct"，但在理论定义下未必如此。
- 建议：在 Section 4.4 明确讨论这个近似的局限性，说明它是上界估计（credit agreement rate 被高估），或提供样本分析支持操作化的合理性。

**W2 [warning] Window-size cliff 基于 single seed，统计可靠性不足**

- 具体位置：Section 4.3 (Window-size sweep), Figure 2b
- 问题：h=2, 5, 10, 20 的 sweep 结果来自单个 seed。论文称 h=10 到 h=20 之间存在 "credit assignment cliff"，但鉴于 11-seed 评估中观察到的高变异性，不同 seed 的 cliff 位置可能不同，甚至某些 seed 可能不存在 cliff。Section 4.3 末尾确实提到 "multi-seed verification is needed"，但这个声明与前文 "cliff" 的强烈措辞不匹配。
- 建议：弱化 "cliff" 的表述（改为 "preliminary observation"），或增加至少 3 seeds 的验证。

**W3 [warning] REINFORCE++ 仅训练 15 步，对比可能不公平**

- 具体位置：Table 1, Appendix C (REINFORCE++ description)
- 问题：REINFORCE++ 使用 per-token running-mean baseline（无 critic），训练 15 步后与 SFT baseline 持平（12.50%）。论文据此暗示 REINFORCE++ 无效。但 (a) REINFORCE++ 是 episode-level 的，不受 sign misattribution 影响; (b) 没有 learned critic 的 REINFORCE 收敛更慢是预期行为; (c) 论文自己的 Cell D 在部分 seeds 上也需要 10-15 步才能看到改进。15 步可能根本不足以让 REINFORCE++ 收敛。
- 建议：要么延长 REINFORCE++ 的训练（至少 30-50 步），要么在论文中明确将此定位为 "initial comparison" 而非方法有效性的结论。

**W4 [warning] Table 1 的报告标准不一致**

- 具体位置：Table 1 caption
- 问题：Cell A 报告 "best seed"，Cell B 报告 "best checkpoint (step 5)"，Cell D 报告 "mean of two seeds (range)"。三种不同的报告标准在同一表中直接比较，使读者难以进行 apple-to-apple comparison。最关键的是 Cell D 用 mean 而 Cell A 用 best，如果 Cell A 也用 mean 可能数字会更差（强化结论），但如果 Cell B 也用 mean 而非 best checkpoint 可能数字也不同。
- 建议：统一报告标准。最严格的做法是全部报告 mean ± std，或全部报告 best checkpoint + mean。

**W5 [warning] 52.07% credit agreement rate 缺乏统计检验**

- 具体位置：Section 4.4
- 问题：论文称 52.07% "indistinguishable from 50% random chance"，但未提供统计检验（binomial test 或 chi-squared test）和样本量。如果样本量很大，52.07% 可能在统计上显著不等于 50%。反之如果确实不显著，应提供 p-value 和 confidence interval。
- 建议：报告 credit agreement 的样本量、binomial test p-value 和 95% CI。

**W6 [warning] SFT baseline 训练细节缺失影响可复现性**

- 具体位置：Section 4.1 ("Qwen3-1.7B fine-tuned on 2,546 expert demonstrations")
- 问题：2,546 demonstrations 的来源（人工标注？GPT-4 生成？rule-based agent？）未说明。SFT 训练的超参数（learning rate、epochs、batch size）未在主文或附录中提供。SFT baseline 是所有对比的基础，其训练细节对可复现性至关重要。
- 建议：在 Appendix B 中补充 SFT 训练细节，包括 demonstration 来源和训练超参数。

### Minor（不影响接收）

- **M1**: Abstract 和 Conclusion 中 "80.9%" 和 "52%" 频繁并列出现，建议在首次出现时就说明前者是 binary reward 理论值、后者是 penalty reward 实测值，而非让读者到 Appendix 才能理解差异。
- **M2**: Eq. 3 中 sign(Â_k) ≈ sign(R_episode − μ) 的 "≈" 未量化近似程度。在 penalty reward 下这个近似从 r>0.99 降到什么程度？Section 4.4 报告 r>0.99 但这是在什么 reward 结构下？
- **M3**: Section 4.3 中 "effective learning rate is 0.66 × 0.19 ≈ 12.6%"——实际计算 0.656 × 0.191 = 0.1253 ≈ 12.5%，paper 写 12.6% 有微小的 rounding inconsistency。
- **M4**: Table 2 中 seed100 出现两次（step 5 和 step 10），这在排版上不够清晰，建议标注为 seed100† 或合并行。
- **M5**: Section 4.7 中 ScienceWorld baseline 在 text 中为 30.1%，但 restricting context 后为 "34.8% to 4.5% (30.3pp M1 gap)"——30.1% 和 34.8% 似乎是不同指标（task success vs. 其他），建议统一或说明差异。

---

## Questions for Authors

**Q1**: Proposition 2 预测 binary reward 下 80.9% incorrect sign，实验测量 penalty reward 下 52% agreement。是否可以在 penalty reward 下推导 closed-form 的 P(correct | update)？如果 penalty 参数从 0 增大到 0.1，P(correct) 如何变化？

**Q2**: Cell C 的 KL 崩溃是否尝试过 gradient clipping per window position 或 advantage clipping？如果 Cell C 可以稳定训练，你们预期结果会是什么？

**Q3**: Eq. 6 的 "comparable magnitude" 假设。你们是否有实验日志中的 advantage 分布数据？successful episode 中 window 的平均 |Â| 与 failed episode 中的平均 |Â| 比值是多少？

**Q4**: Credit agreement 52.07% 的样本量是多少？binomial test p-value？

**Q5**: Factorial conditions 为何仅用 2 seeds？鉴于 11-seed 评估已完成，是否可以对 Cell B、Cell D 也运行更多 seeds？

---

## 总体评分

**Overall Assessment: 3.0 (Findings)**

**一句话总结**: 论文提出了一个重要且实用的诊断——step-independent windowing 在多轮 agent RL 中引入结构性信用分配缺陷——但理论分析的核心数字（80.9%）与实验测量（52%）之间存在未充分解释的差距，cumulative divergence 论证依赖过强假设，factorial 设计有结构性缺口（Cell C 缺失）且统计功效不足（2 seeds），这些共同削弱了论文的方法论严谨性。

## 官方维度打分（ACL ARR review form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 2.5/5 | Proposition 2 推导正确但仅适用于 binary reward；Eq.6 的 comparable magnitude 假设过强；theory-experiment gap (80.9% vs 52%) 未在主文充分讨论；factorial 因 Cell C 缺失而不完整；多处 single-seed claims |
| Excitement | 3.5/5 | 诊断 step-independent windowing 的结构性缺陷是有价值的贡献，对使用 RAGEN 等框架的从业者有直接指导意义；但修复方案（episode-level GRPO）本身不新颖，仅是回到原始设计 |
| Reproducibility | 2.5/5 | 引用了 RAGEN GitHub 仓库，主要超参数在 Appendix B 中列出；但 SFT baseline 训练细节缺失，部分 seeds 的 checkpoints 不可用（Table 2 footnote），episode-level GRPO 的具体实现修改未描述 |
| Reviewer Confidence | 4/5 | 我对 RL credit assignment 理论和 GRPO 算法有较好了解，仔细验证了数学推导和数字一致性 |


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 220 · 2026-05-23T09:10:15.603859+00:00_

Reviewer 1 审稿意见已收到。等待 Reviewer 2 提交后进入交叉分享环节。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director"
}
```

</details>

---


## Round 17

## Round 17

6 recorded events


### User

_source line 221 · 2026-05-23T09:10:18.250800+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 审稿报告：新颖性与完整性

**论文**: Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Fix
**Venue**: EMNLP 2026 (ARR May 2026 cycle)

---

## Summary

本文诊断了 multi-turn agent RL 中 step-independent windowing 训练范式的结构性缺陷。作者 formalize 了两个导致训练失败的机制：(1) Policy Information Loss (M1)——截断上下文导致固定性能天花板；(2) Advantage Sign Misattribution (M2)——group normalization 下 advantage 的符号反映 episode 结果而非局部动作质量，导致累积退化。在 p=12.5%, K=8 时，理论预测 80.9% 的梯度更新方向错误（penalty reward 下实测 52%，与随机无异）。通过 2×2 factorial 分离两个机制，并展示 episode-level GRPO（即 GRPO 原始设计）解决两者。11-seed 评估显示 73% 避免 collapse 但仅 36% 实现统计显著 OOD 泛化。单 seed 8B 和 ScienceWorld 提供初步跨规模/跨环境证据。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| **Soundness** | 3.5/5 | 理论框架 clean，Propositions 推导正确；但 Cell C 缺失削弱 factorial，80.9% 理论 vs 52% 实测存在显著 gap，跨规模/跨环境均为 single-seed |
| **Excitement** | 2.5/5 | 诊断贡献有用但 fix 就是 GRPO 原始设计，无方法论新颖性；36% seed 泛化率限制实用价值；多个同期工作已在探索相同问题空间 |
| **Reproducibility** | 4/5 | Hyperparameters 清晰，RAGEN 框架标注，seed 信息完整；缺代码公开承诺 |
| **Overall Assessment** | 3.0 — Findings | 扎实的诊断分析，formalize 了真实问题，但受限于 fix 无新颖性、seed 依赖严重、缺少与同期方法的对比 |
| **Confidence** | 4/5 | 熟悉 GRPO/agent RL 文献，核实了关键技术声明 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] 缺少与同期方法的实验对比
- 具体位置：Section 4 (Experiments), Section 5 (Related Work)
- 问题：论文在 Introduction 中声称 "GiGPO, GAGPO, Turn-PPO address symptoms but not the structural root cause: the windowing itself"，但未提供任何实验证据支撑此论断。既没有在 ALFWorld 上跑 Turn-PPO / SWEET-RL / HCAPO 的对比，也没有引用这些方法在 ALFWorld 上的已有数据。特别是 HCAPO (Tan et al., 2026, arXiv:2603.08754) 在 ALFWorld + Qwen2.5-7B 上报告了比 GRPO 高 13.8% 的 success rate，直接与本文实验场景重叠，但未被引用或讨论。
- 为什么影响接收：如果 Turn-PPO 或 HCAPO 在 step-independent windowing 下仍能取得不错效果，则本文 "windowing itself is the root cause" 的核心论点会被削弱。不比较就做此声明属于 unsupported claim。
- 建议修改方向：(a) 至少在 ALFWorld 上跑 Turn-PPO 或 SWEET-RL 作为 baseline；(b) 引用并讨论 HCAPO 在 ALFWorld 上的结果；(c) 如果无法实验对比，将 Introduction 中的强声明改为 hypothesis。

**N2** [critical] Episode-level fix 的 seed 依赖严重且未解释
- 具体位置：Section 4.4, Table 2, Section 6 Discussion
- 问题：11 seeds 中仅 4 个 (36%) 达到 p<0.01 显著 OOD 泛化。这意味着使用论文推荐的 episode-level GRPO，有 64% 的概率无法获得有意义的改进。论文承认 "identifying this mechanism is an important open question" (Section 6)，但对于一篇推荐"fix"的论文来说，fix 不可靠是致命问题。Stagnant seeds (seed100/200/300) 和 generalized seeds (seed1/4/5/6) 之间的差异完全没有诊断分析——论文的诊断能力止于 "step-independent is broken" 但无法解释为什么 episode-level 也经常不 work。
- 为什么影响接收：论文标题包含 "Episode-Level Fix"，但该 fix 的可靠性存疑。如果 36% 的成功率对比 step-independent 的 0% 已是进步，这应该在 abstract/conclusion 中更显著地 qualified。目前 abstract 说 "resolves both mechanisms" 但实际上只在少数 seed 上 resolve。
- 建议修改方向：(a) 分析 generalized vs stagnant seeds 的早期 training dynamics 差异（如 gradient norm、advantage distribution）；(b) 在 abstract 和 title 中 qualify "fix" 为 "necessary condition" 而非 "fix"；(c) 讨论 seed selection 策略（如早期 OOD 指标作为 early stopping signal）。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] Cell C 缺失削弱 2×2 factorial 的完整性
- 具体位置：Section 2.5, Section 4.2, Appendix C.4
- 问题：论文宣称 2×2 factorial 分离两个机制，但实际只有 3 个 cells。Cell C（full observation + step-level advantage，仅 M2 active）因训练不稳定未能实现。论文归因于 "full-length sequences with step-level advantage normalization" 导致 KL divergence spike。然而 Cell C 正是隔离 M2 的关键实验——没有它，我们无法独立确认 M2 的影响。目前 M2 的证据来自 A→B 对比（同时移除 M2 并改变 advantage granularity），存在混淆变量。
- 建议：(a) 尝试 gradient clipping per window / advantage clipping 使 Cell C 稳定；(b) 如果确实无法实现，应更 prominently 讨论此 gap 对结论的影响，目前 "important gap in the factorial" 一句带过太轻描淡写。

**W2** [warning] 理论预测与实测的 gap (80.9% → 52%) 需要更深入分析
- 具体位置：Section 3 (Proposition 2), Section 4.3, Appendix A.2
- 问题：Proposition 2 在 binary reward 下预测 19.1% correct-sign rate (80.9% incorrect)。实测在 penalty reward 下为 52% (credit agreement rate)。论文解释差异来自 penalty reward 引入的 intra-group variance，但未量化这一效应。52% 与 50% random 无统计区分，而 19.1% 与 52% 差距巨大。如果 penalty reward（实际系统常用）能将 correct-sign rate 从 19.1% 提升到 52%，那 binary reward 下的理论分析对实际系统的指导意义需要重新评估。
- 建议：(a) 推导 penalty reward 下的修正公式或给出 bound；(b) 跑纯 binary reward 实验验证 19.1% 预测；(c) 更明确地讨论理论结果的适用范围。

**W3** [warning] 跨规模/跨环境证据太弱
- 具体位置：Section 4.5 (Cross-Scale), Section 4.6 (Cross-Environment)
- 问题：8B 实验和 ScienceWorld 实验均为 single seed。论文自己也反复声明 "multi-seed verification is needed"。8B 的 90.3% OOD 结果令人瞩目，但 single-seed 无法排除是幸运 seed（特别是 1.7B 上仅 36% seed 泛化）。ScienceWorld 只跑了 Cell A collapse，没有 Cell D 的 recovery 对照。
- 建议：至少 3 seeds 8B，或者将 cross-scale 证据明确降级为 "anecdotal evidence"（目前 "preliminary evidence" 已经比较谨慎，但 abstract 中 "90.3% OOD vs collapse to 1.5%" 的表述给人印象较强）。

**W4** [warning] 重要相关工作遗漏
- 具体位置：Section 5 (Related Work)
- 问题：以下直接相关的 2025-2026 工作未引用：
  1. **HCAPO** (Tan et al., 2026, arXiv:2603.08754) — Hindsight Credit Assignment for Long-Horizon LLM Agents，在 ALFWorld 上做实验，比 GRPO 提升 13.8%，**直接竞争性工作**
  2. **RC-GRPO** (Feb 2026, arXiv:2602.03025) — Reward-Conditioned GRPO，解决 within-group reward variance collapse，与本文 M2 高度相关
  3. **iStar** (Liu et al., 2025, arXiv:2509.19199) — Implicit step rewards for agentic RL，WebShop 上的 SOTA
  4. **"From Reasoning to Agentic" survey** (April 2026, arXiv:2604.09459) — 47 篇 credit assignment 方法综述，本文应该 position 自己在此 taxonomy 中
  5. **EDGE-GRPO** (2025, arXiv:2507.21848) — 解决 advantage collapse，与 GRPO collapse phenomena 段落直接相关
- 这些工作大部分在 ARR May 2026 deadline (2026-05-25) 前 3+ 个月发表，按 ARR guidelines 应被检索到。

---

## 小问题（不影响接收）

- **术语一致性**：论文主要用 "step-independent"，但 Related Work 中出现 "step-level windowing"（Section 5 para 1）和 "window-level"（Section 1），建议统一。
- **Table 2 注释**：seed1 标记 $\dagger$ "RAGEN built-in eval; checkpoint unavailable for re-evaluation"——如果关键结果无法 reproduce（checkpoint 丢失），这在 reproducibility 上是减分项。
- **Proposition 2 中 "locally good actions" 的定义**：Definition 1 定义了 "locally correct"，但 Proposition 2 proofsketch 中切换为 "locally good actions"——应保持术语一致。
- **Figure 1 可读性**：y 轴 "P(correct sign | update) (%)" 的百分号与正文中的小数表述不一致（正文说 19.1%，图中显示 19.1）。
- **Appendix E Table 5**：多个 seed 的 OOD 和 ID 数据标记 "---" (unavailable)，11 seeds 中有 4 个 seed 缺少 step-5 OOD 数据——评估的系统性打折扣。

---

## Questions to Authors

1. **关于 HCAPO 对比**：HCAPO (arXiv:2603.08754) 在 ALFWorld + Qwen2.5-7B 上比 GRPO 提升 13.8%，且使用 step-level credit assignment。这是否意味着 step-level credit assignment 在有好的 credit assignment 策略时是可行的？如果是，论文 "the windowing itself is the problem" 的论断需要如何修正？

2. **关于 seed 依赖**：在 4 个 generalized seeds 之间是否存在共同特征（如初始 loss、早期 gradient norm pattern）？是否可以设计 early stopping 策略来避免 stagnant seeds？

3. **关于 Cell C**：是否尝试过 (a) 使用 PPO 的 clipping 代替 GRPO 的 group normalization 来稳定 Cell C，或 (b) 使用 gradient accumulation 来处理 full-length sequences 的内存问题？

4. **关于计算成本**：Episode-level training 的 O(T²) attention cost 是一个重要的实际障碍。对于 T=50 步的 ALFWorld，episode-level 相比 h=2 的 step-independent 的实际 wall-clock 时间比例是多少？

---

## Missing References

1. Tan et al., 2026. "Hindsight Credit Assignment for Long-Horizon LLM Agents." arXiv:2603.08754. **[直接竞争——ALFWorld 实验]**
2. RC-GRPO, Feb 2026. arXiv:2602.03025. **[GRPO variance collapse, 与 M2 高度相关]**
3. Liu et al., 2025. "Agentic Reinforcement Learning with Implicit Step Rewards." arXiv:2509.19199. **[iStar, step reward 方法]**
4. Survey: "From Reasoning to Agentic: Credit Assignment in RL for LLMs." April 2026. arXiv:2604.09459. **[47 篇综述，应 position]**
5. EDGE-GRPO, 2025. arXiv:2507.21848. **[Advantage collapse 直接相关]**

---

## 主要优势

1. **清晰的问题 formalization**：将散见于多个工作中的 step-independent training 失败现象统一为两个可分离的机制（M1: information loss, M2: sign misattribution），并给出可验证的理论预测。
2. **干净的 factorial 实验设计**：2×2 factorial（虽然缺 Cell C）系统地分离了两个机制，A→B→D 的 progression 具有说服力。
3. **诚实的报告风格**：论文没有 cherry-pick 最好的 seed，而是报告了所有 11 seeds 的结果并分类分析（collapsed/stagnant/generalized）。单 seed 实验均标注 "preliminary"，符合良好的科学实践。
4. **实用的 practitioner guidance**：Section 6 Discussion 的实践建议（"use largest feasible h, at least h≥20"）对社区有直接价值。
5. **Credit agreement rate 测量**：Section 4.3 的 52% 经验测量直接验证了理论预测的方向性（≈random），虽然数值差异需要解释。

---

## 总体评分

**Overall**: 3.0 — Findings

**一句话总结**: 扎实的诊断分析 paper，清晰地 formalize 了 step-independent agent RL 的两个结构性缺陷，但受限于 fix 无方法论新颖性（就是原始 GRPO）、36% 的 seed 泛化率、缺少与 HCAPO 等直接竞争方法的对比、以及单 seed 的跨规模证据。适合 Findings 接收，但需要补充关键实验对比并 qualify overclaiming。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 222 · 2026-05-23T09:10:56.442731+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "project": "cost-verify-agent-rl",
  "reviewer_id": "1",
  "round_number": "1",
  "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应：对每个主要观点标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n# Reviewer 2 审稿报告：新颖性与完整性\n\n## Summary\n本文诊断了 multi-turn agent RL 中 step-independent windowing 训练范式的结构性缺陷。作者 formalize 了两个导致训练失败的机制：(1) Policy Information Loss (M1)——截断上下文导致固定性能天花板；(2) Advantage Sign Misattribution (M2)——group normalization 下 advantage 的符号反映 episode 结果而非局部动作质量，导致累积退化。在 p=12.5%, K=8 时，理论预测 80.9% 的梯度更新方向错误（penalty reward 下实测 52%，与随机无异）。通过 2×2 factorial 分离两个机制，并展示 episode-level GRPO（即 GRPO 原始设计）解决两者。11-seed 评估显示 73% 避免 collapse 但仅 36% 实现统计显著 OOD 泛化。单 seed 8B 和 ScienceWorld 提供初步跨规模/跨环境证据。\n\n## Must-Fix\n\n**N1** [critical] 缺少与同期方法的实验对比\n- 论文声称 \"GiGPO, GAGPO, Turn-PPO address symptoms but not the structural root cause\"，但未提供实验证据。特别是 HCAPO (Tan et al., 2026, arXiv:2603.08754) 在 ALFWorld + Qwen2.5-7B 上报告了比 GRPO 高 13.8%，直接竞争但未引用。\n\n**N2** [critical] Episode-level fix 的 seed 依赖严重且未解释\n- 11 seeds 中仅 36% 达到显著 OOD 泛化。论文标题包含 \"Fix\" 但该 fix 的可靠性存疑。Abstract 说 \"resolves both mechanisms\" 但只在少数 seed 上 resolve。建议 qualify \"fix\" 为 \"necessary condition\"。\n\n## Should-Fix\n\n**W1** Cell C 缺失削弱 factorial 完整性（与你的 N3 重合）\n\n**W2** 80.9% vs 52% gap 需要更深入分析（与你的 N1 重合）\n\n**W3** 跨规模/跨环境证据太弱——8B single seed, ScienceWorld 只有 Cell A 没有 Cell D recovery\n\n**W4** 重要相关工作遗漏：HCAPO, RC-GRPO, iStar, \"From Reasoning to Agentic\" survey, EDGE-GRPO\n\n## Minor\n- 术语不一致：step-independent / step-level windowing / window-level 混用\n- seed1 checkpoint 丢失影响 reproducibility\n- Definition 1 用 \"locally correct\" 但 Proposition 2 proof 切换为 \"locally good actions\"\n- Table 5 (Appendix E) 多个 seed 缺数据\n\n## Overall: 3.0 (Findings)\n- Soundness 3.5, Excitement 2.5, Reproducibility 4.0, Confidence 4/5\n\n---\n\n请逐条回应上述意见。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "project": "cost-verify-agent-rl",
    "reviewer_id": "1",
    "round_number": "1",
    "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应：对每个主要观点标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n# Reviewer 2 审稿报告：新颖性与完整性\n\n## Summary\n本文诊断了 multi-turn agent RL 中 step-independent windowing 训练范式的结构性缺陷。作者 formalize 了两个导致训练失败的机制：(1) Policy Information Loss (M1)——截断上下文导致固定性能天花板；(2) Advantage Sign Misattribution (M2)——group normalization 下 advantage 的符号反映 episode 结果而非局部动作质量，导致累积退化。在 p=12.5%, K=8 时，理论预测 80.9% 的梯度更新方向错误（penalty reward 下实测 52%，与随机无异）。通过 2×2 factorial 分离两个机制，并展示 episode-level GRPO（即 GRPO 原始设计）解决两者。11-seed 评估显示 73% 避免 collapse 但仅 36% 实现统计显著 OOD 泛化。单 seed 8B 和 ScienceWorld 提供初步跨规模/跨环境证据。\n\n## Must-Fix\n\n**N1** [critical] 缺少与同期方法的实验对比\n- 论文声称 \"GiGPO, GAGPO, Turn-PPO address symptoms but not the structural root cause\"，但未提供实验证据。特别是 HCAPO (Tan et al., 2026, arXiv:2603.08754) 在 ALFWorld + Qwen2.5-7B 上报告了比 GRPO 高 13.8%，直接竞争但未引用。\n\n**N2** [critical] Episode-level fix 的 seed 依赖严重且未解释\n- 11 seeds 中仅 36% 达到显著 OOD 泛化。论文标题包含 \"Fix\" 但该 fix 的可靠性存疑。Abstract 说 \"resolves both mechanisms\" 但只在少数 seed 上 resolve。建议 qualify \"fix\" 为 \"necessary condition\"。\n\n## Should-Fix\n\n**W1** Cell C 缺失削弱 factorial 完整性（与你的 N3 重合）\n\n**W2** 80.9% vs 52% gap 需要更深入分析（与你的 N1 重合）\n\n**W3** 跨规模/跨环境证据太弱——8B single seed, ScienceWorld 只有 Cell A 没有 Cell D recovery\n\n**W4** 重要相关工作遗漏：HCAPO, RC-GRPO, iStar, \"From Reasoning to Agentic\" survey, EDGE-GRPO\n\n## Minor\n- 术语不一致：step-independent / step-level windowing / window-level 混用\n- seed1 checkpoint 丢失影响 reproducibility\n- Definition 1 用 \"locally correct\" 但 Proposition 2 proof 切换为 \"locally good actions\"\n- Table 5 (Appendix E) 多个 seed 缺数据\n\n## Overall: 3.0 (Findings)\n- Soundness 3.5, Excitement 2.5, Reproducibility 4.0, Confidence 4/5\n\n---\n\n请逐条回应上述意见。"
  }
}
```

</details>

---


### Tool result

_source line 223 · 2026-05-23T09:11:14.615604+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_648eaf83d2b24d445764257cf6a55525:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 18172
}
```

</details>

---


### Tool call

_source line 224 · 2026-05-23T09:11:15.067679+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "project": "cost-verify-agent-rl",
  "reviewer_id": "2",
  "round_number": "1",
  "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应：对每个主要观点标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n# Reviewer 1: 方法严谨性审查\n\n## Must-Fix\n\n**N1** [critical] 理论预测与实验测量之间的 28.9pp 差距在主文中处理不当\n- Abstract/Intro 将 80.9% (binary theory) 和 52% (penalty experiment) 简单并列，给读者造成两者互相支持的印象，实际存在实质性矛盾。gap 解释仅在 Appendix A.2。建议：主文 Section 3/4.4 讨论差异，或将标题数字改为 52%。\n\n**N2** [critical] Eq. 6 累积发散论证依赖过强假设\n- \"comparable magnitude\" 假设在 GRPO group normalization 下几乎不成立。成功 episode 的 advantage 量级可能系统性大于失败 episode，部分补偿频率劣势。如果量级不可比，sign misattribution 可能从 \"active divergence\" 降级为 \"noisy convergence\"。\n\n**N3** [critical] Factorial 设计有结构性缺陷：Cell C 缺失且种子数不足\n- Cell C 缺失使 \"empirical separation\" 不完整；每 condition 仅 2 seeds，在高 seed variability 下不足以稳定估计。\n\n## Should-Fix\n\n**W1** Definition 1 操作化存在逻辑循环——用 episode outcome 替代 local quality\n\n**W2** Window-size cliff 基于 single seed\n\n**W3** REINFORCE++ 仅 15 步，对比可能不公平\n\n**W4** Table 1 报告标准不一致（best seed / best checkpoint / mean 混用）\n\n**W5** 52.07% credit agreement 缺乏统计检验（无 binomial test、样本量、CI）\n\n**W6** SFT baseline 训练细节缺失\n\n## Minor\n- M1: 80.9% vs 52% 首次出现时应说明差异\n- M2: Eq. 3 \"≈\" 未量化\n- M3: 12.6% rounding inconsistency (应为 12.5%)\n- M4: seed100 在 Table 2 出现两次\n- M5: ScienceWorld 30.1% vs 34.8% 指标差异\n\n## Overall: 3.0 (Findings)\n- Soundness 2.5, Excitement 3.5, Reproducibility 2.5, Confidence 4/5\n\n---\n\n请逐条回应上述意见。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "project": "cost-verify-agent-rl",
    "reviewer_id": "2",
    "round_number": "1",
    "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应：对每个主要观点标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n# Reviewer 1: 方法严谨性审查\n\n## Must-Fix\n\n**N1** [critical] 理论预测与实验测量之间的 28.9pp 差距在主文中处理不当\n- Abstract/Intro 将 80.9% (binary theory) 和 52% (penalty experiment) 简单并列，给读者造成两者互相支持的印象，实际存在实质性矛盾。gap 解释仅在 Appendix A.2。建议：主文 Section 3/4.4 讨论差异，或将标题数字改为 52%。\n\n**N2** [critical] Eq. 6 累积发散论证依赖过强假设\n- \"comparable magnitude\" 假设在 GRPO group normalization 下几乎不成立。成功 episode 的 advantage 量级可能系统性大于失败 episode，部分补偿频率劣势。如果量级不可比，sign misattribution 可能从 \"active divergence\" 降级为 \"noisy convergence\"。\n\n**N3** [critical] Factorial 设计有结构性缺陷：Cell C 缺失且种子数不足\n- Cell C 缺失使 \"empirical separation\" 不完整；每 condition 仅 2 seeds，在高 seed variability 下不足以稳定估计。\n\n## Should-Fix\n\n**W1** Definition 1 操作化存在逻辑循环——用 episode outcome 替代 local quality\n\n**W2** Window-size cliff 基于 single seed\n\n**W3** REINFORCE++ 仅 15 步，对比可能不公平\n\n**W4** Table 1 报告标准不一致（best seed / best checkpoint / mean 混用）\n\n**W5** 52.07% credit agreement 缺乏统计检验（无 binomial test、样本量、CI）\n\n**W6** SFT baseline 训练细节缺失\n\n## Minor\n- M1: 80.9% vs 52% 首次出现时应说明差异\n- M2: Eq. 3 \"≈\" 未量化\n- M3: 12.6% rounding inconsistency (应为 12.5%)\n- M4: seed100 在 Table 2 出现两次\n- M5: ScienceWorld 30.1% vs 34.8% 指标差异\n\n## Overall: 3.0 (Findings)\n- Soundness 2.5, Excitement 3.5, Reproducibility 2.5, Confidence 4/5\n\n---\n\n请逐条回应上述意见。"
  }
}
```

</details>

---


### Tool result

_source line 225 · 2026-05-23T09:11:16.527495+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_648eaf83d2b24d445764257cf6a55525:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1459
}
```

</details>

---


### Assistant

_source line 226 · 2026-05-23T09:11:18.980890+00:00_

交叉分享已发送。等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director"
}
```

</details>

---


## Round 18

## Round 18

12 recorded events


### User

_source line 227 · 2026-05-23T09:11:20.136634+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

核心发现：

1. **3 个 Must-Fix 问题**：(a) 理论预测 80.9% vs 实测 52% 的差距在主文中处理不当，构成误导；(b) Eq.6 累积发散的 "comparable magnitude" 假设过强，GRPO normalization 下 correct/incorrect gradient 的量级系统性不可比；(c) Factorial 设计因 Cell C 缺失而不完整，且每个 condition 仅 2 seeds 统计功效严重不足。

2. **6 个 Should-Fix 问题**：Definition 1 操作化循环、window-size cliff 单 seed、REINFORCE++ 对比不公平、Table 1 报告标准不一致、52% credit agreement 缺统计检验、SFT baseline 细节缺失。

3. **Overall: 3.0 (Findings)**，Soundness 2.5/5，Excitement 3.5/5。论文的诊断方向有价值，但方法论严谨性不足以支撑 Conference 级别接收。

---

[Reviewer 2 审稿结果]:
审稿报告已提交给 Review Director。

**审稿总结**：

- **Overall: 3.0 (Findings)**，Soundness 3.5，Excitement 2.5，Reproducibility 4，Confidence 4
- **2 个 Must-Fix**：(1) 缺少与 HCAPO/Turn-PPO 等同期方法的实验对比，Introduction 中的强声明缺乏实验支撑；(2) Episode-level fix 仅 36% seed 泛化，title 中 "Fix" 的表述 overclaiming
- **4 个 Should-Fix**：Cell C 缺失、理论与实测 gap (80.9%→52%)、跨规模证据太弱 (single seed)、遗漏 5 篇重要相关工作（尤其 HCAPO 在 ALFWorld 上有直接竞争性结果）
- **优势**：清晰的问题 formalization、干净的 factorial 设计、诚实的多 seed 报告风格

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 228 · 2026-05-23T09:11:45.553354+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "cost-verify-agent-rl"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "cost-verify-agent-rl"
  }
}
```

</details>

---


### Tool result

_source line 229 · 2026-05-23T09:11:45.905184+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-23T09:04:07.844728+00:00\", \"completed_at\": \"2026-05-23T09:07:27.561935+00:00\", \"findings\": [{\"severity\": \"warning\", \"dimension\": \"page 1-3\", \"message\": \"前 3 页无任何 display item（首个 figure 在第 4 页）。审稿人前 2 分钟内只看到文字和公式，缺少视觉锚点。Pages 2-3 有数学推导可部分缓解，但考虑将 Figure 1（理论结果图）或一个概念架构图提前到 page 2 以建立审稿人的第一印象锚定。\"}, {\"severity\": \"warning\", \"dimension\": \"page 13\", \"message\": \"页面底部约 1/3 空白（Table 5 下方），可通过调整 float 位置或将 Figure 4/5 从 page 14 上移来填充。\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Figure 3 使用红色+绿色柱状图配色，对红绿色盲读者不友好。建议改用 blue+orange 或 Okabe-Ito 色板。\"}, {\"severity\": \"info\", \"dimension\": \"page 14\", \"message\": \"Figure 4(b) 同样使用绿色/红色对比，存在色盲可读性风险。\"}, {\"severity\": \"info\", \"dimension\": \"page 14\", \"message\": \"最后一页（附录末页）内容约占 60%，底部有明显空白。非正文页影响较小。\"}, {\"severity\": \"info\", \"dimension\": \"page 4\", \"message\": \"脚注包含 GitHub 链接 (RAGEN-AI/RAGEN)，若作者与 RAGEN 开发者相关，可能违反匿名审稿要求。\"}, {\"severity\": \"info\", \"dimension\": \"page 5\", \"message\": \"Table 2 列数较多（7 列），字号偏小但仍可读。脚注 dagger 符号清晰。\"}], \"counts\": {\"critical\": 0, \"warning\": 2, \"info\": 5}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 230 · 2026-05-23T09:11:45.905539+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "cost-verify-agent-rl"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "cost-verify-agent-rl"
  }
}
```

</details>

---


### Tool result

_source line 231 · 2026-05-23T09:11:45.955971+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 232 · 2026-05-23T09:12:22.824760+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:update_review_issues",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:update_review_issues",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 233 · 2026-05-23T09:12:22.825238+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 234 · 2026-05-23T09:14:00.055217+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "cost-verify-agent-rl",
  "issues_yaml": "- id: W1\n  summary: '\"Locally correct actions\" 定义操作化存在逻辑循环'\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: [R1, R2], note: \"Entire theoretical framework depends on this undefined concept\"}\n    - {round: 1, action_taken: \"Definition 1 added in theoretical_analysis.tex; operationalized in experiments.tex Section 4.4\"}\n    - {round: 2, reviewers: [R1], note: \"定义已添加但操作化存在循环：用 episode outcome 标记 locally correct，恰好犯了论文批评的错误。成功 episode 中的次优 window 也被标记为 locally correct。\"}\n  action_items:\n    - {round: 2, action: \"在 Section 4.4 讨论操作化的近似性质（上界估计），或提供样本分析支持合理性\", assigned_to: main_agent, status: pending}\n\n- id: W2\n  summary: \"Theory (80.9%) vs experiment (52%) gap 在主文中仍处理不当\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: [R1, R2], note: \"Prop 2 predicts 19.1%, measured 52.07%. Intro/Conclusion use 80.9% but experiments show 52%\"}\n    - {round: 1, action_taken: \"Penalty reward analysis added to appendix. Intro/Conclusion/Abstract present 80.9% qualified with '(52% under penalty reward)'\"}\n    - {round: 2, reviewers: [R1, R2], note: \"Round 1 修复不充分。Abstract/Intro 仍将两个数字简单并列，给读者造成互相支持的印象。Gap 解释仍仅在 Appendix A.2。需要在主文 Section 3/4.4 讨论差异，或将标题数字改为 52%。缺乏 penalty reward 下的理论修正公式或 pure binary 实验验证。\"}\n  action_items:\n    - {round: 2, action: \"在主文 Section 3 或 4.4 显著讨论 binary vs penalty reward 差异；推导 penalty reward 修正公式或跑纯 binary 实验；考虑将标题数字改为实验值\", assigned_to: main_agent, status: pending}\n\n- id: W3\n  summary: \"10/20 citations use Anonymous authors — ARR compliance violation\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 1, reviewers: [R1, R2], note: \"irc2026, grpolambda2025, oar2026 etc.\"}\n    - {round: 1, action_taken: \"All 10 entries updated with real authors. Total 33 citations.\"}\n    - {round: 2, note: \"本轮未被提及，已修复确认\"}\n  resolution: \"All citations now have real authors\"\n  resolution_round: 1\n\n- id: W4\n  summary: \"8B 和 ScienceWorld 跨规模/跨环境证据仍然不足\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: [R1, R2], note: \"Confirmatory language vs actual statistical power mismatch\"}\n    - {round: 1, action_taken: \"All 8B/ScienceWorld claims use 'preliminary'/'single-seed' qualifiers\"}\n    - {round: 2, reviewers: [R2], note: \"措辞已降级为 preliminary，但 abstract 中 '90.3% OOD vs collapse to 1.5%' 仍给人强印象。ScienceWorld 只有 Cell A collapse 无 Cell D recovery。1.7B 仅 36% seed 泛化下，single-seed 8B 无法排除幸运 seed。\"}\n  action_items:\n    - {round: 2, action: \"至少 3 seeds 8B 验证，或将 cross-scale 进一步降级为 anecdotal evidence；ScienceWorld 补 Cell D\", assigned_to: main_agent, status: pending}\n\n- id: W5\n  summary: \"h-sweep cliff claim 仍基于 single seed\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: [R1, R2], note: \"High seed variability makes single-seed cliff claim unreliable\"}\n    - {round: 1, action_taken: \"Caveat added: 'This cliff pattern is observed in a single seed'\"}\n    - {round: 2, reviewers: [R1], note: \"Caveat 已加但 'cliff' 强措辞不匹配，建议改为 'preliminary observation' 或增加 3+ seeds\"}\n  action_items:\n    - {round: 2, action: \"弱化 cliff 措辞或增加多 seed 验证\", assigned_to: main_agent, status: pending}\n\n- id: W6\n  summary: \"Limited novelty — fix 是回到 GRPO 原始设计 + seed 依赖严重\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: [R1, R2], note: \"R1 Major (Excitement 3.5), R2 Critical (Excitement 2.5)\"}\n    - {round: 1, action_taken: \"Intro P3: 'Our primary contribution is diagnostic'\"}\n    - {round: 2, reviewers: [R2], note: \"36% seed 泛化率使 'Fix' 表述 overclaiming。Abstract 'resolves both mechanisms' 只在少数 seed 上 resolve。Title 中 'Fix' 需 qualify 为 'necessary condition'。\"}\n  action_items:\n    - {round: 2, action: \"Title 和 Abstract 中将 'Fix' qualify 为 necessary condition 而非 sufficient fix；分析 generalized vs stagnant seeds 早期 dynamics 差异\", assigned_to: main_agent, status: pending}\n\n- id: W7\n  summary: \"重要相关工作遗漏（5 篇直接竞争/高度相关论文）\"\n  category: writing\n  severity: critical\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - {round: 1, note: \"Round 1 修复了 citation count (20→33) 和 Anonymous 问题\"}\n    - {round: 2, reviewers: [R2], note: \"5 篇重要遗漏：HCAPO (arXiv:2603.08754, ALFWorld 直接竞争), RC-GRPO (arXiv:2602.03025), iStar (arXiv:2509.19199), From Reasoning to Agentic survey (arXiv:2604.09459), EDGE-GRPO (arXiv:2507.21848)。特别是 HCAPO 在 ALFWorld+Qwen2.5-7B 上报告比 GRPO 高 13.8%。\"}\n  action_items:\n    - {round: 2, action: \"引用并讨论 5 篇论文，特别是 HCAPO 需在 Related Work 和 Experiments 中 position\", assigned_to: main_agent, status: pending}\n\n- id: W8\n  summary: \"Cell C 缺失使 factorial 不完整\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: [R1, R2], note: \"Cell C would isolate M2 without M1\"}\n    - {round: 1, action_taken: \"Cell C prediction in experiments.tex, crash record in appendix (6 runs, KL spike)\"}\n    - {round: 2, reviewers: [R1, R2], note: \"问题仍在。Cell C 正是隔离 M2 的关键——没有它无法独立确认 M2 影响。Cell C crash 本身说明 step-level advantage 在 full context 下行为可能质性不同。建议尝试 gradient clipping/advantage clipping 或更 prominently 讨论 gap 对结论的影响。\"}\n  action_items:\n    - {round: 2, action: \"尝试 gradient clipping per window 稳定 Cell C，或更显著讨论 Cell C 缺失对 M2 隔离结论的影响\", assigned_to: main_agent, status: pending}\n\n- id: W9\n  summary: \"REINFORCE++ 仅 15 步，对比可能不公平\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: [R1, R2], note: \"REINFORCE++ 12.5% may be undertrained\"}\n    - {round: 1, action_taken: \"Appendix: REINFORCE++ caveat added\"}\n    - {round: 2, reviewers: [R1], note: \"Caveat 已加但问题实质未解决。REINFORCE++ 是 episode-level 不受 sign misattribution 影响，无 critic 收敛本来就慢，15 步不足。\"}\n  action_items:\n    - {round: 2, action: \"延长 REINFORCE++ 训练至 30-50 步，或将结论定位为 'initial comparison'\", assigned_to: main_agent, status: pending}\n\n- id: W10\n  summary: \"Conclusion drops 'locally correct actions' qualifier on 80.9%\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 1, action_taken: \"Conclusion now uses '80.9% incorrect-sign updates under binary reward (52% measured under penalty reward)'\"}\n    - {round: 2, note: \"本轮未单独提及，已与 W2 合并处理\"}\n  resolution: \"Merged with W2 fix\"\n  resolution_round: 1\n\n- id: W11\n  summary: \"Eq.6 累积发散论证依赖 comparable magnitude 假设过强\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: [R1, R2], note: \"Simple conditional probability, lacks formal connection to divergence\"}\n    - {round: 1, action_taken: \"Cumulative divergence sketch added in theoretical_analysis.tex with Eq. biased_gradient\"}\n    - {round: 2, reviewers: [R1], note: \"Round 1 加了 Eq.6 但假设 'comparable magnitude' 过强。GRPO normalization 下成功 episode 的 advantage 量级系统性大于失败 episode（μ 较小时 r+-μ 远大于 0-μ）。一个大的 correct gradient 可能抵消多个小的 incorrect gradients，使 monotonic divergence 结论不成立。需要实际 advantage 分布数据或将 Eq.6 降级为 worst-case analysis。\"}\n  action_items:\n    - {round: 2, action: \"从实验日志提取 advantage 分布，分析 correct vs incorrect gradient 量级比；若无法证明量级可比，将 Eq.6 降级为 worst-case analysis\", assigned_to: main_agent, status: pending}\n\n- id: W12\n  summary: \"Table 1 报告标准不一致\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: [R1, R2], note: \"best seed / best checkpoint / mean mixed\"}\n    - {round: 1, action_taken: \"Table 1 caption unified to 'best checkpoint per seed'\"}\n    - {round: 2, reviewers: [R1], note: \"Caption 改了但实际数据仍混用：Cell A 是 best seed，Cell B 是 best checkpoint (step 5)，Cell D 是 mean of two seeds。需统一为 mean±std 或全部 best checkpoint + mean。\"}\n  action_items:\n    - {round: 2, action: \"统一 Table 1 所有 conditions 的报告标准\", assigned_to: main_agent, status: pending}\n\n- id: R2-N1\n  summary: \"缺少与 HCAPO/Turn-PPO 等同期方法的实验对比\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - {round: 2, reviewers: [R2], note: \"Introduction 声称 'GiGPO, GAGPO, Turn-PPO address symptoms not root cause' 但无实验支撑。HCAPO 在 ALFWorld+Qwen2.5-7B 上比 GRPO 高 13.8%，直接竞争未引用。如果这些方法在 step-independent 下仍有效，核心论点被削弱。\"}\n  action_items:\n    - {round: 2, action: \"在 ALFWorld 上跑 Turn-PPO 或 HCAPO baseline；若无法实验则将强声明改为 hypothesis\", assigned_to: main_agent, status: pending}\n\n- id: R1-W5\n  summary: \"52.07% credit agreement rate 缺乏统计检验\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - {round: 2, reviewers: [R1], note: \"称 52.07% '与 50% 无异' 但未报告 binomial test p-value、样本量和 95% CI\"}\n  action_items:\n    - {round: 2, action: \"报告 credit agreement 样本量、binomial test p-value 和 95% CI\", assigned_to: main_agent, status: pending}\n\n- id: R1-W6\n  summary: \"SFT baseline 训练细节缺失\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - {round: 2, reviewers: [R1], note: \"2,546 demonstrations 来源（人工/GPT-4/rule-based）未说明，SFT 超参数未提供\"}\n  action_items:\n    - {round: 2, action: \"Appendix B 补充 SFT 训练细节：demonstration 来源和训练超参数\", assigned_to: main_agent, status: pending}\n\n- id: AUDIT-1\n  summary: \"Seed count inconsistency: 27% vs 36%\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 1, reviewers: [audit], note: \"5 locations had 27%, Table 2 clearly shows 4 G seeds.\"}\n    - {round: 1, action_taken: \"All 5 locations updated to 36%\"}\n    - {round: 2, note: \"本轮未提及，已修复确认\"}\n  resolution: \"All locations updated to 36%\"\n  resolution_round: 1\n\n- id: AUDIT-2\n  summary: \"Cell C described as 'degenerate' — incorrect\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 1, reviewers: [audit], note: \"method.tex claimed Cell C degenerate but was actually attempted\"}\n    - {round: 1, action_taken: \"'degenerate' removed, Cell C description updated\"}\n    - {round: 2, note: \"本轮未提及，已修复确认\"}\n  resolution: \"Corrected in all files\"\n  resolution_round: 1\n\n- id: R-add1\n  summary: \"Contribution 2 overclaim for single-seed evidence\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 1, action_taken: \"Downgraded to 'preliminary evidence'\"}\n    - {round: 2, note: \"本轮未单独提及，但 R2-W3 延续了类似关切\"}\n  resolution: \"Contribution 2 downgraded\"\n  resolution_round: 1\n\n- id: R-add2\n  summary: \"Table 2 needs anti-cherry-picking defense\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 1, action_taken: \"Table 7 in appendix with all seeds at step 5\"}\n    - {round: 2, note: \"本轮未提及，已修复确认\"}\n  resolution: \"Appendix table added\"\n  resolution_round: 1\n\n- id: R-add3\n  summary: \"seed2 classification boundary justification\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 1, action_taken: \"Table 2 caption: 'Seed2 achieves p=0.02, falling just outside p<0.01 threshold'\"}\n    - {round: 2, note: \"本轮未提及，已修复确认\"}\n  resolution: \"Caption updated\"\n  resolution_round: 1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "cost-verify-agent-rl",
    "issues_yaml": "- id: W1\n  summary: '\"Locally correct actions\" 定义操作化存在逻辑循环'\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: [R1, R2], note: \"Entire theoretical framework depends on this undefined concept\"}\n    - {round: 1, action_taken: \"Definition 1 added in theoretical_analysis.tex; operationalized in experiments.tex Section 4.4\"}\n    - {round: 2, reviewers: [R1], note: \"定义已添加但操作化存在循环：用 episode outcome 标记 locally correct，恰好犯了论文批评的错误。成功 episode 中的次优 window 也被标记为 locally correct。\"}\n  action_items:\n    - {round: 2, action: \"在 Section 4.4 讨论操作化的近似性质（上界估计），或提供样本分析支持合理性\", assigned_to: main_agent, status: pending}\n\n- id: W2\n  summary: \"Theory (80.9%) vs experiment (52%) gap 在主文中仍处理不当\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: [R1, R2], note: \"Prop 2 predicts 19.1%, measured 52.07%. Intro/Conclusion use 80.9% but experiments show 52%\"}\n    - {round: 1, action_taken: \"Penalty reward analysis added to appendix. Intro/Conclusion/Abstract present 80.9% qualified with '(52% under penalty reward)'\"}\n    - {round: 2, reviewers: [R1, R2], note: \"Round 1 修复不充分。Abstract/Intro 仍将两个数字简单并列，给读者造成互相支持的印象。Gap 解释仍仅在 Appendix A.2。需要在主文 Section 3/4.4 讨论差异，或将标题数字改为 52%。缺乏 penalty reward 下的理论修正公式或 pure binary 实验验证。\"}\n  action_items:\n    - {round: 2, action: \"在主文 Section 3 或 4.4 显著讨论 binary vs penalty reward 差异；推导 penalty reward 修正公式或跑纯 binary 实验；考虑将标题数字改为实验值\", assigned_to: main_agent, status: pending}\n\n- id: W3\n  summary: \"10/20 citations use Anonymous authors — ARR compliance violation\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 1, reviewers: [R1, R2], note: \"irc2026, grpolambda2025, oar2026 etc.\"}\n    - {round: 1, action_taken: \"All 10 entries updated with real authors. Total 33 citations.\"}\n    - {round: 2, note: \"本轮未被提及，已修复确认\"}\n  resolution: \"All citations now have real authors\"\n  resolution_round: 1\n\n- id: W4\n  summary: \"8B 和 ScienceWorld 跨规模/跨环境证据仍然不足\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: [R1, R2], note: \"Confirmatory language vs actual statistical power mismatch\"}\n    - {round: 1, action_taken: \"All 8B/ScienceWorld claims use 'preliminary'/'single-seed' qualifiers\"}\n    - {round: 2, reviewers: [R2], note: \"措辞已降级为 preliminary，但 abstract 中 '90.3% OOD vs collapse to 1.5%' 仍给人强印象。ScienceWorld 只有 Cell A collapse 无 Cell D recovery。1.7B 仅 36% seed 泛化下，single-seed 8B 无法排除幸运 seed。\"}\n  action_items:\n    - {round: 2, action: \"至少 3 seeds 8B 验证，或将 cross-scale 进一步降级为 anecdotal evidence；ScienceWorld 补 Cell D\", assigned_to: main_agent, status: pending}\n\n- id: W5\n  summary: \"h-sweep cliff claim 仍基于 single seed\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: [R1, R2], note: \"High seed variability makes single-seed cliff claim unreliable\"}\n    - {round: 1, action_taken: \"Caveat added: 'This cliff pattern is observed in a single seed'\"}\n    - {round: 2, reviewers: [R1], note: \"Caveat 已加但 'cliff' 强措辞不匹配，建议改为 'preliminary observation' 或增加 3+ seeds\"}\n  action_items:\n    - {round: 2, action: \"弱化 cliff 措辞或增加多 seed 验证\", assigned_to: main_agent, status: pending}\n\n- id: W6\n  summary: \"Limited novelty — fix 是回到 GRPO 原始设计 + seed 依赖严重\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: [R1, R2], note: \"R1 Major (Excitement 3.5), R2 Critical (Excitement 2.5)\"}\n    - {round: 1, action_taken: \"Intro P3: 'Our primary contribution is diagnostic'\"}\n    - {round: 2, reviewers: [R2], note: \"36% seed 泛化率使 'Fix' 表述 overclaiming。Abstract 'resolves both mechanisms' 只在少数 seed 上 resolve。Title 中 'Fix' 需 qualify 为 'necessary condition'。\"}\n  action_items:\n    - {round: 2, action: \"Title 和 Abstract 中将 'Fix' qualify 为 necessary condition 而非 sufficient fix；分析 generalized vs stagnant seeds 早期 dynamics 差异\", assigned_to: main_agent, status: pending}\n\n- id: W7\n  summary: \"重要相关工作遗漏（5 篇直接竞争/高度相关论文）\"\n  category: writing\n  severity: critical\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - {round: 1, note: \"Round 1 修复了 citation count (20→33) 和 Anonymous 问题\"}\n    - {round: 2, reviewers: [R2], note: \"5 篇重要遗漏：HCAPO (arXiv:2603.08754, ALFWorld 直接竞争), RC-GRPO (arXiv:2602.03025), iStar (arXiv:2509.19199), From Reasoning to Agentic survey (arXiv:2604.09459), EDGE-GRPO (arXiv:2507.21848)。特别是 HCAPO 在 ALFWorld+Qwen2.5-7B 上报告比 GRPO 高 13.8%。\"}\n  action_items:\n    - {round: 2, action: \"引用并讨论 5 篇论文，特别是 HCAPO 需在 Related Work 和 Experiments 中 position\", assigned_to: main_agent, status: pending}\n\n- id: W8\n  summary: \"Cell C 缺失使 factorial 不完整\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: [R1, R2], note: \"Cell C would isolate M2 without M1\"}\n    - {round: 1, action_taken: \"Cell C prediction in experiments.tex, crash record in appendix (6 runs, KL spike)\"}\n    - {round: 2, reviewers: [R1, R2], note: \"问题仍在。Cell C 正是隔离 M2 的关键——没有它无法独立确认 M2 影响。Cell C crash 本身说明 step-level advantage 在 full context 下行为可能质性不同。建议尝试 gradient clipping/advantage clipping 或更 prominently 讨论 gap 对结论的影响。\"}\n  action_items:\n    - {round: 2, action: \"尝试 gradient clipping per window 稳定 Cell C，或更显著讨论 Cell C 缺失对 M2 隔离结论的影响\", assigned_to: main_agent, status: pending}\n\n- id: W9\n  summary: \"REINFORCE++ 仅 15 步，对比可能不公平\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: [R1, R2], note: \"REINFORCE++ 12.5% may be undertrained\"}\n    - {round: 1, action_taken: \"Appendix: REINFORCE++ caveat added\"}\n    - {round: 2, reviewers: [R1], note: \"Caveat 已加但问题实质未解决。REINFORCE++ 是 episode-level 不受 sign misattribution 影响，无 critic 收敛本来就慢，15 步不足。\"}\n  action_items:\n    - {round: 2, action: \"延长 REINFORCE++ 训练至 30-50 步，或将结论定位为 'initial comparison'\", assigned_to: main_agent, status: pending}\n\n- id: W10\n  summary: \"Conclusion drops 'locally correct actions' qualifier on 80.9%\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 1, action_taken: \"Conclusion now uses '80.9% incorrect-sign updates under binary reward (52% measured under penalty reward)'\"}\n    - {round: 2, note: \"本轮未单独提及，已与 W2 合并处理\"}\n  resolution: \"Merged with W2 fix\"\n  resolution_round: 1\n\n- id: W11\n  summary: \"Eq.6 累积发散论证依赖 comparable magnitude 假设过强\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: [R1, R2], note: \"Simple conditional probability, lacks formal connection to divergence\"}\n    - {round: 1, action_taken: \"Cumulative divergence sketch added in theoretical_analysis.tex with Eq. biased_gradient\"}\n    - {round: 2, reviewers: [R1], note: \"Round 1 加了 Eq.6 但假设 'comparable magnitude' 过强。GRPO normalization 下成功 episode 的 advantage 量级系统性大于失败 episode（μ 较小时 r+-μ 远大于 0-μ）。一个大的 correct gradient 可能抵消多个小的 incorrect gradients，使 monotonic divergence 结论不成立。需要实际 advantage 分布数据或将 Eq.6 降级为 worst-case analysis。\"}\n  action_items:\n    - {round: 2, action: \"从实验日志提取 advantage 分布，分析 correct vs incorrect gradient 量级比；若无法证明量级可比，将 Eq.6 降级为 worst-case analysis\", assigned_to: main_agent, status: pending}\n\n- id: W12\n  summary: \"Table 1 报告标准不一致\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - {round: 1, reviewers: [R1, R2], note: \"best seed / best checkpoint / mean mixed\"}\n    - {round: 1, action_taken: \"Table 1 caption unified to 'best checkpoint per seed'\"}\n    - {round: 2, reviewers: [R1], note: \"Caption 改了但实际数据仍混用：Cell A 是 best seed，Cell B 是 best checkpoint (step 5)，Cell D 是 mean of two seeds。需统一为 mean±std 或全部 best checkpoint + mean。\"}\n  action_items:\n    - {round: 2, action: \"统一 Table 1 所有 conditions 的报告标准\", assigned_to: main_agent, status: pending}\n\n- id: R2-N1\n  summary: \"缺少与 HCAPO/Turn-PPO 等同期方法的实验对比\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - {round: 2, reviewers: [R2], note: \"Introduction 声称 'GiGPO, GAGPO, Turn-PPO address symptoms not root cause' 但无实验支撑。HCAPO 在 ALFWorld+Qwen2.5-7B 上比 GRPO 高 13.8%，直接竞争未引用。如果这些方法在 step-independent 下仍有效，核心论点被削弱。\"}\n  action_items:\n    - {round: 2, action: \"在 ALFWorld 上跑 Turn-PPO 或 HCAPO baseline；若无法实验则将强声明改为 hypothesis\", assigned_to: main_agent, status: pending}\n\n- id: R1-W5\n  summary: \"52.07% credit agreement rate 缺乏统计检验\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - {round: 2, reviewers: [R1], note: \"称 52.07% '与 50% 无异' 但未报告 binomial test p-value、样本量和 95% CI\"}\n  action_items:\n    - {round: 2, action: \"报告 credit agreement 样本量、binomial test p-value 和 95% CI\", assigned_to: main_agent, status: pending}\n\n- id: R1-W6\n  summary: \"SFT baseline 训练细节缺失\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - {round: 2, reviewers: [R1], note: \"2,546 demonstrations 来源（人工/GPT-4/rule-based）未说明，SFT 超参数未提供\"}\n  action_items:\n    - {round: 2, action: \"Appendix B 补充 SFT 训练细节：demonstration 来源和训练超参数\", assigned_to: main_agent, status: pending}\n\n- id: AUDIT-1\n  summary: \"Seed count inconsistency: 27% vs 36%\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 1, reviewers: [audit], note: \"5 locations had 27%, Table 2 clearly shows 4 G seeds.\"}\n    - {round: 1, action_taken: \"All 5 locations updated to 36%\"}\n    - {round: 2, note: \"本轮未提及，已修复确认\"}\n  resolution: \"All locations updated to 36%\"\n  resolution_round: 1\n\n- id: AUDIT-2\n  summary: \"Cell C described as 'degenerate' — incorrect\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 1, reviewers: [audit], note: \"method.tex claimed Cell C degenerate but was actually attempted\"}\n    - {round: 1, action_taken: \"'degenerate' removed, Cell C description updated\"}\n    - {round: 2, note: \"本轮未提及，已修复确认\"}\n  resolution: \"Corrected in all files\"\n  resolution_round: 1\n\n- id: R-add1\n  summary: \"Contribution 2 overclaim for single-seed evidence\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 1, action_taken: \"Downgraded to 'preliminary evidence'\"}\n    - {round: 2, note: \"本轮未单独提及，但 R2-W3 延续了类似关切\"}\n  resolution: \"Contribution 2 downgraded\"\n  resolution_round: 1\n\n- id: R-add2\n  summary: \"Table 2 needs anti-cherry-picking defense\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 1, action_taken: \"Table 7 in appendix with all seeds at step 5\"}\n    - {round: 2, note: \"本轮未提及，已修复确认\"}\n  resolution: \"Appendix table added\"\n  resolution_round: 1\n\n- id: R-add3\n  summary: \"seed2 classification boundary justification\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 1, action_taken: \"Table 2 caption: 'Seed2 achieves p=0.02, falling just outside p<0.01 threshold'\"}\n    - {round: 2, note: \"本轮未提及，已修复确认\"}\n  resolution: \"Caption updated\"\n  resolution_round: 1"
  }
}
```

</details>

---


### Tool result

_source line 235 · 2026-05-23T09:14:00.106763+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/review_issues.yaml\", \"bytes\": 11586}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 236 · 2026-05-23T09:16:34.479036+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "cost-verify-agent-rl",
  "report": "# 审稿报告 — Round 2 (Fresh Review)\n\n**论文**: Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Fix\n**Venue**: EMNLP 2026 (ARR May 2026 cycle, deadline 2026-05-25)\n**审稿模式**: Fresh（重新审稿）\n**Reviewer 编排**: 2 名 Reviewer（R1: 方法严谨性, R2: 新颖性/完整性）+ 视觉审查 Agent\n\n---\n\n## Summary\n\n本文诊断了多轮 agent RL 中 step-independent windowing 的两个结构性失败机制：(1) Policy Information Loss (M1)——截断上下文导致固定性能天花板；(2) Advantage Sign Misattribution (M2)——group normalization 下 advantage 符号反映 episode 结果而非局部动作质量，导致累积退化。在 p=12.5%, K=8 时，理论预测 binary reward 下 80.9% 梯度方向错误；penalty reward 下实测 52% credit agreement（≈随机）。通过 2×2 factorial 分离两个机制（实际为 3/4 cells，Cell C 未实现），展示 episode-level GRPO 解决两者。11-seed 评估显示 73% 避免 collapse 但仅 36% 实现统计显著 OOD 泛化。初步单 seed 8B（90.3% OOD）和 ScienceWorld 跨环境证据。\n\n---\n\n## Strengths\n\n**S1. 问题定位精准且有实际影响**。Step-independent windowing 是 RAGEN 等框架的默认配置，广泛使用但缺乏理论审视。将训练崩溃追溯到信用分配结构缺陷（而非超参数问题）对从业者有直接指导价值。\n\n**S2. 理论分析在假设范围内正确**。Proposition 2 的推导（P(correct|update) = p/[1-(1-p)^K]）逻辑清晰，数值验证一致。Figure 1 直观展示 sign error 随任务难度恶化的趋势。\n\n**S3. 诚实透明的多 seed 报告**。11-seed 评估揭示 collapsed/stagnant/generalized 三类结果分布，未 cherry-pick 最好 seed。Appendix 提供 step-5 统一评估表作为 anti-cherry-picking defense。\n\n**S4. Factorial 设计思路合理**。2×2 分离 observation scope 和 advantage granularity 的想法概念清晰，A→B→D 的 progression 叙事有效。\n\n**S5. 实践指导明确**。Discussion 中 \"use largest feasible h (h≥20); h≤10 collapses\" 的建议对社区有直接可操作价值。\n\n---\n\n## Weaknesses\n\n### Must-Fix（5 项，影响接收决定）\n\n**MF1 [R1+R2 共识] 理论预测 80.9% vs 实验测量 52% 的差距在主文中处理不当**\n- Abstract/Intro 将 80.9%（binary reward 理论值）和 52%（penalty reward 实测值）简单并列，给读者造成两者互相支持的印象，实际两者之间存在 28.9pp 差距。Gap 解释仅在 Appendix A.2（penalty-induced variance），主文无充分讨论。如果 penalty reward（实际系统常用）将 correct-sign rate 从 19.1% 提升到 52%，Proposition 2 的定量预测在实际系统下的指导意义需重新评估。\n- **建议**：(a) 在主文 Section 3 或 4.4 显著讨论差异；(b) 推导 penalty reward 修正公式或跑纯 binary 实验验证理论预测；(c) 考虑将标题数字改为实验值。\n- **Round 1 状态**：曾被标记并修复（加了并列呈现），但修复不充分，本轮两位 Reviewer 再次提出。\n\n**MF2 [R1 提出, R2 共识] Eq.6 累积发散论证的 \"comparable magnitude\" 假设过强**\n- Eq.6 假设 correct 和 incorrect gradient 量级相当，但 GRPO normalization 下成功 episode 的 advantage 量级系统性大于失败 episode（μ 较小时 r+−μ 远大于 0−μ）。一个大的 correct gradient 可能抵消多个小的 incorrect gradients，使 \"monotonic divergence\" 结论不成立。这从根本上影响论文的因果解释——sign misattribution 的实际影响可能从 \"active divergence\" 降级为 \"noisy convergence\"。\n- **建议**：(a) 从实验日志提取 advantage 分布数据分析量级比；(b) 若无法证明量级可比，将 Eq.6 降级为 worst-case analysis。\n\n**MF3 [R1+R2 共识] Factorial 设计不完整：Cell C 缺失 + 种子数不足**\n- 2×2 factorial 实际只有 3/4 cells。Cell C（full context + step-level advantage）正是独立隔离 M2 的关键——没有它，M2 的证据来自 A→B 对比（同时改变了 advantage granularity），存在混淆变量。Cell C 的 6 次 KL 崩溃本身说明 step-level advantage 在 full context 下行为可能质性不同。每个 condition 仅 2 seeds，在论文自己发现的高 seed variability（27% collapse, 36% stagnate, 36% generalize）下统计功效严重不足。\n- **建议**：(a) 尝试 gradient/advantage clipping 稳定 Cell C；(b) 增加 factorial seeds 至 5+；(c) 更显著讨论 Cell C 缺失对结论的具体影响。\n- **Round 1 状态**：曾被标记并修复（加了 Cell C crash record），但核心问题（实验不完整）未解决。\n\n**MF4 [R2 提出] 缺少与同期方法的实验对比**\n- Introduction 声称 \"GiGPO, GAGPO, Turn-PPO address symptoms but not the structural root cause: the windowing itself\"，但无实验支撑。特别是 **HCAPO** (Tan et al., 2026, arXiv:2603.08754) 在 ALFWorld + Qwen2.5-7B 上报告比 GRPO 高 13.8%，使用 step-level credit assignment 但取得良好效果——直接挑战 \"windowing itself is the problem\" 的核心论点，且未被引用。\n- **建议**：(a) 至少在 ALFWorld 上跑 Turn-PPO 或 HCAPO baseline；(b) 若无法实验对比，将强声明改为 hypothesis。\n- **新发现**：Round 2 新增。\n\n**MF5 [R2 提出, R1 部分共识] Episode-level \"Fix\" 的 seed 依赖严重 + 标题 overclaiming**\n- 11 seeds 中仅 4 个 (36%) 达到 p<0.01 显著 OOD 泛化——使用论文推荐的 fix 有 64% 概率无法获得有意义改进。Abstract 说 \"resolves both mechanisms\" 但实际只在少数 seed 上 resolve。Title 中 \"Fix\" 暗示可靠解决方案，与实际 36% 成功率不匹配。Stagnant vs. generalized seeds 的差异完全没有诊断分析。\n- **建议**：(a) Title/Abstract 中将 \"Fix\" qualify 为 \"necessary condition\"；(b) 分析 generalized vs stagnant seeds 早期 dynamics 差异；(c) 讨论 seed selection 策略。\n\n### Should-Fix（7 项，影响评分但不一票否决）\n\n**SF1 [R1] Definition 1 操作化存在逻辑循环**。Section 4.4 用 \"成功 episode 中所有 valid action windows\" 操作化 \"locally correct\"，恰好犯了论文所批评的错误——用 episode outcome 替代 local quality。建议讨论近似局限性。\n\n**SF2 [R1] Window-size cliff 基于 single seed**。鉴于高 seed variability，\"cliff\" 措辞过强，建议改为 \"preliminary observation\" 或增加 3+ seeds 验证。Round 1 已加 caveat 但措辞仍不匹配。\n\n**SF3 [R1] REINFORCE++ 仅 15 步，对比不公平**。REINFORCE++ 是 episode-level（不受 M2 影响），无 critic 收敛本来就慢。建议延长至 30-50 步或定位为 \"initial comparison\"。\n\n**SF4 [R1] Table 1 报告标准不一致**。Cell A: best seed, Cell B: best checkpoint (step 5), Cell D: mean of two seeds——同表混用三种标准。建议统一。Round 1 改了 caption 但数据仍混用。\n\n**SF5 [R1] 52.07% credit agreement 缺乏统计检验**。未报告样本量、binomial test p-value 和 95% CI。\"与 50% 无异\" 需统计证据支撑。\n\n**SF6 [R1] SFT baseline 训练细节缺失**。2,546 demonstrations 来源（人工/GPT-4/rule-based）和 SFT 训练超参数均未提供。\n\n**SF7 [R2] 5 篇重要相关工作遗漏**：HCAPO (arXiv:2603.08754), RC-GRPO (arXiv:2602.03025), iStar (arXiv:2509.19199), From Reasoning to Agentic survey (arXiv:2604.09459), EDGE-GRPO (arXiv:2507.21848)。\n\n### Minor（5 项）\n\n- **m1**: 术语不一致：\"step-independent\" / \"step-level windowing\" / \"window-level\" 混用\n- **m2**: Definition 1 \"locally correct\" vs Proposition 2 proof \"locally good actions\" 术语切换\n- **m3**: Section 3 \"effective learning rate 12.6%\"——实算 0.656×0.191=12.5%，有微小 rounding inconsistency\n- **m4**: ScienceWorld Section 4.7 中 baseline 30.1% vs restricting context \"34.8% to 4.5%\"——30.1% 和 34.8% 似为不同指标，未说明\n- **m5**: Figure 3 和 Figure 4(b) 使用红/绿配色，对色盲读者不友好\n\n---\n\n## Reviewer Consensus\n\n两位 Reviewer 在以下关键问题上达成共识 [AGREE]：\n\n1. **80.9% vs 52% gap**（MF1）：理论与实验的差距在主文中处理不当，需要更显著的讨论\n2. **Cell C 缺失**（MF3）：factorial 设计因此不完整，论文目前对此 gap 的讨论不够充分\n3. **Single-seed 跨规模/跨环境证据**：\"preliminary\" 标注已加但仍需更多 seeds\n4. **Fix 无方法论新颖性**：episode-level GRPO 就是原始 GRPO 设计\n5. **诊断贡献有价值**：问题 formalization 清晰，对社区有实际指导意义\n6. **Overall 3.0 (Findings)**：适合 Findings 接收但不够 Conference\n\n## Reviewer Divergence\n\n两位 Reviewer 在以下方面有不同侧重（互补而非矛盾）：\n\n| 维度 | R1 | R2 |\n|------|----|----|\n| Soundness | 2.5/5（更严格） | 3.5/5 |\n| Excitement | 3.5/5 | 2.5/5（更严格） |\n| 关注焦点 | 数学严谨性（Eq.6 假设、Definition 循环） | 竞争性对比（HCAPO 遗漏）和 framing |\n\nR1 认为理论部分的严谨性问题（Eq.6 假设过强）比 R2 更严重（critical vs 未特别关注）。R2 认为缺少实验对比（HCAPO）比 R1 更严重（critical vs 未提及）。两者互补——方法论和定位均需改进。\n\n---\n\n## Questions（需要作者澄清）\n\n1. Proposition 2 预测 binary 下 80.9% incorrect sign，实测 penalty 下 52% agreement。是否可在 penalty reward 下推导 closed-form P(correct|update)？如果 penalty 从 0 增大到 0.1，P(correct) 如何变化？\n2. Eq.6 的 comparable magnitude 假设——实验日志中 successful vs failed episode 的平均 |Â| 比值是多少？\n3. Cell C 的 KL 崩溃是否尝试过 gradient clipping per window / advantage clipping / PPO clipping？\n4. Credit agreement 52.07% 的样本量和 binomial test p-value？\n5. 4 个 generalized seeds 之间是否存在共同特征（初始 loss、早期 gradient norm）？可否设计 early stopping 策略？\n6. HCAPO 在 ALFWorld+Qwen2.5-7B 上比 GRPO 高 13.8% 且用 step-level credit——是否意味着 step-level credit 在好的 assignment 策略下可行？核心论点需如何修正？\n7. Episode-level vs h=2 的实际 wall-clock 时间比？O(T²) attention cost 是重要实际障碍。\n\n---\n\n## Missing References\n\n1. **HCAPO** — Tan et al., 2026. \"Hindsight Credit Assignment for Long-Horizon LLM Agents.\" arXiv:2603.08754. **[直接竞争——ALFWorld 实验，step-level credit 取得好效果]**\n2. **RC-GRPO** — Feb 2026. arXiv:2602.03025. **[GRPO variance collapse, 与 M2 高度相关]**\n3. **iStar** — Liu et al., 2025. arXiv:2509.19199. **[Implicit step rewards, WebShop SOTA]**\n4. **\"From Reasoning to Agentic\" survey** — April 2026. arXiv:2604.09459. **[47 篇 credit assignment 综述，应 position]**\n5. **EDGE-GRPO** — 2025. arXiv:2507.21848. **[Advantage collapse 直接相关]**\n\n---\n\n## External Review\n\n**状态**：未配置。项目配置中未启用外部审稿（paperreview.ai）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查 Agent 已完成（2 warning, 5 info，0 critical）。\n\n**Warnings:**\n- **Pages 1-3 无 display item**：首个 figure 在第 4 页。审稿人前 2 分钟只看到文字和公式，缺少视觉锚点。建议将 Figure 1（理论曲线）或概念架构图提前到 page 2。\n- **Page 13 底部约 1/3 空白**：Table 5 下方，可调整 float 位置或上移 Figure 4/5 填充。\n\n**Info:**\n- Figure 3 和 Figure 4(b) 使用红/绿配色，对色盲读者不友好，建议改用 blue/orange 或 Okabe-Ito 色板\n- Page 4 脚注 GitHub 链接 (RAGEN-AI/RAGEN)，若作者与 RAGEN 相关可能违反匿名规则\n- Table 2 字号偏小但仍可读\n- 附录末页内容约 60%，底部有空白（影响较小）\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.0 — Findings**\n\n| 维度 | R1 | R2 | 综合 |\n|------|----|----|------|\n| Soundness | 2.5 | 3.5 | 3.0 |\n| Excitement | 3.5 | 2.5 | 3.0 |\n| Reproducibility | 2.5 | 4.0 | 3.0 |\n| Confidence | 4/5 | 4/5 | 4/5 |\n\n**综合评价**：\n\n本文提出了一个有价值的诊断——step-independent windowing 在多轮 agent RL 中引入结构性信用分配缺陷，将散见于多个工作的训练失败统一为两个可分离机制（information loss + sign misattribution）。问题 formalization 清晰，多 seed 报告诚实。\n\n但论文存在多个影响接收级别的问题：(1) 理论核心数字 80.9% 与实验测量 52% 的差距在主文中处理不当；(2) Eq.6 累积发散论证依赖过强假设；(3) factorial 因 Cell C 缺失而不完整且种子数不足；(4) 缺少与 HCAPO 等直接竞争方法的实验对比；(5) \"Fix\" 仅 36% seed 泛化但标题/abstract overclaiming。\n\n**建议**：适合 EMNLP 2026 Findings 接收。距 Conference 级别需要：(a) 补充与 HCAPO/Turn-PPO 的实验对比；(b) 解决 Eq.6 假设问题；(c) 增加 factorial seeds；(d) 更诚实地 qualify \"Fix\" 的可靠性。\n\n---\n\n## Detailed Comments（逐节）\n\n### Abstract\n- \"theory predicts 80.9%...empirical measurement...yields a 52% credit agreement rate\" 并列呈现两个实际上有 28.9pp 差距的数字，需要在首次出现时说明一个是 binary 理论值一个是 penalty 实测值\n- \"resolves both mechanisms\" 过强——仅 36% seed 达到显著泛化\n\n### Introduction\n- P1: 清晰的问题引出，从 framework default 到 training instability 的叙事有效\n- P2: \"Concurrent methods...address symptoms but not the structural root cause\" 缺乏实验支撑，HCAPO 在 ALFWorld 上的结果可能反驳此声明\n- P3: \"Our primary contribution is diagnostic\" 定位合理\n- Contribution 2: \"preliminary cross-scale...evidence\" 措辞已降级，但 abstract 中 \"90.3% OOD\" 仍给人强印象\n\n### Method (Section 2)\n- 2.1-2.3: 问题 formulation 和 dual mechanism 分析清晰\n- 2.4: Episode-level training 描述准确——\"not a new method, but the original GRPO design\"\n- 2.5: Cell C 描述需更显著讨论缺失的后果\n\n### Theoretical Analysis (Section 3)\n- Proposition 1, 2: 推导在 binary reward 假设下正确\n- Eq.6: \"comparable magnitude\" 假设过强，需降级或提供实证支持\n- \"effective learning rate 12.6%\"——应为 12.5%（rounding）\n- Reward saturation 分析有价值\n\n### Experiments (Section 4)\n- 4.1 Setup: SFT baseline 缺训练细节（demonstration 来源、超参数）\n- 4.2 Factorial: Cell C 缺失问题；2 seeds/condition 不足\n- 4.3 Results: Table 1 报告标准不一致\n- 4.4 Sign Verification: 52% credit agreement 需统计检验\n- 4.5 Seed Variability: 诚实报告，但缺少 generalized vs stagnant seeds 的诊断分析\n- 4.6 Cross-Scale: Single seed，abstract 呈现过强\n- 4.7 Cross-Environment: 只有 Cell A collapse，缺 Cell D recovery；30.1% vs 34.8% 差异未说明\n\n### Related Work (Section 5)\n- 遗漏 5 篇重要相关工作（见 Missing References）\n- 术语不一致需统一\n\n### Discussion (Section 6)\n- Practitioner guidance 有价值\n- Seed-dependent transfer 的讨论诚实但缺深度\n\n### Limitations\n- 覆盖 3 个点（环境/规模局限、seed dependency、长 episode 限制），符合 EMNLP 要求\n- 可补充 penalty reward 下理论适用性的局限",
  "reviewer_ids_acknowledged": "[\"1\", \"2\"]",
  "cross_response_reviewer_ids": "[\"1\", \"2\"]",
  "overall_score": "3.0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "project": "cost-verify-agent-rl",
    "report": "# 审稿报告 — Round 2 (Fresh Review)\n\n**论文**: Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Fix\n**Venue**: EMNLP 2026 (ARR May 2026 cycle, deadline 2026-05-25)\n**审稿模式**: Fresh（重新审稿）\n**Reviewer 编排**: 2 名 Reviewer（R1: 方法严谨性, R2: 新颖性/完整性）+ 视觉审查 Agent\n\n---\n\n## Summary\n\n本文诊断了多轮 agent RL 中 step-independent windowing 的两个结构性失败机制：(1) Policy Information Loss (M1)——截断上下文导致固定性能天花板；(2) Advantage Sign Misattribution (M2)——group normalization 下 advantage 符号反映 episode 结果而非局部动作质量，导致累积退化。在 p=12.5%, K=8 时，理论预测 binary reward 下 80.9% 梯度方向错误；penalty reward 下实测 52% credit agreement（≈随机）。通过 2×2 factorial 分离两个机制（实际为 3/4 cells，Cell C 未实现），展示 episode-level GRPO 解决两者。11-seed 评估显示 73% 避免 collapse 但仅 36% 实现统计显著 OOD 泛化。初步单 seed 8B（90.3% OOD）和 ScienceWorld 跨环境证据。\n\n---\n\n## Strengths\n\n**S1. 问题定位精准且有实际影响**。Step-independent windowing 是 RAGEN 等框架的默认配置，广泛使用但缺乏理论审视。将训练崩溃追溯到信用分配结构缺陷（而非超参数问题）对从业者有直接指导价值。\n\n**S2. 理论分析在假设范围内正确**。Proposition 2 的推导（P(correct|update) = p/[1-(1-p)^K]）逻辑清晰，数值验证一致。Figure 1 直观展示 sign error 随任务难度恶化的趋势。\n\n**S3. 诚实透明的多 seed 报告**。11-seed 评估揭示 collapsed/stagnant/generalized 三类结果分布，未 cherry-pick 最好 seed。Appendix 提供 step-5 统一评估表作为 anti-cherry-picking defense。\n\n**S4. Factorial 设计思路合理**。2×2 分离 observation scope 和 advantage granularity 的想法概念清晰，A→B→D 的 progression 叙事有效。\n\n**S5. 实践指导明确**。Discussion 中 \"use largest feasible h (h≥20); h≤10 collapses\" 的建议对社区有直接可操作价值。\n\n---\n\n## Weaknesses\n\n### Must-Fix（5 项，影响接收决定）\n\n**MF1 [R1+R2 共识] 理论预测 80.9% vs 实验测量 52% 的差距在主文中处理不当**\n- Abstract/Intro 将 80.9%（binary reward 理论值）和 52%（penalty reward 实测值）简单并列，给读者造成两者互相支持的印象，实际两者之间存在 28.9pp 差距。Gap 解释仅在 Appendix A.2（penalty-induced variance），主文无充分讨论。如果 penalty reward（实际系统常用）将 correct-sign rate 从 19.1% 提升到 52%，Proposition 2 的定量预测在实际系统下的指导意义需重新评估。\n- **建议**：(a) 在主文 Section 3 或 4.4 显著讨论差异；(b) 推导 penalty reward 修正公式或跑纯 binary 实验验证理论预测；(c) 考虑将标题数字改为实验值。\n- **Round 1 状态**：曾被标记并修复（加了并列呈现），但修复不充分，本轮两位 Reviewer 再次提出。\n\n**MF2 [R1 提出, R2 共识] Eq.6 累积发散论证的 \"comparable magnitude\" 假设过强**\n- Eq.6 假设 correct 和 incorrect gradient 量级相当，但 GRPO normalization 下成功 episode 的 advantage 量级系统性大于失败 episode（μ 较小时 r+−μ 远大于 0−μ）。一个大的 correct gradient 可能抵消多个小的 incorrect gradients，使 \"monotonic divergence\" 结论不成立。这从根本上影响论文的因果解释——sign misattribution 的实际影响可能从 \"active divergence\" 降级为 \"noisy convergence\"。\n- **建议**：(a) 从实验日志提取 advantage 分布数据分析量级比；(b) 若无法证明量级可比，将 Eq.6 降级为 worst-case analysis。\n\n**MF3 [R1+R2 共识] Factorial 设计不完整：Cell C 缺失 + 种子数不足**\n- 2×2 factorial 实际只有 3/4 cells。Cell C（full context + step-level advantage）正是独立隔离 M2 的关键——没有它，M2 的证据来自 A→B 对比（同时改变了 advantage granularity），存在混淆变量。Cell C 的 6 次 KL 崩溃本身说明 step-level advantage 在 full context 下行为可能质性不同。每个 condition 仅 2 seeds，在论文自己发现的高 seed variability（27% collapse, 36% stagnate, 36% generalize）下统计功效严重不足。\n- **建议**：(a) 尝试 gradient/advantage clipping 稳定 Cell C；(b) 增加 factorial seeds 至 5+；(c) 更显著讨论 Cell C 缺失对结论的具体影响。\n- **Round 1 状态**：曾被标记并修复（加了 Cell C crash record），但核心问题（实验不完整）未解决。\n\n**MF4 [R2 提出] 缺少与同期方法的实验对比**\n- Introduction 声称 \"GiGPO, GAGPO, Turn-PPO address symptoms but not the structural root cause: the windowing itself\"，但无实验支撑。特别是 **HCAPO** (Tan et al., 2026, arXiv:2603.08754) 在 ALFWorld + Qwen2.5-7B 上报告比 GRPO 高 13.8%，使用 step-level credit assignment 但取得良好效果——直接挑战 \"windowing itself is the problem\" 的核心论点，且未被引用。\n- **建议**：(a) 至少在 ALFWorld 上跑 Turn-PPO 或 HCAPO baseline；(b) 若无法实验对比，将强声明改为 hypothesis。\n- **新发现**：Round 2 新增。\n\n**MF5 [R2 提出, R1 部分共识] Episode-level \"Fix\" 的 seed 依赖严重 + 标题 overclaiming**\n- 11 seeds 中仅 4 个 (36%) 达到 p<0.01 显著 OOD 泛化——使用论文推荐的 fix 有 64% 概率无法获得有意义改进。Abstract 说 \"resolves both mechanisms\" 但实际只在少数 seed 上 resolve。Title 中 \"Fix\" 暗示可靠解决方案，与实际 36% 成功率不匹配。Stagnant vs. generalized seeds 的差异完全没有诊断分析。\n- **建议**：(a) Title/Abstract 中将 \"Fix\" qualify 为 \"necessary condition\"；(b) 分析 generalized vs stagnant seeds 早期 dynamics 差异；(c) 讨论 seed selection 策略。\n\n### Should-Fix（7 项，影响评分但不一票否决）\n\n**SF1 [R1] Definition 1 操作化存在逻辑循环**。Section 4.4 用 \"成功 episode 中所有 valid action windows\" 操作化 \"locally correct\"，恰好犯了论文所批评的错误——用 episode outcome 替代 local quality。建议讨论近似局限性。\n\n**SF2 [R1] Window-size cliff 基于 single seed**。鉴于高 seed variability，\"cliff\" 措辞过强，建议改为 \"preliminary observation\" 或增加 3+ seeds 验证。Round 1 已加 caveat 但措辞仍不匹配。\n\n**SF3 [R1] REINFORCE++ 仅 15 步，对比不公平**。REINFORCE++ 是 episode-level（不受 M2 影响），无 critic 收敛本来就慢。建议延长至 30-50 步或定位为 \"initial comparison\"。\n\n**SF4 [R1] Table 1 报告标准不一致**。Cell A: best seed, Cell B: best checkpoint (step 5), Cell D: mean of two seeds——同表混用三种标准。建议统一。Round 1 改了 caption 但数据仍混用。\n\n**SF5 [R1] 52.07% credit agreement 缺乏统计检验**。未报告样本量、binomial test p-value 和 95% CI。\"与 50% 无异\" 需统计证据支撑。\n\n**SF6 [R1] SFT baseline 训练细节缺失**。2,546 demonstrations 来源（人工/GPT-4/rule-based）和 SFT 训练超参数均未提供。\n\n**SF7 [R2] 5 篇重要相关工作遗漏**：HCAPO (arXiv:2603.08754), RC-GRPO (arXiv:2602.03025), iStar (arXiv:2509.19199), From Reasoning to Agentic survey (arXiv:2604.09459), EDGE-GRPO (arXiv:2507.21848)。\n\n### Minor（5 项）\n\n- **m1**: 术语不一致：\"step-independent\" / \"step-level windowing\" / \"window-level\" 混用\n- **m2**: Definition 1 \"locally correct\" vs Proposition 2 proof \"locally good actions\" 术语切换\n- **m3**: Section 3 \"effective learning rate 12.6%\"——实算 0.656×0.191=12.5%，有微小 rounding inconsistency\n- **m4**: ScienceWorld Section 4.7 中 baseline 30.1% vs restricting context \"34.8% to 4.5%\"——30.1% 和 34.8% 似为不同指标，未说明\n- **m5**: Figure 3 和 Figure 4(b) 使用红/绿配色，对色盲读者不友好\n\n---\n\n## Reviewer Consensus\n\n两位 Reviewer 在以下关键问题上达成共识 [AGREE]：\n\n1. **80.9% vs 52% gap**（MF1）：理论与实验的差距在主文中处理不当，需要更显著的讨论\n2. **Cell C 缺失**（MF3）：factorial 设计因此不完整，论文目前对此 gap 的讨论不够充分\n3. **Single-seed 跨规模/跨环境证据**：\"preliminary\" 标注已加但仍需更多 seeds\n4. **Fix 无方法论新颖性**：episode-level GRPO 就是原始 GRPO 设计\n5. **诊断贡献有价值**：问题 formalization 清晰，对社区有实际指导意义\n6. **Overall 3.0 (Findings)**：适合 Findings 接收但不够 Conference\n\n## Reviewer Divergence\n\n两位 Reviewer 在以下方面有不同侧重（互补而非矛盾）：\n\n| 维度 | R1 | R2 |\n|------|----|----|\n| Soundness | 2.5/5（更严格） | 3.5/5 |\n| Excitement | 3.5/5 | 2.5/5（更严格） |\n| 关注焦点 | 数学严谨性（Eq.6 假设、Definition 循环） | 竞争性对比（HCAPO 遗漏）和 framing |\n\nR1 认为理论部分的严谨性问题（Eq.6 假设过强）比 R2 更严重（critical vs 未特别关注）。R2 认为缺少实验对比（HCAPO）比 R1 更严重（critical vs 未提及）。两者互补——方法论和定位均需改进。\n\n---\n\n## Questions（需要作者澄清）\n\n1. Proposition 2 预测 binary 下 80.9% incorrect sign，实测 penalty 下 52% agreement。是否可在 penalty reward 下推导 closed-form P(correct|update)？如果 penalty 从 0 增大到 0.1，P(correct) 如何变化？\n2. Eq.6 的 comparable magnitude 假设——实验日志中 successful vs failed episode 的平均 |Â| 比值是多少？\n3. Cell C 的 KL 崩溃是否尝试过 gradient clipping per window / advantage clipping / PPO clipping？\n4. Credit agreement 52.07% 的样本量和 binomial test p-value？\n5. 4 个 generalized seeds 之间是否存在共同特征（初始 loss、早期 gradient norm）？可否设计 early stopping 策略？\n6. HCAPO 在 ALFWorld+Qwen2.5-7B 上比 GRPO 高 13.8% 且用 step-level credit——是否意味着 step-level credit 在好的 assignment 策略下可行？核心论点需如何修正？\n7. Episode-level vs h=2 的实际 wall-clock 时间比？O(T²) attention cost 是重要实际障碍。\n\n---\n\n## Missing References\n\n1. **HCAPO** — Tan et al., 2026. \"Hindsight Credit Assignment for Long-Horizon LLM Agents.\" arXiv:2603.08754. **[直接竞争——ALFWorld 实验，step-level credit 取得好效果]**\n2. **RC-GRPO** — Feb 2026. arXiv:2602.03025. **[GRPO variance collapse, 与 M2 高度相关]**\n3. **iStar** — Liu et al., 2025. arXiv:2509.19199. **[Implicit step rewards, WebShop SOTA]**\n4. **\"From Reasoning to Agentic\" survey** — April 2026. arXiv:2604.09459. **[47 篇 credit assignment 综述，应 position]**\n5. **EDGE-GRPO** — 2025. arXiv:2507.21848. **[Advantage collapse 直接相关]**\n\n---\n\n## External Review\n\n**状态**：未配置。项目配置中未启用外部审稿（paperreview.ai）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查 Agent 已完成（2 warning, 5 info，0 critical）。\n\n**Warnings:**\n- **Pages 1-3 无 display item**：首个 figure 在第 4 页。审稿人前 2 分钟只看到文字和公式，缺少视觉锚点。建议将 Figure 1（理论曲线）或概念架构图提前到 page 2。\n- **Page 13 底部约 1/3 空白**：Table 5 下方，可调整 float 位置或上移 Figure 4/5 填充。\n\n**Info:**\n- Figure 3 和 Figure 4(b) 使用红/绿配色，对色盲读者不友好，建议改用 blue/orange 或 Okabe-Ito 色板\n- Page 4 脚注 GitHub 链接 (RAGEN-AI/RAGEN)，若作者与 RAGEN 相关可能违反匿名规则\n- Table 2 字号偏小但仍可读\n- 附录末页内容约 60%，底部有空白（影响较小）\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.0 — Findings**\n\n| 维度 | R1 | R2 | 综合 |\n|------|----|----|------|\n| Soundness | 2.5 | 3.5 | 3.0 |\n| Excitement | 3.5 | 2.5 | 3.0 |\n| Reproducibility | 2.5 | 4.0 | 3.0 |\n| Confidence | 4/5 | 4/5 | 4/5 |\n\n**综合评价**：\n\n本文提出了一个有价值的诊断——step-independent windowing 在多轮 agent RL 中引入结构性信用分配缺陷，将散见于多个工作的训练失败统一为两个可分离机制（information loss + sign misattribution）。问题 formalization 清晰，多 seed 报告诚实。\n\n但论文存在多个影响接收级别的问题：(1) 理论核心数字 80.9% 与实验测量 52% 的差距在主文中处理不当；(2) Eq.6 累积发散论证依赖过强假设；(3) factorial 因 Cell C 缺失而不完整且种子数不足；(4) 缺少与 HCAPO 等直接竞争方法的实验对比；(5) \"Fix\" 仅 36% seed 泛化但标题/abstract overclaiming。\n\n**建议**：适合 EMNLP 2026 Findings 接收。距 Conference 级别需要：(a) 补充与 HCAPO/Turn-PPO 的实验对比；(b) 解决 Eq.6 假设问题；(c) 增加 factorial seeds；(d) 更诚实地 qualify \"Fix\" 的可靠性。\n\n---\n\n## Detailed Comments（逐节）\n\n### Abstract\n- \"theory predicts 80.9%...empirical measurement...yields a 52% credit agreement rate\" 并列呈现两个实际上有 28.9pp 差距的数字，需要在首次出现时说明一个是 binary 理论值一个是 penalty 实测值\n- \"resolves both mechanisms\" 过强——仅 36% seed 达到显著泛化\n\n### Introduction\n- P1: 清晰的问题引出，从 framework default 到 training instability 的叙事有效\n- P2: \"Concurrent methods...address symptoms but not the structural root cause\" 缺乏实验支撑，HCAPO 在 ALFWorld 上的结果可能反驳此声明\n- P3: \"Our primary contribution is diagnostic\" 定位合理\n- Contribution 2: \"preliminary cross-scale...evidence\" 措辞已降级，但 abstract 中 \"90.3% OOD\" 仍给人强印象\n\n### Method (Section 2)\n- 2.1-2.3: 问题 formulation 和 dual mechanism 分析清晰\n- 2.4: Episode-level training 描述准确——\"not a new method, but the original GRPO design\"\n- 2.5: Cell C 描述需更显著讨论缺失的后果\n\n### Theoretical Analysis (Section 3)\n- Proposition 1, 2: 推导在 binary reward 假设下正确\n- Eq.6: \"comparable magnitude\" 假设过强，需降级或提供实证支持\n- \"effective learning rate 12.6%\"——应为 12.5%（rounding）\n- Reward saturation 分析有价值\n\n### Experiments (Section 4)\n- 4.1 Setup: SFT baseline 缺训练细节（demonstration 来源、超参数）\n- 4.2 Factorial: Cell C 缺失问题；2 seeds/condition 不足\n- 4.3 Results: Table 1 报告标准不一致\n- 4.4 Sign Verification: 52% credit agreement 需统计检验\n- 4.5 Seed Variability: 诚实报告，但缺少 generalized vs stagnant seeds 的诊断分析\n- 4.6 Cross-Scale: Single seed，abstract 呈现过强\n- 4.7 Cross-Environment: 只有 Cell A collapse，缺 Cell D recovery；30.1% vs 34.8% 差异未说明\n\n### Related Work (Section 5)\n- 遗漏 5 篇重要相关工作（见 Missing References）\n- 术语不一致需统一\n\n### Discussion (Section 6)\n- Practitioner guidance 有价值\n- Seed-dependent transfer 的讨论诚实但缺深度\n\n### Limitations\n- 覆盖 3 个点（环境/规模局限、seed dependency、长 episode 限制），符合 EMNLP 要求\n- 可补充 penalty reward 下理论适用性的局限",
    "reviewer_ids_acknowledged": "[\"1\", \"2\"]",
    "cross_response_reviewer_ids": "[\"1\", \"2\"]",
    "overall_score": "3.0"
  }
}
```

</details>

---


### Tool result

_source line 237 · 2026-05-23T09:16:38.844616+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_4ebf0fb2d0159caa355a1a855f5ac59f:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4365
}
```

</details>

---


### Assistant

_source line 238 · 2026-05-23T09:16:48.576266+00:00_

审稿报告已投递。

**Round 2 审稿完成**，结果摘要：

- **Overall: 3.0 (Findings)**，两位 Reviewer 一致
- **5 个 Must-Fix**：(1) 80.9% vs 52% 理论/实验差距主文处理不当；(2) Eq.6 comparable magnitude 假设过强；(3) Factorial Cell C 缺失 + 种子不足；(4) 缺少与 HCAPO 等同期方法的实验对比；(5) "Fix" overclaiming（36% seed 泛化）
- **7 个 Should-Fix**：Definition 1 操作化循环、h-sweep cliff 单 seed、REINFORCE++ 对比不公平、Table 1 标准不一致、52% 缺统计检验、SFT 细节缺失、5 篇 missing references
- **Issue Tracker 已同步**：Round 1 的 16 个 issue 中 6 个确认 resolved，10 个在 Round 2 重新出现或演化为新形式，另新增 3 个 issue

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director"
}
```

</details>

---


## Round 19

## Round 19

2 recorded events


### User

_source line 239 · 2026-05-23T09:16:48.583680+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 对 Reviewer 2 审稿意见的交叉回应

---

## Must-Fix 回应

**[AGREE] R2-N1: 缺少与同期方法的实验对比**

同意这是一个重要缺陷，但严重程度我评为 should-fix 而非 must-fix。

理由：论文在 Introduction 中做出了明确的因果声明——"GiGPO, GAGPO, Turn-PPO address symptoms but not the structural root cause: the windowing itself"（Section 1, page 1）——但全文没有任何实验数据支撑这个声明。这属于 unsupported claim。

不过我认为严重程度应降至 should-fix，原因是：(a) 论文的核心贡献定位为 diagnostic 而非 method，所以不需要 SOTA comparison；(b) 这些都是 concurrent work，要求全部复现不现实；(c) 但至少应该对 1-2 个代表性方法（如 Turn-PPO 或 GiGPO）提供实验对比，或者将 "address symptoms" 的声明弱化为 hypothesis 而非 conclusion。

关于 HCAPO 遗漏：我无法独立验证这篇论文的具体内容，但如果它确实在 ALFWorld + Qwen 上直接报告了结果，则属于高度相关的 concurrent work，应当引用并讨论。

**[AGREE] R2-N2: Seed 依赖严重且 "Fix" 措辞过强**

同意，但补充更精确的分析。

论文标题包含 "Episode-Level Fix"，Abstract 说 "resolves both mechanisms"。从技术层面看，episode-level GRPO 确实**结构性地**消除了 M1（恢复完整上下文）和 M2（统一 advantage 消除 window-level sign error），这个声明在**机制层面**是准确的。但 "Fix" 一词在读者理解中意味着 "解决了训练问题"，而 36% 的 OOD 泛化率和 27% 的 collapse 率说明 episode-level GRPO 远非可靠的解决方案。

论文 Contribution 3 确实写了 "necessary but not sufficient"（Section 1, page 2），说明作者意识到了这个问题。但 Abstract 和标题的措辞更为绝对化，与正文的 nuanced 讨论不一致。

建议：标题中 "Fix" 应改为更中性的措辞（如 "Episode-Level Resolution" 或 "Episode-Level Remedy"），Abstract 中 "resolves both mechanisms" 应限定为 "structurally eliminates both mechanisms but does not guarantee generalization"。

---

## Should-Fix 回应

**[AGREE] R2-W1: Cell C 缺失削弱 factorial 完整性**

完全同意，与我的 N3 一致。补充一个 R2 未提到的角度：Cell C 的 KL 崩溃本身可能提供了关于 M2 的重要信息。如果 full context + step-level advantage 总是导致 KL 崩溃，这可能意味着 M2 在 full context 下的行为模式与在 truncated context 下**质性不同**——不是简单的 sign error，而是 advantage magnitude 爆炸。这与论文将 M2 描述为 "sign 问题" 的框架不完全吻合，值得在论文中讨论。

**[AGREE] R2-W2: 80.9% vs 52% gap 需更深入分析**

完全同意，与我的 N1 一致。我在自己的审稿中将此列为 critical，因为这是 Abstract 的标题数字。

**[AGREE] R2-W3: 跨规模/跨环境证据太弱**

同意。补充一个 R2 已指出但值得强调的点：ScienceWorld 实验仅展示了 Cell A 的 collapse，**没有 Cell D 的 recovery**。这意味着 ScienceWorld 只验证了 "step-independent training fails"（已知现象），没有验证 "episode-level training fixes it"（论文核心声明）。单方面的验证不构成 "cross-environment validation"。

不过论文在 Section 4.7 末尾诚实地写了 "These single-seed results provide preliminary evidence... multi-seed and multi-environment verification would strengthen this claim"（page 6），措辞已经是 preliminary。

**[PARTIALLY AGREE] R2-W4: 重要相关工作遗漏**

我无法独立验证 HCAPO、RC-GRPO、iStar、EDGE-GRPO 等论文的具体内容和发表状态。如果这些是 2025-2026 年的 arXiv preprints 且与 step-independent windowing / GRPO credit assignment 直接相关，则确实应当引用。但 Related Work (Section 5, page 7) 已经覆盖了较广泛的类别（multi-turn credit methods, GRPO collapse phenomena），所以这更多是补充性的而非结构性缺陷。

建议作者检查 R2 列出的每篇论文，将相关的加入 Related Work 讨论。

---

## Minor 回应

**[AGREE] 术语不一致**：确认论文中 "step-independent" / "step-level windowing" / "window-level" 确实在不同位置混用。Section 2.2 用 "step-independent training"，Section 2.3.2 用 "step-independent training"，但 Section 1 用 "step-independent windowing"，Table 1 用 "step" 作为 advantage granularity 标签。应统一为一个主术语。

**[AGREE] seed1 checkpoint 丢失**：Table 2 footnote 标注 seed1 用 RAGEN built-in eval 且 checkpoint 不可用。这确实影响 reproducibility，因为 seed1 是 generalized 类别中最先报告的 seed。

**[AGREE] Definition 1 术语切换**：Definition 1 用 "locally correct"，Proposition 2 proof 切换为 "locally good actions"——这两个术语是否等价？如果等价应统一；如果不等价应区分。

**[AGREE] Table 5 数据缺失**：Appendix E (Table 5) 中 seed2, seed4, seed5 的 OOD 数据为 "---"，seed2048, seed200 的 ID 数据也为 "---"。缺失率约 40%，削弱了 unified step-5 evaluation 作为 anti-cherry-picking 措施的有效性。

---

## 对 R2 Overall Assessment 的回应

R2 给出 Overall 3.0 (Findings)，Soundness 3.5，Excitement 2.5。

我的评分是 Overall 3.0，Soundness 2.5，Excitement 3.5。

**关于 Soundness 差异（R2: 3.5 vs 我: 2.5）**：我认为 R2 可能对 Eq. 6 的 comparable magnitude 假设和 theory-experiment gap 的评估偏宽松。Proposition 2 推导本身无误，但 Eq. 6 的累积发散论证是论文因果叙事的关键环节，其依赖的假设在 GRPO normalization 下几乎必然不成立（我的 N2），这显著影响 soundness。

**关于 Excitement 差异（R2: 2.5 vs 我: 3.5）**：R2 给低 excitement 可能因为 fix 不新颖（回到原始 GRPO 设计）。我认为诊断本身的价值不应被低估——在社区广泛使用 step-independent windowing 且频繁遇到训练失败的背景下，形式化地指出这个范式的结构性缺陷、并提供从业者可操作的指导（Section 6 practitioner guidance），对社区是有意义的贡献。诊断性论文的 excitement 应评估其改变从业者行为的潜力，而非方法新颖性。

**共识**：两位 reviewer 均认为 3.0 (Findings) 是合理的评分档位。论文的核心诊断有价值，但方法论严谨性的多处不足（theory-experiment gap、factorial 不完整、统计功效不足）使其目前不满足主会议标准。


---

[Reviewer 1 审稿结果]:
交叉回应已提交。总结：

- R2 的两个 Must-Fix 我均 **[AGREE]**，但建议将 N1（缺少同期方法对比）降级为 should-fix，因为论文定位是 diagnostic 而非 method
- R2 的四个 Should-Fix 我均 **[AGREE]** 或 **[PARTIALLY AGREE]**，其中 W1 和 W2 与我自己的 N3、N1 重合
- R2 的所有 Minor 我均 **[AGREE]**
- 两位 reviewer 在 Overall 3.0 (Findings) 上达成共识；主要分歧在 Soundness（我更严格：2.5 vs R2 的 3.5）和 Excitement（我更宽松：3.5 vs R2 的 2.5）

---

[Reviewer 2 审稿意见]:

# Reviewer 2 对 Reviewer 1 审稿意见的逐条回应

---

## Must-Fix

**[AGREE] R1-N1: 80.9% vs 52% gap 在主文中处理不当**

同意。我在自己的审稿中也将此列为 Should-Fix (W2)。补充以下观察：

- Abstract 的措辞 "theory predicts 80.9%...empirical measurement...yields 52%" 确实给人两者互相验证的暗示，但两者实际在不同 reward structure 下得出。读者如果不读 Appendix A.2，会误以为理论被实验"大致验证"了。
- 更深层的问题是：论文在多处（Abstract, Introduction, Conclusion）以 80.9% 作为 headline number，但实际系统使用 penalty reward（-0.1 per invalid action），此时 correct-sign rate 是 52%（≈random）。52% 仍然支持 "credit assignment is broken" 的结论，但 "80.9% incorrect" 和 "52% incorrect" 传递的严重程度截然不同。
- 建议：主文 Section 3 增加一段讨论 penalty reward 对理论预测的影响，明确告知读者 80.9% 是理论上限而非实测值。

**[AGREE] R1-N2: Eq. 6 累积发散论证的 "comparable magnitude" 假设过强**

同意，且我认为这比 R1 指出的更严重。具体来说：

- 在 p=12.5%, K=8 的 GRPO 中，成功 rollout 的 advantage ≈ (r+ - μ)/σ。由于 μ 接近 0（大多数 rollout 失败），成功 rollout 的 advantage 量级远大于失败 rollout。这意味着虽然 80.9% 的更新方向错误，但正确方向的更新可能有更大的 magnitude，产生部分补偿效应。
- Eq. 6 的 "monotonic divergence" 结论（$\|\theta_t - \theta^*\| \geq \|\theta_t - \theta^*\| + t \cdot \eta(1-2P_c)\|g\|$，Section 3, theoretical_analysis.tex line 40）依赖于 $g_+$ 和 $g_-$ 量级相当的假设。如果 $\|g_+\| \gg \|g_-\|$，即使 $P_c < 0.5$，期望梯度仍可能指向正确方向。
- 然而，实验观察到的 catastrophic collapse（Table 1: Cell A 从 SFT 12.5% 降至 0%）表明在实践中 magnitude 补偿不足以阻止退化。因此，正确的修正方向不是推翻结论，而是将理论表述从"必然发散"弱化为"在实验观察的条件下发散"。
- **建议作者**：(a) 明确标注 "comparable magnitude" 为简化假设；(b) 分析实际训练中 correct vs incorrect update 的 magnitude 分布；(c) 将 Eq. 6 的结论改为 sufficient condition 而非必然结果。

**[AGREE] R1-N3: Cell C 缺失且种子数不足**

完全同意。我在自己的 W1 中也标记了此问题。补充：

- 2 seeds per condition 在论文自己展示的高 seed variability 下（Section 4.4: 11 seeds 中 3 categories 几乎均匀分布）确实不够。Cell B 的两个 seed 分别达到 20% 和 55% training success（Section 4.2, experiments.tex line 20），差距极大，说明 2 seeds 可能恰好落在不同 outcome modes。
- Cell C 缺失不仅是 factorial 的完整性问题：没有 Cell C，论文实际上无法证明 M2 的**独立影响**。A→B 对比同时改变了 advantage granularity（step→episode）和 advantage sign 属性，这两个变化是 confounded 的。论文声称 A→B 隔离了 M2（"The A→B comparison isolates M2"，experiments.tex line 24），但严格来说是隔离了 "step-level advantage 与 episode-level advantage 的差异"，而 M2 只是其中一个组成部分。

---

## Should-Fix

**[AGREE] R1-W1: Definition 1 操作化的逻辑循环**

同意。Section 4.3 用 "successful episode 中 valid actions = locally correct" 来测量 credit agreement（experiments.tex line 62），但这恰恰是 episode-level outcome 决定 local quality 标签——与论文批评 GRPO 做的事情结构相同。一个 successful episode 中的 valid action 不一定是 causal contributor（可能是 irrelevant action）。更好的操作化需要 counterfactual 测试（如替换单个 window 并观察 episode outcome 变化），但这在计算上可能不可行。论文应至少承认此局限性。

**[AGREE] R1-W2: Window-size cliff 基于 single seed**

同意。我在 W3 中也标记了类似问题（跨规模/跨环境 single-seed）。h-sweep 的 cliff 模式（Figure 2b）如果恰好是 outlier seed 的特征，则 "credit assignment cliff" 的结论不可靠。

**[REBUT] R1-W3: REINFORCE++ 仅 15 步**

部分不同意。R1 的担忧有道理（15 步可能不够），但论文的 argument 是 Cell A 展示的是 **active degradation**（从 SFT 12.5% 降至 0%），而非 undertraining。REINFORCE++ 维持在 SFT baseline（12.5%）没有退化也没有改进（Appendix C, appendix.tex line 96），这至少说明 REINFORCE++ 的 episode-level 设计避免了 catastrophic collapse。论文并未声称 REINFORCE++ 不如 episode-level GRPO——而是说 REINFORCE++ 的 per-token baseline 不如 group normalization 有效。不过我同意应该标注 15 步可能不足。

**[AGREE] R1-W4: Table 1 报告标准不一致**

同意。Table 1 caption 中 Cell A = "best seed", Cell B = "best checkpoint (step 5)", Cell D = "mean of two seeds"（experiments.tex line 35-36）。这种混用使得跨 condition 对比不公平。如果所有 condition 统一用 "best checkpoint per seed, then mean across seeds"，Table 1 的数字可能不同。

**[AGREE] R1-W5: 52.07% 缺乏统计检验**

同意。52.07% 是一个精确到小数点后两位的数字，但没有提供：样本量（多少个 window-update pairs）、binomial test p-value（against H0: 50%）、confidence interval。如果样本量足够大，52.07% 可能统计显著地 >50%（虽然实质意义不大）；如果样本量小，则可能不显著。这是一个容易修复的遗漏。

**[AGREE] R1-W6: SFT baseline 训练细节缺失**

同意。Section 4.1 提到 "Qwen3-1.7B fine-tuned on 2,546 expert demonstrations (SFT baseline: 12.5% in-distribution, 0% pre-SFT)"（experiments.tex line 9），但缺少：learning rate、epochs、early stopping criterion、evaluation protocol (τ=0? τ=0.4?)。作为所有 RL 实验的起点，SFT baseline 的细节对 reproducibility 至关重要。

---

## Minor

**[AGREE] R1-M1**: 80.9% vs 52% 首次出现时确实应该注释差异来源。

**[AGREE] R1-M2**: Eq. 3 "≈" 应该给出 bound 或 empirical verification。

**[REBUT] R1-M3**: 12.6% 不是 rounding error——它是 $0.66 \times 0.191 = 0.126$，即 "effective learning rate" 的计算结果（Section 3, theoretical_analysis.tex line 33: "0.66 × 0.19 ≈ 12.6% of nominal"），不是 baseline success rate 12.5%。这是两个不同的数字，R1 可能混淆了。

**[AGREE] R1-M4**: seed100 在 Table 2 出现两次（step 5: 11.19%, step 10: 12.69%）。同一 seed 不同 checkpoint 出现在同一 table 中不标准，应拆分或注释。

**[AGREE] R1-M5**: ScienceWorld 的 30.1% (Section 4.6, "SFT baseline 30.1%") vs 34.8% ("Restricting context to h=2 drops SFT success from 34.8% to 4.5%") 确实需要说明是不同评估集还是不同指标。从上下文推断，30.1% 可能是 full-context SFT 的 task success rate，34.8% 可能是不同的 evaluation split，但论文未澄清。

---

## 总体评价

R1 的审稿质量很高，找到了多个我也独立发现的问题（理论-实测 gap、Cell C 缺失、seed 不足），也找到了我遗漏的重要技术问题（Eq. 6 magnitude 假设、Definition 1 循环操作化、Table 1 报告不一致）。

**我与 R1 在 Overall 评分上一致：3.0 (Findings)**。

R1 给 Soundness 2.5/5，我给 3.5/5——差异来源主要是 Eq. 6 的 magnitude 假设问题。R1 认为这可能从根本上改变结论（从 divergence 降级为 noisy convergence），我认为实验观察到的 collapse（Cell A: 0%）已经 empirically 确认了 divergence 发生，理论不精确但方向正确。这是一个程度判断，R1 的担忧有合理基础。

R1 给 Excitement 3.5/5（高于我的 2.5），R1 给 Reproducibility 2.5/5（低于我的 4.0）。R1 的 reproducibility 评分更合理——考虑到 SFT 细节缺失、Table 1 报告不一致、checkpoint 丢失（seed1 $\dagger$ 标记）等问题，3.0 可能更准确。


---

[Reviewer 2 审稿结果]:
审稿交叉回应已提交给 Review Director。

总结：对 R1 的 10 个主要观点中，我 **[AGREE] 8 个**，**[REBUT] 2 个**：
- **反驳 W3**（REINFORCE++ 15步）：论文的 argument 是关于 active degradation vs undertraining 的区分，REINFORCE++ 不退化本身已说明问题
- **反驳 M3**（12.6% rounding）：这是 effective learning rate 计算（0.66×0.19），不是 baseline success rate 12.5%，R1 可能混淆了两个数字

与 R1 在 Overall 3.0 (Findings) 评分上一致。主要分歧在 Soundness（我 3.5 vs R1 2.5）和 Excitement（我 2.5 vs R1 3.5）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 240 · 2026-05-23T09:17:30.892087+00:00_

两位 Reviewer 的详细交叉回应已收到。

**收敛确认**：

- Overall 3.0 (Findings) 共识保持不变
- R1 对 R2 的 10 个观点：8 个 [AGREE]，2 个调整严重程度（R2-N1 建议降为 should-fix）
- R2 对 R1 的 10 个观点：8 个 [AGREE]，2 个 [REBUT]

**两个 REBUT 值得记录**：

1. **R1-W3 (REINFORCE++ 15步)**：R2 认为论文的 argument 关于 active degradation vs undertraining 的区分是成立的——REINFORCE++ 不退化本身已说明 episode-level 设计避免了 catastrophic collapse，15 步虽短但论点方向正确。
2. **R1-M3 (12.6% rounding)**：R2 纠正了 R1——0.66×0.191=0.126≈12.6% 是 effective learning rate 的正确计算，与 baseline success rate 12.5% 是两个不同数字，**不是 rounding error**。

**修正**：已提交报告中的 m3（12.6% rounding inconsistency）为误判，该数字实际上正确。此修正不影响整体评分和结论。

审稿报告已于交叉回应前投递至 Research Director（Overall 3.0 Findings）。完整的 Round 2 圆桌审稿流程结束。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director"
}
```

</details>

---


## Round 20

## Round 20

56 recorded events


### User

_source line 241 · 2026-05-23T15:53:07.745831+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: cost-verify-agent-rl
- 论文路径: projects/cost-verify-agent-rl/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 截止日期: 2026-05-25
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 242 · 2026-05-23T15:53:13.729824+00:00_

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
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 243 · 2026-05-23T15:53:13.780770+00:00_

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
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 244 · 2026-05-23T15:53:21.607869+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,get_external_review_status,get_visual_check_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,read_project_file,WebSearch",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,get_external_review_status,get_visual_check_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,read_project_file,WebSearch",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 245 · 2026-05-23T15:53:21.658456+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 246 · 2026-05-23T15:53:24.268100+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,get_external_review_status,get_visual_check_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,read_project_file",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,get_external_review_status,get_visual_check_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,read_project_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 247 · 2026-05-23T15:53:24.319746+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "ToolSearch",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 248 · 2026-05-23T15:53:27.482210+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "director_get_project_overview",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "director_get_project_overview",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 249 · 2026-05-23T15:53:27.482956+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 250 · 2026-05-23T15:53:30.594397+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 251 · 2026-05-23T15:53:30.645011+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 252 · 2026-05-23T15:53:35.662700+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "cost-verify-agent-rl"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "cost-verify-agent-rl"
  }
}
```

</details>

---


### Tool result

_source line 253 · 2026-05-23T15:53:36.616793+00:00_

{"result":"# 项目 cost-verify-agent-rl 概况\n\n## 实验状态 (183 个)\n\n- **exp010**: DONE (failed) — \n- **exp009**: DONE (failed) — \n- **exp008**: PREPARING (killed) — \n- **exp007**: DONE (failed) — \n- **exp007_dryrun**: PREPARING — \n- **exp003**: DONE (failed) — \n- **exp005**: PREPARING — \n- **exp_003**: PREPARING (failed) — \n- **exp_003_dryrun**: PREPARING (failed) — \n- **exp_003_dryrun2**: PREPARING (failed) — \n- **exp003_dryrun3**: PREPARING (failed) — \n- **exp_003_dryrun3**: PREPARING (failed) — \n- **exp_002**: DONE (failed) — \n- **exp_001b**: DONE (failed) — \n- **exp_001**: DONE (failed) — \n\n## 最新报告\n&lt;!-- AUTO-FACTS-BEGIN (generated 2026-05-23T01:08:36Z; do not edit — regenerated by auto_build_report_facts) -->\n## 📊 当前状态（auto-derived from registry）\n\n**总计**: 180 个实验 — ANALYZING 1, DONE 147, PREPARING 32\n**DONE 分布**: failed 62, killed 20, negative 23, success 42\n\n### 💾 磁盘余量\n- **bjb1-17606**:\n  - `/init`: 150M/150M 可用（已用 0%）\n  - `/autodl-pub/data`: 5.7T/10T 可用（已用 44%）\n  - `/usr/bin/nvidia-smi`: 817G/879G 可用（已用 3%）\n- **westd-47453**:\n  - `/autodl-pub`: 5.3T/7.3T 可用（已用 24%）\n  - `/init`: 150M/150M 可用（已用 1%）\n  - `/usr/bin/nvidia-smi`: 813G/879G 可用（已用 3%）\n\n### 🏃 RUNNING\n_（无）_\n\n### 📌 最近完成 (top 5)\n- `exp029_seed7_high_kl_step7_ood_v2` [failed] — 2026-05-23T00:28:57\n- `exp029_seed7_high_kl_step5_ood_v2` [failed] — 2026-05-23T00:28:55\n- `exp029_seed100_resume_step10` [success] — 2026-05-23T00:17:50\n- `exp029_seed7_ood_precollapse` [killed] — 2026-05-22T22:33:47\n- `exp029_seed300_step5_ood_eval_v4` [success] — 2026-05-22T22:26:20\n\n### 🔴 最近失败原因 (top 3)\n- `exp029_seed7_high_kl_step7_ood_v2`: _(no failure_reason — pre-2026-04-24 entry)_\n- `exp029_seed7_high_kl_step5_ood_v2`: _(no failure_reason — pre-2026-04-24 entry)_\n- `exp029_seed7_ood_precollapse`: _(no failure_reason — pre-2026-04-24 entry)_\n\n&lt;!-- AUTO-FACTS-END -->\n\n---\n\n# Handover — 2026-05-23\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|
…[truncated 1681 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 254 · 2026-05-23T15:53:36.767822+00:00_

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
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission guidelines ARR site:aclweb.org"
  }
}
```

</details>

---


### Tool call

_source line 255 · 2026-05-23T15:53:38.524608+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/main.tex",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/main.tex",
    "limit": "80"
  }
}
```

</details>

---


### Tool result

_source line 256 · 2026-05-23T15:53:38.826114+00:00_

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
12	\usepackage{amsmath}
13	\usepackage{amssymb}
14	\usepackage{amsthm}
15	\usepackage{enumitem}
16	
17	\title{Sign Misattribution in Step-Independent Agent RL:\\Dual Mechanism Diagnosis and Episode-Level Correction}
18	
19	\author{Anonymous}
20	
21	\begin{document}
22	\maketitle
23	
24	\begin{abstract}
25	Reinforcement learning for multi-turn LLM agents requires credit assignment across long interaction trajectories. The dominant training paradigm decomposes these trajectories into fixed-size windows optimized independently via Group Relative Policy Optimization (GRPO), yet this ubiquitous design choice has received little scrutiny. We identify a structural credit assignment pathology driven by two distinct mechanisms: \textit{policy information loss}, which truncates cross-window context and imposes a constant performance ceiling, and \textit{advantage sign misattribution}, which causes the majority of gradient updates for locally correct actions to carry incorrect sign. A factorial experiment isolates each mechanism: removing sign misattribution converts catastrophic collapse into bounded learning; removing information loss enables out-of-distribution (OOD) generalization. Direct sign measurement confirms the theoretical prediction, with credit agreement dropping to near-random levels. Episode-level GRPO, which treats the full trajectory as a single optimization sample, eliminates both failure modes. However, a systematic multi-seed evaluation reveals that avoiding collapse is necessary but not sufficient: 73\% of seeds stabilize, yet only 36\% achieve statistically significant OOD transfer. Cross-scale verification at 8B parameters and cross-environment validation on ScienceWorld provide preliminary evidence that the patholog
…[truncated 1422 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 257 · 2026-05-23T15:53:38.826622+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 258 · 2026-05-23T15:53:38.877319+00:00_

1	- id: W1
2	  summary: '"Locally correct actions" 定义操作化存在逻辑循环'
3	  category: method
4	  severity: warning
5	  status: in_progress
6	  first_raised_round: 1
7	  last_seen_round: 2
8	  mentions:
9	    - {round: 1, reviewers: [R1, R2], note: "Entire theoretical framework depends on this undefined concept"}
10	    - {round: 1, action_taken: "Definition 1 added in theoretical_analysis.tex; operationalized in experiments.tex Section 4.4"}
11	    - {round: 2, reviewers: [R1], note: "定义已添加但操作化存在循环：用 episode outcome 标记 locally correct，恰好犯了论文批评的错误。成功 episode 中的次优 window 也被标记为 locally correct。"}
12	  action_items:
13	    - {round: 2, action: "在 Section 4.4 讨论操作化的近似性质（上界估计）", assigned_to: main_agent, status: done}
14	
15	- id: W2
16	  summary: "Theory (80.9%) vs experiment (52%) gap 在主文中仍处理不当"
17	  category: method
18	  severity: critical
19	  status: in_progress
20	  first_raised_round: 1
21	  last_seen_round: 2
22	  mentions:
23	    - {round: 1, reviewers: [R1, R2], note: "Prop 2 predicts 19.1%, measured 52.07%. Intro/Conclusion use 80.9% but experiments show 52%"}
24	    - {round: 1, action_taken: "Penalty reward analysis added to appendix. Intro/Conclusion/Abstract present 80.9% qualified with '(52% under penalty reward)'"}
25	    - {round: 2, reviewers: [R1, R2], note: "Round 1 修复不充分。Abstract/Intro 仍将两个数字简单并列。缺乏 penalty reward 下的理论修正公式或 pure binary 实验验证。"}
26	  action_items:
27	    - {round: 2, action: "在主文 Section 3/4.4 讨论 binary vs penalty reward 差异", assigned_to: main_agent, status: done}
28	    - {round: 2, action: "跑纯 binary reward 实验验证 Proposition 2", assigned_to: main_agent, status: in_progress}
29	
30	- id: W3
31	  summary: "10/20 citations use Anonymous authors — ARR compliance violation"
32	  category: format
33	  severity: critical
34	  status: resolved
35	  first_raised_round: 1
36	  last_seen_round: 1
37	  mentions:
38	    - {round: 1, reviewers: [R1, R2], note: "irc2026, grpolambda2025, oar2026 etc."}
39	    - {round: 1, action_taken: "All 10 entries updated
…[truncated 10136 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 259 · 2026-05-23T15:53:42.340305+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines ARR site:aclweb.org"

Links: [{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"*SEM 2026: Commitment Link for ARR-Reviewed Papers (Deadline: 10 April 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/sem-2026-commitment-link-arr-reviewed-papers-deadline-10-april-2026"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"The 64th Annual Meeting of the Association for Computational Linguistics - ACL 2026","url":"https://2026.aclweb.org/"},{"title":"The 2nd BabyLM Workshop | ACL Member Portal","url":"https://www.aclweb.org/portal/content/2nd-babylm-workshop"},{"title":"Call for Papers: The 20th Linguistic Annotation Workshop (LAW XX), co-located with ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-20th-linguistic-annotation-workshop-law-xx-co-located-acl-2026"},{"title":"Jan. 2025 ACL Standing Committee on Peer Review (COPR) Report 1","url":"https://www.aclweb.org/adminwiki/images/9/9e/COPR-5-cycle-report-to-publish.pdf"}]

Based on the web search results, I found information about EMNLP 2026, though the results primarily show workshop calls and tut
…[truncated 1291 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "WebSearch",
  "elapsed_ms": 5572
}
```

</details>

---


### Tool call

_source line 260 · 2026-05-23T15:54:10.336072+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 ARR submission deadline page limit author guidelines 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 ARR submission deadline page limit author guidelines 2026"
  }
}
```

</details>

---


### Tool call

_source line 261 · 2026-05-23T15:54:10.838107+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"ACL Rolling Review\" 2026 submission guidelines page limit template"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"ACL Rolling Review\" 2026 submission guidelines page limit template"
  }
}
```

</details>

---


### Tool call

_source line 262 · 2026-05-23T15:54:12.895487+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 263 · 2026-05-23T15:54:12.946217+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/theoretical_analysis.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/experiments.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 264 · 2026-05-23T15:54:17.211914+00:00_

Web search results for query: ""ACL Rolling Review" 2026 submission guidelines page limit template"

Links: [{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Paper formatting guidelines - ACLPUB","url":"https://acl-org.github.io/ACLPUB/formatting.html"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"}]

Based on the search results, here are the key details about the ACL Rolling Review 2026 submission guidelines regarding page limits and templates:

## Page Limits

Review versions of long papers may have up to eight (8) pages of content plus unlimited pages for references. Review versions of short papers may have up to four (4) pages of content, plus unlimited pages for references.

## Template Requirements

Paper submissions must use the official ACL style template, which is availab
…[truncated 894 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "WebSearch",
  "elapsed_ms": 6373
}
```

</details>

---


### Tool result

_source line 265 · 2026-05-23T15:54:23.234640+00:00_

Web search results for query: "EMNLP 2026 ARR submission deadline page limit author guidelines 2026"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"EMNLP 2026 on X: \"📢 Submitting to the May 19th ARR deadline? ✅ Make sure your profile is complete, including your DBLP link: https://t.co/jr60DoKZ2R 📄 Do not forget to review: (1) Author Guidelines https://t.co/QTDyAWZtKS (2) ACL Publication policy https://t.co/nImuaa9cez #NLProc #EMNLP25 #ARR\" / X","url":"https://x.com/emnlpmeeting/status/1923431912778895593"},{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"Authors Guidelines","url":"http://aclrollingreview.org/authors"},{"title":"EMNLP 2026 LaTeX Template | ACL Style Files & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/emnlp"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"EMNLP 2026 Conference | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FConference"},{"title":"Submissions | Transactions of the Association for Computational Linguistics","url":"https://transacl.org/index.php/tacl/about/submissions"}]

Based on the search results, here is the information about EMNLP 2026 ARR submission details:

## Submission Deadline

The ARR submission deadline for long and short papers is May 25, 2026.

## Page Limits

The format uses a two-column layout with an 8-page limit for long papers and a 4-page limit for short papers. Additionally, final versions of accepted papers will be given one additional page of content (up to 9 pages for long papers, up to 5 pages for short papers) to address reviewers' comments.

## Au
…[truncated 826 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "WebSearch",
  "elapsed_ms": 12898
}
```

</details>

---


### Tool call

_source line 266 · 2026-05-23T15:54:35.666807+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 267 · 2026-05-23T15:54:35.968316+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Reinforcement learning from sparse terminal reward has emerged as a promising paradigm for training LLM agents on multi-turn interactive tasks spanning 30--50 interaction steps~\cite{kim2025reflact,digiRL2024,wang2022scienceworld}. Group Relative Policy Optimization (GRPO)~\cite{shao2024deepseekmath}, with its critic-free design, has become the algorithm of choice. Yet a gap persists between the promise of RL-driven agent improvement and the reality of training outcomes: recent agent RL systems~\cite{ragen2025,selfguide2026,spear2025,feng2025gigpo} share a common, unscrutinized implementation pattern (decomposing trajectories into fixed-size windows, each optimized independently) and frequently report training instability without diagnosing its root cause.
5	
6	We show this \textit{step-independent} default introduces a fundamental credit assignment pathology. Step-independent training partitions trajectories into non-overlapping $h$-step windows, each optimized via GRPO. This produces a two-phase collapse: task success drops to 0\% while action validity initially remains high, then continued training destroys even basic formatting. Standard remedies (dense reward shaping, discount tuning) fail. Concurrent methods that improve per-step credit quality (GiGPO~\cite{feng2025gigpo}, GAGPO~\cite{gagpo2026}, Turn-PPO~\cite{turnppo2026}, HCAPO~\cite{hcapo2026}) address the symptom through improved credit assignment mechanisms, validating that sign correctness is the critical factor. Our contribution is orthogonal: we formally diagnose \textit{why} the default windowing fails.
7	
8	We trace the collapse to two mechanisms at different layers. \textit{\textbf{Policy information loss}} (M1) operates at the inference layer: each window lacks access to earlier observations, imposing a constant performance ceiling. \textit{\textbf{Advantage sign misattribution}} (M2) operates at the training layer: under binary reward, the 
…[truncated 1881 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 268 · 2026-05-23T15:54:35.968702+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 269 · 2026-05-23T15:54:36.420811+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Problem Formulation and GRPO}
5	\label{sec:problem_formulation}
6	
7	We model the multi-turn agent as a partially observable Markov decision process (POMDP) where the policy $\pi_\phi(a_t \mid h_t)$ generates actions conditioned on interaction history $h_t = (o_1, a_1, \ldots, o_t)$. Episodes of $T$ steps terminate with binary reward $R \in \{0, r_+\}$. GRPO~\cite{shao2024deepseekmath} samples $K$ rollouts per task and computes group-relative advantages:
8	\begin{align}
9	\hat{A}_k &= \frac{R_k - \mu}{\sigma + \epsilon}, \notag \\
10	\mu &= \frac{1}{K}\sum_{j=1}^K R_j, \quad \sigma = \sqrt{\frac{1}{K}\sum_{j=1}^K (R_j - \mu)^2}
11	\label{eq:grpo_advantage}
12	\end{align}
13	GRPO is episode-level by design: each rollout receives one return and one advantage, with no inherent temporal discounting.
14	
15	\subsection{Step-Independent Windowing}
16	\label{sec:step_independent}
17	
18	Agent RL frameworks must reconcile GRPO's episode-level design with the memory constraints of long trajectories. RAGEN~\cite{ragen2025} introduces \textbf{step-independent training}: the trajectory is partitioned into non-overlapping $h$-step windows, each receiving a discounted return:
19	\begin{equation}
20	R_k = \gamma^{(N - k)} \cdot R_{\text{episode}}
21	\label{eq:step_return}
22	\end{equation}
23	where $N = \lceil T/h \rceil$ is the number of windows. Each window is optimized as an independent GRPO sample. This reduces sequence length from $O(T)$ to $O(h)$ and multiplies the effective batch size, but structurally alters credit assignment.
24	
25	\begin{figure*}[t]
26	\centering
27	\includegraphics[width=\textwidth]{fig_overview.pdf}
28	\caption{Step-independent windowing (left) partitions the trajectory into fixed windows, each optimized independently. This introduces two failure mechanisms: M1 (information loss) truncates context at window boundaries, and M2 (sign misattribution) assigns all windows the same advantage sign base
…[truncated 3323 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 270 · 2026-05-23T15:54:36.421168+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/theoretical_analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/theoretical_analysis.tex"
  }
}
```

</details>

---


### Tool result

_source line 271 · 2026-05-23T15:54:36.772700+00:00_

1	\section{Theoretical Analysis}
2	\label{sec:theory}
3	
4	Sign misattribution is the more fundamental failure mechanism because it causes active divergence, not merely slow convergence. We derive the probability of incorrect gradient direction below; full proofs appear in Appendix~\ref{app:theory_full}.
5	
6	\textbf{Definition 1} (Locally correct action). \textit{An action $a_t$ is \textbf{locally correct} if it would receive positive advantage under an oracle that observes the full episode history $h_t$ and has access to the true action-value function. Equivalently, window $k$ contains locally correct actions if replacing them (holding all other windows fixed) would decrease the probability of episode success.}
7	
8	\textbf{Proposition 1.} \textit{Under step-independent training with binary episode reward $R_{\text{episode}} \in \{0, r_+\}$, the probability that window $k$'s advantage $\hat{A}_k$ has the correct sign (aligned with local action quality) approaches the base success rate $p$ as the number of rollouts $K$ per group increases.}
9	
10	\textit{Proof sketch.} In a failed episode ($R_{\text{episode}} = 0$), all windows receive $R_k = 0$. If any rollout in the group succeeded, $\mu > 0$, so every window in the failed episode receives $\hat{A}_k < 0$---including windows with locally correct actions. The probability of receiving the wrong sign in a failed episode is $1 - (1-p)^{K-1}$ (at least one group member succeeded). As $K$ grows, this approaches $1-p$, and the overall probability of correct sign approaches $p$. \hfill$\square$
11	
12	The key distinction is temporal. Information loss (M1) imposes a constant ceiling determined by $h$; sign misattribution (M2) is cumulative---each wrong-sign gradient step erodes policy competence below that ceiling. A wrong-sign gradient moves the optimizer \textit{away} from good policies; a reduced-magnitude gradient from discounting ($\gamma^{(N-k)}$) still points toward good policies. Sign errors produce active diverge
…[truncated 4135 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 272 · 2026-05-23T15:54:36.773072+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 273 · 2026-05-23T15:54:36.873851+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	Step-independent training collapses while episode-level training succeeds; a factorial design separates the two mechanisms; and window size $h$ modulates severity.
5	
6	\subsection{Setup}
7	\label{sec:setup}
8	
9	We evaluate on ALFWorld~\cite{shridhar2021alfworld}, a text-based household environment with six task types requiring sequential reasoning over up to 50 steps. Reward is binary: $R \in \{0, r_+\}$. The base policy is Qwen3-1.7B fine-tuned on expert demonstrations (SFT baseline: 12.5\% in-distribution). At this baseline success rate, Proposition~2 predicts the majority of gradient updates carry incorrect sign. All conditions use RAGEN~\cite{ragen2025} (v0.1, commit \texttt{3a6b48b})\footnote{Our implementation extends RAGEN v0.1 with episode-level training support. Code: \url{https://github.com/RAGEN-AI/RAGEN}.} with GRPO~\cite{shao2024deepseekmath} ($K{=}8$; full hyperparameters in Appendix~\ref{app:hyperparameters}). We report success rate on a 134-task OOD set (primary) and 32-task in-distribution set (secondary). Seed counts are noted per condition.
10	
11	\subsection{Factorial Mechanism Separation}
12	\label{sec:factorial_experiments}
13	
14	We implement the factorial design from Section~\ref{sec:factorial_design} with two seeds per condition. Cell~C (full observation, step-level advantage) would isolate M2 without M1, but we encountered persistent training instability in this configuration (Appendix~\ref{app:cell_c}).
15	
16	\subsection{Results}
17	\label{sec:results}
18	
19	Cell~A collapses in two phases (Table~\ref{tab:main_results}): task success drops to 0\% while action validity initially remains high, then continued sign misattribution destroys even basic formatting.% exp_id: hsweep_h2_seed1, hsweep_h2_seed2
20	Cell~B eliminates sign misattribution while retaining information loss: training success improves, but OOD generalization is bounded by the information-loss ceiling. Both seeds converg
…[truncated 9304 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 274 · 2026-05-23T15:54:41.491538+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 275 · 2026-05-23T15:54:42.344952+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{RL for multi-turn LLM agents.}
5	PPO~\cite{schulman2017ppo}, GRPO~\cite{shao2024deepseekmath}, and DPO~\cite{rafailov2023dpo} underpin RLHF~\cite{ouyang2022instructgpt} and have been extended to multi-turn agents~\cite{yao2023react} through step-independent windowing~\cite{ragen2025}. Subsequent work improves algorithms (GiGPO~\cite{feng2025gigpo}), reward design (Self-Guide~\cite{selfguide2026}), or pipelines (SPEAR~\cite{spear2025}, DigiRL~\cite{digiRL2024}), but all assume trajectory decomposition into fixed windows is benign. We show this assumption is false.
6	
7	\paragraph{Credit assignment.}
8	TD($\lambda$)~\cite{sutton1988td}, GAE~\cite{schulman2016gae}, and REINFORCE~\cite{williams1992reinforce} span bootstrapping to Monte Carlo returns; reward shaping~\cite{ng1999shaping} and counterfactual baselines~\cite{foerster2018coma} address sparse reward. Several studies corroborate our diagnosis: IRC~\cite{irc2026} and MC-GRPO~\cite{mcgrpo2025} observe sign disagreement between per-turn and outcome advantages, GRPO-$\lambda$~\cite{grpolambda2025} proves estimation error grows with position, and OAR~\cite{oar2026} identifies reward aliasing. Turn-PPO~\cite{turnppo2026}, GAGPO~\cite{gagpo2026}, MT-GRPO~\cite{mtgrpo2025}, SWEET-RL~\cite{sweetrl2025}, and iStar~\cite{istar2025} propose finer-grained credit methods; HCAPO~\cite{hcapo2026} validates that sign correctness is the critical bottleneck. We diagnose \textit{why} the default fails, informing when finer-grained credit is safe.
9	
10	\paragraph{GRPO collapse phenomena.}
11	RAGEN-2~\cite{ragen2_2026} proves advantage collapse when reward variance vanishes, GRPO-Collapse~\cite{grpocollapse2025} identifies a death spiral in Search-R1, and RC-GRPO~\cite{rcgrpo2026} and EDGE-GRPO~\cite{edgegrpo2025} address variance collapse. Our dual-mechanism diagnosis unifies these: reward variance collapse is a special case of reward saturation (Section~\ref{sec:
…[truncated 73 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "Read",
  "elapsed_ms": 853
}
```

</details>

---


### Tool call

_source line 276 · 2026-05-23T15:54:42.495938+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 277 · 2026-05-23T15:54:42.847560+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Generality and mechanism interaction.}
5	Sign misattribution arises whenever three structural properties co-occur: (a) step-level windowing, (b) sparse binary reward, and (c) group-relative normalization. Under these conditions, the advantage sign collapses to a proxy for episode outcome, and severity scales with task difficulty ($P(\text{correct} \mid \text{update}) \to p$). M1 and M2 interact in a vicious cycle: M1 lowers $p$, increasing wrong-sign updates under M2, which further degrades $p$. The A$\to$B comparison provides direct evidence: identical observation scope ($h{=}2$), yet eliminating step-level advantage converts catastrophic collapse into bounded learning. Six factors explaining why step-independent became the default are detailed in Appendix~\ref{app:why_defaults}.
6	
7	\paragraph{Seed-dependent OOD generalization.}
8	The multi-seed evaluation reveals a bimodal distribution: a stagnant cluster with OOD performance indistinguishable from SFT and a generalized cluster with significant improvement. Training duration does not explain the gap, pointing to initialization sensitivity as the likely driver.
9	
10	\paragraph{Practitioner guidance.}
11	Use episode-level credit when the full episode fits in context; otherwise use the largest feasible $h$ ($h{\geq}20$; $h{\leq}10$ collapses). Finer-grained methods should be applied only after establishing an episode-level baseline.
12	
13	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 278 · 2026-05-23T15:54:42.998452+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 279 · 2026-05-23T15:54:42.998819+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	Step-independent training fails through two mechanisms: information loss imposes a constant performance ceiling while sign misattribution causes cumulative degradation, with the majority of gradient updates carrying incorrect sign. Episode-level GRPO addresses both failure modes, achieving substantial OOD improvement at both 1.7B and 8B scales, though only a minority of seeds achieve statistically significant generalization. Sign errors are more destructive than magnitude imprecision; this finding applies to any agent RL method combining step-level windowing, sparse binary reward, and group-relative normalization.
5	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 280 · 2026-05-23T15:54:43.350285+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/appendix.tex",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/appendix.tex",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 281 · 2026-05-23T15:54:43.451233+00:00_

1	\appendix
2	
3	\section{Theoretical Analysis: Full Derivations}
4	\label{app:theory_full}
5	
6	\subsection{Why Sign Misattribution is the Core Mechanism}
7	\label{app:sign_fundamental}
8	
9	The two mechanisms identified in Section~\ref{sec:dual_mechanism} operate at different layers and produce qualitatively different failures. Policy information loss (Mechanism 1) operates at the inference layer, restricting the observable context and establishing a structural performance ceiling that is constant across training. Sign misattribution (Mechanism 2) operates at the training layer, corrupting gradient directions and progressively degrading performance below this ceiling.
10	
11	\textit{Proof of Proposition 1.} Define ``correct sign'' as follows: for a window containing locally beneficial actions, the correct sign of $\hat{A}_k$ is positive (reinforcement); for a window containing locally detrimental actions, the correct sign is negative (suppression). Under binary reward, the return for window $k$ is $R_k = \gamma^{(N-k)} \cdot R_{\text{episode}}$ (Equation~\ref{eq:step_return}). In a failed episode ($R_{\text{episode}} = 0$), all windows receive $R_k = 0$ regardless of their local action quality. If the group contains at least one successful rollout, the group mean $\mu > 0$, and all windows in the failed episode receive negative advantages after normalization via Equation~\ref{eq:grpo_advantage}. This includes windows where the agent took locally correct actions. Now consider a window with locally correct actions. In a successful episode (probability $p$), the window receives positive $\hat{A}_k$, which is the correct sign. In a failed episode (probability $1 - p$), the window receives negative $\hat{A}_k$ whenever $\mu > 0$, which is the wrong sign. The probability that $\mu = 0$ (all $K$ rollouts in the group failed) is $(1-p)^K$, which shrinks exponentially with $K$. As $K$ grows, nearly every failed episode produces a non-zero group mean, and the window receive
…[truncated 17330 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 282 · 2026-05-23T15:54:48.658150+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/appendix.tex",
  "offset": "185"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/appendix.tex",
    "offset": "185"
  }
}
```

</details>

---


### Tool result

_source line 283 · 2026-05-23T15:54:48.708723+00:00_

&lt;system-reminder>Warning: the file exists but is shorter than the provided offset (185). The file has 185 lines.&lt;/system-reminder>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 284 · 2026-05-23T15:54:55.284410+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "cost-verify-agent-rl",
  "file": "paper_checklist.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "cost-verify-agent-rl",
    "file": "paper_checklist.yaml"
  }
}
```

</details>

---


### Tool result

_source line 285 · 2026-05-23T15:54:55.829478+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'cost-verify-agent-rl'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 545
}
```

</details>

---


### Tool call

_source line 286 · 2026-05-23T15:54:55.829853+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 287 · 2026-05-23T15:54:55.880453+00:00_

1	@inproceedings{shridhar2021alfworld,
2	  title     = {{ALFWorld}: Aligning Text and Embodied Environments for Interactive Learning},
3	  author    = {Shridhar, Mohit and Yuan, Xingdi and C\^{o}t\'{e}, Marc-Alexandre and Bisk, Yonatan and Trischler, Adam and Hausknecht, Matthew},
4	  booktitle = {International Conference on Learning Representations},
5	  year      = {2021},
6	}
7	
8	
9	@inproceedings{digiRL2024,
10	  title     = {{DigiRL}: Training In-The-Wild Device-Control Agents with Autonomous Reinforcement Learning},
11	  author    = {Bai, Hao and Zhou, Yifei and Cemri, Mert and Pan, Jiayi and Suhr, Alane and Levine, Sergey and Kumar, Aviral},
12	  booktitle = {Advances in Neural Information Processing Systems},
13	  year      = {2024},
14	}
15	
16	@inproceedings{feng2025gigpo,
17	  title     = {{GiGPO}: Group-in-Group Policy Optimization for {LLM} Agent Training},
18	  author    = {Feng, Lang and Xue, Zhenghai and Liu, Tingcong and An, Bo},
19	  booktitle = {Advances in Neural Information Processing Systems},
20	  year      = {2025},
21	}
22	
23	@inproceedings{kim2025reflact,
24	  title     = {{ReflAct}: World-Grounded Decision Making in {LLM} Agents via Goal-State Reflection},
25	  author    = {Kim, Jeonghye and Rhee, Sojeong and Kim, Minbeom and Kim, Dohyung and Lee, Sangmook and Sung, Youngchul and Jung, Kyomin},
26	  booktitle = {Proceedings of the Conference on Empirical Methods in Natural Language Processing},
27	  year      = {2025},
28	}
29	
30	
31	@article{ragen2025,
32	  title   = {{RAGEN}: Understanding Self-Evolution in {LLM} Agents via Multi-Turn Reinforcement Learning},
33	  author  = {Wang, Zihan and Wang, Kangrui and Wang, Qineng and Zhang, Pingyue and Li, Linjie and Yang, Zhengyuan and Jin, Xing and Yu, Kefan and Nguyen, Minh Nhat and Liu, Licheng and Gottlieb, Eli and Lu, Yiping and Cho, Kyunghyun and Wu, Jiajun and Li, Fei-Fei and Wang, Lijuan and Choi, Yejin and Li, Manling},
34	  journal = {arXiv preprint arXiv:2504.20073},
35	  year    =
…[truncated 12201 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 288 · 2026-05-23T15:55:47.000715+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "cost-verify-agent-rl",
  "review_chat_id": "oc_648eaf83d2b24d445764257cf6a55525"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "cost-verify-agent-rl",
    "review_chat_id": "oc_648eaf83d2b24d445764257cf6a55525"
  }
}
```

</details>

---


### Tool call

_source line 289 · 2026-05-23T15:55:47.500803+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "cost-verify-agent-rl"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "cost-verify-agent-rl"
  }
}
```

</details>

---


### Tool result

_source line 290 · 2026-05-23T15:56:08.305143+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 21304
}
```

</details>

---


### Tool result

_source line 291 · 2026-05-23T15:56:08.305478+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 20804
}
```

</details>

---


### Tool call

_source line 292 · 2026-05-23T15:56:08.456340+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

````json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "cost-verify-agent-rl",
  "text": "你是 Reviewer 1，负责**方法严谨性与实验设计**审查。\n\n## Venue 信息\n- **目标**: EMNLP 2026（通过 ARR 统一审稿）\n- **截止日期**: 2026-05-25\n- **页数限制**: Long paper，正文 8 页，参考文献不限，Limitations 不计入页数\n- **模板**: ACL style template，[review] 模式\n- **匿名规则**: Double-blind\n\n## 论文路径\n- LaTeX 源码: `projects/cost-verify-agent-rl/docs/paper/main.tex`（含 \\input 的各章节文件在同一目录）\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/review_round_3/submitted.pdf`\n\n## 你的审查侧重\n\n### 1. 理论分析严谨性\n- Proposition 1/2 的推导是否正确、假设是否合理\n- Definition 1（\"locally correct action\"）的操作化是否存在逻辑问题\n- Eq. 6 累积发散论证中 \"comparable magnitude\" 假设（文中称实测比值 1.32）的合理性\n- Theory 预测 (19.1% correct sign under binary) 与实验测量 (52% under penalty reward) 之间的 gap 是否被充分解释\n\n### 2. 实验设计\n- 2×2 factorial design 的完整性：Cell C 缺失对结论的影响\n- 统计检验：52.07% credit agreement rate 的统计显著性（报告了 n, p-value, CI 吗？）\n- 11-seed 评估的分类标准（Collapsed/Stagnant/Generalized）是否合理\n- Table 1 的报告标准是否一致（best checkpoint per seed vs. mean vs. best seed 混用？）\n\n### 3. 数据一致性\n- Table 1/2 的数据是否与正文描述一致\n- 8B 和 ScienceWorld 单 seed 结果的证据力\n- REINFORCE++ 对比公平性（仅 15 步训练）\n- Window-size sweep 的 cliff claim 是否有足够统计支撑\n\n### 4. 跨规模/跨环境验证\n- 8B 单 seed 结果（90.3% OOD）的 claims 是否适当 hedge\n- ScienceWorld 验证的深度是否足够\n\n请按以下格式输出审稿意见：\n\n```\n## Summary\n（2-3 句论文概述）\n\n## Strengths\nS1. ...\nS2. ...\n\n## Weaknesses\nW1. [severity: critical/major/minor] ...\nW2. ...\n\n## Questions\nQ1. ...\n\n## Missing References\n（如有）\n\n## Detailed Comments\n（逐节详细意见）\n\n## Overall Assessment\n- Score: X/5（参照 EMNLP 2026 评分标准）\n- Confidence: X/5\n- 一句话总评\n```"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "cost-verify-agent-rl",
    "text": "你是 Reviewer 1，负责**方法严谨性与实验设计**审查。\n\n## Venue 信息\n- **目标**: EMNLP 2026（通过 ARR 统一审稿）\n- **截止日期**: 2026-05-25\n- **页数限制**: Long paper，正文 8 页，参考文献不限，Limitations 不计入页数\n- **模板**: ACL style template，[review] 模式\n- **匿名规则**: Double-blind\n\n## 论文路径\n- LaTeX 源码: `projects/cost-verify-agent-rl/docs/paper/main.tex`（含 \\input 的各章节文件在同一目录）\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/review_round_3/submitted.pdf`\n\n## 你的审查侧重\n\n### 1. 理论分析严谨性\n- Proposition 1/2 的推导是否正确、假设是否合理\n- Definition 1（\"locally correct action\"）的操作化是否存在逻辑问题\n- Eq. 6 累积发散论证中 \"comparable magnitude\" 假设（文中称实测比值 1.32）的合理性\n- Theory 预测 (19.1% correct sign under binary) 与实验测量 (52% under penalty reward) 之间的 gap 是否被充分解释\n\n### 2. 实验设计\n- 2×2 factorial design 的完整性：Cell C 缺失对结论的影响\n- 统计检验：52.07% credit agreement rate 的统计显著性（报告了 n, p-value, CI 吗？）\n- 11-seed 评估的分类标准（Collapsed/Stagnant/Generalized）是否合理\n- Table 1 的报告标准是否一致（best checkpoint per seed vs. mean vs. best seed 混用？）\n\n### 3. 数据一致性\n- Table 1/2 的数据是否与正文描述一致\n- 8B 和 ScienceWorld 单 seed 结果的证据力\n- REINFORCE++ 对比公平性（仅 15 步训练）\n- Window-size sweep 的 cliff claim 是否有足够统计支撑\n\n### 4. 跨规模/跨环境验证\n- 8B 单 seed 结果（90.3% OOD）的 claims 是否适当 hedge\n- ScienceWorld 验证的深度是否足够\n\n请按以下格式输出审稿意见：\n\n```\n## Summary\n（2-3 句论文概述）\n\n## Strengths\nS1. ...\nS2. ...\n\n## Weaknesses\nW1. [severity: critical/major/minor] ...\nW2. ...\n\n## Questions\nQ1. ...\n\n## Missing References\n（如有）\n\n## Detailed Comments\n（逐节详细意见）\n\n## Overall Assessment\n- Score: X/5（参照 EMNLP 2026 评分标准）\n- Confidence: X/5\n- 一句话总评\n```"
  }
}
````

</details>

---


### Tool result

_source line 293 · 2026-05-23T15:56:27.492991+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_648eaf83d2b24d445764257cf6a55525:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 19036
}
```

</details>

---


### Tool call

_source line 294 · 2026-05-23T15:56:27.643779+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

````json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "cost-verify-agent-rl",
  "text": "你是 Reviewer 2，负责**新颖性、完整性与格式合规**审查。\n\n## Venue 信息\n- **目标**: EMNLP 2026（通过 ARR 统一审稿）\n- **截止日期**: 2026-05-25\n- **页数限制**: Long paper，正文 8 页，参考文献不限，Limitations 不计入页数\n- **模板**: ACL style template，[review] 模式\n- **匿名规则**: Double-blind\n- **评分标准**: 5=Consider for Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 论文路径\n- LaTeX 源码: `projects/cost-verify-agent-rl/docs/paper/main.tex`（含 \\input 的各章节文件在同一目录）\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/review_round_3/submitted.pdf`\n\n## 你的审查侧重\n\n### 1. 新颖性与贡献评估\n- \"Dual mechanism diagnosis\" 的新颖性：这是新发现还是已知问题的重新 formalize？\n- Episode-level GRPO 是 GRPO 的原始设计——\"fix\" 的新颖性在哪里？\n- 36% seed 泛化率下，contribution 3 的 claims 是否 overclaim？\n- 与同期方法（HCAPO, Turn-PPO, GiGPO, GAGPO, RC-GRPO, iStar, EDGE-GRPO）的定位是否准确？是否缺少实验对比？\n\n### 2. Related Work 覆盖度\n- 是否遗漏重要的直接竞争/高度相关工作？\n- 对 concurrent work 的 positioning 是否公平？\n- 引用是否都是真实可查的论文？（检查 arXiv ID 格式是否合理）\n\n### 3. 写作质量\n- Abstract 是否 ≤200 words？\n- Claims 与 evidence 是否匹配？（特别注意 abstract/intro/conclusion 中的强表述 vs 实际实验证据）\n- Narrative 逻辑是否清晰？各章节衔接是否顺畅？\n- 是否有 overclaiming？（如 \"resolves\" vs \"addresses\"，\"confirms\" vs \"suggests\"）\n\n### 4. 格式合规\n- 正文是否 ≤8 页？\n- Limitations section 位置是否正确（conclusion 之后、references 之前）？内容是否充分？\n- 匿名要求：是否有去匿名化信息泄露？（代码链接、致谢、自引用）\n- 引用格式是否统一？所有引用是否都有真实作者（非 Anonymous）？\n- 图表质量和位置是否合理？\n\n### 5. Limitations 评估\n- Limitations section 是否涵盖了关键局限？\n- 是否过长或过短？（EMNLP 2026 规范：一小段，3 个点左右）\n\n请按以下格式输出审稿意见：\n\n```\n## Summary\n（2-3 句论文概述）\n\n## Strengths\nS1. ...\nS2. ...\n\n## Weaknesses\nW1. [severity: critical/major/minor] ...\nW2. ...\n\n## Questions\nQ1. ...\n\n## Missing References\n（如有）\n\n## Detailed Comments\n（逐节详细意见）\n\n## Overall Assessment\n- Score: X/5（参照 EMNLP 2026 评分标准）\n- Confidence: X/5\n- 一句话总评\n```"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "cost-verify-agent-rl",
    "text": "你是 Reviewer 2，负责**新颖性、完整性与格式合规**审查。\n\n## Venue 信息\n- **目标**: EMNLP 2026（通过 ARR 统一审稿）\n- **截止日期**: 2026-05-25\n- **页数限制**: Long paper，正文 8 页，参考文献不限，Limitations 不计入页数\n- **模板**: ACL style template，[review] 模式\n- **匿名规则**: Double-blind\n- **评分标准**: 5=Consider for Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 论文路径\n- LaTeX 源码: `projects/cost-verify-agent-rl/docs/paper/main.tex`（含 \\input 的各章节文件在同一目录）\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/review_round_3/submitted.pdf`\n\n## 你的审查侧重\n\n### 1. 新颖性与贡献评估\n- \"Dual mechanism diagnosis\" 的新颖性：这是新发现还是已知问题的重新 formalize？\n- Episode-level GRPO 是 GRPO 的原始设计——\"fix\" 的新颖性在哪里？\n- 36% seed 泛化率下，contribution 3 的 claims 是否 overclaim？\n- 与同期方法（HCAPO, Turn-PPO, GiGPO, GAGPO, RC-GRPO, iStar, EDGE-GRPO）的定位是否准确？是否缺少实验对比？\n\n### 2. Related Work 覆盖度\n- 是否遗漏重要的直接竞争/高度相关工作？\n- 对 concurrent work 的 positioning 是否公平？\n- 引用是否都是真实可查的论文？（检查 arXiv ID 格式是否合理）\n\n### 3. 写作质量\n- Abstract 是否 ≤200 words？\n- Claims 与 evidence 是否匹配？（特别注意 abstract/intro/conclusion 中的强表述 vs 实际实验证据）\n- Narrative 逻辑是否清晰？各章节衔接是否顺畅？\n- 是否有 overclaiming？（如 \"resolves\" vs \"addresses\"，\"confirms\" vs \"suggests\"）\n\n### 4. 格式合规\n- 正文是否 ≤8 页？\n- Limitations section 位置是否正确（conclusion 之后、references 之前）？内容是否充分？\n- 匿名要求：是否有去匿名化信息泄露？（代码链接、致谢、自引用）\n- 引用格式是否统一？所有引用是否都有真实作者（非 Anonymous）？\n- 图表质量和位置是否合理？\n\n### 5. Limitations 评估\n- Limitations section 是否涵盖了关键局限？\n- 是否过长或过短？（EMNLP 2026 规范：一小段，3 个点左右）\n\n请按以下格式输出审稿意见：\n\n```\n## Summary\n（2-3 句论文概述）\n\n## Strengths\nS1. ...\nS2. ...\n\n## Weaknesses\nW1. [severity: critical/major/minor] ...\nW2. ...\n\n## Questions\nQ1. ...\n\n## Missing References\n（如有）\n\n## Detailed Comments\n（逐节详细意见）\n\n## Overall Assessment\n- Score: X/5（参照 EMNLP 2026 评分标准）\n- Confidence: X/5\n- 一句话总评\n```"
  }
}
````

</details>

---


### Tool result

_source line 295 · 2026-05-23T15:56:29.101492+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_648eaf83d2b24d445764257cf6a55525:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1457
}
```

</details>

---


### Assistant

_source line 296 · 2026-05-23T15:56:45.572501+00:00_

Round 1 已启动：

- **视觉审查 Agent**：已派发（并行执行，不阻塞）
- **外部审稿**：未配置，跳过
- **Reviewer 1**（方法严谨性 + 实验设计）：已分配
- **Reviewer 2**（新颖性 + 完整性 + 格式合规）：已分配

等待两位 Reviewer 返回初审意见。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director"
}
```

</details>

---


## Round 21

## Round 21

2 recorded events


### User

_source line 297 · 2026-05-23T16:04:40.856362+00:00_

[Reviewer 1 审稿结果]:
全部 15 页已阅读完毕。现在基于 ARR review form 的官方维度，聚焦 Director 指定的四个审查方向，撰写完整审稿意见。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 298 · 2026-05-23T16:05:59.727251+00:00_

## Summary
本文诊断了 multi-turn LLM agent RL 中 step-independent windowed GRPO 训练的 credit assignment 失败，识别出两个独立机制——policy information loss（M1）和 advantage sign misattribution（M2）——并通过 2×2 factorial 实验分离、direct sign measurement 验证、以及 episode-level GRPO 修复进行了系统研究。11-seed 评估揭示了 seed-dependent OOD generalization（仅 36% seeds 达到显著泛化）。

---

## Strengths

**S1. 问题重要且诊断清晰。** Step-independent windowing 是社区默认实践，本文首次系统诊断其为何失败（而非仅报告失败），Proposition 1/2 给出了 closed-form 的 wrong-sign probability，分析直觉清晰。

**S2. Factorial design 有效分离机制。** A→B 比较隔离 M2（消除 sign misattribution 将 catastrophic collapse 转为 bounded learning），B→D 比较隔离 M1（消除 information loss 使 OOD generalization 成为可能）。两个比较方向互补，实验逻辑清晰。

**S3. 11-seed 系统评估和坦诚报告。** 不仅报告最佳结果，还揭示了 73% stabilize / 36% generalize 的全貌，展示了 seed-dependent transfer gap。这种坦诚在 agent RL 论文中罕见且有价值。

**S4. 连接丰富的 concurrent work。** Related Work 引用了大量 2025-2026 同期工作（HCAPO, Turn-PPO, GiGPO, GAGPO, RC-GRPO, iStar 等），positioning 为 "complementary: they fix the symptom, we diagnose the cause"。

---

## Weaknesses

**W1. [Critical] Theory-experiment gap 处理仍不充分。** Proposition 2 预测 binary reward 下 80.9% wrong-sign rate，实验在 penalty reward 下测得 52%。论文虽用一段解释了 penalty reward 的 variance-breaking 效应，但缺乏 penalty reward 下的修正公式。读者无法从理论预测出 52% 这个数字。如果 theory 只适用于 pure binary reward，应在主文中明确标注适用范围并提供 pure binary reward 的实验验证。Appendix 中有 binomial test 拒绝 H0: P=0.191，但这只证明了 gap 存在，不解释 gap 的定量来源。

**W2. [Critical] Cell C 缺失严重削弱 factorial completeness。** Cell C（full context + step-level advantage）是隔离 M2-without-M1 的关键条件。6 次 attempt 均因 KL spike 崩溃（Appendix D.4），但论文未充分讨论这意味着什么——Cell C 的崩溃本身可能说明 step-level advantage 在 full context 下的行为质性不同于 truncated context，这会影响对 M2 独立效应的结论。当前讨论将其视为工程障碍而非理论信号。

**W3. [Major] "Locally correct action" 操作化的循环性。** Definition 1 定义 locally correct action 为 "replacing them would decrease episode success probability"。但 Section 4.4 的操作化方式是：成功 episode 中所有 valid-action windows 标记为 locally correct。这恰好犯了论文批评的错误——用 episode outcome 标记 local quality。论文称这是 "conservative approximation / upper bound"，但成功 episode 中可能包含多个次优 window（特别是在 50-step trajectories 中），上界有多松没有讨论。

**W4. [Major] Table 1 报告标准不一致。** Caption 称 "best checkpoint per seed"，但：
- Cell A 报告 "best seed"（2 seeds 取最佳）
- Cell B 报告 "best checkpoint (step 5)"
- Cell D 报告 "mean of two seeds"
三个 condition 用了三种不同的汇总方式，直接比较有误导风险。

**W5. [Major] 52.07% credit agreement 的统计检验报告。** 论文称 credit agreement "marginally above random chance"，报告了 p=0.025。但 n=3000, effect size 仅 +2pp。这实际上 *刚好显著*（p<0.05 but >0.01），在多重比较下可能不显著。Wilson CI [50.3%, 53.9%] 说明效应很小。论文应更明确地讨论这是否 meaningful difference vs. statistical artifact。

**W6. [Major] REINFORCE++ baseline 不公平。** REINFORCE++ 跑了 15 步，与 SFT baseline 持平。论文承认 "15 training steps may be insufficient"，但仍将其列入 Table 1 作为 baseline comparison。REINFORCE++ 是 episode-level 的（不受 M2 影响），没有 critic 本来收敛就慢。15 步的比较既不能证明也不能反驳什么。

**W7. [Minor] Window-size sweep 的 "threshold" claim 基于 single seed。** Figure 2(b) 的 h=10 到 h=20 之间的 threshold 仅基于 seed 1。论文已加 "single seed" caveat，但 threshold 的 framing 仍给人 robust finding 的印象。

**W8. [Minor] 8B result (90.3% OOD) 过于突出。** 8B Cell D 达到 90.3% OOD（vs. 1.7B 最佳 30.6%），但这是单 seed 结果。Abstract 中 "cross-scale verification at 8B" 的措辞可能让读者高估证据强度。

---

## Questions

**Q1.** Proposition 2 的推导假设 binary reward。在你们实际使用的 penalty reward 下，能否推导出修正后的 correct-sign probability 的 closed-form 或 bound？

**Q2.** Cell C 崩溃的 KL spike pattern 是否可以用理论框架解释？如果 full context + step-level advantage 导致 extreme advantage magnitudes，这是否意味着 M2 在 full context 下的效应与 truncated context 下质性不同？

**Q3.** 11 seeds 中 generalized seeds（seed1/4/5/6）与 stagnant seeds（seed100/200/300）在 SFT initialization 时是否有可观测的差异（如 initial OOD performance, loss landscape 特征）？

**Q4.** Figure 2(b) 中 h≤20 使用 32-task ID set，episode-level 使用 134-task OOD set，caption 已标注但 magnitudes 不可比。是否有 h=20/h=10 在 OOD set 上的数据？

---

## Missing References

- **StepAgent (2025)**: "StepAgent: Step-Level Reward Modeling for Agent Training" — 与 step-level credit assignment 直接相关
- **AgentTrek (2025)**: "AgentTrek: Agent Trajectory Synthesis via Guiding Replay with Web Tutorials" — 可能与 demonstration-based SFT baseline 相关

---

## Detailed Comments

### Introduction
- P1 "frequently report training instability without diagnosing its root cause" — 需要引用具体论文报告了什么 instability。当前泛泛而论。
- P2 对 concurrent methods 的 positioning ("address the symptom") 准确但可能引起争议。HCAPO 的 hindsight credit assignment 本质上也是一种 diagnosis，不仅仅是 symptom treatment。

### Method
- Section 2.2 的 Figure 1 overview 很好，但 step-independent 的 discount formula (Eq. 2) 中 γ^(N-k) 的作用需要更清楚地说明——它引入 magnitude decay 但不影响 sign。当前在 Section 2.3.2 才提到这一点。
- Section 2.5 Factorial Design 部分简洁有效。

### Theoretical Analysis
- Proposition 1 的 proof sketch 清晰。
- Proposition 2 的 derivation 正确，但 "reward saturation" paragraph 中 "effective learning rate is 0.66 × 0.19 ≈ 12.5%" 的说法有误导性——这不是传统意义上的 learning rate，更像是 "fraction of useful gradient signal"。
- Cumulative divergence (Eq. 6) 中 |A_correct|/|A_wrong| ≈ 1.32 的实测值有用，但仅报告了 per-group weighted average，没有报告方差或分布。

### Experiments
- Table 2 的分类标准明确，p<0.01 threshold 合理。seed2 的 p=0.03 分类为 Stagnant 是保守但正确的选择。
- Section 4.5 的 8B/ScienceWorld 部分："preliminary evidence" 措辞恰当。

### Discussion
- Practitioner guidance (h≥20) 有实用价值。
- Seed-dependent transfer 的讨论过短——这是一个重要的 open question，值得更多分析。

### Limitations
- 覆盖了 3 个关键点（scale/environment 限制、seed variability、eval variance），长度适当。

---

## Overall Assessment

- **Score: 3.5 / 5** (Borderline Conference)
- **Confidence: 4 / 5**
- 核心诊断（dual mechanism）有价值且实验设计巧妙，但 theory-experiment gap 的定量解释不足、Cell C 缺失削弱 factorial 完整性、Table 报告标准不一致降低了可信度。如能充分解决 W1 和 W4，可提升至 Conference 水平。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director"
}
```

</details>

---


## Round 22

## Round 22

6 recorded events


### User

_source line 299 · 2026-05-23T16:10:09.947412+00:00_

[Reviewer 2 审稿结果]:
API Error: {"type":"error","error":{"details":null,"type":"overloaded_error","message":"Overloaded"},"request_id":"req_011CbKnUtQTBMjMqL6pWTZ7V"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 300 · 2026-05-23T16:10:57.027484+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

````json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "cost-verify-agent-rl",
  "text": "你是 Reviewer 1，负责**方法严谨性与实验设计**审查。上次派发因中断未产出完整审稿意见，请重新完成。\n\n## Venue 信息\n- **目标**: EMNLP 2026（通过 ARR 统一审稿）\n- **截止日期**: 2026-05-25\n- **页数限制**: Long paper，正文 8 页，参考文献不限，Limitations 不计入页数\n- **模板**: ACL style template，[review] 模式\n- **匿名规则**: Double-blind\n\n## 论文路径\n- LaTeX 源码: `projects/cost-verify-agent-rl/docs/paper/main.tex`（含 \\input 的各章节文件在同一目录）\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/review_round_3/submitted.pdf`\n\n## 你的审查侧重\n\n### 1. 理论分析严谨性\n- Proposition 1/2 的推导是否正确、假设是否合理\n- Definition 1（\"locally correct action\"）的操作化是否存在逻辑问题\n- Eq. 6 累积发散论证中 \"comparable magnitude\" 假设（文中称实测比值 1.32）的合理性\n- Theory 预测 (19.1% correct sign under binary) 与实验测量 (52% under penalty reward) 之间的 gap 是否被充分解释\n\n### 2. 实验设计\n- 2×2 factorial design 的完整性：Cell C 缺失对结论的影响\n- 统计检验：52.07% credit agreement rate 的统计显著性（报告了 n, p-value, CI 吗？）\n- 11-seed 评估的分类标准（Collapsed/Stagnant/Generalized）是否合理\n- Table 1 的报告标准是否一致（best checkpoint per seed vs. mean vs. best seed 混用？）\n\n### 3. 数据一致性\n- Table 1/2 的数据是否与正文描述一致\n- 8B 和 ScienceWorld 单 seed 结果的证据力\n- REINFORCE++ 对比公平性（仅 15 步训练）\n- Window-size sweep 的 cliff claim 是否有足够统计支撑\n\n### 4. 跨规模/跨环境验证\n- 8B 单 seed 结果（90.3% OOD）的 claims 是否适当 hedge\n- ScienceWorld 验证的深度是否足够\n\n请按以下格式输出审稿意见：\n\n```\n## Summary\n（2-3 句论文概述）\n\n## Strengths\nS1. ...\nS2. ...\n\n## Weaknesses\nW1. [severity: critical/major/minor] ...\nW2. ...\n\n## Questions\nQ1. ...\n\n## Missing References\n（如有）\n\n## Detailed Comments\n（逐节详细意见）\n\n## Overall Assessment\n- Score: X/5（参照 EMNLP 2026 评分标准）\n- Confidence: X/5\n- 一句话总评\n```"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "cost-verify-agent-rl",
    "text": "你是 Reviewer 1，负责**方法严谨性与实验设计**审查。上次派发因中断未产出完整审稿意见，请重新完成。\n\n## Venue 信息\n- **目标**: EMNLP 2026（通过 ARR 统一审稿）\n- **截止日期**: 2026-05-25\n- **页数限制**: Long paper，正文 8 页，参考文献不限，Limitations 不计入页数\n- **模板**: ACL style template，[review] 模式\n- **匿名规则**: Double-blind\n\n## 论文路径\n- LaTeX 源码: `projects/cost-verify-agent-rl/docs/paper/main.tex`（含 \\input 的各章节文件在同一目录）\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/review_round_3/submitted.pdf`\n\n## 你的审查侧重\n\n### 1. 理论分析严谨性\n- Proposition 1/2 的推导是否正确、假设是否合理\n- Definition 1（\"locally correct action\"）的操作化是否存在逻辑问题\n- Eq. 6 累积发散论证中 \"comparable magnitude\" 假设（文中称实测比值 1.32）的合理性\n- Theory 预测 (19.1% correct sign under binary) 与实验测量 (52% under penalty reward) 之间的 gap 是否被充分解释\n\n### 2. 实验设计\n- 2×2 factorial design 的完整性：Cell C 缺失对结论的影响\n- 统计检验：52.07% credit agreement rate 的统计显著性（报告了 n, p-value, CI 吗？）\n- 11-seed 评估的分类标准（Collapsed/Stagnant/Generalized）是否合理\n- Table 1 的报告标准是否一致（best checkpoint per seed vs. mean vs. best seed 混用？）\n\n### 3. 数据一致性\n- Table 1/2 的数据是否与正文描述一致\n- 8B 和 ScienceWorld 单 seed 结果的证据力\n- REINFORCE++ 对比公平性（仅 15 步训练）\n- Window-size sweep 的 cliff claim 是否有足够统计支撑\n\n### 4. 跨规模/跨环境验证\n- 8B 单 seed 结果（90.3% OOD）的 claims 是否适当 hedge\n- ScienceWorld 验证的深度是否足够\n\n请按以下格式输出审稿意见：\n\n```\n## Summary\n（2-3 句论文概述）\n\n## Strengths\nS1. ...\nS2. ...\n\n## Weaknesses\nW1. [severity: critical/major/minor] ...\nW2. ...\n\n## Questions\nQ1. ...\n\n## Missing References\n（如有）\n\n## Detailed Comments\n（逐节详细意见）\n\n## Overall Assessment\n- Score: X/5（参照 EMNLP 2026 评分标准）\n- Confidence: X/5\n- 一句话总评\n```"
  }
}
````

</details>

---


### Tool result

_source line 301 · 2026-05-23T16:11:14.703823+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_648eaf83d2b24d445764257cf6a55525:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 17676
}
```

</details>

---


### Tool call

_source line 302 · 2026-05-23T16:11:15.005220+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

````json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "cost-verify-agent-rl",
  "text": "你是 Reviewer 2，负责**新颖性、完整性与格式合规**审查。上次派发因 API 过载失败，请重新完成。\n\n## Venue 信息\n- **目标**: EMNLP 2026（通过 ARR 统一审稿）\n- **截止日期**: 2026-05-25\n- **页数限制**: Long paper，正文 8 页，参考文献不限，Limitations 不计入页数\n- **模板**: ACL style template，[review] 模式\n- **匿名规则**: Double-blind\n- **评分标准**: 5=Consider for Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 论文路径\n- LaTeX 源码: `projects/cost-verify-agent-rl/docs/paper/main.tex`（含 \\input 的各章节文件在同一目录）\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/review_round_3/submitted.pdf`\n\n## 你的审查侧重\n\n### 1. 新颖性与贡献评估\n- \"Dual mechanism diagnosis\" 的新颖性：这是新发现还是已知问题的重新 formalize？\n- Episode-level GRPO 是 GRPO 的原始设计——\"fix\" 的新颖性在哪里？\n- 36% seed 泛化率下，contribution 3 的 claims 是否 overclaim？\n- 与同期方法（HCAPO, Turn-PPO, GiGPO, GAGPO, RC-GRPO, iStar, EDGE-GRPO）的定位是否准确？是否缺少实验对比？\n\n### 2. Related Work 覆盖度\n- 是否遗漏重要的直接竞争/高度相关工作？\n- 对 concurrent work 的 positioning 是否公平？\n- 引用是否都是真实可查的论文？（检查 arXiv ID 格式是否合理）\n\n### 3. 写作质量\n- Abstract 是否 ≤200 words？\n- Claims 与 evidence 是否匹配？（特别注意 abstract/intro/conclusion 中的强表述 vs 实际实验证据）\n- Narrative 逻辑是否清晰？各章节衔接是否顺畅？\n- 是否有 overclaiming？（如 \"resolves\" vs \"addresses\"，\"confirms\" vs \"suggests\"）\n\n### 4. 格式合规\n- 正文是否 ≤8 页？\n- Limitations section 位置是否正确（conclusion 之后、references 之前）？内容是否充分？\n- 匿名要求：是否有去匿名化信息泄露？（代码链接、致谢、自引用）\n- 引用格式是否统一？所有引用是否都有真实作者（非 Anonymous）？\n- 图表质量和位置是否合理？\n\n### 5. Limitations 评估\n- Limitations section 是否涵盖了关键局限？\n- 是否过长或过短？（EMNLP 2026 规范：一小段，3 个点左右）\n\n请按以下格式输出审稿意见：\n\n```\n## Summary\n（2-3 句论文概述）\n\n## Strengths\nS1. ...\nS2. ...\n\n## Weaknesses\nW1. [severity: critical/major/minor] ...\nW2. ...\n\n## Questions\nQ1. ...\n\n## Missing References\n（如有）\n\n## Detailed Comments\n（逐节详细意见）\n\n## Overall Assessment\n- Score: X/5（参照 EMNLP 2026 评分标准）\n- Confidence: X/5\n- 一句话总评\n```"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "cost-verify-agent-rl",
    "text": "你是 Reviewer 2，负责**新颖性、完整性与格式合规**审查。上次派发因 API 过载失败，请重新完成。\n\n## Venue 信息\n- **目标**: EMNLP 2026（通过 ARR 统一审稿）\n- **截止日期**: 2026-05-25\n- **页数限制**: Long paper，正文 8 页，参考文献不限，Limitations 不计入页数\n- **模板**: ACL style template，[review] 模式\n- **匿名规则**: Double-blind\n- **评分标准**: 5=Consider for Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 论文路径\n- LaTeX 源码: `projects/cost-verify-agent-rl/docs/paper/main.tex`（含 \\input 的各章节文件在同一目录）\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/review_round_3/submitted.pdf`\n\n## 你的审查侧重\n\n### 1. 新颖性与贡献评估\n- \"Dual mechanism diagnosis\" 的新颖性：这是新发现还是已知问题的重新 formalize？\n- Episode-level GRPO 是 GRPO 的原始设计——\"fix\" 的新颖性在哪里？\n- 36% seed 泛化率下，contribution 3 的 claims 是否 overclaim？\n- 与同期方法（HCAPO, Turn-PPO, GiGPO, GAGPO, RC-GRPO, iStar, EDGE-GRPO）的定位是否准确？是否缺少实验对比？\n\n### 2. Related Work 覆盖度\n- 是否遗漏重要的直接竞争/高度相关工作？\n- 对 concurrent work 的 positioning 是否公平？\n- 引用是否都是真实可查的论文？（检查 arXiv ID 格式是否合理）\n\n### 3. 写作质量\n- Abstract 是否 ≤200 words？\n- Claims 与 evidence 是否匹配？（特别注意 abstract/intro/conclusion 中的强表述 vs 实际实验证据）\n- Narrative 逻辑是否清晰？各章节衔接是否顺畅？\n- 是否有 overclaiming？（如 \"resolves\" vs \"addresses\"，\"confirms\" vs \"suggests\"）\n\n### 4. 格式合规\n- 正文是否 ≤8 页？\n- Limitations section 位置是否正确（conclusion 之后、references 之前）？内容是否充分？\n- 匿名要求：是否有去匿名化信息泄露？（代码链接、致谢、自引用）\n- 引用格式是否统一？所有引用是否都有真实作者（非 Anonymous）？\n- 图表质量和位置是否合理？\n\n### 5. Limitations 评估\n- Limitations section 是否涵盖了关键局限？\n- 是否过长或过短？（EMNLP 2026 规范：一小段，3 个点左右）\n\n请按以下格式输出审稿意见：\n\n```\n## Summary\n（2-3 句论文概述）\n\n## Strengths\nS1. ...\nS2. ...\n\n## Weaknesses\nW1. [severity: critical/major/minor] ...\nW2. ...\n\n## Questions\nQ1. ...\n\n## Missing References\n（如有）\n\n## Detailed Comments\n（逐节详细意见）\n\n## Overall Assessment\n- Score: X/5（参照 EMNLP 2026 评分标准）\n- Confidence: X/5\n- 一句话总评\n```"
  }
}
````

</details>

---


### Tool result

_source line 303 · 2026-05-23T16:11:16.465762+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_648eaf83d2b24d445764257cf6a55525:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1460
}
```

</details>

---


### Assistant

_source line 304 · 2026-05-23T16:11:27.832702+00:00_

两位 Reviewer 已重新派发，等待审稿结果返回。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director"
}
```

</details>

---


## Round 23

## Round 23

2 recorded events


### User

_source line 305 · 2026-05-23T16:16:28.537210+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 审稿意见（新颖性、完整性与格式合规）

---

## Summary

本文诊断了 step-independent windowing 训练多轮 LLM agent 时的两种失败机制：(1) 策略信息丢失（M1，窗口截断跨步上下文导致性能天花板），(2) 优势符号错误归因（M2，episode 级二值奖励被统一赋予所有窗口，导致多数梯度方向错误）。通过 2×2 factorial 实验在 ALFWorld 上隔离两种机制，表明 episode-level GRPO（即 GRPO 原始设计）可同时消除两种失败模式，实现 OOD 泛化。初步的 8B 跨规模和 ScienceWorld 跨环境验证提供了扩展证据。

---

## Strengths

**S1. 系统化的 factorial 实验设计。** 2×2 设计（trajectory scope × advantage granularity）超越了该领域常见的 ad-hoc 消融，提供了清晰的因果隔离框架（Section 2.5, Table 1）。A→B 对比隔离 M2，B→D 对比隔离 M1，逻辑链条完整。

**S2. 可验证的理论预测。** Proposition 1-2 给出了二值奖励下符号正确概率的定量公式（Equation 4: P(correct|update) = p/(1-(1-p)^K)），在 p=12.5%, K=8 时预测 19.1% 正确率，并在 Section 4.4 和 Figure 4 中得到了实证验证。理论预测与实测的一致性增强了说服力。

**S3. 诚实的局限报告。** 36% seed 泛化率、OOD 评估的高方差（seed5 的 30pp range）、Cell C 的训练不稳定——这些不利结果都被明确报告（Limitations, Table 2），没有被掩盖。Contribution 3 的 "necessary but not sufficient" 框架也体现了恰当的审慎。

**S4. 全面的 Related Work 覆盖。** Section 5 讨论了 15+ 同期方法（Turn-PPO, HCAPO, GAGPO, GiGPO, SWEET-RL, iStar, EDGE-GRPO, MC-GRPO, RC-GRPO, OAR, GRPO-λ, IRC, MT-GRPO, RAGEN-2, GRPO-Collapse），定位公平，明确区分本文的诊断贡献与这些方法的算法贡献。

**S5. 清晰的可视化。** Figure 1 对 step-independent vs episode-level 的对比图直观有效；Figure 2 将理论预测可视化；Figure 3b 的窗口大小 sweep 揭示了阈值效应。

---

## Weaknesses

**W1. [critical] Episode-level GRPO 无方法论新颖性。** 论文在 Section 2.4 (约 line 135) 明确承认 episode-level training "is GRPO's original design; step-independent windowing is the deviation。" 所提出的 "fix" 是撤销一个偏离，而非提出新方法。尽管诊断贡献有价值，但将回归原始算法包装为 Contribution 3（"Episode-level fix"）膨胀了论文的贡献声明。严格来说，论文的 actionable output 是 "不要用 step-independent windowing"——这是一个负面结果，不是新方法。

**W2. [critical] 完全缺乏与同期方法的实验对比。** Related Work 讨论了 15+ 方法，其中多个在同一 benchmark 上报告了结果（如 HCAPO 在 ALFWorld 上用 Qwen2.5-7B 取得 +13.8%），但实验部分仅对比 SFT baseline 和作者自己的 factorial conditions。论文声称诊断框架能 "inform when finer-grained credit is safe"（Section 5, page 7），但没有任何实验证据支持这一声明。这是最严重的缺陷：一篇定位于 "诊断 + 指导" 的论文，必须展示诊断如何指导实践。至少应与 HCAPO（同 benchmark）和 Turn-PPO（同问题）做实验对比。

**W3. [major] Factorial 设计不完整——Cell C 缺失。** 2×2 设计依赖 4 个条件来清晰隔离两种机制，但 Cell C（full trajectory + step-level advantage，仅隔离 M1）因 "persistent training instability" 被放入 Appendix D。这破坏了 factorial 的完整性：论文无法展示单独移除 M1 的效果。更重要的是，Cell C 的不稳定性暗示 M1 和 M2 之间存在交互效应，而论文的加性框架未能捕捉这一点。如果 M2 确实是 "更根本的机制"（Section 3 声称 sign errors 比 magnitude imprecision 更具破坏性），那 Cell C（保留 M2、移除 M1）应该表现类似 Cell A——但实际出现了不同的失败模式（instability vs collapse），这需要解释。

**W4. [major] 主实验统计力严重不足。** Table 1 的 factorial 对比仅用 2 seeds 的均值。鉴于 Table 2 显示 11 seeds 下 OOD 结果从 0% 到 38.7% 的巨大方差，2-seed 对比的可靠性极低。核心的机制隔离声明建立在 n=2 之上——这不构成统计证据。应至少使用与 Cell D 相同的 11 seeds 进行 factorial 比较。

**W5. [major] 双机制诊断形式化了已知问题。** M1（窗口截断导致信息丢失）本质上是 partial observability 问题——RL 中有大量文献。M2（共享 episode 奖励导致符号错误）是经典 credit assignment 问题在 GRPO 框架下的具体实例。Proposition 1 的结论（正确符号概率 → 基础成功率 p）在直觉上并不令人惊讶：低成功率任务中多数 episode 失败，因此多数窗口获得负优势。多个同期工作（MC-GRPO 观察到 sign disagreement, HCAPO 验证 sign correctness 是关键瓶颈, IRC 发现 advantage misalignment）独立地识别了同一问题，稀释了诊断的新颖性。

**W6. [minor] Conclusion 的泛化声明超出实验证据。** Section 7 称 finding "applies to any agent RL method combining step-level windowing, sparse binary reward, and group-relative normalization"。实验仅测试了 GRPO 在 ALFWorld（和初步的 ScienceWorld）上的表现。"any agent RL method" 的声明远超实验范围。

**W7. [minor] 多个引用存在准确性问题。** 经 web search 验证：
- **Turn-PPO** (Li et al., 2026a): 论文引用 arXiv:2512.17906，实际 ID 为 arXiv:2512.17008；且该文已被 EACL 2026 Findings 接收，应引用正式出版版本。
- **MC-GRPO** (Kim, 2025): 论文中标题似为 "Medium-context..."，实际标题为 "Median-Centered Group Relative Policy Optimization for Small-Rollout Reinforcement Learning"；作者名为 Youngeun Kim（非 Youngjun），arXiv ID 为 2601.22582（2026年1月）。
- **IRC** (Modesna et al., 2026): 作者名拼写与 arXiv 记录有显著差异（如 Modecrua vs Modesna, Kaewtawee vs Kawsatawee）。
- **GRPO-λ** (Parthasarathi et al., 2025): 可能因字体渲染问题显示为 "GRPO-3"。
这些错误虽不影响论文核心论点，但反映了引用工作的审慎程度不足。

**W8. [minor] 潜在匿名性泄露。** Page 5 脚注 1 提供了 GitHub 风格的代码路径（"RAGEN-47/RAGEN"）。如果这标识了作者身份，则违反 double-blind 要求。如果是匿名化链接，应更明确地说明。

---

## Questions

**Q1.** Cell C 为什么出现训练不稳定性，而 Cell A 和 Cell B 没有？如果 M1 和 M2 的效应是加性的（论文的隐含假设），Cell C（保留 M2、移除 M1）的行为应可预测。不稳定性暗示 M1 可能有某种 "正则化" 效果，或 M1-M2 之间存在交互作用。

**Q2.** 36% 泛化的 seeds 与 64% 停滞的 seeds 有何区别？是否分析了初始化特征、早期训练动态、或 in-distribution 性能轨迹？Table 2 中 seed100 的 "minimal improvement from step 5 to step 15" 是否提供了任何线索？

**Q3.** Proposition 2 在 p=12.5% 时计算 19.1% 正确率。随着训练推进 p 增加，正确率也会改善。是否存在 phase transition——在某个 p 值之上训练变得 self-correcting？如果存在，step-independent training 或许只需要一个更好的初始化（higher p at start）即可工作。

**Q4.** HCAPO 在 ALFWorld 上用 Qwen2.5-7B 取得 +13.8% 改进。论文的诊断框架能否预测 HCAPO 的成功（或失败条件）？如果不能，"inform when finer-grained credit is safe" 的声明缺乏支撑。

**Q5.** Dense reward（Appendix D, Figure 6b）显示 agent 最大化格式级奖励而不解决任务（action validity 97.5%, task success 0%）。这是否意味着 M2 在 dense reward 下转变为 reward hacking？这似乎是一个重要发现但论文仅在 appendix 中简要提及。

---

## Missing References

- **Harutyunyan et al. (2019)**, "Hindsight Credit Assignment" (NeurIPS) — 序列决策中 hindsight credit assignment 的基础工作，与 M2 直接相关。
- **Arjona-Medina et al. (2019)**, "RUDDER: Return Decomposition for Delayed Rewards" (NeurIPS) — 提出 delayed reward 的 return decomposition，与 M2 的 reward attribution 问题高度相关。
- 论文未引用 partial observability / POMDP 文献来支撑 M1 的分析——这是一个概念上的缺失。

---

## Detailed Comments

### Abstract
约 155 words，远在 200 限制之内。✓ 内容准确概括了贡献。但 "eliminates both failure modes" 与 Conclusion 中的 "addresses both mechanisms" 存在措辞不一致——前者更强，后者更准确。

### Section 1 (Introduction)
三个贡献结构清晰。Contribution 3 的 "necessary but not sufficient" 框架诚实。但 "Our primary contribution is diagnostic" 的表述（page 2, ~line 80）暗示论文自我定位为分析型贡献——这与将 episode-level GRPO 列为 contribution 之间有张力。

### Section 2 (Method)
问题形式化（POMDP）标准且正确。GRPO 描述准确。Section 2.3 的 M1/M2 定义清晰。但 M1 本质是 partial observability，论文未建立与 POMDP 文献的联系。Section 2.5 的 factorial 设计是论文的实验骨架，但 Cell C 的缺失在此已埋下隐患。

### Section 3 (Theoretical Analysis)
Proposition 1-2 在二值奖励假设下数学正确。P(correct|update) = p/(1-(1-p)^K) 的推导可验证。但 Equation 5 的 cumulative divergence 论证将 "wrong-sign gradient" 等同于 "policy moves away from good behavior"——在 policy gradient 方法中，梯度方向与策略改进方向不完全等价（因 KL constraint、learning rate 等因素），论证存在过度简化。

### Section 4 (Experiments)
Factorial 实验是最大亮点，但 2-seed 是最大弱点。Window size sweep（Figure 3b）揭示 h=10-20 的阈值效应——这暗示中间方案（larger windows, overlapping windows）可能有效，但论文将问题呈现为二元（step-independent vs episode-level）。Section 4.4 的 sign-episode agreement 验证是强有力的经验证据。

Cross-scale (Table 4/Figure 5) 和 cross-environment 验证虽标记为 "preliminary"，但增加了结果的可信度。

### Section 5 (Related Work)
覆盖全面，定位公平。"We diagnose why the default fails, informing when finer-grained credit is safe" 是有吸引力的定位，但缺乏实验支撑成为空洞声明。

### Section 6 (Discussion)
M1-M2 vicious cycle 的论述有趣但定性。Connection to classical credit assignment（Appendix A.4）有价值但应在主文中更突出。

### Section 7 (Conclusion) & Limitations
结论措辞适当（"addresses" 而非 "eliminates"）。Limitations 涵盖 4-5 个要点，长度略超 "一小段、3 个点" 的 EMNLP 建议，但内容实质且诚实。位置正确（Conclusion 之后、References 之前）。✓

### 格式合规检查
| 项目 | 状态 |
|------|------|
| 正文 ≤8 页 | ✓ Sections 1-7 在 8 页内 |
| Limitations 位置 | ✓ Conclusion 后、References 前 |
| 单一 Limitations section | ✓ Appendix 无重复 |
| Abstract ≤200 words | ✓ ~155 words |
| Double-blind 匿名 | ⚠ 脚注 1 代码链接存疑 |
| 引用格式统一 | ⚠ 部分引用有准确性问题 |
| 所有引用有真实作者 | ✓ 无 "Anonymous" 引用 |
| 图表质量 | ✓ 清晰、位置合理 |

---

## Overall Assessment

### ARR 官方维度打分

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.0/5 | 理论在二值奖励假设下成立且可验证；Cell C 缺失破坏 factorial 完整性；2-seed 主实验不构成统计证据 |
| Excitement | 2.5/5 | 诊断框架有用但核心 insight 已知（credit assignment + partial observability）；fix 无新颖性；36% 泛化率限制实用价值 |
| Reproducibility | 4.0/5 | 超参数完整（Appendix B）、训练细节详尽、单一环境降低复现门槛 |

- **Overall Score: 3.0 / 5 (Findings)**
- **Confidence: 4 / 5**
- **一句话总评**: 论文提供了系统化的诊断框架来分析 step-independent agent RL 中的 credit assignment 失败，理论可验证、实验设计有新意，但"fix"无方法论新颖性（episode-level GRPO = 原始 GRPO），完全缺乏与 15+ 同期方法的实验对比，主实验仅 2 seeds 的统计力不足以支撑核心声明——总体贡献适合 Findings track。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 306 · 2026-05-23T16:16:36.189934+00:00_

Reviewer 2 审稿意见已收到，评分 3.0/5 (Findings)。等待 Reviewer 1 返回审稿意见后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director"
}
```

</details>

---


## Round 24

## Round 24

2 recorded events


### User

_source line 307 · 2026-05-23T16:16:46.385809+00:00_

[Reviewer 2 审稿结果]:
审稿意见已提交给 Review Director。

核心判断：**3.0/5 (Findings)**。主要依据：

1. **新颖性不足**：Episode-level GRPO 是 GRPO 原始设计，"fix" 无方法论贡献；双机制诊断形式化了已知的 credit assignment + partial observability 问题，多个同期工作独立发现了相同现象。

2. **实验对比缺失**：Related Work 讨论了 15+ 同期方法但实验部分完全没有对比（HCAPO 甚至在同一 benchmark ALFWorld 上有结果）。

3. **统计力不足**：核心 factorial 对比仅 2 seeds，而 11-seed 评估显示 OOD 结果从 0% 到 38.7% 的巨大方差。

4. **Cell C 缺失**：2×2 factorial 缺少一个条件（训练不稳定被放入 appendix），破坏了因果隔离的完整性。

5. **引用问题**：Turn-PPO arXiv ID 错误、MC-GRPO 标题错误、IRC 作者名拼写有误。

优势方面：factorial 设计本身有新意、理论预测可验证、局限报告诚实、Related Work 覆盖全面、格式基本合规。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 308 · 2026-05-23T16:16:57.689494+00:00_

Reviewer 2 审稿意见已收到（3.0/5 Findings）。等待 Reviewer 1 的审稿意见返回后进入 Step 2 交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director"
}
```

</details>

---


## Round 25

## Round 25

6 recorded events


### User

_source line 309 · 2026-05-23T16:17:34.434938+00:00_

[Reviewer 1 审稿意见]:
## Summary

本文诊断了多轮 LLM agent RL 中 step-independent windowing 的一种结构性信用分配病理——"sign misattribution"。作者提出双机制框架：M1（信息丢失，推理层截断跨窗口上下文）和 M2（符号错误归因，训练层将 episode 结果的 advantage 符号错误传播给局部正确的动作）。理论分析（Proposition 1/2）推导出 binary reward 下仅 19.1% 梯度更新方向正确。实验采用 2×2 factorial design（缺失 Cell C），在 ALFWorld 1.7B/8B 和 ScienceWorld 上验证 episode-level GRPO 的修正效果。11-seed 评估显示仅 36% seeds 达到显著 OOD 泛化。

## Strengths

**S1. 问题定位有价值且动机清晰。** 将 step-independent training 的失败分解为两个独立机制（M1 信息丢失 + M2 符号错误归因）是一个有意义的诊断贡献，概念框架（Figure 1）清晰直观。社区普遍采用 step-independent windowing（RAGEN, GAGRPO 等），诊断其系统性缺陷具有实际意义。

**S2. 理论分析在其有效范围内是正确的。** Proposition 1/2 在 binary reward 假设下的推导过程逻辑严密。Eq. 4 的推导（P(correct|update) = p/(1-(1-p)^K)）可以验证：p=0.125, K=8 时确实得到 19.04%。三种情况的分类（episode 成功、episode 失败但组内有成功、全组失败）是完备的。

**S3. 实验报告的诚实度高于平均水平。** 论文坦诚报告了 Cell C 失败（Appendix D）、11-seed 中仅 36% 泛化、单 seed 跨规模结果的局限性、以及 seed-dependent transfer 仍是 open question。这种诚实度在 ML 论文中值得肯定。

**S4. 11-seed 评估是有价值的设计。** 多数论文只报告最佳 seed，本文的 11-seed 系统评估揭示了 episode-level GRPO 本身的高方差问题，为社区提供了更真实的预期。

**S5. Factorial 实验设计思路正确。** 2×2 factorial（即使不完整）比标准 ablation 更能支撑因果推断，A→B 对比（隔离 M2）和 B→D 对比（隔离 M1）的逻辑链条清晰。

## Weaknesses

**W1. [critical] Proposition 1/2 隐含假设"episode 成功 ⟹ 所有窗口局部正确"，但这与 Definition 1 矛盾。**
- 具体位置：Section 3, Appendix A.1
- 问题：Proposition 1 的证明将成功 episode 中所有窗口视为获得"correct sign"（正梯度=正确方向）。但 Definition 1 定义 locally correct action 需要"在 oracle 下获得正 advantage"。一个成功 episode 可以包含次优甚至有害的局部动作（agent 侥幸通过），这些窗口获得正 advantage 实际上是"incorrect sign"。因此 Proposition 2 的 19.1% 是 P(correct sign) 的**上界**，而非精确值，但论文将其作为精确预测使用。
- 为什么影响接收：核心理论贡献的内部一致性问题。如果成功 episode 中也存在符号错误，实际的 correct sign probability 更低，这反而强化了论文论点——但当前的理论表述不够严谨。
- 建议：明确 Proposition 1/2 的隐含假设（episode 成功 ⟹ 全窗口局部正确），或将 19.1% 明确标注为上界。

**W2. [critical] Cell C 缺失实质性破坏了 2×2 factorial 的因果推断力。**
- 具体位置：Section 2.5, Section 4.2, Appendix D
- 问题：Cell C（full trajectory + step-level advantage）本应隔离 M2（无 M1 干扰），是验证"M2 是独立有害机制"的关键对照。其缺失意味着：(1) 无法确认 M2 在无 M1 条件下是否独立导致退化；(2) 无法排除 M1 和 M2 之间存在交互效应（interaction effect）。Appendix D 报告 Cell C 在 6 次不同超参数配置下均出现 KL 散度爆炸和 NaN loss，但未分析**为什么**全 trajectory + step-level advantage 会导致训练不稳定——这本身可能暗示两个机制并非如论文假设的那样可分离。
- 为什么影响接收：论文声称"comparing A vs. B isolates sign misattribution; comparing B vs. D isolates information loss"（Section 4.2），但没有 Cell C 的交叉验证，这一因果分离声明缺乏完整支撑。
- 建议：(1) 深入分析 Cell C 失败的原因（是梯度方差过大？是 step-level normalization 在长序列上的数值问题？）；(2) 讨论 Cell C 缺失对因果推断的具体限制；(3) 考虑是否可通过缩短序列长度或梯度裁剪使 Cell C 稳定运行。

**W3. [critical] 理论分析仅覆盖 binary reward，但全部主实验使用 penalty reward，理论-实验脱节。**
- 具体位置：Section 3 (Propositions 1-2) vs. Section 4 (experiments)
- 问题：Proposition 1/2 在 binary reward R∈{0, r₊} 下推导，给出 19.1% correct sign rate。但 Section 4.1 明确说实验使用 penalty reward（invalid action 扣 0.1）。实验测得 52% credit agreement rate（Section 4.4），论文仅以"reflects the reward structure difference"（Appendix A.2）一笔带过，未提供 penalty reward 下的对应理论分析。这意味着论文的核心量化预测（19.1%）在主实验设置下从未被直接验证。
- Appendix A.2 用 binomial test 拒绝了 H₀: P=0.191（p < 10⁻¹⁰），但这只证明 52% ≠ 19.1%，不解释 52% 的理论来源。
- 为什么影响接收：理论贡献和实验验证之间存在断层。如果理论只能预测 binary reward 的行为，其指导意义有限，因为实际系统很少使用纯 binary reward。
- 建议：(1) 推导 penalty reward 下的 correct sign probability（至少给出定性方向）；(2) 在 binary reward 设置下直接验证 19.1% 预测（Figure 4 只验证了 sign-episode correlation=100%，但这是一个不同的指标）。

**W4. [major] 52% credit agreement rate 的统计显著性很弱，作为核心实证证据不足。**
- 具体位置：Section 4.4
- 问题：52.07% 被描述为"marginally above random chance"。n≈3000 窗口下，52% vs 50%（随机基线）的 z-test: z = (0.52-0.50)/√(0.50×0.50/3000) ≈ 2.19, p ≈ 0.028。这仅达到 marginal significance（且未做多重比较校正）。作为论文核心 claim"step-independent training 产生符号错误归因"的主要实证证据，这个效应量（2 个百分点）和统计强度都偏弱。
- 论文确实坦诚地用了"marginally above random chance"措辞，但后续讨论中仍将此作为"confirms sign misattribution as the causal driver"（Section 4.4 末尾）的依据，措辞过强。
- 建议：(1) 报告 52% vs 50% 的正式检验结果（z, p, 95% CI）；(2) 软化 causal driver 的措辞；(3) 考虑是否可以增加 n 或使用更灵敏的指标。

**W5. [major] Table 1 报告标准不一致，影响跨 Cell 可比性。**
- 具体位置：Table 1 caption (page 5)
- 问题：Cell A 报告"best seed"，Cell B 报告"best checkpoint (step 5)"，Cell D 报告"mean of two seeds"。三种不同的报告标准使得跨 Cell 比较缺乏公平性。更值得注意的是，Cell D 的 OOD range 为 10.4-23.9%，其中**一个 seed（10.4%）低于 SFT baseline（12.56%）**。仅报告 mean（17.16%）掩盖了这一重要信息。
- 建议：所有 Cell 统一报告 mean ± std（或全部 seed 结果），并在正文中讨论 Cell D 单 seed 低于 SFT baseline 的情况。

**W6. [major] 8B 单 seed 结果（90.3% OOD）的证据力极弱，hedge 不足。**
- 具体位置：Section 4.6, Table 4 (Appendix C), Figure 5
- 问题：1.7B 的 11-seed 评估已经表明仅 36% seeds 泛化。在这一前提下，8B 的单 seed 结果（90.3% OOD）几乎不能支撑任何 claim。论文用"preliminary evidence"修饰，但在 abstract 中写"effects persisting at 8B scale"没有任何 hedge。ScienceWorld 同样是单 seed。
- 为什么影响接收：8B 和跨环境是论文 generality claim 的基础，但证据力过弱。
- 建议：(1) abstract 中加上"single-seed"限定词；(2) 正文中明确讨论：给定 1.7B 的高 seed 方差，单 seed 8B 结果可能恰好落在 generalized 区间，不能排除其他 seed 会 collapse；(3) 如果资源允许，补充至少 2-3 个 8B seed。

**W7. [major] REINFORCE++ 对比不公平（仅 15 步训练）。**
- 具体位置：Appendix D
- 问题：REINFORCE++ 仅训练 15 步后被判定为"matches the SFT baseline without improvement"。论文自己承认"15 training steps may be insufficient for REINFORCE++ to converge"，但仍在正文和 appendix 中将此作为 episode-level training 优越性的佐证（"suggesting that per-token advantage normalization alone does not help"）。15 步对于一个需要从 episode returns bootstrapping 的算法来说明显不足。
- 建议：要么给 REINFORCE++ 充分训练步数，要么删除这个对比，或明确标注此对比不具结论性。

**W8. [minor] Window-size sweep 的 cliff claim 基于单 seed。**
- 具体位置：Section 4.4, Figure 3b
- 问题：h=10 和 h=20 之间的"threshold"仅在 seed 1 上观察到。论文承认"multi-seed verification is needed to confirm its robustness"，但在讨论中仍以此为依据论述（Section 6 提到"step-level windowing" as a structural property）。
- 建议：将 cliff claim 的措辞从描述性改为假设性（"We observe a possible threshold..."），或补充多 seed 验证。

**W9. [minor] Eq. 6 "comparable magnitude" 假设的合理性论证单薄。**
- 具体位置：Section 3, Eq. 5-6
- 问题：累积发散论证的关键假设是 sign error 和 magnitude 的效应"comparable"。论文引用实测 |p₊|/|p₋| 比值为 1.32 作为支撑。但 (1) 1.32 是单个训练阶段的测量值，不同训练阶段可能差异很大；(2) 论文未说明这是在什么条件下（哪个 seed、哪个训练步、什么 reward 结构）测得的。一个单点测量不足以支撑"comparable magnitude"的一般性声明。
- 建议：报告 |p₊|/|p₋| 在多个训练步/seeds 上的分布，或将此论证弱化为"在我们的实验条件下"。

**W10. [minor] Definition 1 的操作化与理论定义之间存在 gap。**
- 具体位置：Section 3 (Definition 1) vs. Section 4.4 (credit agreement)
- 问题：Definition 1 要求"在 oracle 下获得正 advantage"，但 Section 4.4 的操作化仅检查窗口是否包含 valid actions + episode 是否成功。Action validity（格式合规）是 local correctness 的必要条件而非充分条件——一个 valid 但 suboptimal 的动作不一定 locally correct。论文未讨论这一 gap 对测量精度的影响。
- 建议：承认操作化是 Definition 1 的宽松近似（upper bound on true local correctness），并讨论可能的 false positive rate。

## Questions

**Q1.** Cell C 的训练不稳定是否可能暗示 M1 和 M2 之间存在非独立的交互效应？如果是，双机制分离的框架是否需要修正？

**Q2.** 在 binary reward 设置下（Figure 4 左侧），sign-episode correlation 达到 100%。但 Proposition 2 预测 binary 下 P(correct sign|update) = 19.1%。100% sign-episode correlation 和 19.1% correct sign rate 如何同时成立？这两个指标的精确定义和区别是什么？

**Q3.** Table 2 的 11-seed 中，Collapsed/Stagnant/Generalized 三类的分类阈值是否敏感？如果将"90% drop from peak"改为"80% drop"，分类结果会如何变化？

**Q4.** Cell D 的两个 seed 中，OOD 10.4% 的 seed 是否属于 11-seed 评估中的 stagnant 类别？如果是，Table 1 报告 mean 而不提这一点是否 misleading？

**Q5.** 论文声称"training duration does not explain the gap between stagnant and generalized seeds"（Section 4.5）。支撑这一 claim 的证据具体是什么？是否控制了训练步数、学习率等变量？

## Missing References

未发现明显缺失的关键引用。Related work 覆盖了 GRPO、step-independent training、credit assignment 的主要工作。可考虑引用以下补充方向：
- Temporal difference learning with eligibility traces（Section A.4 有提及 TD(λ) 但可在正文中更明确对比）
- Multi-agent credit assignment literature（Section A.4 简要提及但可强化，因为 sign misattribution 与 multi-agent reward shaping 有结构相似性）

## Detailed Comments

### Section 1 (Introduction)
- "causes the majority of gradient updates for locally correct actions to carry incorrect sign"：这里的"majority"隐含了 Proposition 2 的结论（80.9% incorrect），但 Proposition 2 仅在 binary reward 下成立，而实验用 penalty reward 时 incorrect rate 仅约 48%——"majority"措辞在实际实验条件下不成立。建议区分 binary vs. penalty reward 的情况。

### Section 2 (Method)
- Section 2.1: GRPO 公式（Eq. 1）的表述清晰准确。
- Section 2.3: 双机制分析的概念描述清楚，M1 和 M2 的区分有意义。
- Eq. 3: sign(A_k) = sign(R_episode - ρ) 的推导逻辑正确——在 step-independent 设置下，同一 episode 的所有窗口确实获得相同的 advantage 符号。

### Section 3 (Theoretical Analysis)
- Proposition 1 证明逻辑在其假设范围内正确。但假设"成功 episode 的所有窗口都应获得正梯度"是一个强假设（见 W1）。
- Proposition 2 是 Proposition 1 的直接推论，数值计算正确（已验证 p/(1-(1-p)^K) = 0.125/0.6564 ≈ 0.1904）。
- Figure 2 有效可视化了 correct sign probability 与 episode success rate 的关系，各 K 值曲线的趋势符合理论预测。

### Section 4 (Experiments)
- Table 1 数据与正文描述基本一致，但报告标准不统一（W5）。
- Figure 3a 的训练动态清晰展示了 Cell A 的两阶段崩溃和 Cell D 的稳定改善。
- Figure 3b 的 window-size sweep 仅有单 seed（W8），且图中仅显示约 6 个数据点，cliff 的精确位置难以确定。
- Figure 4 的 binary vs. penalty reward 对比是有效的补充实验，但 binary 下 100% correlation 与 Proposition 2 的 19.1% 预测之间的关系需要澄清（Q2）。
- Table 2（11-seed 评估）是论文的重要贡献，但分类标准的稳健性未验证（Q3）。

### Section 5 (Related Work)
- 覆盖较全面，包含了 GRPO collapse 相关的最新工作（RAGEN-2, RAGEN, GAGRPO, Turn-PPO 等）。
- Credit assignment 小节（Section A.4 in Appendix）与 TD(λ)/GAE 的对比有价值。

### Section 6 (Discussion)
- "Three structural properties co-occur: (a) step-level windowing, (b) sparse binary reward, and (c) group-relative normalization" 的分析框架有洞察力。
- M1-M2 vicious cycle 的论述有说服力但缺乏定量支撑。

### Limitations
- 涵盖了主要局限性（单 seed 跨规模、seed-dependent transfer、仅两个环境）。
- 格式合规：Limitations 作为单独 section 放在正文中，长度适中。

### 页数与格式
- 正文（Sections 1-7）在 8 页内，Limitations 不计入页数，参考文献无限制。格式合规。
- Double-blind：未发现明显的匿名性违反。

## Overall Assessment

- **Soundness**: 3/5 — 理论分析在 binary reward 假设内正确，但与实验条件（penalty reward）脱节；Cell C 缺失削弱因果推断；核心实证指标（52% credit agreement）统计力度弱。
- **Excitement**: 3.5/5 — 问题诊断有实际价值，dual mechanism 框架直观有用，但修正方案（episode-level GRPO）本质上是"不做 windowing"，技术新颖性有限。
- **Reproducibility**: 3/5 — 超参数完整报告（Table 3, Appendix B），但 36% seed 泛化率意味着复现"成功"结果需要大量 seed 筛选。

- **Score: 3/5 (Findings)**
- **Confidence: 4/5**
- 一句话总评：论文提出了一个有价值的诊断框架（sign misattribution in step-independent agent RL），理论分析在其有效范围内正确，但理论仅覆盖 binary reward 而实验用 penalty reward 的脱节、Cell C 缺失对 factorial design 的破坏、以及核心实证指标的统计弱度共同限制了 claims 的支撑力度，建议补强理论-实验桥接和统计证据后投稿。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 310 · 2026-05-23T16:18:26.419282+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "cost-verify-agent-rl",
  "text": "以下是 Reviewer 2 的完整审稿意见。请逐条回应：对每个 Weakness 和 Question，用 **[AGREE]** 表示同意并说明理由，或 **[REBUT]** 表示反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 完整审稿意见\n\n### Summary\n本文诊断了 step-independent windowing 训练多轮 LLM agent 时的两种失败机制：(1) 策略信息丢失（M1），(2) 优势符号错误归因（M2）。通过 2×2 factorial 实验在 ALFWorld 上隔离两种机制，表明 episode-level GRPO 可同时消除两种失败模式。\n\n### Strengths\nS1. 系统化的 factorial 实验设计\nS2. 可验证的理论预测\nS3. 诚实的局限报告\nS4. 全面的 Related Work 覆盖\nS5. 清晰的可视化\n\n### Weaknesses\n\n**W1. [critical] Episode-level GRPO 无方法论新颖性。** 论文承认 episode-level training \"is GRPO's original design; step-independent windowing is the deviation。\" \"fix\" 是撤销一个偏离，而非提出新方法。将回归原始算法包装为 Contribution 3 膨胀了贡献声明。\n\n**W2. [critical] 完全缺乏与同期方法的实验对比。** Related Work 讨论了 15+ 方法（如 HCAPO 在 ALFWorld 上 +13.8%），但实验部分仅对比 SFT baseline 和自己的 factorial conditions。一篇定位于\"诊断 + 指导\"的论文必须展示诊断如何指导实践。\n\n**W3. [major] Cell C 缺失破坏 factorial 完整性。** Cell C 的不稳定性暗示 M1 和 M2 之间存在交互效应，论文的加性框架未能捕捉。如果 M2 确实是\"更根本的机制\"，Cell C（保留 M2、移除 M1）应表现类似 Cell A，但实际出现了不同的失败模式（instability vs collapse）。\n\n**W4. [major] 主实验统计力严重不足。** Table 1 的 factorial 对比仅用 2 seeds。11-seed 评估显示 OOD 从 0% 到 38.7% 的巨大方差，2-seed 对比不构成统计证据。\n\n**W5. [major] 双机制诊断形式化了已知问题。** M1 本质是 partial observability，M2 是经典 credit assignment 问题。Proposition 1 的结论在直觉上并不令人惊讶。多个同期工作独立发现了同一问题。\n\n**W6. [minor] Conclusion 泛化声明超出实验证据。** \"applies to any agent RL method\" 远超实验范围。\n\n**W7. [minor] 多个引用存在准确性问题。** Turn-PPO arXiv ID 错误、MC-GRPO 标题错误、IRC 作者名拼写有误。\n\n**W8. [minor] 潜在匿名性泄露。** Page 5 脚注 1 的 GitHub 代码链接可能标识作者身份。\n\n### Questions\n\n**Q1.** Cell C 为什么出现训练不稳定性，而 Cell A 和 Cell B 没有？\n\n**Q2.** 36% 泛化的 seeds 与 64% 停滞的 seeds 有何区别？\n\n**Q3.** 是否存在 phase transition——在某个 p 值之上训练变得 self-correcting？\n\n**Q4.** HCAPO 在 ALFWorld 上用 Qwen2.5-7B 取得 +13.8% 改进。论文的诊断框架能否预测 HCAPO 的成功？\n\n**Q5.** Dense reward 显示 agent 最大化格式级奖励而不解决任务。这是否意味着 M2 在 dense reward 下转变为 reward hacking？\n\n### Missing References\n- Harutyunyan et al. (2019), \"Hindsight Credit Assignment\" (NeurIPS)\n- Arjona-Medina et al. (2019), \"RUDDER: Return Decomposition for Delayed Rewards\" (NeurIPS)\n- POMDP 文献\n\n---\n\n请对以上每个 W1-W8 和 Q1-Q5 逐条回应 [AGREE] 或 [REBUT]。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "cost-verify-agent-rl",
    "text": "以下是 Reviewer 2 的完整审稿意见。请逐条回应：对每个 Weakness 和 Question，用 **[AGREE]** 表示同意并说明理由，或 **[REBUT]** 表示反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 完整审稿意见\n\n### Summary\n本文诊断了 step-independent windowing 训练多轮 LLM agent 时的两种失败机制：(1) 策略信息丢失（M1），(2) 优势符号错误归因（M2）。通过 2×2 factorial 实验在 ALFWorld 上隔离两种机制，表明 episode-level GRPO 可同时消除两种失败模式。\n\n### Strengths\nS1. 系统化的 factorial 实验设计\nS2. 可验证的理论预测\nS3. 诚实的局限报告\nS4. 全面的 Related Work 覆盖\nS5. 清晰的可视化\n\n### Weaknesses\n\n**W1. [critical] Episode-level GRPO 无方法论新颖性。** 论文承认 episode-level training \"is GRPO's original design; step-independent windowing is the deviation。\" \"fix\" 是撤销一个偏离，而非提出新方法。将回归原始算法包装为 Contribution 3 膨胀了贡献声明。\n\n**W2. [critical] 完全缺乏与同期方法的实验对比。** Related Work 讨论了 15+ 方法（如 HCAPO 在 ALFWorld 上 +13.8%），但实验部分仅对比 SFT baseline 和自己的 factorial conditions。一篇定位于\"诊断 + 指导\"的论文必须展示诊断如何指导实践。\n\n**W3. [major] Cell C 缺失破坏 factorial 完整性。** Cell C 的不稳定性暗示 M1 和 M2 之间存在交互效应，论文的加性框架未能捕捉。如果 M2 确实是\"更根本的机制\"，Cell C（保留 M2、移除 M1）应表现类似 Cell A，但实际出现了不同的失败模式（instability vs collapse）。\n\n**W4. [major] 主实验统计力严重不足。** Table 1 的 factorial 对比仅用 2 seeds。11-seed 评估显示 OOD 从 0% 到 38.7% 的巨大方差，2-seed 对比不构成统计证据。\n\n**W5. [major] 双机制诊断形式化了已知问题。** M1 本质是 partial observability，M2 是经典 credit assignment 问题。Proposition 1 的结论在直觉上并不令人惊讶。多个同期工作独立发现了同一问题。\n\n**W6. [minor] Conclusion 泛化声明超出实验证据。** \"applies to any agent RL method\" 远超实验范围。\n\n**W7. [minor] 多个引用存在准确性问题。** Turn-PPO arXiv ID 错误、MC-GRPO 标题错误、IRC 作者名拼写有误。\n\n**W8. [minor] 潜在匿名性泄露。** Page 5 脚注 1 的 GitHub 代码链接可能标识作者身份。\n\n### Questions\n\n**Q1.** Cell C 为什么出现训练不稳定性，而 Cell A 和 Cell B 没有？\n\n**Q2.** 36% 泛化的 seeds 与 64% 停滞的 seeds 有何区别？\n\n**Q3.** 是否存在 phase transition——在某个 p 值之上训练变得 self-correcting？\n\n**Q4.** HCAPO 在 ALFWorld 上用 Qwen2.5-7B 取得 +13.8% 改进。论文的诊断框架能否预测 HCAPO 的成功？\n\n**Q5.** Dense reward 显示 agent 最大化格式级奖励而不解决任务。这是否意味着 M2 在 dense reward 下转变为 reward hacking？\n\n### Missing References\n- Harutyunyan et al. (2019), \"Hindsight Credit Assignment\" (NeurIPS)\n- Arjona-Medina et al. (2019), \"RUDDER: Return Decomposition for Delayed Rewards\" (NeurIPS)\n- POMDP 文献\n\n---\n\n请对以上每个 W1-W8 和 Q1-Q5 逐条回应 [AGREE] 或 [REBUT]。"
  }
}
```

</details>

---


### Tool result

_source line 311 · 2026-05-23T16:18:56.188269+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_648eaf83d2b24d445764257cf6a55525:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 29768
}
```

</details>

---


### Tool call

_source line 312 · 2026-05-23T16:18:56.339958+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "cost-verify-agent-rl",
  "text": "以下是 Reviewer 1 的完整审稿意见。请逐条回应：对每个 Weakness 和 Question，用 **[AGREE]** 表示同意并说明理由，或 **[REBUT]** 表示反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 完整审稿意见\n\n### Summary\n本文诊断了多轮 LLM agent RL 中 step-independent windowing 的一种结构性信用分配病理——\"sign misattribution\"。双机制框架：M1（信息丢失）和 M2（符号错误归因）。理论分析推导出 binary reward 下仅 19.1% 梯度更新方向正确。实验采用 2×2 factorial design（缺失 Cell C），在 ALFWorld 1.7B/8B 和 ScienceWorld 上验证。\n\n### Strengths\nS1. 问题定位有价值且动机清晰\nS2. 理论分析在其有效范围内正确\nS3. 实验报告的诚实度高于平均水平\nS4. 11-seed 评估有价值\nS5. Factorial 实验设计思路正确\n\n### Weaknesses\n\n**W1. [critical] Proposition 1/2 隐含假设\"episode 成功 ⟹ 所有窗口局部正确\"，与 Definition 1 矛盾。** Proposition 1 将成功 episode 中所有窗口视为获得\"correct sign\"，但 Definition 1 定义 locally correct action 需要\"在 oracle 下获得正 advantage\"。成功 episode 可包含次优窗口。因此 19.1% 是上界而非精确值，但论文将其作为精确预测使用。\n\n**W2. [critical] Cell C 缺失实质性破坏了 2×2 factorial 的因果推断力。** Cell C 本应隔离 M2（无 M1 干扰），是验证\"M2 独立有害\"的关键对照。缺失意味着无法确认 M2 在无 M1 条件下是否独立导致退化，无法排除交互效应。\n\n**W3. [critical] 理论分析仅覆盖 binary reward，但全部主实验使用 penalty reward，理论-实验脱节。** Proposition 1/2 预测 19.1%，实验测得 52%。论文仅以\"reflects the reward structure difference\"一笔带过，未提供 penalty reward 下的理论分析。核心量化预测在主实验设置下从未被直接验证。\n\n**W4. [major] 52% credit agreement rate 统计显著性很弱。** n≈3000 下 52% vs 50% 的 z≈2.19, p≈0.028，仅 marginal significance。但论文仍称\"confirms sign misattribution as the causal driver\"，措辞过强。\n\n**W5. [major] Table 1 报告标准不一致。** Cell A 报告 best seed，Cell B 报告 best checkpoint，Cell D 报告 mean。Cell D 的 OOD range 10.4-23.9% 中一个 seed 低于 SFT baseline。\n\n**W6. [major] 8B 单 seed 结果 hedge 不足。** 1.7B 的 11-seed 评估已表明仅 36% seeds 泛化，8B 单 seed 几乎不能支撑 claim。abstract 中\"effects persisting at 8B scale\"无 hedge。\n\n**W7. [major] REINFORCE++ 对比不公平（仅 15 步）。** 论文自己承认可能 insufficient，但仍将此作为 episode-level training 优越性的佐证。\n\n**W8. [minor] Window-size sweep cliff claim 基于单 seed。**\n\n**W9. [minor] Eq.6 comparable magnitude 假设论证单薄。** 1.32 是单点测量，条件未详细说明。\n\n**W10. [minor] Definition 1 操作化与理论定义有 gap。** 操作化仅检查 valid actions + episode success，是 locally correct 的宽松近似。\n\n### Questions\n\n**Q1.** Cell C 的训练不稳定是否暗示 M1 和 M2 之间存在非独立交互效应？\n\n**Q2.** Binary reward 下 100% sign-episode correlation 和 19.1% correct sign rate 如何同时成立？\n\n**Q3.** Collapsed/Stagnant/Generalized 三类的分类阈值是否敏感？\n\n**Q4.** Cell D 的两个 seed 中 OOD 10.4% 的 seed 是否属于 stagnant？\n\n**Q5.** \"training duration does not explain the gap\" 的具体证据是什么？\n\n### Missing References\n- TD(λ) 可在正文更明确对比\n- Multi-agent credit assignment 文献可强化\n\n---\n\n请对以上每个 W1-W10 和 Q1-Q5 逐条回应 [AGREE] 或 [REBUT]。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "cost-verify-agent-rl",
    "text": "以下是 Reviewer 1 的完整审稿意见。请逐条回应：对每个 Weakness 和 Question，用 **[AGREE]** 表示同意并说明理由，或 **[REBUT]** 表示反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 完整审稿意见\n\n### Summary\n本文诊断了多轮 LLM agent RL 中 step-independent windowing 的一种结构性信用分配病理——\"sign misattribution\"。双机制框架：M1（信息丢失）和 M2（符号错误归因）。理论分析推导出 binary reward 下仅 19.1% 梯度更新方向正确。实验采用 2×2 factorial design（缺失 Cell C），在 ALFWorld 1.7B/8B 和 ScienceWorld 上验证。\n\n### Strengths\nS1. 问题定位有价值且动机清晰\nS2. 理论分析在其有效范围内正确\nS3. 实验报告的诚实度高于平均水平\nS4. 11-seed 评估有价值\nS5. Factorial 实验设计思路正确\n\n### Weaknesses\n\n**W1. [critical] Proposition 1/2 隐含假设\"episode 成功 ⟹ 所有窗口局部正确\"，与 Definition 1 矛盾。** Proposition 1 将成功 episode 中所有窗口视为获得\"correct sign\"，但 Definition 1 定义 locally correct action 需要\"在 oracle 下获得正 advantage\"。成功 episode 可包含次优窗口。因此 19.1% 是上界而非精确值，但论文将其作为精确预测使用。\n\n**W2. [critical] Cell C 缺失实质性破坏了 2×2 factorial 的因果推断力。** Cell C 本应隔离 M2（无 M1 干扰），是验证\"M2 独立有害\"的关键对照。缺失意味着无法确认 M2 在无 M1 条件下是否独立导致退化，无法排除交互效应。\n\n**W3. [critical] 理论分析仅覆盖 binary reward，但全部主实验使用 penalty reward，理论-实验脱节。** Proposition 1/2 预测 19.1%，实验测得 52%。论文仅以\"reflects the reward structure difference\"一笔带过，未提供 penalty reward 下的理论分析。核心量化预测在主实验设置下从未被直接验证。\n\n**W4. [major] 52% credit agreement rate 统计显著性很弱。** n≈3000 下 52% vs 50% 的 z≈2.19, p≈0.028，仅 marginal significance。但论文仍称\"confirms sign misattribution as the causal driver\"，措辞过强。\n\n**W5. [major] Table 1 报告标准不一致。** Cell A 报告 best seed，Cell B 报告 best checkpoint，Cell D 报告 mean。Cell D 的 OOD range 10.4-23.9% 中一个 seed 低于 SFT baseline。\n\n**W6. [major] 8B 单 seed 结果 hedge 不足。** 1.7B 的 11-seed 评估已表明仅 36% seeds 泛化，8B 单 seed 几乎不能支撑 claim。abstract 中\"effects persisting at 8B scale\"无 hedge。\n\n**W7. [major] REINFORCE++ 对比不公平（仅 15 步）。** 论文自己承认可能 insufficient，但仍将此作为 episode-level training 优越性的佐证。\n\n**W8. [minor] Window-size sweep cliff claim 基于单 seed。**\n\n**W9. [minor] Eq.6 comparable magnitude 假设论证单薄。** 1.32 是单点测量，条件未详细说明。\n\n**W10. [minor] Definition 1 操作化与理论定义有 gap。** 操作化仅检查 valid actions + episode success，是 locally correct 的宽松近似。\n\n### Questions\n\n**Q1.** Cell C 的训练不稳定是否暗示 M1 和 M2 之间存在非独立交互效应？\n\n**Q2.** Binary reward 下 100% sign-episode correlation 和 19.1% correct sign rate 如何同时成立？\n\n**Q3.** Collapsed/Stagnant/Generalized 三类的分类阈值是否敏感？\n\n**Q4.** Cell D 的两个 seed 中 OOD 10.4% 的 seed 是否属于 stagnant？\n\n**Q5.** \"training duration does not explain the gap\" 的具体证据是什么？\n\n### Missing References\n- TD(λ) 可在正文更明确对比\n- Multi-agent credit assignment 文献可强化\n\n---\n\n请对以上每个 W1-W10 和 Q1-Q5 逐条回应 [AGREE] 或 [REBUT]。"
  }
}
```

</details>

---


### Tool result

_source line 313 · 2026-05-23T16:18:57.910872+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_648eaf83d2b24d445764257cf6a55525:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1570
}
```

</details>

---


### Assistant

_source line 314 · 2026-05-23T16:19:00.259897+00:00_

交叉分享已派发，等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director"
}
```

</details>

---


## Round 26

## Round 26

2 recorded events


### User

_source line 315 · 2026-05-23T16:19:02.882451+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

核心发现：
- **3 个 critical 问题**：(1) Proposition 1/2 隐含"成功 episode ⟹ 全窗口局部正确"的强假设与 Definition 1 矛盾；(2) Cell C 缺失破坏 2×2 factorial 因果推断；(3) 理论仅覆盖 binary reward 但实验用 penalty reward，核心量化预测 19.1% 从未在实验条件下直接验证
- **4 个 major 问题**：52% credit agreement 统计力度弱、Table 1 报告标准不一致、8B 单 seed hedge 不足、REINFORCE++ 对比不公平
- **3 个 minor 问题**：window-size cliff 单 seed、"comparable magnitude" 单点测量、Definition 1 操作化 gap
- **Overall: 3/5 (Findings)**，Confidence 4/5

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 316 · 2026-05-23T16:19:07.232958+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director"
}
```

</details>

---


## Round 27

## Round 27

2 recorded events


### User

_source line 317 · 2026-05-23T16:20:57.110445+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应

---

### Weaknesses

**[AGREE] R2-W1: Episode-level GRPO 无方法论新颖性**
同意这是一个实质性问题。论文 Section 2.4 明确承认 "This is GRPO's original design; step-independent windowing is the deviation"，即 "fix" 仅是回归原始算法。Contribution 3 表述为 "Episode-level fix: necessary but not sufficient"（page 2），虽有 hedge，但将"撤销一个偏离"列为独立贡献确实有膨胀之嫌。不过我认为论文的核心价值在于诊断（Contributions 1-2）而非修正方案，R2 的批评更多指向 framing 而非 substance。建议作者将 Contribution 3 合并到 Contribution 2 中，作为 factorial 实验的结论之一，而非独立贡献。

**[AGREE] R2-W2: 完全缺乏与同期方法的实验对比**
同意。论文 Section 5 讨论了 HCAPO（+13.8% on ALFWorld）、Turn-PPO、GAGRPO、DigiRL 等 15+ 方法，但实验部分（Section 4）仅有内部 factorial 对比和 SFT baseline。对于一篇自称 "our contribution is diagnostic"（page 1）的论文，虽然不必追求 SOTA，但至少应展示诊断框架的预测力——例如，用 M1/M2 框架解释 HCAPO 或 Turn-PPO 为何有效（它们分别解决了哪个机制？）。纯诊断而无实践验证会削弱论文的 impact。

**[AGREE] R2-W3: Cell C 缺失破坏 factorial 完整性**
强烈同意。这与我的 R1-W2 一致。R2 进一步指出了一个我未明确提出的观察：Cell C 出现**不同于 Cell A 的失败模式**（NaN instability vs. gradual collapse），这可能暗示 M1 和 M2 之间存在**交互效应**而非加性关系。如果移除 M1（full context）但保留 M2（step-level advantage），训练不是像 Cell A 那样"慢慢崩溃"，而是直接 NaN 爆炸，这说明 M1 的 context truncation 可能实际上起到了某种"稳定器"作用（限制了梯度方差），而论文的加性框架无法捕捉这一点。Appendix D 仅报告了 Cell C 失败的现象（KL 散度爆炸、NaN loss），未分析其机制。这是论文因果推断链中最薄弱的环节。

**[AGREE] R2-W4: 主实验统计力严重不足**
同意，与我的 R1-W5 一致。Table 1 的 factorial 核心对比仅有 2 seeds per cell，而 Table 2 的 11-seed 评估显示 OOD 范围从 0% 到 38.71%。在如此高的方差下，2-seed 对比本质上是 anecdotal evidence。补充一点：Cell D 的 2 seeds 中一个 OOD 为 10.4%（低于 SFT baseline 12.56%），另一个为 23.9%——这意味着 Cell D 的 2-seed "mean" 可能恰好落在有利区间，再多一个不幸的 seed 就可能推翻结论。

**[REBUT] R2-W5: 双机制诊断形式化了已知问题**
部分反驳。R2 认为 M1 是 partial observability、M2 是经典 credit assignment，因此诊断缺乏新颖性。但我认为有以下区分：

1. **M2 的具体机制并非显而易见。** 经典 credit assignment 问题关注"哪个动作对结果贡献最大"，而本文的 sign misattribution 具体指出了 GRPO 的 group-relative normalization 如何在 step-independent 设置下系统性地**反转**梯度方向（Eq. 3, Section 2.3.2）。这不是泛泛的 credit assignment 困难，而是特定算法结构的特定缺陷。

2. **Proposition 2 的量化预测有增量价值。** 尽管"binary reward 下大多数梯度方向错误"可能直觉上不令人惊讶，但精确的 19.1%（在 p=12.5%, K=8 下）提供了可验证的定量 benchmark。Section A.2 的 binomial test 确认实验值（52% under penalty reward）显著偏离理论值，这为理解 reward structure 的影响提供了新数据。

3. **但 R2 关于"多个同期工作独立发现同一问题"的观察是合理的。** RAGEN-2（Wang et al., 2026b）、GRPO-Collapse（Deng et al., 2025）、EDGE-GRPO（Zhang et al., 2025）均独立识别了类似问题，削弱了诊断的 priority claim。论文 Section 5 已引用这些工作，但未充分讨论自身分析相对于这些同期发现的 incremental contribution。

综合判断：诊断的**形式**有增量新颖性（定量预测 + factorial 分离），但 novelty claim 应适度下调。

**[AGREE] R2-W6: Conclusion 泛化声明超出实验证据**
同意。Section 7（page 8）写 "this finding applies to any agent RL method combining step-level windowing, sparse binary reward, and group-relative normalization"。虽然列出了三个条件作为限定，但实验仅覆盖 ALFWorld（1.7B/8B）和 ScienceWorld（单 seed），两者都是 text-based household 环境。对于 web navigation、code generation、tool use 等不同结构的 agent 任务，三个条件是否同时成立未被验证。建议改为 "our experiments on ALFWorld and ScienceWorld suggest that..."。

**[AGREE] R2-W7: 引用准确性问题**
同意应检查。引用准确性是基本的学术规范。我在审稿过程中未逐一核实 arXiv ID，但如果 R2 已发现 Turn-PPO arXiv ID 错误、MC-GRPO 标题错误、IRC 作者名拼写有误等具体问题，这些必须在修订中更正。建议作者对全部参考文献做系统性核查。

**[AGREE] R2-W8: 潜在匿名性泄露**
同意这是需要关注的合规问题。Page 5 脚注 1 提及代码实现链接（从图像中我看到类似 "RAGEN-47/RAGEN" 的文字），如果该 GitHub 组织/仓库可追溯到作者，则违反 double-blind 规则。ARR 要求论文匿名化，代码链接应通过 anonymous GitHub 或在 camera-ready 阶段再添加。但我注意到论文使用的是 "[review]" 模式的 ACL template，部分模板允许匿名化链接——需确认具体链接是否可识别身份。

---

### Questions

**[AGREE] R2-Q1: Cell C 为什么不稳定而 Cell A/B 没有？**
这与我的 R1-Q1 一致。论文未提供机制层面的解释。我的假设：Cell C 使用 full trajectory（无 context truncation）+ step-level advantage normalization。Full trajectory 意味着每个 step 的梯度基于完整上下文计算，梯度方差可能远大于 windowed 设置（因为 step-level advantage 的 normalization 分母在长序列上变小）。但这是猜测——论文应提供梯度方差或 KL 散度的定量分析来解释 Cell C 的失败模式。

**[AGREE] R2-Q2: 泛化 vs. 停滞 seeds 的区别是什么？**
这与我的 R1-Q5 一致。论文 Section 4.5 声称 "training duration does not explain the gap"，但未给出任何正面解释。Table 2 的数据中，seed 编号与结果之间的关系不明——是否与初始化权重有关？是否与特定 rollout 采样有关？这是论文最大的 open question 之一，缺乏分析削弱了方法的实用性（如果无法预测哪些 seed 会泛化，episode-level GRPO 的实际部署成本会很高）。

**[REBUT] R2-Q3: 是否存在 phase transition？**
部分反驳——论文的理论框架实际上可以回答这个问题。从 Proposition 2 的公式 P(correct|update) = p/(1-(1-p)^K)，令 P > 0.5 可解出临界 p 值。对于 K=8：p/(1-(1-p)^8) > 0.5，数值求解得 p ≈ 0.39。即当 episode success rate 超过约 39% 时，majority 的梯度更新方向正确，训练可能变为 self-correcting。

但这只是 binary reward 下的理论预测。论文的实验数据（Figure 3a）显示 Cell D 在 step 3-5 时 success rate 从 ~5% 上升到 ~35%（SFT baseline 12.5%），尚未跨过这个理论临界点，但 OOD 性能已开始改善。这暗示 penalty reward 下的临界值可能更低。论文应补充这一分析——它会使理论更具指导意义。

**[AGREE] R2-Q4: 诊断框架能否预测 HCAPO 的成功？**
同意这是一个关键问题。如果论文的诊断框架有预测力，它应该能解释为什么 HCAPO（hierarchical credit assignment + PPO）能在 ALFWorld 上取得 +13.8% 改进。按照 M1/M2 框架：HCAPO 通过 hierarchical structure 可能部分解决 M2（更精细的 credit assignment 减少符号错误），但是否同时解决 M1 取决于其 context window 设计。论文应至少讨论 1-2 个同期方法在 M1/M2 框架下的预期行为，即使没有实验对比。这会将诊断从"事后解释"提升为"预测性工具"。

**[AGREE] R2-Q5: Dense reward 下 M2 是否转变为 reward hacking？**
同意这是一个有洞察力的观察。Figure 6b（Appendix, page 15）显示 dense reward 下 action validity 从 60% 上升到 97.5% 但 task success 保持 0%，agent 最大化了格式级奖励而未解决任务。这在技术上不是 M2（sign misattribution 特指 advantage 符号在窗口间的错误传播），而是一种 reward shaping pathology——dense reward 创造了一个与 task completion 不对齐的局部最优。但 R2 的更深层观点是合理的：M2 和 reward hacking 可能共享一个根因，即 credit signal 与 task objective 的 misalignment。论文将 dense reward 作为 "standard remedy that fails"（Figure 6a）讨论（Appendix D），但未将其纳入 M1/M2 框架做统一分析。

---

### Missing References

**[AGREE]** Harutyunyan et al. (2019) "Hindsight Credit Assignment" 和 Arjona-Medina et al. (2019) "RUDDER" 是 temporal credit assignment 的重要工作，与本文的 sign misattribution 问题直接相关。论文 Appendix A.4 已讨论 TD(λ) 和 GAE，但遗漏了这两篇更直接对标的方法。POMDP 文献的引用在 M1（信息丢失导致 partial observability）的讨论中也应加入，以锚定到更广泛的理论背景。

---

### 综合评价

R2 的审稿意见整体有效。最有力的批评是 W2（缺乏同期方法对比）和 W3（Cell C 缺失的更深层含义），这两点与我的审查发现互补。W1 和 W5 关于新颖性的批评在程度上我有部分保留（诊断本身有增量价值），但 R2 指出的 framing 问题（overclaiming）是合理的。W4（统计力不足）与我的 R1-W5 完全一致。Q3（phase transition）是一个论文理论框架可以回答但遗漏了的好问题，建议作者补充。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 318 · 2026-05-23T16:21:01.488107+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director"
}
```

</details>

---


## Round 28

## Round 28

2 recorded events


### User

_source line 319 · 2026-05-23T16:21:08.048450+00:00_

[Reviewer 1 审稿结果]:
已提交对 Reviewer 2 全部 W1-W8 和 Q1-Q5 的逐条回应。总结：

- **7 项 AGREE**（W1/W2/W3/W4/W6/W7/W8），其中 W3（Cell C 缺失暗示 M1-M2 交互效应）和 W2（缺乏同期方法对比）是最有力的批评
- **1 项 REBUT**（W5），认为虽然 M1/M2 的个体概念已知，但 GRPO 特定的量化诊断有增量价值
- Questions 中对 Q3（phase transition）做了 partial REBUT，指出论文的理论框架可以回答这个问题但遗漏了

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 320 · 2026-05-23T16:21:14.732932+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director"
}
```

</details>

---


## Round 29

## Round 29

10 recorded events


### User

_source line 321 · 2026-05-23T16:24:48.772071+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 对 Reviewer 1 审稿意见的逐条交叉回应

---

### Weaknesses 回应

**[AGREE] R1-W1: Proposition 1/2 假设 "episode 成功 ⟹ 所有窗口局部正确" 与 Definition 1 存在 gap。**
同意这是一个理论严谨性问题。Proposition 1 的推导（Appendix A.1, Cases 1-3）将成功 episode 中所有窗口的正优势视为 "correct sign"，但 Definition 1 要求窗口在 oracle 下独立获得正 advantage，两者并非等价。成功 episode 完全可以包含次优窗口（例如冗余探索步骤仍被标记为 "correct"）。不过需补充一点：这个 gap 的方向是使 19.1% 成为**上界**——如果部分"成功"窗口实际是次优的，真实正确率更低，论文的 sign misattribution 结论反而被**强化**而非削弱。问题在于论文将 19.1% 作为精确预测使用（Section 3, "only 19.1% of gradient updates are correct"），而非上界，措辞不准确。

**[AGREE] R1-W2: Cell C 缺失破坏 factorial 因果推断。**
完全同意。这与我的 W3 一致。Cell C（full trajectory + step-level advantage）应隔离 M2 的独立效应。它的训练不稳定性（Appendix D）不仅是缺失数据，更暗示 M1 和 M2 之间存在**非加性交互效应**——论文的隐含框架是两种机制独立且可加性分离，但 Cell C 的行为与此矛盾。如果 M1（信息丢失/partial observability）实际上有某种"稳定化"作用（限制策略的探索空间从而避免 M2 引起的极端不稳定），那么双机制的"独立诊断"框架就需要修正。

**[AGREE] R1-W3: 理论-实验脱节（binary vs penalty reward）。**
同意这是一个重要的清晰性问题。论文的核心量化预测是 19.1%（Proposition 2, binary reward, p=12.5%, K=8），而 Section 4.4 报告的实证 credit agreement rate 是 52%。两者之间的巨大差距（19.1% vs 52%）论文仅以 "reflects the reward structure difference" 一句带过（Section 4.4 末段），未提供 penalty reward 下的理论推导。

更深层的问题是：Section 4.1 称 "Reward is binary: R ∈ {0, r_s}"，暗示主实验使用 binary reward。但如果主实验确实使用 binary reward，那么成功 episode 中所有窗口的 advantage sign 应一致为正（因为所有窗口共享相同的正回报），credit agreement 应接近 100% 而非 52%。52% 的结果强烈暗示实际训练使用了包含步骤级惩罚的 reward 结构，与 Section 4.1 的 "binary" 声明矛盾。论文对 reward 设计的描述存在不一致，这直接影响理论分析的适用性判断。

不过也需指出：即便理论-实验存在间接关系，52% ≈ 50%（随机水平）这一定性结论本身支持 sign misattribution 的存在。理论的定量精度有问题，但定性方向正确。

**[AGREE] R1-W4: 52% credit agreement 的统计措辞过强。**
同意措辞问题。52% vs 50% 在 n≈3000 下的 z≈2.19, p≈0.028 仅为 marginal significance，但论文称 "confirms sign misattribution as the causal driver"。不过我想补充一个重要的解读角度：论文的核心论证并非"52% 显著高于 50%"，而是"credit agreement 如此接近随机水平（50%），说明 advantage sign 几乎不携带 local action quality 信息"。从这个角度看，52% ≈ 50% 本身就是证据——不需要证明偏离的显著性，而是需要证明 agreement 远低于有效 credit assignment 应有的水平。但论文的措辞确实混淆了这两种论证方式，应明确区分。

**[AGREE] R1-W5: Table 1 报告标准不一致。**
同意。Table 1 的脚注（page 5）明确标注了不同条件使用不同聚合方式：Cell A = best seed, Cell B = best checkpoint (step 5), Cell D = mean of two seeds。这种不一致使条件间对比不公平：
- Cell A 的 best seed 在两个 seed 都 collapse 到 0% 时不影响结果（max(0,0)=0）
- Cell B 的 best checkpoint 选择性地报告训练中的最佳时间点，可能高估其稳定性能
- Cell D 的 mean 是最保守的报告方式

这种不一致性虽然不改变核心结论（Cell D > Cell B > Cell A 的排序在任何合理聚合下可能都成立），但降低了实验方法论的严谨度。所有条件应使用统一的聚合标准。

**[REBUT] R1-W6: 8B 单 seed 的 hedge 问题。**
Reviewer 1 称 "abstract 中 'effects persisting at 8B scale' 无 hedge"，但 Abstract 的实际措辞是 "**Preliminary** cross-scale verification at 8B parameters... provide **preliminary** evidence that the pathology extends beyond our primary setting"（page 1）。Abstract 使用了两次 "preliminary" 来修饰 8B 和 ScienceWorld 结果，这是明确的 hedging。

不过 Reviewer 1 的关切方向是合理的：Introduction 中 Contribution 3 写道 "achieving substantial OOD improvement at both 1.7B and 8B scales"（page 2），此处的 "substantial" 未附带 "preliminary" 修饰词，在单 seed 8B 结果的支撑下确实过强。因此，**abstract 的 hedging 是充分的，但 Introduction contribution claim 的 hedging 不足**。

**[AGREE] R1-W7: REINFORCE++ 对比不公平。**
同意。15 个训练步数对 REINFORCE++ 可能严重不足。论文在 Appendix D（page 13）自己承认 "15 training steps may be insufficient for REINFORCE++ to converge"，但仍然用此结果作为 episode-level training 优越性的间接证据。论文的辩护是 "Cell A collapse pattern represents active degradation rather than undertraining"——但这个辩护适用于 Cell A（GRPO），不适用于 REINFORCE++。REINFORCE++ 作为不同算法，其收敛速度可能截然不同。在给定资源下，至少应运行到 REINFORCE++ 性能稳定或明确下降。

**[AGREE] R1-W8: Window-size sweep cliff 基于单 seed。**
同意。Figure 3b 的窗口大小阈值效应（h=10-20）如果仅基于单 seed，则 cliff 的位置和存在性都无法确认。与我审稿意见中关于统计力不足的总体关切一致。

**[AGREE] R1-W9: Eq.6 comparable magnitude 假设单薄。**
同意。用单点测量（1.32）论证 "comparable magnitude" 的假设不充分。理想情况下应在多个训练阶段、多个 seed 上测量梯度幅度比率，并报告分布而非单点。

**[AGREE] R1-W10: Definition 1 操作化与理论定义有 gap。**
同意。操作化定义（valid actions + episode success → "locally correct"）是理论定义（oracle 下独立获得正 advantage）的宽松近似。论文在 Section 4.4 中承认这一点（"This operationalization is a conservative approximation"），但未量化这种近似的误差幅度。与 W1 形成联动：理论定义的严格性和操作化的宽松性之间的 gap 贯穿了从理论到实验的整个验证链。

---

### Questions 回应

**[AGREE] R1-Q1: Cell C 不稳定暗示 M1-M2 交互效应。**
同意，这与我的 Q1 一致。如果两种机制是独立的，Cell C（保留 M2、移除 M1）的行为应该可预测——应表现为"有 sign errors 但无 information loss"的某种中间状态。出现完全不同的失败模式（instability vs collapse）强烈暗示 M1 对 M2 有调节作用（moderation effect），论文的加性框架需要修正或至少讨论这一可能性。

**[REBUT] R1-Q2: Binary reward 下 100% sign-episode correlation 和 19.1% correct sign 可同时成立。**
这两个指标测量的是不同的东西，逻辑上不矛盾：
- **100% sign-episode correlation**（Figure 4 left）：advantage sign 完美跟踪 episode 结果——成功 episode 的窗口获得正 advantage，失败 episode 的窗口获得负 advantage。这是 sign-**episode** 的关系。
- **19.1% correct sign**（Proposition 2）：在所有非零梯度更新中，只有 19.1% 来自成功 episode 因而对 locally correct 窗口具有正确方向。

两者可同时成立因为 p=12.5%：~87.5% 的 episode 失败，这些失败 episode 中的 locally correct 窗口（存在有效动作但 episode 整体失败的窗口）全部获得负 advantage——sign 完美跟踪了 episode 结果（100% correlation），但方向对于 local action quality 来说是**错误的**（contributes to the low 19.1%）。这正是 M2 的核心：sign 反映 episode outcome 而非 local quality。

不过需注意：如 W3 所述，19.1% 是 binary reward 下的理论值，实测 52% 在不同 reward 下获得，两者的对应关系论文未充分说明。

**[AGREE] R1-Q3: Collapsed/Stagnant/Generalized 分类阈值敏感性。**
同意。论文在 Section 4.5（page 6）定义 collapsed seeds 为 "those where in-distribution success drops >90% from peak and remains below baseline for ≥ 2 consecutive steps"，non-collapsed 和 generalized 的定义较模糊。分类阈值的敏感性分析（例如：将 90% 改为 80% 或 95% 时结论是否变化）未提供。

**[AGREE] R1-Q4: Cell D OOD 10.4% seed 是否属于 stagnant。**
同意这需要澄清。Table 2（page 7）的 OOD range 为 10.4-23.9%。10.4% 虽高于 SFT baseline（如果 SFT OOD 为 ~5-7%），但在 11-seed 评估中属于低端。根据论文的分类标准，其归类取决于统计检验（Fisher exact test, p<0.01），但 Table 1 和 Table 2 之间的分类标准描述不够清晰。

**[AGREE] R1-Q5: "training duration doesn't explain the gap" 证据薄弱。**
同意。论文仅引用 seed100 的单一观察（"minimal improvement from step 5 to step 15"）作为证据，这是 n=1 的轶事证据。系统性的分析应包括：(a) 所有 stagnant seeds 的训练曲线比较，(b) 延长训练至更多步数（如 30-50 步）的探索性实验。

---

### 与 Reviewer 2 自身意见的关系总结

**R1 与 R2 的高度一致点：**
- Cell C 缺失破坏 factorial 完整性（R1-W2 = R2-W3）
- 统计力不足（R1-W5 报告不一致 ≈ R2-W4 2-seed 问题）
- M1-M2 交互效应（R1-Q1 = R2-Q1）

**R1 提出但 R2 未独立识别的重要问题：**
- W1 (Proposition 假设与 Definition 1 矛盾) — 理论层面的精确性问题，有价值
- W3 (binary vs penalty reward 脱节) — 值得注意的理论-实验一致性问题
- W7 (REINFORCE++ 对比不公平) — 实验方法论问题

**R2 提出但 R1 未涵盖的重要问题：**
- **缺乏与同期方法的实验对比**（R2-W2）— 15+ 方法在 Related Work 中讨论但无一被实验比较，这是论文最严重的缺陷之一
- **Episode-level GRPO 无方法论新颖性**（R2-W1）— fix 是回归原始算法，非新贡献
- **引用准确性问题**（R2-W7）— Turn-PPO arXiv ID 错误、MC-GRPO 标题错误等

**整体评分对齐：** R1 和 R2 的评估方向一致——论文有用但新颖性和实验力度不足以支撑主会议接收。R2 给出 Overall 3.0/5 (Findings)，与 R1 的评估基调吻合。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 322 · 2026-05-23T16:25:23.442902+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "cost-verify-agent-rl"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "cost-verify-agent-rl"
  }
}
```

</details>

---


### Tool result

_source line 323 · 2026-05-23T16:25:23.644098+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-23T15:55:50.958991+00:00\", \"completed_at\": \"2026-05-23T15:59:01.591713+00:00\", \"findings\": [{\"severity\": \"warning\", \"dimension\": \"page 10\", \"message\": \"参考文献末页仅顶部 2 条条目（约占页面 5%），其余 ~95% 为空白。系 appendix 前 \\\\clearpage 所致，但空白面积过大，视觉上不专业。建议取消强制分页或调整 references 排版填充页面\"}, {\"severity\": \"warning\", \"dimension\": \"page 1-2\", \"message\": \"连续 2 页无任何 display item（figure/table）。第 2 页有公式部分缓解单调感，但审稿人翻过整个第 1-2 页都没有视觉锚点。Figure 1 直到第 3 页才出现——仍在 3 页窗口内，但处于边界\"}, {\"severity\": \"info\", \"dimension\": \"page 3\", \"message\": \"Figure 1 使用红-绿对比标注 M1/M2 机制（绿色=正确/保留，红色=错误/截断）。红绿色盲用户难以区分。图中有文字标签和 +/- 符号辅助，但建议换用蓝-橙或 Okabe-Ito 色板提升无障碍性\"}, {\"severity\": \"info\", \"dimension\": \"page 6\", \"message\": \"Figure 3 图例文字偏小（\\\"Cell A: window, M1+M2 (n)\\\" 等），在 150dpi 渲染下勉强可读。打印时可能更吃力，建议适当放大图例字号\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Table 2 信息密度较高（11 seeds × 多列 + 多个脚注标记 †‡§ 等），可读但略显拥挤。对审稿人快速扫描不够友好，可考虑将 Stagnant/Generalized 分组更明显地视觉区分\"}, {\"severity\": \"info\", \"dimension\": \"page 15\", \"message\": \"附录末页（Figure 6 + Figure 7）内容约占页面 55%，底部有较大空白。附录末页不影响正文审稿印象，优先级低\"}], \"counts\": {\"critical\": 0, \"warning\": 2, \"info\": 4}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 324 · 2026-05-23T16:25:23.644541+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "cost-verify-agent-rl"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "cost-verify-agent-rl"
  }
}
```

</details>

---


### Tool result

_source line 325 · 2026-05-23T16:25:23.745218+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_648eaf83d2b24d445764257cf6a55525:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 100
}
```

</details>

---
