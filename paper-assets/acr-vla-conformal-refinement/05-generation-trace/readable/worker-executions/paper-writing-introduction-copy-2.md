# paper writing introduction

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 35
- **Recorded user turns:** 0
- **Tool calls:** 11
- **Original source:** `logs/workers/worker_paper_writing_introduction_20260518T101546.log`
- **Structured JSON:** [`927339c0f30ab06df3ba.json`](../../sessions/92/927339c0f30ab06df3ba.json)

## Before a recorded user message

35 recorded events

### Log line

_source line 1_

Warning: no stdin data received in 3s, proceeding without it. If piping from a slow command, redirect stdin explicitly: < /dev/null to skip, or wait longer.

---

### System

_source line 2_

```json
{
  "type": "system",
  "subtype": "init",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement",
  "session_id": "8146b578-f41a-49c2-b99a-be63bde75274",
  "tools": [
    "Task",
    "AskUserQuestion",
    "Bash",
    "CronCreate",
    "CronDelete",
    "CronList",
    "Edit",
    "EnterPlanMode",
    "EnterWorktree",
    "ExitPlanMode",
    "ExitWorktree",
    "Glob",
    "Grep",
    "ListMcpResourcesTool",
    "Monitor",
    "NotebookEdit",
    "PushNotification",
    "Read",
    "ReadMcpResourceTool",
    "RemoteTrigger",
    "ScheduleWakeup",
    "Skill",
    "TaskOutput",
    "TaskStop",
    "TodoWrite",
    "ToolSearch",
    "WebFetch",
    "WebSearch",
    "Write",
    "mcp__agent-ml-research__auto_build_provenance",
    "mcp__agent-ml-research__bootstrap_provenance",
    "mcp__agent-ml-research__check_paper_consistency",
    "mcp__agent-ml-research__check_provenance_completeness",
    "mcp__agent-ml-research__cleanup_pdf_images",
    "mcp__agent-ml-research__compute_coverage_matrix",
    "mcp__agent-ml-research__edit_paper_section",
    "mcp__agent-ml-research__get_image_info",
    "mcp__agent-ml-research__get_worker_status",
    "mcp__agent-ml-research__list_artifacts",
    "mcp__agent-ml-research__list_workers",
    "mcp__agent-ml-research__load_project_config",
    "mcp__agent-ml-research__overleaf_init",
    "mcp__agent-ml-research__overleaf_pull",
    "mcp__agent-ml-research__overleaf_push",
    "mcp__agent-ml-research__overleaf_status",
    "mcp__agent-ml-research__overleaf_sync",
    "mcp__agent-ml-research__paper_agent_post_to_director",
    "mcp__agent-ml-research__paper_agent_request_review",
    "mcp__agent-ml-research__paper_compile_and_check",
    "mcp__agent-ml-research__pdf_to_images",
    "mcp__agent-ml-research__read_experiment_plan_with_status",
    "mcp__agent-ml-research__read_project_file",
    "mcp__agent-ml-research__read_registry",
    "mcp__agent-ml-research__read_roadmap",
    "mcp__agent-ml-research__register_artifact",
    "mcp__agent-ml-research__save_project_file",
    "mcp__agent-ml-research__send_progress",
    "mcp__agent-ml-research__spawn_worker",
    "mcp__agent-ml-research__verify_references",
    "mcp__agent-ml-research__write_paper_section"
  ],
  "mcp_servers": [
    {
      "name": "agent-ml-research",
      "status": "connected"
    }
  ],
  "model": "claude-opus-4-6",
  "permissionMode": "bypassPermissions",
  "slash_commands": [
    "update-config",
    "debug",
    "simplify",
    "batch",
    "fewer-permission-prompts",
    "loop",
    "schedule",
    "claude-api",
    "clear",
    "compact",
    "context",
    "heapdump",
    "init",
    "review",
    "security-review",
    "extra-usage",
    "usage",
    "insights",
    "team-onboarding"
  ],
  "apiKeySource": "none",
  "claude_code_version": "2.1.126",
  "output_style": "default",
  "agents": [
    "claude",
    "Explore",
    "general-purpose",
    "Plan",
    "statusline-setup"
  ],
  "skills": [
    "update-config",
    "debug",
    "simplify",
    "batch",
    "fewer-permission-prompts",
    "loop",
    "schedule",
    "claude-api"
  ],
  "plugins": [],
  "analytics_disabled": false,
  "uuid": "fc814d45-d7e2-49d0-9cc0-e5ea1edb3409",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/memory/"
  },
  "fast_mode_state": "off"
}
```

---

### Runtime record

_source line 3_

```json
{
  "type": "rate_limit_event",
  "rate_limit_info": {
    "status": "allowed",
    "resetsAt": 1779113400,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "25b75048-7f07-4fdb-b0ab-7fad8afd10ea",
  "session_id": "8146b578-f41a-49c2-b99a-be63bde75274"
}
```

---

### Assistant

_source line 4_

I'll start by reading the required skill files and context documents in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8146b578-f41a-49c2-b99a-be63bde75274",
  "uuid": "1e06b7b4-f9c2-46fb-ba37-c61f3e730a62",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qd65KxaAJFk6Ua4jJJpjJv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14054,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14054
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 5_

<details open><summary>🔧 Tool call — Read · `toolu_013fkC3HMQxYuvEQbehgoxWB`</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8146b578-f41a-49c2-b99a-be63bde75274",
  "uuid": "9891b39c-0f17-4354-9608-c4cf31dfe689",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qd65KxaAJFk6Ua4jJJpjJv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14054,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14054
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-18T10:15:56.252Z_

<details><summary>↩ Tool result · `toolu_013fkC3HMQxYuvEQbehgoxWB`</summary>

````text
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
94	4. CHECK   → 确认你引用的 claim 确实出自该论文
95	5. ADD     → 加入 .bib 文件
96	```
97	
98	### 3.3 API 速查
99	
100	| API | 用途 | 限制 |
101	|-----|------|------|
102	| **Semantic Scholar** | ML/AI 论文搜索 | 1 RPS (免费) |
103	| **CrossRef** | DOI → BibTeX | 需 mailto 头 |
104	| **arXiv** | 预印本搜索 | 3s 间隔 |
105	
106	```python
107	# DOI → BibTeX（最可靠的方式）
108	import requests
109	def doi_to_bibtex(doi: str) -> str:
110	    r = requests.get(f"https://doi.org/{doi}",
111	                     headers={"Accept": "application/x-bibtex"})
112	    r.raise_for_status()
113	    return r.text
114	
115	# Semantic Scholar 搜索
116	from semanticscholar import SemanticScholar
117	sch = SemanticScholar()
118	results = sch.search_paper("attention mechanism transformers", limit=5)
119	for p in results:
120	    print(f"{p.title} | DOI: {p.externalIds.get('DOI', 'N/A')}")
121	```
122	
123	### 3.4 引用处理规则
124	
125	| 情况 | 处理 |
126	|------|------|
127	| 找到论文 + DOI + BibTeX | 直接用 |
128	| 找到论文，无 DOI | 用 arXiv BibTeX |
129	| 论文存在但无法获取 BibTeX | 标记 placeholder，告知用户 |
130	| 不确定论文是否存在 | 标记 `[CITATION NEEDED]`，告知用户 |
131	| "我觉得有篇关于 X 的论文" | **绝不引用** — 先搜索或标记 |
132	
133	---
134	
135	## 4. 顶会模板速查
136	
137	### 4.1 ML/AI 会议
138	
139	| 会议 | 页数限制 | 主文件 | 样式文件 | 必须项 |
140	|------|---------|--------|---------|--------|
141	| **NeurIPS** | 9 页 | `main.tex` | `neurips.sty` | Paper Checklist |
142	| **ICML** | 8 页 (+1 camera-ready) | `example_paper.tex` | `icml2026.sty` | Broader Impact |
143	| **ICLR** | 9 页 (+1) | `iclr_conference.tex` | `iclr_conference.sty` | LLM 使用声明 |
144	| **ACL/EMNLP** | 8 页 (long) | `acl_latex.tex` | `acl.sty` | Limitations 必须 |
145	| **AAAI** | 7 页 (+1) | `aaai_template.tex` | `aaai.sty` | 严格样式 |
146	| **COLM** | 9 页 (+1) | `colm_conference.tex` | `colm_conference.sty` | 语言模型聚焦 |
147	
148	### 4.2 系统会议
149	
150	| 会议 | 页数限制 | 模板类型 | 关键要求 |
151	|------|---------|---------|---------|
152	| **OSDI** | 12 页 (+2) | USENIX `usenix.sty` | Research / Operational 双 track |
153	| **NSDI** | 12 页 | USENIX | Introduction 预筛 |
154	| **ASPLOS** | 12 页 | ACM `acmart.cls (sigplan)` | 前 2 页快速评审 |
155	| **SOSP** | 12 页 | ACM `acmart.cls (sigplan)` | 可选 Artifact Evaluation |
156	
157	### 4.3 模板使用原则
158	
159	```bash
160	# 1. 复制整个模板目录（不要只拷 .tex）
161	cp -r templates/neurips2025/ ~/papers/my-paper/
162	
163	# 2. 先编译未修改的模板，确认能跑通
164	latexmk -pdf main.tex
165	
166	# 3. 逐章替换内容，频繁编译
167	```
168	
169	**禁止事项：**
170	- 不要修改 `.sty` 文件
171	- 不要在会议模板间复制 `\usepackage` 行
172	- 不要只复制 `.tex` 而不带 `.sty/.bst`
173	
174	---
175	
176	## 5. 写作规范
177	
178	### 5.1 时间分配（Neel Nanda）
179	
180	花**大致相等**的时间在：
181	1. Abstract
182	2. Introduction
183	3. 图表
184	4. **其余所有内容加起来**
185	
186	审稿人读论文的顺序：标题 → 摘要 → 引言 → 图表 → 也许正文。
187	
188	### 5.2 Abstract 五句法（Sebastian Farquhar）
189	
190	```
191	1. 你做了什么（"We introduce/prove/demonstrate..."）
192	2. 为什么这很难且重要
193	3. 怎么做的（含专业关键词以便检索）
194	4. 有什么证据
195	5. 最惊人的数字/结果
196	```
197	
198	删除一切泛泛的开头：~~"Large language models have achieved remarkable success..."~~
199	
200	### 5.3 句子级清晰度（Gopen & Swan）
201	
202	| 原则 | 规则 |
203	|------|------|
204	| 主谓紧邻 | 不要在主语和动词之间插入长从句 |
205	| 重点在句尾 | 把关键数字/结论放在句末 |
206	| 旧信息在前 | 先放读者已知的内容，再引入新概念 |
207	| 动词表达动作 | "We analyzed" 而非 "We performed an analysis" |
208	
209	### 5.4 常见修改
210	
211	| 问题 | 修复 |
212	|------|------|
213	| Abstract 太泛 | 删第一句（如果它能放在任何 ML 论文前面） |
214	| Introduction 超 1.5 页 | 背景挪到 Related Work |
215	| 实验没有显式 claim | 每个实验前加 "This tests whether..." |
216	| 缺统计显著性 | 加 error bars + 运行次数 + 计算方法 |
217	
218	---
219	
220	## 6. 投稿工程链
221	
222	### 6.1 构建
223	
224	```bash
225	# 推荐：latexmk 一键构建
226	latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
227	
228	# 手动：需要多次编译
229	pdflatex main.tex && bibtex main && pdflatex main.tex && pdflatex main.tex
230	```
231	
232	### 6.2 Lint + 格式化
233	
234	```bash
235	# Lint: 检查常见 LaTeX 问题
236	chktex main.tex
237	
238	# 格式化: 减少 diff 噪声
239	latexindent -w main.tex
240	```
241	
242	### 6.3 图表格式
243	
244	| 类型 | 格式 | 说明 |
245	|------|------|------|
246	| 矢量图（plot、diagram） | PDF | matplotlib: `plt.savefig('fig.pdf')` |
247	| 照片/heatmap | PNG 600dpi 或 TIFF | 栅格图 |
248	| 表格 | `booktabs` 包 | `\toprule/\midrule/\bottomrule` |
249	
250	```latex
251	\usepackage{booktabs}
252	\begin{tabular}{lcc}
253	\toprule
254	Method & Accuracy $\uparrow$ & Latency $\downarrow$ \\
255	\midrule
256	Baseline & 85.2 & 45ms \\
257	\textbf{Ours} & \textbf{92.1} & 38ms \\
258	\bottomrule
259	\end{tabular}
260	```
261	
262	**图表规范：**
263	- 用色盲友好色板（Okabe-Ito 或 Paul Tol）
264	- 图内不放标题（用 caption）
265	- Caption 独立可理解（不依赖正文）
266	- 最佳值加粗，标注方向符号（↑ 越高越好，↓ 越低越好）
267	
268	### 6.4 投稿打包
269	
270	```bash
271	# 清理辅助文件
272	latexmk -c
273	
274	# 打包投稿
275	zip -r submission.zip main.tex *.sty *.bst *.bib figures/ --exclude='*.aux' --exclude='*.log'
276	```
277	
278	### 6.5 常见失败点
279	
280	| 问题 | 解决 |
281	|------|------|
282	| 图片格式混用导致编译失败 | 统一用 PDF |
283	| 字体未嵌入 | `pdffonts output.pdf` 检查 |
284	| Overfull box 过多 | 关键位置手动调行 |
285	| 引用缺字段 | 检查 DOI/年份/期刊名 |
286	| 超页数 | 用 `\vspace{-Xpt}` 微调，或精简内容 |
287	
288	---
289	
290	## 7. 会议转投
291	
292	当论文被拒或转投其他会议时：
293	
294	### 7.1 ML/AI 会议间转换
295	
296	| 转换 | 页数变化 | 关键调整 |
297	|------|---------|---------|
298	| NeurIPS → ICML | 9→8 | 删 1 页，加 Broader Impact |
299	| ICML → ICLR | 8→9 | 可扩展实验 + LLM 声明 |
300	| NeurIPS → ACL | 9→8 | 按 NLP 惯例重组 + Limitations |
301	| ICLR → AAAI | 9→7 | 大幅精简，严格样式 |
302	
303	### 7.2 转投原则
304	
305	1. **永远用目标模板重新开始** — 复制目标模板，迁移内容，不要合并 preamble
306	2. **只迁移正文内容** — 不复制 `\usepackage`、header/footer 命令
307	3. **根据审稿意见改进** — 但不要在新稿中提及旧投稿（双盲）
308	4. **检查目标会议特殊要求** — checklist、ethics statement、LLM 声明等
309	
310	---
311	
312	## 8. 投前清单
313	
314	### 通用清单
315	
316	- [ ] Abstract/Intro/Conclusion 的 claim 一致
317	- [ ] 每个 contribution 有对应 evidence
318	- [ ] 所有引用已程序化验证（无幻觉引用）
319	- [ ] Error bars + 运行次数 + 统计方法
320	- [ ] Limitations 章节存在且诚实
321	- [ ] 匿名化（双盲审稿）
322	- [ ] 符合页数限制
323	- [ ] 所有图表有自包含 caption
324	- [ ] `.bib` 中无缺失字段
325	- [ ] PDF 编译无 warning
326	
327	### 会议特定
328	
329	| 会议 | 额外要求 |
330	|------|---------|
331	| NeurIPS | 16 项 Paper Checklist（附录，不计页数） |
332	| ICML | Broader Impact Statement |
333	| ICLR | LLM 使用声明 |
334	| ACL/EMNLP | Limitations 章节（必须），Ethics Statement |
335	| AAAI | 严格样式文件合规 |
336	
337	---
338	
339	## 参考资源
340	
341	**写作方法论：**
342	- [Neel Nanda: How to Write ML Papers](https://www.alignmentforum.org/posts/eJGptPbbFPZGLpjsp/) — What/Why/So What 框架
343	- [Farquhar: How to Write ML Papers](https://sebastianfarquhar.com/on-research/2024/11/04/how_to_write_ml_papers/) — 五句法 Abstract
344	- [Gopen & Swan: Science of Scientific Writing](https://cseweb.ucsd.edu/~swanson/papers/science-of-writing.pdf) — 读者预期 7 原则
345	- [Lipton: Heuristics for Scientific Writing](https://www.approximatelycorrect.com/2018/01/29/heuristics-technical-scientific-writing-machine-learning-perspective/) — 用词
346	- [Perez: Easy Paper Writing Tips](https://ethanperez.net/easy-paper-writing-tips/) — 微观清晰度
347	
348	**API：**
349	- [Semantic Scholar](https://api.semanticscholar.org/api-docs/) | [CrossRef](https://www.crossref.org/documentation/) | [arXiv](https://info.arxiv.org/help/api/)
350	
351	**会议官方：**
352	- [NeurIPS](https://neurips.cc/) | [ICML](https://icml.cc/) | [ICLR](https://iclr.cc/) | [ACL](https://www.aclweb.org/) | [AAAI](https://aaai.org/) | [EMNLP](https://2025.emnlp.org/)
353	
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8146b578-f41a-49c2-b99a-be63bde75274",
  "uuid": "fdea3279-8557-439f-9b4b-6dfb87645f36",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md",
      "content": "---\nname: latex-paper\ndescription: ML 顶会论文 LaTeX 写作全流程——Claim-Evidence 方法论、引用防幻觉、顶会模板速查、投稿工程链、会议转投。写论文/投稿时参考。\nscope: global\ntags:\n- latex\n- paper-writing\n- academic\n- citation\n- submission\nversion: 1\nroles:\n- agent\n- worker\n---\n\n# LaTeX 论文写作全流程\n\nML/AI 顶会论文从草稿到投稿的完整指南。整合 Orchestra Research、VibeSkills、claim2evidence 三方最佳实践。\n\n---\n\n## 1. 工作模式\n\n开始前选择模式：\n\n| 模式 | 说明 | 适用 |\n|------|------|------|\n| **Build** | 从实验笔记/结果/代码生成论文 | 新稿 |\n| **Improve** | 改写已有章节，强化论证 | 修改稿 |\n| **Audit** | 输出风险列表 + 缺失证据 + 修复建议 | 投前检查 |\n\n---\n\n## 2. Claim-Evidence 方法论\n\n**核心原则：论文是一个有中心贡献的故事，不是实验的堆砌。**\n\n### 2.1 一句话贡献\n\n在写任何内容之前，必须能用一句话说清贡献。如果不能，说明还没准备好写论文。\n\n### 2.2 Claim-Evidence Map\n\n为每个 contribution 建立 claim→evidence 映射表：\n\n| Contribution | Claim | Evidence | Table/Figure |\n|-------------|-------|----------|-------------|\n| C1: 方法 X 在 Y 上 SOTA | 比所有 baseline 高 ≥2% | 5-seed 平均，p<0.05 | Table 1 |\n| C2: 消融证明 Z 是关键 | 去掉 Z 后掉 >5% | 消融实验 | Table 2 |\n| C3: 计算效率 | 比 baseline 快 3× | FLOPs + wall-clock | Figure 3 |\n\n**没有直接证据支撑的 claim 必须删除或降级为 discussion。**\n\n### 2.3 章节起草顺序\n\n```\n1. Introduction + Experiments（先确定 claim 和 evidence）\n2. Method（评估问题稳定后再写细节）\n3. Related Work\n4. Abstract + Title（核心 claim 定型后最后写）\n```\n\n### 2.4 Quality Gates\n\n投稿前必须通过：\n- [ ] 前两段出现显式 novelty 声明\n- [ ] 每个 contribution 有可验证的 evidence\n- [ ] Abstract / Intro / Conclusion 的 claim 一致\n- [ ] Limitations 真实且技术性诚实\n- [ ] 审稿人两分钟内能识别 delta\n\n---\n\n## 3. 引用防幻觉（CRITICAL）\n\n**AI 生成引用有 ~40% 错误率。绝对禁止凭记忆写 BibTeX。**\n\n### 3.1 黄金法则\n\n```\nIF 无法程序化获取引用:\n    → 标记 [CITATION NEEDED] 或 \\cite{PLACEHOLDER_verify}\n    → 明确告知用户\n    → 绝不编造看似合理的引用\n```\n\n### 3.2 五步验证流程\n\n```\n1. SEARCH  → Semantic Scholar API 搜索关键词\n2. VERIFY  → 至少 2 个来源确认论文存在（S2 + arXiv/CrossRef）\n3. RETRIEVE → 通过 DOI 获取 BibTeX（程序化，非记忆）\n4. CHECK   → 确认你引用的 claim 确实出自该论文\n5. ADD     → 加入 .bib 文件\n```\n\n### 3.3 API 速查\n\n| API | 用途 | 限制 |\n|-----|------|------|\n| **Semantic Scholar** | ML/AI 论文搜索 | 1 RPS (免费) |\n| **CrossRef** | DOI → BibTeX | 需 mailto 头 |\n| **arXiv** | 预印本搜索 | 3s 间隔 |\n\n```python\n# DOI → BibTeX（最可靠的方式）\nimport requests\ndef doi_to_bibtex(doi: str) -> str:\n    r = requests.get(f\"https://doi.org/{doi}\",\n                     headers={\"Accept\": \"application/x-bibtex\"})\n    r.raise_for_status()\n    return r.text\n\n# Semantic Scholar 搜索\nfrom semanticscholar import SemanticScholar\nsch = SemanticScholar()\nresults = sch.search_paper(\"attention mechanism transformers\", limit=5)\nfor p in results:\n    print(f\"{p.title} | DOI: {p.externalIds.get('DOI', 'N/A')}\")\n```\n\n### 3.4 引用处理规则\n\n| 情况 | 处理 |\n|------|------|\n| 找到论文 + DOI + BibTeX | 直接用 |\n| 找到论文，无 DOI | 用 arXiv BibTeX |\n| 论文存在但无法获取 BibTeX | 标记 placeholder，告知用户 |\n| 不确定论文是否存在 | 标记 `[CITATION NEEDED]`，告知用户 |\n| \"我觉得有篇关于 X 的论文\" | **绝不引用** — 先搜索或标记 |\n\n---\n\n## 4. 顶会模板速查\n\n### 4.1 ML/AI 会议\n\n| 会议 | 页数限制 | 主文件 | 样式文件 | 必须项 |\n|------|---------|--------|---------|--------|\n| **NeurIPS** | 9 页 | `main.tex` | `neurips.sty` | Paper Checklist |\n| **ICML** | 8 页 (+1 camera-ready) | `example_paper.tex` | `icml2026.sty` | Broader Impact |\n| **ICLR** | 9 页 (+1) | `iclr_conference.tex` | `iclr_conference.sty` | LLM 使用声明 |\n| **ACL/EMNLP** | 8 页 (long) | `acl_latex.tex` | `acl.sty` | Limitations 必须 |\n| **AAAI** | 7 页 (+1) | `aaai_template.tex` | `aaai.sty` | 严格样式 |\n| **COLM** | 9 页 (+1) | `colm_conference.tex` | `colm_conference.sty` | 语言模型聚焦 |\n\n### 4.2 系统会议\n\n| 会议 | 页数限制 | 模板类型 | 关键要求 |\n|------|---------|---------|---------|\n| **OSDI** | 12 页 (+2) | USENIX `usenix.sty` | Research / Operational 双 track |\n| **NSDI** | 12 页 | USENIX | Introduction 预筛 |\n| **ASPLOS** | 12 页 | ACM `acmart.cls (sigplan)` | 前 2 页快速评审 |\n| **SOSP** | 12 页 | ACM `acmart.cls (sigplan)` | 可选 Artifact Evaluation |\n\n### 4.3 模板使用原则\n\n```bash\n# 1. 复制整个模板目录（不要只拷 .tex）\ncp -r templates/neurips2025/ ~/papers/my-paper/\n\n# 2. 先编译未修改的模板，确认能跑通\nlatexmk -pdf main.tex\n\n# 3. 逐章替换内容，频繁编译\n```\n\n**禁止事项：**\n- 不要修改 `.sty` 文件\n- 不要在会议模板间复制 `\\usepackage` 行\n- 不要只复制 `.tex` 而不带 `.sty/.bst`\n\n---\n\n## 5. 写作规范\n\n### 5.1 时间分配（Neel Nanda）\n\n花**大致相等**的时间在：\n1. Abstract\n2. Introduction\n3. 图表\n4. **其余所有内容加起来**\n\n审稿人读论文的顺序：标题 → 摘要 → 引言 → 图表 → 也许正文。\n\n### 5.2 Abstract 五句法（Sebastian Farquhar）\n\n```\n1. 你做了什么（\"We introduce/prove/demonstrate...\"）\n2. 为什么这很难且重要\n3. 怎么做的（含专业关键词以便检索）\n4. 有什么证据\n5. 最惊人的数字/结果\n```\n\n删除一切泛泛的开头：~~\"Large language models have achieved remarkable success...\"~~\n\n### 5.3 句子级清晰度（Gopen & Swan）\n\n| 原则 | 规则 |\n|------|------|\n| 主谓紧邻 | 不要在主语和动词之间插入长从句 |\n| 重点在句尾 | 把关键数字/结论放在句末 |\n| 旧信息在前 | 先放读者已知的内容，再引入新概念 |\n| 动词表达动作 | \"We analyzed\" 而非 \"We performed an analysis\" |\n\n### 5.4 常见修改\n\n| 问题 | 修复 |\n|------|------|\n| Abstract 太泛 | 删第一句（如果它能放在任何 ML 论文前面） |\n| Introduction 超 1.5 页 | 背景挪到 Related Work |\n| 实验没有显式 claim | 每个实验前加 \"This tests whether...\" |\n| 缺统计显著性 | 加 error bars + 运行次数 + 计算方法 |\n\n---\n\n## 6. 投稿工程链\n\n### 6.1 构建\n\n```bash\n# 推荐：latexmk 一键构建\nlatexmk -pdf -interaction=nonstopmode -halt-on-error main.tex\n\n# 手动：需要多次编译\npdflatex main.tex && bibtex main && pdflatex main.tex && pdflatex main.tex\n```\n\n### 6.2 Lint + 格式化\n\n```bash\n# Lint: 检查常见 LaTeX 问题\nchktex main.tex\n\n# 格式化: 减少 diff 噪声\nlatexindent -w main.tex\n```\n\n### 6.3 图表格式\n\n| 类型 | 格式 | 说明 |\n|------|------|------|\n| 矢量图（plot、diagram） | PDF | matplotlib: `plt.savefig('fig.pdf')` |\n| 照片/heatmap | PNG 600dpi 或 TIFF | 栅格图 |\n| 表格 | `booktabs` 包 | `\\toprule/\\midrule/\\bottomrule` |\n\n```latex\n\\usepackage{booktabs}\n\\begin{tabular}{lcc}\n\\toprule\nMethod & Accuracy $\\uparrow$ & Latency $\\downarrow$ \\\\\n\\midrule\nBaseline & 85.2 & 45ms \\\\\n\\textbf{Ours} & \\textbf{92.1} & 38ms \\\\\n\\bottomrule\n\\end{tabular}\n```\n\n**图表规范：**\n- 用色盲友好色板（Okabe-Ito 或 Paul Tol）\n- 图内不放标题（用 caption）\n- Caption 独立可理解（不依赖正文）\n- 最佳值加粗，标注方向符号（↑ 越高越好，↓ 越低越好）\n\n### 6.4 投稿打包\n\n```bash\n# 清理辅助文件\nlatexmk -c\n\n# 打包投稿\nzip -r submission.zip main.tex *.sty *.bst *.bib figures/ --exclude='*.aux' --exclude='*.log'\n```\n\n### 6.5 常见失败点\n\n| 问题 | 解决 |\n|------|------|\n| 图片格式混用导致编译失败 | 统一用 PDF |\n| 字体未嵌入 | `pdffonts output.pdf` 检查 |\n| Overfull box 过多 | 关键位置手动调行 |\n| 引用缺字段 | 检查 DOI/年份/期刊名 |\n| 超页数 | 用 `\\vspace{-Xpt}` 微调，或精简内容 |\n\n---\n\n## 7. 会议转投\n\n当论文被拒或转投其他会议时：\n\n### 7.1 ML/AI 会议间转换\n\n| 转换 | 页数变化 | 关键调整 |\n|------|---------|---------|\n| NeurIPS → ICML | 9→8 | 删 1 页，加 Broader Impact |\n| ICML → ICLR | 8→9 | 可扩展实验 + LLM 声明 |\n| NeurIPS → ACL | 9→8 | 按 NLP 惯例重组 + Limitations |\n| ICLR → AAAI | 9→7 | 大幅精简，严格样式 |\n\n### 7.2 转投原则\n\n1. **永远用目标模板重新开始** — 复制目标模板，迁移内容，不要合并 preamble\n2. **只迁移正文内容** — 不复制 `\\usepackage`、header/footer 命令\n3. **根据审稿意见改进** — 但不要在新稿中提及旧投稿（双盲）\n4. **检查目标会议特殊要求** — checklist、ethics statement、LLM 声明等\n\n---\n\n## 8. 投前清单\n\n### 通用清单\n\n- [ ] Abstract/Intro/Conclusion 的 claim 一致\n- [ ] 每个 contribution 有对应 evidence\n- [ ] 所有引用已程序化验证（无幻觉引用）\n- [ ] Error bars + 运行次数 + 统计方法\n- [ ] Limitations 章节存在且诚实\n- [ ] 匿名化（双盲审稿）\n- [ ] 符合页数限制\n- [ ] 所有图表有自包含 caption\n- [ ] `.bib` 中无缺失字段\n- [ ] PDF 编译无 warning\n\n### 会议特定\n\n| 会议 | 额外要求 |\n|------|---------|\n| NeurIPS | 16 项 Paper Checklist（附录，不计页数） |\n| ICML | Broader Impact Statement |\n| ICLR | LLM 使用声明 |\n| ACL/EMNLP | Limitations 章节（必须），Ethics Statement |\n| AAAI | 严格样式文件合规 |\n\n---\n\n## 参考资源\n\n**写作方法论：**\n- [Neel Nanda: How to Write ML Papers](https://www.alignmentforum.org/posts/eJGptPbbFPZGLpjsp/) — What/Why/So What 框架\n- [Farquhar: How to Write ML Papers](https://sebastianfarquhar.com/on-research/2024/11/04/how_to_write_ml_papers/) — 五句法 Abstract\n- [Gopen & Swan: Science of Scientific Writing](https://cseweb.ucsd.edu/~swanson/papers/science-of-writing.pdf) — 读者预期 7 原则\n- [Lipton: Heuristics for Scientific Writing](https://www.approximatelycorrect.com/2018/01/29/heuristics-technical-scientific-writing-machine-learning-perspective/) — 用词\n- [Perez: Easy Paper Writing Tips](https://ethanperez.net/easy-paper-writing-tips/) — 微观清晰度\n\n**API：**\n- [Semantic Scholar](https://api.semanticscholar.org/api-docs/) | [CrossRef](https://www.crossref.org/documentation/) | [arXiv](https://info.arxiv.org/help/api/)\n\n**会议官方：**\n- [NeurIPS](https://neurips.cc/) | [ICML](https://icml.cc/) | [ICLR](https://iclr.cc/) | [ACL](https://www.aclweb.org/) | [AAAI](https://aaai.org/) | [EMNLP](https://2025.emnlp.org/)\n",
      "numLines": 353,
      "startLine": 1,
      "totalLines": 353
    }
  }
}
````

</details>

---

### Tool call

_source line 7_

<details open><summary>🔧 Tool call — Read · `toolu_01Je4YSH3RPnpNPZd5gxa7bB`</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8146b578-f41a-49c2-b99a-be63bde75274",
  "uuid": "e18a7142-1bce-4ddc-93ed-accdf2b9c8c1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qd65KxaAJFk6Ua4jJJpjJv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14054,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14054
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-18T10:15:56.849Z_

<details><summary>↩ Tool result · `toolu_01Je4YSH3RPnpNPZd5gxa7bB`</summary>

````text
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
74	- **禁止过度宣传**：不说 "revolutionary"、"groundbreaking"
75	- **禁止写成 Introduction 的缩写**：Abstract 是独立阅读单元
76	- **禁止术语堆积**：如果审稿人几十秒内判断不出价值，就失败了
77	- **缩写必须定义**：Abstract 中首次出现的缩写必须展开
78	
79	### 2.3 审稿人视角检验
80	
81	写完后用这个标准自检：审稿人能否在 30 秒内判断——
82	- 问题是否重要？
83	- 方法是否清楚？
84	- 贡献是否可信？
85	- 结果是否有说服力？
86	
87	---
88	
89	## 三、Introduction 写作规范
90	
91	### 3.1 完整叙事线（5 段结构）
92	
93	Introduction 需要从一个清晰、重要的问题切入，逐步把读者带到核心贡献：
94	
95	1. **研究背景**（1-2 段）：大模型在某类能力/应用中已取得进展，但仍存在一个关键瓶颈
96	2. **问题重要性**（1 段）：结合真实应用、已有方法局限或当前趋势，说明这不是小问题
97	3. **现有方法不足**（1 段）：系统梳理为什么不够（依赖更大模型/更多数据/更复杂推理/更高成本，或只在特定 benchmark 有效）
98	4. **本文核心想法**（1 段）：我们观察到什么、提出了什么方法、为什么能解决上述问题
99	5. **贡献总结**（列表）：清楚列出方法贡献、实验贡献和分析贡献
100	
101	### 3.2 整体叙事结构
102	
103	```
104	现有进展 → 关键缺口 → 本文洞察 → 方法概述 → 实验证据 → 贡献总结
105	```
106	
107	### 3.3 禁忌
108	
109	- **禁止泛泛介绍**：不要开头就写 "LLMs have shown remarkable capabilities..."，要从具体问题切入
110	- **禁止缺少过渡**：每段之间必须有逻辑连接
111	- **禁止实验报告风格**：Introduction 不是 "我们做了 X 实验得到了 Y 结果" 的罗列
112	- 每条 Contribution 必须有对应的 section/table 支撑
113	- Contribution 列表中不能出现未在前文铺垫过的概念
114	
115	---
116	
117	## 四、Related Work 写作规范
118	
119	### 4.1 目标
120	
121	让审稿人相信：作者理解这个领域，知道自己的方法站在什么位置，清楚相对已有工作的真实增量在哪里。
122	
123	### 4.2 结构要求
124	
125	- 把已有工作分成几个清晰的主题（如模型训练、推理增强、工具调用、数据构建、评测等）
126	- 每类简要说明：已有方法做了什么、解决了哪些问题、和本文的关系
127	- 帮助读者理解：哪些是本文直接继承的，哪些方法不同但解决相似问题，哪些留下了本文要解决的缺口
128	
129	### 4.3 禁忌
130	
131	- **禁止论文堆砌**：不要写成 "A proposed X. B proposed Y. C proposed Z." 的列表
132	- **目标不是展示读了多少论文**，而是做归纳和比较
133	- Contribution claim（"To our knowledge, no prior work..."）应放在 Introduction，不在 Related Work
134	
135	### 4.4 引用充足度
136	
137	- 引用必须覆盖：**直接相关方法、baseline 论文、评测 benchmark 论文、理论基础**
138	- 任何一类缺失，审稿人会立刻看出来调研不充分
139	- 引用密度参照目标会议近年录用论文的量级——明显偏少意味着 Related Work 调研不足
140	
141	---
142	
143	## 五、去 AI 写作风格（硬规则）
144	
145	以下模式是 AI 生成文本的典型标志，审稿人一眼能看出。**必须全部消除。**
146	
147	### 5.1 严禁破折号（最显著的 AI 痕迹）
148	
149	**这是 AI 写作最容易被识别的标志，审稿人最敏感。单列为最高优先级硬规则。**
150	
151	- 解释性 em-dash（—，U+2014）和 en-dash（–，U+2013）必须**全部删除**
152	- 替代方式：用逗号、括号或拆分为两个句子
153	- 强制检查命令：
154	  ```bash
155	  grep -n "—" paper/*.tex     # em-dash，每处人工判断是否必要
156	  grep -n " – " paper/*.tex   # 解释性 en-dash，几乎都应删除
157	  ```
158	- 例外（允许保留）：表格分隔符、数字范围（`2020–2024`、`pp. 12–18`）、专有名词（`Newton–Raphson`）
159	
160	### 5.2 段落与句式
161	
162	- **禁止过度分段**：不需要每 2-3 句就换段，自然段 5-8 句是正常的
163	- **减少关系从句**（which, that, who）：能用简洁直接的句子就不用从句
164	- **禁止 -ing 短语结尾**：如 "..., highlighting the applicability of..." / "..., demonstrating the effectiveness of..."。这是 AI 写作最典型的标志之一
165	- **禁止连续使用 "Furthermore" / "Moreover" / "Additionally"**：一段内最多用一个过渡词
166	- **避免 "It is worth noting that..." / "Notably, ..."**：直接写要说的内容
167	
168	### 5.3 用词黑名单
169	
170	- 避免 "delve into" / "leverage" / "utilize" / "facilitate" — 用 "explore" / "use" / "enable"
171	- 避免 "a myriad of" / "a plethora of" — 用 "many" / "various"
172	- 避免 "in the realm of" / "in the context of" — 直接说
173	- 避免 "paradigm shift" / "novel" 过度使用
174	
175	### 5.4 校对清单（4 步）
176	
177	1. 全文 proofread 语法和拼写
178	2. 检查所有代词/指示词（this, that, it）是否指代明确
179	3. **`grep "—"` + `grep " – "` 全文清零**（删除所有解释性 dash，§5.1）
180	4. `grep "ing,"` 模式——大部分 -ing 分词短语需要改写
181	
182	---
183	
184	## 六、图表与视觉规范
185	
186	### 6.1 知识密度原则
187	
188	- **图表的信息必须紧凑**——不能为了美观而留大量白空间
189	- 一张图如果只传达一个简单信息，要么缩小要么合并到其他图中
190	- 能用 inline text 说清的不要占一整个 Figure
191	
192	### 6.2 表格规范
193	
194	- 表格和正文文字不能视觉重叠（检查 column 宽度和 alignment）
195	- 小数精度全表统一
196	- 最优加粗、次优下划线
197	- Caption 必须自包含
198	
199	### 6.3 图片规范
200	
201	- 数值标签不能被线、bar、点遮住——用白色背景或偏移标签
202	- 图中字体 >= 7pt（打印后仍可读）
203	- 栏宽约束需匹配目标 venue 模板要求
204	- 概念图/流程图要有信息量，不要画一个 trivial 的 pipeline 然后占半页
205	
206	### 6.4 空间效率
207	
208	- 顶会正文页数严格受限（具体页数查目标会议官网），每 cm² 都是宝贵资源
209	- 优先使用 `\subfigure` 合并相关图
210	- Table 能 inline 就不要单独浮动
211	- 图表占比与其对叙事的贡献成正比
212	
213	---
214	
215	## 七、投稿前通用准备
216	
217	### 7.1 模板必须官方（硬规则）
218	
219	- LaTeX 模板**必须从目标会议官网下载**（CallForPapers / Author Instructions 页面）
220	- **不要用**：
221	  - 网上他人转载的复制版本（可能被改过 margin / 行号设置）
222	  - 上一年的模板（参数可能变：字体、margin、行号、anonymous 选项等）
223	  - 组里学长留的旧版本（来源不明、无法追溯）
224	- 风险：
225	  - 样式不符合 → desk reject
226	  - margin 不对 → 被审稿人质疑诚信
227	  - reference 格式错 → 被认为不规范
228	- 流程：先查会议官网 templates → 找不到再 `WebSearch "{venue} {year} latex template official"` → 仍找不到汇报 Director（不要用就近年版本顶替）
229	- `\documentclass[]{}` 选项必须与目标 venue + 阶段（review / camera-ready）一致
230	
231	### 7.2 投稿要求逐项核对
232	
233	- 目标会议如要求 Checklist / Ethical Statement / Broader Impact Statement / Reproducibility Statement，必须**认真填每一项**，不要全写 N/A
234	- 页数限制：查目标会议官网
235	- 匿名化要求：review 版 vs camera-ready 版本设置不同
236	- 行号开启（review 版常需）
237	- 字体大小、margin 不得修改 sty 文件
238	
239	### 7.3 最终修改 10 项检查流程
240	
241	提交前必须逐一检查：
242	1. 所有最新实验结果已全部录入
243	2. 根据实验结果将叙事调至最优状态
244	3. 附录所有内容在正文中被引用且融入叙事
245	4. 无数据堆砌（每个数字服务于叙事推进）
246	5. Abstract 和 Introduction 具有吸引力（不是实验报告风格）
247	6. 全文主线统一（idea 变化后各章节逻辑一致）
248	7. 所有专有名词有定义
249	8. 无 AI 风格标志（dash、-ing phrases、过度分段）
250	9. 图表知识密度高、无视觉遮挡
251	10. Reference 覆盖直接相关方法、baseline、benchmark、理论基础
252	
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8146b578-f41a-49c2-b99a-be63bde75274",
  "uuid": "3f39232b-be00-4b3d-b4ee-d4cb79c35abb",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md",
      "content": "---\nname: paper-writing-norms\ndescription: 顶会级别论文写作风格规范——章节写法（Abstract/Intro/Related Work）、去 AI 风格、视觉密度、叙事哲学。Paper Agent 和 Worker 写论文章节时必须加载。\nallowed-tools: [Read, Write, Edit, Glob, Grep]\nscope: global\nversion: 2\npriority: 9\ntags:\n  - writing\n  - paper\n  - style\n  - norms\nroles:\n  - agent\n  - worker\n  - paper_agent\n---\n\n# 论文写作风格规范\n\n> 核心哲学：**论文是一个有说服力的故事，不是实验报告。** 审稿人在几十秒内判断论文价值——如果 Abstract 和 Introduction 读起来像实验日志，论文就已经失败了。\n\n---\n\n## 一、总体写作哲学\n\n### 1.1 故事驱动，不是数据堆砌\n\n- 论文必须以\"故事线\"为核心展开：问题 → 洞察 → 方法 → 验证\n- 禁止大量实验数据堆砌——每个数字出现必须服务于叙事推进\n- 附录内容必须在正文中有明确引用且融入叙事，禁止简单堆砌\n- 如果附录数据对核心叙事有重大影响，根据附录数据调整论文 framing\n\n### 1.2 主线统一性\n\n- 当 idea 在研究过程中发生变化后，**必须重审全文逻辑**\n- 常见问题：Introduction 讲的故事 A，Method 做的是故事 B，Results 又在讲故事 C\n- 修复方式：从最终实验结论反推，重写 Introduction 的问题定义和动机\n- 每次 idea 调整后检查：Abstract → Introduction → Method → Results → Discussion → Conclusion 是否形成一条连贯主线\n\n### 1.3 专有名词必须有定义\n\n- 首次出现的专有名词/缩写必须给出完整定义和解释\n- Abstract 中使用的缩写也必须在 Abstract 内定义（如 LLM = Large Language Model）\n- 不能假设读者知道你自己定义的术语——论文从来没解释过的概念不能直接使用\n- 通用规则：如果一个非标准术语第一次出现时没有括号定义，就是写作 bug\n\n### 1.4 写作前必读同类优秀论文\n\n- 每个章节动笔前，找 **2-3 篇目标会议近 1-2 年的高分论文**作为风格参考——同类问题或同类方法皆可\n- 重点学：\n  - Abstract 怎么用最少篇幅讲完故事\n  - Introduction 怎么从大问题切入到具体贡献\n  - Related Work 怎么 positioning 自己（不是 survey）\n  - Table/Figure 怎么压缩信息密度\n- **不是抄袭**，是学习同行的故事节奏和审美——不同子领域叙事节奏差异很大\n- 实操：Paper Agent 可以从 `literature_map.yaml` 中挑 `role=foundation` 或 `role=direct-competitor` 的论文，把 `{title, venue, year, abstract}` 附在 Worker 的 task_prompt 中作为概念参考；如需学习写作风格本身，让 Worker 通过 WebSearch 取得论文链接并 fetch 全文\n\n---\n\n## 二、Abstract 写作规范\n\n### 2.1 四个必答问题（150-250 words）\n\nAbstract 必须在很短的篇幅内清楚回答：\n1. **研究什么问题** — 1-2 句话交代背景和痛点\n2. **为什么重要** — 现有方法的不足（不用写太多）\n3. **本文提出什么** — 核心贡献的关键机制（简要，不堆砌细节）\n4. **结果说明什么** — 用具体实验结论支撑贡献\n\n### 2.2 禁忌\n\n- **禁止堆砌数据**：Abstract 不是 Results 的缩写。最多引用 2-3 个关键数字，要服务于 claim\n- **禁止过度宣传**：不说 \"revolutionary\"、\"groundbreaking\"\n- **禁止写成 Introduction 的缩写**：Abstract 是独立阅读单元\n- **禁止术语堆积**：如果审稿人几十秒内判断不出价值，就失败了\n- **缩写必须定义**：Abstract 中首次出现的缩写必须展开\n\n### 2.3 审稿人视角检验\n\n写完后用这个标准自检：审稿人能否在 30 秒内判断——\n- 问题是否重要？\n- 方法是否清楚？\n- 贡献是否可信？\n- 结果是否有说服力？\n\n---\n\n## 三、Introduction 写作规范\n\n### 3.1 完整叙事线（5 段结构）\n\nIntroduction 需要从一个清晰、重要的问题切入，逐步把读者带到核心贡献：\n\n1. **研究背景**（1-2 段）：大模型在某类能力/应用中已取得进展，但仍存在一个关键瓶颈\n2. **问题重要性**（1 段）：结合真实应用、已有方法局限或当前趋势，说明这不是小问题\n3. **现有方法不足**（1 段）：系统梳理为什么不够（依赖更大模型/更多数据/更复杂推理/更高成本，或只在特定 benchmark 有效）\n4. **本文核心想法**（1 段）：我们观察到什么、提出了什么方法、为什么能解决上述问题\n5. **贡献总结**（列表）：清楚列出方法贡献、实验贡献和分析贡献\n\n### 3.2 整体叙事结构\n\n```\n现有进展 → 关键缺口 → 本文洞察 → 方法概述 → 实验证据 → 贡献总结\n```\n\n### 3.3 禁忌\n\n- **禁止泛泛介绍**：不要开头就写 \"LLMs have shown remarkable capabilities...\"，要从具体问题切入\n- **禁止缺少过渡**：每段之间必须有逻辑连接\n- **禁止实验报告风格**：Introduction 不是 \"我们做了 X 实验得到了 Y 结果\" 的罗列\n- 每条 Contribution 必须有对应的 section/table 支撑\n- Contribution 列表中不能出现未在前文铺垫过的概念\n\n---\n\n## 四、Related Work 写作规范\n\n### 4.1 目标\n\n让审稿人相信：作者理解这个领域，知道自己的方法站在什么位置，清楚相对已有工作的真实增量在哪里。\n\n### 4.2 结构要求\n\n- 把已有工作分成几个清晰的主题（如模型训练、推理增强、工具调用、数据构建、评测等）\n- 每类简要说明：已有方法做了什么、解决了哪些问题、和本文的关系\n- 帮助读者理解：哪些是本文直接继承的，哪些方法不同但解决相似问题，哪些留下了本文要解决的缺口\n\n### 4.3 禁忌\n\n- **禁止论文堆砌**：不要写成 \"A proposed X. B proposed Y. C proposed Z.\" 的列表\n- **目标不是展示读了多少论文**，而是做归纳和比较\n- Contribution claim（\"To our knowledge, no prior work...\"）应放在 Introduction，不在 Related Work\n\n### 4.4 引用充足度\n\n- 引用必须覆盖：**直接相关方法、baseline 论文、评测 benchmark 论文、理论基础**\n- 任何一类缺失，审稿人会立刻看出来调研不充分\n- 引用密度参照目标会议近年录用论文的量级——明显偏少意味着 Related Work 调研不足\n\n---\n\n## 五、去 AI 写作风格（硬规则）\n\n以下模式是 AI 生成文本的典型标志，审稿人一眼能看出。**必须全部消除。**\n\n### 5.1 严禁破折号（最显著的 AI 痕迹）\n\n**这是 AI 写作最容易被识别的标志，审稿人最敏感。单列为最高优先级硬规则。**\n\n- 解释性 em-dash（—，U+2014）和 en-dash（–，U+2013）必须**全部删除**\n- 替代方式：用逗号、括号或拆分为两个句子\n- 强制检查命令：\n  ```bash\n  grep -n \"—\" paper/*.tex     # em-dash，每处人工判断是否必要\n  grep -n \" – \" paper/*.tex   # 解释性 en-dash，几乎都应删除\n  ```\n- 例外（允许保留）：表格分隔符、数字范围（`2020–2024`、`pp. 12–18`）、专有名词（`Newton–Raphson`）\n\n### 5.2 段落与句式\n\n- **禁止过度分段**：不需要每 2-3 句就换段，自然段 5-8 句是正常的\n- **减少关系从句**（which, that, who）：能用简洁直接的句子就不用从句\n- **禁止 -ing 短语结尾**：如 \"..., highlighting the applicability of...\" / \"..., demonstrating the effectiveness of...\"。这是 AI 写作最典型的标志之一\n- **禁止连续使用 \"Furthermore\" / \"Moreover\" / \"Additionally\"**：一段内最多用一个过渡词\n- **避免 \"It is worth noting that...\" / \"Notably, ...\"**：直接写要说的内容\n\n### 5.3 用词黑名单\n\n- 避免 \"delve into\" / \"leverage\" / \"utilize\" / \"facilitate\" — 用 \"explore\" / \"use\" / \"enable\"\n- 避免 \"a myriad of\" / \"a plethora of\" — 用 \"many\" / \"various\"\n- 避免 \"in the realm of\" / \"in the context of\" — 直接说\n- 避免 \"paradigm shift\" / \"novel\" 过度使用\n\n### 5.4 校对清单（4 步）\n\n1. 全文 proofread 语法和拼写\n2. 检查所有代词/指示词（this, that, it）是否指代明确\n3. **`grep \"—\"` + `grep \" – \"` 全文清零**（删除所有解释性 dash，§5.1）\n4. `grep \"ing,\"` 模式——大部分 -ing 分词短语需要改写\n\n---\n\n## 六、图表与视觉规范\n\n### 6.1 知识密度原则\n\n- **图表的信息必须紧凑**——不能为了美观而留大量白空间\n- 一张图如果只传达一个简单信息，要么缩小要么合并到其他图中\n- 能用 inline text 说清的不要占一整个 Figure\n\n### 6.2 表格规范\n\n- 表格和正文文字不能视觉重叠（检查 column 宽度和 alignment）\n- 小数精度全表统一\n- 最优加粗、次优下划线\n- Caption 必须自包含\n\n### 6.3 图片规范\n\n- 数值标签不能被线、bar、点遮住——用白色背景或偏移标签\n- 图中字体 >= 7pt（打印后仍可读）\n- 栏宽约束需匹配目标 venue 模板要求\n- 概念图/流程图要有信息量，不要画一个 trivial 的 pipeline 然后占半页\n\n### 6.4 空间效率\n\n- 顶会正文页数严格受限（具体页数查目标会议官网），每 cm² 都是宝贵资源\n- 优先使用 `\\subfigure` 合并相关图\n- Table 能 inline 就不要单独浮动\n- 图表占比与其对叙事的贡献成正比\n\n---\n\n## 七、投稿前通用准备\n\n### 7.1 模板必须官方（硬规则）\n\n- LaTeX 模板**必须从目标会议官网下载**（CallForPapers / Author Instructions 页面）\n- **不要用**：\n  - 网上他人转载的复制版本（可能被改过 margin / 行号设置）\n  - 上一年的模板（参数可能变：字体、margin、行号、anonymous 选项等）\n  - 组里学长留的旧版本（来源不明、无法追溯）\n- 风险：\n  - 样式不符合 → desk reject\n  - margin 不对 → 被审稿人质疑诚信\n  - reference 格式错 → 被认为不规范\n- 流程：先查会议官网 templates → 找不到再 `WebSearch \"{venue} {year} latex template official\"` → 仍找不到汇报 Director（不要用就近年版本顶替）\n- `\\documentclass[]{}` 选项必须与目标 venue + 阶段（review / camera-ready）一致\n\n### 7.2 投稿要求逐项核对\n\n- 目标会议如要求 Checklist / Ethical Statement / Broader Impact Statement / Reproducibility Statement，必须**认真填每一项**，不要全写 N/A\n- 页数限制：查目标会议官网\n- 匿名化要求：review 版 vs camera-ready 版本设置不同\n- 行号开启（review 版常需）\n- 字体大小、margin 不得修改 sty 文件\n\n### 7.3 最终修改 10 项检查流程\n\n提交前必须逐一检查：\n1. 所有最新实验结果已全部录入\n2. 根据实验结果将叙事调至最优状态\n3. 附录所有内容在正文中被引用且融入叙事\n4. 无数据堆砌（每个数字服务于叙事推进）\n5. Abstract 和 Introduction 具有吸引力（不是实验报告风格）\n6. 全文主线统一（idea 变化后各章节逻辑一致）\n7. 所有专有名词有定义\n8. 无 AI 风格标志（dash、-ing phrases、过度分段）\n9. 图表知识密度高、无视觉遮挡\n10. Reference 覆盖直接相关方法、baseline、benchmark、理论基础\n",
      "numLines": 252,
      "startLine": 1,
      "totalLines": 252
    }
  }
}
````

</details>

---

### Tool call

_source line 9_

<details open><summary>🔧 Tool call — Read · `toolu_01Udf2SfwLv1P1XgbUuap4VK`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8146b578-f41a-49c2-b99a-be63bde75274",
  "uuid": "6d1be302-ec63-44b4-a006-097169de942e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qd65KxaAJFk6Ua4jJJpjJv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14054,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14054
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-18T10:15:57.202Z_

<details><summary>↩ Tool result · `toolu_01Udf2SfwLv1P1XgbUuap4VK`</summary>

```text
1	\section{Introduction}
2	\label{sec:intro}
3	
4	% --- Para 1: VLAs are impressive but fragile under distribution shift ---
5	Vision-language-action models (VLAs) that generate actions via flow matching~\cite{black2024pi0,shukor2025smolvla,lipman2023flow} have reached high success rates on in-distribution benchmarks such as LIBERO~\cite{liu2023libero}.
6	Yet this near-saturation masks a fragile reality: visual and physical perturbations routinely encountered in deployment (camera viewpoint shifts, object layout changes, robot initial state variation) can degrade success rates by over 65 percentage points. For example, $\pi_0$ drops from 94.2\% to 6.6\% under robot initial-state perturbation, and UniVLA from 95.2\% to 4.3\% under camera viewpoint changes~\cite{fei2025liberoplus}.
7	Closing this robustness gap without retraining the base policy is a prerequisite for deploying VLAs outside tightly controlled settings.
8	
9	% --- Para 2: Existing approaches and the gap ---
10	Two lines of work address VLA robustness.
11	\emph{Training-time methods} improve the base policy itself through robustness-aware objectives~\cite{srpo2025,robustvla2025,digflow2025} or test-time reinforcement learning~\cite{liu2026ttvla}.
12	These approaches are effective but require retraining or per-task RL, and their gains are bounded by the training distribution.
13	\emph{Inference-time methods} leave the policy frozen.
14	ReconVLA~\cite{chen2026reconvla} applies conformal quantile regression to calibrate action-level uncertainty and uses these estimates for uncertainty-guided action selection and out-of-distribution detection, taking a complementary UQ-driven approach rather than learning explicit corrective residuals.
15	VLA-Pilot~\cite{li2025vlapilot} applies evolutionary optimization over action samples, but incurs 2.41\,s per control step, too slow for real-time manipulation.
16	A2C2~\cite{a2c2_2025} learns a per-step correction head for pre-generated action chunks on a frozen VLA, but applies correction unconditionally without multi-sample selection or explicit magnitude control.
17	In short, no existing inference-time method combines multi-sample conformal selection with bounded residual correction in a two-stage pipeline.
18	
19	% --- Para 3: Our approach — sample-then-correct ---
20	We introduce \textbf{ACR-VLA} (\textbf{A}daptive \textbf{C}onformal \textbf{R}efinement for VLA), an inference-time module that improves frozen VLA actions through a \emph{sample-then-correct} pipeline.
21	At each control step, ACR-VLA draws $K{=}10$ action samples from the frozen VLA, selects the most conforming candidate via Mahalanobis-based nonconformity scoring with shrinkage covariance estimation~\cite{ledoit2004well,braun2025cgs}, and then applies a learned residual correction via a lightweight \emph{Conformal Residual Module} (CRM).
22	CRM is a 330K-parameter MLP conditioned on the VLA's frozen observation embedding.
23	It predicts a small residual $\boldsymbol{\delta}$ whose $L_2$ norm is clipped to a bound $\varepsilon$, producing the corrected action $\mathbf{a}^* = a_{\mathrm{base}} + \mathrm{clip}(\boldsymbol{\delta})$.
24	The critical design insight is that correction operates on a high-quality starting point (the conformal-selected action) and that bounding the correction magnitude prevents compounding errors from destabilizing the closed-loop trajectory.
25	The base VLA is never modified; ACR-VLA attaches as a post-hoc module to any frozen flow-matching VLA.
26	
27	% --- Para 4: Key findings (with exp_id references) ---
28	We evaluate ACR-VLA on LIBERO-Object (10 tasks, 100 trials per method) and LIBERO-Spatial (10 tasks, 100 trials) using SmolVLA~\cite{shukor2025smolvla} as the frozen backbone. Three findings emerge:
29	
30	\textbf{(1)~The full pipeline significantly improves over the frozen VLA.}
31	Across five seeds on LIBERO-Object, the sample-then-correct pipeline (obs\_only, $\varepsilon{=}0.2$) achieves mean $17.0 \pm 2.8$\% versus VLA-only mean $10.75 \pm 1.5$\% ($p < 0.01$, pooled Fisher's exact test), a +6\,pp improvement.
32	% obs_only eps=0.2 seeds 42-46: 22/16/16/16/15%. VLA-only seeds 42-45: 10.75±1.5%. Argmin seeds 42-45: 13.5±2.4%.
33	The margin over conformal selection alone (Argmin mean $13.5 \pm 2.4$\%) is +3.5\,pp, consistent across seeds but not statistically significant ($p = 0.075$), suggesting larger evaluation budgets are needed to confirm this gap.
34	
35	\textbf{(2)~Observation features suffice for correction; conformal features do not help.}
36	Counter to intuition from synthetic experiments, conditioning CRM on per-DOF conformal statistics (perdof: 11.0\%) performs no better than selection alone (12.0\%), while scalar conformal conditioning (9.0\%) is actively harmful.
37	% exp_id: eval-acr-object-v4-small (perdof 11.0%), eval-acr-object-v4-scalar (9.0%)
38	Only observation-conditioned CRM (19.0\%) produces meaningful improvement.
39	This honest negative result highlights a gap between per-step prediction accuracy (where richer features help in offline evaluation) and closed-loop task success, where covariance estimation noise from $K{=}10$ samples undermines per-DOF conditioning.
40	
41	\textbf{(3)~Correction magnitude control is critical and previously unrecognized.}
42	Without magnitude bounding, the per-DOF-conditioned CRM's natural output ($\|\boldsymbol{\delta}\|_2 \approx 1.42$) causes catastrophic failure: 0\% success on LIBERO-Spatial, as compounding correction errors rapidly drive the state distribution away from the CRM's training regime.
43	Constraining corrections to $\|\boldsymbol{\delta}\|_2 \leq 0.1$ recovers the full improvement.
44	% exp_id: eval-acr-spatial-v4-default-r3 (norm=1.42, 0%), eval-acr-object-v4-obs-only (norm=0.1, 19.0%)
45	Observation-conditioned CRM maintains stable 35--36\% success on LIBERO-Spatial across $\varepsilon \in [0.05, 0.3]$, while per-DOF-conditioned CRM collapses from 35\% to 26\% over the same range. This robustness gap is the paper's strongest evidence: it holds across all tested seeds and magnitude bounds, independent of the seed-42 outlier.
46	% exp_id: eval-mag-obsonly-norm005, eval-mag-obsonly-norm03, eval-mag-perdof-norm03
47	
48	We note that correction offers targeted improvements on object-centric manipulation rather than universal gains: on LIBERO-Spatial, the best CRM variant performs within 1\,pp of the selection baseline, suggesting that the correction mechanism is most effective when distribution shift induces systematic action biases that a learned module can identify and compensate.
49	
50	% --- Para 5: Contributions ---
51	Our contributions are:
52	\begin{enumerate}[leftmargin=*,nosep]
53	  \item \textbf{A sample-then-correct pipeline for frozen VLAs.}
54	  We propose ACR-VLA, which combines conformal sample selection with learned residual correction for frozen flow-matching VLAs.
55	  On LIBERO-Object, this pipeline significantly improves over the frozen VLA baseline (+6\,pp, $p < 0.01$, 5-seed pooled test).
56	  % obs_only eps=0.2 5-seed mean 17.0±2.8% vs VLA-only 4-seed mean 10.75±1.5%
57	
58	  \item \textbf{Systematic conditioning comparison and honest negative result.}
59	  We compare three CRM conditioning variants (per-DOF conformal features, scalar uncertainty, and observation features) and find that only observation conditioning is effective.
60	  This challenges the intuition that richer uncertainty features should yield better corrections, and reveals that covariance estimation noise at $K{=}10$ undermines per-DOF conditioning in closed-loop settings.
61	
62	  \item \textbf{Systematic empirical study of correction magnitude sensitivity for VLA action refinement.}
63	  We show that unbounded correction causes catastrophic failure and that observation-conditioned CRM is uniquely robust across a $6{\times}$ range of magnitude bounds ($\varepsilon \in [0.05, 0.3]$), establishing magnitude control as a critical design axis for inference-time action correction.
64	\end{enumerate}
65	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8146b578-f41a-49c2-b99a-be63bde75274",
  "uuid": "e57b841b-d877-4152-b76c-8f1db77f826a",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/introduction.tex",
      "content": "\\section{Introduction}\n\\label{sec:intro}\n\n% --- Para 1: VLAs are impressive but fragile under distribution shift ---\nVision-language-action models (VLAs) that generate actions via flow matching~\\cite{black2024pi0,shukor2025smolvla,lipman2023flow} have reached high success rates on in-distribution benchmarks such as LIBERO~\\cite{liu2023libero}.\nYet this near-saturation masks a fragile reality: visual and physical perturbations routinely encountered in deployment (camera viewpoint shifts, object layout changes, robot initial state variation) can degrade success rates by over 65 percentage points. For example, $\\pi_0$ drops from 94.2\\% to 6.6\\% under robot initial-state perturbation, and UniVLA from 95.2\\% to 4.3\\% under camera viewpoint changes~\\cite{fei2025liberoplus}.\nClosing this robustness gap without retraining the base policy is a prerequisite for deploying VLAs outside tightly controlled settings.\n\n% --- Para 2: Existing approaches and the gap ---\nTwo lines of work address VLA robustness.\n\\emph{Training-time methods} improve the base policy itself through robustness-aware objectives~\\cite{srpo2025,robustvla2025,digflow2025} or test-time reinforcement learning~\\cite{liu2026ttvla}.\nThese approaches are effective but require retraining or per-task RL, and their gains are bounded by the training distribution.\n\\emph{Inference-time methods} leave the policy frozen.\nReconVLA~\\cite{chen2026reconvla} applies conformal quantile regression to calibrate action-level uncertainty and uses these estimates for uncertainty-guided action selection and out-of-distribution detection, taking a complementary UQ-driven approach rather than learning explicit corrective residuals.\nVLA-Pilot~\\cite{li2025vlapilot} applies evolutionary optimization over action samples, but incurs 2.41\\,s per control step, too slow for real-time manipulation.\nA2C2~\\cite{a2c2_2025} learns a per-step correction head for pre-generated action chunks on a frozen VLA, but applies correction unconditionally without multi-sample selection or explicit magnitude control.\nIn short, no existing inference-time method combines multi-sample conformal selection with bounded residual correction in a two-stage pipeline.\n\n% --- Para 3: Our approach — sample-then-correct ---\nWe introduce \\textbf{ACR-VLA} (\\textbf{A}daptive \\textbf{C}onformal \\textbf{R}efinement for VLA), an inference-time module that improves frozen VLA actions through a \\emph{sample-then-correct} pipeline.\nAt each control step, ACR-VLA draws $K{=}10$ action samples from the frozen VLA, selects the most conforming candidate via Mahalanobis-based nonconformity scoring with shrinkage covariance estimation~\\cite{ledoit2004well,braun2025cgs}, and then applies a learned residual correction via a lightweight \\emph{Conformal Residual Module} (CRM).\nCRM is a 330K-parameter MLP conditioned on the VLA's frozen observation embedding.\nIt predicts a small residual $\\boldsymbol{\\delta}$ whose $L_2$ norm is clipped to a bound $\\varepsilon$, producing the corrected action $\\mathbf{a}^* = a_{\\mathrm{base}} + \\mathrm{clip}(\\boldsymbol{\\delta})$.\nThe critical design insight is that correction operates on a high-quality starting point (the conformal-selected action) and that bounding the correction magnitude prevents compounding errors from destabilizing the closed-loop trajectory.\nThe base VLA is never modified; ACR-VLA attaches as a post-hoc module to any frozen flow-matching VLA.\n\n% --- Para 4: Key findings (with exp_id references) ---\nWe evaluate ACR-VLA on LIBERO-Object (10 tasks, 100 trials per method) and LIBERO-Spatial (10 tasks, 100 trials) using SmolVLA~\\cite{shukor2025smolvla} as the frozen backbone. Three findings emerge:\n\n\\textbf{(1)~The full pipeline significantly improves over the frozen VLA.}\nAcross five seeds on LIBERO-Object, the sample-then-correct pipeline (obs\\_only, $\\varepsilon{=}0.2$) achieves mean $17.0 \\pm 2.8$\\% versus VLA-only mean $10.75 \\pm 1.5$\\% ($p < 0.01$, pooled Fisher's exact test), a +6\\,pp improvement.\n% obs_only eps=0.2 seeds 42-46: 22/16/16/16/15%. VLA-only seeds 42-45: 10.75±1.5%. Argmin seeds 42-45: 13.5±2.4%.\nThe margin over conformal selection alone (Argmin mean $13.5 \\pm 2.4$\\%) is +3.5\\,pp, consistent across seeds but not statistically significant ($p = 0.075$), suggesting larger evaluation budgets are needed to confirm this gap.\n\n\\textbf{(2)~Observation features suffice for correction; conformal features do not help.}\nCounter to intuition from synthetic experiments, conditioning CRM on per-DOF conformal statistics (perdof: 11.0\\%) performs no better than selection alone (12.0\\%), while scalar conformal conditioning (9.0\\%) is actively harmful.\n% exp_id: eval-acr-object-v4-small (perdof 11.0%), eval-acr-object-v4-scalar (9.0%)\nOnly observation-conditioned CRM (19.0\\%) produces meaningful improvement.\nThis honest negative result highlights a gap between per-step prediction accuracy (where richer features help in offline evaluation) and closed-loop task success, where covariance estimation noise from $K{=}10$ samples undermines per-DOF conditioning.\n\n\\textbf{(3)~Correction magnitude control is critical and previously unrecognized.}\nWithout magnitude bounding, the per-DOF-conditioned CRM's natural output ($\\|\\boldsymbol{\\delta}\\|_2 \\approx 1.42$) causes catastrophic failure: 0\\% success on LIBERO-Spatial, as compounding correction errors rapidly drive the state distribution away from the CRM's training regime.\nConstraining corrections to $\\|\\boldsymbol{\\delta}\\|_2 \\leq 0.1$ recovers the full improvement.\n% exp_id: eval-acr-spatial-v4-default-r3 (norm=1.42, 0%), eval-acr-object-v4-obs-only (norm=0.1, 19.0%)\nObservation-conditioned CRM maintains stable 35--36\\% success on LIBERO-Spatial across $\\varepsilon \\in [0.05, 0.3]$, while per-DOF-conditioned CRM collapses from 35\\% to 26\\% over the same range. This robustness gap is the paper's strongest evidence: it holds across all tested seeds and magnitude bounds, independent of the seed-42 outlier.\n% exp_id: eval-mag-obsonly-norm005, eval-mag-obsonly-norm03, eval-mag-perdof-norm03\n\nWe note that correction offers targeted improvements on object-centric manipulation rather than universal gains: on LIBERO-Spatial, the best CRM variant performs within 1\\,pp of the selection baseline, suggesting that the correction mechanism is most effective when distribution shift induces systematic action biases that a learned module can identify and compensate.\n\n% --- Para 5: Contributions ---\nOur contributions are:\n\\begin{enumerate}[leftmargin=*,nosep]\n  \\item \\textbf{A sample-then-correct pipeline for frozen VLAs.}\n  We propose ACR-VLA, which combines conformal sample selection with learned residual correction for frozen flow-matching VLAs.\n  On LIBERO-Object, this pipeline significantly improves over the frozen VLA baseline (+6\\,pp, $p < 0.01$, 5-seed pooled test).\n  % obs_only eps=0.2 5-seed mean 17.0±2.8% vs VLA-only 4-seed mean 10.75±1.5%\n\n  \\item \\textbf{Systematic conditioning comparison and honest negative result.}\n  We compare three CRM conditioning variants (per-DOF conformal features, scalar uncertainty, and observation features) and find that only observation conditioning is effective.\n  This challenges the intuition that richer uncertainty features should yield better corrections, and reveals that covariance estimation noise at $K{=}10$ undermines per-DOF conditioning in closed-loop settings.\n\n  \\item \\textbf{Systematic empirical study of correction magnitude sensitivity for VLA action refinement.}\n  We show that unbounded correction causes catastrophic failure and that observation-conditioned CRM is uniquely robust across a $6{\\times}$ range of magnitude bounds ($\\varepsilon \\in [0.05, 0.3]$), establishing magnitude control as a critical design axis for inference-time action correction.\n\\end{enumerate}\n",
      "numLines": 65,
      "startLine": 1,
      "totalLines": 65
    }
  }
}
```

</details>

---

### Tool call

_source line 11_

<details open><summary>🔧 Tool call — Read · `toolu_01VF2AaLuPQ3RQoogwA4Lcxv`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8146b578-f41a-49c2-b99a-be63bde75274",
  "uuid": "71cb4d4d-79fc-437e-a9c6-d5631b707e13",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qd65KxaAJFk6Ua4jJJpjJv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14054,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14054
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-18T10:15:58.120Z_

<details><summary>↩ Tool result · `toolu_01VF2AaLuPQ3RQoogwA4Lcxv`</summary>

```text
1	
2	\section{Method}
3	\label{sec:method}
4	
5	\textbf{ACR-VLA} improves actions from a frozen flow-matching VLA at inference time through a sample-then-correct pipeline (Figure~\ref{fig:pipeline}): draw $K$ action samples, select the candidate closest to the sample mean, and apply a learned residual correction bounded in magnitude. The base VLA is never retrained.
6	
7	\subsection{Problem Setup}
8	\label{sec:problem_setup}
9	
10	Let $\pi_\theta$ be a frozen flow-matching VLA that, given an observation $o_t$ (image, language instruction, proprioceptive state), generates action chunks of length $C{=}50$ in $\mathbb{R}^{d \times C}$ with $d{=}6$ (3 translation + 3 rotation). Under receding-horizon execution, only the first $H{=}5$ steps of each chunk influence the robot before re-planning, so we discard the remainder. The gripper dimension is handled separately via direct thresholding and is excluded from the pipeline.
11	
12	We instantiate ACR-VLA on SmolVLA~\cite{shukor2025smolvla}, a 450M-parameter flow-matching VLA that generates actions via learned flow matching~\cite{lipman2023flow}. Each forward pass produces a stochastic action sample, so querying $\pi_\theta$ independently $K$ times yields $K$ candidate action chunks. Our goal is to produce a single action more accurate than any individual sample, with no changes to~$\pi_\theta$. The method applies to any flow-matching VLA that supports repeated sampling.
13	
14	\subsection{Multi-Sample Selection}
15	\label{sec:selection}
16	
17	We draw $K{=}10$ action chunks from $\pi_\theta$ via independent flow-matching rollouts and truncate each to $H{=}5$ steps, yielding samples $\{a_h^{(k)}\}_{k=1}^K$ with $a_h^{(k)} \in \mathbb{R}^d$ for horizon step $h = 1, \dots, H$. For each step, we compute the sample mean $\boldsymbol{\mu}_h = \frac{1}{K}\sum_{k=1}^K a_h^{(k)}$ and select the sample with the smallest total $L_2$ distance to the mean across all horizon steps:
18	\begin{equation}
19	  a_{\mathrm{base}} = \argmin_{k \in \{1,\dots,K\}} \sum_{h=1}^{H} \bigl\|a_h^{(k)} - \boldsymbol{\mu}_h\bigr\|_2^2.
20	  \label{eq:argmin}
21	\end{equation}
22	This procedure identifies the most representative sample from the action distribution. Unlike the element-wise mean, which blends potentially incompatible action modes and can produce out-of-distribution actions, argmin selection returns an actual sample from the VLA's generative process and preserves within-sample temporal coherence across the $H$ steps. The selection operates independently of the downstream correction module: it is a statistical denoising step that provides the CRM with a higher-quality starting point.
23	
24	\subsection{Correction Module (CRM)}
25	\label{sec:crm}
26	
27	The CRM is a lightweight MLP that refines the selected action $a_{\mathrm{base}}$ by predicting a bounded residual correction conditioned on the current observation and the selected action itself.
28	
29	\paragraph{Architecture.}
30	The CRM consists of three fully connected layers with ReLU activations: $\mathrm{Linear}(n_{\mathrm{in}}, 256) \to \mathrm{ReLU} \to \mathrm{Linear}(256, 256) \to \mathrm{ReLU} \to \mathrm{Linear}(256, 30)$, preceded by input normalization. For the primary obs\_only variant ($n_{\mathrm{in}}{=}990$), the input is the concatenation of the frozen observation embedding $\mathbf{z}_{\mathrm{obs}} \in \mathbb{R}^{960}$ from SmolVLA's vision-language encoder and the selected action $a_{\mathrm{base}} \in \mathbb{R}^{30}$ ($H{=}5$ steps $\times$ $d{=}6$ DOFs), for a total of 327,198 parameters (${\sim}$327K). The output is a residual $\boldsymbol{\delta} \in \mathbb{R}^{30}$, and the corrected action is:
31	\begin{equation}
32	  \mathbf{a}^* = a_{\mathrm{base}} + \mathrm{clip}\bigl(\boldsymbol{\delta},\; \|\boldsymbol{\delta}\|_2 \leq \varepsilon\bigr),
33	  \label{eq:crm}
34	\end{equation}
35	where $\varepsilon$ is a norm bound that limits the correction magnitude (Section~\ref{sec:magnitude}). The CRM never sees individual action candidates: it receives only the already-selected $a_{\mathrm{base}}$ and predicts a correction toward the expert action.
36	
37	\paragraph{Conditioning variants.}
38	We compare three CRM variants that share the same MLP architecture but differ in their input:
39	\begin{itemize}[nosep]
40	  \item \textbf{obs\_only} (primary): $[\mathbf{z}_{\mathrm{obs}};\, a_{\mathrm{base}}] \in \mathbb{R}^{990}$, 327K parameters. No conformal or uncertainty features.
41	  \item \textbf{perdof}: $[\mathbf{z}_{\mathrm{obs}};\, a_{\mathrm{base}};\, \mathbf{u}_{\mathrm{dof}}] \in \mathbb{R}^{1030}$, 337K parameters. The 40-dimensional vector $\mathbf{u}_{\mathrm{dof}}$ consists of 30 per-DOF standard deviations ($H{\times}d$), 5 conformal prediction radii~\cite{angelopoulos2023gentle} (one per horizon step), and 5 log-volume terms derived from the Ledoit--Wolf shrinkage covariance~\cite{ledoit2004well} of the $K$ samples.
42	  \item \textbf{scalar}: $[\mathbf{z}_{\mathrm{obs}};\, a_{\mathrm{base}};\, u_s] \in \mathbb{R}^{991}$, 327K parameters, where $u_s$ is a single scalar uncertainty summary.
43	\end{itemize}
44	The obs\_only variant is our primary method. Despite the name ``Conformal Residual Module,'' the primary variant does not condition on conformal statistics. The perdof variant conditions on conformal-calibrated uncertainty features~\cite{braun2025cgs}, but Section~\ref{sec:ablation} shows that these features fail to improve closed-loop performance at the $K{=}10$ sample budget.
45	
46	\paragraph{Training.}
47	The CRM is trained offline on demonstration trajectories from LIBERO~\cite{liu2023libero} with $L_2$ loss:
48	\begin{equation}
49	  \mathcal{L} = \bigl\|\mathbf{a}^* - \mathbf{a}_{\mathrm{expert}}\bigr\|_2^2,
50	  \label{eq:loss}
51	\end{equation}
52	where $\mathbf{a}_{\mathrm{expert}}$ is the demonstration action. The training set comprises 26{,}737 precomputed samples from 10 demonstrations per task across 20 LIBERO tasks. For each demonstration step, we run $K{=}10$ forward passes through the frozen SmolVLA, apply argmin selection~(\ref{eq:argmin}) to obtain $a_{\mathrm{base}}$, and train the CRM to predict the residual that moves $a_{\mathrm{base}}$ toward $\mathbf{a}_{\mathrm{expert}}$. Data augmentation includes additive Gaussian noise on the mean-action vector ($\sigma \in [0.02, 0.1]$) and, for variants that receive uncertainty inputs, noise on those features ($\sigma \approx 0.006$). Both forms of augmentation improve generalization to the state distribution encountered during closed-loop evaluation, which diverges from the demonstration distribution due to compounding errors~\cite{ross2011dagger}.
53	
54	\subsection{Magnitude Control}
55	\label{sec:magnitude}
56	
57	The norm bound $\varepsilon$ in~(\ref{eq:crm}) controls how far the CRM can deviate from the selected action and is critical for stable closed-loop performance.
58	
59	Without clipping, the CRM's natural output has $\|\boldsymbol{\delta}\|_2 \approx 1.42$. At this magnitude, compounding error across the trajectory destroys task performance: the perdof variant achieves 0\% success on LIBERO-Spatial across three seeds. Each over-corrected action shifts the state distribution away from the CRM's training regime, and subsequent corrections compound the deviation. This failure is analogous to the compounding error problem in imitation learning~\cite{ross2011dagger} but manifests at inference time rather than during data collection.
60	% exp_id: eval-acr-spatial-v4-default-r3 (uncapped norm~1.42, perdof 0%, 3 seeds)
61	
62	Constraining $\varepsilon$ to $[0.05, 0.2]$ yields stable corrections. We use $\varepsilon{=}0.2$ as the primary setting. The obs\_only variant is robust across all tested bounds ($\varepsilon \in [0.03, \text{uncapped}]$), maintaining 13.5--17.5\% on LIBERO-Object across five seeds. The perdof variant degrades progressively as $\varepsilon$ increases, collapsing from 14\% to 0\% over the same range. The root cause is rank-deficient covariance estimation at dimension-to-sample ratio $d/K = 0.6$: noisy per-DOF directional signals are harmless when clipped to small magnitude but catastrophic when the bound is loose. Section~\ref{sec:magnitude_results} presents the full sensitivity analysis.
63	% exp_id: magnitude sweep obs_only seeds 42-46, perdof seeds 42-46
64	
65	The necessity of magnitude control connects ACR-VLA to the residual policy learning literature. Silver et al.~\cite{silver2018residual} introduced residual learning with zero-initialization for combining learned and classical controllers. TRANSIC~\cite{jiang2024transic} applies learned binary gating to selectively enable residual actions. PLD~\cite{xiao2026pld} bounds corrections within a fixed range during RL training. ACR-VLA uses fixed $L_2$ norm clipping, the simplest instantiation: a hard constraint that prevents the correction from overwhelming the base policy, with no learned gating or multi-stage pipeline.
66	
67	\subsection{Inference Protocol}
68	\label{sec:inference_protocol}
69	
70	Each control step proceeds as follows:
71	\begin{enumerate}[nosep]
72	  \item Draw $K{=}10$ action chunks from the frozen VLA $\pi_\theta$ and truncate to $H{=}5$ steps.
73	  \item Compute the sample mean $\boldsymbol{\mu}_h$ per horizon step and select $a_{\mathrm{base}}$ via $L_2$ argmin~(\ref{eq:argmin}).
74	  \item Extract the observation embedding $\mathbf{z}_{\mathrm{obs}}$ from the frozen VLA encoder.
75	  \item Compute $\boldsymbol{\delta} = \mathrm{CRM}([\mathbf{z}_{\mathrm{obs}};\, a_{\mathrm{base}}])$ and clip to $\|\boldsymbol{\delta}\|_2 \leq \varepsilon$.
76	  \item Execute the first action of $\mathbf{a}^* = a_{\mathrm{base}} + \mathrm{clip}(\boldsymbol{\delta})$.
77	  \item Observe new state and re-plan from step~1.
78	\end{enumerate}
79	The computational overhead is $K{=}10$ extra forward passes through the base VLA plus ${\sim}$3\,ms for CRM inference. The base VLA is never modified.
80	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8146b578-f41a-49c2-b99a-be63bde75274",
  "uuid": "6b5cd677-e5f1-4e0b-9805-a2c4027c447d",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/method.tex",
      "content": "\n\\section{Method}\n\\label{sec:method}\n\n\\textbf{ACR-VLA} improves actions from a frozen flow-matching VLA at inference time through a sample-then-correct pipeline (Figure~\\ref{fig:pipeline}): draw $K$ action samples, select the candidate closest to the sample mean, and apply a learned residual correction bounded in magnitude. The base VLA is never retrained.\n\n\\subsection{Problem Setup}\n\\label{sec:problem_setup}\n\nLet $\\pi_\\theta$ be a frozen flow-matching VLA that, given an observation $o_t$ (image, language instruction, proprioceptive state), generates action chunks of length $C{=}50$ in $\\mathbb{R}^{d \\times C}$ with $d{=}6$ (3 translation + 3 rotation). Under receding-horizon execution, only the first $H{=}5$ steps of each chunk influence the robot before re-planning, so we discard the remainder. The gripper dimension is handled separately via direct thresholding and is excluded from the pipeline.\n\nWe instantiate ACR-VLA on SmolVLA~\\cite{shukor2025smolvla}, a 450M-parameter flow-matching VLA that generates actions via learned flow matching~\\cite{lipman2023flow}. Each forward pass produces a stochastic action sample, so querying $\\pi_\\theta$ independently $K$ times yields $K$ candidate action chunks. Our goal is to produce a single action more accurate than any individual sample, with no changes to~$\\pi_\\theta$. The method applies to any flow-matching VLA that supports repeated sampling.\n\n\\subsection{Multi-Sample Selection}\n\\label{sec:selection}\n\nWe draw $K{=}10$ action chunks from $\\pi_\\theta$ via independent flow-matching rollouts and truncate each to $H{=}5$ steps, yielding samples $\\{a_h^{(k)}\\}_{k=1}^K$ with $a_h^{(k)} \\in \\mathbb{R}^d$ for horizon step $h = 1, \\dots, H$. For each step, we compute the sample mean $\\boldsymbol{\\mu}_h = \\frac{1}{K}\\sum_{k=1}^K a_h^{(k)}$ and select the sample with the smallest total $L_2$ distance to the mean across all horizon steps:\n\\begin{equation}\n  a_{\\mathrm{base}} = \\argmin_{k \\in \\{1,\\dots,K\\}} \\sum_{h=1}^{H} \\bigl\\|a_h^{(k)} - \\boldsymbol{\\mu}_h\\bigr\\|_2^2.\n  \\label{eq:argmin}\n\\end{equation}\nThis procedure identifies the most representative sample from the action distribution. Unlike the element-wise mean, which blends potentially incompatible action modes and can produce out-of-distribution actions, argmin selection returns an actual sample from the VLA's generative process and preserves within-sample temporal coherence across the $H$ steps. The selection operates independently of the downstream correction module: it is a statistical denoising step that provides the CRM with a higher-quality starting point.\n\n\\subsection{Correction Module (CRM)}\n\\label{sec:crm}\n\nThe CRM is a lightweight MLP that refines the selected action $a_{\\mathrm{base}}$ by predicting a bounded residual correction conditioned on the current observation and the selected action itself.\n\n\\paragraph{Architecture.}\nThe CRM consists of three fully connected layers with ReLU activations: $\\mathrm{Linear}(n_{\\mathrm{in}}, 256) \\to \\mathrm{ReLU} \\to \\mathrm{Linear}(256, 256) \\to \\mathrm{ReLU} \\to \\mathrm{Linear}(256, 30)$, preceded by input normalization. For the primary obs\\_only variant ($n_{\\mathrm{in}}{=}990$), the input is the concatenation of the frozen observation embedding $\\mathbf{z}_{\\mathrm{obs}} \\in \\mathbb{R}^{960}$ from SmolVLA's vision-language encoder and the selected action $a_{\\mathrm{base}} \\in \\mathbb{R}^{30}$ ($H{=}5$ steps $\\times$ $d{=}6$ DOFs), for a total of 327,198 parameters (${\\sim}$327K). The output is a residual $\\boldsymbol{\\delta} \\in \\mathbb{R}^{30}$, and the corrected action is:\n\\begin{equation}\n  \\mathbf{a}^* = a_{\\mathrm{base}} + \\mathrm{clip}\\bigl(\\boldsymbol{\\delta},\\; \\|\\boldsymbol{\\delta}\\|_2 \\leq \\varepsilon\\bigr),\n  \\label{eq:crm}\n\\end{equation}\nwhere $\\varepsilon$ is a norm bound that limits the correction magnitude (Section~\\ref{sec:magnitude}). The CRM never sees individual action candidates: it receives only the already-selected $a_{\\mathrm{base}}$ and predicts a correction toward the expert action.\n\n\\paragraph{Conditioning variants.}\nWe compare three CRM variants that share the same MLP architecture but differ in their input:\n\\begin{itemize}[nosep]\n  \\item \\textbf{obs\\_only} (primary): $[\\mathbf{z}_{\\mathrm{obs}};\\, a_{\\mathrm{base}}] \\in \\mathbb{R}^{990}$, 327K parameters. No conformal or uncertainty features.\n  \\item \\textbf{perdof}: $[\\mathbf{z}_{\\mathrm{obs}};\\, a_{\\mathrm{base}};\\, \\mathbf{u}_{\\mathrm{dof}}] \\in \\mathbb{R}^{1030}$, 337K parameters. The 40-dimensional vector $\\mathbf{u}_{\\mathrm{dof}}$ consists of 30 per-DOF standard deviations ($H{\\times}d$), 5 conformal prediction radii~\\cite{angelopoulos2023gentle} (one per horizon step), and 5 log-volume terms derived from the Ledoit--Wolf shrinkage covariance~\\cite{ledoit2004well} of the $K$ samples.\n  \\item \\textbf{scalar}: $[\\mathbf{z}_{\\mathrm{obs}};\\, a_{\\mathrm{base}};\\, u_s] \\in \\mathbb{R}^{991}$, 327K parameters, where $u_s$ is a single scalar uncertainty summary.\n\\end{itemize}\nThe obs\\_only variant is our primary method. Despite the name ``Conformal Residual Module,'' the primary variant does not condition on conformal statistics. The perdof variant conditions on conformal-calibrated uncertainty features~\\cite{braun2025cgs}, but Section~\\ref{sec:ablation} shows that these features fail to improve closed-loop performance at the $K{=}10$ sample budget.\n\n\\paragraph{Training.}\nThe CRM is trained offline on demonstration trajectories from LIBERO~\\cite{liu2023libero} with $L_2$ loss:\n\\begin{equation}\n  \\mathcal{L} = \\bigl\\|\\mathbf{a}^* - \\mathbf{a}_{\\mathrm{expert}}\\bigr\\|_2^2,\n  \\label{eq:loss}\n\\end{equation}\nwhere $\\mathbf{a}_{\\mathrm{expert}}$ is the demonstration action. The training set comprises 26{,}737 precomputed samples from 10 demonstrations per task across 20 LIBERO tasks. For each demonstration step, we run $K{=}10$ forward passes through the frozen SmolVLA, apply argmin selection~(\\ref{eq:argmin}) to obtain $a_{\\mathrm{base}}$, and train the CRM to predict the residual that moves $a_{\\mathrm{base}}$ toward $\\mathbf{a}_{\\mathrm{expert}}$. Data augmentation includes additive Gaussian noise on the mean-action vector ($\\sigma \\in [0.02, 0.1]$) and, for variants that receive uncertainty inputs, noise on those features ($\\sigma \\approx 0.006$). Both forms of augmentation improve generalization to the state distribution encountered during closed-loop evaluation, which diverges from the demonstration distribution due to compounding errors~\\cite{ross2011dagger}.\n\n\\subsection{Magnitude Control}\n\\label{sec:magnitude}\n\nThe norm bound $\\varepsilon$ in~(\\ref{eq:crm}) controls how far the CRM can deviate from the selected action and is critical for stable closed-loop performance.\n\nWithout clipping, the CRM's natural output has $\\|\\boldsymbol{\\delta}\\|_2 \\approx 1.42$. At this magnitude, compounding error across the trajectory destroys task performance: the perdof variant achieves 0\\% success on LIBERO-Spatial across three seeds. Each over-corrected action shifts the state distribution away from the CRM's training regime, and subsequent corrections compound the deviation. This failure is analogous to the compounding error problem in imitation learning~\\cite{ross2011dagger} but manifests at inference time rather than during data collection.\n% exp_id: eval-acr-spatial-v4-default-r3 (uncapped norm~1.42, perdof 0%, 3 seeds)\n\nConstraining $\\varepsilon$ to $[0.05, 0.2]$ yields stable corrections. We use $\\varepsilon{=}0.2$ as the primary setting. The obs\\_only variant is robust across all tested bounds ($\\varepsilon \\in [0.03, \\text{uncapped}]$), maintaining 13.5--17.5\\% on LIBERO-Object across five seeds. The perdof variant degrades progressively as $\\varepsilon$ increases, collapsing from 14\\% to 0\\% over the same range. The root cause is rank-deficient covariance estimation at dimension-to-sample ratio $d/K = 0.6$: noisy per-DOF directional signals are harmless when clipped to small magnitude but catastrophic when the bound is loose. Section~\\ref{sec:magnitude_results} presents the full sensitivity analysis.\n% exp_id: magnitude sweep obs_only seeds 42-46, perdof seeds 42-46\n\nThe necessity of magnitude control connects ACR-VLA to the residual policy learning literature. Silver et al.~\\cite{silver2018residual} introduced residual learning with zero-initialization for combining learned and classical controllers. TRANSIC~\\cite{jiang2024transic} applies learned binary gating to selectively enable residual actions. PLD~\\cite{xiao2026pld} bounds corrections within a fixed range during RL training. ACR-VLA uses fixed $L_2$ norm clipping, the simplest instantiation: a hard constraint that prevents the correction from overwhelming the base policy, with no learned gating or multi-stage pipeline.\n\n\\subsection{Inference Protocol}\n\\label{sec:inference_protocol}\n\nEach control step proceeds as follows:\n\\begin{enumerate}[nosep]\n  \\item Draw $K{=}10$ action chunks from the frozen VLA $\\pi_\\theta$ and truncate to $H{=}5$ steps.\n  \\item Compute the sample mean $\\boldsymbol{\\mu}_h$ per horizon step and select $a_{\\mathrm{base}}$ via $L_2$ argmin~(\\ref{eq:argmin}).\n  \\item Extract the observation embedding $\\mathbf{z}_{\\mathrm{obs}}$ from the frozen VLA encoder.\n  \\item Compute $\\boldsymbol{\\delta} = \\mathrm{CRM}([\\mathbf{z}_{\\mathrm{obs}};\\, a_{\\mathrm{base}}])$ and clip to $\\|\\boldsymbol{\\delta}\\|_2 \\leq \\varepsilon$.\n  \\item Execute the first action of $\\mathbf{a}^* = a_{\\mathrm{base}} + \\mathrm{clip}(\\boldsymbol{\\delta})$.\n  \\item Observe new state and re-plan from step~1.\n\\end{enumerate}\nThe computational overhead is $K{=}10$ extra forward passes through the base VLA plus ${\\sim}$3\\,ms for CRM inference. The base VLA is never modified.\n",
      "numLines": 80,
      "startLine": 1,
      "totalLines": 80
    }
  }
}
```

</details>

---

### Tool call

_source line 13_

<details open><summary>🔧 Tool call — Read · `toolu_018C83Kp9C9yKnZfseKAZ1FG`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8146b578-f41a-49c2-b99a-be63bde75274",
  "uuid": "24c80f69-5b22-43d5-8e02-78c313d1931e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qd65KxaAJFk6Ua4jJJpjJv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14054,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14054
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-18T10:15:58.243Z_

<details><summary>↩ Tool result · `toolu_018C83Kp9C9yKnZfseKAZ1FG`</summary>

```text
1	
2	\section{Experiments}
3	\label{sec:experiments}
4	
5	We evaluate ACR-VLA on two LIBERO task suites to answer three questions:
6	(i)~Does observation-conditioned residual correction significantly improve over the frozen VLA baseline?
7	(ii)~Do per-DOF conformal features provide additional benefit beyond observation conditioning?
8	(iii)~How sensitive is performance to the magnitude bound $\varepsilon$?
9	The answers are: yes (+6.3\,pp over VLA-only, $p < 0.01$), no (honest negative), and critically, unbounded correction is catastrophic, but obs\_only is robust across all tested seeds and magnitude bounds.
10	
11	\subsection{Experimental Setup}
12	\label{sec:exp_setup}
13	
14	\paragraph{Benchmarks.}
15	We use two suites from the LIBERO benchmark~\cite{liu2023libero}:
16	\textbf{LIBERO-Spatial} (10 tasks requiring spatial reasoning about object layout) and \textbf{LIBERO-Object} (10 tasks requiring generalization across novel object instances).
17	Each task is evaluated over 10 rollouts with a maximum episode length of 300 steps, yielding 100 episodes per suite. Success is binary: an episode succeeds if the task predicate is satisfied before the step limit.
18	
19	\paragraph{Base VLA.}
20	We build on SmolVLA~\cite{shukor2025smolvla}, a 450M-parameter flow-matching VLA.
21	We use the checkpoint \texttt{lerobot/smolvla\_libero}, which receives dual-camera RGB input (agentview + eye-in-hand, $256{\times}256$) and 8D proprioceptive state.
22	Actions are 7D: 6D end-effector pose (3 translation + 3 rotation) plus 1D gripper, with the gripper dimension handled outside the correction pipeline via direct thresholding.
23	
24	\paragraph{Baselines.}
25	All methods use the same frozen SmolVLA checkpoint:
26	\begin{itemize}[nosep]
27	  \item \textbf{VLA-only} ($K{=}1$): single sample from the frozen VLA, no selection or correction.
28	  \item \textbf{VLA-mean} ($K{=}10$): mean of 10 independent flow-matching samples, no selection or correction.
29	  \item \textbf{Argmin} ($K{=}10$): select sample closest to sample mean via $L_2$ distance (Section~\ref{sec:selection}), no CRM correction.
30	\end{itemize}
31	
32	\paragraph{CRM variants.}
33	All CRM variants share the same 3-layer MLP architecture (input$\to$256$\to$256$\to$30) and differ only in their conditioning input:
34	\begin{itemize}[nosep]
35	  \item \textbf{obs\_only}: $[\mathbf{z}_{\mathrm{obs}};\, a_{\mathrm{base}}] \in \mathbb{R}^{990}$ (960D observation embedding + 30D selected action; ${\sim}$327K params). This is our primary method.
36	  \item \textbf{perdof}: $[\mathbf{z}_{\mathrm{obs}};\, a_{\mathrm{base}};\, \mathbf{u}_{\mathrm{dof}}] \in \mathbb{R}^{1030}$ (additional 40D per-DOF conformal features; ${\sim}$337K params).
37	  \item \textbf{scalar}: $[\mathbf{z}_{\mathrm{obs}};\, a_{\mathrm{base}};\, u_s] \in \mathbb{R}^{991}$ (additional 1D scalar uncertainty; ${\sim}$327K params).
38	\end{itemize}
39	
40	\paragraph{Training.}
41	CRM is trained on 26{,}737 precomputed samples derived from 10 demonstrations per task across all 20 LIBERO tasks.
42	For each demonstration step, we run $K{=}10$ forward passes through the frozen SmolVLA, apply argmin $L_2$ selection to obtain $a_{\mathrm{base}}$.
43	Optimization uses Adam with learning rate $10^{-3}$, batch size 32, for 50 epochs with seed 42.
44	Data augmentation includes additive Gaussian noise on the mean-action vector ($\sigma \in [0.02, 0.1]$) and uncertainty features ($\sigma \approx 0.006$).
45	The default magnitude bound is $\varepsilon = 0.2$ for all CRM variants unless stated otherwise.
46	
47	\paragraph{Statistical protocol.}
48	Table~\ref{tab:main} reports seed 42 (10 rollouts $\times$ 10 tasks = 100 episodes per suite).
49	For the primary comparison, we replicate across multiple seeds on LIBERO-Object: obs\_only ($\varepsilon{=}0.2$, 6 seeds) achieves mean $17.5 \pm 2.8$\%, VLA-only (5 seeds) achieves mean $11.2 \pm 1.6$\%, and Argmin (5 seeds) achieves mean $12.4 \pm 2.9$\%.
50	Pooled Fisher's exact test: obs\_only vs.\ VLA-only yields $p = 0.0074$ (Cohen's $d = 1.21$).
51	All six obs\_only seeds exceed the VLA-only mean, confirming reproducible improvement despite per-seed variance.
52	Multi-seed VLA-mean evaluation (4 seeds, mean 12.5\%) confirms that averaging provides no consistent benefit over single-sample execution.
53	
54	
55	\subsection{Main Results}
56	\label{sec:main_results}
57	
58	Table~\ref{tab:main} compares all methods on both benchmarks.
59	
60	\begin{table}[t]
61	\centering
62	\caption{Task success rate (\%\,$\uparrow$) on LIBERO-Object and LIBERO-Spatial (10 tasks $\times$ 10 rollouts each, seed 42). $\Delta$ denotes improvement over the Argmin selection baseline. All methods use the same frozen SmolVLA checkpoint.}
63	\label{tab:main}
64	\small
65	\begin{tabular}{lccc}
66	\toprule
67	Method & Object (\%) & Spatial (\%) & $\Delta$ Object \\
68	\midrule
69	VLA-only ($K{=}1$)    & 12.0 & 30.0 & $\phantom{+}0.0$ \\
70	VLA-mean ($K{=}10$)   & 12.0 & 32.0 & $\phantom{+}0.0$ \\
71	Argmin ($K{=}10$)      & 12.0 & 34.0 & --- \\
72	\midrule
73	scalar ($\varepsilon{=}0.1$)  & \phantom{0}9.0 & 32.0 & $-3.0$ \\
74	perdof ($\varepsilon{=}0.1$)  & 11.0 & 35.0 & $-1.0$ \\
75	\textbf{obs\_only} ($\varepsilon{=}0.1$) & \textbf{19.0} & \textbf{35.0} & $\mathbf{+7.0}$ \\
76	\midrule
77	obs\_only ($\varepsilon{=}0.2$) & \textbf{22.0} & 35.0 & $+10.0$ \\
78	\bottomrule
79	\end{tabular}
80	\end{table}
81	
82	\paragraph{Object benchmark: correction helps.}
83	On LIBERO-Object, obs\_only at $\varepsilon{=}0.1$ achieves 19.0\% (seed 42), and at $\varepsilon{=}0.2$ yields 22.0\%.
84	Across six seeds ($\varepsilon{=}0.2$), the pipeline achieves mean $17.5 \pm 2.8$\% versus VLA-only mean $11.2 \pm 1.6$\% ($p = 0.0074$, pooled Fisher's exact test; Cohen's $d = 1.21$).
85	The improvement over Argmin (mean $12.4 \pm 2.9$\%) is +5.1\,pp.
86	
87	At seed 42, three baselines (VLA-only, VLA-mean, and Argmin) all achieve 12.0\%, indicating that neither multi-sample averaging nor $L_2$ argmin selection provides meaningful benefit on this task suite.
88	The VLA-mean result is informative: averaging 10 independent flow-matching samples does not reduce error compared to a single sample ($K{=}1$), confirming that action diversity does not center around the correct action.
89	The obs\_only CRM breaks through this plateau by predicting corrective residuals conditioned on the observation embedding.
90	
91	\paragraph{Pipeline decomposition: selection and correction are synergistic.}
92	To isolate contributions, we evaluate the CRM without multi-sample selection ($K{=}1$): the CRM corrects a single VLA output directly.
93	At $K{=}1$, CRM correction achieves 10.3\% (3-seed mean), at the VLA-only level (11.2\%).
94	Argmin selection without correction achieves 12.4\% (5-seed mean), a modest +1.2\,pp gain.
95	Neither component alone meaningfully improves the frozen VLA, yet the full pipeline ($K{=}10$, selection + correction) achieves 17.5\%, a +6.3\,pp gain ($p = 0.0074$).
96	This synergy arises because argmin selection filters out the worst samples, providing the CRM with a higher-quality starting point; the CRM then applies corrections that are more reliable on these pre-screened candidates.
97	In terms of contribution decomposition: selection accounts for ${\sim}$1\,pp and correction for ${\sim}$5\,pp, with correction 4--5$\times$ more valuable than selection alone.
98	
99	\paragraph{Spatial benchmark: correction does not help.}
100	On LIBERO-Spatial, all methods cluster within a 5\,pp band (30--35\%).
101	The best CRM variants (obs\_only, perdof) achieve 35\%, only 1\,pp above the Argmin baseline (34\%).
102	This is a null result that we report prominently.
103	
104	We interpret this as follows: spatial perturbations in LIBERO-Spatial involve changes to object layout (e.g., moving target locations), which may require re-planning rather than local action correction.
105	The VLA's observation encoder cannot extract correctable error signals from spatial shifts. The problem is not that actions are inaccurate given the current state, but that the task structure itself has changed.
106	Residual correction at the action level is the wrong granularity for this type of generalization.
107	
108	\paragraph{Key finding.}
109	The full pipeline significantly improves over VLA-only for object manipulation ($p < 0.01$), where the challenge is fine-grained motor control with novel objects.
110	For spatial reasoning, where the challenge is planning under layout changes, correction at the action level provides no benefit over selection alone.
111	
112	
113	\subsection{CRM Conditioning Ablation}
114	\label{sec:ablation}
115	
116	We focus the conditioning ablation on LIBERO-Object, where meaningful differences emerge (Table~\ref{tab:main}).
117	
118	\paragraph{Ranking.}
119	obs\_only (19.0\%) $\gg$ Argmin (12.0\%) $\approx$ perdof (11.0\%) $>$ scalar (9.0\%).
120	
121	This ordering is the central negative result of our ablation: per-DOF conformal features, despite being intuitively richer (40 additional dimensions capturing per-DOF standard deviations, conformal radii, and log-volume terms), \emph{hurt} rather than help.
122	Scalar uncertainty conditioning (1 additional dimension) performs even worse, falling 3.0\,pp below the Argmin baseline that uses no correction at all.
123	
124	The scalar $<$ perdof ordering is consistent across seeds (scalar: 9\%/6\% for seeds 42/44; perdof: 11\%/8\%).
125	One-dimensional scalar uncertainty compresses all six action dimensions into a single number.
126	When certain dimensions carry high uncertainty but the correction direction is already correct along those axes, the scalar signal cannot distinguish this case from one where correction is needed everywhere.
127	The result is uniform over-correction or under-correction across all dimensions.
128	Per-DOF conditioning at least permits dimension-specific judgments, though at $K{=}10$ these judgments remain too noisy to be useful.
129	Even 1D scalar uncertainty conditioning is harmful, confirming that conformal scores at $K{=}10$ are unreliable regardless of aggregation dimensionality.
130	The noise originates in the score itself (rank-deficient covariance estimate from 10 samples in 6D), not in how these scores are decomposed across dimensions.
131	
132	\paragraph{Why does richer conditioning fail?}
133	We identify three factors:
134	
135	\emph{(1) Noisy covariance estimation.}
136	With $K{=}10$ samples in $d{=}6$ dimensions, the dimension-to-sample ratio is $d/K = 0.6$.
137	While Ledoit--Wolf shrinkage~\cite{ledoit2004well} stabilizes the covariance estimate for selection (Section~\ref{sec:selection}), the per-DOF features derived from this estimate (standard deviations, conformal radii) still carry substantial estimation noise.
138	Feeding these noisy features as CRM input introduces a distribution shift between training data (where noise patterns are consistent) and closed-loop evaluation (where compounding state-distribution drift produces different noise patterns).
139	
140	\emph{(2) Observation features are sufficient.}
141	The frozen VLA observation embedding $\mathbf{z}_{\mathrm{obs}} \in \mathbb{R}^{960}$ already encodes task-relevant geometric information: object identity, spatial layout, gripper-object relationship, and task progress.
142	This information subsumes what the per-DOF conformal features attempt to capture, namely which action dimensions are uncertain given the current scene.
143	The CRM learns to map directly from scene understanding to corrective residuals, without the intermediate conformal statistics.
144	
145	\emph{(3) Per-step MSE $\neq$ episode success.}
146	All CRM variants achieve low per-step MSE on held-out demonstration data, yet offline prediction accuracy does not predict closed-loop task success.
147	In closed-loop evaluation, small per-step errors compound and the robot visits states far from the demonstration distribution~\cite{ross2011dagger}.
148	The noisy conformal features amplify this drift: occasional erroneous correction directions, even when small in magnitude, can trigger cascading failures in individual episodes.
149	
150	\paragraph{Connection to magnitude sensitivity.}
151	The obs\_only variant is also more robust across magnitude bounds $\varepsilon$ than perdof (Section~\ref{sec:magnitude_results}), providing further evidence that observation-only conditioning yields a more stable correction signal.
152	
153	
154	\subsection{Conditioning-Magnitude Interaction}
155	\label{sec:magnitude_results}
156	
157	The norm bound $\varepsilon$ controls how far the CRM can deviate from the selected action.
158	Figure~\ref{fig:magnitude} plots success rate against $\varepsilon$ on LIBERO-Object for both conditioning variants.
159	
160	\begin{figure}[t]
161	\centering
162	\includegraphics[width=\linewidth]{figures/fig2_magnitude.pdf}
163	\caption{Success rate (\%) vs.\ magnitude bound $\varepsilon$ on LIBERO-Object. obs\_only (blue) remains above the VLA-only baseline (11.2\%, dashed) across all tested $\varepsilon$ including uncapped (${\approx}$1.42). perdof (orange) collapses progressively, reaching 0\% at the uncapped setting (3 seeds). Error bars: $\pm$1 std; hollow markers: $n < 3$.}
164	\label{fig:magnitude}
165	\end{figure}
166	
167	\paragraph{obs\_only is robust across all magnitudes.}
168	The obs\_only variant maintains 13.5--17.5\% across $\varepsilon \in [0.03, \text{uncapped}]$, peaking at 17.5\% ($\varepsilon{=}0.2$, 6 seeds) and remaining above VLA-only (11.2\%) at every tested bound, including uncapped (14.3\%, 3 seeds).
169	The practitioner need not carefully tune $\varepsilon$: any value in $[0.05, 0.3]$ yields comparable performance.
170	
171	\paragraph{perdof collapses progressively.}
172	The perdof variant starts at 14.0\% ($\varepsilon{=}0.03$, $n{=}1$), drops to 11.0\% at $\varepsilon{=}0.1$ (6 seeds), and collapses to 0\% at the uncapped setting (3 seeds, all zero).
173	This progressive degradation traces to rank-deficient covariance estimation: with $K{=}10$ samples in $d{=}6$ dimensions ($d/K = 0.6$), per-DOF features carry substantial estimation noise.
174	At tight $\varepsilon$, clipping masks the noisy correction directions; as the bound loosens, erroneous corrections compound across the trajectory.
175	
176	\paragraph{Scalar conditioning is worse than no conditioning.}
177	The scalar variant achieves 8.3\% (3 seeds at $\varepsilon{=}0.2$), below VLA-only (11.2\%).
178	This confirms that conformal statistics at $K{=}10$ are unreliable regardless of aggregation dimensionality: the noise originates in the score itself (rank-deficient covariance), not in how the scores are decomposed.
179	
180	\paragraph{Practical recommendation.}
181	We use $\varepsilon{=}0.2$ as the primary setting.
182	Within $[0.05, 0.3]$, obs\_only never degrades below the VLA-only baseline across all tested seeds.
183	
184	
185	\subsection{Inference-Time Scaling with $K$}
186	\label{sec:k_scaling}
187	
188	Figure~\ref{fig:kvalue} plots task success rate against the number of VLA samples $K$.
189	
190	\begin{figure}[t]
191	\centering
192	\includegraphics[width=\linewidth]{figures/fig3_kvalue.pdf}
193	\caption{Success rate (\%) vs.\ number of VLA samples $K$ on LIBERO-Object (obs\_only, $\varepsilon{=}0.2$). Reference lines: VLA-only (11.2\%, 5 seeds) and Argmin-only (12.4\%, 5 seeds). Error bars: $\pm$1 std where available; hollow marker for $K{=}5$ ($n{=}1$).}
194	\label{fig:kvalue}
195	\end{figure}
196	
197	Performance increases monotonically with $K$: $K{=}1$ (10.3\%, 3 seeds) $\to$ $K{=}5$ (14.0\%, 1 seed) $\to$ $K{=}10$ (17.5\%, 6 seeds).
198	At $K{=}1$, CRM correction alone performs at the VLA-only level (11.2\%), confirming that the correction module requires multi-sample selection to be effective.
199	The monotonic trend parallels inference-time compute scaling in LLMs~\cite{snell2024scaling}, where repeated sampling with selection (best-of-$N$) improves output quality.
200	In our setting, more samples yield a better argmin starting point, which in turn enables more effective correction.
201	
202	The $K{=}5$ data point is preliminary ($n{=}1$), but it falls on the monotonic trend, suggesting that even moderate sample budgets can capture partial gains.
203	The compute cost scales linearly: $K{=}10$ requires 10 forward passes through the frozen VLA plus ${\sim}$3\,ms for CRM inference, a ${\sim}$10$\times$ increase in VLA compute.
204	
205	
206	\subsection{Applicability Boundary: Stochastic VLA Diversity}
207	\label{sec:applicability}
208	
209	The multi-sample pipeline requires stochastic action diversity across samples. We test this prerequisite by comparing SmolVLA (flow-matching, 450M) with OpenVLA~\cite{kim2024openvla} (autoregressive tokenization, 7B).
210	
211	\begin{figure}[t]
212	\centering
213	\includegraphics[width=\linewidth]{figures/fig4_diversity.pdf}
214	\caption{Per-DOF action variance (log scale) across $K{=}10$ samples for SmolVLA (flow-matching) and OpenVLA (tokenized). OpenVLA produces 8/10 identical samples at temperature $T{=}0.5$, with per-DOF variance below $10^{-30}$ for most dimensions.}
215	\label{fig:diversity}
216	\end{figure}
217	
218	Figure~\ref{fig:diversity} shows the contrast: SmolVLA produces meaningfully diverse samples across all action dimensions, while OpenVLA at temperature $T{=}0.5$ generates 8 out of 10 identical action sequences, with per-DOF variance below $10^{-30}$ for most dimensions.
219	This near-determinism arises from autoregressive token selection: the argmax decoding at each token position collapses the distribution to a single mode, and moderate temperature fails to overcome the peaked distribution.
220	
221	This result establishes an applicability boundary: multi-sample inference-time correction is specific to stochastic generative VLAs (flow-matching, diffusion). Tokenized VLAs lack the action diversity that selection and correction rely on.
222	The boundary is architectural, not a limitation of our method: any inference-time approach that draws multiple action candidates requires the base policy to produce diverse samples.
223	
224	
225	\subsection{Per-Task Analysis}
226	\label{sec:per_task}
227	
228	Table~\ref{tab:pertask} reports per-task success rates on LIBERO-Object (seed 42) for the VLA-only baseline, Argmin selection, and obs\_only at two magnitude bounds.
229	
230	\begin{table}[t]
231	\centering
232	\caption{Per-task success rate (\%) on LIBERO-Object (seed 42, 10 rollouts per task). Tasks ordered by obs\_only $\varepsilon{=}0.2$ improvement over VLA-only.}
233	\label{tab:pertask}
234	\small
235	\begin{tabular}{lcccc}
236	\toprule
237	Task & VLA-only & Argmin & obs\_only 0.1 & obs\_only 0.2 \\
238	\midrule
239	chocolate\_pudding & 20 & 30 & 50 & 60 \\
240	ketchup            &  0 &  0 & 10 & 20 \\
241	bbq\_sauce         & 20 & 30 & 40 & 40 \\
242	salad\_dressing    & 20 & 10 & 20 & 30 \\
243	butter             &  0 & 10 & 10 & 10 \\
244	milk               & 10 & 10 & 20 & 20 \\
245	orange\_juice      & 30 & 30 & 30 & 30 \\
246	tomato\_sauce      & 10 &  0 &  0 & 10 \\
247	alphabet\_soup     &  0 &  0 &  0 &  0 \\
248	cream\_cheese      & 10 &  0 & 10 &  0 \\
249	\bottomrule
250	\end{tabular}
251	\end{table}
252	
253	\paragraph{Improvement concentrates on medium-difficulty tasks.}
254	The +10\,pp aggregate gain of obs\_only ($\varepsilon{=}0.2$) over VLA-only is not uniformly distributed across tasks.
255	The largest improvements appear on tasks where the frozen VLA partially succeeds but makes correctable errors: chocolate\_pudding (+40\,pp, from 20\% to 60\%), bbq\_sauce and ketchup (+20\,pp each), and salad\_dressing (+10\,pp).
256	These four tasks account for 9 of the 10 additional successes.
257	Conversely, four tasks (alphabet\_soup, cream\_cheese, tomato\_sauce, butter) remain at 0--10\% across all methods, including obs\_only.
258	For these tasks, the base policy fails so completely that local action-level correction cannot recover a viable trajectory.
259	
260	\paragraph{Implications for the correction mechanism.}
261	Correction benefits tasks where the frozen VLA partially succeeds but makes correctable errors, rather than tasks where the base policy fails catastrophically or already succeeds reliably.
262	This pattern is expected for a residual correction approach bounded by $\varepsilon$: the CRM can fix small deviations in grasp pose or approach angle, but cannot recover from fundamental planning failures (e.g., reaching toward the wrong object entirely).
263	The concentrated improvement profile also addresses the question of effect size: the aggregate +10\,pp is not a uniform +1\,pp across 10 tasks, but a substantial +20--40\,pp on specific tasks diluted by tasks outside the correctable regime.
264	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8146b578-f41a-49c2-b99a-be63bde75274",
  "uuid": "5449374d-00dc-437e-a614-e2121c36bba1",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/experiments.tex",
      "content": "\n\\section{Experiments}\n\\label{sec:experiments}\n\nWe evaluate ACR-VLA on two LIBERO task suites to answer three questions:\n(i)~Does observation-conditioned residual correction significantly improve over the frozen VLA baseline?\n(ii)~Do per-DOF conformal features provide additional benefit beyond observation conditioning?\n(iii)~How sensitive is performance to the magnitude bound $\\varepsilon$?\nThe answers are: yes (+6.3\\,pp over VLA-only, $p < 0.01$), no (honest negative), and critically, unbounded correction is catastrophic, but obs\\_only is robust across all tested seeds and magnitude bounds.\n\n\\subsection{Experimental Setup}\n\\label{sec:exp_setup}\n\n\\paragraph{Benchmarks.}\nWe use two suites from the LIBERO benchmark~\\cite{liu2023libero}:\n\\textbf{LIBERO-Spatial} (10 tasks requiring spatial reasoning about object layout) and \\textbf{LIBERO-Object} (10 tasks requiring generalization across novel object instances).\nEach task is evaluated over 10 rollouts with a maximum episode length of 300 steps, yielding 100 episodes per suite. Success is binary: an episode succeeds if the task predicate is satisfied before the step limit.\n\n\\paragraph{Base VLA.}\nWe build on SmolVLA~\\cite{shukor2025smolvla}, a 450M-parameter flow-matching VLA.\nWe use the checkpoint \\texttt{lerobot/smolvla\\_libero}, which receives dual-camera RGB input (agentview + eye-in-hand, $256{\\times}256$) and 8D proprioceptive state.\nActions are 7D: 6D end-effector pose (3 translation + 3 rotation) plus 1D gripper, with the gripper dimension handled outside the correction pipeline via direct thresholding.\n\n\\paragraph{Baselines.}\nAll methods use the same frozen SmolVLA checkpoint:\n\\begin{itemize}[nosep]\n  \\item \\textbf{VLA-only} ($K{=}1$): single sample from the frozen VLA, no selection or correction.\n  \\item \\textbf{VLA-mean} ($K{=}10$): mean of 10 independent flow-matching samples, no selection or correction.\n  \\item \\textbf{Argmin} ($K{=}10$): select sample closest to sample mean via $L_2$ distance (Section~\\ref{sec:selection}), no CRM correction.\n\\end{itemize}\n\n\\paragraph{CRM variants.}\nAll CRM variants share the same 3-layer MLP architecture (input$\\to$256$\\to$256$\\to$30) and differ only in their conditioning input:\n\\begin{itemize}[nosep]\n  \\item \\textbf{obs\\_only}: $[\\mathbf{z}_{\\mathrm{obs}};\\, a_{\\mathrm{base}}] \\in \\mathbb{R}^{990}$ (960D observation embedding + 30D selected action; ${\\sim}$327K params). This is our primary method.\n  \\item \\textbf{perdof}: $[\\mathbf{z}_{\\mathrm{obs}};\\, a_{\\mathrm{base}};\\, \\mathbf{u}_{\\mathrm{dof}}] \\in \\mathbb{R}^{1030}$ (additional 40D per-DOF conformal features; ${\\sim}$337K params).\n  \\item \\textbf{scalar}: $[\\mathbf{z}_{\\mathrm{obs}};\\, a_{\\mathrm{base}};\\, u_s] \\in \\mathbb{R}^{991}$ (additional 1D scalar uncertainty; ${\\sim}$327K params).\n\\end{itemize}\n\n\\paragraph{Training.}\nCRM is trained on 26{,}737 precomputed samples derived from 10 demonstrations per task across all 20 LIBERO tasks.\nFor each demonstration step, we run $K{=}10$ forward passes through the frozen SmolVLA, apply argmin $L_2$ selection to obtain $a_{\\mathrm{base}}$.\nOptimization uses Adam with learning rate $10^{-3}$, batch size 32, for 50 epochs with seed 42.\nData augmentation includes additive Gaussian noise on the mean-action vector ($\\sigma \\in [0.02, 0.1]$) and uncertainty features ($\\sigma \\approx 0.006$).\nThe default magnitude bound is $\\varepsilon = 0.2$ for all CRM variants unless stated otherwise.\n\n\\paragraph{Statistical protocol.}\nTable~\\ref{tab:main} reports seed 42 (10 rollouts $\\times$ 10 tasks = 100 episodes per suite).\nFor the primary comparison, we replicate across multiple seeds on LIBERO-Object: obs\\_only ($\\varepsilon{=}0.2$, 6 seeds) achieves mean $17.5 \\pm 2.8$\\%, VLA-only (5 seeds) achieves mean $11.2 \\pm 1.6$\\%, and Argmin (5 seeds) achieves mean $12.4 \\pm 2.9$\\%.\nPooled Fisher's exact test: obs\\_only vs.\\ VLA-only yields $p = 0.0074$ (Cohen's $d = 1.21$).\nAll six obs\\_only seeds exceed the VLA-only mean, confirming reproducible improvement despite per-seed variance.\nMulti-seed VLA-mean evaluation (4 seeds, mean 12.5\\%) confirms that averaging provides no consistent benefit over single-sample execution.\n\n\n\\subsection{Main Results}\n\\label{sec:main_results}\n\nTable~\\ref{tab:main} compares all methods on both benchmarks.\n\n\\begin{table}[t]\n\\centering\n\\caption{Task success rate (\\%\\,$\\uparrow$) on LIBERO-Object and LIBERO-Spatial (10 tasks $\\times$ 10 rollouts each, seed 42). $\\Delta$ denotes improvement over the Argmin selection baseline. All methods use the same frozen SmolVLA checkpoint.}\n\\label{tab:main}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nMethod & Object (\\%) & Spatial (\\%) & $\\Delta$ Object \\\\\n\\midrule\nVLA-only ($K{=}1$)    & 12.0 & 30.0 & $\\phantom{+}0.0$ \\\\\nVLA-mean ($K{=}10$)   & 12.0 & 32.0 & $\\phantom{+}0.0$ \\\\\nArgmin ($K{=}10$)      & 12.0 & 34.0 & --- \\\\\n\\midrule\nscalar ($\\varepsilon{=}0.1$)  & \\phantom{0}9.0 & 32.0 & $-3.0$ \\\\\nperdof ($\\varepsilon{=}0.1$)  & 11.0 & 35.0 & $-1.0$ \\\\\n\\textbf{obs\\_only} ($\\varepsilon{=}0.1$) & \\textbf{19.0} & \\textbf{35.0} & $\\mathbf{+7.0}$ \\\\\n\\midrule\nobs\\_only ($\\varepsilon{=}0.2$) & \\textbf{22.0} & 35.0 & $+10.0$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Object benchmark: correction helps.}\nOn LIBERO-Object, obs\\_only at $\\varepsilon{=}0.1$ achieves 19.0\\% (seed 42), and at $\\varepsilon{=}0.2$ yields 22.0\\%.\nAcross six seeds ($\\varepsilon{=}0.2$), the pipeline achieves mean $17.5 \\pm 2.8$\\% versus VLA-only mean $11.2 \\pm 1.6$\\% ($p = 0.0074$, pooled Fisher's exact test; Cohen's $d = 1.21$).\nThe improvement over Argmin (mean $12.4 \\pm 2.9$\\%) is +5.1\\,pp.\n\nAt seed 42, three baselines (VLA-only, VLA-mean, and Argmin) all achieve 12.0\\%, indicating that neither multi-sample averaging nor $L_2$ argmin selection provides meaningful benefit on this task suite.\nThe VLA-mean result is informative: averaging 10 independent flow-matching samples does not reduce error compared to a single sample ($K{=}1$), confirming that action diversity does not center around the correct action.\nThe obs\\_only CRM breaks through this plateau by predicting corrective residuals conditioned on the observation embedding.\n\n\\paragraph{Pipeline decomposition: selection and correction are synergistic.}\nTo isolate contributions, we evaluate the CRM without multi-sample selection ($K{=}1$): the CRM corrects a single VLA output directly.\nAt $K{=}1$, CRM correction achieves 10.3\\% (3-seed mean), at the VLA-only level (11.2\\%).\nArgmin selection without correction achieves 12.4\\% (5-seed mean), a modest +1.2\\,pp gain.\nNeither component alone meaningfully improves the frozen VLA, yet the full pipeline ($K{=}10$, selection + correction) achieves 17.5\\%, a +6.3\\,pp gain ($p = 0.0074$).\nThis synergy arises because argmin selection filters out the worst samples, providing the CRM with a higher-quality starting point; the CRM then applies corrections that are more reliable on these pre-screened candidates.\nIn terms of contribution decomposition: selection accounts for ${\\sim}$1\\,pp and correction for ${\\sim}$5\\,pp, with correction 4--5$\\times$ more valuable than selection alone.\n\n\\paragraph{Spatial benchmark: correction does not help.}\nOn LIBERO-Spatial, all methods cluster within a 5\\,pp band (30--35\\%).\nThe best CRM variants (obs\\_only, perdof) achieve 35\\%, only 1\\,pp above the Argmin baseline (34\\%).\nThis is a null result that we report prominently.\n\nWe interpret this as follows: spatial perturbations in LIBERO-Spatial involve changes to object layout (e.g., moving target locations), which may require re-planning rather than local action correction.\nThe VLA's observation encoder cannot extract correctable error signals from spatial shifts. The problem is not that actions are inaccurate given the current state, but that the task structure itself has changed.\nResidual correction at the action level is the wrong granularity for this type of generalization.\n\n\\paragraph{Key finding.}\nThe full pipeline significantly improves over VLA-only for object manipulation ($p < 0.01$), where the challenge is fine-grained motor control with novel objects.\nFor spatial reasoning, where the challenge is planning under layout changes, correction at the action level provides no benefit over selection alone.\n\n\n\\subsection{CRM Conditioning Ablation}\n\\label{sec:ablation}\n\nWe focus the conditioning ablation on LIBERO-Object, where meaningful differences emerge (Table~\\ref{tab:main}).\n\n\\paragraph{Ranking.}\nobs\\_only (19.0\\%) $\\gg$ Argmin (12.0\\%) $\\approx$ perdof (11.0\\%) $>$ scalar (9.0\\%).\n\nThis ordering is the central negative result of our ablation: per-DOF conformal features, despite being intuitively richer (40 additional dimensions capturing per-DOF standard deviations, conformal radii, and log-volume terms), \\emph{hurt} rather than help.\nScalar uncertainty conditioning (1 additional dimension) performs even worse, falling 3.0\\,pp below the Argmin baseline that uses no correction at all.\n\nThe scalar $<$ perdof ordering is consistent across seeds (scalar: 9\\%/6\\% for seeds 42/44; perdof: 11\\%/8\\%).\nOne-dimensional scalar uncertainty compresses all six action dimensions into a single number.\nWhen certain dimensions carry high uncertainty but the correction direction is already correct along those axes, the scalar signal cannot distinguish this case from one where correction is needed everywhere.\nThe result is uniform over-correction or under-correction across all dimensions.\nPer-DOF conditioning at least permits dimension-specific judgments, though at $K{=}10$ these judgments remain too noisy to be useful.\nEven 1D scalar uncertainty conditioning is harmful, confirming that conformal scores at $K{=}10$ are unreliable regardless of aggregation dimensionality.\nThe noise originates in the score itself (rank-deficient covariance estimate from 10 samples in 6D), not in how these scores are decomposed across dimensions.\n\n\\paragraph{Why does richer conditioning fail?}\nWe identify three factors:\n\n\\emph{(1) Noisy covariance estimation.}\nWith $K{=}10$ samples in $d{=}6$ dimensions, the dimension-to-sample ratio is $d/K = 0.6$.\nWhile Ledoit--Wolf shrinkage~\\cite{ledoit2004well} stabilizes the covariance estimate for selection (Section~\\ref{sec:selection}), the per-DOF features derived from this estimate (standard deviations, conformal radii) still carry substantial estimation noise.\nFeeding these noisy features as CRM input introduces a distribution shift between training data (where noise patterns are consistent) and closed-loop evaluation (where compounding state-distribution drift produces different noise patterns).\n\n\\emph{(2) Observation features are sufficient.}\nThe frozen VLA observation embedding $\\mathbf{z}_{\\mathrm{obs}} \\in \\mathbb{R}^{960}$ already encodes task-relevant geometric information: object identity, spatial layout, gripper-object relationship, and task progress.\nThis information subsumes what the per-DOF conformal features attempt to capture, namely which action dimensions are uncertain given the current scene.\nThe CRM learns to map directly from scene understanding to corrective residuals, without the intermediate conformal statistics.\n\n\\emph{(3) Per-step MSE $\\neq$ episode success.}\nAll CRM variants achieve low per-step MSE on held-out demonstration data, yet offline prediction accuracy does not predict closed-loop task success.\nIn closed-loop evaluation, small per-step errors compound and the robot visits states far from the demonstration distribution~\\cite{ross2011dagger}.\nThe noisy conformal features amplify this drift: occasional erroneous correction directions, even when small in magnitude, can trigger cascading failures in individual episodes.\n\n\\paragraph{Connection to magnitude sensitivity.}\nThe obs\\_only variant is also more robust across magnitude bounds $\\varepsilon$ than perdof (Section~\\ref{sec:magnitude_results}), providing further evidence that observation-only conditioning yields a more stable correction signal.\n\n\n\\subsection{Conditioning-Magnitude Interaction}\n\\label{sec:magnitude_results}\n\nThe norm bound $\\varepsilon$ controls how far the CRM can deviate from the selected action.\nFigure~\\ref{fig:magnitude} plots success rate against $\\varepsilon$ on LIBERO-Object for both conditioning variants.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\linewidth]{figures/fig2_magnitude.pdf}\n\\caption{Success rate (\\%) vs.\\ magnitude bound $\\varepsilon$ on LIBERO-Object. obs\\_only (blue) remains above the VLA-only baseline (11.2\\%, dashed) across all tested $\\varepsilon$ including uncapped (${\\approx}$1.42). perdof (orange) collapses progressively, reaching 0\\% at the uncapped setting (3 seeds). Error bars: $\\pm$1 std; hollow markers: $n < 3$.}\n\\label{fig:magnitude}\n\\end{figure}\n\n\\paragraph{obs\\_only is robust across all magnitudes.}\nThe obs\\_only variant maintains 13.5--17.5\\% across $\\varepsilon \\in [0.03, \\text{uncapped}]$, peaking at 17.5\\% ($\\varepsilon{=}0.2$, 6 seeds) and remaining above VLA-only (11.2\\%) at every tested bound, including uncapped (14.3\\%, 3 seeds).\nThe practitioner need not carefully tune $\\varepsilon$: any value in $[0.05, 0.3]$ yields comparable performance.\n\n\\paragraph{perdof collapses progressively.}\nThe perdof variant starts at 14.0\\% ($\\varepsilon{=}0.03$, $n{=}1$), drops to 11.0\\% at $\\varepsilon{=}0.1$ (6 seeds), and collapses to 0\\% at the uncapped setting (3 seeds, all zero).\nThis progressive degradation traces to rank-deficient covariance estimation: with $K{=}10$ samples in $d{=}6$ dimensions ($d/K = 0.6$), per-DOF features carry substantial estimation noise.\nAt tight $\\varepsilon$, clipping masks the noisy correction directions; as the bound loosens, erroneous corrections compound across the trajectory.\n\n\\paragraph{Scalar conditioning is worse than no conditioning.}\nThe scalar variant achieves 8.3\\% (3 seeds at $\\varepsilon{=}0.2$), below VLA-only (11.2\\%).\nThis confirms that conformal statistics at $K{=}10$ are unreliable regardless of aggregation dimensionality: the noise originates in the score itself (rank-deficient covariance), not in how the scores are decomposed.\n\n\\paragraph{Practical recommendation.}\nWe use $\\varepsilon{=}0.2$ as the primary setting.\nWithin $[0.05, 0.3]$, obs\\_only never degrades below the VLA-only baseline across all tested seeds.\n\n\n\\subsection{Inference-Time Scaling with $K$}\n\\label{sec:k_scaling}\n\nFigure~\\ref{fig:kvalue} plots task success rate against the number of VLA samples $K$.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\linewidth]{figures/fig3_kvalue.pdf}\n\\caption{Success rate (\\%) vs.\\ number of VLA samples $K$ on LIBERO-Object (obs\\_only, $\\varepsilon{=}0.2$). Reference lines: VLA-only (11.2\\%, 5 seeds) and Argmin-only (12.4\\%, 5 seeds). Error bars: $\\pm$1 std where available; hollow marker for $K{=}5$ ($n{=}1$).}\n\\label{fig:kvalue}\n\\end{figure}\n\nPerformance increases monotonically with $K$: $K{=}1$ (10.3\\%, 3 seeds) $\\to$ $K{=}5$ (14.0\\%, 1 seed) $\\to$ $K{=}10$ (17.5\\%, 6 seeds).\nAt $K{=}1$, CRM correction alone performs at the VLA-only level (11.2\\%), confirming that the correction module requires multi-sample selection to be effective.\nThe monotonic trend parallels inference-time compute scaling in LLMs~\\cite{snell2024scaling}, where repeated sampling with selection (best-of-$N$) improves output quality.\nIn our setting, more samples yield a better argmin starting point, which in turn enables more effective correction.\n\nThe $K{=}5$ data point is preliminary ($n{=}1$), but it falls on the monotonic trend, suggesting that even moderate sample budgets can capture partial gains.\nThe compute cost scales linearly: $K{=}10$ requires 10 forward passes through the frozen VLA plus ${\\sim}$3\\,ms for CRM inference, a ${\\sim}$10$\\times$ increase in VLA compute.\n\n\n\\subsection{Applicability Boundary: Stochastic VLA Diversity}\n\\label{sec:applicability}\n\nThe multi-sample pipeline requires stochastic action diversity across samples. We test this prerequisite by comparing SmolVLA (flow-matching, 450M) with OpenVLA~\\cite{kim2024openvla} (autoregressive tokenization, 7B).\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\linewidth]{figures/fig4_diversity.pdf}\n\\caption{Per-DOF action variance (log scale) across $K{=}10$ samples for SmolVLA (flow-matching) and OpenVLA (tokenized). OpenVLA produces 8/10 identical samples at temperature $T{=}0.5$, with per-DOF variance below $10^{-30}$ for most dimensions.}\n\\label{fig:diversity}\n\\end{figure}\n\nFigure~\\ref{fig:diversity} shows the contrast: SmolVLA produces meaningfully diverse samples across all action dimensions, while OpenVLA at temperature $T{=}0.5$ generates 8 out of 10 identical action sequences, with per-DOF variance below $10^{-30}$ for most dimensions.\nThis near-determinism arises from autoregressive token selection: the argmax decoding at each token position collapses the distribution to a single mode, and moderate temperature fails to overcome the peaked distribution.\n\nThis result establishes an applicability boundary: multi-sample inference-time correction is specific to stochastic generative VLAs (flow-matching, diffusion). Tokenized VLAs lack the action diversity that selection and correction rely on.\nThe boundary is architectural, not a limitation of our method: any inference-time approach that draws multiple action candidates requires the base policy to produce diverse samples.\n\n\n\\subsection{Per-Task Analysis}\n\\label{sec:per_task}\n\nTable~\\ref{tab:pertask} reports per-task success rates on LIBERO-Object (seed 42) for the VLA-only baseline, Argmin selection, and obs\\_only at two magnitude bounds.\n\n\\begin{table}[t]\n\\centering\n\\caption{Per-task success rate (\\%) on LIBERO-Object (seed 42, 10 rollouts per task). Tasks ordered by obs\\_only $\\varepsilon{=}0.2$ improvement over VLA-only.}\n\\label{tab:pertask}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nTask & VLA-only & Argmin & obs\\_only 0.1 & obs\\_only 0.2 \\\\\n\\midrule\nchocolate\\_pudding & 20 & 30 & 50 & 60 \\\\\nketchup            &  0 &  0 & 10 & 20 \\\\\nbbq\\_sauce         & 20 & 30 & 40 & 40 \\\\\nsalad\\_dressing    & 20 & 10 & 20 & 30 \\\\\nbutter             &  0 & 10 & 10 & 10 \\\\\nmilk               & 10 & 10 & 20 & 20 \\\\\norange\\_juice      & 30 & 30 & 30 & 30 \\\\\ntomato\\_sauce      & 10 &  0 &  0 & 10 \\\\\nalphabet\\_soup     &  0 &  0 &  0 &  0 \\\\\ncream\\_cheese      & 10 &  0 & 10 &  0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Improvement concentrates on medium-difficulty tasks.}\nThe +10\\,pp aggregate gain of obs\\_only ($\\varepsilon{=}0.2$) over VLA-only is not uniformly distributed across tasks.\nThe largest improvements appear on tasks where the frozen VLA partially succeeds but makes correctable errors: chocolate\\_pudding (+40\\,pp, from 20\\% to 60\\%), bbq\\_sauce and ketchup (+20\\,pp each), and salad\\_dressing (+10\\,pp).\nThese four tasks account for 9 of the 10 additional successes.\nConversely, four tasks (alphabet\\_soup, cream\\_cheese, tomato\\_sauce, butter) remain at 0--10\\% across all methods, including obs\\_only.\nFor these tasks, the base policy fails so completely that local action-level correction cannot recover a viable trajectory.\n\n\\paragraph{Implications for the correction mechanism.}\nCorrection benefits tasks where the frozen VLA partially succeeds but makes correctable errors, rather than tasks where the base policy fails catastrophically or already succeeds reliably.\nThis pattern is expected for a residual correction approach bounded by $\\varepsilon$: the CRM can fix small deviations in grasp pose or approach angle, but cannot recover from fundamental planning failures (e.g., reaching toward the wrong object entirely).\nThe concentrated improvement profile also addresses the question of effect size: the aggregate +10\\,pp is not a uniform +1\\,pp across 10 tasks, but a substantial +20--40\\,pp on specific tasks diluted by tasks outside the correctable regime.\n",
      "numLines": 264,
      "startLine": 1,
      "totalLines": 264
    }
  }
}
```

</details>

---

### Assistant

_source line 15_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the context I need. Let me carefully craft the Introduction following the exact specifications in the task, using the D058 corrections and hard data provided. Let me also check for any `\cite` keys used in the existing method and experiments sections to ensure consistency.

Key things to note:
1. Selection is "argmin L2 distance to sample mean" — NOT "Mahalanobis" or "conformal selection"
2. CRM is a CORRECTION module — does NOT rank candidates
3. obs_only variant does NOT use conformal statistics
4. Primary ε = 0.2 (not 0.1)


5. CRM has roughly 327K parameters
6. I should dial back the language around "conformal" since the core method doesn't actually rely on conformal features
7. Keep the ACR-VLA name but shift focus away from the conformal aspect

The main result shows obs_only with K=10 and ε=0.2 achieves 17.5% across 6 seeds versus VLA-only at 11.2% across 5 seeds—that's a 6.3 percentage point improvement with strong statistical significance (Fisher p=0.0074, Cohen's d=1.21). The component breakdown reveals that CRM correction alone at K=1 gets us to 10.3%, essentially matching VLA-only performance, which confirms the argmin selection mechanism is doing the heavy lifting.

Breaking down the gains further, selection contributes roughly 1 percentage point while correction adds about 5 percentage points. The conditioning results are striking—obs_only reaches 19% on seed 42 while per-DOF drops to 11% and argmin sits at 12%, showing that conformal features actually degrade performance. Across different epsilon values, obs_only stays robust between 13.5-17.5%, but per-DOF collapses dramatically from 14% down to near zero. K-value scaling is monotonic: K=1 gives 10.3%, K=5 reaches 14%, and K=10 hits 17.5%. OpenVLA shows minimal diversity with 8 out of 10 identical samples and per-DOF variance below 1e-30, which makes sense for tokenized VLAs. The spatial task yields null results across all methods clustering around 30-35%, suggesting correction doesn't help there. The CRM architecture uses an MLP with 990D input feeding through 256 hidden units twice before outputting 30 dimensions.

The selection mechanism relies on L2 distance to the sample mean rather than Mahalanobis distance or conformal scoring, and the input combines 960D observation features with 30D base actions.

I'm checking the citation keys from the existing paper to keep things consistent, then structuring the introduction around five key paragraphs: first establishing how flow-matching VLAs fail under distribution shift using LIBERO+ benchmarks, then covering existing robustness approaches, followed by the core contribution, experimental validation, and broader implications. the gap**
- Training-time: SRPO, RobustVLA, DiG-Flow (require retraining)
- Inference-time: ReconVLA (UQ, no correction), A2C2 (temporal correction, complementary), VLA-Pilot (2.41s latency)
- Gap: No systematic study of what drives effective inference-time correction

**Para 3: Our approach — sample-then-correct**
- ACR-VLA: K=10 samples → argmin L2 selection → CRM learned residual → bounded output
- CRM: ~327K param MLP conditioned on obs embedding + selected action
- Key insight: correction on high-quality starting point + magnitude bounding prevents compounding

**Para 4: Three key findings (with correct numbers)**
- (C1) Full pipeline: 17.5% vs 11.2% (+6.3pp, p=0.0074, 6 seeds). Component decomposition shows where gains come from.
- (C2) Conditioning-magnitude interaction: observation-only setup stays robust while per-DOF collapses, and conformal features degrade performance.
- (C3) Applicability boundary: the method needs a stochastic VLA, but OpenVLA's tokenized outputs produce 8 out of 10 identical samples.

**Para 5: Contributions list (3 items)**

Now I'm drafting the full introduction section. I need to be precise about terminology—the CRM is a correction module, not a ranking system, and the observation-only baseline doesn't use conformal statistics. I'm setting the primary error threshold at 0.2, noting the CRM has roughly 327K parameters, and keeping the focus on the correction mechanism rather than conformal methods. Let me start with how VLAs struggle under distribution shift and build toward the motivation for our approach.

I'm establishing the severity of the problem: models like π₀ and UniVLA see dramatic performance drops—from 94% to 7% and 95% to 4%—when facing initial-state perturbations or viewpoint changes on LIBERO+. This fragility under real-world conditions is the core issue we're addressing. Then I'm transitioning to existing solutions and where they fall short, setting up why a test-time correction approach is necessary. -time reinforcement learning, but they require retraining or per-task RL and stay constrained by their training distribution. Inference-time methods keep the policy fixed: ReconVLA uses conformal quantile regression for uncertainty and out-of-distribution detection without learning corrective residuals; A2C2 trains a per-step correction head on frozen VLA action chunks but applies it unconditionally without multi-sample selection or magnitude control; VLA-Pilot uses evolutionary optimization over action samples but takes 2.41 seconds per control step. While inference-time action refinement is gaining attention, key questions remain unaddressed: how much does selecting among candidates matter compared to learned correction, what observation features should guide the correction, and how does closed-loop performance vary with correction magnitude—no prior work systematically breaks down these factors.

I'm introducing ACR-VLA, an inference-time action refinement module for frozen flow-matching VLAs that samples multiple action candidates, selects the one closest to the mean, and applies a learned residual correction through a lightweight correction module that takes the VLA's observation embedding and selected action as input to predict a bounded residual adjustment.

The key insight is that correcting from a pre-screened starting point is more stable than correcting arbitrary samples, and clipping the correction magnitude prevents errors from cascading through the trajectory while keeping the base VLA unchanged.

I'm evaluating this on LIBERO-Object and LIBERO-Spatial tasks with SmolVLA as the backbone, and three main findings are emerging.

First, the full pipeline substantially outperforms the frozen VLA—achieving 17.5% success versus 11.2% baseline—with correction driving most of the gain (about 5 percentage points) while selection contributes roughly 1 percentage point. Correction alone at K=1 reaches only 10.3%, and selection alone gets 12.4%, so both components are necessary.

Second, observation features alone are sufficient for correction, and conformal uncertainty features...

Actually, let me continue with the next thinking: observation-only conditioning achieves 19% success and remains robust across different magnitude bounds (13.5–17.5%), whereas per-DOF conformal conditioning collapses as the bounds increase due to rank-deficient covariance estimation with limited samples. Third, multi-sample correction requires the model to produce diverse action samples—SmolVLA's flow-matching approach generates the variety needed for effective selection and correction, but OpenVLA's autoregressive tokenization produces nearly identical samples with negligible variance, which breaks the approach.

Now I'm outlining the main contributions: a multi-sample inference-time correction pipeline that combines argmin selection with bounded residual correction for frozen flow-matching VLAs, decomposing the improvements into selection and correction components, achieving a statistically significant +6.3 percentage point gain over the baseline on LIBERO-Object.

I'm also detailing a systematic study comparing three conditioning variants across different magnitude bounds, finding that observation-only conditioning remains robust while conformal features and scalar uncertainty actually hurt performance, which contradicts the assumption that richer uncertainty representations help.

Finally, I'm establishing an architectural boundary showing that tokenized VLAs lack the sample diversity needed for multi-sample correction, meaning inference-time action refinement methods have fundamental applicability limits based on the underlying model's stochasticity. I'm verifying the table references map correctly to their sections, and the word count looks on target. Actually, I need to reconsider the module naming—the method section uses "Conformal Residual Module" consistently, even though the corrections suggest de-emphasizing the conformal aspect, so I should keep that terminology for consistency with what's already established in the paper. I need to align the naming across sections—the method defines it as "Conformal Residual Module (CRM)" so I should use that consistently in paragraph 3 instead of "Correction Residual Module." Even though the conformal aspect isn't emphasized, keeping the established name maintains coherence throughout the paper. I'm checking the word count across the five paragraphs—roughly 90, 140, 120, 250, and 200 words respectively—which lands me right around 800 words total. For the introduction, I'll expand the ACR-VLA acronym once but avoid bolding the "Conformal" part to keep it de-emphasized, staying consistent with how the method section handles it.

Actually, the cleaner approach is to just introduce it as "ACR-VLA, an inference-time action refinement module for frozen flow-matching VLAs" without spelling out the full acronym—that naturally downplays the conformal aspect. Now let me verify the key numbers one more time: the 17.5% versus 11.2% improvement is a 6.3 percentage point gain with p=0.0074 and Cohen's d=1.21, the K=1 baseline sits at 10.3%, argmin reaches 12.4%, and the observation-only seed 42 shows 19% at ε=0.1.

Looking at the experimental table more carefully, I see the conditioning comparison at ε=0.1 shows observation-only at 19%, perdof at 11%, scalar at 9%, and argmin at 12%, while the primary result uses ε=0.2 data across multiple seeds where observation-only reaches 22%. I need to be clear about which epsilon value I'm citing when I reference the seed 42 conditioning comparison versus the main multi-seed result.

For the spatial null result, I should check whether it fits into the three key findings or if it belongs elsewhere in the contribution structure—it seems to be mentioned as part of the applicability boundary rather than a standalone finding. I'm settling on a few key refinements: standardizing the terminology to "Conformal Residual Module" for consistency with the method section, keeping the VLA acronym unexpanded to avoid overemphasizing the conformal aspect, weaving in the spatial null result finding, and doing a final pass for clarity before finalizing the text.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8146b578-f41a-49c2-b99a-be63bde75274",
  "uuid": "3aeeff33-501f-4c66-ba57-296c0b62967b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JnZF74AFuUCqm71AqTCA1P",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 23159,
      "cache_read_input_tokens": 25895,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 23159
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Assistant

_source line 16_

Now I have all the context. Let me also check what cite keys are used across the paper for consistency.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8146b578-f41a-49c2-b99a-be63bde75274",
  "uuid": "47184436-2f12-4d32-a3e0-3ed61b263f10",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JnZF74AFuUCqm71AqTCA1P",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 23159,
      "cache_read_input_tokens": 25895,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 23159
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 17_

<details open><summary>🔧 Tool call — Grep · `toolu_01UpmxYwdsuhVnd7YfjkjV4x`</summary>

```json
{
  "pattern": "\\\\cite\\{",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper",
  "output_mode": "content",
  "-n": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8146b578-f41a-49c2-b99a-be63bde75274",
  "uuid": "271d2a20-c4c8-4077-a651-931d53398177",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JnZF74AFuUCqm71AqTCA1P",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 23159,
      "cache_read_input_tokens": 25895,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 23159
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-18T10:17:58.260Z_

<details><summary>↩ Tool result · `toolu_01UpmxYwdsuhVnd7YfjkjV4x`</summary>

```text
docs/paper/related_work.tex:8:RobustVLA~\cite{robustvla2025} combines RL post-training with Jacobian regularization and smoothness regularization to stabilize action predictions under observation noise and action perturbations.
docs/paper/related_work.tex:9:SRPO~\cite{srpo2025} applies self-referential RL fine-tuning, using the policy's own successful rollouts as references to shape rewards for failed trajectories via latent world model representations.
docs/paper/related_work.tex:10:DiG-Flow~\cite{digflow2025} uses distributional discrepancy between observation and action embeddings as a gating signal to rebalance representation-level control, without modifying the flow-matching trajectory.
docs/paper/related_work.tex:11:TT-VLA~\cite{liu2026ttvla} blurs the training/inference boundary by adapting VLA parameters at test time through RL with progress rewards, but still requires per-task reward design and gradient updates during deployment.
docs/paper/related_work.tex:15:ReconVLA~\cite{chen2026reconvla} applies conformal quantile regression to calibrate per-action uncertainty bounds and uses squared Mahalanobis distance for out-of-distribution detection, enabling uncertainty-guided action selection and proactive failure detection without retraining.
docs/paper/related_work.tex:16:SC-VLA~\cite{liu2026scvla} performs online action refinement through sparse world imagination combined with residual RL, but requires task-level RL training for the correction policy.
docs/paper/related_work.tex:17:VLA-Pilot~\cite{li2025vlapilot} applies evolutionary diffusion optimization guided by an MLLM verifier, achieving plug-and-play correction at the cost of 2.41\,s per control step---prohibitive for real-time manipulation.
docs/paper/related_work.tex:18:A2C2~\cite{a2c2_2025} learns a lightweight correction head that runs at every control step to correct each action within a pre-generated chunk, restoring closed-loop responsiveness; however, it applies correction unconditionally without first selecting a high-quality starting action or modulating correction magnitude based on uncertainty.
docs/paper/related_work.tex:29:Conformal prediction (CP) provides distribution-free coverage guarantees under exchangeability~\cite{angelopoulos2023gentle}.
docs/paper/related_work.tex:30:For multivariate outputs, Braun et al.~\cite{braun2025cgs} develop Conformalized Gaussian Scoring (CGS), which uses Mahalanobis-based nonconformity scores to construct prediction regions that respect cross-dimensional covariance---the scoring method ACR-VLA builds upon for its selection stage.
docs/paper/related_work.tex:33:Conformalized Teleoperation~\cite{zhao2024conformalized} uses CP to quantify uncertainty in high-DOF action mappings during shared autonomy, flagging unreliable predictions for human review.
docs/paper/related_work.tex:34:CP-in-the-Loop~\cite{wang2025cploop} integrates conformal prediction regions as feedback constraints in trajectory optimization, tightening or relaxing plans based on calibrated uncertainty.
docs/paper/related_work.tex:35:ACP+CBF~\cite{zhou2025acp_cbf} combines adaptive conformal prediction with control barrier functions to maintain safety constraints under distribution shift in RL policies.
docs/paper/related_work.tex:45:Silver et al.~\cite{silver2018residual} introduced the framework for classical controllers, using zero-initialization to ensure the learned residual starts from the base policy's behavior and gradually improves upon it.
docs/paper/related_work.tex:47:TRANSIC~\cite{jiang2024transic} uses a learned binary gate conditioned on the current state to decide whether to apply a sim-to-real residual, demonstrating that ungated correction causes model collapse.
docs/paper/related_work.tex:48:PLD~\cite{xiao2026pld} freezes the VLA backbone and trains lightweight residual actors with bounded corrections ($[-\xi, \xi]$) via off-policy RL, then distills improved trajectories back into the base model.
docs/paper/related_work.tex:49:DRC~\cite{pan2025drc} applies exponential decay to each expert correction event, allowing corrective signals to persist and fade after application.
docs/paper/related_work.tex:59:DiU~\cite{xing2026diu} derives a closed-form posterior covariance for flow-matching models by computing the divergence of the velocity field, enabling single-pass per-DOF uncertainty estimation without additional sampling.
docs/paper/related_work.tex:60:SAFE~\cite{gu2025safe} trains a multitask failure detector on VLA internal features and uses conformal prediction to calibrate detection timing, triggering intervention when anomalous states are detected.
docs/paper/related_work.tex:61:Zollo and Zemel~\cite{zollo2025vla_calibration} provide the first systematic study of confidence calibration in VLAs, finding that prompt ensembles combined with Platt scaling improve calibration across manipulation tasks.
docs/paper/related_work.tex:65:Functionally, ACR-VLA uses uncertainty for action selection (identifying the lowest-nonconformity sample), whereas DiU targets efficient uncertainty visualization, SAFE targets failure detection, and VLA calibration~\cite{zollo2025vla_calibration} targets confidence reliability.
docs/paper/experiments.tex:15:We use two suites from the LIBERO benchmark~\cite{liu2023libero}:
docs/paper/experiments.tex:20:We build on SmolVLA~\cite{shukor2025smolvla}, a 450M-parameter flow-matching VLA.
docs/paper/experiments.tex:137:While Ledoit--Wolf shrinkage~\cite{ledoit2004well} stabilizes the covariance estimate for selection (Section~\ref{sec:selection}), the per-DOF features derived from this estimate (standard deviations, conformal radii) still carry substantial estimation noise.
docs/paper/experiments.tex:147:In closed-loop evaluation, small per-step errors compound and the robot visits states far from the demonstration distribution~\cite{ross2011dagger}.
docs/paper/experiments.tex:199:The monotonic trend parallels inference-time compute scaling in LLMs~\cite{snell2024scaling}, where repeated sampling with selection (best-of-$N$) improves output quality.
docs/paper/experiments.tex:209:The multi-sample pipeline requires stochastic action diversity across samples. We test this prerequisite by comparing SmolVLA (flow-matching, 450M) with OpenVLA~\cite{kim2024openvla} (autoregressive tokenization, 7B).
docs/paper/discussion.tex:8:At $K{=}10$ samples in $d{=}6$ dimensions, the dimension-to-sample ratio $d/K = 0.6$ means that even with Ledoit--Wolf shrinkage~\cite{ledoit2004well}, per-DOF statistics (standard deviations, conformal radii) carry substantial estimation noise.
docs/paper/discussion.tex:14:In closed-loop execution, compounding error~\cite{ross2011dagger} shifts the state distribution away from training data, and the noisy conformal features amplify this drift: occasional erroneous correction directions, even when small in magnitude, can trigger cascading failures in individual episodes.
docs/paper/discussion.tex:30:  \item \emph{Simulation only.} All experiments use LIBERO~\cite{liu2023libero}; real-robot transfer is untested.
docs/paper/discussion.tex:31:  \item \emph{Single VLA backbone.} We evaluate only SmolVLA~\cite{shukor2025smolvla} (450M parameters). Whether ACR-VLA transfers to larger VLAs (e.g., $\pi_0$, OpenVLA) is unknown.
docs/paper/method.tex:12:We instantiate ACR-VLA on SmolVLA~\cite{shukor2025smolvla}, a 450M-parameter flow-matching VLA that generates actions via learned flow matching~\cite{lipman2023flow}. Each forward pass produces a stochastic action sample, so querying $\pi_\theta$ independently $K$ times yields $K$ candidate action chunks. Our goal is to produce a single action more accurate than any individual sample, with no changes to~$\pi_\theta$. The method applies to any flow-matching VLA that supports repeated sampling.
docs/paper/method.tex:41:  \item \textbf{perdof}: $[\mathbf{z}_{\mathrm{obs}};\, a_{\mathrm{base}};\, \mathbf{u}_{\mathrm{dof}}] \in \mathbb{R}^{1030}$, 337K parameters. The 40-dimensional vector $\mathbf{u}_{\mathrm{dof}}$ consists of 30 per-DOF standard deviations ($H{\times}d$), 5 conformal prediction radii~\cite{angelopoulos2023gentle} (one per horizon step), and 5 log-volume terms derived from the Ledoit--Wolf shrinkage covariance~\cite{ledoit2004well} of the $K$ samples.
docs/paper/method.tex:44:The obs\_only variant is our primary method. Despite the name ``Conformal Residual Module,'' the primary variant does not condition on conformal statistics. The perdof variant conditions on conformal-calibrated uncertainty features~\cite{braun2025cgs}, but Section~\ref{sec:ablation} shows that these features fail to improve closed-loop performance at the $K{=}10$ sample budget.
docs/paper/method.tex:47:The CRM is trained offline on demonstration trajectories from LIBERO~\cite{liu2023libero} with $L_2$ loss:
docs/paper/method.tex:52:[Omitted long matching line]
docs/paper/method.tex:59:[Omitted long matching line]
docs/paper/method.tex:65:[Omitted long matching line]
docs/paper/introduction.tex:5:Vision-language-action models (VLAs) that generate actions via flow matching~\cite{black2024pi0,shukor2025smolvla,lipman2023flow} have reached high success rates on in-distribution benchmarks such as LIBERO~\cite{liu2023libero}.
docs/paper/introduction.tex:6:Yet this near-saturation masks a fragile reality: visual and physical perturbations routinely encountered in deployment (camera viewpoint shifts, object layout changes, robot initial state variation) can degrade success rates by over 65 percentage points. For example, $\pi_0$ drops from 94.2\% to 6.6\% under robot initial-state perturbation, and UniVLA from 95.2\% to 4.3\% under camera viewpoint changes~\cite{fei2025liberoplus}.
docs/paper/introduction.tex:11:\emph{Training-time methods} improve the base policy itself through robustness-aware objectives~\cite{srpo2025,robustvla2025,digflow2025} or test-time reinforcement learning~\cite{liu2026ttvla}.
docs/paper/introduction.tex:14:ReconVLA~\cite{chen2026reconvla} applies conformal quantile regression to calibrate action-level uncertainty and uses these estimates for uncertainty-guided action selection and out-of-distribution detection, taking a complementary UQ-driven approach rather than learning explicit corrective residuals.
docs/paper/introduction.tex:15:VLA-Pilot~\cite{li2025vlapilot} applies evolutionary optimization over action samples, but incurs 2.41\,s per control step, too slow for real-time manipulation.
docs/paper/introduction.tex:16:A2C2~\cite{a2c2_2025} learns a per-step correction head for pre-generated action chunks on a frozen VLA, but applies correction unconditionally without multi-sample selection or explicit magnitude control.
docs/paper/introduction.tex:21:At each control step, ACR-VLA draws $K{=}10$ action samples from the frozen VLA, selects the most conforming candidate via Mahalanobis-based nonconformity scoring with shrinkage covariance estimation~\cite{ledoit2004well,braun2025cgs}, and then applies a learned residual correction via a lightweight \emph{Conformal Residual Module} (CRM).
docs/paper/introduction.tex:28:We evaluate ACR-VLA on LIBERO-Object (10 tasks, 100 trials per method) and LIBERO-Spatial (10 tasks, 100 trials) using SmolVLA~\cite{shukor2025smolvla} as the frozen backbone. Three findings emerge:
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8146b578-f41a-49c2-b99a-be63bde75274",
  "uuid": "a781225d-6359-48ae-bec6-f684c1f14e86",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/related_work.tex:8:RobustVLA~\\cite{robustvla2025} combines RL post-training with Jacobian regularization and smoothness regularization to stabilize action predictions under observation noise and action perturbations.\ndocs/paper/related_work.tex:9:SRPO~\\cite{srpo2025} applies self-referential RL fine-tuning, using the policy's own successful rollouts as references to shape rewards for failed trajectories via latent world model representations.\ndocs/paper/related_work.tex:10:DiG-Flow~\\cite{digflow2025} uses distributional discrepancy between observation and action embeddings as a gating signal to rebalance representation-level control, without modifying the flow-matching trajectory.\ndocs/paper/related_work.tex:11:TT-VLA~\\cite{liu2026ttvla} blurs the training/inference boundary by adapting VLA parameters at test time through RL with progress rewards, but still requires per-task reward design and gradient updates during deployment.\ndocs/paper/related_work.tex:15:ReconVLA~\\cite{chen2026reconvla} applies conformal quantile regression to calibrate per-action uncertainty bounds and uses squared Mahalanobis distance for out-of-distribution detection, enabling uncertainty-guided action selection and proactive failure detection without retraining.\ndocs/paper/related_work.tex:16:SC-VLA~\\cite{liu2026scvla} performs online action refinement through sparse world imagination combined with residual RL, but requires task-level RL training for the correction policy.\ndocs/paper/related_work.tex:17:VLA-Pilot~\\cite{li2025vlapilot} applies evolutionary diffusion optimization guided by an MLLM verifier, achieving plug-and-play correction at the cost of 2.41\\,s per control step---prohibitive for real-time manipulation.\ndocs/paper/related_work.tex:18:A2C2~\\cite{a2c2_2025} learns a lightweight correction head that runs at every control step to correct each action within a pre-generated chunk, restoring closed-loop responsiveness; however, it applies correction unconditionally without first selecting a high-quality starting action or modulating correction magnitude based on uncertainty.\ndocs/paper/related_work.tex:29:Conformal prediction (CP) provides distribution-free coverage guarantees under exchangeability~\\cite{angelopoulos2023gentle}.\ndocs/paper/related_work.tex:30:For multivariate outputs, Braun et al.~\\cite{braun2025cgs} develop Conformalized Gaussian Scoring (CGS), which uses Mahalanobis-based nonconformity scores to construct prediction regions that respect cross-dimensional covariance---the scoring method ACR-VLA builds upon for its selection stage.\ndocs/paper/related_work.tex:33:Conformalized Teleoperation~\\cite{zhao2024conformalized} uses CP to quantify uncertainty in high-DOF action mappings during shared autonomy, flagging unreliable predictions for human review.\ndocs/paper/related_work.tex:34:CP-in-the-Loop~\\cite{wang2025cploop} integrates conformal prediction regions as feedback constraints in trajectory optimization, tightening or relaxing plans based on calibrated uncertainty.\ndocs/paper/related_work.tex:35:ACP+CBF~\\cite{zhou2025acp_cbf} combines adaptive conformal prediction with control barrier functions to maintain safety constraints under distribution shift in RL policies.\ndocs/paper/related_work.tex:45:Silver et al.~\\cite{silver2018residual} introduced the framework for classical controllers, using zero-initialization to ensure the learned residual starts from the base policy's behavior and gradually improves upon it.\ndocs/paper/related_work.tex:47:TRANSIC~\\cite{jiang2024transic} uses a learned binary gate conditioned on the current state to decide whether to apply a sim-to-real residual, demonstrating that ungated correction causes model collapse.\ndocs/paper/related_work.tex:48:PLD~\\cite{xiao2026pld} freezes the VLA backbone and trains lightweight residual actors with bounded corrections ($[-\\xi, \\xi]$) via off-policy RL, then distills improved trajectories back into the base model.\ndocs/paper/related_work.tex:49:DRC~\\cite{pan2025drc} applies exponential decay to each expert correction event, allowing corrective signals to persist and fade after application.\ndocs/paper/related_work.tex:59:DiU~\\cite{xing2026diu} derives a closed-form posterior covariance for flow-matching models by computing the divergence of the velocity field, enabling single-pass per-DOF uncertainty estimation without additional sampling.\ndocs/paper/related_work.tex:60:SAFE~\\cite{gu2025safe} trains a multitask failure detector on VLA internal features and uses conformal prediction to calibrate detection timing, triggering intervention when anomalous states are detected.\ndocs/paper/related_work.tex:61:Zollo and Zemel~\\cite{zollo2025vla_calibration} provide the first systematic study of confidence calibration in VLAs, finding that prompt ensembles combined with Platt scaling improve calibration across manipulation tasks.\ndocs/paper/related_work.tex:65:Functionally, ACR-VLA uses uncertainty for action selection (identifying the lowest-nonconformity sample), whereas DiU targets efficient uncertainty visualization, SAFE targets failure detection, and VLA calibration~\\cite{zollo2025vla_calibration} targets confidence reliability.\ndocs/paper/experiments.tex:15:We use two suites from the LIBERO benchmark~\\cite{liu2023libero}:\ndocs/paper/experiments.tex:20:We build on SmolVLA~\\cite{shukor2025smolvla}, a 450M-parameter flow-matching VLA.\ndocs/paper/experiments.tex:137:While Ledoit--Wolf shrinkage~\\cite{ledoit2004well} stabilizes the covariance estimate for selection (Section~\\ref{sec:selection}), the per-DOF features derived from this estimate (standard deviations, conformal radii) still carry substantial estimation noise.\ndocs/paper/experiments.tex:147:In closed-loop evaluation, small per-step errors compound and the robot visits states far from the demonstration distribution~\\cite{ross2011dagger}.\ndocs/paper/experiments.tex:199:The monotonic trend parallels inference-time compute scaling in LLMs~\\cite{snell2024scaling}, where repeated sampling with selection (best-of-$N$) improves output quality.\ndocs/paper/experiments.tex:209:The multi-sample pipeline requires stochastic action diversity across samples. We test this prerequisite by comparing SmolVLA (flow-matching, 450M) with OpenVLA~\\cite{kim2024openvla} (autoregressive tokenization, 7B).\ndocs/paper/discussion.tex:8:At $K{=}10$ samples in $d{=}6$ dimensions, the dimension-to-sample ratio $d/K = 0.6$ means that even with Ledoit--Wolf shrinkage~\\cite{ledoit2004well}, per-DOF statistics (standard deviations, conformal radii) carry substantial estimation noise.\ndocs/paper/discussion.tex:14:In closed-loop execution, compounding error~\\cite{ross2011dagger} shifts the state distribution away from training data, and the noisy conformal features amplify this drift: occasional erroneous correction directions, even when small in magnitude, can trigger cascading failures in individual episodes.\ndocs/paper/discussion.tex:30:  \\item \\emph{Simulation only.} All experiments use LIBERO~\\cite{liu2023libero}; real-robot transfer is untested.\ndocs/paper/discussion.tex:31:  \\item \\emph{Single VLA backbone.} We evaluate only SmolVLA~\\cite{shukor2025smolvla} (450M parameters). Whether ACR-VLA transfers to larger VLAs (e.g., $\\pi_0$, OpenVLA) is unknown.\ndocs/paper/method.tex:12:We instantiate ACR-VLA on SmolVLA~\\cite{shukor2025smolvla}, a 450M-parameter flow-matching VLA that generates actions via learned flow matching~\\cite{lipman2023flow}. Each forward pass produces a stochastic action sample, so querying $\\pi_\\theta$ independently $K$ times yields $K$ candidate action chunks. Our goal is to produce a single action more accurate than any individual sample, with no changes to~$\\pi_\\theta$. The method applies to any flow-matching VLA that supports repeated sampling.\ndocs/paper/method.tex:41:  \\item \\textbf{perdof}: $[\\mathbf{z}_{\\mathrm{obs}};\\, a_{\\mathrm{base}};\\, \\mathbf{u}_{\\mathrm{dof}}] \\in \\mathbb{R}^{1030}$, 337K parameters. The 40-dimensional vector $\\mathbf{u}_{\\mathrm{dof}}$ consists of 30 per-DOF standard deviations ($H{\\times}d$), 5 conformal prediction radii~\\cite{angelopoulos2023gentle} (one per horizon step), and 5 log-volume terms derived from the Ledoit--Wolf shrinkage covariance~\\cite{ledoit2004well} of the $K$ samples.\ndocs/paper/method.tex:44:The obs\\_only variant is our primary method. Despite the name ``Conformal Residual Module,'' the primary variant does not condition on conformal statistics. The perdof variant conditions on conformal-calibrated uncertainty features~\\cite{braun2025cgs}, but Section~\\ref{sec:ablation} shows that these features fail to improve closed-loop performance at the $K{=}10$ sample budget.\ndocs/paper/method.tex:47:The CRM is trained offline on demonstration trajectories from LIBERO~\\cite{liu2023libero} with $L_2$ loss:\ndocs/paper/method.tex:52:[Omitted long matching line]\ndocs/paper/method.tex:59:[Omitted long matching line]\ndocs/paper/method.tex:65:[Omitted long matching line]\ndocs/paper/introduction.tex:5:Vision-language-action models (VLAs) that generate actions via flow matching~\\cite{black2024pi0,shukor2025smolvla,lipman2023flow} have reached high success rates on in-distribution benchmarks such as LIBERO~\\cite{liu2023libero}.\ndocs/paper/introduction.tex:6:Yet this near-saturation masks a fragile reality: visual and physical perturbations routinely encountered in deployment (camera viewpoint shifts, object layout changes, robot initial state variation) can degrade success rates by over 65 percentage points. For example, $\\pi_0$ drops from 94.2\\% to 6.6\\% under robot initial-state perturbation, and UniVLA from 95.2\\% to 4.3\\% under camera viewpoint changes~\\cite{fei2025liberoplus}.\ndocs/paper/introduction.tex:11:\\emph{Training-time methods} improve the base policy itself through robustness-aware objectives~\\cite{srpo2025,robustvla2025,digflow2025} or test-time reinforcement learning~\\cite{liu2026ttvla}.\ndocs/paper/introduction.tex:14:ReconVLA~\\cite{chen2026reconvla} applies conformal quantile regression to calibrate action-level uncertainty and uses these estimates for uncertainty-guided action selection and out-of-distribution detection, taking a complementary UQ-driven approach rather than learning explicit corrective residuals.\ndocs/paper/introduction.tex:15:VLA-Pilot~\\cite{li2025vlapilot} applies evolutionary optimization over action samples, but incurs 2.41\\,s per control step, too slow for real-time manipulation.\ndocs/paper/introduction.tex:16:A2C2~\\cite{a2c2_2025} learns a per-step correction head for pre-generated action chunks on a frozen VLA, but applies correction unconditionally without multi-sample selection or explicit magnitude control.\ndocs/paper/introduction.tex:21:At each control step, ACR-VLA draws $K{=}10$ action samples from the frozen VLA, selects the most conforming candidate via Mahalanobis-based nonconformity scoring with shrinkage covariance estimation~\\cite{ledoit2004well,braun2025cgs}, and then applies a learned residual correction via a lightweight \\emph{Conformal Residual Module} (CRM).\ndocs/paper/introduction.tex:28:We evaluate ACR-VLA on LIBERO-Object (10 tasks, 100 trials per method) and LIBERO-Spatial (10 tasks, 100 trials) using SmolVLA~\\cite{shukor2025smolvla} as the frozen backbone. Three findings emerge:",
    "numLines": 46
  }
}
```

</details>

---

### Assistant

_source line 19_

<details><summary>Logged reasoning block</summary>

```text
Good. I have all cite keys. Now let me write the final introduction.

Key cite keys I need:
- \cite{black2024pi0,shukor2025smolvla,lipman2023flow} for flow-matching VLAs
- \cite{liu2023libero} for LIBERO
- \cite{fei2025liberoplus} for LIBERO+ robustness data
- \cite{srpo2025,robustvla2025,digflow2025} for training-time methods


- \cite{liu2026ttvla,chen2026reconvla,li2025vlapilot,a2c2_2025,kim2024openvla} for recent VLA approaches
- \cite{ross2011dagger} for compounding error

Now I'm drafting the final version, making sure to briefly mention the spatial null result in finding (1) to be transparent about the scope, and deciding whether to include the Conformal Residual Module discussion.

Looking back at the task description and the method section, I think the cleanest approach is to introduce it once as "Conformal Residual Module (CRM)" and then refer to it as the correction module or just CRM going forward. The method section already notes the naming mismatch, so I don't need to belabor that point in the intro. I'll keep the focus on what it actually does—a correction module with about 327K parameters conditioned on the observation embedding and selected action—rather than overemphasizing the conformal aspect.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8146b578-f41a-49c2-b99a-be63bde75274",
  "uuid": "744f39b8-17c7-4730-998f-cd1738b068fe",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VuaXQYB8twAhgm3RbgpYXZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8831,
      "cache_read_input_tokens": 49054,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8831
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Assistant

_source line 20_

Writing the rewritten introduction now.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8146b578-f41a-49c2-b99a-be63bde75274",
  "uuid": "28fc2b6b-ce32-496e-96c2-583c5efd937a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VuaXQYB8twAhgm3RbgpYXZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8831,
      "cache_read_input_tokens": 49054,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8831
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 21_

<details open><summary>🔧 Tool call — Write · `toolu_01Wq9AqKL2n7s1fsfvLLN6t5`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/introduction.tex",
  "content": "\\section{Introduction}\n\\label{sec:intro}\n\n% --- Para 1: VLAs are impressive but fragile under distribution shift ---\nVision-Language-Action models (VLAs) that generate actions via flow matching~\\cite{black2024pi0,shukor2025smolvla,lipman2023flow} have reached near-saturation on in-distribution benchmarks such as LIBERO~\\cite{liu2023libero}.\nYet this performance masks severe fragility: visual and physical perturbations common in deployment (camera viewpoint shifts, object layout changes, robot initial-state variation) routinely degrade success by over 65 percentage points.\nOn the LIBERO+ benchmark~\\cite{fei2025liberoplus}, $\\pi_0$ drops from 94.2\\% to 6.6\\% under initial-state perturbation, and UniVLA drops from 95.2\\% to 4.3\\% under viewpoint changes.\nClosing this robustness gap without retraining the base policy is a prerequisite for deploying VLAs outside tightly controlled laboratory settings.\n\n% --- Para 2: Existing approaches and the gap ---\nTwo lines of work address this challenge.\nTraining-time methods improve the base policy through robustness-aware objectives~\\cite{srpo2025,robustvla2025,digflow2025} or test-time reinforcement learning~\\cite{liu2026ttvla}, but require retraining or per-task RL and remain bounded by the training distribution.\nInference-time methods leave the policy frozen: ReconVLA~\\cite{chen2026reconvla} applies conformal quantile regression for uncertainty quantification and out-of-distribution detection, but does not learn corrective residuals; A2C2~\\cite{a2c2_2025} trains a per-step correction head on frozen VLA action chunks, but applies correction unconditionally without multi-sample selection or explicit magnitude control; VLA-Pilot~\\cite{li2025vlapilot} applies evolutionary optimization over action samples, but incurs 2.41\\,s per control step.\nDespite growing interest in inference-time action refinement, fundamental design questions remain unanswered: how much does candidate selection contribute relative to learned correction?\nWhat observation features should condition the correction module?\nHow sensitive is closed-loop performance to correction magnitude?\nNo existing work provides a systematic decomposition of these factors.\n\n% --- Para 3: Our approach — sample-then-correct ---\nWe introduce ACR-VLA, an inference-time action refinement module for frozen flow-matching VLAs.\nAt each control step, ACR-VLA draws $K{=}10$ action samples from the frozen VLA, selects the candidate closest to the sample mean by $L_2$ distance, and applies a learned residual correction via a lightweight Conformal Residual Module (CRM).\nThe CRM is a ${\\sim}$327K-parameter MLP that takes as input the frozen VLA's observation embedding ($\\mathbb{R}^{960}$) concatenated with the selected action ($\\mathbb{R}^{30}$) and predicts a residual $\\boldsymbol{\\delta}$ whose $L_2$ norm is clipped to a bound $\\varepsilon$, producing the corrected action $\\mathbf{a}^* = a_{\\mathrm{base}} + \\mathrm{clip}(\\boldsymbol{\\delta})$.\nThe key design insight is twofold: correction on a pre-screened starting point is more reliable than correction on an arbitrary single sample, and bounding the correction magnitude prevents compounding errors from destabilizing the closed-loop trajectory.\nThe base VLA is never modified; ACR-VLA attaches as a post-hoc module to any frozen flow-matching VLA.\n\n% --- Para 4: Three key findings ---\nWe evaluate ACR-VLA on LIBERO-Object and LIBERO-Spatial (10 tasks, 100 trials each) using SmolVLA~\\cite{shukor2025smolvla} as the frozen backbone.\nThree findings emerge.\n\n\\textbf{(1) The full pipeline significantly improves over the frozen VLA, with correction as the dominant factor.}\nWith observation-only conditioning at $\\varepsilon{=}0.2$, the pipeline achieves 17.5\\% mean success across 6 seeds versus 11.2\\% for VLA-only across 5 seeds (+6.3\\,pp, pooled Fisher's exact $p = 0.0074$, Cohen's $d = 1.21$).\nComponent decomposition reveals that correction accounts for ${\\sim}$5\\,pp and selection for ${\\sim}$1\\,pp: at $K{=}1$ (correction without selection), success is 10.3\\%, at the VLA-only level; argmin selection alone yields 12.4\\%.\nNeither component suffices in isolation.\nOn LIBERO-Spatial, all methods cluster within 30--35\\%, a null result that bounds the scope of action-level correction to object-centric manipulation (Section~\\ref{sec:main_results}, Table~\\ref{tab:main}).\n\n\\textbf{(2) Observation features suffice for correction; conformal uncertainty features hurt.}\nWe compare three CRM conditioning variants at fixed $\\varepsilon{=}0.1$: observation-only conditioning (19\\%, seed 42) substantially outperforms per-DOF conformal conditioning (11\\%), argmin selection alone (12\\%), and scalar uncertainty conditioning (9\\%).\nThe observation-only variant is also robust across magnitude bounds, maintaining 13.5--17.5\\% for all tested $\\varepsilon$, while per-DOF conditioning collapses from 14\\% to 0\\% as $\\varepsilon$ increases.\nThe root cause is rank-deficient covariance estimation at $K{=}10$ samples in 6 dimensions (Section~\\ref{sec:ablation}, Section~\\ref{sec:magnitude_results}).\n\n\\textbf{(3) Multi-sample correction requires stochastic action diversity.}\nSmolVLA (flow-matching) produces diverse samples suitable for selection and correction.\nOpenVLA~\\cite{kim2024openvla} (autoregressive tokenization) generates 8 out of 10 identical samples with per-DOF variance below $10^{-30}$.\nThis establishes an architectural applicability boundary: the pipeline is specific to stochastic generative VLAs (Section~\\ref{sec:applicability}, Figure~\\ref{fig:diversity}).\n\n% --- Para 5: Contributions ---\nOur contributions are:\n\\begin{enumerate}[leftmargin=*,nosep]\n  \\item \\textbf{A multi-sample inference-time correction pipeline with component decomposition.}\n  We propose ACR-VLA, which combines $L_2$ argmin selection with bounded residual correction for frozen flow-matching VLAs, and decompose the pipeline into selection (${\\sim}$1\\,pp) and correction (${\\sim}$5\\,pp) contributions.\n  The full pipeline achieves a statistically significant +6.3\\,pp improvement over the frozen VLA baseline ($p = 0.0074$, 6 seeds) on LIBERO-Object (Section~\\ref{sec:main_results}).\n\n  \\item \\textbf{First systematic conditioning and magnitude study, with an honest negative on conformal features.}\n  We compare three conditioning variants across a $6{\\times}$ range of magnitude bounds and find that observation-only conditioning is robust across all settings, while per-DOF conformal features and scalar uncertainty are harmful.\n  This challenges the intuition that richer uncertainty features improve correction (Section~\\ref{sec:ablation}, Section~\\ref{sec:magnitude_results}).\n\n  \\item \\textbf{Applicability boundary: stochastic diversity as a prerequisite.}\n  We show that tokenized VLAs lack the sample diversity required for multi-sample correction and that action-level correction does not transfer to spatial reasoning tasks, establishing clear scope boundaries for inference-time action refinement (Section~\\ref{sec:applicability}).\n\\end{enumerate}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8146b578-f41a-49c2-b99a-be63bde75274",
  "uuid": "e94cfef0-4f1d-4aa2-ad4b-ba0baf5d7345",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VuaXQYB8twAhgm3RbgpYXZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8831,
      "cache_read_input_tokens": 49054,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8831
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-18T10:18:48.758Z_

<details><summary>↩ Tool result · `toolu_01Wq9AqKL2n7s1fsfvLLN6t5`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/introduction.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8146b578-f41a-49c2-b99a-be63bde75274",
  "uuid": "ed3b4c2d-204a-4f84-b9e8-634450528a60",
  "tool_use_result": {
    "type": "update",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/introduction.tex",
    "content": "\\section{Introduction}\n\\label{sec:intro}\n\n% --- Para 1: VLAs are impressive but fragile under distribution shift ---\nVision-Language-Action models (VLAs) that generate actions via flow matching~\\cite{black2024pi0,shukor2025smolvla,lipman2023flow} have reached near-saturation on in-distribution benchmarks such as LIBERO~\\cite{liu2023libero}.\nYet this performance masks severe fragility: visual and physical perturbations common in deployment (camera viewpoint shifts, object layout changes, robot initial-state variation) routinely degrade success by over 65 percentage points.\nOn the LIBERO+ benchmark~\\cite{fei2025liberoplus}, $\\pi_0$ drops from 94.2\\% to 6.6\\% under initial-state perturbation, and UniVLA drops from 95.2\\% to 4.3\\% under viewpoint changes.\nClosing this robustness gap without retraining the base policy is a prerequisite for deploying VLAs outside tightly controlled laboratory settings.\n\n% --- Para 2: Existing approaches and the gap ---\nTwo lines of work address this challenge.\nTraining-time methods improve the base policy through robustness-aware objectives~\\cite{srpo2025,robustvla2025,digflow2025} or test-time reinforcement learning~\\cite{liu2026ttvla}, but require retraining or per-task RL and remain bounded by the training distribution.\nInference-time methods leave the policy frozen: ReconVLA~\\cite{chen2026reconvla} applies conformal quantile regression for uncertainty quantification and out-of-distribution detection, but does not learn corrective residuals; A2C2~\\cite{a2c2_2025} trains a per-step correction head on frozen VLA action chunks, but applies correction unconditionally without multi-sample selection or explicit magnitude control; VLA-Pilot~\\cite{li2025vlapilot} applies evolutionary optimization over action samples, but incurs 2.41\\,s per control step.\nDespite growing interest in inference-time action refinement, fundamental design questions remain unanswered: how much does candidate selection contribute relative to learned correction?\nWhat observation features should condition the correction module?\nHow sensitive is closed-loop performance to correction magnitude?\nNo existing work provides a systematic decomposition of these factors.\n\n% --- Para 3: Our approach — sample-then-correct ---\nWe introduce ACR-VLA, an inference-time action refinement module for frozen flow-matching VLAs.\nAt each control step, ACR-VLA draws $K{=}10$ action samples from the frozen VLA, selects the candidate closest to the sample mean by $L_2$ distance, and applies a learned residual correction via a lightweight Conformal Residual Module (CRM).\nThe CRM is a ${\\sim}$327K-parameter MLP that takes as input the frozen VLA's observation embedding ($\\mathbb{R}^{960}$) concatenated with the selected action ($\\mathbb{R}^{30}$) and predicts a residual $\\boldsymbol{\\delta}$ whose $L_2$ norm is clipped to a bound $\\varepsilon$, producing the corrected action $\\mathbf{a}^* = a_{\\mathrm{base}} + \\mathrm{clip}(\\boldsymbol{\\delta})$.\nThe key design insight is twofold: correction on a pre-screened starting point is more reliable than correction on an arbitrary single sample, and bounding the correction magnitude prevents compounding errors from destabilizing the closed-loop trajectory.\nThe base VLA is never modified; ACR-VLA attaches as a post-hoc module to any frozen flow-matching VLA.\n\n% --- Para 4: Three key findings ---\nWe evaluate ACR-VLA on LIBERO-Object and LIBERO-Spatial (10 tasks, 100 trials each) using SmolVLA~\\cite{shukor2025smolvla} as the frozen backbone.\nThree findings emerge.\n\n\\textbf{(1) The full pipeline significantly improves over the frozen VLA, with correction as the dominant factor.}\nWith observation-only conditioning at $\\varepsilon{=}0.2$, the pipeline achieves 17.5\\% mean success across 6 seeds versus 11.2\\% for VLA-only across 5 seeds (+6.3\\,pp, pooled Fisher's exact $p = 0.0074$, Cohen's $d = 1.21$).\nComponent decomposition reveals that correction accounts for ${\\sim}$5\\,pp and selection for ${\\sim}$1\\,pp: at $K{=}1$ (correction without selection), success is 10.3\\%, at the VLA-only level; argmin selection alone yields 12.4\\%.\nNeither component suffices in isolation.\nOn LIBERO-Spatial, all methods cluster within 30--35\\%, a null result that bounds the scope of action-level correction to object-centric manipulation (Section~\\ref{sec:main_results}, Table~\\ref{tab:main}).\n\n\\textbf{(2) Observation features suffice for correction; conformal uncertainty features hurt.}\nWe compare three CRM conditioning variants at fixed $\\varepsilon{=}0.1$: observation-only conditioning (19\\%, seed 42) substantially outperforms per-DOF conformal conditioning (11\\%), argmin selection alone (12\\%), and scalar uncertainty conditioning (9\\%).\nThe observation-only variant is also robust across magnitude bounds, maintaining 13.5--17.5\\% for all tested $\\varepsilon$, while per-DOF conditioning collapses from 14\\% to 0\\% as $\\varepsilon$ increases.\nThe root cause is rank-deficient covariance estimation at $K{=}10$ samples in 6 dimensions (Section~\\ref{sec:ablation}, Section~\\ref{sec:magnitude_results}).\n\n\\textbf{(3) Multi-sample correction requires stochastic action diversity.}\nSmolVLA (flow-matching) produces diverse samples suitable for selection and correction.\nOpenVLA~\\cite{kim2024openvla} (autoregressive tokenization) generates 8 out of 10 identical samples with per-DOF variance below $10^{-30}$.\nThis establishes an architectural applicability boundary: the pipeline is specific to stochastic generative VLAs (Section~\\ref{sec:applicability}, Figure~\\ref{fig:diversity}).\n\n% --- Para 5: Contributions ---\nOur contributions are:\n\\begin{enumerate}[leftmargin=*,nosep]\n  \\item \\textbf{A multi-sample inference-time correction pipeline with component decomposition.}\n  We propose ACR-VLA, which combines $L_2$ argmin selection with bounded residual correction for frozen flow-matching VLAs, and decompose the pipeline into selection (${\\sim}$1\\,pp) and correction (${\\sim}$5\\,pp) contributions.\n  The full pipeline achieves a statistically significant +6.3\\,pp improvement over the frozen VLA baseline ($p = 0.0074$, 6 seeds) on LIBERO-Object (Section~\\ref{sec:main_results}).\n\n  \\item \\textbf{First systematic conditioning and magnitude study, with an honest negative on conformal features.}\n  We compare three conditioning variants across a $6{\\times}$ range of magnitude bounds and find that observation-only conditioning is robust across all settings, while per-DOF conformal features and scalar uncertainty are harmful.\n  This challenges the intuition that richer uncertainty features improve correction (Section~\\ref{sec:ablation}, Section~\\ref{sec:magnitude_results}).\n\n  \\item \\textbf{Applicability boundary: stochastic diversity as a prerequisite.}\n  We show that tokenized VLAs lack the sample diversity required for multi-sample correction and that action-level correction does not transfer to spatial reasoning tasks, establishing clear scope boundaries for inference-time action refinement (Section~\\ref{sec:applicability}).\n\\end{enumerate}\n",
    "structuredPatch": [
      {
        "oldStart": 2,
        "oldLines": 63,
        "newStart": 2,
        "newLines": 58,
        "lines": [
          " \\label{sec:intro}",
          " ",
          " % --- Para 1: VLAs are impressive but fragile under distribution shift ---",
          "-Vision-language-action models (VLAs) that generate actions via flow matching~\\cite{black2024pi0,shukor2025smolvla,lipman2023flow} have reached high success rates on in-distribution benchmarks such as LIBERO~\\cite{liu2023libero}.",
          "-Yet this near-saturation masks a fragile reality: visual and physical perturbations routinely encountered in deployment (camera viewpoint shifts, object layout changes, robot initial state variation) can degrade success rates by over 65 percentage points. For example, $\\pi_0$ drops from 94.2\\% to 6.6\\% under robot initial-state perturbation, and UniVLA from 95.2\\% to 4.3\\% under camera viewpoint changes~\\cite{fei2025liberoplus}.",
          "-Closing this robustness gap without retraining the base policy is a prerequisite for deploying VLAs outside tightly controlled settings.",
          "+Vision-Language-Action models (VLAs) that generate actions via flow matching~\\cite{black2024pi0,shukor2025smolvla,lipman2023flow} have reached near-saturation on in-distribution benchmarks such as LIBERO~\\cite{liu2023libero}.",
          "+Yet this performance masks severe fragility: visual and physical perturbations common in deployment (camera viewpoint shifts, object layout changes, robot initial-state variation) routinely degrade success by over 65 percentage points.",
          "+On the LIBERO+ benchmark~\\cite{fei2025liberoplus}, $\\pi_0$ drops from 94.2\\% to 6.6\\% under initial-state perturbation, and UniVLA drops from 95.2\\% to 4.3\\% under viewpoint changes.",
          "+Closing this robustness gap without retraining the base policy is a prerequisite for deploying VLAs outside tightly controlled laboratory settings.",
          " ",
          " % --- Para 2: Existing approaches and the gap ---",
          "-Two lines of work address VLA robustness.",
          "-\\emph{Training-time methods} improve the base policy itself through robustness-aware objectives~\\cite{srpo2025,robustvla2025,digflow2025} or test-time reinforcement learning~\\cite{liu2026ttvla}.",
          "-These approaches are effective but require retraining or per-task RL, and their gains are bounded by the training distribution.",
          "-\\emph{Inference-time methods} leave the policy frozen.",
          "-ReconVLA~\\cite{chen2026reconvla} applies conformal quantile regression to calibrate action-level uncertainty and uses these estimates for uncertainty-guided action selection and out-of-distribution detection, taking a complementary UQ-driven approach rather than learning explicit corrective residuals.",
          "-VLA-Pilot~\\cite{li2025vlapilot} applies evolutionary optimization over action samples, but incurs 2.41\\,s per control step, too slow for real-time manipulation.",
          "-A2C2~\\cite{a2c2_2025} learns a per-step correction head for pre-generated action chunks on a frozen VLA, but applies correction unconditionally without multi-sample selection or explicit magnitude control.",
          "-In short, no existing inference-time method combines multi-sample conformal selection with bounded residual correction in a two-stage pipeline.",
          "+Two lines of work address this challenge.",
          "+Training-time methods improve the base policy through robustness-aware objectives~\\cite{srpo2025,robustvla2025,digflow2025} or test-time reinforcement learning~\\cite{liu2026ttvla}, but require retraining or per-task RL and remain bounded by the training distribution.",
          "+Inference-time methods leave the policy frozen: ReconVLA~\\cite{chen2026reconvla} applies conformal quantile regression for uncertainty quantification and out-of-distribution detection, but does not learn corrective residuals; A2C2~\\cite{a2c2_2025} trains a per-step correction head on frozen VLA action chunks, but applies correction unconditionally without multi-sample selection or explicit magnitude control; VLA-Pilot~\\cite{li2025vlapilot} applies evolutionary optimization over action samples, but incurs 2.41\\,s per control step.",
          "+Despite growing interest in inference-time action refinement, fundamental design questions remain unanswered: how much does candidate selection contribute relative to learned correction?",
          "+What observation features should condition the correction module?",
          "+How sensitive is closed-loop performance to correction magnitude?",
          "+No existing work provides a systematic decomposition of these factors.",
          " ",
          " % --- Para 3: Our approach — sample-then-correct ---",
          "-We introduce \\textbf{ACR-VLA} (\\textbf{A}daptive \\textbf{C}onformal \\textbf{R}efinement for VLA), an inference-time module that improves frozen VLA actions through a \\emph{sample-then-correct} pipeline.",
          "-At each control step, ACR-VLA draws $K{=}10$ action samples from the frozen VLA, selects the most conforming candidate via Mahalanobis-based nonconformity scoring with shrinkage covariance estimation~\\cite{ledoit2004well,braun2025cgs}, and then applies a learned residual correction via a lightweight \\emph{Conformal Residual Module} (CRM).",
          "-CRM is a 330K-parameter MLP conditioned on the VLA's frozen observation embedding.",
          "-It predicts a small residual $\\boldsymbol{\\delta}$ whose $L_2$ norm is clipped to a bound $\\varepsilon$, producing the corrected action $\\mathbf{a}^* = a_{\\mathrm{base}} + \\mathrm{clip}(\\boldsymbol{\\delta})$.",
          "-The critical design insight is that correction operates on a high-quality starting point (the conformal-selected action) and that bounding the correction magnitude prevents compounding errors from destabilizing the closed-loop trajectory.",
          "+We introduce ACR-VLA, an inference-time action refinement module for frozen flow-matching VLAs.",
          "+At each control step, ACR-VLA draws $K{=}10$ action samples from the frozen VLA, selects the candidate closest to the sample mean by $L_2$ distance, and applies a learned residual correction via a lightweight Conformal Residual Module (CRM).",
          "+The CRM is a ${\\sim}$327K-parameter MLP that takes as input the frozen VLA's observation embedding ($\\mathbb{R}^{960}$) concatenated with the selected action ($\\mathbb{R}^{30}$) and predicts a residual $\\boldsymbol{\\delta}$ whose $L_2$ norm is clipped to a bound $\\varepsilon$, producing the corrected action $\\mathbf{a}^* = a_{\\mathrm{base}} + \\mathrm{clip}(\\boldsymbol{\\delta})$.",
          "+The key design insight is twofold: correction on a pre-screened starting point is more reliable than correction on an arbitrary single sample, and bounding the correction magnitude prevents compounding errors from destabilizing the closed-loop trajectory.",
          " The base VLA is never modified; ACR-VLA attaches as a post-hoc module to any frozen flow-matching VLA.",
          " ",
          "-% --- Para 4: Key findings (with exp_id references) ---",
          "-We evaluate ACR-VLA on LIBERO-Object (10 tasks, 100 trials per method) and LIBERO-Spatial (10 tasks, 100 trials) using SmolVLA~\\cite{shukor2025smolvla} as the frozen backbone. Three findings emerge:",
          "+% --- Para 4: Three key findings ---",
          "+We evaluate ACR-VLA on LIBERO-Object and LIBERO-Spatial (10 tasks, 100 trials each) using SmolVLA~\\cite{shukor2025smolvla} as the frozen backbone.",
          "+Three findings emerge.",
          " ",
          "-\\textbf{(1)~The full pipeline significantly improves over the frozen VLA.}",
          "-Across five seeds on LIBERO-Object, the sample-then-correct pipeline (obs\\_only, $\\varepsilon{=}0.2$) achieves mean $17.0 \\pm 2.8$\\% versus VLA-only mean $10.75 \\pm 1.5$\\% ($p < 0.01$, pooled Fisher's exact test), a +6\\,pp improvement.",
          "-% obs_only eps=0.2 seeds 42-46: 22/16/16/16/15%. VLA-only seeds 42-45: 10.75±1.5%. Argmin seeds 42-45: 13.5±2.4%.",
          "-The margin over conformal selection alone (Argmin mean $13.5 \\pm 2.4$\\%) is +3.5\\,pp, consistent across seeds but not statistically significant ($p = 0.075$), suggesting larger evaluation budgets are needed to confirm this gap.",
          "+\\textbf{(1) The full pipeline significantly improves over the frozen VLA, with correction as the dominant factor.}",
          "+With observation-only conditioning at $\\varepsilon{=}0.2$, the pipeline achieves 17.5\\% mean success across 6 seeds versus 11.2\\% for VLA-only across 5 seeds (+6.3\\,pp, pooled Fisher's exact $p = 0.0074$, Cohen's $d = 1.21$).",
          "+Component decomposition reveals that correction accounts for ${\\sim}$5\\,pp and selection for ${\\sim}$1\\,pp: at $K{=}1$ (correction without selection), success is 10.3\\%, at the VLA-only level; argmin selection alone yields 12.4\\%.",
          "+Neither component suffices in isolation.",
          "+On LIBERO-Spatial, all methods cluster within 30--35\\%, a null result that bounds the scope of action-level correction to object-centric manipulation (Section~\\ref{sec:main_results}, Table~\\ref{tab:main}).",
          " ",
          "-\\textbf{(2)~Observation features suffice for correction; conformal features do not help.}",
          "-Counter to intuition from synthetic experiments, conditioning CRM on per-DOF conformal statistics (perdof: 11.0\\%) performs no better than selection alone (12.0\\%), while scalar conformal conditioning (9.0\\%) is actively harmful.",
          "-% exp_id: eval-acr-object-v4-small (perdof 11.0%), eval-acr-object-v4-scalar (9.0%)",
          "-Only observation-conditioned CRM (19.0\\%) produces meaningful improvement.",
          "-This honest negative result highlights a gap between per-step prediction accuracy (where richer features help in offline evaluation) and closed-loop task success, where covariance estimation noise from $K{=}10$ samples undermines per-DOF conditioning.",
          "+\\textbf{(2) Observation features suffice for correction; conformal uncertainty features hurt.}",
          "+We compare three CRM conditioning variants at fixed $\\varepsilon{=}0.1$: observation-only conditioning (19\\%, seed 42) substantially outperforms per-DOF conformal conditioning (11\\%), argmin selection alone (12\\%), and scalar uncertainty conditioning (9\\%).",
          "+The observation-only variant is also robust across magnitude bounds, maintaining 13.5--17.5\\% for all tested $\\varepsilon$, while per-DOF conditioning collapses from 14\\% to 0\\% as $\\varepsilon$ increases.",
          "+The root cause is rank-deficient covariance estimation at $K{=}10$ samples in 6 dimensions (Section~\\ref{sec:ablation}, Section~\\ref{sec:magnitude_results}).",
          " ",
          "-\\textbf{(3)~Correction magnitude control is critical and previously unrecognized.}",
          "-Without magnitude bounding, the per-DOF-conditioned CRM's natural output ($\\|\\boldsymbol{\\delta}\\|_2 \\approx 1.42$) causes catastrophic failure: 0\\% success on LIBERO-Spatial, as compounding correction errors rapidly drive the state distribution away from the CRM's training regime.",
          "-Constraining corrections to $\\|\\boldsymbol{\\delta}\\|_2 \\leq 0.1$ recovers the full improvement.",
          "-% exp_id: eval-acr-spatial-v4-default-r3 (norm=1.42, 0%), eval-acr-object-v4-obs-only (norm=0.1, 19.0%)",
          "-Observation-conditioned CRM maintains stable 35--36\\% success on LIBERO-Spatial across $\\varepsilon \\in [0.05, 0.3]$, while per-DOF-conditioned CRM collapses from 35\\% to 26\\% over the same range. This robustness gap is the paper's strongest evidence: it holds across all tested seeds and magnitude bounds, independent of the seed-42 outlier.",
          "-% exp_id: eval-mag-obsonly-norm005, eval-mag-obsonly-norm03, eval-mag-perdof-norm03",
          "+\\textbf{(3) Multi-sample correction requires stochastic action diversity.}",
          "+SmolVLA (flow-matching) produces diverse samples suitable for selection and correction.",
          "+OpenVLA~\\cite{kim2024openvla} (autoregressive tokenization) generates 8 out of 10 identical samples with per-DOF variance below $10^{-30}$.",
          "+This establishes an architectural applicability boundary: the pipeline is specific to stochastic generative VLAs (Section~\\ref{sec:applicability}, Figure~\\ref{fig:diversity}).",
          " ",
          "-We note that correction offers targeted improvements on object-centric manipulation rather than universal gains: on LIBERO-Spatial, the best CRM variant performs within 1\\,pp of the selection baseline, suggesting that the correction mechanism is most effective when distribution shift induces systematic action biases that a learned module can identify and compensate.",
          "-",
          " % --- Para 5: Contributions ---",
          " Our contributions are:",
          " \\begin{enumerate}[leftmargin=*,nosep]",
          "-  \\item \\textbf{A sample-then-correct pipeline for frozen VLAs.}",
          "-  We propose ACR-VLA, which combines conformal sample selection with learned residual correction for frozen flow-matching VLAs.",
          "-  On LIBERO-Object, this pipeline significantly improves over the frozen VLA baseline (+6\\,pp, $p < 0.01$, 5-seed pooled test).",
          "-  % obs_only eps=0.2 5-seed mean 17.0±2.8% vs VLA-only 4-seed mean 10.75±1.5%",
          "+  \\item \\textbf{A multi-sample inference-time correction pipeline with component decomposition.}",
          "+  We propose ACR-VLA, which combines $L_2$ argmin selection with bounded residual correction for frozen flow-matching VLAs, and decompose the pipeline into selection (${\\sim}$1\\,pp) and correction (${\\sim}$5\\,pp) contributions.",
          "+  The full pipeline achieves a statistically significant +6.3\\,pp improvement over the frozen VLA baseline ($p = 0.0074$, 6 seeds) on LIBERO-Object (Section~\\ref{sec:main_results}).",
          " ",
          "-  \\item \\textbf{Systematic conditioning comparison and honest negative result.}",
          "-  We compare three CRM conditioning variants (per-DOF conformal features, scalar uncertainty, and observation features) and find that only observation conditioning is effective.",
          "-  This challenges the intuition that richer uncertainty features should yield better corrections, and reveals that covariance estimation noise at $K{=}10$ undermines per-DOF conditioning in closed-loop settings.",
          "+  \\item \\textbf{First systematic conditioning and magnitude study, with an honest negative on conformal features.}",
          "+  We compare three conditioning variants across a $6{\\times}$ range of magnitude bounds and find that observation-only conditioning is robust across all settings, while per-DOF conformal features and scalar uncertainty are harmful.",
          "+  This challenges the intuition that richer uncertainty features improve correction (Section~\\ref{sec:ablation}, Section~\\ref{sec:magnitude_results}).",
          " ",
          "-  \\item \\textbf{Systematic empirical study of correction magnitude sensitivity for VLA action refinement.}",
          "-  We show that unbounded correction causes catastrophic failure and that observation-conditioned CRM is uniquely robust across a $6{\\times}$ range of magnitude bounds ($\\varepsilon \\in [0.05, 0.3]$), establishing magnitude control as a critical design axis for inference-time action correction.",
          "+  \\item \\textbf{Applicability boundary: stochastic diversity as a prerequisite.}",
          "+  We show that tokenized VLAs lack the sample diversity required for multi-sample correction and that action-level correction does not transfer to spatial reasoning tasks, establishing clear scope boundaries for inference-time action refinement (Section~\\ref{sec:applicability}).",
          " \\end{enumerate}"
        ]
      }
    ],
    "originalFile": "\\section{Introduction}\n\\label{sec:intro}\n\n% --- Para 1: VLAs are impressive but fragile under distribution shift ---\nVision-language-action models (VLAs) that generate actions via flow matching~\\cite{black2024pi0,shukor2025smolvla,lipman2023flow} have reached high success rates on in-distribution benchmarks such as LIBERO~\\cite{liu2023libero}.\nYet this near-saturation masks a fragile reality: visual and physical perturbations routinely encountered in deployment (camera viewpoint shifts, object layout changes, robot initial state variation) can degrade success rates by over 65 percentage points. For example, $\\pi_0$ drops from 94.2\\% to 6.6\\% under robot initial-state perturbation, and UniVLA from 95.2\\% to 4.3\\% under camera viewpoint changes~\\cite{fei2025liberoplus}.\nClosing this robustness gap without retraining the base policy is a prerequisite for deploying VLAs outside tightly controlled settings.\n\n% --- Para 2: Existing approaches and the gap ---\nTwo lines of work address VLA robustness.\n\\emph{Training-time methods} improve the base policy itself through robustness-aware objectives~\\cite{srpo2025,robustvla2025,digflow2025} or test-time reinforcement learning~\\cite{liu2026ttvla}.\nThese approaches are effective but require retraining or per-task RL, and their gains are bounded by the training distribution.\n\\emph{Inference-time methods} leave the policy frozen.\nReconVLA~\\cite{chen2026reconvla} applies conformal quantile regression to calibrate action-level uncertainty and uses these estimates for uncertainty-guided action selection and out-of-distribution detection, taking a complementary UQ-driven approach rather than learning explicit corrective residuals.\nVLA-Pilot~\\cite{li2025vlapilot} applies evolutionary optimization over action samples, but incurs 2.41\\,s per control step, too slow for real-time manipulation.\nA2C2~\\cite{a2c2_2025} learns a per-step correction head for pre-generated action chunks on a frozen VLA, but applies correction unconditionally without multi-sample selection or explicit magnitude control.\nIn short, no existing inference-time method combines multi-sample conformal selection with bounded residual correction in a two-stage pipeline.\n\n% --- Para 3: Our approach — sample-then-correct ---\nWe introduce \\textbf{ACR-VLA} (\\textbf{A}daptive \\textbf{C}onformal \\textbf{R}efinement for VLA), an inference-time module that improves frozen VLA actions through a \\emph{sample-then-correct} pipeline.\nAt each control step, ACR-VLA draws $K{=}10$ action samples from the frozen VLA, selects the most conforming candidate via Mahalanobis-based nonconformity scoring with shrinkage covariance estimation~\\cite{ledoit2004well,braun2025cgs}, and then applies a learned residual correction via a lightweight \\emph{Conformal Residual Module} (CRM).\nCRM is a 330K-parameter MLP conditioned on the VLA's frozen observation embedding.\nIt predicts a small residual $\\boldsymbol{\\delta}$ whose $L_2$ norm is clipped to a bound $\\varepsilon$, producing the corrected action $\\mathbf{a}^* = a_{\\mathrm{base}} + \\mathrm{clip}(\\boldsymbol{\\delta})$.\nThe critical design insight is that correction operates on a high-quality starting point (the conformal-selected action) and that bounding the correction magnitude prevents compounding errors from destabilizing the closed-loop trajectory.\nThe base VLA is never modified; ACR-VLA attaches as a post-hoc module to any frozen flow-matching VLA.\n\n% --- Para 4: Key findings (with exp_id references) ---\nWe evaluate ACR-VLA on LIBERO-Object (10 tasks, 100 trials per method) and LIBERO-Spatial (10 tasks, 100 trials) using SmolVLA~\\cite{shukor2025smolvla} as the frozen backbone. Three findings emerge:\n\n\\textbf{(1)~The full pipeline significantly improves over the frozen VLA.}\nAcross five seeds on LIBERO-Object, the sample-then-correct pipeline (obs\\_only, $\\varepsilon{=}0.2$) achieves mean $17.0 \\pm 2.8$\\% versus VLA-only mean $10.75 \\pm 1.5$\\% ($p < 0.01$, pooled Fisher's exact test), a +6\\,pp improvement.\n% obs_only eps=0.2 seeds 42-46: 22/16/16/16/15%. VLA-only seeds 42-45: 10.75±1.5%. Argmin seeds 42-45: 13.5±2.4%.\nThe margin over conformal selection alone (Argmin mean $13.5 \\pm 2.4$\\%) is +3.5\\,pp, consistent across seeds but not statistically significant ($p = 0.075$), suggesting larger evaluation budgets are needed to confirm this gap.\n\n\\textbf{(2)~Observation features suffice for correction; conformal features do not help.}\nCounter to intuition from synthetic experiments, conditioning CRM on per-DOF conformal statistics (perdof: 11.0\\%) performs no better than selection alone (12.0\\%), while scalar conformal conditioning (9.0\\%) is actively harmful.\n% exp_id: eval-acr-object-v4-small (perdof 11.0%), eval-acr-object-v4-scalar (9.0%)\nOnly observation-conditioned CRM (19.0\\%) produces meaningful improvement.\nThis honest negative result highlights a gap between per-step prediction accuracy (where richer features help in offline evaluation) and closed-loop task success, where covariance estimation noise from $K{=}10$ samples undermines per-DOF conditioning.\n\n\\textbf{(3)~Correction magnitude control is critical and previously unrecognized.}\nWithout magnitude bounding, the per-DOF-conditioned CRM's natural output ($\\|\\boldsymbol{\\delta}\\|_2 \\approx 1.42$) causes catastrophic failure: 0\\% success on LIBERO-Spatial, as compounding correction errors rapidly drive the state distribution away from the CRM's training regime.\nConstraining corrections to $\\|\\boldsymbol{\\delta}\\|_2 \\leq 0.1$ recovers the full improvement.\n% exp_id: eval-acr-spatial-v4-default-r3 (norm=1.42, 0%), eval-acr-object-v4-obs-only (norm=0.1, 19.0%)\nObservation-conditioned CRM maintains stable 35--36\\% success on LIBERO-Spatial across $\\varepsilon \\in [0.05, 0.3]$, while per-DOF-conditioned CRM collapses from 35\\% to 26\\% over the same range. This robustness gap is the paper's strongest evidence: it holds across all tested seeds and magnitude bounds, independent of the seed-42 outlier.\n% exp_id: eval-mag-obsonly-norm005, eval-mag-obsonly-norm03, eval-mag-perdof-norm03\n\nWe note that correction offers targeted improvements on object-centric manipulation rather than universal gains: on LIBERO-Spatial, the best CRM variant performs within 1\\,pp of the selection baseline, suggesting that the correction mechanism is most effective when distribution shift induces systematic action biases that a learned module can identify and compensate.\n\n% --- Para 5: Contributions ---\nOur contributions are:\n\\begin{enumerate}[leftmargin=*,nosep]\n  \\item \\textbf{A sample-then-correct pipeline for frozen VLAs.}\n  We propose ACR-VLA, which combines conformal sample selection with learned residual correction for frozen flow-matching VLAs.\n  On LIBERO-Object, this pipeline significantly improves over the frozen VLA baseline (+6\\,pp, $p < 0.01$, 5-seed pooled test).\n  % obs_only eps=0.2 5-seed mean 17.0±2.8% vs VLA-only 4-seed mean 10.75±1.5%\n\n  \\item \\textbf{Systematic conditioning comparison and honest negative result.}\n  We compare three CRM conditioning variants (per-DOF conformal features, scalar uncertainty, and observation features) and find that only observation conditioning is effective.\n  This challenges the intuition that richer uncertainty features should yield better corrections, and reveals that covariance estimation noise at $K{=}10$ undermines per-DOF conditioning in closed-loop settings.\n\n  \\item \\textbf{Systematic empirical study of correction magnitude sensitivity for VLA action refinement.}\n  We show that unbounded correction causes catastrophic failure and that observation-conditioned CRM is uniquely robust across a $6{\\times}$ range of magnitude bounds ($\\varepsilon \\in [0.05, 0.3]$), establishing magnitude control as a critical design axis for inference-time action correction.\n\\end{enumerate}\n",
    "userModified": false
  }
}
```

</details>

---

### Assistant

_source line 23_

<details><summary>Logged reasoning block</summary>

```text
Now let me verify the file by reading it back, and check for any violations of the writing rules.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8146b578-f41a-49c2-b99a-be63bde75274",
  "uuid": "15ea7d21-e131-45a4-badd-0bfed281efc3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Pvjg7mt67zi6BJQmU9D8vU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2677,
      "cache_read_input_tokens": 57885,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2677
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Assistant

_source line 24_

Let me verify the output against the writing rules.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8146b578-f41a-49c2-b99a-be63bde75274",
  "uuid": "dd0d4d4c-2dbd-4237-9f5d-e5893db5bf3a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Pvjg7mt67zi6BJQmU9D8vU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2677,
      "cache_read_input_tokens": 57885,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2677
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 25_

<details open><summary>🔧 Tool call — Grep · `toolu_01TY4V68RMBYpdQgBtd129U5`</summary>

```json
{
  "pattern": "—",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/introduction.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8146b578-f41a-49c2-b99a-be63bde75274",
  "uuid": "b0654fed-2146-42c5-9dfe-db6fdf6f00a1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Pvjg7mt67zi6BJQmU9D8vU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2677,
      "cache_read_input_tokens": 57885,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2677
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-18T10:18:52.915Z_

<details><summary>↩ Tool result · `toolu_01TY4V68RMBYpdQgBtd129U5`</summary>

```text
19:% --- Para 3: Our approach — sample-then-correct ---
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8146b578-f41a-49c2-b99a-be63bde75274",
  "uuid": "bf2669c4-fa2d-41e4-88a2-f44a96c12d69",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "19:% --- Para 3: Our approach — sample-then-correct ---",
    "numLines": 1
  }
}
```

</details>

---

### Tool call

_source line 27_

<details open><summary>🔧 Tool call — Grep · `toolu_01N2anHm2K7SNi3QEsCHAahM`</summary>

```json
{
  "pattern": " – ",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/introduction.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8146b578-f41a-49c2-b99a-be63bde75274",
  "uuid": "67ffc746-082d-489b-bb68-5fd36c8f4e25",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Pvjg7mt67zi6BJQmU9D8vU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2677,
      "cache_read_input_tokens": 57885,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2677
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-18T10:18:53.882Z_

<details><summary>↩ Tool result · `toolu_01N2anHm2K7SNi3QEsCHAahM`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8146b578-f41a-49c2-b99a-be63bde75274",
  "uuid": "ab031e39-635c-48c6-b4d3-e6231b60574a",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "",
    "numLines": 0
  }
}
```

</details>

---

### Tool call

_source line 29_

<details open><summary>🔧 Tool call — Grep · `toolu_01JqHkMC2fkVgXYHBKMKKv4x`</summary>

```json
{
  "pattern": "ing,|ing\\.",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/introduction.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8146b578-f41a-49c2-b99a-be63bde75274",
  "uuid": "745658e9-1f82-4175-bd16-35ba13d9bd58",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Pvjg7mt67zi6BJQmU9D8vU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2677,
      "cache_read_input_tokens": 57885,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2677
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-18T10:18:55.238Z_

<details><summary>↩ Tool result · `toolu_01JqHkMC2fkVgXYHBKMKKv4x`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8146b578-f41a-49c2-b99a-be63bde75274",
  "uuid": "4a44cd49-9522-4bef-8f90-b6f1c7cffa49",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "",
    "numLines": 0
  }
}
```

</details>

---

### Tool call

_source line 31_

<details open><summary>🔧 Tool call — Grep · `toolu_01TjyP1rB7M9Djs77pyT4cvW`</summary>

```json
{
  "pattern": "Furthermore|Moreover|Additionally|delve|leverage|utilize|facilitate|It is worth noting|Notably",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/introduction.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8146b578-f41a-49c2-b99a-be63bde75274",
  "uuid": "a6734eef-d7c6-485c-bad5-d22f08f0ec99",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Pvjg7mt67zi6BJQmU9D8vU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2677,
      "cache_read_input_tokens": 57885,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2677
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-18T10:18:56.366Z_

<details><summary>↩ Tool result · `toolu_01TjyP1rB7M9Djs77pyT4cvW`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8146b578-f41a-49c2-b99a-be63bde75274",
  "uuid": "749ffb65-af4f-4dc3-ac59-d8b986bdcc9d",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "",
    "numLines": 0
  }
}
```

</details>

---

### Assistant

_source line 33_

<details><summary>Logged reasoning block</summary>

```text
The em-dash on line 19 is in a comment, not in the actual text. That's fine. All other checks pass. Let me also verify the file looks correct by reading it back.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8146b578-f41a-49c2-b99a-be63bde75274",
  "uuid": "4ab523cc-a518-4326-8f16-4bddbebec1be",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MnstyRNZ3PyyEYXLVy2wBg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 668,
      "cache_read_input_tokens": 60562,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 668
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Assistant

_source line 34_

The em-dash on line 19 is only in a LaTeX comment (`%`), not in rendered text. All writing rule checks pass: no em-dashes in text, no explanatory en-dashes, no -ing phrase endings, no blacklisted words.

The rewritten introduction:
- Follows the 5-paragraph + contributions structure exactly as specified
- Uses all D058-corrected terminology (L2 argmin selection, not Mahalanobis; CRM as correction module; ~327K params; ε=0.2 primary)
- Uses exact hard data numbers (17.5% vs 11.2%, +6.3pp, p=0.0074, d=1.21; K=1 10.3%; argmin 12.4%; obs_only 19% seed42; perdof collapse 14%→0%; OpenVLA 8/10 identical, variance <1e-30; spatial 30-35% null)
- De-emphasizes "conformal" (ACR-VLA not expanded; CRM name kept for consistency with method.tex but described functionally as a correction module)
- Includes spatial null result in finding (1) and contribution C3
- Every contribution has section/table/figure references
- All abbreviations (VLA, CRM) defined on first use
- ~780 words, targeting 1.5 pages

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8146b578-f41a-49c2-b99a-be63bde75274",
  "uuid": "886dad6f-0a5b-490f-9be0-cf95d803f51a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MnstyRNZ3PyyEYXLVy2wBg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 668,
      "cache_read_input_tokens": 60562,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 668
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Task result

_source line 35_

The em-dash on line 19 is only in a LaTeX comment (`%`), not in rendered text. All writing rule checks pass: no em-dashes in text, no explanatory en-dashes, no -ing phrase endings, no blacklisted words.

The rewritten introduction:
- Follows the 5-paragraph + contributions structure exactly as specified
- Uses all D058-corrected terminology (L2 argmin selection, not Mahalanobis; CRM as correction module; ~327K params; ε=0.2 primary)
- Uses exact hard data numbers (17.5% vs 11.2%, +6.3pp, p=0.0074, d=1.21; K=1 10.3%; argmin 12.4%; obs_only 19% seed42; perdof collapse 14%→0%; OpenVLA 8/10 identical, variance <1e-30; spatial 30-35% null)
- De-emphasizes "conformal" (ACR-VLA not expanded; CRM name kept for consistency with method.tex but described functionally as a correction module)
- Includes spatial null result in finding (1) and contribution C3
- Every contribution has section/table/figure references
- All abbreviations (VLA, CRM) defined on first use
- ~780 words, targeting 1.5 pages

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 193917,
  "duration_api_ms": 194934,
  "num_turns": 12,
  "stop_reason": "end_turn",
  "session_id": "8146b578-f41a-49c2-b99a-be63bde75274",
  "total_cost_usd": 0.6505197500000001,
  "usage": {
    "input_tokens": 7,
    "cache_creation_input_tokens": 49389,
    "cache_read_input_tokens": 205237,
    "output_tokens": 9475,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 49389,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 376,
        "cache_read_input_tokens": 60562,
        "cache_creation_input_tokens": 668,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 668
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2215,
      "outputTokens": 19,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.00231,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 7,
      "outputTokens": 9475,
      "cacheReadInputTokens": 205237,
      "cacheCreationInputTokens": 49389,
      "webSearchRequests": 0,
      "costUSD": 0.64820975,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "2795e51e-3f73-4e59-9e43-beec57d8f2f1"
}
```

</details>

---
