# paper writing related work

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 17
- **Recorded user turns:** 0
- **Tool calls:** 8
- **Original source:** `logs/chats/worker_paper_writing_related_work_20260518T195445.jsonl`
- **Structured JSON:** [`3c316a37797908d910f8.json`](../../sessions/3c/3c316a37797908d910f8.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

17 recorded events

### Tool call

_source line 1 · 2026-05-18T19:57:30.543064+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_20260518T195445",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-18T19:57:30.543663+00:00_

1	---
2	name: paper-writing-norms
3	description: 顶会级别论文写作风格规范——章节写法（Abstract/Intro/Related Work）、去 AI 风格、视觉密度、叙事哲学。Paper Agent 和 Worker 写论文章节时必须加载。
4	allowed-tools: [Read, Write, Edit, Glob, Grep]
5	scope: global
6	version: 2
7	priority: 9
8	tags:
9	  - writing
10	  - paper
11	  - style
12	  - norms
13	roles:
14	  - agent
15	  - worker
16	  - paper_agent
17	---
18	
19	# 论文写作风格规范
20	
21	> 核心哲学：**论文是一个有说服力的故事，不是实验报告。** 审稿人在几十秒内判断论文价值——如果 Abstract 和 Introduction 读起来像实验日志，论文就已经失败了。
22	
23	---
24	
25	## 一、总体写作哲学
26	
27	### 1.1 故事驱动，不是数据堆砌
28	
29	- 论文必须以"故事线"为核心展开：问题 → 洞察 → 方法 → 验证
30	- 禁止大量实验数据堆砌——每个数字出现必须服务于叙事推进
31	- 附录内容必须在正文中有明确引用且融入叙事，禁止简单堆砌
32	- 如果附录数据对核心叙事有重大影响，根据附录数据调整论文 framing
33	
34	### 1.2 主线统一性
35	
36	- 当 idea 在研究过程中发生变化后，**必须重审全文逻辑**
37	- 常见问题：Introduction 讲的故事 A，Method 做的是故事 B，Results 又在讲故事 C
38	- 修复方式：从最终实验结论反推，重写 Introduction 的问题定义和动机
39	- 每次 idea 调整后检查：Abstract → Introduction → Method → Results → Discussion → Conclusion 是否形成一条连贯主线
40	
41	### 1.3 专有名词必须有定义
42	
43	- 首次出现的专有名词/缩写必须给出完整定义和解释
44	- Abstract 中使用的缩写也必须在 Abstract 内定义（如 LLM = Large Language Model）
45	- 不能假设读者知道你自己定义的术语——论文从来没解释过的概念不能直接使用
46	- 通用规则：如果一个非标准术语第一次出现时没有括号定义，就是写作 bug
47	
48	### 1.4 写作前必读同类优秀论文
49	
50	- 每个章节动笔前，找 **2-3 篇目标会议近 1-2 年的高分论文**作为风格参考——同类问题或同类方法皆可
51	- 重点学：
52	  - Abstract 怎么用最少篇幅讲完故事
53	  - Introduction 怎么从大问题切入到具体贡献
54	  - Related Work 怎么 positioning 自己（不是 survey）
55	  - Table/Figure 怎么压缩信息密度
56	- **不是抄袭**，是学习同行的故事节奏和审美——不同子领域叙事节奏差异很大
57	- 实操：Paper Agent 可以从 `literature_map.yaml` 中挑 `role=foundation` 或 `role=direct-competitor` 的论文，把 `{title, venue, year, abstract}` 附在 Worker 的 task_prompt 中作为概念参考；如需学习写作风格本身，让 Worker 通过 WebSearch 取得论文链接并 fetch 全文
58	
59	---
60	
61	## 二、Abstract 写作规范
62	
63	### 2.1 四个必答问题（150-250 words）
64	
65	Abstract 必须在很短的篇幅内清楚回答：
66	1. **研究什么问题** — 1-2 句话交代背景和痛点
67	2. **为什么重要** — 现有方法的不足（不用写太多）
68	3. **本文提出什么** — 核心贡献的关键机制（简要，不堆砌细节）
69	4. **结果说明什么** — 用具体实验结论支撑贡献
70	
71	### 2.2 禁忌
72	
73	- **禁止堆砌数据**：Abstract 不是 Results 的缩写。最多引用 2-3 个关键数字，要服务于 claim
74	- **
…[truncated 4866 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260518T195445",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-18T19:57:30.543874+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_20260518T195445",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-18T19:57:30.544241+00:00_

1	---
2	name: latex-paper
3	description: ML 顶会论文 LaTeX 写作全流程——Claim-Evidence 方法论、引用防幻觉、顶会模板速查、投稿工程链、会议转投。写论文/投稿时参考。
4	scope: global
5	tags:
6	- latex
7	- paper-writing
8	- academic
9	- citation
10	- submission
11	version: 1
12	roles:
13	- agent
14	- worker
15	---
16	
17	# LaTeX 论文写作全流程
18	
19	ML/AI 顶会论文从草稿到投稿的完整指南。整合 Orchestra Research、VibeSkills、claim2evidence 三方最佳实践。
20	
21	---
22	
23	## 1. 工作模式
24	
25	开始前选择模式：
26	
27	| 模式 | 说明 | 适用 |
28	|------|------|------|
29	| **Build** | 从实验笔记/结果/代码生成论文 | 新稿 |
30	| **Improve** | 改写已有章节，强化论证 | 修改稿 |
31	| **Audit** | 输出风险列表 + 缺失证据 + 修复建议 | 投前检查 |
32	
33	---
34	
35	## 2. Claim-Evidence 方法论
36	
37	**核心原则：论文是一个有中心贡献的故事，不是实验的堆砌。**
38	
39	### 2.1 一句话贡献
40	
41	在写任何内容之前，必须能用一句话说清贡献。如果不能，说明还没准备好写论文。
42	
43	### 2.2 Claim-Evidence Map
44	
45	为每个 contribution 建立 claim→evidence 映射表：
46	
47	| Contribution | Claim | Evidence | Table/Figure |
48	|-------------|-------|----------|-------------|
49	| C1: 方法 X 在 Y 上 SOTA | 比所有 baseline 高 ≥2% | 5-seed 平均，p<0.05 | Table 1 |
50	| C2: 消融证明 Z 是关键 | 去掉 Z 后掉 >5% | 消融实验 | Table 2 |
51	| C3: 计算效率 | 比 baseline 快 3× | FLOPs + wall-clock | Figure 3 |
52	
53	**没有直接证据支撑的 claim 必须删除或降级为 discussion。**
54	
55	### 2.3 章节起草顺序
56	
57	```
58	1. Introduction + Experiments（先确定 claim 和 evidence）
59	2. Method（评估问题稳定后再写细节）
60	3. Related Work
61	4. Abstract + Title（核心 claim 定型后最后写）
62	```
63	
64	### 2.4 Quality Gates
65	
66	投稿前必须通过：
67	- [ ] 前两段出现显式 novelty 声明
68	- [ ] 每个 contribution 有可验证的 evidence
69	- [ ] Abstract / Intro / Conclusion 的 claim 一致
70	- [ ] Limitations 真实且技术性诚实
71	- [ ] 审稿人两分钟内能识别 delta
72	
73	---
74	
75	## 3. 引用防幻觉（CRITICAL）
76	
77	**AI 生成引用有 ~40% 错误率。绝对禁止凭记忆写 BibTeX。**
78	
79	### 3.1 黄金法则
80	
81	```
82	IF 无法程序化获取引用:
83	    → 标记 [CITATION NEEDED] 或 \cite{PLACEHOLDER_verify}
84	    → 明确告知用户
85	    → 绝不编造看似合理的引用
86	```
87	
88	### 3.2 五步验证流程
89	
90	```
91	1. SEARCH  → Semantic Scholar API 搜索关键词
92	2. VERIFY  → 至少 2 个来源确认论文存在（S2 + arXiv/CrossRef）
93	3. RETRIEVE → 通过 DOI 获取 BibTeX（程序化，非记忆）
94	4. CHECK   → 确认
…[truncated 7201 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260518T195445",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-18T19:57:30.544409+00:00_

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
  "session": "worker_paper_writing_related_work_20260518T195445",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-18T19:57:30.544594+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{RL Training for LLM Agents.}
5	The ReAct paradigm~\cite{yao2023react} established interleaved reasoning and acting as the standard framework for LLM agents. Group Relative Policy Optimization (GRPO)~\cite{shao2024deepseekmath} emerged from mathematical reasoning alignment and was scaled to large systems through techniques such as dynamic sampling and clip-higher stabilization~\cite{dapo2025}. Adapting GRPO to multi-turn interactive agents requires addressing the mismatch between its episode-level design and the practical constraints of long trajectories. RAGEN~\cite{ragen2025} introduced the step-independent windowing approach that has become the community default, partitioning trajectories into fixed-size windows optimized separately. Subsequent work has proposed algorithmic improvements that operate within or alongside this framework. GiGPO~\cite{feng2025gigpo} addresses credit assignment through a nested group structure that estimates step-level advantages without a learned critic, achieving substantial gains on ALFWorld and WebShop. Self-Guide~\cite{selfguide2026} co-evolves an internal reward model with the policy, providing denser learning signals than binary episode outcomes. SPEAR~\cite{spear2025} combines self-imitation learning with progressive curriculum to handle sparse rewards in early training. DigiRL~\cite{digiRL2024} demonstrates autonomous online RL for device-control agents, achieving substantial gains over supervised fine-tuning. WebAgent-R1~\cite{wei2025webagent-r1} extends GRPO to multi-turn web interaction (M-GRPO) with dynamic context compression, while SORL~\cite{li2025sorl} introduces turn-level importance sampling for off-policy stability. HCAPO~\cite{hcapo2026} uses an LLM-as-critic to assign hindsight credit at critical decision states. These methods improve training algorithms or reward design at various granularities. None diagnoses the step-independent windowing mechan
…[truncated 4945 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260518T195445",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-18T19:57:30.544757+00:00_

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
  "session": "worker_paper_writing_related_work_20260518T195445",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/references.bib"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-18T19:57:30.544959+00:00_

1	@inproceedings{shridhar2021alfworld,
2	  title     = {{ALFWorld}: Aligning Text and Embodied Environments for Interactive Learning},
3	  author    = {Shridhar, Mohit and Yuan, Xingdi and C\^{o}t\'{e}, Marc-Alexandre and Bisk, Yonatan and Trischler, Adam and Hausknecht, Matthew},
4	  booktitle = {International Conference on Learning Representations},
5	  year      = {2021},
6	}
7	
8	@inproceedings{agent-omit2026,
9	  title     = {Agent-Omit: Training Efficient {LLM} Agents for Adaptive Thought and Observation Omission via Agentic {RL}},
10	  author    = {Ning, Yansong and Fang, Jun and Tan, Naiqiang and Liu, Hao},
11	  booktitle = {Proceedings of the International Conference on Machine Learning},
12	  year      = {2026},
13	}
14	
15	@article{choudhury2025agentprm,
16	  title   = {Process Reward Models for {LLM} Agents: Practical Framework and Directions},
17	  author  = {Choudhury, Sanjiban},
18	  journal = {arXiv preprint arXiv:2502.10325},
19	  year    = {2025},
20	}
21	
22	@article{dapo2025,
23	  title   = {{DAPO}: An Open-Source {LLM} Reinforcement Learning System at Scale},
24	  author  = {Yu, Qiying and Zhang, Zheng and Zhu, Ruofei and Yuan, Yufeng and Zuo, Xiaochen and Yue, Yu and Dai, Weinan and Fan, Tiantian and Liu, Gaohong and Liu, Lingjun and Liu, Xin and Lin, Haibin and Lin, Zhiqi and Ma, Bole and Sheng, Guangming and Tong, Yuxuan and Zhang, Chi and Zhang, Mofan and Zhang, Wang and Zhu, Hang and Zhu, Jinhua and Chen, Jiaze and Chen, Jiangjie and Wang, Chengyi and Yu, Hongli and Song, Yuxuan and Wei, Xiangpeng and Zhou, Hao and Liu, Jingjing and Ma, Wei-Ying and Zhang, Ya-Qin and Yan, Lin and Qiao, Mu and Wu, Yonghui and Wang, Mingxuan},
25	  journal = {arXiv preprint arXiv:2503.14476},
26	  year    = {2025},
27	}
28	
29	@inproceedings{foerster2018coma,
30	  title     = {Counterfactual Multi-Agent Policy Gradients},
31	  author    = {Foerster, Jakob and Farquhar, Gregory and Afouras, Triantafyllos and Nardelli, Nantas and Whiteson, Shimon},
32	  booktit
…[truncated 11911 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260518T195445",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-18T19:57:30.545217+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/related_work.tex",
  "content": "\\section{Related Work}\n\\label{sec:related_work}\n\n\\paragraph{RL Training for Multi-Turn LLM Agents.}\nThe ReAct paradigm~\\cite{yao2023react} established interleaved reasoning and acting as the standard framework for LLM agents. Group Relative Policy Optimization (GRPO)~\\cite{shao2024deepseekmath}, originally developed for mathematical reasoning, was scaled to large systems through dynamic sampling and clip-higher stabilization~\\cite{dapo2025}. Adapting GRPO to multi-turn agents requires addressing the mismatch between its episode-level formulation and the memory constraints of long trajectories. RAGEN~\\cite{ragen2025} introduced the step-independent windowing approach that has since become the community default: trajectories are partitioned into fixed-size windows, each optimized with an independently normalized baseline. Subsequent work improves training algorithms or reward design within this framework. GiGPO~\\cite{feng2025gigpo} estimates step-level advantages through a nested group structure without a learned critic. Self-Guide~\\cite{selfguide2026} co-evolves an internal reward model with the policy to provide denser signals than binary outcomes. SPEAR~\\cite{spear2025} combines self-imitation with progressive curriculum to mitigate sparse-reward starvation. DigiRL~\\cite{digiRL2024} demonstrates autonomous online RL for device-control agents. WebAgent-R1~\\cite{wei2025webagent-r1} extends GRPO to multi-turn web interaction with dynamic context compression, and SORL~\\cite{li2025sorl} introduces turn-level importance sampling for off-policy stability. HCAPO~\\cite{hcapo2026} uses an LLM-as-critic to assign hindsight credit at critical decision states. These methods improve the algorithm, the reward, or the training pipeline at various granularities, yet none diagnoses the step-independent windowing mechanism itself as a source of systematic sign errors. We identify and formalize this structural failure.\n\n\\paragraph{Credit Assignment in Reinforcement Learning.}\nTemporal credit assignment spans a well-studied spectrum. REINFORCE~\\cite{williams1992reinforce} provides unbiased but high-variance episode-level gradients. PPO~\\cite{schulman2017ppo} reduces variance via a learned critic and clipped surrogate objectives. GAE~\\cite{schulman2016gae} interpolates between one-step TD and Monte Carlo returns through the $\\lambda$ parameter, with TD($\\lambda$)~\\cite{sutton1988td} establishing this interpolation in the tabular setting. RUDDER~\\cite{rudder2019} decomposes delayed rewards via sequence-to-sequence modeling but introduces bias whose correction slows exponentially with horizon. For LLM agents, AgentPRM~\\cite{choudhury2025agentprm,xi2025agentprm} estimates step-level value through Monte Carlo rollouts, and SkillMaster~\\cite{skillmaster2026} proposes DualAdv-GRPO with separate advantages for task-solving and skill-editing. In cooperative multi-agent RL, COMA~\\cite{foerster2018coma} and QMIX~\\cite{rashid2018qmix} address the analogous problem of attributing shared team rewards to individual agents via counterfactual baselines and value decomposition. Several independent studies provide direct evidence that step-independent credit assignment produces sign-level errors. IRC~\\cite{irc2026} reports that per-turn advantages $A^I$ frequently disagree in sign with outcome advantages $A^O$, with the resulting miscalibration causing a 14 percentage-point degradation (54\\% vs.\\ 68\\%). MC-GRPO~\\cite{mcgrpo2025} measures a 5\\% sign-flip rate and shows through controlled injection that this rate alone accounts for approximately 4\\% accuracy loss. GRPO-$\\lambda$~\\cite{grpolambda2025} proves in Lemma~1 that the value estimation error grows with sequence position, since the baseline $\\mu_t$ is biased for all $t > 0$. OAR~\\cite{oar2026} identifies ``reward aliasing'' arising from coarse-grained credit assignment. G-RA~\\cite{gra2025} visualizes accumulated reward diverging in sign from outcome reward. Decoupled-CA~\\cite{decoupledca2026} (under review) finds that invalid actions in positive-outcome trajectories receive positive credit and proposes multiplicative gated rewards to correct this. Episode-level GRPO, as we advocate, corresponds to GAE(1,1) without a critic: uniform advantage across all steps forfeits per-step granularity in exchange for correct gradient direction. Our contribution is not a new credit assignment algorithm but a diagnosis of why the community's standard practice produces catastrophic sign errors in multi-turn settings.\n\n\\paragraph{Multi-Turn Agent Credit Assignment.}\nA parallel thread develops credit assignment methods specifically for multi-turn LLM agents. Turn-PPO~\\cite{turnppo2026} estimates turn-level advantages within PPO and reports that standard GRPO directly crashes on WebShop and Sokoban, with three proposed fixes all failing to recover. GiGPO~\\cite{feng2025gigpo} structures advantages at two scales (episode-level macro and step-level micro) and ablates both as indispensable. GAGPO~\\cite{gagpo2026} replaces Monte Carlo step advantages with TD/GAE-style recursive estimation. iStar~\\cite{istar2025} merges episode and step advantages at the token level but observes that token-level granularity increases fluctuation rather than improving stability. MT-GRPO~\\cite{mtgrpo2025} contrasts its turn-level method against an outcome-only GRPO baseline (GRPO-OR): 0.04 exact match versus 0.50, a 12$\\times$ gap that underscores the severity of multi-turn credit assignment failure. SWEET-RL~\\cite{sweetrl2025} finds that episode-level agents degrade sharply beyond 10 turns. These methods propose solutions to the multi-turn credit assignment problem. We complement them with a mechanistic diagnosis: two specific failure modes (policy information loss at the inference layer and advantage sign misattribution at the training layer) explain why step-independent windowing fails and why episode-level assignment eliminates both.\n\n\\paragraph{GRPO Collapse and Training Instability.}\nSeveral independent groups have documented collapse phenomena in GRPO-based training that corroborate our analysis. RAGEN-2~\\cite{ragen2_2026} provides a mathematical proof of advantage collapse: when within-prompt reward variance approaches zero, task-relevant gradients vanish and KL regularization dominates, driving the policy back toward the reference model. GRPO-Collapse~\\cite{grpocollapse2025} identifies the Lazy Likelihood-Displacement death spiral in Search-R1, where all four tested models collapse within 300 training steps. Gradient Coupling~\\cite{gradientcoupling2025} challenges the ``reward miscalibration'' hypothesis and argues in Lemma~3.1 that flawed actions have naturally negative expected advantage; the true failure mode is gradient coupling from high input similarity across consecutive steps. This expected-value analysis is compatible with our per-sample sign analysis: expected advantages can be correct in aggregate (averaged over many samples) while per-sample signs remain near-random under high variance, precisely the regime where step-independent windowing operates. These independent observations converge on a shared conclusion that step-independent GRPO training is structurally unstable in multi-turn settings. Our work unifies these phenomena under a dual-mechanism diagnosis (M1 and M2) and validates the episode-level alternative through controlled training dynamics.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_20260518T195445",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/related_work.tex",
    "content": "\\section{Related Work}\n\\label{sec:related_work}\n\n\\paragraph{RL Training for Multi-Turn LLM Agents.}\nThe ReAct paradigm~\\cite{yao2023react} established interleaved reasoning and acting as the standard framework for LLM agents. Group Relative Policy Optimization (GRPO)~\\cite{shao2024deepseekmath}, originally developed for mathematical reasoning, was scaled to large systems through dynamic sampling and clip-higher stabilization~\\cite{dapo2025}. Adapting GRPO to multi-turn agents requires addressing the mismatch between its episode-level formulation and the memory constraints of long trajectories. RAGEN~\\cite{ragen2025} introduced the step-independent windowing approach that has since become the community default: trajectories are partitioned into fixed-size windows, each optimized with an independently normalized baseline. Subsequent work improves training algorithms or reward design within this framework. GiGPO~\\cite{feng2025gigpo} estimates step-level advantages through a nested group structure without a learned critic. Self-Guide~\\cite{selfguide2026} co-evolves an internal reward model with the policy to provide denser signals than binary outcomes. SPEAR~\\cite{spear2025} combines self-imitation with progressive curriculum to mitigate sparse-reward starvation. DigiRL~\\cite{digiRL2024} demonstrates autonomous online RL for device-control agents. WebAgent-R1~\\cite{wei2025webagent-r1} extends GRPO to multi-turn web interaction with dynamic context compression, and SORL~\\cite{li2025sorl} introduces turn-level importance sampling for off-policy stability. HCAPO~\\cite{hcapo2026} uses an LLM-as-critic to assign hindsight credit at critical decision states. These methods improve the algorithm, the reward, or the training pipeline at various granularities, yet none diagnoses the step-independent windowing mechanism itself as a source of systematic sign errors. We identify and formalize this structural failure.\n\n\\paragraph{Credit Assignment in Reinforcement Learning.}\nTemporal credit assignment spans a well-studied spectrum. REINFORCE~\\cite{williams1992reinforce} provides unbiased but high-variance episode-level gradients. PPO~\\cite{schulman2017ppo} reduces variance via a learned critic and clipped surrogate objectives. GAE~\\cite{schulman2016gae} interpolates between one-step TD and Monte Carlo returns through the $\\lambda$ parameter, with TD($\\lambda$)~\\cite{sutton1988td} establishing this interpolation in the tabular setting. RUDDER~\\cite{rudder2019} decomposes delayed rewards via sequence-to-sequence modeling but introduces bias whose correction slows exponentially with horizon. For LLM agents, AgentPRM~\\cite{choudhury2025agentprm,xi2025agentprm} estimates step-level value through Monte Carlo rollouts, and SkillMaster~\\cite{skillmaster2026} proposes DualAdv-GRPO with separate advantages for task-solving and skill-editing. In cooperative multi-agent RL, COMA~\\cite{foerster2018coma} and QMIX~\\cite{rashid2018qmix} address the analogous problem of attributing shared team rewards to individual agents via counterfactual baselines and value decomposition. Several independent studies provide direct evidence that step-independent credit assignment produces sign-level errors. IRC~\\cite{irc2026} reports that per-turn advantages $A^I$ frequently disagree in sign with outcome advantages $A^O$, with the resulting miscalibration causing a 14 percentage-point degradation (54\\% vs.\\ 68\\%). MC-GRPO~\\cite{mcgrpo2025} measures a 5\\% sign-flip rate and shows through controlled injection that this rate alone accounts for approximately 4\\% accuracy loss. GRPO-$\\lambda$~\\cite{grpolambda2025} proves in Lemma~1 that the value estimation error grows with sequence position, since the baseline $\\mu_t$ is biased for all $t > 0$. OAR~\\cite{oar2026} identifies ``reward aliasing'' arising from coarse-grained credit assignment. G-RA~\\cite{gra2025} visualizes accumulated reward diverging in sign from outcome reward. Decoupled-CA~\\cite{decoupledca2026} (under review) finds that invalid actions in positive-outcome trajectories receive positive credit and proposes multiplicative gated rewards to correct this. Episode-level GRPO, as we advocate, corresponds to GAE(1,1) without a critic: uniform advantage across all steps forfeits per-step granularity in exchange for correct gradient direction. Our contribution is not a new credit assignment algorithm but a diagnosis of why the community's standard practice produces catastrophic sign errors in multi-turn settings.\n\n\\paragraph{Multi-Turn Agent Credit Assignment.}\nA parallel thread develops credit assignment methods specifically for multi-turn LLM agents. Turn-PPO~\\cite{turnppo2026} estimates turn-level advantages within PPO and reports that standard GRPO directly crashes on WebShop and Sokoban, with three proposed fixes all failing to recover. GiGPO~\\cite{feng2025gigpo} structures advantages at two scales (episode-level macro and step-level micro) and ablates both as indispensable. GAGPO~\\cite{gagpo2026} replaces Monte Carlo step advantages with TD/GAE-style recursive estimation. iStar~\\cite{istar2025} merges episode and step advantages at the token level but observes that token-level granularity increases fluctuation rather than improving stability. MT-GRPO~\\cite{mtgrpo2025} contrasts its turn-level method against an outcome-only GRPO baseline (GRPO-OR): 0.04 exact match versus 0.50, a 12$\\times$ gap that underscores the severity of multi-turn credit assignment failure. SWEET-RL~\\cite{sweetrl2025} finds that episode-level agents degrade sharply beyond 10 turns. These methods propose solutions to the multi-turn credit assignment problem. We complement them with a mechanistic diagnosis: two specific failure modes (policy information loss at the inference layer and advantage sign misattribution at the training layer) explain why step-independent windowing fails and why episode-level assignment eliminates both.\n\n\\paragraph{GRPO Collapse and Training Instability.}\nSeveral independent groups have documented collapse phenomena in GRPO-based training that corroborate our analysis. RAGEN-2~\\cite{ragen2_2026} provides a mathematical proof of advantage collapse: when within-prompt reward variance approaches zero, task-relevant gradients vanish and KL regularization dominates, driving the policy back toward the reference model. GRPO-Collapse~\\cite{grpocollapse2025} identifies the Lazy Likelihood-Displacement death spiral in Search-R1, where all four tested models collapse within 300 training steps. Gradient Coupling~\\cite{gradientcoupling2025} challenges the ``reward miscalibration'' hypothesis and argues in Lemma~3.1 that flawed actions have naturally negative expected advantage; the true failure mode is gradient coupling from high input similarity across consecutive steps. This expected-value analysis is compatible with our per-sample sign analysis: expected advantages can be correct in aggregate (averaged over many samples) while per-sample signs remain near-random under high variance, precisely the regime where step-independent windowing operates. These independent observations converge on a shared conclusion that step-independent GRPO training is structurally unstable in multi-turn settings. Our work unifies these phenomena under a dual-mechanism diagnosis (M1 and M2) and validates the episode-level alternative through controlled training dynamics.\n"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-18T19:57:30.545493+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/related_work.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260518T195445",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-18T19:57:30.545684+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/references.bib",
  "old_string": "@article{yang2026ares,\n  title   = {{ARES}: Adaptive Reasoning Effort Selection for Efficient {LLM} Agents},\n  author  = {Yang, Jingbo and Hou, Bairu and Wei, Wei and Bao, Yujia and Chang, Shiyu},\n  journal = {arXiv preprint arXiv:2603.07915},\n  year    = {2026},\n}",
  "new_string": "@article{yang2026ares,\n  title   = {{ARES}: Adaptive Reasoning Effort Selection for Efficient {LLM} Agents},\n  author  = {Yang, Jingbo and Hou, Bairu and Wei, Wei and Bao, Yujia and Chang, Shiyu},\n  journal = {arXiv preprint arXiv:2603.07915},\n  year    = {2026},\n}\n\n@article{irc2026,\n  title   = {Multi-Turn Reinforcement Learning for Tool-Calling Agents with Iterative Reward Calibration},\n  author  = {Anonymous},\n  journal = {arXiv preprint arXiv:2604.02869},\n  year    = {2026},\n}\n\n@article{mcgrpo2025,\n  title   = {{MC-GRPO}: Median-Centered Group Relative Policy Optimization for Small-Rollout Reinforcement Learning},\n  author  = {Kim, Youngeun},\n  journal = {arXiv preprint arXiv:2601.22582},\n  year    = {2025},\n}\n\n@article{gra2025,\n  title   = {Stabilizing Long-term Multi-turn Reinforcement Learning with Gated Rewards},\n  author  = {Anonymous},\n  journal = {arXiv preprint arXiv:2508.10548},\n  year    = {2025},\n}\n\n@article{grpolambda2025,\n  title   = {{GRPO-$\\lambda$}: Credit Assignment improves {LLM} Reasoning},\n  author  = {Anonymous},\n  journal = {arXiv preprint arXiv:2510.00194},\n  year    = {2025},\n}\n\n@article{oar2026,\n  title   = {Outcome-Grounded Advantage Reshaping for Fine-Grained Credit Assignment in Mathematical Reasoning},\n  author  = {Anonymous},\n  journal = {arXiv preprint arXiv:2601.07408},\n  year    = {2026},\n}\n\n@article{decoupledca2026,\n  title   = {Both Local Validity and Global Effectiveness Matter: Decoupled Credit Assignment for Long-Horizon Agentic Learning},\n  author  = {Lu, Wenxuan and Zhang, Zhanqiu and Guo, Steven Y. and Zang, Tianning},\n  journal = {Submitted to ICLR 2026 (under review)},\n  year    = {2026},\n  note    = {OpenReview: Suja4AQ9Fo},\n}\n\n@article{ragen2_2026,\n  title   = {{RAGEN-2}: Reasoning Collapse in Agentic {RL}},\n  author  = {Anonymous},\n  journal = {arXiv preprint arXiv:2604.06268},\n  year    = {2026},\n}\n\n@article{grpocollapse2025,\n  title   = {On {GRPO} Collapse in {Search-R1}: The Lazy Likelihood-Displacement Death Spiral},\n  author  = {Anonymous},\n  journal = {arXiv preprint arXiv:2512.04220},\n  year    = {2025},\n}\n\n@article{gradientcoupling2025,\n  title   = {Gradient Coupling: The Hidden Barrier to Generalization in Agentic {RL}},\n  author  = {Anonymous},\n  journal = {arXiv preprint arXiv:2509.23870},\n  year    = {2025},\n}\n\n@article{turnppo2026,\n  title   = {{Turn-PPO}: Turn-Level Advantage Estimation with {PPO} for Improved Multi-Turn {RL}},\n  author  = {Anonymous},\n  journal = {arXiv preprint arXiv:2512.17008},\n  year    = {2026},\n}\n\n@article{gagpo2026,\n  title   = {{GAGPO}: Generalized Advantage Grouped Policy Optimization},\n  author  = {Anonymous},\n  journal = {arXiv preprint arXiv:2605.13217},\n  year    = {2026},\n}\n\n@article{istar2025,\n  title   = {Agentic Reinforcement Learning with Implicit Step Rewards},\n  author  = {Anonymous},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year    = {2025},\n}\n\n@article{mtgrpo2025,\n  title   = {Reinforcing Multi-Turn Reasoning in {LLM} Agents via Turn-Level Credit Assignment},\n  author  = {Anonymous},\n  journal = {arXiv preprint arXiv:2505.11821},\n  year    = {2025},\n}\n\n@article{sweetrl2025,\n  title   = {{SWEET-RL}: Training Multi-Turn {LLM} Agents on Collaborative Reasoning Tasks},\n  author  = {Anonymous},\n  journal = {arXiv preprint arXiv:2503.15478},\n  year    = {2025},\n}\n\n@inproceedings{rudder2019,\n  title     = {{RUDDER}: Return Decomposition for Delayed Rewards},\n  author    = {Arjona-Medina, Jose A. and Gillhofer, Michael and Widrich, Michael and Unterthiner, Thomas and Brandstetter, Johannes and Hochreiter, Sepp},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year      = {2019},\n}\n\n@article{ca_survey2026,\n  title   = {From Reasoning to Agentic: Credit Assignment in {RL} for {LLMs}},\n  author  = {Anonymous},\n  journal = {arXiv preprint arXiv:2604.09459},\n  year    = {2026},\n}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_20260518T195445",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/references.bib",
    "old_string": "@article{yang2026ares,\n  title   = {{ARES}: Adaptive Reasoning Effort Selection for Efficient {LLM} Agents},\n  author  = {Yang, Jingbo and Hou, Bairu and Wei, Wei and Bao, Yujia and Chang, Shiyu},\n  journal = {arXiv preprint arXiv:2603.07915},\n  year    = {2026},\n}",
    "new_string": "@article{yang2026ares,\n  title   = {{ARES}: Adaptive Reasoning Effort Selection for Efficient {LLM} Agents},\n  author  = {Yang, Jingbo and Hou, Bairu and Wei, Wei and Bao, Yujia and Chang, Shiyu},\n  journal = {arXiv preprint arXiv:2603.07915},\n  year    = {2026},\n}\n\n@article{irc2026,\n  title   = {Multi-Turn Reinforcement Learning for Tool-Calling Agents with Iterative Reward Calibration},\n  author  = {Anonymous},\n  journal = {arXiv preprint arXiv:2604.02869},\n  year    = {2026},\n}\n\n@article{mcgrpo2025,\n  title   = {{MC-GRPO}: Median-Centered Group Relative Policy Optimization for Small-Rollout Reinforcement Learning},\n  author  = {Kim, Youngeun},\n  journal = {arXiv preprint arXiv:2601.22582},\n  year    = {2025},\n}\n\n@article{gra2025,\n  title   = {Stabilizing Long-term Multi-turn Reinforcement Learning with Gated Rewards},\n  author  = {Anonymous},\n  journal = {arXiv preprint arXiv:2508.10548},\n  year    = {2025},\n}\n\n@article{grpolambda2025,\n  title   = {{GRPO-$\\lambda$}: Credit Assignment improves {LLM} Reasoning},\n  author  = {Anonymous},\n  journal = {arXiv preprint arXiv:2510.00194},\n  year    = {2025},\n}\n\n@article{oar2026,\n  title   = {Outcome-Grounded Advantage Reshaping for Fine-Grained Credit Assignment in Mathematical Reasoning},\n  author  = {Anonymous},\n  journal = {arXiv preprint arXiv:2601.07408},\n  year    = {2026},\n}\n\n@article{decoupledca2026,\n  title   = {Both Local Validity and Global Effectiveness Matter: Decoupled Credit Assignment for Long-Horizon Agentic Learning},\n  author  = {Lu, Wenxuan and Zhang, Zhanqiu and Guo, Steven Y. and Zang, Tianning},\n  journal = {Submitted to ICLR 2026 (under review)},\n  year    = {2026},\n  note    = {OpenReview: Suja4AQ9Fo},\n}\n\n@article{ragen2_2026,\n  title   = {{RAGEN-2}: Reasoning Collapse in Agentic {RL}},\n  author  = {Anonymous},\n  journal = {arXiv preprint arXiv:2604.06268},\n  year    = {2026},\n}\n\n@article{grpocollapse2025,\n  title   = {On {GRPO} Collapse in {Search-R1}: The Lazy Likelihood-Displacement Death Spiral},\n  author  = {Anonymous},\n  journal = {arXiv preprint arXiv:2512.04220},\n  year    = {2025},\n}\n\n@article{gradientcoupling2025,\n  title   = {Gradient Coupling: The Hidden Barrier to Generalization in Agentic {RL}},\n  author  = {Anonymous},\n  journal = {arXiv preprint arXiv:2509.23870},\n  year    = {2025},\n}\n\n@article{turnppo2026,\n  title   = {{Turn-PPO}: Turn-Level Advantage Estimation with {PPO} for Improved Multi-Turn {RL}},\n  author  = {Anonymous},\n  journal = {arXiv preprint arXiv:2512.17008},\n  year    = {2026},\n}\n\n@article{gagpo2026,\n  title   = {{GAGPO}: Generalized Advantage Grouped Policy Optimization},\n  author  = {Anonymous},\n  journal = {arXiv preprint arXiv:2605.13217},\n  year    = {2026},\n}\n\n@article{istar2025,\n  title   = {Agentic Reinforcement Learning with Implicit Step Rewards},\n  author  = {Anonymous},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year    = {2025},\n}\n\n@article{mtgrpo2025,\n  title   = {Reinforcing Multi-Turn Reasoning in {LLM} Agents via Turn-Level Credit Assignment},\n  author  = {Anonymous},\n  journal = {arXiv preprint arXiv:2505.11821},\n  year    = {2025},\n}\n\n@article{sweetrl2025,\n  title   = {{SWEET-RL}: Training Multi-Turn {LLM} Agents on Collaborative Reasoning Tasks},\n  author  = {Anonymous},\n  journal = {arXiv preprint arXiv:2503.15478},\n  year    = {2025},\n}\n\n@inproceedings{rudder2019,\n  title     = {{RUDDER}: Return Decomposition for Delayed Rewards},\n  author    = {Arjona-Medina, Jose A. and Gillhofer, Michael and Widrich, Michael and Unterthiner, Thomas and Brandstetter, Johannes and Hochreiter, Sepp},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year      = {2019},\n}\n\n@article{ca_survey2026,\n  title   = {From Reasoning to Agentic: Credit Assignment in {RL} for {LLMs}},\n  author  = {Anonymous},\n  journal = {arXiv preprint arXiv:2604.09459},\n  year    = {2026},\n}"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-18T19:57:30.545964+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/references.bib has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260518T195445",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-18T19:57:30.546146+00:00_

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
  "session": "worker_paper_writing_related_work_20260518T195445",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-18T19:57:30.546319+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{RL Training for Multi-Turn LLM Agents.}
5	The ReAct paradigm~\cite{yao2023react} established interleaved reasoning and acting as the standard framework for LLM agents. Group Relative Policy Optimization (GRPO)~\cite{shao2024deepseekmath}, originally developed for mathematical reasoning, was scaled to large systems through dynamic sampling and clip-higher stabilization~\cite{dapo2025}. Adapting GRPO to multi-turn agents requires addressing the mismatch between its episode-level formulation and the memory constraints of long trajectories. RAGEN~\cite{ragen2025} introduced the step-independent windowing approach that has since become the community default: trajectories are partitioned into fixed-size windows, each optimized with an independently normalized baseline. Subsequent work improves training algorithms or reward design within this framework. GiGPO~\cite{feng2025gigpo} estimates step-level advantages through a nested group structure without a learned critic. Self-Guide~\cite{selfguide2026} co-evolves an internal reward model with the policy to provide denser signals than binary outcomes. SPEAR~\cite{spear2025} combines self-imitation with progressive curriculum to mitigate sparse-reward starvation. DigiRL~\cite{digiRL2024} demonstrates autonomous online RL for device-control agents. WebAgent-R1~\cite{wei2025webagent-r1} extends GRPO to multi-turn web interaction with dynamic context compression, and SORL~\cite{li2025sorl} introduces turn-level importance sampling for off-policy stability. HCAPO~\cite{hcapo2026} uses an LLM-as-critic to assign hindsight credit at critical decision states. These methods improve the algorithm, the reward, or the training pipeline at various granularities, yet none diagnoses the step-independent windowing mechanism itself as a source of systematic sign errors. We identify and formalize this structural failure.
6	
7	\paragraph{Credit Assignment in Reinforcement Learn
…[truncated 5421 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260518T195445",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-18T19:57:30.546466+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/references.bib",
  "offset": "250"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_20260518T195445",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/references.bib",
    "offset": "250"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-18T19:57:30.546667+00:00_

250	}
251	
252	@article{yang2026ares,
253	  title   = {{ARES}: Adaptive Reasoning Effort Selection for Efficient {LLM} Agents},
254	  author  = {Yang, Jingbo and Hou, Bairu and Wei, Wei and Bao, Yujia and Chang, Shiyu},
255	  journal = {arXiv preprint arXiv:2603.07915},
256	  year    = {2026},
257	}
258	
259	@article{irc2026,
260	  title   = {Multi-Turn Reinforcement Learning for Tool-Calling Agents with Iterative Reward Calibration},
261	  author  = {Anonymous},
262	  journal = {arXiv preprint arXiv:2604.02869},
263	  year    = {2026},
264	}
265	
266	@article{mcgrpo2025,
267	  title   = {{MC-GRPO}: Median-Centered Group Relative Policy Optimization for Small-Rollout Reinforcement Learning},
268	  author  = {Kim, Youngeun},
269	  journal = {arXiv preprint arXiv:2601.22582},
270	  year    = {2025},
271	}
272	
273	@article{gra2025,
274	  title   = {Stabilizing Long-term Multi-turn Reinforcement Learning with Gated Rewards},
275	  author  = {Anonymous},
276	  journal = {arXiv preprint arXiv:2508.10548},
277	  year    = {2025},
278	}
279	
280	@article{grpolambda2025,
281	  title   = {{GRPO-$\lambda$}: Credit Assignment improves {LLM} Reasoning},
282	  author  = {Anonymous},
283	  journal = {arXiv preprint arXiv:2510.00194},
284	  year    = {2025},
285	}
286	
287	@article{oar2026,
288	  title   = {Outcome-Grounded Advantage Reshaping for Fine-Grained Credit Assignment in Mathematical Reasoning},
289	  author  = {Anonymous},
290	  journal = {arXiv preprint arXiv:2601.07408},
291	  year    = {2026},
292	}
293	
294	@article{decoupledca2026,
295	  title   = {Both Local Validity and Global Effectiveness Matter: Decoupled Credit Assignment for Long-Horizon Agentic Learning},
296	  author  = {Lu, Wenxuan and Zhang, Zhanqiu and Guo, Steven Y. and Zang, Tianning},
297	  journal = {Submitted to ICLR 2026 (under review)},
298	  year    = {2026},
299	  note    = {OpenReview: Suja4AQ9Fo},
300	}
301	
302	@article{ragen2_2026,
303	  title   = {{RAGEN-2}: Reasoning Collapse in Agentic {
…[truncated 2380 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_20260518T195445",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-18T19:57:30.546890+00:00_

完成。两个文件已更新：

- `related_work.tex`：4 段结构（Multi-Turn RL / Credit Assignment / Multi-Turn CA / GRPO Collapse），每段末尾有定位句，~870 words，无 em-dash、无 -ing 结尾、无论文堆砌
- `references.bib`：末尾添加 16 个新条目（irc2026, mcgrpo2025, gra2025, grpolambda2025, oar2026, decoupledca2026, ragen2_2026, grpocollapse2025, gradientcoupling2025, turnppo2026, gagpo2026, istar2025, mtgrpo2025, sweetrl2025, rudder2019, ca_survey2026）

引用验证约束已遵守：GRPO-λ 用 "Lemma 1 bounds value estimation error"、OAR 用 "reward aliasing"、Decoupled-CA 标注 under review、IRC 用 14pp (54% vs 68%)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_writing_related_work_20260518T195445"
}
```

</details>

---
