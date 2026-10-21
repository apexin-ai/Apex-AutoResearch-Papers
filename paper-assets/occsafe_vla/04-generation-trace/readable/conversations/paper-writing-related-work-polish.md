# paper writing related work polish

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 15
- **Recorded user turns:** 0
- **Tool calls:** 7
- **Original source:** `logs/chats/worker_paper_writing_related_work_polish_20260528T004646.jsonl`
- **Structured JSON:** [`e70d6e44c2021de3a9c4.json`](../../sessions/e7/e70d6e44c2021de3a9c4.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

15 recorded events

### Tool call

_source line 1 · 2026-05-28T00:49:29.924680+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_polish_20260528T004646",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-28T00:49:29.925055+00:00_

1	
2	\section{Related Work}
3	
4	\subsection{VLA Safety and Spatial Representations}
5	
6	Vision-language-action models achieve high task success but remain collision-prone~\cite{li2026vlasafety}. Existing safety approaches filter actions via control barrier functions or embed constraints during training~\cite{hu2025vlsa, zhai2026cofreevla, raja2024ogmcbf, zhang2025safevla}; none examines whether spatial representations contribute to safety. A parallel line enriches VLAs with 3D structure---through depth fusion, representation alignment, geometric encoding, or occupancy prediction~\cite{yuan2025depthvla, li2025qdepthvla, rao2026augvla3d, bhat20253dcavla, abouzeid2025geoaware, yang2024depthanything, li2026spatialforcing, wu2025spatialvla, li2025pointvla, sun2025geovla, wu2026stvla, chen2026gstvla, tu2026sgvla, xiao2026stemvla, li2026corridorvla, liu2025occvla, li2022bevformer, sima2023occnet, tian2023occ3d}---yet none evaluates collision avoidance. Critically, SpatialVLA~\cite{wu2025spatialvla}, DepthVLA~\cite{yuan2025depthvla}, and OccVLA~\cite{liu2025occvla} all report task success improvements from spatial auxiliary supervision but do not include safety metrics; the implicit assumption---that spatial awareness should improve safety because the robot ``knows where things are''---remains untested. We address this gap by directly measuring collision avoidance under controlled spatial supervision conditions.
7	
8	\subsection{Auxiliary Tasks and Multi-Task Gradient Dynamics}
9	
10	Multi-task learning exploits shared representations~\cite{caruana1997multitask, ruder2017overview}, but auxiliary tasks risk negative transfer through optimization conflict or generalization failure~\cite{chen2018gradnorm, yu2020pcgrad, liu2021cagrad, navon2022nashmtl, jiang2023forkmerge}. PCGrad~\cite{yu2020pcgrad} projects conflicting task gradients to remove their interfering components, while CAGrad~\cite{liu2021cagrad} seeks a descent direction within a conflict-averse region that minimi
…[truncated 1368 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_polish_20260528T004646",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-28T00:49:29.925248+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_polish_20260528T004646",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/references.bib"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-28T00:49:29.925506+00:00_

1	% References for OccSafe-VLA
2	% Bib key convention: {first_author_surname_lower}{year}{keyword_lower}
3	
4	% ============================================================
5	% VLA Safety
6	% ============================================================
7	
8	@article{hu2025vlsa,
9	  author    = {Songqiao Hu and Zeyi Liu and Shuang Liu and Jun Cen and Zihan Meng and Xiao He},
10	  title     = {{VLSA}: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer},
11	  journal   = {arXiv preprint arXiv:2512.11891},
12	  year      = {2025},
13	  note      = {arXiv:2512.11891}
14	}
15	
16	@inproceedings{zhang2025safevla,
17	  author    = {Borong Zhang and others},
18	  title     = {{SafeVLA}: Towards Safety Alignment of Vision-Language-Action Model via Constrained Learning},
19	  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
20	  year      = {2025},
21	  note      = {Spotlight. arXiv:2503.03480}
22	}
23	
24	@article{zhai2026cofreevla,
25	  author    = {Xuanran Zhai and others},
26	  title     = {{CoFreeVLA}: Collision-Free Dual-Arm Manipulation via {VLA} Model and Risk Estimation},
27	  journal   = {arXiv preprint arXiv:2601.21712},
28	  year      = {2026},
29	  note      = {arXiv:2601.21712}
30	}
31	
32	
33	@article{li2026vlasafety,
34	  author    = {Qi Li and others},
35	  title     = {Vision-Language-Action Safety: Threats, Challenges, Evaluations, and Mechanisms},
36	  journal   = {arXiv preprint arXiv:2604.23775},
37	  year      = {2026},
38	  note      = {arXiv:2604.23775}
39	}
40	
41	% ============================================================
42	% Safety Mechanisms (barrier functions / occupancy-based safety)
43	% ============================================================
44	
45	
46	@article{raja2024ogmcbf,
47	  author    = {Golnaz Raja and Teemu M{\"o}kk{\"o}nen and Reza Ghabcheloo},
48	  title     = {Safe Robot Control using Occupancy Grid Map-based Control Barrier Function ({OGM-CBF})},
49	  journal   = {arXiv prepr
…[truncated 15535 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_polish_20260528T004646",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-28T00:49:29.925711+00:00_

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
  "session": "worker_paper_writing_related_work_polish_20260528T004646",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-28T00:49:29.926098+00:00_

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
…[truncated 5709 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_polish_20260528T004646",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-28T00:49:29.926394+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/related_work.tex",
  "old_string": "Vision-language-action models achieve high task success but remain collision-prone~\\cite{li2026vlasafety}. Existing safety approaches filter actions via control barrier functions or embed constraints during training~\\cite{hu2025vlsa, zhai2026cofreevla, raja2024ogmcbf, zhang2025safevla}; none examines whether spatial representations contribute to safety. A parallel line enriches VLAs with 3D structure---through depth fusion, representation alignment, geometric encoding, or occupancy prediction~\\cite{yuan2025depthvla, li2025qdepthvla, rao2026augvla3d, bhat20253dcavla, abouzeid2025geoaware, yang2024depthanything, li2026spatialforcing, wu2025spatialvla, li2025pointvla, sun2025geovla, wu2026stvla, chen2026gstvla, tu2026sgvla, xiao2026stemvla, li2026corridorvla, liu2025occvla, li2022bevformer, sima2023occnet, tian2023occ3d}---yet none evaluates collision avoidance. Critically, SpatialVLA~\\cite{wu2025spatialvla}, DepthVLA~\\cite{yuan2025depthvla}, and OccVLA~\\cite{liu2025occvla} all report task success improvements from spatial auxiliary supervision but do not include safety metrics; the implicit assumption---that spatial awareness should improve safety because the robot ``knows where things are''---remains untested. We address this gap by directly measuring collision avoidance under controlled spatial supervision conditions.",
  "new_string": "Vision-language-action models achieve high task success but remain collision-prone~\\cite{li2026vlasafety}. Existing safety approaches filter actions via control barrier functions or embed constraints during training~\\cite{hu2025vlsa, zhai2026cofreevla, raja2024ogmcbf, zhang2025safevla}; none examines whether spatial representations contribute to safety. A parallel line enriches VLAs with 3D structure (depth fusion, representation alignment, geometric encoding, or occupancy prediction)~\\cite{yuan2025depthvla, li2025qdepthvla, rao2026augvla3d, bhat20253dcavla, abouzeid2025geoaware, yang2024depthanything, li2026spatialforcing, wu2025spatialvla, li2025pointvla, sun2025geovla, wu2026stvla, chen2026gstvla, tu2026sgvla, xiao2026stemvla, li2026corridorvla, liu2025occvla, li2022bevformer, sima2023occnet, tian2023occ3d}, yet none evaluates collision avoidance. The occupancy branch of this line originated in autonomous driving: BEVFormer~\\cite{li2022bevformer} introduced transformer-based bird's-eye-view estimation, and subsequent work formalized dense 3D occupancy as a unified scene representation~\\cite{sima2023occnet, tian2023occ3d}. OccVLA~\\cite{liu2025occvla} adapted this concept to robotics by supervising a VLA with implicit occupancy targets; our BEV occupancy auxiliary head follows the same principle but serves as a controlled experimental factor to isolate the safety effect of spatial supervision. SpatialVLA~\\cite{wu2025spatialvla}, DepthVLA~\\cite{yuan2025depthvla}, and OccVLA all report task success improvements from spatial auxiliary supervision but do not include safety metrics. The assumption that spatial awareness should improve safety because the robot ``knows where things are'' remains untested; we address this gap by directly measuring collision avoidance under controlled spatial supervision conditions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_polish_20260528T004646",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/related_work.tex",
    "old_string": "Vision-language-action models achieve high task success but remain collision-prone~\\cite{li2026vlasafety}. Existing safety approaches filter actions via control barrier functions or embed constraints during training~\\cite{hu2025vlsa, zhai2026cofreevla, raja2024ogmcbf, zhang2025safevla}; none examines whether spatial representations contribute to safety. A parallel line enriches VLAs with 3D structure---through depth fusion, representation alignment, geometric encoding, or occupancy prediction~\\cite{yuan2025depthvla, li2025qdepthvla, rao2026augvla3d, bhat20253dcavla, abouzeid2025geoaware, yang2024depthanything, li2026spatialforcing, wu2025spatialvla, li2025pointvla, sun2025geovla, wu2026stvla, chen2026gstvla, tu2026sgvla, xiao2026stemvla, li2026corridorvla, liu2025occvla, li2022bevformer, sima2023occnet, tian2023occ3d}---yet none evaluates collision avoidance. Critically, SpatialVLA~\\cite{wu2025spatialvla}, DepthVLA~\\cite{yuan2025depthvla}, and OccVLA~\\cite{liu2025occvla} all report task success improvements from spatial auxiliary supervision but do not include safety metrics; the implicit assumption---that spatial awareness should improve safety because the robot ``knows where things are''---remains untested. We address this gap by directly measuring collision avoidance under controlled spatial supervision conditions.",
    "new_string": "Vision-language-action models achieve high task success but remain collision-prone~\\cite{li2026vlasafety}. Existing safety approaches filter actions via control barrier functions or embed constraints during training~\\cite{hu2025vlsa, zhai2026cofreevla, raja2024ogmcbf, zhang2025safevla}; none examines whether spatial representations contribute to safety. A parallel line enriches VLAs with 3D structure (depth fusion, representation alignment, geometric encoding, or occupancy prediction)~\\cite{yuan2025depthvla, li2025qdepthvla, rao2026augvla3d, bhat20253dcavla, abouzeid2025geoaware, yang2024depthanything, li2026spatialforcing, wu2025spatialvla, li2025pointvla, sun2025geovla, wu2026stvla, chen2026gstvla, tu2026sgvla, xiao2026stemvla, li2026corridorvla, liu2025occvla, li2022bevformer, sima2023occnet, tian2023occ3d}, yet none evaluates collision avoidance. The occupancy branch of this line originated in autonomous driving: BEVFormer~\\cite{li2022bevformer} introduced transformer-based bird's-eye-view estimation, and subsequent work formalized dense 3D occupancy as a unified scene representation~\\cite{sima2023occnet, tian2023occ3d}. OccVLA~\\cite{liu2025occvla} adapted this concept to robotics by supervising a VLA with implicit occupancy targets; our BEV occupancy auxiliary head follows the same principle but serves as a controlled experimental factor to isolate the safety effect of spatial supervision. SpatialVLA~\\cite{wu2025spatialvla}, DepthVLA~\\cite{yuan2025depthvla}, and OccVLA all report task success improvements from spatial auxiliary supervision but do not include safety metrics. The assumption that spatial awareness should improve safety because the robot ``knows where things are'' remains untested; we address this gap by directly measuring collision avoidance under controlled spatial supervision conditions."
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-28T00:49:29.926597+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/related_work.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_polish_20260528T004646",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-28T00:49:29.926758+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/related_work.tex",
  "old_string": "BatchNorm layers are known to be sensitive to distributional shifts in multi-task and domain adaptation settings: Li et al.~\\cite{li2017adabn} show that recalibrating BN statistics suffices to adapt across domains, and Schneider et al.~\\cite{schneider2020bn} demonstrate that BN running statistics degrade robustness under covariate shift. These findings motivate our factorial inclusion of normalization type as an experimental factor.",
  "new_string": "Batch normalization~\\cite{ioffe2015batchnorm} standardizes activations using mini-batch statistics, coupling each sample's representation to the batch composition. Layer normalization~\\cite{ba2016layernorm} removes this dependence by computing statistics per token, making it the default in transformer architectures, while group normalization~\\cite{wu2018groupnorm} offers a batch-size-independent alternative by normalizing within channel groups. This design choice becomes consequential when auxiliary tasks alter the training distribution: Li et al.~\\cite{li2017adabn} show that recalibrating BN statistics suffices to adapt across domains, and Schneider et al.~\\cite{schneider2020bn} demonstrate that BN running statistics degrade robustness under covariate shift. Our factorial design varies the normalization scheme in the auxiliary head between BatchNorm and LayerNorm, directly testing whether these distributional sensitivities propagate to the primary action objective."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_polish_20260528T004646",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/related_work.tex",
    "old_string": "BatchNorm layers are known to be sensitive to distributional shifts in multi-task and domain adaptation settings: Li et al.~\\cite{li2017adabn} show that recalibrating BN statistics suffices to adapt across domains, and Schneider et al.~\\cite{schneider2020bn} demonstrate that BN running statistics degrade robustness under covariate shift. These findings motivate our factorial inclusion of normalization type as an experimental factor.",
    "new_string": "Batch normalization~\\cite{ioffe2015batchnorm} standardizes activations using mini-batch statistics, coupling each sample's representation to the batch composition. Layer normalization~\\cite{ba2016layernorm} removes this dependence by computing statistics per token, making it the default in transformer architectures, while group normalization~\\cite{wu2018groupnorm} offers a batch-size-independent alternative by normalizing within channel groups. This design choice becomes consequential when auxiliary tasks alter the training distribution: Li et al.~\\cite{li2017adabn} show that recalibrating BN statistics suffices to adapt across domains, and Schneider et al.~\\cite{schneider2020bn} demonstrate that BN running statistics degrade robustness under covariate shift. Our factorial design varies the normalization scheme in the auxiliary head between BatchNorm and LayerNorm, directly testing whether these distributional sensitivities propagate to the primary action objective."
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-28T00:49:29.926921+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/related_work.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_polish_20260528T004646",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-28T00:49:29.927049+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/references.bib",
  "old_string": "% ============================================================\n% BatchNorm in Domain Adaptation / Robustness\n% ============================================================",
  "new_string": "% ============================================================\n% Normalization Techniques\n% ============================================================\n\n@inproceedings{ioffe2015batchnorm,\n  author    = {Sergey Ioffe and Christian Szegedy},\n  title     = {Batch Normalization: Accelerating Deep Network Training by Reducing Internal Covariate Shift},\n  booktitle = {International Conference on Machine Learning (ICML)},\n  year      = {2015},\n  note      = {arXiv:1502.03167}\n}\n\n@article{ba2016layernorm,\n  author    = {Jimmy Lei Ba and Jamie Ryan Kiros and Geoffrey E. Hinton},\n  title     = {Layer Normalization},\n  journal   = {arXiv preprint arXiv:1607.06450},\n  year      = {2016},\n  note      = {arXiv:1607.06450}\n}\n\n@inproceedings{wu2018groupnorm,\n  author    = {Yuxin Wu and Kaiming He},\n  title     = {Group Normalization},\n  booktitle = {European Conference on Computer Vision (ECCV)},\n  year      = {2018},\n  note      = {arXiv:1803.08494}\n}\n\n% ============================================================\n% BatchNorm in Domain Adaptation / Robustness\n% ============================================================"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_polish_20260528T004646",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/references.bib",
    "old_string": "% ============================================================\n% BatchNorm in Domain Adaptation / Robustness\n% ============================================================",
    "new_string": "% ============================================================\n% Normalization Techniques\n% ============================================================\n\n@inproceedings{ioffe2015batchnorm,\n  author    = {Sergey Ioffe and Christian Szegedy},\n  title     = {Batch Normalization: Accelerating Deep Network Training by Reducing Internal Covariate Shift},\n  booktitle = {International Conference on Machine Learning (ICML)},\n  year      = {2015},\n  note      = {arXiv:1502.03167}\n}\n\n@article{ba2016layernorm,\n  author    = {Jimmy Lei Ba and Jamie Ryan Kiros and Geoffrey E. Hinton},\n  title     = {Layer Normalization},\n  journal   = {arXiv preprint arXiv:1607.06450},\n  year      = {2016},\n  note      = {arXiv:1607.06450}\n}\n\n@inproceedings{wu2018groupnorm,\n  author    = {Yuxin Wu and Kaiming He},\n  title     = {Group Normalization},\n  booktitle = {European Conference on Computer Vision (ECCV)},\n  year      = {2018},\n  note      = {arXiv:1803.08494}\n}\n\n% ============================================================\n% BatchNorm in Domain Adaptation / Robustness\n% ============================================================"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-28T00:49:29.927235+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/references.bib has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_polish_20260528T004646",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-28T00:49:29.927373+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_polish_20260528T004646",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-28T00:49:29.927519+00:00_

1	
2	\section{Related Work}
3	
4	\subsection{VLA Safety and Spatial Representations}
5	
6	Vision-language-action models achieve high task success but remain collision-prone~\cite{li2026vlasafety}. Existing safety approaches filter actions via control barrier functions or embed constraints during training~\cite{hu2025vlsa, zhai2026cofreevla, raja2024ogmcbf, zhang2025safevla}; none examines whether spatial representations contribute to safety. A parallel line enriches VLAs with 3D structure (depth fusion, representation alignment, geometric encoding, or occupancy prediction)~\cite{yuan2025depthvla, li2025qdepthvla, rao2026augvla3d, bhat20253dcavla, abouzeid2025geoaware, yang2024depthanything, li2026spatialforcing, wu2025spatialvla, li2025pointvla, sun2025geovla, wu2026stvla, chen2026gstvla, tu2026sgvla, xiao2026stemvla, li2026corridorvla, liu2025occvla, li2022bevformer, sima2023occnet, tian2023occ3d}, yet none evaluates collision avoidance. The occupancy branch of this line originated in autonomous driving: BEVFormer~\cite{li2022bevformer} introduced transformer-based bird's-eye-view estimation, and subsequent work formalized dense 3D occupancy as a unified scene representation~\cite{sima2023occnet, tian2023occ3d}. OccVLA~\cite{liu2025occvla} adapted this concept to robotics by supervising a VLA with implicit occupancy targets; our BEV occupancy auxiliary head follows the same principle but serves as a controlled experimental factor to isolate the safety effect of spatial supervision. SpatialVLA~\cite{wu2025spatialvla}, DepthVLA~\cite{yuan2025depthvla}, and OccVLA all report task success improvements from spatial auxiliary supervision but do not include safety metrics. The assumption that spatial awareness should improve safety because the robot ``knows where things are'' remains untested; we address this gap by directly measuring collision avoidance under controlled spatial supervision conditions.
7	
8	\subsection{Auxiliary Tasks and Multi-Task Gradient Dynamics}
9	

…[truncated 2412 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_polish_20260528T004646",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-28T00:49:29.927740+00:00_

All edits complete. Summary of changes:

**`related_work.tex`:**
- **Subsection 1**: Added 2 sentences tracing occupancy prediction from AD (BEVFormer → OccNet/Occ3D) to robotics (OccVLA), positioning our BEV head as a controlled experimental factor rather than a task success tool. Removed all 3 em-dashes (`---`), replaced with parentheses/commas. Removed "Critically" opener.
- **Subsection 2**: Added 3 sentences introducing BN/LN/GN fundamentals with citations, integrated smoothly into the existing domain adaptation discussion. Final positioning sentence now explicitly states the BN-vs-LN factorial variation in the auxiliary head.

**`references.bib`:**
- Added `ioffe2015batchnorm`, `ba2016layernorm`, `wu2018groupnorm` in a new "Normalization Techniques" section above the existing "BatchNorm in Domain Adaptation" section.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_writing_related_work_polish_20260528T004646"
}
```

</details>

---
