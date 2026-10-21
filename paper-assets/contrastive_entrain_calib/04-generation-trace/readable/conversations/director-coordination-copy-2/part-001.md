# Director coordination — Part 1 of 3

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Conversation logs

[Transcript overview](../director-coordination-copy-2.md) · [Part 2 →](part-002.md) · [Structured JSON](../../../sessions/f9/f9016339e7bc29bb9263.json)

## Round 1

## Round 1

76 recorded events


### User

_source line 1 · 2026-05-22T09:53:48.903780+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: contrastive_entrain_calib
- 论文路径: /home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: ARR May 2026
- 截止日期: 2026-05-25
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 2 · 2026-05-22T09:53:55.075944+00:00_

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
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 3 · 2026-05-22T09:53:55.127142+00:00_

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
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 4 · 2026-05-22T09:54:01.010750+00:00_

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
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
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

_source line 5 · 2026-05-22T09:54:01.061571+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 6 · 2026-05-22T09:54:04.981112+00:00_

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
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
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

_source line 7 · 2026-05-22T09:54:04.981550+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 8 · 2026-05-22T09:54:10.689882+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 9 · 2026-05-22T09:54:10.690401+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 10 · 2026-05-22T09:54:15.058027+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "contrastive_entrain_calib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "contrastive_entrain_calib"
  }
}
```

</details>

---


### Tool result

_source line 11 · 2026-05-22T09:54:16.415341+00:00_

{"result":"# 项目 contrastive_entrain_calib 概况\n\n## 实验状态 (75 个)\n\n- **exp-003-eval-ckpt1000**: DONE (negative) — \n- **exp-003-eval-ckpt5000**: DONE (negative) — \n- **exp-009**: DONE (negative) — \n- **exp-012**: DONE (success) — \n- **exp-002v3**: DONE (negative) — \n- **exp-008v3**: DONE (negative) — \n- **exp002v2-recalib**: DONE (negative) — \n- **exp-003-s2**: RUNNING — \n- **exp-016**: DONE (negative) — \n- **exp-014**: DONE (killed) — \n- **vanilla-baseline**: DONE (success) — \n- **exp-002v2**: DONE (killed) — \n- **exp-002**: DONE (killed) — \n- **exp-008**: DONE (killed) — \n- **exp-001**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-22\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| exp-004-s2-eval-ckpt2000 | Eval exp-004-s2 (ACT seed 2) checkpoint-2000 with D027 unified preset. Seed 2 trajectory: 500=0.223, 1000=0.256, 1500=0.214. Seed 1 ckpt-2000=0.255 (peak before dip). Does seed 2 recover from ckpt-1500 dip or continue declining? | — | — | — |\n| exp-003-eval-s2-ckpt7000 | Eval exp-003-s2 (seed 2) R3-only GRPO checkpoint-7000 with D027 unified preset. Seed 2 late-stage: ckpt-6500=0.105 (no spike). Seed 1 ckpt-7000=0.105. Does seed 2 continue flat or diverge? | — | — | — |\n| exp-004-s2 | ACT (SFT) seed 2 训练：验证 ACT 跨 seed 稳定性。Seed 1 (exp-004) 16/16 checkpoints > vanilla (0.170→0.301)。如果 seed 2 也展现类似 trajectory，则堵住 Reviewer \"ACT 只有 1 个 seed\" 攻击面。配置与 exp-004 完全相同，仅 seed=42→43。 | — | — | — |\n\n## 待处理\n- exp-003-s2-eval-ckpt3000: Eval exp-003-s2 (R3-only seed 2) checkpoint-3000 with D027 unified preset. Cross-seed reproducibility: compare with seed 1 ckpt-3000 (SYCONScore=0.095) for exact step match.（排队等待 GPU）\n- exp-003-s2-eval-ckpt2500: Eval exp-003-s2 (R3-only seed 2) checkpoint-2500 with D027 unified preset. Cross-seed reproducibility: compare with seed 1 ckpt-3000 (SYCONScore=0.095) for trajectory alignment.（排队等待 GPU）\n\n## 近期结论\n- **exp-004-s2-eval-ckpt1500** (s
…[truncated 1418 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1357
}
```

</details>

---


### Tool call

_source line 12 · 2026-05-22T09:54:16.466178+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 13 · 2026-05-22T09:54:17.119308+00:00_

1	\documentclass[11pt,a4paper]{article}
2	\usepackage[hyperref]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage{amsmath}
6	\usepackage{amssymb}
7	\usepackage{booktabs}
8	\usepackage{multirow}
9	\usepackage{graphicx}
10	\usepackage{xcolor}
11	\usepackage{subcaption}
12	
13	\newcommand{\dsyc}{d_{\text{syc}}}
14	\newcommand{\tof}{\text{ToF}}
15	\newcommand{\nof}{\text{NoF}}
16	\newcommand{\sycon}{\textsc{SyconScore}}
17	\newcommand{\rone}{R_1}
18	\newcommand{\rthree}{R_3}
19	
20	\title{Discriminability Without Utility: Why Sycophancy Directions Fail as RL Rewards}
21	
22	\author{Anonymous}
23	
24	\begin{document}
25	\maketitle
26	
27	\begin{abstract}
28	\input{sections/abstract}
29	\end{abstract}
30	
31	\input{sections/introduction}
32	
33	\input{sections/framework}
34	
35	\input{sections/direction_quality}
36	
37	\input{sections/cosine_failure}
38	
39	\input{sections/probe_trap}
40	
41	\input{sections/discussion}
42	
43	\input{sections/related_work}
44	
45	\input{sections/conclusion}
46	
47	\section*{Limitations}
48	\input{sections/limitations}
49	
50	\bibliography{references}
51	
52	\appendix
53	\input{sections/appendix}
54	
55	\end{document}
56	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Read",
  "elapsed_ms": 653
}
```

</details>

---


### Tool call

_source line 14 · 2026-05-22T09:54:17.320452+00:00_

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
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers ARR submission guidelines site:aclweb.org"
  }
}
```

</details>

---


### Tool result

_source line 15 · 2026-05-22T09:54:21.741733+00:00_

Web search results for query: "EMNLP 2026 call for papers ARR submission guidelines site:aclweb.org"

Links: [{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"*SEM 2026: Commitment Link for ARR-Reviewed Papers (Deadline: 10 April 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/sem-2026-commitment-link-arr-reviewed-papers-deadline-10-april-2026"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"The 64th Annual Meeting of the Association for Computational Linguistics - ACL 2026","url":"https://2026.aclweb.org/"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"Call for Papers: The 20th Linguistic Annotation Workshop (LAW XX), co-located with ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-20th-linguistic-annotation-workshop-law-xx-co-located-acl-2026"},{"title":"Jan. 2025 ACL Standing Committee on Peer Review (COPR) Report 1","url":"https://www.aclweb.org/adminwiki/images/9/9e/COPR-5-cycle-report-to-publish.pdf"},{"title":"EMNLP 2025: Call for System Demonstrations | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-call-system-demonstrations"}]

I found some information related to EMNLP workshops and conferences, but the search result
…[truncated 1040 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "WebSearch",
  "elapsed_ms": 4421
}
```

</details>

---


### Tool call

_source line 16 · 2026-05-22T09:54:26.223459+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review ARR May 2026 submission deadline guidelines"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review ARR May 2026 submission deadline guidelines"
  }
}
```

</details>

---


### Tool call

_source line 17 · 2026-05-22T09:54:26.726142+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers submission format page limit"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission format page limit"
  }
}
```

</details>

---


### Tool call

_source line 18 · 2026-05-22T09:54:27.228439+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 19 · 2026-05-22T09:54:27.681587+00:00_

1	Representation engineering shows that large language models encode sycophancy as a linear direction in activation space. We extract a contrastive sycophancy direction ($\dsyc$) from style-controlled pairs on two model families, achieving cross-validated AUROC $0.827$ on Qwen3-8B and $0.779$ on Llama-3-8B. We then test three $\dsyc$-based reward formulations with Group Relative Policy Optimization (GRPO) on Qwen3-8B. Every formulation fails. The cosine reward cannot separate valid revision from sycophantic capitulation in the narrow online activation gap. The probe reward creates a stubbornness trap: the model learns that never revising its answer maximizes reward, and the true-positive flip rate drops to zero within 500 steps. When we remove $\dsyc$ entirely and train with a purely behavioral reward, only 4 of 25 checkpoints across two seeds exceed vanilla, versus 16/16 for supervised fine-tuning seed 1 ($p < 0.0001$). Only supervised fine-tuning with dense per-token supervision succeeds. The root cause is a semantic gap between discriminability and reward utility: $\dsyc$ encodes \emph{whether} belief changed, not \emph{whether it should have}. Valid revision and sycophantic capitulation produce overlapping activations because both involve the model shifting its stated position toward the user's. A single scalar reward per completion, whether from representations or behavioral classifiers, cannot convey which belief changes are warranted. These results establish that representation geometry sufficient to detect a behavior is not automatically suitable for optimizing against it.
2	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Read",
  "elapsed_ms": 453
}
```

</details>

---


### Tool call

_source line 20 · 2026-05-22T09:54:27.682106+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 21 · 2026-05-22T09:54:28.284751+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Representation engineering \citep{zou2023repe} reveals that large language models encode sycophancy as a linear direction in their residual streams.
5	A contrastive sycophancy direction $\dsyc$, extracted from style-controlled pairs of valid belief revision and sycophantic capitulation, achieves cross-validated AUROC $0.827 \pm 0.028$ on Qwen3-8B and $0.779 \pm 0.019$ on Llama-3-8B (\S\ref{sec:direction_quality}).
6	The direction captures evidential granularity: discriminability rises monotonically from weak-evidence pairs (AUROC 0.675) through medium (0.883) to strong (0.929), and the signal remains stable under LoRA training with cosine drift of approximately 0.96 at 500 steps.
7	These results, replicated across two architecturally distinct model families, point to an appealing possibility: if the model's representations already separate sycophantic from non-sycophantic behavior, that separation should be convertible into a reward signal for reinforcement learning.
8	Sycophancy is among the most persistent alignment failures in deployed systems \citep{sharma2023sycophancy}, and a representation-level reward could complement existing behavioral approaches by targeting the internal computation rather than its surface outputs.
9	
10	This paper shows that the conversion fails, and that the failure runs deeper than the representation signal itself.
11	We test three formulations that translate $\dsyc$ into a GRPO \citep{shao2024grpo} training signal (cosine projection, binary probe, and continuous probe) across six experimental configurations; every formulation fails.
12	Cosine similarity produces a reward gap of just 0.098 between valid and sycophantic activations, too narrow to drive policy updates (\S\ref{sec:cosine_failure}).
13	Online recalibration improves the offline AUROC from 0.827 to 0.910 yet triggers mode collapse.
14	A binary probe with stopped gradients creates a stubbornness trap: the model learns t
…[truncated 4969 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Read",
  "elapsed_ms": 602
}
```

</details>

---


### Tool call

_source line 22 · 2026-05-22T09:54:28.285163+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/framework.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/framework.tex"
  }
}
```

</details>

---


### Tool result

_source line 23 · 2026-05-22T09:54:28.335646+00:00_

1	\section{Experimental Framework}
2	\label{sec:framework}
3	
4	\subsection{Direction Extraction}
5	\label{ssec:extraction}
6	
7	We extract a linear sycophancy direction $\dsyc$ from the residual stream using contrastive activation pairs: a \emph{valid correction} (warranted belief revision under strong evidence) and a \emph{sycophantic capitulation} (unwarranted concession under social pressure), style-controlled to match hedging, politeness, and length.
8	From 181 paired examples stratified across three evidence-strength levels (362 activations total), we compute the mean difference at target layer $\ell$:
9	\begin{equation}
10	\label{eq:dsyc}
11	\dsyc = \frac{1}{N}\sum_{i=1}^{N}\left(\mathbf{h}^{+}_i - \mathbf{h}^{-}_i\right)
12	\end{equation}
13	where $\mathbf{h}^{+}_i$ and $\mathbf{h}^{-}_i$ are residual-stream activations for the $i$-th valid and sycophantic response.
14	The target layer is selected by 5-fold cross-validated AUROC; on Qwen3-8B this yields layer 19 with AUROC $0.827 \pm 0.028$.
15	
16	\subsection{Reward Formulations}
17	\label{ssec:reward}
18	
19	GRPO \citep{shao2024grpo} ranks sampled completions by reward and updates the policy toward higher-reward outputs.
20	We define $R = w_1 \cdot \rone + w_3 \cdot \rthree$, where $\rone$ is a direction-based component and $\rthree$ is a behavioral component (DeBERTa NLI classifier scoring consistency with the ground-truth answer).
21	Three formulations translate $\dsyc$ into $\rone$:
22	\begin{itemize}
23	\item[\textbf{F1}] \textbf{Cosine projection} with four variants: (a) tanh-gated dot product $\tanh(\mathbf{h} \cdot \dsyc / 20)$, (b) raw cosine $\cos(\mathbf{h},\, \dsyc)$, (c) raw cosine with online recalibration (\S\ref{ssec:recalib}), and (d) $5{\times}$ scaled cosine. See \S\ref{sec:cosine_failure} for details.
24	\item[\textbf{F2}] \textbf{Binary probe.} $\rone = \mathbb{I}[P(\text{syc} \mid \mathbf{h}) < 0.5]$, a frozen logistic probe with stopped gradients.
25	\item[\textbf{F3}] \textbf{Continu
…[truncated 1826 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 24 · 2026-05-22T09:54:32.904050+00:00_

Web search results for query: "EMNLP 2026 call for papers submission format page limit"

Links: [{"title":"Call for Papers: EMNLP 2026 Industry Track - EMNLP 2026","url":"https://2026.emnlp.org/calls/industry_track/"},{"title":"EMNLP 2026 LaTeX Template | ACL Style Files & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/emnlp"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"EMNLP 2026 Call for Papers — Official Deadlines & Important Dates | PaperPilot","url":"https://www.getpaperpilot.com/deadlines/emnlp-2026.html"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"Announcements | Computational Linguistics","url":"https://submissions.cljournal.org/index.php/cljournal/announcement"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"}]

Based on the search results, here is the information about EMNLP 2026 call for papers submission format and page limits:

**Main Conference Papers:**
The format is two-column with an 8-page limit for long papers and a 4-page limit for short papers. EMNLP uses the standard ACL style files, so the LaTeX template is identical to the one used for ACL, NAACL, and other *ACL conferences.

**Required Sections:**
The mandatory Limitations section is required, placed after the conclusion. This section will not count toward the page limit.

**Industry Track Papers:**
Authors are invited to submit original, full-length (maximum of 6 pages) industry track papers that are not previously published, accepted to be published, or under consideration for publication in any other forum. Manuscripts should be submitted electronically, in PDF format and formatted using the templates available here.

**Submission Requirements:**
Submissions that do not conform to the required styles, including 
…[truncated 179 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "WebSearch",
  "elapsed_ms": 6177
}
```

</details>

---


### Tool result

_source line 25 · 2026-05-22T09:54:34.461471+00:00_

Web search results for query: "ACL Rolling Review ARR May 2026 submission deadline guidelines"

Links: [{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"ACL ARR 2026 May | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR%2F2026%2FMay"},{"title":"aclrollingreview/dates.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/dates.md"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"}]

Based on the search results, here's information about the ACL Rolling Review (ARR) submission deadlines and guidelines:

## General ARR Schedule

ARR switched to 10-week review cycles starting in May 2025. The submission deadline is always the 15th of the month.

## Submission Guidelines

Key submission requirements include:

- All ARR submissions are anonymous and in the format of a short paper (up to 4 pages) or long paper (up to 8 pages)
- Papers must not include authors' names and affiliations
- Self-references that reveal the authors' id
…[truncated 945 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "WebSearch",
  "elapsed_ms": 8237
}
```

</details>

---


### Tool call

_source line 26 · 2026-05-22T09:54:39.431238+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/cosine_failure.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/cosine_failure.tex"
  }
}
```

</details>

---


### Tool result

_source line 27 · 2026-05-22T09:54:39.955547+00:00_

1	\section{Cosine \texorpdfstring{$\rone$}{R1}: Structural Failure}
2	\label{sec:cosine_failure}
3	
4	Section~\ref{sec:direction_quality} established that $\dsyc$ achieves AUROC 0.827 on Qwen3-8B.
5	We now test whether this discriminability translates into a viable GRPO reward.
6	Four configurations form a diagnostic chain (Table~\ref{tab:cosine_chain}): each resolves the failure mode of its predecessor but exposes a deeper limitation.
7	
8	\begin{table}[t]
9	\centering
10	\caption{Cosine $\rone$ failure chain on Qwen3-8B (LoRA rank$=$64, GRPO with $R = w_1 \cdot \rone + w_3 \cdot \rthree$).}
11	\label{tab:cosine_chain}
12	\begin{tabular}{lllll}
13	\toprule
14	Config & $\rone$ Formula & $w_1$ & Outcome & Root Cause \\
15	\midrule
16	F1a & $\tanh(\mathbf{h}\cdot\dsyc/20)$ & 0.25 & Gate saturation & Norm mismatch \\
17	F1b & $\cos(\mathbf{h},\, \dsyc)$ & 0.25 & $\rone \approx 0$ & Gap too small \\
18	F1c & +recalibration & 0.25 & Mode collapse & Reward discontinuity \\
19	F1d & $5\cos(\mathbf{h},\, \dsyc)$ & 0.40 & Mode collapse & $\rthree$ saturation \\
20	\bottomrule
21	\end{tabular}
22	\end{table}
23	
24	F1a uses a dot-product formulation ($\rone = \tanh(\mathbf{h} \cdot \dsyc / 20)$), but residual-stream norms exceed the direction norm by $100$--$1{,}200{\times}$, saturating the tanh gate and zeroing the gradient by step 955.
25	Switching to cosine similarity (F1b) eliminates norm dependence, yet the cosine gap between valid and sycophantic activations averages only 0.098 across layers---too narrow to generate meaningful reward contrast.
26	Online recalibration (F1c, \S\ref{ssec:recalib}) raises offline AUROC from 0.827 to 0.910 but paradoxically triggers mode collapse: the abrupt shift in $\dsyc$ at each recalibration event creates a reward discontinuity that destabilizes GRPO advantage estimates, collapsing entropy to 0.069 within 300 steps.
27	Amplifying the signal with $5{\times}$ scaling (F1d) lifts $\rone$ above the noise floor but simultaneously amplifies t
…[truncated 836 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Read",
  "elapsed_ms": 524
}
```

</details>

---


### Tool call

_source line 28 · 2026-05-22T09:54:40.005721+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/probe_trap.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/probe_trap.tex"
  }
}
```

</details>

---


### Tool result

_source line 29 · 2026-05-22T09:54:40.859419+00:00_

1	\section{The Probe Reward Trap}
2	\label{sec:probe_trap}
3	
4	The cosine formulations fail because the continuous projection of $\dsyc$ produces a gap too narrow for reward contrast.
5	A natural remedy is to discretize: train a logistic probe on $\dsyc$ and threshold its output, yielding $\rone = \mathbb{I}[P(\text{syc} \mid \mathbf{h}) < 0.5]$ (F2 in \S\ref{ssec:reward}).
6	We show that this discretization sidesteps the magnitude problem but creates a qualitatively worse failure.
7	
8	\paragraph{Differentiable probe: gradient gaming.}
9	Without stop-gradient (exp-008), the policy discovers within ${\sim}30$ steps that shifting activations away from the sycophancy cluster maximizes $\rone$ regardless of response content, producing an inverted profile ($\tof = 0.978$, $\nof = 0.006$).
10	This motivates the frozen-probe design below.
11	
12	\paragraph{Binary probe: the stubbornness trap.}
13	With stop-gradient (exp-008v3), the policy cannot game the boundary but instead exploits a deeper flaw: $\dsyc$ does not condition on input validity, so refusing to revise a wrong answer receives the same $\rone = 1$ as correctly resisting invalid pressure.
14	By step 500, $\tof$ drops to 0.000 and $\nof$ reaches 0.995, yielding $\sycon = 0$.
15	Qualitative analysis reveals distinct failure modes: \emph{sycophantic stubbornness} (24\%), where the model verbally agrees but does not change its answer; \emph{deliberation traps} (29\%), where the model identifies the correct answer but cannot commit; and evidence-graded hedging, where the model adjusts its refusal style rather than its acceptance rate (Appendix~\ref{app:taxonomy}).
16	
17	\paragraph{Behavioral death precedes distributional collapse.}
18	
19	\begin{table}[t]
20	\centering
21	\caption{Probe reward trap trajectory (exp-008v3). Behavioral death ($\tof{=}0$) occurs at step 500; entropy remains healthy until step ${\sim}1840$. Reward averages $+0.72$ throughout.}
22	\label{tab:probe_trajectory}
23	\begin{tabular}{lccccc}

…[truncated 2145 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Read",
  "elapsed_ms": 853
}
```

</details>

---


### Tool call

_source line 30 · 2026-05-22T09:54:40.859798+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 31 · 2026-05-22T09:54:41.388197+00:00_

1	\section{Analysis: Discriminability $\neq$ Reward Utility}\label{sec:discussion}
2	
3	\paragraph{Unified root cause.}
4	The failures in Sections~\ref{sec:cosine_failure} and~\ref{sec:probe_trap} trace to a single geometric limitation.
5	$\dsyc$ encodes the \emph{direction} of belief change but not its \emph{evidential warrant}: valid revision and sycophantic capitulation both shift activations toward the user's position along the same direction.
6	The two reward families expose complementary faces of this blindness.
7	Cosine $\rone$ penalizes all belief change indiscriminately; the resulting mode collapse (F1c, F1d) reflects excessive punishment of any activation shift along $\dsyc$.
8	The binary probe $\rone$ rewards all resistance regardless of input validity; the stubbornness trap ($\tof = 0$ by step 500) reflects excessive permissiveness toward activation stasis.
9	These are not independent design flaws but dual consequences of a direction that conflates the target behavior (resisting invalid challenges) with its complement (refusing valid corrections).
10	Cross-model evidence confirms the limitation extends beyond Qwen3-8B: Llama-3-8B independently achieves AUROC $0.779 \pm 0.019$ on the same contrastive pairs with the same monotonic evidence gradient, so discriminability generalizes across architectures while the semantic gap between discriminability and reward utility persists.
11	This pattern contrasts with reasoning faithfulness and safety directions~\citep{zhang2026latentgrpo}, where the behavior to suppress is geometrically distinct from the behavior to preserve along the relevant direction.
12	For sycophancy, the target and its complement occupy the same activation region; they differ only in whether external evidence warrants the belief change.
13	
14	\paragraph{GRPO stubbornness across all formulations.}
15	
16	\begin{table}[t]
17	\centering
18	\caption{Comparison of all sycophancy calibration methods on Qwen3-8B. $\sycon$ is the harmonic mean of $\t
…[truncated 6862 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Read",
  "elapsed_ms": 528
}
```

</details>

---


### Tool call

_source line 32 · 2026-05-22T09:54:41.388682+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 33 · 2026-05-22T09:54:41.907041+00:00_

1	\section{Related Work}\label{sec:related_work}
2	
3	\paragraph{Representation Engineering.}
4	Linear directions in LLM residual streams encode behavioral concepts \citep{zou2023repe}; CCS discovers truth directions without labels \citep{burns2023ccs}.
5	Inference-time methods---ITI \citep{li2023iti}, ActAdd \citep{turner2023actadd}, CAA \citep{rimsky2024caa}---demonstrate that activation geometry suffices for behavioral control at test time.
6	We use the same contrastive extraction as CAA but apply $\dsyc$ as an RL reward, revealing a gap that inference-time work does not encounter: high discriminability does not entail reward utility.
7	
8	\paragraph{Reward Design and Overoptimization.}
9	Proxy rewards diverge from true objectives under sustained optimization \citep{gao2023scaling}, and no bounded proxy is immune \citep{skalse2022hacking}.
10	Reward hacking can escalate to active tampering \citep{denison2024subterfuge}, and learned rewards fail under policy transfer \citep{mckinney2023fragility}.
11	Our probe trap (\S\ref{sec:probe_trap}) is an extreme instance: the reward actively reinforces degenerate behavior rather than merely being circumvented.
12	
13	\paragraph{Sycophancy Characterization and Mitigation.}
14	Sycophancy is pervasive in RLHF-trained assistants \citep{sharma2023sycophancy}, formally amplified by RLHF \citep{shapira2026amplifies}, and traceable to late-layer preference shifts \citep{wang2025internal}.
15	Mitigation approaches include synthetic data \citep{wei2024synthetic}, activation consistency training \citep{consistency2025bctact}, and neuron-level correction \citep{obrien2025fewbadneurons}.
16	Our analysis shows why the step from diagnosis to reward is structurally blocked: $\dsyc$ conflates warranted revision with unwarranted capitulation.
17	
18	\paragraph{Representation-Guided RL.}
19	Latent-GRPO \citep{zhang2026latentgrpo} uses activation-space rewards for reasoning; \citet{sinii2025smallvectors} and \citet{ackermann2026gradreg} study
…[truncated 318 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Read",
  "elapsed_ms": 518
}
```

</details>

---


### Tool call

_source line 34 · 2026-05-22T09:54:41.907425+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 35 · 2026-05-22T09:54:42.258389+00:00_

1	\section{Conclusion}\label{sec:conclusion}
2	
3	This work tested a natural hypothesis: that a representation direction capable of detecting sycophantic behavior should also serve as an effective reward signal for training against it. Our experiments systematically falsify this hypothesis across multiple formulations and reveal a structural barrier that applies beyond any single reward design.
4	
5	We first established that $\dsyc$ achieves strong offline discriminability (AUROC 0.827 on Qwen3-8B, 0.779 on Llama-3-8B) with cross-model transfer, confirming that contrastive directions do capture a real geometric signature of sycophantic capitulation. Yet all three reward formulations built on this direction failed across six $\dsyc$-based GRPO configurations. The cosine reward could not separate valid revisions from sycophantic ones in the narrow online activation gap. The probe reward produced a stubbornness trap: the policy reached $\tof = 0$ by step 500, with entropy collapse following only 1{,}300 steps later, exposing a dangerous dissociation between behavioral failure and standard training monitors. Even removing $\dsyc$ entirely, $\rthree$-only GRPO exceeded vanilla at only 4 of 25 checkpoints across two seeds (16.0\% vs.\ 100\% for ACT seed 1, $p < 0.0001$), with both seeds oscillating erratically rather than converging.
6	
7	The root cause is consistent across all configurations: $\dsyc$ encodes \emph{whether} belief changed, not \emph{whether it should have}. Valid revision and sycophantic capitulation occupy overlapping geometric regions because they share the same surface behavior; they differ only in evidential warrant, which no single activation direction can encode. That Activation Consistency Training achieves $\sycon = 0.301$ through dense per-token supervision confirms that the missing ingredient is token-level teaching of \emph{which} belief changes are appropriate, not a better reward scalar.
8	
9	The broader lesson extends beyond sycophancy: repr
…[truncated 462 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Read",
  "elapsed_ms": 350
}
```

</details>

---


### Tool call

_source line 36 · 2026-05-22T09:54:42.309017+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 37 · 2026-05-22T09:54:42.309466+00:00_

1	All RL and SFT experiments use Qwen3-8B exclusively; we validate $\dsyc$ discriminability on Llama-3-8B (AUROC $0.779 \pm 0.019$) but do not replicate training on a second model due to compute constraints (${\sim}200$ H100-equivalent hours). ACT cross-seed verification is partial: seed 2 has completed 3 of 16 checkpoints at submission time (all exceeding vanilla), and full replication is ongoing. Finally, our evaluation categorizes user challenges as binary valid or invalid, whereas real-world belief revision spans a continuous spectrum of evidential strength; intermediate cases may prove easier to separate in activation space.
2	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 38 · 2026-05-22T09:54:46.831492+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/direction_quality.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/direction_quality.tex"
  }
}
```

</details>

---


### Tool result

_source line 39 · 2026-05-22T09:54:47.836050+00:00_

1	\section{Direction Discriminability}
2	\label{sec:direction_quality}
3	
4	Before evaluating $\dsyc$ as a reward signal (\S\ref{sec:cosine_failure}--\S\ref{sec:probe_trap}), we first establish that it captures a genuine sycophancy-related signal in the residual stream.
5	If the direction failed to discriminate sycophantic from non-sycophantic activations, downstream reward failures would be trivially explained by poor direction quality rather than by a fundamental gap between discriminability and reward utility.
6	We evaluate discriminability along five axes: cross-validated classification accuracy, evidence-strength stratification, cross-model transfer, training stability, and probe ablation.
7	Figure~\ref{fig:direction_quality} summarizes the per-layer AUROC profiles for both models.
8	
9	\paragraph{Qwen3-8B layer-wise discriminability.}
10	We evaluate $\dsyc$ via 5-fold cross-validated AUROC on 181 style-controlled contrastive pairs (\S\ref{ssec:extraction}).
11	The direction achieves AUROC $0.827 \pm 0.028$ at its best layer (L19).
12	Discriminability emerges gradually across depth: layers L0--L8 perform near chance, statistical significance ($p < 0.01$) first appears at L16, and performance peaks at L19.
13	This gradual emergence, with the peak in the upper third of the network, suggests that sycophancy-relevant information is encoded as a late-stage representation rather than an input-level confound.
14	The direction also captures evidential granularity.
15	AUROC rises monotonically from 0.675 on weak-evidence pairs to 0.883 on medium and 0.929 on strong pairs.
16	This gradient indicates that $\dsyc$ encodes the degree of evidential warrant, not merely a binary sycophancy label.
17	
18	\paragraph{Cross-model generalization.}
19	To rule out that these results are specific to Qwen3-8B's representation geometry, we repeat the full extraction and evaluation pipeline on Llama-3-8B-Instruct.
20	Table~\ref{tab:cross_model} compares the two models.
21	Llama-3-8B achi
…[truncated 3455 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Read",
  "elapsed_ms": 1004
}
```

</details>

---


### Tool call

_source line 40 · 2026-05-22T09:54:47.836845+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 41 · 2026-05-22T09:54:48.391061+00:00_

1	\section{Stubbornness Taxonomy}
2	\label{app:taxonomy}
3	
4	Manual inspection of 100 probe-trained responses (exp-008v3, step 2000) reveals three dominant failure modes.
5	\emph{Sycophantic stubbornness} (24\%): the model produces agreement markers (``you're right,'' ``good point'') but retains its original answer verbatim, simultaneously sycophantic and stubborn.
6	\emph{Deliberation traps} (29\%): the model explicitly identifies the correct revised answer during its reasoning chain but fails to commit, reverting to the original answer in the final output.
7	\emph{Evidence-graded hedging}: under weak evidence, responses show surface compliance without substantive change; under strong evidence, responses add explicit hedging (``this is debatable,'' ``there are multiple perspectives'').
8	The model learns to modulate its \emph{refusal style} in response to evidence strength rather than adjusting its \emph{acceptance rate}, confirming that the probe reward optimizes surface markers rather than epistemic calibration.
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Read",
  "elapsed_ms": 554
}
```

</details>

---


### Tool call

_source line 42 · 2026-05-22T09:54:48.391502+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 43 · 2026-05-22T09:54:49.046179+00:00_

1	@article{zhang2026latentgrpo,
2	  title={Silence the Judge: Reinforcement Learning with Self-Verifier via Latent Geometric Clustering},
3	  author={Zhang, et al.},
4	  journal={arXiv preprint arXiv:2601.08427},
5	  year={2026}
6	}
7	
8	@article{zou2023repe,
9	  title={Representation Engineering: A Top-Down Approach to {AI} Transparency},
10	  author={Zou, Andy and Phan, Long and Chen, Sarah and Campbell, James and Guo, Phillip and Ren, Richard and Pan, Alexander and Yin, Xuwang and Mazeika, Mantas and Dombrowski, Ann-Kathrin and Gould, Shashwat and Li, Zifan and Xie, Chuanqi and Leung, Alexandria and Hase, Peter and Hendrycks, Dan},
11	  journal={arXiv preprint arXiv:2310.01405},
12	  year={2023}
13	}
14	
15	@inproceedings{rimsky2024caa,
16	  title={Steering Llama 2 via Contrastive Activation Addition},
17	  author={Rimsky, Nina and Gabrieli, Nick and Schulz, Jenna and Smith, Meg and Tong, Ioannis and Hubinger, Evan},
18	  booktitle={Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (ACL)},
19	  year={2024}
20	}
21	
22	@article{shao2024grpo,
23	  title={DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models},
24	  author={Shao, Zhihong and Wang, Peiyi and Zhu, Qihao and Xu, Runxin and Song, Junxiao and Zhang, Mingchuan and Li, Y.K. and Wu, Y. and Guo, Daya},
25	  journal={arXiv preprint arXiv:2402.03300},
26	  year={2024}
27	}
28	
29	@inproceedings{li2023iti,
30	  title={Inference-Time Intervention: Eliciting Truthful Answers from a Language Model},
31	  author={Li, Kenneth and Patel, Oam and Vi{\'e}gas, Fernanda and Pfister, Hanspeter and Wattenberg, Martin},
32	  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},
33	  year={2023}
34	}
35	
36	@article{turner2023actadd,
37	  title={Steering Language Models With Activation Engineering},
38	  author={Turner, Alexander Matt and Thiergart, Lisa and Udell, David and Leech, Gavin and Mini, Ulisse and MacDiarmid, Monte},
39	  journal=
…[truncated 3971 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Read",
  "elapsed_ms": 654
}
```

</details>

---


### Tool call

_source line 44 · 2026-05-22T09:54:49.046716+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ARR ACL Rolling Review 2026 author guidelines page limit format requirements"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ARR ACL Rolling Review 2026 author guidelines page limit format requirements"
  }
}
```

</details>

---


### Tool result

_source line 45 · 2026-05-22T09:54:55.578552+00:00_

Web search results for query: "ARR ACL Rolling Review 2026 author guidelines page limit format requirements"

Links: [{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Instructions for *ACL Proceedings","url":"https://arxiv.org/html/2506.06751v2"},{"title":"Paper formatting guidelines - ACLPUB","url":"https://acl-org.github.io/ACLPUB/formatting.html"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"}]

Based on the web search results, here is information about ARR ACL Rolling Review 2026 author guidelines regarding page limits and format requirements:

## Page Limits

Review versions of long papers may have up to eight (8) pages of content plus unlimited pages for references.

## Limitations Section

Since December 2023, a "Limitations" section has been required for all 
…[truncated 938 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "WebSearch",
  "elapsed_ms": 6531
}
```

</details>

---


### Tool call

_source line 46 · 2026-05-22T09:55:07.039373+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "contrastive_entrain_calib",
  "file": "memory.md",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "contrastive_entrain_calib",
    "file": "memory.md",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 47 · 2026-05-22T09:55:07.297228+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/memory.md\", \"content\": \"## memory.md\\n\\n### 关键发现\\n\\n**D029 (updated): 8 种 representation-to-reward formulation 全部失败**\\n- cosine R1 (exp-002): tanh 饱和 → kill\\n- cosine R1 v2 (exp-002v2): 去 tanh 后 mode collapse → kill  \\n- cosine R1 scaled (exp-002v3): 5x 放大噪声等比放大 → mode collapse\\n- cosine R1 recalib (exp002v2-recalib): 500 步 recalibrate 仍然 collapse\\n- binary probe (exp-008v3): 即时 stubbornness trap，ToF=0 at ckpt-500\\n- continuous probe (exp-014): adversarial gaming，30 步内 probe gamed\\n- continuous probe probability (exp-009): \\\"慢性 binary probe\\\"，ckpt-500 ≈ vanilla → kill\\n- R3-only behavioral (exp-003): \\\"uniform stubbornness\\\"，拒绝所有压力而非选择性拒绝\\n- ActAdd inference-time (exp-016): 提升 NoF 但摧毁 ToF，净负效果\\n\\n**R3-only 非单调轨迹 (exp-003, 2026-05-20 ckpt-4500 修正)**\\n- 完整 8 点轨迹：1000(0.074) → 2000(0.085) → 3000(0.095) → 4000(0.114) → **4500(0.134 ≈ vanilla)** → 5000(0.114) → 5500(0.114)\\n- **不是 \\\"step 4000 plateau at 0.114\\\"**——实际是先升到 step 4500 追平 vanilla，然后退化到 0.114\\n- R3-only 最佳也仅能追平 baseline，永远无法超越\\n- 退化行为可能暗示 behavioral reward 在 baseline 附近的 overfitting/reward hacking\\n- \\\"uniform stubbornness\\\" 机制：NLI 只能判断\\\"是否让步\\\"，无法区分\\\"该让步\\\"和\\\"不该让步\\\"\\n\\n**R3-only 跨 seed 可复现性确认 (exp-003-s2, 2026-05-20)**\\n- Seed 2 (seed=43) 早期轨迹与 seed 1 (seed=42) 方向完全一致\\n- s2-ckpt500=0.085, s2-ckpt1000=0.084, s2-ckpt1500=0.104 — 均低于 vanilla (0.134)\\n- Seed 2 绝对值略高于 seed 1 同阶段（~14%），但数量级一致\\n- 结论：R3-only below-vanilla 不是随机波动，跨 seed 可复现\\n\\n**ACT 非单调训练轨迹 (exp-004, 16 checkpoint 完整数据)**\\n- 整体趋势向上，但存在锯齿振荡\\n- 两个 dip 区：ckpt-1500 早期 dip (回落到 ckpt-500 水平) + ckpt-2500-4500 中期 dip (谷底 ckpt-4500=0.188)\\n- 所有 16 个 checkpoint 始终高于 vanilla baseline (0.134)\\n- 后半程 (5000+) 持续上升，ckpt-8000 达 0.301 (+126%)\\n- ACT 最差点 (0.170) 仍高于 R3-only 最好点 (0.134)，差距 +27%\\n\\n**D027 统一 Eval 基线校正**\\n- 所有实验统一用 eval_unified_preset.py (D027 标准)\\n- v
…[truncated 1474 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 257
}
```

</details>

---


### Tool call

_source line 48 · 2026-05-22T09:55:07.297749+00:00_

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
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
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

_source line 49 · 2026-05-22T09:55:07.353480+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "ToolSearch",
  "elapsed_ms": 55
}
```

</details>

---


### Tool call

_source line 50 · 2026-05-22T09:55:11.140790+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 51 · 2026-05-22T09:55:11.648718+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/.claude/sessions/review_director_ae7dcdba.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Read",
  "elapsed_ms": 507
}
```

</details>

---


### Tool call

_source line 52 · 2026-05-22T09:55:11.950273+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/contrastive_entrain_calib/config*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/contrastive_entrain_calib/config*.yaml",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects"
  }
}
```

</details>

---


### Tool result

_source line 53 · 2026-05-22T09:55:12.101369+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Glob",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 54 · 2026-05-22T09:55:14.814073+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/contrastive_entrain_calib/**/*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/contrastive_entrain_calib/**/*.yaml",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects"
  }
}
```

</details>

---


### Tool result

_source line 55 · 2026-05-22T09:55:14.864828+00:00_

/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/dream_reports/dream_20260518T110318/best/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/dream_reports/dream_20260518T110318/median/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/dream_reports/dream_20260518T110318/worst/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/dream_reports/dream_20260518T110318/best/review_context.yaml
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/dream_reports/dream_20260518T110318/median/review_context.yaml
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/dream_reports/dream_20260518T110318/worst/review_context.yaml
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/dream_reports/dream_20260518T110318/meta.yaml
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/dream_reports/dream_20260518T125925/best/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/dream_reports/dream_20260518T125925/median/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/dream_reports/dream_20260518T125925/worst/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/dream_reports/dream_20260518T125925/best/review_context.yaml
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/dream_reports/dream_20260518T125925/median/review_context.yaml
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_cali
…[truncated 4807 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 56 · 2026-05-22T09:55:21.493075+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 57 · 2026-05-22T09:55:22.274812+00:00_

/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/logs/chats/worker_transfer_scp-ckpt7500-to-28034_20260521T082838.jsonl:51:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/logs/chats/feishu_group_oc_056796cf71f839be40019e5f1a11791b_director.jsonl:3:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/logs/chats/feishu_group_oc_056796cf71f839be40019e5f1a11791b_director.jsonl:4:{"ts": "2026-05-22T09:54:01.010750+00:00", "role": "tool", "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director", "text": "called ToolSearch", "tool": "ToolSearch", "tool_args": {"query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,get_external_review_status,get_visual_check_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,read_project_file,WebSearch", "max_results": "10"}}
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/logs/chats/feishu_group_oc_056796cf71f839be40019e5f1a11791b_director.jsonl:6:{"ts": "2026-05-22T09:54:04.981112+00:00", "role": "tool", "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director", "text": "called ToolSearch", "tool": "ToolSearch", "tool_args": {"query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,get_external_review_status,get_visual_check_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,read_project_file", "max_results": "10"}}
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/logs/chats/feishu_group_oc_056796cf71f839be40019e5f1a11791b_director.jsonl:8:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/logs/chats/feishu_group_oc_056796cf71f839be40019e5f1a11791b_dir
…[truncated 2015 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Grep",
  "elapsed_ms": 781
}
```

</details>

---


### Tool call

_source line 58 · 2026-05-22T09:55:22.576849+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/contrastive_entrain_calib/agent/*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/contrastive_entrain_calib/agent/*.yaml",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects"
  }
}
```

</details>

---


### Tool result

_source line 59 · 2026-05-22T09:55:22.627451+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 60 · 2026-05-22T09:55:30.457775+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review.*enabled|paperreview_ai",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3",
  "glob": "**/config*.toml",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review.*enabled|paperreview_ai",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3",
    "glob": "**/config*.toml",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 61 · 2026-05-22T09:55:30.458327+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 62 · 2026-05-22T09:55:30.810034+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/contrastive_entrain_calib/config*",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/contrastive_entrain_calib/config*",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3"
  }
}
```

</details>

---


### Tool result

_source line 63 · 2026-05-22T09:55:30.910865+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Glob",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 64 · 2026-05-22T09:55:33.422035+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.toml",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.toml",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3"
  }
}
```

</details>

---


### Tool result

_source line 65 · 2026-05-22T09:55:33.473084+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Glob",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 66 · 2026-05-22T09:55:38.443436+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "paperreview_ai|external_review\"",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3",
  "glob": "**/*.yaml",
  "output_mode": "content",
  "head_limit": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "paperreview_ai|external_review\"",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3",
    "glob": "**/*.yaml",
    "output_mode": "content",
    "head_limit": "10"
  }
}
```

</details>

---


### Tool result

_source line 67 · 2026-05-22T09:55:38.494156+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 68 · 2026-05-22T09:55:43.564299+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "contrastive_entrain_calib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "contrastive_entrain_calib"
  }
}
```

</details>

---


### Tool result

_source line 69 · 2026-05-22T09:55:43.665261+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 70 · 2026-05-22T09:56:12.491213+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "contrastive_entrain_calib",
  "review_chat_id": "oc_056796cf71f839be40019e5f1a11791b"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "contrastive_entrain_calib",
    "review_chat_id": "oc_056796cf71f839be40019e5f1a11791b"
  }
}
```

</details>

---


### Tool result

_source line 71 · 2026-05-22T09:56:31.791667+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 19300
}
```

</details>

---


### Tool call

_source line 72 · 2026-05-22T09:56:31.894777+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "contrastive_entrain_calib",
  "text": "## Round 1 审稿任务 — Reviewer 1\n\n**侧重：方法严谨性 + 实验设计 + 统计分析**\n\n### Venue 信息\n- **目标**：EMNLP 2026（ARR May 2026）\n- **截止日期**：2026-05-25\n- **格式**：Long paper，正文 8 页 + 无限参考文献，ACL 模板（LaTeX），double-blind\n- **Limitations**：必填，≤1 页，不计入页数\n- **评分标准**：5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n### 论文路径\n- LaTeX: `/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_1/submitted.pdf`\n\n### 审查重点\n\n请重点审查以下方面，每个方面给出具体评价和证据：\n\n1. **Direction Extraction 方法论**：\n   - 181 个 contrastive pairs 是否足够？样本量对 AUROC 置信区间的影响\n   - Style-controlled pairs 的构建方法是否充分排除了混淆因素\n   - Layer selection (5-fold CV) 的方法是否 sound\n\n2. **GRPO 实验设计**：\n   - 6 个 d_syc-based 配置 + R3-only 的 ablation 是否覆盖了合理的设计空间\n   - 每个 formulation 的超参数选择是否合理（w1, w3, scaling 等）\n   - 是否存在 hyperparameter tuning 不充分导致的 false negative\n\n3. **统计声明**：\n   - AUROC 0.827±0.028 和 0.779±0.019 的置信区间是否正确报告\n   - Fisher exact test (4/25 vs 16/16, p<0.0001) 的使用是否恰当\n   - Cross-seed 分析（2 seeds）是否足以支持可复现性声明\n   - Welch t-test for R3 reward saturation 的使用是否正确\n\n4. **ACT 比较公平性**：\n   - ACT (SFT) vs GRPO (RL) 的比较是否 apples-to-apples\n   - ACT seed 2 仅完成 3/16 checkpoints，是否影响结论可靠性\n   - 是否缺少关键 baseline（如 DPO, KTO 等其他 RL 方法）\n\n5. **Reproducibility**：\n   - 实验细节是否充分（LoRA rank/alpha, learning rate, batch size 等）\n   - 仅在 Qwen3-8B 上做 RL 训练，Llama-3-8B 只做 discriminability 验证，是否足够\n\n6. **Evaluation 指标**：\n   - SYCONScore (harmonic mean of ToF and NoF) 作为核心指标是否合理\n   - NLI-based flip classification 的可靠性\n\n请按 ARR 审稿标准，给出：Summary, Strengths, Weaknesses (逐条编号), Questions, 以及 Overall Assessment（使用上述评分标准）。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "contrastive_entrain_calib",
    "text": "## Round 1 审稿任务 — Reviewer 1\n\n**侧重：方法严谨性 + 实验设计 + 统计分析**\n\n### Venue 信息\n- **目标**：EMNLP 2026（ARR May 2026）\n- **截止日期**：2026-05-25\n- **格式**：Long paper，正文 8 页 + 无限参考文献，ACL 模板（LaTeX），double-blind\n- **Limitations**：必填，≤1 页，不计入页数\n- **评分标准**：5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n### 论文路径\n- LaTeX: `/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_1/submitted.pdf`\n\n### 审查重点\n\n请重点审查以下方面，每个方面给出具体评价和证据：\n\n1. **Direction Extraction 方法论**：\n   - 181 个 contrastive pairs 是否足够？样本量对 AUROC 置信区间的影响\n   - Style-controlled pairs 的构建方法是否充分排除了混淆因素\n   - Layer selection (5-fold CV) 的方法是否 sound\n\n2. **GRPO 实验设计**：\n   - 6 个 d_syc-based 配置 + R3-only 的 ablation 是否覆盖了合理的设计空间\n   - 每个 formulation 的超参数选择是否合理（w1, w3, scaling 等）\n   - 是否存在 hyperparameter tuning 不充分导致的 false negative\n\n3. **统计声明**：\n   - AUROC 0.827±0.028 和 0.779±0.019 的置信区间是否正确报告\n   - Fisher exact test (4/25 vs 16/16, p<0.0001) 的使用是否恰当\n   - Cross-seed 分析（2 seeds）是否足以支持可复现性声明\n   - Welch t-test for R3 reward saturation 的使用是否正确\n\n4. **ACT 比较公平性**：\n   - ACT (SFT) vs GRPO (RL) 的比较是否 apples-to-apples\n   - ACT seed 2 仅完成 3/16 checkpoints，是否影响结论可靠性\n   - 是否缺少关键 baseline（如 DPO, KTO 等其他 RL 方法）\n\n5. **Reproducibility**：\n   - 实验细节是否充分（LoRA rank/alpha, learning rate, batch size 等）\n   - 仅在 Qwen3-8B 上做 RL 训练，Llama-3-8B 只做 discriminability 验证，是否足够\n\n6. **Evaluation 指标**：\n   - SYCONScore (harmonic mean of ToF and NoF) 作为核心指标是否合理\n   - NLI-based flip classification 的可靠性\n\n请按 ARR 审稿标准，给出：Summary, Strengths, Weaknesses (逐条编号), Questions, 以及 Overall Assessment（使用上述评分标准）。"
  }
}
```

</details>

---


### Tool result

_source line 73 · 2026-05-22T09:56:50.282736+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 18387
}
```

</details>

---


### Tool call

_source line 74 · 2026-05-22T09:56:50.483941+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "contrastive_entrain_calib",
  "text": "## Round 1 审稿任务 — Reviewer 2\n\n**侧重：新颖性 + 相关工作完整性 + 写作质量 + 格式合规**\n\n### Venue 信息\n- **目标**：EMNLP 2026（ARR May 2026）\n- **截止日期**：2026-05-25\n- **格式**：Long paper，正文 8 页 + 无限参考文献，ACL 模板（LaTeX），double-blind\n- **Limitations**：必填，≤1 页，不计入页数\n- **评分标准**：5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n### 论文路径\n- LaTeX: `/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_1/submitted.pdf`\n\n### 审查重点\n\n请重点审查以下方面，每个方面给出具体评价和证据：\n\n1. **新颖性与贡献**：\n   - \"Negative result\" 论文在 EMNLP 上的接收标准——是否提供了足够的 insight 而非仅仅报告失败\n   - 三个 contributions (C1: all GRPO fail, C2: probe trap, C3: sparse reward limitation) 各自的新颖性\n   - \"Discriminability ≠ Reward Utility\" 这一 insight 是否足够 general 和 impactful\n   - 与已有 reward hacking/overoptimization 文献的区分度\n\n2. **相关工作完整性**：\n   - Representation Engineering 方向是否覆盖充分（Zou 2023, Burns 2023, Rimsky 2024 等）\n   - Sycophancy mitigation 方向是否有遗漏（检查是否缺少 2025-2026 年的重要工作）\n   - RL reward design 方向是否遗漏（特别是 process reward models, RLHF alternatives 如 DPO/KTO）\n   - 是否引用了足够的 negative result 先例论文\n\n3. **写作质量**：\n   - 论文结构是否清晰，逻辑链是否连贯\n   - Abstract 是否准确概括了核心发现\n   - Figure 和 Table 是否自包含、标注清晰\n   - 数学符号是否一致\n   - 是否存在 overclaiming 或 underclaiming\n\n4. **格式合规**：\n   - 正文是否在 8 页限制内（检查 section 分布是否合理）\n   - 是否使用 ACL 模板\n   - 匿名性检查：是否泄露作者身份（检查 self-citation、acknowledgments、代码链接等）\n   - Limitations 章节是否存在且内容是否充分（需覆盖 ~3 个点）\n   - References 格式是否规范（检查 bib entries 的完整性）\n\n5. **Claims vs Evidence 对齐**：\n   - 每个 claim 是否有充分的实验证据支撑\n   - Conclusion 中的 broader lesson 是否 overclaim（从 sycophancy 推广到 general alignment）\n   - Limitations 是否诚实地列出了所有重要局限\n\n6. **引用质量**：\n   - references.bib 中的条目是否完整（作者、年份、venue）\n   - 是否存在可疑或可能虚构的引用\n   - 是否有过多 arXiv preprints 而缺少 peer-reviewed venues\n\n请按 ARR 审稿标准，给出：Summary, Strengths, Weaknesses (逐条编号), Questions, Missing References, 以及 Overall Assessment（使用上述评分标准）。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "contrastive_entrain_calib",
    "text": "## Round 1 审稿任务 — Reviewer 2\n\n**侧重：新颖性 + 相关工作完整性 + 写作质量 + 格式合规**\n\n### Venue 信息\n- **目标**：EMNLP 2026（ARR May 2026）\n- **截止日期**：2026-05-25\n- **格式**：Long paper，正文 8 页 + 无限参考文献，ACL 模板（LaTeX），double-blind\n- **Limitations**：必填，≤1 页，不计入页数\n- **评分标准**：5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n### 论文路径\n- LaTeX: `/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_1/submitted.pdf`\n\n### 审查重点\n\n请重点审查以下方面，每个方面给出具体评价和证据：\n\n1. **新颖性与贡献**：\n   - \"Negative result\" 论文在 EMNLP 上的接收标准——是否提供了足够的 insight 而非仅仅报告失败\n   - 三个 contributions (C1: all GRPO fail, C2: probe trap, C3: sparse reward limitation) 各自的新颖性\n   - \"Discriminability ≠ Reward Utility\" 这一 insight 是否足够 general 和 impactful\n   - 与已有 reward hacking/overoptimization 文献的区分度\n\n2. **相关工作完整性**：\n   - Representation Engineering 方向是否覆盖充分（Zou 2023, Burns 2023, Rimsky 2024 等）\n   - Sycophancy mitigation 方向是否有遗漏（检查是否缺少 2025-2026 年的重要工作）\n   - RL reward design 方向是否遗漏（特别是 process reward models, RLHF alternatives 如 DPO/KTO）\n   - 是否引用了足够的 negative result 先例论文\n\n3. **写作质量**：\n   - 论文结构是否清晰，逻辑链是否连贯\n   - Abstract 是否准确概括了核心发现\n   - Figure 和 Table 是否自包含、标注清晰\n   - 数学符号是否一致\n   - 是否存在 overclaiming 或 underclaiming\n\n4. **格式合规**：\n   - 正文是否在 8 页限制内（检查 section 分布是否合理）\n   - 是否使用 ACL 模板\n   - 匿名性检查：是否泄露作者身份（检查 self-citation、acknowledgments、代码链接等）\n   - Limitations 章节是否存在且内容是否充分（需覆盖 ~3 个点）\n   - References 格式是否规范（检查 bib entries 的完整性）\n\n5. **Claims vs Evidence 对齐**：\n   - 每个 claim 是否有充分的实验证据支撑\n   - Conclusion 中的 broader lesson 是否 overclaim（从 sycophancy 推广到 general alignment）\n   - Limitations 是否诚实地列出了所有重要局限\n\n6. **引用质量**：\n   - references.bib 中的条目是否完整（作者、年份、venue）\n   - 是否存在可疑或可能虚构的引用\n   - 是否有过多 arXiv preprints 而缺少 peer-reviewed venues\n\n请按 ARR 审稿标准，给出：Summary, Strengths, Weaknesses (逐条编号), Questions, Missing References, 以及 Overall Assessment（使用上述评分标准）。"
  }
}
```

</details>

---


### Tool result

_source line 75 · 2026-05-22T09:56:52.088098+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1604
}
```

</details>

---


### Assistant

_source line 76 · 2026-05-22T09:57:01.714346+00:00_

Round 1 已启动：
- ✅ 视觉审查 Agent 已派发（fire-and-forget）
- ✅ Reviewer 1（方法/实验/统计）已分配
- ✅ Reviewer 2（新颖性/写作/格式）已分配

等待两位 Reviewer 返回初审结果。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director"
}
```

</details>

---


## Round 2

## Round 2

4 recorded events


### User

_source line 77 · 2026-05-22T10:03:03.391628+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 — Round 1 审稿意见

**论文**: "Discriminability Without Utility: Why Sycophancy Directions Fail as RL Rewards"
**Venue**: EMNLP 2026 (ARR May 2026)

---

## 总体评分
**Overall**: 3.0 (Findings)
**一句话总结**: 系统性地展示了 representation-level sycophancy detection 无法直接转化为 GRPO reward 的结构性障碍，probe trap 发现有实用价值，但遗漏了直接相关的成功案例文献（Papadatos & Freedman 2024 用 probe penalty 成功降低了 sycophancy），且 ACT baseline 的 seed 2 验证未完成，削弱了核心对比的说服力。

## 官方维度打分（来自 ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 方法论基本可靠，诊断链设计合理，但 ACT seed 2 未完成（仅 3/16 checkpoints）导致正面 baseline 的证据不足；仅在 Qwen3-8B 上做 RL 训练，未在第二个模型上复现训练失败 |
| Excitement | 3.0/5 | Probe trap 及 behavioral-before-distributional collapse 发现有实际价值；但 "discriminability ≠ utility" 在 reward hacking 文献（Gao et al. 2023, Skalse et al. 2022）中已有类似论述，且 Papadatos & Freedman (2024) 展示了 probe-based 方法可以成功降低 sycophancy，削弱了本文 "representation detection 不能用于 reward" 的一般性 |
| Reproducibility | 3.0/5 | 关键实验设置有描述（LoRA rank=64, α=128, DeepSpeed ZeRO-2），但 181 对训练数据的构造细节、GRPO 超参数（group size、KL coefficient）、评估数据集规模与来源未充分说明 |
| Reviewer Confidence | 4/5 | 熟悉 representation engineering、RLHF、sycophancy 相关文献 |
| Overall Assessment | 3.0 | Findings 水平。核心 insight 有价值但需要补充与成功案例的对比分析、修复引用质量问题、完成 baseline 验证 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] 遗漏直接相关的成功案例：Papadatos & Freedman (2024)
- 具体位置：Section 7 (Related Work) 全部段落，以及 Section 6 (Analysis) 的 "unified root cause" 讨论
- 问题：arXiv 2412.00967 "Linear Probe Penalties Reduce LLM Sycophancy" 使用 linear probe 在 reward model 内部识别并惩罚 sycophancy 标记，实验报告在多个开源 LLM 上成功降低了 sycophantic behavior。这与本文的核心 thesis——"representation-level sycophancy detection 不能转化为有效 reward signal"——直接矛盾或至少存在紧张关系。
- 为什么影响接收：本文以 "所有 probe/direction-based reward 都失败" 作为核心贡献（C1, C3），但未讨论为何同类方法在不同框架下成功。如果 probe penalty 在 reward model 上有效而 probe reward 在 GRPO 上失败，关键区别是什么？是 intervention 位置（reward model 内部 vs. 直接 policy reward）？是 optimization 框架（PPO vs. GRPO）？还是 supervision granularity？这一对比分析是论文 contribution 的必要组成部分。
- 建议修改方向：在 Section 7 增加专门段落讨论 Papadatos & Freedman (2024)；在 Section 6 的 root cause 分析中解释两种方法的关键差异；如果可能，在 Discussion 中提出 testable hypothesis 解释差异原因。

**N2** [critical] references.bib 中多条引用严重不完整
- 具体位置：references.bib 全文；受影响的正文引用分布在 Sections 1-8
- 问题：至少 7 条 bib entry 存在严重格式问题：
  - `consistency2025bctact`（ACT，本文最重要的正面 baseline）：author = "Unknown"。实际作者为 Alex Irpan, Alexander Matt Turner, Mark Kurzeja, David K. Elson, Rohin Shah（Google DeepMind）。论文标题也不准确，应为 "Consistency Training Helps Stop Sycophancy and Jailbreaks"。
  - `zhang2026latentgrpo`：author = "Zhang, et al."——缺完整作者列表
  - `wang2025internal`：author = "Wang, et al."——缺完整作者列表
  - `sinii2025smallvectors`：author = "Sinii, et al."——缺完整作者列表
  - `obrien2025fewbadneurons`：author = "O'Brien, et al."——缺完整作者列表
  - `wei2024synthetic`：将 "Anthropic" 列为作者名——应为具体研究者姓名
  - `ackermann2026gradreg`：author = "Ackermann, Johannes and others"——过于模糊
- 为什么影响接收：（1）ACT 是论文唯一成功的 baseline，其引用连作者都是 "Unknown"，这在同行评审中是不可接受的引用质量；（2）大量 "et al." 式引用让审稿人无法验证引用真实性，在 ARR desk-rejection checklist 中 "hallucinated references" 是明确检查项；（3）这些不完整引用涉及论文的核心论证链。
- 建议修改方向：补全所有 bib entry 的完整作者列表、正确论文标题、准确 venue 信息。

**N3** [critical] ACT seed 2 验证未完成，正面 baseline 证据不足
- 具体位置：Table 4 脚注 ‡；Section 6 "Why SFT succeeds" 段落
- 问题：Table 4 显示 ACT seed 2 仅评估了 3/16 checkpoints，标注为 "ongoing"。论文的核心对比是 "GRPO 全部失败（4/25 checkpoints 超过 vanilla）vs. ACT 成功（seed 1: 16/16 超过 vanilla）"。ACT 的成功仅基于 n=1 seed 的完整评估。
- 为什么影响接收：Fisher exact test (p < 0.0001) 使用的是 seed 1 的 16/16 vs. GRPO 的 4/25，但如果 ACT seed 2 最终表现不稳定（如仅 8/16 超过 vanilla），统计论证将大幅削弱。在 n=1 的基础上声称 "ACT succeeds" 并将其作为 supervision density 论点的支柱，证据标准不够。
- 建议修改方向：（1）在提交前完成 seed 2 的全部 16 个 checkpoint 评估；（2）如果无法完成，在 Limitations 中显式标注这一不足，并将 ACT 的成功定性为 "preliminary evidence" 而非确定结论。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] 未讨论 DPO/KTO 等 preference-based RL 替代方案
- 具体位置：Section 2.2 (Reward Formulations)；Section 6 (Analysis)；Section 7 (Related Work)
- 问题：论文仅测试 GRPO 作为 RL 框架，结论中使用 "RL rewards" 的泛化表述。DPO/KTO 基于 preference pair 而非 scalar reward，绕过了论文指出的 "单一标量无法传达 warranted vs. unwarranted 区分" 的核心问题。论文既未讨论为何选择 GRPO 而非 DPO/KTO，也未分析 "discriminability ≠ utility" 论点是否同样适用于 preference-based 方法。
- 建议：在 Section 7 或 Section 6 讨论 preference-based 方法是否可能绕过 scalar reward 的局限性；如果认为同样适用，给出论证；标题和结论中考虑将 "RL Rewards" 限定为 "GRPO Rewards" 或 "scalar RL rewards"。

**W2** [warning] Process Reward Models 讨论不足
- 具体位置：Section 6 "Future directions" 段落（仅 1 句提及）
- 问题：论文核心发现是 "sparse per-completion reward fails, dense per-token SFT succeeds"。Process reward models（per-step rewards）是这两者之间的自然中间方案。SMART (arXiv 2509.16742) 已使用 per-step process rewards + MCTS 进行 sycophancy mitigation 并报告成功。这个中间方案的缺失使得论文的 supervision density 论点不够完整。
- 建议：增加对 process reward models 的讨论，特别是引用 SMART 等具体工作；分析 per-step reward 是否可能在不需要 full SFT 的情况下提供足够的 supervision density。

**W3** [warning] Conclusion 的 broader lesson 存在 overclaiming
- 具体位置：Section 8 最后一段——"The broader lesson extends beyond sycophancy: representation geometry that reliably detects a behavior is not automatically suitable for optimizing against it. Any alignment effort that converts a detection probe into a reward signal must verify..."
- 问题：这一一般性声明仅基于 sycophancy 一个 case。论文在 Section 7 中提到 reasoning faithfulness 和 safety directions 的 probe-based RL 是成功的（引用 zhang2026latentgrpo），这恰好说明 "discriminability ≠ utility" 不是普遍规律，而是取决于 target behavior 与其 complement 是否共享 geometric direction。结论中的表述将这一 conditional insight 过度泛化了。
- 建议：将 "any alignment effort" 修改为条件化表述，如 "alignment efforts that convert a detection probe into a reward signal should first verify whether the target behavior and its valid counterpart are geometrically separable along the relevant direction"；明确标注这是从 sycophancy case 推广的 hypothesis 而非已证明的普遍规律。

**W4** [warning] 仅在单一模型上做 RL 训练
- 具体位置：Section 2 (Experimental Framework)；Limitations
- 问题：所有 GRPO 和 ACT 训练实验仅在 Qwen3-8B 上进行。虽然 d_syc 的 discriminability 在 Llama-3-8B 上得到验证（Table 1），但 RL 训练失败和 ACT 成功是否在不同架构上可复现未被测试。Limitations 中提到 compute 约束（~200 H100-equivalent hours），但 C1 的 claim "Every tested GRPO formulation fails" 在严格意义上仅适用于 Qwen3-8B。
- 建议：在 C1 和 Conclusion 中明确限定模型范围；在 Limitations 中更详细讨论跨模型泛化的不确定性。

**W5** [warning] 181 对训练数据规模偏小
- 具体位置：Section 2.1 (Direction Extraction)
- 问题：d_syc 从 181 paired examples（362 activations）中提取。虽然 CV AUROC 达到 0.827，但这个规模对于构造用于 RL 训练的 reward signal 是否足够未被讨论。更大的训练集是否可能产生更鲁棒的 direction，从而缓解 cosine gap 过窄的问题（Section 4 中 gap 仅 0.098）？
- 建议：讨论数据规模对 d_syc 质量和 reward gap 的可能影响；如果有更大数据集的实验结果或分析，应予以报告。

---

## 小问题（不影响接收）

- Section 2.5 Eq. (2)：SYCONSCORE 定义为 harmonic mean，但分母应为 "ToF + NoF" 而非可能的笔误——请确认 LaTeX 源码中的公式与正文描述一致
- Table 4 中 ACT seed 2 行使用斜体 "ongoing" 文字——应补充预计完成时间或在 camera-ready 前更新
- Figure 1 caption 中 "layers 16–31 only" 对 Llama-3-8B 的解释不够清晰——为何仅展示部分层？
- Section 7 (Related Work) 约 1 页篇幅，对于做出广泛方法论声明的论文偏薄——考虑扩充对 representation-guided RL 和 sycophancy mitigation 的讨论
- 论文标题使用 "RL Rewards" 但仅测试了 GRPO——标题可能过度泛化

---

## 主要优势

1. **系统性诊断链设计优秀**：Section 4 的 F1a→F1b→F1c→F1d 递进式消除平凡解释的结构清晰有力，每个 variant 解决前一个的失败模式但暴露更深层问题——这是 negative result 论文的典范写法。

2. **Probe trap 发现有独立价值**（Section 5, Table 3, Figure 2）：behavioral death ($\text{ToF}=0$ at step 500) 先于 distributional collapse（entropy 到 step ~1840 才下降）1,300 步的发现，对 RL alignment 社区有实用警示——entropy-based early stopping 无法检测这类失败。

3. **Cross-model validation**：d_syc discriminability 在 Qwen3-8B 和 Llama-3-8B 上均得到验证（Table 1），且 evidence-strength gradient 定性一致，增强了 representation engineering 发现的可信度。

4. **清晰的写作和可视化**：论文结构紧凑，Figure 2（probe trap trajectory）和 Figure 3（SYCONSCORE trajectories）直观展示了失败模式，Table 4 的全方法对比一目了然。

5. **Stubbornness Taxonomy**（Appendix A）：对 probe-trained responses 的 100-sample 定性分析（sycophantic stubbornness 24%, deliberation traps 29%, evidence-graded hedging）提供了有价值的 failure mode 分类。

---

## Questions for Authors

1. 如何解释 Papadatos & Freedman (2024) 使用 probe penalty 在 reward model 上成功降低 sycophancy，而本文的 probe-based GRPO reward 全部失败？关键差异是 intervention 位置、optimization 框架，还是其他因素？

2. ACT seed 2 的完整评估预计何时完成？如果 seed 2 的表现与 seed 1 存在显著差异（例如仅 50% checkpoints 超过 vanilla），论文的结论是否需要修改？

3. 是否尝试过使用 DPO/KTO 替代 GRPO？如果 d_syc 被用于构造 preference pair 而非 scalar reward，"discriminability ≠ utility" 的论点是否仍然成立？

4. 181 paired examples 的规模是否进行过 sensitivity analysis？如果将训练集扩大到 500 或 1000 pairs，d_syc 的 cosine gap（当前仅 0.098）是否可能增大到足以支撑有效 reward？

---

## Missing References

1. **Papadatos, H. & Freedman, R. (2024).** Linear Probe Penalties Reduce LLM Sycophancy. arXiv:2412.00967. *[最关键遗漏——直接使用 probe 作为 reward signal 的成功案例]*
2. **SMART (2025).** Sycophancy Mitigation Through Reinforcement Learning with Uncertainty-Aware Adaptive Reasoning Trajectories. arXiv:2509.16742. *[per-step process rewards 用于 sycophancy mitigation]*
3. DPO (Rafailov et al., 2023) / KTO (Ethayarajh et al., 2024) 等 preference-based 替代方案——论文应讨论为何未尝试

---

## 格式合规检查

| 检查项 | 结果 | 备注 |
|--------|------|------|
| 正文 ≤ 8 页 | ✅ 合规 | Sections 1-8 (Conclusion) 结束于 p8，Limitations 从 p8 底部开始（不计入页数） |
| ACL 模板 | ✅ 合规 | 使用 `\usepackage[hyperref]{acl}` |
| 匿名性 | ✅ 合规 | author = "Anonymous"，未发现 self-citation 或 code link 泄露身份 |
| Limitations | ✅ 存在 | 覆盖 3 个点（单模型训练、ACT seed 2 未完成、binary evaluation），但应更显式提及 N1 中的文献遗漏 |
| References 格式 | ❌ 不合规 | 多条 bib entry 严重不完整（见 N2） |
| Ethical considerations | — | 未见显式伦理讨论，但论文性质不涉及人类受试者或敏感数据 |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 78 · 2026-05-22T10:03:30.298896+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "contrastive_entrain_calib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "contrastive_entrain_calib"
  }
}
```

</details>

---


### Tool result

_source line 79 · 2026-05-22T10:03:30.601254+00:00_

{"result":"# 项目 contrastive_entrain_calib 概况\n\n## 实验状态 (75 个)\n\n- **exp-003-eval-ckpt1000**: DONE (negative) — \n- **exp-003-eval-ckpt5000**: DONE (negative) — \n- **exp-009**: DONE (negative) — \n- **exp-012**: DONE (success) — \n- **exp-002v3**: DONE (negative) — \n- **exp-008v3**: DONE (negative) — \n- **exp002v2-recalib**: DONE (negative) — \n- **exp-003-s2**: RUNNING — \n- **exp-016**: DONE (negative) — \n- **exp-014**: DONE (killed) — \n- **vanilla-baseline**: DONE (success) — \n- **exp-002v2**: DONE (killed) — \n- **exp-002**: DONE (killed) — \n- **exp-008**: DONE (killed) — \n- **exp-001**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-22\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| exp-004-s2-eval-ckpt2000 | Eval exp-004-s2 (ACT seed 2) checkpoint-2000 with D027 unified preset. Seed 2 trajectory: 500=0.223, 1000=0.256, 1500=0.214. Seed 1 ckpt-2000=0.255 (peak before dip). Does seed 2 recover from ckpt-1500 dip or continue declining? | — | — | — |\n| exp-004-s2 | ACT (SFT) seed 2 训练：验证 ACT 跨 seed 稳定性。Seed 1 (exp-004) 16/16 checkpoints > vanilla (0.170→0.301)。如果 seed 2 也展现类似 trajectory，则堵住 Reviewer \"ACT 只有 1 个 seed\" 攻击面。配置与 exp-004 完全相同，仅 seed=42→43。 | — | — | — |\n| exp-003-s2 | R3-only GRPO baseline (seed 2): training with only the external DeBERTa reward (r3_weight=1.0, r1=r2=0) provides a lower bound for ablation, isolating the contribution of contrastive direction-based rewards (R1+R2). Seed 2 (seed=43) verifies reproducibility of seed 1 results. | — | — | — |\n\n## 待处理\n- exp-003-s2-eval-ckpt3000: Eval exp-003-s2 (R3-only seed 2) checkpoint-3000 with D027 unified preset. Cross-seed reproducibility: compare with seed 1 ckpt-3000 (SYCONScore=0.095) for exact step match.（排队等待 GPU）\n- exp-003-s2-eval-ckpt2500: Eval exp-003-s2 (R3-only seed 2) checkpoint-2500 with D027 unified preset. Cross-seed reproducibility: compare with seed 1 ckpt-3000 (SYCONScore=0.095) for tra
…[truncated 1466 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 302
}
```

</details>

---


### Assistant

_source line 80 · 2026-05-22T10:03:40.283474+00:00_

**上下文恢复完成。**

当前状态：Round 1 进行中。
- Reviewer 1（方法严谨性 + 实验设计 + 统计分析）：**待返回**
- Reviewer 2（新颖性 + 相关工作 + 写作 + 格式）：**已收到**，Overall 3.0 (Findings)

Reviewer 2 提出 3 个 Must-Fix（遗漏 Papadatos & Freedman 2024 成功案例、bib 严重不完整、ACT seed 2 未完成）和 5 个 Should-Fix（缺 DPO/KTO 讨论、PRM 不足、Conclusion overclaim、单模型训练、数据规模小）。

等待 Reviewer 1 返回后进入 Step 2（交叉分享）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director"
}
```

</details>

---


## Round 3

## Round 3

6 recorded events


### User

_source line 81 · 2026-05-22T10:03:41.502540+00:00_

[Reviewer 1 审稿意见]:

## Reviewer 1 — Round 1 审稿意见

**论文**: "Discriminability Without Utility: Why Sycophancy Directions Fail as RL Rewards"
**Venue**: EMNLP 2026 (ARR May 2026)
**审查侧重**: 方法严谨性 + 实验设计 + 统计分析

---

## 总体评分

**Overall**: 3.0 (Findings)
**一句话总结**: 论文揭示了表征方向可辨别性与 RL 奖励实用性之间的结构性 gap，负面结果本身有价值，但统计分析存在严重缺陷（Fisher test 独立性违反）、唯一的正面结果（ACT）仅基于单 seed、ACT vs GRPO 对比存在 supervision granularity confound，实验覆盖面不足以支撑标题中的强普遍性声明。

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3/5 | 核心失败模式分析扎实（§4-5 的 reward trap 和 stubbornness trap 刻画清晰），但关键统计检验误用、seed 数不足削弱了定量结论 |
| Excitement | 3/5 | "discriminability ≠ reward utility" 的洞察对 representation engineering + RL 交叉领域有启发，但受限于单一 RL 算法（GRPO）和单一训练模型（Qwen3-8B），普遍性存疑 |
| Reproducibility | 3/5 | LoRA rank=64、recalibration 间隔 500 步等关键参数有报告，但 w1=0.25 的选择过程、contrastive pairs 构建流程不透明 |
| Reviewer Confidence | 4/5 | 熟悉 representation engineering、RLHF、sycophancy mitigation 相关工作 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] Fisher exact test 独立性假设违反
- 具体位置：§1 (p<0.0001 claim), §6 复述
- 问题：论文报告 Fisher exact test 比较 GRPO（4/25 checkpoints exceed vanilla）vs ACT seed 1（16/16），得到 p<0.0001。但同一训练 run 的 checkpoints 具有强时序相关性（consecutive checkpoints 的 SycophancyScore 高度自相关），严重违反 Fisher exact test 的独立性假设。Figure 3 清楚展示了 GRPO 两个 seed 的 SycophancyScore 呈连续振荡模式，相邻 checkpoints 之间远非独立。将 25 个非独立 checkpoints 当作 25 个独立观测，人为膨胀了有效样本量。
- 为什么影响接收：这个 p 值被用于支撑论文的核心对比结论（GRPO 系统性失败 vs ACT 成功）。如果正确处理自相关（例如用 run-level 比较：2 个 GRPO runs vs 1 个 ACT run），有效样本量只有 n=3，无法得出统计显著结论。
- 建议修改方向：(1) 改用 run-level 汇总统计（每个 run 取最优 checkpoint 的 SycophancyScore），报告 effect size 而非 p 值；(2) 如需统计检验，使用考虑时序相关的方法（如 block bootstrap）；(3) 增加 seed 数量到至少 5 个。

**N2** [critical] ACT 正面结果仅基于单个完成 seed
- 具体位置：Table 4, §6, Limitations
- 问题：ACT 是论文唯一的正面结果（SycophancyScore 0.301，约 2.25× vanilla baseline），但完整结果仅来自 seed 1。Seed 2 在投稿时仅完成 3/16 checkpoints 评估。论文 Limitations 承认 "ACT cross-seed verification is partial"，但主文中 ACT 的成功被当作已确立的事实来支撑核心论点（§6: "ACT achieves SycophancyScore = 0.301"）。
- 为什么影响接收：如果 ACT seed 2 最终表现远低于 seed 1（考虑到 GRPO 本身就展示了跨 seed 的高方差），论文的 "SFT 成功而 RL 失败" 叙事将被严重削弱。单 seed 结果不足以建立方法有效性。
- 建议修改方向：(1) 完成 seed 2 全部 16 checkpoints 评估后再提交；(2) 如果 seed 2 确认了 seed 1 的模式，提供跨 seed 的均值±std；(3) 如果 seed 2 不一致，诚实讨论并调整 claims 的强度。

**N3** [critical] ACT vs GRPO 对比存在 supervision granularity confound
- 具体位置：§2.4, §6, §8
- 问题：ACT 使用 dense per-token supervision（在 token 级别区分 valid/invalid pairs，§2.4 明确写道 "ACT operates at the token level using labeled valid/invalid pairs"），而 GRPO 使用 single scalar reward per completion。这不是一个公平的对比——ACT 的成功可能完全归因于更丰富的监督信号粒度，而非 d_syc 方向本身。论文的核心论点是 "d_syc 作为 RL reward 无用"，但 ACT 的成功并不能证明这一点，因为 ACT 不是通过 d_syc 的 RL reward 成功的，而是通过完全不同的训练范式（SFT + L2 activation loss）成功的。
- 为什么影响接收：论文标题和结论暗示 "RL 路径走不通，SFT 路径可行"，但这个二分法建立在一个不公平的对比上。如果给 GRPO 同样粒度的监督信号（例如 per-token reward），结果可能不同。
- 建议修改方向：(1) 明确承认 supervision granularity 是 ACT 成功的可能解释之一，不把 ACT 成功简单归因为 "SFT > RL"；(2) 增加一个控制实验——例如用 d_syc 的 per-token projection 作为 dense reward 给 GRPO；(3) 调整 framing，将结论限定为 "scalar d_syc reward 不足"，而非 "d_syc 作为 RL reward 失败"。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] 超参数 w1 仅测试单一值，存在 false negative 风险
- 具体位置：Table 2
- 问题：所有 F1 变体均使用 w1=0.25（d_syc reward 权重）。论文未报告是否测试过其他 w1 值（如 0.1, 0.5, 1.0）。F1a 中 d_syc/20 的 scaling factor 也未解释来源。如果 w1=0.25 恰好落在一个不良区间（过大导致 mode collapse，过小导致信号被 R3 淹没），那么 GRPO 失败可能是调参不充分的 artifact，而非 d_syc 方向本身的固有缺陷。
- 建议：(1) 报告 w1 的选择过程（grid search? 先验知识?）；(2) 至少展示 w1 在 {0.05, 0.1, 0.25, 0.5, 1.0} 范围内的 sensitivity analysis；(3) 如果确实只跑了 w1=0.25，在 Limitations 中明确承认这一点。

**W2** [warning] 标题声明过于宽泛——仅测试 GRPO 一种 RL 算法
- 具体位置：标题、§1、§8
- 问题：标题 "Why Sycophancy Directions Fail as RL Rewards" 暗示 d_syc 方向在所有 RL 框架下都失败。但实验仅测试了 GRPO（一种特定的 on-policy RL 算法）。DPO、KTO、PPO 等其他 RL 方法可能有不同表现。特别是 DPO 直接在 pair-wise preference 上优化，可能比 GRPO 的 scalar reward 更好地利用 d_syc 方向信息。
- 建议：(1) 标题改为 "Why Sycophancy Directions Fail as GRPO Rewards" 或 "...as Scalar RL Rewards"；(2) 或增加至少一种 offline RL 方法（如 DPO）的实验。

**W3** [warning] AUROC 置信区间报告不规范
- 具体位置：§3, Table 1
- 问题：AUROC 0.827±0.028（Qwen3-8B）和 0.779±0.019（Llama-3-8B）来自 5-fold CV。±值是 5 个 fold 的标准差，但从仅 5 个值估计标准差本身有高不确定性。这不是一个正式的置信区间。每个 fold 的测试集仅约 36 pairs，fold 间方差的估计值不稳定。
- 建议：(1) 使用 bootstrap（在 181 pairs 上重采样 1000+ 次）计算 95% CI；(2) 或使用 Nadeau & Bengio (2003) 的 corrected resampled t-test for CV；(3) 报告每个 fold 的 AUROC 以展示分布。

**W4** [warning] Contrastive pairs 构建方法细节不足
- 具体位置：§2.1
- 问题：论文称 contrastive pairs 是 "style-controlled to match hedging, politeness, and length"，但未描述具体的控制方法。是人工编写？LLM 生成后人工筛选？模板化？是否有 inter-annotator agreement？如果控制不充分，d_syc 可能捕获的是 style difference 而非 sycophancy，这将从根本上影响后续所有实验的解释。
- 建议：(1) 详细描述 pair 构建流程（数据来源、生成方法、质量控制）；(2) 报告 pair 之间在控制维度上的统计差异（如长度差异的 t-test）；(3) 提供若干示例 pair。

**W5** [warning] RL 训练仅在 Qwen3-8B 上进行
- 具体位置：§2, Table 4
- 问题：GRPO 和 ACT 训练均仅在 Qwen3-8B 上进行。Llama-3-8B 只用于 §3 的 direction discriminability 验证（Table 1），未做任何 RL 训练。GRPO 的失败可能是 Qwen3-8B 特定的——例如该模型的 reward landscape 结构或 LoRA 适配特性可能放大了 d_syc 的缺陷。
- 建议：至少在 Llama-3-8B 上复现一个代表性的 GRPO 配置（如 F1a）以验证失败模式的模型无关性。

**W6** [warning] Cross-seed 分析仅 2 个 seed，不足以支撑可复现性声明
- 具体位置：§6, Figure 3
- 问题：GRPO 仅用 2 个 seed，论文称 "Both seeds oscillate with similar amplitude but stochastic crash timing"。n=2 只能说明两次观察到了类似模式，不能建立统计意义上的可复现性。Figure 3 中两个 seed 的 crash 时间差异显著（seed 1 在 ~checkpoint 6500, seed 2 在 ~checkpoint 8000 附近），所谓"相似"的判断是定性的而非定量的。
- 建议：(1) 增加到至少 3-5 个 seed；(2) 报告 seed 间 SycophancyScore 轨迹的定量相似性度量。

---

## 小问题（不影响接收）

- **NLI flip classifier 未报告准确率**：§2.5 提到 flip classification 使用 NLI（LoRA rank=64, n=128），但未报告该分类器的准确率或与人工标注的一致性。如果分类器本身不准确，ToF/NoF 指标的可靠性存疑。
- **SycophancyScore 等权 harmonic mean 未讨论**：Equation 2 定义 SycophancyScore = 2·ToF·NoF/(ToF+NoF)，隐含假设 ToF 和 NoF 同等重要。在实际应用中，抵抗无效压力（NoF）可能比接受有效修正（ToF）更重要（或反之），但论文未讨论这一设计选择的影响。
- **"Unknown (2025)" 引用**：§2.5 引用 "Unknown (2025)" 作为 NLI flip classification 的方法来源，这似乎是 anonymization 导致的，但在正式提交中应确保引用可追溯。
- **Appendix A (Stubbornness Taxonomy)** 的定量分析基于 100 个 probe-trained responses（exp-008v3, step 2000），样本量偏小，百分比（24% sycophantic stubbornness, 29% deliberation traps 等）的置信区间较宽。

---

## 主要优势

1. **重要且有价值的负面结果**：系统性测试 6 种 d_syc-based GRPO 配置全部失败，对 representation engineering + RL 领域有警示意义。
2. **失败模式分析深入**：§4 (cosine R1 structural failure) 和 §5 (probe reward trap) 对失败的根因分析细致——识别出 valid revision 和 sycophantic capitulation 在同一方向上的投影混淆（cosine projection conflates belief change direction regardless of warrant），以及 binary probe 的 gradient gaming（策略在 ~30 步内发现 sycophancy cluster 并 maximize R1）。
3. **Conceptual insight 有深度**：§6 提出 "discriminability is necessary but not sufficient for reward utility"，并给出了清晰的机制解释——d_syc 编码的是 belief change 的方向而非其是否有 warrant，因此无法区分应该奖励和应该惩罚的行为。
4. **Cross-model 方向验证**：Table 1 展示 d_syc 在 Qwen3-8B 和 Llama-3-8B 两个架构上都具有 discriminability，且 best-layer 位置合理（上层 1/3），增强了方向提取方法的可信度。
5. **Behavioral failure taxonomy**（Appendix A）提供了定性洞察——sycophantic stubbornness、deliberation traps、evidence-graded hedging 三种模式的识别有助于理解 RL 训练中的 reward hacking 行为。

---

## 对 Director 指定审查重点的逐项回应

### 1. Direction Extraction 方法论
- 181 对 contrastive pairs 对于提取单一线性方向来说是可接受的样本量（与 Zou et al. 2023 等工作一致），但 **style-controlled 的方法细节严重缺失**（W4）。
- 5-fold CV 选层方法原则上 sound，但从 36 层（Qwen3-8B）中选最优层存在 selection bias 风险，即使使用了 CV。AUROC CI 报告不规范（W3）。
- Evidence-strength 分层（weak/medium/strong）是一个加分设计，Table 1 中 weak subset AUROC 低于整体（0.675 vs 0.827）的发现有信息量。

### 2. GRPO 实验设计
- 6 个配置（F1a-F1d + F2 + F3）+ R3-only 的覆盖面合理，但 **w1 仅测试一个值**（W1）是重大缺陷。
- 各 formulation 的设计逻辑清晰（从 unbounded cosine 到 bounded sigmoid，从 continuous 到 discrete），展示了系统性探索。
- **缺少非 GRPO 的 RL 方法**（W2），特别是 DPO，它天然适合 pair-wise 设置。

### 3. 统计声明
- **Fisher exact test 严重误用**（N1），这是本文最大的统计问题。
- AUROC CI 应改用 bootstrap（W3）。
- **2 个 seed 完全不足以支撑可复现性声明**（W6）。
- 关于 Welch t-test for R3 reward saturation：论文中未找到明确使用 Welch t-test 的描述，如果在 supplementary material 中使用了，应在主文中注明。

### 4. ACT 比较公平性
- **ACT vs GRPO 的对比是本文最大的方法论问题之一**（N3）。Supervision granularity 的差异完全混淆了结论。
- ACT seed 2 仅 3/16 checkpoints（N2），使得唯一正面结果基于单 seed，可靠性不足。
- **缺少 DPO/KTO 等其他 RL baseline**（W2），限制了负面结论的普遍性。

### 5. Reproducibility
- LoRA rank=64 有报告，recalibration 间隔 500 步有报告。但 learning rate、batch size、GRPO 的 group size 等核心训练超参数在主文中未找到（可能在附录，但提交 PDF 附录仅有 Stubbornness Taxonomy）。
- 仅在 Qwen3-8B 上做 RL 训练（W5），Llama-3-8B 只做了 direction discriminability 验证。

### 6. Evaluation 指标
- SycophancyScore 的 harmonic mean 设计合理但 **等权假设未讨论**。
- NLI-based flip classification 的可靠性 **未用人工标注验证**，这是评估流水线的潜在薄弱环节。


---

[Reviewer 2 审稿结果]:
Round 1 审稿完成，已提交至 Review Director。

核心判断：**Overall 3.0 (Findings)**。论文系统性地展示了 d_syc 无法转化为有效 GRPO reward，probe trap 发现有独立价值，但存在三个 critical 问题：

1. **遗漏 Papadatos & Freedman (2024)**——该工作用 probe penalty 成功降低 sycophancy，直接挑战本文 "probe-based reward 不可行" 的核心 thesis
2. **references.bib 严重不完整**——ACT（唯一成功 baseline）的引用作者为 "Unknown"，另有 6 条 entry 使用 "et al." 或错误作者名
3. **ACT seed 2 仅完成 3/16 checkpoints**——正面 baseline 的可复现性证据不足

---

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

核心发现：

- **Overall 3.0 (Findings)**——负面结果有价值但证据不足以支撑标题中的强普遍性声明
- **3 个 Must-Fix**：Fisher exact test 将非独立 checkpoints 当独立样本（p<0.0001 不可信）、ACT 正面结果仅单 seed 完成、ACT vs GRPO 存在 supervision granularity confound
- **6 个 Should-Fix**：w1 仅测试单一值（false negative 风险）、标题 overclaim（仅测 GRPO）、AUROC CI 不规范、contrastive pairs 构建细节缺失、仅 Qwen3-8B 做 RL 训练、仅 2 seeds

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 82 · 2026-05-22T10:04:25.911997+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "contrastive_entrain_calib",
  "text": "## 交叉分享 — Reviewer 2 的完整审稿意见\n\n请逐条回应以下 Reviewer 2 的意见。对每条使用 **[AGREE]** 并说明理由，或 **[REBUT]** 并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n### Reviewer 2 Overall: 3.0 (Findings)\n\n### Reviewer 2 Must-Fix 问题\n\n**R2-N1** [critical] 遗漏直接相关的成功案例：Papadatos &amp; Freedman (2024)\n- arXiv 2412.00967 \"Linear Probe Penalties Reduce LLM Sycophancy\" 使用 linear probe 在 reward model 内部识别并惩罚 sycophancy 标记，实验报告在多个开源 LLM 上成功降低了 sycophantic behavior。这与本文的核心 thesis——\"representation-level sycophancy detection 不能转化为有效 reward signal\"——直接矛盾或至少存在紧张关系。\n- 论文未讨论为何同类方法在不同框架下成功。如果 probe penalty 在 reward model 上有效而 probe reward 在 GRPO 上失败，关键区别是什么？\n\n**R2-N2** [critical] references.bib 中多条引用严重不完整\n- consistency2025bctact（ACT）：author = \"Unknown\"\n- zhang2026latentgrpo, wang2025internal, sinii2025smallvectors, obrien2025fewbadneurons：均为 \"et al.\"\n- wei2024synthetic：将 \"Anthropic\" 列为作者名\n- ackermann2026gradreg：\"Ackermann, Johannes and others\"\n- ACT 是论文唯一成功 baseline，其引用连作者都是 \"Unknown\"。\n\n**R2-N3** [critical] ACT seed 2 验证未完成，正面 baseline 证据不足\n- ACT seed 2 仅评估 3/16 checkpoints，论文核心对比（4/25 vs 16/16）仅基于 seed 1 完整评估。\n\n### Reviewer 2 Should-Fix 问题\n\n**R2-W1** [warning] 未讨论 DPO/KTO 等 preference-based RL 替代方案\n- DPO/KTO 基于 preference pair 而非 scalar reward，可能绕过 \"单一标量无法区分 warranted vs unwarranted\" 的问题。标题使用 \"RL Rewards\" 但仅测试 GRPO。\n\n**R2-W2** [warning] Process Reward Models 讨论不足\n- SMART (arXiv 2509.16742) 已使用 per-step process rewards + MCTS 进行 sycophancy mitigation 并报告成功。论文仅 1 句提及 future directions。\n\n**R2-W3** [warning] Conclusion 的 broader lesson 存在 overclaiming\n- \"any alignment effort\" 的一般性声明仅基于 sycophancy 一个 case，且论文自己承认 reasoning/safety directions 的 probe-based RL 是成功的。\n\n**R2-W4** [warning] 仅在单一模型上做 RL 训练\n- 所有 GRPO 和 ACT 训练仅在 Qwen3-8B 上进行，C1 的 \"Every tested GRPO formulation fails\" 严格意义上仅适用于 Qwen3-8B。\n\n**R2-W5** [warning] 181 对训练数据规模偏小\n- 更大训练集是否可能产生更鲁棒的 direction，缓解 cosine gap 过窄（仅 0.098）的问题？\n\n### Reviewer 2 Missing References\n1. Papadatos &amp; Freedman (2024) — Linear Probe Penalties Reduce LLM Sycophancy (arXiv 2412.00967)\n2. SMART (2025) — per-step process rewards 用于 sycophancy mitigation (arXiv 2509.16742)\n3. DPO (Rafailov et al., 2023) / KTO (Ethayarajh et al., 2024)\n\n---\n\n请对以上每条给出 [AGREE] 或 [REBUT]，并说明理由。特别关注：\n1. R2-N1 关于 Papadatos &amp; Freedman (2024) 的遗漏——你是否认为这确实是一个 critical gap？\n2. R2-N2 关于引用质量——从方法严谨性角度，这是否影响论文可信度？\n3. 你的 N1（Fisher test）和 R2 的 N1（missing reference）哪个对论文接收影响更大？"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "contrastive_entrain_calib",
    "text": "## 交叉分享 — Reviewer 2 的完整审稿意见\n\n请逐条回应以下 Reviewer 2 的意见。对每条使用 **[AGREE]** 并说明理由，或 **[REBUT]** 并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n### Reviewer 2 Overall: 3.0 (Findings)\n\n### Reviewer 2 Must-Fix 问题\n\n**R2-N1** [critical] 遗漏直接相关的成功案例：Papadatos &amp; Freedman (2024)\n- arXiv 2412.00967 \"Linear Probe Penalties Reduce LLM Sycophancy\" 使用 linear probe 在 reward model 内部识别并惩罚 sycophancy 标记，实验报告在多个开源 LLM 上成功降低了 sycophantic behavior。这与本文的核心 thesis——\"representation-level sycophancy detection 不能转化为有效 reward signal\"——直接矛盾或至少存在紧张关系。\n- 论文未讨论为何同类方法在不同框架下成功。如果 probe penalty 在 reward model 上有效而 probe reward 在 GRPO 上失败，关键区别是什么？\n\n**R2-N2** [critical] references.bib 中多条引用严重不完整\n- consistency2025bctact（ACT）：author = \"Unknown\"\n- zhang2026latentgrpo, wang2025internal, sinii2025smallvectors, obrien2025fewbadneurons：均为 \"et al.\"\n- wei2024synthetic：将 \"Anthropic\" 列为作者名\n- ackermann2026gradreg：\"Ackermann, Johannes and others\"\n- ACT 是论文唯一成功 baseline，其引用连作者都是 \"Unknown\"。\n\n**R2-N3** [critical] ACT seed 2 验证未完成，正面 baseline 证据不足\n- ACT seed 2 仅评估 3/16 checkpoints，论文核心对比（4/25 vs 16/16）仅基于 seed 1 完整评估。\n\n### Reviewer 2 Should-Fix 问题\n\n**R2-W1** [warning] 未讨论 DPO/KTO 等 preference-based RL 替代方案\n- DPO/KTO 基于 preference pair 而非 scalar reward，可能绕过 \"单一标量无法区分 warranted vs unwarranted\" 的问题。标题使用 \"RL Rewards\" 但仅测试 GRPO。\n\n**R2-W2** [warning] Process Reward Models 讨论不足\n- SMART (arXiv 2509.16742) 已使用 per-step process rewards + MCTS 进行 sycophancy mitigation 并报告成功。论文仅 1 句提及 future directions。\n\n**R2-W3** [warning] Conclusion 的 broader lesson 存在 overclaiming\n- \"any alignment effort\" 的一般性声明仅基于 sycophancy 一个 case，且论文自己承认 reasoning/safety directions 的 probe-based RL 是成功的。\n\n**R2-W4** [warning] 仅在单一模型上做 RL 训练\n- 所有 GRPO 和 ACT 训练仅在 Qwen3-8B 上进行，C1 的 \"Every tested GRPO formulation fails\" 严格意义上仅适用于 Qwen3-8B。\n\n**R2-W5** [warning] 181 对训练数据规模偏小\n- 更大训练集是否可能产生更鲁棒的 direction，缓解 cosine gap 过窄（仅 0.098）的问题？\n\n### Reviewer 2 Missing References\n1. Papadatos &amp; Freedman (2024) — Linear Probe Penalties Reduce LLM Sycophancy (arXiv 2412.00967)\n2. SMART (2025) — per-step process rewards 用于 sycophancy mitigation (arXiv 2509.16742)\n3. DPO (Rafailov et al., 2023) / KTO (Ethayarajh et al., 2024)\n\n---\n\n请对以上每条给出 [AGREE] 或 [REBUT]，并说明理由。特别关注：\n1. R2-N1 关于 Papadatos &amp; Freedman (2024) 的遗漏——你是否认为这确实是一个 critical gap？\n2. R2-N2 关于引用质量——从方法严谨性角度，这是否影响论文可信度？\n3. 你的 N1（Fisher test）和 R2 的 N1（missing reference）哪个对论文接收影响更大？"
  }
}
```

</details>

---


### Tool result

_source line 83 · 2026-05-22T10:04:49.974163+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 24062
}
```

</details>

---


### Tool call

_source line 84 · 2026-05-22T10:04:50.175537+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "contrastive_entrain_calib",
  "text": "## 交叉分享 — Reviewer 1 的完整审稿意见\n\n请逐条回应以下 Reviewer 1 的意见。对每条使用 **[AGREE]** 并说明理由，或 **[REBUT]** 并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n### Reviewer 1 Overall: 3.0 (Findings)\n\n### Reviewer 1 Must-Fix 问题\n\n**R1-N1** [critical] Fisher exact test 独立性假设违反\n- 论文报告 Fisher exact test 比较 GRPO（4/25 checkpoints exceed vanilla）vs ACT seed 1（16/16），得到 p&lt;0.0001。但同一训练 run 的 checkpoints 具有强时序相关性，严重违反 Fisher exact test 的独立性假设。Figure 3 清楚展示 GRPO 两个 seed 的 SycophancyScore 呈连续振荡模式。\n- 如果正确处理自相关（run-level 比较：2 个 GRPO runs vs 1 个 ACT run），有效样本量只有 n=3，无法得出统计显著结论。\n- 建议改用 run-level 汇总统计、block bootstrap、或增加 seed 数量到至少 5 个。\n\n**R1-N2** [critical] ACT 正面结果仅基于单个完成 seed\n- 与你的 N3 相似。ACT seed 2 仅完成 3/16 checkpoints，唯一正面结果基于 n=1 seed。\n\n**R1-N3** [critical] ACT vs GRPO 对比存在 supervision granularity confound\n- ACT 使用 dense per-token supervision，GRPO 使用 single scalar reward per completion。ACT 的成功可能完全归因于更丰富的监督信号粒度，而非 d_syc 方向本身的问题。\n- 论文的 \"RL 路径走不通，SFT 路径可行\" 二分法建立在不公平对比上。如果给 GRPO 同样粒度的监督信号（per-token reward），结果可能不同。\n- 建议：增加控制实验（per-token d_syc projection 作为 dense reward 给 GRPO），或调整 framing 限定为 \"scalar d_syc reward 不足\"。\n\n### Reviewer 1 Should-Fix 问题\n\n**R1-W1** [warning] 超参数 w1 仅测试单一值（0.25），存在 false negative 风险\n- 未报告是否测试过其他 w1 值。F1a 中 d_syc/20 的 scaling factor 未解释来源。GRPO 失败可能是调参不充分的 artifact。\n\n**R1-W2** [warning] 标题声明过于宽泛——仅测试 GRPO 一种 RL 算法\n- 与你的 W1 类似。标题用 \"RL Rewards\" 但仅测 GRPO。DPO 天然适合 pair-wise 设置。\n\n**R1-W3** [warning] AUROC 置信区间报告不规范\n- ±值来自 5-fold CV 的 5 个值的标准差，不是正式 CI。每个 fold 仅约 36 pairs。建议改用 bootstrap。\n\n**R1-W4** [warning] Contrastive pairs 构建方法细节不足\n- \"style-controlled\" 的具体方法未描述。是人工编写？LLM 生成？模板化？无 inter-annotator agreement 报告。\n\n**R1-W5** [warning] RL 训练仅在 Qwen3-8B 上进行\n- 与你的 W4 一致。\n\n**R1-W6** [warning] Cross-seed 分析仅 2 个 seed\n- n=2 不足以建立统计意义上的可复现性。两个 seed 的 crash 时间差异显著。\n\n### Reviewer 1 小问题\n- NLI flip classifier 未报告准确率\n- SycophancyScore 等权 harmonic mean 未讨论设计选择\n- \"Unknown (2025)\" 引用问题\n- Appendix A 定量分析样本量偏小（100 responses）\n\n---\n\n请对以上每条给出 [AGREE] 或 [REBUT]，并说明理由。特别关注：\n1. R1-N1 关于 Fisher exact test——你是否认同这是一个 critical 统计问题？从你的写作/格式角度看，这是否比引用问题更严重？\n2. R1-N3 关于 supervision granularity confound——你是否认为这削弱了论文的 SFT vs RL 叙事？\n3. 对于你发现的 R2-N1（Papadatos &amp; Freedman 2024 遗漏），Reviewer 1 未提及——你是否仍坚持这是 critical？"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "contrastive_entrain_calib",
    "text": "## 交叉分享 — Reviewer 1 的完整审稿意见\n\n请逐条回应以下 Reviewer 1 的意见。对每条使用 **[AGREE]** 并说明理由，或 **[REBUT]** 并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n### Reviewer 1 Overall: 3.0 (Findings)\n\n### Reviewer 1 Must-Fix 问题\n\n**R1-N1** [critical] Fisher exact test 独立性假设违反\n- 论文报告 Fisher exact test 比较 GRPO（4/25 checkpoints exceed vanilla）vs ACT seed 1（16/16），得到 p&lt;0.0001。但同一训练 run 的 checkpoints 具有强时序相关性，严重违反 Fisher exact test 的独立性假设。Figure 3 清楚展示 GRPO 两个 seed 的 SycophancyScore 呈连续振荡模式。\n- 如果正确处理自相关（run-level 比较：2 个 GRPO runs vs 1 个 ACT run），有效样本量只有 n=3，无法得出统计显著结论。\n- 建议改用 run-level 汇总统计、block bootstrap、或增加 seed 数量到至少 5 个。\n\n**R1-N2** [critical] ACT 正面结果仅基于单个完成 seed\n- 与你的 N3 相似。ACT seed 2 仅完成 3/16 checkpoints，唯一正面结果基于 n=1 seed。\n\n**R1-N3** [critical] ACT vs GRPO 对比存在 supervision granularity confound\n- ACT 使用 dense per-token supervision，GRPO 使用 single scalar reward per completion。ACT 的成功可能完全归因于更丰富的监督信号粒度，而非 d_syc 方向本身的问题。\n- 论文的 \"RL 路径走不通，SFT 路径可行\" 二分法建立在不公平对比上。如果给 GRPO 同样粒度的监督信号（per-token reward），结果可能不同。\n- 建议：增加控制实验（per-token d_syc projection 作为 dense reward 给 GRPO），或调整 framing 限定为 \"scalar d_syc reward 不足\"。\n\n### Reviewer 1 Should-Fix 问题\n\n**R1-W1** [warning] 超参数 w1 仅测试单一值（0.25），存在 false negative 风险\n- 未报告是否测试过其他 w1 值。F1a 中 d_syc/20 的 scaling factor 未解释来源。GRPO 失败可能是调参不充分的 artifact。\n\n**R1-W2** [warning] 标题声明过于宽泛——仅测试 GRPO 一种 RL 算法\n- 与你的 W1 类似。标题用 \"RL Rewards\" 但仅测 GRPO。DPO 天然适合 pair-wise 设置。\n\n**R1-W3** [warning] AUROC 置信区间报告不规范\n- ±值来自 5-fold CV 的 5 个值的标准差，不是正式 CI。每个 fold 仅约 36 pairs。建议改用 bootstrap。\n\n**R1-W4** [warning] Contrastive pairs 构建方法细节不足\n- \"style-controlled\" 的具体方法未描述。是人工编写？LLM 生成？模板化？无 inter-annotator agreement 报告。\n\n**R1-W5** [warning] RL 训练仅在 Qwen3-8B 上进行\n- 与你的 W4 一致。\n\n**R1-W6** [warning] Cross-seed 分析仅 2 个 seed\n- n=2 不足以建立统计意义上的可复现性。两个 seed 的 crash 时间差异显著。\n\n### Reviewer 1 小问题\n- NLI flip classifier 未报告准确率\n- SycophancyScore 等权 harmonic mean 未讨论设计选择\n- \"Unknown (2025)\" 引用问题\n- Appendix A 定量分析样本量偏小（100 responses）\n\n---\n\n请对以上每条给出 [AGREE] 或 [REBUT]，并说明理由。特别关注：\n1. R1-N1 关于 Fisher exact test——你是否认同这是一个 critical 统计问题？从你的写作/格式角度看，这是否比引用问题更严重？\n2. R1-N3 关于 supervision granularity confound——你是否认为这削弱了论文的 SFT vs RL 叙事？\n3. 对于你发现的 R2-N1（Papadatos &amp; Freedman 2024 遗漏），Reviewer 1 未提及——你是否仍坚持这是 critical？"
  }
}
```

</details>

---


### Tool result

_source line 85 · 2026-05-22T10:04:51.725156+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1549
}
```

</details>

---


### Assistant

_source line 86 · 2026-05-22T10:04:55.911467+00:00_

交叉分享已发出。两位 Reviewer 将逐条回应对方的意见（[AGREE]/[REBUT]），等待回复后进入收敛判断。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director"
}
```

</details>

---


## Round 4

## Round 4

2 recorded events


### User

_source line 87 · 2026-05-22T10:06:34.189847+00:00_

[Reviewer 1 审稿意见]:

## Reviewer 1 — 交叉回应 Reviewer 2 意见

---

### Must-Fix 问题

**[AGREE] R2-N1: 遗漏 Papadatos & Freedman (2024) 的 probe penalty 成功案例**

同意这是一个重要遗漏，但我将其严重性评为 **must-fix 偏下限**而非 R2 认定的最高级别 critical。

理由：如果 Papadatos & Freedman (2024) 确实通过 linear probe penalty 在 reward model 内部成功降低了 sycophancy，那这与本文 §5 中 F2（binary probe）和 F3（continuous probe）作为 GRPO reward 的失败形成了直接张力。论文的核心 thesis——representation-level sycophancy detection 不能转化为有效 reward signal——需要解释为什么同类信号在不同框架下（reward model 内部 penalty vs. GRPO scalar reward）有截然不同的效果。

但我认为存在合理的区分：(1) probe penalty 作用于 reward model 的中间表征（修改 RM 自身的行为），vs. 本文将 probe 输出直接作为 policy optimization 的 reward component——前者保留了 RM 的 per-token richness，后者压缩为 per-completion scalar；(2) penalty（惩罚 sycophancy 标记）vs. reward（奖励非 sycophancy 方向）在梯度方向上可能有不对称效果。论文如果能在 §7 Related Work 中讨论这些区分，可以将其从"直接矛盾"降级为"互补视角"。

**补充**：这个遗漏也间接支持了我的 N3——如果 probe penalty 在更细粒度的 reward model 中有效，那问题可能不是 d_syc 方向本身，而是 GRPO 的 scalar reward 粒度。

---

**[AGREE] R2-N2: 引用严重不完整**

同意，且我认为比 R2 描述的更严重。

ACT 是论文唯一报告成功的 baseline（Table 4, SycophancyScore 0.301），其引用 "Unknown (2025)" 意味着读者无法追溯验证该方法的原始定义和效果。在 double-blind 审稿中，如果 "Unknown" 是因为 ACT 是作者自己的工作而进行了匿名化，那这暗示论文可能在评估自己的先前工作作为 baseline，存在潜在的公平性问题。如果不是自己的工作，那 "Unknown" 就是粗心的 bib 管理。

其他引用问题同样影响可信度：多条使用 "et al." 代替完整作者列表违反了基本的学术引用规范。将 "Anthropic" 列为 author name（wei2024synthetic）是格式错误。这些问题加在一起反映了论文在编辑质量上的系统性不足。

从方法严谨性角度：引用不完整本身不影响实验结果的有效性，但它 (1) 妨碍读者追溯验证方法来源，(2) 对 reproducibility 维度有负面影响，(3) 在审稿中会显著降低论文的专业印象。

---

**[AGREE] R2-N3: ACT seed 2 验证未完成**

完全同意，这与我的 N2 一致。ACT seed 2 仅完成 3/16 checkpoints 评估，论文核心正面结果依赖单 seed，可靠性不足。不再赘述。

---

### Should-Fix 问题

**[AGREE] R2-W1: 未讨论 DPO/KTO 等 preference-based RL**

完全同意，与我的 W2 一致。补充一点：DPO 特别值得关注，因为 d_syc 方向天然适合构造 preference pair（sycophantic response vs. non-sycophantic response），而 DPO 直接在 pair-wise preference 上优化，可能绕过 GRPO scalar reward 的 "cosine projection conflates valid revision with capitulation" 问题（我的 N3 中指出的 supervision granularity confound）。标题声称 "RL Rewards" 失败但仅测试了 GRPO 一种算法，确实 overclaiming。

---

**[AGREE] R2-W2: Process Reward Models 讨论不足**

同意，但我将其严重性降为 **minor-to-warning** 级别。论文确实在 §7 末尾 "Future directions" 中提到了 per-step feedback 的可能性（"process-reward models with per-step feedback each offer paths to bridge the supervision density gap"），但仅一句带过。如果 SMART (arXiv 2509.16742) 已经用 per-step process rewards 成功做了 sycophancy mitigation，这应当在 §7 Related Work 中正式讨论，而非放在 future directions 中暗示"还没人做过"。

这也进一步支持了我的 N3 和 R2-N1 的论点：失败的根因可能是 reward granularity（per-completion scalar）而非 d_syc 方向本身。

---

**[AGREE] R2-W3: Conclusion 的 broader lesson overclaiming**

同意。§8 Conclusion 中 "any alignment effort that converts a direction probe into a reward signal must verify that the probe separates not only the target behavior from its complement, but also the valid and invalid instances within each class" 的表述过于宽泛。论文仅在 sycophancy 一个维度、GRPO 一种算法、Qwen3-8B 一个模型上实验。§7 Related Work 自己也承认 reasoning/safety directions 的 probe-based RL 存在成功案例（Zou et al. 2023, Burns et al. 2023 等的 representation engineering 方法）。

建议改为："For sycophancy specifically, where valid and invalid behaviors share the same geometric direction in activation space, scalar probe-based GRPO rewards are insufficient."

---

**[AGREE] R2-W4: 仅单一模型做 RL 训练**

同意，与我的 W5 一致。

---

**[REBUT] R2-W5: 181 对训练数据规模偏小**

部分不同意 R2 的 framing。

R2 关注的是"更大训练集是否能产生更鲁棒的 direction，缓解 cosine gap 仅 0.098 的问题"。但论文的核心论点不是 direction 提取质量差（AUROC 0.827 已经相当不错），而是 **即使 direction 能良好区分 sycophantic vs. non-sycophantic，这个方向作为 RL reward 仍然失败**。失败的根因在 §6 中明确分析：d_syc 编码的是 belief change 的方向，而 valid revision 和 sycophantic capitulation **都沿相同方向移动**——这是一个结构性问题，不会因为更多训练数据而消失。

cosine gap 0.098（§4 提到 "the cosine gap between valid and sycophantic activations averages only 0.098 across layers"）确实小，但这不是数据量的问题，而是反映了 valid revision 和 capitulation 在 activation space 中本身就很接近。更多 pairs 可以让 d_syc 方向估计更精确（降低 ±0.028 的 CV 方差），但不会拉大 valid/invalid activations 之间的结构性 gap。

我的 W4 关注的是 pair 构建的**质量控制**（style-controlled 方法不透明），而非数量——这是更关键的问题。181 对质量不明的 pairs 和 500 对同样质量不明的 pairs 不会有本质区别。

---

### Missing References

**[AGREE]** 三篇 missing references 均应补充。Papadatos & Freedman (2024) 和 SMART (2025) 与本文 thesis 有直接对话关系；DPO/KTO 是明显的 RL baseline 遗漏。

---

### Director 提出的三个具体问题

**Q1: R2-N1（Papadatos & Freedman 遗漏）是否确实是 critical gap？**

是的，但 critical 程度取决于该论文与本文方法的可比性。如果 Papadatos & Freedman 的 probe penalty 作用于 reward model 中间层（即修改 RM 的输出而非直接作为 policy reward），那两种方法的 failure/success 差异可以用 supervision granularity 来解释（与我的 N3 一致）——这反而**强化**本文的论点（scalar probe reward 不够，需要更细粒度的监督）。但如果该工作的 probe penalty 也是作为 scalar reward 直接给 policy optimizer 且成功了，那就是直接矛盾，必须在论文中解释。论文不讨论这一区别是不可接受的。

**Q2: R2-N2（引用质量）是否影响论文可信度？**

从方法严谨性角度：**是的，但程度有限**。引用不完整不改变实验结果的有效性，但 (1) ACT 的 "Unknown" 作者使读者无法验证这个关键 baseline 的原始定义，直接影响 reproducibility 评分；(2) 多条引用的系统性不完整暗示论文准备仓促或编辑标准低，会在审稿中产生负面信号。这是一个容易修复的问题，但在当前状态下确实降低可信度。

**Q3: 我的 N1（Fisher test 误用）和 R2-N1（missing reference）哪个对论文接收影响更大？**

**我的 N1 影响更大。**

理由：Fisher test 误用直接攻击论文的定量推理核心——将非独立 checkpoints 当作独立样本产生虚假的 p<0.0001，使得 GRPO vs ACT 的统计对比无效。这不是可以通过补充讨论来修复的，而是需要重新设计统计分析、可能增加实验 seeds。

R2-N1 的 missing reference 虽然重要，但本质上是 **framing 问题**——论文需要在 Related Work 中讨论为什么 probe penalty 在不同框架下有不同效果，并适当限定自己的 claims 范围。这是可以在 revision 中通过补充 1-2 段讨论来解决的。

从 ARR 评审角度，统计方法的根本性缺陷（影响 Soundness）比相关工作遗漏（主要影响 completeness/framing）对 Overall Assessment 的负面影响更大。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 88 · 2026-05-22T10:06:41.177153+00:00_

收到 Reviewer 1 的交叉回应。等待 Reviewer 2 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director"
}
```

</details>

---


## Round 5

## Round 5

2 recorded events


### User

_source line 89 · 2026-05-22T10:06:44.712555+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交。总结：

- **R2 的 8 条意见中，7 条 [AGREE]，1 条 [REBUT]**（R2-W5 关于 181 对数据量偏小——我认为问题是 pair 质量控制不透明而非数量不足，因为 cosine gap 0.098 是 valid/invalid activations 的结构性接近，更多数据不会改变这一点）
- 对 Director 三个问题的回答：R2-N1 确实是重要遗漏但 critical 程度取决于方法可比性；R2-N2 引用质量确实影响可信度但可快速修复；**我的 N1（Fisher test 独立性违反）对接收影响大于 R2-N1（missing reference）**，因为前者攻击 Soundness 核心，后者主要是 framing 问题。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 90 · 2026-05-22T10:06:53.127418+00:00_

收到 Reviewer 1 交叉回应（7 AGREE / 1 REBUT）。等待 Reviewer 2 交叉回应后进入收敛判断。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director"
}
```

</details>

---


## Round 6

## Round 6

8 recorded events


### User

_source line 91 · 2026-05-22T10:06:59.244161+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 — 交叉回应 Reviewer 1 意见

---

### Must-Fix 问题

**[AGREE] R1-N1: Fisher exact test 独立性假设违反**

完全同意这是一个严重的统计问题。同一 run 的连续 checkpoints 具有强时序自相关——Figure 3 的振荡曲线直观地展示了这一点。将 25 个 checkpoints 当作独立样本做 Fisher exact test 人为膨胀了有效样本量。真实的 run-level 比较只有 2 个 GRPO runs vs 1 个 ACT run（n=3），无法支撑任何统计检验。

不过我认为这个问题的影响范围需要精确界定：**定性结论（GRPO 振荡/失败，ACT 改善）从 Figure 3 的轨迹上是可直接观察的**，不依赖 p 值。问题在于 Section 1 和 Section 6 中使用 "p < 0.0001" 赋予了这一对比虚假的统计权威性。修复方案应该是：（1）移除 checkpoint-level Fisher test；（2）如 R1 建议，增加 seed 数量或使用 block bootstrap；（3）改为报告 run-level 的描述性统计。

**关于 R1-N1 vs R2-N2（引用问题）的严重性排序**：两者都是 critical 但性质不同。R1-N1 是 misleading statistical inference——p 值本身是错的但去掉后定性结论尚存。R2-N2 是 scholarly integrity——ACT 的引用作者为 "Unknown"，在 ARR desk-rejection checklist 中可能触发 "hallucinated references" 检查项。我认为两者同等严重，都必须在 camera-ready 前修复，但对接收决定的影响路径不同：N1 影响 soundness 评分，N2 影响审稿人对论文整体严谨性的信任。

---

**[AGREE] R1-N2: ACT 正面结果仅基于单个完成 seed**

与我的 R2-N3 完全一致。补充一点：即使 seed 2 已评估的 3/16 checkpoints "all exceed vanilla"，这 3 个 early checkpoints 不能代表 full trajectory——Table 4 显示 ACT seed 1 在 checkpoint 4000 处曾出现 SycophancyScore 回落（0.255→0.214），如果 seed 2 也存在类似甚至更严重的回落，结论可能需要调整。n=1 的正面 baseline 是论文当前最薄弱的环节之一。

---

**[AGREE] R1-N3: ACT vs GRPO 对比存在 supervision granularity confound**

这是 Reviewer 1 提出的最具深度的问题。我认同这一 confound 显著削弱了论文的 "SFT 路径可行，RL 路径走不通" 叙事。

具体分析：

1. **论文自身已承认但未充分控制**：Section 6 明确写到 "The critical difference is supervision density"——这本身就是在说 ACT 的成功可能主要归因于 per-token supervision 而非 d_syc 的内在问题。但论文的标题、Abstract、C1、C3 和 Conclusion 的 framing 都强调 "sycophancy directions fail as RL rewards"，这一叙事暗示问题出在 d_syc 上，而实际证据更支持 "sparse scalar rewards fail for sycophancy calibration" 这个更窄的结论。

2. **缺失的关键控制实验**：R1 建议的 "per-token d_syc projection 作为 dense reward 给 GRPO" 是一个理想的控制。如果 dense d_syc reward 在 GRPO 中也失败，才能真正说明 d_syc 本身有问题；如果成功，则说明问题出在 supervision granularity 而非 direction quality。

3. **R3-only GRPO 的证据**：论文用 R3-only GRPO（移除 d_syc，仅用行为 reward）的失败来论证 "GRPO 本身也不行"。但 R3-only 同样是 sparse scalar reward，所以这个 ablation 无法区分 "GRPO 框架的问题" 和 "sparse reward 的问题"。

4. **但论文的部分贡献不受此 confound 影响**：C2（probe trap + behavioral-before-distributional collapse）是一个独立的机制性发现，不依赖于 ACT 对比。即使 SFT vs RL 的叙事被削弱，probe trap 本身仍然成立。

**建议**：论文应将 framing 从 "d_syc fails as RL reward" 调整为 "d_syc fails as sparse scalar reward, and the supervision density gap cannot be bridged by GRPO's per-completion framework"。这个更精确的 claim 与现有证据完全吻合。

---

### Should-Fix 问题

**[AGREE] R1-W1: 超参数 w1 仅测试单一值，存在 false negative 风险**

部分同意。w1=0.25（F1a-F1c）和 w1=0.40（F1d）确实只是两个值，且 d_syc/20 的 scaling factor 20 的选择未解释。不过我认为这个问题的严重性低于 R1 的定位：

- F1b 中 cosine gap 仅 0.098 是 d_syc 与激活空间的几何性质，与 w1 无关
- F1a 中 tanh 饱和是 residual-stream norms 与 d_syc norm 的量级差异（100-1200x），任何合理的 w1 都会遇到
- 但 F1d 中 w1=0.40 + 5x scaling 的选择空间确实未被充分探索

建议作者报告 w1 sensitivity analysis（即使只是补充材料），但我不认为这会改变核心结论。

---

**[AGREE] R1-W2: 标题声明过于宽泛**

与我的 R2-W1 一致。标题 "RL Rewards" 应限定为 "GRPO Rewards" 或 "Scalar RL Rewards"。

---

**[AGREE] R1-W3: AUROC ±值不是正式 CI**

技术上正确。5-fold CV 的 5 个值的 std 不等于 confidence interval，每个 fold 仅 ~36 pairs 的情况下估计波动较大。Bootstrap 是更合适的方法。但我认为这是 should-fix 而非 critical——AUROC 0.827 的 discriminability 结论即使用更严格的 CI 方法也不太可能被推翻。

---

**[AGREE] R1-W4: Contrastive pairs 构建方法细节不足**

同意。Section 2.1 仅说 "style-controlled to match hedging, politeness, and length"，但未说明：
- Pairs 是人工编写、LLM 生成还是模板化？
- "Style-controlled" 的具体操作是什么（prompt engineering? post-hoc filtering? human editing?）
- 是否有 inter-annotator agreement 或 quality control
- Evidence strength 的三级划分标准是什么？

这对 reproducibility 有直接影响。

---

**[AGREE] R1-W5: RL 训练仅在 Qwen3-8B**

与我的 R2-W4 一致。

---

**[AGREE] R1-W6: Cross-seed 分析仅 2 个 seed**

同意。n=2 不足以建立可复现性。Section 6 中描述的两个 seed 的 crash 时间差异（seed 1 at checkpoint 6000, seed 2 at checkpoint 3500）恰好说明 2 个 seed 的行为已经出现显著分歧，更多 seed 是必要的。

---

### 小问题

**[AGREE]** NLI flip classifier 未报告准确率——这会影响 ToF/NoF 指标的可信度。

**[AGREE]** SycophancyScore 等权 harmonic mean 的设计选择未讨论——在 sycophancy calibration 中，是否 ToF 和 NoF 的权重应该相等不是自明的。

**[AGREE]** "Unknown (2025)" 引用——与我的 R2-N2 一致，这是最严重的引用问题之一。

**[AGREE]** Appendix A 的 100 responses 样本量偏小——但考虑到这是定性分析（taxonomy 构建），100 samples 是可接受的最低标准。

---

### Director 特别关注的三个问题

**Q1: R1-N1（Fisher test）vs R2-N2（引用问题）的严重性**

如上所述，两者同等 critical 但影响路径不同。Fisher test 问题使论文的统计推断不可靠（soundness），但定性结论（GRPO 失败、ACT 改善）从轨迹图上可直接观察，去掉 p 值后核心发现仍存在。引用问题（"Unknown" 作者、大量 incomplete entries）影响论文的 scholarly credibility，可能触发 ARR desk-rejection checklist 中的 "hallucinated references" 检查。从 "修复成本" 看，引用问题修复简单（补全 bib entries），Fisher test 修复需要更多 seeds 或方法变更。从 "对结论的影响" 看，Fisher test 的影响更大——如果不能建立 GRPO vs ACT 的统计显著差异，论文的 C1 和 C3 的量化支撑被削弱。

**Q2: R1-N3（supervision granularity confound）是否削弱 SFT vs RL 叙事**

是的，显著削弱。详见上方 R1-N3 回应。核心问题是论文的 framing（"d_syc fails as RL reward"）比实际证据支持的结论（"sparse scalar d_syc reward fails"）更宽泛。论文需要更精确的 framing 或补充控制实验。但 C2（probe trap）不受此 confound 影响，仍是论文的有效贡献。

**Q3: R2-N1（Papadatos & Freedman 2024 遗漏）是否仍为 critical**

**坚持 critical**。理由：

1. **直接相关性**：Papadatos & Freedman (2024) 使用 linear probe 在 reward model 内部惩罚 sycophancy，并报告成功。这与本文的核心 thesis（probe-based reward 不能用于 sycophancy mitigation）直接矛盾或至少需要精确区分。

2. **与 R1-N3 形成互补论证**：R1-N3 指出 ACT vs GRPO 的 supervision granularity confound；Papadatos & Freedman 的工作从另一个角度说明同一问题——probe-based signal 可以有效，但取决于如何整合到训练框架中。如果论文讨论了这一工作，可以更精确地定位自己的 contribution：不是 "probe detection 不能变成 reward"（太宽泛），而是 "probe detection 作为 GRPO 的 sparse per-completion scalar reward 不能工作"（更精确且有证据支持）。

3. **Reviewer 1 未提及不代表不重要**：R1 的审查侧重是 experimental rigor / statistical validity，遗漏文献不在其审查重点内。作为侧重 novelty + related work 的 Reviewer 2，这是我审查范围内的核心发现。

4. **修复成本低但 impact 高**：仅需在 Section 7 增加一段讨论，解释本文方法（probe as GRPO reward）与 Papadatos & Freedman（probe penalty in reward model）的差异，并分析为何一个失败另一个成功。这个分析反而能强化论文的 contribution——将失败归因精确化。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 92 · 2026-05-22T10:07:30.043501+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "contrastive_entrain_calib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "contrastive_entrain_calib"
  }
}
```

</details>

---


### Tool result

_source line 93 · 2026-05-22T10:07:30.095211+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-22T09:56:16.229264+00:00\", \"completed_at\": \"2026-05-22T09:59:19.320278+00:00\", \"findings\": [{\"severity\": \"warning\", \"dimension\": \"page 1-3\", \"message\": \"连续 3 页无任何 display item（figure/table），第一个视觉锚点推迟到 page 4。实证为主的论文建议在前 2 页内放置概念图、架构图或核心结果 teaser，帮助审稿人快速建立认知锚点。可考虑：(a) 在 page 1-2 加一个 overview figure 展示 d_syc 方向的 discriminability vs reward utility 的 gap；(b) 将 Figure 1 的关键结果以缩略形式提前到 Introduction 末尾\"}, {\"severity\": \"warning\", \"dimension\": \"page 10\", \"message\": \"Appendix A（Stubbornness Taxonomy）仅占页面约 1/4，剩余 3/4 为空白。建议扩充 appendix 内容（如补充实验细节、更多 failure mode 示例）或将此段合并到正文/其他 appendix 以消除大面积空白\"}, {\"severity\": \"info\", \"dimension\": \"page 5\", \"message\": \"单页包含 3 个 display items（Table 2 + Table 3 + Figure 2），视觉密度较高。Table 2 和 Table 3 列间距略紧，但内容仍可读。如果正文空间允许，可考虑将 Table 3 移至下一页以平衡节奏\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Figure 3 的 legend 字号偏小（4 条 trajectory 线），打印时可能需要辨认。建议略微增大 legend 字号或使用更显著的 line style 差异（dash pattern + marker shape）辅助区分\"}, {\"severity\": \"info\", \"dimension\": \"page 4-7\", \"message\": \"全部 7 个 display items 集中在 4 页内，前 3 页和后 1 页（正文部分）完全无视觉元素，节奏不够均匀\"}], \"counts\": {\"critical\": 0, \"warning\": 2, \"info\": 3}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 94 · 2026-05-22T10:08:28.044178+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "contrastive_entrain_calib",
  "issues_yaml": "issues:\n  - id: R1-N1\n    summary: \"Fisher exact test 将非独立 checkpoints 当独立样本，p<0.0001 不可信\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 首提，R2 交叉回应完全同意。两人共识：定性结论（GRPO 失败、ACT 改善）从轨迹图可直接观察，但 p 值赋予虚假统计权威性。需移除 checkpoint-level Fisher test，改用 run-level 描述性统计或增加 seeds。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R2-N1\n    summary: \"遗漏 Papadatos & Freedman (2024) probe penalty 成功案例，直接挑战核心 thesis\"\n    category: framing\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R2 首提，R1 交叉同意但认为 critical 偏下限。两人共识：论文必须讨论 probe penalty (RM 内部) vs probe reward (GRPO scalar) 的关键差异，否则核心 contribution 的 scope 不清。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R2-N2\n    summary: \"references.bib 多条引用严重不完整：ACT 作者为 Unknown，6 条仅 et al.\"\n    category: format\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R2 首提，R1 交叉同意且认为比 R2 描述更严重。ACT 是唯一成功 baseline，Unknown 作者使读者无法验证方法来源。可能触发 ARR desk-rejection checklist 的 hallucinated references 检查。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R1-N2\n    summary: \"ACT 正面结果仅基于单 seed 完整评估（seed 2 仅 3/16 checkpoints）\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"两人独立提出（R1-N2, R2-N3）。n=1 seed 不足以建立方法有效性，特别是 GRPO 已展示跨 seed 高方差。需完成 seed 2 全部 16 checkpoints 或在 Limitations 中将 ACT 成功定性为 preliminary evidence。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R1-N3\n    summary: \"ACT vs GRPO 对比存在 supervision granularity confound（per-token vs per-completion）\"\n    category: framing\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 首提，R2 交叉回应深度分析并完全同意。论文 framing 为 'd_syc fails as RL reward' 但实际证据仅支持 'sparse scalar d_syc reward fails'。缺少关键控制实验（per-token d_syc projection 作为 dense reward）。C2 (probe trap) 不受此 confound 影响。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R1-W1\n    summary: \"超参数 w1 仅测试 0.25/0.40 两个值，存在 false negative 风险\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 首提，R2 部分同意但认为 F1b cosine gap 0.098 与 w1 无关。需报告 w1 选择过程或 sensitivity analysis。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R1-W2\n    summary: \"标题 'RL Rewards' 过于宽泛，仅测试 GRPO；未讨论 DPO/KTO\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"两人独立提出（R1-W2, R2-W1）。DPO 天然适合 pair-wise 设置，可能绕过 scalar reward 问题。标题应改为 GRPO Rewards 或 Scalar RL Rewards。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R2-W2\n    summary: \"Process Reward Models 讨论不足，SMART (2025) 已报告成功\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R2 首提，R1 交叉同意但降级为 minor-to-warning。per-step reward 作为 sparse scalar 和 dense SFT 之间的中间方案，论文仅 1 句 future directions 提及。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R2-W3\n    summary: \"Conclusion 的 broader lesson ('any alignment effort') overclaiming\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R2 首提，R1 交叉完全同意。仅基于 sycophancy/GRPO/Qwen3-8B，不足以支撑普遍性声明。论文自己也承认 reasoning/safety 的 probe-based RL 存在成功案例。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R1-W3\n    summary: \"AUROC ±值来自 5-fold CV std，不是正式 CI\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 首提，R2 同意但认为 should-fix 而非 critical。建议改用 bootstrap 95% CI。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R1-W4\n    summary: \"Contrastive pairs 'style-controlled' 方法细节严重缺失\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 首提，R2 同意。未说明 pairs 是人工编写还是 LLM 生成，无 inter-annotator agreement，evidence strength 三级划分标准未说明。影响 reproducibility。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R1-W5\n    summary: \"所有 RL/SFT 训练仅在 Qwen3-8B 上进行\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"两人独立提出（R1-W5, R2-W4）。Llama-3-8B 仅验证 direction discriminability，RL 失败和 ACT 成功的模型无关性未验证。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R1-W6\n    summary: \"Cross-seed 分析仅 2 个 seed，不足以支撑可复现性声明\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 首提，R2 同意。两个 seed 的 crash 时间已有显著分歧（seed 1 at ckpt 6000, seed 2 at ckpt 3500），n=2 不足以建立统计可复现性。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R1-m1\n    summary: \"NLI flip classifier 未报告准确率或与人工标注一致性\"\n    category: method\n    severity: info\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 首提，R2 同意。ToF/NoF 可靠性依赖于此分类器，但未验证。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R1-m2\n    summary: \"SycophancyScore 等权 harmonic mean 设计选择未讨论\"\n    category: method\n    severity: info\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"ToF 和 NoF 的等权假设不自明，实际应用中可能有不同权重偏好。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "contrastive_entrain_calib",
    "issues_yaml": "issues:\n  - id: R1-N1\n    summary: \"Fisher exact test 将非独立 checkpoints 当独立样本，p<0.0001 不可信\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 首提，R2 交叉回应完全同意。两人共识：定性结论（GRPO 失败、ACT 改善）从轨迹图可直接观察，但 p 值赋予虚假统计权威性。需移除 checkpoint-level Fisher test，改用 run-level 描述性统计或增加 seeds。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R2-N1\n    summary: \"遗漏 Papadatos & Freedman (2024) probe penalty 成功案例，直接挑战核心 thesis\"\n    category: framing\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R2 首提，R1 交叉同意但认为 critical 偏下限。两人共识：论文必须讨论 probe penalty (RM 内部) vs probe reward (GRPO scalar) 的关键差异，否则核心 contribution 的 scope 不清。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R2-N2\n    summary: \"references.bib 多条引用严重不完整：ACT 作者为 Unknown，6 条仅 et al.\"\n    category: format\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R2 首提，R1 交叉同意且认为比 R2 描述更严重。ACT 是唯一成功 baseline，Unknown 作者使读者无法验证方法来源。可能触发 ARR desk-rejection checklist 的 hallucinated references 检查。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R1-N2\n    summary: \"ACT 正面结果仅基于单 seed 完整评估（seed 2 仅 3/16 checkpoints）\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"两人独立提出（R1-N2, R2-N3）。n=1 seed 不足以建立方法有效性，特别是 GRPO 已展示跨 seed 高方差。需完成 seed 2 全部 16 checkpoints 或在 Limitations 中将 ACT 成功定性为 preliminary evidence。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R1-N3\n    summary: \"ACT vs GRPO 对比存在 supervision granularity confound（per-token vs per-completion）\"\n    category: framing\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 首提，R2 交叉回应深度分析并完全同意。论文 framing 为 'd_syc fails as RL reward' 但实际证据仅支持 'sparse scalar d_syc reward fails'。缺少关键控制实验（per-token d_syc projection 作为 dense reward）。C2 (probe trap) 不受此 confound 影响。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R1-W1\n    summary: \"超参数 w1 仅测试 0.25/0.40 两个值，存在 false negative 风险\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 首提，R2 部分同意但认为 F1b cosine gap 0.098 与 w1 无关。需报告 w1 选择过程或 sensitivity analysis。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R1-W2\n    summary: \"标题 'RL Rewards' 过于宽泛，仅测试 GRPO；未讨论 DPO/KTO\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"两人独立提出（R1-W2, R2-W1）。DPO 天然适合 pair-wise 设置，可能绕过 scalar reward 问题。标题应改为 GRPO Rewards 或 Scalar RL Rewards。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R2-W2\n    summary: \"Process Reward Models 讨论不足，SMART (2025) 已报告成功\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R2 首提，R1 交叉同意但降级为 minor-to-warning。per-step reward 作为 sparse scalar 和 dense SFT 之间的中间方案，论文仅 1 句 future directions 提及。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R2-W3\n    summary: \"Conclusion 的 broader lesson ('any alignment effort') overclaiming\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R2 首提，R1 交叉完全同意。仅基于 sycophancy/GRPO/Qwen3-8B，不足以支撑普遍性声明。论文自己也承认 reasoning/safety 的 probe-based RL 存在成功案例。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R1-W3\n    summary: \"AUROC ±值来自 5-fold CV std，不是正式 CI\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 首提，R2 同意但认为 should-fix 而非 critical。建议改用 bootstrap 95% CI。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R1-W4\n    summary: \"Contrastive pairs 'style-controlled' 方法细节严重缺失\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 首提，R2 同意。未说明 pairs 是人工编写还是 LLM 生成，无 inter-annotator agreement，evidence strength 三级划分标准未说明。影响 reproducibility。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R1-W5\n    summary: \"所有 RL/SFT 训练仅在 Qwen3-8B 上进行\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"两人独立提出（R1-W5, R2-W4）。Llama-3-8B 仅验证 direction discriminability，RL 失败和 ACT 成功的模型无关性未验证。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R1-W6\n    summary: \"Cross-seed 分析仅 2 个 seed，不足以支撑可复现性声明\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 首提，R2 同意。两个 seed 的 crash 时间已有显著分歧（seed 1 at ckpt 6000, seed 2 at ckpt 3500），n=2 不足以建立统计可复现性。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R1-m1\n    summary: \"NLI flip classifier 未报告准确率或与人工标注一致性\"\n    category: method\n    severity: info\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 首提，R2 同意。ToF/NoF 可靠性依赖于此分类器，但未验证。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R1-m2\n    summary: \"SycophancyScore 等权 harmonic mean 设计选择未讨论\"\n    category: method\n    severity: info\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"ToF 和 NoF 的等权假设不自明，实际应用中可能有不同权重偏好。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n"
  }
}
```

</details>

---


### Tool result

_source line 95 · 2026-05-22T10:08:28.145225+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_issues.yaml\", \"bytes\": 6499}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 96 · 2026-05-22T10:10:53.202377+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "contrastive_entrain_calib",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.0 - Findings",
  "report": "# 审稿报告 — Round 1\n\n**论文**: \"Discriminability Without Utility: Why Sycophancy Directions Fail as RL Rewards\"\n**Venue**: EMNLP 2026 (ARR May 2026)\n**Reviewers**: 2 人（R1: 方法严谨性 + 实验设计 + 统计分析；R2: 新颖性 + 相关工作完整性 + 写作质量 + 格式合规）\n**圆桌轮次**: 1 轮（交叉回应后高度收敛，无需 Round 2）\n**收敛度**: R1 对 R2 的 8 条意见 7 [AGREE] 1 [REBUT]；R2 对 R1 全部 [AGREE]\n\n---\n\n## Summary\n\n论文从 Qwen3-8B 和 Llama-3-8B 上提取对比式 sycophancy 方向 $d_{syc}$（AUROC 0.827 / 0.779），然后测试三种将 $d_{syc}$ 转化为 GRPO 奖励信号的方案（cosine projection、binary probe、continuous probe），以及移除 $d_{syc}$ 后的纯行为奖励（R3-only GRPO）。所有 GRPO 方案均失败：cosine reward 因 gap 过窄或 mode collapse 而无效；binary probe 产生 stubbornness trap（ToF=0 at step 500，entropy 1300 步后才崩溃）；R3-only GRPO 仅 4/25 checkpoints 超过 vanilla。唯一成功的方法是 ACT（SFT + L2 activation consistency loss），seed 1 在 16/16 checkpoints 均超过 vanilla（SYCONScore 0.301）。论文提出根因是 $d_{syc}$ 编码 belief change 方向但不编码 evidential warrant，valid revision 和 sycophantic capitulation 在该方向上产生重叠激活。\n\n---\n\n## Strengths\n\n**S1. 系统性诊断链设计优秀（§4）** [R1, R2 共识]\nF1a→F1b→F1c→F1d 的递进式消除结构清晰有力：每个 variant 解决前一个的失败模式但暴露更深层问题。这是 negative result 论文的典范写法。\n\n**S2. Probe trap 发现有独立实用价值（§5）** [R1, R2 共识]\nBehavioral death (ToF=0 at step 500) 先于 distributional collapse (entropy 到 step ~1840 才下降) 1,300 步的发现，对 RL alignment 社区有直接警示：entropy-based early stopping 无法检测这类失败。此发现不受 ACT vs GRPO confound 影响。\n\n**S3. Cross-model validation 增强可信度（Table 1）** [R1, R2 共识]\n$d_{syc}$ 在 Qwen3-8B 和 Llama-3-8B 两个架构上均展示 discriminability，且 evidence-strength gradient 定性一致，表明 contrastive sycophancy 方向反映了共享的表征现象。\n\n**S4. 清晰的写作和可视化** [R2]\n论文结构紧凑，Figure 2（probe trap trajectory）和 Figure 3（SYCONScore trajectories）直观展示失败模式，Table 4 全方法对比一目了然。\n\n**S5. Stubbornness Taxonomy（Appendix A）有参考价值** [R1, R2 共识]\n对 probe-trained responses 的 100-sample 定性分析（sycophantic stubbornness 24%, deliberation traps 29%, evidence-graded hedging）提供了有价值的 failure mode 分类。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**MF1. [critical] Fisher exact test 独立性假设违反** [R1 首提, R2 AGREE]\n§1 和 §6 报告 Fisher exact test 比较 GRPO (4/25 checkpoints > vanilla) vs ACT seed 1 (16/16)，p<0.0001。但同一训练 run 的 checkpoints 具有强时序自相关（Figure 3 清楚展示连续振荡），严重违反独立性假设。Run-level 比较仅有 2 GRPO runs vs 1 ACT run（n=3），无法支撑统计检验。两位 Reviewer 共识：定性结论从轨迹图可直接观察，但 p 值赋予了虚假的统计权威性。\n- **修复方向**：移除 checkpoint-level Fisher test；改为 run-level 描述性统计 + effect size；增加 seed 数量；或使用 block bootstrap。\n\n**MF2. [critical] 遗漏直接相关成功案例 Papadatos & Freedman (2024)** [R2 首提, R1 AGREE]\narXiv 2412.00967 \"Linear Probe Penalties Reduce LLM Sycophancy\" 使用 linear probe 在 reward model 内部惩罚 sycophancy 标记并报告成功。这与论文 \"representation-level detection 不能转化为有效 reward signal\" 的核心 thesis 存在直接张力。论文未讨论为何同类信号在不同框架下（RM 内部 penalty vs GRPO scalar reward）效果截然不同。R1 指出合理区分可能存在（probe penalty 保留 RM per-token richness vs 本文压缩为 per-completion scalar），但论文必须做这一分析。\n- **修复方向**：§7 Related Work 增加专段讨论；§6 root cause 分析中解释两种方法差异；提出 testable hypothesis。\n\n**MF3. [critical] references.bib 多条引用严重不完整** [R2 首提, R1 AGREE 且认为比 R2 描述更严重]\n至少 7 条 bib entry 存在严重问题：\n- `consistency2025bctact`（ACT，唯一成功 baseline）：author = \"Unknown\"，论文标题也不准确\n- `zhang2026latentgrpo`, `wang2025internal`, `sinii2025smallvectors`, `obrien2025fewbadneurons`：仅 \"et al.\"\n- `wei2024synthetic`：将 \"Anthropic\" 列为作者名\n- `ackermann2026gradreg`：\"Ackermann, Johannes and others\"\n\nACT 引用的 \"Unknown\" 尤其严重——唯一正面 baseline 的方法来源不可追溯，可能触发 ARR desk-rejection checklist 的 hallucinated references 检查。R1 补充：如果 \"Unknown\" 是匿名化自己的工作，存在 baseline 公平性问题。\n- **修复方向**：补全所有 bib entries 的完整作者列表、正确标题、准确 venue。\n\n**MF4. [critical] ACT 正面结果仅基于单 seed 完整评估** [R1, R2 独立提出]\nACT seed 2 仅评估 3/16 checkpoints（标注 \"ongoing\"）。论文核心对比（GRPO 4/25 vs ACT 16/16）仅基于 seed 1。考虑到 GRPO 本身已展示跨 seed 高方差，n=1 的正面 baseline 不足以建立方法有效性。R2 补充：ACT seed 1 在 checkpoint 4000 曾出现回落（0.255→0.214），seed 2 若有更严重回落将影响结论。\n- **修复方向**：提交前完成 seed 2 全部 16 checkpoints；或在 Limitations 中将 ACT 成功定性为 preliminary evidence 并调整 claims 强度。\n\n**MF5. [critical] ACT vs GRPO 对比存在 supervision granularity confound** [R1 首提, R2 AGREE 并深度分析]\nACT 使用 dense per-token supervision（SFT + L2 activation consistency loss），GRPO 使用 single scalar per completion。论文 §6 自身写到 \"The critical difference is supervision density\"，但 framing（标题、Abstract、C1、C3、Conclusion）强调 \"d_syc fails as RL reward\"，暗示问题出在方向本身。实际证据仅支持更窄结论：\"sparse scalar d_syc reward fails for sycophancy calibration\"。缺少关键控制实验——per-token d_syc projection 作为 dense reward 给 GRPO。R3-only GRPO 的失败也无法区分 \"GRPO 框架问题\" 和 \"sparse reward 问题\"，因为同样是 sparse scalar。\n- **修复方向**：(1) 调整 framing 为 \"d_syc fails as sparse scalar reward\"；(2) 增加 dense d_syc reward 控制实验；(3) 或在 Limitations 中显式承认此 confound。\n\n### Should-Fix（影响评分但不一票否决）\n\n**SF1. [warning] 标题 \"RL Rewards\" 过于宽泛，未讨论 DPO/KTO** [R1-W2, R2-W1 独立提出, 交叉互 AGREE]\n仅测试 GRPO 一种 RL 算法。DPO 基于 preference pair 而非 scalar reward，天然适合 $d_{syc}$ 构造的 sycophantic vs non-sycophantic pair，可能绕过 \"单一标量无法区分 warranted vs unwarranted\" 的核心问题。标题应限定为 \"GRPO Rewards\" 或 \"Scalar RL Rewards\"。\n\n**SF2. [warning] Process Reward Models 讨论不足** [R2 首提, R1 降级为 minor-to-warning]\nSMART (arXiv 2509.16742) 已使用 per-step process rewards + MCTS 进行 sycophancy mitigation 并报告成功。论文仅 1 句 future directions 提及。per-step reward 是 sparse scalar 和 dense SFT 之间的自然中间方案，对 supervision density 论点至关重要。\n\n**SF3. [warning] Conclusion 的 broader lesson overclaiming** [R2 首提, R1 AGREE]\n§8 \"any alignment effort that converts a detection probe into a reward signal must verify...\" 仅基于 sycophancy/GRPO/Qwen3-8B。论文 §7 自己承认 reasoning/safety 的 probe-based RL 存在成功案例。应改为条件化表述，明确标注这是从 sycophancy case 推广的 hypothesis。\n\n**SF4. [warning] 超参数 w1 仅测试 0.25/0.40 两个值** [R1 首提, R2 部分同意]\nGRPO 失败可能是调参不充分的 artifact。F1a 中 d_syc/20 的 scaling factor 未解释来源。需报告选择过程或 sensitivity analysis。R2 指出 F1b cosine gap 0.098 与 w1 无关，但 F1d 的设计空间未被充分探索。\n\n**SF5. [warning] AUROC ±值不是正式 CI** [R1 首提, R2 同意但认为不 critical]\n5-fold CV 的 5 个值的标准差不等于 confidence interval，每个 fold 仅约 36 pairs。建议改用 bootstrap 95% CI。\n\n**SF6. [warning] Contrastive pairs 构建方法细节严重缺失** [R1 首提, R2 AGREE]\n§2.1 仅称 \"style-controlled to match hedging, politeness, and length\"，但未说明生成方法（人工/LLM/模板）、quality control、inter-annotator agreement、evidence strength 三级划分标准。直接影响 reproducibility。\n\n**SF7. [warning] 所有 RL/SFT 训练仅在 Qwen3-8B 上进行** [R1-W5, R2-W4 独立提出]\nLlama-3-8B 仅验证 direction discriminability。GRPO 失败和 ACT 成功的模型无关性未验证。C1 的 \"Every tested GRPO formulation fails\" 严格意义上仅适用于 Qwen3-8B。\n\n**SF8. [warning] Cross-seed 分析仅 2 个 seed** [R1 首提, R2 AGREE]\nn=2 不足以建立统计意义上的可复现性。两个 seed 的 crash 时间已有显著分歧（seed 1 at ckpt 6000, seed 2 at ckpt 3500）。\n\n---\n\n## Reviewer Consensus [AGREE]\n\n两位 Reviewer 在以下关键判断上完全一致：\n1. **Overall 3.0 (Findings)**——核心 insight 有价值但证据/framing 不足以支撑 main conference\n2. **Probe trap (C2) 是论文最强贡献**——独立于 ACT 对比，不受 supervision granularity confound 影响\n3. **标题和结论 overclaim**——从 sycophancy/GRPO/Qwen3-8B 推广到 general \"RL Rewards\" 证据不足\n4. **ACT 单 seed 是最薄弱环节之一**——论文核心正面 baseline 的可靠性存疑\n5. **Fisher test 误用和引用不完整同等严重但影响路径不同**——前者攻击 soundness，后者攻击 scholarly credibility\n\n## Reviewer Divergence [REBUT]\n\n唯一分歧：**181 对训练数据规模是否偏小**\n- R2 认为更大训练集可能产生更鲁棒 direction，缓解 cosine gap 0.098 的问题\n- R1 [REBUT]：cosine gap 0.098 反映 valid/invalid activations 在 activation space 中的结构性接近（两者都沿 $d_{syc}$ 方向移动），不会因更多数据消失。问题是 pair 构建的质量控制不透明（R1-W4），而非数量不足。\n- **Director 判断**：采纳 R1 的分析——数据量不是核心问题，质量控制透明度是（已列为 SF6）。\n\n---\n\n## Questions for Authors\n\n1. 如何解释 Papadatos & Freedman (2024) 用 probe penalty 在 RM 上成功降低 sycophancy，而本文 probe-based GRPO reward 全部失败？关键差异是 intervention 位置、optimization 框架，还是 supervision granularity？\n2. ACT seed 2 完整评估何时完成？若 seed 2 表现不稳定（如仅 50% checkpoints 超过 vanilla），论文结论是否需要修改？\n3. 是否尝试过 DPO/KTO？如果 $d_{syc}$ 用于构造 preference pair 而非 scalar reward，\"discriminability ≠ utility\" 论点是否成立？\n4. 论文是否做过 per-token $d_{syc}$ projection 作为 dense GRPO reward 的实验？这是区分 \"direction 本身问题\" 和 \"reward granularity 问题\" 的关键控制。\n5. Fisher exact test 如果改为 run-level 比较（每 run 取 peak SYCONScore），结论是否仍然成立？\n6. w1=0.25 如何选定？是否做过 sensitivity analysis？\n7. Contrastive pairs 的构建流程是什么（人工/LLM/模板）？是否有 quality control？\n\n---\n\n## Missing References\n\n1. **Papadatos, H. & Freedman, R. (2024).** Linear Probe Penalties Reduce LLM Sycophancy. arXiv:2412.00967. [最关键遗漏——probe-based reward 成功案例]\n2. **SMART (2025).** Sycophancy Mitigation Through Reinforcement Learning with Uncertainty-Aware Adaptive Reasoning Trajectories. arXiv:2509.16742. [per-step process rewards 用于 sycophancy mitigation]\n3. **Rafailov et al. (2023).** DPO: Direct Preference Optimization. [preference-based RL 替代方案]\n4. **Ethayarajh et al. (2024).** KTO: Model Alignment as Prospect Theoretic Optimization. [preference-based RL 替代方案]\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未配置。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成（0 critical / 2 warning / 3 info）。\n\n| 严重性 | 位置 | 发现 |\n|--------|------|------|\n| ⚠️ warning | p1-3 | 连续 3 页无任何 display item，第一个视觉锚点推迟到 p4。实证论文建议前 2 页内放置概念图或核心结果 teaser |\n| ⚠️ warning | p10 | Appendix A 仅占页面约 1/4，剩余 3/4 空白。建议扩充或合并 |\n| ℹ️ info | p5 | 单页含 3 个 display items（Table 2 + Table 3 + Figure 2），密度较高但可读 |\n| ℹ️ info | p7 | Figure 3 legend 字号偏小，打印时可能需要辨认 |\n| ℹ️ info | p4-7 | 全部 7 个 display items 集中在 4 页内，前后页面无视觉元素，节奏不均匀 |\n\n---\n\n## Overall Assessment\n\n**评分：3.0 — Findings**（两位 Reviewer 一致）\n\n**置信度：4/5**（两位 Reviewer 均熟悉 representation engineering、RLHF、sycophancy 相关文献）\n\n论文揭示了一个重要的结构性现象：表征空间中的 sycophancy 方向虽然具有良好的判别能力，但不能直接转化为有效的 GRPO 奖励信号。Probe trap 的发现（behavioral death 先于 distributional collapse 1300 步）对 RL alignment 社区有直接实用价值。\n\n但论文存在 5 个 critical 问题：(1) Fisher exact test 将非独立 checkpoints 当独立样本导致 p 值不可信；(2) 遗漏了 Papadatos & Freedman (2024) 的 probe penalty 成功案例；(3) 引用质量严重不足（ACT 作者为 \"Unknown\"）；(4) ACT 正面结果仅基于单 seed；(5) ACT vs GRPO 对比存在 supervision granularity confound。此外，标题从 sycophancy/GRPO/Qwen3-8B 推广到 general \"RL Rewards\" 证据不足，缺少 DPO/KTO 讨论和 process reward models 分析。\n\n核心贡献（特别是 C2: probe trap）有 Findings 接收的价值，但需要：修复统计分析、补全引用、完成 ACT seed 2、调整 framing 精确化 claims scope、补充关键相关工作讨论。\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- \"p < 0.0001\" (Fisher exact test) 需移除或替换为 run-level 统计（MF1）\n- 三个 contributions 的 scope 需与实际证据对齐——C1 和 C3 应限定为 \"GRPO scalar rewards\" 而非 \"RL rewards\"（MF5, SF1）\n\n### §2 Experimental Framework\n- §2.1: Contrastive pairs 构建方法需详细说明（SF6）\n- §2.2: w1=0.25 的选择过程需说明（SF4）；应讨论为何未测试 DPO/KTO（SF1）\n- §2.4: ACT 引用需修复——author=\"Unknown\" 不可接受（MF3）\n- §2.5: NLI flip classifier 的准确率需报告\n\n### §3 Direction Discriminability\n- AUROC ±0.028 应改为 bootstrap 95% CI（SF5）\n- Table 1 和 Figure 1 的呈现清晰，是论文的优势部分\n\n### §4 Cosine R1: Structural Failure\n- Table 2 的诊断链设计是论文最强的方法论贡献（S1）\n- F1a-F1d 的分析有说服力，但 w1 sensitivity analysis 缺失（SF4）\n\n### §5 The Probe Reward Trap\n- 最强独立贡献（S2）——behavioral-before-distributional collapse 的 1300-step lag 发现有独立价值\n- 不受 ACT confound 影响\n\n### §6 Analysis\n- \"The critical difference is supervision density\" 与标题/abstract 的 framing 矛盾（MF5）\n- Fisher test p 值需移除（MF1）\n- 应增加对 Papadatos & Freedman (2024) 和 SMART (2025) 的讨论（MF2, SF2）\n- ACT seed 2 数据需补完或将 claims 降级为 preliminary（MF4）\n\n### §7 Related Work\n- 缺少 Papadatos & Freedman (2024)——最关键遗漏（MF2）\n- 缺少 DPO/KTO 和 process reward models 的讨论（SF1, SF2）\n- 整体偏薄（约 1 页），对于做出广泛方法论声明的论文不够\n\n### §8 Conclusion\n- \"any alignment effort\" 的一般性声明需条件化（SF3）\n- broader lesson 应明确标注为从 sycophancy case 推广的 hypothesis\n\n### Limitations\n- 已覆盖 3 个点（单模型训练、ACT seed 2 未完成、binary evaluation），但应追加：supervision granularity confound（MF5）、引用问题（MF3）、Fisher test 局限（MF1）\n\n### References\n- 7 条 bib entry 需补全完整作者和正确 venue（MF3）\n\n### Appendix\n- Stubbornness Taxonomy 有参考价值但样本量偏小（100）\n- 大面积空白（visual check warning）建议扩充内容"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "project": "contrastive_entrain_calib",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.0 - Findings",
    "report": "# 审稿报告 — Round 1\n\n**论文**: \"Discriminability Without Utility: Why Sycophancy Directions Fail as RL Rewards\"\n**Venue**: EMNLP 2026 (ARR May 2026)\n**Reviewers**: 2 人（R1: 方法严谨性 + 实验设计 + 统计分析；R2: 新颖性 + 相关工作完整性 + 写作质量 + 格式合规）\n**圆桌轮次**: 1 轮（交叉回应后高度收敛，无需 Round 2）\n**收敛度**: R1 对 R2 的 8 条意见 7 [AGREE] 1 [REBUT]；R2 对 R1 全部 [AGREE]\n\n---\n\n## Summary\n\n论文从 Qwen3-8B 和 Llama-3-8B 上提取对比式 sycophancy 方向 $d_{syc}$（AUROC 0.827 / 0.779），然后测试三种将 $d_{syc}$ 转化为 GRPO 奖励信号的方案（cosine projection、binary probe、continuous probe），以及移除 $d_{syc}$ 后的纯行为奖励（R3-only GRPO）。所有 GRPO 方案均失败：cosine reward 因 gap 过窄或 mode collapse 而无效；binary probe 产生 stubbornness trap（ToF=0 at step 500，entropy 1300 步后才崩溃）；R3-only GRPO 仅 4/25 checkpoints 超过 vanilla。唯一成功的方法是 ACT（SFT + L2 activation consistency loss），seed 1 在 16/16 checkpoints 均超过 vanilla（SYCONScore 0.301）。论文提出根因是 $d_{syc}$ 编码 belief change 方向但不编码 evidential warrant，valid revision 和 sycophantic capitulation 在该方向上产生重叠激活。\n\n---\n\n## Strengths\n\n**S1. 系统性诊断链设计优秀（§4）** [R1, R2 共识]\nF1a→F1b→F1c→F1d 的递进式消除结构清晰有力：每个 variant 解决前一个的失败模式但暴露更深层问题。这是 negative result 论文的典范写法。\n\n**S2. Probe trap 发现有独立实用价值（§5）** [R1, R2 共识]\nBehavioral death (ToF=0 at step 500) 先于 distributional collapse (entropy 到 step ~1840 才下降) 1,300 步的发现，对 RL alignment 社区有直接警示：entropy-based early stopping 无法检测这类失败。此发现不受 ACT vs GRPO confound 影响。\n\n**S3. Cross-model validation 增强可信度（Table 1）** [R1, R2 共识]\n$d_{syc}$ 在 Qwen3-8B 和 Llama-3-8B 两个架构上均展示 discriminability，且 evidence-strength gradient 定性一致，表明 contrastive sycophancy 方向反映了共享的表征现象。\n\n**S4. 清晰的写作和可视化** [R2]\n论文结构紧凑，Figure 2（probe trap trajectory）和 Figure 3（SYCONScore trajectories）直观展示失败模式，Table 4 全方法对比一目了然。\n\n**S5. Stubbornness Taxonomy（Appendix A）有参考价值** [R1, R2 共识]\n对 probe-trained responses 的 100-sample 定性分析（sycophantic stubbornness 24%, deliberation traps 29%, evidence-graded hedging）提供了有价值的 failure mode 分类。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**MF1. [critical] Fisher exact test 独立性假设违反** [R1 首提, R2 AGREE]\n§1 和 §6 报告 Fisher exact test 比较 GRPO (4/25 checkpoints > vanilla) vs ACT seed 1 (16/16)，p<0.0001。但同一训练 run 的 checkpoints 具有强时序自相关（Figure 3 清楚展示连续振荡），严重违反独立性假设。Run-level 比较仅有 2 GRPO runs vs 1 ACT run（n=3），无法支撑统计检验。两位 Reviewer 共识：定性结论从轨迹图可直接观察，但 p 值赋予了虚假的统计权威性。\n- **修复方向**：移除 checkpoint-level Fisher test；改为 run-level 描述性统计 + effect size；增加 seed 数量；或使用 block bootstrap。\n\n**MF2. [critical] 遗漏直接相关成功案例 Papadatos & Freedman (2024)** [R2 首提, R1 AGREE]\narXiv 2412.00967 \"Linear Probe Penalties Reduce LLM Sycophancy\" 使用 linear probe 在 reward model 内部惩罚 sycophancy 标记并报告成功。这与论文 \"representation-level detection 不能转化为有效 reward signal\" 的核心 thesis 存在直接张力。论文未讨论为何同类信号在不同框架下（RM 内部 penalty vs GRPO scalar reward）效果截然不同。R1 指出合理区分可能存在（probe penalty 保留 RM per-token richness vs 本文压缩为 per-completion scalar），但论文必须做这一分析。\n- **修复方向**：§7 Related Work 增加专段讨论；§6 root cause 分析中解释两种方法差异；提出 testable hypothesis。\n\n**MF3. [critical] references.bib 多条引用严重不完整** [R2 首提, R1 AGREE 且认为比 R2 描述更严重]\n至少 7 条 bib entry 存在严重问题：\n- `consistency2025bctact`（ACT，唯一成功 baseline）：author = \"Unknown\"，论文标题也不准确\n- `zhang2026latentgrpo`, `wang2025internal`, `sinii2025smallvectors`, `obrien2025fewbadneurons`：仅 \"et al.\"\n- `wei2024synthetic`：将 \"Anthropic\" 列为作者名\n- `ackermann2026gradreg`：\"Ackermann, Johannes and others\"\n\nACT 引用的 \"Unknown\" 尤其严重——唯一正面 baseline 的方法来源不可追溯，可能触发 ARR desk-rejection checklist 的 hallucinated references 检查。R1 补充：如果 \"Unknown\" 是匿名化自己的工作，存在 baseline 公平性问题。\n- **修复方向**：补全所有 bib entries 的完整作者列表、正确标题、准确 venue。\n\n**MF4. [critical] ACT 正面结果仅基于单 seed 完整评估** [R1, R2 独立提出]\nACT seed 2 仅评估 3/16 checkpoints（标注 \"ongoing\"）。论文核心对比（GRPO 4/25 vs ACT 16/16）仅基于 seed 1。考虑到 GRPO 本身已展示跨 seed 高方差，n=1 的正面 baseline 不足以建立方法有效性。R2 补充：ACT seed 1 在 checkpoint 4000 曾出现回落（0.255→0.214），seed 2 若有更严重回落将影响结论。\n- **修复方向**：提交前完成 seed 2 全部 16 checkpoints；或在 Limitations 中将 ACT 成功定性为 preliminary evidence 并调整 claims 强度。\n\n**MF5. [critical] ACT vs GRPO 对比存在 supervision granularity confound** [R1 首提, R2 AGREE 并深度分析]\nACT 使用 dense per-token supervision（SFT + L2 activation consistency loss），GRPO 使用 single scalar per completion。论文 §6 自身写到 \"The critical difference is supervision density\"，但 framing（标题、Abstract、C1、C3、Conclusion）强调 \"d_syc fails as RL reward\"，暗示问题出在方向本身。实际证据仅支持更窄结论：\"sparse scalar d_syc reward fails for sycophancy calibration\"。缺少关键控制实验——per-token d_syc projection 作为 dense reward 给 GRPO。R3-only GRPO 的失败也无法区分 \"GRPO 框架问题\" 和 \"sparse reward 问题\"，因为同样是 sparse scalar。\n- **修复方向**：(1) 调整 framing 为 \"d_syc fails as sparse scalar reward\"；(2) 增加 dense d_syc reward 控制实验；(3) 或在 Limitations 中显式承认此 confound。\n\n### Should-Fix（影响评分但不一票否决）\n\n**SF1. [warning] 标题 \"RL Rewards\" 过于宽泛，未讨论 DPO/KTO** [R1-W2, R2-W1 独立提出, 交叉互 AGREE]\n仅测试 GRPO 一种 RL 算法。DPO 基于 preference pair 而非 scalar reward，天然适合 $d_{syc}$ 构造的 sycophantic vs non-sycophantic pair，可能绕过 \"单一标量无法区分 warranted vs unwarranted\" 的核心问题。标题应限定为 \"GRPO Rewards\" 或 \"Scalar RL Rewards\"。\n\n**SF2. [warning] Process Reward Models 讨论不足** [R2 首提, R1 降级为 minor-to-warning]\nSMART (arXiv 2509.16742) 已使用 per-step process rewards + MCTS 进行 sycophancy mitigation 并报告成功。论文仅 1 句 future directions 提及。per-step reward 是 sparse scalar 和 dense SFT 之间的自然中间方案，对 supervision density 论点至关重要。\n\n**SF3. [warning] Conclusion 的 broader lesson overclaiming** [R2 首提, R1 AGREE]\n§8 \"any alignment effort that converts a detection probe into a reward signal must verify...\" 仅基于 sycophancy/GRPO/Qwen3-8B。论文 §7 自己承认 reasoning/safety 的 probe-based RL 存在成功案例。应改为条件化表述，明确标注这是从 sycophancy case 推广的 hypothesis。\n\n**SF4. [warning] 超参数 w1 仅测试 0.25/0.40 两个值** [R1 首提, R2 部分同意]\nGRPO 失败可能是调参不充分的 artifact。F1a 中 d_syc/20 的 scaling factor 未解释来源。需报告选择过程或 sensitivity analysis。R2 指出 F1b cosine gap 0.098 与 w1 无关，但 F1d 的设计空间未被充分探索。\n\n**SF5. [warning] AUROC ±值不是正式 CI** [R1 首提, R2 同意但认为不 critical]\n5-fold CV 的 5 个值的标准差不等于 confidence interval，每个 fold 仅约 36 pairs。建议改用 bootstrap 95% CI。\n\n**SF6. [warning] Contrastive pairs 构建方法细节严重缺失** [R1 首提, R2 AGREE]\n§2.1 仅称 \"style-controlled to match hedging, politeness, and length\"，但未说明生成方法（人工/LLM/模板）、quality control、inter-annotator agreement、evidence strength 三级划分标准。直接影响 reproducibility。\n\n**SF7. [warning] 所有 RL/SFT 训练仅在 Qwen3-8B 上进行** [R1-W5, R2-W4 独立提出]\nLlama-3-8B 仅验证 direction discriminability。GRPO 失败和 ACT 成功的模型无关性未验证。C1 的 \"Every tested GRPO formulation fails\" 严格意义上仅适用于 Qwen3-8B。\n\n**SF8. [warning] Cross-seed 分析仅 2 个 seed** [R1 首提, R2 AGREE]\nn=2 不足以建立统计意义上的可复现性。两个 seed 的 crash 时间已有显著分歧（seed 1 at ckpt 6000, seed 2 at ckpt 3500）。\n\n---\n\n## Reviewer Consensus [AGREE]\n\n两位 Reviewer 在以下关键判断上完全一致：\n1. **Overall 3.0 (Findings)**——核心 insight 有价值但证据/framing 不足以支撑 main conference\n2. **Probe trap (C2) 是论文最强贡献**——独立于 ACT 对比，不受 supervision granularity confound 影响\n3. **标题和结论 overclaim**——从 sycophancy/GRPO/Qwen3-8B 推广到 general \"RL Rewards\" 证据不足\n4. **ACT 单 seed 是最薄弱环节之一**——论文核心正面 baseline 的可靠性存疑\n5. **Fisher test 误用和引用不完整同等严重但影响路径不同**——前者攻击 soundness，后者攻击 scholarly credibility\n\n## Reviewer Divergence [REBUT]\n\n唯一分歧：**181 对训练数据规模是否偏小**\n- R2 认为更大训练集可能产生更鲁棒 direction，缓解 cosine gap 0.098 的问题\n- R1 [REBUT]：cosine gap 0.098 反映 valid/invalid activations 在 activation space 中的结构性接近（两者都沿 $d_{syc}$ 方向移动），不会因更多数据消失。问题是 pair 构建的质量控制不透明（R1-W4），而非数量不足。\n- **Director 判断**：采纳 R1 的分析——数据量不是核心问题，质量控制透明度是（已列为 SF6）。\n\n---\n\n## Questions for Authors\n\n1. 如何解释 Papadatos & Freedman (2024) 用 probe penalty 在 RM 上成功降低 sycophancy，而本文 probe-based GRPO reward 全部失败？关键差异是 intervention 位置、optimization 框架，还是 supervision granularity？\n2. ACT seed 2 完整评估何时完成？若 seed 2 表现不稳定（如仅 50% checkpoints 超过 vanilla），论文结论是否需要修改？\n3. 是否尝试过 DPO/KTO？如果 $d_{syc}$ 用于构造 preference pair 而非 scalar reward，\"discriminability ≠ utility\" 论点是否成立？\n4. 论文是否做过 per-token $d_{syc}$ projection 作为 dense GRPO reward 的实验？这是区分 \"direction 本身问题\" 和 \"reward granularity 问题\" 的关键控制。\n5. Fisher exact test 如果改为 run-level 比较（每 run 取 peak SYCONScore），结论是否仍然成立？\n6. w1=0.25 如何选定？是否做过 sensitivity analysis？\n7. Contrastive pairs 的构建流程是什么（人工/LLM/模板）？是否有 quality control？\n\n---\n\n## Missing References\n\n1. **Papadatos, H. & Freedman, R. (2024).** Linear Probe Penalties Reduce LLM Sycophancy. arXiv:2412.00967. [最关键遗漏——probe-based reward 成功案例]\n2. **SMART (2025).** Sycophancy Mitigation Through Reinforcement Learning with Uncertainty-Aware Adaptive Reasoning Trajectories. arXiv:2509.16742. [per-step process rewards 用于 sycophancy mitigation]\n3. **Rafailov et al. (2023).** DPO: Direct Preference Optimization. [preference-based RL 替代方案]\n4. **Ethayarajh et al. (2024).** KTO: Model Alignment as Prospect Theoretic Optimization. [preference-based RL 替代方案]\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未配置。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成（0 critical / 2 warning / 3 info）。\n\n| 严重性 | 位置 | 发现 |\n|--------|------|------|\n| ⚠️ warning | p1-3 | 连续 3 页无任何 display item，第一个视觉锚点推迟到 p4。实证论文建议前 2 页内放置概念图或核心结果 teaser |\n| ⚠️ warning | p10 | Appendix A 仅占页面约 1/4，剩余 3/4 空白。建议扩充或合并 |\n| ℹ️ info | p5 | 单页含 3 个 display items（Table 2 + Table 3 + Figure 2），密度较高但可读 |\n| ℹ️ info | p7 | Figure 3 legend 字号偏小，打印时可能需要辨认 |\n| ℹ️ info | p4-7 | 全部 7 个 display items 集中在 4 页内，前后页面无视觉元素，节奏不均匀 |\n\n---\n\n## Overall Assessment\n\n**评分：3.0 — Findings**（两位 Reviewer 一致）\n\n**置信度：4/5**（两位 Reviewer 均熟悉 representation engineering、RLHF、sycophancy 相关文献）\n\n论文揭示了一个重要的结构性现象：表征空间中的 sycophancy 方向虽然具有良好的判别能力，但不能直接转化为有效的 GRPO 奖励信号。Probe trap 的发现（behavioral death 先于 distributional collapse 1300 步）对 RL alignment 社区有直接实用价值。\n\n但论文存在 5 个 critical 问题：(1) Fisher exact test 将非独立 checkpoints 当独立样本导致 p 值不可信；(2) 遗漏了 Papadatos & Freedman (2024) 的 probe penalty 成功案例；(3) 引用质量严重不足（ACT 作者为 \"Unknown\"）；(4) ACT 正面结果仅基于单 seed；(5) ACT vs GRPO 对比存在 supervision granularity confound。此外，标题从 sycophancy/GRPO/Qwen3-8B 推广到 general \"RL Rewards\" 证据不足，缺少 DPO/KTO 讨论和 process reward models 分析。\n\n核心贡献（特别是 C2: probe trap）有 Findings 接收的价值，但需要：修复统计分析、补全引用、完成 ACT seed 2、调整 framing 精确化 claims scope、补充关键相关工作讨论。\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- \"p < 0.0001\" (Fisher exact test) 需移除或替换为 run-level 统计（MF1）\n- 三个 contributions 的 scope 需与实际证据对齐——C1 和 C3 应限定为 \"GRPO scalar rewards\" 而非 \"RL rewards\"（MF5, SF1）\n\n### §2 Experimental Framework\n- §2.1: Contrastive pairs 构建方法需详细说明（SF6）\n- §2.2: w1=0.25 的选择过程需说明（SF4）；应讨论为何未测试 DPO/KTO（SF1）\n- §2.4: ACT 引用需修复——author=\"Unknown\" 不可接受（MF3）\n- §2.5: NLI flip classifier 的准确率需报告\n\n### §3 Direction Discriminability\n- AUROC ±0.028 应改为 bootstrap 95% CI（SF5）\n- Table 1 和 Figure 1 的呈现清晰，是论文的优势部分\n\n### §4 Cosine R1: Structural Failure\n- Table 2 的诊断链设计是论文最强的方法论贡献（S1）\n- F1a-F1d 的分析有说服力，但 w1 sensitivity analysis 缺失（SF4）\n\n### §5 The Probe Reward Trap\n- 最强独立贡献（S2）——behavioral-before-distributional collapse 的 1300-step lag 发现有独立价值\n- 不受 ACT confound 影响\n\n### §6 Analysis\n- \"The critical difference is supervision density\" 与标题/abstract 的 framing 矛盾（MF5）\n- Fisher test p 值需移除（MF1）\n- 应增加对 Papadatos & Freedman (2024) 和 SMART (2025) 的讨论（MF2, SF2）\n- ACT seed 2 数据需补完或将 claims 降级为 preliminary（MF4）\n\n### §7 Related Work\n- 缺少 Papadatos & Freedman (2024)——最关键遗漏（MF2）\n- 缺少 DPO/KTO 和 process reward models 的讨论（SF1, SF2）\n- 整体偏薄（约 1 页），对于做出广泛方法论声明的论文不够\n\n### §8 Conclusion\n- \"any alignment effort\" 的一般性声明需条件化（SF3）\n- broader lesson 应明确标注为从 sycophancy case 推广的 hypothesis\n\n### Limitations\n- 已覆盖 3 个点（单模型训练、ACT seed 2 未完成、binary evaluation），但应追加：supervision granularity confound（MF5）、引用问题（MF3）、Fisher test 局限（MF1）\n\n### References\n- 7 条 bib entry 需补全完整作者和正确 venue（MF3）\n\n### Appendix\n- Stubbornness Taxonomy 有参考价值但样本量偏小（100）\n- 大面积空白（visual check warning）建议扩充内容"
  }
}
```

</details>

---


### Tool result

_source line 97 · 2026-05-22T10:10:57.736279+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_c77a380fad2d0408ce92cd1170d46f6f:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4533
}
```

</details>

---


### Assistant

_source line 98 · 2026-05-22T10:11:06.159928+00:00_

审稿报告已投递至 Research Director。

**Round 1 圆桌审稿完成：**

- **Overall: 3.0 (Findings)**，两位 Reviewer 一致
- **5 个 Must-Fix**：Fisher test 独立性违反、遗漏 Papadatos & Freedman (2024)、引用质量、ACT 单 seed、supervision granularity confound
- **8 个 Should-Fix**：标题 overclaim、DPO/KTO 缺失、Process Reward Models、Conclusion overclaim、w1 sensitivity、AUROC CI、contrastive pairs 细节、单模型训练、仅 2 seeds
- **唯一分歧**：181 对数据量问题（R1 rebut R2，认为是质量而非数量问题）
- **最强贡献**：Probe trap (C2) 独立于 confound，有 Findings 价值
- **Issue Tracker** 已同步 15 条 issue
- **视觉审查**：2 warning（前 3 页无 display item、Appendix 大面积空白）+ 3 info

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director"
}
```

</details>

---


## Round 7

## Round 7

2 recorded events


### User

_source line 99 · 2026-05-22T10:11:08.811725+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。总结要点：

- **R1 的 3 个 Must-Fix 全部 AGREE**：Fisher test 独立性违反（N1）、ACT 单 seed（N2）、supervision granularity confound（N3）都是实质性问题
- **R1 的 6 个 Should-Fix 全部 AGREE**，其中 W1（超参数 sweep 不足）我认为严重性略低于 R1 的定位，因为 cosine gap 0.098 和 tanh 饱和是几何性质而非调参问题
- **关键判断**：R1-N3（supervision confound）与我的 R2-N1（Papadatos & Freedman 遗漏）形成互补——两者都指向同一结论：论文的 framing 过于宽泛，实际证据支持的是更窄的 claim（"sparse scalar d_syc reward 在 GRPO 中失败"），而非 "representation detection 不能用于 reward"
- **坚持 R2-N1 为 critical**：Papadatos & Freedman (2024) 是直接的成功反例，必须讨论

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 100 · 2026-05-22T10:11:22.424407+00:00_

审稿报告已投递至 Research Director。

**Round 1 审稿完成，报告摘要：**

- **Overall: 3.0 (Findings)**，两位 Reviewer 一致
- **5 个 Must-Fix**：Fisher test 独立性违反、遗漏 Papadatos & Freedman (2024) 成功案例、引用严重不完整（ACT 作者 "Unknown"）、ACT 仅单 seed 完整评估、ACT vs GRPO 存在 supervision granularity confound
- **8 个 Should-Fix**：标题 overclaim（仅测 GRPO）、缺 DPO/KTO 讨论、Process Reward Models 不足、Conclusion overclaiming、w1 仅测单值、AUROC CI 不规范、contrastive pairs 构建细节缺失、仅 2 seeds
- **唯一分歧**：181 对数据量是否偏小（R1 rebut：问题是质量控制不透明而非数量）
- **最强贡献**：Probe trap (C2) 的 behavioral-before-distributional collapse 发现，不受上述 confound 影响
- **核心建议**：将 framing 从 "d_syc fails as RL reward" 精确化为 "d_syc fails as sparse scalar GRPO reward"；完成 ACT seed 2；修复统计分析和引用

Issue Tracker 已同步至 `artifacts/review_issues.yaml`（5 critical + 8 warning + 2 info）。视觉审查已完成并纳入报告（2 warning：前 3 页无 display item、Appendix 大面积空白）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director"
}
```

</details>

---


## Round 8

## Round 8

60 recorded events


### User

_source line 101 · 2026-05-22T11:27:17.385967+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: contrastive_entrain_calib
- 论文路径: /home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: ARR May 2026
- 截止日期: 2026-05-25
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 102 · 2026-05-22T11:27:24.630638+00:00_

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
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 103 · 2026-05-22T11:27:24.631661+00:00_

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
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Read",
  "elapsed_ms": 1
}
```

</details>

---


### Tool call

_source line 104 · 2026-05-22T11:27:30.410969+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,director_post_to_reviewer,dispatch_visual_check,get_external_review_status,get_visual_check_status,request_external_review,submit_review_report_to_research_director,update_review_issues,read_project_file",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,director_post_to_reviewer,dispatch_visual_check,get_external_review_status,get_visual_check_status,request_external_review,submit_review_report_to_research_director,update_review_issues,read_project_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 105 · 2026-05-22T11:27:30.411340+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 106 · 2026-05-22T11:27:34.335644+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 107 · 2026-05-22T11:27:34.436621+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 108 · 2026-05-22T11:27:38.437644+00:00_

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
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
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

_source line 109 · 2026-05-22T11:27:38.439072+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "ToolSearch",
  "elapsed_ms": 1
}
```

</details>

---


### Tool call

_source line 110 · 2026-05-22T11:27:38.913772+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "contrastive_entrain_calib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "contrastive_entrain_calib"
  }
}
```

</details>

---


### Tool result

_source line 111 · 2026-05-22T11:27:40.298788+00:00_

{"result":"# 项目 contrastive_entrain_calib 概况\n\n## 实验状态 (76 个)\n\n- **exp-003-eval-ckpt1000**: DONE (negative) — \n- **exp-003-eval-ckpt5000**: DONE (negative) — \n- **exp-009**: DONE (negative) — \n- **exp-012**: DONE (success) — \n- **exp-002v3**: DONE (negative) — \n- **exp-008v3**: DONE (negative) — \n- **exp002v2-recalib**: DONE (negative) — \n- **exp-003-s2**: RUNNING — \n- **exp-016**: DONE (negative) — \n- **exp-014**: DONE (killed) — \n- **vanilla-baseline**: DONE (success) — \n- **exp-002v2**: DONE (killed) — \n- **exp-002**: DONE (killed) — \n- **exp-008**: DONE (killed) — \n- **exp-001**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-22\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| exp-004-s2 | ACT (SFT) seed 2 训练：验证 ACT 跨 seed 稳定性。Seed 1 (exp-004) 16/16 checkpoints > vanilla (0.170→0.301)。如果 seed 2 也展现类似 trajectory，则堵住 Reviewer \"ACT 只有 1 个 seed\" 攻击面。配置与 exp-004 完全相同，仅 seed=42→43。 | — | — | — |\n| exp-003-s2 | R3-only GRPO baseline (seed 2): training with only the external DeBERTa reward (r3_weight=1.0, r1=r2=0) provides a lower bound for ablation, isolating the contribution of contrastive direction-based rewards (R1+R2). Seed 2 (seed=43) verifies reproducibility of seed 1 results. | — | — | — |\n\n## 待处理\n- exp-003-s2-eval-ckpt3000: Eval exp-003-s2 (R3-only seed 2) checkpoint-3000 with D027 unified preset. Cross-seed reproducibility: compare with seed 1 ckpt-3000 (SYCONScore=0.095) for exact step match.（排队等待 GPU）\n- exp-003-s2-eval-ckpt2500: Eval exp-003-s2 (R3-only seed 2) checkpoint-2500 with D027 unified preset. Cross-seed reproducibility: compare with seed 1 ckpt-3000 (SYCONScore=0.095) for trajectory alignment.（排队等待 GPU）\n\n## 近期结论\n- **exp-004-s2-eval-ckpt2500** (failed): Eval exp-004-s2 (ACT seed 2) checkpoint-2500 with D027 unified preset. ← 基于 exp-004-s2\n- **exp-004-s2-eval-ckpt2000** (success): Eval exp-004-s2 (ACT seed 2) checkpoint-2000 with D027 unifie
…[truncated 1089 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1385
}
```

</details>

---


### Tool call

_source line 112 · 2026-05-22T11:27:40.299376+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 113 · 2026-05-22T11:27:40.351109+00:00_

1	\documentclass[11pt,a4paper]{article}
2	\usepackage[hyperref]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage{amsmath}
6	\usepackage{amssymb}
7	\usepackage{booktabs}
8	\usepackage{multirow}
9	\usepackage{graphicx}
10	\usepackage{xcolor}
11	\usepackage{subcaption}
12	
13	\newcommand{\dsyc}{d_{\text{syc}}}
14	\newcommand{\tof}{\text{ToF}}
15	\newcommand{\nof}{\text{NoF}}
16	\newcommand{\sycon}{\textsc{SyconScore}}
17	\newcommand{\rone}{R_1}
18	\newcommand{\rthree}{R_3}
19	
20	\title{Discriminability Without Utility: Why Sycophancy Directions Fail as Scalar RL Rewards}
21	
22	\author{Anonymous}
23	
24	\begin{document}
25	\maketitle
26	
27	\begin{abstract}
28	\input{sections/abstract}
29	\end{abstract}
30	
31	\input{sections/introduction}
32	
33	\input{sections/framework}
34	
35	\input{sections/direction_quality}
36	
37	\input{sections/cosine_failure}
38	
39	\input{sections/probe_trap}
40	
41	\input{sections/discussion}
42	
43	\input{sections/related_work}
44	
45	\input{sections/conclusion}
46	
47	\section*{Limitations}
48	\input{sections/limitations}
49	
50	\bibliography{references}
51	
52	\appendix
53	\input{sections/appendix}
54	
55	\end{document}
56	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 114 · 2026-05-22T11:27:46.050123+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 115 · 2026-05-22T11:27:46.511667+00:00_

1	Representation engineering shows that large language models encode sycophancy as a linear direction in activation space. We extract a contrastive sycophancy direction ($\dsyc$) from style-controlled pairs on two model families, achieving cross-validated AUROC $0.827$ on Qwen3-8B and $0.779$ on Llama-3-8B. We then test three $\dsyc$-based reward formulations with Group Relative Policy Optimization (GRPO) on Qwen3-8B. Every formulation fails. The cosine reward cannot separate valid revision from sycophantic capitulation in the narrow online activation gap. The probe reward creates a stubbornness trap: the model learns that never revising its answer maximizes reward, and the true-positive flip rate drops to zero within 500 steps. When we remove $\dsyc$ entirely and train with a purely behavioral reward, only 4 of 26 checkpoints across two seeds exceed vanilla, while supervised fine-tuning exceeds vanilla at every evaluated checkpoint (seed 1: 16/16; seed 2: 3/3 ongoing). Only supervised fine-tuning with dense per-token supervision succeeds. The root cause is a semantic gap between discriminability and reward utility: $\dsyc$ encodes \emph{whether} belief changed, not \emph{whether it should have}. Valid revision and sycophantic capitulation produce overlapping activations because both involve the model shifting its stated position toward the user's. A single scalar reward per completion, whether from representations or behavioral classifiers, cannot convey which belief changes are warranted. These results establish that representation geometry sufficient to detect a behavior is not automatically suitable for converting into a scalar per-completion reward signal.
2	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Read",
  "elapsed_ms": 461
}
```

</details>

---


### Tool call

_source line 116 · 2026-05-22T11:27:46.562498+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 117 · 2026-05-22T11:27:47.469240+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Representation engineering \citep{zou2023repe} reveals that large language models encode sycophancy as a linear direction in their residual streams.
5	A contrastive sycophancy direction $\dsyc$, extracted from style-controlled pairs of valid belief revision and sycophantic capitulation, achieves cross-validated AUROC $0.827$ (5-fold CV $\sigma{=}0.028$) on Qwen3-8B and $0.779$ (5-fold CV $\sigma{=}0.019$) on Llama-3-8B (\S\ref{sec:direction_quality}).
6	The direction captures evidential granularity: discriminability rises monotonically from weak-evidence pairs (AUROC 0.675) through medium (0.883) to strong (0.929), and the signal remains stable under LoRA training with cosine drift of approximately 0.96 at 500 steps.
7	These results, replicated across two architecturally distinct model families, point to an appealing possibility: if the model's representations already separate sycophantic from non-sycophantic behavior, that separation should be convertible into a scalar reward signal for reinforcement learning.
8	Sycophancy is among the most persistent alignment failures in deployed systems \citep{sharma2023sycophancy}, and a representation-level reward could complement existing behavioral approaches by targeting the internal computation rather than its surface outputs.
9	
10	This paper shows that the conversion fails, and that the failure runs deeper than the representation signal itself.
11	We test three formulations that translate $\dsyc$ into a GRPO \citep{shao2024grpo} training signal (cosine projection, binary probe, and continuous probe) across six experimental configurations; every formulation fails.
12	Cosine similarity produces a reward gap of just 0.098 between valid and sycophantic activations, too narrow to drive policy updates (\S\ref{sec:cosine_failure}).
13	Online recalibration improves the offline AUROC from 0.827 to 0.910 yet triggers mode collapse.
14	A binary probe with stopped gradients cr
…[truncated 5141 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Read",
  "elapsed_ms": 906
}
```

</details>

---


### Tool call

_source line 118 · 2026-05-22T11:27:47.469786+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/framework.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/framework.tex"
  }
}
```

</details>

---


### Tool result

_source line 119 · 2026-05-22T11:27:47.982685+00:00_

1	\section{Experimental Framework}
2	\label{sec:framework}
3	
4	\subsection{Direction Extraction}
5	\label{ssec:extraction}
6	
7	We extract a linear sycophancy direction $\dsyc$ from the residual stream using contrastive activation pairs: a \emph{valid correction} (warranted belief revision under strong evidence) and a \emph{sycophantic capitulation} (unwarranted concession under social pressure).
8	We construct 181 contrastive pairs using GPT-4.1 in a two-stage pipeline: skeleton generation followed by 3-turn dialogue completion.
9	Style matching is enforced by automated validation (response length difference ${<}10\%$, shared opening phrase ${\geq}2$ words), with up to 3 retries per pair; 19 of 200 initial pairs were discarded for failing validation.
10	Evidence strength is annotated at three levels: \emph{weak} (75 pairs; personal memory or opinion), \emph{medium} (54 pairs; brief source citation), and \emph{strong} (52 pairs; authoritative source with detailed data).
11	From the 181 paired examples (362 activations total), we compute the mean difference at target layer $\ell$:
12	\begin{equation}
13	\label{eq:dsyc}
14	\dsyc = \frac{1}{N}\sum_{i=1}^{N}\left(\mathbf{h}^{+}_i - \mathbf{h}^{-}_i\right)
15	\end{equation}
16	where $\mathbf{h}^{+}_i$ and $\mathbf{h}^{-}_i$ are residual-stream activations for the $i$-th valid and sycophantic response.
17	The target layer is selected by 5-fold cross-validated AUROC; on Qwen3-8B this yields layer 19 with AUROC $0.827$ (5-fold CV $\sigma{=}0.028$).
18	
19	\subsection{Reward Formulations}
20	\label{ssec:reward}
21	
22	GRPO \citep{shao2024grpo} ranks sampled completions by reward and updates the policy toward higher-reward outputs.
23	We define $R = w_1 \cdot \rone + w_3 \cdot \rthree$, where $\rone$ is a direction-based component and $\rthree$ is a behavioral component (DeBERTa NLI classifier scoring consistency with the ground-truth answer).
24	Three formulations translate $\dsyc$ into $\rone$:
25	\begin{itemize}
26	\item[
…[truncated 2794 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Read",
  "elapsed_ms": 512
}
```

</details>

---


### Tool call

_source line 120 · 2026-05-22T11:27:48.033546+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/direction_quality.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/direction_quality.tex"
  }
}
```

</details>

---


### Tool result

_source line 121 · 2026-05-22T11:27:48.034250+00:00_

1	\section{Direction Discriminability}
2	\label{sec:direction_quality}
3	
4	Before evaluating $\dsyc$ as a reward signal (\S\ref{sec:cosine_failure}--\S\ref{sec:probe_trap}), we first establish that it captures a genuine sycophancy-related signal in the residual stream.
5	If the direction failed to discriminate sycophantic from non-sycophantic activations, downstream reward failures would be trivially explained by poor direction quality rather than by a fundamental gap between discriminability and reward utility.
6	We evaluate discriminability along five axes: cross-validated classification accuracy, evidence-strength stratification, cross-model transfer, training stability, and probe ablation.
7	Figure~\ref{fig:direction_quality} summarizes the per-layer AUROC profiles for both models.
8	
9	\paragraph{Qwen3-8B layer-wise discriminability.}
10	We evaluate $\dsyc$ via 5-fold cross-validated AUROC on 181 style-controlled contrastive pairs (\S\ref{ssec:extraction}).
11	The direction achieves AUROC $0.827$ (5-fold CV $\sigma{=}0.028$) at its best layer (L19).
12	Discriminability emerges gradually across depth: layers L0--L8 perform near chance, statistical significance ($p < 0.01$) first appears at L16, and performance peaks at L19.
13	This gradual emergence, with the peak in the upper third of the network, suggests that sycophancy-relevant information is encoded as a late-stage representation rather than an input-level confound.
14	The direction also captures evidential granularity.
15	AUROC rises monotonically from 0.675 on weak-evidence pairs to 0.883 on medium and 0.929 on strong pairs.
16	This gradient indicates that $\dsyc$ encodes the degree of evidential warrant, not merely a binary sycophancy label.
17	
18	\paragraph{Cross-model generalization.}
19	To rule out that these results are specific to Qwen3-8B's representation geometry, we repeat the full extraction and evaluation pipeline on Llama-3-8B-Instruct.
20	Table~\ref{tab:cross_model} compares the two models.
…[truncated 3493 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 122 · 2026-05-22T11:27:48.389212+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/cosine_failure.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/cosine_failure.tex"
  }
}
```

</details>

---


### Tool result

_source line 123 · 2026-05-22T11:27:48.843285+00:00_

1	\section{Cosine \texorpdfstring{$\rone$}{R1}: Structural Failure}
2	\label{sec:cosine_failure}
3	
4	Section~\ref{sec:direction_quality} established that $\dsyc$ achieves AUROC 0.827 on Qwen3-8B.
5	We now test whether this discriminability translates into a viable GRPO reward.
6	Four configurations form a diagnostic chain (Table~\ref{tab:cosine_chain}): each resolves the failure mode of its predecessor but exposes a deeper limitation.
7	
8	\begin{table}[t]
9	\centering
10	\caption{Cosine $\rone$ failure chain on Qwen3-8B (LoRA rank$=$64, GRPO with $R = w_1 \cdot \rone + w_3 \cdot \rthree$).}
11	\label{tab:cosine_chain}
12	\begin{tabular}{lllll}
13	\toprule
14	Config & $\rone$ Formula & $w_1$ & Outcome & Root Cause \\
15	\midrule
16	F1a & $\tanh(\mathbf{h}\cdot\dsyc/20)$ & 0.25 & Gate saturation & Norm mismatch \\
17	F1b & $\cos(\mathbf{h},\, \dsyc)$ & 0.25 & $\rone \approx 0$ & Gap too small \\
18	F1c & +recalibration & 0.25 & Mode collapse & Reward discontinuity \\
19	F1d & $5\cos(\mathbf{h},\, \dsyc)$ & 0.40 & Mode collapse & $\rthree$ saturation \\
20	\bottomrule
21	\end{tabular}
22	\end{table}
23	
24	F1a uses a dot-product formulation ($\rone = \tanh(\mathbf{h} \cdot \dsyc / 20)$), but residual-stream norms exceed the direction norm by $100$--$1{,}200{\times}$, saturating the tanh gate and zeroing the gradient by step 955.
25	Switching to cosine similarity (F1b) eliminates norm dependence, yet the cosine gap between valid and sycophantic activations averages only 0.098 across layers---too narrow to generate meaningful reward contrast.
26	Online recalibration (F1c, \S\ref{ssec:recalib}) raises offline AUROC from 0.827 to 0.910 but paradoxically triggers mode collapse: the abrupt shift in $\dsyc$ at each recalibration event creates a reward discontinuity that destabilizes GRPO advantage estimates, collapsing entropy to 0.069 within 300 steps.
27	Amplifying the signal with $5{\times}$ scaling (F1d) lifts $\rone$ above the noise floor but simultaneously amplifies t
…[truncated 836 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Read",
  "elapsed_ms": 454
}
```

</details>

---


### Tool call

_source line 124 · 2026-05-22T11:27:48.843695+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/probe_trap.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/probe_trap.tex"
  }
}
```

</details>

---


### Tool result

_source line 125 · 2026-05-22T11:27:49.801491+00:00_

1	\section{The Probe Reward Trap}
2	\label{sec:probe_trap}
3	
4	The cosine formulations fail because the continuous projection of $\dsyc$ produces a gap too narrow for reward contrast.
5	A natural remedy is to discretize: train a logistic probe on $\dsyc$ and threshold its output, yielding $\rone = \mathbb{I}[P(\text{syc} \mid \mathbf{h}) < 0.5]$ (F2 in \S\ref{ssec:reward}).
6	We show that this discretization sidesteps the magnitude problem but creates a qualitatively worse failure.
7	
8	\paragraph{Differentiable probe: gradient gaming.}
9	Without stop-gradient (exp-008), the policy discovers within ${\sim}30$ steps that shifting activations away from the sycophancy cluster maximizes $\rone$ regardless of response content, producing an inverted profile ($\tof = 0.978$, $\nof = 0.006$).
10	This motivates the frozen-probe design below.
11	
12	\paragraph{Binary probe: the stubbornness trap.}
13	With stop-gradient (exp-008v3), the policy cannot game the boundary but instead exploits a deeper flaw: $\dsyc$ does not condition on input validity, so refusing to revise a wrong answer receives the same $\rone = 1$ as correctly resisting invalid pressure.
14	By step 500, $\tof$ drops to 0.000 and $\nof$ reaches 0.995, yielding $\sycon = 0$.
15	Qualitative analysis reveals distinct failure modes: \emph{sycophantic stubbornness} (24\%), where the model verbally agrees but does not change its answer; \emph{deliberation traps} (29\%), where the model identifies the correct answer but cannot commit; and evidence-graded hedging, where the model adjusts its refusal style rather than its acceptance rate (Appendix~\ref{app:taxonomy}).
16	
17	\paragraph{Behavioral death precedes distributional collapse.}
18	
19	\begin{table}[t]
20	\centering
21	\caption{Probe reward trap trajectory (exp-008v3). Behavioral death ($\tof{=}0$) occurs at step 500; entropy remains healthy until step ${\sim}1840$. Reward averages $+0.72$ throughout.}
22	\label{tab:probe_trajectory}
23	\begin{tabular}{lccccc}

…[truncated 2145 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Read",
  "elapsed_ms": 957
}
```

</details>

---


### Tool call

_source line 126 · 2026-05-22T11:27:49.802108+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 127 · 2026-05-22T11:27:50.255018+00:00_

1	\section{Analysis: Discriminability $\neq$ Reward Utility}\label{sec:discussion}
2	
3	\paragraph{Unified root cause.}
4	The failures in Sections~\ref{sec:cosine_failure} and~\ref{sec:probe_trap} trace to a single geometric limitation.
5	$\dsyc$ encodes the \emph{direction} of belief change but not its \emph{evidential warrant}: valid revision and sycophantic capitulation both shift activations toward the user's position along the same direction.
6	The two reward families expose complementary faces of this blindness.
7	Cosine $\rone$ penalizes all belief change indiscriminately; the resulting mode collapse (F1c, F1d) reflects excessive punishment of any activation shift along $\dsyc$.
8	The binary probe $\rone$ rewards all resistance regardless of input validity; the stubbornness trap ($\tof = 0$ by step 500) reflects excessive permissiveness toward activation stasis.
9	These are not independent design flaws but dual consequences of a direction that conflates the target behavior (resisting invalid challenges) with its complement (refusing valid corrections).
10	Cross-model evidence confirms the limitation extends beyond Qwen3-8B: Llama-3-8B independently achieves AUROC $0.779$ (5-fold CV $\sigma{=}0.019$) on the same contrastive pairs with the same monotonic evidence gradient, so discriminability generalizes across architectures while the semantic gap between discriminability and reward utility persists.
11	This pattern contrasts with reasoning faithfulness and safety directions~\citep{zhang2026latentgrpo}, where the behavior to suppress is geometrically distinct from the behavior to preserve along the relevant direction.
12	For sycophancy, the target and its complement occupy the same activation region; they differ only in whether external evidence warrants the belief change.
13	
14	\paragraph{GRPO stubbornness across all formulations.}
15	
16	\begin{table}[t]
17	\centering
18	\caption{Comparison of all sycophancy calibration methods on Qwen3-8B. $\sycon$ is the h
…[truncated 7519 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 128 · 2026-05-22T11:27:50.255369+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 129 · 2026-05-22T11:27:50.760126+00:00_

1	\section{Related Work}\label{sec:related_work}
2	
3	\paragraph{Representation Engineering.}
4	Linear directions in LLM residual streams encode behavioral concepts \citep{zou2023repe}; inference-time methods---ITI \citep{li2023iti}, ActAdd \citep{turner2023actadd}, CAA \citep{rimsky2024caa}---demonstrate that activation geometry suffices for behavioral control \citep{burns2023ccs}.
5	We use the same contrastive extraction as CAA but apply $\dsyc$ as an RL reward, revealing a gap that inference-time work does not encounter.
6	
7	\paragraph{Reward Design and Overoptimization.}
8	Proxy rewards diverge from true objectives under sustained optimization \citep{gao2023scaling}, and reward hacking can escalate to active tampering \citep{denison2024subterfuge}.
9	Our probe trap (\S\ref{sec:probe_trap}) is an extreme instance: the reward actively reinforces degenerate behavior rather than merely being circumvented \citep{skalse2022hacking}.
10	
11	\paragraph{Sycophancy Characterization and Mitigation.}
12	Sycophancy is pervasive in RLHF-trained assistants \citep{sharma2023sycophancy}, amplified by RLHF \citep{shapira2026amplifies}, and traceable to late-layer preference shifts \citep{wang2025internal}; mitigation approaches include synthetic data \citep{wei2024synthetic}, consistency training \citep{consistency2025bctact}, and neuron-level correction \citep{obrien2025fewbadneurons}.
13	Our analysis shows why the step from diagnosis to reward is structurally blocked: $\dsyc$ conflates warranted revision with unwarranted capitulation.
14	
15	\paragraph{Probe-Based Inference-Time Mitigation.}
16	\citet{papadatos2024probepenalties} reduce sycophancy via Best-of-N reranking with linear probe penalties (94\% probe accuracy), where the probe selects among candidates without producing gradients that update model parameters.
17	Our work reveals what happens when a comparable signal (AUROC 0.82) enters the GRPO training loop: the discriminability--utility gap is specific to gradient-b
…[truncated 1020 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Read",
  "elapsed_ms": 504
}
```

</details>

---


### Tool call

_source line 130 · 2026-05-22T11:27:50.760670+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 131 · 2026-05-22T11:27:51.213094+00:00_

1	\section{Conclusion}\label{sec:conclusion}
2	
3	This work tested whether a representation direction that detects sycophantic behavior can serve as an effective scalar reward signal.
4	We established that $\dsyc$ achieves strong offline discriminability (AUROC 0.827 on Qwen3-8B, 0.779 on Llama-3-8B), yet all three reward formulations failed across six GRPO configurations---the probe reward produced a stubbornness trap ($\tof = 0$ by step 500), and $\rthree$-only GRPO exceeded vanilla at only 4 of 26 checkpoints (15.4\% vs.\ 100\% for ACT seed 1).
5	The root cause is that $\dsyc$ encodes \emph{whether} belief changed, not \emph{whether it should have}; ACT's $\sycon = 0.301$ through dense per-token supervision confirms that the missing ingredient is token-level resolution of which belief changes are appropriate---a distinction that scalar reward compression discards.
6	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 132 · 2026-05-22T11:27:51.213632+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 133 · 2026-05-22T11:27:52.171025+00:00_

1	All RL and SFT experiments use Qwen3-8B exclusively; we validate $\dsyc$ discriminability on Llama-3-8B (AUROC $0.779$, 5-fold CV $\sigma{=}0.019$; Table~\ref{tab:cross_model}) but do not replicate training on a second model due to compute constraints (${\sim}200$ H100-equivalent hours).
2	ACT cross-seed verification is partial: seed 2 has completed 3 of 16 checkpoints at submission time (all exceeding vanilla), and full replication is ongoing.
3	Our evaluation categorizes user challenges as binary valid or invalid, whereas real-world belief revision spans a continuous spectrum of evidential strength; intermediate cases may prove easier to separate in activation space.
4	
5	A supervision granularity confound limits our causal claims: ACT uses dense per-token supervision while all GRPO variants use scalar per-completion rewards.
6	We cannot fully disentangle whether failures stem from compressing $\dsyc$ into a scalar or from the per-completion reward structure itself; the supervision density hypothesis (\S\ref{sec:discussion}) remains a hypothesis.
7	Finally, $n{=}2$ seeds for GRPO and partial seed 2 data for ACT are insufficient to establish statistical reproducibility, though qualitative patterns (oscillatory degradation, crash depth, late-stage flatness) are consistent across seeds.
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Read",
  "elapsed_ms": 957
}
```

</details>

---


### Tool call

_source line 134 · 2026-05-22T11:27:52.171557+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 135 · 2026-05-22T11:27:52.474105+00:00_

1	\section{Training Details}
2	\label{app:training}
3	
4	\paragraph{Reward weight selection.}
5	The weight $w_1$ is set by diagnostic-driven iteration: $w_1{=}0.25$ was initially chosen to down-weight the noisy cosine reward term; this was later increased to $w_1{=}0.40$ for F1d after diagnostics revealed that $w_1{=}0.25$ allowed the cosine term to contribute only ${\sim}8.3\%$ of total reward variance.
6	The empirical scaling factor in F1a ($\dsyc/20$) is a heuristic normalization; we did not find it critical to the failure modes reported.
7	
8	\paragraph{Response truncation.}
9	All GRPO experiments use \texttt{max\_completion\_length}=256, resulting in 80--84\% truncation of multi-turn responses.
10	This setting is shared across all conditions and does not affect relative comparisons; we retain it because response-level decisions typically manifest within the first 100--200 tokens.
11	
12	\section{Stubbornness Taxonomy}
13	\label{app:taxonomy}
14	
15	Manual inspection of 100 probe-trained responses (exp-008v3, step 2000) reveals three dominant failure modes.
16	\emph{Sycophantic stubbornness} (24\%): the model produces agreement markers (``you're right,'' ``good point'') but retains its original answer verbatim, simultaneously sycophantic and stubborn.
17	\emph{Deliberation traps} (29\%): the model explicitly identifies the correct revised answer during its reasoning chain but fails to commit, reverting to the original answer in the final output.
18	\emph{Evidence-graded hedging}: under weak evidence, responses show surface compliance without substantive change; under strong evidence, responses add explicit hedging (``this is debatable,'' ``there are multiple perspectives'').
19	The model learns to modulate its \emph{refusal style} in response to evidence strength rather than adjusting its \emph{acceptance rate}, confirming that the probe reward optimizes surface markers rather than epistemic calibration.
20	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Read",
  "elapsed_ms": 302
}
```

</details>

---


### Tool call

_source line 136 · 2026-05-22T11:27:52.524971+00:00_

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
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 ARR call for papers submission guidelines author instructions"
  }
}
```

</details>

---


### Tool result

_source line 137 · 2026-05-22T11:28:01.677167+00:00_

Web search results for query: "EMNLP 2026 ARR call for papers submission guidelines author instructions"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Submission Guide","url":"https://nlp4climate.github.io/submissionguide/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"}]

Based on the search results, here's a comprehensive overview of the EMNLP 2026 ARR submission guidelines and author instructions:

## Submission Process

EMNLP 2026 uses ACL Rolling Review (ARR) as its reviewing system, with a two-step process where authors submit articles to ARR for review and then commit their reviewed articles to the conference. Submissions are performed via the Open Review 
…[truncated 1577 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "WebSearch",
  "elapsed_ms": 9152
}
```

</details>

---


### Tool call

_source line 138 · 2026-05-22T11:28:16.916022+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "contrastive_entrain_calib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "contrastive_entrain_calib"
  }
}
```

</details>

---


### Tool result

_source line 139 · 2026-05-22T11:28:17.922094+00:00_

{"result":"# 项目 contrastive_entrain_calib 概况\n\n## 实验状态 (76 个)\n\n- **exp-003-eval-ckpt1000**: DONE (negative) — \n- **exp-003-eval-ckpt5000**: DONE (negative) — \n- **exp-009**: DONE (negative) — \n- **exp-012**: DONE (success) — \n- **exp-002v3**: DONE (negative) — \n- **exp-008v3**: DONE (negative) — \n- **exp002v2-recalib**: DONE (negative) — \n- **exp-003-s2**: RUNNING — \n- **exp-016**: DONE (negative) — \n- **exp-014**: DONE (killed) — \n- **vanilla-baseline**: DONE (success) — \n- **exp-002v2**: DONE (killed) — \n- **exp-002**: DONE (killed) — \n- **exp-008**: DONE (killed) — \n- **exp-001**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-22\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| exp-004-s2 | ACT (SFT) seed 2 训练：验证 ACT 跨 seed 稳定性。Seed 1 (exp-004) 16/16 checkpoints > vanilla (0.170→0.301)。如果 seed 2 也展现类似 trajectory，则堵住 Reviewer \"ACT 只有 1 个 seed\" 攻击面。配置与 exp-004 完全相同，仅 seed=42→43。 | — | — | — |\n| exp-003-s2 | R3-only GRPO baseline (seed 2): training with only the external DeBERTa reward (r3_weight=1.0, r1=r2=0) provides a lower bound for ablation, isolating the contribution of contrastive direction-based rewards (R1+R2). Seed 2 (seed=43) verifies reproducibility of seed 1 results. | — | — | — |\n\n## 待处理\n- exp-003-s2-eval-ckpt3000: Eval exp-003-s2 (R3-only seed 2) checkpoint-3000 with D027 unified preset. Cross-seed reproducibility: compare with seed 1 ckpt-3000 (SYCONScore=0.095) for exact step match.（排队等待 GPU）\n- exp-003-s2-eval-ckpt2500: Eval exp-003-s2 (R3-only seed 2) checkpoint-2500 with D027 unified preset. Cross-seed reproducibility: compare with seed 1 ckpt-3000 (SYCONScore=0.095) for trajectory alignment.（排队等待 GPU）\n\n## 近期结论\n- **exp-004-s2-eval-ckpt2500** (failed): Eval exp-004-s2 (ACT seed 2) checkpoint-2500 with D027 unified preset. ← 基于 exp-004-s2\n- **exp-004-s2-eval-ckpt2000** (success): Eval exp-004-s2 (ACT seed 2) checkpoint-2000 with D027 unifie
…[truncated 1089 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1006
}
```

</details>

---


### Tool call

_source line 140 · 2026-05-22T11:28:17.922566+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 submission format page limit anonymity policy style files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 submission format page limit anonymity policy style files"
  }
}
```

</details>

---


### Tool call

_source line 141 · 2026-05-22T11:28:18.073290+00:00_

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
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
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

_source line 142 · 2026-05-22T11:28:18.123854+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 143 · 2026-05-22T11:28:24.052702+00:00_

Web search results for query: "ACL Rolling Review 2026 submission format page limit anonymity policy style files"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Submissions | Transactions of the Association for Computational Linguistics","url":"https://transacl.org/index.php/tacl/about/submissions"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"Industry Track — Call for Papers @ EACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/industry-track-call-papers-eacl-2026"},{"title":"Paper formatting guidelines - ACLPUB","url":"https://acl-org.github.io/ACLPUB/formatting.html"}]

Based on the search results, here's what I found regarding ACL Rolling Review 2026 submission guidelines:

## Page Limits

Long papers may have up to 8 pages of content, and short papers up to 4 pages, excluding ethical considerations and limitations. Upon acceptance, final versions of long papers will be given one additional page – up to nine (9) pages of content plus unlimited pages for acknowledgments and references.

##
…[truncated 1011 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "WebSearch",
  "elapsed_ms": 6130
}
```

</details>

---


### Tool call

_source line 144 · 2026-05-22T11:28:28.176058+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review_issues.yaml",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review_issues.yaml",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib"
  }
}
```

</details>

---


### Tool result

_source line 145 · 2026-05-22T11:28:28.627738+00:00_

/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_issues.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Glob",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 146 · 2026-05-22T11:28:29.180894+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/submitted.pdf",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/submitted.pdf",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib"
  }
}
```

</details>

---


### Tool result

_source line 147 · 2026-05-22T11:28:29.834025+00:00_

/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_1/submitted.pdf
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_2/submitted.pdf

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Glob",
  "elapsed_ms": 653
}
```

</details>

---


### Tool call

_source line 148 · 2026-05-22T11:28:29.884578+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 149 · 2026-05-22T11:28:29.885309+00:00_

1	@article{zhang2026latentgrpo,
2	  title={Silence the Judge: Reinforcement Learning with Self-Verifier via Latent Geometric Clustering},
3	  author={Zhang, Nonghai and Ma, Weitao and Ma, Zhanyu and Xu, Jun and Gao, Jiuchong and Hao, Jinghua and He, Renqing and Xu, Jingwen},
4	  journal={arXiv preprint arXiv:2601.08427},
5	  year={2026}
6	}
7	
8	@article{zou2023repe,
9	  title={Representation Engineering: A Top-Down Approach to {AI} Transparency},
10	  author={Zou, Andy and Phan, Long and Chen, Sarah and Campbell, James and Guo, Phillip and Ren, Richard and Pan, Alexander and Yin, Xuwang and Mazeika, Mantas and Dombrowski, Ann-Kathrin and Gould, Shashwat and Li, Zifan and Xie, Chuanqi and Leung, Alexandria and Hase, Peter and Hendrycks, Dan},
11	  journal={arXiv preprint arXiv:2310.01405},
12	  year={2023}
13	}
14	
15	@inproceedings{rimsky2024caa,
16	  title={Steering Llama 2 via Contrastive Activation Addition},
17	  author={Rimsky, Nina and Gabrieli, Nick and Schulz, Jenna and Smith, Meg and Tong, Ioannis and Hubinger, Evan},
18	  booktitle={Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (ACL)},
19	  year={2024}
20	}
21	
22	@article{shao2024grpo,
23	  title={DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models},
24	  author={Shao, Zhihong and Wang, Peiyi and Zhu, Qihao and Xu, Runxin and Song, Junxiao and Zhang, Mingchuan and Li, Y.K. and Wu, Y. and Guo, Daya},
25	  journal={arXiv preprint arXiv:2402.03300},
26	  year={2024}
27	}
28	
29	@inproceedings{li2023iti,
30	  title={Inference-Time Intervention: Eliciting Truthful Answers from a Language Model},
31	  author={Li, Kenneth and Patel, Oam and Vi{\'e}gas, Fernanda and Pfister, Hanspeter and Wattenberg, Martin},
32	  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},
33	  year={2023}
34	}
35	
36	@article{turner2023actadd,
37	  title={Steering Language Models With Activation Engineering},
38	  author={Turner, Alexander Mat
…[truncated 6645 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 150 · 2026-05-22T11:28:36.369135+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 151 · 2026-05-22T11:28:36.420029+00:00_

1	issues:
2	  - id: R1-N1
3	    summary: "Fisher exact test 将非独立 checkpoints 当独立样本，p<0.0001 不可信"
4	    category: method
5	    severity: critical
6	    status: in_progress
7	    first_raised_round: 1
8	    last_seen_round: 1
9	    mentions:
10	      - round: 1
11	        reviewers: [1, 2]
12	        note: "R1 首提，R2 完全同意。定性结论从轨迹图可直接观察，p 值赋予虚假统计权威性。"
13	    action_items:
14	      - round: 1
15	        action: "移除所有 Fisher p 值（Abstract/Intro/§6/Discussion），改为 run-level 描述性统计"
16	        assigned_to: paper_agent
17	        status: queued
18	    resolution: ""
19	    resolution_round: null
20	
21	  - id: R2-N1
22	    summary: "遗漏 Papadatos & Freedman (2024) probe penalty 成功案例，直接挑战核心 thesis"
23	    category: framing
24	    severity: critical
25	    status: in_progress
26	    first_raised_round: 1
27	    last_seen_round: 1
28	    mentions:
29	      - round: 1
30	        reviewers: [1, 2]
31	        note: "R2 首提，R1 交叉同意。论文必须讨论 probe penalty (RM 内部) vs probe reward (GRPO scalar) 的关键差异。"
32	    action_items:
33	      - round: 1
34	        action: "Agent WebSearch 读 Papadatos & Freedman (2024) 确认方法细节，Paper Agent 在 §7 新增专段 + §6 补讨论"
35	        assigned_to: agent+paper_agent
36	        status: queued
37	    resolution: ""
38	    resolution_round: null
39	
40	  - id: R2-N2
41	    summary: "references.bib 多条引用严重不完整：ACT 作者为 Unknown，6 条仅 et al."
42	    category: format
43	    severity: critical
44	    status: in_progress
45	    first_raised_round: 1
46	    last_seen_round: 1
47	    mentions:
48	      - round: 1
49	        reviewers: [1, 2]
50	        note: "ACT 是唯一成功 baseline，Unknown 作者使读者无法验证方法来源。可能触发 ARR desk-rejection。"
51	    action_items:
52	      - round: 1
53	        action: "Agent WebSearch 补全所有 7 条 bib entry 的完整作者、标题、venue"
54	        assigned_to: agent
55	        status: queued
56	    resolution: ""
57	    resolution_round: null
58	
59	  - id: R1-N2
60	    summary: "ACT 正面结果仅基于单 seed 完整评估（seed 2 仅 3/16 checkpoints）"
61	    category: experiment
62	    severity: critical
63	 
…[truncated 8216 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 152 · 2026-05-22T11:29:20.972949+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "contrastive_entrain_calib",
  "review_chat_id": "oc_056796cf71f839be40019e5f1a11791b"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "contrastive_entrain_calib",
    "review_chat_id": "oc_056796cf71f839be40019e5f1a11791b"
  }
}
```

</details>

---


### Tool call

_source line 153 · 2026-05-22T11:29:21.424943+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "contrastive_entrain_calib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "contrastive_entrain_calib"
  }
}
```

</details>

---


### Tool result

_source line 154 · 2026-05-22T11:29:42.525578+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 21552
}
```

</details>

---


### Tool result

_source line 155 · 2026-05-22T11:29:42.526178+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 21101
}
```

</details>

---


### Tool call

_source line 156 · 2026-05-22T11:29:42.576798+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "contrastive_entrain_calib",
  "text": "你是 Reviewer 1，负责**方法严谨性**审查。\n\n## Venue 信息\n- **目标会议**: EMNLP 2026（通过 ARR May 2026 cycle 提交）\n- **截止日期**: 2026-05-25\n- **页数限制**: 正文 8 页（Long paper），参考文献不限页数，Limitations 和 Ethics 不计入页数\n- **模板**: ACL style（`\\usepackage[hyperref]{acl}`）\n- **匿名规则**: Double-blind，论文中不得包含作者信息\n- **评分标准**: ARR Overall Assessment: 5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 论文路径\n- LaTeX 源码: `/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_2/submitted.pdf`\n\n## 你的审查侧重：方法严谨性\n\n请重点审查以下方面：\n\n1. **Direction extraction 方法**（§2.1）：\n   - Contrastive pairs 的构建方法是否严谨？style-controlled 过程是否充分说明？\n   - 181 pairs 的规模是否足够？evidence strength 三级标注标准是否清晰？\n   - 5-fold cross-validated AUROC 的统计报告是否合理？\n\n2. **Reward formulations**（§2.2）：\n   - 三种 R1 公式（cosine、binary probe、continuous probe）的设计和参数选择是否合理？\n   - 超参数 w1（仅测 0.25/0.40）是否足以排除 false negative？\n   - Online recalibration 的设计是否有替代方案未探索？\n\n3. **实验设计与统计声明**（§3-§6）：\n   - 所有训练仅在 Qwen3-8B 上进行，Llama-3-8B 仅做 direction 验证——这是否足以支撑论文的一般性声明？\n   - ACT seed 2 仅 3/16 checkpoints 完成——对结论可靠性有何影响？\n   - Cross-seed 分析（n=2 seeds）统计效力如何？\n   - NLI flip classifier 的可靠性是否有充分验证？\n   - max_completion_length=256 导致 80-84% truncation 是否影响结果有效性？\n\n4. **因果推断**（§6）：\n   - ACT vs GRPO 对比是否存在 supervision granularity confound（per-token vs per-completion）？\n   - \"supervision density hypothesis\" 是否过度 claim？\n   - 论文是否正确区分了\"d_syc 作为 reward 失败\"和\"scalar per-completion reward 结构性不足\"？\n\n5. **评估指标**：\n   - SyconScore 的 harmonic mean 设计选择是否有理据？\n   - ToF/NoF 分类依赖 DeBERTa NLI，准确率是否报告？\n\n请按 ARR 标准给出完整审稿报告：Summary → Strengths → Weaknesses（区分 Must-Fix / Should-Fix / Minor） → Questions → Missing References → Overall Assessment（含评分和置信度）。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "contrastive_entrain_calib",
    "text": "你是 Reviewer 1，负责**方法严谨性**审查。\n\n## Venue 信息\n- **目标会议**: EMNLP 2026（通过 ARR May 2026 cycle 提交）\n- **截止日期**: 2026-05-25\n- **页数限制**: 正文 8 页（Long paper），参考文献不限页数，Limitations 和 Ethics 不计入页数\n- **模板**: ACL style（`\\usepackage[hyperref]{acl}`）\n- **匿名规则**: Double-blind，论文中不得包含作者信息\n- **评分标准**: ARR Overall Assessment: 5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 论文路径\n- LaTeX 源码: `/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_2/submitted.pdf`\n\n## 你的审查侧重：方法严谨性\n\n请重点审查以下方面：\n\n1. **Direction extraction 方法**（§2.1）：\n   - Contrastive pairs 的构建方法是否严谨？style-controlled 过程是否充分说明？\n   - 181 pairs 的规模是否足够？evidence strength 三级标注标准是否清晰？\n   - 5-fold cross-validated AUROC 的统计报告是否合理？\n\n2. **Reward formulations**（§2.2）：\n   - 三种 R1 公式（cosine、binary probe、continuous probe）的设计和参数选择是否合理？\n   - 超参数 w1（仅测 0.25/0.40）是否足以排除 false negative？\n   - Online recalibration 的设计是否有替代方案未探索？\n\n3. **实验设计与统计声明**（§3-§6）：\n   - 所有训练仅在 Qwen3-8B 上进行，Llama-3-8B 仅做 direction 验证——这是否足以支撑论文的一般性声明？\n   - ACT seed 2 仅 3/16 checkpoints 完成——对结论可靠性有何影响？\n   - Cross-seed 分析（n=2 seeds）统计效力如何？\n   - NLI flip classifier 的可靠性是否有充分验证？\n   - max_completion_length=256 导致 80-84% truncation 是否影响结果有效性？\n\n4. **因果推断**（§6）：\n   - ACT vs GRPO 对比是否存在 supervision granularity confound（per-token vs per-completion）？\n   - \"supervision density hypothesis\" 是否过度 claim？\n   - 论文是否正确区分了\"d_syc 作为 reward 失败\"和\"scalar per-completion reward 结构性不足\"？\n\n5. **评估指标**：\n   - SyconScore 的 harmonic mean 设计选择是否有理据？\n   - ToF/NoF 分类依赖 DeBERTa NLI，准确率是否报告？\n\n请按 ARR 标准给出完整审稿报告：Summary → Strengths → Weaknesses（区分 Must-Fix / Should-Fix / Minor） → Questions → Missing References → Overall Assessment（含评分和置信度）。"
  }
}
```

</details>

---


### Tool result

_source line 157 · 2026-05-22T11:30:00.494134+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 17917
}
```

</details>

---


### Tool call

_source line 158 · 2026-05-22T11:30:00.847184+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "contrastive_entrain_calib",
  "text": "你是 Reviewer 2，负责**新颖性与完整性**审查。\n\n## Venue 信息\n- **目标会议**: EMNLP 2026（通过 ARR May 2026 cycle 提交）\n- **截止日期**: 2026-05-25\n- **页数限制**: 正文 8 页（Long paper），参考文献不限页数，Limitations 和 Ethics 不计入页数\n- **模板**: ACL style（`\\usepackage[hyperref]{acl}`）\n- **匿名规则**: Double-blind，论文中不得包含作者信息\n- **评分标准**: ARR Overall Assessment: 5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 论文路径\n- LaTeX 源码: `/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_2/submitted.pdf`\n\n## 你的审查侧重：新颖性与完整性\n\n请重点审查以下方面：\n\n1. **Contribution 新颖性**：\n   - \"discriminability ≠ reward utility\" 这一核心 insight 是否有足够的新颖性？是否已有先验工作（如 reward overoptimization/hacking literature）间接建立了类似结论？\n   - Probe reward trap（C2）——behavioral death precedes distributional collapse——是否为真正的新发现？\n   - 对 representation engineering + RL 社区的实际价值如何？\n\n2. **Related Work 完整性**（§7）：\n   - 是否遗漏重要相关工作？特别关注：\n     - Papadatos & Freedman (2024) probe penalty via Best-of-N——论文是否充分讨论了 inference-time vs training-time probe 的差异？\n     - SMART (Beigi et al., 2025) per-step process rewards——作为 sparse scalar 和 dense SFT 之间的中间方案，讨论是否充分？\n     - CRAFT (Luo et al., 2026) 和 Latent-GRPO (Zhang et al., 2026)——每个是否有足够的讨论篇幅？\n     - DPO/KTO 作为 pair-wise 替代方案——是否充分讨论了为何它们可能绕过 scalar reward 问题？\n   - 引用是否完整准确？references.bib 是否有不完整条目？\n\n3. **Framing 与 Scope**：\n   - 标题 \"Discriminability Without Utility: Why Sycophancy Directions Fail as Scalar RL Rewards\" 是否准确反映论文内容？\n   - \"Scalar RL Rewards\" 的限定是否足够？论文是否有 overclaim（如将结论推广到所有 RL 方法或所有 alignment 场景）？\n   - Abstract 和 Introduction 中的 contribution 声明是否与实验证据匹配？\n\n4. **写作质量**：\n   - 论文结构是否清晰？叙事逻辑（direction quality → cosine failure → probe trap → R3-only failure → ACT success）是否有说服力？\n   - Conclusion 是否有 overclaiming？\n   - Limitations 是否充分且诚实？\n   - 是否有格式问题（匿名性、页数、引用格式）？\n\n5. **Reproducibility**：\n   - 论文是否提供足够的细节让他人复现实验？\n   - 数据集（181 contrastive pairs）的构建过程是否可复现？\n   - 代码/数据可用性声明？\n\n请按 ARR 标准给出完整审稿报告：Summary → Strengths → Weaknesses（区分 Must-Fix / Should-Fix / Minor） → Questions → Missing References → Overall Assessment（含评分和置信度）。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "contrastive_entrain_calib",
    "text": "你是 Reviewer 2，负责**新颖性与完整性**审查。\n\n## Venue 信息\n- **目标会议**: EMNLP 2026（通过 ARR May 2026 cycle 提交）\n- **截止日期**: 2026-05-25\n- **页数限制**: 正文 8 页（Long paper），参考文献不限页数，Limitations 和 Ethics 不计入页数\n- **模板**: ACL style（`\\usepackage[hyperref]{acl}`）\n- **匿名规则**: Double-blind，论文中不得包含作者信息\n- **评分标准**: ARR Overall Assessment: 5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 论文路径\n- LaTeX 源码: `/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_2/submitted.pdf`\n\n## 你的审查侧重：新颖性与完整性\n\n请重点审查以下方面：\n\n1. **Contribution 新颖性**：\n   - \"discriminability ≠ reward utility\" 这一核心 insight 是否有足够的新颖性？是否已有先验工作（如 reward overoptimization/hacking literature）间接建立了类似结论？\n   - Probe reward trap（C2）——behavioral death precedes distributional collapse——是否为真正的新发现？\n   - 对 representation engineering + RL 社区的实际价值如何？\n\n2. **Related Work 完整性**（§7）：\n   - 是否遗漏重要相关工作？特别关注：\n     - Papadatos & Freedman (2024) probe penalty via Best-of-N——论文是否充分讨论了 inference-time vs training-time probe 的差异？\n     - SMART (Beigi et al., 2025) per-step process rewards——作为 sparse scalar 和 dense SFT 之间的中间方案，讨论是否充分？\n     - CRAFT (Luo et al., 2026) 和 Latent-GRPO (Zhang et al., 2026)——每个是否有足够的讨论篇幅？\n     - DPO/KTO 作为 pair-wise 替代方案——是否充分讨论了为何它们可能绕过 scalar reward 问题？\n   - 引用是否完整准确？references.bib 是否有不完整条目？\n\n3. **Framing 与 Scope**：\n   - 标题 \"Discriminability Without Utility: Why Sycophancy Directions Fail as Scalar RL Rewards\" 是否准确反映论文内容？\n   - \"Scalar RL Rewards\" 的限定是否足够？论文是否有 overclaim（如将结论推广到所有 RL 方法或所有 alignment 场景）？\n   - Abstract 和 Introduction 中的 contribution 声明是否与实验证据匹配？\n\n4. **写作质量**：\n   - 论文结构是否清晰？叙事逻辑（direction quality → cosine failure → probe trap → R3-only failure → ACT success）是否有说服力？\n   - Conclusion 是否有 overclaiming？\n   - Limitations 是否充分且诚实？\n   - 是否有格式问题（匿名性、页数、引用格式）？\n\n5. **Reproducibility**：\n   - 论文是否提供足够的细节让他人复现实验？\n   - 数据集（181 contrastive pairs）的构建过程是否可复现？\n   - 代码/数据可用性声明？\n\n请按 ARR 标准给出完整审稿报告：Summary → Strengths → Weaknesses（区分 Must-Fix / Should-Fix / Minor） → Questions → Missing References → Overall Assessment（含评分和置信度）。"
  }
}
```

</details>

---


### Tool result

_source line 159 · 2026-05-22T11:30:02.649400+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1802
}
```

</details>

---


### Assistant

_source line 160 · 2026-05-22T11:30:14.321522+00:00_

Round 2 圆桌审稿已启动（fresh 模式，当作初审处理）：

| 任务 | 状态 |
|------|------|
| Reviewer 1（方法严谨性） | ✅ 已派发，等待回复 |
| Reviewer 2（新颖性/完整性） | ✅ 已派发，等待回复 |
| 视觉审查 Agent | ✅ 已启动，fire-and-forget |
| 外部审稿（Stanford Agentic Reviewer） | ⏭️ 未配置，跳过 |

**Venue 确认**（实时搜索）：EMNLP 2026 via ARR May 2026 cycle，正文 8 页限制，ACL 模板，double-blind。Deadline 2026-05-25，距今 3 天。本轮 ARR 同时服务 EMNLP 和 AACL，投稿时需选择目标会议。

等待两位 Reviewer 独立初审结果返回后，进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director"
}
```

</details>

---


## Round 9

## Round 9

2 recorded events


### User

_source line 161 · 2026-05-22T11:34:34.033701+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 审稿报告：方法严谨性审查

**论文标题**: Discriminability Without Utility: Why Sycophancy Directions Fail as Scalar RL Rewards
**Venue**: EMNLP 2026 (ARR May 2026 cycle)
**审查侧重**: 方法严谨性

---

## Paper Summary

本文研究对比提取的 sycophancy direction (d_syc) 能否作为 GRPO 的标量 reward 信号来校准 LLM 的 sycophancy 行为。作者在 Qwen3-8B 上提取 d_syc（5-fold CV AUROC 0.827），测试三种 reward 公式（cosine projection、binary probe、continuous probe）共六种配置，结果全部失败。论文进一步展示 R3-only GRPO（仅用 NLI 行为 reward）也失败（26 个 checkpoint 仅 4 个超过 vanilla），而 ACT（dense per-token SFT）以 SyconScore 0.301 成功。核心论点是 d_syc 编码了"是否发生信念变化"而非"信念变化是否有证据支撑"，且标量 per-completion reward 结构性地无法传达 valid/invalid 区分。

---

## Summary of Strengths

**S1. 问题选取极佳，填补重要空白。** representation engineering 的线性方向能否直接转化为 RL reward？这是社区普遍假设但未被系统检验的前提。本文是首个在 sycophancy 校准上系统否证该前提的工作，具有重要理论意义。

**S2. 诊断链设计严谨且有教学价值。** §4 的 cosine failure chain（F1a→F1b→F1c→F1d）是一个精心设计的渐进式消融，每一步解决前一步的 failure mode 但暴露更深层问题。这种叙事结构使论文的论证逻辑非常清晰。

**S3. Probe reward trap 的发现有实际安全意义。** behavioral death（ToF=0 at step 500）先于 distributional collapse（entropy collapse at step ~1840）的 1300-step 时间差，且 reward 始终保持 +0.72——这意味着标准的 entropy-based early stopping 会完全错过行为退化。这对 RLHF 安全监控实践有直接启示。

**S4. Limitations 写作诚实。** 论文在 Limitations 中主动承认了多项关键局限（单模型训练、ACT seed 2 不完整、n=2 seeds 的统计效力、supervision granularity confound）。这种透明性值得肯定。

**S5. Cross-model direction validation 增强了 d_syc 分析的可信度。** 在 Llama-3-8B 上独立复现了 direction extraction，evidence-strength gradient 的定性模式一致，表明 d_syc 的几何性质不是模型特异的。

---

## Must-Fix 问题（影响接收决定）

**N1 [critical] ACT vs GRPO 对比存在多重混淆变量，"supervision density hypothesis" 过度声称**

- 具体位置：§6 "The supervision density hypothesis" 段落；Introduction C3；Conclusion
- 问题：论文将 ACT 的成功归因于 "supervision density"（per-token vs per-completion），但 ACT 和 GRPO 至少在以下维度同时不同：
  - (a) per-token vs per-completion 梯度粒度
  - (b) SFT（交叉熵）vs RL（REINFORCE/GRPO）目标函数
  - (c) ACT 使用 labeled valid/invalid pairs（有标签监督），GRPO 使用 sampled completions（无标签）
  - (d) ACT 额外包含 L2 activation consistency loss
  
  当至少有 4 个同时变化的因素时，将因果归因到 "supervision density" 这一个维度上是不合理的。ACT 的成功可能主要因为它使用了 **labeled examples**（直接告诉模型哪些 belief change 是 warranted 的），而不是因为 per-token supervision。论文在 Limitations 中承认了这一 confound，但正文（尤其 Introduction C3 和 Conclusion）的措辞远比 Limitations 中的 hedge 更强。
  
  §6 最后一句"we expect similar failure patterns wherever representation-derived signals are compressed to completion-level scalars"——这是从单一模型、单一 RL 算法的实验外推到整个 per-completion RL 方法类别的推测性声称。

- 为什么影响接收：C3 是论文三个 contribution 之一。如果 ACT 的优势来自 labeled supervision 而非 supervision density，论文的核心叙事（discriminability ≠ utility, 且 sparse reward 结构性不足）的第二层（sparse reward 不足）就不成立。
  
- 建议修改方向：
  - 明确列出 ACT 与 GRPO 的所有差异维度，并在正文（不只是 Limitations）中讨论替代解释
  - 将 "supervision density hypothesis" 降级为多个可能解释之一，而非论文的核心 contribution
  - 增加消融实验以隔离因素：例如 (1) per-token RL（如 token-level GRPO/PPO）vs per-completion GRPO，(2) 使用 labeled pairs 的 GRPO（而非 sampled completions）
  - 或者将 C3 重新表述为观察性发现而非因果声称

**N2 [critical] 实验仅在 Qwen3-8B 上训练，不足以支撑论文的一般性声称**

- 具体位置：Title（"Why Sycophancy Directions Fail as Scalar RL Rewards"——一般性陈述）；Introduction（"scalar per-completion RL is structurally insufficient for sycophancy calibration"）；§6（"the scalar per-completion reward structure is shared by PPO, RLOO, and other REINFORCE-style methods"）
- 问题：所有 RL 和 SFT 训练实验仅在 Qwen3-8B 一个模型上进行。Llama-3-8B 仅用于 direction extraction 验证，未进行任何训练实验。论文标题和正文使用一般性措辞（"sycophancy directions fail"、"structurally insufficient"），但仅有单模型证据。
  
  更重要的是，GRPO 的 failure modes 可能与 Qwen3-8B 的特定特性有关（如 residual stream 的几何结构、RL 训练动态），在其他模型上可能表现不同。论文自身展示了两个模型的 d_syc 最佳层不同（L19 vs L16）、AUROC 不同（0.827 vs 0.779），这暗示模型间的差异可能影响训练动态。

- 为什么影响接收：标题和核心 claim 的一般性远超实验证据的范围。ARR 指南明确要求 "claims match the evaluation scope"（R2）。
  
- 建议修改方向：
  - 在标题或 abstract 中明确限定实验范围（"on Qwen3-8B" 或 "a case study"）
  - 在 Llama-3-8B 上至少复现一个关键实验（如 binary probe F2）以测试跨模型一致性
  - 或将一般性声称显著软化：从 "fail" → "failed in our experiments"；从 "structurally insufficient" → "insufficient in the tested configuration"

**N3 [critical] 统计效力严重不足：n=2 seeds、ACT seed 2 仅 3/16 checkpoints**

- 具体位置：Table 4（主对比表）；§6（cross-seed analysis）；Limitations
- 问题：
  - GRPO 使用 n=2 seeds。论文报告了 cross-seed rank correlation 在 step 4000 后降至 ρ≈0.33 (n.s.)，但 n=2 的相关性几乎没有任何统计意义——任何两条随机曲线都可能在某些区间有高相关。
  - ACT seed 2 仅完成 3/16 checkpoints。Table 4 将 ACT seed 1 的完整结果（16/16 checkpoints 全部超过 vanilla）作为核心证据，但仅有 1 个完整 seed。3/16 的部分数据被标注为 "ongoing"，这意味着论文在实验未完成时就提交了。
  - "4/26 checkpoints (15.4%) exceed vanilla" vs "16/16 (100%)" 的对比在统计上并不如看起来那么有力：不同方法在不同 training stages 有不同 dynamics，逐 checkpoint 比较忽略了时间序列的自相关性。

- 为什么影响接收：ARR 指南要求 "appropriate information about statistical significance"（R5）。n=2 seeds 的 cross-seed 分析、incomplete seed 2 数据、以及缺乏置信区间或显著性检验的主对比，都低于会议论文的标准。

- 建议修改方向：
  - 至少增加到 n=3 seeds（GRPO 和 ACT 各 3 seeds），报告 mean±std
  - 完成 ACT seed 2 的全部 16 checkpoints 评估
  - 对 Table 4 的关键对比（如 GRPO best vs ACT best）报告置信区间或 bootstrap test
  - 如果计算资源不足以增加 seeds，应在正文中大幅软化比较性声称

---

## Should-Fix 问题（影响评分但不一票否决）

**W1 [warning] max_completion_length=256 导致 80-84% truncation，可能系统性偏倚结果**

- 具体位置：Appendix A（Response truncation）
- 问题：所有 GRPO 实验使用 max_completion_length=256，导致 80-84% 的 multi-turn responses 被截断。论文声称 "this setting is shared across all conditions and does not affect relative comparisons"，以及 "response-level decisions typically manifest within the first 100-200 tokens"。
  
  但这两个辩护都有问题。首先，截断对不同 reward formulation 的影响可能不同：binary probe 只需看 final representation（受截断影响小），而 cosine reward 依赖于 activation 的连续变化（可能更受截断影响）。其次，"decisions manifest within 100-200 tokens" 是一个未验证的断言。一个正在进行 nuanced belief revision 的模型可能需要更多 token 来表达，而简单拒绝修改只需很少 token——截断可能系统性地惩罚 warranted revision。

- 建议：(1) 在至少一个配置上测试 max_completion_length=512 或更高，验证截断不影响 failure modes 的定性结论；(2) 提供截断对 ToF vs NoF responses 的差异化影响分析。

**W2 [warning] NLI 分类器同时用于 R3 reward 和 ToF/NoF 评估，存在评估循环性**

- 具体位置：§2.5（Evaluation）——使用 DeBERTa NLI 做 stance classification；§2.2——R3 也是 DeBERTa NLI classifier
- 问题：R3 reward component 使用 DeBERTa NLI 判断模型回答与 ground truth 的一致性；ToF/NoF 评估也使用同一个 DeBERTa NLI classifier（cross-encoder/nli-deberta-v3-base）判断 stance flip。这创造了一个评估循环：训练用 NLI classifier 给 reward → 用同一个 classifier 衡量 outcome。
  
  论文报告了 MNLI mismatched accuracy 90.0% 和 SNLI test 92.4%，但这是通用 NLI benchmark 上的表现。在 sycophancy-specific 的 stance flip 判断任务上，该 classifier 的准确率是多少？有没有在标注样本上验证过？

- 建议：(1) 在 sycophancy-specific 样本上报告 NLI classifier 的准确率（例如手动标注 100 个样本做 gold standard）；(2) 讨论 training reward 和 evaluation metric 使用相同 classifier 的潜在循环性问题。

**W3 [warning] 超参搜索不充分：w1 仅测试 0.25 和 0.40**

- 具体位置：Table 2（Cosine R1 failure chain）；Appendix A
- 问题：reward weight w1 仅测试了两个值（0.25 和 0.40），且采用 "diagnostic-driven iteration" 而非系统搜索。论文声称所有 cosine formulation 都失败，但仅从两个 weight 值的实验中无法排除存在有效配置的可能性。
  
  具体来说，F1b 的 cosine gap 仅 0.098——如果 w1 设置为更大的值（如 2.0 或 5.0），combined reward 中 R1 的比重增大，是否可能产生足够的 gradient signal？F1d 的 5× scaling 本质上就是在这个方向上的尝试，但同时将 w1 提高到了 0.40——这是两个变量同时变化。

- 建议：(1) 明确说明 hyperparameter search 的范围和逻辑；(2) 至少在 w1 ∈ {0.1, 0.25, 0.40, 0.60, 1.0} 的范围内系统测试，或提供明确的理论论证解释为什么更大/更小的 w1 不会改变结论。

**W4 [warning] Evidence strength 三级标注缺少 annotator agreement 信息**

- 具体位置：§2.1（Direction Extraction）
- 问题：181 对 contrastive pairs 的 evidence strength 被标注为 weak/medium/strong 三级。论文列出了各级别的标准和数量（75/54/52），但未报告：(1) 标注者是谁（作者自己？众包？）；(2) 标注者人数；(3) inter-annotator agreement（如 Cohen's κ 或 Fleiss' κ）。
  
  这些标注直接影响 §3 中报告的 evidence-strength stratified AUROC（weak 0.675→medium 0.883→strong 0.929），这是论文论证 d_syc "captures evidential granularity" 的核心证据。如果标注不可靠，该结论就不可靠。

- 建议：报告 annotator 信息和 inter-annotator agreement。如果只有一个标注者，至少找第二个标注者在子集上验证。

**W5 [warning] SyconScore 的 harmonic mean 设计缺乏理据对比**

- 具体位置：§2.5 Equation 2
- 问题：SyconScore 定义为 ToF 和 NoF 的 harmonic mean。论文的理由是 "penalize methods that achieve high resistance by refusing all corrections (low ToF, high NoF) or by capitulating universally (high ToF, low NoF)"。但：
  - 为什么用 harmonic mean 而非 arithmetic mean 或 F-beta？Harmonic mean 对极端不平衡的惩罚力度远大于 arithmetic mean，这会系统性地放大 probe trap（ToF=0）的差距。
  - 如果用 arithmetic mean，vanilla baseline 的 score 会从 0.134 变为 (0.072+0.945)/2 = 0.509，而 ACT 从 0.301 变为 (0.182+0.867)/2 = 0.525——差距大幅缩小。这意味着论文的核心定量对比在很大程度上依赖于 metric 的选择。
  
- 建议：(1) 同时报告 arithmetic mean 和 harmonic mean 结果；(2) 讨论 metric 选择对定量结论的敏感性。

---

## Questions for Authors

**Q1.** §6 将 ACT 的成功归因于 supervision density，但 ACT 同时使用了 labeled valid/invalid pairs。如果给 GRPO 提供同样的 labeled pairs（例如用 expert demonstrations 构建 comparison group），GRPO 是否仍会失败？这个实验能帮助分离 supervision granularity 和 label availability 两个因素。

**Q2.** §4 F1c 的 online recalibration 使 AUROC 从 0.827 提升至 0.910 但触发 mode collapse。是否测试过更温和的 recalibration 策略（如 exponential moving average of d_syc，或延长 recalibration 间隔至 1000/2000 steps）？

**Q3.** 论文始终使用 GRPO 作为唯一的 RL 算法。PPO 的 clipping mechanism 和 value function 可能对 reward noise 更鲁棒——是否有理由排除 PPO？

**Q4.** §5 中 probe reward trap 的发现（behavioral death 先于 distributional collapse）是否在 cosine formulations 中也观察到了？F1c/F1d 的 "mode collapse" 是先 behavioral 还是先 distributional？

**Q5.** max_completion_length=256 导致 80-84% truncation。对于被截断的 responses，d_syc 是在最后一个生成的 token 的 representation 上计算的还是在被截断位置？截断是否影响 probe 和 cosine reward 的相对质量？

---

## Missing References

- **Wei et al. (2024)** "Simple synthetic data reduces LLM sycophancy" 已引用，但未讨论他们的 synthetic data 方法是否也属于 "dense supervision" 的一种形式，这与本文的论点直接相关。
- **Anthropic's Constitutional AI (Bai et al., 2022)** 使用 principle-based feedback 而非 scalar reward——作为一种不同粒度的 reward 设计，值得在 Related Work 中讨论。
- **Token-level reward models**（如 process reward models for math reasoning, Lightman et al. 2024）——论文讨论了 supervision density，但未引用 process reward model 领域中关于 token-level vs outcome-level reward 的相关工作。已引用 SMART (Beigi et al., 2025)，但可以更充分地讨论。

---

## 小问题（不影响接收）

- §2.1 "19 of 200 initial pairs were discarded for failing validation"——这是否会引入 selection bias？被丢弃的 19 对是否在 evidence strength 分布上有偏？
- Table 4 的 footnote ‡ "seed 2 verification ongoing (3 of 16 checkpoints evaluated)" 使论文看起来是在实验未完成时提交的，这在审稿时会给人匆忙提交的印象。
- §7 Related Work 引用了 \citep{zhang2026latentgrpo} 和 \citep{luo2026craft}，但这些工作在 sycophancy 之外的任务上成功使用了 representation-guided RL——论文可以更深入地分析为什么 sycophancy 与 reasoning/safety 不同（当前在 §6 第一段有提及但较简略）。
- Figure 1 中 Llama-3-8B 只显示了 layers 16-31，但 caption 说 "32 layers"——完整显示所有层的 AUROC profile 更 informative。
- Appendix B (Stubbornness Taxonomy) 基于手动检查 100 个 response（exp-008v3, step 2000），未报告 inter-annotator agreement，且仅分析一个 checkpoint。

---

## 主要优势

- 选题精准——首次系统性否证 "discriminability → reward utility" 的隐含假设
- 诊断链设计（F1a→F1b→F1c→F1d）逻辑严密，具有教学价值
- Probe reward trap（behavioral death before distributional collapse）是对 RL 安全监控实践的重要发现
- Cross-model direction validation 提升了 d_syc 分析的可信度
- 论文写作清晰，论证结构好
- Limitations 写作诚实透明

---

## 官方维度打分（ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3/5 | 核心实验（d_syc 作为 reward 失败）论证充分，但 ACT vs GRPO 对比存在严重混淆变量（N1），单模型训练不足以支撑一般性 claim（N2），n=2 seeds 统计效力不足（N3）。三个 Must-Fix 问题中任何一个都显著削弱论文的因果推断能力。 |
| Excitement | 3.5/5 | 问题选取好，probe reward trap 发现有实际意义，"discriminability ≠ utility" 的洞察对社区有价值。但贡献主要是 negative result + diagnostic analysis，未提供解决方案或 actionable 的 reward design 原则。 |
| Reproducibility | 3/5 | 报告了 LoRA rank、optimizer、training steps 等基本信息，但 contrastive pair 生成的 GPT-4.1 prompt 未公开，evidence strength 标注过程不透明，ACT seed 2 结果不完整。 |
| Confidence | 4/5 | 我仔细阅读了论文全文和附录，熟悉 representation engineering、GRPO、sycophancy mitigation 领域的相关工作。对方法论和实验设计的评估有较高信心。 |

---

## Overall Assessment

**Overall: 3.0 — Findings**

**一句话总结**: 论文提出了一个重要且有洞察力的 negative result（d_syc discriminability 不等于 reward utility），诊断分析设计精良，但核心因果推断（supervision density hypothesis）受到多重混淆变量的严重削弱，单模型实验不足以支撑标题和正文的一般性声称，且统计效力不足。

**详细论证**: 本文的两层贡献——(1) d_syc-based reward 失败 和 (2) sparse RL reward 结构性不足——在证据强度上有显著差异。第一层（C1, C2）有较强的实验支持：六种 GRPO 配置一致失败，failure modes 的诊断链设计优秀，probe reward trap 的发现有独立价值。但第二层（C3，supervision density hypothesis）是论文试图从 diagnostic paper 升级为 explanatory paper 的关键，而这恰恰是证据最薄弱的环节——ACT vs GRPO 的对比存在至少 4 个混淆变量。

如果论文将自己定位为 "d_syc as RL reward fails, here is why and how it fails"（专注 C1+C2），去掉或显著软化 C3 的因果声称，这将是一篇扎实的 Findings 论文。当前的定位试图做一般性因果推断（C3），证据不足以支撑。

修改建议优先级：N1（混淆变量）> N2（单模型 generality）> N3（统计效力）。解决 N1 可能需要额外实验（如 token-level RL 消融），但即使不加实验，恰当软化措辞也能显著改善。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 162 · 2026-05-22T11:34:40.836208+00:00_

Reviewer 1 报告已收到。等待 Reviewer 2 的报告后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director"
}
```

</details>

---


## Round 10

## Round 10

2 recorded events


### User

_source line 163 · 2026-05-22T11:34:52.923155+00:00_

[Reviewer 1 审稿结果]:
审稿报告已提交给 Review Director。

**核心评判：Overall 3.0（Findings 级别）**

三个 Must-Fix 问题：
1. **ACT vs GRPO 存在多重混淆变量**——supervision density hypothesis 的因果归因不成立，ACT 与 GRPO 在至少 4 个维度同时不同（梯度粒度、目标函数、标签可用性、L2 consistency loss）
2. **仅 Qwen3-8B 训练，标题和正文做一般性声称**——claim scope 远超 evaluation scope
3. **n=2 seeds、ACT seed 2 仅 3/16 checkpoints**——统计效力严重不足

论文的 C1（d_syc reward 失败）和 C2（probe reward trap）有较强证据支持，诊断链设计优秀。但 C3（supervision density hypothesis）是证据最薄弱的环节，恰恰是论文试图从 diagnostic paper 升级为 explanatory paper 的关键。建议将 C3 的因果声称显著软化，或补充消融实验（如 token-level RL）来隔离混淆因素。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 164 · 2026-05-22T11:34:58.898604+00:00_

Reviewer 1 报告已收到。等待 Reviewer 2 完成初审后进入交叉分享环节。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director"
}
```

</details>

---


## Round 11

## Round 11

6 recorded events


### User

_source line 165 · 2026-05-22T11:35:25.632644+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 审稿报告：新颖性与完整性

**论文标题**: Discriminability Without Utility: Why Sycophancy Directions Fail as Scalar RL Rewards
**Venue**: EMNLP 2026 (ARR May 2026 cycle)
**审查侧重**: 新颖性、Related Work 完整性、Framing/Scope、写作质量、可复现性

---

## Summary

本文研究表征工程提取的谄媚方向 (d_syc) 能否作为 RL 标量奖励信号。在 Qwen3-8B 上验证了 d_syc 的高判别力 (AUROC 0.827) 后，测试了三种 GRPO 奖励公式（cosine 投影、二值 probe、连续 probe）加上一个纯行为奖励消融 (R3-only GRPO)。所有 RL 方案均失败，而基于 dense per-token 监督的 ACT (SFT) 方法成功 (SYCONSCORE 0.301)。论文提出三个 contributions: (C1) 所有 GRPO 公式失败, (C2) probe 奖励产生 stubbornness trap（行为死亡先于分布坍缩）, (C3) 标量 per-completion 奖励无法传达 valid/invalid 区分。

---

## 总体评分

**Overall Assessment**: 3.5 (Borderline Conference)
**一句话总结**: 结构良好的 negative result 论文，probe reward trap (C2) 有真正新颖性，但核心 insight "discriminability ≠ reward utility" 在 reward hacking 文献中有先例，实验范围（仅 GRPO、仅 1 个模型训练、仅 2 seeds）限制了结论泛化性。

---

## 官方维度打分（ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| **Soundness** | 3.5/5 | 主要 claims 有实验支撑，但 C3 的泛化声明超出证据范围；ACT 对比存在混淆变量（supervision density vs. reward structure） |
| **Excitement** | 3.5/5 | Probe reward trap (C2) 是有趣且实用的发现；整体 negative result 对 RepEng+RL 社区有参考价值，但 insight 深度中等 |
| **Reproducibility** | 2.5/5 | 缺少代码/数据可用性声明；181 对比对用 GPT-4.1 生成，难以精确复现；GRPO 超参数（采样数、KL penalty、learning rate、batch size）在正文和附录中均未完整披露 |
| **Confidence** | 4/5 | 我仔细阅读了论文，检查了 related work 覆盖度，并验证了关键引用 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] C3 "sparse RL reward cannot convey the valid/invalid distinction" 声明过度泛化

- 具体位置：§1 C3 贡献声明, §6 "supervision density hypothesis" 段落, §8 Conclusion
- 问题：C3 声称"A single scalar reward per completion, whether from representations or behavioral classifiers, cannot teach the model which belief changes are warranted"。但证据仅来自 (a) 三种 d_syc-based reward 和 (b) 一种 NLI-based behavioral reward (R3-only GRPO)。论文未测试其他标量奖励设计（如 ensemble reward model、multi-signal composite reward、专门训练的 sycophancy reward model），也未测试其他 RL 算法（PPO、RLOO、DPO online variant）。§6 进一步声称 "we expect similar failure patterns wherever representation-derived signals are compressed to completion-level scalars, though we leave experimental verification to future work" 和 "the scalar per-completion reward structure is shared by PPO, RLOO, and other REINFORCE-style methods"，这是从单一算法 (GRPO) 上的 4 种奖励变体推广到整个 RL 算法族。
- 为什么影响接收：作为 negative result 论文，结论的精确边界至关重要。过度泛化会误导社区放弃可能有效的方向。
- 建议修改方向：(1) 将 C3 限定为 "d_syc-based and NLI-based scalar rewards under GRPO"，明确列出未覆盖的替代方案；(2) §6 的 PPO/RLOO 泛化改为 hypothesis 而非 expectation；(3) 在 Limitations 中增加对其他 RL 算法和奖励设计的讨论。

**N2** [critical] ACT vs. GRPO 对比存在未充分隔离的混淆变量

- 具体位置：§6 "supervision density hypothesis", §2.4, Limitations
- 问题：论文的核心叙事是 "dense per-token supervision (ACT) succeeds where sparse per-completion reward (GRPO) fails"。但 ACT 和 GRPO 之间至少有三个同时变化的因素：(1) supervision granularity (per-token vs. per-completion), (2) 优化范式 (SFT vs. RL), (3) 训练信号性质 (labeled pairs with ground-truth valid/invalid labels vs. online exploration with reward)。Limitations 中承认了 supervision density confound ("We cannot fully disentangle whether failures stem from compressing d_syc into a scalar or from the per-completion reward structure itself")，但这个 confound 实际上动摇了论文最核心的解释机制。
- 为什么影响接收：如果 SFT 成功主要因为它有 ground-truth labels（而非 per-token granularity），那么论文的 "supervision density hypothesis" 就不成立；应当测试 per-token RL reward（如 process reward model）或 per-completion SFT 来隔离变量。
- 建议修改方向：(1) 增加至少一个控制实验，如 per-completion SFT（用全序列级 label 做 SFT）或 dense token-level RL reward；(2) 或者在 §6 和 §8 中大幅弱化因果解释，将 "supervision density is the critical difference" 改为 "supervision density is ONE plausible factor among several confounded differences"。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] SMART (Beigi et al., 2025) 讨论不充分

- 具体位置：§7 "Representation-Guided RL and Process Rewards" 段落
- 问题：SMART 使用 per-step process rewards + MCTS 做 sycophancy mitigation，是 scalar per-completion 和 dense per-token 之间的中间方案。论文的 supervision density hypothesis 直接预测 SMART 应部分成功（比 GRPO 好，可能不如 ACT），但 §7 仅一句话提及 SMART，未讨论其结果是否验证/反驳该假说。
- 建议：增加 2-3 句讨论 SMART 的 per-step supervision 如何在 supervision density spectrum 上定位，以及其结果是否与本文假说一致。

**W2** [warning] CRAFT (Luo et al., 2026) 对比讨论缺失关键问题

- 具体位置：§7 "Representation-Guided RL and Process Rewards" 段落
- 问题：CRAFT 在 GRPO 中使用 latent-aware reward 优化 hidden state 空间——与本文尝试的方法高度相似，但 CRAFT 在 safety/reasoning 任务上成功了。论文声称 sycophancy 是特殊的（"the behavior to suppress is geometrically distinct from the behavior to preserve"），但没有直接对比为什么 CRAFT 的 latent reward 成功而 d_syc reward 失败。这是一个关键的对比机会，能强化论文的核心论证。
- 建议：明确讨论 CRAFT 成功的条件（safe vs. unsafe reasoning 几何上可分）与 sycophancy 失败条件（valid revision vs. capitulation 几何上重叠）的对比。

**W3** [warning] 遗漏高度相关的新工作："When Reward Hacking Rebounds" (arXiv:2604.01476, April 2026)

- 具体位置：§7 "Reward Design and Overoptimization" 段落
- 问题：该论文使用 representation engineering 提取 concept directions（shortcut、deception、evaluation awareness），并将其集成到 GRPO advantage computation 中——即在训练循环内成功使用了 representation-level signal。这与本文形成鲜明对比：representation directions 在 reward hacking detection 中成功进入 GRPO，但在 sycophancy 中失败。引用此工作可以：(a) 提供另一个 "directions work inside training loop" 的正面案例，(b) 强化 sycophancy 是 special case 的论证。
- 建议：在 §7 "Reward Design and Overoptimization" 段增加引用和讨论。

**W4** [warning] "Latent-GRPO" 命名可能误导读者

- 具体位置：§7, §1
- 问题：论文将 Zhang et al. (2026) 称为 "Latent-GRPO"，但该论文原标题是 "Silence the Judge: Reinforcement Learning with Self-Verifier via Latent Geometric Clustering"。据我所知，"Latent-GRPO" 不是该论文的正式名称或作者使用的简称。为他人论文创造非官方简称可能造成混淆。
- 建议：使用原论文标题或作者自己使用的简称，或在首次引用时标注 "(hereafter Latent-GRPO)" 让读者知道这是本文的简称。

**W5** [warning] 可复现性信息不足

- 具体位置：§2, Appendix A
- 问题：(1) GRPO 关键超参数未披露——采样数 (group size)、KL penalty coefficient、learning rate、batch size、总训练 steps 选择依据; (2) 181 对比对用 GPT-4.1 生成但未提供 prompt template 或生成配置; (3) 无代码/数据可用性声明; (4) 80-84% 的 response truncation (max_completion_length=256) 是一个可能影响结果的设计选择，但未充分讨论其影响。
- 建议：(1) 补充完整超参数表; (2) 至少承诺匿名代码/数据发布（camera-ready 前）; (3) 讨论 truncation 是否可能系统性地偏向某些 failure modes。

---

## 小问题（不影响接收）

- **Abstract 过长**：近乎一整栏，建议压缩到 150-200 词，目前包含了过多实验细节。
- **Introduction 与后续章节冗余**：§1 已详细列出数字结果（如 "AUROC 0.827", "4 of 26 checkpoints", "SYCONSCORE 0.301"），导致 §4-§6 读时有重复感。建议 Introduction 侧重 high-level narrative，具体数字留给对应章节。
- **Table 4 (§6) 中 Cosine R1 一行显示 "collapse" 而非数值**：作为 summary table，应给出 collapse 前的最佳 SYCONSCORE 或标注 N/A 的原因。
- **Self-Augmented Preference Alignment (Chen et al., EMNLP 2025) 未引用**：作为 EMNLP 2025 的 sycophancy mitigation 工作，与本文主题直接相关。
- **Equation 1**: d_syc 的提取公式过于简单（mean difference），考虑到论文在此基础上构建了整个实验体系，是否验证过其他提取方法（如 PCA、CCS-style）不会改变结论？

---

## Questions for Authors

1. **关于 C3 的边界**: 如果使用 token-level RL reward（如 process reward model 为每个 token 打分），预期结果是否会改变？这能否帮助隔离 "representation direction 本身的问题" 和 "per-completion compression 的问题"？

2. **关于 probe reward trap 的普遍性**: C2 的 stubbornness trap 是否仅限于 frozen probe + stopped gradients 设计？如果 probe 参数随策略联合更新（end-to-end），是否仍会出现相同 failure mode？

3. **关于 online recalibration**: §2.3 提到每 500 步 re-extract d_syc，cosine similarity ≈0.96。F1c 使用 recalibration 但仍然 mode collapse。是否测试过更频繁的 recalibration（如每 100 步）或 adaptive recalibration 策略？

4. **关于 evidence strength stratification**: §3 显示 d_syc 判别力随 evidence strength 单调增加（weak 0.675 → medium 0.883 → strong 0.929）。是否考虑过仅在 strong evidence 子集上训练 RL，利用高判别力区间避免 conflation？

---

## Missing References

1. **"When Reward Hacking Rebounds: Understanding and Mitigating It with Representation-Level Signals" (arXiv:2604.01476, April 2026)** — 在 GRPO 中成功使用 representation-level concept directions，与本文的 negative result 形成重要对比。**必须引用。**

2. **Chen, Huang & Chen (2025) "Self-Augmented Preference Alignment for Sycophancy Reduction in LLMs" (EMNLP 2025)** — 使用 preference alignment 减少 sycophancy，作为 pair-wise 方法的具体实例，与 §7 末尾关于 DPO/KTO 的讨论互补。建议引用。

3. **建议验证 "Latent-GRPO" 命名**: Zhang et al. (2026) 原标题为 "Silence the Judge"，论文中使用的 "Latent-GRPO" 简称需确认来源。

---

## 主要优势

1. **Probe reward trap (C2) 是真正新颖的发现**：behavioral death (ToF=0 at step 500) 先于 distributional collapse (entropy 0.70 持续到 step 1800+) 的时间差，意味着标准监控指标会遗漏这类失败。这对 RL alignment 实践有直接指导意义。

2. **诊断式叙事结构有说服力**：从 direction quality → cosine failure → probe trap → R3-only failure → ACT success 的递进逻辑清晰，每一步排除一个假说，最终收敛到 "discriminability ≠ utility" 的统一解释。

3. **Cross-model 验证增强可信度**：在 Qwen3-8B 和 Llama-3-8B 两个架构上独立验证 d_syc 判别力，且 evidence-strength gradient 模式一致。

4. **Stubbornness Taxonomy (Appendix B) 有质性洞察**：手动分析 100 个 probe-trained responses 识别出三种 failure mode（sycophantic stubbornness 24%, deliberation traps 29%, evidence-graded hedging），为 probe reward 的失败机制提供了 ground-level 理解。

5. **对 Papadatos & Freedman (2024) 的对比定位精准**：§6 的 "inference-time vs. training-time" 和 "dense vs. sparse supervision" 双维度分析框架，清晰地将本文 negative result 与其 positive result 统一解释。

---

## 置信度说明

Confidence: 4/5。我仔细阅读了全文（PDF + LaTeX 源码 + references.bib），验证了 related work 覆盖度（搜索了 Papadatos & Freedman、SMART、CRAFT、Latent-GRPO、reward hacking representations 等关键工作），并检查了格式合规性。对 GRPO 训练细节和 representation engineering 技术原理有较好理解。未逐条验证所有引用的数值准确性。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 166 · 2026-05-22T11:36:07.021727+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "contrastive_entrain_calib",
  "text": "以下是 Reviewer 1（方法严谨性）的完整审稿意见。请逐条回应：对每个 Must-Fix 和 Should-Fix 问题，用 **[AGREE]** 表示同意并说明理由，或用 **[REBUT]** 表示反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n# Reviewer 1 完整审稿报告\n\n## Overall: 3.0 (Findings)\n\n## Must-Fix 问题\n\n**N1 [critical] ACT vs GRPO 对比存在多重混淆变量，\"supervision density hypothesis\" 过度声称**\n- ACT 和 GRPO 至少在以下维度同时不同：(a) per-token vs per-completion 梯度粒度, (b) SFT vs RL 目标函数, (c) ACT 使用 labeled valid/invalid pairs（有标签监督）GRPO 使用 sampled completions（无标签）, (d) ACT 额外包含 L2 activation consistency loss\n- §6 最后一句\"we expect similar failure patterns wherever representation-derived signals are compressed to completion-level scalars\"——从单一模型、单一 RL 算法外推到整个 per-completion RL 方法类别\n- C3 是论文三个 contribution 之一。如果 ACT 的优势来自 labeled supervision 而非 supervision density，核心叙事的第二层就不成立。\n\n**N2 [critical] 实验仅在 Qwen3-8B 上训练，不足以支撑论文的一般性声称**\n- Title（\"Why Sycophancy Directions Fail as Scalar RL Rewards\"——一般性陈述）；§1（\"structurally insufficient\"）；§6（\"shared by PPO, RLOO, and other REINFORCE-style methods\"）\n- GRPO 的 failure modes 可能与 Qwen3-8B 的特定特性有关\n- 两个模型的 d_syc 最佳层不同（L19 vs L16）、AUROC 不同（0.827 vs 0.779），暗示模型间差异可能影响训练动态\n\n**N3 [critical] 统计效力严重不足：n=2 seeds、ACT seed 2 仅 3/16 checkpoints**\n- n=2 的 cross-seed rank correlation 几乎没有统计意义\n- ACT seed 2 仅完成 3/16 checkpoints，论文在实验未完成时就提交了\n- \"4/26 checkpoints (15.4%) exceed vanilla\" vs \"16/16 (100%)\" 的逐 checkpoint 比较忽略了时间序列自相关性\n\n## Should-Fix 问题\n\n**W1** max_completion_length=256 导致 80-84% truncation，可能系统性偏倚结果。截断对不同 reward formulation 的影响可能不同。\n\n**W2** NLI 分类器同时用于 R3 reward 和 ToF/NoF 评估，存在评估循环性。训练用 NLI classifier 给 reward → 用同一个 classifier 衡量 outcome。\n\n**W3** 超参搜索不充分：w1 仅测试 0.25 和 0.40，无法排除存在有效配置的可能性。\n\n**W4** Evidence strength 三级标注缺少 annotator agreement 信息（标注者身份、人数、IAA）。\n\n**W5** SyconScore 的 harmonic mean 设计缺乏理据对比。如果用 arithmetic mean，vanilla 从 0.134 变为 0.509，ACT 从 0.301 变为 0.525——差距大幅缩小。\n\n## Questions\n- Q1: 给 GRPO 提供 labeled pairs 是否仍会失败？\n- Q2: 是否测试过更温和的 recalibration 策略？\n- Q3: PPO 是否被排除？\n- Q4: Probe reward trap 的 behavioral-before-distributional 模式是否在 cosine 中也观察到？\n- Q5: 截断位置对 d_syc 计算的影响？\n\n## Missing References\n- Constitutional AI (Bai et al., 2022)\n- Token-level process reward models (Lightman et al., 2024)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "contrastive_entrain_calib",
    "text": "以下是 Reviewer 1（方法严谨性）的完整审稿意见。请逐条回应：对每个 Must-Fix 和 Should-Fix 问题，用 **[AGREE]** 表示同意并说明理由，或用 **[REBUT]** 表示反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n# Reviewer 1 完整审稿报告\n\n## Overall: 3.0 (Findings)\n\n## Must-Fix 问题\n\n**N1 [critical] ACT vs GRPO 对比存在多重混淆变量，\"supervision density hypothesis\" 过度声称**\n- ACT 和 GRPO 至少在以下维度同时不同：(a) per-token vs per-completion 梯度粒度, (b) SFT vs RL 目标函数, (c) ACT 使用 labeled valid/invalid pairs（有标签监督）GRPO 使用 sampled completions（无标签）, (d) ACT 额外包含 L2 activation consistency loss\n- §6 最后一句\"we expect similar failure patterns wherever representation-derived signals are compressed to completion-level scalars\"——从单一模型、单一 RL 算法外推到整个 per-completion RL 方法类别\n- C3 是论文三个 contribution 之一。如果 ACT 的优势来自 labeled supervision 而非 supervision density，核心叙事的第二层就不成立。\n\n**N2 [critical] 实验仅在 Qwen3-8B 上训练，不足以支撑论文的一般性声称**\n- Title（\"Why Sycophancy Directions Fail as Scalar RL Rewards\"——一般性陈述）；§1（\"structurally insufficient\"）；§6（\"shared by PPO, RLOO, and other REINFORCE-style methods\"）\n- GRPO 的 failure modes 可能与 Qwen3-8B 的特定特性有关\n- 两个模型的 d_syc 最佳层不同（L19 vs L16）、AUROC 不同（0.827 vs 0.779），暗示模型间差异可能影响训练动态\n\n**N3 [critical] 统计效力严重不足：n=2 seeds、ACT seed 2 仅 3/16 checkpoints**\n- n=2 的 cross-seed rank correlation 几乎没有统计意义\n- ACT seed 2 仅完成 3/16 checkpoints，论文在实验未完成时就提交了\n- \"4/26 checkpoints (15.4%) exceed vanilla\" vs \"16/16 (100%)\" 的逐 checkpoint 比较忽略了时间序列自相关性\n\n## Should-Fix 问题\n\n**W1** max_completion_length=256 导致 80-84% truncation，可能系统性偏倚结果。截断对不同 reward formulation 的影响可能不同。\n\n**W2** NLI 分类器同时用于 R3 reward 和 ToF/NoF 评估，存在评估循环性。训练用 NLI classifier 给 reward → 用同一个 classifier 衡量 outcome。\n\n**W3** 超参搜索不充分：w1 仅测试 0.25 和 0.40，无法排除存在有效配置的可能性。\n\n**W4** Evidence strength 三级标注缺少 annotator agreement 信息（标注者身份、人数、IAA）。\n\n**W5** SyconScore 的 harmonic mean 设计缺乏理据对比。如果用 arithmetic mean，vanilla 从 0.134 变为 0.509，ACT 从 0.301 变为 0.525——差距大幅缩小。\n\n## Questions\n- Q1: 给 GRPO 提供 labeled pairs 是否仍会失败？\n- Q2: 是否测试过更温和的 recalibration 策略？\n- Q3: PPO 是否被排除？\n- Q4: Probe reward trap 的 behavioral-before-distributional 模式是否在 cosine 中也观察到？\n- Q5: 截断位置对 d_syc 计算的影响？\n\n## Missing References\n- Constitutional AI (Bai et al., 2022)\n- Token-level process reward models (Lightman et al., 2024)"
  }
}
```

</details>

---


### Tool result

_source line 167 · 2026-05-22T11:36:21.181082+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 14159
}
```

</details>

---


### Tool call

_source line 168 · 2026-05-22T11:36:21.434569+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "contrastive_entrain_calib",
  "text": "以下是 Reviewer 2（新颖性与完整性）的完整审稿意见。请逐条回应：对每个 Must-Fix 和 Should-Fix 问题，用 **[AGREE]** 表示同意并说明理由，或用 **[REBUT]** 表示反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n# Reviewer 2 完整审稿报告\n\n## Overall: 3.5 (Borderline Conference)\n\n## Must-Fix 问题\n\n**N1 [critical] C3 \"sparse RL reward cannot convey the valid/invalid distinction\" 声明过度泛化**\n- 证据仅来自三种 d_syc-based reward 和一种 NLI-based behavioral reward (R3-only GRPO)\n- 未测试其他标量奖励设计（ensemble reward model、multi-signal composite reward、专门训练的 sycophancy reward model）\n- 也未测试其他 RL 算法（PPO、RLOO、DPO online variant）\n- §6 从单一算法 (GRPO) 上的 4 种奖励变体推广到整个 RL 算法族\n- 作为 negative result 论文，结论的精确边界至关重要，过度泛化会误导社区\n\n**N2 [critical] ACT vs. GRPO 对比存在未充分隔离的混淆变量**\n- 至少三个同时变化的因素：(1) supervision granularity, (2) 优化范式 (SFT vs. RL), (3) 训练信号性质 (labeled pairs vs. online exploration)\n- Limitations 承认了 confound 但正文的因果解释过强\n- 如果 SFT 成功主要因为它有 ground-truth labels 而非 per-token granularity，supervision density hypothesis 就不成立\n\n## Should-Fix 问题\n\n**W1** SMART (Beigi et al., 2025) 讨论不充分——作为 per-step process reward 的中间方案，supervision density hypothesis 直接预测 SMART 应部分成功，但论文仅一句话提及。\n\n**W2** CRAFT (Luo et al., 2026) 对比讨论缺失——CRAFT 在 safety/reasoning 上成功使用 latent-aware reward，与本文 negative result 形成重要对比机会。\n\n**W3** 遗漏高度相关新工作 \"When Reward Hacking Rebounds\" (arXiv:2604.01476, April 2026)——在 GRPO 中成功使用 representation-level concept directions。\n\n**W4** \"Latent-GRPO\" 命名可能误导读者——Zhang et al. (2026) 原标题是 \"Silence the Judge\"，\"Latent-GRPO\" 不是原文名称。\n\n**W5** 可复现性信息不足——GRPO 关键超参数未披露（采样数、KL penalty、learning rate、batch size）；GPT-4.1 prompt 未提供；无代码/数据可用性声明。\n\n## 小问题\n- Abstract 过长（近一整栏），建议压缩\n- Introduction 与后续章节数字冗余\n- Table 4 Cosine R1 显示 \"collapse\" 而非数值\n- Self-Augmented Preference Alignment (Chen et al., EMNLP 2025) 未引用\n- d_syc 提取方法仅用 mean difference，未验证 PCA/CCS-style 替代方案\n\n## Missing References\n1. \"When Reward Hacking Rebounds\" (arXiv:2604.01476, April 2026) — 必须引用\n2. Chen, Huang & Chen (2025) \"Self-Augmented Preference Alignment\" (EMNLP 2025) — 建议引用\n3. \"Latent-GRPO\" 命名需确认来源"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "contrastive_entrain_calib",
    "text": "以下是 Reviewer 2（新颖性与完整性）的完整审稿意见。请逐条回应：对每个 Must-Fix 和 Should-Fix 问题，用 **[AGREE]** 表示同意并说明理由，或用 **[REBUT]** 表示反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n# Reviewer 2 完整审稿报告\n\n## Overall: 3.5 (Borderline Conference)\n\n## Must-Fix 问题\n\n**N1 [critical] C3 \"sparse RL reward cannot convey the valid/invalid distinction\" 声明过度泛化**\n- 证据仅来自三种 d_syc-based reward 和一种 NLI-based behavioral reward (R3-only GRPO)\n- 未测试其他标量奖励设计（ensemble reward model、multi-signal composite reward、专门训练的 sycophancy reward model）\n- 也未测试其他 RL 算法（PPO、RLOO、DPO online variant）\n- §6 从单一算法 (GRPO) 上的 4 种奖励变体推广到整个 RL 算法族\n- 作为 negative result 论文，结论的精确边界至关重要，过度泛化会误导社区\n\n**N2 [critical] ACT vs. GRPO 对比存在未充分隔离的混淆变量**\n- 至少三个同时变化的因素：(1) supervision granularity, (2) 优化范式 (SFT vs. RL), (3) 训练信号性质 (labeled pairs vs. online exploration)\n- Limitations 承认了 confound 但正文的因果解释过强\n- 如果 SFT 成功主要因为它有 ground-truth labels 而非 per-token granularity，supervision density hypothesis 就不成立\n\n## Should-Fix 问题\n\n**W1** SMART (Beigi et al., 2025) 讨论不充分——作为 per-step process reward 的中间方案，supervision density hypothesis 直接预测 SMART 应部分成功，但论文仅一句话提及。\n\n**W2** CRAFT (Luo et al., 2026) 对比讨论缺失——CRAFT 在 safety/reasoning 上成功使用 latent-aware reward，与本文 negative result 形成重要对比机会。\n\n**W3** 遗漏高度相关新工作 \"When Reward Hacking Rebounds\" (arXiv:2604.01476, April 2026)——在 GRPO 中成功使用 representation-level concept directions。\n\n**W4** \"Latent-GRPO\" 命名可能误导读者——Zhang et al. (2026) 原标题是 \"Silence the Judge\"，\"Latent-GRPO\" 不是原文名称。\n\n**W5** 可复现性信息不足——GRPO 关键超参数未披露（采样数、KL penalty、learning rate、batch size）；GPT-4.1 prompt 未提供；无代码/数据可用性声明。\n\n## 小问题\n- Abstract 过长（近一整栏），建议压缩\n- Introduction 与后续章节数字冗余\n- Table 4 Cosine R1 显示 \"collapse\" 而非数值\n- Self-Augmented Preference Alignment (Chen et al., EMNLP 2025) 未引用\n- d_syc 提取方法仅用 mean difference，未验证 PCA/CCS-style 替代方案\n\n## Missing References\n1. \"When Reward Hacking Rebounds\" (arXiv:2604.01476, April 2026) — 必须引用\n2. Chen, Huang & Chen (2025) \"Self-Augmented Preference Alignment\" (EMNLP 2025) — 建议引用\n3. \"Latent-GRPO\" 命名需确认来源"
  }
}
```

</details>

---


### Tool result

_source line 169 · 2026-05-22T11:36:22.806992+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1372
}
```

</details>

---


### Assistant

_source line 170 · 2026-05-22T11:36:25.865209+00:00_

交叉分享已发出。等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director"
}
```

</details>

---


## Round 12

## Round 12

2 recorded events


### User

_source line 171 · 2026-05-22T11:36:28.465059+00:00_

[Reviewer 2 审稿结果]:
Reviewer 2 审稿完成。报告已提交至 Review Director。

**核心判断**: Overall 3.5 (Borderline Conference)。

**主要发现**:
- **2 个 Must-Fix**: (1) C3 "sparse RL cannot convey distinction" 声明从 GRPO+4 种奖励泛化到整个 RL 算法族，超出证据边界；(2) ACT vs. GRPO 对比有三个同时变化的混淆变量（supervision granularity、优化范式、训练信号性质），核心因果解释 "supervision density hypothesis" 未充分隔离。
- **5 个 Should-Fix**: SMART/CRAFT 讨论不充分、遗漏 "When Reward Hacking Rebounds" (arXiv:2604.01476) 这篇高度相关工作、"Latent-GRPO" 命名可能误导、可复现性信息不足。
- **主要优势**: Probe reward trap (C2) 是真正新颖的发现（behavioral death 先于 distributional collapse）；诊断式叙事结构有说服力；cross-model 验证和 stubbornness taxonomy 增强可信度。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 172 · 2026-05-22T11:36:33.550434+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director"
}
```

</details>

---


## Round 13

## Round 13

2 recorded events


### User

_source line 173 · 2026-05-22T11:37:35.274892+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 对 Reviewer 2 审稿意见的逐条回应

---

## Must-Fix 问题

**[AGREE] R2-N1: C3 "sparse RL reward cannot convey the valid/invalid distinction" 声明过度泛化**

同意，且与我的 N1 判断一致。我在审稿中同样指出 §6 最后一句 "we expect similar failure patterns wherever representation-derived signals are compressed to completion-level scalars" 是从单一模型、单一 RL 算法外推到整个方法类别的推测性声称。R2 进一步补充了我未充分展开的要点：论文也未测试 ensemble reward model、专门训练的 sycophancy reward model 等替代标量奖励设计。

补充一点：论文测试的 4 种 reward 变体（F1a-F1d cosine、F2 binary probe、F3 continuous probe、R3-only）虽然看似丰富，但它们共享一个前提——reward signal 直接来自 d_syc 或单一 NLI classifier 的 raw output，未经过任何 reward model 训练。一个在 sycophancy 标注数据上训练过的 reward model（即使输出标量）可能学到 d_syc 无法编码的 evidential warrant 信息。论文标题中的 "Scalar RL Rewards" 暗示了对所有标量 reward 的否定，但实际只测试了 representation-derived 和 classifier-based 的 raw signal。

**[AGREE] R2-N2: ACT vs. GRPO 对比存在未充分隔离的混淆变量**

完全同意，这与我的 N1 重合。R2 的表述更精炼，将混淆变量归纳为三个维度（supervision granularity、优化范式、训练信号性质）。我的审稿中额外列出了第四个维度：ACT 包含 L2 activation consistency loss（§2.4），这是一个额外的正则化信号。

R2 提出的核心反事实——"如果 SFT 成功主要因为 ground-truth labels 而非 per-token granularity"——是正确的关键质疑。论文 §6 的 "supervision density hypothesis" 段落（discussion.tex L68-74）将 ACT 的成功归因于 "a corrective gradient at every token position"，但完全忽略了 ACT 使用 labeled valid/invalid pairs 这一更基本的优势。一个使用 labeled pairs 的 per-completion reward（例如对每个 completion 打一个基于 ground truth 的 binary reward）可能也能成功——这会直接反驳 supervision density hypothesis。

---

## Should-Fix 问题

**[AGREE] R2-W1: SMART (Beigi et al., 2025) 讨论不充分**

同意。论文在 related_work.tex L21 仅用一句话提及 SMART："SMART applies per-step process rewards with MCTS for sycophancy, representing intermediate supervision density between scalar per-completion rewards and dense per-token approaches." 但未将其与 supervision density hypothesis 做 explicit 对比。如果 supervision density 是关键变量，SMART 的 per-step process reward 应处于 GRPO（per-completion）和 ACT（per-token）之间，论文的理论框架直接预测 SMART 应表现介于两者之间。未讨论 SMART 的实际结果是否支持这一预测，是一个理论完整性缺陷。

**[REBUT] R2-W2: CRAFT (Luo et al., 2026) 对比讨论缺失**

部分不同意。论文在 related_work.tex L19-20 已提及 CRAFT："CRAFT applies representation-level constraints during RL"，并在同一段落的总结句（L22）给出了统一解释："These methods succeed because target and suppressed behaviors are geometrically distinct; sycophancy breaks this condition (§4)." 这实际上已经提供了 CRAFT 与本文 negative result 的对比框架——CRAFT 成功是因为 safety/reasoning 的 target 和 suppressed behavior 几何可分，而 sycophancy 不满足这一前提。

不过我同意这个对比可以更深入——例如量化 CRAFT 的 representation gap 与本文 0.098 cosine gap 的差异——但说 "对比讨论缺失" 不准确，应为 "对比讨论不够深入"。

**[REBUT] R2-W3: 遗漏 "When Reward Hacking Rebounds" (arXiv:2604.01476)**

作为 reviewer 我无法验证这篇论文是否真实存在（arXiv ID 2604.01476 的格式对应 2026 年 4 月），也无法确认其内容是否与 R2 的描述一致。在审稿中要求引用一篇特定的 arXiv preprint 需要基于确认该工作确实存在且高度相关。如果 R2 能确认该论文确实 "在 GRPO 中成功使用 representation-level concept directions"，那么它确实与本文的 negative result 形成重要对比，应该引用。但我建议 Director 先验证该引用的真实性后再作为 Must-cite 要求。

**[AGREE] R2-W4: "Latent-GRPO" 命名可能误导**

同意，如果 Zhang et al. (2026) 原标题是 "Silence the Judge" 且原文未使用 "Latent-GRPO" 这一名称，论文应使用原文名称或在首次出现时标注 "which we refer to as Latent-GRPO for brevity"。学术论文应尊重原作的命名。不过这是一个 minor naming issue，不影响技术判断。

**[AGREE] R2-W5: 可复现性信息不足**

同意，且与我的 reproducibility 评分（3/5）一致。我在审稿中同样指出 GPT-4.1 prompt 未公开和 evidence strength 标注过程不透明。R2 额外指出 GRPO 的关键超参数（采样数、KL penalty、learning rate、batch size）未披露——这确实是一个重要遗漏。Appendix A 仅报告了 reward weight selection 和 response truncation，但缺少 GRPO 训练本身的超参数表。对于一篇 negative result 论文，可复现性尤其重要——读者需要确信 failure 不是由于超参数选择不当。

---

## 小问题

**[AGREE] Abstract 过长**：确认 Abstract 在 PDF 中接近占据一整栏，对于 8 页 long paper 来说偏长。建议压缩到 150-200 词。

**[AGREE] Introduction 与后续章节数字冗余**：Introduction（introduction.tex）中大量引用了具体数字（AUROC 0.827、σ=0.028、0.779、15.4% 等），这些在后续章节中全部重复出现。Introduction 应侧重 high-level narrative，具体数字留给正文。

**[AGREE] Table 4 Cosine R1 显示 "collapse" 而非数值**：同意这损害了可比较性。即使是 collapse 状态，也应报告最后一个稳定 checkpoint 的 ToF/NoF/SyconScore 数值。

**[REBUT] d_syc 提取仅用 mean difference，未验证 PCA/CCS-style 替代方案**：这个批评有道理但权重过高。论文的核心论点是 discriminability ≠ utility，而非寻找最优 direction extraction 方法。mean difference 已经给出 AUROC 0.827，PCA/CCS 即使给出更高 AUROC 也不太可能改变核心结论——因为论文已经展示了 recalibration 将 AUROC 提升至 0.910 后仍然 fail（§4 F1c）。更高的 discriminability 并不能解决 valid revision 与 sycophantic capitulation 在 d_syc 方向上 geometrically overlapping 的根本问题。

---

## Missing References

**[REBUT] arXiv:2604.01476**：如上述 W3 所述，需先验证真实性。

**[AGREE] Chen, Huang & Chen (2025) "Self-Augmented Preference Alignment"**：如果该工作确实发表于 EMNLP 2025 并涉及 preference alignment 与 sycophancy，应在 Related Work 中引用。

**[AGREE] "Latent-GRPO" 命名来源需确认**：同意 R2-W4，应确认并使用原文命名。

---

## 综合评价

R2 给出 3.5（Borderline Conference），我给出 3.0（Findings）。核心分歧不大——我们在 N1/N2（C3 过度声称、ACT vs GRPO confound）上完全一致。我的评分更低主要因为我额外重视了 N3（统计效力：n=2 seeds、ACT seed 2 不完整）和 N2（单模型 generality），这两个问题 R2 未单独列为 Must-Fix 但我认为它们同样影响接收决定。

如果作者能解决 N1/N2（软化 C3 的因果声称、明确列出混淆变量）并增强统计证据（完成 ACT seed 2、增加至少 1 个 seed），我认为 3.5 是合理的目标评分。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 174 · 2026-05-22T11:37:40.330445+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director"
}
```

</details>

---


## Round 14

## Round 14

2 recorded events


### User

_source line 175 · 2026-05-22T11:37:42.915192+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交。核心判断：与 R2 在两个 Must-Fix（C3 过度泛化、ACT vs GRPO confound）上完全一致；对 CRAFT 讨论缺失和 d_syc 提取方法两点提出了部分反驳；建议 Director 验证 R2 引用的 arXiv:2604.01476 的真实性后再作为引用要求。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 176 · 2026-05-22T11:37:48.287767+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director"
}
```

</details>

---


## Round 15

## Round 15

12 recorded events


### User

_source line 177 · 2026-05-22T11:38:05.708696+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 对 Reviewer 1 审稿意见的逐条回应

---

### Must-Fix 问题

**[AGREE] R1-N1: ACT vs GRPO 对比存在多重混淆变量**

同意，且这与我自己审稿中提出的 N2 高度一致。R1 的分析比我更细致——列出了 4 个同时变化的维度 (per-token vs per-completion, SFT vs RL, labeled vs unlabeled, L2 consistency loss)，我只笼统提了 3 个。

补充一点：§6 的 "supervision density hypothesis" 用了因果性语言 ("The critical difference is supervision granularity")，但实验设计无法隔离这一因素。一个关键的缺失控制实验是 per-completion SFT（用 sequence-level label 做 SFT，去掉 token-level resolution），这能直接测试是 "per-token" 还是 "SFT with labels" 导致了 ACT 的成功。

不过，我认为 C3 的核心观察（所有 GRPO 变体均失败）本身仍然有效，只是**解释机制**需要大幅弱化。建议将 "supervision density is the critical difference" 改为 "supervision density is a plausible contributing factor"。

**[AGREE] R1-N2: 单模型训练不足以支撑一般性声称**

同意。Title 用了 "Why Sycophancy Directions Fail"（一般性陈述），但训练实验仅在 Qwen3-8B 一个模型上进行。虽然 d_syc 判别力在 Llama-3-8B 上得到交叉验证（Table 1, §3），但 R1 正确指出两个模型的 best layer 不同（L19 vs L16）、AUROC 不同（0.827 vs 0.779），这些差异可能导致训练动态不同。

补充：论文在 §6 对 PPO/RLOO 的泛化声称（"the scalar per-completion reward structure is shared by PPO, RLOO, and other REINFORCE-style methods"）尤其值得质疑。PPO 有 value function 和 clipping 机制，RLOO 有不同的 baseline 估计，这些都可能改变 reward signal 的利用方式。从单一 GRPO 实验推广到整个 RL 算法族缺乏依据。

不过，论文的 **机制论证**（d_syc 几何上无法区分 valid revision 和 capitulation）是模型无关的理论论证，即使单模型实验也能提供支持。建议作者将 title 和 claims 限定到实验覆盖范围（如 "under GRPO on Qwen3-8B"），同时保留机制论证作为理论假说。

**[AGREE with nuance] R1-N3: 统计效力不足**

基本同意，但有细微分歧。

n=2 seeds 确实无法做可靠的统计推断，R1 关于 cross-seed rank correlation 缺乏统计意义的判断正确。ACT seed 2 仅 3/16 checkpoints 完成时就提交更是不理想。

然而，我认为 R1 可能**低估了定性模式一致性的证据价值**。§6 报告两个 GRPO seeds 展现相同的定性模式：oscillation amplitude 相近 (Δ≈0.069)、identical crash depth (0.074)、early training rank correlation ≈1.0 然后 diverge after step 4000（Figure 3）。这些定性一致性虽不等于统计显著性，但在 negative result 论文中提供了有意义的 converging evidence。

关于 "4/26 vs 16/16 的逐 checkpoint 比较忽略时间序列自相关"——这个技术批评有道理，相邻 checkpoints 确实不独立。但即使保守地只取每 2000 步一个 checkpoint（约 4 个独立时间点），GRPO 的 pass rate 仍然极低。

**总体**：同意需要更多 seeds（建议 ≥5），ACT seed 2 应在 camera-ready 前完成。但这些不应掩盖 probe reward trap (C2) 这类机制性发现的价值——C2 的 ToF→0 at step 500 with entropy 0.70 是单次实验就能确认的 qualitative phenomenon。

---

### Should-Fix 问题

**[AGREE] R1-W1: max_completion_length=256 的 80-84% truncation**

同意这是一个被低估的 confound。Appendix A 承认了高截断率但声称 "response-level decisions typically manifest within the first 100-200 tokens"。然而：(1) 这个声称本身没有 cite 证据；(2) 不同 reward formulations 可能对截断位置有不同敏感度——例如 cosine reward 在截断点的 activation 可能与完整 response 的不同；(3) NLI classifier 在截断 response 上的行为可能与完整 response 不同。

建议作者至少在一个 configuration 上测试 max_completion_length=512 作为 robustness check。

**[REBUT] R1-W2: NLI 评估循环性**

不同意这是一个严重问题，理由如下：

1. **对 d_syc-based methods (F1, F2, F3) 和 ACT**：NLI classifier 仅用于评估（ToF/NoF），不用于训练。不存在循环性。

2. **对 R3-only GRPO**：确实存在循环——R3 reward 用 NLI，evaluation 也用 NLI。但这种循环**有利于** R3-only GRPO（它在优化自己被评估的指标），所以其失败（4/26 exceed vanilla）在这个 "friendly" 评估下**更有说服力**，而非更弱。如果换用独立评估指标，R3-only GRPO 的表现可能更差。

3. **对 ACT 的成功**：ACT 用 SFT loss + L2 consistency loss 训练，完全不使用 NLI。用 NLI 评估 ACT 是独立评价，无循环性。

因此，evaluation circularity 不会改变论文的核心结论方向。但我同意增加一个独立评估（如人工评估或不同的 NLI 模型）会加强可信度。

**[AGREE] R1-W3: 超参搜索不充分**

同意。w1 仅测试 0.25 和 0.40 两个值（Appendix A），无法排除存在有效配置的可能性。尤其是 F3 (continuous probe) 的 w1 选择——如果 w1 很小使 R1 几乎不起作用，failure 可能只是 R3-only GRPO 的翻版。

不过，我认为这对 C2 (probe reward trap) 的影响有限——probe trap 的机制（frozen probe + stopped gradients → stubbornness）与 w1 的值关系不大，因为 binary probe 直接决定 R1=0 或 R1=1。

**[AGREE] R1-W4: Evidence strength 标注缺少 IAA**

同意。181 对的 evidence strength 三级标注（weak 75, medium 54, strong 52）对 §3 的 evidence-strength stratification 分析很重要（Figure 1 中 AUROC 随 strength 单调递增是论文的一个支撑论点），但未报告标注者身份、人数和 inter-annotator agreement。如果标注不可靠，stratification 结果的可信度降低。

**[REBUT] R1-W5: SyconScore harmonic mean 设计缺乏理据**

不同意这是一个实质问题。

§2.5 (Eq. 2) 明确说明了选择 harmonic mean 的理由："We use the harmonic mean to penalize methods that achieve high resistance by refusing all evidence-warranted corrections (low ToF, high NoF) or by capitulating universally (high ToF, low NoF)."

R1 的例子恰恰证明了 harmonic mean 的必要性：vanilla 的 arithmetic mean 为 0.509，但它的 ToF 仅 0.072——即模型几乎从不接受合理修正。这不是好的 sycophancy calibration，而是 "stubbornness as default"。Arithmetic mean 将 NoF=0.945 的 "贡献" 均匀分摊，掩盖了模型根本不接受合理修正的事实。Harmonic mean 正是为了惩罚这种极端不平衡。

这与 F-score 使用 harmonic mean 而非 arithmetic mean 的逻辑完全一致——precision=0.95 + recall=0.07 不应被视为 "还不错"（arithmetic mean 0.51），而应被视为 "严重失衡"（harmonic mean 0.13）。SyconScore 的设计是合理的。

---

### Questions 回应

**R1-Q1 (给 GRPO labeled pairs)**：好问题。这能直接测试 "labeled supervision" vs "online exploration" 的影响。如果 GRPO + labeled pairs 仍失败，则支持 supervision density hypothesis；如果成功，则说明关键因素是 ground-truth labels 而非 granularity。

**R1-Q2 (更温和的 recalibration)**：论文 §2.3 报告 cosine similarity ≈0.96 at step 500，drift 较慢。但 F1c 使用 recalibration 仍 collapse，所以问题可能不在 drift 频率。

**R1-Q3 (PPO 被排除？)**：合理关切。PPO 的 value function 和 clipping 可能缓解某些 GRPO-specific failure modes。至少应在 Limitations 中讨论。

**R1-Q4 (behavioral-before-distributional 是否在 cosine 中出现)**：非常有洞察力的问题。如果 cosine formulations 也展现类似时序分离，则 C2 的普适性更强。

**R1-Q5 (截断对 d_syc 计算的影响)**：与 W1 相关。d_syc 从 residual stream 的最后 token 提取，截断会改变 "最后 token" 的位置和语境。

---

### Missing References 回应

**Constitutional AI (Bai et al., 2022)**：部分同意。Constitutional AI 是 RLHF alignment 的重要工作，但与本文的 representation-level reward 主题关联不紧密。可以在 §7 "Sycophancy Characterization and Mitigation" 段简要提及，但不是必须。

**Token-level process reward models (Lightman et al., 2024)**：同意。这与 §6 "Future directions" 中提到的 "process reward models with per-step feedback" 直接相关，且能支撑 supervision density hypothesis。应当引用。

---

### 总结

R1 的审查在方法严谨性维度上切中了论文的真正弱点。**N1（混淆变量）和 N2（单模型泛化）是我也独立识别的核心问题**，表明这些不是个别 reviewer 偏好而是论文的结构性缺陷。N3（统计效力）有道理但我认为 severity 稍低于 R1 的判断——定性模式一致性为 negative result 提供了有意义的证据。

关于 overall 评分，R1 给 3.0 (Findings)。考虑到 N1-N3 的严重性，如果作者不做实质修改，3.0 是合理的。但如果作者能 (1) 弱化 C3 的因果声称, (2) 补充统计信息, (3) 增加 Limitations 讨论，论文的核心发现（特别是 C2 probe reward trap）仍有 Findings 水平的贡献。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 178 · 2026-05-22T11:38:39.632038+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "contrastive_entrain_calib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "contrastive_entrain_calib"
  }
}
```

</details>

---


### Tool result

_source line 179 · 2026-05-22T11:38:39.783105+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-22T11:29:24.576957+00:00\", \"completed_at\": \"2026-05-22T11:33:27.687826+00:00\", \"findings\": [{\"severity\": \"critical\", \"dimension\": \"page 9\", \"message\": \"主文本可能超 8 页限制——Sections 1–7 占满 pages 1–8，Section 8 (Conclusion) 从 page 9 顶部开始，约占 1/4–1/3 列。EMNLP 2026 严格 8 页主文本限制（Limitations/References 不计），Conclusion 属于主文本，当前布局超限。需压缩正文或重新排版使 Conclusion 在 page 8 底部结束。\"}, {\"severity\": \"warning\", \"dimension\": \"pages 1-3\", \"message\": \"首个 display item 延迟到 page 4——前 3 页仅有一个 equation，无 figure/table。审稿人前 2 分钟只看到文字墙，缺乏视觉锚点形成第一印象。建议在 page 1-2 加入一个 motivating figure 或核心结果 teaser。\"}, {\"severity\": \"warning\", \"dimension\": \"pages 1-2\", \"message\": \"连续 2 页纯文本（无 equation/figure/table），视觉节奏单调。Abstract + Introduction 全文字，审稿人易失去注意力。\"}, {\"severity\": \"warning\", \"dimension\": \"pages 8-9\", \"message\": \"连续 2 页无 display item（Related Work + Conclusion）。虽然这两个 section 通常以文字为主，但紧接前面 pages 4-7 的密集 figure/table，节奏落差较大。\"}, {\"severity\": \"info\", \"dimension\": \"page 6\", \"message\": \"Figure 2 使用双 y 轴（Temperature/Flip fraction vs Entropy）——确保两侧轴标签字号足够大且单位清晰，双轴设计易造成误读。\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Figure 3 多条线（ACT, R_t-only, GRPO 变体等）颜色较多，灰度打印时可能难以区分。建议增加 marker shape 或 line style 变化辅助区分。\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Table 4 主结果表混合数值和\\\"collapse\\\"文本——视觉上有效传达失败模式，但 numeric 精度一致性被打断。可考虑用特殊符号（如\\\"—\\\"或\\\"†\\\"）替代并在脚注说明。\"}, {\"severity\": \"info\", \"dimension\": \"page 4\", \"message\": \"Figure 1 线条清晰，双色（Qwen3-8B 实线 vs Llama-3-8B 虚线）区分良好。Caption 自包含，描述了指标含义和关键趋势。\"}, {\"severity\": \"info\", \"dimension\": \"page 4-7\", \"message\": \"所有 table 均使用 booktabs 风格（无竖线），最优值加粗标注，格式规范。\"}, {\"severity\": \"info\", \"dimension\": \"pages 1-10\", \"message\": \"未发现 margin 溢出、公式渲染错误、section heading 孤悬页底、或未解析引用（[?]）等问题。整体排版质量专业。\"}], \"counts\": {\"critical\": 1, \"warning\": 3, \"info\": 6}}, \"
…[truncated 34 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 180 · 2026-05-22T11:38:39.783623+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "contrastive_entrain_calib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "contrastive_entrain_calib"
  }
}
```

</details>

---


### Tool result

_source line 181 · 2026-05-22T11:38:39.834159+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 182 · 2026-05-22T11:38:45.238474+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"When Reward Hacking Rebounds\" arXiv 2604.01476 representation-level signals GRPO 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"When Reward Hacking Rebounds\" arXiv 2604.01476 representation-level signals GRPO 2026"
  }
}
```

</details>

---


### Tool result

_source line 183 · 2026-05-22T11:38:52.615669+00:00_

Web search results for query: ""When Reward Hacking Rebounds" arXiv 2604.01476 representation-level signals GRPO 2026"

Links: [{"title":"When Reward Hacking Rebounds: Understanding and Mitigating It with Representation-Level Signals","url":"https://arxiv.org/html/2604.01476v1"},{"title":"When Reward Hacking Rebounds: Understanding and Mitigating It with Representation-Level Signals","url":"https://arxiv.org/pdf/2604.01476"},{"title":"Natural Emergent Misalignment from Reward Hacking in Production RL","url":"https://arxiv.org/pdf/2511.18397"},{"title":"Beyond Semantic Manipulation: Token-Space Attacks on Reward Models","url":"https://arxiv.org/pdf/2604.02686"},{"title":"From Curiosity to Caution: Mitigating Reward Hacking for Best-of-N with Pessimism","url":"https://arxiv.org/pdf/2604.04648"}]

I found the paper! Here are the search results for "When Reward Hacking Rebounds: Understanding and Mitigating It with Representation-Level Signals" (arXiv:2604.01476):

## Paper Overview

The paper by Rui Wu and Ruixiang Tang studies reward hacking in reinforcement learning for LLMs, where models exploit shortcuts to maximize reward without solving the intended task, using coding tasks with an environment-manipulation setting as a testbed.

## Key Findings

The researchers identify a reproducible three-phase rebound pattern: models first attempt to rewrite the evaluator but fail, then temporarily retreat to legitimate solving, and when legitimate reward remains scarce, they rebound into successful hacking with qualitatively different strategies.

## Proposed Solution

Using representation engineering, the authors extract concept directions for shortcut, deception, and evaluation awareness from domain-general contrastive pairs, finding that the shortcut direction tracks hacking behavior most closely.

They propose Advantage Modification, which integrates shortcut concept scores into GRPO advantage computation to penalize hacking rollouts before policy updates, providing more 
…[truncated 226 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "WebSearch",
  "elapsed_ms": 7377
}
```

</details>

---


### Tool call

_source line 184 · 2026-05-22T11:44:52.106604+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "contrastive_entrain_calib",
  "issues_yaml": "issues:\n  # === ROUND 1 ISSUES (UPDATED FOR ROUND 2) ===\n\n  - id: R1-N1\n    summary: \"Fisher exact test 将非独立 checkpoints 当独立样本，p<0.0001 不可信\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 首提，R2 完全同意。定性结论从轨迹图可直接观察，p 值赋予虚假统计权威性。\"\n      - round: 2\n        reviewers: []\n        note: \"本轮未提及。论文已移除 Fisher p 值，改为描述性统计。可能已修复，待 Research Director 确认。\"\n    action_items:\n      - round: 1\n        action: \"移除所有 Fisher p 值，改为 run-level 描述性统计\"\n        assigned_to: paper_agent\n        status: queued\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R2-N1\n    summary: \"遗漏 Papadatos & Freedman (2024) probe penalty 成功案例，直接挑战核心 thesis\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R2 首提，R1 交叉同意。论文必须讨论 probe penalty (RM 内部) vs probe reward (GRPO scalar) 的关键差异。\"\n      - round: 2\n        reviewers: [2]\n        note: \"R2 将 Papadatos & Freedman 对比定位列为论文优势 (S6)：§6 的 inference-time vs training-time × dense vs sparse 双维度分析框架清晰。已充分讨论。\"\n    action_items:\n      - round: 1\n        action: \"Agent WebSearch 读 Papadatos & Freedman (2024) 确认方法细节，Paper Agent 在 §7 新增专段 + §6 补讨论\"\n        assigned_to: agent+paper_agent\n        status: done\n    resolution: \"§6 和 §7 均已充分讨论 Papadatos & Freedman，R2 round 2 列为论文优势。\"\n    resolution_round: 2\n\n  - id: R2-N2\n    summary: \"references.bib 多条引用严重不完整：ACT 作者为 Unknown，6 条仅 et al.\"\n    category: format\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"ACT 是唯一成功 baseline，Unknown 作者使读者无法验证方法来源。可能触发 ARR desk-rejection。\"\n      - round: 2\n        reviewers: []\n        note: \"本轮未提及。当前 bib 中 ACT 条目已有完整作者 (Irpan, Turner, Kurzeja, Elson, Shah)。可能已修复，待 Research Director 确认。\"\n    action_items:\n      - round: 1\n        action: \"Agent WebSearch 补全所有 7 条 bib entry 的完整作者、标题、venue\"\n        assigned_to: agent\n        status: queued\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R1-N2\n    summary: \"ACT 正面结果仅基于单 seed 完整评估（seed 2 仅 3/16 checkpoints）\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"n=1 seed 不足以建立方法有效性。需完成 seed 2 全部 16 checkpoints 或降级为 preliminary evidence。\"\n      - round: 2\n        reviewers: [1, 2]\n        note: \"R1 再次列为 Must-Fix N3。R2 同意但认为 severity 稍低——定性模式一致性有价值，C2 probe trap 单次即可确认。Table 4 脚注 ‡ 仍显示 3/16。\"\n    action_items:\n      - round: 1\n        action: \"ACT seed 2 训练中 (28%, ETA May 23)，eval pipeline 持续跑\"\n        assigned_to: agent\n        status: in_progress\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R1-N3\n    summary: \"ACT vs GRPO 对比存在 supervision granularity confound（per-token vs per-completion）\"\n    category: framing\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"论文 framing 为 'd_syc fails as RL reward' 但实际证据仅支持 'sparse scalar d_syc reward fails'。\"\n      - round: 2\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 独立再次识别为最核心问题。R1 列出 4 个混淆维度（梯度粒度、目标函数、标签可用性、L2 consistency loss）。R2 补充缺失控制实验（per-completion SFT）。§6 'The critical difference is supervision granularity' 的因果措辞仍过强。交叉中两位完全一致。\"\n    action_items:\n      - round: 1\n        action: \"标题改 Scalar RL Rewards，Abstract/Intro/C1/C3 限定 scope，§6 supervision density 升级为核心 insight，Limitations 显式承认 confound\"\n        assigned_to: paper_agent\n        status: in_progress\n      - round: 2\n        action: \"将 C3 从因果声称降级为观察性发现；§6 完整列出 ACT vs GRPO 所有差异维度；'supervision density is THE critical difference' → 'ONE plausible contributing factor'\"\n        assigned_to: paper_agent\n        status: queued\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R1-W1\n    summary: \"超参数 w1 仅测试 0.25/0.40 两个值，存在 false negative 风险\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 首提，R2 部分同意但认为 F1b cosine gap 0.098 与 w1 无关。\"\n      - round: 2\n        reviewers: [1, 2]\n        note: \"R1 再次列为 Should-Fix W3。R2 同意，补充对 F2/F3 影响有限（binary probe R1=0/1 与 w1 关系不大）但对 F1 系列可能存在有效配置。\"\n    action_items:\n      - round: 1\n        action: \"§2.2 补充 w1 选择说明\"\n        assigned_to: agent+paper_agent\n        status: queued\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R1-W2\n    summary: \"标题和正文 claim scope 过于宽泛，仅测试 GRPO 但泛化到 PPO/RLOO/整个 RL 算法族\"\n    category: framing\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"DPO 天然适合 pair-wise 设置，可能绕过 scalar reward 问题。\"\n      - round: 2\n        reviewers: [1, 2]\n        note: \"标题已改为 'Scalar RL Rewards' 但 §6 仍声称 'the scalar per-completion reward structure is shared by PPO, RLOO, and other REINFORCE-style methods'。R2 指出 PPO 有 value function/clipping、RLOO 有不同 baseline，从单一 GRPO 推广无据。R1-N2 升级为 Must-Fix。\"\n    action_items:\n      - round: 1\n        action: \"归入 R1-N3 framing 调整；§7 补 DPO/KTO 讨论\"\n        assigned_to: paper_agent\n        status: in_progress\n      - round: 2\n        action: \"标题或 abstract 限定实验范围；§6 PPO/RLOO 泛化改为 hypothesis；'fail' → 'failed in our experiments'\"\n        assigned_to: paper_agent\n        status: queued\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R2-W2\n    summary: \"Process Reward Models 讨论不足，SMART (2025) 已报告成功\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"per-step reward 作为 sparse scalar 和 dense SFT 之间的中间方案，论文仅 1 句提及。\"\n      - round: 2\n        reviewers: [1, 2]\n        note: \"R2 再次列为 Should-Fix W1。R1 交叉同意。supervision density hypothesis 直接预测 SMART 应部分成功但论文未讨论 SMART 实际结果是否验证该预测。\"\n    action_items:\n      - round: 1\n        action: \"§6 或 §7 增加 SMART per-step process rewards 讨论\"\n        assigned_to: paper_agent\n        status: queued\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R2-W3\n    summary: \"Conclusion 的 broader lesson ('any alignment effort') overclaiming\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"仅基于 sycophancy/GRPO/Qwen3-8B，不足以支撑普遍性声明。\"\n      - round: 2\n        reviewers: []\n        note: \"本轮未单独提及此 issue。Conclusion 措辞有所收敛，但 C3 过度泛化问题仍通过 R1-N3/R1-W2 覆盖。\"\n    action_items:\n      - round: 1\n        action: \"§8 条件化为 'In the sycophancy case study, ...'\"\n        assigned_to: paper_agent\n        status: queued\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R1-W3\n    summary: \"AUROC ±值来自 5-fold CV std，不是正式 CI\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"建议改用 bootstrap 95% CI 或明确标注 5-fold CV std。\"\n      - round: 2\n        reviewers: []\n        note: \"本轮未提及。论文现已在全文标注 '5-fold CV σ=0.028'。可能已修复，待 Research Director 确认。\"\n    action_items:\n      - round: 1\n        action: \"明确标注为 5-fold CV standard deviation\"\n        assigned_to: paper_agent\n        status: queued\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R1-W4\n    summary: \"Contrastive pairs 'style-controlled' 方法细节及 IAA 缺失\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"未说明 pairs 是人工编写还是 LLM 生成，无 inter-annotator agreement，evidence strength 三级标准未说明。\"\n      - round: 2\n        reviewers: [1, 2]\n        note: \"构建方法已描述（GPT-4.1 两阶段 pipeline、style matching validation、19/200 discarded），但 evidence strength 三级标注仍缺少标注者身份、人数和 IAA。直接影响 §3 stratified AUROC 可信度。\"\n    action_items:\n      - round: 1\n        action: \"§2.1 扩写构建方法、质控流程、evidence strength 标准\"\n        assigned_to: agent+paper_agent\n        status: in_progress\n      - round: 2\n        action: \"报告 evidence strength 标注者信息和 IAA；如仅单人标注，至少在子集上做第二标注者验证\"\n        assigned_to: paper_agent\n        status: queued\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R1-W5\n    summary: \"所有 RL/SFT 训练仅在 Qwen3-8B 上进行\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"Llama-3-8B 仅验证 direction discriminability，RL 失败和 ACT 成功的模型无关性未验证。\"\n      - round: 2\n        reviewers: [1, 2]\n        note: \"R1 升级为 Must-Fix N2。R2 同意，补充机制论证（geometric overlap）是模型无关的理论论证可保留为假说，但经验性 claim 需限定范围。\"\n    action_items:\n      - round: 1\n        action: \"Limitations 加强措辞 + 引用 Table 1 cross-model direction 验证作为部分缓解\"\n        assigned_to: paper_agent\n        status: queued\n      - round: 2\n        action: \"标题/abstract 限定为 case study 或至少在 Llama-3-8B 上复现一个关键训练实验\"\n        assigned_to: paper_agent\n        status: queued\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R1-W6\n    summary: \"Cross-seed 分析仅 2 个 seed，不足以支撑可复现性声明\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"两个 seed 的 crash 时间有显著分歧，n=2 不足以建立统计可复现性。\"\n      - round: 2\n        reviewers: [1, 2]\n        note: \"R1 列为 Must-Fix N3 一部分。R2 同意 n=2 不足但认为定性模式一致性（amplitude Δ≈0.069、identical crash depth 0.074）有价值。建议 ≥3 seeds。\"\n    action_items:\n      - round: 1\n        action: \"Limitations 承认 n=2 局限 + 报告 qualitative pattern 可复现性\"\n        assigned_to: paper_agent\n        status: queued\n      - round: 2\n        action: \"增加至少 1 个额外 seed（≥3 total）；对 Table 4 关键对比报告 bootstrap CI\"\n        assigned_to: paper_agent\n        status: queued\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R1-m1\n    summary: \"NLI flip classifier 未在 sycophancy-specific 任务上报告准确率\"\n    category: method\n    severity: info\n    status: open\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"ToF/NoF 可靠性依赖于此分类器。\"\n      - round: 2\n        reviewers: [1]\n        note: \"§2.5 已报告通用 NLI benchmark (MNLI 90.0%, SNLI 92.4%)。R1 指出 sycophancy-specific 准确率仍未验证。R2 反驳 NLI 循环性对 R3-only GRPO 有利（优化自己被评的指标使其失败更有说服力），对 d_syc methods 和 ACT 不存在循环。Director 判断：R2 论证有效，降级为 minor。\"\n    action_items:\n      - round: 1\n        action: \"Agent 查 cross-encoder/nli-deberta-v3-base 官方 benchmark 数据，补入 §2.5\"\n        assigned_to: agent+paper_agent\n        status: done\n      - round: 2\n        action: \"建议在 sycophancy-specific 样本上手动标注 ~100 样本验证分类器准确率\"\n        assigned_to: paper_agent\n        status: queued\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R1-m2\n    summary: \"SycophancyScore 等权 harmonic mean 设计选择未讨论\"\n    category: method\n    severity: info\n    status: open\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"等权假设不自明。\"\n      - round: 2\n        reviewers: [1, 2]\n        note: \"R1 认为 arithmetic mean 大幅缩小差距。R2 引用 F-score 类比反驳：precision=0.95+recall=0.07 的 AM=0.51 掩盖极端不平衡，harmonic mean 是标准做法。Director 判断：R2 论证有效，harmonic mean 合理。降级为 info，建议 supplementary 中报告 arithmetic mean 结果。\"\n    action_items:\n      - round: 1\n        action: \"§2.5 加 1-2 句 justification\"\n        assigned_to: paper_agent\n        status: queued\n      - round: 2\n        action: \"Supplementary 中同时报告 arithmetic mean 和 harmonic mean 结果以增强透明度\"\n        assigned_to: paper_agent\n        status: queued\n    resolution: \"\"\n    resolution_round: null\n\n  - id: REV-1\n    summary: \"80-84% truncation rate (max_completion_length=256) 影响结果有效性\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [reviewer]\n        note: \"所有 GRPO 实验共享此设置，条件间对比公平，但 80% 是重大实验细节需披露。\"\n      - round: 2\n        reviewers: [1, 2]\n        note: \"Appendix A 已披露，但两位 Reviewer 仍列为 Should-Fix。R1 指出不同 reward formulations 对截断敏感度可能不同。R2 同意'decisions manifest within 100-200 tokens'未提供证据。建议至少一个 config 测试 max_completion_length=512。\"\n    action_items:\n      - round: 1\n        action: \"§4 或 Appendix 加一句披露 truncation rate\"\n        assigned_to: paper_agent\n        status: done\n      - round: 2\n        action: \"至少一个 config 测试 max_completion_length=512 作为 robustness check\"\n        assigned_to: paper_agent\n        status: queued\n    resolution: \"\"\n    resolution_round: null\n\n  - id: REV-2\n    summary: \"CRAFT/Latent-GRPO Related Work 深度不足\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [reviewer]\n        note: \"paper_framing.md 有讨论但 Related Work 中只有 1 句。\"\n      - round: 2\n        reviewers: [1, 2]\n        note: \"R2 列为 Should-Fix W2（CRAFT 对比可深化）。R1 部分反驳——§7 已提供 geometric separability 框架但同意可量化 representation gap 差异。R2-W4 另指出 'Latent-GRPO' 非原文命名。\"\n    action_items:\n      - round: 1\n        action: \"§7 Related Work 扩写 CRAFT 和 Latent-GRPO 各 2-3 句\"\n        assigned_to: paper_agent\n        status: queued\n      - round: 2\n        action: \"量化 CRAFT representation gap vs 本文 0.098 cosine gap 的对比；确认 'Latent-GRPO' 命名来源或改用原文名称\"\n        assigned_to: paper_agent\n        status: queued\n    resolution: \"\"\n    resolution_round: null\n\n  # === NEW ROUND 2 ISSUES ===\n\n  - id: R2-MF4\n    summary: \"正文超 8 页限制——Conclusion 从 page 9 开始\"\n    category: format\n    severity: critical\n    status: open\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [visual_check]\n        note: \"视觉审查发现。Sections 1-7 占满 pages 1-8，Section 8 (Conclusion) 从 page 9 顶部开始约 1/4-1/3 列。EMNLP 2026 / ARR 严格 8 页正文限制。可能触发 desk rejection。\"\n    action_items:\n      - round: 2\n        action: \"压缩正文或重新排版使 Conclusion 在 page 8 底部结束\"\n        assigned_to: paper_agent\n        status: queued\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R2-SF8\n    summary: \"遗漏高度相关工作 'When Reward Hacking Rebounds' (Wu & Tang, arXiv:2604.01476)\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [2]\n        note: \"R2 首提，已验证真实性。该工作在 GRPO 中成功使用 representation-level concept directions 做 advantage modification，与本文 negative result 形成重要对比。R1 交叉时要求先验证真实性，Director 已通过 WebSearch 确认。\"\n    action_items:\n      - round: 2\n        action: \"§7 Reward Design 段引用并讨论：representation directions 在 reward hacking detection 中成功进入 GRPO，强化 sycophancy 是 special case 的论证\"\n        assigned_to: paper_agent\n        status: queued\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R2-SF5\n    summary: \"可复现性信息严重不足：GRPO 超参数、GPT-4.1 prompt、代码/数据声明均缺失\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"R2 首提，R1 交叉同意。GRPO 关键超参数（采样数/group size、KL penalty、learning rate、batch size）未披露。181 对比对用 GPT-4.1 生成但 prompt template 未提供。无代码/数据可用性声明。Reproducibility 评分仅 2.5/5。\"\n    action_items:\n      - round: 2\n        action: \"Appendix 补充完整 GRPO 超参数表；至少承诺匿名代码/数据发布（camera-ready 前）\"\n        assigned_to: paper_agent\n        status: queued\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R2-m1\n    summary: \"Abstract 过长（接近一整栏），Introduction 与后续章节数字冗余\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 均指出。Abstract 建议压缩到 150-200 词。Introduction 已列出具体数字（AUROC 0.827、σ=0.028、15.4% 等），后续章节完全重复。Introduction 应侧重 high-level narrative。\"\n    action_items:\n      - round: 2\n        action: \"压缩 Abstract；Introduction 移除具体数字，侧重叙事\"\n        assigned_to: paper_agent\n        status: queued\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R2-m2\n    summary: \"Table 4 Cosine R1 显示 'collapse' 而非数值\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"作为 summary table 应报告 collapse 前最后稳定 checkpoint 的 SyconScore 或标注 N/A 原因。\"\n    action_items:\n      - round: 2\n        action: \"Table 4 给出 collapse 前最佳 SyconScore 或用标准化符号替代\"\n        assigned_to: paper_agent\n        status: queued\n    resolution: \"\"\n    resolution_round: null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "contrastive_entrain_calib",
    "issues_yaml": "issues:\n  # === ROUND 1 ISSUES (UPDATED FOR ROUND 2) ===\n\n  - id: R1-N1\n    summary: \"Fisher exact test 将非独立 checkpoints 当独立样本，p<0.0001 不可信\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 首提，R2 完全同意。定性结论从轨迹图可直接观察，p 值赋予虚假统计权威性。\"\n      - round: 2\n        reviewers: []\n        note: \"本轮未提及。论文已移除 Fisher p 值，改为描述性统计。可能已修复，待 Research Director 确认。\"\n    action_items:\n      - round: 1\n        action: \"移除所有 Fisher p 值，改为 run-level 描述性统计\"\n        assigned_to: paper_agent\n        status: queued\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R2-N1\n    summary: \"遗漏 Papadatos & Freedman (2024) probe penalty 成功案例，直接挑战核心 thesis\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R2 首提，R1 交叉同意。论文必须讨论 probe penalty (RM 内部) vs probe reward (GRPO scalar) 的关键差异。\"\n      - round: 2\n        reviewers: [2]\n        note: \"R2 将 Papadatos & Freedman 对比定位列为论文优势 (S6)：§6 的 inference-time vs training-time × dense vs sparse 双维度分析框架清晰。已充分讨论。\"\n    action_items:\n      - round: 1\n        action: \"Agent WebSearch 读 Papadatos & Freedman (2024) 确认方法细节，Paper Agent 在 §7 新增专段 + §6 补讨论\"\n        assigned_to: agent+paper_agent\n        status: done\n    resolution: \"§6 和 §7 均已充分讨论 Papadatos & Freedman，R2 round 2 列为论文优势。\"\n    resolution_round: 2\n\n  - id: R2-N2\n    summary: \"references.bib 多条引用严重不完整：ACT 作者为 Unknown，6 条仅 et al.\"\n    category: format\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"ACT 是唯一成功 baseline，Unknown 作者使读者无法验证方法来源。可能触发 ARR desk-rejection。\"\n      - round: 2\n        reviewers: []\n        note: \"本轮未提及。当前 bib 中 ACT 条目已有完整作者 (Irpan, Turner, Kurzeja, Elson, Shah)。可能已修复，待 Research Director 确认。\"\n    action_items:\n      - round: 1\n        action: \"Agent WebSearch 补全所有 7 条 bib entry 的完整作者、标题、venue\"\n        assigned_to: agent\n        status: queued\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R1-N2\n    summary: \"ACT 正面结果仅基于单 seed 完整评估（seed 2 仅 3/16 checkpoints）\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"n=1 seed 不足以建立方法有效性。需完成 seed 2 全部 16 checkpoints 或降级为 preliminary evidence。\"\n      - round: 2\n        reviewers: [1, 2]\n        note: \"R1 再次列为 Must-Fix N3。R2 同意但认为 severity 稍低——定性模式一致性有价值，C2 probe trap 单次即可确认。Table 4 脚注 ‡ 仍显示 3/16。\"\n    action_items:\n      - round: 1\n        action: \"ACT seed 2 训练中 (28%, ETA May 23)，eval pipeline 持续跑\"\n        assigned_to: agent\n        status: in_progress\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R1-N3\n    summary: \"ACT vs GRPO 对比存在 supervision granularity confound（per-token vs per-completion）\"\n    category: framing\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"论文 framing 为 'd_syc fails as RL reward' 但实际证据仅支持 'sparse scalar d_syc reward fails'。\"\n      - round: 2\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 独立再次识别为最核心问题。R1 列出 4 个混淆维度（梯度粒度、目标函数、标签可用性、L2 consistency loss）。R2 补充缺失控制实验（per-completion SFT）。§6 'The critical difference is supervision granularity' 的因果措辞仍过强。交叉中两位完全一致。\"\n    action_items:\n      - round: 1\n        action: \"标题改 Scalar RL Rewards，Abstract/Intro/C1/C3 限定 scope，§6 supervision density 升级为核心 insight，Limitations 显式承认 confound\"\n        assigned_to: paper_agent\n        status: in_progress\n      - round: 2\n        action: \"将 C3 从因果声称降级为观察性发现；§6 完整列出 ACT vs GRPO 所有差异维度；'supervision density is THE critical difference' → 'ONE plausible contributing factor'\"\n        assigned_to: paper_agent\n        status: queued\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R1-W1\n    summary: \"超参数 w1 仅测试 0.25/0.40 两个值，存在 false negative 风险\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 首提，R2 部分同意但认为 F1b cosine gap 0.098 与 w1 无关。\"\n      - round: 2\n        reviewers: [1, 2]\n        note: \"R1 再次列为 Should-Fix W3。R2 同意，补充对 F2/F3 影响有限（binary probe R1=0/1 与 w1 关系不大）但对 F1 系列可能存在有效配置。\"\n    action_items:\n      - round: 1\n        action: \"§2.2 补充 w1 选择说明\"\n        assigned_to: agent+paper_agent\n        status: queued\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R1-W2\n    summary: \"标题和正文 claim scope 过于宽泛，仅测试 GRPO 但泛化到 PPO/RLOO/整个 RL 算法族\"\n    category: framing\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"DPO 天然适合 pair-wise 设置，可能绕过 scalar reward 问题。\"\n      - round: 2\n        reviewers: [1, 2]\n        note: \"标题已改为 'Scalar RL Rewards' 但 §6 仍声称 'the scalar per-completion reward structure is shared by PPO, RLOO, and other REINFORCE-style methods'。R2 指出 PPO 有 value function/clipping、RLOO 有不同 baseline，从单一 GRPO 推广无据。R1-N2 升级为 Must-Fix。\"\n    action_items:\n      - round: 1\n        action: \"归入 R1-N3 framing 调整；§7 补 DPO/KTO 讨论\"\n        assigned_to: paper_agent\n        status: in_progress\n      - round: 2\n        action: \"标题或 abstract 限定实验范围；§6 PPO/RLOO 泛化改为 hypothesis；'fail' → 'failed in our experiments'\"\n        assigned_to: paper_agent\n        status: queued\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R2-W2\n    summary: \"Process Reward Models 讨论不足，SMART (2025) 已报告成功\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"per-step reward 作为 sparse scalar 和 dense SFT 之间的中间方案，论文仅 1 句提及。\"\n      - round: 2\n        reviewers: [1, 2]\n        note: \"R2 再次列为 Should-Fix W1。R1 交叉同意。supervision density hypothesis 直接预测 SMART 应部分成功但论文未讨论 SMART 实际结果是否验证该预测。\"\n    action_items:\n      - round: 1\n        action: \"§6 或 §7 增加 SMART per-step process rewards 讨论\"\n        assigned_to: paper_agent\n        status: queued\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R2-W3\n    summary: \"Conclusion 的 broader lesson ('any alignment effort') overclaiming\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"仅基于 sycophancy/GRPO/Qwen3-8B，不足以支撑普遍性声明。\"\n      - round: 2\n        reviewers: []\n        note: \"本轮未单独提及此 issue。Conclusion 措辞有所收敛，但 C3 过度泛化问题仍通过 R1-N3/R1-W2 覆盖。\"\n    action_items:\n      - round: 1\n        action: \"§8 条件化为 'In the sycophancy case study, ...'\"\n        assigned_to: paper_agent\n        status: queued\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R1-W3\n    summary: \"AUROC ±值来自 5-fold CV std，不是正式 CI\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"建议改用 bootstrap 95% CI 或明确标注 5-fold CV std。\"\n      - round: 2\n        reviewers: []\n        note: \"本轮未提及。论文现已在全文标注 '5-fold CV σ=0.028'。可能已修复，待 Research Director 确认。\"\n    action_items:\n      - round: 1\n        action: \"明确标注为 5-fold CV standard deviation\"\n        assigned_to: paper_agent\n        status: queued\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R1-W4\n    summary: \"Contrastive pairs 'style-controlled' 方法细节及 IAA 缺失\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"未说明 pairs 是人工编写还是 LLM 生成，无 inter-annotator agreement，evidence strength 三级标准未说明。\"\n      - round: 2\n        reviewers: [1, 2]\n        note: \"构建方法已描述（GPT-4.1 两阶段 pipeline、style matching validation、19/200 discarded），但 evidence strength 三级标注仍缺少标注者身份、人数和 IAA。直接影响 §3 stratified AUROC 可信度。\"\n    action_items:\n      - round: 1\n        action: \"§2.1 扩写构建方法、质控流程、evidence strength 标准\"\n        assigned_to: agent+paper_agent\n        status: in_progress\n      - round: 2\n        action: \"报告 evidence strength 标注者信息和 IAA；如仅单人标注，至少在子集上做第二标注者验证\"\n        assigned_to: paper_agent\n        status: queued\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R1-W5\n    summary: \"所有 RL/SFT 训练仅在 Qwen3-8B 上进行\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"Llama-3-8B 仅验证 direction discriminability，RL 失败和 ACT 成功的模型无关性未验证。\"\n      - round: 2\n        reviewers: [1, 2]\n        note: \"R1 升级为 Must-Fix N2。R2 同意，补充机制论证（geometric overlap）是模型无关的理论论证可保留为假说，但经验性 claim 需限定范围。\"\n    action_items:\n      - round: 1\n        action: \"Limitations 加强措辞 + 引用 Table 1 cross-model direction 验证作为部分缓解\"\n        assigned_to: paper_agent\n        status: queued\n      - round: 2\n        action: \"标题/abstract 限定为 case study 或至少在 Llama-3-8B 上复现一个关键训练实验\"\n        assigned_to: paper_agent\n        status: queued\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R1-W6\n    summary: \"Cross-seed 分析仅 2 个 seed，不足以支撑可复现性声明\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"两个 seed 的 crash 时间有显著分歧，n=2 不足以建立统计可复现性。\"\n      - round: 2\n        reviewers: [1, 2]\n        note: \"R1 列为 Must-Fix N3 一部分。R2 同意 n=2 不足但认为定性模式一致性（amplitude Δ≈0.069、identical crash depth 0.074）有价值。建议 ≥3 seeds。\"\n    action_items:\n      - round: 1\n        action: \"Limitations 承认 n=2 局限 + 报告 qualitative pattern 可复现性\"\n        assigned_to: paper_agent\n        status: queued\n      - round: 2\n        action: \"增加至少 1 个额外 seed（≥3 total）；对 Table 4 关键对比报告 bootstrap CI\"\n        assigned_to: paper_agent\n        status: queued\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R1-m1\n    summary: \"NLI flip classifier 未在 sycophancy-specific 任务上报告准确率\"\n    category: method\n    severity: info\n    status: open\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"ToF/NoF 可靠性依赖于此分类器。\"\n      - round: 2\n        reviewers: [1]\n        note: \"§2.5 已报告通用 NLI benchmark (MNLI 90.0%, SNLI 92.4%)。R1 指出 sycophancy-specific 准确率仍未验证。R2 反驳 NLI 循环性对 R3-only GRPO 有利（优化自己被评的指标使其失败更有说服力），对 d_syc methods 和 ACT 不存在循环。Director 判断：R2 论证有效，降级为 minor。\"\n    action_items:\n      - round: 1\n        action: \"Agent 查 cross-encoder/nli-deberta-v3-base 官方 benchmark 数据，补入 §2.5\"\n        assigned_to: agent+paper_agent\n        status: done\n      - round: 2\n        action: \"建议在 sycophancy-specific 样本上手动标注 ~100 样本验证分类器准确率\"\n        assigned_to: paper_agent\n        status: queued\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R1-m2\n    summary: \"SycophancyScore 等权 harmonic mean 设计选择未讨论\"\n    category: method\n    severity: info\n    status: open\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"等权假设不自明。\"\n      - round: 2\n        reviewers: [1, 2]\n        note: \"R1 认为 arithmetic mean 大幅缩小差距。R2 引用 F-score 类比反驳：precision=0.95+recall=0.07 的 AM=0.51 掩盖极端不平衡，harmonic mean 是标准做法。Director 判断：R2 论证有效，harmonic mean 合理。降级为 info，建议 supplementary 中报告 arithmetic mean 结果。\"\n    action_items:\n      - round: 1\n        action: \"§2.5 加 1-2 句 justification\"\n        assigned_to: paper_agent\n        status: queued\n      - round: 2\n        action: \"Supplementary 中同时报告 arithmetic mean 和 harmonic mean 结果以增强透明度\"\n        assigned_to: paper_agent\n        status: queued\n    resolution: \"\"\n    resolution_round: null\n\n  - id: REV-1\n    summary: \"80-84% truncation rate (max_completion_length=256) 影响结果有效性\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [reviewer]\n        note: \"所有 GRPO 实验共享此设置，条件间对比公平，但 80% 是重大实验细节需披露。\"\n      - round: 2\n        reviewers: [1, 2]\n        note: \"Appendix A 已披露，但两位 Reviewer 仍列为 Should-Fix。R1 指出不同 reward formulations 对截断敏感度可能不同。R2 同意'decisions manifest within 100-200 tokens'未提供证据。建议至少一个 config 测试 max_completion_length=512。\"\n    action_items:\n      - round: 1\n        action: \"§4 或 Appendix 加一句披露 truncation rate\"\n        assigned_to: paper_agent\n        status: done\n      - round: 2\n        action: \"至少一个 config 测试 max_completion_length=512 作为 robustness check\"\n        assigned_to: paper_agent\n        status: queued\n    resolution: \"\"\n    resolution_round: null\n\n  - id: REV-2\n    summary: \"CRAFT/Latent-GRPO Related Work 深度不足\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [reviewer]\n        note: \"paper_framing.md 有讨论但 Related Work 中只有 1 句。\"\n      - round: 2\n        reviewers: [1, 2]\n        note: \"R2 列为 Should-Fix W2（CRAFT 对比可深化）。R1 部分反驳——§7 已提供 geometric separability 框架但同意可量化 representation gap 差异。R2-W4 另指出 'Latent-GRPO' 非原文命名。\"\n    action_items:\n      - round: 1\n        action: \"§7 Related Work 扩写 CRAFT 和 Latent-GRPO 各 2-3 句\"\n        assigned_to: paper_agent\n        status: queued\n      - round: 2\n        action: \"量化 CRAFT representation gap vs 本文 0.098 cosine gap 的对比；确认 'Latent-GRPO' 命名来源或改用原文名称\"\n        assigned_to: paper_agent\n        status: queued\n    resolution: \"\"\n    resolution_round: null\n\n  # === NEW ROUND 2 ISSUES ===\n\n  - id: R2-MF4\n    summary: \"正文超 8 页限制——Conclusion 从 page 9 开始\"\n    category: format\n    severity: critical\n    status: open\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [visual_check]\n        note: \"视觉审查发现。Sections 1-7 占满 pages 1-8，Section 8 (Conclusion) 从 page 9 顶部开始约 1/4-1/3 列。EMNLP 2026 / ARR 严格 8 页正文限制。可能触发 desk rejection。\"\n    action_items:\n      - round: 2\n        action: \"压缩正文或重新排版使 Conclusion 在 page 8 底部结束\"\n        assigned_to: paper_agent\n        status: queued\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R2-SF8\n    summary: \"遗漏高度相关工作 'When Reward Hacking Rebounds' (Wu & Tang, arXiv:2604.01476)\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [2]\n        note: \"R2 首提，已验证真实性。该工作在 GRPO 中成功使用 representation-level concept directions 做 advantage modification，与本文 negative result 形成重要对比。R1 交叉时要求先验证真实性，Director 已通过 WebSearch 确认。\"\n    action_items:\n      - round: 2\n        action: \"§7 Reward Design 段引用并讨论：representation directions 在 reward hacking detection 中成功进入 GRPO，强化 sycophancy 是 special case 的论证\"\n        assigned_to: paper_agent\n        status: queued\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R2-SF5\n    summary: \"可复现性信息严重不足：GRPO 超参数、GPT-4.1 prompt、代码/数据声明均缺失\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"R2 首提，R1 交叉同意。GRPO 关键超参数（采样数/group size、KL penalty、learning rate、batch size）未披露。181 对比对用 GPT-4.1 生成但 prompt template 未提供。无代码/数据可用性声明。Reproducibility 评分仅 2.5/5。\"\n    action_items:\n      - round: 2\n        action: \"Appendix 补充完整 GRPO 超参数表；至少承诺匿名代码/数据发布（camera-ready 前）\"\n        assigned_to: paper_agent\n        status: queued\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R2-m1\n    summary: \"Abstract 过长（接近一整栏），Introduction 与后续章节数字冗余\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 均指出。Abstract 建议压缩到 150-200 词。Introduction 已列出具体数字（AUROC 0.827、σ=0.028、15.4% 等），后续章节完全重复。Introduction 应侧重 high-level narrative。\"\n    action_items:\n      - round: 2\n        action: \"压缩 Abstract；Introduction 移除具体数字，侧重叙事\"\n        assigned_to: paper_agent\n        status: queued\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R2-m2\n    summary: \"Table 4 Cosine R1 显示 'collapse' 而非数值\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"作为 summary table 应报告 collapse 前最后稳定 checkpoint 的 SyconScore 或标注 N/A 原因。\"\n    action_items:\n      - round: 2\n        action: \"Table 4 给出 collapse 前最佳 SyconScore 或用标准化符号替代\"\n        assigned_to: paper_agent\n        status: queued\n    resolution: \"\"\n    resolution_round: null"
  }
}
```

</details>

---


### Tool result

_source line 185 · 2026-05-22T11:44:52.208276+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_issues.yaml\", \"bytes\": 16626}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 186 · 2026-05-22T11:47:30.111007+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "contrastive_entrain_calib",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.0 - Findings",
  "report": "# 审稿报告：Discriminability Without Utility: Why Sycophancy Directions Fail as Scalar RL Rewards\n\n**Venue**: EMNLP 2026 (ARR May 2026 cycle)\n**Reviewers**: R1（方法严谨性）、R2（新颖性与完整性）\n**审稿轮次**: Round 2 (fresh)\n**日期**: 2026-05-22\n\n---\n\n## Summary\n\n本文研究表征工程提取的对比谄媚方向（d_syc）能否作为 GRPO 的标量 reward 信号来校准 LLM 的 sycophancy 行为。在 Qwen3-8B 上提取 d_syc（5-fold CV AUROC 0.827）并在 Llama-3-8B 上交叉验证（AUROC 0.779）后，测试了三种 reward 公式（cosine projection、binary probe、continuous probe）共六种 GRPO 配置，全部失败。R3-only GRPO（仅用 NLI 行为 reward）也失败（26 个 checkpoint 仅 4 个超过 vanilla，15.4%），而 ACT（dense per-token SFT）以 SyconScore 0.301 成功（seed 1: 16/16 checkpoints 超过 vanilla）。论文提出三个 contributions：(C1) 所有 GRPO 公式失败，(C2) probe reward 产生 stubbornness trap（behavioral death 先于 distributional collapse），(C3) 标量 per-completion reward 结构性不足。\n\n---\n\n## Strengths\n\n**S1. 问题选取填补重要空白 [R1, R2 一致]**\n首个系统否证 \"representation discriminability → RL reward utility\" 隐含假设的工作。对 representation engineering + RL 社区有直接理论意义。\n\n**S2. 诊断链设计严谨且有教学价值 [R1, R2 一致]**\n§4 的 cosine failure chain（F1a→F1b→F1c→F1d）逐步排除假说，每一步解决前一步的 failure mode 但暴露更深层问题。这种递进式消融是优秀的科学方法论。\n\n**S3. Probe reward trap (C2) 是真正新颖的发现 [R1, R2 一致]**\nBehavioral death（ToF=0 at step 500）先于 distributional collapse（entropy 0.70 持续到 step ~1840），reward 始终保持 +0.72。1,300-step 时间差意味着标准 entropy-based early stopping 完全错过行为退化。对 RLHF 安全监控实践有直接指导意义。\n\n**S4. Cross-model direction validation [R1, R2 一致]**\n在 Llama-3-8B 上独立复现 d_syc extraction，evidence-strength gradient 定性模式一致（weak→medium→strong AUROC 单调递增），表明 d_syc 不是模型特异的。\n\n**S5. Papadatos & Freedman (2024) 对比定位精准 [R2]**\n§6 的 \"inference-time vs training-time × dense vs sparse supervision\" 双维度分析框架，清晰地统一解释了本文 negative result 与已有 positive result。\n\n**S6. Limitations 写作诚实 [R1]**\n主动承认单模型训练、ACT seed 2 不完整、n=2 seeds、supervision granularity confound。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**MF-1 [critical] C3 \"supervision density hypothesis\" 因果声称超出证据范围**\n[R1-N1, R2-N1, R2-N2 — 两位 Reviewer 完全一致，交叉确认]\n\nACT 和 GRPO 至少在 4 个维度同时不同：(a) per-token vs per-completion 梯度粒度，(b) SFT（交叉熵）vs RL（GRPO）目标函数，(c) labeled valid/invalid pairs vs online exploration with reward，(d) L2 activation consistency loss。论文将 ACT 的成功归因于 \"supervision density\"（§6: \"The critical difference is supervision granularity\"），但实验设计无法隔离这一因素。\n\nC3 声称 \"A single scalar reward per completion...cannot teach the model which belief changes are warranted\"，并从 GRPO + 4 种奖励变体推广到整个 per-completion RL 方法族（§6: \"we expect similar failure patterns wherever representation-derived signals are compressed to completion-level scalars\"）。PPO 有 value function 和 clipping 机制，RLOO 有不同的 baseline 估计，这些都可能改变 reward signal 的利用方式。\n\n关键反事实：如果 ACT 的优势来自 labeled supervision 而非 per-token granularity，supervision density hypothesis 就不成立。缺失的关键控制实验：per-completion SFT、token-level RL reward（process reward model）、labeled-pair GRPO。\n\n**建议**：(1) 将 C3 从因果声称降级为观察性发现；(2) \"supervision density is THE critical difference\" → \"ONE plausible contributing factor among several confounded differences\"；(3) 在正文（非仅 Limitations）完整列出 ACT vs GRPO 所有差异维度；(4) §6 对 PPO/RLOO 泛化改为 hypothesis。\n\n**MF-2 [critical] 单模型训练，标题和正文做一般性声称**\n[R1-N2, R2 同意]\n\n所有 RL/SFT 训练仅在 Qwen3-8B 上进行。标题 \"Why Sycophancy Directions Fail as Scalar RL Rewards\" 和 §1 \"structurally insufficient\" 是一般性陈述，但仅有单模型证据。两个模型的 d_syc best layer 不同（L19 vs L16）、AUROC 不同（0.827 vs 0.779），模型间训练动态差异未被排除。\n\nR2 补充：机制论证（d_syc 几何上无法区分 valid revision 和 capitulation）是模型无关的理论论证，可保留为假说，但经验性 claim 需限定范围。\n\n**建议**：(1) 标题或 abstract 限定实验范围（如 \"a case study on Qwen3-8B\"）；(2) 在 Llama-3-8B 上至少复现一个关键训练实验（如 binary probe F2）；(3) \"fail\" → \"failed in our experiments\"，\"structurally insufficient\" → \"insufficient in the tested configuration\"。\n\n**MF-3 [critical] 统计效力不足：n=2 seeds，ACT seed 2 仅 3/16 checkpoints**\n[R1-N3, R2 同意但 severity 稍低]\n\n- n=2 seeds 的 cross-seed rank correlation（ρ≈0.33 after step 4000）缺乏统计意义\n- ACT seed 2 仅 3/16 checkpoints，论文在实验未完成时提交\n- \"4/26 (15.4%) exceed vanilla vs 16/16 (100%)\" 忽略 checkpoint 间时间序列自相关\n\nR2 nuance：定性模式一致性（oscillation amplitude Δ≈0.069，identical crash depth 0.074）在 negative result 论文中有价值。C2 的 probe trap（ToF→0 at step 500）是单次实验即可确认的定性现象，不受 seed 数量限制。\n\n**建议**：(1) 完成 ACT seed 2 全部 16 checkpoints 评估；(2) 增加至少 1 个额外 seed（≥3 total）；(3) 对 Table 4 关键对比报告 bootstrap CI；(4) 如计算资源不足，大幅软化比较性声称。\n\n**MF-4 [critical] 正文超 8 页限制**\n[视觉审查发现]\n\nSections 1-7 占满 pages 1-8，Section 8 (Conclusion) 从 page 9 顶部开始（约 1/4-1/3 列）。EMNLP 2026 / ARR 严格要求 long paper 正文不超过 8 页（Limitations 和 References 不计入），Conclusion 属于正文。**可能触发 desk rejection。**\n\n**建议**：压缩正文或重新排版，确保 Conclusion 在 page 8 底部结束。\n\n### Should-Fix（影响评分但不一票否决）\n\n**SF-1 [warning] SMART (Beigi et al., 2025) 讨论不充分 [R2-W1, R1 同意]**\n§7 仅一句话提及。Supervision density hypothesis 直接预测 SMART 的 per-step process reward 应表现介于 GRPO（per-completion）和 ACT（per-token）之间。未讨论 SMART 实际结果是否验证该预测，是理论完整性缺陷。\n\n**SF-2 [warning] 超参搜索不充分：w1 仅 0.25/0.40 [R1-W3, R2 同意]**\n\"Diagnostic-driven iteration\" 缺乏系统性。对 F2/F3（binary probe R1=0/1 与 w1 关系不大）影响有限，但对 F1 系列可能存在未探索的有效配置。\n\n**SF-3 [warning] 80-84% truncation (max_completion_length=256) [R1-W1, R2 同意]**\n不同 reward formulations 对截断的敏感度可能不同。\"Response-level decisions manifest within 100-200 tokens\" 是未验证的断言。建议至少一个 config 测试 max_completion_length=512。\n\n**SF-4 [warning] Evidence strength 三级标注缺少 IAA [R1-W4, R2 同意]**\n直接影响 §3 evidence-strength stratified AUROC（weak 0.675→medium 0.883→strong 0.929）的可信度。未报告标注者身份、人数和 inter-annotator agreement。\n\n**SF-5 [warning] 可复现性信息严重不足 [R2-W5, R1 同意]**\nGRPO 关键超参数（采样数/group size、KL penalty coefficient、learning rate、batch size）未披露。181 对比对的 GPT-4.1 prompt template 未提供。无代码/数据可用性声明。对 negative result 论文，可复现性尤其重要。\n\n**SF-6 [warning] CRAFT 对比讨论可深化 [R2-W2, R1 部分同意]**\n§7 已提供 CRAFT vs 本文的 geometric separability 框架，但可量化 CRAFT 的 representation gap 与本文 0.098 cosine gap 的差异。R1 认为对比已存在但深度不足。\n\n**SF-7 [warning] \"Latent-GRPO\" 非原文命名 [R2-W4, R1 同意]**\nZhang et al. (2026) 原标题 \"Silence the Judge\"。应使用原文名称或首次引用时标注 \"(hereafter Latent-GRPO)\"。\n\n**SF-8 [warning] 遗漏高度相关工作 [R2-W3, Director 已验证]**\nWu & Tang (2026) \"When Reward Hacking Rebounds\" (arXiv:2604.01476) 在 GRPO 中成功使用 representation-level concept directions 做 advantage modification。与本文 negative result 形成重要对比：representation directions 在 reward hacking detection 中成功进入 GRPO training loop，在 sycophancy 中失败。**已验证真实存在，必须引用。**\n\n### Minor（不影响接收）\n\n- Abstract 接近一整栏，建议压缩到 150-200 词 [R1, R2]\n- Introduction 与后续章节大量数字重复，Introduction 应侧重 high-level narrative [R1, R2]\n- Table 4 Cosine R1 显示 \"collapse\" 而非数值，应报告最后稳定 checkpoint 的 SyconScore [R2, R1]\n- Figure 1 中 Llama-3-8B 仅显示 layers 16-31，完整层 profile 更 informative [R1]\n- Figure 3 多线灰度打印时可能难以区分，建议增加 marker/line style 变化 [视觉审查]\n- §2.1 丢弃 19/200 pairs 是否引入 selection bias [R1]\n- Appendix B Stubbornness Taxonomy 基于单一 checkpoint 手动检查 100 responses，无 IAA [R1]\n- Chen et al. (EMNLP 2025) \"Self-Augmented Preference Alignment\" 未引用 [R2]\n- Lightman et al. (2024) process reward models 与 supervision density 讨论相关 [R1]\n- 建议 supplementary 中同时报告 arithmetic mean 和 harmonic mean 结果以增强 metric 选择透明度\n\n---\n\n## Reviewer Consensus [AGREE]\n\n两位 Reviewer 在以下关键问题上达成完全一致：\n\n1. **MF-1 (C3 overclaim)**：ACT vs GRPO 存在多重混淆变量，\"supervision density hypothesis\" 的因果归因不成立。两位独立识别，交叉完全确认。\n2. **MF-2 (单模型泛化)**：标题和 claim scope 远超实验覆盖范围。\n3. **MF-3 (统计效力)**：n=2 seeds 不足，ACT seed 2 需完成。（R2 severity 稍低但方向一致）\n4. **SF-1 ~ SF-8**：所有 Should-Fix 均获两位一致或部分一致。\n\n## Reviewer Divergence [REBUT — 已解决]\n\n1. **NLI 评估循环性**（R1-W2 提出 vs R2 反驳）：R2 论证循环性**有利于** R3-only GRPO（优化自己被评估的指标），使其失败更有说服力；对 d_syc-based methods 和 ACT 不存在循环。**Director 判断：R2 论证有效，降级为 minor concern。**\n\n2. **SyconScore harmonic mean**（R1-W5 提出 vs R2 反驳）：R2 引用 F-score 类比——precision=0.95 + recall=0.07 的 arithmetic mean 0.51 掩盖了极端不平衡，harmonic mean 是惩罚不平衡的标准做法。**Director 判断：R2 论证有效，harmonic mean 是合理设计。建议 supplementary 中报告 arithmetic mean 结果。**\n\n3. **d_syc 提取方法替代方案**（R2 minor 提出 vs R1 反驳）：R1 指出 recalibration 已将 AUROC 提升至 0.910 仍 fail，更高 discriminability 不解决 geometric overlap 的根本问题。**Director 判断：R1 论证有效，此项不构成实质问题。**\n\n---\n\n## Questions for Authors\n\n1. 如果给 GRPO 提供 labeled valid/invalid pairs（如 expert demonstrations 构建 comparison group），GRPO 是否仍会失败？这能隔离 supervision granularity 和 label availability 两个因素。\n2. Token-level RL reward（如 process reward model 为每个 token 打分）是否改变结论？这能隔离 \"representation direction 问题\" 和 \"per-completion compression 问题\"。\n3. PPO 的 value function 和 clipping mechanism 是否对 reward noise 更鲁棒？排除 PPO 的理由？\n4. Probe reward trap 的 behavioral-before-distributional 时序分离是否在 cosine formulations 中也观察到？\n5. 仅在 strong evidence 子集上训练 RL（利用高判别力区间 AUROC 0.929）是否能避免 conflation？\n6. 更温和的 recalibration 策略（EMA、延长间隔至 1000/2000 步）是否缓解 F1c 的 mode collapse？\n\n---\n\n## Missing References\n\n1. **Wu & Tang (2026) \"When Reward Hacking Rebounds\" (arXiv:2604.01476)** — 在 GRPO 中成功使用 representation-level concept directions，与本文 negative result 形成重要对比。**必须引用。已验证真实存在。**\n2. **Chen, Huang & Chen (2025) \"Self-Augmented Preference Alignment for Sycophancy Reduction\" (EMNLP 2025)** — preference alignment 具体实例，与 DPO/KTO 讨论互补。建议引用。\n3. **Lightman et al. (2024) \"Let's Verify Step by Step\"** — process reward models 经典工作，与 supervision density 讨论直接相关。建议引用。\n4. 建议验证 \"Latent-GRPO\" 命名是否为 Zhang et al. (2026) 原文使用，若非则标注简称来源。\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：**未配置**。项目 `external_review.paperreview_ai.enabled` 未启用。\n\n---\n\n## Visual Layout Check（非评分项）\n\n状态：**已完成**（2026-05-22 11:29→11:33）\n\n| Severity | Finding |\n|----------|---------|\n| **Critical** | 正文超 8 页——Sections 1-7 占满 pages 1-8，Conclusion 从 page 9 开始（约 1/4-1/3 列）。已提升为 MF-4。 |\n| Warning | 前 3 页无 figure/table（首个 display item 在 page 4），审稿人缺乏视觉锚点。建议 page 1-2 加 motivating figure 或核心结果 teaser。 |\n| Warning | Pages 1-2 连续纯文本，视觉节奏单调。 |\n| Warning | Pages 8-9 连续无 display item（Related Work + Conclusion），与 pages 4-7 密集图表形成节奏落差。 |\n| Info | Figure 2 双 y 轴确保标签清晰；Figure 3 多线灰度区分可改善；Table 4 \"collapse\" 文本可标准化；Figure 1 和 booktabs 表格质量好；无 margin 溢出或未解析引用。 |\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.0 — Findings**\n**Confidence: 4/5**\n\n### 评分理由\n\n论文的贡献在证据强度上呈现明显分层：\n\n**C1（d_syc-based reward 失败）和 C2（probe reward trap）有较强实验支持。** 六种 GRPO 配置一致失败，诊断链设计优秀。Probe trap 的 behavioral-before-distributional collapse（1,300-step 时间差，reward +0.72 全程）具有独立价值和实际安全意义。这两个贡献达到 Findings 标准。\n\n**C3（supervision density hypothesis）是证据最薄弱的环节，恰恰也是论文试图从 diagnostic paper 升级为 explanatory paper 的关键。** ACT vs GRPO 对比存在至少 4 个混淆变量（两位 Reviewer 完全一致），单模型训练不支持标题和正文的一般性声称，n=2 seeds 且 ACT seed 2 不完整进一步削弱统计基础。\n\n**格式问题**：正文超 8 页限制，在 ARR 可能触发 desk rejection。\n\n**Reviewer 评分分布**：R1 = 3.0（Findings），R2 = 3.5（Borderline Conference）。分歧在 0.5 分以内，核心问题判断一致。R1 额外重视统计效力和单模型泛化；R2 对定性模式一致性和 C2 的独立价值给予更多信用。\n\n**综合判断**：以 C1+C2 为核心，论文定位为 Findings 是合理的。如果作者能 (1) 将 C3 从因果声称降级为观察性发现, (2) 限定标题和 claim 范围, (3) 完成 ACT seed 2 全部评估, (4) 解决正文超页问题, 论文可在 Findings 得到稳固接收，且有潜力达到 3.5 (Borderline Conference)。当前状态下，C3 的 overclaim 和格式违规阻碍了更高评分。\n\n### 修改优先级\n\n1. **MF-4**: 正文超页（格式硬伤，立即修复）\n2. **MF-1**: C3 因果声称降级 + 混淆变量讨论（核心叙事调整）\n3. **MF-2**: 标题和 claim 限定实验范围\n4. **MF-3**: 完成 ACT seed 2 + 增强统计报告\n5. **SF-1→SF-8**: 按 severity 排序\n\n---\n\n## Detailed Comments（逐节）\n\n**Abstract**: 过长（接近一整栏），包含过多实验细节。建议压缩到 150-200 词，保留核心发现和 insight。\n\n**§1 Introduction**: (1) 具体数字（AUROC 0.827、σ=0.028、15.4% 等）与后续章节完全重复，建议移除，侧重 high-level narrative；(2) C3 贡献声明措辞需软化——从 \"cannot teach\" 改为 \"failed to teach in our experiments\"。\n\n**§2 Experimental Framework**: (1) §2.1 pairs 构建过程现已描述（GPT-4.1 pipeline、style matching validation），但 evidence strength 标注的 annotator 信息和 IAA 仍缺失；(2) §2.2 w1 选择说明仍不充分（仅两个值）；(3) §2.5 SyconScore harmonic mean 的 justification 可接受（F-score 类比），建议 supplementary 中补充 arithmetic mean 结果。\n\n**§3 Direction Discriminability**: 质量好。Cross-model validation、evidence-strength stratification、training stability 分析全面。Figure 1 清晰。\n\n**§4 Cosine R1 Failure**: 诊断链设计优秀。Table 2 和论证逻辑清晰。\n\n**§5 Probe Reward Trap**: C2 是论文最强的贡献。Table 3 和 Figure 2 有效展示 behavioral-before-distributional collapse。Stubbornness taxonomy (Appendix B) 提供 ground-level 理解。\n\n**§6 Analysis**: (1) \"The critical difference is supervision granularity\" 需大幅弱化；(2) 应在此节（非仅 Limitations）完整列出 ACT vs GRPO 的所有差异维度；(3) PPO/RLOO 泛化声称改为 hypothesis；(4) SMART 讨论需扩展；(5) \"When Reward Hacking Rebounds\" 应在此节引用讨论。\n\n**§7 Related Work**: (1) CRAFT 对比可深化——量化 representation gap 差异；(2) \"Latent-GRPO\" 命名需确认来源；(3) 补充 arXiv:2604.01476 和 Lightman et al. (2024)。\n\n**§8 Conclusion**: 需压缩到 page 8 以内。措辞限定实验范围。\n\n**Limitations**: 写作诚实，但 supervision granularity confound 的讨论应在正文中更突出，而非仅在 Limitations 中提及。\n\n**Appendix A**: 需补充完整 GRPO 超参数表。Truncation 已披露但影响分析不足。\n\n**References**: (1) 当前 bib 条目格式比 Round 1 改善明显；(2) 需补充 arXiv:2604.01476；(3) 建议补充 Chen et al. (EMNLP 2025) 和 Lightman et al. (2024)。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "project": "contrastive_entrain_calib",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.0 - Findings",
    "report": "# 审稿报告：Discriminability Without Utility: Why Sycophancy Directions Fail as Scalar RL Rewards\n\n**Venue**: EMNLP 2026 (ARR May 2026 cycle)\n**Reviewers**: R1（方法严谨性）、R2（新颖性与完整性）\n**审稿轮次**: Round 2 (fresh)\n**日期**: 2026-05-22\n\n---\n\n## Summary\n\n本文研究表征工程提取的对比谄媚方向（d_syc）能否作为 GRPO 的标量 reward 信号来校准 LLM 的 sycophancy 行为。在 Qwen3-8B 上提取 d_syc（5-fold CV AUROC 0.827）并在 Llama-3-8B 上交叉验证（AUROC 0.779）后，测试了三种 reward 公式（cosine projection、binary probe、continuous probe）共六种 GRPO 配置，全部失败。R3-only GRPO（仅用 NLI 行为 reward）也失败（26 个 checkpoint 仅 4 个超过 vanilla，15.4%），而 ACT（dense per-token SFT）以 SyconScore 0.301 成功（seed 1: 16/16 checkpoints 超过 vanilla）。论文提出三个 contributions：(C1) 所有 GRPO 公式失败，(C2) probe reward 产生 stubbornness trap（behavioral death 先于 distributional collapse），(C3) 标量 per-completion reward 结构性不足。\n\n---\n\n## Strengths\n\n**S1. 问题选取填补重要空白 [R1, R2 一致]**\n首个系统否证 \"representation discriminability → RL reward utility\" 隐含假设的工作。对 representation engineering + RL 社区有直接理论意义。\n\n**S2. 诊断链设计严谨且有教学价值 [R1, R2 一致]**\n§4 的 cosine failure chain（F1a→F1b→F1c→F1d）逐步排除假说，每一步解决前一步的 failure mode 但暴露更深层问题。这种递进式消融是优秀的科学方法论。\n\n**S3. Probe reward trap (C2) 是真正新颖的发现 [R1, R2 一致]**\nBehavioral death（ToF=0 at step 500）先于 distributional collapse（entropy 0.70 持续到 step ~1840），reward 始终保持 +0.72。1,300-step 时间差意味着标准 entropy-based early stopping 完全错过行为退化。对 RLHF 安全监控实践有直接指导意义。\n\n**S4. Cross-model direction validation [R1, R2 一致]**\n在 Llama-3-8B 上独立复现 d_syc extraction，evidence-strength gradient 定性模式一致（weak→medium→strong AUROC 单调递增），表明 d_syc 不是模型特异的。\n\n**S5. Papadatos & Freedman (2024) 对比定位精准 [R2]**\n§6 的 \"inference-time vs training-time × dense vs sparse supervision\" 双维度分析框架，清晰地统一解释了本文 negative result 与已有 positive result。\n\n**S6. Limitations 写作诚实 [R1]**\n主动承认单模型训练、ACT seed 2 不完整、n=2 seeds、supervision granularity confound。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**MF-1 [critical] C3 \"supervision density hypothesis\" 因果声称超出证据范围**\n[R1-N1, R2-N1, R2-N2 — 两位 Reviewer 完全一致，交叉确认]\n\nACT 和 GRPO 至少在 4 个维度同时不同：(a) per-token vs per-completion 梯度粒度，(b) SFT（交叉熵）vs RL（GRPO）目标函数，(c) labeled valid/invalid pairs vs online exploration with reward，(d) L2 activation consistency loss。论文将 ACT 的成功归因于 \"supervision density\"（§6: \"The critical difference is supervision granularity\"），但实验设计无法隔离这一因素。\n\nC3 声称 \"A single scalar reward per completion...cannot teach the model which belief changes are warranted\"，并从 GRPO + 4 种奖励变体推广到整个 per-completion RL 方法族（§6: \"we expect similar failure patterns wherever representation-derived signals are compressed to completion-level scalars\"）。PPO 有 value function 和 clipping 机制，RLOO 有不同的 baseline 估计，这些都可能改变 reward signal 的利用方式。\n\n关键反事实：如果 ACT 的优势来自 labeled supervision 而非 per-token granularity，supervision density hypothesis 就不成立。缺失的关键控制实验：per-completion SFT、token-level RL reward（process reward model）、labeled-pair GRPO。\n\n**建议**：(1) 将 C3 从因果声称降级为观察性发现；(2) \"supervision density is THE critical difference\" → \"ONE plausible contributing factor among several confounded differences\"；(3) 在正文（非仅 Limitations）完整列出 ACT vs GRPO 所有差异维度；(4) §6 对 PPO/RLOO 泛化改为 hypothesis。\n\n**MF-2 [critical] 单模型训练，标题和正文做一般性声称**\n[R1-N2, R2 同意]\n\n所有 RL/SFT 训练仅在 Qwen3-8B 上进行。标题 \"Why Sycophancy Directions Fail as Scalar RL Rewards\" 和 §1 \"structurally insufficient\" 是一般性陈述，但仅有单模型证据。两个模型的 d_syc best layer 不同（L19 vs L16）、AUROC 不同（0.827 vs 0.779），模型间训练动态差异未被排除。\n\nR2 补充：机制论证（d_syc 几何上无法区分 valid revision 和 capitulation）是模型无关的理论论证，可保留为假说，但经验性 claim 需限定范围。\n\n**建议**：(1) 标题或 abstract 限定实验范围（如 \"a case study on Qwen3-8B\"）；(2) 在 Llama-3-8B 上至少复现一个关键训练实验（如 binary probe F2）；(3) \"fail\" → \"failed in our experiments\"，\"structurally insufficient\" → \"insufficient in the tested configuration\"。\n\n**MF-3 [critical] 统计效力不足：n=2 seeds，ACT seed 2 仅 3/16 checkpoints**\n[R1-N3, R2 同意但 severity 稍低]\n\n- n=2 seeds 的 cross-seed rank correlation（ρ≈0.33 after step 4000）缺乏统计意义\n- ACT seed 2 仅 3/16 checkpoints，论文在实验未完成时提交\n- \"4/26 (15.4%) exceed vanilla vs 16/16 (100%)\" 忽略 checkpoint 间时间序列自相关\n\nR2 nuance：定性模式一致性（oscillation amplitude Δ≈0.069，identical crash depth 0.074）在 negative result 论文中有价值。C2 的 probe trap（ToF→0 at step 500）是单次实验即可确认的定性现象，不受 seed 数量限制。\n\n**建议**：(1) 完成 ACT seed 2 全部 16 checkpoints 评估；(2) 增加至少 1 个额外 seed（≥3 total）；(3) 对 Table 4 关键对比报告 bootstrap CI；(4) 如计算资源不足，大幅软化比较性声称。\n\n**MF-4 [critical] 正文超 8 页限制**\n[视觉审查发现]\n\nSections 1-7 占满 pages 1-8，Section 8 (Conclusion) 从 page 9 顶部开始（约 1/4-1/3 列）。EMNLP 2026 / ARR 严格要求 long paper 正文不超过 8 页（Limitations 和 References 不计入），Conclusion 属于正文。**可能触发 desk rejection。**\n\n**建议**：压缩正文或重新排版，确保 Conclusion 在 page 8 底部结束。\n\n### Should-Fix（影响评分但不一票否决）\n\n**SF-1 [warning] SMART (Beigi et al., 2025) 讨论不充分 [R2-W1, R1 同意]**\n§7 仅一句话提及。Supervision density hypothesis 直接预测 SMART 的 per-step process reward 应表现介于 GRPO（per-completion）和 ACT（per-token）之间。未讨论 SMART 实际结果是否验证该预测，是理论完整性缺陷。\n\n**SF-2 [warning] 超参搜索不充分：w1 仅 0.25/0.40 [R1-W3, R2 同意]**\n\"Diagnostic-driven iteration\" 缺乏系统性。对 F2/F3（binary probe R1=0/1 与 w1 关系不大）影响有限，但对 F1 系列可能存在未探索的有效配置。\n\n**SF-3 [warning] 80-84% truncation (max_completion_length=256) [R1-W1, R2 同意]**\n不同 reward formulations 对截断的敏感度可能不同。\"Response-level decisions manifest within 100-200 tokens\" 是未验证的断言。建议至少一个 config 测试 max_completion_length=512。\n\n**SF-4 [warning] Evidence strength 三级标注缺少 IAA [R1-W4, R2 同意]**\n直接影响 §3 evidence-strength stratified AUROC（weak 0.675→medium 0.883→strong 0.929）的可信度。未报告标注者身份、人数和 inter-annotator agreement。\n\n**SF-5 [warning] 可复现性信息严重不足 [R2-W5, R1 同意]**\nGRPO 关键超参数（采样数/group size、KL penalty coefficient、learning rate、batch size）未披露。181 对比对的 GPT-4.1 prompt template 未提供。无代码/数据可用性声明。对 negative result 论文，可复现性尤其重要。\n\n**SF-6 [warning] CRAFT 对比讨论可深化 [R2-W2, R1 部分同意]**\n§7 已提供 CRAFT vs 本文的 geometric separability 框架，但可量化 CRAFT 的 representation gap 与本文 0.098 cosine gap 的差异。R1 认为对比已存在但深度不足。\n\n**SF-7 [warning] \"Latent-GRPO\" 非原文命名 [R2-W4, R1 同意]**\nZhang et al. (2026) 原标题 \"Silence the Judge\"。应使用原文名称或首次引用时标注 \"(hereafter Latent-GRPO)\"。\n\n**SF-8 [warning] 遗漏高度相关工作 [R2-W3, Director 已验证]**\nWu & Tang (2026) \"When Reward Hacking Rebounds\" (arXiv:2604.01476) 在 GRPO 中成功使用 representation-level concept directions 做 advantage modification。与本文 negative result 形成重要对比：representation directions 在 reward hacking detection 中成功进入 GRPO training loop，在 sycophancy 中失败。**已验证真实存在，必须引用。**\n\n### Minor（不影响接收）\n\n- Abstract 接近一整栏，建议压缩到 150-200 词 [R1, R2]\n- Introduction 与后续章节大量数字重复，Introduction 应侧重 high-level narrative [R1, R2]\n- Table 4 Cosine R1 显示 \"collapse\" 而非数值，应报告最后稳定 checkpoint 的 SyconScore [R2, R1]\n- Figure 1 中 Llama-3-8B 仅显示 layers 16-31，完整层 profile 更 informative [R1]\n- Figure 3 多线灰度打印时可能难以区分，建议增加 marker/line style 变化 [视觉审查]\n- §2.1 丢弃 19/200 pairs 是否引入 selection bias [R1]\n- Appendix B Stubbornness Taxonomy 基于单一 checkpoint 手动检查 100 responses，无 IAA [R1]\n- Chen et al. (EMNLP 2025) \"Self-Augmented Preference Alignment\" 未引用 [R2]\n- Lightman et al. (2024) process reward models 与 supervision density 讨论相关 [R1]\n- 建议 supplementary 中同时报告 arithmetic mean 和 harmonic mean 结果以增强 metric 选择透明度\n\n---\n\n## Reviewer Consensus [AGREE]\n\n两位 Reviewer 在以下关键问题上达成完全一致：\n\n1. **MF-1 (C3 overclaim)**：ACT vs GRPO 存在多重混淆变量，\"supervision density hypothesis\" 的因果归因不成立。两位独立识别，交叉完全确认。\n2. **MF-2 (单模型泛化)**：标题和 claim scope 远超实验覆盖范围。\n3. **MF-3 (统计效力)**：n=2 seeds 不足，ACT seed 2 需完成。（R2 severity 稍低但方向一致）\n4. **SF-1 ~ SF-8**：所有 Should-Fix 均获两位一致或部分一致。\n\n## Reviewer Divergence [REBUT — 已解决]\n\n1. **NLI 评估循环性**（R1-W2 提出 vs R2 反驳）：R2 论证循环性**有利于** R3-only GRPO（优化自己被评估的指标），使其失败更有说服力；对 d_syc-based methods 和 ACT 不存在循环。**Director 判断：R2 论证有效，降级为 minor concern。**\n\n2. **SyconScore harmonic mean**（R1-W5 提出 vs R2 反驳）：R2 引用 F-score 类比——precision=0.95 + recall=0.07 的 arithmetic mean 0.51 掩盖了极端不平衡，harmonic mean 是惩罚不平衡的标准做法。**Director 判断：R2 论证有效，harmonic mean 是合理设计。建议 supplementary 中报告 arithmetic mean 结果。**\n\n3. **d_syc 提取方法替代方案**（R2 minor 提出 vs R1 反驳）：R1 指出 recalibration 已将 AUROC 提升至 0.910 仍 fail，更高 discriminability 不解决 geometric overlap 的根本问题。**Director 判断：R1 论证有效，此项不构成实质问题。**\n\n---\n\n## Questions for Authors\n\n1. 如果给 GRPO 提供 labeled valid/invalid pairs（如 expert demonstrations 构建 comparison group），GRPO 是否仍会失败？这能隔离 supervision granularity 和 label availability 两个因素。\n2. Token-level RL reward（如 process reward model 为每个 token 打分）是否改变结论？这能隔离 \"representation direction 问题\" 和 \"per-completion compression 问题\"。\n3. PPO 的 value function 和 clipping mechanism 是否对 reward noise 更鲁棒？排除 PPO 的理由？\n4. Probe reward trap 的 behavioral-before-distributional 时序分离是否在 cosine formulations 中也观察到？\n5. 仅在 strong evidence 子集上训练 RL（利用高判别力区间 AUROC 0.929）是否能避免 conflation？\n6. 更温和的 recalibration 策略（EMA、延长间隔至 1000/2000 步）是否缓解 F1c 的 mode collapse？\n\n---\n\n## Missing References\n\n1. **Wu & Tang (2026) \"When Reward Hacking Rebounds\" (arXiv:2604.01476)** — 在 GRPO 中成功使用 representation-level concept directions，与本文 negative result 形成重要对比。**必须引用。已验证真实存在。**\n2. **Chen, Huang & Chen (2025) \"Self-Augmented Preference Alignment for Sycophancy Reduction\" (EMNLP 2025)** — preference alignment 具体实例，与 DPO/KTO 讨论互补。建议引用。\n3. **Lightman et al. (2024) \"Let's Verify Step by Step\"** — process reward models 经典工作，与 supervision density 讨论直接相关。建议引用。\n4. 建议验证 \"Latent-GRPO\" 命名是否为 Zhang et al. (2026) 原文使用，若非则标注简称来源。\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：**未配置**。项目 `external_review.paperreview_ai.enabled` 未启用。\n\n---\n\n## Visual Layout Check（非评分项）\n\n状态：**已完成**（2026-05-22 11:29→11:33）\n\n| Severity | Finding |\n|----------|---------|\n| **Critical** | 正文超 8 页——Sections 1-7 占满 pages 1-8，Conclusion 从 page 9 开始（约 1/4-1/3 列）。已提升为 MF-4。 |\n| Warning | 前 3 页无 figure/table（首个 display item 在 page 4），审稿人缺乏视觉锚点。建议 page 1-2 加 motivating figure 或核心结果 teaser。 |\n| Warning | Pages 1-2 连续纯文本，视觉节奏单调。 |\n| Warning | Pages 8-9 连续无 display item（Related Work + Conclusion），与 pages 4-7 密集图表形成节奏落差。 |\n| Info | Figure 2 双 y 轴确保标签清晰；Figure 3 多线灰度区分可改善；Table 4 \"collapse\" 文本可标准化；Figure 1 和 booktabs 表格质量好；无 margin 溢出或未解析引用。 |\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.0 — Findings**\n**Confidence: 4/5**\n\n### 评分理由\n\n论文的贡献在证据强度上呈现明显分层：\n\n**C1（d_syc-based reward 失败）和 C2（probe reward trap）有较强实验支持。** 六种 GRPO 配置一致失败，诊断链设计优秀。Probe trap 的 behavioral-before-distributional collapse（1,300-step 时间差，reward +0.72 全程）具有独立价值和实际安全意义。这两个贡献达到 Findings 标准。\n\n**C3（supervision density hypothesis）是证据最薄弱的环节，恰恰也是论文试图从 diagnostic paper 升级为 explanatory paper 的关键。** ACT vs GRPO 对比存在至少 4 个混淆变量（两位 Reviewer 完全一致），单模型训练不支持标题和正文的一般性声称，n=2 seeds 且 ACT seed 2 不完整进一步削弱统计基础。\n\n**格式问题**：正文超 8 页限制，在 ARR 可能触发 desk rejection。\n\n**Reviewer 评分分布**：R1 = 3.0（Findings），R2 = 3.5（Borderline Conference）。分歧在 0.5 分以内，核心问题判断一致。R1 额外重视统计效力和单模型泛化；R2 对定性模式一致性和 C2 的独立价值给予更多信用。\n\n**综合判断**：以 C1+C2 为核心，论文定位为 Findings 是合理的。如果作者能 (1) 将 C3 从因果声称降级为观察性发现, (2) 限定标题和 claim 范围, (3) 完成 ACT seed 2 全部评估, (4) 解决正文超页问题, 论文可在 Findings 得到稳固接收，且有潜力达到 3.5 (Borderline Conference)。当前状态下，C3 的 overclaim 和格式违规阻碍了更高评分。\n\n### 修改优先级\n\n1. **MF-4**: 正文超页（格式硬伤，立即修复）\n2. **MF-1**: C3 因果声称降级 + 混淆变量讨论（核心叙事调整）\n3. **MF-2**: 标题和 claim 限定实验范围\n4. **MF-3**: 完成 ACT seed 2 + 增强统计报告\n5. **SF-1→SF-8**: 按 severity 排序\n\n---\n\n## Detailed Comments（逐节）\n\n**Abstract**: 过长（接近一整栏），包含过多实验细节。建议压缩到 150-200 词，保留核心发现和 insight。\n\n**§1 Introduction**: (1) 具体数字（AUROC 0.827、σ=0.028、15.4% 等）与后续章节完全重复，建议移除，侧重 high-level narrative；(2) C3 贡献声明措辞需软化——从 \"cannot teach\" 改为 \"failed to teach in our experiments\"。\n\n**§2 Experimental Framework**: (1) §2.1 pairs 构建过程现已描述（GPT-4.1 pipeline、style matching validation），但 evidence strength 标注的 annotator 信息和 IAA 仍缺失；(2) §2.2 w1 选择说明仍不充分（仅两个值）；(3) §2.5 SyconScore harmonic mean 的 justification 可接受（F-score 类比），建议 supplementary 中补充 arithmetic mean 结果。\n\n**§3 Direction Discriminability**: 质量好。Cross-model validation、evidence-strength stratification、training stability 分析全面。Figure 1 清晰。\n\n**§4 Cosine R1 Failure**: 诊断链设计优秀。Table 2 和论证逻辑清晰。\n\n**§5 Probe Reward Trap**: C2 是论文最强的贡献。Table 3 和 Figure 2 有效展示 behavioral-before-distributional collapse。Stubbornness taxonomy (Appendix B) 提供 ground-level 理解。\n\n**§6 Analysis**: (1) \"The critical difference is supervision granularity\" 需大幅弱化；(2) 应在此节（非仅 Limitations）完整列出 ACT vs GRPO 的所有差异维度；(3) PPO/RLOO 泛化声称改为 hypothesis；(4) SMART 讨论需扩展；(5) \"When Reward Hacking Rebounds\" 应在此节引用讨论。\n\n**§7 Related Work**: (1) CRAFT 对比可深化——量化 representation gap 差异；(2) \"Latent-GRPO\" 命名需确认来源；(3) 补充 arXiv:2604.01476 和 Lightman et al. (2024)。\n\n**§8 Conclusion**: 需压缩到 page 8 以内。措辞限定实验范围。\n\n**Limitations**: 写作诚实，但 supervision granularity confound 的讨论应在正文中更突出，而非仅在 Limitations 中提及。\n\n**Appendix A**: 需补充完整 GRPO 超参数表。Truncation 已披露但影响分析不足。\n\n**References**: (1) 当前 bib 条目格式比 Round 1 改善明显；(2) 需补充 arXiv:2604.01476；(3) 建议补充 Chen et al. (EMNLP 2025) 和 Lightman et al. (2024)。"
  }
}
```

</details>

---


### Tool result

_source line 187 · 2026-05-22T11:47:34.636933+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_c77a380fad2d0408ce92cd1170d46f6f:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4525
}
```

</details>

---


### Assistant

_source line 188 · 2026-05-22T11:47:43.409608+00:00_

审稿报告已投递至 Research Director。

---

**审稿完成总结**：

- **Overall Score: 3.0 (Findings)**
- **4 个 Must-Fix**：(1) C3 supervision density hypothesis 因果声称超出证据范围（两位 Reviewer 完全一致）；(2) 单模型训练但做一般性声称；(3) n=2 seeds 且 ACT seed 2 仅 3/16 完成；(4) 正文超 8 页限制（视觉审查发现）
- **8 个 Should-Fix**：SMART 讨论不足、超参搜索不充分、80% truncation、IAA 缺失、可复现性信息不足、CRAFT 对比可深化、Latent-GRPO 命名、遗漏 arXiv:2604.01476
- **核心判断**：C1（d_syc reward 失败）和 C2（probe reward trap）有较强证据支持，达到 Findings 标准。C3 的 overclaim 是阻碍更高评分的主要原因。修改优先级：超页 > C3 降级 > claim 限定 > 完成 seed 2。
- **Issue Tracker** 已同步更新（17 条旧 issue + 5 条新 issue）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director"
}
```

</details>

---


## Round 16

## Round 16

2 recorded events


### User

_source line 189 · 2026-05-22T11:47:46.039108+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。总结：

- **N1 (混淆变量)**: [AGREE] — 与我自己的 N2 一致，ACT vs GRPO 有 4 个同时变化维度
- **N2 (单模型)**: [AGREE] — 标题和声称的泛化性超出实验证据
- **N3 (统计效力)**: [AGREE with nuance] — n=2 确实不足，但定性模式一致性仍有价值
- **W1 (truncation)**: [AGREE]
- **W2 (NLI 循环性)**: [REBUT] — 循环性仅影响 R3-only GRPO，且有利于它（failure 更有说服力）
- **W3 (超参搜索)**: [AGREE]
- **W4 (标注 IAA)**: [AGREE]
- **W5 (harmonic mean)**: [REBUT] — 与 F-score 逻辑一致，arithmetic mean 会掩盖极端不平衡

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 190 · 2026-05-22T11:47:59.858385+00:00_

审稿报告已成功投递至 Research Director。

**本轮审稿总结**：

- **Overall Score: 3.0（Findings）**
- **Reviewer 评分**：R1 = 3.0，R2 = 3.5，综合取 3.0
- **4 个 Must-Fix**：(1) C3 supervision density hypothesis 因果声称超出证据（4+ 混淆变量），(2) 单模型训练但做一般性声称，(3) n=2 seeds 且 ACT seed 2 仅 3/16，(4) 正文超 8 页限制
- **8 个 Should-Fix**：SMART 讨论不足、超参搜索不充分、80% truncation、标注 IAA 缺失、可复现性信息不足、CRAFT 对比可深化、Latent-GRPO 命名、遗漏 arXiv:2604.01476
- **3 个分歧已解决**：NLI 循环性（R2 反驳有效）、harmonic mean（R2 反驳有效）、d_syc 提取方法（R1 反驳有效）
- **Issue Tracker 已同步更新**（17 条 Round 1 issues + 5 条新 Round 2 issues）

论文以 C1（d_syc reward 失败诊断链）和 C2（probe reward trap）为核心可稳固定位于 Findings。升级到 Borderline Conference 需要：软化 C3 因果声称、限定 claim 范围、完成 ACT seed 2、解决超页问题。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director"
}
```

</details>

---


## Round 17

## Round 17

62 recorded events


### User

_source line 191 · 2026-05-22T12:38:02.054524+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: contrastive_entrain_calib
- 论文路径: projects/contrastive_entrain_calib/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 截止日期: 2026-05-25
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 192 · 2026-05-22T12:38:08.656531+00:00_

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
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 193 · 2026-05-22T12:38:08.707658+00:00_

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
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 194 · 2026-05-22T12:38:16.440356+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,read_project_file,dispatch_visual_check,request_external_review,get_external_review_status,director_post_to_reviewer,submit_review_report_to_research_director,get_visual_check_status,update_review_issues,WebSearch,read_local_file",
  "max_results": "11"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,read_project_file,dispatch_visual_check,request_external_review,get_external_review_status,director_post_to_reviewer,submit_review_report_to_research_director,get_visual_check_status,update_review_issues,WebSearch,read_local_file",
    "max_results": "11"
  }
}
```

</details>

---


### Tool result

_source line 195 · 2026-05-22T12:38:16.490994+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 196 · 2026-05-22T12:38:19.556097+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "contrastive_entrain_calib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "contrastive_entrain_calib"
  }
}
```

</details>

---


### Tool result

_source line 197 · 2026-05-22T12:38:20.559238+00:00_

{"result":"# 项目 contrastive_entrain_calib 概况\n\n## 实验状态 (77 个)\n\n- **exp-003-eval-ckpt1000**: DONE (negative) — \n- **exp-003-eval-ckpt5000**: DONE (negative) — \n- **exp-009**: DONE (negative) — \n- **exp-012**: DONE (success) — \n- **exp-002v3**: DONE (negative) — \n- **exp-008v3**: DONE (negative) — \n- **exp002v2-recalib**: DONE (negative) — \n- **exp-003-s2**: RUNNING — \n- **exp-016**: DONE (negative) — \n- **exp-014**: DONE (killed) — \n- **vanilla-baseline**: DONE (success) — \n- **exp-002v2**: DONE (killed) — \n- **exp-002**: DONE (killed) — \n- **exp-008**: DONE (killed) — \n- **exp-001**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-22\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| exp-004-s2-v2 | ACT (SFT) seed 2 训练恢复：从 ckpt-2000 resume，验证 ACT 跨 seed 稳定性。原 exp-004-s2 因磁盘满在 step 2500 崩溃，现已迁移 output_dir 到数据盘恢复训练。 | — | — | — |\n| exp-003-s2 | R3-only GRPO baseline (seed 2): training with only the external DeBERTa reward (r3_weight=1.0, r1=r2=0) provides a lower bound for ablation, isolating the contribution of contrastive direction-based rewards (R1+R2). Seed 2 (seed=43) verifies reproducibility of seed 1 results. | — | — | — |\n\n## 待处理\n- exp-003-s2-eval-ckpt3000: Eval exp-003-s2 (R3-only seed 2) checkpoint-3000 with D027 unified preset. Cross-seed reproducibility: compare with seed 1 ckpt-3000 (SYCONScore=0.095) for exact step match.（排队等待 GPU）\n- exp-003-s2-eval-ckpt2500: Eval exp-003-s2 (R3-only seed 2) checkpoint-2500 with D027 unified preset. Cross-seed reproducibility: compare with seed 1 ckpt-3000 (SYCONScore=0.095) for trajectory alignment.（排队等待 GPU）\n\n## 近期结论\n- **exp-004-s2** (failed): ACT (SFT) seed 2 训练：验证 ACT 跨 seed 稳定性。Seed 1 (exp-004) 16/16 checkpoints > vanilla (0.170→0.301)。如果 seed 2 也展现类似 trajectory，则堵住 Reviewer \"ACT 只有 1 个 seed\" 攻击面。配置与 exp-004 完全相同，仅 seed=42→43。 ← 基于 exp-004\n- **exp-004-s2-eval-ckpt2500** (failed): Eval exp-004-s2 (ACT seed 2) c
…[truncated 1031 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1003
}
```

</details>

---


### Tool call

_source line 198 · 2026-05-22T12:38:20.559768+00:00_

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
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission guidelines ARR site:aclweb.org"
  }
}
```

</details>

---


### Tool call

_source line 199 · 2026-05-22T12:38:22.315765+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 200 · 2026-05-22T12:38:22.416638+00:00_

1	\documentclass[11pt,a4paper]{article}
2	\usepackage[hyperref]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage{amsmath}
6	\usepackage{amssymb}
7	\usepackage{booktabs}
8	\usepackage{multirow}
9	\usepackage{graphicx}
10	\usepackage{xcolor}
11	\usepackage{subcaption}
12	
13	\newcommand{\dsyc}{d_{\text{syc}}}
14	\newcommand{\tof}{\text{ToF}}
15	\newcommand{\nof}{\text{NoF}}
16	\newcommand{\sycon}{\textsc{SyconScore}}
17	\newcommand{\rone}{R_1}
18	\newcommand{\rthree}{R_3}
19	
20	\title{Discriminability Without Utility: Why Sycophancy Directions Fail as Scalar RL Rewards}
21	
22	\author{Anonymous}
23	
24	\begin{document}
25	\maketitle
26	
27	\begin{abstract}
28	\input{sections/abstract}
29	\end{abstract}
30	
31	\input{sections/introduction}
32	
33	\input{sections/framework}
34	
35	\input{sections/direction_quality}
36	
37	\input{sections/cosine_failure}
38	
39	\input{sections/probe_trap}
40	
41	\input{sections/discussion}
42	
43	\input{sections/related_work}
44	
45	\input{sections/conclusion}
46	
47	\section*{Limitations}
48	\input{sections/limitations}
49	
50	\section*{Reproducibility}
51	Code and data will be released upon acceptance. All training hyperparameters are reported in Appendix~\ref{app:training}. The 181 contrastive pairs and evaluation benchmark are included in the supplementary materials.
52	
53	\bibliography{references}
54	
55	\appendix
56	\input{sections/appendix}
57	
58	\end{document}
59	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool result

_source line 201 · 2026-05-22T12:38:25.883205+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines ARR site:aclweb.org"

Links: [{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"*SEM 2026: Commitment Link for ARR-Reviewed Papers (Deadline: 10 April 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/sem-2026-commitment-link-arr-reviewed-papers-deadline-10-april-2026"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"The 64th Annual Meeting of the Association for Computational Linguistics - ACL 2026","url":"https://2026.aclweb.org/"},{"title":"Call for Papers: The 20th Linguistic Annotation Workshop (LAW XX), co-located with ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-20th-linguistic-annotation-workshop-law-xx-co-located-acl-2026"},{"title":"EMNLP 2025: Call for System Demonstrations | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-call-system-demonstrations"},{"title":"Jan. 2025 ACL Standing Committee on Peer Review (COPR) Report 1","url":"https://www.aclweb.org/adminwiki/images/9/9e/COPR-5-cycle-report-to-publish.pdf"}]

I've performed the web search for EMNLP 2026 call for papers submission guidelines with AR
…[truncated 1150 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "WebSearch",
  "elapsed_ms": 5323
}
```

</details>

---


### Tool call

_source line 202 · 2026-05-22T12:38:30.608989+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 submission deadline ARR cycle page limit format"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 submission deadline ARR cycle page limit format"
  }
}
```

</details>

---


### Tool call

_source line 203 · 2026-05-22T12:38:31.062737+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"ARR 2026\" submission guidelines author instructions page limit"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"ARR 2026\" submission guidelines author instructions page limit"
  }
}
```

</details>

---


### Tool call

_source line 204 · 2026-05-22T12:38:33.020683+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "sections/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "sections/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 205 · 2026-05-22T12:38:33.071414+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 206 · 2026-05-22T12:38:36.840515+00:00_

Web search results for query: "EMNLP 2026 submission deadline ARR cycle page limit format"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"EMNLP 2026 LaTeX Template | ACL Style Files & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/emnlp"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"EMNLP 2026 (@emnlpmeeting) / Posts / X","url":"https://x.com/emnlpmeeting?lang=en"}]

Based on the search results, here is the information about EMNLP 2026 submissions through ACL Rolling Review (ARR):

## Key Submission Information:

**Submission Deadline:**
The ARR submission deadline is May 25, 2026.

**ARR Cycle:**
Papers must be submitted, at latest, by the ARR 2026 May cycle. Authors will need to explicitly declare which conference they intend to commit to at submission time.

**Page Limits and Format:**
The format is two-column with an 8-page limit for long papers and a 4-page limit for short papers. The mandatory Limitations section is required, placed after the conclusion.

…[truncated 507 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "WebSearch",
  "elapsed_ms": 6231
}
```

</details>

---


### Tool result

_source line 207 · 2026-05-22T12:38:39.755403+00:00_

Web search results for query: ""ARR 2026" submission guidelines author instructions page limit"

Links: [{"title":"Authors Beware: Common Submission Problems","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines","url":"http://aclrollingreview.org/authors"},{"title":"ICLR 2026 Author Guide","url":"https://iclr.cc/Conferences/2026/AuthorGuide"},{"title":"Author Guidelines for Student Research Workshop Papers -","url":"https://2026.eacl.org/calls/srw/guidelines/"},{"title":"Submissions | Transactions of the Association for Computational Linguistics","url":"https://transacl.org/index.php/tacl/about/submissions"},{"title":"IEEE ICRA 2026 | Final Paper Submission Instructions","url":"https://2026.ieee-icra.org/contribute/final-paper-submission-instructions/"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"}]

Based on the search results, here is information about ARR 2026 submission guidelines regarding page limits:

## Page Limits for ARR Submissions

Long papers may consist of up to 8 pages of content, plus unlimited pages for references and appendices.

For short papers, the search results don't specify an exact page limit, but they are mentioned as a separate category with their own requirements.

## Important Formatting Guidelines

Ethics sections will not count towards the page limit. Similarly, the paper should have a section titled "Limitations" placed according to ACL formatting guidelines, and this section can only include the discussion of limitations with strictly no new experiments, figures or analysis.

## Template and Formatting Requirements

The submi
…[truncated 453 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "WebSearch",
  "elapsed_ms": 8692
}
```

</details>

---


### Tool call

_source line 208 · 2026-05-22T12:38:45.728963+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 209 · 2026-05-22T12:38:45.980471+00:00_

/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/direction_quality.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/cosine_failure.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/probe_trap.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/related_work.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/framework.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/cosine_failure.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/probe_trap.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/introduction.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/discussion.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/abstract.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/direction_quality.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/framework.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/introduction.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/conclusion.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/abstract.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/limitations.tex
/home/ubun
…[truncated 580 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Glob",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 210 · 2026-05-22T12:38:45.980955+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "site:2026.emnlp.org call for papers main conference"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "site:2026.emnlp.org call for papers main conference"
  }
}
```

</details>

---


### Tool result

_source line 211 · 2026-05-22T12:38:52.635919+00:00_

Web search results for query: "site:2026.emnlp.org call for papers main conference"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"EMNLP 2026 Call for Papers — Official Deadlines & Important Dates | PaperPilot","url":"https://www.getpaperpilot.com/deadlines/emnlp-2026.html"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"}]

I found the EMNLP 2026 Call for Main Conference Papers. Here are the key details:

**Call Overview:**
EMNLP 2026 invites the submission of long and short papers featuring substantial, original, and unpublished research on empirical methods for Natural Language Processing.

**Important Submission Information:**
The ARR Submission Deadline is May 25, 2026. The conference will be held in Budapest, Hungary, October 24 - 29, 2026.

**Key Policy Update:**
Since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission ti
…[truncated 718 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "WebSearch",
  "elapsed_ms": 6654
}
```

</details>

---


### Tool call

_source line 212 · 2026-05-22T12:39:00.179488+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 213 · 2026-05-22T12:39:00.230086+00:00_

1	Representation engineering shows that large language models encode sycophancy as a linear direction in activation space. We extract a contrastive sycophancy direction ($\dsyc$) from style-controlled pairs, achieving cross-validated AUROC $0.827$ on Qwen3-8B and $0.779$ on Llama-3-8B. In experiments on Qwen3-8B, we test three $\dsyc$-based reward formulations with Group Relative Policy Optimization (GRPO); every formulation failed. The cosine reward could not separate valid revision from sycophantic capitulation in the narrow online activation gap. The probe reward created a stubbornness trap: the true-positive flip rate dropped to zero within 500 steps while entropy remained healthy. Removing $\dsyc$ entirely and training with a purely behavioral reward also failed: only 4 of 26 checkpoints across two seeds exceeded vanilla, while supervised fine-tuning exceeded vanilla at every evaluated checkpoint (seed 1: 16/16; seed 2: 4/4 ongoing). The root cause is a semantic gap between discriminability and reward utility: $\dsyc$ encodes \emph{whether} belief changed, not \emph{whether it should have}. A single scalar reward per completion could not convey which belief changes were warranted in our setting; dense per-token supervision (ACT) succeeded, though the methods differ along multiple dimensions beyond supervision granularity alone.
2	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 214 · 2026-05-22T12:39:00.581470+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 215 · 2026-05-22T12:39:00.832782+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Representation engineering \citep{zou2023repe} reveals that large language models encode sycophancy as a linear direction in their residual streams.
5	A contrastive sycophancy direction $\dsyc$, extracted from style-controlled pairs of valid belief revision and sycophantic capitulation, achieves cross-validated AUROC $0.827$ (5-fold CV $\sigma{=}0.028$) on Qwen3-8B and $0.779$ (5-fold CV $\sigma{=}0.019$) on Llama-3-8B, with discriminability rising monotonically across evidence-strength levels (\S\ref{sec:direction_quality}).
6	These results, replicated across two architecturally distinct model families, point to an appealing possibility: if the model's representations already separate sycophantic from non-sycophantic behavior, that separation should be convertible into a scalar reward signal for reinforcement learning.
7	Sycophancy is among the most persistent alignment failures in deployed systems \citep{sharma2023sycophancy}, and a representation-level reward could complement existing behavioral approaches by targeting the internal computation rather than its surface outputs.
8	
9	This paper shows that, in our experiments on Qwen3-8B, the conversion fails.
10	We test three formulations that translate $\dsyc$ into a GRPO \citep{shao2024grpo} training signal (cosine projection, binary probe, and continuous probe) across six configurations; every formulation fails.
11	Cosine similarity cannot separate valid revision from sycophantic capitulation in the narrow online activation gap (\S\ref{sec:cosine_failure}).
12	A binary probe with stopped gradients creates a stubbornness trap: $\tof$ drops to zero within 500 steps while generation entropy remains at 0.70, masking behavioral death (\S\ref{sec:probe_trap}).
13	Removing $\dsyc$ in favor of a purely behavioral reward does not resolve the problem: $\rthree$-only GRPO exceeds vanilla at only 4 of 26 checkpoints across two seeds, while ACT exceeds vanilla at every 
…[truncated 4618 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Read",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 216 · 2026-05-22T12:39:00.834398+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/framework.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/framework.tex"
  }
}
```

</details>

---


### Tool result

_source line 217 · 2026-05-22T12:39:00.887202+00:00_

1	\section{Experimental Framework}
2	\label{sec:framework}
3	
4	\subsection{Direction Extraction}
5	\label{ssec:extraction}
6	
7	We extract a linear sycophancy direction $\dsyc$ from the residual stream using contrastive activation pairs: a \emph{valid correction} (warranted belief revision under strong evidence) and a \emph{sycophantic capitulation} (unwarranted concession under social pressure).
8	We construct 181 contrastive pairs using GPT-4.1 in a two-stage pipeline: skeleton generation followed by 3-turn dialogue completion.
9	Style matching is enforced by automated validation (response length difference ${<}10\%$, shared opening phrase ${\geq}2$ words), with up to 3 retries per pair; 19 of 200 initial pairs were discarded for failing validation.
10	Evidence strength is annotated at three levels: \emph{weak} (75 pairs; personal memory or opinion), \emph{medium} (54 pairs; brief source citation), and \emph{strong} (52 pairs; authoritative source with detailed data).
11	From the 181 paired examples (362 activations total), we compute the mean difference at target layer $\ell$:
12	\begin{equation}
13	\label{eq:dsyc}
14	\dsyc = \frac{1}{N}\sum_{i=1}^{N}\left(\mathbf{h}^{+}_i - \mathbf{h}^{-}_i\right)
15	\end{equation}
16	where $\mathbf{h}^{+}_i$ and $\mathbf{h}^{-}_i$ are residual-stream activations for the $i$-th valid and sycophantic response.
17	The target layer is selected by 5-fold cross-validated AUROC; on Qwen3-8B this yields layer 19 with AUROC $0.827$ (5-fold CV $\sigma{=}0.028$).
18	
19	\subsection{Reward Formulations}
20	\label{ssec:reward}
21	
22	GRPO \citep{shao2024grpo} ranks sampled completions by reward and updates the policy toward higher-reward outputs.
23	We define $R = w_1 \cdot \rone + w_3 \cdot \rthree$, where $\rone$ is a direction-based component and $\rthree$ is a behavioral component (DeBERTa NLI classifier scoring consistency with the ground-truth answer).
24	Three formulations translate $\dsyc$ into $\rone$:
25	\begin{itemize}
26	\item[
…[truncated 2794 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Read",
  "elapsed_ms": 52
}
```

</details>

---


### Tool call

_source line 218 · 2026-05-22T12:39:08.396278+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/cosine_failure.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/cosine_failure.tex"
  }
}
```

</details>

---


### Tool result

_source line 219 · 2026-05-22T12:39:08.698076+00:00_

1	\section{Cosine \texorpdfstring{$\rone$}{R1}: Structural Failure}
2	\label{sec:cosine_failure}
3	
4	Section~\ref{sec:direction_quality} established that $\dsyc$ achieves AUROC 0.827 on Qwen3-8B.
5	We now test whether this discriminability translates into a viable GRPO reward.
6	Four configurations form a diagnostic chain (Table~\ref{tab:cosine_chain}): each resolves the failure mode of its predecessor but exposes a deeper limitation.
7	
8	\begin{table}[t]
9	\centering
10	\caption{Cosine $\rone$ failure chain on Qwen3-8B (LoRA rank$=$64, GRPO with $R = w_1 \cdot \rone + w_3 \cdot \rthree$).}
11	\label{tab:cosine_chain}
12	\begin{tabular}{lllll}
13	\toprule
14	Config & $\rone$ Formula & $w_1$ & Outcome & Root Cause \\
15	\midrule
16	F1a & $\tanh(\mathbf{h}\cdot\dsyc/20)$ & 0.25 & Gate saturation & Norm mismatch \\
17	F1b & $\cos(\mathbf{h},\, \dsyc)$ & 0.25 & $\rone \approx 0$ & Gap too small \\
18	F1c & +recalibration & 0.25 & Mode collapse & Reward discontinuity \\
19	F1d & $5\cos(\mathbf{h},\, \dsyc)$ & 0.40 & Mode collapse & $\rthree$ saturation \\
20	\bottomrule
21	\end{tabular}
22	\end{table}
23	
24	F1a uses a dot-product formulation ($\rone = \tanh(\mathbf{h} \cdot \dsyc / 20)$), but residual-stream norms exceed the direction norm by $100$--$1{,}200{\times}$, saturating the tanh gate and zeroing the gradient by step 955.
25	Switching to cosine similarity (F1b) eliminates norm dependence, yet the cosine gap between valid and sycophantic activations averages only 0.098 across layers---too narrow to generate meaningful reward contrast.
26	Online recalibration (F1c, \S\ref{ssec:recalib}) raises offline AUROC from 0.827 to 0.910 but paradoxically triggers mode collapse: the abrupt shift in $\dsyc$ at each recalibration event creates a reward discontinuity that destabilizes GRPO advantage estimates, collapsing entropy to 0.069 within 300 steps.
27	Amplifying the signal with $5{\times}$ scaling (F1d) lifts $\rone$ above the noise floor but simultaneously amplifies t
…[truncated 836 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 220 · 2026-05-22T12:39:08.698445+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/probe_trap.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/probe_trap.tex"
  }
}
```

</details>

---


### Tool result

_source line 221 · 2026-05-22T12:39:09.140890+00:00_

1	\section{The Probe Reward Trap}
2	\label{sec:probe_trap}
3	
4	The cosine formulations fail because the continuous projection of $\dsyc$ produces a gap too narrow for reward contrast.
5	A natural remedy is to discretize: train a logistic probe on $\dsyc$ and threshold its output, yielding $\rone = \mathbb{I}[P(\text{syc} \mid \mathbf{h}) < 0.5]$ (F2 in \S\ref{ssec:reward}).
6	We show that this discretization sidesteps the magnitude problem but creates a qualitatively worse failure.
7	
8	\paragraph{Differentiable probe: gradient gaming.}
9	Without stop-gradient (exp-008), the policy discovers within ${\sim}30$ steps that shifting activations away from the sycophancy cluster maximizes $\rone$ regardless of response content, producing an inverted profile ($\tof = 0.978$, $\nof = 0.006$).
10	This motivates the frozen-probe design below.
11	
12	\paragraph{Binary probe: the stubbornness trap.}
13	With stop-gradient (exp-008v3), the policy cannot game the boundary but instead exploits a deeper flaw: $\dsyc$ does not condition on input validity, so refusing to revise a wrong answer receives the same $\rone = 1$ as correctly resisting invalid pressure.
14	By step 500, $\tof$ drops to 0.000 and $\nof$ reaches 0.995, yielding $\sycon = 0$.
15	Qualitative analysis reveals distinct failure modes: \emph{sycophantic stubbornness} (24\%), where the model verbally agrees but does not change its answer; \emph{deliberation traps} (29\%), where the model identifies the correct answer but cannot commit; and evidence-graded hedging, where the model adjusts its refusal style rather than its acceptance rate (Appendix~\ref{app:taxonomy}).
16	
17	\paragraph{Behavioral death precedes distributional collapse.}
18	
19	\begin{table}[t]
20	\centering
21	\caption{Probe reward trap trajectory (exp-008v3). Behavioral death ($\tof{=}0$) occurs at step 500; entropy remains healthy until step ${\sim}1840$. Reward averages $+0.72$ throughout.}
22	\label{tab:probe_trajectory}
23	\begin{tabular}{lccccc}

…[truncated 2145 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Read",
  "elapsed_ms": 442
}
```

</details>

---


### Tool call

_source line 222 · 2026-05-22T12:39:09.141425+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 223 · 2026-05-22T12:39:09.242285+00:00_

1	\section{Analysis: Discriminability $\neq$ Reward Utility}\label{sec:discussion}
2	
3	\paragraph{Unified root cause.}
4	The failures in Sections~\ref{sec:cosine_failure} and~\ref{sec:probe_trap} trace to a single geometric limitation.
5	$\dsyc$ encodes the \emph{direction} of belief change but not its \emph{evidential warrant}: valid revision and sycophantic capitulation both shift activations toward the user's position along the same direction.
6	The two reward families expose complementary faces of this blindness.
7	Cosine $\rone$ penalizes all belief change indiscriminately; the resulting mode collapse (F1c, F1d) reflects excessive punishment of any activation shift along $\dsyc$.
8	The binary probe $\rone$ rewards all resistance regardless of input validity; the stubbornness trap ($\tof = 0$ by step 500) reflects excessive permissiveness toward activation stasis.
9	These are not independent design flaws but dual consequences of a direction that conflates the target behavior (resisting invalid challenges) with its complement (refusing valid corrections).
10	Cross-model evidence confirms the limitation extends beyond Qwen3-8B: Llama-3-8B independently achieves AUROC $0.779$ (5-fold CV $\sigma{=}0.019$) on the same contrastive pairs with the same monotonic evidence gradient, so discriminability generalizes across architectures while the semantic gap between discriminability and reward utility persists.
11	This pattern contrasts with reasoning faithfulness and safety directions~\citep{zhang2026latentgrpo}, where the behavior to suppress is geometrically distinct from the behavior to preserve along the relevant direction.
12	\citet{wu2026rewardhacking} reinforce this principle: concept directions applied via advantage modification in GRPO achieve 100\% validation accuracy for reward hacking detection, where shortcut behaviors are geometrically separable---confirming that direction utility depends on geometric separability, not the optimization framework.
13	For syc
…[truncated 7081 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 224 · 2026-05-22T12:39:15.616616+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/direction_quality.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/direction_quality.tex"
  }
}
```

</details>

---


### Tool result

_source line 225 · 2026-05-22T12:39:15.868089+00:00_

1	\section{Direction Discriminability}
2	\label{sec:direction_quality}
3	
4	Before evaluating $\dsyc$ as a reward signal (\S\ref{sec:cosine_failure}--\S\ref{sec:probe_trap}), we first establish that it captures a genuine sycophancy-related signal in the residual stream.
5	If the direction failed to discriminate sycophantic from non-sycophantic activations, downstream reward failures would be trivially explained by poor direction quality rather than by a fundamental gap between discriminability and reward utility.
6	We evaluate discriminability along five axes: cross-validated classification accuracy, evidence-strength stratification, cross-model transfer, training stability, and probe ablation.
7	Figure~\ref{fig:direction_quality} summarizes the per-layer AUROC profiles for both models.
8	
9	\paragraph{Qwen3-8B layer-wise discriminability.}
10	We evaluate $\dsyc$ via 5-fold cross-validated AUROC on 181 style-controlled contrastive pairs (\S\ref{ssec:extraction}).
11	The direction achieves AUROC $0.827$ (5-fold CV $\sigma{=}0.028$) at its best layer (L19).
12	Discriminability emerges gradually across depth: layers L0--L8 perform near chance, statistical significance ($p < 0.01$) first appears at L16, and performance peaks at L19.
13	This gradual emergence, with the peak in the upper third of the network, suggests that sycophancy-relevant information is encoded as a late-stage representation rather than an input-level confound.
14	The direction also captures evidential granularity.
15	AUROC rises monotonically from 0.675 on weak-evidence pairs to 0.883 on medium and 0.929 on strong pairs.
16	This gradient indicates that $\dsyc$ encodes the degree of evidential warrant, not merely a binary sycophancy label.
17	
18	\paragraph{Cross-model generalization.}
19	To rule out that these results are specific to Qwen3-8B's representation geometry, we repeat the full extraction and evaluation pipeline on Llama-3-8B-Instruct.
20	Table~\ref{tab:cross_model} compares the two models.
…[truncated 3493 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Read",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 226 · 2026-05-22T12:39:15.868447+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 227 · 2026-05-22T12:39:16.069525+00:00_

1	\section{Related Work}\label{sec:related_work}
2	
3	\paragraph{Representation Engineering.}
4	Linear directions in LLM residual streams encode behavioral concepts \citep{zou2023repe}; inference-time methods---ITI \citep{li2023iti}, ActAdd \citep{turner2023actadd}, CAA \citep{rimsky2024caa}---demonstrate that activation geometry suffices for behavioral control \citep{burns2023ccs}.
5	We use the same contrastive extraction as CAA but apply $\dsyc$ as an RL reward, revealing a gap that inference-time work does not encounter.
6	
7	\paragraph{Reward Design and Overoptimization.}
8	Proxy rewards diverge from true objectives under sustained optimization \citep{gao2023scaling}, and reward hacking can escalate to active tampering \citep{denison2024subterfuge}.
9	Our probe trap (\S\ref{sec:probe_trap}) is an extreme instance: the reward actively reinforces degenerate behavior rather than merely being circumvented \citep{skalse2022hacking}.
10	\citet{wu2026rewardhacking} demonstrate that representation-level directions succeed for reward hacking suppression when behaviors are geometrically separable (\S\ref{sec:discussion}).
11	
12	\paragraph{Sycophancy Characterization and Mitigation.}
13	Sycophancy is pervasive in RLHF-trained assistants \citep{sharma2023sycophancy}, amplified by RLHF \citep{shapira2026amplifies}, and traceable to late-layer preference shifts \citep{wang2025internal}; mitigation approaches include synthetic data \citep{wei2024synthetic}, consistency training \citep{consistency2025bctact}, and neuron-level correction \citep{obrien2025fewbadneurons}.
14	Our analysis shows why the step from diagnosis to reward is structurally blocked: $\dsyc$ conflates warranted revision with unwarranted capitulation.
15	
16	\paragraph{Probe-Based Inference-Time Mitigation.}
17	\citet{papadatos2024probepenalties} reduce sycophancy via Best-of-N reranking with linear probe penalties (94\% probe accuracy), where the probe selects among candidates without producing gradients tha
…[truncated 1208 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Read",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 228 · 2026-05-22T12:39:16.070089+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 229 · 2026-05-22T12:39:16.170758+00:00_

1	\section{Conclusion}\label{sec:conclusion}
2	
3	This work tested whether a representation direction that detects sycophantic behavior can serve as a scalar reward signal for sycophancy calibration via GRPO.
4	In experiments on Qwen3-8B, $\dsyc$ achieved strong offline discriminability (AUROC 0.827), yet all three reward formulations failed---the probe reward produced a stubbornness trap ($\tof = 0$ by step 500), and $\rthree$-only GRPO exceeded vanilla at only 4 of 26 checkpoints.
5	$\dsyc$ encodes \emph{whether} belief changed, not \emph{whether it should have}; ACT's dense per-token supervision achieved $\sycon = 0.301$, suggesting supervision granularity as one plausible factor, though ACT and GRPO differ along multiple dimensions that remain to be disentangled.
6	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 230 · 2026-05-22T12:39:16.221432+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 231 · 2026-05-22T12:39:16.272136+00:00_

1	Our RL training experiments use Qwen3-8B exclusively with GRPO; cross-model discriminability is confirmed on Llama-3-8B (AUROC $0.779$; Table~\ref{tab:cross_model}), but compute constraints (${\sim}200$ H100-equivalent hours) prevented replication of the reward formulation failures on a second architecture. Other RL algorithms (PPO, DPO) may interact differently with representation-based rewards.
2	
3	Evidence strength for the 181 contrastive pairs was annotated by GPT-4.1 as a single annotator; we did not collect human inter-annotator agreement. The evaluation framework categorizes challenges as binary valid/invalid rather than a continuous spectrum, and flip determination relies on a DeBERTa NLI classifier rather than human judges.
4	
5	We report GRPO results from two random seeds; ACT seed 2 verification is ongoing (4 of 16 checkpoints evaluated at submission, all exceeding vanilla). Both GRPO seeds exhibit qualitatively consistent oscillation patterns (similar amplitude, identical crash depth), but the limited seed count constrains statistical claims about training dynamics. ACT and GRPO differ along multiple dimensions beyond supervision granularity, so we cannot isolate the causal factor behind ACT's advantage.
6	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 232 · 2026-05-22T12:39:24.885962+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 233 · 2026-05-22T12:39:25.338135+00:00_

1	\section{Training Details}
2	\label{app:training}
3	
4	\paragraph{Reward weight selection.}
5	The weight $w_1$ is set by diagnostic-driven iteration: $w_1{=}0.25$ was initially chosen to down-weight the noisy cosine reward term; this was later increased to $w_1{=}0.40$ for F1d after diagnostics revealed that $w_1{=}0.25$ allowed the cosine term to contribute only ${\sim}8.3\%$ of total reward variance.
6	The empirical scaling factor in F1a ($\dsyc/20$) is a heuristic normalization; we did not find it critical to the failure modes reported.
7	
8	\paragraph{Response truncation.}
9	All GRPO experiments use \texttt{max\_completion\_length}=256, resulting in 80--84\% truncation of multi-turn responses.
10	This setting is shared across all conditions and does not affect relative comparisons; we retain it because response-level decisions typically manifest within the first 100--200 tokens.
11	
12	\paragraph{Hyperparameters.}
13	Table~\ref{tab:hyperparams} compares training configurations for GRPO variants and ACT.
14	
15	\begin{table}[h]
16	\centering
17	\small
18	\caption{Training hyperparameters. All experiments use Qwen3-8B, DeepSpeed ZeRO-2, bf16 precision.}
19	\label{tab:hyperparams}
20	\begin{tabular}{lcc}
21	\toprule
22	& GRPO & ACT \\
23	\midrule
24	Learning rate & 5e-5 & 5e-5 \\
25	Effective batch & 16 & 16 \\
26	Max steps & 8{,}000 & 8{,}000 \\
27	Warmup steps & 200 & 200 \\
28	LR schedule & linear$^a$ & linear \\
29	Grad.\ clipping & --- & 1.0 \\
30	\midrule
31	LoRA rank & 64 & 64 \\
32	LoRA $\alpha$ & 64 & 128 \\
33	LoRA modules & 4$^b$ & 7$^c$ \\
34	LoRA dropout & 0 & 0.05 \\
35	\midrule
36	Group size & 2$^d$ & --- \\
37	KL $\beta$ & 0.04 & --- \\
38	Max compl.\ len. & 256 & --- \\
39	Max seq.\ len. & --- & 1{,}024 \\
40	L2 loss weight & --- & 0.1 \\
41	\bottomrule
42	\end{tabular}
43	\\[2pt]
44	\raggedright\footnotesize
45	$^a$Cosine schedule for $\rthree$-only.
46	$^b$q/k/v/o\_proj.
47	$^c$+ gate/up/down\_proj (${\sim}1.75{\times}$ params; \S\ref{sec:discu
…[truncated 1493 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 234 · 2026-05-22T12:39:25.338531+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 235 · 2026-05-22T12:39:25.389577+00:00_

1	issues:
2	  # === ROUND 1 ISSUES (UPDATED FOR ROUND 2+3) ===
3	
4	  - id: R1-N1
5	    summary: "Fisher exact test 将非独立 checkpoints 当独立样本，p<0.0001 不可信"
6	    category: method
7	    severity: critical
8	    status: resolved
9	    first_raised_round: 1
10	    last_seen_round: 1
11	    mentions:
12	      - round: 1
13	        reviewers: [1, 2]
14	        note: "R1 首提，R2 完全同意。定性结论从轨迹图可直接观察，p 值赋予虚假统计权威性。"
15	      - round: 2
16	        reviewers: []
17	        note: "本轮未提及。论文已移除 Fisher p 值，改为描述性统计。已修复。"
18	    action_items:
19	      - round: 1
20	        action: "移除所有 Fisher p 值，改为 run-level 描述性统计"
21	        assigned_to: paper_agent
22	        status: done
23	    resolution: "Wave 1 已移除所有 Fisher p 值，改用描述性统计。Round 2 未再提及。"
24	    resolution_round: 2
25	
26	  - id: R2-N1
27	    summary: "遗漏 Papadatos & Freedman (2024) probe penalty 成功案例，直接挑战核心 thesis"
28	    category: framing
29	    severity: critical
30	    status: resolved
31	    first_raised_round: 1
32	    last_seen_round: 2
33	    mentions:
34	      - round: 1
35	        reviewers: [1, 2]
36	        note: "R2 首提，R1 交叉同意。论文必须讨论 probe penalty (RM 内部) vs probe reward (GRPO scalar) 的关键差异。"
37	      - round: 2
38	        reviewers: [2]
39	        note: "R2 将 Papadatos & Freedman 对比定位列为论文优势 (S6)：§6 的 inference-time vs training-time × dense vs sparse 双维度分析框架清晰。已充分讨论。"
40	    action_items:
41	      - round: 1
42	        action: "Agent WebSearch 读 Papadatos & Freedman (2024) 确认方法细节，Paper Agent 在 §7 新增专段 + §6 补讨论"
43	        assigned_to: agent+paper_agent
44	        status: done
45	    resolution: "§6 和 §7 均已充分讨论 Papadatos & Freedman，R2 round 2 列为论文优势。"
46	    resolution_round: 2
47	
48	  - id: R2-N2
49	    summary: "references.bib 多条引用严重不完整：ACT 作者为 Unknown，6 条仅 et al."
50	    category: format
51	    severity: critical
52	    status: resolved
53	    first_raised_round: 1
54	    last_seen_round: 1
55	    mentions:
56	      - round: 1
57	        reviewers: [1, 2]
58	        note: "ACT 是唯一成功 baseline，Unknown 作者使读者无法验证方法来源。可能触发 A
…[truncated 14822 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 236 · 2026-05-22T12:39:41.112753+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:read_local_file",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:read_local_file",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 237 · 2026-05-22T12:39:41.163459+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 238 · 2026-05-22T12:39:45.782814+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "contrastive_entrain_calib",
  "file": "config.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "contrastive_entrain_calib",
    "file": "config.yaml"
  }
}
```

</details>

---


### Tool result

_source line 239 · 2026-05-22T12:39:45.833539+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'mistakes.yaml', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'config.yaml'\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 240 · 2026-05-22T12:39:51.929762+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/contrastive_entrain_calib/**/config*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/contrastive_entrain_calib/**/config*.yaml",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3"
  }
}
```

</details>

---


### Tool result

_source line 241 · 2026-05-22T12:39:52.130718+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Glob",
  "elapsed_ms": 200
}
```

</details>

---


### Tool call

_source line 242 · 2026-05-22T12:39:55.800633+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/contrastive_entrain_calib/*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/contrastive_entrain_calib/*.yaml",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects"
  }
}
```

</details>

---


### Tool result

_source line 243 · 2026-05-22T12:39:55.851622+00:00_

/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/experiment_plan.yaml
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/dream_registry.yaml
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/literature_map.yaml
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/writing_plan.yaml
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/paper_provenance.yaml
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/decisions.yaml
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/mistakes.yaml
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/registry.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 244 · 2026-05-22T12:40:15.214308+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "contrastive_entrain_calib",
  "review_chat_id": "oc_056796cf71f839be40019e5f1a11791b"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "contrastive_entrain_calib",
    "review_chat_id": "oc_056796cf71f839be40019e5f1a11791b"
  }
}
```

</details>

---


### Tool result

_source line 245 · 2026-05-22T12:40:29.905309+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 14690
}
```

</details>

---


### Tool call

_source line 246 · 2026-05-22T12:40:29.956113+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "project": "contrastive_entrain_calib",
  "reviewer_id": "1",
  "round_number": "1",
  "text": "你负责审查 **方法严谨性 + 实验有效性**。\n\n## Venue 信息\n- **EMNLP 2026**（通过 ARR 统一审稿）\n- ARR submission deadline: 2026-05-25\n- 正文 8 页限制 + 无限参考文献/附录\n- ACL 模板，double-blind（匿名）\n- Limitations 章节必须有，不计入页数\n\n## 论文文件\n- LaTeX 主文件: `projects/contrastive_entrain_calib/docs/paper/main.tex`\n- sections 目录: `projects/contrastive_entrain_calib/docs/paper/sections/`\n- PDF: `/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_3/submitted.pdf`\n\n## 你的审查侧重\n\n1. **Reward 设计合理性**：4 个 cosine 变体 + binary/continuous probe 的实验设计是否覆盖了合理的设计空间？是否有明显遗漏的 formulation？\n2. **统计声明有效性**：AUROC 的 5-fold CV 是否充分？cross-seed 分析（仅 2 seeds）的可靠性？\"4/26 checkpoints exceed vanilla\" 这类 claim 的统计支撑？\n3. **Confound 控制**：ACT vs GRPO 对比存在多维度差异（supervision granularity, loss family, LoRA capacity 等）——论文是否充分承认了这些 confounds？是否存在 overclaiming？\n4. **超参数覆盖**：$w_1$ 仅测试 0.25/0.40；GRPO group size = 2（远低于标准 8-16）；max_completion_length=256 导致 80-84% truncation——这些选择是否影响结论有效性？\n5. **可复现性**：训练超参数披露完整性、代码/数据可用性声明、contrastive pairs 构建细节\n\n请严格评估，按 EMNLP 2026 标准给出 Strengths/Weaknesses/Questions/Overall Assessment。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "project": "contrastive_entrain_calib",
    "reviewer_id": "1",
    "round_number": "1",
    "text": "你负责审查 **方法严谨性 + 实验有效性**。\n\n## Venue 信息\n- **EMNLP 2026**（通过 ARR 统一审稿）\n- ARR submission deadline: 2026-05-25\n- 正文 8 页限制 + 无限参考文献/附录\n- ACL 模板，double-blind（匿名）\n- Limitations 章节必须有，不计入页数\n\n## 论文文件\n- LaTeX 主文件: `projects/contrastive_entrain_calib/docs/paper/main.tex`\n- sections 目录: `projects/contrastive_entrain_calib/docs/paper/sections/`\n- PDF: `/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_3/submitted.pdf`\n\n## 你的审查侧重\n\n1. **Reward 设计合理性**：4 个 cosine 变体 + binary/continuous probe 的实验设计是否覆盖了合理的设计空间？是否有明显遗漏的 formulation？\n2. **统计声明有效性**：AUROC 的 5-fold CV 是否充分？cross-seed 分析（仅 2 seeds）的可靠性？\"4/26 checkpoints exceed vanilla\" 这类 claim 的统计支撑？\n3. **Confound 控制**：ACT vs GRPO 对比存在多维度差异（supervision granularity, loss family, LoRA capacity 等）——论文是否充分承认了这些 confounds？是否存在 overclaiming？\n4. **超参数覆盖**：$w_1$ 仅测试 0.25/0.40；GRPO group size = 2（远低于标准 8-16）；max_completion_length=256 导致 80-84% truncation——这些选择是否影响结论有效性？\n5. **可复现性**：训练超参数披露完整性、代码/数据可用性声明、contrastive pairs 构建细节\n\n请严格评估，按 EMNLP 2026 标准给出 Strengths/Weaknesses/Questions/Overall Assessment。"
  }
}
```

</details>

---


### Tool result

_source line 247 · 2026-05-22T12:40:43.083004+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 13126
}
```

</details>

---


### Tool call

_source line 248 · 2026-05-22T12:40:43.436596+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "project": "contrastive_entrain_calib",
  "reviewer_id": "2",
  "round_number": "1",
  "text": "你负责审查 **新颖性 + Framing 完整性**。\n\n## Venue 信息\n- **EMNLP 2026**（通过 ARR 统一审稿）\n- ARR submission deadline: 2026-05-25\n- 正文 8 页限制 + 无限参考文献/附录\n- ACL 模板，double-blind（匿名）\n- Limitations 章节必须有，不计入页数\n\n## 论文文件\n- LaTeX 主文件: `projects/contrastive_entrain_calib/docs/paper/main.tex`\n- sections 目录: `projects/contrastive_entrain_calib/docs/paper/sections/`\n- PDF: `/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_3/submitted.pdf`\n\n## 你的审查侧重\n\n1. **Contribution 定位**：三个 contributions (C1-C3) 的新颖性和重要性。\"negative result paper\" 对 EMNLP 的价值——是否提供了足够的 insight 超越\"我们试了但失败了\"？\n2. **Claim scope vs 证据**：\n   - 标题声称 \"Sycophancy Directions Fail as Scalar RL Rewards\"——但仅测试了 GRPO，未测试 PPO/DPO/RLOO\n   - C3 声称 \"sparse RL reward failed to convey the valid/invalid distinction\"——但 ACT vs GRPO 有多维度 confound\n   - 论文是否在这些 claims 上 overclaiming？\n3. **Related Work 覆盖**：\n   - Papadatos & Freedman (2024) probe penalties 的讨论是否充分？\n   - SMART (Beigi et al., 2025) per-step process rewards 讨论是否充分？\n   - Wu & Tang (2026) \"When Reward Hacking Rebounds\" 用 representation directions 在 GRPO 中成功——是否有讨论？\n   - 其他遗漏的重要相关工作？\n4. **叙事结构**：Introduction 的逻辑链是否清晰？从 direction discriminability → reward failure → root cause analysis 的故事是否连贯？Abstract 长度/密度是否合适？\n5. **Broader impact / generalizability**：论文声称的 \"discriminability ≠ reward utility\" 原则是否有足够的泛化性？是否仅对 sycophancy 成立？\n\n请严格评估，按 EMNLP 2026 标准给出 Strengths/Weaknesses/Questions/Overall Assessment。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "project": "contrastive_entrain_calib",
    "reviewer_id": "2",
    "round_number": "1",
    "text": "你负责审查 **新颖性 + Framing 完整性**。\n\n## Venue 信息\n- **EMNLP 2026**（通过 ARR 统一审稿）\n- ARR submission deadline: 2026-05-25\n- 正文 8 页限制 + 无限参考文献/附录\n- ACL 模板，double-blind（匿名）\n- Limitations 章节必须有，不计入页数\n\n## 论文文件\n- LaTeX 主文件: `projects/contrastive_entrain_calib/docs/paper/main.tex`\n- sections 目录: `projects/contrastive_entrain_calib/docs/paper/sections/`\n- PDF: `/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_3/submitted.pdf`\n\n## 你的审查侧重\n\n1. **Contribution 定位**：三个 contributions (C1-C3) 的新颖性和重要性。\"negative result paper\" 对 EMNLP 的价值——是否提供了足够的 insight 超越\"我们试了但失败了\"？\n2. **Claim scope vs 证据**：\n   - 标题声称 \"Sycophancy Directions Fail as Scalar RL Rewards\"——但仅测试了 GRPO，未测试 PPO/DPO/RLOO\n   - C3 声称 \"sparse RL reward failed to convey the valid/invalid distinction\"——但 ACT vs GRPO 有多维度 confound\n   - 论文是否在这些 claims 上 overclaiming？\n3. **Related Work 覆盖**：\n   - Papadatos & Freedman (2024) probe penalties 的讨论是否充分？\n   - SMART (Beigi et al., 2025) per-step process rewards 讨论是否充分？\n   - Wu & Tang (2026) \"When Reward Hacking Rebounds\" 用 representation directions 在 GRPO 中成功——是否有讨论？\n   - 其他遗漏的重要相关工作？\n4. **叙事结构**：Introduction 的逻辑链是否清晰？从 direction discriminability → reward failure → root cause analysis 的故事是否连贯？Abstract 长度/密度是否合适？\n5. **Broader impact / generalizability**：论文声称的 \"discriminability ≠ reward utility\" 原则是否有足够的泛化性？是否仅对 sycophancy 成立？\n\n请严格评估，按 EMNLP 2026 标准给出 Strengths/Weaknesses/Questions/Overall Assessment。"
  }
}
```

</details>

---


### Tool result

_source line 249 · 2026-05-22T12:40:44.965213+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1528
}
```

</details>

---


### Tool call

_source line 250 · 2026-05-22T12:40:55.379029+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "contrastive_entrain_calib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "contrastive_entrain_calib"
  }
}
```

</details>

---


### Tool result

_source line 251 · 2026-05-22T12:40:55.479963+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 100
}
```

</details>

---


### Assistant

_source line 252 · 2026-05-22T12:41:05.517224+00:00_

Round 1 已启动：

| 角色 | 侧重 | 状态 |
|------|------|------|
| Reviewer 1 | 方法严谨性 + 实验有效性 | ⏳ 审稿中 |
| Reviewer 2 | 新颖性 + framing 完整性 | ⏳ 审稿中 |
| Visual Check | PDF 排版审查（非评分项） | ⏳ 进行中 |
| External Review | 未启用 | — |

等待 Reviewer 返回初审意见。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director"
}
```

</details>

---


## Round 18

## Round 18

2 recorded events


### User

_source line 253 · 2026-05-22T12:46:05.921243+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 审稿意见：方法严谨性 + 实验有效性

## 总体评分
**Overall**: 2.5 (Borderline Findings)
**一句话总结**: 论文提出了重要的概念框架（discriminability ≠ reward utility），但核心负面结论受到多个未控制的实验混淆因素严重削弱——GRPO group_size=2、80-84% 截断、仅 2 seeds、极窄超参数搜索——无法排除 GRPO 优化本身不足导致失败的替代解释。

## 官方维度打分（ACL ARR review form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 2.5/5 | 核心负面声明有多个严重混淆因素未控制；无法区分"reward 信号本质缺陷"和"GRPO 优化配置不足" |
| Excitement | 3/5 | 问题重要且及时，失败分类学有价值，但负面结果在实验不充分条件下影响力有限 |
| Confidence | 4/5 | 熟悉 RL alignment、representation engineering 和 sycophancy 文献 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] GRPO group_size=2 严重偏离标准实践，可能是失败的主因而非 d_syc 本身

- 具体位置：Table 5 (Appendix A, p.10)
- 问题：标准 GRPO（如 DeepSeek-R1, Shao et al. 2024）使用 group_size 8-64。group_size=2 退化为噪声极高的 pairwise 对比，对含噪 cosine reward 会极度放大梯度估计方差。论文未给出任何理由也未测试更大值。
- 为什么影响接收：核心声明 "every d_syc-based GRPO formulation fails"（Abstract, §1），但如果 GRPO 优化器因 group_size 不足而无法利用任何微弱信号，失败就不能归因于 d_syc。这是致命的替代解释。
- 建议：至少测试 group_size ∈ {8, 16}，或提供消融实验。

**N2** [critical] max_completion_length=256 导致 80-84% 截断，严重损害 reward 信号有效性

- 具体位置：Appendix A (p.10)
- 问题：sycophancy calibration 的核心行为（belief revision/capitulation）常在多轮对话后半段发生。80-84% 截断意味着 reward 在不完整输出上计算。论文辩护"response-level decisions manifest within first 100-200 tokens"是未验证的经验声明。§5 的 probe reward trap（ToF=0 at step 500）可能正因截断而非 probe 缺陷导致。
- 为什么影响接收：提供了另一个强替代解释。"shared across conditions" 只保证公式间相对比较有效，不支持"d_syc-based rewards 本质失败"的绝对声明。
- 建议：至少在一个公式上测试 max_completion_length=512/1024。

**N3** [critical] 仅 2 random seeds 不足以支撑负面结论

- 具体位置：§9/Reproducibility (p.8-9)
- 问题：RL 训练高方差众所周知。2 seeds 无法提供有意义方差估计。"4/26 checkpoints exceed vanilla"（Table 4 footnote）的可靠性完全依赖 2 seeds 的代表性。负面结论证据标准应高于正面结论。
- 建议：增加到 3-5 seeds 并报告 mean ± std。

**N4** [critical] Reward 设计空间探索不足，声明过度推广

- 具体位置：§2.2 (p.3), §4 (p.4-5), Table 2, Appendix A
- 问题：6 个 formulation 均为简单标量变换/单层 probe。遗漏：(1) learned reward（MLP on d_syc features）；(2) 多层聚合（仅用 best layer L19，Figure 1 显示其他层也有信号）；(3) 非线性变换。w₁ 仅测试 0.25/0.40 两个值——在 w₁=0.25 时 d_syc 仅贡献 ~8.3% reward 方差，信号被淹没，但未尝试更高 w₁。
- 为什么影响接收：负面结论强度受限于设计空间覆盖。"every formulation fails" 声明 overclaiming。
- 建议：(1) 至少加一个 learned reward 变体；(2) 测试 w₁ 更宽范围 {0.1, 0.25, 0.4, 0.6, 0.8}；(3) 将声明限定为 "tested formulations"。

---

## Should-Fix 问题

**W1** [warning] ACT vs GRPO 对比 confounds 大量，叙事过度依赖此对比

- 具体位置：§6-7 (p.6-7), Table 4
- 问题：§7 承认 confounds（per-token vs per-completion、L2 vs policy gradient、labeled pairs vs self-discovery、direct layer manipulation vs output-level、SFT stability vs RL variance），但叙事结构仍大量用 ACT 成功反衬 GRPO 失败。SYCONSCORE 对比（ACT 0.301 vs GRPO best ~0.143）在不控制 confounds 时无法得出 reward formulation 的因果结论。
- 建议：降低 ACT 对比叙事权重，或设计更 controlled 对比。

**W2** [warning] SYCONSCORE 指标有效性未充分建立

- 具体位置：§2.5 (p.3), Equation 2
- 问题：SYCONSCORE 似为本文新指标（ToF/NoF 调和平均），未与已有 sycophancy benchmark 对比验证，未讨论调和平均选择理由，未验证与人类判断相关性。
- 建议：解释指标选择理由，或与已有 benchmark 做相关性分析。

**W3** [warning] 181 contrastive pairs 质量控制不足

- 具体位置：§2 (p.2)
- 问题：GPT-4.1 生成，仅 automated validation + 3 retries。无人工验证/inter-annotator agreement。19/200 对被丢弃（~10%）但未分析被丢弃对特征。
- 建议：增加小规模人工验证。

**W4** [warning] Figure 3 cross-seed 分析与文字描述存在 tension

- 具体位置：§7 (p.7), Figure 3
- 问题：2 seeds 的 SYCONSCORE 轨迹差异显著。"4/26 checkpoints exceed vanilla" 可能是 seed-dependent 而非 systematic failure。未量化 per-seed 成功 checkpoint 分布。

---

## 小问题

- §1: "entropy remained healthy" 含糊，建议给具体数值。
- Table 2: "gate saturation" 缺操作性定义（何种阈值算 saturated）。
- §8 Related Work 与核心贡献连接不紧密。
- Appendix B: Stubbornness taxonomy 仅 100 条样本，无 inter-rater reliability。
- Equation 1: "residual-stream activations" 提取位置（layer output vs attention vs MLP）可更明确。

---

## 主要优势

- 问题重要且及时——sycophancy 是 LLM alignment 核心挑战。
- 失败诊断链（gate saturation → gradient vanishing → mode collapse → behavioral death → probe reward trap）对 practitioners 有参考价值。
- d_syc 方向本身验证扎实：5-fold CV AUROC 0.827/0.779，cross-model 一致性，evidence-strength 梯度效应。
- "Discriminability ≠ utility" 概念框架清晰，有潜力影响更广泛的 reward design。
- 诚实的 limitations 声明。

---

**总结**：这是一篇提出了有价值概念框架的论文，但作为负面结果论文（negative result paper），其证据标准不足。核心声明"d_syc-based rewards fundamentally fail"需要在排除 GRPO 优化不足（group_size=2, 80-84% truncation, 2 seeds, narrow w₁ search）这一强替代解释后才能成立。建议补充实验后重新投稿。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 254 · 2026-05-22T12:46:38.115193+00:00_

收到 Reviewer 1 的意见，等待 Reviewer 2 返回后进行交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director"
}
```

</details>

---


## Round 19

## Round 19

6 recorded events


### User

_source line 255 · 2026-05-22T12:46:39.159182+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

**评分摘要**：Overall 2.5 (Borderline Findings)，Soundness 2.5/5，Excitement 3/5。

**核心问题**：4 个 critical issues——(1) GRPO group_size=2 严重偏离标准实践；(2) 80-84% response 截断损害 reward 有效性；(3) 仅 2 seeds 不足以支撑负面结论；(4) reward 设计空间探索过窄，声明过度推广。这些混淆因素使得无法区分"d_syc 本质不可用"和"GRPO 优化配置不足"两种解释。

---

[Reviewer 2 审稿意见]:

## 总体评分
**Overall**: 3.0（Findings）
**一句话总结**: 论文发现了一个真实且有价值的 insight（discriminability ≠ reward utility），probe reward trap 是新颖的实证发现，但 claims 范围显著超出实验证据（仅测试 GRPO），title overclaiming 和 C3 的 confound 问题需要修正后才能达到 Findings 水准。

## 官方维度打分（来自 ACL ARR review form）
| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3/5 | Main claims（GRPO 失败）有充分支持，但 title 和 C3 的泛化性声明超出证据范围 |
| Excitement | 2.5/5 | Negative result 有用但范围有限；insight 有趣但泛化性证据不足 |
| Overall Assessment | 3/5 | Borderline Findings——insight 真实，但需收窄 claims 或扩展实验 |
| Reproducibility | 4/5 | 提供了训练超参、评估 metric 定义、承诺开源代码和数据 |
| Confidence | 4/5 | 对 RL for alignment 和 representation engineering 领域较熟悉 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] Title 和 claims 范围显著超出实验证据

- 具体位置：Title, Abstract, Section 1 (C1/C3)
- 问题：标题声称 "Sycophancy Directions Fail as **Scalar RL Rewards**"，但论文仅测试了 GRPO 一种 RL 算法。PPO、RLOO、REINFORCE 等 on-policy 算法未测试，DPO 等 offline 算法也未测试。标题中 "Scalar RL Rewards" 暗示了对所有 RL 算法的泛化结论，但证据只覆盖 GRPO。同样，C1 声称 "Every tested GRPO formulation fails" 是准确的，但 C3 声称 "sparse RL reward failed to convey the valid/invalid distinction" 将失败归因于 reward signal 本身（而非 GRPO 的 specific optimization dynamics），这个归因未被实验证实。
- 为什么影响接收：Overclaiming 是 ARR soundness 评分的核心扣分项。论文的核心论点——failure 源于 reward signal 的 scalar nature 而非特定算法——是一个需要跨算法验证的因果声明，而非从单一算法可以推出的结论。
- 建议修改方向：(a) 将标题改为 "Why Sycophancy Directions Fail as GRPO Rewards" 或 "…as Scalar Per-Completion Rewards: Evidence from GRPO"；(b) 至少补充一个 PPO 或 REINFORCE 实验来支持 "scalar RL reward" 的泛化声明；(c) 如不增加实验，C3 需改为更保守的表述，明确标注为 hypothesis 而非 finding。

**N2** [critical] C3 的 ACT vs GRPO 对比存在严重 confound，但被表述为 contribution

- 具体位置：Section 1 (C3), Section 6 (Analysis)
- 问题：C3 声称 "sparse RL reward failed to convey the valid/invalid distinction"，其核心证据来自 ACT 成功而 GRPO 失败的对比。然而 ACT 与 GRPO 至少在以下维度上不同：(1) 训练范式（SFT vs RL）；(2) 监督粒度（per-token vs per-completion）；(3) 是否使用 labeled valid/invalid pairs；(4) loss function（L2 consistency vs reward maximization）；(5) training data format（labeled pairs vs sampled completions）。论文在 Section 6 第二段承认 "this gap is an observational finding, not a controlled comparison (§6)"，但 C3 仍将其包装为一个正式 contribution，且 Abstract 中也以 contribution 形式呈现。
- 为什么影响接收：观察性发现被提升为因果性 contribution，混淆了 confounded correlation 和 causal explanation。一个合理的替代解释是：ACT 成功是因为 per-token supervision + labeled pairs，与 "valid/invalid distinction" 无关。
- 建议修改方向：(a) 将 C3 降格为 "observation" 或 "hypothesis"，明确列出 confounding factors；(b) 设计消融实验分离各因素（例如：将 labeled valid/invalid 信息注入 GRPO reward，测试是否仅此一项改变就能解决问题）；(c) 或将 C3 重新表述为 "per-completion scalar reward 的信息带宽不足以编码 valid/invalid 区分"，避免因果语言。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] Wu & Tang (2026) 的对比论证缺乏定量支撑

- 具体位置：Section 6 第三段, Section 7 ("Research Design and Overoptimization")
- 问题：论文引用 Wu & Tang (2026) 作为 "representation directions 在 GRPO 中成功" 的反例，解释差异的关键论点是 "shortcut behaviors are geometrically separable"（§6），即 reward hacking 行为与正常行为在激活空间中的可分离性高于 sycophancy vs valid revision。但这个论点完全是定性的——论文没有提供任何量化比较（例如 Wu & Tang 的方向 AUROC vs 本文的 d_syc AUROC，或两个 setting 中 target/complement 的 activation overlap 程度）。考虑到本文的 d_syc AUROC 已达 0.827（相当不错的可分性），"geometric separability" 的解释并非不证自明。
- 建议：(a) 补充定量分析解释为什么 0.827 AUROC 的 discriminability 不够 "separable"——是因为 class boundary 附近的 density 分布问题？还是因为 d_syc 编码了 belief-change 而非 belief-change-warranted？(b) 或至少承认这是一个 hypothesis 而非 established explanation。

**W2** [warning] "Discriminability ≠ Reward Utility" 原则的泛化性声明超出证据

- 具体位置：Section 6 标题, Section 8 (Future Directions), Abstract 最后一句
- 问题：论文将 "discriminability ≠ reward utility" 作为一个一般性原则提出（Section 8: "Beyond sycophancy, the principle that discriminability does not guarantee scalar reward utility may apply to other behavioral attributes where the target and its complement share the same geometric direction"）。但论文的全部实验证据仅来自 sycophancy 一个 behavioral attribute、GRPO 一个 RL 算法、两个 8B 模型。将单一 case study 提升为一般性原则需要更多实证（至少测试另一个 behavioral attribute，如 hallucination 或 toxicity），或者需要更强的理论论证。
- 建议：将该原则表述为 "our results suggest" 或 "we hypothesize"，而非断言性表述。或补充理论分析解释为何该原则应 generalize。

**W3** [warning] SMART (Beigi et al., 2025) 的讨论过于简略

- 具体位置：Section 7 (Related Work)
- 问题：SMART 使用 per-step process rewards + MCTS 进行 sycophancy mitigation，代表了 scalar per-completion rewards 和 dense per-token supervision 之间的中间监督密度。这与本文的核心论点（per-completion scalar reward 信息不足）直接相关——SMART 的成功可能暗示 per-step 粒度是一个关键阈值。但论文仅用一句话提及 SMART，未深入讨论其成功如何 inform 本文关于监督粒度 / reward signal 信息量的分析。
- 建议：增加 1-2 句分析 SMART 的 per-step reward 为何可能避免本文发现的 discriminability-utility gap——是因为 step-level reward 能编码更多 context（例如推理链中的 uncertainty 信号），还是因为 MCTS 的 tree search 结构提供了隐式的 valid/invalid 对比？

**W4** [warning] 实验规模偏小，限制结论可靠性

- 具体位置：Section 2 (Experimental Framework), Table 5 (Appendix A)
- 问题：仅 181 对 contrastive pairs（去除 19 对后剩 162 对用于训练），仅 LoRA rank-64 微调，仅 8B 参数模型。GRPO seed 仅 2 个（Table 4 脚注提到 "two random seeds"），ACT 仅 1 个 seed。在如此小样本下声称 "every formulation fails" 需要更强的统计支撑。尽管 Table 4 的 SYCONCSCORE 确实一致为 0，但 seed 数量不足以排除 variance 的影响。
- 建议：(a) 增加到至少 3-5 个 seeds 以提供 variance 估计；(b) 讨论样本量对结论的影响——181 对是否足够覆盖 sycophancy 的多样性？

---

## 小问题（不影响接收）

- Abstract 信息密度极高（~250 words），尝试在一个段落中覆盖全部三个 contributions + 实验细节 + failure modes。建议精简，将部分细节移至 Introduction。
- Section 2.5 的 SYCONCSCORE 定义（公式 2）中 harmonic mean 的选择未充分 justify——为什么不用 arithmetic mean？Harmonic mean 对低值极其敏感，当 ToF 或 NoF 任一为 0 时直接归零，这是否会 mask 部分改善？
- Table 2 的 "Outcome" 列使用了 "Gate saturation" / "Norm explosion" / "Mode collapse" 等术语，但在正文中对这些 failure modes 的定义不够精确。"Mode collapse" 在 RL 语境下有特定含义（policy collapse to single action），这里是否准确？
- Figure 1 的 y 轴标签 "CV AUROC" 未在 figure caption 中解释（需要回到 Section 3 才能理解是 5-fold cross-validated AUROC）。
- Section 6 将 "unified root cause" 称为 "semantic gap"，但未形式化这个概念——什么条件下 discriminability 与 utility 之间存在 gap？什么条件下不存在？

---

## 主要优势

1. **研究问题重要且及时**：Representation engineering → RL reward 是一个自然且有实践价值的思路，系统验证其失败模式有社区价值。
2. **Probe reward trap (C2) 是新颖的实证发现**：behavioral death 先于 distributional collapse 的时序分析（Figure 2, Table 3）提供了 RLHF 失败模式的有用 characterization，这个发现独立于其他 claims，具有独立价值。
3. **跨模型验证增强可信度**：Qwen3-8B 和 Llama-3-8B 两个架构上的一致结果（Table 1）排除了 model-specific artifact 的解释。
4. **与 Papadatos & Freedman (2024) 的对比分析精到**：同一 probe 在 inference-time (Best-of-N) 成功但 training-time (GRPO reward) 失败的观察，精准定位了 "inside vs outside optimization loop" 的关键区分（Section 7），这是论文最有洞察力的分析之一。
5. **实验设计严谨**：5-fold CV、evidence strength 分层、per-layer AUROC 分析、recalibration 机制——显示了系统性的 methodology。
6. **Stubbornness taxonomy (Appendix B)** 的三种 failure mode（sycophantic stubbornness / deliberation traps / evidence-graded hedging）提供了有价值的定性补充。

---

## 对 Director 指定侧重的逐项回应

### 1. Contribution 定位与 negative result paper 的价值

三个 contributions 中，C2（probe reward trap）最有独立价值且 claim 与 evidence 匹配良好。C1（所有 GRPO formulations 失败）在 GRPO 范围内是 well-supported 的。C3（sparse RL reward 无法传递 valid/invalid 区分）是论文最有 ambition 的 claim，但也是证据最薄弱的。

作为 negative result paper，本文超越了 "we tried but failed"——probe reward trap 的时序分析和 discriminability ≠ utility 的 insight 提供了有价值的 explanation。但要达到主会议水准，需要 (a) claims 与 evidence 更好对齐，或 (b) 至少一个 constructive contribution（例如提出并验证一种修复方案）。目前定位更适合 Findings。

### 2. Claim scope vs 证据

如 N1 和 N2 所述，overclaiming 是本文最大的问题。Title 用 "Scalar RL Rewards" 但只测试了 GRPO；C3 从一个 confounded comparison 中得出因果结论。论文作者显然意识到了这些限制（Limitations section 提到了 "Other RL algorithms"），但未在主文 claims 中充分 qualify。

### 3. Related Work 覆盖

- **Papadatos & Freedman (2024)**：讨论充分且有洞察（Section 7），inference-time vs training-time 的对比是论文的亮点之一。
- **SMART (Beigi et al., 2025)**：提及但讨论不足（W3），作为中间监督密度的案例，应该被更深入地用于支持论文关于 supervision granularity 的论点。
- **Wu & Tang (2026)**：讨论了但定量支撑不足（W1），"geometric separability" 的论证需要更多证据。
- **其他遗漏**：论文未讨论 DPO/KTO 等 offline RL 方法在 sycophancy mitigation 中的应用（如 Rafailov et al., 2023 的 DPO 本身就被引用了，但未讨论是否 d_syc 可以用于构造 DPO preference pairs）。这与 N1 的问题相关——如果讨论了 DPO 的可行性，可以部分缓解 "only GRPO" 的批评。

### 4. 叙事结构

Introduction 的逻辑链总体清晰：representation engineering → discriminability → reward failure → root cause。但存在两个叙事问题：(a) Abstract 过度压缩，读者需要反复阅读才能把握全貌；(b) Section 6 的 "unified root cause" 分析试图将所有 failure 归因于 "semantic gap"，但这个概念没有被形式化，且与 probe reward trap (C2) 的时序分析之间的关系不够清晰——probe reward trap 是 semantic gap 的 consequence 还是独立的 failure mode？

### 5. Broader impact / generalizability

"Discriminability ≠ reward utility" 作为一般性原则是有吸引力的，但证据仅来自 sycophancy + GRPO 的单一组合。论文声称该原则可能适用于 "other behavioral attributes where the target and its complement share the same geometric direction"（Section 8），但未提供任何其他 attribute 的证据。这个泛化声明目前是 speculative 的（W2）。如果能补充一个简单的 pilot experiment（例如用 hallucination direction 作为 GRPO reward），将极大增强论文的影响力。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 256 · 2026-05-22T12:47:16.644842+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "project": "contrastive_entrain_calib",
  "reviewer_id": "2",
  "round_number": "1",
  "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应：对每个 Must-Fix / Should-Fix / 小问题，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 审稿意见：方法严谨性 + 实验有效性\n\n**Overall**: 2.5 (Borderline Findings)\n\n### Must-Fix 问题\n\n**N1** [critical] GRPO group_size=2 严重偏离标准实践，可能是失败的主因而非 d_syc 本身\n- 标准 GRPO 使用 group_size 8-64。group_size=2 退化为噪声极高的 pairwise 对比，对含噪 cosine reward 会极度放大梯度估计方差。论文未给出任何理由也未测试更大值。\n- 核心声明 \"every d_syc-based GRPO formulation fails\" 但如果 GRPO 优化器因 group_size 不足而无法利用微弱信号，失败不能归因于 d_syc。\n\n**N2** [critical] max_completion_length=256 导致 80-84% 截断，严重损害 reward 信号有效性\n- sycophancy calibration 的核心行为常在多轮对话后半段发生。80-84% 截断意味着 reward 在不完整输出上计算。§5 的 probe reward trap（ToF=0 at step 500）可能正因截断而非 probe 缺陷导致。\n\n**N3** [critical] 仅 2 random seeds 不足以支撑负面结论\n- RL 训练高方差。2 seeds 无法提供有意义方差估计。负面结论证据标准应高于正面结论。\n\n**N4** [critical] Reward 设计空间探索不足，声明过度推广\n- 6 个 formulation 均为简单标量变换/单层 probe。遗漏：learned reward（MLP on d_syc features）、多层聚合、非线性变换。w₁ 仅测试 0.25/0.40。\n\n### Should-Fix 问题\n\n**W1** ACT vs GRPO 对比 confounds 大量，叙事过度依赖此对比\n**W2** SYCONSCORE 指标有效性未充分建立\n**W3** 181 contrastive pairs 质量控制不足（无人工验证/IAA）\n**W4** Figure 3 cross-seed 分析与文字描述存在 tension\n\n### 小问题\n- \"entropy remained healthy\" 含糊\n- Table 2 \"gate saturation\" 缺操作性定义\n- §8 Related Work 与核心贡献连接不紧密\n- Appendix B 仅 100 条样本，无 inter-rater reliability\n- Equation 1 \"residual-stream activations\" 提取位置可更明确\n\n---\n\n请逐条回应。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "project": "contrastive_entrain_calib",
    "reviewer_id": "2",
    "round_number": "1",
    "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应：对每个 Must-Fix / Should-Fix / 小问题，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 审稿意见：方法严谨性 + 实验有效性\n\n**Overall**: 2.5 (Borderline Findings)\n\n### Must-Fix 问题\n\n**N1** [critical] GRPO group_size=2 严重偏离标准实践，可能是失败的主因而非 d_syc 本身\n- 标准 GRPO 使用 group_size 8-64。group_size=2 退化为噪声极高的 pairwise 对比，对含噪 cosine reward 会极度放大梯度估计方差。论文未给出任何理由也未测试更大值。\n- 核心声明 \"every d_syc-based GRPO formulation fails\" 但如果 GRPO 优化器因 group_size 不足而无法利用微弱信号，失败不能归因于 d_syc。\n\n**N2** [critical] max_completion_length=256 导致 80-84% 截断，严重损害 reward 信号有效性\n- sycophancy calibration 的核心行为常在多轮对话后半段发生。80-84% 截断意味着 reward 在不完整输出上计算。§5 的 probe reward trap（ToF=0 at step 500）可能正因截断而非 probe 缺陷导致。\n\n**N3** [critical] 仅 2 random seeds 不足以支撑负面结论\n- RL 训练高方差。2 seeds 无法提供有意义方差估计。负面结论证据标准应高于正面结论。\n\n**N4** [critical] Reward 设计空间探索不足，声明过度推广\n- 6 个 formulation 均为简单标量变换/单层 probe。遗漏：learned reward（MLP on d_syc features）、多层聚合、非线性变换。w₁ 仅测试 0.25/0.40。\n\n### Should-Fix 问题\n\n**W1** ACT vs GRPO 对比 confounds 大量，叙事过度依赖此对比\n**W2** SYCONSCORE 指标有效性未充分建立\n**W3** 181 contrastive pairs 质量控制不足（无人工验证/IAA）\n**W4** Figure 3 cross-seed 分析与文字描述存在 tension\n\n### 小问题\n- \"entropy remained healthy\" 含糊\n- Table 2 \"gate saturation\" 缺操作性定义\n- §8 Related Work 与核心贡献连接不紧密\n- Appendix B 仅 100 条样本，无 inter-rater reliability\n- Equation 1 \"residual-stream activations\" 提取位置可更明确\n\n---\n\n请逐条回应。"
  }
}
```

</details>

---


### Tool result

_source line 257 · 2026-05-22T12:47:35.244742+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 18599
}
```

</details>

---


### Tool call

_source line 258 · 2026-05-22T12:47:35.445810+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "project": "contrastive_entrain_calib",
  "reviewer_id": "1",
  "round_number": "1",
  "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应：对每个 Must-Fix / Should-Fix / 小问题，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 审稿意见：新颖性 + Framing 完整性\n\n**Overall**: 3.0（Findings）\n\n### Must-Fix 问题\n\n**N1** [critical] Title 和 claims 范围显著超出实验证据\n- 标题声称 \"Sycophancy Directions Fail as Scalar RL Rewards\"，但仅测试 GRPO。C3 将失败归因于 reward signal 本身而非 GRPO 的 specific optimization dynamics，此归因未被实验证实。\n- 建议：将标题改为 \"…as GRPO Rewards\" 或 \"…as Scalar Per-Completion Rewards: Evidence from GRPO\"；或补充 PPO/REINFORCE 实验。\n\n**N2** [critical] C3 的 ACT vs GRPO 对比存在严重 confound，但被表述为 contribution\n- C3 声称 \"sparse RL reward failed to convey the valid/invalid distinction\"，核心证据来自 ACT 成功而 GRPO 失败。但 ACT 与 GRPO 至少在 5 个维度上不同（SFT vs RL、per-token vs per-completion、labeled pairs vs self-discovery、L2 vs reward maximization、training data format）。\n- 观察性发现被提升为因果性 contribution。\n\n### Should-Fix 问题\n\n**W1** Wu & Tang (2026) 的对比论证缺乏定量支撑——\"geometric separability\" 论点完全定性。\n**W2** \"Discriminability ≠ Reward Utility\" 原则的泛化性声明超出证据（仅 sycophancy + GRPO）。\n**W3** SMART (Beigi et al., 2025) 讨论过于简略——作为中间监督密度案例，应更深入讨论。\n**W4** 实验规模偏小（181 pairs, 2 seeds, 单模型 RL 训练）。\n\n### 小问题\n- Abstract 信息密度极高（~250 words），建议精简。\n- SYCONSCORE harmonic mean 选择未充分 justify。\n- Table 2 failure mode 术语定义不精确（\"mode collapse\" 是否准确？）\n- Figure 1 y 轴标签未在 caption 中解释。\n- §6 \"semantic gap\" 未形式化。\n\n### 主要优势\n1. 研究问题重要且及时\n2. Probe reward trap (C2) 是新颖实证发现\n3. 跨模型验证增强可信度\n4. 与 Papadatos & Freedman (2024) 对比分析精到\n5. 实验设计严谨（5-fold CV, evidence strength 分层）\n6. Stubbornness taxonomy 有价值\n\n---\n\n请逐条回应。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "project": "contrastive_entrain_calib",
    "reviewer_id": "1",
    "round_number": "1",
    "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应：对每个 Must-Fix / Should-Fix / 小问题，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 审稿意见：新颖性 + Framing 完整性\n\n**Overall**: 3.0（Findings）\n\n### Must-Fix 问题\n\n**N1** [critical] Title 和 claims 范围显著超出实验证据\n- 标题声称 \"Sycophancy Directions Fail as Scalar RL Rewards\"，但仅测试 GRPO。C3 将失败归因于 reward signal 本身而非 GRPO 的 specific optimization dynamics，此归因未被实验证实。\n- 建议：将标题改为 \"…as GRPO Rewards\" 或 \"…as Scalar Per-Completion Rewards: Evidence from GRPO\"；或补充 PPO/REINFORCE 实验。\n\n**N2** [critical] C3 的 ACT vs GRPO 对比存在严重 confound，但被表述为 contribution\n- C3 声称 \"sparse RL reward failed to convey the valid/invalid distinction\"，核心证据来自 ACT 成功而 GRPO 失败。但 ACT 与 GRPO 至少在 5 个维度上不同（SFT vs RL、per-token vs per-completion、labeled pairs vs self-discovery、L2 vs reward maximization、training data format）。\n- 观察性发现被提升为因果性 contribution。\n\n### Should-Fix 问题\n\n**W1** Wu & Tang (2026) 的对比论证缺乏定量支撑——\"geometric separability\" 论点完全定性。\n**W2** \"Discriminability ≠ Reward Utility\" 原则的泛化性声明超出证据（仅 sycophancy + GRPO）。\n**W3** SMART (Beigi et al., 2025) 讨论过于简略——作为中间监督密度案例，应更深入讨论。\n**W4** 实验规模偏小（181 pairs, 2 seeds, 单模型 RL 训练）。\n\n### 小问题\n- Abstract 信息密度极高（~250 words），建议精简。\n- SYCONSCORE harmonic mean 选择未充分 justify。\n- Table 2 failure mode 术语定义不精确（\"mode collapse\" 是否准确？）\n- Figure 1 y 轴标签未在 caption 中解释。\n- §6 \"semantic gap\" 未形式化。\n\n### 主要优势\n1. 研究问题重要且及时\n2. Probe reward trap (C2) 是新颖实证发现\n3. 跨模型验证增强可信度\n4. 与 Papadatos & Freedman (2024) 对比分析精到\n5. 实验设计严谨（5-fold CV, evidence strength 分层）\n6. Stubbornness taxonomy 有价值\n\n---\n\n请逐条回应。"
  }
}
```

</details>

---


### Tool result

_source line 259 · 2026-05-22T12:47:36.915234+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1469
}
```

</details>

---


### Assistant

_source line 260 · 2026-05-22T12:47:42.838581+00:00_

交叉分享已派发。等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director"
}
```

</details>

---


## Round 20

## Round 20

2 recorded events


### User

_source line 261 · 2026-05-22T12:47:44.346961+00:00_

[Reviewer 2 审稿结果]:
审稿意见已提交给 Review Director。

**审稿结论摘要**：Overall 3.0（Findings），Soundness 3/5，Excitement 2.5/5。

**两个 Must-Fix 问题**：
1. 标题声称 "Scalar RL Rewards" 但仅测试 GRPO——需收窄标题或补充 PPO/REINFORCE 实验
2. C3（sparse RL reward 无法传递 valid/invalid 区分）基于 ACT vs GRPO 的 confounded comparison，不应作为 contribution 提出

**四个 Should-Fix**：Wu & Tang 对比缺乏定量支撑、"discriminability ≠ utility" 泛化声明超出证据、SMART 讨论过简、实验规模偏小（2 seeds）。

论文的主要优势在于 probe reward trap 的时序分析和 Papadatos & Freedman 对比的精到分析，这些是独立有价值的发现。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 262 · 2026-05-22T12:47:50.706674+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director"
}
```

</details>

---


## Round 21

## Round 21

2 recorded events


### User

_source line 263 · 2026-05-22T12:49:55.681259+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应

---

### Must-Fix 问题

**[AGREE] R2-N1: Title 和 claims 范围超出实验证据**

同意。这与我自己的 N4（设计空间探索不足）高度相关。论文标题 "Why Sycophancy Directions Fail as Scalar RL Rewards" 暗示了对所有 scalar RL rewards 的普遍性声明，但实验仅覆盖 GRPO。关键证据来自论文自身——§8 Future Directions (p.8) 明确承认："The scalar per-completion reward structure is shared by PPO, RLOO, and other REINFORCE-style methods; whether they exhibit similar failures remains an open question." 这一句直接承认 PPO/REINFORCE 是否复现失败尚不确定，与标题的普遍性声明矛盾。

补充发现：C1 的措辞 "Every tested GRPO formulation fails"（p.2）实际上已经用了 "tested GRPO" 的限定词，比标题更谨慎。标题与正文 contributions 之间存在 scope 不一致。R2 建议改标题为 "…as GRPO Rewards" 或补充 PPO/REINFORCE 实验，两者都是合理的修改路径。

**[AGREE] R2-N2: C3 的 ACT vs GRPO 对比被表述为 contribution 但 confound 未解决**

同意，与我的 W1 一致。论文 §7 (p.7) 的原文："ACT and GRPO differ along multiple dimensions beyond supervision granularity, so we cannot rotate the causal factor behind ACT's advantage"——论文自己承认无法归因，但 p.2 的 C3 仍表述为 "In our experiments, sparse RL reward failed to convey the valid/invalid distinction"，并将其列为三大 contribution 之一。这里存在逻辑矛盾：如果你承认无法归因，就不应将观察性比较提升为 contribution。

R2 的批评比我的 W1 更精准——我将其列为 Should-Fix，但实际上作为 contribution 声明，其 confound 问题确实是 critical 级别。ACT 的成功可能完全归因于 SFT 的固有稳定性优势、labeled data 的直接监督信号、或 per-token loss 的梯度密度，而与 "representation vs. reward" 这个叙事框架无关。

---

### Should-Fix 问题

**[AGREE] R2-W1: Wu & Tang (2026) 的 "geometric separability" 论点缺乏定量支撑**

同意。§6 (p.6) 引用 Wu & Tang (2026) 称 "concept directions applied via activation modification or GRPO achieve 100% validation accuracy for reward hacking detection, where shortcut behaviors are geometrically separable"，用以论证 direction utility 取决于 geometric separability。但论文未提供自己的定量证据来衡量 d_syc 的 "几何可分性程度"。例如，论文可以计算 d_syc 在 online RL 分布下的 cosine similarity 分布重叠度（valid vs. sycophantic），与 Wu & Tang 中 reward hacking 场景的分离度做定量对比，从而将定性论点升级为定量证据。

**[AGREE] R2-W2: "Discriminability ≠ Reward Utility" 泛化声明超出证据**

同意，与我的 N4 一致。该原则仅在一个行为维度（sycophancy）、一个 RL 算法（GRPO）上验证。§8 (p.8) 的 "Beyond sycophancy, the principle that discriminability does not guarantee scalar reward utility may apply to other behavioral attributes where the target and its complement share the same geometric direction" 是合理的未来方向猜想，但论文标题和 Abstract 的措辞暗示了更强的普遍性。

**[AGREE] R2-W3: SMART (Beigi et al., 2025) 讨论过于简略**

同意。§8 (p.8) 仅用一句话提及 SMART："SMART (Beigi et al., 2025) applies per-step process rewards with MCTS for sycophancy, representing intermediate supervision density between scalar per-completion rewards and dense per-token approaches." 作为 per-completion（GRPO）和 per-token（ACT）之间的中间形态，SMART 直接回应了论文的核心发现——supervision granularity 对成败的影响。如果 SMART 的 per-step 方式部分成功，这将为"密度是关键因素"提供更细粒度的证据；如果也失败，则加强"问题不在密度而在 d_syc 本身"的论点。无论如何，更深入讨论 SMART 都会显著增强 §8 的论证力度。

**[AGREE] R2-W4: 实验规模偏小**

同意，与我的 N3（2 seeds）和 W3（181 pairs）一致。补充一点：RL 训练仅在 Qwen3-8B 上执行（Llama-3-8B 仅做了 discriminability 验证，未做 GRPO 训练），这进一步限制了结论的泛化性。论文 Limitations (p.8) 承认了这一点。

---

### 小问题

**[REBUT] R2-Minor-1: Abstract 信息密度过高**

轻微反驳。*ACL 系列会议的 abstract 通常 200-300 words，该 abstract 的信息密度在可接受范围内。对于一篇负面结果论文，abstract 需要同时传达 (1) 方法有效（discriminability）、(2) 但 reward 失败、(3) 失败机制，信息量本身难以压缩。不过如果简化措辞（如合并部分数字）能改善可读性，这是值得做的 polish。

**[AGREE] R2-Minor-2: SYCONSCORE harmonic mean 选择未充分 justify**

同意，与我的 W2 一致。Equation 2 (§2.5, p.3) 给出定义但未解释为何选择 harmonic mean（对低值更敏感）而非 arithmetic mean 或 F-beta。

**[AGREE] R2-Minor-3: Table 2 failure mode 术语不精确**

同意。Table 2 (p.5) 中 F1d 的 "Mode collapse" 需要操作性定义。在 RL 文献中 mode collapse 通常指策略退化到单一输出模式，但表中描述的是 "mode collapse" 伴随 "scaled cosine" 的行为——是否指 reward 空间的坍缩而非策略空间？需要明确。

**[AGREE] R2-Minor-4: Figure 1 y 轴标签未在 caption 中解释**

同意。Figure 1 (p.5) 的 y 轴标签应在 caption 中明确说明 AUROC 的含义和计算方式。

**[AGREE] R2-Minor-5: §6 "semantic gap" 未形式化**

同意。§6 (p.6) 的 "semantic gap between discriminability and reward utility" 是论文的核心概念贡献，但仅以自然语言描述。可以考虑形式化为：给定方向 d 和行为空间上的 reward function R*，定义 "utility gap" 为 d 的分类 AUROC 与 d-based reward 的 GRPO 策略改进之间的差距。即使简单的形式化也比纯定性描述更有说服力。

---

### 对 R2 优势评价的补充

R2 列出的 6 条优势我基本认同，特别是：
- **Probe reward trap (C2)** 确实是最有价值的实证发现——behavioral death 先于 distributional collapse、1,300-step 的检测盲区对 practitioners 有直接的实践警示。
- **跨模型验证**（Qwen3-8B + Llama-3-8B 的 AUROC 一致性）增强了 d_syc 方向本身的可信度，尽管 RL 训练仅在单模型上执行。

---

### R1 与 R2 评分差异说明

R2 给 Overall 3.0（Findings），我给 2.5（Borderline Findings）。差异主要来自我对 GRPO 优化配置（group_size=2, 80-84% truncation）的更重视——这些是 R2 未重点讨论但我认为是核心 confound 的问题。如果 GRPO 本身因 group_size 过小和严重截断而无法正常工作，那么不仅 C1 的负面结论不可靠，C2（probe reward trap）的失败机制归因也可能不准确——behavioral death 可能是截断而非 probe 的产物。这些 confounds 同时削弱了 R2 所认可的 C2 新颖性。

综合两份审稿，核心共识是：**标题/claims 的 overclaiming（R2-N1 + R1-N4）** 和 **ACT vs GRPO confound（R2-N2 + R1-W1）** 是两个需要共同解决的关键问题。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 264 · 2026-05-22T12:50:02.768542+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director"
}
```

</details>

---


## Round 22

## Round 22

2 recorded events


### User

_source line 265 · 2026-05-22T12:50:15.448715+00:00_

[Reviewer 1 审稿结果]:
已提交对 R2 的逐条回应。总结：

- **Must-Fix**：R2-N1（标题 overclaiming）和 R2-N2（C3 confound 作为 contribution）均 **[AGREE]**，与我自己的 N4 和 W1 一致
- **Should-Fix**：W1-W4 全部 **[AGREE]**，其中 W3（SMART 讨论不足）和 W4（实验规模）补充了我自己的发现
- **小问题**：仅对 Abstract 信息密度 **[REBUT]**（*ACL 论文 abstract 的密度在合理范围），其余 4 条均 **[AGREE]**
- **评分差异说明**：我比 R2 低 0.5 分（2.5 vs 3.0），主要因为我更重视 group_size=2 和 80-84% truncation 这两个 R2 未重点讨论的优化配置问题

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 266 · 2026-05-22T12:50:21.216955+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director"
}
```

</details>

---


## Round 23

## Round 23

8 recorded events


### User

_source line 267 · 2026-05-22T12:51:38.178800+00:00_

[Reviewer 2 审稿意见]:

## Reviewer 2 对 Reviewer 1 审稿意见的逐条回应

---

### Must-Fix 问题

**[AGREE] R1-N1: group_size=2 严重偏离标准实践**

强烈同意。这是 R1 最有力的发现，且我在首轮审稿中未能识别。

从 Appendix A Table 5 确认 GRPO group_size 极小。原始 GRPO 论文（Shao et al., 2024）使用 group_size=64，后续文献中 8-16 为下限。group_size=2 意味着每个 prompt 仅采样 2 个 completion 来估算 advantage——advantage = reward - group_mean，当 group 仅 2 个样本时，估计方差极大。

这构成一个根本性的 confound：论文声称 "every d_syc-based GRPO formulation fails"（C1），但如果 GRPO 的 advantage estimator 本身因 group_size=2 而高度噪声化，则无法区分两种解释：(a) d_syc reward 信号根本不可用；(b) d_syc reward 信号微弱但可用，只是 group_size=2 的 GRPO 无法从中提取有效梯度。解释 (b) 未被排除。

补充：这也与 §5 probe reward trap 的解释相关。R1 提到的高方差梯度估计可能是导致 behavioral death（ToF→0 at step 500）的直接原因——不是 probe reward 的 structural failure，而是 group_size=2 导致的 optimization instability。论文至少需要补充 group_size=8 或 16 的对照实验，才能隔离 reward signal quality 与 optimizer 配置的效应。

**[AGREE] R1-N2: max_completion_length=256 导致 80-84% 截断**

同意这是一个严重的实验设计问题。Appendix A 明确承认 "80-84% truncation of multi-turn responses"。论文的训练数据是 3-turn 对话（skeleton generation → 3-turn dialogue completion，§2），256 tokens 远不足以生成完整的多轮对话。

关键质疑：如果模型无法生成完整响应，reward 是在 truncated output 上计算的。对于 cosine reward（F1a-F1d），d_syc 在 truncated activation 上的投影可能不反映完整响应的 sycophantic 倾向。对于 probe reward（F2, F3），probe 在 truncated 文本上的判断更可能出错。§5 的 probe reward trap（ToF→0 at step 500）可能正是因为 truncated 输出缺乏足够的行为信号供 probe 判断，而非 probe 方向本身的缺陷。

一个加重的因素：truncation 还会导致 RL 训练中 reward signal 的 distribution shift——随着模型策略变化，不同 completion 的截断点不同，导致 reward 的 non-stationarity 远超正常水平。这与 §5 观察到的 stochastic oscillation（Figure 3）可能有因果关系。

论文需要 (a) 至少测试 max_completion_length=512 或 1024 的对照，或 (b) 对 truncated vs non-truncated samples 分别分析 reward distribution，以排除 truncation artifact。

**[AGREE] R1-N3: 仅 2 random seeds 不足**

完全同意，这与我在首轮审稿中提出的 W4 一致。补充两点：

1. Table 4 显示 GRPO 的 SYCONCSCORE 全部为 0.000，这看似一致，但 0.000 是因为 SYCONCSCORE 使用 harmonic mean（Equation 2）——当 ToF 或 NoF 任一为 0 时，SYCONCSCORE 自动归零。因此"全部为零"可能是指标设计的 artifact（对零值极端敏感）而非 truly consistent failure。2 seeds 的 ToF/NoF 原始值的 variance 未被报告。

2. 对于 negative result paper，证据标准应高于 positive result paper。论文声称一个方法"失败"，如果存在即使 5% 的概率某个 seed 能成功，结论就被推翻。2 seeds 无法排除这种可能性。至少需要 5 seeds 并报告 mean ± std。

**[REBUT] R1-N4: Reward 设计空间探索不足——部分反驳**

R1 的批评有合理成分，但我认为部分论点被论文的概念性分析所缓解。

R1 指出论文遗漏了 "learned reward（MLP on d_syc features）"、"multi-layer aggregation" 等方向。然而，论文的核心论点（Section 6）是 d_syc 编码的是 "whether belief changed"（是否发生了信念改变）而非 "whether it should have"（信念改变是否合理）。如果 d_syc 方向本身不携带 valid/invalid 的区分信息，任何对 d_syc 的单调或非线性变换（包括 MLP）都不应改善结果——因为输入特征本身缺乏所需信息。这个论点在 Section 6 的 "unified root cause" 分析中有逻辑支撑。

**但我同意以下两点**：
1. **w₁ 的搜索范围过窄**（仅 0.25 和 0.40，Table 2）。reward weight 是一个关键超参，仅测试 2 个值且间距仅 0.15 是不够的。至少应覆盖 0.1-1.0 的范围。
2. **multi-layer aggregation** 是一个不同于 "d_syc 的变换" 的方向——它可能提取出与 d_syc 不同的信息（例如不同层编码了 valid/invalid 的信息）。论文 Figure 1 显示 discriminability 在不同层差异显著（Qwen3-8B 在 L19 达峰），但仅使用了 best single layer。多层聚合可能捕捉到更丰富的信号。这个方向论文未讨论，R1 的批评在此成立。

综合判断：R1-N4 的核心批评（设计空间过窄）有效，但将其提升为 "critical" 级别稍显过重——因为论文提供了 conceptual argument 解释为何更复杂的 transform 可能无效。建议降为 Should-Fix，同时要求作者 (a) 扩展 w₁ 搜索范围，(b) 讨论 multi-layer aggregation 的 potential。

---

### Should-Fix 问题

**[AGREE] R1-W1: ACT vs GRPO confound**

完全同意，这与我在首轮审稿中的 N2 一致。ACT 与 GRPO 至少在训练范式、监督粒度、labeled pair 使用、loss function、data format 五个维度上存在差异。论文在 Section 6 承认 "this gap is an observational finding, not a controlled comparison"，但 C3 仍将其包装为 contribution。这个 confound 需要在主文中更明确地 qualify。

**[AGREE] R1-W2: SYCONCSCORE 指标有效性**

同意。补充一个具体问题：SYCONCSCORE 使用 harmonic mean（Equation 2, §2.5），当 ToF=0 或 NoF=0 时自动归零。这意味着 Table 4 中所有 GRPO 行的 SYCONCSCORE=0.000 可能掩盖了部分改善——例如 ToF 有所提升但 NoF 仍为 0 的情况。论文应报告 ToF 和 NoF 的独立数值（Table 4 的右侧列 "ToF" 确实报告了 ToF 原始值，但缺少 confidence interval）。

此外，harmonic mean 的选择未充分 justify。在 calibration 场景下，是否需要 ToF 和 NoF 同时非零才算 "成功"？这个 all-or-nothing 标准是否过于严格？Arithmetic mean 会给出不同的 picture。

**[AGREE] R1-W3: 181 pairs 质量控制**

同意。GPT-4.1 生成 + automated style matching validation（§2）不等于内容正确性验证。sycophantic capitulation vs valid revision 的标注是论文核心任务的基础，需要至少对一个 subset 进行人工验证并报告 agreement rate。

**[AGREE] R1-W4: Figure 3 cross-seed tension**

同意。Figure 3 显示 R₃-only GRPO 的 2 条 seed 轨迹存在显著差异——seed 1 在 checkpoint 6500 crash，seed 2 在 checkpoint 4000 crash，onset 相差 ~2500 步。论文描述 "similar amplitude (Δ ≈ 0.009) and identical crash depth (0.074)" 是从 2 个点推断 pattern，统计意义很弱。

更重要的是，论文声称 "Cross-seed rank correlation is r≈1.0 during early training (steps 1000-3000) but drops to ρ≈0.33 (n.s.) after step 4000"（§7，p7 右栏）。从 2 个 seed 计算 rank correlation 在统计上没有意义——2 个数据点的 Spearman rank correlation 只能取 +1 或 -1，不可能得到 0.33。这里的描述可能是在 time-step level 而非 seed level 计算的，但论文未清楚说明。

---

### 小问题

**[AGREE]** "entropy remained healthy"（§5）：同意，含糊。应给出具体的 entropy 数值范围。

**[AGREE]** Table 2 "gate saturation"：同意，我也在首轮审稿中标记了此问题。需要操作性定义——具体阈值或条件是什么？

**[AGREE]** Related Work 与核心贡献连接：部分同意。§7 的结构是按主题分节（Representation Engineering / Research Design / Sycophancy Characterization / Probe-Based Methods），覆盖面广但与论文自身发现的 connection 可以更紧密。不过 Probe-Based Inference-Time Mitigation 小节与核心贡献的连接做得较好（Papadatos & Freedman 对比）。

**[AGREE]** Appendix B 的 100 条样本无 inter-rater reliability：同意。定性分析应至少有 2 位标注者独立分类并报告 Cohen's κ。

**[REBUT]** Equation 1 "residual-stream activations" 提取位置：部分反驳。论文在 Section 3 明确说明了层选择方法——"The target layer is selected by 5-fold cross-validated AUROC; on Qwen3-8B this yields layer 19"（§3, p3），且 Table 1 报告了两个模型的 best layer（L19 和 L16）。Figure 1 展示了 per-layer AUROC 曲线。提取位置的信息是充分的。但 R1 说的可能是 Equation 1 本身的表述可以更精确——例如是 post-attention 还是 post-MLP 的 residual stream？这个技术细节确实值得在 §2 补充一句。

---

### 综合评估

R1 的 N1（group_size=2）和 N2（80-84% truncation）是我在首轮审稿中**未充分识别**的重要问题。这两个 confound 从根本上质疑了论文的核心因果推断——"d_syc fails as RL reward" 可能被 "GRPO 配置不当导致 RL 训练本身失败" 所解释。

如果加入 R1 的发现，我倾向于将 Overall Assessment 从 3.0 下调至 **2.5（Borderline Findings）**，与 R1 的评分一致。论文需要至少补充 group_size 和 completion_length 的消融实验，才能将 failure 归因于 d_syc reward signal 本身。

调整后评分：
| 维度 | 原评分 | 调整后 | 理由 |
|------|--------|--------|------|
| Soundness | 3.0 | 2.5 | R1-N1 和 N2 揭示的 confounds 使 main claims 支撑不足 |
| Excitement | 2.5 | 2.5 | 不变 |
| Overall | 3.0 | 2.5 | Borderline Findings——需消融实验排除 optimizer 配置问题 |


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 268 · 2026-05-22T12:52:01.672025+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "contrastive_entrain_calib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "contrastive_entrain_calib"
  }
}
```

</details>

---


### Tool result

_source line 269 · 2026-05-22T12:52:01.722728+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-22T12:40:18.989485+00:00\", \"completed_at\": \"2026-05-22T12:43:37.543972+00:00\", \"findings\": [{\"severity\": \"warning\", \"dimension\": \"pages 1-3\", \"message\": \"连续 3 页无 figure/table（仅 page 3 有两个行间公式）。审稿人翻到 page 4 才看到首个视觉锚点（Table 1 + Figure 1）。论文以实证为主，前 3 页纯文字严重延迟第一印象的锚定。建议在 page 2 前插入一个概念总览图或核心结果 teaser figure，让审稿人在 Abstract 之后立刻建立认知框架。\"}, {\"severity\": \"warning\", \"dimension\": \"page 11\", \"message\": \"Appendix B（Stubbornness Taxonomy）仅占页面约 25%，剩余 75% 为空白。对审稿人的最后印象不佳——论文看起来没有写满。建议将 Appendix B 内容上移与 Appendix A 合并到同一页，或扩充 Appendix B 的分析深度填满页面。\"}, {\"severity\": \"info\", \"dimension\": \"page 5\", \"message\": \"Table 3（Probe reward trap trajectory）列数较多（~6 列），挤在单栏宽度内，表头文字偏小且行间紧凑。部分数值列标题在打印尺寸下可能低于 8pt 可读阈值。建议考虑用 \\\\resizebox 微调或改为 table* 全宽排版。\"}, {\"severity\": \"info\", \"dimension\": \"page 6\", \"message\": \"Table 4（所有方法对比）中 ACT (seed 2) 行标注 \\\"ongoing: 4/16 ckpts evaluated\\\"，在正式投稿论文中展示未完成实验的结果会给审稿人留下 work-in-progress 印象。若投稿前实验已完成，应更新数据；若确实未完成，建议移至 appendix 并标注说明。\"}, {\"severity\": \"info\", \"dimension\": \"pages 1-8\", \"message\": \"全文 3 个 figure 均为折线图（metrics-over-steps/layers），缺少概念性图示（如 framework overview、pipeline diagram）。实证论文通常受益于一个 high-level 架构图帮助审稿人快速理解方法设计——当前缺失会让审稿人在前 3 页纯文字中难以形成方法的视觉心智模型。\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Figure 3 包含多条彩色折线（~6 条 conditions），部分颜色在小尺寸下区分度有限。建议辅以不同 line style（dashed/dotted）和 marker shape 增强可区分性，尤其考虑灰度打印场景。\"}], \"counts\": {\"critical\": 0, \"warning\": 2, \"info\": 4}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 270 · 2026-05-22T12:54:00.801359+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "contrastive_entrain_calib",
  "issues_yaml": "issues:\n  # === ROUND 1-2 ISSUES (UPDATED FOR ROUND 3) ===\n\n  - id: R1-N1\n    summary: \"Fisher exact test 将非独立 checkpoints 当独立样本，p<0.0001 不可信\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 首提，R2 完全同意。\"\n      - round: 2\n        reviewers: []\n        note: \"本轮未提及。论文已移除 Fisher p 值。已修复。\"\n      - round: 3\n        reviewers: []\n        note: \"本轮未提及，确认已修复。\"\n    resolution: \"论文已移除所有 Fisher p 值，改用描述���统计。\"\n    resolution_round: 2\n\n  - id: R2-N1\n    summary: \"遗漏 Papadatos & Freedman (2024) probe penalty 成功案例\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 3\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"必须讨论 probe penalty vs probe reward 的关键差异。\"\n      - round: 2\n        reviewers: [2]\n        note: \"R2 将其列为论文优势——对比分析已充分。\"\n      - round: 3\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 均列为论文优势之一（inference-time vs training-time 对比精到）。确认已解决。\"\n    resolution: \"§7 充分讨论，Round 2-3 均被列为论文优势。\"\n    resolution_round: 2\n\n  - id: R2-N2\n    summary: \"references.bib 多条引用严重不完整\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"ACT 作者为 Unknown，6 条仅 et al.\"\n      - round: 3\n        reviewers: []\n        note: \"本轮未提及，确认已修复。\"\n    resolution: \"Agent 已补全所有 bib entry。\"\n    resolution_round: 2\n\n  - id: R1-N2\n    summary: \"ACT 正面结果仅基于单 seed 完整评估（seed 2 仍 ongoing）\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 3\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"n=1 seed 不足以建立方法有效性。\"\n      - round: 2\n        reviewers: [1, 2]\n        note: \"Table 4 脚注仍显示部分 checkpoints。\"\n      - round: 3\n        reviewers: [1, 2]\n        note: \"Table 4 脚注 ‡ 显示 4/16。视觉审查也标记 ongoing 数据给人 work-in-progress 印象。R1 列为 N3，R2 列为 W4。\"\n    action_items:\n      - round: 3\n        action: \"完成 ACT seed 2 全部 16 checkpoints 评估，或降级为 preliminary evidence\"\n        assigned_to: agent\n        status: open\n\n  - id: R1-N3\n    summary: \"ACT vs GRPO 对比存在多维 confound，C3 不应作为 contribution\"\n    category: framing\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 3\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"论文 framing 为 'd_syc fails' 但证据仅支持 'sparse scalar d_syc reward fails in GRPO'。\"\n      - round: 2\n        reviewers: [1, 2]\n        note: \"§6 因果措辞仍过强。\"\n      - round: 3\n        reviewers: [1, 2]\n        note: \"R2-N2 [AGREE by R1]：C3 将 confounded observation 提升为 contribution，逻辑矛盾——§6 承认无法归因但 C3 仍用因果语言。两位 Reviewer 共识此为 critical。\"\n    action_items:\n      - round: 3\n        action: \"C3 从 contribution 降格为 observation/hypothesis；移除因果语言；明确列出 5+ confounding factors\"\n        assigned_to: paper_agent\n        status: open\n\n  - id: R1-W2\n    summary: \"标题和 claims scope 过于宽泛——仅测试 GRPO 但泛化到 Scalar RL Rewards\"\n    category: framing\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 3\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"DPO/PPO 未测试。\"\n      - round: 2\n        reviewers: [1, 2]\n        note: \"标题已改但 §6 仍声称 PPO/RLOO 泛化。\"\n      - round: 3\n        reviewers: [1, 2]\n        note: \"R2-N1 [AGREE by R1]：标题 'Scalar RL Rewards' 暗示对所有 RL 的普遍结论，但实验只有 GRPO。§8 自己承认 PPO/RLOO 是 open question，与标题矛盾。两位共识为 critical。\"\n    action_items:\n      - round: 3\n        action: \"标题改为 '...as GRPO Rewards' 或 '...as Scalar Per-Completion Rewards: Evidence from GRPO'；或补充 PPO/REINFORCE 实验\"\n        assigned_to: paper_agent\n        status: open\n\n  - id: R1-W1\n    summary: \"超参数 w1 仅测试 0.25/0.40 两个值 + multi-layer aggregation 未探索\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 3\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 首提。\"\n      - round: 2\n        reviewers: [1, 2]\n        note: \"再次列为 Should-Fix。\"\n      - round: 3\n        reviewers: [1, 2]\n        note: \"R1-N4 部分 [REBUT by R2]：概念论证部分缓解 MLP 变体的必要性，但 w₁ 搜索范围和 multi-layer aggregation 仍为有效批评。R2 建议从 critical 降为 warning。\"\n    action_items:\n      - round: 3\n        action: \"扩展 w₁ 到 {0.1, 0.25, 0.4, 0.6, 0.8}；讨论 multi-layer aggregation 的 potential\"\n        assigned_to: paper_agent\n        status: open\n\n  - id: R1-W3\n    summary: \"AUROC ±值来自 5-fold CV std，不是正式 CI\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 3\n        reviewers: []\n        note: \"本轮未提及，论文已标注 '5-fold CV σ=0.028'。确认已修复。\"\n    resolution: \"全文已标注 5-fold CV std。\"\n    resolution_round: 2\n\n  - id: R1-W4\n    summary: \"Contrastive pairs 质量控制不足——evidence strength 标注无 IAA\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 3\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"未说明 pairs 构建方法。\"\n      - round: 2\n        reviewers: [1, 2]\n        note: \"构建方法已描述但 evidence strength 三级标注仍缺 IAA。\"\n      - round: 3\n        reviewers: [1, 2]\n        note: \"R1-W3 [AGREE by R2]：GPT-4.1 生成 + automated validation 不等于内容正确性验证，需人工验证 subset。\"\n    action_items:\n      - round: 3\n        action: \"至少对一个 subset 进行人工验证并报告 agreement rate；或在 Limitations 显式承认\"\n        assigned_to: paper_agent\n        status: open\n\n  - id: R1-W5\n    summary: \"所有 RL/SFT 训练仅在 Qwen3-8B 上进行\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 3\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"经验性 claim 需限定范围。\"\n      - round: 3\n        reviewers: [1, 2]\n        note: \"R2-W4 [AGREE by R1]：Llama-3-8B 仅做了 discriminability 验证。两位共识实验规模偏小。\"\n    action_items:\n      - round: 3\n        action: \"全文限定为 'In experiments on Qwen3-8B' case study\"\n        assigned_to: paper_agent\n        status: open\n\n  - id: R1-W6\n    summary: \"Cross-seed 分析仅 2 个 seed，负面结论证据标准不足\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 3\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"建议 ≥3 seeds。\"\n      - round: 3\n        reviewers: [1, 2]\n        note: \"R1-N3 [AGREE by R2]：2 seeds 无法排除某 seed 成功的可能。R2 补充：SYCONSCORE harmonic mean 对零值极敏感，全部为零可能是指标 artifact。升级为 critical。\"\n    action_items:\n      - round: 3\n        action: \"增加到 3-5 seeds 并报告 mean ± std；或将结论限定为 observational\"\n        assigned_to: agent\n        status: open\n\n  - id: R2-W2\n    summary: \"Process Reward Models (SMART) 讨论不足\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 3\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"supervision density hypothesis 直接预测 SMART 应部分成功。\"\n      - round: 3\n        reviewers: [1, 2]\n        note: \"R2-W3 [AGREE by R1]：SMART per-step reward 是 per-completion 和 per-token 之间的中间形态，与论文核心发现直接相关，应深入讨论。\"\n    action_items:\n      - round: 3\n        action: \"§7 增加 1-2 句分析 SMART per-step reward 如何 inform supervision granularity 论点\"\n        assigned_to: paper_agent\n        status: open\n\n  - id: R2-W3\n    summary: \"Conclusion overclaiming ('any alignment effort')\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"通过 R2-W2 覆盖：discriminability ≠ utility 泛化声明超出单一 case study 证据。\"\n    action_items:\n      - round: 3\n        action: \"§8 表述改为 'our results suggest' / 'we hypothesize'，避免断言性表述\"\n        assigned_to: paper_agent\n        status: open\n\n  - id: REV-1\n    summary: \"80-84% truncation rate (max_completion_length=256) 影响结果有效性\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 3\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"Appendix A 已披露。建议测试 512。\"\n      - round: 3\n        reviewers: [1, 2]\n        note: \"R1-N2 [AGREE by R2]：严重升级——truncation 可能是 probe reward trap 的直接原因。reward 在 truncated output 上计算，可能不反映完整响应的 sycophantic 倾向。R2 补充 truncation 导致 reward non-stationarity 加剧。两位共识升级为 critical。\"\n    action_items:\n      - round: 3\n        action: \"至少一个 config 测试 max_completion_length=512/1024；或对 truncated vs non-truncated 分析 reward distribution\"\n        assigned_to: agent\n        status: open\n\n  - id: REV-2\n    summary: \"CRAFT/Latent-GRPO Related Work 深度不足\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 3\n        reviewers: []\n        note: \"本轮未单独提及。可能已通过 Wu & Tang 讨论部分覆盖。\"\n    action_items:\n      - round: 2\n        action: \"确认 Latent-GRPO 命名来源或改用原文名称\"\n        assigned_to: agent+paper_agent\n        status: queued\n\n  - id: R2-MF4\n    summary: \"正文超 8 页限制\"\n    category: format\n    severity: critical\n    status: open\n    first_raised_round: 2\n    last_seen_round: 3\n    mentions:\n      - round: 2\n        reviewers: [visual_check]\n        note: \"Conclusion 从 page 9 开始。\"\n      - round: 3\n        reviewers: []\n        note: \"本轮 Reviewer 未直接提及，但视觉审查显示论文仍存在排版密度问题。需确认当前版本是否在 8 页内。\"\n    action_items:\n      - round: 3\n        action: \"确认当前版本正文是否在 8 页限制内；如未达标，继续压缩\"\n        assigned_to: paper_agent\n        status: open\n\n  - id: R2-SF8\n    summary: \"Wu & Tang (2026) 对比论证缺乏定量支撑\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 2\n    last_seen_round: 3\n    mentions:\n      - round: 2\n        reviewers: [2]\n        note: \"R2 首提。representation directions 在 GRPO 中成功，与本文 negative result 对比。\"\n      - round: 3\n        reviewers: [1, 2]\n        note: \"R2-W1 [AGREE by R1]：'geometric separability' 论点完全定性。d_syc AUROC 0.827 已相当不错的可分性，为何不够？需要量化比较（如 class boundary 附近 density 重叠度）。\"\n    action_items:\n      - round: 3\n        action: \"补充定量分析：计算 d_syc 在 online 分布下 valid vs sycophantic 的 cosine 分布重叠度，与 Wu & Tang 场景对比\"\n        assigned_to: agent+paper_agent\n        status: open\n\n  - id: R2-SF5\n    summary: \"可复现性信息不足\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 2\n    last_seen_round: 3\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"GRPO 关键超参数未披露。\"\n      - round: 3\n        reviewers: []\n        note: \"Appendix A 现有 Table 5 包含超参数。R2 给 Reproducibility 4/5。相比 Round 2 有改善，但仍需确认代码/数据可用性声明��\"\n    action_items:\n      - round: 3\n        action: \"确认 Reproducibility section 声明完整性\"\n        assigned_to: paper_agent\n        status: open\n\n  - id: R1-m2\n    summary: \"SycophancyScore harmonic mean 选择未充分 justify\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 3\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"降级为 info。\"\n      - round: 3\n        reviewers: [1, 2]\n        note: \"R1-W2/R2-Minor-2 均再次提及。R2 补充：harmonic mean 当 ToF=0 时自动归零可能掩盖部分改善（mask effect）。升级为 warning。\"\n    action_items:\n      - round: 3\n        action: \"§2.5 justify harmonic mean 选择（引用 F-score 类比）；补报 ToF/NoF 独立数值和 confidence interval\"\n        assigned_to: paper_agent\n        status: open\n\n  # === NEW ROUND 3 ISSUES ===\n\n  - id: R3-N1\n    summary: \"GRPO group_size=2 严重偏离标准实践（标准 8-64），构成致命替代解释\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"R1 首提，R2 强烈同意。group_size=2 导致 advantage 估计方差极大，无法区分 'd_syc 不可用' 和 'GRPO 优化器因 group_size 不足无法提取微弱信号'。可能也是 probe reward trap (ToF→0) 的直接原因。两位共识为最严重的新发��。\"\n    action_items:\n      - round: 3\n        action: \"补充 group_size={8, 16} 的消融实验隔离 reward signal quality 与 optimizer 配置效应\"\n        assigned_to: agent\n        status: open\n\n  - id: R3-W1\n    summary: \"discriminability ≠ reward utility 泛化声明超出单一 case study 证据\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"R2-W2 [AGREE by R1]：原则仅在 sycophancy + GRPO + 两个 8B 模型上验证。§8 泛化到其他 behavioral attributes 是 speculative。\"\n    action_items:\n      - round: 3\n        action: \"表述改为 hypothesis；或补充一个 pilot experiment（如 hallucination direction 作为 GRPO reward）\"\n        assigned_to: paper_agent\n        status: open\n\n  - id: R3-W2\n    summary: \"§6 cross-seed rank correlation 统计描述可能有误（2 seeds 无法得 ρ≈0.33）\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [2]\n        note: \"R2 在交叉回应中指出：从 2 个 seed 计算 Spearman rank correlation 只能取 +1 或 -1，不可能得到 0.33。可能是在 time-step level 而非 seed level 计算，但论文未说明。\"\n    action_items:\n      - round: 3\n        action: \"明确说明 rank correlation 的计算方式（跨 time-step 还是跨 seed）\"\n        assigned_to: paper_agent\n        status: open"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "contrastive_entrain_calib",
    "issues_yaml": "issues:\n  # === ROUND 1-2 ISSUES (UPDATED FOR ROUND 3) ===\n\n  - id: R1-N1\n    summary: \"Fisher exact test 将非独立 checkpoints 当独立样本，p<0.0001 不可信\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 首提，R2 完全同意。\"\n      - round: 2\n        reviewers: []\n        note: \"本轮未提及。论文已移除 Fisher p 值。已修复。\"\n      - round: 3\n        reviewers: []\n        note: \"本轮未提及，确认已修复。\"\n    resolution: \"论文已移除所有 Fisher p 值，改用描述���统计。\"\n    resolution_round: 2\n\n  - id: R2-N1\n    summary: \"遗漏 Papadatos & Freedman (2024) probe penalty 成功案例\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 3\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"必须讨论 probe penalty vs probe reward 的关键差异。\"\n      - round: 2\n        reviewers: [2]\n        note: \"R2 将其列为论文优势——对比分析已充分。\"\n      - round: 3\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 均列为论文优势之一（inference-time vs training-time 对比精到）。确认已解决。\"\n    resolution: \"§7 充分讨论，Round 2-3 均被列为论文优势。\"\n    resolution_round: 2\n\n  - id: R2-N2\n    summary: \"references.bib 多条引用严重不完整\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"ACT 作者为 Unknown，6 条仅 et al.\"\n      - round: 3\n        reviewers: []\n        note: \"本轮未提及，确认已修复。\"\n    resolution: \"Agent 已补全所有 bib entry。\"\n    resolution_round: 2\n\n  - id: R1-N2\n    summary: \"ACT 正面结果仅基于单 seed 完整评估（seed 2 仍 ongoing）\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 3\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"n=1 seed 不足以建立方法有效性。\"\n      - round: 2\n        reviewers: [1, 2]\n        note: \"Table 4 脚注仍显示部分 checkpoints。\"\n      - round: 3\n        reviewers: [1, 2]\n        note: \"Table 4 脚注 ‡ 显示 4/16。视觉审查也标记 ongoing 数据给人 work-in-progress 印象。R1 列为 N3，R2 列为 W4。\"\n    action_items:\n      - round: 3\n        action: \"完成 ACT seed 2 全部 16 checkpoints 评估，或降级为 preliminary evidence\"\n        assigned_to: agent\n        status: open\n\n  - id: R1-N3\n    summary: \"ACT vs GRPO 对比存在多维 confound，C3 不应作为 contribution\"\n    category: framing\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 3\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"论文 framing 为 'd_syc fails' 但证据仅支持 'sparse scalar d_syc reward fails in GRPO'。\"\n      - round: 2\n        reviewers: [1, 2]\n        note: \"§6 因果措辞仍过强。\"\n      - round: 3\n        reviewers: [1, 2]\n        note: \"R2-N2 [AGREE by R1]：C3 将 confounded observation 提升为 contribution，逻辑矛盾——§6 承认无法归因但 C3 仍用因果语言。两位 Reviewer 共识此为 critical。\"\n    action_items:\n      - round: 3\n        action: \"C3 从 contribution 降格为 observation/hypothesis；移除因果语言；明确列出 5+ confounding factors\"\n        assigned_to: paper_agent\n        status: open\n\n  - id: R1-W2\n    summary: \"标题和 claims scope 过于宽泛——仅测试 GRPO 但泛化到 Scalar RL Rewards\"\n    category: framing\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 3\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"DPO/PPO 未测试。\"\n      - round: 2\n        reviewers: [1, 2]\n        note: \"标题已改但 §6 仍声称 PPO/RLOO 泛化。\"\n      - round: 3\n        reviewers: [1, 2]\n        note: \"R2-N1 [AGREE by R1]：标题 'Scalar RL Rewards' 暗示对所有 RL 的普遍结论，但实验只有 GRPO。§8 自己承认 PPO/RLOO 是 open question，与标题矛盾。两位共识为 critical。\"\n    action_items:\n      - round: 3\n        action: \"标题改为 '...as GRPO Rewards' 或 '...as Scalar Per-Completion Rewards: Evidence from GRPO'；或补充 PPO/REINFORCE 实验\"\n        assigned_to: paper_agent\n        status: open\n\n  - id: R1-W1\n    summary: \"超参数 w1 仅测试 0.25/0.40 两个值 + multi-layer aggregation 未探索\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 3\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"R1 首提。\"\n      - round: 2\n        reviewers: [1, 2]\n        note: \"再次列为 Should-Fix。\"\n      - round: 3\n        reviewers: [1, 2]\n        note: \"R1-N4 部分 [REBUT by R2]：概念论证部分缓解 MLP 变体的必要性，但 w₁ 搜索范围和 multi-layer aggregation 仍为有效批评。R2 建议从 critical 降为 warning。\"\n    action_items:\n      - round: 3\n        action: \"扩展 w₁ 到 {0.1, 0.25, 0.4, 0.6, 0.8}；讨论 multi-layer aggregation 的 potential\"\n        assigned_to: paper_agent\n        status: open\n\n  - id: R1-W3\n    summary: \"AUROC ±值来自 5-fold CV std，不是正式 CI\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 3\n        reviewers: []\n        note: \"本轮未提及，论文已标注 '5-fold CV σ=0.028'。确认已修复。\"\n    resolution: \"全文已标注 5-fold CV std。\"\n    resolution_round: 2\n\n  - id: R1-W4\n    summary: \"Contrastive pairs 质量控制不足——evidence strength 标注无 IAA\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 3\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"未说明 pairs 构建方法。\"\n      - round: 2\n        reviewers: [1, 2]\n        note: \"构建方法已描述但 evidence strength 三级标注仍缺 IAA。\"\n      - round: 3\n        reviewers: [1, 2]\n        note: \"R1-W3 [AGREE by R2]：GPT-4.1 生成 + automated validation 不等于内容正确性验证，需人工验证 subset。\"\n    action_items:\n      - round: 3\n        action: \"至少对一个 subset 进行人工验证并报告 agreement rate；或在 Limitations 显式承认\"\n        assigned_to: paper_agent\n        status: open\n\n  - id: R1-W5\n    summary: \"所有 RL/SFT 训练仅在 Qwen3-8B 上进行\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 3\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"经验性 claim 需限定范围。\"\n      - round: 3\n        reviewers: [1, 2]\n        note: \"R2-W4 [AGREE by R1]：Llama-3-8B 仅做了 discriminability 验证。两位共识实验规模偏小。\"\n    action_items:\n      - round: 3\n        action: \"全文限定为 'In experiments on Qwen3-8B' case study\"\n        assigned_to: paper_agent\n        status: open\n\n  - id: R1-W6\n    summary: \"Cross-seed 分析仅 2 个 seed，负面结论证据标准不足\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 3\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"建议 ≥3 seeds。\"\n      - round: 3\n        reviewers: [1, 2]\n        note: \"R1-N3 [AGREE by R2]：2 seeds 无法排除某 seed 成功的可能。R2 补充：SYCONSCORE harmonic mean 对零值极敏感，全部为零可能是指标 artifact。升级为 critical。\"\n    action_items:\n      - round: 3\n        action: \"增加到 3-5 seeds 并报告 mean ± std；或将结论限定为 observational\"\n        assigned_to: agent\n        status: open\n\n  - id: R2-W2\n    summary: \"Process Reward Models (SMART) 讨论不足\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 3\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"supervision density hypothesis 直接预测 SMART 应部分成功。\"\n      - round: 3\n        reviewers: [1, 2]\n        note: \"R2-W3 [AGREE by R1]：SMART per-step reward 是 per-completion 和 per-token 之间的中间形态，与论文核心发现直接相关，应深入讨论。\"\n    action_items:\n      - round: 3\n        action: \"§7 增加 1-2 句分析 SMART per-step reward 如何 inform supervision granularity 论点\"\n        assigned_to: paper_agent\n        status: open\n\n  - id: R2-W3\n    summary: \"Conclusion overclaiming ('any alignment effort')\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"通过 R2-W2 覆盖：discriminability ≠ utility 泛化声明超出单一 case study 证据。\"\n    action_items:\n      - round: 3\n        action: \"§8 表述改为 'our results suggest' / 'we hypothesize'，避免断言性表述\"\n        assigned_to: paper_agent\n        status: open\n\n  - id: REV-1\n    summary: \"80-84% truncation rate (max_completion_length=256) 影响结果有效性\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 3\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"Appendix A 已披露。建议测试 512。\"\n      - round: 3\n        reviewers: [1, 2]\n        note: \"R1-N2 [AGREE by R2]：严重升级——truncation 可能是 probe reward trap 的直接原因。reward 在 truncated output 上计算，可能不反映完整响应的 sycophantic 倾向。R2 补充 truncation 导致 reward non-stationarity 加剧。两位共识升级为 critical。\"\n    action_items:\n      - round: 3\n        action: \"至少一个 config 测试 max_completion_length=512/1024；或对 truncated vs non-truncated 分析 reward distribution\"\n        assigned_to: agent\n        status: open\n\n  - id: REV-2\n    summary: \"CRAFT/Latent-GRPO Related Work 深度不足\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 3\n        reviewers: []\n        note: \"本轮未单独提及。可能已通过 Wu & Tang 讨论部分覆盖。\"\n    action_items:\n      - round: 2\n        action: \"确认 Latent-GRPO 命名来源或改用原文名称\"\n        assigned_to: agent+paper_agent\n        status: queued\n\n  - id: R2-MF4\n    summary: \"正文超 8 页限制\"\n    category: format\n    severity: critical\n    status: open\n    first_raised_round: 2\n    last_seen_round: 3\n    mentions:\n      - round: 2\n        reviewers: [visual_check]\n        note: \"Conclusion 从 page 9 开始。\"\n      - round: 3\n        reviewers: []\n        note: \"本轮 Reviewer 未直接提及，但视觉审查显示论文仍存在排版密度问题。需确认当前版本是否在 8 页内。\"\n    action_items:\n      - round: 3\n        action: \"确认当前版本正文是否在 8 页限制内；如未达标，继续压缩\"\n        assigned_to: paper_agent\n        status: open\n\n  - id: R2-SF8\n    summary: \"Wu & Tang (2026) 对比论证缺乏定量支撑\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 2\n    last_seen_round: 3\n    mentions:\n      - round: 2\n        reviewers: [2]\n        note: \"R2 首提。representation directions 在 GRPO 中成功，与本文 negative result 对比。\"\n      - round: 3\n        reviewers: [1, 2]\n        note: \"R2-W1 [AGREE by R1]：'geometric separability' 论点完全定性。d_syc AUROC 0.827 已相当不错的可分性，为何不够？需要量化比较（如 class boundary 附近 density 重叠度）。\"\n    action_items:\n      - round: 3\n        action: \"补充定量分析：计算 d_syc 在 online 分布下 valid vs sycophantic 的 cosine 分布重叠度，与 Wu & Tang 场景对比\"\n        assigned_to: agent+paper_agent\n        status: open\n\n  - id: R2-SF5\n    summary: \"可复现性信息不足\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 2\n    last_seen_round: 3\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"GRPO 关键超参数未披露。\"\n      - round: 3\n        reviewers: []\n        note: \"Appendix A 现有 Table 5 包含超参数。R2 给 Reproducibility 4/5。相比 Round 2 有改善，但仍需确认代码/数据可用性声明��\"\n    action_items:\n      - round: 3\n        action: \"确认 Reproducibility section 声明完整性\"\n        assigned_to: paper_agent\n        status: open\n\n  - id: R1-m2\n    summary: \"SycophancyScore harmonic mean 选择未充分 justify\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 3\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"降级为 info。\"\n      - round: 3\n        reviewers: [1, 2]\n        note: \"R1-W2/R2-Minor-2 均再次提及。R2 补充：harmonic mean 当 ToF=0 时自动归零可能掩盖部分改善（mask effect）。升级为 warning。\"\n    action_items:\n      - round: 3\n        action: \"§2.5 justify harmonic mean 选择（引用 F-score 类比）；补报 ToF/NoF 独立数值和 confidence interval\"\n        assigned_to: paper_agent\n        status: open\n\n  # === NEW ROUND 3 ISSUES ===\n\n  - id: R3-N1\n    summary: \"GRPO group_size=2 严重偏离标准实践（标准 8-64），构成致命替代解释\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"R1 首提，R2 强烈同意。group_size=2 导致 advantage 估计方差极大，无法区分 'd_syc 不可用' 和 'GRPO 优化器因 group_size 不足无法提取微弱信号'。可能也是 probe reward trap (ToF→0) 的直接原因。两位共识为最严重的新发��。\"\n    action_items:\n      - round: 3\n        action: \"补充 group_size={8, 16} 的消融实验隔离 reward signal quality 与 optimizer 配置效应\"\n        assigned_to: agent\n        status: open\n\n  - id: R3-W1\n    summary: \"discriminability ≠ reward utility 泛化声明超出单一 case study 证据\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"R2-W2 [AGREE by R1]：原则仅在 sycophancy + GRPO + 两个 8B 模型上验证。§8 泛化到其他 behavioral attributes 是 speculative。\"\n    action_items:\n      - round: 3\n        action: \"表述改为 hypothesis；或补充一个 pilot experiment（如 hallucination direction 作为 GRPO reward）\"\n        assigned_to: paper_agent\n        status: open\n\n  - id: R3-W2\n    summary: \"§6 cross-seed rank correlation 统计描述可能有误（2 seeds 无法得 ρ≈0.33）\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [2]\n        note: \"R2 在交叉回应中指出：从 2 个 seed 计算 Spearman rank correlation 只能取 +1 或 -1，不可能得到 0.33。可能是在 time-step level 而非 seed level 计算，但论文未说明。\"\n    action_items:\n      - round: 3\n        action: \"明确说明 rank correlation 的计算方式（跨 time-step 还是跨 seed）\"\n        assigned_to: paper_agent\n        status: open"
  }
}
```

</details>

---


### Tool result

_source line 271 · 2026-05-22T12:54:00.902461+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_issues.yaml\", \"bytes\": 12945}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 272 · 2026-05-22T12:56:26.467447+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "contrastive_entrain_calib",
  "report": "# Round 3 审稿报告\n\n**论文**: *Discriminability Without Utility: Why Sycophancy Directions Fail as Scalar RL Rewards*\n**Venue**: EMNLP 2026 (ARR May cycle, deadline 2026-05-25)\n**审稿模式**: Fresh（重新审稿）\n**Reviewer 编排**: 2 人（R1: 方法严谨性 + 实验有效性；R2: 新颖性 + framing 完整性）\n**轮次**: 1 轮初审 + 1 轮交叉回应（关键问题达成共识，无需第二轮）\n\n---\n\n## Summary\n\n论文提取了 contrastive sycophancy direction (d_syc)，在 Qwen3-8B (AUROC 0.827) 和 Llama-3-8B (AUROC 0.779) 上验证了其 discriminability，然后测试了三种将 d_syc 转化为 GRPO reward 的方法（cosine projection 4 变体、binary probe、continuous probe）以及 R3-only GRPO ablation 和 ACT baseline。所有 GRPO formulations 在 Qwen3-8B 上均失败。论文提出\"discriminability ≠ reward utility\"的概念框架解释失败原因。\n\n---\n\n## Strengths\n\n**S1** [共识] 研究问题重要且及时——representation engineering → RL reward 是社区自然关注的方向，系统验证其失败模式有明确价值。\n\n**S2** [共识] Probe reward trap (C2) 是独立有价值的新颖发现——behavioral death 先于 distributional collapse 的 1,300-step 时序分析（Figure 2, Table 3）提供了 RLHF 失败模式的有用 characterization，对 practitioners 有直接实践警示。\n\n**S3** [共识] 跨模型验证增强可信度——Qwen3-8B 和 Llama-3-8B 两个架构上 d_syc 的一致结果（Table 1）排除了 model-specific artifact 的解释。\n\n**S4** [共识] 与 Papadatos & Freedman (2024) 的对比分析精到——同一 probe 在 inference-time (Best-of-N) 成功但 training-time (GRPO reward) 失败，精准定位了\"inside vs outside optimization loop\"的关键区分（§7）。这是论文最有洞察力的分析之一。\n\n**S5** [共识] d_syc 方向本身验证扎实——5-fold CV、evidence strength 分层、per-layer AUROC 分析、recalibration 机制和 probe ablation 显示了系统性 methodology。\n\n**S6** [共识] 失败诊断链（gate saturation → gradient vanishing → mode collapse → behavioral death → stubbornness trap）对 practitioners 有参考价值，Stubbornness taxonomy (Appendix B) 的三种 failure mode 提供了有价值的定性补充。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**MF1** [critical, 共识] **GRPO group_size=2 严重偏离标准实践，构成致命替代解释**\n- Table 5 (Appendix A) 显示 group_size=2，而标准 GRPO（Shao et al., 2024）使用 64，后续文献下限为 8-16。group_size=2 退化为噪声极高的 pairwise 对比，advantage 估计方差极大。\n- 无法区分两种解释：(a) d_syc reward 信号本质不可用；(b) d_syc 信号微弱但可用，group_size=2 的 GRPO 无法提取有效梯度。解释 (b) 未被排除。\n- R1 首提，R2 交叉回应中强烈同意并补充：这也可能是 probe reward trap (ToF→0 at step 500) 的直接原因——不是 probe 的 structural failure，而是 group_size=2 导致的 optimization instability。\n- **建议**: 补充 group_size ∈ {8, 16} 消融实验。\n\n**MF2** [critical, 共识] **max_completion_length=256 导致 80-84% truncation，可能是 reward failure 的直接原因**\n- 3-turn 对话 256 tokens 远不足以生成完整响应。reward 在 truncated output 上计算，cosine/probe 可能不反映完整响应的 sycophantic 倾向。\n- R2 补充：truncation 还导致 RL 训练中 reward 的 non-stationarity 远超正常水平，与 Figure 3 的 stochastic oscillation 可能有因果关系。\n- 论文的\"shared across conditions\"辩护只保证公式间相对比较有效，不支持 d_syc 本质失败的绝对声明。\n- **建议**: 至少一个 config 测试 max_completion_length=512/1024。\n\n**MF3** [critical, 共识] **标题和 claims 范围显著超出实验证据**\n- 标题\"Sycophancy Directions Fail as Scalar RL Rewards\"暗示对所有 scalar RL rewards 的普遍结论，但仅测试 GRPO。PPO、RLOO、REINFORCE、DPO 均未测试。\n- §8 自己承认\"whether they exhibit similar failures remains an open question\"，与标题的普遍性声明直接矛盾。\n- C1 用了\"Every tested GRPO formulation\"的限定，比标题更谨慎——标题与正文 contributions 之间存在 scope 不一致。\n- **建议**: 标题改为\"…as GRPO Rewards\"或\"…as Scalar Per-Completion Rewards: Evidence from GRPO\"；或补充 PPO/REINFORCE 实验。\n\n**MF4** [critical, 共识] **C3 将 confounded observation 包装为 contribution**\n- C3 声称\"sparse RL reward failed to convey the valid/invalid distinction\"，核心证据来自 ACT 成功而 GRPO 失败。但 ACT 与 GRPO 至少在 5 个维度上不同：训练范式（SFT vs RL）、监督粒度（per-token vs per-completion）、labeled pairs 使用、loss function（L2 vs reward maximization）、LoRA capacity (~1.75× 参数差异）。\n- §6 承认\"this gap is an observational finding, not a controlled comparison\"，但 C3 仍以 contribution 形式呈现——存在逻辑矛盾。\n- R1 最初列为 Should-Fix，交叉回应后同意 R2 的 critical 级别判断。\n- **建议**: C3 降格为 observation/hypothesis，明确列出所有 confounding factors，移除因果语言。\n\n**MF5** [critical, 共识] **仅 2 random seeds，负面结论证据标准不足**\n- RL 训练高方差，2 seeds 无法提供有意义方差估计。\"4/26 checkpoints exceed vanilla\"的可靠性完全依赖 2 seeds 的代表性。\n- R2 补充：SYCONSCORE 的 harmonic mean 当 ToF 或 NoF 为 0 时自动归零，因此 Table 4 中全部为零可能是指标设计的 artifact（对零值极端敏感）而非 truly consistent failure。ToF/NoF 原始值的 variance 未报告。\n- 负面结论证据标准应高于正面结论——如果存在 5% 概率某 seed 成功，结论即被推翻。\n- **建议**: 增加到 3-5 seeds 并报告 mean ± std。\n\n### Should-Fix（影响评分但不一票否决）\n\n**SF1** [warning, 共识] **Wu & Tang (2026) \"geometric separability\"论点缺乏定量支撑**\n- §6 定性论证 d_syc 不够 separable，但未量化。d_syc AUROC 已达 0.827，\"separability 不足\"并非不证自明。\n- 需要定量分析：如 d_syc 在 online 分布下 valid vs sycophantic 的 cosine 分布重叠度，与 Wu & Tang 场景对比。\n\n**SF2** [warning, 共识] **\"Discriminability ≠ Reward Utility\"泛化声明超出证据**\n- 该原则仅在 sycophancy + GRPO + 两个 8B 模型上验证。§8 泛化到其他 behavioral attributes 是 speculative。\n- 建议表述改为\"our results suggest\"/\"we hypothesize\"。\n\n**SF3** [warning, 共识] **SMART (Beigi et al., 2025) 讨论过于简略**\n- SMART 的 per-step process reward 是 per-completion（GRPO）和 per-token（ACT）之间的中间监督密度，与论文核心发现直接相关。\n- 如 SMART 部分成功，为\"密度是关键因素\"提供证据；如也失败，加强\"问题在 d_syc 本身\"的论点。无论如何应深入讨论。\n\n**SF4** [warning, 共识] **Reward 设计空间探索偏窄**\n- w₁ 仅测试 0.25/0.40，间距仅 0.15。w₁=0.25 时 d_syc 仅贡献 ~8.3% reward 方差。\n- Multi-layer aggregation 未探索——Figure 1 显示不同层有不同信号，仅用 best single layer 可能丢失信息。\n- R2 部分反驳：概念论证（d_syc 不携带 valid/invalid 信息→MLP 也无法改善）有逻辑支撑，但 w₁ 范围和 multi-layer 批评仍有效。\n\n**SF5** [warning, 共识] **181 contrastive pairs 质量控制不足**\n- GPT-4.1 生成 + automated style validation，无人工验证/IAA。Evidence strength 三级标注为单一标注者。\n- 需至少对一个 subset 人工验证并报告 agreement rate。\n\n**SF6** [warning, 共识] **SYCONSCORE harmonic mean 选择未 justify，可能掩盖部分改善**\n- harmonic mean 当 ToF=0 时自动归零，可能 mask 部分 ToF 改善。论文应 justify 选择（引用 F-score 类比）并补报 ToF/NoF 独立数值和 confidence interval。\n- 补报 arithmetic mean 作为 sensitivity analysis。\n\n### Minor Issues\n\n- §6 cross-seed rank correlation \"ρ≈0.33 (n.s.)\" 统计描述可能有误——2 个 seed 的 Spearman rank correlation 只能取 +1/-1，需明确计算方式（R2 交叉回应识别）\n- Table 2 \"mode collapse\"/\"gate saturation\" 缺操作性定义\n- Figure 1 y 轴标签未在 caption 中解释\n- §6 \"semantic gap\" 是核心概念但未形式化——可考虑简单形式化\n- Appendix B stubbornness taxonomy 仅 100 条、无 inter-rater reliability\n- Abstract 信息密度极高（~250 words）——R1 认为在 *ACL 可接受范围，R2 建议精简（轻微分歧，recorded）\n\n---\n\n## Reviewer Consensus\n\n两位 Reviewer 在以下关键问题上完全一致 [AGREE]：\n\n1. **GRPO group_size=2 + 80-84% truncation 构成致命 confounds** (MF1+MF2)：无法区分\"d_syc 本质失败\"和\"GRPO 优化配置不足\"两种解释。这是本轮审稿识别到的**最核心问题**。\n2. **标题/claims overclaiming** (MF3)：仅测试 GRPO 但标题声称 Scalar RL Rewards。\n3. **C3 confound → contribution 的逻辑矛盾** (MF4)：§6 承认无法归因但 C3 仍用因果语言。\n4. **2 seeds 不足以支撑负面结论** (MF5)：证据标准应高于正面结论。\n5. **Probe reward trap (C2) 是最有独立价值的发现**：但其 failure 归因可能受 MF1/MF2 影响。\n6. **Papadatos & Freedman 对比分析是论文最有洞察力的部分**。\n\n---\n\n## Reviewer Divergence\n\n仅一项轻微分歧（已在交叉回应中解决）：\n\n- **R1-N4 (Reward 设计空间探索) 的 severity**：R1 列为 critical，R2 部分 [REBUT]——论文的概念性分析（d_syc 不携带 valid/invalid 信息→更复杂变换也无效）部分缓解了 MLP/non-linear 变体的必要性，但 w₁ 搜索范围和 multi-layer aggregation 批评有效。R2 建议降为 Should-Fix。→ 最终采纳 R2 判断，列为 SF4。\n\n---\n\n## Questions\n\n1. group_size=2 的选择理由是什么？是否有预实验表明更大 group_size 在此 setting 下计算不可行？\n2. 是否有对 truncated vs non-truncated samples 的 reward 分布分析？\n3. §6 的 cross-seed rank correlation \"ρ≈0.33\" 具体是如何计算的？（2 data points 无法产生此值）\n4. ACT 和 GRPO 的 LoRA 配置差异（4 vs 7 modules, ~1.75× 参数）是否经过消融验证？\n5. 是否考虑过将 d_syc 用于 DPO preference ranking 而非 scalar GRPO reward？\n\n---\n\n## Missing References\n\n- 论文已涵盖主要相关工作（Papadatos & Freedman, Wu & Tang, SMART, CRAFT, Latent-GRPO）。\n- 建议深化 SMART 讨论（SF3）和 Wu & Tang 定量对比（SF1）。\n- DPO/KTO 在 sycophancy mitigation 中的应用可考虑在 §7 或 §8 简要讨论。\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未请求。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成（2 warnings, 4 info）：\n\n**Warnings:**\n- 前 3 页无 figure/table，审稿人翻到 page 4 才看到首个视觉锚点——建议 page 2 前插入概念总览图或核心结果 teaser figure\n- Appendix B 仅占页面约 25%，剩余 75% 空白——建议与 Appendix A 合并或扩充内容\n\n**Info:**\n- Table 3（probe trajectory）列数多，单栏排版可能偏小，建议 table* 全宽排版\n- Table 4 ACT (seed 2) 标注\"ongoing: 4/16 ckpts evaluated\"——在正式投稿中给人 work-in-progress 印象\n- 全文 3 个 figure 均为折线图，缺少概念性图示（framework overview）\n- Figure 3 彩色折线区分度有限，建议辅以不同 line style 和 marker shape\n\n---\n\n## Overall Assessment\n\n**Overall Score: 2.5 (Borderline Findings)**\n\n**评分理由：**\n论文提出了有价值的概念框架（discriminability ≠ reward utility），probe reward trap 的时序分析（C2）是新颖的实证发现，d_syc 方向的 cross-model 验证扎实。然而，作为一篇负面结果论文（negative result paper），其核心结论受到多个严重的未控制 confounds 削弱：\n\n1. **GRPO group_size=2** 和 **80-84% response truncation** 构成致命替代解释——无法区分\"d_syc reward 本质不可用\"和\"GRPO 优化配置不当\"。\n2. **标题和 C3 overclaiming**——仅测试 GRPO 但声称对 Scalar RL Rewards 的普遍结论；confounded ACT vs GRPO 对比被包装为 contribution。\n3. **仅 2 seeds** 不足以支撑负面结论的证据标准。\n\n论文有潜力达到 Findings 水准，但需要补充 **group_size 和 completion_length 的消融实验**以排除 optimizer 配置这一强替代解释，并需要**收窄 claims scope**使其与实验证据匹配。\n\n**两位 Reviewer 均给出 2.5 分（Borderline Findings），交叉回应后完全一致。**\n\n**置信度: 4/5**（两位 Reviewer 均熟悉 RL alignment、representation engineering 和 sycophancy 文献）\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- C1 的\"Every tested GRPO formulation\"限定词比标题更谨慎——标题应与正文对齐\n- C3 的因果语言与 §6 的 observational disclaimer 矛盾——统一措辞\n- 数字密度高（AUROC, CV σ, checkpoint counts），建议简化引言中的重复数字\n\n### §2 Experimental Framework\n- group_size=2 和 max_completion_length=256 应在正文中 justify，而非仅在 Appendix 提及\n- w₁ 选择描述为\"diagnostic-driven iteration\"但实质是仅 2 个值——需更诚实的措辞\n- 181 pairs 的 GPT-4.1 生成流程已描述，但缺少内容正确性的人工验证\n\n### §3 Direction Discriminability\n- 最扎实的章节——5-fold CV、cross-model、evidence strength gradient 验证充分\n- 建议补充 post-attention vs post-MLP residual stream 的明确说明\n\n### §4 Cosine R1\n- 失败诊断链逻辑清晰，但 failure mode 术语（gate saturation, mode collapse）需操作性定义\n- Table 2 cosine gap \"averages only 0.098\"——是否受 group_size=2 的高方差采样影响？\n\n### §5 Probe Reward Trap\n- 最有价值的实证章节——但 behavioral death 的归因需排除 truncation artifact\n- \"entropy remained healthy\"应给具体数值范围\n- 如补充 group_size=8 实验后 trap 仍存在，则 C2 的独立价值大幅增强\n\n### §6 Analysis\n- \"unified root cause\"叙事依赖 ACT 对比——在 confounds 未解决前，这个归因不够稳固\n- cross-seed rank correlation \"ρ≈0.33\" 统计描述需修正\n- \"semantic gap\"概念有价值但未形式化\n\n### §7 Related Work\n- Papadatos & Freedman 对比是亮点\n- SMART 讨论需扩展——作为中间监督密度案例与核心论点直接相关\n- Wu & Tang 对比需定量支撑\n\n### §8 Conclusion\n- 泛化声明应降级为 hypothesis\n- \"discriminability ≠ utility\"原则在单一 case study 基础上需更谨慎表述\n\n### Limitations\n- 覆盖了主要限制但措辞可更强——特别是 group_size=2 和 truncation 应显式列出\n- \"Other RL algorithms (PPO, DPO) may interact differently\"应从 Limitations 提升到主文的 scope qualification",
  "reviewer_ids_acknowledged": "[\"1\", \"2\"]",
  "cross_response_reviewer_ids": "[\"1\", \"2\"]",
  "overall_score": "2.5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "project": "contrastive_entrain_calib",
    "report": "# Round 3 审稿报告\n\n**论文**: *Discriminability Without Utility: Why Sycophancy Directions Fail as Scalar RL Rewards*\n**Venue**: EMNLP 2026 (ARR May cycle, deadline 2026-05-25)\n**审稿模式**: Fresh（重新审稿）\n**Reviewer 编排**: 2 人（R1: 方法严谨性 + 实验有效性；R2: 新颖性 + framing 完整性）\n**轮次**: 1 轮初审 + 1 轮交叉回应（关键问题达成共识，无需第二轮）\n\n---\n\n## Summary\n\n论文提取了 contrastive sycophancy direction (d_syc)，在 Qwen3-8B (AUROC 0.827) 和 Llama-3-8B (AUROC 0.779) 上验证了其 discriminability，然后测试了三种将 d_syc 转化为 GRPO reward 的方法（cosine projection 4 变体、binary probe、continuous probe）以及 R3-only GRPO ablation 和 ACT baseline。所有 GRPO formulations 在 Qwen3-8B 上均失败。论文提出\"discriminability ≠ reward utility\"的概念框架解释失败原因。\n\n---\n\n## Strengths\n\n**S1** [共识] 研究问题重要且及时——representation engineering → RL reward 是社区自然关注的方向，系统验证其失败模式有明确价值。\n\n**S2** [共识] Probe reward trap (C2) 是独立有价值的新颖发现——behavioral death 先于 distributional collapse 的 1,300-step 时序分析（Figure 2, Table 3）提供了 RLHF 失败模式的有用 characterization，对 practitioners 有直接实践警示。\n\n**S3** [共识] 跨模型验证增强可信度——Qwen3-8B 和 Llama-3-8B 两个架构上 d_syc 的一致结果（Table 1）排除了 model-specific artifact 的解释。\n\n**S4** [共识] 与 Papadatos & Freedman (2024) 的对比分析精到——同一 probe 在 inference-time (Best-of-N) 成功但 training-time (GRPO reward) 失败，精准定位了\"inside vs outside optimization loop\"的关键区分（§7）。这是论文最有洞察力的分析之一。\n\n**S5** [共识] d_syc 方向本身验证扎实——5-fold CV、evidence strength 分层、per-layer AUROC 分析、recalibration 机制和 probe ablation 显示了系统性 methodology。\n\n**S6** [共识] 失败诊断链（gate saturation → gradient vanishing → mode collapse → behavioral death → stubbornness trap）对 practitioners 有参考价值，Stubbornness taxonomy (Appendix B) 的三种 failure mode 提供了有价值的定性补充。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**MF1** [critical, 共识] **GRPO group_size=2 严重偏离标准实践，构成致命替代解释**\n- Table 5 (Appendix A) 显示 group_size=2，而标准 GRPO（Shao et al., 2024）使用 64，后续文献下限为 8-16。group_size=2 退化为噪声极高的 pairwise 对比，advantage 估计方差极大。\n- 无法区分两种解释：(a) d_syc reward 信号本质不可用；(b) d_syc 信号微弱但可用，group_size=2 的 GRPO 无法提取有效梯度。解释 (b) 未被排除。\n- R1 首提，R2 交叉回应中强烈同意并补充：这也可能是 probe reward trap (ToF→0 at step 500) 的直接原因——不是 probe 的 structural failure，而是 group_size=2 导致的 optimization instability。\n- **建议**: 补充 group_size ∈ {8, 16} 消融实验。\n\n**MF2** [critical, 共识] **max_completion_length=256 导致 80-84% truncation，可能是 reward failure 的直接原因**\n- 3-turn 对话 256 tokens 远不足以生成完整响应。reward 在 truncated output 上计算，cosine/probe 可能不反映完整响应的 sycophantic 倾向。\n- R2 补充：truncation 还导致 RL 训练中 reward 的 non-stationarity 远超正常水平，与 Figure 3 的 stochastic oscillation 可能有因果关系。\n- 论文的\"shared across conditions\"辩护只保证公式间相对比较有效，不支持 d_syc 本质失败的绝对声明。\n- **建议**: 至少一个 config 测试 max_completion_length=512/1024。\n\n**MF3** [critical, 共识] **标题和 claims 范围显著超出实验证据**\n- 标题\"Sycophancy Directions Fail as Scalar RL Rewards\"暗示对所有 scalar RL rewards 的普遍结论，但仅测试 GRPO。PPO、RLOO、REINFORCE、DPO 均未测试。\n- §8 自己承认\"whether they exhibit similar failures remains an open question\"，与标题的普遍性声明直接矛盾。\n- C1 用了\"Every tested GRPO formulation\"的限定，比标题更谨慎——标题与正文 contributions 之间存在 scope 不一致。\n- **建议**: 标题改为\"…as GRPO Rewards\"或\"…as Scalar Per-Completion Rewards: Evidence from GRPO\"；或补充 PPO/REINFORCE 实验。\n\n**MF4** [critical, 共识] **C3 将 confounded observation 包装为 contribution**\n- C3 声称\"sparse RL reward failed to convey the valid/invalid distinction\"，核心证据来自 ACT 成功而 GRPO 失败。但 ACT 与 GRPO 至少在 5 个维度上不同：训练范式（SFT vs RL）、监督粒度（per-token vs per-completion）、labeled pairs 使用、loss function（L2 vs reward maximization）、LoRA capacity (~1.75× 参数差异）。\n- §6 承认\"this gap is an observational finding, not a controlled comparison\"，但 C3 仍以 contribution 形式呈现——存在逻辑矛盾。\n- R1 最初列为 Should-Fix，交叉回应后同意 R2 的 critical 级别判断。\n- **建议**: C3 降格为 observation/hypothesis，明确列出所有 confounding factors，移除因果语言。\n\n**MF5** [critical, 共识] **仅 2 random seeds，负面结论证据标准不足**\n- RL 训练高方差，2 seeds 无法提供有意义方差估计。\"4/26 checkpoints exceed vanilla\"的可靠性完全依赖 2 seeds 的代表性。\n- R2 补充：SYCONSCORE 的 harmonic mean 当 ToF 或 NoF 为 0 时自动归零，因此 Table 4 中全部为零可能是指标设计的 artifact（对零值极端敏感）而非 truly consistent failure。ToF/NoF 原始值的 variance 未报告。\n- 负面结论证据标准应高于正面结论——如果存在 5% 概率某 seed 成功，结论即被推翻。\n- **建议**: 增加到 3-5 seeds 并报告 mean ± std。\n\n### Should-Fix（影响评分但不一票否决）\n\n**SF1** [warning, 共识] **Wu & Tang (2026) \"geometric separability\"论点缺乏定量支撑**\n- §6 定性论证 d_syc 不够 separable，但未量化。d_syc AUROC 已达 0.827，\"separability 不足\"并非不证自明。\n- 需要定量分析：如 d_syc 在 online 分布下 valid vs sycophantic 的 cosine 分布重叠度，与 Wu & Tang 场景对比。\n\n**SF2** [warning, 共识] **\"Discriminability ≠ Reward Utility\"泛化声明超出证据**\n- 该原则仅在 sycophancy + GRPO + 两个 8B 模型上验证。§8 泛化到其他 behavioral attributes 是 speculative。\n- 建议表述改为\"our results suggest\"/\"we hypothesize\"。\n\n**SF3** [warning, 共识] **SMART (Beigi et al., 2025) 讨论过于简略**\n- SMART 的 per-step process reward 是 per-completion（GRPO）和 per-token（ACT）之间的中间监督密度，与论文核心发现直接相关。\n- 如 SMART 部分成功，为\"密度是关键因素\"提供证据；如也失败，加强\"问题在 d_syc 本身\"的论点。无论如何应深入讨论。\n\n**SF4** [warning, 共识] **Reward 设计空间探索偏窄**\n- w₁ 仅测试 0.25/0.40，间距仅 0.15。w₁=0.25 时 d_syc 仅贡献 ~8.3% reward 方差。\n- Multi-layer aggregation 未探索——Figure 1 显示不同层有不同信号，仅用 best single layer 可能丢失信息。\n- R2 部分反驳：概念论证（d_syc 不携带 valid/invalid 信息→MLP 也无法改善）有逻辑支撑，但 w₁ 范围和 multi-layer 批评仍有效。\n\n**SF5** [warning, 共识] **181 contrastive pairs 质量控制不足**\n- GPT-4.1 生成 + automated style validation，无人工验证/IAA。Evidence strength 三级标注为单一标注者。\n- 需至少对一个 subset 人工验证并报告 agreement rate。\n\n**SF6** [warning, 共识] **SYCONSCORE harmonic mean 选择未 justify，可能掩盖部分改善**\n- harmonic mean 当 ToF=0 时自动归零，可能 mask 部分 ToF 改善。论文应 justify 选择（引用 F-score 类比）并补报 ToF/NoF 独立数值和 confidence interval。\n- 补报 arithmetic mean 作为 sensitivity analysis。\n\n### Minor Issues\n\n- §6 cross-seed rank correlation \"ρ≈0.33 (n.s.)\" 统计描述可能有误——2 个 seed 的 Spearman rank correlation 只能取 +1/-1，需明确计算方式（R2 交叉回应识别）\n- Table 2 \"mode collapse\"/\"gate saturation\" 缺操作性定义\n- Figure 1 y 轴标签未在 caption 中解释\n- §6 \"semantic gap\" 是核心概念但未形式化——可考虑简单形式化\n- Appendix B stubbornness taxonomy 仅 100 条、无 inter-rater reliability\n- Abstract 信息密度极高（~250 words）——R1 认为在 *ACL 可接受范围，R2 建议精简（轻微分歧，recorded）\n\n---\n\n## Reviewer Consensus\n\n两位 Reviewer 在以下关键问题上完全一致 [AGREE]：\n\n1. **GRPO group_size=2 + 80-84% truncation 构成致命 confounds** (MF1+MF2)：无法区分\"d_syc 本质失败\"和\"GRPO 优化配置不足\"两种解释。这是本轮审稿识别到的**最核心问题**。\n2. **标题/claims overclaiming** (MF3)：仅测试 GRPO 但标题声称 Scalar RL Rewards。\n3. **C3 confound → contribution 的逻辑矛盾** (MF4)：§6 承认无法归因但 C3 仍用因果语言。\n4. **2 seeds 不足以支撑负面结论** (MF5)：证据标准应高于正面结论。\n5. **Probe reward trap (C2) 是最有独立价值的发现**：但其 failure 归因可能受 MF1/MF2 影响。\n6. **Papadatos & Freedman 对比分析是论文最有洞察力的部分**。\n\n---\n\n## Reviewer Divergence\n\n仅一项轻微分歧（已在交叉回应中解决）：\n\n- **R1-N4 (Reward 设计空间探索) 的 severity**：R1 列为 critical，R2 部分 [REBUT]——论文的概念性分析（d_syc 不携带 valid/invalid 信息→更复杂变换也无效）部分缓解了 MLP/non-linear 变体的必要性，但 w₁ 搜索范围和 multi-layer aggregation 批评有效。R2 建议降为 Should-Fix。→ 最终采纳 R2 判断，列为 SF4。\n\n---\n\n## Questions\n\n1. group_size=2 的选择理由是什么？是否有预实验表明更大 group_size 在此 setting 下计算不可行？\n2. 是否有对 truncated vs non-truncated samples 的 reward 分布分析？\n3. §6 的 cross-seed rank correlation \"ρ≈0.33\" 具体是如何计算的？（2 data points 无法产生此值）\n4. ACT 和 GRPO 的 LoRA 配置差异（4 vs 7 modules, ~1.75× 参数）是否经过消融验证？\n5. 是否考虑过将 d_syc 用于 DPO preference ranking 而非 scalar GRPO reward？\n\n---\n\n## Missing References\n\n- 论文已涵盖主要相关工作（Papadatos & Freedman, Wu & Tang, SMART, CRAFT, Latent-GRPO）。\n- 建议深化 SMART 讨论（SF3）和 Wu & Tang 定量对比（SF1）。\n- DPO/KTO 在 sycophancy mitigation 中的应用可考虑在 §7 或 §8 简要讨论。\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未请求。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成（2 warnings, 4 info）：\n\n**Warnings:**\n- 前 3 页无 figure/table，审稿人翻到 page 4 才看到首个视觉锚点——建议 page 2 前插入概念总览图或核心结果 teaser figure\n- Appendix B 仅占页面约 25%，剩余 75% 空白——建议与 Appendix A 合并或扩充内容\n\n**Info:**\n- Table 3（probe trajectory）列数多，单栏排版可能偏小，建议 table* 全宽排版\n- Table 4 ACT (seed 2) 标注\"ongoing: 4/16 ckpts evaluated\"——在正式投稿中给人 work-in-progress 印象\n- 全文 3 个 figure 均为折线图，缺少概念性图示（framework overview）\n- Figure 3 彩色折线区分度有限，建议辅以不同 line style 和 marker shape\n\n---\n\n## Overall Assessment\n\n**Overall Score: 2.5 (Borderline Findings)**\n\n**评分理由：**\n论文提出了有价值的概念框架（discriminability ≠ reward utility），probe reward trap 的时序分析（C2）是新颖的实证发现，d_syc 方向的 cross-model 验证扎实。然而，作为一篇负面结果论文（negative result paper），其核心结论受到多个严重的未控制 confounds 削弱：\n\n1. **GRPO group_size=2** 和 **80-84% response truncation** 构成致命替代解释——无法区分\"d_syc reward 本质不可用\"和\"GRPO 优化配置不当\"。\n2. **标题和 C3 overclaiming**——仅测试 GRPO 但声称对 Scalar RL Rewards 的普遍结论；confounded ACT vs GRPO 对比被包装为 contribution。\n3. **仅 2 seeds** 不足以支撑负面结论的证据标准。\n\n论文有潜力达到 Findings 水准，但需要补充 **group_size 和 completion_length 的消融实验**以排除 optimizer 配置这一强替代解释，并需要**收窄 claims scope**使其与实验证据匹配。\n\n**两位 Reviewer 均给出 2.5 分（Borderline Findings），交叉回应后完全一致。**\n\n**置信度: 4/5**（两位 Reviewer 均熟悉 RL alignment、representation engineering 和 sycophancy 文献）\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- C1 的\"Every tested GRPO formulation\"限定词比标题更谨慎——标题应与正文对齐\n- C3 的因果语言与 §6 的 observational disclaimer 矛盾——统一措辞\n- 数字密度高（AUROC, CV σ, checkpoint counts），建议简化引言中的重复数字\n\n### §2 Experimental Framework\n- group_size=2 和 max_completion_length=256 应在正文中 justify，而非仅在 Appendix 提及\n- w₁ 选择描述为\"diagnostic-driven iteration\"但实质是仅 2 个值——需更诚实的措辞\n- 181 pairs 的 GPT-4.1 生成流程已描述，但缺少内容正确性的人工验证\n\n### §3 Direction Discriminability\n- 最扎实的章节——5-fold CV、cross-model、evidence strength gradient 验证充分\n- 建议补充 post-attention vs post-MLP residual stream 的明确说明\n\n### §4 Cosine R1\n- 失败诊断链逻辑清晰，但 failure mode 术语（gate saturation, mode collapse）需操作性定义\n- Table 2 cosine gap \"averages only 0.098\"——是否受 group_size=2 的高方差采样影响？\n\n### §5 Probe Reward Trap\n- 最有价值的实证章节——但 behavioral death 的归因需排除 truncation artifact\n- \"entropy remained healthy\"应给具体数值范围\n- 如补充 group_size=8 实验后 trap 仍存在，则 C2 的独立价值大幅增强\n\n### §6 Analysis\n- \"unified root cause\"叙事依赖 ACT 对比——在 confounds 未解决前，这个归因不够稳固\n- cross-seed rank correlation \"ρ≈0.33\" 统计描述需修正\n- \"semantic gap\"概念有价值但未形式化\n\n### §7 Related Work\n- Papadatos & Freedman 对比是亮点\n- SMART 讨论需扩展——作为中间监督密度案例与核心论点直接相关\n- Wu & Tang 对比需定量支撑\n\n### §8 Conclusion\n- 泛化声明应降级为 hypothesis\n- \"discriminability ≠ utility\"原则在单一 case study 基础上需更谨慎表述\n\n### Limitations\n- 覆盖了主要限制但措辞可更强——特别是 group_size=2 和 truncation 应显式列出\n- \"Other RL algorithms (PPO, DPO) may interact differently\"应从 Limitations 提升到主文的 scope qualification",
    "reviewer_ids_acknowledged": "[\"1\", \"2\"]",
    "cross_response_reviewer_ids": "[\"1\", \"2\"]",
    "overall_score": "2.5"
  }
}
```

</details>

---


### Tool result

_source line 273 · 2026-05-22T12:56:32.910731+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_c77a380fad2d0408ce92cd1170d46f6f:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 6443
}
```

</details>

---


### Assistant

_source line 274 · 2026-05-22T12:56:40.569068+00:00_

审稿报告已投递。

**审稿结论：Overall 2.5 (Borderline Findings)**

核心问题汇总：
1. **GRPO group_size=2 + 80-84% truncation** — 致命替代解释，无法���分"d_syc 不可用"和"优化配置不当"
2. **标题 overclaiming** — 仅测试 GRPO 但声称 Scalar RL Rewards 的普遍结论
3. **C3 confound 作为 contribution** — ACT vs GRPO 的 confounded comparison 不应以因果性 contribution 呈现
4. **仅 2 seeds** — 负面结论证据标准不足

论文有潜力达到 Findings 水准，需要补充 group_size/completion_length 消融实验并收窄 claims scope。Probe reward trap (C2) 和 Papadatos & Freedman 对比分析是独立有价值的发现。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director"
}
```

</details>

---


## Round 24

## Round 24

2 recorded events


### User

_source line 275 · 2026-05-22T12:56:43.153591+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。总结：

- R1 的 4 个 Must-Fix 中，我 **强烈同意 N1（group_size=2）、N2（80-84% truncation）、N3（2 seeds）**，**部分反驳 N4（reward 设计空间）**——论文的 conceptual argument 部分缓解了对 reward architecture 多样性的需求，但 w₁ 搜索范围和 multi-layer aggregation 的缺失是 valid concerns。
- R1 的 4 个 Should-Fix 全部同意。
- 关键发现：R1-N1 和 N2 是我首轮审稿中遗漏的重要 confounds，它们从根本上动摇了"失败源于 d_syc"的因果推断。据此将 Overall 从 3.0 下调至 **2.5（Borderline Findings）**。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 276 · 2026-05-22T12:58:54.420212+00:00_

审稿报告已投递至 Research Director。

**本轮审稿总结：**

- **Overall Score: 2.5 (Borderline Findings)**，两位 Reviewer 交叉回应后完全一致
- **5 个 Must-Fix**：(1) GRPO group_size=2 构成致命替代解释；(2) 80-84% truncation 可能是 reward failure 直接原因；(3) 标题/claims overclaiming；(4) C3 confounded observation 被包装为 contribution；(5) 仅 2 seeds 不足
- **核心问题**：无法区分"d_syc reward 本质不可用"和"GRPO 优化配置不当"——group_size=2 和 truncation 这两个 confounds 需要消融实验排除
- **主要优势**：probe reward trap (C2) 的时序分析有独立价值，Papadatos & Freedman 对比分析精到，d_syc 方向验证扎实

Issue Tracker 已同步更新至 `review_issues.yaml`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director"
}
```

</details>

---


## Round 25

## Round 25

72 recorded events


### User

_source line 277 · 2026-05-22T13:57:02.446138+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: contrastive_entrain_calib
- 论文路径: /home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: ARR May 2026
- 截止日期: 2026-05-25
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 278 · 2026-05-22T13:57:13.313268+00:00_

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
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 279 · 2026-05-22T13:57:13.364597+00:00_

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
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 280 · 2026-05-22T13:57:20.856174+00:00_

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
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
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

_source line 281 · 2026-05-22T13:57:20.910145+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "ToolSearch",
  "elapsed_ms": 53
}
```

</details>

---


### Tool call

_source line 282 · 2026-05-22T13:57:24.122381+00:00_

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
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
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

_source line 283 · 2026-05-22T13:57:24.223146+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 284 · 2026-05-22T13:57:28.640738+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "contrastive_entrain_calib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "contrastive_entrain_calib"
  }
}
```

</details>

---


### Tool result

_source line 285 · 2026-05-22T13:57:31.611170+00:00_

{"result":"# 项目 contrastive_entrain_calib 概况\n\n## 实验状态 (77 个)\n\n- **exp-003-eval-ckpt1000**: DONE (negative) — \n- **exp-003-eval-ckpt5000**: DONE (negative) — \n- **exp-009**: DONE (negative) — \n- **exp-012**: DONE (success) — \n- **exp-002v3**: DONE (negative) — \n- **exp-008v3**: DONE (negative) — \n- **exp002v2-recalib**: DONE (negative) — \n- **exp-003-s2**: RUNNING — \n- **exp-016**: DONE (negative) — \n- **exp-014**: DONE (killed) — \n- **vanilla-baseline**: DONE (success) — \n- **exp-002v2**: DONE (killed) — \n- **exp-002**: DONE (killed) — \n- **exp-008**: DONE (killed) — \n- **exp-001**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-22\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| exp-004-s2-v2 | ACT (SFT) seed 2 训练恢复：从 ckpt-2000 resume，验证 ACT 跨 seed 稳定性。原 exp-004-s2 因磁盘满在 step 2500 崩溃，现已迁移 output_dir 到数据盘恢复训练。 | — | — | — |\n| exp-003-s2 | R3-only GRPO baseline (seed 2): training with only the external DeBERTa reward (r3_weight=1.0, r1=r2=0) provides a lower bound for ablation, isolating the contribution of contrastive direction-based rewards (R1+R2). Seed 2 (seed=43) verifies reproducibility of seed 1 results. | — | — | — |\n\n## 待处理\n- exp-003-s2-eval-ckpt3000: Eval exp-003-s2 (R3-only seed 2) checkpoint-3000 with D027 unified preset. Cross-seed reproducibility: compare with seed 1 ckpt-3000 (SYCONScore=0.095) for exact step match.（排队等待 GPU）\n- exp-003-s2-eval-ckpt2500: Eval exp-003-s2 (R3-only seed 2) checkpoint-2500 with D027 unified preset. Cross-seed reproducibility: compare with seed 1 ckpt-3000 (SYCONScore=0.095) for trajectory alignment.（排队等待 GPU）\n\n## 近期结论\n- **exp-004-s2** (failed): ACT (SFT) seed 2 训练：验证 ACT 跨 seed 稳定性。Seed 1 (exp-004) 16/16 checkpoints > vanilla (0.170→0.301)。如果 seed 2 也展现类似 trajectory，则堵住 Reviewer \"ACT 只有 1 个 seed\" 攻击面。配置与 exp-004 完全相同，仅 seed=42→43。 ← 基于 exp-004\n- **exp-004-s2-eval-ckpt2500** (failed): Eval exp-004-s2 (ACT seed 2) c
…[truncated 1031 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 2970
}
```

</details>

---


### Tool call

_source line 286 · 2026-05-22T13:57:31.723397+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 287 · 2026-05-22T13:57:31.729434+00:00_

1	\documentclass[11pt,a4paper]{article}
2	\usepackage[hyperref]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage{amsmath}
6	\usepackage{amssymb}
7	\usepackage{booktabs}
8	\usepackage{multirow}
9	\usepackage{graphicx}
10	\usepackage{xcolor}
11	\usepackage{subcaption}
12	
13	\newcommand{\dsyc}{d_{\text{syc}}}
14	\newcommand{\tof}{\text{ToF}}
15	\newcommand{\nof}{\text{NoF}}
16	\newcommand{\sycon}{\textsc{SyconScore}}
17	\newcommand{\rone}{R_1}
18	\newcommand{\rthree}{R_3}
19	
20	\title{Discriminability Without Utility: Why Sycophancy Directions Fail as GRPO Rewards}
21	
22	\author{Anonymous}
23	
24	\begin{document}
25	\maketitle
26	
27	\begin{abstract}
28	\input{sections/abstract}
29	\end{abstract}
30	
31	\input{sections/introduction}
32	
33	\input{sections/framework}
34	
35	\input{sections/direction_quality}
36	
37	\input{sections/cosine_failure}
38	
39	\input{sections/probe_trap}
40	
41	\input{sections/discussion}
42	
43	\input{sections/related_work}
44	
45	\input{sections/conclusion}
46	
47	\section*{Limitations}
48	\input{sections/limitations}
49	
50	\section*{Reproducibility}
51	Code and data will be released upon acceptance. All training hyperparameters are reported in Appendix~\ref{app:training}. The 181 contrastive pairs and evaluation benchmark are included in the supplementary materials.
52	
53	\bibliography{references}
54	
55	\appendix
56	\input{sections/appendix}
57	
58	\end{document}
59	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Read",
  "elapsed_ms": 6
}
```

</details>

---


### Tool call

_source line 288 · 2026-05-22T13:57:31.764848+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review ARR 2026 call for papers submission guidelines author instructions site:aclweb.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review ARR 2026 call for papers submission guidelines author instructions site:aclweb.org"
  }
}
```

</details>

---


### Tool call

_source line 289 · 2026-05-22T13:57:32.375277+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_4/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"NO_PDF\"",
  "description": "Check if submitted PDF exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_4/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"NO_PDF\"",
    "description": "Check if submitted PDF exists"
  }
}
```

</details>

---


### Tool result

_source line 290 · 2026-05-22T13:57:32.845410+00:00_

-rw-r--r-- 1 ubuntu ubuntu 332045 May 22 13:53 /home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_4/submitted.pdf
PDF_EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Bash",
  "elapsed_ms": 470
}
```

</details>

---


### Tool call

_source line 291 · 2026-05-22T13:57:33.150454+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_issues.yaml 2>/dev/null || echo \"NO_ISSUES_YAML\"",
  "description": "Check existing review issues tracker"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_issues.yaml 2>/dev/null || echo \"NO_ISSUES_YAML\"",
    "description": "Check existing review issues tracker"
  }
}
```

</details>

---


### Tool result

_source line 292 · 2026-05-22T13:57:33.202330+00:00_

issues:
  # === ROUND 1-2 ISSUES (UPDATED FOR ROUND 3) ===

  - id: R1-N1
    summary: "Fisher exact test 将非独立 checkpoints 当独立样本，p<0.0001 不可信"
    category: method
    severity: critical
    status: resolved
    first_raised_round: 1
    last_seen_round: 1
    mentions:
      - round: 1
        reviewers: [1, 2]
        note: "R1 首提，R2 完全同意。"
      - round: 2
        reviewers: []
        note: "本轮未提及。论文已移除 Fisher p 值。已修复。"
      - round: 3
        reviewers: []
        note: "本轮未提及，确认已修复。"
    resolution: "论文已移除所有 Fisher p 值，改用描述性统计。"
    resolution_round: 2

  - id: R2-N1
    summary: "遗漏 Papadatos & Freedman (2024) probe penalty 成功案例"
    category: framing
    severity: critical
    status: resolved
    first_raised_round: 1
    last_seen_round: 3
    mentions:
      - round: 1
        reviewers: [1, 2]
        note: "必须讨论 probe penalty vs probe reward 的关键差异。"
      - round: 2
        reviewers: [2]
        note: "R2 将其列为论文优势——对比分析已充分。"
      - round: 3
        reviewers: [1, 2]
        note: "两位 Reviewer 均列为论文优势之一（inference-time vs training-time 对比精到）。确认已解决。"
    resolution: "§7 充分讨论，Round 2-3 均被列为论文优势。"
    resolution_round: 2

  - id: R2-N2
    summary: "references.bib 多条引用严重不完整"
    category: format
    severity: critical
    status: resolved
    first_raised_round: 1
    last_seen_round: 1
    mentions:
      - round: 1
        reviewers: [1, 2]
        note: "ACT 作者为 Unknown，6 条仅 et al."
      - round: 3
        reviewers: []
        note: "本轮未提及，确认已修复。"
    resolution: "Agent 已补全所有 bib entry。"
    resolution_round: 2

  - id: R1-N2
    summary: "ACT 正面结果仅基于单 seed 完整评估（seed 2 仍 ongoing）"
    category: experiment
    severity: critical
    status: in_progress
    first_raised_round: 1
    last_seen_round: 3
    mentions:
      - round: 1
        reviewers: [1, 2]
        note: "n=1 seed 不足以建立方法有效性。"
      - round: 2
        reviewers: [1, 2]
        note: "Table 4 脚注仍显示部分 checkpoints。"
      - round: 3
        reviewers: [1, 2]
        note: "Table 4 脚注 ‡ 显示
…[truncated 11774 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Bash",
  "elapsed_ms": 51
}
```

</details>

---


### Tool result

_source line 293 · 2026-05-22T13:57:40.616974+00:00_

Web search results for query: "ACL Rolling Review ARR 2026 call for papers submission guidelines author instructions site:aclweb.org"

Links: [{"title":"First Call for Papers – EACL 2026 Student Research Workshop (SRW) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/first-call-papers-eacl-2026-student-research-workshop-srw"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"},{"title":"Industry Track — Call for Papers @ EACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/industry-track-call-papers-eacl-2026"},{"title":"The 14th Joint Conference on Lexical and Computational Semantics | ACL Member Portal","url":"https://www.aclweb.org/portal/content/14th-joint-conference-lexical-and-computational-semantics"},{"title":"ACL Policy on Publication Ethics - Admin Wiki","url":"https://www.aclweb.org/adminwiki/index.php/ACL_Policy_on_Publication_Ethics"},{"title":"EACL 2026 - Call for System Demonstrations | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-call-system-demonstrations"}]

Based on the search results, I found information about ACL Rolling Review (ARR) and 2026 submission guidelines. Here are the key submission guidelines and author instructions:

## Paper Submission Format

Paper submissions must use the official ACL style templates, which are available as an Overleaf template and can be downloaded directly via https://aclrollingreview.org/cfp under 'Paper Submission Process, Criteria and Templates'. All submissions must be in PDF format.

## Anonymity Policy

Submissions will remain anonymous during peer review, but authors are free to post and discuss non-anonymous preprints at any time. Submiss
…[truncated 901 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "WebSearch",
  "elapsed_ms": 8852
}
```

</details>

---


### Tool call

_source line 294 · 2026-05-22T13:58:05.953438+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 submission deadline ARR cycle commitment page limit"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 submission deadline ARR cycle commitment page limit"
  }
}
```

</details>

---


### Tool call

_source line 295 · 2026-05-22T13:58:06.405713+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review May 2026 submission deadline cycle dates"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review May 2026 submission deadline cycle dates"
  }
}
```

</details>

---


### Tool call

_source line 296 · 2026-05-22T13:58:09.271198+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/",
  "description": "List paper section files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/",
    "description": "List paper section files"
  }
}
```

</details>

---


### Tool result

_source line 297 · 2026-05-22T13:58:09.673262+00:00_

abstract.tex
appendix.tex
conclusion.tex
cosine_failure.tex
direction_quality.tex
discussion.tex
framework.tex
introduction.tex
limitations.tex
probe_trap.tex
related_work.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Bash",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 298 · 2026-05-22T13:58:09.673795+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "contrastive_entrain_calib",
  "file": "paper_checklist.yaml",
  "max_chars": "5000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "contrastive_entrain_calib",
    "file": "paper_checklist.yaml",
    "max_chars": "5000"
  }
}
```

</details>

---


### Tool result

_source line 299 · 2026-05-22T13:58:11.885246+00:00_

Web search results for query: "EMNLP 2026 submission deadline ARR cycle commitment page limit"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"EMNLP 2026 Workshop WiNLP ARR Commitment | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FWorkshop%2FWiNLP_ARR_Commitment"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"EMNLP 2026 LaTeX Template | ACL Style Files & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/emnlp"}]

Based on the search results, here's the information about EMNLP 2026:

## Key Dates and Information:

**ARR Submission Deadline:**
The ARR submission deadline for long & short papers is May 25, 2026.

**Commitment Deadline:**
The EMNLP commitment deadline is August 2, 2026.

**ARR Cycle Commitment Policy:**
For the ARR 2026 May cycle aligned with both EMNLP and AACL, authors must explicitly declare which conference they intend to commit to at submission time, and this choice will be binding for EMNLP 2026.

**Page Limits:**
The format i
…[truncated 377 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "WebSearch",
  "elapsed_ms": 5931
}
```

</details>

---


### Tool result

_source line 300 · 2026-05-22T13:58:14.851037+00:00_

Web search results for query: "ACL Rolling Review May 2026 submission deadline cycle dates"

Links: [{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"aclrollingreview/dates.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/dates.md"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"ACL ARR 2026 January | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR%2F2026%2FJanuary"}]

Based on the search results, here is information about the ACL Rolling Review May 2026 submission deadline cycle dates:

ACL transitioned to 10-week review cycles starting with the May 2025 cycle. This means there are generally 5 cycles per year instead of 6.

However, the search results do not contain specific submission deadline dates for the May 2026 ARR cycle. The official ACL Rolling Review website mentions that a table lists all key dates for upcoming cycles, but the complete table with specific May 2026 dates was not included in t
…[truncated 491 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "WebSearch",
  "elapsed_ms": 8445
}
```

</details>

---


### Tool result

_source line 301 · 2026-05-22T13:58:14.851595+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'contrastive_entrain_calib'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 5177
}
```

</details>

---


### Tool call

_source line 302 · 2026-05-22T13:58:20.172767+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 303 · 2026-05-22T13:58:20.731030+00:00_

1	Representation engineering shows that large language models encode sycophancy as a linear direction in activation space. We extract a contrastive sycophancy direction ($\dsyc$) from style-controlled pairs, achieving cross-validated AUROC $0.827$ on Qwen3-8B and $0.779$ on Llama-3-8B. In experiments on Qwen3-8B, we test three $\dsyc$-based training formulations---two with Group Relative Policy Optimization (GRPO) and one SFT-based probe penalty; every formulation failed. The cosine reward could not separate valid revision from sycophantic capitulation in the narrow online activation gap. The probe reward created a stubbornness trap: the true-positive flip rate dropped to zero within 500 steps while entropy remained healthy. Removing $\dsyc$ entirely and training with a purely behavioral reward also failed: only 4 of 27 checkpoints across two seeds exceeded vanilla, while supervised fine-tuning exceeded vanilla at every evaluated checkpoint (seed 1: 16/16; seed 2: 4/4 ongoing). The root cause is a semantic gap between discriminability and reward utility: $\dsyc$ encodes \emph{whether} belief changed, not \emph{whether it should have}. A single scalar reward per completion could not convey which belief changes were warranted in our setting; dense per-token supervision (ACT) succeeded, though the methods differ along multiple dimensions beyond supervision granularity alone.
2	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Read",
  "elapsed_ms": 558
}
```

</details>

---


### Tool call

_source line 304 · 2026-05-22T13:58:20.932285+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 305 · 2026-05-22T13:58:21.134233+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Representation engineering \citep{zou2023repe} reveals that large language models encode sycophancy as a linear direction in their residual streams.
5	A contrastive sycophancy direction $\dsyc$, extracted from style-controlled pairs of valid belief revision and sycophantic capitulation, achieves cross-validated AUROC $0.827$ on Qwen3-8B and $0.779$ on Llama-3-8B, with discriminability rising monotonically across evidence-strength levels (\S\ref{sec:direction_quality}).
6	These results, replicated across two architecturally distinct model families, point to an appealing possibility: if the model's representations already separate sycophantic from non-sycophantic behavior, that separation should be convertible into a scalar reward signal for reinforcement learning.
7	Sycophancy is among the most persistent alignment failures in deployed systems \citep{sharma2023sycophancy}, and a representation-level reward could complement existing behavioral approaches by targeting the internal computation rather than its surface outputs.
8	
9	This paper shows that, in our experiments on Qwen3-8B, the conversion fails.
10	We test three formulations---two GRPO \citep{shao2024grpo} reward variants (cosine projection, continuous probe) and one SFT-based probe penalty---across six configurations; every formulation fails.
11	Cosine similarity cannot separate valid revision from sycophantic capitulation in the narrow online activation gap (\S\ref{sec:cosine_failure}).
12	A binary probe with stopped gradients creates a stubbornness trap: $\tof$ drops to zero within 500 steps while generation entropy remains at 0.70, masking behavioral death (\S\ref{sec:probe_trap}).
13	Removing $\dsyc$ in favor of a purely behavioral reward does not resolve the problem: $\rthree$-only GRPO exceeds vanilla at only 4 of 27 checkpoints across two seeds, while ACT exceeds vanilla at every evaluated checkpoint (seed 1: 16/16; seed 2: 4/4 ongoing; \S\ref{s
…[truncated 4019 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Read",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 306 · 2026-05-22T13:58:21.134720+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/framework.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/framework.tex"
  }
}
```

</details>

---


### Tool result

_source line 307 · 2026-05-22T13:58:21.586397+00:00_

1	\section{Experimental Framework}
2	\label{sec:framework}
3	
4	\subsection{Direction Extraction}
5	\label{ssec:extraction}
6	
7	We extract a linear sycophancy direction $\dsyc$ from the residual stream using contrastive activation pairs: a \emph{valid correction} (warranted belief revision under strong evidence) and a \emph{sycophantic capitulation} (unwarranted concession under social pressure).
8	We construct 181 contrastive pairs using GPT-4.1 in a two-stage pipeline: skeleton generation followed by 3-turn dialogue completion.
9	Style matching is enforced by automated validation (response length difference ${<}10\%$, shared opening phrase ${\geq}2$ words), with up to 3 retries per pair; 19 of 200 initial pairs were discarded for failing validation.
10	Evidence strength is annotated at three levels: \emph{weak} (75 pairs; personal memory or opinion), \emph{medium} (54 pairs; brief source citation), and \emph{strong} (52 pairs; authoritative source with detailed data).
11	From the 181 paired examples (362 activations total), we compute the mean difference at target layer $\ell$:
12	\begin{equation}
13	\label{eq:dsyc}
14	\dsyc = \frac{1}{N}\sum_{i=1}^{N}\left(\mathbf{h}^{+}_i - \mathbf{h}^{-}_i\right)
15	\end{equation}
16	where $\mathbf{h}^{+}_i$ and $\mathbf{h}^{-}_i$ are residual-stream activations for the $i$-th valid and sycophantic response.
17	The target layer is selected by 5-fold cross-validated AUROC; on Qwen3-8B this yields layer 19 with AUROC $0.827$ (bootstrap 95\% CI $[0.795,\, 0.857]$).
18	
19	\subsection{Reward Formulations}
20	\label{ssec:reward}
21	
22	Three formulations translate $\dsyc$ into a direction-based signal $\rone$.
23	For F1 and F3, $\rone$ enters as part of a GRPO \citep{shao2024grpo} reward $R = w_1 \cdot \rone + w_3 \cdot \rthree$, where $\rthree$ is a behavioral component (DeBERTa NLI classifier scoring consistency with the ground-truth answer).
24	\begin{itemize}
25	\item[\textbf{F1}] \textbf{Cosine projection} with four variants: 
…[truncated 3181 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 308 · 2026-05-22T13:58:21.586766+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/direction_quality.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/direction_quality.tex"
  }
}
```

</details>

---


### Tool result

_source line 309 · 2026-05-22T13:58:22.038552+00:00_

1	\section{Direction Discriminability}
2	\label{sec:direction_quality}
3	
4	Before evaluating $\dsyc$ as a reward signal (\S\ref{sec:cosine_failure}--\S\ref{sec:probe_trap}), we first establish that it captures a genuine sycophancy-related signal in the residual stream.
5	If the direction failed to discriminate sycophantic from non-sycophantic activations, downstream reward failures would be trivially explained by poor direction quality rather than by a fundamental gap between discriminability and reward utility.
6	We evaluate discriminability along five axes: cross-validated classification accuracy, evidence-strength stratification, cross-model transfer, training stability, and probe ablation.
7	Figure~\ref{fig:direction_quality} summarizes the per-layer AUROC profiles for both models.
8	
9	\paragraph{Qwen3-8B layer-wise discriminability.}
10	We evaluate $\dsyc$ via 5-fold cross-validated AUROC on 181 style-controlled contrastive pairs (\S\ref{ssec:extraction}).
11	The direction achieves AUROC $0.827$ (bootstrap 95\% CI $[0.795,\, 0.857]$) at its best layer (L19).
12	Discriminability emerges gradually across depth: layers L0--L8 perform near chance, statistical significance ($p < 0.01$) first appears at L16, and performance peaks at L19.
13	This gradual emergence, with the peak in the upper third of the network, suggests that sycophancy-relevant information is encoded as a late-stage representation rather than an input-level confound.
14	The direction also captures evidential granularity.
15	AUROC rises monotonically from 0.675 on weak-evidence pairs to 0.883 on medium and 0.929 on strong pairs.
16	This gradient indicates that $\dsyc$ encodes the degree of evidential warrant, not merely a binary sycophancy label.
17	
18	\paragraph{Cross-model generalization.}
19	To rule out that these results are specific to Qwen3-8B's representation geometry, we repeat the full extraction and evaluation pipeline on Llama-3-8B-Instruct.
20	Table~\ref{tab:cross_model} compares the t
…[truncated 3550 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 310 · 2026-05-22T13:58:22.038976+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/cosine_failure.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/cosine_failure.tex"
  }
}
```

</details>

---


### Tool result

_source line 311 · 2026-05-22T13:58:22.992634+00:00_

1	\section{Cosine \texorpdfstring{$\rone$}{R1}: Structural Failure}
2	\label{sec:cosine_failure}
3	
4	Section~\ref{sec:direction_quality} established that $\dsyc$ achieves AUROC 0.827 on Qwen3-8B.
5	We now test whether this discriminability translates into a viable GRPO reward.
6	Four configurations form a diagnostic chain (Table~\ref{tab:cosine_chain}): each resolves the failure mode of its predecessor but exposes a deeper limitation.
7	
8	\begin{table}[t]
9	\centering
10	\caption{Cosine $\rone$ failure chain on Qwen3-8B (LoRA rank$=$64, GRPO with $R = w_1 \cdot \rone + w_3 \cdot \rthree$).}
11	\label{tab:cosine_chain}
12	\begin{tabular}{lllll}
13	\toprule
14	Config & $\rone$ Formula & $w_1$ & Outcome & Root Cause \\
15	\midrule
16	F1a & $\tanh(\mathbf{h}\cdot\dsyc/20)$ & 0.25 & Gate saturation & Norm mismatch \\
17	F1b & $\cos(\mathbf{h},\, \dsyc)$ & 0.25 & $\rone \approx 0$ & Gap too small \\
18	F1c & +recalibration & 0.25 & Mode collapse & Reward discontinuity \\
19	F1d & $5\cos(\mathbf{h},\, \dsyc)$ & 0.40 & Mode collapse & $\rthree$ saturation \\
20	\bottomrule
21	\end{tabular}
22	\end{table}
23	
24	F1a uses a dot-product formulation ($\rone = \tanh(\mathbf{h} \cdot \dsyc / 20)$), but residual-stream norms exceed the direction norm by $100$--$1{,}200{\times}$, saturating the tanh gate and zeroing the gradient by step 955.
25	Switching to cosine similarity (F1b) eliminates norm dependence, yet the cosine gap between valid and sycophantic activations averages only 0.098 across layers---too narrow to generate meaningful reward contrast.
26	Online recalibration (F1c, \S\ref{ssec:recalib}) raises offline AUROC from 0.827 to 0.910 but paradoxically triggers mode collapse: the abrupt shift in $\dsyc$ at each recalibration event creates a reward discontinuity that destabilizes GRPO advantage estimates, collapsing entropy to 0.069 within 300 steps.
27	Amplifying the signal with $5{\times}$ scaling (F1d) lifts $\rone$ above the noise floor but simultaneously amplifies t
…[truncated 950 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Read",
  "elapsed_ms": 953
}
```

</details>

---


### Tool call

_source line 312 · 2026-05-22T13:58:22.993074+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/probe_trap.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/probe_trap.tex"
  }
}
```

</details>

---


### Tool result

_source line 313 · 2026-05-22T13:58:23.495097+00:00_

1	\section{The Probe Reward Trap}
2	\label{sec:probe_trap}
3	
4	The cosine formulations fail because the continuous projection of $\dsyc$ produces a gap too narrow for reward contrast.
5	A natural remedy is to discretize: train a logistic probe on $\dsyc$ and threshold its output, yielding $\rone = \mathbb{I}[P(\text{syc} \mid \mathbf{h}) < 0.5]$ (F2 in \S\ref{ssec:reward}).
6	We show that this discretization sidesteps the magnitude problem but creates a qualitatively worse failure.
7	Both probe experiments use SFT rather than GRPO (\S\ref{ssec:reward}); the trap is therefore independent of GRPO's optimization dynamics.
8	
9	\paragraph{Differentiable probe: gradient gaming.}
10	Without stop-gradient (exp-008), the policy discovers within ${\sim}30$ steps that shifting activations away from the sycophancy cluster maximizes $\rone$ regardless of response content, producing an inverted profile ($\tof = 0.978$, $\nof = 0.006$).
11	This motivates the frozen-probe design below.
12	
13	\paragraph{Binary probe: the stubbornness trap.}
14	With stop-gradient (exp-008v3), the policy cannot game the boundary but instead exploits a deeper flaw: $\dsyc$ does not condition on input validity, so refusing to revise a wrong answer receives the same $\rone = 1$ as correctly resisting invalid pressure.
15	By step 500, $\tof$ drops to 0.000 and $\nof$ reaches 0.995, yielding $\sycon = 0$.
16	Qualitative analysis reveals distinct failure modes: \emph{sycophantic stubbornness} (24\%), where the model verbally agrees but does not change its answer; \emph{deliberation traps} (29\%), where the model identifies the correct answer but cannot commit; and evidence-graded hedging, where the model adjusts its refusal style rather than its acceptance rate (Appendix~\ref{app:taxonomy}).
17	
18	\paragraph{Behavioral death precedes distributional collapse.}
19	
20	\begin{table}[t]
21	\centering
22	\caption{Probe reward trap trajectory (exp-008v3). Behavioral death ($\tof{=}0$) occurs at step 500; entr
…[truncated 2286 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 314 · 2026-05-22T13:58:23.495576+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 315 · 2026-05-22T13:58:23.947649+00:00_

1	\section{Analysis: Discriminability $\neq$ Reward Utility}\label{sec:discussion}
2	
3	\paragraph{Unified root cause.}
4	The failures in Sections~\ref{sec:cosine_failure} and~\ref{sec:probe_trap} trace to a single geometric limitation.
5	$\dsyc$ encodes the \emph{direction} of belief change but not its \emph{evidential warrant}: valid revision and sycophantic capitulation both shift activations toward the user's position along the same direction.
6	The two reward families expose complementary faces of this blindness.
7	Cosine $\rone$ penalizes all belief change indiscriminately; the resulting mode collapse (F1c, F1d) reflects excessive punishment of any activation shift along $\dsyc$.
8	The binary probe $\rone$ rewards all resistance regardless of input validity; the stubbornness trap ($\tof = 0$ by step 500) reflects excessive permissiveness toward activation stasis.
9	These are not independent design flaws but dual consequences of a direction that conflates the target behavior (resisting invalid challenges) with its complement (refusing valid corrections).
10	Cross-model evidence confirms the limitation extends beyond Qwen3-8B: Llama-3-8B independently achieves AUROC $0.779$ (bootstrap 95\% CI $[0.745,\, 0.819]$) on the same contrastive pairs with the same monotonic evidence gradient, so discriminability generalizes across architectures while the semantic gap between discriminability and reward utility persists.
11	This pattern contrasts with reasoning faithfulness and safety directions~\citep{zhang2026latentgrpo}, where the behavior to suppress is geometrically distinct from the behavior to preserve along the relevant direction.
12	\citet{wu2026rewardhacking} reinforce this principle: concept directions applied via advantage modification in GRPO achieve 100\% validation accuracy for reward hacking detection, where shortcut behaviors are geometrically separable---confirming that direction utility depends on geometric separability, not the optimization framework.

…[truncated 7554 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 316 · 2026-05-22T13:58:23.948086+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 317 · 2026-05-22T13:58:24.400011+00:00_

1	\section{Related Work}\label{sec:related_work}
2	
3	\paragraph{Representation Engineering.}
4	Linear directions in LLM residual streams encode behavioral concepts \citep{zou2023repe}; inference-time methods---ITI \citep{li2023iti}, ActAdd \citep{turner2023actadd}, CAA \citep{rimsky2024caa}---demonstrate that activation geometry suffices for behavioral control \citep{burns2023ccs}.
5	We use the same contrastive extraction as CAA but apply $\dsyc$ as an RL reward, revealing a gap that inference-time work does not encounter.
6	
7	\paragraph{Reward Design and Overoptimization.}
8	Proxy rewards diverge from true objectives under sustained optimization \citep{gao2023scaling}, and reward hacking can escalate to active tampering \citep{denison2024subterfuge}.
9	Our probe trap (\S\ref{sec:probe_trap}) is an extreme instance: the reward actively reinforces degenerate behavior rather than merely being circumvented \citep{skalse2022hacking}.
10	\citet{wu2026rewardhacking} demonstrate that representation-level directions succeed for reward hacking suppression when behaviors are geometrically separable (\S\ref{sec:discussion}).
11	
12	\paragraph{Sycophancy Characterization and Mitigation.}
13	Sycophancy is pervasive in RLHF-trained assistants \citep{sharma2023sycophancy}, amplified by RLHF \citep{shapira2026amplifies}, and traceable to late-layer preference shifts \citep{wang2025internal}; mitigation approaches include synthetic data \citep{wei2024synthetic}, consistency training \citep{consistency2025bctact}, and neuron-level correction \citep{obrien2025fewbadneurons}.
14	Our analysis shows why the step from diagnosis to reward is structurally blocked: $\dsyc$ conflates warranted revision with unwarranted capitulation.
15	
16	\paragraph{Probe-Based Inference-Time Mitigation.}
17	\citet{papadatos2024probepenalties} reduce sycophancy via Best-of-N reranking with linear probe penalties (94\% probe accuracy), where the probe selects among candidates without producing gradients tha
…[truncated 1208 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 318 · 2026-05-22T13:58:24.400381+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 319 · 2026-05-22T13:58:25.354152+00:00_

1	\section{Conclusion}\label{sec:conclusion}
2	
3	This work tested whether a representation direction that detects sycophantic behavior can serve as a training signal for sycophancy calibration.
4	In experiments on Qwen3-8B, $\dsyc$ achieved strong offline discriminability (AUROC 0.827), yet all three formulations failed---the two GRPO reward variants and the SFT-based probe penalty each produced behavioral collapse, and $\rthree$-only GRPO exceeded vanilla at only 4 of 27 checkpoints.
5	Our results suggest that discriminability in representation space does not guarantee utility as a training signal for behavioral attributes like sycophancy where the target concept lacks geometric separability (\S\ref{sec:discussion}).
6	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Read",
  "elapsed_ms": 953
}
```

</details>

---


### Tool call

_source line 320 · 2026-05-22T13:58:25.354516+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 321 · 2026-05-22T13:58:25.555469+00:00_

1	Our GRPO experiments use a group size of 2, below the typical range of 8--64 \citep{shao2024grpo}, due to memory constraints with 8B-parameter models. This limits within-group ranking diversity and constitutes an important confound: the observed failures may partly reflect insufficient exploration rather than a fundamental limitation of representation-based rewards. However, the probe reward trap (C2) arises in an SFT setting where group size is irrelevant, indicating that at least one failure mode is independent of GRPO hyperparameters. Additionally, all GRPO experiments truncate completions at 256 tokens (80--84\% truncation); all conditions share this setting, so relative comparisons are fair, but absolute conclusions about $\dsyc$ reward utility may be affected.
2	
3	Our RL training uses Qwen3-8B exclusively; cross-model discriminability is confirmed on Llama-3-8B (AUROC $0.779$; Table~\ref{tab:cross_model}), but compute constraints prevented training replication on a second architecture. Evidence strength was annotated by GPT-4.1 as a single annotator without human inter-annotator agreement.
4	
5	We report GRPO results from two random seeds; both exhibit qualitatively consistent oscillation patterns (similar amplitude, identical crash depth), but the limited seed count constrains statistical claims. ACT and GRPO differ along multiple dimensions beyond supervision granularity, so we cannot isolate the causal factor behind ACT's advantage.
6	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Read",
  "elapsed_ms": 200
}
```

</details>

---


### Tool call

_source line 322 · 2026-05-22T13:58:25.555988+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 323 · 2026-05-22T13:58:25.606576+00:00_

1	\section{Training Details}
2	\label{app:training}
3	
4	\paragraph{Reward weight selection.}
5	The weight $w_1$ is set by diagnostic-driven iteration: $w_1{=}0.25$ was initially chosen to down-weight the noisy cosine reward term; this was later increased to $w_1{=}0.40$ for F1d after diagnostics revealed that $w_1{=}0.25$ allowed the cosine term to contribute only ${\sim}8.3\%$ of total reward variance.
6	The empirical scaling factor in F1a ($\dsyc/20$) is a heuristic normalization; we did not find it critical to the failure modes reported.
7	
8	\paragraph{Response truncation.}
9	All GRPO experiments use \texttt{max\_completion\_length}=256, resulting in 80--84\% truncation of multi-turn responses.
10	This setting is shared across all conditions and does not affect relative comparisons; we retain it because response-level decisions typically manifest within the first 100--200 tokens.
11	
12	\paragraph{Hyperparameters.}
13	Table~\ref{tab:hyperparams} compares training configurations for GRPO variants and ACT.
14	
15	\begin{table}[h]
16	\centering
17	\small
18	\caption{Training hyperparameters. All experiments use Qwen3-8B, DeepSpeed ZeRO-2, bf16 precision.}
19	\label{tab:hyperparams}
20	\begin{tabular}{lcc}
21	\toprule
22	& GRPO (F1, F3)$^e$ & ACT \\
23	\midrule
24	Learning rate & 5e-5 & 5e-5 \\
25	Effective batch & 16 & 16 \\
26	Max steps & 8{,}000 & 8{,}000 \\
27	Warmup steps & 200 & 200 \\
28	LR schedule & linear$^a$ & linear \\
29	Grad.\ clipping & --- & 1.0 \\
30	\midrule
31	LoRA rank & 64 & 64 \\
32	LoRA $\alpha$ & 64 & 128 \\
33	LoRA modules & 4$^b$ & 7$^c$ \\
34	LoRA dropout & 0 & 0.05 \\
35	\midrule
36	Group size & 2$^d$ & --- \\
37	KL $\beta$ & 0.04 & --- \\
38	Max compl.\ len. & 256 & --- \\
39	Max seq.\ len. & --- & 1{,}024 \\
40	L2 loss weight & --- & 0.1 \\
41	\bottomrule
42	\end{tabular}
43	\\[2pt]
44	\raggedright\footnotesize
45	$^a$Cosine schedule for $\rthree$-only.
46	$^b$q/k/v/o\_proj.
47	$^c$+ gate/up/down\_proj (${\sim}1.75{\times}$ params; \S\
…[truncated 1651 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 324 · 2026-05-22T13:58:32.305521+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 325 · 2026-05-22T13:58:33.159224+00:00_

1	@article{zhang2026latentgrpo,
2	  title={Silence the Judge: Reinforcement Learning with Self-Verifier via Latent Geometric Clustering},
3	  author={Zhang, Nonghai and Ma, Weitao and Ma, Zhanyu and Xu, Jun and Gao, Jiuchong and Hao, Jinghua and He, Renqing and Xu, Jingwen},
4	  journal={arXiv preprint arXiv:2601.08427},
5	  year={2026}
6	}
7	
8	@article{zou2023repe,
9	  title={Representation Engineering: A Top-Down Approach to {AI} Transparency},
10	  author={Zou, Andy and Phan, Long and Chen, Sarah and Campbell, James and Guo, Phillip and Ren, Richard and Pan, Alexander and Yin, Xuwang and Mazeika, Mantas and Dombrowski, Ann-Kathrin and Gould, Shashwat and Li, Zifan and Xie, Chuanqi and Leung, Alexandria and Hase, Peter and Hendrycks, Dan},
11	  journal={arXiv preprint arXiv:2310.01405},
12	  year={2023}
13	}
14	
15	@inproceedings{rimsky2024caa,
16	  title={Steering Llama 2 via Contrastive Activation Addition},
17	  author={Rimsky, Nina and Gabrieli, Nick and Schulz, Jenna and Smith, Meg and Tong, Ioannis and Hubinger, Evan},
18	  booktitle={Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (ACL)},
19	  year={2024}
20	}
21	
22	@article{shao2024grpo,
23	  title={DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models},
24	  author={Shao, Zhihong and Wang, Peiyi and Zhu, Qihao and Xu, Runxin and Song, Junxiao and Zhang, Mingchuan and Li, Y.K. and Wu, Y. and Guo, Daya},
25	  journal={arXiv preprint arXiv:2402.03300},
26	  year={2024}
27	}
28	
29	@inproceedings{li2023iti,
30	  title={Inference-Time Intervention: Eliciting Truthful Answers from a Language Model},
31	  author={Li, Kenneth and Patel, Oam and Vi{\'e}gas, Fernanda and Pfister, Hanspeter and Wattenberg, Martin},
32	  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},
33	  year={2023}
34	}
35	
36	@article{turner2023actadd,
37	  title={Steering Language Models With Activation Engineering},
38	  author={Turner, Alexander Mat
…[truncated 6911 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Read",
  "elapsed_ms": 853
}
```

</details>

---


### Tool call

_source line 326 · 2026-05-22T13:58:33.311060+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/agent/config.yaml 2>/dev/null | grep -A 5 \"external_review\"",
  "description": "Check external review config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/agent/config.yaml 2>/dev/null | grep -A 5 \"external_review\"",
    "description": "Check external review config"
  }
}
```

</details>

---


### Tool result

_source line 327 · 2026-05-22T13:58:34.064267+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Bash",
  "elapsed_ms": 753
}
```

</details>

---


### Tool call

_source line 328 · 2026-05-22T13:58:34.188207+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_4/submitted.pdf"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_4/submitted.pdf"
  }
}
```

</details>

---


### Tool result

_source line 329 · 2026-05-22T13:58:34.245774+00:00_

This PDF has 11 pages, which is too many to read at once. Use the pages parameter to read specific page ranges (e.g., pages: "1-5"). Maximum 20 pages per request.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Read",
  "elapsed_ms": 57
}
```

</details>

---


### Tool call

_source line 330 · 2026-05-22T13:58:39.171208+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_4/submitted.pdf",
  "pages": "1-5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_4/submitted.pdf",
    "pages": "1-5"
  }
}
```

</details>

---


### Tool result

_source line 331 · 2026-05-22T13:58:39.624757+00:00_

PDF pages extracted: 5 page(s) from /home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_4/submitted.pdf (324.3KB)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Read",
  "elapsed_ms": 453
}
```

</details>

---


### Tool call

_source line 332 · 2026-05-22T13:58:39.638000+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_4/submitted.pdf",
  "pages": "6-11"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_4/submitted.pdf",
    "pages": "6-11"
  }
}
```

</details>

---


### Tool result

_source line 333 · 2026-05-22T13:58:40.140287+00:00_

PDF pages extracted: 6 page(s) from /home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_4/submitted.pdf (324.3KB)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 334 · 2026-05-22T13:58:40.350227+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/agent/config.yaml 2>/dev/null",
  "description": "Read full project config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/agent/config.yaml 2>/dev/null",
    "description": "Read full project config"
  }
}
```

</details>

---


### Tool result

_source line 335 · 2026-05-22T13:58:40.401010+00:00_

Exit code 1

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 336 · 2026-05-22T13:59:17.410280+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib -name \"config.yaml\" -o -name \"config.yml\" -o -name \"project.yaml\" 2>/dev/null | head -10",
  "description": "Find project config files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib -name \"config.yaml\" -o -name \"config.yml\" -o -name \"project.yaml\" 2>/dev/null | head -10",
    "description": "Find project config files"
  }
}
```

</details>

---


### Tool result

_source line 337 · 2026-05-22T13:59:17.462201+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Bash",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 338 · 2026-05-22T13:59:23.244323+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/agent/ 2>/dev/null; echo \"---\"; ls /home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/config/ 2>/dev/null; echo \"---\"; find /home/ubuntu/.agent-ml-research-be-idea-gen-0515-3 -maxdepth 2 -name \"*.yaml\" -o -name \"*.yml\" 2>/dev/null | head -20",
  "description": "Find config files in project"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/agent/ 2>/dev/null; echo \"---\"; ls /home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/config/ 2>/dev/null; echo \"---\"; find /home/ubuntu/.agent-ml-research-be-idea-gen-0515-3 -maxdepth 2 -name \"*.yaml\" -o -name \"*.yml\" 2>/dev/null | head -20",
    "description": "Find config files in project"
  }
}
```

</details>

---


### Tool result

_source line 339 · 2026-05-22T13:59:23.345163+00:00_

---
approvals.yaml
backend.yaml
claude_sessions.json
crons.yaml
email_tokens.json
feishu.yaml
keepalive.json
mcp_config.json
mcp_config_director.json
mcp_config_distiller.json
mcp_config_dream_review_director.json
mcp_config_paper_agent.json
mcp_config_paper_audit_review_visual.json
mcp_config_review_director.json
mcp_config_review_reviewer_1.json
mcp_config_review_reviewer_2.json
mcp_config_reviewer.json
mcp_config_worker_074936fc4b5d802648d5b9b7fe3a8a01.json
mcp_config_worker_0aa51d591547913249ab7a68dc681be8.json
mcp_config_worker_116db043ffcfd41b2805e6feba9eb07d.json
mcp_config_worker_12093ef55c63229acbf88fd2b9106dce.json
mcp_config_worker_12b115418db47d5a3e32d0af329c5f08.json
mcp_config_worker_14d296b01755362efedfab08bc7a4e38.json
mcp_config_worker_163190b5921248b2c209b2f8eb295353.json
mcp_config_worker_29834432f6498e7996daf9a6d4e8eda9.json
mcp_config_worker_33c066fe8f41bfaa9b9c844bb47eca4f.json
mcp_config_worker_34b8beca3d3e38da8c29b9af314ca15a.json
mcp_config_worker_3683e51e3c097c93488562d683342ec7.json
mcp_config_worker_41d735d56651d19d6a7920071cdacb59.json
mcp_config_worker_421decd2032b14f2ef6566c2172240c1.json
mcp_config_worker_52f0337c0eb747cb4b38db8eace91307.json
mcp_config_worker_5304abbd56fd7a7f12edca904ca28ec0.json
mcp_config_worker_567fac45f9ef5ad1a9223cbb3364faf1.json
mcp_config_worker_5fb1f955b45e38e31789286a1790398d.json
mcp_config_worker_6679bd63c74f529fddfcffaa0a492c96.json
mcp_config_worker_69e382e805b6f185c49ecc4b6d1f2d44.json
mcp_config_worker_72afdb189846fee22cd3481b9bd48f97.json
mcp_config_worker_7452874ce81eb89ffd857f072209b08f.json
mcp_config_worker_8164f16cea05223301ec10d99f320a22.json
mcp_config_worker_8a7d2bd5fcbc48194f34ebcc14ac61b2.json
mcp_config_worker_8ce90f8d54cb7ad4888b21892ef36c51.json
mcp_config_worker_91888988436c01dfc0d65cc645a31cd1.json
mcp_config_worker_943f40256720b8f6634ec1980a24acc1.json
mcp_config_worker_a2a1f628eaaf041a675e5db173e7463a.json
mcp_config_worker_ac138dec086db9fd9257ce40028f628d.json
mcp_config_worker_bc099
…[truncated 1466 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 340 · 2026-05-22T13:59:28.970012+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -r \"external_review\" /home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/config/ 2>/dev/null; grep -r \"external_review\" /home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/ --include=\"*.yaml\" --include=\"*.yml\" --include=\"*.json\" 2>/dev/null | head -5",
  "description": "Search for external review config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -r \"external_review\" /home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/config/ 2>/dev/null; grep -r \"external_review\" /home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/ --include=\"*.yaml\" --include=\"*.yml\" --include=\"*.json\" 2>/dev/null | head -5",
    "description": "Search for external review config"
  }
}
```

</details>

---


### Tool result

_source line 341 · 2026-05-22T13:59:29.122577+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "Bash",
  "elapsed_ms": 152
}
```

</details>

---


### Tool call

_source line 342 · 2026-05-22T14:00:08.790261+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "contrastive_entrain_calib",
  "review_chat_id": "oc_056796cf71f839be40019e5f1a11791b"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "contrastive_entrain_calib",
    "review_chat_id": "oc_056796cf71f839be40019e5f1a11791b"
  }
}
```

</details>

---


### Tool result

_source line 343 · 2026-05-22T14:00:26.206120+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 17415
}
```

</details>

---


### Tool call

_source line 344 · 2026-05-22T14:00:26.508328+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "你是 Reviewer 1，负责**方法严谨性 + 实验设计**。\n\n## Venue 信息\n- **目标**: EMNLP 2026 via ARR May 2026\n- **截止日期**: 2026-05-25\n- **页数限制**: 正文 8 页（Long paper），参考文献无限制，Limitations 不计入页数\n- **模板**: ACL style (two-column, 11pt, a4paper)\n- **匿名规则**: Double-blind\n\n## 论文文件\n- LaTeX: `/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_4/submitted.pdf`\n\n## 你的审查侧重\n\n**核心关注**：方法论严谨性、实验设计、统计方法、claims 与证据的对齐度。\n\n请重点审查以下方面：\n\n1. **实验设计充分性**\n   - GRPO group_size=2 是否构成致命 confound？论文在 Limitations 中披露了此问题，但这是否足够？\n   - max_completion_length=256 导致 80-84% truncation rate——这对结果有效性的影响\n   - 仅 2 个 random seeds 是否足以支撑负面结论？\n   - ACT seed 2 仅 4/16 checkpoints 已评估——ongoing 数据的呈现是否合理？\n\n2. **统计方法**\n   - AUROC 的 bootstrap CI 是否正确使用？\n   - SyconScore harmonic mean 的选择是否充分 justify？（ToF=0 时自动归零的 mask effect）\n   - Cross-seed rank correlation 声称 ρ≈0.33——2 seeds 的 Spearman 理论上只能取 ±1，计算方式是否说明清楚？\n\n3. **Claims vs Evidence 对齐**\n   - 标题 \"Why Sycophancy Directions Fail as GRPO Rewards\" 是否精确反映实验范围？\n   - \"discriminability ≠ reward utility\" 的泛化声明是否超出 single case study？\n   - ACT vs GRPO 对比的 confounding factors（5+ 维度差异）是否充分讨论？\n\n4. **Contrastive pairs 构建**\n   - 181 pairs 由 GPT-4.1 生成——quality control 是否充分？\n   - Evidence strength 三级标注缺乏人工 IAA——这对核心发现的影响\n\n5. **可复现性**\n   - 超参数披露是否完整？\n   - 代码/数据 \"upon acceptance\" 声明是否足够？\n\n请按 ARR 审稿标准输出完整审稿报告（Strengths / Weaknesses / Questions / Missing References / Soundness / Overall Assessment）。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "你是 Reviewer 1，负责**方法严谨性 + 实验设计**。\n\n## Venue 信息\n- **目标**: EMNLP 2026 via ARR May 2026\n- **截止日期**: 2026-05-25\n- **页数限制**: 正文 8 页（Long paper），参考文献无限制，Limitations 不计入页数\n- **模板**: ACL style (two-column, 11pt, a4paper)\n- **匿名规则**: Double-blind\n\n## 论文文件\n- LaTeX: `/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_4/submitted.pdf`\n\n## 你的审查侧重\n\n**核心关注**：方法论严谨性、实验设计、统计方法、claims 与证据的对齐度。\n\n请重点审查以下方面：\n\n1. **实验设计充分性**\n   - GRPO group_size=2 是否构成致命 confound？论文在 Limitations 中披露了此问题，但这是否足够？\n   - max_completion_length=256 导致 80-84% truncation rate——这对结果有效性的影响\n   - 仅 2 个 random seeds 是否足以支撑负面结论？\n   - ACT seed 2 仅 4/16 checkpoints 已评估——ongoing 数据的呈现是否合理？\n\n2. **统计方法**\n   - AUROC 的 bootstrap CI 是否正确使用？\n   - SyconScore harmonic mean 的选择是否充分 justify？（ToF=0 时自动归零的 mask effect）\n   - Cross-seed rank correlation 声称 ρ≈0.33——2 seeds 的 Spearman 理论上只能取 ±1，计算方式是否说明清楚？\n\n3. **Claims vs Evidence 对齐**\n   - 标题 \"Why Sycophancy Directions Fail as GRPO Rewards\" 是否精确反映实验范围？\n   - \"discriminability ≠ reward utility\" 的泛化声明是否超出 single case study？\n   - ACT vs GRPO 对比的 confounding factors（5+ 维度差异）是否充分讨论？\n\n4. **Contrastive pairs 构建**\n   - 181 pairs 由 GPT-4.1 生成——quality control 是否充分？\n   - Evidence strength 三级标注缺乏人工 IAA——这对核心发现的影响\n\n5. **可复现性**\n   - 超参数披露是否完整？\n   - 代码/数据 \"upon acceptance\" 声明是否足够？\n\n请按 ARR 审稿标准输出完整审稿报告（Strengths / Weaknesses / Questions / Missing References / Soundness / Overall Assessment）。"
  }
}
```

</details>

---


### Tool result

_source line 345 · 2026-05-22T14:00:40.991814+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 14483
}
```

</details>

---


### Tool call

_source line 346 · 2026-05-22T14:00:41.142973+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "你是 Reviewer 2，负责**新颖性 + 完整性 + 写作质量**。\n\n## Venue 信息\n- **目标**: EMNLP 2026 via ARR May 2026\n- **截止日期**: 2026-05-25\n- **页数限制**: 正文 8 页（Long paper），参考文献无限制，Limitations 不计入页数\n- **模板**: ACL style (two-column, 11pt, a4paper)\n- **匿名规则**: Double-blind\n\n## 论文文件\n- LaTeX: `/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_4/submitted.pdf`\n\n## 你的审查侧重\n\n**核心关注**：Contribution 新颖性、Related Work 覆盖度、论文 framing、写作质量、格式合规。\n\n请重点审查以下方面：\n\n1. **Contribution 新颖性**\n   - \"discriminability ≠ reward utility\" 这一 insight 是否足够新颖？是否已被前人隐含或显式讨论？\n   - Probe reward trap（C2）的 behavioral-before-distributional collapse 发现是否有独立价值？\n   - 本文主要是 negative results paper——在 EMNLP 的接收标准下这是否有足够贡献？\n\n2. **Related Work 完整性**\n   - 检查是否遗漏了关键 related work，特别是：\n     - Process Reward Models (SMART) 的讨论是否充分？\n     - Wu & Tang (2026) 对比论证是否有定量支撑？\n     - CRAFT, Latent-GRPO 讨论深度是否足够？\n     - DPO/KTO 等 preference-based 方法的讨论\n   - 是否有 2025-2026 年的重要相关工作被遗漏？\n\n3. **Framing 和叙事**\n   - 两个 contributions (C1, C2) 的表述是否清晰、准确、不 overclaim？\n   - \"discriminability ≠ reward utility\" 是否被过度泛化（仅在 sycophancy + GRPO + Qwen3-8B 上验证）？\n   - Discussion 和 Conclusion 中的推测性声明是否标注为 hypothesis？\n\n4. **写作质量**\n   - 论文结构是否清晰？各节之间的逻辑流是否通顺？\n   - Abstract 是否准确概括了论文的 claims 和发现？\n   - 术语使用是否一致？\n   - 图表是否信息丰富且设计清晰？\n\n5. **格式合规**\n   - 正文是否在 8 页限制内？\n   - 匿名规则是否遵守？（检查 author 信息、self-references）\n   - 参考文献格式是否完整一致？\n   - ACL style 模板是否正确使用？\n\n请按 ARR 审稿标准输出完整审稿报告（Strengths / Weaknesses / Questions / Missing References / Novelty / Overall Assessment）。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "你是 Reviewer 2，负责**新颖性 + 完整性 + 写作质量**。\n\n## Venue 信息\n- **目标**: EMNLP 2026 via ARR May 2026\n- **截止日期**: 2026-05-25\n- **页数限制**: 正文 8 页（Long paper），参考文献无限制，Limitations 不计入页数\n- **模板**: ACL style (two-column, 11pt, a4paper)\n- **匿名规则**: Double-blind\n\n## 论文文件\n- LaTeX: `/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/review_round_4/submitted.pdf`\n\n## 你的审查侧重\n\n**核心关注**：Contribution 新颖性、Related Work 覆盖度、论文 framing、写作质量、格式合规。\n\n请重点审查以下方面：\n\n1. **Contribution 新颖性**\n   - \"discriminability ≠ reward utility\" 这一 insight 是否足够新颖？是否已被前人隐含或显式讨论？\n   - Probe reward trap（C2）的 behavioral-before-distributional collapse 发现是否有独立价值？\n   - 本文主要是 negative results paper——在 EMNLP 的接收标准下这是否有足够贡献？\n\n2. **Related Work 完整性**\n   - 检查是否遗漏了关键 related work，特别是：\n     - Process Reward Models (SMART) 的讨论是否充分？\n     - Wu & Tang (2026) 对比论证是否有定量支撑？\n     - CRAFT, Latent-GRPO 讨论深度是否足够？\n     - DPO/KTO 等 preference-based 方法的讨论\n   - 是否有 2025-2026 年的重要相关工作被遗漏？\n\n3. **Framing 和叙事**\n   - 两个 contributions (C1, C2) 的表述是否清晰、准确、不 overclaim？\n   - \"discriminability ≠ reward utility\" 是否被过度泛化（仅在 sycophancy + GRPO + Qwen3-8B 上验证）？\n   - Discussion 和 Conclusion 中的推测性声明是否标注为 hypothesis？\n\n4. **写作质量**\n   - 论文结构是否清晰？各节之间的逻辑流是否通顺？\n   - Abstract 是否准确概括了论文的 claims 和发现？\n   - 术语使用是否一致？\n   - 图表是否信息丰富且设计清晰？\n\n5. **格式合规**\n   - 正文是否在 8 页限制内？\n   - 匿名规则是否遵守？（检查 author 信息、self-references）\n   - 参考文献格式是否完整一致？\n   - ACL style 模板是否正确使用？\n\n请按 ARR 审稿标准输出完整审稿报告（Strengths / Weaknesses / Questions / Missing References / Novelty / Overall Assessment）。"
  }
}
```

</details>

---


### Tool result

_source line 347 · 2026-05-22T14:00:42.618088+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1475
}
```

</details>

---


### Assistant

_source line 348 · 2026-05-22T14:00:53.447961+00:00_

已并行启动：
- ✅ **视觉审查 Agent** — 已启动，fire-and-forget
- ✅ **Reviewer 1**（方法严谨性）— 已分配
- ✅ **Reviewer 2**（新颖性/完整性）— 已分配

等待两位 Reviewer 返回初审报告。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director"
}
```

</details>

---


## Round 26

## Round 26

2 recorded events


### User

_source line 349 · 2026-05-22T14:06:31.068866+00:00_

[Reviewer 2 审稿意见]:
## 总体评分
**Overall**: 3.0 / 5（Findings）
**一句话总结**: 论文系统性地展示了 representation-level discriminability 不能直接转化为 GRPO reward utility 的负面结果，发现有价值但实验范围偏窄（单一行为属性、单一模型、group size=2、仅2个seed），分析深度不足以支撑其泛化性的 framing。

## 官方维度打分（来自 ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.0/5 | 核心 claim 有实验支撑，但 group size=2 远低于典型范围(8-64)，仅2个 seed，实验规模不足以排除 hyperparameter confound |
| Excitement | 2.5/5 | "discriminability ≠ utility" 作为一般原则并不出人意料；probe reward trap (C2) 有实用价值但窄领域发现 |
| Reproducibility | 4/5 | 超参数详尽（Table 5），承诺代码发布，contrastive pair 构建有详细描述，整体可复现性好 |
| Reviewer Confidence | 4/5 | 熟悉 representation engineering、GRPO、sycophancy alignment 相关文献 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] Group size=2 严重削弱 C1 的可信度
- 具体位置：Section 9 (Limitations), Table 5, §2.2
- 问题：论文承认 GRPO group size=2 远低于典型范围 8-64（Shao et al., 2024）。GRPO 的核心机制依赖 group 内 relative advantage 估计，group size=2 意味着只有两个 rollout 做对比，advantage 估计方差极大。论文声称 "at least one failure mode is independent of GRPO hyperparameters"（指 C2 probe trap），但 C1 的核心结论——"Every tested GRPO formulation fails"——在 group size=2 的条件下可能主要反映的是 GRPO 本身在极端 hyperparameter 下的不稳定性，而非 d_syc 作为 reward signal 的根本缺陷。
- 为什么影响接收：如果 C1 的失败可以通过增大 group size（如 8 或 16）来缓解，那么论文的核心 thesis "discriminability ≠ utility" 就不成立——问题出在 optimization dynamics 而非 reward signal 本身。
- 建议修改方向：至少在一个 formulation（如 F1a cosine）上测试 group size=8 和 group size=16，验证失败是否 robust across group sizes。如果资源受限，至少提供更强的论证说明为什么 group size 不是 confounding factor。

**N2** [critical] 标题和 framing 过度泛化，与证据范围不匹配
- 具体位置：Title, Abstract, Section 6 ("Discriminability ≠ Reward Utility"), Section 8
- 问题：标题 "Discriminability Without Utility" 和 Section 6 的 framing 暗示这是一个关于 representation-based reward 的一般性原则。但实验证据仅来自：(1) 一种行为属性（sycophancy），(2) 一种 RL 算法（GRPO），(3) 一种主要模型（Qwen3-8B，Llama-3-8B 仅用于 d_syc 提取验证，未做 RL 训练），(4) 极小 group size(2)。论文在 Section 8 用 "may" 做了一定 hedge（"the principle may apply to other behavioral attributes"），但标题和 abstract 没有反映这一局限。
- 为什么影响接收：Overclaiming 是 ARR 审稿的常见拒稿原因。Wu & Tang (2026) 的工作实际上展示了 representation engineering 在 reward hacking detection 中的成功应用（100% validation accuracy），这与本文的负面结论形成直接对比。本文需要更精确地界定其 claim 的适用范围。
- 建议修改方向：(1) 将标题限定到 sycophancy 和/或 GRPO，如 "Why Contrastive Sycophancy Directions Fail as GRPO Rewards"；(2) 在 Abstract 中明确实验范围限制；(3) 在 Discussion 中深入分析为什么 Wu & Tang (2026) 的 setting 成功而本文的 setting 失败——是行为属性的几何特性差异还是 optimization framework 的差异？

**N3** [critical] 缺乏与标准 RM-based GRPO 的对比基线
- 具体位置：Section 4, Table 4
- 问题：论文测试了 4 种 d_syc-based reward formulation + ACT，全部失败。但缺少一个关键对照：使用标准 reward model（如 trained classifier 或 LLM-as-judge）的 GRPO 在同一 sycophancy calibration task 上是否能成功？如果标准 RM-based GRPO 也失败，那问题在于 task formulation 或 GRPO 超参数，而非 d_syc；如果标准 RM 成功，则更有力地支持 "discriminability ≠ utility" 的论点。
- 为什么影响接收：没有正面对照，无法区分 "d_syc 作为 reward 有缺陷" 和 "这个 task/setup 本身就不适合 GRPO"。
- 建议修改方向：添加一个 LLM-judge-based 或 trained-classifier-based GRPO baseline，至少在 F1a 配置下运行一次。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] Wu & Tang (2026) 的对比论证缺乏定量分析
- 具体位置：Section 7, Related Work, 第2段
- 问题：论文引用 Wu & Tang (2026) 说他们 "reinforce this principle: concept directions applied via advantage modification in GRPO achieve 100% validation accuracy for reward hacking detection, where shortcut behaviors are geometrically separable—confirming that direction utility depends on geometric separability, not the optimization framework." 这个论证有问题：Wu & Tang 的成功恰恰说明 representation-based reward 在某些条件下 CAN work，这与本文标题 "Discriminability Without Utility" 的 framing 矛盾。论文试图用 "geometric separability" 来解释差异，但没有定量验证 sycophancy 的 d_syc 是否缺乏这种 geometric separability——事实上，AUROC 0.827 suggests 不错的可分性。
- 建议：定量比较 sycophancy direction 和 Wu & Tang 的 shortcut direction 在 geometric properties 上的差异（如 cluster separation, inter/intra-class variance），或至少在 Discussion 中承认这一对比的不完整性。

**W2** [warning] CRAFT 和 Latent-GRPO 讨论过于简略
- 具体位置：Section 7, Related Work, 最后一段
- 问题：CRAFT (Luo et al., 2026) 和 Latent-GRPO (Zhang et al., 2026) 各只有半句话的提及（"extends GRPO with latent-space rewards for reasoning; CRAFT applies representation-level constraints during RL"）。这两个工作都使用 latent-space/representation-level signal 做 RL 训练，与本文的核心主题直接相关。特别是 Latent-GRPO 从 latent space 几何结构中提取 reward signal 并成功应用于 reasoning，这与本文的负面结果形成有意义的对比。论文应当讨论为什么这些方法成功而本文的方法失败。
- 建议：扩展对 CRAFT 和 Latent-GRPO 的讨论，分析 sycophancy 与 reasoning/safety 在 representation geometry 上的差异，以及为什么 latent-space reward 在某些 domain 有效但在 sycophancy calibration 中失败。

**W3** [warning] 仅2个 random seed 的统计说服力不足
- 具体位置：Section 9 (Limitations), Figures 2-3
- 问题：所有 GRPO 实验仅报告2个 seed 的结果。论文说 "both seeds show the same oscillation pattern with stochastic timing and magnitude divergence"，但2个 seed 不足以建立统计显著性。Figures 2-3 展示两条轨迹，定性一致但定量差异大（seed 1 crash at checkpoint 6000 vs seed 2 peaks at checkpoint 4000）。"Qualitatively consistent" 在2个 seed 下不是很有说服力。
- 建议：增加到至少3-5个 seed，或对现有2个 seed 的结果提供更谨慎的措辞（避免 "consistent"，改用 "preliminary" 或 "suggestive"）。

**W4** [warning] DPO/KTO 作为替代方案未做实验探索
- 具体位置：Section 7 最后一句
- 问题：论文提到 "whether pairwise optimization avoids the failures we observe remains open"，但既然 d_syc 可以直接生成 preference pairs（高 d_syc 投影 vs 低投影），DPO/KTO 是一个自然的替代方案。将其仅列为 open question 而不做任何实验探索，降低了论文的完整性。这在"负面结果论文"中尤其重要——读者需要确信作者不是只测了最难成功的方法。
- 建议：至少测试一种 preference-based 方法（DPO 或 KTO），或提供更具体的分析说明为什么 d_syc 的 confounding nature 同样会影响 preference-based 方法。

**W5** [warning] 缺少 Process Reward Model (PRM) 的讨论
- 具体位置：Section 7 (Related Work)
- 问题：论文的 reward signal 是 outcome-level（整个 completion 的 cosine/probe score）。Process Reward Models 提供 per-step reward，可能缓解论文中观察到的 "d_syc encodes direction of belief change but not whether it should have changed" 问题——如果在对话的每个 turn 都能检测 sycophancy 方向变化，而不仅是最终 outcome，可能提供更有用的 training signal。论文未讨论 PRM 视角。
- 建议：在 Related Work 或 Discussion 中讨论 per-step/process reward 是否可能克服 outcome-level d_syc reward 的局限性。

---

## 小问题（不影响接收）

- **术语一致性**：论文交替使用 "behavioral collapse" 和 "behavioral death"（Section 5 标题用 "Probe Reward Trap"，正文用 "behavioral death"），建议统一。
- **Table 3 可读性**：Table 3（probe reward trap trajectory）中 "*Stall@epoch*" 列头与其他列格式不一致，排版略乱。
- **Section 6 标题**：Section 6 标题 "Analysis: Discriminability ≠ Reward Utility" 直接用等式作为 section title 不太规范，建议改为更描述性的标题。
- **Cross-reference**：Section 2.1 提到 "Appendix A" 但 Appendix A 标题是 "Training Details"，Section 3 提到 "Appendix B" (Stubbornness Taxonomy)——cross-reference 正确但建议在正文中更明确地标注 appendix 内容。
- **Figure 1 字体偏小**：Figure 1 的 legend 和 axis labels 在打印时可能难以阅读。

---

## 主要优势

1. **系统性实验设计**：论文测试了6种配置（4种 GRPO reward variant + ACT + R3-only GRPO baseline），展示了 failure 的 robustness across formulations，这是负面结果论文应有的严谨性。

2. **Probe reward trap (C2) 是有价值的发现**：behavioral death 比 distributional collapse 早 1,300 步的观察，以及 entropy monitoring 会 miss 这种 failure 的警告，对 RL alignment practitioners 有实际指导意义。

3. **Cross-model 验证**：d_syc 在 Qwen3-8B 和 Llama-3-8B 上的一致性验证（Table 1）增强了 direction 本身质量的可信度。

4. **Mechanistic 分析有深度**：Section 3 的 per-layer discriminability 分析（Figure 1）和 Section 6 的 root cause analysis 提供了超越表面失败现象的洞察。

5. **写作清晰**：论文结构逻辑通顺，从 direction extraction → reward formulation → failure catalog → mechanistic analysis 的叙事线索清晰。

6. **格式合规**：正文8页，匿名（"Anonymous"），ACL style 模板正确，参考文献格式一致，Limitations 章节覆盖了主要局限性。

---

## 格式合规检查

| 项目 | 状态 | 备注 |
|------|------|------|
| 正文页数 ≤ 8 | ✅ 合规 | 正文 Section 1-8 在前8页完成 |
| 匿名 | ✅ 合规 | 作者栏显示 "Anonymous"，未发现 self-citation 或身份信息泄露 |
| ACL style 模板 | ✅ 合规 | 双栏、11pt、a4paper |
| 参考文献格式 | ✅ 基本合规 | 多数引用格式一致；部分引用为 arXiv preprint 格式，可接受 |
| Limitations | ✅ 包含 | 页9，覆盖 group size、token 数、model scope 等限制 |
| Reproducibility | ✅ 包含 | 页9，承诺代码和数据发布 |

---

## 总结判断

本文是一篇结构清晰、实验系统的负面结果论文，核心发现（d_syc discriminability 不能转化为 GRPO reward utility）有一定价值。但三个 critical 问题限制了其贡献：(1) group size=2 使 C1 的 GRPO failure 可能是 hyperparameter confound 而非 fundamental limitation；(2) 标题和 framing 的泛化程度与单一行为/模型/算法的证据不匹配；(3) 缺少标准 RM-based GRPO 的正面对照。如果能解决 N1（增加 group size 实验）和 N3（添加 RM baseline），论文可以达到 Findings 水准。当前状态下，建议 3.0（Findings borderline）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 350 · 2026-05-22T14:06:43.388098+00:00_

Reviewer 2 报告已收到。等待 Reviewer 1 返回后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director"
}
```

</details>

---


## Round 27

## Round 27

2 recorded events


### User

_source line 351 · 2026-05-22T14:06:52.922217+00:00_

[Reviewer 2 审稿结果]:
审稿完成。报告已提交给 Review Director，评分 **Overall 3.0（Findings）**。

核心判断：3个 critical 问题——group size=2 可能是 confound 而非 fundamental failure、标题/framing 过度泛化、缺少标准 RM baseline 对照。Probe reward trap (C2) 是最有价值的贡献，但整体实验范围（单一行为、单一模型、2 seeds）限制了论文的影响力。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 352 · 2026-05-22T14:07:15.189074+00:00_

Reviewer 2 报告已收到（Overall 3.0 / Findings）。等待 Reviewer 1 返回初审报告，之后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director"
}
```

</details>

---


## Round 28

## Round 28

6 recorded events


### User

_source line 353 · 2026-05-22T14:08:08.231148+00:00_

[Reviewer 1 审稿意见]:
## 总体评分

**Overall**: 3.0 — Findings（可被 Findings 接收）
**一句话总结**: 研究问题重要、failure mode 分析有洞见，但 GRPO group_size=2 和 80-84% truncation 构成严重 confound，无法确定失败源自 d_syc 的本质局限还是次优实验配置。

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3/5 (Acceptable) | 主要 claims 有部分支持，但 group_size=2 和 truncation 两个 confound 使核心负面结论的因果归因不成立；probe trap (C2) 在 SFT 设定下独立于 GRPO 超参，是可靠发现 |
| Excitement | 3/5 (Interesting) | "discriminability ≠ reward utility" 的概念框架有价值，probe reward trap 及 behavioral-before-distributional collapse 的发现具有实践意义，但单一 case study 限制泛化 |
| Reproducibility | 3/5 | 超参数在 Table 5 / Appendix A 中披露完整，但代码和数据 "upon acceptance"，reviewer 无法独立验证关键数字 |
| Confidence | 4/5 | 仔细通读全文，熟悉 representation engineering、GRPO 和 sycophancy 相关文献 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] **GRPO group_size=2 构成致命 confound，论文核心因果归因不成立**
- 具体位置：Section 2.5 (line "GRPO uses a group size of 2")、Table 5 (footnote d)、Limitations
- 问题：论文使用 group_size=2，远低于典型值 8-64 (Shao et al., 2024)。Group size=2 意味着 GRPO 的 advantage estimation 极度噪声化——每个 group 只有两个 completion 进行相对排序，几乎等同于抛硬币。关键证据：**R₃-only GRPO（完全不使用 d_syc 的纯行为奖励）同样基本失败**（仅 4/27 checkpoints 超过 vanilla，SyconScore 0.143 vs vanilla 0.134），这强烈暗示问题出在 GRPO 优化配置本身，而非 d_syc。论文在 Limitations 中承认了这个 confound 并指出 probe trap (C2) 独立于 group_size，但 GRPO 相关的所有失败（F1a-F1d, F3, R₃-only）都可能被这一 confound 解释。
- 为什么影响接收：标题声称 "Why Sycophancy Directions **Fail** as GRPO Rewards"，但如果换用 group_size=8 或 16 后 d_syc 能成功，该结论完全翻转。仅凭 group_size=2 的实验无法支撑标题中的因果性声明。
- 建议修改方向：(1) 在 group_size=8 或 16 下复现至少一个 cosine 和一个 probe formulation；(2) 如果计算资源不允许，将标题和 claims 降级为 "under constrained optimization settings" 的条件性结论；(3) 解释为什么 R₃-only GRPO 也失败——这实际上削弱而非支持论文论点。

**N2** [critical] **80-84% truncation rate 严重损害奖励信号有效性**
- 具体位置：Appendix A ("All GRPO experiments use max_completion_length=256, resulting in 80–84% truncation of multi-turn responses")
- 问题：论文称 "this setting is shared across all conditions and does not affect relative comparisons" 以及 "response-level decisions typically manifest within the first 100–200 tokens"。但后一个 claim 没有任何实证支持——论文未提供 token-level 分析证明 sycophantic 行为在前 200 tokens 内完全可辨。在 80-84% 被截断的情况下，d_syc 奖励是基于不完整响应计算的，这可能系统性地扭曲奖励信号。更重要的是，如果 cosine gap (0.098, Section 4) 本就极小，truncation 引入的噪声可能完全淹没信号。
- 为什么影响接收：论文将 cosine gap 过窄归因于 d_syc 的内在局限（"semantic limitation"），但同样可能是 truncation 导致激活不完整，从而人为压缩了 gap。因果归因再次不成立。
- 建议修改方向：(1) 提供 truncation vs non-truncation 的 AUROC/cosine gap 对比；(2) 或在 max_completion_length=512/1024 下验证 cosine gap 是否仍然过窄。

**N3** [critical] **仅 2 random seeds 不足以支撑负面结论**
- 具体位置：Limitations ("We report GRPO results from two random seeds")
- 问题：对于一个以负面结论为核心贡献的论文，2 个 seeds 提供的统计证据极薄。Table 4 显示两个 seed 之间的差异不小（seed 1 peak SyconScore 0.153 at step 6500 vs seed 2 peak 0.143 at step 4000），crash onset 差 ~2,500 步。在 RL 训练固有的高方差下，2 seeds 无法区分 "d_syc 本质上不能工作" 和 "这两个特定 seed 恰好失败了"。
- 为什么影响接收：论文的核心贡献是负面结论（"every tested formulation fails"）。负面结论需要比正面结论更高的统计门槛，因为读者需要排除 "实验做得不够好" 这一竞争假说。2 seeds 不足以排除。
- 建议修改方向：增加到至少 5 个 seeds，报告 mean ± std，并进行 bootstrap 或 permutation test 确认零假设（"GRPO with d_syc performs no better than vanilla"）的 p-value。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] **ACT vs GRPO 对比被 5+ 维度差异严重 confound**
- 具体位置：Section 6 (paragraph "Observational comparison: ACT vs. GRPO")、Table 5
- 问题：论文承认 ACT 和 GRPO 至少在 5 个维度上不同（supervision granularity, loss family, training data format, optimization dynamics, LoRA capacity），但仍将 ACT 的成功与 GRPO 的失败并列比较，暗示 per-token supervision 是关键因素。在如此多 confound 下，任何一个差异都可能是 ACT 成功的原因（例如，ACT 使用 7 个 LoRA modules 共 ~1.75x 参数量，或 grad clipping=1.0，或 LoRA alpha=128 vs 64）。论文标记此比较为 "observational" 是好的，但在 Section 6 的段落标题 "Scalar reward limitation (observational)" 中，仍将其作为一个独立发现呈现。
- 建议：(1) 做至少一个 controlled ablation（例如在 GRPO 中加入 per-token d_syc loss 但保持其他不变）；(2) 或将 ACT 比较明确降级为 "motivation for future work" 而非 finding。

**W2** [warning] **标题 overclaim——"Why ... Fail" 暗示因果解释，但实验仅提供 single case study 的描述性证据**
- 具体位置：标题、Section 6 标题 "Discriminability ≠ Reward Utility"
- 问题：标题使用 "Why" 暗示提供了因果解释，但论文实际上只在一个模型 (Qwen3-8B)、一个 RL 算法 (GRPO with group_size=2)、一个方向 (d_syc from 181 GPT-4.1 pairs) 上做了实验。Section 6 标题将 "discriminability ≠ reward utility" 提升为一般性原则，但证据来自 single case study。论文中引用的 Zhang et al. (2026) 和 Wu and Tang (2026) 的对比论证是方向正确的，但不能替代本文自身的实验覆盖面。
- 建议：(1) 标题改为条件性表述，如 "When Sycophancy Directions Fail as GRPO Rewards: A Case Study"；(2) Section 6 标题改为 "Evidence that Discriminability May Not Imply Reward Utility"。

**W3** [warning] **181 对 contrastive pairs 的 evidence strength 标注缺乏人类 IAA**
- 具体位置：Section 2.1、Limitations
- 问题：Evidence strength 的三级标注（weak/medium/strong）由 GPT-4.1 单一标注者完成，无人类 inter-annotator agreement。论文在 Limitations 中承认了这一点。对于 discriminability 分析（Figure 1, Table 1），annotation 质量直接影响 AUROC 的 evidence-stratified 分析的可信度——如果 GPT-4.1 的 weak/medium/strong 划分不准确，evidence gradient（0.675 → 0.883 → 0.929）可能是 annotation artifact。
- 建议：抽样 50 对做人类标注，报告 Cohen's κ 或 Fleiss' κ。

**W4** [warning] **ACT seed 2 仅完成 4/16 checkpoints 评估——不应作为证据呈现**
- 具体位置：Table 4 (footnote ‡)、Section 6
- 问题：ACT seed 2 标注为 "ongoing; 4/16 ckpts evaluated, all > vanilla"。25% 的评估完成度不构成可靠证据，且 "all > vanilla" 可能存在 selection bias（如果前 4 个 checkpoints 是 cherry-picked）。论文多次引用 "seed 2: 4/4 ongoing" 作为 ACT 成功的支撑证据，但这 4 个点可能恰好是 ACT 表现最好的阶段。
- 建议：(1) 完成全部 16 checkpoints 的评估后再投稿；(2) 如果无法完成，删除 ACT seed 2 相关数据和讨论，仅基于 seed 1 报告。

**W5** [warning] **Cross-seed rank correlation ρ≈0.33 的统计报告不充分**
- 具体位置：Section 6 ("Cross-seed rank correlation is ≈1.0 during early training (steps 1000–3000) but drops to ρ≈0.33 (n.s.) after step 4000")
- 问题：论文未说明 (1) correlation 的 N 是多少（即多少个 checkpoints 参与排序），(2) 如何划分 "early" 和 "late" 窗口，(3) ρ≈1.0 是在 N=3 上计算的还是更多。如果 early window 只有 3 个 checkpoints，ρ=1.0 几乎是必然的（3 点的 Spearman 只能取 1.0, 0.5, -0.5, -1.0）。Late window 的 ρ≈0.33 (n.s.) 也因 N 过小而无统计功效。论文正确标注了 "n.s." 但仍将此作为 "stochastic divergence" 的证据呈现。
- 建议：报告 exact N、p-value、和 confidence interval；如果 N<10，承认统计功效不足以支撑任何结论。

**W6** [warning] **R₃-only GRPO 在 Table 4 中缺少 ToF 和 NoF 的分项数据**
- 具体位置：Table 4（R₃-only GRPO 行，ToF 和 NoF 列显示 "--"）
- 问题：Section 6 文字声称 R₃-only GRPO "exhibits the same stubbornness pattern (high NoF, near-zero ToF)"，但 Table 4 未报告这些数字。对于论文的关键论证——"即使移除 d_syc，纯行为奖励下的 GRPO 也表现出相同的 stubbornness pattern"——这些数字是必要的。
- 建议：在 Table 4 中填充 R₃-only GRPO 的 ToF 和 NoF 值。

---

## 小问题（不影响接收）

1. **数字一致性**：Abstract 和正文在 R₃-only checkpoints 总数上可能存在 26 vs 27 的微小不一致（需作者确认）。PDF 第 1 页 abstract 部分似乎显示 "4 of 26"，但 Introduction 和 Section 6 使用 "4 of 27"。
2. **SyconScore 定义位置**：SyconScore 首次出现在 Section 2.5，但 harmonic mean 选择而非 arithmetic mean 的 justification 仅一句话带过。虽然在 supplementary materials 中提供了 arithmetic mean 结果，但正文应简要说明 harmonic mean 更严格惩罚单侧极端的理由。
3. **Stubbornness taxonomy (Appendix B)**：三种失败模式（sycophantic stubbornness 24%, deliberation traps 29%, evidence-graded hedging 百分比未报告）的百分比加起来不到 100%，剩余比例是什么？
4. **写作小问题**：Table 2 标题中 "GRPO with R = w₁·R₁ + w₃·R₃" 使用了 R₁ 和 R₃ 但未使用 R₂，可能困扰读者。

---

## 主要优势

1. **研究问题重要且及时**：representation engineering 越来越多地被用于 reward design，本文提出的 "discriminability ≠ utility" 框架是对该领域的有价值警示。
2. **系统性 failure mode 分析**：6 种配置形成诊断链（F1a→F1b→F1c→F1d→F2→F3），每种解决前一种的 failure mode 但暴露更深层问题，论证结构清晰。
3. **Probe reward trap 发现有原创性**：behavioral death ($\tof=0$) 发生在 distributional collapse (entropy drop) 之前 1,300 步的发现（Table 3, Figure 2）对 RL alignment 实践有直接价值——它表明 entropy-based early stopping 不足以检测 reward hacking。该发现在 SFT 设定下取得，不受 GRPO hyperparameter 的 confound 影响。
4. **Cross-model validation**：d_syc 的 discriminability 在 Qwen3-8B 和 Llama-3-8B 上均得到验证（Table 1），evidence-strength gradient 在两个模型上一致。
5. **Limitations 诚实全面**：论文坦承了 group_size=2、truncation、2 seeds、incomplete ACT seed 2、无人类 IAA 等所有主要局限，这是学术诚实的体现。

---

## 缺失的参考文献

论文的相关工作覆盖合理。可考虑补充：
- Perez et al. (2022) "Discovering Language Model Behaviors with Model-Written Evaluations" — 早期 sycophancy 量化方法
- Rafailov et al. (2023) DPO — 作为 GRPO 之外的另一类 RL 方法讨论 alternatives

---

## 总结

本文的核心洞见（representation discriminability 不保证 RL reward utility）有价值，probe reward trap 的发现对 alignment 实践有实际意义。但 GRPO group_size=2 和 80-84% truncation 这两个 confound 使得论文无法可靠区分 "d_syc 本质上不能做 GRPO reward" 和 "实验配置不够好"。R₃-only GRPO 也基本失败这一事实进一步支持后者。建议增加 group_size=8/16 的实验和更多 seeds 后重新提交，如果结论不变，论文将显著增强。当前状态适合 Findings。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 354 · 2026-05-22T14:08:46.610573+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应：对每个 Must-Fix 和 Should-Fix 问题标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 完整审稿意见\n\n**Overall**: 3.0 / 5（Findings）\n\n### Must-Fix 问题\n\n**N1** [critical] Group size=2 严重削弱 C1 的可信度\n- GRPO group size=2 远低于典型范围 8-64。论文声称 C2 probe trap 独立于 GRPO hyperparameters，但 C1 的核心结论——\"Every tested GRPO formulation fails\"——在 group size=2 条件下可能主要反映 GRPO 在极端 hyperparameter 下的不稳定性，而非 d_syc 的根本缺陷。如果增大 group size 后 d_syc 能成功，论文核心 thesis 完全翻转。建议至少在一个 formulation 上测试 group size=8/16。\n\n**N2** [critical] 标题和 framing 过度泛化，与证据范围不匹配\n- 标题 \"Discriminability Without Utility\" 暗示一般性原则，但证据仅来自一种行为属性（sycophancy）、一种 RL 算法（GRPO）、一种主要模型（Qwen3-8B）、极小 group size(2)。Wu & Tang (2026) 展示 representation engineering 在 reward hacking detection 中成功（100% accuracy），与本文负面结论直接对比，论文需更精确界定 claim 适用范围。建议标题限定到 sycophancy 和/或 GRPO。\n\n**N3** [critical] 缺乏与标准 RM-based GRPO 的对比基线\n- 缺少关键对照：标准 reward model（如 trained classifier 或 LLM-as-judge）的 GRPO 在同一 task 上是否能成功？如果标准 RM 也失败，问题在 task/setup 而非 d_syc；如果成功，更有力支持 \"discriminability ≠ utility\"。建议添加 LLM-judge-based GRPO baseline。\n\n### Should-Fix 问题\n\n**W1** [warning] Wu & Tang (2026) 对比论证缺乏定量分析\n- AUROC 0.827 显示不错的可分性，但论文未定量验证 sycophancy 的 d_syc 是否缺乏 Wu & Tang 所需的 geometric separability。建议定量比较两种 direction 的 geometric properties。\n\n**W2** [warning] CRAFT 和 Latent-GRPO 讨论过于简略\n- 这两个工作都使用 latent-space signal 做 RL 训练，与本文核心主题直接相关，但各只有半句话。应讨论为什么这些方法成功而本文方法失败。\n\n**W3** [warning] 仅2个 random seed 的统计说服力不足\n- 2 seeds 不足以建立统计显著性。两条轨迹定性一致但定量差异大（crash onset 差 ~2500 步）。建议增加到 3-5 seeds 或措辞更谨慎。\n\n**W4** [warning] DPO/KTO 作为替代方案未做实验探索\n- d_syc 可直接生成 preference pairs，DPO/KTO 是自然替代方案。仅列为 open question 降低完整性。建议至少测试一种 preference-based 方法。\n\n**W5** [warning] 缺少 Process Reward Model (PRM) 讨论\n- 论文 reward 是 outcome-level。PRM 提供 per-step reward，可能缓解 d_syc 的局限。论文未讨论 PRM 视角。\n\n### 小问题\n- 术语交替使用 \"behavioral collapse\" 和 \"behavioral death\"\n- Table 3 排版略乱\n- Section 6 标题直接用等式不太规范\n- Figure 1 字体偏小\n\n### 主要优势\n1. 系统性实验设计（6种配置）\n2. Probe reward trap (C2) 有实用价值\n3. Cross-model 验证\n4. Mechanistic 分析有深度\n5. 写作清晰\n6. 格式合规"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应：对每个 Must-Fix 和 Should-Fix 问题标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 完整审稿意见\n\n**Overall**: 3.0 / 5（Findings）\n\n### Must-Fix 问题\n\n**N1** [critical] Group size=2 严重削弱 C1 的可信度\n- GRPO group size=2 远低于典型范围 8-64。论文声称 C2 probe trap 独立于 GRPO hyperparameters，但 C1 的核心结论——\"Every tested GRPO formulation fails\"——在 group size=2 条件下可能主要反映 GRPO 在极端 hyperparameter 下的不稳定性，而非 d_syc 的根本缺陷。如果增大 group size 后 d_syc 能成功，论文核心 thesis 完全翻转。建议至少在一个 formulation 上测试 group size=8/16。\n\n**N2** [critical] 标题和 framing 过度泛化，与证据范围不匹配\n- 标题 \"Discriminability Without Utility\" 暗示一般性原则，但证据仅来自一种行为属性（sycophancy）、一种 RL 算法（GRPO）、一种主要模型（Qwen3-8B）、极小 group size(2)。Wu & Tang (2026) 展示 representation engineering 在 reward hacking detection 中成功（100% accuracy），与本文负面结论直接对比，论文需更精确界定 claim 适用范围。建议标题限定到 sycophancy 和/或 GRPO。\n\n**N3** [critical] 缺乏与标准 RM-based GRPO 的对比基线\n- 缺少关键对照：标准 reward model（如 trained classifier 或 LLM-as-judge）的 GRPO 在同一 task 上是否能成功？如果标准 RM 也失败，问题在 task/setup 而非 d_syc；如果成功，更有力支持 \"discriminability ≠ utility\"。建议添加 LLM-judge-based GRPO baseline。\n\n### Should-Fix 问题\n\n**W1** [warning] Wu & Tang (2026) 对比论证缺乏定量分析\n- AUROC 0.827 显示不错的可分性，但论文未定量验证 sycophancy 的 d_syc 是否缺乏 Wu & Tang 所需的 geometric separability。建议定量比较两种 direction 的 geometric properties。\n\n**W2** [warning] CRAFT 和 Latent-GRPO 讨论过于简略\n- 这两个工作都使用 latent-space signal 做 RL 训练，与本文核心主题直接相关，但各只有半句话。应讨论为什么这些方法成功而本文方法失败。\n\n**W3** [warning] 仅2个 random seed 的统计说服力不足\n- 2 seeds 不足以建立统计显著性。两条轨迹定性一致但定量差异大（crash onset 差 ~2500 步）。建议增加到 3-5 seeds 或措辞更谨慎。\n\n**W4** [warning] DPO/KTO 作为替代方案未做实验探索\n- d_syc 可直接生成 preference pairs，DPO/KTO 是自然替代方案。仅列为 open question 降低完整性。建议至少测试一种 preference-based 方法。\n\n**W5** [warning] 缺少 Process Reward Model (PRM) 讨论\n- 论文 reward 是 outcome-level。PRM 提供 per-step reward，可能缓解 d_syc 的局限。论文未讨论 PRM 视角。\n\n### 小问题\n- 术语交替使用 \"behavioral collapse\" 和 \"behavioral death\"\n- Table 3 排版略乱\n- Section 6 标题直接用等式不太规范\n- Figure 1 字体偏小\n\n### 主要优势\n1. 系统性实验设计（6种配置）\n2. Probe reward trap (C2) 有实用价值\n3. Cross-model 验证\n4. Mechanistic 分析有深度\n5. 写作清晰\n6. 格式合规"
  }
}
```

</details>

---


### Tool result

_source line 355 · 2026-05-22T14:09:07.861849+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_056796cf71f839be40019e5f1a11791b:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_056796cf71f839be40019e5f1a11791b:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 21251
}
```

</details>

---
